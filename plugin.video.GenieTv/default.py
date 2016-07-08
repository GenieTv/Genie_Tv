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
IiiIII111iI = "2.9.0"
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
o0oOoO00o = "[COLORgreen]GenieTv[/COLOR]"
i1 = Net ( )
oOOoo00O0O = xbmcgui . Dialog ( )
i1111 = base64 . decodestring
i11 = o0oO0 . getSetting ( 'Build' )
I11 = o0oO0 . getSetting ( 'Local' )
Oo0o0000o0o0 = o0oO0 . getSetting ( 'Remote' )
oOo0oooo00o = o0oO0 . getSetting ( 'LocalM3u' )
oO0o0o0ooO0oO = o0oO0 . getSetting ( 'User' )
oo0o0O00 = o0oO0 . getSetting ( 'Pass' )
oO = o0oO0 . getSetting ( 'AdultPass' )
i1iiIIiiI111 = xbmcgui . Dialog ( )
oooOOOOO = xbmc . translatePath ( 'special://home/' )
i1iiIII111ii = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + I1i1iiI1 , 'fanart.jpg' ) )
i1iIIi1 = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + I1i1iiI1 , 'icon.png' ) )
ii11iIi1I = ( i1111 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vR2VuaWVBcnQvb3JpZ2luLnBuZw==' ) )
iI111I11I1I1 = xbmc . translatePath ( 'special://database' )
OOooO0OOoo = xbmc . translatePath ( 'special://home/userdata/addon_data/plugin.video.GenieTV' )
iIii1 = xbmc . translatePath ( 'special://thumbnails' ) ;
oOOoO0 = "GenieTv"
O0OoO000O0OO = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv' ) )
iiI1IiI = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/Change_Log_Temp' ) )
II = 'http://'
ooOoOoo0O = base64 . decodestring ( 'LnBocA==' )
OooO0 = base64 . decodestring ( 'aHR0cDovL2JhY2syYmFzaWNzYnVpbGQuY28udWsvdGVzdC8=' )
II11iiii1Ii = [ ]
OO0o = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/imports/tvGuide/ResetDatabase.py' ) )
Ooo = o0oO0 . getLocalizedString
O0o0Oo = CookieJar ( )
Oo00OOOOO = urllib2 . build_opener ( urllib2 . HTTPCookieProcessor ( O0o0Oo ) )
Oo00OOOOO . addheaders = [ ( 'User-Agent' , 'Mozilla/5.0' ) ]
O0O = int ( sys . argv [ 1 ] )
O00o0OO = xbmc . translatePath ( o0oO0 . getAddonInfo ( 'profile' ) . decode ( 'utf-8' ) )
I11i1 = os . path . join ( OOooO0OOoo , 'favorites' )
iIi1ii1I1 = OOooO0OOoo + '/addons.ini'
o0 = xbmc . translatePath ( 'special://home/userdata/' )
I11II1i = xbmc . translatePath ( 'special://home/userdatabroke/' )
IIIII = ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9QYW5zQm94L09SSUdJTlMv' ) )
ooooooO0oo = xbmc . translatePath ( os . path . join ( 'special://home/userdata/addon_data/script.ivueguide/master.db' ) )
IIiiiiiiIi1I1 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , 'favourites.xml' ) )
I1IIIii = xbmc . translatePath ( os . path . join ( 'special://home/userdata/addon_data/plugin.video.GenieTv/favorites' ) )
oOoOooOo0o0 = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/addon.xml' ) )
OOOO = xbmc . translatePath ( os . path . join ( 'special://home/addons/repository.GenieTv/addon.xml' ) )
if os . path . exists ( I11i1 ) == True :
 OOO00 = open ( I11i1 ) . read ( )
else : OOO00 = [ ]
iiiiiIIii = o0oO0 . getSetting ( 'debug' )
if os . path . exists ( OOooO0OOoo ) == False :
 os . makedirs ( OOooO0OOoo )
def O000OO0 ( url ) :
 I11iii1Ii = urllib2 . Request ( url )
 I11iii1Ii . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
 I1IIiiIiii = ''
 O000oo0O = ''
 try :
  I1IIiiIiii = urllib2 . urlopen ( I11iii1Ii )
  O000oo0O = I1IIiiIiii . read ( )
  I1IIiiIiii . close ( )
 except : pass
 if O000oo0O != '' :
  return O000oo0O
 else :
  O000oo0O = 'Failed'
  return O000oo0O
  if 66 - 66: OoOo00o / IIIii1II1II % iI1iI1I1i1I + Ii11Ii1I / o0oOO0O00o0O % OooO0OoOOOO
i1Ii = [ ]
o00OO00OoO = O000OO0 ( i1111 ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby8=' ) )
if o00OO00OoO != 'Failed' :
 i1Ii . append ( i1111 ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby8=' ) )
if not o00OO00OoO != 'Failed' :
 OOOO0OOoO0O0 = O000OO0 ( i1111 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20v' ) )
 if OOOO0OOoO0O0 != 'Failed' :
  i1Ii . append ( i1111 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20v' ) )
 if not OOOO0OOoO0O0 != 'Failed' :
  O0Oo000ooO00 = O000OO0 ( i1111 ( 'aHR0cDovL2hlcm92aXNpb24ueDEwaG9zdC5jb20vaGVyb3Zpc2lvbi54MTBob3N0LmNvbS9HZW5pZVR2L3JlZG8v' ) )
  if O0Oo000ooO00 != 'Failed' :
   i1Ii . append ( i1111 ( 'aHR0cDovL2hlcm92aXNpb24ueDEwaG9zdC5jb20vaGVyb3Zpc2lvbi54MTBob3N0LmNvbS9HZW5pZVR2L3JlZG8v' ) )
  if not O0Oo000ooO00 != 'Failed' :
   oO0 = O000OO0 ( i1111 ( 'aHR0cDovLzUuMTM1LjEuNDYvcmVkby8=' ) )
   if oO0 != 'Failed' :
    i1Ii . append ( i1111 ( 'aHR0cDovLzUuMTM1LjEuNDYvcmVkby8=' ) )
else :
 pass
Ii1iIiII1ii1 = ( str ( i1Ii ) ) . replace ( '[\'' , '' ) . replace ( '\']' , '' )
ooOooo000oOO = Ii1iIiII1ii1 + 'GenieArt/'
if 59 - 59: IIIi + O0OoO - iI1iI1I1i1I % Ii
if 61 - 61: IIiIiII11i * OoOo00o % I1ii11iIi11i
def O0O0O0OoOO ( ) :
 if not os . path . exists ( IiII ) :
  oOOoo00O0O . ok ( "[COLOR=white]Incompatible[/COLOR]" , "Unfortunately GenieTv will only work with" , 'its official repo please install from trusted source' , '' )
  o0ooO = 'genie tv repo not being installed '
  O0o0O00Oo0o0 ( o0ooO )
 else :
  O00O0oOO00O00 ( )
  if 11 - 11: OooO0OoOOOO . Ii1I
def O00O0oOO00O00 ( ) :
 if 92 - 92: o0oOO0O00o0O . IIIi
 i1i = iiI111I1iIiI ( i1111 ( 'aHR0cHM6Ly9naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvYmxvYi9tYXN0ZXIvVmVyc2lvbl9Mb2cudHh0' ) )
 IIIi1I1IIii1II = open ( oOoOooOo0o0 ) . read ( )
 O0 = open ( OOOO ) . read ( )
 if 25 - 25: Ii1I
 Ii1i = re . compile ( 'version="(.+?)" provider' ) . findall ( IIIi1I1IIii1II )
 I1 = re . compile ( 'version="(.+?)" provider-name' ) . findall ( O0 )
 iiIii = re . compile ( 'GENIE TV ADDON - Version = &quot;(.+?)&quot;' ) . findall ( i1i )
 ooo0O = re . compile ( 'GENIE TV REPO - Version = &quot;(.+?)&quot;' ) . findall ( i1i )
 for oOoO0o00OO0 in Ii1i :
  i1I1ii = oOoO0o00OO0
  for oOOo0 in iiIii :
   if not oOOo0 == i1I1ii :
    Oo0oO0ooo . create ( 'Incorrect Addon Version' , 'Downloading Correct Version' , )
    xbmc . sleep ( 1000 )
    Oo0oO0ooo . close
    oo00O00oO ( )
   if oOOo0 == i1I1ii :
    iIiIIIi
 for ooo00OOOooO in I1 :
  O00OOOoOoo0O = ooo00OOOooO
  for O000OOo00oo in ooo0O :
   if not O000OOo00oo == O00OOOoOoo0O :
    Oo0oO0ooo . create ( 'Incorrect Repo Installed' , 'Installing Correct Version' , '' )
    xbmc . sleep ( 1000 )
    Oo0oO0ooo . close
    oo0OOo ( )
   if O000OOo00oo == O00OOOoOoo0O :
    xbmc . sleep ( 100 )
    iIiIIIi
def ooOOO00Ooo ( ) :
 O0O0O0OoOO ( )
 IiIIIi1iIi ( )
 ooOOoooooo ( '[COLORgreen]Force Genie Update Kodi 16+[/COLOR]' , i1111 ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVwby9yZXBvc2l0b3J5LkdlbmllVHYtMC4xLjAuemlw' ) , 10085 , ooOooo000oOO + 'updategenie.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'My Build' ) == 'true' :
  II1I ( '[COLORgreen]WIZARD[/COLOR]' , str ( Ii1iIiII1ii1 ) , 4001 , ooOooo000oOO + 'MB.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Streams' ) == 'true' :
  II1I ( '[COLORgreen]STREAMS[/COLOR]' , str ( Ii1iIiII1ii1 ) , 4002 , ooOooo000oOO + 'streams.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Music' ) == 'true' :
  II1I ( '[COLORgreen]Music[/COLOR]' , str ( Ii1iIiII1ii1 ) , 4003 , ooOooo000oOO + 'MUSIC.png' , i1iiIII111ii , '' )
  if 84 - 84: OooO0OoOOOO . Ii . OooO0OoOOOO * Ii1I - iI1iI1I1i1I
 if o0oO0 . getSetting ( 'Builders Toolbox' ) == 'true' :
  II1I ( '[COLORgreen]BUILDERS TOOLBOX[/COLOR]' , str ( Ii1iIiII1ii1 ) , 32 , ooOooo000oOO + 'builderstoolbox.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Source List' ) == 'true' :
  II1I ( '[COLORgreen]SOURCE LIST[/COLOR]' , str ( Ii1iIiII1ii1 ) , 46 , ooOooo000oOO + 'sources.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Maintainance' ) == 'true' :
  II1I ( '[COLORgreen]MAINTENANCE[/COLOR]' , str ( Ii1iIiII1ii1 ) , 3 , ooOooo000oOO + 'MAIN6.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Addons' ) == 'true' :
  II1I ( '[COLORgreen]ADDONS[/COLOR]' , '' , 10050 , ooOooo000oOO + 'ADDONS.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'APK Tool' ) == 'true' :
  II1I ( '[COLORgreen]APK TOOL[/COLOR]' , str ( Ii1iIiII1ii1 ) , 30039 , ooOooo000oOO + 'APK.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Rss Feed' ) == 'true' :
  II1I ( '[COLORgreen]GenieTv RSS Feed[/COLOR]' , str ( Ii1iIiII1ii1 ) , 39 , ooOooo000oOO + 'RSS.png' , i1iiIII111ii , '' )
  if 42 - 42: Ii
  if 33 - 33: o0oOO0O00o0O - o0o00Oo0O * ooOoO0O00 * I11i - I1ii11iIi11i
 iiIiI ( 'movies' , 'MAIN' )
 if 91 - 91: o0oOO0O00o0O % ooOoO0O00 % iI11I1II1I1I
def IIi1I11I1II ( ) :
 O0O0O0OoOO ( )
 II1I ( '[COLORgreen]BACKUP MY BUILD[/COLOR]' , str ( Ii1iIiII1ii1 ) , 10060 , ooOooo000oOO + 'MB.png' , i1iiIII111ii , '' )
 II1I ( '[COLORgreen]RESTORE MY BUILD[/COLOR]' , str ( Ii1iIiII1ii1 ) , 49 , ooOooo000oOO + 'MB.png' , i1iiIII111ii , '' )
 II1I ( '[COLORgreen]WIPE GENIE[/COLOR]' , str ( Ii1iIiII1ii1 ) , 41 , ooOooo000oOO + 'wipegenie.png' , i1iiIII111ii , '' )
 if 63 - 63: ii - oO0o . IIiIiII11i / I11i . OOooOOo / o0o00Oo0O
 II1I ( '[COLORgreen]Genie BUILDS[/COLOR]' , str ( Ii1iIiII1ii1 ) , 44 , ooOooo000oOO + 'WISHESAN.png' , i1iiIII111ii , '' )
 iiIiI ( 'movies' , 'MAIN' )
def o0OOOO00O0Oo ( ) :
 O0O0O0OoOO ( )
 if oO == '5knuckleshuffle' :
  II1I ( '[COLORgreen]XVID[/COLOR]' , str ( Ii1iIiII1ii1 ) , 10100 , ooOooo000oOO + 'JIZBOX.png' , i1iiIII111ii , '' )
  II1I ( '[COLORgreen]ADULT CHANNELS[/COLOR]' , str ( Ii1iIiII1ii1 ) , 30033 , ooOooo000oOO + 'adult.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Favourites' ) == 'true' :
  II1I ( '[COLORgreen]FAVOURITES[/COLOR]' , str ( Ii1iIiII1ii1 ) , 10057 , ooOooo000oOO + 'FAVORITES.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Search' ) == 'true' :
  II1I ( '[COLORgreen]SEARCH[/COLOR]' , str ( Ii1iIiII1ii1 ) , 9000 , ooOooo000oOO + 'search.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'TV GUIDE' ) == 'true' :
  ooOOoooooo ( '[COLORgreen]TV GUIDE[/COLOR]' , '' , 10063 , ooOooo000oOO + 'GTVIPTV.png' , i1iiIII111ii , '' )
 II1I ( '[COLORgreen]STREAM TEAM[/COLOR]' , str ( Ii1iIiII1ii1 ) , 4006 , ooOooo000oOO + 'streamteam.png' , i1iiIII111ii , '' )
 II1I ( '[COLORgreen]24/7 STREAMS[/COLOR]' , '' , 30030 , ooOooo000oOO + '247.png' , i1iiIII111ii , '' )
 II1I ( '[COLORgreen]MOVIES[/COLOR]' , str ( Ii1iIiII1ii1 ) , 4004 , ooOooo000oOO + 'MOVIESv.png' , i1iiIII111ii , '' )
 II1I ( '[COLORgreen]TV SHOWS[/COLOR]' , str ( Ii1iIiII1ii1 ) , 4005 , ooOooo000oOO + 'TVSHOWSv.png' , i1iiIII111ii , '' )
 II1I ( '[COLORgreen]KIDS[/COLOR]' , str ( Ii1iIiII1ii1 ) , 4007 , ooOooo000oOO + 'KIDSv.png' , i1iiIII111ii , '' )
 II1I ( '[COLORgreen]NEWS[/COLOR]' , str ( Ii1iIiII1ii1 ) , 30032 , ooOooo000oOO + 'NEWS.png' , i1iiIII111ii , '' )
 II1I ( '[COLORgreen]GenieTv TUTORIALS[/COLOR]' , ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9pVHZfU3RyZWFtcy9UVVRTL21haW4ucGhw' ) ) , 1016 , ooOooo000oOO + 'TUTS.png' , i1iiIII111ii , '' )
 II1I ( '[COLORgreen]HOBBIES[/COLOR]' , str ( Ii1iIiII1ii1 ) , 4008 , ooOooo000oOO + 'hobbies.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'YOUTUBE' ) == 'true' :
  II1I ( '[COLORgreen]SEARCH YOUTUBE[/COLOR]' , str ( Ii1iIiII1ii1 ) , 10064 , ooOooo000oOO + 'youtube.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'REQUESTS' ) == 'true' :
  II1I ( '[COLORgreen]REQUESTS[/COLOR]' , str ( Ii1iIiII1ii1 ) + ( i1111 ( 'L1JFUVVFU1RTLnBocA==' ) ) , 10066 , ooOooo000oOO + 'requests.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Stand Up' ) == 'true' :
  II1I ( '[COLORgreen]STAND UP[/COLOR]' , '' , 10003 , ooOooo000oOO + 'ORIGINSTANDUP.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Documentaries' ) == 'true' :
  II1I ( '[COLORgreen]DOCUMENTARIES[/COLOR]' , str ( Ii1iIiII1ii1 ) , 8040 , ooOooo000oOO + 'documentary.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Disclose' ) == 'true' :
  II1I ( '[COLORgreen]DISCLOSE TV[/COLOR]' , str ( Ii1iIiII1ii1 ) , 7001 , ooOooo000oOO + 'disclose.png' , i1iiIII111ii , '' )
  if 48 - 48: o0o00Oo0O
  if 11 - 11: iI1iI1I1i1I + ii - oO0o / I11i + I1ii11iIi11i . IIiIiII11i
 if o0oO0 . getSetting ( 'Playlist Loader' ) == 'true' :
  II1I ( '[COLORgreen]PLAYLIST LOADER[/COLOR]' , str ( Ii1iIiII1ii1 ) , 3000 , ooOooo000oOO + 'loader.png' , i1iiIII111ii , '' )
  if 41 - 41: Ii11Ii1I - o0o00Oo0O - o0o00Oo0O
  if 68 - 68: IIIii1II1II % IIIi
  if 88 - 88: iI11I1II1I1I - O0OoO + IIIii1II1II
  if 40 - 40: oOo0O0Ooo * Ii11Ii1I + IIIii1II1II % o0oOO0O00o0O
  if 74 - 74: OoOo00o - I1ii11iIi11i + ii + IIIi / OOooOOo
  if 23 - 23: o0o00Oo0O
  if 85 - 85: Ii11Ii1I
  if 84 - 84: oOo0O0Ooo . iI11I1II1I1I % ii + Ii11Ii1I % ii % oO0o
  if 42 - 42: oO0o / iI1iI1I1i1I / I11i + o0oOO0O00o0O / OOooOOo
  if 84 - 84: O0OoO * IIiIiII11i + I1ii11iIi11i
  if 53 - 53: o0oOO0O00o0O % IIiIiII11i . OooO0OoOOOO - iI11I1II1I1I - OooO0OoOOOO * IIiIiII11i
  if 77 - 77: iI11I1II1I1I * oO0o
 iiIiI ( 'movies' , 'MAIN' )
 if 95 - 95: oOo0O0Ooo + Ii
def IiIIIi1iIi ( ) :
 if not os . path . exists ( iiI1IiI ) :
  I1Ii ( 'Change Log 08/07/16 - v2.9.0' , 'Silent Hunter and Redemption Streams added to search function, Quick Silver music source in music section, live music channels renewed, Discovery section fixed and updated with new content, Popcorn Box in movies section fixed and updated, Disclose Tv Fixed and updated' )
  os . makedirs ( iiI1IiI )
  if 94 - 94: Ii11Ii1I - IIiIiII11i . IIIii1II1II % iI1iI1I1i1I . Ii + o0o00Oo0O
  if 26 - 26: iI1iI1I1i1I - iI11I1II1I1I - oOo0O0Ooo / oO0o . OOooOOo % iI11I1II1I1I
def OO ( ) :
 O0O0O0OoOO ( )
 II1I ( '[COLORgreen]SEARCH MOVIES[/COLOR]' , str ( Ii1iIiII1ii1 ) , 9001 , ooOooo000oOO + 'search.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Popcorn Box' ) == 'true' :
  II1I ( '[COLORgreen]POPCORN BOX[/COLOR]' , str ( Ii1iIiII1ii1 ) , 7061 , ooOooo000oOO + 'popcorn.png' , i1iiIII111ii , '' )
 II1I ( '[COLORgreen]Film Trailers[/COLOR]' , i1111 ( 'aHR0cDovL3RoZW1vdmllYm94Lm5ldC9leHBsb3Jl' ) , 10068 , ooOooo000oOO + 'movietrailers.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'CLASSIC MOVIES' ) == 'true' :
  II1I ( '[COLORgreen]CLASSIC MOVIES[/COLOR]' , '' , 8060 , ooOooo000oOO + 'classicmovies.png' , i1iiIII111ii , '' )
 iiIiI ( 'movies' , 'MAIN' )
def iIiIIi1 ( ) :
 O0O0O0OoOO ( )
 if o0oO0 . getSetting ( 'G-tv' ) == 'true' :
  II1I ( '[COLORgreen]G-Tv PRIVATE LIST[/COLOR]' , '' , 10058 , ooOooo000oOO + 'GTVIPTV.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'TV GUIDE' ) == 'true' :
  ooOOoooooo ( '[COLORgreen]TV GUIDE[/COLOR]' , '' , 10063 , ooOooo000oOO + 'GTVIPTV.png' , i1iiIII111ii , '' )
 ooOOoooooo ( '[COLORgreen]Link GTV Donators Username and Password to Guide[/COLOR]' , '' , 4010 , ooOooo000oOO + 'GTVIPTV.png' , i1iiIII111ii , '' )
 if 7 - 7: O0OoO - I1ii11iIi11i - OoOo00o + O0OoO
 if 26 - 26: Ii11Ii1I
def I11iiI1i1 ( ) :
 O0O0O0OoOO ( )
 II1I ( '[COLORgreen]SEARCH SERIES[/COLOR]' , str ( Ii1iIiII1ii1 ) , 9002 , ooOooo000oOO + 'search.png' , i1iiIII111ii , '' )
 if 47 - 47: o0oOO0O00o0O - Ii11Ii1I . IIiIiII11i + ii . Ii
 if 94 - 94: I11i * Ii11Ii1I / I1ii11iIi11i / Ii11Ii1I
 if o0oO0 . getSetting ( 'Watch Series' ) == 'true' :
  II1I ( '[COLORgreen]WATCH SERIES[/COLOR]' , '' , 10040 , ooOooo000oOO + 'WATCHSERIES.png' , i1iiIII111ii , '' )
 II1I ( '[COLORgreen]iWATCH SERIES[/COLOR]' , '' , 8020 , ooOooo000oOO + 'iwatch.png' , i1iiIII111ii , '' )
 if 87 - 87: I1ii11iIi11i . OooO0OoOOOO
 if 75 - 75: O0OoO + OOooOOo + I11i * iI1iI1I1i1I % OoOo00o . o0oOO0O00o0O
 if o0oO0 . getSetting ( 'CLASSIC TV' ) == 'true' :
  II1I ( '[COLORgreen]CLASSIC TV[/COLOR]' , str ( Ii1iIiII1ii1 ) , 8064 , ooOooo000oOO + 'classictv.png' , i1iiIII111ii , '' )
 II1I ( '[COLORgreen]TV Show Trailers[/COLOR]' , i1111 ( 'aHR0cHM6Ly93d3cueW91dHViZS5jb20vd2F0Y2g/dj03WkZJUzJBcUF6OCZsaXN0PVBMM2t4NWgyVHJZR3dwVzBWYk5lbnBqLUJLTUJUR2dKUEU=' ) , 10069 , ooOooo000oOO + 'tvtrailers.png' , i1iiIII111ii , '' )
 if 55 - 55: IIIii1II1II . oOo0O0Ooo
 iiIiI ( 'movies' , 'MAIN' )
def oOo0O0o00o ( ) :
 O0O0O0OoOO ( )
 if o0oO0 . getSetting ( 'Silent Hunter' ) == 'true' :
  II1I ( '[COLORgreen]SILENT HUNTER[/COLOR]' , ( i1111 ( 'aHR0cDovLzUuMTM1LjIwNy45Ni8=' ) ) , 10084 , ooOooo000oOO + 'SILENTHUNTER.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'The Reaper' ) == 'true' :
  II1I ( '[COLORgreen]THE REAPER[/COLOR]' , ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9UaGVfUmVhcGVyL21haW4ucGhw' ) ) , 1016 , ooOooo000oOO + 'reap.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Pandoras Box' ) == 'true' :
  II1I ( '[COLORgreen]PANDORAS BOX[/COLOR]' , str ( Ii1iIiII1ii1 ) , 10025 , ooOooo000oOO + 'PANDORASBOX.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Redemption Streams' ) == 'true' :
  II1I ( '[COLORgreen]Redemption Streams[/COLOR]' , ( i1111 ( 'aHR0cDovL3JlZGVtcHRpb25idWlsZC4xNm1iLmNvbS9SZWRlbXB0aW9uL21haW4ucGhw' ) ) , 1016 , ooOooo000oOO + 'redemption.png' , i1iiIII111ii , '' )
 II1I ( '[COLORgreen]DoJo STREAMS[/COLOR]' , ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9kb2pvc3RyZWFtcy9tYWluLnBocA==' ) ) , 1016 , ( i1111 ( 'SHR0cDovL2dlbmlldHZjdW50cy5jby51ay9kb2pvc3RyZWFtcy9kb2pvbG9nby5wbmc=' ) ) , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Scooby Streams' ) == 'true' :
  II1I ( '[COLORgreen]SCOOBY STREAMS[/COLOR]' , str ( Ii1iIiII1ii1 ) , 1023 , ooOooo000oOO + 'scoob.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'HeroVision' ) == 'true' :
  II1I ( '[COLORgreen]HEROVISION[/COLOR]' , '' , 1017 , ooOooo000oOO + 'hero.png' , i1iiIII111ii , '' )
 II1I ( '[COLORgreen]ITV[/COLOR]' , ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9pVHZfU3RyZWFtcy9tYWluLnBocA==' ) ) , 1016 , ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9pVHZfU3RyZWFtcy9pdHZzdHJlYW1zLnBuZw==' ) ) , i1iiIII111ii , '' )
 if 64 - 64: IIIii1II1II % iI11I1II1I1I * OoOo00o
 iiIiI ( 'movies' , 'MAIN' )
 if 79 - 79: o0o00Oo0O
def oOO00O ( ) :
 O0O0O0OoOO ( )
 II1I ( '[COLORgreen]SILENT HUNTER[/COLOR]' , ( i1111 ( 'aHR0cDovLzUuMTM1LjIwNy45Ni8=' ) ) , 1006 , ooOooo000oOO + 'SILENTHUNTER.png' , i1iiIII111ii , '' )
 II1I ( '[COLORgreen]SILENT HUNTER SCRAPES[/COLOR]' , ( i1111 ( 'aHR0cDovLzUuMTM1LjIwNy45Ni9TY3JhcGVzL21haW4ucGhw' ) ) , 1016 , ooOooo000oOO + 'SILENTHUNTER.png' , i1iiIII111ii , '' )
 if 77 - 77: I1ii11iIi11i - ooOoO0O00 - iI1iI1I1i1I . OOooOOo
def IiI1i ( ) :
 II1I ( '[COLORgreen]HEROVISION[/COLOR]' , ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC9tYWluLnBocA==' ) ) , 1016 , ooOooo000oOO + 'hero.png' , i1iiIII111ii , '' )
 II1I ( '[COLORgreen]HEROVISION SCRAPES[/COLOR]' , ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC9zY3JhcGVkL3NjcmFwZWQucGhw' ) ) , 1024 , ooOooo000oOO + 'hero.png' , i1iiIII111ii , '' )
 if 92 - 92: OooO0OoOOOO . OooO0OoOOOO + oO0o
def IiIiI1111I1I ( ) :
 O0O0O0OoOO ( )
 II1I ( '[COLORgreen]SEARCH CARTOONS[/COLOR]' , '' , 10005 , ooOooo000oOO + 'search.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'WCO' ) == 'true' :
  II1I ( '[COLORgreen]WATCH CARTOONS ONLINE[/COLOR]' , str ( Ii1iIiII1ii1 ) , 21004 , ooOooo000oOO + 'watchcartoons.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Cartoons' ) == 'true' :
  II1I ( '[COLORgreen]CARTOONS[/COLOR]' , '' , 10001 , ooOooo000oOO + 'ORIGINCARTOON.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Anime' ) == 'true' :
  II1I ( '[COLORgreen]AnimeLand[/COLOR]' , ( i1111 ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2R1YmJlZC1hbmltZQ==' ) ) , 10004 , ooOooo000oOO + 'anime.png' , i1iiIII111ii , '' )
 iiIiI ( 'movies' , 'MAIN' )
def i1ioOOoo00O00o ( ) :
 O0O0O0OoOO ( )
 if o0oO0 . getSetting ( 'Football' ) == 'true' :
  II1I ( '[COLORgreen]FOOTBALL[/COLOR]' , '' , 10002 , ooOooo000oOO + 'ORIGINFOOTBALL.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Fitness' ) == 'true' :
  II1I ( '[COLORgreen]FITNESS[/COLOR]' , ( i1111 ( 'aHR0cHM6Ly93d3cuZml0bmVzc2JsZW5kZXIuY29tL3ZpZGVvcw==' ) ) , 7085 , ooOooo000oOO + 'FITNESS.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Go Fishing' ) == 'true' :
  II1I ( '[COLORgreen]Go Fishing[/COLOR]' , str ( Ii1iIiII1ii1 ) , 8090 , ooOooo000oOO + 'gofish.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'GenieTv Kitchen' ) == 'true' :
  II1I ( '[COLORgreen]GenieTv Kitchen[/COLOR]' , ( i1111 ( 'aHR0cDovL2Zvb2QubmR0di5jb20vdmlkZW9z' ) ) , 8045 , ooOooo000oOO + 'geniekitchen.png' , i1iiIII111ii , '' )
 iiIiI ( 'movies' , 'MAIN' )
 if 98 - 98: IIIii1II1II + OooO0OoOOOO + OoOo00o % ii
 if 97 - 97: o0o00Oo0O * ii . ii
 if 33 - 33: IIIi + o0oOO0O00o0O * OoOo00o / iI11I1II1I1I - oOo0O0Ooo
def iIiIIIi ( ) :
 o00OO00OoO = iiI111I1iIiI ( 'http://genietv.co.uk/genietv_art/testdelete.txt' )
 Ii1i = re . compile ( '<unwanted_addon =(.+?)</unwanted_addon>' ) . findall ( o00OO00OoO )
 for o0ooO in Ii1i :
  o0ooO = ( str ( o0ooO ) )
  if os . path . exists ( xbmc . translatePath ( o0ooO ) ) :
   O0oO = ( o0ooO ) . replace ( 'special://home/addons/' , '' )
   I1Ii ( "Please remove any addons or repo's that may alter Genie Tv coding without your knowledge" , "It has been recognised you have \n[COLORred]" + O0oO + "[/COLOR]\n installed on your system. In order for genie to function this addon must be removed. \n\nThere have been 'creative differences' between ourselves and this addon. Initially we just stopped our addon from working if this addon was installed, but when private talks were undertaken the 'author' (we use this term very lightly) of this addon gave us a choice, either remove our block or they will tamper with our addon, they then saw fit to host our addon and begin pushing unwanted and unauthorised, potentially malicious updates (we've no idea what they altered and with there approach anything could be possible) so we took steps to remove this addon purely for your protection from alterations to code from, self confessed, unskilled individuals. \n\nHowever the approach we took i guess can be seen as malicious because we did not inform you of actions that altered your device without your knowledge (bar a popup telling you this was happening), for this we apologise, it was a major oversight on our part and made us no better than them. \n\nAll are free to continue to use genie tv at no cost but you must make a decision. A box will soon open and you will need to choose remove or close. If you choose remove you are accepting to remove these addons that we believe have the potential to maliciously alter your device from an unofficial source or if you press close it will close genie, it will not be useable until these addons are remove and you can chose to use whatever addon you see fit at your own risk. \n\nThis is not 'playing god' please dont see it that way but merely protecting our hard work and in the end your experience from this.  We hope this issue resolves itself and things return to normality as much as, if not more than, yourself. Please wait to decide what action you wish to take" )
   xbmc . sleep ( 40000 )
   OO0ooOOO0OOO = xbmcgui . Dialog ( ) . yesno ( 'Remove Potentially Harmful Addons' , 'Remove will remove addons known to alter genie tv' , 'Close will stop genie tv working to protect' , 'you from any potential unwanted updates' , nolabel = 'Close' , yeslabel = 'Remove' )
   if OO0ooOOO0OOO == 0 :
    O0o0O00Oo0o0 ( o0ooO )
    oO00oooOOoOo0 ( )
   elif OO0ooOOO0OOO == 1 :
    OoOOoOooooOOo ( o0ooO )
  else :
   pass
   if 87 - 87: oOo0O0Ooo
def OoOOoOooooOOo ( addon ) :
 O0oO = ( addon ) . replace ( 'special://home/addons/' , '' )
 Oo0oO0ooo . create ( "[COLOR=white]The addons are being removed as requested[/COLOR]" , 'Please enjoy Genie Tv and we thank you for your support' , '[COLORyellow]Hopefully this may end soon and peace is restored[/COLOR]' )
 xbmc . sleep ( 3000 )
 addon = xbmc . translatePath ( str ( addon ) )
 shutil . rmtree ( addon , ignore_errors = True )
 Oo0oO0ooo . update ( 100 , "" , "Your Device is now clean" )
 xbmc . sleep ( 1000 )
 Oo0oO0ooo . close ( )
 if 58 - 58: OOooOOo % I11i
def O0o0O00Oo0o0 ( addon ) :
 oOOoo00O0O . ok ( "[COLOR=white]Incompatible[/COLOR]" , "Unfortunately GenieTv will not work with" , addon , 'please remove then reinstall genie' )
 i1OOoO = os . path . join ( O0OoO000O0OO , 'default.py' )
 OO0O000 = open ( i1OOoO , "w+" )
 if 37 - 37: ii - o0o00Oo0O - I11i
 OO0O000 . write ( r'Genie Tv will not work with certain addons in an attempt to bring you original content from the best developers' )
 OO0O000 . write ( r'and not those simply out to profit or make a name for themselves off others work' )
 OO0O000 . write ( r'Please remove' + unwanted_addons + 'if you would like to use genie tv then uninstall and reinstall from official repo' )
 if 77 - 77: IIIii1II1II * iI11I1II1I1I
 if 98 - 98: oOo0O0Ooo % Ii11Ii1I * ii
 if 51 - 51: iI11I1II1I1I . OOooOOo / OoOo00o + I11i
 if 33 - 33: O0OoO . IIiIiII11i % o0oOO0O00o0O + I11i
 if 71 - 71: I1ii11iIi11i % IIIii1II1II
 if 98 - 98: iI1iI1I1i1I % Ii % O0OoO + Ii11Ii1I
 if 78 - 78: Ii1I % OoOo00o / o0oOO0O00o0O - iI11I1II1I1I
 if 69 - 69: IIIi
 if 11 - 11: oOo0O0Ooo
 if 16 - 16: Ii11Ii1I + OooO0OoOOOO * o0o00Oo0O % ooOoO0O00 . oOo0O0Ooo
 if 67 - 67: ii / oOo0O0Ooo * Ii11Ii1I + iI1iI1I1i1I
 if 65 - 65: ii - Ii1I / O0OoO / IIiIiII11i / ooOoO0O00
 if 71 - 71: IIIi + Ii11Ii1I
 if 28 - 28: IIIii1II1II
 if 38 - 38: O0OoO % IIiIiII11i % iI1iI1I1i1I / oO0o + OOooOOo / ooOoO0O00
 if 54 - 54: iI11I1II1I1I % Ii1I - IIIii1II1II / OoOo00o - oO0o . iI1iI1I1i1I
 if 11 - 11: Ii1I . oO0o * OooO0OoOOOO * ii + O0OoO
 if 33 - 33: o0o00Oo0O * I11i - IIIi % IIIi
 if 18 - 18: IIIi / I1ii11iIi11i * IIIi + IIIi * Ii * Ii1I
def I1II1 ( ) :
 II1I ( 'Genre' , i1111 ( 'aHR0cDovL2ltb3ZpZW1heC5zZS9tb3ZpZXMv' ) , 10073 , ooOooo000oOO + 'genievision.png' , i1iiIII111ii , '' )
 II1I ( 'Most Viewed' , i1111 ( 'aHR0cDovL2ltb3ZpZW1heC5zZS9tb3ZpZXMv' ) , 10077 , ooOooo000oOO + 'genievision.png' , i1iiIII111ii , '' )
 II1I ( 'Box Office' , i1111 ( 'aHR0cDovL2ltb3ZpZW1heC5zZS9jYXRlZ29yeS9ib3gtb2ZmaWNlLw==' ) , 10074 , ooOooo000oOO + 'genievision.png' , i1iiIII111ii , '' )
 II1I ( 'Search' , '' , 10078 , ooOooo000oOO + 'genievision.png' , i1iiIII111ii , '' )
 if 86 - 86: iI11I1II1I1I / OOooOOo . IIiIiII11i
def II1i111Ii1i ( ) :
 iii1 = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 ooO0oooOO0 = 'http://imoviemax.se/?s=' + ( iii1 ) . replace ( ' ' , '+' )
 o0o = ooO0oooOO0 . lower ( )
 oo0 ( o0o )
def oOOOoo00 ( url ) :
 iiIiIIIiiI = [ ]
 o00OO00OoO = iiI111I1iIiI ( url )
 Ii1i = re . compile ( '<li class="cat-item cat-item-.+? "><a href="(.+?)">(.+?)</a><i>(.+?)</i></li>' ) . findall ( o00OO00OoO )
 for url , iiI1IIIi , II11IiIi11 in Ii1i :
  if iiI1IIIi in iiIiIIIiiI :
   pass
  else :
   II1I ( iiI1IIIi + ' - ' + II11IiIi11 + ' Films' , url , 10074 , ooOooo000oOO + 'genievision.png' , i1iiIII111ii , '' )
   iiIiIIIiiI . append ( iiI1IIIi )
   if 7 - 7: oO0o . Ii11Ii1I % OoOo00o * O0OoO + OooO0OoOOOO + IIIi
def IIIIiII1i ( url ) :
 o00OO00OoO = iiI111I1iIiI ( url )
 Ii1i = re . compile ( '<li>.+?<b>.+?</b>.+?<a href="(.+?)">(.+?)</a>.+?<span>(.+?)</span>' , re . DOTALL ) . findall ( o00OO00OoO )
 for url , iiI1IIIi , i1II1 in Ii1i :
  II1I ( iiI1IIIi + ' - Views:' + i1II1 , url , 10075 , ooOooo000oOO + 'genievision.png' , i1iiIII111ii , '' )
  if 25 - 25: IIIi / iI11I1II1I1I % o0oOO0O00o0O
  if 42 - 42: Ii * iI11I1II1I1I / Ii1I . Ii % iI1iI1I1i1I
def oo0 ( url ) :
 i1iI = [ ]
 o00OO00OoO = iiI111I1iIiI ( url )
 next = re . compile ( "<link rel='next' href='(.+?)' />" ) . findall ( o00OO00OoO )
 for next in next :
  II1I ( 'NEXT PAGE' , next , 10074 , ooOooo000oOO + 'Next.png' , i1iiIII111ii , '' )
 Ii1i = re . compile ( '<div class="movie">.+?<img src="(.+?)" alt="(.+?)" />.+?<a href="(.+?)"><span class="player"></span></a>' , re . DOTALL ) . findall ( o00OO00OoO )
 for IiI1iiiIii , iiI1IIIi , url in Ii1i :
  II1I ( iiI1IIIi , url , 10075 , IiI1iiiIii , IiI1iiiIii , '' )
  i1iI . append ( iiI1IIIi )
  if 7 - 7: IIIi * oO0o - O0OoO + IIIii1II1II * oOo0O0Ooo % oO0o
def iI1i111I1Ii ( img , name , url ) :
 img = img
 name = name
 o00OO00OoO = iiI111I1iIiI ( url )
 Ii1i = re . compile ( '<div id="(.+?)" class="player-content"><iframe class="playerframe" src="(.+?)" scrolling="no".+?</iframe></div>' ) . findall ( o00OO00OoO )
 for i11i1ii1I , url in Ii1i :
  print '>>>>>>>>>>>>>>>>>>>>>>>>>>> before' + url
  o0OO0o0o00o = ( url ) . replace ( 'player' , 'watch' ) + '&fv=&sou='
  print '<<<<<<<<<<<<<<<<<<<<<<<<<<< after' + o0OO0o0o00o
  oOo0 = ( i11i1ii1I ) . replace ( 'play-' , 'Server ' )
  ooOOoooooo ( oOo0 , o0OO0o0o00o , 10076 , img , img , '' )
  if 56 - 56: I11i + IIiIiII11i + OOooOOo - O0OoO . OOooOOo
def OOOooo ( url ) :
 o00OO00OoO = iiI111I1iIiI ( url )
 Ii1i = re . compile ( '<source src="(.+?)" type="video/mp4">' ) . findall ( o00OO00OoO )
 for OooO0OO in Ii1i :
  if '=m' in OooO0OO :
   o0OOo0o0O0O ( OooO0OO )
  elif 'php' in OooO0OO :
   OOOooo ( url )
  else :
   o00OO00OoO = iiI111I1iIiI ( OooO0OO )
   Ii1i = re . compile ( 'content="(.+?)">' ) . findall ( o00OO00OoO )
   for o0OO0o0oOOO0O in Ii1i :
    o0OOo0o0O0O ( OooO0OO )
    if 49 - 49: Ii1I . I11i . IIiIiII11i
    if 98 - 98: o0oOO0O00o0O
    if 68 - 68: iI11I1II1I1I * iI11I1II1I1I . I11i / IIiIiII11i % I1ii11iIi11i
def i1i11I11 ( url ) :
 o00OO00OoO = iiI111I1iIiI ( url )
 iiiiII1I = re . compile ( '<td id=".+?" class="today">.+?title="(.+?)">(.+?)</td>' , re . DOTALL ) . findall ( o00OO00OoO )
 for ooo00Ooo , Oo0o0O00 in iiiiII1I :
  print 'there ><><><><><><><><><><><><'
  ooo00Ooo = ooo00Ooo
  Ii1i = re . compile ( '<p><a href=".+?" rel=".+?">(.+?)</a>.+?<br /><a href=".+?">(.+?)</a>.+?</p>' , re . DOTALL ) . findall ( str ( Oo0o0O00 ) )
  for iiI1IIIi , ii1 in Ii1i :
   print 'here <><><><><><><><><><><><>'
   II1I ( '[COLORred]' + ooo00Ooo + '[/COLOR] - ' + iiI1IIIi + ' - [COLORgreen]' + ii1 + '[/COLOR]' , i1111 ( 'aHR0cDovL3d3dy5wb2dkZXNpZ24uY28udWsvY2F0Lw==' ) , 10070 , ooOooo000oOO + 'loader.png' , i1iiIII111ii , '' )
 I1i11 = re . compile ( '<td id=".+?" class="day">.+?title="(.+?)">(.+?)</td>' , re . DOTALL ) . findall ( o00OO00OoO )
 for ooo00Ooo , OOo0O0oo0OO0O in I1i11 :
  print 'there ><><><><><><><><><><><><'
  ooo00Ooo = ooo00Ooo
  Ii1i = re . compile ( '<p><a href=".+?" rel=".+?">(.+?)</a>.+?<br /><a href=".+?">(.+?)</a>.+?</p>' , re . DOTALL ) . findall ( str ( OOo0O0oo0OO0O ) )
  for iiI1IIIi , ii1 in Ii1i :
   print 'here <><><><><><><><><><><><>'
   II1I ( '[COLORred]' + ooo00Ooo + '[/COLOR] - ' + iiI1IIIi + ' - [COLORgreen]' + ii1 + '[/COLOR]' , i1111 ( 'aHR0cDovL3d3dy5wb2dkZXNpZ24uY28udWsvY2F0Lw==' ) , 10070 , ooOooo000oOO + 'loader.png' , i1iiIII111ii , '' )
   if 68 - 68: OoOo00o . iI1iI1I1i1I % ii . iI1iI1I1i1I
   if 64 - 64: iI11I1II1I1I / oOo0O0Ooo . IIiIiII11i + ii . oO0o
   if 56 - 56: I1ii11iIi11i . Ii1I . oOo0O0Ooo
def ii111I ( url ) :
 o00OO00OoO = iiI111I1iIiI ( url )
 I1i11 = re . compile ( '<li class="yt-uix-scroller-scroll-unit "(.+?)</li>' , re . DOTALL ) . findall ( o00OO00OoO )
 for I1i11 in I1i11 :
  iiI1IIIi = re . compile ( 'data-video-title="(.+?)"' ) . findall ( str ( I1i11 ) )
  for iiI1IIIi in iiI1IIIi :
   iiI1IIIi = ( iiI1IIIi ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&' , '&' )
  url = re . compile ( '<a href="/w(.+?)&' ) . findall ( str ( I1i11 ) )
  for url in url :
   url = 'https://www.youtube.com/w' + url
  iiI = re . compile ( '<img.+?="(.+?)"' ) . findall ( str ( I1i11 ) )
  for iiI in iiI :
   iiI = 'http:' + iiI
  ooOOoooooo ( '[COLORgreen]' + iiI1IIIi + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , iiI , '' , '' )
  if 7 - 7: OOooOOo + IIiIiII11i . ooOoO0O00
  if 63 - 63: iI11I1II1I1I / IIIi / OoOo00o / o0oOO0O00o0O
  if 33 - 33: OooO0OoOOOO % iI11I1II1I1I * oOo0O0Ooo
  if 95 - 95: O0OoO / O0OoO
def IIiI1Ii ( url ) :
 if 57 - 57: IIIii1II1II - O0OoO - iI1iI1I1i1I + oO0o
 I1IIIiI11i1 = [ ]
 o00OO00OoO = iiI111I1iIiI ( url )
 Ii1i = re . compile ( '<div class="explore-list">.+?<div class="el-img"><a href="(.+?)" class=".+?"><img src="(.+?)" alt=".+?<h3>(.+?)</h3><p>(.+?)</p></div>' , re . DOTALL ) . findall ( o00OO00OoO )
 for OooO0OO , IiI1iiiIii , iiI1IIIi , i11I1I1I in Ii1i :
  iiI1IIIi = ( iiI1IIIi ) . replace ( '&#039;' , '\'' ) . replace ( '&' , '&' ) . replace ( '&quot;' , '"' )
  OOOO0OOoO0O0 = iiI111I1iIiI ( OooO0OO )
  I1 = re . compile ( '<!-- # player # -->.+?<iframe title=".+?".+?src="http://www.youtube.com/embed/(.+?)?autohide.+?<!-- detail box -->(.+?)</div>' , re . DOTALL ) . findall ( OOOO0OOoO0O0 )
  for oOOOo00O00O , iIIIII1I in I1 :
   ooI1i = re . compile ( '<p>(.+?)</p>' , re . DOTALL ) . findall ( str ( iIIIII1I ) )
   for iIII in ooI1i :
    if iiI1IIIi in I1IIIiI11i1 :
     pass
    else :
     ooOOoooooo ( iiI1IIIi , oOOOo00O00O , 8043 , IiI1iiiIii , IiI1iiiIii , iIII )
     iiIiI ( 'movies' , 'INFO' )
     I1IIIiI11i1 . append ( iiI1IIIi )
     if 70 - 70: o0oOO0O00o0O / iI11I1II1I1I
     if 85 - 85: ii % ooOoO0O00 * ii / Ii1I
def ooOOoO ( url ) :
 I1i11i = IiIi ( url )
 Ii1i = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( I1i11i )
 for url , OOOOO0O00 , iIII , Iii , iiI1IIIi in Ii1i :
  II1I ( iiI1IIIi , url , 10065 , OOOOO0O00 , Iii , iIII )
 iiIiI ( 'movies' , 'INFO' )
 if 31 - 31: I11i % oO0o
def iI1I ( ) :
 iii1 = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 ooO0oooOO0 = 'https://www.youtube.com/results?search_query=' + ( iii1 ) . replace ( ' ' , '+' )
 o0o = ooO0oooOO0 . lower ( )
 o00OO00OoO = iiI111I1iIiI ( o0o )
 Ii1i = re . compile ( '<img src="(.+?)" alt=.+?yt-lockup-title "><a href="(.+?)".+?data-sessionlink=.+?" title="(.+?)".+?<span class="accessible-description".+?>(.+?)</span>.+?<div class="yt-lockup-description yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr">(.+?)</div>' , re . DOTALL ) . findall ( o00OO00OoO )
 next = re . compile ( '<a href="(.+?)" class="yt-uix-button.+?class="yt-uix-button-content">Next.+?</span></a>' ) . findall ( o00OO00OoO )
 for OooOoOo in next :
  OooOoOo = 'https://www.youtube.com' + OooOoOo
  II1I ( '[COLORgreen] NEXT [/COLOR]' , OooOoOo , 10065 , ooOooo000oOO + 'Next.png' , i1iiIII111ii , '' )
 for IiI1iiiIii , OooOoOo , iiI1IIIi , III1I1Iii1iiI , iIIIII1I in Ii1i :
  II11iiii1Ii . append ( iiI1IIIi )
  iiIiI ( 'tvshows' , 'INFO' )
  iiI = 'http:' + ( IiI1iiiIii ) . replace ( 'https:' , '' )
  print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>' + iiI
  OooOoOo = 'http://www.youtube.com' + OooOoOo
  ooOOoooooo ( '[COLORred]' + III1I1Iii1iiI + '[/COLOR]' + '[COLORgreen]' + iiI1IIIi + '[/COLOR]' , ( OooOoOo ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , iiI , iiI , iIIIII1I )
 else :
  Ii1i = re . compile ( '<img src="(.+?)" alt=.+?yt-lockup-title "><a href="(.+?)".+?data-sessionlink=.+?" title="(.+?)".+?<span class="accessible-description".+?>(.+?)</span>' , re . DOTALL ) . findall ( o00OO00OoO )
  for IiI1iiiIii , OooOoOo , iiI1IIIi , III1I1Iii1iiI in Ii1i :
   print 'im doing it'
   iiIiI ( 'tvshows' , 'INFO' )
   iiI = 'http:' + ( IiI1iiiIii ) . replace ( 'https:' , '' )
   OooOoOo = 'http://www.youtube.com' + OooOoOo
   if '&' in OooOoOo :
    print ' i got here'
    o00OO00OoO = iiI111I1iIiI ( OooOoOo )
    I1i11 = re . compile ( '<li class="yt-uix-scroller-scroll-unit "(.+?)</li>' , re . DOTALL ) . findall ( o00OO00OoO )
    for I1i11 in I1i11 :
     iiI1IIIi = re . compile ( 'data-video-title="(.+?)"' ) . findall ( str ( I1i11 ) )
     for iiI1IIIi in iiI1IIIi :
      iiI1IIIi = ( iiI1IIIi ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&' , '&' )
     OooOoOo = re . compile ( '<a href="/w(.+?)&' ) . findall ( str ( I1i11 ) )
     for OooOoOo in OooOoOo :
      OooOoOo = 'https://www.youtube.com/w' + OooOoOo
     iiI = re . compile ( '<img.+?="(.+?)"' ) . findall ( str ( I1i11 ) )
     for iiI in iiI :
      iiI = 'http:' + iiI
     ooOOoooooo ( '[COLORred]' + III1I1Iii1iiI + '[/COLOR]' + '[COLORgreen]' + iiI1IIIi + '[/COLOR]' , ( OooOoOo ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , iiI , i1iiIII111ii , '' )
   elif iiI1IIIi in II11iiii1Ii :
    pass
   elif 'user' in OooOoOo or 'elete' in iiI1IIIi :
    pass
   elif 'hannel' in OooOoOo :
    print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' + OooOoOo
    o00OO00OoO = iiI111I1iIiI ( OooOoOo )
    i1Iii11I1i = re . compile ( 'data-thumb="(.+?)".+?href="(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( o00OO00OoO )
    for IiI1iiiIii , OooOoOo , iiI1IIIi in i1Iii11I1i :
     if 'outube' in OooOoOo or 'list' in OooOoOo :
      pass
     elif 'atch' in OooOoOo :
      OooOoOo = ( OooOoOo ) . replace ( '/watch?v=' , '' )
      ooOOoooooo ( '[COLORred]' + III1I1Iii1iiI + '[/COLOR]' + '[COLORgreen]' + iiI1IIIi + '[/COLOR]' , ( OooOoOo ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , 'http:' + IiI1iiiIii , 'http:' + IiI1iiiIii , '' )
     else :
      pass
   else :
    ooOOoooooo ( '[COLORred]' + III1I1Iii1iiI + '[/COLOR]' + '[COLORgreen]' + iiI1IIIi + '[/COLOR]' , ( OooOoOo ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , iiI , iiI , '' )
    if 72 - 72: iI11I1II1I1I * Ii11Ii1I % O0OoO / oO0o
def I11i1II ( url ) :
 o00OO00OoO = iiI111I1iIiI ( url )
 Ii1i = re . compile ( '<img src="(.+?)" alt=.+?yt-lockup-title "><a href="(.+?)".+?data-sessionlink=.+?" title="(.+?)".+?<span class="accessible-description".+?>(.+?)</span>.+?<div class="yt-lockup-description yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr">(.+?)</div>' , re . DOTALL ) . findall ( o00OO00OoO )
 next = re . compile ( '<a href="(.+?)" class="yt-uix-button.+?class="yt-uix-button-content">Next.+?</span></a>' ) . findall ( o00OO00OoO )
 for url in next :
  url = 'https://www.youtube.com' + url
  II1I ( '[COLORgreen] NEXT [/COLOR]' , url , 10065 , ooOooo000oOO + 'Next.png' , i1iiIII111ii , '' )
 for IiI1iiiIii , url , iiI1IIIi , III1I1Iii1iiI , iIIIII1I in Ii1i :
  II11iiii1Ii . append ( iiI1IIIi )
  iiIiI ( 'tvshows' , 'INFO' )
  iiI = 'http:' + ( IiI1iiiIii ) . replace ( 'https:' , '' )
  print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>' + iiI
  url = 'http://www.youtube.com' + url
  ooOOoooooo ( '[COLORred]' + III1I1Iii1iiI + '[/COLOR]' + '[COLORgreen]' + iiI1IIIi + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , iiI , iiI , iIIIII1I )
 else :
  Ii1i = re . compile ( '<img src="(.+?)" alt=.+?yt-lockup-title "><a href="(.+?)".+?data-sessionlink=.+?" title="(.+?)".+?<span class="accessible-description".+?>(.+?)</span>' , re . DOTALL ) . findall ( o00OO00OoO )
  for IiI1iiiIii , url , iiI1IIIi , III1I1Iii1iiI in Ii1i :
   iiIiI ( 'tvshows' , 'INFO' )
   iiI = 'http:' + ( IiI1iiiIii ) . replace ( 'https:' , '' )
   url = 'http://www.youtube.com' + url
   if '&' in url :
    o00OO00OoO = iiI111I1iIiI ( url )
    I1i11 = re . compile ( '<li class="yt-uix-scroller-scroll-unit "(.+?)</li>' , re . DOTALL ) . findall ( o00OO00OoO )
    for I1i11 in I1i11 :
     iiI1IIIi = re . compile ( 'data-video-title="(.+?)"' ) . findall ( str ( I1i11 ) )
     for iiI1IIIi in iiI1IIIi :
      iiI1IIIi = ( iiI1IIIi ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&' , '&' )
     url = re . compile ( '<a href="/w(.+?)&' ) . findall ( str ( I1i11 ) )
     for url in url :
      url = 'https://www.youtube.com/w' + url
     iiI = re . compile ( '<img.+?="(.+?)"' ) . findall ( str ( I1i11 ) )
     for iiI in iiI :
      iiI = 'http:' + iiI
     ooOOoooooo ( '[COLORred]' + III1I1Iii1iiI + '[/COLOR]' + '[COLORgreen]' + iiI1IIIi + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , iiI , i1iiIII111ii , '' )
   elif iiI1IIIi in II11iiii1Ii :
    pass
   elif 'user' in url or 'elete' in iiI1IIIi :
    pass
   elif 'hannel' in url :
    print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' + url
    o00OO00OoO = iiI111I1iIiI ( url )
    i1Iii11I1i = re . compile ( 'data-thumb="(.+?)".+?href="(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( o00OO00OoO )
    for IiI1iiiIii , url , iiI1IIIi in i1Iii11I1i :
     if 'outube' in url or 'list' in url :
      pass
     elif 'atch' in url :
      url = ( url ) . replace ( '/watch?v=' , '' )
      ooOOoooooo ( '[COLORred]' + III1I1Iii1iiI + '[/COLOR]' + '[COLORgreen]' + iiI1IIIi + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , 'http:' + IiI1iiiIii , 'http:' + IiI1iiiIii , '' )
     else :
      pass
   else :
    ooOOoooooo ( '[COLORred]' + III1I1Iii1iiI + '[/COLOR]' + '[COLORgreen]' + iiI1IIIi + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , iiI , iiI , '' )
    if 72 - 72: iI11I1II1I1I . ooOoO0O00 / I1ii11iIi11i . IIiIiII11i
    if 54 - 54: IIiIiII11i % IIiIiII11i
def Oo00000o0o ( ) :
 if oo0o0O00 == 'insert_password' :
  oOOoo00O0O . ok ( '[COLORgreen]Donators Login[/COLOR]' , 'You need to set username and password to access this' , 'These are unique and provided to donators to help with server and stream costs' , 'Donate @ [COLORgreen]http://architects.x10host.com[/COLOR]' )
  o0oO0 . openSettings ( sys . argv [ 0 ] )
 else :
  O0OOoOOO0oO = open ( iIi1ii1I1 )
  Ii1i = re . compile ( 'plugin.video.GenieTv.+?2Flive%2F(.+?)%2F(.+?)%2F' ) . findall ( str ( O0OOoOOO0oO ) )
  for I1ii11 , oOoOoOoo0 in Ii1i :
   if I1ii11 == 'needs replacing' or oOoOoOoo0 == 'needs replacing' :
    III1ii1I ( )
  II1I ( '[COLORgreen]DONATORS LIST[/COLOR]' , str ( Ii1iIiII1ii1 ) + '/thelistnew.m3u' , 7080 , ooOooo000oOO + 'GTVIPTV.png' , i1iiIII111ii , '' )
  if 13 - 13: Ii + ooOoO0O00 * iI11I1II1I1I % ii - IIiIiII11i * IIIii1II1II
def iiIi1iI1iIii ( ) :
 i1iiIIiiI111 . ok ( '[COLOR=white]ReCreate Addons.ini[/COLOR]' , 'If it doesnt work ensure login details are correct and retry' , '' , 'This will allow access to streams in guide without linking to favourites' )
 xbmc . executebuiltin ( "XBMC.RunScript(" + OO0o + ")" )
 III1ii1I ( )
 i1iiIIiiI111 . ok ( '[COLOR=yellow]Done[/COLOR]' , 'Done' , 'Easy as that' , 'Now Go to guide and it should link your GTV streams' )
 if 68 - 68: IIIii1II1II
def OooO0oo ( ) :
 try :
  o0o0oOoOO0O = gui . TVGuide ( )
  o0o0oOoOO0O . doModal ( )
  del o0o0oOoOO0O
  if 16 - 16: OooO0OoOOOO % iI11I1II1I1I . Ii11Ii1I
 except :
  import sys
  import traceback as tb
  ( oooooOOO000Oo , Ooo00OoOOO , traceback ) = sys . exc_info ( )
  tb . print_exception ( oooooOOO000Oo , Ooo00OoOOO , traceback )
  if 98 - 98: iI11I1II1I1I * Ii1I * IIIii1II1II + O0OoO % Ii % o0o00Oo0O
def i1OO0oOOoo ( ) :
 II1I ( 'Full Backup' , '' , 10061 , ooOooo000oOO + 'Backup.png' , i1iiIII111ii , 'Back Up Your Full System' )
 if os . path . exists ( I1IIIii ) :
  II1I ( 'Backup Genie Favourites' , OooOoOo , 10062 , ooOooo000oOO + 'Backup.png' , i1iiIII111ii , 'Back Up Your favourites' )
 if os . path . exists ( ooooooO0oo ) :
  II1I ( 'Backup Ivue Config' , ooooooO0oo , 10062 , ooOooo000oOO + 'Backup.png' , i1iiIII111ii , 'Back Up Your master.db' )
 if os . path . exists ( IIiiiiiiIi1I1 ) :
  II1I ( 'Backup Kodi Favourites' , IIiiiiiiIi1I1 , 10062 , ooOooo000oOO + 'Backup.png' , i1iiIII111ii , 'Back Up Your favourites.xml' )
  if 52 - 52: I11i % I1ii11iIi11i
  if 64 - 64: o0o00Oo0O % iI1iI1I1i1I % o0o00Oo0O * oO0o . OoOo00o + oOo0O0Ooo
  if 75 - 75: iI1iI1I1i1I . ii % I11i * iI1iI1I1i1I % ii
zip = o0oO0 . getSetting ( 'zip' )
I11i1iIiIIIIIii = xbmc . translatePath ( os . path . join ( zip ) )
def OOo0 ( ) :
 ii11I1 = xbmc . translatePath ( os . path . join ( zip , 'testCBFolder' ) )
 if not os . path . exists ( zip ) :
  i1iiIIiiI111 . ok ( '[COLOR=white]Origin[/COLOR]' , 'The download location you have stored does not exist .\nPlease update the addon settings and try again.' , '' , '' )
  o0oO0 . openSettings ( sys . argv [ 0 ] )
  if 75 - 75: oO0o / IIiIiII11i % o0o00Oo0O
  if 38 - 38: ii * O0OoO % o0o00Oo0O * OOooOOo
  if 29 - 29: Ii1I / ooOoO0O00 . oOo0O0Ooo - OOooOOo - OOooOOo - Ii11Ii1I
def IiiIiI111iI ( name , url , description ) :
 if 'Backup' in name :
  if 'Genie' in name :
   url = I1IIIii
  elif 'Ivue' in name :
   url = ooooooO0oo
  elif 'Kodi' in name :
   url = IIiiiiiiIi1I1
  OOo0 ( )
  OOo = open ( url ) . read ( )
  i1i11I1I1iii1 = os . path . join ( I11i1iIiIIIIIii , description . split ( 'Your ' ) [ 1 ] )
  I1iii11 = open ( i1i11I1I1iii1 , mode = 'w' )
  I1iii11 . write ( OOo )
  I1iii11 . close ( )
 else :
  if 'guisettings.xml' in description :
   ooo0OiII1iii = open ( os . path . join ( I11i1iIiIIIIIii , description . split ( 'Your ' ) [ 1 ] ) ) . read ( )
   i11i1iiiII = '<setting type="(.+?)" name="%s.(.+?)">(.+?)</setting>' % skin
   Ii1i = re . compile ( i11i1iiiII ) . findall ( ooo0OiII1iii )
   for type , ooOO0oO0oo00o , oOOo0oo0O in Ii1i :
    oOOo0oo0O = oOOo0oo0O . replace ( '&quot;' , '' ) . replace ( '&' , '&' )
    xbmc . executebuiltin ( "Skin.Se	t%s(%s,%s)" % ( type . title ( ) , ooOO0oO0oo00o , oOOo0oo0O ) )
  else :
   i1i11I1I1iii1 = os . path . join ( url )
   OOo = open ( os . path . join ( I11i1iIiIIIIIii , description . split ( 'Your ' ) [ 1 ] ) ) . read ( )
   I1iii11 = open ( i1i11I1I1iii1 , mode = 'w' )
   I1iii11 . write ( OOo )
   I1iii11 . close ( )
 i1iiIIiiI111 . ok ( "[COLOR=white]Origin[/COLOR]" , "" , 'All Done !' , '' )
 if 13 - 13: oOo0O0Ooo % OOooOOo . Ii1I / I1ii11iIi11i % IIIii1II1II . ii
 if 22 - 22: OooO0OoOOOO / Ii
 if 62 - 62: oO0o / Ii1I
 if 7 - 7: ii . OooO0OoOOOO
def O000OOO0OOo ( ) :
 i1i1I111iIi1 = 1
 OOo0 ( )
 oo00O00oO000o = xbmc . translatePath ( os . path . join ( I11i1iIiIIIIIii , 'Build Backup' , 'Full Backup' , '' ) )
 OOo00OoO = xbmc . translatePath ( os . path . join ( I11i1iIiIIIIIii , 'Build Backup' , 'my_full_backup.zip' ) )
 iIi1 = xbmc . translatePath ( os . path . join ( I11i1iIiIIIIIii , 'Build Backup' , 'my_full_backup_GUI_Settings.zip' ) )
 if not os . path . exists ( oo00O00oO000o ) :
  os . makedirs ( oo00O00oO000o )
 i11iiI1111 = oOOoo00O0O . input ( 'Enter a name for this backup' , type = xbmcgui . INPUT_ALPHANUM )
 if ( not i11iiI1111 ) : return False , 0
 oOoooo000Oo00 = i11iiI1111
 OOoo = xbmc . translatePath ( os . path . join ( oo00O00oO000o , oOoooo000Oo00 + '.zip' ) )
 o00O00oO00 = [ 'plugin.video.GenieTv' ]
 Ii1i1i1i1I1Ii = [ "xbmc.log" , "xbmc.old.log" , "kodi.log" , "kodi.old.log" , '.DS_Store' , '.setup_complete' , 'XBMCHelper.conf' ]
 iiiI1 = [ 'plugin.video.GenieTv' , 'repository.origin' , 'cache' , 'system' , 'Thumbnails' , "peripheral_data" , 'library' , 'keymaps' ]
 OOOoO0O = [ "xbmc.log" , "xbmc.old.log" , "kodi.log" , "kodi.old.log" , "Textures13.db" , '.DS_Store' , '.setup_complete' , 'XBMCHelper.conf' , 'advancedsettings.xml' ]
 o0iiiI1I1iIIIi1 = "Creating full backup of existing build"
 IiiI1iiiiI1iI = "Creating Community Build"
 iIiiiii1i = "Archiving..."
 iiIi1IIiI = ""
 i1oO0OO0 = "Please Wait"
 o0O0Oo00 ( oooOOOOO , OOoo , IiiI1iiiiI1iI , iIiiiii1i , iiIi1IIiI , i1oO0OO0 , iiiI1 , OOOoO0O )
 time . sleep ( 1 )
 O0Oo0o000oO = xbmc . translatePath ( os . path . join ( oo00O00oO000o , oOoooo000Oo00 + '_guisettings.zip' ) )
 oO0o00oOOooO0 = zipfile . ZipFile ( O0Oo0o000oO , mode = 'w' )
 try :
  oO0o00oOOooO0 . write ( xbmc . translatePath ( os . path . join ( oooOOOOO , 'userdata' , 'profiles.xml' ) ) , 'profiles.xml' , zipfile . ZIP_DEFLATED )
 except : pass
 oO0o00oOOooO0 . close ( )
 if i1i1I111iIi1 == 0 :
  i1iiIIiiI111 . ok ( "FAILED!" , 'The guisettings.xml file could not be found on your' , 'system, please reboot and try again.' , '' )
 else :
  i1iiIIiiI111 . ok ( "SUCCESS!" , 'You Are Now Backed Up. If you\'d like to share this build with' , 'the community please post details on the forum at' , '[COLOR=blue][B]http://rh-project.info[/COLOR][/B]' )
  i1iiIIiiI111 . ok ( "Build Locations" , 'Full Backup (only used to restore on this device): [COLOR=yellow]' + OOo00OoO , '[/COLOR]Universal Backup (can be used on any device): [COLOR=yellow]' + OOoo + '[/COLOR]' )
  if 79 - 79: oO0o - iI11I1II1I1I + Ii11Ii1I - IIIi
def o0O0Oo00 ( sourcefile , destfile , message_header , message1 , message2 , message3 , exclude_dirs , exclude_files ) :
 OoO = zipfile . ZipFile ( destfile , 'w' , zipfile . ZIP_DEFLATED )
 iIIiii = len ( sourcefile )
 O0i11i1iiI1i = [ ]
 oO0oOOoo00000 = [ ]
 Oo0oO0ooo . create ( message_header , message1 , message2 , message3 )
 for oOo00 , i1iI11i1IIi , ii1IIi111 in os . walk ( sourcefile ) :
  for file in ii1IIi111 :
   oO0oOOoo00000 . append ( file )
 iI1 = len ( oO0oOOoo00000 )
 for oOo00 , i1iI11i1IIi , ii1IIi111 in os . walk ( sourcefile ) :
  i1iI11i1IIi [ : ] = [ OoOo00o0OO for OoOo00o0OO in i1iI11i1IIi if OoOo00o0OO not in exclude_dirs ]
  ii1IIi111 [ : ] = [ I1iii11 for I1iii11 in ii1IIi111 if I1iii11 not in exclude_files ]
  for file in ii1IIi111 :
   O0i11i1iiI1i . append ( file )
   ii1IIIIiI11 = len ( O0i11i1iiI1i ) / float ( iI1 ) * 100
   Oo0oO0ooo . update ( int ( ii1IIIIiI11 ) , "Backing Up" , '[COLOR yellow]%s[/COLOR]' % file , 'Please Wait' )
   iI1IIIii = os . path . join ( oOo00 , file )
   if not 'temp' in i1iI11i1IIi :
    if not 'plugin.program.originwizard' in i1iI11i1IIi :
     import time
     I1i11ii11 = '01/01/1980'
     OO00O0oOO = time . strftime ( '%d/%m/%Y' , time . gmtime ( os . path . getmtime ( iI1IIIii ) ) )
     if OO00O0oOO > I1i11ii11 :
      OoO . write ( iI1IIIii , iI1IIIii [ iIIiii : ] )
 OoO . close ( )
 Oo0oO0ooo . close ( )
 if 4 - 4: ii - ooOoO0O00 % Ii11Ii1I - IIIii1II1II * I11i
 if 85 - 85: ii * iI11I1II1I1I . o0oOO0O00o0O / ii % oOo0O0Ooo % o0o00Oo0O
def I1iii ( ) :
 O0O0O0OoOO ( )
 II1I ( '[COLORgreen]SCOOBY STREAMS[/COLOR]' , ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvdHZjYXRzLnBocA==' ) ) , 1016 , ooOooo000oOO + 'scoob.png' , i1iiIII111ii , '' )
 II1I ( '[COLORgreen]SCOOBY SCRAPES[/COLOR]' , ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvc2NyYXBlZC9jYXRzLnBocA==' ) ) , 1024 , ooOooo000oOO + 'scoob.png' , i1iiIII111ii , '' )
 if 86 - 86: Ii1I * o0o00Oo0O * OooO0OoOOOO
 if 51 - 51: IIiIiII11i + OooO0OoOOOO . ooOoO0O00 . Ii1I + OOooOOo * oOo0O0Ooo
def OOoOoo0 ( ) :
 O0O0O0OoOO ( )
 II1I ( '[COLORgreen]SEARCH MOVIES[/COLOR]' , str ( Ii1iIiII1ii1 ) , 9001 , ooOooo000oOO + 'MOVIESv.png' , i1iiIII111ii , '' )
 II1I ( '[COLORgreen]SEARCH SERIES[/COLOR]' , str ( Ii1iIiII1ii1 ) , 9002 , ooOooo000oOO + 'TVSHOWSv.png' , i1iiIII111ii , '' )
 II1I ( '[COLORgreen]SEARCH CARTOONS[/COLOR]' , '' , 10005 , ooOooo000oOO + 'ORIGINCARTOON' , i1iiIII111ii , '' )
 if 17 - 17: Ii11Ii1I + OoOo00o . oO0o - I1ii11iIi11i * Ii
 if 20 - 20: oOo0O0Ooo . ii % IIIii1II1II
 if 63 - 63: oOo0O0Ooo % iI11I1II1I1I
 if 39 - 39: o0oOO0O00o0O / IIiIiII11i / Ii1I % oOo0O0Ooo
def O0Oo00 ( ) :
 O0O0O0OoOO ( )
 II1I ( '[COLORgreen]QuickSilver[/COLOR]' , ( i1111 ( 'aHR0cDovL3F1aWNrc2lsdmVyLW11c2ljLmNvbS9xdWlja3NpbHZlcm11c2ljLw==' ) ) , 1006 , ( i1111 ( 'aHR0cDovL3F1aWNrc2lsdmVyLW11c2ljLmNvbS9RdWlja3NpbHZlck11aXNjL3F1aWNrc2lsdmVyMi5wbmc=' ) ) , i1iiIII111ii , '' )
 II1I ( '[COLORgreen]MUSIC CHANNELS[/COLOR]' , str ( Ii1iIiII1ii1 ) , 30031 , ooOooo000oOO + 'musicch.png' , i1iiIII111ii , '' )
 II1I ( '[COLORgreen]UK RADIO[/COLOR]' , ( i1111 ( 'aHR0cDovL3d3dy5saXN0ZW5saXZlLmV1L3VrLmh0bWw=' ) ) , 10111113 , ooOooo000oOO + 'radio.png' , i1iiIII111ii , '' )
 II1I ( '[COLORgreen]WORLD RADIO[/COLOR]' , str ( Ii1iIiII1ii1 ) , 1013 , ooOooo000oOO + 'radio.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'CONCERTS' ) == 'true' :
  II1I ( '[COLORgreen]CONCERTS[/COLOR]' , ( i1111 ( 'aHR0cHM6Ly93d3cucmVkZGl0LmNvbS9yL2Z1bGxjb25jZXJ0cy8=' ) ) , 7050 , ooOooo000oOO + 'concerts.png' , i1iiIII111ii , '' )
  if 41 - 41: iI11I1II1I1I % iI1iI1I1i1I
 II1I ( '[COLORgreen]MUSIC VIDEOS[/COLOR]' , ( i1111 ( 'aHR0cDovLzE3Ni45LjE5Mi4yMjEvbXA0Lw==' ) ) , 1032 , ooOooo000oOO + 'musicvideos.png' , i1iiIII111ii , '' )
 II1I ( '[COLORgreen]MUSIC[/COLOR]' , str ( Ii1iIiII1ii1 ) + ( i1111 ( 'L3ZvZC91cmxzL211c2ljLnBocA==' ) ) , 1010 , ooOooo000oOO + 'MUSIC.png' , i1iiIII111ii , '' )
 II1I ( '[COLORgreen]MUSIC SEARCH[/COLOR]' , str ( Ii1iIiII1ii1 ) , 1111 , ooOooo000oOO + 'search.png' , i1iiIII111ii , '' )
 II1I ( '[COLORgreen]KODIBLE AUDIO BOOKS[/COLOR]' , 'http://doremisa.com/audiobooks/' , 30000 , ooOooo000oOO + 'kodible.png' , i1iiIII111ii , '' )
 if 59 - 59: IIIii1II1II + Ii
 iiIiI ( 'movies' , 'MAIN' )
 if 88 - 88: Ii - O0OoO
def O0iIi1IiII ( ) :
 O0O0O0OoOO ( )
 if 27 - 27: o0oOO0O00o0O . iI1iI1I1i1I . iI11I1II1I1I . iI11I1II1I1I
 ooOOoooooo ( 'DELETE CACHE' , 'url' , 14 , ooOooo000oOO + 'MAIN5.png' , i1iiIII111ii , '' )
 ooOOoooooo ( 'DELETE PACKAGES' , 'url' , 6 , ooOooo000oOO + 'MAIN4.png' , i1iiIII111ii , '' )
 ooOOoooooo ( 'FORCE REFRESH' , 'url' , 10 , ooOooo000oOO + 'MAIN3.png' , i1iiIII111ii , 'Force Refresh All Repos' )
 if 20 - 20: I11i / ooOoO0O00
 ooOOoooooo ( 'CHECK MY IP' , 'url' , 12 , ooOooo000oOO + 'MAIN2.png' , i1iiIII111ii , '' )
 ooOOoooooo ( 'ANDROID ONLY DELETE TEXTURE13.DB&THUBMNAIL FOLDER' , 'url' , 13 , ooOooo000oOO + 'MAIN1.png' , i1iiIII111ii , 'Only Works On Android On Windows It Deletes Your Thumnails Folder But Does Not Delete The Textures13.db' )
 II1I ( '[COLORgreen]ADVANCED SETTINGS XML[/COLOR]' , str ( Ii1iIiII1ii1 ) , 4 , ooOooo000oOO + 'XML.png' , i1iiIII111ii , '' )
 II1I ( '[COLORgreen]URL FIXES[/COLOR]' , str ( Ii1iIiII1ii1 ) , 20 , ooOooo000oOO + 'URLFIX.png' , i1iiIII111ii , '' )
 iiIiI ( 'movies' , 'MAIN' )
 if 71 - 71: OOooOOo . ooOoO0O00
 if 94 - 94: IIIii1II1II . IIIi
def iI1Ii11111iIi ( ) :
 O0O0O0OoOO ( )
 II1I ( '[COLORgreen]REPOS[/COLOR]' , ( i1111 ( 'aHR0cDovL21pcnJvcnMua29kaS50di9hZGRvbnMv' ) ) , 2030 , ooOooo000oOO + 'repos.png' , i1iiIII111ii , '' )
 II1I ( '[COLORgreen]NEW[/COLOR]' , str ( Ii1iIiII1ii1 ) , 22 , ooOooo000oOO + 'NEW.png' , i1iiIII111ii , '' )
 II1I ( '[COLORgreen]IPTV[/COLOR]' , str ( Ii1iIiII1ii1 ) , 23 , ooOooo000oOO + 'IPTV.png' , i1iiIII111ii , '' )
 II1I ( '[COLORgreen]VIDEO[/COLOR]' , str ( Ii1iIiII1ii1 ) , 24 , ooOooo000oOO + 'VIDEO.png' , i1iiIII111ii , '' )
 II1I ( '[COLORgreen]SPORTS[/COLOR]' , str ( Ii1iIiII1ii1 ) , 25 , ooOooo000oOO + 'SPORTS.png' , i1iiIII111ii , '' )
 II1I ( '[COLORgreen]KIDS[/COLOR]' , str ( Ii1iIiII1ii1 ) , 26 , ooOooo000oOO + 'KIDS.png' , i1iiIII111ii , '' )
 II1I ( '[COLORgreen]MUSIC[/COLOR]' , str ( Ii1iIiII1ii1 ) , 27 , ooOooo000oOO + 'MUSIC.png' , i1iiIII111ii , '' )
 II1I ( '[COLORgreen]PROGRAMS[/COLOR]' , str ( Ii1iIiII1ii1 ) , 28 , ooOooo000oOO + 'PROGRAMS.png' , i1iiIII111ii , '' )
 II1I ( '[COLORgreen]XXX[/COLOR]' , 'URL' , 29 , ooOooo000oOO + 'XXX.png' , i1iiIII111ii , '' )
 iiIiI ( 'movies' , 'MAIN' )
 if 84 - 84: o0o00Oo0O . iI1iI1I1i1I - IIiIiII11i . O0OoO / IIiIiII11i
 if 47 - 47: ii
def ii1i1i1IiII ( ) :
 O0O0O0OoOO ( )
 ooOOoooooo ( 'CHECK ADVANCED XML' , str ( Ii1iIiII1ii1 ) , 8 , ooOooo000oOO + 'XML.png' , i1iiIII111ii , '' )
 ooOOoooooo ( 'MUCKYS XML' , str ( Ii1iIiII1ii1 ) + '/wizard/muckys.xml' , 7 , ooOooo000oOO + 'XML.png' , i1iiIII111ii , '' )
 ooOOoooooo ( '0CACHE XML' , str ( Ii1iIiII1ii1 ) + '/wizard/0cache.xml' , 7 , ooOooo000oOO + 'XML.png' , i1iiIII111ii , '' )
 ooOOoooooo ( 'MIKEY1234 XML' , str ( Ii1iIiII1ii1 ) + '/wizard/mikey.xml' , 7 , ooOooo000oOO + 'XML.png' , i1iiIII111ii , '' )
 ooOOoooooo ( 'TUXENS XML' , str ( Ii1iIiII1ii1 ) + '/wizard/tuxens.xml' , 7 , ooOooo000oOO + 'XML.png' , i1iiIII111ii , '' )
 ooOOoooooo ( 'P2P RECOMMENDED XML1' , str ( Ii1iIiII1ii1 ) + '/wizard/p2p1.xml' , 7 , ooOooo000oOO + 'XML.png' , i1iiIII111ii , '' )
 ooOOoooooo ( 'P2P RECOMMENDED XML2' , str ( Ii1iIiII1ii1 ) + '/wizard/p2p2.xml' , 7 , ooOooo000oOO + 'XML.png' , i1iiIII111ii , '' )
 ooOOoooooo ( 'DELETE XML' , str ( Ii1iIiII1ii1 ) , 11 , ooOooo000oOO + 'XML.png' , i1iiIII111ii , '' )
 iiIiI ( 'movies' , 'MAIN' )
 if 63 - 63: o0oOO0O00o0O . oO0o / IIiIiII11i * OooO0OoOOOO + OoOo00o % Ii11Ii1I
def I1i11iIIi11 ( ) :
 O0O0O0OoOO ( )
 ooOOoooooo ( '[COLORgreen]My Local Zip[/COLOR]' , I11 , 48 , ooOooo000oOO + 'MB.png' , i1iiIII111ii , '' )
 ooOOoooooo ( '[COLORgreen]My Online Zip[/COLOR]' , i11 , 43 , ooOooo000oOO + 'MB.png' , i1iiIII111ii , '' )
 if 98 - 98: IIIi
def iiI1II11II1i ( ) :
 O0O0O0OoOO ( )
 ooOOoooooo ( 'INSTALL FTV GUIDE AND OTHER ADDONS REQUIRED' , str ( Ii1iIiII1ii1 ) + '/wizard/customftv/ftvguide-addons.zip' , 5 , ooOooo000oOO + 'FTV4.png' , i1iiIII111ii , '' )
 ooOOoooooo ( 'FTV GUIDE FIRST RUN SETTINGS' , str ( Ii1iIiII1ii1 ) + '/wizard/customftv/settings.xml' , 17 , ooOooo000oOO + 'FTV3.png' , i1iiIII111ii , '' )
 ooOOoooooo ( 'FTV GUIDE ADDONS2.INI UPDATE DAILY' , 'http://ren.byethost12.com/addons2.ini' , 16 , ooOooo000oOO + 'FTV1.png' , i1iiIII111ii , '' )
 ooOOoooooo ( 'RESET FTV DATABASE' , 'url' , 18 , ooOooo000oOO + 'FTV2.png' , i1iiIII111ii , '' )
 if 67 - 67: IIIii1II1II + I1ii11iIi11i
 if 84 - 84: o0o00Oo0O * ii - OooO0OoOOOO * OooO0OoOOOO
 if 8 - 8: O0OoO / ooOoO0O00 . OoOo00o
def i1I1IiI ( ) :
 O0O0O0OoOO ( )
 II1I ( '[COLORgreen]SKINS[/COLOR]' , str ( Ii1iIiII1ii1 ) , 33 , ooOooo000oOO + 'skinp.png' , i1iiIII111ii , '' )
 II1I ( '[COLORgreen]ARTWORK PACKS[/COLOR]' , str ( Ii1iIiII1ii1 ) , 34 , ooOooo000oOO + 'artp.png' , i1iiIII111ii , '' )
 II1I ( '[COLORgreen]CREATE UNIVERSAL PATHS[/COLOR]' , oooOOOOO , 35 , ooOooo000oOO + 'GUI.png' , i1iiIII111ii , '' )
 iiIiI ( 'movies' , 'MAIN' )
 if 66 - 66: oO0o
def oOO ( url ) :
 O000oo0O = iiI111I1iIiI ( I11I ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 Ii1i = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( O000oo0O )
 for iiI1IIIi , url , OOOOO0O00 , Iii , iIIIII1I in Ii1i :
  II1I ( iiI1IIIi , url , 5 , OOOOO0O00 , Iii , iIIIII1I )
 iiIiI ( 'movies' , 'MAIN' )
 if 6 - 6: Ii1I + OoOo00o
def Ii1iI11iI1 ( ) :
 O0O0O0OoOO ( )
 II1I ( '[COLORgreen]GOTHAM SKINS[/COLOR]' , str ( Ii1iIiII1ii1 ) , 36 , ooOooo000oOO + 'GSKIN.png' , i1iiIII111ii , '' )
 II1I ( '[COLORgreen]HELIX SKINS[/COLOR]' , str ( Ii1iIiII1ii1 ) , 37 , ooOooo000oOO + 'HSKIN.png' , i1iiIII111ii , '' )
 II1I ( '[COLORgreen]ISENGAARD SKINS[/COLOR]' , oooOOOOO , 38 , ooOooo000oOO + 'ISKIN.png' , i1iiIII111ii , '' )
 iiIiI ( 'movies' , 'MAIN' )
 if 5 - 5: iI11I1II1I1I
def OOoo00oO00 ( url ) :
 O000oo0O = iiI111I1iIiI ( str ( Ii1iIiII1ii1 ) + OO0oOOo ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 Ii1i = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( O000oo0O )
 for iiI1IIIi , url , OOOOO0O00 , Iii , iIIIII1I in Ii1i :
  II1I ( iiI1IIIi , url , 42 , OOOOO0O00 , Iii , iIIIII1I )
 iiIiI ( 'movies' , 'MAIN' )
 if 94 - 94: I11i + ii * iI1iI1I1i1I - I1ii11iIi11i . OooO0OoOOOO - I11i
def I1i11IiI11i1 ( url ) :
 O000oo0O = iiI111I1iIiI ( str ( Ii1iIiII1ii1 ) + OOoOoO00O0O0o ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 Ii1i = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( O000oo0O )
 for iiI1IIIi , url , OOOOO0O00 , Iii , iIIIII1I in Ii1i :
  II1I ( iiI1IIIi , url , 42 , OOOOO0O00 , Iii , iIIIII1I )
 iiIiI ( 'movies' , 'MAIN' )
 if 12 - 12: Ii1I + oO0o % iI1iI1I1i1I
def o0Ooo0o0ooo0 ( url ) :
 O000oo0O = iiI111I1iIiI ( str ( Ii1iIiII1ii1 ) + oo0o0000Oo0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 Ii1i = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( O000oo0O )
 for iiI1IIIi , url , OOOOO0O00 , Iii , iIIIII1I in Ii1i :
  II1I ( iiI1IIIi , url , 42 , OOOOO0O00 , Iii , iIIIII1I )
 iiIiI ( 'movies' , 'MAIN' )
 if 80 - 80: IIIi - I1ii11iIi11i
def OOooO ( url ) :
 O000oo0O = iiI111I1iIiI ( i1111 ( 'aHR0cHM6Ly9kbC5kcm9wYm94dXNlcmNvbnRlbnQuY29tL3MvN2ZrMjhndDlwb3QxMjJhL0JVSUxEUy50eHQ/ZGw9MA==' ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 Ii1i = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( O000oo0O )
 for iiI1IIIi , url , OOOOO0O00 , Iii , iIIIII1I in Ii1i :
  II1I ( iiI1IIIi , url , 42 , OOOOO0O00 , Iii , iIIIII1I )
 iiIiI ( 'movies' , 'MAIN' )
 if 79 - 79: IIIi % OoOo00o % I11i % Ii11Ii1I - IIiIiII11i * ii
def oOOO ( url ) :
 O000oo0O = iiI111I1iIiI ( str ( Ii1iIiII1ii1 ) + ooo0oooo0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 Ii1i = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( O000oo0O )
 for iiI1IIIi , url , OOOOO0O00 , Iii , iIIIII1I in Ii1i :
  II1I ( iiI1IIIi , url , 40 , OOOOO0O00 , Iii , iIIIII1I )
 iiIiI ( 'movies' , 'MAIN' )
 if 62 - 62: Ii1I + Ii11Ii1I + ooOoO0O00 / ii
def IIiiii ( url ) :
 O000oo0O = iiI111I1iIiI ( str ( Ii1iIiII1ii1 ) + iI111i1I1II ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 Ii1i = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( O000oo0O )
 for iiI1IIIi , url , OOOOO0O00 , Iii , iIIIII1I in Ii1i :
  II1I ( iiI1IIIi , url , 5 , OOOOO0O00 , Iii , iIIIII1I )
 iiIiI ( 'movies' , 'MAIN' )
 if 96 - 96: IIIi / I1ii11iIi11i * IIiIiII11i - o0oOO0O00o0O * I1ii11iIi11i
def o0Ii1Iii111IiI1 ( ) :
 II1I ( '[COLORgreen]APK (Android only)[/COLOR]' , str ( Ii1iIiII1ii1 ) , 2 , ooOooo000oOO + 'APK.png' , i1iiIII111ii , '' )
 II1I ( '[COLORgreen]APK Search[/COLOR]' , str ( Ii1iIiII1ii1 ) , 30038 , ooOooo000oOO + 'search.png' , i1iiIII111ii , '' )
 if 98 - 98: IIIi - ii % oOo0O0Ooo + o0o00Oo0O . Ii11Ii1I
def OoOO ( ) :
 I1i11i = IiIi ( i1111 ( 'aHR0cDovL3d3dy5hcGtjcmFmdC5jb20v' ) )
 Ii1i = re . compile ( 'href="(.+?)">Android Apps</a>' ) . findall ( I1i11i )
 I1 = re . compile ( 'href="(.+?)">Android Games</a>' ) . findall ( I1i11i )
 iIII1I1i1i = re . compile ( 'href="(.+?)">Wallpapers</a>' ) . findall ( I1i11i )
 o0O = re . compile ( 'href="(.+?)">Widgets</a>' ) . findall ( I1i11i )
 for OooOoOo in Ii1i :
  IIiI1I1 ( 'Android Apps' , OooOoOo , 30035 , ooOooo000oOO + 'apps.png' )
 for OooOoOo in I1 :
  IIiI1I1 ( 'Android Games' , OooOoOo , 30035 , ooOooo000oOO + 'GAMES.png' )
 for OooOoOo in iIII1I1i1i :
  IIiI1I1 ( 'Wallpapers' , OooOoOo , 30036 , ooOooo000oOO + 'wallpapers.png' )
 for OooOoOo in o0O :
  IIiI1I1 ( 'Widgets' , OooOoOo , 30036 , ooOooo000oOO + 'widgets.png' )
 iiIiI ( 'movies' , 'MAIN' )
def I11I1IIiiII1 ( url ) :
 I1i11i = IiIi ( url )
 Ii1i = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( I1i11i )
 for url , iiI1IIIi in Ii1i :
  if 'cat' in url :
   IIiI1I1 ( iiI1IIIi , url , 30036 , ooOooo000oOO + 'APK.png' )
def IIIIIii1ii11 ( url ) :
 I1i11i = IiIi ( url )
 Ii1i = re . compile ( 'src="(.+?)".+?href="(.+?)" title ="(.+?)"' , re . DOTALL ) . findall ( I1i11i )
 I1 = re . compile ( 'class="pagination_next"><a href="(.+?)">»</a></li>' ) . findall ( I1i11i )
 for IiI1iiiIii , url , iiI1IIIi in Ii1i :
  IIiI1I1 ( iiI1IIIi , url , 30037 , IiI1iiiIii )
 for url in I1 :
  IIiI1I1 ( 'NEXT PAGE' , url , 30036 , ooOooo000oOO + 'APK.png' )
def OOOooo0OooOoO ( url ) :
 I1i11i = IiIi ( url )
 Ii1i = re . compile ( '>Direct Download : <a  href="(.+?)">' ) . findall ( I1i11i )
 for url in Ii1i :
  oOoOOOo ( url )
def oOoOOOo ( url ) :
 I1i11i = IiIi ( url )
 Ii1i = re . compile ( 'href="(.+?)">Download APK from APKCRAFT</a></p>' ) . findall ( I1i11i )
 for url in Ii1i :
  ii1I ( url )
def o0OOoOoO00 ( ) :
 iii1 = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 ooO0oooOO0 = 'http://www.apkcraft.com/search/app/?search_text=' + ( iii1 ) . replace ( ' ' , '+' ) + '&search_type=1'
 o0o = ooO0oooOO0 . lower ( )
 IIIIIii1ii11 ( o0o )
 if 15 - 15: OooO0OoOOOO / o0o00Oo0O . I11i . Ii
def ii1I ( url ) :
 ii11I1 = xbmc . translatePath ( os . path . join ( o0OO0O0Oo , 'Download' ) )
 Oo0oO0ooo = xbmcgui . DialogProgress ( )
 Oo0oO0ooo . create ( "Your App Is Downloading" , "Why not check out our website" , '' , 'Http://architects.x10host.com' )
 OOOOO = os . path . join ( ii11I1 , iiI1IIIi + '.apk' )
 try :
  os . remove ( OOOOO )
 except :
  pass
 downloader . download ( url , OOOOO , Oo0oO0ooo )
 i1iiIIiiI111 = xbmcgui . Dialog ( )
 i1iiIIiiI111 . ok ( "GenieTv" , "[COLORred]Please press ok, exit kodi and go to your downloads folder to install your app[/COLOR]" , "[COLORblue]Tool Brought To You By GenieTv[/COLOR]" )
 if 67 - 67: OoOo00o % I11i . ii + IIIii1II1II * iI1iI1I1i1I * OOooOOo
def iiIii1I ( url ) :
 ii11I1 = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/resources/downloads' ) )
 Oo0oO0ooo = xbmcgui . DialogProgress ( )
 Oo0oO0ooo . create ( "Your fILM Is Downloading" , "Why not check out our website" , '' , 'Http://architects.x10host.com' )
 OOOOO = os . path . join ( ii11I1 , iiI1IIIi + '.mp4' )
 try :
  os . remove ( OOOOO )
 except :
  pass
 downloader . download ( url , OOOOO , Oo0oO0ooo )
 i1iiIIiiI111 = xbmcgui . Dialog ( )
 i1iiIIiiI111 . ok ( "GenieTv" , "[COLORred]Please press ok, Your download With Be Avaiilable Via The My Downloads Button[/COLOR]" , "[COLORblue]Tool Brought To You By GenieTv[/COLOR]" )
 if 47 - 47: O0OoO . iI1iI1I1i1I / I11i
 if 83 - 83: I11i / IIIii1II1II / IIIii1II1II + I11i * IIIi + I11i
def IIIIiii ( name , url , description ) :
 ii11I1 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 Oo0oO0ooo = xbmcgui . DialogProgress ( )
 Oo0oO0ooo . create ( "Your Art Pack Is Downloading" , "Why not check out our website" , '' , 'Http://architects.x10host.com' )
 OOOOO = os . path . join ( ii11I1 , name )
 try :
  os . remove ( OOOOO )
 except :
  pass
 downloader . download ( url , OOOOO , Oo0oO0ooo )
 oO0oIIIii1iiIi = xbmc . translatePath ( os . path . join ( oo00 ) )
 time . sleep ( 2 )
 Oo0oO0ooo . update ( 0 , "" , "Placing Your Art Please Wait" )
 print '======================================='
 print oO0oIIIii1iiIi
 print '======================================='
 extract . all ( OOOOO , oO0oIIIii1iiIi , Oo0oO0ooo )
 i1iiIIiiI111 = xbmcgui . Dialog ( )
 i1iiIIiiI111 . ok ( "GenieTv" , "[COLORred]Once complete your artwork will be stored in your Media folder, Accessible via the Homefolder, Enjoy[/COLOR]" )
 if 63 - 63: Ii1I
 if 6 - 6: O0OoO / Ii1I
def oOooO00o0O ( url ) :
 O000oo0O = iiI111I1iIiI ( Ii1iIiII1ii1 + ( i1111 ( 'L0dlbmllVHYvdGVzdC93aC50eHQ=' ) ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 Ii1i = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( O000oo0O )
 for iiI1IIIi , url , OOOOO0O00 , Iii , iIIIII1I in Ii1i :
  II1I ( iiI1IIIi , url , 5 , OOOOO0O00 , Iii , iIIIII1I )
 iiIiI ( 'movies' , 'INFO' )
 if 80 - 80: IIIii1II1II / iI1iI1I1i1I / OOooOOo + ooOoO0O00 - I1ii11iIi11i
 if 11 - 11: I11i * oO0o
def iIi1IiI ( url ) :
 O000oo0O = iiI111I1iIiI ( Ii1iIiII1ii1 + ( i1111 ( 'L0dlbmllVHYvdGVzdC93aC54bWw=' ) ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 Ii1i = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( O000oo0O )
 for iiI1IIIi , url , OOOOO0O00 , Iii , iIIIII1I in Ii1i :
  II1I ( iiI1IIIi , url , 30015 , OOOOO0O00 , Iii , iIIIII1I )
 iiIiI ( 'movies' , 'MAIN' )
 if 14 - 14: OooO0OoOOOO % OoOo00o % I1ii11iIi11i - Ii
def o0OO000ooOo ( url , iconimage , fanart ) :
 O000oo0O = iiI111I1iIiI ( url )
 o0OO0o0o00o = url
 IiI1iiiIii = iconimage
 fanart = fanart
 Ii1i = re . compile ( 'href="(.+?)">(.+?)</a>' ) . findall ( O000oo0O )
 for OooO0OO , iiI1IIIi in Ii1i :
  if '.mp4' in iiI1IIIi :
   ooOOoooooo ( 'Watch VIDEO' , url + '/' + OooO0OO , 222 , IiI1iiiIii , fanart , '' )
  if 'description' in iiI1IIIi :
   ooOOoooooo ( 'Read Description' , url + '/' + OooO0OO , 30017 , IiI1iiiIii , fanart , '' )
  if 'images' in iiI1IIIi :
   II1I ( 'View Images' , url + '/' + OooO0OO , 30018 , IiI1iiiIii , fanart , '' )
  if 'url' in iiI1IIIi :
   ooOOoooooo ( 'Install Build On Android' , url + '/' + OooO0OO , 30016 , IiI1iiiIii , fanart , '' )
  if 'url' in iiI1IIIi :
   ooOOoooooo ( 'Install Build On Pc' , url + '/' + OooO0OO , 30019 , IiI1iiiIii , fanart , '' )
 iiIiI ( 'movies' , 'INFO' )
 if 86 - 86: oO0o * ii
def OooO0oOo ( url ) :
 O000oo0O = iiI111I1iIiI ( url )
 Ii1i = re . compile ( 'url="(.+?)"' ) . findall ( O000oo0O )
 for url in Ii1i :
  oOOo00O0OOOo ( url )
  if 31 - 31: iI1iI1I1i1I % IIIii1II1II * iI1iI1I1i1I
def IiI ( url ) :
 O000oo0O = iiI111I1iIiI ( url )
 Ii1i = re . compile ( 'url="(.+?)"' ) . findall ( O000oo0O )
 for url in Ii1i :
  I1i1iii1Ii ( url )
  if 23 - 23: Ii
def II1I11IIi ( url ) :
 O000oo0O = iiI111I1iIiI ( url )
 Ii1i = re . compile ( 'desc="(.+?)"' ) . findall ( O000oo0O )
 for OoOOo in Ii1i :
  I1Ii ( 'Description:' , OoOOo )
  if 17 - 17: ooOoO0O00
def i1IIII1iii11I ( url ) :
 O000oo0O = iiI111I1iIiI ( url )
 url = url
 Ii1i = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( O000oo0O )
 for OooO0OO , iiI1IIIi in Ii1i :
  if 'png' in iiI1IIIi :
   ooOOoooooo ( 'image' , '' , '' , url + '/' + OooO0OO , url + '/' + OooO0OO , '' )
 iiIiI ( 'movies' , 'MAIN' )
 if 97 - 97: ii - IIIi
def oooo00 ( name , url , description ) :
 ii11I1 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 Oo0oO0ooo = xbmcgui . DialogProgress ( )
 Oo0oO0ooo . create ( "GenieTv" , "Downloading Content" , '' , 'Please Wait' )
 OOOOO = os . path . join ( ii11I1 , name + '.zip' )
 try :
  os . remove ( OOOOO )
 except :
  pass
 downloader . download ( url , OOOOO , Oo0oO0ooo )
 OO00O000OOO = xbmc . translatePath ( os . path . join ( 'special://home' , 'addons' ) )
 time . sleep ( 2 )
 Oo0oO0ooo . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print OO00O000OOO
 print '======================================='
 extract . all ( OOOOO , OO00O000OOO , Oo0oO0ooo )
 i1iiIIiiI111 = xbmcgui . Dialog ( )
 i1iiIIiiI111 . ok ( "GenieTv" , "Press ok to finish install" , "[COLOR yellow]Brought To You By GenieTv[/COLOR]" )
 oO00oooOOoOo0 ( )
 if 3 - 3: o0o00Oo0O
 if 64 - 64: ooOoO0O00 % O0OoO / Ii - ooOoO0O00 % IIIii1II1II . o0oOO0O00o0O
def I1i1iii1Ii ( url ) :
 ii11I1 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 Oo0oO0ooo = xbmcgui . DialogProgress ( )
 Oo0oO0ooo . create ( "GenieTv" , "Downloading " , '' , 'Please Wait' )
 OOOOO = os . path . join ( ii11I1 , 'plugin.program.GenieTv.install' + '.zip' )
 try :
  os . remove ( OOOOO )
 except :
  pass
 downloader . download ( url , OOOOO , Oo0oO0ooo )
 OO00O000OOO = xbmc . translatePath ( os . path . join ( 'special://' , 'home' ) )
 time . sleep ( 2 )
 Oo0oO0ooo . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print OO00O000OOO
 print '======================================='
 extract . all ( OOOOO , OO00O000OOO , Oo0oO0ooo )
 II1i111 ( url )
 i1iiIIiiI111 = xbmcgui . Dialog ( )
 i1iiIIiiI111 . ok ( "GenieTv" , "Press ok to force close kodi, if unsuccessful using windows Please kill kodi via taskmanager" , "[COLOR yellow]Brought To You By GenieTv[/COLOR]" )
 i1iiiIii11 ( )
 if 67 - 67: I11i % OOooOOo . OOooOOo - O0OoO
def oOOo00O0OOOo ( url ) :
 ii11I1 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 Oo0oO0ooo = xbmcgui . DialogProgress ( )
 Oo0oO0ooo . create ( "GenieTv" , "Downloading " , '' , 'Please Wait' )
 OOOOO = os . path . join ( ii11I1 , 'plugin.program.GenieTv.install' + '.zip' )
 try :
  os . remove ( OOOOO )
 except :
  pass
 downloader . download ( url , OOOOO , Oo0oO0ooo )
 OO00O000OOO = xbmc . translatePath ( os . path . join ( 'special://' , 'home' ) )
 time . sleep ( 2 )
 Oo0oO0ooo . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print OO00O000OOO
 print '======================================='
 extract . all ( OOOOO , OO00O000OOO , Oo0oO0ooo )
 II1i111 ( url )
 i1iiIIiiI111 = xbmcgui . Dialog ( )
 i1iiIIiiI111 . ok ( "GenieTv" , "Please Disconnect The Power From Your Device. DO NOT EXIT CLEANLY VIA SHUTDOWN" , "[COLOR yellow]Brought To You By GenieTv[/COLOR]" )
 if 90 - 90: O0OoO + IIiIiII11i * Ii1I / Ii11Ii1I . I11i + I11i
 if 40 - 40: O0OoO / OOooOOo % Ii % Ii1I / oOo0O0Ooo
def ooOOOOo0 ( name , url , description ) :
 OO00O000OOO = xbmc . translatePath ( os . path . join ( 'special://' , 'home' ) )
 Oo0oO0ooo = xbmcgui . DialogProgress ( )
 OOOOO = os . path . join ( I11 )
 time . sleep ( 2 )
 Oo0oO0ooo . create ( "GenieTv" , "Restoring" , '' , 'Please Wait' )
 print '======================================='
 print OO00O000OOO
 print '======================================='
 extract . all ( OOOOO , OO00O000OOO , Oo0oO0ooo )
 i1iiIIiiI111 = xbmcgui . Dialog ( )
 i1iiIIiiI111 . ok ( "GenieTv" , "Please Disconnect The Power From Your Device. DO NOT EXIT CLEANLY VIA SHUTDOWN" , "[COLOR yellow]Brought To You By GenieTv[/COLOR]" )
 if 38 - 38: ii / Ii1I . o0o00Oo0O / ooOoO0O00 / I1ii11iIi11i + iI11I1II1I1I
 if 96 - 96: o0oOO0O00o0O
def i1iiiIii11 ( ) :
 OO0ooOOO0OOO = xbmcgui . Dialog ( ) . yesno ( 'Force Close Kodi' , 'You are about to close Kodi' , 'Would you like to continue?' , nolabel = 'No, Cancel' , yeslabel = 'Yes, Close' )
 if OO0ooOOO0OOO == 0 :
  return
 elif OO0ooOOO0OOO == 1 :
  pass
 i1I11iIII1i1I = oOO0oo ( )
 print "Platform: " + str ( i1I11iIII1i1I )
 if i1I11iIII1i1I == 'osx' :
  print "############   try osx force close  #################"
  try : os . system ( 'killall -9 XBMC' )
  except : pass
  try : os . system ( 'killall -9 Kodi' )
  except : pass
  i1iiIIiiI111 . ok ( "[COLOR=red][B]WARNING  !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu." , '' )
 elif i1I11iIII1i1I == 'linux' :
  print "############   try linux force close  #################"
  try : os . system ( 'killall XBMC' )
  except : pass
  try : os . system ( 'killall Kodi' )
  except : pass
  try : os . system ( 'killall -9 xbmc.bin' )
  except : pass
  try : os . system ( 'killall -9 kodi.bin' )
  except : pass
  i1iiIIiiI111 . ok ( "[COLOR=red][B]WARNING  !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu." , '' )
 elif i1I11iIII1i1I == 'android' :
  print "############   try android force close  #################"
  try : os . system ( 'adb shell am force-stop org.xbmc.kodi' )
  except : pass
  try : os . system ( 'adb shell am force-stop org.kodi' )
  except : pass
  try : os . system ( 'adb shell am force-stop org.xbmc.xbmc' )
  except : pass
  try : os . system ( 'adb shell am force-stop org.xbmc' )
  except : pass
  i1iiIIiiI111 . ok ( "[COLOR=red][B]WARNING  !!![/COLOR][/B]" , "Your system has been detected as Android, you " , "[COLOR=yellow][B]MUST[/COLOR][/B] force close XBMC/Kodi. [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu." , "Pulling the power cable is the simplest method to force close." )
 elif i1I11iIII1i1I == 'windows' :
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
  i1iiIIiiI111 . ok ( "[COLOR=red][B]WARNING  !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu." , "Use task manager and NOT ALT F4" )
 else :
  print "############   try atv force close  #################"
  try : os . system ( 'killall AppleTV' )
  except : pass
  print "############   try raspbmc force close  #################"
  try : os . system ( 'sudo initctl stop kodi' )
  except : pass
  try : os . system ( 'sudo initctl stop xbmc' )
  except : pass
  i1iiIIiiI111 . ok ( "[COLOR=red][B]WARNING  !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit via the menu." , "Your platform could not be detected so just pull the power cable." )
  if 13 - 13: ii * OoOo00o - Ii11Ii1I / IIIii1II1II + iI1iI1I1i1I + OooO0OoOOOO
def oOO0oo ( ) :
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
  if 39 - 39: iI11I1II1I1I - ii
  if 81 - 81: Ii1I - o0o00Oo0O * ii
  if 23 - 23: IIiIiII11i / OoOo00o
def iII1Iii1I11i ( url ) :
 Oo0oO0ooo . create ( "[COLOR=green]GenieTv[/COLOR]" , "Renaming paths..." , '' , 'Please Wait' )
 for i1o0oooO , i1iI11i1IIi , ii1IIi111 in os . walk ( url ) :
  for file in ii1IIi111 :
   if file . endswith ( ".xml" ) :
    Oo0oO0ooo . update ( 0 , "Fixing" , file , 'Please Wait' )
    ooo0OiII1iii = open ( ( os . path . join ( i1o0oooO , file ) ) ) . read ( )
    ooOo = ooo0OiII1iii . replace ( oooOOOOO , 'special://home/' )
    I1iii11 = open ( ( os . path . join ( i1o0oooO , file ) ) , mode = 'w' )
    I1iii11 . write ( str ( ooOo ) )
    I1iii11 . close ( )
 i1iiiIii11 ( )
 if 84 - 84: IIIii1II1II
def o0OoO00 ( ) :
 I1i11i = IiIi ( i1111 ( 'aHR0cDovL3d3dy5saXN0ZW5saXZlLmV1Lw==' ) )
 Ii1i = re . compile ( '<a href="(.+?)">(.+?)</a></td></tr>' ) . findall ( I1i11i )
 for OooOoOo , iiI1IIIi in Ii1i :
  IIiI1I1 ( iiI1IIIi , 'http://www.listenlive.eu/' + OooOoOo , 10111113 , ooOooo000oOO + 'radio.png' )
def IIIIIiII1 ( url ) :
 I1i11i = IiIi ( url )
 Ii1i = re . compile ( '<tr>.+?<td><a href=".+?"><b>(.+?)</b>.+?<td><a href="(.+?)">' , re . DOTALL ) . findall ( I1i11i )
 for iiI1IIIi , url in Ii1i :
  iii11 ( iiI1IIIi , url , 222 , ooOooo000oOO + 'radio.png' )
  if 35 - 35: IIIi . OOooOOo * Ii
def iiII ( ) :
 I1i11i = IiIi ( i1111 ( 'aHR0cDovL3d3dy50b29uamV0LmNvbS8=' ) )
 Ii1i = re . compile ( '<a href="(.+?)" style="font-size:.8em;">(.+?)</a>' ) . findall ( I1i11i )
 for OooOoOo , iiI1IIIi in Ii1i :
  IIiI1I1 ( '[COLORgreen]' + iiI1IIIi + '[/COLOR]' , 'http://www.toonjet.com/' + OooOoOo , 8051 , ooOooo000oOO + 'classictoons.png' )
def o0Oii1111i ( url ) :
 I1i11i = IiIi ( url )
 Ii1i = re . compile ( '<a href="(.+?)"><img src="(.+?)"' ) . findall ( I1i11i )
 I1 = re . compile ( '<a href="(.+?)">.+?</a></td></tr></table>' ) . findall ( I1i11i )
 for url , IiI1iiiIii in Ii1i :
  if 'ol.gif' in IiI1iiiIii :
   pass
  elif 'link_block_' in IiI1iiiIii :
   pass
  elif '.png' in IiI1iiiIii :
   pass
  else :
   IIiI1I1 ( ( IiI1iiiIii ) . replace ( 'http://www.toonjet.com/images/icons/' , '' ) . replace ( 'images/icons/' , '' ) . replace ( '.jpg' , '' ) . replace ( '_icon' , '' ) . replace ( '_' , ' ' ) , 'http://www.toonjet.com/' + url , 8052 , ooOooo000oOO + 'vod.png' )
 for url in I1 :
  IIiI1I1 ( 'NEXT PAGE' , 'http://www.toonjet.com/' + url , 8051 , ooOooo000oOO + 'Next.png' )
def O0ooOO ( url ) :
 I1i11i = IiIi ( url )
 Ii1i = re . compile ( '<iframe width="640" height="480" src="(.+?)" frameborder="0" allowfullscreen></iframe>' ) . findall ( I1i11i )
 for url in Ii1i :
  iii11 ( '[COLORgreen]PLAY[/COLOR]' , ( url ) . replace ( 'http://www.youtube.com/embed/' , '' ) . replace ( '?autoplay=0' , '' ) , 8043 , ooOooo000oOO + 'classictoons.png' )
  if 28 - 28: Ii / I11i . iI11I1II1I1I / IIiIiII11i
  if 72 - 72: ii / oOo0O0Ooo + Ii11Ii1I / OOooOOo * Ii11Ii1I
def Ii1iIi111i1i1 ( ) :
 IIOO0ooOo0OoOo0 ( 'Audio Books' , '' , 30011 , ooOooo000oOO + 'audiobooks.png' , ooOooo000oOO + 'audiobooks.png' , '' )
 IIOO0ooOo0OoOo0 ( 'Kids Audio Books' , '' , 30006 , ooOooo000oOO + 'kidsaudiobooks.png' , ooOooo000oOO + 'kidsaudiobooks.png' , '' )
 if 87 - 87: OoOo00o . oOo0O0Ooo
def i1iIIIiiiI ( ) :
 IIOO0ooOo0OoOo0 ( 'All' , '' , 30001 , ooOooo000oOO + 'kodible.png' , ooOooo000oOO + 'kodible.png' , '' )
 IIOO0ooOo0OoOo0 ( 'Popular' , '' , 30012 , ooOooo000oOO + 'POPULARv.png' , ooOooo000oOO + 'POPULARv.png' , '' )
 IIOO0ooOo0OoOo0 ( 'Search' , '' , 30013 , ooOooo000oOO + 'search.png' , ooOooo000oOO + 'search.png' , '' )
 if 94 - 94: o0o00Oo0O - iI1iI1I1i1I - iI11I1II1I1I % O0OoO / Ii11Ii1I % o0oOO0O00o0O
def iIi1IIi1ii ( ) :
 o00OO00OoO = iiI111I1iIiI ( OooO0 + 'books' + ooOoOoo0O )
 Ii1i = re . compile ( '<NAME=>(.*?)</NAME><URL=>(.*?)</URL><CAT=>(.*?)</CAT>' ) . findall ( o00OO00OoO )
 for iiI1IIIi , OooOoOo , I11Ii in Ii1i :
  if 'Parent' in iiI1IIIi :
   pass
  elif '2' in I11Ii :
   IIOO0ooOo0OoOo0 ( ( iiI1IIIi ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , OooOoOo , 30010 , ooOooo000oOO + 'kodible.png' , ooOooo000oOO + 'kodible.png' , '' )
   if 16 - 16: I1ii11iIi11i / Ii
def oo00IIIIIIIiI ( ) :
 iii1 = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 o0o = iii1 . lower ( )
 o00OO00OoO = iiI111I1iIiI ( OooO0 + 'books' + ooOoOoo0O )
 Ii1i = re . compile ( '<NAME=>(.*?)</NAME><URL=>(.*?)</URL><CAT=>(.*?)</CAT>' ) . findall ( o00OO00OoO )
 for iiI1IIIi , OooOoOo , I11Ii in Ii1i :
  if iii1 in iiI1IIIi . lower ( ) :
   if '1' in I11Ii :
    IIOO0ooOo0OoOo0 ( ( iiI1IIIi ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , OooOoOo , 30010 , ooOooo000oOO + 'kodible.png' , ooOooo000oOO + 'kodible.png' , '' )
   elif '2' in I11Ii :
    IIOO0ooOo0OoOo0 ( ( iiI1IIIi ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , OooOoOo , 30010 , ooOooo000oOO + 'kodible.png' , ooOooo000oOO + 'kodible.png' , '' )
   elif '3' in I11Ii :
    IIOO0ooOo0OoOo0 ( ( iiI1IIIi ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , OooOoOo , 30009 , ooOooo000oOO + 'kodible.png' , ooOooo000oOO + 'kodible.png' , '' )
    if 12 - 12: o0oOO0O00o0O . OooO0OoOOOO . OOooOOo / o0o00Oo0O
    if 58 - 58: I11i - IIiIiII11i % OoOo00o + IIIi . OOooOOo / OooO0OoOOOO
def IIo00ooo ( ) :
 o00OO00OoO = iiI111I1iIiI ( OooO0 + 'books' + ooOoOoo0O )
 Ii1i = re . compile ( '<NAME=>(.*?)</NAME><URL=>(.*?)</URL><CAT=>(.*?)</CAT>' ) . findall ( o00OO00OoO )
 for iiI1IIIi , OooOoOo , I11Ii in Ii1i :
  if '1' in I11Ii :
   IIOO0ooOo0OoOo0 ( ( iiI1IIIi ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , OooOoOo , 3010 , ooOooo000oOO + 'kodible.png' , ooOooo000oOO + 'kodible.png' , '' )
  elif '2' in I11Ii :
   IIOO0ooOo0OoOo0 ( ( iiI1IIIi ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , OooOoOo , 30010 , ooOooo000oOO + 'kodible.png' , ooOooo000oOO + 'kodible.png' , '' )
  elif '3' in I11Ii :
   IIOO0ooOo0OoOo0 ( ( iiI1IIIi ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , OooOoOo , 30009 , ooOooo000oOO + 'kodible.png' , ooOooo000oOO + 'kodible.png' , '' )
   if 31 - 31: o0o00Oo0O * I11i % I11i / OoOo00o / iI1iI1I1i1I / oO0o
 xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 11 - 11: OOooOOo + OooO0OoOOOO - ii / oO0o
def iIIi1iI1I1IIi ( url ) :
 OooO0OO = url
 o00OO00OoO = iiI111I1iIiI ( url )
 I1 = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( o00OO00OoO )
 for url , iiI1IIIi in I1 :
  if 'mp3' in iiI1IIIi :
   II1I ( ( iiI1IIIi ) . replace ( '%20' , ' ' ) , OooO0OO + url , 10012 , ooOooo000oOO + 'kodible.png' , ooOooo000oOO + 'kodible.png' , '' )
  if 'wma' in iiI1IIIi :
   II1I ( ( iiI1IIIi ) . replace ( '%20' , ' ' ) , OooO0OO + url , 10012 , ooOooo000oOO + 'kodible.png' , ooOooo000oOO + 'kodible.png' , '' )
  if 'm4b' in iiI1IIIi :
   II1I ( ( iiI1IIIi ) . replace ( '%20' , ' ' ) , OooO0OO + url , 10012 , ooOooo000oOO + 'kodible.png' , ooOooo000oOO + 'kodible.png' , '' )
  elif '/' in iiI1IIIi :
   IIOO0ooOo0OoOo0 ( ( iiI1IIIi ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , OooO0OO + url , 30009 , ooOooo000oOO + 'kodible.png' , ooOooo000oOO + 'kodible.png' , '' )
   if 77 - 77: O0OoO / I1ii11iIi11i + O0OoO % I11i - oOo0O0Ooo * oOo0O0Ooo
   if 23 - 23: o0oOO0O00o0O . IIiIiII11i % Ii1I - ii * I1ii11iIi11i . iI11I1II1I1I
   if 37 - 37: o0oOO0O00o0O / I1ii11iIi11i . iI1iI1I1i1I * iI1iI1I1i1I
def o0O0Oo0Ooo0 ( url ) :
 o00OO00OoO = iiI111I1iIiI ( url )
 OooO0OO = url
 Ii1i = re . compile ( '<li><a href="(.+?)">(.+?)</a></li>' ) . findall ( o00OO00OoO )
 for url , iiI1IIIi in Ii1i :
  if 'Parent' in iiI1IIIi :
   pass
  elif '.db' in iiI1IIIi :
   pass
  elif '.jpg' in iiI1IIIi :
   pass
  elif '.html' in iiI1IIIi :
   pass
  elif '.doc' in iiI1IIIi :
   pass
  elif 'mp3' in iiI1IIIi :
   II1I ( ( iiI1IIIi ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , OooO0OO + url , 10012 , ooOooo000oOO + 'kodible.png' , ooOooo000oOO + 'kodible.png' , '' )
  elif 'm4a' in iiI1IIIi :
   II1I ( ( iiI1IIIi ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , OooO0OO + url , 10012 , ooOooo000oOO + 'kodible.png' , ooOooo000oOO + 'kodible.png' , '' )
  else :
   IIOO0ooOo0OoOo0 ( ( iiI1IIIi ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , OooO0OO + url , 30010 , ooOooo000oOO + 'kodible.png' , ooOooo000oOO + 'kodible.png' , '' )
   if 35 - 35: OooO0OoOOOO + ooOoO0O00 * OoOo00o - Ii11Ii1I . I1ii11iIi11i
   if 31 - 31: I11i
def Ii1IIiiIiiIi ( ) :
 IIOO0ooOo0OoOo0 ( 'A-Z' , '' , 30007 , ooOooo000oOO + 'kodible.png' , ooOooo000oOO + 'kodible.png' , '' )
 IIOO0ooOo0OoOo0 ( 'All' , '' , 30003 , ooOooo000oOO + 'kodible.png' , ooOooo000oOO + 'kodible.png' , '' )
 IIOO0ooOo0OoOo0 ( 'Search' , '' , 30014 , ooOooo000oOO + 'kodible.png' , ooOooo000oOO + 'kodible.png' , '' )
 if 40 - 40: I11i
def oOOo0oo0o0o0 ( ) :
 o00OO00OoO = iiI111I1iIiI ( i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9tcDNfZG93bmxvYWRzLmh0bQ==' ) )
 Ii1i = re . compile ( '<td width=".+?" align="center">.+?<a href="(.*?)">.+?<img border="0" src="images/Squeeze%20(.*?).gif" width="74" height=".*?"></a></td>' , re . DOTALL ) . findall ( o00OO00OoO )
 for OooOoOo , IiI1iiiIii in Ii1i :
  print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<' + OooOoOo + '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
  if '-x' in IiI1iiiIii :
   pass
  else :
   IIOO0ooOo0OoOo0 ( IiI1iiiIii , ( i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) ) + ( OooOoOo ) . replace ( 'colour_it' , 'books_audio/audio_books_a' ) , 30008 , ( i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9pbWFnZXMvU3F1ZWV6ZSUyMA==' ) ) + IiI1iiiIii + '.gif' , ooOooo000oOO + 'kodible.png' , '' )
   if 43 - 43: Ii1I / oOo0O0Ooo . O0OoO
 xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 62 - 62: iI11I1II1I1I + o0oOO0O00o0O . I1ii11iIi11i / OooO0OoOOOO % o0o00Oo0O . IIIi
 if 93 - 93: Ii % iI11I1II1I1I % Ii + I11i / I11i / IIiIiII11i
def I1i ( url ) :
 o00OO00OoO = iiI111I1iIiI ( url )
 Ii1i = re . compile ( '<td width=".*?" height=".*?"><b>.*?<a href="(.*?)">(.*?)</a></b></td>' , re . DOTALL ) . findall ( o00OO00OoO )
 for url , iiI1IIIi in Ii1i :
  if '</a>' in iiI1IIIi :
   pass
  elif '(' in iiI1IIIi :
   IIOO0ooOo0OoOo0 ( ( iiI1IIIi ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '.mp3' , '' ) , i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) + url , 30005 , ooOooo000oOO + 'kodible.png' , ooOooo000oOO + 'kodible.png' , '' )
  else :
   II1I ( ( iiI1IIIi ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '.mp3' , '' ) , i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) + url , 30004 , ooOooo000oOO + 'kodible.png' , ooOooo000oOO + 'kodible.png' , '' )
   if 59 - 59: ii . Ii11Ii1I / o0o00Oo0O - IIIii1II1II
 xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 1 - 1: OooO0OoOOOO / OooO0OoOOOO - Ii
def OO0oIiII1iiI ( ) :
 iii1 = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 o0o = iii1 . lower ( )
 o00OO00OoO = iiI111I1iIiI ( i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9jb21wbGV0ZV9saXN0Lmh0bQ==' ) )
 Ii1i = re . compile ( '<td width=".+?">.*?<b>.+?<a href="(.*?)">(.*?)</a></b></td>' , re . DOTALL ) . findall ( o00OO00OoO )
 for OooOoOo , iiI1IIIi in Ii1i :
  if iii1 in iiI1IIIi . lower ( ) :
   if '</a>' in iiI1IIIi :
    pass
   elif '(' in iiI1IIIi :
    IIOO0ooOo0OoOo0 ( ( iiI1IIIi ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + OooOoOo , 30005 , ooOooo000oOO + 'kodible.png' , ooOooo000oOO + 'kodible.png' , '' )
   else :
    II1I ( ( iiI1IIIi ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + OooOoOo , 30004 , ooOooo000oOO + 'kodible.png' , ooOooo000oOO + 'kodible.png' , '' )
    if 34 - 34: oOo0O0Ooo . OoOo00o + ooOoO0O00
    if 98 - 98: OoOo00o % OooO0OoOOOO * Ii % Ii1I
def iIiI1IIiii11 ( ) :
 o00OO00OoO = iiI111I1iIiI ( i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9jb21wbGV0ZV9saXN0Lmh0bQ==' ) )
 Ii1i = re . compile ( '<td width=".+?">.*?<b>.+?<a href="(.*?)">(.*?)</a></b></td>' , re . DOTALL ) . findall ( o00OO00OoO )
 for OooOoOo , iiI1IIIi in Ii1i :
  if '</a>' in iiI1IIIi :
   pass
  elif '(' in iiI1IIIi :
   IIOO0ooOo0OoOo0 ( ( iiI1IIIi ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + OooOoOo , 30005 , ooOooo000oOO + 'kodible.png' , ooOooo000oOO + 'kodible.png' , '' )
  else :
   II1I ( ( iiI1IIIi ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + OooOoOo , 30004 , ooOooo000oOO + 'kodible.png' , ooOooo000oOO + 'kodible.png' , '' )
   if 33 - 33: iI11I1II1I1I / o0oOO0O00o0O - oOo0O0Ooo * iI1iI1I1i1I
 xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 53 - 53: O0OoO
 if 98 - 98: IIIi
def o0oo0000 ( url ) :
 o00OO00OoO = iiI111I1iIiI ( url )
 Ii1i = re . compile ( '<a href="(.+?)">Download</a></b></td>' ) . findall ( o00OO00OoO )
 for url in Ii1i :
  OooO0OO = ( i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) ) + url
  Resolve ( OooO0OO )
  if 42 - 42: IIIi + IIIi * IIiIiII11i
def o0Oo ( url ) :
 o00OO00OoO = iiI111I1iIiI ( url )
 Ii1i = re . compile ( '<td width="247">(.*?)</td>.*?<a href="(.+?)">' , re . DOTALL ) . findall ( o00OO00OoO )
 for iiI1IIIi , url in Ii1i :
  if '<p align' in iiI1IIIi :
   pass
  elif '&nbsp;' in iiI1IIIi :
   pass
  else :
   II1I ( ( iiI1IIIi ) . replace ( '&nbsp;' , '' ) , i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) + url , 10012 , ooOooo000oOO + 'kodible.png' , ooOooo000oOO + 'kodible.png' , '' )
   if 57 - 57: IIIii1II1II / I1ii11iIi11i
 xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 69 - 69: OoOo00o - I1ii11iIi11i % OooO0OoOOOO
 if 50 - 50: ii
def IiI1i111IiIiIi1 ( ) :
 o00OO00OoO = cloudflare . source ( i1111 ( 'aHR0cDovL3dhdGNoY2FydG9vbnNvbmxpbmUuZXUv' ) )
 Ii1i = re . compile ( 'class="menu-item menu-item-type-.+?><a href="([^"]*)">(.+?)</a></li>' , re . DOTALL ) . findall ( o00OO00OoO )
 for OooOoOo , iiI1IIIi in Ii1i :
  if 'ongoing' in OooOoOo :
   II1I ( '[COLORgreen]' + iiI1IIIi + '[/COLOR]' , OooOoOo , 21005 , ooOooo000oOO + 'on-going.png' , '' , '' )
  if 'cartoon-series' in OooOoOo :
   II1I ( '[COLORgreen]' + iiI1IIIi + '[/COLOR]' , OooOoOo , 21005 , ooOooo000oOO + 'cartoonseries.png' , '' , '' )
  if 'disney' in OooOoOo :
   II1I ( '[COLORgreen]' + iiI1IIIi + '[/COLOR]' , OooOoOo , 21005 , ooOooo000oOO + 'disneytoons.png' , '' , '' )
  if 'genre' in OooOoOo :
   II1I ( '[COLORgreen]' + iiI1IIIi + '[/COLOR]' , OooOoOo , 21005 , ooOooo000oOO + 'cartoongenre.png' , '' , '' )
  if 'years' in OooOoOo :
   II1I ( '[COLORgreen]' + iiI1IIIi + '[/COLOR]' , OooOoOo , 21005 , ooOooo000oOO + 'years.png' , '' , '' )
def i1II11II1 ( url ) :
 o00OO00OoO = cloudflare . source ( url )
 Ii1i = re . compile ( '<a href="([^"]*)" title="([^"]*)" rel="nofollow" id="featured-thumbnail">.+?<div class="featured-thumbnail"><img width="140" height="200" src="([^"]*)"' , re . DOTALL ) . findall ( o00OO00OoO )
 II1IIIii = re . compile ( '<button type="button"><a href="([^"]*)" target="_blank">(.+?)</a>' ) . findall ( o00OO00OoO )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' ) . findall ( o00OO00OoO )
 for url , iiI1IIIi , IiI1iiiIii in Ii1i :
  II1I ( '[COLORgreen]' + iiI1IIIi + '[/COLOR]' , url , 21006 , IiI1iiiIii , IiI1iiiIii , iiI1IIIi )
 for url , iiI1IIIi in II1IIIii :
  II1I ( '[COLORgreen]' + iiI1IIIi + '[/COLOR]' , url , 21005 , ooOooo000oOO + 'watchcartoons.png' , '' , '' )
 for url in next :
  II1I ( '[COLORgreen]NEXT[/COLOR]' , url , 21005 , ooOooo000oOO + 'Next.png' , '' , '' )
def iIIIiIi1I1i ( url ) :
 o00OO00OoO = cloudflare . source ( url )
 Ii1i = re . compile ( '<li><a href="([^"]*)" >(.+?)</a></li>' , re . DOTALL ) . findall ( o00OO00OoO )
 OoOOoO0oOo = re . compile ( 'file:"([^"]*)",type:"mp4",label:"([^"]*)"' , re . DOTALL ) . findall ( o00OO00OoO )
 O0ooOOOO0O0 = re . compile ( 'src="([^"]*)" frameborder=' ) . findall ( o00OO00OoO )
 i1IIi1i1Ii1 = re . compile ( '<iframe src="([^"]*)"' ) . findall ( o00OO00OoO )
 for url , iiI1IIIi in Ii1i :
  II1I ( '[COLORgreen]' + iiI1IIIi + '[/COLOR]' , url , 21007 , ooOooo000oOO + 'watchcartoons.png' , '' , '' )
 for url in O0ooOOOO0O0 :
  II1I ( '[COLORgreen]PLAY[/COLOR]' , 'http:' + url , 222 , ooOooo000oOO + 'watchcartoons.png' , '' , '' )
 for url , iiI1IIIi in OoOOoO0oOo :
  ooOOoooooo ( '[COLORgreen]' + iiI1IIIi + '[/COLOR]' , url , 222 , ooOooo000oOO + 'watchcartoons.png' , '' , '' )
 else :
  II1I ( '[COLORgreen]NO STREAMS AVAILABLE[/COLOR]' , url , 21005 , ooOooo000oOO + 'watchcartoons.png' , '' , '' )
def Iiio0Oo0oO ( url ) :
 o00OO00OoO = cloudflare . source ( url )
 Ii1i = re . compile ( 'file:"([^"]*)",type:"mp4",label:"([^"]*)"' , re . DOTALL ) . findall ( o00OO00OoO )
 for url , iiI1IIIi in Ii1i :
  ooOOoooooo ( '[COLORgreen]' + iiI1IIIi + '[/COLOR]' , url , 222 , ooOooo000oOO + 'watchcartoons.png' , '' , '' )
  if 48 - 48: OoOo00o . I11i / OoOo00o
def Oo ( ) :
 IIiI1I1 ( '[COLORgreen]CARTOONS[/COLOR]' , '' , 20001 , ooOooo000oOO + 'ORIGINCARTOON.png' )
 IIiI1I1 ( '[COLORgreen]ANIME[/COLOR]' , 'https://kissanime.to/AnimeList' , 20001 , ooOooo000oOO + 'ORIGINCARTOON.png' )
 if 66 - 66: OooO0OoOOOO
def O0oOo ( ) :
 IIiI1I1 ( '[COLORgreen]BY NAME[/COLOR]' , 'http://kisscartoon.me/CartoonList' , 20002 , ooOooo000oOO + 'ORIGINCARTOON.png' )
 IIiI1I1 ( '[COLORgreen]BY GENRE[/COLOR]' , 'http://kisscartoon.me/CartoonList' , 20003 , ooOooo000oOO + 'ORIGINCARTOON.png' )
 if 68 - 68: Ii1I % ii % Ii1I + IIIi
def iIiIIi ( url ) :
 o00OO00OoO = cloudflare . source ( url )
 Ii1i = re . compile ( 'href="(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( o00OO00OoO )
 for url , iiI1IIIi in Ii1i :
  if '?c=' in url :
   IIiI1I1 ( '[COLORgreen]' + iiI1IIIi + '[/COLOR]' , 'http://kisscartoon.me' + url , 20004 , ooOooo000oOO + 'ORIGINCARTOON.png' )
   if 14 - 14: I11i / IIIii1II1II - iI11I1II1I1I - OoOo00o % O0OoO
def I1iIiI1IiIIII ( url ) :
 o00OO00OoO = cloudflare . source ( url )
 Ii1i = re . compile ( 'href="(.+?)" title="(.+?)">/n(.+?)</a><br/>' , re . DOTALL ) . findall ( o00OO00OoO )
 for url , I1iiIi111I , iiI1IIIi in Ii1i :
  if 'Genre' in url :
   IIiI1I1 ( '[COLORgreen]' + iiI1IIIi + '[/COLOR]' , 'http://kisscartoon.me' + url , 20004 , ooOooo000oOO + 'ORIGINCARTOON.png' )
   if 34 - 34: Ii - IIiIiII11i / oOo0O0Ooo % I11i
def iI1IiiiI11 ( url ) :
 o00OO00OoO = cloudflare . source ( url )
 Ii1i = re . compile ( 'src="(.+?)" style=.+?<a class="bigChar" href="(.+?)">(.+?)</a>.+?<p>(.+?)</p>' , re . DOTALL ) . findall ( o00OO00OoO )
 for url , I1iiIi111I , iiI1IIIi in Ii1i :
  II1I ( '[COLORgreen]' + iiI1IIIi + '[/COLOR]' , 'http://kisscartoon.me' + url , 20005 , img , '' , I1iiIi111I )
  if 80 - 80: OoOo00o + I11i * Ii11Ii1I + oO0o
def O0oOoOO0oo0O0OOO0 ( url ) :
 o00OO00OoO = cloudflare . source ( url )
 Ii1i = re . compile ( '<img width="120" height="165" src="(.+?)" style=.+?<a class="bigChar" href="(.+?)">(.+?)</a>.+?<p>(.+?)</p>' , re . DOTALL ) . findall ( o00OO00OoO )
 for url , I1iiIi111I , iiI1IIIi in Ii1i :
  II1I ( '[COLORgreen]' + iiI1IIIi + '[/COLOR]' , 'http://kisscartoon.me' + url , 20005 , img , '' , I1iiIi111I )
  if 76 - 76: Ii / OOooOOo + OOooOOo / ooOoO0O00 * oOo0O0Ooo
  if 12 - 12: IIIi % Ii + I11i + IIIi / iI1iI1I1i1I
  if 53 - 53: OooO0OoOOOO . IIIi % iI11I1II1I1I % OOooOOo % iI1iI1I1i1I
  if 53 - 53: IIIi
  if 69 - 69: OOooOOo . I11i . oOo0O0Ooo - Ii1I
def IiiiI ( ) :
 if 12 - 12: IIiIiII11i
 II1I ( '[COLORgreen]Cartoons[/COLOR]' , i1111 ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2NhcnRvb24=' ) , 10004 , ooOooo000oOO + 'ORIGINCARTOON.png' , i1iiIII111ii , '' )
 II1I ( '[COLORgreen]Search Cartoons[/COLOR]' , '' , 10005 , ooOooo000oOO + 'ORIGINCARTOON.png' , i1iiIII111ii , '' )
 if 2 - 2: ooOoO0O00 - oOo0O0Ooo + iI1iI1I1i1I . IIiIiII11i
def iIIiI1iiI ( ) :
 iii1 = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 o0o = iii1 . lower ( )
 o00OO00OoO = iiI111I1iIiI ( i1111 ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2NhcnRvb24=' ) )
 Ii1i = re . compile ( '<td><a href="(.+?)">(.+)</a></td>' ) . findall ( o00OO00OoO )
 for OooOoOo , iiI1IIIi in Ii1i :
  if iii1 in iiI1IIIi . lower ( ) :
   if 'Dad!' in iiI1IIIi :
    pass
   elif 'Family Guy' in iiI1IIIi :
    pass
   elif '2 Stupid' in iiI1IIIi :
    pass
   elif 'The Zelfs' in iiI1IIIi :
    pass
   elif 'A Clone' in iiI1IIIi :
    pass
   elif 'A.T.O.M' in iiI1IIIi :
    pass
   elif 'Almost Naked' in iiI1IIIi :
    pass
   elif 'Angry Kid' in iiI1IIIi :
    pass
   elif 'Annoying Orange' in iiI1IIIi :
    pass
   elif 'Aqua Teen' in iiI1IIIi :
    pass
   elif 'Assy Mcgee' in iiI1IIIi :
    pass
   elif 'Astroblast' in iiI1IIIi :
    pass
   elif 'Atomic Betty' in iiI1IIIi :
    pass
   elif 'Axe Cop' in iiI1IIIi :
    pass
   elif 'Baby Playpen' in iiI1IIIi :
    pass
   elif 'Beavis and Butt' in iiI1IIIi :
    pass
   elif 'Celebrity Deathmatch' in iiI1IIIi :
    pass
   elif 'Clerks The' in iiI1IIIi :
    pass
   elif 'Crapston Villas' in iiI1IIIi :
    pass
   elif 'Duckman:' in iiI1IIIi :
    pass
   elif 'Stripperella' in iiI1IIIi :
    pass
   elif 'Vixen' in iiI1IIIi :
    pass
   else :
    II1I ( '[COLORgreen]' + iiI1IIIi + '[/COLOR]' , OooOoOo , 10006 , ooOooo000oOO + 'ORIGINCARTOON.png' , i1iiIII111ii , '' )
  xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 18 - 18: o0oOO0O00o0O - OoOo00o % o0oOO0O00o0O / iI1iI1I1i1I
def O0Oo00OO00Ooo ( url ) :
 I1i11i = iiI111I1iIiI ( url )
 Ii1i = re . compile ( '<td><a href="(.+?)">(.+)</a></td>' ) . findall ( I1i11i )
 for url , iiI1IIIi in Ii1i :
  if 'Dad!' in iiI1IIIi :
   pass
  elif 'Family Guy' in iiI1IIIi :
   pass
  elif '2 Stupid' in iiI1IIIi :
   pass
  elif 'The Zelfs' in iiI1IIIi :
   pass
  elif 'A Clone' in iiI1IIIi :
   pass
  elif 'A.T.O.M' in iiI1IIIi :
   pass
  elif 'Almost Naked' in iiI1IIIi :
   pass
  elif 'Angry Kid' in iiI1IIIi :
   pass
  elif 'Annoying Orange' in iiI1IIIi :
   pass
  elif 'Aqua Teen' in iiI1IIIi :
   pass
  elif 'Assy Mcgee' in iiI1IIIi :
   pass
  elif 'Astroblast' in iiI1IIIi :
   pass
  elif 'Atomic Betty' in iiI1IIIi :
   pass
  elif 'Axe Cop' in iiI1IIIi :
   pass
  elif 'Baby Playpen' in iiI1IIIi :
   pass
  elif 'Beavis and Butt' in iiI1IIIi :
   pass
  elif 'Celebrity Deathmatch' in iiI1IIIi :
   pass
  elif 'Clerks The' in iiI1IIIi :
   pass
  elif 'Crapston Villas' in iiI1IIIi :
   pass
  elif 'Duckman:' in iiI1IIIi :
   pass
  elif 'Stripperella' in iiI1IIIi :
   pass
  elif 'Vixen' in iiI1IIIi :
   pass
  else :
   II1I ( '[COLORgreen]' + iiI1IIIi + '[/COLOR]' , url , 10006 , ooOooo000oOO + 'ORIGINCARTOON.png' , i1iiIII111ii , '' )
 xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 87 - 87: I1ii11iIi11i * IIIii1II1II % OooO0OoOOOO % OOooOOo
def iIi1Ii ( url ) :
 I1i11i = iiI111I1iIiI ( url )
 I1 = re . compile ( '<img src="(.+?)" id="series_image" width="250" height="370" alt=".+?" />' ) . findall ( I1i11i )
 for IiI1iiiIii in I1 :
  IiI1IIIII1I = IiI1iiiIii
 iIII1I1i1i = re . compile ( '<li><a href="(.+?)">Next</a></li>' ) . findall ( I1i11i )
 for url in iIII1I1i1i :
  II1I ( '[COLORgreen]NEXT PAGE[/COLOR]' , url , 10006 , ooOooo000oOO + 'Next.png' , i1iiIII111ii , '' )
 Ii1i = re . compile ( '&nbsp;<a href="(.+?)">(.+?)</a>' ) . findall ( I1i11i )
 for url , iiI1IIIi in Ii1i :
  iii11 ( '[COLORgreen]' + iiI1IIIi + '[/COLOR]' , url , 10007 , IiI1IIIII1I )
  if 35 - 35: Ii11Ii1I - Ii11Ii1I + ooOoO0O00 - o0o00Oo0O - IIIi
  if 58 - 58: OOooOOo - o0oOO0O00o0O - ii
 xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 96 - 96: iI11I1II1I1I
def OOOo00 ( url , IMAGE ) :
 I1i11i = iiI111I1iIiI ( url )
 Ii1i = re . compile ( '"playlist">(.+?)</span></div><div><iframe src="(.+?)"' ) . findall ( I1i11i )
 for iiI1IIIi , url in Ii1i :
  print iiI1IIIi + '     ' + url
  if 'easy' in url :
   OoIIi1iI ( url )
   if 92 - 92: oO0o * O0OoO
   if 35 - 35: Ii
  xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 99 - 99: IIiIiII11i . I11i + o0o00Oo0O
def OoIIi1iI ( url ) :
 I1i11i = iiI111I1iIiI ( url )
 Ii1i = re . compile ( "url: '(.+?)'," ) . findall ( I1i11i )
 for url in Ii1i :
  O00o0O ( url )
  if 32 - 32: I11i + OOooOOo - ii
  if 39 - 39: ii * IIIii1II1II * o0o00Oo0O . iI1iI1I1i1I . oO0o + O0OoO
  if 9 - 9: OOooOOo + OoOo00o % ii + I11i
def ooOO0o ( ) :
 if 51 - 51: I1ii11iIi11i - Ii1I * iI1iI1I1i1I
 II1I ( '[COLORgreen]Stand Up[/COLOR]' , '' , 10014 , ooOooo000oOO + 'ORIGINSTANDUP.png' , i1iiIII111ii , '' )
 II1I ( '[COLORgreen]Search Comedian[/COLOR]' , '' , 10015 , ooOooo000oOO + 'ORIGINSTANDUP.png' , i1iiIII111ii , '' )
 II1I ( '[COLORgreen]Others[/COLOR]' , '' , 10017 , ooOooo000oOO + 'ORIGINSTANDUP.png' , i1iiIII111ii , '' )
 if 12 - 12: iI11I1II1I1I % O0OoO % O0OoO
def o0i1iI1iiI1I ( ) :
 o00OO00OoO = iiI111I1iIiI ( ( i1111 ( 'aHR0cDovL2JhY2syYmFzaWNzYnVpbGQuY28udWsvdGVzdC9zdGFuZHVwbGlzdC5waHA=' ) ) )
 Ii1i = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( o00OO00OoO )
 for OooOoOo , IiI1iiiIii , iiI1IIIi in Ii1i :
  if 'elete' in iiI1IIIi :
   pass
  else :
   iii11 ( '[COLORgreen]' + iiI1IIIi + '[/COLOR]' , OooOoOo , 222 , IiI1iiiIii )
   if 52 - 52: oO0o % Ii11Ii1I * IIiIiII11i
def I1IiIii11I ( ) :
 iii1 = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 o0o = iii1 . lower ( )
 o00OO00OoO = iiI111I1iIiI ( ( i1111 ( 'aHR0cDovL3d3dy5jb3VjaHRyaXBwZXIuY29tL2ZvcnVtMi9wYWdlLnBocD9wYWdlPTM=' ) ) )
 i1iii1ii = re . compile ( '<tr>.+?<td width=".+?" align=".+?">.+?<img border=".+?" src="..(.+?)" width=".+?" height=".+?"></td>.+?<td width=".+?" valign=".+?" align=".+?"><font size=".+?">(.+?)</font></td>.+?<td width=".+?">(.+?)</td>' , re . DOTALL ) . findall ( o00OO00OoO )
 for IiI1iiiIii , II1 , i1iII1IiiIiI1 in i1iii1ii :
  for iii1 in II1 :
   print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< img >>>>>>>>>>>>>>>>>>>>>>>>>>'
   I11Iii1 = re . compile ( '<a href="(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( i1iII1IiiIiI1 )
   for OooOoOo , iiI1IIIi in I11Iii1 :
    if 'tube' in OooOoOo :
     pass
    elif 'stage' in OooOoOo :
     iii11 ( '[COLORgreen]' + II1 + '   -   ' + iiI1IIIi + '[/COLOR]' , ( OooOoOo ) . replace ( '" target="_blank' , '' ) , 10016 , 'http://couchtripper.com/' + IiI1iiiIii , )
    elif 'vee' in OooOoOo :
     pass
     if 16 - 16: Ii11Ii1I * oO0o / OoOo00o
def II1iiI ( ) :
 o00OO00OoO = iiI111I1iIiI ( ( i1111 ( 'aHR0cDovL3d3dy5jb3VjaHRyaXBwZXIuY29tL2ZvcnVtMi9wYWdlLnBocD9wYWdlPTM=' ) ) )
 i1iii1ii = re . compile ( '<tr>.+?<td width=".+?" align=".+?">.+?<img border=".+?" src="..(.+?)" width=".+?" height=".+?"></td>.+?<td width=".+?" valign=".+?" align=".+?"><font size=".+?">(.+?)</font></td>.+?<td width=".+?">(.+?)</td>' , re . DOTALL ) . findall ( o00OO00OoO )
 for IiI1iiiIii , II1 , i1iII1IiiIiI1 in i1iii1ii :
  I11Iii1 = re . compile ( '<a href="(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( i1iII1IiiIiI1 )
  for OooOoOo , iiI1IIIi in I11Iii1 :
   if 'tube' in OooOoOo :
    pass
   elif 'stage' in OooOoOo :
    iii11 ( '[COLORgreen]' + II1 + '   -   ' + iiI1IIIi + '[/COLOR]' , ( OooOoOo ) . replace ( '" target="_blank' , '' ) , 10016 , 'http://couchtripper.com/' + IiI1iiiIii )
   elif 'vee' in OooOoOo :
    pass
    if 31 - 31: I11i % iI1iI1I1i1I + iI11I1II1I1I + Ii * IIIi
    if 45 - 45: IIIii1II1II * IIIi . O0OoO - IIIi + OooO0OoOOOO
 xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 34 - 34: IIIii1II1II . I1ii11iIi11i
def OOoO0oO00o ( url ) :
 o00OO00OoO = iiI111I1iIiI ( url )
 print '>>>>>>>>>>>>>>>>>>>>>>>>' + url + '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'
 oOOOo00O00O = re . compile ( "url\[.+?\] = '(.+?)';" ) . findall ( o00OO00OoO )
 print '>>>>>>>>>>>>>>>>>>>>>>>' + ( str ( oOOOo00O00O ) ) + '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
 for url in oOOOo00O00O :
  O00o0O ( ( url ) . replace ( '[' , '' ) . replace ( ']' , '' ) . replace ( '\'' , '' ) )
  if 10 - 10: oO0o
  if 22 - 22: Ii / o0o00Oo0O
  if 94 - 94: O0OoO * iI1iI1I1i1I - OooO0OoOOOO . iI11I1II1I1I
  if 66 - 66: O0OoO - IIIii1II1II * OOooOOo / OoOo00o * IIiIiII11i * oO0o
  if 91 - 91: ii / Ii11Ii1I . oOo0O0Ooo + O0OoO . IIiIiII11i
  if 45 - 45: OoOo00o * OOooOOo / iI11I1II1I1I
  if 77 - 77: IIIi - iI1iI1I1i1I
def iiI1iI1I ( ) :
 if 27 - 27: Ii1I * IIIi - oO0o + Ii11Ii1I * Ii11Ii1I
 o0OO0O0OO0oO0 ( '[COLOR darkgoldenrod]Open Pandora\'s Box[/COLOR]' , '' , 10029 , 'https://encrypted-tbn1.gstatic.com/images?q=tbn%3AANd9GcTQ9r4TA8yIw9ggxuwsHxWojo6tPVfgTe8QIOxOQwzNR2TavtCi6Q' , i1iiIII111ii , '' )
 o0OO0O0OO0oO0 ( '[COLOR darkgoldenrod]Search[/COLOR]' , '' , 10026 , 'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png' , i1iiIII111ii , '' )
 if 9 - 9: OoOo00o % Ii / I1ii11iIi11i
 iiIiI ( 'movies' , 'MAIN' )
 if 20 - 20: OoOo00o * o0o00Oo0O + iI1iI1I1i1I - ii . iI1iI1I1i1I
def oOII1ii1ii11I1 ( ) :
 o0OO0O0OO0oO0 ( 'Search Pandoras Films' , '' , 10027 , 'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png' , i1iiIII111ii , '' )
 o0OO0O0OO0oO0 ( 'Search Pandoras TV' , '' , 10028 , 'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png' , i1iiIII111ii , '' )
 if 88 - 88: Ii1I
 iiIiI ( 'movies' , 'MAIN' )
def oOOooooo0OoO0 ( ) :
 if 11 - 11: ooOoO0O00 % oO0o % o0oOO0O00o0O
 iii1 = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 o0o = iii1 . lower ( )
 O0Oo0 = [ '480p' , '720p' , '1080p' , 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' , '720paction' , '720padventure' , '720panimation' , '720pcomedy' , '720pcrime' , '720pdocumentary' , '720pdrama' , '720pfamily' , '720pfantasy' , '720phorror' , '720pmystery' , '720promance' , '720psci-Fi' , '720psport' , '720pthriller' , '720pwestern' , '1080paction' , '1080padventure' , '1080panimation' , '1080pcomedy' , '1080pcrime' , '1080pdocumentary' , '1080pdrama' , '1080pfamily' , '1080pfantasy' , '1080phorror' , '1080pmystery' , '1080promance' , '1080psci-Fi' , '1080psport' , '1080pthriller' , '1080pwestern' , 'films' ]
 if 80 - 80: oOo0O0Ooo - iI11I1II1I1I . IIIii1II1II + oO0o - IIIi
 for iI1iIiiiI1I1 in O0Oo0 :
  OOOOOo = IIIII + iI1iIiiiI1I1 + ooOoOoo0O
  o00OO00OoO = O000OO0 ( OOOOOo )
  Ii1i = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( o00OO00OoO )
  for OooOoOo , OOOOO0O00 , iIII , Iii , iiI1IIIi in Ii1i :
   if iii1 in iiI1IIIi . lower ( ) :
    I1IiiiIiI ( iiI1IIIi , OooOoOo , 222 , OOOOO0O00 , Iii , iIII )
    if 77 - 77: Ii11Ii1I / IIiIiII11i - Ii11Ii1I / IIIii1II1II
    iiIiI ( 'movies' , 'MAIN' )
    xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
    if 97 - 97: IIIii1II1II / OoOo00o . IIiIiII11i
    if 44 - 44: Ii11Ii1I % iI1iI1I1i1I . IIIi
def Ii11Iii ( ) :
 if 68 - 68: oOo0O0Ooo % o0o00Oo0O
 iii1 = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 o0o = iii1 . lower ( )
 O0Oo0 = [ 'tvnum' , 'a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' , 'p' , 'q' , 'r' , 's' , 't' , 'u' , 'v' , 'w' , 'x' , 'y' , 'z' ]
 if 74 - 74: ooOoO0O00 + OOooOOo + iI11I1II1I1I * OOooOOo * iI11I1II1I1I + iI1iI1I1i1I
 for iI1iIiiiI1I1 in O0Oo0 :
  Oo0o = IIIII + iI1iIiiiI1I1 + ooOoOoo0O
  o00OO00OoO = O000OO0 ( Oo0o )
  Ii1i = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( o00OO00OoO )
  for iiI1IIIi , iIII , OooOoOo , IiI1iiiIii , Iii , IiI1I1I in Ii1i :
   if iii1 in iiI1IIIi . lower ( ) :
    o0OO0O0OO0oO0 ( iiI1IIIi , OooOoOo , IiI1I1I , IiI1iiiIii , Iii , iIII )
    if 62 - 62: OooO0OoOOOO * o0o00Oo0O
    iiIiI ( 'movies' , 'MAIN' )
    xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
    if 86 - 86: Ii1I * IIiIiII11i * iI1iI1I1i1I
    if 74 - 74: Ii1I / OooO0OoOOOO
def oo0oO0oO ( ) :
 if 48 - 48: OOooOOo % Ii1I / iI1iI1I1i1I . iI11I1II1I1I * IIiIiII11i
 I1i11i = iiI111I1iIiI ( IIIII + 'spongemain.php' )
 Ii1i = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( I1i11i )
 for iiI1IIIi , iIII , OooOoOo , IiI1iiiIii , Iii , IiI1I1I in Ii1i :
  o0OO0O0OO0oO0 ( iiI1IIIi , OooOoOo , IiI1I1I , IiI1iiiIii , Iii , iIII )
  iiIiI ( 'movies' , 'MAIN' )
def oo000oO ( url ) :
 if 78 - 78: Ii11Ii1I + OOooOOo + OooO0OoOOOO - OooO0OoOOOO . Ii / oO0o
 xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
 I11i11i1 = ( '%s%s' % ( OOO , url ) )
 O000oo0O = iiI111I1iIiI ( url )
 Ii1i = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( O000oo0O )
 for url , OOOOO0O00 , iIII , ii1i1iiI , iiI1IIIi in Ii1i :
  I1IiiiIiI ( iiI1IIIi , url , 222 , OOOOO0O00 , ii1i1iiI , iIII )
  if 94 - 94: ooOoO0O00 * ooOoO0O00 % IIiIiII11i + IIIii1II1II
  iiIiI ( 'movies' , 'MAIN' )
  if 28 - 28: oOo0O0Ooo
  xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 49 - 49: iI1iI1I1i1I . I11i % OoOo00o / Ii11Ii1I
  if 95 - 95: o0o00Oo0O * OOooOOo * OooO0OoOOOO . O0OoO / iI11I1II1I1I
def I1IIi1I ( url ) :
 if 14 - 14: OoOo00o + o0o00Oo0O / OooO0OoOOOO
 I1i11i = iiI111I1iIiI ( url )
 Ii1i = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( I1i11i )
 for iiI1IIIi , iIII , url , IiI1iiiIii , Iii , IiI1I1I in Ii1i :
  o0OO0O0OO0oO0 ( iiI1IIIi , url , IiI1I1I , IiI1iiiIii , Iii , iIII )
  if 24 - 24: oO0o - OoOo00o + Ii1I / o0oOO0O00o0O % oOo0O0Ooo + iI11I1II1I1I
  iiIiI ( 'movies' , 'MAIN' )
  if 79 - 79: OOooOOo / O0OoO
  if 77 - 77: I1ii11iIi11i
 xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 46 - 46: IIIi
def I1IiiiIiI ( name , url , mode , iconimage , fanart , description ) :
 if 72 - 72: o0oOO0O00o0O * IIIii1II1II
 oooo = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 iiiIIIii = True
 ooOoo00 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 ooOoo00 . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 ooOoo00 . setProperty ( "Fanart_Image" , fanart )
 iiiIIIii = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = oooo , listitem = ooOoo00 , isFolder = False )
 return iiiIIIii
 if 34 - 34: IIiIiII11i + O0OoO * iI11I1II1I1I - IIIi - oO0o
def o0OO0O0OO0oO0 ( name , url , mode , iconimage , fanart , description ) :
 if 69 - 69: iI11I1II1I1I * oOo0O0Ooo - o0oOO0O00o0O + o0o00Oo0O + o0o00Oo0O
 oooo = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 iiiIIIii = True
 ooOoo00 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 ooOoo00 . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 ooOoo00 . setProperty ( "Fanart_Image" , fanart )
 iiiIIIii = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = oooo , listitem = ooOoo00 , isFolder = True )
 return iiiIIIii
if 65 - 65: IIIi / Ii / oO0o - IIIii1II1II
if 9 - 9: oOo0O0Ooo / IIIi - I1ii11iIi11i * iI11I1II1I1I
if 86 - 86: IIiIiII11i + O0OoO + OooO0OoOOOO
if 9 - 9: O0OoO + IIiIiII11i % O0OoO % OooO0OoOOOO + iI11I1II1I1I
if 59 - 59: ooOoO0O00
if 48 - 48: o0o00Oo0O * Ii11Ii1I * oO0o . oO0o * iI1iI1I1i1I - Ii11Ii1I
if 14 - 14: Ii1I + Ii
if 83 - 83: Ii1I / Ii + IIiIiII11i . o0oOO0O00o0O * IIIii1II1II + OooO0OoOOOO
if 42 - 42: ooOoO0O00 % IIiIiII11i . O0OoO
if 7 - 7: Ii1I - OoOo00o * IIIii1II1II + I11i . Ii1I
if 85 - 85: o0o00Oo0O
if 32 - 32: ii . oO0o / I1ii11iIi11i * I11i / I11i * Ii11Ii1I
if 19 - 19: Ii11Ii1I
if 55 - 55: IIIii1II1II % IIIii1II1II / o0o00Oo0O % o0oOO0O00o0O - I11i . I1ii11iIi11i
if 49 - 49: iI11I1II1I1I * ooOoO0O00 . ii
def OOOO0oOo00O ( string ) :
 if iiiiiIIii == 'true' :
  xbmc . log ( "[addon.live.GenieTV-%s]: %s" % ( addon_version , string ) )
  if 32 - 32: OooO0OoOOOO % Ii11Ii1I - oOo0O0Ooo
def oo0ooooo00o ( name , url , iconimage , fanart , mode , playlist = None , regexs = None ) :
 OoOo = [ ]
 try :
  if 26 - 26: IIIii1II1II
  name = name . encode ( 'utf-8' , 'ignore' )
 except :
  pass
 if os . path . exists ( I11i1 ) == False :
  OOOO0oOo00O ( 'Making Favorites File' )
  OoOo . append ( ( name , url , iconimage , fanart , mode , playlist , regexs ) )
  ooo0OiII1iii = open ( I11i1 , "w" )
  ooo0OiII1iii . write ( json . dumps ( OoOo ) )
  ooo0OiII1iii . close ( )
 else :
  OOOO0oOo00O ( 'Appending Favorites' )
  ooo0OiII1iii = open ( I11i1 ) . read ( )
  Oo0oOo000OoO0 = json . loads ( ooo0OiII1iii )
  Oo0oOo000OoO0 . append ( ( name , url , iconimage , fanart , mode ) )
  ooOo = open ( I11i1 , "w" )
  ooOo . write ( json . dumps ( Oo0oOo000OoO0 ) )
  ooOo . close ( )
  if 25 - 25: Ii1I . ooOoO0O00 . IIiIiII11i / IIIi
  if 54 - 54: ooOoO0O00 . iI1iI1I1i1I - Ii1I + O0OoO + I1ii11iIi11i / I1ii11iIi11i
def i1ii1IiiiiIi1I ( ) :
 if os . path . exists ( I11i1 ) == False :
  OoOo = [ ]
  OOOO0oOo00O ( 'Making Favorites File' )
  OoOo . append ( ( 'Genie Tv Favourites Section' , '' , '' , '' , '' , '' , '' ) )
  ooo0OiII1iii = open ( I11i1 , "w" )
  ooo0OiII1iii . write ( json . dumps ( OoOo ) )
  ooo0OiII1iii . close ( )
 else :
  ooo0O0o0OoOO = json . loads ( open ( I11i1 ) . read ( ) )
  iIi11i = len ( ooo0O0o0OoOO )
  for o0o00o0Oo in ooo0O0o0OoOO :
   iiI1IIIi = o0o00o0Oo [ 0 ]
   OooOoOo = o0o00o0Oo [ 1 ]
   OOOOO0O00 = o0o00o0Oo [ 2 ]
   try :
    OOOOOooOOoo = o0o00o0Oo [ 3 ]
    if OOOOOooOOoo == None :
     raise
   except :
    if o0oO0 . getSetting ( 'use_thumb' ) == "true" :
     OOOOOooOOoo = OOOOO0O00
    else :
     OOOOOooOOoo = Iii
   try : i1I1iIii11 = o0o00o0Oo [ 5 ]
   except : i1I1iIii11 = None
   try : oOoO0O0oO = o0o00o0Oo [ 6 ]
   except : oOoO0O0oO = None
   if 92 - 92: I1ii11iIi11i / Ii + Ii1I
   if o0o00o0Oo [ 4 ] == 0 :
    II1I ( iiI1IIIi , OooOoOo , '' , OOOOO0O00 , Iii , '' , 'fav' )
   else :
    II1I ( iiI1IIIi , OooOoOo , o0o00o0Oo [ 4 ] , OOOOO0O00 , Iii , '' , 'fav' )
    if 87 - 87: OOooOOo % iI11I1II1I1I
def o0OO0OOO0O ( name ) :
 Oo0oOo000OoO0 = json . loads ( open ( I11i1 ) . read ( ) )
 for Iii1I in range ( len ( Oo0oOo000OoO0 ) ) :
  if Oo0oOo000OoO0 [ Iii1I ] [ 0 ] == name :
   del Oo0oOo000OoO0 [ Iii1I ]
   ooOo = open ( I11i1 , "w" )
   ooOo . write ( json . dumps ( Oo0oOo000OoO0 ) )
   ooOo . close ( )
   break
 xbmc . executebuiltin ( "XBMC.Container.Refresh" )
 if 75 - 75: OooO0OoOOOO
 if 35 - 35: oOo0O0Ooo
def III1ii1I ( ) :
 iiII1iiIi = os . path . join ( OOooO0OOoo , 'addons.ini' )
 iI1i1I1III1i = open ( iiII1iiIi , "w+" )
 if 68 - 68: Ii11Ii1I - OoOo00o + I1ii11iIi11i
 iI1i1I1III1i . write ( r'# This file contains the "built-in" channels' + '\n' )
 iI1i1I1III1i . write ( r'# It is parsed by Pythons ConfigParser' + '\n\n' )
 iI1i1I1III1i . write ( r'[plugin.video.GenieTv]' + '\n' )
 iI1i1I1III1i . write ( r'BBC One=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F191.m3u8&mode=10012&name=[COLORgreen]BBC+One%0D[%2FCOLOR]' + '\n' )
 iI1i1I1III1i . write ( r'BBC Two=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F190.m3u8&mode=10012&name=[COLORgreen]BBC+Two%0D[%2FCOLOR]' + '\n' )
 iI1i1I1III1i . write ( r'BBC Four=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F188.m3u8&mode=10012&name=[COLORgreen]BBC+Four%0D[%2FCOLOR]' + '\n' )
 iI1i1I1III1i . write ( r'ITV=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F208.m3u8&mode=10012&name=[COLORgreen]ITV1%0D[%2FCOLOR]' + '\n' )
 iI1i1I1III1i . write ( r'ITV2=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F207.m3u8&mode=10012&name=[COLORgreen]ITV2%0D[%2FCOLOR]' + '\n' )
 iI1i1I1III1i . write ( r'ITV3=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F206.m3u8&mode=10012&name=[COLORgreen]ITV3%0D[%2FCOLOR]' + '\n' )
 iI1i1I1III1i . write ( r'ITV4=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F205.m3u8&mode=10012&name=[COLORgreen]ITV4%0D[%2FCOLOR]' + '\n' )
 iI1i1I1III1i . write ( r'Channel 4=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F183.m3u8&mode=10012&name=[COLORgreen]Channel+4%0D[%2FCOLOR]' + '\n' )
 iI1i1I1III1i . write ( r'Channel 5=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F185.m3u8&mode=10012&name=[COLORgreen]Channel+5%0D[%2FCOLOR]' + '\n' )
 iI1i1I1III1i . write ( r'5STAR=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F187.m3u8&mode=10012&name=[COLORgreen]5%2A%0D[%2FCOLOR]' + '\n' )
 iI1i1I1III1i . write ( r'5 USA=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F186.m3u8&mode=10012&name=[COLORgreen]5USA%0D[%2FCOLOR]' + '\n' )
 iI1i1I1III1i . write ( r'RTE One=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F194.m3u8&mode=10012&name=[COLORgreen]RTE+One%0D[%2FCOLOR]' + '\n' )
 iI1i1I1III1i . write ( r'RTE Two=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F193.m3u8&mode=10012&name=[COLORgreen]RTE+Two%0D[%2FCOLOR]' + '\n' )
 iI1i1I1III1i . write ( r'TG4=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F192.m3u8&mode=10012&name=[COLORgreen]TG4%0D[%2FCOLOR]' + '\n' )
 iI1i1I1III1i . write ( r'Sky1=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F32.m3u8&mode=10012&name=[COLORgreen]Sky+1%0D[%2FCOLOR]' + '\n' )
 iI1i1I1III1i . write ( r'Sky2=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F33.m3u8&mode=10012&name=[COLORgreen]Sky+2%0D[%2FCOLOR]' + '\n' )
 iI1i1I1III1i . write ( r'Sky Living=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F35.m3u8&mode=10012&name=[COLORgreen]Sky+Living%0D[%2FCOLOR]' + '\n' )
 iI1i1I1III1i . write ( r'Sky Atlantic=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F34.m3u8&mode=10012&name=[COLORgreen]Sky+Atlantic%0D[%2FCOLOR]' + '\n' )
 iI1i1I1III1i . write ( r'Dave=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F325.m3u8&mode=10012&name=[COLORgreen]Dave%0D[%2FCOLOR]' + '\n' )
 iI1i1I1III1i . write ( r'Pick=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F324.m3u8&mode=10012&name=[COLORgreen]Pick%0D[%2FCOLOR]' + '\n' )
 iI1i1I1III1i . write ( r'GOLD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F326.m3u8&mode=10012&name=[COLORgreen]Gold%0D[%2FCOLOR]' + '\n' )
 iI1i1I1III1i . write ( r'Watch HD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F518.m3u8&mode=10012&name=[COLORgreen]Watch%0D[%2FCOLOR]' + '\n' )
 iI1i1I1III1i . write ( r'YESTERDAY=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F377.m3u8&mode=10012&name=[COLORgreen]Yesterday%0D[%2FCOLOR]' + '\n' )
 iI1i1I1III1i . write ( r'Comedy Central=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F181.m3u8&mode=10012&name=[COLORgreen]Comedy+Central%0D[%2FCOLOR]' + '\n' )
 iI1i1I1III1i . write ( r'London Live=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F830.m3u8&mode=10012&name=[COLORgreen]London+Live%0D[%2FCOLOR]' + '\n' )
 iI1i1I1III1i . write ( r'Disney Junior=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F230.m3u8&mode=10012&name=[COLORgreen]Disney+Jr.%0D[%2FCOLOR]' + '\n' )
 iI1i1I1III1i . write ( r'Disney Chnl=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F231.m3u8&mode=10012&name=[COLORgreen]Disney+Channel%0D[%2FCOLOR]' + '\n' )
 iI1i1I1III1i . write ( r'Animal Planet=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F198.m3u8&mode=10012&name=[COLORgreen]Animal+Planet%0D[%2FCOLOR]' + '\n' )
 iI1i1I1III1i . write ( r'Nat Geo=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F197.m3u8&mode=10012&name=[COLORgreen]National+Geographic+Channel%0D[%2FCOLOR]' + '\n' )
 iI1i1I1III1i . write ( r'Discovery=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F200.m3u8&mode=10012&name=[COLORgreen]Discovery+Channel%0D[%2FCOLOR]' + '\n' )
 iI1i1I1III1i . write ( r'Discovery Science=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F199.m3u8&mode=10012&name=[COLORgreen]Discovery+Science%0D[%2FCOLOR]' + '\n' )
 iI1i1I1III1i . write ( r'Disc.Turbo=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F168.m3u8&mode=10012&name=[COLORgreen]Discovery+Turbo%0D[%2FCOLOR]' + '\n' )
 iI1i1I1III1i . write ( r'Food Network=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F639.m3u8&mode=10012&name=[COLORgreen]Food+Network%0D[%2FCOLOR]' + '\n' )
 iI1i1I1III1i . write ( r'MTV MUSIC=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F234.m3u8&mode=10012&name=[COLORgreen]MTV+Music%0D[%2FCOLOR]' + '\n' )
 iI1i1I1III1i . write ( r'Film4=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F182.m3u8&mode=10012&name=[COLORgreen]Film4%0D[%2FCOLOR]' + '\n' )
 iI1i1I1III1i . write ( r'True Movies=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F853.m3u8&mode=10012&name=[COLORgreen]True+Movies%0D[%2FCOLOR]' + '\n' )
 iI1i1I1III1i . write ( r'True Movies 2=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F852.m3u8&mode=10012&name=[COLORgreen]True+Movies+2%0D[%2FCOLOR]' + '\n' )
 iI1i1I1III1i . write ( r'Sky Action=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F732.m3u8&mode=10012&name=[COLORgreen]Sky+Movies+Action+%26+Adventure%0D[%2FCOLOR]' + '\n' )
 iI1i1I1III1i . write ( r'Sky ScFiHorror=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F511.m3u8&mode=10012&name=[COLORgreen]Sky+Movies+Sci-Fi+%26+Horror%0D[%2FCOLOR]' + '\n' )
 iI1i1I1III1i . write ( r'SkyPremiereHD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F516.m3u8&mode=10012&name=[COLORgreen]Sky+Movies+Premiere%0D[%2FCOLOR]' + '\n' )
 iI1i1I1III1i . write ( r'Sky Greats=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F512.m3u8&mode=10012&name=[COLORgreen]Sky+Movies+Greats%0D[%2FCOLOR]' + '\n' )
 iI1i1I1III1i . write ( r'Sky Family=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F509.m3u8&mode=10012&name=[COLORgreen]Sky+Movies+Family%0D[%2FCOLOR]' + '\n' )
 iI1i1I1III1i . write ( r'Sky DramaRom=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F510.m3u8&mode=10012&name=[COLORgreen]Sky+Movies+Drama+%26+Romance%0D[%2FCOLOR]' + '\n' )
 iI1i1I1III1i . write ( r'Sky Thriller=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F514.m3u8&mode=10012&name=[COLORgreen]Sky+Movies+Crime+%26+Thriller%0D[%2FCOLOR]' + '\n' )
 iI1i1I1III1i . write ( r'Sky Comedy=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F513.m3u8&mode=10012&name=[COLORgreen]Sky+Movies+Comedy%0D[%2FCOLOR]' + '\n' )
 iI1i1I1III1i . write ( r'Sky Showcase=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F46.m3u8&mode=10012&name=[COLORgreen]Sky+Movies+Showcase%0D[%2FCOLOR]' + '\n' )
 iI1i1I1III1i . write ( r'Sky Select=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F45.m3u8&mode=10012&name=[COLORgreen]Sky+Movies+Select%0D[%2FCOLOR]' + '\n' )
 iI1i1I1III1i . write ( r'Sky Disney=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F195.m3u8&mode=10012&name=[COLORgreen]Sky+Movies+Disney%0D[%2FCOLOR]' + '\n' )
 iI1i1I1III1i . write ( r'Sky Sports 1=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F18.m3u8&mode=10012&name=[COLORgreen]Sky+Sports+1%0D[%2FCOLOR]' + '\n' )
 iI1i1I1III1i . write ( r'Sky Sports 2=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F19.m3u8&mode=10012&name=[COLORgreen]Sky+Sports+2%0D[%2FCOLOR]' + '\n' )
 iI1i1I1III1i . write ( r'Sky Sports 3=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F20.m3u8&mode=10012&name=[COLORgreen]Sky+Sports+3%0D[%2FCOLOR]' + '\n' )
 iI1i1I1III1i . write ( r'Sky Sports 4=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F21.m3u8&mode=10012&name=[COLORgreen]Sky+Sports+4%0D[%2FCOLOR]' + '\n' )
 iI1i1I1III1i . write ( r'Sky Sports 5=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F22.m3u8&mode=10012&name=[COLORgreen]Sky+Sports+5%0D[%2FCOLOR]' + '\n' )
 iI1i1I1III1i . write ( r'Sky Sports F1=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F24.m3u8&mode=10012&name=[COLORgreen]Sky+Sports+F1%0D[%2FCOLOR]' + '\n' )
 iI1i1I1III1i . write ( r'Sky Sports News=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F23.m3u8&mode=10012&name=[COLORgreen]Sky+Sports+News%0D[%2FCOLOR]' + '\n' )
 iI1i1I1III1i . write ( r'BT Sport 1=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F309.m3u8&mode=10012&name=[COLORgreen]BT+Sport+1%0D[%2FCOLOR]' + '\n' )
 iI1i1I1III1i . write ( r'BT Sport 2=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F26.m3u8&mode=10012&name=[COLORgreen]BT+Sport+2%0D[%2FCOLOR]' + '\n' )
 iI1i1I1III1i . write ( r'BT Sport Europe=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F705.m3u8&mode=10012&name=[COLORgreen]BT+Sport+Europe%0D[%2FCOLOR]' + '\n' )
 iI1i1I1III1i . write ( r'BT Sport ESPN=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F28.m3u8&mode=10012&name=[COLORgreen]BT+Sport+ESPN%0D[%2FCOLOR]' + '\n' )
 iI1i1I1III1i . write ( r'Box Nation=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F173.m3u8&mode=10012&name=[COLORgreen]Box+Nation%0D[%2FCOLOR]' + '\n' )
 iI1i1I1III1i . write ( r'WWENetwork=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F178.m3u8&mode=10012&name=[COLORgreen]WWENetwork%0D[%2FCOLOR]' + '\n' )
 iI1i1I1III1i . write ( r'Eurosport=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F269.m3u8&mode=10012&name=[COLORgreen]Eurosport+1%0D[%2FCOLOR]' + '\n' )
 iI1i1I1III1i . write ( r'Eurosport 2=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F748.m3u8&mode=10012&name=[COLORgreen]Eurosport+2%0D[%2FCOLOR]' + '\n' )
 iI1i1I1III1i . write ( r'At The Races=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F170.m3u8&mode=10012&name=[COLORgreen]At+the+Races%0D[%2FCOLOR]' + '\n' )
 iI1i1I1III1i . write ( r'Racing UK=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F171.m3u8&mode=10012&name=[COLORgreen]Racing+UK%0D[%2FCOLOR]' + '\n' )
 iI1i1I1III1i . write ( r'Poker central US=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F826.m3u8&mode=10012&name=[COLORgreen]Poker+central+US%0D[%2FCOLOR]' + '\n' )
 if 44 - 44: Ii11Ii1I * I11i * IIiIiII11i
 if 5 - 5: ooOoO0O00 + o0o00Oo0O % o0o00Oo0O * o0o00Oo0O + OOooOOo % ooOoO0O00
def O0OOo ( ) :
 I1i11i = iiI111I1iIiI ( i1111 ( 'aHR0cDovL2dlbmlldHYuY28udWsvMjQ3c3RyZWFtLm0zdQ==' ) )
 Ii1i = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( I1i11i )
 for iiI1IIIi , OooOoOo in Ii1i :
  ooOOoooooo ( iiI1IIIi , ( OooOoOo ) . strip ( ) , 222 , ooOooo000oOO + '247.png' , ooOooo000oOO + '247.png' , '' )
def I1ii11I ( ) :
 I1i11i = iiI111I1iIiI ( i1111 ( 'aHR0cDovL2dlbmlldHYuY28udWsvbXVzaWMubTN1' ) )
 Ii1i = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( I1i11i )
 for iiI1IIIi , OooOoOo in Ii1i :
  ooOOoooooo ( iiI1IIIi , ( OooOoOo ) . strip ( ) , 222 , ooOooo000oOO + 'musicch.png' , ooOooo000oOO + 'musicch.png' , '' )
def II1II1IIII ( ) :
 I1i11i = iiI111I1iIiI ( i1111 ( 'aHR0cDovL2dlbmlldHYuY28udWsvbmV3cy5tM3U=' ) )
 Ii1i = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( I1i11i )
 for iiI1IIIi , OooOoOo in Ii1i :
  ooOOoooooo ( iiI1IIIi , ( OooOoOo ) . strip ( ) , 222 , ooOooo000oOO + 'NEWS.png' , ooOooo000oOO + 'NEWS.png' , '' )
def i1iiiiI1IiIIii ( ) :
 I1i11i = iiI111I1iIiI ( i1111 ( 'aHR0cDovL2dlbmlldHYuY28udWsvYWR1bHQubTN1' ) )
 Ii1i = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( I1i11i )
 for iiI1IIIi , OooOoOo in Ii1i :
  ooOOoooooo ( iiI1IIIi , ( OooOoOo ) . strip ( ) , 222 , ooOooo000oOO + 'adult.png' , ooOooo000oOO + 'adult.png' , '' )
def IIIIiiiIi11Ii1iI ( ) :
 I1i11i = iiI111I1iIiI ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9pVHZfU3RyZWFtcy9UVVRTL21haW4ucGhw' ) )
 Ii1i = re . compile ( 'href="/watch?v=(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( I1i11i )
 for OooOoOo , iiI1IIIi in Ii1i :
  ooOOoooooo ( iiI1IIIi , OooOoOo , 1016 , ooOooo000oOO + 'TUTS.png' , ooOooo000oOO + 'TUTS.png' , '' )
  if 87 - 87: I1ii11iIi11i + o0o00Oo0O - iI1iI1I1i1I * iI11I1II1I1I . IIIi % I11i
  if 83 - 83: IIiIiII11i * ooOoO0O00 * o0oOO0O00o0O . Ii1I / iI1iI1I1i1I + ooOoO0O00
def i1Iio0oO00 ( ) :
 if 88 - 88: iI1iI1I1i1I + Ii % OoOo00o * IIIii1II1II * IIIii1II1II * Ii11Ii1I
 II1I ( '[COLORgreen]Recent Episodes[/COLOR]' , '' , 10019 , ooOooo000oOO + 'dtv.png' , i1iiIII111ii , '' )
 II1I ( '[COLORgreen]Genres[/COLOR]' , '' , 10020 , ooOooo000oOO + 'dtv.png' , i1iiIII111ii , '' )
 II1I ( '[COLORgreen]Search[/COLOR]' , '' , 10021 , ooOooo000oOO + 'dtv.png' , i1iiIII111ii , '' )
 if 24 - 24: O0OoO / o0oOO0O00o0O + OooO0OoOOOO . OooO0OoOOOO
def I1ii1i ( ) :
 if 22 - 22: OoOo00o * Ii11Ii1I * Ii + o0oOO0O00o0O * OOooOOo * oO0o
 I1i11i = cloudflare . source ( i1111 ( 'aHR0cDovL2RpemlsYWIuY29t' ) )
 Ii1i = re . compile ( '<li id=".+?">.+?<a href="(.+?)">.+?<img width="40" height="40" src="(.+?)" alt=""/>.+?<span class="title">\n(.+?)</span>.+?<span class="alt-title">\n(.+?)</span>.+?</a>.+?</li>' , re . DOTALL ) . findall ( I1i11i )
 for OooOoOo , IiI1iiiIii , iiI1IIIi , ii1 in Ii1i :
  II1I ( iiI1IIIi + '  -  ' + ( ii1 ) . replace ( 'sezon' , 'Season' ) . replace ( 'bölüm' , 'Episode' ) , OooOoOo , 10023 , ooOooo000oOO + 'dtv.png' , i1iiIII111ii , '' )
  if 85 - 85: o0oOO0O00o0O * IIIii1II1II % I1ii11iIi11i - o0oOO0O00o0O - iI1iI1I1i1I
  if 46 - 46: o0o00Oo0O
  if 65 - 65: iI11I1II1I1I % OoOo00o + o0o00Oo0O / ii
def O0000oO0o00 ( ) :
 if 80 - 80: ii + OooO0OoOOOO
 II1I ( '[COLORgreen]Action[/COLOR]' , 'Aksiyon' , 10024 , ooOooo000oOO + 'dtv.png' , i1iiIII111ii , '' )
 II1I ( '[COLORgreen]Adventure[/COLOR]' , 'Macera' , 10024 , ooOooo000oOO + 'dtv.png' , i1iiIII111ii , '' )
 II1I ( '[COLORgreen]Animation[/COLOR]' , 'Animasyon' , 10024 , ooOooo000oOO + 'dtv.png' , i1iiIII111ii , '' )
 II1I ( '[COLORgreen]Anime[/COLOR]' , 'Anime' , 10024 , ooOooo000oOO + 'dtv.png' , i1iiIII111ii , '' )
 II1I ( '[COLORgreen]Biography[/COLOR]' , 'Biyografi' , 10024 , ooOooo000oOO + 'dtv.png' , i1iiIII111ii , '' )
 II1I ( '[COLORgreen]Comedy[/COLOR]' , 'Komedi' , 10024 , ooOooo000oOO + 'dtv.png' , i1iiIII111ii , '' )
 II1I ( '[COLORgreen]Crime[/COLOR]' , 'Su%C3%A7' , 10024 , ooOooo000oOO + 'dtv.png' , i1iiIII111ii , '' )
 II1I ( '[COLORgreen]Documentary[/COLOR]' , 'Belgesel' , 10024 , ooOooo000oOO + 'dtv.png' , i1iiIII111ii , '' )
 II1I ( '[COLORgreen]Drama[/COLOR]' , 'Dram' , 10024 , ooOooo000oOO + 'dtv.png' , i1iiIII111ii , '' )
 II1I ( '[COLORgreen]Family[/COLOR]' , 'Aile' , 10024 , ooOooo000oOO + 'dtv.png' , i1iiIII111ii , '' )
 II1I ( '[COLORgreen]Fantasy[/COLOR]' , 'Fantastik' , 10024 , ooOooo000oOO + 'dtv.png' , i1iiIII111ii , '' )
 II1I ( '[COLORgreen]History[/COLOR]' , 'Tarih' , 10024 , ooOooo000oOO + 'dtv.png' , i1iiIII111ii , '' )
 II1I ( '[COLORgreen]Horror[/COLOR]' , 'Korku' , 10024 , ooOooo000oOO + 'dtv.png' , i1iiIII111ii , '' )
 II1I ( '[COLORgreen]Mini-Series[/COLOR]' , 'Mini%20Dizi' , 10024 , ooOooo000oOO + 'dtv.png' , i1iiIII111ii , '' )
 II1I ( '[COLORgreen]Musical[/COLOR]' , 'M%C3%BCzikal' , 10024 , ooOooo000oOO + 'dtv.png' , i1iiIII111ii , '' )
 II1I ( '[COLORgreen]Mystery[/COLOR]' , 'Gizem' , 10024 , ooOooo000oOO + 'dtv.png' , i1iiIII111ii , '' )
 II1I ( '[COLORgreen]Romance[/COLOR]' , 'Romantik' , 10024 , ooOooo000oOO + 'dtv.png' , i1iiIII111ii , '' )
 II1I ( '[COLORgreen]Science Fiction[/COLOR]' , 'Bilim%20Kurgu' , 10024 , ooOooo000oOO + 'dtv.png' , i1iiIII111ii , '' )
 II1I ( '[COLORgreen]Sport[/COLOR]' , 'Spor' , 10024 , ooOooo000oOO + 'dtv.png' , i1iiIII111ii , '' )
 II1I ( '[COLORgreen]Thriller[/COLOR]' , 'Gerilim' , 10024 , ooOooo000oOO + 'dtv.png' , i1iiIII111ii , '' )
 II1I ( '[COLORgreen]War[/COLOR]' , 'Sava%C5%9F' , 10024 , ooOooo000oOO + 'dtv.png' , i1iiIII111ii , '' )
 II1I ( '[COLORgreen]Western[/COLOR]' , 'Tarih' , 10024 , ooOooo000oOO + 'dtv.png' , i1iiIII111ii , '' )
 II1I ( '[COLORgreen]Youth[/COLOR]' , 'Gen%C3%A7lik' , 10024 , ooOooo000oOO + 'dtv.png' , i1iiIII111ii , '' )
 if 95 - 95: IIIi / OoOo00o * IIIi - ii * ii % oO0o
def iI1I1I1i1i ( url ) :
 o0OO0o0o00o = 'http://dizilab.com/arsiv?limit=100&tur=' + url + '&orderby=&ulke=&order=&yil=&dizi_adi='
 o00OO00OoO = cloudflare . source ( o0OO0o0o00o )
 Ii1i = re . compile ( '<div class="tv-series-single">.+?<a href="(.+?)" class="film-image">.+?<img src="(.+?)" alt=""/>.+?<span class="position">.+?</span>\n(.+?)</a>' , re . DOTALL ) . findall ( o00OO00OoO )
 for url , IiI1iiiIii , iiI1IIIi in Ii1i :
  II1I ( '[COLORgreen]' + iiI1IIIi + '[/COLOR]' , url , 10022 , ooOooo000oOO + 'dtv.png' , i1iiIII111ii , '' )
  if 87 - 87: OOooOOo / OooO0OoOOOO . O0OoO - IIIii1II1II / oO0o
  if 41 - 41: IIiIiII11i
  if 27 - 27: I1ii11iIi11i * OOooOOo % iI11I1II1I1I . oOo0O0Ooo
  if 70 - 70: iI1iI1I1i1I % IIiIiII11i % o0o00Oo0O . ooOoO0O00 / IIIi
def OO0ooOoOO0OOo ( ) :
 if 51 - 51: iI11I1II1I1I * I11i / iI11I1II1I1I . iI11I1II1I1I . o0oOO0O00o0O * iI1iI1I1i1I
 iii1 = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 o0o = iii1 . lower ( )
 OooOoOo = ( i1111 ( 'aHR0cDovL2RpemlsYWIuY29tL2Fyc2l2P2xpbWl0PSZ0dXI9Jm9yZGVyYnk9JnVsa2U9Jm9yZGVyPSZ5aWw9JmRpemlfYWRpPQ==' ) ) + ( iii1 ) . replace ( ' ' , '+' )
 o00OO00OoO = cloudflare . source ( OooOoOo )
 Ii1i = re . compile ( '<a href="(.+?)" class="film-image">\n<img src="(.+?)" alt=""/>\n</a>\n<div class="tss-detail">\n<a class="title" style="" href=".+?">\n<span class="position">.+?</span>\n(.+?)</a>' ) . findall ( o00OO00OoO )
 for OooOoOo , IiI1iiiIii , iiI1IIIi in Ii1i :
  if iii1 in iiI1IIIi . lower ( ) :
   II1I ( '[COLORgreen]' + iiI1IIIi + '[/COLOR]' , OooOoOo , 10022 , ooOooo000oOO + 'dtv.png' )
   if 93 - 93: OoOo00o * Ii11Ii1I
   if 27 - 27: oOo0O0Ooo * O0OoO
   if 77 - 77: OooO0OoOOOO
def Ooi1I11 ( url ) :
 o00OO00OoO = cloudflare . source ( url )
 Ii1i = re . compile ( '<a class="season" href="(.+?)">\n(.+?)\n</a>.+?<a class="episode" href=".+?">\n(.+?)\n</a>.+?<a class="episode-name" href=".+?">\n(.+?)</a>' , re . DOTALL ) . findall ( o00OO00OoO )
 for OooO0OO , iII11ii1ii , oOO0OOOo000o , iiI1IIIi in Ii1i :
  OO00oo = ( oOO0OOOo000o ) . replace ( 'Sezon' , '' ) . replace ( 'bölüm' , '' ) . replace ( 'Bölüm' , '' ) . replace ( 'BÃ¶lÃ¼m' , '' ) . replace ( '.' , '' )
  O0Oo0O0 = ( iII11ii1ii ) . replace ( 'bölüm' , '' ) . replace ( 'Sezon' , '' ) . replace ( 'Bölüm' , '' ) . replace ( 'BÃ¶lÃ¼m' , '' ) . replace ( '.' , '' )
  I1IiiIiii1 = 'Season ' + O0Oo0O0 + 'Episode ' + OO00oo + iiI1IIIi
  i11i ( I1IiiIiii1 , OooO0OO )
  if 86 - 86: Ii11Ii1I
  xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 29 - 29: iI11I1II1I1I - oO0o + oOo0O0Ooo % iI11I1II1I1I % IIIii1II1II
  if 84 - 84: OooO0OoOOOO + Ii1I + Ii11Ii1I + o0oOO0O00o0O
def i11i ( name , url ) :
 OooO0OO = url
 ooOOo0o = name
 OOOO0OOoO0O0 = cloudflare . source ( OooO0OO )
 I1 = re . compile ( 'file: "(.+?)",.+?label: "(.+?)",' , re . DOTALL ) . findall ( OOOO0OOoO0O0 )
 for oOOOo00O00O , IiI1Iii1 in I1 :
  iii11 ( '[COLORgreen]' + ooOOo0o + IiI1Iii1 + '[/COLOR]' , oOOOo00O00O , 10012 , ooOooo000oOO + 'dtv.png' )
  if 85 - 85: Ii / Ii . oO0o . o0o00Oo0O
 xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 67 - 67: IIiIiII11i / I11i . IIIii1II1II . ii
 if 19 - 19: OooO0OoOOOO . Ii1I / OOooOOo
def O00oo ( ) :
 if 75 - 75: iI11I1II1I1I * Ii - ii . OOooOOo
 if 70 - 70: OoOo00o * OoOo00o + I1ii11iIi11i * IIIii1II1II % oOo0O0Ooo + iI11I1II1I1I
 if 2 - 2: Ii
 if 98 - 98: OoOo00o / oO0o - Ii11Ii1I - oOo0O0Ooo / OOooOOo + Ii
 if 17 - 17: iI1iI1I1i1I
 if 97 - 97: Ii1I * Ii1I / o0oOO0O00o0O
 if 6 - 6: OoOo00o
 if 72 - 72: iI1iI1I1i1I * Ii1I - OOooOOo / Ii1I + IIIii1II1II - o0oOO0O00o0O
 if 49 - 49: oO0o - o0o00Oo0O / oO0o * OOooOOo + IIIi
 if 35 - 35: IIiIiII11i . oOo0O0Ooo / ooOoO0O00 / oOo0O0Ooo * OoOo00o
 if 85 - 85: IIiIiII11i . O0OoO % IIIii1II1II % iI1iI1I1i1I
 if 80 - 80: OoOo00o * iI1iI1I1i1I / iI11I1II1I1I % OoOo00o / iI11I1II1I1I
 if 42 - 42: ooOoO0O00 / Ii . I1ii11iIi11i * o0oOO0O00o0O . Ii * o0o00Oo0O
 if 44 - 44: ooOoO0O00 . oOo0O0Ooo / Ii + OooO0OoOOOO
 if 27 - 27: IIIii1II1II
 II1I ( '[COLORgreen]Newest Episodes Added[/COLOR]' , 'http://www.watchseries.li/latest' , 10046 , ooOooo000oOO + 'WATCHSERIES.png' , '' , '' )
 II1I ( '[COLORgreen]This Week\'s Popular Episodes[/COLOR]' , 'http://www.watchseries.li/new' , 10042 , ooOooo000oOO + 'WATCHSERIES.png' , '' , '' )
 II1I ( '[COLORgreen]Search Program[/COLOR]' , '' , 10043 , ooOooo000oOO + 'WATCHSERIES.png' , '' , '' )
 if 52 - 52: IIIi % OOooOOo + iI11I1II1I1I * OoOo00o . Ii11Ii1I
 if 95 - 95: iI11I1II1I1I . OooO0OoOOOO - ii * oO0o / I11i
def oOo0OO0o0 ( url ) :
 o00OO00OoO = iiI111I1iIiI ( url )
 I1i11 = re . compile ( '<ul class="pagination" style="line-height: 3;">(.+?)</ul>' , re . DOTALL ) . findall ( o00OO00OoO )
 Ii1i = re . compile ( '<li><a href="/letters/(.+?)">(.+?)</a></li>' ) . findall ( str ( I1i11 ) )
 for url , iiI1IIIi in Ii1i :
  II1I ( '[COLORgreen]' + iiI1IIIi + '[/COLOR]' , 'http://watchseries.li/letters/' + url , 10049 , ooOooo000oOO + 'WATCHSERIES.png' , '' , '' )
  if 35 - 35: I1ii11iIi11i . I1ii11iIi11i % ii - Ii11Ii1I
def iIII11Iiii1 ( url ) :
 o00OO00OoO = iiI111I1iIiI ( url )
 Ii1i = re . compile ( '<a href="(.+?)" class="sr-header">(.+?)</a>' ) . findall ( o00OO00OoO )
 for url , iiI1IIIi in Ii1i :
  II1I ( '[COLORgreen]' + iiI1IIIi + '[/COLOR]' , 'http://watchseries.li/' + url , 10049 , ooOooo000oOO + 'WATCHSERIES.png' , '' , '' )
  if 95 - 95: oOo0O0Ooo
def o0OoO0OOoO0Oo0 ( url ) :
 o00OO00OoO = iiI111I1iIiI ( url )
 Ii1i = re . compile ( '<li class="col-md-6 col-xs-12 list-movies-li"><a href="(.+?)" title=".+?">(.+?)<span class="epnum">.+?</span></a></li>' , re . DOTALL ) . findall ( o00OO00OoO )
 I1 = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="(.+?)">Next</a></li></ul>' , re . DOTALL ) . findall ( o00OO00OoO )
 for url , iiI1IIIi in Ii1i :
  II1I ( '[COLORgreen]' + ( iiI1IIIi ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' ) + '[/COLOR]' , 'http://www.watchseries.li' + url , 10044 , ooOooo000oOO + 'WATCHSERIES.png' , '' , '' )
 for url in I1 :
  II1I ( '[COLORgreen]' + 'NEXT' + '[/COLOR]' , 'http://www.watchseries.li' + url , 10049 , ooOooo000oOO + 'Next.png' , '' , '' )
  if 91 - 91: IIiIiII11i
  if 53 - 53: oO0o % I11i / IIIii1II1II % OooO0OoOOOO % oO0o % ii
def i11i1i ( ) :
 iii1 = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 I1ii1Ii1 = 'http://www.watchseries.li/search/' + iii1 . replace ( ' ' , '%20' )
 o00OO00OoO = iiI111I1iIiI ( I1ii1Ii1 )
 Ii1i = re . compile ( '<img src="(.+?)".+?<a href="(.+?)" title=".+?"><b>(.+?)</b>' , re . DOTALL ) . findall ( o00OO00OoO )
 for IiI1iiiIii , OooOoOo , iiI1IIIi in Ii1i :
  if 'watch online' in iiI1IIIi :
   pass
  else :
   print OooOoOo
   II1I ( '[COLORgreen]' + iiI1IIIi + '[/COLOR]' , 'http://www.watchseries.li' + OooOoOo , 10044 , IiI1iiiIii , '' , '' )
   if 73 - 73: o0o00Oo0O . OoOo00o + Ii + iI11I1II1I1I - iI1iI1I1i1I / OOooOOo
   xbmcplugin . setContent ( O0O , 'movies' )
   if 99 - 99: Ii1I * OoOo00o * Ii1I - IIiIiII11i + Ii11Ii1I
def OOooO0Oo00 ( url ) :
 o00OO00OoO = iiI111I1iIiI ( url )
 Ii1i = re . compile ( '<img src="(.+?)".+?<div class="block-left-home-inside-text">.+?<a href="(.+?)" title=".+?"><b>(.+?)</b> <br>.+?<span class=".+?">(.+?)</span></a><br>(.+?)<br>' , re . DOTALL ) . findall ( o00OO00OoO )
 for IiI1iiiIii , url , iiI1IIIi , oOO0OOOo000o , iIII in Ii1i :
  iIIIIIIIiIII = ( iiI1IIIi ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' ) + ' - ' + ( oOO0OOOo000o ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' )
  II1I ( '[COLORgreen]' + iIIIIIIIiIII + '[/COLOR]' , 'http://www.watchseries.li' + url , 10045 , IiI1iiiIii , '' , iIII )
  if 94 - 94: o0oOO0O00o0O * iI11I1II1I1I . iI1iI1I1i1I
def IiiI11I1IIiI ( url ) :
 o00OO00OoO = iiI111I1iIiI ( url )
 Ii1i = re . compile ( '<li class="col-md-6 col-xs-12 list-movies-li"><a href="(.+?)" title=".+?">(.+?)<span class="epnum">.+?</span></a></li>' , re . DOTALL ) . findall ( o00OO00OoO )
 I1 = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="(.+?)">Next</a></li></ul>' , re . DOTALL ) . findall ( o00OO00OoO )
 for url , iiI1IIIi in Ii1i :
  iIIIIIIIiIII = ( iiI1IIIi ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' )
  II1I ( '[COLORgreen]' + iIIIIIIIiIII + '[/COLOR]' , 'http://www.watchseries.li' + url , 10045 , ooOooo000oOO + 'WATCHSERIES.png' , '' , '' )
 for url in I1 :
  II1I ( '[COLORgreen]' + 'NEXT' + '[/COLOR]' , 'http://www.watchseries.li' + url , 10046 , ooOooo000oOO + 'Next.png' , '' , '' )
  if 5 - 5: I1ii11iIi11i
def o0oOo00 ( url ) :
 o00OO00OoO = iiI111I1iIiI ( url )
 Ii1i = re . compile ( '<div class="mask">.+?<a href="(.+?)" title="(.+?)">.+?<img src="(.+?)"' , re . DOTALL ) . findall ( o00OO00OoO )
 I1 = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="(.+?)">Next</a></li></ul>' , re . DOTALL ) . findall ( o00OO00OoO )
 for url , iiI1IIIi , IiI1iiiIii in Ii1i :
  II1I ( '[COLORgreen]' + ( iiI1IIIi ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' ) + '[/COLOR]' , 'http://www.watchseries.li' + url , 10044 , IiI1iiiIii , '' , '' )
 for url in I1 :
  II1I ( '[COLORgreen]' + 'NEXT' + '[/COLOR]' , 'http://www.watchseries.li' + url , 10041 , ooOooo000oOO + 'Next.png' , '' , '' )
  if 22 - 22: iI11I1II1I1I + OooO0OoOOOO + Ii1I + IIIi - Ii11Ii1I
def I1IIII1i1 ( url ) :
 o00OO00OoO = iiI111I1iIiI ( url )
 I1i11 = re . compile ( '<div class="col-md-6 col-xs-12".+?<a href=".+?" itemprop="url"><span itemprop="name">(.+?)</span>(.+?)</ul>' , re . DOTALL ) . findall ( o00OO00OoO )
 for iII11ii1ii , i1iii1ii in I1i11 :
  Ii1i = re . compile ( '<li itemprop="episode".+?<meta itemprop="url" content="(.+?)">.+?<span class="" itemprop="name">\n(.+?)\n' , re . DOTALL ) . findall ( str ( i1iii1ii ) )
  for url , iiI1IIIi in Ii1i :
   iIIIIIIIiIII = ( iII11ii1ii ) . replace ( '  ' , '' ) + ' ' + ( iiI1IIIi ) . replace ( '&nbsp;' , ' ' ) . replace ( '&#039;' , '\'' ) . replace ( '  ' , '' )
   II1I ( '[COLORgreen]' + iIIIIIIIiIII + '[/COLOR]' , 'http://www.watchseries.li' + url , 10045 , ooOooo000oOO + 'WATCHSERIES.png' , '' , '' )
 I1 = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="(.+?)">Next</a></li></ul>' , re . DOTALL ) . findall ( o00OO00OoO )
 for url in I1 :
  II1I ( '[COLORgreen]' + 'NEXT' + '[/COLOR]' , 'http://www.watchseries.li' + url , 10044 , ooOooo000oOO + 'Next.png' , '' , '' )
  if 67 - 67: I1ii11iIi11i / O0OoO - OooO0OoOOOO
  if 74 - 74: iI1iI1I1i1I * Ii11Ii1I - Ii1I % iI11I1II1I1I
class oOoOoO0o0 ( ) :
 if 18 - 18: Ii11Ii1I
 List = [ ]
 source_list = [ ]
 def __init__ ( self , name ) :
  if 25 - 25: oO0o * OoOo00o % Ii + Ii * oO0o
  iIIIIIIIiIII = name
  self . Get_Sources ( OooOoOo , iIIIIIIIiIII )
  if 42 - 42: IIiIiII11i / o0o00Oo0O . iI11I1II1I1I / o0o00Oo0O / oO0o / ii
  if 62 - 62: o0o00Oo0O . I1ii11iIi11i
 def Get_Sources ( self , URL , season_name ) :
  Oo0oO0ooo = xbmcgui . DialogProgress ( )
  o00OO00OoO = iiI111I1iIiI ( URL )
  Ii1i = re . compile ( '<td>.+?<a href="/link/(.+?)".+?height="16px">(.+?)\n' , re . DOTALL ) . findall ( o00OO00OoO )
  for OooOoOo , iiI1IIIi in Ii1i :
   URL = 'http://www.watchseries.li/link/' + OooOoOo
   self . Get_site_link ( URL , season_name )
   if 33 - 33: I1ii11iIi11i / iI11I1II1I1I % ooOoO0O00
 def Get_site_link ( self , url , season_name ) :
  o00OO00OoO = iiI111I1iIiI ( url )
  Ii1i = re . compile ( '<iframe style=.+?" src="(.+?)"' ) . findall ( o00OO00OoO )
  I1 = re . compile ( '<IFRAME SRC="(.+?)"' ) . findall ( o00OO00OoO )
  iIII1I1i1i = re . compile ( '<IFRAME style=".+?" SRC="(.+?)"' ) . findall ( o00OO00OoO )
  for url in Ii1i :
   self . main ( url , season_name )
  for url in I1 :
   self . main ( url , season_name )
  for url in iIII1I1i1i :
   self . main ( url , season_name )
   if 76 - 76: Ii11Ii1I + iI11I1II1I1I + OOooOOo . oO0o
 def main ( self , url , season_name ) :
  Oo0oO0ooo . create ( "[COLORwhite]Origin[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
  if 'daclips.in' in url :
   i1i1 = 'DACLIPS'
   if i1i1 in oOoOoO0o0 . source_list :
    pass
   else :
    self . daclips ( url , season_name , i1i1 )
    Oo0oO0ooo . update ( 0 , "" , "Getting Daclips Links" )
  else :
   if 'filehoot.com' in url :
    i1i1 = 'FILEHOOT'
    if i1i1 in oOoOoO0o0 . source_list :
     pass
    else :
     Oo0oO0ooo . update ( 0 , "" , "Getting Filehoot Links" )
     self . filehoot ( url , season_name , i1i1 )
   else :
    if 'thevideo.me' in url :
     i1i1 = 'THEVIDEO'
     if i1i1 in oOoOoO0o0 . source_list :
      pass
     else :
      self . thevideo ( url , season_name , i1i1 )
      Oo0oO0ooo . update ( 0 , "" , "Getting Thevideo Links" )
    else :
     if 'allmyvideos.net' in url :
      i1i1 = 'ALLMYVIDEOS'
      if i1i1 in oOoOoO0o0 . source_list :
       pass
      else :
       self . allmyvid ( url , season_name , i1i1 )
       Oo0oO0ooo . update ( 0 , "" , "Getting Allmyvideo Links" )
     else :
      if 'vidspot.net' in url :
       i1i1 = 'VIDSPOT'
       if i1i1 in oOoOoO0o0 . source_list :
        pass
       else :
        self . vidspot ( url , season_name , i1i1 )
        Oo0oO0ooo . update ( 0 , "" , "Getting Vidspot Links" )
      else :
       if 'vodlocker' in url :
        i1i1 = 'VODLOCKER'
        if i1i1 in oOoOoO0o0 . source_list :
         pass
        else :
         self . vodlocker ( url , season_name , i1i1 )
         Oo0oO0ooo . update ( 0 , "" , "Getting Vodlocker Links" )
         if 68 - 68: Ii11Ii1I - oOo0O0Ooo
         if 41 - 41: OoOo00o
 def allmyvid ( self , url , season_name , source_name ) :
  o00OO00OoO = iiI111I1iIiI ( url )
  Ii1i = re . compile ( '"file" : "(.+?)",\n.+?"default" : .+?,\n.+?"label" : "(.+?)"' , re . DOTALL ) . findall ( o00OO00OoO )
  for I11II1 , iiI1IIIi in Ii1i :
   self . Printer ( I11II1 , season_name , source_name )
   if 46 - 46: OOooOOo
 def vidspot ( self , url , season_name , source_name ) :
  o00OO00OoO = iiI111I1iIiI ( url )
  Ii1i = re . compile ( '"file" : "(.+?)",\n.+?"default" : .+?,\n.+?"label" : "(.+?)"' ) . findall ( o00OO00OoO )
  for I11II1 , iiI1IIIi in Ii1i :
   self . Printer ( I11II1 , season_name , source_name )
   if 83 - 83: Ii * IIIi
 def thevideo ( self , url , season_name , source_name ) :
  o00OO00OoO = iiI111I1iIiI ( url )
  Ii1i = re . compile ( "{ label: '.+?', file: '(.+?)' }" ) . findall ( o00OO00OoO )
  for I11II1 in Ii1i :
   self . Printer ( I11II1 , season_name , source_name )
   if 49 - 49: I1ii11iIi11i * OoOo00o + I11i - Ii
 def vodlocker ( self , url , season_name , source_name ) :
  o00OO00OoO = iiI111I1iIiI ( url )
  Ii1i = re . compile ( 'file: "(.+?)",.+?skin' , re . DOTALL ) . findall ( o00OO00OoO )
  for I11II1 in Ii1i :
   self . Printer ( I11II1 , season_name , source_name )
   if 74 - 74: I1ii11iIi11i / iI11I1II1I1I . IIiIiII11i - oO0o
 def daclips ( self , url , season_name , source_name ) :
  o00OO00OoO = iiI111I1iIiI ( url )
  Ii1i = re . compile ( '{ file: "(.+?)", type:"video" }' ) . findall ( o00OO00OoO )
  for I11II1 in Ii1i :
   self . Printer ( I11II1 , season_name , source_name )
   if 62 - 62: IIIii1II1II / IIiIiII11i + OOooOOo % O0OoO / OOooOOo + Ii1I
 def filehoot ( self , url , season_name , source_name ) :
  o00OO00OoO = iiI111I1iIiI ( url )
  Ii1i = re . compile ( 'file: "(.+?)",.+?skin' , re . DOTALL ) . findall ( o00OO00OoO )
  for I11II1 in Ii1i :
   self . Printer ( I11II1 , season_name , source_name )
   if 2 - 2: Ii - IIIi + oO0o % iI1iI1I1i1I * Ii11Ii1I
 def Printer ( self , Link , season_name , source_name ) :
  if 54 - 54: o0o00Oo0O - o0oOO0O00o0O . IIIii1II1II % o0oOO0O00o0O + o0oOO0O00o0O
  if Link in oOoOoO0o0 . List :
   pass
  elif source_name in oOoOoO0o0 . source_list :
   pass
  else :
   iii11 ( '[COLORgreen]' + source_name + '[/COLOR]' , Link , 10012 , ooOooo000oOO + 'WATCHSERIES.png' )
   Oo0oO0ooo . update ( 100 , "" , "Got Source" )
   oOoOoO0o0 . List . append ( Link )
   oOoOoO0o0 . source_list . append ( source_name )
   if 36 - 36: IIIii1II1II % Ii
   xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
   if 47 - 47: ooOoO0O00 + IIiIiII11i . I1ii11iIi11i * OoOo00o . iI1iI1I1i1I / ooOoO0O00
   if 50 - 50: IIIi / ooOoO0O00 % ii
   if 83 - 83: Ii1I * Ii1I + IIIii1II1II
   if 57 - 57: o0o00Oo0O - o0o00Oo0O . Ii1I / I11i / Ii11Ii1I
   if 20 - 20: IIIii1II1II * IIiIiII11i - OOooOOo - OoOo00o * IIIi
def I1i1II1 ( ) :
 II1I ( '[COLORgreen]Highlights[/COLOR]' , '' , 10008 , ooOooo000oOO + 'ORIGINFOOTBALL.png' , i1iiIII111ii , '' )
 II1I ( '[COLORgreen]Fixtures[/COLOR]' , '' , 10009 , ooOooo000oOO + 'ORIGINFOOTBALL.png' , i1iiIII111ii , '' )
 if 89 - 89: oO0o / oO0o
def iI ( ) :
 I1i11i = iiI111I1iIiI ( i1111 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20vcXVpY2tpbmRleC5odG1s' ) )
 Ii1i = re . compile ( '<a target="_self" href="(.+?)".+?src="(.+?)" alt="(.+?)"' , re . DOTALL ) . findall ( I1i11i )
 for OooOoOo , IiI1iiiIii , iiI1IIIi in Ii1i :
  II1I ( '[COLORgreen]' + ( iiI1IIIi ) . replace ( 'amp;' , '' ) + '[/COLOR]' , i1111 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20v' ) + OooOoOo , 10010 , i1111 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20v' ) + IiI1iiiIii , i1iiIII111ii , '' )
  if 3 - 3: oO0o * ooOoO0O00 . oOo0O0Ooo . o0o00Oo0O - OOooOOo
def OOoooOoO0 ( url ) :
 o00OO00OoO = iiI111I1iIiI ( url )
 I1i11 = re . compile ( 'AndClearL.+?><h2.+?head>(.*?)float' , re . DOTALL ) . findall ( o00OO00OoO )
 for I1i11 in I1i11 :
  O0OOoooo0 = re . compile ( '(.*?)</h2>' ) . findall ( str ( I1i11 ) )
  for iIiIi1IiIi1iI in O0OOoooo0 :
   iIiIi1IiIi1iI = iIiIi1IiIi1iI
  o00OO0 = re . compile ( 'comp_head>(.*?)</span>.*?<div class = fLeft width = ".*?"><img src="(.*?)">.*?</div>.*?ST:(.*?)</div>(.+?)<!-- around all of channel types ENDS 2-->' , re . DOTALL ) . findall ( str ( I1i11 ) )
  for oooOo , IiI1iiiIii , time , oOoO0Oo0 in o00OO0 :
   i1Iii11I1i = re . compile ( ",CAPTION, '(.+?)&nbsp" ) . findall ( oOoO0Oo0 )
   II1I ( '[COLORgreen]' + iIiIi1IiIi1iI + ' - ' + oooOo + ' - ' + time + '[/COLOR]' , '' , 10010 , i1111 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20=' ) + IiI1iiiIii , i1iiIII111ii , ( str ( i1Iii11I1i ) ) )
   if 7 - 7: O0OoO + Ii11Ii1I
 iiIiI ( 'tvshows' , 'Media Info 3' )
 if 32 - 32: iI11I1II1I1I % oOo0O0Ooo / Ii + IIIii1II1II - I11i . o0oOO0O00o0O
def oo00I1IiI1IIiI ( ) :
 II1I ( '[COLORgreen]Latest[/COLOR]' , 'http://www.fullmatchesandshows.com' , 10011 , 'http://www.fancyicons.com/free-icons/125/miscellaneous/png/256/football_256.png' , ooOooo000oOO + 'fanart.jpg' , '' )
 II1I ( '[COLORgreen]EURO 2016[/COLOR]' , 'http://www.fullmatchesandshows.com/euro-2016/' , 10011 , 'http://football.mywapblog.com/files/uefa-euro-2016-logo.png' , ooOooo000oOO + 'fanart.jpg' , '' )
 II1I ( '[COLORgreen]Shows[/COLOR]' , 'http://www.fullmatchesandshows.com/category/show/' , 10011 , 'http://www.fm-base.co.uk/forum/attachments/club-competition-logos/3885-soccer-am-logo-socceram.png' , ooOooo000oOO + 'fanart.jpg' , '' )
 II1I ( '[COLORgreen]Premier League[/COLOR]' , 'http://www.fullmatchesandshows.com/premier-league/' , 10011 , 'https://footballseasons.files.wordpress.com/2013/05/premier-league.png' , ooOooo000oOO + 'fanart.jpg' , '' )
 II1I ( '[COLORgreen]La Liga[/COLOR]' , 'http://www.fullmatchesandshows.com/la-liga/' , 10011 , 'http://1.bp.blogspot.com/-c6kQ40ryhyo/U19cUlz25sI/AAAAAAAABak/qtn5chSFZm0/s1600/la-liga-logo_display_image.png' , ooOooo000oOO + 'fanart.jpg' , '' )
 II1I ( '[COLORgreen]Bundesliga[/COLOR]' , 'http://www.fullmatchesandshows.com/bundesliga/' , 10011 , 'http://m.img.brothersoft.com/iphone/189/518670189_icon175x175.jpg' , ooOooo000oOO + 'fanart.jpg' , '' )
 II1I ( '[COLORgreen]Champions League[/COLOR]' , 'http://www.fullmatchesandshows.com/champions-league/' , 10011 , 'http://www.ecursuri.ro/images/teste/test-champions-league.jpg' , ooOooo000oOO + 'fanart.jpg' , '' )
 II1I ( '[COLORgreen]Serie A[/COLOR]' , 'http://www.fullmatchesandshows.com/category/serie-a/' , 10011 , 'http://files.jcriccione.it/200000223-2484526782/serie%20a.png' , ooOooo000oOO + 'fanart.jpg' , '' )
 II1I ( '[COLORgreen]Ligue 1[/COLOR]' , 'http://www.fullmatchesandshows.com/category/ligue-1/' , 10011 , 'http://a1.mzstatic.com/us/r30/Purple5/v4/37/c7/44/37c744ae-5824-42b7-6ce0-5f471f52baab/icon180x180.jpeg' , ooOooo000oOO + 'fanart.jpg' , '' )
 II1I ( '[COLORgreen]Copa America 2015[/COLOR]' , 'http://www.fullmatchesandshows.com/copa-america-2015/' , 10011 , 'https://pbs.twimg.com/profile_images/521966985907691520/Nq9OAPIo_400x400.png' , ooOooo000oOO + 'fanart.jpg' , '' )
 II1I ( '[COLORgreen]CONCACAF[/COLOR]' , 'http://www.fullmatchesandshows.com/category/concacaf/' , 10011 , 'http://a3.mzstatic.com/us/r30/Purple3/v4/40/26/14/4026147c-7022-4ca3-504e-e78950cc3f1c/icon175x175.png' , ooOooo000oOO + 'fanart.jpg' , '' )
 II1I ( '[COLORgreen]Women World Cup[/COLOR]' , 'http://www.fullmatchesandshows.com/category/women-world-cup/' , 10011 , 'https://upload.wikimedia.org/wikipedia/en/thumb/7/76/2015_FIFA_Women\'s_World_Cup_logo.svg/967px-2015_FIFA_Women\'s_World_Cup_logo.svg.png' , ooOooo000oOO + 'fanart.jpg' , '' )
 if 79 - 79: ooOoO0O00
def iIi1ooo0Oooooo ( url ) :
 o00OO00OoO = iiI111I1iIiI ( url )
 Ii1i = re . compile ( 'class="entry-thumb" src="(.+?)" alt="".+?<h3 class="entry-title td-module-title"><a href="(.+?)" rel="bookmark" title=".+?">(.+?)</a></h3>' , re . DOTALL ) . findall ( o00OO00OoO )
 I1 = re . compile ( '<a href="([^"]*)" rel="bookmark" title="([^"]*)"><img width="218" height="150" class="entry-thumb" src="([^"]*)"' , re . DOTALL ) . findall ( o00OO00OoO )
 for IiI1iiiIii , url , iiI1IIIi in Ii1i :
  Ooi1IIii11i1I1 = iiI1IIIi . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) . replace ( '&#8217;' , '' )
  iii11 ( '[COLORgreen]' + Ooi1IIii11i1I1 + '[/COLOR]' , url , 10013 , IiI1iiiIii )
 for url , iiI1IIIi , IiI1iiiIii in I1 :
  Ooi1IIii11i1I1 = iiI1IIIi . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) . replace ( '&#8217;' , '' )
  iii11 ( '[COLORgreen]' + Ooi1IIii11i1I1 + '[/COLOR]' , url , 10013 , IiI1iiiIii )
  if 12 - 12: ooOoO0O00 / IIIii1II1II % O0OoO * OooO0OoOOOO * o0o00Oo0O * iI11I1II1I1I
def OOOOoO ( url ) :
 o00OO00OoO = iiI111I1iIiI ( url )
 Ii1i = re . compile ( '<script data-config="(.+?)" data-height' ) . findall ( o00OO00OoO )
 for oOOOo00O00O in Ii1i :
  Iii11111iiI = ( oOOOo00O00O ) . replace ( '/v2' , '' ) . replace ( 'zeus.json' , 'video-sd.mp4?hosting_id=21772' ) . replace ( 'config.playwire.com' , 'cdn.video.playwire.com' )
  O00o0O ( 'http:' + Iii11111iiI )
  if 67 - 67: I11i
  if 76 - 76: OOooOOo - oOo0O0Ooo + IIIii1II1II + iI1iI1I1i1I
def i1Iiii ( url ) :
 I1i11i = IiIi ( url )
 Ii1i = re . compile ( '<a href="([^"]*)" title="([^"]*)"><img itemprop="image" content="([^"]*)"' , re . DOTALL ) . findall ( I1i11i )
 I1 = re . compile ( "<a rel='next' href=([^=]*)=" , re . DOTALL ) . findall ( I1i11i )
 for url , iiI1IIIi , IiI1iiiIii in Ii1i :
  iii11 ( iiI1IIIi , url , 8046 , IiI1iiiIii )
 for url in I1 :
  IIiI1I1 ( 'NEXT PAGE' , ( url ) . replace ( ' class' , '' ) , 8045 , ooOooo000oOO + 'Next.png' )
def o0O0O ( url ) :
 I1i11i = IiIi ( url )
 Ii1i = re . compile ( "__filename='([^']*)',.+?__fullimage='([^']*)',.+?__title='([^']*)'," , re . DOTALL ) . findall ( I1i11i )
 for url , IiI1iiiIii , iiI1IIIi in Ii1i :
  O00o0O ( 'http://bitcast-b.bitgravity.com/ndtvod/23372/ndtv/' + url )
  if 56 - 56: o0o00Oo0O
def iIIIII1iI ( url ) :
 I1i11i = IiIi ( url )
 Ii1i = re . compile ( "src='http://www.youtube.com/embed/(.+?)?version=3&#038;rel=1&#038;fs=1&#038;autohide=2&#038;showsearch=0&#038;showinfo=1&#038;iv_load_policy=1&#038;wmode=transparent' frameborder='0' allowfullscreen='true'></iframe>" ) . findall ( I1i11i )
 for url in Ii1i :
  yt . PlayVideo ( url )
  if 18 - 18: I1ii11iIi11i - o0o00Oo0O
def O00oooooo ( ) :
 I1i11i = IiIi ( i1111 ( 'aHR0cDovL3RvcGRvY3VtZW50YXJ5ZmlsbXMuY29tLw==' ) )
 Ii1i = re . compile ( '<a href="(.+?)" >(.+?)</a></li>' ) . findall ( I1i11i )
 for OooOoOo , iiI1IIIi in Ii1i :
  IIiI1I1 ( iiI1IIIi , OooOoOo , 8041 , ooOooo000oOO + 'documentary.png' )
def Ii111111ii ( url ) :
 I1i11i = IiIi ( url )
 Ii1i = re . compile ( '<a href="([^"]*)" title="([^"]*)"><img width="95" height="125" src="([^"]*)"' , re . DOTALL ) . findall ( I1i11i )
 I1 = re . compile ( 'title="([^"]*)" href="([^"]*)"><img src="([^"]*)"' , re . DOTALL ) . findall ( I1i11i )
 next = re . compile ( 'class="inactive">.+?</a><a href="(.+?)">Next</a></div>' , re . DOTALL ) . findall ( I1i11i )
 for url , iiI1IIIi , IiI1iiiIii in Ii1i :
  IIiI1I1 ( ( iiI1IIIi ) . replace ( '&#039;s' , '' ) , url , 8042 , IiI1iiiIii )
 for iiI1IIIi , url , IiI1iiiIii in I1 :
  IIiI1I1 ( ( iiI1IIIi ) . replace ( '&#039;s' , '' ) , url , 8042 , IiI1iiiIii )
 for url in next :
  IIiI1I1 ( 'NEXT PAGE' , url , 8041 , ooOooo000oOO + 'Next.png' )
  if 83 - 83: oO0o + IIIii1II1II - I11i + iI11I1II1I1I % I1ii11iIi11i
  if 23 - 23: I11i + Ii11Ii1I % OOooOOo % oOo0O0Ooo % ii
def OOOOoo00OO0O0Ooo0 ( url ) :
 I1i11i = IiIi ( url )
 Ii1i = re . compile ( '<meta itemprop="name" content="(.+?)".+?<meta itemprop="thumbnailUrl" content="(.+?)".+?<meta itemprop="embedUrl" content="(.+?)".+?<meta itemprop="description" content="(.+?)" />' , re . DOTALL ) . findall ( I1i11i )
 I1 = re . compile ( '<div class="video new-video"><iframe width="766" height="431" src="(.+?)&iv_load_policy=3&showinfo=0&autohide=1"' , re . DOTALL ) . findall ( I1i11i )
 for iiI1IIIi , IiI1iiiIii , url , I1iiIi111I in Ii1i :
  iii11 ( ( iiI1IIIi ) . replace ( '&#039;s' , '' ) , url . replace ( 'https://www.youtube.com/embed/videoseries?list=' , '' ) . replace ( 'https://www.youtube.com/embed/' , '' ) , 8043 , IiI1iiiIii )
 for url in I1 :
  ooOOO00oOOooO ( ( url ) . replace ( '//' , 'http://' ) )
  if 46 - 46: iI11I1II1I1I . Ii - OOooOOo % o0o00Oo0O / IIiIiII11i * ooOoO0O00
def ooOOO00oOOooO ( url ) :
 I1i11i = IiIi ( url )
 Ii1i = re . compile ( '<link rel="canonical" href="(.+?)">  <link rel="stylesheet"' ) . findall ( I1i11i )
 for url in Ii1i :
  iii11 ( 'PLAY' , ( url ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , ooOooo000oOO + 'documentary.png' )
  if 66 - 66: o0o00Oo0O
def oOooOOo00ooO ( ) :
 o00OO00OoO = IiIi ( 'http://www.stream2watch.co/live-tv' )
 Ii1i = re . compile ( '<a href="(.+?)">.+?<img src="(.+?)" alt=".+?"/>.+?<span class="country_name">(.+?)<br />(.+?)</span>' , re . DOTALL ) . findall ( o00OO00OoO )
 for OooOoOo , IiI1iiiIii , iiI1IIIi , o0OO0oooo in Ii1i :
  IIiI1I1 ( ( iiI1IIIi + '[COLORgreen]' + o0OO0oooo + '[/COLOR]' ) , OooOoOo , 8086 , IiI1iiiIii )
  if 40 - 40: IIIi - OOooOOo * iI1iI1I1i1I - OooO0OoOOOO / OOooOOo
def OO0oo ( url ) :
 o00OO00OoO = IiIi ( url )
 Ii1i = re . compile ( '<a class="front_channel_href" href="(.+?)" title=".+?">.+?<img class="front_channel_thumb" src="(.+?)" alt=".+?"/>.+?<span class="front_channel_name">(.+?)</span>' , re . DOTALL ) . findall ( o00OO00OoO )
 for url , IiI1iiiIii , iiI1IIIi in Ii1i :
  IIiI1I1 ( '[COLORgreen]' + iiI1IIIi + '[/COLOR]' , url , 8087 , IiI1iiiIii )
  if 90 - 90: IIIi + Ii1I / IIIi + OooO0OoOOOO / IIiIiII11i
def o00oO0O0oo0o ( url ) :
 o00OO00OoO = iiI111I1iIiI ( url )
 Ii1i = re . compile ( 'a id="code_.+?data-f-href="(.+?)" data-code-embed="">(.+?)</a>' , re . DOTALL ) . findall ( o00OO00OoO )
 for url , iiI1IIIi in Ii1i :
  iIi11I11 ( url , iiI1IIIi )
  if 40 - 40: iI11I1II1I1I
def iIi11I11 ( url , name ) :
 o00OO00OoO = iiI111I1iIiI ( url )
 Ii1i = re . compile ( "playStream\('.+?', '(.+?)'\);" , re . DOTALL ) . findall ( o00OO00OoO )
 for url in Ii1i :
  print url
  iii11 ( '[COLORgreen]' + name + '[/COLOR]' , url , 222 , '' )
  if 92 - 92: OOooOOo % o0o00Oo0O
def oo00ooooOOo00 ( ) :
 I1i11i = IiIi ( i1111 ( 'aHR0cDovL3d3dy5zb2xpZS5vcmcvYWxpYnJhcnkvaW5kZXguaHRtbA==' ) )
 Ii1i = re . compile ( '<td align="center" valign="top">.+?<a href="(.+?)">.+?<img src="(.+?)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( I1i11i )
 for OooOoOo , IiI1iiiIii , iiI1IIIi in Ii1i :
  IIiI1I1 ( ( '[COLORgreen]' + iiI1IIIi + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + OooOoOo , 3002 , 'http://www.solie.org/alibrary/' + IiI1iiiIii )
def ii1i ( url ) :
 I1i11i = IiIi ( url )
 Ii1i = re . compile ( '<td align="center" valign="top">.+?<a href="(.+?)">.+?<img src="(.+?)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( I1i11i )
 for url , IiI1iiiIii , iiI1IIIi in Ii1i :
  IIiI1I1 ( ( '[COLORgreen]' + iiI1IIIi + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3003 , 'http://www.solie.org/alibrary/' + IiI1iiiIii )
def OO00Oooo000 ( url ) :
 I1i11i = IiIi ( url )
 Ii1i = re . compile ( '<br><a href="([^"]*)">(.+?)</a>' ) . findall ( I1i11i )
 iI1ii111iiIii = re . compile ( 'href="([^"]*)">Season(.+?)</a>' ) . findall ( I1i11i )
 next = re . compile ( '<a href="([^"]*)">Episodes</a>' ) . findall ( I1i11i )
 I1 = re . compile ( '<td align="center" valign="top">.+?<a href="(.+?)">.+?<img src="(.+?)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( I1i11i )
 for url , iiI1IIIi in Ii1i :
  iii11 ( ( '[COLORgreen]' + iiI1IIIi + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3004 , ooOooo000oOO + 'classicmovies.png' )
 for url , iiI1IIIi in iI1ii111iiIii :
  IIiI1I1 ( '[COLORgreen]Season- ' + iiI1IIIi + '[/COLOR]' , 'http://www.solie.org/alibrary/' + url , 3003 , ooOooo000oOO + 'classicmovies.png' )
 for url in next :
  IIiI1I1 ( '[COLORgreen]NEXT[/COLOR]' , 'http://www.solie.org/alibrary/' + url , 3003 , ooOooo000oOO + 'Next.png' )
 for url , IiI1iiiIii , iiI1IIIi in I1 :
  IIiI1I1 ( ( '[COLORgreen]' + iiI1IIIi + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3003 , 'http://www.solie.org/alibrary/' + IiI1iiiIii )
def oO0oiIiI ( url ) :
 I1i11i = IiIi ( url )
 Ii1i = re . compile ( '<iframe.+?src="([^"]*)"' ) . findall ( I1i11i )
 for url in Ii1i :
  iIIiiiI1iI1 ( url )
def iIIiiiI1iI1 ( url ) :
 I1i11i = IiIi ( url )
 Ii1i = re . compile ( '<meta property="og:video" content="([^"]*)"/>' ) . findall ( I1i11i )
 for url in Ii1i :
  O00o0O ( url )
  if 86 - 86: Ii1I * O0OoO
def O0oO0o0OOOOOO ( ) :
 I1i11i = IiIi ( i1111 ( 'aHR0cDovL3JldHJvdmlzaW9uLnR2L2FsbC8=' ) )
 Ii1i = re . compile ( '<a href="([^"]*)"><h2><font color=".+?"><h2>(.+?)</font></h2></a>' ) . findall ( I1i11i )
 for OooOoOo , iiI1IIIi in Ii1i :
  iii11 ( ( '[COLORgreen]' + iiI1IIIi + '[/COLOR]' ) . replace ( '&#8211;' , ':' ) , OooOoOo , 8065 , ooOooo000oOO + 'classicmovies.png' )
def IiI1i11IiIiii ( url ) :
 I1i11i = IiIi ( url )
 Ii1i = re . compile ( "v.src = '([^']*)';" ) . findall ( I1i11i )
 for url in Ii1i :
  o0OOo0o0O0O ( url )
  if 4 - 4: IIIi - oOo0O0Ooo % OoOo00o / I11i % OoOo00o * IIiIiII11i
def IiI1I ( ) :
 I1i11i = IiIi ( i1111 ( 'aHR0cDovL3JldHJvdmlzaW9uLnR2L2NsYXNzaWMtdHYv' ) )
 Ii1i = re . compile ( '<a href="([^"]*)"><h2><font color=".+?"><h2>(.+?)</font></h2></a>' ) . findall ( I1i11i )
 for OooOoOo , iiI1IIIi in Ii1i :
  iii11 ( ( '[COLORgreen]' + iiI1IIIi + '[/COLOR]' ) . replace ( '&#8211;' , ':' ) , OooOoOo , 8065 , ooOooo000oOO + 'classictv.png' )
def IIIiIi1iiI ( url ) :
 I1i11i = IiIi ( url )
 Ii1i = re . compile ( 'href="([^"]*)">' , re . DOTALL ) . findall ( I1i11i )
 I1 = re . compile ( "videoId: '([^']*)'" , re . DOTALL ) . findall ( I1i11i )
 for url in Ii1i :
  if 'mp4' in url :
   O00o0O ( url )
 for url in I1 :
  yt . PlayVideo ( url )
  if 15 - 15: Ii1I . o0oOO0O00o0O
def o0Iiii ( ) :
 o00OO00OoO = iiI111I1iIiI ( i1111 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vbTN1c3RyZWFtcw==' ) )
 Ii1i = re . compile ( '<li><a href="(.+?)"> (.+?).m3u</a></li>' ) . findall ( o00OO00OoO )
 for OooOoOo , iiI1IIIi in Ii1i :
  IIiI1I1 ( ( '[COLORgreen]' + iiI1IIIi + '[/COLOR]' ) . replace ( '-' , ' ' ) . replace ( '_' , ' ' ) , ( i1111 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vbTN1c3RyZWFtcy8=' ) ) + OooOoOo , 8071 , ooOooo000oOO + 'streams.png' )
def I1i1I ( url ) :
 o00OO00OoO = IiIi ( url )
 Ii1i = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( o00OO00OoO )
 for iiI1IIIi , url in Ii1i :
  if '(Free Access)' in iiI1IIIi :
   url = ( url ) . strip ( )
  else :
   url = ( ( i1111 ( 'aHR0cDovL3BpZXN1c3R2Lm5ldDo4MDAwL2xpdmUv' ) ) + oO0o0o0ooO0oO + '/' + oo0o0O00 + url ) . strip ( )
  iii11 ( ( '[COLORgreen]' + iiI1IIIi + '[/COLOR]' ) . replace ( '_' , ' ' ) . replace ( '(Free Access)' , '[COLORwhite] - Free Access[/COLOR]' ) , url , 222 , ooOooo000oOO + 'streams.png' )
def i1111iI1 ( url ) :
 o00OO00OoO = IiIi ( url )
 Ii1i = re . compile ( 'EXTINF:(.+?),(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( o00OO00OoO )
 for IiI1iiiIii , iiI1IIIi , url in Ii1i :
  url = ( ( i1111 ( 'aHR0cDovL3BpZXN1c3R2Lm5ldDo4MDAwL2xpdmUv' ) ) + oO0o0o0ooO0oO + '/' + oo0o0O00 + url ) . strip ( )
  iii11 ( ( '[COLORgreen]' + iiI1IIIi + '[/COLOR]' ) . replace ( '_' , ' ' ) , url , 10012 , IiI1iiiIii )
  if 76 - 76: ii - IIiIiII11i % OOooOOo + OoOo00o + iI11I1II1I1I . OOooOOo
def iIo00OOOOOo0OOo ( ) :
 IIOO0ooOo0OoOo0 ( 'Best Videos' , 'http://www.xvideos.com/best' , 10105 , ooOooo000oOO + 'JIZBOX.png' , '' , '' )
 IIOO0ooOo0OoOo0 ( 'Genres' , 'http://www.xvideos.com' , 10106 , ooOooo000oOO + 'JIZBOX.png' , '' , '' )
 IIOO0ooOo0OoOo0 ( 'Recently Uploaded' , 'http://xvideos.com' , 10105 , ooOooo000oOO + 'JIZBOX.png' , '' , '' )
 IIOO0ooOo0OoOo0 ( 'Tags' , 'http://www.xvideos.com/tags' , 10103 , ooOooo000oOO + 'JIZBOX.png' , '' , '' )
 IIOO0ooOo0OoOo0 ( 'Search' , '' , 10107 , ooOooo000oOO + 'JIZBOX.png' , '' , '' , )
 if 44 - 44: iI1iI1I1i1I * I11i
def II11ii1I11 ( url ) :
 o00OO00OoO = iiI111I1iIiI ( url )
 o0oO00o = re . compile ( '<li><a class=".+?".+?href="(.+?)">Next</a></li>' ) . findall ( o00OO00OoO )
 for url in o0oO00o :
  IIOO0ooOo0OoOo0 ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10103 , ooOooo000oOO + 'JIZBOX.png' , '' , '' )
 Ii1i = re . compile ( '<li><a href="(.+?)"><b>(.+?)</b><span class="navbadge default"(.+?)</span>' ) . findall ( o00OO00OoO )
 for url , iiI1IIIi , II11IiIi11 in Ii1i :
  IIOO0ooOo0OoOo0 ( ( iiI1IIIi + ' - No of Videos : ' + ( II11IiIi11 ) ) . replace ( '"></span>' , ' ' ) . replace ( '<span class="flag-small flag-' , '' ) . replace ( '>' , '' ) , 'http://www.xvideos.com' + url , 10105 , ooOooo000oOO + 'JIZBOX.png' , '' , '' )
  if 78 - 78: I1ii11iIi11i * IIIi - ii - oO0o
def o0OOo ( url ) :
 o00OO00OoO = iiI111I1iIiI ( url )
 o0oO00o = re . compile ( 'href="([^"]*)">Next</a></li>' ) . findall ( o00OO00OoO )
 for url in o0oO00o :
  IIOO0ooOo0OoOo0 ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10104 , ooOooo000oOO + 'Next.png' , '' , '' )
 Ii1i = re . compile ( ':"([^"]*)".+?;</script></a></div></div><p class="profile-name"><a href="([^"]*)">(.+?)</a></p><p class="profile-counts">\n(.+?)\n' , re . DOTALL ) . findall ( o00OO00OoO )
 for IiI1iiiIii , url , iiI1IIIi , IiI1Ii11Ii in Ii1i :
  IIOO0ooOo0OoOo0 ( iiI1IIIi + '--' + IiI1Ii11Ii , 'http://www.xvideos.com' + url + '#_tabVideos,videos-best' , 10105 , ( IiI1iiiIii ) . replace ( 'http:\/\/' , 'http://' ) , '' , '' )
  if 99 - 99: o0o00Oo0O . I11i % iI1iI1I1i1I - I1ii11iIi11i / iI1iI1I1i1I
  if 20 - 20: OOooOOo * o0oOO0O00o0O
def i1i1I1iiIiIII ( url ) :
 o00OO00OoO = iiI111I1iIiI ( url )
 Ii1i = re . compile ( '<div class="thumb"><script>.+?<img src="(.+?)".+?<a href="(.+?)" title=".+?">(.+?)</a></p>.+?uration">(.+?)</span>.+?Porn quality:(.+?)</span>' , re . DOTALL ) . findall ( o00OO00OoO )
 for IiI1iiiIii , url , iiI1IIIi , III1I1Iii1iiI , o0IiIiI111IIII1 in Ii1i :
  IIOO0ooOo0OoOo0 ( iiI1IIIi + ' - Porn Quality : ' + o0IiIiI111IIII1 + ' - ' + III1I1Iii1iiI , 'http://www.xvideos.com' + url , 10108 , IiI1iiiIii , IiI1iiiIii , o0IiIiI111IIII1 + ' - ' + III1I1Iii1iiI )
 OOOoOooO000oO = re . compile ( '<li><a href="([^"]*)" class="no-page">Next</a></li></ul></div>' ) . findall ( o00OO00OoO )
 for url in OOOoOooO000oO :
  IIOO0ooOo0OoOo0 ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10105 , ooOooo000oOO + 'Next.png' , '' , '' )
  if 87 - 87: o0oOO0O00o0O % I1ii11iIi11i
def OOo000o ( url ) :
 o00OO00OoO = iiI111I1iIiI ( url )
 I1i11 = re . compile ( '<div class="main-categories">(.+?)</div>' , re . DOTALL ) . findall ( o00OO00OoO )
 o0oO00o = re . compile ( '<li><a class=".+?".+?href="(.+?)">Next</a></li>' ) . findall ( o00OO00OoO )
 for url in o0oO00o :
  IIOO0ooOo0OoOo0 ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10106 , ooOooo000oOO + 'Next.png' , '' , '' )
 Ii1i = re . compile ( '<li><a href="(.+?)" class="btn btn-default">(.+?)</a>' ) . findall ( str ( I1i11 ) )
 for url , iiI1IIIi in Ii1i :
  IIOO0ooOo0OoOo0 ( iiI1IIIi , 'http://www.xvideos.com' + url , 10105 , ooOooo000oOO + 'JIZBOX.png' , '' , '' )
  if 37 - 37: o0oOO0O00o0O
  if 33 - 33: oO0o - o0o00Oo0O - oO0o
def O000oooOO0Oo0 ( ) :
 iii1 = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 I1iIiIii = ( iii1 ) . replace ( ' ' , '+' ) . replace ( '&' , '&' )
 o0o = I1iIiIii . lower ( )
 OO0 = 'http://www.xvideos.com/?k=' + o0o
 print OO0 + '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'
 o00OO00OoO = iiI111I1iIiI ( OO0 )
 Ii1i = re . compile ( '<div class="thumb-inside"><script>.+?<img src="(.+?)".+?<a href="(.+?)" title=".+?">(.+?)</a></p>.+?uration">(.+?)</span>.+?Porn quality:(.+?)</span>' , re . DOTALL ) . findall ( o00OO00OoO )
 for IiI1iiiIii , OooOoOo , iiI1IIIi , III1I1Iii1iiI , o0IiIiI111IIII1 in Ii1i :
  IIOO0ooOo0OoOo0 ( iiI1IIIi + ' - Porn Quality : ' + o0IiIiI111IIII1 + ' - ' + III1I1Iii1iiI , 'http://www.xvideos.com' + OooOoOo , 10108 , IiI1iiiIii , IiI1iiiIii , o0IiIiI111IIII1 + ' - ' + III1I1Iii1iiI )
 OOOoOooO000oO = re . compile ( '<li><a href="([^"]*)" class="no-page">Next</a></li></ul></div>' ) . findall ( o00OO00OoO )
 for OooOoOo in OOOoOooO000oO :
  IIOO0ooOo0OoOo0 ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + OooOoOo , 10105 , ooOooo000oOO + 'Next.png' , '' , '' )
  if 17 - 17: Ii11Ii1I * IIiIiII11i / OooO0OoOOOO + iI11I1II1I1I . iI1iI1I1i1I - o0o00Oo0O
def O0OOO00OOO00o ( url ) :
 o00OO00OoO = iiI111I1iIiI ( url )
 Ii1i = re . compile ( "setVideoUrlLow.+?'([^']*)'" ) . findall ( o00OO00OoO )
 I1 = re . compile ( "setVideoUrlHigh.+?'([^']*)'" ) . findall ( o00OO00OoO )
 iIII1I1i1i = re . compile ( "setVideoHLS.+?'([^']*)'" ) . findall ( o00OO00OoO )
 for url in Ii1i :
  if 'http' in url :
   iii11 ( '[COLORgreen]LOW[/COLOR]' , url , 222 , ooOooo000oOO + 'JIZBOX.png' )
 for url in I1 :
  if 'http' in url :
   iii11 ( '[COLORgreen]HIGH[/COLOR]' , url , 222 , ooOooo000oOO + 'JIZBOX.png' )
 for url in iIII1I1i1i :
  if 'http' in url :
   iii11 ( '[COLORgreen]HLS[/COLOR]' , url , 222 , ooOooo000oOO + 'JIZBOX.png' )
   if 12 - 12: o0o00Oo0O
def OoO00OooO0 ( url ) :
 OoOOoO0oOo = xbmc . Player ( o00OOo ( ) )
 import urlresolver
 try : OoOOoO0oOo . play ( url )
 except : pass
 if 40 - 40: iI11I1II1I1I + o0oOO0O00o0O * OOooOOo + OoOo00o
 if 15 - 15: iI1iI1I1i1I % oOo0O0Ooo - iI11I1II1I1I * O0OoO
def oO0O0o0o000 ( ) :
 o00OO00OoO = iiI111I1iIiI ( i1111 ( 'aHR0cDovL3d3dy5nb2Zpc2hpbmcuY28udWsvQW5nbGluZy1UaW1lcy9TZWN0aW9uL1ZpZGVvcy8=' ) )
 Ii1i = re . compile ( 'class="item.+?"><a href="(.+?)">(.+?)</a></li>' ) . findall ( o00OO00OoO )
 for OooOoOo , iiI1IIIi in Ii1i :
  IIiI1I1 ( '[COLORgreen]' + iiI1IIIi + '[/COLOR]' , ( 'http://www.gofishing.co.uk' + OooOoOo ) . replace ( 'http://www.gofishing.co.ukhttp://www.gofishing.co.uk' , 'http://www.gofishing.co.uk' ) , 8091 , ooOooo000oOO + 'gofish.png' )
def III1 ( url ) :
 o00OO00OoO = IiIi ( url )
 Ii1i = re . compile ( '<h2><a id=.+?href="([^"]*)">(.+?)</a></h2>' , re . DOTALL ) . findall ( o00OO00OoO )
 I1 = re . compile ( '<h3><a href="([^"]*)" id=.+?>(.+?)</a> </h3>.+?<img src="([^"]*)"' , re . DOTALL ) . findall ( o00OO00OoO )
 next = re . compile ( 'href="([^"]*)">next</a>&gt;</li>' , re . DOTALL ) . findall ( o00OO00OoO )
 for url , iiI1IIIi in Ii1i :
  iii11 ( '[COLORgreen]' + iiI1IIIi + '[/COLOR]' , 'http://www.gofishing.co.uk/' + url , 8092 , ooOooo000oOO + 'gofish.png' )
 for url , iiI1IIIi , IiI1iiiIii in I1 :
  iii11 ( '[COLORgreen]' + iiI1IIIi + '[/COLOR]' , 'http://www.gofishing.co.uk/' + url , 8092 , 'http://www.gofishing.co.uk/' + IiI1iiiIii )
 for url in next :
  IIiI1I1 ( '[COLORgreen]NEXT[/COLOR]' , url . replace ( ' ' , '+' ) , 8091 , ooOooo000oOO + 'Next.png' )
def OOO000OOo0o0O ( url ) :
 o00OO00OoO = IiIi ( url )
 Ii1i = re . compile ( 'src="https://www.youtube.com/embed/(.+?)"' ) . findall ( o00OO00OoO )
 for url in Ii1i :
  yt . PlayVideo ( url )
  if 14 - 14: o0oOO0O00o0O - iI1iI1I1i1I * ii + IIIii1II1II . IIiIiII11i
  if 15 - 15: iI1iI1I1i1I % Ii
  if 73 - 73: O0OoO % O0OoO . o0oOO0O00o0O + IIIi
Ii1IOOooO00OO = '{PQ},' ; O00OoOOoo = '{SC},' ; IiIIi11i = '{XG},' ; IIii11i = '{JP},' ; oO0OOO00 = '{HW},' ; I1iIiI1iiiiI1 = '{RT},'
def IIII1ii1 ( ) :
 Oo0oO0ooo = xbmcgui . DialogProgress ( )
 OOO0O0OOo = ( i1111 ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 iii1 = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 o0o = iii1 . lower ( )
 OooOoOo = ( i1111 ( 'aHR0cDovL2RsNC5tb3ZpZWZhcnNpLmNvbS9maWxtLzIwMTUtNy8=' ) )
 OooO0OO = ( i1111 ( 'aHR0cDovLzUuMTM1LjIwNy45Ni9OZXclMjBSZWxlYXNlcyUyMChDcmFwJTIwQ29waWVzKS8=' ) )
 o0OO0o0oOOO0O = ( i1111 ( 'aHR0cDovLzIxNy4yMTkuMTQzLjEwOC8xMzI3Lw==' ) )
 Iii1 = ( i1111 ( 'aHR0cDovLzUuMTM1LjIwNy45Ni9OZXclMjBSZWxlYXNlcy8=' ) )
 OOoO = ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvbW92L2FsbC5waHA=' ) )
 i1IiiI = ( i1111 ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 O0OOO0 = ( i1111 ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL3NlYXJjaC8/cT0=' ) ) + iii1
 o0OIi = ( i1111 ( 'aHR0cDovL3JlZGVtcHRpb25idWlsZC4xNm1iLmNvbS9SZWRlbXB0aW9uL21vdmllcy9hbGxtb3ZpZS5waHA=' ) )
 IIi1iiI = ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9UaGVfUmVhcGVyL2FsbG1vdmllcy5waHA=' ) )
 o0ooOO00OO0o0O = ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC9tb3ZmdWxsLnBocA==' ) )
 III1IiiIiiI1i = ( i1111 ( 'aHR0cDovLzUuMTM1LjIwNy45Ni9TY3JhcGVzL1NILnBocA==' ) )
 if 73 - 73: ooOoO0O00 % iI1iI1I1i1I - O0OoO / I11i % oO0o / IIIi
 Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Checking Sources" , '' , 'Please Wait' )
 o00OO00OoO = O000OO0 ( OooOoOo )
 Oo0oO0ooo . update ( 0 , "" , "Checking Source 1/9 Links" )
 OOOO0OOoO0O0 = O000OO0 ( OooO0OO )
 Oo0oO0ooo . update ( 14 , "" , "Checking Source 2/9 Links" )
 O0Oo000ooO00 = O000OO0 ( o0OO0o0oOOO0O )
 Oo0oO0ooo . update ( 28 , "" , "Checking Source 3/9 Links" )
 oO0 = O000OO0 ( Iii1 )
 Oo0oO0ooo . update ( 40 , "" , "Checking Source 4/9 Links" )
 O00Oo = O000OO0 ( OOoO )
 Oo0oO0ooo . update ( 52 , "" , "Checking Source 5/9 Links" )
 i1ii1II11I = O000OO0 ( O0OOO0 )
 Oo0oO0ooo . update ( 64 , "" , "Checking Source 6/9 Links" )
 OO000OO = O000OO0 ( o0OIi )
 Oo0oO0ooo . update ( 76 , "" , "Checking Source 7/9 Links" )
 O00o0000OO = O000OO0 ( IIi1iiI )
 Oo0oO0ooo . update ( 88 , "" , "Checking Source 8/9 Links" )
 O0Ooo0O0OO = O000OO0 ( o0ooOO00OO0o0O )
 Oo0oO0ooo . update ( 100 , "" , "Checking Source 9/9 Links" )
 iiI1iiii1Iii = O000OO0 ( III1IiiIiiI1i )
 if 94 - 94: Ii % OoOo00o + I1ii11iIi11i + OoOo00o
 if 33 - 33: OooO0OoOOOO . I1ii11iIi11i / iI11I1II1I1I
 if o00OO00OoO != 'Failed' :
  Ii1i = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( o00OO00OoO )
  for iiiIiIiI , iiI1IIIi in Ii1i :
   if iii1 in iiI1IIIi . lower ( ) :
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    iii11 ( ( '[COLORgreen]' + iiI1IIIi + '- source 1[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( OooOoOo + iiiIiIiI ) , 222 , '' )
    Oo0oO0ooo . update ( 0 , "" , "Getting Source 1 Links" )
 if OOOO0OOoO0O0 != 'Failed' :
  I1 = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( OOOO0OOoO0O0 )
  for iiiIiIiI , iiI1IIIi in I1 :
   if iii1 in iiI1IIIi . lower ( ) :
    iii11 ( ( '[COLORgreen]' + iiI1IIIi + '- Silent Hunter Cams[/COLOR]' ) . replace ( 'mkv' , '' ) . replace ( '.' , ' ' ) , ( OooO0OO + iiiIiIiI ) , 222 , '' )
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 9 , "" , "Getting Silent Hunter Cams Links" )
 if O0Oo000ooO00 != 'Failed' :
  iIII1I1i1i = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( O0Oo000ooO00 )
  for iiiIiIiI , iiI1IIIi in iIII1I1i1i :
   if iii1 in iiI1IIIi . lower ( ) :
    IIiI1I1 ( ( '[COLORgreen]' + iiI1IIIi + '- source 3[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( o0OO0o0oOOO0O + iiiIiIiI ) , 1006 , '' )
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 18 , "" , "Getting Source 3 Links" )
 if oO0 != 'Failed' :
  o0O = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( oO0 )
  for iiiIiIiI , iiI1IIIi in o0O :
   if iii1 in iiI1IIIi . lower ( ) :
    iii11 ( ( '[COLORgreen]' + iiI1IIIi + '- Silent Hunter[/COLOR]' ) . replace ( 'mkv' , '' ) . replace ( '.' , ' ' ) , OooOoOo , 222 , '' )
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 27 , "" , "Getting Silent Hunter Links" )
 if O00Oo != 'Failed' :
  i1iIoOO0oo = [ ]
  i1iiIIiII1 = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( O00Oo )
  for OooOoOo , OOOOO0O00 , iIII , ii1i1iiI , iiI1IIIi in i1iiIIiII1 :
   if iii1 in iiI1IIIi . lower ( ) :
    if iiI1IIIi in i1iIoOO0oo :
     pass
    else :
     II1I ( ( '[COLORgreen]' + iiI1IIIi + '- source Scooby[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( 'Ganool' , '' ) . replace ( 'ShAaNiG' , '' ) . replace ( 'YIFY' , '' ) . replace ( '[[ Max-Movie.In ]]' , '' ) . replace ( '.mkv' , '' ) . replace ( '.mp4' , '' ) . replace ( '.' , ' ' ) , OooOoOo , 1016 , OOOOO0O00 , ii1i1iiI , iIII )
     i1iIoOO0oo . append ( iiI1IIIi )
     Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     Oo0oO0ooo . update ( 36 , "" , "Getting Scooby Links" )
     iiIiI ( 'tvshows' , 'Media Info 3' )
 if i1ii1II11I != 'Failed' :
  o0O00OooooO = re . compile ( 'href="(.+?)".+?src="(.+?)" alt="Image of (.+?)"' , re . DOTALL ) . findall ( i1ii1II11I )
  for OooOoOo , IiI1iiiIii , iiI1IIIi in o0O00OooooO :
   if iii1 in iiI1IIIi . lower ( ) :
    IIiI1I1 ( ( '[COLORgreen]' + iiI1IIIi + '- source Snag[/COLOR]' ) . replace ( '&#x27;' , '' ) , 'http://www.snagfilms.com' + OooOoOo , 7067 , IiI1iiiIii )
    Oo0oO0ooo . update ( 45 , "" , "Getting Snag Links" )
    if 77 - 77: oOo0O0Ooo % O0OoO
    iiIiI ( 'tvshows' , 'Media Info 3' )
 if OO000OO != 'Failed' :
  oO0oo = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( OO000OO )
  for OooOoOo , OOOOO0O00 , iIII , ii1i1iiI , iiI1IIIi in oO0oo :
   if iii1 in iiI1IIIi . lower ( ) :
    ooOOoooooo ( ( '[COLORgreen]' + iiI1IIIi + '- source Redemption[/COLOR]' ) , OooOoOo , 222 , OOOOO0O00 , ii1i1iiI , iIII )
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 53 , "" , "Getting Redemption Links" )
    if 52 - 52: OooO0OoOOOO % O0OoO
    iiIiI ( 'tvshows' , 'Media Info 3' )
 if O00o0000OO != 'Failed' :
  I111 = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( O00o0000OO )
  for OooOoOo , OOOOO0O00 , iIII , ii1i1iiI , iiI1IIIi in I111 :
   if iii1 in iiI1IIIi . lower ( ) :
    ooOOoooooo ( ( '[COLORgreen]' + iiI1IIIi + '- source Reaper[/COLOR]' ) , OooOoOo , 222 , OOOOO0O00 , ii1i1iiI , iIII )
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 61 , "" , "Getting Reaper Links" )
    if 51 - 51: Ii1I * OoOo00o
    iiIiI ( 'tvshows' , 'Media Info 3' )
 if O0Ooo0O0OO != 'Failed' :
  i1oooOoOoOO = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( O0Ooo0O0OO )
  for OooOoOo , OOOOO0O00 , iIII , ii1i1iiI , iiI1IIIi in i1oooOoOoOO :
   if iii1 in iiI1IIIi . lower ( ) :
    ooOOoooooo ( ( '[COLORgreen]' + iiI1IIIi + '- source Herovision[/COLOR]' ) , OooOoOo , 222 , OOOOO0O00 , ii1i1iiI , iIII )
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 70 , "" , "Getting Herovision Links" )
    if 51 - 51: IIiIiII11i / I1ii11iIi11i / oOo0O0Ooo + Ii
    iiIiI ( 'tvshows' , 'Media Info 3' )
    if 5 - 5: iI1iI1I1i1I
 if iiI1iiii1Iii != 'Failed' :
  iii1IiiiI1i1 = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( iiI1iiii1Iii )
  for OooOoOo , OOOOO0O00 , iiI1IIIi in iii1IiiiI1i1 :
   if iii1 in iiI1IIIi . lower ( ) :
    IIiI1I1 ( ( '[COLORgreen]' + iiI1IIIi + '- source Silent Hunter[/COLOR]' ) , OooOoOo , 222 , OOOOO0O00 )
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 78 , "" , "Getting Silent Hunter Links" )
    if 37 - 37: I1ii11iIi11i - ooOoO0O00 - OooO0OoOOOO + iI1iI1I1i1I . iI11I1II1I1I
    iiIiI ( 'tvshows' , 'Media Info 3' )
 O0Oo0 = [ '480p' , '720p' , '1080p' , 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' , '720paction' , '720padventure' , '720panimation' , '720pcomedy' , '720pcrime' , '720pdocumentary' , '720pdrama' , '720pfamily' , '720pfantasy' , '720phorror' , '720pmystery' , '720promance' , '720psci-Fi' , '720psport' , '720pthriller' , '720pwestern' , '1080paction' , '1080padventure' , '1080panimation' , '1080pcomedy' , '1080pcrime' , '1080pdocumentary' , '1080pdrama' , '1080pfamily' , '1080pfantasy' , '1080phorror' , '1080pmystery' , '1080promance' , '1080psci-Fi' , '1080psport' , '1080pthriller' , '1080pwestern' , 'films' ]
 if 59 - 59: ii - IIIi % I11i . iI1iI1I1i1I + ooOoO0O00 * iI1iI1I1i1I
 for iI1iIiiiI1I1 in O0Oo0 :
  OOOOOo = IIIII + iI1iIiiiI1I1 + ooOoOoo0O
  ii11111I = O000OO0 ( OOOOOo )
  if ii11111I != 'Failed' :
   OOOOoOOO000o0O0O = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( ii11111I )
   for OooOoOo , OOOOO0O00 , iIII , ii1i1iiI , iiI1IIIi in OOOOoOOO000o0O0O :
    if iii1 in iiI1IIIi . lower ( ) :
     ooOOoooooo ( '[COLORgreen]' + iiI1IIIi + ' - Source Pandoras[/COLOR]' , OooOoOo , 222 , OOOOO0O00 , ii1i1iiI , iIII )
     Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     Oo0oO0ooo . update ( 89 , "" , "Getting Pandoras Links" )
     if 28 - 28: ooOoO0O00 . IIIii1II1II
     iiIiI ( 'tvshows' , 'Media Info 3' )
     if 88 - 88: iI1iI1I1i1I + oOo0O0Ooo - iI1iI1I1i1I / ii - Ii
 O0Oo0 = [ '0-9/' , 'A/' , 'B/' , 'C/' , 'D/' , 'E/' , 'F/' , 'G/' , 'H/' , 'I/' , 'J/' , 'K/' , 'L/' , 'M/' , 'N/' , 'O/' , 'P/' , 'R/' , 'S/' , 'T/' , 'U/' , 'V/' , 'W/' , 'X/' , 'Y/' , 'Z/' ]
 if 24 - 24: iI11I1II1I1I
 if 89 - 89: Ii11Ii1I / ooOoO0O00 - I11i % oOo0O0Ooo . I1ii11iIi11i - o0o00Oo0O
 for iI1iIiiiI1I1 in O0Oo0 :
  OOOOOo = OOO0O0OOo + iI1iIiiiI1I1
  OOOoo00o0o = O000OO0 ( OOOOOo )
  if O00Oo != 'Failed' :
   O00o0OO0OO0oo = re . compile ( '<li><a href="(.+?)"> (.+?)</a></li>' ) . findall ( OOOoo00o0o )
   for iiiIiIiI , iiI1IIIi in O00o0OO0OO0oo :
    if iii1 in iiI1IIIi . lower ( ) :
     iii11 ( ( '[COLORgreen]' + iiI1IIIi + 'source 5[/COLOR]' ) . replace ( 'Ganool' , '' ) . replace ( 'ShAaNiG' , '' ) . replace ( 'YIFY' , '' ) . replace ( '[[ Max-Movie.In ]]' , '' ) . replace ( '.mkv' , '' ) . replace ( '.mp4' , '' ) . replace ( '.' , ' ' ) , ( OOO0O0OOo + iI1iIiiiI1I1 + iiiIiIiI ) , 222 , '' )
     Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     Oo0oO0ooo . update ( 100 , "" , "Getting Source 5 Links" )
     if 59 - 59: ii % iI1iI1I1i1I / IIIi + ii . ii
     iiIiI ( 'tvshows' , 'Media Info 3' )
     if 87 - 87: iI1iI1I1i1I + OoOo00o
     if 3 - 3: ii
def IiIiI11IIi11Iii ( ) :
 if 9 - 9: OoOo00o
 iii1 = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 o0o = iii1 . lower ( )
 if 2 - 2: iI11I1II1I1I * oOo0O0Ooo % ooOoO0O00 % Ii1I + ii + oOo0O0Ooo
 OooOoOo = ( i1111 ( 'aHR0cDovL2RsLmZhcnNpbW92aWUubmV0L1NlcmlhbC8=' ) )
 OooO0OO = ( i1111 ( 'aHR0cDovL3JlZGVtcHRpb25idWlsZC4xNm1iLmNvbS9SZWRlbXB0aW9uL3R2c2hvd3MvdHZtYWluLnBocA==' ) )
 o0OO0o0oOOO0O = ( i1111 ( 'aHR0cDovL3R2LmRsLXBhcnMuaW4v' ) )
 Iii1 = ( i1111 ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9BbWVyaWNhbiUyMFNlcmlhbC8=' ) )
 OOoO = ( i1111 ( 'aHR0cDovL2RpemlsYWIuY29tL2Fyc2l2P2xpbWl0PSZ0dXI9Jm9yZGVyYnk9JnVsa2U9Jm9yZGVyPSZ5aWw9JmRpemlfYWRpPQ==' ) ) + ( o0o ) . replace ( ' ' , '+' )
 i1IiiI = ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvc2hvd3MvdHZhbGwucGhw' ) )
 O0OOO0 = ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9UaGVfUmVhcGVyL2FsbHR2LnBocA==' ) )
 o0OIi = ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC90dmZ1bGwucGhw' ) )
 if 16 - 16: IIIii1II1II
 Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Checking Sources" , '' , 'Please Wait' )
 if 63 - 63: o0oOO0O00o0O
 Oo0oO0ooo . update ( 0 , "" , "Checking Source 1/9 Links" )
 o00OO00OoO = O000OO0 ( OooOoOo )
 Oo0oO0ooo . update ( 14 , "" , "Checking Source 2/9 Links" )
 OOOO0OOoO0O0 = O000OO0 ( OooO0OO )
 Oo0oO0ooo . update ( 28 , "" , "Checking Source 3/9 Links" )
 O0Oo000ooO00 = O000OO0 ( o0OO0o0oOOO0O )
 Oo0oO0ooo . update ( 40 , "" , "Checking Source 4/9 Links" )
 oO0 = O000OO0 ( Iii1 )
 Oo0oO0ooo . update ( 52 , "" , "Checking Source 5/9 Links" )
 O00Oo = cloudflare . source ( OOoO )
 Oo0oO0ooo . update ( 64 , "" , "Checking Source 6/9 Links" )
 OOOoo00o0o = O000OO0 ( i1IiiI )
 Oo0oO0ooo . update ( 76 , "" , "Checking Source 7/9 Links" )
 i1ii1II11I = O000OO0 ( O0OOO0 )
 Oo0oO0ooo . update ( 88 , "" , "Checking Source 8/9 Links" )
 OO000OO = O000OO0 ( o0OIi )
 Oo0oO0ooo . update ( 100 , "" , "Checking Source 9/9 Links" )
 if 11 - 11: o0oOO0O00o0O - iI11I1II1I1I
 if OO000OO != 'Failed' :
  oO0oo = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( OO000OO )
  for OooOoOo , OOOOO0O00 , iIII , ii1i1iiI , iiI1IIIi in oO0oo :
   if o0o in iiI1IIIi . lower ( ) :
    II1I ( ( '[COLORgreen]' + iiI1IIIi + '- source HeroVision[/COLOR]' ) , OooOoOo , 1016 , OOOOO0O00 , ii1i1iiI , iIII )
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 10 , "" , "Getting Herovision Links" )
    if 92 - 92: oO0o
    iiIiI ( 'tvshows' , 'Media Info 3' )
    if 15 - 15: OooO0OoOOOO / OooO0OoOOOO + iI11I1II1I1I % ii
 if i1ii1II11I != 'Failed' :
  o0O00OooooO = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( i1ii1II11I )
  for OooOoOo , OOOOO0O00 , iIII , ii1i1iiI , iiI1IIIi in o0O00OooooO :
   if o0o in iiI1IIIi . lower ( ) :
    II1I ( ( '[COLORgreen]' + iiI1IIIi + '- source Reaper[/COLOR]' ) , OooOoOo , 1016 , OOOOO0O00 , ii1i1iiI , iIII )
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 20 , "" , "Getting Reaper Links" )
    if 12 - 12: O0OoO
    iiIiI ( 'tvshows' , 'Media Info 3' )
    if 36 - 36: IIIi . OooO0OoOOOO * ii - I11i
    if 60 - 60: IIIii1II1II . o0oOO0O00o0O / iI11I1II1I1I + IIIii1II1II * IIIi
    if 82 - 82: Ii . iI11I1II1I1I * oOo0O0Ooo - iI1iI1I1i1I + Ii11Ii1I
    if 48 - 48: Ii1I
    if 96 - 96: O0OoO . ii
    if 39 - 39: IIIii1II1II + oO0o
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 30 , "" , "Getting CoolSeries Links" )
    if 80 - 80: IIIii1II1II % oO0o / OOooOOo
    iiIiI ( 'tvshows' , 'Media Info 3' )
 if o00OO00OoO != 'Failed' :
  Ii1i = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( o00OO00OoO )
  for iiI1IIIi in Ii1i :
   if o0o in iiI1IIIi . lower ( ) :
    IIiI1I1 ( '[COLORgreen]' + ( iiI1IIIi ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) + ' source 1 [/COLOR]' , ( OooOoOo + iiI1IIIi ) . replace ( ' ' , '%20' ) , 1006 , '' )
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 40 , "" , "Getting Source 1 Links" )
    if 54 - 54: I1ii11iIi11i % oO0o - IIIii1II1II - iI1iI1I1i1I
    iiIiI ( 'tvshows' , 'Media Info 3' )
 if OOOO0OOoO0O0 != 'Failed' :
  I1 = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( OOOO0OOoO0O0 )
  for OooOoOo , OOOOO0O00 , iIII , ii1i1iiI , iiI1IIIi in I1 :
   if o0o in iiI1IIIi . lower ( ) :
    IIiI1I1 ( ( iiI1IIIi + '[COLORblue] - source Redemption[/COLOR]' ) . replace ( '..&gt;' , '' ) , OooOoOo , 1016 , '' )
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 50 , "" , "Getting Redemption Links" )
    if 71 - 71: O0OoO . Ii
    iiIiI ( 'tvshows' , 'Media Info 3' )
 if O0Oo000ooO00 != 'Failed' :
  iIII1I1i1i = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( O0Oo000ooO00 )
  for iiI1IIIi in iIII1I1i1i :
   if o0o in iiI1IIIi . lower ( ) :
    IIiI1I1 ( ( iiI1IIIi + ' source 3' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( o0OO0o0oOOO0O + iiI1IIIi ) . replace ( ' ' , '%20' ) , 1006 , '' )
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 60 , "" , "Getting Source 3 Links" )
    if 56 - 56: o0o00Oo0O * o0oOO0O00o0O + o0oOO0O00o0O * iI11I1II1I1I / O0OoO * IIIi
    iiIiI ( 'tvshows' , 'Media Info 3' )
 if oO0 != 'Failed' :
  o0O = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( oO0 )
  for iiI1IIIi in o0O :
   if o0o in iiI1IIIi . lower ( ) :
    IIiI1I1 ( ( iiI1IIIi + ' source 4' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( Iii1 + iiI1IIIi ) . replace ( ' ' , '%20' ) , 1006 , '' )
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 70 , "" , "Getting Source 4 Links" )
    if 25 - 25: iI11I1II1I1I . iI1iI1I1i1I * Ii + I1ii11iIi11i * iI1iI1I1i1I
    iiIiI ( 'tvshows' , 'Media Info 3' )
 if O00Oo != 'Failed' :
  i1iiIIiII1 = re . compile ( '<a href="(.+?)" class="film-image">\n<img src="(.+?)" alt=""/>\n</a>\n<div class="tss-detail">\n<a class="title" style="" href=".+?">\n<span class="position">.+?</span>\n(.+?)</a>' ) . findall ( O00Oo )
  for OooOoOo , IiI1iiiIii , iiI1IIIi in i1iiIIiII1 :
   if o0o in iiI1IIIi . lower ( ) :
    IIiI1I1 ( '[COLORgreen]' + iiI1IIIi + ' - Source - Dizi[/COLOR]' , OooOoOo , 8062 , IiI1iiiIii )
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 80 , "" , "Getting Dizi Links" )
    if 67 - 67: o0oOO0O00o0O
    iiIiI ( 'tvshows' , 'Media Info 3' )
 if OOOoo00o0o != 'Failed' :
  O00o0OO0OO0oo = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( OOOoo00o0o )
  for OooOoOo , OOOOO0O00 , iIII , ii1i1iiI , iiI1IIIi in O00o0OO0OO0oo :
   if o0o in iiI1IIIi . lower ( ) :
    II1I ( ( '[COLORgreen]' + iiI1IIIi + '- Source Scooby[/COLOR]' ) , OooOoOo , 1016 , OOOOO0O00 , ii1i1iiI , iIII )
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 90 , "" , "Getting Scooby Links" )
    if 88 - 88: I1ii11iIi11i
    iiIiI ( 'tvshows' , 'Media Info 3' )
    if 8 - 8: Ii1I
 o000 = [ 'a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' , 'p' , 'q' , 'r' , 's' , 't' , 'u' , 'v' , 'w' , 'x' , 'y' , 'z' ]
 if 30 - 30: Ii11Ii1I + IIiIiII11i % ii
 for iI1iIiiiI1I1 in o000 :
  OOOOOo = IIIII + iI1iIiiiI1I1 + ooOoOoo0O
  O0Ooo0O0OO = iiI111I1iIiI ( OOOOOo )
  if O0Ooo0O0OO != 'Failed' :
   i1oooOoOoOO = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( O0Ooo0O0OO )
   for iiI1IIIi , iIII , OooOoOo , IiI1iiiIii , Iii , IiI1I1I in i1oooOoOoOO :
    if o0o in iiI1IIIi . lower ( ) :
     II1I ( '[COLORgreen]' + iiI1IIIi + ' - Source Pandoras[/COLOR]' , OooOoOo , IiI1I1I , IiI1iiiIii , Iii , iIII )
     Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     Oo0oO0ooo . update ( 100 , "" , "Getting Pandoras Links" )
     if 89 - 89: Ii11Ii1I
     iiIiI ( 'tvshows' , 'Media Info 3' )
     if 51 - 51: o0oOO0O00o0O
     if 68 - 68: o0oOO0O00o0O - I11i * oO0o % O0OoO . O0OoO - iI11I1II1I1I
 xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
def Ii1IOoO0o0O ( ) :
 if 20 - 20: o0o00Oo0O
 iii1 = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 o0o = iii1 . lower ( )
 OooOoOo = ( i1111 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz' ) )
 o00OO00OoO = iiI111I1iIiI ( OooOoOo )
 Ii1i = re . compile ( '"id":".+?","name":"(.+?)","img":"(.+?)","stream_url3":".+?","cat_id":"(.+?)","stream_url2":".+?","stream_url":".+?"}' , re . DOTALL ) . findall ( o00OO00OoO )
 for iiI1IIIi , IiI1iiiIii , Ooo0oOOoo0O in Ii1i :
  OoooOo00 = i1111 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv' ) + ( IiI1iiiIii ) . replace ( '\\' , '' )
  if iii1 in iiI1IIIi . lower ( ) :
   IIiI1I1 ( iiI1IIIi , '' , 7022 , OoooOo00 )
   if 98 - 98: oO0o . iI11I1II1I1I % ii % I1ii11iIi11i - Ii1I
 xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
oO0I1I1i1I1I1I1 = '{ZH},' ; iI11IiIiiII1 = '{IX},' ; I11iii1i = '{LM},'
if 29 - 29: ii . IIiIiII11i % OOooOOo
def IiiIi1I11 ( url ) :
 i1I1Ii11II1i = cloudflare . source ( url )
 Ii1i = re . compile ( '<a class="season" href="(.+?)">\n(.+?)\n</a>\n</span>\n<span>\n<a class="episode" href=".+?">\n(.+?)\n</a>\n</span>\n<span>\n<a class="episode-name" href=".+?">\n(.+?)</a>' ) . findall ( i1I1Ii11II1i )
 for url , iII11ii1ii , ii1 , iiI1IIIi in Ii1i :
  IIiI1I1 ( ( iII11ii1ii ) . replace ( 'Sezon' , ' Season ' ) + ( ii1 ) . replace ( 'Bölüm' , ' Episode ' ) + iiI1IIIi , url , 8063 , '' )
  if 83 - 83: OooO0OoOOOO
  if 30 - 30: I1ii11iIi11i
  if 8 - 8: o0o00Oo0O + OoOo00o + IIIi
  if 47 - 47: iI1iI1I1i1I
def Oooo0O0Oooo ( url ) :
 i1I1Ii11II1i = cloudflare . source ( url )
 Ii1i = re . compile ( 'file: "(.+?)",.+?label: "(.+?)",' , re . DOTALL ) . findall ( i1I1Ii11II1i )
 for url , iiI1IIIi in Ii1i :
  iii11 ( iiI1IIIi , url , 222 , '' )
  if 47 - 47: Ii / I1ii11iIi11i - I1ii11iIi11i * oO0o
  if 48 - 48: OooO0OoOOOO
  if 96 - 96: OoOo00o / o0o00Oo0O . IIiIiII11i + OooO0OoOOOO % I11i
  if 67 - 67: o0o00Oo0O % IIIi
def III ( ) :
 if 48 - 48: IIIii1II1II . IIIii1II1II + Ii + Ii1I % o0o00Oo0O
 i1I1Ii11II1i = cloudflare . source ( i1111 ( 'aHR0cDovL2RpemlsYWIuY29t' ) )
 Ii1i = re . compile ( '<li id=".+?">.+?<a href="(.+?)">.+?<img width="40" height="40" src="(.+?)" alt=""/>.+?<span class="title">\n(.+?)</span>.+?<span class="alt-title">\n(.+?)</span>.+?</a>.+?</li>' , re . DOTALL ) . findall ( i1I1Ii11II1i )
 for OooOoOo , IiI1iiiIii , iiI1IIIi , ii1 in Ii1i :
  IIiI1I1 ( iiI1IIIi + '  -  ' + ( ii1 ) . replace ( 'sezon' , 'Season' ) . replace ( 'bölüm' , 'Episode' ) , OooOoOo , 8063 , IiI1iiiIii )
  if 67 - 67: O0OoO / iI1iI1I1i1I * oOo0O0Ooo % ii
def ii1IIiI1iI1i ( ) :
 I1i11i = IiIi ( i1111 ( 'aHR0cDovL3d3dy50dmd1aWRlLmNvLnVrLw==' ) )
 Ii1i = re . compile ( '<a href="(.+?)"  qt-title=".+?" qt-text=".+?<br> .+?" title="(.+?)".+?class=".+? src="(.+?)" alt=".+?" /></a>' , re . DOTALL ) . findall ( I1i11i )
 for OooOoOo , iiI1IIIi , IiI1iiiIii in Ii1i :
  iii11 ( '[COLORgreen]' + iiI1IIIi + '[/COLOR]' , OooOoOo , 8002 , IiI1iiiIii )
def IIiII11 ( url ) :
 I1i11i = IiIi ( url )
 Ii1i = re . compile ( '<table border="0".+?url((.+?));background-repeat: no-repeat;">.+?<tr>.+?<span class="season">(.+?)</span><br>.+?<a href="(.+?)"+?>(.+?)</span><br>.+?<span class="programmetext">(.+?)</span></a><br>' , re . DOTALL ) . findall ( I1i11i )
 for IiI1iiiIii , time , url , iiI1IIIi , I1iiIi111I in Ii1i :
  II1I ( '%s %s' % ( '[COLORgreen]' + iiI1IIIi + '[/COLOR]' , time ) , url , 1015 , IiI1iiiIii , I1iiIi111I )
  if 58 - 58: o0oOO0O00o0O
def I11IIIII ( ) :
 if 53 - 53: ii . ii + I11i - o0oOO0O00o0O + IIIii1II1II
 IIiI1I1 ( 'Coronation Street' , '' , 8001 , '' )
 IIiI1I1 ( 'Eastenders' , '' , 8002 , '' )
 IIiI1I1 ( 'Emmerdale' , '' , 8003 , '' )
 IIiI1I1 ( 'Hollyoaks' , '' , 8004 , '' )
 IIiI1I1 ( 'Im a Celebrity' , '' , 8005 , '' )
 if 44 - 44: IIIi - OooO0OoOOOO
 if 100 - 100: OoOo00o . oO0o - Ii11Ii1I + o0o00Oo0O * oO0o
 if 59 - 59: IIiIiII11i
 if 43 - 43: I1ii11iIi11i + ii
def i1I111iIii1i1 ( ) :
 o00OO00OoO = iiI111I1iIiI ( 'http://uksoapshare.blogspot.co.uk/' )
 Ii1i = re . compile ( '<a href="(.+?)".+?target=_blank>(.+?)</a>' ) . findall ( o00OO00OoO )
 for OooOoOo , iiI1IIIi in Ii1i :
  if 'Holly' in iiI1IIIi :
   IiI1iiiIii = 'http://2.bp.blogspot.com/-9c7Sieh1RKs/UjD6TGAEEnI/AAAAAAAAAC8/84uwHfxcuYg/s1600/Hollyoaks.png'
   if 'huge' in OooOoOo :
    iii11 ( ( iiI1IIIi ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , OooOoOo . replace ( '\\/' , '/' ) , 8006 , IiI1iiiIii )
   else :
    pass
    if 80 - 80: IIIi / Ii + ii
 xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE_IGNORE_THE ) ;
 if 38 - 38: Ii1I % O0OoO + ooOoO0O00 * ii * OoOo00o
def OoO0o0OO ( ) :
 o00OO00OoO = iiI111I1iIiI ( 'http://uksoapshare.blogspot.co.uk/' )
 Ii1i = re . compile ( '<a href="(.+?)".+?target=_blank>(.+?)</a>' ) . findall ( o00OO00OoO )
 for OooOoOo , iiI1IIIi in Ii1i :
  if 'East' in iiI1IIIi :
   IiI1iiiIii = 'http://3.bp.blogspot.com/-KWHcNbNJU8Y/Vi1ousRl7fI/AAAAAAAAAT8/ksNE12LH0nE/s1600/eastenders.jpg'
   if 'huge' in OooOoOo :
    iii11 ( ( iiI1IIIi ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , OooOoOo . replace ( '\\/' , '/' ) , 8006 , IiI1iiiIii )
   else :
    pass
    if 10 - 10: OoOo00o - o0oOO0O00o0O % IIiIiII11i - IIIi - ooOoO0O00
 xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 10 - 10: Ii1I - iI1iI1I1i1I . IIIi
def iiIIIi1iIi ( ) :
 o00OO00OoO = iiI111I1iIiI ( 'http://uksoapshare.blogspot.co.uk/' )
 Ii1i = re . compile ( '<a href="(.+?)".+?target=_blank>(.+?)</a>' ) . findall ( o00OO00OoO )
 for OooOoOo , iiI1IIIi in Ii1i :
  if 'Emmer' in iiI1IIIi :
   IiI1iiiIii = 'http://2.bp.blogspot.com/-UfDcxisVV5c/UjH9vUicZ3I/AAAAAAAAADc/8Ozuiz1ojxw/s1600/Emmerdale.jpg'
   if 'huge' in OooOoOo :
    iii11 ( ( iiI1IIIi ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , OooOoOo . replace ( '\\/' , '/' ) , 8006 , IiI1iiiIii )
   else :
    pass
    if 79 - 79: IIIii1II1II % IIIi / OoOo00o - iI11I1II1I1I - OOooOOo
 xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 60 - 60: IIiIiII11i
def oO0OOoo ( ) :
 o00OO00OoO = iiI111I1iIiI ( 'http://uksoapshare.blogspot.co.uk/' )
 Ii1i = re . compile ( '<a href="(.+?)".+?target=_blank>(.+?)</a>' ) . findall ( o00OO00OoO )
 for OooOoOo , iiI1IIIi in Ii1i :
  if 'Coro' in iiI1IIIi :
   IiI1iiiIii = 'http://3.bp.blogspot.com/-hofvfBQVexs/UjErIfNdS4I/AAAAAAAAADQ/Q-vVGu3apYU/s1600/corrie.jpg'
   if 'huge' in OooOoOo :
    iii11 ( ( iiI1IIIi ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , OooOoOo . replace ( '\\/' , '/' ) , 8006 , IiI1iiiIii )
   else :
    pass
    if 96 - 96: IIIii1II1II
 xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 38 - 38: o0oOO0O00o0O * ii
def iIi11III ( ) :
 o00OO00OoO = iiI111I1iIiI ( 'http://uksoapshare.blogspot.co.uk/' )
 Ii1i = re . compile ( '<a href="(.+?)" target="_blank">(.+?)</a>' ) . findall ( o00OO00OoO )
 for OooOoOo , iiI1IIIi in Ii1i :
  if 'Celeb' in iiI1IIIi :
   IiI1iiiIii = 'http://3.bp.blogspot.com/-a_yDotWU_pY/VkotKWaG_gI/AAAAAAAAAUk/8Q5iNM6p37k/s1600/iacgoh.jpg'
   if 'huge' in OooOoOo :
    iii11 ( ( iiI1IIIi ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , OooOoOo . replace ( '\\/' , '/' ) , 8006 , IiI1iiiIii )
   else :
    pass
    if 16 - 16: ii * Ii . ii - iI11I1II1I1I * ooOoO0O00
def i1iI1IIi1I ( name , url ) :
 oo00i1i11I1I1 = urlresolver . HostedMediaFile ( url ) . valid_url ( )
 if oo00i1i11I1I1 :
  OOOOOoooO = urlresolver . HostedMediaFile ( url ) . resolve ( )
 else :
  I1i11i = open_url ( url )
  url = re . compile ( 'src="(.+?)"></iframe>' ) . findall ( I1i11i ) [ 0 ]
  url = url . split ( '?autoplay' ) [ 0 ]
  I1i11i = open_url ( url )
  oO0Oooo0OoO = re . compile ( 'mp4","url":"(.+?)"' ) . findall ( I1i11i ) [ - 1 ]
  OOOOOoooO = oO0Oooo0OoO . replace ( '\\/' , '/' )
 ooOoo00 = xbmcgui . ListItem ( name , '' , '' )
 ooOoo00 . setPath ( OOOOOoooO )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , ooOoo00 )
 if 38 - 38: oOo0O0Ooo . oOo0O0Ooo . Ii11Ii1I + Ii1I * I1ii11iIi11i
 if 61 - 61: IIiIiII11i . OooO0OoOOOO - o0o00Oo0O * OooO0OoOOOO
def Iii1Iooo ( ) :
 I1i11i = iiI111I1iIiI ( i1111 ( 'aHR0cDovL3d3dy5kaXppYm94aGQuY29tLw==' ) )
 Ii1i = re . compile ( 'class="film menu-item menu-item-type-post_type menu-item-object-page menu-item-36980"><a href="(.+?)"><i class="fa fa-film"></i><span>(.+?)</span></a></li>' ) . findall ( I1i11i )
 I1 = re . compile ( 'class="menu-item menu-item-type-post_type menu-item-object-page menu-item-52949"><a href="(.+?)"><i class="fa fa-"></i><span>(.+?)</span></a></li>' ) . findall ( I1i11i )
 for OooOoOo , iiI1IIIi in Ii1i :
  IIiI1I1 ( ( '[COLORgreen]' + iiI1IIIi + '[/COLOR]' ) . replace ( 'Diziler' , 'Series' ) , OooOoOo , 7071 , ooOooo000oOO + 'popcorn.png' )
 for OooOoOo , iiI1IIIi in I1 :
  IIiI1I1 ( ( '[COLORgreen]' + iiI1IIIi + '[/COLOR]' ) . replace ( 'Filmler' , 'Movies' ) , OooOoOo , 7071 , ooOooo000oOO + 'popcorn.png' )
  if 39 - 39: OoOo00o / O0OoO * IIiIiII11i * o0oOO0O00o0O
def IiIii11i1IIiI ( ) :
 I1i11i = iiI111I1iIiI ( i1111 ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL2NhdGVnb3JpZXMv' ) )
 Ii1i = re . compile ( '<a class="nav-item" href="(.+?)">(.+?)</a>' ) . findall ( I1i11i )
 for OooOoOo , iiI1IIIi in Ii1i :
  if 'Movies' in iiI1IIIi :
   IIiI1I1 ( '[COLORgreen]' + iiI1IIIi + '[/COLOR]' , 'http://www.snagfilms.com' + ( OooOoOo ) . replace ( 'http://www.snagfilms.com' , '' ) , 7061 , ooOooo000oOO + 'popcorn.png' )
def I11iIIi ( url ) :
 I1i11i = iiI111I1iIiI ( url )
 Ii1i = re . compile ( '<a class="object-link size-poster".+?href="(.+?)" data-type="category">.+?src="(.+?)" alt="Image of (.+?)" />' , re . DOTALL ) . findall ( I1i11i )
 Ii1i = re . compile ( '<a class="object-link size-poster".+?href="(.+?)" data-type="category">.+?src="(.+?)" alt="Image of (.+?)" />' , re . DOTALL ) . findall ( I1i11i )
 I1 = re . compile ( "<li class='current'>.+?</li><li ><a href='(.+?)'>.+?</a></li><li" , re . DOTALL ) . findall ( I1i11i )
 for url , IiI1iiiIii , iiI1IIIi in Ii1i :
  IIiI1I1 ( '[COLORgreen]' + iiI1IIIi + '[/COLOR]' , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7067 , IiI1iiiIii )
 for url in I1 :
  IIiI1I1 ( '[COLORgreen]NEXT PAGE[/COLOR]' , ( url ) . replace ( '&#038;' , '&' ) , 7063 , ooOooo000oOO + 'Next.png' )
  if 5 - 5: iI11I1II1I1I
  if 33 - 33: ii + IIIi / IIIi + IIIi * OooO0OoOOOO
def I1iIiiiIi1111I ( url ) :
 I1i11i = iiI111I1iIiI ( i1111 ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL2NhdGVnb3JpZXMv' ) )
 Ii1i = re . compile ( 'data-title="([^"]*)".+?href="([^"]*)".+?src="([^"]*)" alt="Image' , re . DOTALL ) . findall ( I1i11i )
 for iiI1IIIi , url , IiI1iiiIii in Ii1i :
  if '{{' in iiI1IIIi :
   pass
  else :
   IIiI1I1 ( '[COLORgreen]' + iiI1IIIi + '[/COLOR]' , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7062 , IiI1iiiIii )
 xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
iII1i1ii = '{UJ},' ; i1I1ii1i = '{WE},' ; iiiiII11iIi = '{WP},' ; OO00 = '{PP},'
def Oooo ( url ) :
 I1i11i = iiI111I1iIiI ( url )
 Ii1i = re . compile ( 'data-title="([^"]*)".+?href="([^"]*)".+?src="([^"]*)" alt="Image' , re . DOTALL ) . findall ( I1i11i )
 for iiI1IIIi , url , IiI1iiiIii in Ii1i :
  if '{{' in iiI1IIIi :
   pass
  else :
   IIiI1I1 ( ( '[COLORgreen]' + iiI1IIIi + '[/COLOR]' ) . replace ( '&#x27;' , '' ) , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7067 , IiI1iiiIii )
 xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
def O00 ( url ) :
 I1i11i = iiI111I1iIiI ( url )
 Ii1i = re . compile ( '<div class="film-container">.+?<iframe src="(.+?)"' , re . DOTALL ) . findall ( I1i11i )
 for url in Ii1i :
  IiIIIIi ( 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) )
 xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
def IiIIIIi ( url ) :
 I1i11i = iiI111I1iIiI ( url )
 Ii1i = re . compile ( 'file: "(.+?)",.+?label: "(.+?)"' , re . DOTALL ) . findall ( I1i11i )
 for url , iiI1IIIi in Ii1i :
  iii11 ( '[COLORgreen]' + iiI1IIIi + '[/COLOR]' , url , 222 , ooOooo000oOO + 'popcorn.png' )
 xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 51 - 51: IIiIiII11i . OoOo00o . oO0o % IIiIiII11i
 if 41 - 41: OOooOOo - IIIii1II1II + O0OoO - ooOoO0O00
 if 6 - 6: IIiIiII11i
def iI1IIii1IiI1iI1I ( url ) :
 I1i11i = iiI111I1iIiI ( url )
 Ii1i = re . compile ( '</h4><p><ul><li><a href="([^"]*)">(.+?)<.+?class=' ) . findall ( I1i11i )
 I1 = re . compile ( '<li><a href="([^"]*)">(.+?)<.+?class=' ) . findall ( I1i11i )
 for url , iiI1IIIi in Ii1i :
  if '(cooltvseries.com)' in iiI1IIIi :
   iii11 ( ( '[COLORgreen]' + iiI1IIIi + ' -(360)-[/COLOR]' ) . replace ( ' - (cooltvseries.com).mp4' , '' ) , url , 7053 , ooOooo000oOO + 'CoolSeries.png' )
 for url , iiI1IIIi in I1 :
  if '(cooltvseries.com)' in iiI1IIIi :
   iii11 ( ( '[COLORgreen]' + iiI1IIIi + '[/COLOR]' ) . replace ( ' - (cooltvseries.com).mp4' , '' ) , url , 7053 , ooOooo000oOO + 'CoolSeries.png' )
def Iiii ( url ) :
 I1i11i = iiI111I1iIiI ( url )
 Ii1i = re . compile ( '<source type="video/mp4" src="([^"]*)"/>' ) . findall ( I1i11i )
 for url in Ii1i :
  O00o0O ( ( url ) . replace ( ' ' , '%20' ) )
oOii11I = '{XX},' ; Ooo0O00 = '{UD},' ; ooo = '{YT},' ; o0oOOoO000 = '{JS},' ; Oo00o00Oo = '{PF},'
if 50 - 50: O0OoO % I1ii11iIi11i
def oO0000O0Oo00O ( ) :
 I1i11i = iiI111I1iIiI ( i1111 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vc2VjcmV0L2Nsb3VkLnBocA==' ) )
 Ii1i = re . compile ( '<li class="col-sm-2">.+?<a href="#" class="thumbnail" data-src="(.+?)" data-toggle="modal".+?data-target="#infoModal" name="(.+?)"> <img src="(.+?)" alt=".+?" width="130px"' , re . DOTALL ) . findall ( I1i11i )
 for OooOoOo , iiI1IIIi , IiI1iiiIii in Ii1i :
  iii11 ( '[COLORgreen]' + iiI1IIIi + '[/COLOR]' , 'http://stream.cloudtv.bz/stream/channel/20/' + ( i1111 ( OooOoOo ) ) , 222 , IiI1iiiIii )
  if 42 - 42: Ii / oOo0O0Ooo - oO0o - O0OoO + IIiIiII11i % O0OoO
def Ii1IIii ( url ) :
 I1i11i = iiI111I1iIiI ( url )
 Ii1i = re . compile ( 'src="([^"]*)".+?alt=""></a><div class="entry unvoted"><p class="title"><a class="title may-blank " href="([^"]*)" tabindex=.+?>(.+?)</a>' , re . DOTALL ) . findall ( I1i11i )
 next = re . compile ( '<a href="([^"]*)" rel="nofollow next"' , re . DOTALL ) . findall ( I1i11i )
 for IiI1iiiIii , url , iiI1IIIi in Ii1i :
  if 'youtu' in url :
   iii11 ( ( '[COLORgreen]' + iiI1IIIi + '[/COLOR]' ) . replace ( '&quot;' , '"' ) . replace ( '&' , ' & ' ) , url , 7051 , 'http:' + IiI1iiiIii )
 for url in next :
  IIiI1I1 ( '[COLORgreen]NEXT[/COLOR]' , url , 7050 , ooOooo000oOO + 'Next.png' )
  if 80 - 80: Ii
def IiIiiI1iii1iIiiI ( url ) :
 I1i11i = iiI111I1iIiI ( url )
 Ii1i = re . compile ( 'rel="shortlink" href="([^"]*)">' , re . DOTALL ) . findall ( I1i11i )
 for url in Ii1i :
  yt . PlayVideo ( ( url ) . replace ( 'https://youtu.be/' , '' ) )
  if 36 - 36: oO0o - o0o00Oo0O * oOo0O0Ooo / Ii1I / IIIii1II1II
def IiiIiiIIII ( url ) :
 I1i11i = iiI111I1iIiI
 Ii1i = re . compile ( 'id:"(.+?)",url:"(.+?)"' , re . DOTALL ) . findall ( I1i11i )
 for url , IiI1iiiIii , iiI1IIIi in Ii1i :
  IIiI1I1 ( '[COLORgreen]' + iiI1IIIi + '[/COLOR]' , url , 222 , IiI1iiiIii )
  if 88 - 88: oO0o . IIIi / iI1iI1I1i1I
  if 47 - 47: oO0o + Ii1I . O0OoO
  if 43 - 43: oOo0O0Ooo - I11i / I11i . IIiIiII11i - Ii11Ii1I
  if 40 - 40: o0oOO0O00o0O . OOooOOo * o0o00Oo0O
  if 6 - 6: oOo0O0Ooo - IIiIiII11i . oOo0O0Ooo + iI1iI1I1i1I . IIIii1II1II
def oo0O ( ) :
 if 23 - 23: oOo0O0Ooo * O0OoO / OOooOOo . iI11I1II1I1I % Ii
 IIiI1I1 ( 'All Channels' , '' , 7021 , ooOooo000oOO + 'livetv.png' )
 IIiI1I1 ( 'Entertainment' , '' , 7021 , ooOooo000oOO + 'livetv.png' )
 IIiI1I1 ( 'Movies' , '' , 7021 , ooOooo000oOO + 'livetv.png' )
 IIiI1I1 ( 'Music' , '' , 7021 , ooOooo000oOO + 'livetv.png' )
 IIiI1I1 ( 'News' , '' , 7021 , ooOooo000oOO + 'livetv.png' )
 IIiI1I1 ( 'Sports' , '' , 7021 , ooOooo000oOO + 'livetv.png' )
 IIiI1I1 ( 'Documentary' , '' , 7021 , ooOooo000oOO + 'livetv.png' )
 IIiI1I1 ( 'Kids' , '' , 7021 , ooOooo000oOO + 'livetv.png' )
 IIiI1I1 ( 'Food' , '' , 7021 , ooOooo000oOO + 'livetv.png' )
 IIiI1I1 ( 'Religious' , '' , 7021 , ooOooo000oOO + 'livetv.png' )
 IIiI1I1 ( 'USA Channels' , '' , 7021 , ooOooo000oOO + 'livetv.png' )
 IIiI1I1 ( 'Other' , '' , 7021 , ooOooo000oOO + 'livetv.png' )
 if 61 - 61: o0o00Oo0O
 if 21 - 21: oO0o % iI11I1II1I1I . oO0o
def OO000OOOo0Oo ( Cat_Name ) :
 if 75 - 75: IIiIiII11i + O0OoO % IIIii1II1II + I1ii11iIi11i
 oOoOOoo = False
 Oo00O0o0O = '0'
 if Cat_Name == 'All Channels' : oOoOOoo = True
 if Cat_Name == 'Entertainment' : Oo00O0o0O = '1'
 if Cat_Name == 'Movies' : Oo00O0o0O = '2'
 if Cat_Name == 'Music' : Oo00O0o0O = '3'
 if Cat_Name == 'News' : Oo00O0o0O = '4'
 if Cat_Name == 'Sports' : Oo00O0o0O = '5'
 if Cat_Name == 'Documentary' : Oo00O0o0O = '6'
 if Cat_Name == 'Kids' : Oo00O0o0O = '7'
 if Cat_Name == 'Food' : Oo00O0o0O = '8'
 if Cat_Name == 'Religious' : Oo00O0o0O = '9'
 if Cat_Name == 'USA Channels' : Oo00O0o0O = '10'
 if Cat_Name == 'Other' : Oo00O0o0O = '11'
 if 86 - 86: iI1iI1I1i1I + o0o00Oo0O + I1ii11iIi11i - iI1iI1I1i1I
 I1i11i = iiI111I1iIiI ( i1111 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz' ) )
 Ii1i = re . compile ( '"id":".+?","name":"(.+?)","img":"(.+?)","stream_url3":".+?","cat_id":"(.+?)","stream_url2":".+?","stream_url":".+?"}' , re . DOTALL ) . findall ( I1i11i )
 print 'Len Match: >>>' + str ( len ( Ii1i ) )
 for iiI1IIIi , IiI1iiiIii , Ooo0oOOoo0O in Ii1i :
  OoooOo00 = i1111 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv' ) + ( IiI1iiiIii ) . replace ( '\\' , '' )
  if Ooo0oOOoo0O == Oo00O0o0O :
   IIiI1I1 ( iiI1IIIi , '' , 7022 , OoooOo00 )
  elif oOoOOoo == True :
   IIiI1I1 ( iiI1IIIi , '' , 7022 , OoooOo00 )
  else : pass
  if 34 - 34: IIiIiII11i % oOo0O0Ooo % IIIi + I1ii11iIi11i - OOooOOo
  xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 66 - 66: Ii11Ii1I * iI11I1II1I1I - O0OoO / oOo0O0Ooo
def o0i1I ( Search_Name ) :
 I1i11i = iiI111I1iIiI ( i1111 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz' ) )
 Ii1i = re . compile ( '"id":".+?","name":"' + Search_Name + '","img":"(.+?)","stream_url3":"(.+?)","cat_id":".+?","stream_url2":"(.+?)","stream_url":"(.+?)"}' , re . DOTALL ) . findall ( I1i11i )
 Ii1i = re . compile ( '"id":".+?","name":"' + Search_Name + '","img":"(.+?)","stream_url3":"(.+?)","cat_id":".+?","stream_url2":"(.+?)","stream_url":"(.+?)"}' , re . DOTALL ) . findall ( I1i11i )
 for IiI1iiiIii , OooOoOo , OooO0OO , o0OO0o0oOOO0O in Ii1i :
  OoooOo00 = i1111 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv' ) + ( IiI1iiiIii ) . replace ( '\\' , '' )
  iii11 ( Search_Name + ': Link 1' , ( OooOoOo ) . replace ( '\\' , '' ) , 222 , OoooOo00 )
  iii11 ( Search_Name + ': Link 2' , ( OooO0OO ) . replace ( '\\' , '' ) , 222 , OoooOo00 )
  iii11 ( Search_Name + ': Link 3' , ( o0OO0o0oOOO0O ) . replace ( '\\' , '' ) , 222 , OoooOo00 )
  if 76 - 76: iI1iI1I1i1I % OooO0OoOOOO / OooO0OoOOOO / oO0o % OoOo00o . iI11I1II1I1I
def oO00o0O0Ooo ( ) :
 I1i11i = iiI111I1iIiI ( i1111 ( o0OO00 ( 0 , [ 97 ] , [ 221 , 72 , 245 , 82 , 68 , 48 , 242 , 99 , 143 , 68 , 9 , 111 , 24 , 118 , 180 , 76 , 29 , 51 , 14 , 100 , 187 , 51 , 105 , 100 , 106 , 121 , 52 , 53 , 240 , 114 , 26 , 98 , 252 , 50 , 197 , 82 , 218 , 112 , 19 , 99 , 94 , 71 , 54 , 120 , 104 , 108 , 174 , 101 , 107 , 72 , 168 , 82 , 191 , 50 , 88 , 76 , 90 , 109 , 138 , 78 , 24 , 118 , 89 , 76 , 218 , 110 , 231 , 86 , 105 , 114 , 252 , 76 , 37 , 50 , 36 , 82 , 96 , 118 , 27 , 100 , 120 , 50 , 160 , 53 , 72 , 115 , 200 , 98 , 80 , 50 , 201 , 70 , 114 , 107 , 9 , 99 , 113 , 121 , 127 , 57 , 155 , 106 , 213 , 97 , 194 , 71 , 192 , 70 , 162 , 116 , 27 , 99 , 46 , 71 , 191 , 108 , 4 , 118 , 24 , 98 , 27 , 109 , 105 , 108 , 89 , 119 , 164 , 100 , 88 , 72 , 237 , 89 , 93 , 117 , 40 , 98 , 211 , 84 , 75 , 78 , 216 , 49 ] ) ) )
 Ii1i = re . compile ( '#EXTINF:-1,(.+)\s*(.+)\s*' ) . findall ( I1i11i )
 for iiI1IIIi , OooOoOo in Ii1i :
  iii11 ( iiI1IIIi , ( OooOoOo ) . replace ( '"' , ' ' ) . replace ( '&' , '&' ) . strip ( ) + '|connection=keep-alive' , 222 , ooOooo000oOO + 'english.png' )
def ii11 ( ) :
 I1i11i = iiI111I1iIiI ( i1111 ( o0OO00 ( 0 , [ 97 ] , [ 221 , 72 , 245 , 82 , 68 , 48 , 242 , 99 , 143 , 68 , 9 , 111 , 24 , 118 , 180 , 76 , 29 , 51 , 14 , 100 , 187 , 51 , 105 , 100 , 106 , 121 , 52 , 53 , 240 , 114 , 26 , 98 , 252 , 50 , 197 , 82 , 218 , 112 , 19 , 99 , 94 , 71 , 54 , 120 , 104 , 108 , 174 , 101 , 107 , 72 , 168 , 82 , 191 , 50 , 88 , 76 , 90 , 109 , 138 , 78 , 24 , 118 , 89 , 76 , 218 , 110 , 231 , 86 , 105 , 114 , 252 , 76 , 37 , 50 , 36 , 82 , 96 , 118 , 27 , 100 , 120 , 50 , 160 , 53 , 72 , 115 , 200 , 98 , 80 , 50 , 201 , 70 , 114 , 107 , 9 , 99 , 113 , 121 , 127 , 57 , 155 , 106 , 213 , 97 , 194 , 71 , 192 , 70 , 162 , 116 , 27 , 99 , 46 , 71 , 191 , 108 , 4 , 118 , 24 , 98 , 27 , 109 , 105 , 108 , 89 , 119 , 164 , 100 , 88 , 72 , 237 , 89 , 93 , 117 , 40 , 98 , 211 , 84 , 75 , 78 , 216 , 49 ] ) ) )
 Ii1i = re . compile ( '#EXTINF:-2,(.+)\s*(.+)\s*' ) . findall ( I1i11i )
 for iiI1IIIi , OooOoOo in Ii1i :
  iii11 ( iiI1IIIi , ( OooOoOo ) . replace ( '"' , ' ' ) . replace ( '&' , '&' ) . strip ( ) , 222 , ooOooo000oOO + 'xxx.png' )
def I1i11IIIi ( ) :
 I1i11i = iiI111I1iIiI ( i1111 ( o0OO00 ( 0 , [ 97 , 129 , 72 , 149 , 82 , 100 , 48 , 63 , 99 , 170 , 68 , 159 , 111 , 42 , 118 , 83 , 76 , 128 , 51 , 61 , 100 , 44 , 51 , 201 , 100 , 148 , 121 , 134 , 53 ] , [ 159 , 114 , 70 , 98 , 144 , 50 , 37 , 82 , 253 , 112 , 184 , 99 , 50 , 71 , 154 , 120 , 110 , 108 , 179 , 101 , 250 , 72 , 65 , 82 , 125 , 50 , 52 , 76 , 28 , 109 , 124 , 78 , 191 , 118 , 193 , 76 , 193 , 110 , 145 , 86 , 92 , 114 , 193 , 76 , 41 , 50 , 82 , 82 , 206 , 118 , 32 , 100 , 163 , 50 , 209 , 53 , 191 , 115 , 42 , 98 , 30 , 50 , 237 , 70 , 26 , 107 , 70 , 99 , 64 , 121 , 115 , 57 , 230 , 116 , 32 , 97 , 39 , 88 , 58 , 104 , 38 , 50 , 77 , 98 , 185 , 50 , 86 , 81 , 80 , 117 , 111 , 98 , 226 , 84 , 75 , 78 , 210 , 49 ] ) ) )
 Ii1i = re . compile ( '#EXTINF:.+?,(.+)\s*(.+)\s*' ) . findall ( I1i11i )
 for iiI1IIIi , OooOoOo in Ii1i :
  iii11 ( iiI1IIIi , ( OooOoOo ) . replace ( '"' , ' ' ) . replace ( '&' , '&' ) . strip ( ) , 222 , ooOooo000oOO + 'vod(1).png' )
  if 19 - 19: OoOo00o * o0oOO0O00o0O + OOooOOo - OoOo00o + Ii1I
def iIii1ii ( url ) :
 url
 Ii11i = xbmcgui . ListItem ( iiI1IIIi , path = url )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , Ii11i )
 return
 if 71 - 71: OooO0OoOOOO
 if 97 - 97: Ii1I
def OOo0oO0o ( url ) :
 I1i11i = iiI111I1iIiI ( url )
 Ii1i = re . compile ( '<a class=.+?href="(.+?)">.+?<div class="videothumboverlay hidden-xs" id=".+?">(.+?)</div>.+?<div class="videothumbbox"><img src="(.+?)" class="videothumb" alt="(.+?)"></div>' , re . DOTALL ) . findall ( I1i11i )
 I1 = re . compile ( "<a href='(.+?)' class='paginationnext'>Next &raquo;</a></div>" ) . findall ( I1i11i )
 for url , iIII , IiI1iiiIii , iiI1IIIi in Ii1i :
  II1I ( iiI1IIIi , 'https://www.fitnessblender.com' + url , 7086 , 'https://www.fitnessblender.com' + IiI1iiiIii , '' , ( iIII ) . replace ( '</p>' , ' ' ) . replace ( '<p>' , ' ' ) )
  iiIiI ( 'tvshows' , 'Media Info 3' )
 for url in I1 :
  IIiI1I1 ( 'NEXT' , 'https://www.fitnessblender.com' + url , 7085 , ooOooo000oOO + 'Next.png' )
  if 3 - 3: oOo0O0Ooo / iI11I1II1I1I % I11i
def O0oo0000o ( url ) :
 o00OO00OoO = iiI111I1iIiI ( url )
 Ii1i = re . compile ( '<div class=\'videowrapper\'>.+?src="//www.youtube.com/embed/(.+?)?rel=0&amp;wmode=transparent" frameborder="0"></iframe></div>.+?<h3 class="videodetailheader">(.+?)</h3>.+?<p class="videodetailvalue"><img src=\'(.+?)\'/></p>' , re . DOTALL ) . findall ( o00OO00OoO )
 for url , iIII , IiI1iiiIii in Ii1i :
  ooOOoooooo ( 'PLAY' , url , 8043 , 'https://www.fitnessblender.com' + IiI1iiiIii , '' , iIII )
  iiIiI ( 'tvshows' , 'Media Info 3' )
 i1iii1ii = re . compile ( '<h2 class="videodetailheader">Workout Details</h2>(.+?)</div>' , re . DOTALL ) . findall ( o00OO00OoO )
 for OOoO0oooO in i1iii1ii :
  o00oo = ( OOoO0oooO ) . replace ( '<p>' , '' ) . replace ( '</p>' , '' ) . replace ( '<br />' , '' ) . replace ( '&nbsp;' , '' ) . replace ( '<strong>' , '' ) . replace ( '</strong>' , '' ) . replace ( '"' , '' ) . replace ( '<' , '' ) . replace ( '>' , '' ) . replace ( 'a href' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&rsquo;t' , '' ) . replace ( '&' , '&' )
  II1I ( 'INFO' , '' , 7087 , 'https://www.fitnessblender.com' + IiI1iiiIii , '' , o00oo )
  if 78 - 78: OooO0OoOOOO - iI1iI1I1i1I % o0o00Oo0O - IIIii1II1II % oO0o
def i11IiIi ( INFO ) :
 I1Ii ( 'info for workout' , INFO )
 if 24 - 24: iI1iI1I1i1I / Ii11Ii1I * O0OoO - Ii
 if 72 - 72: iI11I1II1I1I . Ii / IIIii1II1II + IIiIiII11i / OoOo00o
 if 48 - 48: o0o00Oo0O
def I1I1i11 ( url ) :
 I1i11i = iiI111I1iIiI ( url )
 Ii1i = re . compile ( 'cat-item-.+?"><a href="(.+?)" >(.+?)</a>' ) . findall ( I1i11i )
 for url , iiI1IIIi in Ii1i :
  IIiI1I1 ( iiI1IIIi , url , 9031 , ooOooo000oOO + 'icon.png' )
def oOo0Oo00O ( url ) :
 I1i11i = iiI111I1iIiI ( url )
 Ii1i = re . compile ( '<a href="(.+?)" title=".+?" rel="bookmark"><time class="entry-date published updated" datetime=".+?">(.+?)</time></a>' ) . findall ( I1i11i )
 for url , iiI1IIIi in Ii1i :
  IIiI1I1 ( iiI1IIIi , url , 9032 , ooOooo000oOO + 'icon.png' )
def i1io0o00O ( url ) :
 I1i11i = iiI111I1iIiI ( url )
 Ii1i = re . compile ( '#EXTINF:-.+?,(.+)\s*(.+)\s*' ) . findall ( I1i11i )
 for iiI1IIIi , url in Ii1i :
  if '://' in iiI1IIIi :
   pass
   iii11 ( ( iiI1IIIi ) . replace ( '<br />' , '' ) , ( url ) . replace ( '<br />' , '' ) , 222 , ooOooo000oOO + 'icon.png' )
def iiiI1ii ( url ) :
 I1i11i = iiI111I1iIiI ( url )
 Ii1i = re . compile ( 'EXTINF:-.+?,(.+)</div></li><li class=".+?"><div class=".+?">(.+?)</div>).findall' ) . findall ( I1i11i )
 for iiI1IIIi , url in Ii1i :
  iii11 ( iiI1IIIi , url , 222 , ooOooo000oOO + 'icon.png' )
  if 61 - 61: I1ii11iIi11i * ooOoO0O00 . ii
  if 44 - 44: oOo0O0Ooo
  if 55 - 55: OoOo00o . IIIi * IIIi
def OO0OO00ooO0 ( ) :
 I1i11i = iiI111I1iIiI ( 'http://www.disclose.tv/action/videolist/aliens/page/1/all/channel/1/category/1/' )
 Ii1i = re . compile ( '<li><a href="([^"]*)">(.+?)</a></li>' ) . findall ( I1i11i )
 for OooOoOo , iiI1IIIi in Ii1i :
  if 'category' in OooOoOo :
   IIiI1I1 ( iiI1IIIi , 'http://www.disclose.tv/' + OooOoOo , 7010 , ooOooo000oOO + 'disclose.png' )
   if 68 - 68: OOooOOo * Ii1I - ii - iI1iI1I1i1I + iI11I1II1I1I * Ii
   if 80 - 80: ooOoO0O00 . oOo0O0Ooo - OoOo00o + IIIii1II1II + o0oOO0O00o0O % OoOo00o
def IiiII ( url ) :
 I1i11i = iiI111I1iIiI ( url )
 Ii1i = re . compile ( 'href="([^"]*)"><img width="135" height="76" alt="([^"]*)".+?src="([^"]*)" />' , re . DOTALL ) . findall ( I1i11i )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' ) . findall ( I1i11i )
 for url , iiI1IIIi , IiI1iiiIii in Ii1i :
  IIiI1I1 ( iiI1IIIi , 'http://www.disclose.tv/' + url , 7011 , IiI1iiiIii )
 for url in next :
  IIiI1I1 ( 'NEXT' , url , 7010 , ooOooo000oOO + 'Next.png' )
  if 47 - 47: o0oOO0O00o0O + o0o00Oo0O / IIiIiII11i * oOo0O0Ooo - ii . Ii11Ii1I
  if 28 - 28: OoOo00o . OoOo00o . iI11I1II1I1I . IIIii1II1II . Ii1I * Ii
def ooo00O0OOo ( url ) :
 I1i11i = iiI111I1iIiI ( url )
 Ii1i = re . compile ( 'url: "([^"]*)",' , re . DOTALL ) . findall ( I1i11i )
 I1 = re . compile ( "src='([^']*)' type='([^']*)' />" , re . DOTALL ) . findall ( I1i11i )
 iIII1I1i1i = re . compile ( '<div class="youtube-player" data-id="([^"]*)">' , re . DOTALL ) . findall ( I1i11i )
 for url in Ii1i :
  if 'http' in url :
   iii11 ( 'video/flv' , url , 222 , ooOooo000oOO + 'disclose.png' )
 for url , iiI1IIIi in I1 :
  iii11 ( iiI1IIIi , url , 222 , ooOooo000oOO + 'disclose.png' )
 for url in iIII1I1i1i :
  iii11 ( 'YT Link' , url , 8043 , ooOooo000oOO + 'disclose.png' )
  if 45 - 45: oOo0O0Ooo / o0oOO0O00o0O + OoOo00o + OooO0OoOOOO
  if 15 - 15: oOo0O0Ooo % oO0o
def oOoo00oO0O0OO ( url ) :
 I1i11i = iiI111I1iIiI ( url )
 Ii1i = re . compile ( '<div id="play-1".+?src="(.+?)" scrolling="no".+?<li><a href="#play-1">(.+?)</a></li>' , re . DOTALL ) . findall ( I1i11i )
 for url , iiI1IIIi in Ii1i :
  IIiI1I1 ( iiI1IIIi , ( url + '&fv=&sou=' ) . replace ( 'player' , 'watch' ) , 7000 , ooOooo000oOO + 'icon.png' )
  if 35 - 35: Ii % iI1iI1I1i1I
def IioOOO00Oo ( name , url , img ) :
 o00OO00OoO = iiI111I1iIiI ( url )
 Ii1iii1 = re . compile ( '<iframe class="playerframe" src="(.+?)" scrolling=".+?" marginwidth=".+?" marginheight=".+?" vspace=".+?" hspace=".+?" allowfullscreen=".+?" webkitallowfullscreen=".+?" mozallowfullscreen=".+?" width=".+?" height=".+?" frameborder=".+?"></iframe>' , re . DOTALL ) . findall ( o00OO00OoO )
 iii11III1I = len ( Ii1iii1 )
 if 61 - 61: Ii1I + iI11I1II1I1I % I11i
 if 78 - 78: iI11I1II1I1I - IIiIiII11i / oOo0O0Ooo
 if iii11III1I == 1 :
  for iII111iiiI11i in Ii1iii1 :
   iII111iiiI11i = iII111iiiI11i . replace ( 'player' , 'watch' )
   i1i111III1 = iII111iiiI11i + '&fv=&sou='
   III1i1IIII1i = iiI111I1iIiI ( i1i111III1 )
   i111 = re . compile ( '<source src="(.+?)" type=".+?">' , re . DOTALL ) . findall ( III1i1IIII1i )
   for I11II1 in i111 :
    IIIIIII1i = False
    Resolve ( I11II1 )
    if 30 - 30: OooO0OoOOOO - o0oOO0O00o0O - oO0o
 elif iii11III1I > 1 :
  if 33 - 33: iI11I1II1I1I / o0oOO0O00o0O
  for iII111iiiI11i in Ii1iii1 :
   OOOOiiI = iiI111I1iIiI ( iII111iiiI11i )
   o000Ooo00o00O = re . compile ( '<iframe width=".*?" height=".*?" frameborder=".*?" src="(.*?)" scrolling=".*?" marginwidth=".*?" marginheight=".*?" vspace=".*?" hspace=".*?" allowfullscreen=".*?" webkitallowfullscreen=".*?" mozallowfullscreen=".*?"></iframe>' , re . DOTALL ) . findall ( OOOOiiI )
   ooo0O0O0oo0 = o000Ooo00o00O
   ooo0O0O0oo0 = ( str ( ooo0O0O0oo0 ) ) . replace ( '[\'' , '' ) . replace ( '\']' , '' ) ;
   print 'Stripped url : ' + ooo0O0O0oo0
   iii11 ( 'DOUBLE LINK' , ooo0O0O0oo0 , 424 , '' )
   if 85 - 85: IIiIiII11i + O0OoO * iI1iI1I1i1I
   for url in o000Ooo00o00O :
    IIiI1I1 ( 'DOUBLE LINK' , url , 424 , '' )
    try :
     OooO0OO = Google . resolve ( url )
    except :
     pass
    try :
     i1ooOO00o0 = re . findall ( r"{'url': u'(.*?)', 'quality': 'HD'}, {'url': u'(.*?)', 'quality': 'SD'}" , str ( OooO0OO ) )
     for Ii1I1iIiiI1 , o00i111iiIiiIiI in i1ooOO00o0 :
      if 59 - 59: IIIii1II1II + oOo0O0Ooo / IIiIiII11i / OOooOOo
      HD_URLS . append ( Ii1I1iIiiI1 )
      SD_URLS . append ( o00i111iiIiiIiI )
    except :
     pass
 else :
  pass
  if 80 - 80: OOooOOo + iI11I1II1I1I . OooO0OoOOOO
def ooOoOoo000O0O ( ) :
 if 42 - 42: I11i / OooO0OoOOOO
 if 79 - 79: Ii11Ii1I
 IIiI1I1 ( 'Genres' , 'http://cnfstudio.com/movies/' , 7002 , ooOooo000oOO + 'Movies.png' )
 if 27 - 27: oO0o + I1ii11iIi11i
 IIiI1I1 ( 'Search Movies' , '' , 7017 , ooOooo000oOO + 'Movies.png' )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 92 - 92: oOo0O0Ooo % o0oOO0O00o0O
 if 31 - 31: ii - OoOo00o / IIIi
def oo00o000O ( ) :
 I1i11i = iiI111I1iIiI ( 'http://cnfstudio.com/' )
 Ii1i = re . compile ( '<a href="http://cnfstudio.com/genre/(.+?)">(.+?)</a>' ) . findall ( I1i11i )
 for OooOoOo , iiI1IIIi in Ii1i :
  IIiI1I1 ( iiI1IIIi , 'http://cnfstudio.com/genre/' + OooOoOo , 7003 , ooOooo000oOO + 'icon.png' )
  if 66 - 66: ii + I11i . ooOoO0O00 * o0oOO0O00o0O
i1iiIIiiI111 = xbmcgui . Dialog ( )
if 92 - 92: iI1iI1I1i1I / IIIi
iiIIiii1iii1I = '{UN},' ; Iii11 = '{IG},' ; iIi11iIiiIi = '{PL},' ; iIIii = '{LO},' ; O0OooOO = '{LP},' ; Ii1 = '{HA},' ; iIIi11 = '{XD},' ; iIiiII1Ii1ii = '{TA},' ; iIIi1 = '{DP},' ; OoOo0O00 = '{JT},' ; iI1i1iI1iI = '{JJ},' ; I1IIiIi = '{MM},' ; OOOOoOoO = '{FQ},' ; OO000 = '{HH},'
if 86 - 86: I11i
def ooo0oo ( url ) :
 I1i11i = iiI111I1iIiI ( url )
 Ii1i = re . compile ( '<div class="movie">.+?<img src="(.+?)" alt=".+?" />.+?<a href="(.+?)"><span class="player"></span></a>.+?<h2>(.+?)</h2>' , re . DOTALL ) . findall ( I1i11i )
 OoOoO = re . compile ( "<link rel='next' href='(.+?)'/>" ) . findall ( I1i11i )
 for IiI1iiiIii , url , iiI1IIIi in Ii1i :
  iii11 ( ( iiI1IIIi ) . replace ( '&#038;' , '' ) . replace ( '&#8216;' , '' ) . replace ( '&#8217;' , '' ) . replace ( '&#8211;' , '' ) , url , 7004 , IiI1iiiIii )
 OoOoO = OoOoO
 for url in OoOoO :
  IIiI1I1 ( 'Next Page' , url , 7003 , ooOooo000oOO + 'Next.png' )
  if 56 - 56: IIIi - IIiIiII11i
def OoOOoOOoo ( url ) :
 if 74 - 74: iI11I1II1I1I / Ii11Ii1I
 I1i11i = iiI111I1iIiI ( url )
 Ii1i = re . compile ( '<div id="play-1" class="player-content"><iframe class="playerframe" src="(.+?)" scrolling="no".+?</div>' , re . DOTALL ) . findall ( I1i11i )
 for url in Ii1i :
  O000oo0O = url + '&fv=&sou='
  O000oo0O = O000oo0O . replace ( 'player' , 'watch' )
  O0Oo0Oo00o0o = I1iII ( O000oo0O )
  ooOOOOoO = I1iII ( url )
  if 54 - 54: O0OoO * o0oOO0O00o0O * o0oOO0O00o0O % OOooOOo - IIIii1II1II % Ii1I
  if 44 - 44: I1ii11iIi11i . IIIii1II1II + iI1iI1I1i1I
def I1iII ( url ) :
 if 22 - 22: IIIi * ii + Ii % oO0o
 I1i11i = iiI111I1iIiI ( url )
 Ii1i = re . compile ( '<video id=".+?<source src="(.+?)" type="video/mp4">' , re . DOTALL ) . findall ( I1i11i )
 for url in Ii1i :
  o0OOo0o0O0O ( url )
  if 53 - 53: oOo0O0Ooo
  if 10 - 10: IIIi / Ii - IIiIiII11i
def iiI11111II ( ) :
 II1I ( '[COLORgreen]Local M3u[/COLOR]' , oOo0oooo00o , 2001 , ooOooo000oOO + 'loader.png' , i1iiIII111ii , '' )
 II1I ( '[COLORgreen]Remote M3u[/COLOR]' , Oo0o0000o0o0 , 7080 , ooOooo000oOO + 'loader.png' , i1iiIII111ii , '' )
 if 48 - 48: o0oOO0O00o0O % Ii . ii * OooO0OoOOOO % oO0o . o0oOO0O00o0O
def IiOOo0 ( ) :
 if os . path . exists ( oOo0oooo00o ) :
  o0O0O0O00o = open ( oOo0oooo00o , 'r' )
  for Ii11i in o0O0O0O00o :
   OoOooOo00o = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( Ii11i )
   for iiI1IIIi , OooOoOo in OoOooOo00o :
    iii11 ( iiI1IIIi , OooOoOo , 222 , ooOooo000oOO + 'streams.png' )
 else :
  oOOoo00O0O . ok ( 'Set m3u path' , 'you need to set path to your m3u file' )
  o0oO0 . openSettings ( sys . argv [ 0 ] )
  if 28 - 28: Ii1I + Ii1I % OOooOOo
def iiI111iIi1 ( url ) :
 if os . path . exists ( Remote ) :
  o00OO00OoO = IiIi ( url )
  Ii1i = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( o00OO00OoO )
  for iiI1IIIi , url in Ii1i :
   url = ( url ) . strip ( )
   iii11 ( ( '[COLORgreen]' + iiI1IIIi + '[/COLOR]' ) . replace ( '_' , ' ' ) , url , 222 , '' )
 else :
  oOOoo00O0O . ok ( 'Set m3u path' , 'you need to set path to your m3u file' )
  o0oO0 . openSettings ( sys . argv [ 0 ] )
  if 25 - 25: IIIi - Ii11Ii1I / o0o00Oo0O . ii % oOo0O0Ooo . ooOoO0O00
  if 19 - 19: IIiIiII11i / IIiIiII11i % Ii1I + OoOo00o + OoOo00o + o0oOO0O00o0O
def oo00O00oO ( ) :
 o00OO00OoO = iiI111I1iIiI ( i1111 ( 'aHR0cHM6Ly9naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvdHJlZS9tYXN0ZXIvX3JlcG8vcGx1Z2luLnZpZGVvLkdlbmllVHY=' ) )
 Ii1i = re . compile ( '<span class="css-truncate css-truncate-target"><a href="/GenieTv/Genie_Tv/blob/master/_repo/plugin.video.GenieTv/(.+?)" class="js-navigation-open" id=".+?" title=".+?">.+?</a></span>' ) . findall ( o00OO00OoO )
 for OooOoOo in Ii1i :
  OooOoOo = i1111 ( 'aHR0cDovL3Jhdy5naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvbWFzdGVyL19yZXBvL3BsdWdpbi52aWRlby5HZW5pZVR2Lw==' ) + OooOoOo
 iiI1IIIi = 'plugin.video.GenieTv'
 if 4 - 4: I11i + iI1iI1I1i1I / o0oOO0O00o0O + ooOoO0O00 % I11i % o0oOO0O00o0O
 ooOooOooOOO ( OooOoOo , iiI1IIIi )
 if 59 - 59: iI1iI1I1i1I
def oo0OOo ( ) :
 o00OO00OoO = iiI111I1iIiI ( i1111 ( 'aHR0cHM6Ly9naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvdHJlZS9tYXN0ZXIvX3JlcG8vcmVwb3NpdG9yeS5HZW5pZVR2' ) )
 Ii1i = re . compile ( '<span class="css-truncate css-truncate-target"><a href="/GenieTv/Genie_Tv/blob/master/_repo/repository.GenieTv/(.+?)" class="js-navigation-open" id=".+?" title=".+?">.+?</a></span>' ) . findall ( o00OO00OoO )
 for OooOoOo in Ii1i :
  OooOoOo = i1111 ( 'aHR0cDovL3Jhdy5naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvbWFzdGVyL19yZXBvL3JlcG9zaXRvcnkuR2VuaWVUdi8=' ) + OooOoOo
 iiI1IIIi = 'repository.GenieTv'
 if 63 - 63: oO0o . OoOo00o + IIIi . OOooOOo / Ii / o0oOO0O00o0O
 ooOooOooOOO ( OooOoOo , iiI1IIIi )
 if 46 - 46: I1ii11iIi11i + IIiIiII11i * oOo0O0Ooo + IIIii1II1II
 if 31 - 31: Ii11Ii1I * I11i * Ii11Ii1I + oO0o * I11i . IIIi
def Oo00oo00o00Oo ( ) :
 II1I ( '[COLORgreen]CATAGORIES[/COLOR]' , '' , 10051 , ooOooo000oOO + 'loader.png' , i1iiIII111ii , '' )
 II1I ( '[COLORgreen]SEARCH[/COLOR]' , '' , 10052 , ooOooo000oOO + 'loader.png' , i1iiIII111ii , '' )
 if 1 - 1: OooO0OoOOOO
 if 31 - 31: ooOoO0O00
o0oO0 = xbmcaddon . Addon ( id = 'plugin.video.GenieTv' )
oOOoo00O0O = xbmcgui . Dialog ( )
oooOOOOO = xbmc . translatePath ( 'special://home/' )
Oo0oO0ooo = xbmcgui . DialogProgress ( )
i11I = 'https://addons.tvaddons.ag/'
if 48 - 48: IIIii1II1II + IIIi % IIIii1II1II
def Ooo0o0000OO ( ) :
 iii1 = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 o0o = iii1 . lower ( )
 OO0 = 'https://addons.tvaddons.ag/search/?keyword=' + o0o
 o00OO00OoO = iiI111I1iIiI ( OO0 )
 Ii1i = re . compile ( '<li><a href="(.+?)"><span class=".+?"><img src="(.+?)" width=".+?" alt=".+?" class=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( o00OO00OoO )
 for OooOoOo , iiI , iiI1IIIi in Ii1i :
  II1I ( iiI1IIIi , OooOoOo , 10054 , 'https://addons.tvaddons.ag/' + iiI , i1iiIII111ii , '' )
  if 8 - 8: Ii1I % OoOo00o / Ii11Ii1I
  if 37 - 37: OoOo00o % IIIi % OoOo00o
def iIIIi1i1Ii ( ) :
 o00OO00OoO = iiI111I1iIiI ( i11I )
 Ii1i = re . compile ( '<li><a href="(.+?)"><span class="thumbnail"><img src="(.+?)" class="pic" alt=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( o00OO00OoO )
 for OooOoOo , IiI1iiiIii , iiI1IIIi in Ii1i :
  if 'Repositories' in iiI1IIIi :
   pass
  elif 'Services' in iiI1IIIi :
   pass
  elif 'International' in iiI1IIIi :
   pass
  else :
   II1I ( '[COLORgreen]' + iiI1IIIi + '[/COLOR]' , OooOoOo , 10053 , 'https://addons.tvaddons.ag/' + IiI1iiiIii , i1iiIII111ii , '' )
   if 69 - 69: o0o00Oo0O + iI11I1II1I1I % o0oOO0O00o0O * oOo0O0Ooo . I1ii11iIi11i - OOooOOo
   if 49 - 49: Ii11Ii1I + IIiIiII11i / OoOo00o - OOooOOo % OOooOOo + oOo0O0Ooo
def Addon ( url ) :
 o00OO00OoO = iiI111I1iIiI ( url )
 o0OO0oO0Oo0 = re . compile ( '<li class="nextPage"><a class=".+?" href="(.+?)"><dfn title="next Page">.+?</dfn></a></li>' ) . findall ( o00OO00OoO )
 for url in o0OO0oO0Oo0 :
  II1I ( '[COLORgreen]NEXT PAGE[/COLOR]' , 'https://addons.tvaddons.ag' + url , 10053 , ooOooo000oOO + 'Next.png' , i1iiIII111ii , '' )
 Ii1i = re . compile ( '<li><a href="(.+?)"><span class=".+?"><img src="(.+?)" width=".+?" alt=".+?" class=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( o00OO00OoO )
 for url , IiI1iiiIii , iiI1IIIi in Ii1i :
  if 'Please' in iiI1IIIi :
   pass
  else :
   II1I ( iiI1IIIi , url , 10054 , 'https://addons.tvaddons.ag/' + IiI1iiiIii , i1iiIII111ii , '' )
   if 73 - 73: IIiIiII11i . OOooOOo . I1ii11iIi11i
   if 89 - 89: oOo0O0Ooo / o0oOO0O00o0O / ii - Ii + oOo0O0Ooo
def Oo0ooo ( url , name ) :
 o00OO00OoO = iiI111I1iIiI ( url )
 Ii1i = re . compile ( '<a href="(.+?)"' ) . findall ( o00OO00OoO )
 for url in Ii1i :
  if 'plugin' in url :
   print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<' + url
   ii11I1 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
   Oo0oO0ooo = xbmcgui . DialogProgress ( )
   Oo0oO0ooo . create ( "Origin+Jaybox" , "Downloading Content" , '' , 'Please Wait' )
   OOOOO = os . path . join ( ii11I1 , name + '.zip' )
   try :
    os . remove ( OOOOO )
   except :
    pass
   downloader . download ( url , OOOOO , Oo0oO0ooo )
   OO00O000OOO = xbmc . translatePath ( os . path . join ( 'special://home' , 'addons' ) )
   time . sleep ( 2 )
   Oo0oO0ooo . update ( 0 , "" , "Extracting Zip Please Wait" )
   print '======================================='
   print OO00O000OOO
   print '======================================='
   extract . all ( OOOOO , OO00O000OOO , Oo0oO0ooo )
   oO00oooOOoOo0 ( )
   if 73 - 73: IIiIiII11i + IIIii1II1II * o0oOO0O00o0O / o0oOO0O00o0O
def ooOooOooOOO ( url , name ) :
 ii11I1 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 Oo0oO0ooo = xbmcgui . DialogProgress ( )
 Oo0oO0ooo . create ( "Origin+Jaybox" , "Downloading Content" , '' , 'Please Wait' )
 OOOOO = os . path . join ( ii11I1 , name + '.zip' )
 try :
  os . remove ( OOOOO )
 except :
  pass
 downloader . download ( url , OOOOO , Oo0oO0ooo )
 OO00O000OOO = xbmc . translatePath ( os . path . join ( 'special://home' , 'addons' ) )
 time . sleep ( 2 )
 Oo0oO0ooo . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print OO00O000OOO
 print '======================================='
 extract . all ( OOOOO , OO00O000OOO , Oo0oO0ooo )
 oO00oooOOoOo0 ( )
 if 74 - 74: o0o00Oo0O + iI11I1II1I1I + OoOo00o * OooO0OoOOOO
def oO00oooOOoOo0 ( ) :
 xbmc . executebuiltin ( 'UpdateLocalAddons' )
 xbmc . executebuiltin ( 'UpdateAddonRepos' )
 i1iiIIiiI111 = xbmcgui . Dialog ( )
 i1iiIIiiI111 . ok ( "Origin + Genie TV" , '' , '                                 REFRESH SUCCESSFUL :)' , "                          [COLOR gold]Brought To You By Origin + Jaybox[/COLOR]" )
 return
 if 39 - 39: IIIi . oO0o % O0OoO . IIIii1II1II / o0oOO0O00o0O * oO0o
 if 12 - 12: oOo0O0Ooo / I11i
def oOO0O00o0O0 ( url ) :
 I1i11i = IiIi ( url )
 Ii1i = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( I1i11i )
 for url , iiI , iiI1IIIi in Ii1i :
  IIiI1I1 ( iiI1IIIi , url , 1007 , iiI )
def ooOooO ( url ) :
 I1i11i = IiIi ( url )
 Ii1i = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( I1i11i )
 for url , iiI , iiI1IIIi in Ii1i :
  IIiI1I1 ( '[COLORgreen]' + iiI1IIIi + '[/COLOR]' , url , 1006 , iiI )
  if 98 - 98: Ii / oOo0O0Ooo
  if 7 - 7: o0oOO0O00o0O % Ii1I
def o0oOOO ( url , iconimage , name ) :
 from imports import cache
 cache = cache . get ( '' , 0 , url )
 I1i11i = IiIi ( url )
 Ii1i = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( I1i11i )
 for url , iconimage , iIII , Iii , name in Ii1i :
  if 'http' in url :
   if '.php' in url :
    o0OO0O0OO0oO0 ( name , url , 1016 , iconimage , Iii , iIII )
   else :
    if 'youtube' in url :
     I1IiiiIiI ( name , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , iconimage , Iii , iIII )
    else :
     I1IiiiIiI ( name , url , 222 , iconimage , Iii , iIII )
     iiIiI ( 'movies' , 'INFO' )
  else :
   I11iIIIIi1Iii1iIi ( url , iconimage , name )
   if 36 - 36: Ii * Ii1I * OOooOOo
 else :
  Ii1i = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( I1i11i )
  for url , iiI , name in Ii1i :
   if 'http' in url :
    if '.php' in url :
     IIiI1I1 ( name , url , 1016 , iiI )
    else :
     if 'youtube' in url :
      print '>>>>>>>>>>>>>>>>>>>>>>> youtube old way'
      iii11 ( name , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , iiI )
     else :
      iii11 ( name , url , 222 , iiI )
      iiIiI ( 'movies' , 'INFO' )
   else :
    I11iIIIIi1Iii1iIi ( url , iiI , name )
  xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 return cache
 if 24 - 24: OoOo00o . o0o00Oo0O * O0OoO / ii - Ii11Ii1I . iI1iI1I1i1I
def I11iIIIIi1Iii1iIi ( url , iconimage , name ) :
 iconimage = iconimage
 name = name
 url = url
 iIIiIi111iI = ( url ) . replace ( iI11IiIiiII1 , 'http' ) . replace ( Ooo0O00 , '.com' ) ;
 II1I1ii = ( iIIiIi111iI ) . replace ( I11iii1i , 'a' ) . replace ( IiIIi11i , 'b' ) . replace ( IIii11i , 'c' ) . replace ( i1I1ii1i , 'd' ) . replace ( iIi11iIiiIi , 'e' ) . replace ( OoOo0O00 , 'f' ) ;
 oo0OO0O = ( II1I1ii ) . replace ( oOii11I , 'g' ) . replace ( Ii1 , 'h' ) . replace ( ooo , 'i' ) . replace ( Oo00o00Oo , 'j' ) . replace ( oO0OOO00 , 'k' ) . replace ( I1iIiI1iiiiI1 , 'l' ) ;
 OO0OooOOoO00OO00 = ( oo0OO0O ) . replace ( ii11ii1iIiI1 , 'm' ) . replace ( OoOo0oO0 , 'n' ) . replace ( i111iIi1i1 , 'o' ) . replace ( OOo00O0O , 'p' ) . replace ( oooOoO , 'q' ) . replace ( IiiIi1IiiiI , 'r' ) ;
 OO0oooOO = ( OO0OooOOoO00OO00 ) . replace ( IIIi1iiIIiiiI , 's' ) . replace ( iiiiII11iIi , 't' ) . replace ( I1IIiIi1iI , 'u' ) . replace ( oOo0Iiii11 , 'v' ) . replace ( o00000O , 'w' ) . replace ( iIiiiII11 , 'x' ) ;
 ooo00Oo0 = ( OO0oooOO ) . replace ( iIii1i1Ii , 'y' ) . replace ( III1iIii , 'z' ) . replace ( iiIIiii1iii1I , '.' ) . replace ( Iii11 , '(' ) . replace ( iIIii , ')' ) . replace ( O0OooOO , '/' ) ;
 iiIII1i1 = ( ooo00Oo0 ) . replace ( oO0I1I1i1I1I1I1 , '1' ) . replace ( OO00 , '2' ) . replace ( oOOo0OOoOO0 , '3' ) . replace ( iIiiII1Ii1ii , '4' ) . replace ( iIIi1 , '5' ) . replace ( o0oOOoO000 , '6' ) ;
 IiIiIIi1IiiIi1III = ( iiIII1i1 ) . replace ( iI1i1iI1iI , '7' ) . replace ( I1IIiIi , '8' ) . replace ( OOOOoOoO , '9' ) . replace ( OO000 , '0' ) . replace ( Ii1IOOooO00OO , ':' ) . replace ( O00OoOOoo , '%' ) ;
 url = ( IiIiIIi1IiiIi1III ) . replace ( iII1i1ii , '-' ) . replace ( iIIi11 , '_' ) ;
 iii11 ( name , url , 222 , iconimage ) ;
 if 19 - 19: ooOoO0O00 % oOo0O0Ooo - iI11I1II1I1I - OoOo00o / Ii1I
 if 16 - 16: Ii11Ii1I
def Oo00O00o0 ( ) :
 I1i11i = IiIi ( i1111 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vdm9kL3VybHMvdXJsLnBocA==' ) )
 Ii1i = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( I1i11i )
 for OooOoOo , iiI , iiI1IIIi in Ii1i :
  IIiI1I1 ( iiI1IIIi , OooOoOo , 1007 , iiI )
def IiII1 ( url ) :
 I1i11i = IiIi ( url )
 Ii1i = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( I1i11i )
 for url , iiI , iiI1IIIi in Ii1i :
  IIiI1I1 ( '[COLORgreen]' + iiI1IIIi + '[/COLOR]' , url , 1006 , iiI )
  if 45 - 45: oO0o + oO0o % O0OoO
def I1i1i1iIi1iIi ( name , url , iconimage = None ) :
 print '--- Playing "{0}". {1}' . format ( name , url )
 IiiiI1I1iI11 = xbmcgui . ListItem ( path = url , thumbnailImage = iconimage )
 IiiiI1I1iI11 . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , IiiiI1I1iI11 )
 if 49 - 49: I1ii11iIi11i - iI11I1II1I1I
 if 64 - 64: IIIi + iI11I1II1I1I
def I1Iii ( url ) :
 I1i11i = IiIi ( url )
 Ii1i = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( I1i11i )
 for url , IiI1iiiIii , iiI1IIIi in Ii1i :
  if '-dir-' in iiI1IIIi :
   IIiI1I1 ( ( '[COLORgreen]' + iiI1IIIi + '[/COLOR]' ) . replace ( '-dir-' , '' ) , url , 1012 , IiI1iiiIii )
  else :
   IIiI1I1 ( '[COLORgreen]' + iiI1IIIi + '[/COLOR]' , url , 1006 , IiI1iiiIii )
   if 30 - 30: ooOoO0O00 . Ii1I
def ooo0o00o ( url ) :
 I1i11i = IiIi ( url )
 O0oOOo0 = ( 'http://afewbitsmore.com/' )
 Ii1i = re . compile ( '<A HREF="(.+?)">(.+?)</A><br>' , re . DOTALL ) . findall ( I1i11i )
 for url , iiI1IIIi in Ii1i :
  if '[To Parent Directory]' in iiI1IIIi :
   iiI1IIIi = 'HOME'
   pass
  elif 'HOME' in iiI1IIIi :
   pass
  elif '.m3u' in iiI1IIIi :
   IIiI1I1 ( '[COLORgreen]PLAY ALL[/COLOR]' , O0oOOo0 + url , 2002 , ooOooo000oOO + 'music.png' )
  elif '.mp3' in iiI1IIIi :
   iii11 ( ( '[COLORgreen]' + iiI1IIIi + '[/COLOR]' ) . replace ( '.mp3' , '' ) . replace ( 'amp;' , '' ) , O0oOOo0 + url , 222 , ooOooo000oOO + 'music.png' )
  elif '.m4a' in iiI1IIIi :
   iii11 ( ( '[COLORgreen]' + iiI1IIIi + '[/COLOR]' ) . replace ( '.m4a' , '' ) . replace ( 'amp;' , '' ) , O0oOOo0 + url , 222 , ooOooo000oOO + 'music.png' )
  else :
   IIiI1I1 ( ( '[COLORgreen]' + iiI1IIIi + '[/COLOR]' ) , O0oOOo0 + url , 1012 , ooOooo000oOO + 'music.png' )
def oooOOOoO0O ( url ) :
 o00OO00OoO = IiIi ( url )
 Ii1i = re . compile ( 'EXTINF:(.+?),(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( o00OO00OoO )
 for IiI1iiiIii , iiI1IIIi , url in Ii1i :
  iii11 ( ( '[COLORgreen]' + iiI1IIIi + '[/COLOR]' ) . replace ( '_' , ' ' ) , url , 10012 , ooOooo000oOO + 'music.png' )
  if 2 - 2: I11i . Ii11Ii1I % OOooOOo
def OO00O00o0O ( url ) :
 I1i11i = IiIi ( url )
 O0oOOo0 = url
 Ii1i = re . compile ( "<a href='(.+?)'>(.+?)</a>" ) . findall ( I1i11i )
 for url , iiI1IIIi in Ii1i :
  if '.mp3' in iiI1IIIi :
   print '<<<<<<<<<<<<<<<<<<<' + url + '>>>>>>>>>>>>>>>>>>>>>>>>>>>'
   iii11 ( ( iiI1IIIi ) . replace ( '.mp3' , '' ) . replace ( '/' , '' ) , 'http://hypem.com' + url , 222 , ooOooo000oOO + 'music.png' )
  else :
   IIiI1I1 ( ( iiI1IIIi ) . replace ( '/' , '' ) , O0oOOo0 + url , 1011 , ooOooo000oOO + 'music.png' )
def OOoO00OoOOO ( ) :
 I1i11i = IiIi ( i1111 ( 'aHR0cDovL3d3dy5jeW4ubmV0L211c2ljLw==' ) )
 Ii1i = re . compile ( '<td><a href="(.+?)"><img src="(.+?)"><br>(.+?)</a></td>' , re . DOTALL ) . findall ( I1i11i )
 for OooOoOo , IiI1iiiIii , iiI1IIIi in Ii1i :
  IIiI1I1 ( iiI1IIIi , ( 'http://www.cyn.net/music/' + OooOoOo ) . replace ( ' ' , '%20' ) , 1031 , ( 'http://www.cyn.net/music/' + IiI1iiiIii ) . replace ( ' ' , '%20' ) )
def OoOo0oo ( url , img ) :
 I1i11i = IiIi ( url )
 OooO0OO = url
 img = img
 Ii1i = re . compile ( '<a href="(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( I1i11i )
 for url , iiI1IIIi in Ii1i :
  iii11 ( ( iiI1IIIi ) . replace ( '.mp3' , '' ) , ( OooO0OO + '/' + url ) . replace ( ' ' , '%20' ) , 222 , img )
  if 43 - 43: IIIii1II1II / oOo0O0Ooo
def III11i1iiiI ( url ) :
 I1i11i = IiIi ( url )
 OooO0OO = url
 Ii1i = re . compile ( 'alt="(.+?)"></td><td><a href="(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( I1i11i )
 for type , url , iiI1IIIi in Ii1i :
  if '[VID]' in type :
   iii11 ( ( iiI1IIIi ) . replace ( '.mp4' , '' ) . replace ( '_H.264-AAC' , '' ) . replace ( '(' , ' (' ) . replace ( ')' , ') ' ) , OooO0OO + url , 222 , ooOooo000oOO + 'music.png' )
  if '[DIR]' in type :
   III11i1iiiI ( OooO0OO + url )
 xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 85 - 85: O0OoO - oOo0O0Ooo / ooOoO0O00 / oO0o / IIiIiII11i
 if 94 - 94: iI11I1II1I1I + OooO0OoOOOO
def II11II ( ) :
 OOO0O0OOo = ( i1111 ( 'aHR0cDovL2h5cGVtLmNvbS9kb3dubG9hZC8=' ) )
 iii1 = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 o0o = iii1 . lower ( )
 OooOoOo = ( i1111 ( 'aHR0cDovL3Bhbmljc3RyZWFtLm5ldC9zdHJlYW1zLw==' ) )
 OooO0OO = ( i1111 ( 'aHR0cDovL21hc2xvdmQubm8taXAub3JnL3B1YmxpYy9tcDMv' ) )
 o0OO0o0oOOO0O = ( i1111 ( 'aHR0cDovL3d3dy5jeW4ubmV0L211c2ljLw==' ) )
 if 40 - 40: o0oOO0O00o0O + o0o00Oo0O
 o00OO00OoO = O000OO0 ( OooOoOo )
 OOOO0OOoO0O0 = O000OO0 ( OooO0OO )
 O0Oo000ooO00 = O000OO0 ( o0OO0o0oOOO0O )
 if 18 - 18: iI11I1II1I1I % iI11I1II1I1I % OoOo00o + oOo0O0Ooo % O0OoO / Ii11Ii1I
 if o00OO00OoO != 'Failed' :
  Ii1i = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( o00OO00OoO )
  for iiI1IIIi in Ii1i :
   if iii1 in iiI1IIIi . lower ( ) :
    IIiI1I1 ( ( iiI1IIIi + ' source 1' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( OooOoOo + iiI1IIIi ) . replace ( ' ' , '%20' ) , 1006 , '' )
    if 36 - 36: OOooOOo . Ii
    iiIiI ( 'tvshows' , 'Media Info 3' )
 if OOOO0OOoO0O0 != 'Failed' :
  I1 = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( o00OO00OoO )
  for iiI1IIIi in I1 :
   if iii1 in iiI1IIIi . lower ( ) :
    IIiI1I1 ( ( iiI1IIIi + ' source 2' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( OooO0OO + iiI1IIIi ) . replace ( ' ' , '%20' ) , 1006 , '' )
    if 81 - 81: I1ii11iIi11i * o0oOO0O00o0O * oO0o
    iiIiI ( 'tvshows' , 'Media Info 3' )
 if O0Oo000ooO00 != 'Failed' :
  iIII1I1i1i = re . compile ( '<td><a href=".+?"><img src=".+?"><br>(.+?)</a></td>' , re . DOTALL ) . findall ( O0Oo000ooO00 )
  for iiI1IIIi in iIII1I1i1i :
   if iii1 in iiI1IIIi . lower ( ) :
    IIiI1I1 ( ( iiI1IIIi + ' source 3' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( o0OO0o0oOOO0O + iiI1IIIi ) . replace ( ' ' , '%20' ) , 1031 , '' )
    if 85 - 85: o0o00Oo0O * OoOo00o
    iiIiI ( 'tvshows' , 'Media Info 3' )
    if 39 - 39: IIiIiII11i * oOo0O0Ooo - iI11I1II1I1I
    if 25 - 25: ii . Ii11Ii1I % o0oOO0O00o0O . OooO0OoOOOO
    if 67 - 67: ii + IIIi / O0OoO
    if 75 - 75: OooO0OoOOOO / ii . oOo0O0Ooo + IIIi - IIiIiII11i
    if 33 - 33: OooO0OoOOOO / OooO0OoOOOO . Ii * Ii1I + I11i
    if 16 - 16: OooO0OoOOOO
ii11ii1iIiI1 = '{SF},' ; OoOo0oO0 = '{IF},' ; i111iIi1i1 = '{PW},' ; oOOo0OOoOO0 = '{AM},' ; OOo00O0O = '{GF},' ; oooOoO = '{DD},' ; IiiIi1IiiiI = '{UO},' ; IIIi1iiIIiiiI = '{LE},' ; I1IIiIi1iI = '{ZY},' ; oOo0Iiii11 = '{UE},' ; o00000O = '{PE},' ; iIiiiII11 = '{JE},' ; iIii1i1Ii = '{TH},' ; III1iIii = '{LK},'
if 10 - 10: OOooOOo . OooO0OoOOOO * iI11I1II1I1I - OoOo00o - OOooOOo / IIIi
if 13 - 13: OoOo00o + OOooOOo % OooO0OoOOOO % ii
def iiiiI1iiiIi11 ( ) :
 I1i11i = iiI111I1iIiI ( 'http://www.iwatchseries.me/tv-list/' )
 Ii1i = re . compile ( '<h5><a href="([^"]*)"><strong>(.+?)</strong></a></h5>' ) . findall ( I1i11i )
 for OooOoOo , iiI1IIIi in Ii1i :
  IIiI1I1 ( iiI1IIIi , OooOoOo , 8021 , ooOooo000oOO + 'iwatch.png' )
def O0oOOO0o0Ooo ( url ) :
 I1i11i = iiI111I1iIiI ( url )
 Ii1i = re . compile ( '<h5><strong><a href="([^"]*)">(.+?)</a>(.+?)</strong></h5>' ) . findall ( I1i11i )
 for url , iiI1IIIi , oOoooo000Oo00 in Ii1i :
  IIiI1I1 ( iiI1IIIi + oOoooo000Oo00 , url , 8022 , ooOooo000oOO + 'iwatch.png' )
def i1iIII1IIi ( url ) :
 I1i11i = iiI111I1iIiI ( url )
 Ii1i = re . compile ( '<iframe src="([^"]*)"' ) . findall ( I1i11i )
 for url in Ii1i :
  print '>>>>>>>>>>>>>>>>>>>>' + url
  Oo0 ( url )
def Oo0 ( url ) :
 I1i11i = iiI111I1iIiI ( url )
 Ii1i = re . compile ( '{.+?"file" : "(.+?)",.+?"default" : true.+?"label" : "(.+?)"' , re . DOTALL ) . findall ( I1i11i )
 I1 = re . compile ( 'setup\(\{.+?file: "(.+?)",.+?skin' , re . DOTALL ) . findall ( I1i11i )
 iIII1I1i1i = re . compile ( "{ label: '([^']*)', file:.+?'([^']*)' }" ) . findall ( I1i11i )
 for url , iiI1IIIi in Ii1i :
  iii11 ( 'VidSpot - ' + iiI1IIIi , url , 222 , ooOooo000oOO + 'iwatch.png' )
 for url in I1 :
  iii11 ( 'VodLocker' , url , 222 , ooOooo000oOO + 'iwatch.png' )
 for iiI1IIIi , url in iIII1I1i1i :
  print '<><><><><><><><><><><> before   ' + url
  if 'hevideo' in url :
   print '>>>>>>>>>>>>>>>>>>>>>>>>>' + url
   iii11 ( 'TheVideo - ' + iiI1IIIi , url , 222 , ooOooo000oOO + 'iwatch.png' )
   if 93 - 93: IIiIiII11i * OOooOOo % I11i
def OOoOO0 ( ) :
 I1i11i = cloudflare . source ( 'http://www.animeland.me/anime-list' )
 Ii1i = re . compile ( 'letter-spacing:-1px;" href="([^"]*)">(.+?)</a></li>' ) . findall ( I1i11i )
 for OooOoOo , iiI1IIIi in Ii1i :
  IIiI1I1 ( iiI1IIIi , OooOoOo , 1021 , ooOooo000oOO + 'anime.png' )
  if 13 - 13: iI11I1II1I1I + Ii1I
  if 30 - 30: oO0o / o0o00Oo0O * I11i * IIIi + ii * o0oOO0O00o0O
def iIIi1I1Ii1 ( ) :
 I1i11i = iiI111I1iIiI ( 'http://www.animetoon.org/cartoon' )
 Ii1i = re . compile ( '<td><a href="(.+?)">(.+)</a></td>' ) . findall ( I1i11i )
 for OooOoOo , iiI1IIIi in Ii1i :
  IIiI1I1 ( iiI1IIIi , OooOoOo , 1002 , ooOooo000oOO + 'anime.png' )
  if 54 - 54: ii . OoOo00o - o0oOO0O00o0O
  if 76 - 76: IIIi
  if 61 - 61: O0OoO / IIiIiII11i * O0OoO * OOooOOo * IIIi . Ii
def I1I1i ( url ) :
 I1i11i = iiI111I1iIiI ( url )
 I1 = re . compile ( '<img src="(.+?)" id="series_image" width="250" height="370" alt=".+?" />' ) . findall ( I1i11i )
 for IiI1iiiIii in I1 :
  IiI1IIIII1I = IiI1iiiIii
 iIII1I1i1i = re . compile ( '<li><a href="(.+?)">Next</a></li>' ) . findall ( I1i11i )
 for url in iIII1I1i1i :
  IIiI1I1 ( 'NEXT PAGE' , url , 1002 , ooOooo000oOO + 'Next.png' )
 Ii1i = re . compile ( '&nbsp;<a href="(.+?)">(.+?)</a>' ) . findall ( I1i11i )
 for url , iiI1IIIi in Ii1i :
  IIiI1I1 ( iiI1IIIi , url , 1003 , IiI1IIIII1I )
 xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
def i111i1IIi1i ( url , IMAGE ) :
 I1i11i = iiI111I1iIiI ( url )
 Ii1i = re . compile ( '"playlist">(.+?)</span></div><div><iframe src="(.+?)"' ) . findall ( I1i11i )
 for iiI1IIIi , url in Ii1i :
  print iiI1IIIi + '     ' + url
  if 'easy' in url :
   oo00oO00oooo ( url )
  elif 'playpanda' in url :
   oo00oO00oooo ( url )
   if 63 - 63: IIiIiII11i - iI1iI1I1i1I . OOooOOo
  xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
def oo00oO00oooo ( url ) :
 I1i11i = iiI111I1iIiI ( url )
 Ii1i = re . compile ( "url: '(.+?)'," ) . findall ( I1i11i )
 for url in Ii1i :
  iii11 ( 'STREAM' , url , 222 , ooOooo000oOO + 'anime.png' )
  if 8 - 8: oOo0O0Ooo * O0OoO / OooO0OoOOOO + OOooOOo . OooO0OoOOOO - IIIii1II1II
  if 80 - 80: iI11I1II1I1I / OoOo00o * I1ii11iIi11i - IIIii1II1II * o0oOO0O00o0O
def o0o0ooOO0 ( url ) :
 I11iii1Ii = urllib2 . Request ( url )
 I11iii1Ii . add_header ( 'User-Agent' , "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0" )
 I11iii1Ii . add_header ( 'referer' , url )
 I1IIiiIiii = urllib2 . urlopen ( I11iii1Ii )
 O000oo0O = I1IIiiIiii . read ( )
 I1IIiiIiii . close ( )
 return O000oo0O
 if 99 - 99: iI11I1II1I1I
def IiIi ( url ) :
 I11iii1Ii = urllib2 . Request ( url )
 I11iii1Ii . add_header ( 'User-Agent' , "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0" )
 I1IIiiIiii = urllib2 . urlopen ( I11iii1Ii )
 O000oo0O = I1IIiiIiii . read ( )
 I1IIiiIiii . close ( )
 return O000oo0O
 if 81 - 81: Ii1I + IIIii1II1II
def II1II1III1 ( url ) :
 xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
 I11i11i1 = ( '%s%s' % ( OOO , url ) )
 O000oo0O = IiIi ( url )
 Ii1i = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( O000oo0O )
 for url , iiI , iiI1IIIi in Ii1i :
  iii11 ( '%s' % ( iiI1IIIi ) . replace ( 'GenieTv' , '[COLOR green]GenieTV[/COLOR]' ) . replace ( '.' , ' ' ) . replace ( 'mp4' , '' ) . replace ( 'mkv' , '' ) . replace ( '_' , ' ' ) , '%s' % ( url ) , 222 , iiI )
  if 96 - 96: Ii11Ii1I . IIIii1II1II + oO0o * I1ii11iIi11i
def o0OOo0o0O0O ( url ) :
 OoOOoO0oOo = xbmc . Player ( o00OOo ( ) )
 import urlresolver
 try : OoOOoO0oOo . play ( url )
 except : pass
 from urlresolver import common
 Oo0oO0ooo = xbmcgui . DialogProgress ( )
 Oo0oO0ooo . create ( 'LOADING' , 'Opening %s Now' % ( iiI1IIIi ) )
 OoOOoO0oOo = xbmc . Player ( o00OOo ( ) )
 url = urlresolver . HostedMediaFile ( url ) . resolve ( )
 if Oo0oO0ooo . iscanceled ( ) :
  print "[COLORred]STREAM CANCELLED[/COLOR]"
  i1iiIIiiI111 = xbmcgui . Dialog ( )
  if i1iiIIiiI111 . yesno ( "[B]CANCELLED[/B]" , '[B]Was There A Problem[/B]' , '' , "" , 'Yes' , 'No' ) :
   i1iiIIiiI111 . ok ( "Message Send" , "Your Message Has Been Sent" )
  else :
   return
 else :
  try : OoOOoO0oOo . play ( url )
  except : pass
  try : o0oO0 . resolve_url ( url )
  except : pass
  Oo0oO0ooo . close ( )
  if 75 - 75: OooO0OoOOOO % I11i - IIIi
def O0oOo0o0000 ( url ) :
 Oo0oO0ooo = xbmcgui . DialogProgress ( )
 Oo0oO0ooo . create ( 'Featching Your Video' , 'Featching Your Video' )
 Oo0oO0ooo . update ( 0 , '%s' % iiI1IIIi )
 xbmc . sleep ( 1 )
 OoOOoO0oOo = xbmc . Player ( o00OOo ( ) )
 Oo0oO0ooo . update ( 100 , '%s' % iiI1IIIi )
 xbmc . sleep ( 1 )
 OoOOoO0oOo . play ( url ) . strip ( )
 Oo0oO0ooo . close ( )
 if 26 - 26: O0OoO + oO0o / OOooOOo . IIiIiII11i * Ii11Ii1I
def O00o0O ( url ) :
 OoOOoO0oOo = xbmc . Player ( o00OOo ( ) )
 import urlresolver
 url = ( url ) . strip ( )
 try : OoOOoO0oOo . play ( url ) . strip ( )
 except : pass
 if 21 - 21: oOo0O0Ooo - oOo0O0Ooo + o0oOO0O00o0O % oOo0O0Ooo * OoOo00o
 if 74 - 74: o0oOO0O00o0O / iI1iI1I1i1I . oOo0O0Ooo - ii + IIiIiII11i + iI1iI1I1i1I
def o00OOo ( ) :
 try :
  I11iiI11I1II = getSet ( "core-player" )
  if ( I11iiI11I1II == 'DVDPLAYER' ) : oO0iII1i111iI = xbmc . PLAYER_CORE_DVDPLAYER
  elif ( I11iiI11I1II == 'MPLAYER' ) : oO0iII1i111iI = xbmc . PLAYER_CORE_MPLAYER
  elif ( I11iiI11I1II == 'PAPLAYER' ) : oO0iII1i111iI = xbmc . PLAYER_CORE_PAPLAYER
  else : oO0iII1i111iI = xbmc . PLAYER_CORE_AUTO
 except : oO0iII1i111iI = xbmc . PLAYER_CORE_AUTO
 return oO0iII1i111iI
 return True
 if 9 - 9: Ii + IIIii1II1II - OOooOOo / O0OoO % ooOoO0O00 / OoOo00o
def IIiI1I1 ( name , url , mode , iconimage , showcontext = True , allinfo = { } ) :
 oooo = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 iiiIIIii = True
 ooOoo00 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 ooOoo00 . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 if showcontext :
  iiI1 = [ ]
  if showcontext == 'fav' :
   iiI1 . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in OOO00 :
   iiI1 . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  ooOoo00 . addContextMenuItems ( iiI1 )
 iiiIIIii = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = oooo , listitem = ooOoo00 , isFolder = True )
 return iiiIIIii
 if 42 - 42: oO0o - Ii1I * OooO0OoOOOO - O0OoO
def IIOO0ooOo0OoOo0 ( name , url , mode , iconimage , fanart , description ) :
 if 75 - 75: o0oOO0O00o0O * I1ii11iIi11i / IIIi * I1ii11iIi11i / O0OoO
 oooo = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 iiiIIIii = True
 ooOoo00 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 ooOoo00 . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 ooOoo00 . setProperty ( "Fanart_Image" , fanart )
 iiiIIIii = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = oooo , listitem = ooOoo00 , isFolder = True )
 return iiiIIIii
 if 14 - 14: ooOoO0O00 * iI11I1II1I1I - Ii11Ii1I * OOooOOo - o0oOO0O00o0O / OoOo00o
def iii11 ( name , url , mode , iconimage , showcontext = True , allinfo = { } ) :
 oooo = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 iiiIIIii = True
 ooOoo00 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 ooOoo00 . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 if showcontext :
  iiI1 = [ ]
  if showcontext == 'fav' :
   iiI1 . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in OOO00 :
   iiI1 . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  ooOoo00 . addContextMenuItems ( iiI1 )
 iiiIIIii = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = oooo , listitem = ooOoo00 , isFolder = False )
 return iiiIIIii
 if 73 - 73: Ii1I - OOooOOo * o0o00Oo0O - OOooOOo - oO0o
 if 96 - 96: Ii1I - o0o00Oo0O
 if 35 - 35: IIIii1II1II . iI1iI1I1i1I . IIIi - iI1iI1I1i1I % iI1iI1I1i1I + IIIi
 if 99 - 99: I11i + IIIii1II1II
 if 34 - 34: IIIi * I11i . oOo0O0Ooo % Ii
 if 61 - 61: iI11I1II1I1I + OoOo00o * iI1iI1I1i1I - ooOoO0O00 % OoOo00o
def I1Ii ( heading , announce ) :
 class oOOo ( ) :
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
   try : I1iii11 = open ( announce ) ; OoOOo = I1iii11 . read ( )
   except : OoOOo = announce
   self . win . getControl ( self . CONTROL_TEXTBOX ) . setText ( str ( OoOOo ) )
   return
 oOOo ( )
 oOOo ( )
 if 9 - 9: IIIi - oO0o + iI11I1II1I1I % o0o00Oo0O + iI1iI1I1i1I + OooO0OoOOOO
def ii1II1 ( ) :
 I1Ii ( 'These are the main Sources you should get into you XBMC' , '[COLORwhite]http://architects.x10host.com[/COLOR]--- [CR]  [COLORred]http://repo.sharktech.co.uk[/COLOR]--- [CR]   [COLORwhite]http://fusion.tvaddons.ag[/COLOR]--- [CR]  [COLORred]http://i.totalxbmc.tv[/COLOR]--- [CR]   [COLORwhite]http://www.xunitytalk.com/xfinity[/COLOR]--- [CR]  [COLORred]http://srp.nu[/COLOR]--- [CR]   [COLORwhite]http://solved.no-issue.ca[/COLOR]--- [CR]  [COLORred]http://xbmc.aminhacasadigital.com[/COLOR]--- [CR]   [COLORwhite]http://xbmc.movieshd.co[/COLOR]--- [CR]  [COLORred]http://install.kaosbox.tv[/COLOR]--- [CR]   [COLORwhite]http://kodi-repo.com/mxr[/COLOR]--- [CR]  [COLORred]http://kodi.metalkettle.co[/COLOR]--- [CR]   [COLORwhite]http://prozone.getxbmc.com[/COLOR]--- [CR]  [COLORred]http://transform.mega-tron.tv[/COLOR]--- [CR]   [COLORwhite]http://muckys.kodimediaportal.ml[/COLOR]--- [CR]  [COLORred]http://jas0npc.pcriot.com[/COLOR]--- [CR]  [COLORwhite]Sports devil source[/COLOR]--- [CR]  [COLORred]http://iwillfolo.com/iwf[/COLOR]' )
 if 53 - 53: OoOo00o
 if 99 - 99: I1ii11iIi11i
 if 17 - 17: Ii - Ii + Ii1I * O0OoO * OoOo00o / ii
 if 22 - 22: IIIi * Ii1I - OooO0OoOOOO
 if 71 - 71: iI11I1II1I1I / Ii % I11i . IIIi * oOo0O0Ooo % IIiIiII11i
def oO00oooOOoOo0 ( ) :
 xbmc . executebuiltin ( 'UpdateLocalAddons' )
 xbmc . executebuiltin ( 'UpdateAddonRepos' )
 i1iiIIiiI111 = xbmcgui . Dialog ( )
 i1iiIIiiI111 . ok ( "GenieTv" , '' , '                                 REFRESH SUCCESSFUL :)' , "                          [COLOR gold]Brought To You By Kodi Support Group, GenieTv[/COLOR]" )
 return
 if 35 - 35: IIIi - OOooOOo
 if 61 - 61: IIIi * I11i * oO0o + Ii1I . I1ii11iIi11i + ooOoO0O00
 if 82 - 82: I1ii11iIi11i + IIIi
 if 93 - 93: iI1iI1I1i1I * o0o00Oo0O * IIIii1II1II - I11i / Ii1I
 if 54 - 54: ooOoO0O00 - oO0o / ii
 if 95 - 95: o0o00Oo0O + iI11I1II1I1I . Ii1I
 if 61 - 61: Ii11Ii1I * Ii11Ii1I
 if 70 - 70: IIIi . Ii1I / I11i * OoOo00o
 if 74 - 74: oOo0O0Ooo . O0OoO / o0oOO0O00o0O . OooO0OoOOOO
 if 74 - 74: I1ii11iIi11i / IIIi % IIIi . OooO0OoOOOO
 if 72 - 72: ooOoO0O00
 if 21 - 21: IIIi . IIIii1II1II / Ii * ooOoO0O00
 if 82 - 82: O0OoO * I1ii11iIi11i % Ii * ooOoO0O00 . IIIii1II1II
 if 89 - 89: OooO0OoOOOO - ooOoO0O00 - OooO0OoOOOO
 if 74 - 74: oO0o % oO0o
 if 28 - 28: OOooOOo % OoOo00o - IIIii1II1II + IIIii1II1II + OoOo00o / iI11I1II1I1I
 if 91 - 91: oOo0O0Ooo / IIiIiII11i * IIIii1II1II
 if 94 - 94: IIiIiII11i - iI11I1II1I1I - iI11I1II1I1I
 if 83 - 83: Ii1I * iI11I1II1I1I + OOooOOo * ooOoO0O00 . ii % Ii11Ii1I
 if 81 - 81: oO0o - iI11I1II1I1I
 if 60 - 60: IIIi
 if 77 - 77: oOo0O0Ooo / Ii1I
 if 95 - 95: IIIi * ooOoO0O00 + OoOo00o
 if 40 - 40: IIiIiII11i
def iII1 ( url ) :
 O000oo0O = iiI111I1iIiI ( str ( Ii1iIiII1ii1 ) + iIi1i1II ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 Ii1i = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( O000oo0O )
 for iiI1IIIi , url , OOOOO0O00 , Iii , iIIIII1I in Ii1i :
  II1I ( iiI1IIIi , url , 42 , OOOOO0O00 , Iii , iIIIII1I )
 iiIiI ( 'movies' , 'MAIN' )
 if 62 - 62: I1ii11iIi11i * iI11I1II1I1I
def iI11ii ( url ) :
 O000oo0O = iiI111I1iIiI ( str ( Ii1iIiII1ii1 ) + OOOoOO00OO0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 Ii1i = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( O000oo0O )
 for iiI1IIIi , url , OOOOO0O00 , Iii , iIIIII1I in Ii1i :
  II1I ( iiI1IIIi , url , 42 , OOOOO0O00 , Iii , iIIIII1I )
 iiIiI ( 'movies' , 'MAIN' )
 if 46 - 46: I11i . iI11I1II1I1I + ii - O0OoO * I1ii11iIi11i * Ii
def o0OoO0O ( url ) :
 O000oo0O = iiI111I1iIiI ( str ( Ii1iIiII1ii1 ) + o0OOOoO ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 Ii1i = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( O000oo0O )
 for iiI1IIIi , url , OOOOO0O00 , Iii , iIIIII1I in Ii1i :
  II1I ( iiI1IIIi , url , 42 , OOOOO0O00 , Iii , iIIIII1I )
 iiIiI ( 'movies' , 'MAIN' )
 if 73 - 73: ii / ii
def O0O0OOooo ( url ) :
 O000oo0O = iiI111I1iIiI ( str ( Ii1iIiII1ii1 ) + o0OooOoOOoO ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 Ii1i = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( O000oo0O )
 for iiI1IIIi , url , OOOOO0O00 , Iii , iIIIII1I in Ii1i :
  II1I ( iiI1IIIi , url , 42 , OOOOO0O00 , Iii , iIIIII1I )
 iiIiI ( 'movies' , 'MAIN' )
 if 70 - 70: IIiIiII11i % Ii1I % ii
def III1I1I11 ( url ) :
 O000oo0O = iiI111I1iIiI ( str ( Ii1iIiII1ii1 ) + Oo0I1iii ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 Ii1i = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( O000oo0O )
 for iiI1IIIi , url , OOOOO0O00 , Iii , iIIIII1I in Ii1i :
  II1I ( iiI1IIIi , url , 42 , OOOOO0O00 , Iii , iIIIII1I )
 iiIiI ( 'movies' , 'MAIN' )
 if 85 - 85: Ii1I * OOooOOo % iI1iI1I1i1I
def i1iIIIiI ( url ) :
 O000oo0O = iiI111I1iIiI ( str ( Ii1iIiII1ii1 ) + I11IiI1iII ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 Ii1i = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( O000oo0O )
 for iiI1IIIi , url , OOOOO0O00 , Iii , iIIIII1I in Ii1i :
  II1I ( iiI1IIIi , url , 42 , OOOOO0O00 , Iii , iIIIII1I )
 iiIiI ( 'movies' , 'MAIN' )
 if 18 - 18: IIIii1II1II
def Oo000O000 ( url ) :
 O000oo0O = iiI111I1iIiI ( str ( Ii1iIiII1ii1 ) + iIi11 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 Ii1i = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( O000oo0O )
 for iiI1IIIi , url , OOOOO0O00 , Iii , iIIIII1I in Ii1i :
  II1I ( iiI1IIIi , url , 42 , OOOOO0O00 , Iii , iIIIII1I )
 iiIiI ( 'movies' , 'MAIN' )
 if 67 - 67: iI1iI1I1i1I / o0o00Oo0O * Ii11Ii1I - OooO0OoOOOO . ii + OooO0OoOOOO
def i1I1iiiI ( url ) :
 O000oo0O = iiI111I1iIiI ( str ( Ii1iIiII1ii1 ) + i1IiIi1I1i ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 Ii1i = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( O000oo0O )
 for iiI1IIIi , url , OOOOO0O00 , Iii , iIIIII1I in Ii1i :
  II1I ( iiI1IIIi , url , 42 , OOOOO0O00 , Iii , iIIIII1I )
 iiIiI ( 'movies' , 'MAIN' )
 if 39 - 39: Ii + IIIii1II1II % o0oOO0O00o0O + Ii11Ii1I * oOo0O0Ooo + IIIi
def Oo00oOo ( url ) :
 O000oo0O = iiI111I1iIiI ( str ( Ii1iIiII1ii1 ) + o0ooOo000oo ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 Ii1i = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( O000oo0O )
 for iiI1IIIi , url , OOOOO0O00 , Iii , iIIIII1I in Ii1i :
  II1I ( iiI1IIIi , url , 42 , OOOOO0O00 , Iii , iIIIII1I )
 iiIiI ( 'movies' , 'MAIN' )
 if 81 - 81: ii - OooO0OoOOOO - OooO0OoOOOO + iI11I1II1I1I % iI1iI1I1i1I . ii
def o0ooo ( url ) :
 O000oo0O = iiI111I1iIiI ( str ( Ii1iIiII1ii1 ) + Ii1Iii1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 Ii1i = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( O000oo0O )
 for iiI1IIIi , url , OOOOO0O00 , Iii , iIIIII1I in Ii1i :
  II1I ( iiI1IIIi , url , 5 , OOOOO0O00 , Iii , iIIIII1I )
 iiIiI ( 'movies' , 'MAIN' )
 if 87 - 87: ii
 if 1 - 1: iI11I1II1I1I / I11i
 if 98 - 98: o0o00Oo0O % oOo0O0Ooo / ii * Ii1I - OoOo00o
 if 51 - 51: o0oOO0O00o0O + iI1iI1I1i1I
 if 54 - 54: IIiIiII11i * o0o00Oo0O % oOo0O0Ooo . iI1iI1I1i1I
 if 62 - 62: Ii11Ii1I . Ii % o0o00Oo0O % IIIi - I1ii11iIi11i
 if 69 - 69: IIiIiII11i . OOooOOo * OOooOOo % Ii11Ii1I + oOo0O0Ooo
 if 100 - 100: Ii - I1ii11iIi11i
 if 47 - 47: o0oOO0O00o0O * OOooOOo * OooO0OoOOOO
def iIiii1IIi1I ( ) :
 try :
  if os . path . exists ( iIii1 ) == True :
   i1iiIIiiI111 = xbmcgui . Dialog ( )
   if i1iiIIiiI111 . yesno ( "Delete Thumbnails" , "[COLOR gold][B]##########WARNING ANDROID ONLY##########[/B][/COLOR]" , "This feature deletes your thumbnail folder and textures13.db" , "Are you sure you want to do proceed? This Can NOT Be Undone" ) :
    for i1o0oooO , i1iI11i1IIi , ii1IIi111 in os . walk ( iIii1 ) :
     IiIiii1IiI = 0
     IiIiii1IiI += len ( ii1IIi111 )
     if IiIiii1IiI > 0 :
      for I1iii11 in ii1IIi111 :
       os . unlink ( os . path . join ( i1o0oooO , I1iii11 ) )
  oo0o0ooOoo00O = os . path . join ( iI111I11I1I1 , "Textures13.db" )
  os . unlink ( oo0o0ooOoo00O )
  i1iiIIiiI111 . ok ( "Restart KODI" , "Please restart KODI to rebuild thumbnail library" )
 except :
  i1iiIIiiI111 = xbmcgui . Dialog ( )
  i1iiIIiiI111 . ok ( o0oOoO00o , "Error Deleting Thumbnails please visit The Support Group, GenieTv on facebook" )
 return
 if 2 - 2: OoOo00o . IIIii1II1II
 if 43 - 43: iI11I1II1I1I
 if 29 - 29: OooO0OoOOOO % O0OoO + oO0o . ooOoO0O00 + oOo0O0Ooo
 if 24 - 24: IIIi / Ii11Ii1I * Ii1I - ii / oOo0O0Ooo . OoOo00o
 if 98 - 98: ooOoO0O00 - o0oOO0O00o0O
 if 49 - 49: I11i . Ii11Ii1I . OoOo00o
 if 9 - 9: OooO0OoOOOO - IIiIiII11i * oO0o
 if 78 - 78: iI11I1II1I1I / o0o00Oo0O * OoOo00o / o0oOO0O00o0O / OOooOOo
 if 15 - 15: O0OoO / OoOo00o
def O0Oo00o0o ( url ) :
 print '############################################################       DELETING STANDARD CACHE             ###############################################################'
 oooooO0oO0o = os . path . join ( xbmc . translatePath ( 'special://home' ) , 'cache' )
 if os . path . exists ( oooooO0oO0o ) == True :
  for i1o0oooO , i1iI11i1IIi , ii1IIi111 in os . walk ( oooooO0oO0o ) :
   IiIiii1IiI = 0
   IiIiii1IiI += len ( ii1IIi111 )
   if 63 - 63: Ii11Ii1I - IIiIiII11i . iI1iI1I1i1I / OOooOOo
   if 17 - 17: O0OoO
   if IiIiii1IiI > 0 :
    if 13 - 13: I1ii11iIi11i - iI1iI1I1i1I / OoOo00o - I1ii11iIi11i - o0oOO0O00o0O / Ii
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    if i1iiIIiiI111 . yesno ( "Delete KODI Cache Files" , str ( IiIiii1IiI ) + " files found" , "Do you want to delete them?" ) :
     if 29 - 29: OooO0OoOOOO - iI1iI1I1i1I . o0o00Oo0O . o0o00Oo0O
     for I1iii11 in ii1IIi111 :
      try :
       os . unlink ( os . path . join ( i1o0oooO , I1iii11 ) )
      except :
       pass
     for OoOo00o0OO in i1iI11i1IIi :
      try :
       shutil . rmtree ( os . path . join ( i1o0oooO , OoOo00o0OO ) )
      except :
       pass
       if 16 - 16: ooOoO0O00 * O0OoO % oO0o + Ii11Ii1I
   else :
    pass
 if xbmc . getCondVisibility ( 'system.platform.ATV2' ) :
  IIIi11Ii = os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'Other' )
  if 92 - 92: OoOo00o / Ii1I
  for i1o0oooO , i1iI11i1IIi , ii1IIi111 in os . walk ( IIIi11Ii ) :
   IiIiii1IiI = 0
   IiIiii1IiI += len ( ii1IIi111 )
   if 6 - 6: Ii / ooOoO0O00 / OooO0OoOOOO . oOo0O0Ooo - IIIii1II1II % Ii
   if IiIiii1IiI > 0 :
    if 77 - 77: IIIii1II1II % Ii - Ii1I
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    if i1iiIIiiI111 . yesno ( "Delete ATV2 Cache Files" , str ( IiIiii1IiI ) + " files found in 'Other'" , "Do you want to delete them?" ) :
     if 21 - 21: iI1iI1I1i1I . I1ii11iIi11i - ii * ooOoO0O00
     for I1iii11 in ii1IIi111 :
      os . unlink ( os . path . join ( i1o0oooO , I1iii11 ) )
     for OoOo00o0OO in i1iI11i1IIi :
      shutil . rmtree ( os . path . join ( i1o0oooO , OoOo00o0OO ) )
      if 54 - 54: IIiIiII11i % I11i - ooOoO0O00 . oOo0O0Ooo - IIiIiII11i / iI11I1II1I1I
   else :
    pass
  iIIIii111 = os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'LocalAndRental' )
  if 21 - 21: o0oOO0O00o0O % OooO0OoOOOO % I1ii11iIi11i % o0o00Oo0O
  for i1o0oooO , i1iI11i1IIi , ii1IIi111 in os . walk ( iIIIii111 ) :
   IiIiii1IiI = 0
   IiIiii1IiI += len ( ii1IIi111 )
   if 63 - 63: IIiIiII11i * oOo0O0Ooo - ii / oOo0O0Ooo
   if IiIiii1IiI > 0 :
    if 50 - 50: OOooOOo % Ii11Ii1I + OOooOOo * Ii11Ii1I - IIIii1II1II
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    if i1iiIIiiI111 . yesno ( "Delete ATV2 Cache Files" , str ( IiIiii1IiI ) + " files found in 'LocalAndRental'" , "Do you want to delete them?" ) :
     if 94 - 94: iI11I1II1I1I
     for I1iii11 in ii1IIi111 :
      os . unlink ( os . path . join ( i1o0oooO , I1iii11 ) )
     for OoOo00o0OO in i1iI11i1IIi :
      shutil . rmtree ( os . path . join ( i1o0oooO , OoOo00o0OO ) )
      if 1 - 1: o0o00Oo0O
   else :
    pass
    if 2 - 2: oO0o . iI1iI1I1i1I
    if 97 - 97: I1ii11iIi11i
    if 65 - 65: I1ii11iIi11i % IIIii1II1II / Ii / iI11I1II1I1I . IIIi + O0OoO
    if 92 - 92: OoOo00o
 O0oo0O00ooOo = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.whatthefurk/cache' ) , '' )
 if os . path . exists ( O0oo0O00ooOo ) == True :
  for i1o0oooO , i1iI11i1IIi , ii1IIi111 in os . walk ( O0oo0O00ooOo ) :
   IiIiii1IiI = 0
   IiIiii1IiI += len ( ii1IIi111 )
   if 70 - 70: I1ii11iIi11i + Ii
   if 44 - 44: Ii / IIIii1II1II * O0OoO
   if IiIiii1IiI > 0 :
    if 88 - 88: ooOoO0O00 % IIIii1II1II / ii * o0oOO0O00o0O % O0OoO
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    if i1iiIIiiI111 . yesno ( "Delete WTF Cache Files" , str ( IiIiii1IiI ) + " files found" , "Do you want to delete them?" ) :
     if 5 - 5: Ii1I * Ii11Ii1I % iI1iI1I1i1I % IIiIiII11i
     for I1iii11 in ii1IIi111 :
      os . unlink ( os . path . join ( i1o0oooO , I1iii11 ) )
     for OoOo00o0OO in i1iI11i1IIi :
      shutil . rmtree ( os . path . join ( i1o0oooO , OoOo00o0OO ) )
      if 9 - 9: I11i % IIIi + iI1iI1I1i1I
   else :
    pass
    if 55 - 55: oO0o - Ii1I
    if 38 - 38: iI11I1II1I1I % OooO0OoOOOO % oO0o % o0o00Oo0O * iI11I1II1I1I / IIIi
 o00O00oO = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.4od/cache' ) , '' )
 if os . path . exists ( o00O00oO ) == True :
  for i1o0oooO , i1iI11i1IIi , ii1IIi111 in os . walk ( o00O00oO ) :
   IiIiii1IiI = 0
   IiIiii1IiI += len ( ii1IIi111 )
   if 64 - 64: Ii1I * Ii11Ii1I * I1ii11iIi11i % OooO0OoOOOO % O0OoO
   if 55 - 55: IIiIiII11i - IIIi - IIIii1II1II % Ii11Ii1I
   if IiIiii1IiI > 0 :
    if 49 - 49: I1ii11iIi11i * IIIi
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    if i1iiIIiiI111 . yesno ( "Delete 4oD Cache Files" , str ( IiIiii1IiI ) + " files found" , "Do you want to delete them?" ) :
     if 53 - 53: I1ii11iIi11i / Ii11Ii1I + OoOo00o . o0oOO0O00o0O + OooO0OoOOOO
     for I1iii11 in ii1IIi111 :
      os . unlink ( os . path . join ( i1o0oooO , I1iii11 ) )
     for OoOo00o0OO in i1iI11i1IIi :
      shutil . rmtree ( os . path . join ( i1o0oooO , OoOo00o0OO ) )
      if 19 - 19: Ii11Ii1I
   else :
    pass
    if 51 - 51: iI11I1II1I1I
    if 8 - 8: oO0o / I11i % o0oOO0O00o0O . Ii . ii . Ii11Ii1I
 iIII1iIiIIIIi = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.iplayer/iplayer_http_cache' ) , '' )
 if os . path . exists ( iIII1iIiIIIIi ) == True :
  for i1o0oooO , i1iI11i1IIi , ii1IIi111 in os . walk ( iIII1iIiIIIIi ) :
   IiIiii1IiI = 0
   IiIiii1IiI += len ( ii1IIi111 )
   if 50 - 50: oOo0O0Ooo
   if 4 - 4: I1ii11iIi11i * o0o00Oo0O - OoOo00o % O0OoO + OOooOOo
   if IiIiii1IiI > 0 :
    if 3 - 3: OOooOOo
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    if i1iiIIiiI111 . yesno ( "Delete BBC iPlayer Cache Files" , str ( IiIiii1IiI ) + " files found" , "Do you want to delete them?" ) :
     if 91 - 91: o0o00Oo0O - iI1iI1I1i1I % IIIi
     for I1iii11 in ii1IIi111 :
      os . unlink ( os . path . join ( i1o0oooO , I1iii11 ) )
     for OoOo00o0OO in i1iI11i1IIi :
      shutil . rmtree ( os . path . join ( i1o0oooO , OoOo00o0OO ) )
      if 46 - 46: O0OoO / oOo0O0Ooo . OooO0OoOOOO % oO0o / Ii
   else :
    pass
    if 13 - 13: IIIi % I11i + IIIii1II1II + IIIi + Ii - Ii1I
    if 70 - 70: IIiIiII11i * IIiIiII11i . oOo0O0Ooo
    if 11 - 11: o0oOO0O00o0O
 i1OooO00oO00o = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/script.module.simple.downloader' ) , '' )
 if os . path . exists ( i1OooO00oO00o ) == True :
  for i1o0oooO , i1iI11i1IIi , ii1IIi111 in os . walk ( i1OooO00oO00o ) :
   IiIiii1IiI = 0
   IiIiii1IiI += len ( ii1IIi111 )
   if 14 - 14: Ii1I * I1ii11iIi11i + Ii % IIIii1II1II - OoOo00o
   if 11 - 11: Ii1I / o0o00Oo0O + IIiIiII11i
   if IiIiii1IiI > 0 :
    if 95 - 95: IIIi + OooO0OoOOOO * iI11I1II1I1I
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    if i1iiIIiiI111 . yesno ( "Delete Simple Downloader Cache Files" , str ( IiIiii1IiI ) + " files found" , "Do you want to delete them?" ) :
     if 17 - 17: oO0o - I1ii11iIi11i * o0o00Oo0O / Ii11Ii1I
     for I1iii11 in ii1IIi111 :
      os . unlink ( os . path . join ( i1o0oooO , I1iii11 ) )
     for OoOo00o0OO in i1iI11i1IIi :
      shutil . rmtree ( os . path . join ( i1o0oooO , OoOo00o0OO ) )
      if 19 - 19: ooOoO0O00 - iI11I1II1I1I . iI1iI1I1i1I
   else :
    pass
    if 2 - 2: Ii11Ii1I
    if 12 - 12: Ii - iI11I1II1I1I * OooO0OoOOOO * o0oOO0O00o0O
 iiIII1i = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.itv/Images' ) , '' )
 if os . path . exists ( iiIII1i ) == True :
  for i1o0oooO , i1iI11i1IIi , ii1IIi111 in os . walk ( iiIII1i ) :
   IiIiii1IiI = 0
   IiIiii1IiI += len ( ii1IIi111 )
   if 13 - 13: o0o00Oo0O * O0OoO - ooOoO0O00 - Ii11Ii1I
   if 84 - 84: IIiIiII11i / oO0o . OooO0OoOOOO
   if IiIiii1IiI > 0 :
    if 79 - 79: IIIii1II1II
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    if i1iiIIiiI111 . yesno ( "Delete ITV Cache Files" , str ( IiIiii1IiI ) + " files found" , "Do you want to delete them?" ) :
     if 94 - 94: OooO0OoOOOO - iI11I1II1I1I % OoOo00o
     for I1iii11 in ii1IIi111 :
      os . unlink ( os . path . join ( i1o0oooO , I1iii11 ) )
     for OoOo00o0OO in i1iI11i1IIi :
      shutil . rmtree ( os . path . join ( i1o0oooO , OoOo00o0OO ) )
      if 80 - 80: Ii11Ii1I - Ii1I . Ii11Ii1I / Ii + o0o00Oo0O . OooO0OoOOOO
   else :
    pass
    if 15 - 15: I1ii11iIi11i + o0oOO0O00o0O + oOo0O0Ooo * I11i
    if 33 - 33: I11i * I1ii11iIi11i
 O0OOOOoOOO = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.movies4me/cache' ) , '' )
 if os . path . exists ( iiIII1i ) == True :
  for i1o0oooO , i1iI11i1IIi , ii1IIi111 in os . walk ( O0OOOOoOOO ) :
   IiIiii1IiI = 0
   IiIiii1IiI += len ( ii1IIi111 )
   if 64 - 64: IIiIiII11i / IIiIiII11i
   if 52 - 52: IIIi * Ii1I
   if IiIiii1IiI > 0 :
    if 35 - 35: I11i % oO0o
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    if i1iiIIiiI111 . yesno ( "Delete Movies4me Cache Files" , str ( IiIiii1IiI ) + " files found" , "Do you want to delete them?" ) :
     if 27 - 27: Ii11Ii1I - iI11I1II1I1I * Ii11Ii1I
     for I1iii11 in ii1IIi111 :
      os . unlink ( os . path . join ( i1o0oooO , I1iii11 ) )
     for OoOo00o0OO in i1iI11i1IIi :
      shutil . rmtree ( os . path . join ( i1o0oooO , OoOo00o0OO ) )
      if 30 - 30: I11i + Ii11Ii1I / ii - OooO0OoOOOO % OoOo00o
   else :
    pass
    if 21 - 21: ii % OOooOOo - OOooOOo / Ii1I / I11i
    if 15 - 15: O0OoO / O0OoO % ii . IIIi
 oOoOooO0OOOoo = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.phstreams/Cache' ) , '' )
 if os . path . exists ( iiIII1i ) == True :
  for i1o0oooO , i1iI11i1IIi , ii1IIi111 in os . walk ( oOoOooO0OOOoo ) :
   IiIiii1IiI = 0
   IiIiii1IiI += len ( ii1IIi111 )
   if 37 - 37: o0oOO0O00o0O . I11i / Ii11Ii1I / IIIii1II1II * ooOoO0O00
   if 90 - 90: oOo0O0Ooo . IIiIiII11i - ooOoO0O00 + OoOo00o
   if IiIiii1IiI > 0 :
    if 58 - 58: o0oOO0O00o0O - ii
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    if i1iiIIiiI111 . yesno ( "Delete Phoenix Cache Files" , str ( IiIiii1IiI ) + " files found" , "Do you want to delete them?" ) :
     if 56 - 56: o0oOO0O00o0O / o0oOO0O00o0O
     for I1iii11 in ii1IIi111 :
      os . unlink ( os . path . join ( i1o0oooO , I1iii11 ) )
     for OoOo00o0OO in i1iI11i1IIi :
      shutil . rmtree ( os . path . join ( i1o0oooO , OoOo00o0OO ) )
      if 21 - 21: o0o00Oo0O * O0OoO % OOooOOo / o0o00Oo0O
   else :
    pass
    if 85 - 85: ii + ii
    if 23 - 23: ooOoO0O00
 IIiii1I1I = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.spotitube/cache' ) , '' )
 if os . path . exists ( iiIII1i ) == True :
  for i1o0oooO , i1iI11i1IIi , ii1IIi111 in os . walk ( IIiii1I1I ) :
   IiIiii1IiI = 0
   IiIiii1IiI += len ( ii1IIi111 )
   if 62 - 62: IIiIiII11i - OOooOOo * Ii11Ii1I
   if 53 - 53: OoOo00o + o0oOO0O00o0O
   if IiIiii1IiI > 0 :
    if 61 - 61: OoOo00o % I1ii11iIi11i % Ii11Ii1I
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    if i1iiIIiiI111 . yesno ( "Delete YouTube Music Cache Files" , str ( IiIiii1IiI ) + " files found" , "Do you want to delete them?" ) :
     if 21 - 21: ooOoO0O00 + IIiIiII11i
     for I1iii11 in ii1IIi111 :
      os . unlink ( os . path . join ( i1o0oooO , I1iii11 ) )
     for OoOo00o0OO in i1iI11i1IIi :
      shutil . rmtree ( os . path . join ( i1o0oooO , OoOo00o0OO ) )
      if 24 - 24: Ii + ooOoO0O00 * OOooOOo % o0oOO0O00o0O
   else :
    pass
    if 39 - 39: OOooOOo + IIIi % o0o00Oo0O
    if 26 - 26: O0OoO + OOooOOo
 II111I1i1 = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.supercartoons/cache' ) , '' )
 if os . path . exists ( iiIII1i ) == True :
  for i1o0oooO , i1iI11i1IIi , ii1IIi111 in os . walk ( II111I1i1 ) :
   IiIiii1IiI = 0
   IiIiii1IiI += len ( ii1IIi111 )
   if 10 - 10: o0o00Oo0O . OOooOOo * OooO0OoOOOO / IIIi / ooOoO0O00
   if 32 - 32: o0o00Oo0O / IIIii1II1II . O0OoO % IIIi
   if IiIiii1IiI > 0 :
    if 18 - 18: OooO0OoOOOO * o0oOO0O00o0O / iI1iI1I1i1I / o0o00Oo0O
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    if i1iiIIiiI111 . yesno ( "Delete SuperCartoons Cache Files" , str ( IiIiii1IiI ) + " files found" , "Do you want to delete them?" ) :
     if 11 - 11: iI11I1II1I1I / Ii11Ii1I + ii % ooOoO0O00 * Ii
     for I1iii11 in ii1IIi111 :
      os . unlink ( os . path . join ( i1o0oooO , I1iii11 ) )
     for OoOo00o0OO in i1iI11i1IIi :
      shutil . rmtree ( os . path . join ( i1o0oooO , OoOo00o0OO ) )
      if 86 - 86: Ii - o0o00Oo0O - Ii . iI11I1II1I1I . OooO0OoOOOO
   else :
    pass
    if 84 - 84: ooOoO0O00 / iI11I1II1I1I / OoOo00o / Ii11Ii1I
    if 7 - 7: OOooOOo . IIIii1II1II % I1ii11iIi11i
 o00OO000 = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.tvonline.cc/cache' ) , '' )
 if os . path . exists ( iiIII1i ) == True :
  for i1o0oooO , i1iI11i1IIi , ii1IIi111 in os . walk ( o00OO000 ) :
   IiIiii1IiI = 0
   IiIiii1IiI += len ( ii1IIi111 )
   if 53 - 53: OOooOOo - ooOoO0O00 % Ii1I
   if 37 - 37: oO0o - I1ii11iIi11i
   if IiIiii1IiI > 0 :
    if 38 - 38: Ii / oO0o
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    if i1iiIIiiI111 . yesno ( "Delete TVonline Cache Files" , str ( IiIiii1IiI ) + " files found" , "Do you want to delete them?" ) :
     if 64 - 64: OooO0OoOOOO
     for I1iii11 in ii1IIi111 :
      os . unlink ( os . path . join ( i1o0oooO , I1iii11 ) )
     for OoOo00o0OO in i1iI11i1IIi :
      shutil . rmtree ( os . path . join ( i1o0oooO , OoOo00o0OO ) )
      if 80 - 80: oOo0O0Ooo - Ii / oO0o / OOooOOo + OOooOOo
   else :
    pass
    if 89 - 89: o0o00Oo0O + OooO0OoOOOO * IIIi
    if 30 - 30: OOooOOo
 IIIII11 = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.youtube/kodion' ) , '' )
 if os . path . exists ( iiIII1i ) == True :
  for i1o0oooO , i1iI11i1IIi , ii1IIi111 in os . walk ( IIIII11 ) :
   IiIiii1IiI = 0
   IiIiii1IiI += len ( ii1IIi111 )
   if 48 - 48: IIIi / O0OoO . iI11I1II1I1I
   if 72 - 72: ooOoO0O00 . I11i
   if IiIiii1IiI > 0 :
    if 3 - 3: OOooOOo % IIiIiII11i - o0o00Oo0O
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    if i1iiIIiiI111 . yesno ( "Delete YouTube Cache Files" , str ( IiIiii1IiI ) + " files found" , "Do you want to delete them?" ) :
     if 52 - 52: oO0o
     for I1iii11 in ii1IIi111 :
      os . unlink ( os . path . join ( i1o0oooO , I1iii11 ) )
     for OoOo00o0OO in i1iI11i1IIi :
      shutil . rmtree ( os . path . join ( i1o0oooO , OoOo00o0OO ) )
      if 49 - 49: Ii11Ii1I . Ii1I % O0OoO . I1ii11iIi11i * IIIii1II1II
   else :
    pass
    if 44 - 44: iI11I1II1I1I / o0o00Oo0O * I1ii11iIi11i + oOo0O0Ooo . O0OoO
    if 20 - 20: o0oOO0O00o0O + I11i . IIIi / Ii
    if 7 - 7: OOooOOo / OOooOOo . IIIi * o0o00Oo0O + OooO0OoOOOO + OoOo00o
 OoO00oOO00O00 = xbmc . translatePath ( 'special://masterprofile/addon_data/plugin.video.genesis' )
 i1iiIIiiI111 = xbmcgui . Dialog ( )
 try :
  if i1iiIIiiI111 . yesno ( "Delete Genesis Cache Files" , "Do you want to delete cache" ) :
   oOo0o00oO0o = os . path . join ( OoO00oOO00O00 , "cache.db" )
   os . unlink ( oOo0o00oO0o )
   if 83 - 83: ooOoO0O00 * OOooOOo * o0o00Oo0O . I11i
 except :
  pass
  if 37 - 37: oOo0O0Ooo + ii . IIIi + oOo0O0Ooo . OooO0OoOOOO
 i1iiIIiiI111 = xbmcgui . Dialog ( )
 i1iiIIiiI111 . ok ( "GenieTv" , "                               Finished Deleting Cache " , "                          [COLOR gold]Brought To You By GenieTv[/COLOR]" )
 if 44 - 44: OOooOOo . IIIi . ooOoO0O00 . OOooOOo * O0OoO
 if 59 - 59: IIiIiII11i * ii - ii
 if 33 - 33: o0o00Oo0O . Ii % I11i
 if 50 - 50: O0OoO
 if 81 - 81: Ii * iI11I1II1I1I / I1ii11iIi11i * IIIii1II1II
 if 83 - 83: Ii - oOo0O0Ooo * Ii
 if 59 - 59: o0oOO0O00o0O - ii / O0OoO + Ii1I . I11i - o0oOO0O00o0O
 if 29 - 29: OoOo00o
 if 26 - 26: o0o00Oo0O % IIIii1II1II - OooO0OoOOOO . IIIii1II1II
def OOo0O0 ( url ) :
 print '###' + o0oOoO00o + ' - DELETING PACKAGES###'
 Iiiii = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' , '' ) )
 try :
  for i1o0oooO , i1iI11i1IIi , ii1IIi111 in os . walk ( Iiiii ) :
   IiIiii1IiI = 0
   IiIiii1IiI += len ( ii1IIi111 )
   if 8 - 8: iI11I1II1I1I . iI11I1II1I1I + Ii11Ii1I . IIIii1II1II
   if 58 - 58: iI11I1II1I1I + IIIi - Ii1I - ooOoO0O00 * OOooOOo
   if IiIiii1IiI > 0 :
    if 4 - 4: ii
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    if i1iiIIiiI111 . yesno ( "Delete Package Cache Files" , str ( IiIiii1IiI ) + " files found" , "Do you want to delete them?" ) :
     if 7 - 7: OooO0OoOOOO
     for I1iii11 in ii1IIi111 :
      os . unlink ( os . path . join ( i1o0oooO , I1iii11 ) )
     for OoOo00o0OO in i1iI11i1IIi :
      shutil . rmtree ( os . path . join ( i1o0oooO , OoOo00o0OO ) )
     i1iiIIiiI111 = xbmcgui . Dialog ( )
     i1iiIIiiI111 . ok ( o0oOoO00o , "       Deleting Packages all done" )
    else :
     pass
   else :
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    i1iiIIiiI111 . ok ( o0oOoO00o , "       No Packages to DELETE" )
 except :
  i1iiIIiiI111 = xbmcgui . Dialog ( )
  i1iiIIiiI111 . ok ( o0oOoO00o , "Error Deleting Packages please visit The Support Group, GenieTv on facebook" )
 return
 if 26 - 26: IIIii1II1II + I1ii11iIi11i
 if 71 - 71: oOo0O0Ooo . O0OoO
 if 43 - 43: Ii1I * IIIii1II1II
 if 1 - 1: oO0o * O0OoO + OooO0OoOOOO . OoOo00o / O0OoO
 if 91 - 91: Ii11Ii1I + iI1iI1I1i1I - I1ii11iIi11i % OOooOOo . o0oOO0O00o0O
 if 51 - 51: IIIii1II1II / iI1iI1I1i1I
 if 51 - 51: O0OoO * OoOo00o - IIIi + o0oOO0O00o0O
 if 46 - 46: I11i - Ii % oO0o / Ii11Ii1I - OOooOOo
 if 88 - 88: OoOo00o * oOo0O0Ooo / oO0o - IIIii1II1II / ooOoO0O00 . IIIi
def II1i111 ( url ) :
 print '###' + o0oOoO00o + ' - DELETING PACKAGES###'
 Iiiii = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' , '' ) )
 try :
  for i1o0oooO , i1iI11i1IIi , ii1IIi111 in os . walk ( Iiiii ) :
   IiIiii1IiI = 0
   IiIiii1IiI += len ( ii1IIi111 )
   if 26 - 26: Ii - O0OoO
   if 45 - 45: O0OoO + IIiIiII11i % o0oOO0O00o0O
   if IiIiii1IiI > 0 :
    if 55 - 55: O0OoO - OoOo00o % oOo0O0Ooo
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    if i1iiIIiiI111 . yesno ( "Delete Package Cache Files" , str ( IiIiii1IiI ) + " files found" , "Do you want to delete them?" ) :
     if 61 - 61: O0OoO
     for I1iii11 in ii1IIi111 :
      os . unlink ( os . path . join ( i1o0oooO , I1iii11 ) )
     for OoOo00o0OO in i1iI11i1IIi :
      shutil . rmtree ( os . path . join ( i1o0oooO , OoOo00o0OO ) )
     i1iiIIiiI111 = xbmcgui . Dialog ( )
     i1iiIIiiI111 . ok ( o0oOoO00o , "       Deleting Packages all done" )
    else :
     pass
   else :
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    i1iiIIiiI111 . ok ( o0oOoO00o , "       No Packages to DELETE" )
 except :
  i1iiIIiiI111 = xbmcgui . Dialog ( )
  i1iiIIiiI111 . ok ( o0oOoO00o , "Error Deleting Packages please visit The Support Group, GenieTv on facebook" )
 O0Oo00o0o ( url )
 return
 if 22 - 22: iI11I1II1I1I / O0OoO / oOo0O0Ooo - I11i
 if 21 - 21: OoOo00o . Ii * iI1iI1I1i1I . IIIii1II1II / IIIii1II1II
 if 42 - 42: ii / IIIi . I11i / o0o00Oo0O - OooO0OoOOOO * OooO0OoOOOO
 if 1 - 1: Ii11Ii1I % IIIi
 if 97 - 97: OOooOOo
 if 13 - 13: OOooOOo % IIIii1II1II . o0o00Oo0O / I1ii11iIi11i % I1ii11iIi11i
 if 19 - 19: IIIi % O0OoO - O0OoO % oOo0O0Ooo . IIIii1II1II - ii
 if 100 - 100: oOo0O0Ooo + Ii11Ii1I + I11i . ooOoO0O00 % ii
 if 64 - 64: o0o00Oo0O % ooOoO0O00 * IIIi - Ii11Ii1I + I1ii11iIi11i
 if 65 - 65: OOooOOo . Ii
def III111i1IIiiI ( url , name ) :
 ii11I1 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 OOo0oo = os . path . join ( ii11I1 , 'advancedsettings.xml' )
 i1iiIIiiI111 = xbmcgui . Dialog ( )
 ooo0ooOoOOoO = os . path . join ( ii11I1 , 'advancedsettings.xml.bak' )
 if os . path . exists ( ooo0ooOoOOoO ) == False :
  if i1iiIIiiI111 . yesno ( "Back Up Original" , 'Have You Backed Up Your Original?' , '' , "[B][COLOR red]     AS YOU CANNOT GO BACK !!![/B][/COLOR]" ) :
   print '###' + o0oOoO00o + ' - ADVANCED XML###'
   ii11I1 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
   OOo0oo = os . path . join ( ii11I1 , 'advancedsettings.xml' )
   try :
    os . remove ( OOo0oo )
    print '=== GenieTv - REMOVING    ' + str ( OOo0oo ) + '    ==='
   except :
    pass
   O000oo0O = i1 . http_GET ( url ) . content
   ooo0OiII1iii = open ( OOo0oo , "w" )
   ooo0OiII1iii . write ( O000oo0O )
   ooo0OiII1iii . close ( )
   print '=== GenieTv - WRITING NEW    ' + str ( OOo0oo ) + '    ==='
   i1iiIIiiI111 = xbmcgui . Dialog ( )
   i1iiIIiiI111 . ok ( o0oOoO00o , "       Done Adding new Advanced XML" )
 else :
  print '###' + o0oOoO00o + ' - ADVANCED XML###'
  ii11I1 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
  OOo0oo = os . path . join ( ii11I1 , 'advancedsettings.xml' )
  try :
   os . remove ( OOo0oo )
   print '=== GenieTv - REMOVING    ' + str ( OOo0oo ) + '    ==='
  except :
   pass
  O000oo0O = i1 . http_GET ( url ) . content
  ooo0OiII1iii = open ( OOo0oo , "w" )
  ooo0OiII1iii . write ( O000oo0O )
  ooo0OiII1iii . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( OOo0oo ) + '    ==='
  i1iiIIiiI111 = xbmcgui . Dialog ( )
  i1iiIIiiI111 . ok ( o0oOoO00o , "       Done Adding new Advanced XML" )
 return
 if 8 - 8: Ii / O0OoO
def I1I1IiiI1ii1 ( url , name ) :
 print '###' + o0oOoO00o + ' - CHECK ADVANCE XML###'
 ii11I1 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 OOo0oo = os . path . join ( ii11I1 , 'advancedsettings.xml' )
 try :
  ooo0OiII1iii = open ( OOo0oo ) . read ( )
  if 'zero' in ooo0OiII1iii :
   name = '0CACHE'
  elif 'tuxen' in ooo0OiII1iii :
   name = 'TUXENS'
  elif 'muckys' in ooo0OiII1iii :
   name = 'MUCKYS'
  elif 'p2p1' in ooo0OiII1iii :
   name = '1st P2P RECOMMENDED'
  elif 'p2p2' in ooo0OiII1iii :
   name = '2nd P2P RECOMMENDED'
  elif 'mikey' in ooo0OiII1iii :
   name = 'MIKEY1234'
 except :
  name = "NO ADVANCED"
 i1iiIIiiI111 = xbmcgui . Dialog ( )
 i1iiIIiiI111 . ok ( o0oOoO00o , "[COLOR yellow]YOU HAVE[/COLOR] " + name + "[COLOR yellow] XML SETTINGS SETUP[/COLOR]" )
 return
 if 24 - 24: Ii1I * I11i
def OO0oOo00 ( url ) :
 print '###' + o0oOoO00o + ' - DELETING ADVANCE XML###'
 ii11I1 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 OOo0oo = os . path . join ( ii11I1 , 'advancedsettings.xml' )
 try :
  os . remove ( OOo0oo )
  i1iiIIiiI111 = xbmcgui . Dialog ( )
  print '=== GenieTv - DELETING    ' + str ( OOo0oo ) + '    ==='
  i1iiIIiiI111 . ok ( o0oOoO00o , "       Remove Advanced Settings Sucessfull" )
 except :
  i1iiIIiiI111 = xbmcgui . Dialog ( )
  i1iiIIiiI111 . ok ( o0oOoO00o , "       No Advanced Settings To Remove" )
 return
 if 5 - 5: IIIii1II1II + o0o00Oo0O / IIIi . iI11I1II1I1I - OOooOOo + I1ii11iIi11i
 if 55 - 55: Ii1I - Ii11Ii1I
 if 9 - 9: Ii1I - OooO0OoOOOO
 if 64 - 64: ooOoO0O00
 if 71 - 71: OooO0OoOOOO * I11i
 if 99 - 99: I11i
 if 28 - 28: ii % o0o00Oo0O - IIIii1II1II / I11i / oOo0O0Ooo
 if 41 - 41: IIiIiII11i * OooO0OoOOOO / oO0o . OoOo00o
 if 50 - 50: ii + iI11I1II1I1I / OoOo00o / IIIii1II1II . Ii . O0OoO
 if 75 - 75: iI11I1II1I1I % O0OoO / IIIii1II1II - o0oOO0O00o0O % Ii
def i11oO0OoO ( url = 'http://www.iplocation.net/' , inc = 1 ) :
 Ii1i = re . compile ( "<td width='80'>(.+?)</td><td>(.+?)</td><td>(.+?)</td><td>.+?</td><td>(.+?)</td>" ) . findall ( i1 . http_GET ( url ) . content )
 for i1II1IiIi111 , oooI1iIiii , OoOOo0OO0OOoo , i1I in Ii1i :
  if inc < 2 : i1iiIIiiI111 = xbmcgui . Dialog ( ) ; i1iiIIiiI111 . ok ( 'Check My IP' , "[B][COLOR gold]Your IP Address is: [/COLOR][/B] %s" % i1II1IiIi111 , '[B][COLOR gold]Your IP is based in: [/COLOR][/B] %s' % OoOOo0OO0OOoo , '[B][COLOR gold]Your Service Provider is:[/COLOR][/B] %s' % i1I )
  inc = inc + 1
  if 32 - 32: O0OoO . OooO0OoOOOO . IIiIiII11i
  if 25 - 25: OooO0OoOOOO * IIIi - OoOo00o * Ii * oOo0O0Ooo * IIIii1II1II
  if 56 - 56: ii . oOo0O0Ooo . IIiIiII11i % o0oOO0O00o0O
  if 59 - 59: O0OoO % I1ii11iIi11i - OoOo00o + OooO0OoOOOO
  if 33 - 33: Ii11Ii1I + OOooOOo - Ii1I + iI11I1II1I1I % ooOoO0O00 * OooO0OoOOOO
  if 21 - 21: o0o00Oo0O * O0OoO % oO0o
  if 14 - 14: o0o00Oo0O / IIIi / O0OoO + OooO0OoOOOO - OooO0OoOOOO
  if 10 - 10: o0o00Oo0O - Ii1I / IIIi % OOooOOo / ii / Ii11Ii1I
  if 73 - 73: O0OoO + OooO0OoOOOO % I11i . Ii1I / IIIii1II1II . IIIi
def O00O0oo ( url , name ) :
 i1iiIIiiI111 = xbmcgui . Dialog ( )
 if i1iiIIiiI111 . yesno ( "GenieTv" , '                                    Install Latest .ini File' ) :
  print '###' + o0oOoO00o + ' - CUSTOM FTV INI###'
  ii11I1 = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/plugin.video.GenieTv' , '' ) )
  OOo0oo = os . path . join ( ii11I1 , 'addons2.ini' )
  O000oo0O = i1 . http_GET ( url ) . content
  ooo0OiII1iii = open ( OOo0oo , "w" )
  ooo0OiII1iii . write ( O000oo0O )
  ooo0OiII1iii . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( OOo0oo ) + '    ==='
  i1iiIIiiI111 = xbmcgui . Dialog ( )
  i1iiIIiiI111 . ok ( o0oOoO00o , "                               Done Adding New .ini File" )
 return
 if 18 - 18: IIiIiII11i / oO0o . Ii - iI1iI1I1i1I % I1ii11iIi11i
def OO00oOooo0Oo ( url , name ) :
 i1iiIIiiI111 = xbmcgui . Dialog ( )
 if i1iiIIiiI111 . yesno ( "GenieTv" , '                               Install Custom Settings' ) :
  print '###' + o0oOoO00o + ' - CUSTOM FTV SETTINGS###'
  ii11I1 = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/plugin.video.GenieTv' , '' ) )
  OOo0oo = os . path . join ( ii11I1 , 'settings.xml' )
  O000oo0O = i1 . http_GET ( url ) . content
  ooo0OiII1iii = open ( OOo0oo , "w" )
  ooo0OiII1iii . write ( O000oo0O )
  ooo0OiII1iii . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( OOo0oo ) + '    ==='
  i1iiIIiiI111 = xbmcgui . Dialog ( )
  i1iiIIiiI111 . ok ( o0oOoO00o , "                               Done Adding New Settings" )
 return
 if 16 - 16: oO0o
 if 44 - 44: iI1iI1I1i1I . OooO0OoOOOO % IIIi - O0OoO - Ii1I
def iIIiIi1IiI1 ( ) :
 try :
  Oo0O = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/plugin.video.GenieTv' , '' ) )
  if os . path . exists ( Oo0O ) == True :
   i1iiIIiiI111 = xbmcgui . Dialog ( )
   if i1iiIIiiI111 . yesno ( "GenieTv" , "                               Delete FTV Guide Database" ) :
    Iii1I1III11 = os . path . join ( Oo0O , "source.db" )
    os . unlink ( Iii1I1III11 )
  i1iiIIiiI111 . ok ( "GenieTv" , "                                     FTV Database Reset" )
 except :
  i1iiIIiiI111 = xbmcgui . Dialog ( )
  i1iiIIiiI111 . ok ( o0oOoO00o , "               Error Deleting Database No Database To Delete" )
 return
 if 6 - 6: Ii11Ii1I * ooOoO0O00
 if 6 - 6: o0o00Oo0O - o0o00Oo0O - o0o00Oo0O - I11i / Ii % OOooOOo
 if 84 - 84: Ii11Ii1I
 if 70 - 70: iI11I1II1I1I
 if 45 - 45: o0o00Oo0O - OOooOOo % IIIii1II1II
def iiI111I1iIiI ( url ) :
 I11iii1Ii = urllib2 . Request ( url )
 I11iii1Ii . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
 I1IIiiIiii = urllib2 . urlopen ( I11iii1Ii )
 O000oo0O = I1IIiiIiii . read ( )
 I1IIiiIiii . close ( )
 return O000oo0O
 if 100 - 100: Ii . IIIii1II1II . Ii
 if 81 - 81: oOo0O0Ooo
 if 76 - 76: o0o00Oo0O - O0OoO / Ii11Ii1I . I1ii11iIi11i - Ii11Ii1I
 if 75 - 75: O0OoO % IIIii1II1II / I11i % IIiIiII11i
 if 30 - 30: I11i
 if 15 - 15: IIiIiII11i - Ii11Ii1I - o0oOO0O00o0O . OoOo00o / Ii
 if 38 - 38: oO0o
def IiiIIIII ( params ) :
 plugintools . log ( "freshstart.main_list " + repr ( params ) ) ; iiiII = plugintools . message_yes_no ( o0oOoO00o , "Do you wish to restore your" , "Kodi configuration to default settings?" )
 if iiiII :
  Oo0Ooo = xbmcaddon . Addon ( id = o00 ) . getAddonInfo ( 'path' ) ; Oo0Ooo = xbmc . translatePath ( Oo0Ooo ) ;
  II1iII11 = os . path . join ( Oo0Ooo , ".." , ".." ) ; II1iII11 = os . path . abspath ( II1iII11 ) ; plugintools . log ( "freshstart.main_list xbmcPath=" + II1iII11 ) ; iiiI1IiIi1i1I = False
  try :
   for i1o0oooO , i1iI11i1IIi , ii1IIi111 in os . walk ( II1iII11 , topdown = True ) :
    i1iI11i1IIi [ : ] = [ OoOo00o0OO for OoOo00o0OO in i1iI11i1IIi if OoOo00o0OO not in iiIIIII1i1iI ]
    for iiI1IIIi in ii1IIi111 :
     try : os . remove ( os . path . join ( i1o0oooO , iiI1IIIi ) )
     except :
      if iiI1IIIi not in [ "Addons15.db" , "MyVideos75.db" , "Textures13.db" , "xbmc.log" ] : iiiI1IiIi1i1I = True
      plugintools . log ( "Error removing " + i1o0oooO + " " + iiI1IIIi )
    for iiI1IIIi in i1iI11i1IIi :
     try : os . rmdir ( os . path . join ( i1o0oooO , iiI1IIIi ) )
     except :
      if iiI1IIIi not in [ "Database" , "userdata" ] : iiiI1IiIi1i1I = True
      plugintools . log ( "Error removing " + i1o0oooO + " " + iiI1IIIi )
   if not iiiI1IiIi1i1I : plugintools . log ( "freshstart.main_list All user files removed, you now have a clean install" ) ; plugintools . message ( o0oOoO00o , "The process is complete, you're now back to a fresh Kodi configuration with GenieTv!" , "Please reboot your system or restart Kodi in order for the changes to be applied." )
   else : plugintools . log ( "freshstart.main_list User files partially removed" ) ; plugintools . message ( o0oOoO00o , "The process is complete, you're now back to a fresh Kodi configuration with GenieTv" , "Please reboot your system or restart Kodi in order for the changes to be applied." )
  except : plugintools . message ( o0oOoO00o , "Problem found" , "Your settings has not been changed" ) ; import traceback ; plugintools . log ( traceback . format_exc ( ) ) ; plugintools . log ( "freshstart.main_list NOT removed" )
  plugintools . add_item ( action = "" , title = "Now Exit Kodi" , folder = False )
 else : plugintools . message ( o0oOoO00o , "Your settings" , "has not been changed" ) ; plugintools . add_item ( action = "" , title = "Done" , folder = False )
 i1iiiIii11 ( )
 if 94 - 94: Ii11Ii1I + o0o00Oo0O - ii / o0o00Oo0O
 if 70 - 70: ii / IIIii1II1II - oO0o % ii
 if 25 - 25: I1ii11iIi11i % I11i % ooOoO0O00
def I1oOO000oOo0O0o ( ) :
 OoiiI1I = [ ]
 OOOOo0o0O0 = sys . argv [ 2 ]
 if len ( OOOOo0o0O0 ) >= 2 :
  I1I1i1 = sys . argv [ 2 ]
  Ii1Ii = I1I1i1 . replace ( '?' , '' )
  if ( I1I1i1 [ len ( I1I1i1 ) - 1 ] == '/' ) :
   I1I1i1 = I1I1i1 [ 0 : len ( I1I1i1 ) - 2 ]
  iII = Ii1Ii . split ( '&' )
  OoiiI1I = { }
  for o0o00o0Oo in range ( len ( iII ) ) :
   OOoOOooO = { }
   OOoOOooO = iII [ o0o00o0Oo ] . split ( '=' )
   if ( len ( OOoOOooO ) ) == 2 :
    OoiiI1I [ OOoOOooO [ 0 ] ] = OOoOOooO [ 1 ]
    if 33 - 33: OooO0OoOOOO * iI1iI1I1i1I
 return OoiiI1I
 if 96 - 96: I11i - oOo0O0Ooo % OOooOOo + oO0o - OooO0OoOOOO - OooO0OoOOOO
i1ii1iiI1iI = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkbw==' )
o0OO0O0Oo = base64 . decodestring ( 'L3N0b3JhZ2UvZW11bGF0ZWQvMA==' )
Ii1i1 = base64 . decodestring ( 'L2dlbmllLnR4dA==' )
iiI1iiiii = base64 . decodestring ( 'LmFyY2hpdGVjdHMueDEwaG9zdC5jb20vdGVzdC93aC50eHQ=' )
I11I = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby9maXhlcy9maXhlcy50eHQ=' )
OOoOO = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby9hcHBzL2FwcHMueG1s' )
iIi1i1II = base64 . decodestring ( 'L2FkZG9ucy9uZXcudHh0' )
OOo00OOoOOO = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby92b2Qvdm9kLnBocA==' )
OOOoOO00OO0 = base64 . decodestring ( 'L2FkZG9ucy9pcHR2LnR4dA==' )
o0OOOoO = base64 . decodestring ( 'L2FkZG9ucy92aWRlby50eHQ=' )
o0OooOoOOoO = base64 . decodestring ( 'L2FkZG9ucy9zcG9ydHMudHh0' )
Oo0I1iii = base64 . decodestring ( 'L2FkZG9ucy9raWRzLnR4dA==' )
I11IiI1iII = base64 . decodestring ( 'L2FkZG9ucy9tdXNpYy50eHQ=' )
iIi11 = base64 . decodestring ( 'L2FkZG9ucy9wcm9ncmFtcy50eHQ=' )
i1IiIi1I1i = base64 . decodestring ( 'L2FkZG9ucy94eHgudHh0' )
o0ooOo000oo = base64 . decodestring ( 'L2FkZG9ucy9yZXBvLnR4dA==' )
iI111i1I1II = base64 . decodestring ( 'L2FkZG9ucy9wYWNrcy50eHQ=' )
I1iII11I1I = base64 . decodestring ( 'L2FkZG9ucy9za2lucy50eHQ=' )
ooo0oooo0 = base64 . decodestring ( 'L2FkZG9ucy9hcnQudHh0' )
OO0oOOo = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2dvdGhhbS50eHQ=' )
OOoOoO00O0O0o = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2hlbGl4LnR4dA==' )
oo0o0000Oo0 = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2lzZW5nYXJkLnR4dA==' )
Ii1Iii1 = base64 . decodestring ( 'L2FkZG9ucy9SU1MudHh0' )
OOO = base64 . decodestring ( 'Q1VOVA==' )
def II1I ( name , url , mode , iconimage , fanart , description , showcontext = True , allinfo = { } ) :
 oooo = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 iiiIIIii = True
 ooOoo00 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 ooOoo00 . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 ooOoo00 . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  iiI1 = [ ]
  if showcontext == 'fav' :
   iiI1 . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in OOO00 :
   iiI1 . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fanart=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , urllib . quote_plus ( fanart ) , mode ) ) )
  ooOoo00 . addContextMenuItems ( iiI1 )
 iiiIIIii = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = oooo , listitem = ooOoo00 , isFolder = True )
 return iiiIIIii
 if 50 - 50: Ii11Ii1I + IIIii1II1II . iI11I1II1I1I
def ooOOoooooo ( name , url , mode , iconimage , fanart , description ) :
 oooo = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 iiiIIIii = True
 ooOoo00 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 ooOoo00 . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 ooOoo00 . setProperty ( "Fanart_Image" , fanart )
 iiiIIIii = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = oooo , listitem = ooOoo00 , isFolder = False )
 return iiiIIIii
 if 13 - 13: Ii . O0OoO / ooOoO0O00 - OooO0OoOOOO + o0o00Oo0O
 if 88 - 88: ii
I1I1i1 = I1oOO000oOo0O0o ( )
OooOoOo = None
iiI1IIIi = None
IiI1I1I = None
OOOOO0O00 = None
Iii = None
iIIIII1I = None
iiii1I1IiI = None
if 49 - 49: Ii1I + OoOo00o * o0oOO0O00o0O * O0OoO / oOo0O0Ooo . Ii1I
if 80 - 80: oOo0O0Ooo % OooO0OoOOOO / iI1iI1I1i1I * oO0o - OoOo00o / OoOo00o
try :
 iiii1I1IiI = int ( I1I1i1 [ "fav_mode" ] )
except :
 pass
 if 13 - 13: I1ii11iIi11i
try :
 OooOoOo = urllib . unquote_plus ( I1I1i1 [ "url" ] )
except :
 pass
try :
 iiI1IIIi = urllib . unquote_plus ( I1I1i1 [ "name" ] )
except :
 pass
try :
 OOOOO0O00 = urllib . unquote_plus ( I1I1i1 [ "iconimage" ] )
except :
 pass
try :
 IiI1I1I = int ( I1I1i1 [ "mode" ] )
except :
 pass
try :
 Iii = urllib . unquote_plus ( I1I1i1 [ "fanart" ] )
except :
 pass
try :
 iIIIII1I = urllib . unquote_plus ( I1I1i1 [ "description" ] )
except :
 pass
 if 70 - 70: o0oOO0O00o0O
 if 51 - 51: o0o00Oo0O - Ii1I / iI1iI1I1i1I * IIiIiII11i + oO0o % Ii1I
print str ( oOOoO0 ) + ': ' + str ( IiiIII111iI )
print "Mode: " + str ( IiI1I1I )
print "URL: " + str ( OooOoOo )
print "Name: " + str ( iiI1IIIi )
print "IconImage: " + str ( OOOOO0O00 )
if 58 - 58: OoOo00o + OooO0OoOOOO % o0oOO0O00o0O - Ii11Ii1I - IIIii1II1II % Ii11Ii1I
if 86 - 86: I11i
def iiIiI ( content , viewType ) :
 if 15 - 15: OoOo00o - iI11I1II1I1I - IIiIiII11i - OooO0OoOOOO % Ii1I
 if content :
  xbmcplugin . setContent ( int ( sys . argv [ 1 ] ) , content )
 if o0oO0 . getSetting ( 'auto-view' ) == 'true' :
  xbmc . executebuiltin ( "Container.SetViewMode(%s)" % o0oO0 . getSetting ( viewType ) )
  if 80 - 80: OooO0OoOOOO * o0oOO0O00o0O . ooOoO0O00 % Ii11Ii1I % Ii1I + O0OoO
if OOOOO0O00 == None : OOOOO0O00 = i1iIIi1
if Iii == None : Iii = i1iiIII111ii
if IiI1I1I == None :
 ooOOO00Ooo ( )
 if 6 - 6: Ii1I . OoOo00o . oO0o + OooO0OoOOOO
elif IiI1I1I == 1 :
 oOooO00o0O ( OooOoOo )
 if 65 - 65: Ii1I / O0OoO
elif IiI1I1I == 44 :
 iIi1IiI ( OooOoOo )
 if 23 - 23: IIIii1II1II / IIIii1II1II * I11i * IIIii1II1II
elif IiI1I1I == 2 :
 OoOO ( )
 if 57 - 57: o0oOO0O00o0O
elif IiI1I1I == 3 :
 O0iIi1IiII ( )
 if 29 - 29: oOo0O0Ooo
elif IiI1I1I == 21 :
 iI1Ii11111iIi ( )
 if 41 - 41: IIIi * oO0o - o0oOO0O00o0O . Ii11Ii1I
elif IiI1I1I == 4 :
 ii1i1i1IiII ( )
 if 41 - 41: iI11I1II1I1I - o0o00Oo0O - Ii1I - OoOo00o + IIIi
elif IiI1I1I == 5 :
 I1i1iii1Ii ( OooOoOo )
 if 22 - 22: o0o00Oo0O % OooO0OoOOOO % o0oOO0O00o0O % oOo0O0Ooo
elif IiI1I1I == 6 :
 OOo0O0 ( OooOoOo )
 if 34 - 34: o0oOO0O00o0O . I1ii11iIi11i % Ii1I . o0oOO0O00o0O % OooO0OoOOOO / OooO0OoOOOO
elif IiI1I1I == 7 :
 III111i1IIiiI ( OooOoOo , iiI1IIIi )
 if 84 - 84: Ii11Ii1I
elif IiI1I1I == 8 :
 I1I1IiiI1ii1 ( OooOoOo , iiI1IIIi )
 if 1 - 1: OoOo00o - I1ii11iIi11i * iI11I1II1I1I * I1ii11iIi11i * ooOoO0O00
elif IiI1I1I == 9 :
 FIXREPOSADDONS ( OooOoOo )
 if 9 - 9: o0oOO0O00o0O - o0oOO0O00o0O
elif IiI1I1I == 10 :
 oO00oooOOoOo0 ( )
 if 3 - 3: o0o00Oo0O + o0o00Oo0O - o0o00Oo0O - o0o00Oo0O % ii + OoOo00o
elif IiI1I1I == 11 :
 OO0oOo00 ( OooOoOo )
 if 20 - 20: oO0o + iI1iI1I1i1I . IIiIiII11i / Ii
elif IiI1I1I == 12 :
 i11oO0OoO ( )
 if 50 - 50: ii / oO0o % iI11I1II1I1I
elif IiI1I1I == 13 :
 iIiii1IIi1I ( )
 if 41 - 41: Ii1I % Ii1I + OooO0OoOOOO . o0oOO0O00o0O % IIIi * O0OoO
elif IiI1I1I == 14 :
 O0Oo00o0o ( OooOoOo )
 if 57 - 57: Ii11Ii1I . IIIi . IIiIiII11i % ii * o0o00Oo0O + iI11I1II1I1I
elif IiI1I1I == 15 :
 iiI1II11II1i ( )
 if 94 - 94: ooOoO0O00 * oO0o * OOooOOo
elif IiI1I1I == 16 :
 O00O0oo ( OooOoOo , iiI1IIIi )
 if 93 - 93: O0OoO / IIIii1II1II * o0o00Oo0O
elif IiI1I1I == 17 :
 OO00oOooo0Oo ( OooOoOo , iiI1IIIi )
 if 17 - 17: oO0o / O0OoO % oOo0O0Ooo
elif IiI1I1I == 18 :
 iIIiIi1IiI1 ( )
 if 47 - 47: I1ii11iIi11i * oO0o / I11i * oOo0O0Ooo
elif IiI1I1I == 19 :
 ii1I ( OooOoOo )
 if 60 - 60: Ii1I / OooO0OoOOOO . Ii / oO0o % IIiIiII11i
elif IiI1I1I == 40 :
 IIIIiii ( iiI1IIIi , OooOoOo , iIIIII1I )
 if 6 - 6: o0oOO0O00o0O % I11i + IIIi
elif IiI1I1I == 42 :
 oooo00 ( iiI1IIIi , OooOoOo , iIIIII1I )
 if 91 - 91: I11i + o0o00Oo0O * OoOo00o * OooO0OoOOOO * Ii1I
elif IiI1I1I == 43 :
 oOOo00O0OOOo ( OooOoOo )
 if 83 - 83: ii
elif IiI1I1I == 20 :
 oOO ( OooOoOo )
 if 52 - 52: I11i / OOooOOo % OoOo00o % oO0o / OooO0OoOOOO % I11i
elif IiI1I1I == 22 :
 iII1 ( OooOoOo )
 if 88 - 88: IIIii1II1II / Ii / Ii11Ii1I / Ii * Ii1I % iI1iI1I1i1I
elif IiI1I1I == 23 :
 iI11ii ( OooOoOo )
 if 43 - 43: OOooOOo * oO0o % ooOoO0O00 * Ii11Ii1I + iI11I1II1I1I
elif IiI1I1I == 24 :
 o0OoO0O ( OooOoOo )
 if 80 - 80: I11i . o0oOO0O00o0O . ii
elif IiI1I1I == 25 :
 O0O0OOooo ( OooOoOo )
 if 63 - 63: O0OoO . IIIii1II1II
elif IiI1I1I == 26 :
 III1I1I11 ( OooOoOo )
 if 66 - 66: oOo0O0Ooo
elif IiI1I1I == 27 :
 i1iIIIiI ( OooOoOo )
 if 99 - 99: oO0o % o0o00Oo0O . IIIi - Ii1I . I1ii11iIi11i / OOooOOo
elif IiI1I1I == 28 :
 Oo000O000 ( OooOoOo )
 if 60 - 60: Ii1I
elif IiI1I1I == 29 :
 i1I1iiiI ( OooOoOo )
 if 78 - 78: OoOo00o + IIiIiII11i
elif IiI1I1I == 30 :
 IIiiii ( OooOoOo )
 if 55 - 55: ii
elif IiI1I1I == 31 :
 Oo00oOo ( OooOoOo )
 if 90 - 90: oOo0O0Ooo
elif IiI1I1I == 32 :
 i1I1IiI ( )
 if 4 - 4: IIIii1II1II % O0OoO - IIIii1II1II - I11i
elif IiI1I1I == 33 :
 Ii1iI11iI1 ( )
 if 30 - 30: OooO0OoOOOO
elif IiI1I1I == 35 :
 iII1Iii1I11i ( OooOoOo )
 if 34 - 34: OoOo00o - IIiIiII11i - I11i + o0oOO0O00o0O + IIIi
elif IiI1I1I == 34 :
 oOOO ( OooOoOo )
 if 70 - 70: ii + oO0o * I1ii11iIi11i
elif IiI1I1I == 36 :
 OOoo00oO00 ( OooOoOo )
 if 20 - 20: Ii - IIiIiII11i - O0OoO % OoOo00o . O0OoO
elif IiI1I1I == 37 :
 I1i11IiI11i1 ( OooOoOo )
 if 50 - 50: iI11I1II1I1I + IIIi - iI1iI1I1i1I - ii
elif IiI1I1I == 38 :
 o0Ooo0o0ooo0 ( OooOoOo )
 if 84 - 84: OOooOOo - iI1iI1I1i1I
elif IiI1I1I == 41 :
 IiiIIIII ( I1I1i1 )
 if 80 - 80: Ii % IIIii1II1II - I1ii11iIi11i % IIIii1II1II
elif IiI1I1I == 39 :
 o0ooo ( OooOoOo )
 if 89 - 89: Ii11Ii1I * iI1iI1I1i1I + OOooOOo / Ii
elif IiI1I1I == 45 :
 TEXTS ( )
 if 68 - 68: ii * iI1iI1I1i1I
elif IiI1I1I == 46 :
 ii1II1 ( )
 if 86 - 86: I11i / OOooOOo
elif IiI1I1I == 47 :
 GEVID ( )
 if 40 - 40: o0oOO0O00o0O
elif IiI1I1I == 48 :
 ooOOOOo0 ( iiI1IIIi , OooOoOo , iIIIII1I )
 if 62 - 62: O0OoO / IIIii1II1II
elif IiI1I1I == 49 :
 I1i11iIIi11 ( )
 if 74 - 74: o0oOO0O00o0O % IIIi / IIIi - iI11I1II1I1I - IIiIiII11i + IIIii1II1II
elif IiI1I1I == 222 :
 o0OOo0o0O0O ( OooOoOo )
 if 92 - 92: iI1iI1I1i1I % IIIi
elif IiI1I1I == 333 :
 II1II1III1 ( OooOoOo )
 if 18 - 18: O0OoO + IIIi / IIIii1II1II / OoOo00o + iI11I1II1I1I % OooO0OoOOOO
 if 94 - 94: iI1iI1I1i1I
elif IiI1I1I == 1020 :
 OOoOO0 ( )
 if 37 - 37: OoOo00o
elif IiI1I1I == 1021 :
 ANIMEEP ( )
 if 52 - 52: Ii1I * oOo0O0Ooo . IIIii1II1II + ooOoO0O00 % OoOo00o / iI11I1II1I1I
elif IiI1I1I == 1022 :
 ANIMEPLAY ( OooOoOo )
 if 68 - 68: IIIi - OOooOOo . Ii + I11i
elif IiI1I1I == 1001 :
 iIIi1I1Ii1 ( )
 if 71 - 71: Ii / ooOoO0O00 * oOo0O0Ooo / OOooOOo
elif IiI1I1I == 1005 :
 Oo00O00o0 ( )
 if 33 - 33: iI1iI1I1i1I . I1ii11iIi11i
elif IiI1I1I == 1007 :
 IiII1 ( OooOoOo )
 if 89 - 89: o0oOO0O00o0O + ooOoO0O00 - OooO0OoOOOO + O0OoO . IIiIiII11i
elif IiI1I1I == 1010 :
 I1Iii ( OooOoOo )
 if 85 - 85: iI11I1II1I1I - Ii11Ii1I * I1ii11iIi11i . OoOo00o + IIIi
elif IiI1I1I == 1011 :
 OO00O00o0O ( OooOoOo )
 if 13 - 13: o0o00Oo0O + iI11I1II1I1I % IIiIiII11i + iI11I1II1I1I
elif IiI1I1I == 1012 :
 ooo0o00o ( OooOoOo )
 if 85 - 85: oOo0O0Ooo * iI11I1II1I1I . o0oOO0O00o0O / o0oOO0O00o0O
elif IiI1I1I == 1030 :
 OOoO00OoOOO ( )
 if 43 - 43: oOo0O0Ooo
elif IiI1I1I == 1031 :
 OoOo0oo ( OooOoOo , OOOOO0O00 )
 if 78 - 78: oO0o % IIiIiII11i + OOooOOo / oOo0O0Ooo
elif IiI1I1I == 1032 :
 III11i1iiiI ( OooOoOo )
 if 34 - 34: I11i % Ii1I + Ii11Ii1I * iI1iI1I1i1I / OoOo00o
elif IiI1I1I == 1006 :
 Parse . ParseURL ( OooOoOo )
 if 18 - 18: O0OoO
elif IiI1I1I == 2030 :
 Parse . addonParseURL ( OooOoOo )
 if 92 - 92: oO0o % iI11I1II1I1I / OooO0OoOOOO * o0oOO0O00o0O . ooOoO0O00 + OoOo00o
elif IiI1I1I == 2031 :
 Parse . apkParseURL ( OooOoOo )
 if 24 - 24: OooO0OoOOOO . o0oOO0O00o0O * OooO0OoOOOO % Ii . Ii + ooOoO0O00
elif IiI1I1I == 1002 :
 I1I1i ( OooOoOo )
 if 64 - 64: iI11I1II1I1I / OooO0OoOOOO / I1ii11iIi11i - Ii1I
elif IiI1I1I == 1003 :
 i111i1IIi1i ( OooOoOo , OOOOO0O00 )
 if 100 - 100: OooO0OoOOOO + ooOoO0O00 * oO0o
elif IiI1I1I == 1004 :
 oo00oO00oooo ( OooOoOo )
 if 64 - 64: OoOo00o * Ii . I1ii11iIi11i
elif IiI1I1I == 1008 :
 oO0000O0Oo00O ( )
 if 52 - 52: I1ii11iIi11i / O0OoO / o0oOO0O00o0O - I11i / o0oOO0O00o0O
elif IiI1I1I == 1009 :
 iiI111iIi1 ( OooOoOo )
 if 74 - 74: ooOoO0O00 . iI11I1II1I1I
elif IiI1I1I == 2001 :
 IiOOo0 ( )
 if 85 - 85: oOo0O0Ooo
elif IiI1I1I == 2002 :
 oooOOOoO0O ( OooOoOo )
 if 10 - 10: o0o00Oo0O . IIiIiII11i / ii
elif IiI1I1I == 1013 :
 o0OoO00 ( )
elif IiI1I1I == 10111113 :
 IIIIIiII1 ( OooOoOo )
 if 72 - 72: ii . I11i + o0o00Oo0O
elif IiI1I1I == 1014 :
 ii1IIiI1iI1i ( )
 if 46 - 46: OOooOOo * iI1iI1I1i1I / OoOo00o + I1ii11iIi11i + OooO0OoOOOO
elif IiI1I1I == 1015 :
 IIiII11 ( OooOoOo )
 if 95 - 95: I11i - Ii11Ii1I
elif IiI1I1I == 1016 :
 o0oOOO ( OooOoOo , OOOOO0O00 , iiI1IIIi )
 if 67 - 67: Ii1I * I1ii11iIi11i % I11i
elif IiI1I1I == 1017 :
 IiI1i ( )
 if 19 - 19: OOooOOo . IIIii1II1II . ii
elif IiI1I1I == 1023 :
 I1iii ( )
 if 79 - 79: IIIii1II1II * O0OoO * oOo0O0Ooo * Ii1I / Ii1I
elif IiI1I1I == 1024 :
 oOO0O00o0O0 ( OooOoOo )
 if 62 - 62: O0OoO * Ii11Ii1I % Ii1I - ooOoO0O00 - Ii1I
elif IiI1I1I == 1025 :
 ooOooO ( OooOoOo )
 if 24 - 24: IIIii1II1II
elif IiI1I1I == 4001 :
 IIi1I11I1II ( )
 if 71 - 71: OooO0OoOOOO - ooOoO0O00
elif IiI1I1I == 4002 :
 o0OOOO00O0Oo ( )
 if 56 - 56: OOooOOo + OoOo00o
elif IiI1I1I == 4003 :
 O0Oo00 ( )
 if 74 - 74: o0oOO0O00o0O / IIIi / IIiIiII11i - o0oOO0O00o0O / OoOo00o % iI1iI1I1i1I
elif IiI1I1I == 4004 :
 OO ( )
 if 19 - 19: OooO0OoOOOO % ii + ii
elif IiI1I1I == 4005 :
 I11iiI1i1 ( )
 if 7 - 7: ooOoO0O00
elif IiI1I1I == 4006 :
 oOo0O0o00o ( )
 if 91 - 91: OOooOOo - OOooOOo . OooO0OoOOOO
elif IiI1I1I == 4007 :
 IiIiI1111I1I ( )
 if 33 - 33: IIIi - iI11I1II1I1I / Ii11Ii1I % o0o00Oo0O
elif IiI1I1I == 4008 :
 i1ioOOoo00O00o ( )
 if 80 - 80: OooO0OoOOOO % ii - OooO0OoOOOO
elif IiI1I1I == 4009 : iIiIIi1 ( )
elif IiI1I1I == 4010 : iiIi1iI1iIii ( )
elif IiI1I1I == 3000 :
 iiI11111II ( )
 if 27 - 27: IIIi - I11i * Ii1I - oOo0O0Ooo
elif IiI1I1I == 3001 :
 oo00ooooOOo00 ( )
 if 22 - 22: I1ii11iIi11i % ii - I1ii11iIi11i - o0oOO0O00o0O . Ii11Ii1I
elif IiI1I1I == 3002 :
 ii1i ( OooOoOo )
 if 100 - 100: IIiIiII11i / IIIi / o0oOO0O00o0O - Ii1I * iI11I1II1I1I
elif IiI1I1I == 3003 :
 OO00Oooo000 ( OooOoOo )
 if 7 - 7: ooOoO0O00 . OooO0OoOOOO % Ii * Ii1I . iI1iI1I1i1I % Ii1I
elif IiI1I1I == 3004 :
 oO0oiIiI ( OooOoOo )
 if 35 - 35: oOo0O0Ooo
elif IiI1I1I == 404 :
 I1i1i1iIi1iIi ( iiI1IIIi , OooOoOo , OOOOO0O00 )
 if 48 - 48: ii % ii - oO0o . OOooOOo
elif IiI1I1I == 405 :
 O0oOo0o0000 ( OooOoOo )
 if 22 - 22: O0OoO . Ii . ii . ooOoO0O00
elif IiI1I1I == 7030 :
 oo0O ( )
 if 12 - 12: OOooOOo % IIIii1II1II + OoOo00o . o0o00Oo0O % iI11I1II1I1I
elif IiI1I1I == 7021 :
 OO000OOOo0Oo ( iiI1IIIi )
 if 41 - 41: ii
elif IiI1I1I == 7022 :
 o0i1I ( iiI1IIIi )
 if 13 - 13: iI1iI1I1i1I + IIIi - IIIi % OoOo00o / iI1iI1I1i1I
elif IiI1I1I == 7000 :
 IioOOO00Oo ( iiI1IIIi , OooOoOo , img )
 if 4 - 4: oOo0O0Ooo + IIIii1II1II - OooO0OoOOOO + o0oOO0O00o0O
elif IiI1I1I == 7050 :
 Ii1IIii ( OooOoOo )
 if 78 - 78: Ii11Ii1I
elif IiI1I1I == 7051 :
 IiIiiI1iii1iIiiI ( OooOoOo )
 if 29 - 29: IIiIiII11i
elif IiI1I1I == 7052 :
 iI1IIii1IiI1iI1I ( OooOoOo )
 if 79 - 79: iI11I1II1I1I - Ii + O0OoO - IIiIiII11i . iI11I1II1I1I
elif IiI1I1I == 7053 :
 Iiii ( OooOoOo )
 if 84 - 84: I1ii11iIi11i % iI1iI1I1i1I * o0o00Oo0O * iI1iI1I1i1I
elif IiI1I1I == 7054 :
 CoolPlay ( OooOoOo )
 if 66 - 66: IIIii1II1II / iI11I1II1I1I - OOooOOo % o0o00Oo0O . O0OoO
elif IiI1I1I == 7060 :
 IiIii11i1IIiI ( )
 if 12 - 12: I1ii11iIi11i + oOo0O0Ooo
elif IiI1I1I == 7061 :
 I1iIiiiIi1111I ( OooOoOo )
 if 37 - 37: ooOoO0O00 * Ii
elif IiI1I1I == 7063 :
 I11iIIi ( OooOoOo )
 if 95 - 95: Ii % IIIi * I1ii11iIi11i + ooOoO0O00 . o0o00Oo0O + Ii1I
elif IiI1I1I == 7062 :
 Oooo ( OooOoOo )
 if 7 - 7: oO0o * Ii * iI11I1II1I1I / IIIii1II1II / IIIi
elif IiI1I1I == 7064 :
 NATatozcat ( )
 if 35 - 35: o0oOO0O00o0O * IIIii1II1II
elif IiI1I1I == 7067 :
 O00 ( OooOoOo )
 if 65 - 65: IIiIiII11i % ooOoO0O00
elif IiI1I1I == 7066 :
 NATatozA ( OooOoOo )
 if 13 - 13: oO0o * IIIi + I1ii11iIi11i - OooO0OoOOOO
elif IiI1I1I == 7065 :
 IiIIIIi ( OooOoOo )
 if 31 - 31: oO0o
elif IiI1I1I == 7070 :
 Iii1Iooo ( )
 if 68 - 68: oO0o + ooOoO0O00 / iI11I1II1I1I + IIiIiII11i * iI11I1II1I1I + Ii1I
elif IiI1I1I == 7071 :
 DIZIlist ( OooOoOo )
 if 77 - 77: Ii - IIIi . Ii1I % I1ii11iIi11i . Ii11Ii1I
elif IiI1I1I == 7072 :
 DIZIpull ( OooOoOo )
 if 9 - 9: I11i
elif IiI1I1I == 7073 :
 WATCHDIZI ( OooOoOo )
 if 55 - 55: IIIii1II1II % iI11I1II1I1I + iI1iI1I1i1I . O0OoO
elif IiI1I1I == 7002 :
 oo00o000O ( )
 if 71 - 71: Ii / ooOoO0O00 + OOooOOo
elif IiI1I1I == 7003 :
 ooo0oo ( OooOoOo )
 if 23 - 23: Ii
elif IiI1I1I == 7004 :
 OoOOoOOoo ( OooOoOo )
 if 88 - 88: IIiIiII11i - o0oOO0O00o0O / ii
elif IiI1I1I == 7020 :
 I1iII ( OooOoOo )
 if 71 - 71: Ii1I
elif IiI1I1I == 7001 :
 OO0OO00ooO0 ( )
 if 19 - 19: I1ii11iIi11i - oO0o + Ii / iI11I1II1I1I
elif IiI1I1I == 7010 :
 IiiII ( OooOoOo )
 if 1 - 1: OooO0OoOOOO % ooOoO0O00
elif IiI1I1I == 7011 :
 ooo00O0OOo ( OooOoOo )
 if 41 - 41: oO0o * oO0o / o0oOO0O00o0O + Ii1I . I11i
elif IiI1I1I == 7012 :
 oOoo00oO0O0OO ( OooOoOo )
 if 84 - 84: Ii + oO0o * oOo0O0Ooo + Ii1I / Ii11Ii1I
elif IiI1I1I == 7013 :
 cnfTVPlay2 ( OooOoOo )
elif IiI1I1I == 7014 :
 CNF_Studio_Indexer . MV_Movies ( OooOoOo )
elif IiI1I1I == 7015 :
 CNF_Studio_Indexer . Movie_ByYear ( OooOoOo )
elif IiI1I1I == 7016 :
 CNF_Studio_Indexer . Resolve_CNF_Link ( iiI1IIIi , OooOoOo , OOOOO0O00 )
elif IiI1I1I == 7017 :
 CNF_Studio_Indexer . Search_Movie ( )
elif IiI1I1I == 7018 :
 ooOoOoo000O0O ( )
elif IiI1I1I == 7019 :
 CNF_Studio_Indexer . List_Movies ( OooOoOo )
elif IiI1I1I == 7020 :
 CNF_Studio_Indexer . Get_Movie_Page ( OooOoOo )
elif IiI1I1I == 7024 :
 CNF_Studio_Indexer . Box_Office ( OooOoOo )
 if 80 - 80: Ii1I
elif IiI1I1I == 8000 :
 I11IIIII ( )
elif IiI1I1I == 8001 :
 oO0OOoo ( )
elif IiI1I1I == 8002 :
 OoO0o0OO ( )
elif IiI1I1I == 8003 :
 iiIIIi1iIi ( )
elif IiI1I1I == 8004 :
 i1I111iIii1i1 ( )
elif IiI1I1I == 8005 :
 iIi11III ( )
elif IiI1I1I == 8006 :
 i1iI1IIi1I ( iiI1IIIi , OooOoOo )
elif IiI1I1I == 8030 :
 OOooO ( OooOoOo )
elif IiI1I1I == 8045 :
 i1Iiii ( OooOoOo )
elif IiI1I1I == 8046 :
 o0O0O ( OooOoOo )
elif IiI1I1I == 8047 :
 iIIIII1iI ( OooOoOo )
elif IiI1I1I == 8020 :
 iiiiI1iiiIi11 ( )
elif IiI1I1I == 8021 :
 O0oOOO0o0Ooo ( OooOoOo )
elif IiI1I1I == 8022 :
 i1iIII1IIi ( OooOoOo )
elif IiI1I1I == 8023 :
 Oo0 ( OooOoOo )
elif IiI1I1I == 8040 :
 O00oooooo ( )
elif IiI1I1I == 8041 :
 Ii111111ii ( OooOoOo )
elif IiI1I1I == 8042 :
 OOOOoo00OO0O0Ooo0 ( OooOoOo )
elif IiI1I1I == 8043 :
 yt . PlayVideo ( OooOoOo )
elif IiI1I1I == 8044 :
 ooOOO00oOOooO ( OooOoOo )
elif IiI1I1I == 8060 :
 O0oO0o0OOOOOO ( )
elif IiI1I1I == 8061 :
 IiI1i11IiIiii ( OooOoOo )
elif IiI1I1I == 8064 :
 IiI1I ( )
elif IiI1I1I == 8065 :
 IIIiIi1iiI ( OooOoOo )
elif IiI1I1I == 8070 :
 o0Iiii ( )
elif IiI1I1I == 8071 :
 I1i1I ( OooOoOo )
elif IiI1I1I == 7080 :
 i1111iI1 ( OooOoOo )
elif IiI1I1I == 8090 :
 oO0O0o0o000 ( )
elif IiI1I1I == 8091 :
 III1 ( OooOoOo )
elif IiI1I1I == 8092 :
 OOO000OOo0o0O ( OooOoOo )
elif IiI1I1I == 8081 :
 III ( )
elif IiI1I1I == 8062 :
 IiiIi1I11 ( OooOoOo )
elif IiI1I1I == 8063 :
 Oooo0O0Oooo ( OooOoOo )
elif IiI1I1I == 8050 :
 iiII ( )
elif IiI1I1I == 8051 :
 o0Oii1111i ( OooOoOo )
elif IiI1I1I == 8052 :
 O0ooOO ( OooOoOo )
elif IiI1I1I == 8085 :
 oOooOOo00ooO ( )
elif IiI1I1I == 8086 :
 OO0oo ( OooOoOo )
elif IiI1I1I == 8087 :
 o00oO0O0oo0o ( OooOoOo )
elif IiI1I1I == 8088 :
 iIi11I11 ( OooOoOo , iiI1IIIi )
elif IiI1I1I == 9000 :
 OOoOoo0 ( )
elif IiI1I1I == 1111 :
 II11II ( )
elif IiI1I1I == 9001 :
 IIII1ii1 ( )
elif IiI1I1I == 9002 :
 IiIiI11IIi11Iii ( )
elif IiI1I1I == 9003 :
 Ii1IOoO0o0O ( )
elif IiI1I1I == 50 :
 iiIii1I ( OooOoOo )
elif IiI1I1I == 9020 :
 champlist ( )
elif IiI1I1I == 9021 :
 oO00o0O0Ooo ( )
elif IiI1I1I == 9022 :
 ii11 ( )
elif IiI1I1I == 9023 :
 I1i11IIIi ( )
elif IiI1I1I == 9024 :
 iIii1ii ( OooOoOo )
elif IiI1I1I == 9030 :
 I1I1i11 ( OooOoOo )
elif IiI1I1I == 9031 :
 oOo0Oo00O ( OooOoOo )
elif IiI1I1I == 9032 :
 i1io0o00O ( OooOoOo )
elif IiI1I1I == 9033 :
 iiiI1ii ( OooOoOo )
elif IiI1I1I == 7085 :
 OOo0oO0o ( OooOoOo )
elif IiI1I1I == 7086 :
 O0oo0000o ( OooOoOo )
elif IiI1I1I == 7087 :
 i11IiIi ( iIIIII1I )
elif IiI1I1I == 9666 :
 II1i111 ( OooOoOo )
elif IiI1I1I == 10100 : iIo00OOOOOo0OOo ( )
elif IiI1I1I == 10105 : i1i1I1iiIiIII ( OooOoOo )
elif IiI1I1I == 10106 : OOo000o ( OooOoOo )
elif IiI1I1I == 10104 : o0OOo ( OooOoOo )
elif IiI1I1I == 10107 : O000oooOO0Oo0 ( )
elif IiI1I1I == 10103 : II11ii1I11 ( OooOoOo )
elif IiI1I1I == 10108 : O0OOO00OOO00o ( OooOoOo )
elif IiI1I1I == 10107 : O000oooOO0Oo0 ( )
elif IiI1I1I == 10000 : Origin_Menu ( )
elif IiI1I1I == 10001 : IiiiI ( )
elif IiI1I1I == 10002 : I1i1II1 ( )
elif IiI1I1I == 10003 : ooOO0o ( )
elif IiI1I1I == 10004 : O0Oo00OO00Ooo ( OooOoOo )
elif IiI1I1I == 10005 : iIIiI1iiI ( )
elif IiI1I1I == 10006 : iIi1Ii ( OooOoOo )
elif IiI1I1I == 10007 : OOOo00 ( OooOoOo , OOOOO0O00 )
elif IiI1I1I == 10008 : oo00I1IiI1IIiI ( )
elif IiI1I1I == 10009 : iI ( )
elif IiI1I1I == 10010 : OOoooOoO0 ( OooOoOo )
elif IiI1I1I == 10011 : iIi1ooo0Oooooo ( OooOoOo )
elif IiI1I1I == 10012 : O00o0O ( OooOoOo )
elif IiI1I1I == 10013 : OOOOoO ( OooOoOo )
elif IiI1I1I == 10014 : II1iiI ( )
elif IiI1I1I == 10015 : I1IiIii11I ( )
elif IiI1I1I == 10016 : OOoO0oO00o ( OooOoOo )
elif IiI1I1I == 10017 : o0i1iI1iiI1I ( )
elif IiI1I1I == 10018 : i1Iio0oO00 ( )
elif IiI1I1I == 10019 : I1ii1i ( )
elif IiI1I1I == 10020 : O0000oO0o00 ( )
elif IiI1I1I == 10021 : OO0ooOoOO0OOo ( )
elif IiI1I1I == 10022 : Ooi1I11 ( OooOoOo )
elif IiI1I1I == 10023 : i11i ( iiI1IIIi , OooOoOo )
elif IiI1I1I == 10024 : iI1I1I1i1i ( OooOoOo )
elif IiI1I1I == 10025 : iiI1iI1I ( )
elif IiI1I1I == 10026 : oOII1ii1ii11I1 ( )
elif IiI1I1I == 10027 : oOOooooo0OoO0 ( )
elif IiI1I1I == 10028 : Ii11Iii ( )
elif IiI1I1I == 10029 : oo0oO0oO ( )
elif IiI1I1I == 423 : I1IIi1I ( OooOoOo )
elif IiI1I1I == 426 : oo000oO ( OooOoOo )
elif IiI1I1I == 10030 : Izle_Films ( )
elif IiI1I1I == 10031 : Latest_Izle_Movies ( )
elif IiI1I1I == 10032 : Izle_Genres ( )
elif IiI1I1I == 10033 : Izle_Pop_Movies ( )
elif IiI1I1I == 10034 : Izle_Boxsets ( )
elif IiI1I1I == 10035 : Izle_Search ( )
elif IiI1I1I == 10036 : Izle_Genres_Movie ( OooOoOo )
elif IiI1I1I == 10037 : Izle_Boxset_single ( OooOoOo )
elif IiI1I1I == 10038 : Izle_IFRAME ( )
elif IiI1I1I == 10039 : Izle_Boxsets_Next ( OooOoOo )
elif IiI1I1I == 10040 : O00oo ( )
elif IiI1I1I == 10041 : o0oOo00 ( OooOoOo )
elif IiI1I1I == 10042 : OOooO0Oo00 ( OooOoOo )
elif IiI1I1I == 10043 : i11i1i ( )
elif IiI1I1I == 10044 : I1IIII1i1 ( OooOoOo )
elif IiI1I1I == 10045 : oOoOoO0o0 ( iiI1IIIi )
elif IiI1I1I == 10046 : IiiI11I1IIiI ( OooOoOo )
elif IiI1I1I == 10047 : oOo0OO0o0 ( OooOoOo )
elif IiI1I1I == 10048 : iIII11Iiii1 ( OooOoOo )
elif IiI1I1I == 10049 : o0OoO0OOoO0Oo0 ( OooOoOo )
elif IiI1I1I == 10050 : Oo00oo00o00Oo ( )
elif IiI1I1I == 10051 : iIIIi1i1Ii ( )
elif IiI1I1I == 10052 : Ooo0o0000OO ( )
elif IiI1I1I == 10053 : Addon ( OooOoOo )
elif IiI1I1I == 10054 : Oo0ooo ( OooOoOo , iiI1IIIi )
elif IiI1I1I == 10055 :
 OOOO0oOo00O ( "addFavorite" )
 try :
  iiI1IIIi = iiI1IIIi . split ( '\\ ' ) [ 1 ]
 except :
  pass
 try :
  iiI1IIIi = iiI1IIIi . split ( '  - ' ) [ 0 ]
 except :
  pass
 oo0ooooo00o ( iiI1IIIi , OooOoOo , OOOOO0O00 , Iii , iiii1I1IiI )
elif IiI1I1I == 10056 :
 OOOO0oOo00O ( "rmFavorite" )
 try :
  iiI1IIIi = iiI1IIIi . split ( '\\ ' ) [ 1 ]
 except :
  pass
 try :
  iiI1IIIi = iiI1IIIi . split ( '  - ' ) [ 0 ]
 except :
  pass
 o0OO0OOO0O ( iiI1IIIi )
elif IiI1I1I == 10057 :
 OOOO0oOo00O ( "getFavorites" )
 i1ii1IiiiiIi1I ( )
elif IiI1I1I == 10058 : Oo00000o0o ( )
elif IiI1I1I == 10059 : Donators_Guide ( )
elif IiI1I1I == 10060 : i1OO0oOOoo ( )
elif IiI1I1I == 10061 : O000OOO0OOo ( )
elif IiI1I1I == 10062 : IiiIiI111iI ( iiI1IIIi , OooOoOo , iIIIII1I )
elif IiI1I1I == 10063 : OooO0oo ( )
elif IiI1I1I == 10064 : iI1I ( )
elif IiI1I1I == 10065 : I11i1II ( OooOoOo )
elif IiI1I1I == 10066 : ooOOoO ( OooOoOo )
elif IiI1I1I == 10068 : IIiI1Ii ( OooOoOo )
elif IiI1I1I == 10069 : ii111I ( OooOoOo )
elif IiI1I1I == 10070 : i1i11I11 ( OooOoOo )
elif IiI1I1I == 10071 : Genie_Watch ( )
elif IiI1I1I == 10072 : I1II1 ( )
elif IiI1I1I == 10073 : oOOOoo00 ( OooOoOo )
elif IiI1I1I == 10074 : oo0 ( OooOoOo )
elif IiI1I1I == 10075 : iI1i111I1Ii ( OOOOO0O00 , iiI1IIIi , OooOoOo )
elif IiI1I1I == 10076 : OOOooo ( OooOoOo )
elif IiI1I1I == 10077 : IIIIiII1i ( OooOoOo )
elif IiI1I1I == 10078 : II1i111Ii1i ( )
elif IiI1I1I == 10079 : Genie_Watch_Tv_Shows ( )
elif IiI1I1I == 10080 : Genie_Watch_Tv_Genre ( OooOoOo )
elif IiI1I1I == 10081 : Genie_Watch_TV_PlayRun ( OooOoOo )
elif IiI1I1I == 10082 : Genie_Watch_TV_Episodes ( OooOoOo , OOOOO0O00 )
elif IiI1I1I == 10083 : Genie_Watch_Tv_Recent ( OooOoOo )
elif IiI1I1I == 10084 : oOO00O ( )
elif IiI1I1I == 10085 : oo00O00oO ( )
elif IiI1I1I == 10086 : oo0OOo ( )
elif IiI1I1I == 20000 : Oo ( )
elif IiI1I1I == 20001 : O0oOo ( )
elif IiI1I1I == 20002 : iIiIIi ( OooOoOo )
elif IiI1I1I == 20003 : I1iIiI1IiIIII ( OooOoOo )
elif IiI1I1I == 20004 : iI1IiiiI11 ( OooOoOo )
elif IiI1I1I == 21004 : IiI1i111IiIiIi1 ( )
elif IiI1I1I == 21005 : i1II11II1 ( OooOoOo )
elif IiI1I1I == 21006 : iIIIiIi1I1i ( OooOoOo )
elif IiI1I1I == 21007 : Iiio0Oo0oO ( OooOoOo )
elif IiI1I1I == 30000 : Ii1iIi111i1i1 ( )
elif IiI1I1I == 30001 : IIo00ooo ( )
elif IiI1I1I == 10012 : Resolve ( OooOoOo )
elif IiI1I1I == 30003 : iIiI1IIiii11 ( )
elif IiI1I1I == 30004 : o0oo0000 ( OooOoOo )
elif IiI1I1I == 30005 : o0Oo ( OooOoOo )
elif IiI1I1I == 30006 : Ii1IIiiIiiIi ( )
elif IiI1I1I == 30007 : oOOo0oo0o0o0 ( )
elif IiI1I1I == 30008 : I1i ( OooOoOo )
elif IiI1I1I == 30009 : iIIi1iI1I1IIi ( OooOoOo )
elif IiI1I1I == 30010 : o0O0Oo0Ooo0 ( OooOoOo )
elif IiI1I1I == 30011 : i1iIIIiiiI ( )
elif IiI1I1I == 30012 : iIi1IIi1ii ( )
elif IiI1I1I == 30013 : oo00IIIIIIIiI ( )
elif IiI1I1I == 30014 : OO0oIiII1iiI ( )
elif IiI1I1I == 30015 : o0OO000ooOo ( OooOoOo , OOOOO0O00 , Iii )
elif IiI1I1I == 30016 : OooO0oOo ( OooOoOo )
elif IiI1I1I == 30019 : IiI ( OooOoOo )
elif IiI1I1I == 30017 : II1I11IIi ( OooOoOo )
elif IiI1I1I == 30018 : i1IIII1iii11I ( OooOoOo )
elif IiI1I1I == 30030 : O0OOo ( )
elif IiI1I1I == 30031 : I1ii11I ( )
elif IiI1I1I == 30032 : II1II1IIII ( )
elif IiI1I1I == 30033 : i1iiiiI1IiIIii ( )
elif IiI1I1I == 30034 : IIIIiiiIi11Ii1iI ( )
elif IiI1I1I == 30035 : I11I1IIiiII1 ( OooOoOo )
elif IiI1I1I == 30036 : IIIIIii1ii11 ( OooOoOo )
elif IiI1I1I == 30037 : OOOooo0OooOoO ( OooOoOo )
elif IiI1I1I == 30038 : o0OOoOoO00 ( )
elif IiI1I1I == 30039 : o0Ii1Iii111IiI1 ( )
if 67 - 67: IIiIiII11i
xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
