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
IiiIII111iI = "2.8.4"
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
  II1I ( '[COLORgreen]APK TOOL[/COLOR]' , str ( Ii1iIiII1ii1 ) , 2 , ooOooo000oOO + 'APK.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Rss Feed' ) == 'true' :
  II1I ( '[COLORgreen]GenieTv RSS Feed[/COLOR]' , str ( Ii1iIiII1ii1 ) , 39 , ooOooo000oOO + 'RSS.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Addons Packs' ) == 'true' :
  II1I ( '[COLORgreen]ADDONS PACKS[/COLOR]' , str ( Ii1iIiII1ii1 ) , 30 , ooOooo000oOO + 'ADDONP.png' , i1iiIII111ii , '' )
 iiO0o0oOOOoOo ( 'movies' , 'MAIN' )
 if 17 - 17: I11i . oOo0O0Ooo * o0oOO0O00o0O % o0oOO0O00o0O
def iI1I ( ) :
 O0O0O0OoOO ( )
 II1I ( '[COLORgreen]BACKUP MY BUILD[/COLOR]' , str ( Ii1iIiII1ii1 ) , 10060 , ooOooo000oOO + 'MB.png' , i1iiIII111ii , '' )
 II1I ( '[COLORgreen]RESTORE MY BUILD[/COLOR]' , str ( Ii1iIiII1ii1 ) , 49 , ooOooo000oOO + 'MB.png' , i1iiIII111ii , '' )
 II1I ( '[COLORgreen]WIPE GENIE[/COLOR]' , str ( Ii1iIiII1ii1 ) , 41 , ooOooo000oOO + 'wipegenie.png' , i1iiIII111ii , '' )
 if 18 - 18: Ii11Ii1I + oO0o % Ii1I * OoOo00o - OooO0OoOOOO
 II1I ( '[COLORgreen]Genie BUILDS[/COLOR]' , str ( Ii1iIiII1ii1 ) , 44 , ooOooo000oOO + 'WISHESAN.png' , i1iiIII111ii , '' )
 iiO0o0oOOOoOo ( 'movies' , 'MAIN' )
def oOiI ( ) :
 O0O0O0OoOO ( )
 if oO == '5knuckleshuffle' :
  II1I ( '[COLORgreen]XVID[/COLOR]' , str ( Ii1iIiII1ii1 ) , 10100 , ooOooo000oOO + 'JIZBOX.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Favourites' ) == 'true' :
  II1I ( '[COLORgreen]FAVOURITES[/COLOR]' , str ( Ii1iIiII1ii1 ) , 10057 , ooOooo000oOO + 'FAVORITES.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Search' ) == 'true' :
  II1I ( '[COLORgreen]SEARCH[/COLOR]' , str ( Ii1iIiII1ii1 ) , 9000 , ooOooo000oOO + 'search.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'TV GUIDE' ) == 'true' :
  ooOOoooooo ( '[COLORgreen]TV GUIDE[/COLOR]' , '' , 10063 , ooOooo000oOO + 'GTVIPTV.png' , i1iiIII111ii , '' )
 II1I ( '[COLORgreen]MOVIES[/COLOR]' , str ( Ii1iIiII1ii1 ) , 4004 , ooOooo000oOO + 'MOVIESv.png' , i1iiIII111ii , '' )
 II1I ( '[COLORgreen]TV SHOWS[/COLOR]' , str ( Ii1iIiII1ii1 ) , 4005 , ooOooo000oOO + 'TVSHOWSv.png' , i1iiIII111ii , '' )
 II1I ( '[COLORgreen]STREAM TEAM[/COLOR]' , str ( Ii1iIiII1ii1 ) , 4006 , ooOooo000oOO + 'streamteam.png' , i1iiIII111ii , '' )
 II1I ( '[COLORgreen]KIDS[/COLOR]' , str ( Ii1iIiII1ii1 ) , 4007 , ooOooo000oOO + 'KIDSv.png' , i1iiIII111ii , '' )
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
  if 32 - 32: o0oOO0O00o0O . OooO0OoOOOO . OooO0OoOOOO
  if 62 - 62: Ii1I + OooO0OoOOOO % o0oOO0O00o0O + IIIii1II1II
 if o0oO0 . getSetting ( 'Playlist Loader' ) == 'true' :
  II1I ( '[COLORgreen]PLAYLIST LOADER[/COLOR]' , str ( Ii1iIiII1ii1 ) , 3000 , ooOooo000oOO + 'loader.png' , i1iiIII111ii , '' )
  if 33 - 33: o0o00Oo0O . OooO0OoOOOO . oOo0O0Ooo
  if 72 - 72: ooOoO0O00 / oO0o + ii - I1ii11iIi11i
  if 29 - 29: Ii1I + OoOo00o % o0o00Oo0O
  if 10 - 10: iI1iI1I1i1I / IIIi - oOo0O0Ooo * iI11I1II1I1I - oOo0O0Ooo
  if 97 - 97: Ii1I + oOo0O0Ooo * Ii11Ii1I + IIIii1II1II % o0oOO0O00o0O
  if 74 - 74: OoOo00o - I1ii11iIi11i + ii + IIIi / OOooOOo
  if 23 - 23: o0o00Oo0O
  if 85 - 85: Ii11Ii1I
  if 84 - 84: oOo0O0Ooo . iI11I1II1I1I % ii + Ii11Ii1I % ii % oO0o
  if 42 - 42: oO0o / iI1iI1I1i1I / I11i + o0oOO0O00o0O / OOooOOo
  if 84 - 84: O0OoO * IIiIiII11i + I1ii11iIi11i
  if 53 - 53: o0oOO0O00o0O % IIiIiII11i . OooO0OoOOOO - iI11I1II1I1I - OooO0OoOOOO * IIiIiII11i
  if 77 - 77: iI11I1II1I1I * oO0o
 iiO0o0oOOOoOo ( 'movies' , 'MAIN' )
 if 95 - 95: oOo0O0Ooo + Ii
def IiIIIi1iIi ( ) :
 if not os . path . exists ( iiI1IiI ) :
  I1Ii ( 'Change Log 11/05/16 - v2.8.3' , 'Fixing search function, took out few sources that are taking ages and bringing back no results. \n\nFixed Genie Favourites so it shouldn\'t error now if nothing in there \n\nAdded Function to check official version of Genie Tv and repo is installed and get correct one on starting genie if not. To keep you up to date and so we know people are using only versions from correct source save answering questions after things are altered without our knowledge' )
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
 iiO0o0oOOOoOo ( 'movies' , 'MAIN' )
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
 if o0oO0 . getSetting ( 'Dizzy Tv' ) == 'true' :
  II1I ( '[COLORgreen]DIZZY TV[/COLOR]' , '' , 10018 , ooOooo000oOO + 'dtv.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Watch Series' ) == 'true' :
  II1I ( '[COLORgreen]WATCH SERIES[/COLOR]' , '' , 10040 , ooOooo000oOO + 'WATCHSERIES.png' , i1iiIII111ii , '' )
 II1I ( '[COLORgreen]iWATCH SERIES[/COLOR]' , '' , 8020 , ooOooo000oOO + 'iwatch.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Recent Episodes' ) == 'true' :
  II1I ( '[COLORgreen]RECENT EPISODES[/COLOR]' , str ( Ii1iIiII1ii1 ) , 8081 , ooOooo000oOO + 'recent.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'CLASSIC TV' ) == 'true' :
  II1I ( '[COLORgreen]CLASSIC TV[/COLOR]' , str ( Ii1iIiII1ii1 ) , 8064 , ooOooo000oOO + 'classictv.png' , i1iiIII111ii , '' )
 II1I ( '[COLORgreen]TV Show Trailers[/COLOR]' , i1111 ( 'aHR0cHM6Ly93d3cueW91dHViZS5jb20vd2F0Y2g/dj03WkZJUzJBcUF6OCZsaXN0PVBMM2t4NWgyVHJZR3dwVzBWYk5lbnBqLUJLTUJUR2dKUEU=' ) , 10069 , ooOooo000oOO + 'tvtrailers.png' , i1iiIII111ii , '' )
 II1I ( '[COLORgreen]TV Show Schedule[/COLOR]' , i1111 ( 'aHR0cDovL3d3dy5wb2dkZXNpZ24uY28udWsvY2F0Lw==' ) , 10070 , ooOooo000oOO + 'tvschedule.png' , i1iiIII111ii , '' )
 iiO0o0oOOOoOo ( 'movies' , 'MAIN' )
def I1i1Iiiii ( ) :
 O0O0O0OoOO ( )
 if o0oO0 . getSetting ( 'Scooby Streams' ) == 'true' :
  II1I ( '[COLORgreen]SCOOBY STREAMS[/COLOR]' , str ( Ii1iIiII1ii1 ) , 1023 , ooOooo000oOO + 'scoob.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'The Reaper' ) == 'true' :
  II1I ( '[COLORgreen]THE REAPER[/COLOR]' , ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9UaGVfUmVhcGVyL21haW4ucGhw' ) ) , 1016 , ooOooo000oOO + 'reap.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Pandoras Box' ) == 'true' :
  II1I ( '[COLORgreen]PANDORAS BOX[/COLOR]' , str ( Ii1iIiII1ii1 ) , 10025 , ooOooo000oOO + 'PANDORASBOX.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'HeroVision' ) == 'true' :
  II1I ( '[COLORgreen]HEROVISION[/COLOR]' , '' , 1017 , ooOooo000oOO + 'hero.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Silent Hunter' ) == 'true' :
  II1I ( '[COLORgreen]SILENT HUNTER[/COLOR]' , ( i1111 ( 'aHR0cDovLzUuMTM1LjIwNy45Ni8=' ) ) , 10084 , ooOooo000oOO + 'SILENTHUNTER.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Redemption Streams' ) == 'true' :
  II1I ( '[COLORgreen]Redemption Streams[/COLOR]' , ( i1111 ( 'aHR0cDovL3JlZGVtcHRpb25idWlsZC4xNm1iLmNvbS9SZWRlbXB0aW9uL21haW4ucGhw' ) ) , 1016 , ooOooo000oOO + 'redemption.png' , i1iiIII111ii , '' )
 II1I ( '[COLORgreen]ITV[/COLOR]' , ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9pVHZfU3RyZWFtcy9tYWluLnBocA==' ) ) , 1016 , ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9pVHZfU3RyZWFtcy9pdHZzdHJlYW1zLnBuZw==' ) ) , i1iiIII111ii , '' )
 iiO0o0oOOOoOo ( 'movies' , 'MAIN' )
 if 94 - 94: I11i * Ii11Ii1I / I1ii11iIi11i / Ii11Ii1I
def oO0O0OO0O ( ) :
 O0O0O0OoOO ( )
 II1I ( '[COLORgreen]SILENT HUNTER[/COLOR]' , ( i1111 ( 'aHR0cDovLzUuMTM1LjIwNy45Ni8=' ) ) , 1006 , ooOooo000oOO + 'SILENTHUNTER.png' , i1iiIII111ii , '' )
 II1I ( '[COLORgreen]SILENT HUNTER SCRAPES[/COLOR]' , ( i1111 ( 'aHR0cDovLzUuMTM1LjIwNy45Ni9TY3JhcGVzL21haW4ucGhw' ) ) , 1016 , ooOooo000oOO + 'SILENTHUNTER.png' , i1iiIII111ii , '' )
 if 81 - 81: OoOo00o . I11i % o0o00Oo0O / oOo0O0Ooo - OoOo00o
def Ii1I1i ( ) :
 II1I ( '[COLORgreen]HEROVISION[/COLOR]' , ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC9tYWluLnBocA==' ) ) , 1016 , ooOooo000oOO + 'hero.png' , i1iiIII111ii , '' )
 II1I ( '[COLORgreen]HEROVISION SCRAPES[/COLOR]' , ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC9zY3JhcGVkL3NjcmFwZWQucGhw' ) ) , 1024 , ooOooo000oOO + 'hero.png' , i1iiIII111ii , '' )
 if 99 - 99: OoOo00o . o0oOO0O00o0O + O0OoO % OoOo00o . Ii % o0o00Oo0O
def oOO00O ( ) :
 O0O0O0OoOO ( )
 II1I ( '[COLORgreen]SEARCH CARTOONS[/COLOR]' , '' , 10005 , ooOooo000oOO + 'search.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'WCO' ) == 'true' :
  II1I ( '[COLORgreen]WATCH CARTOONS ONLINE[/COLOR]' , str ( Ii1iIiII1ii1 ) , 21004 , ooOooo000oOO + 'watchcartoons.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Cartoons' ) == 'true' :
  II1I ( '[COLORgreen]CARTOONS[/COLOR]' , '' , 10001 , ooOooo000oOO + 'ORIGINCARTOON.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Anime' ) == 'true' :
  II1I ( '[COLORgreen]AnimeLand[/COLOR]' , ( i1111 ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2R1YmJlZC1hbmltZQ==' ) ) , 10004 , ooOooo000oOO + 'anime.png' , i1iiIII111ii , '' )
 iiO0o0oOOOoOo ( 'movies' , 'MAIN' )
def OOOoo0OO ( ) :
 O0O0O0OoOO ( )
 if o0oO0 . getSetting ( 'Football' ) == 'true' :
  II1I ( '[COLORgreen]FOOTBALL[/COLOR]' , '' , 10002 , ooOooo000oOO + 'ORIGINFOOTBALL.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Fitness' ) == 'true' :
  II1I ( '[COLORgreen]FITNESS[/COLOR]' , ( i1111 ( 'aHR0cHM6Ly93d3cuZml0bmVzc2JsZW5kZXIuY29tL3ZpZGVvcw==' ) ) , 7085 , ooOooo000oOO + 'FITNESS.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Go Fishing' ) == 'true' :
  II1I ( '[COLORgreen]Go Fishing[/COLOR]' , str ( Ii1iIiII1ii1 ) , 8090 , ooOooo000oOO + 'gofish.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'GenieTv Kitchen' ) == 'true' :
  II1I ( '[COLORgreen]GenieTv Kitchen[/COLOR]' , ( i1111 ( 'aHR0cDovL2Zvb2QubmR0di5jb20vdmlkZW9z' ) ) , 8045 , ooOooo000oOO + 'geniekitchen.png' , i1iiIII111ii , '' )
 iiO0o0oOOOoOo ( 'movies' , 'MAIN' )
 if 57 - 57: oO0o / O0OoO
 if 29 - 29: iI11I1II1I1I + OOooOOo * oO0o * IIIii1II1II . oOo0O0Ooo * oOo0O0Ooo
 if 7 - 7: OooO0OoOOOO * IIIi % Ii11Ii1I - I11i
def iIiIIIi ( ) :
 o00OO00OoO = iiI111I1iIiI ( 'http://genietv.co.uk/genietv_art/testdelete.txt' )
 Ii1i = re . compile ( '<unwanted_addon =(.+?)</unwanted_addon>' ) . findall ( o00OO00OoO )
 for o0ooO in Ii1i :
  o0ooO = ( str ( o0ooO ) )
  if os . path . exists ( xbmc . translatePath ( o0ooO ) ) :
   i1ioOOoo00O00o = ( o0ooO ) . replace ( 'special://home/addons/' , '' )
   I1Ii ( "Please remove any addons or repo's that may alter Genie Tv coding without your knowledge" , "It has been recognised you have \n[COLORred]" + i1ioOOoo00O00o + "[/COLOR]\n installed on your system. In order for genie to function this addon must be removed. \n\nThere have been 'creative differences' between ourselves and this addon. Initially we just stopped our addon from working if this addon was installed, but when private talks were undertaken the 'author' (we use this term very lightly) of this addon gave us a choice, either remove our block or they will tamper with our addon, they then saw fit to host our addon and begin pushing unwanted and unauthorised, potentially malicious updates (we've no idea what they altered and with there approach anything could be possible) so we took steps to remove this addon purely for your protection from alterations to code from, self confessed, unskilled individuals. \n\nHowever the approach we took i guess can be seen as malicious because we did not inform you of actions that altered your device without your knowledge (bar a popup telling you this was happening), for this we apologise, it was a major oversight on our part and made us no better than them. \n\nAll are free to continue to use genie tv at no cost but you must make a decision. A box will soon open and you will need to choose remove or close. If you choose remove you are accepting to remove these addons that we believe have the potential to maliciously alter your device from an unofficial source or if you press close it will close genie, it will not be useable until these addons are remove and you can chose to use whatever addon you see fit at your own risk. \n\nThis is not 'playing god' please dont see it that way but merely protecting our hard work and in the end your experience from this.  We hope this issue resolves itself and things return to normality as much as, if not more than, yourself. Please wait to decide what action you wish to take" )
   xbmc . sleep ( 40000 )
   O0O00Oo = xbmcgui . Dialog ( ) . yesno ( 'Remove Potentially Harmful Addons' , 'Remove will remove addons known to alter genie tv' , 'Close will stop genie tv working to protect' , 'you from any potential unwanted updates' , nolabel = 'Close' , yeslabel = 'Remove' )
   if O0O00Oo == 0 :
    O0o0O00Oo0o0 ( o0ooO )
    oooooo0O000o ( )
   elif O0O00Oo == 1 :
    OoO ( o0ooO )
  else :
   pass
   if 51 - 51: ii * IIIii1II1II
def OoO ( addon ) :
 i1ioOOoo00O00o = ( addon ) . replace ( 'special://home/addons/' , '' )
 Oo0oO0ooo . create ( "[COLOR=white]The addons are being removed as requested[/COLOR]" , 'Please enjoy Genie Tv and we thank you for your support' , '[COLORyellow]Hopefully this may end soon and peace is restored[/COLOR]' )
 xbmc . sleep ( 3000 )
 addon = xbmc . translatePath ( str ( addon ) )
 shutil . rmtree ( addon , ignore_errors = True )
 Oo0oO0ooo . update ( 100 , "" , "Your Device is now clean" )
 xbmc . sleep ( 1000 )
 Oo0oO0ooo . close ( )
 if 73 - 73: Ii1I * Ii % OoOo00o . Ii1I
def O0o0O00Oo0o0 ( addon ) :
 oOOoo00O0O . ok ( "[COLOR=white]Incompatible[/COLOR]" , "Unfortunately GenieTv will not work with" , addon , 'please remove then reinstall genie' )
 OOOOo0 = os . path . join ( O0OoO000O0OO , 'default.py' )
 IiiiIIiIi1 = open ( OOOOo0 , "w+" )
 if 74 - 74: iI11I1II1I1I * Ii1I + OOooOOo / ooOoO0O00 / IIiIiII11i . I1ii11iIi11i
 IiiiIIiIi1 . write ( r'Genie Tv will not work with certain addons in an attempt to bring you original content from the best developers' )
 IiiiIIiIi1 . write ( r'and not those simply out to profit or make a name for themselves off others work' )
 IiiiIIiIi1 . write ( r'Please remove' + unwanted_addons + 'if you would like to use genie tv then uninstall and reinstall from official repo' )
 if 62 - 62: ii * oOo0O0Ooo
 if 58 - 58: OOooOOo % I11i
 if 50 - 50: IIIi . I11i
 if 97 - 97: o0o00Oo0O + OOooOOo
 if 89 - 89: I11i + oO0o * iI1iI1I1i1I * Ii11Ii1I
 if 37 - 37: ii - o0o00Oo0O - I11i
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
def iI1111ii1I ( ) :
 II1I ( 'Genre' , i1111 ( 'aHR0cDovL2ltb3ZpZW1heC5zZS9tb3ZpZXMv' ) , 10073 , ooOooo000oOO + 'genievision.png' , i1iiIII111ii , '' )
 II1I ( 'Most Viewed' , i1111 ( 'aHR0cDovL2ltb3ZpZW1heC5zZS9tb3ZpZXMv' ) , 10077 , ooOooo000oOO + 'genievision.png' , i1iiIII111ii , '' )
 II1I ( 'Box Office' , i1111 ( 'aHR0cDovL2ltb3ZpZW1heC5zZS9jYXRlZ29yeS9ib3gtb2ZmaWNlLw==' ) , 10074 , ooOooo000oOO + 'genievision.png' , i1iiIII111ii , '' )
 II1I ( 'Search' , '' , 10078 , ooOooo000oOO + 'genievision.png' , i1iiIII111ii , '' )
 if 45 - 45: ooOoO0O00 + I11i
def OOO ( ) :
 IIiI1i1i = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 O00Oo0 = 'http://imoviemax.se/?s=' + ( IIiI1i1i ) . replace ( ' ' , '+' )
 IiII111i1i11 = O00Oo0 . lower ( )
 i111iIi1i1II1 ( IiII111i1i11 )
def oooO ( url ) :
 i1I1i111Ii = [ ]
 o00OO00OoO = iiI111I1iIiI ( url )
 Ii1i = re . compile ( '<li class="cat-item cat-item-.+? "><a href="(.+?)">(.+?)</a><i>(.+?)</i></li>' ) . findall ( o00OO00OoO )
 for url , ooo , i1i1iI1iiiI in Ii1i :
  if ooo in i1I1i111Ii :
   pass
  else :
   II1I ( ooo + ' - ' + i1i1iI1iiiI + ' Films' , url , 10074 , ooOooo000oOO + 'genievision.png' , i1iiIII111ii , '' )
   i1I1i111Ii . append ( ooo )
   if 51 - 51: oOo0O0Ooo % IIIi . OoOo00o / iI11I1II1I1I / iI1iI1I1i1I . OoOo00o
def IIIii11 ( url ) :
 o00OO00OoO = iiI111I1iIiI ( url )
 Ii1i = re . compile ( '<li>.+?<b>.+?</b>.+?<a href="(.+?)">(.+?)</a>.+?<span>(.+?)</span>' , re . DOTALL ) . findall ( o00OO00OoO )
 for url , ooo , iiIiIIIiiI in Ii1i :
  II1I ( ooo + ' - Views:' + iiIiIIIiiI , url , 10075 , ooOooo000oOO + 'genievision.png' , i1iiIII111ii , '' )
  if 12 - 12: o0o00Oo0O - I11i
  if 81 - 81: OOooOOo - OOooOOo . o0oOO0O00o0O
def i111iIi1i1II1 ( url ) :
 o0OoOo00o0o = [ ]
 o00OO00OoO = iiI111I1iIiI ( url )
 next = re . compile ( "<link rel='next' href='(.+?)' />" ) . findall ( o00OO00OoO )
 for next in next :
  II1I ( 'NEXT PAGE' , next , 10074 , ooOooo000oOO + 'Next.png' , i1iiIII111ii , '' )
 Ii1i = re . compile ( '<div class="movie">.+?<img src="(.+?)" alt="(.+?)" />.+?<a href="(.+?)"><span class="player"></span></a>' , re . DOTALL ) . findall ( o00OO00OoO )
 for I1II1I11I1I , ooo , url in Ii1i :
  II1I ( ooo , url , 10075 , I1II1I11I1I , I1II1I11I1I , '' )
  o0OoOo00o0o . append ( ooo )
  if 54 - 54: ii + I11i - ooOoO0O00 % Ii
def iII1iIi11i ( img , name , url ) :
 img = img
 name = name
 o00OO00OoO = iiI111I1iIiI ( url )
 Ii1i = re . compile ( '<div id="(.+?)" class="player-content"><iframe class="playerframe" src="(.+?)" scrolling="no".+?</iframe></div>' ) . findall ( o00OO00OoO )
 for o0ooooO0o0O , url in Ii1i :
  print '>>>>>>>>>>>>>>>>>>>>>>>>>>> before' + url
  iiIi11iI1iii = ( url ) . replace ( 'player' , 'watch' ) + '&fv=&sou='
  print '<<<<<<<<<<<<<<<<<<<<<<<<<<< after' + iiIi11iI1iii
  oo000o0000oO = ( o0ooooO0o0O ) . replace ( 'play-' , 'Server ' )
  ooOOoooooo ( oo000o0000oO , iiIi11iI1iii , 10076 , img , img , '' )
  if 15 - 15: OOooOOo % oOo0O0Ooo * iI1iI1I1i1I
def O0OoooO0 ( url ) :
 o00OO00OoO = iiI111I1iIiI ( url )
 Ii1i = re . compile ( '<source src="(.+?)" type="video/mp4">' ) . findall ( o00OO00OoO )
 for ooo0O0o00O in Ii1i :
  if '=m' in ooo0O0o00O :
   I1i11 ( ooo0O0o00O )
  elif 'php' in ooo0O0o00O :
   O0OoooO0 ( url )
  else :
   o00OO00OoO = iiI111I1iIiI ( ooo0O0o00O )
   Ii1i = re . compile ( 'content="(.+?)">' ) . findall ( o00OO00OoO )
   for IiIi1I1 in Ii1i :
    I1i11 ( ooo0O0o00O )
    if 39 - 39: IIiIiII11i + OOooOOo - O0OoO . OOooOOo
    if 84 - 84: oO0o + ooOoO0O00 - IIiIiII11i . Ii1I * ii + oOo0O0Ooo
    if 38 - 38: IIIii1II1II + IIiIiII11i % O0OoO % OOooOOo - Ii11Ii1I / ii
def oOOoo0000O0o0 ( url ) :
 o00OO00OoO = iiI111I1iIiI ( url )
 II1III = re . compile ( '<td id=".+?" class="today">.+?title="(.+?)">(.+?)</td>' , re . DOTALL ) . findall ( o00OO00OoO )
 for III1 , OooooO0oOOOO in II1III :
  print 'there ><><><><><><><><><><><><'
  III1 = III1
  Ii1i = re . compile ( '<p><a href=".+?" rel=".+?">(.+?)</a>.+?<br /><a href=".+?">(.+?)</a>.+?</p>' , re . DOTALL ) . findall ( str ( OooooO0oOOOO ) )
  for ooo , o0O00oOOoo in Ii1i :
   print 'here <><><><><><><><><><><><>'
   II1I ( '[COLORred]' + III1 + '[/COLOR] - ' + ooo + ' - [COLORgreen]' + o0O00oOOoo + '[/COLOR]' , i1111 ( 'aHR0cDovL3d3dy5wb2dkZXNpZ24uY28udWsvY2F0Lw==' ) , 10070 , ooOooo000oOO + 'loader.png' , i1iiIII111ii , '' )
 i1I1iIi = re . compile ( '<td id=".+?" class="day">.+?title="(.+?)">(.+?)</td>' , re . DOTALL ) . findall ( o00OO00OoO )
 for III1 , IIii11Ii1i1I in i1I1iIi :
  print 'there ><><><><><><><><><><><><'
  III1 = III1
  Ii1i = re . compile ( '<p><a href=".+?" rel=".+?">(.+?)</a>.+?<br /><a href=".+?">(.+?)</a>.+?</p>' , re . DOTALL ) . findall ( str ( IIii11Ii1i1I ) )
  for ooo , o0O00oOOoo in Ii1i :
   print 'here <><><><><><><><><><><><>'
   II1I ( '[COLORred]' + III1 + '[/COLOR] - ' + ooo + ' - [COLORgreen]' + o0O00oOOoo + '[/COLOR]' , i1111 ( 'aHR0cDovL3d3dy5wb2dkZXNpZ24uY28udWsvY2F0Lw==' ) , 10070 , ooOooo000oOO + 'loader.png' , i1iiIII111ii , '' )
   if 76 - 76: o0o00Oo0O + ooOoO0O00 . I1ii11iIi11i * oOo0O0Ooo * Ii11Ii1I
   if 14 - 14: I11i % o0o00Oo0O * o0oOO0O00o0O + Ii11Ii1I + I1ii11iIi11i * Ii11Ii1I
   if 3 - 3: OOooOOo * I1ii11iIi11i
def oOoO00oo0O ( url ) :
 o00OO00OoO = iiI111I1iIiI ( url )
 i1I1iIi = re . compile ( '<li class="yt-uix-scroller-scroll-unit "(.+?)</li>' , re . DOTALL ) . findall ( o00OO00OoO )
 for i1I1iIi in i1I1iIi :
  ooo = re . compile ( 'data-video-title="(.+?)"' ) . findall ( str ( i1I1iIi ) )
  for ooo in ooo :
   ooo = ( ooo ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&' , '&' )
  url = re . compile ( '<a href="/w(.+?)&' ) . findall ( str ( i1I1iIi ) )
  for url in url :
   url = 'https://www.youtube.com/w' + url
  oooiiI = re . compile ( '<img.+?="(.+?)"' ) . findall ( str ( i1I1iIi ) )
  for oooiiI in oooiiI :
   oooiiI = 'http:' + oooiiI
  ooOOoooooo ( '[COLORgreen]' + ooo + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , oooiiI , '' , '' )
  if 56 - 56: I1ii11iIi11i . Ii1I . oOo0O0Ooo
  if 39 - 39: o0o00Oo0O + IIIi
  if 91 - 91: ii - iI11I1II1I1I + OOooOOo / oO0o . OOooOOo + o0o00Oo0O
  if 26 - 26: Ii1I - ii
def iiI1iI111ii1i ( url ) :
 if 32 - 32: IIiIiII11i * OOooOOo % ooOoO0O00 - o0oOO0O00o0O + iI11I1II1I1I + Ii1I
 OO0O0Oo000 = [ ]
 o00OO00OoO = iiI111I1iIiI ( url )
 Ii1i = re . compile ( '<div class="explore-list">.+?<div class="el-img"><a href="(.+?)" class=".+?"><img src="(.+?)" alt=".+?<h3>(.+?)</h3><p>(.+?)</p></div>' , re . DOTALL ) . findall ( o00OO00OoO )
 for ooo0O0o00O , I1II1I11I1I , ooo , iiI11i1II in Ii1i :
  ooo = ( ooo ) . replace ( '&#039;' , '\'' ) . replace ( '&' , '&' ) . replace ( '&quot;' , '"' )
  OOOO0OOoO0O0 = iiI111I1iIiI ( ooo0O0o00O )
  I1 = re . compile ( '<!-- # player # -->.+?<iframe title=".+?".+?src="http://www.youtube.com/embed/(.+?)?autohide.+?<!-- detail box -->(.+?)</div>' , re . DOTALL ) . findall ( OOOO0OOoO0O0 )
  for OO0O0OOo0O , I1o0OooOOOOOO in I1 :
   OOooO0o0 = re . compile ( '<p>(.+?)</p>' , re . DOTALL ) . findall ( str ( I1o0OooOOOOOO ) )
   for iiIII1i in OOooO0o0 :
    if ooo in OO0O0Oo000 :
     pass
    else :
     ooOOoooooo ( ooo , OO0O0OOo0O , 8043 , I1II1I11I1I , I1II1I11I1I , iiIII1i )
     iiO0o0oOOOoOo ( 'movies' , 'INFO' )
     OO0O0Oo000 . append ( ooo )
     if 31 - 31: o0oOO0O00o0O . IIIii1II1II - O0OoO . ii / ii
     if 56 - 56: oO0o / OoOo00o / Ii + ii - I1ii11iIi11i - iI1iI1I1i1I
def Iii1iiIi1II ( url ) :
 OO0O00oOo = ii1II ( url )
 Ii1i = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( OO0O00oOo )
 for url , iI1IOooOoOo , iiIII1i , III1I1Iii1iiI , ooo in Ii1i :
  II1I ( ooo , url , 10065 , iI1IOooOoOo , III1I1Iii1iiI , iiIII1i )
 iiO0o0oOOOoOo ( 'movies' , 'INFO' )
 if 17 - 17: Ii11Ii1I % iI11I1II1I1I - iI11I1II1I1I
def O0o0O0 ( ) :
 IIiI1i1i = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 O00Oo0 = 'https://www.youtube.com/results?search_query=' + ( IIiI1i1i ) . replace ( ' ' , '+' )
 IiII111i1i11 = O00Oo0 . lower ( )
 o00OO00OoO = iiI111I1iIiI ( IiII111i1i11 )
 Ii1i = re . compile ( '<img src="(.+?)" alt=.+?yt-lockup-title "><a href="(.+?)".+?data-sessionlink=.+?" title="(.+?)".+?<span class="accessible-description".+?>(.+?)</span>.+?<div class="yt-lockup-description yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr">(.+?)</div>' , re . DOTALL ) . findall ( o00OO00OoO )
 next = re . compile ( '<a href="(.+?)" class="yt-uix-button.+?class="yt-uix-button-content">Next.+?</span></a>' ) . findall ( o00OO00OoO )
 for Ii1II1I11i1 in next :
  Ii1II1I11i1 = 'https://www.youtube.com' + Ii1II1I11i1
  II1I ( '[COLORgreen] NEXT [/COLOR]' , Ii1II1I11i1 , 10065 , ooOooo000oOO + 'Next.png' , i1iiIII111ii , '' )
 for I1II1I11I1I , Ii1II1I11i1 , ooo , oOoooooOoO , I1o0OooOOOOOO in Ii1i :
  II11iiii1Ii . append ( ooo )
  iiO0o0oOOOoOo ( 'tvshows' , 'INFO' )
  oooiiI = 'http:' + ( I1II1I11I1I ) . replace ( 'https:' , '' )
  print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>' + oooiiI
  Ii1II1I11i1 = 'http://www.youtube.com' + Ii1II1I11i1
  ooOOoooooo ( '[COLORred]' + oOoooooOoO + '[/COLOR]' + '[COLORgreen]' + ooo + '[/COLOR]' , ( Ii1II1I11i1 ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , oooiiI , oooiiI , I1o0OooOOOOOO )
 else :
  Ii1i = re . compile ( '<img src="(.+?)" alt=.+?yt-lockup-title "><a href="(.+?)".+?data-sessionlink=.+?" title="(.+?)".+?<span class="accessible-description".+?>(.+?)</span>' , re . DOTALL ) . findall ( o00OO00OoO )
  for I1II1I11I1I , Ii1II1I11i1 , ooo , oOoooooOoO in Ii1i :
   print 'im doing it'
   iiO0o0oOOOoOo ( 'tvshows' , 'INFO' )
   oooiiI = 'http:' + ( I1II1I11I1I ) . replace ( 'https:' , '' )
   Ii1II1I11i1 = 'http://www.youtube.com' + Ii1II1I11i1
   if '&' in Ii1II1I11i1 :
    print ' i got here'
    o00OO00OoO = iiI111I1iIiI ( Ii1II1I11i1 )
    i1I1iIi = re . compile ( '<li class="yt-uix-scroller-scroll-unit "(.+?)</li>' , re . DOTALL ) . findall ( o00OO00OoO )
    for i1I1iIi in i1I1iIi :
     ooo = re . compile ( 'data-video-title="(.+?)"' ) . findall ( str ( i1I1iIi ) )
     for ooo in ooo :
      ooo = ( ooo ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&' , '&' )
     Ii1II1I11i1 = re . compile ( '<a href="/w(.+?)&' ) . findall ( str ( i1I1iIi ) )
     for Ii1II1I11i1 in Ii1II1I11i1 :
      Ii1II1I11i1 = 'https://www.youtube.com/w' + Ii1II1I11i1
     oooiiI = re . compile ( '<img.+?="(.+?)"' ) . findall ( str ( i1I1iIi ) )
     for oooiiI in oooiiI :
      oooiiI = 'http:' + oooiiI
     ooOOoooooo ( '[COLORred]' + oOoooooOoO + '[/COLOR]' + '[COLORgreen]' + ooo + '[/COLOR]' , ( Ii1II1I11i1 ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , oooiiI , i1iiIII111ii , '' )
   elif ooo in II11iiii1Ii :
    pass
   elif 'user' in Ii1II1I11i1 or 'elete' in ooo :
    pass
   elif 'hannel' in Ii1II1I11i1 :
    print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' + Ii1II1I11i1
    o00OO00OoO = iiI111I1iIiI ( Ii1II1I11i1 )
    Ii111 = re . compile ( 'data-thumb="(.+?)".+?href="(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( o00OO00OoO )
    for I1II1I11I1I , Ii1II1I11i1 , ooo in Ii111 :
     if 'outube' in Ii1II1I11i1 or 'list' in Ii1II1I11i1 :
      pass
     elif 'atch' in Ii1II1I11i1 :
      Ii1II1I11i1 = ( Ii1II1I11i1 ) . replace ( '/watch?v=' , '' )
      ooOOoooooo ( '[COLORred]' + oOoooooOoO + '[/COLOR]' + '[COLORgreen]' + ooo + '[/COLOR]' , ( Ii1II1I11i1 ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , 'http:' + I1II1I11I1I , 'http:' + I1II1I11I1I , '' )
     else :
      pass
   else :
    ooOOoooooo ( '[COLORred]' + oOoooooOoO + '[/COLOR]' + '[COLORgreen]' + ooo + '[/COLOR]' , ( Ii1II1I11i1 ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , oooiiI , oooiiI , '' )
    if 10 - 10: IIIi % OooO0OoOOOO * OooO0OoOOOO . iI1iI1I1i1I / Ii11Ii1I % IIIii1II1II
def IIII1 ( url ) :
 o00OO00OoO = iiI111I1iIiI ( url )
 Ii1i = re . compile ( '<img src="(.+?)" alt=.+?yt-lockup-title "><a href="(.+?)".+?data-sessionlink=.+?" title="(.+?)".+?<span class="accessible-description".+?>(.+?)</span>.+?<div class="yt-lockup-description yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr">(.+?)</div>' , re . DOTALL ) . findall ( o00OO00OoO )
 next = re . compile ( '<a href="(.+?)" class="yt-uix-button.+?class="yt-uix-button-content">Next.+?</span></a>' ) . findall ( o00OO00OoO )
 for url in next :
  url = 'https://www.youtube.com' + url
  II1I ( '[COLORgreen] NEXT [/COLOR]' , url , 10065 , ooOooo000oOO + 'Next.png' , i1iiIII111ii , '' )
 for I1II1I11I1I , url , ooo , oOoooooOoO , I1o0OooOOOOOO in Ii1i :
  II11iiii1Ii . append ( ooo )
  iiO0o0oOOOoOo ( 'tvshows' , 'INFO' )
  oooiiI = 'http:' + ( I1II1I11I1I ) . replace ( 'https:' , '' )
  print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>' + oooiiI
  url = 'http://www.youtube.com' + url
  ooOOoooooo ( '[COLORred]' + oOoooooOoO + '[/COLOR]' + '[COLORgreen]' + ooo + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , oooiiI , oooiiI , I1o0OooOOOOOO )
 else :
  Ii1i = re . compile ( '<img src="(.+?)" alt=.+?yt-lockup-title "><a href="(.+?)".+?data-sessionlink=.+?" title="(.+?)".+?<span class="accessible-description".+?>(.+?)</span>' , re . DOTALL ) . findall ( o00OO00OoO )
  for I1II1I11I1I , url , ooo , oOoooooOoO in Ii1i :
   iiO0o0oOOOoOo ( 'tvshows' , 'INFO' )
   oooiiI = 'http:' + ( I1II1I11I1I ) . replace ( 'https:' , '' )
   url = 'http://www.youtube.com' + url
   if '&' in url :
    o00OO00OoO = iiI111I1iIiI ( url )
    i1I1iIi = re . compile ( '<li class="yt-uix-scroller-scroll-unit "(.+?)</li>' , re . DOTALL ) . findall ( o00OO00OoO )
    for i1I1iIi in i1I1iIi :
     ooo = re . compile ( 'data-video-title="(.+?)"' ) . findall ( str ( i1I1iIi ) )
     for ooo in ooo :
      ooo = ( ooo ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&' , '&' )
     url = re . compile ( '<a href="/w(.+?)&' ) . findall ( str ( i1I1iIi ) )
     for url in url :
      url = 'https://www.youtube.com/w' + url
     oooiiI = re . compile ( '<img.+?="(.+?)"' ) . findall ( str ( i1I1iIi ) )
     for oooiiI in oooiiI :
      oooiiI = 'http:' + oooiiI
     ooOOoooooo ( '[COLORred]' + oOoooooOoO + '[/COLOR]' + '[COLORgreen]' + ooo + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , oooiiI , i1iiIII111ii , '' )
   elif ooo in II11iiii1Ii :
    pass
   elif 'user' in url or 'elete' in ooo :
    pass
   elif 'hannel' in url :
    print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' + url
    o00OO00OoO = iiI111I1iIiI ( url )
    Ii111 = re . compile ( 'data-thumb="(.+?)".+?href="(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( o00OO00OoO )
    for I1II1I11I1I , url , ooo in Ii111 :
     if 'outube' in url or 'list' in url :
      pass
     elif 'atch' in url :
      url = ( url ) . replace ( '/watch?v=' , '' )
      ooOOoooooo ( '[COLORred]' + oOoooooOoO + '[/COLOR]' + '[COLORgreen]' + ooo + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , 'http:' + I1II1I11I1I , 'http:' + I1II1I11I1I , '' )
     else :
      pass
   else :
    ooOOoooooo ( '[COLORred]' + oOoooooOoO + '[/COLOR]' + '[COLORgreen]' + ooo + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , oooiiI , oooiiI , '' )
    if 10 - 10: IIIi / O0OoO + Ii / Ii11Ii1I
    if 74 - 74: IIIii1II1II + o0o00Oo0O + ooOoO0O00 - ooOoO0O00 + IIiIiII11i
def oOOO0oo0 ( ) :
 if oo0o0O00 == 'insert_password' :
  oOOoo00O0O . ok ( '[COLORgreen]Donators Login[/COLOR]' , 'You need to set username and password to access this' , 'These are unique and provided to donators to help with server and stream costs' , 'Donate @ [COLORgreen]http://architects.x10host.com[/COLOR]' )
  o0oO0 . openSettings ( sys . argv [ 0 ] )
 else :
  iIi1i1iIi1iI = open ( iIi1ii1I1 )
  Ii1i = re . compile ( 'plugin.video.GenieTv.+?2Flive%2F(.+?)%2F(.+?)%2F' ) . findall ( str ( iIi1i1iIi1iI ) )
  for iiIi1iI1iIii , o00OooO0oo in Ii1i :
   if iiIi1iI1iIii == 'needs replacing' or o00OooO0oo == 'needs replacing' :
    o0o0oOoOO0O ( )
  II1I ( '[COLORgreen]DONATORS LIST[/COLOR]' , str ( Ii1iIiII1ii1 ) + '/thelistnew.m3u' , 7080 , ooOooo000oOO + 'GTVIPTV.png' , i1iiIII111ii , '' )
  if 16 - 16: OooO0OoOOOO % iI11I1II1I1I . Ii11Ii1I
def oooooOOO000Oo ( ) :
 i1iiIIiiI111 . ok ( '[COLOR=white]ReCreate Addons.ini[/COLOR]' , 'If it doesnt work ensure login details are correct and retry' , '' , 'This will allow access to streams in guide without linking to favourites' )
 xbmc . executebuiltin ( "XBMC.RunScript(" + OO0o + ")" )
 o0o0oOoOO0O ( )
 i1iiIIiiI111 . ok ( '[COLOR=yellow]Done[/COLOR]' , 'Done' , 'Easy as that' , 'Now Go to guide and it should link your GTV streams' )
 if 52 - 52: IIiIiII11i % OooO0OoOOOO . OOooOOo * iI11I1II1I1I
def I111i1II ( ) :
 try :
  O0ooooo0OOOO0 = gui . TVGuide ( )
  O0ooooo0OOOO0 . doModal ( )
  del O0ooooo0OOOO0
  if 9 - 9: IIiIiII11i - I11i / o0oOO0O00o0O / I11i
 except :
  import sys
  import traceback as tb
  ( I1i111iiIIIi , O00 , traceback ) = sys . exc_info ( )
  tb . print_exception ( I1i111iiIIIi , O00 , traceback )
  if 17 - 17: Ii11Ii1I - ii % Ii11Ii1I . OooO0OoOOOO / Ii % o0oOO0O00o0O
def iIiIIIIIii ( ) :
 II1I ( 'Full Backup' , '' , 10061 , ooOooo000oOO + 'Backup.png' , i1iiIII111ii , 'Back Up Your Full System' )
 if os . path . exists ( I1IIIii ) :
  II1I ( 'Backup Genie Favourites' , Ii1II1I11i1 , 10062 , ooOooo000oOO + 'Backup.png' , i1iiIII111ii , 'Back Up Your favourites' )
 if os . path . exists ( ooooooO0oo ) :
  II1I ( 'Backup Ivue Config' , ooooooO0oo , 10062 , ooOooo000oOO + 'Backup.png' , i1iiIII111ii , 'Back Up Your master.db' )
 if os . path . exists ( IIiiiiiiIi1I1 ) :
  II1I ( 'Backup Kodi Favourites' , IIiiiiiiIi1I1 , 10062 , ooOooo000oOO + 'Backup.png' , i1iiIII111ii , 'Back Up Your favourites.xml' )
  if 58 - 58: I11i / OooO0OoOOOO . OOooOOo / ii + IIIi
  if 86 - 86: iI1iI1I1i1I * oOo0O0Ooo + iI1iI1I1i1I + IIiIiII11i
  if 8 - 8: IIIi - o0oOO0O00o0O / O0OoO
zip = o0oO0 . getSetting ( 'zip' )
oo0oOoo = xbmc . translatePath ( os . path . join ( zip ) )
def oOOO0o00o ( ) :
 iI11 = xbmc . translatePath ( os . path . join ( zip , 'testCBFolder' ) )
 if not os . path . exists ( zip ) :
  i1iiIIiiI111 . ok ( '[COLOR=white]Origin[/COLOR]' , 'The download location you have stored does not exist .\nPlease update the addon settings and try again.' , '' , '' )
  o0oO0 . openSettings ( sys . argv [ 0 ] )
  if 96 - 96: IIIii1II1II
  if 85 - 85: I11i . OOooOOo / O0OoO . o0o00Oo0O % IIIi
  if 90 - 90: I1ii11iIi11i % o0o00Oo0O * iI11I1II1I1I . o0oOO0O00o0O
def I1iii11 ( name , url , description ) :
 if 'Backup' in name :
  if 'Genie' in name :
   url = I1IIIii
  elif 'Ivue' in name :
   url = ooooooO0oo
  elif 'Kodi' in name :
   url = IIiiiiiiIi1I1
  oOOO0o00o ( )
  ooo0OiII1iii = open ( url ) . read ( )
  i11i1iiiII = os . path . join ( oo0oOoo , description . split ( 'Your ' ) [ 1 ] )
  ooOO0oO0oo00o = open ( i11i1iiiII , mode = 'w' )
  ooOO0oO0oo00o . write ( ooo0OiII1iii )
  ooOO0oO0oo00o . close ( )
 else :
  if 'guisettings.xml' in description :
   oOOo0oo0O = open ( os . path . join ( oo0oOoo , description . split ( 'Your ' ) [ 1 ] ) ) . read ( )
   IiiIiI1Ii1i = '<setting type="(.+?)" name="%s.(.+?)">(.+?)</setting>' % skin
   Ii1i = re . compile ( IiiIiI1Ii1i ) . findall ( oOOo0oo0O )
   for type , i1iIi , iiiii1II in Ii1i :
    iiiii1II = iiiii1II . replace ( '&quot;' , '' ) . replace ( '&' , '&' )
    xbmc . executebuiltin ( "Skin.Se	t%s(%s,%s)" % ( type . title ( ) , i1iIi , iiiii1II ) )
  else :
   i11i1iiiII = os . path . join ( url )
   ooo0OiII1iii = open ( os . path . join ( oo0oOoo , description . split ( 'Your ' ) [ 1 ] ) ) . read ( )
   ooOO0oO0oo00o = open ( i11i1iiiII , mode = 'w' )
   ooOO0oO0oo00o . write ( ooo0OiII1iii )
   ooOO0oO0oo00o . close ( )
 i1iiIIiiI111 . ok ( "[COLOR=white]Origin[/COLOR]" , "" , 'All Done !' , '' )
 if 81 - 81: Ii11Ii1I * I11i + IIIi + I1ii11iIi11i - ii
 if 32 - 32: Ii11Ii1I * o0o00Oo0O
 if 100 - 100: O0OoO % iI11I1II1I1I * IIiIiII11i - o0oOO0O00o0O
 if 92 - 92: O0OoO
def II11iI111i1 ( ) :
 Oo00OoOo = 1
 oOOO0o00o ( )
 ii1ii111 = xbmc . translatePath ( os . path . join ( oo0oOoo , 'Build Backup' , 'Full Backup' , '' ) )
 i11111I1I = xbmc . translatePath ( os . path . join ( oo0oOoo , 'Build Backup' , 'my_full_backup.zip' ) )
 ii1 = xbmc . translatePath ( os . path . join ( oo0oOoo , 'Build Backup' , 'my_full_backup_GUI_Settings.zip' ) )
 if not os . path . exists ( ii1ii111 ) :
  os . makedirs ( ii1ii111 )
 Oo0000oOo = oOOoo00O0O . input ( 'Enter a name for this backup' , type = xbmcgui . INPUT_ALPHANUM )
 if ( not Oo0000oOo ) : return False , 0
 I11o0oO00oO0o0o0 = Oo0000oOo
 I1I = xbmc . translatePath ( os . path . join ( ii1ii111 , I11o0oO00oO0o0o0 + '.zip' ) )
 ooooo = [ 'plugin.video.GenieTv' ]
 i11IIIiI1I = [ "xbmc.log" , "xbmc.old.log" , "kodi.log" , "kodi.old.log" , '.DS_Store' , '.setup_complete' , 'XBMCHelper.conf' ]
 o0iiiI1I1iIIIi1 = [ 'plugin.video.GenieTv' , 'repository.origin' , 'cache' , 'system' , 'Thumbnails' , "peripheral_data" , 'library' , 'keymaps' ]
 Iii = [ "xbmc.log" , "xbmc.old.log" , "kodi.log" , "kodi.old.log" , "Textures13.db" , '.DS_Store' , '.setup_complete' , 'XBMCHelper.conf' , 'advancedsettings.xml' ]
 I1iiiiI1iI = "Creating full backup of existing build"
 iIiiiii1i = "Creating Community Build"
 iiIi1IIiI = "Archiving..."
 i1oO0OO0 = ""
 o0O0Oo00 = "Please Wait"
 O0Oo0o000oO ( oooOOOOO , I1I , iIiiiii1i , iiIi1IIiI , i1oO0OO0 , o0O0Oo00 , o0iiiI1I1iIIIi1 , Iii )
 time . sleep ( 1 )
 oO0o00oOOooO0 = xbmc . translatePath ( os . path . join ( ii1ii111 , I11o0oO00oO0o0o0 + '_guisettings.zip' ) )
 OOOoO000 = zipfile . ZipFile ( oO0o00oOOooO0 , mode = 'w' )
 try :
  OOOoO000 . write ( xbmc . translatePath ( os . path . join ( oooOOOOO , 'userdata' , 'profiles.xml' ) ) , 'profiles.xml' , zipfile . ZIP_DEFLATED )
 except : pass
 OOOoO000 . close ( )
 if Oo00OoOo == 0 :
  i1iiIIiiI111 . ok ( "FAILED!" , 'The guisettings.xml file could not be found on your' , 'system, please reboot and try again.' , '' )
 else :
  i1iiIIiiI111 . ok ( "SUCCESS!" , 'You Are Now Backed Up. If you\'d like to share this build with' , 'the community please post details on the forum at' , '[COLOR=blue][B]http://rh-project.info[/COLOR][/B]' )
  i1iiIIiiI111 . ok ( "Build Locations" , 'Full Backup (only used to restore on this device): [COLOR=yellow]' + i11111I1I , '[/COLOR]Universal Backup (can be used on any device): [COLOR=yellow]' + I1I + '[/COLOR]' )
  if 57 - 57: IIiIiII11i
def O0Oo0o000oO ( sourcefile , destfile , message_header , message1 , message2 , message3 , exclude_dirs , exclude_files ) :
 oOOOoo = zipfile . ZipFile ( destfile , 'w' , zipfile . ZIP_DEFLATED )
 Ii1ii111i1 = len ( sourcefile )
 i1i1i1I = [ ]
 oOoo000 = [ ]
 Oo0oO0ooo . create ( message_header , message1 , message2 , message3 )
 for OooOo00o , IiI11i1IIiiI , oOOo000oOoO0 in os . walk ( sourcefile ) :
  for file in oOOo000oOoO0 :
   oOoo000 . append ( file )
 OoOo00o0OO = len ( oOoo000 )
 for OooOo00o , IiI11i1IIiiI , oOOo000oOoO0 in os . walk ( sourcefile ) :
  IiI11i1IIiiI [ : ] = [ ii1IIIIiI11 for ii1IIIIiI11 in IiI11i1IIiiI if ii1IIIIiI11 not in exclude_dirs ]
  oOOo000oOoO0 [ : ] = [ ooOO0oO0oo00o for ooOO0oO0oo00o in oOOo000oOoO0 if ooOO0oO0oo00o not in exclude_files ]
  for file in oOOo000oOoO0 :
   i1i1i1I . append ( file )
   iI1IIIii = len ( i1i1i1I ) / float ( OoOo00o0OO ) * 100
   Oo0oO0ooo . update ( int ( iI1IIIii ) , "Backing Up" , '[COLOR yellow]%s[/COLOR]' % file , 'Please Wait' )
   I1i11ii11 = os . path . join ( OooOo00o , file )
   if not 'temp' in IiI11i1IIiiI :
    if not 'plugin.program.originwizard' in IiI11i1IIiiI :
     import time
     OO00O0oOO = '01/01/1980'
     Ii1iI111 = time . strftime ( '%d/%m/%Y' , time . gmtime ( os . path . getmtime ( I1i11ii11 ) ) )
     if Ii1iI111 > OO00O0oOO :
      oOOOoo . write ( I1i11ii11 , I1i11ii11 [ Ii1ii111i1 : ] )
 oOOOoo . close ( )
 Oo0oO0ooo . close ( )
 if 51 - 51: OooO0OoOOOO * o0o00Oo0O / IIiIiII11i . Ii11Ii1I % IIIii1II1II / oOo0O0Ooo
 if 9 - 9: oOo0O0Ooo % oOo0O0Ooo % IIiIiII11i
def I1I1i1I ( ) :
 O0O0O0OoOO ( )
 II1I ( '[COLORgreen]SCOOBY STREAMS[/COLOR]' , ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvdHZjYXRzLnBocA==' ) ) , 1016 , ooOooo000oOO + 'scoob.png' , i1iiIII111ii , '' )
 II1I ( '[COLORgreen]SCOOBY SCRAPES[/COLOR]' , ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvc2NyYXBlZC9jYXRzLnBocA==' ) ) , 1024 , ooOooo000oOO + 'scoob.png' , i1iiIII111ii , '' )
 if 87 - 87: o0o00Oo0O / iI11I1II1I1I * ooOoO0O00
 if 41 - 41: OOooOOo * iI1iI1I1i1I / OOooOOo % OoOo00o
def IioO0oOOO0Ooo ( ) :
 O0O0O0OoOO ( )
 II1I ( '[COLORgreen]SEARCH MOVIES[/COLOR]' , str ( Ii1iIiII1ii1 ) , 9001 , ooOooo000oOO + 'MOVIESv.png' , i1iiIII111ii , '' )
 II1I ( '[COLORgreen]SEARCH SERIES[/COLOR]' , str ( Ii1iIiII1ii1 ) , 9002 , ooOooo000oOO + 'TVSHOWSv.png' , i1iiIII111ii , '' )
 II1I ( '[COLORgreen]SEARCH CARTOONS[/COLOR]' , '' , 10005 , ooOooo000oOO + 'ORIGINCARTOON' , i1iiIII111ii , '' )
 if 38 - 38: oOo0O0Ooo
 if 84 - 84: OoOo00o % ooOoO0O00
 if 70 - 70: I1ii11iIi11i . ii - o0oOO0O00o0O
 if 30 - 30: Ii1I % oOo0O0Ooo
def O0Oo00 ( ) :
 O0O0O0OoOO ( )
 II1I ( '[COLORgreen]RADIO[/COLOR]' , str ( Ii1iIiII1ii1 ) , 1013 , ooOooo000oOO + 'radio.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'CONCERTS' ) == 'true' :
  II1I ( '[COLORgreen]CONCERTS[/COLOR]' , ( i1111 ( 'aHR0cHM6Ly93d3cucmVkZGl0LmNvbS9yL2Z1bGxjb25jZXJ0cy8=' ) ) , 7050 , ooOooo000oOO + 'concerts.png' , i1iiIII111ii , '' )
  if 41 - 41: iI11I1II1I1I % iI1iI1I1i1I
 II1I ( '[COLORgreen]MUSIC VIDEOS[/COLOR]' , ( i1111 ( 'aHR0cDovLzE3Ni45LjE5Mi4yMjEvbXA0Lw==' ) ) , 1032 , ooOooo000oOO + 'musicvideos.png' , i1iiIII111ii , '' )
 II1I ( '[COLORgreen]MUSIC[/COLOR]' , str ( Ii1iIiII1ii1 ) + ( i1111 ( 'L3ZvZC91cmxzL211c2ljLnBocA==' ) ) , 1010 , ooOooo000oOO + 'MUSIC.png' , i1iiIII111ii , '' )
 II1I ( '[COLORgreen]MUSIC SEARCH[/COLOR]' , str ( Ii1iIiII1ii1 ) , 1111 , ooOooo000oOO + 'search.png' , i1iiIII111ii , '' )
 II1I ( '[COLORgreen]KODIBLE AUDIO BOOKS[/COLOR]' , 'http://doremisa.com/audiobooks/' , 30000 , ooOooo000oOO + 'kodible.png' , i1iiIII111ii , '' )
 if 59 - 59: IIIii1II1II + Ii
 iiO0o0oOOOoOo ( 'movies' , 'MAIN' )
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
 iiO0o0oOOOoOo ( 'movies' , 'MAIN' )
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
 iiO0o0oOOOoOo ( 'movies' , 'MAIN' )
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
 iiO0o0oOOOoOo ( 'movies' , 'MAIN' )
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
 iiO0o0oOOOoOo ( 'movies' , 'MAIN' )
 if 66 - 66: oO0o
def oOO ( url ) :
 O000oo0O = iiI111I1iIiI ( I11I ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 Ii1i = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( O000oo0O )
 for ooo , url , iI1IOooOoOo , III1I1Iii1iiI , I1o0OooOOOOOO in Ii1i :
  II1I ( ooo , url , 5 , iI1IOooOoOo , III1I1Iii1iiI , I1o0OooOOOOOO )
 iiO0o0oOOOoOo ( 'movies' , 'MAIN' )
 if 6 - 6: Ii1I + OoOo00o
def Ii1iI11iI1 ( ) :
 O0O0O0OoOO ( )
 II1I ( '[COLORgreen]GOTHAM SKINS[/COLOR]' , str ( Ii1iIiII1ii1 ) , 36 , ooOooo000oOO + 'GSKIN.png' , i1iiIII111ii , '' )
 II1I ( '[COLORgreen]HELIX SKINS[/COLOR]' , str ( Ii1iIiII1ii1 ) , 37 , ooOooo000oOO + 'HSKIN.png' , i1iiIII111ii , '' )
 II1I ( '[COLORgreen]ISENGAARD SKINS[/COLOR]' , oooOOOOO , 38 , ooOooo000oOO + 'ISKIN.png' , i1iiIII111ii , '' )
 iiO0o0oOOOoOo ( 'movies' , 'MAIN' )
 if 5 - 5: iI11I1II1I1I
def OOo ( url ) :
 O000oo0O = iiI111I1iIiI ( str ( Ii1iIiII1ii1 ) + o00oO00 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 Ii1i = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( O000oo0O )
 for ooo , url , iI1IOooOoOo , III1I1Iii1iiI , I1o0OooOOOOOO in Ii1i :
  II1I ( ooo , url , 42 , iI1IOooOoOo , III1I1Iii1iiI , I1o0OooOOOOOO )
 iiO0o0oOOOoOo ( 'movies' , 'MAIN' )
 if 59 - 59: IIIii1II1II + iI11I1II1I1I * I11i + IIIi . o0oOO0O00o0O
def IiI1iII1II111 ( url ) :
 O000oo0O = iiI111I1iIiI ( str ( Ii1iIiII1ii1 ) + IIiI11i1111Ii ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 Ii1i = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( O000oo0O )
 for ooo , url , iI1IOooOoOo , III1I1Iii1iiI , I1o0OooOOOOOO in Ii1i :
  II1I ( ooo , url , 42 , iI1IOooOoOo , III1I1Iii1iiI , I1o0OooOOOOOO )
 iiO0o0oOOOoOo ( 'movies' , 'MAIN' )
 if 63 - 63: IIIii1II1II + O0OoO
def O0ooOOO0 ( url ) :
 O000oo0O = iiI111I1iIiI ( str ( Ii1iIiII1ii1 ) + Ii11Iii1i1ii ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 Ii1i = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( O000oo0O )
 for ooo , url , iI1IOooOoOo , III1I1Iii1iiI , I1o0OooOOOOOO in Ii1i :
  II1I ( ooo , url , 42 , iI1IOooOoOo , III1I1Iii1iiI , I1o0OooOOOOOO )
 iiO0o0oOOOoOo ( 'movies' , 'MAIN' )
 if 26 - 26: IIiIiII11i % Ii % iI11I1II1I1I % iI1iI1I1i1I * iI1iI1I1i1I * Ii1I
def IiI1I11iIii ( url ) :
 O000oo0O = iiI111I1iIiI ( i1111 ( 'aHR0cHM6Ly9kbC5kcm9wYm94dXNlcmNvbnRlbnQuY29tL3MvN2ZrMjhndDlwb3QxMjJhL0JVSUxEUy50eHQ/ZGw9MA==' ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 Ii1i = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( O000oo0O )
 for ooo , url , iI1IOooOoOo , III1I1Iii1iiI , I1o0OooOOOOOO in Ii1i :
  II1I ( ooo , url , 42 , iI1IOooOoOo , III1I1Iii1iiI , I1o0OooOOOOOO )
 iiO0o0oOOOoOo ( 'movies' , 'MAIN' )
 if 63 - 63: o0oOO0O00o0O * iI1iI1I1i1I * Ii11Ii1I - OoOo00o - Ii11Ii1I
def o0oo ( url ) :
 O000oo0O = iiI111I1iIiI ( str ( Ii1iIiII1ii1 ) + oOoOoo0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 Ii1i = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( O000oo0O )
 for ooo , url , iI1IOooOoOo , III1I1Iii1iiI , I1o0OooOOOOOO in Ii1i :
  II1I ( ooo , url , 40 , iI1IOooOoOo , III1I1Iii1iiI , I1o0OooOOOOOO )
 iiO0o0oOOOoOo ( 'movies' , 'MAIN' )
 if 16 - 16: oOo0O0Ooo
def IIIII1iii ( url ) :
 O000oo0O = iiI111I1iIiI ( str ( Ii1iIiII1ii1 ) + IIiiii ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 Ii1i = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( O000oo0O )
 for ooo , url , iI1IOooOoOo , III1I1Iii1iiI , I1o0OooOOOOOO in Ii1i :
  II1I ( ooo , url , 5 , iI1IOooOoOo , III1I1Iii1iiI , I1o0OooOOOOOO )
 iiO0o0oOOOoOo ( 'movies' , 'MAIN' )
 if 37 - 37: I11i % O0OoO
def O0II11i11II ( ) :
 OO0O00oOo = ii1II ( i1111 ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby9hcGt0b29sL2Fway5waHA=' ) )
 Ii1i = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( OO0O00oOo )
 for Ii1II1I11i1 , oooiiI , ooo in Ii1i :
  II1Ii1iI1i1 ( ooo , Ii1II1I11i1 , 2031 , oooiiI )
  if 54 - 54: o0o00Oo0O
def OOoO000O00oO ( name , url , description ) :
 iI11 = xbmc . translatePath ( os . path . join ( i1OoOO , 'Download' ) )
 Oo0oO0ooo = xbmcgui . DialogProgress ( )
 Oo0oO0ooo . create ( "Your App Is Downloading" , "Why not check out our website" , '' , 'Http://architects.x10host.com' )
 iIII1I1i1i = os . path . join ( iI11 , name + '.apk' )
 try :
  os . remove ( iIII1I1i1i )
 except :
  pass
 downloader . download ( url , iIII1I1i1i , Oo0oO0ooo )
 i1iiIIiiI111 = xbmcgui . Dialog ( )
 i1iiIIiiI111 . ok ( "GenieTv" , "[COLORred]Please press ok, exit kodi and go to your downloads folder to install your app[/COLOR]" , "[COLORblue]Tool Brought To You By GenieTv[/COLOR]" )
 if 79 - 79: Ii11Ii1I . oO0o
def IIiI1I1 ( url ) :
 iI11 = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/resources/downloads' ) )
 Oo0oO0ooo = xbmcgui . DialogProgress ( )
 Oo0oO0ooo . create ( "Your fILM Is Downloading" , "Why not check out our website" , '' , 'Http://architects.x10host.com' )
 iIII1I1i1i = os . path . join ( iI11 , ooo + '.mp4' )
 try :
  os . remove ( iIII1I1i1i )
 except :
  pass
 downloader . download ( url , iIII1I1i1i , Oo0oO0ooo )
 i1iiIIiiI111 = xbmcgui . Dialog ( )
 i1iiIIiiI111 . ok ( "GenieTv" , "[COLORred]Please press ok, Your download With Be Avaiilable Via The My Downloads Button[/COLOR]" , "[COLORblue]Tool Brought To You By GenieTv[/COLOR]" )
 if 15 - 15: Ii11Ii1I * I1ii11iIi11i % Ii1I * iI11I1II1I1I - Ii
 if 60 - 60: oOo0O0Ooo * IIIi % oO0o + OoOo00o
def o0ooO00OOooo0Ooo ( name , url , description ) :
 iI11 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 Oo0oO0ooo = xbmcgui . DialogProgress ( )
 Oo0oO0ooo . create ( "Your Art Pack Is Downloading" , "Why not check out our website" , '' , 'Http://architects.x10host.com' )
 iIII1I1i1i = os . path . join ( iI11 , name )
 try :
  os . remove ( iIII1I1i1i )
 except :
  pass
 downloader . download ( url , iIII1I1i1i , Oo0oO0ooo )
 o0oOOoOOO = xbmc . translatePath ( os . path . join ( oo00 ) )
 time . sleep ( 2 )
 Oo0oO0ooo . update ( 0 , "" , "Placing Your Art Please Wait" )
 print '======================================='
 print o0oOOoOOO
 print '======================================='
 extract . all ( iIII1I1i1i , o0oOOoOOO , Oo0oO0ooo )
 i1iiIIiiI111 = xbmcgui . Dialog ( )
 i1iiIIiiI111 . ok ( "GenieTv" , "[COLORred]Once complete your artwork will be stored in your Media folder, Accessible via the Homefolder, Enjoy[/COLOR]" )
 if 32 - 32: ooOoO0O00 . iI1iI1I1i1I / oO0o
 if 85 - 85: iI1iI1I1i1I
def ooOoO0 ( url ) :
 O000oo0O = iiI111I1iIiI ( Ii1iIiII1ii1 + ( i1111 ( 'L0dlbmllVHYvdGVzdC93aC50eHQ=' ) ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 Ii1i = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( O000oo0O )
 for ooo , url , iI1IOooOoOo , III1I1Iii1iiI , I1o0OooOOOOOO in Ii1i :
  II1I ( ooo , url , 5 , iI1IOooOoOo , III1I1Iii1iiI , I1o0OooOOOOOO )
 iiO0o0oOOOoOo ( 'movies' , 'INFO' )
 if 86 - 86: I11i
 if 27 - 27: o0o00Oo0O . I11i . Ii1I . Ii1I + Ii1I * I11i
def oOo00oOOOOO ( url ) :
 O000oo0O = iiI111I1iIiI ( Ii1iIiII1ii1 + ( i1111 ( 'L0dlbmllVHYvdGVzdC93aC54bWw=' ) ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 Ii1i = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( O000oo0O )
 for ooo , url , iI1IOooOoOo , III1I1Iii1iiI , I1o0OooOOOOOO in Ii1i :
  II1I ( ooo , url , 30015 , iI1IOooOoOo , III1I1Iii1iiI , I1o0OooOOOOOO )
 iiO0o0oOOOoOo ( 'movies' , 'MAIN' )
 if 85 - 85: ii - oO0o - IIIi / O0OoO - iI1iI1I1i1I
def iIiI ( url , iconimage , fanart ) :
 O000oo0O = iiI111I1iIiI ( url )
 iiIi11iI1iii = url
 I1II1I11I1I = iconimage
 fanart = fanart
 Ii1i = re . compile ( 'href="(.+?)">(.+?)</a>' ) . findall ( O000oo0O )
 for ooo0O0o00O , ooo in Ii1i :
  if '.mp4' in ooo :
   ooOOoooooo ( 'Watch VIDEO' , url + '/' + ooo0O0o00O , 222 , I1II1I11I1I , fanart , '' )
  if 'description' in ooo :
   ooOOoooooo ( 'Read Description' , url + '/' + ooo0O0o00O , 30017 , I1II1I11I1I , fanart , '' )
  if 'images' in ooo :
   II1I ( 'View Images' , url + '/' + ooo0O0o00O , 30018 , I1II1I11I1I , fanart , '' )
  if 'url' in ooo :
   ooOOoooooo ( 'Install Build On Android' , url + '/' + ooo0O0o00O , 30016 , I1II1I11I1I , fanart , '' )
  if 'url' in ooo :
   ooOOoooooo ( 'Install Build On Pc' , url + '/' + ooo0O0o00O , 30019 , I1II1I11I1I , fanart , '' )
 iiO0o0oOOOoOo ( 'movies' , 'INFO' )
 if 5 - 5: I1ii11iIi11i * OOooOOo
def ii1I11iIiIII1 ( url ) :
 O000oo0O = iiI111I1iIiI ( url )
 Ii1i = re . compile ( 'url="(.+?)"' ) . findall ( O000oo0O )
 for url in Ii1i :
  oOO0OOOOoooO ( url )
  if 22 - 22: iI1iI1I1i1I + iI11I1II1I1I
def IIIii1iiIi ( url ) :
 O000oo0O = iiI111I1iIiI ( url )
 Ii1i = re . compile ( 'url="(.+?)"' ) . findall ( O000oo0O )
 for url in Ii1i :
  oooo0OOo ( url )
  if 72 - 72: o0o00Oo0O / O0OoO + ii * o0oOO0O00o0O
def OoOo0OOOoOo ( url ) :
 O000oo0O = iiI111I1iIiI ( url )
 Ii1i = re . compile ( 'desc="(.+?)"' ) . findall ( O000oo0O )
 for IIiiIIi1 in Ii1i :
  I1Ii ( 'Description:' , IIiiIIi1 )
  if 51 - 51: OOooOOo
def I11IIIiIi11 ( url ) :
 O000oo0O = iiI111I1iIiI ( url )
 url = url
 Ii1i = re . compile ( '<li><a href="(.+?)"> (.+?)</a></li>' ) . findall ( O000oo0O )
 for ooo0O0o00O , ooo in Ii1i :
  if 'png' in ooo :
   ooOOoooooo ( 'image' , '' , '' , url + ooo0O0o00O , url + '/' + ooo0O0o00O , '' )
 iiO0o0oOOOoOo ( 'movies' , 'MAIN' )
 if 39 - 39: Ii11Ii1I % o0o00Oo0O % OOooOOo . ooOoO0O00
def oOo00OooO0oO ( name , url , description ) :
 iI11 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 Oo0oO0ooo = xbmcgui . DialogProgress ( )
 Oo0oO0ooo . create ( "GenieTv" , "Downloading Content" , '' , 'Please Wait' )
 iIII1I1i1i = os . path . join ( iI11 , name + '.zip' )
 try :
  os . remove ( iIII1I1i1i )
 except :
  pass
 downloader . download ( url , iIII1I1i1i , Oo0oO0ooo )
 I1IIi = xbmc . translatePath ( os . path . join ( 'special://home' , 'addons' ) )
 time . sleep ( 2 )
 Oo0oO0ooo . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print I1IIi
 print '======================================='
 extract . all ( iIII1I1i1i , I1IIi , Oo0oO0ooo )
 i1iiIIiiI111 = xbmcgui . Dialog ( )
 i1iiIIiiI111 . ok ( "GenieTv" , "Press ok to finish install" , "[COLOR yellow]Brought To You By GenieTv[/COLOR]" )
 oooooo0O000o ( )
 if 69 - 69: Ii11Ii1I + I1ii11iIi11i + IIiIiII11i - oOo0O0Ooo / iI1iI1I1i1I
 if 74 - 74: iI1iI1I1i1I - IIIii1II1II + ooOoO0O00 . oOo0O0Ooo + IIIii1II1II - iI1iI1I1i1I
def oooo0OOo ( url ) :
 iI11 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 Oo0oO0ooo = xbmcgui . DialogProgress ( )
 Oo0oO0ooo . create ( "GenieTv" , "Downloading " , '' , 'Please Wait' )
 iIII1I1i1i = os . path . join ( iI11 , 'plugin.program.GenieTv.install' + '.zip' )
 try :
  os . remove ( iIII1I1i1i )
 except :
  pass
 downloader . download ( url , iIII1I1i1i , Oo0oO0ooo )
 I1IIi = xbmc . translatePath ( os . path . join ( 'special://' , 'home' ) )
 time . sleep ( 2 )
 Oo0oO0ooo . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print I1IIi
 print '======================================='
 extract . all ( iIII1I1i1i , I1IIi , Oo0oO0ooo )
 IiIiiiiI1 ( url )
 i1iiIIiiI111 = xbmcgui . Dialog ( )
 i1iiIIiiI111 . ok ( "GenieTv" , "Press ok to force close kodi, if unsuccessful using windows Please kill kodi via taskmanager" , "[COLOR yellow]Brought To You By GenieTv[/COLOR]" )
 OO00OOoO0o ( )
 if 4 - 4: ooOoO0O00 - Ii / Ii / ii
def oOO0OOOOoooO ( url ) :
 iI11 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 Oo0oO0ooo = xbmcgui . DialogProgress ( )
 Oo0oO0ooo . create ( "GenieTv" , "Downloading " , '' , 'Please Wait' )
 iIII1I1i1i = os . path . join ( iI11 , 'plugin.program.GenieTv.install' + '.zip' )
 try :
  os . remove ( iIII1I1i1i )
 except :
  pass
 downloader . download ( url , iIII1I1i1i , Oo0oO0ooo )
 I1IIi = xbmc . translatePath ( os . path . join ( 'special://' , 'home' ) )
 time . sleep ( 2 )
 Oo0oO0ooo . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print I1IIi
 print '======================================='
 extract . all ( iIII1I1i1i , I1IIi , Oo0oO0ooo )
 IiIiiiiI1 ( url )
 i1iiIIiiI111 = xbmcgui . Dialog ( )
 i1iiIIiiI111 . ok ( "GenieTv" , "Please Disconnect The Power From Your Device. DO NOT EXIT CLEANLY VIA SHUTDOWN" , "[COLOR yellow]Brought To You By GenieTv[/COLOR]" )
 if 100 - 100: I1ii11iIi11i + I11i - o0o00Oo0O % IIiIiII11i . o0oOO0O00o0O
 if 92 - 92: IIiIiII11i * ii - IIIi
def oooo00 ( name , url , description ) :
 I1IIi = xbmc . translatePath ( os . path . join ( 'special://' , 'home' ) )
 Oo0oO0ooo = xbmcgui . DialogProgress ( )
 iIII1I1i1i = os . path . join ( I11 )
 time . sleep ( 2 )
 Oo0oO0ooo . create ( "GenieTv" , "Restoring" , '' , 'Please Wait' )
 print '======================================='
 print I1IIi
 print '======================================='
 extract . all ( iIII1I1i1i , I1IIi , Oo0oO0ooo )
 i1iiIIiiI111 = xbmcgui . Dialog ( )
 i1iiIIiiI111 . ok ( "GenieTv" , "Please Disconnect The Power From Your Device. DO NOT EXIT CLEANLY VIA SHUTDOWN" , "[COLOR yellow]Brought To You By GenieTv[/COLOR]" )
 if 96 - 96: Ii1I % O0OoO % Ii11Ii1I - O0OoO % OOooOOo + Ii1I
 if 3 - 3: o0o00Oo0O
def OO00OOoO0o ( ) :
 O0O00Oo = xbmcgui . Dialog ( ) . yesno ( 'Force Close Kodi' , 'You are about to close Kodi' , 'Would you like to continue?' , nolabel = 'No, Cancel' , yeslabel = 'Yes, Close' )
 if O0O00Oo == 0 :
  return
 elif O0O00Oo == 1 :
  pass
 Ooo0Oo0oo0 = oOO0o000Oo00o ( )
 print "Platform: " + str ( Ooo0Oo0oo0 )
 if Ooo0Oo0oo0 == 'osx' :
  print "############   try osx force close  #################"
  try : os . system ( 'killall -9 XBMC' )
  except : pass
  try : os . system ( 'killall -9 Kodi' )
  except : pass
  i1iiIIiiI111 . ok ( "[COLOR=red][B]WARNING  !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu." , '' )
 elif Ooo0Oo0oo0 == 'linux' :
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
 elif Ooo0Oo0oo0 == 'android' :
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
 elif Ooo0Oo0oo0 == 'windows' :
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
  if 21 - 21: ii - iI11I1II1I1I
def oOO0o000Oo00o ( ) :
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
  if 93 - 93: OoOo00o - I11i % OOooOOo . OOooOOo - O0OoO
  if 90 - 90: O0OoO + IIiIiII11i * Ii1I / Ii11Ii1I . I11i + I11i
  if 40 - 40: O0OoO / OOooOOo % Ii % Ii1I / oOo0O0Ooo
def ooOOOOo0 ( url ) :
 Oo0oO0ooo . create ( "[COLOR=green]GenieTv[/COLOR]" , "Renaming paths..." , '' , 'Please Wait' )
 for IiiIi , IiI11i1IIiiI , oOOo000oOoO0 in os . walk ( url ) :
  for file in oOOo000oOoO0 :
   if file . endswith ( ".xml" ) :
    Oo0oO0ooo . update ( 0 , "Fixing" , file , 'Please Wait' )
    oOOo0oo0O = open ( ( os . path . join ( IiiIi , file ) ) ) . read ( )
    iIIi = oOOo0oo0O . replace ( oooOOOOO , 'special://home/' )
    ooOO0oO0oo00o = open ( ( os . path . join ( IiiIi , file ) ) , mode = 'w' )
    ooOO0oO0oo00o . write ( str ( iIIi ) )
    ooOO0oO0oo00o . close ( )
 OO00OOoO0o ( )
 if 96 - 96: o0oOO0O00o0O
def i1I11iIII1i1I ( ) :
 OO0O00oOo = ii1II ( i1111 ( 'aHR0cDovL3d3dy5saXN0ZW5saXZlLmV1L3VrLmh0bWw=' ) )
 Ii1i = re . compile ( '<tr>.+?<td><a href=".+?"><b>(.+?)</b>.+?<td><a href="(.+?)">' , re . DOTALL ) . findall ( OO0O00oOo )
 for ooo , Ii1II1I11i1 in Ii1i :
  oOO0oo ( ooo , Ii1II1I11i1 , 222 , ooOooo000oOO + 'radio.png' )
  if 13 - 13: ii * OoOo00o - Ii11Ii1I / IIIii1II1II + iI1iI1I1i1I + OooO0OoOOOO
def iii1III1i ( ) :
 OO0O00oOo = ii1II ( i1111 ( 'aHR0cDovL3d3dy50b29uamV0LmNvbS8=' ) )
 Ii1i = re . compile ( '<a href="(.+?)" style="font-size:.8em;">(.+?)</a>' ) . findall ( OO0O00oOo )
 for Ii1II1I11i1 , ooo in Ii1i :
  II1Ii1iI1i1 ( '[COLORgreen]' + ooo + '[/COLOR]' , 'http://www.toonjet.com/' + Ii1II1I11i1 , 8051 , ooOooo000oOO + 'classictoons.png' )
def iiiIi ( url ) :
 OO0O00oOo = ii1II ( url )
 Ii1i = re . compile ( '<a href="(.+?)"><img src="(.+?)"' ) . findall ( OO0O00oOo )
 I1 = re . compile ( '<a href="(.+?)">.+?</a></td></tr></table>' ) . findall ( OO0O00oOo )
 for url , I1II1I11I1I in Ii1i :
  if 'ol.gif' in I1II1I11I1I :
   pass
  elif 'link_block_' in I1II1I11I1I :
   pass
  elif '.png' in I1II1I11I1I :
   pass
  else :
   II1Ii1iI1i1 ( ( I1II1I11I1I ) . replace ( 'http://www.toonjet.com/images/icons/' , '' ) . replace ( 'images/icons/' , '' ) . replace ( '.jpg' , '' ) . replace ( '_icon' , '' ) . replace ( '_' , ' ' ) , 'http://www.toonjet.com/' + url , 8052 , ooOooo000oOO + 'vod.png' )
 for url in I1 :
  II1Ii1iI1i1 ( 'NEXT PAGE' , 'http://www.toonjet.com/' + url , 8051 , ooOooo000oOO + 'Next.png' )
def II1Iii ( url ) :
 OO0O00oOo = ii1II ( url )
 Ii1i = re . compile ( '<iframe width="640" height="480" src="(.+?)" frameborder="0" allowfullscreen></iframe>' ) . findall ( OO0O00oOo )
 for url in Ii1i :
  oOO0oo ( '[COLORgreen]PLAY[/COLOR]' , ( url ) . replace ( 'http://www.youtube.com/embed/' , '' ) . replace ( '?autoplay=0' , '' ) , 8043 , ooOooo000oOO + 'classictoons.png' )
  if 73 - 73: iI1iI1I1i1I * ii . o0o00Oo0O . OooO0OoOOOO
  if 55 - 55: I1ii11iIi11i
def ooO0o ( ) :
 ii1iI1iI1 ( 'Audio Books' , '' , 30011 , ooOooo000oOO + 'audiobooks.png' , ooOooo000oOO + 'audiobooks.png' , '' )
 ii1iI1iI1 ( 'Kids Audio Books' , '' , 30006 , ooOooo000oOO + 'kidsaudiobooks.png' , ooOooo000oOO + 'kidsaudiobooks.png' , '' )
 if 55 - 55: O0OoO + IIIii1II1II
def IIIIIiII1 ( ) :
 ii1iI1iI1 ( 'All' , '' , 30001 , ooOooo000oOO + 'kodible.png' , ooOooo000oOO + 'kodible.png' , '' )
 ii1iI1iI1 ( 'Popular' , '' , 30012 , ooOooo000oOO + 'POPULARv.png' , ooOooo000oOO + 'POPULARv.png' , '' )
 ii1iI1iI1 ( 'Search' , '' , 30013 , ooOooo000oOO + 'search.png' , ooOooo000oOO + 'search.png' , '' )
 if 45 - 45: oOo0O0Ooo / o0oOO0O00o0O . o0oOO0O00o0O
def i1oO ( ) :
 o00OO00OoO = iiI111I1iIiI ( OooO0 + 'books' + ooOoOoo0O )
 Ii1i = re . compile ( '<NAME=>(.*?)</NAME><URL=>(.*?)</URL><CAT=>(.*?)</CAT>' ) . findall ( o00OO00OoO )
 for ooo , Ii1II1I11i1 , iI in Ii1i :
  if 'Parent' in ooo :
   pass
  elif '2' in iI :
   ii1iI1iI1 ( ( ooo ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , Ii1II1I11i1 , 30010 , ooOooo000oOO + 'kodible.png' , ooOooo000oOO + 'kodible.png' , '' )
   if 42 - 42: ii + I1ii11iIi11i % IIiIiII11i + oO0o
def I11i11I1iiII ( ) :
 IIiI1i1i = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 IiII111i1i11 = IIiI1i1i . lower ( )
 o00OO00OoO = iiI111I1iIiI ( OooO0 + 'books' + ooOoOoo0O )
 Ii1i = re . compile ( '<NAME=>(.*?)</NAME><URL=>(.*?)</URL><CAT=>(.*?)</CAT>' ) . findall ( o00OO00OoO )
 for ooo , Ii1II1I11i1 , iI in Ii1i :
  if IIiI1i1i in ooo . lower ( ) :
   if '1' in iI :
    ii1iI1iI1 ( ( ooo ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , Ii1II1I11i1 , 30010 , ooOooo000oOO + 'kodible.png' , ooOooo000oOO + 'kodible.png' , '' )
   elif '2' in iI :
    ii1iI1iI1 ( ( ooo ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , Ii1II1I11i1 , 30010 , ooOooo000oOO + 'kodible.png' , ooOooo000oOO + 'kodible.png' , '' )
   elif '3' in iI :
    ii1iI1iI1 ( ( ooo ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , Ii1II1I11i1 , 30009 , ooOooo000oOO + 'kodible.png' , ooOooo000oOO + 'kodible.png' , '' )
    if 28 - 28: Ii / I11i . iI11I1II1I1I / IIiIiII11i
    if 72 - 72: ii / oOo0O0Ooo + Ii11Ii1I / OOooOOo * Ii11Ii1I
def Ii1iIi111i1i1 ( ) :
 o00OO00OoO = iiI111I1iIiI ( OooO0 + 'books' + ooOoOoo0O )
 Ii1i = re . compile ( '<NAME=>(.*?)</NAME><URL=>(.*?)</URL><CAT=>(.*?)</CAT>' ) . findall ( o00OO00OoO )
 for ooo , Ii1II1I11i1 , iI in Ii1i :
  if '1' in iI :
   ii1iI1iI1 ( ( ooo ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , Ii1II1I11i1 , 3010 , ooOooo000oOO + 'kodible.png' , ooOooo000oOO + 'kodible.png' , '' )
  elif '2' in iI :
   ii1iI1iI1 ( ( ooo ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , Ii1II1I11i1 , 30010 , ooOooo000oOO + 'kodible.png' , ooOooo000oOO + 'kodible.png' , '' )
  elif '3' in iI :
   ii1iI1iI1 ( ( ooo ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , Ii1II1I11i1 , 30009 , ooOooo000oOO + 'kodible.png' , ooOooo000oOO + 'kodible.png' , '' )
   if 45 - 45: OOooOOo . I11i % OOooOOo * oOo0O0Ooo % oOo0O0Ooo
 xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 63 - 63: IIIi
def oo00ooOoo ( url ) :
 ooo0O0o00O = url
 o00OO00OoO = iiI111I1iIiI ( url )
 I1 = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( o00OO00OoO )
 for url , ooo in I1 :
  if 'mp3' in ooo :
   II1I ( ( ooo ) . replace ( '%20' , ' ' ) , ooo0O0o00O + url , 10012 , ooOooo000oOO + 'kodible.png' , ooOooo000oOO + 'kodible.png' , '' )
  if 'wma' in ooo :
   II1I ( ( ooo ) . replace ( '%20' , ' ' ) , ooo0O0o00O + url , 10012 , ooOooo000oOO + 'kodible.png' , ooOooo000oOO + 'kodible.png' , '' )
  if 'm4b' in ooo :
   II1I ( ( ooo ) . replace ( '%20' , ' ' ) , ooo0O0o00O + url , 10012 , ooOooo000oOO + 'kodible.png' , ooOooo000oOO + 'kodible.png' , '' )
  elif '/' in ooo :
   ii1iI1iI1 ( ( ooo ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , ooo0O0o00O + url , 30009 , ooOooo000oOO + 'kodible.png' , ooOooo000oOO + 'kodible.png' , '' )
   if 28 - 28: Ii11Ii1I
   if 1 - 1: Ii11Ii1I
   if 48 - 48: o0o00Oo0O + o0o00Oo0O . IIIi - O0OoO
def o00oo0000 ( url ) :
 o00OO00OoO = iiI111I1iIiI ( url )
 ooo0O0o00O = url
 Ii1i = re . compile ( '<li><a href="(.+?)">(.+?)</a></li>' ) . findall ( o00OO00OoO )
 for url , ooo in Ii1i :
  if 'Parent' in ooo :
   pass
  elif '.db' in ooo :
   pass
  elif '.jpg' in ooo :
   pass
  elif '.html' in ooo :
   pass
  elif '.doc' in ooo :
   pass
  elif 'mp3' in ooo :
   II1I ( ( ooo ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , ooo0O0o00O + url , 10012 , ooOooo000oOO + 'kodible.png' , ooOooo000oOO + 'kodible.png' , '' )
  elif 'm4a' in ooo :
   II1I ( ( ooo ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , ooo0O0o00O + url , 10012 , ooOooo000oOO + 'kodible.png' , ooOooo000oOO + 'kodible.png' , '' )
  else :
   ii1iI1iI1 ( ( ooo ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , ooo0O0o00O + url , 30010 , ooOooo000oOO + 'kodible.png' , ooOooo000oOO + 'kodible.png' , '' )
   if 44 - 44: I1ii11iIi11i % iI11I1II1I1I
   if 90 - 90: IIiIiII11i + ii % ii
def I11Ii ( ) :
 ii1iI1iI1 ( 'A-Z' , '' , 7 , ooOooo000oOO + 'kodible.png' , ooOooo000oOO + 'kodible.png' , '' )
 ii1iI1iI1 ( 'All' , '' , 3 , ooOooo000oOO + 'kodible.png' , ooOooo000oOO + 'kodible.png' , '' )
 ii1iI1iI1 ( 'Search' , '' , 14 , ooOooo000oOO + 'kodible.png' , ooOooo000oOO + 'kodible.png' , '' )
 if 16 - 16: I1ii11iIi11i / Ii
def oo00IIIIIIIiI ( ) :
 o00OO00OoO = iiI111I1iIiI ( i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9tcDNfZG93bmxvYWRzLmh0bQ==' ) )
 Ii1i = re . compile ( '<td width=".+?" align="center">.+?<a href="(.*?)">.+?<img border="0" src="images/Squeeze%20(.*?).gif" width="74" height=".*?"></a></td>' , re . DOTALL ) . findall ( o00OO00OoO )
 for Ii1II1I11i1 , I1II1I11I1I in Ii1i :
  print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<' + Ii1II1I11i1 + '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
  if '-x' in I1II1I11I1I :
   pass
  else :
   ii1iI1iI1 ( I1II1I11I1I , ( i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) ) + ( Ii1II1I11i1 ) . replace ( 'colour_it' , 'books_audio/audio_books_a' ) , 30008 , ( i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9pbWFnZXMvU3F1ZWV6ZSUyMA==' ) ) + I1II1I11I1I + '.gif' , ooOooo000oOO + 'kodible.png' , '' )
   if 12 - 12: o0oOO0O00o0O . OooO0OoOOOO . OOooOOo / o0o00Oo0O
 xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 58 - 58: I11i - IIiIiII11i % OoOo00o + IIIi . OOooOOo / OooO0OoOOOO
 if 8 - 8: Ii1I . oO0o * iI1iI1I1i1I + IIiIiII11i % Ii
def i1i1IiIiIi1Ii ( url ) :
 o00OO00OoO = iiI111I1iIiI ( url )
 Ii1i = re . compile ( '<td width=".*?" height=".*?"><b>.*?<a href="(.*?)">(.*?)</a></b></td>' , re . DOTALL ) . findall ( o00OO00OoO )
 for url , ooo in Ii1i :
  if '</a>' in ooo :
   pass
  elif '(' in ooo :
   ii1iI1iI1 ( ( ooo ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '.mp3' , '' ) , i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) + url , 30005 , ooOooo000oOO + 'kodible.png' , ooOooo000oOO + 'kodible.png' , '' )
  else :
   II1I ( ( ooo ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '.mp3' , '' ) , i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) + url , 30004 , ooOooo000oOO + 'kodible.png' , ooOooo000oOO + 'kodible.png' , '' )
   if 64 - 64: IIIii1II1II + ii * ii
 xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 41 - 41: O0OoO . I1ii11iIi11i + oOo0O0Ooo
def o0O0OO ( ) :
 IIiI1i1i = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 IiII111i1i11 = IIiI1i1i . lower ( )
 o00OO00OoO = iiI111I1iIiI ( i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9jb21wbGV0ZV9saXN0Lmh0bQ==' ) )
 Ii1i = re . compile ( '<td width=".+?">.*?<b>.+?<a href="(.*?)">(.*?)</a></b></td>' , re . DOTALL ) . findall ( o00OO00OoO )
 for Ii1II1I11i1 , ooo in Ii1i :
  if IIiI1i1i in ooo . lower ( ) :
   if '</a>' in ooo :
    pass
   elif '(' in ooo :
    ii1iI1iI1 ( ( ooo ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + Ii1II1I11i1 , 30005 , ooOooo000oOO + 'kodible.png' , ooOooo000oOO + 'kodible.png' , '' )
   else :
    II1I ( ( ooo ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + Ii1II1I11i1 , 30004 , ooOooo000oOO + 'kodible.png' , ooOooo000oOO + 'kodible.png' , '' )
    if 22 - 22: IIiIiII11i * oO0o * iI1iI1I1i1I + Ii1I * I11i
    if 100 - 100: ooOoO0O00 / OooO0OoOOOO
def IiII1iiIiI ( ) :
 o00OO00OoO = iiI111I1iIiI ( i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9jb21wbGV0ZV9saXN0Lmh0bQ==' ) )
 Ii1i = re . compile ( '<td width=".+?">.*?<b>.+?<a href="(.*?)">(.*?)</a></b></td>' , re . DOTALL ) . findall ( o00OO00OoO )
 for Ii1II1I11i1 , ooo in Ii1i :
  if '</a>' in ooo :
   pass
  elif '(' in ooo :
   ii1iI1iI1 ( ( ooo ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + Ii1II1I11i1 , 30005 , ooOooo000oOO + 'kodible.png' , ooOooo000oOO + 'kodible.png' , '' )
  else :
   II1I ( ( ooo ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + Ii1II1I11i1 , 30004 , ooOooo000oOO + 'kodible.png' , ooOooo000oOO + 'kodible.png' , '' )
   if 59 - 59: o0o00Oo0O % I1ii11iIi11i
 xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 92 - 92: Ii11Ii1I % o0oOO0O00o0O / Ii1I % Ii1I * oOo0O0Ooo
 if 74 - 74: o0o00Oo0O . oOo0O0Ooo % oO0o % OooO0OoOOOO
def oOo0OooOo ( url ) :
 o00OO00OoO = iiI111I1iIiI ( url )
 Ii1i = re . compile ( '<a href="(.+?)">Download</a></b></td>' ) . findall ( o00OO00OoO )
 for url in Ii1i :
  ooo0O0o00O = ( i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) ) + url
  Resolve ( ooo0O0o00O )
  if 51 - 51: iI1iI1I1i1I . I1ii11iIi11i
def IiiIiiIi ( url ) :
 o00OO00OoO = iiI111I1iIiI ( url )
 Ii1i = re . compile ( '<td width="247">(.*?)</td>.*?<a href="(.+?)">' , re . DOTALL ) . findall ( o00OO00OoO )
 for ooo , url in Ii1i :
  if '<p align' in ooo :
   pass
  elif '&nbsp;' in ooo :
   pass
  else :
   II1I ( ( ooo ) . replace ( '&nbsp;' , '' ) , i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) + url , 10012 , ooOooo000oOO + 'kodible.png' , ooOooo000oOO + 'kodible.png' , '' )
   if 40 - 40: I11i
 xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 78 - 78: iI11I1II1I1I
 if 56 - 56: ii - iI1iI1I1i1I - ooOoO0O00
def I1i1I ( ) :
 o00OO00OoO = cloudflare . source ( i1111 ( 'aHR0cDovL3dhdGNoY2FydG9vbnNvbmxpbmUuZXUv' ) )
 Ii1i = re . compile ( 'class="menu-item menu-item-type-.+?><a href="([^"]*)">(.+?)</a></li>' , re . DOTALL ) . findall ( o00OO00OoO )
 for Ii1II1I11i1 , ooo in Ii1i :
  if 'ongoing' in Ii1II1I11i1 :
   II1I ( '[COLORgreen]' + ooo + '[/COLOR]' , Ii1II1I11i1 , 21005 , ooOooo000oOO + 'on-going.png' , '' , '' )
  if 'cartoon-series' in Ii1II1I11i1 :
   II1I ( '[COLORgreen]' + ooo + '[/COLOR]' , Ii1II1I11i1 , 21005 , ooOooo000oOO + 'cartoonseries.png' , '' , '' )
  if 'disney' in Ii1II1I11i1 :
   II1I ( '[COLORgreen]' + ooo + '[/COLOR]' , Ii1II1I11i1 , 21005 , ooOooo000oOO + 'disneytoons.png' , '' , '' )
  if 'genre' in Ii1II1I11i1 :
   II1I ( '[COLORgreen]' + ooo + '[/COLOR]' , Ii1II1I11i1 , 21005 , ooOooo000oOO + 'cartoongenre.png' , '' , '' )
  if 'years' in Ii1II1I11i1 :
   II1I ( '[COLORgreen]' + ooo + '[/COLOR]' , Ii1II1I11i1 , 21005 , ooOooo000oOO + 'years.png' , '' , '' )
def iii1I1Iii ( url ) :
 o00OO00OoO = cloudflare . source ( url )
 Ii1i = re . compile ( '<a href="([^"]*)" title="([^"]*)" rel="nofollow" id="featured-thumbnail">.+?<div class="featured-thumbnail"><img width="140" height="200" src="([^"]*)"' , re . DOTALL ) . findall ( o00OO00OoO )
 o00oo0 = re . compile ( '<button type="button"><a href="([^"]*)" target="_blank">(.+?)</a>' ) . findall ( o00OO00OoO )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' ) . findall ( o00OO00OoO )
 for url , ooo , I1II1I11I1I in Ii1i :
  II1I ( '[COLORgreen]' + ooo + '[/COLOR]' , url , 21006 , I1II1I11I1I , I1II1I11I1I , ooo )
 for url , ooo in o00oo0 :
  II1I ( '[COLORgreen]' + ooo + '[/COLOR]' , url , 21005 , ooOooo000oOO + 'watchcartoons.png' , '' , '' )
 for url in next :
  II1I ( '[COLORgreen]NEXT[/COLOR]' , url , 21005 , ooOooo000oOO + 'Next.png' , '' , '' )
def Oo0oOooOoOo ( url ) :
 o00OO00OoO = cloudflare . source ( url )
 Ii1i = re . compile ( '<li><a href="([^"]*)" >(.+?)</a></li>' , re . DOTALL ) . findall ( o00OO00OoO )
 I1i = re . compile ( 'file:"([^"]*)",type:"mp4",label:"([^"]*)"' , re . DOTALL ) . findall ( o00OO00OoO )
 Oo = re . compile ( 'src="([^"]*)" frameborder=' ) . findall ( o00OO00OoO )
 IiIiIi1I1 = re . compile ( '<iframe src="([^"]*)"' ) . findall ( o00OO00OoO )
 for url , ooo in Ii1i :
  II1I ( '[COLORgreen]' + ooo + '[/COLOR]' , url , 21007 , ooOooo000oOO + 'watchcartoons.png' , '' , '' )
 for url in Oo :
  II1I ( '[COLORgreen]PLAY[/COLOR]' , 'http:' + url , 222 , ooOooo000oOO + 'watchcartoons.png' , '' , '' )
 for url , ooo in I1i :
  ooOOoooooo ( '[COLORgreen]' + ooo + '[/COLOR]' , url , 222 , ooOooo000oOO + 'watchcartoons.png' , '' , '' )
 else :
  II1I ( '[COLORgreen]NO STREAMS AVAILABLE[/COLOR]' , url , 21005 , ooOooo000oOO + 'watchcartoons.png' , '' , '' )
def IiI1ii1Ii ( url ) :
 o00OO00OoO = cloudflare . source ( url )
 Ii1i = re . compile ( 'file:"([^"]*)",type:"mp4",label:"([^"]*)"' , re . DOTALL ) . findall ( o00OO00OoO )
 for url , ooo in Ii1i :
  ooOOoooooo ( '[COLORgreen]' + ooo + '[/COLOR]' , url , 222 , ooOooo000oOO + 'watchcartoons.png' , '' , '' )
  if 51 - 51: Ii * I11i / oOo0O0Ooo
def iIIi1I ( ) :
 II1Ii1iI1i1 ( '[COLORgreen]CARTOONS[/COLOR]' , '' , 20001 , ooOooo000oOO + 'ORIGINCARTOON.png' )
 II1Ii1iI1i1 ( '[COLORgreen]ANIME[/COLOR]' , 'https://kissanime.to/AnimeList' , 20001 , ooOooo000oOO + 'ORIGINCARTOON.png' )
 if 82 - 82: OooO0OoOOOO * Ii % IIiIiII11i - ii
def OO0 ( ) :
 II1Ii1iI1i1 ( '[COLORgreen]BY NAME[/COLOR]' , 'http://kisscartoon.me/CartoonList' , 20002 , ooOooo000oOO + 'ORIGINCARTOON.png' )
 II1Ii1iI1i1 ( '[COLORgreen]BY GENRE[/COLOR]' , 'http://kisscartoon.me/CartoonList' , 20003 , ooOooo000oOO + 'ORIGINCARTOON.png' )
 if 62 - 62: ooOoO0O00 / O0OoO . oOo0O0Ooo * I11i
def i11i1Ii1 ( url ) :
 o00OO00OoO = cloudflare . source ( url )
 Ii1i = re . compile ( 'href="(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( o00OO00OoO )
 for url , ooo in Ii1i :
  if '?c=' in url :
   II1Ii1iI1i1 ( '[COLORgreen]' + ooo + '[/COLOR]' , 'http://kisscartoon.me' + url , 20004 , ooOooo000oOO + 'ORIGINCARTOON.png' )
   if 98 - 98: IIIi
def o0oo0000 ( url ) :
 o00OO00OoO = cloudflare . source ( url )
 Ii1i = re . compile ( 'href="(.+?)" title="(.+?)">/n(.+?)</a><br/>' , re . DOTALL ) . findall ( o00OO00OoO )
 for url , i111i1i , ooo in Ii1i :
  if 'Genre' in url :
   II1Ii1iI1i1 ( '[COLORgreen]' + ooo + '[/COLOR]' , 'http://kisscartoon.me' + url , 20004 , ooOooo000oOO + 'ORIGINCARTOON.png' )
   if 19 - 19: IIiIiII11i - ooOoO0O00 - IIIii1II1II / IIIii1II1II + OOooOOo
def OO0Oooo0oo ( url ) :
 o00OO00OoO = cloudflare . source ( url )
 Ii1i = re . compile ( 'src="(.+?)" style=.+?<a class="bigChar" href="(.+?)">(.+?)</a>.+?<p>(.+?)</p>' , re . DOTALL ) . findall ( o00OO00OoO )
 for url , i111i1i , ooo in Ii1i :
  II1I ( '[COLORgreen]' + ooo + '[/COLOR]' , 'http://kisscartoon.me' + url , 20005 , img , '' , i111i1i )
  if 42 - 42: Ii11Ii1I * IIIi . OooO0OoOOOO * oOo0O0Ooo + OOooOOo
def i1i1II11II1 ( url ) :
 o00OO00OoO = cloudflare . source ( url )
 Ii1i = re . compile ( '<img width="120" height="165" src="(.+?)" style=.+?<a class="bigChar" href="(.+?)">(.+?)</a>.+?<p>(.+?)</p>' , re . DOTALL ) . findall ( o00OO00OoO )
 for url , i111i1i , ooo in Ii1i :
  II1I ( '[COLORgreen]' + ooo + '[/COLOR]' , 'http://kisscartoon.me' + url , 20005 , img , '' , i111i1i )
  if 5 - 5: I1ii11iIi11i - Ii1I % OoOo00o - IIiIiII11i . oOo0O0Ooo + o0oOO0O00o0O
  if 47 - 47: o0o00Oo0O - iI11I1II1I1I - o0oOO0O00o0O
  if 46 - 46: Ii11Ii1I . IIIii1II1II * oO0o . ii + Ii1I
  if 72 - 72: IIiIiII11i + IIIii1II1II
  if 91 - 91: iI11I1II1I1I % oO0o . I11i + Ii11Ii1I + I11i
def o00OOo ( ) :
 if 87 - 87: oO0o % oOo0O0Ooo
 II1I ( '[COLORgreen]Cartoons[/COLOR]' , i1111 ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2NhcnRvb24=' ) , 10004 , ooOooo000oOO + 'ORIGINCARTOON.png' , i1iiIII111ii , '' )
 II1I ( '[COLORgreen]Search Cartoons[/COLOR]' , '' , 10005 , ooOooo000oOO + 'ORIGINCARTOON.png' , i1iiIII111ii , '' )
 if 77 - 77: iI11I1II1I1I - ooOoO0O00 . OoOo00o
def iIi1iIIIiIiI ( ) :
 IIiI1i1i = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 IiII111i1i11 = IIiI1i1i . lower ( )
 o00OO00OoO = iiI111I1iIiI ( i1111 ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2NhcnRvb24=' ) )
 Ii1i = re . compile ( '<td><a href="(.+?)">(.+)</a></td>' ) . findall ( o00OO00OoO )
 for Ii1II1I11i1 , ooo in Ii1i :
  if IIiI1i1i in ooo . lower ( ) :
   if 'Dad!' in ooo :
    pass
   elif 'Family Guy' in ooo :
    pass
   elif '2 Stupid' in ooo :
    pass
   elif 'The Zelfs' in ooo :
    pass
   elif 'A Clone' in ooo :
    pass
   elif 'A.T.O.M' in ooo :
    pass
   elif 'Almost Naked' in ooo :
    pass
   elif 'Angry Kid' in ooo :
    pass
   elif 'Annoying Orange' in ooo :
    pass
   elif 'Aqua Teen' in ooo :
    pass
   elif 'Assy Mcgee' in ooo :
    pass
   elif 'Astroblast' in ooo :
    pass
   elif 'Atomic Betty' in ooo :
    pass
   elif 'Axe Cop' in ooo :
    pass
   elif 'Baby Playpen' in ooo :
    pass
   elif 'Beavis and Butt' in ooo :
    pass
   elif 'Celebrity Deathmatch' in ooo :
    pass
   elif 'Clerks The' in ooo :
    pass
   elif 'Crapston Villas' in ooo :
    pass
   elif 'Duckman:' in ooo :
    pass
   elif 'Stripperella' in ooo :
    pass
   elif 'Vixen' in ooo :
    pass
   else :
    II1I ( '[COLORgreen]' + ooo + '[/COLOR]' , Ii1II1I11i1 , 10006 , ooOooo000oOO + 'ORIGINCARTOON.png' , i1iiIII111ii , '' )
  xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 62 - 62: Ii % IIIii1II1II . OooO0OoOOOO . IIIii1II1II
def ooOo0O0O0oOO0 ( url ) :
 OO0O00oOo = iiI111I1iIiI ( url )
 Ii1i = re . compile ( '<td><a href="(.+?)">(.+)</a></td>' ) . findall ( OO0O00oOo )
 for url , ooo in Ii1i :
  if 'Dad!' in ooo :
   pass
  elif 'Family Guy' in ooo :
   pass
  elif '2 Stupid' in ooo :
   pass
  elif 'The Zelfs' in ooo :
   pass
  elif 'A Clone' in ooo :
   pass
  elif 'A.T.O.M' in ooo :
   pass
  elif 'Almost Naked' in ooo :
   pass
  elif 'Angry Kid' in ooo :
   pass
  elif 'Annoying Orange' in ooo :
   pass
  elif 'Aqua Teen' in ooo :
   pass
  elif 'Assy Mcgee' in ooo :
   pass
  elif 'Astroblast' in ooo :
   pass
  elif 'Atomic Betty' in ooo :
   pass
  elif 'Axe Cop' in ooo :
   pass
  elif 'Baby Playpen' in ooo :
   pass
  elif 'Beavis and Butt' in ooo :
   pass
  elif 'Celebrity Deathmatch' in ooo :
   pass
  elif 'Clerks The' in ooo :
   pass
  elif 'Crapston Villas' in ooo :
   pass
  elif 'Duckman:' in ooo :
   pass
  elif 'Stripperella' in ooo :
   pass
  elif 'Vixen' in ooo :
   pass
  else :
   II1I ( '[COLORgreen]' + ooo + '[/COLOR]' , url , 10006 , ooOooo000oOO + 'ORIGINCARTOON.png' , i1iiIII111ii , '' )
 xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 10 - 10: I1ii11iIi11i + o0o00Oo0O
def Ii1iI ( url ) :
 OO0O00oOo = iiI111I1iIiI ( url )
 I1 = re . compile ( '<img src="(.+?)" id="series_image" width="250" height="370" alt=".+?" />' ) . findall ( OO0O00oOo )
 for I1II1I11I1I in I1 :
  Oo0O0O000 = I1II1I11I1I
 II1Ii = re . compile ( '<li><a href="(.+?)">Next</a></li>' ) . findall ( OO0O00oOo )
 for url in II1Ii :
  II1I ( '[COLORgreen]NEXT PAGE[/COLOR]' , url , 10006 , ooOooo000oOO + 'Next.png' , i1iiIII111ii , '' )
 Ii1i = re . compile ( '&nbsp;<a href="(.+?)">(.+?)</a>' ) . findall ( OO0O00oOo )
 for url , ooo in Ii1i :
  oOO0oo ( '[COLORgreen]' + ooo + '[/COLOR]' , url , 10007 , Oo0O0O000 )
  if 57 - 57: OOooOOo - OoOo00o / O0OoO % Ii
  if 3 - 3: o0oOO0O00o0O . O0OoO % oOo0O0Ooo + Ii1I
 xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 64 - 64: ooOoO0O00
def IIii1 ( url , IMAGE ) :
 OO0O00oOo = iiI111I1iIiI ( url )
 Ii1i = re . compile ( '"playlist">(.+?)</span></div><div><iframe src="(.+?)"' ) . findall ( OO0O00oOo )
 for ooo , url in Ii1i :
  print ooo + '     ' + url
  if 'easy' in url :
   IiiiI111I ( url )
   if 49 - 49: I11i * Ii11Ii1I + iI1iI1I1i1I + o0oOO0O00o0O
   if 30 - 30: I11i / IIIii1II1II / OooO0OoOOOO % O0OoO + IIiIiII11i
  xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 4 - 4: o0oOO0O00o0O - I1ii11iIi11i - OooO0OoOOOO - iI1iI1I1i1I % Ii / oO0o
def IiiiI111I ( url ) :
 OO0O00oOo = iiI111I1iIiI ( url )
 Ii1i = re . compile ( "url: '(.+?)'," ) . findall ( OO0O00oOo )
 for url in Ii1i :
  i1iii11 ( url )
  if 92 - 92: OOooOOo . ii - IIIi
  if 74 - 74: iI11I1II1I1I % o0oOO0O00o0O * IIIii1II1II * iI11I1II1I1I
  if 73 - 73: I11i % IIIi . IIIii1II1II
def ooOOoOo ( ) :
 if 90 - 90: IIiIiII11i / oOo0O0Ooo
 II1I ( '[COLORgreen]Stand Up[/COLOR]' , '' , 10014 , ooOooo000oOO + 'ORIGINSTANDUP.png' , i1iiIII111ii , '' )
 II1I ( '[COLORgreen]Search Comedian[/COLOR]' , '' , 10015 , ooOooo000oOO + 'ORIGINSTANDUP.png' , i1iiIII111ii , '' )
 II1I ( '[COLORgreen]Others[/COLOR]' , '' , 10017 , ooOooo000oOO + 'ORIGINSTANDUP.png' , i1iiIII111ii , '' )
 if 45 - 45: iI11I1II1I1I
def iIiIii1ii ( ) :
 o00OO00OoO = iiI111I1iIiI ( ( i1111 ( 'aHR0cDovL2JhY2syYmFzaWNzYnVpbGQuY28udWsvdGVzdC9zdGFuZHVwbGlzdC5waHA=' ) ) )
 Ii1i = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( o00OO00OoO )
 for Ii1II1I11i1 , I1II1I11I1I , ooo in Ii1i :
  if 'elete' in ooo :
   pass
  else :
   oOO0oo ( '[COLORgreen]' + ooo + '[/COLOR]' , Ii1II1I11i1 , 222 , I1II1I11I1I )
   if 8 - 8: oO0o + OOooOOo . iI11I1II1I1I % o0o00Oo0O
def iI11Ii111 ( ) :
 IIiI1i1i = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 IiII111i1i11 = IIiI1i1i . lower ( )
 o00OO00OoO = iiI111I1iIiI ( ( i1111 ( 'aHR0cDovL3d3dy5jb3VjaHRyaXBwZXIuY29tL2ZvcnVtMi9wYWdlLnBocD9wYWdlPTM=' ) ) )
 OOo00OO00Oo = re . compile ( '<tr>.+?<td width=".+?" align=".+?">.+?<img border=".+?" src="..(.+?)" width=".+?" height=".+?"></td>.+?<td width=".+?" valign=".+?" align=".+?"><font size=".+?">(.+?)</font></td>.+?<td width=".+?">(.+?)</td>' , re . DOTALL ) . findall ( o00OO00OoO )
 for I1II1I11I1I , I1I1I11Ii , i1iII1IiiIiI1 in OOo00OO00Oo :
  for IIiI1i1i in I1I1I11Ii :
   print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< img >>>>>>>>>>>>>>>>>>>>>>>>>>'
   ii1Iii1 = re . compile ( '<a href="(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( i1iII1IiiIiI1 )
   for Ii1II1I11i1 , ooo in ii1Iii1 :
    if 'tube' in Ii1II1I11i1 :
     pass
    elif 'stage' in Ii1II1I11i1 :
     oOO0oo ( '[COLORgreen]' + I1I1I11Ii + '   -   ' + ooo + '[/COLOR]' , ( Ii1II1I11i1 ) . replace ( '" target="_blank' , '' ) , 10016 , 'http://couchtripper.com/' + I1II1I11I1I , )
    elif 'vee' in Ii1II1I11i1 :
     pass
     if 80 - 80: Ii11Ii1I - I11i
def iI1II1I1I ( ) :
 o00OO00OoO = iiI111I1iIiI ( ( i1111 ( 'aHR0cDovL3d3dy5jb3VjaHRyaXBwZXIuY29tL2ZvcnVtMi9wYWdlLnBocD9wYWdlPTM=' ) ) )
 OOo00OO00Oo = re . compile ( '<tr>.+?<td width=".+?" align=".+?">.+?<img border=".+?" src="..(.+?)" width=".+?" height=".+?"></td>.+?<td width=".+?" valign=".+?" align=".+?"><font size=".+?">(.+?)</font></td>.+?<td width=".+?">(.+?)</td>' , re . DOTALL ) . findall ( o00OO00OoO )
 for I1II1I11I1I , I1I1I11Ii , i1iII1IiiIiI1 in OOo00OO00Oo :
  ii1Iii1 = re . compile ( '<a href="(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( i1iII1IiiIiI1 )
  for Ii1II1I11i1 , ooo in ii1Iii1 :
   if 'tube' in Ii1II1I11i1 :
    pass
   elif 'stage' in Ii1II1I11i1 :
    oOO0oo ( '[COLORgreen]' + I1I1I11Ii + '   -   ' + ooo + '[/COLOR]' , ( Ii1II1I11i1 ) . replace ( '" target="_blank' , '' ) , 10016 , 'http://couchtripper.com/' + I1II1I11I1I )
   elif 'vee' in Ii1II1I11i1 :
    pass
    if 79 - 79: IIIii1II1II / IIIi . OOooOOo - Ii1I
    if 47 - 47: ii % o0o00Oo0O * o0oOO0O00o0O . Ii11Ii1I
 xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 38 - 38: o0o00Oo0O - OooO0OoOOOO % IIIi
def ooO ( url ) :
 o00OO00OoO = iiI111I1iIiI ( url )
 print '>>>>>>>>>>>>>>>>>>>>>>>>' + url + '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'
 OO0O0OOo0O = re . compile ( "url\[.+?\] = '(.+?)';" ) . findall ( o00OO00OoO )
 print '>>>>>>>>>>>>>>>>>>>>>>>' + ( str ( OO0O0OOo0O ) ) + '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
 for url in OO0O0OOo0O :
  i1iii11 ( ( url ) . replace ( '[' , '' ) . replace ( ']' , '' ) . replace ( '\'' , '' ) )
  if 39 - 39: IIIii1II1II / Ii1I / oOo0O0Ooo * IIIi
  if 44 - 44: o0o00Oo0O + O0OoO . iI11I1II1I1I + I1ii11iIi11i / o0o00Oo0O - iI1iI1I1i1I
  if 83 - 83: OooO0OoOOOO * iI1iI1I1i1I / I1ii11iIi11i
  if 32 - 32: I11i + OOooOOo - ii
  if 39 - 39: ii * IIIii1II1II * o0o00Oo0O . iI1iI1I1i1I . oO0o + O0OoO
  if 9 - 9: OOooOOo + OoOo00o % ii + I11i
  if 56 - 56: ii + Ii1I - o0oOO0O00o0O
def III1I1 ( ) :
 if 12 - 12: iI11I1II1I1I % O0OoO % O0OoO
 o0i1iI1iiI1I ( '[COLOR darkgoldenrod]Open Pandora\'s Box[/COLOR]' , '' , 10029 , 'https://encrypted-tbn1.gstatic.com/images?q=tbn%3AANd9GcTQ9r4TA8yIw9ggxuwsHxWojo6tPVfgTe8QIOxOQwzNR2TavtCi6Q' , i1iiIII111ii , '' )
 o0i1iI1iiI1I ( '[COLOR darkgoldenrod]Search[/COLOR]' , '' , 10026 , 'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png' , i1iiIII111ii , '' )
 if 52 - 52: oO0o % Ii11Ii1I * IIiIiII11i
 iiO0o0oOOOoOo ( 'movies' , 'MAIN' )
 if 4 - 4: iI1iI1I1i1I % o0o00Oo0O - ii + O0OoO . OoOo00o % IIiIiII11i
def Iiii1iiiIiI1 ( ) :
 o0i1iI1iiI1I ( 'Search Pandoras Films' , '' , 10027 , 'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png' , i1iiIII111ii , '' )
 o0i1iI1iiI1I ( 'Search Pandoras TV' , '' , 10028 , 'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png' , i1iiIII111ii , '' )
 if 27 - 27: Ii11Ii1I + oOo0O0Ooo * iI11I1II1I1I . ii * OOooOOo
 iiO0o0oOOOoOo ( 'movies' , 'MAIN' )
def OOOo ( ) :
 if 74 - 74: Ii11Ii1I - ii . I1ii11iIi11i
 IIiI1i1i = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 IiII111i1i11 = IIiI1i1i . lower ( )
 III1Ii1i1I1 = [ '480p' , '720p' , '1080p' , 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' , '720paction' , '720padventure' , '720panimation' , '720pcomedy' , '720pcrime' , '720pdocumentary' , '720pdrama' , '720pfamily' , '720pfantasy' , '720phorror' , '720pmystery' , '720promance' , '720psci-Fi' , '720psport' , '720pthriller' , '720pwestern' , '1080paction' , '1080padventure' , '1080panimation' , '1080pcomedy' , '1080pcrime' , '1080pdocumentary' , '1080pdrama' , '1080pfamily' , '1080pfantasy' , '1080phorror' , '1080pmystery' , '1080promance' , '1080psci-Fi' , '1080psport' , '1080pthriller' , '1080pwestern' , 'films' ]
 if 97 - 97: IIIi . O0OoO - IIIi + oOo0O0Ooo * IIiIiII11i
 for I111Ii in III1Ii1i1I1 :
  II11 = IIIII + I111Ii + ooOoOoo0O
  o00OO00OoO = O000OO0 ( II11 )
  Ii1i = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( o00OO00OoO )
  for Ii1II1I11i1 , iI1IOooOoOo , iiIII1i , III1I1Iii1iiI , ooo in Ii1i :
   if IIiI1i1i in ooo . lower ( ) :
    iIi ( ooo , Ii1II1I11i1 , 222 , iI1IOooOoOo , III1I1Iii1iiI , iiIII1i )
    if 29 - 29: o0o00Oo0O . IIIi
    iiO0o0oOOOoOo ( 'movies' , 'MAIN' )
    xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
    if 66 - 66: OoOo00o * iI11I1II1I1I % iI11I1II1I1I * OooO0OoOOOO - O0OoO - OooO0OoOOOO
    if 70 - 70: IIIi + OoOo00o
def o00ooo0 ( ) :
 if 39 - 39: O0OoO . IIiIiII11i
 IIiI1i1i = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 IiII111i1i11 = IIiI1i1i . lower ( )
 III1Ii1i1I1 = [ 'tvnum' , 'a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' , 'p' , 'q' , 'r' , 's' , 't' , 'u' , 'v' , 'w' , 'x' , 'y' , 'z' ]
 if 45 - 45: OoOo00o * OOooOOo / iI11I1II1I1I
 for I111Ii in III1Ii1i1I1 :
  o00ooOoO0 = IIIII + I111Ii + ooOoOoo0O
  o00OO00OoO = O000OO0 ( o00ooOoO0 )
  Ii1i = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( o00OO00OoO )
  for ooo , iiIII1i , Ii1II1I11i1 , I1II1I11I1I , III1I1Iii1iiI , IIi11II1II111 in Ii1i :
   if IIiI1i1i in ooo . lower ( ) :
    o0i1iI1iiI1I ( ooo , Ii1II1I11i1 , IIi11II1II111 , I1II1I11I1I , III1I1Iii1iiI , iiIII1i )
    if 55 - 55: O0OoO
    iiO0o0oOOOoOo ( 'movies' , 'MAIN' )
    xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
    if 82 - 82: IIIi - IIIii1II1II + oO0o
    if 64 - 64: I11i . o0o00Oo0O * Ii11Ii1I + ii - I1ii11iIi11i . ii
def OOoO0oo0O ( ) :
 if 49 - 49: I11i
 OO0O00oOo = iiI111I1iIiI ( IIIII + 'spongemain.php' )
 Ii1i = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( OO0O00oOo )
 for ooo , iiIII1i , Ii1II1I11i1 , I1II1I11I1I , III1I1Iii1iiI , IIi11II1II111 in Ii1i :
  o0i1iI1iiI1I ( ooo , Ii1II1I11i1 , IIi11II1II111 , I1II1I11I1I , III1I1Iii1iiI , iiIII1i )
  iiO0o0oOOOoOo ( 'movies' , 'MAIN' )
def II1ii1ii11I1 ( url ) :
 if 88 - 88: Ii1I
 xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
 oOOooooo0OoO0 = ( '%s%s' % ( ii1I111i1Ii , url ) )
 O000oo0O = iiI111I1iIiI ( url )
 Ii1i = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( O000oo0O )
 for url , iI1IOooOoOo , iiIII1i , OOOooO0OO0o , ooo in Ii1i :
  iIi ( ooo , url , 222 , iI1IOooOoOo , OOOooO0OO0o , iiIII1i )
  if 10 - 10: Ii11Ii1I - OOooOOo . ii . IIIii1II1II . oO0o * o0oOO0O00o0O
  iiO0o0oOOOoOo ( 'movies' , 'MAIN' )
  if 78 - 78: OoOo00o / oO0o - OoOo00o * ii . OOooOOo
  xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 96 - 96: oOo0O0Ooo % ooOoO0O00 . I11i . o0o00Oo0O
  if 37 - 37: ooOoO0O00 - IIIii1II1II % ii / IIIii1II1II % O0OoO
def iiIiII11i1 ( url ) :
 if 93 - 93: OOooOOo % iI11I1II1I1I
 OO0O00oOo = iiI111I1iIiI ( url )
 Ii1i = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( OO0O00oOo )
 for ooo , iiIII1i , url , I1II1I11I1I , III1I1Iii1iiI , IIi11II1II111 in Ii1i :
  o0i1iI1iiI1I ( ooo , url , IIi11II1II111 , I1II1I11I1I , III1I1Iii1iiI , iiIII1i )
  if 90 - 90: oOo0O0Ooo - IIIii1II1II / Ii11Ii1I / o0o00Oo0O / iI1iI1I1i1I
  iiO0o0oOOOoOo ( 'movies' , 'MAIN' )
  if 87 - 87: OOooOOo / OooO0OoOOOO + iI11I1II1I1I
  if 93 - 93: iI11I1II1I1I + OoOo00o % O0OoO
 xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 21 - 21: IIIii1II1II
def iIi ( name , url , mode , iconimage , fanart , description ) :
 if 6 - 6: OooO0OoOOOO
 i1I1II = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 Ii1I1I1i11ii = True
 OoOo0oO0o = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 OoOo0oO0o . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 OoOo0oO0o . setProperty ( "Fanart_Image" , fanart )
 Ii1I1I1i11ii = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = i1I1II , listitem = OoOo0oO0o , isFolder = False )
 return Ii1I1I1i11ii
 if 54 - 54: o0oOO0O00o0O % ooOoO0O00 + Ii1I
def o0i1iI1iiI1I ( name , url , mode , iconimage , fanart , description ) :
 if 2 - 2: iI11I1II1I1I * OoOo00o / OOooOOo . iI1iI1I1i1I / OooO0OoOOOO
 i1I1II = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 Ii1I1I1i11ii = True
 OoOo0oO0o = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 OoOo0oO0o . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 OoOo0oO0o . setProperty ( "Fanart_Image" , fanart )
 Ii1I1I1i11ii = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = i1I1II , listitem = OoOo0oO0o , isFolder = True )
 return Ii1I1I1i11ii
if 75 - 75: OOooOOo
if 78 - 78: Ii11Ii1I + OOooOOo + OooO0OoOOOO - OooO0OoOOOO . Ii / oO0o
if 27 - 27: Ii11Ii1I - o0o00Oo0O % iI1iI1I1i1I * IIIi . OooO0OoOOOO % iI11I1II1I1I
if 37 - 37: ii + o0o00Oo0O - ooOoO0O00 % O0OoO
if 24 - 24: OOooOOo
if 94 - 94: ooOoO0O00 * ooOoO0O00 % IIiIiII11i + IIIii1II1II
if 28 - 28: oOo0O0Ooo
if 49 - 49: iI1iI1I1i1I . I11i % OoOo00o / Ii11Ii1I
if 95 - 95: o0o00Oo0O * OOooOOo * OooO0OoOOOO . O0OoO / iI11I1II1I1I
if 28 - 28: OooO0OoOOOO + OoOo00o - O0OoO / iI11I1II1I1I - oOo0O0Ooo
if 45 - 45: o0o00Oo0O / ooOoO0O00 * OoOo00o * oO0o
if 35 - 35: Ii1I / o0oOO0O00o0O % oOo0O0Ooo + iI11I1II1I1I
if 79 - 79: OOooOOo / O0OoO
if 77 - 77: I1ii11iIi11i
if 46 - 46: IIIi
def o00OoooooooOo ( string ) :
 if iiiiiIIii == 'true' :
  xbmc . log ( "[addon.live.GenieTV-%s]: %s" % ( addon_version , string ) )
  if 32 - 32: I11i + oOo0O0Ooo . IIIi
def iIiIi1Ii11IiI1I1 ( name , url , iconimage , fanart , mode , playlist = None , regexs = None ) :
 OOoIiiIIi1 = [ ]
 try :
  if 28 - 28: I11i
  name = name . encode ( 'utf-8' , 'ignore' )
 except :
  pass
 if os . path . exists ( I11i1 ) == False :
  o00OoooooooOo ( 'Making Favorites File' )
  OOoIiiIIi1 . append ( ( name , url , iconimage , fanart , mode , playlist , regexs ) )
  oOOo0oo0O = open ( I11i1 , "w" )
  oOOo0oo0O . write ( json . dumps ( OOoIiiIIi1 ) )
  oOOo0oo0O . close ( )
 else :
  o00OoooooooOo ( 'Appending Favorites' )
  oOOo0oo0O = open ( I11i1 ) . read ( )
  IIi = json . loads ( oOOo0oo0O )
  IIi . append ( ( name , url , iconimage , fanart , mode ) )
  iIIi = open ( I11i1 , "w" )
  iIIi . write ( json . dumps ( IIi ) )
  iIIi . close ( )
  if 32 - 32: IIIi * iI11I1II1I1I + I1ii11iIi11i * I1ii11iIi11i
  if 29 - 29: OooO0OoOOOO * iI1iI1I1i1I . oO0o
def O00O0 ( ) :
 if os . path . exists ( I11i1 ) == False :
  OOoIiiIIi1 = [ ]
  o00OoooooooOo ( 'Making Favorites File' )
  OOoIiiIIi1 . append ( ( 'Genie Tv Favourites Section' , '' , '' , '' , '' , '' , '' ) )
  oOOo0oo0O = open ( I11i1 , "w" )
  oOOo0oo0O . write ( json . dumps ( OOoIiiIIi1 ) )
  oOOo0oo0O . close ( )
 else :
  IiI = json . loads ( open ( I11i1 ) . read ( ) )
  O0o0OO00 = len ( IiI )
  for iIi11i in IiI :
   ooo = iIi11i [ 0 ]
   Ii1II1I11i1 = iIi11i [ 1 ]
   iI1IOooOoOo = iIi11i [ 2 ]
   try :
    ooIII1II1iii1i = iIi11i [ 3 ]
    if ooIII1II1iii1i == None :
     raise
   except :
    if o0oO0 . getSetting ( 'use_thumb' ) == "true" :
     ooIII1II1iii1i = iI1IOooOoOo
    else :
     ooIII1II1iii1i = III1I1Iii1iiI
   try : O0OO0oOO = iIi11i [ 5 ]
   except : O0OO0oOO = None
   try : ooooO = iIi11i [ 6 ]
   except : ooooO = None
   if 92 - 92: I11i / I11i * Ii11Ii1I
   if iIi11i [ 4 ] == 0 :
    II1I ( ooo , Ii1II1I11i1 , '' , iI1IOooOoOo , III1I1Iii1iiI , '' , 'fav' )
   else :
    II1I ( ooo , Ii1II1I11i1 , iIi11i [ 4 ] , iI1IOooOoOo , III1I1Iii1iiI , '' , 'fav' )
    if 19 - 19: Ii11Ii1I
def O0o00oO0oOO ( name ) :
 IIi = json . loads ( open ( I11i1 ) . read ( ) )
 for iiiii1I1III1 in range ( len ( IIi ) ) :
  if IIi [ iiiii1I1III1 ] [ 0 ] == name :
   del IIi [ iiiii1I1III1 ]
   iIIi = open ( I11i1 , "w" )
   iIIi . write ( json . dumps ( IIi ) )
   iIIi . close ( )
   break
 xbmc . executebuiltin ( "XBMC.Container.Refresh" )
 if 12 - 12: o0oOO0O00o0O . OOooOOo * oOo0O0Ooo
 if 37 - 37: Ii1I * oOo0O0Ooo % Ii % ooOoO0O00 % OooO0OoOOOO
def o0o0oOoOO0O ( ) :
 iii = os . path . join ( OOooO0OOoo , 'addons.ini' )
 O0o0O = open ( iii , "w+" )
 if 6 - 6: IIiIiII11i
 O0o0O . write ( r'# This file contains the "built-in" channels' + '\n' )
 O0o0O . write ( r'# It is parsed by Pythons ConfigParser' + '\n\n' )
 O0o0O . write ( r'[plugin.video.GenieTv]' + '\n' )
 O0o0O . write ( r'BBC One=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F191.m3u8&mode=10012&name=[COLORgreen]BBC+One%0D[%2FCOLOR]' + '\n' )
 O0o0O . write ( r'BBC Two=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F190.m3u8&mode=10012&name=[COLORgreen]BBC+Two%0D[%2FCOLOR]' + '\n' )
 O0o0O . write ( r'BBC Four=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F188.m3u8&mode=10012&name=[COLORgreen]BBC+Four%0D[%2FCOLOR]' + '\n' )
 O0o0O . write ( r'ITV=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F208.m3u8&mode=10012&name=[COLORgreen]ITV1%0D[%2FCOLOR]' + '\n' )
 O0o0O . write ( r'ITV2=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F207.m3u8&mode=10012&name=[COLORgreen]ITV2%0D[%2FCOLOR]' + '\n' )
 O0o0O . write ( r'ITV3=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F206.m3u8&mode=10012&name=[COLORgreen]ITV3%0D[%2FCOLOR]' + '\n' )
 O0o0O . write ( r'ITV4=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F205.m3u8&mode=10012&name=[COLORgreen]ITV4%0D[%2FCOLOR]' + '\n' )
 O0o0O . write ( r'Channel 4=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F183.m3u8&mode=10012&name=[COLORgreen]Channel+4%0D[%2FCOLOR]' + '\n' )
 O0o0O . write ( r'Channel 5=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F185.m3u8&mode=10012&name=[COLORgreen]Channel+5%0D[%2FCOLOR]' + '\n' )
 O0o0O . write ( r'5STAR=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F187.m3u8&mode=10012&name=[COLORgreen]5%2A%0D[%2FCOLOR]' + '\n' )
 O0o0O . write ( r'5 USA=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F186.m3u8&mode=10012&name=[COLORgreen]5USA%0D[%2FCOLOR]' + '\n' )
 O0o0O . write ( r'RTE One=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F194.m3u8&mode=10012&name=[COLORgreen]RTE+One%0D[%2FCOLOR]' + '\n' )
 O0o0O . write ( r'RTE Two=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F193.m3u8&mode=10012&name=[COLORgreen]RTE+Two%0D[%2FCOLOR]' + '\n' )
 O0o0O . write ( r'TG4=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F192.m3u8&mode=10012&name=[COLORgreen]TG4%0D[%2FCOLOR]' + '\n' )
 O0o0O . write ( r'Sky1=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F32.m3u8&mode=10012&name=[COLORgreen]Sky+1%0D[%2FCOLOR]' + '\n' )
 O0o0O . write ( r'Sky2=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F33.m3u8&mode=10012&name=[COLORgreen]Sky+2%0D[%2FCOLOR]' + '\n' )
 O0o0O . write ( r'Sky Living=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F35.m3u8&mode=10012&name=[COLORgreen]Sky+Living%0D[%2FCOLOR]' + '\n' )
 O0o0O . write ( r'Sky Atlantic=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F34.m3u8&mode=10012&name=[COLORgreen]Sky+Atlantic%0D[%2FCOLOR]' + '\n' )
 O0o0O . write ( r'Dave=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F325.m3u8&mode=10012&name=[COLORgreen]Dave%0D[%2FCOLOR]' + '\n' )
 O0o0O . write ( r'Pick=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F324.m3u8&mode=10012&name=[COLORgreen]Pick%0D[%2FCOLOR]' + '\n' )
 O0o0O . write ( r'GOLD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F326.m3u8&mode=10012&name=[COLORgreen]Gold%0D[%2FCOLOR]' + '\n' )
 O0o0O . write ( r'Watch HD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F518.m3u8&mode=10012&name=[COLORgreen]Watch%0D[%2FCOLOR]' + '\n' )
 O0o0O . write ( r'YESTERDAY=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F377.m3u8&mode=10012&name=[COLORgreen]Yesterday%0D[%2FCOLOR]' + '\n' )
 O0o0O . write ( r'Comedy Central=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F181.m3u8&mode=10012&name=[COLORgreen]Comedy+Central%0D[%2FCOLOR]' + '\n' )
 O0o0O . write ( r'London Live=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F830.m3u8&mode=10012&name=[COLORgreen]London+Live%0D[%2FCOLOR]' + '\n' )
 O0o0O . write ( r'Disney Junior=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F230.m3u8&mode=10012&name=[COLORgreen]Disney+Jr.%0D[%2FCOLOR]' + '\n' )
 O0o0O . write ( r'Disney Chnl=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F231.m3u8&mode=10012&name=[COLORgreen]Disney+Channel%0D[%2FCOLOR]' + '\n' )
 O0o0O . write ( r'Animal Planet=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F198.m3u8&mode=10012&name=[COLORgreen]Animal+Planet%0D[%2FCOLOR]' + '\n' )
 O0o0O . write ( r'Nat Geo=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F197.m3u8&mode=10012&name=[COLORgreen]National+Geographic+Channel%0D[%2FCOLOR]' + '\n' )
 O0o0O . write ( r'Discovery=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F200.m3u8&mode=10012&name=[COLORgreen]Discovery+Channel%0D[%2FCOLOR]' + '\n' )
 O0o0O . write ( r'Discovery Science=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F199.m3u8&mode=10012&name=[COLORgreen]Discovery+Science%0D[%2FCOLOR]' + '\n' )
 O0o0O . write ( r'Disc.Turbo=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F168.m3u8&mode=10012&name=[COLORgreen]Discovery+Turbo%0D[%2FCOLOR]' + '\n' )
 O0o0O . write ( r'Food Network=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F639.m3u8&mode=10012&name=[COLORgreen]Food+Network%0D[%2FCOLOR]' + '\n' )
 O0o0O . write ( r'MTV MUSIC=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F234.m3u8&mode=10012&name=[COLORgreen]MTV+Music%0D[%2FCOLOR]' + '\n' )
 O0o0O . write ( r'Film4=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F182.m3u8&mode=10012&name=[COLORgreen]Film4%0D[%2FCOLOR]' + '\n' )
 O0o0O . write ( r'True Movies=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F853.m3u8&mode=10012&name=[COLORgreen]True+Movies%0D[%2FCOLOR]' + '\n' )
 O0o0O . write ( r'True Movies 2=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F852.m3u8&mode=10012&name=[COLORgreen]True+Movies+2%0D[%2FCOLOR]' + '\n' )
 O0o0O . write ( r'Sky Action=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F732.m3u8&mode=10012&name=[COLORgreen]Sky+Movies+Action+%26+Adventure%0D[%2FCOLOR]' + '\n' )
 O0o0O . write ( r'Sky ScFiHorror=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F511.m3u8&mode=10012&name=[COLORgreen]Sky+Movies+Sci-Fi+%26+Horror%0D[%2FCOLOR]' + '\n' )
 O0o0O . write ( r'SkyPremiereHD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F516.m3u8&mode=10012&name=[COLORgreen]Sky+Movies+Premiere%0D[%2FCOLOR]' + '\n' )
 O0o0O . write ( r'Sky Greats=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F512.m3u8&mode=10012&name=[COLORgreen]Sky+Movies+Greats%0D[%2FCOLOR]' + '\n' )
 O0o0O . write ( r'Sky Family=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F509.m3u8&mode=10012&name=[COLORgreen]Sky+Movies+Family%0D[%2FCOLOR]' + '\n' )
 O0o0O . write ( r'Sky DramaRom=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F510.m3u8&mode=10012&name=[COLORgreen]Sky+Movies+Drama+%26+Romance%0D[%2FCOLOR]' + '\n' )
 O0o0O . write ( r'Sky Thriller=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F514.m3u8&mode=10012&name=[COLORgreen]Sky+Movies+Crime+%26+Thriller%0D[%2FCOLOR]' + '\n' )
 O0o0O . write ( r'Sky Comedy=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F513.m3u8&mode=10012&name=[COLORgreen]Sky+Movies+Comedy%0D[%2FCOLOR]' + '\n' )
 O0o0O . write ( r'Sky Showcase=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F46.m3u8&mode=10012&name=[COLORgreen]Sky+Movies+Showcase%0D[%2FCOLOR]' + '\n' )
 O0o0O . write ( r'Sky Select=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F45.m3u8&mode=10012&name=[COLORgreen]Sky+Movies+Select%0D[%2FCOLOR]' + '\n' )
 O0o0O . write ( r'Sky Disney=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F195.m3u8&mode=10012&name=[COLORgreen]Sky+Movies+Disney%0D[%2FCOLOR]' + '\n' )
 O0o0O . write ( r'Sky Sports 1=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F18.m3u8&mode=10012&name=[COLORgreen]Sky+Sports+1%0D[%2FCOLOR]' + '\n' )
 O0o0O . write ( r'Sky Sports 2=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F19.m3u8&mode=10012&name=[COLORgreen]Sky+Sports+2%0D[%2FCOLOR]' + '\n' )
 O0o0O . write ( r'Sky Sports 3=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F20.m3u8&mode=10012&name=[COLORgreen]Sky+Sports+3%0D[%2FCOLOR]' + '\n' )
 O0o0O . write ( r'Sky Sports 4=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F21.m3u8&mode=10012&name=[COLORgreen]Sky+Sports+4%0D[%2FCOLOR]' + '\n' )
 O0o0O . write ( r'Sky Sports 5=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F22.m3u8&mode=10012&name=[COLORgreen]Sky+Sports+5%0D[%2FCOLOR]' + '\n' )
 O0o0O . write ( r'Sky Sports F1=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F24.m3u8&mode=10012&name=[COLORgreen]Sky+Sports+F1%0D[%2FCOLOR]' + '\n' )
 O0o0O . write ( r'Sky Sports News=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F23.m3u8&mode=10012&name=[COLORgreen]Sky+Sports+News%0D[%2FCOLOR]' + '\n' )
 O0o0O . write ( r'BT Sport 1=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F309.m3u8&mode=10012&name=[COLORgreen]BT+Sport+1%0D[%2FCOLOR]' + '\n' )
 O0o0O . write ( r'BT Sport 2=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F26.m3u8&mode=10012&name=[COLORgreen]BT+Sport+2%0D[%2FCOLOR]' + '\n' )
 O0o0O . write ( r'BT Sport Europe=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F705.m3u8&mode=10012&name=[COLORgreen]BT+Sport+Europe%0D[%2FCOLOR]' + '\n' )
 O0o0O . write ( r'BT Sport ESPN=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F28.m3u8&mode=10012&name=[COLORgreen]BT+Sport+ESPN%0D[%2FCOLOR]' + '\n' )
 O0o0O . write ( r'Box Nation=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F173.m3u8&mode=10012&name=[COLORgreen]Box+Nation%0D[%2FCOLOR]' + '\n' )
 O0o0O . write ( r'WWENetwork=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F178.m3u8&mode=10012&name=[COLORgreen]WWENetwork%0D[%2FCOLOR]' + '\n' )
 O0o0O . write ( r'Eurosport=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F269.m3u8&mode=10012&name=[COLORgreen]Eurosport+1%0D[%2FCOLOR]' + '\n' )
 O0o0O . write ( r'Eurosport 2=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F748.m3u8&mode=10012&name=[COLORgreen]Eurosport+2%0D[%2FCOLOR]' + '\n' )
 O0o0O . write ( r'At The Races=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F170.m3u8&mode=10012&name=[COLORgreen]At+the+Races%0D[%2FCOLOR]' + '\n' )
 O0o0O . write ( r'Racing UK=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F171.m3u8&mode=10012&name=[COLORgreen]Racing+UK%0D[%2FCOLOR]' + '\n' )
 O0o0O . write ( r'Poker central US=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F826.m3u8&mode=10012&name=[COLORgreen]Poker+central+US%0D[%2FCOLOR]' + '\n' )
 if 7 - 7: Ii11Ii1I % ooOoO0O00 * ii * o0o00Oo0O + o0oOO0O00o0O
 if 95 - 95: ii + iI1iI1I1i1I - Ii1I / Ii1I . ooOoO0O00 . ii
 if 29 - 29: O0OoO - ooOoO0O00 . iI1iI1I1i1I - Ii1I + O0OoO + ii
def iii1 ( ) :
 if 13 - 13: iI11I1II1I1I
 II1I ( '[COLORgreen]Recent Episodes[/COLOR]' , '' , 10019 , ooOooo000oOO + 'dtv.png' , i1iiIII111ii , '' )
 II1I ( '[COLORgreen]Genres[/COLOR]' , '' , 10020 , ooOooo000oOO + 'dtv.png' , i1iiIII111ii , '' )
 II1I ( '[COLORgreen]Search[/COLOR]' , '' , 10021 , ooOooo000oOO + 'dtv.png' , i1iiIII111ii , '' )
 if 77 - 77: Ii - iI11I1II1I1I / OoOo00o / O0OoO / oO0o
def ooo0O0o0OoOO ( ) :
 if 9 - 9: oO0o
 OO0O00oOo = cloudflare . source ( i1111 ( 'aHR0cDovL2RpemlsYWIuY29t' ) )
 Ii1i = re . compile ( '<li id=".+?">.+?<a href="(.+?)">.+?<img width="40" height="40" src="(.+?)" alt=""/>.+?<span class="title">\n(.+?)</span>.+?<span class="alt-title">\n(.+?)</span>.+?</a>.+?</li>' , re . DOTALL ) . findall ( OO0O00oOo )
 for Ii1II1I11i1 , I1II1I11I1I , ooo , o0O00oOOoo in Ii1i :
  II1I ( ooo + '  -  ' + ( o0O00oOOoo ) . replace ( 'sezon' , 'Season' ) . replace ( 'bölüm' , 'Episode' ) , Ii1II1I11i1 , 10023 , ooOooo000oOO + 'dtv.png' , i1iiIII111ii , '' )
  if 60 - 60: IIIi
  if 98 - 98: O0OoO
  if 34 - 34: iI11I1II1I1I * iI1iI1I1i1I * iI1iI1I1i1I / Ii1I
def IIIIIIi1i ( ) :
 if 26 - 26: iI11I1II1I1I - o0o00Oo0O . o0o00Oo0O
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
 if 68 - 68: IIIii1II1II + OoOo00o . o0o00Oo0O . Ii11Ii1I % ooOoO0O00 % IIIii1II1II
def i1I1iI ( url ) :
 iiIi11iI1iii = 'http://dizilab.com/arsiv?limit=100&tur=' + url + '&orderby=&ulke=&order=&yil=&dizi_adi='
 o00OO00OoO = cloudflare . source ( iiIi11iI1iii )
 Ii1i = re . compile ( '<div class="tv-series-single">.+?<a href="(.+?)" class="film-image">.+?<img src="(.+?)" alt=""/>.+?<span class="position">.+?</span>\n(.+?)</a>' , re . DOTALL ) . findall ( o00OO00OoO )
 for url , I1II1I11I1I , ooo in Ii1i :
  II1I ( '[COLORgreen]' + ooo + '[/COLOR]' , url , 10022 , ooOooo000oOO + 'dtv.png' , i1iiIII111ii , '' )
  if 92 - 92: I1ii11iIi11i / Ii + Ii1I
  if 87 - 87: OOooOOo % iI11I1II1I1I
  if 72 - 72: IIIii1II1II . IIIii1II1II - Ii1I
  if 48 - 48: I1ii11iIi11i - O0OoO + I1ii11iIi11i - oOo0O0Ooo * Ii . o0oOO0O00o0O
def I1iIIIiI ( ) :
 if 60 - 60: oOo0O0Ooo . Ii + OOooOOo / Ii1I * IIiIiII11i * IIIii1II1II
 IIiI1i1i = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 IiII111i1i11 = IIiI1i1i . lower ( )
 Ii1II1I11i1 = ( i1111 ( 'aHR0cDovL2RpemlsYWIuY29tL2Fyc2l2P2xpbWl0PSZ0dXI9Jm9yZGVyYnk9JnVsa2U9Jm9yZGVyPSZ5aWw9JmRpemlfYWRpPQ==' ) ) + ( IIiI1i1i ) . replace ( ' ' , '+' )
 o00OO00OoO = cloudflare . source ( Ii1II1I11i1 )
 Ii1i = re . compile ( '<a href="(.+?)" class="film-image">\n<img src="(.+?)" alt=""/>\n</a>\n<div class="tss-detail">\n<a class="title" style="" href=".+?">\n<span class="position">.+?</span>\n(.+?)</a>' ) . findall ( o00OO00OoO )
 for Ii1II1I11i1 , I1II1I11I1I , ooo in Ii1i :
  if IIiI1i1i in ooo . lower ( ) :
   II1I ( '[COLORgreen]' + ooo + '[/COLOR]' , Ii1II1I11i1 , 10022 , ooOooo000oOO + 'dtv.png' )
   if 59 - 59: I1ii11iIi11i + o0oOO0O00o0O - IIIii1II1II . I11i + oOo0O0Ooo % OoOo00o
   if 37 - 37: o0oOO0O00o0O + o0oOO0O00o0O % I11i
   if 29 - 29: O0OoO
def ii1iIi1Ii1 ( url ) :
 o00OO00OoO = cloudflare . source ( url )
 Ii1i = re . compile ( '<a class="season" href="(.+?)">\n(.+?)\n</a>.+?<a class="episode" href=".+?">\n(.+?)\n</a>.+?<a class="episode-name" href=".+?">\n(.+?)</a>' , re . DOTALL ) . findall ( o00OO00OoO )
 for ooo0O0o00O , oOOoOOO0oo0 , O00O , ooo in Ii1i :
  O0OOOOOoo = ( O00O ) . replace ( 'Sezon' , '' ) . replace ( 'bölüm' , '' ) . replace ( 'Bölüm' , '' ) . replace ( 'BÃ¶lÃ¼m' , '' ) . replace ( '.' , '' )
  oo0ooO0 = ( oOOoOOO0oo0 ) . replace ( 'bölüm' , '' ) . replace ( 'Sezon' , '' ) . replace ( 'Bölüm' , '' ) . replace ( 'BÃ¶lÃ¼m' , '' ) . replace ( '.' , '' )
  oOooo0OOO = 'Season ' + oo0ooO0 + 'Episode ' + O0OOOOOoo + ooo
  oooO00O ( oOooo0OOO , ooo0O0o00O )
  if 2 - 2: OoOo00o . IIIi * I1ii11iIi11i + o0o00Oo0O - iI1iI1I1i1I * iI11I1II1I1I
  xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 12 - 12: I11i * IIIi % IIiIiII11i * ooOoO0O00 * iI11I1II1I1I
  if 81 - 81: I1ii11iIi11i - iI1iI1I1i1I
def oooO00O ( name , url ) :
 ooo0O0o00O = url
 ii1iII1iI111 = name
 OOOO0OOoO0O0 = cloudflare . source ( ooo0O0o00O )
 I1 = re . compile ( 'file: "(.+?)",.+?label: "(.+?)",' , re . DOTALL ) . findall ( OOOO0OOoO0O0 )
 for OO0O0OOo0O , o0o0O0O000 in I1 :
  oOO0oo ( '[COLORgreen]' + ii1iII1iI111 + o0o0O0O000 + '[/COLOR]' , OO0O0OOo0O , 10012 , ooOooo000oOO + 'dtv.png' )
  if 24 - 24: O0OoO / o0oOO0O00o0O + OooO0OoOOOO . OooO0OoOOOO
 xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 39 - 39: O0OoO + o0o00Oo0O / ooOoO0O00 % OooO0OoOOOO / OoOo00o * OooO0OoOOOO
 if 77 - 77: OooO0OoOOOO . IIIi % OOooOOo
def I1111III11 ( ) :
 if 46 - 46: o0o00Oo0O
 if 65 - 65: iI11I1II1I1I % OoOo00o + o0o00Oo0O / ii
 if 52 - 52: Ii11Ii1I % IIIii1II1II * oOo0O0Ooo % iI1iI1I1i1I + IIIii1II1II / o0oOO0O00o0O
 if 80 - 80: ii + OooO0OoOOOO
 if 95 - 95: IIIi / OoOo00o * IIIi - ii * ii % oO0o
 if 43 - 43: I1ii11iIi11i . IIIi
 if 12 - 12: IIIi + IIIii1II1II + iI1iI1I1i1I . OooO0OoOOOO / Ii11Ii1I
 if 29 - 29: OooO0OoOOOO . O0OoO - IIiIiII11i
 if 68 - 68: iI11I1II1I1I + IIiIiII11i / OoOo00o
 if 91 - 91: OOooOOo % iI11I1II1I1I . oOo0O0Ooo
 if 70 - 70: iI1iI1I1i1I % IIiIiII11i % o0o00Oo0O . ooOoO0O00 / IIIi
 if 100 - 100: Ii1I * Ii % OoOo00o / I1ii11iIi11i / O0OoO + Ii1I
 if 59 - 59: IIIi - OooO0OoOOOO
 if 14 - 14: iI11I1II1I1I - iI11I1II1I1I
 if 5 - 5: OooO0OoOOOO
 II1I ( '[COLORgreen]Newest Episodes Added[/COLOR]' , 'http://www.watchseries.li/latest' , 10046 , ooOooo000oOO + 'WATCHSERIES.png' , '' , '' )
 II1I ( '[COLORgreen]This Week\'s Popular Episodes[/COLOR]' , 'http://www.watchseries.li/new' , 10042 , ooOooo000oOO + 'WATCHSERIES.png' , '' , '' )
 II1I ( '[COLORgreen]Search Program[/COLOR]' , '' , 10043 , ooOooo000oOO + 'WATCHSERIES.png' , '' , '' )
 if 84 - 84: IIiIiII11i * OoOo00o * IIiIiII11i % OooO0OoOOOO / oOo0O0Ooo
 if 100 - 100: OooO0OoOOOO . Ii11Ii1I - iI11I1II1I1I . Ii / IIiIiII11i
def o0oO0OO00oo0o ( url ) :
 o00OO00OoO = iiI111I1iIiI ( url )
 i1I1iIi = re . compile ( '<ul class="pagination" style="line-height: 3;">(.+?)</ul>' , re . DOTALL ) . findall ( o00OO00OoO )
 Ii1i = re . compile ( '<li><a href="/letters/(.+?)">(.+?)</a></li>' ) . findall ( str ( i1I1iIi ) )
 for url , ooo in Ii1i :
  II1I ( '[COLORgreen]' + ooo + '[/COLOR]' , 'http://watchseries.li/letters/' + url , 10049 , ooOooo000oOO + 'WATCHSERIES.png' , '' , '' )
  if 17 - 17: OooO0OoOOOO / Ii1I - I11i * Ii1I
def i11i11II11i ( url ) :
 o00OO00OoO = iiI111I1iIiI ( url )
 Ii1i = re . compile ( '<a href="(.+?)" class="sr-header">(.+?)</a>' ) . findall ( o00OO00OoO )
 for url , ooo in Ii1i :
  II1I ( '[COLORgreen]' + ooo + '[/COLOR]' , 'http://watchseries.li/' + url , 10049 , ooOooo000oOO + 'WATCHSERIES.png' , '' , '' )
  if 9 - 9: OOooOOo - Ii1I * O0OoO . O0OoO - oOo0O0Ooo
def OOooOooo0OOo0 ( url ) :
 o00OO00OoO = iiI111I1iIiI ( url )
 Ii1i = re . compile ( '<li class="col-md-6 col-xs-12 list-movies-li"><a href="(.+?)" title=".+?">(.+?)<span class="epnum">.+?</span></a></li>' , re . DOTALL ) . findall ( o00OO00OoO )
 I1 = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="(.+?)">Next</a></li></ul>' , re . DOTALL ) . findall ( o00OO00OoO )
 for url , ooo in Ii1i :
  II1I ( '[COLORgreen]' + ( ooo ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' ) + '[/COLOR]' , 'http://www.watchseries.li' + url , 10044 , ooOooo000oOO + 'WATCHSERIES.png' , '' , '' )
 for url in I1 :
  II1I ( '[COLORgreen]' + 'NEXT' + '[/COLOR]' , 'http://www.watchseries.li' + url , 10049 , ooOooo000oOO + 'Next.png' , '' , '' )
  if 87 - 87: OooO0OoOOOO
  if 17 - 17: Ii11Ii1I / iI11I1II1I1I - oO0o + oOo0O0Ooo % IIIii1II1II
def III1III11II ( ) :
 IIiI1i1i = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 iIi1iI = 'http://www.watchseries.li/search/' + IIiI1i1i . replace ( ' ' , '%20' )
 o00OO00OoO = iiI111I1iIiI ( iIi1iI )
 Ii1i = re . compile ( '<img src="(.+?)".+?<a href="(.+?)" title=".+?"><b>(.+?)</b>' , re . DOTALL ) . findall ( o00OO00OoO )
 for I1II1I11I1I , Ii1II1I11i1 , ooo in Ii1i :
  if 'watch online' in ooo :
   pass
  else :
   print Ii1II1I11i1
   II1I ( '[COLORgreen]' + ooo + '[/COLOR]' , 'http://www.watchseries.li' + Ii1II1I11i1 , 10044 , I1II1I11I1I , '' , '' )
   if 63 - 63: oO0o / OOooOOo * iI11I1II1I1I . IIIi
   xbmcplugin . setContent ( O0O , 'movies' )
   if 85 - 85: Ii / Ii . oO0o . o0o00Oo0O
def OooOo ( url ) :
 o00OO00OoO = iiI111I1iIiI ( url )
 Ii1i = re . compile ( '<img src="(.+?)".+?<div class="block-left-home-inside-text">.+?<a href="(.+?)" title=".+?"><b>(.+?)</b> <br>.+?<span class=".+?">(.+?)</span></a><br>(.+?)<br>' , re . DOTALL ) . findall ( o00OO00OoO )
 for I1II1I11I1I , url , ooo , O00O , iiIII1i in Ii1i :
  oOo0 = ( ooo ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' ) + ' - ' + ( O00O ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' )
  II1I ( '[COLORgreen]' + oOo0 + '[/COLOR]' , 'http://www.watchseries.li' + url , 10045 , I1II1I11I1I , '' , iiIII1i )
  if 30 - 30: IIIii1II1II + IIiIiII11i - OooO0OoOOOO * ii
def I1iIiiiI1 ( url ) :
 o00OO00OoO = iiI111I1iIiI ( url )
 Ii1i = re . compile ( '<li class="col-md-6 col-xs-12 list-movies-li"><a href="(.+?)" title=".+?">(.+?)<span class="epnum">.+?</span></a></li>' , re . DOTALL ) . findall ( o00OO00OoO )
 I1 = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="(.+?)">Next</a></li></ul>' , re . DOTALL ) . findall ( o00OO00OoO )
 for url , ooo in Ii1i :
  oOo0 = ( ooo ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' )
  II1I ( '[COLORgreen]' + oOo0 + '[/COLOR]' , 'http://www.watchseries.li' + url , 10045 , ooOooo000oOO + 'WATCHSERIES.png' , '' , '' )
 for url in I1 :
  II1I ( '[COLORgreen]' + 'NEXT' + '[/COLOR]' , 'http://www.watchseries.li' + url , 10046 , ooOooo000oOO + 'Next.png' , '' , '' )
  if 87 - 87: OOooOOo - O0OoO - IIIii1II1II + I1ii11iIi11i % iI11I1II1I1I / Ii
def i1iIIII1iiIIi ( url ) :
 o00OO00OoO = iiI111I1iIiI ( url )
 Ii1i = re . compile ( '<div class="mask">.+?<a href="(.+?)" title="(.+?)">.+?<img src="(.+?)"' , re . DOTALL ) . findall ( o00OO00OoO )
 I1 = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="(.+?)">Next</a></li></ul>' , re . DOTALL ) . findall ( o00OO00OoO )
 for url , ooo , I1II1I11I1I in Ii1i :
  II1I ( '[COLORgreen]' + ( ooo ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' ) + '[/COLOR]' , 'http://www.watchseries.li' + url , 10044 , I1II1I11I1I , '' , '' )
 for url in I1 :
  II1I ( '[COLORgreen]' + 'NEXT' + '[/COLOR]' , 'http://www.watchseries.li' + url , 10041 , ooOooo000oOO + 'Next.png' , '' , '' )
  if 17 - 17: iI1iI1I1i1I
def oOoO0ooO0000 ( url ) :
 o00OO00OoO = iiI111I1iIiI ( url )
 i1I1iIi = re . compile ( '<div class="col-md-6 col-xs-12".+?<a href=".+?" itemprop="url"><span itemprop="name">(.+?)</span>(.+?)</ul>' , re . DOTALL ) . findall ( o00OO00OoO )
 for oOOoOOO0oo0 , OOo00OO00Oo in i1I1iIi :
  Ii1i = re . compile ( '<li itemprop="episode".+?<meta itemprop="url" content="(.+?)">.+?<span class="" itemprop="name">\n(.+?)\n' , re . DOTALL ) . findall ( str ( OOo00OO00Oo ) )
  for url , ooo in Ii1i :
   oOo0 = ( oOOoOOO0oo0 ) . replace ( '  ' , '' ) + ' ' + ( ooo ) . replace ( '&nbsp;' , ' ' ) . replace ( '&#039;' , '\'' ) . replace ( '  ' , '' )
   II1I ( '[COLORgreen]' + oOo0 + '[/COLOR]' , 'http://www.watchseries.li' + url , 10045 , ooOooo000oOO + 'WATCHSERIES.png' , '' , '' )
 I1 = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="(.+?)">Next</a></li></ul>' , re . DOTALL ) . findall ( o00OO00OoO )
 for url in I1 :
  II1I ( '[COLORgreen]' + 'NEXT' + '[/COLOR]' , 'http://www.watchseries.li' + url , 10044 , ooOooo000oOO + 'Next.png' , '' , '' )
  if 60 - 60: OOooOOo / Ii1I + IIIii1II1II - o0oOO0O00o0O
  if 49 - 49: oO0o - o0o00Oo0O / oO0o * OOooOOo + IIIi
class Iiii1I ( ) :
 if 61 - 61: iI11I1II1I1I - iI1iI1I1i1I / o0oOO0O00o0O * iI1iI1I1i1I % Ii11Ii1I % o0oOO0O00o0O
 List = [ ]
 source_list = [ ]
 def __init__ ( self , name ) :
  if 63 - 63: IIIii1II1II % iI11I1II1I1I
  oOo0 = name
  self . Get_Sources ( Ii1II1I11i1 , oOo0 )
  if 20 - 20: oO0o . oOo0O0Ooo * Ii / Ii
  if 89 - 89: o0oOO0O00o0O . Ii * o0o00Oo0O
 def Get_Sources ( self , URL , season_name ) :
  Oo0oO0ooo = xbmcgui . DialogProgress ( )
  o00OO00OoO = iiI111I1iIiI ( URL )
  Ii1i = re . compile ( '<td>.+?<a href="/link/(.+?)".+?height="16px">(.+?)\n' , re . DOTALL ) . findall ( o00OO00OoO )
  for Ii1II1I11i1 , ooo in Ii1i :
   URL = 'http://www.watchseries.li/link/' + Ii1II1I11i1
   self . Get_site_link ( URL , season_name )
   if 44 - 44: ooOoO0O00 . oOo0O0Ooo / Ii + OooO0OoOOOO
 def Get_site_link ( self , url , season_name ) :
  o00OO00OoO = iiI111I1iIiI ( url )
  Ii1i = re . compile ( '<iframe style=.+?" src="(.+?)"' ) . findall ( o00OO00OoO )
  I1 = re . compile ( '<IFRAME SRC="(.+?)"' ) . findall ( o00OO00OoO )
  II1Ii = re . compile ( '<IFRAME style=".+?" SRC="(.+?)"' ) . findall ( o00OO00OoO )
  for url in Ii1i :
   self . main ( url , season_name )
  for url in I1 :
   self . main ( url , season_name )
  for url in II1Ii :
   self . main ( url , season_name )
   if 27 - 27: IIIii1II1II
 def main ( self , url , season_name ) :
  Oo0oO0ooo . create ( "[COLORwhite]Origin[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
  if 'daclips.in' in url :
   O0OO0ooO00 = 'DACLIPS'
   if O0OO0ooO00 in Iiii1I . source_list :
    pass
   else :
    self . daclips ( url , season_name , O0OO0ooO00 )
    Oo0oO0ooo . update ( 0 , "" , "Getting Daclips Links" )
  else :
   if 'filehoot.com' in url :
    O0OO0ooO00 = 'FILEHOOT'
    if O0OO0ooO00 in Iiii1I . source_list :
     pass
    else :
     Oo0oO0ooo . update ( 0 , "" , "Getting Filehoot Links" )
     self . filehoot ( url , season_name , O0OO0ooO00 )
   else :
    if 'thevideo.me' in url :
     O0OO0ooO00 = 'THEVIDEO'
     if O0OO0ooO00 in Iiii1I . source_list :
      pass
     else :
      self . thevideo ( url , season_name , O0OO0ooO00 )
      Oo0oO0ooo . update ( 0 , "" , "Getting Thevideo Links" )
    else :
     if 'allmyvideos.net' in url :
      O0OO0ooO00 = 'ALLMYVIDEOS'
      if O0OO0ooO00 in Iiii1I . source_list :
       pass
      else :
       self . allmyvid ( url , season_name , O0OO0ooO00 )
       Oo0oO0ooo . update ( 0 , "" , "Getting Allmyvideo Links" )
     else :
      if 'vidspot.net' in url :
       O0OO0ooO00 = 'VIDSPOT'
       if O0OO0ooO00 in Iiii1I . source_list :
        pass
       else :
        self . vidspot ( url , season_name , O0OO0ooO00 )
        Oo0oO0ooo . update ( 0 , "" , "Getting Vidspot Links" )
      else :
       if 'vodlocker' in url :
        O0OO0ooO00 = 'VODLOCKER'
        if O0OO0ooO00 in Iiii1I . source_list :
         pass
        else :
         self . vodlocker ( url , season_name , O0OO0ooO00 )
         Oo0oO0ooo . update ( 0 , "" , "Getting Vodlocker Links" )
         if 83 - 83: iI11I1II1I1I
         if 63 - 63: ii * oO0o / iI1iI1I1i1I - OoOo00o . iI11I1II1I1I + o0oOO0O00o0O
 def allmyvid ( self , url , season_name , source_name ) :
  o00OO00OoO = iiI111I1iIiI ( url )
  Ii1i = re . compile ( '"file" : "(.+?)",\n.+?"default" : .+?,\n.+?"label" : "(.+?)"' , re . DOTALL ) . findall ( o00OO00OoO )
  for ii1IIiI1IIi , ooo in Ii1i :
   self . Printer ( ii1IIiI1IIi , season_name , source_name )
   if 76 - 76: o0oOO0O00o0O / oO0o + OOooOOo
 def vidspot ( self , url , season_name , source_name ) :
  o00OO00OoO = iiI111I1iIiI ( url )
  Ii1i = re . compile ( '"file" : "(.+?)",\n.+?"default" : .+?,\n.+?"label" : "(.+?)"' ) . findall ( o00OO00OoO )
  for ii1IIiI1IIi , ooo in Ii1i :
   self . Printer ( ii1IIiI1IIi , season_name , source_name )
   if 86 - 86: Ii + Ii . IIIi % oOo0O0Ooo . O0OoO
 def thevideo ( self , url , season_name , source_name ) :
  o00OO00OoO = iiI111I1iIiI ( url )
  Ii1i = re . compile ( "{ label: '.+?', file: '(.+?)' }" ) . findall ( o00OO00OoO )
  for ii1IIiI1IIi in Ii1i :
   self . Printer ( ii1IIiI1IIi , season_name , source_name )
   if 17 - 17: Ii11Ii1I
 def vodlocker ( self , url , season_name , source_name ) :
  o00OO00OoO = iiI111I1iIiI ( url )
  Ii1i = re . compile ( 'file: "(.+?)",.+?skin' , re . DOTALL ) . findall ( o00OO00OoO )
  for ii1IIiI1IIi in Ii1i :
   self . Printer ( ii1IIiI1IIi , season_name , source_name )
   if 67 - 67: o0o00Oo0O * iI1iI1I1i1I - I11i - IIiIiII11i
 def daclips ( self , url , season_name , source_name ) :
  o00OO00OoO = iiI111I1iIiI ( url )
  Ii1i = re . compile ( '{ file: "(.+?)", type:"video" }' ) . findall ( o00OO00OoO )
  for ii1IIiI1IIi in Ii1i :
   self . Printer ( ii1IIiI1IIi , season_name , source_name )
   if 41 - 41: oOo0O0Ooo - IIIi % IIiIiII11i . IIIi - iI1iI1I1i1I
 def filehoot ( self , url , season_name , source_name ) :
  o00OO00OoO = iiI111I1iIiI ( url )
  Ii1i = re . compile ( 'file: "(.+?)",.+?skin' , re . DOTALL ) . findall ( o00OO00OoO )
  for ii1IIiI1IIi in Ii1i :
   self . Printer ( ii1IIiI1IIi , season_name , source_name )
   if 45 - 45: Ii11Ii1I - IIIii1II1II
 def Printer ( self , Link , season_name , source_name ) :
  if 70 - 70: oO0o % oOo0O0Ooo / oOo0O0Ooo . iI1iI1I1i1I % O0OoO . IIiIiII11i
  if Link in Iiii1I . List :
   pass
  elif source_name in Iiii1I . source_list :
   pass
  else :
   oOO0oo ( '[COLORgreen]' + source_name + '[/COLOR]' , Link , 10012 , ooOooo000oOO + 'WATCHSERIES.png' )
   Oo0oO0ooo . update ( 100 , "" , "Got Source" )
   Iiii1I . List . append ( Link )
   Iiii1I . source_list . append ( source_name )
   if 10 - 10: Ii11Ii1I - Ii . Ii1I % ooOoO0O00
   xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
   if 78 - 78: iI11I1II1I1I * I1ii11iIi11i . I1ii11iIi11i - IIIii1II1II . iI11I1II1I1I
   if 30 - 30: O0OoO + O0OoO % OooO0OoOOOO - I11i - Ii1I
   if 36 - 36: iI1iI1I1i1I % IIIii1II1II
   if 72 - 72: oOo0O0Ooo / o0oOO0O00o0O - o0o00Oo0O + iI1iI1I1i1I
   if 83 - 83: o0o00Oo0O
def oOOOOOo ( ) :
 II1I ( '[COLORgreen]Highlights[/COLOR]' , '' , 10008 , ooOooo000oOO + 'ORIGINFOOTBALL.png' , i1iiIII111ii , '' )
 II1I ( '[COLORgreen]Fixtures[/COLOR]' , '' , 10009 , ooOooo000oOO + 'ORIGINFOOTBALL.png' , i1iiIII111ii , '' )
 if 50 - 50: IIIi + O0OoO + o0oOO0O00o0O
def ii11iiI11I ( ) :
 OO0O00oOo = iiI111I1iIiI ( i1111 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20vcXVpY2tpbmRleC5odG1s' ) )
 Ii1i = re . compile ( '<a target="_self" href="(.+?)".+?src="(.+?)" alt="(.+?)"' , re . DOTALL ) . findall ( OO0O00oOo )
 for Ii1II1I11i1 , I1II1I11I1I , ooo in Ii1i :
  II1I ( '[COLORgreen]' + ( ooo ) . replace ( 'amp;' , '' ) + '[/COLOR]' , i1111 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20v' ) + Ii1II1I11i1 , 10010 , i1111 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20v' ) + I1II1I11I1I , i1iiIII111ii , '' )
  if 96 - 96: iI11I1II1I1I + Ii - I1ii11iIi11i . O0OoO
def iiIi11i1IiI ( url ) :
 o00OO00OoO = iiI111I1iIiI ( url )
 i1I1iIi = re . compile ( 'AndClearL.+?><h2.+?head>(.*?)float' , re . DOTALL ) . findall ( o00OO00OoO )
 for i1I1iIi in i1I1iIi :
  oO00O0O0 = re . compile ( '(.*?)</h2>' ) . findall ( str ( i1I1iIi ) )
  for oO0o0OO in oO00O0O0 :
   oO0o0OO = oO0o0OO
  i111I11I = re . compile ( 'comp_head>(.*?)</span>.*?<div class = fLeft width = ".*?"><img src="(.*?)">.*?</div>.*?ST:(.*?)</div>(.+?)<!-- around all of channel types ENDS 2-->' , re . DOTALL ) . findall ( str ( i1I1iIi ) )
  for OoOoOOoO , I1II1I11I1I , time , ii1ii1i11I1I in i111I11I :
   Ii111 = re . compile ( ",CAPTION, '(.+?)&nbsp" ) . findall ( ii1ii1i11I1I )
   II1I ( '[COLORgreen]' + oO0o0OO + ' - ' + OoOoOOoO + ' - ' + time + '[/COLOR]' , '' , 10010 , i1111 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20=' ) + I1II1I11I1I , i1iiIII111ii , ( str ( Ii111 ) ) )
   if 41 - 41: OooO0OoOOOO
 iiO0o0oOOOoOo ( 'tvshows' , 'Media Info 3' )
 if 3 - 3: OooO0OoOOOO + IIiIiII11i / iI11I1II1I1I
def iiiiIii ( ) :
 if 6 - 6: oO0o / I1ii11iIi11i / o0oOO0O00o0O
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
 if 13 - 13: Ii1I % OOooOOo
def ooOii1i11 ( url ) :
 o00OO00OoO = iiI111I1iIiI ( url )
 Ii1i = re . compile ( 'itemprop="image" class="entry-thumb" src="(.+?)".+?<h3 itemprop="name" class="entry-title td-module-title"><a itemprop="url" href="(.+?)" rel="bookmark" title=".+?">(.+?)</a></h3>' , re . DOTALL ) . findall ( o00OO00OoO )
 for I1II1I11I1I , url , ooo in Ii1i :
  IiIiIi1I11I = ooo . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' )
  oOO0oo ( '[COLORgreen]' + IiIiIi1I11I + '[/COLOR]' , url , 10013 , I1II1I11I1I )
  if 43 - 43: Ii + o0oOO0O00o0O + O0OoO / IIIi . Ii1I + o0oOO0O00o0O
def iIIi1IiIi ( url ) :
 o00OO00OoO = iiI111I1iIiI ( url )
 Ii1i = re . compile ( '<script data-config="(.+?)" data-height' ) . findall ( o00OO00OoO )
 for OO0O0OOo0O in Ii1i :
  III1i = ( OO0O0OOo0O ) . replace ( '/v2' , '' ) . replace ( 'zeus.json' , 'video-sd.mp4?hosting_id=21772' ) . replace ( 'config.playwire.com' , 'cdn.video.playwire.com' )
  i1iii11 ( 'http:' + III1i )
  if 69 - 69: Ii11Ii1I / ooOoO0O00 + O0OoO
  if 35 - 35: Ii - OoOo00o % Ii
def II111I1Iii ( url ) :
 OO0O00oOo = ii1II ( url )
 Ii1i = re . compile ( '<a href="([^"]*)" title="([^"]*)"><img itemprop="image" content="([^"]*)"' , re . DOTALL ) . findall ( OO0O00oOo )
 I1 = re . compile ( "<a rel='next' href=([^=]*)=" , re . DOTALL ) . findall ( OO0O00oOo )
 for url , ooo , I1II1I11I1I in Ii1i :
  oOO0oo ( ooo , url , 8046 , I1II1I11I1I )
 for url in I1 :
  II1Ii1iI1i1 ( 'NEXT PAGE' , ( url ) . replace ( ' class' , '' ) , 8045 , ooOooo000oOO + 'Next.png' )
def OO00Oo00oO ( url ) :
 OO0O00oOo = ii1II ( url )
 Ii1i = re . compile ( "__filename='([^']*)',.+?__fullimage='([^']*)',.+?__title='([^']*)'," , re . DOTALL ) . findall ( OO0O00oOo )
 for url , I1II1I11I1I , ooo in Ii1i :
  i1iii11 ( 'http://bitcast-b.bitgravity.com/ndtvod/23372/ndtv/' + url )
  if 94 - 94: Ii / IIIi / I1ii11iIi11i
def I1iII ( url ) :
 OO0O00oOo = ii1II ( url )
 Ii1i = re . compile ( "src='http://www.youtube.com/embed/(.+?)?version=3&#038;rel=1&#038;fs=1&#038;autohide=2&#038;showsearch=0&#038;showinfo=1&#038;iv_load_policy=1&#038;wmode=transparent' frameborder='0' allowfullscreen='true'></iframe>" ) . findall ( OO0O00oOo )
 for url in Ii1i :
  yt . PlayVideo ( url )
  if 29 - 29: ooOoO0O00 % o0oOO0O00o0O / OooO0OoOOOO + OOooOOo - IIIii1II1II - Ii1I
def OoiiI1i111 ( ) :
 OO0O00oOo = ii1II ( i1111 ( 'aHR0cDovL3RvcGRvY3VtZW50YXJ5ZmlsbXMuY29tLw==' ) )
 Ii1i = re . compile ( '<a href="(.+?)" >(.+?)</a></li><li>' ) . findall ( OO0O00oOo )
 for Ii1II1I11i1 , ooo in Ii1i :
  II1Ii1iI1i1 ( ooo , Ii1II1I11i1 , 8041 , ooOooo000oOO + 'documentary.png' )
def oO0O0o0O ( url ) :
 OO0O00oOo = ii1II ( url )
 Ii1i = re . compile ( '<h2><a href="(.+?)" title="(.+?)">.+?</a></h2>.+?src="(.+?)"' , re . DOTALL ) . findall ( OO0O00oOo )
 I1 = re . compile ( 'class="inactive">.+?</a><a href="(.+?)">Next</a></div>' , re . DOTALL ) . findall ( OO0O00oOo )
 for url , ooo , I1II1I11I1I in Ii1i :
  II1Ii1iI1i1 ( ( ooo ) . replace ( '&#039;s' , '' ) , url , 8042 , I1II1I11I1I )
 for url in I1 :
  II1Ii1iI1i1 ( 'NEXT PAGE' , url , 8041 , ooOooo000oOO + 'Next.png' )
  if 100 - 100: OOooOOo % I1ii11iIi11i
  if 76 - 76: IIiIiII11i / oO0o + ii . Ii1I . iI1iI1I1i1I . O0OoO
def iiiI ( url ) :
 OO0O00oOo = ii1II ( url )
 Ii1i = re . compile ( '<meta itemprop="name" content="(.+?)".+?<meta itemprop="thumbnailUrl" content="(.+?)".+?<meta itemprop="embedUrl" content="(.+?)".+?<meta itemprop="description" content="(.+?)" />' , re . DOTALL ) . findall ( OO0O00oOo )
 I1 = re . compile ( '<div class="video new-video"><iframe width="766" height="431" src="(.+?)&iv_load_policy=3&showinfo=0&autohide=1"' , re . DOTALL ) . findall ( OO0O00oOo )
 for ooo , I1II1I11I1I , url , i111i1i in Ii1i :
  oOO0oo ( ( ooo ) . replace ( '&#039;s' , '' ) , url . replace ( 'https://www.youtube.com/embed/' , '' ) , 8043 , I1II1I11I1I )
 for url in I1 :
  iIIIiiiIiI1 ( ( url ) . replace ( '//' , 'http://' ) )
  if 95 - 95: Ii11Ii1I - Ii1I - o0o00Oo0O . oOo0O0Ooo . o0oOO0O00o0O
def iIIIiiiIiI1 ( url ) :
 OO0O00oOo = ii1II ( url )
 Ii1i = re . compile ( '<link rel="canonical" href="(.+?)">  <link rel="stylesheet"' ) . findall ( OO0O00oOo )
 for url in Ii1i :
  oOO0oo ( 'PLAY' , ( url ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , ooOooo000oOO + 'documentary.png' )
  if 7 - 7: IIIi
def ii1IiIi1i ( ) :
 o00OO00OoO = ii1II ( 'http://www.stream2watch.co/live-tv' )
 Ii1i = re . compile ( '<a href="(.+?)">.+?<img src="(.+?)" alt=".+?"/>.+?<span class="country_name">(.+?)<br />(.+?)</span>' , re . DOTALL ) . findall ( o00OO00OoO )
 for Ii1II1I11i1 , I1II1I11I1I , ooo , OOOO00OoooO in Ii1i :
  II1Ii1iI1i1 ( ( ooo + '[COLORgreen]' + OOOO00OoooO + '[/COLOR]' ) , Ii1II1I11i1 , 8086 , I1II1I11I1I )
  if 7 - 7: Ii1I / IIiIiII11i - iI1iI1I1i1I + ooOoO0O00 + Ii11Ii1I
def i11i11i ( url ) :
 o00OO00OoO = ii1II ( url )
 Ii1i = re . compile ( '<a class="front_channel_href" href="(.+?)" title=".+?">.+?<img class="front_channel_thumb" src="(.+?)" alt=".+?"/>.+?<span class="front_channel_name">(.+?)</span>' , re . DOTALL ) . findall ( o00OO00OoO )
 for url , I1II1I11I1I , ooo in Ii1i :
  II1Ii1iI1i1 ( '[COLORgreen]' + ooo + '[/COLOR]' , url , 8087 , I1II1I11I1I )
  if 31 - 31: Ii + IIIii1II1II - o0o00Oo0O
def OOoo00O000Oo ( url ) :
 o00OO00OoO = iiI111I1iIiI ( url )
 Ii1i = re . compile ( 'a id="code_.+?data-f-href="(.+?)" data-code-embed="">(.+?)</a>' , re . DOTALL ) . findall ( o00OO00OoO )
 for url , ooo in Ii1i :
  OOoO0oooo ( url , ooo )
  if 24 - 24: iI1iI1I1i1I / oOo0O0Ooo * ooOoO0O00 % ii
def OOoO0oooo ( url , name ) :
 o00OO00OoO = iiI111I1iIiI ( url )
 Ii1i = re . compile ( "playStream\('.+?', '(.+?)'\);" , re . DOTALL ) . findall ( o00OO00OoO )
 for url in Ii1i :
  print url
  oOO0oo ( '[COLORgreen]' + name + '[/COLOR]' , url , 222 , '' )
  if 99 - 99: Ii . IIiIiII11i . ii
def Ooi1IIii11i1I1 ( ) :
 OO0O00oOo = ii1II ( i1111 ( 'aHR0cDovL3d3dy5zb2xpZS5vcmcvYWxpYnJhcnkvaW5kZXguaHRtbA==' ) )
 Ii1i = re . compile ( '<td align="center" valign="top">.+?<a href="(.+?)">.+?<img src="(.+?)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( OO0O00oOo )
 for Ii1II1I11i1 , I1II1I11I1I , ooo in Ii1i :
  II1Ii1iI1i1 ( ( '[COLORgreen]' + ooo + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + Ii1II1I11i1 , 3002 , 'http://www.solie.org/alibrary/' + I1II1I11I1I )
def Ii1I1 ( url ) :
 OO0O00oOo = ii1II ( url )
 Ii1i = re . compile ( '<td align="center" valign="top">.+?<a href="(.+?)">.+?<img src="(.+?)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( OO0O00oOo )
 for url , I1II1I11I1I , ooo in Ii1i :
  II1Ii1iI1i1 ( ( '[COLORgreen]' + ooo + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3003 , 'http://www.solie.org/alibrary/' + I1II1I11I1I )
def O0oo00oOOO0o ( url ) :
 OO0O00oOo = ii1II ( url )
 Ii1i = re . compile ( '<br><a href="([^"]*)">(.+?)</a>' ) . findall ( OO0O00oOo )
 II1i = re . compile ( 'href="([^"]*)">Season(.+?)</a>' ) . findall ( OO0O00oOo )
 next = re . compile ( '<a href="([^"]*)">Episodes</a>' ) . findall ( OO0O00oOo )
 I1 = re . compile ( '<td align="center" valign="top">.+?<a href="(.+?)">.+?<img src="(.+?)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( OO0O00oOo )
 for url , ooo in Ii1i :
  oOO0oo ( ( '[COLORgreen]' + ooo + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3004 , ooOooo000oOO + 'classicmovies.png' )
 for url , ooo in II1i :
  II1Ii1iI1i1 ( '[COLORgreen]Season- ' + ooo + '[/COLOR]' , 'http://www.solie.org/alibrary/' + url , 3003 , ooOooo000oOO + 'classicmovies.png' )
 for url in next :
  II1Ii1iI1i1 ( '[COLORgreen]NEXT[/COLOR]' , 'http://www.solie.org/alibrary/' + url , 3003 , ooOooo000oOO + 'Next.png' )
 for url , I1II1I11I1I , ooo in I1 :
  II1Ii1iI1i1 ( ( '[COLORgreen]' + ooo + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3003 , 'http://www.solie.org/alibrary/' + I1II1I11I1I )
def I111iiIIiI1I ( url ) :
 OO0O00oOo = ii1II ( url )
 Ii1i = re . compile ( '<iframe.+?src="([^"]*)"' ) . findall ( OO0O00oOo )
 for url in Ii1i :
  ooO00Oo ( url )
def ooO00Oo ( url ) :
 OO0O00oOo = ii1II ( url )
 Ii1i = re . compile ( '<meta property="og:video" content="([^"]*)"/>' ) . findall ( OO0O00oOo )
 for url in Ii1i :
  i1iii11 ( url )
  if 41 - 41: Ii - ooOoO0O00 / I1ii11iIi11i * OooO0OoOOOO / IIIi - I1ii11iIi11i
def oOOoOOO0oOoo ( ) :
 OO0O00oOo = ii1II ( i1111 ( 'aHR0cDovL3JldHJvdmlzaW9uLnR2L2FsbC8=' ) )
 Ii1i = re . compile ( '<a href="([^"]*)"><h2><font color=".+?"><h2>(.+?)</font></h2></a>' ) . findall ( OO0O00oOo )
 for Ii1II1I11i1 , ooo in Ii1i :
  oOO0oo ( ( '[COLORgreen]' + ooo + '[/COLOR]' ) . replace ( '&#8211;' , ':' ) , Ii1II1I11i1 , 8061 , ooOooo000oOO + 'classicmovies.png' )
def o0O0ooooooo00 ( url ) :
 OO0O00oOo = ii1II ( url )
 Ii1i = re . compile ( "v.src = '([^']*)';" ) . findall ( OO0O00oOo )
 for url in Ii1i :
  i1iii11 ( url )
  if 28 - 28: O0OoO * iI1iI1I1i1I % Ii * o0oOO0O00o0O / Ii11Ii1I
def iIII1iIi ( ) :
 OO0O00oOo = ii1II ( i1111 ( 'aHR0cDovL3JldHJvdmlzaW9uLnR2L2NsYXNzaWMtdHYv' ) )
 Ii1i = re . compile ( '<a href="([^"]*)"><h2><font color=".+?"><h2>(.+?)</font></h2></a>' ) . findall ( OO0O00oOo )
 for Ii1II1I11i1 , ooo in Ii1i :
  oOO0oo ( ( '[COLORgreen]' + ooo + '[/COLOR]' ) . replace ( '&#8211;' , ':' ) , Ii1II1I11i1 , 8061 , ooOooo000oOO + 'classictv.png' )
def o000O0oo ( url ) :
 OO0O00oOo = ii1II ( url )
 Ii1i = re . compile ( "v.src = '([^']*)';" ) . findall ( OO0O00oOo )
 for url in Ii1i :
  i1iii11 ( url )
  if 78 - 78: oO0o / I1ii11iIi11i - iI11I1II1I1I - Ii * o0oOO0O00o0O
def o0O0Ooo ( ) :
 o00OO00OoO = iiI111I1iIiI ( i1111 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vbTN1c3RyZWFtcw==' ) )
 Ii1i = re . compile ( '<li><a href="(.+?)"> (.+?).m3u</a></li>' ) . findall ( o00OO00OoO )
 for Ii1II1I11i1 , ooo in Ii1i :
  II1Ii1iI1i1 ( ( '[COLORgreen]' + ooo + '[/COLOR]' ) . replace ( '-' , ' ' ) . replace ( '_' , ' ' ) , ( i1111 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vbTN1c3RyZWFtcy8=' ) ) + Ii1II1I11i1 , 8071 , ooOooo000oOO + 'streams.png' )
def O0o ( url ) :
 o00OO00OoO = ii1II ( url )
 Ii1i = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( o00OO00OoO )
 for ooo , url in Ii1i :
  oOO0oo ( ( '[COLORgreen]' + ooo + '[/COLOR]' ) . replace ( '_' , ' ' ) , ( url ) . strip ( ) , 404 , ooOooo000oOO + 'streams.png' )
def O00oOOooO ( url ) :
 o00OO00OoO = ii1II ( url )
 Ii1i = re . compile ( 'EXTINF:(.+?),(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( o00OO00OoO )
 for I1II1I11I1I , ooo , url in Ii1i :
  url = ( ( i1111 ( 'aHR0cDovL3BpZXN1c3R2Lm5ldDo4MDAwL2xpdmUv' ) ) + oO0o0o0ooO0oO + '/' + oo0o0O00 + url ) . strip ( )
  oOO0oo ( ( '[COLORgreen]' + ooo + '[/COLOR]' ) . replace ( '_' , ' ' ) , url , 10012 , I1II1I11I1I )
  if 46 - 46: iI11I1II1I1I . Ii - OOooOOo % o0o00Oo0O / IIiIiII11i * ooOoO0O00
def oOIiiIIi ( ) :
 ii1iI1iI1 ( 'Best Videos' , 'http://www.xvideos.com/best' , 10105 , ooOooo000oOO + 'JIZBOX.png' , '' , '' )
 ii1iI1iI1 ( 'Genres' , 'http://www.xvideos.com' , 10106 , ooOooo000oOO + 'JIZBOX.png' , '' , '' )
 ii1iI1iI1 ( 'Recently Uploaded' , 'http://xvideos.com' , 10105 , ooOooo000oOO + 'JIZBOX.png' , '' , '' )
 ii1iI1iI1 ( 'Tags' , 'http://www.xvideos.com/tags' , 10103 , ooOooo000oOO + 'JIZBOX.png' , '' , '' )
 ii1iI1iI1 ( 'Search' , '' , 10107 , ooOooo000oOO + 'JIZBOX.png' , '' , '' , )
 if 96 - 96: ooOoO0O00 . iI1iI1I1i1I + OoOo00o + Ii1I * IIIii1II1II - IIiIiII11i
def iIO0OO0o0O00oO ( url ) :
 o00OO00OoO = iiI111I1iIiI ( url )
 o00O = re . compile ( '<li><a class=".+?".+?href="(.+?)">Next</a></li>' ) . findall ( o00OO00OoO )
 for url in o00O :
  ii1iI1iI1 ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10103 , ooOooo000oOO + 'JIZBOX.png' , '' , '' )
 Ii1i = re . compile ( '<li><a href="(.+?)"><b>(.+?)</b><span class="navbadge default"(.+?)</span>' ) . findall ( o00OO00OoO )
 for url , ooo , i1i1iI1iiiI in Ii1i :
  ii1iI1iI1 ( ooo + ' - No of Videos : ' + ( i1i1iI1iiiI ) . replace ( '>' , '' ) , 'http://www.xvideos.com' + url , 10105 , ooOooo000oOO + 'JIZBOX.png' , '' , '' )
  if 92 - 92: I1ii11iIi11i - IIIi
def IIi11 ( url ) :
 o00OO00OoO = iiI111I1iIiI ( url )
 o00O = re . compile ( 'href="([^"]*)">Next</a></li>' ) . findall ( o00OO00OoO )
 for url in o00O :
  ii1iI1iI1 ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10104 , ooOooo000oOO + 'Next.png' , '' , '' )
 Ii1i = re . compile ( ':"([^"]*)".+?;</script></a></div></div><p class="profile-name"><a href="([^"]*)">(.+?)</a></p><p class="profile-counts">\n(.+?)\n' , re . DOTALL ) . findall ( o00OO00OoO )
 for I1II1I11I1I , url , ooo , o0O0oo0 in Ii1i :
  ii1iI1iI1 ( ooo + '--' + o0O0oo0 , 'http://www.xvideos.com' + url + '#_tabVideos,videos-best' , 10105 , ( I1II1I11I1I ) . replace ( 'http:\/\/' , 'http://' ) , '' , '' )
  if 33 - 33: I11i / o0o00Oo0O + IIIii1II1II
  if 75 - 75: OooO0OoOOOO % Ii + iI11I1II1I1I
def oOoOo0o00o ( url ) :
 o00OO00OoO = iiI111I1iIiI ( url )
 Ii1i = re . compile ( '<div class="thumb-inside"><script>.+?<img src="(.+?)".+?<a href="(.+?)" title=".+?">(.+?)</a></p>.+?uration">(.+?)</span>.+?Porn quality:(.+?)</span>' , re . DOTALL ) . findall ( o00OO00OoO )
 for I1II1I11I1I , url , ooo , oOoooooOoO , iIIi1 in Ii1i :
  ooOOoooooo ( ooo + ' - Porn Quality : ' + iIIi1 + ' - ' + oOoooooOoO , 'http://www.xvideos.com' + url , 10108 , I1II1I11I1I , I1II1I11I1I , iIIi1 + ' - ' + oOoooooOoO )
 ooo0o0 = re . compile ( '<li><a href="([^"]*)" class="no-page">Next</a></li></ul></div>' ) . findall ( o00OO00OoO )
 for url in ooo0o0 :
  ii1iI1iI1 ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10105 , ooOooo000oOO + 'Next.png' , '' , '' )
  if 84 - 84: iI1iI1I1i1I - I1ii11iIi11i * o0o00Oo0O / Ii11Ii1I . Ii11Ii1I
def ooO0 ( url ) :
 o00OO00OoO = iiI111I1iIiI ( url )
 i1I1iIi = re . compile ( '<div class="main-categories">(.+?)</div>' , re . DOTALL ) . findall ( o00OO00OoO )
 o00O = re . compile ( '<li><a class=".+?".+?href="(.+?)">Next</a></li>' ) . findall ( o00OO00OoO )
 for url in o00O :
  ii1iI1iI1 ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10106 , ooOooo000oOO + 'Next.png' , '' , '' )
 Ii1i = re . compile ( '<li><a href="(.+?)" class="btn btn-default">(.+?)</a>' ) . findall ( str ( i1I1iIi ) )
 for url , ooo in Ii1i :
  ii1iI1iI1 ( ooo , 'http://www.xvideos.com' + url , 10105 , ooOooo000oOO + 'JIZBOX.png' , '' , '' )
  if 34 - 34: ooOoO0O00 % OooO0OoOOOO
  if 80 - 80: ii / iI11I1II1I1I + Ii1I / ooOoO0O00 / I11i
def oOoO ( ) :
 IIiI1i1i = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 ii1IIii = ( IIiI1i1i ) . replace ( ' ' , '+' ) . replace ( '&' , '&' )
 IiII111i1i11 = ii1IIii . lower ( )
 IiI11i1I11111 = 'http://www.xvideos.com/?k=' + IiII111i1i11
 print IiI11i1I11111 + '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'
 o00OO00OoO = iiI111I1iIiI ( IiI11i1I11111 )
 Ii1i = re . compile ( '<div class="thumb-inside"><script>.+?<img src="(.+?)".+?<a href="(.+?)" title=".+?">(.+?)</a></p>.+?uration">(.+?)</span>.+?Porn quality:(.+?)</span>' , re . DOTALL ) . findall ( o00OO00OoO )
 for I1II1I11I1I , Ii1II1I11i1 , ooo , oOoooooOoO , iIIi1 in Ii1i :
  ooOOoooooo ( ooo + ' - Porn Quality : ' + iIIi1 + ' - ' + oOoooooOoO , 'http://www.xvideos.com' + Ii1II1I11i1 , 10108 , I1II1I11I1I , I1II1I11I1I , iIIi1 + ' - ' + oOoooooOoO )
 ooo0o0 = re . compile ( '<li><a href="([^"]*)" class="no-page">Next</a></li></ul></div>' ) . findall ( o00OO00OoO )
 for Ii1II1I11i1 in ooo0o0 :
  ii1iI1iI1 ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + Ii1II1I11i1 , 10105 , ooOooo000oOO + 'Next.png' , '' , '' )
  if 34 - 34: oOo0O0Ooo * OOooOOo * OoOo00o + Ii1I
def II1iO00Oo ( url ) :
 o00OO00OoO = iiI111I1iIiI ( url )
 Ii1i = re . compile ( 'flv_url=(.+?)\;' ) . findall ( o00OO00OoO )
 for url in Ii1i :
  iiiO0ooO0O0Ooo0o = ( url ) . replace ( '%3A' , ':' ) . replace ( '%2F' , '/' ) . replace ( '%3F' , '?' ) . replace ( '%3D' , '=' ) . replace ( '%26' , '&' ) . replace ( '&amp' , '' )
  IIi11IIiIi1i ( iiiO0ooO0O0Ooo0o )
  if 20 - 20: ooOoO0O00 . Ii1I . IIIi % ooOoO0O00
def IIi11IIiIi1i ( url ) :
 I1i = xbmc . Player ( I1iii ( ) )
 import urlresolver
 try : I1i . play ( url )
 except : pass
 if 29 - 29: IIiIiII11i - o0o00Oo0O % O0OoO
 if 40 - 40: I11i + iI1iI1I1i1I
def OoO000Oo0oO ( ) :
 o00OO00OoO = iiI111I1iIiI ( i1111 ( 'aHR0cDovL3d3dy5nb2Zpc2hpbmcuY28udWsvQW5nbGluZy1UaW1lcy9TZWN0aW9uL1ZpZGVvcy8=' ) )
 Ii1i = re . compile ( 'class="item.+?"><a href="(.+?)">(.+?)</a></li>' ) . findall ( o00OO00OoO )
 for Ii1II1I11i1 , ooo in Ii1i :
  II1Ii1iI1i1 ( '[COLORgreen]' + ooo + '[/COLOR]' , ( 'http://www.gofishing.co.uk' + Ii1II1I11i1 ) . replace ( 'http://www.gofishing.co.ukhttp://www.gofishing.co.uk' , 'http://www.gofishing.co.uk' ) , 8091 , ooOooo000oOO + 'gofish.png' )
def iiiIiiiI1 ( url ) :
 o00OO00OoO = ii1II ( url )
 Ii1i = re . compile ( '<h2><a id=.+?href="([^"]*)">(.+?)</a></h2>' , re . DOTALL ) . findall ( o00OO00OoO )
 I1 = re . compile ( '<h3><a href="([^"]*)" id=.+?>(.+?)</a> </h3>.+?<img src="([^"]*)"' , re . DOTALL ) . findall ( o00OO00OoO )
 next = re . compile ( 'href="([^"]*)">next</a>&gt;</li>' , re . DOTALL ) . findall ( o00OO00OoO )
 for url , ooo in Ii1i :
  oOO0oo ( '[COLORgreen]' + ooo + '[/COLOR]' , 'http://www.gofishing.co.uk/' + url , 8092 , ooOooo000oOO + 'gofish.png' )
 for url , ooo , I1II1I11I1I in I1 :
  oOO0oo ( '[COLORgreen]' + ooo + '[/COLOR]' , 'http://www.gofishing.co.uk/' + url , 8092 , 'http://www.gofishing.co.uk/' + I1II1I11I1I )
 for url in next :
  II1Ii1iI1i1 ( '[COLORgreen]NEXT[/COLOR]' , url . replace ( ' ' , '+' ) , 8091 , ooOooo000oOO + 'Next.png' )
def I1IIIIIi1IIiI ( url ) :
 o00OO00OoO = ii1II ( url )
 Ii1i = re . compile ( 'src="https://www.youtube.com/embed/(.+?)"' ) . findall ( o00OO00OoO )
 for url in Ii1i :
  yt . PlayVideo ( url )
  if 26 - 26: I11i % IIIii1II1II + IIIii1II1II % iI1iI1I1i1I * Ii / o0oOO0O00o0O
  if 64 - 64: OoOo00o % OOooOOo / IIiIiII11i % O0OoO - o0oOO0O00o0O
  if 2 - 2: IIIi - Ii1I + I11i * oO0o / o0oOO0O00o0O
iIIiI11iI1Ii1 = '{PQ},' ; o00oo = '{SC},' ; O0oO0oo0O = '{XG},' ; oooOOO0ooOoOOO = '{JP},' ; o0IiIiI111IIII1 = '{HW},' ; OOOoOooO000oO = '{RT},'
def o0OOOOOo00 ( ) :
 Oo0oO0ooo = xbmcgui . DialogProgress ( )
 oo0oOO = ( i1111 ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 IIiI1i1i = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 IiII111i1i11 = IIiI1i1i . lower ( )
 Ii1II1I11i1 = ( i1111 ( 'aHR0cDovL2RsNC5tb3ZpZWZhcnNpLmNvbS9maWxtLzIwMTUtNy8=' ) )
 ooo0O0o00O = ( i1111 ( 'aHR0cDovL2RsLmF2YWRsLmNvbS9OZXcvTW92aWUv' ) )
 IiIi1I1 = ( i1111 ( 'aHR0cDovLzIxNy4yMTkuMTQzLjEwOC8xMzI3Lw==' ) )
 if 41 - 41: oO0o . IIIi * OooO0OoOOOO * IIIi
 ooOO = ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvbW92L2FsbC5waHA=' ) )
 O0oOoOoOoo0OoO0 = ( i1111 ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 I1iiI1iiI1i1 = ( i1111 ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL3NlYXJjaC8/cT0=' ) ) + IIiI1i1i
 OOOO00OOO00 = ( i1111 ( 'aHR0cDovL3JlZGVtcHRpb25idWlsZC4xNm1iLmNvbS9SZWRlbXB0aW9uL21vdmllcy9hbGxtb3ZpZS5waHA=' ) )
 ii1OO0 = ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9UaGVfUmVhcGVyL2FsbG1vdmllcy5waHA=' ) )
 OoOoO00OOoOOOo0 = ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC9tb3ZmdWxsLnBocA==' ) )
 oOoO00O = ( i1111 ( 'aHR0cDovLzUuMTM1LjIwNy45Ni9TY3JhcGVzL1NILnBocA==' ) )
 if 31 - 31: O0OoO . OOooOOo % OOooOOo % I1ii11iIi11i % oOo0O0Ooo * o0oOO0O00o0O
 Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Checking Sources" , '' , 'Please Wait' )
 o00OO00OoO = O000OO0 ( Ii1II1I11i1 )
 Oo0oO0ooo . update ( 0 , "" , "Checking Source 1/9 Links" )
 if 22 - 22: iI1iI1I1i1I % OooO0OoOOOO . OOooOOo / O0OoO + IIIii1II1II
 Oo0oO0ooo . update ( 14 , "" , "Checking Source 2/9 Links" )
 O0Oo000ooO00 = O000OO0 ( IiIi1I1 )
 Oo0oO0ooo . update ( 28 , "" , "Checking Source 3/9 Links" )
 if 85 - 85: oOo0O0Ooo - O0OoO % I1ii11iIi11i % IIiIiII11i - ii % OooO0OoOOOO
 Oo0oO0ooo . update ( 40 , "" , "Checking Source 4/9 Links" )
 iI111Iii1ii = O000OO0 ( ooOO )
 Oo0oO0ooo . update ( 52 , "" , "Checking Source 5/9 Links" )
 Ii1I11i1I1 = O000OO0 ( I1iiI1iiI1i1 )
 Oo0oO0ooo . update ( 64 , "" , "Checking Source 6/9 Links" )
 ooo0OO0OOooO0 = O000OO0 ( OOOO00OOO00 )
 Oo0oO0ooo . update ( 76 , "" , "Checking Source 7/9 Links" )
 O00O00 = O000OO0 ( ii1OO0 )
 Oo0oO0ooo . update ( 88 , "" , "Checking Source 8/9 Links" )
 oOooO0OoO = O000OO0 ( OoOoO00OOoOOOo0 )
 Oo0oO0ooo . update ( 100 , "" , "Checking Source 9/9 Links" )
 o0oOOOOoo0 = O000OO0 ( oOoO00O )
 if 80 - 80: Ii % Ii1I
 if 54 - 54: I11i + iI1iI1I1i1I - iI11I1II1I1I % O0OoO % OooO0OoOOOO
 if o00OO00OoO != 'Failed' :
  Ii1i = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( o00OO00OoO )
  for II1iiI1 , ooo in Ii1i :
   if IIiI1i1i . lower in ooo . lower ( ) :
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    oOO0oo ( ( '[COLORgreen]' + ooo + '- source 1[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( Ii1II1I11i1 + II1iiI1 ) , 222 , '' )
    Oo0oO0ooo . update ( 0 , "" , "Getting Source 1 Links" )
    if 4 - 4: I1ii11iIi11i - oO0o - Ii * IIIi / Ii11Ii1I - IIIii1II1II
    if 45 - 45: I11i % I1ii11iIi11i * ooOoO0O00 - o0o00Oo0O
    if 82 - 82: IIiIiII11i / o0oOO0O00o0O
    if 96 - 96: I1ii11iIi11i / OoOo00o . IIiIiII11i . I1ii11iIi11i
    if 91 - 91: IIiIiII11i . IIIii1II1II + I11i
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 9 , "" , "Getting Source 2 Links" )
 if O0Oo000ooO00 != 'Failed' :
  II1Ii = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( O0Oo000ooO00 )
  for II1iiI1 , ooo in II1Ii :
   if IIiI1i1i . lower in ooo . lower ( ) :
    II1Ii1iI1i1 ( ( '[COLORgreen]' + ooo + '- source 3[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( IiIi1I1 + II1iiI1 ) , 1006 , '' )
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 18 , "" , "Getting Source 3 Links" )
    if 8 - 8: IIIii1II1II * I1ii11iIi11i / o0oOO0O00o0O - oO0o - ii
    if 100 - 100: OoOo00o . iI11I1II1I1I . iI11I1II1I1I
    if 55 - 55: OoOo00o
    if 37 - 37: OooO0OoOOOO / Ii / I1ii11iIi11i
    if 97 - 97: IIIi . iI1iI1I1i1I / oOo0O0Ooo
    if 83 - 83: iI1iI1I1i1I - Ii1I * OoOo00o
    if 90 - 90: I1ii11iIi11i * oOo0O0Ooo
 if iI111Iii1ii != 'Failed' :
  OO0OooOo = [ ]
  ii111iI1i1 = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( iI111Iii1ii )
  for Ii1II1I11i1 , iI1IOooOoOo , iiIII1i , OOOooO0OO0o , ooo in ii111iI1i1 :
   if IIiI1i1i . lower in ooo . lower ( ) :
    if ooo in OO0OooOo :
     pass
    else :
     II1I ( ( '[COLORgreen]' + ooo + '- source Scooby[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( 'Ganool' , '' ) . replace ( 'ShAaNiG' , '' ) . replace ( 'YIFY' , '' ) . replace ( '[[ Max-Movie.In ]]' , '' ) . replace ( '.mkv' , '' ) . replace ( '.mp4' , '' ) . replace ( '.' , ' ' ) , Ii1II1I11i1 , 1016 , iI1IOooOoOo , OOOooO0OO0o , iiIII1i )
     OO0OooOo . append ( ooo )
     Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     Oo0oO0ooo . update ( 36 , "" , "Getting Scooby Links" )
     iiO0o0oOOOoOo ( 'tvshows' , 'Media Info 3' )
 if Ii1I11i1I1 != 'Failed' :
  OO000 = re . compile ( 'href="(.+?)".+?src="(.+?)" alt="Image of (.+?)"' , re . DOTALL ) . findall ( Ii1I11i1I1 )
  for Ii1II1I11i1 , I1II1I11I1I , ooo in OO000 :
   if IIiI1i1i . lower in ooo . lower ( ) :
    II1Ii1iI1i1 ( ( '[COLORgreen]' + ooo + '- source Snag[/COLOR]' ) . replace ( '&#x27;' , '' ) , 'http://www.snagfilms.com' + Ii1II1I11i1 , 7067 , I1II1I11I1I )
    Oo0oO0ooo . update ( 45 , "" , "Getting Snag Links" )
    if 31 - 31: oO0o * o0o00Oo0O / iI1iI1I1i1I . ii * iI1iI1I1i1I . Ii1I
    iiO0o0oOOOoOo ( 'tvshows' , 'Media Info 3' )
 if ooo0OO0OOooO0 != 'Failed' :
  III1II111II11 = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( ooo0OO0OOooO0 )
  for Ii1II1I11i1 , iI1IOooOoOo , iiIII1i , OOOooO0OO0o , ooo in III1II111II11 :
   if IIiI1i1i . lower in ooo . lower ( ) :
    ooOOoooooo ( ( '[COLORgreen]' + ooo + '- source Redemption[/COLOR]' ) , Ii1II1I11i1 , 222 , iI1IOooOoOo , OOOooO0OO0o , iiIII1i )
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 53 , "" , "Getting Redemption Links" )
    if 72 - 72: ooOoO0O00 % O0OoO % OooO0OoOOOO % OoOo00o - OoOo00o
    iiO0o0oOOOoOo ( 'tvshows' , 'Media Info 3' )
 if O00O00 != 'Failed' :
  OOoo0O0OOOo0 = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( O00O00 )
  for Ii1II1I11i1 , iI1IOooOoOo , iiIII1i , OOOooO0OO0o , ooo in OOoo0O0OOOo0 :
   if IIiI1i1i . lower in ooo . lower ( ) :
    ooOOoooooo ( ( '[COLORgreen]' + ooo + '- source Reaper[/COLOR]' ) , Ii1II1I11i1 , 222 , iI1IOooOoOo , OOOooO0OO0o , iiIII1i )
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 61 , "" , "Getting Reaper Links" )
    if 25 - 25: iI11I1II1I1I % IIiIiII11i / iI1iI1I1i1I / Ii1I
    iiO0o0oOOOoOo ( 'tvshows' , 'Media Info 3' )
 if oOooO0OoO != 'Failed' :
  iI1iIIIIIiIi1 = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( oOooO0OoO )
  for Ii1II1I11i1 , iI1IOooOoOo , iiIII1i , OOOooO0OO0o , ooo in iI1iIIIIIiIi1 :
   if IIiI1i1i . lower in ooo . lower ( ) :
    ooOOoooooo ( ( '[COLORgreen]' + ooo + '- source Herovision[/COLOR]' ) , Ii1II1I11i1 , 222 , iI1IOooOoOo , OOOooO0OO0o , iiIII1i )
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 70 , "" , "Getting Herovision Links" )
    if 19 - 19: OOooOOo . I11i . ii
    iiO0o0oOOOoOo ( 'tvshows' , 'Media Info 3' )
    if 13 - 13: IIIii1II1II . I1ii11iIi11i / IIiIiII11i
 if o0oOOOOoo0 != 'Failed' :
  iiI1iIII1ii = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( o0oOOOOoo0 )
  for Ii1II1I11i1 , iI1IOooOoOo , ooo in iiI1iIII1ii :
   if IIiI1i1i . lower in ooo . lower ( ) :
    II1Ii1iI1i1 ( ( '[COLORgreen]' + ooo + '- source Silent Hunter[/COLOR]' ) , Ii1II1I11i1 , 222 , iI1IOooOoOo )
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 78 , "" , "Getting Silent Hunter Links" )
    if 5 - 5: IIIi % ii . OOooOOo
    iiO0o0oOOOoOo ( 'tvshows' , 'Media Info 3' )
 III1Ii1i1I1 = [ '480p' , '720p' , '1080p' , 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' , '720paction' , '720padventure' , '720panimation' , '720pcomedy' , '720pcrime' , '720pdocumentary' , '720pdrama' , '720pfamily' , '720pfantasy' , '720phorror' , '720pmystery' , '720promance' , '720psci-Fi' , '720psport' , '720pthriller' , '720pwestern' , '1080paction' , '1080padventure' , '1080panimation' , '1080pcomedy' , '1080pcrime' , '1080pdocumentary' , '1080pdrama' , '1080pfamily' , '1080pfantasy' , '1080phorror' , '1080pmystery' , '1080promance' , '1080psci-Fi' , '1080psport' , '1080pthriller' , '1080pwestern' , 'films' ]
 if 67 - 67: Ii1I + Ii11Ii1I
 for I111Ii in III1Ii1i1I1 :
  II11 = IIIII + I111Ii + ooOoOoo0O
  o0O00OooooO = O000OO0 ( II11 )
  if o0O00OooooO != 'Failed' :
   oO00OoO0oo = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( o0O00OooooO )
   for Ii1II1I11i1 , iI1IOooOoOo , iiIII1i , OOOooO0OO0o , ooo in oO00OoO0oo :
    if IIiI1i1i . lower in ooo . lower ( ) :
     ooOOoooooo ( '[COLORgreen]' + ooo + ' - Source Pandoras[/COLOR]' , Ii1II1I11i1 , 222 , iI1IOooOoOo , OOOooO0OO0o , iiIII1i )
     Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     Oo0oO0ooo . update ( 89 , "" , "Getting Pandoras Links" )
     if 52 - 52: OooO0OoOOOO % O0OoO
     iiO0o0oOOOoOo ( 'tvshows' , 'Media Info 3' )
     if 25 - 25: iI1iI1I1i1I / iI1iI1I1i1I % ii - Ii1I * OoOo00o
 III1Ii1i1I1 = [ '0-9/' , 'A/' , 'B/' , 'C/' , 'D/' , 'E/' , 'F/' , 'G/' , 'H/' , 'I/' , 'J/' , 'K/' , 'L/' , 'M/' , 'N/' , 'O/' , 'P/' , 'R/' , 'S/' , 'T/' , 'U/' , 'V/' , 'W/' , 'X/' , 'Y/' , 'Z/' ]
 if 23 - 23: Ii
 if 100 - 100: OoOo00o + o0o00Oo0O . oOo0O0Ooo + ooOoO0O00 - OOooOOo + I11i
 for I111Ii in III1Ii1i1I1 :
  II11 = oo0oOO + I111Ii
  ooOOo = O000OO0 ( II11 )
  if iI111Iii1ii != 'Failed' :
   i1iii1IiiiI1i1 = re . compile ( '<li><a href="(.+?)"> (.+?)</a></li>' ) . findall ( ooOOo )
   for II1iiI1 , ooo in i1iii1IiiiI1i1 :
    if IIiI1i1i . lower in ooo . lower ( ) :
     oOO0oo ( ( '[COLORgreen]' + ooo + 'source 5[/COLOR]' ) . replace ( 'Ganool' , '' ) . replace ( 'ShAaNiG' , '' ) . replace ( 'YIFY' , '' ) . replace ( '[[ Max-Movie.In ]]' , '' ) . replace ( '.mkv' , '' ) . replace ( '.mp4' , '' ) . replace ( '.' , ' ' ) , ( oo0oOO + I111Ii + II1iiI1 ) , 222 , '' )
     Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     Oo0oO0ooo . update ( 100 , "" , "Getting Source 5 Links" )
     if 37 - 37: I1ii11iIi11i - ooOoO0O00 - OooO0OoOOOO + iI1iI1I1i1I . iI11I1II1I1I
     iiO0o0oOOOoOo ( 'tvshows' , 'Media Info 3' )
     if 59 - 59: ii - IIIi % I11i . iI1iI1I1i1I + ooOoO0O00 * iI1iI1I1i1I
     if 5 - 5: IIiIiII11i - OooO0OoOOOO
def O0O00oO0OoO0o ( ) :
 if 5 - 5: IIIii1II1II % I1ii11iIi11i % OooO0OoOOOO % O0OoO
 IIiI1i1i = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 IiII111i1i11 = IIiI1i1i . lower ( )
 if 17 - 17: Ii11Ii1I + IIiIiII11i + ii / IIIii1II1II / OooO0OoOOOO
 Ii1II1I11i1 = ( i1111 ( 'aHR0cDovL2RsLmZhcnNpbW92aWUubmV0L1NlcmlhbC8=' ) )
 if 80 - 80: I11i % ooOoO0O00 / iI1iI1I1i1I
 IiIi1I1 = ( i1111 ( 'aHR0cDovL3R2LmRsLXBhcnMuaW4v' ) )
 ooi1i1Ii1IiIII = ( i1111 ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9BbWVyaWNhbiUyMFNlcmlhbC8=' ) )
 ooOO = ( i1111 ( 'aHR0cDovL2RpemlsYWIuY29tL2Fyc2l2P2xpbWl0PSZ0dXI9Jm9yZGVyYnk9JnVsa2U9Jm9yZGVyPSZ5aWw9JmRpemlfYWRpPQ==' ) ) + ( IiII111i1i11 ) . replace ( ' ' , '+' )
 O0oOoOoOoo0OoO0 = ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvc2hvd3MvdHZhbGwucGhw' ) )
 I1iiI1iiI1i1 = ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9UaGVfUmVhcGVyL2FsbHR2LnBocA==' ) )
 OOOO00OOO00 = ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC90dmZ1bGwucGhw' ) )
 if 9 - 9: iI1iI1I1i1I - OoOo00o + o0o00Oo0O / o0oOO0O00o0O % ooOoO0O00
 Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Checking Sources" , '' , 'Please Wait' )
 if 97 - 97: I11i * O0OoO
 Oo0oO0ooo . update ( 0 , "" , "Checking Source 1/9 Links" )
 o00OO00OoO = O000OO0 ( Ii1II1I11i1 )
 Oo0oO0ooo . update ( 14 , "" , "Checking Source 2/9 Links" )
 if 78 - 78: iI1iI1I1i1I . IIIii1II1II + OoOo00o * o0oOO0O00o0O - ooOoO0O00
 Oo0oO0ooo . update ( 28 , "" , "Checking Source 3/9 Links" )
 O0Oo000ooO00 = O000OO0 ( IiIi1I1 )
 Oo0oO0ooo . update ( 40 , "" , "Checking Source 4/9 Links" )
 oO0 = O000OO0 ( ooi1i1Ii1IiIII )
 Oo0oO0ooo . update ( 52 , "" , "Checking Source 5/9 Links" )
 iI111Iii1ii = cloudflare . source ( ooOO )
 Oo0oO0ooo . update ( 64 , "" , "Checking Source 6/9 Links" )
 ooOOo = O000OO0 ( O0oOoOoOoo0OoO0 )
 Oo0oO0ooo . update ( 76 , "" , "Checking Source 7/9 Links" )
 Ii1I11i1I1 = O000OO0 ( I1iiI1iiI1i1 )
 Oo0oO0ooo . update ( 88 , "" , "Checking Source 8/9 Links" )
 ooo0OO0OOooO0 = O000OO0 ( OOOO00OOO00 )
 Oo0oO0ooo . update ( 100 , "" , "Checking Source 9/9 Links" )
 if 27 - 27: Ii11Ii1I % ooOoO0O00 . I1ii11iIi11i % IIIi
 if ooo0OO0OOooO0 != 'Failed' :
  III1II111II11 = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( ooo0OO0OOooO0 )
  for Ii1II1I11i1 , iI1IOooOoOo , iiIII1i , OOOooO0OO0o , ooo in III1II111II11 :
   if IiII111i1i11 in ooo . lower ( ) :
    II1I ( ( '[COLORgreen]' + ooo + '- source HeroVision[/COLOR]' ) , Ii1II1I11i1 , 1016 , iI1IOooOoOo , OOOooO0OO0o , iiIII1i )
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 10 , "" , "Getting Herovision Links" )
    if 10 - 10: OooO0OoOOOO / ii
    iiO0o0oOOOoOo ( 'tvshows' , 'Media Info 3' )
    if 50 - 50: Ii - ii . OoOo00o + o0o00Oo0O . ooOoO0O00
 if Ii1I11i1I1 != 'Failed' :
  OO000 = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( Ii1I11i1I1 )
  for Ii1II1I11i1 , iI1IOooOoOo , iiIII1i , OOOooO0OO0o , ooo in OO000 :
   if IiII111i1i11 in ooo . lower ( ) :
    II1I ( ( '[COLORgreen]' + ooo + '- source Reaper[/COLOR]' ) , Ii1II1I11i1 , 1016 , iI1IOooOoOo , OOOooO0OO0o , iiIII1i )
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 20 , "" , "Getting Reaper Links" )
    if 91 - 91: I11i . o0oOO0O00o0O % I1ii11iIi11i - o0oOO0O00o0O . OoOo00o % Ii
    iiO0o0oOOOoOo ( 'tvshows' , 'Media Info 3' )
    if 25 - 25: iI11I1II1I1I
    if 63 - 63: O0OoO
    if 96 - 96: iI1iI1I1i1I
    if 34 - 34: OOooOOo / oO0o - oOo0O0Ooo . o0o00Oo0O . IIIii1II1II
    if 63 - 63: o0oOO0O00o0O
    if 11 - 11: o0oOO0O00o0O - iI11I1II1I1I
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 30 , "" , "Getting CoolSeries Links" )
    if 92 - 92: oO0o
    iiO0o0oOOOoOo ( 'tvshows' , 'Media Info 3' )
 if o00OO00OoO != 'Failed' :
  Ii1i = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( o00OO00OoO )
  for ooo in Ii1i :
   if IiII111i1i11 in ooo . lower ( ) :
    II1Ii1iI1i1 ( '[COLORgreen]' + ( ooo ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) + ' source 1 [/COLOR]' , ( Ii1II1I11i1 + ooo ) . replace ( ' ' , '%20' ) , 1006 , '' )
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 40 , "" , "Getting Source 1 Links" )
    if 15 - 15: OooO0OoOOOO / OooO0OoOOOO + iI11I1II1I1I % ii
    iiO0o0oOOOoOo ( 'tvshows' , 'Media Info 3' )
    if 12 - 12: O0OoO
    if 36 - 36: IIIi . OooO0OoOOOO * ii - I11i
    if 60 - 60: IIIii1II1II . o0oOO0O00o0O / iI11I1II1I1I + IIIii1II1II * IIIi
    if 82 - 82: Ii . iI11I1II1I1I * oOo0O0Ooo - iI1iI1I1i1I + Ii11Ii1I
    if 48 - 48: Ii1I
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 50 , "" , "Getting Source 2 Links" )
    if 96 - 96: O0OoO . ii
    iiO0o0oOOOoOo ( 'tvshows' , 'Media Info 3' )
 if O0Oo000ooO00 != 'Failed' :
  II1Ii = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( O0Oo000ooO00 )
  for ooo in II1Ii :
   if IiII111i1i11 in ooo . lower ( ) :
    II1Ii1iI1i1 ( ( ooo + ' source 3' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( IiIi1I1 + ooo ) . replace ( ' ' , '%20' ) , 1006 , '' )
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 60 , "" , "Getting Source 3 Links" )
    if 39 - 39: IIIii1II1II + oO0o
    iiO0o0oOOOoOo ( 'tvshows' , 'Media Info 3' )
 if oO0 != 'Failed' :
  oOoOOOO0OOO = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( oO0 )
  for ooo in oOoOOOO0OOO :
   if IiII111i1i11 in ooo . lower ( ) :
    II1Ii1iI1i1 ( ( ooo + ' source 4' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( ooi1i1Ii1IiIII + ooo ) . replace ( ' ' , '%20' ) , 1006 , '' )
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 70 , "" , "Getting Source 4 Links" )
    if 58 - 58: iI1iI1I1i1I % Ii / Ii * O0OoO - IIIi
    iiO0o0oOOOoOo ( 'tvshows' , 'Media Info 3' )
 if iI111Iii1ii != 'Failed' :
  ii111iI1i1 = re . compile ( '<a href="(.+?)" class="film-image">\n<img src="(.+?)" alt=""/>\n</a>\n<div class="tss-detail">\n<a class="title" style="" href=".+?">\n<span class="position">.+?</span>\n(.+?)</a>' ) . findall ( iI111Iii1ii )
  for Ii1II1I11i1 , I1II1I11I1I , ooo in ii111iI1i1 :
   if IiII111i1i11 in ooo . lower ( ) :
    II1Ii1iI1i1 ( '[COLORgreen]' + ooo + ' - Source - Dizi[/COLOR]' , Ii1II1I11i1 , 8062 , I1II1I11I1I )
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 80 , "" , "Getting Dizi Links" )
    if 6 - 6: OooO0OoOOOO * IIiIiII11i % iI11I1II1I1I
    iiO0o0oOOOoOo ( 'tvshows' , 'Media Info 3' )
 if ooOOo != 'Failed' :
  i1iii1IiiiI1i1 = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( ooOOo )
  for Ii1II1I11i1 , iI1IOooOoOo , iiIII1i , OOOooO0OO0o , ooo in i1iii1IiiiI1i1 :
   if IiII111i1i11 in ooo . lower ( ) :
    II1I ( ( '[COLORgreen]' + ooo + '- Source Scooby[/COLOR]' ) , Ii1II1I11i1 , 1016 , iI1IOooOoOo , OOOooO0OO0o , iiIII1i )
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 90 , "" , "Getting Scooby Links" )
    if 86 - 86: ooOoO0O00 * o0o00Oo0O % O0OoO . I1ii11iIi11i % O0OoO . I1ii11iIi11i
    iiO0o0oOOOoOo ( 'tvshows' , 'Media Info 3' )
    if 71 - 71: o0oOO0O00o0O . Ii * o0o00Oo0O + o0o00Oo0O
 Oo0 = [ 'a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' , 'p' , 'q' , 'r' , 's' , 't' , 'u' , 'v' , 'w' , 'x' , 'y' , 'z' ]
 if 75 - 75: oO0o / Ii11Ii1I + IIiIiII11i % OooO0OoOOOO . Ii
 for I111Ii in Oo0 :
  II11 = IIIII + I111Ii + ooOoOoo0O
  oOooO0OoO = iiI111I1iIiI ( II11 )
  if oOooO0OoO != 'Failed' :
   iI1iIIIIIiIi1 = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( oOooO0OoO )
   for ooo , iiIII1i , Ii1II1I11i1 , I1II1I11I1I , III1I1Iii1iiI , IIi11II1II111 in iI1iIIIIIiIi1 :
    if IiII111i1i11 in ooo . lower ( ) :
     II1I ( '[COLORgreen]' + ooo + ' - Source Pandoras[/COLOR]' , Ii1II1I11i1 , IIi11II1II111 , I1II1I11I1I , III1I1Iii1iiI , iiIII1i )
     Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     Oo0oO0ooo . update ( 100 , "" , "Getting Pandoras Links" )
     if 76 - 76: o0oOO0O00o0O . OooO0OoOOOO % o0oOO0O00o0O - IIIi
     iiO0o0oOOOoOo ( 'tvshows' , 'Media Info 3' )
     if 51 - 51: ii + I11i * iI11I1II1I1I * OoOo00o / ooOoO0O00
     if 19 - 19: o0oOO0O00o0O - OOooOOo % OoOo00o / ii % o0oOO0O00o0O
 xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
def ooOoOoO0 ( ) :
 if 31 - 31: Ii - O0OoO / Ii1I - Ii11Ii1I
 IIiI1i1i = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 IiII111i1i11 = IIiI1i1i . lower ( )
 Ii1II1I11i1 = ( i1111 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz' ) )
 o00OO00OoO = iiI111I1iIiI ( Ii1II1I11i1 )
 Ii1i = re . compile ( '"id":".+?","name":"(.+?)","img":"(.+?)","stream_url3":".+?","cat_id":"(.+?)","stream_url2":".+?","stream_url":".+?"}' , re . DOTALL ) . findall ( o00OO00OoO )
 for ooo , I1II1I11I1I , iiIiIi1111iI1 in Ii1i :
  III = i1111 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv' ) + ( I1II1I11I1I ) . replace ( '\\' , '' )
  if IIiI1i1i in ooo . lower ( ) :
   II1Ii1iI1i1 ( ooo , '' , 7022 , III )
   if 59 - 59: ii / OooO0OoOOOO + iI1iI1I1i1I . o0oOO0O00o0O * Ii11Ii1I - ii
 xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
OO0O0OO0O0 = '{ZH},' ; oOoo = '{IX},' ; oo0O00ooo0o = '{LM},'
if 29 - 29: ii . IIiIiII11i % OOooOOo
def IiiIi1I11 ( url ) :
 i1I1Ii11II1i = cloudflare . source ( url )
 Ii1i = re . compile ( '<a class="season" href="(.+?)">\n(.+?)\n</a>\n</span>\n<span>\n<a class="episode" href=".+?">\n(.+?)\n</a>\n</span>\n<span>\n<a class="episode-name" href=".+?">\n(.+?)</a>' ) . findall ( i1I1Ii11II1i )
 for url , oOOoOOO0oo0 , o0O00oOOoo , ooo in Ii1i :
  II1Ii1iI1i1 ( ( oOOoOOO0oo0 ) . replace ( 'Sezon' , ' Season ' ) + ( o0O00oOOoo ) . replace ( 'Bölüm' , ' Episode ' ) + ooo , url , 8063 , '' )
  if 83 - 83: OooO0OoOOOO
  if 30 - 30: I1ii11iIi11i
  if 8 - 8: o0o00Oo0O + OoOo00o + IIIi
  if 47 - 47: iI1iI1I1i1I
def Oooo0O0Oooo ( url ) :
 i1I1Ii11II1i = cloudflare . source ( url )
 Ii1i = re . compile ( 'file: "(.+?)",.+?label: "(.+?)",' , re . DOTALL ) . findall ( i1I1Ii11II1i )
 for url , ooo in Ii1i :
  oOO0oo ( ooo , url , 222 , '' )
  if 47 - 47: Ii / I1ii11iIi11i - I1ii11iIi11i * oO0o
  if 48 - 48: OooO0OoOOOO
  if 96 - 96: OoOo00o / o0o00Oo0O . IIiIiII11i + OooO0OoOOOO % I11i
  if 67 - 67: o0o00Oo0O % IIIi
def IIII1I ( ) :
 if 70 - 70: Ii11Ii1I . o0o00Oo0O - IIIii1II1II
 i1I1Ii11II1i = cloudflare . source ( i1111 ( 'aHR0cDovL2RpemlsYWIuY29t' ) )
 Ii1i = re . compile ( '<li id=".+?">.+?<a href="(.+?)">.+?<img width="40" height="40" src="(.+?)" alt=""/>.+?<span class="title">\n(.+?)</span>.+?<span class="alt-title">\n(.+?)</span>.+?</a>.+?</li>' , re . DOTALL ) . findall ( i1I1Ii11II1i )
 for Ii1II1I11i1 , I1II1I11I1I , ooo , o0O00oOOoo in Ii1i :
  II1Ii1iI1i1 ( ooo + '  -  ' + ( o0O00oOOoo ) . replace ( 'sezon' , 'Season' ) . replace ( 'bölüm' , 'Episode' ) , Ii1II1I11i1 , 8063 , I1II1I11I1I )
  if 62 - 62: IIIi * iI1iI1I1i1I
def oOo ( ) :
 OO0O00oOo = ii1II ( i1111 ( 'aHR0cDovL3d3dy50dmd1aWRlLmNvLnVrLw==' ) )
 Ii1i = re . compile ( '<a href="(.+?)"  qt-title=".+?" qt-text=".+?<br> .+?" title="(.+?)".+?class=".+? src="(.+?)" alt=".+?" /></a>' , re . DOTALL ) . findall ( OO0O00oOo )
 for Ii1II1I11i1 , ooo , I1II1I11I1I in Ii1i :
  oOO0oo ( '[COLORgreen]' + ooo + '[/COLOR]' , Ii1II1I11i1 , 8002 , I1II1I11I1I )
def oOOoO0oO0oo0O ( url ) :
 OO0O00oOo = ii1II ( url )
 Ii1i = re . compile ( '<table border="0".+?url((.+?));background-repeat: no-repeat;">.+?<tr>.+?<span class="season">(.+?)</span><br>.+?<a href="(.+?)"+?>(.+?)</span><br>.+?<span class="programmetext">(.+?)</span></a><br>' , re . DOTALL ) . findall ( OO0O00oOo )
 for I1II1I11I1I , time , url , ooo , i111i1i in Ii1i :
  II1I ( '%s %s' % ( '[COLORgreen]' + ooo + '[/COLOR]' , time ) , url , 1015 , I1II1I11I1I , i111i1i )
  if 55 - 55: I1ii11iIi11i
def IIi1i1I11IIII ( ) :
 if 55 - 55: iI11I1II1I1I % oO0o / Ii1I / I11i
 II1Ii1iI1i1 ( 'Coronation Street' , '' , 8001 , '' )
 II1Ii1iI1i1 ( 'Eastenders' , '' , 8002 , '' )
 II1Ii1iI1i1 ( 'Emmerdale' , '' , 8003 , '' )
 II1Ii1iI1i1 ( 'Hollyoaks' , '' , 8004 , '' )
 II1Ii1iI1i1 ( 'Im a Celebrity' , '' , 8005 , '' )
 if 39 - 39: oO0o % OoOo00o / OooO0OoOOOO * o0oOO0O00o0O * OoOo00o . OoOo00o
 if 42 - 42: IIIi % oO0o . Ii1I
 if 4 - 4: ooOoO0O00 + OOooOOo
 if 39 - 39: iI11I1II1I1I + O0OoO
def o00oOoo0o00 ( ) :
 o00OO00OoO = iiI111I1iIiI ( 'http://uksoapshare.blogspot.co.uk/' )
 Ii1i = re . compile ( '<a href="(.+?)".+?target=_blank>(.+?)</a>' ) . findall ( o00OO00OoO )
 for Ii1II1I11i1 , ooo in Ii1i :
  if 'Holly' in ooo :
   I1II1I11I1I = 'http://2.bp.blogspot.com/-9c7Sieh1RKs/UjD6TGAEEnI/AAAAAAAAAC8/84uwHfxcuYg/s1600/Hollyoaks.png'
   if 'huge' in Ii1II1I11i1 :
    oOO0oo ( ( ooo ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , Ii1II1I11i1 . replace ( '\\/' , '/' ) , 8006 , I1II1I11I1I )
   else :
    pass
    if 42 - 42: oO0o * Ii
 xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE_IGNORE_THE ) ;
 if 16 - 16: o0oOO0O00o0O % oOo0O0Ooo - O0OoO
def ooO00OoO0o0OO ( ) :
 o00OO00OoO = iiI111I1iIiI ( 'http://uksoapshare.blogspot.co.uk/' )
 Ii1i = re . compile ( '<a href="(.+?)".+?target=_blank>(.+?)</a>' ) . findall ( o00OO00OoO )
 for Ii1II1I11i1 , ooo in Ii1i :
  if 'East' in ooo :
   I1II1I11I1I = 'http://3.bp.blogspot.com/-KWHcNbNJU8Y/Vi1ousRl7fI/AAAAAAAAAT8/ksNE12LH0nE/s1600/eastenders.jpg'
   if 'huge' in Ii1II1I11i1 :
    oOO0oo ( ( ooo ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , Ii1II1I11i1 . replace ( '\\/' , '/' ) , 8006 , I1II1I11I1I )
   else :
    pass
    if 10 - 10: OoOo00o - o0oOO0O00o0O % IIiIiII11i - IIIi - ooOoO0O00
 xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 10 - 10: Ii1I - iI1iI1I1i1I . IIIi
def iiIIIi1iIi ( ) :
 o00OO00OoO = iiI111I1iIiI ( 'http://uksoapshare.blogspot.co.uk/' )
 Ii1i = re . compile ( '<a href="(.+?)".+?target=_blank>(.+?)</a>' ) . findall ( o00OO00OoO )
 for Ii1II1I11i1 , ooo in Ii1i :
  if 'Emmer' in ooo :
   I1II1I11I1I = 'http://2.bp.blogspot.com/-UfDcxisVV5c/UjH9vUicZ3I/AAAAAAAAADc/8Ozuiz1ojxw/s1600/Emmerdale.jpg'
   if 'huge' in Ii1II1I11i1 :
    oOO0oo ( ( ooo ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , Ii1II1I11i1 . replace ( '\\/' , '/' ) , 8006 , I1II1I11I1I )
   else :
    pass
    if 79 - 79: IIIii1II1II % IIIi / OoOo00o - iI11I1II1I1I - OOooOOo
 xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 60 - 60: IIiIiII11i
def oO0OOoo ( ) :
 o00OO00OoO = iiI111I1iIiI ( 'http://uksoapshare.blogspot.co.uk/' )
 Ii1i = re . compile ( '<a href="(.+?)".+?target=_blank>(.+?)</a>' ) . findall ( o00OO00OoO )
 for Ii1II1I11i1 , ooo in Ii1i :
  if 'Coro' in ooo :
   I1II1I11I1I = 'http://3.bp.blogspot.com/-hofvfBQVexs/UjErIfNdS4I/AAAAAAAAADQ/Q-vVGu3apYU/s1600/corrie.jpg'
   if 'huge' in Ii1II1I11i1 :
    oOO0oo ( ( ooo ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , Ii1II1I11i1 . replace ( '\\/' , '/' ) , 8006 , I1II1I11I1I )
   else :
    pass
    if 96 - 96: IIIii1II1II
 xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 38 - 38: o0oOO0O00o0O * ii
def iIi11III ( ) :
 o00OO00OoO = iiI111I1iIiI ( 'http://uksoapshare.blogspot.co.uk/' )
 Ii1i = re . compile ( '<a href="(.+?)" target="_blank">(.+?)</a>' ) . findall ( o00OO00OoO )
 for Ii1II1I11i1 , ooo in Ii1i :
  if 'Celeb' in ooo :
   I1II1I11I1I = 'http://3.bp.blogspot.com/-a_yDotWU_pY/VkotKWaG_gI/AAAAAAAAAUk/8Q5iNM6p37k/s1600/iacgoh.jpg'
   if 'huge' in Ii1II1I11i1 :
    oOO0oo ( ( ooo ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , Ii1II1I11i1 . replace ( '\\/' , '/' ) , 8006 , I1II1I11I1I )
   else :
    pass
    if 16 - 16: ii * Ii . ii - iI11I1II1I1I * ooOoO0O00
def i1iI1IIi1I ( name , url ) :
 oo00i1i11I1I1 = urlresolver . HostedMediaFile ( url ) . valid_url ( )
 if oo00i1i11I1I1 :
  OOOOOoooO = urlresolver . HostedMediaFile ( url ) . resolve ( )
 else :
  OO0O00oOo = open_url ( url )
  url = re . compile ( 'src="(.+?)"></iframe>' ) . findall ( OO0O00oOo ) [ 0 ]
  url = url . split ( '?autoplay' ) [ 0 ]
  OO0O00oOo = open_url ( url )
  oO0Oooo0OoO = re . compile ( 'mp4","url":"(.+?)"' ) . findall ( OO0O00oOo ) [ - 1 ]
  OOOOOoooO = oO0Oooo0OoO . replace ( '\\/' , '/' )
 OoOo0oO0o = xbmcgui . ListItem ( name , '' , '' )
 OoOo0oO0o . setPath ( OOOOOoooO )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , OoOo0oO0o )
 if 38 - 38: oOo0O0Ooo . oOo0O0Ooo . Ii11Ii1I + Ii1I * I1ii11iIi11i
 if 61 - 61: IIiIiII11i . OooO0OoOOOO - o0o00Oo0O * OooO0OoOOOO
def Iii1I ( ) :
 OO0O00oOo = iiI111I1iIiI ( i1111 ( 'aHR0cDovL3d3dy5kaXppYm94aGQuY29tLw==' ) )
 Ii1i = re . compile ( 'class="film menu-item menu-item-type-post_type menu-item-object-page menu-item-36980"><a href="(.+?)"><i class="fa fa-film"></i><span>(.+?)</span></a></li>' ) . findall ( OO0O00oOo )
 I1 = re . compile ( 'class="menu-item menu-item-type-post_type menu-item-object-page menu-item-52949"><a href="(.+?)"><i class="fa fa-"></i><span>(.+?)</span></a></li>' ) . findall ( OO0O00oOo )
 for Ii1II1I11i1 , ooo in Ii1i :
  II1Ii1iI1i1 ( ( '[COLORgreen]' + ooo + '[/COLOR]' ) . replace ( 'Diziler' , 'Series' ) , Ii1II1I11i1 , 7071 , ooOooo000oOO + 'popcorn.png' )
 for Ii1II1I11i1 , ooo in I1 :
  II1Ii1iI1i1 ( ( '[COLORgreen]' + ooo + '[/COLOR]' ) . replace ( 'Filmler' , 'Movies' ) , Ii1II1I11i1 , 7071 , ooOooo000oOO + 'popcorn.png' )
  if 100 - 100: ii . I1ii11iIi11i / Ii1I
def I11i1I11iIii ( ) :
 OO0O00oOo = iiI111I1iIiI ( i1111 ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL2NhdGVnb3JpZXMv' ) )
 Ii1i = re . compile ( '<a class="nav-item" href="(.+?)">(.+?)</a>' ) . findall ( OO0O00oOo )
 for Ii1II1I11i1 , ooo in Ii1i :
  if 'Movies' in ooo :
   II1Ii1iI1i1 ( '[COLORgreen]' + ooo + '[/COLOR]' , 'http://www.snagfilms.com' + ( Ii1II1I11i1 ) . replace ( 'http://www.snagfilms.com' , '' ) , 7061 , ooOooo000oOO + 'popcorn.png' )
def O0OOo ( url ) :
 OO0O00oOo = iiI111I1iIiI ( url )
 Ii1i = re . compile ( '<a class="object-link size-poster".+?href="(.+?)" data-type="category">.+?src="(.+?)" alt="Image of (.+?)" />' , re . DOTALL ) . findall ( OO0O00oOo )
 Ii1i = re . compile ( '<a class="object-link size-poster".+?href="(.+?)" data-type="category">.+?src="(.+?)" alt="Image of (.+?)" />' , re . DOTALL ) . findall ( OO0O00oOo )
 I1 = re . compile ( "<li class='current'>.+?</li><li ><a href='(.+?)'>.+?</a></li><li" , re . DOTALL ) . findall ( OO0O00oOo )
 for url , I1II1I11I1I , ooo in Ii1i :
  II1Ii1iI1i1 ( '[COLORgreen]' + ooo + '[/COLOR]' , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7067 , I1II1I11I1I )
 for url in I1 :
  II1Ii1iI1i1 ( '[COLORgreen]NEXT PAGE[/COLOR]' , ( url ) . replace ( '&#038;' , '&' ) , 7063 , ooOooo000oOO + 'Next.png' )
  if 62 - 62: OOooOOo % O0OoO * iI11I1II1I1I
  if 38 - 38: Ii . iI11I1II1I1I . IIIii1II1II / oO0o
def iI1111i1i1ii ( url ) :
 OO0O00oOo = iiI111I1iIiI ( i1111 ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL2NhdGVnb3JpZXMv' ) )
 Ii1i = re . compile ( '<a class="object-link size-poster".+?href="(.+?)" data-type="category">.+?src="(.+?)" alt="Image of (.+?)" />' , re . DOTALL ) . findall ( OO0O00oOo )
 for url , I1II1I11I1I , ooo in Ii1i :
  II1Ii1iI1i1 ( '[COLORgreen]' + ooo + '[/COLOR]' , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7062 , I1II1I11I1I )
  if 62 - 62: ii / OOooOOo . OooO0OoOOOO . OooO0OoOOOO % O0OoO
iII = '{UJ},' ; O0ooo = '{WE},' ; II1ii1iii1ii = '{WP},' ; I11iIiI1 = '{PP},'
def i1I1iiii1Ii11 ( url ) :
 OO0O00oOo = iiI111I1iIiI ( url )
 Ii1i = re . compile ( 'href="(.+?)".+?src="(.+?)" alt="Image of (.+?)"' , re . DOTALL ) . findall ( OO0O00oOo )
 for url , I1II1I11I1I , ooo in Ii1i :
  II1Ii1iI1i1 ( ( '[COLORgreen]' + ooo + '[/COLOR]' ) . replace ( '&#x27;' , '' ) , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7067 , I1II1I11I1I )
  if 25 - 25: Ii / OOooOOo - IIIi / oO0o . I11i . I11i
def iI1 ( url ) :
 OO0O00oOo = iiI111I1iIiI ( url )
 Ii1i = re . compile ( '<div class="film-container">.+?<iframe src="(.+?)"' , re . DOTALL ) . findall ( OO0O00oOo )
 for url in Ii1i :
  iIIII1 ( 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) )
  if 65 - 65: o0o00Oo0O / IIiIiII11i . iI11I1II1I1I . OoOo00o / I1ii11iIi11i % iI11I1II1I1I
def iIIII1 ( url ) :
 OO0O00oOo = iiI111I1iIiI ( url )
 Ii1i = re . compile ( 'file: "(.+?)",.+?label: "(.+?)"' , re . DOTALL ) . findall ( OO0O00oOo )
 for url , ooo in Ii1i :
  oOO0oo ( '[COLORgreen]' + ooo + '[/COLOR]' , url , 222 , ooOooo000oOO + 'popcorn.png' )
  if 74 - 74: ooOoO0O00 / oOo0O0Ooo % Ii1I / o0o00Oo0O % iI1iI1I1i1I - OOooOOo
  if 31 - 31: oOo0O0Ooo / ii . iI11I1II1I1I * OOooOOo . ii + IIiIiII11i
  if 8 - 8: Ii1I * Ii1I * ooOoO0O00 + o0oOO0O00o0O . Ii1I
  if 100 - 100: ii - o0o00Oo0O . iI1iI1I1i1I / iI1iI1I1i1I + IIiIiII11i * OOooOOo
def i11111 ( url ) :
 OO0O00oOo = iiI111I1iIiI ( url )
 Ii1i = re . compile ( '</h4><p><ul><li><a href="([^"]*)">(.+?)<.+?class=' ) . findall ( OO0O00oOo )
 I1 = re . compile ( '<li><a href="([^"]*)">(.+?)<.+?class=' ) . findall ( OO0O00oOo )
 for url , ooo in Ii1i :
  if '(cooltvseries.com)' in ooo :
   oOO0oo ( ( '[COLORgreen]' + ooo + ' -(360)-[/COLOR]' ) . replace ( ' - (cooltvseries.com).mp4' , '' ) , url , 7053 , ooOooo000oOO + 'CoolSeries.png' )
 for url , ooo in I1 :
  if '(cooltvseries.com)' in ooo :
   oOO0oo ( ( '[COLORgreen]' + ooo + '[/COLOR]' ) . replace ( ' - (cooltvseries.com).mp4' , '' ) , url , 7053 , ooOooo000oOO + 'CoolSeries.png' )
def o0o00OoOo0 ( url ) :
 OO0O00oOo = iiI111I1iIiI ( url )
 Ii1i = re . compile ( '<source type="video/mp4" src="([^"]*)"/>' ) . findall ( OO0O00oOo )
 for url in Ii1i :
  i1iii11 ( ( url ) . replace ( ' ' , '%20' ) )
oo0O0000O0 = '{XX},' ; o0OO0ooOOO = '{UD},' ; i1i1I1Ii1IIii = '{YT},' ; oooOOoo = '{JS},' ; iI1iii1iIiiI = '{PF},'
if 36 - 36: oO0o - o0o00Oo0O * oOo0O0Ooo / Ii1I / IIIii1II1II
def IiiIiiIIII ( ) :
 OO0O00oOo = iiI111I1iIiI ( i1111 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vc2VjcmV0L2Nsb3VkLnBocA==' ) )
 Ii1i = re . compile ( '<li class="col-sm-2">.+?<a href="#" class="thumbnail" data-src="(.+?)" data-toggle="modal".+?data-target="#infoModal" name="(.+?)"> <img src="(.+?)" alt=".+?" width="130px"' , re . DOTALL ) . findall ( OO0O00oOo )
 for Ii1II1I11i1 , ooo , I1II1I11I1I in Ii1i :
  oOO0oo ( '[COLORgreen]' + ooo + '[/COLOR]' , 'http://stream.cloudtv.bz/stream/channel/20/' + ( i1111 ( Ii1II1I11i1 ) ) , 222 , I1II1I11I1I )
  if 88 - 88: oO0o . IIIi / iI1iI1I1i1I
def iIiI1I1 ( url ) :
 OO0O00oOo = iiI111I1iIiI ( url )
 Ii1i = re . compile ( 'src="([^"]*)".+?alt=""></a><div class="entry unvoted"><p class="title"><a class="title may-blank " href="([^"]*)" tabindex=.+?>(.+?)</a>' , re . DOTALL ) . findall ( OO0O00oOo )
 next = re . compile ( '<a href="([^"]*)" rel="nofollow next"' , re . DOTALL ) . findall ( OO0O00oOo )
 for I1II1I11I1I , url , ooo in Ii1i :
  if 'youtu' in url :
   oOO0oo ( ( '[COLORgreen]' + ooo + '[/COLOR]' ) . replace ( '&quot;' , '"' ) . replace ( '&' , ' & ' ) , url , 7051 , 'http:' + I1II1I11I1I )
 for url in next :
  II1Ii1iI1i1 ( '[COLORgreen]NEXT[/COLOR]' , url , 7050 , ooOooo000oOO + 'Next.png' )
  if 62 - 62: I11i / iI11I1II1I1I
def O0OOoOoo0OOo ( url ) :
 OO0O00oOo = iiI111I1iIiI ( url )
 Ii1i = re . compile ( 'rel="shortlink" href="([^"]*)">' , re . DOTALL ) . findall ( OO0O00oOo )
 for url in Ii1i :
  yt . PlayVideo ( ( url ) . replace ( 'https://youtu.be/' , '' ) )
  if 30 - 30: o0o00Oo0O / IIIii1II1II % iI1iI1I1i1I
def i1I ( url ) :
 OO0O00oOo = iiI111I1iIiI
 Ii1i = re . compile ( 'id:"(.+?)",url:"(.+?)"' , re . DOTALL ) . findall ( OO0O00oOo )
 for url , I1II1I11I1I , ooo in Ii1i :
  II1Ii1iI1i1 ( '[COLORgreen]' + ooo + '[/COLOR]' , url , 222 , I1II1I11I1I )
  if 23 - 23: oOo0O0Ooo * O0OoO / OOooOOo . iI11I1II1I1I % Ii
  if 61 - 61: o0o00Oo0O
  if 21 - 21: oO0o % iI11I1II1I1I . oO0o
  if 99 - 99: I11i * IIIii1II1II % OoOo00o * OoOo00o + ii
  if 82 - 82: iI1iI1I1i1I / OOooOOo - IIIii1II1II / O0OoO
def I1iIIi ( ) :
 if 46 - 46: oOo0O0Ooo . OooO0OoOOOO - Ii - IIIi
 II1Ii1iI1i1 ( 'All Channels' , '' , 7021 , ooOooo000oOO + 'livetv.png' )
 II1Ii1iI1i1 ( 'Entertainment' , '' , 7021 , ooOooo000oOO + 'livetv.png' )
 II1Ii1iI1i1 ( 'Movies' , '' , 7021 , ooOooo000oOO + 'livetv.png' )
 II1Ii1iI1i1 ( 'Music' , '' , 7021 , ooOooo000oOO + 'livetv.png' )
 II1Ii1iI1i1 ( 'News' , '' , 7021 , ooOooo000oOO + 'livetv.png' )
 II1Ii1iI1i1 ( 'Sports' , '' , 7021 , ooOooo000oOO + 'livetv.png' )
 II1Ii1iI1i1 ( 'Documentary' , '' , 7021 , ooOooo000oOO + 'livetv.png' )
 II1Ii1iI1i1 ( 'Kids' , '' , 7021 , ooOooo000oOO + 'livetv.png' )
 II1Ii1iI1i1 ( 'Food' , '' , 7021 , ooOooo000oOO + 'livetv.png' )
 II1Ii1iI1i1 ( 'Religious' , '' , 7021 , ooOooo000oOO + 'livetv.png' )
 II1Ii1iI1i1 ( 'USA Channels' , '' , 7021 , ooOooo000oOO + 'livetv.png' )
 II1Ii1iI1i1 ( 'Other' , '' , 7021 , ooOooo000oOO + 'livetv.png' )
 if 97 - 97: IIiIiII11i % I1ii11iIi11i * OooO0OoOOOO
 if 51 - 51: I1ii11iIi11i % IIIii1II1II . I1ii11iIi11i
def o0o0oO0OOO ( Cat_Name ) :
 if 66 - 66: Ii11Ii1I * iI11I1II1I1I - O0OoO / oOo0O0Ooo
 o0i1I = False
 O0o0o00OoOo = '0'
 if Cat_Name == 'All Channels' : o0i1I = True
 if Cat_Name == 'Entertainment' : O0o0o00OoOo = '1'
 if Cat_Name == 'Movies' : O0o0o00OoOo = '2'
 if Cat_Name == 'Music' : O0o0o00OoOo = '3'
 if Cat_Name == 'News' : O0o0o00OoOo = '4'
 if Cat_Name == 'Sports' : O0o0o00OoOo = '5'
 if Cat_Name == 'Documentary' : O0o0o00OoOo = '6'
 if Cat_Name == 'Kids' : O0o0o00OoOo = '7'
 if Cat_Name == 'Food' : O0o0o00OoOo = '8'
 if Cat_Name == 'Religious' : O0o0o00OoOo = '9'
 if Cat_Name == 'USA Channels' : O0o0o00OoOo = '10'
 if Cat_Name == 'Other' : O0o0o00OoOo = '11'
 if 85 - 85: Ii11Ii1I
 OO0O00oOo = iiI111I1iIiI ( i1111 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz' ) )
 Ii1i = re . compile ( '"id":".+?","name":"(.+?)","img":"(.+?)","stream_url3":".+?","cat_id":"(.+?)","stream_url2":".+?","stream_url":".+?"}' , re . DOTALL ) . findall ( OO0O00oOo )
 print 'Len Match: >>>' + str ( len ( Ii1i ) )
 for ooo , I1II1I11I1I , iiIiIi1111iI1 in Ii1i :
  III = i1111 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv' ) + ( I1II1I11I1I ) . replace ( '\\' , '' )
  if iiIiIi1111iI1 == O0o0o00OoOo :
   II1Ii1iI1i1 ( ooo , '' , 7022 , III )
  elif o0i1I == True :
   II1Ii1iI1i1 ( ooo , '' , 7022 , III )
  else : pass
  if 61 - 61: oOo0O0Ooo * I1ii11iIi11i % Ii1I * IIiIiII11i / IIiIiII11i + ooOoO0O00
  xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 17 - 17: ii % OoOo00o - ooOoO0O00 % OooO0OoOOOO % I1ii11iIi11i
def IiOO0OOOOOo ( Search_Name ) :
 OO0O00oOo = iiI111I1iIiI ( i1111 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz' ) )
 Ii1i = re . compile ( '"id":".+?","name":"' + Search_Name + '","img":"(.+?)","stream_url3":"(.+?)","cat_id":".+?","stream_url2":"(.+?)","stream_url":"(.+?)"}' , re . DOTALL ) . findall ( OO0O00oOo )
 Ii1i = re . compile ( '"id":".+?","name":"' + Search_Name + '","img":"(.+?)","stream_url3":"(.+?)","cat_id":".+?","stream_url2":"(.+?)","stream_url":"(.+?)"}' , re . DOTALL ) . findall ( OO0O00oOo )
 for I1II1I11I1I , Ii1II1I11i1 , ooo0O0o00O , IiIi1I1 in Ii1i :
  III = i1111 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv' ) + ( I1II1I11I1I ) . replace ( '\\' , '' )
  oOO0oo ( Search_Name + ': Link 1' , ( Ii1II1I11i1 ) . replace ( '\\' , '' ) , 222 , III )
  oOO0oo ( Search_Name + ': Link 2' , ( ooo0O0o00O ) . replace ( '\\' , '' ) , 222 , III )
  oOO0oo ( Search_Name + ': Link 3' , ( IiIi1I1 ) . replace ( '\\' , '' ) , 222 , III )
  if 7 - 7: o0o00Oo0O + Ii11Ii1I . IIiIiII11i
def iii11i1i1 ( ) :
 OO0O00oOo = iiI111I1iIiI ( i1111 ( o0OO00 ( 0 , [ 97 ] , [ 221 , 72 , 245 , 82 , 68 , 48 , 242 , 99 , 143 , 68 , 9 , 111 , 24 , 118 , 180 , 76 , 29 , 51 , 14 , 100 , 187 , 51 , 105 , 100 , 106 , 121 , 52 , 53 , 240 , 114 , 26 , 98 , 252 , 50 , 197 , 82 , 218 , 112 , 19 , 99 , 94 , 71 , 54 , 120 , 104 , 108 , 174 , 101 , 107 , 72 , 168 , 82 , 191 , 50 , 88 , 76 , 90 , 109 , 138 , 78 , 24 , 118 , 89 , 76 , 218 , 110 , 231 , 86 , 105 , 114 , 252 , 76 , 37 , 50 , 36 , 82 , 96 , 118 , 27 , 100 , 120 , 50 , 160 , 53 , 72 , 115 , 200 , 98 , 80 , 50 , 201 , 70 , 114 , 107 , 9 , 99 , 113 , 121 , 127 , 57 , 155 , 106 , 213 , 97 , 194 , 71 , 192 , 70 , 162 , 116 , 27 , 99 , 46 , 71 , 191 , 108 , 4 , 118 , 24 , 98 , 27 , 109 , 105 , 108 , 89 , 119 , 164 , 100 , 88 , 72 , 237 , 89 , 93 , 117 , 40 , 98 , 211 , 84 , 75 , 78 , 216 , 49 ] ) ) )
 Ii1i = re . compile ( '#EXTINF:-1,(.+)\s*(.+)\s*' ) . findall ( OO0O00oOo )
 for ooo , Ii1II1I11i1 in Ii1i :
  oOO0oo ( ooo , ( Ii1II1I11i1 ) . replace ( '"' , ' ' ) . replace ( '&' , '&' ) . strip ( ) + '|connection=keep-alive' , 222 , ooOooo000oOO + 'english.png' )
def o00OOo0o ( ) :
 OO0O00oOo = iiI111I1iIiI ( i1111 ( o0OO00 ( 0 , [ 97 ] , [ 221 , 72 , 245 , 82 , 68 , 48 , 242 , 99 , 143 , 68 , 9 , 111 , 24 , 118 , 180 , 76 , 29 , 51 , 14 , 100 , 187 , 51 , 105 , 100 , 106 , 121 , 52 , 53 , 240 , 114 , 26 , 98 , 252 , 50 , 197 , 82 , 218 , 112 , 19 , 99 , 94 , 71 , 54 , 120 , 104 , 108 , 174 , 101 , 107 , 72 , 168 , 82 , 191 , 50 , 88 , 76 , 90 , 109 , 138 , 78 , 24 , 118 , 89 , 76 , 218 , 110 , 231 , 86 , 105 , 114 , 252 , 76 , 37 , 50 , 36 , 82 , 96 , 118 , 27 , 100 , 120 , 50 , 160 , 53 , 72 , 115 , 200 , 98 , 80 , 50 , 201 , 70 , 114 , 107 , 9 , 99 , 113 , 121 , 127 , 57 , 155 , 106 , 213 , 97 , 194 , 71 , 192 , 70 , 162 , 116 , 27 , 99 , 46 , 71 , 191 , 108 , 4 , 118 , 24 , 98 , 27 , 109 , 105 , 108 , 89 , 119 , 164 , 100 , 88 , 72 , 237 , 89 , 93 , 117 , 40 , 98 , 211 , 84 , 75 , 78 , 216 , 49 ] ) ) )
 Ii1i = re . compile ( '#EXTINF:-2,(.+)\s*(.+)\s*' ) . findall ( OO0O00oOo )
 for ooo , Ii1II1I11i1 in Ii1i :
  oOO0oo ( ooo , ( Ii1II1I11i1 ) . replace ( '"' , ' ' ) . replace ( '&' , '&' ) . strip ( ) , 222 , ooOooo000oOO + 'xxx.png' )
def IiIiI ( ) :
 OO0O00oOo = iiI111I1iIiI ( i1111 ( o0OO00 ( 0 , [ 97 , 129 , 72 , 149 , 82 , 100 , 48 , 63 , 99 , 170 , 68 , 159 , 111 , 42 , 118 , 83 , 76 , 128 , 51 , 61 , 100 , 44 , 51 , 201 , 100 , 148 , 121 , 134 , 53 ] , [ 159 , 114 , 70 , 98 , 144 , 50 , 37 , 82 , 253 , 112 , 184 , 99 , 50 , 71 , 154 , 120 , 110 , 108 , 179 , 101 , 250 , 72 , 65 , 82 , 125 , 50 , 52 , 76 , 28 , 109 , 124 , 78 , 191 , 118 , 193 , 76 , 193 , 110 , 145 , 86 , 92 , 114 , 193 , 76 , 41 , 50 , 82 , 82 , 206 , 118 , 32 , 100 , 163 , 50 , 209 , 53 , 191 , 115 , 42 , 98 , 30 , 50 , 237 , 70 , 26 , 107 , 70 , 99 , 64 , 121 , 115 , 57 , 230 , 116 , 32 , 97 , 39 , 88 , 58 , 104 , 38 , 50 , 77 , 98 , 185 , 50 , 86 , 81 , 80 , 117 , 111 , 98 , 226 , 84 , 75 , 78 , 210 , 49 ] ) ) )
 Ii1i = re . compile ( '#EXTINF:.+?,(.+)\s*(.+)\s*' ) . findall ( OO0O00oOo )
 for ooo , Ii1II1I11i1 in Ii1i :
  oOO0oo ( ooo , ( Ii1II1I11i1 ) . replace ( '"' , ' ' ) . replace ( '&' , '&' ) . strip ( ) , 222 , ooOooo000oOO + 'vod(1).png' )
  if 77 - 77: I11i
def O0oo0000o ( url ) :
 url
 OOoO0oooO = xbmcgui . ListItem ( ooo , path = url )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , OOoO0oooO )
 return
 if 66 - 66: o0oOO0O00o0O / Ii * o0o00Oo0O
 if 78 - 78: OooO0OoOOOO - iI1iI1I1i1I % o0o00Oo0O - IIIii1II1II % oO0o
def i11IiIi ( url ) :
 OO0O00oOo = iiI111I1iIiI ( url )
 Ii1i = re . compile ( '<a class=.+?href="(.+?)">.+?<div class="videothumboverlay hidden-xs" id=".+?">(.+?)</div>.+?<div class="videothumbbox"><img src="(.+?)" class="videothumb" alt="(.+?)"></div>' , re . DOTALL ) . findall ( OO0O00oOo )
 I1 = re . compile ( "<a href='(.+?)' class='paginationnext'>Next &raquo;</a></div>" ) . findall ( OO0O00oOo )
 for url , iiIII1i , I1II1I11I1I , ooo in Ii1i :
  II1I ( ooo , 'https://www.fitnessblender.com' + url , 7086 , 'https://www.fitnessblender.com' + I1II1I11I1I , '' , ( iiIII1i ) . replace ( '</p>' , ' ' ) . replace ( '<p>' , ' ' ) )
  iiO0o0oOOOoOo ( 'tvshows' , 'Media Info 3' )
 for url in I1 :
  II1Ii1iI1i1 ( 'NEXT' , 'https://www.fitnessblender.com' + url , 7085 , ooOooo000oOO + 'Next.png' )
  if 24 - 24: iI1iI1I1i1I / Ii11Ii1I * O0OoO - Ii
def OoiIiiII ( url ) :
 o00OO00OoO = iiI111I1iIiI ( url )
 Ii1i = re . compile ( '<div class=\'videowrapper\'>.+?src="//www.youtube.com/embed/(.+?)?rel=0&amp;wmode=transparent" frameborder="0"></iframe></div>.+?<h3 class="videodetailheader">(.+?)</h3>.+?<p class="videodetailvalue"><img src=\'(.+?)\'/></p>' , re . DOTALL ) . findall ( o00OO00OoO )
 for url , iiIII1i , I1II1I11I1I in Ii1i :
  ooOOoooooo ( 'PLAY' , url , 8043 , 'https://www.fitnessblender.com' + I1II1I11I1I , '' , iiIII1i )
  iiO0o0oOOOoOo ( 'tvshows' , 'Media Info 3' )
 OOo00OO00Oo = re . compile ( '<h2 class="videodetailheader">Workout Details</h2>(.+?)</div>' , re . DOTALL ) . findall ( o00OO00OoO )
 for iII1I in OOo00OO00Oo :
  o00oOOo0Oo = ( iII1I ) . replace ( '<p>' , '' ) . replace ( '</p>' , '' ) . replace ( '<br />' , '' ) . replace ( '&nbsp;' , '' ) . replace ( '<strong>' , '' ) . replace ( '</strong>' , '' ) . replace ( '"' , '' ) . replace ( '<' , '' ) . replace ( '>' , '' ) . replace ( 'a href' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&rsquo;t' , '' ) . replace ( '&' , '&' )
  II1I ( 'INFO' , '' , 7087 , 'https://www.fitnessblender.com' + I1II1I11I1I , '' , o00oOOo0Oo )
  if 91 - 91: IIiIiII11i - iI11I1II1I1I / ooOoO0O00 * ooOoO0O00 % I1ii11iIi11i
def o0OOoOooO0ooO ( INFO ) :
 I1Ii ( 'info for workout' , INFO )
 if 50 - 50: Ii + ii / o0o00Oo0O + I11i / Ii + OoOo00o
 if 90 - 90: o0oOO0O00o0O * Ii11Ii1I - o0oOO0O00o0O + oO0o + iI1iI1I1i1I % o0o00Oo0O
 if 11 - 11: IIIii1II1II % IIIi * OOooOOo
def OoO00oo0 ( url ) :
 OO0O00oOo = iiI111I1iIiI ( url )
 Ii1i = re . compile ( 'cat-item-.+?"><a href="(.+?)" >(.+?)</a>' ) . findall ( OO0O00oOo )
 for url , ooo in Ii1i :
  II1Ii1iI1i1 ( ooo , url , 9031 , ooOooo000oOO + 'icon.png' )
def oOOO ( url ) :
 OO0O00oOo = iiI111I1iIiI ( url )
 Ii1i = re . compile ( '<a href="(.+?)" title=".+?" rel="bookmark"><time class="entry-date published updated" datetime=".+?">(.+?)</time></a>' ) . findall ( OO0O00oOo )
 for url , ooo in Ii1i :
  II1Ii1iI1i1 ( ooo , url , 9032 , ooOooo000oOO + 'icon.png' )
def o00OoOooo ( url ) :
 OO0O00oOo = iiI111I1iIiI ( url )
 Ii1i = re . compile ( '#EXTINF:-.+?,(.+)\s*(.+)\s*' ) . findall ( OO0O00oOo )
 for ooo , url in Ii1i :
  if '://' in ooo :
   pass
   oOO0oo ( ( ooo ) . replace ( '<br />' , '' ) , ( url ) . replace ( '<br />' , '' ) , 222 , ooOooo000oOO + 'icon.png' )
def i1I1ii1 ( url ) :
 OO0O00oOo = iiI111I1iIiI ( url )
 Ii1i = re . compile ( 'EXTINF:-.+?,(.+)</div></li><li class=".+?"><div class=".+?">(.+?)</div>).findall' ) . findall ( OO0O00oOo )
 for ooo , url in Ii1i :
  oOO0oo ( ooo , url , 222 , ooOooo000oOO + 'icon.png' )
  if 28 - 28: o0o00Oo0O / Ii11Ii1I / OooO0OoOOOO / iI11I1II1I1I
  if 64 - 64: OoOo00o
  if 5 - 5: Ii
def Oo0o0oo0 ( ) :
 OO0O00oOo = iiI111I1iIiI ( 'http://www.disclose.tv/action/videolist/aliens/page/1/all/channel/1/category/1/' )
 Ii1i = re . compile ( '<li><a href="([^"]*)">(.+?)</a></li>' ) . findall ( OO0O00oOo )
 for Ii1II1I11i1 , ooo in Ii1i :
  II1Ii1iI1i1 ( ooo , 'http://www.disclose.tv/' + Ii1II1I11i1 , 7010 , ooOooo000oOO + 'disclose.png' )
  if 86 - 86: OoOo00o % o0o00Oo0O + oO0o
  if 52 - 52: I1ii11iIi11i / o0oOO0O00o0O
def Iii1IIII1Iii ( url ) :
 OO0O00oOo = iiI111I1iIiI ( url )
 Ii1i = re . compile ( 'href="([^"]*)"><img width="135" height="76" alt="([^"]*)".+?src="([^"]*)" />' , re . DOTALL ) . findall ( OO0O00oOo )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' ) . findall ( OO0O00oOo )
 for url , ooo , I1II1I11I1I in Ii1i :
  II1Ii1iI1i1 ( ooo , 'http://www.disclose.tv/' + url , 7011 , I1II1I11I1I )
 for url in next :
  II1Ii1iI1i1 ( 'NEXT' , url , 7010 , ooOooo000oOO + 'Next.png' )
  if 94 - 94: OoOo00o . I11i % I11i % oOo0O0Ooo - o0oOO0O00o0O / Ii
  if 73 - 73: o0o00Oo0O * IIIi . ooOoO0O00
def OO00OoOO ( url ) :
 OO0O00oOo = iiI111I1iIiI ( url )
 Ii1i = re . compile ( 'url: "([^"]*)",' , re . DOTALL ) . findall ( OO0O00oOo )
 I1 = re . compile ( "src='([^']*)' type='([^']*)' />" , re . DOTALL ) . findall ( OO0O00oOo )
 for url in Ii1i :
  if 'http' in url :
   oOO0oo ( 'video/flv' , url , 222 , ooOooo000oOO + 'disclose.png' )
 for url , ooo in I1 :
  oOO0oo ( ooo , url , 222 , ooOooo000oOO + 'disclose.png' )
  if 45 - 45: IIiIiII11i * ooOoO0O00
  if 25 - 25: OOooOOo + iI11I1II1I1I % iI1iI1I1i1I / I1ii11iIi11i * I1ii11iIi11i
def OOOOO0oO0 ( url ) :
 OO0O00oOo = iiI111I1iIiI ( url )
 Ii1i = re . compile ( '<div id="play-1".+?src="(.+?)" scrolling="no".+?<li><a href="#play-1">(.+?)</a></li>' , re . DOTALL ) . findall ( OO0O00oOo )
 for url , ooo in Ii1i :
  II1Ii1iI1i1 ( ooo , ( url + '&fv=&sou=' ) . replace ( 'player' , 'watch' ) , 7000 , ooOooo000oOO + 'icon.png' )
  if 41 - 41: IIiIiII11i . oOo0O0Ooo / oO0o . O0OoO
def O00oooO00oo ( name , url , img ) :
 o00OO00OoO = iiI111I1iIiI ( url )
 Ii111III1i11I = re . compile ( '<iframe class="playerframe" src="(.+?)" scrolling=".+?" marginwidth=".+?" marginheight=".+?" vspace=".+?" hspace=".+?" allowfullscreen=".+?" webkitallowfullscreen=".+?" mozallowfullscreen=".+?" width=".+?" height=".+?" frameborder=".+?"></iframe>' , re . DOTALL ) . findall ( o00OO00OoO )
 O0iI1iIi = len ( Ii111III1i11I )
 if 19 - 19: IIIi * OooO0OoOOOO . I1ii11iIi11i - I1ii11iIi11i - oO0o
 if 51 - 51: o0o00Oo0O * oOo0O0Ooo / OooO0OoOOOO - Ii1I
 if O0iI1iIi == 1 :
  for oooo0 in Ii111III1i11I :
   oooo0 = oooo0 . replace ( 'player' , 'watch' )
   OOOOiiI = oooo0 + '&fv=&sou='
   o000Ooo00o00O = iiI111I1iIiI ( OOOOiiI )
   ooo0O0O0oo0 = re . compile ( '<source src="(.+?)" type=".+?">' , re . DOTALL ) . findall ( o000Ooo00o00O )
   for ii1IIiI1IIi in ooo0O0O0oo0 :
    oo000oO = False
    Resolve ( ii1IIiI1IIi )
    if 8 - 8: oOo0O0Ooo % IIiIiII11i - I11i - iI1iI1I1i1I % oOo0O0Ooo
 elif O0iI1iIi > 1 :
  if 93 - 93: Ii11Ii1I * o0oOO0O00o0O / IIIii1II1II
  for oooo0 in Ii111III1i11I :
   oooO00oo0 = iiI111I1iIiI ( oooo0 )
   o000 = re . compile ( '<iframe width=".*?" height=".*?" frameborder=".*?" src="(.*?)" scrolling=".*?" marginwidth=".*?" marginheight=".*?" vspace=".*?" hspace=".*?" allowfullscreen=".*?" webkitallowfullscreen=".*?" mozallowfullscreen=".*?"></iframe>' , re . DOTALL ) . findall ( oooO00oo0 )
   oOiiIIIII = o000
   oOiiIIIII = ( str ( oOiiIIIII ) ) . replace ( '[\'' , '' ) . replace ( '\']' , '' ) ;
   print 'Stripped url : ' + oOiiIIIII
   oOO0oo ( 'DOUBLE LINK' , oOiiIIIII , 424 , '' )
   if 19 - 19: IIiIiII11i / OOooOOo
   for url in o000 :
    II1Ii1iI1i1 ( 'DOUBLE LINK' , url , 424 , '' )
    try :
     ooo0O0o00O = Google . resolve ( url )
    except :
     pass
    try :
     oOoo00 = re . findall ( r"{'url': u'(.*?)', 'quality': 'HD'}, {'url': u'(.*?)', 'quality': 'SD'}" , str ( ooo0O0o00O ) )
     for IIiIi , I1I1IIiiI1 in oOoo00 :
      if 79 - 79: Ii11Ii1I
      HD_URLS . append ( IIiIi )
      SD_URLS . append ( I1I1IIiiI1 )
    except :
     pass
 else :
  pass
  if 27 - 27: oO0o + I1ii11iIi11i
def oO0oOOooO0 ( ) :
 if 62 - 62: Ii - iI1iI1I1i1I
 if 81 - 81: iI1iI1I1i1I
 II1Ii1iI1i1 ( 'Genres' , 'http://cnfstudio.com/movies/' , 7002 , ooOooo000oOO + 'Movies.png' )
 if 92 - 92: IIIii1II1II - I1ii11iIi11i - ii / OooO0OoOOOO - ooOoO0O00
 II1Ii1iI1i1 ( 'Search Movies' , '' , 7017 , ooOooo000oOO + 'Movies.png' )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 81 - 81: ooOoO0O00 / IIIi % Ii . iI11I1II1I1I * OOooOOo + ii
 if 31 - 31: ooOoO0O00 % IIiIiII11i
def Ii1iii11I ( ) :
 OO0O00oOo = iiI111I1iIiI ( 'http://cnfstudio.com/' )
 Ii1i = re . compile ( '<a href="http://cnfstudio.com/genre/(.+?)">(.+?)</a>' ) . findall ( OO0O00oOo )
 for Ii1II1I11i1 , ooo in Ii1i :
  II1Ii1iI1i1 ( ooo , 'http://cnfstudio.com/genre/' + Ii1II1I11i1 , 7003 , ooOooo000oOO + 'icon.png' )
  if 2 - 2: ii - Ii11Ii1I % OoOo00o / oOo0O0Ooo / I11i
i1iiIIiiI111 = xbmcgui . Dialog ( )
if 3 - 3: IIiIiII11i / IIIii1II1II
i1IIiiIIIIi = '{UN},' ; IiIIIi = '{IG},' ; Oo0iII = '{PL},' ; O0oo = '{LO},' ; iIIi1OoOo0O00 = '{LP},' ; iI1i1iI1iI = '{HA},' ; I1IIiIi = '{XD},' ; OOOOoOoO = '{TA},' ; OO000o0oOoo0o = '{DP},' ; IiiIiIIi = '{JT},' ; O00Oo = '{JJ},' ; oOOoo = '{MM},' ; oo0O0 = '{FQ},' ; Ii111Ii11 = '{HH},'
if 10 - 10: ii . oOo0O0Ooo * o0o00Oo0O * oO0o - IIIii1II1II
def IIIiII11 ( url ) :
 OO0O00oOo = iiI111I1iIiI ( url )
 Ii1i = re . compile ( '<div class="movie">.+?<img src="(.+?)" alt=".+?" />.+?<a href="(.+?)"><span class="player"></span></a>.+?<h2>(.+?)</h2>' , re . DOTALL ) . findall ( OO0O00oOo )
 O00OO00OOOoO = re . compile ( "<link rel='next' href='(.+?)'/>" ) . findall ( OO0O00oOo )
 for I1II1I11I1I , url , ooo in Ii1i :
  oOO0oo ( ( ooo ) . replace ( '&#038;' , '' ) . replace ( '&#8216;' , '' ) . replace ( '&#8217;' , '' ) . replace ( '&#8211;' , '' ) , url , 7004 , I1II1I11I1I )
 O00OO00OOOoO = O00OO00OOOoO
 for url in O00OO00OOOoO :
  II1Ii1iI1i1 ( 'Next Page' , url , 7003 , ooOooo000oOO + 'Next.png' )
  if 47 - 47: ooOoO0O00 % O0OoO - I1ii11iIi11i * iI1iI1I1i1I / Ii
def Iii1Iii ( url ) :
 if 48 - 48: IIIii1II1II
 OO0O00oOo = iiI111I1iIiI ( url )
 Ii1i = re . compile ( '<div id="play-1" class="player-content"><iframe class="playerframe" src="(.+?)" scrolling="no".+?</div>' , re . DOTALL ) . findall ( OO0O00oOo )
 for url in Ii1i :
  O000oo0O = url + '&fv=&sou='
  O000oo0O = O000oo0O . replace ( 'player' , 'watch' )
  I1111III111ii = o0oO0oOooO ( O000oo0O )
  oo00o00O0 = o0oO0oOooO ( url )
  if 52 - 52: o0oOO0O00o0O + o0o00Oo0O % I11i % o0o00Oo0O % IIiIiII11i + ii
  if 51 - 51: o0oOO0O00o0O % Ii
def o0oO0oOooO ( url ) :
 if 28 - 28: Ii1I + Ii1I % OOooOOo
 OO0O00oOo = iiI111I1iIiI ( url )
 Ii1i = re . compile ( '<video id=".+?<source src="(.+?)" type="video/mp4">' , re . DOTALL ) . findall ( OO0O00oOo )
 for url in Ii1i :
  I1i11 ( url )
  if 12 - 12: iI1iI1I1i1I
  if 19 - 19: Ii11Ii1I * ooOoO0O00 % o0o00Oo0O + iI1iI1I1i1I
def I1i1ii1ii ( ) :
 II1I ( '[COLORgreen]Local M3u[/COLOR]' , oOo0oooo00o , 2001 , ooOooo000oOO + 'loader.png' , i1iiIII111ii , '' )
 II1I ( '[COLORgreen]Remote M3u[/COLOR]' , Oo0o0000o0o0 , 1009 , ooOooo000oOO + 'loader.png' , i1iiIII111ii , '' )
 if 32 - 32: OooO0OoOOOO / ii
def IIIIIIi1IIi1I11i ( url ) :
 Ii1i = re . compile ( '^#EXTINF:-?[0-9]*(.*?),(.*?)\n(.*?)$' , re . I + re . M + re . U + re . S ) . findall
 for O0o0oOooOoo , ooo , url in Ii1i :
  oOO0oo ( ooo , url , 222 , ooOooo000oOO + 'streams.png' )
  if 59 - 59: Ii1I + iI1iI1I1i1I . OoOo00o
  if 87 - 87: oO0o
def oo00O00oO ( ) :
 o00OO00OoO = iiI111I1iIiI ( i1111 ( 'aHR0cHM6Ly9naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvdHJlZS9tYXN0ZXIvX3JlcG8vcGx1Z2luLnZpZGVvLkdlbmllVHY=' ) )
 Ii1i = re . compile ( '<span class="css-truncate css-truncate-target"><a href="/GenieTv/Genie_Tv/blob/master/_repo/plugin.video.GenieTv/(.+?)" class="js-navigation-open" id=".+?" title=".+?">.+?</a></span>' ) . findall ( o00OO00OoO )
 for Ii1II1I11i1 in Ii1i :
  Ii1II1I11i1 = i1111 ( 'aHR0cDovL3Jhdy5naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvbWFzdGVyL19yZXBvL3BsdWdpbi52aWRlby5HZW5pZVR2Lw==' ) + Ii1II1I11i1
 ooo = 'plugin.video.GenieTv'
 if 34 - 34: IIIi . OOooOOo / Ii / o0oOO0O00o0O
 II1iII1 ( Ii1II1I11i1 , ooo )
 if 31 - 31: Ii11Ii1I * I11i * Ii11Ii1I + oO0o * I11i . IIIi
def oo0OOo ( ) :
 o00OO00OoO = iiI111I1iIiI ( i1111 ( 'aHR0cHM6Ly9naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvdHJlZS9tYXN0ZXIvX3JlcG8vcmVwb3NpdG9yeS5HZW5pZVR2' ) )
 Ii1i = re . compile ( '<span class="css-truncate css-truncate-target"><a href="/GenieTv/Genie_Tv/blob/master/_repo/repository.GenieTv/(.+?)" class="js-navigation-open" id=".+?" title=".+?">.+?</a></span>' ) . findall ( o00OO00OoO )
 for Ii1II1I11i1 in Ii1i :
  Ii1II1I11i1 = i1111 ( 'aHR0cDovL3Jhdy5naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvbWFzdGVyL19yZXBvL3JlcG9zaXRvcnkuR2VuaWVUdi8=' ) + Ii1II1I11i1
 ooo = 'repository.GenieTv'
 if 89 - 89: ii * Ii11Ii1I * oOo0O0Ooo . O0OoO * Ii11Ii1I / o0oOO0O00o0O
 II1iII1 ( Ii1II1I11i1 , ooo )
 if 46 - 46: Ii
 if 15 - 15: o0o00Oo0O / ooOoO0O00 / ooOoO0O00 . o0oOO0O00o0O % OOooOOo + oOo0O0Ooo
def I11111ii1i ( ) :
 II1I ( '[COLORgreen]CATAGORIES[/COLOR]' , '' , 10051 , ooOooo000oOO + 'loader.png' , i1iiIII111ii , '' )
 II1I ( '[COLORgreen]SEARCH[/COLOR]' , '' , 10052 , ooOooo000oOO + 'loader.png' , i1iiIII111ii , '' )
 if 78 - 78: iI1iI1I1i1I % I1ii11iIi11i + OOooOOo . Ii1I % OoOo00o / Ii11Ii1I
 if 37 - 37: OoOo00o % IIIi % OoOo00o
o0oO0 = xbmcaddon . Addon ( id = 'plugin.video.GenieTv' )
oOOoo00O0O = xbmcgui . Dialog ( )
oooOOOOO = xbmc . translatePath ( 'special://home/' )
Oo0oO0ooo = xbmcgui . DialogProgress ( )
iIII = 'https://addons.tvaddons.ag/'
if 43 - 43: o0oOO0O00o0O + Ii
def o00ii11iiIIII ( ) :
 IIiI1i1i = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 IiII111i1i11 = IIiI1i1i . lower ( )
 IiI11i1I11111 = 'https://addons.tvaddons.ag/search/?keyword=' + IiII111i1i11
 o00OO00OoO = iiI111I1iIiI ( IiI11i1I11111 )
 Ii1i = re . compile ( '<li><a href="(.+?)"><span class=".+?"><img src="(.+?)" width=".+?" alt=".+?" class=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( o00OO00OoO )
 for Ii1II1I11i1 , oooiiI , ooo in Ii1i :
  II1I ( ooo , Ii1II1I11i1 , 10054 , 'https://addons.tvaddons.ag/' + oooiiI , i1iiIII111ii , '' )
  if 96 - 96: oOo0O0Ooo % OoOo00o / OoOo00o
  if 81 - 81: OOooOOo + I11i + I1ii11iIi11i
def OO0oO0Oo ( ) :
 o00OO00OoO = iiI111I1iIiI ( iIII )
 Ii1i = re . compile ( '<li><a href="(.+?)"><span class="thumbnail"><img src="(.+?)" class="pic" alt=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( o00OO00OoO )
 for Ii1II1I11i1 , I1II1I11I1I , ooo in Ii1i :
  if 'Repositories' in ooo :
   pass
  elif 'Services' in ooo :
   pass
  elif 'International' in ooo :
   pass
  else :
   II1I ( '[COLORgreen]' + ooo + '[/COLOR]' , Ii1II1I11i1 , 10053 , 'https://addons.tvaddons.ag/' + I1II1I11I1I , i1iiIII111ii , '' )
   if 82 - 82: Ii + iI11I1II1I1I / I1ii11iIi11i + IIIii1II1II * IIiIiII11i
   if 34 - 34: I11i % ii
def Addon ( url ) :
 o00OO00OoO = iiI111I1iIiI ( url )
 iIIIi = re . compile ( '<li class="nextPage"><a class=".+?" href="(.+?)"><dfn title="next Page">.+?</dfn></a></li>' ) . findall ( o00OO00OoO )
 for url in iIIIi :
  II1I ( '[COLORgreen]NEXT PAGE[/COLOR]' , 'https://addons.tvaddons.ag' + url , 10053 , ooOooo000oOO + 'Next.png' , i1iiIII111ii , '' )
 Ii1i = re . compile ( '<li><a href="(.+?)"><span class=".+?"><img src="(.+?)" width=".+?" alt=".+?" class=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( o00OO00OoO )
 for url , I1II1I11I1I , ooo in Ii1i :
  if 'Please' in ooo :
   pass
  else :
   II1I ( ooo , url , 10054 , 'https://addons.tvaddons.ag/' + I1II1I11I1I , i1iiIII111ii , '' )
   if 74 - 74: o0o00Oo0O . iI1iI1I1i1I
   if 64 - 64: O0OoO / ooOoO0O00 % o0oOO0O00o0O
def OOoOo0O0 ( url , name ) :
 o00OO00OoO = iiI111I1iIiI ( url )
 Ii1i = re . compile ( '<a href="(.+?)"' ) . findall ( o00OO00OoO )
 for url in Ii1i :
  if 'plugin' in url :
   print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<' + url
   iI11 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
   Oo0oO0ooo = xbmcgui . DialogProgress ( )
   Oo0oO0ooo . create ( "Origin+Jaybox" , "Downloading Content" , '' , 'Please Wait' )
   iIII1I1i1i = os . path . join ( iI11 , name + '.zip' )
   try :
    os . remove ( iIII1I1i1i )
   except :
    pass
   downloader . download ( url , iIII1I1i1i , Oo0oO0ooo )
   I1IIi = xbmc . translatePath ( os . path . join ( 'special://home' , 'addons' ) )
   time . sleep ( 2 )
   Oo0oO0ooo . update ( 0 , "" , "Extracting Zip Please Wait" )
   print '======================================='
   print I1IIi
   print '======================================='
   extract . all ( iIII1I1i1i , I1IIi , Oo0oO0ooo )
   oooooo0O000o ( )
   if 39 - 39: IIIi . oO0o % O0OoO . IIIii1II1II / o0oOO0O00o0O * oO0o
def II1iII1 ( url , name ) :
 iI11 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 Oo0oO0ooo = xbmcgui . DialogProgress ( )
 Oo0oO0ooo . create ( "Origin+Jaybox" , "Downloading Content" , '' , 'Please Wait' )
 iIII1I1i1i = os . path . join ( iI11 , name + '.zip' )
 try :
  os . remove ( iIII1I1i1i )
 except :
  pass
 downloader . download ( url , iIII1I1i1i , Oo0oO0ooo )
 I1IIi = xbmc . translatePath ( os . path . join ( 'special://home' , 'addons' ) )
 time . sleep ( 2 )
 Oo0oO0ooo . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print I1IIi
 print '======================================='
 extract . all ( iIII1I1i1i , I1IIi , Oo0oO0ooo )
 oooooo0O000o ( )
 if 12 - 12: oOo0O0Ooo / I11i
def oooooo0O000o ( ) :
 xbmc . executebuiltin ( 'UpdateLocalAddons' )
 xbmc . executebuiltin ( 'UpdateAddonRepos' )
 i1iiIIiiI111 = xbmcgui . Dialog ( )
 i1iiIIiiI111 . ok ( "Origin + Genie TV" , '' , '                                 REFRESH SUCCESSFUL :)' , "                          [COLOR gold]Brought To You By Origin + Jaybox[/COLOR]" )
 return
 if 86 - 86: I1ii11iIi11i % OOooOOo
 if 77 - 77: Ii11Ii1I % IIIii1II1II / OoOo00o
def OOoOo ( url ) :
 OO0O00oOo = ii1II ( url )
 Ii1i = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( OO0O00oOo )
 for url , oooiiI , ooo in Ii1i :
  II1Ii1iI1i1 ( ooo , url , 1007 , oooiiI )
def Iiiiiii11IIiI ( url ) :
 OO0O00oOo = ii1II ( url )
 Ii1i = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( OO0O00oOo )
 for url , oooiiI , ooo in Ii1i :
  II1Ii1iI1i1 ( '[COLORgreen]' + ooo + '[/COLOR]' , url , 1006 , oooiiI )
  if 93 - 93: oOo0O0Ooo
  if 35 - 35: iI1iI1I1i1I + IIIii1II1II / IIIii1II1II
def i1IIIi1Iii1i ( url , iconimage , name ) :
 from imports import cache
 cache = cache . get ( '' , 0 , url )
 OO0O00oOo = ii1II ( url )
 Ii1i = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( OO0O00oOo )
 for url , iconimage , iiIII1i , III1I1Iii1iiI , name in Ii1i :
  if 'http' in url :
   if '.php' in url :
    o0i1iI1iiI1I ( name , url , 1016 , iconimage , III1I1Iii1iiI , iiIII1i )
   else :
    if 'youtube' in url :
     iIi ( name , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , iconimage , III1I1Iii1iiI , iiIII1i )
    else :
     iIi ( name , url , 222 , iconimage , III1I1Iii1iiI , iiIII1i )
     iiO0o0oOOOoOo ( 'movies' , 'INFO' )
  else :
   oO0o0O ( url , iconimage , name )
   if 50 - 50: iI11I1II1I1I * OoOo00o
 else :
  Ii1i = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( OO0O00oOo )
  for url , oooiiI , name in Ii1i :
   if 'http' in url :
    if '.php' in url :
     II1Ii1iI1i1 ( name , url , 1016 , oooiiI )
    else :
     if 'youtube' in url :
      print '>>>>>>>>>>>>>>>>>>>>>>> youtube old way'
      oOO0oo ( name , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , oooiiI )
     else :
      oOO0oo ( name , url , 222 , oooiiI )
      iiO0o0oOOOoOo ( 'movies' , 'INFO' )
   else :
    oO0o0O ( url , oooiiI , name )
  xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 return cache
 if 85 - 85: ooOoO0O00
def oO0o0O ( url , iconimage , name ) :
 iconimage = iconimage
 name = name
 url = url
 Oo00 = ( url ) . replace ( oOoo , 'http' ) . replace ( o0OO0ooOOO , '.com' ) ;
 iIIiIi111iI = ( Oo00 ) . replace ( oo0O00ooo0o , 'a' ) . replace ( O0oO0oo0O , 'b' ) . replace ( oooOOO0ooOoOOO , 'c' ) . replace ( O0ooo , 'd' ) . replace ( Oo0iII , 'e' ) . replace ( IiiIiIIi , 'f' ) ;
 II1I1ii = ( iIIiIi111iI ) . replace ( oo0O0000O0 , 'g' ) . replace ( iI1i1iI1iI , 'h' ) . replace ( i1i1I1Ii1IIii , 'i' ) . replace ( iI1iii1iIiiI , 'j' ) . replace ( o0IiIiI111IIII1 , 'k' ) . replace ( OOOoOooO000oO , 'l' ) ;
 oo0OO0O = ( II1I1ii ) . replace ( OO0OooOOoO00OO00 , 'm' ) . replace ( ii11ii1iIiI1 , 'n' ) . replace ( OoOo0oO0 , 'o' ) . replace ( i111iIi1i1 , 'p' ) . replace ( OOo00O0O , 'q' ) . replace ( oooOoO , 'r' ) ;
 IiiIi1IiiiI = ( oo0OO0O ) . replace ( OO0oooOO , 's' ) . replace ( II1ii1iii1ii , 't' ) . replace ( IIIi1iiIIiiiI , 'u' ) . replace ( I1IIiIi1iI , 'v' ) . replace ( oOo0Iiii11 , 'w' ) . replace ( o00000O , 'x' ) ;
 iIiiiII11 = ( IiiIi1IiiiI ) . replace ( ooo00Oo0 , 'y' ) . replace ( iIii1i1Ii , 'z' ) . replace ( i1IIiiIIIIi , '.' ) . replace ( IiIIIi , '(' ) . replace ( O0oo , ')' ) . replace ( iIIi1OoOo0O00 , '/' ) ;
 III1iIii = ( iIiiiII11 ) . replace ( OO0O0OO0O0 , '1' ) . replace ( I11iIiI1 , '2' ) . replace ( iiIII1i1 , '3' ) . replace ( OOOOoOoO , '4' ) . replace ( OO000o0oOoo0o , '5' ) . replace ( oooOOoo , '6' ) ;
 oOOo0OOoOO0 = ( III1iIii ) . replace ( O00Oo , '7' ) . replace ( oOOoo , '8' ) . replace ( oo0O0 , '9' ) . replace ( Ii111Ii11 , '0' ) . replace ( iIIiI11iI1Ii1 , ':' ) . replace ( o00oo , '%' ) ;
 url = ( oOOo0OOoOO0 ) . replace ( iII , '-' ) . replace ( I1IIiIi , '_' ) ;
 oOO0oo ( name , url , 222 , iconimage ) ;
 if 30 - 30: IIiIiII11i / oOo0O0Ooo - O0OoO + OOooOOo * O0OoO / OOooOOo
 if 17 - 17: oO0o
def IIIi11i ( ) :
 OO0O00oOo = ii1II ( i1111 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vdm9kL3VybHMvdXJsLnBocA==' ) )
 Ii1i = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( OO0O00oOo )
 for Ii1II1I11i1 , oooiiI , ooo in Ii1i :
  II1Ii1iI1i1 ( ooo , Ii1II1I11i1 , 1007 , oooiiI )
def oooOOoo0 ( url ) :
 OO0O00oOo = ii1II ( url )
 Ii1i = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( OO0O00oOo )
 for url , oooiiI , ooo in Ii1i :
  II1Ii1iI1i1 ( '[COLORgreen]' + ooo + '[/COLOR]' , url , 1006 , oooiiI )
  if 79 - 79: ii - O0OoO * Ii11Ii1I - IIiIiII11i % OOooOOo * OooO0OoOOOO
def iI1III ( name , url , iconimage = None ) :
 print '--- Playing "{0}". {1}' . format ( name , url )
 I1I111 = xbmcgui . ListItem ( path = url , thumbnailImage = iconimage )
 I1I111 . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , I1I111 )
 if 2 - 2: iI1iI1I1i1I / I1ii11iIi11i / Ii11Ii1I / Ii1I / ii
 if 22 - 22: iI11I1II1I1I * oOo0O0Ooo / iI1iI1I1i1I + OOooOOo
def o00OoOOoO ( url ) :
 OO0O00oOo = ii1II ( url )
 Ii1i = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( OO0O00oOo )
 for url , I1II1I11I1I , ooo in Ii1i :
  if '-dir-' in ooo :
   II1Ii1iI1i1 ( ( '[COLORgreen]' + ooo + '[/COLOR]' ) . replace ( '-dir-' , '' ) , url , 1012 , I1II1I11I1I )
  else :
   II1Ii1iI1i1 ( '[COLORgreen]' + ooo + '[/COLOR]' , url , 1006 , I1II1I11I1I )
   if 28 - 28: iI11I1II1I1I * iI1iI1I1i1I . oOo0O0Ooo
def oooiI1i ( url ) :
 OO0O00oOo = ii1II ( url )
 iiiO0ooO0O0Ooo0o = ( 'http://afewbitsmore.com/' )
 Ii1i = re . compile ( '<A HREF="(.+?)">(.+?)</A><br>' , re . DOTALL ) . findall ( OO0O00oOo )
 for url , ooo in Ii1i :
  if '[To Parent Directory]' in ooo :
   ooo = 'HOME'
   pass
  elif 'HOME' in ooo :
   pass
  elif '.m3u' in ooo :
   II1Ii1iI1i1 ( '[COLORgreen]PLAY ALL[/COLOR]' , iiiO0ooO0O0Ooo0o + url , 2002 , ooOooo000oOO + 'music.png' )
  elif '.mp3' in ooo :
   oOO0oo ( ( '[COLORgreen]' + ooo + '[/COLOR]' ) . replace ( '.mp3' , '' ) . replace ( 'amp;' , '' ) , iiiO0ooO0O0Ooo0o + url , 222 , ooOooo000oOO + 'music.png' )
  elif '.m4a' in ooo :
   oOO0oo ( ( '[COLORgreen]' + ooo + '[/COLOR]' ) . replace ( '.m4a' , '' ) . replace ( 'amp;' , '' ) , iiiO0ooO0O0Ooo0o + url , 222 , ooOooo000oOO + 'music.png' )
  else :
   II1Ii1iI1i1 ( ( '[COLORgreen]' + ooo + '[/COLOR]' ) , iiiO0ooO0O0Ooo0o + url , 1012 , ooOooo000oOO + 'music.png' )
def o0Ii11I1iIIi ( url ) :
 o00OO00OoO = ii1II ( url )
 Ii1i = re . compile ( 'EXTINF:(.+?),(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( o00OO00OoO )
 for I1II1I11I1I , ooo , url in Ii1i :
  oOO0oo ( ( '[COLORgreen]' + ooo + '[/COLOR]' ) . replace ( '_' , ' ' ) , url , 10012 , ooOooo000oOO + 'music.png' )
  if 68 - 68: iI1iI1I1i1I / iI11I1II1I1I . I1ii11iIi11i + Ii + I11i
def OOI1III1I11I1 ( url ) :
 OO0O00oOo = ii1II ( url )
 iiiO0ooO0O0Ooo0o = url
 Ii1i = re . compile ( "<a href='(.+?)'>(.+?)</a>" ) . findall ( OO0O00oOo )
 for url , ooo in Ii1i :
  if '.mp3' in ooo :
   print '<<<<<<<<<<<<<<<<<<<' + url + '>>>>>>>>>>>>>>>>>>>>>>>>>>>'
   oOO0oo ( ( ooo ) . replace ( '.mp3' , '' ) . replace ( '/' , '' ) , 'http://hypem.com' + url , 222 , ooOooo000oOO + 'music.png' )
  else :
   II1Ii1iI1i1 ( ( ooo ) . replace ( '/' , '' ) , iiiO0ooO0O0Ooo0o + url , 1011 , ooOooo000oOO + 'music.png' )
def oO000OoO00OoO ( ) :
 OO0O00oOo = ii1II ( i1111 ( 'aHR0cDovL3d3dy5jeW4ubmV0L211c2ljLw==' ) )
 Ii1i = re . compile ( '<td><a href="(.+?)"><img src="(.+?)"><br>(.+?)</a></td>' , re . DOTALL ) . findall ( OO0O00oOo )
 for Ii1II1I11i1 , I1II1I11I1I , ooo in Ii1i :
  II1Ii1iI1i1 ( ooo , ( 'http://www.cyn.net/music/' + Ii1II1I11i1 ) . replace ( ' ' , '%20' ) , 1031 , ( 'http://www.cyn.net/music/' + I1II1I11I1I ) . replace ( ' ' , '%20' ) )
def I1IiIi1iiI ( url , img ) :
 OO0O00oOo = ii1II ( url )
 ooo0O0o00O = url
 img = img
 Ii1i = re . compile ( '<a href="(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( OO0O00oOo )
 for url , ooo in Ii1i :
  oOO0oo ( ( ooo ) . replace ( '.mp3' , '' ) , ( ooo0O0o00O + '/' + url ) . replace ( ' ' , '%20' ) , 222 , img )
  if 26 - 26: oOo0O0Ooo % OOooOOo
def OO00o0oo ( url ) :
 OO0O00oOo = ii1II ( url )
 ooo0O0o00O = url
 Ii1i = re . compile ( 'alt="(.+?)"></td><td><a href="(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( OO0O00oOo )
 for type , url , ooo in Ii1i :
  if '[VID]' in type :
   oOO0oo ( ( ooo ) . replace ( '.mp4' , '' ) . replace ( '_H.264-AAC' , '' ) . replace ( '(' , ' (' ) . replace ( ')' , ') ' ) , ooo0O0o00O + url , 222 , ooOooo000oOO + 'music.png' )
  if '[DIR]' in type :
   OO00o0oo ( ooo0O0o00O + url )
 xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 3 - 3: Ii11Ii1I * O0OoO - oOo0O0Ooo / ooOoO0O00
 if 21 - 21: IIiIiII11i + IIIi
def i1Io00OOOo ( ) :
 oo0oOO = ( i1111 ( 'aHR0cDovL2h5cGVtLmNvbS9kb3dubG9hZC8=' ) )
 IIiI1i1i = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 IiII111i1i11 = IIiI1i1i . lower ( )
 Ii1II1I11i1 = ( i1111 ( 'aHR0cDovL3Bhbmljc3RyZWFtLm5ldC9zdHJlYW1zLw==' ) )
 ooo0O0o00O = ( i1111 ( 'aHR0cDovL21hc2xvdmQubm8taXAub3JnL3B1YmxpYy9tcDMv' ) )
 IiIi1I1 = ( i1111 ( 'aHR0cDovL3d3dy5jeW4ubmV0L211c2ljLw==' ) )
 if 39 - 39: ii . iI1iI1I1i1I * Ii11Ii1I . OOooOOo . OoOo00o
 o00OO00OoO = O000OO0 ( Ii1II1I11i1 )
 OOOO0OOoO0O0 = O000OO0 ( ooo0O0o00O )
 O0Oo000ooO00 = O000OO0 ( IiIi1I1 )
 if 75 - 75: O0OoO / Ii11Ii1I
 if o00OO00OoO != 'Failed' :
  Ii1i = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( o00OO00OoO )
  for ooo in Ii1i :
   if IIiI1i1i in ooo . lower ( ) :
    II1Ii1iI1i1 ( ( ooo + ' source 1' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( Ii1II1I11i1 + ooo ) . replace ( ' ' , '%20' ) , 1006 , '' )
    if 36 - 36: OOooOOo . Ii
    iiO0o0oOOOoOo ( 'tvshows' , 'Media Info 3' )
 if OOOO0OOoO0O0 != 'Failed' :
  I1 = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( o00OO00OoO )
  for ooo in I1 :
   if IIiI1i1i in ooo . lower ( ) :
    II1Ii1iI1i1 ( ( ooo + ' source 2' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( ooo0O0o00O + ooo ) . replace ( ' ' , '%20' ) , 1006 , '' )
    if 81 - 81: I1ii11iIi11i * o0oOO0O00o0O * oO0o
    iiO0o0oOOOoOo ( 'tvshows' , 'Media Info 3' )
 if O0Oo000ooO00 != 'Failed' :
  II1Ii = re . compile ( '<td><a href=".+?"><img src=".+?"><br>(.+?)</a></td>' , re . DOTALL ) . findall ( O0Oo000ooO00 )
  for ooo in II1Ii :
   if IIiI1i1i in ooo . lower ( ) :
    II1Ii1iI1i1 ( ( ooo + ' source 3' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( IiIi1I1 + ooo ) . replace ( ' ' , '%20' ) , 1031 , '' )
    if 85 - 85: o0o00Oo0O * OoOo00o
    iiO0o0oOOOoOo ( 'tvshows' , 'Media Info 3' )
    if 39 - 39: IIiIiII11i * oOo0O0Ooo - iI11I1II1I1I
    if 25 - 25: ii . Ii11Ii1I % o0oOO0O00o0O . OooO0OoOOOO
    if 67 - 67: ii + IIIi / O0OoO
    if 75 - 75: OooO0OoOOOO / ii . oOo0O0Ooo + IIIi - IIiIiII11i
    if 33 - 33: OooO0OoOOOO / OooO0OoOOOO . Ii * Ii1I + I11i
    if 16 - 16: OooO0OoOOOO
OO0OooOOoO00OO00 = '{SF},' ; ii11ii1iIiI1 = '{IF},' ; OoOo0oO0 = '{PW},' ; iiIII1i1 = '{AM},' ; i111iIi1i1 = '{GF},' ; OOo00O0O = '{DD},' ; oooOoO = '{UO},' ; OO0oooOO = '{LE},' ; IIIi1iiIIiiiI = '{ZY},' ; I1IIiIi1iI = '{UE},' ; oOo0Iiii11 = '{PE},' ; o00000O = '{JE},' ; ooo00Oo0 = '{TH},' ; iIii1i1Ii = '{LK},'
if 10 - 10: OOooOOo . OooO0OoOOOO * iI11I1II1I1I - OoOo00o - OOooOOo / IIIi
if 13 - 13: OoOo00o + OOooOOo % OooO0OoOOOO % ii
def iiiiI1iiiIi11 ( ) :
 OO0O00oOo = iiI111I1iIiI ( 'http://www.iwatchseries.me/tv-list/' )
 Ii1i = re . compile ( '<h5><a href="([^"]*)"><strong>(.+?)</strong></a></h5>' ) . findall ( OO0O00oOo )
 for Ii1II1I11i1 , ooo in Ii1i :
  II1Ii1iI1i1 ( ooo , Ii1II1I11i1 , 8021 , ooOooo000oOO + 'iwatch.png' )
def O0oOOO0o0Ooo ( url ) :
 OO0O00oOo = iiI111I1iIiI ( url )
 Ii1i = re . compile ( '<h5><strong><a href="([^"]*)">(.+?)</a>(.+?)</strong></h5>' ) . findall ( OO0O00oOo )
 for url , ooo , I11o0oO00oO0o0o0 in Ii1i :
  II1Ii1iI1i1 ( ooo + I11o0oO00oO0o0o0 , url , 8022 , ooOooo000oOO + 'iwatch.png' )
def i1iIII1IIi ( url ) :
 OO0O00oOo = iiI111I1iIiI ( url )
 Ii1i = re . compile ( '<iframe src="([^"]*)"' ) . findall ( OO0O00oOo )
 for url in Ii1i :
  print '>>>>>>>>>>>>>>>>>>>>' + url
  Oo0oo0OOO0OOoOO ( url )
def Oo0oo0OOO0OOoOO ( url ) :
 OO0O00oOo = iiI111I1iIiI ( url )
 Ii1i = re . compile ( '{.+?"file" : "(.+?)",.+?"default" : true.+?"label" : "(.+?)"' , re . DOTALL ) . findall ( OO0O00oOo )
 I1 = re . compile ( 'setup\(\{.+?file: "(.+?)",.+?skin' , re . DOTALL ) . findall ( OO0O00oOo )
 II1Ii = re . compile ( "{ label: '([^']*)', file:.+?'([^']*)' }" ) . findall ( OO0O00oOo )
 for url , ooo in Ii1i :
  oOO0oo ( 'VidSpot - ' + ooo , url , 222 , ooOooo000oOO + 'iwatch.png' )
 for url in I1 :
  oOO0oo ( 'VodLocker' , url , 222 , ooOooo000oOO + 'iwatch.png' )
 for ooo , url in II1Ii :
  print '<><><><><><><><><><><> before   ' + url
  if 'hevideo' in url :
   print '>>>>>>>>>>>>>>>>>>>>>>>>>' + url
   oOO0oo ( 'TheVideo - ' + ooo , url , 222 , ooOooo000oOO + 'iwatch.png' )
   if 97 - 97: ooOoO0O00
def ii1iI1i1 ( ) :
 OO0O00oOo = cloudflare . source ( 'http://www.animeland.me/anime-list' )
 Ii1i = re . compile ( 'letter-spacing:-1px;" href="([^"]*)">(.+?)</a></li>' ) . findall ( OO0O00oOo )
 for Ii1II1I11i1 , ooo in Ii1i :
  II1Ii1iI1i1 ( ooo , Ii1II1I11i1 , 1021 , ooOooo000oOO + 'anime.png' )
  if 51 - 51: O0OoO * o0oOO0O00o0O / ooOoO0O00
  if 2 - 2: OoOo00o + OooO0OoOOOO . o0oOO0O00o0O - ooOoO0O00 + IIIi
def ooOOo0O0o00o00 ( ) :
 OO0O00oOo = iiI111I1iIiI ( 'http://www.animetoon.org/cartoon' )
 Ii1i = re . compile ( '<td><a href="(.+?)">(.+)</a></td>' ) . findall ( OO0O00oOo )
 for Ii1II1I11i1 , ooo in Ii1i :
  II1Ii1iI1i1 ( ooo , Ii1II1I11i1 , 1002 , ooOooo000oOO + 'anime.png' )
  if 90 - 90: IIIi . IIiIiII11i . Ii1I
  if 32 - 32: O0OoO - oO0o . o0oOO0O00o0O . o0oOO0O00o0O % ooOoO0O00 * Ii11Ii1I
  if 65 - 65: o0oOO0O00o0O / O0OoO . IIiIiII11i
def o0oO00oooo ( url ) :
 OO0O00oOo = iiI111I1iIiI ( url )
 I1 = re . compile ( '<img src="(.+?)" id="series_image" width="250" height="370" alt=".+?" />' ) . findall ( OO0O00oOo )
 for I1II1I11I1I in I1 :
  Oo0O0O000 = I1II1I11I1I
 II1Ii = re . compile ( '<li><a href="(.+?)">Next</a></li>' ) . findall ( OO0O00oOo )
 for url in II1Ii :
  II1Ii1iI1i1 ( 'NEXT PAGE' , url , 1002 , ooOooo000oOO + 'Next.png' )
 Ii1i = re . compile ( '&nbsp;<a href="(.+?)">(.+?)</a>' ) . findall ( OO0O00oOo )
 for url , ooo in Ii1i :
  II1Ii1iI1i1 ( ooo , url , 1003 , Oo0O0O000 )
 xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
def ooo0Oo00O ( url , IMAGE ) :
 OO0O00oOo = iiI111I1iIiI ( url )
 Ii1i = re . compile ( '"playlist">(.+?)</span></div><div><iframe src="(.+?)"' ) . findall ( OO0O00oOo )
 for ooo , url in Ii1i :
  print ooo + '     ' + url
  if 'easy' in url :
   I1iII1 ( url )
  elif 'playpanda' in url :
   I1iII1 ( url )
   if 70 - 70: ooOoO0O00 % O0OoO . Ii1I - OooO0OoOOOO + IIIii1II1II
  xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
def I1iII1 ( url ) :
 OO0O00oOo = iiI111I1iIiI ( url )
 Ii1i = re . compile ( "url: '(.+?)'," ) . findall ( OO0O00oOo )
 for url in Ii1i :
  oOO0oo ( 'STREAM' , url , 222 , ooOooo000oOO + 'anime.png' )
  if 84 - 84: OoOo00o + IIiIiII11i * IIiIiII11i % I11i / o0oOO0O00o0O + O0OoO
  if 9 - 9: o0oOO0O00o0O
def iIi11I1II ( url ) :
 I11iii1Ii = urllib2 . Request ( url )
 I11iii1Ii . add_header ( 'User-Agent' , "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0" )
 I11iii1Ii . add_header ( 'referer' , url )
 I1IIiiIiii = urllib2 . urlopen ( I11iii1Ii )
 O000oo0O = I1IIiiIiii . read ( )
 I1IIiiIiii . close ( )
 return O000oo0O
 if 93 - 93: Ii1I - O0OoO % Ii1I
def ii1II ( url ) :
 I11iii1Ii = urllib2 . Request ( url )
 I11iii1Ii . add_header ( 'User-Agent' , "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0" )
 I1IIiiIiii = urllib2 . urlopen ( I11iii1Ii )
 O000oo0O = I1IIiiIiii . read ( )
 I1IIiiIiii . close ( )
 return O000oo0O
 if 12 - 12: IIIii1II1II + oO0o * iI1iI1I1i1I + Ii11Ii1I + OooO0OoOOOO
def O0O00oOo0o000 ( url ) :
 xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
 oOOooooo0OoO0 = ( '%s%s' % ( ii1I111i1Ii , url ) )
 O000oo0O = ii1II ( url )
 Ii1i = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( O000oo0O )
 for url , oooiiI , ooo in Ii1i :
  oOO0oo ( '%s' % ( ooo ) . replace ( 'GenieTv' , '[COLOR green]GenieTV[/COLOR]' ) . replace ( '.' , ' ' ) . replace ( 'mp4' , '' ) . replace ( 'mkv' , '' ) . replace ( '_' , ' ' ) , '%s' % ( url ) , 222 , oooiiI )
  if 85 - 85: oOo0O0Ooo % O0OoO
def I1i11 ( url ) :
 I1i = xbmc . Player ( I1iii ( ) )
 import urlresolver
 try : I1i . play ( url )
 except : pass
 from urlresolver import common
 Oo0oO0ooo = xbmcgui . DialogProgress ( )
 Oo0oO0ooo . create ( 'LOADING' , 'Opening %s Now' % ( ooo ) )
 I1i = xbmc . Player ( I1iii ( ) )
 url = urlresolver . HostedMediaFile ( url ) . resolve ( )
 if Oo0oO0ooo . iscanceled ( ) :
  print "[COLORred]STREAM CANCELLED[/COLOR]"
  i1iiIIiiI111 = xbmcgui . Dialog ( )
  if i1iiIIiiI111 . yesno ( "[B]CANCELLED[/B]" , '[B]Was There A Problem[/B]' , '' , "" , 'Yes' , 'No' ) :
   i1iiIIiiI111 . ok ( "Message Send" , "Your Message Has Been Sent" )
  else :
   return
 else :
  try : I1i . play ( url )
  except : pass
  try : o0oO0 . resolve_url ( url )
  except : pass
  Oo0oO0ooo . close ( )
  if 25 - 25: OOooOOo . IIiIiII11i * Ii11Ii1I
def IiII111I ( url ) :
 Oo0oO0ooo = xbmcgui . DialogProgress ( )
 Oo0oO0ooo . create ( 'Featching Your Video' , 'Featching Your Video' )
 Oo0oO0ooo . update ( 0 , '%s' % ooo )
 xbmc . sleep ( 1 )
 I1i = xbmc . Player ( I1iii ( ) )
 Oo0oO0ooo . update ( 100 , '%s' % ooo )
 xbmc . sleep ( 1 )
 I1i . play ( url ) . strip ( )
 Oo0oO0ooo . close ( )
 if 62 - 62: ooOoO0O00 * iI11I1II1I1I % OoOo00o % OOooOOo / ii
def i1iii11 ( url ) :
 I1i = xbmc . Player ( I1iii ( ) )
 import urlresolver
 url = ( url ) . strip ( )
 try : I1i . play ( url ) . strip ( )
 except : pass
 if 39 - 39: I1ii11iIi11i % o0oOO0O00o0O
 if 90 - 90: oOo0O0Ooo * Ii1I . iI1iI1I1i1I * Ii11Ii1I - I11i
def I1iii ( ) :
 try :
  IiI1 = getSet ( "core-player" )
  if ( IiI1 == 'DVDPLAYER' ) : iII1i111iI = xbmc . PLAYER_CORE_DVDPLAYER
  elif ( IiI1 == 'MPLAYER' ) : iII1i111iI = xbmc . PLAYER_CORE_MPLAYER
  elif ( IiI1 == 'PAPLAYER' ) : iII1i111iI = xbmc . PLAYER_CORE_PAPLAYER
  else : iII1i111iI = xbmc . PLAYER_CORE_AUTO
 except : iII1i111iI = xbmc . PLAYER_CORE_AUTO
 return iII1i111iI
 return True
 if 9 - 9: Ii + IIIii1II1II - OOooOOo / O0OoO % ooOoO0O00 / OoOo00o
def II1Ii1iI1i1 ( name , url , mode , iconimage , showcontext = True , allinfo = { } ) :
 i1I1II = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 Ii1I1I1i11ii = True
 OoOo0oO0o = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 OoOo0oO0o . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 if showcontext :
  iiI1 = [ ]
  if showcontext == 'fav' :
   iiI1 . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in OOO00 :
   iiI1 . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  OoOo0oO0o . addContextMenuItems ( iiI1 )
 Ii1I1I1i11ii = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = i1I1II , listitem = OoOo0oO0o , isFolder = True )
 return Ii1I1I1i11ii
 if 42 - 42: oO0o - Ii1I * OooO0OoOOOO - O0OoO
def ii1iI1iI1 ( name , url , mode , iconimage , fanart , description ) :
 if 75 - 75: o0oOO0O00o0O * I1ii11iIi11i / IIIi * I1ii11iIi11i / O0OoO
 i1I1II = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 Ii1I1I1i11ii = True
 OoOo0oO0o = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 OoOo0oO0o . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 OoOo0oO0o . setProperty ( "Fanart_Image" , fanart )
 Ii1I1I1i11ii = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = i1I1II , listitem = OoOo0oO0o , isFolder = True )
 return Ii1I1I1i11ii
 if 14 - 14: ooOoO0O00 * iI11I1II1I1I - Ii11Ii1I * OOooOOo - o0oOO0O00o0O / OoOo00o
def oOO0oo ( name , url , mode , iconimage , showcontext = True , allinfo = { } ) :
 i1I1II = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 Ii1I1I1i11ii = True
 OoOo0oO0o = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 OoOo0oO0o . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 if showcontext :
  iiI1 = [ ]
  if showcontext == 'fav' :
   iiI1 . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in OOO00 :
   iiI1 . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  OoOo0oO0o . addContextMenuItems ( iiI1 )
 Ii1I1I1i11ii = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = i1I1II , listitem = OoOo0oO0o , isFolder = False )
 return Ii1I1I1i11ii
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
   try : ooOO0oO0oo00o = open ( announce ) ; IIiiIIi1 = ooOO0oO0oo00o . read ( )
   except : IIiiIIi1 = announce
   self . win . getControl ( self . CONTROL_TEXTBOX ) . setText ( str ( IIiiIIi1 ) )
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
def oooooo0O000o ( ) :
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
 for ooo , url , iI1IOooOoOo , III1I1Iii1iiI , I1o0OooOOOOOO in Ii1i :
  II1I ( ooo , url , 42 , iI1IOooOoOo , III1I1Iii1iiI , I1o0OooOOOOOO )
 iiO0o0oOOOoOo ( 'movies' , 'MAIN' )
 if 62 - 62: I1ii11iIi11i * iI11I1II1I1I
def iI11ii ( url ) :
 O000oo0O = iiI111I1iIiI ( str ( Ii1iIiII1ii1 ) + OOOoOO00OO0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 Ii1i = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( O000oo0O )
 for ooo , url , iI1IOooOoOo , III1I1Iii1iiI , I1o0OooOOOOOO in Ii1i :
  II1I ( ooo , url , 42 , iI1IOooOoOo , III1I1Iii1iiI , I1o0OooOOOOOO )
 iiO0o0oOOOoOo ( 'movies' , 'MAIN' )
 if 46 - 46: I11i . iI11I1II1I1I + ii - O0OoO * I1ii11iIi11i * Ii
def o0OoO0O ( url ) :
 O000oo0O = iiI111I1iIiI ( str ( Ii1iIiII1ii1 ) + o0OOOoO ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 Ii1i = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( O000oo0O )
 for ooo , url , iI1IOooOoOo , III1I1Iii1iiI , I1o0OooOOOOOO in Ii1i :
  II1I ( ooo , url , 42 , iI1IOooOoOo , III1I1Iii1iiI , I1o0OooOOOOOO )
 iiO0o0oOOOoOo ( 'movies' , 'MAIN' )
 if 73 - 73: ii / ii
def O0O0OOooo ( url ) :
 O000oo0O = iiI111I1iIiI ( str ( Ii1iIiII1ii1 ) + o0OooOoOOoO ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 Ii1i = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( O000oo0O )
 for ooo , url , iI1IOooOoOo , III1I1Iii1iiI , I1o0OooOOOOOO in Ii1i :
  II1I ( ooo , url , 42 , iI1IOooOoOo , III1I1Iii1iiI , I1o0OooOOOOOO )
 iiO0o0oOOOoOo ( 'movies' , 'MAIN' )
 if 70 - 70: IIiIiII11i % Ii1I % ii
def III1I1I11 ( url ) :
 O000oo0O = iiI111I1iIiI ( str ( Ii1iIiII1ii1 ) + Oo0I1iii ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 Ii1i = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( O000oo0O )
 for ooo , url , iI1IOooOoOo , III1I1Iii1iiI , I1o0OooOOOOOO in Ii1i :
  II1I ( ooo , url , 42 , iI1IOooOoOo , III1I1Iii1iiI , I1o0OooOOOOOO )
 iiO0o0oOOOoOo ( 'movies' , 'MAIN' )
 if 85 - 85: Ii1I * OOooOOo % iI1iI1I1i1I
def i1iIIIiI ( url ) :
 O000oo0O = iiI111I1iIiI ( str ( Ii1iIiII1ii1 ) + I11IiI1iII ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 Ii1i = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( O000oo0O )
 for ooo , url , iI1IOooOoOo , III1I1Iii1iiI , I1o0OooOOOOOO in Ii1i :
  II1I ( ooo , url , 42 , iI1IOooOoOo , III1I1Iii1iiI , I1o0OooOOOOOO )
 iiO0o0oOOOoOo ( 'movies' , 'MAIN' )
 if 18 - 18: IIIii1II1II
def Oo000O000 ( url ) :
 O000oo0O = iiI111I1iIiI ( str ( Ii1iIiII1ii1 ) + iIi11 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 Ii1i = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( O000oo0O )
 for ooo , url , iI1IOooOoOo , III1I1Iii1iiI , I1o0OooOOOOOO in Ii1i :
  II1I ( ooo , url , 42 , iI1IOooOoOo , III1I1Iii1iiI , I1o0OooOOOOOO )
 iiO0o0oOOOoOo ( 'movies' , 'MAIN' )
 if 67 - 67: iI1iI1I1i1I / o0o00Oo0O * Ii11Ii1I - OooO0OoOOOO . ii + OooO0OoOOOO
def i1I1iiiI ( url ) :
 O000oo0O = iiI111I1iIiI ( str ( Ii1iIiII1ii1 ) + i1IiIi1I1i ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 Ii1i = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( O000oo0O )
 for ooo , url , iI1IOooOoOo , III1I1Iii1iiI , I1o0OooOOOOOO in Ii1i :
  II1I ( ooo , url , 42 , iI1IOooOoOo , III1I1Iii1iiI , I1o0OooOOOOOO )
 iiO0o0oOOOoOo ( 'movies' , 'MAIN' )
 if 39 - 39: Ii + IIIii1II1II % o0oOO0O00o0O + Ii11Ii1I * oOo0O0Ooo + IIIi
def Oo00oOo ( url ) :
 O000oo0O = iiI111I1iIiI ( str ( Ii1iIiII1ii1 ) + o0ooOo000oo ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 Ii1i = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( O000oo0O )
 for ooo , url , iI1IOooOoOo , III1I1Iii1iiI , I1o0OooOOOOOO in Ii1i :
  II1I ( ooo , url , 42 , iI1IOooOoOo , III1I1Iii1iiI , I1o0OooOOOOOO )
 iiO0o0oOOOoOo ( 'movies' , 'MAIN' )
 if 81 - 81: ii - OooO0OoOOOO - OooO0OoOOOO + iI11I1II1I1I % iI1iI1I1i1I . ii
def o0o ( url ) :
 O000oo0O = iiI111I1iIiI ( str ( Ii1iIiII1ii1 ) + ooIi1Iii1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 Ii1i = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( O000oo0O )
 for ooo , url , iI1IOooOoOo , III1I1Iii1iiI , I1o0OooOOOOOO in Ii1i :
  II1I ( ooo , url , 5 , iI1IOooOoOo , III1I1Iii1iiI , I1o0OooOOOOOO )
 iiO0o0oOOOoOo ( 'movies' , 'MAIN' )
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
    for IiiIi , IiI11i1IIiiI , oOOo000oOoO0 in os . walk ( iIii1 ) :
     IiIi = 0
     IiIi += len ( oOOo000oOoO0 )
     if IiIi > 0 :
      for ooOO0oO0oo00o in oOOo000oOoO0 :
       os . unlink ( os . path . join ( IiiIi , ooOO0oO0oo00o ) )
  ii1IiI = os . path . join ( iI111I11I1I1 , "Textures13.db" )
  os . unlink ( ii1IiI )
  i1iiIIiiI111 . ok ( "Restart KODI" , "Please restart KODI to rebuild thumbnail library" )
 except :
  i1iiIIiiI111 = xbmcgui . Dialog ( )
  i1iiIIiiI111 . ok ( o0oOoO00o , "Error Deleting Thumbnails please visit The Support Group, GenieTv on facebook" )
 return
 if 73 - 73: ii * o0o00Oo0O * O0OoO
 if 7 - 7: IIiIiII11i + ooOoO0O00
 if 95 - 95: Ii + ii / IIIii1II1II - iI11I1II1I1I + iI11I1II1I1I
 if 29 - 29: OooO0OoOOOO % O0OoO + oO0o . ooOoO0O00 + oOo0O0Ooo
 if 24 - 24: IIIi / Ii11Ii1I * Ii1I - ii / oOo0O0Ooo . OoOo00o
 if 98 - 98: ooOoO0O00 - o0oOO0O00o0O
 if 49 - 49: I11i . Ii11Ii1I . OoOo00o
 if 9 - 9: OooO0OoOOOO - IIiIiII11i * oO0o
 if 78 - 78: iI11I1II1I1I / o0o00Oo0O * OoOo00o / o0oOO0O00o0O / OOooOOo
def i1II1 ( url ) :
 print '############################################################       DELETING STANDARD CACHE             ###############################################################'
 Oo00o0o0O = os . path . join ( xbmc . translatePath ( 'special://home' ) , 'cache' )
 if os . path . exists ( Oo00o0o0O ) == True :
  for IiiIi , IiI11i1IIiiI , oOOo000oOoO0 in os . walk ( Oo00o0o0O ) :
   IiIi = 0
   IiIi += len ( oOOo000oOoO0 )
   if 82 - 82: IIiIiII11i
   if 15 - 15: IIIii1II1II
   if IiIi > 0 :
    if 77 - 77: OOooOOo
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    if i1iiIIiiI111 . yesno ( "Delete KODI Cache Files" , str ( IiIi ) + " files found" , "Do you want to delete them?" ) :
     if 91 - 91: OoOo00o
     for ooOO0oO0oo00o in oOOo000oOoO0 :
      try :
       os . unlink ( os . path . join ( IiiIi , ooOO0oO0oo00o ) )
      except :
       pass
     for ii1IIIIiI11 in IiI11i1IIiiI :
      try :
       shutil . rmtree ( os . path . join ( IiiIi , ii1IIIIiI11 ) )
      except :
       pass
       if 56 - 56: iI11I1II1I1I % IIiIiII11i / OOooOOo % ii
   else :
    pass
 if xbmc . getCondVisibility ( 'system.platform.ATV2' ) :
  I1IiIIIIi1iiI = os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'Other' )
  if 57 - 57: iI1iI1I1i1I . o0o00Oo0O . ii . IIIi - Ii11Ii1I / O0OoO
  for IiiIi , IiI11i1IIiiI , oOOo000oOoO0 in os . walk ( I1IiIIIIi1iiI ) :
   IiIi = 0
   IiIi += len ( oOOo000oOoO0 )
   if 34 - 34: OOooOOo % I11i - OoOo00o
   if IiIi > 0 :
    if 40 - 40: o0oOO0O00o0O
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    if i1iiIIiiI111 . yesno ( "Delete ATV2 Cache Files" , str ( IiIi ) + " files found in 'Other'" , "Do you want to delete them?" ) :
     if 82 - 82: IIIi . ooOoO0O00 / OoOo00o
     for ooOO0oO0oo00o in oOOo000oOoO0 :
      os . unlink ( os . path . join ( IiiIi , ooOO0oO0oo00o ) )
     for ii1IIIIiI11 in IiI11i1IIiiI :
      shutil . rmtree ( os . path . join ( IiiIi , ii1IIIIiI11 ) )
      if 56 - 56: o0oOO0O00o0O
   else :
    pass
  iii1o0o0O00OoOo = os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'LocalAndRental' )
  if 59 - 59: iI1iI1I1i1I
  for IiiIi , IiI11i1IIiiI , oOOo000oOoO0 in os . walk ( iii1o0o0O00OoOo ) :
   IiIi = 0
   IiIi += len ( oOOo000oOoO0 )
   if 59 - 59: ii * I11i / IIIi
   if IiIi > 0 :
    if 75 - 75: I11i - ii
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    if i1iiIIiiI111 . yesno ( "Delete ATV2 Cache Files" , str ( IiIi ) + " files found in 'LocalAndRental'" , "Do you want to delete them?" ) :
     if 21 - 21: oOo0O0Ooo + iI11I1II1I1I / Ii / OoOo00o
     for ooOO0oO0oo00o in oOOo000oOoO0 :
      os . unlink ( os . path . join ( IiiIi , ooOO0oO0oo00o ) )
     for ii1IIIIiI11 in IiI11i1IIiiI :
      shutil . rmtree ( os . path . join ( IiiIi , ii1IIIIiI11 ) )
      if 66 - 66: ii + o0oOO0O00o0O . OooO0OoOOOO % ooOoO0O00
   else :
    pass
    if 58 - 58: IIIii1II1II % o0oOO0O00o0O * o0o00Oo0O + Ii1I - OooO0OoOOOO
    if 26 - 26: ooOoO0O00 / oOo0O0Ooo / iI1iI1I1i1I + iI1iI1I1i1I
    if 46 - 46: IIIi % Ii1I + Ii11Ii1I
    if 67 - 67: iI11I1II1I1I . Ii . Ii . Ii / iI1iI1I1i1I + O0OoO
 i11IiIiii = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.whatthefurk/cache' ) , '' )
 if os . path . exists ( i11IiIiii ) == True :
  for IiiIi , IiI11i1IIiiI , oOOo000oOoO0 in os . walk ( i11IiIiii ) :
   IiIi = 0
   IiIi += len ( oOOo000oOoO0 )
   if 15 - 15: O0OoO * iI11I1II1I1I * OoOo00o
   if 96 - 96: IIIi * iI11I1II1I1I / OOooOOo % IIIii1II1II * IIiIiII11i
   if IiIi > 0 :
    if 3 - 3: IIIii1II1II . I1ii11iIi11i / Ii + oO0o
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    if i1iiIIiiI111 . yesno ( "Delete WTF Cache Files" , str ( IiIi ) + " files found" , "Do you want to delete them?" ) :
     if 47 - 47: OooO0OoOOOO . IIIii1II1II
     for ooOO0oO0oo00o in oOOo000oOoO0 :
      os . unlink ( os . path . join ( IiiIi , ooOO0oO0oo00o ) )
     for ii1IIIIiI11 in IiI11i1IIiiI :
      shutil . rmtree ( os . path . join ( IiiIi , ii1IIIIiI11 ) )
      if 96 - 96: iI1iI1I1i1I % IIiIiII11i / O0OoO % IIIii1II1II / O0OoO % Ii
   else :
    pass
    if 57 - 57: iI1iI1I1i1I - iI1iI1I1i1I % IIiIiII11i % I1ii11iIi11i . I11i % I1ii11iIi11i
    if 91 - 91: oOo0O0Ooo - oO0o - I1ii11iIi11i - Ii11Ii1I * iI11I1II1I1I
 OO0ooo0OOO = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.4od/cache' ) , '' )
 if os . path . exists ( OO0ooo0OOO ) == True :
  for IiiIi , IiI11i1IIiiI , oOOo000oOoO0 in os . walk ( OO0ooo0OOO ) :
   IiIi = 0
   IiIi += len ( oOOo000oOoO0 )
   if 69 - 69: IIIi + iI11I1II1I1I * OoOo00o + OooO0OoOOOO % O0OoO - Ii11Ii1I
   if 83 - 83: OooO0OoOOOO % I11i * I11i
   if IiIi > 0 :
    if 58 - 58: IIIi - iI1iI1I1i1I
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    if i1iiIIiiI111 . yesno ( "Delete 4oD Cache Files" , str ( IiIi ) + " files found" , "Do you want to delete them?" ) :
     if 69 - 69: oOo0O0Ooo + I1ii11iIi11i * I11i * ooOoO0O00 % I1ii11iIi11i
     for ooOO0oO0oo00o in oOOo000oOoO0 :
      os . unlink ( os . path . join ( IiiIi , ooOO0oO0oo00o ) )
     for ii1IIIIiI11 in IiI11i1IIiiI :
      shutil . rmtree ( os . path . join ( IiiIi , ii1IIIIiI11 ) )
      if 41 - 41: OoOo00o . o0oOO0O00o0O + ii * Ii11Ii1I . I11i
   else :
    pass
    if 11 - 11: o0o00Oo0O
    if 96 - 96: o0oOO0O00o0O + I11i
 Iiiii1III1iIi = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.iplayer/iplayer_http_cache' ) , '' )
 if os . path . exists ( Iiiii1III1iIi ) == True :
  for IiiIi , IiI11i1IIiiI , oOOo000oOoO0 in os . walk ( Iiiii1III1iIi ) :
   IiIi = 0
   IiIi += len ( oOOo000oOoO0 )
   if 43 - 43: OoOo00o + OOooOOo . oOo0O0Ooo . Ii
   if 71 - 71: I11i + IIIii1II1II . I1ii11iIi11i - OOooOOo * Ii . OOooOOo
   if IiIi > 0 :
    if 91 - 91: o0o00Oo0O - iI1iI1I1i1I % IIIi
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    if i1iiIIiiI111 . yesno ( "Delete BBC iPlayer Cache Files" , str ( IiIi ) + " files found" , "Do you want to delete them?" ) :
     if 46 - 46: O0OoO / oOo0O0Ooo . OooO0OoOOOO % oO0o / Ii
     for ooOO0oO0oo00o in oOOo000oOoO0 :
      os . unlink ( os . path . join ( IiiIi , ooOO0oO0oo00o ) )
     for ii1IIIIiI11 in IiI11i1IIiiI :
      shutil . rmtree ( os . path . join ( IiiIi , ii1IIIIiI11 ) )
      if 13 - 13: IIIi % I11i + IIIii1II1II + IIIi + Ii - Ii1I
   else :
    pass
    if 70 - 70: IIiIiII11i * IIiIiII11i . oOo0O0Ooo
    if 11 - 11: o0oOO0O00o0O
    if 20 - 20: Ii11Ii1I . IIIi % Ii11Ii1I
 i11iI1 = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/script.module.simple.downloader' ) , '' )
 if os . path . exists ( i11iI1 ) == True :
  for IiiIi , IiI11i1IIiiI , oOOo000oOoO0 in os . walk ( i11iI1 ) :
   IiIi = 0
   IiIi += len ( oOOo000oOoO0 )
   if 92 - 92: iI11I1II1I1I
   if 75 - 75: oO0o - IIIii1II1II + I11i . OoOo00o % OOooOOo . IIiIiII11i
   if IiIi > 0 :
    if 56 - 56: IIiIiII11i . I1ii11iIi11i * oO0o
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    if i1iiIIiiI111 . yesno ( "Delete Simple Downloader Cache Files" , str ( IiIi ) + " files found" , "Do you want to delete them?" ) :
     if 92 - 92: iI11I1II1I1I * Ii1I . oO0o - I1ii11iIi11i * o0o00Oo0O / Ii11Ii1I
     for ooOO0oO0oo00o in oOOo000oOoO0 :
      os . unlink ( os . path . join ( IiiIi , ooOO0oO0oo00o ) )
     for ii1IIIIiI11 in IiI11i1IIiiI :
      shutil . rmtree ( os . path . join ( IiiIi , ii1IIIIiI11 ) )
      if 19 - 19: ooOoO0O00 - iI11I1II1I1I . iI1iI1I1i1I
   else :
    pass
    if 2 - 2: Ii11Ii1I
    if 12 - 12: Ii - iI11I1II1I1I * OooO0OoOOOO * o0oOO0O00o0O
 iiIII1iIiI1Ii11Iiii = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.itv/Images' ) , '' )
 if os . path . exists ( iiIII1iIiI1Ii11Iiii ) == True :
  for IiiIi , IiI11i1IIiiI , oOOo000oOoO0 in os . walk ( iiIII1iIiI1Ii11Iiii ) :
   IiIi = 0
   IiIi += len ( oOOo000oOoO0 )
   if 44 - 44: Ii % IIIi % OoOo00o + iI1iI1I1i1I * OoOo00o . Ii11Ii1I
   if 89 - 89: ii % IIiIiII11i - oO0o % Ii
   if IiIi > 0 :
    if 7 - 7: OooO0OoOOOO
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    if i1iiIIiiI111 . yesno ( "Delete ITV Cache Files" , str ( IiIi ) + " files found" , "Do you want to delete them?" ) :
     if 15 - 15: I1ii11iIi11i + o0oOO0O00o0O + oOo0O0Ooo * I11i
     for ooOO0oO0oo00o in oOOo000oOoO0 :
      os . unlink ( os . path . join ( IiiIi , ooOO0oO0oo00o ) )
     for ii1IIIIiI11 in IiI11i1IIiiI :
      shutil . rmtree ( os . path . join ( IiiIi , ii1IIIIiI11 ) )
      if 33 - 33: I11i * I1ii11iIi11i
   else :
    pass
    if 88 - 88: IIIi % IIIii1II1II - OOooOOo - OOooOOo . oOo0O0Ooo
    if 52 - 52: IIiIiII11i / IIiIiII11i / oOo0O0Ooo - IIIi
 Oo0OOo = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.movies4me/cache' ) , '' )
 if os . path . exists ( iiIII1iIiI1Ii11Iiii ) == True :
  for IiiIi , IiI11i1IIiiI , oOOo000oOoO0 in os . walk ( Oo0OOo ) :
   IiIi = 0
   IiIi += len ( oOOo000oOoO0 )
   if 43 - 43: OooO0OoOOOO % Ii11Ii1I . IIIii1II1II / I1ii11iIi11i
   if 55 - 55: Ii1I % ii
   if IiIi > 0 :
    if 73 - 73: ooOoO0O00 - o0oOO0O00o0O % OoOo00o / ooOoO0O00 + IIiIiII11i + Ii1I
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    if i1iiIIiiI111 . yesno ( "Delete Movies4me Cache Files" , str ( IiIi ) + " files found" , "Do you want to delete them?" ) :
     if 54 - 54: OoOo00o
     for ooOO0oO0oo00o in oOOo000oOoO0 :
      os . unlink ( os . path . join ( IiiIi , ooOO0oO0oo00o ) )
     for ii1IIIIiI11 in IiI11i1IIiiI :
      shutil . rmtree ( os . path . join ( IiiIi , ii1IIIIiI11 ) )
      if 26 - 26: O0OoO % ii . IIIi * O0OoO + IIiIiII11i - Ii1I
   else :
    pass
    if 20 - 20: oO0o
    if 99 - 99: I1ii11iIi11i + ii . o0oOO0O00o0O + o0o00Oo0O
 oo000o0O = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.phstreams/Cache' ) , '' )
 if os . path . exists ( iiIII1iIiI1Ii11Iiii ) == True :
  for IiiIi , IiI11i1IIiiI , oOOo000oOoO0 in os . walk ( oo000o0O ) :
   IiIi = 0
   IiIi += len ( oOOo000oOoO0 )
   if 1 - 1: IIiIiII11i - ooOoO0O00 + OoOo00o
   if 58 - 58: o0oOO0O00o0O - ii
   if IiIi > 0 :
    if 56 - 56: o0oOO0O00o0O / o0oOO0O00o0O
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    if i1iiIIiiI111 . yesno ( "Delete Phoenix Cache Files" , str ( IiIi ) + " files found" , "Do you want to delete them?" ) :
     if 21 - 21: o0o00Oo0O * O0OoO % OOooOOo / o0o00Oo0O
     for ooOO0oO0oo00o in oOOo000oOoO0 :
      os . unlink ( os . path . join ( IiiIi , ooOO0oO0oo00o ) )
     for ii1IIIIiI11 in IiI11i1IIiiI :
      shutil . rmtree ( os . path . join ( IiiIi , ii1IIIIiI11 ) )
      if 85 - 85: ii + ii
   else :
    pass
    if 23 - 23: ooOoO0O00
    if 31 - 31: I1ii11iIi11i - iI11I1II1I1I / iI1iI1I1i1I . oO0o
 oOOo0O0Oo = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.spotitube/cache' ) , '' )
 if os . path . exists ( iiIII1iIiI1Ii11Iiii ) == True :
  for IiiIi , IiI11i1IIiiI , oOOo000oOoO0 in os . walk ( oOOo0O0Oo ) :
   IiIi = 0
   IiIi += len ( oOOo000oOoO0 )
   if 50 - 50: OoOo00o * iI1iI1I1i1I + IIIii1II1II - I1ii11iIi11i
   if 79 - 79: oO0o / ooOoO0O00
   if IiIi > 0 :
    if 30 - 30: OOooOOo - Ii
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    if i1iiIIiiI111 . yesno ( "Delete YouTube Music Cache Files" , str ( IiIi ) + " files found" , "Do you want to delete them?" ) :
     if 94 - 94: OOooOOo % o0oOO0O00o0O
     for ooOO0oO0oo00o in oOOo000oOoO0 :
      os . unlink ( os . path . join ( IiiIi , ooOO0oO0oo00o ) )
     for ii1IIIIiI11 in IiI11i1IIiiI :
      shutil . rmtree ( os . path . join ( IiiIi , ii1IIIIiI11 ) )
      if 39 - 39: OOooOOo + IIIi % o0o00Oo0O
   else :
    pass
    if 26 - 26: O0OoO + OOooOOo
    if 17 - 17: Ii1I - o0oOO0O00o0O % I1ii11iIi11i * o0o00Oo0O % o0o00Oo0O * IIIii1II1II
 iIi1i1iiIiiiI = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.supercartoons/cache' ) , '' )
 if os . path . exists ( iiIII1iIiI1Ii11Iiii ) == True :
  for IiiIi , IiI11i1IIiiI , oOOo000oOoO0 in os . walk ( iIi1i1iiIiiiI ) :
   IiIi = 0
   IiIi += len ( oOOo000oOoO0 )
   if 79 - 79: ii * IIIi - ooOoO0O00 * ii % o0o00Oo0O % iI11I1II1I1I
   if 82 - 82: OOooOOo . Ii11Ii1I
   if IiIi > 0 :
    if 73 - 73: IIIi
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    if i1iiIIiiI111 . yesno ( "Delete SuperCartoons Cache Files" , str ( IiIi ) + " files found" , "Do you want to delete them?" ) :
     if 25 - 25: OooO0OoOOOO
     for ooOO0oO0oo00o in oOOo000oOoO0 :
      os . unlink ( os . path . join ( IiiIi , ooOO0oO0oo00o ) )
     for ii1IIIIiI11 in IiI11i1IIiiI :
      shutil . rmtree ( os . path . join ( IiiIi , ii1IIIIiI11 ) )
      if 77 - 77: I11i . iI11I1II1I1I . ii . iI11I1II1I1I
   else :
    pass
    if 87 - 87: IIiIiII11i - ii / ooOoO0O00 . Ii11Ii1I - I1ii11iIi11i . Ii
    if 47 - 47: I1ii11iIi11i % oO0o - O0OoO - I1ii11iIi11i * OoOo00o
 OOOOO0oOOoO = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.tvonline.cc/cache' ) , '' )
 if os . path . exists ( iiIII1iIiI1Ii11Iiii ) == True :
  for IiiIi , IiI11i1IIiiI , oOOo000oOoO0 in os . walk ( OOOOO0oOOoO ) :
   IiIi = 0
   IiIi += len ( oOOo000oOoO0 )
   if 42 - 42: oOo0O0Ooo + Ii / oO0o
   if 64 - 64: OooO0OoOOOO
   if IiIi > 0 :
    if 80 - 80: oOo0O0Ooo - Ii / oO0o / OOooOOo + OOooOOo
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    if i1iiIIiiI111 . yesno ( "Delete TVonline Cache Files" , str ( IiIi ) + " files found" , "Do you want to delete them?" ) :
     if 89 - 89: o0o00Oo0O + OooO0OoOOOO * IIIi
     for ooOO0oO0oo00o in oOOo000oOoO0 :
      os . unlink ( os . path . join ( IiiIi , ooOO0oO0oo00o ) )
     for ii1IIIIiI11 in IiI11i1IIiiI :
      shutil . rmtree ( os . path . join ( IiiIi , ii1IIIIiI11 ) )
      if 30 - 30: OOooOOo
   else :
    pass
    if 39 - 39: Ii1I + I11i + IIIi + OooO0OoOOOO
    if 48 - 48: IIIi / O0OoO . iI11I1II1I1I
 ooo0OOoo = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.youtube/kodion' ) , '' )
 if os . path . exists ( iiIII1iIiI1Ii11Iiii ) == True :
  for IiiIi , IiI11i1IIiiI , oOOo000oOoO0 in os . walk ( ooo0OOoo ) :
   IiIi = 0
   IiIi += len ( oOOo000oOoO0 )
   if 52 - 52: oO0o
   if 49 - 49: Ii11Ii1I . Ii1I % O0OoO . I1ii11iIi11i * IIIii1II1II
   if IiIi > 0 :
    if 44 - 44: iI11I1II1I1I / o0o00Oo0O * I1ii11iIi11i + oOo0O0Ooo . O0OoO
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    if i1iiIIiiI111 . yesno ( "Delete YouTube Cache Files" , str ( IiIi ) + " files found" , "Do you want to delete them?" ) :
     if 20 - 20: o0oOO0O00o0O + I11i . IIIi / Ii
     for ooOO0oO0oo00o in oOOo000oOoO0 :
      os . unlink ( os . path . join ( IiiIi , ooOO0oO0oo00o ) )
     for ii1IIIIiI11 in IiI11i1IIiiI :
      shutil . rmtree ( os . path . join ( IiiIi , ii1IIIIiI11 ) )
      if 7 - 7: OOooOOo / OOooOOo . IIIi * o0o00Oo0O + OooO0OoOOOO + OoOo00o
   else :
    pass
    if 98 - 98: IIiIiII11i * OooO0OoOOOO - oOo0O0Ooo % I11i - o0oOO0O00o0O % Ii1I
    if 69 - 69: ooOoO0O00 % oO0o % IIIi / O0OoO / O0OoO
    if 6 - 6: IIiIiII11i % Ii1I % ooOoO0O00 * O0OoO
 iIIoooO0 = xbmc . translatePath ( 'special://masterprofile/addon_data/plugin.video.genesis' )
 i1iiIIiiI111 = xbmcgui . Dialog ( )
 try :
  if i1iiIIiiI111 . yesno ( "Delete Genesis Cache Files" , "Do you want to delete cache" ) :
   iI1iIi1ii1I1 = os . path . join ( iIIoooO0 , "cache.db" )
   os . unlink ( iI1iIi1ii1I1 )
   if 59 - 59: IIiIiII11i * ii - ii
 except :
  pass
  if 33 - 33: o0o00Oo0O . Ii % I11i
 i1iiIIiiI111 = xbmcgui . Dialog ( )
 i1iiIIiiI111 . ok ( "GenieTv" , "                               Finished Deleting Cache " , "                          [COLOR gold]Brought To You By GenieTv[/COLOR]" )
 if 50 - 50: O0OoO
 if 81 - 81: Ii * iI11I1II1I1I / I1ii11iIi11i * IIIii1II1II
 if 83 - 83: Ii - oOo0O0Ooo * Ii
 if 59 - 59: o0oOO0O00o0O - ii / O0OoO + Ii1I . I11i - o0oOO0O00o0O
 if 29 - 29: OoOo00o
 if 26 - 26: o0o00Oo0O % IIIii1II1II - OooO0OoOOOO . IIIii1II1II
 if 70 - 70: I11i + iI1iI1I1i1I / o0oOO0O00o0O + O0OoO / oOo0O0Ooo
 if 33 - 33: ii . o0o00Oo0O
 if 59 - 59: iI11I1II1I1I
def i1OOoO0OO0oO ( url ) :
 print '###' + o0oOoO00o + ' - DELETING PACKAGES###'
 iii1iII1iii = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' , '' ) )
 try :
  for IiiIi , IiI11i1IIiiI , oOOo000oOoO0 in os . walk ( iii1iII1iii ) :
   IiIi = 0
   IiIi += len ( oOOo000oOoO0 )
   if 97 - 97: IIIi / IIIii1II1II - Ii
   if 79 - 79: OOooOOo + iI11I1II1I1I * ooOoO0O00 * O0OoO - iI1iI1I1i1I * oO0o
   if IiIi > 0 :
    if 78 - 78: o0oOO0O00o0O % Ii + o0oOO0O00o0O + I11i
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    if i1iiIIiiI111 . yesno ( "Delete Package Cache Files" , str ( IiIi ) + " files found" , "Do you want to delete them?" ) :
     if 22 - 22: iI1iI1I1i1I - I11i
     for ooOO0oO0oo00o in oOOo000oOoO0 :
      os . unlink ( os . path . join ( IiiIi , ooOO0oO0oo00o ) )
     for ii1IIIIiI11 in IiI11i1IIiiI :
      shutil . rmtree ( os . path . join ( IiiIi , ii1IIIIiI11 ) )
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
 if 54 - 54: OoOo00o * oO0o - o0oOO0O00o0O * iI1iI1I1i1I + I11i - Ii11Ii1I
 if 5 - 5: OoOo00o + Ii11Ii1I
 if 48 - 48: IIIi * ooOoO0O00 - Ii1I / oOo0O0Ooo + Ii - ooOoO0O00
 if 91 - 91: I11i / Ii
 if 96 - 96: oO0o + o0oOO0O00o0O * IIiIiII11i
 if 82 - 82: I11i + Ii11Ii1I * oOo0O0Ooo - OoOo00o
 if 6 - 6: IIIii1II1II / iI11I1II1I1I / O0OoO / oOo0O0Ooo - ooOoO0O00 - IIIii1II1II
 if 8 - 8: Ii * iI1iI1I1i1I . IIIii1II1II / IIIii1II1II
 if 42 - 42: ii / IIIi . I11i / o0o00Oo0O - OooO0OoOOOO * OooO0OoOOOO
def IiIiiiiI1 ( url ) :
 print '###' + o0oOoO00o + ' - DELETING PACKAGES###'
 iii1iII1iii = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' , '' ) )
 try :
  for IiiIi , IiI11i1IIiiI , oOOo000oOoO0 in os . walk ( iii1iII1iii ) :
   IiIi = 0
   IiIi += len ( oOOo000oOoO0 )
   if 1 - 1: Ii11Ii1I % IIIi
   if 97 - 97: OOooOOo
   if IiIi > 0 :
    if 13 - 13: OOooOOo % IIIii1II1II . o0o00Oo0O / I1ii11iIi11i % I1ii11iIi11i
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    if i1iiIIiiI111 . yesno ( "Delete Package Cache Files" , str ( IiIi ) + " files found" , "Do you want to delete them?" ) :
     if 19 - 19: IIIi % O0OoO - O0OoO % oOo0O0Ooo . IIIii1II1II - ii
     for ooOO0oO0oo00o in oOOo000oOoO0 :
      os . unlink ( os . path . join ( IiiIi , ooOO0oO0oo00o ) )
     for ii1IIIIiI11 in IiI11i1IIiiI :
      shutil . rmtree ( os . path . join ( IiiIi , ii1IIIIiI11 ) )
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
 i1II1 ( url )
 return
 if 100 - 100: oOo0O0Ooo + Ii11Ii1I + I11i . ooOoO0O00 % ii
 if 64 - 64: o0o00Oo0O % ooOoO0O00 * IIIi - Ii11Ii1I + I1ii11iIi11i
 if 65 - 65: OOooOOo . Ii
 if 36 - 36: OoOo00o * o0oOO0O00o0O + OooO0OoOOOO * o0oOO0O00o0O . Ii1I - iI11I1II1I1I
 if 14 - 14: iI1iI1I1i1I * OoOo00o + Ii
 if 84 - 84: o0oOO0O00o0O / IIiIiII11i
 if 86 - 86: oOo0O0Ooo
 if 97 - 97: IIiIiII11i
 if 38 - 38: oOo0O0Ooo
 if 42 - 42: I11i
def ii1i1 ( url , name ) :
 iI11 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 O0OooO0oo = os . path . join ( iI11 , 'advancedsettings.xml' )
 i1iiIIiiI111 = xbmcgui . Dialog ( )
 o0OO0 = os . path . join ( iI11 , 'advancedsettings.xml.bak' )
 if os . path . exists ( o0OO0 ) == False :
  if i1iiIIiiI111 . yesno ( "Back Up Original" , 'Have You Backed Up Your Original?' , '' , "[B][COLOR red]     AS YOU CANNOT GO BACK !!![/B][/COLOR]" ) :
   print '###' + o0oOoO00o + ' - ADVANCED XML###'
   iI11 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
   O0OooO0oo = os . path . join ( iI11 , 'advancedsettings.xml' )
   try :
    os . remove ( O0OooO0oo )
    print '=== GenieTv - REMOVING    ' + str ( O0OooO0oo ) + '    ==='
   except :
    pass
   O000oo0O = i1 . http_GET ( url ) . content
   oOOo0oo0O = open ( O0OooO0oo , "w" )
   oOOo0oo0O . write ( O000oo0O )
   oOOo0oo0O . close ( )
   print '=== GenieTv - WRITING NEW    ' + str ( O0OooO0oo ) + '    ==='
   i1iiIIiiI111 = xbmcgui . Dialog ( )
   i1iiIIiiI111 . ok ( o0oOoO00o , "       Done Adding new Advanced XML" )
 else :
  print '###' + o0oOoO00o + ' - ADVANCED XML###'
  iI11 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
  O0OooO0oo = os . path . join ( iI11 , 'advancedsettings.xml' )
  try :
   os . remove ( O0OooO0oo )
   print '=== GenieTv - REMOVING    ' + str ( O0OooO0oo ) + '    ==='
  except :
   pass
  O000oo0O = i1 . http_GET ( url ) . content
  oOOo0oo0O = open ( O0OooO0oo , "w" )
  oOOo0oo0O . write ( O000oo0O )
  oOOo0oo0O . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( O0OooO0oo ) + '    ==='
  i1iiIIiiI111 = xbmcgui . Dialog ( )
  i1iiIIiiI111 . ok ( o0oOoO00o , "       Done Adding new Advanced XML" )
 return
 if 82 - 82: IIIii1II1II - Ii1I / OooO0OoOOOO / Ii11Ii1I
def IIiii1I ( url , name ) :
 print '###' + o0oOoO00o + ' - CHECK ADVANCE XML###'
 iI11 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 O0OooO0oo = os . path . join ( iI11 , 'advancedsettings.xml' )
 try :
  oOOo0oo0O = open ( O0OooO0oo ) . read ( )
  if 'zero' in oOOo0oo0O :
   name = '0CACHE'
  elif 'tuxen' in oOOo0oo0O :
   name = 'TUXENS'
  elif 'muckys' in oOOo0oo0O :
   name = 'MUCKYS'
  elif 'p2p1' in oOOo0oo0O :
   name = '1st P2P RECOMMENDED'
  elif 'p2p2' in oOOo0oo0O :
   name = '2nd P2P RECOMMENDED'
  elif 'mikey' in oOOo0oo0O :
   name = 'MIKEY1234'
 except :
  name = "NO ADVANCED"
 i1iiIIiiI111 = xbmcgui . Dialog ( )
 i1iiIIiiI111 . ok ( o0oOoO00o , "[COLOR yellow]YOU HAVE[/COLOR] " + name + "[COLOR yellow] XML SETTINGS SETUP[/COLOR]" )
 return
 if 11 - 11: I1ii11iIi11i + IIiIiII11i - Ii1I
def OoOOoo0o00O0oO ( url ) :
 print '###' + o0oOoO00o + ' - DELETING ADVANCE XML###'
 iI11 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 O0OooO0oo = os . path . join ( iI11 , 'advancedsettings.xml' )
 try :
  os . remove ( O0OooO0oo )
  i1iiIIiiI111 = xbmcgui . Dialog ( )
  print '=== GenieTv - DELETING    ' + str ( O0OooO0oo ) + '    ==='
  i1iiIIiiI111 . ok ( o0oOoO00o , "       Remove Advanced Settings Sucessfull" )
 except :
  i1iiIIiiI111 = xbmcgui . Dialog ( )
  i1iiIIiiI111 . ok ( o0oOoO00o , "       No Advanced Settings To Remove" )
 return
 if 28 - 28: ii % o0o00Oo0O - IIIii1II1II / I11i / oOo0O0Ooo
 if 41 - 41: IIiIiII11i * OooO0OoOOOO / oO0o . OoOo00o
 if 50 - 50: ii + iI11I1II1I1I / OoOo00o / IIIii1II1II . Ii . O0OoO
 if 75 - 75: iI11I1II1I1I % O0OoO / IIIii1II1II - o0oOO0O00o0O % Ii
 if 11 - 11: iI1iI1I1i1I . Ii11Ii1I
 if 87 - 87: IIIii1II1II + IIIii1II1II
 if 45 - 45: ooOoO0O00 - I1ii11iIi11i
 if 87 - 87: OOooOOo - oO0o * oO0o / Ii11Ii1I . iI1iI1I1i1I * I11i
 if 21 - 21: IIiIiII11i
 if 29 - 29: OOooOOo % Ii11Ii1I
def iii11 ( url = 'http://www.iplocation.net/' , inc = 1 ) :
 Ii1i = re . compile ( "<td width='80'>(.+?)</td><td>(.+?)</td><td>(.+?)</td><td>.+?</td><td>(.+?)</td>" ) . findall ( i1 . http_GET ( url ) . content )
 for oOo0OO0 , OoOiIiIi1i1ii11 , O0O0o0o0OOooo , I1II1 in Ii1i :
  if inc < 2 : i1iiIIiiI111 = xbmcgui . Dialog ( ) ; i1iiIIiiI111 . ok ( 'Check My IP' , "[B][COLOR gold]Your IP Address is: [/COLOR][/B] %s" % oOo0OO0 , '[B][COLOR gold]Your IP is based in: [/COLOR][/B] %s' % O0O0o0o0OOooo , '[B][COLOR gold]Your Service Provider is:[/COLOR][/B] %s' % I1II1 )
  inc = inc + 1
  if 97 - 97: I1ii11iIi11i + OooO0OoOOOO - OooO0OoOOOO / I1ii11iIi11i
  if 76 - 76: oO0o + IIIii1II1II - OooO0OoOOOO . ooOoO0O00
  if 87 - 87: O0OoO + o0o00Oo0O
  if 69 - 69: iI11I1II1I1I + ooOoO0O00 % IIiIiII11i . oO0o * OoOo00o * OooO0OoOOOO
  if 90 - 90: IIIi
  if 62 - 62: IIiIiII11i
  if 60 - 60: ooOoO0O00 * IIiIiII11i + Ii11Ii1I / IIIi % OOooOOo
  if 100 - 100: iI11I1II1I1I * ooOoO0O00 - Ii - IIIi % Ii11Ii1I
  if 56 - 56: iI1iI1I1i1I
def Oo0ooo0ooo ( url , name ) :
 i1iiIIiiI111 = xbmcgui . Dialog ( )
 if i1iiIIiiI111 . yesno ( "GenieTv" , '                                    Install Latest .ini File' ) :
  print '###' + o0oOoO00o + ' - CUSTOM FTV INI###'
  iI11 = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/plugin.video.GenieTv' , '' ) )
  O0OooO0oo = os . path . join ( iI11 , 'addons2.ini' )
  O000oo0O = i1 . http_GET ( url ) . content
  oOOo0oo0O = open ( O0OooO0oo , "w" )
  oOOo0oo0O . write ( O000oo0O )
  oOOo0oo0O . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( O0OooO0oo ) + '    ==='
  i1iiIIiiI111 = xbmcgui . Dialog ( )
  i1iiIIiiI111 . ok ( o0oOoO00o , "                               Done Adding New .ini File" )
 return
 if 45 - 45: iI1iI1I1i1I . I1ii11iIi11i % Ii11Ii1I % o0oOO0O00o0O
def IiIiii1IiiiI ( url , name ) :
 i1iiIIiiI111 = xbmcgui . Dialog ( )
 if i1iiIIiiI111 . yesno ( "GenieTv" , '                               Install Custom Settings' ) :
  print '###' + o0oOoO00o + ' - CUSTOM FTV SETTINGS###'
  iI11 = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/plugin.video.GenieTv' , '' ) )
  O0OooO0oo = os . path . join ( iI11 , 'settings.xml' )
  O000oo0O = i1 . http_GET ( url ) . content
  oOOo0oo0O = open ( O0OooO0oo , "w" )
  oOOo0oo0O . write ( O000oo0O )
  oOOo0oo0O . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( O0OooO0oo ) + '    ==='
  i1iiIIiiI111 = xbmcgui . Dialog ( )
  i1iiIIiiI111 . ok ( o0oOoO00o , "                               Done Adding New Settings" )
 return
 if 44 - 44: iI1iI1I1i1I . OooO0OoOOOO % IIIi - O0OoO - Ii1I
 if 34 - 34: Ii1I % ooOoO0O00 - oO0o
def IiI111i ( ) :
 try :
  IiI1ii1 = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/plugin.video.GenieTv' , '' ) )
  if os . path . exists ( IiI1ii1 ) == True :
   i1iiIIiiI111 = xbmcgui . Dialog ( )
   if i1iiIIiiI111 . yesno ( "GenieTv" , "                               Delete FTV Guide Database" ) :
    OOO00oo0 = os . path . join ( IiI1ii1 , "source.db" )
    os . unlink ( OOO00oo0 )
  i1iiIIiiI111 . ok ( "GenieTv" , "                                     FTV Database Reset" )
 except :
  i1iiIIiiI111 = xbmcgui . Dialog ( )
  i1iiIIiiI111 . ok ( o0oOoO00o , "               Error Deleting Database No Database To Delete" )
 return
 if 80 - 80: OooO0OoOOOO . I11i
 if 8 - 8: I11i . IIiIiII11i . o0oOO0O00o0O - Ii
 if 50 - 50: Ii11Ii1I . o0o00Oo0O % oO0o . OoOo00o + Ii11Ii1I . OOooOOo
 if 69 - 69: Ii + Ii . Ii - Ii % Ii11Ii1I / o0oOO0O00o0O
 if 59 - 59: ii
def iiI111I1iIiI ( url ) :
 I11iii1Ii = urllib2 . Request ( url )
 I11iii1Ii . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
 I1IIiiIiii = urllib2 . urlopen ( I11iii1Ii )
 O000oo0O = I1IIiiIiii . read ( )
 I1IIiiIiii . close ( )
 return O000oo0O
 if 96 - 96: Ii11Ii1I
 if 54 - 54: iI1iI1I1i1I % iI1iI1I1i1I - O0OoO
 if 32 - 32: I11i % IIiIiII11i / I11i . IIIii1II1II . I11i
 if 29 - 29: ii % IIiIiII11i % Ii - I1ii11iIi11i
 if 5 - 5: Ii1I . IIiIiII11i . ooOoO0O00
 if 35 - 35: I11i + oO0o - Ii1I
 if 24 - 24: IIiIiII11i
def iI11Ii1Ii ( params ) :
 plugintools . log ( "freshstart.main_list " + repr ( params ) ) ; iII1iII11iii = plugintools . message_yes_no ( o0oOoO00o , "Do you wish to restore your" , "Kodi configuration to default settings?" )
 if iII1iII11iii :
  i1iIIi = xbmcaddon . Addon ( id = o00 ) . getAddonInfo ( 'path' ) ; i1iIIi = xbmc . translatePath ( i1iIIi ) ;
  oo0O0OO0Oooo = os . path . join ( i1iIIi , ".." , ".." ) ; oo0O0OO0Oooo = os . path . abspath ( oo0O0OO0Oooo ) ; plugintools . log ( "freshstart.main_list xbmcPath=" + oo0O0OO0Oooo ) ; IiiI11Iii = False
  try :
   for IiiIi , IiI11i1IIiiI , oOOo000oOoO0 in os . walk ( oo0O0OO0Oooo , topdown = True ) :
    IiI11i1IIiiI [ : ] = [ ii1IIIIiI11 for ii1IIIIiI11 in IiI11i1IIiiI if ii1IIIIiI11 not in iiIIIII1i1iI ]
    for ooo in oOOo000oOoO0 :
     try : os . remove ( os . path . join ( IiiIi , ooo ) )
     except :
      if ooo not in [ "Addons15.db" , "MyVideos75.db" , "Textures13.db" , "xbmc.log" ] : IiiI11Iii = True
      plugintools . log ( "Error removing " + IiiIi + " " + ooo )
    for ooo in IiI11i1IIiiI :
     try : os . rmdir ( os . path . join ( IiiIi , ooo ) )
     except :
      if ooo not in [ "Database" , "userdata" ] : IiiI11Iii = True
      plugintools . log ( "Error removing " + IiiIi + " " + ooo )
   if not IiiI11Iii : plugintools . log ( "freshstart.main_list All user files removed, you now have a clean install" ) ; plugintools . message ( o0oOoO00o , "The process is complete, you're now back to a fresh Kodi configuration with GenieTv!" , "Please reboot your system or restart Kodi in order for the changes to be applied." )
   else : plugintools . log ( "freshstart.main_list User files partially removed" ) ; plugintools . message ( o0oOoO00o , "The process is complete, you're now back to a fresh Kodi configuration with GenieTv" , "Please reboot your system or restart Kodi in order for the changes to be applied." )
  except : plugintools . message ( o0oOoO00o , "Problem found" , "Your settings has not been changed" ) ; import traceback ; plugintools . log ( traceback . format_exc ( ) ) ; plugintools . log ( "freshstart.main_list NOT removed" )
  plugintools . add_item ( action = "" , title = "Now Exit Kodi" , folder = False )
 else : plugintools . message ( o0oOoO00o , "Your settings" , "has not been changed" ) ; plugintools . add_item ( action = "" , title = "Done" , folder = False )
 OO00OOoO0o ( )
 if 42 - 42: iI1iI1I1i1I + ooOoO0O00 - Ii11Ii1I / OooO0OoOOOO . o0oOO0O00o0O
 if 30 - 30: I1ii11iIi11i + Ii11Ii1I % Ii * ooOoO0O00 + oOo0O0Ooo % IIIii1II1II
 if 30 - 30: Ii * I1ii11iIi11i . IIiIiII11i + Ii1I / I11i % IIIi
def OOOo0o ( ) :
 oo0o0o0o0o0 = [ ]
 Ii1Ii = sys . argv [ 2 ]
 if len ( Ii1Ii ) >= 2 :
  iIIOOoOOooO = sys . argv [ 2 ]
  i1111II1iIII = iIIOOoOOooO . replace ( '?' , '' )
  if ( iIIOOoOOooO [ len ( iIIOOoOOooO ) - 1 ] == '/' ) :
   iIIOOoOOooO = iIIOOoOOooO [ 0 : len ( iIIOOoOOooO ) - 2 ]
  I1ii11ii1iiI = i1111II1iIII . split ( '&' )
  oo0o0o0o0o0 = { }
  for iIi11i in range ( len ( I1ii11ii1iiI ) ) :
   oO0oo0 = { }
   oO0oo0 = I1ii11ii1iiI [ iIi11i ] . split ( '=' )
   if ( len ( oO0oo0 ) ) == 2 :
    oo0o0o0o0o0 [ oO0oo0 [ 0 ] ] = oO0oo0 [ 1 ]
    if 12 - 12: Ii + ooOoO0O00 - Ii11Ii1I + o0o00Oo0O . oOo0O0Ooo
 return oo0o0o0o0o0
 if 8 - 8: I11i
ooOO0O0O = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkbw==' )
i1OoOO = base64 . decodestring ( 'L3N0b3JhZ2UvZW11bGF0ZWQvMA==' )
IIIiIIIi111iI = base64 . decodestring ( 'L2dlbmllLnR4dA==' )
II1IIII1i1i = base64 . decodestring ( 'LmFyY2hpdGVjdHMueDEwaG9zdC5jb20vdGVzdC93aC50eHQ=' )
I11I = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby9maXhlcy9maXhlcy50eHQ=' )
IiIiI1i1ii = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby9hcHBzL2FwcHMueG1s' )
iIi1i1II = base64 . decodestring ( 'L2FkZG9ucy9uZXcudHh0' )
iiii1I1IiI = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby92b2Qvdm9kLnBocA==' )
OOOoOO00OO0 = base64 . decodestring ( 'L2FkZG9ucy9pcHR2LnR4dA==' )
o0OOOoO = base64 . decodestring ( 'L2FkZG9ucy92aWRlby50eHQ=' )
o0OooOoOOoO = base64 . decodestring ( 'L2FkZG9ucy9zcG9ydHMudHh0' )
Oo0I1iii = base64 . decodestring ( 'L2FkZG9ucy9raWRzLnR4dA==' )
I11IiI1iII = base64 . decodestring ( 'L2FkZG9ucy9tdXNpYy50eHQ=' )
iIi11 = base64 . decodestring ( 'L2FkZG9ucy9wcm9ncmFtcy50eHQ=' )
i1IiIi1I1i = base64 . decodestring ( 'L2FkZG9ucy94eHgudHh0' )
o0ooOo000oo = base64 . decodestring ( 'L2FkZG9ucy9yZXBvLnR4dA==' )
IIiiii = base64 . decodestring ( 'L2FkZG9ucy9wYWNrcy50eHQ=' )
II1I11i = base64 . decodestring ( 'L2FkZG9ucy9za2lucy50eHQ=' )
oOoOoo0 = base64 . decodestring ( 'L2FkZG9ucy9hcnQudHh0' )
o00oO00 = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2dvdGhhbS50eHQ=' )
IIiI11i1111Ii = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2hlbGl4LnR4dA==' )
Ii11Iii1i1ii = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2lzZW5nYXJkLnR4dA==' )
ooIi1Iii1 = base64 . decodestring ( 'L2FkZG9ucy9SU1MudHh0' )
ii1I111i1Ii = base64 . decodestring ( 'Q1VOVA==' )
def II1I ( name , url , mode , iconimage , fanart , description , showcontext = True , allinfo = { } ) :
 i1I1II = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 Ii1I1I1i11ii = True
 OoOo0oO0o = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 OoOo0oO0o . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 OoOo0oO0o . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  iiI1 = [ ]
  if showcontext == 'fav' :
   iiI1 . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in OOO00 :
   iiI1 . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fanart=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , urllib . quote_plus ( fanart ) , mode ) ) )
  OoOo0oO0o . addContextMenuItems ( iiI1 )
 Ii1I1I1i11ii = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = i1I1II , listitem = OoOo0oO0o , isFolder = True )
 return Ii1I1I1i11ii
 if 97 - 97: oOo0O0Ooo
def ooOOoooooo ( name , url , mode , iconimage , fanart , description ) :
 i1I1II = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 Ii1I1I1i11ii = True
 OoOo0oO0o = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 OoOo0oO0o . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 OoOo0oO0o . setProperty ( "Fanart_Image" , fanart )
 Ii1I1I1i11ii = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = i1I1II , listitem = OoOo0oO0o , isFolder = False )
 return Ii1I1I1i11ii
 if 56 - 56: Ii11Ii1I * ooOoO0O00 + IIIi * I11i % oO0o
 if 22 - 22: iI11I1II1I1I - I1ii11iIi11i . Ii % o0oOO0O00o0O
iIIOOoOOooO = OOOo0o ( )
Ii1II1I11i1 = None
ooo = None
IIi11II1II111 = None
iI1IOooOoOo = None
III1I1Iii1iiI = None
I1o0OooOOOOOO = None
OooO00Oo = None
if 81 - 81: Ii1I - oO0o * OoOo00o
if 81 - 81: o0oOO0O00o0O - Ii11Ii1I - IIIii1II1II % OooO0OoOOOO % I11i . iI11I1II1I1I
try :
 OooO00Oo = int ( iIIOOoOOooO [ "fav_mode" ] )
except :
 pass
 if 79 - 79: Ii1I - Ii1I . Ii11Ii1I / OooO0OoOOOO
try :
 Ii1II1I11i1 = urllib . unquote_plus ( iIIOOoOOooO [ "url" ] )
except :
 pass
try :
 ooo = urllib . unquote_plus ( iIIOOoOOooO [ "name" ] )
except :
 pass
try :
 iI1IOooOoOo = urllib . unquote_plus ( iIIOOoOOooO [ "iconimage" ] )
except :
 pass
try :
 IIi11II1II111 = int ( iIIOOoOOooO [ "mode" ] )
except :
 pass
try :
 III1I1Iii1iiI = urllib . unquote_plus ( iIIOOoOOooO [ "fanart" ] )
except :
 pass
try :
 I1o0OooOOOOOO = urllib . unquote_plus ( iIIOOoOOooO [ "description" ] )
except :
 pass
 if 57 - 57: O0OoO * iI11I1II1I1I * o0oOO0O00o0O * Ii11Ii1I / Ii11Ii1I
 if 43 - 43: o0o00Oo0O * Ii - ii - OoOo00o
print str ( oOOoO0 ) + ': ' + str ( IiiIII111iI )
print "Mode: " + str ( IIi11II1II111 )
print "URL: " + str ( Ii1II1I11i1 )
print "Name: " + str ( ooo )
print "IconImage: " + str ( iI1IOooOoOo )
if 46 - 46: OoOo00o * ooOoO0O00 / Ii1I
if 100 - 100: oOo0O0Ooo - IIIii1II1II
def iiO0o0oOOOoOo ( content , viewType ) :
 if 91 - 91: I11i * Ii1I - o0oOO0O00o0O . IIiIiII11i
 if content :
  xbmcplugin . setContent ( int ( sys . argv [ 1 ] ) , content )
 if o0oO0 . getSetting ( 'auto-view' ) == 'true' :
  xbmc . executebuiltin ( "Container.SetViewMode(%s)" % o0oO0 . getSetting ( viewType ) )
  if 1 - 1: IIIii1II1II + IIIi * Ii1I
if iI1IOooOoOo == None : iI1IOooOoOo = i1iIIi1
if III1I1Iii1iiI == None : III1I1Iii1iiI = i1iiIII111ii
if IIi11II1II111 == None :
 ooOOO00Ooo ( )
 if 44 - 44: o0oOO0O00o0O
elif IIi11II1II111 == 1 :
 ooOoO0 ( Ii1II1I11i1 )
 if 79 - 79: I11i % IIIii1II1II . o0o00Oo0O
elif IIi11II1II111 == 44 :
 oOo00oOOOOO ( Ii1II1I11i1 )
 if 56 - 56: OoOo00o + ooOoO0O00 * o0oOO0O00o0O - o0o00Oo0O
elif IIi11II1II111 == 2 :
 O0II11i11II ( )
 if 84 - 84: o0oOO0O00o0O % oOo0O0Ooo / iI11I1II1I1I * Ii11Ii1I * iI11I1II1I1I + Ii1I
elif IIi11II1II111 == 3 :
 O0iIi1IiII ( )
 if 78 - 78: OooO0OoOOOO / o0oOO0O00o0O * Ii11Ii1I . IIIii1II1II . OoOo00o - IIIi
elif IIi11II1II111 == 21 :
 iI1Ii11111iIi ( )
 if 39 - 39: O0OoO . ooOoO0O00 + ii . o0oOO0O00o0O - Ii % IIIi
elif IIi11II1II111 == 4 :
 ii1i1i1IiII ( )
 if 38 - 38: OoOo00o
elif IIi11II1II111 == 5 :
 oooo0OOo ( Ii1II1I11i1 )
 if 9 - 9: iI1iI1I1i1I . oO0o . OoOo00o / ii
elif IIi11II1II111 == 6 :
 i1OOoO0OO0oO ( Ii1II1I11i1 )
 if 59 - 59: iI11I1II1I1I + ooOoO0O00 % IIiIiII11i
elif IIi11II1II111 == 7 :
 ii1i1 ( Ii1II1I11i1 , ooo )
 if 2 - 2: IIiIiII11i + iI1iI1I1i1I . oO0o
elif IIi11II1II111 == 8 :
 IIiii1I ( Ii1II1I11i1 , ooo )
 if 14 - 14: IIIii1II1II * oOo0O0Ooo - Ii1I
elif IIi11II1II111 == 9 :
 FIXREPOSADDONS ( Ii1II1I11i1 )
 if 10 - 10: o0oOO0O00o0O % IIIi * Ii1I * o0o00Oo0O * Ii % IIIi
elif IIi11II1II111 == 10 :
 oooooo0O000o ( )
 if 68 - 68: ii * OOooOOo
elif IIi11II1II111 == 11 :
 OoOOoo0o00O0oO ( Ii1II1I11i1 )
 if 9 - 9: IIIi
elif IIi11II1II111 == 12 :
 iii11 ( )
 if 36 - 36: IIIi / OOooOOo + OOooOOo * O0OoO / IIIii1II1II * o0o00Oo0O
elif IIi11II1II111 == 13 :
 iIiii1IIi1I ( )
 if 17 - 17: oO0o / O0OoO % oOo0O0Ooo
elif IIi11II1II111 == 14 :
 i1II1 ( Ii1II1I11i1 )
 if 47 - 47: I1ii11iIi11i * oO0o / I11i * oOo0O0Ooo
elif IIi11II1II111 == 15 :
 iiI1II11II1i ( )
 if 60 - 60: Ii1I / OooO0OoOOOO . Ii / oO0o % IIiIiII11i
elif IIi11II1II111 == 16 :
 Oo0ooo0ooo ( Ii1II1I11i1 , ooo )
 if 6 - 6: o0oOO0O00o0O % I11i + IIIi
elif IIi11II1II111 == 17 :
 IiIiii1IiiiI ( Ii1II1I11i1 , ooo )
 if 91 - 91: I11i + o0o00Oo0O * OoOo00o * OooO0OoOOOO * Ii1I
elif IIi11II1II111 == 18 :
 IiI111i ( )
 if 83 - 83: ii
elif IIi11II1II111 == 19 :
 OOoO000O00oO ( ooo , Ii1II1I11i1 , I1o0OooOOOOOO )
 if 52 - 52: I11i / OOooOOo % OoOo00o % oO0o / OooO0OoOOOO % I11i
elif IIi11II1II111 == 40 :
 o0ooO00OOooo0Ooo ( ooo , Ii1II1I11i1 , I1o0OooOOOOOO )
 if 88 - 88: IIIii1II1II / Ii / Ii11Ii1I / Ii * Ii1I % iI1iI1I1i1I
elif IIi11II1II111 == 42 :
 oOo00OooO0oO ( ooo , Ii1II1I11i1 , I1o0OooOOOOOO )
 if 43 - 43: OOooOOo * oO0o % ooOoO0O00 * Ii11Ii1I + iI11I1II1I1I
elif IIi11II1II111 == 43 :
 oOO0OOOOoooO ( Ii1II1I11i1 )
 if 80 - 80: I11i . o0oOO0O00o0O . ii
elif IIi11II1II111 == 20 :
 oOO ( Ii1II1I11i1 )
 if 63 - 63: O0OoO . IIIii1II1II
elif IIi11II1II111 == 22 :
 iII1 ( Ii1II1I11i1 )
 if 66 - 66: oOo0O0Ooo
elif IIi11II1II111 == 23 :
 iI11ii ( Ii1II1I11i1 )
 if 99 - 99: oO0o % o0o00Oo0O . IIIi - Ii1I . I1ii11iIi11i / OOooOOo
elif IIi11II1II111 == 24 :
 o0OoO0O ( Ii1II1I11i1 )
 if 60 - 60: Ii1I
elif IIi11II1II111 == 25 :
 O0O0OOooo ( Ii1II1I11i1 )
 if 78 - 78: OoOo00o + IIiIiII11i
elif IIi11II1II111 == 26 :
 III1I1I11 ( Ii1II1I11i1 )
 if 55 - 55: ii
elif IIi11II1II111 == 27 :
 i1iIIIiI ( Ii1II1I11i1 )
 if 90 - 90: oOo0O0Ooo
elif IIi11II1II111 == 28 :
 Oo000O000 ( Ii1II1I11i1 )
 if 4 - 4: IIIii1II1II % O0OoO - IIIii1II1II - I11i
elif IIi11II1II111 == 29 :
 i1I1iiiI ( Ii1II1I11i1 )
 if 30 - 30: OooO0OoOOOO
elif IIi11II1II111 == 30 :
 IIIII1iii ( Ii1II1I11i1 )
 if 34 - 34: OoOo00o - IIiIiII11i - I11i + o0oOO0O00o0O + IIIi
elif IIi11II1II111 == 31 :
 Oo00oOo ( Ii1II1I11i1 )
 if 70 - 70: ii + oO0o * I1ii11iIi11i
elif IIi11II1II111 == 32 :
 i1I1IiI ( )
 if 20 - 20: Ii - IIiIiII11i - O0OoO % OoOo00o . O0OoO
elif IIi11II1II111 == 33 :
 Ii1iI11iI1 ( )
 if 50 - 50: iI11I1II1I1I + IIIi - iI1iI1I1i1I - ii
elif IIi11II1II111 == 35 :
 ooOOOOo0 ( Ii1II1I11i1 )
 if 84 - 84: OOooOOo - iI1iI1I1i1I
elif IIi11II1II111 == 34 :
 o0oo ( Ii1II1I11i1 )
 if 80 - 80: Ii % IIIii1II1II - I1ii11iIi11i % IIIii1II1II
elif IIi11II1II111 == 36 :
 OOo ( Ii1II1I11i1 )
 if 89 - 89: Ii11Ii1I * iI1iI1I1i1I + OOooOOo / Ii
elif IIi11II1II111 == 37 :
 IiI1iII1II111 ( Ii1II1I11i1 )
 if 68 - 68: ii * iI1iI1I1i1I
elif IIi11II1II111 == 38 :
 O0ooOOO0 ( Ii1II1I11i1 )
 if 86 - 86: I11i / OOooOOo
elif IIi11II1II111 == 41 :
 iI11Ii1Ii ( iIIOOoOOooO )
 if 40 - 40: o0oOO0O00o0O
elif IIi11II1II111 == 39 :
 o0o ( Ii1II1I11i1 )
 if 62 - 62: O0OoO / IIIii1II1II
elif IIi11II1II111 == 45 :
 TEXTS ( )
 if 74 - 74: o0oOO0O00o0O % IIIi / IIIi - iI11I1II1I1I - IIiIiII11i + IIIii1II1II
elif IIi11II1II111 == 46 :
 ii1II1 ( )
 if 92 - 92: iI1iI1I1i1I % IIIi
elif IIi11II1II111 == 47 :
 GEVID ( )
 if 18 - 18: O0OoO + IIIi / IIIii1II1II / OoOo00o + iI11I1II1I1I % OooO0OoOOOO
elif IIi11II1II111 == 48 :
 oooo00 ( ooo , Ii1II1I11i1 , I1o0OooOOOOOO )
 if 94 - 94: iI1iI1I1i1I
elif IIi11II1II111 == 49 :
 I1i11iIIi11 ( )
 if 37 - 37: OoOo00o
elif IIi11II1II111 == 222 :
 I1i11 ( Ii1II1I11i1 )
 if 52 - 52: Ii1I * oOo0O0Ooo . IIIii1II1II + ooOoO0O00 % OoOo00o / iI11I1II1I1I
elif IIi11II1II111 == 333 :
 O0O00oOo0o000 ( Ii1II1I11i1 )
 if 68 - 68: IIIi - OOooOOo . Ii + I11i
 if 71 - 71: Ii / ooOoO0O00 * oOo0O0Ooo / OOooOOo
elif IIi11II1II111 == 1020 :
 ii1iI1i1 ( )
 if 33 - 33: iI1iI1I1i1I . I1ii11iIi11i
elif IIi11II1II111 == 1021 :
 ANIMEEP ( )
 if 89 - 89: o0oOO0O00o0O + ooOoO0O00 - OooO0OoOOOO + O0OoO . IIiIiII11i
elif IIi11II1II111 == 1022 :
 ANIMEPLAY ( Ii1II1I11i1 )
 if 85 - 85: iI11I1II1I1I - Ii11Ii1I * I1ii11iIi11i . OoOo00o + IIIi
elif IIi11II1II111 == 1001 :
 ooOOo0O0o00o00 ( )
 if 13 - 13: o0o00Oo0O + iI11I1II1I1I % IIiIiII11i + iI11I1II1I1I
elif IIi11II1II111 == 1005 :
 IIIi11i ( )
 if 85 - 85: oOo0O0Ooo * iI11I1II1I1I . o0oOO0O00o0O / o0oOO0O00o0O
elif IIi11II1II111 == 1007 :
 oooOOoo0 ( Ii1II1I11i1 )
 if 43 - 43: oOo0O0Ooo
elif IIi11II1II111 == 1010 :
 o00OoOOoO ( Ii1II1I11i1 )
 if 78 - 78: oO0o % IIiIiII11i + OOooOOo / oOo0O0Ooo
elif IIi11II1II111 == 1011 :
 OOI1III1I11I1 ( Ii1II1I11i1 )
 if 34 - 34: I11i % Ii1I + Ii11Ii1I * iI1iI1I1i1I / OoOo00o
elif IIi11II1II111 == 1012 :
 oooiI1i ( Ii1II1I11i1 )
 if 18 - 18: O0OoO
elif IIi11II1II111 == 1030 :
 oO000OoO00OoO ( )
 if 92 - 92: oO0o % iI11I1II1I1I / OooO0OoOOOO * o0oOO0O00o0O . ooOoO0O00 + OoOo00o
elif IIi11II1II111 == 1031 :
 I1IiIi1iiI ( Ii1II1I11i1 , iI1IOooOoOo )
 if 24 - 24: OooO0OoOOOO . o0oOO0O00o0O * OooO0OoOOOO % Ii . Ii + ooOoO0O00
elif IIi11II1II111 == 1032 :
 OO00o0oo ( Ii1II1I11i1 )
 if 64 - 64: iI11I1II1I1I / OooO0OoOOOO / I1ii11iIi11i - Ii1I
elif IIi11II1II111 == 1006 :
 Parse . ParseURL ( Ii1II1I11i1 )
 if 100 - 100: OooO0OoOOOO + ooOoO0O00 * oO0o
elif IIi11II1II111 == 2030 :
 Parse . addonParseURL ( Ii1II1I11i1 )
 if 64 - 64: OoOo00o * Ii . I1ii11iIi11i
elif IIi11II1II111 == 2031 :
 Parse . apkParseURL ( Ii1II1I11i1 )
 if 52 - 52: I1ii11iIi11i / O0OoO / o0oOO0O00o0O - I11i / o0oOO0O00o0O
elif IIi11II1II111 == 1002 :
 o0oO00oooo ( Ii1II1I11i1 )
 if 74 - 74: ooOoO0O00 . iI11I1II1I1I
elif IIi11II1II111 == 1003 :
 ooo0Oo00O ( Ii1II1I11i1 , iI1IOooOoOo )
 if 85 - 85: oOo0O0Ooo
elif IIi11II1II111 == 1004 :
 I1iII1 ( Ii1II1I11i1 )
 if 10 - 10: o0o00Oo0O . IIiIiII11i / ii
elif IIi11II1II111 == 1008 :
 IiiIiiIIII ( )
 if 72 - 72: ii . I11i + o0o00Oo0O
elif IIi11II1II111 == 1009 :
 M3UPLAY ( Ii1II1I11i1 )
 if 46 - 46: OOooOOo * iI1iI1I1i1I / OoOo00o + I1ii11iIi11i + OooO0OoOOOO
elif IIi11II1II111 == 2001 :
 IIIIIIi1IIi1I11i ( Ii1II1I11i1 )
 if 95 - 95: I11i - Ii11Ii1I
elif IIi11II1II111 == 2002 :
 o0Ii11I1iIIi ( Ii1II1I11i1 )
 if 67 - 67: Ii1I * I1ii11iIi11i % I11i
elif IIi11II1II111 == 1013 :
 i1I11iIII1i1I ( )
 if 19 - 19: OOooOOo . IIIii1II1II . ii
elif IIi11II1II111 == 1014 :
 oOo ( )
 if 79 - 79: IIIii1II1II * O0OoO * oOo0O0Ooo * Ii1I / Ii1I
elif IIi11II1II111 == 1015 :
 oOOoO0oO0oo0O ( Ii1II1I11i1 )
 if 62 - 62: O0OoO * Ii11Ii1I % Ii1I - ooOoO0O00 - Ii1I
elif IIi11II1II111 == 1016 :
 i1IIIi1Iii1i ( Ii1II1I11i1 , iI1IOooOoOo , ooo )
 if 24 - 24: IIIii1II1II
elif IIi11II1II111 == 1017 :
 Ii1I1i ( )
 if 71 - 71: OooO0OoOOOO - ooOoO0O00
elif IIi11II1II111 == 1023 :
 I1I1i1I ( )
 if 56 - 56: OOooOOo + OoOo00o
elif IIi11II1II111 == 1024 :
 OOoOo ( Ii1II1I11i1 )
 if 74 - 74: o0oOO0O00o0O / IIIi / IIiIiII11i - o0oOO0O00o0O / OoOo00o % iI1iI1I1i1I
elif IIi11II1II111 == 1025 :
 Iiiiiii11IIiI ( Ii1II1I11i1 )
 if 19 - 19: OooO0OoOOOO % ii + ii
elif IIi11II1II111 == 4001 :
 iI1I ( )
 if 7 - 7: ooOoO0O00
elif IIi11II1II111 == 4002 :
 oOiI ( )
 if 91 - 91: OOooOOo - OOooOOo . OooO0OoOOOO
elif IIi11II1II111 == 4003 :
 O0Oo00 ( )
 if 33 - 33: IIIi - iI11I1II1I1I / Ii11Ii1I % o0o00Oo0O
elif IIi11II1II111 == 4004 :
 OO ( )
 if 80 - 80: OooO0OoOOOO % ii - OooO0OoOOOO
elif IIi11II1II111 == 4005 :
 I11iiI1i1 ( )
 if 27 - 27: IIIi - I11i * Ii1I - oOo0O0Ooo
elif IIi11II1II111 == 4006 :
 I1i1Iiiii ( )
 if 22 - 22: I1ii11iIi11i % ii - I1ii11iIi11i - o0oOO0O00o0O . Ii11Ii1I
elif IIi11II1II111 == 4007 :
 oOO00O ( )
 if 100 - 100: IIiIiII11i / IIIi / o0oOO0O00o0O - Ii1I * iI11I1II1I1I
elif IIi11II1II111 == 4008 :
 OOOoo0OO ( )
 if 7 - 7: ooOoO0O00 . OooO0OoOOOO % Ii * Ii1I . iI1iI1I1i1I % Ii1I
elif IIi11II1II111 == 4009 : iIiIIi1 ( )
elif IIi11II1II111 == 4010 : oooooOOO000Oo ( )
elif IIi11II1II111 == 3000 :
 I1i1ii1ii ( )
 if 35 - 35: oOo0O0Ooo
elif IIi11II1II111 == 3001 :
 Ooi1IIii11i1I1 ( )
 if 48 - 48: ii % ii - oO0o . OOooOOo
elif IIi11II1II111 == 3002 :
 Ii1I1 ( Ii1II1I11i1 )
 if 22 - 22: O0OoO . Ii . ii . ooOoO0O00
elif IIi11II1II111 == 3003 :
 O0oo00oOOO0o ( Ii1II1I11i1 )
 if 12 - 12: OOooOOo % IIIii1II1II + OoOo00o . o0o00Oo0O % iI11I1II1I1I
elif IIi11II1II111 == 3004 :
 I111iiIIiI1I ( Ii1II1I11i1 )
 if 41 - 41: ii
elif IIi11II1II111 == 404 :
 iI1III ( ooo , Ii1II1I11i1 , iI1IOooOoOo )
 if 13 - 13: iI1iI1I1i1I + IIIi - IIIi % OoOo00o / iI1iI1I1i1I
elif IIi11II1II111 == 405 :
 IiII111I ( Ii1II1I11i1 )
 if 4 - 4: oOo0O0Ooo + IIIii1II1II - OooO0OoOOOO + o0oOO0O00o0O
elif IIi11II1II111 == 7030 :
 I1iIIi ( )
 if 78 - 78: Ii11Ii1I
elif IIi11II1II111 == 7021 :
 o0o0oO0OOO ( ooo )
 if 29 - 29: IIiIiII11i
elif IIi11II1II111 == 7022 :
 IiOO0OOOOOo ( ooo )
 if 79 - 79: iI11I1II1I1I - Ii + O0OoO - IIiIiII11i . iI11I1II1I1I
elif IIi11II1II111 == 7000 :
 O00oooO00oo ( ooo , Ii1II1I11i1 , img )
 if 84 - 84: I1ii11iIi11i % iI1iI1I1i1I * o0o00Oo0O * iI1iI1I1i1I
elif IIi11II1II111 == 7050 :
 iIiI1I1 ( Ii1II1I11i1 )
 if 66 - 66: IIIii1II1II / iI11I1II1I1I - OOooOOo % o0o00Oo0O . O0OoO
elif IIi11II1II111 == 7051 :
 O0OOoOoo0OOo ( Ii1II1I11i1 )
 if 12 - 12: I1ii11iIi11i + oOo0O0Ooo
elif IIi11II1II111 == 7052 :
 i11111 ( Ii1II1I11i1 )
 if 37 - 37: ooOoO0O00 * Ii
elif IIi11II1II111 == 7053 :
 o0o00OoOo0 ( Ii1II1I11i1 )
 if 95 - 95: Ii % IIIi * I1ii11iIi11i + ooOoO0O00 . o0o00Oo0O + Ii1I
elif IIi11II1II111 == 7054 :
 CoolPlay ( Ii1II1I11i1 )
 if 7 - 7: oO0o * Ii * iI11I1II1I1I / IIIii1II1II / IIIi
elif IIi11II1II111 == 7060 :
 I11i1I11iIii ( )
 if 35 - 35: o0oOO0O00o0O * IIIii1II1II
elif IIi11II1II111 == 7061 :
 iI1111i1i1ii ( Ii1II1I11i1 )
 if 65 - 65: IIiIiII11i % ooOoO0O00
elif IIi11II1II111 == 7063 :
 O0OOo ( Ii1II1I11i1 )
 if 13 - 13: oO0o * IIIi + I1ii11iIi11i - OooO0OoOOOO
elif IIi11II1II111 == 7062 :
 i1I1iiii1Ii11 ( Ii1II1I11i1 )
 if 31 - 31: oO0o
elif IIi11II1II111 == 7064 :
 NATatozcat ( )
 if 68 - 68: oO0o + ooOoO0O00 / iI11I1II1I1I + IIiIiII11i * iI11I1II1I1I + Ii1I
elif IIi11II1II111 == 7067 :
 iI1 ( Ii1II1I11i1 )
 if 77 - 77: Ii - IIIi . Ii1I % I1ii11iIi11i . Ii11Ii1I
elif IIi11II1II111 == 7066 :
 NATatozA ( Ii1II1I11i1 )
 if 9 - 9: I11i
elif IIi11II1II111 == 7065 :
 iIIII1 ( Ii1II1I11i1 )
 if 55 - 55: IIIii1II1II % iI11I1II1I1I + iI1iI1I1i1I . O0OoO
elif IIi11II1II111 == 7070 :
 Iii1I ( )
 if 71 - 71: Ii / ooOoO0O00 + OOooOOo
elif IIi11II1II111 == 7071 :
 DIZIlist ( Ii1II1I11i1 )
 if 23 - 23: Ii
elif IIi11II1II111 == 7072 :
 DIZIpull ( Ii1II1I11i1 )
 if 88 - 88: IIiIiII11i - o0oOO0O00o0O / ii
elif IIi11II1II111 == 7073 :
 WATCHDIZI ( Ii1II1I11i1 )
 if 71 - 71: Ii1I
elif IIi11II1II111 == 7002 :
 Ii1iii11I ( )
 if 19 - 19: I1ii11iIi11i - oO0o + Ii / iI11I1II1I1I
elif IIi11II1II111 == 7003 :
 IIIiII11 ( Ii1II1I11i1 )
 if 1 - 1: OooO0OoOOOO % ooOoO0O00
elif IIi11II1II111 == 7004 :
 Iii1Iii ( Ii1II1I11i1 )
 if 41 - 41: oO0o * oO0o / o0oOO0O00o0O + Ii1I . I11i
elif IIi11II1II111 == 7020 :
 o0oO0oOooO ( Ii1II1I11i1 )
 if 84 - 84: Ii + oO0o * oOo0O0Ooo + Ii1I / Ii11Ii1I
elif IIi11II1II111 == 7001 :
 Oo0o0oo0 ( )
 if 80 - 80: Ii1I
elif IIi11II1II111 == 7010 :
 Iii1IIII1Iii ( Ii1II1I11i1 )
 if 67 - 67: IIiIiII11i
elif IIi11II1II111 == 7011 :
 OO00OoOO ( Ii1II1I11i1 )
 if 2 - 2: I11i - o0o00Oo0O * Ii11Ii1I % OooO0OoOOOO
elif IIi11II1II111 == 7012 :
 OOOOO0oO0 ( Ii1II1I11i1 )
 if 64 - 64: ooOoO0O00 . O0OoO
elif IIi11II1II111 == 7013 :
 cnfTVPlay2 ( Ii1II1I11i1 )
elif IIi11II1II111 == 7014 :
 CNF_Studio_Indexer . MV_Movies ( Ii1II1I11i1 )
elif IIi11II1II111 == 7015 :
 CNF_Studio_Indexer . Movie_ByYear ( Ii1II1I11i1 )
elif IIi11II1II111 == 7016 :
 CNF_Studio_Indexer . Resolve_CNF_Link ( ooo , Ii1II1I11i1 , iI1IOooOoOo )
elif IIi11II1II111 == 7017 :
 CNF_Studio_Indexer . Search_Movie ( )
elif IIi11II1II111 == 7018 :
 oO0oOOooO0 ( )
elif IIi11II1II111 == 7019 :
 CNF_Studio_Indexer . List_Movies ( Ii1II1I11i1 )
elif IIi11II1II111 == 7020 :
 CNF_Studio_Indexer . Get_Movie_Page ( Ii1II1I11i1 )
elif IIi11II1II111 == 7024 :
 CNF_Studio_Indexer . Box_Office ( Ii1II1I11i1 )
 if 7 - 7: OoOo00o . o0oOO0O00o0O - o0oOO0O00o0O / IIIi % I1ii11iIi11i
elif IIi11II1II111 == 8000 :
 IIi1i1I11IIII ( )
elif IIi11II1II111 == 8001 :
 oO0OOoo ( )
elif IIi11II1II111 == 8002 :
 ooO00OoO0o0OO ( )
elif IIi11II1II111 == 8003 :
 iiIIIi1iIi ( )
elif IIi11II1II111 == 8004 :
 o00oOoo0o00 ( )
elif IIi11II1II111 == 8005 :
 iIi11III ( )
elif IIi11II1II111 == 8006 :
 i1iI1IIi1I ( ooo , Ii1II1I11i1 )
elif IIi11II1II111 == 8030 :
 IiI1I11iIii ( Ii1II1I11i1 )
elif IIi11II1II111 == 8045 :
 II111I1Iii ( Ii1II1I11i1 )
elif IIi11II1II111 == 8046 :
 OO00Oo00oO ( Ii1II1I11i1 )
elif IIi11II1II111 == 8047 :
 I1iII ( Ii1II1I11i1 )
elif IIi11II1II111 == 8020 :
 iiiiI1iiiIi11 ( )
elif IIi11II1II111 == 8021 :
 O0oOOO0o0Ooo ( Ii1II1I11i1 )
elif IIi11II1II111 == 8022 :
 i1iIII1IIi ( Ii1II1I11i1 )
elif IIi11II1II111 == 8023 :
 Oo0oo0OOO0OOoOO ( Ii1II1I11i1 )
elif IIi11II1II111 == 8040 :
 OoiiI1i111 ( )
elif IIi11II1II111 == 8041 :
 oO0O0o0O ( Ii1II1I11i1 )
elif IIi11II1II111 == 8042 :
 iiiI ( Ii1II1I11i1 )
elif IIi11II1II111 == 8043 :
 yt . PlayVideo ( Ii1II1I11i1 )
elif IIi11II1II111 == 8044 :
 iIIIiiiIiI1 ( Ii1II1I11i1 )
elif IIi11II1II111 == 8060 :
 oOOoOOO0oOoo ( )
elif IIi11II1II111 == 8061 :
 o0O0ooooooo00 ( Ii1II1I11i1 )
elif IIi11II1II111 == 8064 :
 iIII1iIi ( )
elif IIi11II1II111 == 8065 :
 o000O0oo ( Ii1II1I11i1 )
elif IIi11II1II111 == 8070 :
 o0O0Ooo ( )
elif IIi11II1II111 == 8071 :
 O0o ( Ii1II1I11i1 )
elif IIi11II1II111 == 7080 :
 O00oOOooO ( Ii1II1I11i1 )
elif IIi11II1II111 == 8090 :
 OoO000Oo0oO ( )
elif IIi11II1II111 == 8091 :
 iiiIiiiI1 ( Ii1II1I11i1 )
elif IIi11II1II111 == 8092 :
 I1IIIIIi1IIiI ( Ii1II1I11i1 )
elif IIi11II1II111 == 8081 :
 IIII1I ( )
elif IIi11II1II111 == 8062 :
 IiiIi1I11 ( Ii1II1I11i1 )
elif IIi11II1II111 == 8063 :
 Oooo0O0Oooo ( Ii1II1I11i1 )
elif IIi11II1II111 == 8050 :
 iii1III1i ( )
elif IIi11II1II111 == 8051 :
 iiiIi ( Ii1II1I11i1 )
elif IIi11II1II111 == 8052 :
 II1Iii ( Ii1II1I11i1 )
elif IIi11II1II111 == 8085 :
 ii1IiIi1i ( )
elif IIi11II1II111 == 8086 :
 i11i11i ( Ii1II1I11i1 )
elif IIi11II1II111 == 8087 :
 OOoo00O000Oo ( Ii1II1I11i1 )
elif IIi11II1II111 == 8088 :
 OOoO0oooo ( Ii1II1I11i1 , ooo )
elif IIi11II1II111 == 9000 :
 IioO0oOOO0Ooo ( )
elif IIi11II1II111 == 1111 :
 i1Io00OOOo ( )
elif IIi11II1II111 == 9001 :
 o0OOOOOo00 ( )
elif IIi11II1II111 == 9002 :
 O0O00oO0OoO0o ( )
elif IIi11II1II111 == 9003 :
 ooOoOoO0 ( )
elif IIi11II1II111 == 50 :
 IIiI1I1 ( Ii1II1I11i1 )
elif IIi11II1II111 == 9020 :
 champlist ( )
elif IIi11II1II111 == 9021 :
 iii11i1i1 ( )
elif IIi11II1II111 == 9022 :
 o00OOo0o ( )
elif IIi11II1II111 == 9023 :
 IiIiI ( )
elif IIi11II1II111 == 9024 :
 O0oo0000o ( Ii1II1I11i1 )
elif IIi11II1II111 == 9030 :
 OoO00oo0 ( Ii1II1I11i1 )
elif IIi11II1II111 == 9031 :
 oOOO ( Ii1II1I11i1 )
elif IIi11II1II111 == 9032 :
 o00OoOooo ( Ii1II1I11i1 )
elif IIi11II1II111 == 9033 :
 i1I1ii1 ( Ii1II1I11i1 )
elif IIi11II1II111 == 7085 :
 i11IiIi ( Ii1II1I11i1 )
elif IIi11II1II111 == 7086 :
 OoiIiiII ( Ii1II1I11i1 )
elif IIi11II1II111 == 7087 :
 o0OOoOooO0ooO ( I1o0OooOOOOOO )
elif IIi11II1II111 == 9666 :
 IiIiiiiI1 ( Ii1II1I11i1 )
elif IIi11II1II111 == 10100 : oOIiiIIi ( )
elif IIi11II1II111 == 10105 : oOoOo0o00o ( Ii1II1I11i1 )
elif IIi11II1II111 == 10106 : ooO0 ( Ii1II1I11i1 )
elif IIi11II1II111 == 10104 : IIi11 ( Ii1II1I11i1 )
elif IIi11II1II111 == 10107 : oOoO ( )
elif IIi11II1II111 == 10103 : iIO0OO0o0O00oO ( Ii1II1I11i1 )
elif IIi11II1II111 == 10108 : II1iO00Oo ( Ii1II1I11i1 )
elif IIi11II1II111 == 10107 : oOoO ( )
elif IIi11II1II111 == 10000 : Origin_Menu ( )
elif IIi11II1II111 == 10001 : o00OOo ( )
elif IIi11II1II111 == 10002 : oOOOOOo ( )
elif IIi11II1II111 == 10003 : ooOOoOo ( )
elif IIi11II1II111 == 10004 : ooOo0O0O0oOO0 ( Ii1II1I11i1 )
elif IIi11II1II111 == 10005 : iIi1iIIIiIiI ( )
elif IIi11II1II111 == 10006 : Ii1iI ( Ii1II1I11i1 )
elif IIi11II1II111 == 10007 : IIii1 ( Ii1II1I11i1 , iI1IOooOoOo )
elif IIi11II1II111 == 10008 : iiiiIii ( )
elif IIi11II1II111 == 10009 : ii11iiI11I ( )
elif IIi11II1II111 == 10010 : iiIi11i1IiI ( Ii1II1I11i1 )
elif IIi11II1II111 == 10011 : ooOii1i11 ( Ii1II1I11i1 )
elif IIi11II1II111 == 10012 : i1iii11 ( Ii1II1I11i1 )
elif IIi11II1II111 == 10013 : iIIi1IiIi ( Ii1II1I11i1 )
elif IIi11II1II111 == 10014 : iI1II1I1I ( )
elif IIi11II1II111 == 10015 : iI11Ii111 ( )
elif IIi11II1II111 == 10016 : ooO ( Ii1II1I11i1 )
elif IIi11II1II111 == 10017 : iIiIii1ii ( )
elif IIi11II1II111 == 10018 : iii1 ( )
elif IIi11II1II111 == 10019 : ooo0O0o0OoOO ( )
elif IIi11II1II111 == 10020 : IIIIIIi1i ( )
elif IIi11II1II111 == 10021 : I1iIIIiI ( )
elif IIi11II1II111 == 10022 : ii1iIi1Ii1 ( Ii1II1I11i1 )
elif IIi11II1II111 == 10023 : oooO00O ( ooo , Ii1II1I11i1 )
elif IIi11II1II111 == 10024 : i1I1iI ( Ii1II1I11i1 )
elif IIi11II1II111 == 10025 : III1I1 ( )
elif IIi11II1II111 == 10026 : Iiii1iiiIiI1 ( )
elif IIi11II1II111 == 10027 : OOOo ( )
elif IIi11II1II111 == 10028 : o00ooo0 ( )
elif IIi11II1II111 == 10029 : OOoO0oo0O ( )
elif IIi11II1II111 == 423 : iiIiII11i1 ( Ii1II1I11i1 )
elif IIi11II1II111 == 426 : II1ii1ii11I1 ( Ii1II1I11i1 )
elif IIi11II1II111 == 10030 : Izle_Films ( )
elif IIi11II1II111 == 10031 : Latest_Izle_Movies ( )
elif IIi11II1II111 == 10032 : Izle_Genres ( )
elif IIi11II1II111 == 10033 : Izle_Pop_Movies ( )
elif IIi11II1II111 == 10034 : Izle_Boxsets ( )
elif IIi11II1II111 == 10035 : Izle_Search ( )
elif IIi11II1II111 == 10036 : Izle_Genres_Movie ( Ii1II1I11i1 )
elif IIi11II1II111 == 10037 : Izle_Boxset_single ( Ii1II1I11i1 )
elif IIi11II1II111 == 10038 : Izle_IFRAME ( )
elif IIi11II1II111 == 10039 : Izle_Boxsets_Next ( Ii1II1I11i1 )
elif IIi11II1II111 == 10040 : I1111III11 ( )
elif IIi11II1II111 == 10041 : i1iIIII1iiIIi ( Ii1II1I11i1 )
elif IIi11II1II111 == 10042 : OooOo ( Ii1II1I11i1 )
elif IIi11II1II111 == 10043 : III1III11II ( )
elif IIi11II1II111 == 10044 : oOoO0ooO0000 ( Ii1II1I11i1 )
elif IIi11II1II111 == 10045 : Iiii1I ( ooo )
elif IIi11II1II111 == 10046 : I1iIiiiI1 ( Ii1II1I11i1 )
elif IIi11II1II111 == 10047 : o0oO0OO00oo0o ( Ii1II1I11i1 )
elif IIi11II1II111 == 10048 : i11i11II11i ( Ii1II1I11i1 )
elif IIi11II1II111 == 10049 : OOooOooo0OOo0 ( Ii1II1I11i1 )
elif IIi11II1II111 == 10050 : I11111ii1i ( )
elif IIi11II1II111 == 10051 : OO0oO0Oo ( )
elif IIi11II1II111 == 10052 : o00ii11iiIIII ( )
elif IIi11II1II111 == 10053 : Addon ( Ii1II1I11i1 )
elif IIi11II1II111 == 10054 : OOoOo0O0 ( Ii1II1I11i1 , ooo )
elif IIi11II1II111 == 10055 :
 o00OoooooooOo ( "addFavorite" )
 try :
  ooo = ooo . split ( '\\ ' ) [ 1 ]
 except :
  pass
 try :
  ooo = ooo . split ( '  - ' ) [ 0 ]
 except :
  pass
 iIiIi1Ii11IiI1I1 ( ooo , Ii1II1I11i1 , iI1IOooOoOo , III1I1Iii1iiI , OooO00Oo )
elif IIi11II1II111 == 10056 :
 o00OoooooooOo ( "rmFavorite" )
 try :
  ooo = ooo . split ( '\\ ' ) [ 1 ]
 except :
  pass
 try :
  ooo = ooo . split ( '  - ' ) [ 0 ]
 except :
  pass
 O0o00oO0oOO ( ooo )
elif IIi11II1II111 == 10057 :
 o00OoooooooOo ( "getFavorites" )
 O00O0 ( )
elif IIi11II1II111 == 10058 : oOOO0oo0 ( )
elif IIi11II1II111 == 10059 : Donators_Guide ( )
elif IIi11II1II111 == 10060 : iIiIIIIIii ( )
elif IIi11II1II111 == 10061 : II11iI111i1 ( )
elif IIi11II1II111 == 10062 : I1iii11 ( ooo , Ii1II1I11i1 , I1o0OooOOOOOO )
elif IIi11II1II111 == 10063 : I111i1II ( )
elif IIi11II1II111 == 10064 : O0o0O0 ( )
elif IIi11II1II111 == 10065 : IIII1 ( Ii1II1I11i1 )
elif IIi11II1II111 == 10066 : Iii1iiIi1II ( Ii1II1I11i1 )
elif IIi11II1II111 == 10068 : iiI1iI111ii1i ( Ii1II1I11i1 )
elif IIi11II1II111 == 10069 : oOoO00oo0O ( Ii1II1I11i1 )
elif IIi11II1II111 == 10070 : oOOoo0000O0o0 ( Ii1II1I11i1 )
elif IIi11II1II111 == 10071 : Genie_Watch ( )
elif IIi11II1II111 == 10072 : iI1111ii1I ( )
elif IIi11II1II111 == 10073 : oooO ( Ii1II1I11i1 )
elif IIi11II1II111 == 10074 : i111iIi1i1II1 ( Ii1II1I11i1 )
elif IIi11II1II111 == 10075 : iII1iIi11i ( iI1IOooOoOo , ooo , Ii1II1I11i1 )
elif IIi11II1II111 == 10076 : O0OoooO0 ( Ii1II1I11i1 )
elif IIi11II1II111 == 10077 : IIIii11 ( Ii1II1I11i1 )
elif IIi11II1II111 == 10078 : OOO ( )
elif IIi11II1II111 == 10079 : Genie_Watch_Tv_Shows ( )
elif IIi11II1II111 == 10080 : Genie_Watch_Tv_Genre ( Ii1II1I11i1 )
elif IIi11II1II111 == 10081 : Genie_Watch_TV_PlayRun ( Ii1II1I11i1 )
elif IIi11II1II111 == 10082 : Genie_Watch_TV_Episodes ( Ii1II1I11i1 , iI1IOooOoOo )
elif IIi11II1II111 == 10083 : Genie_Watch_Tv_Recent ( Ii1II1I11i1 )
elif IIi11II1II111 == 10084 : oO0O0OO0O ( )
elif IIi11II1II111 == 10085 : oo00O00oO ( )
elif IIi11II1II111 == 10086 : oo0OOo ( )
elif IIi11II1II111 == 20000 : iIIi1I ( )
elif IIi11II1II111 == 20001 : OO0 ( )
elif IIi11II1II111 == 20002 : i11i1Ii1 ( Ii1II1I11i1 )
elif IIi11II1II111 == 20003 : o0oo0000 ( Ii1II1I11i1 )
elif IIi11II1II111 == 20004 : OO0Oooo0oo ( Ii1II1I11i1 )
elif IIi11II1II111 == 21004 : I1i1I ( )
elif IIi11II1II111 == 21005 : iii1I1Iii ( Ii1II1I11i1 )
elif IIi11II1II111 == 21006 : Oo0oOooOoOo ( Ii1II1I11i1 )
elif IIi11II1II111 == 21007 : IiI1ii1Ii ( Ii1II1I11i1 )
elif IIi11II1II111 == 30000 : ooO0o ( )
elif IIi11II1II111 == 30001 : Ii1iIi111i1i1 ( )
elif IIi11II1II111 == 10012 : Resolve ( Ii1II1I11i1 )
elif IIi11II1II111 == 30003 : IiII1iiIiI ( )
elif IIi11II1II111 == 30004 : oOo0OooOo ( Ii1II1I11i1 )
elif IIi11II1II111 == 30005 : IiiIiiIi ( Ii1II1I11i1 )
elif IIi11II1II111 == 30006 : I11Ii ( )
elif IIi11II1II111 == 30007 : oo00IIIIIIIiI ( )
elif IIi11II1II111 == 30008 : i1i1IiIiIi1Ii ( Ii1II1I11i1 )
elif IIi11II1II111 == 30009 : oo00ooOoo ( Ii1II1I11i1 )
elif IIi11II1II111 == 30010 : o00oo0000 ( Ii1II1I11i1 )
elif IIi11II1II111 == 30011 : IIIIIiII1 ( )
elif IIi11II1II111 == 30012 : i1oO ( )
elif IIi11II1II111 == 30013 : I11i11I1iiII ( )
elif IIi11II1II111 == 30014 : o0O0OO ( )
elif IIi11II1II111 == 30015 : iIiI ( Ii1II1I11i1 , iI1IOooOoOo , III1I1Iii1iiI )
elif IIi11II1II111 == 30016 : ii1I11iIiIII1 ( Ii1II1I11i1 )
elif IIi11II1II111 == 30019 : IIIii1iiIi ( Ii1II1I11i1 )
elif IIi11II1II111 == 30017 : OoOo0OOOoOo ( Ii1II1I11i1 )
elif IIi11II1II111 == 30018 : I11IIIiIi11 ( Ii1II1I11i1 )
if 61 - 61: OoOo00o - Ii1I / o0oOO0O00o0O % Ii1I + oO0o / I1ii11iIi11i
xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
