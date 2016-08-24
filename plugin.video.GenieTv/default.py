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
IiiIII111iI = "3.0.6"
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
O0o0Oo = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/imports/tvGuide/addon.py' ) )
Oo00OOOOO = o0oO0 . getLocalizedString
O0O = CookieJar ( )
O00o0OO = urllib2 . build_opener ( urllib2 . HTTPCookieProcessor ( O0O ) )
O00o0OO . addheaders = [ ( 'User-Agent' , 'Mozilla/5.0' ) ]
I11i1 = int ( sys . argv [ 1 ] )
iIi1ii1I1 = xbmc . translatePath ( o0oO0 . getAddonInfo ( 'profile' ) . decode ( 'utf-8' ) )
o0 = os . path . join ( iIii1 , 'favorites' )
I11II1i = iIii1 + '/addons.ini'
IIIII = xbmc . translatePath ( 'special://home/userdata/' )
ooooooO0oo = xbmc . translatePath ( 'special://home/userdatabroke/' )
IIiiiiiiIi1I1 = xbmc . translatePath ( 'special://home/addons/plugin.video.GenieTv' )
I1IIIii = xbmc . translatePath ( 'special://home/userdata/addon_data' )
oOoOooOo0o0 = I1IIIii + 'GenieTvWatched'
if not os . path . exists ( oOoOooOo0o0 ) :
 os . makedirs ( oOoOooOo0o0 )
OOOO = oOoOooOo0o0 + 'watched.txt'
if not os . path . exists ( OOOO ) :
 open ( OOOO , 'w+' )
OOO00 = open ( OOOO ) . read ( )
iiiiiIIii = ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9QYW5zQm94L09SSUdJTlMv' ) )
O000OO0 = xbmc . translatePath ( os . path . join ( 'special://home/userdata/addon_data/script.ivueguide/master.db' ) )
I11iii1Ii = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , 'favourites.xml' ) )
I1IIiiIiii = xbmc . translatePath ( os . path . join ( 'special://home/userdata/addon_data/plugin.video.GenieTv/favorites' ) )
O000oo0O = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/addon.xml' ) )
OOOOi11i1 = xbmc . translatePath ( os . path . join ( 'special://home/addons/repository.GenieTv/addon.xml' ) )
if os . path . exists ( o0 ) == True :
 IIIii1II1II = open ( o0 ) . read ( )
else : IIIii1II1II = [ ]
i1I1iI = o0oO0 . getSetting ( 'debug' )
if os . path . exists ( iIii1 ) == False :
 os . makedirs ( iIii1 )
def oo0OooOOo0 ( url ) :
 o0O = urllib2 . Request ( url )
 o0O . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
 O00oO = ''
 I11i1I1I = ''
 try :
  O00oO = urllib2 . urlopen ( o0O )
  I11i1I1I = O00oO . read ( )
  O00oO . close ( )
 except : pass
 if I11i1I1I != '' :
  return I11i1I1I
 else :
  I11i1I1I = 'Failed'
  return I11i1I1I
  if 83 - 83: OoOOOOO / iIi1i111II
OoOO00O = [ ]
oOOoO0O0O0 = oo0OooOOo0 ( i1111 ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby8=' ) )
if oOOoO0O0O0 != 'Failed' :
 OoOO00O . append ( i1111 ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby8=' ) )
if not oOOoO0O0O0 != 'Failed' :
 Oo000o = oo0OooOOo0 ( i1111 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20v' ) )
 if Oo000o != 'Failed' :
  OoOO00O . append ( i1111 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20v' ) )
 if not Oo000o != 'Failed' :
  I11IiI1I11i1i = oo0OooOOo0 ( i1111 ( 'aHR0cDovL2hlcm92aXNpb24ueDEwaG9zdC5jb20vaGVyb3Zpc2lvbi54MTBob3N0LmNvbS9HZW5pZVR2L3JlZG8v' ) )
  if I11IiI1I11i1i != 'Failed' :
   OoOO00O . append ( i1111 ( 'aHR0cDovL2hlcm92aXNpb24ueDEwaG9zdC5jb20vaGVyb3Zpc2lvbi54MTBob3N0LmNvbS9HZW5pZVR2L3JlZG8v' ) )
  if not I11IiI1I11i1i != 'Failed' :
   iI1ii1Ii = oo0OooOOo0 ( i1111 ( 'aHR0cDovLzUuMTM1LjEuNDYvcmVkby8=' ) )
   if iI1ii1Ii != 'Failed' :
    OoOO00O . append ( i1111 ( 'aHR0cDovLzUuMTM1LjEuNDYvcmVkby8=' ) )
else :
 pass
oooo000 = ( str ( OoOO00O ) ) . replace ( '[\'' , '' ) . replace ( '\']' , '' )
iIIIi1 = oooo000 + 'GenieArt/NEW/'
if 20 - 20: I1i1IiI1 + I1i1III % OO0O0OoOO0
if 10 - 10: i1I11i1I % Oo0o00
def O0O0oOO00O00o ( ) :
 if not os . path . exists ( IiII ) :
  oOOoo00O0O . ok ( "[COLOR=white]Incompatible[/COLOR]" , "Unfortunately GenieTv will only work with" , 'its official repo please install from trusted source' , '' )
  iI1ii11iIi1i = 'genie tv repo not being installed '
  iiI111I1iIiI ( iI1ii11iIi1i )
 else :
  IIIi1I1IIii1II ( )
  if 65 - 65: oOo . ooOoO0O00 % i1I11i1I / oOo0O0Ooo
def IIIi1I1IIii1II ( ) :
 if 15 - 15: i1I11i1I . iI11I1II1I1I . ii / Ii - I1i1III . ooOoO0O00
 i1O0OoO0o = OO0oOO0O ( i1111 ( 'aHR0cHM6Ly9naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvYmxvYi9tYXN0ZXIvVmVyc2lvbl9Mb2cudHh0' ) )
 oOiIi1IIIi1 = open ( O000oo0O ) . read ( )
 O0oOoOOOoOO = open ( OOOOi11i1 ) . read ( )
 if 38 - 38: Oo0o00
 Ii1 = re . compile ( 'version="(.+?)" provider' ) . findall ( oOiIi1IIIi1 )
 OOooOO000 = re . compile ( 'version="(.+?)" provider-name' ) . findall ( O0oOoOOOoOO )
 OOoOoo = re . compile ( 'GENIE TV ADDON - Version = &quot;(.+?)&quot;' ) . findall ( i1O0OoO0o )
 oO0000OOo00 = re . compile ( 'GENIE TV REPO - Version = &quot;(.+?)&quot;' ) . findall ( i1O0OoO0o )
 for iiIi1IIiIi in Ii1 :
  oOO00Oo = iiIi1IIiIi
  for i1iIIIi1i in OOoOoo :
   if not i1iIIIi1i == oOO00Oo :
    Oo0oO0ooo . create ( 'Incorrect Addon Version' , 'Downloading Correct Version' , )
    xbmc . sleep ( 1000 )
    Oo0oO0ooo . close
    iI1iIIiiii ( )
   if i1iIIIi1i == oOO00Oo :
    i1iI11i1ii11
 for OOooo0O00o in OOooOO000 :
  oOOoOooOo = OOooo0O00o
  for O000oo in oO0000OOo00 :
   if not O000oo == oOOoOooOo :
    Oo0oO0ooo . create ( 'Incorrect Repo Installed' , 'Installing Correct Version' , '' )
    xbmc . sleep ( 1000 )
    Oo0oO0ooo . close
    IIi1I11I1II ( )
   if O000oo == oOOoOooOo :
    xbmc . sleep ( 100 )
    i1iI11i1ii11
def OooOoooOo ( ) :
 O0O0oOO00O00o ( )
 ii11IIII11I ( )
 if 81 - 81: OOooOOo / o0o00Oo0O . i1I11i1I . oOo0O0Ooo
 OoOO ( '[COLOR' + oO0o0o0ooO0oO + ']SETTINGS[/COLOR]' , '' , 60000 , iIIIi1 + 'settings.png' , i1iIIi1 , '' )
 OoOO ( '[COLOR' + oO0o0o0ooO0oO + ']Force Genie Update Kodi 16+[/COLOR]' , i1111 ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVwby9yZXBvc2l0b3J5LkdlbmllVHYtMC4xLjAuemlw' ) , 10085 , iIIIi1 + 'GenieUpdate.png' , i1iIIi1 , '' )
 if o0oO0 . getSetting ( 'My Build' ) == 'true' :
  ooOOO0 ( '[COLOR' + oO0o0o0ooO0oO + ']WIZARD[/COLOR]' , str ( oooo000 ) , 4001 , iIIIi1 + 'Wizard.png' , i1iIIi1 , '' )
 if o0oO0 . getSetting ( 'Streams' ) == 'true' :
  ooOOO0 ( '[COLOR' + oO0o0o0ooO0oO + ']STREAMS[/COLOR]' , str ( oooo000 ) , 4002 , iIIIi1 + 'Streams.png' , i1iIIi1 , '' )
 if o0oO0 . getSetting ( 'Music' ) == 'true' :
  ooOOO0 ( '[COLOR' + oO0o0o0ooO0oO + ']Music[/COLOR]' , str ( oooo000 ) , 4003 , iIIIi1 + 'Music.png' , i1iIIi1 , '' )
  if 65 - 65: o0o00Oo0O
 if o0oO0 . getSetting ( 'Builders Toolbox' ) == 'true' :
  ooOOO0 ( '[COLOR' + oO0o0o0ooO0oO + ']BUILDERS TOOLBOX[/COLOR]' , str ( oooo000 ) , 32 , iIIIi1 + 'BuildersToolbox.png' , i1iIIi1 , '' )
 if o0oO0 . getSetting ( 'Source List' ) == 'true' :
  OoOO ( '[COLOR' + oO0o0o0ooO0oO + ']SOURCE LIST[/COLOR]' , str ( oooo000 ) , 46 , iIIIi1 + 'SoruceList.png' , i1iIIi1 , '' )
 if o0oO0 . getSetting ( 'Maintainance' ) == 'true' :
  ooOOO0 ( '[COLOR' + oO0o0o0ooO0oO + ']MAINTENANCE[/COLOR]' , str ( oooo000 ) , 3 , iIIIi1 + 'Maintenance.png' , i1iIIi1 , '' )
 if o0oO0 . getSetting ( 'Addons' ) == 'true' :
  ooOOO0 ( '[COLOR' + oO0o0o0ooO0oO + ']ADDONS[/COLOR]' , '' , 10050 , iIIIi1 + 'Addons.png' , i1iIIi1 , '' )
 if o0oO0 . getSetting ( 'APK Tool' ) == 'true' :
  ooOOO0 ( '[COLOR' + oO0o0o0ooO0oO + ']APK TOOL[/COLOR]' , str ( oooo000 ) , 30039 , iIIIi1 + 'APKTools.png' , i1iIIi1 , '' )
 if o0oO0 . getSetting ( 'Rss Feed' ) == 'true' :
  ooOOO0 ( '[COLOR' + oO0o0o0ooO0oO + ']GenieTv RSS Feed[/COLOR]' , str ( oooo000 ) , 39 , iIIIi1 + 'GenieTVRSSFeed.png' , i1iIIi1 , '' )
  if 68 - 68: iIi1i111II % Oo0o00
  if 88 - 88: iI11I1II1I1I - oOo + iIi1i111II
 IiI111111IIII ( 'movies' , 'MAIN' )
def i1Ii ( ) :
 ii111iI1iIi1 = wiz . log_check ( )
 OOO = ii111iI1iIi1 . replace ( LOG , "" )
 if os . path . exists ( ii111iI1iIi1 ) or not ii111iI1iIi1 == False :
  oo0OOo0 = open ( ii111iI1iIi1 , mode = 'r' ) ; I11IiI = oo0OOo0 . read ( ) ; oo0OOo0 . close ( )
  wiz . TextBoxes ( "%s - %s" % ( ADDONTITLE , OOO ) , I11IiI )
 else :
  wiz . LogNotify ( 'View Log' , 'No Log File Found!' )
def O0ooO0Oo00o ( ) :
 O0O0oOO00O00o ( )
 ooOOO0 ( '[COLOR' + oO0o0o0ooO0oO + ']BACKUP MY BUILD[/COLOR]' , str ( oooo000 ) , 10060 , iIIIi1 + 'BackupMyBuild.png' , i1iIIi1 , '' )
 ooOOO0 ( '[COLOR' + oO0o0o0ooO0oO + ']RESTORE MY BUILD[/COLOR]' , str ( oooo000 ) , 49 , iIIIi1 + 'RestoreMyBuild.png' , i1iIIi1 , '' )
 ooOOO0 ( '[COLOR' + oO0o0o0ooO0oO + ']WIPE GENIE[/COLOR]' , str ( oooo000 ) , 41 , iIIIi1 + 'WipeGenie.png' , i1iIIi1 , '' )
 if 77 - 77: iI11I1II1I1I * oO0o
 ooOOO0 ( '[COLOR' + oO0o0o0ooO0oO + ']Genie BUILDS[/COLOR]' , str ( oooo000 ) , 44 , iIIIi1 + 'GenieBuilds.png' , i1iIIi1 , '' )
 IiI111111IIII ( 'movies' , 'MAIN' )
def oOooOo0 ( ) :
 O0O0oOO00O00o ( )
 if i1iiIIiiI111 == '5knuckleshuffle' :
  ooOOO0 ( '[COLOR' + oO0o0o0ooO0oO + ']XVID[/COLOR]' , str ( oooo000 ) , 10100 , iIIIi1 + 'Jizbox.png' , i1iIIi1 , '' )
  ooOOO0 ( '[COLOR' + oO0o0o0ooO0oO + ']ADULT CHANNELS[/COLOR]' , str ( oooo000 ) , 30033 , iIIIi1 + 'adu.png' , i1iIIi1 , '' )
 if o0oO0 . getSetting ( 'Favourites' ) == 'true' :
  ooOOO0 ( '[COLOR' + oO0o0o0ooO0oO + ']FAVOURITES[/COLOR]' , str ( oooo000 ) , 10057 , iIIIi1 + 'Favourites.png' , i1iIIi1 , '' )
 if o0oO0 . getSetting ( 'Search' ) == 'true' :
  ooOOO0 ( '[COLOR' + oO0o0o0ooO0oO + ']SEARCH[/COLOR]' , str ( oooo000 ) , 9000 , iIIIi1 + 'Search.png' , i1iIIi1 , '' )
 ooOOO0 ( '[COLOR' + oO0o0o0ooO0oO + ']G-Tv Live List[/COLOR]' , '' , 4009 , iIIIi1 + 'GTV.png' , i1iIIi1 , '' )
 if o0oO0 . getSetting ( 'TV GUIDE' ) == 'true' :
  OoOO ( '[COLOR' + oO0o0o0ooO0oO + ']TV GUIDE[/COLOR]' , '' , 10063 , iIIIi1 + 'TvGuide.png' , i1iIIi1 , '' )
  if 38 - 38: Oo0o00
 ooOOO0 ( '[COLOR' + oO0o0o0ooO0oO + ']STREAM TEAM[/COLOR]' , str ( oooo000 ) , 4006 , iIIIi1 + 'StreamTeam.png' , i1iIIi1 , '' )
 ooOOO0 ( '[COLOR' + oO0o0o0ooO0oO + ']MOVIES[/COLOR]' , str ( oooo000 ) , 4004 , iIIIi1 + 'Movies.png' , i1iIIi1 , '' )
 ooOOO0 ( '[COLOR' + oO0o0o0ooO0oO + ']TV SHOWS[/COLOR]' , str ( oooo000 ) , 4005 , iIIIi1 + 'TVShows.png' , i1iIIi1 , '' )
 if o0oO0 . getSetting ( 'Football' ) == 'true' :
  ooOOO0 ( '[COLOR' + oO0o0o0ooO0oO + ']FOOTBALL[/COLOR]' , '' , 10002 , iIIIi1 + 'Football.png' , i1iIIi1 , '' )
 ooOOO0 ( '[COLOR' + oO0o0o0ooO0oO + ']KIDS[/COLOR]' , str ( oooo000 ) , 4007 , iIIIi1 + 'Kids.png' , i1iIIi1 , '' )
 ooOOO0 ( '[COLOR' + oO0o0o0ooO0oO + ']24/7 STREAMS[/COLOR]' , '' , 30030 , iIIIi1 + '247Streams.png' , i1iIIi1 , '' )
 ooOOO0 ( '[COLOR' + oO0o0o0ooO0oO + ']NEWS[/COLOR]' , str ( oooo000 ) , 30032 , iIIIi1 + 'News.png' , i1iIIi1 , '' )
 ooOOO0 ( '[COLOR' + oO0o0o0ooO0oO + ']GenieTv TUTORIALS[/COLOR]' , ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9pVHZfU3RyZWFtcy9UVVRTL21haW4ucGhw' ) ) , 1016 , iIIIi1 + 'GenieTVTutorials.png' , i1iIIi1 , '' )
 ooOOO0 ( '[COLOR' + oO0o0o0ooO0oO + ']HOBBIES[/COLOR]' , str ( oooo000 ) , 4008 , iIIIi1 + 'Hobbies.png' , i1iIIi1 , '' )
 if o0oO0 . getSetting ( 'YOUTUBE' ) == 'true' :
  ooOOO0 ( '[COLOR' + oO0o0o0ooO0oO + ']SEARCH YOUTUBE[/COLOR]' , str ( oooo000 ) , 10064 , iIIIi1 + 'SeachYouTube.png' , i1iIIi1 , '' )
 if o0oO0 . getSetting ( 'REQUESTS' ) == 'true' :
  ooOOO0 ( '[COLOR' + oO0o0o0ooO0oO + ']REQUESTS[/COLOR]' , str ( oooo000 ) + ( i1111 ( 'L1JFUVVFU1RTLnBocA==' ) ) , 10066 , iIIIi1 + 'Requests.png' , i1iIIi1 , '' )
 if o0oO0 . getSetting ( 'Stand Up' ) == 'true' :
  ooOOO0 ( '[COLOR' + oO0o0o0ooO0oO + ']STAND UP[/COLOR]' , '' , 10003 , iIIIi1 + 'StandUp.png' , i1iIIi1 , '' )
 if o0oO0 . getSetting ( 'Documentaries' ) == 'true' :
  ooOOO0 ( '[COLOR' + oO0o0o0ooO0oO + ']DOCUMENTARIES[/COLOR]' , str ( oooo000 ) , 8040 , iIIIi1 + 'documentaries.png' , i1iIIi1 , '' )
 if o0oO0 . getSetting ( 'Disclose' ) == 'true' :
  ooOOO0 ( '[COLOR' + oO0o0o0ooO0oO + ']DISCLOSE TV[/COLOR]' , str ( oooo000 ) , 7001 , iIIIi1 + 'DiscloseTV.png' , i1iIIi1 , '' )
  if 84 - 84: iI11I1II1I1I % OO0O0OoOO0 / iI11I1II1I1I % I1i1IiI1
  if 45 - 45: o0o00Oo0O
 if o0oO0 . getSetting ( 'Playlist Loader' ) == 'true' :
  ooOOO0 ( '[COLOR' + oO0o0o0ooO0oO + ']PLAYLIST LOADER[/COLOR]' , str ( oooo000 ) , 3000 , iIIIi1 + 'PlaylistLoader.png' , i1iIIi1 , '' )
  if 26 - 26: I1i1IiI1 - iI11I1II1I1I - oOo0O0Ooo / oO0o . OOooOOo % iI11I1II1I1I
  if 91 - 91: I11i . iI11I1II1I1I / OoOOOOO + ooOoO0O00
  if 42 - 42: oOo . I11i . oOo - Ii1I
  if 40 - 40: oOo - Ii / I1i1III
  if 35 - 35: I1i1III - oOo0O0Ooo % I11i . ii % I1i1III
  if 47 - 47: OO0O0OoOO0 - I1i1III . IIiIiII11i + ii . Ii
  if 94 - 94: I11i * I1i1III / I1ii11iIi11i / I1i1III
  if 87 - 87: I1ii11iIi11i . i1I11i1I
  if 75 - 75: oOo + OOooOOo + I11i * I1i1IiI1 % OoOOOOO . OO0O0OoOO0
  if 55 - 55: iIi1i111II . oOo0O0Ooo
  if 61 - 61: I1ii11iIi11i % i1I11i1I . I1ii11iIi11i
  if 100 - 100: Oo0o00 * o0o00Oo0O
 IiI111111IIII ( 'movies' , 'MAIN' )
 if 64 - 64: iIi1i111II % iI11I1II1I1I * OoOOOOO
def ii11IIII11I ( ) :
 if not os . path . exists ( II ) :
  o0iI11I1II ( 'Change Log 6/8/16 - v3.0.6' , 'G-Tv and Ultimate integrated into GenieTv, Ultimate option in guide settings, Settings button added, all searches updated, new servers online' )
  os . makedirs ( II )
  if 40 - 40: iI11I1II1I1I / OOooOOo % Ii1I + IIiIiII11i
  if 27 - 27: IIiIiII11i * OOooOOo * iI11I1II1I1I
def oOo00oOoO000 ( ) :
 O0O0oOO00O00o ( )
 ooOOO0 ( '[COLOR' + oO0o0o0ooO0oO + ']SEARCH MOVIES[/COLOR]' , str ( oooo000 ) , 9001 , iIIIi1 + 'Search.png' , i1iIIi1 , '' )
 if o0oO0 . getSetting ( 'Popcorn Box' ) == 'true' :
  ooOOO0 ( '[COLOR' + oO0o0o0ooO0oO + ']POPCORN BOX[/COLOR]' , str ( oooo000 ) , 7061 , iIIIi1 + 'PopcornBox.png' , i1iIIi1 , '' )
 ooOOO0 ( '[COLOR' + oO0o0o0ooO0oO + ']Film Trailers[/COLOR]' , i1111 ( 'aHR0cDovL3RoZW1vdmllYm94Lm5ldC9leHBsb3Jl' ) , 10068 , iIIIi1 + 'FilmTrailers.png' , i1iIIi1 , '' )
 if o0oO0 . getSetting ( 'CLASSIC MOVIES' ) == 'true' :
  ooOOO0 ( '[COLOR' + oO0o0o0ooO0oO + ']CLASSIC MOVIES[/COLOR]' , '' , 8060 , iIIIi1 + 'ClassicMovies.png' , i1iIIi1 , '' )
 IiI111111IIII ( 'movies' , 'MAIN' )
def OOooo0oOO0O ( ) :
 O0O0oOO00O00o ( )
 o00O0 ( )
 if 83 - 83: oOo
 if 65 - 65: oOo0O0Ooo % I1i1III * OoOOOOO
 ooOOO0 ( '[COLOR' + oO0o0o0ooO0oO + ']Football On G-Tv[/COLOR]' , ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 7080 , iIIIi1 + 'TodaysMacthes.png' , i1iIIi1 , '' )
 if o0oO0 . getSetting ( 'TV GUIDE' ) == 'true' :
  OoOO ( '[COLOR' + oO0o0o0ooO0oO + ']TV GUIDE[/COLOR]' , '' , 10063 , iIIIi1 + 'TvGuide.png' , i1iIIi1 , '' )
 OoOO ( '[COLOR' + oO0o0o0ooO0oO + ']Link GTV to Guide[/COLOR]' , '' , 4010 , iIIIi1 + 'linkchannels.png' , i1iIIi1 , '' )
 if 19 - 19: Oo0o00 + iI11I1II1I1I . ii . I1i1IiI1 / Oo0o00 + i1I11i1I
 if 85 - 85: Ii1I - iI11I1II1I1I
def Ii1iI1I1 ( ) :
 O0O0oOO00O00o ( )
 ooOOO0 ( '[COLOR' + oO0o0o0ooO0oO + ']SEARCH SERIES[/COLOR]' , str ( oooo000 ) , 9002 , iIIIi1 + 'Search.png' , i1iIIi1 , '' )
 if 57 - 57: Ii . Ii1I - I1i1III - OoOOOOO + OOooOOo
 if 63 - 63: OOooOOo * OO0O0OoOO0
 if o0oO0 . getSetting ( 'Watch Series' ) == 'true' :
  ooOOO0 ( '[COLOR' + oO0o0o0ooO0oO + ']WATCH SERIES[/COLOR]' , '' , 10040 , iIIIi1 + 'WatchSeries.png' , i1iIIi1 , '' )
 ooOOO0 ( '[COLOR' + oO0o0o0ooO0oO + ']iWATCH SERIES[/COLOR]' , '' , 8020 , iIIIi1 + 'iWatchSeries.png' , i1iIIi1 , '' )
 if 69 - 69: o0o00Oo0O . oO0o
 if 49 - 49: oOo0O0Ooo - I1i1IiI1
 if o0oO0 . getSetting ( 'CLASSIC TV' ) == 'true' :
  ooOOO0 ( '[COLOR' + oO0o0o0ooO0oO + ']CLASSIC TV[/COLOR]' , str ( oooo000 ) , 8064 , iIIIi1 + 'ClassicTV.png' , i1iIIi1 , '' )
 ooOOO0 ( '[COLOR' + oO0o0o0ooO0oO + ']TV Show Trailers[/COLOR]' , i1111 ( 'aHR0cHM6Ly93d3cueW91dHViZS5jb20vd2F0Y2g/dj03WkZJUzJBcUF6OCZsaXN0PVBMM2t4NWgyVHJZR3dwVzBWYk5lbnBqLUJLTUJUR2dKUEU=' ) , 10069 , iIIIi1 + 'TVShowTrailers.png' , i1iIIi1 , '' )
 if 74 - 74: iI11I1II1I1I * Ii1I + OOooOOo / ooOoO0O00 / IIiIiII11i . I1ii11iIi11i
 IiI111111IIII ( 'movies' , 'MAIN' )
def oooOo0OOOoo0 ( ) :
 O0O0oOO00O00o ( )
 if o0oO0 . getSetting ( 'Silent Hunter' ) == 'true' :
  ooOOO0 ( '[COLOR' + oO0o0o0ooO0oO + ']SILENT HUNTER[/COLOR]' , ( i1111 ( 'aHR0cDovL2dlbmlldHYuY28udWsvc2lsZW50aHVudGVyL2xpc3RzL21haW4ucGhw' ) ) , 1016 , iIIIi1 + 'SilentHunter.png' , i1iIIi1 , '' )
 if o0oO0 . getSetting ( 'The Reaper' ) == 'true' :
  ooOOO0 ( '[COLOR' + oO0o0o0ooO0oO + ']THE REAPER[/COLOR]' , ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9UaGVfUmVhcGVyL21haW4ucGhw' ) ) , 1016 , iIIIi1 + 'TheReaper.png' , i1iIIi1 , '' )
 if o0oO0 . getSetting ( 'Pandoras Box' ) == 'true' :
  ooOOO0 ( '[COLOR' + oO0o0o0ooO0oO + ']PANDORAS BOX[/COLOR]' , str ( oooo000 ) , 10025 , iIIIi1 + 'PandorasBox.png' , i1iIIi1 , '' )
 if o0oO0 . getSetting ( 'Redemption Streams' ) == 'true' :
  ooOOO0 ( '[COLOR' + oO0o0o0ooO0oO + ']Redemption Streams[/COLOR]' , ( i1111 ( 'aHR0cDovL3JlZGVtcHRpb25zdHJlYW1zLmNvLnVrL1JlZGVtcHRpb24vbWFpbi5waHA=' ) ) , 1016 , iIIIi1 + 'RedemptionStreams.png' , i1iIIi1 , '' )
 ooOOO0 ( '[COLOR' + oO0o0o0ooO0oO + ']DoJo STREAMS[/COLOR]' , ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9kb2pvc3RyZWFtcy9tYWluLnBocA==' ) ) , 1016 , iIIIi1 + 'DojoStreams.png' , i1iIIi1 , '' )
 if o0oO0 . getSetting ( 'Scooby Streams' ) == 'true' :
  ooOOO0 ( '[COLOR' + oO0o0o0ooO0oO + ']SCOOBY STREAMS[/COLOR]' , str ( oooo000 ) , 1023 , iIIIi1 + 'ScoobyStreams.png' , i1iIIi1 , '' )
 if o0oO0 . getSetting ( 'HeroVision' ) == 'true' :
  ooOOO0 ( '[COLOR' + oO0o0o0ooO0oO + ']HEROVISION[/COLOR]' , '' , 1017 , iIIIi1 + 'Herovision.png' , i1iIIi1 , '' )
 ooOOO0 ( '[COLOR' + oO0o0o0ooO0oO + ']ITV[/COLOR]' , ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9pVHZfU3RyZWFtcy9tYWluLnBocA==' ) ) , 1016 , iIIIi1 + 'ITVStreams.png' , i1iIIi1 , '' )
 if 51 - 51: I1ii11iIi11i / OOooOOo . iIi1i111II * I11i + oO0o * i1I11i1I
 IiI111111IIII ( 'movies' , 'MAIN' )
 if 73 - 73: oO0o + ii - o0o00Oo0O - I1i1III - IIiIiII11i
def O0Oo0oOOoooOOOOo ( ) :
 O0O0oOO00O00o ( )
 OoOO ( '[COLOR' + oO0o0o0ooO0oO + ']SILENT HUNTER[/COLOR]' , ( i1111 ( 'aHR0cDovLzUuMTM1LjIwNy45Ni8=' ) ) , 1006 , iIIIi1 + 'SilentHunter.png' , i1iIIi1 , '' )
 ooOOO0 ( '[COLOR' + oO0o0o0ooO0oO + ']SERVER 1[/COLOR]' , ( i1111 ( 'aHR0cDovLzUuMTM1LjIwNy45Ni8=' ) ) , 1018 , iIIIi1 + 'SilentHunter.png' , i1iIIi1 , '' )
 ooOOO0 ( '[COLOR' + oO0o0o0ooO0oO + ']SERVER 2[/COLOR]' , ( i1111 ( 'aHR0cDovL3NpbGVudGh1bnRlci5zcnZlLmlvLw==' ) ) , 1018 , iIIIi1 + 'SilentHunter.png' , i1iIIi1 , '' )
 ooOOO0 ( '[COLOR' + oO0o0o0ooO0oO + ']SCRAPES[/COLOR]' , ( i1111 ( 'aHR0cDovLzUuMTM1LjIwNy45Ni9TY3JhcGVzL21haW4ucGhw' ) ) , 1016 , iIIIi1 + 'SilentHunter.png' , i1iIIi1 , '' )
def o0oO0O0o0O00O ( url ) :
 OoO000O0Oo = Oo0o0oooo0O0 ( url )
 url = url
 Ii1 = re . compile ( 'alt="([^"]*)"></td><td><a href="([^"]*)".+?</td><td align=' ) . findall ( OoO000O0Oo )
 for OooooOOoo0 , i1I1IiiIi1i in Ii1 :
  if '[DIR]' in OooooOOoo0 :
   iiI11ii1I1 ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + i1I1IiiIi1i + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mkv' , '' ) , url + i1I1IiiIi1i , 1018 , iIIIi1 + 'SilentHunter.png' )
  if 'mkv' in i1I1IiiIi1i :
   Ooo0OOoOoO0 ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + i1I1IiiIi1i + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mkv' , '' ) , url + i1I1IiiIi1i , 222 , iIIIi1 + 'SilentHunter.png' )
  if 'avi' in i1I1IiiIi1i :
   Ooo0OOoOoO0 ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + i1I1IiiIi1i + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mkv' , '' ) , url + i1I1IiiIi1i , 222 , iIIIi1 + 'SilentHunter.png' )
   if 70 - 70: OoOOOOO
def oOOoO0o0oO ( ) :
 ooOOO0 ( '[COLOR' + oO0o0o0ooO0oO + ']HEROVISION[/COLOR]' , ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC9tYWluLnBocA==' ) ) , 1016 , iIIIi1 + 'Herovision.png' , i1iIIi1 , '' )
 ooOOO0 ( '[COLOR' + oO0o0o0ooO0oO + ']HEROVISION SCRAPES[/COLOR]' , ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC9zY3JhcGVkL3NjcmFwZWQucGhw' ) ) , 1024 , iIIIi1 + 'Herovision.png' , i1iIIi1 , '' )
 if 93 - 93: i1I11i1I * ii + oOo
def IiII111i1i11 ( ) :
 O0O0oOO00O00o ( )
 ooOOO0 ( '[COLOR' + oO0o0o0ooO0oO + ']SEARCH CARTOONS[/COLOR]' , '' , 10005 , iIIIi1 + 'SearchCartoons.png' , i1iIIi1 , '' )
 if o0oO0 . getSetting ( 'WCO' ) == 'true' :
  ooOOO0 ( '[COLOR' + oO0o0o0ooO0oO + ']WATCH CARTOONS ONLINE[/COLOR]' , str ( oooo000 ) , 21004 , iIIIi1 + 'watchcartoons.png' , i1iIIi1 , '' )
 if o0oO0 . getSetting ( 'Cartoons' ) == 'true' :
  ooOOO0 ( '[COLOR' + oO0o0o0ooO0oO + ']CARTOONS[/COLOR]' , '' , 10001 , iIIIi1 + 'Cartoons.png' , i1iIIi1 , '' )
 if o0oO0 . getSetting ( 'Anime' ) == 'true' :
  ooOOO0 ( '[COLOR' + oO0o0o0ooO0oO + ']AnimeLand[/COLOR]' , ( i1111 ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2R1YmJlZC1hbmltZQ==' ) ) , 10004 , iIIIi1 + 'anime.png' , i1iIIi1 , '' )
 IiI111111IIII ( 'movies' , 'MAIN' )
def i111iIi1i1II1 ( ) :
 O0O0oOO00O00o ( )
 if o0oO0 . getSetting ( 'Football' ) == 'true' :
  ooOOO0 ( '[COLOR' + oO0o0o0ooO0oO + ']FOOTBALL[/COLOR]' , '' , 10002 , iIIIi1 + 'Football.png' , i1iIIi1 , '' )
 if o0oO0 . getSetting ( 'Fitness' ) == 'true' :
  ooOOO0 ( '[COLOR' + oO0o0o0ooO0oO + ']FITNESS[/COLOR]' , ( i1111 ( 'aHR0cHM6Ly93d3cuZml0bmVzc2JsZW5kZXIuY29tL3ZpZGVvcw==' ) ) , 7085 , iIIIi1 + 'Fitness.png' , i1iIIi1 , '' )
 if o0oO0 . getSetting ( 'Go Fishing' ) == 'true' :
  ooOOO0 ( '[COLOR' + oO0o0o0ooO0oO + ']Go Fishing[/COLOR]' , str ( oooo000 ) , 8090 , iIIIi1 + 'GoFishing.png' , i1iIIi1 , '' )
 if o0oO0 . getSetting ( 'GenieTv Kitchen' ) == 'true' :
  ooOOO0 ( '[COLOR' + oO0o0o0ooO0oO + ']GenieTv Kitchen[/COLOR]' , ( i1111 ( 'aHR0cDovL2Zvb2QubmR0di5jb20vdmlkZW9z' ) ) , 8045 , iIIIi1 + 'GenieTVKitchen.png' , i1iIIi1 , '' )
 IiI111111IIII ( 'movies' , 'MAIN' )
 if 86 - 86: iI11I1II1I1I / OOooOOo . IIiIiII11i
 if 19 - 19: Ii1I % ii % i1I11i1I * I11i % o0o00Oo0O
 if 67 - 67: oOo0O0Ooo . ooOoO0O00
def i1iI11i1ii11 ( ) :
 oOOoO0O0O0 = OO0oOO0O ( 'http://genietv.co.uk/genietv_art/testdelete.txt' )
 Ii1 = re . compile ( '<unwanted_addon =(.+?)</unwanted_addon>' ) . findall ( oOOoO0O0O0 )
 for iI1ii11iIi1i in Ii1 :
  iI1ii11iIi1i = ( str ( iI1ii11iIi1i ) )
  if os . path . exists ( xbmc . translatePath ( iI1ii11iIi1i ) ) :
   i1i1iI1iiiI = ( iI1ii11iIi1i ) . replace ( 'special://home/addons/' , '' )
   o0iI11I1II ( "Please remove any addons or repo's that may alter Genie Tv coding without your knowledge" , "It has been recognised you have \n[COLORred]" + i1i1iI1iiiI + "[/COLOR]\n installed on your system. In order for genie to function this addon must be removed. \n\nThere have been 'creative differences' between ourselves and this addon. Initially we just stopped our addon from working if this addon was installed, but when private talks were undertaken the 'author' (we use this term very lightly) of this addon gave us a choice, either remove our block or they will tamper with our addon, they then saw fit to host our addon and begin pushing unwanted and unauthorised, potentially malicious updates (we've no idea what they altered and with there approach anything could be possible) so we took steps to remove this addon purely for your protection from alterations to code from, self confessed, unskilled individuals. \n\nHowever the approach we took i guess can be seen as malicious because we did not inform you of actions that altered your device without your knowledge (bar a popup telling you this was happening), for this we apologise, it was a major oversight on our part and made us no better than them. \n\nAll are free to continue to use genie tv at no cost but you must make a decision. A box will soon open and you will need to choose remove or close. If you choose remove you are accepting to remove these addons that we believe have the potential to maliciously alter your device from an unofficial source or if you press close it will close genie, it will not be useable until these addons are remove and you can chose to use whatever addon you see fit at your own risk. \n\nThis is not 'playing god' please dont see it that way but merely protecting our hard work and in the end your experience from this.  We hope this issue resolves itself and things return to normality as much as, if not more than, yourself. Please wait to decide what action you wish to take" )
   xbmc . sleep ( 40000 )
   Ooo0oOooo0 = xbmcgui . Dialog ( ) . yesno ( 'Remove Potentially Harmful Addons' , 'Remove will remove addons known to alter genie tv' , 'Close will stop genie tv working to protect' , 'you from any potential unwanted updates' , nolabel = 'Close' , yeslabel = 'Remove' )
   if Ooo0oOooo0 == 0 :
    iiI111I1iIiI ( iI1ii11iIi1i )
    oOOOoo00 ( )
   elif Ooo0oOooo0 == 1 :
    iiIiIIIiiI ( iI1ii11iIi1i )
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
 if 81 - 81: OOooOOo - OOooOOo . OO0O0OoOO0
def iiI111I1iIiI ( addon ) :
 oOOoo00O0O . ok ( "[COLOR=white]Incompatible[/COLOR]" , "Unfortunately GenieTv will not work with" , addon , 'please remove then reinstall genie' )
 o0OoOo00o0o = os . path . join ( iiI1IiI , 'default.py' )
 I1II1I11I1I = open ( o0OoOo00o0o , "w+" )
 if 54 - 54: ii + I11i - ooOoO0O00 % Ii
 I1II1I11I1I . write ( r'Genie Tv will not work with certain addons in an attempt to bring you original content from the best developers' )
 I1II1I11I1I . write ( r'and not those simply out to profit or make a name for themselves off others work' )
 I1II1I11I1I . write ( r'Please remove' + unwanted_addons + 'if you would like to use genie tv then uninstall and reinstall from official repo' )
 if 3 - 3: I11i % I11i
 if 83 - 83: IIiIiII11i + Oo0o00
 if 73 - 73: OO0O0OoOO0
 if 42 - 42: Ii * iI11I1II1I1I / Ii1I . Ii % I1i1IiI1
 if 41 - 41: i1I11i1I / o0o00Oo0O
 if 51 - 51: I1i1IiI1 % oOo0O0Ooo
 if 60 - 60: oOo0O0Ooo / iIi1i111II . oOo0O0Ooo / Oo0o00 . i1I11i1I
 if 92 - 92: OOooOOo + Oo0o00 * I1i1III % oOo0O0Ooo
 if 42 - 42: I1ii11iIi11i
 if 76 - 76: oOo0O0Ooo * OO0O0OoOO0 % Oo0o00
 if 57 - 57: iI11I1II1I1I - ooOoO0O00 / Oo0o00 - o0o00Oo0O * ii % IIiIiII11i
 if 68 - 68: ii * I1i1IiI1 % OOooOOo - i1I11i1I
 if 34 - 34: Oo0o00 . iI11I1II1I1I * OOooOOo * OoOOOOO / Oo0o00 / Ii1I
 if 78 - 78: I1ii11iIi11i - I11i / OOooOOo
 if 10 - 10: OO0O0OoOO0 + I1ii11iIi11i * Ii1I + iI11I1II1I1I / Oo0o00 / Ii1I
 if 42 - 42: oOo0O0Ooo
 if 38 - 38: iIi1i111II + IIiIiII11i % oOo % OOooOOo - I1i1III / ii
 if 73 - 73: I11i * o0o00Oo0O - Ii
 if 85 - 85: I1i1III % OO0O0OoOO0 + I1i1IiI1 / I11i . OoOOOOO + iIi1i111II
def ooOoOo0 ( ) :
 ooOOO0 ( 'Genre' , i1111 ( 'aHR0cDovL2ltb3ZpZW1heC5zZS9tb3ZpZXMv' ) , 10073 , iIIIi1 + 'genievision.png' , i1iIIi1 , '' )
 ooOOO0 ( 'Most Viewed' , i1111 ( 'aHR0cDovL2ltb3ZpZW1heC5zZS9tb3ZpZXMv' ) , 10077 , iIIIi1 + 'genievision.png' , i1iIIi1 , '' )
 ooOOO0 ( 'Box Office' , i1111 ( 'aHR0cDovL2ltb3ZpZW1heC5zZS9jYXRlZ29yeS9ib3gtb2ZmaWNlLw==' ) , 10074 , iIIIi1 + 'genievision.png' , i1iIIi1 , '' )
 ooOOO0 ( 'Search' , '' , 10078 , iIIIi1 + 'genievision.png' , i1iIIi1 , '' )
 if 2 - 2: OO0O0OoOO0 % iI11I1II1I1I * iI11I1II1I1I . I11i / OO0O0OoOO0
def iII1i1 ( ) :
 O0oOOoooOO0O = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 ooo00Ooo = 'http://imoviemax.se/?s=' + ( O0oOOoooOO0O ) . replace ( ' ' , '+' )
 Oo0o0O00 = ooo00Ooo . lower ( )
 ii1 ( Oo0o0O00 )
def I1i11 ( url ) :
 OO = [ ]
 oOOoO0O0O0 = OO0oOO0O ( url )
 Ii1 = re . compile ( '<li class="cat-item cat-item-.+? "><a href="(.+?)">(.+?)</a><i>(.+?)</i></li>' ) . findall ( oOOoO0O0O0 )
 for url , o0O0oo0OO0O , OO0 in Ii1 :
  if o0O0oo0OO0O in OO :
   pass
  else :
   ooOOO0 ( o0O0oo0OO0O + ' - ' + OO0 + ' Films' , url , 10074 , iIIIi1 + 'genievision.png' , i1iIIi1 , '' )
   OO . append ( o0O0oo0OO0O )
   if 72 - 72: ii
def OooooOoooO ( url ) :
 oOOoO0O0O0 = OO0oOO0O ( url )
 Ii1 = re . compile ( '<li>.+?<b>.+?</b>.+?<a href="(.+?)">(.+?)</a>.+?<span>(.+?)</span>' , re . DOTALL ) . findall ( oOOoO0O0O0 )
 for url , o0O0oo0OO0O , oOIIiIi in Ii1 :
  ooOOO0 ( o0O0oo0OO0O + ' - Views:' + oOIIiIi , url , 10075 , iIIIi1 + 'genievision.png' , i1iIIi1 , '' )
  if 91 - 91: Ii1I * I1ii11iIi11i / oOo0O0Ooo . o0o00Oo0O + oO0o + OOooOOo
  if 8 - 8: OoOOOOO / Ii1I
def ii1 ( url ) :
 i1iI1 = [ ]
 oOOoO0O0O0 = OO0oOO0O ( url )
 next = re . compile ( "<link rel='next' href='(.+?)' />" ) . findall ( oOOoO0O0O0 )
 for next in next :
  ooOOO0 ( 'NEXT PAGE' , next , 10074 , iIIIi1 + 'Next.png' , i1iIIi1 , '' )
 Ii1 = re . compile ( '<div class="movie">.+?<img src="(.+?)" alt="(.+?)" />.+?<a href="(.+?)"><span class="player"></span></a>' , re . DOTALL ) . findall ( oOOoO0O0O0 )
 for i11ii1ii11i , o0O0oo0OO0O , url in Ii1 :
  ooOOO0 ( o0O0oo0OO0O , url , 10075 , i11ii1ii11i , i11ii1ii11i , '' )
  i1iI1 . append ( o0O0oo0OO0O )
  if 70 - 70: ooOoO0O00 - OO0O0OoOO0 + I1ii11iIi11i
def II1I1I1Ii ( img , name , url ) :
 img = img
 name = name
 oOOoO0O0O0 = OO0oOO0O ( url )
 Ii1 = re . compile ( '<div id="(.+?)" class="player-content"><iframe class="playerframe" src="(.+?)" scrolling="no".+?</iframe></div>' ) . findall ( oOOoO0O0O0 )
 for OOOOoO00o0O , url in Ii1 :
  print '>>>>>>>>>>>>>>>>>>>>>>>>>>> before' + url
  I1I1I1IIi1III = ( url ) . replace ( 'player' , 'watch' ) + '&fv=&sou='
  print '<<<<<<<<<<<<<<<<<<<<<<<<<<< after' + I1I1I1IIi1III
  II11IiiIII = ( OOOOoO00o0O ) . replace ( 'play-' , 'Server ' )
  OoOO ( II11IiiIII , I1I1I1IIi1III , 10076 , img , img , '' )
  if 58 - 58: I1i1III + I11i - oOo0O0Ooo
def i1i1ii ( url ) :
 oOOoO0O0O0 = OO0oOO0O ( url )
 Ii1 = re . compile ( '<source src="(.+?)" type="video/mp4">' ) . findall ( oOOoO0O0O0 )
 for i1I1IiiIi1i in Ii1 :
  if '=m' in i1I1IiiIi1i :
   iII1ii1 ( i1I1IiiIi1i )
  elif 'php' in i1I1IiiIi1i :
   i1i1ii ( url )
  else :
   oOOoO0O0O0 = OO0oOO0O ( i1I1IiiIi1i )
   Ii1 = re . compile ( 'content="(.+?)">' ) . findall ( oOOoO0O0O0 )
   for I1i1iiiI1 in Ii1 :
    iII1ii1 ( i1I1IiiIi1i )
    if 24 - 24: OoOOOOO / Ii + OoOOOOO
    if 20 - 20: I1i1IiI1 + I1i1III / o0o00Oo0O % iI11I1II1I1I
    if 88 - 88: OOooOOo / IIiIiII11i
def OOOOO0O00 ( url ) :
 oOOoO0O0O0 = OO0oOO0O ( url )
 Iii = re . compile ( '<td id=".+?" class="today">.+?title="(.+?)">(.+?)</td>' , re . DOTALL ) . findall ( oOOoO0O0O0 )
 for iIIiIiI1I1 , ooO in Iii :
  print 'there ><><><><><><><><><><><><'
  iIIiIiI1I1 = iIIiIiI1I1
  Ii1 = re . compile ( '<p><a href=".+?" rel=".+?">(.+?)</a>.+?<br /><a href=".+?">(.+?)</a>.+?</p>' , re . DOTALL ) . findall ( str ( ooO ) )
  for o0O0oo0OO0O , iiOO0O0Ooo in Ii1 :
   print 'here <><><><><><><><><><><><>'
   ooOOO0 ( '[COLORred]' + iIIiIiI1I1 + '[/COLOR] - ' + o0O0oo0OO0O + ' - [COLOR' + oO0o0o0ooO0oO + ']' + iiOO0O0Ooo + '[/COLOR]' , i1111 ( 'aHR0cDovL3d3dy5wb2dkZXNpZ24uY28udWsvY2F0Lw==' ) , 10070 , iIIIi1 + 'loader.png' , i1iIIi1 , '' )
 oOoO0 = re . compile ( '<td id=".+?" class="day">.+?title="(.+?)">(.+?)</td>' , re . DOTALL ) . findall ( oOOoO0O0O0 )
 for iIIiIiI1I1 , Oo0 in oOoO0 :
  print 'there ><><><><><><><><><><><><'
  iIIiIiI1I1 = iIIiIiI1I1
  Ii1 = re . compile ( '<p><a href=".+?" rel=".+?">(.+?)</a>.+?<br /><a href=".+?">(.+?)</a>.+?</p>' , re . DOTALL ) . findall ( str ( Oo0 ) )
  for o0O0oo0OO0O , iiOO0O0Ooo in Ii1 :
   print 'here <><><><><><><><><><><><>'
   ooOOO0 ( '[COLORred]' + iIIiIiI1I1 + '[/COLOR] - ' + o0O0oo0OO0O + ' - [COLOR' + oO0o0o0ooO0oO + ']' + iiOO0O0Ooo + '[/COLOR]' , i1111 ( 'aHR0cDovL3d3dy5wb2dkZXNpZ24uY28udWsvY2F0Lw==' ) , 10070 , iIIIi1 + 'loader.png' , i1iIIi1 , '' )
   if 83 - 83: Ii % I11i % oOo
   if 11 - 11: IIiIiII11i % oO0o * OO0O0OoOO0 + oOo + I1i1III
   if 24 - 24: I1ii11iIi11i - OoOOOOO % iI11I1II1I1I . ooOoO0O00 / o0o00Oo0O
def ii1ii111 ( url ) :
 oOOoO0O0O0 = OO0oOO0O ( url )
 oOoO0 = re . compile ( '<li class="yt-uix-scroller-scroll-unit "(.+?)</li>' , re . DOTALL ) . findall ( oOOoO0O0O0 )
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
  OoOO ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , I111i1i1111 , '' , '' )
  if 49 - 49: oO0o / OoOOOOO + o0o00Oo0O * I11i
  if 28 - 28: oOo + Ii / I1i1IiI1 % OOooOOo % I1ii11iIi11i - o0o00Oo0O
  if 54 - 54: ooOoO0O00 + IIiIiII11i
  if 83 - 83: Ii1I - oOo0O0Ooo + iIi1i111II
def iIi1Ii1i1iI ( url ) :
 if 16 - 16: iIi1i111II / I1ii11iIi11i / ii * oOo0O0Ooo + ooOoO0O00 % iIi1i111II
 ooo0o00 = [ ]
 oOOoO0O0O0 = OO0oOO0O ( url )
 Ii1 = re . compile ( '<div class="explore-list">.+?<div class="el-img"><a href="(.+?)" class=".+?"><img src="(.+?)" alt=".+?<h3>(.+?)</h3><p>(.+?)</p></div>' , re . DOTALL ) . findall ( oOOoO0O0O0 )
 for i1I1IiiIi1i , i11ii1ii11i , o0O0oo0OO0O , ooOo0o00 in Ii1 :
  o0O0oo0OO0O = ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' ) . replace ( '&#039;' , '\'' ) . replace ( '&' , '&' ) . replace ( '&quot;' , '"' )
  Oo000o = OO0oOO0O ( i1I1IiiIi1i )
  OOooOO000 = re . compile ( '<!-- # player # -->.+?<iframe title=".+?".+?src="http://www.youtube.com/embed/(.+?)?autohide.+?<!-- detail box -->(.+?)</div>' , re . DOTALL ) . findall ( Oo000o )
  for IIi , oOoO00oo0O in OOooOO000 :
   IiiiI = re . compile ( '<p>(.+?)</p>' , re . DOTALL ) . findall ( str ( oOoO00oo0O ) )
   for O00OoOO0oo0 in IiiiI :
    if o0O0oo0OO0O in ooo0o00 :
     pass
    else :
     OoOO ( o0O0oo0OO0O , IIi , 8043 , i11ii1ii11i , i11ii1ii11i , O00OoOO0oo0 )
     IiI111111IIII ( 'movies' , 'INFO' )
     ooo0o00 . append ( o0O0oo0OO0O )
     if 96 - 96: OOooOOo . I11i - oOo
     if 99 - 99: i1I11i1I . I1ii11iIi11i - I1i1III % I1i1III * o0o00Oo0O . IIiIiII11i
def iIIII1iIIii ( url ) :
 OoO000O0Oo = Oo0o0oooo0O0 ( url )
 Ii1 = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( OoO000O0Oo )
 for url , oOOO00o000o , O00OoOO0oo0 , iIi11i1 , o0O0oo0OO0O in Ii1 :
  ooOOO0 ( o0O0oo0OO0O , url , 10065 , oOOO00o000o , iIi11i1 , O00OoOO0oo0 )
 IiI111111IIII ( 'movies' , 'INFO' )
 if 71 - 71: oOo
def Ooo0o00o0o ( ) :
 O0oOOoooOO0O = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 ooo00Ooo = 'https://www.youtube.com/results?search_query=' + ( O0oOOoooOO0O ) . replace ( ' ' , '+' )
 Oo0o0O00 = ooo00Ooo . lower ( )
 oOOoO0O0O0 = OO0oOO0O ( Oo0o0O00 )
 Ii1 = re . compile ( '<img src="(.+?)" alt=.+?yt-lockup-title "><a href="(.+?)".+?data-sessionlink=.+?" title="(.+?)".+?<span class="accessible-description".+?>(.+?)</span>.+?<div class="yt-lockup-description yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr">(.+?)</div>' , re . DOTALL ) . findall ( oOOoO0O0O0 )
 next = re . compile ( '<a href="(.+?)" class="yt-uix-button.+?class="yt-uix-button-content">Next.+?</span></a>' ) . findall ( oOOoO0O0O0 )
 for IiIIIIIi in next :
  IiIIIIIi = 'https://www.youtube.com' + IiIIIIIi
  ooOOO0 ( '[COLOR' + oO0o0o0ooO0oO + '] NEXT [/COLOR]' , IiIIIIIi , 10065 , iIIIi1 + 'Next.png' , i1iIIi1 , '' )
 for i11ii1ii11i , IiIIIIIi , o0O0oo0OO0O , IiIi1iIIi1 , oOoO00oo0O in Ii1 :
  OO0o . append ( o0O0oo0OO0O )
  IiI111111IIII ( 'tvshows' , 'INFO' )
  I111i1i1111 = 'http:' + ( i11ii1ii11i ) . replace ( 'https:' , '' )
  print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>' + I111i1i1111
  IiIIIIIi = 'http://www.youtube.com' + IiIIIIIi
  OoOO ( '[COLORred]' + IiIi1iIIi1 + '[/COLOR]' + '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' , ( IiIIIIIi ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , I111i1i1111 , I111i1i1111 , oOoO00oo0O )
 else :
  Ii1 = re . compile ( '<img src="(.+?)" alt=.+?yt-lockup-title "><a href="(.+?)".+?data-sessionlink=.+?" title="(.+?)".+?<span class="accessible-description".+?>(.+?)</span>' , re . DOTALL ) . findall ( oOOoO0O0O0 )
  for i11ii1ii11i , IiIIIIIi , o0O0oo0OO0O , IiIi1iIIi1 in Ii1 :
   print 'im doing it'
   IiI111111IIII ( 'tvshows' , 'INFO' )
   I111i1i1111 = 'http:' + ( i11ii1ii11i ) . replace ( 'https:' , '' )
   IiIIIIIi = 'http://www.youtube.com' + IiIIIIIi
   if '&' in IiIIIIIi :
    print ' i got here'
    oOOoO0O0O0 = OO0oOO0O ( IiIIIIIi )
    oOoO0 = re . compile ( '<li class="yt-uix-scroller-scroll-unit "(.+?)</li>' , re . DOTALL ) . findall ( oOOoO0O0O0 )
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
     OoOO ( '[COLORred]' + IiIi1iIIi1 + '[/COLOR]' + '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' , ( IiIIIIIi ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , I111i1i1111 , i1iIIi1 , '' )
   elif o0O0oo0OO0O in OO0o :
    pass
   elif 'user' in IiIIIIIi or 'elete' in o0O0oo0OO0O :
    pass
   elif 'hannel' in IiIIIIIi :
    print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' + IiIIIIIi
    oOOoO0O0O0 = OO0oOO0O ( IiIIIIIi )
    O0OoO0ooOO0o = re . compile ( 'data-thumb="(.+?)".+?href="(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( oOOoO0O0O0 )
    for i11ii1ii11i , IiIIIIIi , o0O0oo0OO0O in O0OoO0ooOO0o :
     if 'outube' in IiIIIIIi or 'list' in IiIIIIIi :
      pass
     elif 'atch' in IiIIIIIi :
      IiIIIIIi = ( IiIIIIIi ) . replace ( '/watch?v=' , '' )
      OoOO ( '[COLORred]' + IiIi1iIIi1 + '[/COLOR]' + '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' , ( IiIIIIIi ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , 'http:' + i11ii1ii11i , 'http:' + i11ii1ii11i , '' )
     else :
      pass
   else :
    OoOO ( '[COLORred]' + IiIi1iIIi1 + '[/COLOR]' + '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' , ( IiIIIIIi ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , I111i1i1111 , I111i1i1111 , '' )
    if 81 - 81: o0o00Oo0O * IIiIiII11i + oOo0O0Ooo * Ii - Ii1I / oOo0O0Ooo
def oO0o00ooO ( url ) :
 oOOoO0O0O0 = OO0oOO0O ( url )
 Ii1 = re . compile ( '<img src="(.+?)" alt=.+?yt-lockup-title "><a href="(.+?)".+?data-sessionlink=.+?" title="(.+?)".+?<span class="accessible-description".+?>(.+?)</span>.+?<div class="yt-lockup-description yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr">(.+?)</div>' , re . DOTALL ) . findall ( oOOoO0O0O0 )
 next = re . compile ( '<a href="(.+?)" class="yt-uix-button.+?class="yt-uix-button-content">Next.+?</span></a>' ) . findall ( oOOoO0O0O0 )
 for url in next :
  url = 'https://www.youtube.com' + url
  ooOOO0 ( '[COLOR' + oO0o0o0ooO0oO + '] NEXT [/COLOR]' , url , 10065 , iIIIi1 + 'Next.png' , i1iIIi1 , '' )
 for i11ii1ii11i , url , o0O0oo0OO0O , IiIi1iIIi1 , oOoO00oo0O in Ii1 :
  OO0o . append ( o0O0oo0OO0O )
  IiI111111IIII ( 'tvshows' , 'INFO' )
  I111i1i1111 = 'http:' + ( i11ii1ii11i ) . replace ( 'https:' , '' )
  print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>' + I111i1i1111
  url = 'http://www.youtube.com' + url
  OoOO ( '[COLORred]' + IiIi1iIIi1 + '[/COLOR]' + '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , I111i1i1111 , I111i1i1111 , oOoO00oo0O )
 else :
  Ii1 = re . compile ( '<img src="(.+?)" alt=.+?yt-lockup-title "><a href="(.+?)".+?data-sessionlink=.+?" title="(.+?)".+?<span class="accessible-description".+?>(.+?)</span>' , re . DOTALL ) . findall ( oOOoO0O0O0 )
  for i11ii1ii11i , url , o0O0oo0OO0O , IiIi1iIIi1 in Ii1 :
   IiI111111IIII ( 'tvshows' , 'INFO' )
   I111i1i1111 = 'http:' + ( i11ii1ii11i ) . replace ( 'https:' , '' )
   url = 'http://www.youtube.com' + url
   if '&' in url :
    oOOoO0O0O0 = OO0oOO0O ( url )
    oOoO0 = re . compile ( '<li class="yt-uix-scroller-scroll-unit "(.+?)</li>' , re . DOTALL ) . findall ( oOOoO0O0O0 )
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
     OoOO ( '[COLORred]' + IiIi1iIIi1 + '[/COLOR]' + '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , I111i1i1111 , i1iIIi1 , '' )
   elif o0O0oo0OO0O in OO0o :
    pass
   elif 'user' in url or 'elete' in o0O0oo0OO0O :
    pass
   elif 'hannel' in url :
    print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' + url
    oOOoO0O0O0 = OO0oOO0O ( url )
    O0OoO0ooOO0o = re . compile ( 'data-thumb="(.+?)".+?href="(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( oOOoO0O0O0 )
    for i11ii1ii11i , url , o0O0oo0OO0O in O0OoO0ooOO0o :
     if 'outube' in url or 'list' in url :
      pass
     elif 'atch' in url :
      url = ( url ) . replace ( '/watch?v=' , '' )
      OoOO ( '[COLORred]' + IiIi1iIIi1 + '[/COLOR]' + '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , 'http:' + i11ii1ii11i , 'http:' + i11ii1ii11i , '' )
     else :
      pass
   else :
    OoOO ( '[COLORred]' + IiIi1iIIi1 + '[/COLOR]' + '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , I111i1i1111 , I111i1i1111 , '' )
    if 24 - 24: i1I11i1I * Ii * iIi1i111II
    if 85 - 85: I11i . OOooOOo / oOo . o0o00Oo0O % Oo0o00
def o00O0 ( ) :
 if oO == 'insert_password' :
  oOOoo00O0O . ok ( '[COLOR' + oO0o0o0ooO0oO + ']G-Tv Login[/COLOR]' , 'You need to set username and password to access this' , 'These are unique and provided upon purchase' , 'from [COLOR' + oO0o0o0ooO0oO + ']http://GenieTv.co.uk[/COLOR]' )
  o0oO0 . openSettings ( sys . argv [ 0 ] )
 else :
  OO0ooo0oOO = open ( I11II1i )
  Ii1 = re . compile ( 'plugin.video.GenieTv.+?2Flive%2F(.+?)%2F(.+?)%2F' ) . findall ( str ( OO0ooo0oOO ) )
  for oo000ii , OoO in Ii1 :
   if oo000ii == 'needs replacing' or OoO == 'needs replacing' :
    Iiiiii111i1ii ( )
  ooOOO0 ( '[COLOR' + oO0o0o0ooO0oO + ']G-Tv PRIVATE LIST[/COLOR]' , ( i1111 ( 'aHR0cDovL2dlbmlldHYuY28udWsvZ3VpZGUvdGhlbGlzdG5ldy5tM3U=' ) ) , 7080 , iIIIi1 + 'PrivateList.png' , i1iIIi1 , '' )
  ooOOO0 ( '[COLOR' + oO0o0o0ooO0oO + ']G-Tv ULTIMATE[/COLOR]' , ( i1111 ( 'aHR0cDovL2dlbmlldHYuY28udWsvZ3VpZGUvdGhlbGlzdHVsdC5tM3U=' ) ) , 60001 , iIIIi1 + 'UltimateList.png' , i1iIIi1 , '' )
  if 25 - 25: iIi1i111II - oOo / Ii
def iiI1ii11i1 ( ) :
 oooOOOOO . ok ( '[COLOR=white]ReCreate Addons.ini[/COLOR]' , 'If it doesnt work ensure login details are correct and retry' , '' , 'This will allow access to streams in guide without linking to favourites' )
 xbmc . executebuiltin ( "XBMC.RunScript(" + Ooo + ")" )
 Iiiiii111i1ii ( )
 oooOOOOO . ok ( '[COLOR=yellow]Done[/COLOR]' , 'Done' , 'Easy as that' , 'Now Go to guide and it should link your GTV streams' )
 if 38 - 38: Ii1I - OO0O0OoOO0 / o0o00Oo0O . Oo0o00
def i1iiIiI1Ii1i ( ) :
 ooOOO0 ( 'Live Events' , '' , 60002 , iIIIi1 + 'UltimateList.png' , i1iIIi1 , '' )
 ooOOO0 ( 'Full List' , '' , 60003 , iIIIi1 + 'UltimateList.png' , i1iIIi1 , '' )
 ooOOO0 ( 'VOD Latest' , '' , 60003 , iIIIi1 + 'UltimateList.png' , i1iIIi1 , '' )
 ooOOO0 ( 'Entertainment' , '' , 60003 , iIIIi1 + 'UltimateList.png' , i1iIIi1 , '' )
 ooOOO0 ( 'Factual' , '' , 60003 , iIIIi1 + 'UltimateList.png' , i1iIIi1 , '' )
 ooOOO0 ( 'Movie Channels' , '' , 60003 , iIIIi1 + 'UltimateList.png' , i1iIIi1 , '' )
 ooOOO0 ( 'Kids' , '' , 60003 , iIIIi1 + 'UltimateList.png' , i1iIIi1 , '' )
 ooOOO0 ( 'Music' , '' , 60003 , iIIIi1 + 'UltimateList.png' , i1iIIi1 , '' )
 ooOOO0 ( 'UK Sports' , '' , 60003 , iIIIi1 + 'UltimateList.png' , i1iIIi1 , '' )
 ooOOO0 ( 'International Sports' , '' , 60003 , iIIIi1 + 'UltimateList.png' , i1iIIi1 , '' )
 ooOOO0 ( 'German' , '' , 60003 , iIIIi1 + 'UltimateList.png' , i1iIIi1 , '' )
 ooOOO0 ( 'World' , '' , 60003 , iIIIi1 + 'UltimateList.png' , i1iIIi1 , '' )
 if 22 - 22: i1I11i1I / Ii
def oOOoo ( name ) :
 iII1111III1I = name
 oOOoO0O0O0 = OO0oOO0O ( i1111 ( 'aHR0cDovL2dlbmlldHYuY28udWsvZ3VpZGUvdGhlbGlzdHVsdC5tM3U=' ) )
 Ii1 = re . compile ( '#EXTINF:.+?tvg-name="(.+?)" tvg-logo="(.+?)" group-title="(.+?)"",.+?\n(.+?)\n' ) . findall ( oOOoO0O0O0 )
 for name , i11ii1ii11i , ii11i , IiIIIIIi in Ii1 :
  if iII1111III1I == 'Full List' :
   IiIIIIIi = ( IiIIIIIi ) . replace ( 'replace_user' , oo0o0O00 ) . replace ( 'replace_pass' , oO )
   OoOO ( ( '' + name + '' ) . replace ( '_' , ' ' ) , ( IiIIIIIi ) . strip ( ) , 10012 , i11ii1ii11i , i11ii1ii11i , '' )
  else :
   iII1111III1I = ( iII1111III1I ) . replace ( 'World' , 'القنوات العربية' )
   if iII1111III1I in ii11i :
    IiIIIIIi = ( IiIIIIIi ) . replace ( 'replace_user' , oo0o0O00 ) . replace ( 'replace_pass' , oO )
    print IiIIIIIi + '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
    OoOO ( ( '' + name + '' ) . replace ( '_' , ' ' ) , ( IiIIIIIi ) . strip ( ) , 10012 , i11ii1ii11i , i11ii1ii11i , '' )
   else :
    pass
    if 100 - 100: oOo % iI11I1II1I1I * IIiIiII11i - OO0O0OoOO0
def oo00O00oO000o ( name ) :
 iII1111III1I = name
 oOOoO0O0O0 = OO0oOO0O ( i1111 ( 'aHR0cDovL2dlbmlldHYuY28udWsvZ3VpZGUvdGhlbGlzdHVsdC5tM3U=' ) )
 Ii1 = re . compile ( '#EXTINF:-1 tvg-name="(.+?)" tvg-logo="(.+?)" group-title="Live Events"",.+?\n(.+?)\n' ) . findall ( oOOoO0O0O0 )
 for name , i11ii1ii11i , IiIIIIIi in Ii1 :
  IiIIIIIi = ( IiIIIIIi ) . replace ( 'replace_user' , oo0o0O00 ) . replace ( 'replace_pass' , oO )
  OoOO ( ( '' + name + '' ) . replace ( '_' , ' ' ) , ( IiIIIIIi ) . strip ( ) , 10012 , i11ii1ii11i , i11ii1ii11i , '' )
 else :
  OoOO ( '[COLORred]Streams will appear here for live events when available[/COLOR]' , '' , 10012 , '' , '' , '' )
  if 71 - 71: Ii1I - oOo / OOooOOo * OOooOOo / ooOoO0O00 . ooOoO0O00
  if 53 - 53: Oo0o00
  if 21 - 21: I1i1IiI1
  if 92 - 92: Ii / Oo0o00 - OO0O0OoOO0 % oOo * Oo0o00 + I1ii11iIi11i
  if 11 - 11: ii . Oo0o00
  if 80 - 80: ii - iIi1i111II * I1i1III * Ii1I / oOo0O0Ooo / iIi1i111II
  if 13 - 13: Oo0o00 * oOo + Ii * Oo0o00 - oOo
  if 23 - 23: iI11I1II1I1I * ooOoO0O00 % ii * i1I11i1I
  if 9 - 9: i1I11i1I - IIiIiII11i + o0o00Oo0O / iI11I1II1I1I / Ii
  if 39 - 39: i1I11i1I * I1ii11iIi11i + iI11I1II1I1I - i1I11i1I + iIi1i111II
  if 69 - 69: o0o00Oo0O
  if 85 - 85: oOo / o0o00Oo0O
def iI1iIIIi1i ( ) :
 ooOOO0 ( 'Full Backup' , '' , 10061 , iIIIi1 + 'FullBackUp.png' , i1iIIi1 , 'Back Up Your Full System' )
 if os . path . exists ( I1IIiiIiii ) :
  ooOOO0 ( 'Backup Genie Favourites' , IiIIIIIi , 10062 , iIIIi1 + 'BackupGenieFavourites.png' , i1iIIi1 , 'Back Up Your favourites' )
 if os . path . exists ( O000OO0 ) :
  ooOOO0 ( 'Backup Ivue Config' , O000OO0 , 10062 , iIIIi1 + 'BackUpIvueConfig.png' , i1iIIi1 , 'Back Up Your master.db' )
 if os . path . exists ( I11iii1Ii ) :
  ooOOO0 ( 'Backup Kodi Favourites' , I11iii1Ii , 10062 , iIIIi1 + 'BackKodiFavourites.png' , i1iIIi1 , 'Back Up Your favourites.xml' )
  if 89 - 89: iI11I1II1I1I
  if 21 - 21: I1i1IiI1 % I1i1IiI1
  if 27 - 27: Ii / Ii1I
zip = o0oO0 . getSetting ( 'zip' )
oOoOOo = xbmc . translatePath ( os . path . join ( zip ) )
def ii1iI ( ) :
 IIiooOooo0 = xbmc . translatePath ( os . path . join ( zip , 'testCBFolder' ) )
 if not os . path . exists ( zip ) :
  oooOOOOO . ok ( '[COLOR=white]Origin[/COLOR]' , 'The download location you have stored does not exist .\nPlease update the addon settings and try again.' , '' , '' )
  o0oO0 . openSettings ( sys . argv [ 0 ] )
  if 67 - 67: oOo0O0Ooo
  if 55 - 55: Ii1I - OO0O0OoOO0 * I11i + OOooOOo * OOooOOo * o0o00Oo0O
  if 91 - 91: Oo0o00 - iIi1i111II % iI11I1II1I1I - ii % oOo
def OO0I1i11iIIi ( name , url , description ) :
 if 'Backup' in name :
  if 'Genie' in name :
   url = I1IIiiIiii
  elif 'Ivue' in name :
   url = O000OO0
  elif 'Kodi' in name :
   url = I11iii1Ii
  ii1iI ( )
  i1IIIIiI111I = open ( url ) . read ( )
  iIIIIIii = os . path . join ( oOoOOo , description . split ( 'Your ' ) [ 1 ] )
  oo0OOo0 = open ( iIIIIIii , mode = 'w' )
  oo0OOo0 . write ( i1IIIIiI111I )
  oo0OOo0 . close ( )
 else :
  if 'guisettings.xml' in description :
   Ii1ii111i1 = open ( os . path . join ( oOoOOo , description . split ( 'Your ' ) [ 1 ] ) ) . read ( )
   i1i1i1I = '<setting type="(.+?)" name="%s.(.+?)">(.+?)</setting>' % skin
   Ii1 = re . compile ( i1i1i1I ) . findall ( Ii1ii111i1 )
   for type , oOoo000 , OooOo00o in Ii1 :
    OooOo00o = OooOo00o . replace ( '&quot;' , '' ) . replace ( '&' , '&' )
    xbmc . executebuiltin ( "Skin.Se	t%s(%s,%s)" % ( type . title ( ) , oOoo000 , OooOo00o ) )
  else :
   iIIIIIii = os . path . join ( url )
   i1IIIIiI111I = open ( os . path . join ( oOoOOo , description . split ( 'Your ' ) [ 1 ] ) ) . read ( )
   oo0OOo0 = open ( iIIIIIii , mode = 'w' )
   oo0OOo0 . write ( i1IIIIiI111I )
   oo0OOo0 . close ( )
 oooOOOOO . ok ( "[COLOR=white]Origin[/COLOR]" , "" , 'All Done !' , '' )
 if 20 - 20: ooOoO0O00 * Oo0o00 + IIiIiII11i % I11i % OoOOOOO
 if 13 - 13: I1ii11iIi11i
 if 60 - 60: Ii1I * oOo0O0Ooo
 if 17 - 17: iIi1i111II % I1ii11iIi11i / Ii1I . i1I11i1I * iIi1i111II - IIiIiII11i
def i1i1IIii1i1 ( ) :
 oOoO00 = 1
 ii1iI ( )
 iI1IIIii = xbmc . translatePath ( os . path . join ( oOoOOo , 'Build Backup' , 'Full Backup' , '' ) )
 I1i11ii11 = xbmc . translatePath ( os . path . join ( oOoOOo , 'Build Backup' , 'my_full_backup.zip' ) )
 OO00O0oOO = xbmc . translatePath ( os . path . join ( oOoOOo , 'Build Backup' , 'my_full_backup_GUI_Settings.zip' ) )
 if not os . path . exists ( iI1IIIii ) :
  os . makedirs ( iI1IIIii )
 Ii1iI111 = oOOoo00O0O . input ( 'Enter a name for this backup' , type = xbmcgui . INPUT_ALPHANUM )
 if ( not Ii1iI111 ) : return False , 0
 O0oooo00o0Oo = Ii1iI111
 I1iii = xbmc . translatePath ( os . path . join ( iI1IIIii , O0oooo00o0Oo + '.zip' ) )
 oO0o0O0Ooo0o = [ 'plugin.video.GenieTv' ]
 i1Ii11II = [ "xbmc.log" , "xbmc.old.log" , "kodi.log" , "kodi.old.log" , '.DS_Store' , '.setup_complete' , 'XBMCHelper.conf' ]
 IioO0oOOO0Ooo = [ 'plugin.video.GenieTv' , 'repository.origin' , 'cache' , 'system' , 'Thumbnails' , "peripheral_data" , 'library' , 'keymaps' ]
 i1i1I = [ "xbmc.log" , "xbmc.old.log" , "kodi.log" , "kodi.old.log" , "Textures13.db" , '.DS_Store' , '.setup_complete' , 'XBMCHelper.conf' , 'advancedsettings.xml' ]
 IiIIi1 = "Creating full backup of existing build"
 iII11I1Ii1 = "Creating Community Build"
 o0o0 = "Archiving..."
 oOo0oO = ""
 IIi1IIIIi = "Please Wait"
 OOOoO ( i1iiIII111ii , I1iii , iII11I1Ii1 , o0o0 , oOo0oO , IIi1IIIIi , IioO0oOOO0Ooo , i1i1I )
 time . sleep ( 1 )
 I1i = xbmc . translatePath ( os . path . join ( iI1IIIii , O0oooo00o0Oo + '_guisettings.zip' ) )
 iiiI = zipfile . ZipFile ( I1i , mode = 'w' )
 try :
  iiiI . write ( xbmc . translatePath ( os . path . join ( i1iiIII111ii , 'userdata' , 'profiles.xml' ) ) , 'profiles.xml' , zipfile . ZIP_DEFLATED )
 except : pass
 iiiI . close ( )
 if oOoO00 == 0 :
  oooOOOOO . ok ( "FAILED!" , 'The guisettings.xml file could not be found on your' , 'system, please reboot and try again.' , '' )
 else :
  oooOOOOO . ok ( "SUCCESS!" , 'You Are Now Backed Up. If you\'d like to share this build with' , 'the community please post details on the forum at' , '[COLOR=blue][B]http://rh-project.info[/COLOR][/B]' )
  oooOOOOO . ok ( "Build Locations" , 'Full Backup (only used to restore on this device): [COLOR=yellow]' + I1i11ii11 , '[/COLOR]Universal Backup (can be used on any device): [COLOR=yellow]' + I1iii + '[/COLOR]' )
  if 21 - 21: Ii / ooOoO0O00 + oOo0O0Ooo * iIi1i111II . Oo0o00
def OOOoO ( sourcefile , destfile , message_header , message1 , message2 , message3 , exclude_dirs , exclude_files ) :
 OoOoo0oO = zipfile . ZipFile ( destfile , 'w' , zipfile . ZIP_DEFLATED )
 iioo0o0OoOOO = len ( sourcefile )
 ooO0oO00O0o = [ ]
 ooOO00oOOo000 = [ ]
 Oo0oO0ooo . create ( message_header , message1 , message2 , message3 )
 for IIii11II11II1 , II1I , OoOo000oOo0oo in os . walk ( sourcefile ) :
  for file in OoOo000oOo0oo :
   ooOO00oOOo000 . append ( file )
 oO0O = len ( ooOO00oOOo000 )
 for IIii11II11II1 , II1I , OoOo000oOo0oo in os . walk ( sourcefile ) :
  II1I [ : ] = [ oOO for oOO in II1I if oOO not in exclude_dirs ]
  OoOo000oOo0oo [ : ] = [ oo0OOo0 for oo0OOo0 in OoOo000oOo0oo if oo0OOo0 not in exclude_files ]
  for file in OoOo000oOo0oo :
   ooO0oO00O0o . append ( file )
   iiiIIiIi = len ( ooO0oO00O0o ) / float ( oO0O ) * 100
   Oo0oO0ooo . update ( int ( iiiIIiIi ) , "Backing Up" , '[COLOR yellow]%s[/COLOR]' % file , 'Please Wait' )
   OooOOO = os . path . join ( IIii11II11II1 , file )
   if not 'temp' in II1I :
    if not 'plugin.program.originwizard' in II1I :
     import time
     Ii1iI11iI1 = '01/01/1980'
     i11I1II = time . strftime ( '%d/%m/%Y' , time . gmtime ( os . path . getmtime ( OooOOO ) ) )
     if i11I1II > Ii1iI11iI1 :
      OoOoo0oO . write ( OooOOO , OooOOO [ iioo0o0OoOOO : ] )
 OoOoo0oO . close ( )
 Oo0oO0ooo . close ( )
 if 79 - 79: oO0o . OO0O0OoOO0 * I1i1III - iIi1i111II + oOo
 if 14 - 14: Ii - OO0O0OoOO0 * OOooOOo
def OO0oIII111i11IiI ( ) :
 O0O0oOO00O00o ( )
 ooOOO0 ( '[COLOR' + oO0o0o0ooO0oO + ']SCOOBY STREAMS[/COLOR]' , ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvdHZjYXRzLnBocA==' ) ) , 1016 , iIIIi1 + 'scoob.png' , i1iIIi1 , '' )
 ooOOO0 ( '[COLOR' + oO0o0o0ooO0oO + ']SCOOBY SCRAPES[/COLOR]' , ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvc2NyYXBlZC9jYXRzLnBocA==' ) ) , 1024 , iIIIi1 + 'scoob.png' , i1iIIi1 , '' )
 if 71 - 71: I1i1IiI1 / I1i1IiI1 * OoOOOOO * OoOOOOO / IIiIiII11i
 if 35 - 35: iIi1i111II * I11i * oOo0O0Ooo % I1ii11iIi11i . OOooOOo
def O00o00O ( ) :
 O0O0oOO00O00o ( )
 ooOOO0 ( '[COLOR' + oO0o0o0ooO0oO + ']SEARCH MOVIES[/COLOR]' , str ( oooo000 ) , 9001 , iIIIi1 + 'MOVIESv.png' , i1iIIi1 , '' )
 ooOOO0 ( '[COLOR' + oO0o0o0ooO0oO + ']SEARCH SERIES[/COLOR]' , str ( oooo000 ) , 9002 , iIIIi1 + 'TVSHOWSv.png' , i1iIIi1 , '' )
 ooOOO0 ( '[COLOR' + oO0o0o0ooO0oO + ']SEARCH CARTOONS[/COLOR]' , '' , 10005 , iIIIi1 + 'ORIGINCARTOON' , i1iIIi1 , '' )
 if 3 - 3: iIi1i111II
 if 20 - 20: IIiIiII11i . OO0O0OoOO0 / IIiIiII11i % Ii % OO0O0OoOO0
 if 11 - 11: i1I11i1I % Ii1I % I1i1III / IIiIiII11i % Oo0o00 - I1ii11iIi11i
 if 96 - 96: Ii1I / IIiIiII11i . I1i1III - OO0O0OoOO0 * I1i1IiI1 * OoOOOOO
def O00oo0ooO ( ) :
 O0O0oOO00O00o ( )
 ooOOO0 ( '[COLOR' + oO0o0o0ooO0oO + ']QuickSilver[/COLOR]' , ( i1111 ( 'aHR0cDovL3F1aWNrc2lsdmVyLW11c2ljLmNvbS9rb2RpbXVzaWM=' ) ) , 1006 , iIIIi1 + 'Quicksilver.png' , i1iIIi1 , '' )
 ooOOO0 ( '[COLOR' + oO0o0o0ooO0oO + ']MUSIC CHANNELS[/COLOR]' , str ( oooo000 ) , 30031 , iIIIi1 + 'MusicChannels.png' , i1iIIi1 , '' )
 ooOOO0 ( '[COLOR' + oO0o0o0ooO0oO + ']UK RADIO[/COLOR]' , ( i1111 ( 'aHR0cDovL3d3dy5saXN0ZW5saXZlLmV1L3VrLmh0bWw=' ) ) , 10111113 , iIIIi1 + 'UKRadio.png' , i1iIIi1 , '' )
 ooOOO0 ( '[COLOR' + oO0o0o0ooO0oO + ']WORLD RADIO[/COLOR]' , str ( oooo000 ) , 1013 , iIIIi1 + 'WorldRadio.png' , i1iIIi1 , '' )
 if o0oO0 . getSetting ( 'CONCERTS' ) == 'true' :
  ooOOO0 ( '[COLOR' + oO0o0o0ooO0oO + ']CONCERTS[/COLOR]' , ( i1111 ( 'aHR0cHM6Ly93d3cucmVkZGl0LmNvbS9yL2Z1bGxjb25jZXJ0cy8=' ) ) , 7050 , iIIIi1 + 'Concerts.png' , i1iIIi1 , '' )
  if 38 - 38: iI11I1II1I1I - IIiIiII11i - oOo0O0Ooo
 ooOOO0 ( '[COLOR' + oO0o0o0ooO0oO + ']MUSIC VIDEOS[/COLOR]' , ( i1111 ( 'aHR0cDovLzE3Ni45LjE5Mi4yMjEvbXA0Lw==' ) ) , 1032 , iIIIi1 + 'MusicVideos.png' , i1iIIi1 , '' )
 ooOOO0 ( '[COLOR' + oO0o0o0ooO0oO + ']MUSIC[/COLOR]' , str ( oooo000 ) + ( i1111 ( 'L3ZvZC91cmxzL211c2ljLnBocA==' ) ) , 1010 , iIIIi1 + 'Music.png' , i1iIIi1 , '' )
 ooOOO0 ( '[COLOR' + oO0o0o0ooO0oO + ']MUSIC SEARCH[/COLOR]' , str ( oooo000 ) , 1111 , iIIIi1 + 'MusicSearch.png' , i1iIIi1 , '' )
 ooOOO0 ( '[COLOR' + oO0o0o0ooO0oO + ']KODIBLE AUDIO BOOKS[/COLOR]' , 'http://doremisa.com/audiobooks/' , 30000 , iIIIi1 + 'KodibleAudioBooks.png' , i1iIIi1 , '' )
 if 71 - 71: ii
 IiI111111IIII ( 'movies' , 'MAIN' )
 if 33 - 33: Oo0o00
def OOO0ooo ( ) :
 O0O0oOO00O00o ( )
 if 7 - 7: I11i + ooOoO0O00 . oOo0O0Ooo / I1ii11iIi11i
 OoOO ( 'DELETE CACHE' , 'url' , 14 , iIIIi1 + 'DeleteCache.png' , i1iIIi1 , '' )
 OoOO ( 'DELETE PACKAGES' , 'url' , 6 , iIIIi1 + 'DeletePackages.png' , i1iIIi1 , '' )
 OoOO ( 'FORCE REFRESH' , 'url' , 10 , iIIIi1 + 'ForceRefresh.png' , i1iIIi1 , 'Force Refresh All Repos' )
 if 22 - 22: oOo - oOo % iIi1i111II . Oo0o00 + OoOOOOO
 OoOO ( 'CHECK MY IP' , 'url' , 12 , iIIIi1 + 'CheckMyIP.png' , i1iIIi1 , '' )
 OoOO ( 'ANDROID ONLY DELETE TEXTURE13.DB&THUBMNAIL FOLDER' , 'url' , 13 , iIIIi1 + 'DeleteTextureAndThumbnailFolderAndroidOnly.png' , i1iIIi1 , 'Only Works On Android On Windows It Deletes Your Thumnails Folder But Does Not Delete The Textures13.db' )
 ooOOO0 ( '[COLOR' + oO0o0o0ooO0oO + ']ADVANCED SETTINGS XML[/COLOR]' , str ( oooo000 ) , 4 , iIIIi1 + 'AdvancedSettingXML.png' , i1iIIi1 , '' )
 ooOOO0 ( '[COLOR' + oO0o0o0ooO0oO + ']URL FIXES[/COLOR]' , str ( oooo000 ) , 20 , iIIIi1 + 'URLFixes.png' , i1iIIi1 , '' )
 IiI111111IIII ( 'movies' , 'MAIN' )
 if 63 - 63: oOo0O0Ooo % Oo0o00 * I11i + Oo0o00 / I1ii11iIi11i % OO0O0OoOO0
 if 45 - 45: i1I11i1I
def iI1Ii11111iIi ( ) :
 O0O0oOO00O00o ( )
 ooOOO0 ( '[COLOR' + oO0o0o0ooO0oO + ']REPOS[/COLOR]' , ( i1111 ( 'aHR0cDovL21pcnJvcnMua29kaS50di9hZGRvbnMv' ) ) , 2030 , iIIIi1 + 'repos.png' , i1iIIi1 , '' )
 ooOOO0 ( '[COLOR' + oO0o0o0ooO0oO + ']NEW[/COLOR]' , str ( oooo000 ) , 22 , iIIIi1 + 'NEW.png' , i1iIIi1 , '' )
 ooOOO0 ( '[COLOR' + oO0o0o0ooO0oO + ']IPTV[/COLOR]' , str ( oooo000 ) , 23 , iIIIi1 + 'IPTV.png' , i1iIIi1 , '' )
 ooOOO0 ( '[COLOR' + oO0o0o0ooO0oO + ']VIDEO[/COLOR]' , str ( oooo000 ) , 24 , iIIIi1 + 'VIDEO.png' , i1iIIi1 , '' )
 ooOOO0 ( '[COLOR' + oO0o0o0ooO0oO + ']SPORTS[/COLOR]' , str ( oooo000 ) , 25 , iIIIi1 + 'SPORTS.png' , i1iIIi1 , '' )
 ooOOO0 ( '[COLOR' + oO0o0o0ooO0oO + ']KIDS[/COLOR]' , str ( oooo000 ) , 26 , iIIIi1 + 'KIDS.png' , i1iIIi1 , '' )
 ooOOO0 ( '[COLOR' + oO0o0o0ooO0oO + ']MUSIC[/COLOR]' , str ( oooo000 ) , 27 , iIIIi1 + 'MUSIC.png' , i1iIIi1 , '' )
 ooOOO0 ( '[COLOR' + oO0o0o0ooO0oO + ']PROGRAMS[/COLOR]' , str ( oooo000 ) , 28 , iIIIi1 + 'PROGRAMS.png' , i1iIIi1 , '' )
 ooOOO0 ( '[COLOR' + oO0o0o0ooO0oO + ']XXX[/COLOR]' , 'URL' , 29 , iIIIi1 + 'XXX.png' , i1iIIi1 , '' )
 IiI111111IIII ( 'movies' , 'MAIN' )
 if 20 - 20: ii * I11i * o0o00Oo0O . iIi1i111II
 if 78 - 78: iI11I1II1I1I + I1i1IiI1 - I1i1III * Oo0o00 - ii % OOooOOo
def i1OoOO ( ) :
 O0O0oOO00O00o ( )
 OoOO ( 'CHECK ADVANCED XML' , str ( oooo000 ) , 8 , iIIIi1 + 'XML.png' , i1iIIi1 , '' )
 OoOO ( 'MUCKYS XML' , str ( oooo000 ) + '/wizard/muckys.xml' , 7 , iIIIi1 + 'XML.png' , i1iIIi1 , '' )
 OoOO ( '0CACHE XML' , str ( oooo000 ) + '/wizard/0cache.xml' , 7 , iIIIi1 + 'XML.png' , i1iIIi1 , '' )
 OoOO ( 'MIKEY1234 XML' , str ( oooo000 ) + '/wizard/mikey.xml' , 7 , iIIIi1 + 'XML.png' , i1iIIi1 , '' )
 OoOO ( 'TUXENS XML' , str ( oooo000 ) + '/wizard/tuxens.xml' , 7 , iIIIi1 + 'XML.png' , i1iIIi1 , '' )
 OoOO ( 'P2P RECOMMENDED XML1' , str ( oooo000 ) + '/wizard/p2p1.xml' , 7 , iIIIi1 + 'XML.png' , i1iIIi1 , '' )
 OoOO ( 'P2P RECOMMENDED XML2' , str ( oooo000 ) + '/wizard/p2p2.xml' , 7 , iIIIi1 + 'XML.png' , i1iIIi1 , '' )
 OoOO ( 'DELETE XML' , str ( oooo000 ) , 11 , iIIIi1 + 'XML.png' , i1iIIi1 , '' )
 IiI111111IIII ( 'movies' , 'MAIN' )
 if 44 - 44: iIi1i111II
def O0O0o0o0o ( ) :
 O0O0oOO00O00o ( )
 OoOO ( '[COLOR' + oO0o0o0ooO0oO + ']My Local Zip[/COLOR]' , I11 , 48 , iIIIi1 + 'MyLocalZIP.png' , i1iIIi1 , '' )
 OoOO ( '[COLOR' + oO0o0o0ooO0oO + ']My Online Zip[/COLOR]' , i11 , 43 , iIIIi1 + 'MyOnlineZip.png' , i1iIIi1 , '' )
 if 9 - 9: I1ii11iIi11i + OOooOOo - iI11I1II1I1I - I1i1III + I11i
def o000O0OOoo ( ) :
 O0O0oOO00O00o ( )
 OoOO ( 'INSTALL FTV GUIDE AND OTHER ADDONS REQUIRED' , str ( oooo000 ) + '/wizard/customftv/ftvguide-addons.zip' , 5 , iIIIi1 + 'FTV4.png' , i1iIIi1 , '' )
 OoOO ( 'FTV GUIDE FIRST RUN SETTINGS' , str ( oooo000 ) + '/wizard/customftv/settings.xml' , 17 , iIIIi1 + 'FTV3.png' , i1iIIi1 , '' )
 OoOO ( 'FTV GUIDE ADDONS2.INI UPDATE DAILY' , 'http://ren.byethost12.com/addons2.ini' , 16 , iIIIi1 + 'FTV1.png' , i1iIIi1 , '' )
 OoOO ( 'RESET FTV DATABASE' , 'url' , 18 , iIIIi1 + 'FTV2.png' , i1iIIi1 , '' )
 if 60 - 60: oOo0O0Ooo * Oo0o00 % oO0o + OoOOOOO
 if 52 - 52: ooOoO0O00
 if 84 - 84: I1i1III / i1I11i1I
def OOOooo0OooOoO ( ) :
 O0O0oOO00O00o ( )
 ooOOO0 ( '[COLOR' + oO0o0o0ooO0oO + ']SKINS[/COLOR]' , str ( oooo000 ) , 33 , iIIIi1 + 'Skins.png' , i1iIIi1 , '' )
 ooOOO0 ( '[COLOR' + oO0o0o0ooO0oO + ']ARTWORK PACKS[/COLOR]' , str ( oooo000 ) , 34 , iIIIi1 + 'ArtworkPacks.png' , i1iIIi1 , '' )
 ooOOO0 ( '[COLOR' + oO0o0o0ooO0oO + ']CREATE UNIVERSAL PATHS[/COLOR]' , i1iiIII111ii , 35 , iIIIi1 + 'CreateUniversalPath.png' , i1iIIi1 , '' )
 IiI111111IIII ( 'movies' , 'MAIN' )
 if 91 - 91: OoOOOOO + oOo0O0Ooo
def OoOooo ( ) :
 I11i1I1I = OO0oOO0O ( i1111 ( 'aHR0cDovL2dlbmlldHYuY28udWsvaW5kZXgucGhwL2d0di1pcHR2' ) )
 Ii1 = re . compile ( ' src="([^"]*)".+?><br />(.+?)</span></li>' , re . DOTALL ) . findall ( I11i1I1I )
 for i11ii1ii11i , o0O0oo0OO0O in Ii1 :
  OoOO ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' ) . replace ( '&amp;' , '&' ) . replace ( '<br />' , '' ) . replace ( '&nbsp;' , ' ' ) . replace ( '</span><span style="margin: 0px; padding: 0px;">' , ' ' ) , '' , '' , i11ii1ii11i , i11ii1ii11i , '' )
 IiI111111IIII ( 'tvshows' , 'INFO' )
 if 74 - 74: iI11I1II1I1I * i1I11i1I % OOooOOo
def iiI11iIi ( url ) :
 I11i1I1I = OO0oOO0O ( oooOO0OO0O ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 Ii1 = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( I11i1I1I )
 for o0O0oo0OO0O , url , oOOO00o000o , iIi11i1 , oOoO00oo0O in Ii1 :
  ooOOO0 ( o0O0oo0OO0O , url , 5 , oOOO00o000o , iIi11i1 , oOoO00oo0O )
 IiI111111IIII ( 'movies' , 'MAIN' )
 if 78 - 78: I1i1III / IIiIiII11i % OOooOOo
def oO00OoOO ( ) :
 O0O0oOO00O00o ( )
 ooOOO0 ( '[COLOR' + oO0o0o0ooO0oO + ']GOTHAM SKINS[/COLOR]' , str ( oooo000 ) , 36 , iIIIi1 + 'GothamSkins.png' , i1iIIi1 , '' )
 ooOOO0 ( '[COLOR' + oO0o0o0ooO0oO + ']HELIX SKINS[/COLOR]' , str ( oooo000 ) , 37 , iIIIi1 + 'HelixSkins.png' , i1iIIi1 , '' )
 ooOOO0 ( '[COLOR' + oO0o0o0ooO0oO + ']ISENGAARD SKINS[/COLOR]' , i1iiIII111ii , 38 , iIIIi1 + 'IsengaardSkins.png' , i1iIIi1 , '' )
 IiI111111IIII ( 'movies' , 'MAIN' )
 if 18 - 18: oOo - OOooOOo % ooOoO0O00 + o0o00Oo0O + Ii + ooOoO0O00
def oOo0o0O ( url ) :
 I11i1I1I = OO0oOO0O ( str ( oooo000 ) + OOoOO ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 Ii1 = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( I11i1I1I )
 for o0O0oo0OO0O , url , oOOO00o000o , iIi11i1 , oOoO00oo0O in Ii1 :
  ooOOO0 ( o0O0oo0OO0O , url , 42 , oOOO00o000o , iIi11i1 , oOoO00oo0O )
 IiI111111IIII ( 'movies' , 'MAIN' )
 if 66 - 66: I1ii11iIi11i - I11i * i1I11i1I + OOooOOo + I11i - iI11I1II1I1I
def iiiI1ii11 ( url ) :
 I11i1I1I = OO0oOO0O ( str ( oooo000 ) + ii1i ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 Ii1 = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( I11i1I1I )
 for o0O0oo0OO0O , url , oOOO00o000o , iIi11i1 , oOoO00oo0O in Ii1 :
  ooOOO0 ( o0O0oo0OO0O , url , 42 , oOOO00o000o , iIi11i1 , oOoO00oo0O )
 IiI111111IIII ( 'movies' , 'MAIN' )
 if 5 - 5: OoOOOOO . Ii1I . IIiIiII11i . ii
def Oo0OooO0 ( url ) :
 I11i1I1I = OO0oOO0O ( str ( oooo000 ) + oO00oOo0OOO ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 Ii1 = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( I11i1I1I )
 for o0O0oo0OO0O , url , oOOO00o000o , iIi11i1 , oOoO00oo0O in Ii1 :
  ooOOO0 ( o0O0oo0OO0O , url , 42 , oOOO00o000o , iIi11i1 , oOoO00oo0O )
 IiI111111IIII ( 'movies' , 'MAIN' )
 if 23 - 23: ooOoO0O00 . I11i * oO0o
def iIi1IiI ( url ) :
 I11i1I1I = OO0oOO0O ( i1111 ( 'aHR0cHM6Ly9kbC5kcm9wYm94dXNlcmNvbnRlbnQuY29tL3MvN2ZrMjhndDlwb3QxMjJhL0JVSUxEUy50eHQ/ZGw9MA==' ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 Ii1 = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( I11i1I1I )
 for o0O0oo0OO0O , url , oOOO00o000o , iIi11i1 , oOoO00oo0O in Ii1 :
  ooOOO0 ( o0O0oo0OO0O , url , 42 , oOOO00o000o , iIi11i1 , oOoO00oo0O )
 IiI111111IIII ( 'movies' , 'MAIN' )
 if 14 - 14: i1I11i1I % OoOOOOO % I1ii11iIi11i - Ii
def o0OO000ooOo ( url ) :
 I11i1I1I = OO0oOO0O ( str ( oooo000 ) + oOo00OooO0oO ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 Ii1 = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( I11i1I1I )
 for o0O0oo0OO0O , url , oOOO00o000o , iIi11i1 , oOoO00oo0O in Ii1 :
  ooOOO0 ( o0O0oo0OO0O , url , 40 , oOOO00o000o , iIi11i1 , oOoO00oo0O )
 IiI111111IIII ( 'movies' , 'MAIN' )
 if 16 - 16: i1I11i1I / I1ii11iIi11i + iIi1i111II / I1i1III
def IIIiiI1 ( url ) :
 I11i1I1I = OO0oOO0O ( str ( oooo000 ) + O0O0ooOOO ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 Ii1 = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( I11i1I1I )
 for o0O0oo0OO0O , url , oOOO00o000o , iIi11i1 , oOoO00oo0O in Ii1 :
  ooOOO0 ( o0O0oo0OO0O , url , 5 , oOOO00o000o , iIi11i1 , oOoO00oo0O )
 IiI111111IIII ( 'movies' , 'MAIN' )
 if 70 - 70: oOo . o0o00Oo0O . Oo0o00 . o0o00Oo0O + ooOoO0O00
def i1II1I ( ) :
 ooOOO0 ( '[COLOR' + oO0o0o0ooO0oO + ']APK (Android only)[/COLOR]' , str ( oooo000 ) , 2 , iIIIi1 + 'APKAndroidOnly.png' , i1iIIi1 , '' )
 ooOOO0 ( '[COLOR' + oO0o0o0ooO0oO + ']APK Search[/COLOR]' , str ( oooo000 ) , 30038 , iIIIi1 + 'APKSearch.png' , i1iIIi1 , '' )
 if 95 - 95: oO0o - iIi1i111II / IIiIiII11i % Ii1I . I11i
def iii1IIII1iii11I ( ) :
 OoO000O0Oo = Oo0o0oooo0O0 ( i1111 ( 'aHR0cDovL2Fway5rb3BsYXllci5jb20vZ2FtZS8=' ) )
 Ii1 = re . compile ( 'href="([^"]*)">GAME</a>' ) . findall ( OoO000O0Oo )
 OOooOO000 = re . compile ( 'href="([^"]*)">APP</a>' ) . findall ( OoO000O0Oo )
 for IiIIIIIi in Ii1 :
  iiI11ii1I1 ( 'Android Apps' , ( i1111 ( 'aHR0cDovL2Fway5rb3BsYXllci5jb20=' ) ) + IiIIIIIi , 30036 , iIIIi1 + 'apps.png' )
 for IiIIIIIi in OOooOO000 :
  iiI11ii1I1 ( 'Android Games' , ( i1111 ( 'aHR0cDovL2Fway5rb3BsYXllci5jb20=' ) ) + IiIIIIIi , 30035 , iIIIi1 + 'GAMES.png' )
 IiI111111IIII ( 'movies' , 'MAIN' )
def oo0OoOooo ( url ) :
 OoO000O0Oo = Oo0o0oooo0O0 ( url )
 Ii1 = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( OoO000O0Oo )
 for url , o0O0oo0OO0O in Ii1 :
  if '/game' in url :
   iiI11ii1I1 ( ( o0O0oo0OO0O ) . replace ( '&amp;' , ' - ' ) , ( i1111 ( 'aHR0cDovL2Fway5rb3BsYXllci5jb20=' ) ) + url , 30037 , iIIIi1 + 'APK.png' )
def O00O00O000OOO ( url ) :
 OoO000O0Oo = Oo0o0oooo0O0 ( url )
 Ii1 = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( OoO000O0Oo )
 for url , o0O0oo0OO0O in Ii1 :
  if '/app' in url :
   iiI11ii1I1 ( ( o0O0oo0OO0O ) . replace ( '&amp;' , ' - ' ) , ( i1111 ( 'aHR0cDovL2Fway5rb3BsYXllci5jb20=' ) ) + url , 30037 , iIIIi1 + 'APK.png' )
def iI ( url ) :
 OoO000O0Oo = Oo0o0oooo0O0 ( url )
 Ii1 = re . compile ( ' <img src="([^"]*)".+?title="([^"]*)">.+?<a href="([^"]*)"' , re . DOTALL ) . findall ( OoO000O0Oo )
 OOooOO000 = re . compile ( 'href="([^"]*)">NEXT </a>' ) . findall ( OoO000O0Oo )
 for i11ii1ii11i , o0O0oo0OO0O , url in Ii1 :
  iiI11ii1I1 ( ( o0O0oo0OO0O ) . replace ( '&#39;' , '' ) . replace ( '&amp;' , ' - ' ) . replace ( '&#174;:' , ': ' ) . replace ( '&#174;' , ' ' ) , url , 19 , i11ii1ii11i )
 for url in OOooOO000 :
  iiI11ii1I1 ( 'NEXT' , ( i1111 ( 'aHR0cDovL2Fway5rb3BsYXllci5jb20=' ) ) + url , 30037 , iIIIi1 + 'Next.png' )
def Oo0O ( url ) :
 OoO000O0Oo = Oo0o0oooo0O0 ( url )
 Ii1 = re . compile ( 'href="(.+?)">Download APK from APKCRAFT</a></p>' ) . findall ( OoO000O0Oo )
 for url in Ii1 :
  Ii11 ( url )
def II1i111 ( ) :
 O0oOOoooOO0O = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 ooo00Ooo = 'http://apk.koplayer.com/search?q=' + ( O0oOOoooOO0O ) . replace ( ' ' , '+' ) + '&region='
 Oo0o0O00 = ooo00Ooo . lower ( )
 iI ( Oo0o0O00 )
 if 50 - 50: i1I11i1I % ooOoO0O00
def Ii11 ( url ) :
 IIiooOooo0 = xbmc . translatePath ( os . path . join ( iii11II1I , 'Download' ) )
 Oo0oO0ooo = xbmcgui . DialogProgress ( )
 Oo0oO0ooo . create ( "Your App Is Downloading" , "Why not check out our website" , '' , 'Http://GenieTv.co.uk' )
 iI111I11i = os . path . join ( IIiooOooo0 , o0O0oo0OO0O + '.apk' )
 try :
  os . remove ( iI111I11i )
 except :
  pass
 downloader . download ( url , iI111I11i , Oo0oO0ooo )
 oooOOOOO = xbmcgui . Dialog ( )
 oooOOOOO . ok ( "GenieTv" , "[COLORred]Please press ok, exit kodi and go to your downloads folder to install your app[/COLOR]" , "[COLORblue]Tool Brought To You By GenieTv[/COLOR]" )
 if 23 - 23: I1i1III . I11i + I1ii11iIi11i - iIi1i111II
def II1iiIiIiI ( url ) :
 IIiooOooo0 = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/resources/downloads' ) )
 Oo0oO0ooo = xbmcgui . DialogProgress ( )
 Oo0oO0ooo . create ( "Your fILM Is Downloading" , "Why not check out our website" , '' , 'Http://GenieTv.co.uk' )
 iI111I11i = os . path . join ( IIiooOooo0 , o0O0oo0OO0O + '.mp4' )
 try :
  os . remove ( iI111I11i )
 except :
  pass
 downloader . download ( url , iI111I11i , Oo0oO0ooo )
 oooOOOOO = xbmcgui . Dialog ( )
 oooOOOOO . ok ( "GenieTv" , "[COLORred]Please press ok, Your download With Be Avaiilable Via The My Downloads Button[/COLOR]" , "[COLORblue]Tool Brought To You By GenieTv[/COLOR]" )
 if 24 - 24: I1ii11iIi11i - ooOoO0O00 + I1i1IiI1
 if 38 - 38: ii / Ii1I . o0o00Oo0O / ooOoO0O00 / I1ii11iIi11i + iI11I1II1I1I
def ooO00O00oOO ( name , url , description ) :
 IIiooOooo0 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 Oo0oO0ooo = xbmcgui . DialogProgress ( )
 Oo0oO0ooo . create ( "Your Art Pack Is Downloading" , "Why not check out our website" , '' , 'Http://GenieTv.co.uk' )
 iI111I11i = os . path . join ( IIiooOooo0 , name )
 try :
  os . remove ( iI111I11i )
 except :
  pass
 downloader . download ( url , iI111I11i , Oo0oO0ooo )
 I1 = xbmc . translatePath ( os . path . join ( oo00 ) )
 time . sleep ( 2 )
 Oo0oO0ooo . update ( 0 , "" , "Placing Your Art Please Wait" )
 print '======================================='
 print I1
 print '======================================='
 extract . all ( iI111I11i , I1 , Oo0oO0ooo )
 oooOOOOO = xbmcgui . Dialog ( )
 oooOOOOO . ok ( "GenieTv" , "[COLORred]Once complete your artwork will be stored in your Media folder, Accessible via the Homefolder, Enjoy[/COLOR]" )
 if 48 - 48: oOo0O0Ooo + Ii1I + IIiIiII11i * Ii
 if 13 - 13: ii * OoOOOOO - I1i1III / iIi1i111II + I1i1IiI1 + i1I11i1I
def iii1III1i ( url ) :
 I11i1I1I = OO0oOO0O ( oooo000 + ( i1111 ( 'L0dlbmllVHYvdGVzdC93aC50eHQ=' ) ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 Ii1 = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( I11i1I1I )
 for o0O0oo0OO0O , url , oOOO00o000o , iIi11i1 , oOoO00oo0O in Ii1 :
  ooOOO0 ( o0O0oo0OO0O , url , 5 , oOOO00o000o , iIi11i1 , oOoO00oo0O )
 IiI111111IIII ( 'movies' , 'INFO' )
 if 17 - 17: IIiIiII11i / IIiIiII11i
 if 65 - 65: i1I11i1I + I1ii11iIi11i
def Ooo0O0 ( url ) :
 I11i1I1I = OO0oOO0O ( oooo000 + ( i1111 ( 'L0dlbmllVHYvdGVzdC93aC54bWw=' ) ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 Ii1 = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( I11i1I1I )
 for o0O0oo0OO0O , url , oOOO00o000o , iIi11i1 , oOoO00oo0O in Ii1 :
  ooOOO0 ( o0O0oo0OO0O , url , 30015 , oOOO00o000o , iIi11i1 , oOoO00oo0O )
 IiI111111IIII ( 'movies' , 'MAIN' )
 if 71 - 71: ii
def iIiI1iiiI1ii ( url , iconimage , fanart ) :
 I11i1I1I = OO0oOO0O ( url )
 I1I1I1IIi1III = url
 i11ii1ii11i = iconimage
 fanart = fanart
 Ii1 = re . compile ( 'href="(.+?)">(.+?)</a>' ) . findall ( I11i1I1I )
 for i1I1IiiIi1i , o0O0oo0OO0O in Ii1 :
  if '.mp4' in o0O0oo0OO0O :
   OoOO ( 'Watch VIDEO' , url + '/' + i1I1IiiIi1i , 222 , i11ii1ii11i , fanart , '' )
  if 'description' in o0O0oo0OO0O :
   OoOO ( 'Read Description' , url + '/' + i1I1IiiIi1i , 30017 , i11ii1ii11i , fanart , '' )
  if 'images' in o0O0oo0OO0O :
   ooOOO0 ( 'View Images' , url + '/' + i1I1IiiIi1i , 30018 , i11ii1ii11i , fanart , '' )
  if 'url' in o0O0oo0OO0O :
   OoOO ( 'Install Build On Android' , url + '/' + i1I1IiiIi1i , 30016 , i11ii1ii11i , fanart , '' )
  if 'url' in o0O0oo0OO0O :
   OoOO ( 'Install Build On Pc' , url + '/' + i1I1IiiIi1i , 30019 , i11ii1ii11i , fanart , '' )
 IiI111111IIII ( 'movies' , 'INFO' )
 if 29 - 29: OO0O0OoOO0 . iIi1i111II . oOo0O0Ooo * OOooOOo
def OO00o ( url ) :
 I11i1I1I = OO0oOO0O ( url )
 Ii1 = re . compile ( 'url="(.+?)"' ) . findall ( I11i1I1I )
 for url in Ii1 :
  OOOOoOO0O ( url )
  if 37 - 37: Ii / OO0O0OoOO0
def oo00OoO ( url ) :
 I11i1I1I = OO0oOO0O ( url )
 Ii1 = re . compile ( 'url="(.+?)"' ) . findall ( I11i1I1I )
 for url in Ii1 :
  iIIi1IIi ( url )
  if 43 - 43: Oo0o00 % OO0O0OoOO0
def o0O0ooOOoO ( url ) :
 I11i1I1I = OO0oOO0O ( url )
 Ii1 = re . compile ( 'desc="(.+?)"' ) . findall ( I11i1I1I )
 for iIi11ii in Ii1 :
  o0iI11I1II ( 'Description:' , iIi11ii )
  if 50 - 50: I1i1III / OOooOOo * I1i1III
def Ii1iIi111i1i1 ( url ) :
 I11i1I1I = OO0oOO0O ( url )
 url = url
 Ii1 = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( I11i1I1I )
 for i1I1IiiIi1i , o0O0oo0OO0O in Ii1 :
  if 'png' in o0O0oo0OO0O :
   OoOO ( 'image' , '' , '' , url + '/' + i1I1IiiIi1i , url + '/' + i1I1IiiIi1i , '' )
 IiI111111IIII ( 'movies' , 'MAIN' )
 if 45 - 45: OOooOOo . I11i % OOooOOo * oOo0O0Ooo % oOo0O0Ooo
def oOoOo00ooOooo ( name , url , description ) :
 IIiooOooo0 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 Oo0oO0ooo = xbmcgui . DialogProgress ( )
 Oo0oO0ooo . create ( "GenieTv" , "Downloading Content" , '' , 'Please Wait' )
 iI111I11i = os . path . join ( IIiooOooo0 , name + '.zip' )
 try :
  os . remove ( iI111I11i )
 except :
  pass
 downloader . download ( url , iI111I11i , Oo0oO0ooo )
 IioOoooO00O = xbmc . translatePath ( os . path . join ( 'special://home' , 'addons' ) )
 time . sleep ( 2 )
 Oo0oO0ooo . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print IioOoooO00O
 print '======================================='
 extract . all ( iI111I11i , IioOoooO00O , Oo0oO0ooo )
 oooOOOOO = xbmcgui . Dialog ( )
 oooOOOOO . ok ( "GenieTv" , "Press ok to finish install" , "[COLOR yellow]Brought To You By GenieTv[/COLOR]" )
 oOOOoo00 ( )
 if 6 - 6: I1i1III % ooOoO0O00 . I1i1III * I1i1III
 if 81 - 81: iIi1i111II / iI11I1II1I1I + i1I11i1I
def iIIi1IIi ( url ) :
 IIiooOooo0 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 Oo0oO0ooo = xbmcgui . DialogProgress ( )
 Oo0oO0ooo . create ( "GenieTv" , "Downloading " , '' , 'Please Wait' )
 iI111I11i = os . path . join ( IIiooOooo0 , 'plugin.program.GenieTv.install' + '.zip' )
 try :
  os . remove ( iI111I11i )
 except :
  pass
 downloader . download ( url , iI111I11i , Oo0oO0ooo )
 IioOoooO00O = xbmc . translatePath ( os . path . join ( 'special://' , 'home' ) )
 time . sleep ( 2 )
 Oo0oO0ooo . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print IioOoooO00O
 print '======================================='
 extract . all ( iI111I11i , IioOoooO00O , Oo0oO0ooo )
 i1iiI ( url )
 oooOOOOO = xbmcgui . Dialog ( )
 oooOOOOO . ok ( "GenieTv" , "Press ok to force close kodi, if unsuccessful using windows Please kill kodi via taskmanager" , "[COLOR yellow]Brought To You By GenieTv[/COLOR]" )
 o0OooooOoOO ( )
 if 19 - 19: i1I11i1I
def OOOOoOO0O ( url ) :
 IIiooOooo0 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 Oo0oO0ooo = xbmcgui . DialogProgress ( )
 Oo0oO0ooo . create ( "GenieTv" , "Downloading " , '' , 'Please Wait' )
 iI111I11i = os . path . join ( IIiooOooo0 , 'plugin.program.GenieTv.install' + '.zip' )
 try :
  os . remove ( iI111I11i )
 except :
  pass
 downloader . download ( url , iI111I11i , Oo0oO0ooo )
 IioOoooO00O = xbmc . translatePath ( os . path . join ( 'special://' , 'home' ) )
 time . sleep ( 2 )
 Oo0oO0ooo . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print IioOoooO00O
 print '======================================='
 extract . all ( iI111I11i , IioOoooO00O , Oo0oO0ooo )
 i1iiI ( url )
 oooOOOOO = xbmcgui . Dialog ( )
 oooOOOOO . ok ( "GenieTv" , "DO NOT EXIT CLEANLY VIA SHUTDOWN, Please press home button got to settings/apps and force close kodi and clear cache. " , "[COLOR yellow]Brought To You By GenieTv[/COLOR]" )
 if 78 - 78: iIi1i111II % I11i
 if 39 - 39: Ii1I + oOo0O0Ooo - iI11I1II1I1I - I11i
def I1ii1II1iII ( name , url , description ) :
 IioOoooO00O = xbmc . translatePath ( os . path . join ( 'special://' , 'home' ) )
 Oo0oO0ooo = xbmcgui . DialogProgress ( )
 iI111I11i = os . path . join ( I11 )
 time . sleep ( 2 )
 Oo0oO0ooo . create ( "GenieTv" , "Restoring" , '' , 'Please Wait' )
 print '======================================='
 print IioOoooO00O
 print '======================================='
 extract . all ( iI111I11i , IioOoooO00O , Oo0oO0ooo )
 oooOOOOO = xbmcgui . Dialog ( )
 oooOOOOO . ok ( "GenieTv" , "Please Disconnect The Power From Your Device. DO NOT EXIT CLEANLY VIA SHUTDOWN" , "[COLOR yellow]Brought To You By GenieTv[/COLOR]" )
 if 8 - 8: OOooOOo / o0o00Oo0O * o0o00Oo0O % Oo0o00 - I1ii11iIi11i + I1i1IiI1
 if 83 - 83: o0o00Oo0O . oOo0O0Ooo
def o0OooooOoOO ( ) :
 Ooo0oOooo0 = xbmcgui . Dialog ( ) . yesno ( 'Force Close Kodi' , 'You are about to close Kodi' , 'Would you like to continue?' , nolabel = 'No, Cancel' , yeslabel = 'Yes, Close' )
 if Ooo0oOooo0 == 0 :
  return
 elif Ooo0oOooo0 == 1 :
  pass
 O0OIIi1 = iIII1iiII ( )
 print "Platform: " + str ( O0OIIi1 )
 if O0OIIi1 == 'osx' :
  print "############   try osx force close  #################"
  try : os . system ( 'killall -9 XBMC' )
  except : pass
  try : os . system ( 'killall -9 Kodi' )
  except : pass
  oooOOOOO . ok ( "[COLOR=red][B]WARNING  !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu." , '' )
 elif O0OIIi1 == 'linux' :
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
 elif O0OIIi1 == 'android' :
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
 elif O0OIIi1 == 'windows' :
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
  if 16 - 16: I1ii11iIi11i + oOo / I1ii11iIi11i / oO0o % OoOOOOO % Ii1I
def iIII1iiII ( ) :
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
  if 22 - 22: IIiIiII11i * oO0o * I1i1IiI1 + Ii1I * I11i
  if 100 - 100: ooOoO0O00 / i1I11i1I
  if 3 - 3: IIiIiII11i % Ii1I - ii * I1ii11iIi11i . iI11I1II1I1I
def I1iI ( url ) :
 Oo0oO0ooo . create ( "[COLOR=green]GenieTv[/COLOR]" , "Renaming paths..." , '' , 'Please Wait' )
 for O0o00O0Oo0 , II1I , OoOo000oOo0oo in os . walk ( url ) :
  for file in OoOo000oOo0oo :
   if file . endswith ( ".xml" ) :
    Oo0oO0ooo . update ( 0 , "Fixing" , file , 'Please Wait' )
    Ii1ii111i1 = open ( ( os . path . join ( O0o00O0Oo0 , file ) ) ) . read ( )
    o0I11iII = Ii1ii111i1 . replace ( i1iiIII111ii , 'special://home/' )
    oo0OOo0 = open ( ( os . path . join ( O0o00O0Oo0 , file ) ) , mode = 'w' )
    oo0OOo0 . write ( str ( o0I11iII ) )
    oo0OOo0 . close ( )
 o0OooooOoOO ( )
 if 2 - 2: oOo0O0Ooo + I11i . I11i . o0o00Oo0O / I1i1IiI1
def iIiiIiiIi ( ) :
 OoO000O0Oo = Oo0o0oooo0O0 ( i1111 ( 'aHR0cDovL3d3dy5saXN0ZW5saXZlLmV1Lw==' ) )
 Ii1 = re . compile ( '<a href="(.+?)">(.+?)</a></td></tr>' ) . findall ( OoO000O0Oo )
 for IiIIIIIi , o0O0oo0OO0O in Ii1 :
  iiI11ii1I1 ( o0O0oo0OO0O , 'http://www.listenlive.eu/' + IiIIIIIi , 10111113 , iIIIi1 + 'radio.png' )
def i1iiIIIi ( url ) :
 OoO000O0Oo = Oo0o0oooo0O0 ( url )
 Ii1 = re . compile ( '<tr>.+?<td><a href=".+?"><b>(.+?)</b>.+?<td><a href="(.+?)">' , re . DOTALL ) . findall ( OoO000O0Oo )
 for o0O0oo0OO0O , url in Ii1 :
  Ooo0OOoOoO0 ( o0O0oo0OO0O , url , 222 , iIIIi1 + 'radio.png' )
  if 62 - 62: o0o00Oo0O / oOo0O0Ooo % o0o00Oo0O * oO0o % oOo0O0Ooo
def IiOOoo0oO00oo00 ( ) :
 OoO000O0Oo = Oo0o0oooo0O0 ( i1111 ( 'aHR0cDovL3d3dy50b29uamV0LmNvbS8=' ) )
 Ii1 = re . compile ( '<a href="(.+?)" style="font-size:.8em;">(.+?)</a>' ) . findall ( OoO000O0Oo )
 for IiIIIIIi , o0O0oo0OO0O in Ii1 :
  iiI11ii1I1 ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' , 'http://www.toonjet.com/' + IiIIIIIi , 8051 , iIIIi1 + 'classictoons.png' )
 xbmcplugin . addSortMethod ( I11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
def O0 ( url ) :
 OoO000O0Oo = Oo0o0oooo0O0 ( url )
 Ii1 = re . compile ( '<a href="(.+?)"><img src="(.+?)"' ) . findall ( OoO000O0Oo )
 OOooOO000 = re . compile ( '<a href="(.+?)">.+?</a></td></tr></table>' ) . findall ( OoO000O0Oo )
 for url , i11ii1ii11i in Ii1 :
  if 'ol.gif' in i11ii1ii11i :
   pass
  elif 'link_block_' in i11ii1ii11i :
   pass
  elif '.png' in i11ii1ii11i :
   pass
  else :
   iiI11ii1I1 ( ( i11ii1ii11i ) . replace ( 'http://www.toonjet.com/images/icons/' , '' ) . replace ( 'images/icons/' , '' ) . replace ( '.jpg' , '' ) . replace ( '_icon' , '' ) . replace ( '_' , ' ' ) , 'http://www.toonjet.com/' + url , 8052 , iIIIi1 + 'vod.png' )
 for url in OOooOO000 :
  iiI11ii1I1 ( 'NEXT PAGE' , 'http://www.toonjet.com/' + url , 8051 , iIIIi1 + 'Next.png' )
 xbmcplugin . addSortMethod ( I11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
def iiooO0o0oO ( url ) :
 OoO000O0Oo = Oo0o0oooo0O0 ( url )
 Ii1 = re . compile ( '<iframe width="640" height="480" src="(.+?)" frameborder="0" allowfullscreen></iframe>' ) . findall ( OoO000O0Oo )
 for url in Ii1 :
  Ooo0OOoOoO0 ( '[COLOR' + oO0o0o0ooO0oO + ']PLAY[/COLOR]' , ( url ) . replace ( 'http://www.youtube.com/embed/' , '' ) . replace ( '?autoplay=0' , '' ) , 8043 , iIIIi1 + 'classictoons.png' )
  if 67 - 67: ii
  if 29 - 29: o0o00Oo0O - Ii - IIiIiII11i + iIi1i111II * i1I11i1I
def IiI1ii1Ii ( ) :
 oooOOOoOOOo0O ( 'Audio Books' , '' , 30011 , iIIIi1 + 'AudioBooks.png' , iIIIi1 + 'AudioBooks.png' , '' )
 oooOOOoOOOo0O ( 'Kids Audio Books' , '' , 30006 , iIIIi1 + 'KidsAudioBooks.png' , iIIIi1 + 'KidsAudioBooks.png' , '' )
 if 82 - 82: i1I11i1I * Ii % IIiIiII11i - ii
def OO0Ooo0 ( ) :
 oooOOOoOOOo0O ( 'All' , '' , 30001 , iIIIi1 + 'KodibleAudioBooks.png' , iIIIi1 + 'KodibleAudioBooks.png' , '' )
 oooOOOoOOOo0O ( 'Popular' , '' , 30012 , iIIIi1 + 'POPULARv.png' , iIIIi1 + 'POPULARv.png' , '' )
 oooOOOoOOOo0O ( 'Search' , '' , 30013 , iIIIi1 + 'Search.png' , iIIIi1 + 'Search.png' , '' )
 if 91 - 91: ooOoO0O00 - iI11I1II1I1I
def Oo0Oo00o00oO ( ) :
 oOOoO0O0O0 = OO0oOO0O ( II11iiii1Ii + 'books' + OooO0 )
 Ii1 = re . compile ( '<NAME=>(.*?)</NAME><URL=>(.*?)</URL><CAT=>(.*?)</CAT>' ) . findall ( oOOoO0O0O0 )
 for o0O0oo0OO0O , IiIIIIIi , o0000 in Ii1 :
  if 'Parent' in o0O0oo0OO0O :
   pass
  elif '2' in o0000 :
   oooOOOoOOOo0O ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , IiIIIIIi , 30010 , iIIIi1 + 'KodibleAudioBooks.png' , iIIIi1 + 'KodibleAudioBooks.png' , '' )
   if 42 - 42: Oo0o00 + Oo0o00 * IIiIiII11i
def o0Oo ( ) :
 O0oOOoooOO0O = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 Oo0o0O00 = O0oOOoooOO0O . lower ( )
 oOOoO0O0O0 = OO0oOO0O ( II11iiii1Ii + 'books' + OooO0 )
 Ii1 = re . compile ( '<NAME=>(.*?)</NAME><URL=>(.*?)</URL><CAT=>(.*?)</CAT>' ) . findall ( oOOoO0O0O0 )
 for o0O0oo0OO0O , IiIIIIIi , o0000 in Ii1 :
  if O0oOOoooOO0O in o0O0oo0OO0O . lower ( ) :
   if '1' in o0000 :
    oooOOOoOOOo0O ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , IiIIIIIi , 30010 , iIIIi1 + 'KodibleAudioBooks.png' , iIIIi1 + 'KodibleAudioBooks.png' , '' )
   elif '2' in o0000 :
    oooOOOoOOOo0O ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , IiIIIIIi , 30010 , iIIIi1 + 'KodibleAudioBooks.png' , iIIIi1 + 'KodibleAudioBooks.png' , '' )
   elif '3' in o0000 :
    oooOOOoOOOo0O ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , IiIIIIIi , 30009 , iIIIi1 + 'KodibleAudioBooks.png' , iIIIi1 + 'KodibleAudioBooks.png' , '' )
    if 57 - 57: iIi1i111II / I1ii11iIi11i
    if 69 - 69: OoOOOOO - I1ii11iIi11i % i1I11i1I
def ii1ii11i111IiI ( ) :
 oOOoO0O0O0 = OO0oOO0O ( II11iiii1Ii + 'books' + OooO0 )
 Ii1 = re . compile ( '<NAME=>(.*?)</NAME><URL=>(.*?)</URL><CAT=>(.*?)</CAT>' ) . findall ( oOOoO0O0O0 )
 for o0O0oo0OO0O , IiIIIIIi , o0000 in Ii1 :
  if '1' in o0000 :
   oooOOOoOOOo0O ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , IiIIIIIi , 3010 , iIIIi1 + 'KodibleAudioBooks.png' , iIIIi1 + 'KodibleAudioBooks.png' , '' )
  elif '2' in o0000 :
   oooOOOoOOOo0O ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , IiIIIIIi , 30010 , iIIIi1 + 'KodibleAudioBooks.png' , iIIIi1 + 'KodibleAudioBooks.png' , '' )
  elif '3' in o0000 :
   oooOOOoOOOo0O ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , IiIIIIIi , 30009 , iIIIi1 + 'KodibleAudioBooks.png' , iIIIi1 + 'KodibleAudioBooks.png' , '' )
   if 25 - 25: I1i1IiI1 . oOo0O0Ooo + OoOOOOO
 xbmcplugin . addSortMethod ( I11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 75 - 75: i1I11i1I - I11i % OO0O0OoOO0 + Ii
def O0OOOo ( url ) :
 i1I1IiiIi1i = url
 oOOoO0O0O0 = OO0oOO0O ( url )
 OOooOO000 = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( oOOoO0O0O0 )
 for url , o0O0oo0OO0O in OOooOO000 :
  if 'mp3' in o0O0oo0OO0O :
   ooOOO0 ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' ) . replace ( '%20' , ' ' ) , i1I1IiiIi1i + url , 10012 , iIIIi1 + 'KodibleAudioBooks.png' , iIIIi1 + 'KodibleAudioBooks.png' , '' )
  if 'wma' in o0O0oo0OO0O :
   ooOOO0 ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' ) . replace ( '%20' , ' ' ) , i1I1IiiIi1i + url , 10012 , iIIIi1 + 'KodibleAudioBooks.png' , iIIIi1 + 'KodibleAudioBooks.png' , '' )
  if 'm4b' in o0O0oo0OO0O :
   ooOOO0 ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' ) . replace ( '%20' , ' ' ) , i1I1IiiIi1i + url , 10012 , iIIIi1 + 'KodibleAudioBooks.png' , iIIIi1 + 'KodibleAudioBooks.png' , '' )
  elif '/' in o0O0oo0OO0O :
   oooOOOoOOOo0O ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , i1I1IiiIi1i + url , 30009 , iIIIi1 + 'KodibleAudioBooks.png' , iIIIi1 + 'KodibleAudioBooks.png' , '' )
   if 30 - 30: OO0O0OoOO0 / oO0o + OoOOOOO
   if 6 - 6: OO0O0OoOO0 . I1i1IiI1 + I1i1III . Oo0o00
   if 70 - 70: oO0o
def i1iIi1111 ( url ) :
 oOOoO0O0O0 = OO0oOO0O ( url )
 i1I1IiiIi1i = url
 Ii1 = re . compile ( '<li><a href="(.+?)">(.+?)</a></li>' ) . findall ( oOOoO0O0O0 )
 for url , o0O0oo0OO0O in Ii1 :
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
   ooOOO0 ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , i1I1IiiIi1i + url , 10012 , iIIIi1 + 'KodibleAudioBooks.png' , iIIIi1 + 'KodibleAudioBooks.png' , '' )
  elif 'm4a' in o0O0oo0OO0O :
   ooOOO0 ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , i1I1IiiIi1i + url , 10012 , iIIIi1 + 'KodibleAudioBooks.png' , iIIIi1 + 'KodibleAudioBooks.png' , '' )
  else :
   oooOOOoOOOo0O ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , i1I1IiiIi1i + url , 30010 , iIIIi1 + 'KodibleAudioBooks.png' , iIIIi1 + 'KodibleAudioBooks.png' , '' )
   if 13 - 13: oO0o
   if 37 - 37: I1i1III + Oo0o00 - I1ii11iIi11i + I1i1III
def Oo0o0Oo0O ( ) :
 oooOOOoOOOo0O ( 'A-Z' , '' , 30007 , iIIIi1 + 'KodibleAudioBooks.png' , iIIIi1 + 'KodibleAudioBooks.png' , '' )
 oooOOOoOOOo0O ( 'All' , '' , 30003 , iIIIi1 + 'KodibleAudioBooks.png' , iIIIi1 + 'KodibleAudioBooks.png' , '' )
 oooOOOoOOOo0O ( 'Search' , '' , 30014 , iIIIi1 + 'KodibleAudioBooks.png' , iIIIi1 + 'KodibleAudioBooks.png' , '' )
 if 63 - 63: iI11I1II1I1I
def II1Ii ( ) :
 oOOoO0O0O0 = OO0oOO0O ( i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9tcDNfZG93bmxvYWRzLmh0bQ==' ) )
 Ii1 = re . compile ( '<td width=".+?" align="center">.+?<a href="(.*?)">.+?<img border="0" src="images/Squeeze%20(.*?).gif" width="74" height=".*?"></a></td>' , re . DOTALL ) . findall ( oOOoO0O0O0 )
 for IiIIIIIi , i11ii1ii11i in Ii1 :
  print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<' + IiIIIIIi + '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
  if '-x' in i11ii1ii11i :
   pass
  else :
   oooOOOoOOOo0O ( i11ii1ii11i , ( i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) ) + ( IiIIIIIi ) . replace ( 'colour_it' , 'books_audio/audio_books_a' ) , 30008 , ( i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9pbWFnZXMvU3F1ZWV6ZSUyMA==' ) ) + i11ii1ii11i + '.gif' , iIIIi1 + 'KodibleAudioBooks.png' , '' )
   if 89 - 89: OOooOOo - oO0o
 xbmcplugin . addSortMethod ( I11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 8 - 8: I11i / Ii1I - Ii % iI11I1II1I1I
 if 66 - 66: i1I11i1I
def O0oOo ( url ) :
 oOOoO0O0O0 = OO0oOO0O ( url )
 Ii1 = re . compile ( '<td width=".*?" height=".*?"><b>.*?<a href="(.*?)">(.*?)</a></b></td>' , re . DOTALL ) . findall ( oOOoO0O0O0 )
 for url , o0O0oo0OO0O in Ii1 :
  if '</a>' in o0O0oo0OO0O :
   pass
  elif '(' in o0O0oo0OO0O :
   oooOOOoOOOo0O ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '.mp3' , '' ) , i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) + url , 30005 , iIIIi1 + 'KodibleAudioBooks.png' , iIIIi1 + 'KodibleAudioBooks.png' , '' )
  else :
   ooOOO0 ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '.mp3' , '' ) , i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) + url , 30004 , iIIIi1 + 'KodibleAudioBooks.png' , iIIIi1 + 'KodibleAudioBooks.png' , '' )
   if 68 - 68: Ii1I % ii % Ii1I + Oo0o00
 xbmcplugin . addSortMethod ( I11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 10 - 10: I1ii11iIi11i + o0o00Oo0O
def Ii1iI ( ) :
 O0oOOoooOO0O = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 Oo0o0O00 = O0oOOoooOO0O . lower ( )
 oOOoO0O0O0 = OO0oOO0O ( i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9jb21wbGV0ZV9saXN0Lmh0bQ==' ) )
 Ii1 = re . compile ( '<td width=".+?">.*?<b>.+?<a href="(.*?)">(.*?)</a></b></td>' , re . DOTALL ) . findall ( oOOoO0O0O0 )
 for IiIIIIIi , o0O0oo0OO0O in Ii1 :
  if O0oOOoooOO0O in o0O0oo0OO0O . lower ( ) :
   if '</a>' in o0O0oo0OO0O :
    pass
   elif '(' in o0O0oo0OO0O :
    oooOOOoOOOo0O ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + IiIIIIIi , 30005 , iIIIi1 + 'KodibleAudioBooks.png' , iIIIi1 + 'KodibleAudioBooks.png' , '' )
   else :
    ooOOO0 ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + IiIIIIIi , 30004 , iIIIi1 + 'KodibleAudioBooks.png' , iIIIi1 + 'KodibleAudioBooks.png' , '' )
    if 53 - 53: iI11I1II1I1I - OoOOOOO % OOooOOo * Oo0o00 % oOo
    if 29 - 29: I11i / I1ii11iIi11i * Ii1I . I11i
def oO00 ( ) :
 oOOoO0O0O0 = OO0oOO0O ( i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9jb21wbGV0ZV9saXN0Lmh0bQ==' ) )
 Ii1 = re . compile ( '<td width=".+?">.*?<b>.+?<a href="(.*?)">(.*?)</a></b></td>' , re . DOTALL ) . findall ( oOOoO0O0O0 )
 for IiIIIIIi , o0O0oo0OO0O in Ii1 :
  if '</a>' in o0O0oo0OO0O :
   pass
  elif '(' in o0O0oo0OO0O :
   oooOOOoOOOo0O ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + IiIIIIIi , 30005 , iIIIi1 + 'KodibleAudioBooks.png' , iIIIi1 + 'KodibleAudioBooks.png' , '' )
  else :
   ooOOO0 ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + IiIIIIIi , 30004 , iIIIi1 + 'KodibleAudioBooks.png' , iIIIi1 + 'KodibleAudioBooks.png' , '' )
   if 1 - 1: OoOOOOO
 xbmcplugin . addSortMethod ( I11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 12 - 12: oOo % oOo0O0Ooo + OoOOOOO - ooOoO0O00 . I1i1III / oOo0O0Ooo
 if 51 - 51: iIi1i111II . oOo0O0Ooo
def Oo ( url ) :
 oOOoO0O0O0 = OO0oOO0O ( url )
 Ii1 = re . compile ( '<a href="(.+?)">Download</a></b></td>' ) . findall ( oOOoO0O0O0 )
 for url in Ii1 :
  i1I1IiiIi1i = ( i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) ) + url
  Resolve ( i1I1IiiIi1i )
  if 34 - 34: Oo0o00 % OoOOOOO % OOooOOo
def OO0O00o0 ( url ) :
 oOOoO0O0O0 = OO0oOO0O ( url )
 Ii1 = re . compile ( '<td width="247">(.*?)</td>.*?<a href="(.+?)">' , re . DOTALL ) . findall ( oOOoO0O0O0 )
 for o0O0oo0OO0O , url in Ii1 :
  if '<p align' in o0O0oo0OO0O :
   pass
  elif '&nbsp;' in o0O0oo0OO0O :
   pass
  else :
   ooOOO0 ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) , i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) + url , 10012 , iIIIi1 + 'KodibleAudioBooks.png' , iIIIi1 + 'KodibleAudioBooks.png' , '' )
   if 32 - 32: iIi1i111II / i1I11i1I % oOo + IIiIiII11i
 xbmcplugin . addSortMethod ( I11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 4 - 4: OO0O0OoOO0 - I1ii11iIi11i - i1I11i1I - I1i1IiI1 % Ii / oO0o
 if 50 - 50: oOo + ooOoO0O00
def i11IiIIi11I ( ) :
 oOOoO0O0O0 = cloudflare . source ( i1111 ( 'aHR0cDovL3dhdGNoY2FydG9vbnNvbmxpbmUuZXUv' ) )
 Ii1 = re . compile ( 'class="menu-item menu-item-type-.+?><a href="([^"]*)">(.+?)</a></li>' , re . DOTALL ) . findall ( oOOoO0O0O0 )
 for IiIIIIIi , o0O0oo0OO0O in Ii1 :
  if 'ongoing' in IiIIIIIi :
   ooOOO0 ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' , IiIIIIIi , 21005 , iIIIi1 + 'OnGoing.png' , '' , '' )
  if 'cartoon-series' in IiIIIIIi :
   ooOOO0 ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' , IiIIIIIi , 21005 , iIIIi1 + 'CartoonShows.png' , '' , '' )
  if 'disney' in IiIIIIIi :
   ooOOO0 ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' , IiIIIIIi , 21005 , iIIIi1 + 'Disney.png' , '' , '' )
  if 'genre' in IiIIIIIi :
   ooOOO0 ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' , IiIIIIIi , 21005 , iIIIi1 + 'Genre.png' , '' , '' )
  if 'years' in IiIIIIIi :
   ooOOO0 ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' , IiIIIIIi , 21005 , iIIIi1 + 'Years.png' , '' , '' )
def o000o0O0Oo00 ( url ) :
 oOOoO0O0O0 = cloudflare . source ( url )
 Ii1 = re . compile ( '<a href="([^"]*)" title="([^"]*)" rel="nofollow" id="featured-thumbnail">.+?<div class="featured-thumbnail"><img width="140" height="200" src="([^"]*)"' , re . DOTALL ) . findall ( oOOoO0O0O0 )
 ooOOoOo = re . compile ( '<button type="button"><a href="([^"]*)" target="_blank">(.+?)</a>' ) . findall ( oOOoO0O0O0 )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' ) . findall ( oOOoO0O0O0 )
 for url , o0O0oo0OO0O , i11ii1ii11i in Ii1 :
  ooOOO0 ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) , url , 21006 , i11ii1ii11i , i11ii1ii11i , o0O0oo0OO0O )
 for url , o0O0oo0OO0O in ooOOoOo :
  ooOOO0 ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' , url , 21005 , iIIIi1 + 'watchcartoons.png' , '' , '' )
 for url in next :
  ooOOO0 ( '[COLOR' + oO0o0o0ooO0oO + ']NEXT[/COLOR]' , url , 21005 , iIIIi1 + 'Next.png' , '' , '' )
def oooO ( url ) :
 oOOoO0O0O0 = cloudflare . source ( url )
 Ii1 = re . compile ( '<li><a href="([^"]*)" target=_blank>(.+?)</a></li>' , re . DOTALL ) . findall ( oOOoO0O0O0 )
 iiIIi = re . compile ( 'file:"([^"]*)",type:"mp4",label:"([^"]*)"' , re . DOTALL ) . findall ( oOOoO0O0O0 )
 i1i = re . compile ( 'src="([^"]*)" frameborder=' ) . findall ( oOOoO0O0O0 )
 iIIiI1iiI = re . compile ( '<iframe src="([^"]*)"' ) . findall ( oOOoO0O0O0 )
 for url , o0O0oo0OO0O in Ii1 :
  ooOOO0 ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) . replace ( '&#8217;' , '' ) , url , 21007 , iIIIi1 + 'watchcartoons.png' , '' , '' )
 for url in i1i :
  ooOOO0 ( '[COLOR' + oO0o0o0ooO0oO + ']PLAY[/COLOR]' , 'http:' + url , 222 , iIIIi1 + 'watchcartoons.png' , '' , '' )
 for url , o0O0oo0OO0O in iiIIi :
  OoOO ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' , url , 222 , iIIIi1 + 'watchcartoons.png' , '' , '' )
 else :
  ooOOO0 ( '[COLOR' + oO0o0o0ooO0oO + ']NO STREAMS AVAILABLE[/COLOR]' , url , 21005 , iIIIi1 + 'watchcartoons.png' , '' , '' )
def I11Ii111I ( url ) :
 oOOoO0O0O0 = cloudflare . source ( url )
 Ii1 = re . compile ( 'file:"([^"]*)",type:"mp4",label:"([^"]*)"' , re . DOTALL ) . findall ( oOOoO0O0O0 )
 for url , o0O0oo0OO0O in Ii1 :
  OoOO ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' , url , 222 , iIIIi1 + 'watchcartoons.png' , '' , '' )
  if 98 - 98: iI11I1II1I1I + Oo0o00 % OOooOOo + I1i1IiI1 % OOooOOo
def iI1I1I11IiII ( ) :
 iiI11ii1I1 ( '[COLOR' + oO0o0o0ooO0oO + ']CARTOONS[/COLOR]' , '' , 20001 , iIIIi1 + 'ORIGINCARTOON.png' )
 iiI11ii1I1 ( '[COLOR' + oO0o0o0ooO0oO + ']ANIME[/COLOR]' , 'https://kissanime.to/AnimeList' , 20001 , iIIIi1 + 'ORIGINCARTOON.png' )
 if 47 - 47: OoOOOOO % iI11I1II1I1I
def IiI1IIIII1I ( ) :
 iiI11ii1I1 ( '[COLOR' + oO0o0o0ooO0oO + ']BY NAME[/COLOR]' , 'http://kisscartoon.me/CartoonList' , 20002 , iIIIi1 + 'ORIGINCARTOON.png' )
 iiI11ii1I1 ( '[COLOR' + oO0o0o0ooO0oO + ']BY GENRE[/COLOR]' , 'http://kisscartoon.me/CartoonList' , 20003 , iIIIi1 + 'ORIGINCARTOON.png' )
 if 35 - 35: I1i1III - I1i1III + ooOoO0O00 - o0o00Oo0O - Oo0o00
def oOO0o0oo0 ( url ) :
 oOOoO0O0O0 = cloudflare . source ( url )
 Ii1 = re . compile ( 'href="(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( oOOoO0O0O0 )
 for url , o0O0oo0OO0O in Ii1 :
  if '?c=' in url :
   iiI11ii1I1 ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' , 'http://kisscartoon.me' + url , 20004 , iIIIi1 + 'ORIGINCARTOON.png' )
   if 78 - 78: iIi1i111II + OO0O0OoOO0 . i1I11i1I
def OoIIi1iI ( url ) :
 oOOoO0O0O0 = cloudflare . source ( url )
 Ii1 = re . compile ( 'href="(.+?)" title="(.+?)">/n(.+?)</a><br/>' , re . DOTALL ) . findall ( oOOoO0O0O0 )
 for url , oO0Ooo0OooOOo , o0O0oo0OO0O in Ii1 :
  if 'Genre' in url :
   iiI11ii1I1 ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' , 'http://kisscartoon.me' + url , 20004 , iIIIi1 + 'ORIGINCARTOON.png' )
   if 71 - 71: i1I11i1I + ooOoO0O00 * I1ii11iIi11i % I1ii11iIi11i / I1ii11iIi11i
def OoO00o0 ( url ) :
 oOOoO0O0O0 = cloudflare . source ( url )
 Ii1 = re . compile ( 'src="(.+?)" style=.+?<a class="bigChar" href="(.+?)">(.+?)</a>.+?<p>(.+?)</p>' , re . DOTALL ) . findall ( oOOoO0O0O0 )
 for url , oO0Ooo0OooOOo , o0O0oo0OO0O in Ii1 :
  ooOOO0 ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' , 'http://kisscartoon.me' + url , 20005 , img , '' , oO0Ooo0OooOOo )
  if 68 - 68: o0o00Oo0O
def II1iIII ( url ) :
 oOOoO0O0O0 = cloudflare . source ( url )
 Ii1 = re . compile ( '<img width="120" height="165" src="(.+?)" style=.+?<a class="bigChar" href="(.+?)">(.+?)</a>.+?<p>(.+?)</p>' , re . DOTALL ) . findall ( oOOoO0O0O0 )
 for url , oO0Ooo0OooOOo , o0O0oo0OO0O in Ii1 :
  ooOOO0 ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' , 'http://kisscartoon.me' + url , 20005 , img , '' , oO0Ooo0OooOOo )
  if 79 - 79: ii + Ii1I - I1ii11iIi11i + ii
  if 61 - 61: ooOoO0O00 * oO0o - I1ii11iIi11i - oOo
  if 57 - 57: OOooOOo . iI11I1II1I1I % oOo % I1i1III * OOooOOo
  if 8 - 8: OOooOOo . oOo % OoOOOOO . oOo0O0Ooo % oOo0O0Ooo . I1i1III
  if 47 - 47: I1i1IiI1 + oOo + IIiIiII11i % Ii
def OOoOoo00Oo ( ) :
 if 9 - 9: IIiIiII11i * IIiIiII11i . Ii * iI11I1II1I1I
 ooOOO0 ( '[COLOR' + oO0o0o0ooO0oO + ']Cartoons[/COLOR]' , i1111 ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2NhcnRvb24=' ) , 10004 , iIIIi1 + 'ORIGINCARTOON.png' , i1iIIi1 , '' )
 ooOOO0 ( '[COLOR' + oO0o0o0ooO0oO + ']Search Cartoons[/COLOR]' , '' , 10005 , iIIIi1 + 'ORIGINCARTOON.png' , i1iIIi1 , '' )
 if 18 - 18: oO0o . IIiIiII11i % OOooOOo % I1i1III
def oo0 ( ) :
 O0oOOoooOO0O = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 Oo0o0O00 = O0oOOoooOO0O . lower ( )
 oOOoO0O0O0 = OO0oOO0O ( i1111 ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2NhcnRvb24=' ) )
 if 16 - 16: I1i1III * oO0o / OoOOOOO
 Ii1 = re . compile ( '<td><a href="(.+?)">(.+)</a></td>' ) . findall ( oOOoO0O0O0 )
 if 22 - 22: OoOOOOO + iI11I1II1I1I % I1ii11iIi11i / I1i1IiI1 / I1i1III
 for IiIIIIIi , o0O0oo0OO0O in Ii1 :
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
    ooOOO0 ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' , IiIIIIIi , 10006 , iIIIi1 + 'ORIGINCARTOON.png' , i1iIIi1 , '' )
    if 54 - 54: OOooOOo % i1I11i1I . Ii
    if 93 - 93: oOo % Ii % Oo0o00
  xbmcplugin . addSortMethod ( I11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 64 - 64: Oo0o00 + oOo0O0Ooo * o0o00Oo0O / I1ii11iIi11i - I1i1IiI1 % I1i1IiI1
def o0oO00 ( url ) :
 OoO000O0Oo = OO0oOO0O ( url )
 Ii1 = re . compile ( '<td><a href="(.+?)">(.+)</a></td>' ) . findall ( OoO000O0Oo )
 for url , o0O0oo0OO0O in Ii1 :
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
   ooOOO0 ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' , url , 10006 , iIIIi1 + 'ORIGINCARTOON.png' , i1iIIi1 , '' )
 xbmcplugin . addSortMethod ( I11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 2 - 2: iI11I1II1I1I
def iiii1 ( url ) :
 OoO000O0Oo = OO0oOO0O ( url )
 OOooOO000 = re . compile ( '<img src="(.+?)" id="series_image" width="250" height="370" alt=".+?" />' ) . findall ( OoO000O0Oo )
 for i11ii1ii11i in OOooOO000 :
  OO0o0oO0O000o = i11ii1ii11i
 I1iI11iii = re . compile ( '<li><a href="(.+?)">Next</a></li>' ) . findall ( OoO000O0Oo )
 for url in I1iI11iii :
  ooOOO0 ( '[COLOR' + oO0o0o0ooO0oO + ']NEXT PAGE[/COLOR]' , url , 10006 , iIIIi1 + 'Next.png' , i1iIIi1 , '' )
 Ii1 = re . compile ( '&nbsp;<a href="(.+?)">(.+?)</a>' ) . findall ( OoO000O0Oo )
 for url , o0O0oo0OO0O in Ii1 :
  Ooo0OOoOoO0 ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' , url , 10007 , OO0o0oO0O000o )
  if 78 - 78: o0o00Oo0O / IIiIiII11i * oO0o
  if 50 - 50: ii - iI11I1II1I1I + ooOoO0O00 % Oo0o00 - iI11I1II1I1I % o0o00Oo0O
 xbmcplugin . addSortMethod ( I11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 58 - 58: i1I11i1I + iI11I1II1I1I
def Oo00OO0OO ( url , IMAGE ) :
 OoO000O0Oo = OO0oOO0O ( url )
 Ii1 = re . compile ( '"playlist">(.+?)</span></div><div><iframe src="(.+?)"' ) . findall ( OoO000O0Oo )
 for o0O0oo0OO0O , url in Ii1 :
  print o0O0oo0OO0O + '     ' + url
  if 'easy' in url :
   OOo00OO0O0O ( url )
   if 64 - 64: I11i . o0o00Oo0O * I1i1III + ii - I1ii11iIi11i . ii
   if 70 - 70: I1ii11iIi11i - OoOOOOO . iI11I1II1I1I % I1i1IiI1 / OOooOOo - o0o00Oo0O
  xbmcplugin . addSortMethod ( I11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 55 - 55: OO0O0OoOO0 - oO0o
def OOo00OO0O0O ( url ) :
 OoO000O0Oo = OO0oOO0O ( url )
 Ii1 = re . compile ( "url: '(.+?)'," ) . findall ( OoO000O0Oo )
 for url in Ii1 :
  o0i1I11iI1iiI ( url )
  if 48 - 48: I1i1IiI1 . ii . oOo0O0Ooo . OOooOOo % Ii1I / OO0O0OoOO0
  if 11 - 11: ooOoO0O00 % oO0o % OO0O0OoOO0
  if 99 - 99: oOo / iI11I1II1I1I - I1i1III * Ii1I % oOo0O0Ooo
def i1II1i ( ) :
 if 10 - 10: I1i1III - OOooOOo . ii . iIi1i111II . oO0o * OO0O0OoOO0
 ooOOO0 ( '[COLOR' + oO0o0o0ooO0oO + ']Stand Up[/COLOR]' , '' , 10014 , iIIIi1 + 'StandUp.png' , i1iIIi1 , '' )
 ooOOO0 ( '[COLOR' + oO0o0o0ooO0oO + ']Search Comedian[/COLOR]' , '' , 10015 , iIIIi1 + 'SearchComedian.png' , i1iIIi1 , '' )
 ooOOO0 ( '[COLOR' + oO0o0o0ooO0oO + ']Others[/COLOR]' , '' , 10017 , iIIIi1 + 'Others.png' , i1iIIi1 , '' )
 if 78 - 78: OoOOOOO / oO0o - OoOOOOO * ii . OOooOOo
def OOoooOoO0Oo ( ) :
 oOOoO0O0O0 = OO0oOO0O ( ( i1111 ( 'aHR0cDovL2JhY2syYmFzaWNzYnVpbGQuY28udWsvdGVzdC9zdGFuZHVwbGlzdC5waHA=' ) ) )
 Ii1 = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( oOOoO0O0O0 )
 for IiIIIIIi , i11ii1ii11i , o0O0oo0OO0O in Ii1 :
  if 'elete' in o0O0oo0OO0O :
   pass
  else :
   Ooo0OOoOoO0 ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' , IiIIIIIi , 222 , i11ii1ii11i )
   if 78 - 78: ii / iIi1i111II % OOooOOo * ii
def ooOO00o00 ( ) :
 O0oOOoooOO0O = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 Oo0o0O00 = O0oOOoooOO0O . lower ( )
 oOOoO0O0O0 = OO0oOO0O ( ( i1111 ( 'aHR0cDovL3d3dy5jb3VjaHRyaXBwZXIuY29tL2ZvcnVtMi9wYWdlLnBocD9wYWdlPTM=' ) ) )
 Ii11Iii = re . compile ( '<tr>.+?<td width=".+?" align=".+?">.+?<img border=".+?" src="..(.+?)" width=".+?" height=".+?"></td>.+?<td width=".+?" valign=".+?" align=".+?"><font size=".+?">(.+?)</font></td>.+?<td width=".+?">(.+?)</td>' , re . DOTALL ) . findall ( oOOoO0O0O0 )
 for i11ii1ii11i , ooo00OoOO0o , i1iII1IiiIiI1 in Ii11Iii :
  for O0oOOoooOO0O in ooo00OoOO0o :
   print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< img >>>>>>>>>>>>>>>>>>>>>>>>>>'
   oo0O0o = re . compile ( '<a href="(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( i1iII1IiiIiI1 )
   for IiIIIIIi , o0O0oo0OO0O in oo0O0o :
    if 'tube' in IiIIIIIi :
     pass
    elif 'stage' in IiIIIIIi :
     Ooo0OOoOoO0 ( '[COLOR' + oO0o0o0ooO0oO + ']' + ooo00OoOO0o + '   -   ' + o0O0oo0OO0O + '[/COLOR]' , ( IiIIIIIi ) . replace ( '" target="_blank' , '' ) , 10016 , 'http://couchtripper.com/' + i11ii1ii11i , )
    elif 'vee' in IiIIIIIi :
     pass
     if 13 - 13: iI11I1II1I1I . OOooOOo * oOo0O0Ooo / OoOOOOO * I1i1III
def O00o ( ) :
 oOOoO0O0O0 = OO0oOO0O ( ( i1111 ( 'aHR0cDovL3d3dy5jb3VjaHRyaXBwZXIuY29tL2ZvcnVtMi9wYWdlLnBocD9wYWdlPTM=' ) ) )
 Ii11Iii = re . compile ( '<tr>.+?<td width=".+?" align=".+?">.+?<img border=".+?" src="..(.+?)" width=".+?" height=".+?"></td>.+?<td width=".+?" valign=".+?" align=".+?"><font size=".+?">(.+?)</font></td>.+?<td width=".+?">(.+?)</td>' , re . DOTALL ) . findall ( oOOoO0O0O0 )
 for i11ii1ii11i , ooo00OoOO0o , i1iII1IiiIiI1 in Ii11Iii :
  oo0O0o = re . compile ( '<a href="(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( i1iII1IiiIiI1 )
  for IiIIIIIi , o0O0oo0OO0O in oo0O0o :
   if 'tube' in IiIIIIIi :
    pass
   elif 'stage' in IiIIIIIi :
    Ooo0OOoOoO0 ( '[COLOR' + oO0o0o0ooO0oO + ']' + ooo00OoOO0o + '   -   ' + o0O0oo0OO0O + '[/COLOR]' , ( IiIIIIIi ) . replace ( '" target="_blank' , '' ) , 10016 , 'http://couchtripper.com/' + i11ii1ii11i )
   elif 'vee' in IiIIIIIi :
    pass
    if 86 - 86: Ii1I * IIiIiII11i * I1i1IiI1
    if 74 - 74: Ii1I / i1I11i1I
 xbmcplugin . addSortMethod ( I11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 60 - 60: Ii1I
def IIoO00OoOo ( url ) :
 oOOoO0O0O0 = OO0oOO0O ( url )
 print '>>>>>>>>>>>>>>>>>>>>>>>>' + url + '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'
 IIi = re . compile ( "url\[.+?\] = '(.+?)';" ) . findall ( oOOoO0O0O0 )
 print '>>>>>>>>>>>>>>>>>>>>>>>' + ( str ( IIi ) ) + '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
 for url in IIi :
  o0i1I11iI1iiI ( ( url ) . replace ( '[' , '' ) . replace ( ']' , '' ) . replace ( '\'' , '' ) )
  if 74 - 74: IIiIiII11i . o0o00Oo0O - oOo0O0Ooo + i1I11i1I % Ii % OOooOOo
  if 78 - 78: I1i1III + OOooOOo + i1I11i1I - i1I11i1I . Ii / oO0o
  if 27 - 27: I1i1III - o0o00Oo0O % I1i1IiI1 * Oo0o00 . i1I11i1I % iI11I1II1I1I
  if 37 - 37: ii + o0o00Oo0O - ooOoO0O00 % oOo
  if 24 - 24: OOooOOo
  if 94 - 94: ooOoO0O00 * ooOoO0O00 % IIiIiII11i + iIi1i111II
  if 28 - 28: oOo0O0Ooo
def I11o0000o0Oo ( ) :
 if 90 - 90: iI11I1II1I1I * IIiIiII11i
 oOOo0OoOOOoo ( '[COLOR darkgoldenrod]Open Pandora\'s Box[/COLOR]' , '' , 10029 , 'https://encrypted-tbn1.gstatic.com/images?q=tbn%3AANd9GcTQ9r4TA8yIw9ggxuwsHxWojo6tPVfgTe8QIOxOQwzNR2TavtCi6Q' , i1iIIi1 , '' )
 oOOo0OoOOOoo ( '[COLOR darkgoldenrod]Search[/COLOR]' , '' , 10026 , 'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png' , i1iIIi1 , '' )
 if 88 - 88: OoOOOOO * oO0o
 IiI111111IIII ( 'movies' , 'MAIN' )
 if 35 - 35: Ii1I / OO0O0OoOO0 % oOo0O0Ooo + iI11I1II1I1I
def oO00o ( ) :
 oOOo0OoOOOoo ( 'Search Pandoras Films' , '' , 10027 , 'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png' , i1iIIi1 , '' )
 oOOo0OoOOOoo ( 'Search Pandoras TV' , '' , 10028 , 'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png' , i1iIIi1 , '' )
 if 36 - 36: Oo0o00 . IIiIiII11i % oOo
 IiI111111IIII ( 'movies' , 'MAIN' )
def OoooooooO ( ) :
 if 4 - 4: I1ii11iIi11i + I11i
 O0oOOoooOO0O = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 Oo0o0O00 = O0oOOoooOO0O . lower ( )
 iIIiIii11i1Ii = [ 'hey1080p' , 'hey3D' , 'hey' , '480p' , '720p' , '1080p' , 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' , '720paction' , '720padventure' , '720panimation' , '720pcomedy' , '720pcrime' , '720pdocumentary' , '720pdrama' , '720pfamily' , '720pfantasy' , '720phorror' , '720pmystery' , '720promance' , '720psci-Fi' , '720psport' , '720pthriller' , '720pwestern' , '1080paction' , '1080padventure' , '1080panimation' , '1080pcomedy' , '1080pcrime' , '1080pdocumentary' , '1080pdrama' , '1080pfamily' , '1080pfantasy' , '1080phorror' , '1080pmystery' , '1080promance' , '1080psci-Fi' , '1080psport' , '1080pthriller' , '1080pwestern' , 'top10animation' , 'top10biography' , 'top10comedy' , 'top10crime' , 'top10documentary' , 'top10drama' , 'top10family' , 'top10fantasy' , 'top10horror' , 'top10mystery' , 'top10romance' , 'top10sci-fi' , 'top10sport' , 'top10thriller' , 'top10western' , 'top10action' , 'top10music' ]
 if 95 - 95: iI11I1II1I1I - Oo0o00 - iIi1i111II + Oo0o00 % Ii1I . oOo0O0Ooo
 for IiiIIi1 in iIIiIii11i1Ii :
  iI1iIiiI = iiiiiIIii + IiiIIi1 + OooO0
  oOOoO0O0O0 = oo0OooOOo0 ( iI1iIiiI )
  Ii1 = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( oOOoO0O0O0 )
  for IiIIIIIi , oOOO00o000o , O00OoOO0oo0 , iIi11i1 , o0O0oo0OO0O in Ii1 :
   if O0oOOoooOO0O in o0O0oo0OO0O . lower ( ) :
    Oo0OOo ( o0O0oo0OO0O , IiIIIIIi , 222 , oOOO00o000o , iIi11i1 , O00OoOO0oo0 )
    if 36 - 36: o0o00Oo0O * oO0o % OO0O0OoOO0 * OO0O0OoOO0 / oO0o * i1I11i1I
    IiI111111IIII ( 'movies' , 'MAIN' )
    xbmcplugin . addSortMethod ( I11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
    if 14 - 14: ooOoO0O00 . i1I11i1I + o0o00Oo0O * oOo
    if 76 - 76: oO0o
def o00ooOOo ( ) :
 if 83 - 83: Ii1I / Ii + IIiIiII11i . OO0O0OoOO0 * iIi1i111II + i1I11i1I
 O0oOOoooOO0O = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 Oo0o0O00 = O0oOOoooOO0O . lower ( )
 iIIiIii11i1Ii = [ 'tvnum' , 'a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' , 'p' , 'q' , 'r' , 's' , 't' , 'u' , 'v' , 'w' , 'x' , 'y' , 'z' ]
 if 42 - 42: ooOoO0O00 % IIiIiII11i . oOo
 for IiiIIi1 in iIIiIii11i1Ii :
  II1II1iI = iiiiiIIii + IiiIIi1 + OooO0
  oOOoO0O0O0 = oo0OooOOo0 ( II1II1iI )
  Ii1 = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( oOOoO0O0O0 )
  for o0O0oo0OO0O , O00OoOO0oo0 , IiIIIIIi , i11ii1ii11i , iIi11i1 , OooooO in Ii1 :
   if O0oOOoooOO0O in o0O0oo0OO0O . lower ( ) :
    oOOo0OoOOOoo ( o0O0oo0OO0O , IiIIIIIi , OooooO , i11ii1ii11i , iIi11i1 , O00OoOO0oo0 )
    if 92 - 92: I11i / I11i * I1i1III
    IiI111111IIII ( 'movies' , 'MAIN' )
    xbmcplugin . addSortMethod ( I11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
    if 19 - 19: I1i1III
    if 55 - 55: iIi1i111II % iIi1i111II / o0o00Oo0O % OO0O0OoOO0 - I11i . I1ii11iIi11i
def iiiii1I1III1 ( ) :
 if 12 - 12: OO0O0OoOO0 . OOooOOo * oOo0O0Ooo
 OoO000O0Oo = OO0oOO0O ( iiiiiIIii + 'spongemain.php' )
 Ii1 = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( OoO000O0Oo )
 for o0O0oo0OO0O , O00OoOO0oo0 , IiIIIIIi , i11ii1ii11i , iIi11i1 , OooooO in Ii1 :
  oOOo0OoOOOoo ( o0O0oo0OO0O , IiIIIIIi , OooooO , i11ii1ii11i , iIi11i1 , O00OoOO0oo0 )
  IiI111111IIII ( 'movies' , 'MAIN' )
def II1I1i1i1iii ( url ) :
 if 14 - 14: iIi1i111II
 xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
 o0oo0Ooooo0 = ( '%s%s' % ( Oo0oOo000OoO0 , url ) )
 I11i1I1I = OO0oOO0O ( url )
 Ii1 = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( I11i1I1I )
 for url , oOOO00o000o , O00OoOO0oo0 , IIii1I1i , o0O0oo0OO0O in Ii1 :
  IIII1iIIii = re . compile ( 'url="(.+?)"\n' ) . findall ( str ( OOO00 ) )
  for IiiOooooOo0 in IIII1iIIii :
   if IiiOooooOo0 == url :
    o0O0oo0OO0O = ( '[COLORred]Watched - [/COLOR]' + o0O0oo0OO0O ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' )
  Oo0OOo ( o0O0oo0OO0O , url , 222 , oOOO00o000o , IIii1I1i , O00OoOO0oo0 )
  if 45 - 45: i1I11i1I / o0o00Oo0O / OOooOOo * iIi1i111II
  IiI111111IIII ( 'movies' , 'MAIN' )
  if 18 - 18: iI11I1II1I1I + iIi1i111II + iI11I1II1I1I . Ii1I + Oo0o00 . oOo
  xbmcplugin . addSortMethod ( I11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 7 - 7: Ii1I + iI11I1II1I1I * I1i1IiI1 * I1i1IiI1 / IIiIiII11i - I1i1III
  if 65 - 65: OoOOOOO + OOooOOo + IIiIiII11i
def oOOooi1I1iIii11 ( url ) :
 if 80 - 80: OOooOOo - IIiIiII11i
 OoO000O0Oo = OO0oOO0O ( url )
 Ii1 = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( OoO000O0Oo )
 for o0O0oo0OO0O , O00OoOO0oo0 , url , i11ii1ii11i , iIi11i1 , OooooO in Ii1 :
  oOOo0OoOOOoo ( o0O0oo0OO0O , url , OooooO , i11ii1ii11i , iIi11i1 , O00OoOO0oo0 )
  if 35 - 35: oOo - oO0o . I1ii11iIi11i * I1ii11iIi11i / Ii + Ii1I
  IiI111111IIII ( 'movies' , 'MAIN' )
  if 87 - 87: OOooOOo % iI11I1II1I1I
  if 72 - 72: iIi1i111II . iIi1i111II - Ii1I
 xbmcplugin . addSortMethod ( I11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 48 - 48: I1ii11iIi11i - oOo + I1ii11iIi11i - oOo0O0Ooo * Ii . OO0O0OoOO0
def Oo0OOo ( name , url , mode , iconimage , fanart , description ) :
 if 35 - 35: i1I11i1I . o0o00Oo0O + I1ii11iIi11i + iIi1i111II + ooOoO0O00
 OooOooO0O0o0 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 OOO0o0 = True
 IIIIII111Ii = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 IIIIII111Ii . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 IIIIII111Ii . setProperty ( "Fanart_Image" , fanart )
 OOO0o0 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = OooOooO0O0o0 , listitem = IIIIII111Ii , isFolder = False )
 return OOO0o0
 if 5 - 5: ooOoO0O00 + o0o00Oo0O % o0o00Oo0O * o0o00Oo0O + OOooOOo % ooOoO0O00
def oOOo0OoOOOoo ( name , url , mode , iconimage , fanart , description ) :
 if 80 - 80: OO0O0OoOO0 / I11i + oO0o / OoOOOOO
 OooOooO0O0o0 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 OOO0o0 = True
 IIIIII111Ii = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 IIIIII111Ii . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 IIIIII111Ii . setProperty ( "Fanart_Image" , fanart )
 OOO0o0 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = OooOooO0O0o0 , listitem = IIIIII111Ii , isFolder = True )
 return OOO0o0
if 46 - 46: Ii / i1I11i1I % ooOoO0O00 - I1i1IiI1 * OOooOOo
if 94 - 94: I1i1III - Ii1I + I11i - I1ii11iIi11i
if 15 - 15: iIi1i111II
if 31 - 31: OO0O0OoOO0 / ooOoO0O00 . oO0o
if 83 - 83: OoOOOOO / iI11I1II1I1I + ooOoO0O00 / OO0O0OoOO0
if 47 - 47: OoOOOOO + ii . IIiIiII11i . OO0O0OoOO0
if 66 - 66: oOo * OOooOOo
if 2 - 2: OoOOOOO . Oo0o00 * I1ii11iIi11i + o0o00Oo0O - I1i1IiI1 * iI11I1II1I1I
if 12 - 12: I11i * Oo0o00 % IIiIiII11i * ooOoO0O00 * iI11I1II1I1I
if 81 - 81: I1ii11iIi11i - I1i1IiI1
if 24 - 24: ii . oO0o * IIiIiII11i
if 59 - 59: Oo0o00 + oO0o / iIi1i111II
if 97 - 97: I1ii11iIi11i * OO0O0OoOO0 % oOo . OO0O0OoOO0 - Oo0o00 - iIi1i111II
if 79 - 79: oOo0O0Ooo - oOo
if 37 - 37: i1I11i1I . I1ii11iIi11i * I1ii11iIi11i * IIiIiII11i * o0o00Oo0O
def o00O ( string ) :
 if i1I1iI == 'true' :
  xbmc . log ( "[addon.live.GenieTV-%s]: %s" % ( addon_version , string ) )
  if 88 - 88: Ii + OO0O0OoOO0 * OOooOOo * OO0O0OoOO0 + I1i1IiI1
def O0OOO00OooO ( name , url , iconimage , fanart , mode , playlist = None , regexs = None ) :
 OOOiI1 = [ ]
 try :
  if 84 - 84: iIi1i111II * oOo0O0Ooo % I1i1IiI1 + iIi1i111II / OO0O0OoOO0
  name = name . encode ( 'utf-8' , 'ignore' )
 except :
  pass
 if os . path . exists ( o0 ) == False :
  o00O ( 'Making Favorites File' )
  OOOiI1 . append ( ( name , url , iconimage , fanart , mode , playlist , regexs ) )
  Ii1ii111i1 = open ( o0 , "w" )
  Ii1ii111i1 . write ( json . dumps ( OOOiI1 ) )
  Ii1ii111i1 . close ( )
 else :
  o00O ( 'Appending Favorites' )
  Ii1ii111i1 = open ( o0 ) . read ( )
  oo000o = json . loads ( Ii1ii111i1 )
  oo000o . append ( ( name , url , iconimage , fanart , mode ) )
  o0I11iII = open ( o0 , "w" )
  o0I11iII . write ( json . dumps ( oo000o ) )
  o0I11iII . close ( )
  if 95 - 95: OoOOOOO - oOo * I1i1IiI1 / oO0o / IIiIiII11i + o0o00Oo0O
  if 37 - 37: I1i1IiI1 . Oo0o00 + iIi1i111II + I1i1IiI1 . i1I11i1I / I1i1III
def i1I ( ) :
 if os . path . exists ( o0 ) == False :
  OOOiI1 = [ ]
  o00O ( 'Making Favorites File' )
  OOOiI1 . append ( ( 'Genie Tv Favourites Section' , '' , '' , '' , '' , '' , '' ) )
  Ii1ii111i1 = open ( o0 , "w" )
  Ii1ii111i1 . write ( json . dumps ( OOOiI1 ) )
  Ii1ii111i1 . close ( )
 else :
  oOOoooO0O0 = json . loads ( open ( o0 ) . read ( ) )
  ii1O0ooooo000 = len ( oOOoooO0O0 )
  for OooOoOO0OO in oOOoooO0O0 :
   o0O0oo0OO0O = OooOoOO0OO [ 0 ]
   IiIIIIIi = OooOoOO0OO [ 1 ]
   oOOO00o000o = OooOoOO0OO [ 2 ]
   try :
    I1iiIiiii1111 = OooOoOO0OO [ 3 ]
    if I1iiIiiii1111 == None :
     raise
   except :
    if o0oO0 . getSetting ( 'use_thumb' ) == "true" :
     I1iiIiiii1111 = oOOO00o000o
    else :
     I1iiIiiii1111 = iIi11i1
   try : I1ii1i11i = OooOoOO0OO [ 5 ]
   except : I1ii1i11i = None
   try : Oooooo0O00o = OooOoOO0OO [ 6 ]
   except : Oooooo0O00o = None
   if 36 - 36: OOooOOo + i1I11i1I * o0o00Oo0O . ii * ii
   if OooOoOO0OO [ 4 ] == 0 :
    ooOOO0 ( o0O0oo0OO0O , IiIIIIIi , '' , oOOO00o000o , iIi11i1 , '' , 'fav' )
   else :
    ooOOO0 ( o0O0oo0OO0O , IiIIIIIi , OooOoOO0OO [ 4 ] , oOOO00o000o , iIi11i1 , '' , 'fav' )
    if 51 - 51: Ii1I * Ii1I
def OOo000o0 ( name ) :
 oo000o = json . loads ( open ( o0 ) . read ( ) )
 for o00oo0OO0 in range ( len ( oo000o ) ) :
  if oo000o [ o00oo0OO0 ] [ 0 ] == name :
   del oo000o [ o00oo0OO0 ]
   o0I11iII = open ( o0 , "w" )
   o0I11iII . write ( json . dumps ( oo000o ) )
   o0I11iII . close ( )
   break
 xbmc . executebuiltin ( "XBMC.Container.Refresh" )
 if 60 - 60: oOo
 if 66 - 66: I1i1IiI1 / oOo % ooOoO0O00 - OoOOOOO . o0o00Oo0O / o0o00Oo0O
def Iiiiii111i1ii ( ) :
 oo00o0 = os . path . join ( iIii1 , 'addons.ini' )
 I1IiI = open ( oo00o0 , "w+" )
 if 44 - 44: iIi1i111II / iIi1i111II . I11i % i1I11i1I + OOooOOo
 I1IiI . write ( r'# This file contains the "built-in" channels' + '\n' )
 I1IiI . write ( r'# It is parsed by Pythons ConfigParser' + '\n\n' )
 I1IiI . write ( r'[plugin.video.GenieTv]' + '\n' )
 I1IiI . write ( r'BBC One=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F191.m3u8&mode=10012&name===BBC+One+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/bbc_one.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/bbc_one.jpg+&amp;description=' + '\n' )
 I1IiI . write ( r'BBC Two=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F190.m3u8&mode=10012&name===BBC+Two+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/bbc_two_uk.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/bbc_two_uk.jpg+&amp;description=' + '\n' )
 I1IiI . write ( r'BBC Three=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F189.m3u8&mode=10012&name===BBC+Three+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/bbc_three.jpg&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/bbc_three.jpg&amp;description=' + '\n' )
 I1IiI . write ( r'BBC Four=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F188.m3u8&mode=10012&name===BBC+Four+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/bbc_four_uk.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/bbc_four_uk.jpg+&amp;description=' + '\n' )
 I1IiI . write ( r'ITV=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F208.m3u8&mode=10012&name===ITV1+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/itv_uk_london.jpg&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/itv_uk_london.jpg&amp;description=' + '\n' )
 I1IiI . write ( r'ITV2=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F207.m3u8&mode=10012&name===ITV2+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/itv2.jpg++&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/itv2.jpg++&amp;description=' + '\n' )
 I1IiI . write ( r'ITV3=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F206.m3u8&mode=10012&name===ITV3+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/itv3.jpg++&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/itv3.jpg++&amp;description=' + '\n' )
 I1IiI . write ( r'ITV4=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F205.m3u8&mode=10012&name===ITV4+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/itv4.jpg++&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/itv4.jpg++&amp;description=' + '\n' )
 I1IiI . write ( r'ITV Encore=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F328.m3u8&mode=10012&name===ITV+Encore&amp;iconimage=http%3A//j.static-locatetv.com/images/content/mid/3/1026632_the_encore_hour.jpg&amp;fanart=http%3A//j.static-locatetv.com/images/content/mid/3/1026632_the_encore_hour.jpg&amp;description=' + '\n' )
 I1IiI . write ( r'ITVBe=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F203.m3u8&mode=10012&name===ITV+BE+UK&amp;iconimage=http%3A//hub.tv-ark.org.uk/images/itv/images/itv_be.jpg+&amp;fanart=http%3A//hub.tv-ark.org.uk/images/itv/images/itv_be.jpg+&amp;description=' + '\n' )
 I1IiI . write ( r'E4=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F775.m3u8&mode=10012&name===E4+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/e4_uk.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/e4_uk.jpg+&amp;description=' + '\n' )
 I1IiI . write ( r'More4=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F776.m3u8&mode=10012&name===More4+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/channel4_more4_uk.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/channel4_more4_uk.jpg+&amp;description=' + '\n' )
 I1IiI . write ( r'5STAR=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F187.m3u8&mode=10012&name===5%2A+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/channel5_star.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/channel5_star.jpg+&amp;description=' + '\n' )
 I1IiI . write ( r'5 USA=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F186.m3u8&mode=10012&name===5USA+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/channel5_usa.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/channel5_usa.jpg+&amp;description=' + '\n' )
 I1IiI . write ( r'Channel 4=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F183.m3u8&mode=10012&name===Channel+4+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/channel4_ie.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/channel4_ie.jpg+&amp;description=' + '\n' )
 I1IiI . write ( r'Channel 5=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F185.m3u8&mode=10012&name===Channel+5+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/channel5_uk.jpg&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/channel5_uk.jpg&amp;description=' + '\n' )
 I1IiI . write ( r'alibi HD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F329.m3u8&mode=10012&name===Alibi+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/alibi_uktv.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/alibi_uktv.jpg+&amp;description=' + '\n' )
 I1IiI . write ( r'Dave HD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F325.m3u8&mode=10012&name===Dave+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/dave_uktv.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/dave_uktv.jpg+&amp;description=' + '\n' )
 I1IiI . write ( r'GOLD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F326.m3u8&mode=10012&name===Gold+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/gold_uktv.jpg&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/gold_uktv.jpg&amp;description=' + '\n' )
 I1IiI . write ( r'Pick=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F324.m3u8&mode=10012&name===Pick+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/pick_tv.jpg&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/pick_tv.jpg&amp;description=' + '\n' )
 I1IiI . write ( r'Really=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F631.m3u8&mode=10012&name===Really&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/really_uktv.jpg++&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/really_uktv.jpg++&amp;description=' + '\n' )
 I1IiI . write ( r'YESTERDAY=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F377.m3u8&mode=10012&name===Yesterday+UK&amp;iconimage=http%3A//lm-media-ltd.net/logos/Yesterday.jpg&amp;fanart=http%3A//lm-media-ltd.net/logos/Yesterday.jpg&amp;description=' + '\n' )
 I1IiI . write ( r'Watch HD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F518.m3u8&mode=10012&name===Watch+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/watch_uktv.jpg++&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/watch_uktv.jpg++&amp;description=' + '\n' )
 I1IiI . write ( r'CBS Action=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F637.m3u8&mode=10012&name===CBS+Action+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/cbs_action.jpg++&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/cbs_action.jpg++&amp;description=' + '\n' )
 I1IiI . write ( r'CBS Drama=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F636.m3u8&mode=10012&name===CBC+Drama+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/cbs_drama.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/cbs_drama.jpg+&amp;description=' + '\n' )
 I1IiI . write ( r'CBS Reality=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F635.m3u8&mode=10012&name===CBS+Reality+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/cbs_reality.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/cbs_reality.jpg+&amp;description=' + '\n' )
 I1IiI . write ( r'True Drama=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F634.m3u8&mode=10012&name===True+Drama+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/true_drama_uk.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/true_drama_uk.jpg+&amp;description=' + '\n' )
 I1IiI . write ( r'Challenge=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F772.m3u8&mode=10012&name===Challenge+UK&amp;iconimage=https%3A//i.ytimg.com/i/RCV-1IVhGZWY1k-Em9QVQA/mq1.jpg+&amp;fanart=https%3A//i.ytimg.com/i/RCV-1IVhGZWY1k-Em9QVQA/mq1.jpg+&amp;description=' + '\n' )
 I1IiI . write ( r'RTE One=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F194.m3u8&mode=10012&name===RTE+One+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/rte_one.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/rte_one.jpg+&amp;description=' + '\n' )
 I1IiI . write ( r'RTE Two=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F193.m3u8&mode=10012&name===RTE+Two+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/rte_two.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/rte_two.jpg+&amp;description=' + '\n' )
 I1IiI . write ( r'TG4=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F192.m3u8&mode=10012&name===TG4&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/tg4.jpg++&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/tg4.jpg++&amp;description=' + '\n' )
 I1IiI . write ( r'3e=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F769.m3u8&mode=10012&name===3e+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/3e_ie.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/3e_ie.jpg+&amp;description=' + '\n' )
 I1IiI . write ( r'TV3=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F774.m3u8&mode=10012&name===TV3+UK&amp;iconimage=https%3A//pbs.twimg.com/profile_images/683994318852485125/eQ0KQ53-.jpg+&amp;fanart=https%3A//pbs.twimg.com/profile_images/683994318852485125/eQ0KQ53-.jpg+&amp;description=' + '\n' )
 I1IiI . write ( r'ComedyXtra=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F767.m3u8&mode=10012&name===Comedy+Central+Extra+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/comedy_central_extra_uk.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/comedy_central_extra_uk.jpg+&amp;description=' + '\n' )
 I1IiI . write ( r'FOX HD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F179.m3u8&mode=10012&name===FOX+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/fox_uk.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/fox_uk.jpg+&amp;description=' + '\n' )
 I1IiI . write ( r'Syfy HD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F180.m3u8&mode=10012&name===Syfy+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/syfy_uk.jpg&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/syfy_uk.jpg&amp;description=' + '\n' )
 I1IiI . write ( r'TCM=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F632.m3u8&mode=10012&name===TCM+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/tcm_uk.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/tcm_uk.jpg+&amp;description=' + '\n' )
 I1IiI . write ( r'TLC=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F768.m3u8&mode=10012&name===TLC+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/tlc_uk.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/tlc_uk.jpg+&amp;description=' + '\n' )
 I1IiI . write ( r'Universal HD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F404.m3u8&mode=10012&name===Universal+Channel+UK&amp;iconimage=http%3A//theident.gallery/universalhd/2013/misc/UNIVERSAL-2013-PROMO-100PERCENT-1-8.jpg+&amp;fanart=http%3A//theident.gallery/universalhd/2013/misc/UNIVERSAL-2013-PROMO-100PERCENT-1-8.jpg+&amp;description=' + '\n' )
 I1IiI . write ( r'Universal+1=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F771.m3u8&mode=10012&name===Universal+Channel+%2B1+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/universal_channel_uk_plus1.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/universal_channel_uk_plus1.jpg+&amp;description=' + '\n' )
 I1IiI . write ( r'Sky1=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F32.m3u8&mode=10012&name===Sky+1+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/sky_uk_1.jpg&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/sky_uk_1.jpg&amp;description=' + '\n' )
 I1IiI . write ( r'Sky2=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F33.m3u8&mode=10012&name===Sky+2+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/sky_uk_2.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/sky_uk_2.jpg+&amp;description=' + '\n' )
 I1IiI . write ( r'Sky Living=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F35.m3u8&mode=10012&name===Sky+Living+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/sky_uk_living.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/sky_uk_living.jpg+&amp;description=' + '\n' )
 I1IiI . write ( r'Sky Atlantic=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F34.m3u8&mode=10012&name===Sky+Atlantic+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/sky_uk_atlantic.jpg&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/sky_uk_atlantic.jpg&amp;description=' + '\n' )
 I1IiI . write ( r'Food Network=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F639.m3u8&mode=10012&name===Food+Network&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/food_network_uk.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/food_network_uk.jpg+&amp;description=' + '\n' )
 I1IiI . write ( r'SkyPremiereHD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F516.m3u8&mode=10012&name===Sky+Movies+Premiere+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/sky_uk_movies_premiere.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/sky_uk_movies_premiere.jpg+&amp;description=' + '\n' )
 I1IiI . write ( r'Sky Action=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F732.m3u8&mode=10012&name===Sky+Movies+Action+%26+Adventure+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/sky_uk_movies_action_adventure.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/sky_uk_movies_action_adventure.jpg+&amp;description=' + '\n' )
 I1IiI . write ( r'Sky Thriller=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F514.m3u8&mode=10012&name===Sky+Movies+Crime+%26+Thriller+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/sky_uk_movies_crime_thriller.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/sky_uk_movies_crime_thriller.jpg+&amp;description=' + '\n' )
 I1IiI . write ( r'Sky ScFiHorror=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F511.m3u8&mode=10012&name===Sky+Movies+Sci-Fi+%26+Horror+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/sky_uk_movies_scifi_horror.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/sky_uk_movies_scifi_horror.jpg+&amp;description=' + '\n' )
 I1IiI . write ( r'Sky Comedy=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F513.m3u8&mode=10012&name===Sky+Movies+Comedy+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/sky_uk_movies_comedy.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/sky_uk_movies_comedy.jpg+&amp;description=' + '\n' )
 I1IiI . write ( r'Sky Greats=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F512.m3u8&mode=10012&name===Sky+Movies+Greats+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/sky_uk_movies_modern_greats.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/sky_uk_movies_modern_greats.jpg+&amp;description=' + '\n' )
 I1IiI . write ( r'Sky Showcase=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F46.m3u8&mode=10012&name===Sky+Movies+Showcase+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/sky_uk_movies_showcase.jpg++&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/sky_uk_movies_showcase.jpg++&amp;description=' + '\n' )
 I1IiI . write ( r'Sky Select=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F45.m3u8&mode=10012&name===Sky+Movies+Select+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/sky_uk_movies_select_hd.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/sky_uk_movies_select_hd.jpg+&amp;description=' + '\n' )
 I1IiI . write ( r'Sky DramaRom=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F510.m3u8&mode=10012&name===Sky+Movies+Drama+%26+Romance+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/sky_uk_movies_drama_romance.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/sky_uk_movies_drama_romance.jpg+&amp;description=' + '\n' )
 I1IiI . write ( r'Sky Family=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F509.m3u8&mode=10012&name===Sky+Movies+Family+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/sky_uk_movies_family_hd.jpg++&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/sky_uk_movies_family_hd.jpg++&amp;description=' + '\n' )
 I1IiI . write ( r'Sky Disney=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F195.m3u8&mode=10012&name===Sky+Movies+Disney+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/sky_uk_movies_disney.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/sky_uk_movies_disney.jpg+&amp;description=' + '\n' )
 I1IiI . write ( r'Film4=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F182.m3u8&mode=10012&name===Film4+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/film4.jpg++&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/film4.jpg++&amp;description=' + '\n' )
 I1IiI . write ( r'Movies 24=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F633.m3u8&mode=10012&name===Movies+24+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/movies24_uk.jpg++&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/movies24_uk.jpg++&amp;description=' + '\n' )
 I1IiI . write ( r'JollyHD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F739.m3u8&mode=10012&name===JollyHD&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/tring_jolly_hd.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/tring_jolly_hd.jpg+&amp;description=' + '\n' )
 I1IiI . write ( r'Film Dy HD AL=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F777.m3u8&mode=10012&name===Film+Dy+HD+AL&amp;iconimage=http%3A//www.sat-address.com/f/pics/logotipi/Film-Dy-DigitAlb_o.jpg+&amp;fanart=http%3A//www.sat-address.com/f/pics/logotipi/Film-Dy-DigitAlb_o.jpg+&amp;description=' + '\n' )
 I1IiI . write ( r'Film Nje HD AL=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F778.m3u8&mode=10012&name===Film+Nje+HD+AL&amp;iconimage=http%3A//www.sat-address.com/f/pics/logotipi/Film-Nje-DigitAlb_o.jpg+&amp;fanart=http%3A//www.sat-address.com/f/pics/logotipi/Film-Nje-DigitAlb_o.jpg+&amp;description=' + '\n' )
 I1IiI . write ( r'HBO Adria=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F564.m3u8&mode=10012&name===HBO+Adria&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/hbo_adria.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/hbo_adria.jpg+&amp;description=' + '\n' )
 I1IiI . write ( r'HBO 2 Adria=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F672.m3u8&mode=10012&name===HBO+2+Adria&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/hbo2_ce.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/hbo2_ce.jpg+&amp;description=' + '\n' )
 I1IiI . write ( r'HBO 3 Adria=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F738.m3u8&mode=10012&name===HBO+3+Adria&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/hbo3_nl.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/hbo3_nl.jpg+&amp;description=' + '\n' )
 I1IiI . write ( r'HBO 1 (NL)=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F675.m3u8&mode=10012&name===HBO+1+%28NL%29&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/hbo_nl_hd.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/hbo_nl_hd.jpg+&amp;description=' + '\n' )
 I1IiI . write ( r'HBO 2 (NL)=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F674.m3u8&mode=10012&name===HBO+2+%28NL%29&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/hbo2_nl.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/hbo2_nl.jpg+&amp;description=' + '\n' )
 I1IiI . write ( r'HBO 3 (NL)=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F673.m3u8&mode=10012&name===HBO+3+%28NL%29&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/hbo3_nl.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/hbo3_nl.jpg+&amp;description=' + '\n' )
 I1IiI . write ( r'TVCINE 1 HD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F851.m3u8&mode=10012&name===TVCINE+1+HD+PT&amp;iconimage=http%3A//www.zipestream.com/images/TVC1.png+&amp;fanart=http%3A//www.zipestream.com/images/TVC1.png+&amp;description=' + '\n' )
 I1IiI . write ( r'TVCINE 2 HD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F850.m3u8&mode=10012&name===TVCINE+2+HD+PT&amp;iconimage=http%3A//www.zipestream.com/images/TVC2.png&amp;fanart=http%3A//www.zipestream.com/images/TVC2.png&amp;description=' + '\n' )
 I1IiI . write ( r'TVCINE 3 HD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F849.m3u8&mode=10012&name===TVCINE+3+HD+PT&amp;iconimage=http%3A//www.zipestream.com/images/TVC3.png+&amp;fanart=http%3A//www.zipestream.com/images/TVC3.png+&amp;description=' + '\n' )
 I1IiI . write ( r'TVCINE 4 HD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F848.m3u8&mode=10012&name===TVCINE+4+HD+PT&amp;iconimage=http%3A//www.zipestream.com/images/TVC4.png+&amp;fanart=http%3A//www.zipestream.com/images/TVC4.png+&amp;description=' + '\n' )
 I1IiI . write ( r'Hollywood (Pt)=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F702.m3u8&mode=10012&name===Hollywood+%28Pt%29&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/canal_hollywood_hd.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/canal_hollywood_hd.jpg+&amp;description=' + '\n' )
 I1IiI . write ( r'US &amp; UK Movies from Asia=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F396.m3u8&mode=10012&name===US+%26+UK+Movies+from+Asia&amp;iconimage=http%3A//vignette4.wikia.nocookie.net/logopedia/images/8/8e/My_Movie_Channel_official_slogan.jpg+&amp;fanart=http%3A//vignette4.wikia.nocookie.net/logopedia/images/8/8e/My_Movie_Channel_official_slogan.jpg+&amp;description=' + '\n' )
 I1IiI . write ( r'ABC HD US=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F295.m3u8&mode=10012&name===ABC+HD+US&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/abc_hd.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/abc_hd.jpg+&amp;description=' + '\n' )
 I1IiI . write ( r'ABC=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F11.m3u8&mode=10012&name===ABC+%28US%29&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/abc_hd.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/abc_hd.jpg+&amp;description=' + '\n' )
 I1IiI . write ( r'A&E=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F16.m3u8&mode=10012&name===A%26E+%28US%29&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/ae_us.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/ae_us.jpg+&amp;description=' + '\n' )
 I1IiI . write ( r'AMC=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F52.m3u8&mode=10012&name===AMC+%28US%29&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/amc_us.jpg++&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/amc_us.jpg++&amp;description=' + '\n' )
 I1IiI . write ( r'AXS TV=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F392.m3u8&mode=10012&name===AXS+TV+%28US%29&amp;iconimage=http%3A//www.musicnewsnashville.com/wp-content/uploads/2014/04/axs-tv_logo.jpg&amp;fanart=http%3A//www.musicnewsnashville.com/wp-content/uploads/2014/04/axs-tv_logo.jpg&amp;description=' + '\n' )
 I1IiI . write ( r'Bravo=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F14.m3u8&mode=10012&name===Bravo+%28US%29&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/bravo_us.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/bravo_us.jpg+&amp;description=' + '\n' )
 I1IiI . write ( r'CBS=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F250.m3u8&mode=10012&name===CBS+%28US%29&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/cbs.jpg&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/cbs.jpg&amp;description=' + '\n' )
 I1IiI . write ( r'CW=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F626.m3u8&mode=10012&name===CW+%28US%29&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/kcwq_palm_springs.jpg++&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/kcwq_palm_springs.jpg++&amp;description=' + '\n' )
 I1IiI . write ( r'FOX=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F297.m3u8&mode=10012&name===Fox+HD+US&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/fox_bg.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/fox_bg.jpg+&amp;description=' + '\n' )
 I1IiI . write ( r'FOX=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F13.m3u8&mode=10012&name===Fox+%28US%29&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/fox_bg.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/fox_bg.jpg+&amp;description=' + '\n' )
 I1IiI . write ( r'FX=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F409.m3u8&mode=10012&name===FX+%28US%29&amp;iconimage=http%3A//www.casinopartydesigners.com/images/fx-140x140.jpg+&amp;fanart=http%3A//www.casinopartydesigners.com/images/fx-140x140.jpg+&amp;description=' + '\n' )
 I1IiI . write ( r'NBC=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F15.m3u8&mode=10012&name===NBC+%28US%29&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/nbc.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/nbc.jpg+&amp;description=' + '\n' )
 I1IiI . write ( r'PBSNET (PBS)=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F398.m3u8&mode=10012&name===PBS+%28US%29&amp;iconimage=http%3A//vignette2.wikia.nocookie.net/arthur/images/5/58/PBS.jpg+&amp;fanart=http%3A//vignette2.wikia.nocookie.net/arthur/images/5/58/PBS.jpg+&amp;description=' + '\n' )
 I1IiI . write ( r'Lifetime HD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F627.m3u8&mode=10012&name===Lifetime+USA&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/lifetime_us.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/lifetime_us.jpg+&amp;description=' + '\n' )
 I1IiI . write ( r'Spike TV<=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F375.m3u8&mode=10012&name===Spike+%28US%29&amp;iconimage=http%3A//1.images.spike.com/images/missing_image2.jpg&amp;fanart=http%3A//1.images.spike.com/images/missing_image2.jpg&amp;description=' + '\n' )
 I1IiI . write ( r'Syfy=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F238.m3u8&mode=10012&name===Syfy+%28US%29&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/syfy_us.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/syfy_us.jpg+&amp;description=' + '\n' )
 I1IiI . write ( r'TBS=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F253.m3u8&mode=10012&name===TBS+%28US%29&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/tbs_hd.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/tbs_hd.jpg+&amp;description=' + '\n' )
 I1IiI . write ( r'TNT=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F381.m3u8&mode=10012&name===TNT+%28US%29&amp;iconimage=http%3A//web.cablecolor.cl/images/Canales/Seriespeliculas/tnt.jpg++&amp;fanart=http%3A//web.cablecolor.cl/images/Canales/Seriespeliculas/tnt.jpg++&amp;description=' + '\n' )
 I1IiI . write ( r'USA=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F379.m3u8&mode=10012&name===USA+%28US%29&amp;iconimage=http%3A//images.bwwstatic.com/columnpic6/24BBCD1DC-0C7F-5F83-A9B18707E9842A5E.jpg+&amp;fanart=http%3A//images.bwwstatic.com/columnpic6/24BBCD1DC-0C7F-5F83-A9B18707E9842A5E.jpg+&amp;description=' + '\n' )
 I1IiI . write ( r'KTLA=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F628.m3u8&mode=10012&name===KTLA+/CW&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/ktla_cw5_los_angeles.jpg++&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/ktla_cw5_los_angeles.jpg++&amp;description=' + '\n' )
 I1IiI . write ( r'Global BC (CA)=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F399.m3u8&mode=10012&name===Global+BC+%28CA%29&amp;iconimage=http%3A//priceypads.com/wp-content/uploads/2010/01/Global-BC.jpg&amp;fanart=http%3A//priceypads.com/wp-content/uploads/2010/01/Global-BC.jpg&amp;description=' + '\n' )
 I1IiI . write ( r'Space HD Ca=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F630.m3u8&mode=10012&name===Space+HD+Ca&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/space_ca_hd.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/space_ca_hd.jpg+&amp;description=' + '\n' )
 I1IiI . write ( r'WPIX=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F629.m3u8&mode=10012&name===WPIX+II+CA&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/wpix_cw11_new_york.jpg++&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/wpix_cw11_new_york.jpg++&amp;description=' + '\n' )
 I1IiI . write ( r'Hallmark Channel=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F525.m3u8&mode=10012&name===Hallmark+Channel+HD&amp;iconimage=http%3A//www.kadoshop-leenhouts.nl/uploads/1/3/5/1/13510121/8447772_orig.jpg++&amp;fanart=http%3A//www.kadoshop-leenhouts.nl/uploads/1/3/5/1/13510121/8447772_orig.jpg++&amp;description=' + '\n' )
 I1IiI . write ( r'CineMAX=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F553.m3u8&mode=10012&name===Cinemax+East&amp;iconimage=http%3A//static.wixstatic.com/media/17a537_42bb4d4b404748b490b8252b9d3c8451.jpeg+&amp;fanart=http%3A//static.wixstatic.com/media/17a537_42bb4d4b404748b490b8252b9d3c8451.jpeg+&amp;description=' + '\n' )
 I1IiI . write ( r'Cinemax 5 StarMAX HD East (5MAXHD)=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F403.m3u8&mode=10012&name===Cinemax+5+StarMax&amp;iconimage=http%3A//vignette2.wikia.nocookie.net/logopedia/images/2/22/5StarMax_2011.jpg++++&amp;fanart=http%3A//vignette2.wikia.nocookie.net/logopedia/images/2/22/5StarMax_2011.jpg++++&amp;description=' + '\n' )
 I1IiI . write ( r'Cinemax ActionMax HD East (AMAXHD)=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F402.m3u8&mode=10012&name===Cinemax+ActionMax+East&amp;iconimage=http%3A//vignette3.wikia.nocookie.net/company-bumpers/images/1/10/ActionMax_ID_%281998-2001%29.jpg+++&amp;fanart=http%3A//vignette3.wikia.nocookie.net/company-bumpers/images/1/10/ActionMax_ID_%281998-2001%29.jpg+++&amp;description=' + '\n' )
 I1IiI . write ( r'MoreMAX=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F401.m3u8&mode=10012&name===Cinemax+Moremax&amp;iconimage=http%3A//vignette3.wikia.nocookie.net/logopedia/images/3/38/MoreMax_2011.jpg+++&amp;fanart=http%3A//vignette3.wikia.nocookie.net/logopedia/images/3/38/MoreMax_2011.jpg+++&amp;description=' + '\n' )
 I1IiI . write ( r'HBO (Pacific)=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F249.m3u8&mode=10012&name===HBO&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/hbo_east.jpg+++&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/hbo_east.jpg+++&amp;description=' + '\n' )
 I1IiI . write ( r'HBO Comedy HD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F244.m3u8&mode=10012&name===HBO+Comedy+%28US%29&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/hbo_comedy_us.jpg+++&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/hbo_comedy_us.jpg+++&amp;description=' + '\n' )
 I1IiI . write ( r'HBO Signature (Pacific)=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F247.m3u8&mode=10012&name===HBO+Signature&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/hbo_signature.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/hbo_signature.jpg+&amp;description=' + '\n' )
 I1IiI . write ( r'HBO Zone (Pacific)=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F242.m3u8&mode=10012&name===HBO+Zone&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/hbo_zone_us.jpg++&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/hbo_zone_us.jpg++&amp;description=' + '\n' )
 I1IiI . write ( r'Starz (Pacific)=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F582.m3u8&mode=10012&name===Starz+%28US%29&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/starz.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/starz.jpg+&amp;description=' + '\n' )
 I1IiI . write ( r'Starz Cinema=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F400.m3u8&mode=10012&name===Starz+Cinema+East&amp;iconimage=https%3A//www.starzplay.com/Images/starz/starz_facebook_logo_large.png+++&amp;fanart=https%3A//www.starzplay.com/Images/starz/starz_facebook_logo_large.png+++&amp;description=' + '\n' )
 I1IiI . write ( r'Starz Edge (Pacific)=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F413.m3u8&mode=10012&name===Starz+Edge+East&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/starz_edge.jpg+++&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/starz_edge.jpg+++&amp;description=' + '\n' )
 I1IiI . write ( r'Encore (ENCe)=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F581.m3u8&mode=10012&name===Starz+Encore+East+%28US%29&amp;iconimage=http%3A//www.secv.com/images/premium_starz.jpg+&amp;fanart=http%3A//www.secv.com/images/premium_starz.jpg+&amp;description=' + '\n' )
 I1IiI . write ( r'Showtime=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F554.m3u8&mode=10012&name===Showtime+%28US%29&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/showtime_west.jpg+++&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/showtime_west.jpg+++&amp;description=' + '\n' )
 I1IiI . write ( r'Showtime Beyond=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F414.m3u8&mode=10012&name===Showtime+2+East&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/showtime2_east.jpg+++&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/showtime2_east.jpg+++&amp;description=' + '\n' )
 I1IiI . write ( r'Showtime West=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F416.m3u8&mode=10012&name===Showtime+West&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/showtime_west.jpg++&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/showtime_west.jpg++&amp;description=' + '\n' )
 I1IiI . write ( r'Showtime Beyond=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F415.m3u8&mode=10012&name===Showtime+Showcase+East&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/showtime_showcase_east.jpg+++&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/showtime_showcase_east.jpg+++&amp;description=' + '\n' )
 I1IiI . write ( r'BabyTV=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F523.m3u8&mode=10012&name===BabyTV&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/baby_tv.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/baby_tv.jpg+&amp;description=' + '\n' )
 I1IiI . write ( r'Cartoon Netwrk=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F519.m3u8&mode=10012&name===Cartoon+Netwrk&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/cartoon_network_us.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/cartoon_network_us.jpg+&amp;description=' + '\n' )
 I1IiI . write ( r'Disney Chnl=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F231.m3u8&mode=10012&name===Disney+Channel+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/disney_channel_uk.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/disney_channel_uk.jpg+&amp;description=' + '\n' )
 I1IiI . write ( r'Disney Junior=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F230.m3u8&mode=10012&name===Disney+Jr.+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/disney_junior_uk.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/disney_junior_uk.jpg+&amp;description=' + '\n' )
 I1IiI . write ( r'Disney XD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F770.m3u8&mode=10012&name===Disney+XD+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/disney_xd_uk.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/disney_xd_uk.jpg+&amp;description=' + '\n' )
 I1IiI . write ( r'Nicktoons=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F520.m3u8&mode=10012&name===Nicktoons&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/nicktoons_uk.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/nicktoons_uk.jpg+&amp;description=' + '\n' )
 I1IiI . write ( r'Nickelodeon=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F521.m3u8&mode=10012&name===Nickelodeon&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/nickelodeon_us.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/nickelodeon_us.jpg+&amp;description=' + '\n' )
 I1IiI . write ( r'Nick Jr.=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F522.m3u8&mode=10012&name===Nick+Jr.&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/nick_jr_uk.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/nick_jr_uk.jpg+&amp;description=' + '\n' )
 I1IiI . write ( r'Animal Planet (APL)=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F198.m3u8&mode=10012&name===Animal+Planet+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/animal_planet_europe.jpg++&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/animal_planet_europe.jpg++&amp;description=' + '\n' )
 I1IiI . write ( r'Discovery=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F200.m3u8&mode=10012&name===Discovery+Channel+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/discovery_uk.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/discovery_uk.jpg+&amp;description=' + '\n' )
 I1IiI . write ( r'Disc.History=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F201.m3u8&mode=10012&name===Discovery+History+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/discovery_history.jpg++&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/discovery_history.jpg++&amp;description=' + '\n' )
 I1IiI . write ( r'Disc.Science=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F199.m3u8&mode=10012&name===Discovery+Science+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/discovery_science.jpg++&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/discovery_science.jpg++&amp;description=' + '\n' )
 I1IiI . write ( r'Disc.Turbo=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F168.m3u8&mode=10012&name===Discovery+Turbo+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/discovery_turbo_uk.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/discovery_turbo_uk.jpg+&amp;description=' + '\n' )
 I1IiI . write ( r'DMAX=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F638.m3u8&mode=10012&name===DMAX+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/dmax_uk.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/dmax_uk.jpg+&amp;description=' + '\n' )
 I1IiI . write ( r'History=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F196.m3u8&mode=10012&name===History+Channel+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/history_uk.jpg++&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/history_uk.jpg++&amp;description=' + '\n' )
 I1IiI . write ( r'H2=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F468.m3u8&mode=10012&name===H2+UK&amp;iconimage=http%3A//www.mediared.tv/uploads/9/0/6/6/9066987/9872449.jpg+&amp;fanart=http%3A//www.mediared.tv/uploads/9/0/6/6/9066987/9872449.jpg+&amp;description=' + '\n' )
 I1IiI . write ( r'CI=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F202.m3u8&mode=10012&name===Crime+%26+Investigation+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/crime_investigation_network_uk.jpg++&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/crime_investigation_network_uk.jpg++&amp;description=' + '\n' )
 I1IiI . write ( r'National Geographic Channel=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F197.m3u8&mode=10012&name===National+Geographic+Channel+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/nat_geo_uk.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/nat_geo_uk.jpg+&amp;description=' + '\n' )
 I1IiI . write ( r'National Geographic Wild=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F622.m3u8&mode=10012&name===Nat+Geo+Wild+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/nat_geo_wild_uk.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/nat_geo_wild_uk.jpg+&amp;description=' + '\n' )
 I1IiI . write ( r'MTV CLASSIC=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F420.m3u8&mode=10012&name===MTV+Classic&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/mtv_classic_uk.jpg++&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/mtv_classic_uk.jpg++&amp;description=' + '\n' )
 I1IiI . write ( r'MTV HITS=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F235.m3u8&mode=10012&name===MTV+Hits&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/mtv_hits_uk.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/mtv_hits_uk.jpg+&amp;description=' + '\n' )
 I1IiI . write ( r'MTV MUSIC=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F234.m3u8&mode=10012&name===MTV+Music+UK&amp;iconimage=https%3A//upload.wikimedia.org/wikipedia/commons/thumb/f/f9/MTV_Music_2013.png/220px-MTV_Music_2013.png&amp;fanart=https%3A//upload.wikimedia.org/wikipedia/commons/thumb/f/f9/MTV_Music_2013.png/220px-MTV_Music_2013.png&amp;description=' + '\n' )
 I1IiI . write ( r'VH1=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F556.m3u8&mode=10012&name===VH1+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/vh1_uk.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/vh1_uk.jpg+&amp;description=' + '\n' )
 I1IiI . write ( r'Sky Sports 1 HD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F323.m3u8&mode=10012&name===Sky+Sports+1+HD&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/sky_uk_sports_hd1.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/sky_uk_sports_hd1.jpg+&amp;description=' + '\n' )
 I1IiI . write ( r'Sky Sports 1=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F18.m3u8&mode=10012&name===Sky+Sports+1+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/sky_uk_sports_hd1.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/sky_uk_sports_hd1.jpg+&amp;description=' + '\n' )
 I1IiI . write ( r'Sky Sports 2 HD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F322.m3u8&mode=10012&name===Sky+Sports+2+HD&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/sky_uk_sports_hd2.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/sky_uk_sports_hd2.jpg+&amp;description=' + '\n' )
 I1IiI . write ( r'Sky Sports 2=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F19.m3u8&mode=10012&name===Sky+Sports+2+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/sky_uk_sports_hd2.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/sky_uk_sports_hd2.jpg+&amp;description=' + '\n' )
 I1IiI . write ( r'Sky Sports 3 HD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F321.m3u8&mode=10012&name===Sky+Sports+3+HD&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/sky_uk_sports_hd3.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/sky_uk_sports_hd3.jpg+&amp;description=' + '\n' )
 I1IiI . write ( r'Sky Sports 3=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F20.m3u8&mode=10012&name===Sky+Sports+3+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/sky_uk_sports_hd3.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/sky_uk_sports_hd3.jpg+&amp;description=' + '\n' )
 I1IiI . write ( r'Sky Sports 4 HD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F320.m3u8&mode=10012&name===Sky+Sports+4+HD&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/sky_uk_sports_hd4.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/sky_uk_sports_hd4.jpg+&amp;description=' + '\n' )
 I1IiI . write ( r'Sky Sports 4=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F21.m3u8&mode=10012&name===Sky+Sports+4+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/sky_uk_sports_hd4.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/sky_uk_sports_hd4.jpg+&amp;description=' + '\n' )
 I1IiI . write ( r'Sky Sports 5 HD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F339.m3u8&mode=10012&name===Sky+Sports+5+HD&amp;iconimage=http%3A//www.sky.com/shop/export/sites/www.sky.com/shop/__EPG/EPGImages/sports_5hd.png_1689595083.png&amp;fanart=http%3A//www.sky.com/shop/export/sites/www.sky.com/shop/__EPG/EPGImages/sports_5hd.png_1689595083.png&amp;description=' + '\n' )
 I1IiI . write ( r'Sky Sports 5=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F22.m3u8&mode=10012&name===Sky+Sports+5+UK&amp;iconimage=http%3A//store.virginmedia.com/content/dam/eSales/TV/logos-81x45/sky-sports-5-hd-pos.png+&amp;fanart=http%3A//store.virginmedia.com/content/dam/eSales/TV/logos-81x45/sky-sports-5-hd-pos.png+&amp;description=' + '\n' )
 I1IiI . write ( r'Sky Sports F1 HD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F374.m3u8&mode=10012&name===Sky+Sports+F1+HD&amp;iconimage=http%3A//img.skysports.com/11/11/660x350/f1new_2682772.jpg+&amp;fanart=http%3A//img.skysports.com/11/11/660x350/f1new_2682772.jpg+&amp;description=' + '\n' )
 I1IiI . write ( r'Sky Sports F1=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F24.m3u8&mode=10012&name===Sky+Sports+F1+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/sky_uk_sports_f1_hd.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/sky_uk_sports_f1_hd.jpg+&amp;description=' + '\n' )
 I1IiI . write ( r'Sky SpN HQ HD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F23.m3u8&mode=10012&name===Sky+Sports+News+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/sky_uk_sports_news_hd.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/sky_uk_sports_news_hd.jpg+&amp;description=' + '\n' )
 I1IiI . write ( r'BT Sport 1 HD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F316.m3u8&mode=10012&name===BT+Sport+1+HD&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/bt_sport_1_hd.jpg&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/bt_sport_1_hd.jpg&amp;description=' + '\n' )
 I1IiI . write ( r'BT Sport 1=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F309.m3u8&mode=10012&name===BT+Sport+1+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/bt_sport_1_hd.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/bt_sport_1_hd.jpg+&amp;description=' + '\n' )
 I1IiI . write ( r'BT Sport 2 HD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F308.m3u8&mode=10012&name===BT+Sport+2+HD&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/bt_sport_2_hd.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/bt_sport_2_hd.jpg+&amp;description=' + '\n' )
 I1IiI . write ( r'BT Sports 2 HD (1080) Test=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F599.m3u8&mode=10012&name===BT+Sports+2+HD+%281080%29+Test&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/bt_sport_2_hd.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/bt_sport_2_hd.jpg+&amp;description=' + '\n' )
 I1IiI . write ( r'BT Sports 2 HD Test=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F707.m3u8&mode=10012&name===BT+Sports+2+HD+Test&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/bt_sport_2_hd.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/bt_sport_2_hd.jpg+&amp;description=' + '\n' )
 I1IiI . write ( r'BT Sport 2=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F26.m3u8&mode=10012&name===BT+Sport+2+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/bt_sport_2_hd.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/bt_sport_2_hd.jpg+&amp;description=' + '\n' )
 I1IiI . write ( r'BT Sport EurHD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F382.m3u8&mode=10012&name===BT+Sport+Europe+HD&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/bt_sport_uk.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/bt_sport_uk.jpg+&amp;description=' + '\n' )
 I1IiI . write ( r'BT Sport Europe=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F705.m3u8&mode=10012&name===BT+Sport+Europe&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/bt_sport_1_hd.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/bt_sport_1_hd.jpg+&amp;description=' + '\n' )
 I1IiI . write ( r'BT Sport\/\/ESPN=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F28.m3u8&mode=10012&name===BT+Sport+ESPN&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/espn_uk.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/espn_uk.jpg+&amp;description=' + '\n' )
 I1IiI . write ( r'Premier HD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F310.m3u8&mode=10012&name===Premier+Sports+HD&amp;iconimage=http%3A//w3.satkurier.pl/pliki/24801.jpg+&amp;fanart=http%3A//w3.satkurier.pl/pliki/24801.jpg+&amp;description=' + '\n' )
 I1IiI . write ( r'Premier Sports HD 1080P=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F384.m3u8&mode=10012&name===Premier+Sports+HD+1080P&amp;iconimage=http%3A//w3.satkurier.pl/pliki/24801.jpg+&amp;fanart=http%3A//w3.satkurier.pl/pliki/24801.jpg+&amp;description=' + '\n' )
 I1IiI . write ( r'Premier Sports=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F175.m3u8&mode=10012&name===Premier+Sports+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/premier_sports.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/premier_sports.jpg+&amp;description=' + '\n' )
 I1IiI . write ( r'Setanta Ireland=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F176.m3u8&mode=10012&name===Setanta+Sports+Ireland+1+UK&amp;iconimage=http%3A//www.setanta.com/Themes/setanta/img/channel_logos/Setanta.png+&amp;fanart=http%3A//www.setanta.com/Themes/setanta/img/channel_logos/Setanta.png+&amp;description=' + '\n' )
 I1IiI . write ( r'At The Races=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F170.m3u8&mode=10012&name===At+the+Races+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/at_the_races_uk.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/at_the_races_uk.jpg+&amp;description=' + '\n' )
 I1IiI . write ( r'Racing UK=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F171.m3u8&mode=10012&name===Racing+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/racing_uk.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/racing_uk.jpg+&amp;description=' + '\n' )
 I1IiI . write ( r'MUTV=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F172.m3u8&mode=10012&name===Manchester+United+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/mutv.jpg&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/mutv.jpg&amp;description=' + '\n' )
 I1IiI . write ( r'LFCTV=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F174.m3u8&mode=10012&name===Liverpool+TV+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/liverpool_football_club.jpg&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/liverpool_football_club.jpg&amp;description=' + '\n' )
 I1IiI . write ( r'Chelsea TV=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F177.m3u8&mode=10012&name===Chelsea+TV+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/chelsea_tv.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/chelsea_tv.jpg+&amp;description=' + '\n' )
 I1IiI . write ( r'Eurosport=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F269.m3u8&mode=10012&name===Eurosport+1+UK&amp;iconimage=http%3A//euro-2012.ru/download/Logo-eurosport.jpg+&amp;fanart=http%3A//euro-2012.ru/download/Logo-eurosport.jpg+&amp;description=' + '\n' )
 I1IiI . write ( r'Eurosport 2 UK=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F748.m3u8&mode=10012&name===Eurosport+2+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/eurosport2.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/eurosport2.jpg+&amp;description=' + '\n' )
 I1IiI . write ( r'1HD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F83.m3u8&mode=10012&name===BEIN+SPORTS+1&amp;iconimage=http%3A//digigroup.az/media/images/1.jpg+&amp;fanart=http%3A//digigroup.az/media/images/1.jpg+&amp;description=' + '\n' )
 I1IiI . write ( r'2HD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F84.m3u8&mode=10012&name===BEIN+SPORTS+2&amp;iconimage=http%3A//digigroup.az/media/images/2.jpg++&amp;fanart=http%3A//digigroup.az/media/images/2.jpg++&amp;description=' + '\n' )
 I1IiI . write ( r'3HD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F85.m3u8&mode=10012&name===BEIN+SPORTS+3&amp;iconimage=http%3A//digigroup.az/media/images/3.jpg++&amp;fanart=http%3A//digigroup.az/media/images/3.jpg++&amp;description=' + '\n' )
 I1IiI . write ( r'4HD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F86.m3u8&mode=10012&name===BEIN+SPORTS+4&amp;iconimage=http%3A//digigroup.az/media/images/4.jpg++&amp;fanart=http%3A//digigroup.az/media/images/4.jpg++&amp;description=' + '\n' )
 I1IiI . write ( r'5HD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F87.m3u8&mode=10012&name===BEIN+SPORTS+5&amp;iconimage=http%3A//digigroup.az/media/images/5.jpg++&amp;fanart=http%3A//digigroup.az/media/images/5.jpg++&amp;description=' + '\n' )
 I1IiI . write ( r'6HD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F88.m3u8&mode=10012&name===BEIN+SPORTS+6&amp;iconimage=http%3A//digigroup.az/media/images/6.jpg++&amp;fanart=http%3A//digigroup.az/media/images/6.jpg++&amp;description=' + '\n' )
 I1IiI . write ( r'7HD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F89.m3u8&mode=10012&name===BEIN+SPORTS+7&amp;iconimage=http%3A//digigroup.az/media/images/7.jpg++&amp;fanart=http%3A//digigroup.az/media/images/7.jpg++&amp;description=' + '\n' )
 I1IiI . write ( r'8HD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F90.m3u8&mode=10012&name===BEIN+SPORTS+8&amp;iconimage=http%3A//digigroup.az/media/images/8.jpg++&amp;fanart=http%3A//digigroup.az/media/images/8.jpg++&amp;description=' + '\n' )
 I1IiI . write ( r'9HD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F91.m3u8&mode=10012&name===BEIN+SPORTS+9&amp;iconimage=http%3A//digigroup.az/media/images/9.jpg++&amp;fanart=http%3A//digigroup.az/media/images/9.jpg++&amp;description=' + '\n' )
 I1IiI . write ( r'10HD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F92.m3u8&mode=10012&name===BEIN+SPORTS+10&amp;iconimage=http%3A//digigroup.az/media/images/10.jpg++&amp;fanart=http%3A//digigroup.az/media/images/10.jpg++&amp;description=' + '\n' )
 I1IiI . write ( r'12HD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F424.m3u8&mode=10012&name===BEIN+SPORTS+12&amp;iconimage=http%3A//digigroup.az/media/images/12.jpg++&amp;fanart=http%3A//digigroup.az/media/images/12.jpg++&amp;description=' + '\n' )
 I1IiI . write ( r'Astro SuperSport=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F60.m3u8&mode=10012&name===Astro+Supersport+1&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/astro_supersport1.jpg++&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/astro_supersport1.jpg++&amp;description=' + '\n' )
 I1IiI . write ( r'Astro SuperSport 2=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F59.m3u8&mode=10012&name===Astro+Supersport+2&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/astro_supersport2.jpg++&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/astro_supersport2.jpg++&amp;description=' + '\n' )
 I1IiI . write ( r'Astro SuperSport 3=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F58.m3u8&mode=10012&name===Astro+Supersport+3&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/astro_supersport3.jpg+++&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/astro_supersport3.jpg+++&amp;description=' + '\n' )
 I1IiI . write ( r'Astro SuperSport 4=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F57.m3u8&mode=10012&name===Astro+Supersport+4&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/astro_supersport4.jpg++++&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/astro_supersport4.jpg++++&amp;description=' + '\n' )
 I1IiI . write ( r'STADIUM 1 (CTH 211 SD / 56HD)=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F67.m3u8&mode=10012&name===CTH+Stadium+1+HD&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/stadium1_th.jpg+++&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/stadium1_th.jpg+++&amp;description=' + '\n' )
 I1IiI . write ( r'STADIUM 2 (CTH 212 SD / 57 HD)=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F66.m3u8&mode=10012&name===CTH+Stadium+2+HD&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/stadium2_th.jpg+++&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/stadium2_th.jpg+++&amp;description=' + '\n' )
 I1IiI . write ( r'STADIUM 3 (CTH 213 SD / 58 HD)=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F65.m3u8&mode=10012&name===CTH+Stadium+3+HD&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/stadium3_th.jpg++&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/stadium3_th.jpg++&amp;description=' + '\n' )
 I1IiI . write ( r'STADIUM 4 (CTH 214 SD / 59 HD)=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F64.m3u8&mode=10012&name===CTH+Stadium+4+HD&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/stadium4_th.jpg++&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/stadium4_th.jpg++&amp;description=' + '\n' )
 I1IiI . write ( r'STADIUM 5 (CTH 216 SD / 60 HD)=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F63.m3u8&mode=10012&name===CTH+Stadium+5+HD&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/stadium5_th.jpg++&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/stadium5_th.jpg++&amp;description=' + '\n' )
 I1IiI . write ( r'STADIUM 6 (CTH 216 SD / 61 HD)=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F62.m3u8&mode=10012&name===CTH+STADIUM+6+HD&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/stadium6_th.jpg+++&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/stadium6_th.jpg+++&amp;description=' + '\n' )
 I1IiI . write ( r'STADIUM X (CTH 217 SD / 62 HD)=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F61.m3u8&mode=10012&name===CTH+STADIUM+X+HD&amp;iconimage=http%3A//stepfb.net/live/movieposters/136.png++&amp;fanart=http%3A//stepfb.net/live/movieposters/136.png++&amp;description=' + '\n' )
 I1IiI . write ( r'TV Arena Sport 1=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F163.m3u8&mode=10012&name===Arena+Sport+1&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/arenasport1_rs.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/arenasport1_rs.jpg+&amp;description=' + '\n' )
 I1IiI . write ( r'TV Arena Sport 2=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F167.m3u8&mode=10012&name===Arena+Sport+2&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/arenasport2_rs.jpg++&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/arenasport2_rs.jpg++&amp;description=' + '\n' )
 I1IiI . write ( r'TV Arena Sport 3=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F164.m3u8&mode=10012&name===Arena+Sport+3&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/arenasport3_rs.jpg++&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/arenasport3_rs.jpg++&amp;description=' + '\n' )
 I1IiI . write ( r'TV Arena Sport 4=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F165.m3u8&mode=10012&name===Arena+Sport+4&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/arenasport4_rs.jpg++&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/arenasport4_rs.jpg++&amp;description=' + '\n' )
 I1IiI . write ( r'TSN1=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F96.m3u8&mode=10012&name===TSN+1&amp;iconimage=http%3A//tgo-tv.com/images/tv/tsn1.jpg+++&amp;fanart=http%3A//tgo-tv.com/images/tv/tsn1.jpg+++&amp;description=' + '\n' )
 I1IiI . write ( r'TSN2=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F97.m3u8&mode=10012&name===TSN+2&amp;iconimage=http%3A//tgo-tv.com/images/tv/tsn2.jpg++&amp;fanart=http%3A//tgo-tv.com/images/tv/tsn2.jpg++&amp;description=' + '\n' )
 I1IiI . write ( r'TSN3=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F98.m3u8&mode=10012&name===TSN+3&amp;iconimage=http%3A//cdn1.sportngin.com/attachments/news_article/5782/7585/tsn_thumb.jpg+++&amp;fanart=http%3A//cdn1.sportngin.com/attachments/news_article/5782/7585/tsn_thumb.jpg+++&amp;description=' + '\n' )
 I1IiI . write ( r'TSN4=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F99.m3u8&mode=10012&name===TSN+4&amp;iconimage=http%3A//contact.sourcecable.ca/wp-content/uploads/2015/05/TSN4_CMYK.jpg+&amp;fanart=http%3A//contact.sourcecable.ca/wp-content/uploads/2015/05/TSN4_CMYK.jpg+&amp;description=' + '\n' )
 I1IiI . write ( r'FOX Sports 1 Eredivisie HD"=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F531.m3u8&mode=10012&name===Fox+Sports+1+%28Nl%29&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/fox_sports1_au.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/fox_sports1_au.jpg+&amp;description=' + '\n' )
 I1IiI . write ( r'FOX Sports 2 HD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F530.m3u8&mode=10012&name===Fox+Sports+2+%28Nl%29&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/fox_sports_nl_02.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/fox_sports_nl_02.jpg+&amp;description=' + '\n' )
 I1IiI . write ( r'FOX Sports 3 Eredivisie HD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F529.m3u8&mode=10012&name===Fox+Sports+3+%28Nl%29&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/fox_sports3_au.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/fox_sports3_au.jpg+&amp;description=' + '\n' )
 I1IiI . write ( r'FOX Sports 4 HD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F528.m3u8&mode=10012&name===Fox+Sports+4+%28Nl%29&amp;iconimage=http%3A//www.sat-address.com/f/pics/logotipi/Fox-Sports-4-Int-NL_o.jpg+&amp;fanart=http%3A//www.sat-address.com/f/pics/logotipi/Fox-Sports-4-Int-NL_o.jpg+&amp;description=' + '\n' )
 I1IiI . write ( r'FOX Sports 5 Eredivisie HD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F527.m3u8&mode=10012&name===Fox+Sports+5+%28Nl%29&amp;iconimage=http%3A//www.sat-address.com/f/pics/logotipi/Fox-Sports-5-Eredivisie_o.jpg+&amp;fanart=http%3A//www.sat-address.com/f/pics/logotipi/Fox-Sports-5-Eredivisie_o.jpg+&amp;description=' + '\n' )
 I1IiI . write ( r'Arena Sport 5=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F166.m3u8&mode=10012&name===Arena+Sport+5&amp;iconimage=http%3A//fanclub365.vn/s/41663-arena_sport_5-.jpg+++&amp;fanart=http%3A//fanclub365.vn/s/41663-arena_sport_5-.jpg+++&amp;description=' + '\n' )
 I1IiI . write ( r'CBS Sports Network (CBS SN)=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F378.m3u8&mode=10012&name===CBS+Sports+%28US%29&amp;iconimage=http%3A//images.bwwstatic.com/columnpic6/2FBEB2A30-DAF8-BAC8-F5562F03F5F07369.jpg++&amp;fanart=http%3A//images.bwwstatic.com/columnpic6/2FBEB2A30-DAF8-BAC8-F5562F03F5F07369.jpg++&amp;description=' + '\n' )
 I1IiI . write ( r'NBA TV=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F304.m3u8&mode=10012&name===NBA+TV+%28US%29&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/nba_tv.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/nba_tv.jpg+&amp;description=' + '\n' )
 I1IiI . write ( r'NFL NETWORK=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F95.m3u8&mode=10012&name===NFL+Network+%28US%29&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/nfl_network.jpg++&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/nfl_network.jpg++&amp;description=' + '\n' )
 I1IiI . write ( r'Viasat Sports RU=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F278.m3u8&mode=10012&name===Viasat+Sports+RU&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/viasat_sport_no.jpg&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/viasat_sport_no.jpg&amp;description=' + '\n' )
 I1IiI . write ( r'E! Entertainment Television=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F835.m3u8&mode=10012&name===E%21+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/e_uk.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/e_uk.jpg+&amp;description=' + '\n' )
 I1IiI . write ( r'London Live=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F830.m3u8&mode=10012&name===London+Live&amp;iconimage=http%3A//www.londoncommunications.co.uk/wp-content/uploads/2014/03/London-Live.jpg+&amp;fanart=http%3A//www.londoncommunications.co.uk/wp-content/uploads/2014/03/London-Live.jpg+&amp;description=' + '\n' )
 I1IiI . write ( r'AXNHD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F842.m3u8&mode=10012&name===AXN+HD+PT&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/axn_de_hd.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/axn_de_hd.jpg+&amp;description=' + '\n' )
 I1IiI . write ( r'AXNBLACKHD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F841.m3u8&mode=10012&name===AXN+BLACK+HD+PT&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/axn_black_pt.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/axn_black_pt.jpg+&amp;description=' + '\n' )
 I1IiI . write ( r'FOX=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F845.m3u8&mode=10012&name===Fox+hd+PT&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/fox_hd_lam.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/fox_hd_lam.jpg+&amp;description=' + '\n' )
 I1IiI . write ( r'FOXLIFE=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F843.m3u8&mode=10012&name===FoxLife+HD+PT&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/fox_life_hd.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/fox_life_hd.jpg+&amp;description=' + '\n' )
 I1IiI . write ( r'FOXCRIME=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F844.m3u8&mode=10012&name===Fox+Crime+HD+PT&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/fox_crime_asia_hd.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/fox_crime_asia_hd.jpg+&amp;description=' + '\n' )
 I1IiI . write ( r'MOVHD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F839.m3u8&mode=10012&name===Mov+HD+PT&amp;iconimage=http%3A//canalmov.pt/wp-content/themes/site/images/cabecera_logo/logoprincipal.png+&amp;fanart=http%3A//canalmov.pt/wp-content/themes/site/images/cabecera_logo/logoprincipal.png+&amp;description=' + '\n' )
 I1IiI . write ( r'SYFYHD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F838.m3u8&mode=10012&name===SyFy+PT&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/syfy_universal_fr.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/syfy_universal_fr.jpg+&amp;description=' + '\n' )
 I1IiI . write ( r'True Movies 1=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F853.m3u8&mode=10012&name===True+Movies+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/true_movies1_uk.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/true_movies1_uk.jpg+&amp;description=' + '\n' )
 I1IiI . write ( r'True Movies 2 UK=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F852.m3u8&mode=10012&name===True+Movies+2+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/true_movies2.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/true_movies2.jpg+&amp;description=' + '\n' )
 I1IiI . write ( r'FOXMOVIESHD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F846.m3u8&mode=10012&name===Fox+Movies+PT&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/fox_movies_pt.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/fox_movies_pt.jpg+&amp;description=' + '\n' )
 I1IiI . write ( r'Comedy Central=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F837.m3u8&mode=10012&name===Comedy+Central+HD+US&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/comedy_central_at_hd.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/comedy_central_at_hd.jpg+&amp;description=' + '\n' )
 I1IiI . write ( r'Discovery Family Channel (DFCH)=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F836.m3u8&mode=10012&name===Discovery+Family++HD+US&amp;iconimage=https%3A//pmcdeadline2.files.wordpress.com/2015/03/discovery-family.jpg+&amp;fanart=https%3A//pmcdeadline2.files.wordpress.com/2015/03/discovery-family.jpg+&amp;description=' + '\n' )
 I1IiI . write ( r'E! (E!)=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F834.m3u8&mode=10012&name===E%21+US&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/e_uk.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/e_uk.jpg+&amp;description=' + '\n' )
 I1IiI . write ( r'ABC Family=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F833.m3u8&mode=10012&name===Family+Channel+US&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/my_family_tv.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/my_family_tv.jpg+&amp;description=' + '\n' )
 I1IiI . write ( r'VH1 (VH1)=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F828.m3u8&mode=10012&name===VH1+US&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/vh1_hd.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/vh1_hd.jpg+&amp;description=' + '\n' )
 I1IiI . write ( r'Slice=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F829.m3u8&mode=10012&name===SLICE+TV+US&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/slice.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/slice.jpg+&amp;description=' + '\n' )
 I1IiI . write ( r'Lifetime Movie Network=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F524.m3u8&mode=10012&name===LMN+US&amp;iconimage=http%3A//cdn.realscreen.com/wp/wp-content/uploads/2013/09/LMN.jpg+++&amp;fanart=http%3A//cdn.realscreen.com/wp/wp-content/uploads/2013/09/LMN.jpg+++&amp;description=' + '\n' )
 I1IiI . write ( r'Cartoon Netwrk=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F519.m3u8&mode=10012&name===Cartoon+Network+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/cartoon_network_uk.jpg++&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/cartoon_network_uk.jpg++&amp;description=' + '\n' )
 I1IiI . write ( r'Cartoon Network=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F809.m3u8&mode=10012&name===Cartoon+Network+US&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/cartoon_network_us.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/cartoon_network_us.jpg+&amp;description=' + '\n' )
 I1IiI . write ( r'CBBC=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F808.m3u8&mode=10012&name===CBBC+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/bbc_cbbc.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/bbc_cbbc.jpg+&amp;description=' + '\n' )
 I1IiI . write ( r'CBeebies=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F807.m3u8&mode=10012&name===Cbeebies&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/bbc_cbeebies_asia.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/bbc_cbeebies_asia.jpg+&amp;description=' + '\n' )
 I1IiI . write ( r'Animal Planet=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F818.m3u8&mode=10012&name===Animal+Planet+HD+US&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/animal_planet_us_hd.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/animal_planet_us_hd.jpg+&amp;description=' + '\n' )
 I1IiI . write ( r'The Discovery Channel=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F817.m3u8&mode=10012&name===Discovery+Channel+HD+US&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/discovery_ca.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/discovery_ca.jpg+&amp;description=' + '\n' )
 I1IiI . write ( r'Do-It-Yourself Network=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F815.m3u8&mode=10012&name===DIY+Network+US&amp;iconimage=http%3A//www.homesoldpledge.com/wp-content/uploads/2014/04/logo-diy-network.jpg+&amp;fanart=http%3A//www.homesoldpledge.com/wp-content/uploads/2014/04/logo-diy-network.jpg+&amp;description=' + '\n' )
 I1IiI . write ( r'H2 (H2)=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F814.m3u8&mode=10012&name===H2+US&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/history_2_us.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/history_2_us.jpg+&amp;description=' + '\n' )
 I1IiI . write ( r'History Channel (HIST)=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F813.m3u8&mode=10012&name===HISTORY+US&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/history_hd.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/history_hd.jpg+&amp;description=' + '\n' )
 I1IiI . write ( r'Investigation Discovery (ID)=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F812.m3u8&mode=10012&name===Investigation+Discovery++US&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/investigation_discovery_us_hd.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/investigation_discovery_us_hd.jpg+&amp;description=' + '\n' )
 I1IiI . write ( r'National Geographic Channel=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F810.m3u8&mode=10012&name===National+Geographic+US&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/nat_geo_eur_hd.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/nat_geo_eur_hd.jpg+&amp;description=' + '\n' )
 I1IiI . write ( r'NatGeo WILD (NGWILD)=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F811.m3u8&mode=10012&name===NAT+GEO+WILD+US&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/nat_geo_wild_us_hd.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/nat_geo_wild_us_hd.jpg+&amp;description=' + '\n' )
 I1IiI . write ( r'MTV CLASSIC=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F420.m3u8&mode=10012&name===MTV+Classic&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/mtv_classic_uk.jpg++&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/mtv_classic_uk.jpg++&amp;description=' + '\n' )
 I1IiI . write ( r'Clubland TV=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F806.m3u8&mode=10012&name===Clubland+Music&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/clubland_tv.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/clubland_tv.jpg+&amp;description=' + '\n' )
 I1IiI . write ( r'The Box=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F805.m3u8&mode=10012&name===The+Box&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/the_box_uk.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/the_box_uk.jpg+&amp;description=' + '\n' )
 I1IiI . write ( r'BoxNation=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F173.m3u8&mode=10012&name===Box+Nation+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/box_nation.jpg++&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/box_nation.jpg++&amp;description=' + '\n' )
 I1IiI . write ( r'Big Ten HD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F823.m3u8&mode=10012&name===Big+Ten+Network+US&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/big_ten_network_hd.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/big_ten_network_hd.jpg+&amp;description=' + '\n' )
 I1IiI . write ( r'MLB Network=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F822.m3u8&mode=10012&name===MLB+US&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/mlb_network.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/mlb_network.jpg+&amp;description=' + '\n' )
 I1IiI . write ( r'Willow Cricket=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F824.m3u8&mode=10012&name===Willow+Sports+HD+US&amp;iconimage=https%3A//1.bp.blogspot.com/-Ar8J69gqR44/Vuak-8J1uWI/AAAAAAAAA1o/nQgEJbrZRbQnz_iXtg4TkNU5TAg5MPDLA/s320/willow-cricket.jpg+&amp;fanart=https%3A//1.bp.blogspot.com/-Ar8J69gqR44/Vuak-8J1uWI/AAAAAAAAA1o/nQgEJbrZRbQnz_iXtg4TkNU5TAg5MPDLA/s320/willow-cricket.jpg+&amp;description=' + '\n' )
 if 57 - 57: OO0O0OoOO0 % oO0o - oO0o
 if 5 - 5: ooOoO0O00 + ii % OOooOOo
 I1IiI . write ( r'AXN White HD PT=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F840.m3u8&mode=10012&name===AXN+White+HD+PT&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/axn_white_us.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/axn_white_us.jpg+&amp;description=' + '\n' )
 I1IiI . write ( r'CINEMUNDO PT=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F847.m3u8&mode=10012&name===CINEMUNDO+PT&amp;iconimage=https%3A//i.vimeocdn.com/portrait/9079238_300x300.jpg+&amp;fanart=https%3A//i.vimeocdn.com/portrait/9079238_300x300.jpg+&amp;description=' + '\n' )
 I1IiI . write ( r'FreeForm US=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F832.m3u8&mode=10012&name===FreeForm+US&amp;iconimage=http%3A//t2.snewsi.com/188/8/18885012.jpg+&amp;fanart=http%3A//t2.snewsi.com/188/8/18885012.jpg+&amp;description=' + '\n' )
 I1IiI . write ( r'HIFI US=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F831.m3u8&mode=10012&name===HIFI+US&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/hifi_music_art.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/hifi_music_art.jpg+&amp;description=' + '\n' )
 I1IiI . write ( r'Discovery Home &amp; Health UK=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F816.m3u8&mode=10012&name===Discovery+Home+%26+Health+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/discovery_home_health_uk_plus1.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/discovery_home_health_uk_plus1.jpg+&amp;description=' + '\n' )
 I1IiI . write ( r'CITY TV=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F803.m3u8&mode=10012&name===CITY+TV&amp;iconimage=http%3A//thewatchtv.com/wp-content/uploads/2013/05/Watch-CITY-TV-Live-TV-from-Bulgaria.jpg+&amp;fanart=http%3A//thewatchtv.com/wp-content/uploads/2013/05/Watch-CITY-TV-Live-TV-from-Bulgaria.jpg+&amp;description=' + '\n' )
 I1IiI . write ( r'DANCE HD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F802.m3u8&mode=10012&name===DANCE+HD&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/dance_tv_hu.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/dance_tv_hu.jpg+&amp;description=' + '\n' )
 I1IiI . write ( r'Dream music=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F799.m3u8&mode=10012&name===Dream+music&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/dream_tv_tr.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/dream_tv_tr.jpg+&amp;description=' + '\n' )
 I1IiI . write ( r'Europe Plus Music=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F796.m3u8&mode=10012&name===Europe+Plus+Music&amp;iconimage=http%3A//1tv.ucoz.ru/logo_channel/ee.jpeg+&amp;fanart=http%3A//1tv.ucoz.ru/logo_channel/ee.jpeg+&amp;description=' + '\n' )
 I1IiI . write ( r'HITV Music=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F804.m3u8&mode=10012&name===HITV+Music&amp;iconimage=http%3A//static-cdn1.ustream.tv/i/channel/picture/8/6/3/7/8637664/8637664_hit_music_channel_1309019162%2C66x66%2Cr%3A1.jpg+&amp;fanart=http%3A//static-cdn1.ustream.tv/i/channel/picture/8/6/3/7/8637664/8637664_hit_music_channel_1309019162%2C66x66%2Cr%3A1.jpg+&amp;description=' + '\n' )
 I1IiI . write ( r'Music Channel=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F800.m3u8&mode=10012&name===Music+Channel&amp;iconimage=https%3A//upload.wikimedia.org/wikipedia/en/f/f8/Music_Choice_%2528logo%2529.jpg+&amp;fanart=https%3A//upload.wikimedia.org/wikipedia/en/f/f8/Music_Choice_%2528logo%2529.jpg+&amp;description=' + '\n' )
 I1IiI . write ( r'Heavy Metal=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F801.m3u8&mode=10012&name===Heavy+Metal&amp;iconimage=https%3A//channelpear.com/images/heavymetaltelevision.png+&amp;fanart=https%3A//channelpear.com/images/heavymetaltelevision.png+&amp;description=' + '\n' )
 I1IiI . write ( r'Si TV Music=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F797.m3u8&mode=10012&name===Si+TV+Music&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/si_tv_hn.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/si_tv_hn.jpg+&amp;description=' + '\n' )
 I1IiI . write ( r'VEVO Music=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F798.m3u8&mode=10012&name===VEVO+Music&amp;iconimage=http%3A//i.imgur.com/6Bv76t9.jpg+&amp;fanart=http%3A//i.imgur.com/6Bv76t9.jpg+&amp;description=' + '\n' )
 I1IiI . write ( r'beIN Sport 1 (Fr)=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F9.m3u8&mode=10012&name===beIN+Sport+1+%28Fr%29&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/be_in_sport1_hd.jpg++&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/be_in_sport1_hd.jpg++&amp;description=' + '\n' )
 I1IiI . write ( r'beIN Sport 2 (Fr)=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F81.m3u8&mode=10012&name===beIN+Sport+2+%28Fr%29&amp;iconimage=http%3A//3.bp.blogspot.com/-X28wcyKEmyA/Vl-TLcw3MEI/AAAAAAAAAIo/AZGqtQkviSM/s1600/index.png+&amp;fanart=http%3A//3.bp.blogspot.com/-X28wcyKEmyA/Vl-TLcw3MEI/AAAAAAAAAIo/AZGqtQkviSM/s1600/index.png+&amp;description=' + '\n' )
 I1IiI . write ( r'beIN Sport 3 (Fr)=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F82.m3u8&mode=10012&name===beIN+Sport+3+%28Fr%29&amp;iconimage=http%3A//nowwatchtvlive.me/wp-content/uploads/2014/01/beinsport_3hd.jpg+++&amp;fanart=http%3A//nowwatchtvlive.me/wp-content/uploads/2014/01/beinsport_3hd.jpg+++&amp;description=' + '\n' )
 I1IiI . write ( r'Bein Sport US HD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F766.m3u8&mode=10012&name===Bein+Sport+US+HD&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/be_in_sport_us.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/be_in_sport_us.jpg+&amp;description=' + '\n' )
 I1IiI . write ( r'RDS=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F505.m3u8&mode=10012&name===RDS&amp;iconimage=http%3A//www.bellmedia.ca/wp-content/uploads/2014/02/tv_rds-500x500.png++&amp;fanart=http%3A//www.bellmedia.ca/wp-content/uploads/2014/02/tv_rds-500x500.png++&amp;description=' + '\n' )
 I1IiI . write ( r'Fox Sports 1 (US)=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F262.m3u8&mode=10012&name===Fox+Sports+1+%28US%29&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/fox_sports_lam_basico.jpg++&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/fox_sports_lam_basico.jpg++&amp;description=' + '\n' )
 I1IiI . write ( r'Fox Sports 2 (US)=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F261.m3u8&mode=10012&name===Fox+Sports+2+%28US%29&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/fox_sports_lam_basico.jpg++&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/fox_sports_lam_basico.jpg++&amp;description=' + '\n' )
 I1IiI . write ( r'Fox Sports 1 (Asia)=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F391.m3u8&mode=10012&name===Fox+Sports+1+%28Asia%29&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/fox_sports_lam_hd.jpg++&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/fox_sports_lam_hd.jpg++&amp;description=' + '\n' )
 I1IiI . write ( r'KP+ PM HD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F475.m3u8&mode=10012&name===KP%2B+PM+HD&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/k_plus_pc.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/k_plus_pc.jpg+&amp;description=' + '\n' )
 I1IiI . write ( r'K+ 1 HD Sports/Movies=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F390.m3u8&mode=10012&name===K%2B+1+HD+Sports/Movies&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/k_plus_1.jpg++&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/k_plus_1.jpg++&amp;description=' + '\n' )
 I1IiI . write ( r'Skynet Sports HD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F473.m3u8&mode=10012&name===Skynet+Sports+HD&amp;iconimage=http%3A//www.sat-address.com/f/pics/logotipi/Sky-Net-Sports-HD_o.jpg+&amp;fanart=http%3A//www.sat-address.com/f/pics/logotipi/Sky-Net-Sports-HD_o.jpg+&amp;description=' + '\n' )
 I1IiI . write ( r'Skynet Sports 2=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F474.m3u8&mode=10012&name===Skynet+Sports+2&amp;iconimage=http%3A//www.sat-address.com/f/pics/logotipi/Sky-Net-Sports-2_o.jpg+&amp;fanart=http%3A//www.sat-address.com/f/pics/logotipi/Sky-Net-Sports-2_o.jpg+&amp;description=' + '\n' )
 I1IiI . write ( r'True SportsHD 3=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F274.m3u8&mode=10012&name===True+SportsHD+3&amp;iconimage=http%3A//stepfb.net/live/movieposters/22.jpg+&amp;fanart=http%3A//stepfb.net/live/movieposters/22.jpg+&amp;description=' + '\n' )
 I1IiI . write ( r'True Sport 2=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F276.m3u8&mode=10012&name===True+Sport+2&amp;iconimage=http%3A//tv-online.im/wp-content/uploads/2013/10/True-Sport-2-LIVE.jpg&amp;fanart=http%3A//tv-online.im/wp-content/uploads/2013/10/True-Sport-2-LIVE.jpg&amp;description=' + '\n' )
 I1IiI . write ( r'NBC Sports Network (US)=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F209.m3u8&mode=10012&name===NBC+Sports+Network+%28US%29&amp;iconimage=http%3A//www.nyinterconnect.com/wp-content/uploads/nbc_sports.jpg+++&amp;fanart=http%3A//www.nyinterconnect.com/wp-content/uploads/nbc_sports.jpg+++&amp;description=' + '\n' )
 I1IiI . write ( r'EPL Extra Time 1 (USA TV)=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F255.m3u8&mode=10012&name===EPL+Extra+Time+1+%28USA+TV%29&amp;iconimage=https%3A//secure.toolkitfiles.co.uk/clients/7007/siteimages/medium/Premier_League_logo.jpg++&amp;fanart=https%3A//secure.toolkitfiles.co.uk/clients/7007/siteimages/medium/Premier_League_logo.jpg++&amp;description=' + '\n' )
 I1IiI . write ( r'EPL Extra Time 3 (Spike USA)=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F257.m3u8&mode=10012&name===EPL+Extra+Time+3+%28Spike+USA%29&amp;iconimage=https%3A//secure.toolkitfiles.co.uk/clients/7007/siteimages/medium/Premier_League_logo.jpg++&amp;fanart=https%3A//secure.toolkitfiles.co.uk/clients/7007/siteimages/medium/Premier_League_logo.jpg++&amp;description=' + '\n' )
 I1IiI . write ( r'EPL Extra Time 4 (AXS TV)=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F258.m3u8&mode=10012&name===EPL+Extra+Time+4+%28AXS+TV%29&amp;iconimage=https%3A//secure.toolkitfiles.co.uk/clients/7007/siteimages/medium/Premier_League_logo.jpg++&amp;fanart=https%3A//secure.toolkitfiles.co.uk/clients/7007/siteimages/medium/Premier_League_logo.jpg++&amp;description=' + '\n' )
 I1IiI . write ( r'Sportsnet World=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F367.m3u8&mode=10012&name===Sportsnet+World+HD+US&amp;iconimage=http%3A//www.stream2watch.co/images/thumbs/sportsnet%2520world%2520live%2520stream.jpg++&amp;fanart=http%3A//www.stream2watch.co/images/thumbs/sportsnet%2520world%2520live%2520stream.jpg++&amp;description=' + '\n' )
 I1IiI . write ( r'Sportsnet NY=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F385.m3u8&mode=10012&name===Sportsnet+Ontario+HD&amp;iconimage=http%3A//www.stream2watch.co/images/thumbs/Sportsnet_ontario%2520live%2520stream.jpg+&amp;fanart=http%3A//www.stream2watch.co/images/thumbs/Sportsnet_ontario%2520live%2520stream.jpg+&amp;description=' + '\n' )
 I1IiI . write ( r'Sportsnet One HD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F259.m3u8&mode=10012&name===Sportsnet+One+HD&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/sportsnet_one.jpg++&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/sportsnet_one.jpg++&amp;description=' + '\n' )
 I1IiI . write ( r'ESPN=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F314.m3u8&mode=10012&name===ESPN+%28US%29&amp;iconimage=http%3A//www.allaccess.com/assets/img/editorial/raw/es/espn.jpg&amp;fanart=http%3A//www.allaccess.com/assets/img/editorial/raw/es/espn.jpg&amp;description=' + '\n' )
 I1IiI . write ( r'ESPN 2 (US)=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F315.m3u8&mode=10012&name===ESPN+2+%28US%29&amp;iconimage=http%3A//www.lime.com/widgets/limetv/bb-coverflow/images/channel-logos/espn2-logo.jpg+&amp;fanart=http%3A//www.lime.com/widgets/limetv/bb-coverflow/images/channel-logos/espn2-logo.jpg+&amp;description=' + '\n' )
 I1IiI . write ( r'Sport Klub 1=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F594.m3u8&mode=10012&name===Sport+Klub+1&amp;iconimage=http%3A//www.stream2watch.co/images/thumbs/sport_klub_si_1.jpg+&amp;fanart=http%3A//www.stream2watch.co/images/thumbs/sport_klub_si_1.jpg+&amp;description=' + '\n' )
 I1IiI . write ( r'Sport Klub 2=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F593.m3u8&mode=10012&name===Sport+Klub+2&amp;iconimage=http%3A//www.sat-address.com/f/pics/logotipi/Sport-Klub-2-Slovenia_o.jpg+&amp;fanart=http%3A//www.sat-address.com/f/pics/logotipi/Sport-Klub-2-Slovenia_o.jpg+&amp;description=' + '\n' )
 I1IiI . write ( r'Sport Klub 3=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F592.m3u8&mode=10012&name===Sport+Klub+3&amp;iconimage=http%3A//www.sat-address.com/f/pics/logotipi/Sport-Klub-3-Slovenia_o.jpg+&amp;fanart=http%3A//www.sat-address.com/f/pics/logotipi/Sport-Klub-3-Slovenia_o.jpg+&amp;description=' + '\n' )
 I1IiI . write ( r'Golf HD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F260.m3u8&mode=10012&name===Golf+HD&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/golf_channel_us_hd.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/golf_channel_us_hd.jpg+&amp;description=' + '\n' )
 I1IiI . write ( r'Golf Channel 1080p=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F332.m3u8&mode=10012&name===Golf+Channel+1080p&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/golf_channel_us_hd.jpg&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/golf_channel_us_hd.jpg&amp;description=' + '\n' )
 I1IiI . write ( r'WWENetwork=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F178.m3u8&mode=10012&name===WWENetwork&amp;iconimage=http%3A//3.bp.blogspot.com/-d6ZVw8_zw14/VWh38v-qd2I/AAAAAAAAFKQ/9_kwqxiqYUc/s320/20140102_EPLIGHT_Network_Announcement_nodate_C.jpg++&amp;fanart=http%3A//3.bp.blogspot.com/-d6ZVw8_zw14/VWh38v-qd2I/AAAAAAAAFKQ/9_kwqxiqYUc/s320/20140102_EPLIGHT_Network_Announcement_nodate_C.jpg++&amp;description=' + '\n' )
 I1IiI . write ( r'Motor Sports 1 Aus=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F281.m3u8&mode=10012&name===Motor+Sports+1+Aus&amp;iconimage=http%3A//4.bp.blogspot.com/_Fb0x6TGTbPs/SMhHr89KwEI/AAAAAAAABkU/CCkn-Bo_iEY/s400/motosport%2Btv.JPG++&amp;fanart=http%3A//4.bp.blogspot.com/_Fb0x6TGTbPs/SMhHr89KwEI/AAAAAAAABkU/CCkn-Bo_iEY/s400/motosport%2Btv.JPG++&amp;description=' + '\n' )
 I1IiI . write ( r'Fight Sports (USEE)=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F433.m3u8&mode=10012&name===Fight+Sports+%28USEE%29&amp;iconimage=http%3A//www.frocus.net/images/logotv/original/fight-channel.jpg+&amp;fanart=http%3A//www.frocus.net/images/logotv/original/fight-channel.jpg+&amp;description=' + '\n' )
 I1IiI . write ( r'Sky Sport 2 IT=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F471.m3u8&mode=10012&name===Sky+Sport+2+IT&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/sky_it_sport2_hd.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/sky_it_sport2_hd.jpg+&amp;description=' + '\n' )
 I1IiI . write ( r'Sky Sport 1 IT=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F472.m3u8&mode=10012&name===Sky+Sport+1+IT&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/sky_it_sport1_hd.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/sky_it_sport1_hd.jpg+&amp;description=' + '\n' )
 I1IiI . write ( r'TyC Sports=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F31.m3u8&mode=10012&name===TyC+Sports&amp;iconimage=http%3A//1.bp.blogspot.com/_yDxTw4hZsW8/TEnPHPkFjqI/AAAAAAAAQsk/IJH-Y4kFA8g/s400/TYC_logo.jpg++&amp;fanart=http%3A//1.bp.blogspot.com/_yDxTw4hZsW8/TEnPHPkFjqI/AAAAAAAAQsk/IJH-Y4kFA8g/s400/TYC_logo.jpg++&amp;description=' + '\n' )
 I1IiI . write ( r'ORF Sport +=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F423.m3u8&mode=10012&name===ORF+Sport+%2B&amp;iconimage=http%3A//tubestatic.orf.at/static/images/site/tube/20141042/17.10.14-sporthd.5298157.jpg+&amp;fanart=http%3A//tubestatic.orf.at/static/images/site/tube/20141042/17.10.14-sporthd.5298157.jpg+&amp;description=' + '\n' )
 if 63 - 63: oO0o / OOooOOo * iI11I1II1I1I . Oo0o00
 if 85 - 85: Ii / Ii . oO0o . o0o00Oo0O
def OooOo ( ) :
 OoO000O0Oo = OO0oOO0O ( i1111 ( 'aHR0cDovL2dlbmlldHYuY28udWsvMjQ3c3RyZWFtLm0zdQ==' ) )
 Ii1 = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( OoO000O0Oo )
 for o0O0oo0OO0O , IiIIIIIi in Ii1 :
  OoOO ( o0O0oo0OO0O , ( IiIIIIIi ) . strip ( ) , 222 , iIIIi1 + '247.png' , iIIIi1 + '247.png' , '' )
def oOo0 ( ) :
 OoO000O0Oo = OO0oOO0O ( i1111 ( 'aHR0cDovL2dlbmlldHYuY28udWsvbXVzaWMubTN1' ) )
 Ii1 = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( OoO000O0Oo )
 for o0O0oo0OO0O , IiIIIIIi in Ii1 :
  OoOO ( o0O0oo0OO0O , ( IiIIIIIi ) . strip ( ) , 222 , iIIIi1 + 'musicch.png' , iIIIi1 + 'musicch.png' , '' )
def I1Ii11i ( ) :
 OoO000O0Oo = OO0oOO0O ( i1111 ( 'aHR0cDovL2dlbmlldHYuY28udWsvbmV3cy5tM3U=' ) )
 Ii1 = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( OoO000O0Oo )
 for o0O0oo0OO0O , IiIIIIIi in Ii1 :
  OoOO ( o0O0oo0OO0O , ( IiIIIIIi ) . strip ( ) , 222 , iIIIi1 + 'NEWS.png' , iIIIi1 + 'NEWS.png' , '' )
def I1iIiiiI1 ( ) :
 OoO000O0Oo = OO0oOO0O ( i1111 ( 'aHR0cDovL2dlbmlldHYuY28udWsvYWR1bHQubTN1' ) )
 Ii1 = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( OoO000O0Oo )
 for o0O0oo0OO0O , IiIIIIIi in Ii1 :
  OoOO ( o0O0oo0OO0O , ( IiIIIIIi ) . strip ( ) , 222 , iIIIi1 + 'adult.png' , iIIIi1 + 'adult.png' , '' )
def OOO0O00Oo ( ) :
 OoO000O0Oo = OO0oOO0O ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9pVHZfU3RyZWFtcy9UVVRTL21haW4ucGhw' ) )
 Ii1 = re . compile ( 'href="/watch?v=(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( OoO000O0Oo )
 for IiIIIIIi , o0O0oo0OO0O in Ii1 :
  OoOO ( o0O0oo0OO0O , IiIIIIIi , 1016 , iIIIi1 + 'TUTS.png' , iIIIi1 + 'TUTS.png' , '' )
  if 13 - 13: iI11I1II1I1I
  if 2 - 2: ooOoO0O00 * OoOOOOO - OoOOOOO + ii % OOooOOo / OOooOOo
def i11IiI1iiI11 ( ) :
 if 85 - 85: Ii1I - OOooOOo / Ii1I + iIi1i111II - OO0O0OoOO0
 ooOOO0 ( '[COLOR' + oO0o0o0ooO0oO + ']Recent Episodes[/COLOR]' , '' , 10019 , iIIIi1 + 'dtv.png' , i1iIIi1 , '' )
 ooOOO0 ( '[COLOR' + oO0o0o0ooO0oO + ']Genres[/COLOR]' , '' , 10020 , iIIIi1 + 'dtv.png' , i1iIIi1 , '' )
 ooOOO0 ( '[COLOR' + oO0o0o0ooO0oO + ']Search[/COLOR]' , '' , 10021 , iIIIi1 + 'dtv.png' , i1iIIi1 , '' )
 if 49 - 49: oO0o - o0o00Oo0O / oO0o * OOooOOo + Oo0o00
def Iiii1I ( ) :
 if 61 - 61: iI11I1II1I1I - I1i1IiI1 / OO0O0OoOO0 * I1i1IiI1 % I1i1III % OO0O0OoOO0
 OoO000O0Oo = cloudflare . source ( i1111 ( 'aHR0cDovL2RpemlsYWIuY29t' ) )
 Ii1 = re . compile ( '<li id=".+?">.+?<a href="(.+?)">.+?<img width="40" height="40" src="(.+?)" alt=""/>.+?<span class="title">\n(.+?)</span>.+?<span class="alt-title">\n(.+?)</span>.+?</a>.+?</li>' , re . DOTALL ) . findall ( OoO000O0Oo )
 for IiIIIIIi , i11ii1ii11i , o0O0oo0OO0O , iiOO0O0Ooo in Ii1 :
  ooOOO0 ( o0O0oo0OO0O + '  -  ' + ( iiOO0O0Ooo ) . replace ( 'sezon' , 'Season' ) . replace ( 'bölüm' , 'Episode' ) , IiIIIIIi , 10023 , iIIIi1 + 'dtv.png' , i1iIIi1 , '' )
  if 63 - 63: iIi1i111II % iI11I1II1I1I
  if 20 - 20: oO0o . oOo0O0Ooo * Ii / Ii
  if 89 - 89: OO0O0OoOO0 . Ii * o0o00Oo0O
def Iiii1 ( ) :
 if 27 - 27: iIi1i111II
 ooOOO0 ( '[COLOR' + oO0o0o0ooO0oO + ']Action[/COLOR]' , 'Aksiyon' , 10024 , iIIIi1 + 'dtv.png' , i1iIIi1 , '' )
 ooOOO0 ( '[COLOR' + oO0o0o0ooO0oO + ']Adventure[/COLOR]' , 'Macera' , 10024 , iIIIi1 + 'dtv.png' , i1iIIi1 , '' )
 ooOOO0 ( '[COLOR' + oO0o0o0ooO0oO + ']Animation[/COLOR]' , 'Animasyon' , 10024 , iIIIi1 + 'dtv.png' , i1iIIi1 , '' )
 ooOOO0 ( '[COLOR' + oO0o0o0ooO0oO + ']Anime[/COLOR]' , 'Anime' , 10024 , iIIIi1 + 'dtv.png' , i1iIIi1 , '' )
 ooOOO0 ( '[COLOR' + oO0o0o0ooO0oO + ']Biography[/COLOR]' , 'Biyografi' , 10024 , iIIIi1 + 'dtv.png' , i1iIIi1 , '' )
 ooOOO0 ( '[COLOR' + oO0o0o0ooO0oO + ']Comedy[/COLOR]' , 'Komedi' , 10024 , iIIIi1 + 'dtv.png' , i1iIIi1 , '' )
 ooOOO0 ( '[COLOR' + oO0o0o0ooO0oO + ']Crime[/COLOR]' , 'Su%C3%A7' , 10024 , iIIIi1 + 'dtv.png' , i1iIIi1 , '' )
 ooOOO0 ( '[COLOR' + oO0o0o0ooO0oO + ']Documentary[/COLOR]' , 'Belgesel' , 10024 , iIIIi1 + 'dtv.png' , i1iIIi1 , '' )
 ooOOO0 ( '[COLOR' + oO0o0o0ooO0oO + ']Drama[/COLOR]' , 'Dram' , 10024 , iIIIi1 + 'dtv.png' , i1iIIi1 , '' )
 ooOOO0 ( '[COLOR' + oO0o0o0ooO0oO + ']Family[/COLOR]' , 'Aile' , 10024 , iIIIi1 + 'dtv.png' , i1iIIi1 , '' )
 ooOOO0 ( '[COLOR' + oO0o0o0ooO0oO + ']Fantasy[/COLOR]' , 'Fantastik' , 10024 , iIIIi1 + 'dtv.png' , i1iIIi1 , '' )
 ooOOO0 ( '[COLOR' + oO0o0o0ooO0oO + ']History[/COLOR]' , 'Tarih' , 10024 , iIIIi1 + 'dtv.png' , i1iIIi1 , '' )
 ooOOO0 ( '[COLOR' + oO0o0o0ooO0oO + ']Horror[/COLOR]' , 'Korku' , 10024 , iIIIi1 + 'dtv.png' , i1iIIi1 , '' )
 ooOOO0 ( '[COLOR' + oO0o0o0ooO0oO + ']Mini-Series[/COLOR]' , 'Mini%20Dizi' , 10024 , iIIIi1 + 'dtv.png' , i1iIIi1 , '' )
 ooOOO0 ( '[COLOR' + oO0o0o0ooO0oO + ']Musical[/COLOR]' , 'M%C3%BCzikal' , 10024 , iIIIi1 + 'dtv.png' , i1iIIi1 , '' )
 ooOOO0 ( '[COLOR' + oO0o0o0ooO0oO + ']Mystery[/COLOR]' , 'Gizem' , 10024 , iIIIi1 + 'dtv.png' , i1iIIi1 , '' )
 ooOOO0 ( '[COLOR' + oO0o0o0ooO0oO + ']Romance[/COLOR]' , 'Romantik' , 10024 , iIIIi1 + 'dtv.png' , i1iIIi1 , '' )
 ooOOO0 ( '[COLOR' + oO0o0o0ooO0oO + ']Science Fiction[/COLOR]' , 'Bilim%20Kurgu' , 10024 , iIIIi1 + 'dtv.png' , i1iIIi1 , '' )
 ooOOO0 ( '[COLOR' + oO0o0o0ooO0oO + ']Sport[/COLOR]' , 'Spor' , 10024 , iIIIi1 + 'dtv.png' , i1iIIi1 , '' )
 ooOOO0 ( '[COLOR' + oO0o0o0ooO0oO + ']Thriller[/COLOR]' , 'Gerilim' , 10024 , iIIIi1 + 'dtv.png' , i1iIIi1 , '' )
 ooOOO0 ( '[COLOR' + oO0o0o0ooO0oO + ']War[/COLOR]' , 'Sava%C5%9F' , 10024 , iIIIi1 + 'dtv.png' , i1iIIi1 , '' )
 ooOOO0 ( '[COLOR' + oO0o0o0ooO0oO + ']Western[/COLOR]' , 'Tarih' , 10024 , iIIIi1 + 'dtv.png' , i1iIIi1 , '' )
 ooOOO0 ( '[COLOR' + oO0o0o0ooO0oO + ']Youth[/COLOR]' , 'Gen%C3%A7lik' , 10024 , iIIIi1 + 'dtv.png' , i1iIIi1 , '' )
 if 52 - 52: Oo0o00 % OOooOOo + iI11I1II1I1I * OoOOOOO . I1i1III
def OoOooOO0oOOo0O ( url ) :
 I1I1I1IIi1III = 'http://dizilab.com/arsiv?limit=100&tur=' + url + '&orderby=&ulke=&order=&yil=&dizi_adi='
 oOOoO0O0O0 = cloudflare . source ( I1I1I1IIi1III )
 Ii1 = re . compile ( '<div class="tv-series-single">.+?<a href="(.+?)" class="film-image">.+?<img src="(.+?)" alt=""/>.+?<span class="position">.+?</span>\n(.+?)</a>' , re . DOTALL ) . findall ( oOOoO0O0O0 )
 for url , i11ii1ii11i , o0O0oo0OO0O in Ii1 :
  ooOOO0 ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' , url , 10022 , iIIIi1 + 'dtv.png' , i1iIIi1 , '' )
  if 42 - 42: OO0O0OoOO0 / I11i + I1ii11iIi11i . I1ii11iIi11i % iIi1i111II
  if 16 - 16: ooOoO0O00 + oO0o % OOooOOo + I1i1III * I1ii11iIi11i
  if 3 - 3: Ii
  if 81 - 81: oOo0O0Ooo . ii * I1i1III . OoOOOOO - o0o00Oo0O * OoOOOOO
def OoO0Oo00 ( ) :
 if 1 - 1: Oo0o00 - I1i1IiI1
 O0oOOoooOO0O = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 Oo0o0O00 = O0oOOoooOO0O . lower ( )
 IiIIIIIi = ( i1111 ( 'aHR0cDovL2RpemlsYWIuY29tL2Fyc2l2P2xpbWl0PSZ0dXI9Jm9yZGVyYnk9JnVsa2U9Jm9yZGVyPSZ5aWw9JmRpemlfYWRpPQ==' ) ) + ( O0oOOoooOO0O ) . replace ( ' ' , '+' )
 oOOoO0O0O0 = cloudflare . source ( IiIIIIIi )
 Ii1 = re . compile ( '<a href="(.+?)" class="film-image">\n<img src="(.+?)" alt=""/>\n</a>\n<div class="tss-detail">\n<a class="title" style="" href=".+?">\n<span class="position">.+?</span>\n(.+?)</a>' ) . findall ( oOOoO0O0O0 )
 for IiIIIIIi , i11ii1ii11i , o0O0oo0OO0O in Ii1 :
  if O0oOOoooOO0O in o0O0oo0OO0O . lower ( ) :
   ooOOO0 ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' , IiIIIIIi , 10022 , iIIIi1 + 'dtv.png' )
   if 45 - 45: I1i1III - iIi1i111II
   if 70 - 70: oO0o % oOo0O0Ooo / oOo0O0Ooo . I1i1IiI1 % oOo . IIiIiII11i
   if 10 - 10: I1i1III - Ii . Ii1I % ooOoO0O00
def OooOOOoOoo0O0 ( url ) :
 oOOoO0O0O0 = cloudflare . source ( url )
 Ii1 = re . compile ( '<a class="season" href="(.+?)">\n(.+?)\n</a>.+?<a class="episode" href=".+?">\n(.+?)\n</a>.+?<a class="episode-name" href=".+?">\n(.+?)</a>' , re . DOTALL ) . findall ( oOOoO0O0O0 )
 for i1I1IiiIi1i , O0OOOOo0 , OOooO0Oo00 , o0O0oo0OO0O in Ii1 :
  iIIIIIIIiIII = ( OOooO0Oo00 ) . replace ( 'Sezon' , '' ) . replace ( 'bölüm' , '' ) . replace ( 'Bölüm' , '' ) . replace ( 'BÃ¶lÃ¼m' , '' ) . replace ( '.' , '' )
  o0oo0o00ooO00 = ( O0OOOOo0 ) . replace ( 'bölüm' , '' ) . replace ( 'Sezon' , '' ) . replace ( 'Bölüm' , '' ) . replace ( 'BÃ¶lÃ¼m' , '' ) . replace ( '.' , '' )
  IIiIiiI1i = 'Season ' + o0oo0o00ooO00 + 'Episode ' + iIIIIIIIiIII + o0O0oo0OO0O
  IIiO0Oo ( IIiIiiI1i , i1I1IiiIi1i )
  if 35 - 35: Ii1I + Oo0o00 - OOooOOo % OoOOOOO % I11i % OOooOOo
  xbmcplugin . addSortMethod ( I11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 45 - 45: oOo0O0Ooo * iIi1i111II % oO0o
  if 24 - 24: oOo - I1i1IiI1 * OoOOOOO
def IIiO0Oo ( name , url ) :
 i1I1IiiIi1i = url
 O00OoOoO = name
 Oo000o = cloudflare . source ( i1I1IiiIi1i )
 OOooOO000 = re . compile ( 'file: "(.+?)",.+?label: "(.+?)",' , re . DOTALL ) . findall ( Oo000o )
 for IIi , ooO0o0oo in OOooOO000 :
  Ooo0OOoOoO0 ( '[COLOR' + oO0o0o0ooO0oO + ']' + O00OoOoO + ooO0o0oo + '[/COLOR]' , IIi , 10012 , iIIIi1 + 'dtv.png' )
  if 79 - 79: i1I11i1I % oO0o
 xbmcplugin . addSortMethod ( I11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 81 - 81: Ii + Ii * oO0o + i1I11i1I
 if 32 - 32: o0o00Oo0O . ii
def iiI ( ) :
 if 17 - 17: Ii / I1ii11iIi11i . oO0o / oOo0O0Ooo
 if 38 - 38: ooOoO0O00 . Ii1I % I1i1III + iI11I1II1I1I + o0o00Oo0O
 if 47 - 47: oO0o + i1I11i1I / IIiIiII11i
 if 97 - 97: Ii1I / oOo0O0Ooo % o0o00Oo0O + ooOoO0O00 - oOo
 if 38 - 38: I11i % Oo0o00 + Ii + OO0O0OoOO0 + oOo / Ii
 if 94 - 94: OO0O0OoOO0 - I1ii11iIi11i + OoOOOOO
 if 59 - 59: I1i1IiI1 . oOo0O0Ooo - iI11I1II1I1I + iI11I1II1I1I
 if 56 - 56: OoOOOOO + oOo
 if 32 - 32: IIiIiII11i + OOooOOo % oOo / OOooOOo + Ii1I
 if 2 - 2: Ii - Oo0o00 + oO0o % I1i1IiI1 * I1i1III
 if 54 - 54: o0o00Oo0O - OO0O0OoOO0 . iIi1i111II % OO0O0OoOO0 + OO0O0OoOO0
 if 36 - 36: iIi1i111II % Ii
 if 47 - 47: ooOoO0O00 + IIiIiII11i . I1ii11iIi11i * OoOOOOO . I1i1IiI1 / ooOoO0O00
 ooOOO0 ( '[COLOR' + oO0o0o0ooO0oO + ']Newest Episodes Added[/COLOR]' , 'http://www.watchseries.ac/latest' , 10046 , iIIIi1 + 'WATCHSERIES.png' , '' , '' )
 ooOOO0 ( '[COLOR' + oO0o0o0ooO0oO + ']This Week\'s Popular Episodes[/COLOR]' , 'http://www.watchseries.ac/new' , 10042 , iIIIi1 + 'WATCHSERIES.png' , '' , '' )
 ooOOO0 ( '[COLOR' + oO0o0o0ooO0oO + ']Genres[/COLOR]' , 'http://www.watchseries.ac/series' , 10048 , iIIIi1 + 'WATCHSERIES.png' , '' , '' )
 ooOOO0 ( '[COLOR' + oO0o0o0ooO0oO + ']Series[/COLOR]' , 'http://www.watchseries.ac/series' , 10041 , iIIIi1 + 'WATCHSERIES.png' , '' , '' )
 ooOOO0 ( '[COLOR' + oO0o0o0ooO0oO + ']Search Program[/COLOR]' , '' , 10043 , iIIIi1 + 'WATCHSERIES.png' , '' , '' )
 if 50 - 50: Oo0o00 / ooOoO0O00 % ii
 if 83 - 83: Ii1I * Ii1I + iIi1i111II
def OooooOoO ( url ) :
 oOOoO0O0O0 = OO0oOO0O ( url )
 oOoO0 = re . compile ( '<ul class="pagination" style="line-height: 3;">(.+?)</ul>' , re . DOTALL ) . findall ( oOOoO0O0O0 )
 Ii1 = re . compile ( '<li><a href="/letters/(.+?)">(.+?)</a></li>' ) . findall ( str ( oOoO0 ) )
 for url , o0O0oo0OO0O in Ii1 :
  ooOOO0 ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' , 'http://www.watchseries.ac/letters/' + url , 10049 , iIIIi1 + 'WATCHSERIES.png' , '' , '' )
  if 79 - 79: oOo % iIi1i111II
def oO0O0o0O ( url ) :
 oOOoO0O0O0 = OO0oOO0O ( url )
 Ii1 = re . compile ( '<a href="(.+?)" class="sr-header">(.+?)</a>' ) . findall ( oOOoO0O0O0 )
 for url , o0O0oo0OO0O in Ii1 :
  ooOOO0 ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' , 'http://www.watchseries.ac/' + url , 10049 , iIIIi1 + 'WATCHSERIES.png' , '' , '' )
  if 100 - 100: OOooOOo % I1ii11iIi11i
def OoOOiI ( url ) :
 oOOoO0O0O0 = OO0oOO0O ( url )
 Ii1 = re . compile ( '<li class="col-md-6 col-xs-12 list-movies-li"><a href="(.+?)" title=".+?">(.+?)<span class="epnum">.+?</span></a></li>' , re . DOTALL ) . findall ( oOOoO0O0O0 )
 OOooOO000 = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="(.+?)">Next</a></li></ul>' , re . DOTALL ) . findall ( oOOoO0O0O0 )
 for url , o0O0oo0OO0O in Ii1 :
  ooOOO0 ( '[COLOR' + oO0o0o0ooO0oO + ']' + ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' ) + '[/COLOR]' , 'http://www.watchseries.ac' + url , 10044 , iIIIi1 + 'WATCHSERIES.png' , '' , '' )
 for url in OOooOO000 :
  ooOOO0 ( '[COLOR' + oO0o0o0ooO0oO + ']' + 'NEXT' + '[/COLOR]' , 'http://www.watchseries.ac' + url , 10049 , iIIIi1 + 'Next.png' , '' , '' )
  if 3 - 3: oO0o * ooOoO0O00 . oOo0O0Ooo . o0o00Oo0O - OOooOOo
  if 81 - 81: oOo0O0Ooo - iI11I1II1I1I / oOo0O0Ooo / o0o00Oo0O
def I1I1IIiiii1ii ( ) :
 O0oOOoooOO0O = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oOo0O = 'http://www.watchseries.ac/search/' + O0oOOoooOO0O . replace ( ' ' , '%20' )
 oOOoO0O0O0 = OO0oOO0O ( oOo0O )
 Ii1 = re . compile ( '<img src="(.+?)".+?<a href="(.+?)" title=".+?"><b>(.+?)</b>' , re . DOTALL ) . findall ( oOOoO0O0O0 )
 for i11ii1ii11i , IiIIIIIi , o0O0oo0OO0O in Ii1 :
  if 'watch online' in o0O0oo0OO0O :
   pass
  else :
   print IiIIIIIi
   ooOOO0 ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' , 'http://www.watchseries.ac' + IiIIIIIi , 10044 , i11ii1ii11i , '' , '' )
   if 30 - 30: I1i1III . Ii1I / iIi1i111II
   xbmcplugin . setContent ( I11i1 , 'movies' )
   if 2 - 2: i1I11i1I % oOo0O0Ooo - Oo0o00
def oooOo ( url ) :
 oOOoO0O0O0 = OO0oOO0O ( url )
 Ii1 = re . compile ( '<img src="(.+?)".+?<div class="block-left-home-inside-text">.+?<a href="(.+?)" title=".+?"><b>(.+?)</b> <br>.+?<span class=".+?">(.+?)</span></a><br>(.+?)<br>' , re . DOTALL ) . findall ( oOOoO0O0O0 )
 for i11ii1ii11i , url , o0O0oo0OO0O , OOooO0Oo00 , O00OoOO0oo0 in Ii1 :
  oOoO0Oo0 = ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' ) + ' - ' + ( OOooO0Oo00 ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' )
  ooOOO0 ( '[COLOR' + oO0o0o0ooO0oO + ']' + oOoO0Oo0 + '[/COLOR]' , 'http://www.watchseries.ac' + url , 10045 , i11ii1ii11i , '' , O00OoOO0oo0 )
  if 7 - 7: oOo + I1i1III
def IiiIIiI1iI1 ( url ) :
 oOOoO0O0O0 = OO0oOO0O ( url )
 Ii1 = re . compile ( '<li class="col-md-6 col-xs-12 list-movies-li"><a href="(.+?)" title=".+?">(.+?)<span class="epnum">.+?</span></a></li>' , re . DOTALL ) . findall ( oOOoO0O0O0 )
 OOooOO000 = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="(.+?)">Next</a></li></ul>' , re . DOTALL ) . findall ( oOOoO0O0O0 )
 for url , o0O0oo0OO0O in Ii1 :
  oOoO0Oo0 = ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' )
  ooOOO0 ( '[COLOR' + oO0o0o0ooO0oO + ']' + oOoO0Oo0 + '[/COLOR]' , 'http://www.watchseries.ac' + url , 10045 , iIIIi1 + 'WATCHSERIES.png' , '' , '' )
 for url in OOooOO000 :
  ooOOO0 ( '[COLOR' + oO0o0o0ooO0oO + ']' + 'NEXT' + '[/COLOR]' , 'http://www.watchseries.ac' + url , 10046 , iIIIi1 + 'Next.png' , '' , '' )
  if 86 - 86: ooOoO0O00 / I1i1III * oOo0O0Ooo
def OOoO0OOoO0ooo ( url ) :
 oOOoO0O0O0 = OO0oOO0O ( url )
 Ii1 = re . compile ( '<div class="mask">.+?<a href="(.+?)" title="(.+?)">.+?<img src="(.+?)"' , re . DOTALL ) . findall ( oOOoO0O0O0 )
 OOooOO000 = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="(.+?)">Next</a></li></ul>' , re . DOTALL ) . findall ( oOOoO0O0O0 )
 for url , o0O0oo0OO0O , i11ii1ii11i in Ii1 :
  ooOOO0 ( '[COLOR' + oO0o0o0ooO0oO + ']' + ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' ) + '[/COLOR]' , 'http://www.watchseries.ac' + url , 10044 , i11ii1ii11i , '' , '' )
 for url in OOooOO000 :
  ooOOO0 ( '[COLOR' + oO0o0o0ooO0oO + ']' + 'NEXT' + '[/COLOR]' , 'http://www.watchseries.ac' + url , 10041 , iIIIi1 + 'Next.png' , '' , '' )
  if 23 - 23: ooOoO0O00 - I1i1IiI1
def ooo0Oooooo ( url ) :
 oOOoO0O0O0 = OO0oOO0O ( url )
 Ii1 = re . compile ( '<meta itemprop="url" content="([^"]*)">.+?<a href="([^"]*)" class="table-link">' , re . DOTALL ) . findall ( oOOoO0O0O0 )
 oOoO0 = re . compile ( '<div class="col-md-6 col-xs-12".+?<a href=".+?" itemprop="url"><span itemprop="name">(.+?)</span>(.+?)</ul>' , re . DOTALL ) . findall ( oOOoO0O0O0 )
 for O0OOOOo0 , Ii11Iii in oOoO0 :
  Ii1 = re . compile ( '<li itemprop="episode".+?<meta itemprop="url" content="(.+?)">.+?<span class="" itemprop="name">\n(.+?)\n' , re . DOTALL ) . findall ( str ( Ii11Iii ) )
  for url , o0O0oo0OO0O in Ii1 :
   oOoO0Oo0 = ( O0OOOOo0 ) . replace ( '  ' , '' ) + ' ' + ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&#039;' , '\'' ) . replace ( '  ' , '' )
   ooOOO0 ( '[COLOR' + oO0o0o0ooO0oO + ']' + oOoO0Oo0 + '[/COLOR]' , 'http://www.watchseries.ac' + url , 10045 , iIIIi1 + 'WATCHSERIES.png' , '' , '' )
 OOooOO000 = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="(.+?)">Next</a></li></ul>' , re . DOTALL ) . findall ( oOOoO0O0O0 )
 for o0O0oo0OO0O , url in Ii1 :
  ooOOO0 ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' ) . replace ( '/episode/' , '' ) . replace ( '_' , ' ' ) . replace ( '.html' , '' ) , 'http://www.watchseries.ac' + url , 10045 , iIIIi1 + 'WATCHSERIES.png' , '' , '' )
 for url in OOooOO000 :
  ooOOO0 ( '[COLOR' + oO0o0o0ooO0oO + ']' + 'NEXT' + '[/COLOR]' , 'http://www.watchseries.ac' + url , 10044 , iIIIi1 + 'Next.png' , '' , '' )
  xbmcplugin . addSortMethod ( I11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 59 - 59: Ii . ii / I1i1IiI1 * Ii1I + ii
class Ii1I1i1ii1I1 ( ) :
 if 98 - 98: i1I11i1I * iI11I1II1I1I . I1i1III * I1ii11iIi11i / Ii1I + oOo
 List = [ ]
 source_list = [ ]
 def __init__ ( self , name ) :
  if 25 - 25: OoOOOOO
  oOoO0Oo0 = name
  self . Get_Sources ( IiIIIIIi , oOoO0Oo0 )
  if 19 - 19: oOo0O0Ooo % I1i1III . i1I11i1I * oOo
  if 89 - 89: OOooOOo . iIi1i111II
 def Get_Sources ( self , URL , season_name ) :
  Oo0oO0ooo = xbmcgui . DialogProgress ( )
  oOOoO0O0O0 = OO0oOO0O ( URL )
  Ii1 = re . compile ( '<td>.+?<a href="/link/(.+?)".+?height="16px">(.+?)\n' , re . DOTALL ) . findall ( oOOoO0O0O0 )
  for IiIIIIIi , o0O0oo0OO0O in Ii1 :
   URL = 'http://www.watchseries.ac/link/' + IiIIIIIi
   self . Get_site_link ( URL , season_name )
   if 7 - 7: OoOOOOO % OOooOOo - oOo0O0Ooo + I1ii11iIi11i
 def Get_site_link ( self , url , season_name ) :
  oOOoO0O0O0 = OO0oOO0O ( url )
  Ii1 = re . compile ( '<iframe style=.+?" src="(.+?)"' ) . findall ( oOOoO0O0O0 )
  OOooOO000 = re . compile ( '<IFRAME SRC="(.+?)"' ) . findall ( oOOoO0O0O0 )
  I1iI11iii = re . compile ( '<IFRAME style=".+?" SRC="(.+?)"' ) . findall ( oOOoO0O0O0 )
  for url in Ii1 :
   self . main ( url , season_name )
  for url in OOooOO000 :
   self . main ( url , season_name )
  for url in I1iI11iii :
   self . main ( url , season_name )
   if 70 - 70: IIiIiII11i + Oo0o00 + Ii - ooOoO0O00 / i1I11i1I
 def main ( self , url , season_name ) :
  Oo0oO0ooo . create ( "[COLORwhite]Origin[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
  if 'daclips.in' in url :
   iI1IIiiIIIII = 'DACLIPS'
   if iI1IIiiIIIII in Ii1I1i1ii1I1 . source_list :
    pass
   else :
    self . daclips ( url , season_name , iI1IIiiIIIII )
    Oo0oO0ooo . update ( 0 , "" , "Getting Daclips Links" )
  else :
   if 'filehoot.com' in url :
    iI1IIiiIIIII = 'FILEHOOT'
    if iI1IIiiIIIII in Ii1I1i1ii1I1 . source_list :
     pass
    else :
     Oo0oO0ooo . update ( 0 , "" , "Getting Filehoot Links" )
     self . filehoot ( url , season_name , iI1IIiiIIIII )
   else :
    if 'thevideo.me' in url :
     iI1IIiiIIIII = 'THEVIDEO'
     if iI1IIiiIIIII in Ii1I1i1ii1I1 . source_list :
      pass
     else :
      self . thevideo ( url , season_name , iI1IIiiIIIII )
      Oo0oO0ooo . update ( 0 , "" , "Getting Thevideo Links" )
    else :
     if 'allmyvideos.net' in url :
      iI1IIiiIIIII = 'ALLMYVIDEOS'
      if iI1IIiiIIIII in Ii1I1i1ii1I1 . source_list :
       pass
      else :
       self . allmyvid ( url , season_name , iI1IIiiIIIII )
       Oo0oO0ooo . update ( 0 , "" , "Getting Allmyvideo Links" )
     else :
      if 'vidspot.net' in url :
       iI1IIiiIIIII = 'VIDSPOT'
       if iI1IIiiIIIII in Ii1I1i1ii1I1 . source_list :
        pass
       else :
        self . vidspot ( url , season_name , iI1IIiiIIIII )
        Oo0oO0ooo . update ( 0 , "" , "Getting Vidspot Links" )
      else :
       if 'vodlocker' in url :
        iI1IIiiIIIII = 'VODLOCKER'
        if iI1IIiiIIIII in Ii1I1i1ii1I1 . source_list :
         pass
        else :
         self . vodlocker ( url , season_name , iI1IIiiIIIII )
         Oo0oO0ooo . update ( 0 , "" , "Getting Vodlocker Links" )
         if 43 - 43: OO0O0OoOO0 + I1ii11iIi11i / ii
         if 24 - 24: o0o00Oo0O + I11i * I1i1III - Oo0o00
 def allmyvid ( self , url , season_name , source_name ) :
  oOOoO0O0O0 = OO0oOO0O ( url )
  Ii1 = re . compile ( '"file" : "(.+?)",\n.+?"default" : .+?,\n.+?"label" : "(.+?)"' , re . DOTALL ) . findall ( oOOoO0O0O0 )
  for iii11i1 , o0O0oo0OO0O in Ii1 :
   self . Printer ( iii11i1 , season_name , source_name )
   if 100 - 100: I1i1IiI1 % Ii * OO0O0OoOO0 / oO0o % Ii1I + iIi1i111II
 def vidspot ( self , url , season_name , source_name ) :
  oOOoO0O0O0 = OO0oOO0O ( url )
  Ii1 = re . compile ( '"file" : "(.+?)",\n.+?"default" : .+?,\n.+?"label" : "(.+?)"' ) . findall ( oOOoO0O0O0 )
  for iii11i1 , o0O0oo0OO0O in Ii1 :
   self . Printer ( iii11i1 , season_name , source_name )
   if 48 - 48: iI11I1II1I1I % ooOoO0O00 + OOooOOo % I11i
 def thevideo ( self , url , season_name , source_name ) :
  oOOoO0O0O0 = OO0oOO0O ( url )
  Ii1 = re . compile ( "{ label: '.+?', file: '(.+?)' }" ) . findall ( oOOoO0O0O0 )
  for iii11i1 in Ii1 :
   self . Printer ( iii11i1 , season_name , source_name )
   if 79 - 79: OOooOOo % oOo0O0Ooo % I1i1III / ooOoO0O00 % oO0o
 def vodlocker ( self , url , season_name , source_name ) :
  oOOoO0O0O0 = OO0oOO0O ( url )
  Ii1 = re . compile ( 'file: "(.+?)",.+?skin' , re . DOTALL ) . findall ( oOOoO0O0O0 )
  for iii11i1 in Ii1 :
   self . Printer ( iii11i1 , season_name , source_name )
   if 56 - 56: iI11I1II1I1I - Ii * OO0O0OoOO0
 def daclips ( self , url , season_name , source_name ) :
  oOOoO0O0O0 = OO0oOO0O ( url )
  Ii1 = re . compile ( '{ file: "(.+?)", type:"video" }' ) . findall ( oOOoO0O0O0 )
  for iii11i1 in Ii1 :
   self . Printer ( iii11i1 , season_name , source_name )
   if 84 - 84: iIi1i111II + I1i1III + I11i
 def filehoot ( self , url , season_name , source_name ) :
  oOOoO0O0O0 = OO0oOO0O ( url )
  Ii1 = re . compile ( 'file: "(.+?)",.+?skin' , re . DOTALL ) . findall ( oOOoO0O0O0 )
  for iii11i1 in Ii1 :
   self . Printer ( iii11i1 , season_name , source_name )
   if 33 - 33: I1i1III
 def Printer ( self , Link , season_name , source_name ) :
  if 93 - 93: oOo
  if Link in Ii1I1i1ii1I1 . List :
   pass
  elif source_name in Ii1I1i1ii1I1 . source_list :
   pass
  else :
   Ooo0OOoOoO0 ( '[COLOR' + oO0o0o0ooO0oO + ']' + source_name + '[/COLOR]' , Link , 10012 , iIIIi1 + 'WATCHSERIES.png' )
   Oo0oO0ooo . update ( 100 , "" , "Got Source" )
   Ii1I1i1ii1I1 . List . append ( Link )
   Ii1I1i1ii1I1 . source_list . append ( source_name )
   if 34 - 34: OoOOOOO - oOo * I1ii11iIi11i / I11i
   xbmcplugin . addSortMethod ( I11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
   if 19 - 19: Ii1I
   if 46 - 46: iI11I1II1I1I . Ii - OOooOOo % o0o00Oo0O / IIiIiII11i * ooOoO0O00
   if 66 - 66: o0o00Oo0O
   if 52 - 52: oO0o * ii
   if 12 - 12: o0o00Oo0O + i1I11i1I * ooOoO0O00 . oO0o
def o0OO0oooo ( ) :
 ooOOO0 ( '[COLOR' + oO0o0o0ooO0oO + ']Highlights[/COLOR]' , '' , 10008 , iIIIi1 + 'Highlights.png' , i1iIIi1 , '' )
 ooOOO0 ( '[COLOR' + oO0o0o0ooO0oO + ']Fixtures[/COLOR]' , '' , 10009 , iIIIi1 + 'Fixtures.png' , i1iIIi1 , '' )
 ooOOO0 ( '[COLOR' + oO0o0o0ooO0oO + ']Today On G-Tv[/COLOR]' , ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 7080 , iIIIi1 + 'TodaysMacthes.png' , i1iIIi1 , '' )
 ooOOO0 ( '[COLOR' + oO0o0o0ooO0oO + ']Premier League Table[/COLOR]' , 'http://www.sportinglife.com/football/premier-league/table' , 50002 , iIIIi1 + 'PremiereLeague.png' , i1iIIi1 , '' )
 if 40 - 40: Oo0o00 - OOooOOo * I1i1IiI1 - i1I11i1I / OOooOOo
def OO0oo ( url ) :
 ooOOO0 ( '[COLORwhite]                                                    pl        w        d        l        f        a        pts[/COLOR]' , '' , '' , '' , '' , '' )
 OoO000O0Oo = OO0oOO0O ( url )
 Ii1 = re . compile ( '<td>(.+?)</td>.+?<td class="ixt div"><strong><a href="([^"]*)">([^>]*)</a></strong></td>.+?<td class="div">([^>]*)</td>.+?<td>([^>]*)</td>.+?<td>([^>]*)</td>.+?<td>([^>]*)</td>.+?<td class="mobile-hdn">([^>]*)</td>.+?<td class="mobile-hdn">([^>]*)</td>.+?<td class="div">([^>]*)</td>.+?<td class="div">([^>]*)</td>' , re . DOTALL ) . findall ( OoO000O0Oo )
 for O0oOO0o , url , oo000oO0O , o0o , iIi11I11 , oOO , i1ioO , oo0OOo0 , Ii1ii111i1 , I11iiI , i1iIii1i111 in Ii1 :
  oo000oO0O = oo000oO0O
  if 'Arsenal' in oo000oO0O :
   I111i1i1111 = iIIIi1 + 'arsenal-logo.png'
   o0O0oo0OO0O = '[COLOR' + oO0o0o0ooO0oO + ']' + O0oOO0o + ' - ' + oo000oO0O + '                                  ' + o0o + '        ' + iIi11I11 + '        ' + oOO + '        ' + i1ioO + '        ' + oo0OOo0 + '        ' + Ii1ii111i1 + '        ' + I11iiI + '[/COLOR]'
  elif 'Bournemouth' in oo000oO0O :
   I111i1i1111 = iIIIi1 + 'afc-bournemouth.png'
   o0O0oo0OO0O = '[COLOR' + oO0o0o0ooO0oO + ']' + O0oOO0o + ' - ' + oo000oO0O + '                       ' + o0o + '        ' + iIi11I11 + '        ' + oOO + '        ' + i1ioO + '        ' + oo0OOo0 + '        ' + Ii1ii111i1 + '        ' + I11iiI + '[/COLOR]'
  elif 'Burnley' in oo000oO0O :
   I111i1i1111 = iIIIi1 + 'KEGnQWW.png'
   o0O0oo0OO0O = '[COLOR' + oO0o0o0ooO0oO + ']' + O0oOO0o + ' - ' + oo000oO0O + '                                   ' + o0o + '        ' + iIi11I11 + '        ' + oOO + '        ' + i1ioO + '        ' + oo0OOo0 + '        ' + Ii1ii111i1 + '        ' + I11iiI + '[/COLOR]'
  elif 'Chelsea' in oo000oO0O :
   I111i1i1111 = iIIIi1 + 'chelsea.png'
   o0O0oo0OO0O = '[COLOR' + oO0o0o0ooO0oO + ']' + O0oOO0o + ' - ' + oo000oO0O + '                                  ' + o0o + '        ' + iIi11I11 + '        ' + oOO + '        ' + i1ioO + '        ' + oo0OOo0 + '        ' + Ii1ii111i1 + '        ' + I11iiI + '[/COLOR]'
  elif 'Crystal' in oo000oO0O :
   I111i1i1111 = iIIIi1 + 'CrystalPalace.0.png'
   o0O0oo0OO0O = '[COLOR' + oO0o0o0ooO0oO + ']' + O0oOO0o + ' - ' + oo000oO0O + '                       ' + o0o + '        ' + iIi11I11 + '        ' + oOO + '        ' + i1ioO + '        ' + oo0OOo0 + '        ' + Ii1ii111i1 + '        ' + I11iiI + '[/COLOR]'
  elif 'Everton' in oo000oO0O :
   I111i1i1111 = iIIIi1 + 'Everton.png'
   o0O0oo0OO0O = '[COLOR' + oO0o0o0ooO0oO + ']' + O0oOO0o + ' - ' + oo000oO0O + '                                   ' + o0o + '        ' + iIi11I11 + '        ' + oOO + '        ' + i1ioO + '        ' + oo0OOo0 + '        ' + Ii1ii111i1 + '        ' + I11iiI + '[/COLOR]'
  elif 'Hull' in oo000oO0O :
   I111i1i1111 = iIIIi1 + 'hull-city-afc.png'
   o0O0oo0OO0O = '[COLOR' + oO0o0o0ooO0oO + ']' + O0oOO0o + ' - ' + oo000oO0O + '                                 ' + o0o + '        ' + iIi11I11 + '        ' + oOO + '        ' + i1ioO + '        ' + oo0OOo0 + '        ' + Ii1ii111i1 + '        ' + I11iiI + '[/COLOR]'
  elif 'Leicester' in oo000oO0O :
   I111i1i1111 = iIIIi1 + 'leicester-city-fc-hd-logo.png'
   o0O0oo0OO0O = '[COLOR' + oO0o0o0ooO0oO + ']' + O0oOO0o + ' - ' + oo000oO0O + '                       ' + o0o + '        ' + iIi11I11 + '        ' + oOO + '        ' + i1ioO + '        ' + oo0OOo0 + '        ' + Ii1ii111i1 + '        ' + I11iiI + '[/COLOR]'
  elif 'Liverpool' in oo000oO0O :
   I111i1i1111 = iIIIi1 + 'liverpool-logo.png'
   o0O0oo0OO0O = '[COLOR' + oO0o0o0ooO0oO + ']' + O0oOO0o + ' - ' + oo000oO0O + '                               ' + o0o + '        ' + iIi11I11 + '        ' + oOO + '        ' + i1ioO + '        ' + oo0OOo0 + '        ' + Ii1ii111i1 + '        ' + I11iiI + '[/COLOR]'
  elif 'Manchester City' in oo000oO0O :
   I111i1i1111 = iIIIi1 + 'city-logo.png'
   o0O0oo0OO0O = '[COLOR' + oO0o0o0ooO0oO + ']' + O0oOO0o + ' - ' + oo000oO0O + '               ' + o0o + '        ' + iIi11I11 + '        ' + oOO + '        ' + i1ioO + '        ' + oo0OOo0 + '        ' + Ii1ii111i1 + '        ' + I11iiI + '[/COLOR]'
  elif 'Manchester United' in oo000oO0O :
   I111i1i1111 = iIIIi1 + '91.png'
   o0O0oo0OO0O = '[COLOR' + oO0o0o0ooO0oO + ']' + O0oOO0o + ' - ' + oo000oO0O + '          ' + o0o + '        ' + iIi11I11 + '        ' + oOO + '        ' + i1ioO + '        ' + oo0OOo0 + '        ' + Ii1ii111i1 + '        ' + I11iiI + '[/COLOR]'
  elif 'Middlesbrough' in oo000oO0O :
   I111i1i1111 = iIIIi1 + 'middlesbrough-fc-hd-logo.png'
   o0O0oo0OO0O = '[COLOR' + oO0o0o0ooO0oO + ']' + O0oOO0o + ' - ' + oo000oO0O + '                 ' + o0o + '        ' + iIi11I11 + '        ' + oOO + '        ' + i1ioO + '        ' + oo0OOo0 + '        ' + Ii1ii111i1 + '        ' + I11iiI + '[/COLOR]'
  elif 'Southampton' in oo000oO0O :
   I111i1i1111 = iIIIi1 + 'southampton-fc-logo.png'
   o0O0oo0OO0O = '[COLOR' + oO0o0o0ooO0oO + ']' + O0oOO0o + ' - ' + oo000oO0O + '                   ' + o0o + '        ' + iIi11I11 + '        ' + oOO + '        ' + i1ioO + '        ' + oo0OOo0 + '        ' + Ii1ii111i1 + '        ' + I11iiI + '[/COLOR]'
  elif 'Stoke City' in oo000oO0O :
   I111i1i1111 = iIIIi1 + 'stoke-city.png'
   o0O0oo0OO0O = '[COLOR' + oO0o0o0ooO0oO + ']' + O0oOO0o + ' - ' + oo000oO0O + '                          ' + o0o + '        ' + iIi11I11 + '        ' + oOO + '        ' + i1ioO + '        ' + oo0OOo0 + '        ' + Ii1ii111i1 + '        ' + I11iiI + '[/COLOR]'
  elif 'Sunderland' in oo000oO0O :
   I111i1i1111 = iIIIi1 + 'sunderland-logo.png'
   o0O0oo0OO0O = '[COLOR' + oO0o0o0ooO0oO + ']' + O0oOO0o + ' - ' + oo000oO0O + '                        ' + o0o + '        ' + iIi11I11 + '        ' + oOO + '        ' + i1ioO + '        ' + oo0OOo0 + '        ' + Ii1ii111i1 + '        ' + I11iiI + '[/COLOR]'
  elif 'Swansea' in oo000oO0O :
   I111i1i1111 = iIIIi1 + 'swansea-city-afc.png'
   o0O0oo0OO0O = '[COLOR' + oO0o0o0ooO0oO + ']' + O0oOO0o + ' - ' + oo000oO0O + '                    ' + o0o + '        ' + iIi11I11 + '        ' + oOO + '        ' + i1ioO + '        ' + oo0OOo0 + '        ' + Ii1ii111i1 + '        ' + I11iiI + '[/COLOR]'
  elif 'Tottenham' in oo000oO0O :
   I111i1i1111 = iIIIi1 + 'tottenham-hotspur_zps4e3ed7c1.png'
   o0O0oo0OO0O = '[COLOR' + oO0o0o0ooO0oO + ']' + O0oOO0o + ' - ' + oo000oO0O + '        ' + o0o + '        ' + iIi11I11 + '        ' + oOO + '        ' + i1ioO + '        ' + oo0OOo0 + '        ' + Ii1ii111i1 + '        ' + I11iiI + '[/COLOR]'
  elif 'Watford' in oo000oO0O :
   I111i1i1111 = iIIIi1 + 'watford-fc-hd-logo.png'
   o0O0oo0OO0O = '[COLOR' + oO0o0o0ooO0oO + ']' + O0oOO0o + ' - ' + oo000oO0O + '                              ' + o0o + '        ' + iIi11I11 + '        ' + oOO + '        ' + i1ioO + '        ' + oo0OOo0 + '        ' + Ii1ii111i1 + '        ' + I11iiI + '[/COLOR]'
  elif 'Bromwich' in oo000oO0O :
   I111i1i1111 = iIIIi1 + 'west-bromwich-albion-logo.png'
   o0O0oo0OO0O = '[COLOR' + oO0o0o0ooO0oO + ']' + O0oOO0o + ' - ' + oo000oO0O + '   ' + o0o + '        ' + iIi11I11 + '        ' + oOO + '        ' + i1ioO + '        ' + oo0OOo0 + '        ' + Ii1ii111i1 + '        ' + I11iiI + '[/COLOR]'
  elif 'West Ham' in oo000oO0O :
   I111i1i1111 = iIIIi1 + 'west-ham.png'
   o0O0oo0OO0O = '[COLOR' + oO0o0o0ooO0oO + ']' + O0oOO0o + ' - ' + oo000oO0O + '             ' + o0o + '        ' + iIi11I11 + '        ' + oOO + '        ' + i1ioO + '        ' + oo0OOo0 + '        ' + Ii1ii111i1 + '        ' + I11iiI + '[/COLOR]'
  ooOOO0 ( str ( o0O0oo0OO0O ) , ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 50003 , I111i1i1111 , I111i1i1111 , oo000oO0O )
  if 65 - 65: I1ii11iIi11i * o0o00Oo0O / I1i1III . Oo0o00 % I1ii11iIi11i
def i1Ii1i1 ( description ) :
 oo000oO0O = description
 IiIIIIIi = ( 'http://www.fullmatchesandshows.com/?s=' + oo000oO0O ) . replace ( ' ' , '%20' )
 OoOo ( IiIIIIIi )
 if 33 - 33: ooOoO0O00 / Oo0o00 - ooOoO0O00 . I1ii11iIi11i
def iIIi1 ( ) :
 OoO000O0Oo = OO0oOO0O ( i1111 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20vcXVpY2tpbmRleC5odG1s' ) )
 Ii1 = re . compile ( '<a target="_self" href="(.+?)".+?src="(.+?)" alt="(.+?)"' , re . DOTALL ) . findall ( OoO000O0Oo )
 for IiIIIIIi , i11ii1ii11i , o0O0oo0OO0O in Ii1 :
  ooOOO0 ( '[COLOR' + oO0o0o0ooO0oO + ']' + ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' ) . replace ( 'amp;' , '' ) + '[/COLOR]' , i1111 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20v' ) + IiIIIIIi , 10010 , i1111 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20v' ) + i11ii1ii11i , i1iIIi1 , '' )
  if 65 - 65: ooOoO0O00 . Ii1I / oOo
def I1i1I11111iI1 ( url ) :
 oOOoO0O0O0 = OO0oOO0O ( url )
 oOoO0 = re . compile ( 'AndClearL.+?><h2.+?head>(.*?)float' , re . DOTALL ) . findall ( oOOoO0O0O0 )
 for oOoO0 in oOoO0 :
  IIIIIIi = re . compile ( '(.*?)</h2>' ) . findall ( str ( oOoO0 ) )
  for OO0oOoOoooo0O in IIIIIIi :
   OO0oOoOoooo0O = OO0oOoOoooo0O
  OoO0O = re . compile ( 'comp_head>(.*?)</span>.*?<div class = fLeft width = ".*?"><img src="(.*?)">.*?</div>.*?ST:(.*?)</div>(.+?)<!-- around all of channel types ENDS 2-->' , re . DOTALL ) . findall ( str ( oOoO0 ) )
  for Oo0oo , i11ii1ii11i , time , Oo00OOoOo in OoO0O :
   O0OoO0ooOO0o = re . compile ( ",CAPTION, '(.+?)&nbsp" ) . findall ( Oo00OOoOo )
   ooOOO0 ( '[COLOR' + oO0o0o0ooO0oO + ']' + OO0oOoOoooo0O + ' - ' + Oo0oo + ' - ' + time + '[/COLOR]' , '' , 10010 , i1111 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20=' ) + i11ii1ii11i , i1iIIi1 , ( str ( O0OoO0ooOO0o ) ) )
   if 87 - 87: ii
 IiI111111IIII ( 'tvshows' , 'Media Info 3' )
 if 64 - 64: ooOoO0O00
def I1ii1i1iiii ( ) :
 ooOOO0 ( '[COLOR' + oO0o0o0ooO0oO + ']Latest[/COLOR]' , 'http://www.fullmatchesandshows.com' , 10011 , 'http://www.fancyicons.com/free-icons/125/miscellaneous/png/256/football_256.png' , iIIIi1 + 'fanart.jpg' , '' )
 ooOOO0 ( '[COLOR' + oO0o0o0ooO0oO + ']EURO 2016[/COLOR]' , 'http://www.fullmatchesandshows.com/euro-2016/' , 10011 , 'http://football.mywapblog.com/files/uefa-euro-2016-logo.png' , iIIIi1 + 'fanart.jpg' , '' )
 ooOOO0 ( '[COLOR' + oO0o0o0ooO0oO + ']Shows[/COLOR]' , 'http://www.fullmatchesandshows.com/category/show/' , 10011 , 'http://www.fm-base.co.uk/forum/attachments/club-competition-logos/3885-soccer-am-logo-socceram.png' , iIIIi1 + 'fanart.jpg' , '' )
 ooOOO0 ( '[COLOR' + oO0o0o0ooO0oO + ']Premier League[/COLOR]' , 'http://www.fullmatchesandshows.com/premier-league/' , 10011 , 'https://footballseasons.files.wordpress.com/2013/05/premier-league.png' , iIIIi1 + 'fanart.jpg' , '' )
 ooOOO0 ( '[COLOR' + oO0o0o0ooO0oO + ']La Liga[/COLOR]' , 'http://www.fullmatchesandshows.com/la-liga/' , 10011 , 'http://1.bp.blogspot.com/-c6kQ40ryhyo/U19cUlz25sI/AAAAAAAABak/qtn5chSFZm0/s1600/la-liga-logo_display_image.png' , iIIIi1 + 'fanart.jpg' , '' )
 ooOOO0 ( '[COLOR' + oO0o0o0ooO0oO + ']Bundesliga[/COLOR]' , 'http://www.fullmatchesandshows.com/bundesliga/' , 10011 , 'http://m.img.brothersoft.com/iphone/189/518670189_icon175x175.jpg' , iIIIi1 + 'fanart.jpg' , '' )
 ooOOO0 ( '[COLOR' + oO0o0o0ooO0oO + ']Champions League[/COLOR]' , 'http://www.fullmatchesandshows.com/champions-league/' , 10011 , 'http://www.ecursuri.ro/images/teste/test-champions-league.jpg' , iIIIi1 + 'fanart.jpg' , '' )
 ooOOO0 ( '[COLOR' + oO0o0o0ooO0oO + ']Serie A[/COLOR]' , 'http://www.fullmatchesandshows.com/category/serie-a/' , 10011 , 'http://files.jcriccione.it/200000223-2484526782/serie%20a.png' , iIIIi1 + 'fanart.jpg' , '' )
 ooOOO0 ( '[COLOR' + oO0o0o0ooO0oO + ']Ligue 1[/COLOR]' , 'http://www.fullmatchesandshows.com/category/ligue-1/' , 10011 , 'http://a1.mzstatic.com/us/r30/Purple5/v4/37/c7/44/37c744ae-5824-42b7-6ce0-5f471f52baab/icon180x180.jpeg' , iIIIi1 + 'fanart.jpg' , '' )
 ooOOO0 ( '[COLOR' + oO0o0o0ooO0oO + ']Copa America 2015[/COLOR]' , 'http://www.fullmatchesandshows.com/copa-america-2015/' , 10011 , 'https://pbs.twimg.com/profile_images/521966985907691520/Nq9OAPIo_400x400.png' , iIIIi1 + 'fanart.jpg' , '' )
 ooOOO0 ( '[COLOR' + oO0o0o0ooO0oO + ']CONCACAF[/COLOR]' , 'http://www.fullmatchesandshows.com/category/concacaf/' , 10011 , 'http://a3.mzstatic.com/us/r30/Purple3/v4/40/26/14/4026147c-7022-4ca3-504e-e78950cc3f1c/icon175x175.png' , iIIIi1 + 'fanart.jpg' , '' )
 ooOOO0 ( '[COLOR' + oO0o0o0ooO0oO + ']Women World Cup[/COLOR]' , 'http://www.fullmatchesandshows.com/category/women-world-cup/' , 10011 , 'https://upload.wikimedia.org/wikipedia/en/thumb/7/76/2015_FIFA_Women\'s_World_Cup_logo.svg/967px-2015_FIFA_Women\'s_World_Cup_logo.svg.png' , iIIIi1 + 'fanart.jpg' , '' )
 if 45 - 45: I1i1III / oOo . ii + oO0o
def O00oO000Oo0 ( url ) :
 ooOOO0 ( '[COLOR' + oO0o0o0ooO0oO + ']Live On G-Tv[/COLOR]' , ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 7080 , iIIIi1 + 'TodaysMacthes.png' , i1iIIi1 , '' )
 oOOoO0O0O0 = OO0oOO0O ( url )
 Ii1 = re . compile ( 'class="entry-thumb" src="(.+?)" alt="".+?<h3 class="entry-title td-module-title"><a href="([^"]*)" rel="bookmark" title=".+?">([^>]*)</a></h3>' , re . DOTALL ) . findall ( oOOoO0O0O0 )
 OOooOO000 = re . compile ( '<div class="td-block-span6">.+?<div class="td_module_6 td_module_wrap td-animation-stack">.+?<div class="td-module-thumb"><a href="([^"]*)" rel="bookmark" title=".+?"><img width="100" height="70" class="entry-thumb" src="(.+?)" alt=".+?" title="([^"]*)"/></a></div>.+?</div>' , re . DOTALL ) . findall ( oOOoO0O0O0 )
 for i11ii1ii11i , url , o0O0oo0OO0O in Ii1 :
  iIIiiIi = o0O0oo0OO0O . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) . replace ( '&#8217;' , '' )
  if 'Highlights &' in o0O0oo0OO0O :
   pass
  else :
   iIIiiIi = o0O0oo0OO0O . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) . replace ( '&#8217;' , '' )
   Ooo0OOoOoO0 ( '[COLOR' + oO0o0o0ooO0oO + ']' + iIIiiIi + '[/COLOR]' , url , 10013 , i11ii1ii11i )
 for url , i11ii1ii11i , o0O0oo0OO0O in OOooOO000 :
  iIIiiIi = o0O0oo0OO0O . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) . replace ( '&#8217;' , '' )
  if 'Highlights &' in o0O0oo0OO0O :
   pass
  else :
   Ooo0OOoOoO0 ( '[COLOR' + oO0o0o0ooO0oO + ']' + iIIiiIi + '[/COLOR]' , url , 10013 , i11ii1ii11i )
def OoOo ( url ) :
 ooOOO0 ( '[COLOR' + oO0o0o0ooO0oO + ']Live On G-Tv[/COLOR]' , ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 7080 , iIIIi1 + 'TodaysMacthes.png' , i1iIIi1 , '' )
 oOOoO0O0O0 = OO0oOO0O ( url )
 Ii1 = re . compile ( 'class="entry-thumb" src="(.+?)" alt="".+?<h3 class="entry-title td-module-title"><a href="([^"]*)" rel="bookmark" title=".+?">([^>]*)</a></h3>' , re . DOTALL ) . findall ( oOOoO0O0O0 )
 OOooOO000 = re . compile ( '<div class="td-block-span6">.+?<div class="td_module_6 td_module_wrap td-animation-stack">.+?<div class="td-module-thumb"><a href="([^"]*)" rel="bookmark" title=".+?"><img width="100" height="70" class="entry-thumb" src="(.+?)" alt=".+?" title="([^"]*)"/></a></div>.+?</div>' , re . DOTALL ) . findall ( oOOoO0O0O0 )
 if 19 - 19: I11i
 if 73 - 73: Oo0o00 * I1ii11iIi11i * OOooOOo
 if 65 - 65: Ii + I1ii11iIi11i * ii - oO0o
 if 26 - 26: I11i % iIi1i111II + iIi1i111II % I1i1IiI1 * Ii / OO0O0OoOO0
 if 64 - 64: OoOOOOO % OOooOOo / IIiIiII11i % oOo - OO0O0OoOO0
 if 2 - 2: Oo0o00 - Ii1I + I11i * oO0o / OO0O0OoOO0
 if 26 - 26: iIi1i111II * I1ii11iIi11i
 for url , i11ii1ii11i , o0O0oo0OO0O in OOooOO000 :
  iIIiiIi = o0O0oo0OO0O . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) . replace ( '&#8217;' , '' )
  if 'Highlights &' in o0O0oo0OO0O :
   pass
  else :
   Ooo0OOoOoO0 ( '[COLOR' + oO0o0o0ooO0oO + ']' + iIIiiIi + '[/COLOR]' , url , 10013 , i11ii1ii11i )
   if 31 - 31: I1i1IiI1 * OoOOOOO . I1i1III
def i1Ii11ii1I ( url ) :
 oOOoO0O0O0 = OO0oOO0O ( url )
 Ii1 = re . compile ( '<script data-config="(.+?)" data-height' ) . findall ( oOOoO0O0O0 )
 for IIi in Ii1 :
  OO0oI1iii1i = ( IIi ) . replace ( '/v2' , '' ) . replace ( 'zeus.json' , 'video-sd.mp4?hosting_id=21772' ) . replace ( 'config.playwire.com' , 'cdn.video.playwire.com' )
  o0i1I11iI1iiI ( 'http:' + OO0oI1iii1i )
  if 91 - 91: OoOOOOO - ii * IIiIiII11i
  if 38 - 38: Ii1I + OOooOOo
  if 68 - 68: o0o00Oo0O
  if 76 - 76: Ii1I
def ooO000OO ( url ) :
 OoO000O0Oo = Oo0o0oooo0O0 ( url )
 Ii1 = re . compile ( '<a href="([^"]*)" title="([^"]*)"><img itemprop="image" content="([^"]*)"' , re . DOTALL ) . findall ( OoO000O0Oo )
 OOooOO000 = re . compile ( "<a rel='next' href=([^=]*)=" , re . DOTALL ) . findall ( OoO000O0Oo )
 for url , o0O0oo0OO0O , i11ii1ii11i in Ii1 :
  Ooo0OOoOoO0 ( o0O0oo0OO0O , url , 8046 , i11ii1ii11i )
 for url in OOooOO000 :
  iiI11ii1I1 ( 'NEXT PAGE' , ( url ) . replace ( ' class' , '' ) , 8045 , iIIIi1 + 'Next.png' )
def i111IIiIiiI1 ( url ) :
 OoO000O0Oo = Oo0o0oooo0O0 ( url )
 Ii1 = re . compile ( "__filename='([^']*)',.+?__fullimage='([^']*)',.+?__title='([^']*)'," , re . DOTALL ) . findall ( OoO000O0Oo )
 for url , i11ii1ii11i , o0O0oo0OO0O in Ii1 :
  o0i1I11iI1iiI ( 'http://bitcast-b.bitgravity.com/ndtvod/23372/ndtv/' + url )
  if 73 - 73: OoOOOOO . IIiIiII11i * OO0O0OoOO0 % OoOOOOO + OOooOOo - oO0o
def I1iIi1iIIIIiI ( url ) :
 OoO000O0Oo = Oo0o0oooo0O0 ( url )
 Ii1 = re . compile ( "src='http://www.youtube.com/embed/(.+?)?version=3&#038;rel=1&#038;fs=1&#038;autohide=2&#038;showsearch=0&#038;showinfo=1&#038;iv_load_policy=1&#038;wmode=transparent' frameborder='0' allowfullscreen='true'></iframe>" ) . findall ( OoO000O0Oo )
 for url in Ii1 :
  yt . PlayVideo ( url )
  if 94 - 94: i1I11i1I * I1i1IiI1 * ii / I11i . i1I11i1I - I11i
def I1I1i ( ) :
 OoO000O0Oo = Oo0o0oooo0O0 ( i1111 ( 'aHR0cDovL3RvcGRvY3VtZW50YXJ5ZmlsbXMuY29tLw==' ) )
 if 45 - 45: iIi1i111II
 Ii1 = re . compile ( '<a href="(.+?)" >(.+?)</a></li>' ) . findall ( OoO000O0Oo )
 if 25 - 25: iIi1i111II % o0o00Oo0O
 for IiIIIIIi , o0O0oo0OO0O in Ii1 :
  iiI11ii1I1 ( o0O0oo0OO0O , IiIIIIIi , 8041 , iIIIi1 + 'documentary.png' )
  if 44 - 44: Oo0o00 . I1i1III * IIiIiII11i / i1I11i1I + iI11I1II1I1I
  if 14 - 14: o0o00Oo0O % i1I11i1I % I1i1III * OoOOOOO
  if 65 - 65: I1i1IiI1 % OoOOOOO + Ii1I
 xbmcplugin . addSortMethod ( I11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
def Oooo ( url ) :
 OoO000O0Oo = Oo0o0oooo0O0 ( url )
 Ii1 = re . compile ( '<a href="([^"]*)" title="([^"]*)"><img width="95" height="125" src="([^"]*)"' , re . DOTALL ) . findall ( OoO000O0Oo )
 OOooOO000 = re . compile ( 'title="([^"]*)" href="([^"]*)"><img src="([^"]*)"' , re . DOTALL ) . findall ( OoO000O0Oo )
 next = re . compile ( 'class="inactive">.+?</a><a href="(.+?)">Next</a></div>' , re . DOTALL ) . findall ( OoO000O0Oo )
 for url , o0O0oo0OO0O , i11ii1ii11i in Ii1 :
  iiI11ii1I1 ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' ) . replace ( '&#039;s' , '' ) , url , 8042 , i11ii1ii11i )
 for o0O0oo0OO0O , url , i11ii1ii11i in OOooOO000 :
  iiI11ii1I1 ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' ) . replace ( '&#039;s' , '' ) , url , 8042 , i11ii1ii11i )
 for url in next :
  iiI11ii1I1 ( 'NEXT PAGE' , url , 8041 , iIIIi1 + 'Next.png' )
  if 75 - 75: iI11I1II1I1I % i1I11i1I + Ii1I * o0o00Oo0O . OO0O0OoOO0 - oOo
  if 32 - 32: I1i1III % OoOOOOO - ooOoO0O00
def Ii11III ( url ) :
 OoO000O0Oo = Oo0o0oooo0O0 ( url )
 Ii1 = re . compile ( '<meta itemprop="name" content="(.+?)".+?<meta itemprop="thumbnailUrl" content="(.+?)".+?<meta itemprop="embedUrl" content="(.+?)".+?<meta itemprop="description" content="(.+?)" />' , re . DOTALL ) . findall ( OoO000O0Oo )
 OOooOO000 = re . compile ( '<div class="video new-video"><iframe width="766" height="431" src="(.+?)&iv_load_policy=3&showinfo=0&autohide=1"' , re . DOTALL ) . findall ( OoO000O0Oo )
 for o0O0oo0OO0O , i11ii1ii11i , url , oO0Ooo0OooOOo in Ii1 :
  Ooo0OOoOoO0 ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' ) . replace ( '&#039;s' , '' ) , url . replace ( 'https://www.youtube.com/embed/videoseries?list=' , '' ) . replace ( 'https://www.youtube.com/embed/' , '' ) , 8043 , i11ii1ii11i )
 for url in OOooOO000 :
  I1Ii1i11I1I ( ( url ) . replace ( '//' , 'http://' ) )
  if 71 - 71: oOo0O0Ooo * ooOoO0O00 % I1i1IiI1
def I1Ii1i11I1I ( url ) :
 OoO000O0Oo = Oo0o0oooo0O0 ( url )
 Ii1 = re . compile ( '<link rel="canonical" href="(.+?)">  <link rel="stylesheet"' ) . findall ( OoO000O0Oo )
 for url in Ii1 :
  Ooo0OOoOoO0 ( 'PLAY' , ( url ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , iIIIi1 + 'documentary.png' )
  if 82 - 82: i1I11i1I . OOooOOo / oOo + OO0O0OoOO0 - oOo
def o00OOo0o0O ( url ) :
 OoO000O0Oo = Oo0o0oooo0O0 ( url )
 Ii1 = re . compile ( '<h1><a href="([^"]*)">(.+?)</a>.+?<img src="([^"]*)"' , re . DOTALL ) . findall ( OoO000O0Oo )
 OOooOO000 = re . compile ( 'rel="next" href="([^"]*)">»</a>' ) . findall ( OoO000O0Oo )
 for url , o0O0oo0OO0O , i11ii1ii11i in Ii1 :
  iiI11ii1I1 ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' ) . replace ( '&#038;' , 'and' ) . replace ( '&#8217;' , 'and' ) , url , 8049 , i11ii1ii11i )
 for url in OOooOO000 :
  iiI11ii1I1 ( 'NEXT' , url , 8048 , iIIIi1 + 'Next.png' )
def I111Iii1 ( url ) :
 OoO000O0Oo = Oo0o0oooo0O0 ( url )
 Ii1 = re . compile ( 'src="([^"]*)" frameborder=' ) . findall ( OoO000O0Oo )
 OOooOO000 = re . compile ( '<iframe src="([^"]*)"' ) . findall ( OoO000O0Oo )
 for url in Ii1 :
  if 'tube' in url :
   yt . PlayVideo ( ( url ) . replace ( 'http://www.youtube.com/embed/' , '' ) )
 for url in OOooOO000 :
  if 'rtd' in url :
   i11i ( url )
   if 73 - 73: oOo % oOo . OO0O0OoOO0 + Oo0o00
def i11i ( url ) :
 OoO000O0Oo = Oo0o0oooo0O0 ( url )
 Ii1 = re . compile ( "{file: '([^']*)' + '([^']*)'}" ) . findall ( OoO000O0Oo )
 for I11i1I1I , file in Ii1 :
  url = ( 'https://rtd.rt.com' + I11i1I1I + file )
  o0i1I11iI1iiI ( url )
  if 10 - 10: o0o00Oo0O / iIi1i111II * oOo - oO0o - ooOoO0O00 . OOooOOo
  if 69 - 69: I1ii11iIi11i - I1i1III % I1i1III - iIi1i111II * iIi1i111II / I1ii11iIi11i
def i1IiIIi ( ) :
 oOOoO0O0O0 = Oo0o0oooo0O0 ( 'http://www.stream2watch.co/live-tv' )
 Ii1 = re . compile ( '<a href="(.+?)">.+?<img src="(.+?)" alt=".+?"/>.+?<span class="country_name">(.+?)<br />(.+?)</span>' , re . DOTALL ) . findall ( oOOoO0O0O0 )
 for IiIIIIIi , i11ii1ii11i , o0O0oo0OO0O , OOOOo0 in Ii1 :
  iiI11ii1I1 ( ( o0O0oo0OO0O + '[COLOR' + oO0o0o0ooO0oO + ']' + OOOOo0 + '[/COLOR]' ) , IiIIIIIi , 8086 , i11ii1ii11i )
  if 80 - 80: Ii % Ii1I
def OOO00o0 ( url ) :
 oOOoO0O0O0 = Oo0o0oooo0O0 ( url )
 Ii1 = re . compile ( '<a class="front_channel_href" href="(.+?)" title=".+?">.+?<img class="front_channel_thumb" src="(.+?)" alt=".+?"/>.+?<span class="front_channel_name">(.+?)</span>' , re . DOTALL ) . findall ( oOOoO0O0O0 )
 for url , i11ii1ii11i , o0O0oo0OO0O in Ii1 :
  iiI11ii1I1 ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' , url , 8087 , i11ii1ii11i )
  if 97 - 97: Ii1I / Ii1I / iI11I1II1I1I % ooOoO0O00 . Ii1I . i1I11i1I
def IIII1ii1 ( url ) :
 oOOoO0O0O0 = OO0oOO0O ( url )
 Ii1 = re . compile ( 'a id="code_.+?data-f-href="(.+?)" data-code-embed="">(.+?)</a>' , re . DOTALL ) . findall ( oOOoO0O0O0 )
 for url , o0O0oo0OO0O in Ii1 :
  OOO0O0OOo ( url , o0O0oo0OO0O )
  if 10 - 10: ii / OO0O0OoOO0 / OoOOOOO * I1ii11iIi11i / iI11I1II1I1I
def OOO0O0OOo ( url , name ) :
 oOOoO0O0O0 = OO0oOO0O ( url )
 Ii1 = re . compile ( "playStream\('.+?', '(.+?)'\);" , re . DOTALL ) . findall ( oOOoO0O0O0 )
 for url in Ii1 :
  print url
  Ooo0OOoOoO0 ( '[COLOR' + oO0o0o0ooO0oO + ']' + name + '[/COLOR]' , url , 222 , '' )
  if 63 - 63: IIiIiII11i
def IiiI1I ( ) :
 OoO000O0Oo = Oo0o0oooo0O0 ( i1111 ( 'aHR0cDovL3d3dy5zb2xpZS5vcmcvYWxpYnJhcnkvaW5kZXguaHRtbA==' ) )
 Ii1 = re . compile ( '<td align="center" valign="top">.+?<a href="(.+?)">.+?<img src="(.+?)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( OoO000O0Oo )
 for IiIIIIIi , i11ii1ii11i , o0O0oo0OO0O in Ii1 :
  iiI11ii1I1 ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + IiIIIIIi , 3002 , 'http://www.solie.org/alibrary/' + i11ii1ii11i )
def I1iII1IIi1IiI ( url ) :
 OoO000O0Oo = Oo0o0oooo0O0 ( url )
 Ii1 = re . compile ( '<td align="center" valign="top">.+?<a href="(.+?)">.+?<img src="(.+?)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( OoO000O0Oo )
 for url , i11ii1ii11i , o0O0oo0OO0O in Ii1 :
  iiI11ii1I1 ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3003 , 'http://www.solie.org/alibrary/' + i11ii1ii11i )
def iIi ( url ) :
 OoO000O0Oo = Oo0o0oooo0O0 ( url )
 Ii1 = re . compile ( '<br><a href="([^"]*)">(.+?)</a>' ) . findall ( OoO000O0Oo )
 oo0ooO = re . compile ( 'href="([^"]*)">Season(.+?)</a>' ) . findall ( OoO000O0Oo )
 next = re . compile ( '<a href="([^"]*)">Episodes</a>' ) . findall ( OoO000O0Oo )
 OOooOO000 = re . compile ( '<td align="center" valign="top">.+?<a href="(.+?)">.+?<img src="(.+?)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( OoO000O0Oo )
 for url , o0O0oo0OO0O in Ii1 :
  Ooo0OOoOoO0 ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3004 , iIIIi1 + 'classicmovies.png' )
 for url , o0O0oo0OO0O in oo0ooO :
  iiI11ii1I1 ( '[COLOR' + oO0o0o0ooO0oO + ']Season- ' + o0O0oo0OO0O + '[/COLOR]' , 'http://www.solie.org/alibrary/' + url , 3003 , iIIIi1 + 'classicmovies.png' )
 for url in next :
  iiI11ii1I1 ( '[COLOR' + oO0o0o0ooO0oO + ']NEXT[/COLOR]' , 'http://www.solie.org/alibrary/' + url , 3003 , iIIIi1 + 'Next.png' )
 for url , i11ii1ii11i , o0O0oo0OO0O in OOooOO000 :
  iiI11ii1I1 ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3003 , 'http://www.solie.org/alibrary/' + i11ii1ii11i )
def o0ooOO00OO0o0O ( url ) :
 OoO000O0Oo = Oo0o0oooo0O0 ( url )
 Ii1 = re . compile ( '<iframe.+?src="([^"]*)"' ) . findall ( OoO000O0Oo )
 for url in Ii1 :
  III1IiiIiiI1i ( url )
def III1IiiIiiI1i ( url ) :
 OoO000O0Oo = Oo0o0oooo0O0 ( url )
 Ii1 = re . compile ( '<meta property="og:video" content="([^"]*)"/>' ) . findall ( OoO000O0Oo )
 for url in Ii1 :
  o0i1I11iI1iiI ( url )
  if 73 - 73: ooOoO0O00 % I1i1IiI1 - oOo / I11i % oO0o / Oo0o00
def O00Oo ( ) :
 OoO000O0Oo = Oo0o0oooo0O0 ( i1111 ( 'aHR0cDovL3JldHJvdmlzaW9uLnR2L2FsbC8=' ) )
 Ii1 = re . compile ( '<a href="([^"]*)"><h2><font color=".+?"><h2>(.+?)</font></h2></a>' ) . findall ( OoO000O0Oo )
 for IiIIIIIi , o0O0oo0OO0O in Ii1 :
  Ooo0OOoOoO0 ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' ) . replace ( '&#8211;' , ':' ) , IiIIIIIi , 8065 , iIIIi1 + 'classicmovies.png' )
def i1ii1II11I ( url ) :
 OoO000O0Oo = Oo0o0oooo0O0 ( url )
 Ii1 = re . compile ( "v.src = '([^']*)';" ) . findall ( OoO000O0Oo )
 for url in Ii1 :
  iII1ii1 ( url )
  if 51 - 51: I11i + i1I11i1I * oO0o % Oo0o00 - I1i1IiI1
def Oo0000OOO0 ( ) :
 OoO000O0Oo = Oo0o0oooo0O0 ( i1111 ( 'aHR0cDovL3JldHJvdmlzaW9uLnR2L2NsYXNzaWMtdHYv' ) )
 Ii1 = re . compile ( '<a href="([^"]*)"><h2><font color=".+?"><h2>(.+?)</font></h2></a>' ) . findall ( OoO000O0Oo )
 for IiIIIIIi , o0O0oo0OO0O in Ii1 :
  Ooo0OOoOoO0 ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' ) . replace ( '&#8211;' , ':' ) , IiIIIIIi , 8065 , iIIIi1 + 'classictv.png' )
def Ooo0O0OO ( url ) :
 OoO000O0Oo = Oo0o0oooo0O0 ( url )
 Ii1 = re . compile ( 'href="([^"]*)">' , re . DOTALL ) . findall ( OoO000O0Oo )
 OOooOO000 = re . compile ( "videoId: '([^']*)'" , re . DOTALL ) . findall ( OoO000O0Oo )
 for url in Ii1 :
  if 'mp4' in url :
   o0i1I11iI1iiI ( url )
 for url in OOooOO000 :
  yt . PlayVideo ( url )
  if 38 - 38: Oo0o00
def Iiiii1Iii1I ( ) :
 oOOoO0O0O0 = OO0oOO0O ( i1111 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vbTN1c3RyZWFtcw==' ) )
 Ii1 = re . compile ( '<li><a href="(.+?)"> (.+?).m3u</a></li>' ) . findall ( oOOoO0O0O0 )
 for IiIIIIIi , o0O0oo0OO0O in Ii1 :
  iiI11ii1I1 ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' ) . replace ( '-' , ' ' ) . replace ( '_' , ' ' ) , ( i1111 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vbTN1c3RyZWFtcy8=' ) ) + IiIIIIIi , 8071 , iIIIi1 + 'streams.png' )
def oOOOOoO ( url ) :
 oOOoO0O0O0 = Oo0o0oooo0O0 ( url )
 Ii1 = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( oOOoO0O0O0 )
 for o0O0oo0OO0O , url in Ii1 :
  if '(Free Access)' in o0O0oo0OO0O :
   url = ( url ) . strip ( )
  else :
   url = ( ( i1111 ( 'aHR0cDovL3BpZXN1c3R2Lm5ldDo4MDAwL2xpdmUv' ) ) + oo0o0O00 + '/' + oO + url ) . strip ( )
  Ooo0OOoOoO0 ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' ) . replace ( '_' , ' ' ) . replace ( '(Free Access)' , '[COLORwhite] - Free Access[/COLOR]' ) , url , 222 , iIIIi1 + 'streams.png' )
def IIiI ( url ) :
 oOOoO0O0O0 = Oo0o0oooo0O0 ( url )
 Ii1 = re . compile ( 'EXTINF:(.+?),(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( oOOoO0O0O0 )
 for i11ii1ii11i , o0O0oo0OO0O , url in Ii1 :
  url = ( ( i1111 ( 'aHR0cDovL3BpZXN1c3R2Lm5ldDo4MDAwL2xpdmUv' ) ) + oo0o0O00 + '/' + oO + url ) . strip ( )
  OoOO ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' ) . replace ( '_' , ' ' ) , url , 10012 , i11ii1ii11i , iIi11i1 , '' )
  if 9 - 9: iI11I1II1I1I . ii + ooOoO0O00 - I1ii11iIi11i
def i1iI ( ) :
 oooOOOoOOOo0O ( 'Best Videos' , 'http://www.xvideos.com/best' , 10105 , iIIIi1 + 'Jizbox.png' , '' , '' )
 oooOOOoOOOo0O ( 'Genres' , 'http://www.xvideos.com' , 10106 , iIIIi1 + 'Jizbox.png' , '' , '' )
 oooOOOoOOOo0O ( 'Recently Uploaded' , 'http://xvideos.com' , 10105 , iIIIi1 + 'Jizbox.png' , '' , '' )
 oooOOOoOOOo0O ( 'Tags' , 'http://www.xvideos.com/tags' , 10103 , iIIIi1 + 'Jizbox.png' , '' , '' )
 oooOOOoOOOo0O ( 'Search' , '' , 10107 , iIIIi1 + 'Jizbox.png' , '' , '' , )
 if 84 - 84: I1ii11iIi11i
def iiiiI11iiIIi ( url ) :
 oOOoO0O0O0 = OO0oOO0O ( url )
 I1i11I11Iii = re . compile ( '<li><a class=".+?".+?href="(.+?)">Next</a></li>' ) . findall ( oOOoO0O0O0 )
 for url in I1i11I11Iii :
  oooOOOoOOOo0O ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10103 , iIIIi1 + 'Jizbox.png' , '' , '' )
 Ii1 = re . compile ( '<li><a href="(.+?)"><b>(.+?)</b><span class="navbadge default"(.+?)</span>' ) . findall ( oOOoO0O0O0 )
 for url , o0O0oo0OO0O , OO0 in Ii1 :
  oooOOOoOOOo0O ( ( o0O0oo0OO0O + ' - No of Videos : ' + ( OO0 ) ) . replace ( '"></span>' , ' ' ) . replace ( '<span class="flag-small flag-' , '' ) . replace ( '>' , '' ) , 'http://www.xvideos.com' + url , 10105 , iIIIi1 + 'Jizbox.png' , '' , '' )
  if 3 - 3: I11i
def oO00OoO0oo ( url ) :
 oOOoO0O0O0 = OO0oOO0O ( url )
 I1i11I11Iii = re . compile ( 'href="([^"]*)">Next</a></li>' ) . findall ( oOOoO0O0O0 )
 for url in I1i11I11Iii :
  oooOOOoOOOo0O ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10104 , iIIIi1 + 'Next.png' , '' , '' )
 Ii1 = re . compile ( ':"([^"]*)".+?;</script></a></div></div><p class="profile-name"><a href="([^"]*)">(.+?)</a></p><p class="profile-counts">\n(.+?)\n' , re . DOTALL ) . findall ( oOOoO0O0O0 )
 for i11ii1ii11i , url , o0O0oo0OO0O , o00o0o000Oo in Ii1 :
  oooOOOoOOOo0O ( o0O0oo0OO0O + '--' + o00o0o000Oo , 'http://www.xvideos.com' + url + '#_tabVideos,videos-best' , 10105 , ( i11ii1ii11i ) . replace ( 'http:\/\/' , 'http://' ) , '' , '' )
  if 100 - 100: ooOoO0O00 - Ii . Oo0o00 * oO0o
  if 62 - 62: o0o00Oo0O
def iiIIIIiii ( url ) :
 oOOoO0O0O0 = OO0oOO0O ( url )
 Ii1 = re . compile ( '<div class="thumb"><script>.+?<img src="(.+?)".+?<a href="(.+?)" title=".+?">(.+?)</a></p>.+?uration">(.+?)</span>.+?Porn quality:(.+?)</span>' , re . DOTALL ) . findall ( oOOoO0O0O0 )
 for i11ii1ii11i , url , o0O0oo0OO0O , IiIi1iIIi1 , iiii1iii1IiiiI1i1 in Ii1 :
  oooOOOoOOOo0O ( o0O0oo0OO0O + ' - Porn Quality : ' + iiii1iii1IiiiI1i1 + ' - ' + IiIi1iIIi1 , 'http://www.xvideos.com' + url , 10108 , i11ii1ii11i , i11ii1ii11i , iiii1iii1IiiiI1i1 + ' - ' + IiIi1iIIi1 )
 IIIiI1i1 = re . compile ( '<li><a href="([^"]*)" class="no-page">Next</a></li></ul></div>' ) . findall ( oOOoO0O0O0 )
 for url in IIIiI1i1 :
  oooOOOoOOOo0O ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10105 , iIIIi1 + 'Next.png' , '' , '' )
  if 13 - 13: iIi1i111II * I1i1IiI1 / o0o00Oo0O * I11i
def Ii1iiIi11111I ( url ) :
 oOOoO0O0O0 = OO0oOO0O ( url )
 oOoO0 = re . compile ( '<div class="main-categories">(.+?)</div>' , re . DOTALL ) . findall ( oOOoO0O0O0 )
 I1i11I11Iii = re . compile ( '<li><a class=".+?".+?href="(.+?)">Next</a></li>' ) . findall ( oOOoO0O0O0 )
 for url in I1i11I11Iii :
  oooOOOoOOOo0O ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10106 , iIIIi1 + 'Next.png' , '' , '' )
 Ii1 = re . compile ( '<li><a href="(.+?)" class="btn btn-default">(.+?)</a>' ) . findall ( str ( oOoO0 ) )
 for url , o0O0oo0OO0O in Ii1 :
  oooOOOoOOOo0O ( o0O0oo0OO0O , 'http://www.xvideos.com' + url , 10105 , iIIIi1 + 'Jizbox.png' , '' , '' )
  if 72 - 72: oO0o . I11i * Ii1I . iI11I1II1I1I % Ii1I . I1i1III
  if 70 - 70: iIi1i111II + oOo * I1i1III . I1i1III + oO0o
def ii1O0Ooo0O ( ) :
 O0oOOoooOO0O = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 iii1 = ( O0oOOoooOO0O ) . replace ( ' ' , '+' ) . replace ( '&' , '&' )
 Oo0o0O00 = iii1 . lower ( )
 oOo0OoOOOo0 = 'http://www.xvideos.com/?k=' + Oo0o0O00
 print oOo0OoOOOo0 + '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'
 oOOoO0O0O0 = OO0oOO0O ( oOo0OoOOOo0 )
 Ii1 = re . compile ( '<div class="thumb-inside"><script>.+?<img src="(.+?)".+?<a href="(.+?)" title=".+?">(.+?)</a></p>.+?uration">(.+?)</span>.+?Porn quality:(.+?)</span>' , re . DOTALL ) . findall ( oOOoO0O0O0 )
 for i11ii1ii11i , IiIIIIIi , o0O0oo0OO0O , IiIi1iIIi1 , iiii1iii1IiiiI1i1 in Ii1 :
  oooOOOoOOOo0O ( o0O0oo0OO0O + ' - Porn Quality : ' + iiii1iii1IiiiI1i1 + ' - ' + IiIi1iIIi1 , 'http://www.xvideos.com' + IiIIIIIi , 10108 , i11ii1ii11i , i11ii1ii11i , iiii1iii1IiiiI1i1 + ' - ' + IiIi1iIIi1 )
 IIIiI1i1 = re . compile ( '<li><a href="([^"]*)" class="no-page">Next</a></li></ul></div>' ) . findall ( oOOoO0O0O0 )
 for IiIIIIIi in IIIiI1i1 :
  oooOOOoOOOo0O ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + IiIIIIIi , 10105 , iIIIi1 + 'Next.png' , '' , '' )
  if 55 - 55: OoOOOOO + o0o00Oo0O / OO0O0OoOO0 % oOo / ii
def O00o0OO0OO0oo ( url ) :
 oOOoO0O0O0 = OO0oOO0O ( url )
 Ii1 = re . compile ( "setVideoUrlLow.+?'([^']*)'" ) . findall ( oOOoO0O0O0 )
 OOooOO000 = re . compile ( "setVideoUrlHigh.+?'([^']*)'" ) . findall ( oOOoO0O0O0 )
 I1iI11iii = re . compile ( "setVideoHLS.+?'([^']*)'" ) . findall ( oOOoO0O0O0 )
 for url in Ii1 :
  if 'http' in url :
   Ooo0OOoOoO0 ( '[COLOR' + oO0o0o0ooO0oO + ']LOW[/COLOR]' , url , 222 , iIIIi1 + 'Jizbox.png' )
 for url in OOooOO000 :
  if 'http' in url :
   Ooo0OOoOoO0 ( '[COLOR' + oO0o0o0ooO0oO + ']HIGH[/COLOR]' , url , 222 , iIIIi1 + 'Jizbox.png' )
 for url in I1iI11iii :
  if 'http' in url :
   Ooo0OOoOoO0 ( '[COLOR' + oO0o0o0ooO0oO + ']HLS[/COLOR]' , url , 222 , iIIIi1 + 'Jizbox.png' )
   if 59 - 59: ii % I1i1IiI1 / Oo0o00 + ii . ii
def o0OoooO ( url ) :
 iiIIi = xbmc . Player ( ooOO0 ( ) )
 import urlresolver
 try : iiIIi . play ( url )
 except : pass
 if 81 - 81: Ii + I1i1III % Ii - ooOoO0O00
 if 9 - 9: OoOOOOO
def Ii1I1iIIIiiii ( ) :
 oOOoO0O0O0 = OO0oOO0O ( i1111 ( 'aHR0cDovL3d3dy5nb2Zpc2hpbmcuY28udWsvQW5nbGluZy1UaW1lcy9TZWN0aW9uL1ZpZGVvcy8=' ) )
 Ii1 = re . compile ( 'class="item.+?"><a href="(.+?)">(.+?)</a></li>' ) . findall ( oOOoO0O0O0 )
 for IiIIIIIi , o0O0oo0OO0O in Ii1 :
  iiI11ii1I1 ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' , ( 'http://www.gofishing.co.uk' + IiIIIIIi ) . replace ( 'http://www.gofishing.co.ukhttp://www.gofishing.co.uk' , 'http://www.gofishing.co.uk' ) , 8091 , iIIIi1 + 'gofish.png' )
def O0o ( url ) :
 oOOoO0O0O0 = Oo0o0oooo0O0 ( url )
 Ii1 = re . compile ( '<h2><a id=.+?href="([^"]*)">(.+?)</a></h2>' , re . DOTALL ) . findall ( oOOoO0O0O0 )
 OOooOO000 = re . compile ( '<h3><a href="([^"]*)" id=.+?>(.+?)</a> </h3>.+?<img src="([^"]*)"' , re . DOTALL ) . findall ( oOOoO0O0O0 )
 next = re . compile ( 'href="([^"]*)">next</a>&gt;</li>' , re . DOTALL ) . findall ( oOOoO0O0O0 )
 for url , o0O0oo0OO0O in Ii1 :
  Ooo0OOoOoO0 ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' , 'http://www.gofishing.co.uk/' + url , 8092 , iIIIi1 + 'gofish.png' )
 for url , o0O0oo0OO0O , i11ii1ii11i in OOooOO000 :
  Ooo0OOoOoO0 ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' , 'http://www.gofishing.co.uk/' + url , 8092 , 'http://www.gofishing.co.uk/' + i11ii1ii11i )
 for url in next :
  iiI11ii1I1 ( '[COLOR' + oO0o0o0ooO0oO + ']NEXT[/COLOR]' , url . replace ( ' ' , '+' ) , 8091 , iIIIi1 + 'Next.png' )
def Ii1iIiIi1I11 ( url ) :
 oOOoO0O0O0 = Oo0o0oooo0O0 ( url )
 Ii1 = re . compile ( 'src="https://www.youtube.com/embed/(.+?)"' ) . findall ( oOOoO0O0O0 )
 for url in Ii1 :
  yt . PlayVideo ( url )
  if 12 - 12: iI11I1II1I1I . oOo
  if 36 - 36: Oo0o00 . i1I11i1I * ii - I11i
  if 60 - 60: iIi1i111II . OO0O0OoOO0 / iI11I1II1I1I + iIi1i111II * Oo0o00
OoooO00OoO0 = '{PQ},' ; iiIiI1I1I1IiI = '{SC},' ; I1IIII11 = '{XG},' ; o0I1iI111ii111i = '{JP},' ; o00iI1Ii11iIiiI1 = '{HW},' ; i11iII11ii = '{RT},'
def oOo000O00O0 ( ) :
 Oo0oO0ooo = xbmcgui . DialogProgress ( )
 iI1iiIii1I11I = ( i1111 ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 O0oOOoooOO0O = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 Oo0o0O00 = O0oOOoooOO0O . lower ( )
 IiIIIIIi = ( i1111 ( 'aHR0cDovL2RsNC5tb3ZpZWZhcnNpLmNvbS9maWxtLzIwMTUtNy8=' ) )
 i1I1IiiIi1i = ( i1111 ( 'aHR0cDovLzUuMTM1LjIwNy45Ni9OZXclMjBSZWxlYXNlcyUyMChDcmFwJTIwQ29waWVzKS8=' ) )
 I1i1iiiI1 = ( i1111 ( 'aHR0cDovLzIxNy4yMTkuMTQzLjEwOC8xMzI3Lw==' ) )
 Ii1IiiiI1ii = ( i1111 ( 'aHR0cDovLzUuMTM1LjIwNy45Ni9OZXclMjBSZWxlYXNlcy8=' ) )
 o0oOOoo0O = ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvbW92L2FsbC5waHA=' ) )
 OoooOo00 = ( i1111 ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 OO0III = ( i1111 ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL3NlYXJjaC8/cT0=' ) ) + O0oOOoooOO0O
 OoO0o = ( i1111 ( 'aHR0cDovL3JlZGVtcHRpb25zdHJlYW1zLmNvLnVrL1JlZGVtcHRpb24vbW92aWVzL2FsbG1vdmllLnBocA==' ) )
 OO0o0O0O0O0 = ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9UaGVfUmVhcGVyL2FsbG1vdmllcy5waHA=' ) )
 iI11IiIiiII1 = ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC9tb3ZmdWxsLnBocA==' ) )
 I11iii1i = ( i1111 ( 'aHR0cDovLzUuMTM1LjIwNy45Ni9TY3JhcGVzL1NILnBocA==' ) )
 if 29 - 29: ii . IIiIiII11i % OOooOOo
 Oo0oO0ooo . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Checking Sources" , '' , 'Please Wait' )
 oOOoO0O0O0 = oo0OooOOo0 ( IiIIIIIi )
 Oo0oO0ooo . update ( 0 , "" , "Checking Source 1/9 Links" )
 Oo000o = oo0OooOOo0 ( i1I1IiiIi1i )
 Oo0oO0ooo . update ( 14 , "" , "Checking Source 2/9 Links" )
 I11IiI1I11i1i = oo0OooOOo0 ( I1i1iiiI1 )
 Oo0oO0ooo . update ( 28 , "" , "Checking Source 3/9 Links" )
 iI1ii1Ii = oo0OooOOo0 ( Ii1IiiiI1ii )
 Oo0oO0ooo . update ( 40 , "" , "Checking Source 4/9 Links" )
 IiiIi1I11 = oo0OooOOo0 ( o0oOOoo0O )
 Oo0oO0ooo . update ( 52 , "" , "Checking Source 5/9 Links" )
 i1I1Ii11II1i = oo0OooOOo0 ( OO0III )
 Oo0oO0ooo . update ( 64 , "" , "Checking Source 6/9 Links" )
 oooOoOOoOO0O = oo0OooOOo0 ( OoO0o )
 Oo0oO0ooo . update ( 76 , "" , "Checking Source 7/9 Links" )
 I11iii1I1Iiii = oo0OooOOo0 ( OO0o0O0O0O0 )
 Oo0oO0ooo . update ( 88 , "" , "Checking Source 8/9 Links" )
 IiII1 = oo0OooOOo0 ( iI11IiIiiII1 )
 Oo0oO0ooo . update ( 100 , "" , "Checking Source 9/9 Links" )
 ii111iI = oo0OooOOo0 ( I11iii1i )
 if 9 - 9: oO0o
 if 30 - 30: I11i * IIiIiII11i % o0o00Oo0O % oOo0O0Ooo * I1i1III
 if oOOoO0O0O0 != 'Failed' :
  Ii1 = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( oOOoO0O0O0 )
  for iI1i1I1 , o0O0oo0OO0O in Ii1 :
   if O0oOOoooOO0O in o0O0oo0OO0O . lower ( ) :
    Oo0oO0ooo . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Ooo0OOoOoO0 ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '- source 1[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( IiIIIIIi + iI1i1I1 ) , 222 , '' )
    Oo0oO0ooo . update ( 0 , "" , "Getting Source 1 Links" )
 if Oo000o != 'Failed' :
  OOooOO000 = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( Oo000o )
  for iI1i1I1 , o0O0oo0OO0O in OOooOO000 :
   if O0oOOoooOO0O in o0O0oo0OO0O . lower ( ) :
    Ooo0OOoOoO0 ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '- Silent Hunter Cams[/COLOR]' ) . replace ( 'mkv' , '' ) . replace ( '.' , ' ' ) , ( i1I1IiiIi1i + iI1i1I1 ) , 222 , '' )
    Oo0oO0ooo . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 9 , "" , "Getting Silent Hunter Cams Links" )
 if I11IiI1I11i1i != 'Failed' :
  I1iI11iii = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( I11IiI1I11i1i )
  for iI1i1I1 , o0O0oo0OO0O in I1iI11iii :
   if O0oOOoooOO0O in o0O0oo0OO0O . lower ( ) :
    iiI11ii1I1 ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '- source 3[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( I1i1iiiI1 + iI1i1I1 ) , 1006 , '' )
    Oo0oO0ooo . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 18 , "" , "Getting Source 3 Links" )
 if iI1ii1Ii != 'Failed' :
  iIi1Ii1111i = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( iI1ii1Ii )
  for iI1i1I1 , o0O0oo0OO0O in iIi1Ii1111i :
   if O0oOOoooOO0O in o0O0oo0OO0O . lower ( ) :
    Ooo0OOoOoO0 ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '- Silent Hunter[/COLOR]' ) . replace ( 'mkv' , '' ) . replace ( '.' , ' ' ) , IiIIIIIi , 222 , '' )
    Oo0oO0ooo . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 27 , "" , "Getting Silent Hunter Links" )
 if IiiIi1I11 != 'Failed' :
  i1iooO0oO0o = [ ]
  IIiII11 = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( IiiIi1I11 )
  for IiIIIIIi , oOOO00o000o , O00OoOO0oo0 , IIii1I1i , o0O0oo0OO0O in IIiII11 :
   if O0oOOoooOO0O in o0O0oo0OO0O . lower ( ) :
    if o0O0oo0OO0O in i1iooO0oO0o :
     pass
    else :
     ooOOO0 ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '- source Scooby[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( 'Ganool' , '' ) . replace ( 'ShAaNiG' , '' ) . replace ( 'YIFY' , '' ) . replace ( '[[ Max-Movie.In ]]' , '' ) . replace ( '.mkv' , '' ) . replace ( '.mp4' , '' ) . replace ( '.' , ' ' ) , IiIIIIIi , 1016 , oOOO00o000o , IIii1I1i , O00OoOO0oo0 )
     i1iooO0oO0o . append ( o0O0oo0OO0O )
     Oo0oO0ooo . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     Oo0oO0ooo . update ( 36 , "" , "Getting Scooby Links" )
     IiI111111IIII ( 'tvshows' , 'Media Info 3' )
 if i1I1Ii11II1i != 'Failed' :
  oo0O00OOOOO = re . compile ( 'href="(.+?)".+?src="(.+?)" alt="Image of (.+?)"' , re . DOTALL ) . findall ( i1I1Ii11II1i )
  for IiIIIIIi , i11ii1ii11i , o0O0oo0OO0O in oo0O00OOOOO :
   if O0oOOoooOO0O in o0O0oo0OO0O . lower ( ) :
    iiI11ii1I1 ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '- source Snag[/COLOR]' ) . replace ( '&#x27;' , '' ) , 'http://www.snagfilms.com' + IiIIIIIi , 7067 , i11ii1ii11i )
    Oo0oO0ooo . update ( 45 , "" , "Getting Snag Links" )
    if 53 - 53: ii . ii + I11i - OO0O0OoOO0 + iIi1i111II
    IiI111111IIII ( 'tvshows' , 'Media Info 3' )
 if oooOoOOoOO0O != 'Failed' :
  i1111iIII = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( oooOoOOoOO0O )
  for IiIIIIIi , oOOO00o000o , O00OoOO0oo0 , IIii1I1i , o0O0oo0OO0O in i1111iIII :
   if O0oOOoooOO0O in o0O0oo0OO0O . lower ( ) :
    OoOO ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '- source Redemption[/COLOR]' ) , IiIIIIIi , 222 , oOOO00o000o , IIii1I1i , O00OoOO0oo0 )
    Oo0oO0ooo . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 53 , "" , "Getting Redemption Links" )
    if 50 - 50: o0o00Oo0O * Ii1I + IIiIiII11i . ooOoO0O00 + OOooOOo
    IiI111111IIII ( 'tvshows' , 'Media Info 3' )
 if I11iii1I1Iiii != 'Failed' :
  ii11I11 = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( I11iii1I1Iiii )
  for IiIIIIIi , oOOO00o000o , O00OoOO0oo0 , IIii1I1i , o0O0oo0OO0O in ii11I11 :
   if O0oOOoooOO0O in o0O0oo0OO0O . lower ( ) :
    OoOO ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '- source Reaper[/COLOR]' ) , IiIIIIIi , 222 , oOOO00o000o , IIii1I1i , O00OoOO0oo0 )
    Oo0oO0ooo . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 61 , "" , "Getting Reaper Links" )
    if 75 - 75: I1ii11iIi11i
    IiI111111IIII ( 'tvshows' , 'Media Info 3' )
 if IiII1 != 'Failed' :
  ii11Ii1IiiI1 = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( IiII1 )
  for IiIIIIIi , oOOO00o000o , O00OoOO0oo0 , IIii1I1i , o0O0oo0OO0O in ii11Ii1IiiI1 :
   if O0oOOoooOO0O in o0O0oo0OO0O . lower ( ) :
    OoOO ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '- source Herovision[/COLOR]' ) , IiIIIIIi , 222 , oOOO00o000o , IIii1I1i , O00OoOO0oo0 )
    Oo0oO0ooo . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 70 , "" , "Getting Herovision Links" )
    if 83 - 83: oOo + ooOoO0O00 * ii * OoOOOOO
    IiI111111IIII ( 'tvshows' , 'Media Info 3' )
    if 83 - 83: iI11I1II1I1I - oOo - Oo0o00 / oO0o - o0o00Oo0O
 if ii111iI != 'Failed' :
  O00OoO0oo = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( ii111iI )
  for IiIIIIIi , oOOO00o000o , o0O0oo0OO0O in O00OoO0oo :
   if O0oOOoooOO0O in o0O0oo0OO0O . lower ( ) :
    iiI11ii1I1 ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '- source Silent Hunter[/COLOR]' ) , IiIIIIIi , 222 , oOOO00o000o )
    Oo0oO0ooo . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 78 , "" , "Getting Silent Hunter Links" )
    if 44 - 44: Ii - Oo0o00 % I1ii11iIi11i . I1i1IiI1
    IiI111111IIII ( 'tvshows' , 'Media Info 3' )
 iIIiIii11i1Ii = [ 'hey1080p' , 'hey3D' , 'hey' , '480p' , '720p' , '1080p' , 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' , '720paction' , '720padventure' , '720panimation' , '720pcomedy' , '720pcrime' , '720pdocumentary' , '720pdrama' , '720pfamily' , '720pfantasy' , '720phorror' , '720pmystery' , '720promance' , '720psci-Fi' , '720psport' , '720pthriller' , '720pwestern' , '1080paction' , '1080padventure' , '1080panimation' , '1080pcomedy' , '1080pcrime' , '1080pdocumentary' , '1080pdrama' , '1080pfamily' , '1080pfantasy' , '1080phorror' , '1080pmystery' , '1080promance' , '1080psci-Fi' , '1080psport' , '1080pthriller' , '1080pwestern' , 'top10animation' , 'top10biography' , 'top10comedy' , 'top10crime' , 'top10documentary' , 'top10drama' , 'top10family' , 'top10fantasy' , 'top10horror' , 'top10mystery' , 'top10romance' , 'top10sci-fi' , 'top10sport' , 'top10thriller' , 'top10western' ]
 if 14 - 14: I1ii11iIi11i - i1I11i1I / IIiIiII11i
 for IiiIIi1 in iIIiIii11i1Ii :
  iI1iIiiI = iiiiiIIii + IiiIIi1 + OooO0
  o00Oo0OOOoO = oo0OooOOo0 ( iI1iIiiI )
  if o00Oo0OOOoO != 'Failed' :
   o0oOO = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( o00Oo0OOOoO )
   for IiIIIIIi , oOOO00o000o , O00OoOO0oo0 , IIii1I1i , o0O0oo0OO0O in o0oOO :
    if O0oOOoooOO0O in o0O0oo0OO0O . lower ( ) :
     OoOO ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + ' - Source Pandoras[/COLOR]' , IiIIIIIi , 222 , oOOO00o000o , IIii1I1i , O00OoOO0oo0 )
     Oo0oO0ooo . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     Oo0oO0ooo . update ( 89 , "" , "Getting Pandoras Links" )
     if 84 - 84: Ii + oOo . o0o00Oo0O
     IiI111111IIII ( 'tvshows' , 'Media Info 3' )
     if 69 - 69: Oo0o00 / ii % Ii
 iIIiIii11i1Ii = [ '0-9/' , 'A/' , 'B/' , 'C/' , 'D/' , 'E/' , 'F/' , 'G/' , 'H/' , 'I/' , 'J/' , 'K/' , 'L/' , 'M/' , 'N/' , 'O/' , 'P/' , 'R/' , 'S/' , 'T/' , 'U/' , 'V/' , 'W/' , 'X/' , 'Y/' , 'Z/' ]
 if 18 - 18: Ii - oOo * OoOOOOO + I11i
 if 16 - 16: ii * Ii . ii - iI11I1II1I1I * ooOoO0O00
 for IiiIIi1 in iIIiIii11i1Ii :
  iI1iIiiI = iI1iiIii1I11I + IiiIIi1
  i1iI1IIi1I = oo0OooOOo0 ( iI1iIiiI )
  if i1iI1IIi1I != 'Failed' :
   oo00i1i11I1I1 = re . compile ( '<li><a href="(.+?)"> (.+?)</a></li>' ) . findall ( i1iI1IIi1I )
   for iI1i1I1 , o0O0oo0OO0O in oo00i1i11I1I1 :
    if O0oOOoooOO0O in o0O0oo0OO0O . lower ( ) :
     Ooo0OOoOoO0 ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + 'source 5[/COLOR]' ) . replace ( 'Ganool' , '' ) . replace ( 'ShAaNiG' , '' ) . replace ( 'YIFY' , '' ) . replace ( '[[ Max-Movie.In ]]' , '' ) . replace ( '.mkv' , '' ) . replace ( '.mp4' , '' ) . replace ( '.' , ' ' ) , ( iI1iiIii1I11I + IiiIIi1 + iI1i1I1 ) , 222 , '' )
     Oo0oO0ooo . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     Oo0oO0ooo . update ( 100 , "" , "Getting Source 5 Links" )
     if 82 - 82: oO0o - I1ii11iIi11i - o0o00Oo0O - ii
     IiI111111IIII ( 'tvshows' , 'Media Info 3' )
     if 4 - 4: IIiIiII11i - OoOOOOO % I1ii11iIi11i * Ii
     if 18 - 18: I1ii11iIi11i % o0o00Oo0O
def oooooO00OOO ( ) :
 if 53 - 53: IIiIiII11i
 O0oOOoooOO0O = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 Oo0o0O00 = O0oOOoooOO0O . lower ( )
 if 61 - 61: o0o00Oo0O * oO0o * oOo0O0Ooo % ii / OOooOOo % oOo
 IiIIIIIi = ( i1111 ( 'aHR0cDovL3d3dy53YXRjaHNlcmllcy5hYy9zZWFyY2gv' ) ) + ( O0oOOoooOO0O ) . replace ( ' ' , '%20' )
 i1I1IiiIi1i = ( i1111 ( 'aHR0cDovL3JlZGVtcHRpb25zdHJlYW1zLmNvLnVrL1JlZGVtcHRpb24vdHZzaG93cy90dm1haW4ucGhw' ) )
 I1i1iiiI1 = ( i1111 ( 'aHR0cDovL3R2LmRsLXBhcnMuaW4v' ) )
 Ii1IiiiI1ii = ( i1111 ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9BbWVyaWNhbiUyMFNlcmlhbC8=' ) )
 o0oOOoo0O = ( i1111 ( 'aHR0cDovL2RpemlsYWIuY29tL2Fyc2l2P2xpbWl0PSZ0dXI9Jm9yZGVyYnk9JnVsa2U9Jm9yZGVyPSZ5aWw9JmRpemlfYWRpPQ==' ) ) + ( Oo0o0O00 ) . replace ( ' ' , '+' )
 OoooOo00 = ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvc2hvd3MvdHZhbGwucGhw' ) )
 OO0III = ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9UaGVfUmVhcGVyL2FsbHR2LnBocA==' ) )
 OoO0o = ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC90dmZ1bGwucGhw' ) )
 if 43 - 43: ii
 Oo0oO0ooo . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Checking Sources" , '' , 'Please Wait' )
 if 33 - 33: IIiIiII11i - i1I11i1I - oOo
 Oo0oO0ooo . update ( 0 , "" , "Checking Source 1/9 Links" )
 oOOoO0O0O0 = oo0OooOOo0 ( IiIIIIIi )
 Oo0oO0ooo . update ( 14 , "" , "Checking Source 2/9 Links" )
 Oo000o = oo0OooOOo0 ( i1I1IiiIi1i )
 Oo0oO0ooo . update ( 28 , "" , "Checking Source 3/9 Links" )
 I11IiI1I11i1i = oo0OooOOo0 ( I1i1iiiI1 )
 Oo0oO0ooo . update ( 40 , "" , "Checking Source 4/9 Links" )
 iI1ii1Ii = oo0OooOOo0 ( Ii1IiiiI1ii )
 Oo0oO0ooo . update ( 52 , "" , "Checking Source 5/9 Links" )
 IiiIi1I11 = cloudflare . source ( o0oOOoo0O )
 Oo0oO0ooo . update ( 64 , "" , "Checking Source 6/9 Links" )
 i1iI1IIi1I = oo0OooOOo0 ( OoooOo00 )
 Oo0oO0ooo . update ( 76 , "" , "Checking Source 7/9 Links" )
 i1I1Ii11II1i = oo0OooOOo0 ( OO0III )
 Oo0oO0ooo . update ( 88 , "" , "Checking Source 8/9 Links" )
 oooOoOOoOO0O = oo0OooOOo0 ( OoO0o )
 Oo0oO0ooo . update ( 100 , "" , "Checking Source 9/9 Links" )
 if 92 - 92: oO0o * i1I11i1I
 if oooOoOOoOO0O != 'Failed' :
  i1111iIII = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( oooOoOOoOO0O )
  for IiIIIIIi , oOOO00o000o , O00OoOO0oo0 , IIii1I1i , o0O0oo0OO0O in i1111iIII :
   if Oo0o0O00 in o0O0oo0OO0O . lower ( ) :
    ooOOO0 ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '- source HeroVision[/COLOR]' ) , IiIIIIIi , 1016 , oOOO00o000o , IIii1I1i , O00OoOO0oo0 )
    Oo0oO0ooo . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 10 , "" , "Getting Herovision Links" )
    if 92 - 92: OoOOOOO
    IiI111111IIII ( 'tvshows' , 'Media Info 3' )
    if 7 - 7: OO0O0OoOO0
 if i1I1Ii11II1i != 'Failed' :
  oo0O00OOOOO = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( i1I1Ii11II1i )
  for IiIIIIIi , oOOO00o000o , O00OoOO0oo0 , IIii1I1i , o0O0oo0OO0O in oo0O00OOOOO :
   if Oo0o0O00 in o0O0oo0OO0O . lower ( ) :
    ooOOO0 ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '- source Reaper[/COLOR]' ) , IiIIIIIi , 1016 , oOOO00o000o , IIii1I1i , O00OoOO0oo0 )
    Oo0oO0ooo . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 20 , "" , "Getting Reaper Links" )
    if 73 - 73: oO0o % Ii1I
    IiI111111IIII ( 'tvshows' , 'Media Info 3' )
    if 32 - 32: iIi1i111II + OO0O0OoOO0 + iI11I1II1I1I * I1ii11iIi11i
    if 62 - 62: Ii
    if 2 - 2: oOo0O0Ooo
    if 69 - 69: ii / I1ii11iIi11i * Oo0o00
    if 99 - 99: IIiIiII11i * iI11I1II1I1I % o0o00Oo0O * OoOOOOO / IIiIiII11i % ii
    if 14 - 14: i1I11i1I . i1I11i1I % oOo
    Oo0oO0ooo . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 30 , "" , "Getting CoolSeries Links" )
    if 42 - 42: I11i . iIi1i111II - oOo
    IiI111111IIII ( 'tvshows' , 'Media Info 3' )
 if oOOoO0O0O0 != 'Failed' :
  Ii1 = re . compile ( '<img src="(.+?)".+?<a href="(.+?)" title=".+?"><b>(.+?)</b>' , re . DOTALL ) . findall ( oOOoO0O0O0 )
  for i11ii1ii11i , IiIIIIIi , o0O0oo0OO0O in Ii1 :
   if Oo0o0O00 in o0O0oo0OO0O . lower ( ) :
    ooOOO0 ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + ' - WatchSeries[/COLOR]' , 'http://www.watchseries.ac' + IiIIIIIi , 10044 , i11ii1ii11i , '' , '' )
    Oo0oO0ooo . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 40 , "" , "Getting Source WatchSeries Links" )
    if 33 - 33: IIiIiII11i / o0o00Oo0O / i1I11i1I - I1i1IiI1 - ooOoO0O00
    IiI111111IIII ( 'tvshows' , 'Media Info 3' )
    if 8 - 8: Ii . OO0O0OoOO0 / iI11I1II1I1I / Ii1I / i1I11i1I - I1i1III
    if 32 - 32: I11i . ooOoO0O00 * I1ii11iIi11i
    if 98 - 98: I1i1III - IIiIiII11i / oOo0O0Ooo . OoOOOOO * i1I11i1I . I1i1IiI1
    if 25 - 25: Ii / OOooOOo - Oo0o00 / oO0o . I11i . I11i
    if 6 - 6: OoOOOOO . I1i1IiI1
    if 43 - 43: Ii1I + I11i
    if 50 - 50: OoOOOOO % ooOoO0O00 * o0o00Oo0O
    if 4 - 4: iI11I1II1I1I . ooOoO0O00
    if 63 - 63: iI11I1II1I1I + i1I11i1I % ooOoO0O00 / oOo0O0Ooo % IIiIiII11i
    if 60 - 60: I11i . OOooOOo % Oo0o00 / oOo0O0Ooo / o0o00Oo0O
 if Oo000o != 'Failed' :
  OOooOO000 = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( Oo000o )
  for IiIIIIIi , oOOO00o000o , O00OoOO0oo0 , IIii1I1i , o0O0oo0OO0O in OOooOO000 :
   if Oo0o0O00 in o0O0oo0OO0O . lower ( ) :
    iiI11ii1I1 ( ( o0O0oo0OO0O + '[COLORblue] - source Redemption[/COLOR]' ) . replace ( '..&gt;' , '' ) , IiIIIIIi , 1016 , '' )
    Oo0oO0ooo . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 50 , "" , "Getting Redemption Links" )
    if 19 - 19: Ii . oOo0O0Ooo + IIiIiII11i / iIi1i111II . Ii1I * oOo
    IiI111111IIII ( 'tvshows' , 'Media Info 3' )
 if I11IiI1I11i1i != 'Failed' :
  I1iI11iii = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( I11IiI1I11i1i )
  for o0O0oo0OO0O in I1iI11iii :
   if Oo0o0O00 in o0O0oo0OO0O . lower ( ) :
    iiI11ii1I1 ( ( o0O0oo0OO0O + ' source 3' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( I1i1iiiI1 + o0O0oo0OO0O ) . replace ( ' ' , '%20' ) , 1006 , '' )
    Oo0oO0ooo . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 60 , "" , "Getting Source 3 Links" )
    if 59 - 59: iI11I1II1I1I / Ii1I % oOo
    IiI111111IIII ( 'tvshows' , 'Media Info 3' )
 if iI1ii1Ii != 'Failed' :
  iIi1Ii1111i = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( iI1ii1Ii )
  for o0O0oo0OO0O in iIi1Ii1111i :
   if Oo0o0O00 in o0O0oo0OO0O . lower ( ) :
    iiI11ii1I1 ( ( o0O0oo0OO0O + ' source 4' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( Ii1IiiiI1ii + o0O0oo0OO0O ) . replace ( ' ' , '%20' ) , 1006 , '' )
    Oo0oO0ooo . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 70 , "" , "Getting Source 4 Links" )
    if 84 - 84: iI11I1II1I1I / oOo0O0Ooo . OOooOOo % I1i1IiI1
    IiI111111IIII ( 'tvshows' , 'Media Info 3' )
 if IiiIi1I11 != 'Failed' :
  IIiII11 = re . compile ( '<a href="(.+?)" class="film-image">\n<img src="(.+?)" alt=""/>\n</a>\n<div class="tss-detail">\n<a class="title" style="" href=".+?">\n<span class="position">.+?</span>\n(.+?)</a>' ) . findall ( IiiIi1I11 )
  for IiIIIIIi , i11ii1ii11i , o0O0oo0OO0O in IIiII11 :
   if Oo0o0O00 in o0O0oo0OO0O . lower ( ) :
    iiI11ii1I1 ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + ' - Source - Dizi[/COLOR]' , IiIIIIIi , 8062 , i11ii1ii11i )
    Oo0oO0ooo . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 80 , "" , "Getting Dizi Links" )
    if 99 - 99: I1ii11iIi11i + Ii
    IiI111111IIII ( 'tvshows' , 'Media Info 3' )
 if i1iI1IIi1I != 'Failed' :
  oo00i1i11I1I1 = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( i1iI1IIi1I )
  for IiIIIIIi , oOOO00o000o , O00OoOO0oo0 , IIii1I1i , o0O0oo0OO0O in oo00i1i11I1I1 :
   if Oo0o0O00 in o0O0oo0OO0O . lower ( ) :
    ooOOO0 ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '- Source Scooby[/COLOR]' ) , IiIIIIIi , 1016 , oOOO00o000o , IIii1I1i , O00OoOO0oo0 )
    Oo0oO0ooo . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 90 , "" , "Getting Scooby Links" )
    if 36 - 36: I1i1III * Oo0o00 * iI11I1II1I1I - I1i1IiI1 % Ii
    IiI111111IIII ( 'tvshows' , 'Media Info 3' )
    if 98 - 98: iI11I1II1I1I - ooOoO0O00 + oOo % I1i1IiI1 + oOo / OoOOOOO
 O0O0Oo00OO = [ 'a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' , 'p' , 'q' , 'r' , 's' , 't' , 'u' , 'v' , 'w' , 'x' , 'y' , 'z' ]
 if i1iI1IIi1I != 'Failed' :
  for IiiIIi1 in O0O0Oo00OO :
   iI1iIiiI = iiiiiIIii + IiiIIi1 + OooO0
   IiII1 = OO0oOO0O ( iI1iIiiI )
   if IiII1 != 'Failed' :
    ii11Ii1IiiI1 = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( IiII1 )
    for o0O0oo0OO0O , O00OoOO0oo0 , IiIIIIIi , i11ii1ii11i , iIi11i1 , OooooO in ii11Ii1IiiI1 :
     if Oo0o0O00 in o0O0oo0OO0O . lower ( ) :
      ooOOO0 ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + ' - Source Pandoras[/COLOR]' , IiIIIIIi , OooooO , i11ii1ii11i , iIi11i1 , O00OoOO0oo0 )
      Oo0oO0ooo . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
      Oo0oO0ooo . update ( 100 , "" , "Getting Pandoras Links" )
      if 100 - 100: I11i . oOo0O0Ooo
      IiI111111IIII ( 'tvshows' , 'Media Info 3' )
      if 62 - 62: oOo + IIiIiII11i % oOo
      if 50 - 50: ii + OoOOOOO * oOo0O0Ooo - I1i1III / Ii
 xbmcplugin . addSortMethod ( I11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
def iiiIIiiIi ( ) :
 if 86 - 86: ii % IIiIiII11i . ii * Ii1I
 O0oOOoooOO0O = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 Oo0o0O00 = O0oOOoooOO0O . lower ( )
 IiIIIIIi = ( i1111 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz' ) )
 oOOoO0O0O0 = OO0oOO0O ( IiIIIIIi )
 Ii1 = re . compile ( '"id":".+?","name":"(.+?)","img":"(.+?)","stream_url3":".+?","cat_id":"(.+?)","stream_url2":".+?","stream_url":".+?"}' , re . DOTALL ) . findall ( oOOoO0O0O0 )
 for o0O0oo0OO0O , i11ii1ii11i , iI1II1i in Ii1 :
  iI1iI = i1111 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv' ) + ( i11ii1ii11i ) . replace ( '\\' , '' )
  if O0oOOoooOO0O in o0O0oo0OO0O . lower ( ) :
   iiI11ii1I1 ( o0O0oo0OO0O , '' , 7022 , iI1iI )
   if 69 - 69: Ii1I . oOo0O0Ooo
 xbmcplugin . addSortMethod ( I11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
III1IiIi1 = '{ZH},' ; oOOoO0O = '{IX},' ; OoOoO = '{LM},'
if 57 - 57: I1ii11iIi11i % oO0o
def IIii1IIiiIii ( url ) :
 Oooo0Oo00o = cloudflare . source ( url )
 Ii1 = re . compile ( '<a class="season" href="(.+?)">\n(.+?)\n</a>\n</span>\n<span>\n<a class="episode" href=".+?">\n(.+?)\n</a>\n</span>\n<span>\n<a class="episode-name" href=".+?">\n(.+?)</a>' ) . findall ( Oooo0Oo00o )
 for url , O0OOOOo0 , iiOO0O0Ooo , o0O0oo0OO0O in Ii1 :
  iiI11ii1I1 ( ( O0OOOOo0 ) . replace ( 'Sezon' , ' Season ' ) + ( iiOO0O0Ooo ) . replace ( 'Bölüm' , ' Episode ' ) + o0O0oo0OO0O , url , 8063 , '' )
  if 32 - 32: OOooOOo . iI11I1II1I1I % OoOOOOO . o0o00Oo0O . OOooOOo / OO0O0OoOO0
  if 45 - 45: iI11I1II1I1I
  if 41 - 41: OO0O0OoOO0 % OO0O0OoOO0 - i1I11i1I % oO0o - ii - OO0O0OoOO0
  if 66 - 66: I11i % OOooOOo
def II1I1iIIiIIii ( url ) :
 Oooo0Oo00o = cloudflare . source ( url )
 Ii1 = re . compile ( 'file: "(.+?)",.+?label: "(.+?)",' , re . DOTALL ) . findall ( Oooo0Oo00o )
 for url , o0O0oo0OO0O in Ii1 :
  Ooo0OOoOoO0 ( o0O0oo0OO0O , url , 222 , '' )
  if 65 - 65: Ii - oOo * I1i1IiI1 + oOo / i1I11i1I + I11i
  if 35 - 35: o0o00Oo0O + I1ii11iIi11i - oOo0O0Ooo % I1i1III % IIiIiII11i
  if 77 - 77: Oo0o00 + OoOOOOO
  if 38 - 38: Ii1I - I1i1III * I11i
def iIIIi1iii1I11 ( ) :
 if 81 - 81: i1I11i1I / i1I11i1I / oO0o % OoOOOOO . iI11I1II1I1I
 Oooo0Oo00o = cloudflare . source ( i1111 ( 'aHR0cDovL2RpemlsYWIuY29t' ) )
 Ii1 = re . compile ( '<li id=".+?">.+?<a href="(.+?)">.+?<img width="40" height="40" src="(.+?)" alt=""/>.+?<span class="title">\n(.+?)</span>.+?<span class="alt-title">\n(.+?)</span>.+?</a>.+?</li>' , re . DOTALL ) . findall ( Oooo0Oo00o )
 for IiIIIIIi , i11ii1ii11i , o0O0oo0OO0O , iiOO0O0Ooo in Ii1 :
  iiI11ii1I1 ( o0O0oo0OO0O + '  -  ' + ( iiOO0O0Ooo ) . replace ( 'sezon' , 'Season' ) . replace ( 'bölüm' , 'Episode' ) , IiIIIIIi , 8063 , i11ii1ii11i )
  if 85 - 85: I1i1III
def Oo0O0OooOooo0 ( ) :
 OoO000O0Oo = Oo0o0oooo0O0 ( i1111 ( 'aHR0cDovL3d3dy50dmd1aWRlLmNvLnVrLw==' ) )
 Ii1 = re . compile ( '<a href="(.+?)"  qt-title=".+?" qt-text=".+?<br> .+?" title="(.+?)".+?class=".+? src="(.+?)" alt=".+?" /></a>' , re . DOTALL ) . findall ( OoO000O0Oo )
 for IiIIIIIi , o0O0oo0OO0O , i11ii1ii11i in Ii1 :
  Ooo0OOoOoO0 ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' , IiIIIIIi , 8002 , i11ii1ii11i )
def oO0o00OO ( url ) :
 OoO000O0Oo = Oo0o0oooo0O0 ( url )
 Ii1 = re . compile ( '<table border="0".+?url((.+?));background-repeat: no-repeat;">.+?<tr>.+?<span class="season">(.+?)</span><br>.+?<a href="(.+?)"+?>(.+?)</span><br>.+?<span class="programmetext">(.+?)</span></a><br>' , re . DOTALL ) . findall ( OoO000O0Oo )
 for i11ii1ii11i , time , url , o0O0oo0OO0O , oO0Ooo0OooOOo in Ii1 :
  ooOOO0 ( '%s %s' % ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' , time ) , url , 1015 , i11ii1ii11i , oO0Ooo0OooOOo )
  if 55 - 55: ii
def OO0OOOOOo ( ) :
 if 7 - 7: o0o00Oo0O + I1i1III . IIiIiII11i
 iiI11ii1I1 ( 'Coronation Street' , '' , 8001 , '' )
 iiI11ii1I1 ( 'Eastenders' , '' , 8002 , '' )
 iiI11ii1I1 ( 'Emmerdale' , '' , 8003 , '' )
 iiI11ii1I1 ( 'Hollyoaks' , '' , 8004 , '' )
 iiI11ii1I1 ( 'Im a Celebrity' , '' , 8005 , '' )
 if 12 - 12: oOo0O0Ooo - ooOoO0O00
 if 95 - 95: I1i1IiI1 / i1I11i1I . o0o00Oo0O * i1I11i1I - I11i * I1ii11iIi11i
 if 6 - 6: OOooOOo . IIiIiII11i * oOo0O0Ooo . oOo0O0Ooo / I1i1III
 if 14 - 14: Oo0o00 % i1I11i1I - o0o00Oo0O / Oo0o00
def Oo00OOoO0oo ( ) :
 oOOoO0O0O0 = OO0oOO0O ( 'http://uksoapshare.blogspot.co.uk/' )
 Ii1 = re . compile ( '<a href="(.+?)".+?target=_blank>(.+?)</a>' ) . findall ( oOOoO0O0O0 )
 for IiIIIIIi , o0O0oo0OO0O in Ii1 :
  if 'Holly' in o0O0oo0OO0O :
   i11ii1ii11i = 'http://2.bp.blogspot.com/-9c7Sieh1RKs/UjD6TGAEEnI/AAAAAAAAAC8/84uwHfxcuYg/s1600/Hollyoaks.png'
   if 'huge' in IiIIIIIi :
    Ooo0OOoOoO0 ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , IiIIIIIi . replace ( '\\/' , '/' ) , 8006 , i11ii1ii11i )
   else :
    pass
    if 4 - 4: oO0o - OO0O0OoOO0 / Ii * o0o00Oo0O
 xbmcplugin . addSortMethod ( I11i1 , xbmcplugin . SORT_METHOD_TITLE_IGNORE_THE ) ;
 if 78 - 78: i1I11i1I - I1i1IiI1 % o0o00Oo0O - iIi1i111II % oO0o
def i11IiIi ( ) :
 oOOoO0O0O0 = OO0oOO0O ( 'http://uksoapshare.blogspot.co.uk/' )
 Ii1 = re . compile ( '<a href="(.+?)".+?target=_blank>(.+?)</a>' ) . findall ( oOOoO0O0O0 )
 for IiIIIIIi , o0O0oo0OO0O in Ii1 :
  if 'East' in o0O0oo0OO0O :
   i11ii1ii11i = 'http://3.bp.blogspot.com/-KWHcNbNJU8Y/Vi1ousRl7fI/AAAAAAAAAT8/ksNE12LH0nE/s1600/eastenders.jpg'
   if 'huge' in IiIIIIIi :
    Ooo0OOoOoO0 ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , IiIIIIIi . replace ( '\\/' , '/' ) , 8006 , i11ii1ii11i )
   else :
    pass
    if 24 - 24: I1i1IiI1 / I1i1III * oOo - Ii
 xbmcplugin . addSortMethod ( I11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 72 - 72: iI11I1II1I1I . Ii / iIi1i111II + IIiIiII11i / OoOOOOO
def iioO0o000oOO ( ) :
 oOOoO0O0O0 = OO0oOO0O ( 'http://uksoapshare.blogspot.co.uk/' )
 Ii1 = re . compile ( '<a href="(.+?)".+?target=_blank>(.+?)</a>' ) . findall ( oOOoO0O0O0 )
 for IiIIIIIi , o0O0oo0OO0O in Ii1 :
  if 'Emmer' in o0O0oo0OO0O :
   i11ii1ii11i = 'http://2.bp.blogspot.com/-UfDcxisVV5c/UjH9vUicZ3I/AAAAAAAAADc/8Ozuiz1ojxw/s1600/Emmerdale.jpg'
   if 'huge' in IiIIIIIi :
    Ooo0OOoOoO0 ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , IiIIIIIi . replace ( '\\/' , '/' ) , 8006 , i11ii1ii11i )
   else :
    pass
    if 27 - 27: o0o00Oo0O - I1i1IiI1 * IIiIiII11i - iI11I1II1I1I / oOo
 xbmcplugin . addSortMethod ( I11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 24 - 24: I1ii11iIi11i / iI11I1II1I1I % iIi1i111II * OOooOOo - iI11I1II1I1I
def iI1ii ( ) :
 oOOoO0O0O0 = OO0oOO0O ( 'http://uksoapshare.blogspot.co.uk/' )
 Ii1 = re . compile ( '<a href="(.+?)".+?target=_blank>(.+?)</a>' ) . findall ( oOOoO0O0O0 )
 for IiIIIIIi , o0O0oo0OO0O in Ii1 :
  if 'Coro' in o0O0oo0OO0O :
   i11ii1ii11i = 'http://3.bp.blogspot.com/-hofvfBQVexs/UjErIfNdS4I/AAAAAAAAADQ/Q-vVGu3apYU/s1600/corrie.jpg'
   if 'huge' in IiIIIIIi :
    Ooo0OOoOoO0 ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , IiIIIIIi . replace ( '\\/' , '/' ) , 8006 , i11ii1ii11i )
   else :
    pass
    if 61 - 61: I1ii11iIi11i * ooOoO0O00 . ii
 xbmcplugin . addSortMethod ( I11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 44 - 44: oOo0O0Ooo
def oOO0O0O0OO00oo ( ) :
 oOOoO0O0O0 = OO0oOO0O ( 'http://uksoapshare.blogspot.co.uk/' )
 Ii1 = re . compile ( '<a href="(.+?)" target="_blank">(.+?)</a>' ) . findall ( oOOoO0O0O0 )
 for IiIIIIIi , o0O0oo0OO0O in Ii1 :
  if 'Celeb' in o0O0oo0OO0O :
   i11ii1ii11i = 'http://3.bp.blogspot.com/-a_yDotWU_pY/VkotKWaG_gI/AAAAAAAAAUk/8Q5iNM6p37k/s1600/iacgoh.jpg'
   if 'huge' in IiIIIIIi :
    Ooo0OOoOoO0 ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , IiIIIIIi . replace ( '\\/' , '/' ) , 8006 , i11ii1ii11i )
   else :
    pass
    if 39 - 39: i1I11i1I % OOooOOo * Ii1I - ii - I1ii11iIi11i
def Oo0oOOO ( name , url ) :
 o00OoOooo = urlresolver . HostedMediaFile ( url ) . valid_url ( )
 if o00OoOooo :
  i1I1ii1 = urlresolver . HostedMediaFile ( url ) . resolve ( )
 else :
  OoO000O0Oo = open_url ( url )
  url = re . compile ( 'src="(.+?)"></iframe>' ) . findall ( OoO000O0Oo ) [ 0 ]
  url = url . split ( '?autoplay' ) [ 0 ]
  OoO000O0Oo = open_url ( url )
  Iii1i = re . compile ( 'mp4","url":"(.+?)"' ) . findall ( OoO000O0Oo ) [ - 1 ]
  i1I1ii1 = Iii1i . replace ( '\\/' , '/' )
 IIIIII111Ii = xbmcgui . ListItem ( name , '' , '' )
 IIIIII111Ii . setPath ( i1I1ii1 )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , IIIIII111Ii )
 if 87 - 87: OoOOOOO
 if 15 - 15: iI11I1II1I1I . iIi1i111II . Ii1I * Ii
def ooo00O0OOo ( ) :
 OoO000O0Oo = OO0oOO0O ( i1111 ( 'aHR0cDovL3d3dy5kaXppYm94aGQuY29tLw==' ) )
 Ii1 = re . compile ( 'class="film menu-item menu-item-type-post_type menu-item-object-page menu-item-36980"><a href="(.+?)"><i class="fa fa-film"></i><span>(.+?)</span></a></li>' ) . findall ( OoO000O0Oo )
 OOooOO000 = re . compile ( 'class="menu-item menu-item-type-post_type menu-item-object-page menu-item-52949"><a href="(.+?)"><i class="fa fa-"></i><span>(.+?)</span></a></li>' ) . findall ( OoO000O0Oo )
 for IiIIIIIi , o0O0oo0OO0O in Ii1 :
  iiI11ii1I1 ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' ) . replace ( 'Diziler' , 'Series' ) , IiIIIIIi , 7071 , iIIIi1 + 'popcorn.png' )
 for IiIIIIIi , o0O0oo0OO0O in OOooOO000 :
  iiI11ii1I1 ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' ) . replace ( 'Filmler' , 'Movies' ) , IiIIIIIi , 7071 , iIIIi1 + 'popcorn.png' )
  if 45 - 45: oOo0O0Ooo / OO0O0OoOO0 + OoOOOOO + i1I11i1I
def iIIII1Iii11 ( ) :
 OoO000O0Oo = OO0oOO0O ( i1111 ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL2NhdGVnb3JpZXMv' ) )
 Ii1 = re . compile ( '<a class="nav-item" href="(.+?)">(.+?)</a>' ) . findall ( OoO000O0Oo )
 for IiIIIIIi , o0O0oo0OO0O in Ii1 :
  if 'Movies' in o0O0oo0OO0O :
   iiI11ii1I1 ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' , 'http://www.snagfilms.com' + ( IiIIIIIi ) . replace ( 'http://www.snagfilms.com' , '' ) , 7061 , iIIIi1 + 'popcorn.png' )
def II1IIIi1i1I ( url ) :
 OoO000O0Oo = OO0oOO0O ( url )
 Ii1 = re . compile ( '<a class="object-link size-poster".+?href="(.+?)" data-type="category">.+?src="(.+?)" alt="Image of (.+?)" />' , re . DOTALL ) . findall ( OoO000O0Oo )
 Ii1 = re . compile ( '<a class="object-link size-poster".+?href="(.+?)" data-type="category">.+?src="(.+?)" alt="Image of (.+?)" />' , re . DOTALL ) . findall ( OoO000O0Oo )
 OOooOO000 = re . compile ( "<li class='current'>.+?</li><li ><a href='(.+?)'>.+?</a></li><li" , re . DOTALL ) . findall ( OoO000O0Oo )
 for url , i11ii1ii11i , o0O0oo0OO0O in Ii1 :
  iiI11ii1I1 ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7067 , i11ii1ii11i )
 for url in OOooOO000 :
  iiI11ii1I1 ( '[COLOR' + oO0o0o0ooO0oO + ']NEXT PAGE[/COLOR]' , ( url ) . replace ( '&#038;' , '&' ) , 7063 , iIIIi1 + 'Next.png' )
  if 100 - 100: o0o00Oo0O
  if 94 - 94: Ii1I - I11i
def IIiIIIi1iii1 ( url ) :
 OoO000O0Oo = OO0oOO0O ( i1111 ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL2NhdGVnb3JpZXMv' ) )
 Ii1 = re . compile ( 'data-title="([^"]*)".+?href="([^"]*)".+?src="([^"]*)" alt="Image' , re . DOTALL ) . findall ( OoO000O0Oo )
 for o0O0oo0OO0O , url , i11ii1ii11i in Ii1 :
  if '{{' in o0O0oo0OO0O :
   pass
  else :
   iiI11ii1I1 ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7062 , i11ii1ii11i )
 xbmcplugin . addSortMethod ( I11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
iii11III1I = '{UJ},' ; oO0oO0O = '{WE},' ; ooooO = '{WP},' ; O000oooO0 = '{PP},'
def oOO00 ( url ) :
 OoO000O0Oo = OO0oOO0O ( url )
 Ii1 = re . compile ( 'data-title="([^"]*)".+?href="([^"]*)".+?src="([^"]*)" alt="Image' , re . DOTALL ) . findall ( OoO000O0Oo )
 for o0O0oo0OO0O , url , i11ii1ii11i in Ii1 :
  if '{{' in o0O0oo0OO0O :
   pass
  else :
   iiI11ii1I1 ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' ) . replace ( '&#x27;' , '' ) , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7067 , i11ii1ii11i )
 xbmcplugin . addSortMethod ( I11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
def oO0o00 ( url ) :
 OoO000O0Oo = OO0oOO0O ( url )
 Ii1 = re . compile ( '<div class="film-container">.+?<iframe src="(.+?)"' , re . DOTALL ) . findall ( OoO000O0Oo )
 for url in Ii1 :
  Oo0OOOO0oOoo0 ( 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) )
 xbmcplugin . addSortMethod ( I11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
def Oo0OOOO0oOoo0 ( url ) :
 OoO000O0Oo = OO0oOO0O ( url )
 Ii1 = re . compile ( 'file: "(.+?)",.+?label: "(.+?)"' , re . DOTALL ) . findall ( OoO000O0Oo )
 for url , o0O0oo0OO0O in Ii1 :
  Ooo0OOoOoO0 ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' , url , 222 , iIIIi1 + 'popcorn.png' )
 xbmcplugin . addSortMethod ( I11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 92 - 92: i1I11i1I . I1ii11iIi11i - I1ii11iIi11i - I11i + Oo0o00 - o0o00Oo0O
 if 30 - 30: i1I11i1I - OO0O0OoOO0 - oO0o
 if 33 - 33: iI11I1II1I1I / OO0O0OoOO0
def OOOOiiI ( url ) :
 OoO000O0Oo = OO0oOO0O ( url )
 Ii1 = re . compile ( '</h4><p><ul><li><a href="([^"]*)">(.+?)<.+?class=' ) . findall ( OoO000O0Oo )
 OOooOO000 = re . compile ( '<li><a href="([^"]*)">(.+?)<.+?class=' ) . findall ( OoO000O0Oo )
 for url , o0O0oo0OO0O in Ii1 :
  if '(cooltvseries.com)' in o0O0oo0OO0O :
   Ooo0OOoOoO0 ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + ' -(360)-[/COLOR]' ) . replace ( ' - (cooltvseries.com).mp4' , '' ) , url , 7053 , iIIIi1 + 'CoolSeries.png' )
 for url , o0O0oo0OO0O in OOooOO000 :
  if '(cooltvseries.com)' in o0O0oo0OO0O :
   Ooo0OOoOoO0 ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' ) . replace ( ' - (cooltvseries.com).mp4' , '' ) , url , 7053 , iIIIi1 + 'CoolSeries.png' )
def o000Ooo00o00O ( url ) :
 OoO000O0Oo = OO0oOO0O ( url )
 Ii1 = re . compile ( '<source type="video/mp4" src="([^"]*)"/>' ) . findall ( OoO000O0Oo )
 for url in Ii1 :
  o0i1I11iI1iiI ( ( url ) . replace ( ' ' , '%20' ) )
ooo0O0O0oo0 = '{XX},' ; oo000oO = '{UD},' ; IiIiII11i1 = '{YT},' ; Ii1I1iIiiI1 = '{JS},' ; o00i111iiIiiIiI = '{PF},'
if 59 - 59: iIi1i111II + oOo0O0Ooo / IIiIiII11i / OOooOOo
def oOoo00 ( ) :
 OoO000O0Oo = OO0oOO0O ( i1111 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vc2VjcmV0L2Nsb3VkLnBocA==' ) )
 Ii1 = re . compile ( '<li class="col-sm-2">.+?<a href="#" class="thumbnail" data-src="(.+?)" data-toggle="modal".+?data-target="#infoModal" name="(.+?)"> <img src="(.+?)" alt=".+?" width="130px"' , re . DOTALL ) . findall ( OoO000O0Oo )
 for IiIIIIIi , o0O0oo0OO0O , i11ii1ii11i in Ii1 :
  Ooo0OOoOoO0 ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' , 'http://stream.cloudtv.bz/stream/channel/20/' + ( i1111 ( IiIIIIIi ) ) , 222 , i11ii1ii11i )
  if 29 - 29: iIi1i111II / OOooOOo . iI11I1II1I1I / I1i1IiI1 % OOooOOo % OO0O0OoOO0
def iiI1 ( url ) :
 OoO000O0Oo = OO0oOO0O ( url )
 Ii1 = re . compile ( 'src="([^"]*)".+?alt=""></a><div class="entry unvoted"><p class="title"><a class="title may-blank " href="([^"]*)" tabindex=.+?>(.+?)</a>' , re . DOTALL ) . findall ( OoO000O0Oo )
 next = re . compile ( '<a href="([^"]*)" rel="nofollow next"' , re . DOTALL ) . findall ( OoO000O0Oo )
 for i11ii1ii11i , url , o0O0oo0OO0O in Ii1 :
  if 'youtu' in url :
   Ooo0OOoOoO0 ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' ) . replace ( '&quot;' , '"' ) . replace ( '&' , ' & ' ) , url , 7051 , 'http:' + i11ii1ii11i )
 for url in next :
  iiI11ii1I1 ( '[COLOR' + oO0o0o0ooO0oO + ']NEXT[/COLOR]' , url , 7050 , iIIIi1 + 'Next.png' )
  if 79 - 79: I1i1III
def iII1i1IIIii ( url ) :
 OoO000O0Oo = OO0oOO0O ( url )
 Ii1 = re . compile ( 'rel="shortlink" href="([^"]*)">' , re . DOTALL ) . findall ( OoO000O0Oo )
 for url in Ii1 :
  yt . PlayVideo ( ( url ) . replace ( 'https://youtu.be/' , '' ) )
  if 63 - 63: oOo0O0Ooo - Ii - OO0O0OoOO0 % I1i1IiI1 . I1i1III * Ii1I
def OooO0o ( url ) :
 OoO000O0Oo = OO0oOO0O
 Ii1 = re . compile ( 'id:"(.+?)",url:"(.+?)"' , re . DOTALL ) . findall ( OoO000O0Oo )
 for url , i11ii1ii11i , o0O0oo0OO0O in Ii1 :
  iiI11ii1I1 ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' , url , 222 , i11ii1ii11i )
  if 81 - 81: ooOoO0O00 / Oo0o00 % Ii . iI11I1II1I1I * OOooOOo + ii
  if 31 - 31: ooOoO0O00 % IIiIiII11i
  if 13 - 13: iI11I1II1I1I - IIiIiII11i % o0o00Oo0O . I1i1III % oO0o
  if 2 - 2: ii - I1i1III % OoOOOOO / oOo0O0Ooo / I11i
  if 3 - 3: IIiIiII11i / iIi1i111II
def i1IIiiIIIIi ( ) :
 if 23 - 23: ooOoO0O00 + Ii1I + oOo0O0Ooo - oOo % ii . i1I11i1I
 iiI11ii1I1 ( 'All Channels' , '' , 7021 , iIIIi1 + 'livetv.png' )
 iiI11ii1I1 ( 'Entertainment' , '' , 7021 , iIIIi1 + 'livetv.png' )
 iiI11ii1I1 ( 'Movies' , '' , 7021 , iIIIi1 + 'livetv.png' )
 iiI11ii1I1 ( 'Music' , '' , 7021 , iIIIi1 + 'livetv.png' )
 iiI11ii1I1 ( 'News' , '' , 7021 , iIIIi1 + 'livetv.png' )
 iiI11ii1I1 ( 'Sports' , '' , 7021 , iIIIi1 + 'livetv.png' )
 iiI11ii1I1 ( 'Documentary' , '' , 7021 , iIIIi1 + 'livetv.png' )
 iiI11ii1I1 ( 'Kids' , '' , 7021 , iIIIi1 + 'livetv.png' )
 iiI11ii1I1 ( 'Food' , '' , 7021 , iIIIi1 + 'livetv.png' )
 iiI11ii1I1 ( 'Religious' , '' , 7021 , iIIIi1 + 'livetv.png' )
 iiI11ii1I1 ( 'USA Channels' , '' , 7021 , iIIIi1 + 'livetv.png' )
 iiI11ii1I1 ( 'Other' , '' , 7021 , iIIIi1 + 'livetv.png' )
 if 49 - 49: OoOOOOO . OOooOOo
 if 73 - 73: I1i1III / oOo0O0Ooo / ii + oOo0O0Ooo
def o0OoOo0O00 ( Cat_Name ) :
 if 9 - 9: iIi1i111II
 I1iII = False
 I1IIiIi = '0'
 if Cat_Name == 'All Channels' : I1iII = True
 if Cat_Name == 'Entertainment' : I1IIiIi = '1'
 if Cat_Name == 'Movies' : I1IIiIi = '2'
 if Cat_Name == 'Music' : I1IIiIi = '3'
 if Cat_Name == 'News' : I1IIiIi = '4'
 if Cat_Name == 'Sports' : I1IIiIi = '5'
 if Cat_Name == 'Documentary' : I1IIiIi = '6'
 if Cat_Name == 'Kids' : I1IIiIi = '7'
 if Cat_Name == 'Food' : I1IIiIi = '8'
 if Cat_Name == 'Religious' : I1IIiIi = '9'
 if Cat_Name == 'USA Channels' : I1IIiIi = '10'
 if Cat_Name == 'Other' : I1IIiIi = '11'
 if 93 - 93: OoOOOOO - iIi1i111II + I11i . OoOOOOO / I1i1IiI1
 OoO000O0Oo = OO0oOO0O ( i1111 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz' ) )
 Ii1 = re . compile ( '"id":".+?","name":"(.+?)","img":"(.+?)","stream_url3":".+?","cat_id":"(.+?)","stream_url2":".+?","stream_url":".+?"}' , re . DOTALL ) . findall ( OoO000O0Oo )
 print 'Len Match: >>>' + str ( len ( Ii1 ) )
 for o0O0oo0OO0O , i11ii1ii11i , iI1II1i in Ii1 :
  iI1iI = i1111 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv' ) + ( i11ii1ii11i ) . replace ( '\\' , '' )
  if iI1II1i == I1IIiIi :
   iiI11ii1I1 ( o0O0oo0OO0O , '' , 7022 , iI1iI )
  elif I1iII == True :
   iiI11ii1I1 ( o0O0oo0OO0O , '' , 7022 , iI1iI )
  else : pass
  if 52 - 52: Oo0o00 + Oo0o00
  xbmcplugin . addSortMethod ( I11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 73 - 73: I11i . Ii % ii + oOo . ii / iIi1i111II
def oOiiI1i11I ( Search_Name ) :
 OoO000O0Oo = OO0oOO0O ( i1111 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz' ) )
 Ii1 = re . compile ( '"id":".+?","name":"' + Search_Name + '","img":"(.+?)","stream_url3":"(.+?)","cat_id":".+?","stream_url2":"(.+?)","stream_url":"(.+?)"}' , re . DOTALL ) . findall ( OoO000O0Oo )
 Ii1 = re . compile ( '"id":".+?","name":"' + Search_Name + '","img":"(.+?)","stream_url3":"(.+?)","cat_id":".+?","stream_url2":"(.+?)","stream_url":"(.+?)"}' , re . DOTALL ) . findall ( OoO000O0Oo )
 for i11ii1ii11i , IiIIIIIi , i1I1IiiIi1i , I1i1iiiI1 in Ii1 :
  iI1iI = i1111 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv' ) + ( i11ii1ii11i ) . replace ( '\\' , '' )
  Ooo0OOoOoO0 ( Search_Name + ': Link 1' , ( IiIIIIIi ) . replace ( '\\' , '' ) , 222 , iI1iI )
  Ooo0OOoOoO0 ( Search_Name + ': Link 2' , ( i1I1IiiIi1i ) . replace ( '\\' , '' ) , 222 , iI1iI )
  Ooo0OOoOoO0 ( Search_Name + ': Link 3' , ( I1i1iiiI1 ) . replace ( '\\' , '' ) , 222 , iI1iI )
  if 31 - 31: IIiIiII11i + iIi1i111II - ii . I1i1IiI1
def i1IoOo000Oo00o ( ) :
 OoO000O0Oo = OO0oOO0O ( i1111 ( o0OO00 ( 0 , [ 97 ] , [ 221 , 72 , 245 , 82 , 68 , 48 , 242 , 99 , 143 , 68 , 9 , 111 , 24 , 118 , 180 , 76 , 29 , 51 , 14 , 100 , 187 , 51 , 105 , 100 , 106 , 121 , 52 , 53 , 240 , 114 , 26 , 98 , 252 , 50 , 197 , 82 , 218 , 112 , 19 , 99 , 94 , 71 , 54 , 120 , 104 , 108 , 174 , 101 , 107 , 72 , 168 , 82 , 191 , 50 , 88 , 76 , 90 , 109 , 138 , 78 , 24 , 118 , 89 , 76 , 218 , 110 , 231 , 86 , 105 , 114 , 252 , 76 , 37 , 50 , 36 , 82 , 96 , 118 , 27 , 100 , 120 , 50 , 160 , 53 , 72 , 115 , 200 , 98 , 80 , 50 , 201 , 70 , 114 , 107 , 9 , 99 , 113 , 121 , 127 , 57 , 155 , 106 , 213 , 97 , 194 , 71 , 192 , 70 , 162 , 116 , 27 , 99 , 46 , 71 , 191 , 108 , 4 , 118 , 24 , 98 , 27 , 109 , 105 , 108 , 89 , 119 , 164 , 100 , 88 , 72 , 237 , 89 , 93 , 117 , 40 , 98 , 211 , 84 , 75 , 78 , 216 , 49 ] ) ) )
 Ii1 = re . compile ( '#EXTINF:-1,(.+)\s*(.+)\s*' ) . findall ( OoO000O0Oo )
 for o0O0oo0OO0O , IiIIIIIi in Ii1 :
  Ooo0OOoOoO0 ( o0O0oo0OO0O , ( IiIIIIIi ) . replace ( '"' , ' ' ) . replace ( '&' , '&' ) . strip ( ) + '|connection=keep-alive' , 222 , iIIIi1 + 'english.png' )
def o0ooOOoOoOO ( ) :
 OoO000O0Oo = OO0oOO0O ( i1111 ( o0OO00 ( 0 , [ 97 ] , [ 221 , 72 , 245 , 82 , 68 , 48 , 242 , 99 , 143 , 68 , 9 , 111 , 24 , 118 , 180 , 76 , 29 , 51 , 14 , 100 , 187 , 51 , 105 , 100 , 106 , 121 , 52 , 53 , 240 , 114 , 26 , 98 , 252 , 50 , 197 , 82 , 218 , 112 , 19 , 99 , 94 , 71 , 54 , 120 , 104 , 108 , 174 , 101 , 107 , 72 , 168 , 82 , 191 , 50 , 88 , 76 , 90 , 109 , 138 , 78 , 24 , 118 , 89 , 76 , 218 , 110 , 231 , 86 , 105 , 114 , 252 , 76 , 37 , 50 , 36 , 82 , 96 , 118 , 27 , 100 , 120 , 50 , 160 , 53 , 72 , 115 , 200 , 98 , 80 , 50 , 201 , 70 , 114 , 107 , 9 , 99 , 113 , 121 , 127 , 57 , 155 , 106 , 213 , 97 , 194 , 71 , 192 , 70 , 162 , 116 , 27 , 99 , 46 , 71 , 191 , 108 , 4 , 118 , 24 , 98 , 27 , 109 , 105 , 108 , 89 , 119 , 164 , 100 , 88 , 72 , 237 , 89 , 93 , 117 , 40 , 98 , 211 , 84 , 75 , 78 , 216 , 49 ] ) ) )
 Ii1 = re . compile ( '#EXTINF:-2,(.+)\s*(.+)\s*' ) . findall ( OoO000O0Oo )
 for o0O0oo0OO0O , IiIIIIIi in Ii1 :
  Ooo0OOoOoO0 ( o0O0oo0OO0O , ( IiIIIIIi ) . replace ( '"' , ' ' ) . replace ( '&' , '&' ) . strip ( ) , 222 , iIIIi1 + 'xxx.png' )
def iII11 ( ) :
 OoO000O0Oo = OO0oOO0O ( i1111 ( o0OO00 ( 0 , [ 97 , 129 , 72 , 149 , 82 , 100 , 48 , 63 , 99 , 170 , 68 , 159 , 111 , 42 , 118 , 83 , 76 , 128 , 51 , 61 , 100 , 44 , 51 , 201 , 100 , 148 , 121 , 134 , 53 ] , [ 159 , 114 , 70 , 98 , 144 , 50 , 37 , 82 , 253 , 112 , 184 , 99 , 50 , 71 , 154 , 120 , 110 , 108 , 179 , 101 , 250 , 72 , 65 , 82 , 125 , 50 , 52 , 76 , 28 , 109 , 124 , 78 , 191 , 118 , 193 , 76 , 193 , 110 , 145 , 86 , 92 , 114 , 193 , 76 , 41 , 50 , 82 , 82 , 206 , 118 , 32 , 100 , 163 , 50 , 209 , 53 , 191 , 115 , 42 , 98 , 30 , 50 , 237 , 70 , 26 , 107 , 70 , 99 , 64 , 121 , 115 , 57 , 230 , 116 , 32 , 97 , 39 , 88 , 58 , 104 , 38 , 50 , 77 , 98 , 185 , 50 , 86 , 81 , 80 , 117 , 111 , 98 , 226 , 84 , 75 , 78 , 210 , 49 ] ) ) )
 Ii1 = re . compile ( '#EXTINF:.+?,(.+)\s*(.+)\s*' ) . findall ( OoO000O0Oo )
 for o0O0oo0OO0O , IiIIIIIi in Ii1 :
  Ooo0OOoOoO0 ( o0O0oo0OO0O , ( IiIIIIIi ) . replace ( '"' , ' ' ) . replace ( '&' , '&' ) . strip ( ) , 222 , iIIIi1 + 'vod(1).png' )
  if 96 - 96: I1i1IiI1 * Ii1I * I1i1III + Ii1I % oOo0O0Ooo + Ii
def i1iI11Ii1i ( url ) :
 url
 IiiOooooOo0 = xbmcgui . ListItem ( o0O0oo0OO0O , path = url )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , IiiOooooOo0 )
 return
 if 45 - 45: oOo0O0Ooo . I1ii11iIi11i . Oo0o00 / OoOOOOO
 if 4 - 4: Ii + iIi1i111II
def I1111III111ii ( url ) :
 OoO000O0Oo = OO0oOO0O ( url )
 Ii1 = re . compile ( '<a class=.+?href="(.+?)">.+?<div class="videothumboverlay hidden-xs" id=".+?">(.+?)</div>.+?<div class="videothumbbox"><img src="(.+?)" class="videothumb" alt="(.+?)"></div>' , re . DOTALL ) . findall ( OoO000O0Oo )
 OOooOO000 = re . compile ( "<a href='(.+?)' class='paginationnext'>Next &raquo;</a></div>" ) . findall ( OoO000O0Oo )
 for url , O00OoOO0oo0 , i11ii1ii11i , o0O0oo0OO0O in Ii1 :
  ooOOO0 ( o0O0oo0OO0O , 'https://www.fitnessblender.com' + url , 7086 , 'https://www.fitnessblender.com' + i11ii1ii11i , '' , ( O00OoOO0oo0 ) . replace ( '</p>' , ' ' ) . replace ( '<p>' , ' ' ) )
  IiI111111IIII ( 'tvshows' , 'Media Info 3' )
 for url in OOooOO000 :
  iiI11ii1I1 ( 'NEXT' , 'https://www.fitnessblender.com' + url , 7085 , iIIIi1 + 'Next.png' )
  if 90 - 90: I1i1IiI1
def o0oOooO ( url ) :
 oOOoO0O0O0 = OO0oOO0O ( url )
 Ii1 = re . compile ( '<div class=\'videowrapper\'>.+?src="//www.youtube.com/embed/(.+?)?rel=0&amp;wmode=transparent" frameborder="0"></iframe></div>.+?<h3 class="videodetailheader">(.+?)</h3>.+?<p class="videodetailvalue"><img src=\'(.+?)\'/></p>' , re . DOTALL ) . findall ( oOOoO0O0O0 )
 for url , O00OoOO0oo0 , i11ii1ii11i in Ii1 :
  OoOO ( 'PLAY' , url , 8043 , 'https://www.fitnessblender.com' + i11ii1ii11i , '' , O00OoOO0oo0 )
  IiI111111IIII ( 'tvshows' , 'Media Info 3' )
 Ii11Iii = re . compile ( '<h2 class="videodetailheader">Workout Details</h2>(.+?)</div>' , re . DOTALL ) . findall ( oOOoO0O0O0 )
 for oo00o00O0 in Ii11Iii :
  O00o0O = ( oo00o00O0 ) . replace ( '<p>' , '' ) . replace ( '</p>' , '' ) . replace ( '<br />' , '' ) . replace ( '&nbsp;' , '' ) . replace ( '<strong>' , '' ) . replace ( '</strong>' , '' ) . replace ( '"' , '' ) . replace ( '<' , '' ) . replace ( '>' , '' ) . replace ( 'a href' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&rsquo;t' , '' ) . replace ( '&' , '&' )
  ooOOO0 ( 'INFO' , '' , 7087 , 'https://www.fitnessblender.com' + i11ii1ii11i , '' , O00o0O )
  if 73 - 73: oO0o
def ii11iiII ( INFO ) :
 o0iI11I1II ( 'info for workout' , INFO )
 if 57 - 57: OOooOOo - o0o00Oo0O . ii % oOo - I1i1III
 if 79 - 79: o0o00Oo0O + I1i1IiI1
 if 25 - 25: Oo0o00 - I1i1III / o0o00Oo0O . ii % oOo0O0Ooo . ooOoO0O00
def Ii1i ( url ) :
 OoO000O0Oo = OO0oOO0O ( url )
 Ii1 = re . compile ( 'cat-item-.+?"><a href="(.+?)" >(.+?)</a>' ) . findall ( OoO000O0Oo )
 for url , o0O0oo0OO0O in Ii1 :
  iiI11ii1I1 ( o0O0oo0OO0O , url , 9031 , iIIIi1 + 'icon.png' )
def IIII1i ( url ) :
 OoO000O0Oo = OO0oOO0O ( url )
 Ii1 = re . compile ( '<a href="(.+?)" title=".+?" rel="bookmark"><time class="entry-date published updated" datetime=".+?">(.+?)</time></a>' ) . findall ( OoO000O0Oo )
 for url , o0O0oo0OO0O in Ii1 :
  iiI11ii1I1 ( o0O0oo0OO0O , url , 9032 , iIIIi1 + 'icon.png' )
def oo0O00o0 ( url ) :
 OoO000O0Oo = OO0oOO0O ( url )
 Ii1 = re . compile ( '#EXTINF:-.+?,(.+)\s*(.+)\s*' ) . findall ( OoO000O0Oo )
 for o0O0oo0OO0O , url in Ii1 :
  if '://' in o0O0oo0OO0O :
   pass
   Ooo0OOoOoO0 ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' ) . replace ( '<br />' , '' ) , ( url ) . replace ( '<br />' , '' ) , 222 , iIIIi1 + 'icon.png' )
def Oo0oOooOooO ( url ) :
 OoO000O0Oo = OO0oOO0O ( url )
 Ii1 = re . compile ( 'EXTINF:-.+?,(.+)</div></li><li class=".+?"><div class=".+?">(.+?)</div>).findall' ) . findall ( OoO000O0Oo )
 for o0O0oo0OO0O , url in Ii1 :
  Ooo0OOoOoO0 ( o0O0oo0OO0O , url , 222 , iIIIi1 + 'icon.png' )
  if 38 - 38: Ii - OoOOOOO % i1I11i1I
  if 1 - 1: OoOOOOO + Oo0o00 . oOo0O0Ooo
  if 47 - 47: OO0O0OoOO0 . OOooOOo
def o0oOO0 ( ) :
 OoO000O0Oo = OO0oOO0O ( 'http://www.disclose.tv/action/videolist/aliens/page/1/all/channel/1/category/1/' )
 Ii1 = re . compile ( '<li><a href="([^"]*)">(.+?)</a></li>' ) . findall ( OoO000O0Oo )
 for IiIIIIIi , o0O0oo0OO0O in Ii1 :
  if 'category' in IiIIIIIi :
   iiI11ii1I1 ( o0O0oo0OO0O , 'http://www.disclose.tv/' + IiIIIIIi , 7010 , iIIIi1 + 'disclose.png' )
   if 31 - 31: I1i1III * I11i * I1i1III + oO0o * I11i . Oo0o00
   if 89 - 89: ii * I1i1III * oOo0O0Ooo . oOo * I1i1III / OO0O0OoOO0
def iioo ( url ) :
 OoO000O0Oo = OO0oOO0O ( url )
 Ii1 = re . compile ( 'href="([^"]*)"><img width="135" height="76" alt="([^"]*)".+?src="([^"]*)" />' , re . DOTALL ) . findall ( OoO000O0Oo )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' ) . findall ( OoO000O0Oo )
 for url , o0O0oo0OO0O , i11ii1ii11i in Ii1 :
  iiI11ii1I1 ( o0O0oo0OO0O , 'http://www.disclose.tv/' + url , 7011 , i11ii1ii11i )
 for url in next :
  iiI11ii1I1 ( 'NEXT' , url , 7010 , iIIIi1 + 'Next.png' )
  if 21 - 21: ooOoO0O00
  if 69 - 69: OOooOOo + OOooOOo + iIi1i111II % iIi1i111II * I1i1IiI1 % I1i1III
def ii1111IIiI1 ( url ) :
 OoO000O0Oo = OO0oOO0O ( url )
 Ii1 = re . compile ( 'url: "([^"]*)",' , re . DOTALL ) . findall ( OoO000O0Oo )
 OOooOO000 = re . compile ( "src='([^']*)' type='([^']*)' />" , re . DOTALL ) . findall ( OoO000O0Oo )
 I1iI11iii = re . compile ( '<div class="youtube-player" data-id="([^"]*)">' , re . DOTALL ) . findall ( OoO000O0Oo )
 for url in Ii1 :
  if 'http' in url :
   Ooo0OOoOoO0 ( 'video/flv' , url , 222 , iIIIi1 + 'disclose.png' )
 for url , o0O0oo0OO0O in OOooOO000 :
  Ooo0OOoOoO0 ( o0O0oo0OO0O , url , 222 , iIIIi1 + 'disclose.png' )
 for url in I1iI11iii :
  Ooo0OOoOoO0 ( 'YT Link' , url , 8043 , iIIIi1 + 'disclose.png' )
  if 59 - 59: I1i1III - I1ii11iIi11i
  if 34 - 34: I1i1III - OoOOOOO * ii . oO0o / oOo0O0Ooo
def oO0o0 ( url ) :
 OoO000O0Oo = OO0oOO0O ( url )
 Ii1 = re . compile ( '<div id="play-1".+?src="(.+?)" scrolling="no".+?<li><a href="#play-1">(.+?)</a></li>' , re . DOTALL ) . findall ( OoO000O0Oo )
 for url , o0O0oo0OO0O in Ii1 :
  iiI11ii1I1 ( o0O0oo0OO0O , ( url + '&fv=&sou=' ) . replace ( 'player' , 'watch' ) , 7000 , iIIIi1 + 'icon.png' )
  if 43 - 43: iIi1i111II
def o0IiiIIII1I1i ( name , url , img ) :
 oOOoO0O0O0 = OO0oOO0O ( url )
 I1IIIIII1 = re . compile ( '<iframe class="playerframe" src="(.+?)" scrolling=".+?" marginwidth=".+?" marginheight=".+?" vspace=".+?" hspace=".+?" allowfullscreen=".+?" webkitallowfullscreen=".+?" mozallowfullscreen=".+?" width=".+?" height=".+?" frameborder=".+?"></iframe>' , re . DOTALL ) . findall ( oOOoO0O0O0 )
 O0oO0O = len ( I1IIIIII1 )
 if 20 - 20: OOooOOo % IIiIiII11i . OOooOOo . i1I11i1I + iIi1i111II
 if 26 - 26: OO0O0OoOO0 / ii - I1ii11iIi11i
 if O0oO0O == 1 :
  for iIIi1iii1 in I1IIIIII1 :
   iIIi1iii1 = iIIi1iii1 . replace ( 'player' , 'watch' )
   o00o0 = iIIi1iii1 + '&fv=&sou='
   OOoOo0O0 = OO0oOO0O ( o00o0 )
   I1o0 = re . compile ( '<source src="(.+?)" type=".+?">' , re . DOTALL ) . findall ( OOoOo0O0 )
   for iii11i1 in I1o0 :
    I1IiiiiI1i1I = False
    Resolve ( iii11i1 )
    if 48 - 48: I1i1IiI1 + IIiIiII11i % OoOOOOO % iIi1i111II * IIiIiII11i
 elif O0oO0O > 1 :
  if 41 - 41: oO0o
  for iIIi1iii1 in I1IIIIII1 :
   i1iiiiii1 = OO0oOO0O ( iIIi1iii1 )
   OoO0oOOOO = re . compile ( '<iframe width=".*?" height=".*?" frameborder=".*?" src="(.*?)" scrolling=".*?" marginwidth=".*?" marginheight=".*?" vspace=".*?" hspace=".*?" allowfullscreen=".*?" webkitallowfullscreen=".*?" mozallowfullscreen=".*?"></iframe>' , re . DOTALL ) . findall ( i1iiiiii1 )
   o0oo00OOOo = OoO0oOOOO
   o0oo00OOOo = ( str ( o0oo00OOOo ) ) . replace ( '[\'' , '' ) . replace ( '\']' , '' ) ;
   print 'Stripped url : ' + o0oo00OOOo
   Ooo0OOoOoO0 ( 'DOUBLE LINK' , o0oo00OOOo , 424 , '' )
   if 99 - 99: oOo0O0Ooo / Ii % OoOOOOO
   for url in OoO0oOOOO :
    iiI11ii1I1 ( 'DOUBLE LINK' , url , 424 , '' )
    try :
     i1I1IiiIi1i = Google . resolve ( url )
    except :
     pass
    try :
     i1i1IIi = re . findall ( r"{'url': u'(.*?)', 'quality': 'HD'}, {'url': u'(.*?)', 'quality': 'SD'}" , str ( i1I1IiiIi1i ) )
     for o0oo0Ooo0 , o0OOoO in i1i1IIi :
      if 11 - 11: I1i1III * I11i / i1I11i1I + OOooOOo + oO0o % Oo0o00
      HD_URLS . append ( o0oo0Ooo0 )
      SD_URLS . append ( o0OOoO )
    except :
     pass
 else :
  pass
  if 18 - 18: oOo0O0Ooo - OOooOOo
def II1III ( ) :
 if 14 - 14: Ii1I * Oo0o00 % ooOoO0O00 / Ii1I
 if 48 - 48: I1ii11iIi11i
 iiI11ii1I1 ( 'Genres' , 'http://cnfstudio.com/movies/' , 7002 , iIIIi1 + 'Movies.png' )
 if 75 - 75: Ii1I - i1I11i1I * I1ii11iIi11i . ii * Oo0o00 * oOo0O0Ooo
 iiI11ii1I1 ( 'Search Movies' , '' , 7017 , iIIIi1 + 'Movies.png' )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 30 - 30: OOooOOo / OoOOOOO / I1i1III * I11i * OoOOOOO . oOo0O0Ooo
 if 93 - 93: OOooOOo
def o0OoOo0o0OOoO0 ( ) :
 OoO000O0Oo = OO0oOO0O ( 'http://cnfstudio.com/' )
 Ii1 = re . compile ( '<a href="http://cnfstudio.com/genre/(.+?)">(.+?)</a>' ) . findall ( OoO000O0Oo )
 for IiIIIIIi , o0O0oo0OO0O in Ii1 :
  iiI11ii1I1 ( o0O0oo0OO0O , 'http://cnfstudio.com/genre/' + IiIIIIIi , 7003 , iIIIi1 + 'icon.png' )
  if 30 - 30: I1i1III % I1i1IiI1 + I11i
oooOOOOO = xbmcgui . Dialog ( )
if 65 - 65: iI11I1II1I1I . OO0O0OoOO0 / I1i1III
iI11ii = '{UN},' ; oOoooO00OO0o = '{IG},' ; iIi1iI = '{PL},' ; i11ii = '{LO},' ; IiI111I = '{LP},' ; oo0oO0 = '{HA},' ; ii1i1Iii = '{XD},' ; IIII11111Ii = '{TA},' ; IiiiII = '{DP},' ; OoOoo00Oo0OoO = '{JT},' ; o0o0oOOO = '{JJ},' ; OOooo = '{MM},' ; IIII = '{FQ},' ; o0o0OOo0OOoO = '{HH},'
if 52 - 52: i1I11i1I / IIiIiII11i / oOo0O0Ooo - oOo + OOooOOo * oOo0O0Ooo
def ooOIIIi11i ( url ) :
 OoO000O0Oo = OO0oOO0O ( url )
 Ii1 = re . compile ( '<div class="movie">.+?<img src="(.+?)" alt=".+?" />.+?<a href="(.+?)"><span class="player"></span></a>.+?<h2>(.+?)</h2>' , re . DOTALL ) . findall ( OoO000O0Oo )
 oooOOoo0 = re . compile ( "<link rel='next' href='(.+?)'/>" ) . findall ( OoO000O0Oo )
 for i11ii1ii11i , url , o0O0oo0OO0O in Ii1 :
  Ooo0OOoOoO0 ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' ) . replace ( '&#038;' , '' ) . replace ( '&#8216;' , '' ) . replace ( '&#8217;' , '' ) . replace ( '&#8211;' , '' ) , url , 7004 , i11ii1ii11i )
 oooOOoo0 = oooOOoo0
 for url in oooOOoo0 :
  iiI11ii1I1 ( 'Next Page' , url , 7003 , iIIIi1 + 'Next.png' )
  if 79 - 79: ii - oOo * I1i1III - IIiIiII11i % OOooOOo * i1I11i1I
def iI1III ( url ) :
 if 42 - 42: oOo + OO0O0OoOO0 + I1i1III * I1i1IiI1 . ooOoO0O00
 OoO000O0Oo = OO0oOO0O ( url )
 Ii1 = re . compile ( '<div id="play-1" class="player-content"><iframe class="playerframe" src="(.+?)" scrolling="no".+?</div>' , re . DOTALL ) . findall ( OoO000O0Oo )
 for url in Ii1 :
  I11i1I1I = url + '&fv=&sou='
  I11i1I1I = I11i1I1I . replace ( 'player' , 'watch' )
  oo0oOo = IiiiI1I1iI11 ( I11i1I1I )
  iIiIiI1ii = IiiiI1I1iI11 ( url )
  if 75 - 75: oO0o % ii
  if 16 - 16: o0o00Oo0O / ooOoO0O00
def IiiiI1I1iI11 ( url ) :
 if 58 - 58: I11i / Ii / o0o00Oo0O % I1i1IiI1 % oOo0O0Ooo
 OoO000O0Oo = OO0oOO0O ( url )
 Ii1 = re . compile ( '<video id=".+?<source src="(.+?)" type="video/mp4">' , re . DOTALL ) . findall ( OoO000O0Oo )
 for url in Ii1 :
  iII1ii1 ( url )
  if 86 - 86: i1I11i1I + OOooOOo / oOo0O0Ooo + I1i1IiI1 % I1i1IiI1 / Ii
  if 12 - 12: OOooOOo + I11i . Oo0o00
def ooO00OO ( ) :
 ooOOO0 ( '[COLOR' + oO0o0o0ooO0oO + ']Local M3u[/COLOR]' , oOo0oooo00o , 2001 , iIIIi1 + 'LocalM3U.png' , i1iIIi1 , '' )
 ooOOO0 ( '[COLOR' + oO0o0o0ooO0oO + ']Remote M3u[/COLOR]' , Oo0o0000o0o0 , 7080 , iIIIi1 + 'RemoteM3U.png' , i1iIIi1 , '' )
 if 64 - 64: oOo - I11i % OO0O0OoOO0 % Oo0o00 . OoOOOOO
def OOoO00OoOOO ( ) :
 if os . path . exists ( oOo0oooo00o ) :
  OoOo0oo = open ( oOo0oooo00o , 'r' )
  for IiiOooooOo0 in OoOo0oo :
   i1iIOO00o0oo = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( IiiOooooOo0 )
   for o0O0oo0OO0O , IiIIIIIi in i1iIOO00o0oo :
    Ooo0OOoOoO0 ( o0O0oo0OO0O , IiIIIIIi , 222 , iIIIi1 + 'streams.png' )
 else :
  oOOoo00O0O . ok ( 'Set m3u path' , 'you need to set path to your m3u file' )
  o0oO0 . openSettings ( sys . argv [ 0 ] )
  if 3 - 3: I1i1III * oOo - oOo0O0Ooo / ooOoO0O00
def ii1iIi1 ( url ) :
 if os . path . exists ( Remote ) :
  oOOoO0O0O0 = Oo0o0oooo0O0 ( url )
  Ii1 = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( oOOoO0O0O0 )
  for o0O0oo0OO0O , url in Ii1 :
   url = ( url ) . strip ( )
   Ooo0OOoOoO0 ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' ) . replace ( '_' , ' ' ) , url , 222 , '' )
 else :
  oOOoo00O0O . ok ( 'Set m3u path' , 'you need to set path to your m3u file' )
  o0oO0 . openSettings ( sys . argv [ 0 ] )
  if 44 - 44: oO0o + I1i1IiI1 % oO0o + ooOoO0O00 + OO0O0OoOO0 + o0o00Oo0O
  if 18 - 18: iI11I1II1I1I % iI11I1II1I1I % OoOOOOO + oOo0O0Ooo % oOo / I1i1III
def iI1iIIiiii ( ) :
 oOOoO0O0O0 = OO0oOO0O ( i1111 ( 'aHR0cHM6Ly9naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvdHJlZS9tYXN0ZXIvX3JlcG8vcGx1Z2luLnZpZGVvLkdlbmllVHY=' ) )
 Ii1 = re . compile ( '<span class="css-truncate css-truncate-target"><a href="/GenieTv/Genie_Tv/blob/master/_repo/plugin.video.GenieTv/(.+?)" class="js-navigation-open" id=".+?" title=".+?">.+?</a></span>' ) . findall ( oOOoO0O0O0 )
 for IiIIIIIi in Ii1 :
  IiIIIIIi = i1111 ( 'aHR0cDovL3Jhdy5naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvbWFzdGVyL19yZXBvL3BsdWdpbi52aWRlby5HZW5pZVR2Lw==' ) + IiIIIIIi
 o0O0oo0OO0O = 'plugin.video.GenieTv'
 if 36 - 36: OOooOOo . Ii
 oO00O0o0oOOO ( IiIIIIIi , o0O0oo0OO0O )
 if 96 - 96: oOo0O0Ooo - iI11I1II1I1I
def IIi1I11I1II ( ) :
 oOOoO0O0O0 = OO0oOO0O ( i1111 ( 'aHR0cHM6Ly9naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvdHJlZS9tYXN0ZXIvX3JlcG8vcmVwb3NpdG9yeS5HZW5pZVR2' ) )
 Ii1 = re . compile ( '<span class="css-truncate css-truncate-target"><a href="/GenieTv/Genie_Tv/blob/master/_repo/repository.GenieTv/(.+?)" class="js-navigation-open" id=".+?" title=".+?">.+?</a></span>' ) . findall ( oOOoO0O0O0 )
 for IiIIIIIi in Ii1 :
  IiIIIIIi = i1111 ( 'aHR0cDovL3Jhdy5naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvbWFzdGVyL19yZXBvL3JlcG9zaXRvcnkuR2VuaWVUdi8=' ) + IiIIIIIi
 o0O0oo0OO0O = 'repository.GenieTv'
 if 25 - 25: ii . I1i1III % OO0O0OoOO0 . i1I11i1I
 oO00O0o0oOOO ( IiIIIIIi , o0O0oo0OO0O )
 if 67 - 67: ii + Oo0o00 / oOo
 if 75 - 75: i1I11i1I / ii . oOo0O0Ooo + Oo0o00 - IIiIiII11i
def I1i11iIii1i1iI ( ) :
 ooOOO0 ( '[COLOR' + oO0o0o0ooO0oO + ']CATAGORIES[/COLOR]' , '' , 10051 , iIIIi1 + 'Catagories.png' , i1iIIi1 , '' )
 ooOOO0 ( '[COLOR' + oO0o0o0ooO0oO + ']SEARCH[/COLOR]' , '' , 10052 , iIIIi1 + 'Search.png' , i1iIIi1 , '' )
 if 99 - 99: iI11I1II1I1I - OoOOOOO - OOooOOo / iI11I1II1I1I * I1ii11iIi11i - OoOOOOO
 if 72 - 72: i1I11i1I % ooOoO0O00 / iI11I1II1I1I
o0oO0 = xbmcaddon . Addon ( id = 'plugin.video.GenieTv' )
oOOoo00O0O = xbmcgui . Dialog ( )
i1iiIII111ii = xbmc . translatePath ( 'special://home/' )
Oo0oO0ooo = xbmcgui . DialogProgress ( )
ooIii = 'https://addons.tvaddons.ag/'
if 66 - 66: iIi1i111II * I11i
def OoOOO0o0Ooo ( ) :
 O0oOOoooOO0O = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 Oo0o0O00 = O0oOOoooOO0O . lower ( )
 oOo0OoOOOo0 = 'https://addons.tvaddons.ag/search/?keyword=' + Oo0o0O00
 oOOoO0O0O0 = OO0oOO0O ( oOo0OoOOOo0 )
 Ii1 = re . compile ( '<li><a href="(.+?)"><span class=".+?"><img src="(.+?)" width=".+?" alt=".+?" class=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( oOOoO0O0O0 )
 for IiIIIIIi , I111i1i1111 , o0O0oo0OO0O in Ii1 :
  ooOOO0 ( o0O0oo0OO0O , IiIIIIIi , 10054 , 'https://addons.tvaddons.ag/' + I111i1i1111 , i1iIIi1 , '' )
  if 19 - 19: Ii
  if 80 - 80: oOo0O0Ooo
def oO0OOo ( ) :
 oOOoO0O0O0 = OO0oOO0O ( ooIii )
 Ii1 = re . compile ( '<li><a href="(.+?)"><span class="thumbnail"><img src="(.+?)" class="pic" alt=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( oOOoO0O0O0 )
 for IiIIIIIi , i11ii1ii11i , o0O0oo0OO0O in Ii1 :
  if 'Repositories' in o0O0oo0OO0O :
   pass
  elif 'Services' in o0O0oo0OO0O :
   pass
  elif 'International' in o0O0oo0OO0O :
   pass
  else :
   ooOOO0 ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' , IiIIIIIi , 10053 , 'https://addons.tvaddons.ag/' + i11ii1ii11i , i1iIIi1 , '' )
   if 63 - 63: IIiIiII11i . Oo0o00 % i1I11i1I + IIiIiII11i
   if 81 - 81: iIi1i111II - oOo0O0Ooo % I11i
def Addon ( url ) :
 oOOoO0O0O0 = OO0oOO0O ( url )
 i1iiIiIi1 = re . compile ( '<li class="nextPage"><a class=".+?" href="(.+?)"><dfn title="next Page">.+?</dfn></a></li>' ) . findall ( oOOoO0O0O0 )
 Ii1 = re . compile ( '<li><a href="(.+?)"><span class=".+?"><img src="(.+?)" width=".+?" alt=".+?" class=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( oOOoO0O0O0 )
 for url , i11ii1ii11i , o0O0oo0OO0O in Ii1 :
  if 'Please' in o0O0oo0OO0O :
   pass
  else :
   OoOO ( o0O0oo0OO0O , url , 10054 , 'https://addons.tvaddons.ag/' + i11ii1ii11i , i1iIIi1 , '' )
 for url in i1iiIiIi1 :
  ooOOO0 ( '[COLOR' + oO0o0o0ooO0oO + ']NEXT PAGE[/COLOR]' , 'https://addons.tvaddons.ag' + url , 10053 , iIIIi1 + 'Next.png' , i1iIIi1 , '' )
  if 31 - 31: o0o00Oo0O * I11i * I1ii11iIi11i
  if 95 - 95: OO0O0OoOO0 / Ii / I1ii11iIi11i % ii - I11i * OO0O0OoOO0
def iIIiiII11i1I1 ( url , name ) :
 oOOoO0O0O0 = OO0oOO0O ( url )
 Ii1 = re . compile ( '<a href="(.+?)"' ) . findall ( oOOoO0O0O0 )
 for url in Ii1 :
  if 'plugin' in url :
   print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<' + url
   IIiooOooo0 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
   Oo0oO0ooo = xbmcgui . DialogProgress ( )
   Oo0oO0ooo . create ( "GenieTv" , "Downloading Content" , '' , 'Please Wait' )
   iI111I11i = os . path . join ( IIiooOooo0 , name + '.zip' )
   try :
    os . remove ( iI111I11i )
   except :
    pass
   downloader . download ( url , iI111I11i , Oo0oO0ooo )
   IioOoooO00O = xbmc . translatePath ( os . path . join ( 'special://home' , 'addons' ) )
   time . sleep ( 2 )
   Oo0oO0ooo . update ( 0 , "" , "Extracting Zip Please Wait" )
   print '======================================='
   print IioOoooO00O
   print '======================================='
   extract . all ( iI111I11i , IioOoooO00O , Oo0oO0ooo )
   oOOOoo00 ( )
   if 28 - 28: IIiIiII11i * oOo * OOooOOo * Oo0o00 . IIiIiII11i . Ii1I
def oO00O0o0oOOO ( url , name ) :
 IIiooOooo0 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 Oo0oO0ooo = xbmcgui . DialogProgress ( )
 Oo0oO0ooo . create ( "GenieTv" , "Downloading Content" , '' , 'Please Wait' )
 iI111I11i = os . path . join ( IIiooOooo0 , name + '.zip' )
 try :
  os . remove ( iI111I11i )
 except :
  pass
 downloader . download ( url , iI111I11i , Oo0oO0ooo )
 IioOoooO00O = xbmc . translatePath ( os . path . join ( 'special://home' , 'addons' ) )
 time . sleep ( 2 )
 Oo0oO0ooo . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print IioOoooO00O
 print '======================================='
 extract . all ( iI111I11i , IioOoooO00O , Oo0oO0ooo )
 oOOOoo00 ( )
 if 32 - 32: oOo - oO0o . OO0O0OoOO0 . OO0O0OoOO0 % ooOoO0O00 * I1i1III
def oOOOoo00 ( ) :
 xbmc . executebuiltin ( 'UpdateLocalAddons' )
 xbmc . executebuiltin ( 'UpdateAddonRepos' )
 oooOOOOO = xbmcgui . Dialog ( )
 oooOOOOO . ok ( "Origin + Genie TV" , '' , '                                 REFRESH SUCCESSFUL :)' , "                          [COLOR gold]Brought To You By Origin + Jaybox[/COLOR]" )
 return
 if 65 - 65: OO0O0OoOO0 / oOo . IIiIiII11i
 if 90 - 90: I1i1IiI1
def o00oooo ( url ) :
 OoO000O0Oo = Oo0o0oooo0O0 ( url )
 Ii1 = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( OoO000O0Oo )
 for url , I111i1i1111 , o0O0oo0OO0O in Ii1 :
  iiI11ii1I1 ( o0O0oo0OO0O , url , 1007 , I111i1i1111 )
def ooo0Oo00O ( url ) :
 OoO000O0Oo = Oo0o0oooo0O0 ( url )
 Ii1 = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( OoO000O0Oo )
 for url , I111i1i1111 , o0O0oo0OO0O in Ii1 :
  iiI11ii1I1 ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' , url , 1006 , I111i1i1111 )
  if 28 - 28: i1I11i1I + OOooOOo . i1I11i1I - I1i1III % ooOoO0O00 % iI11I1II1I1I
  if 100 - 100: I1ii11iIi11i - iIi1i111II * oOo * oO0o
def O0ooO ( url , iconimage , name ) :
 from imports import cache
 cache = cache . get ( '' , 0 , url )
 OoO000O0Oo = Oo0o0oooo0O0 ( url )
 Ii1 = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( OoO000O0Oo )
 for url , iconimage , O00OoOO0oo0 , iIi11i1 , name in Ii1 :
  if 'http' in url :
   if '.php' in url :
    IIII1iIIii = re . compile ( 'url="(.+?)"\n' ) . findall ( str ( OOO00 ) )
    for IiiOooooOo0 in IIII1iIIii :
     if IiiOooooOo0 == url :
      name = ( '[COLORred]Watched - [/COLOR]' + name ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' )
    oOOo0OoOOOoo ( name , url , 1016 , iconimage , iIi11i1 , O00OoOO0oo0 )
   else :
    if 'youtube' in url :
     IIII1iIIii = re . compile ( 'url="(.+?)"\n' ) . findall ( str ( OOO00 ) )
     for IiiOooooOo0 in IIII1iIIii :
      if IiiOooooOo0 == url :
       name = ( '[COLORred]Watched - [/COLOR]' + name ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' )
     Oo0OOo ( name , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , iconimage , iIi11i1 , O00OoOO0oo0 )
    else :
     IIII1iIIii = re . compile ( 'url="(.+?)"\n' ) . findall ( str ( OOO00 ) )
     for IiiOooooOo0 in IIII1iIIii :
      if IiiOooooOo0 == url :
       name = ( '[COLORred]Watched - [/COLOR]' + name ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' )
     Oo0OOo ( name , url , 222 , iconimage , iIi11i1 , O00OoOO0oo0 )
     IiI111111IIII ( 'movies' , 'INFO' )
  else :
   Iii1iIIIi11I1 ( url , iconimage , name )
   if 38 - 38: I1ii11iIi11i * Ii1I - oOo % Ii1I
 else :
  Ii1 = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( OoO000O0Oo )
  for url , I111i1i1111 , name in Ii1 :
   if 'http' in url :
    if '.php' in url :
     iiI11ii1I1 ( name , url , 1016 , I111i1i1111 )
    else :
     if 'youtube' in url :
      print '>>>>>>>>>>>>>>>>>>>>>>> youtube old way'
      Ooo0OOoOoO0 ( name , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , I111i1i1111 )
     else :
      IIII1iIIii = re . compile ( 'url="(.+?)"\n' ) . findall ( str ( OOO00 ) )
      for IiiOooooOo0 in IIII1iIIii :
       if IiiOooooOo0 == url :
        name = '[COLORred]Watched - [/COLOR]' + name
      Ooo0OOoOoO0 ( name , url , 222 , I111i1i1111 )
      IiI111111IIII ( 'movies' , 'INFO' )
   else :
    Iii1iIIIi11I1 ( url , I111i1i1111 , name )
  xbmcplugin . addSortMethod ( I11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 return cache
 if 12 - 12: iIi1i111II + oO0o * I1i1IiI1 + I1i1III + i1I11i1I
def Iii1iIIIi11I1 ( url , iconimage , name ) :
 iconimage = iconimage
 name = name
 url = url
 O0O00oOo0o000 = ( url ) . replace ( oOOoO0O , 'http' ) . replace ( oo000oO , '.com' ) ;
 oO0oOoO0o0o = ( O0O00oOo0o000 ) . replace ( OoOoO , 'a' ) . replace ( I1IIII11 , 'b' ) . replace ( o0I1iI111ii111i , 'c' ) . replace ( oO0oO0O , 'd' ) . replace ( iIi1iI , 'e' ) . replace ( OoOoo00Oo0OoO , 'f' ) ;
 OOO00o00o0o0Oo = ( oO0oOoO0o0o ) . replace ( ooo0O0O0oo0 , 'g' ) . replace ( oo0oO0 , 'h' ) . replace ( IiIiII11i1 , 'i' ) . replace ( o00i111iiIiiIiI , 'j' ) . replace ( o00iI1Ii11iIiiI1 , 'k' ) . replace ( i11iII11ii , 'l' ) ;
 ii1I11 = ( OOO00o00o0o0Oo ) . replace ( OoO00 , 'm' ) . replace ( OO0ooO0O , 'n' ) . replace ( II1i111i , 'o' ) . replace ( oOoO0oO00ooOo , 'p' ) . replace ( iIoOO0OO00 , 'q' ) . replace ( O0oO00oO0o00o , 'r' ) ;
 o0OOo0O00OO0O = ( ii1I11 ) . replace ( oOO0oOOoO , 's' ) . replace ( ooooO , 't' ) . replace ( oo0O000O00 , 'u' ) . replace ( oO0oO00 , 'v' ) . replace ( IiiI1Ii1II , 'w' ) . replace ( OO0oIii1I1I , 'x' ) ;
 IIiIIiIi1II1IiI = ( o0OOo0O00OO0O ) . replace ( oo0OoO , 'y' ) . replace ( I11iIiiI , 'z' ) . replace ( iI11ii , '.' ) . replace ( oOoooO00OO0o , '(' ) . replace ( i11ii , ')' ) . replace ( IiI111I , '/' ) ;
 OO000oo0o = ( IIiIIiIi1II1IiI ) . replace ( III1IiIi1 , '1' ) . replace ( O000oooO0 , '2' ) . replace ( I11iiIiI1II11 , '3' ) . replace ( IIII11111Ii , '4' ) . replace ( IiiiII , '5' ) . replace ( Ii1I1iIiiI1 , '6' ) ;
 OOOoOOOo = ( OO000oo0o ) . replace ( o0o0oOOO , '7' ) . replace ( OOooo , '8' ) . replace ( IIII , '9' ) . replace ( o0o0OOo0OOoO , '0' ) . replace ( OoooO00OoO0 , ':' ) . replace ( iiIiI1I1I1IiI , '%' ) ;
 url = ( OOOoOOOo ) . replace ( iii11III1I , '-' ) . replace ( ii1i1Iii , '_' ) ;
 Ooo0OOoOoO0 ( name , url , 222 , iconimage ) ;
 if 82 - 82: I1ii11iIi11i + Oo0o00
 if 93 - 93: I1i1IiI1 * o0o00Oo0O * iIi1i111II - I11i / Ii1I
def oooOo0OO ( ) :
 OoO000O0Oo = Oo0o0oooo0O0 ( i1111 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vdm9kL3VybHMvdXJsLnBocA==' ) )
 Ii1 = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( OoO000O0Oo )
 for IiIIIIIi , I111i1i1111 , o0O0oo0OO0O in Ii1 :
  iiI11ii1I1 ( o0O0oo0OO0O , IiIIIIIi , 1007 , I111i1i1111 )
def iII ( url ) :
 OoO000O0Oo = Oo0o0oooo0O0 ( url )
 Ii1 = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( OoO000O0Oo )
 for url , I111i1i1111 , o0O0oo0OO0O in Ii1 :
  iiI11ii1I1 ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' , url , 1006 , I111i1i1111 )
  if 31 - 31: I1i1III % I11i % Oo0o00 . Ii1I / I11i * OoOOOOO
def OoI1 ( name , url , iconimage = None ) :
 print '--- Playing "{0}". {1}' . format ( name , url )
 OoO00o00 = xbmcgui . ListItem ( path = url , thumbnailImage = iconimage )
 OoO00o00 . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , OoO00o00 )
 if 72 - 72: ooOoO0O00
 if 21 - 21: Oo0o00 . iIi1i111II / Ii * ooOoO0O00
def O00O0ooo00OO0 ( url ) :
 OoO000O0Oo = Oo0o0oooo0O0 ( url )
 Ii1 = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( OoO000O0Oo )
 for url , i11ii1ii11i , o0O0oo0OO0O in Ii1 :
  if '-dir-' in o0O0oo0OO0O :
   iiI11ii1I1 ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' ) . replace ( '-dir-' , '' ) , url , 1012 , i11ii1ii11i )
  else :
   iiI11ii1I1 ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' , url , 1006 , i11ii1ii11i )
   if 63 - 63: I1i1IiI1 * IIiIiII11i
def oo00OO ( url ) :
 OoO000O0Oo = Oo0o0oooo0O0 ( url )
 oOOoOo0Ooo = ( 'http://afewbitsmore.com/' )
 Ii1 = re . compile ( '<A HREF="(.+?)">(.+?)</A><br>' , re . DOTALL ) . findall ( OoO000O0Oo )
 for url , o0O0oo0OO0O in Ii1 :
  if '[To Parent Directory]' in o0O0oo0OO0O :
   o0O0oo0OO0O = 'HOME'
   pass
  elif 'HOME' in o0O0oo0OO0O :
   pass
  elif '.m3u' in o0O0oo0OO0O :
   iiI11ii1I1 ( '[COLOR' + oO0o0o0ooO0oO + ']PLAY ALL[/COLOR]' , oOOoOo0Ooo + url , 2002 , iIIIi1 + 'music.png' )
  elif '.mp3' in o0O0oo0OO0O :
   Ooo0OOoOoO0 ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' ) . replace ( '.mp3' , '' ) . replace ( 'amp;' , '' ) , oOOoOo0Ooo + url , 222 , iIIIi1 + 'music.png' )
  elif '.m4a' in o0O0oo0OO0O :
   Ooo0OOoOoO0 ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' ) . replace ( '.m4a' , '' ) . replace ( 'amp;' , '' ) , oOOoOo0Ooo + url , 222 , iIIIi1 + 'music.png' )
  else :
   iiI11ii1I1 ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' ) , oOOoOo0Ooo + url , 1012 , iIIIi1 + 'music.png' )
def o0OOoOoo00 ( url ) :
 oOOoO0O0O0 = Oo0o0oooo0O0 ( url )
 Ii1 = re . compile ( 'EXTINF:(.+?),(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( oOOoO0O0O0 )
 for i11ii1ii11i , o0O0oo0OO0O , url in Ii1 :
  Ooo0OOoOoO0 ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' ) . replace ( '_' , ' ' ) , url , 10012 , iIIIi1 + 'music.png' )
  if 96 - 96: iI11I1II1I1I + OOooOOo * ooOoO0O00 . OO0O0OoOO0
def IiIIiIi11ii ( url ) :
 OoO000O0Oo = Oo0o0oooo0O0 ( url )
 oOOoOo0Ooo = url
 Ii1 = re . compile ( "<a href='(.+?)'>(.+?)</a>" ) . findall ( OoO000O0Oo )
 for url , o0O0oo0OO0O in Ii1 :
  if '.mp3' in o0O0oo0OO0O :
   print '<<<<<<<<<<<<<<<<<<<' + url + '>>>>>>>>>>>>>>>>>>>>>>>>>>>'
   Ooo0OOoOoO0 ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' ) . replace ( '.mp3' , '' ) . replace ( '/' , '' ) , 'http://hypem.com' + url , 222 , iIIIi1 + 'music.png' )
  else :
   iiI11ii1I1 ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' ) . replace ( '/' , '' ) , oOOoOo0Ooo + url , 1011 , iIIIi1 + 'music.png' )
def II11IiIIiiiii ( ) :
 OoO000O0Oo = Oo0o0oooo0O0 ( i1111 ( 'aHR0cDovL3d3dy5jeW4ubmV0L211c2ljLw==' ) )
 Ii1 = re . compile ( '<td><a href="(.+?)"><img src="(.+?)"><br>(.+?)</a></td>' , re . DOTALL ) . findall ( OoO000O0Oo )
 for IiIIIIIi , i11ii1ii11i , o0O0oo0OO0O in Ii1 :
  iiI11ii1I1 ( o0O0oo0OO0O , ( 'http://www.cyn.net/music/' + IiIIIIIi ) . replace ( ' ' , '%20' ) , 1031 , ( 'http://www.cyn.net/music/' + i11ii1ii11i ) . replace ( ' ' , '%20' ) )
def oooOOo0o0OOO ( url , img ) :
 OoO000O0Oo = Oo0o0oooo0O0 ( url )
 i1I1IiiIi1i = url
 img = img
 Ii1 = re . compile ( '<a href="(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( OoO000O0Oo )
 for url , o0O0oo0OO0O in Ii1 :
  Ooo0OOoOoO0 ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' ) . replace ( '.mp3' , '' ) , ( i1I1IiiIi1i + '/' + url ) . replace ( ' ' , '%20' ) , 222 , img )
  if 17 - 17: iI11I1II1I1I + ooOoO0O00 . Ii1I + I1i1III % ooOoO0O00 . OoOOOOO
def o00OoOO00 ( url ) :
 OoO000O0Oo = Oo0o0oooo0O0 ( url )
 i1I1IiiIi1i = url
 Ii1 = re . compile ( 'alt="(.+?)"></td><td><a href="(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( OoO000O0Oo )
 for type , url , o0O0oo0OO0O in Ii1 :
  if '[VID]' in type :
   Ooo0OOoOoO0 ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' ) . replace ( '.mp4' , '' ) . replace ( '_H.264-AAC' , '' ) . replace ( '(' , ' (' ) . replace ( ')' , ') ' ) , i1I1IiiIi1i + url , 222 , iIIIi1 + 'music.png' )
  if '[DIR]' in type :
   o00OoOO00 ( i1I1IiiIi1i + url )
 xbmcplugin . addSortMethod ( I11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 62 - 62: OOooOOo * ii * I11i
 if 37 - 37: OoOOOOO
def I1Ii1iI1IiI1I ( ) :
 iI1iiIii1I11I = ( i1111 ( 'aHR0cDovL2h5cGVtLmNvbS9kb3dubG9hZC8=' ) )
 O0oOOoooOO0O = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 Oo0o0O00 = O0oOOoooOO0O . lower ( )
 IiIIIIIi = ( i1111 ( 'aHR0cDovL3Bhbmljc3RyZWFtLm5ldC9zdHJlYW1zLw==' ) )
 i1I1IiiIi1i = ( i1111 ( 'aHR0cDovL21hc2xvdmQubm8taXAub3JnL3B1YmxpYy9tcDMv' ) )
 I1i1iiiI1 = ( i1111 ( 'aHR0cDovL3d3dy5jeW4ubmV0L211c2ljLw==' ) )
 if 95 - 95: I1i1IiI1 + I1ii11iIi11i + I1ii11iIi11i
 oOOoO0O0O0 = oo0OooOOo0 ( IiIIIIIi )
 Oo000o = oo0OooOOo0 ( i1I1IiiIi1i )
 I11IiI1I11i1i = oo0OooOOo0 ( I1i1iiiI1 )
 if 33 - 33: ooOoO0O00 % ii / ii
 if oOOoO0O0O0 != 'Failed' :
  Ii1 = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( oOOoO0O0O0 )
  for o0O0oo0OO0O in Ii1 :
   if O0oOOoooOO0O in o0O0oo0OO0O . lower ( ) :
    iiI11ii1I1 ( ( o0O0oo0OO0O + ' source 1' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( IiIIIIIi + o0O0oo0OO0O ) . replace ( ' ' , '%20' ) , 1006 , '' )
    if 88 - 88: Oo0o00 - I1i1III - OoOOOOO + ooOoO0O00
    IiI111111IIII ( 'tvshows' , 'Media Info 3' )
 if Oo000o != 'Failed' :
  OOooOO000 = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( oOOoO0O0O0 )
  for o0O0oo0OO0O in OOooOO000 :
   if O0oOOoooOO0O in o0O0oo0OO0O . lower ( ) :
    iiI11ii1I1 ( ( o0O0oo0OO0O + ' source 2' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( i1I1IiiIi1i + o0O0oo0OO0O ) . replace ( ' ' , '%20' ) , 1006 , '' )
    if 15 - 15: iIi1i111II
    IiI111111IIII ( 'tvshows' , 'Media Info 3' )
 if I11IiI1I11i1i != 'Failed' :
  I1iI11iii = re . compile ( '<td><a href=".+?"><img src=".+?"><br>(.+?)</a></td>' , re . DOTALL ) . findall ( I11IiI1I11i1i )
  for o0O0oo0OO0O in I1iI11iii :
   if O0oOOoooOO0O in o0O0oo0OO0O . lower ( ) :
    iiI11ii1I1 ( ( o0O0oo0OO0O + ' source 3' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( I1i1iiiI1 + o0O0oo0OO0O ) . replace ( ' ' , '%20' ) , 1031 , '' )
    if 31 - 31: OoOOOOO % ooOoO0O00 . ii - I11i + ii
    IiI111111IIII ( 'tvshows' , 'Media Info 3' )
    if 45 - 45: iIi1i111II + I1i1IiI1 / ii - I1i1III + ii
    if 42 - 42: iI11I1II1I1I * oOo0O0Ooo * Oo0o00
    if 62 - 62: iIi1i111II * o0o00Oo0O % i1I11i1I . i1I11i1I . oOo0O0Ooo
    if 91 - 91: ooOoO0O00 . OO0O0OoOO0
    if 37 - 37: OO0O0OoOO0 - I1i1IiI1 + iI11I1II1I1I / Oo0o00 - oO0o . I11i
    if 62 - 62: Ii1I
OoO00 = '{SF},' ; OO0ooO0O = '{IF},' ; II1i111i = '{PW},' ; I11iiIiI1II11 = '{AM},' ; oOoO0oO00ooOo = '{GF},' ; iIoOO0OO00 = '{DD},' ; O0oO00oO0o00o = '{UO},' ; oOO0oOOoO = '{LE},' ; oo0O000O00 = '{ZY},' ; oO0oO00 = '{UE},' ; IiiI1Ii1II = '{PE},' ; OO0oIii1I1I = '{JE},' ; oo0OoO = '{TH},' ; I11iIiiI = '{LK},'
if 47 - 47: Oo0o00 % iIi1i111II * oO0o . iI11I1II1I1I % I1ii11iIi11i + ii
if 2 - 2: Oo0o00 % ii - oOo * Ii1I * i1I11i1I
def Ooi11 ( ) :
 OoO000O0Oo = OO0oOO0O ( 'http://www.iwatchseries.me/tv-list/' )
 Ii1 = re . compile ( '<h5><a href="([^"]*)"><strong>(.+?)</strong></a></h5>' ) . findall ( OoO000O0Oo )
 for IiIIIIIi , o0O0oo0OO0O in Ii1 :
  iiI11ii1I1 ( o0O0oo0OO0O , IiIIIIIi , 8021 , iIIIi1 + 'iwatch.png' )
def O00oOoOo0ooO0O0oo ( url ) :
 OoO000O0Oo = OO0oOO0O ( url )
 Ii1 = re . compile ( '<h5><strong><a href="([^"]*)">(.+?)</a>(.+?)</strong></h5>' ) . findall ( OoO000O0Oo )
 for url , o0O0oo0OO0O , O0oooo00o0Oo in Ii1 :
  iiI11ii1I1 ( o0O0oo0OO0O + O0oooo00o0Oo , url , 8022 , iIIIi1 + 'iwatch.png' )
def ii11IiI ( url ) :
 OoO000O0Oo = OO0oOO0O ( url )
 Ii1 = re . compile ( '<iframe src="([^"]*)"' ) . findall ( OoO000O0Oo )
 for url in Ii1 :
  print '>>>>>>>>>>>>>>>>>>>>' + url
  I1iI1Ii11 ( url )
def I1iI1Ii11 ( url ) :
 OoO000O0Oo = OO0oOO0O ( url )
 Ii1 = re . compile ( '{.+?"file" : "(.+?)",.+?"default" : true.+?"label" : "(.+?)"' , re . DOTALL ) . findall ( OoO000O0Oo )
 OOooOO000 = re . compile ( 'setup\(\{.+?file: "(.+?)",.+?skin' , re . DOTALL ) . findall ( OoO000O0Oo )
 I1iI11iii = re . compile ( "{ label: '([^']*)', file:.+?'([^']*)' }" ) . findall ( OoO000O0Oo )
 for url , o0O0oo0OO0O in Ii1 :
  Ooo0OOoOoO0 ( 'VidSpot - ' + o0O0oo0OO0O , url , 222 , iIIIi1 + 'iwatch.png' )
 for url in OOooOO000 :
  Ooo0OOoOoO0 ( 'VodLocker' , url , 222 , iIIIi1 + 'iwatch.png' )
 for o0O0oo0OO0O , url in I1iI11iii :
  print '<><><><><><><><><><><> before   ' + url
  if 'hevideo' in url :
   print '>>>>>>>>>>>>>>>>>>>>>>>>>' + url
   Ooo0OOoOoO0 ( 'TheVideo - ' + o0O0oo0OO0O , url , 222 , iIIIi1 + 'iwatch.png' )
   if 34 - 34: I1i1III * oOo0O0Ooo + I1i1IiI1 * OOooOOo - IIiIiII11i
def OOo ( ) :
 OoO000O0Oo = cloudflare . source ( 'http://www.animeland.me/anime-list' )
 Ii1 = re . compile ( 'letter-spacing:-1px;" href="([^"]*)">(.+?)</a></li>' ) . findall ( OoO000O0Oo )
 for IiIIIIIi , o0O0oo0OO0O in Ii1 :
  iiI11ii1I1 ( o0O0oo0OO0O , IiIIIIIi , 1021 , iIIIi1 + 'anime.png' )
  if 51 - 51: OO0O0OoOO0
  if 81 - 81: o0o00Oo0O
def i11ii11IiI1 ( ) :
 OoO000O0Oo = OO0oOO0O ( 'http://www.animetoon.org/cartoon' )
 Ii1 = re . compile ( '<td><a href="(.+?)">(.+)</a></td>' ) . findall ( OoO000O0Oo )
 for IiIIIIIi , o0O0oo0OO0O in Ii1 :
  iiI11ii1I1 ( o0O0oo0OO0O , IiIIIIIi , 1002 , iIIIi1 + 'anime.png' )
  if 47 - 47: iI11I1II1I1I % I1i1IiI1 . I1i1IiI1 / o0o00Oo0O . Ii * I1i1III
  if 24 - 24: o0o00Oo0O
  if 33 - 33: ii + OoOOOOO * IIiIiII11i / iIi1i111II
def oooo ( url ) :
 OoO000O0Oo = OO0oOO0O ( url )
 OOooOO000 = re . compile ( '<img src="(.+?)" id="series_image" width="250" height="370" alt=".+?" />' ) . findall ( OoO000O0Oo )
 for i11ii1ii11i in OOooOO000 :
  OO0o0oO0O000o = i11ii1ii11i
 I1iI11iii = re . compile ( '<li><a href="(.+?)">Next</a></li>' ) . findall ( OoO000O0Oo )
 for url in I1iI11iii :
  iiI11ii1I1 ( 'NEXT PAGE' , url , 1002 , iIIIi1 + 'Next.png' )
 Ii1 = re . compile ( '&nbsp;<a href="(.+?)">(.+?)</a>' ) . findall ( OoO000O0Oo )
 for url , o0O0oo0OO0O in Ii1 :
  iiI11ii1I1 ( o0O0oo0OO0O , url , 1003 , OO0o0oO0O000o )
 xbmcplugin . addSortMethod ( I11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
def I11iii1iIIIIi ( url , IMAGE ) :
 OoO000O0Oo = OO0oOO0O ( url )
 Ii1 = re . compile ( '"playlist">(.+?)</span></div><div><iframe src="(.+?)"' ) . findall ( OoO000O0Oo )
 for o0O0oo0OO0O , url in Ii1 :
  print o0O0oo0OO0O + '     ' + url
  if 'easy' in url :
   III1i1iiI1 ( url )
  elif 'playpanda' in url :
   III1i1iiI1 ( url )
   if 62 - 62: I1i1III . Ii % o0o00Oo0O % Oo0o00 - I1ii11iIi11i
  xbmcplugin . addSortMethod ( I11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
def III1i1iiI1 ( url ) :
 OoO000O0Oo = OO0oOO0O ( url )
 Ii1 = re . compile ( "url: '(.+?)'," ) . findall ( OoO000O0Oo )
 for url in Ii1 :
  Ooo0OOoOoO0 ( 'STREAM' , url , 222 , iIIIi1 + 'anime.png' )
  if 69 - 69: IIiIiII11i . OOooOOo * OOooOOo % I1i1III + oOo0O0Ooo
  if 100 - 100: Ii - I1ii11iIi11i
def i11I1Ii1Iiii1 ( url ) :
 o0O = urllib2 . Request ( url )
 o0O . add_header ( 'User-Agent' , "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0" )
 o0O . add_header ( 'referer' , url )
 O00oO = urllib2 . urlopen ( o0O )
 I11i1I1I = O00oO . read ( )
 O00oO . close ( )
 return I11i1I1I
 if 64 - 64: I1i1III . ii - Ii1I
def Oo0o0oooo0O0 ( url ) :
 o0O = urllib2 . Request ( url )
 o0O . add_header ( 'User-Agent' , "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0" )
 O00oO = urllib2 . urlopen ( o0O )
 I11i1I1I = O00oO . read ( )
 O00oO . close ( )
 return I11i1I1I
 if 19 - 19: I1ii11iIi11i
def iIIiI1I1i1 ( url ) :
 xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
 o0oo0Ooooo0 = ( '%s%s' % ( Oo0oOo000OoO0 , url ) )
 I11i1I1I = Oo0o0oooo0O0 ( url )
 Ii1 = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( I11i1I1I )
 for url , I111i1i1111 , o0O0oo0OO0O in Ii1 :
  Ooo0OOoOoO0 ( '%s' % ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' ) . replace ( 'GenieTv' , '[COLOR green]GenieTV[/COLOR]' ) . replace ( '.' , ' ' ) . replace ( 'mp4' , '' ) . replace ( 'mkv' , '' ) . replace ( '_' , ' ' ) , '%s' % ( url ) , 222 , I111i1i1111 )
  if 6 - 6: oOo0O0Ooo . IIiIiII11i + Oo0o00 / oO0o % oOo0O0Ooo . ii
def iII1ii1 ( url ) :
 if 64 - 64: iI11I1II1I1I + IIiIiII11i . OO0O0OoOO0 % I1ii11iIi11i * oOo
 iiii1i1 = open ( OOOO , "a" )
 iiii1i1 . write ( 'url="' + url + '"\n' )
 iiii1i1 . close
 if 98 - 98: Ii1I - ii / oOo0O0Ooo . oOo - ooOoO0O00
 iiIIi = xbmc . Player ( ooOO0 ( ) )
 import urlresolver
 try : iiIIi . play ( url )
 except : pass
 from urlresolver import common
 Oo0oO0ooo = xbmcgui . DialogProgress ( )
 Oo0oO0ooo . create ( 'LOADING' , 'Opening %s Now' % ( o0O0oo0OO0O ) )
 iiIIi = xbmc . Player ( ooOO0 ( ) )
 url = urlresolver . HostedMediaFile ( url ) . resolve ( )
 if Oo0oO0ooo . iscanceled ( ) :
  print "[COLORred]STREAM CANCELLED[/COLOR]"
  oooOOOOO = xbmcgui . Dialog ( )
  if oooOOOOO . yesno ( "[B]CANCELLED[/B]" , '[B]Was There A Problem[/B]' , '' , "" , 'Yes' , 'No' ) :
   oooOOOOO . ok ( "Message Send" , "Your Message Has Been Sent" )
  else :
   return
 else :
  try : iiIIi . play ( url )
  except : pass
  try : o0oO0 . resolve_url ( url )
  except : pass
  Oo0oO0ooo . close ( )
  if 60 - 60: OOooOOo % OOooOOo
def I1I ( url ) :
 Oo0oO0ooo = xbmcgui . DialogProgress ( )
 Oo0oO0ooo . create ( 'Featching Your Video' , 'Featching Your Video' )
 Oo0oO0ooo . update ( 0 , '%s' % o0O0oo0OO0O )
 xbmc . sleep ( 1 )
 iiIIi = xbmc . Player ( ooOO0 ( ) )
 Oo0oO0ooo . update ( 100 , '%s' % o0O0oo0OO0O )
 xbmc . sleep ( 1 )
 iiIIi . play ( url ) . strip ( )
 Oo0oO0ooo . close ( )
 if 9 - 9: i1I11i1I - IIiIiII11i * oO0o
def o0i1I11iI1iiI ( url ) :
 iiIIi = xbmc . Player ( ooOO0 ( ) )
 import urlresolver
 url = ( url ) . strip ( )
 try : iiIIi . play ( url ) . strip ( )
 except : pass
 if 78 - 78: iI11I1II1I1I / o0o00Oo0O * OoOOOOO / OO0O0OoOO0 / OOooOOo
 if 15 - 15: oOo / OoOOOOO
def ooOO0 ( ) :
 try :
  O0Oo00o0o = getSet ( "core-player" )
  if ( O0Oo00o0o == 'DVDPLAYER' ) : oooooO0oO0o = xbmc . PLAYER_CORE_DVDPLAYER
  elif ( O0Oo00o0o == 'MPLAYER' ) : oooooO0oO0o = xbmc . PLAYER_CORE_MPLAYER
  elif ( O0Oo00o0o == 'PAPLAYER' ) : oooooO0oO0o = xbmc . PLAYER_CORE_PAPLAYER
  else : oooooO0oO0o = xbmc . PLAYER_CORE_AUTO
 except : oooooO0oO0o = xbmc . PLAYER_CORE_AUTO
 return oooooO0oO0o
 return True
 if 63 - 63: I1i1III - IIiIiII11i . I1i1IiI1 / OOooOOo
def iiI11ii1I1 ( name , url , mode , iconimage , showcontext = True , allinfo = { } ) :
 OooOooO0O0o0 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 OOO0o0 = True
 IIIIII111Ii = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 IIIIII111Ii . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 if showcontext :
  ii1IIi1IIIIi1 = [ ]
  if showcontext == 'fav' :
   ii1IIi1IIIIi1 . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in IIIii1II1II :
   ii1IIi1IIIIi1 . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  IIIIII111Ii . addContextMenuItems ( ii1IIi1IIIIi1 )
 OOO0o0 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = OooOooO0O0o0 , listitem = IIIIII111Ii , isFolder = True )
 return OOO0o0
 if 4 - 4: Ii1I - i1I11i1I
def oooOOOoOOOo0O ( name , url , mode , iconimage , fanart , description ) :
 if 6 - 6: o0o00Oo0O . ii . Oo0o00 - I1i1III / oOo
 OooOooO0O0o0 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 OOO0o0 = True
 IIIIII111Ii = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 IIIIII111Ii . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 IIIIII111Ii . setProperty ( "Fanart_Image" , fanart )
 OOO0o0 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = OooOooO0O0o0 , listitem = IIIIII111Ii , isFolder = True )
 return OOO0o0
 if 34 - 34: OOooOOo % I11i - OoOOOOO
def Ooo0OOoOoO0 ( name , url , mode , iconimage , showcontext = True , allinfo = { } ) :
 OooOooO0O0o0 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 OOO0o0 = True
 IIIIII111Ii = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 IIIIII111Ii . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 if showcontext :
  ii1IIi1IIIIi1 = [ ]
  if showcontext == 'fav' :
   ii1IIi1IIIIi1 . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in IIIii1II1II :
   ii1IIi1IIIIi1 . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  IIIIII111Ii . addContextMenuItems ( ii1IIi1IIIIi1 )
 OOO0o0 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = OooOooO0O0o0 , listitem = IIIIII111Ii , isFolder = False )
 return OOO0o0
 if 40 - 40: OO0O0OoOO0
 if 82 - 82: Oo0o00 . ooOoO0O00 / OoOOOOO
 if 56 - 56: OO0O0OoOO0
 if 23 - 23: ooOoO0O00
 if 24 - 24: i1I11i1I
 if 51 - 51: iIi1i111II % Ii
def o0iI11I1II ( heading , announce ) :
 class o0OoOoOo0O ( ) :
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
   try : oo0OOo0 = open ( announce ) ; iIi11ii = oo0OOo0 . read ( )
   except : iIi11ii = announce
   self . win . getControl ( self . CONTROL_TEXTBOX ) . setText ( str ( iIi11ii ) )
   return
 o0OoOoOo0O ( )
 o0OoOoOo0O ( )
 if 37 - 37: ooOoO0O00 . Oo0o00 - IIiIiII11i % I11i - ooOoO0O00 . OoOOOOO
def iiiiI ( ) :
 o0iI11I1II ( 'GenieTv recomended sources for Kodi' , '[COLORwhite]http://genietv.com/repo[/COLOR] [CR]  [COLORred]http://genietv.com/repo[/COLOR] [CR]' )
 if 66 - 66: ii + OO0O0OoOO0 . i1I11i1I % ooOoO0O00
 if 58 - 58: iIi1i111II % OO0O0OoOO0 * o0o00Oo0O + Ii1I - i1I11i1I
 if 26 - 26: ooOoO0O00 / oOo0O0Ooo / I1i1IiI1 + I1i1IiI1
 if 46 - 46: Oo0o00 % Ii1I + I1i1III
 if 67 - 67: iI11I1II1I1I . Ii . Ii . Ii / I1i1IiI1 + oOo
def oOOOoo00 ( ) :
 xbmc . executebuiltin ( 'UpdateLocalAddons' )
 xbmc . executebuiltin ( 'UpdateAddonRepos' )
 oooOOOOO = xbmcgui . Dialog ( )
 oooOOOOO . ok ( "GenieTv" , '' , '                                 REFRESH SUCCESSFUL :)' , "                          [COLOR gold]Brought To You By Kodi Support Group, GenieTv[/COLOR]" )
 return
 if 10 - 10: oOo - I1ii11iIi11i % IIiIiII11i
 if 66 - 66: iI11I1II1I1I . iI11I1II1I1I
 if 46 - 46: Oo0o00 * OoOOOOO . I1i1III * Oo0o00 * iI11I1II1I1I / I1i1IiI1
 if 46 - 46: IIiIiII11i % Ii1I . iIi1i111II . I1ii11iIi11i / Ii + oO0o
 if 47 - 47: i1I11i1I . iIi1i111II
 if 96 - 96: I1i1IiI1 % IIiIiII11i / oOo % iIi1i111II / oOo % Ii
 if 57 - 57: I1i1IiI1 - I1i1IiI1 % IIiIiII11i % I1ii11iIi11i . I11i % I1ii11iIi11i
 if 91 - 91: oOo0O0Ooo - oO0o - I1ii11iIi11i - I1i1III * iI11I1II1I1I
 if 68 - 68: oO0o % o0o00Oo0O * iI11I1II1I1I / OoOOOOO * I11i + iIi1i111II
 if 89 - 89: oOo * oOo0O0Ooo . OoOOOOO
 if 75 - 75: oOo - OO0O0OoOO0 % OO0O0OoOO0 + oOo * I11i - Ii1I
 if 26 - 26: I1i1IiI1 * I1i1III % oOo0O0Ooo + OO0O0OoOO0
 if 38 - 38: OO0O0OoOO0 - I1ii11iIi11i / I1i1III + OoOOOOO . OO0O0OoOO0 + i1I11i1I
 if 19 - 19: I1i1III
 if 51 - 51: iI11I1II1I1I
 if 8 - 8: oO0o / I11i % OO0O0OoOO0 . Ii . ii . I1i1III
 if 8 - 8: oO0o * I1ii11iIi11i
 if 41 - 41: I1ii11iIi11i / oO0o / OOooOOo - Ii - OOooOOo
 if 4 - 4: I1i1IiI1 . i1I11i1I
 if 39 - 39: iIi1i111II . I1ii11iIi11i - OOooOOo * Ii
 if 4 - 4: OOooOOo * o0o00Oo0O - I1i1IiI1
 if 72 - 72: I1i1IiI1 + oOo / oOo0O0Ooo . i1I11i1I % oO0o / Ii
 if 13 - 13: Oo0o00 % I11i + iIi1i111II + Oo0o00 + Ii - Ii1I
 if 70 - 70: IIiIiII11i * IIiIiII11i . oOo0O0Ooo
def iiIi1111iiI1 ( url ) :
 I11i1I1I = OO0oOO0O ( str ( oooo000 ) + o00oo00 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 Ii1 = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( I11i1I1I )
 for o0O0oo0OO0O , url , oOOO00o000o , iIi11i1 , oOoO00oo0O in Ii1 :
  ooOOO0 ( o0O0oo0OO0O , url , 42 , oOOO00o000o , iIi11i1 , oOoO00oo0O )
 IiI111111IIII ( 'movies' , 'MAIN' )
 if 57 - 57: iIi1i111II + I11i . iIi1i111II
def ooOOoo0 ( url ) :
 I11i1I1I = OO0oOO0O ( str ( oooo000 ) + i11iiIII1Iii1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 Ii1 = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( I11i1I1I )
 for o0O0oo0OO0O , url , oOOO00o000o , iIi11i1 , oOoO00oo0O in Ii1 :
  ooOOO0 ( o0O0oo0OO0O , url , 42 , oOOO00o000o , iIi11i1 , oOoO00oo0O )
 IiI111111IIII ( 'movies' , 'MAIN' )
 if 19 - 19: ooOoO0O00 - iI11I1II1I1I . I1i1IiI1
def iiIIi1i111i ( url ) :
 I11i1I1I = OO0oOO0O ( str ( oooo000 ) + iIIOoO ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 Ii1 = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( I11i1I1I )
 for o0O0oo0OO0O , url , oOOO00o000o , iIi11i1 , oOoO00oo0O in Ii1 :
  ooOOO0 ( o0O0oo0OO0O , url , 42 , oOOO00o000o , iIi11i1 , oOoO00oo0O )
 IiI111111IIII ( 'movies' , 'MAIN' )
 if 87 - 87: I11i
def O00O ( url ) :
 I11i1I1I = OO0oOO0O ( str ( oooo000 ) + iIO0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 Ii1 = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( I11i1I1I )
 for o0O0oo0OO0O , url , oOOO00o000o , iIi11i1 , oOoO00oo0O in Ii1 :
  ooOOO0 ( o0O0oo0OO0O , url , 42 , oOOO00o000o , iIi11i1 , oOoO00oo0O )
 IiI111111IIII ( 'movies' , 'MAIN' )
 if 94 - 94: i1I11i1I - iI11I1II1I1I % OoOOOOO
def O0oOo0Ooo ( url ) :
 I11i1I1I = OO0oOO0O ( str ( oooo000 ) + III ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 Ii1 = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( I11i1I1I )
 for o0O0oo0OO0O , url , oOOO00o000o , iIi11i1 , oOoO00oo0O in Ii1 :
  ooOOO0 ( o0O0oo0OO0O , url , 42 , oOOO00o000o , iIi11i1 , oOoO00oo0O )
 IiI111111IIII ( 'movies' , 'MAIN' )
 if 40 - 40: Oo0o00 % I11i / oOo0O0Ooo
def II1111II ( url ) :
 I11i1I1I = OO0oOO0O ( str ( oooo000 ) + oOOOoooO ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 Ii1 = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( I11i1I1I )
 for o0O0oo0OO0O , url , oOOO00o000o , iIi11i1 , oOoO00oo0O in Ii1 :
  ooOOO0 ( o0O0oo0OO0O , url , 42 , oOOO00o000o , iIi11i1 , oOoO00oo0O )
 IiI111111IIII ( 'movies' , 'MAIN' )
 if 32 - 32: Ii1I * oOo0O0Ooo + I11i % IIiIiII11i + iIi1i111II + I1i1III
def oo0OOo0Oo00 ( url ) :
 I11i1I1I = OO0oOO0O ( str ( oooo000 ) + o0oOOoOoOOo ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 Ii1 = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( I11i1I1I )
 for o0O0oo0OO0O , url , oOOO00o000o , iIi11i1 , oOoO00oo0O in Ii1 :
  ooOOO0 ( o0O0oo0OO0O , url , 42 , oOOO00o000o , iIi11i1 , oOoO00oo0O )
 IiI111111IIII ( 'movies' , 'MAIN' )
 if 61 - 61: OO0O0OoOO0 * oOo
def i1I1IiIiiI1II ( url ) :
 I11i1I1I = OO0oOO0O ( str ( oooo000 ) + iI1i ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 Ii1 = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( I11i1I1I )
 for o0O0oo0OO0O , url , oOOO00o000o , iIi11i1 , oOoO00oo0O in Ii1 :
  ooOOO0 ( o0O0oo0OO0O , url , 42 , oOOO00o000o , iIi11i1 , oOoO00oo0O )
 IiI111111IIII ( 'movies' , 'MAIN' )
 if 85 - 85: IIiIiII11i - I1i1III
def O0Oo ( url ) :
 I11i1I1I = OO0oOO0O ( str ( oooo000 ) + IIiII ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 Ii1 = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( I11i1I1I )
 for o0O0oo0OO0O , url , oOOO00o000o , iIi11i1 , oOoO00oo0O in Ii1 :
  ooOOO0 ( o0O0oo0OO0O , url , 42 , oOOO00o000o , iIi11i1 , oOoO00oo0O )
 IiI111111IIII ( 'movies' , 'MAIN' )
 if 27 - 27: ii * oOo0O0Ooo - OO0O0OoOO0 / OO0O0OoOO0
def Ii11iIi1iIiii ( url ) :
 I11i1I1I = OO0oOO0O ( str ( oooo000 ) + iIIIi ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 Ii1 = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( I11i1I1I )
 for o0O0oo0OO0O , url , oOOO00o000o , iIi11i1 , oOoO00oo0O in Ii1 :
  ooOOO0 ( o0O0oo0OO0O , url , 5 , iIIIi1 + 'GenieTVRSSFeed.png' , iIIIi1 + 'GenieTVRSSFeed.png' , oOoO00oo0O )
 IiI111111IIII ( 'movies' , 'MAIN' )
 if 11 - 11: I1i1IiI1
 if 45 - 45: OoOOOOO + I11i + i1I11i1I / I1i1III + I11i
 if 33 - 33: OO0O0OoOO0 - I1ii11iIi11i - I1i1IiI1
 if 61 - 61: I1i1III + oOo0O0Ooo / ooOoO0O00 + ooOoO0O00 / OoOOOOO
 if 47 - 47: Oo0o00
 if 25 - 25: OO0O0OoOO0 + oOo0O0Ooo + OOooOOo + Oo0o00 % o0o00Oo0O
 if 26 - 26: oOo + OOooOOo
 if 17 - 17: Ii1I - OO0O0OoOO0 % I1ii11iIi11i * o0o00Oo0O % o0o00Oo0O * iIi1i111II
 if 6 - 6: Oo0o00
def ii1iiIiiiI11 ( ) :
 try :
  if os . path . exists ( oOOoO0 ) == True :
   oooOOOOO = xbmcgui . Dialog ( )
   if oooOOOOO . yesno ( "Delete Thumbnails" , "[COLOR gold][B]##########WARNING ANDROID ONLY##########[/B][/COLOR]" , "This feature deletes your thumbnail folder and textures13.db" , "Are you sure you want to do proceed? This Can NOT Be Undone" ) :
    for O0o00O0Oo0 , II1I , OoOo000oOo0oo in os . walk ( oOOoO0 ) :
     o00o0o0o = 0
     o00o0o0o += len ( OoOo000oOo0oo )
     if o00o0o0o > 0 :
      for oo0OOo0 in OoOo000oOo0oo :
       os . unlink ( os . path . join ( O0o00O0Oo0 , oo0OOo0 ) )
  IiI1 = os . path . join ( OOooO0OOoo , "Textures13.db" )
  os . unlink ( IiI1 )
  oooOOOOO . ok ( "Restart KODI" , "Please restart KODI to rebuild thumbnail library" )
 except :
  oooOOOOO = xbmcgui . Dialog ( )
  oooOOOOO . ok ( o0oOoO00o , "Error Deleting Thumbnails please visit The Support Group, GenieTv on facebook" )
 return
 if 73 - 73: Oo0o00
 if 25 - 25: i1I11i1I
 if 77 - 77: I11i . iI11I1II1I1I . ii . iI11I1II1I1I
 if 87 - 87: IIiIiII11i - ii / ooOoO0O00 . I1i1III - I1ii11iIi11i . Ii
 if 47 - 47: I1ii11iIi11i % oO0o - oOo - I1ii11iIi11i * OoOOOOO
 if 72 - 72: I11i % I11i + OO0O0OoOO0 + Ii1I / I1ii11iIi11i
 if 30 - 30: I1ii11iIi11i + oOo0O0Ooo + Ii / oO0o
 if 64 - 64: i1I11i1I
 if 80 - 80: oOo0O0Ooo - Ii / oO0o / OOooOOo + OOooOOo
def oo000oiIIIII ( url ) :
 print '############################################################       DELETING STANDARD CACHE             ###############################################################'
 IIIi1i1i1iii = os . path . join ( xbmc . translatePath ( 'special://home' ) , 'cache' )
 if os . path . exists ( IIIi1i1i1iii ) == True :
  for O0o00O0Oo0 , II1I , OoOo000oOo0oo in os . walk ( IIIi1i1i1iii ) :
   o00o0o0o = 0
   o00o0o0o += len ( OoOo000oOo0oo )
   if 53 - 53: oO0o
   if 80 - 80: IIiIiII11i - I11i . iI11I1II1I1I
   if o00o0o0o > 0 :
    if 44 - 44: Ii % I1i1IiI1 % Ii1I
    oooOOOOO = xbmcgui . Dialog ( )
    if oooOOOOO . yesno ( "Delete KODI Cache Files" , str ( o00o0o0o ) + " files found" , "Do you want to delete them?" ) :
     if 7 - 7: I1ii11iIi11i * oO0o - IIiIiII11i % Oo0o00 . I1ii11iIi11i . I1ii11iIi11i
     for oo0OOo0 in OoOo000oOo0oo :
      try :
       os . unlink ( os . path . join ( O0o00O0Oo0 , oo0OOo0 ) )
      except :
       pass
     for oOO in II1I :
      try :
       shutil . rmtree ( os . path . join ( O0o00O0Oo0 , oOO ) )
      except :
       pass
       if 5 - 5: ii * Ii1I
   else :
    pass
 if xbmc . getCondVisibility ( 'system.platform.ATV2' ) :
  IIio0 = os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'Other' )
  if 27 - 27: OOooOOo . Oo0o00 * OOooOOo
  for O0o00O0Oo0 , II1I , OoOo000oOo0oo in os . walk ( IIio0 ) :
   o00o0o0o = 0
   o00o0o0o += len ( OoOo000oOo0oo )
   if 8 - 8: OoOOOOO * i1I11i1I * oOo
   if o00o0o0o > 0 :
    if 26 - 26: OO0O0OoOO0 * iIi1i111II / iIi1i111II - OO0O0OoOO0
    oooOOOOO = xbmcgui . Dialog ( )
    if oooOOOOO . yesno ( "Delete ATV2 Cache Files" , str ( o00o0o0o ) + " files found in 'Other'" , "Do you want to delete them?" ) :
     if 59 - 59: I1i1III % OO0O0OoOO0 / IIiIiII11i + oOo0O0Ooo * oOo
     for oo0OOo0 in OoOo000oOo0oo :
      os . unlink ( os . path . join ( O0o00O0Oo0 , oo0OOo0 ) )
     for oOO in II1I :
      shutil . rmtree ( os . path . join ( O0o00O0Oo0 , oOO ) )
      if 100 - 100: Ii1I
   else :
    pass
  oO0o0OooOO0 = os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'LocalAndRental' )
  if 42 - 42: ii . OOooOOo
  for O0o00O0Oo0 , II1I , OoOo000oOo0oo in os . walk ( oO0o0OooOO0 ) :
   o00o0o0o = 0
   o00o0o0o += len ( OoOo000oOo0oo )
   if 93 - 93: oOo0O0Ooo
   if o00o0o0o > 0 :
    if 89 - 89: ii % Ii + Oo0o00
    oooOOOOO = xbmcgui . Dialog ( )
    if oooOOOOO . yesno ( "Delete ATV2 Cache Files" , str ( o00o0o0o ) + " files found in 'LocalAndRental'" , "Do you want to delete them?" ) :
     if 12 - 12: OOooOOo * oOo
     for oo0OOo0 in OoOo000oOo0oo :
      os . unlink ( os . path . join ( O0o00O0Oo0 , oo0OOo0 ) )
     for oOO in II1I :
      shutil . rmtree ( os . path . join ( O0o00O0Oo0 , oOO ) )
      if 59 - 59: IIiIiII11i * ii - ii
   else :
    pass
    if 33 - 33: o0o00Oo0O . Ii % I11i
    if 50 - 50: oOo
    if 81 - 81: Ii * iI11I1II1I1I / I1ii11iIi11i * iIi1i111II
    if 83 - 83: Ii - oOo0O0Ooo * Ii
 O0ooO0oOO = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.whatthefurk/cache' ) , '' )
 if os . path . exists ( O0ooO0oOO ) == True :
  for O0o00O0Oo0 , II1I , OoOo000oOo0oo in os . walk ( O0ooO0oOO ) :
   o00o0o0o = 0
   o00o0o0o += len ( OoOo000oOo0oo )
   if 53 - 53: o0o00Oo0O / IIiIiII11i - iIi1i111II - OoOOOOO . iIi1i111II
   if 4 - 4: iIi1i111II - I1ii11iIi11i % IIiIiII11i - oO0o % ooOoO0O00 % oOo
   if o00o0o0o > 0 :
    if 31 - 31: iI11I1II1I1I / ii
    oooOOOOO = xbmcgui . Dialog ( )
    if oooOOOOO . yesno ( "Delete WTF Cache Files" , str ( o00o0o0o ) + " files found" , "Do you want to delete them?" ) :
     if 8 - 8: iI11I1II1I1I . iI11I1II1I1I + I1i1III . iIi1i111II
     for oo0OOo0 in OoOo000oOo0oo :
      os . unlink ( os . path . join ( O0o00O0Oo0 , oo0OOo0 ) )
     for oOO in II1I :
      shutil . rmtree ( os . path . join ( O0o00O0Oo0 , oOO ) )
      if 58 - 58: iI11I1II1I1I + Oo0o00 - Ii1I - ooOoO0O00 * OOooOOo
   else :
    pass
    if 4 - 4: ii
    if 7 - 7: i1I11i1I
 iII1iii = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.4od/cache' ) , '' )
 if os . path . exists ( iII1iii ) == True :
  for O0o00O0Oo0 , II1I , OoOo000oOo0oo in os . walk ( iII1iii ) :
   o00o0o0o = 0
   o00o0o0o += len ( OoOo000oOo0oo )
   if 97 - 97: Oo0o00 / iIi1i111II - Ii
   if 79 - 79: OOooOOo + iI11I1II1I1I * ooOoO0O00 * oOo - I1i1IiI1 * oO0o
   if o00o0o0o > 0 :
    if 78 - 78: OO0O0OoOO0 % Ii + OO0O0OoOO0 + I11i
    oooOOOOO = xbmcgui . Dialog ( )
    if oooOOOOO . yesno ( "Delete 4oD Cache Files" , str ( o00o0o0o ) + " files found" , "Do you want to delete them?" ) :
     if 22 - 22: I1i1IiI1 - I11i
     for oo0OOo0 in OoOo000oOo0oo :
      os . unlink ( os . path . join ( O0o00O0Oo0 , oo0OOo0 ) )
     for oOO in II1I :
      shutil . rmtree ( os . path . join ( O0o00O0Oo0 , oOO ) )
      if 54 - 54: OoOOOOO * oO0o - OO0O0OoOO0 * I1i1IiI1 + I11i - I1i1III
   else :
    pass
    if 5 - 5: OoOOOOO + I1i1III
    if 48 - 48: Oo0o00 * ooOoO0O00 - Ii1I / oOo0O0Ooo + Ii - ooOoO0O00
 oOo0Oi1i1III11IiIi = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.iplayer/iplayer_http_cache' ) , '' )
 if os . path . exists ( oOo0Oi1i1III11IiIi ) == True :
  for O0o00O0Oo0 , II1I , OoOo000oOo0oo in os . walk ( oOo0Oi1i1III11IiIi ) :
   o00o0o0o = 0
   o00o0o0o += len ( OoOo000oOo0oo )
   if 99 - 99: IIiIiII11i - iI11I1II1I1I
   if 24 - 24: oOo0O0Ooo - ooOoO0O00 - o0o00Oo0O % Oo0o00 - iI11I1II1I1I . I1i1IiI1
   if o00o0o0o > 0 :
    if 26 - 26: oO0o % ooOoO0O00 * o0o00Oo0O . Oo0o00
    oooOOOOO = xbmcgui . Dialog ( )
    if oooOOOOO . yesno ( "Delete BBC iPlayer Cache Files" , str ( o00o0o0o ) + " files found" , "Do you want to delete them?" ) :
     if 31 - 31: o0o00Oo0O - i1I11i1I * Ii * ooOoO0O00
     for oo0OOo0 in OoOo000oOo0oo :
      os . unlink ( os . path . join ( O0o00O0Oo0 , oo0OOo0 ) )
     for oOO in II1I :
      shutil . rmtree ( os . path . join ( O0o00O0Oo0 , oOO ) )
      if 78 - 78: oOo * OOooOOo . I1i1III . OOooOOo % iI11I1II1I1I
   else :
    pass
    if 67 - 67: I1i1III . I1ii11iIi11i
    if 39 - 39: I1i1IiI1 * Oo0o00
    if 63 - 63: oOo % oOo0O0Ooo . iIi1i111II - oOo / I1ii11iIi11i % oOo0O0Ooo
 II1 = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/script.module.simple.downloader' ) , '' )
 if os . path . exists ( II1 ) == True :
  for O0o00O0Oo0 , II1I , OoOo000oOo0oo in os . walk ( II1 ) :
   o00o0o0o = 0
   o00o0o0o += len ( OoOo000oOo0oo )
   if 22 - 22: I1i1III - I1i1IiI1
   if 7 - 7: iIi1i111II / OOooOOo * I1ii11iIi11i % ii - OOooOOo . Ii
   if o00o0o0o > 0 :
    if 36 - 36: OoOOOOO * OO0O0OoOO0 + i1I11i1I * OO0O0OoOO0 . Ii1I - iI11I1II1I1I
    oooOOOOO = xbmcgui . Dialog ( )
    if oooOOOOO . yesno ( "Delete Simple Downloader Cache Files" , str ( o00o0o0o ) + " files found" , "Do you want to delete them?" ) :
     if 14 - 14: I1i1IiI1 * OoOOOOO + Ii
     for oo0OOo0 in OoOo000oOo0oo :
      os . unlink ( os . path . join ( O0o00O0Oo0 , oo0OOo0 ) )
     for oOO in II1I :
      shutil . rmtree ( os . path . join ( O0o00O0Oo0 , oOO ) )
      if 84 - 84: OO0O0OoOO0 / IIiIiII11i
   else :
    pass
    if 86 - 86: oOo0O0Ooo
    if 97 - 97: IIiIiII11i
 iIiIii = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.itv/Images' ) , '' )
 if os . path . exists ( iIiIii ) == True :
  for O0o00O0Oo0 , II1I , OoOo000oOo0oo in os . walk ( iIiIii ) :
   o00o0o0o = 0
   o00o0o0o += len ( OoOo000oOo0oo )
   if 30 - 30: oOo
   if 33 - 33: Oo0o00 * i1I11i1I - o0o00Oo0O + oOo0O0Ooo / i1I11i1I
   if o00o0o0o > 0 :
    if 19 - 19: ooOoO0O00 % IIiIiII11i
    oooOOOOO = xbmcgui . Dialog ( )
    if oooOOOOO . yesno ( "Delete ITV Cache Files" , str ( o00o0o0o ) + " files found" , "Do you want to delete them?" ) :
     if 85 - 85: i1I11i1I - I11i % iIi1i111II - IIiIiII11i
     for oo0OOo0 in OoOo000oOo0oo :
      os . unlink ( os . path . join ( O0o00O0Oo0 , oo0OOo0 ) )
     for oOO in II1I :
      shutil . rmtree ( os . path . join ( O0o00O0Oo0 , oOO ) )
      if 56 - 56: I1i1III * Ii
   else :
    pass
    if 92 - 92: IIiIiII11i - o0o00Oo0O . Oo0o00
    if 59 - 59: OOooOOo
 iiII1iiI = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.movies4me/cache' ) , '' )
 if os . path . exists ( iIiIii ) == True :
  for O0o00O0Oo0 , II1I , OoOo000oOo0oo in os . walk ( iiII1iiI ) :
   o00o0o0o = 0
   o00o0o0o += len ( OoOo000oOo0oo )
   if 57 - 57: Ii - I1i1IiI1 / oOo / I11i * Ii * I11i
   if 28 - 28: ii % o0o00Oo0O - iIi1i111II / I11i / oOo0O0Ooo
   if o00o0o0o > 0 :
    if 41 - 41: IIiIiII11i * i1I11i1I / oO0o . OoOOOOO
    oooOOOOO = xbmcgui . Dialog ( )
    if oooOOOOO . yesno ( "Delete Movies4me Cache Files" , str ( o00o0o0o ) + " files found" , "Do you want to delete them?" ) :
     if 50 - 50: ii + iI11I1II1I1I / OoOOOOO / iIi1i111II . Ii . oOo
     for oo0OOo0 in OoOo000oOo0oo :
      os . unlink ( os . path . join ( O0o00O0Oo0 , oo0OOo0 ) )
     for oOO in II1I :
      shutil . rmtree ( os . path . join ( O0o00O0Oo0 , oOO ) )
      if 75 - 75: iI11I1II1I1I % oOo / iIi1i111II - OO0O0OoOO0 % Ii
   else :
    pass
    if 11 - 11: I1i1IiI1 . I1i1III
    if 87 - 87: iIi1i111II + iIi1i111II
 iiI11II1I = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.phstreams/Cache' ) , '' )
 if os . path . exists ( iIiIii ) == True :
  for O0o00O0Oo0 , II1I , OoOo000oOo0oo in os . walk ( iiI11II1I ) :
   o00o0o0o = 0
   o00o0o0o += len ( OoOo000oOo0oo )
   if 26 - 26: I1i1III . I1i1IiI1 * I11i
   if 21 - 21: IIiIiII11i
   if o00o0o0o > 0 :
    if 29 - 29: OOooOOo % I1i1III
    oooOOOOO = xbmcgui . Dialog ( )
    if oooOOOOO . yesno ( "Delete Phoenix Cache Files" , str ( o00o0o0o ) + " files found" , "Do you want to delete them?" ) :
     if 7 - 7: ooOoO0O00 / i1I11i1I / OO0O0OoOO0
     for oo0OOo0 in OoOo000oOo0oo :
      os . unlink ( os . path . join ( O0o00O0Oo0 , oo0OOo0 ) )
     for oOO in II1I :
      shutil . rmtree ( os . path . join ( O0o00O0Oo0 , oOO ) )
      if 97 - 97: oO0o + iI11I1II1I1I
   else :
    pass
    if 79 - 79: oOo + OoOOOOO - IIiIiII11i . I1ii11iIi11i
    if 26 - 26: i1I11i1I
 oo0o0o = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.spotitube/cache' ) , '' )
 if os . path . exists ( iIiIii ) == True :
  for O0o00O0Oo0 , II1I , OoOo000oOo0oo in os . walk ( oo0o0o ) :
   o00o0o0o = 0
   o00o0o0o += len ( OoOo000oOo0oo )
   if 25 - 25: i1I11i1I * Oo0o00 - OoOOOOO * Ii * oOo0O0Ooo * iIi1i111II
   if 56 - 56: ii . oOo0O0Ooo . IIiIiII11i % OO0O0OoOO0
   if o00o0o0o > 0 :
    if 59 - 59: oOo % I1ii11iIi11i - OoOOOOO + i1I11i1I
    oooOOOOO = xbmcgui . Dialog ( )
    if oooOOOOO . yesno ( "Delete YouTube Music Cache Files" , str ( o00o0o0o ) + " files found" , "Do you want to delete them?" ) :
     if 33 - 33: I1i1III + OOooOOo - Ii1I + iI11I1II1I1I % ooOoO0O00 * i1I11i1I
     for oo0OOo0 in OoOo000oOo0oo :
      os . unlink ( os . path . join ( O0o00O0Oo0 , oo0OOo0 ) )
     for oOO in II1I :
      shutil . rmtree ( os . path . join ( O0o00O0Oo0 , oOO ) )
      if 21 - 21: o0o00Oo0O * oOo % oO0o
   else :
    pass
    if 14 - 14: o0o00Oo0O / Oo0o00 / oOo + i1I11i1I - i1I11i1I
    if 10 - 10: o0o00Oo0O - Ii1I / Oo0o00 % OOooOOo / ii / I1i1III
 O000oOo = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.supercartoons/cache' ) , '' )
 if os . path . exists ( iIiIii ) == True :
  for O0o00O0Oo0 , II1I , OoOo000oOo0oo in os . walk ( O000oOo ) :
   o00o0o0o = 0
   o00o0o0o += len ( OoOo000oOo0oo )
   if 58 - 58: iIi1i111II
   if 94 - 94: ii - oOo % iIi1i111II - OO0O0OoOO0 / ooOoO0O00
   if o00o0o0o > 0 :
    if 5 - 5: ii % IIiIiII11i
    oooOOOOO = xbmcgui . Dialog ( )
    if oooOOOOO . yesno ( "Delete SuperCartoons Cache Files" , str ( o00o0o0o ) + " files found" , "Do you want to delete them?" ) :
     if 7 - 7: Ii - I1i1IiI1 % I1ii11iIi11i
     for oo0OOo0 in OoOo000oOo0oo :
      os . unlink ( os . path . join ( O0o00O0Oo0 , oo0OOo0 ) )
     for oOO in II1I :
      shutil . rmtree ( os . path . join ( O0o00O0Oo0 , oOO ) )
      if 76 - 76: oO0o * OO0O0OoOO0 % I1ii11iIi11i . Ii / ii
   else :
    pass
    if 85 - 85: ii . oO0o . oO0o
    if 70 - 70: I1i1IiI1
 O0O0OoO0 = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.tvonline.cc/cache' ) , '' )
 if os . path . exists ( iIiIii ) == True :
  for O0o00O0Oo0 , II1I , OoOo000oOo0oo in os . walk ( O0O0OoO0 ) :
   o00o0o0o = 0
   o00o0o0o += len ( OoOo000oOo0oo )
   if 60 - 60: oO0o / OO0O0OoOO0 / oOo0O0Ooo + OoOOOOO
   if 93 - 93: ii * I1i1III / o0o00Oo0O + I1i1III - iI11I1II1I1I
   if o00o0o0o > 0 :
    if 6 - 6: i1I11i1I - I1ii11iIi11i - I1i1IiI1 - o0o00Oo0O % ii
    oooOOOOO = xbmcgui . Dialog ( )
    if oooOOOOO . yesno ( "Delete TVonline Cache Files" , str ( o00o0o0o ) + " files found" , "Do you want to delete them?" ) :
     if 88 - 88: o0o00Oo0O / I11i * I11i . I11i . o0o00Oo0O
     for oo0OOo0 in OoOo000oOo0oo :
      os . unlink ( os . path . join ( O0o00O0Oo0 , oo0OOo0 ) )
     for oOO in II1I :
      shutil . rmtree ( os . path . join ( O0o00O0Oo0 , oOO ) )
      if 27 - 27: Ii % OO0O0OoOO0 + I1i1III . iIi1i111II
   else :
    pass
    if 9 - 9: oO0o
    if 43 - 43: I1i1III . iIi1i111II + oOo0O0Ooo * Ii
 ii1ii11Ii = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.youtube/kodion' ) , '' )
 if os . path . exists ( iIiIii ) == True :
  for O0o00O0Oo0 , II1I , OoOo000oOo0oo in os . walk ( ii1ii11Ii ) :
   o00o0o0o = 0
   o00o0o0o += len ( OoOo000oOo0oo )
   if 20 - 20: I1i1III . I1ii11iIi11i - I1i1IiI1 % I1i1IiI1 - oOo0O0Ooo * iIi1i111II
   if 80 - 80: IIiIiII11i / I11i . iIi1i111II . I11i
   if o00o0o0o > 0 :
    if 29 - 29: ii % IIiIiII11i % Ii - I1ii11iIi11i
    oooOOOOO = xbmcgui . Dialog ( )
    if oooOOOOO . yesno ( "Delete YouTube Cache Files" , str ( o00o0o0o ) + " files found" , "Do you want to delete them?" ) :
     if 5 - 5: Ii1I . IIiIiII11i . ooOoO0O00
     for oo0OOo0 in OoOo000oOo0oo :
      os . unlink ( os . path . join ( O0o00O0Oo0 , oo0OOo0 ) )
     for oOO in II1I :
      shutil . rmtree ( os . path . join ( O0o00O0Oo0 , oOO ) )
      if 35 - 35: I11i + oO0o - Ii1I
   else :
    pass
    if 24 - 24: IIiIiII11i
    if 23 - 23: I1ii11iIi11i - OO0O0OoOO0
    if 79 - 79: I1i1IiI1 . o0o00Oo0O - ooOoO0O00
 II1iII11 = xbmc . translatePath ( 'special://masterprofile/addon_data/plugin.video.genesis' )
 oooOOOOO = xbmcgui . Dialog ( )
 try :
  if oooOOOOO . yesno ( "Delete Genesis Cache Files" , "Do you want to delete cache" ) :
   iiiI1 = os . path . join ( II1iII11 , "cache.db" )
   os . unlink ( iiiI1 )
   if 13 - 13: Ii - IIiIiII11i - ii * Oo0o00
 except :
  pass
  if 50 - 50: I1ii11iIi11i - I11i % IIiIiII11i . o0o00Oo0O . OoOOOOO % IIiIiII11i
 oooOOOOO = xbmcgui . Dialog ( )
 oooOOOOO . ok ( "GenieTv" , "                               Finished Deleting Cache " , "                          [COLOR gold]Brought To You By GenieTv[/COLOR]" )
 if 18 - 18: I1i1IiI1 % ii + oO0o / I1i1IiI1
 if 37 - 37: ooOoO0O00 - I1i1III / i1I11i1I . IIiIiII11i % oOo
 if 39 - 39: I1i1III % Ii * oO0o
 if 23 - 23: iIi1i111II + oOo / Ii * I1ii11iIi11i . oO0o
 if 28 - 28: OO0O0OoOO0 - I11i
 if 92 - 92: I1ii11iIi11i % I11i - oOo / oOo / OOooOOo
 if 84 - 84: iIi1i111II
 if 4 - 4: i1I11i1I . Oo0o00 / I1i1III / OO0O0OoOO0 + IIiIiII11i
 if 32 - 32: ooOoO0O00 + iI11I1II1I1I . Ii1I . I1i1IiI1 - I1i1III
def OOOo ( url ) :
 print '###' + o0oOoO00o + ' - DELETING PACKAGES###'
 ii111 = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' , '' ) )
 try :
  for O0o00O0Oo0 , II1I , OoOo000oOo0oo in os . walk ( ii111 ) :
   o00o0o0o = 0
   o00o0o0o += len ( OoOo000oOo0oo )
   if 96 - 96: I11i - oOo0O0Ooo % OOooOOo + oO0o - i1I11i1I - i1I11i1I
   if 2 - 2: oOo % Ii
   if o00o0o0o > 0 :
    if 11 - 11: iI11I1II1I1I . Oo0o00 - I1ii11iIi11i / I1i1IiI1 + IIiIiII11i
    oooOOOOO = xbmcgui . Dialog ( )
    if oooOOOOO . yesno ( "Delete Package Cache Files" , str ( o00o0o0o ) + " files found" , "Do you want to delete them?" ) :
     if 29 - 29: I1i1IiI1 . Ii + ooOoO0O00 - I1i1III + o0o00Oo0O . oOo0O0Ooo
     for oo0OOo0 in OoOo000oOo0oo :
      os . unlink ( os . path . join ( O0o00O0Oo0 , oo0OOo0 ) )
     for oOO in II1I :
      shutil . rmtree ( os . path . join ( O0o00O0Oo0 , oOO ) )
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
 if 8 - 8: I11i
 if 78 - 78: ooOoO0O00 - I1ii11iIi11i
 if 48 - 48: I1i1III - ii + Oo0o00 % I11i - OOooOOo . oOo0O0Ooo
 if 42 - 42: Oo0o00
 if 70 - 70: I11i / I1i1IiI1 + OoOOOOO % oOo0O0Ooo % I1ii11iIi11i + oO0o
 if 80 - 80: iIi1i111II
 if 12 - 12: I1i1III
 if 2 - 2: ii
 if 100 - 100: I1ii11iIi11i / o0o00Oo0O * Ii * ii
def i1iiI ( url ) :
 print '###' + o0oOoO00o + ' - DELETING PACKAGES###'
 ii111 = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' , '' ) )
 try :
  for O0o00O0Oo0 , II1I , OoOo000oOo0oo in os . walk ( ii111 ) :
   o00o0o0o = 0
   o00o0o0o += len ( OoOo000oOo0oo )
   if 46 - 46: o0o00Oo0O % ii
   if 22 - 22: OO0O0OoOO0 + ii - OOooOOo - oO0o * Oo0o00 - OoOOOOO
   if o00o0o0o > 0 :
    if 99 - 99: oOo / oOo0O0Ooo . I1i1III - I1i1III * oOo0O0Ooo
    oooOOOOO = xbmcgui . Dialog ( )
    if oooOOOOO . yesno ( "Delete Package Cache Files" , str ( o00o0o0o ) + " files found" , "Do you want to delete them?" ) :
     if 24 - 24: I1i1IiI1 * oO0o - OoOOOOO / iI11I1II1I1I - I1ii11iIi11i . iIi1i111II
     for oo0OOo0 in OoOo000oOo0oo :
      os . unlink ( os . path . join ( O0o00O0Oo0 , oo0OOo0 ) )
     for oOO in II1I :
      shutil . rmtree ( os . path . join ( O0o00O0Oo0 , oOO ) )
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
 oo000oiIIIII ( url )
 return
 if 2 - 2: oOo - o0o00Oo0O - Ii1I / I1i1IiI1 * OOooOOo
 if 26 - 26: Ii1I + Oo0o00 - OoOOOOO + i1I11i1I % iIi1i111II
 if 84 - 84: I1i1IiI1 % I1i1III % o0o00Oo0O * I11i
 if 15 - 15: OoOOOOO - iI11I1II1I1I - IIiIiII11i - i1I11i1I % Ii1I
 if 80 - 80: i1I11i1I * OO0O0OoOO0 . ooOoO0O00 % I1i1III % Ii1I + oOo
 if 6 - 6: Ii1I . OoOOOOO . oO0o + i1I11i1I
 if 65 - 65: Ii1I / oOo
 if 23 - 23: iIi1i111II / iIi1i111II * I11i * iIi1i111II
 if 57 - 57: OO0O0OoOO0
 if 29 - 29: oOo0O0Ooo
def I1IIi11I1IiIi ( url , name ) :
 IIiooOooo0 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 OO0oO0 = os . path . join ( IIiooOooo0 , 'advancedsettings.xml' )
 oooOOOOO = xbmcgui . Dialog ( )
 I11iI1i11IiI = os . path . join ( IIiooOooo0 , 'advancedsettings.xml.bak' )
 if os . path . exists ( I11iI1i11IiI ) == False :
  if oooOOOOO . yesno ( "Back Up Original" , 'Have You Backed Up Your Original?' , '' , "[B][COLOR red]     AS YOU CANNOT GO BACK !!![/B][/COLOR]" ) :
   print '###' + o0oOoO00o + ' - ADVANCED XML###'
   IIiooOooo0 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
   OO0oO0 = os . path . join ( IIiooOooo0 , 'advancedsettings.xml' )
   try :
    os . remove ( OO0oO0 )
    print '=== GenieTv - REMOVING    ' + str ( OO0oO0 ) + '    ==='
   except :
    pass
   I11i1I1I = i1 . http_GET ( url ) . content
   Ii1ii111i1 = open ( OO0oO0 , "w" )
   Ii1ii111i1 . write ( I11i1I1I )
   Ii1ii111i1 . close ( )
   print '=== GenieTv - WRITING NEW    ' + str ( OO0oO0 ) + '    ==='
   oooOOOOO = xbmcgui . Dialog ( )
   oooOOOOO . ok ( o0oOoO00o , "       Done Adding new Advanced XML" )
 else :
  print '###' + o0oOoO00o + ' - ADVANCED XML###'
  IIiooOooo0 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
  OO0oO0 = os . path . join ( IIiooOooo0 , 'advancedsettings.xml' )
  try :
   os . remove ( OO0oO0 )
   print '=== GenieTv - REMOVING    ' + str ( OO0oO0 ) + '    ==='
  except :
   pass
  I11i1I1I = i1 . http_GET ( url ) . content
  Ii1ii111i1 = open ( OO0oO0 , "w" )
  Ii1ii111i1 . write ( I11i1I1I )
  Ii1ii111i1 . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( OO0oO0 ) + '    ==='
  oooOOOOO = xbmcgui . Dialog ( )
  oooOOOOO . ok ( o0oOoO00o , "       Done Adding new Advanced XML" )
 return
 if 78 - 78: i1I11i1I / OO0O0OoOO0 * I1i1III . iIi1i111II . OoOOOOO - Oo0o00
def I1IiI11 ( url , name ) :
 print '###' + o0oOoO00o + ' - CHECK ADVANCE XML###'
 IIiooOooo0 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 OO0oO0 = os . path . join ( IIiooOooo0 , 'advancedsettings.xml' )
 try :
  Ii1ii111i1 = open ( OO0oO0 ) . read ( )
  if 'zero' in Ii1ii111i1 :
   name = '0CACHE'
  elif 'tuxen' in Ii1ii111i1 :
   name = 'TUXENS'
  elif 'muckys' in Ii1ii111i1 :
   name = 'MUCKYS'
  elif 'p2p1' in Ii1ii111i1 :
   name = '1st P2P RECOMMENDED'
  elif 'p2p2' in Ii1ii111i1 :
   name = '2nd P2P RECOMMENDED'
  elif 'mikey' in Ii1ii111i1 :
   name = 'MIKEY1234'
 except :
  name = "NO ADVANCED"
 oooOOOOO = xbmcgui . Dialog ( )
 oooOOOOO . ok ( o0oOoO00o , "[COLOR yellow]YOU HAVE[/COLOR] " + name + "[COLOR yellow] XML SETTINGS SETUP[/COLOR]" )
 return
 if 3 - 3: o0o00Oo0O + o0o00Oo0O - o0o00Oo0O - o0o00Oo0O % ii + OoOOOOO
def IIi1iii ( url ) :
 print '###' + o0oOoO00o + ' - DELETING ADVANCE XML###'
 IIiooOooo0 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 OO0oO0 = os . path . join ( IIiooOooo0 , 'advancedsettings.xml' )
 try :
  os . remove ( OO0oO0 )
  oooOOOOO = xbmcgui . Dialog ( )
  print '=== GenieTv - DELETING    ' + str ( OO0oO0 ) + '    ==='
  oooOOOOO . ok ( o0oOoO00o , "       Remove Advanced Settings Sucessfull" )
 except :
  oooOOOOO = xbmcgui . Dialog ( )
  oooOOOOO . ok ( o0oOoO00o , "       No Advanced Settings To Remove" )
 return
 if 50 - 50: ii / oO0o % iI11I1II1I1I
 if 41 - 41: Ii1I % Ii1I + i1I11i1I . OO0O0OoOO0 % Oo0o00 * oOo
 if 57 - 57: I1i1III . Oo0o00 . IIiIiII11i % ii * o0o00Oo0O + iI11I1II1I1I
 if 94 - 94: ooOoO0O00 * oO0o * OOooOOo
 if 93 - 93: oOo / iIi1i111II * o0o00Oo0O
 if 17 - 17: oO0o / oOo % oOo0O0Ooo
 if 47 - 47: I1ii11iIi11i * oO0o / I11i * oOo0O0Ooo
 if 60 - 60: Ii1I / i1I11i1I . Ii / oO0o % IIiIiII11i
 if 6 - 6: OO0O0OoOO0 % I11i + Oo0o00
 if 91 - 91: I11i + o0o00Oo0O * OoOOOOO * i1I11i1I * Ii1I
def oO0oO0OoO00 ( url = 'http://www.iplocation.net/' , inc = 1 ) :
 Ii1 = re . compile ( "<td width='80'>(.+?)</td><td>(.+?)</td><td>(.+?)</td><td>.+?</td><td>(.+?)</td>" ) . findall ( i1 . http_GET ( url ) . content )
 for Oo0ooo00o0O0 , II1I1iI1i1IiI , IIii , OoO000Ooo in Ii1 :
  if inc < 2 : oooOOOOO = xbmcgui . Dialog ( ) ; oooOOOOO . ok ( 'Check My IP' , "[B][COLOR gold]Your IP Address is: [/COLOR][/B] %s" % Oo0ooo00o0O0 , '[B][COLOR gold]Your IP is based in: [/COLOR][/B] %s' % IIii , '[B][COLOR gold]Your Service Provider is:[/COLOR][/B] %s' % OoO000Ooo )
  inc = inc + 1
  if 66 - 66: Ii1I . I1ii11iIi11i / Ii1I + Ii1I . IIiIiII11i % oO0o
  if 61 - 61: Ii - ii
  if 90 - 90: oOo0O0Ooo
  if 4 - 4: iIi1i111II % oOo - iIi1i111II - I11i
  if 30 - 30: i1I11i1I
  if 34 - 34: OoOOOOO - IIiIiII11i - I11i + OO0O0OoOO0 + Oo0o00
  if 70 - 70: ii + oO0o * I1ii11iIi11i
  if 20 - 20: Ii - IIiIiII11i - oOo % OoOOOOO . oOo
  if 50 - 50: iI11I1II1I1I + Oo0o00 - I1i1IiI1 - ii
def oO00O0oO ( url , name ) :
 oooOOOOO = xbmcgui . Dialog ( )
 if oooOOOOO . yesno ( "GenieTv" , '                                    Install Latest .ini File' ) :
  print '###' + o0oOoO00o + ' - CUSTOM FTV INI###'
  IIiooOooo0 = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/plugin.video.GenieTv' , '' ) )
  OO0oO0 = os . path . join ( IIiooOooo0 , 'addons2.ini' )
  I11i1I1I = i1 . http_GET ( url ) . content
  Ii1ii111i1 = open ( OO0oO0 , "w" )
  Ii1ii111i1 . write ( I11i1I1I )
  Ii1ii111i1 . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( OO0oO0 ) + '    ==='
  oooOOOOO = xbmcgui . Dialog ( )
  oooOOOOO . ok ( o0oOoO00o , "                               Done Adding New .ini File" )
 return
 if 69 - 69: iIi1i111II + iIi1i111II * I1i1III * I1i1IiI1 + oOo0O0Ooo
def ii1i11iiII ( url , name ) :
 oooOOOOO = xbmcgui . Dialog ( )
 if oooOOOOO . yesno ( "GenieTv" , '                               Install Custom Settings' ) :
  print '###' + o0oOoO00o + ' - CUSTOM FTV SETTINGS###'
  IIiooOooo0 = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/plugin.video.GenieTv' , '' ) )
  OO0oO0 = os . path . join ( IIiooOooo0 , 'settings.xml' )
  I11i1I1I = i1 . http_GET ( url ) . content
  Ii1ii111i1 = open ( OO0oO0 , "w" )
  Ii1ii111i1 . write ( I11i1I1I )
  Ii1ii111i1 . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( OO0oO0 ) + '    ==='
  oooOOOOO = xbmcgui . Dialog ( )
  oooOOOOO . ok ( o0oOoO00o , "                               Done Adding New Settings" )
 return
 if 40 - 40: OO0O0OoOO0
 if 62 - 62: oOo / iIi1i111II
def O0o0O0OoOo0 ( ) :
 try :
  o00o0O0o0o0 = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/plugin.video.GenieTv' , '' ) )
  if os . path . exists ( o00o0O0o0o0 ) == True :
   oooOOOOO = xbmcgui . Dialog ( )
   if oooOOOOO . yesno ( "GenieTv" , "                               Delete FTV Guide Database" ) :
    Ii11i1IiII = os . path . join ( o00o0O0o0o0 , "source.db" )
    os . unlink ( Ii11i1IiII )
  oooOOOOO . ok ( "GenieTv" , "                                     FTV Database Reset" )
 except :
  oooOOOOO = xbmcgui . Dialog ( )
  oooOOOOO . ok ( o0oOoO00o , "               Error Deleting Database No Database To Delete" )
 return
 if 96 - 96: Ii - OOooOOo / OO0O0OoOO0 % ii / iI11I1II1I1I - iIi1i111II
 if 52 - 52: iI11I1II1I1I * OOooOOo + I11i . I1i1IiI1
 if 59 - 59: OO0O0OoOO0 . ooOoO0O00
 if 31 - 31: oOo0O0Ooo + oOo0O0Ooo
 if 11 - 11: i1I11i1I + OOooOOo % I11i * oO0o / i1I11i1I
def OO0oOO0O ( url ) :
 o0O = urllib2 . Request ( url )
 o0O . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
 O00oO = urllib2 . urlopen ( o0O )
 I11i1I1I = O00oO . read ( )
 O00oO . close ( )
 return I11i1I1I
 if 5 - 5: OO0O0OoOO0 / OoOOOOO % oOo . Ii % OOooOOo + OoOOOOO
 if 95 - 95: Ii1I
 if 48 - 48: I1i1IiI1
 if 14 - 14: iI11I1II1I1I / I11i * i1I11i1I
 if 35 - 35: iI11I1II1I1I
 if 34 - 34: oO0o % oOo0O0Ooo . I11i % oO0o % oO0o
 if 30 - 30: oOo0O0Ooo + oOo0O0Ooo
def OOO00o0O ( params ) :
 plugintools . log ( "freshstart.main_list " + repr ( params ) ) ; i111Iii11i1Ii = plugintools . message_yes_no ( o0oOoO00o , "Do you wish to restore your" , "Kodi configuration to default settings?" )
 if i111Iii11i1Ii :
  oo00000ooOooO = xbmcaddon . Addon ( id = o00 ) . getAddonInfo ( 'path' ) ; oo00000ooOooO = xbmc . translatePath ( oo00000ooOooO ) ;
  oo0o0OO00oOO = os . path . join ( oo00000ooOooO , ".." , ".." ) ; oo0o0OO00oOO = os . path . abspath ( oo0o0OO00oOO ) ; plugintools . log ( "freshstart.main_list xbmcPath=" + oo0o0OO00oOO ) ; IiiII1iIi = False
  try :
   for O0o00O0Oo0 , II1I , OoOo000oOo0oo in os . walk ( oo0o0OO00oOO , topdown = True ) :
    II1I [ : ] = [ oOO for oOO in II1I if oOO not in iiIIIII1i1iI ]
    for o0O0oo0OO0O in OoOo000oOo0oo :
     try : os . remove ( os . path . join ( O0o00O0Oo0 , o0O0oo0OO0O ) )
     except :
      if o0O0oo0OO0O not in [ "Addons15.db" , "MyVideos75.db" , "Textures13.db" , "xbmc.log" ] : IiiII1iIi = True
      plugintools . log ( "Error removing " + O0o00O0Oo0 + " " + o0O0oo0OO0O )
    for o0O0oo0OO0O in II1I :
     try : os . rmdir ( os . path . join ( O0o00O0Oo0 , o0O0oo0OO0O ) )
     except :
      if o0O0oo0OO0O not in [ "Database" , "userdata" ] : IiiII1iIi = True
      plugintools . log ( "Error removing " + O0o00O0Oo0 + " " + o0O0oo0OO0O )
   if not IiiII1iIi : plugintools . log ( "freshstart.main_list All user files removed, you now have a clean install" ) ; plugintools . message ( o0oOoO00o , "The process is complete, you're now back to a fresh Kodi configuration with GenieTv!" , "Please reboot your system or restart Kodi in order for the changes to be applied." )
   else : plugintools . log ( "freshstart.main_list User files partially removed" ) ; plugintools . message ( o0oOoO00o , "The process is complete, you're now back to a fresh Kodi configuration with GenieTv" , "Please reboot your system or restart Kodi in order for the changes to be applied." )
  except : plugintools . message ( o0oOoO00o , "Problem found" , "Your settings has not been changed" ) ; import traceback ; plugintools . log ( traceback . format_exc ( ) ) ; plugintools . log ( "freshstart.main_list NOT removed" )
  plugintools . add_item ( action = "" , title = "Now Exit Kodi" , folder = False )
 else : plugintools . message ( o0oOoO00o , "Your settings" , "has not been changed" ) ; plugintools . add_item ( action = "" , title = "Done" , folder = False )
 o0OooooOoOO ( )
 if 96 - 96: ii % OO0O0OoOO0 - ii % o0o00Oo0O
 if 21 - 21: OO0O0OoOO0
 if 1 - 1: I1ii11iIi11i . Ii
def ii1Ii ( ) :
 iiI11Ii1 = [ ]
 II11iII = sys . argv [ 2 ]
 if len ( II11iII ) >= 2 :
  O0O0OOo = sys . argv [ 2 ]
  ii1i111 = O0O0OOo . replace ( '?' , '' )
  if ( O0O0OOo [ len ( O0O0OOo ) - 1 ] == '/' ) :
   O0O0OOo = O0O0OOo [ 0 : len ( O0O0OOo ) - 2 ]
  O0ooOOO00000O = ii1i111 . split ( '&' )
  iiI11Ii1 = { }
  for OooOoOO0OO in range ( len ( O0ooOOO00000O ) ) :
   OOoo = { }
   OOoo = O0ooOOO00000O [ OooOoOO0OO ] . split ( '=' )
   if ( len ( OOoo ) ) == 2 :
    iiI11Ii1 [ OOoo [ 0 ] ] = OOoo [ 1 ]
    if 66 - 66: Ii1I / ooOoO0O00 * oOo0O0Ooo - OOooOOo + OoOOOOO
 return iiI11Ii1
 if 74 - 74: OO0O0OoOO0 / Oo0o00 / IIiIiII11i - OO0O0OoOO0 / OoOOOOO % I1i1IiI1
i1Iiiiii1II = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkbw==' )
iii11II1I = base64 . decodestring ( 'L3N0b3JhZ2UvZW11bGF0ZWQvMA==' )
i1iII1i = base64 . decodestring ( 'L2dlbmllLnR4dA==' )
Ii1I11Ii1iI = base64 . decodestring ( 'LmFyY2hpdGVjdHMueDEwaG9zdC5jb20vdGVzdC93aC50eHQ=' )
oooOO0OO0O = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby9maXhlcy9maXhlcy50eHQ=' )
OOOOOo00OOoO = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby9hcHBzL2FwcHMueG1s' )
o00oo00 = base64 . decodestring ( 'L2FkZG9ucy9uZXcudHh0' )
i111iii1I11I = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby92b2Qvdm9kLnBocA==' )
i11iiIII1Iii1 = base64 . decodestring ( 'L2FkZG9ucy9pcHR2LnR4dA==' )
iIIOoO = base64 . decodestring ( 'L2FkZG9ucy92aWRlby50eHQ=' )
iIO0 = base64 . decodestring ( 'L2FkZG9ucy9zcG9ydHMudHh0' )
III = base64 . decodestring ( 'L2FkZG9ucy9raWRzLnR4dA==' )
oOOOoooO = base64 . decodestring ( 'L2FkZG9ucy9tdXNpYy50eHQ=' )
o0oOOoOoOOo = base64 . decodestring ( 'L2FkZG9ucy9wcm9ncmFtcy50eHQ=' )
iI1i = base64 . decodestring ( 'L2FkZG9ucy94eHgudHh0' )
IIiII = base64 . decodestring ( 'L2FkZG9ucy9yZXBvLnR4dA==' )
O0O0ooOOO = base64 . decodestring ( 'L2FkZG9ucy9wYWNrcy50eHQ=' )
iii111iiI11I = base64 . decodestring ( 'L2FkZG9ucy9za2lucy50eHQ=' )
oOo00OooO0oO = base64 . decodestring ( 'L2FkZG9ucy9hcnQudHh0' )
OOoOO = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2dvdGhhbS50eHQ=' )
ii1i = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2hlbGl4LnR4dA==' )
oO00oOo0OOO = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2lzZW5nYXJkLnR4dA==' )
iIIIi = base64 . decodestring ( 'L2FkZG9ucy9SU1MudHh0' )
Oo0oOo000OoO0 = base64 . decodestring ( 'Q1VOVA==' )
def ooOOO0 ( name , url , mode , iconimage , fanart , description , showcontext = True , allinfo = { } ) :
 OooOooO0O0o0 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 OOO0o0 = True
 IIIIII111Ii = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 IIIIII111Ii . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 IIIIII111Ii . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  ii1IIi1IIIIi1 = [ ]
  if showcontext == 'fav' :
   ii1IIi1IIIIi1 . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in IIIii1II1II :
   ii1IIi1IIIIi1 . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fanart=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , urllib . quote_plus ( fanart ) , mode ) ) )
  IIIIII111Ii . addContextMenuItems ( ii1IIi1IIIIi1 )
 OOO0o0 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = OooOooO0O0o0 , listitem = IIIIII111Ii , isFolder = True )
 return OOO0o0
 if 35 - 35: oOo0O0Ooo
def OoOO ( name , url , mode , iconimage , fanart , description ) :
 OooOooO0O0o0 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 OOO0o0 = True
 IIIIII111Ii = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 IIIIII111Ii . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 IIIIII111Ii . setProperty ( "Fanart_Image" , fanart )
 OOO0o0 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = OooOooO0O0o0 , listitem = IIIIII111Ii , isFolder = False )
 return OOO0o0
 if 48 - 48: ii % ii - oO0o . OOooOOo
 if 22 - 22: oOo . Ii . ii . ooOoO0O00
O0O0OOo = ii1Ii ( )
IiIIIIIi = None
o0O0oo0OO0O = None
OooooO = None
oOOO00o000o = None
iIi11i1 = None
oOoO00oo0O = None
IIIIiI1iiI = None
if 13 - 13: I1i1IiI1 . oO0o
if 73 - 73: I1i1III * ii * I1i1IiI1 - Ii
try :
 IIIIiI1iiI = int ( O0O0OOo [ "fav_mode" ] )
except :
 pass
 if 58 - 58: I11i + OOooOOo - i1I11i1I
try :
 IiIIIIIi = urllib . unquote_plus ( O0O0OOo [ "url" ] )
except :
 pass
try :
 o0O0oo0OO0O = urllib . unquote_plus ( O0O0OOo [ "name" ] )
except :
 pass
try :
 oOOO00o000o = urllib . unquote_plus ( O0O0OOo [ "iconimage" ] )
except :
 pass
try :
 OooooO = int ( O0O0OOo [ "mode" ] )
except :
 pass
try :
 iIi11i1 = urllib . unquote_plus ( O0O0OOo [ "fanart" ] )
except :
 pass
try :
 oOoO00oo0O = urllib . unquote_plus ( O0O0OOo [ "description" ] )
except :
 pass
 if 82 - 82: I1i1III . iI11I1II1I1I / I1i1III / OoOOOOO % iI11I1II1I1I
 if 34 - 34: iIi1i111II
print str ( O0OoO000O0OO ) + ': ' + str ( IiiIII111iI )
print "Mode: " + str ( OooooO )
print "URL: " + str ( IiIIIIIi )
print "Name: " + str ( o0O0oo0OO0O )
print "IconImage: " + str ( oOOO00o000o )
if 99 - 99: IIiIiII11i
if 13 - 13: I1i1IiI1 - oOo + OO0O0OoOO0 % I1i1IiI1 . OO0O0OoOO0 - ooOoO0O00
def IiI111111IIII ( content , viewType ) :
 if 67 - 67: iIi1i111II . Ii + oOo . iI11I1II1I1I
 if content :
  xbmcplugin . setContent ( int ( sys . argv [ 1 ] ) , content )
 if o0oO0 . getSetting ( 'auto-view' ) == 'true' :
  xbmc . executebuiltin ( "Container.SetViewMode(%s)" % o0oO0 . getSetting ( viewType ) )
  if 28 - 28: oOo0O0Ooo + oOo0O0Ooo + Oo0o00
if oOOO00o000o == None : oOOO00o000o = ii11iIi1I
if iIi11i1 == None : iIi11i1 = i1iIIi1
if OooooO == None :
 OooOoooOo ( )
 if 22 - 22: Oo0o00
elif OooooO == 1 :
 iii1III1i ( IiIIIIIi )
 if 89 - 89: oOo . oO0o * ii + OOooOOo / o0o00Oo0O
elif OooooO == 44 :
 Ooo0O0 ( IiIIIIIi )
 if 60 - 60: I1i1IiI1
elif OooooO == 2 :
 iii1IIII1iii11I ( )
 if 97 - 97: Ii * iI11I1II1I1I / IIiIiII11i
elif OooooO == 3 :
 OOO0ooo ( )
 if 66 - 66: IIiIiII11i + OO0O0OoOO0 * OoOOOOO % I1i1IiI1 / ooOoO0O00 / iI11I1II1I1I
elif OooooO == 21 :
 iI1Ii11111iIi ( )
 if 62 - 62: OOooOOo + OoOOOOO * i1I11i1I + o0o00Oo0O / iIi1i111II + oOo
elif OooooO == 4 :
 i1OoOO ( )
 if 38 - 38: ooOoO0O00 / iI11I1II1I1I + OO0O0OoOO0
elif OooooO == 5 :
 iIIi1IIi ( IiIIIIIi )
 if 26 - 26: Ii1I . I1i1III % I11i
elif OooooO == 6 :
 OOOo ( IiIIIIIi )
 if 4 - 4: Oo0o00
elif OooooO == 7 :
 I1IIi11I1IiIi ( IiIIIIIi , o0O0oo0OO0O )
 if 80 - 80: I1ii11iIi11i . o0o00Oo0O % I11i . I11i
elif OooooO == 8 :
 I1IiI11 ( IiIIIIIi , o0O0oo0OO0O )
 if 52 - 52: oO0o % Ii . oOo % OOooOOo % ii
elif OooooO == 9 :
 FIXREPOSADDONS ( IiIIIIIi )
 if 5 - 5: OOooOOo / o0o00Oo0O / Ii
elif OooooO == 10 :
 oOOOoo00 ( )
 if 88 - 88: IIiIiII11i - OO0O0OoOO0 / ii
elif OooooO == 11 :
 IIi1iii ( IiIIIIIi )
 if 71 - 71: Ii1I
elif OooooO == 12 :
 oO0oO0OoO00 ( )
 if 19 - 19: I1ii11iIi11i - oO0o + Ii / iI11I1II1I1I
elif OooooO == 13 :
 ii1iiIiiiI11 ( )
 if 1 - 1: i1I11i1I % ooOoO0O00
elif OooooO == 14 :
 oo000oiIIIII ( IiIIIIIi )
 if 41 - 41: oO0o * oO0o / OO0O0OoOO0 + Ii1I . I11i
elif OooooO == 15 :
 o000O0OOoo ( )
 if 84 - 84: Ii + oO0o * oOo0O0Ooo + Ii1I / I1i1III
elif OooooO == 16 :
 oO00O0oO ( IiIIIIIi , o0O0oo0OO0O )
 if 80 - 80: Ii1I
elif OooooO == 17 :
 ii1i11iiII ( IiIIIIIi , o0O0oo0OO0O )
 if 67 - 67: IIiIiII11i
elif OooooO == 18 :
 O0o0O0OoOo0 ( )
 if 2 - 2: I11i - o0o00Oo0O * I1i1III % i1I11i1I
elif OooooO == 19 :
 Ii11 ( IiIIIIIi )
 if 64 - 64: ooOoO0O00 . oOo
elif OooooO == 40 :
 ooO00O00oOO ( o0O0oo0OO0O , IiIIIIIi , oOoO00oo0O )
 if 7 - 7: OoOOOOO . OO0O0OoOO0 - OO0O0OoOO0 / Oo0o00 % I1ii11iIi11i
elif OooooO == 42 :
 oOoOo00ooOooo ( o0O0oo0OO0O , IiIIIIIi , oOoO00oo0O )
 if 61 - 61: OoOOOOO - Ii1I / OO0O0OoOO0 % Ii1I + oO0o / I1ii11iIi11i
elif OooooO == 43 :
 OOOOoOO0O ( IiIIIIIi )
 if 10 - 10: Ii / OOooOOo
elif OooooO == 20 :
 iiI11iIi ( IiIIIIIi )
 if 27 - 27: oOo0O0Ooo / ii
elif OooooO == 22 :
 iiIi1111iiI1 ( IiIIIIIi )
 if 74 - 74: Ii1I % Oo0o00 - oO0o * I1i1IiI1 . ii * oO0o
elif OooooO == 23 :
 ooOOoo0 ( IiIIIIIi )
 if 99 - 99: OOooOOo . OO0O0OoOO0 - ii - o0o00Oo0O
elif OooooO == 24 :
 iiIIi1i111i ( IiIIIIIi )
 if 6 - 6: iIi1i111II
elif OooooO == 25 :
 O00O ( IiIIIIIi )
 if 3 - 3: o0o00Oo0O - Oo0o00 * I1i1III * iIi1i111II / I1i1III
elif OooooO == 26 :
 O0oOo0Ooo ( IiIIIIIi )
 if 58 - 58: I1i1III * iI11I1II1I1I + oOo . oOo
elif OooooO == 27 :
 II1111II ( IiIIIIIi )
 if 74 - 74: oOo - I11i * i1I11i1I % oOo
elif OooooO == 28 :
 oo0OOo0Oo00 ( IiIIIIIi )
 if 93 - 93: iI11I1II1I1I / OOooOOo % I1ii11iIi11i * Oo0o00 - oO0o - I11i
elif OooooO == 29 :
 i1I1IiIiiI1II ( IiIIIIIi )
 if 44 - 44: ii
elif OooooO == 30 :
 IIIiiI1 ( IiIIIIIi )
 if 82 - 82: OOooOOo . OOooOOo
elif OooooO == 31 :
 O0Oo ( IiIIIIIi )
 if 10 - 10: I1ii11iIi11i * Ii1I . OoOOOOO . ii . iIi1i111II * Ii1I
elif OooooO == 32 :
 OOOooo0OooOoO ( )
 if 80 - 80: Oo0o00 + I1i1IiI1 . Oo0o00 + iIi1i111II
elif OooooO == 33 :
 oO00OoOO ( )
 if 85 - 85: Ii . I1i1IiI1 + I1i1III / I1i1III
elif OooooO == 35 :
 I1iI ( IiIIIIIi )
 if 43 - 43: i1I11i1I . ii - IIiIiII11i
elif OooooO == 34 :
 o0OO000ooOo ( IiIIIIIi )
 if 90 - 90: oOo0O0Ooo - iI11I1II1I1I + Ii1I * iIi1i111II * OoOOOOO
elif OooooO == 36 :
 oOo0o0O ( IiIIIIIi )
 if 19 - 19: Oo0o00 * IIiIiII11i % I1ii11iIi11i - ooOoO0O00
elif OooooO == 37 :
 iiiI1ii11 ( IiIIIIIi )
 if 27 - 27: OOooOOo . o0o00Oo0O / Ii1I . iI11I1II1I1I
elif OooooO == 38 :
 Oo0OooO0 ( IiIIIIIi )
 if 15 - 15: I1i1III + oO0o % iI11I1II1I1I - Ii1I - ooOoO0O00 % I11i
elif OooooO == 41 :
 OOO00o0O ( O0O0OOo )
 if 54 - 54: i1I11i1I - IIiIiII11i . oOo + I1i1III
elif OooooO == 39 :
 Ii11iIi1iIiii ( IiIIIIIi )
 if 45 - 45: OoOOOOO + IIiIiII11i . OO0O0OoOO0 / Ii1I
elif OooooO == 45 :
 TEXTS ( )
 if 76 - 76: I1i1III + OO0O0OoOO0 - i1I11i1I * iI11I1II1I1I % ooOoO0O00
elif OooooO == 46 :
 iiiiI ( )
 if 72 - 72: oOo + IIiIiII11i . o0o00Oo0O - OO0O0OoOO0 / ii . Oo0o00
elif OooooO == 47 :
 GEVID ( )
 if 28 - 28: iI11I1II1I1I . o0o00Oo0O
elif OooooO == 48 :
 I1ii1II1iII ( o0O0oo0OO0O , IiIIIIIi , oOoO00oo0O )
 if 32 - 32: ii
elif OooooO == 49 :
 O0O0o0o0o ( )
 if 29 - 29: Ii1I
elif OooooO == 222 :
 iII1ii1 ( IiIIIIIi )
 if 41 - 41: I1i1III
elif OooooO == 333 :
 iIIiI1I1i1 ( IiIIIIIi )
 if 49 - 49: I1i1III % IIiIiII11i . I1i1III - I11i - I1i1IiI1 * i1I11i1I
 if 47 - 47: o0o00Oo0O . I11i / I1i1III * OO0O0OoOO0
elif OooooO == 1020 :
 OOo ( )
 if 63 - 63: Oo0o00 - OoOOOOO - OO0O0OoOO0 - oOo / OoOOOOO + oO0o
elif OooooO == 1021 :
 ANIMEEP ( )
 if 94 - 94: i1I11i1I / oOo0O0Ooo . IIiIiII11i
elif OooooO == 1022 :
 ANIMEPLAY ( IiIIIIIi )
 if 32 - 32: OoOOOOO . iIi1i111II % iIi1i111II . OOooOOo
elif OooooO == 1001 :
 i11ii11IiI1 ( )
 if 37 - 37: iIi1i111II + o0o00Oo0O + iIi1i111II . OO0O0OoOO0 . I11i
elif OooooO == 1005 :
 oooOo0OO ( )
 if 78 - 78: oOo0O0Ooo / I1i1IiI1 + I11i . I1ii11iIi11i / o0o00Oo0O
elif OooooO == 1007 :
 iII ( IiIIIIIi )
 if 49 - 49: Ii1I
elif OooooO == 1010 :
 O00O0ooo00OO0 ( IiIIIIIi )
 if 66 - 66: I11i . Ii1I
elif OooooO == 1011 :
 IiIIiIi11ii ( IiIIIIIi )
 if 18 - 18: I1ii11iIi11i + i1I11i1I
elif OooooO == 1012 :
 oo00OO ( IiIIIIIi )
 if 79 - 79: oO0o - o0o00Oo0O + IIiIiII11i % I1i1III . oOo0O0Ooo
elif OooooO == 1030 :
 II11IiIIiiiii ( )
 if 43 - 43: oOo0O0Ooo % Ii1I * I1i1III
elif OooooO == 1031 :
 oooOOo0o0OOO ( IiIIIIIi , oOOO00o000o )
 if 31 - 31: I1i1III / OO0O0OoOO0
elif OooooO == 1032 :
 o00OoOO00 ( IiIIIIIi )
 if 3 - 3: i1I11i1I
elif OooooO == 1006 :
 Parse . ParseURL ( IiIIIIIi )
 if 37 - 37: I1i1III * ii * I1i1IiI1 + I1ii11iIi11i . oOo0O0Ooo
elif OooooO == 2030 :
 Parse . addonParseURL ( IiIIIIIi )
 if 61 - 61: iIi1i111II . iIi1i111II
elif OooooO == 2031 :
 Parse . apkParseURL ( IiIIIIIi )
 if 17 - 17: IIiIiII11i / oOo
elif OooooO == 1002 :
 oooo ( IiIIIIIi )
 if 80 - 80: iIi1i111II * oO0o + I1i1III
elif OooooO == 1003 :
 I11iii1iIIIIi ( IiIIIIIi , oOOO00o000o )
 if 62 - 62: ii . o0o00Oo0O % I1ii11iIi11i
elif OooooO == 1004 :
 III1i1iiI1 ( IiIIIIIi )
 if 98 - 98: I11i * I1ii11iIi11i - I1i1III . oOo
elif OooooO == 1008 :
 oOoo00 ( )
 if 2 - 2: I1ii11iIi11i - oOo % iI11I1II1I1I
elif OooooO == 1009 :
 ii1iIi1 ( IiIIIIIi )
 if 88 - 88: Oo0o00 - oO0o
elif OooooO == 2001 :
 OOoO00OoOOO ( )
 if 79 - 79: OO0O0OoOO0
elif OooooO == 2002 :
 o0OOoOoo00 ( IiIIIIIi )
 if 45 - 45: IIiIiII11i + OO0O0OoOO0 . I1i1IiI1 . o0o00Oo0O * ooOoO0O00 - I1i1III
elif OooooO == 1013 :
 iIiiIiiIi ( )
elif OooooO == 10111113 :
 i1iiIIIi ( IiIIIIIi )
 if 48 - 48: Ii1I + I1ii11iIi11i
elif OooooO == 1014 :
 Oo0O0OooOooo0 ( )
 if 76 - 76: Ii1I
elif OooooO == 1015 :
 oO0o00OO ( IiIIIIIi )
 if 98 - 98: IIiIiII11i + oOo0O0Ooo - Ii1I . I1i1III
elif OooooO == 1016 :
 O0ooO ( IiIIIIIi , oOOO00o000o , o0O0oo0OO0O )
 if 51 - 51: I1i1III + Ii * oO0o % I1ii11iIi11i / oOo0O0Ooo - iI11I1II1I1I
elif OooooO == 1017 :
 oOOoO0o0oO ( )
 if 20 - 20: Oo0o00 . I1i1IiI1 . I1i1III + I1i1IiI1 - iIi1i111II * OoOOOOO
elif OooooO == 1018 :
 o0oO0O0o0O00O ( IiIIIIIi )
 if 82 - 82: oO0o
elif OooooO == 1023 :
 OO0oIII111i11IiI ( )
 if 78 - 78: IIiIiII11i / I1i1IiI1 - Ii + Ii1I * I1ii11iIi11i
elif OooooO == 1024 :
 o00oooo ( IiIIIIIi )
 if 17 - 17: OOooOOo
elif OooooO == 1025 :
 ooo0Oo00O ( IiIIIIIi )
 if 72 - 72: OO0O0OoOO0 . I1ii11iIi11i - Ii / oOo0O0Ooo
elif OooooO == 4001 :
 O0ooO0Oo00o ( )
 if 64 - 64: OoOOOOO
elif OooooO == 4002 :
 oOooOo0 ( )
 if 80 - 80: I11i % iI11I1II1I1I
elif OooooO == 4003 :
 O00oo0ooO ( )
 if 63 - 63: i1I11i1I * Ii
elif OooooO == 4004 :
 oOo00oOoO000 ( )
 if 86 - 86: I1i1IiI1 % I1i1IiI1 - OOooOOo + Oo0o00 / oOo0O0Ooo * ii
elif OooooO == 4005 :
 Ii1iI1I1 ( )
 if 26 - 26: IIiIiII11i * OO0O0OoOO0 + I11i / o0o00Oo0O + ooOoO0O00 - I1i1IiI1
elif OooooO == 4006 :
 oooOo0OOOoo0 ( )
 if 56 - 56: iIi1i111II
elif OooooO == 4007 :
 IiII111i1i11 ( )
 if 76 - 76: ooOoO0O00 % iI11I1II1I1I - I11i + i1I11i1I - I1i1IiI1
elif OooooO == 4008 :
 i111iIi1i1II1 ( )
 if 81 - 81: Ii1I + ii - iIi1i111II * o0o00Oo0O
elif OooooO == 4009 : OOooo0oOO0O ( )
elif OooooO == 4010 : iiI1ii11i1 ( )
elif OooooO == 3000 :
 ooO00OO ( )
 if 100 - 100: iI11I1II1I1I - OOooOOo
elif OooooO == 3001 :
 IiiI1I ( )
 if 28 - 28: I1ii11iIi11i . o0o00Oo0O . I1i1IiI1
elif OooooO == 3002 :
 I1iII1IIi1IiI ( IiIIIIIi )
 if 60 - 60: IIiIiII11i + Oo0o00 / OoOOOOO % ii - ooOoO0O00
elif OooooO == 3003 :
 iIi ( IiIIIIIi )
 if 57 - 57: oOo
elif OooooO == 3004 :
 o0ooOO00OO0o0O ( IiIIIIIi )
 if 99 - 99: I1ii11iIi11i + Oo0o00 % oOo - I11i
elif OooooO == 404 :
 OoI1 ( o0O0oo0OO0O , IiIIIIIi , oOOO00o000o )
 if 52 - 52: Ii1I
elif OooooO == 405 :
 I1I ( IiIIIIIi )
 if 93 - 93: OO0O0OoOO0 . Ii
elif OooooO == 7030 :
 i1IIiiIIIIi ( )
 if 24 - 24: iIi1i111II . oO0o + Oo0o00 . OoOOOOO - Ii1I % OO0O0OoOO0
elif OooooO == 7021 :
 o0OoOo0O00 ( o0O0oo0OO0O )
 if 49 - 49: o0o00Oo0O . I1ii11iIi11i / I1i1III
elif OooooO == 7022 :
 oOiiI1i11I ( o0O0oo0OO0O )
 if 29 - 29: Ii1I / OoOOOOO * o0o00Oo0O - Ii - oO0o + I1i1III
elif OooooO == 7000 :
 o0IiiIIII1I1i ( o0O0oo0OO0O , IiIIIIIi , img )
 if 86 - 86: oOo0O0Ooo / Ii1I * I1i1III % Ii
elif OooooO == 7050 :
 iiI1 ( IiIIIIIi )
 if 20 - 20: OO0O0OoOO0 . ii + OO0O0OoOO0 + oOo * Ii1I
elif OooooO == 7051 :
 iII1i1IIIii ( IiIIIIIi )
 if 44 - 44: Ii
elif OooooO == 7052 :
 OOOOiiI ( IiIIIIIi )
 if 69 - 69: iIi1i111II * o0o00Oo0O + Ii
elif OooooO == 7053 :
 o000Ooo00o00O ( IiIIIIIi )
 if 65 - 65: o0o00Oo0O / OO0O0OoOO0 . ooOoO0O00 * OO0O0OoOO0 / iI11I1II1I1I - OoOOOOO
elif OooooO == 7054 :
 CoolPlay ( IiIIIIIi )
 if 93 - 93: OOooOOo % Ii - I1i1III % oO0o
elif OooooO == 7060 :
 iIIII1Iii11 ( )
 if 55 - 55: I11i . Ii1I
elif OooooO == 7061 :
 IIiIIIi1iii1 ( IiIIIIIi )
 if 63 - 63: OoOOOOO
elif OooooO == 7063 :
 II1IIIi1i1I ( IiIIIIIi )
 if 79 - 79: Ii1I - OoOOOOO - I11i . iIi1i111II
elif OooooO == 7062 :
 oOO00 ( IiIIIIIi )
 if 65 - 65: Ii . oO0o % OO0O0OoOO0 + i1I11i1I - Ii
elif OooooO == 7064 :
 NATatozcat ( )
 if 60 - 60: Oo0o00
elif OooooO == 7067 :
 oO0o00 ( IiIIIIIi )
 if 14 - 14: I1ii11iIi11i % OoOOOOO * OO0O0OoOO0 - Ii / Ii1I * Ii
elif OooooO == 7066 :
 NATatozA ( IiIIIIIi )
 if 95 - 95: iI11I1II1I1I + OOooOOo . oOo0O0Ooo + OOooOOo * I1i1IiI1 + iIi1i111II
elif OooooO == 7065 :
 Oo0OOOO0oOoo0 ( IiIIIIIi )
 if 14 - 14: I1i1III - o0o00Oo0O
elif OooooO == 7070 :
 ooo00O0OOo ( )
 if 68 - 68: IIiIiII11i - Ii1I - oO0o * iI11I1II1I1I / oOo0O0Ooo * Ii1I
elif OooooO == 7071 :
 DIZIlist ( IiIIIIIi )
 if 45 - 45: Oo0o00 * I1i1IiI1 / iI11I1II1I1I / oOo0O0Ooo % IIiIiII11i
elif OooooO == 7072 :
 DIZIpull ( IiIIIIIi )
 if 49 - 49: I1i1III / OO0O0OoOO0 . OO0O0OoOO0 . OO0O0OoOO0 + Ii % I1i1IiI1
elif OooooO == 7073 :
 WATCHDIZI ( IiIIIIIi )
 if 7 - 7: i1I11i1I * oOo + OOooOOo
elif OooooO == 7002 :
 o0OoOo0o0OOoO0 ( )
 if 22 - 22: OO0O0OoOO0
elif OooooO == 7003 :
 ooOIIIi11i ( IiIIIIIi )
 if 48 - 48: Ii1I . oOo0O0Ooo
elif OooooO == 7004 :
 iI1III ( IiIIIIIi )
 if 73 - 73: o0o00Oo0O . Oo0o00 - ii % I1i1IiI1 % ooOoO0O00
elif OooooO == 7020 :
 IiiiI1I1iI11 ( IiIIIIIi )
 if 14 - 14: Oo0o00 + I1i1III * I1ii11iIi11i
elif OooooO == 7001 :
 o0oOO0 ( )
 if 49 - 49: I1ii11iIi11i
elif OooooO == 7010 :
 iioo ( IiIIIIIi )
 if 57 - 57: o0o00Oo0O * oOo - OO0O0OoOO0 - iI11I1II1I1I * OO0O0OoOO0
elif OooooO == 7011 :
 ii1111IIiI1 ( IiIIIIIi )
 if 9 - 9: i1I11i1I . I1i1IiI1
elif OooooO == 7012 :
 oO0o0 ( IiIIIIIi )
 if 23 - 23: o0o00Oo0O % ii - o0o00Oo0O . oOo0O0Ooo + Ii
elif OooooO == 7013 :
 cnfTVPlay2 ( IiIIIIIi )
elif OooooO == 7014 :
 CNF_Studio_Indexer . MV_Movies ( IiIIIIIi )
elif OooooO == 7015 :
 CNF_Studio_Indexer . Movie_ByYear ( IiIIIIIi )
elif OooooO == 7016 :
 CNF_Studio_Indexer . Resolve_CNF_Link ( o0O0oo0OO0O , IiIIIIIi , oOOO00o000o )
elif OooooO == 7017 :
 CNF_Studio_Indexer . Search_Movie ( )
elif OooooO == 7018 :
 II1III ( )
elif OooooO == 7019 :
 CNF_Studio_Indexer . List_Movies ( IiIIIIIi )
elif OooooO == 7020 :
 CNF_Studio_Indexer . Get_Movie_Page ( IiIIIIIi )
elif OooooO == 7024 :
 CNF_Studio_Indexer . Box_Office ( IiIIIIIi )
 if 96 - 96: oOo % o0o00Oo0O
elif OooooO == 8000 :
 OO0OOOOOo ( )
elif OooooO == 8001 :
 iI1ii ( )
elif OooooO == 8002 :
 i11IiIi ( )
elif OooooO == 8003 :
 iioO0o000oOO ( )
elif OooooO == 8004 :
 Oo00OOoO0oo ( )
elif OooooO == 8005 :
 oOO0O0O0OO00oo ( )
elif OooooO == 8006 :
 Oo0oOOO ( o0O0oo0OO0O , IiIIIIIi )
elif OooooO == 8030 :
 iIi1IiI ( IiIIIIIi )
elif OooooO == 8045 :
 ooO000OO ( IiIIIIIi )
elif OooooO == 8046 :
 i111IIiIiiI1 ( IiIIIIIi )
elif OooooO == 8047 :
 I1iIi1iIIIIiI ( IiIIIIIi )
elif OooooO == 8048 :
 o00OOo0o0O ( IiIIIIIi )
elif OooooO == 8049 :
 I111Iii1 ( IiIIIIIi )
elif OooooO == 8020 :
 Ooi11 ( )
elif OooooO == 8021 :
 O00oOoOo0ooO0O0oo ( IiIIIIIi )
elif OooooO == 8022 :
 ii11IiI ( IiIIIIIi )
elif OooooO == 8023 :
 I1iI1Ii11 ( IiIIIIIi )
elif OooooO == 8040 :
 I1I1i ( )
elif OooooO == 8041 :
 Oooo ( IiIIIIIi )
elif OooooO == 8042 :
 Ii11III ( IiIIIIIi )
elif OooooO == 8043 :
 yt . PlayVideo ( IiIIIIIi )
elif OooooO == 8044 :
 I1Ii1i11I1I ( IiIIIIIi )
elif OooooO == 8060 :
 O00Oo ( )
elif OooooO == 8061 :
 i1ii1II11I ( IiIIIIIi )
elif OooooO == 8064 :
 Oo0000OOO0 ( )
elif OooooO == 8065 :
 Ooo0O0OO ( IiIIIIIi )
elif OooooO == 8070 :
 Iiiii1Iii1I ( )
elif OooooO == 8071 :
 oOOOOoO ( IiIIIIIi )
elif OooooO == 7080 :
 IIiI ( IiIIIIIi )
elif OooooO == 8090 :
 Ii1I1iIIIiiii ( )
elif OooooO == 8091 :
 O0o ( IiIIIIIi )
elif OooooO == 8092 :
 Ii1iIiIi1I11 ( IiIIIIIi )
elif OooooO == 8081 :
 iIIIi1iii1I11 ( )
elif OooooO == 8062 :
 IIii1IIiiIii ( IiIIIIIi )
elif OooooO == 8063 :
 II1I1iIIiIIii ( IiIIIIIi )
elif OooooO == 8050 :
 IiOOoo0oO00oo00 ( )
elif OooooO == 8051 :
 O0 ( IiIIIIIi )
elif OooooO == 8052 :
 iiooO0o0oO ( IiIIIIIi )
elif OooooO == 8085 :
 i1IiIIi ( )
elif OooooO == 8086 :
 OOO00o0 ( IiIIIIIi )
elif OooooO == 8087 :
 IIII1ii1 ( IiIIIIIi )
elif OooooO == 8088 :
 OOO0O0OOo ( IiIIIIIi , o0O0oo0OO0O )
elif OooooO == 9000 :
 O00o00O ( )
elif OooooO == 1111 :
 I1Ii1iI1IiI1I ( )
elif OooooO == 9001 :
 oOo000O00O0 ( )
elif OooooO == 9002 :
 oooooO00OOO ( )
elif OooooO == 9003 :
 iiiIIiiIi ( )
elif OooooO == 50 :
 II1iiIiIiI ( IiIIIIIi )
elif OooooO == 9020 :
 champlist ( )
elif OooooO == 9021 :
 i1IoOo000Oo00o ( )
elif OooooO == 9022 :
 o0ooOOoOoOO ( )
elif OooooO == 9023 :
 iII11 ( )
elif OooooO == 9024 :
 i1iI11Ii1i ( IiIIIIIi )
elif OooooO == 9030 :
 Ii1i ( IiIIIIIi )
elif OooooO == 9031 :
 IIII1i ( IiIIIIIi )
elif OooooO == 9032 :
 oo0O00o0 ( IiIIIIIi )
elif OooooO == 9033 :
 Oo0oOooOooO ( IiIIIIIi )
elif OooooO == 7085 :
 I1111III111ii ( IiIIIIIi )
elif OooooO == 7086 :
 o0oOooO ( IiIIIIIi )
elif OooooO == 7087 :
 ii11iiII ( oOoO00oo0O )
elif OooooO == 9666 :
 i1iiI ( IiIIIIIi )
elif OooooO == 10100 : i1iI ( )
elif OooooO == 10105 : iiIIIIiii ( IiIIIIIi )
elif OooooO == 10106 : Ii1iiIi11111I ( IiIIIIIi )
elif OooooO == 10104 : oO00OoO0oo ( IiIIIIIi )
elif OooooO == 10107 : ii1O0Ooo0O ( )
elif OooooO == 10103 : iiiiI11iiIIi ( IiIIIIIi )
elif OooooO == 10108 : O00o0OO0OO0oo ( IiIIIIIi )
elif OooooO == 10107 : ii1O0Ooo0O ( )
elif OooooO == 10000 : Origin_Menu ( )
elif OooooO == 10001 : OOoOoo00Oo ( )
elif OooooO == 10002 : o0OO0oooo ( )
elif OooooO == 10003 : i1II1i ( )
elif OooooO == 10004 : o0oO00 ( IiIIIIIi )
elif OooooO == 10005 : oo0 ( )
elif OooooO == 10006 : iiii1 ( IiIIIIIi )
elif OooooO == 10007 : Oo00OO0OO ( IiIIIIIi , oOOO00o000o )
elif OooooO == 10008 : I1ii1i1iiii ( )
elif OooooO == 10009 : iIIi1 ( )
elif OooooO == 10010 : I1i1I11111iI1 ( IiIIIIIi )
elif OooooO == 10011 : O00oO000Oo0 ( IiIIIIIi )
elif OooooO == 10012 : o0i1I11iI1iiI ( IiIIIIIi )
elif OooooO == 10013 : i1Ii11ii1I ( IiIIIIIi )
elif OooooO == 10014 : O00o ( )
elif OooooO == 10015 : ooOO00o00 ( )
elif OooooO == 10016 : IIoO00OoOo ( IiIIIIIi )
elif OooooO == 10017 : OOoooOoO0Oo ( )
elif OooooO == 10018 : i11IiI1iiI11 ( )
elif OooooO == 10019 : Iiii1I ( )
elif OooooO == 10020 : Iiii1 ( )
elif OooooO == 10021 : OoO0Oo00 ( )
elif OooooO == 10022 : OooOOOoOoo0O0 ( IiIIIIIi )
elif OooooO == 10023 : IIiO0Oo ( o0O0oo0OO0O , IiIIIIIi )
elif OooooO == 10024 : OoOooOO0oOOo0O ( IiIIIIIi )
elif OooooO == 10025 : I11o0000o0Oo ( )
elif OooooO == 10026 : oO00o ( )
elif OooooO == 10027 : OoooooooO ( )
elif OooooO == 10028 : o00ooOOo ( )
elif OooooO == 10029 : iiiii1I1III1 ( )
elif OooooO == 423 : oOOooi1I1iIii11 ( IiIIIIIi )
elif OooooO == 426 : II1I1i1i1iii ( IiIIIIIi )
elif OooooO == 10030 : Izle_Films ( )
elif OooooO == 10031 : Latest_Izle_Movies ( )
elif OooooO == 10032 : Izle_Genres ( )
elif OooooO == 10033 : Izle_Pop_Movies ( )
elif OooooO == 10034 : Izle_Boxsets ( )
elif OooooO == 10035 : Izle_Search ( )
elif OooooO == 10036 : Izle_Genres_Movie ( IiIIIIIi )
elif OooooO == 10037 : Izle_Boxset_single ( IiIIIIIi )
elif OooooO == 10038 : Izle_IFRAME ( )
elif OooooO == 10039 : Izle_Boxsets_Next ( IiIIIIIi )
elif OooooO == 10040 : iiI ( )
elif OooooO == 10041 : OOoO0OOoO0ooo ( IiIIIIIi )
elif OooooO == 10042 : oooOo ( IiIIIIIi )
elif OooooO == 10043 : I1I1IIiiii1ii ( )
elif OooooO == 10044 : ooo0Oooooo ( IiIIIIIi )
elif OooooO == 10045 : Ii1I1i1ii1I1 ( o0O0oo0OO0O )
elif OooooO == 10046 : IiiIIiI1iI1 ( IiIIIIIi )
elif OooooO == 10047 : OooooOoO ( IiIIIIIi )
elif OooooO == 10048 : oO0O0o0O ( IiIIIIIi )
elif OooooO == 10049 : OoOOiI ( IiIIIIIi )
elif OooooO == 10050 : I1i11iIii1i1iI ( )
elif OooooO == 10051 : oO0OOo ( )
elif OooooO == 10052 : OoOOO0o0Ooo ( )
elif OooooO == 10053 : Addon ( IiIIIIIi )
elif OooooO == 10054 : iIIiiII11i1I1 ( IiIIIIIi , o0O0oo0OO0O )
elif OooooO == 10055 :
 o00O ( "addFavorite" )
 try :
  o0O0oo0OO0O = o0O0oo0OO0O . split ( '\\ ' ) [ 1 ]
 except :
  pass
 try :
  o0O0oo0OO0O = o0O0oo0OO0O . split ( '  - ' ) [ 0 ]
 except :
  pass
 O0OOO00OooO ( o0O0oo0OO0O , IiIIIIIi , oOOO00o000o , iIi11i1 , IIIIiI1iiI )
elif OooooO == 10056 :
 o00O ( "rmFavorite" )
 try :
  o0O0oo0OO0O = o0O0oo0OO0O . split ( '\\ ' ) [ 1 ]
 except :
  pass
 try :
  o0O0oo0OO0O = o0O0oo0OO0O . split ( '  - ' ) [ 0 ]
 except :
  pass
 OOo000o0 ( o0O0oo0OO0O )
elif OooooO == 10057 :
 o00O ( "getFavorites" )
 i1I ( )
elif OooooO == 10058 : o00O0 ( )
elif OooooO == 10059 : Donators_Guide ( )
elif OooooO == 10060 : iI1iIIIi1i ( )
elif OooooO == 10061 : i1i1IIii1i1 ( )
elif OooooO == 10062 : OO0I1i11iIIi ( o0O0oo0OO0O , IiIIIIIi , oOoO00oo0O )
elif OooooO == 10063 : xbmc . executebuiltin ( "XBMC.RunScript(" + O0o0Oo + ")" )
elif OooooO == 10064 : Ooo0o00o0o ( )
elif OooooO == 10065 : oO0o00ooO ( IiIIIIIi )
elif OooooO == 10066 : iIIII1iIIii ( IiIIIIIi )
elif OooooO == 10068 : iIi1Ii1i1iI ( IiIIIIIi )
elif OooooO == 10069 : ii1ii111 ( IiIIIIIi )
elif OooooO == 10070 : OOOOO0O00 ( IiIIIIIi )
elif OooooO == 10071 : Genie_Watch ( )
elif OooooO == 10072 : ooOoOo0 ( )
elif OooooO == 10073 : I1i11 ( IiIIIIIi )
elif OooooO == 10074 : ii1 ( IiIIIIIi )
elif OooooO == 10075 : II1I1I1Ii ( oOOO00o000o , o0O0oo0OO0O , IiIIIIIi )
elif OooooO == 10076 : i1i1ii ( IiIIIIIi )
elif OooooO == 10077 : OooooOoooO ( IiIIIIIi )
elif OooooO == 10078 : iII1i1 ( )
elif OooooO == 10079 : Genie_Watch_Tv_Shows ( )
elif OooooO == 10080 : Genie_Watch_Tv_Genre ( IiIIIIIi )
elif OooooO == 10081 : Genie_Watch_TV_PlayRun ( IiIIIIIi )
elif OooooO == 10082 : Genie_Watch_TV_Episodes ( IiIIIIIi , oOOO00o000o )
elif OooooO == 10083 : Genie_Watch_Tv_Recent ( IiIIIIIi )
elif OooooO == 10084 : O0Oo0oOOoooOOOOo ( )
elif OooooO == 10085 : iI1iIIiiii ( )
elif OooooO == 10086 : IIi1I11I1II ( )
elif OooooO == 20000 : iI1I1I11IiII ( )
elif OooooO == 20001 : IiI1IIIII1I ( )
elif OooooO == 20002 : oOO0o0oo0 ( IiIIIIIi )
elif OooooO == 20003 : OoIIi1iI ( IiIIIIIi )
elif OooooO == 20004 : OoO00o0 ( IiIIIIIi )
elif OooooO == 21004 : i11IiIIi11I ( )
elif OooooO == 21005 : o000o0O0Oo00 ( IiIIIIIi )
elif OooooO == 21006 : oooO ( IiIIIIIi )
elif OooooO == 21007 : I11Ii111I ( IiIIIIIi )
elif OooooO == 30000 : IiI1ii1Ii ( )
elif OooooO == 30001 : ii1ii11i111IiI ( )
elif OooooO == 10012 : Resolve ( IiIIIIIi )
elif OooooO == 30003 : oO00 ( )
elif OooooO == 30004 : Oo ( IiIIIIIi )
elif OooooO == 30005 : OO0O00o0 ( IiIIIIIi )
elif OooooO == 30006 : Oo0o0Oo0O ( )
elif OooooO == 30007 : II1Ii ( )
elif OooooO == 30008 : O0oOo ( IiIIIIIi )
elif OooooO == 30009 : O0OOOo ( IiIIIIIi )
elif OooooO == 30010 : i1iIi1111 ( IiIIIIIi )
elif OooooO == 30011 : OO0Ooo0 ( )
elif OooooO == 30012 : Oo0Oo00o00oO ( )
elif OooooO == 30013 : o0Oo ( )
elif OooooO == 30014 : Ii1iI ( )
elif OooooO == 30015 : iIiI1iiiI1ii ( IiIIIIIi , oOOO00o000o , iIi11i1 )
elif OooooO == 30016 : OO00o ( IiIIIIIi )
elif OooooO == 30019 : oo00OoO ( IiIIIIIi )
elif OooooO == 30017 : o0O0ooOOoO ( IiIIIIIi )
elif OooooO == 30018 : Ii1iIi111i1i1 ( IiIIIIIi )
elif OooooO == 30030 : OooOo ( )
elif OooooO == 30031 : oOo0 ( )
elif OooooO == 30032 : I1Ii11i ( )
elif OooooO == 30033 : I1iIiiiI1 ( )
elif OooooO == 30034 : OOO0O00Oo ( )
elif OooooO == 30035 : oo0OoOooo ( IiIIIIIi )
elif OooooO == 30036 : O00O00O000OOO ( IiIIIIIi )
elif OooooO == 30037 : iI ( IiIIIIIi )
elif OooooO == 30038 : II1i111 ( )
elif OooooO == 30039 : i1II1I ( )
elif OooooO == 50000 : i1Ii ( )
elif OooooO == 50001 : OoOooo ( )
elif OooooO == 50002 : OO0oo ( IiIIIIIi )
elif OooooO == 50003 : i1Ii1i1 ( oOoO00oo0O )
elif OooooO == 60000 : o0oO0 . openSettings ( sys . argv [ 0 ] )
elif OooooO == 60001 : i1iiIiI1Ii1i ( )
elif OooooO == 60002 : oo00O00oO000o ( o0O0oo0OO0O )
elif OooooO == 60003 : oOOoo ( o0O0oo0OO0O )
if 51 - 51: oOo0O0Ooo - OO0O0OoOO0 / Ii1I . Ii1I + Ii1I
if 87 - 87: IIiIiII11i . I1i1III * oO0o
xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
