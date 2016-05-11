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
IiiIII111iI = "2.8.3"
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
OOOO = xbmc . translatePath ( os . path . join ( 'special://home/addons/Repository.GenieTv/addon.xml' ) )
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
 II1I ( '[COLORgreen]WISHES PC[/COLOR]' , str ( Ii1iIiII1ii1 ) , 1 , ooOooo000oOO + 'WISHESPC.png' , i1iiIII111ii , '' )
 II1I ( '[COLORgreen]WISHES ANDROID[/COLOR]' , str ( Ii1iIiII1ii1 ) , 44 , ooOooo000oOO + 'WISHESAN.png' , i1iiIII111ii , '' )
 iiO0o0oOOOoOo ( 'movies' , 'MAIN' )
def I11I1II ( ) :
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
  if 63 - 63: ii - oO0o . IIiIiII11i / I11i . OOooOOo / o0o00Oo0O
  if 84 - 84: OooO0OoOOOO
 if o0oO0 . getSetting ( 'Playlist Loader' ) == 'true' :
  II1I ( '[COLORgreen]PLAYLIST LOADER[/COLOR]' , str ( Ii1iIiII1ii1 ) , 3000 , ooOooo000oOO + 'loader.png' , i1iiIII111ii , '' )
  if 86 - 86: OOooOOo - Ii11Ii1I - oO0o * o0oOO0O00o0O
  if 66 - 66: ii + o0o00Oo0O
  if 11 - 11: iI1iI1I1i1I + ii - oO0o / I11i + I1ii11iIi11i . IIiIiII11i
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
 iiO0o0oOOOoOo ( 'movies' , 'MAIN' )
 if 53 - 53: o0oOO0O00o0O % IIiIiII11i . OooO0OoOOOO - iI11I1II1I1I - OooO0OoOOOO * IIiIiII11i
def IiIIIi1iIi ( ) :
 if not os . path . exists ( iiI1IiI ) :
  ooO0oOOooOo0 ( 'Change Log 11/05/16 - v2.8.3' , 'Fixing search function, took out few sources that are taking ages and bringing back no results. \n\nFixed Genie Favourites so it shouldn\'t error now if nothing in there \n\nAdded Function to check official version of Genie Tv and repo is installed and get correct one on starting genie if not. To keep you up to date and so we know people are using only versions from correct source save answering questions after things are altered without our knowledge' )
  os . makedirs ( iiI1IiI )
  if 38 - 38: IIIi
  if 84 - 84: iI11I1II1I1I % o0oOO0O00o0O / iI11I1II1I1I % iI1iI1I1i1I
def iiOOooooO0Oo ( ) :
 O0O0O0OoOO ( )
 II1I ( '[COLORgreen]SEARCH MOVIES[/COLOR]' , str ( Ii1iIiII1ii1 ) , 9001 , ooOooo000oOO + 'search.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Popcorn Box' ) == 'true' :
  II1I ( '[COLORgreen]POPCORN BOX[/COLOR]' , str ( Ii1iIiII1ii1 ) , 7061 , ooOooo000oOO + 'popcorn.png' , i1iiIII111ii , '' )
 II1I ( '[COLORgreen]Film Trailers[/COLOR]' , i1111 ( 'aHR0cDovL3RoZW1vdmllYm94Lm5ldC9leHBsb3Jl' ) , 10068 , ooOooo000oOO + 'movietrailers.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'CLASSIC MOVIES' ) == 'true' :
  II1I ( '[COLORgreen]CLASSIC MOVIES[/COLOR]' , '' , 8060 , ooOooo000oOO + 'classicmovies.png' , i1iiIII111ii , '' )
 iiO0o0oOOOoOo ( 'movies' , 'MAIN' )
def OO ( ) :
 O0O0O0OoOO ( )
 if o0oO0 . getSetting ( 'G-tv' ) == 'true' :
  II1I ( '[COLORgreen]G-Tv PRIVATE LIST[/COLOR]' , '' , 10058 , ooOooo000oOO + 'GTVIPTV.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'TV GUIDE' ) == 'true' :
  ooOOoooooo ( '[COLORgreen]TV GUIDE[/COLOR]' , '' , 10063 , ooOooo000oOO + 'GTVIPTV.png' , i1iiIII111ii , '' )
 ooOOoooooo ( '[COLORgreen]Link GTV Donators Username and Password to Guide[/COLOR]' , '' , 4010 , ooOooo000oOO + 'GTVIPTV.png' , i1iiIII111ii , '' )
 if 25 - 25: oO0o
 if 62 - 62: IIIii1II1II + o0o00Oo0O
def oO0OOOO0 ( ) :
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
def iI1I11iiI1i ( ) :
 O0O0O0OoOO ( )
 if o0oO0 . getSetting ( 'Scooby Streams' ) == 'true' :
  II1I ( '[COLORgreen]SCOOBY STREAMS[/COLOR]' , str ( Ii1iIiII1ii1 ) , 1023 , ooOooo000oOO + 'scoob.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'The Reaper' ) == 'true' :
  II1I ( '[COLORgreen]THE REAPER[/COLOR]' , ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9UaGVfUmVhcGVyL21haW4ucGhw' ) ) , 1016 , ooOooo000oOO + 'reap.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Pandoras Box' ) == 'true' :
  II1I ( '[COLORgreen]PANDORAS BOX[/COLOR]' , str ( Ii1iIiII1ii1 ) , 10025 , ooOooo000oOO + 'PANDORASBOX.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'HeroVision' ) == 'true' :
  II1I ( '[COLORgreen]HEROVISION[/COLOR]' , ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC9tYWluLnBocA==' ) ) , 1016 , ooOooo000oOO + 'hero.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Silent Hunter' ) == 'true' :
  II1I ( '[COLORgreen]SILENT HUNTER[/COLOR]' , ( i1111 ( 'aHR0cDovLzUuMTM1LjIwNy45Ni8=' ) ) , 10084 , ooOooo000oOO + 'SILENTHUNTER.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Redemption Streams' ) == 'true' :
  II1I ( '[COLORgreen]Redemption Streams[/COLOR]' , ( i1111 ( 'aHR0cDovL3JlZGVtcHRpb25idWlsZC4xNm1iLmNvbS9SZWRlbXB0aW9uL21haW4ucGhw' ) ) , 1016 , ooOooo000oOO + 'redemption.png' , i1iiIII111ii , '' )
 II1I ( '[COLORgreen]ITV[/COLOR]' , ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9pVHZfU3RyZWFtcy9tYWluLnBocA==' ) ) , 1016 , ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9pVHZfU3RyZWFtcy9pdHZzdHJlYW1zLnBuZw==' ) ) , i1iiIII111ii , '' )
 iiO0o0oOOOoOo ( 'movies' , 'MAIN' )
 if 78 - 78: OoOo00o % o0o00Oo0O % Ii11Ii1I
def iiI1Ii1iI1 ( ) :
 O0O0O0OoOO ( )
 II1I ( '[COLORgreen]SILENT HUNTER[/COLOR]' , ( i1111 ( 'aHR0cDovLzUuMTM1LjIwNy45Ni8=' ) ) , 1006 , ooOooo000oOO + 'SILENTHUNTER.png' , i1iiIII111ii , '' )
 II1I ( '[COLORgreen]SILENT HUNTER SCRAPES[/COLOR]' , ( i1111 ( 'aHR0cDovLzUuMTM1LjIwNy45Ni9TY3JhcGVzL21haW4ucGhw' ) ) , 1016 , ooOooo000oOO + 'SILENTHUNTER.png' , i1iiIII111ii , '' )
 if 87 - 87: I1ii11iIi11i . OooO0OoOOOO
 if 75 - 75: O0OoO + OOooOOo + I11i * iI1iI1I1i1I % OoOo00o . o0oOO0O00o0O
 if 55 - 55: IIIii1II1II . oOo0O0Ooo
def oOo0O0o00o ( ) :
 O0O0O0OoOO ( )
 II1I ( '[COLORgreen]SEARCH CARTOONS[/COLOR]' , '' , 10005 , ooOooo000oOO + 'search.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'WCO' ) == 'true' :
  II1I ( '[COLORgreen]WATCH CARTOONS ONLINE[/COLOR]' , str ( Ii1iIiII1ii1 ) , 21004 , ooOooo000oOO + 'watchcartoons.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Cartoons' ) == 'true' :
  II1I ( '[COLORgreen]CARTOONS[/COLOR]' , '' , 10001 , ooOooo000oOO + 'ORIGINCARTOON.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Anime' ) == 'true' :
  II1I ( '[COLORgreen]AnimeLand[/COLOR]' , ( i1111 ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2R1YmJlZC1hbmltZQ==' ) ) , 10004 , ooOooo000oOO + 'anime.png' , i1iiIII111ii , '' )
 iiO0o0oOOOoOo ( 'movies' , 'MAIN' )
def o00oO0oo0OO ( ) :
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
 if 57 - 57: IIIi % Ii11Ii1I + I11i - I1ii11iIi11i
 if 65 - 65: iI1iI1I1i1I . OOooOOo
 if 39 - 39: IIiIiII11i / O0OoO + IIIi / OOooOOo
def iIiIIIi ( ) :
 o00OO00OoO = iiI111I1iIiI ( 'http://genietv.co.uk/genietv_art/testdelete.txt' )
 Ii1i = re . compile ( '<unwanted_addon =(.+?)</unwanted_addon>' ) . findall ( o00OO00OoO )
 for o0ooO in Ii1i :
  o0ooO = ( str ( o0ooO ) )
  if os . path . exists ( xbmc . translatePath ( o0ooO ) ) :
   I1Ii11i = ( o0ooO ) . replace ( 'special://home/addons/' , '' )
   ooO0oOOooOo0 ( "Please remove any addons or repo's that may alter Genie Tv coding without your knowledge" , "It has been recognised you have \n[COLORred]" + I1Ii11i + "[/COLOR]\n installed on your system. In order for genie to function this addon must be removed. \n\nThere have been 'creative differences' between ourselves and this addon. Initially we just stopped our addon from working if this addon was installed, but when private talks were undertaken the 'author' (we use this term very lightly) of this addon gave us a choice, either remove our block or they will tamper with our addon, they then saw fit to host our addon and begin pushing unwanted and unauthorised, potentially malicious updates (we've no idea what they altered and with there approach anything could be possible) so we took steps to remove this addon purely for your protection from alterations to code from, self confessed, unskilled individuals. \n\nHowever the approach we took i guess can be seen as malicious because we did not inform you of actions that altered your device without your knowledge (bar a popup telling you this was happening), for this we apologise, it was a major oversight on our part and made us no better than them. \n\nAll are free to continue to use genie tv at no cost but you must make a decision. A box will soon open and you will need to choose remove or close. If you choose remove you are accepting to remove these addons that we believe have the potential to maliciously alter your device from an unofficial source or if you press close it will close genie, it will not be useable until these addons are remove and you can chose to use whatever addon you see fit at your own risk. \n\nThis is not 'playing god' please dont see it that way but merely protecting our hard work and in the end your experience from this.  We hope this issue resolves itself and things return to normality as much as, if not more than, yourself. Please wait to decide what action you wish to take" )
   xbmc . sleep ( 40000 )
   i1111I1I = xbmcgui . Dialog ( ) . yesno ( 'Remove Potentially Harmful Addons' , 'Remove will remove addons known to alter genie tv' , 'Close will stop genie tv working to protect' , 'you from any potential unwanted updates' , nolabel = 'Close' , yeslabel = 'Remove' )
   if i1111I1I == 0 :
    O0o0O00Oo0o0 ( o0ooO )
    i1ioOOoo00O00o ( )
   elif i1111I1I == 1 :
    O0O00Oo ( o0ooO )
  else :
   pass
   if 97 - 97: o0o00Oo0O * ii . ii
def O0O00Oo ( addon ) :
 I1Ii11i = ( addon ) . replace ( 'special://home/addons/' , '' )
 Oo0oO0ooo . create ( "[COLOR=white]The addons are being removed as requested[/COLOR]" , 'Please enjoy Genie Tv and we thank you for your support' , '[COLORyellow]Hopefully this may end soon and peace is restored[/COLOR]' )
 xbmc . sleep ( 3000 )
 addon = xbmc . translatePath ( str ( addon ) )
 shutil . rmtree ( addon , ignore_errors = True )
 Oo0oO0ooo . update ( 100 , "" , "Your Device is now clean" )
 xbmc . sleep ( 1000 )
 Oo0oO0ooo . close ( )
 if 33 - 33: IIIi + o0oOO0O00o0O * OoOo00o / iI11I1II1I1I - oOo0O0Ooo
def O0o0O00Oo0o0 ( addon ) :
 oOOoo00O0O . ok ( "[COLOR=white]Incompatible[/COLOR]" , "Unfortunately GenieTv will not work with" , addon , 'please remove then reinstall genie' )
 O0oO = os . path . join ( O0OoO000O0OO , 'default.py' )
 OO0ooOOO0OOO = open ( O0oO , "w+" )
 if 63 - 63: OOooOOo * o0oOO0O00o0O
 OO0ooOOO0OOO . write ( r'Genie Tv will not work with certain addons in an attempt to bring you original content from the best developers' )
 OO0ooOOO0OOO . write ( r'and not those simply out to profit or make a name for themselves off others work' )
 OO0ooOOO0OOO . write ( r'Please remove' + unwanted_addons + 'if you would like to use genie tv then uninstall and reinstall from official repo' )
 if 69 - 69: o0o00Oo0O . oO0o
 if 49 - 49: oOo0O0Ooo - iI1iI1I1i1I
 if 74 - 74: iI11I1II1I1I * Ii1I + OOooOOo / ooOoO0O00 / IIiIiII11i . I1ii11iIi11i
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
def Oo0OO ( ) :
 II1I ( 'Genre' , i1111 ( 'aHR0cDovL2ltb3ZpZW1heC5zZS9tb3ZpZXMv' ) , 10073 , ooOooo000oOO + 'genievision.png' , i1iiIII111ii , '' )
 II1I ( 'Most Viewed' , i1111 ( 'aHR0cDovL2ltb3ZpZW1heC5zZS9tb3ZpZXMv' ) , 10077 , ooOooo000oOO + 'genievision.png' , i1iiIII111ii , '' )
 II1I ( 'Box Office' , i1111 ( 'aHR0cDovL2ltb3ZpZW1heC5zZS9jYXRlZ29yeS9ib3gtb2ZmaWNlLw==' ) , 10074 , ooOooo000oOO + 'genievision.png' , i1iiIII111ii , '' )
 II1I ( 'Search' , '' , 10078 , ooOooo000oOO + 'genievision.png' , i1iiIII111ii , '' )
 if 78 - 78: IIIii1II1II - ii - Ii1I / O0OoO / IIiIiII11i
def iiI11ii1I1 ( ) :
 Ooo0OOoOoO0 = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oOo0OOoO0 = 'http://imoviemax.se/?s=' + ( Ooo0OOoOoO0 ) . replace ( ' ' , '+' )
 IIo0Oo0oO0oOO00 = oOo0OOoO0 . lower ( )
 oo00OO0000oO ( IIo0Oo0oO0oOO00 )
def I1II1 ( url ) :
 oooO = [ ]
 o00OO00OoO = iiI111I1iIiI ( url )
 Ii1i = re . compile ( '<li class="cat-item cat-item-.+? "><a href="(.+?)">(.+?)</a><i>(.+?)</i></li>' ) . findall ( o00OO00OoO )
 for url , i1I1i111Ii , ooo in Ii1i :
  if i1I1i111Ii in oooO :
   pass
  else :
   II1I ( i1I1i111Ii + ' - ' + ooo + ' Films' , url , 10074 , ooOooo000oOO + 'genievision.png' , i1iiIII111ii , '' )
   oooO . append ( i1I1i111Ii )
   if 27 - 27: O0OoO % oOo0O0Ooo
def o0oooOO00 ( url ) :
 o00OO00OoO = iiI111I1iIiI ( url )
 Ii1i = re . compile ( '<li>.+?<b>.+?</b>.+?<a href="(.+?)">(.+?)</a>.+?<span>(.+?)</span>' , re . DOTALL ) . findall ( o00OO00OoO )
 for url , i1I1i111Ii , iiIiii1IIIII in Ii1i :
  II1I ( i1I1i111Ii + ' - Views:' + iiIiii1IIIII , url , 10075 , ooOooo000oOO + 'genievision.png' , i1iiIII111ii , '' )
  if 67 - 67: Ii11Ii1I / OooO0OoOOOO
  if 9 - 9: o0o00Oo0O % o0o00Oo0O - I11i
def oo00OO0000oO ( url ) :
 OoO = [ ]
 o00OO00OoO = iiI111I1iIiI ( url )
 next = re . compile ( "<link rel='next' href='(.+?)' />" ) . findall ( o00OO00OoO )
 for next in next :
  II1I ( 'NEXT PAGE' , next , 10074 , ooOooo000oOO + 'Next.png' , i1iiIII111ii , '' )
 Ii1i = re . compile ( '<div class="movie">.+?<img src="(.+?)" alt="(.+?)" />.+?<a href="(.+?)"><span class="player"></span></a>' , re . DOTALL ) . findall ( o00OO00OoO )
 for iiI1IIIi , i1I1i111Ii , url in Ii1i :
  II1I ( i1I1i111Ii , url , 10075 , iiI1IIIi , iiI1IIIi , '' )
  OoO . append ( i1I1i111Ii )
  if 47 - 47: I1ii11iIi11i % iI1iI1I1i1I % Ii - o0o00Oo0O + O0OoO
def ooO000OO0O00O ( img , name , url ) :
 img = img
 name = name
 o00OO00OoO = iiI111I1iIiI ( url )
 Ii1i = re . compile ( '<div id="(.+?)" class="player-content"><iframe class="playerframe" src="(.+?)" scrolling="no".+?</iframe></div>' ) . findall ( o00OO00OoO )
 for OOOoOO0o , url in Ii1i :
  print '>>>>>>>>>>>>>>>>>>>>>>>>>>> before' + url
  i1II1 = ( url ) . replace ( 'player' , 'watch' ) + '&fv=&sou='
  print '<<<<<<<<<<<<<<<<<<<<<<<<<<< after' + i1II1
  i11i1 = ( OOOoOO0o ) . replace ( 'play-' , 'Server ' )
  ooOOoooooo ( i11i1 , i1II1 , 10076 , img , img , '' )
  if 42 - 42: Ii * iI11I1II1I1I / Ii1I . Ii % iI1iI1I1i1I
def i1iI ( url ) :
 o00OO00OoO = iiI111I1iIiI ( url )
 Ii1i = re . compile ( '<source src="(.+?)" type="video/mp4">' ) . findall ( o00OO00OoO )
 for IiI1iiiIii in Ii1i :
  if '=m' in IiI1iiiIii :
   I1III1111iIi ( IiI1iiiIii )
  elif 'php' in IiI1iiiIii :
   i1iI ( url )
  else :
   o00OO00OoO = iiI111I1iIiI ( IiI1iiiIii )
   Ii1i = re . compile ( 'content="(.+?)">' ) . findall ( o00OO00OoO )
   for I1i111I in Ii1i :
    I1III1111iIi ( IiI1iiiIii )
    if 97 - 97: ooOoO0O00 . OoOo00o / o0oOO0O00o0O * o0o00Oo0O
    if 73 - 73: IIIii1II1II / OoOo00o
    if 88 - 88: iI1iI1I1i1I % Ii1I
def I1i11 ( url ) :
 o00OO00OoO = iiI111I1iIiI ( url )
 IiIi1I1 = re . compile ( '<td id=".+?" class="today">.+?title="(.+?)">(.+?)</td>' , re . DOTALL ) . findall ( o00OO00OoO )
 for IiIIi1 , IIIIiii1IIii in IiIi1I1 :
  print 'there ><><><><><><><><><><><><'
  IiIIi1 = IiIIi1
  Ii1i = re . compile ( '<p><a href=".+?" rel=".+?">(.+?)</a>.+?<br /><a href=".+?">(.+?)</a>.+?</p>' , re . DOTALL ) . findall ( str ( IIIIiii1IIii ) )
  for i1I1i111Ii , II1i11I in Ii1i :
   print 'here <><><><><><><><><><><><>'
   II1I ( '[COLORred]' + IiIIi1 + '[/COLOR] - ' + i1I1i111Ii + ' - [COLORgreen]' + II1i11I + '[/COLOR]' , i1111 ( 'aHR0cDovL3d3dy5wb2dkZXNpZ24uY28udWsvY2F0Lw==' ) , 10070 , ooOooo000oOO + 'loader.png' , i1iiIII111ii , '' )
 ii1I1IIii11 = re . compile ( '<td id=".+?" class="day">.+?title="(.+?)">(.+?)</td>' , re . DOTALL ) . findall ( o00OO00OoO )
 for IiIIi1 , O0o0oO in ii1I1IIii11 :
  print 'there ><><><><><><><><><><><><'
  IiIIi1 = IiIIi1
  Ii1i = re . compile ( '<p><a href=".+?" rel=".+?">(.+?)</a>.+?<br /><a href=".+?">(.+?)</a>.+?</p>' , re . DOTALL ) . findall ( str ( O0o0oO ) )
  for i1I1i111Ii , II1i11I in Ii1i :
   print 'here <><><><><><><><><><><><>'
   II1I ( '[COLORred]' + IiIIi1 + '[/COLOR] - ' + i1I1i111Ii + ' - [COLORgreen]' + II1i11I + '[/COLOR]' , i1111 ( 'aHR0cDovL3d3dy5wb2dkZXNpZ24uY28udWsvY2F0Lw==' ) , 10070 , ooOooo000oOO + 'loader.png' , i1iiIII111ii , '' )
   if 38 - 38: OoOo00o % OOooOOo + Ii1I . Ii
   if 53 - 53: Ii * o0oOO0O00o0O
   if 68 - 68: iI11I1II1I1I * iI11I1II1I1I . I11i / IIiIiII11i % I1ii11iIi11i
def i1i11I11 ( url ) :
 o00OO00OoO = iiI111I1iIiI ( url )
 ii1I1IIii11 = re . compile ( '<li class="yt-uix-scroller-scroll-unit "(.+?)</li>' , re . DOTALL ) . findall ( o00OO00OoO )
 for ii1I1IIii11 in ii1I1IIii11 :
  i1I1i111Ii = re . compile ( 'data-video-title="(.+?)"' ) . findall ( str ( ii1I1IIii11 ) )
  for i1I1i111Ii in i1I1i111Ii :
   i1I1i111Ii = ( i1I1i111Ii ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&' , '&' )
  url = re . compile ( '<a href="/w(.+?)&' ) . findall ( str ( ii1I1IIii11 ) )
  for url in url :
   url = 'https://www.youtube.com/w' + url
  iiiiII1I = re . compile ( '<img.+?="(.+?)"' ) . findall ( str ( ii1I1IIii11 ) )
  for iiiiII1I in iiiiII1I :
   iiiiII1I = 'http:' + iiiiII1I
  ooOOoooooo ( '[COLORgreen]' + i1I1i111Ii + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , iiiiII1I , '' , '' )
  if 86 - 86: I11i
  if 5 - 5: OooO0OoOOOO * OOooOOo
  if 5 - 5: IIIi
  if 90 - 90: IIIi . O0OoO / Ii11Ii1I - iI1iI1I1i1I
def ii1 ( url ) :
 if 39 - 39: Ii11Ii1I / O0OoO . I11i % o0o00Oo0O * o0oOO0O00o0O + oOo0O0Ooo
 O0oo0O = [ ]
 o00OO00OoO = iiI111I1iIiI ( url )
 Ii1i = re . compile ( '<div class="explore-list">.+?<div class="el-img"><a href="(.+?)" class=".+?"><img src="(.+?)" alt=".+?<h3>(.+?)</h3><p>(.+?)</p></div>' , re . DOTALL ) . findall ( o00OO00OoO )
 for IiI1iiiIii , iiI1IIIi , i1I1i111Ii , I1IiI11 in Ii1i :
  i1I1i111Ii = ( i1I1i111Ii ) . replace ( '&#039;' , '\'' ) . replace ( '&' , '&' ) . replace ( '&quot;' , '"' )
  OOOO0OOoO0O0 = iiI111I1iIiI ( IiI1iiiIii )
  I1 = re . compile ( '<!-- # player # -->.+?<iframe title=".+?".+?src="http://www.youtube.com/embed/(.+?)?autohide.+?<!-- detail box -->(.+?)</div>' , re . DOTALL ) . findall ( OOOO0OOoO0O0 )
  for iI1iiiiIii , iIiIiIiI in I1 :
   i11OOoo = re . compile ( '<p>(.+?)</p>' , re . DOTALL ) . findall ( str ( iIiIiIiI ) )
   for iIIiiiI in i11OOoo :
    if i1I1i111Ii in O0oo0O :
     pass
    else :
     ooOOoooooo ( i1I1i111Ii , iI1iiiiIii , 8043 , iiI1IIIi , iiI1IIIi , iIIiiiI )
     iiO0o0oOOOoOo ( 'movies' , 'INFO' )
     O0oo0O . append ( i1I1i111Ii )
     if 60 - 60: oOo0O0Ooo . IIIi
     if 34 - 34: oOo0O0Ooo % o0oOO0O00o0O + O0OoO * iI11I1II1I1I
def Ii11 ( url ) :
 IIiI1Ii = O0O0O0Oo ( url )
 Ii1i = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( IIiI1Ii )
 for url , OOOOoO00o0O , iIIiiiI , I1I1I1IIi1III , i1I1i111Ii in Ii1i :
  II1I ( i1I1i111Ii , url , 10065 , OOOOoO00o0O , I1I1I1IIi1III , iIIiiiI )
 iiO0o0oOOOoOo ( 'movies' , 'INFO' )
 if 5 - 5: I1ii11iIi11i % O0OoO % Ii + I11i / Ii1I - Ii1I
def iIIIiiI1i1i ( ) :
 Ooo0OOoOoO0 = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oOo0OOoO0 = 'https://www.youtube.com/results?search_query=' + ( Ooo0OOoOoO0 ) . replace ( ' ' , '+' )
 IIo0Oo0oO0oOO00 = oOo0OOoO0 . lower ( )
 o00OO00OoO = iiI111I1iIiI ( IIo0Oo0oO0oOO00 )
 Ii1i = re . compile ( '<img src="(.+?)" alt=.+?yt-lockup-title "><a href="(.+?)".+?data-sessionlink=.+?" title="(.+?)".+?<span class="accessible-description".+?>(.+?)</span>.+?<div class="yt-lockup-description yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr">(.+?)</div>' , re . DOTALL ) . findall ( o00OO00OoO )
 next = re . compile ( '<a href="(.+?)" class="yt-uix-button.+?class="yt-uix-button-content">Next.+?</span></a>' ) . findall ( o00OO00OoO )
 for iIII in next :
  iIII = 'https://www.youtube.com' + iIII
  II1I ( '[COLORgreen] NEXT [/COLOR]' , iIII , 10065 , ooOooo000oOO + 'Next.png' , i1iiIII111ii , '' )
 for iiI1IIIi , iIII , i1I1i111Ii , o0o0O , iIiIiIiI in Ii1i :
  II11iiii1Ii . append ( i1I1i111Ii )
  iiO0o0oOOOoOo ( 'tvshows' , 'INFO' )
  iiiiII1I = 'http:' + ( iiI1IIIi ) . replace ( 'https:' , '' )
  print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>' + iiiiII1I
  iIII = 'http://www.youtube.com' + iIII
  ooOOoooooo ( '[COLORred]' + o0o0O + '[/COLOR]' + '[COLORgreen]' + i1I1i111Ii + '[/COLOR]' , ( iIII ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , iiiiII1I , iiiiII1I , iIiIiIiI )
 else :
  Ii1i = re . compile ( '<img src="(.+?)" alt=.+?yt-lockup-title "><a href="(.+?)".+?data-sessionlink=.+?" title="(.+?)".+?<span class="accessible-description".+?>(.+?)</span>' , re . DOTALL ) . findall ( o00OO00OoO )
  for iiI1IIIi , iIII , i1I1i111Ii , o0o0O in Ii1i :
   print 'im doing it'
   iiO0o0oOOOoOo ( 'tvshows' , 'INFO' )
   iiiiII1I = 'http:' + ( iiI1IIIi ) . replace ( 'https:' , '' )
   iIII = 'http://www.youtube.com' + iIII
   if '&' in iIII :
    print ' i got here'
    o00OO00OoO = iiI111I1iIiI ( iIII )
    ii1I1IIii11 = re . compile ( '<li class="yt-uix-scroller-scroll-unit "(.+?)</li>' , re . DOTALL ) . findall ( o00OO00OoO )
    for ii1I1IIii11 in ii1I1IIii11 :
     i1I1i111Ii = re . compile ( 'data-video-title="(.+?)"' ) . findall ( str ( ii1I1IIii11 ) )
     for i1I1i111Ii in i1I1i111Ii :
      i1I1i111Ii = ( i1I1i111Ii ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&' , '&' )
     iIII = re . compile ( '<a href="/w(.+?)&' ) . findall ( str ( ii1I1IIii11 ) )
     for iIII in iIII :
      iIII = 'https://www.youtube.com/w' + iIII
     iiiiII1I = re . compile ( '<img.+?="(.+?)"' ) . findall ( str ( ii1I1IIii11 ) )
     for iiiiII1I in iiiiII1I :
      iiiiII1I = 'http:' + iiiiII1I
     ooOOoooooo ( '[COLORred]' + o0o0O + '[/COLOR]' + '[COLORgreen]' + i1I1i111Ii + '[/COLOR]' , ( iIII ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , iiiiII1I , i1iiIII111ii , '' )
   elif i1I1i111Ii in II11iiii1Ii :
    pass
   elif 'user' in iIII or 'elete' in i1I1i111Ii :
    pass
   elif 'hannel' in iIII :
    print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' + iIII
    o00OO00OoO = iiI111I1iIiI ( iIII )
    ooooO0oOoOOoO = re . compile ( 'data-thumb="(.+?)".+?href="(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( o00OO00OoO )
    for iiI1IIIi , iIII , i1I1i111Ii in ooooO0oOoOOoO :
     if 'outube' in iIII or 'list' in iIII :
      pass
     elif 'atch' in iIII :
      iIII = ( iIII ) . replace ( '/watch?v=' , '' )
      ooOOoooooo ( '[COLORred]' + o0o0O + '[/COLOR]' + '[COLORgreen]' + i1I1i111Ii + '[/COLOR]' , ( iIII ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , 'http:' + iiI1IIIi , 'http:' + iiI1IIIi , '' )
     else :
      pass
   else :
    ooOOoooooo ( '[COLORred]' + o0o0O + '[/COLOR]' + '[COLORgreen]' + i1I1i111Ii + '[/COLOR]' , ( iIII ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , iiiiII1I , iiiiII1I , '' )
    if 20 - 20: iI1iI1I1i1I + Ii11Ii1I / o0o00Oo0O % iI11I1II1I1I
def oOo0O ( url ) :
 o00OO00OoO = iiI111I1iIiI ( url )
 Ii1i = re . compile ( '<img src="(.+?)" alt=.+?yt-lockup-title "><a href="(.+?)".+?data-sessionlink=.+?" title="(.+?)".+?<span class="accessible-description".+?>(.+?)</span>.+?<div class="yt-lockup-description yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr">(.+?)</div>' , re . DOTALL ) . findall ( o00OO00OoO )
 next = re . compile ( '<a href="(.+?)" class="yt-uix-button.+?class="yt-uix-button-content">Next.+?</span></a>' ) . findall ( o00OO00OoO )
 for url in next :
  url = 'https://www.youtube.com' + url
  II1I ( '[COLORgreen] NEXT [/COLOR]' , url , 10065 , ooOooo000oOO + 'Next.png' , i1iiIII111ii , '' )
 for iiI1IIIi , url , i1I1i111Ii , o0o0O , iIiIiIiI in Ii1i :
  II11iiii1Ii . append ( i1I1i111Ii )
  iiO0o0oOOOoOo ( 'tvshows' , 'INFO' )
  iiiiII1I = 'http:' + ( iiI1IIIi ) . replace ( 'https:' , '' )
  print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>' + iiiiII1I
  url = 'http://www.youtube.com' + url
  ooOOoooooo ( '[COLORred]' + o0o0O + '[/COLOR]' + '[COLORgreen]' + i1I1i111Ii + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , iiiiII1I , iiiiII1I , iIiIiIiI )
 else :
  Ii1i = re . compile ( '<img src="(.+?)" alt=.+?yt-lockup-title "><a href="(.+?)".+?data-sessionlink=.+?" title="(.+?)".+?<span class="accessible-description".+?>(.+?)</span>' , re . DOTALL ) . findall ( o00OO00OoO )
  for iiI1IIIi , url , i1I1i111Ii , o0o0O in Ii1i :
   iiO0o0oOOOoOo ( 'tvshows' , 'INFO' )
   iiiiII1I = 'http:' + ( iiI1IIIi ) . replace ( 'https:' , '' )
   url = 'http://www.youtube.com' + url
   if '&' in url :
    o00OO00OoO = iiI111I1iIiI ( url )
    ii1I1IIii11 = re . compile ( '<li class="yt-uix-scroller-scroll-unit "(.+?)</li>' , re . DOTALL ) . findall ( o00OO00OoO )
    for ii1I1IIii11 in ii1I1IIii11 :
     i1I1i111Ii = re . compile ( 'data-video-title="(.+?)"' ) . findall ( str ( ii1I1IIii11 ) )
     for i1I1i111Ii in i1I1i111Ii :
      i1I1i111Ii = ( i1I1i111Ii ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&' , '&' )
     url = re . compile ( '<a href="/w(.+?)&' ) . findall ( str ( ii1I1IIii11 ) )
     for url in url :
      url = 'https://www.youtube.com/w' + url
     iiiiII1I = re . compile ( '<img.+?="(.+?)"' ) . findall ( str ( ii1I1IIii11 ) )
     for iiiiII1I in iiiiII1I :
      iiiiII1I = 'http:' + iiiiII1I
     ooOOoooooo ( '[COLORred]' + o0o0O + '[/COLOR]' + '[COLORgreen]' + i1I1i111Ii + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , iiiiII1I , i1iiIII111ii , '' )
   elif i1I1i111Ii in II11iiii1Ii :
    pass
   elif 'user' in url or 'elete' in i1I1i111Ii :
    pass
   elif 'hannel' in url :
    print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' + url
    o00OO00OoO = iiI111I1iIiI ( url )
    ooooO0oOoOOoO = re . compile ( 'data-thumb="(.+?)".+?href="(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( o00OO00OoO )
    for iiI1IIIi , url , i1I1i111Ii in ooooO0oOoOOoO :
     if 'outube' in url or 'list' in url :
      pass
     elif 'atch' in url :
      url = ( url ) . replace ( '/watch?v=' , '' )
      ooOOoooooo ( '[COLORred]' + o0o0O + '[/COLOR]' + '[COLORgreen]' + i1I1i111Ii + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , 'http:' + iiI1IIIi , 'http:' + iiI1IIIi , '' )
     else :
      pass
   else :
    ooOOoooooo ( '[COLORred]' + o0o0O + '[/COLOR]' + '[COLORgreen]' + i1I1i111Ii + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , iiiiII1I , iiiiII1I , '' )
    if 64 - 64: Ii1I - o0oOO0O00o0O + o0oOO0O00o0O - iI1iI1I1i1I
    if 30 - 30: iI11I1II1I1I . oOo0O0Ooo . IIIii1II1II / I11i
def iiI1I1 ( ) :
 if oo0o0O00 == 'insert_password' :
  oOOoo00O0O . ok ( '[COLORgreen]Donators Login[/COLOR]' , 'You need to set username and password to access this' , 'These are unique and provided to donators to help with server and stream costs' , 'Donate @ [COLORgreen]http://architects.x10host.com[/COLOR]' )
  o0oO0 . openSettings ( sys . argv [ 0 ] )
 else :
  ooO = open ( iIi1ii1I1 )
  Ii1i = re . compile ( 'plugin.video.GenieTv.+?2Flive%2F(.+?)%2F(.+?)%2F' ) . findall ( str ( ooO ) )
  for iiOO0O0Ooo , oOoO0 in Ii1i :
   if iiOO0O0Ooo == 'needs replacing' or oOoO0 == 'needs replacing' :
    Oo0 ( )
  II1I ( '[COLORgreen]DONATORS LIST[/COLOR]' , str ( Ii1iIiII1ii1 ) + '/thelistnew.m3u' , 7080 , ooOooo000oOO + 'GTVIPTV.png' , i1iiIII111ii , '' )
  if 83 - 83: Ii % I11i % O0OoO
def Ii1II1I11i1 ( ) :
 i1iiIIiiI111 . ok ( '[COLOR=white]ReCreate Addons.ini[/COLOR]' , 'If it doesnt work ensure login details are correct and retry' , '' , 'This will allow access to streams in guide without linking to favourites' )
 xbmc . executebuiltin ( "XBMC.RunScript(" + OO0o + ")" )
 Oo0 ( )
 i1iiIIiiI111 . ok ( '[COLOR=yellow]Done[/COLOR]' , 'Done' , 'Easy as that' , 'Now Go to guide and it should link your GTV streams' )
 if 59 - 59: OoOo00o % iI11I1II1I1I . ooOoO0O00
def iiIi1i ( ) :
 try :
  I1i11111i1i11 = gui . TVGuide ( )
  I1i11111i1i11 . doModal ( )
  del I1i11111i1i11
  if 77 - 77: Ii1I + oO0o / OoOo00o + o0o00Oo0O * I11i
 except :
  import sys
  import traceback as tb
  ( I1ii11 , oOoOoOoo0 , traceback ) = sys . exc_info ( )
  tb . print_exception ( I1ii11 , oOoOoOoo0 , traceback )
  if 34 - 34: OOooOOo - IIIii1II1II + o0o00Oo0O . Ii11Ii1I
def iIi1i1iIi1iI ( ) :
 II1I ( 'Full Backup' , '' , 10061 , ooOooo000oOO + 'Backup.png' , i1iiIII111ii , 'Back Up Your Full System' )
 if os . path . exists ( I1IIIii ) :
  II1I ( 'Backup Genie Favourites' , iIII , 10062 , ooOooo000oOO + 'Backup.png' , i1iiIII111ii , 'Back Up Your favourites' )
 if os . path . exists ( ooooooO0oo ) :
  II1I ( 'Backup Ivue Config' , ooooooO0oo , 10062 , ooOooo000oOO + 'Backup.png' , i1iiIII111ii , 'Back Up Your master.db' )
 if os . path . exists ( IIiiiiiiIi1I1 ) :
  II1I ( 'Backup Kodi Favourites' , IIiiiiiiIi1I1 , 10062 , ooOooo000oOO + 'Backup.png' , i1iiIII111ii , 'Back Up Your favourites.xml' )
  if 26 - 26: ii * oOo0O0Ooo + IIIii1II1II
  if 24 - 24: Ii % iI11I1II1I1I + IIIii1II1II / Ii
  if 70 - 70: oO0o * o0o00Oo0O . iI1iI1I1i1I + oOo0O0Ooo . OooO0OoOOOO
zip = o0oO0 . getSetting ( 'zip' )
Ii1iIiII1Ii = xbmc . translatePath ( os . path . join ( zip ) )
def Iii1II1iiiiI ( ) :
 O00OoOO0oo0 = xbmc . translatePath ( os . path . join ( zip , 'testCBFolder' ) )
 if not os . path . exists ( zip ) :
  i1iiIIiiI111 . ok ( '[COLOR=white]Origin[/COLOR]' , 'The download location you have stored does not exist .\nPlease update the addon settings and try again.' , '' , '' )
  o0oO0 . openSettings ( sys . argv [ 0 ] )
  if 96 - 96: OOooOOo . I11i - O0OoO
  if 99 - 99: OooO0OoOOOO . I1ii11iIi11i - Ii11Ii1I % Ii11Ii1I * o0o00Oo0O . IIiIiII11i
  if 4 - 4: Ii11Ii1I
def OO0oOOoo ( name , url , description ) :
 if 'Backup' in name :
  if 'Genie' in name :
   url = I1IIIii
  elif 'Ivue' in name :
   url = ooooooO0oo
  elif 'Kodi' in name :
   url = IIiiiiiiIi1I1
  Iii1II1iiiiI ( )
  oOOO00o000o = open ( url ) . read ( )
  iIi11i1 = os . path . join ( Ii1iIiII1Ii , description . split ( 'Your ' ) [ 1 ] )
  oO00oo0o00o0o = open ( iIi11i1 , mode = 'w' )
  oO00oo0o00o0o . write ( oOOO00o000o )
  oO00oo0o00o0o . close ( )
 else :
  if 'guisettings.xml' in description :
   IiIIIIIi = open ( os . path . join ( Ii1iIiII1Ii , description . split ( 'Your ' ) [ 1 ] ) ) . read ( )
   IiIi1iIIi1 = '<setting type="(.+?)" name="%s.(.+?)">(.+?)</setting>' % skin
   Ii1i = re . compile ( IiIi1iIIi1 ) . findall ( IiIIIIIi )
   for type , O0OoO0ooOO0o , OoOo0oOooOoOO in Ii1i :
    OoOo0oOooOoOO = OoOo0oOooOoOO . replace ( '&quot;' , '' ) . replace ( '&' , '&' )
    xbmc . executebuiltin ( "Skin.Se	t%s(%s,%s)" % ( type . title ( ) , O0OoO0ooOO0o , OoOo0oOooOoOO ) )
  else :
   iIi11i1 = os . path . join ( url )
   oOOO00o000o = open ( os . path . join ( Ii1iIiII1Ii , description . split ( 'Your ' ) [ 1 ] ) ) . read ( )
   oO00oo0o00o0o = open ( iIi11i1 , mode = 'w' )
   oO00oo0o00o0o . write ( oOOO00o000o )
   oO00oo0o00o0o . close ( )
 i1iiIIiiI111 . ok ( "[COLOR=white]Origin[/COLOR]" , "" , 'All Done !' , '' )
 if 60 - 60: ii % Ii11Ii1I * ooOoO0O00
 if 1 - 1: oOo0O0Ooo / OooO0OoOOOO * O0OoO
 if 1 - 1: iI1iI1I1i1I * I11i . OOooOOo / o0o00Oo0O
 if 100 - 100: IIIi . I11i * I1ii11iIi11i % o0o00Oo0O * o0o00Oo0O
def IIIii1 ( ) :
 Oooo0 = 1
 Iii1II1iiiiI ( )
 oOO = xbmc . translatePath ( os . path . join ( Ii1iIiII1Ii , 'Build Backup' , 'Full Backup' , '' ) )
 Oooo = xbmc . translatePath ( os . path . join ( Ii1iIiII1Ii , 'Build Backup' , 'my_full_backup.zip' ) )
 I1i1iiiII1i = xbmc . translatePath ( os . path . join ( Ii1iIiII1Ii , 'Build Backup' , 'my_full_backup_GUI_Settings.zip' ) )
 if not os . path . exists ( oOO ) :
  os . makedirs ( oOO )
 oO0oO0 = oOOoo00O0O . input ( 'Enter a name for this backup' , type = xbmcgui . INPUT_ALPHANUM )
 if ( not oO0oO0 ) : return False , 0
 i1i1IIIIi1i = oO0oO0
 Ii11iiI = xbmc . translatePath ( os . path . join ( oOO , i1i1IIIIi1i + '.zip' ) )
 IIi1iiii1iI = [ 'plugin.video.GenieTv' ]
 iIiiii = [ "xbmc.log" , "xbmc.old.log" , "kodi.log" , "kodi.old.log" , '.DS_Store' , '.setup_complete' , 'XBMCHelper.conf' ]
 O0000OOO0 = [ 'plugin.video.GenieTv' , 'repository.origin' , 'cache' , 'system' , 'Thumbnails' , "peripheral_data" , 'library' , 'keymaps' ]
 ooo0 = [ "xbmc.log" , "xbmc.old.log" , "kodi.log" , "kodi.old.log" , "Textures13.db" , '.DS_Store' , '.setup_complete' , 'XBMCHelper.conf' , 'advancedsettings.xml' ]
 oO000oOo00o0o = "Creating full backup of existing build"
 O00oO0 = "Creating Community Build"
 O0Oo00OoOo = "Archiving..."
 ii1ii111 = ""
 i11111I1I = "Please Wait"
 ii1Oo0000oOo ( oooOOOOO , Ii11iiI , O00oO0 , O0Oo00OoOo , ii1ii111 , i11111I1I , O0000OOO0 , ooo0 )
 time . sleep ( 1 )
 I11o0oO00oO0o0o0 = xbmc . translatePath ( os . path . join ( oOO , i1i1IIIIi1i + '_guisettings.zip' ) )
 I1I = zipfile . ZipFile ( I11o0oO00oO0o0o0 , mode = 'w' )
 try :
  I1I . write ( xbmc . translatePath ( os . path . join ( oooOOOOO , 'userdata' , 'profiles.xml' ) ) , 'profiles.xml' , zipfile . ZIP_DEFLATED )
 except : pass
 I1I . close ( )
 if Oooo0 == 0 :
  i1iiIIiiI111 . ok ( "FAILED!" , 'The guisettings.xml file could not be found on your' , 'system, please reboot and try again.' , '' )
 else :
  i1iiIIiiI111 . ok ( "SUCCESS!" , 'You Are Now Backed Up. If you\'d like to share this build with' , 'the community please post details on the forum at' , '[COLOR=blue][B]http://rh-project.info[/COLOR][/B]' )
  i1iiIIiiI111 . ok ( "Build Locations" , 'Full Backup (only used to restore on this device): [COLOR=yellow]' + Oooo , '[/COLOR]Universal Backup (can be used on any device): [COLOR=yellow]' + Ii11iiI + '[/COLOR]' )
  if 89 - 89: ooOoO0O00 / IIiIiII11i . iI11I1II1I1I
def ii1Oo0000oOo ( sourcefile , destfile , message_header , message1 , message2 , message3 , exclude_dirs , exclude_files ) :
 i11IIIiI1I = zipfile . ZipFile ( destfile , 'w' , zipfile . ZIP_DEFLATED )
 o0iiiI1I1iIIIi1 = len ( sourcefile )
 Iii = [ ]
 I1iiiiI1iI = [ ]
 Oo0oO0ooo . create ( message_header , message1 , message2 , message3 )
 for iIiiiii1i , iiIi1IIiI , i1oO0OO0 in os . walk ( sourcefile ) :
  for file in i1oO0OO0 :
   I1iiiiI1iI . append ( file )
 o0O0Oo00 = len ( I1iiiiI1iI )
 for iIiiiii1i , iiIi1IIiI , i1oO0OO0 in os . walk ( sourcefile ) :
  iiIi1IIiI [ : ] = [ O0Oo0o000oO for O0Oo0o000oO in iiIi1IIiI if O0Oo0o000oO not in exclude_dirs ]
  i1oO0OO0 [ : ] = [ oO00oo0o00o0o for oO00oo0o00o0o in i1oO0OO0 if oO00oo0o00o0o not in exclude_files ]
  for file in i1oO0OO0 :
   Iii . append ( file )
   oO0o00oOOooO0 = len ( Iii ) / float ( o0O0Oo00 ) * 100
   Oo0oO0ooo . update ( int ( oO0o00oOOooO0 ) , "Backing Up" , '[COLOR yellow]%s[/COLOR]' % file , 'Please Wait' )
   OOOoO000 = os . path . join ( iIiiiii1i , file )
   if not 'temp' in iiIi1IIiI :
    if not 'plugin.program.originwizard' in iiIi1IIiI :
     import time
     oOOOO = '01/01/1980'
     IiIi1ii111i1 = time . strftime ( '%d/%m/%Y' , time . gmtime ( os . path . getmtime ( OOOoO000 ) ) )
     if IiIi1ii111i1 > oOOOO :
      i11IIIiI1I . write ( OOOoO000 , OOOoO000 [ o0iiiI1I1iIIIi1 : ] )
 i11IIIiI1I . close ( )
 Oo0oO0ooo . close ( )
 if 31 - 31: IIIii1II1II + o0o00Oo0O
 if 87 - 87: O0OoO
def IIIii ( ) :
 O0O0O0OoOO ( )
 II1I ( '[COLORgreen]SCOOBY STREAMS[/COLOR]' , ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvdHZjYXRzLnBocA==' ) ) , 1016 , ooOooo000oOO + 'scoob.png' , i1iiIII111ii , '' )
 II1I ( '[COLORgreen]SCOOBY SCRAPES[/COLOR]' , str ( Ii1iIiII1ii1 ) , 1024 , ooOooo000oOO + 'scoob.png' , i1iiIII111ii , '' )
 if 83 - 83: OooO0OoOOOO % I11i % oOo0O0Ooo . iI11I1II1I1I - OooO0OoOOOO
 if 88 - 88: ii
def OO00 ( ) :
 O0O0O0OoOO ( )
 II1I ( '[COLORgreen]SEARCH MOVIES[/COLOR]' , str ( Ii1iIiII1ii1 ) , 9001 , ooOooo000oOO + 'MOVIESv.png' , i1iiIII111ii , '' )
 II1I ( '[COLORgreen]SEARCH SERIES[/COLOR]' , str ( Ii1iIiII1ii1 ) , 9002 , ooOooo000oOO + 'TVSHOWSv.png' , i1iiIII111ii , '' )
 II1I ( '[COLORgreen]SEARCH CARTOONS[/COLOR]' , '' , 10005 , ooOooo000oOO + 'ORIGINCARTOON' , i1iiIII111ii , '' )
 if 28 - 28: OoOo00o - Ii . Ii1I + OooO0OoOOOO / Ii1I
 if 35 - 35: OooO0OoOOOO
 if 75 - 75: I1ii11iIi11i / Ii1I . OooO0OoOOOO * IIIii1II1II - IIiIiII11i
 if 41 - 41: Ii11Ii1I
def oOOoo0o0OOOO ( ) :
 O0O0O0OoOO ( )
 II1I ( '[COLORgreen]RADIO[/COLOR]' , str ( Ii1iIiII1ii1 ) , 1013 , ooOooo000oOO + 'radio.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'CONCERTS' ) == 'true' :
  II1I ( '[COLORgreen]CONCERTS[/COLOR]' , ( i1111 ( 'aHR0cHM6Ly93d3cucmVkZGl0LmNvbS9yL2Z1bGxjb25jZXJ0cy8=' ) ) , 7050 , ooOooo000oOO + 'concerts.png' , i1iiIII111ii , '' )
 II1I ( '[COLORgreen]MUSIC[/COLOR]' , str ( Ii1iIiII1ii1 ) , 1030 , ooOooo000oOO + 'MUSIC.png' , i1iiIII111ii , '' )
 II1I ( '[COLORgreen]MUSIC ARCHIVE[/COLOR]' , str ( Ii1iIiII1ii1 ) + ( i1111 ( 'L3ZvZC91cmxzL211c2ljLnBocA==' ) ) , 1010 , ooOooo000oOO + 'MUSIC.png' , i1iiIII111ii , '' )
 II1I ( '[COLORgreen]MUSIC SEARCH[/COLOR]' , str ( Ii1iIiII1ii1 ) , 1111 , ooOooo000oOO + 'search.png' , i1iiIII111ii , '' )
 II1I ( '[COLORgreen]KODIBLE AUDIO BOOKS[/COLOR]' , 'http://doremisa.com/audiobooks/' , 30000 , ooOooo000oOO + 'kodible.png' , i1iiIII111ii , '' )
 if 26 - 26: o0oOO0O00o0O % iI11I1II1I1I + I11i
 iiO0o0oOOOoOo ( 'movies' , 'MAIN' )
 if 67 - 67: OoOo00o + IIiIiII11i - o0o00Oo0O . OoOo00o * IIiIiII11i * iI1iI1I1i1I
def o00OO00O0oOO ( ) :
 O0O0O0OoOO ( )
 if 4 - 4: ii - ooOoO0O00 % Ii11Ii1I - IIIii1II1II * I11i
 ooOOoooooo ( 'DELETE CACHE' , 'url' , 14 , ooOooo000oOO + 'MAIN5.png' , i1iiIII111ii , '' )
 ooOOoooooo ( 'DELETE PACKAGES' , 'url' , 6 , ooOooo000oOO + 'MAIN4.png' , i1iiIII111ii , '' )
 ooOOoooooo ( 'FORCE REFRESH' , 'url' , 10 , ooOooo000oOO + 'MAIN3.png' , i1iiIII111ii , 'Force Refresh All Repos' )
 if 85 - 85: ii * iI11I1II1I1I . o0oOO0O00o0O / ii % oOo0O0Ooo % o0o00Oo0O
 ooOOoooooo ( 'CHECK MY IP' , 'url' , 12 , ooOooo000oOO + 'MAIN2.png' , i1iiIII111ii , '' )
 ooOOoooooo ( 'ANDROID ONLY DELETE TEXTURE13.DB&THUBMNAIL FOLDER' , 'url' , 13 , ooOooo000oOO + 'MAIN1.png' , i1iiIII111ii , 'Only Works On Android On Windows It Deletes Your Thumnails Folder But Does Not Delete The Textures13.db' )
 II1I ( '[COLORgreen]ADVANCED SETTINGS XML[/COLOR]' , str ( Ii1iIiII1ii1 ) , 4 , ooOooo000oOO + 'XML.png' , i1iiIII111ii , '' )
 II1I ( '[COLORgreen]URL FIXES[/COLOR]' , str ( Ii1iIiII1ii1 ) , 20 , ooOooo000oOO + 'URLFIX.png' , i1iiIII111ii , '' )
 iiO0o0oOOOoOo ( 'movies' , 'MAIN' )
 if 36 - 36: Ii11Ii1I / IIiIiII11i / OooO0OoOOOO / OooO0OoOOOO + Ii1I
 if 95 - 95: OooO0OoOOOO
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
 if 51 - 51: IIiIiII11i + OooO0OoOOOO . ooOoO0O00 . Ii1I + OOooOOo * oOo0O0Ooo
 if 72 - 72: OoOo00o + OoOo00o / IIiIiII11i . ii % Ii11Ii1I
def III ( ) :
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
 if 41 - 41: Ii + I1ii11iIi11i / oOo0O0Ooo . ii % OoOo00o % ooOoO0O00
def oOOIi1II ( ) :
 O0O0O0OoOO ( )
 ooOOoooooo ( '[COLORgreen]My Local Zip[/COLOR]' , I11 , 48 , ooOooo000oOO + 'MB.png' , i1iiIII111ii , '' )
 ooOOoooooo ( '[COLORgreen]My Online Zip[/COLOR]' , i11 , 43 , ooOooo000oOO + 'MB.png' , i1iiIII111ii , '' )
 if 89 - 89: IIIi + ii + IIIi * ooOoO0O00 + iI11I1II1I1I % iI1iI1I1i1I
def oOo0oO ( ) :
 O0O0O0OoOO ( )
 ooOOoooooo ( 'INSTALL FTV GUIDE AND OTHER ADDONS REQUIRED' , str ( Ii1iIiII1ii1 ) + '/wizard/customftv/ftvguide-addons.zip' , 5 , ooOooo000oOO + 'FTV4.png' , i1iiIII111ii , '' )
 ooOOoooooo ( 'FTV GUIDE FIRST RUN SETTINGS' , str ( Ii1iIiII1ii1 ) + '/wizard/customftv/settings.xml' , 17 , ooOooo000oOO + 'FTV3.png' , i1iiIII111ii , '' )
 ooOOoooooo ( 'FTV GUIDE ADDONS2.INI UPDATE DAILY' , 'http://ren.byethost12.com/addons2.ini' , 16 , ooOooo000oOO + 'FTV1.png' , i1iiIII111ii , '' )
 ooOOoooooo ( 'RESET FTV DATABASE' , 'url' , 18 , ooOooo000oOO + 'FTV2.png' , i1iiIII111ii , '' )
 if 5 - 5: IIIii1II1II - IIIii1II1II . I1ii11iIi11i + OOooOOo - IIIii1II1II . OoOo00o
 if 31 - 31: IIiIiII11i - iI11I1II1I1I - iI11I1II1I1I % iI1iI1I1i1I
 if 12 - 12: iI11I1II1I1I
def iIi1i ( ) :
 O0O0O0OoOO ( )
 II1I ( '[COLORgreen]SKINS[/COLOR]' , str ( Ii1iIiII1ii1 ) , 33 , ooOooo000oOO + 'skinp.png' , i1iiIII111ii , '' )
 II1I ( '[COLORgreen]ARTWORK PACKS[/COLOR]' , str ( Ii1iIiII1ii1 ) , 34 , ooOooo000oOO + 'artp.png' , i1iiIII111ii , '' )
 II1I ( '[COLORgreen]CREATE UNIVERSAL PATHS[/COLOR]' , oooOOOOO , 35 , ooOooo000oOO + 'GUI.png' , i1iiIII111ii , '' )
 iiO0o0oOOOoOo ( 'movies' , 'MAIN' )
 if 4 - 4: IIIi / Ii / IIIii1II1II
def OooO0ooo0o ( url ) :
 O000oo0O = iiI111I1iIiI ( iii1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 Ii1i = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( O000oo0O )
 for i1I1i111Ii , url , OOOOoO00o0O , I1I1I1IIi1III , iIiIiIiI in Ii1i :
  II1I ( i1I1i111Ii , url , 5 , OOOOoO00o0O , I1I1I1IIi1III , iIiIiIiI )
 iiO0o0oOOOoOo ( 'movies' , 'MAIN' )
 if 32 - 32: Ii11Ii1I . OooO0OoOOOO . ii - oO0o + OoOo00o
def ooO0oO00O0o ( ) :
 O0O0O0OoOO ( )
 II1I ( '[COLORgreen]GOTHAM SKINS[/COLOR]' , str ( Ii1iIiII1ii1 ) , 36 , ooOooo000oOO + 'GSKIN.png' , i1iiIII111ii , '' )
 II1I ( '[COLORgreen]HELIX SKINS[/COLOR]' , str ( Ii1iIiII1ii1 ) , 37 , ooOooo000oOO + 'HSKIN.png' , i1iiIII111ii , '' )
 II1I ( '[COLORgreen]ISENGAARD SKINS[/COLOR]' , oooOOOOO , 38 , ooOooo000oOO + 'ISKIN.png' , i1iiIII111ii , '' )
 iiO0o0oOOOoOo ( 'movies' , 'MAIN' )
 if 70 - 70: IIIi
def i11iIIi11 ( url ) :
 O000oo0O = iiI111I1iIiI ( str ( Ii1iIiII1ii1 ) + ooOooo000OO00 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 Ii1i = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( O000oo0O )
 for i1I1i111Ii , url , OOOOoO00o0O , I1I1I1IIi1III , iIiIiIiI in Ii1i :
  II1I ( i1I1i111Ii , url , 42 , OOOOoO00o0O , I1I1I1IIi1III , iIiIiIiI )
 iiO0o0oOOOoOo ( 'movies' , 'MAIN' )
 if 34 - 34: o0o00Oo0O % ooOoO0O00 - IIIii1II1II + I1ii11iIi11i
def OoOo000oOo0oo ( url ) :
 O000oo0O = iiI111I1iIiI ( str ( Ii1iIiII1ii1 ) + oO0O ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 Ii1i = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( O000oo0O )
 for i1I1i111Ii , url , OOOOoO00o0O , I1I1I1IIi1III , iIiIiIiI in Ii1i :
  II1I ( i1I1i111Ii , url , 42 , OOOOoO00o0O , I1I1I1IIi1III , iIiIiIiI )
 iiO0o0oOOOoOo ( 'movies' , 'MAIN' )
 if 86 - 86: OOooOOo . iI11I1II1I1I - oO0o
def oOOI11I ( url ) :
 O000oo0O = iiI111I1iIiI ( str ( Ii1iIiII1ii1 ) + iIIII1i ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 Ii1i = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( O000oo0O )
 for i1I1i111Ii , url , OOOOoO00o0O , I1I1I1IIi1III , iIiIiIiI in Ii1i :
  II1I ( i1I1i111Ii , url , 42 , OOOOoO00o0O , I1I1I1IIi1III , iIiIiIiI )
 iiO0o0oOOOoOo ( 'movies' , 'MAIN' )
 if 76 - 76: o0oOO0O00o0O + O0OoO
def Iiii11iIi1 ( url ) :
 O000oo0O = iiI111I1iIiI ( i1111 ( 'aHR0cHM6Ly9kbC5kcm9wYm94dXNlcmNvbnRlbnQuY29tL3MvN2ZrMjhndDlwb3QxMjJhL0JVSUxEUy50eHQ/ZGw9MA==' ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 Ii1i = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( O000oo0O )
 for i1I1i111Ii , url , OOOOoO00o0O , I1I1I1IIi1III , iIiIiIiI in Ii1i :
  II1I ( i1I1i111Ii , url , 42 , OOOOoO00o0O , I1I1I1IIi1III , iIiIiIiI )
 iiO0o0oOOOoOo ( 'movies' , 'MAIN' )
 if 40 - 40: iI1iI1I1i1I % oO0o . IIIi
def OOO0oOOo00O ( url ) :
 O000oo0O = iiI111I1iIiI ( str ( Ii1iIiII1ii1 ) + OO0oIII111i11IiI ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 Ii1i = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( O000oo0O )
 for i1I1i111Ii , url , OOOOoO00o0O , I1I1I1IIi1III , iIiIiIiI in Ii1i :
  II1I ( i1I1i111Ii , url , 40 , OOOOoO00o0O , I1I1I1IIi1III , iIiIiIiI )
 iiO0o0oOOOoOo ( 'movies' , 'MAIN' )
 if 71 - 71: iI1iI1I1i1I / iI1iI1I1i1I * OoOo00o * OoOo00o / IIiIiII11i
def II1I1iiIII1I1 ( url ) :
 O000oo0O = iiI111I1iIiI ( str ( Ii1iIiII1ii1 ) + o0Ooo0o0ooo0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 Ii1i = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( O000oo0O )
 for i1I1i111Ii , url , OOOOoO00o0O , I1I1I1IIi1III , iIiIiIiI in Ii1i :
  II1I ( i1I1i111Ii , url , 5 , OOOOoO00o0O , I1I1I1IIi1III , iIiIiIiI )
 iiO0o0oOOOoOo ( 'movies' , 'MAIN' )
 if 70 - 70: Ii % o0oOO0O00o0O
def I11Ii11iI1 ( ) :
 IIiI1Ii = O0O0O0Oo ( i1111 ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby9hcGt0b29sL2Fway5waHA=' ) )
 Ii1i = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( IIiI1Ii )
 for iIII , iiiiII1I , i1I1i111Ii in Ii1i :
  IiIiiI11111I1 ( i1I1i111Ii , iIII , 2031 , iiiiII1I )
  if 55 - 55: O0OoO % ii / ii % ii
def oOoOoo0 ( name , url , description ) :
 O00OoOO0oo0 = xbmc . translatePath ( os . path . join ( ii1II , 'Download' ) )
 Oo0oO0ooo = xbmcgui . DialogProgress ( )
 Oo0oO0ooo . create ( "Your App Is Downloading" , "Why not check out our website" , '' , 'Http://architects.x10host.com' )
 I1iiii = os . path . join ( O00OoOO0oo0 , name + '.apk' )
 try :
  os . remove ( I1iiii )
 except :
  pass
 downloader . download ( url , I1iiii , Oo0oO0ooo )
 i1iiIIiiI111 = xbmcgui . Dialog ( )
 i1iiIIiiI111 . ok ( "GenieTv" , "[COLORred]Please press ok, exit kodi and go to your downloads folder to install your app[/COLOR]" , "[COLORblue]Tool Brought To You By Architects@Work[/COLOR]" )
 if 51 - 51: o0o00Oo0O - ooOoO0O00 / oOo0O0Ooo
def iI111i1I1II ( url ) :
 O00OoOO0oo0 = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/resources/downloads' ) )
 Oo0oO0ooo = xbmcgui . DialogProgress ( )
 Oo0oO0ooo . create ( "Your fILM Is Downloading" , "Why not check out our website" , '' , 'Http://architects.x10host.com' )
 I1iiii = os . path . join ( O00OoOO0oo0 , i1I1i111Ii + '.mp4' )
 try :
  os . remove ( I1iiii )
 except :
  pass
 downloader . download ( url , I1iiii , Oo0oO0ooo )
 i1iiIIiiI111 = xbmcgui . Dialog ( )
 i1iiIIiiI111 . ok ( "GenieTv" , "[COLORred]Please press ok, Your download With Be Avaiilable Via The My Downloads Button[/COLOR]" , "[COLORblue]Tool Brought To You By Architects@Work[/COLOR]" )
 if 96 - 96: IIIi / I1ii11iIi11i * IIiIiII11i - o0oOO0O00o0O * I1ii11iIi11i
 if 81 - 81: OooO0OoOOOO . I11i / IIIi
def Iii111Ii ( name , url , description ) :
 O00OoOO0oo0 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 Oo0oO0ooo = xbmcgui . DialogProgress ( )
 Oo0oO0ooo . create ( "Your Art Pack Is Downloading" , "Why not check out our website" , '' , 'Http://architects.x10host.com' )
 I1iiii = os . path . join ( O00OoOO0oo0 , name )
 try :
  os . remove ( I1iiii )
 except :
  pass
 downloader . download ( url , I1iiii , Oo0oO0ooo )
 O0O00oOooo0OO = xbmc . translatePath ( os . path . join ( oo00 ) )
 time . sleep ( 2 )
 Oo0oO0ooo . update ( 0 , "" , "Placing Your Art Please Wait" )
 print '======================================='
 print O0O00oOooo0OO
 print '======================================='
 extract . all ( I1iiii , O0O00oOooo0OO , Oo0oO0ooo )
 i1iiIIiiI111 = xbmcgui . Dialog ( )
 i1iiIIiiI111 . ok ( "GenieTv" , "[COLORred]Once complete your artwork will be stored in your Media folder, Accessible via the Homefolder, Enjoy[/COLOR]" )
 if 23 - 23: OoOo00o + oO0o
 if 2 - 2: OoOo00o - Ii11Ii1I - iI1iI1I1i1I - IIIi . iI11I1II1I1I
def o0O ( url ) :
 O000oo0O = iiI111I1iIiI ( i1111 ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby9HZW5pZVR2L3Rlc3Qvd2gudHh0' ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 Ii1i = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( O000oo0O )
 for i1I1i111Ii , url , OOOOoO00o0O , I1I1I1IIi1III , iIiIiIiI in Ii1i :
  II1I ( i1I1i111Ii , url , 5 , OOOOoO00o0O , I1I1I1IIi1III , iIiIiIiI )
 try :
  O000oo0O = iiI111I1iIiI ( IIiI1I1 + oO0o0o0ooO0oO + I11I1IIiiII1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
  Ii1i = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( O000oo0O )
  for i1I1i111Ii , url , OOOOoO00o0O , I1I1I1IIi1III , iIiIiIiI in Ii1i :
   II1I ( i1I1i111Ii , url , 5 , OOOOoO00o0O , I1I1I1IIi1III , iIiIiIiI )
 except : pass
 iiO0o0oOOOoOo ( 'movies' , 'INFO' )
 if 31 - 31: oOo0O0Ooo * OoOo00o + ii - o0oOO0O00o0O / ii
 if 19 - 19: OooO0OoOOOO * O0OoO * I11i + o0o00Oo0O / o0o00Oo0O
def ooOoO ( url ) :
 O000oo0O = iiI111I1iIiI ( i1111 ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby9HZW5pZVR2L3Rlc3Qvd2gudHh0' ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 Ii1i = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( O000oo0O )
 for i1I1i111Ii , url , OOOOoO00o0O , I1I1I1IIi1III , iIiIiIiI in Ii1i :
  II1I ( i1I1i111Ii , url , 43 , OOOOoO00o0O , I1I1I1IIi1III , iIiIiIiI )
 try :
  O000oo0O = iiI111I1iIiI ( IIiI1I1 + oO0o0o0ooO0oO + I11I1IIiiII1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
  Ii1i = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( O000oo0O )
  for i1I1i111Ii , url , OOOOoO00o0O , I1I1I1IIi1III , iIiIiIiI in Ii1i :
   II1I ( i1I1i111Ii , url , 43 , OOOOoO00o0O , I1I1I1IIi1III , iIiIiIiI )
 except : pass
 iiO0o0oOOOoOo ( 'movies' , 'INFO' )
 if 91 - 91: OoOo00o + oOo0O0Ooo
 if 59 - 59: oOo0O0Ooo + Ii + ooOoO0O00 / iI1iI1I1i1I
def I11iIiI1 ( name , url , description ) :
 O00OoOO0oo0 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 Oo0oO0ooo = xbmcgui . DialogProgress ( )
 Oo0oO0ooo . create ( "GenieTv" , "Downloading Content" , '' , 'Please Wait' )
 I1iiii = os . path . join ( O00OoOO0oo0 , name + '.zip' )
 try :
  os . remove ( I1iiii )
 except :
  pass
 downloader . download ( url , I1iiii , Oo0oO0ooo )
 oo0oooOo = xbmc . translatePath ( os . path . join ( 'special://home' , 'addons' ) )
 time . sleep ( 2 )
 Oo0oO0ooo . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print oo0oooOo
 print '======================================='
 extract . all ( I1iiii , oo0oooOo , Oo0oO0ooo )
 i1iiIIiiI111 = xbmcgui . Dialog ( )
 i1iiIIiiI111 . ok ( "GenieTv" , "Press ok to finish install" , "[COLOR yellow]Brought To You By Architects@Work[/COLOR]" )
 i1ioOOoo00O00o ( )
 if 59 - 59: IIIi - I11i - O0OoO
 if 48 - 48: ooOoO0O00 + iI1iI1I1i1I % OOooOOo / I1ii11iIi11i - I11i
def OOoOOo0O00O ( name , url , description ) :
 O00OoOO0oo0 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 Oo0oO0ooo = xbmcgui . DialogProgress ( )
 Oo0oO0ooo . create ( "GenieTv" , "Downloading " , '' , 'Please Wait' )
 I1iiii = os . path . join ( O00OoOO0oo0 , 'plugin.program.GenieTv.install' + '.zip' )
 try :
  os . remove ( I1iiii )
 except :
  pass
 downloader . download ( url , I1iiii , Oo0oO0ooo )
 oo0oooOo = xbmc . translatePath ( os . path . join ( 'special://' , 'home' ) )
 time . sleep ( 2 )
 Oo0oO0ooo . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print oo0oooOo
 print '======================================='
 extract . all ( I1iiii , oo0oooOo , Oo0oO0ooo )
 i1iiIIiiI111 = xbmcgui . Dialog ( )
 i1iiIIiiI111 . ok ( "GenieTv" , "Press ok to force close kodi, if unsuccessful using windows Please kill kodi via taskmanager" , "[COLOR yellow]Brought To You By Architects@Work[/COLOR]" )
 iiIii1I ( )
 if 47 - 47: O0OoO . iI1iI1I1i1I / I11i
def OOoOO ( name , url , description ) :
 O00OoOO0oo0 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 Oo0oO0ooo = xbmcgui . DialogProgress ( )
 Oo0oO0ooo . create ( "GenieTv" , "Downloading " , '' , 'Please Wait' )
 I1iiii = os . path . join ( O00OoOO0oo0 , 'plugin.program.GenieTv.install' + '.zip' )
 try :
  os . remove ( I1iiii )
 except :
  pass
 downloader . download ( url , I1iiii , Oo0oO0ooo )
 oo0oooOo = xbmc . translatePath ( os . path . join ( 'special://' , 'home' ) )
 time . sleep ( 2 )
 Oo0oO0ooo . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print oo0oooOo
 print '======================================='
 extract . all ( I1iiii , oo0oooOo , Oo0oO0ooo )
 i1iiIIiiI111 = xbmcgui . Dialog ( )
 i1iiIIiiI111 . ok ( "GenieTv" , "Please Disconnect The Power From Your Device. DO NOT EXIT CLEANLY VIA SHUTDOWN" , "[COLOR yellow]Brought To You By Architects@Work[/COLOR]" )
 if 66 - 66: I1ii11iIi11i - I11i * OooO0OoOOOO + OOooOOo + I11i - iI11I1II1I1I
 if 17 - 17: OoOo00o
def i1ii11 ( name , url , description ) :
 oo0oooOo = xbmc . translatePath ( os . path . join ( 'special://' , 'home' ) )
 Oo0oO0ooo = xbmcgui . DialogProgress ( )
 I1iiii = os . path . join ( I11 )
 time . sleep ( 2 )
 Oo0oO0ooo . create ( "GenieTv" , "Restoring" , '' , 'Please Wait' )
 print '======================================='
 print oo0oooOo
 print '======================================='
 extract . all ( I1iiii , oo0oooOo , Oo0oO0ooo )
 i1iiIIiiI111 = xbmcgui . Dialog ( )
 i1iiIIiiI111 . ok ( "GenieTv" , "Please Disconnect The Power From Your Device. DO NOT EXIT CLEANLY VIA SHUTDOWN" , "[COLOR yellow]Brought To You By Architects@Work[/COLOR]" )
 if 49 - 49: ii / Ii * Ii
 if 58 - 58: OoOo00o
def iiIii1I ( ) :
 i1111I1I = xbmcgui . Dialog ( ) . yesno ( 'Force Close Kodi' , 'You are about to close Kodi' , 'Would you like to continue?' , nolabel = 'No, Cancel' , yeslabel = 'Yes, Close' )
 if i1111I1I == 0 :
  return
 elif i1111I1I == 1 :
  pass
 IiIIi1IiiI1 = oO00oOo0OOO ( )
 print "Platform: " + str ( IiIIi1IiiI1 )
 if IiIIi1IiiI1 == 'osx' :
  print "############   try osx force close  #################"
  try : os . system ( 'killall -9 XBMC' )
  except : pass
  try : os . system ( 'killall -9 Kodi' )
  except : pass
  i1iiIIiiI111 . ok ( "[COLOR=red][B]WARNING  !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu." , '' )
 elif IiIIi1IiiI1 == 'linux' :
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
 elif IiIIi1IiiI1 == 'android' :
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
 elif IiIIi1IiiI1 == 'windows' :
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
  if 23 - 23: ooOoO0O00 . I11i * oO0o
def oO00oOo0OOO ( ) :
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
  if 15 - 15: OOooOOo
  if 62 - 62: Ii11Ii1I
  if 51 - 51: OOooOOo
def I11IIIiIi11 ( url ) :
 Oo0oO0ooo . create ( "[COLOR=green]GenieTv[/COLOR]" , "Renaming paths..." , '' , 'Please Wait' )
 for I11iiIi1i1 , iiIi1IIiI , i1oO0OO0 in os . walk ( url ) :
  for file in i1oO0OO0 :
   if file . endswith ( ".xml" ) :
    Oo0oO0ooo . update ( 0 , "Fixing" , file , 'Please Wait' )
    IiIIIIIi = open ( ( os . path . join ( I11iiIi1i1 , file ) ) ) . read ( )
    i1IiiI1iIi = IiIIIIIi . replace ( oooOOOOO , 'special://home/' )
    oO00oo0o00o0o = open ( ( os . path . join ( I11iiIi1i1 , file ) ) , mode = 'w' )
    oO00oo0o00o0o . write ( str ( i1IiiI1iIi ) )
    oO00oo0o00o0o . close ( )
 iiIii1I ( )
 if 66 - 66: oO0o * I1ii11iIi11i
def II1IIIiiI11 ( ) :
 IIiI1Ii = O0O0O0Oo ( i1111 ( 'aHR0cDovL3d3dy5saXN0ZW5saXZlLmV1L3VrLmh0bWw=' ) )
 Ii1i = re . compile ( '<tr>.+?<td><a href=".+?"><b>(.+?)</b>.+?<td><a href="(.+?)">' , re . DOTALL ) . findall ( IIiI1Ii )
 for i1I1i111Ii , iIII in Ii1i :
  OO0ooOOO00 ( i1I1i111Ii , iIII , 222 , ooOooo000oOO + 'radio.png' )
  if 17 - 17: o0o00Oo0O . IIIi . o0o00Oo0O + o0o00Oo0O / I1ii11iIi11i . O0OoO
def OO00OOoO0o ( ) :
 IIiI1Ii = O0O0O0Oo ( i1111 ( 'aHR0cDovL3d3dy50b29uamV0LmNvbS8=' ) )
 Ii1i = re . compile ( '<a href="(.+?)" style="font-size:.8em;">(.+?)</a>' ) . findall ( IIiI1Ii )
 for iIII , i1I1i111Ii in Ii1i :
  IiIiiI11111I1 ( '[COLORgreen]' + i1I1i111Ii + '[/COLOR]' , 'http://www.toonjet.com/' + iIII , 8051 , ooOooo000oOO + 'classictoons.png' )
def Iiiiiii1 ( url ) :
 IIiI1Ii = O0O0O0Oo ( url )
 Ii1i = re . compile ( '<a href="(.+?)"><img src="(.+?)"' ) . findall ( IIiI1Ii )
 I1 = re . compile ( '<a href="(.+?)">.+?</a></td></tr></table>' ) . findall ( IIiI1Ii )
 for url , iiI1IIIi in Ii1i :
  if 'ol.gif' in iiI1IIIi :
   pass
  elif 'link_block_' in iiI1IIIi :
   pass
  elif '.png' in iiI1IIIi :
   pass
  else :
   IiIiiI11111I1 ( ( iiI1IIIi ) . replace ( 'http://www.toonjet.com/images/icons/' , '' ) . replace ( 'images/icons/' , '' ) . replace ( '.jpg' , '' ) . replace ( '_icon' , '' ) . replace ( '_' , ' ' ) , 'http://www.toonjet.com/' + url , 8052 , ooOooo000oOO + 'vod.png' )
 for url in I1 :
  IiIiiI11111I1 ( 'NEXT PAGE' , 'http://www.toonjet.com/' + url , 8051 , ooOooo000oOO + 'Next.png' )
def oOO0oo ( url ) :
 IIiI1Ii = O0O0O0Oo ( url )
 Ii1i = re . compile ( '<iframe width="640" height="480" src="(.+?)" frameborder="0" allowfullscreen></iframe>' ) . findall ( IIiI1Ii )
 for url in Ii1i :
  OO0ooOOO00 ( '[COLORgreen]PLAY[/COLOR]' , ( url ) . replace ( 'http://www.youtube.com/embed/' , '' ) . replace ( '?autoplay=0' , '' ) , 8043 , ooOooo000oOO + 'classictoons.png' )
  if 29 - 29: oOo0O0Ooo * IIiIiII11i * ii - Ii1I * IIiIiII11i
  if 41 - 41: o0o00Oo0O
def I111I11I111 ( ) :
 iiiiI11ii ( 'Audio Books' , '' , 30011 , ooOooo000oOO + 'audiobooks.png' , ooOooo000oOO + 'audiobooks.png' , '' )
 iiiiI11ii ( 'Kids Audio Books' , '' , 30006 , ooOooo000oOO + 'kidsaudiobooks.png' , ooOooo000oOO + 'kidsaudiobooks.png' , '' )
 if 96 - 96: o0oOO0O00o0O . o0o00Oo0O / o0oOO0O00o0O % o0o00Oo0O
def o0o000 ( ) :
 iiiiI11ii ( 'All' , '' , 30001 , ooOooo000oOO + 'kodible.png' , ooOooo000oOO + 'kodible.png' , '' )
 iiiiI11ii ( 'Popular' , '' , 30012 , ooOooo000oOO + 'POPULARv.png' , ooOooo000oOO + 'POPULARv.png' , '' )
 iiiiI11ii ( 'Search' , '' , 30013 , ooOooo000oOO + 'search.png' , ooOooo000oOO + 'search.png' , '' )
 if 50 - 50: OooO0OoOOOO % ooOoO0O00
def iii11II1I ( ) :
 o00OO00OoO = iiI111I1iIiI ( OooO0 + 'books' + ooOoOoo0O )
 Ii1i = re . compile ( '<NAME=>(.*?)</NAME><URL=>(.*?)</URL><CAT=>(.*?)</CAT>' ) . findall ( o00OO00OoO )
 for i1I1i111Ii , iIII , iI111I11i in Ii1i :
  if 'Parent' in i1I1i111Ii :
   pass
  elif '2' in iI111I11i :
   iiiiI11ii ( ( i1I1i111Ii ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , iIII , 30010 , ooOooo000oOO + 'kodible.png' , ooOooo000oOO + 'kodible.png' , '' )
   if 23 - 23: Ii11Ii1I . I11i + I1ii11iIi11i - IIIii1II1II
def II1iiIiIiI ( ) :
 Ooo0OOoOoO0 = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 IIo0Oo0oO0oOO00 = Ooo0OOoOoO0 . lower ( )
 o00OO00OoO = iiI111I1iIiI ( OooO0 + 'books' + ooOoOoo0O )
 Ii1i = re . compile ( '<NAME=>(.*?)</NAME><URL=>(.*?)</URL><CAT=>(.*?)</CAT>' ) . findall ( o00OO00OoO )
 for i1I1i111Ii , iIII , iI111I11i in Ii1i :
  if Ooo0OOoOoO0 in i1I1i111Ii . lower ( ) :
   if '1' in iI111I11i :
    iiiiI11ii ( ( i1I1i111Ii ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , iIII , 30010 , ooOooo000oOO + 'kodible.png' , ooOooo000oOO + 'kodible.png' , '' )
   elif '2' in iI111I11i :
    iiiiI11ii ( ( i1I1i111Ii ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , iIII , 30010 , ooOooo000oOO + 'kodible.png' , ooOooo000oOO + 'kodible.png' , '' )
   elif '3' in iI111I11i :
    iiiiI11ii ( ( i1I1i111Ii ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , iIII , 30009 , ooOooo000oOO + 'kodible.png' , ooOooo000oOO + 'kodible.png' , '' )
    if 24 - 24: I1ii11iIi11i - ooOoO0O00 + iI1iI1I1i1I
    if 38 - 38: ii / Ii1I . o0o00Oo0O / ooOoO0O00 / I1ii11iIi11i + iI11I1II1I1I
def ooO00O00oOO ( ) :
 o00OO00OoO = iiI111I1iIiI ( OooO0 + 'books' + ooOoOoo0O )
 Ii1i = re . compile ( '<NAME=>(.*?)</NAME><URL=>(.*?)</URL><CAT=>(.*?)</CAT>' ) . findall ( o00OO00OoO )
 for i1I1i111Ii , iIII , iI111I11i in Ii1i :
  if '1' in iI111I11i :
   iiiiI11ii ( ( i1I1i111Ii ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , iIII , 3010 , ooOooo000oOO + 'kodible.png' , ooOooo000oOO + 'kodible.png' , '' )
  elif '2' in iI111I11i :
   iiiiI11ii ( ( i1I1i111Ii ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , iIII , 30010 , ooOooo000oOO + 'kodible.png' , ooOooo000oOO + 'kodible.png' , '' )
  elif '3' in iI111I11i :
   iiiiI11ii ( ( i1I1i111Ii ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , iIII , 30009 , ooOooo000oOO + 'kodible.png' , ooOooo000oOO + 'kodible.png' , '' )
   if 40 - 40: o0oOO0O00o0O . OoOo00o + oOo0O0Ooo + Ii1I + IIIi
 xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 26 - 26: iI11I1II1I1I
def OOOo ( url ) :
 IiI1iiiIii = url
 o00OO00OoO = iiI111I1iIiI ( url )
 I1 = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( o00OO00OoO )
 for url , i1I1i111Ii in I1 :
  if 'mp3' in i1I1i111Ii :
   II1I ( ( i1I1i111Ii ) . replace ( '%20' , ' ' ) , IiI1iiiIii + url , 10012 , ooOooo000oOO + 'kodible.png' , ooOooo000oOO + 'kodible.png' , '' )
  if 'wma' in i1I1i111Ii :
   II1I ( ( i1I1i111Ii ) . replace ( '%20' , ' ' ) , IiI1iiiIii + url , 10012 , ooOooo000oOO + 'kodible.png' , ooOooo000oOO + 'kodible.png' , '' )
  if 'm4b' in i1I1i111Ii :
   II1I ( ( i1I1i111Ii ) . replace ( '%20' , ' ' ) , IiI1iiiIii + url , 10012 , ooOooo000oOO + 'kodible.png' , ooOooo000oOO + 'kodible.png' , '' )
  elif '/' in i1I1i111Ii :
   iiiiI11ii ( ( i1I1i111Ii ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , IiI1iiiIii + url , 30009 , ooOooo000oOO + 'kodible.png' , ooOooo000oOO + 'kodible.png' , '' )
   if 79 - 79: OOooOOo % OooO0OoOOOO % I1ii11iIi11i
   if 29 - 29: ii . oOo0O0Ooo % Ii1I - o0oOO0O00o0O
   if 8 - 8: ooOoO0O00
def iIiI1 ( url ) :
 o00OO00OoO = iiI111I1iIiI ( url )
 IiI1iiiIii = url
 Ii1i = re . compile ( '<li><a href="(.+?)">(.+?)</a></li>' ) . findall ( o00OO00OoO )
 for url , i1I1i111Ii in Ii1i :
  if 'Parent' in i1I1i111Ii :
   pass
  elif '.db' in i1I1i111Ii :
   pass
  elif '.jpg' in i1I1i111Ii :
   pass
  elif '.html' in i1I1i111Ii :
   pass
  elif '.doc' in i1I1i111Ii :
   pass
  elif 'mp3' in i1I1i111Ii :
   II1I ( ( i1I1i111Ii ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , IiI1iiiIii + url , 10012 , ooOooo000oOO + 'kodible.png' , ooOooo000oOO + 'kodible.png' , '' )
  elif 'm4a' in i1I1i111Ii :
   II1I ( ( i1I1i111Ii ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , IiI1iiiIii + url , 10012 , ooOooo000oOO + 'kodible.png' , ooOooo000oOO + 'kodible.png' , '' )
  else :
   iiiiI11ii ( ( i1I1i111Ii ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , IiI1iiiIii + url , 30010 , ooOooo000oOO + 'kodible.png' , ooOooo000oOO + 'kodible.png' , '' )
   if 37 - 37: oO0o * Ii / IIIii1II1II % IIIi
   if 71 - 71: ii
def iIiI1iiiI1ii ( ) :
 iiiiI11ii ( 'A-Z' , '' , 7 , ooOooo000oOO + 'kodible.png' , ooOooo000oOO + 'kodible.png' , '' )
 iiiiI11ii ( 'All' , '' , 3 , ooOooo000oOO + 'kodible.png' , ooOooo000oOO + 'kodible.png' , '' )
 iiiiI11ii ( 'Search' , '' , 14 , ooOooo000oOO + 'kodible.png' , ooOooo000oOO + 'kodible.png' , '' )
 if 29 - 29: o0oOO0O00o0O . IIIii1II1II . oOo0O0Ooo * OOooOOo
def OO00o ( ) :
 o00OO00OoO = iiI111I1iIiI ( i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9tcDNfZG93bmxvYWRzLmh0bQ==' ) )
 Ii1i = re . compile ( '<td width=".+?" align="center">.+?<a href="(.*?)">.+?<img border="0" src="images/Squeeze%20(.*?).gif" width="74" height=".*?"></a></td>' , re . DOTALL ) . findall ( o00OO00OoO )
 for iIII , iiI1IIIi in Ii1i :
  print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<' + iIII + '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
  if '-x' in iiI1IIIi :
   pass
  else :
   iiiiI11ii ( iiI1IIIi , ( i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) ) + ( iIII ) . replace ( 'colour_it' , 'books_audio/audio_books_a' ) , 30008 , ( i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9pbWFnZXMvU3F1ZWV6ZSUyMA==' ) ) + iiI1IIIi + '.gif' , ooOooo000oOO + 'kodible.png' , '' )
   if 60 - 60: Ii1I - OoOo00o - oOo0O0Ooo / I11i
 xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 81 - 81: IIiIiII11i + Ii / o0oOO0O00o0O
 if 85 - 85: Ii + IIIi * OOooOOo
def iiiII ( url ) :
 o00OO00OoO = iiI111I1iIiI ( url )
 Ii1i = re . compile ( '<td width=".*?" height=".*?"><b>.*?<a href="(.*?)">(.*?)</a></b></td>' , re . DOTALL ) . findall ( o00OO00OoO )
 for url , i1I1i111Ii in Ii1i :
  if '</a>' in i1I1i111Ii :
   pass
  elif '(' in i1I1i111Ii :
   iiiiI11ii ( ( i1I1i111Ii ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '.mp3' , '' ) , i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) + url , 30005 , ooOooo000oOO + 'kodible.png' , ooOooo000oOO + 'kodible.png' , '' )
  else :
   II1I ( ( i1I1i111Ii ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '.mp3' , '' ) , i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) + url , 30004 , ooOooo000oOO + 'kodible.png' , ooOooo000oOO + 'kodible.png' , '' )
   if 57 - 57: iI1iI1I1i1I . I1ii11iIi11i + IIiIiII11i
 xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 43 - 43: IIIi % o0oOO0O00o0O
def o0O0ooOOoO ( ) :
 Ooo0OOoOoO0 = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 IIo0Oo0oO0oOO00 = Ooo0OOoOoO0 . lower ( )
 o00OO00OoO = iiI111I1iIiI ( i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9jb21wbGV0ZV9saXN0Lmh0bQ==' ) )
 Ii1i = re . compile ( '<td width=".+?">.*?<b>.+?<a href="(.*?)">(.*?)</a></b></td>' , re . DOTALL ) . findall ( o00OO00OoO )
 for iIII , i1I1i111Ii in Ii1i :
  if Ooo0OOoOoO0 in i1I1i111Ii . lower ( ) :
   if '</a>' in i1I1i111Ii :
    pass
   elif '(' in i1I1i111Ii :
    iiiiI11ii ( ( i1I1i111Ii ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + iIII , 30005 , ooOooo000oOO + 'kodible.png' , ooOooo000oOO + 'kodible.png' , '' )
   else :
    II1I ( ( i1I1i111Ii ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + iIII , 30004 , ooOooo000oOO + 'kodible.png' , ooOooo000oOO + 'kodible.png' , '' )
    if 19 - 19: Ii
    if 54 - 54: IIiIiII11i . iI1iI1I1i1I
def oOOII1i11i1iIi11 ( ) :
 o00OO00OoO = iiI111I1iIiI ( i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9jb21wbGV0ZV9saXN0Lmh0bQ==' ) )
 Ii1i = re . compile ( '<td width=".+?">.*?<b>.+?<a href="(.*?)">(.*?)</a></b></td>' , re . DOTALL ) . findall ( o00OO00OoO )
 for iIII , i1I1i111Ii in Ii1i :
  if '</a>' in i1I1i111Ii :
   pass
  elif '(' in i1I1i111Ii :
   iiiiI11ii ( ( i1I1i111Ii ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + iIII , 30005 , ooOooo000oOO + 'kodible.png' , ooOooo000oOO + 'kodible.png' , '' )
  else :
   II1I ( ( i1I1i111Ii ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + iIII , 30004 , ooOooo000oOO + 'kodible.png' , ooOooo000oOO + 'kodible.png' , '' )
   if 83 - 83: Ii11Ii1I
 xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 25 - 25: iI1iI1I1i1I + OOooOOo . I11i % OOooOOo * IIIii1II1II
 if 32 - 32: Ii - IIIi
def oo00ooOoo ( url ) :
 o00OO00OoO = iiI111I1iIiI ( url )
 Ii1i = re . compile ( '<a href="(.+?)">Download</a></b></td>' ) . findall ( o00OO00OoO )
 for url in Ii1i :
  IiI1iiiIii = ( i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) ) + url
  Resolve ( IiI1iiiIii )
  if 28 - 28: Ii11Ii1I
def iIIIiiiI11I ( url ) :
 o00OO00OoO = iiI111I1iIiI ( url )
 Ii1i = re . compile ( '<td width="247">(.*?)</td>.*?<a href="(.+?)">' , re . DOTALL ) . findall ( o00OO00OoO )
 for i1I1i111Ii , url in Ii1i :
  if '<p align' in i1I1i111Ii :
   pass
  elif '&nbsp;' in i1I1i111Ii :
   pass
  else :
   II1I ( ( i1I1i111Ii ) . replace ( '&nbsp;' , '' ) , i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) + url , 10012 , ooOooo000oOO + 'kodible.png' , ooOooo000oOO + 'kodible.png' , '' )
   if 6 - 6: Ii11Ii1I % ooOoO0O00 . Ii11Ii1I * Ii11Ii1I
 xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 81 - 81: IIIii1II1II / iI11I1II1I1I + OooO0OoOOOO
 if 49 - 49: IIIii1II1II / ii / oOo0O0Ooo
def o0OooooOoOO ( ) :
 o00OO00OoO = cloudflare . source ( i1111 ( 'aHR0cDovL3dhdGNoY2FydG9vbnNvbmxpbmUuZXUv' ) )
 Ii1i = re . compile ( 'class="menu-item menu-item-type-.+?><a href="([^"]*)">(.+?)</a></li>' , re . DOTALL ) . findall ( o00OO00OoO )
 for iIII , i1I1i111Ii in Ii1i :
  if 'ongoing' in iIII :
   II1I ( '[COLORgreen]' + i1I1i111Ii + '[/COLOR]' , iIII , 21005 , ooOooo000oOO + 'on-going.png' , '' , '' )
  if 'cartoon-series' in iIII :
   II1I ( '[COLORgreen]' + i1I1i111Ii + '[/COLOR]' , iIII , 21005 , ooOooo000oOO + 'cartoonseries.png' , '' , '' )
  if 'disney' in iIII :
   II1I ( '[COLORgreen]' + i1I1i111Ii + '[/COLOR]' , iIII , 21005 , ooOooo000oOO + 'disneytoons.png' , '' , '' )
  if 'genre' in iIII :
   II1I ( '[COLORgreen]' + i1I1i111Ii + '[/COLOR]' , iIII , 21005 , ooOooo000oOO + 'cartoongenre.png' , '' , '' )
  if 'years' in iIII :
   II1I ( '[COLORgreen]' + i1I1i111Ii + '[/COLOR]' , iIII , 21005 , ooOooo000oOO + 'years.png' , '' , '' )
def i1i1IIIIIIIi ( url ) :
 o00OO00OoO = cloudflare . source ( url )
 Ii1i = re . compile ( '<a href="([^"]*)" title="([^"]*)" rel="nofollow" id="featured-thumbnail">.+?<div class="featured-thumbnail"><img width="140" height="200" src="([^"]*)"' , re . DOTALL ) . findall ( o00OO00OoO )
 oo0o0oOo = re . compile ( '<button type="button"><a href="([^"]*)" target="_blank">(.+?)</a>' ) . findall ( o00OO00OoO )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' ) . findall ( o00OO00OoO )
 for url , i1I1i111Ii , iiI1IIIi in Ii1i :
  II1I ( '[COLORgreen]' + i1I1i111Ii + '[/COLOR]' , url , 21006 , iiI1IIIi , iiI1IIIi , i1I1i111Ii )
 for url , i1I1i111Ii in oo0o0oOo :
  II1I ( '[COLORgreen]' + i1I1i111Ii + '[/COLOR]' , url , 21005 , ooOooo000oOO + 'watchcartoons.png' , '' , '' )
 for url in next :
  II1I ( '[COLORgreen]NEXT[/COLOR]' , url , 21005 , ooOooo000oOO + 'Next.png' , '' , '' )
def OO0oOOo0o ( url ) :
 o00OO00OoO = cloudflare . source ( url )
 Ii1i = re . compile ( '<li><a href="([^"]*)" >(.+?)</a></li>' , re . DOTALL ) . findall ( o00OO00OoO )
 I1III11iiii11i1 = re . compile ( 'file:"([^"]*)",type:"mp4",label:"([^"]*)"' , re . DOTALL ) . findall ( o00OO00OoO )
 ooOo0OoO = re . compile ( 'src="([^"]*)" frameborder=' ) . findall ( o00OO00OoO )
 i1iiIIi1I = re . compile ( '<iframe src="([^"]*)"' ) . findall ( o00OO00OoO )
 for url , i1I1i111Ii in Ii1i :
  II1I ( '[COLORgreen]' + i1I1i111Ii + '[/COLOR]' , url , 21007 , ooOooo000oOO + 'watchcartoons.png' , '' , '' )
 for url in ooOo0OoO :
  II1I ( '[COLORgreen]PLAY[/COLOR]' , 'http:' + url , 222 , ooOooo000oOO + 'watchcartoons.png' , '' , '' )
 for url , i1I1i111Ii in I1III11iiii11i1 :
  ooOOoooooo ( '[COLORgreen]' + i1I1i111Ii + '[/COLOR]' , url , 222 , ooOooo000oOO + 'watchcartoons.png' , '' , '' )
 else :
  II1I ( '[COLORgreen]NO STREAMS AVAILABLE[/COLOR]' , url , 21005 , ooOooo000oOO + 'watchcartoons.png' , '' , '' )
def iiI1I1IIi11i1 ( url ) :
 o00OO00OoO = cloudflare . source ( url )
 Ii1i = re . compile ( 'file:"([^"]*)",type:"mp4",label:"([^"]*)"' , re . DOTALL ) . findall ( o00OO00OoO )
 for url , i1I1i111Ii in Ii1i :
  ooOOoooooo ( '[COLORgreen]' + i1I1i111Ii + '[/COLOR]' , url , 222 , ooOooo000oOO + 'watchcartoons.png' , '' , '' )
  if 45 - 45: O0OoO % I11i - O0OoO
def i1i1 ( ) :
 IiIiiI11111I1 ( '[COLORgreen]CARTOONS[/COLOR]' , '' , 20001 , ooOooo000oOO + 'ORIGINCARTOON.png' )
 IiIiiI11111I1 ( '[COLORgreen]ANIME[/COLOR]' , 'https://kissanime.to/AnimeList' , 20001 , ooOooo000oOO + 'ORIGINCARTOON.png' )
 if 69 - 69: Ii1I - IIIi
def iiIIi1 ( ) :
 IiIiiI11111I1 ( '[COLORgreen]BY NAME[/COLOR]' , 'http://kisscartoon.me/CartoonList' , 20002 , ooOooo000oOO + 'ORIGINCARTOON.png' )
 IiIiiI11111I1 ( '[COLORgreen]BY GENRE[/COLOR]' , 'http://kisscartoon.me/CartoonList' , 20003 , ooOooo000oOO + 'ORIGINCARTOON.png' )
 if 10 - 10: iI1iI1I1i1I * Ii11Ii1I % ii
def O0Oo0Ooo ( url ) :
 o00OO00OoO = cloudflare . source ( url )
 Ii1i = re . compile ( 'href="(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( o00OO00OoO )
 for url , i1I1i111Ii in Ii1i :
  if '?c=' in url :
   IiIiiI11111I1 ( '[COLORgreen]' + i1I1i111Ii + '[/COLOR]' , 'http://kisscartoon.me' + url , 20004 , ooOooo000oOO + 'ORIGINCARTOON.png' )
   if 78 - 78: oO0o % OooO0OoOOOO * ooOoO0O00
def O0iI ( url ) :
 o00OO00OoO = cloudflare . source ( url )
 Ii1i = re . compile ( 'href="(.+?)" title="(.+?)">/n(.+?)</a><br/>' , re . DOTALL ) . findall ( o00OO00OoO )
 for url , Ii1IIiiIiiIi , i1I1i111Ii in Ii1i :
  if 'Genre' in url :
   IiIiiI11111I1 ( '[COLORgreen]' + i1I1i111Ii + '[/COLOR]' , 'http://kisscartoon.me' + url , 20004 , ooOooo000oOO + 'ORIGINCARTOON.png' )
   if 40 - 40: I11i
def oOOo0oo0o0o0 ( url ) :
 o00OO00OoO = cloudflare . source ( url )
 Ii1i = re . compile ( 'src="(.+?)" style=.+?<a class="bigChar" href="(.+?)">(.+?)</a>.+?<p>(.+?)</p>' , re . DOTALL ) . findall ( o00OO00OoO )
 for url , Ii1IIiiIiiIi , i1I1i111Ii in Ii1i :
  II1I ( '[COLORgreen]' + i1I1i111Ii + '[/COLOR]' , 'http://kisscartoon.me' + url , 20005 , img , '' , Ii1IIiiIiiIi )
  if 43 - 43: Ii1I / oOo0O0Ooo . O0OoO
def Ooo0oO0 ( url ) :
 o00OO00OoO = cloudflare . source ( url )
 Ii1i = re . compile ( '<img width="120" height="165" src="(.+?)" style=.+?<a class="bigChar" href="(.+?)">(.+?)</a>.+?<p>(.+?)</p>' , re . DOTALL ) . findall ( o00OO00OoO )
 for url , Ii1IIiiIiiIi , i1I1i111Ii in Ii1i :
  II1I ( '[COLORgreen]' + i1I1i111Ii + '[/COLOR]' , 'http://kisscartoon.me' + url , 20005 , img , '' , Ii1IIiiIiiIi )
  if 86 - 86: o0o00Oo0O
  if 95 - 95: o0oOO0O00o0O * IIIii1II1II . OOooOOo . ooOoO0O00 . ooOoO0O00 - I11i
  if 26 - 26: iI11I1II1I1I % Ii % Ii1I
  if 67 - 67: ii
  if 29 - 29: o0o00Oo0O - Ii - IIiIiII11i + IIIii1II1II * OooO0OoOOOO
def IiI1ii1Ii ( ) :
 if 51 - 51: Ii * I11i / oOo0O0Ooo
 II1I ( '[COLORgreen]Cartoons[/COLOR]' , i1111 ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2NhcnRvb24=' ) , 10004 , ooOooo000oOO + 'ORIGINCARTOON.png' , i1iiIII111ii , '' )
 II1I ( '[COLORgreen]Search Cartoons[/COLOR]' , '' , 10005 , ooOooo000oOO + 'ORIGINCARTOON.png' , i1iiIII111ii , '' )
 if 40 - 40: oOo0O0Ooo
def I1I1 ( ) :
 Ooo0OOoOoO0 = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 IIo0Oo0oO0oOO00 = Ooo0OOoOoO0 . lower ( )
 o00OO00OoO = iiI111I1iIiI ( i1111 ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2NhcnRvb24=' ) )
 Ii1i = re . compile ( '<td><a href="(.+?)">(.+)</a></td>' ) . findall ( o00OO00OoO )
 for iIII , i1I1i111Ii in Ii1i :
  if Ooo0OOoOoO0 in i1I1i111Ii . lower ( ) :
   if 'Dad!' in i1I1i111Ii :
    pass
   elif 'Family Guy' in i1I1i111Ii :
    pass
   elif '2 Stupid' in i1I1i111Ii :
    pass
   elif 'The Zelfs' in i1I1i111Ii :
    pass
   elif 'A Clone' in i1I1i111Ii :
    pass
   elif 'A.T.O.M' in i1I1i111Ii :
    pass
   elif 'Almost Naked' in i1I1i111Ii :
    pass
   elif 'Angry Kid' in i1I1i111Ii :
    pass
   elif 'Annoying Orange' in i1I1i111Ii :
    pass
   elif 'Aqua Teen' in i1I1i111Ii :
    pass
   elif 'Assy Mcgee' in i1I1i111Ii :
    pass
   elif 'Astroblast' in i1I1i111Ii :
    pass
   elif 'Atomic Betty' in i1I1i111Ii :
    pass
   elif 'Axe Cop' in i1I1i111Ii :
    pass
   elif 'Baby Playpen' in i1I1i111Ii :
    pass
   elif 'Beavis and Butt' in i1I1i111Ii :
    pass
   elif 'Celebrity Deathmatch' in i1I1i111Ii :
    pass
   elif 'Clerks The' in i1I1i111Ii :
    pass
   elif 'Crapston Villas' in i1I1i111Ii :
    pass
   elif 'Duckman:' in i1I1i111Ii :
    pass
   elif 'Stripperella' in i1I1i111Ii :
    pass
   elif 'Vixen' in i1I1i111Ii :
    pass
   else :
    II1I ( '[COLORgreen]' + i1I1i111Ii + '[/COLOR]' , iIII , 10006 , ooOooo000oOO + 'ORIGINCARTOON.png' , i1iiIII111ii , '' )
  xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 63 - 63: o0oOO0O00o0O * Ii1I . ii / IIIii1II1II * I1ii11iIi11i . O0OoO
def Ooo0 ( url ) :
 IIiI1Ii = iiI111I1iIiI ( url )
 Ii1i = re . compile ( '<td><a href="(.+?)">(.+)</a></td>' ) . findall ( IIiI1Ii )
 for url , i1I1i111Ii in Ii1i :
  if 'Dad!' in i1I1i111Ii :
   pass
  elif 'Family Guy' in i1I1i111Ii :
   pass
  elif '2 Stupid' in i1I1i111Ii :
   pass
  elif 'The Zelfs' in i1I1i111Ii :
   pass
  elif 'A Clone' in i1I1i111Ii :
   pass
  elif 'A.T.O.M' in i1I1i111Ii :
   pass
  elif 'Almost Naked' in i1I1i111Ii :
   pass
  elif 'Angry Kid' in i1I1i111Ii :
   pass
  elif 'Annoying Orange' in i1I1i111Ii :
   pass
  elif 'Aqua Teen' in i1I1i111Ii :
   pass
  elif 'Assy Mcgee' in i1I1i111Ii :
   pass
  elif 'Astroblast' in i1I1i111Ii :
   pass
  elif 'Atomic Betty' in i1I1i111Ii :
   pass
  elif 'Axe Cop' in i1I1i111Ii :
   pass
  elif 'Baby Playpen' in i1I1i111Ii :
   pass
  elif 'Beavis and Butt' in i1I1i111Ii :
   pass
  elif 'Celebrity Deathmatch' in i1I1i111Ii :
   pass
  elif 'Clerks The' in i1I1i111Ii :
   pass
  elif 'Crapston Villas' in i1I1i111Ii :
   pass
  elif 'Duckman:' in i1I1i111Ii :
   pass
  elif 'Stripperella' in i1I1i111Ii :
   pass
  elif 'Vixen' in i1I1i111Ii :
   pass
  else :
   II1I ( '[COLORgreen]' + i1I1i111Ii + '[/COLOR]' , url , 10006 , ooOooo000oOO + 'ORIGINCARTOON.png' , i1iiIII111ii , '' )
 xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 91 - 91: ooOoO0O00 - iI11I1II1I1I
def Oo0Oo00o00oO ( url ) :
 IIiI1Ii = iiI111I1iIiI ( url )
 I1 = re . compile ( '<img src="(.+?)" id="series_image" width="250" height="370" alt=".+?" />' ) . findall ( IIiI1Ii )
 for iiI1IIIi in I1 :
  o0000 = iiI1IIIi
 i111i1i = re . compile ( '<li><a href="(.+?)">Next</a></li>' ) . findall ( IIiI1Ii )
 for url in i111i1i :
  II1I ( '[COLORgreen]NEXT PAGE[/COLOR]' , url , 10006 , ooOooo000oOO + 'Next.png' , i1iiIII111ii , '' )
 Ii1i = re . compile ( '&nbsp;<a href="(.+?)">(.+?)</a>' ) . findall ( IIiI1Ii )
 for url , i1I1i111Ii in Ii1i :
  OO0ooOOO00 ( '[COLORgreen]' + i1I1i111Ii + '[/COLOR]' , url , 10007 , o0000 )
  if 19 - 19: IIiIiII11i - ooOoO0O00 - IIIii1II1II / IIIii1II1II + OOooOOo
  if 51 - 51: I1ii11iIi11i % OOooOOo * ii . Ii
 xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 77 - 77: IIiIiII11i
def I1i111IiIiIi1 ( url , IMAGE ) :
 IIiI1Ii = iiI111I1iIiI ( url )
 Ii1i = re . compile ( '"playlist">(.+?)</span></div><div><iframe src="(.+?)"' ) . findall ( IIiI1Ii )
 for i1I1i111Ii , url in Ii1i :
  print i1I1i111Ii + '     ' + url
  if 'easy' in url :
   i1II11II1 ( url )
   if 5 - 5: I1ii11iIi11i - Ii1I % OoOo00o - IIiIiII11i . oOo0O0Ooo + o0oOO0O00o0O
   if 47 - 47: o0o00Oo0O - iI11I1II1I1I - o0oOO0O00o0O
  xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 46 - 46: Ii11Ii1I . IIIii1II1II * oO0o . ii + Ii1I
def i1II11II1 ( url ) :
 IIiI1Ii = iiI111I1iIiI ( url )
 Ii1i = re . compile ( "url: '(.+?)'," ) . findall ( IIiI1Ii )
 for url in Ii1i :
  oo0000o ( url )
  if 12 - 12: I11i + Ii11Ii1I + I11i
  if 95 - 95: Ii11Ii1I + Ii1I * IIIii1II1II
  if 16 - 16: iI1iI1I1i1I / oOo0O0Ooo + oO0o % iI11I1II1I1I - ooOoO0O00 . OoOo00o
def iIi1iIIIiIiI ( ) :
 if 62 - 62: Ii % IIIii1II1II . OooO0OoOOOO . IIIii1II1II
 II1I ( '[COLORgreen]Stand Up[/COLOR]' , '' , 10014 , ooOooo000oOO + 'ORIGINSTANDUP.png' , i1iiIII111ii , '' )
 II1I ( '[COLORgreen]Search Comedian[/COLOR]' , '' , 10015 , ooOooo000oOO + 'ORIGINSTANDUP.png' , i1iiIII111ii , '' )
 II1I ( '[COLORgreen]Others[/COLOR]' , '' , 10017 , ooOooo000oOO + 'ORIGINSTANDUP.png' , i1iiIII111ii , '' )
 if 84 - 84: Ii * oO0o
def I1I1iII1i ( ) :
 o00OO00OoO = iiI111I1iIiI ( ( i1111 ( 'aHR0cDovL2JhY2syYmFzaWNzYnVpbGQuY28udWsvdGVzdC9zdGFuZHVwbGlzdC5waHA=' ) ) )
 Ii1i = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( o00OO00OoO )
 for iIII , iiI1IIIi , i1I1i111Ii in Ii1i :
  if 'elete' in i1I1i111Ii :
   pass
  else :
   OO0ooOOO00 ( '[COLORgreen]' + i1I1i111Ii + '[/COLOR]' , iIII , 222 , iiI1IIIi )
   if 30 - 30: o0o00Oo0O + Ii1I + IIiIiII11i
def III1I ( ) :
 Ooo0OOoOoO0 = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 IIo0Oo0oO0oOO00 = Ooo0OOoOoO0 . lower ( )
 o00OO00OoO = iiI111I1iIiI ( ( i1111 ( 'aHR0cDovL3d3dy5jb3VjaHRyaXBwZXIuY29tL2ZvcnVtMi9wYWdlLnBocD9wYWdlPTM=' ) ) )
 I1I111iIi = re . compile ( '<tr>.+?<td width=".+?" align=".+?">.+?<img border=".+?" src="..(.+?)" width=".+?" height=".+?"></td>.+?<td width=".+?" valign=".+?" align=".+?"><font size=".+?">(.+?)</font></td>.+?<td width=".+?">(.+?)</td>' , re . DOTALL ) . findall ( o00OO00OoO )
 for iiI1IIIi , OoOOOO , i1iII1IiiIiI1 in I1I111iIi :
  for Ooo0OOoOoO0 in OoOOOO :
   print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< img >>>>>>>>>>>>>>>>>>>>>>>>>>'
   I1iiIi111I = re . compile ( '<a href="(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( i1iII1IiiIiI1 )
   for iIII , i1I1i111Ii in I1iiIi111I :
    if 'tube' in iIII :
     pass
    elif 'stage' in iIII :
     OO0ooOOO00 ( '[COLORgreen]' + OoOOOO + '   -   ' + i1I1i111Ii + '[/COLOR]' , ( iIII ) . replace ( '" target="_blank' , '' ) , 10016 , 'http://couchtripper.com/' + iiI1IIIi , )
    elif 'vee' in iIII :
     pass
     if 34 - 34: Ii - IIiIiII11i / oOo0O0Ooo % I11i
def iI1IiiiI11 ( ) :
 o00OO00OoO = iiI111I1iIiI ( ( i1111 ( 'aHR0cDovL3d3dy5jb3VjaHRyaXBwZXIuY29tL2ZvcnVtMi9wYWdlLnBocD9wYWdlPTM=' ) ) )
 I1I111iIi = re . compile ( '<tr>.+?<td width=".+?" align=".+?">.+?<img border=".+?" src="..(.+?)" width=".+?" height=".+?"></td>.+?<td width=".+?" valign=".+?" align=".+?"><font size=".+?">(.+?)</font></td>.+?<td width=".+?">(.+?)</td>' , re . DOTALL ) . findall ( o00OO00OoO )
 for iiI1IIIi , OoOOOO , i1iII1IiiIiI1 in I1I111iIi :
  I1iiIi111I = re . compile ( '<a href="(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( i1iII1IiiIiI1 )
  for iIII , i1I1i111Ii in I1iiIi111I :
   if 'tube' in iIII :
    pass
   elif 'stage' in iIII :
    OO0ooOOO00 ( '[COLORgreen]' + OoOOOO + '   -   ' + i1I1i111Ii + '[/COLOR]' , ( iIII ) . replace ( '" target="_blank' , '' ) , 10016 , 'http://couchtripper.com/' + iiI1IIIi )
   elif 'vee' in iIII :
    pass
    if 80 - 80: OoOo00o + I11i * Ii11Ii1I + oO0o
    if 75 - 75: iI1iI1I1i1I / I11i / IIIii1II1II / OooO0OoOOOO % O0OoO + IIiIiII11i
 xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 4 - 4: o0oOO0O00o0O - I1ii11iIi11i - OooO0OoOOOO - iI1iI1I1i1I % Ii / oO0o
def i1iii11 ( url ) :
 o00OO00OoO = iiI111I1iIiI ( url )
 print '>>>>>>>>>>>>>>>>>>>>>>>>' + url + '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'
 iI1iiiiIii = re . compile ( "url\[.+?\] = '(.+?)';" ) . findall ( o00OO00OoO )
 print '>>>>>>>>>>>>>>>>>>>>>>>' + ( str ( iI1iiiiIii ) ) + '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
 for url in iI1iiiiIii :
  oo0000o ( ( url ) . replace ( '[' , '' ) . replace ( ']' , '' ) . replace ( '\'' , '' ) )
  if 92 - 92: OOooOOo . ii - IIIi
  if 74 - 74: iI11I1II1I1I % o0oOO0O00o0O * IIIii1II1II * iI11I1II1I1I
  if 73 - 73: I11i % IIIi . IIIii1II1II
  if 60 - 60: OOooOOo
  if 5 - 5: oOo0O0Ooo - oOo0O0Ooo - oOo0O0Ooo * ii
  if 28 - 28: iI11I1II1I1I + iI11I1II1I1I
  if 28 - 28: OoOo00o
def ooo0oo ( ) :
 if 8 - 8: oO0o + OOooOOo . iI11I1II1I1I % o0o00Oo0O
 iI11Ii111 ( '[COLOR darkgoldenrod]Open Pandora\'s Box[/COLOR]' , '' , 10029 , 'https://encrypted-tbn1.gstatic.com/images?q=tbn%3AANd9GcTQ9r4TA8yIw9ggxuwsHxWojo6tPVfgTe8QIOxOQwzNR2TavtCi6Q' , i1iiIII111ii , '' )
 iI11Ii111 ( '[COLOR darkgoldenrod]Search[/COLOR]' , '' , 10026 , 'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png' , i1iiIII111ii , '' )
 if 54 - 54: OOooOOo % o0oOO0O00o0O . OOooOOo * IIIii1II1II + OOooOOo % ooOoO0O00
 iiO0o0oOOOoOo ( 'movies' , 'MAIN' )
 if 23 - 23: IIIi - IIIii1II1II + Ii11Ii1I - OOooOOo * OOooOOo . I1ii11iIi11i
def iIii11iI1II ( ) :
 iI11Ii111 ( 'Search Pandoras Films' , '' , 10027 , 'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png' , i1iiIII111ii , '' )
 iI11Ii111 ( 'Search Pandoras TV' , '' , 10028 , 'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png' , i1iiIII111ii , '' )
 if 42 - 42: O0OoO - oOo0O0Ooo + Ii1I % Ii11Ii1I
 iiO0o0oOOOoOo ( 'movies' , 'MAIN' )
def IiIi1III ( ) :
 if 47 - 47: ii % o0o00Oo0O * o0oOO0O00o0O . Ii11Ii1I
 Ooo0OOoOoO0 = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 IIo0Oo0oO0oOO00 = Ooo0OOoOoO0 . lower ( )
 ii111Iiii = [ '480p' , '720p' , '1080p' , 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' , '720paction' , '720padventure' , '720panimation' , '720pcomedy' , '720pcrime' , '720pdocumentary' , '720pdrama' , '720pfamily' , '720pfantasy' , '720phorror' , '720pmystery' , '720promance' , '720psci-Fi' , '720psport' , '720pthriller' , '720pwestern' , '1080paction' , '1080padventure' , '1080panimation' , '1080pcomedy' , '1080pcrime' , '1080pdocumentary' , '1080pdrama' , '1080pfamily' , '1080pfantasy' , '1080phorror' , '1080pmystery' , '1080promance' , '1080psci-Fi' , '1080psport' , '1080pthriller' , '1080pwestern' , 'films' ]
 if 54 - 54: ii - oOo0O0Ooo % Ii1I
 for oO0Ooo0OooOOo in ii111Iiii :
  O00o0O = IIIII + oO0Ooo0OooOOo + ooOoOoo0O
  o00OO00OoO = O000OO0 ( O00o0O )
  Ii1i = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( o00OO00OoO )
  for iIII , OOOOoO00o0O , iIIiiiI , I1I1I1IIi1III , i1I1i111Ii in Ii1i :
   if Ooo0OOoOoO0 in i1I1i111Ii . lower ( ) :
    iIIIiI ( i1I1i111Ii , iIII , 222 , OOOOoO00o0O , I1I1I1IIi1III , iIIiiiI )
    if 93 - 93: O0OoO . iI11I1II1I1I % Ii . OOooOOo % O0OoO + o0o00Oo0O
    iiO0o0oOOOoOo ( 'movies' , 'MAIN' )
    xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
    if 65 - 65: Ii11Ii1I + oO0o - ii
    if 51 - 51: I1ii11iIi11i + OoOo00o / o0oOO0O00o0O - ooOoO0O00
def oO0O0oO0 ( ) :
 if 15 - 15: O0OoO * OOooOOo % OooO0OoOOOO . OOooOOo . iI1iI1I1i1I
 Ooo0OOoOoO0 = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 IIo0Oo0oO0oOO00 = Ooo0OOoOoO0 . lower ( )
 ii111Iiii = [ 'tvnum' , 'a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' , 'p' , 'q' , 'r' , 's' , 't' , 'u' , 'v' , 'w' , 'x' , 'y' , 'z' ]
 if 97 - 97: OoOo00o
 for oO0Ooo0OooOOo in ii111Iiii :
  oOoO0O00oo = IIIII + oO0Ooo0OooOOo + ooOoOoo0O
  o00OO00OoO = O000OO0 ( oOoO0O00oo )
  Ii1i = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( o00OO00OoO )
  for i1I1i111Ii , iIIiiiI , iIII , iiI1IIIi , I1I1I1IIi1III , OOoOoo00Oo in Ii1i :
   if Ooo0OOoOoO0 in i1I1i111Ii . lower ( ) :
    iI11Ii111 ( i1I1i111Ii , iIII , OOoOoo00Oo , iiI1IIIi , I1I1I1IIi1III , iIIiiiI )
    if 9 - 9: IIiIiII11i * IIiIiII11i . Ii * iI11I1II1I1I
    iiO0o0oOOOoOo ( 'movies' , 'MAIN' )
    xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
    if 18 - 18: oO0o . IIiIiII11i % OOooOOo % Ii11Ii1I
    if 87 - 87: iI11I1II1I1I . ii * OOooOOo
def OOOoo0ooOo00O ( ) :
 if 38 - 38: iI11I1II1I1I + Ii * oO0o * O0OoO % IIIii1II1II
 IIiI1Ii = iiI111I1iIiI ( IIIII + 'spongemain.php' )
 Ii1i = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( IIiI1Ii )
 for i1I1i111Ii , iIIiiiI , iIII , iiI1IIIi , I1I1I1IIi1III , OOoOoo00Oo in Ii1i :
  iI11Ii111 ( i1I1i111Ii , iIII , OOoOoo00Oo , iiI1IIIi , I1I1I1IIi1III , iIIiiiI )
  iiO0o0oOOOoOo ( 'movies' , 'MAIN' )
def I1I11IiiI ( url ) :
 if 40 - 40: iI1iI1I1i1I % ii - IIIii1II1II + I11i / IIIii1II1II
 xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
 ooOiii1 = ( '%s%s' % ( OO0o0oO0O000o , url ) )
 O000oo0O = iiI111I1iIiI ( url )
 Ii1i = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( O000oo0O )
 for url , OOOOoO00o0O , iIIiiiI , I1iI11iii , i1I1i111Ii in Ii1i :
  iIIIiI ( i1I1i111Ii , url , 222 , OOOOoO00o0O , I1iI11iii , iIIiiiI )
  if 78 - 78: o0o00Oo0O / IIiIiII11i * oO0o
  iiO0o0oOOOoOo ( 'movies' , 'MAIN' )
  if 50 - 50: ii - iI11I1II1I1I + ooOoO0O00 % IIIi - iI11I1II1I1I % o0o00Oo0O
  xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 58 - 58: OooO0OoOOOO + iI11I1II1I1I
  if 65 - 65: IIiIiII11i - IIIi % I11i - OOooOOo * o0oOO0O00o0O + Ii11Ii1I
def O0o0O0OO0o ( url ) :
 if 54 - 54: OOooOOo . OoOo00o % Ii / ii + OooO0OoOOOO % OoOo00o
 IIiI1Ii = iiI111I1iIiI ( url )
 Ii1i = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( IIiI1Ii )
 for i1I1i111Ii , iIIiiiI , url , iiI1IIIi , I1I1I1IIi1III , OOoOoo00Oo in Ii1i :
  iI11Ii111 ( i1I1i111Ii , url , OOoOoo00Oo , iiI1IIIi , I1I1I1IIi1III , iIIiiiI )
  if 36 - 36: OoOo00o
  iiO0o0oOOOoOo ( 'movies' , 'MAIN' )
  if 74 - 74: ii
  if 72 - 72: o0o00Oo0O + oOo0O0Ooo - o0oOO0O00o0O - oO0o
 xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 100 - 100: o0o00Oo0O
def iIIIiI ( name , url , mode , iconimage , fanart , description ) :
 if 79 - 79: iI11I1II1I1I
 O00oO0o = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 I1i1iii = True
 IiI1iI1 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 IiI1iI1 . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 IiI1iI1 . setProperty ( "Fanart_Image" , fanart )
 I1i1iii = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = O00oO0o , listitem = IiI1iI1 , isFolder = False )
 return I1i1iii
 if 23 - 23: o0oOO0O00o0O + IIIii1II1II * O0OoO / iI11I1II1I1I - o0oOO0O00o0O
def iI11Ii111 ( name , url , mode , iconimage , fanart , description ) :
 if 80 - 80: oOo0O0Ooo - iI11I1II1I1I . IIIii1II1II + oO0o - IIIi
 O00oO0o = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 I1i1iii = True
 IiI1iI1 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 IiI1iI1 . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 IiI1iI1 . setProperty ( "Fanart_Image" , fanart )
 I1i1iii = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = O00oO0o , listitem = IiI1iI1 , isFolder = True )
 return I1i1iii
if 5 - 5: o0oOO0O00o0O
if 62 - 62: OOooOOo . ii . IIIii1II1II . oO0o * o0oOO0O00o0O
if 78 - 78: OoOo00o / oO0o - OoOo00o * ii . OOooOOo
if 96 - 96: oOo0O0Ooo % ooOoO0O00 . I11i . o0o00Oo0O
if 37 - 37: ooOoO0O00 - IIIii1II1II % ii / IIIii1II1II % O0OoO
if 48 - 48: Ii % OoOo00o
if 29 - 29: o0oOO0O00o0O + Ii % iI1iI1I1i1I
if 93 - 93: OOooOOo % iI11I1II1I1I
if 90 - 90: oOo0O0Ooo - IIIii1II1II / Ii11Ii1I / o0o00Oo0O / iI1iI1I1i1I
if 87 - 87: OOooOOo / OooO0OoOOOO + iI11I1II1I1I
if 93 - 93: iI11I1II1I1I + OoOo00o % O0OoO
if 21 - 21: IIIii1II1II
if 6 - 6: OooO0OoOOOO
if 46 - 46: OooO0OoOOOO + OoOo00o
if 79 - 79: ii - OooO0OoOOOO * OooO0OoOOOO . OOooOOo
def Oo00ooO0OoOo ( string ) :
 if iiiiiIIii == 'true' :
  xbmc . log ( "[addon.live.GenieTV-%s]: %s" % ( addon_version , string ) )
  if 99 - 99: OOooOOo
def oO00OoOo ( name , url , iconimage , fanart , mode , playlist = None , regexs = None ) :
 OoOi111i = [ ]
 try :
  if 46 - 46: oO0o * I1ii11iIi11i % OoOo00o + o0o00Oo0O * OooO0OoOOOO
  name = name . encode ( 'utf-8' , 'ignore' )
 except :
  pass
 if os . path . exists ( I11i1 ) == False :
  Oo00ooO0OoOo ( 'Making Favorites File' )
  OoOi111i . append ( ( name , url , iconimage , fanart , mode , playlist , regexs ) )
  IiIIIIIi = open ( I11i1 , "w" )
  IiIIIIIi . write ( json . dumps ( OoOi111i ) )
  IiIIIIIi . close ( )
 else :
  Oo00ooO0OoOo ( 'Appending Favorites' )
  IiIIIIIi = open ( I11i1 ) . read ( )
  ii1I11i = json . loads ( IiIIIIIi )
  ii1I11i . append ( ( name , url , iconimage , fanart , mode ) )
  i1IiiI1iIi = open ( I11i1 , "w" )
  i1IiiI1iIi . write ( json . dumps ( ii1I11i ) )
  i1IiiI1iIi . close ( )
  if 89 - 89: IIIi . OooO0OoOOOO % I1ii11iIi11i . I1ii11iIi11i - ii
  if 56 - 56: iI1iI1I1i1I
def IiI1 ( ) :
 if os . path . exists ( I11i1 ) == False :
  OoOi111i = [ ]
  Oo00ooO0OoOo ( 'Making Favorites File' )
  OoOi111i . append ( ( 'Genie Tv Favourites Section' , '' , '' , '' , '' , '' , '' ) )
  IiIIIIIi = open ( I11i1 , "w" )
  IiIIIIIi . write ( json . dumps ( OoOi111i ) )
  IiIIIIIi . close ( )
 else :
  O0oOIiIII = json . loads ( open ( I11i1 ) . read ( ) )
  IIiI1111i1 = len ( O0oOIiIII )
  for ii1ii1I1IIi1 in O0oOIiIII :
   i1I1i111Ii = ii1ii1I1IIi1 [ 0 ]
   iIII = ii1ii1I1IIi1 [ 1 ]
   OOOOoO00o0O = ii1ii1I1IIi1 [ 2 ]
   try :
    oOOoo0 = ii1ii1I1IIi1 [ 3 ]
    if oOOoo0 == None :
     raise
   except :
    if o0oO0 . getSetting ( 'use_thumb' ) == "true" :
     oOOoo0 = OOOOoO00o0O
    else :
     oOOoo0 = I1I1I1IIi1III
   try : IIIIiI11I = ii1ii1I1IIi1 [ 5 ]
   except : IIIIiI11I = None
   try : iiiI11iIIi1 = ii1ii1I1IIi1 [ 6 ]
   except : iiiI11iIIi1 = None
   if 72 - 72: o0oOO0O00o0O * IIIii1II1II
   if ii1ii1I1IIi1 [ 4 ] == 0 :
    II1I ( i1I1i111Ii , iIII , '' , OOOOoO00o0O , I1I1I1IIi1III , '' , 'fav' )
   else :
    II1I ( i1I1i111Ii , iIII , ii1ii1I1IIi1 [ 4 ] , OOOOoO00o0O , I1I1I1IIi1III , '' , 'fav' )
    if 67 - 67: ooOoO0O00
def iii ( name ) :
 ii1I11i = json . loads ( open ( I11i1 ) . read ( ) )
 for oOOOo in range ( len ( ii1I11i ) ) :
  if ii1I11i [ oOOOo ] [ 0 ] == name :
   del ii1I11i [ oOOOo ]
   i1IiiI1iIi = open ( I11i1 , "w" )
   i1IiiI1iIi . write ( json . dumps ( ii1I11i ) )
   i1IiiI1iIi . close ( )
   break
 xbmc . executebuiltin ( "XBMC.Container.Refresh" )
 if 31 - 31: OOooOOo + OOooOOo . Ii / O0OoO % iI1iI1I1i1I / OOooOOo
 if 29 - 29: Ii1I * Ii1I . oO0o * iI1iI1I1i1I % iI11I1II1I1I * Ii1I
def Oo0 ( ) :
 iIiiIIi1iiII = os . path . join ( OOooO0OOoo , 'addons.ini' )
 oooO00Oo = open ( iIiiIIi1iiII , "w+" )
 if 86 - 86: IIiIiII11i + O0OoO + OooO0OoOOOO
 oooO00Oo . write ( r'# This file contains the "built-in" channels' + '\n' )
 oooO00Oo . write ( r'# It is parsed by Pythons ConfigParser' + '\n\n' )
 oooO00Oo . write ( r'[plugin.video.GenieTv]' + '\n' )
 oooO00Oo . write ( r'BBC One=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F191.m3u8&mode=10012&name=[COLORgreen]BBC+One%0D[%2FCOLOR]' + '\n' )
 oooO00Oo . write ( r'BBC Two=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F190.m3u8&mode=10012&name=[COLORgreen]BBC+Two%0D[%2FCOLOR]' + '\n' )
 oooO00Oo . write ( r'BBC Four=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F188.m3u8&mode=10012&name=[COLORgreen]BBC+Four%0D[%2FCOLOR]' + '\n' )
 oooO00Oo . write ( r'ITV=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F208.m3u8&mode=10012&name=[COLORgreen]ITV1%0D[%2FCOLOR]' + '\n' )
 oooO00Oo . write ( r'ITV2=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F207.m3u8&mode=10012&name=[COLORgreen]ITV2%0D[%2FCOLOR]' + '\n' )
 oooO00Oo . write ( r'ITV3=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F206.m3u8&mode=10012&name=[COLORgreen]ITV3%0D[%2FCOLOR]' + '\n' )
 oooO00Oo . write ( r'ITV4=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F205.m3u8&mode=10012&name=[COLORgreen]ITV4%0D[%2FCOLOR]' + '\n' )
 oooO00Oo . write ( r'Channel 4=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F183.m3u8&mode=10012&name=[COLORgreen]Channel+4%0D[%2FCOLOR]' + '\n' )
 oooO00Oo . write ( r'Channel 5=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F185.m3u8&mode=10012&name=[COLORgreen]Channel+5%0D[%2FCOLOR]' + '\n' )
 oooO00Oo . write ( r'5STAR=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F187.m3u8&mode=10012&name=[COLORgreen]5%2A%0D[%2FCOLOR]' + '\n' )
 oooO00Oo . write ( r'5 USA=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F186.m3u8&mode=10012&name=[COLORgreen]5USA%0D[%2FCOLOR]' + '\n' )
 oooO00Oo . write ( r'RTE One=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F194.m3u8&mode=10012&name=[COLORgreen]RTE+One%0D[%2FCOLOR]' + '\n' )
 oooO00Oo . write ( r'RTE Two=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F193.m3u8&mode=10012&name=[COLORgreen]RTE+Two%0D[%2FCOLOR]' + '\n' )
 oooO00Oo . write ( r'TG4=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F192.m3u8&mode=10012&name=[COLORgreen]TG4%0D[%2FCOLOR]' + '\n' )
 oooO00Oo . write ( r'Sky1=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F32.m3u8&mode=10012&name=[COLORgreen]Sky+1%0D[%2FCOLOR]' + '\n' )
 oooO00Oo . write ( r'Sky2=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F33.m3u8&mode=10012&name=[COLORgreen]Sky+2%0D[%2FCOLOR]' + '\n' )
 oooO00Oo . write ( r'Sky Living=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F35.m3u8&mode=10012&name=[COLORgreen]Sky+Living%0D[%2FCOLOR]' + '\n' )
 oooO00Oo . write ( r'Sky Atlantic=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F34.m3u8&mode=10012&name=[COLORgreen]Sky+Atlantic%0D[%2FCOLOR]' + '\n' )
 oooO00Oo . write ( r'Dave=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F325.m3u8&mode=10012&name=[COLORgreen]Dave%0D[%2FCOLOR]' + '\n' )
 oooO00Oo . write ( r'Pick=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F324.m3u8&mode=10012&name=[COLORgreen]Pick%0D[%2FCOLOR]' + '\n' )
 oooO00Oo . write ( r'GOLD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F326.m3u8&mode=10012&name=[COLORgreen]Gold%0D[%2FCOLOR]' + '\n' )
 oooO00Oo . write ( r'Watch HD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F518.m3u8&mode=10012&name=[COLORgreen]Watch%0D[%2FCOLOR]' + '\n' )
 oooO00Oo . write ( r'YESTERDAY=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F377.m3u8&mode=10012&name=[COLORgreen]Yesterday%0D[%2FCOLOR]' + '\n' )
 oooO00Oo . write ( r'Comedy Central=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F181.m3u8&mode=10012&name=[COLORgreen]Comedy+Central%0D[%2FCOLOR]' + '\n' )
 oooO00Oo . write ( r'London Live=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F830.m3u8&mode=10012&name=[COLORgreen]London+Live%0D[%2FCOLOR]' + '\n' )
 oooO00Oo . write ( r'Disney Junior=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F230.m3u8&mode=10012&name=[COLORgreen]Disney+Jr.%0D[%2FCOLOR]' + '\n' )
 oooO00Oo . write ( r'Disney Chnl=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F231.m3u8&mode=10012&name=[COLORgreen]Disney+Channel%0D[%2FCOLOR]' + '\n' )
 oooO00Oo . write ( r'Animal Planet=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F198.m3u8&mode=10012&name=[COLORgreen]Animal+Planet%0D[%2FCOLOR]' + '\n' )
 oooO00Oo . write ( r'Nat Geo=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F197.m3u8&mode=10012&name=[COLORgreen]National+Geographic+Channel%0D[%2FCOLOR]' + '\n' )
 oooO00Oo . write ( r'Discovery=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F200.m3u8&mode=10012&name=[COLORgreen]Discovery+Channel%0D[%2FCOLOR]' + '\n' )
 oooO00Oo . write ( r'Discovery Science=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F199.m3u8&mode=10012&name=[COLORgreen]Discovery+Science%0D[%2FCOLOR]' + '\n' )
 oooO00Oo . write ( r'Disc.Turbo=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F168.m3u8&mode=10012&name=[COLORgreen]Discovery+Turbo%0D[%2FCOLOR]' + '\n' )
 oooO00Oo . write ( r'Food Network=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F639.m3u8&mode=10012&name=[COLORgreen]Food+Network%0D[%2FCOLOR]' + '\n' )
 oooO00Oo . write ( r'MTV MUSIC=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F234.m3u8&mode=10012&name=[COLORgreen]MTV+Music%0D[%2FCOLOR]' + '\n' )
 oooO00Oo . write ( r'Film4=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F182.m3u8&mode=10012&name=[COLORgreen]Film4%0D[%2FCOLOR]' + '\n' )
 oooO00Oo . write ( r'True Movies=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F853.m3u8&mode=10012&name=[COLORgreen]True+Movies%0D[%2FCOLOR]' + '\n' )
 oooO00Oo . write ( r'True Movies 2=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F852.m3u8&mode=10012&name=[COLORgreen]True+Movies+2%0D[%2FCOLOR]' + '\n' )
 oooO00Oo . write ( r'Sky Action=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F732.m3u8&mode=10012&name=[COLORgreen]Sky+Movies+Action+%26+Adventure%0D[%2FCOLOR]' + '\n' )
 oooO00Oo . write ( r'Sky ScFiHorror=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F511.m3u8&mode=10012&name=[COLORgreen]Sky+Movies+Sci-Fi+%26+Horror%0D[%2FCOLOR]' + '\n' )
 oooO00Oo . write ( r'SkyPremiereHD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F516.m3u8&mode=10012&name=[COLORgreen]Sky+Movies+Premiere%0D[%2FCOLOR]' + '\n' )
 oooO00Oo . write ( r'Sky Greats=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F512.m3u8&mode=10012&name=[COLORgreen]Sky+Movies+Greats%0D[%2FCOLOR]' + '\n' )
 oooO00Oo . write ( r'Sky Family=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F509.m3u8&mode=10012&name=[COLORgreen]Sky+Movies+Family%0D[%2FCOLOR]' + '\n' )
 oooO00Oo . write ( r'Sky DramaRom=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F510.m3u8&mode=10012&name=[COLORgreen]Sky+Movies+Drama+%26+Romance%0D[%2FCOLOR]' + '\n' )
 oooO00Oo . write ( r'Sky Thriller=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F514.m3u8&mode=10012&name=[COLORgreen]Sky+Movies+Crime+%26+Thriller%0D[%2FCOLOR]' + '\n' )
 oooO00Oo . write ( r'Sky Comedy=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F513.m3u8&mode=10012&name=[COLORgreen]Sky+Movies+Comedy%0D[%2FCOLOR]' + '\n' )
 oooO00Oo . write ( r'Sky Showcase=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F46.m3u8&mode=10012&name=[COLORgreen]Sky+Movies+Showcase%0D[%2FCOLOR]' + '\n' )
 oooO00Oo . write ( r'Sky Select=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F45.m3u8&mode=10012&name=[COLORgreen]Sky+Movies+Select%0D[%2FCOLOR]' + '\n' )
 oooO00Oo . write ( r'Sky Disney=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F195.m3u8&mode=10012&name=[COLORgreen]Sky+Movies+Disney%0D[%2FCOLOR]' + '\n' )
 oooO00Oo . write ( r'Sky Sports 1=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F18.m3u8&mode=10012&name=[COLORgreen]Sky+Sports+1%0D[%2FCOLOR]' + '\n' )
 oooO00Oo . write ( r'Sky Sports 2=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F19.m3u8&mode=10012&name=[COLORgreen]Sky+Sports+2%0D[%2FCOLOR]' + '\n' )
 oooO00Oo . write ( r'Sky Sports 3=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F20.m3u8&mode=10012&name=[COLORgreen]Sky+Sports+3%0D[%2FCOLOR]' + '\n' )
 oooO00Oo . write ( r'Sky Sports 4=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F21.m3u8&mode=10012&name=[COLORgreen]Sky+Sports+4%0D[%2FCOLOR]' + '\n' )
 oooO00Oo . write ( r'Sky Sports 5=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F22.m3u8&mode=10012&name=[COLORgreen]Sky+Sports+5%0D[%2FCOLOR]' + '\n' )
 oooO00Oo . write ( r'Sky Sports F1=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F24.m3u8&mode=10012&name=[COLORgreen]Sky+Sports+F1%0D[%2FCOLOR]' + '\n' )
 oooO00Oo . write ( r'Sky Sports News=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F23.m3u8&mode=10012&name=[COLORgreen]Sky+Sports+News%0D[%2FCOLOR]' + '\n' )
 oooO00Oo . write ( r'BT Sport 1=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F309.m3u8&mode=10012&name=[COLORgreen]BT+Sport+1%0D[%2FCOLOR]' + '\n' )
 oooO00Oo . write ( r'BT Sport 2=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F26.m3u8&mode=10012&name=[COLORgreen]BT+Sport+2%0D[%2FCOLOR]' + '\n' )
 oooO00Oo . write ( r'BT Sport Europe=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F705.m3u8&mode=10012&name=[COLORgreen]BT+Sport+Europe%0D[%2FCOLOR]' + '\n' )
 oooO00Oo . write ( r'BT Sport ESPN=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F28.m3u8&mode=10012&name=[COLORgreen]BT+Sport+ESPN%0D[%2FCOLOR]' + '\n' )
 oooO00Oo . write ( r'Box Nation=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F173.m3u8&mode=10012&name=[COLORgreen]Box+Nation%0D[%2FCOLOR]' + '\n' )
 oooO00Oo . write ( r'WWENetwork=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F178.m3u8&mode=10012&name=[COLORgreen]WWENetwork%0D[%2FCOLOR]' + '\n' )
 oooO00Oo . write ( r'Eurosport=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F269.m3u8&mode=10012&name=[COLORgreen]Eurosport+1%0D[%2FCOLOR]' + '\n' )
 oooO00Oo . write ( r'Eurosport 2=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F748.m3u8&mode=10012&name=[COLORgreen]Eurosport+2%0D[%2FCOLOR]' + '\n' )
 oooO00Oo . write ( r'At The Races=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F170.m3u8&mode=10012&name=[COLORgreen]At+the+Races%0D[%2FCOLOR]' + '\n' )
 oooO00Oo . write ( r'Racing UK=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F171.m3u8&mode=10012&name=[COLORgreen]Racing+UK%0D[%2FCOLOR]' + '\n' )
 oooO00Oo . write ( r'Poker central US=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F826.m3u8&mode=10012&name=[COLORgreen]Poker+central+US%0D[%2FCOLOR]' + '\n' )
 if 9 - 9: O0OoO + IIiIiII11i % O0OoO % OooO0OoOOOO + iI11I1II1I1I
 if 59 - 59: ooOoO0O00
 if 48 - 48: o0o00Oo0O * Ii11Ii1I * oO0o . oO0o * iI1iI1I1i1I - Ii11Ii1I
def iIi11i ( ) :
 if 56 - 56: Ii . O0OoO / o0oOO0O00o0O
 II1I ( '[COLORgreen]Recent Episodes[/COLOR]' , '' , 10019 , ooOooo000oOO + 'dtv.png' , i1iiIII111ii , '' )
 II1I ( '[COLORgreen]Genres[/COLOR]' , '' , 10020 , ooOooo000oOO + 'dtv.png' , i1iiIII111ii , '' )
 II1I ( '[COLORgreen]Search[/COLOR]' , '' , 10021 , ooOooo000oOO + 'dtv.png' , i1iiIII111ii , '' )
 if 48 - 48: oO0o * IIIii1II1II + iI11I1II1I1I / IIiIiII11i
def oOO0OO0oOO ( ) :
 if 85 - 85: o0o00Oo0O
 IIiI1Ii = cloudflare . source ( i1111 ( 'aHR0cDovL2RpemlsYWIuY29t' ) )
 Ii1i = re . compile ( '<li id=".+?">.+?<a href="(.+?)">.+?<img width="40" height="40" src="(.+?)" alt=""/>.+?<span class="title">\n(.+?)</span>.+?<span class="alt-title">\n(.+?)</span>.+?</a>.+?</li>' , re . DOTALL ) . findall ( IIiI1Ii )
 for iIII , iiI1IIIi , i1I1i111Ii , II1i11I in Ii1i :
  II1I ( i1I1i111Ii + '  -  ' + ( II1i11I ) . replace ( 'sezon' , 'Season' ) . replace ( 'bölüm' , 'Episode' ) , iIII , 10023 , ooOooo000oOO + 'dtv.png' , i1iiIII111ii , '' )
  if 32 - 32: ii . oO0o / I1ii11iIi11i * I11i / I11i * Ii11Ii1I
  if 19 - 19: Ii11Ii1I
  if 55 - 55: IIIii1II1II % IIIii1II1II / o0o00Oo0O % o0oOO0O00o0O - I11i . I1ii11iIi11i
def iiiii1I1III1 ( ) :
 if 12 - 12: o0oOO0O00o0O . OOooOOo * oOo0O0Ooo
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
 if 37 - 37: Ii1I * oOo0O0Ooo % Ii % ooOoO0O00 % OooO0OoOOOO
def iiiO0 ( url ) :
 i1II1 = 'http://dizilab.com/arsiv?limit=100&tur=' + url + '&orderby=&ulke=&order=&yil=&dizi_adi='
 o00OO00OoO = cloudflare . source ( i1II1 )
 Ii1i = re . compile ( '<div class="tv-series-single">.+?<a href="(.+?)" class="film-image">.+?<img src="(.+?)" alt=""/>.+?<span class="position">.+?</span>\n(.+?)</a>' , re . DOTALL ) . findall ( o00OO00OoO )
 for url , iiI1IIIi , i1I1i111Ii in Ii1i :
  II1I ( '[COLORgreen]' + i1I1i111Ii + '[/COLOR]' , url , 10022 , ooOooo000oOO + 'dtv.png' , i1iiIII111ii , '' )
  if 76 - 76: iI11I1II1I1I
  if 80 - 80: iI11I1II1I1I . o0o00Oo0O / Ii11Ii1I % Ii11Ii1I
  if 93 - 93: ii * I1ii11iIi11i
  if 10 - 10: IIIi * ii + iI1iI1I1i1I - Ii1I / Ii1I . Ii
def i1I1i ( ) :
 if 22 - 22: I1ii11iIi11i % oO0o - ii * I1ii11iIi11i
 Ooo0OOoOoO0 = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 IIo0Oo0oO0oOO00 = Ooo0OOoOoO0 . lower ( )
 iIII = ( i1111 ( 'aHR0cDovL2RpemlsYWIuY29tL2Fyc2l2P2xpbWl0PSZ0dXI9Jm9yZGVyYnk9JnVsa2U9Jm9yZGVyPSZ5aWw9JmRpemlfYWRpPQ==' ) ) + ( Ooo0OOoOoO0 ) . replace ( ' ' , '+' )
 o00OO00OoO = cloudflare . source ( iIII )
 Ii1i = re . compile ( '<a href="(.+?)" class="film-image">\n<img src="(.+?)" alt=""/>\n</a>\n<div class="tss-detail">\n<a class="title" style="" href=".+?">\n<span class="position">.+?</span>\n(.+?)</a>' ) . findall ( o00OO00OoO )
 for iIII , iiI1IIIi , i1I1i111Ii in Ii1i :
  if Ooo0OOoOoO0 in i1I1i111Ii . lower ( ) :
   II1I ( '[COLORgreen]' + i1I1i111Ii + '[/COLOR]' , iIII , 10022 , ooOooo000oOO + 'dtv.png' )
   if 38 - 38: iI11I1II1I1I / O0OoO
   if 13 - 13: iI11I1II1I1I
   if 77 - 77: Ii - iI11I1II1I1I / OoOo00o / O0OoO / oO0o
def ooo0O0o0OoOO ( url ) :
 o00OO00OoO = cloudflare . source ( url )
 Ii1i = re . compile ( '<a class="season" href="(.+?)">\n(.+?)\n</a>.+?<a class="episode" href=".+?">\n(.+?)\n</a>.+?<a class="episode-name" href=".+?">\n(.+?)</a>' , re . DOTALL ) . findall ( o00OO00OoO )
 for IiI1iiiIii , iIi11io0o00o0Oo , OOOOOo , i1I1i111Ii in Ii1i :
  oOOoo = ( OOOOOo ) . replace ( 'Sezon' , '' ) . replace ( 'bölüm' , '' ) . replace ( 'Bölüm' , '' ) . replace ( 'BÃ¶lÃ¼m' , '' ) . replace ( '.' , '' )
  i1I1iIii11 = ( iIi11io0o00o0Oo ) . replace ( 'bölüm' , '' ) . replace ( 'Sezon' , '' ) . replace ( 'Bölüm' , '' ) . replace ( 'BÃ¶lÃ¼m' , '' ) . replace ( '.' , '' )
  oOoO0O0oO = 'Season ' + i1I1iIii11 + 'Episode ' + oOOoo + i1I1i111Ii
  oOOoO ( oOoO0O0oO , IiI1iiiIii )
  if 87 - 87: OOooOOo % iI11I1II1I1I
  xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 72 - 72: IIIii1II1II . IIIii1II1II - Ii1I
  if 48 - 48: I1ii11iIi11i - O0OoO + I1ii11iIi11i - oOo0O0Ooo * Ii . o0oOO0O00o0O
def oOOoO ( name , url ) :
 IiI1iiiIii = url
 I1iIIIiI = name
 OOOO0OOoO0O0 = cloudflare . source ( IiI1iiiIii )
 I1 = re . compile ( 'file: "(.+?)",.+?label: "(.+?)",' , re . DOTALL ) . findall ( OOOO0OOoO0O0 )
 for iI1iiiiIii , Oo in I1 :
  OO0ooOOO00 ( '[COLORgreen]' + I1iIIIiI + Oo + '[/COLOR]' , iI1iiiiIii , 10012 , ooOooo000oOO + 'dtv.png' )
  if 34 - 34: oOo0O0Ooo
 xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 47 - 47: IIIi - IIIii1II1II / O0OoO - I1ii11iIi11i + o0oOO0O00o0O - iI11I1II1I1I
 if 68 - 68: Ii11Ii1I - OoOo00o + I1ii11iIi11i
def i11Iii1Ii1i1 ( ) :
 if 10 - 10: o0oOO0O00o0O . ooOoO0O00 + Ii11Ii1I
 if 66 - 66: oO0o % I11i
 if 21 - 21: OOooOOo - ii % Ii
 if 71 - 71: ooOoO0O00 - iI1iI1I1i1I * IIIi + OoOo00o - oO0o % Ii1I
 if 63 - 63: iI11I1II1I1I + IIIii1II1II . oO0o / oOo0O0Ooo
 if 84 - 84: ooOoO0O00
 if 42 - 42: IIiIiII11i - oO0o - ii . o0oOO0O00o0O / OOooOOo
 if 56 - 56: Ii - iI11I1II1I1I . IIiIiII11i
 if 81 - 81: OooO0OoOOOO / OOooOOo * OooO0OoOOOO . o0o00Oo0O
 if 61 - 61: oO0o * IIIii1II1II + IIIi . iI11I1II1I1I % iI1iI1I1i1I . IIIi
 if 53 - 53: IIIi * OooO0OoOOOO / iI11I1II1I1I / oOo0O0Ooo % Ii1I
 if 39 - 39: oO0o / ii . oO0o * Ii1I / OOooOOo
 if 38 - 38: oO0o / O0OoO % IIIi * iI1iI1I1i1I + Ii % O0OoO
 if 61 - 61: IIIi - Ii11Ii1I % Ii1I / O0OoO / o0oOO0O00o0O + iI11I1II1I1I
 if 87 - 87: IIIi + O0OoO + o0o00Oo0O / ooOoO0O00 % OooO0OoOOOO / IIIi
 II1I ( '[COLORgreen]Newest Episodes Added[/COLOR]' , 'http://www.watchseries.li/latest' , 10046 , ooOooo000oOO + 'WATCHSERIES.png' , '' , '' )
 II1I ( '[COLORgreen]This Week\'s Popular Episodes[/COLOR]' , 'http://www.watchseries.li/new' , 10042 , ooOooo000oOO + 'WATCHSERIES.png' , '' , '' )
 II1I ( '[COLORgreen]Search Program[/COLOR]' , '' , 10043 , ooOooo000oOO + 'WATCHSERIES.png' , '' , '' )
 if 64 - 64: oO0o % OooO0OoOOOO . IIIi % oO0o + iI1iI1I1i1I * OooO0OoOOOO
 if 83 - 83: I11i % OoOo00o + iI1iI1I1i1I % Ii + o0o00Oo0O
def OoOOoooO000 ( url ) :
 o00OO00OoO = iiI111I1iIiI ( url )
 ii1I1IIii11 = re . compile ( '<ul class="pagination" style="line-height: 3;">(.+?)</ul>' , re . DOTALL ) . findall ( o00OO00OoO )
 Ii1i = re . compile ( '<li><a href="/letters/(.+?)">(.+?)</a></li>' ) . findall ( str ( ii1I1IIii11 ) )
 for url , i1I1i111Ii in Ii1i :
  II1I ( '[COLORgreen]' + i1I1i111Ii + '[/COLOR]' , 'http://watchseries.li/letters/' + url , 10049 , ooOooo000oOO + 'WATCHSERIES.png' , '' , '' )
  if 85 - 85: oOo0O0Ooo % iI1iI1I1i1I + IIIii1II1II / Ii11Ii1I % ii
def i11i11II11i1 ( url ) :
 o00OO00OoO = iiI111I1iIiI ( url )
 Ii1i = re . compile ( '<a href="(.+?)" class="sr-header">(.+?)</a>' ) . findall ( o00OO00OoO )
 for url , i1I1i111Ii in Ii1i :
  II1I ( '[COLORgreen]' + i1I1i111Ii + '[/COLOR]' , 'http://watchseries.li/' + url , 10049 , ooOooo000oOO + 'WATCHSERIES.png' , '' , '' )
  if 17 - 17: IIiIiII11i + I1ii11iIi11i . IIIi
def I1I1i1i ( url ) :
 o00OO00OoO = iiI111I1iIiI ( url )
 Ii1i = re . compile ( '<li class="col-md-6 col-xs-12 list-movies-li"><a href="(.+?)" title=".+?">(.+?)<span class="epnum">.+?</span></a></li>' , re . DOTALL ) . findall ( o00OO00OoO )
 I1 = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="(.+?)">Next</a></li></ul>' , re . DOTALL ) . findall ( o00OO00OoO )
 for url , i1I1i111Ii in Ii1i :
  II1I ( '[COLORgreen]' + ( i1I1i111Ii ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' ) + '[/COLOR]' , 'http://www.watchseries.li' + url , 10044 , ooOooo000oOO + 'WATCHSERIES.png' , '' , '' )
 for url in I1 :
  II1I ( '[COLORgreen]' + 'NEXT' + '[/COLOR]' , 'http://www.watchseries.li' + url , 10049 , ooOooo000oOO + 'Next.png' , '' , '' )
  if 87 - 87: OOooOOo / OooO0OoOOOO . O0OoO - IIIii1II1II / oO0o
  if 41 - 41: IIiIiII11i
def II1Iiii11111 ( ) :
 Ooo0OOoOoO0 = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 iiI11I1iiIiII1I = 'http://www.watchseries.li/search/' + Ooo0OOoOoO0 . replace ( ' ' , '%20' )
 o00OO00OoO = iiI111I1iIiI ( iiI11I1iiIiII1I )
 Ii1i = re . compile ( '<img src="(.+?)".+?<a href="(.+?)" title=".+?"><b>(.+?)</b>' , re . DOTALL ) . findall ( o00OO00OoO )
 for iiI1IIIi , iIII , i1I1i111Ii in Ii1i :
  if 'watch online' in i1I1i111Ii :
   pass
  else :
   print iIII
   II1I ( '[COLORgreen]' + i1I1i111Ii + '[/COLOR]' , 'http://www.watchseries.li' + iIII , 10044 , iiI1IIIi , '' , '' )
   if 59 - 59: IIIi - OooO0OoOOOO
   xbmcplugin . setContent ( O0O , 'movies' )
   if 14 - 14: iI11I1II1I1I - iI11I1II1I1I
def i111i1I1ii1i ( url ) :
 o00OO00OoO = iiI111I1iIiI ( url )
 Ii1i = re . compile ( '<img src="(.+?)".+?<div class="block-left-home-inside-text">.+?<a href="(.+?)" title=".+?"><b>(.+?)</b> <br>.+?<span class=".+?">(.+?)</span></a><br>(.+?)<br>' , re . DOTALL ) . findall ( o00OO00OoO )
 for iiI1IIIi , url , i1I1i111Ii , OOOOOo , iIIiiiI in Ii1i :
  O0Oooo = ( i1I1i111Ii ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' ) + ' - ' + ( OOOOOo ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' )
  II1I ( '[COLORgreen]' + O0Oooo + '[/COLOR]' , 'http://www.watchseries.li' + url , 10045 , iiI1IIIi , '' , iIIiiiI )
  if 27 - 27: O0OoO + Ii * iI1iI1I1i1I + OOooOOo + o0oOO0O00o0O
def o0o ( url ) :
 o00OO00OoO = iiI111I1iIiI ( url )
 Ii1i = re . compile ( '<li class="col-md-6 col-xs-12 list-movies-li"><a href="(.+?)" title=".+?">(.+?)<span class="epnum">.+?</span></a></li>' , re . DOTALL ) . findall ( o00OO00OoO )
 I1 = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="(.+?)">Next</a></li></ul>' , re . DOTALL ) . findall ( o00OO00OoO )
 for url , i1I1i111Ii in Ii1i :
  O0Oooo = ( i1I1i111Ii ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' )
  II1I ( '[COLORgreen]' + O0Oooo + '[/COLOR]' , 'http://www.watchseries.li' + url , 10045 , ooOooo000oOO + 'WATCHSERIES.png' , '' , '' )
 for url in I1 :
  II1I ( '[COLORgreen]' + 'NEXT' + '[/COLOR]' , 'http://www.watchseries.li' + url , 10046 , ooOooo000oOO + 'Next.png' , '' , '' )
  if 17 - 17: OooO0OoOOOO / Ii1I - I11i * Ii1I
def i11i11II11i ( url ) :
 o00OO00OoO = iiI111I1iIiI ( url )
 Ii1i = re . compile ( '<div class="mask">.+?<a href="(.+?)" title="(.+?)">.+?<img src="(.+?)"' , re . DOTALL ) . findall ( o00OO00OoO )
 I1 = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="(.+?)">Next</a></li></ul>' , re . DOTALL ) . findall ( o00OO00OoO )
 for url , i1I1i111Ii , iiI1IIIi in Ii1i :
  II1I ( '[COLORgreen]' + ( i1I1i111Ii ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' ) + '[/COLOR]' , 'http://www.watchseries.li' + url , 10044 , iiI1IIIi , '' , '' )
 for url in I1 :
  II1I ( '[COLORgreen]' + 'NEXT' + '[/COLOR]' , 'http://www.watchseries.li' + url , 10041 , ooOooo000oOO + 'Next.png' , '' , '' )
  if 9 - 9: OOooOOo - Ii1I * O0OoO . O0OoO - oOo0O0Ooo
def OOooOooo0OOo0 ( url ) :
 o00OO00OoO = iiI111I1iIiI ( url )
 ii1I1IIii11 = re . compile ( '<div class="col-md-6 col-xs-12".+?<a href=".+?" itemprop="url"><span itemprop="name">(.+?)</span>(.+?)</ul>' , re . DOTALL ) . findall ( o00OO00OoO )
 for iIi11io0o00o0Oo , I1I111iIi in ii1I1IIii11 :
  Ii1i = re . compile ( '<li itemprop="episode".+?<meta itemprop="url" content="(.+?)">.+?<span class="" itemprop="name">\n(.+?)\n' , re . DOTALL ) . findall ( str ( I1I111iIi ) )
  for url , i1I1i111Ii in Ii1i :
   O0Oooo = ( iIi11io0o00o0Oo ) . replace ( '  ' , '' ) + ' ' + ( i1I1i111Ii ) . replace ( '&nbsp;' , ' ' ) . replace ( '&#039;' , '\'' ) . replace ( '  ' , '' )
   II1I ( '[COLORgreen]' + O0Oooo + '[/COLOR]' , 'http://www.watchseries.li' + url , 10045 , ooOooo000oOO + 'WATCHSERIES.png' , '' , '' )
 I1 = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="(.+?)">Next</a></li></ul>' , re . DOTALL ) . findall ( o00OO00OoO )
 for url in I1 :
  II1I ( '[COLORgreen]' + 'NEXT' + '[/COLOR]' , 'http://www.watchseries.li' + url , 10044 , ooOooo000oOO + 'Next.png' , '' , '' )
  if 87 - 87: OooO0OoOOOO
  if 17 - 17: Ii11Ii1I / iI11I1II1I1I - oO0o + oOo0O0Ooo % IIIii1II1II
class III1III11II ( ) :
 if 43 - 43: oOo0O0Ooo
 List = [ ]
 source_list = [ ]
 def __init__ ( self , name ) :
  if 47 - 47: ii % OOooOOo
  O0Oooo = name
  self . Get_Sources ( iIII , O0Oooo )
  if 63 - 63: oO0o / OOooOOo * iI11I1II1I1I . IIIi
  if 85 - 85: Ii / Ii . oO0o . o0o00Oo0O
 def Get_Sources ( self , URL , season_name ) :
  Oo0oO0ooo = xbmcgui . DialogProgress ( )
  o00OO00OoO = iiI111I1iIiI ( URL )
  Ii1i = re . compile ( '<td>.+?<a href="/link/(.+?)".+?height="16px">(.+?)\n' , re . DOTALL ) . findall ( o00OO00OoO )
  for iIII , i1I1i111Ii in Ii1i :
   URL = 'http://www.watchseries.li/link/' + iIII
   self . Get_site_link ( URL , season_name )
   if 67 - 67: IIiIiII11i / I11i . IIIii1II1II . ii
 def Get_site_link ( self , url , season_name ) :
  o00OO00OoO = iiI111I1iIiI ( url )
  Ii1i = re . compile ( '<iframe style=.+?" src="(.+?)"' ) . findall ( o00OO00OoO )
  I1 = re . compile ( '<IFRAME SRC="(.+?)"' ) . findall ( o00OO00OoO )
  i111i1i = re . compile ( '<IFRAME style=".+?" SRC="(.+?)"' ) . findall ( o00OO00OoO )
  for url in Ii1i :
   self . main ( url , season_name )
  for url in I1 :
   self . main ( url , season_name )
  for url in i111i1i :
   self . main ( url , season_name )
   if 19 - 19: OooO0OoOOOO . Ii1I / OOooOOo
 def main ( self , url , season_name ) :
  Oo0oO0ooo . create ( "[COLORwhite]Origin[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
  if 'daclips.in' in url :
   O00oo = 'DACLIPS'
   if O00oo in III1III11II . source_list :
    pass
   else :
    self . daclips ( url , season_name , O00oo )
    Oo0oO0ooo . update ( 0 , "" , "Getting Daclips Links" )
  else :
   if 'filehoot.com' in url :
    O00oo = 'FILEHOOT'
    if O00oo in III1III11II . source_list :
     pass
    else :
     Oo0oO0ooo . update ( 0 , "" , "Getting Filehoot Links" )
     self . filehoot ( url , season_name , O00oo )
   else :
    if 'thevideo.me' in url :
     O00oo = 'THEVIDEO'
     if O00oo in III1III11II . source_list :
      pass
     else :
      self . thevideo ( url , season_name , O00oo )
      Oo0oO0ooo . update ( 0 , "" , "Getting Thevideo Links" )
    else :
     if 'allmyvideos.net' in url :
      O00oo = 'ALLMYVIDEOS'
      if O00oo in III1III11II . source_list :
       pass
      else :
       self . allmyvid ( url , season_name , O00oo )
       Oo0oO0ooo . update ( 0 , "" , "Getting Allmyvideo Links" )
     else :
      if 'vidspot.net' in url :
       O00oo = 'VIDSPOT'
       if O00oo in III1III11II . source_list :
        pass
       else :
        self . vidspot ( url , season_name , O00oo )
        Oo0oO0ooo . update ( 0 , "" , "Getting Vidspot Links" )
      else :
       if 'vodlocker' in url :
        O00oo = 'VODLOCKER'
        if O00oo in III1III11II . source_list :
         pass
        else :
         self . vodlocker ( url , season_name , O00oo )
         Oo0oO0ooo . update ( 0 , "" , "Getting Vodlocker Links" )
         if 75 - 75: iI11I1II1I1I * Ii - ii . OOooOOo
         if 70 - 70: OoOo00o * OoOo00o + I1ii11iIi11i * IIIii1II1II % oOo0O0Ooo + iI11I1II1I1I
 def allmyvid ( self , url , season_name , source_name ) :
  o00OO00OoO = iiI111I1iIiI ( url )
  Ii1i = re . compile ( '"file" : "(.+?)",\n.+?"default" : .+?,\n.+?"label" : "(.+?)"' , re . DOTALL ) . findall ( o00OO00OoO )
  for i1oOOO0ooOO , i1I1i111Ii in Ii1i :
   self . Printer ( i1oOOO0ooOO , season_name , source_name )
   if 3 - 3: ii
 def vidspot ( self , url , season_name , source_name ) :
  o00OO00OoO = iiI111I1iIiI ( url )
  Ii1i = re . compile ( '"file" : "(.+?)",\n.+?"default" : .+?,\n.+?"label" : "(.+?)"' ) . findall ( o00OO00OoO )
  for i1oOOO0ooOO , i1I1i111Ii in Ii1i :
   self . Printer ( i1oOOO0ooOO , season_name , source_name )
   if 71 - 71: OooO0OoOOOO + ooOoO0O00 - o0oOO0O00o0O - Ii . iI1iI1I1i1I - O0OoO
 def thevideo ( self , url , season_name , source_name ) :
  o00OO00OoO = iiI111I1iIiI ( url )
  Ii1i = re . compile ( "{ label: '.+?', file: '(.+?)' }" ) . findall ( o00OO00OoO )
  for i1oOOO0ooOO in Ii1i :
   self . Printer ( i1oOOO0ooOO , season_name , source_name )
   if 85 - 85: Ii1I - OOooOOo / Ii1I + IIIii1II1II - o0oOO0O00o0O
 def vodlocker ( self , url , season_name , source_name ) :
  o00OO00OoO = iiI111I1iIiI ( url )
  Ii1i = re . compile ( 'file: "(.+?)",.+?skin' , re . DOTALL ) . findall ( o00OO00OoO )
  for i1oOOO0ooOO in Ii1i :
   self . Printer ( i1oOOO0ooOO , season_name , source_name )
   if 49 - 49: oO0o - o0o00Oo0O / oO0o * OOooOOo + IIIi
 def daclips ( self , url , season_name , source_name ) :
  o00OO00OoO = iiI111I1iIiI ( url )
  Ii1i = re . compile ( '{ file: "(.+?)", type:"video" }' ) . findall ( o00OO00OoO )
  for i1oOOO0ooOO in Ii1i :
   self . Printer ( i1oOOO0ooOO , season_name , source_name )
   if 35 - 35: IIiIiII11i . oOo0O0Ooo / ooOoO0O00 / oOo0O0Ooo * OoOo00o
 def filehoot ( self , url , season_name , source_name ) :
  o00OO00OoO = iiI111I1iIiI ( url )
  Ii1i = re . compile ( 'file: "(.+?)",.+?skin' , re . DOTALL ) . findall ( o00OO00OoO )
  for i1oOOO0ooOO in Ii1i :
   self . Printer ( i1oOOO0ooOO , season_name , source_name )
   if 85 - 85: IIiIiII11i . O0OoO % IIIii1II1II % iI1iI1I1i1I
 def Printer ( self , Link , season_name , source_name ) :
  if 80 - 80: OoOo00o * iI1iI1I1i1I / iI11I1II1I1I % OoOo00o / iI11I1II1I1I
  if Link in III1III11II . List :
   pass
  elif source_name in III1III11II . source_list :
   pass
  else :
   OO0ooOOO00 ( '[COLORgreen]' + source_name + '[/COLOR]' , Link , 10012 , ooOooo000oOO + 'WATCHSERIES.png' )
   Oo0oO0ooo . update ( 100 , "" , "Got Source" )
   III1III11II . List . append ( Link )
   III1III11II . source_list . append ( source_name )
   if 42 - 42: ooOoO0O00 / Ii . I1ii11iIi11i * o0oOO0O00o0O . Ii * o0o00Oo0O
   xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
   if 44 - 44: ooOoO0O00 . oOo0O0Ooo / Ii + OooO0OoOOOO
   if 27 - 27: IIIii1II1II
   if 52 - 52: IIIi % OOooOOo + iI11I1II1I1I * OoOo00o . Ii11Ii1I
   if 95 - 95: iI11I1II1I1I . OooO0OoOOOO - ii * oO0o / I11i
   if 74 - 74: OoOo00o
def iII1i1IIiI1I ( ) :
 II1I ( '[COLORgreen]Highlights[/COLOR]' , '' , 10008 , ooOooo000oOO + 'ORIGINFOOTBALL.png' , i1iiIII111ii , '' )
 II1I ( '[COLORgreen]Fixtures[/COLOR]' , '' , 10009 , ooOooo000oOO + 'ORIGINFOOTBALL.png' , i1iiIII111ii , '' )
 if 67 - 67: Ii11Ii1I
def iIII11Iiii1 ( ) :
 IIiI1Ii = iiI111I1iIiI ( i1111 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20vcXVpY2tpbmRleC5odG1s' ) )
 Ii1i = re . compile ( '<a target="_self" href="(.+?)".+?src="(.+?)" alt="(.+?)"' , re . DOTALL ) . findall ( IIiI1Ii )
 for iIII , iiI1IIIi , i1I1i111Ii in Ii1i :
  II1I ( '[COLORgreen]' + ( i1I1i111Ii ) . replace ( 'amp;' , '' ) + '[/COLOR]' , i1111 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20v' ) + iIII , 10010 , i1111 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20v' ) + iiI1IIIi , i1iiIII111ii , '' )
  if 95 - 95: oOo0O0Ooo
def o0OoO0OOoO0Oo0 ( url ) :
 o00OO00OoO = iiI111I1iIiI ( url )
 ii1I1IIii11 = re . compile ( 'AndClearL.+?><h2.+?head>(.*?)float' , re . DOTALL ) . findall ( o00OO00OoO )
 for ii1I1IIii11 in ii1I1IIii11 :
  oO00O = re . compile ( '(.*?)</h2>' ) . findall ( str ( ii1I1IIii11 ) )
  for II111IiiiI1 in oO00O :
   II111IiiiI1 = II111IiiiI1
  oooOO0oo0Oo00 = re . compile ( 'comp_head>(.*?)</span>.*?<div class = fLeft width = ".*?"><img src="(.*?)">.*?</div>.*?ST:(.*?)</div>(.+?)<!-- around all of channel types ENDS 2-->' , re . DOTALL ) . findall ( str ( ii1I1IIii11 ) )
  for oOoO , iiI1IIIi , time , iI111I1III in oooOO0oo0Oo00 :
   ooooO0oOoOOoO = re . compile ( ",CAPTION, '(.+?)&nbsp" ) . findall ( iI111I1III )
   II1I ( '[COLORgreen]' + II111IiiiI1 + ' - ' + oOoO + ' - ' + time + '[/COLOR]' , '' , 10010 , i1111 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20=' ) + iiI1IIIi , i1iiIII111ii , ( str ( ooooO0oOoOOoO ) ) )
   if 36 - 36: iI1iI1I1i1I % IIIii1II1II
 iiO0o0oOOOoOo ( 'tvshows' , 'Media Info 3' )
 if 72 - 72: oOo0O0Ooo / o0oOO0O00o0O - o0o00Oo0O + iI1iI1I1i1I
def o0iIIIIi ( ) :
 if 50 - 50: IIIi + O0OoO + o0oOO0O00o0O
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
 if 15 - 15: iI1iI1I1i1I
def IiiI11I1IIiI ( url ) :
 o00OO00OoO = iiI111I1iIiI ( url )
 Ii1i = re . compile ( 'itemprop="image" class="entry-thumb" src="(.+?)".+?<h3 itemprop="name" class="entry-title td-module-title"><a itemprop="url" href="(.+?)" rel="bookmark" title=".+?">(.+?)</a></h3>' , re . DOTALL ) . findall ( o00OO00OoO )
 for iiI1IIIi , url , i1I1i111Ii in Ii1i :
  i1iI1i = i1I1i111Ii . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' )
  OO0ooOOO00 ( '[COLORgreen]' + i1iI1i + '[/COLOR]' , url , 10013 , iiI1IIIi )
  if 59 - 59: OooO0OoOOOO
def oOoO0OOO00O ( url ) :
 o00OO00OoO = iiI111I1iIiI ( url )
 Ii1i = re . compile ( '<script data-config="(.+?)" data-height' ) . findall ( o00OO00OoO )
 for iI1iiiiIii in Ii1i :
  OOOOO0o0OOo = ( iI1iiiiIii ) . replace ( '/v2' , '' ) . replace ( 'zeus.json' , 'video-sd.mp4?hosting_id=21772' ) . replace ( 'config.playwire.com' , 'cdn.video.playwire.com' )
  oo0000o ( 'http:' + OOOOO0o0OOo )
  if 40 - 40: OooO0OoOOOO * OoOo00o % iI1iI1I1i1I * Ii1I
  if 80 - 80: iI11I1II1I1I - ii - Ii1I - Ii1I . ii
def I1i ( url ) :
 IIiI1Ii = O0O0O0Oo ( url )
 Ii1i = re . compile ( '<a href="([^"]*)" title="([^"]*)"><img itemprop="image" content="([^"]*)"' , re . DOTALL ) . findall ( IIiI1Ii )
 I1 = re . compile ( "<a rel='next' href=([^=]*)=" , re . DOTALL ) . findall ( IIiI1Ii )
 for url , i1I1i111Ii , iiI1IIIi in Ii1i :
  OO0ooOOO00 ( i1I1i111Ii , url , 8046 , iiI1IIIi )
 for url in I1 :
  IiIiiI11111I1 ( 'NEXT PAGE' , ( url ) . replace ( ' class' , '' ) , 8045 , ooOooo000oOO + 'Next.png' )
def I11I ( url ) :
 IIiI1Ii = O0O0O0Oo ( url )
 Ii1i = re . compile ( "__filename='([^']*)',.+?__fullimage='([^']*)',.+?__title='([^']*)'," , re . DOTALL ) . findall ( IIiI1Ii )
 for url , iiI1IIIi , i1I1i111Ii in Ii1i :
  oo0000o ( 'http://bitcast-b.bitgravity.com/ndtvod/23372/ndtv/' + url )
  if 81 - 81: Ii + Ii * oO0o + OooO0OoOOOO
def iiiiiI ( url ) :
 IIiI1Ii = O0O0O0Oo ( url )
 Ii1i = re . compile ( "src='http://www.youtube.com/embed/(.+?)?version=3&#038;rel=1&#038;fs=1&#038;autohide=2&#038;showsearch=0&#038;showinfo=1&#038;iv_load_policy=1&#038;wmode=transparent' frameborder='0' allowfullscreen='true'></iframe>" ) . findall ( IIiI1Ii )
 for url in Ii1i :
  yt . PlayVideo ( url )
  if 17 - 17: Ii / I1ii11iIi11i . oO0o / oOo0O0Ooo
def Ii1 ( ) :
 IIiI1Ii = O0O0O0Oo ( i1111 ( 'aHR0cDovL3RvcGRvY3VtZW50YXJ5ZmlsbXMuY29tLw==' ) )
 Ii1i = re . compile ( '<a href="(.+?)" >(.+?)</a></li><li>' ) . findall ( IIiI1Ii )
 for iIII , i1I1i111Ii in Ii1i :
  IiIiiI11111I1 ( i1I1i111Ii , iIII , 8041 , ooOooo000oOO + 'documentary.png' )
def oOooOOOOo0o ( url ) :
 IIiI1Ii = O0O0O0Oo ( url )
 Ii1i = re . compile ( '<h2><a href="(.+?)" title="(.+?)">.+?</a></h2>.+?src="(.+?)"' , re . DOTALL ) . findall ( IIiI1Ii )
 I1 = re . compile ( 'class="inactive">.+?</a><a href="(.+?)">Next</a></div>' , re . DOTALL ) . findall ( IIiI1Ii )
 for url , i1I1i111Ii , iiI1IIIi in Ii1i :
  IiIiiI11111I1 ( ( i1I1i111Ii ) . replace ( '&#039;s' , '' ) , url , 8042 , iiI1IIIi )
 for url in I1 :
  IiIiiI11111I1 ( 'NEXT PAGE' , url , 8041 , ooOooo000oOO + 'Next.png' )
  if 97 - 97: Ii1I / oOo0O0Ooo % o0o00Oo0O + ooOoO0O00 - O0OoO
  if 38 - 38: I11i % IIIi + Ii + o0oOO0O00o0O + O0OoO / Ii
def o0OOOOOo0 ( url ) :
 IIiI1Ii = O0O0O0Oo ( url )
 Ii1i = re . compile ( '<meta itemprop="name" content="(.+?)".+?<meta itemprop="thumbnailUrl" content="(.+?)".+?<meta itemprop="embedUrl" content="(.+?)".+?<meta itemprop="description" content="(.+?)" />' , re . DOTALL ) . findall ( IIiI1Ii )
 I1 = re . compile ( '<div class="video new-video"><iframe width="766" height="431" src="(.+?)&iv_load_policy=3&showinfo=0&autohide=1"' , re . DOTALL ) . findall ( IIiI1Ii )
 for i1I1i111Ii , iiI1IIIi , url , Ii1IIiiIiiIi in Ii1i :
  OO0ooOOO00 ( ( i1I1i111Ii ) . replace ( '&#039;s' , '' ) , url . replace ( 'https://www.youtube.com/embed/' , '' ) , 8043 , iiI1IIIi )
 for url in I1 :
  oooOoO ( ( url ) . replace ( '//' , 'http://' ) )
  if 62 - 62: IIIii1II1II / IIiIiII11i + OOooOOo % O0OoO / OOooOOo + Ii1I
def oooOoO ( url ) :
 IIiI1Ii = O0O0O0Oo ( url )
 Ii1i = re . compile ( '<link rel="canonical" href="(.+?)">  <link rel="stylesheet"' ) . findall ( IIiI1Ii )
 for url in Ii1i :
  OO0ooOOO00 ( 'PLAY' , ( url ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , ooOooo000oOO + 'documentary.png' )
  if 2 - 2: Ii - IIIi + oO0o % iI1iI1I1i1I * Ii11Ii1I
def Ooo000O00 ( ) :
 o00OO00OoO = O0O0O0Oo ( 'http://www.stream2watch.co/live-tv' )
 Ii1i = re . compile ( '<a href="(.+?)">.+?<img src="(.+?)" alt=".+?"/>.+?<span class="country_name">(.+?)<br />(.+?)</span>' , re . DOTALL ) . findall ( o00OO00OoO )
 for iIII , iiI1IIIi , i1I1i111Ii , i1iI1Iiii1I in Ii1i :
  IiIiiI11111I1 ( ( i1I1i111Ii + '[COLORgreen]' + i1iI1Iiii1I + '[/COLOR]' ) , iIII , 8086 , iiI1IIIi )
  if 9 - 9: iI1iI1I1i1I / OOooOOo / IIiIiII11i + IIIi
def o0O0 ( url ) :
 o00OO00OoO = O0O0O0Oo ( url )
 Ii1i = re . compile ( '<a class="front_channel_href" href="(.+?)" title=".+?">.+?<img class="front_channel_thumb" src="(.+?)" alt=".+?"/>.+?<span class="front_channel_name">(.+?)</span>' , re . DOTALL ) . findall ( o00OO00OoO )
 for url , iiI1IIIi , i1I1i111Ii in Ii1i :
  IiIiiI11111I1 ( '[COLORgreen]' + i1I1i111Ii + '[/COLOR]' , url , 8087 , iiI1IIIi )
  if 57 - 57: IIIii1II1II - IIIii1II1II - Ii1I
def iio0o000Oo ( url ) :
 o00OO00OoO = iiI111I1iIiI ( url )
 Ii1i = re . compile ( 'a id="code_.+?data-f-href="(.+?)" data-code-embed="">(.+?)</a>' , re . DOTALL ) . findall ( o00OO00OoO )
 for url , i1I1i111Ii in Ii1i :
  oO0o0O0o0OO00 ( url , i1I1i111Ii )
  if 23 - 23: oO0o + Ii
def oO0o0O0o0OO00 ( url , name ) :
 o00OO00OoO = iiI111I1iIiI ( url )
 Ii1i = re . compile ( "playStream\('.+?', '(.+?)'\);" , re . DOTALL ) . findall ( o00OO00OoO )
 for url in Ii1i :
  print url
  OO0ooOOO00 ( '[COLORgreen]' + name + '[/COLOR]' , url , 222 , '' )
  if 20 - 20: Ii1I
def IIiiiiIiI1III ( ) :
 IIiI1Ii = O0O0O0Oo ( i1111 ( 'aHR0cDovL3d3dy5zb2xpZS5vcmcvYWxpYnJhcnkvaW5kZXguaHRtbA==' ) )
 Ii1i = re . compile ( '<td align="center" valign="top">.+?<a href="(.+?)">.+?<img src="(.+?)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( IIiI1Ii )
 for iIII , iiI1IIIi , i1I1i111Ii in Ii1i :
  IiIiiI11111I1 ( ( '[COLORgreen]' + i1I1i111Ii + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + iIII , 3002 , 'http://www.solie.org/alibrary/' + iiI1IIIi )
def iIiI ( url ) :
 IIiI1Ii = O0O0O0Oo ( url )
 Ii1i = re . compile ( '<td align="center" valign="top">.+?<a href="(.+?)">.+?<img src="(.+?)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( IIiI1Ii )
 for url , iiI1IIIi , i1I1i111Ii in Ii1i :
  IiIiiI11111I1 ( ( '[COLORgreen]' + i1I1i111Ii + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3003 , 'http://www.solie.org/alibrary/' + iiI1IIIi )
def OO0OOoooo0o ( url ) :
 IIiI1Ii = O0O0O0Oo ( url )
 Ii1i = re . compile ( '<br><a href="([^"]*)">(.+?)</a>' ) . findall ( IIiI1Ii )
 IiIi1Ii = re . compile ( 'href="([^"]*)">Season(.+?)</a>' ) . findall ( IIiI1Ii )
 next = re . compile ( '<a href="([^"]*)">Episodes</a>' ) . findall ( IIiI1Ii )
 I1 = re . compile ( '<td align="center" valign="top">.+?<a href="(.+?)">.+?<img src="(.+?)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( IIiI1Ii )
 for url , i1I1i111Ii in Ii1i :
  OO0ooOOO00 ( ( '[COLORgreen]' + i1I1i111Ii + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3004 , ooOooo000oOO + 'classicmovies.png' )
 for url , i1I1i111Ii in IiIi1Ii :
  IiIiiI11111I1 ( '[COLORgreen]Season- ' + i1I1i111Ii + '[/COLOR]' , 'http://www.solie.org/alibrary/' + url , 3003 , ooOooo000oOO + 'classicmovies.png' )
 for url in next :
  IiIiiI11111I1 ( '[COLORgreen]NEXT[/COLOR]' , 'http://www.solie.org/alibrary/' + url , 3003 , ooOooo000oOO + 'Next.png' )
 for url , iiI1IIIi , i1I1i111Ii in I1 :
  IiIiiI11111I1 ( ( '[COLORgreen]' + i1I1i111Ii + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3003 , 'http://www.solie.org/alibrary/' + iiI1IIIi )
def iiIIiI11II1 ( url ) :
 IIiI1Ii = O0O0O0Oo ( url )
 Ii1i = re . compile ( '<iframe.+?src="([^"]*)"' ) . findall ( IIiI1Ii )
 for url in Ii1i :
  oooOo ( url )
def oooOo ( url ) :
 IIiI1Ii = O0O0O0Oo ( url )
 Ii1i = re . compile ( '<meta property="og:video" content="([^"]*)"/>' ) . findall ( IIiI1Ii )
 for url in Ii1i :
  oo0000o ( url )
  if 79 - 79: OoOo00o - IIiIiII11i
def Ii1iiI1 ( ) :
 IIiI1Ii = O0O0O0Oo ( i1111 ( 'aHR0cDovL3JldHJvdmlzaW9uLnR2L2FsbC8=' ) )
 Ii1i = re . compile ( '<a href="([^"]*)"><h2><font color=".+?"><h2>(.+?)</font></h2></a>' ) . findall ( IIiI1Ii )
 for iIII , i1I1i111Ii in Ii1i :
  OO0ooOOO00 ( ( '[COLORgreen]' + i1I1i111Ii + '[/COLOR]' ) . replace ( '&#8211;' , ':' ) , iIII , 8061 , ooOooo000oOO + 'classicmovies.png' )
def o0ooOOoO0oO0 ( url ) :
 IIiI1Ii = O0O0O0Oo ( url )
 Ii1i = re . compile ( "v.src = '([^']*)';" ) . findall ( IIiI1Ii )
 for url in Ii1i :
  oo0000o ( url )
  if 86 - 86: ooOoO0O00 / Ii11Ii1I * oOo0O0Ooo
def OOoO0OOoO0ooo ( ) :
 IIiI1Ii = O0O0O0Oo ( i1111 ( 'aHR0cDovL3JldHJvdmlzaW9uLnR2L2NsYXNzaWMtdHYv' ) )
 Ii1i = re . compile ( '<a href="([^"]*)"><h2><font color=".+?"><h2>(.+?)</font></h2></a>' ) . findall ( IIiI1Ii )
 for iIII , i1I1i111Ii in Ii1i :
  OO0ooOOO00 ( ( '[COLORgreen]' + i1I1i111Ii + '[/COLOR]' ) . replace ( '&#8211;' , ':' ) , iIII , 8061 , ooOooo000oOO + 'classictv.png' )
def ii11i1ii1 ( url ) :
 IIiI1Ii = O0O0O0Oo ( url )
 Ii1i = re . compile ( "v.src = '([^']*)';" ) . findall ( IIiI1Ii )
 for url in Ii1i :
  oo0000o ( url )
  if 37 - 37: Ii
def iI1i ( ) :
 o00OO00OoO = iiI111I1iIiI ( i1111 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vbTN1c3RyZWFtcw==' ) )
 Ii1i = re . compile ( '<li><a href="(.+?)"> (.+?).m3u</a></li>' ) . findall ( o00OO00OoO )
 for iIII , i1I1i111Ii in Ii1i :
  IiIiiI11111I1 ( ( '[COLORgreen]' + i1I1i111Ii + '[/COLOR]' ) . replace ( '-' , ' ' ) . replace ( '_' , ' ' ) , ( i1111 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vbTN1c3RyZWFtcy8=' ) ) + iIII , 8071 , ooOooo000oOO + 'streams.png' )
def i11I ( url ) :
 o00OO00OoO = O0O0O0Oo ( url )
 Ii1i = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( o00OO00OoO )
 for i1I1i111Ii , url in Ii1i :
  OO0ooOOO00 ( ( '[COLORgreen]' + i1I1i111Ii + '[/COLOR]' ) . replace ( '_' , ' ' ) , ( url ) . strip ( ) , 404 , ooOooo000oOO + 'streams.png' )
def o0oO0o0oo0O0 ( url ) :
 o00OO00OoO = O0O0O0Oo ( url )
 Ii1i = re . compile ( 'EXTINF:(.+?),(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( o00OO00OoO )
 for iiI1IIIi , i1I1i111Ii , url in Ii1i :
  url = ( ( i1111 ( 'aHR0cDovL3BpZXN1c3R2Lm5ldDo4MDAwL2xpdmUv' ) ) + oO0o0o0ooO0oO + '/' + oo0o0O00 + url ) . strip ( )
  OO0ooOOO00 ( ( '[COLORgreen]' + i1I1i111Ii + '[/COLOR]' ) . replace ( '_' , ' ' ) , url , 10012 , iiI1IIIi )
  if 98 - 98: OooO0OoOOOO * iI11I1II1I1I . Ii11Ii1I * I1ii11iIi11i / Ii1I + O0OoO
def iiI1ii111 ( ) :
 iiiiI11ii ( 'Best Videos' , 'http://www.xvideos.com/best' , 10105 , ooOooo000oOO + 'JIZBOX.png' , '' , '' )
 iiiiI11ii ( 'Genres' , 'http://www.xvideos.com' , 10106 , ooOooo000oOO + 'JIZBOX.png' , '' , '' )
 iiiiI11ii ( 'Recently Uploaded' , 'http://xvideos.com' , 10105 , ooOooo000oOO + 'JIZBOX.png' , '' , '' )
 iiiiI11ii ( 'Tags' , 'http://www.xvideos.com/tags' , 10103 , ooOooo000oOO + 'JIZBOX.png' , '' , '' )
 iiiiI11ii ( 'Search' , '' , 10107 , ooOooo000oOO + 'JIZBOX.png' , '' , '' , )
 if 97 - 97: o0o00Oo0O / IIIii1II1II + I11i . OoOo00o % OOooOOo - OOooOOo
def i1IiI1Iiii ( url ) :
 o00OO00OoO = iiI111I1iIiI ( url )
 o0O0O = re . compile ( '<li><a class=".+?".+?href="(.+?)">Next</a></li>' ) . findall ( o00OO00OoO )
 for url in o0O0O :
  iiiiI11ii ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10103 , ooOooo000oOO + 'JIZBOX.png' , '' , '' )
 Ii1i = re . compile ( '<li><a href="(.+?)"><b>(.+?)</b><span class="navbadge default"(.+?)</span>' ) . findall ( o00OO00OoO )
 for url , i1I1i111Ii , ooo in Ii1i :
  iiiiI11ii ( i1I1i111Ii + ' - No of Videos : ' + ( ooo ) . replace ( '>' , '' ) , 'http://www.xvideos.com' + url , 10105 , ooOooo000oOO + 'JIZBOX.png' , '' , '' )
  if 56 - 56: o0o00Oo0O
def iIIIII1iI ( url ) :
 o00OO00OoO = iiI111I1iIiI ( url )
 o0O0O = re . compile ( 'href="([^"]*)">Next</a></li>' ) . findall ( o00OO00OoO )
 for url in o0O0O :
  iiiiI11ii ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10104 , ooOooo000oOO + 'Next.png' , '' , '' )
 Ii1i = re . compile ( ':"([^"]*)".+?;</script></a></div></div><p class="profile-name"><a href="([^"]*)">(.+?)</a></p><p class="profile-counts">\n(.+?)\n' , re . DOTALL ) . findall ( o00OO00OoO )
 for iiI1IIIi , url , i1I1i111Ii , iIi1II11i in Ii1i :
  iiiiI11ii ( i1I1i111Ii + '--' + iIi1II11i , 'http://www.xvideos.com' + url + '#_tabVideos,videos-best' , 10105 , ( iiI1IIIi ) . replace ( 'http:\/\/' , 'http://' ) , '' , '' )
  if 8 - 8: ooOoO0O00
  if 20 - 20: o0oOO0O00o0O / IIIii1II1II
def I1111ii11IIII ( url ) :
 o00OO00OoO = iiI111I1iIiI ( url )
 Ii1i = re . compile ( '<div class="thumb-inside"><script>.+?<img src="(.+?)".+?<a href="(.+?)" title=".+?">(.+?)</a></p>.+?uration">(.+?)</span>.+?Porn quality:(.+?)</span>' , re . DOTALL ) . findall ( o00OO00OoO )
 for iiI1IIIi , url , i1I1i111Ii , o0o0O , IiIi1II111I in Ii1i :
  ooOOoooooo ( i1I1i111Ii + ' - Porn Quality : ' + IiIi1II111I + ' - ' + o0o0O , 'http://www.xvideos.com' + url , 10108 , iiI1IIIi , iiI1IIIi , IiIi1II111I + ' - ' + o0o0O )
 o00o = re . compile ( '<li><a href="([^"]*)" class="no-page">Next</a></li></ul></div>' ) . findall ( o00OO00OoO )
 for url in o00o :
  iiiiI11ii ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10105 , ooOooo000oOO + 'Next.png' , '' , '' )
  if 45 - 45: Ii1I + IIIi . o0oOO0O00o0O . o0oOO0O00o0O
def iI1Iii11i1 ( url ) :
 o00OO00OoO = iiI111I1iIiI ( url )
 ii1I1IIii11 = re . compile ( '<div class="main-categories">(.+?)</div>' , re . DOTALL ) . findall ( o00OO00OoO )
 o0O0O = re . compile ( '<li><a class=".+?".+?href="(.+?)">Next</a></li>' ) . findall ( o00OO00OoO )
 for url in o0O0O :
  iiiiI11ii ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10106 , ooOooo000oOO + 'Next.png' , '' , '' )
 Ii1i = re . compile ( '<li><a href="(.+?)" class="btn btn-default">(.+?)</a>' ) . findall ( str ( ii1I1IIii11 ) )
 for url , i1I1i111Ii in Ii1i :
  iiiiI11ii ( i1I1i111Ii , 'http://www.xvideos.com' + url , 10105 , ooOooo000oOO + 'JIZBOX.png' , '' , '' )
  if 34 - 34: OoOo00o - O0OoO * I1ii11iIi11i / I11i
  if 19 - 19: Ii1I
def IiI ( ) :
 Ooo0OOoOoO0 = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 Iii1iiI = ( Ooo0OOoOoO0 ) . replace ( ' ' , '+' ) . replace ( '&' , '&' )
 IIo0Oo0oO0oOO00 = Iii1iiI . lower ( )
 ii1IiiII = 'http://www.xvideos.com/?k=' + IIo0Oo0oO0oOO00
 print ii1IiiII + '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'
 o00OO00OoO = iiI111I1iIiI ( ii1IiiII )
 Ii1i = re . compile ( '<div class="thumb-inside"><script>.+?<img src="(.+?)".+?<a href="(.+?)" title=".+?">(.+?)</a></p>.+?uration">(.+?)</span>.+?Porn quality:(.+?)</span>' , re . DOTALL ) . findall ( o00OO00OoO )
 for iiI1IIIi , iIII , i1I1i111Ii , o0o0O , IiIi1II111I in Ii1i :
  ooOOoooooo ( i1I1i111Ii + ' - Porn Quality : ' + IiIi1II111I + ' - ' + o0o0O , 'http://www.xvideos.com' + iIII , 10108 , iiI1IIIi , iiI1IIIi , IiIi1II111I + ' - ' + o0o0O )
 o00o = re . compile ( '<li><a href="([^"]*)" class="no-page">Next</a></li></ul></div>' ) . findall ( o00OO00OoO )
 for iIII in o00o :
  iiiiI11ii ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + iIII , 10105 , ooOooo000oOO + 'Next.png' , '' , '' )
  if 7 - 7: iI11I1II1I1I * oO0o / OOooOOo % IIIi - I11i - IIIii1II1II
def iiI ( url ) :
 o00OO00OoO = iiI111I1iIiI ( url )
 Ii1i = re . compile ( 'flv_url=(.+?)\;' ) . findall ( o00OO00OoO )
 for url in Ii1i :
  O0OO0o0O00oO = ( url ) . replace ( '%3A' , ':' ) . replace ( '%2F' , '/' ) . replace ( '%3F' , '?' ) . replace ( '%3D' , '=' ) . replace ( '%26' , '&' ) . replace ( '&amp' , '' )
  o00O ( O0OO0o0O00oO )
  if 92 - 92: I1ii11iIi11i - IIIi
def o00O ( url ) :
 I1III11iiii11i1 = xbmc . Player ( IIi11 ( ) )
 import urlresolver
 try : I1III11iiii11i1 . play ( url )
 except : pass
 if 73 - 73: O0OoO + Ii1I
 if 100 - 100: iI11I1II1I1I
def ooOOo00 ( ) :
 o00OO00OoO = iiI111I1iIiI ( i1111 ( 'aHR0cDovL3d3dy5nb2Zpc2hpbmcuY28udWsvQW5nbGluZy1UaW1lcy9TZWN0aW9uL1ZpZGVvcy8=' ) )
 Ii1i = re . compile ( 'class="item.+?"><a href="(.+?)">(.+?)</a></li>' ) . findall ( o00OO00OoO )
 for iIII , i1I1i111Ii in Ii1i :
  IiIiiI11111I1 ( '[COLORgreen]' + i1I1i111Ii + '[/COLOR]' , ( 'http://www.gofishing.co.uk' + iIII ) . replace ( 'http://www.gofishing.co.ukhttp://www.gofishing.co.uk' , 'http://www.gofishing.co.uk' ) , 8091 , ooOooo000oOO + 'gofish.png' )
def IIii1i1IiIi1 ( url ) :
 o00OO00OoO = O0O0O0Oo ( url )
 Ii1i = re . compile ( '<h2><a id=.+?href="([^"]*)">(.+?)</a></h2>' , re . DOTALL ) . findall ( o00OO00OoO )
 I1 = re . compile ( '<h3><a href="([^"]*)" id=.+?>(.+?)</a> </h3>.+?<img src="([^"]*)"' , re . DOTALL ) . findall ( o00OO00OoO )
 next = re . compile ( 'href="([^"]*)">next</a>&gt;</li>' , re . DOTALL ) . findall ( o00OO00OoO )
 for url , i1I1i111Ii in Ii1i :
  OO0ooOOO00 ( '[COLORgreen]' + i1I1i111Ii + '[/COLOR]' , 'http://www.gofishing.co.uk/' + url , 8092 , ooOooo000oOO + 'gofish.png' )
 for url , i1I1i111Ii , iiI1IIIi in I1 :
  OO0ooOOO00 ( '[COLORgreen]' + i1I1i111Ii + '[/COLOR]' , 'http://www.gofishing.co.uk/' + url , 8092 , 'http://www.gofishing.co.uk/' + iiI1IIIi )
 for url in next :
  IiIiiI11111I1 ( '[COLORgreen]NEXT[/COLOR]' , url . replace ( ' ' , '+' ) , 8091 , ooOooo000oOO + 'Next.png' )
def IiiiiIIi11iI ( url ) :
 o00OO00OoO = O0O0O0Oo ( url )
 Ii1i = re . compile ( 'src="https://www.youtube.com/embed/(.+?)"' ) . findall ( o00OO00OoO )
 for url in Ii1i :
  yt . PlayVideo ( url )
  if 22 - 22: IIIii1II1II
  if 22 - 22: o0oOO0O00o0O * iI1iI1I1i1I - I1ii11iIi11i * o0o00Oo0O / Ii
  if 78 - 78: I1ii11iIi11i * o0o00Oo0O / O0OoO + ii + IIIii1II1II
I1iiIiiIiiI = '{PQ},' ; oOoOii1IIii = '{SC},' ; IiI11i1I11111 = '{XG},' ; Ii1IIIIIIiI1 = '{JP},' ; Ii11IiIiiii1 = '{HW},' ; OooO0O0Ooo = '{RT},'
def oO0OIIIiIi1iiI ( ) :
 Oo0oO0ooo = xbmcgui . DialogProgress ( )
 iI1 = ( i1111 ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 Ooo0OOoOoO0 = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 IIo0Oo0oO0oOO00 = Ooo0OOoOoO0 . lower ( )
 iIII = ( i1111 ( 'aHR0cDovL2RsNC5tb3ZpZWZhcnNpLmNvbS9maWxtLzIwMTUtNy8=' ) )
 IiI1iiiIii = ( i1111 ( 'aHR0cDovL2RsLmF2YWRsLmNvbS9OZXcvTW92aWUv' ) )
 I1i111I = ( i1111 ( 'aHR0cDovLzIxNy4yMTkuMTQzLjEwOC8xMzI3Lw==' ) )
 if 94 - 94: iI1iI1I1i1I . oOo0O0Ooo
 oooOoo0OoOO0000 = ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvbW92L2FsbC5waHA=' ) )
 i11Ii1iIIIIi = ( i1111 ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 iiiO000OOO = ( i1111 ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL3NlYXJjaC8/cT0=' ) ) + Ooo0OOoOoO0
 o0IIi1 = ( i1111 ( 'aHR0cDovL3JlZGVtcHRpb25idWlsZC4xNm1iLmNvbS9SZWRlbXB0aW9uL21vdmllcy9hbGxtb3ZpZS5waHA=' ) )
 O00O00o = ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9UaGVfUmVhcGVyL2FsbG1vdmllcy5waHA=' ) )
 I11IiI1iI = ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC9tb3ZmdWxsLnBocA==' ) )
 O0OO0OoO = ( i1111 ( 'aHR0cDovLzUuMTM1LjIwNy45Ni9TY3JhcGVzL1NILnBocA==' ) )
 if 83 - 83: O0OoO / IIIii1II1II
 Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Checking Sources" , '' , 'Please Wait' )
 o00OO00OoO = O000OO0 ( iIII )
 Oo0oO0ooo . update ( 0 , "" , "Checking Source 1/9 Links" )
 if 39 - 39: OooO0OoOOOO + iI1iI1I1i1I
 Oo0oO0ooo . update ( 14 , "" , "Checking Source 2/9 Links" )
 O0Oo000ooO00 = O000OO0 ( I1i111I )
 Oo0oO0ooo . update ( 28 , "" , "Checking Source 3/9 Links" )
 if 9 - 9: oOo0O0Ooo % iI1iI1I1i1I . I1ii11iIi11i * oOo0O0Ooo
 Oo0oO0ooo . update ( 40 , "" , "Checking Source 4/9 Links" )
 OoO0oO0oo0O = O000OO0 ( oooOoo0OoOO0000 )
 Oo0oO0ooo . update ( 52 , "" , "Checking Source 5/9 Links" )
 oooOOO0ooOoOOO = O000OO0 ( iiiO000OOO )
 Oo0oO0ooo . update ( 64 , "" , "Checking Source 6/9 Links" )
 o0IiIiI111IIII1 = O000OO0 ( o0IIi1 )
 Oo0oO0ooo . update ( 76 , "" , "Checking Source 7/9 Links" )
 OOOoOooO000oO = O000OO0 ( O00O00o )
 Oo0oO0ooo . update ( 88 , "" , "Checking Source 8/9 Links" )
 o0OOOOOo00 = O000OO0 ( I11IiI1iI )
 Oo0oO0ooo . update ( 100 , "" , "Checking Source 9/9 Links" )
 oo0oOO = O000OO0 ( O0OO0OoO )
 if 41 - 41: oO0o . IIIi * OooO0OoOOOO * IIIi
 if 74 - 74: iI11I1II1I1I / I11i
 if o00OO00OoO != 'Failed' :
  Ii1i = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( o00OO00OoO )
  for Oo0o0O0o , i1I1i111Ii in Ii1i :
   if Ooo0OOoOoO0 . lower in i1I1i111Ii . lower ( ) :
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    OO0ooOOO00 ( ( '[COLORgreen]' + i1I1i111Ii + '- source 1[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( iIII + Oo0o0O0o ) , 222 , '' )
    Oo0oO0ooo . update ( 0 , "" , "Getting Source 1 Links" )
    if 45 - 45: IIIii1II1II
    if 25 - 25: IIIii1II1II % o0o00Oo0O
    if 44 - 44: IIIi . Ii11Ii1I * IIiIiII11i / OooO0OoOOOO + iI11I1II1I1I
    if 14 - 14: o0o00Oo0O % OooO0OoOOOO % Ii11Ii1I * OoOo00o
    if 65 - 65: iI1iI1I1i1I % OoOo00o + Ii1I
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 9 , "" , "Getting Source 2 Links" )
 if O0Oo000ooO00 != 'Failed' :
  i111i1i = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( O0Oo000ooO00 )
  for Oo0o0O0o , i1I1i111Ii in i111i1i :
   if Ooo0OOoOoO0 . lower in i1I1i111Ii . lower ( ) :
    IiIiiI11111I1 ( ( '[COLORgreen]' + i1I1i111Ii + '- source 3[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( I1i111I + Oo0o0O0o ) , 1006 , '' )
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 18 , "" , "Getting Source 3 Links" )
    if 86 - 86: iI11I1II1I1I / o0o00Oo0O . IIIi % iI11I1II1I1I % I1ii11iIi11i
    if 86 - 86: Ii - I11i . O0OoO * I1ii11iIi11i / Ii11Ii1I % I11i
    if 61 - 61: I11i + OOooOOo
    if 15 - 15: OOooOOo * OoOo00o + IIIii1II1II . iI1iI1I1i1I % oOo0O0Ooo - O0OoO
    if 13 - 13: OOooOOo % OOooOOo % I1ii11iIi11i % oOo0O0Ooo * ooOoO0O00 % iI1iI1I1i1I
    if 82 - 82: OooO0OoOOOO . OOooOOo / O0OoO + o0oOO0O00o0O - O0OoO
    if 55 - 55: O0OoO % I1ii11iIi11i % I11i
 if OoO0oO0oo0O != 'Failed' :
  I1Ii = [ ]
  O00Ooo0ooo0 = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( OoO0oO0oo0O )
  for iIII , OOOOoO00o0O , iIIiiiI , I1iI11iii , i1I1i111Ii in O00Ooo0ooo0 :
   if Ooo0OOoOoO0 . lower in i1I1i111Ii . lower ( ) :
    if i1I1i111Ii in I1Ii :
     pass
    else :
     II1I ( ( '[COLORgreen]' + i1I1i111Ii + '- source Scooby[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( 'Ganool' , '' ) . replace ( 'ShAaNiG' , '' ) . replace ( 'YIFY' , '' ) . replace ( '[[ Max-Movie.In ]]' , '' ) . replace ( '.mkv' , '' ) . replace ( '.mp4' , '' ) . replace ( '.' , ' ' ) , iIII , 1016 , OOOOoO00o0O , I1iI11iii , iIIiiiI )
     I1Ii . append ( i1I1i111Ii )
     Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     Oo0oO0ooo . update ( 36 , "" , "Getting Scooby Links" )
     iiO0o0oOOOoOo ( 'tvshows' , 'Media Info 3' )
 if oooOOO0ooOoOOO != 'Failed' :
  oO00o0O00o = re . compile ( 'href="(.+?)".+?src="(.+?)" alt="Image of (.+?)"' , re . DOTALL ) . findall ( oooOOO0ooOoOOO )
  for iIII , iiI1IIIi , i1I1i111Ii in oO00o0O00o :
   if Ooo0OOoOoO0 . lower in i1I1i111Ii . lower ( ) :
    IiIiiI11111I1 ( ( '[COLORgreen]' + i1I1i111Ii + '- source Snag[/COLOR]' ) . replace ( '&#x27;' , '' ) , 'http://www.snagfilms.com' + iIII , 7067 , iiI1IIIi )
    Oo0oO0ooo . update ( 45 , "" , "Getting Snag Links" )
    if 98 - 98: O0OoO . IIIii1II1II
    iiO0o0oOOOoOo ( 'tvshows' , 'Media Info 3' )
 if o0IiIiI111IIII1 != 'Failed' :
  OOooO00OO = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( o0IiIiI111IIII1 )
  for iIII , OOOOoO00o0O , iIIiiiI , I1iI11iii , i1I1i111Ii in OOooO00OO :
   if Ooo0OOoOoO0 . lower in i1I1i111Ii . lower ( ) :
    ooOOoooooo ( ( '[COLORgreen]' + i1I1i111Ii + '- source Redemption[/COLOR]' ) , iIII , 222 , OOOOoO00o0O , I1iI11iii , iIIiiiI )
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 53 , "" , "Getting Redemption Links" )
    if 70 - 70: Ii11Ii1I - IIIii1II1II * IIIii1II1II / iI11I1II1I1I + o0o00Oo0O
    iiO0o0oOOOoOo ( 'tvshows' , 'Media Info 3' )
 if OOOoOooO000oO != 'Failed' :
  IiIIi11i = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( OOOoOooO000oO )
  for iIII , OOOOoO00o0O , iIIiiiI , I1iI11iii , i1I1i111Ii in IiIIi11i :
   if Ooo0OOoOoO0 . lower in i1I1i111Ii . lower ( ) :
    ooOOoooooo ( ( '[COLORgreen]' + i1I1i111Ii + '- source Reaper[/COLOR]' ) , iIII , 222 , OOOOoO00o0O , I1iI11iii , iIIiiiI )
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 61 , "" , "Getting Reaper Links" )
    if 49 - 49: Ii1I + o0o00Oo0O . Ii11Ii1I * ii
    iiO0o0oOOOoOo ( 'tvshows' , 'Media Info 3' )
 if o0OOOOOo00 != 'Failed' :
  oO0OOO00 = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( o0OOOOOo00 )
  for iIII , OOOOoO00o0O , iIIiiiI , I1iI11iii , i1I1i111Ii in oO0OOO00 :
   if Ooo0OOoOoO0 . lower in i1I1i111Ii . lower ( ) :
    ooOOoooooo ( ( '[COLORgreen]' + i1I1i111Ii + '- source Herovision[/COLOR]' ) , iIII , 222 , OOOOoO00o0O , I1iI11iii , iIIiiiI )
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 70 , "" , "Getting Herovision Links" )
    if 13 - 13: OooO0OoOOOO * Ii1I / Ii1I / iI11I1II1I1I % iI11I1II1I1I
    iiO0o0oOOOoOo ( 'tvshows' , 'Media Info 3' )
    if 21 - 21: Ii1I
 if oo0oOO != 'Failed' :
  oOOOO0oo0O0OO = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( oo0oOO )
  for iIII , OOOOoO00o0O , i1I1i111Ii in oOOOO0oo0O0OO :
   if Ooo0OOoOoO0 . lower in i1I1i111Ii . lower ( ) :
    IiIiiI11111I1 ( ( '[COLORgreen]' + i1I1i111Ii + '- source Silent Hunter[/COLOR]' ) , iIII , 222 , OOOOoO00o0O )
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 78 , "" , "Getting Silent Hunter Links" )
    if 58 - 58: O0OoO - I11i + o0o00Oo0O / ooOoO0O00 % ii
    iiO0o0oOOOoOo ( 'tvshows' , 'Media Info 3' )
 ii111Iiii = [ '480p' , '720p' , '1080p' , 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' , '720paction' , '720padventure' , '720panimation' , '720pcomedy' , '720pcrime' , '720pdocumentary' , '720pdrama' , '720pfamily' , '720pfantasy' , '720phorror' , '720pmystery' , '720promance' , '720psci-Fi' , '720psport' , '720pthriller' , '720pwestern' , '1080paction' , '1080padventure' , '1080panimation' , '1080pcomedy' , '1080pcrime' , '1080pdocumentary' , '1080pdrama' , '1080pfamily' , '1080pfantasy' , '1080phorror' , '1080pmystery' , '1080promance' , '1080psci-Fi' , '1080psport' , '1080pthriller' , '1080pwestern' , 'films' ]
 if 30 - 30: OoOo00o * I1ii11iIi11i / OoOo00o . IIiIiII11i . I1ii11iIi11i
 for oO0Ooo0OooOOo in ii111Iiii :
  O00o0O = IIIII + oO0Ooo0OooOOo + ooOoOoo0O
  ooIi111iII = O000OO0 ( O00o0O )
  if ooIi111iII != 'Failed' :
   Oo0OoOo = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( ooIi111iII )
   for iIII , OOOOoO00o0O , iIIiiiI , I1iI11iii , i1I1i111Ii in Oo0OoOo :
    if Ooo0OOoOoO0 . lower in i1I1i111Ii . lower ( ) :
     ooOOoooooo ( '[COLORgreen]' + i1I1i111Ii + ' - Source Pandoras[/COLOR]' , iIII , 222 , OOOOoO00o0O , I1iI11iii , iIIiiiI )
     Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     Oo0oO0ooo . update ( 89 , "" , "Getting Pandoras Links" )
     if 13 - 13: I11i
     iiO0o0oOOOoOo ( 'tvshows' , 'Media Info 3' )
     if 7 - 7: oOo0O0Ooo + OooO0OoOOOO / Ii / I1ii11iIi11i
 ii111Iiii = [ '0-9/' , 'A/' , 'B/' , 'C/' , 'D/' , 'E/' , 'F/' , 'G/' , 'H/' , 'I/' , 'J/' , 'K/' , 'L/' , 'M/' , 'N/' , 'O/' , 'P/' , 'R/' , 'S/' , 'T/' , 'U/' , 'V/' , 'W/' , 'X/' , 'Y/' , 'Z/' ]
 if 97 - 97: IIIi . iI1iI1I1i1I / oOo0O0Ooo
 if 83 - 83: iI1iI1I1i1I - Ii1I * OoOo00o
 for oO0Ooo0OooOOo in ii111Iiii :
  O00o0O = iI1 + oO0Ooo0OooOOo
  oOO00OO0OooOo = O000OO0 ( O00o0O )
  if OoO0oO0oo0O != 'Failed' :
   ii111iI1i1 = re . compile ( '<li><a href="(.+?)"> (.+?)</a></li>' ) . findall ( oOO00OO0OooOo )
   for Oo0o0O0o , i1I1i111Ii in ii111iI1i1 :
    if Ooo0OOoOoO0 . lower in i1I1i111Ii . lower ( ) :
     OO0ooOOO00 ( ( '[COLORgreen]' + i1I1i111Ii + 'source 5[/COLOR]' ) . replace ( 'Ganool' , '' ) . replace ( 'ShAaNiG' , '' ) . replace ( 'YIFY' , '' ) . replace ( '[[ Max-Movie.In ]]' , '' ) . replace ( '.mkv' , '' ) . replace ( '.mp4' , '' ) . replace ( '.' , ' ' ) , ( iI1 + oO0Ooo0OooOOo + Oo0o0O0o ) , 222 , '' )
     Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     Oo0oO0ooo . update ( 100 , "" , "Getting Source 5 Links" )
     if 80 - 80: oO0o / OooO0OoOOOO * oOo0O0Ooo % OooO0OoOOOO
     iiO0o0oOOOoOo ( 'tvshows' , 'Media Info 3' )
     if 95 - 95: o0o00Oo0O / iI1iI1I1i1I . IIIi
     if 17 - 17: iI1iI1I1i1I
def o0OO0OO000OO ( ) :
 if 92 - 92: iI1iI1I1i1I % ooOoO0O00 % O0OoO % OooO0OoOOOO % I11i
 Ooo0OOoOoO0 = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 IIo0Oo0oO0oOO00 = Ooo0OOoOoO0 . lower ( )
 if 61 - 61: IIIii1II1II * I11i * o0o00Oo0O / o0oOO0O00o0O
 iIII = ( i1111 ( 'aHR0cDovL2RsLmZhcnNpbW92aWUubmV0L1NlcmlhbC8=' ) )
 if 52 - 52: I1ii11iIi11i + iI11I1II1I1I + ooOoO0O00 * Ii11Ii1I - IIiIiII11i . IIiIiII11i
 I1i111I = ( i1111 ( 'aHR0cDovL3R2LmRsLXBhcnMuaW4v' ) )
 Iii1I1iI = ( i1111 ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9BbWVyaWNhbiUyMFNlcmlhbC8=' ) )
 oooOoo0OoOO0000 = ( i1111 ( 'aHR0cDovL2RpemlsYWIuY29tL2Fyc2l2P2xpbWl0PSZ0dXI9Jm9yZGVyYnk9JnVsa2U9Jm9yZGVyPSZ5aWw9JmRpemlfYWRpPQ==' ) ) + ( IIo0Oo0oO0oOO00 ) . replace ( ' ' , '+' )
 i11Ii1iIIIIi = ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvc2hvd3MvdHZhbGwucGhw' ) )
 iiiO000OOO = ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9UaGVfUmVhcGVyL2FsbHR2LnBocA==' ) )
 o0IIi1 = ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC90dmZ1bGwucGhw' ) )
 if 62 - 62: OoOo00o + I1ii11iIi11i / Ii
 Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Checking Sources" , '' , 'Please Wait' )
 if 90 - 90: iI11I1II1I1I + OOooOOo
 Oo0oO0ooo . update ( 0 , "" , "Checking Source 1/9 Links" )
 o00OO00OoO = O000OO0 ( iIII )
 Oo0oO0ooo . update ( 14 , "" , "Checking Source 2/9 Links" )
 if 9 - 9: iI11I1II1I1I . ii + ooOoO0O00 - I1ii11iIi11i
 Oo0oO0ooo . update ( 28 , "" , "Checking Source 3/9 Links" )
 O0Oo000ooO00 = O000OO0 ( I1i111I )
 Oo0oO0ooo . update ( 40 , "" , "Checking Source 4/9 Links" )
 oO0 = O000OO0 ( Iii1I1iI )
 Oo0oO0ooo . update ( 52 , "" , "Checking Source 5/9 Links" )
 OoO0oO0oo0O = cloudflare . source ( oooOoo0OoOO0000 )
 Oo0oO0ooo . update ( 64 , "" , "Checking Source 6/9 Links" )
 oOO00OO0OooOo = O000OO0 ( i11Ii1iIIIIi )
 Oo0oO0ooo . update ( 76 , "" , "Checking Source 7/9 Links" )
 oooOOO0ooOoOOO = O000OO0 ( iiiO000OOO )
 Oo0oO0ooo . update ( 88 , "" , "Checking Source 8/9 Links" )
 o0IiIiI111IIII1 = O000OO0 ( o0IIi1 )
 Oo0oO0ooo . update ( 100 , "" , "Checking Source 9/9 Links" )
 if 30 - 30: o0oOO0O00o0O / oO0o . o0oOO0O00o0O
 if o0IiIiI111IIII1 != 'Failed' :
  OOooO00OO = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( o0IiIiI111IIII1 )
  for iIII , OOOOoO00o0O , iIIiiiI , I1iI11iii , i1I1i111Ii in OOooO00OO :
   if IIo0Oo0oO0oOO00 in i1I1i111Ii . lower ( ) :
    II1I ( ( '[COLORgreen]' + i1I1i111Ii + '- source HeroVision[/COLOR]' ) , iIII , 1016 , OOOOoO00o0O , I1iI11iii , iIIiiiI )
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 10 , "" , "Getting Herovision Links" )
    if 17 - 17: I1ii11iIi11i + ii * ii
    iiO0o0oOOOoOo ( 'tvshows' , 'Media Info 3' )
    if 5 - 5: IIIi % ii . OOooOOo
 if oooOOO0ooOoOOO != 'Failed' :
  oO00o0O00o = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( oooOOO0ooOoOOO )
  for iIII , OOOOoO00o0O , iIIiiiI , I1iI11iii , i1I1i111Ii in oO00o0O00o :
   if IIo0Oo0oO0oOO00 in i1I1i111Ii . lower ( ) :
    II1I ( ( '[COLORgreen]' + i1I1i111Ii + '- source Reaper[/COLOR]' ) , iIII , 1016 , OOOOoO00o0O , I1iI11iii , iIIiiiI )
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 20 , "" , "Getting Reaper Links" )
    if 67 - 67: Ii1I + Ii11Ii1I
    iiO0o0oOOOoOo ( 'tvshows' , 'Media Info 3' )
    if 72 - 72: OooO0OoOOOO % I11i
    if 93 - 93: iI11I1II1I1I + Ii . I11i . ooOoO0O00 % oOo0O0Ooo % O0OoO
    if 74 - 74: OOooOOo / ooOoO0O00 % ii
    if 52 - 52: OooO0OoOOOO % O0OoO
    if 25 - 25: iI1iI1I1i1I / iI1iI1I1i1I % ii - Ii1I * OoOo00o
    if 23 - 23: Ii
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 30 , "" , "Getting CoolSeries Links" )
    if 100 - 100: OoOo00o + o0o00Oo0O . oOo0O0Ooo + ooOoO0O00 - OOooOOo + I11i
    iiO0o0oOOOoOo ( 'tvshows' , 'Media Info 3' )
 if o00OO00OoO != 'Failed' :
  Ii1i = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( o00OO00OoO )
  for i1I1i111Ii in Ii1i :
   if IIo0Oo0oO0oOO00 in i1I1i111Ii . lower ( ) :
    IiIiiI11111I1 ( '[COLORgreen]' + ( i1I1i111Ii ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) + ' source 1 [/COLOR]' , ( iIII + i1I1i111Ii ) . replace ( ' ' , '%20' ) , 1006 , '' )
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 40 , "" , "Getting Source 1 Links" )
    if 65 - 65: IIiIiII11i / I1ii11iIi11i
    iiO0o0oOOOoOo ( 'tvshows' , 'Media Info 3' )
    if 42 - 42: Ii . o0o00Oo0O
    if 75 - 75: IIIi + iI11I1II1I1I
    if 19 - 19: oOo0O0Ooo + Ii . OooO0OoOOOO - iI1iI1I1i1I / Ii11Ii1I + I11i
    if 38 - 38: I1ii11iIi11i / iI11I1II1I1I * iI11I1II1I1I % Ii1I
    if 92 - 92: iI1iI1I1i1I / o0o00Oo0O * oOo0O0Ooo - iI1iI1I1i1I
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 50 , "" , "Getting Source 2 Links" )
    if 99 - 99: Ii % ii
    iiO0o0oOOOoOo ( 'tvshows' , 'Media Info 3' )
 if O0Oo000ooO00 != 'Failed' :
  i111i1i = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( O0Oo000ooO00 )
  for i1I1i111Ii in i111i1i :
   if IIo0Oo0oO0oOO00 in i1I1i111Ii . lower ( ) :
    IiIiiI11111I1 ( ( i1I1i111Ii + ' source 3' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( I1i111I + i1I1i111Ii ) . replace ( ' ' , '%20' ) , 1006 , '' )
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 60 , "" , "Getting Source 3 Links" )
    if 56 - 56: OooO0OoOOOO * IIIi
    iiO0o0oOOOoOo ( 'tvshows' , 'Media Info 3' )
 if oO0 != 'Failed' :
  O00oO0O = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( oO0 )
  for i1I1i111Ii in O00oO0O :
   if IIo0Oo0oO0oOO00 in i1I1i111Ii . lower ( ) :
    IiIiiI11111I1 ( ( i1I1i111Ii + ' source 4' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( Iii1I1iI + i1I1i111Ii ) . replace ( ' ' , '%20' ) , 1006 , '' )
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 70 , "" , "Getting Source 4 Links" )
    if 3 - 3: iI11I1II1I1I % Ii1I . IIIii1II1II % iI1iI1I1i1I
    iiO0o0oOOOoOo ( 'tvshows' , 'Media Info 3' )
 if OoO0oO0oo0O != 'Failed' :
  O00Ooo0ooo0 = re . compile ( '<a href="(.+?)" class="film-image">\n<img src="(.+?)" alt=""/>\n</a>\n<div class="tss-detail">\n<a class="title" style="" href=".+?">\n<span class="position">.+?</span>\n(.+?)</a>' ) . findall ( OoO0oO0oo0O )
  for iIII , iiI1IIIi , i1I1i111Ii in O00Ooo0ooo0 :
   if IIo0Oo0oO0oOO00 in i1I1i111Ii . lower ( ) :
    IiIiiI11111I1 ( '[COLORgreen]' + i1I1i111Ii + ' - Source - Dizi[/COLOR]' , iIII , 8062 , iiI1IIIi )
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 80 , "" , "Getting Dizi Links" )
    if 40 - 40: O0OoO * Ii11Ii1I . Ii11Ii1I + IIiIiII11i + ii
    iiO0o0oOOOoOo ( 'tvshows' , 'Media Info 3' )
 if oOO00OO0OooOo != 'Failed' :
  ii111iI1i1 = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( oOO00OO0OooOo )
  for iIII , OOOOoO00o0O , iIIiiiI , I1iI11iii , i1I1i111Ii in ii111iI1i1 :
   if IIo0Oo0oO0oOO00 in i1I1i111Ii . lower ( ) :
    II1I ( ( '[COLORgreen]' + i1I1i111Ii + '- Source Scooby[/COLOR]' ) , iIII , 1016 , OOOOoO00o0O , I1iI11iii , iIIiiiI )
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 90 , "" , "Getting Scooby Links" )
    if 17 - 17: OooO0OoOOOO % Ii11Ii1I
    iiO0o0oOOOoOo ( 'tvshows' , 'Media Info 3' )
    if 46 - 46: oOo0O0Ooo - iI1iI1I1i1I / ii - ooOoO0O00 . Ii
 Ii1Ii1IiIIIi1 = [ 'a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' , 'p' , 'q' , 'r' , 's' , 't' , 'u' , 'v' , 'w' , 'x' , 'y' , 'z' ]
 if 55 - 55: OoOo00o + o0o00Oo0O / o0oOO0O00o0O % O0OoO / ii
 for oO0Ooo0OooOOo in Ii1Ii1IiIIIi1 :
  O00o0O = IIIII + oO0Ooo0OooOOo + ooOoOoo0O
  o0OOOOOo00 = iiI111I1iIiI ( O00o0O )
  if o0OOOOOo00 != 'Failed' :
   oO0OOO00 = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( o0OOOOOo00 )
   for i1I1i111Ii , iIIiiiI , iIII , iiI1IIIi , I1I1I1IIi1III , OOoOoo00Oo in oO0OOO00 :
    if IIo0Oo0oO0oOO00 in i1I1i111Ii . lower ( ) :
     II1I ( '[COLORgreen]' + i1I1i111Ii + ' - Source Pandoras[/COLOR]' , iIII , OOoOoo00Oo , iiI1IIIi , I1I1I1IIi1III , iIIiiiI )
     Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     Oo0oO0ooo . update ( 100 , "" , "Getting Pandoras Links" )
     if 98 - 98: Ii11Ii1I * iI11I1II1I1I % I1ii11iIi11i % IIIii1II1II
     iiO0o0oOOOoOo ( 'tvshows' , 'Media Info 3' )
     if 88 - 88: o0oOO0O00o0O - IIiIiII11i / o0oOO0O00o0O - Ii11Ii1I
     if 16 - 16: I1ii11iIi11i % IIIi
 xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
def i1iIOo ( ) :
 if 18 - 18: o0o00Oo0O - ooOoO0O00 . IIIi
 Ooo0OOoOoO0 = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 IIo0Oo0oO0oOO00 = Ooo0OOoOoO0 . lower ( )
 iIII = ( i1111 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz' ) )
 o00OO00OoO = iiI111I1iIiI ( iIII )
 Ii1i = re . compile ( '"id":".+?","name":"(.+?)","img":"(.+?)","stream_url3":".+?","cat_id":"(.+?)","stream_url2":".+?","stream_url":".+?"}' , re . DOTALL ) . findall ( o00OO00OoO )
 for i1I1i111Ii , iiI1IIIi , o00OOo00 in Ii1i :
  oooOIi1I1iIIIiiii = i1111 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv' ) + ( iiI1IIIi ) . replace ( '\\' , '' )
  if Ooo0OOoOoO0 in i1I1i111Ii . lower ( ) :
   IiIiiI11111I1 ( i1I1i111Ii , '' , 7022 , oooOIi1I1iIIIiiii )
   if 70 - 70: o0oOO0O00o0O . IIiIiII11i . o0oOO0O00o0O - iI11I1II1I1I
 xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
ooOo0O0 = '{ZH},' ; ooo0I11 = '{IX},' ; OOO0 = '{LM},'
if 16 - 16: o0oOO0O00o0O / iI11I1II1I1I + IIIii1II1II * o0oOO0O00o0O * iI1iI1I1i1I
def iiIiI11IiI1ii ( url ) :
 ooO0O0 = cloudflare . source ( url )
 Ii1i = re . compile ( '<a class="season" href="(.+?)">\n(.+?)\n</a>\n</span>\n<span>\n<a class="episode" href=".+?">\n(.+?)\n</a>\n</span>\n<span>\n<a class="episode-name" href=".+?">\n(.+?)</a>' ) . findall ( ooO0O0 )
 for url , iIi11io0o00o0Oo , II1i11I , i1I1i111Ii in Ii1i :
  IiIiiI11111I1 ( ( iIi11io0o00o0Oo ) . replace ( 'Sezon' , ' Season ' ) + ( II1i11I ) . replace ( 'Bölüm' , ' Episode ' ) + i1I1i111Ii , url , 8063 , '' )
  if 34 - 34: ooOoO0O00 - OOooOOo + I11i - I1ii11iIi11i % Ii1I
  if 43 - 43: iI1iI1I1i1I % ooOoO0O00 % O0OoO . Ii
  if 56 - 56: o0o00Oo0O * o0oOO0O00o0O + o0oOO0O00o0O * iI11I1II1I1I / O0OoO * IIIi
  if 25 - 25: iI11I1II1I1I . iI1iI1I1i1I * Ii + I1ii11iIi11i * iI1iI1I1i1I
def o0oOooO0oo00 ( url ) :
 ooO0O0 = cloudflare . source ( url )
 Ii1i = re . compile ( 'file: "(.+?)",.+?label: "(.+?)",' , re . DOTALL ) . findall ( ooO0O0 )
 for url , i1I1i111Ii in Ii1i :
  OO0ooOOO00 ( i1I1i111Ii , url , 222 , '' )
  if 70 - 70: oOo0O0Ooo + Ii11Ii1I
  if 70 - 70: OooO0OoOOOO . Ii
  if 76 - 76: o0oOO0O00o0O . OooO0OoOOOO % o0oOO0O00o0O - IIIi
  if 51 - 51: ii + I11i * iI11I1II1I1I * OoOo00o / ooOoO0O00
def I11IiI1i ( ) :
 if 81 - 81: iI11I1II1I1I / OoOo00o . Ii * IIiIiII11i
 ooO0O0 = cloudflare . source ( i1111 ( 'aHR0cDovL2RpemlsYWIuY29t' ) )
 Ii1i = re . compile ( '<li id=".+?">.+?<a href="(.+?)">.+?<img width="40" height="40" src="(.+?)" alt=""/>.+?<span class="title">\n(.+?)</span>.+?<span class="alt-title">\n(.+?)</span>.+?</a>.+?</li>' , re . DOTALL ) . findall ( ooO0O0 )
 for iIII , iiI1IIIi , i1I1i111Ii , II1i11I in Ii1i :
  IiIiiI11111I1 ( i1I1i111Ii + '  -  ' + ( II1i11I ) . replace ( 'sezon' , 'Season' ) . replace ( 'bölüm' , 'Episode' ) , iIII , 8063 , iiI1IIIi )
  if 55 - 55: Ii1I
def oOoo0OO0 ( ) :
 IIiI1Ii = O0O0O0Oo ( i1111 ( 'aHR0cDovL3d3dy50dmd1aWRlLmNvLnVrLw==' ) )
 Ii1i = re . compile ( '<a href="(.+?)"  qt-title=".+?" qt-text=".+?<br> .+?" title="(.+?)".+?class=".+? src="(.+?)" alt=".+?" /></a>' , re . DOTALL ) . findall ( IIiI1Ii )
 for iIII , i1I1i111Ii , iiI1IIIi in Ii1i :
  OO0ooOOO00 ( '[COLORgreen]' + i1I1i111Ii + '[/COLOR]' , iIII , 8002 , iiI1IIIi )
def iiIiIi1111iI1 ( url ) :
 IIiI1Ii = O0O0O0Oo ( url )
 Ii1i = re . compile ( '<table border="0".+?url((.+?));background-repeat: no-repeat;">.+?<tr>.+?<span class="season">(.+?)</span><br>.+?<a href="(.+?)"+?>(.+?)</span><br>.+?<span class="programmetext">(.+?)</span></a><br>' , re . DOTALL ) . findall ( IIiI1Ii )
 for iiI1IIIi , time , url , i1I1i111Ii , Ii1IIiiIiiIi in Ii1i :
  II1I ( '%s %s' % ( '[COLORgreen]' + i1I1i111Ii + '[/COLOR]' , time ) , url , 1015 , iiI1IIIi , Ii1IIiiIiiIi )
  if 11 - 11: Ii1I . Ii1I + IIiIiII11i * OOooOOo . OooO0OoOOOO
def I1I1i1I1I1I1 ( ) :
 if 34 - 34: oO0o * Ii11Ii1I * I1ii11iIi11i
 IiIiiI11111I1 ( 'Coronation Street' , '' , 8001 , '' )
 IiIiiI11111I1 ( 'Eastenders' , '' , 8002 , '' )
 IiIiiI11111I1 ( 'Emmerdale' , '' , 8003 , '' )
 IiIiiI11111I1 ( 'Hollyoaks' , '' , 8004 , '' )
 IiIiiI11111I1 ( 'Im a Celebrity' , '' , 8005 , '' )
 if 21 - 21: ii . OOooOOo - iI11I1II1I1I % OooO0OoOOOO
 if 55 - 55: o0o00Oo0O % oOo0O0Ooo . ii * I1ii11iIi11i / ii . Ii11Ii1I
 if 26 - 26: OooO0OoOOOO / iI11I1II1I1I - iI11I1II1I1I
 if 57 - 57: OooO0OoOOOO
def IiI11I1Ii11II ( ) :
 o00OO00OoO = iiI111I1iIiI ( 'http://uksoapshare.blogspot.co.uk/' )
 Ii1i = re . compile ( '<a href="(.+?)".+?target=_blank>(.+?)</a>' ) . findall ( o00OO00OoO )
 for iIII , i1I1i111Ii in Ii1i :
  if 'Holly' in i1I1i111Ii :
   iiI1IIIi = 'http://2.bp.blogspot.com/-9c7Sieh1RKs/UjD6TGAEEnI/AAAAAAAAAC8/84uwHfxcuYg/s1600/Hollyoaks.png'
   if 'huge' in iIII :
    OO0ooOOO00 ( ( i1I1i111Ii ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , iIII . replace ( '\\/' , '/' ) , 8006 , iiI1IIIi )
   else :
    pass
    if 75 - 75: Ii % OooO0OoOOOO
 xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE_IGNORE_THE ) ;
 if 30 - 30: I1ii11iIi11i
def iiII1Ii ( ) :
 o00OO00OoO = iiI111I1iIiI ( 'http://uksoapshare.blogspot.co.uk/' )
 Ii1i = re . compile ( '<a href="(.+?)".+?target=_blank>(.+?)</a>' ) . findall ( o00OO00OoO )
 for iIII , i1I1i111Ii in Ii1i :
  if 'East' in i1I1i111Ii :
   iiI1IIIi = 'http://3.bp.blogspot.com/-KWHcNbNJU8Y/Vi1ousRl7fI/AAAAAAAAAT8/ksNE12LH0nE/s1600/eastenders.jpg'
   if 'huge' in iIII :
    OO0ooOOO00 ( ( i1I1i111Ii ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , iIII . replace ( '\\/' , '/' ) , 8006 , iiI1IIIi )
   else :
    pass
    if 74 - 74: Ii11Ii1I * oOo0O0Ooo / O0OoO / iI1iI1I1i1I + IIiIiII11i + Ii
 xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 16 - 16: oOo0O0Ooo - OoOo00o . I1ii11iIi11i
def oOo000o ( ) :
 o00OO00OoO = iiI111I1iIiI ( 'http://uksoapshare.blogspot.co.uk/' )
 Ii1i = re . compile ( '<a href="(.+?)".+?target=_blank>(.+?)</a>' ) . findall ( o00OO00OoO )
 for iIII , i1I1i111Ii in Ii1i :
  if 'Emmer' in i1I1i111Ii :
   iiI1IIIi = 'http://2.bp.blogspot.com/-UfDcxisVV5c/UjH9vUicZ3I/AAAAAAAAADc/8Ozuiz1ojxw/s1600/Emmerdale.jpg'
   if 'huge' in iIII :
    OO0ooOOO00 ( ( i1I1i111Ii ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , iIII . replace ( '\\/' , '/' ) , 8006 , iiI1IIIi )
   else :
    pass
    if 64 - 64: o0o00Oo0O
 xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 41 - 41: OooO0OoOOOO % I11i
def oo0O0oOOO0o ( ) :
 o00OO00OoO = iiI111I1iIiI ( 'http://uksoapshare.blogspot.co.uk/' )
 Ii1i = re . compile ( '<a href="(.+?)".+?target=_blank>(.+?)</a>' ) . findall ( o00OO00OoO )
 for iIII , i1I1i111Ii in Ii1i :
  if 'Coro' in i1I1i111Ii :
   iiI1IIIi = 'http://3.bp.blogspot.com/-hofvfBQVexs/UjErIfNdS4I/AAAAAAAAADQ/Q-vVGu3apYU/s1600/corrie.jpg'
   if 'huge' in iIII :
    OO0ooOOO00 ( ( i1I1i111Ii ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , iIII . replace ( '\\/' , '/' ) , 8006 , iiI1IIIi )
   else :
    pass
    if 70 - 70: I1ii11iIi11i % Ii11Ii1I . Ii1I
 xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 8 - 8: oOo0O0Ooo - IIIi * iI1iI1I1i1I % ii / OOooOOo
def I1Io0oO0oo ( ) :
 o00OO00OoO = iiI111I1iIiI ( 'http://uksoapshare.blogspot.co.uk/' )
 Ii1i = re . compile ( '<a href="(.+?)" target="_blank">(.+?)</a>' ) . findall ( o00OO00OoO )
 for iIII , i1I1i111Ii in Ii1i :
  if 'Celeb' in i1I1i111Ii :
   iiI1IIIi = 'http://3.bp.blogspot.com/-a_yDotWU_pY/VkotKWaG_gI/AAAAAAAAAUk/8Q5iNM6p37k/s1600/iacgoh.jpg'
   if 'huge' in iIII :
    OO0ooOOO00 ( ( i1I1i111Ii ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , iIII . replace ( '\\/' , '/' ) , 8006 , iiI1IIIi )
   else :
    pass
    if 98 - 98: ii - oOo0O0Ooo + O0OoO
def O0I11IIIII ( name , url ) :
 OoOII11IiI1 = urlresolver . HostedMediaFile ( url ) . valid_url ( )
 if OoOII11IiI1 :
  OoOOOO00oOO = urlresolver . HostedMediaFile ( url ) . resolve ( )
 else :
  IIiI1Ii = open_url ( url )
  url = re . compile ( 'src="(.+?)"></iframe>' ) . findall ( IIiI1Ii ) [ 0 ]
  url = url . split ( '?autoplay' ) [ 0 ]
  IIiI1Ii = open_url ( url )
  iiIIiIi = re . compile ( 'mp4","url":"(.+?)"' ) . findall ( IIiI1Ii ) [ - 1 ]
  OoOOOO00oOO = iiIIiIi . replace ( '\\/' , '/' )
 IiI1iI1 = xbmcgui . ListItem ( name , '' , '' )
 IiI1iI1 . setPath ( OoOOOO00oOO )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , IiI1iI1 )
 if 97 - 97: o0oOO0O00o0O + iI1iI1I1i1I % I1ii11iIi11i . IIiIiII11i / IIiIiII11i * o0oOO0O00o0O
 if 80 - 80: IIIi / Ii + ii
def III11i1iI11 ( ) :
 IIiI1Ii = iiI111I1iIiI ( i1111 ( 'aHR0cDovL3d3dy5kaXppYm94aGQuY29tLw==' ) )
 Ii1i = re . compile ( 'class="film menu-item menu-item-type-post_type menu-item-object-page menu-item-36980"><a href="(.+?)"><i class="fa fa-film"></i><span>(.+?)</span></a></li>' ) . findall ( IIiI1Ii )
 I1 = re . compile ( 'class="menu-item menu-item-type-post_type menu-item-object-page menu-item-52949"><a href="(.+?)"><i class="fa fa-"></i><span>(.+?)</span></a></li>' ) . findall ( IIiI1Ii )
 for iIII , i1I1i111Ii in Ii1i :
  IiIiiI11111I1 ( ( '[COLORgreen]' + i1I1i111Ii + '[/COLOR]' ) . replace ( 'Diziler' , 'Series' ) , iIII , 7071 , ooOooo000oOO + 'popcorn.png' )
 for iIII , i1I1i111Ii in I1 :
  IiIiiI11111I1 ( ( '[COLORgreen]' + i1I1i111Ii + '[/COLOR]' ) . replace ( 'Filmler' , 'Movies' ) , iIII , 7071 , ooOooo000oOO + 'popcorn.png' )
  if 58 - 58: OoOo00o
def oOOo0OO00OoO ( ) :
 IIiI1Ii = iiI111I1iIiI ( i1111 ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL2NhdGVnb3JpZXMv' ) )
 Ii1i = re . compile ( '<a class="nav-item" href="(.+?)">(.+?)</a>' ) . findall ( IIiI1Ii )
 for iIII , i1I1i111Ii in Ii1i :
  if 'Movies' in i1I1i111Ii :
   IiIiiI11111I1 ( '[COLORgreen]' + i1I1i111Ii + '[/COLOR]' , 'http://www.snagfilms.com' + ( iIII ) . replace ( 'http://www.snagfilms.com' , '' ) , 7061 , ooOooo000oOO + 'popcorn.png' )
def oOOo0oO0oOOOo ( url ) :
 IIiI1Ii = iiI111I1iIiI ( url )
 Ii1i = re . compile ( '<a class="object-link size-poster".+?href="(.+?)" data-type="category">.+?src="(.+?)" alt="Image of (.+?)" />' , re . DOTALL ) . findall ( IIiI1Ii )
 Ii1i = re . compile ( '<a class="object-link size-poster".+?href="(.+?)" data-type="category">.+?src="(.+?)" alt="Image of (.+?)" />' , re . DOTALL ) . findall ( IIiI1Ii )
 I1 = re . compile ( "<li class='current'>.+?</li><li ><a href='(.+?)'>.+?</a></li><li" , re . DOTALL ) . findall ( IIiI1Ii )
 for url , iiI1IIIi , i1I1i111Ii in Ii1i :
  IiIiiI11111I1 ( '[COLORgreen]' + i1I1i111Ii + '[/COLOR]' , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7067 , iiI1IIIi )
 for url in I1 :
  IiIiiI11111I1 ( '[COLORgreen]NEXT PAGE[/COLOR]' , ( url ) . replace ( '&#038;' , '&' ) , 7063 , ooOooo000oOO + 'Next.png' )
  if 90 - 90: ooOoO0O00 - Ii11Ii1I
  if 79 - 79: IIiIiII11i - OoOo00o * Ii1I - OOooOOo . Ii1I
def iiII1IIii1i1 ( url ) :
 IIiI1Ii = iiI111I1iIiI ( i1111 ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL2NhdGVnb3JpZXMv' ) )
 Ii1i = re . compile ( '<a class="object-link size-poster".+?href="(.+?)" data-type="category">.+?src="(.+?)" alt="Image of (.+?)" />' , re . DOTALL ) . findall ( IIiI1Ii )
 for url , iiI1IIIi , i1I1i111Ii in Ii1i :
  IiIiiI11111I1 ( '[COLORgreen]' + i1I1i111Ii + '[/COLOR]' , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7062 , iiI1IIIi )
  if 38 - 38: o0oOO0O00o0O * ii
iIi11III = '{UJ},' ; IiiiIi1iiii11 = '{WE},' ; iIIi1IIIii11i = '{WP},' ; Ii11I1I11II = '{PP},'
def IIiiiI ( url ) :
 IIiI1Ii = iiI111I1iIiI ( url )
 Ii1i = re . compile ( 'href="(.+?)".+?src="(.+?)" alt="Image of (.+?)"' , re . DOTALL ) . findall ( IIiI1Ii )
 for url , iiI1IIIi , i1I1i111Ii in Ii1i :
  IiIiiI11111I1 ( ( '[COLORgreen]' + i1I1i111Ii + '[/COLOR]' ) . replace ( '&#x27;' , '' ) , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7067 , iiI1IIIi )
  if 59 - 59: OoOo00o % O0OoO
def ii1I ( url ) :
 IIiI1Ii = iiI111I1iIiI ( url )
 Ii1i = re . compile ( '<div class="film-container">.+?<iframe src="(.+?)"' , re . DOTALL ) . findall ( IIiI1Ii )
 for url in Ii1i :
  I1iiiiIIIIIiiI11i1 ( 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) )
  if 43 - 43: oOo0O0Ooo / o0oOO0O00o0O / O0OoO + iI11I1II1I1I + ii
def I1iiiiIIIIIiiI11i1 ( url ) :
 IIiI1Ii = iiI111I1iIiI ( url )
 Ii1i = re . compile ( 'file: "(.+?)",.+?label: "(.+?)"' , re . DOTALL ) . findall ( IIiI1Ii )
 for url , i1I1i111Ii in Ii1i :
  OO0ooOOO00 ( '[COLORgreen]' + i1I1i111Ii + '[/COLOR]' , url , 222 , ooOooo000oOO + 'popcorn.png' )
  if 33 - 33: IIiIiII11i - OooO0OoOOOO - O0OoO
  if 92 - 92: oO0o * OooO0OoOOOO
  if 92 - 92: OoOo00o
  if 7 - 7: o0oOO0O00o0O
def oOOoOO0O00o ( url ) :
 IIiI1Ii = iiI111I1iIiI ( url )
 Ii1i = re . compile ( '</h4><p><ul><li><a href="([^"]*)">(.+?)<.+?class=' ) . findall ( IIiI1Ii )
 I1 = re . compile ( '<li><a href="([^"]*)">(.+?)<.+?class=' ) . findall ( IIiI1Ii )
 for url , i1I1i111Ii in Ii1i :
  if '(cooltvseries.com)' in i1I1i111Ii :
   OO0ooOOO00 ( ( '[COLORgreen]' + i1I1i111Ii + ' -(360)-[/COLOR]' ) . replace ( ' - (cooltvseries.com).mp4' , '' ) , url , 7053 , ooOooo000oOO + 'CoolSeries.png' )
 for url , i1I1i111Ii in I1 :
  if '(cooltvseries.com)' in i1I1i111Ii :
   OO0ooOOO00 ( ( '[COLORgreen]' + i1I1i111Ii + '[/COLOR]' ) . replace ( ' - (cooltvseries.com).mp4' , '' ) , url , 7053 , ooOooo000oOO + 'CoolSeries.png' )
def Iii1Iii ( url ) :
 IIiI1Ii = iiI111I1iIiI ( url )
 Ii1i = re . compile ( '<source type="video/mp4" src="([^"]*)"/>' ) . findall ( IIiI1Ii )
 for url in Ii1i :
  oo0000o ( ( url ) . replace ( ' ' , '%20' ) )
o000o0o0ooO0 = '{XX},' ; iIi = '{UD},' ; O0OOoOOO0o0o = '{YT},' ; iI = '{JS},' ; Ooo0ooo0oo = '{PF},'
if 21 - 21: OooO0OoOOOO - oOo0O0Ooo % ii + I11i
def o00O0o ( ) :
 IIiI1Ii = iiI111I1iIiI ( i1111 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vc2VjcmV0L2Nsb3VkLnBocA==' ) )
 Ii1i = re . compile ( '<li class="col-sm-2">.+?<a href="#" class="thumbnail" data-src="(.+?)" data-toggle="modal".+?data-target="#infoModal" name="(.+?)"> <img src="(.+?)" alt=".+?" width="130px"' , re . DOTALL ) . findall ( IIiI1Ii )
 for iIII , i1I1i111Ii , iiI1IIIi in Ii1i :
  OO0ooOOO00 ( '[COLORgreen]' + i1I1i111Ii + '[/COLOR]' , 'http://stream.cloudtv.bz/stream/channel/20/' + ( i1111 ( iIII ) ) , 222 , iiI1IIIi )
  if 28 - 28: oOo0O0Ooo
def O00 ( url ) :
 IIiI1Ii = iiI111I1iIiI ( url )
 Ii1i = re . compile ( 'src="([^"]*)".+?alt=""></a><div class="entry unvoted"><p class="title"><a class="title may-blank " href="([^"]*)" tabindex=.+?>(.+?)</a>' , re . DOTALL ) . findall ( IIiI1Ii )
 next = re . compile ( '<a href="([^"]*)" rel="nofollow next"' , re . DOTALL ) . findall ( IIiI1Ii )
 for iiI1IIIi , url , i1I1i111Ii in Ii1i :
  if 'youtu' in url :
   OO0ooOOO00 ( ( '[COLORgreen]' + i1I1i111Ii + '[/COLOR]' ) . replace ( '&quot;' , '"' ) . replace ( '&' , ' & ' ) , url , 7051 , 'http:' + iiI1IIIi )
 for url in next :
  IiIiiI11111I1 ( '[COLORgreen]NEXT[/COLOR]' , url , 7050 , ooOooo000oOO + 'Next.png' )
  if 25 - 25: Ii / OOooOOo - IIIi / oO0o . I11i . I11i
def iI1iIIII1 ( url ) :
 IIiI1Ii = iiI111I1iIiI ( url )
 Ii1i = re . compile ( 'rel="shortlink" href="([^"]*)">' , re . DOTALL ) . findall ( IIiI1Ii )
 for url in Ii1i :
  yt . PlayVideo ( ( url ) . replace ( 'https://youtu.be/' , '' ) )
  if 65 - 65: o0o00Oo0O / IIiIiII11i . iI11I1II1I1I . OoOo00o / I1ii11iIi11i % iI11I1II1I1I
def Oo0Oo ( url ) :
 IIiI1Ii = iiI111I1iIiI
 Ii1i = re . compile ( 'id:"(.+?)",url:"(.+?)"' , re . DOTALL ) . findall ( IIiI1Ii )
 for url , iiI1IIIi , i1I1i111Ii in Ii1i :
  IiIiiI11111I1 ( '[COLORgreen]' + i1I1i111Ii + '[/COLOR]' , url , 222 , iiI1IIIi )
  if 60 - 60: I11i . OOooOOo % IIIi / oOo0O0Ooo / o0o00Oo0O
  if 19 - 19: Ii . oOo0O0Ooo + IIiIiII11i / IIIii1II1II . Ii1I * O0OoO
  if 59 - 59: iI11I1II1I1I / Ii1I % O0OoO
  if 84 - 84: iI11I1II1I1I / oOo0O0Ooo . OOooOOo % iI1iI1I1i1I
  if 99 - 99: I1ii11iIi11i + Ii
def I111Ii11i11I ( ) :
 if 15 - 15: iI1iI1I1i1I / I1ii11iIi11i * iI1iI1I1i1I
 IiIiiI11111I1 ( 'All Channels' , '' , 7021 , ooOooo000oOO + 'livetv.png' )
 IiIiiI11111I1 ( 'Entertainment' , '' , 7021 , ooOooo000oOO + 'livetv.png' )
 IiIiiI11111I1 ( 'Movies' , '' , 7021 , ooOooo000oOO + 'livetv.png' )
 IiIiiI11111I1 ( 'Music' , '' , 7021 , ooOooo000oOO + 'livetv.png' )
 IiIiiI11111I1 ( 'News' , '' , 7021 , ooOooo000oOO + 'livetv.png' )
 IiIiiI11111I1 ( 'Sports' , '' , 7021 , ooOooo000oOO + 'livetv.png' )
 IiIiiI11111I1 ( 'Documentary' , '' , 7021 , ooOooo000oOO + 'livetv.png' )
 IiIiiI11111I1 ( 'Kids' , '' , 7021 , ooOooo000oOO + 'livetv.png' )
 IiIiiI11111I1 ( 'Food' , '' , 7021 , ooOooo000oOO + 'livetv.png' )
 IiIiiI11111I1 ( 'Religious' , '' , 7021 , ooOooo000oOO + 'livetv.png' )
 IiIiiI11111I1 ( 'USA Channels' , '' , 7021 , ooOooo000oOO + 'livetv.png' )
 IiIiiI11111I1 ( 'Other' , '' , 7021 , ooOooo000oOO + 'livetv.png' )
 if 20 - 20: O0OoO - IIIii1II1II * oO0o * I11i * IIIii1II1II / OooO0OoOOOO
 if 40 - 40: oOo0O0Ooo * I11i . oOo0O0Ooo
def o00o0O0 ( Cat_Name ) :
 if 47 - 47: O0OoO
 Oo0oo = False
 IiIi = '0'
 if Cat_Name == 'All Channels' : Oo0oo = True
 if Cat_Name == 'Entertainment' : IiIi = '1'
 if Cat_Name == 'Movies' : IiIi = '2'
 if Cat_Name == 'Music' : IiIi = '3'
 if Cat_Name == 'News' : IiIi = '4'
 if Cat_Name == 'Sports' : IiIi = '5'
 if Cat_Name == 'Documentary' : IiIi = '6'
 if Cat_Name == 'Kids' : IiIi = '7'
 if Cat_Name == 'Food' : IiIi = '8'
 if Cat_Name == 'Religious' : IiIi = '9'
 if Cat_Name == 'USA Channels' : IiIi = '10'
 if Cat_Name == 'Other' : IiIi = '11'
 if 36 - 36: IIIii1II1II * Ii11Ii1I
 IIiI1Ii = iiI111I1iIiI ( i1111 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz' ) )
 Ii1i = re . compile ( '"id":".+?","name":"(.+?)","img":"(.+?)","stream_url3":".+?","cat_id":"(.+?)","stream_url2":".+?","stream_url":".+?"}' , re . DOTALL ) . findall ( IIiI1Ii )
 print 'Len Match: >>>' + str ( len ( Ii1i ) )
 for i1I1i111Ii , iiI1IIIi , o00OOo00 in Ii1i :
  oooOIi1I1iIIIiiii = i1111 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv' ) + ( iiI1IIIi ) . replace ( '\\' , '' )
  if o00OOo00 == IiIi :
   IiIiiI11111I1 ( i1I1i111Ii , '' , 7022 , oooOIi1I1iIIIiiii )
  elif Oo0oo == True :
   IiIiiI11111I1 ( i1I1i111Ii , '' , 7022 , oooOIi1I1iIIIiiii )
  else : pass
  if 16 - 16: IIiIiII11i
  xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 100 - 100: o0o00Oo0O - ooOoO0O00
def iII1iiiiI1i ( Search_Name ) :
 IIiI1Ii = iiI111I1iIiI ( i1111 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz' ) )
 Ii1i = re . compile ( '"id":".+?","name":"' + Search_Name + '","img":"(.+?)","stream_url3":"(.+?)","cat_id":".+?","stream_url2":"(.+?)","stream_url":"(.+?)"}' , re . DOTALL ) . findall ( IIiI1Ii )
 Ii1i = re . compile ( '"id":".+?","name":"' + Search_Name + '","img":"(.+?)","stream_url3":"(.+?)","cat_id":".+?","stream_url2":"(.+?)","stream_url":"(.+?)"}' , re . DOTALL ) . findall ( IIiI1Ii )
 for iiI1IIIi , iIII , IiI1iiiIii , I1i111I in Ii1i :
  oooOIi1I1iIIIiiii = i1111 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv' ) + ( iiI1IIIi ) . replace ( '\\' , '' )
  OO0ooOOO00 ( Search_Name + ': Link 1' , ( iIII ) . replace ( '\\' , '' ) , 222 , oooOIi1I1iIIIiiii )
  OO0ooOOO00 ( Search_Name + ': Link 2' , ( IiI1iiiIii ) . replace ( '\\' , '' ) , 222 , oooOIi1I1iIIIiiii )
  OO0ooOOO00 ( Search_Name + ': Link 3' , ( I1i111I ) . replace ( '\\' , '' ) , 222 , oooOIi1I1iIIIiiii )
  if 58 - 58: iI11I1II1I1I / oOo0O0Ooo - Ii1I . I11i - I1ii11iIi11i
def oOo ( ) :
 IIiI1Ii = iiI111I1iIiI ( i1111 ( o0OO00 ( 0 , [ 97 ] , [ 221 , 72 , 245 , 82 , 68 , 48 , 242 , 99 , 143 , 68 , 9 , 111 , 24 , 118 , 180 , 76 , 29 , 51 , 14 , 100 , 187 , 51 , 105 , 100 , 106 , 121 , 52 , 53 , 240 , 114 , 26 , 98 , 252 , 50 , 197 , 82 , 218 , 112 , 19 , 99 , 94 , 71 , 54 , 120 , 104 , 108 , 174 , 101 , 107 , 72 , 168 , 82 , 191 , 50 , 88 , 76 , 90 , 109 , 138 , 78 , 24 , 118 , 89 , 76 , 218 , 110 , 231 , 86 , 105 , 114 , 252 , 76 , 37 , 50 , 36 , 82 , 96 , 118 , 27 , 100 , 120 , 50 , 160 , 53 , 72 , 115 , 200 , 98 , 80 , 50 , 201 , 70 , 114 , 107 , 9 , 99 , 113 , 121 , 127 , 57 , 155 , 106 , 213 , 97 , 194 , 71 , 192 , 70 , 162 , 116 , 27 , 99 , 46 , 71 , 191 , 108 , 4 , 118 , 24 , 98 , 27 , 109 , 105 , 108 , 89 , 119 , 164 , 100 , 88 , 72 , 237 , 89 , 93 , 117 , 40 , 98 , 211 , 84 , 75 , 78 , 216 , 49 ] ) ) )
 Ii1i = re . compile ( '#EXTINF:-1,(.+)\s*(.+)\s*' ) . findall ( IIiI1Ii )
 for i1I1i111Ii , iIII in Ii1i :
  OO0ooOOO00 ( i1I1i111Ii , ( iIII ) . replace ( '"' , ' ' ) . replace ( '&' , '&' ) . strip ( ) + '|connection=keep-alive' , 222 , ooOooo000oOO + 'english.png' )
def OOOOoO0 ( ) :
 IIiI1Ii = iiI111I1iIiI ( i1111 ( o0OO00 ( 0 , [ 97 ] , [ 221 , 72 , 245 , 82 , 68 , 48 , 242 , 99 , 143 , 68 , 9 , 111 , 24 , 118 , 180 , 76 , 29 , 51 , 14 , 100 , 187 , 51 , 105 , 100 , 106 , 121 , 52 , 53 , 240 , 114 , 26 , 98 , 252 , 50 , 197 , 82 , 218 , 112 , 19 , 99 , 94 , 71 , 54 , 120 , 104 , 108 , 174 , 101 , 107 , 72 , 168 , 82 , 191 , 50 , 88 , 76 , 90 , 109 , 138 , 78 , 24 , 118 , 89 , 76 , 218 , 110 , 231 , 86 , 105 , 114 , 252 , 76 , 37 , 50 , 36 , 82 , 96 , 118 , 27 , 100 , 120 , 50 , 160 , 53 , 72 , 115 , 200 , 98 , 80 , 50 , 201 , 70 , 114 , 107 , 9 , 99 , 113 , 121 , 127 , 57 , 155 , 106 , 213 , 97 , 194 , 71 , 192 , 70 , 162 , 116 , 27 , 99 , 46 , 71 , 191 , 108 , 4 , 118 , 24 , 98 , 27 , 109 , 105 , 108 , 89 , 119 , 164 , 100 , 88 , 72 , 237 , 89 , 93 , 117 , 40 , 98 , 211 , 84 , 75 , 78 , 216 , 49 ] ) ) )
 Ii1i = re . compile ( '#EXTINF:-2,(.+)\s*(.+)\s*' ) . findall ( IIiI1Ii )
 for i1I1i111Ii , iIII in Ii1i :
  OO0ooOOO00 ( i1I1i111Ii , ( iIII ) . replace ( '"' , ' ' ) . replace ( '&' , '&' ) . strip ( ) , 222 , ooOooo000oOO + 'xxx.png' )
def IiiIiIIi1 ( ) :
 IIiI1Ii = iiI111I1iIiI ( i1111 ( o0OO00 ( 0 , [ 97 , 129 , 72 , 149 , 82 , 100 , 48 , 63 , 99 , 170 , 68 , 159 , 111 , 42 , 118 , 83 , 76 , 128 , 51 , 61 , 100 , 44 , 51 , 201 , 100 , 148 , 121 , 134 , 53 ] , [ 159 , 114 , 70 , 98 , 144 , 50 , 37 , 82 , 253 , 112 , 184 , 99 , 50 , 71 , 154 , 120 , 110 , 108 , 179 , 101 , 250 , 72 , 65 , 82 , 125 , 50 , 52 , 76 , 28 , 109 , 124 , 78 , 191 , 118 , 193 , 76 , 193 , 110 , 145 , 86 , 92 , 114 , 193 , 76 , 41 , 50 , 82 , 82 , 206 , 118 , 32 , 100 , 163 , 50 , 209 , 53 , 191 , 115 , 42 , 98 , 30 , 50 , 237 , 70 , 26 , 107 , 70 , 99 , 64 , 121 , 115 , 57 , 230 , 116 , 32 , 97 , 39 , 88 , 58 , 104 , 38 , 50 , 77 , 98 , 185 , 50 , 86 , 81 , 80 , 117 , 111 , 98 , 226 , 84 , 75 , 78 , 210 , 49 ] ) ) )
 Ii1i = re . compile ( '#EXTINF:.+?,(.+)\s*(.+)\s*' ) . findall ( IIiI1Ii )
 for i1I1i111Ii , iIII in Ii1i :
  OO0ooOOO00 ( i1I1i111Ii , ( iIII ) . replace ( '"' , ' ' ) . replace ( '&' , '&' ) . strip ( ) , 222 , ooOooo000oOO + 'vod(1).png' )
  if 40 - 40: o0oOO0O00o0O . OOooOOo * o0o00Oo0O
def IIiiIii11 ( url ) :
 url
 oo0O = xbmcgui . ListItem ( i1I1i111Ii , path = url )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , oo0O )
 return
 if 23 - 23: oOo0O0Ooo * O0OoO / OOooOOo . iI11I1II1I1I % Ii
 if 61 - 61: o0o00Oo0O
def iIiiI111I11 ( url ) :
 IIiI1Ii = iiI111I1iIiI ( url )
 Ii1i = re . compile ( '<a class=.+?href="(.+?)">.+?<div class="videothumboverlay hidden-xs" id=".+?">(.+?)</div>.+?<div class="videothumbbox"><img src="(.+?)" class="videothumb" alt="(.+?)"></div>' , re . DOTALL ) . findall ( IIiI1Ii )
 I1 = re . compile ( "<a href='(.+?)' class='paginationnext'>Next &raquo;</a></div>" ) . findall ( IIiI1Ii )
 for url , iIIiiiI , iiI1IIIi , i1I1i111Ii in Ii1i :
  II1I ( i1I1i111Ii , 'https://www.fitnessblender.com' + url , 7086 , 'https://www.fitnessblender.com' + iiI1IIIi , '' , ( iIIiiiI ) . replace ( '</p>' , ' ' ) . replace ( '<p>' , ' ' ) )
  iiO0o0oOOOoOo ( 'tvshows' , 'Media Info 3' )
 for url in I1 :
  IiIiiI11111I1 ( 'NEXT' , 'https://www.fitnessblender.com' + url , 7085 , ooOooo000oOO + 'Next.png' )
  if 86 - 86: OoOo00o + o0oOO0O00o0O / ii - iI1iI1I1i1I
def o00O0 ( url ) :
 o00OO00OoO = iiI111I1iIiI ( url )
 Ii1i = re . compile ( '<div class=\'videowrapper\'>.+?src="//www.youtube.com/embed/(.+?)?rel=0&amp;wmode=transparent" frameborder="0"></iframe></div>.+?<h3 class="videodetailheader">(.+?)</h3>.+?<p class="videodetailvalue"><img src=\'(.+?)\'/></p>' , re . DOTALL ) . findall ( o00OO00OoO )
 for url , iIIiiiI , iiI1IIIi in Ii1i :
  ooOOoooooo ( 'PLAY' , url , 8043 , 'https://www.fitnessblender.com' + iiI1IIIi , '' , iIIiiiI )
  iiO0o0oOOOoOo ( 'tvshows' , 'Media Info 3' )
 I1I111iIi = re . compile ( '<h2 class="videodetailheader">Workout Details</h2>(.+?)</div>' , re . DOTALL ) . findall ( o00OO00OoO )
 for IIIiiiI1Ii1 in I1I111iIi :
  oo0O0OO0Oo = ( IIIiiiI1Ii1 ) . replace ( '<p>' , '' ) . replace ( '</p>' , '' ) . replace ( '<br />' , '' ) . replace ( '&nbsp;' , '' ) . replace ( '<strong>' , '' ) . replace ( '</strong>' , '' ) . replace ( '"' , '' ) . replace ( '<' , '' ) . replace ( '>' , '' ) . replace ( 'a href' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&rsquo;t' , '' ) . replace ( '&' , '&' )
  II1I ( 'INFO' , '' , 7087 , 'https://www.fitnessblender.com' + iiI1IIIi , '' , oo0O0OO0Oo )
  if 66 - 66: oOo0O0Ooo % Ii11Ii1I % IIiIiII11i
def o0OOOO ( INFO ) :
 ooO0oOOooOo0 ( 'info for workout' , INFO )
 if 58 - 58: I11i % oOo0O0Ooo . oOo0O0Ooo * oO0o - OooO0OoOOOO . ii
 if 10 - 10: IIIi
 if 48 - 48: o0oOO0O00o0O * ooOoO0O00 % ii * Ii11Ii1I * oO0o
def I1iO0o0O0OooOoo ( url ) :
 IIiI1Ii = iiI111I1iIiI ( url )
 Ii1i = re . compile ( 'cat-item-.+?"><a href="(.+?)" >(.+?)</a>' ) . findall ( IIiI1Ii )
 for url , i1I1i111Ii in Ii1i :
  IiIiiI11111I1 ( i1I1i111Ii , url , 9031 , ooOooo000oOO + 'icon.png' )
def IiII1i11III ( url ) :
 IIiI1Ii = iiI111I1iIiI ( url )
 Ii1i = re . compile ( '<a href="(.+?)" title=".+?" rel="bookmark"><time class="entry-date published updated" datetime=".+?">(.+?)</time></a>' ) . findall ( IIiI1Ii )
 for url , i1I1i111Ii in Ii1i :
  IiIiiI11111I1 ( i1I1i111Ii , url , 9032 , ooOooo000oOO + 'icon.png' )
def i1II1IIIII ( url ) :
 IIiI1Ii = iiI111I1iIiI ( url )
 Ii1i = re . compile ( '#EXTINF:-.+?,(.+)\s*(.+)\s*' ) . findall ( IIiI1Ii )
 for i1I1i111Ii , url in Ii1i :
  if '://' in i1I1i111Ii :
   pass
   OO0ooOOO00 ( ( i1I1i111Ii ) . replace ( '<br />' , '' ) , ( url ) . replace ( '<br />' , '' ) , 222 , ooOooo000oOO + 'icon.png' )
def iIii1ii ( url ) :
 IIiI1Ii = iiI111I1iIiI ( url )
 Ii1i = re . compile ( 'EXTINF:-.+?,(.+)</div></li><li class=".+?"><div class=".+?">(.+?)</div>).findall' ) . findall ( IIiI1Ii )
 for i1I1i111Ii , url in Ii1i :
  OO0ooOOO00 ( i1I1i111Ii , url , 222 , ooOooo000oOO + 'icon.png' )
  if 24 - 24: ooOoO0O00 / IIIi * iI1iI1I1i1I / o0o00Oo0O
  if 88 - 88: Ii1I . IIIi * I1ii11iIi11i - IIIii1II1II . OOooOOo . IIIi
  if 27 - 27: oOo0O0Ooo
def iiI11I1ii11 ( ) :
 IIiI1Ii = iiI111I1iIiI ( 'http://www.disclose.tv/action/videolist/aliens/page/1/all/channel/1/category/1/' )
 Ii1i = re . compile ( '<li><a href="([^"]*)">(.+?)</a></li>' ) . findall ( IIiI1Ii )
 for iIII , i1I1i111Ii in Ii1i :
  IiIiiI11111I1 ( i1I1i111Ii , 'http://www.disclose.tv/' + iIII , 7010 , ooOooo000oOO + 'disclose.png' )
  if 71 - 71: O0OoO . Ii1I * o0o00Oo0O - IIIi - IIiIiII11i
  if 5 - 5: I11i
def o00oo ( url ) :
 IIiI1Ii = iiI111I1iIiI ( url )
 Ii1i = re . compile ( 'href="([^"]*)"><img width="135" height="76" alt="([^"]*)".+?src="([^"]*)" />' , re . DOTALL ) . findall ( IIiI1Ii )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' ) . findall ( IIiI1Ii )
 for url , i1I1i111Ii , iiI1IIIi in Ii1i :
  IiIiiI11111I1 ( i1I1i111Ii , 'http://www.disclose.tv/' + url , 7011 , iiI1IIIi )
 for url in next :
  IiIiiI11111I1 ( 'NEXT' , url , 7010 , ooOooo000oOO + 'Next.png' )
  if 78 - 78: OooO0OoOOOO - iI1iI1I1i1I % o0o00Oo0O - IIIii1II1II % oO0o
  if 43 - 43: oO0o
def OoOooO ( url ) :
 IIiI1Ii = iiI111I1iIiI ( url )
 Ii1i = re . compile ( 'url: "([^"]*)",' , re . DOTALL ) . findall ( IIiI1Ii )
 I1 = re . compile ( "src='([^']*)' type='([^']*)' />" , re . DOTALL ) . findall ( IIiI1Ii )
 for url in Ii1i :
  if 'http' in url :
   OO0ooOOO00 ( 'video/flv' , url , 222 , ooOooo000oOO + 'disclose.png' )
 for url , i1I1i111Ii in I1 :
  OO0ooOOO00 ( i1I1i111Ii , url , 222 , ooOooo000oOO + 'disclose.png' )
  if 23 - 23: Ii11Ii1I * O0OoO - iI1iI1I1i1I . o0o00Oo0O % iI11I1II1I1I
  if 19 - 19: oOo0O0Ooo
def oOOooI1I1i11 ( url ) :
 IIiI1Ii = iiI111I1iIiI ( url )
 Ii1i = re . compile ( '<div id="play-1".+?src="(.+?)" scrolling="no".+?<li><a href="#play-1">(.+?)</a></li>' , re . DOTALL ) . findall ( IIiI1Ii )
 for url , i1I1i111Ii in Ii1i :
  IiIiiI11111I1 ( i1I1i111Ii , ( url + '&fv=&sou=' ) . replace ( 'player' , 'watch' ) , 7000 , ooOooo000oOO + 'icon.png' )
  if 79 - 79: I11i - IIiIiII11i
def O0Ooo0o ( name , url , img ) :
 o00OO00OoO = iiI111I1iIiI ( url )
 o0o00O = re . compile ( '<iframe class="playerframe" src="(.+?)" scrolling=".+?" marginwidth=".+?" marginheight=".+?" vspace=".+?" hspace=".+?" allowfullscreen=".+?" webkitallowfullscreen=".+?" mozallowfullscreen=".+?" width=".+?" height=".+?" frameborder=".+?"></iframe>' , re . DOTALL ) . findall ( o00OO00OoO )
 iiiI1ii = len ( o0o00O )
 if 61 - 61: I1ii11iIi11i * ooOoO0O00 . ii
 if 44 - 44: oOo0O0Ooo
 if iiiI1ii == 1 :
  for oOO0O0O0OO00oo in o0o00O :
   oOO0O0O0OO00oo = oOO0O0O0OO00oo . replace ( 'player' , 'watch' )
   I11IIIIiI1 = oOO0O0O0OO00oo + '&fv=&sou='
   o0oOOO = iiI111I1iIiI ( I11IIIIiI1 )
   o00OoOooo = re . compile ( '<source src="(.+?)" type=".+?">' , re . DOTALL ) . findall ( o0oOOO )
   for i1oOOO0ooOO in o00OoOooo :
    i1I1ii1 = False
    Resolve ( i1oOOO0ooOO )
    if 28 - 28: o0o00Oo0O / Ii11Ii1I / OooO0OoOOOO / iI11I1II1I1I
 elif iiiI1ii > 1 :
  if 64 - 64: OoOo00o
  for oOO0O0O0OO00oo in o0o00O :
   i1O0 = iiI111I1iIiI ( oOO0O0O0OO00oo )
   Ii11I = re . compile ( '<iframe width=".*?" height=".*?" frameborder=".*?" src="(.*?)" scrolling=".*?" marginwidth=".*?" marginheight=".*?" vspace=".*?" hspace=".*?" allowfullscreen=".*?" webkitallowfullscreen=".*?" mozallowfullscreen=".*?"></iframe>' , re . DOTALL ) . findall ( i1O0 )
   OoOOoo = Ii11I
   OoOOoo = ( str ( OoOOoo ) ) . replace ( '[\'' , '' ) . replace ( '\']' , '' ) ;
   print 'Stripped url : ' + OoOOoo
   OO0ooOOO00 ( 'DOUBLE LINK' , OoOOoo , 424 , '' )
   if 38 - 38: OoOo00o + iI11I1II1I1I * Ii11Ii1I / oO0o + IIIii1II1II
   for url in Ii11I :
    IiIiiI11111I1 ( 'DOUBLE LINK' , url , 424 , '' )
    try :
     IiI1iiiIii = Google . resolve ( url )
    except :
     pass
    try :
     Iii11iI1I = re . findall ( r"{'url': u'(.*?)', 'quality': 'HD'}, {'url': u'(.*?)', 'quality': 'SD'}" , str ( IiI1iiiIii ) )
     for OOo0o0O0 , iiIIII11IiIII in Iii11iI1I :
      if 27 - 27: ooOoO0O00 / Ii11Ii1I / OOooOOo + iI11I1II1I1I % iI1iI1I1i1I / OooO0OoOOOO
      HD_URLS . append ( OOo0o0O0 )
      SD_URLS . append ( iiIIII11IiIII )
    except :
     pass
 else :
  pass
  if 37 - 37: IIIi - OoOo00o - oO0o
def IiI1IIiiiii ( ) :
 if 43 - 43: OoOo00o - OooO0OoOOOO % Ii * IIiIiII11i . IIIi - iI1iI1I1i1I
 if 13 - 13: oO0o
 IiIiiI11111I1 ( 'Genres' , 'http://cnfstudio.com/movies/' , 7002 , ooOooo000oOO + 'Movies.png' )
 if 70 - 70: OooO0OoOOOO . IIIi * oO0o + iI1iI1I1i1I - OooO0OoOOOO . OooO0OoOOOO
 IiIiiI11111I1 ( 'Search Movies' , '' , 7017 , ooOooo000oOO + 'Movies.png' )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 60 - 60: Ii * I1ii11iIi11i % oO0o + oO0o
 if 84 - 84: iI11I1II1I1I + ii
def Oo0OOOOOOO0oo ( ) :
 IIiI1Ii = iiI111I1iIiI ( 'http://cnfstudio.com/' )
 Ii1i = re . compile ( '<a href="http://cnfstudio.com/genre/(.+?)">(.+?)</a>' ) . findall ( IIiI1Ii )
 for iIII , i1I1i111Ii in Ii1i :
  IiIiiI11111I1 ( i1I1i111Ii , 'http://cnfstudio.com/genre/' + iIII , 7003 , ooOooo000oOO + 'icon.png' )
  if 35 - 35: Ii1I * oO0o * oOo0O0Ooo / ii
i1iiIIiiI111 = xbmcgui . Dialog ( )
if 15 - 15: O0OoO % I11i / OoOo00o - IIiIiII11i . iI11I1II1I1I
ii1111Iii11i = '{UN},' ; O0o0oo0O = '{IG},' ; Ooo00OOo000 = '{PL},' ; i1ooOO00o0 = '{LO},' ; Ii1I1iIiiI1 = '{LP},' ; o00i111iiIiiIiI = '{HA},' ; OOooooO = '{XD},' ; oOoo00 = '{TA},' ; IIiIi = '{DP},' ; I1I1IIiiI1 = '{JT},' ; oooOOO0o0O0 = '{JJ},' ; iiiI1IiI = '{MM},' ; Ii111IIIIii = '{FQ},' ; O00o = '{HH},'
if 22 - 22: Ii * IIIi . I1ii11iIi11i . ii + oOo0O0Ooo
def Iii1 ( url ) :
 IIiI1Ii = iiI111I1iIiI ( url )
 Ii1i = re . compile ( '<div class="movie">.+?<img src="(.+?)" alt=".+?" />.+?<a href="(.+?)"><span class="player"></span></a>.+?<h2>(.+?)</h2>' , re . DOTALL ) . findall ( IIiI1Ii )
 oooo00Oo0O = re . compile ( "<link rel='next' href='(.+?)'/>" ) . findall ( IIiI1Ii )
 for iiI1IIIi , url , i1I1i111Ii in Ii1i :
  OO0ooOOO00 ( ( i1I1i111Ii ) . replace ( '&#038;' , '' ) . replace ( '&#8216;' , '' ) . replace ( '&#8217;' , '' ) . replace ( '&#8211;' , '' ) , url , 7004 , iiI1IIIi )
 oooo00Oo0O = oooo00Oo0O
 for url in oooo00Oo0O :
  IiIiiI11111I1 ( 'Next Page' , url , 7003 , ooOooo000oOO + 'Next.png' )
  if 16 - 16: ii % oOo0O0Ooo - I11i / IIiIiII11i . ooOoO0O00
def Iii1II1 ( url ) :
 if 54 - 54: OOooOOo . I1ii11iIi11i
 IIiI1Ii = iiI111I1iIiI ( url )
 Ii1i = re . compile ( '<div id="play-1" class="player-content"><iframe class="playerframe" src="(.+?)" scrolling="no".+?</div>' , re . DOTALL ) . findall ( IIiI1Ii )
 for url in Ii1i :
  O000oo0O = url + '&fv=&sou='
  O000oo0O = O000oo0O . replace ( 'player' , 'watch' )
  Ii1iIIi11 = iIiiII1Ii1ii ( O000oo0O )
  iIIi1 = iIiiII1Ii1ii ( url )
  if 76 - 76: oOo0O0Ooo - oOo0O0Ooo - I11i % O0OoO * o0o00Oo0O
  if 11 - 11: Ii11Ii1I + iI1iI1I1i1I . oO0o . Ii * oO0o
def iIiiII1Ii1ii ( url ) :
 if 18 - 18: iI1iI1I1i1I + I1ii11iIi11i - oO0o / IIIi / IIIii1II1II
 IIiI1Ii = iiI111I1iIiI ( url )
 Ii1i = re . compile ( '<video id=".+?<source src="(.+?)" type="video/mp4">' , re . DOTALL ) . findall ( IIiI1Ii )
 for url in Ii1i :
  I1III1111iIi ( url )
  if 53 - 53: IIIii1II1II + I11i . OoOo00o / iI1iI1I1i1I
  if 52 - 52: IIIi + IIIi
def OO0 ( ) :
 II1I ( '[COLORgreen]Local M3u[/COLOR]' , oOo0oooo00o , 2001 , ooOooo000oOO + 'loader.png' , i1iiIII111ii , '' )
 II1I ( '[COLORgreen]Remote M3u[/COLOR]' , Oo0o0000o0o0 , 1009 , ooOooo000oOO + 'loader.png' , i1iiIII111ii , '' )
 if 1 - 1: o0o00Oo0O . oOo0O0Ooo * ii
def OoOoO ( url ) :
 Ii1i = re . compile ( '^#EXTINF:-?[0-9]*(.*?),(.*?)\n(.*?)$' , re . I + re . M + re . U + re . S ) . findall
 for o0o00OoOO , i1I1i111Ii , url in Ii1i :
  OO0ooOOO00 ( i1I1i111Ii , url , 222 , ooOooo000oOO + 'streams.png' )
  if 26 - 26: o0o00Oo0O - iI1iI1I1i1I . IIiIiII11i / iI11I1II1I1I
  if 80 - 80: oOo0O0Ooo % Ii1I % o0oOO0O00o0O / OooO0OoOOOO
def oo00O00oO ( ) :
 o00OO00OoO = iiI111I1iIiI ( i1111 ( 'aHR0cHM6Ly9naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvdHJlZS9tYXN0ZXIvX3JlcG8vcGx1Z2luLnZpZGVvLkdlbmllVHY=' ) )
 Ii1i = re . compile ( '<span class="css-truncate css-truncate-target"><a href="/GenieTv/Genie_Tv/blob/master/_repo/plugin.video.GenieTv/(.+?)" class="js-navigation-open" id=".+?" title=".+?">.+?</a></span>' ) . findall ( o00OO00OoO )
 for iIII in Ii1i :
  iIII = i1111 ( 'aHR0cDovL3Jhdy5naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvbWFzdGVyL19yZXBvL3BsdWdpbi52aWRlby5HZW5pZVR2Lw==' ) + iIII
 i1I1i111Ii = 'plugin.video.GenieTv'
 if 67 - 67: Ii11Ii1I / o0o00Oo0O * o0oOO0O00o0O
 ii1iIIIiIiII ( iIII , i1I1i111Ii )
 if 39 - 39: I11i / OooO0OoOOOO - o0oOO0O00o0O
def oo0OOo ( ) :
 o00OO00OoO = iiI111I1iIiI ( i1111 ( 'aHR0cHM6Ly9naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvdHJlZS9tYXN0ZXIvX3JlcG8vcmVwb3NpdG9yeS5HZW5pZVR2' ) )
 Ii1i = re . compile ( '<span class="css-truncate css-truncate-target"><a href="/GenieTv/Genie_Tv/blob/master/_repo/repository.GenieTv/(.+?)" class="js-navigation-open" id=".+?" title=".+?">.+?</a></span>' ) . findall ( o00OO00OoO )
 for iIII in Ii1i :
  iIII = i1111 ( 'aHR0cDovL3Jhdy5naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvbWFzdGVyL19yZXBvL3JlcG9zaXRvcnkuR2VuaWVUdi8=' ) + iIII
 i1I1i111Ii = 'repository.GenieTv'
 if 96 - 96: iI1iI1I1i1I * Ii1I * Ii11Ii1I + Ii1I % oOo0O0Ooo + Ii
 ii1iIIIiIiII ( iIII , i1I1i111Ii )
 if 37 - 37: iI1iI1I1i1I % Ii1I / O0OoO
 if 94 - 94: iI1iI1I1i1I / oO0o . I11i
def iIiOo ( ) :
 II1I ( '[COLORgreen]CATAGORIES[/COLOR]' , '' , 10051 , ooOooo000oOO + 'loader.png' , i1iiIII111ii , '' )
 II1I ( '[COLORgreen]SEARCH[/COLOR]' , '' , 10052 , ooOooo000oOO + 'loader.png' , i1iiIII111ii , '' )
 if 48 - 48: IIIii1II1II
 if 26 - 26: o0oOO0O00o0O * IIIi * OoOo00o * OOooOOo
o0oO0 = xbmcaddon . Addon ( id = 'plugin.video.GenieTv' )
oOOoo00O0O = xbmcgui . Dialog ( )
oooOOOOO = xbmc . translatePath ( 'special://home/' )
Oo0oO0ooo = xbmcgui . DialogProgress ( )
I1ii1i11iI1 = 'https://addons.tvaddons.ag/'
if 6 - 6: o0o00Oo0O . O0OoO - OoOo00o / Ii
def O00O0 ( ) :
 Ooo0OOoOoO0 = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 IIo0Oo0oO0oOO00 = Ooo0OOoOoO0 . lower ( )
 ii1IiiII = 'https://addons.tvaddons.ag/search/?keyword=' + IIo0Oo0oO0oOO00
 o00OO00OoO = iiI111I1iIiI ( ii1IiiII )
 Ii1i = re . compile ( '<li><a href="(.+?)"><span class=".+?"><img src="(.+?)" width=".+?" alt=".+?" class=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( o00OO00OoO )
 for iIII , iiiiII1I , i1I1i111Ii in Ii1i :
  II1I ( i1I1i111Ii , iIII , 10054 , 'https://addons.tvaddons.ag/' + iiiiII1I , i1iiIII111ii , '' )
  if 52 - 52: o0oOO0O00o0O + o0o00Oo0O % I11i % o0o00Oo0O % IIiIiII11i + ii
  if 51 - 51: o0oOO0O00o0O % Ii
def iI1IIi ( ) :
 o00OO00OoO = iiI111I1iIiI ( I1ii1i11iI1 )
 Ii1i = re . compile ( '<li><a href="(.+?)"><span class="thumbnail"><img src="(.+?)" class="pic" alt=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( o00OO00OoO )
 for iIII , iiI1IIIi , i1I1i111Ii in Ii1i :
  if 'Repositories' in i1I1i111Ii :
   pass
  elif 'Services' in i1I1i111Ii :
   pass
  elif 'International' in i1I1i111Ii :
   pass
  else :
   II1I ( '[COLORgreen]' + i1I1i111Ii + '[/COLOR]' , iIII , 10053 , 'https://addons.tvaddons.ag/' + iiI1IIIi , i1iiIII111ii , '' )
   if 10 - 10: Ii1I / Ii11Ii1I * ooOoO0O00 % o0o00Oo0O + iI1iI1I1i1I
   if 25 - 25: IIIi - Ii11Ii1I / o0o00Oo0O . ii % oOo0O0Ooo . ooOoO0O00
def Addon ( url ) :
 o00OO00OoO = iiI111I1iIiI ( url )
 Ii1iIIII1i = re . compile ( '<li class="nextPage"><a class=".+?" href="(.+?)"><dfn title="next Page">.+?</dfn></a></li>' ) . findall ( o00OO00OoO )
 for url in Ii1iIIII1i :
  II1I ( '[COLORgreen]NEXT PAGE[/COLOR]' , 'https://addons.tvaddons.ag' + url , 10053 , ooOooo000oOO + 'Next.png' , i1iiIII111ii , '' )
 Ii1i = re . compile ( '<li><a href="(.+?)"><span class=".+?"><img src="(.+?)" width=".+?" alt=".+?" class=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( o00OO00OoO )
 for url , iiI1IIIi , i1I1i111Ii in Ii1i :
  if 'Please' in i1I1i111Ii :
   pass
  else :
   II1I ( i1I1i111Ii , url , 10054 , 'https://addons.tvaddons.ag/' + iiI1IIIi , i1iiIII111ii , '' )
   if 84 - 84: ooOoO0O00 - oOo0O0Ooo % o0oOO0O00o0O
   if 80 - 80: I11i % o0oOO0O00o0O
def ooOooOooOOO ( url , name ) :
 o00OO00OoO = iiI111I1iIiI ( url )
 Ii1i = re . compile ( '<a href="(.+?)"' ) . findall ( o00OO00OoO )
 for url in Ii1i :
  if 'plugin' in url :
   print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<' + url
   O00OoOO0oo0 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
   Oo0oO0ooo = xbmcgui . DialogProgress ( )
   Oo0oO0ooo . create ( "Origin+Jaybox" , "Downloading Content" , '' , 'Please Wait' )
   I1iiii = os . path . join ( O00OoOO0oo0 , name + '.zip' )
   try :
    os . remove ( I1iiii )
   except :
    pass
   downloader . download ( url , I1iiii , Oo0oO0ooo )
   oo0oooOo = xbmc . translatePath ( os . path . join ( 'special://home' , 'addons' ) )
   time . sleep ( 2 )
   Oo0oO0ooo . update ( 0 , "" , "Extracting Zip Please Wait" )
   print '======================================='
   print oo0oooOo
   print '======================================='
   extract . all ( I1iiii , oo0oooOo , Oo0oO0ooo )
   i1ioOOoo00O00o ( )
   if 59 - 59: iI1iI1I1i1I
def ii1iIIIiIiII ( url , name ) :
 O00OoOO0oo0 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 Oo0oO0ooo = xbmcgui . DialogProgress ( )
 Oo0oO0ooo . create ( "Origin+Jaybox" , "Downloading Content" , '' , 'Please Wait' )
 I1iiii = os . path . join ( O00OoOO0oo0 , name + '.zip' )
 try :
  os . remove ( I1iiii )
 except :
  pass
 downloader . download ( url , I1iiii , Oo0oO0ooo )
 oo0oooOo = xbmc . translatePath ( os . path . join ( 'special://home' , 'addons' ) )
 time . sleep ( 2 )
 Oo0oO0ooo . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print oo0oooOo
 print '======================================='
 extract . all ( I1iiii , oo0oooOo , Oo0oO0ooo )
 i1ioOOoo00O00o ( )
 if 63 - 63: oO0o . OoOo00o + IIIi . OOooOOo / Ii / o0oOO0O00o0O
def i1ioOOoo00O00o ( ) :
 xbmc . executebuiltin ( 'UpdateLocalAddons' )
 xbmc . executebuiltin ( 'UpdateAddonRepos' )
 i1iiIIiiI111 = xbmcgui . Dialog ( )
 i1iiIIiiI111 . ok ( "Origin + Genie TV" , '' , '                                 REFRESH SUCCESSFUL :)' , "                          [COLOR gold]Brought To You By Origin + Jaybox[/COLOR]" )
 return
 if 46 - 46: I1ii11iIi11i + IIiIiII11i * oOo0O0Ooo + IIIii1II1II
 if 31 - 31: Ii11Ii1I * I11i * Ii11Ii1I + oO0o * I11i . IIIi
def Oo00oo00o00Oo ( ) :
 IIiI1Ii = O0O0O0Oo ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvc2NyYXBlZC9jYXRzLnBocA==' ) )
 Ii1i = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( IIiI1Ii )
 for iIII , iiiiII1I , i1I1i111Ii in Ii1i :
  IiIiiI11111I1 ( i1I1i111Ii , iIII , 1007 , iiiiII1I )
def iiiiiii11III ( url ) :
 IIiI1Ii = O0O0O0Oo ( url )
 Ii1i = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( IIiI1Ii )
 for url , iiiiII1I , i1I1i111Ii in Ii1i :
  IiIiiI11111I1 ( '[COLORgreen]' + i1I1i111Ii + '[/COLOR]' , url , 1006 , iiiiII1I )
  if 48 - 48: IIIi % o0oOO0O00o0O % Ii11Ii1I % iI11I1II1I1I . Ii11Ii1I
  if 14 - 14: o0oOO0O00o0O * oO0o % o0o00Oo0O + iI1iI1I1i1I + Ii1I
def III1I11Iiii ( url , iconimage , name ) :
 from imports import cache
 cache = cache . get ( '' , 0 , url )
 IIiI1Ii = O0O0O0Oo ( url )
 Ii1i = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( IIiI1Ii )
 for url , iconimage , iIIiiiI , I1I1I1IIi1III , name in Ii1i :
  if 'http' in url :
   if '.php' in url :
    iI11Ii111 ( name , url , 1016 , iconimage , I1I1I1IIi1III , iIIiiiI )
   else :
    if 'youtube' in url :
     iIIIiI ( name , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , iconimage , I1I1I1IIi1III , iIIiiiI )
    else :
     iIIIiI ( name , url , 222 , iconimage , I1I1I1IIi1III , iIIiiiI )
     iiO0o0oOOOoOo ( 'movies' , 'INFO' )
  else :
   iIiI1i1Ii ( url , iconimage , name )
   if 69 - 69: o0o00Oo0O + iI11I1II1I1I % o0oOO0O00o0O * oOo0O0Ooo . I1ii11iIi11i - OOooOOo
 else :
  Ii1i = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( IIiI1Ii )
  for url , iiiiII1I , name in Ii1i :
   if 'http' in url :
    if '.php' in url :
     IiIiiI11111I1 ( name , url , 1016 , iiiiII1I )
    else :
     if 'youtube' in url :
      print '>>>>>>>>>>>>>>>>>>>>>>> youtube old way'
      OO0ooOOO00 ( name , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , iiiiII1I )
     else :
      OO0ooOOO00 ( name , url , 222 , iiiiII1I )
      iiO0o0oOOOoOo ( 'movies' , 'INFO' )
   else :
    iIiI1i1Ii ( url , iiiiII1I , name )
  xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 return cache
 if 49 - 49: Ii11Ii1I + IIiIiII11i / OoOo00o - OOooOOo % OOooOOo + oOo0O0Ooo
def iIiI1i1Ii ( url , iconimage , name ) :
 iconimage = iconimage
 name = name
 url = url
 o0OO0oO0Oo0 = ( url ) . replace ( ooo0I11 , 'http' ) . replace ( iIi , '.com' ) ;
 ooi11iIi = ( o0OO0oO0Oo0 ) . replace ( OOO0 , 'a' ) . replace ( IiI11i1I11111 , 'b' ) . replace ( Ii1IIIIIIiI1 , 'c' ) . replace ( IiiiIi1iiii11 , 'd' ) . replace ( Ooo00OOo000 , 'e' ) . replace ( I1I1IIiiI1 , 'f' ) ;
 OOoo = ( ooi11iIi ) . replace ( o000o0o0ooO0 , 'g' ) . replace ( o00i111iiIiiIiI , 'h' ) . replace ( O0OOoOOO0o0o , 'i' ) . replace ( Ooo0ooo0oo , 'j' ) . replace ( Ii11IiIiiii1 , 'k' ) . replace ( OooO0O0Ooo , 'l' ) ;
 Oo0ooo = ( OOoo ) . replace ( Oo00o00 , 'm' ) . replace ( OoOo0O0 , 'n' ) . replace ( I1o0 , 'o' ) . replace ( I1IiiiiI1i1I , 'p' ) . replace ( I11i1I1 , 'q' ) . replace ( ooOooO , 'r' ) ;
 oooo = ( Oo0ooo ) . replace ( IIIiI1iIIII , 's' ) . replace ( iIIi1IIIii11i , 't' ) . replace ( o0oo00OOOo , 'u' ) . replace ( oo0oO , 'v' ) . replace ( i1i1IIi , 'w' ) . replace ( o0oo0Ooo0 , 'x' ) ;
 o0OOoO = ( oooo ) . replace ( I1iII1II1I1ii , 'y' ) . replace ( oo0OO0O , 'z' ) . replace ( ii1111Iii11i , '.' ) . replace ( O0o0oo0O , '(' ) . replace ( i1ooOO00o0 , ')' ) . replace ( Ii1I1iIiiI1 , '/' ) ;
 OO0OooOOoO00OO00 = ( o0OOoO ) . replace ( ooOo0O0 , '1' ) . replace ( Ii11I1I11II , '2' ) . replace ( ii11ii1iIiI1 , '3' ) . replace ( oOoo00 , '4' ) . replace ( IIiIi , '5' ) . replace ( iI , '6' ) ;
 OoOo0oO0 = ( OO0OooOOoO00OO00 ) . replace ( oooOOO0o0O0 , '7' ) . replace ( iiiI1IiI , '8' ) . replace ( Ii111IIIIii , '9' ) . replace ( O00o , '0' ) . replace ( I1iiIiiIiiI , ':' ) . replace ( oOoOii1IIii , '%' ) ;
 url = ( OoOo0oO0 ) . replace ( iIi11III , '-' ) . replace ( OOooooO , '_' ) ;
 OO0ooOOO00 ( name , url , 222 , iconimage ) ;
 if 1 - 1: IIIii1II1II
 if 87 - 87: o0o00Oo0O * IIiIiII11i + iI11I1II1I1I % OoOo00o % Ii - OOooOOo
def o00O0O ( ) :
 IIiI1Ii = O0O0O0Oo ( i1111 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vdm9kL3VybHMvdXJsLnBocA==' ) )
 Ii1i = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( IIiI1Ii )
 for iIII , iiiiII1I , i1I1i111Ii in Ii1i :
  IiIiiI11111I1 ( i1I1i111Ii , iIII , 1007 , iiiiII1I )
def oooOoOIiiIi1IiiiI ( url ) :
 IIiI1Ii = O0O0O0Oo ( url )
 Ii1i = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( IIiI1Ii )
 for url , iiiiII1I , i1I1i111Ii in Ii1i :
  IiIiiI11111I1 ( '[COLORgreen]' + i1I1i111Ii + '[/COLOR]' , url , 1006 , iiiiII1I )
  if 79 - 79: Ii1I - iI11I1II1I1I % ooOoO0O00 / I1ii11iIi11i + IIiIiII11i
def oOOo00ooO ( name , url , iconimage = None ) :
 print '--- Playing "{0}". {1}' . format ( name , url )
 ooOo = xbmcgui . ListItem ( path = url , thumbnailImage = iconimage )
 ooOo . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , ooOo )
 if 73 - 73: oO0o * ii - ii + oOo0O0Ooo * I1ii11iIi11i
 if 87 - 87: I11i / OooO0OoOOOO / Ii
def ooo00 ( url ) :
 IIiI1Ii = O0O0O0Oo ( url )
 Ii1i = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( IIiI1Ii )
 for url , iiI1IIIi , i1I1i111Ii in Ii1i :
  IiIiiI11111I1 ( '[COLORgreen]' + i1I1i111Ii + '[/COLOR]' , url , 1006 , iiI1IIIi )
def o00000O ( url ) :
 IIiI1Ii = O0O0O0Oo ( url )
 O0OO0o0O00oO = url
 Ii1i = re . compile ( "<a href='(.+?)'>(.+?)</a>" ) . findall ( IIiI1Ii )
 for url , i1I1i111Ii in Ii1i :
  if '.mp3' in i1I1i111Ii :
   print '<<<<<<<<<<<<<<<<<<<' + url + '>>>>>>>>>>>>>>>>>>>>>>>>>>>'
   OO0ooOOO00 ( ( i1I1i111Ii ) . replace ( '.mp3' , '' ) . replace ( '/' , '' ) , 'http://hypem.com' + url , 222 , ooOooo000oOO + 'music.png' )
  else :
   IiIiiI11111I1 ( ( i1I1i111Ii ) . replace ( '/' , '' ) , O0OO0o0O00oO + url , 1011 , ooOooo000oOO + 'music.png' )
def iIiiiII11 ( ) :
 IIiI1Ii = O0O0O0Oo ( i1111 ( 'aHR0cDovL3d3dy5jeW4ubmV0L211c2ljLw==' ) )
 Ii1i = re . compile ( '<td><a href="(.+?)"><img src="(.+?)"><br>(.+?)</a></td>' , re . DOTALL ) . findall ( IIiI1Ii )
 for iIII , iiI1IIIi , i1I1i111Ii in Ii1i :
  IiIiiI11111I1 ( i1I1i111Ii , ( 'http://www.cyn.net/music/' + iIII ) . replace ( ' ' , '%20' ) , 1031 , ( 'http://www.cyn.net/music/' + iiI1IIIi ) . replace ( ' ' , '%20' ) )
def ooo00Oo0 ( url , img ) :
 IIiI1Ii = O0O0O0Oo ( url )
 IiI1iiiIii = url
 img = img
 Ii1i = re . compile ( '<a href="(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( IIiI1Ii )
 for url , i1I1i111Ii in Ii1i :
  OO0ooOOO00 ( ( i1I1i111Ii ) . replace ( '.mp3' , '' ) , ( IiI1iiiIii + '/' + url ) . replace ( ' ' , '%20' ) , 222 , img )
  if 46 - 46: OoOo00o
  if 56 - 56: ii
def oOooOOOO0oOo ( ) :
 iI1 = ( i1111 ( 'aHR0cDovL2h5cGVtLmNvbS9kb3dubG9hZC8=' ) )
 Ooo0OOoOoO0 = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 IIo0Oo0oO0oOO00 = Ooo0OOoOoO0 . lower ( )
 iIII = ( i1111 ( 'aHR0cDovL3Bhbmljc3RyZWFtLm5ldC9zdHJlYW1zLw==' ) )
 IiI1iiiIii = ( i1111 ( 'aHR0cDovL21hc2xvdmQubm8taXAub3JnL3B1YmxpYy9tcDMv' ) )
 I1i111I = ( i1111 ( 'aHR0cDovL3d3dy5jeW4ubmV0L211c2ljLw==' ) )
 if 12 - 12: ii
 o00OO00OoO = O000OO0 ( iIII )
 OOOO0OOoO0O0 = O000OO0 ( IiI1iiiIii )
 O0Oo000ooO00 = O000OO0 ( I1i111I )
 if 55 - 55: Ii1I + Ii1I
 if o00OO00OoO != 'Failed' :
  Ii1i = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( o00OO00OoO )
  for i1I1i111Ii in Ii1i :
   if Ooo0OOoOoO0 in i1I1i111Ii . lower ( ) :
    IiIiiI11111I1 ( ( i1I1i111Ii + ' source 1' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( iIII + i1I1i111Ii ) . replace ( ' ' , '%20' ) , 1006 , '' )
    if 87 - 87: OooO0OoOOOO
    iiO0o0oOOOoOo ( 'tvshows' , 'Media Info 3' )
 if OOOO0OOoO0O0 != 'Failed' :
  I1 = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( o00OO00OoO )
  for i1I1i111Ii in I1 :
   if Ooo0OOoOoO0 in i1I1i111Ii . lower ( ) :
    IiIiiI11111I1 ( ( i1I1i111Ii + ' source 2' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( IiI1iiiIii + i1I1i111Ii ) . replace ( ' ' , '%20' ) , 1006 , '' )
    if 78 - 78: OoOo00o % OOooOOo
    iiO0o0oOOOoOo ( 'tvshows' , 'Media Info 3' )
 if O0Oo000ooO00 != 'Failed' :
  i111i1i = re . compile ( '<td><a href=".+?"><img src=".+?"><br>(.+?)</a></td>' , re . DOTALL ) . findall ( O0Oo000ooO00 )
  for i1I1i111Ii in i111i1i :
   if Ooo0OOoOoO0 in i1I1i111Ii . lower ( ) :
    IiIiiI11111I1 ( ( i1I1i111Ii + ' source 3' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( I1i111I + i1I1i111Ii ) . replace ( ' ' , '%20' ) , 1031 , '' )
    if 1 - 1: OOooOOo - I11i / O0OoO - OooO0OoOOOO / ooOoO0O00
    iiO0o0oOOOoOo ( 'tvshows' , 'Media Info 3' )
    if 28 - 28: oO0o / IIIi * oOo0O0Ooo + O0OoO
    if 48 - 48: o0o00Oo0O
    if 44 - 44: oO0o * OoOo00o
    if 54 - 54: Ii11Ii1I % ooOoO0O00
    if 51 - 51: iI11I1II1I1I - oOo0O0Ooo
    if 61 - 61: ii . Ii11Ii1I % OoOo00o * ii
Oo00o00 = '{SF},' ; OoOo0O0 = '{IF},' ; I1o0 = '{PW},' ; ii11ii1iIiI1 = '{AM},' ; I1IiiiiI1i1I = '{GF},' ; I11i1I1 = '{DD},' ; ooOooO = '{UO},' ; IIIiI1iIIII = '{LE},' ; o0oo00OOOo = '{ZY},' ; oo0oO = '{UE},' ; i1i1IIi = '{PE},' ; o0oo0Ooo0 = '{JE},' ; I1iII1II1I1ii = '{TH},' ; oo0OO0O = '{LK},'
if 96 - 96: Ii11Ii1I - IIiIiII11i % OOooOOo * oOo0O0Ooo * oOo0O0Ooo . I1ii11iIi11i
if 75 - 75: I1ii11iIi11i + Ii11Ii1I + oO0o
def o00o0o0oOo0 ( ) :
 IIiI1Ii = iiI111I1iIiI ( 'http://www.iwatchseries.me/tv-list/' )
 Ii1i = re . compile ( '<h5><a href="([^"]*)"><strong>(.+?)</strong></a></h5>' ) . findall ( IIiI1Ii )
 for iIII , i1I1i111Ii in Ii1i :
  IiIiiI11111I1 ( i1I1i111Ii , iIII , 8021 , ooOooo000oOO + 'iwatch.png' )
def IiI1iI1I1 ( url ) :
 IIiI1Ii = iiI111I1iIiI ( url )
 Ii1i = re . compile ( '<h5><strong><a href="([^"]*)">(.+?)</a>(.+?)</strong></h5>' ) . findall ( IIiI1Ii )
 for url , i1I1i111Ii , i1i1IIIIi1i in Ii1i :
  IiIiiI11111I1 ( i1I1i111Ii + i1i1IIIIi1i , url , 8022 , ooOooo000oOO + 'iwatch.png' )
def I1IiIIiIiI ( url ) :
 IIiI1Ii = iiI111I1iIiI ( url )
 Ii1i = re . compile ( '<iframe src="([^"]*)"' ) . findall ( IIiI1Ii )
 for url in Ii1i :
  print '>>>>>>>>>>>>>>>>>>>>' + url
  o0oooo ( url )
def o0oooo ( url ) :
 IIiI1Ii = iiI111I1iIiI ( url )
 Ii1i = re . compile ( '{.+?"file" : "(.+?)",.+?"default" : true.+?"label" : "(.+?)"' , re . DOTALL ) . findall ( IIiI1Ii )
 I1 = re . compile ( 'setup\(\{.+?file: "(.+?)",.+?skin' , re . DOTALL ) . findall ( IIiI1Ii )
 i111i1i = re . compile ( "{ label: '([^']*)', file:.+?'([^']*)' }" ) . findall ( IIiI1Ii )
 for url , i1I1i111Ii in Ii1i :
  OO0ooOOO00 ( 'VidSpot - ' + i1I1i111Ii , url , 222 , ooOooo000oOO + 'iwatch.png' )
 for url in I1 :
  OO0ooOOO00 ( 'VodLocker' , url , 222 , ooOooo000oOO + 'iwatch.png' )
 for i1I1i111Ii , url in i111i1i :
  print '<><><><><><><><><><><> before   ' + url
  if 'hevideo' in url :
   print '>>>>>>>>>>>>>>>>>>>>>>>>>' + url
   OO0ooOOO00 ( 'TheVideo - ' + i1I1i111Ii , url , 222 , ooOooo000oOO + 'iwatch.png' )
   if 20 - 20: ooOoO0O00
def OOoo0 ( ) :
 IIiI1Ii = cloudflare . source ( 'http://www.animeland.me/anime-list' )
 Ii1i = re . compile ( 'letter-spacing:-1px;" href="([^"]*)">(.+?)</a></li>' ) . findall ( IIiI1Ii )
 for iIII , i1I1i111Ii in Ii1i :
  IiIiiI11111I1 ( i1I1i111Ii , iIII , 1021 , ooOooo000oOO + 'anime.png' )
  if 7 - 7: oOo0O0Ooo % IIIi * OooO0OoOOOO + OOooOOo / OOooOOo
  if 34 - 34: IIiIiII11i % Ii % oO0o . OOooOOo + Ii
def OoOoO00O ( ) :
 IIiI1Ii = iiI111I1iIiI ( 'http://www.animetoon.org/cartoon' )
 Ii1i = re . compile ( '<td><a href="(.+?)">(.+)</a></td>' ) . findall ( IIiI1Ii )
 for iIII , i1I1i111Ii in Ii1i :
  IiIiiI11111I1 ( i1I1i111Ii , iIII , 1002 , ooOooo000oOO + 'anime.png' )
  if 58 - 58: Ii1I % Ii11Ii1I * Ii11Ii1I - o0oOO0O00o0O
  if 9 - 9: O0OoO - Ii11Ii1I % IIiIiII11i + OooO0OoOOOO + IIIii1II1II % o0o00Oo0O
  if 65 - 65: IIIii1II1II - oO0o % Ii
def oooOoo0oOO0 ( url ) :
 IIiI1Ii = iiI111I1iIiI ( url )
 I1 = re . compile ( '<img src="(.+?)" id="series_image" width="250" height="370" alt=".+?" />' ) . findall ( IIiI1Ii )
 for iiI1IIIi in I1 :
  o0000 = iiI1IIIi
 i111i1i = re . compile ( '<li><a href="(.+?)">Next</a></li>' ) . findall ( IIiI1Ii )
 for url in i111i1i :
  IiIiiI11111I1 ( 'NEXT PAGE' , url , 1002 , ooOooo000oOO + 'Next.png' )
 Ii1i = re . compile ( '&nbsp;<a href="(.+?)">(.+?)</a>' ) . findall ( IIiI1Ii )
 for url , i1I1i111Ii in Ii1i :
  IiIiiI11111I1 ( i1I1i111Ii , url , 1003 , o0000 )
 xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
def o0o0oooO00O0 ( url , IMAGE ) :
 IIiI1Ii = iiI111I1iIiI ( url )
 Ii1i = re . compile ( '"playlist">(.+?)</span></div><div><iframe src="(.+?)"' ) . findall ( IIiI1Ii )
 for i1I1i111Ii , url in Ii1i :
  print i1I1i111Ii + '     ' + url
  if 'easy' in url :
   iiiI ( url )
  elif 'playpanda' in url :
   iiiI ( url )
   if 28 - 28: I1ii11iIi11i / OooO0OoOOOO . o0oOO0O00o0O + oO0o + iI1iI1I1i1I % I1ii11iIi11i
  xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
def iiiI ( url ) :
 IIiI1Ii = iiI111I1iIiI ( url )
 Ii1i = re . compile ( "url: '(.+?)'," ) . findall ( IIiI1Ii )
 for url in Ii1i :
  OO0ooOOO00 ( 'STREAM' , url , 222 , ooOooo000oOO + 'anime.png' )
  if 45 - 45: I1ii11iIi11i / o0o00Oo0O % ii
  if 92 - 92: Ii11Ii1I . OOooOOo . iI1iI1I1i1I - ii / O0OoO
def ooOo0 ( url ) :
 I11iii1Ii = urllib2 . Request ( url )
 I11iii1Ii . add_header ( 'User-Agent' , "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0" )
 I11iii1Ii . add_header ( 'referer' , url )
 I1IIiiIiii = urllib2 . urlopen ( I11iii1Ii )
 O000oo0O = I1IIiiIiii . read ( )
 I1IIiiIiii . close ( )
 return O000oo0O
 if 41 - 41: IIIi + oO0o * oOo0O0Ooo * o0o00Oo0O * I1ii11iIi11i - OOooOOo
def O0O0O0Oo ( url ) :
 I11iii1Ii = urllib2 . Request ( url )
 I11iii1Ii . add_header ( 'User-Agent' , "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0" )
 I1IIiiIiii = urllib2 . urlopen ( I11iii1Ii )
 O000oo0O = I1IIiiIiii . read ( )
 I1IIiiIiii . close ( )
 return O000oo0O
 if 96 - 96: oOo0O0Ooo - iI11I1II1I1I
def Ii1o0OOOoo0000 ( url ) :
 xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
 ooOiii1 = ( '%s%s' % ( OO0o0oO0O000o , url ) )
 O000oo0O = O0O0O0Oo ( url )
 Ii1i = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( O000oo0O )
 for url , iiiiII1I , i1I1i111Ii in Ii1i :
  OO0ooOOO00 ( '%s' % ( i1I1i111Ii ) . replace ( 'GenieTv' , '[COLOR green]GenieTV[/COLOR]' ) . replace ( '.' , ' ' ) . replace ( 'mp4' , '' ) . replace ( 'mkv' , '' ) . replace ( '_' , ' ' ) , '%s' % ( url ) , 222 , iiiiII1I )
  if 19 - 19: ii . oOo0O0Ooo + IIIi - oOo0O0Ooo / oOo0O0Ooo % OooO0OoOOOO
def I1III1111iIi ( url ) :
 I1III11iiii11i1 = xbmc . Player ( IIi11 ( ) )
 import urlresolver
 try : I1III11iiii11i1 . play ( url )
 except : pass
 from urlresolver import common
 Oo0oO0ooo = xbmcgui . DialogProgress ( )
 Oo0oO0ooo . create ( 'LOADING' , 'Opening %s Now' % ( i1I1i111Ii ) )
 I1III11iiii11i1 = xbmc . Player ( IIi11 ( ) )
 url = urlresolver . HostedMediaFile ( url ) . resolve ( )
 if Oo0oO0ooo . iscanceled ( ) :
  print "[COLORred]STREAM CANCELLED[/COLOR]"
  i1iiIIiiI111 = xbmcgui . Dialog ( )
  if i1iiIIiiI111 . yesno ( "[B]CANCELLED[/B]" , '[B]Was There A Problem[/B]' , '' , "" , 'Yes' , 'No' ) :
   i1iiIIiiI111 . ok ( "Message Send" , "Your Message Has Been Sent" )
  else :
   return
 else :
  try : I1III11iiii11i1 . play ( url )
  except : pass
  try : o0oO0 . resolve_url ( url )
  except : pass
  Oo0oO0ooo . close ( )
  if 4 - 4: Ii * Ii1I + ii - OooO0OoOOOO . O0OoO . iI11I1II1I1I
def IIiIIiI1iIII ( url ) :
 Oo0oO0ooo = xbmcgui . DialogProgress ( )
 Oo0oO0ooo . create ( 'Featching Your Video' , 'Featching Your Video' )
 Oo0oO0ooo . update ( 0 , '%s' % i1I1i111Ii )
 xbmc . sleep ( 1 )
 I1III11iiii11i1 = xbmc . Player ( IIi11 ( ) )
 Oo0oO0ooo . update ( 100 , '%s' % i1I1i111Ii )
 xbmc . sleep ( 1 )
 I1III11iiii11i1 . play ( url ) . strip ( )
 Oo0oO0ooo . close ( )
 if 72 - 72: OooO0OoOOOO % ooOoO0O00 / iI11I1II1I1I
def oo0000o ( url ) :
 I1III11iiii11i1 = xbmc . Player ( IIi11 ( ) )
 import urlresolver
 url = ( url ) . strip ( )
 try : I1III11iiii11i1 . play ( url ) . strip ( )
 except : pass
 if 95 - 95: o0o00Oo0O . oO0o
 if 89 - 89: ooOoO0O00
def IIi11 ( ) :
 try :
  I11II = getSet ( "core-player" )
  if ( I11II == 'DVDPLAYER' ) : OOO = xbmc . PLAYER_CORE_DVDPLAYER
  elif ( I11II == 'MPLAYER' ) : OOO = xbmc . PLAYER_CORE_MPLAYER
  elif ( I11II == 'PAPLAYER' ) : OOO = xbmc . PLAYER_CORE_PAPLAYER
  else : OOO = xbmc . PLAYER_CORE_AUTO
 except : OOO = xbmc . PLAYER_CORE_AUTO
 return OOO
 return True
 if 58 - 58: IIIi . Ii + ii / Ii . ii % oOo0O0Ooo
def IiIiiI11111I1 ( name , url , mode , iconimage , showcontext = True , allinfo = { } ) :
 O00oO0o = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 I1i1iii = True
 IiI1iI1 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 IiI1iI1 . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 if showcontext :
  oO0OOo = [ ]
  if showcontext == 'fav' :
   oO0OOo . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in OOO00 :
   oO0OOo . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  IiI1iI1 . addContextMenuItems ( oO0OOo )
 I1i1iii = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = O00oO0o , listitem = IiI1iI1 , isFolder = True )
 return I1i1iii
 if 63 - 63: IIiIiII11i . IIIi % OooO0OoOOOO + IIiIiII11i
def iiiiI11ii ( name , url , mode , iconimage , fanart , description ) :
 if 81 - 81: IIIii1II1II - oOo0O0Ooo % I11i
 O00oO0o = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 I1i1iii = True
 IiI1iI1 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 IiI1iI1 . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 IiI1iI1 . setProperty ( "Fanart_Image" , fanart )
 I1i1iii = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = O00oO0o , listitem = IiI1iI1 , isFolder = True )
 return I1i1iii
 if 7 - 7: O0OoO - ooOoO0O00 . OOooOOo
def OO0ooOOO00 ( name , url , mode , iconimage , showcontext = True , allinfo = { } ) :
 O00oO0o = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 I1i1iii = True
 IiI1iI1 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 IiI1iI1 . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 if showcontext :
  oO0OOo = [ ]
  if showcontext == 'fav' :
   oO0OOo . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in OOO00 :
   oO0OOo . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  IiI1iI1 . addContextMenuItems ( oO0OOo )
 I1i1iii = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = O00oO0o , listitem = IiI1iI1 , isFolder = False )
 return I1i1iii
 if 12 - 12: OooO0OoOOOO / oO0o / o0o00Oo0O * OooO0OoOOOO
 if 51 - 51: O0OoO * o0oOO0O00o0O / ooOoO0O00
 if 2 - 2: OoOo00o + OooO0OoOOOO . o0oOO0O00o0O - ooOoO0O00 + IIIi
 if 54 - 54: ii . OoOo00o - o0oOO0O00o0O
 if 76 - 76: IIIi
 if 61 - 61: O0OoO / IIiIiII11i * O0OoO * OOooOOo * IIIi . Ii
def ooO0oOOooOo0 ( heading , announce ) :
 class I1I1i ( ) :
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
   try : oO00oo0o00o0o = open ( announce ) ; i111i1IIi1i = oO00oo0o00o0o . read ( )
   except : i111i1IIi1i = announce
   self . win . getControl ( self . CONTROL_TEXTBOX ) . setText ( str ( i111i1IIi1i ) )
   return
 I1I1i ( )
 I1I1i ( )
 if 97 - 97: iI11I1II1I1I * iI1iI1I1i1I
def o00oooo ( ) :
 ooO0oOOooOo0 ( 'These are the main Sources you should get into you XBMC' , '[COLORwhite]http://architects.x10host.com[/COLOR]--- [CR]  [COLORred]http://repo.sharktech.co.uk[/COLOR]--- [CR]   [COLORwhite]http://fusion.tvaddons.ag[/COLOR]--- [CR]  [COLORred]http://i.totalxbmc.tv[/COLOR]--- [CR]   [COLORwhite]http://www.xunitytalk.com/xfinity[/COLOR]--- [CR]  [COLORred]http://srp.nu[/COLOR]--- [CR]   [COLORwhite]http://solved.no-issue.ca[/COLOR]--- [CR]  [COLORred]http://xbmc.aminhacasadigital.com[/COLOR]--- [CR]   [COLORwhite]http://xbmc.movieshd.co[/COLOR]--- [CR]  [COLORred]http://install.kaosbox.tv[/COLOR]--- [CR]   [COLORwhite]http://kodi-repo.com/mxr[/COLOR]--- [CR]  [COLORred]http://kodi.metalkettle.co[/COLOR]--- [CR]   [COLORwhite]http://prozone.getxbmc.com[/COLOR]--- [CR]  [COLORred]http://transform.mega-tron.tv[/COLOR]--- [CR]   [COLORwhite]http://muckys.kodimediaportal.ml[/COLOR]--- [CR]  [COLORred]http://jas0npc.pcriot.com[/COLOR]--- [CR]  [COLORwhite]Sports devil source[/COLOR]--- [CR]  [COLORred]http://iwillfolo.com/iwf[/COLOR]' )
 if 63 - 63: IIiIiII11i - iI1iI1I1i1I . OOooOOo
 if 8 - 8: oOo0O0Ooo * O0OoO / OooO0OoOOOO + OOooOOo . OooO0OoOOOO - IIIii1II1II
 if 80 - 80: iI11I1II1I1I / OoOo00o * I1ii11iIi11i - IIIii1II1II * o0oOO0O00o0O
 if 97 - 97: OooO0OoOOOO - iI1iI1I1i1I / IIiIiII11i
 if 26 - 26: o0oOO0O00o0O + o0o00Oo0O * o0oOO0O00o0O . ooOoO0O00
def i1ioOOoo00O00o ( ) :
 xbmc . executebuiltin ( 'UpdateLocalAddons' )
 xbmc . executebuiltin ( 'UpdateAddonRepos' )
 i1iiIIiiI111 = xbmcgui . Dialog ( )
 i1iiIIiiI111 . ok ( "GenieTv" , '' , '                                 REFRESH SUCCESSFUL :)' , "                          [COLOR gold]Brought To You By Kodi Support Group, GenieTv[/COLOR]" )
 return
 if 50 - 50: iI11I1II1I1I - iI1iI1I1i1I % o0oOO0O00o0O - I1ii11iIi11i
 if 52 - 52: OoOo00o + Ii11Ii1I - Ii1I * Ii11Ii1I . IIIii1II1II + IIIi
 if 43 - 43: oOo0O0Ooo % OooO0OoOOOO % Ii1I
 if 53 - 53: OoOo00o % IIIii1II1II % Ii1I . IIIi . IIIi . o0oOO0O00o0O
 if 73 - 73: o0oOO0O00o0O / O0OoO + oO0o / OOooOOo . IIiIiII11i * Ii11Ii1I
 if 21 - 21: oOo0O0Ooo - oOo0O0Ooo + o0oOO0O00o0O % oOo0O0Ooo * OoOo00o
 if 74 - 74: o0oOO0O00o0O / iI1iI1I1i1I . oOo0O0Ooo - ii + IIiIiII11i + iI1iI1I1i1I
 if 36 - 36: Ii11Ii1I * oOo0O0Ooo * Ii1I . iI1iI1I1i1I * Ii1I
 if 76 - 76: IIIii1II1II + o0o00Oo0O / OooO0OoOOOO - oO0o
 if 27 - 27: I1ii11iIi11i - iI11I1II1I1I * o0oOO0O00o0O * IIiIiII11i * Ii1I
 if 9 - 9: Ii + IIIii1II1II - OOooOOo / O0OoO % ooOoO0O00 / OoOo00o
 if 22 - 22: ooOoO0O00
 if 3 - 3: oO0o * Ii1I - o0oOO0O00o0O + Ii1I
 if 63 - 63: iI1iI1I1i1I * O0OoO % IIiIiII11i % IIIi + oOo0O0Ooo * I1ii11iIi11i
 if 96 - 96: OooO0OoOOOO
 if 99 - 99: iI11I1II1I1I - O0OoO
 if 79 - 79: oOo0O0Ooo + OoOo00o % iI1iI1I1i1I % OoOo00o
 if 56 - 56: Ii1I + OoOo00o . oO0o + ii * Ii1I - o0o00Oo0O
 if 35 - 35: IIIii1II1II . iI1iI1I1i1I . IIIi - iI1iI1I1i1I % iI1iI1I1i1I + IIIi
 if 99 - 99: I11i + IIIii1II1II
 if 34 - 34: IIIi * I11i . oOo0O0Ooo % Ii
 if 61 - 61: iI11I1II1I1I + OoOo00o * iI1iI1I1i1I - ooOoO0O00 % OoOo00o
 if 76 - 76: OoOo00o / OOooOOo
 if 12 - 12: IIIi
def OO0oOo ( url ) :
 O000oo0O = iiI111I1iIiI ( str ( Ii1iIiII1ii1 ) + IIiIi1II1IiI ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 Ii1i = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( O000oo0O )
 for i1I1i111Ii , url , OOOOoO00o0O , I1I1I1IIi1III , iIiIiIiI in Ii1i :
  II1I ( i1I1i111Ii , url , 42 , OOOOoO00o0O , I1I1I1IIi1III , iIiIiIiI )
 iiO0o0oOOOoOo ( 'movies' , 'MAIN' )
 if 99 - 99: I1ii11iIi11i
def IiIi1I11 ( url ) :
 O000oo0O = iiI111I1iIiI ( str ( Ii1iIiII1ii1 ) + IiI1O000oo0o ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 Ii1i = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( O000oo0O )
 for i1I1i111Ii , url , OOOOoO00o0O , I1I1I1IIi1III , iIiIiIiI in Ii1i :
  II1I ( i1I1i111Ii , url , 42 , OOOOoO00o0O , I1I1I1IIi1III , iIiIiIiI )
 iiO0o0oOOOoOo ( 'movies' , 'MAIN' )
 if 4 - 4: IIIi * oOo0O0Ooo % oOo0O0Ooo / ii
def OO0000O ( url ) :
 O000oo0O = iiI111I1iIiI ( str ( Ii1iIiII1ii1 ) + iII ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 Ii1i = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( O000oo0O )
 for i1I1i111Ii , url , OOOOoO00o0O , I1I1I1IIi1III , iIiIiIiI in Ii1i :
  II1I ( i1I1i111Ii , url , 42 , OOOOoO00o0O , I1I1I1IIi1III , iIiIiIiI )
 iiO0o0oOOOoOo ( 'movies' , 'MAIN' )
 if 37 - 37: ii % oO0o
def I1111iIIiIIII ( url ) :
 O000oo0O = iiI111I1iIiI ( str ( Ii1iIiII1ii1 ) + oOo0Oii ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 Ii1i = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( O000oo0O )
 for i1I1i111Ii , url , OOOOoO00o0O , I1I1I1IIi1III , iIiIiIiI in Ii1i :
  II1I ( i1I1i111Ii , url , 42 , OOOOoO00o0O , I1I1I1IIi1III , iIiIiIiI )
 iiO0o0oOOOoOo ( 'movies' , 'MAIN' )
 if 57 - 57: O0OoO / Ii11Ii1I % I11i % Ii
def o0OO0Oooo ( url ) :
 O000oo0O = iiI111I1iIiI ( str ( Ii1iIiII1ii1 ) + o00OoO00o00 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 Ii1i = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( O000oo0O )
 for i1I1i111Ii , url , OOOOoO00o0O , I1I1I1IIi1III , iIiIiIiI in Ii1i :
  II1I ( i1I1i111Ii , url , 42 , OOOOoO00o0O , I1I1I1IIi1III , iIiIiIiI )
 iiO0o0oOOOoOo ( 'movies' , 'MAIN' )
 if 72 - 72: ooOoO0O00
def I1Iii11111I1iii ( url ) :
 O000oo0O = iiI111I1iIiI ( str ( Ii1iIiII1ii1 ) + OO0Oo00 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 Ii1i = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( O000oo0O )
 for i1I1i111Ii , url , OOOOoO00o0O , I1I1I1IIi1III , iIiIiIiI in Ii1i :
  II1I ( i1I1i111Ii , url , 42 , OOOOoO00o0O , I1I1I1IIi1III , iIiIiIiI )
 iiO0o0oOOOoOo ( 'movies' , 'MAIN' )
 if 28 - 28: oO0o + IIIi / OOooOOo % OoOo00o - I1ii11iIi11i
def ooOo0Ooo0 ( url ) :
 O000oo0O = iiI111I1iIiI ( str ( Ii1iIiII1ii1 ) + IIIiIii111IIi ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 Ii1i = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( O000oo0O )
 for i1I1i111Ii , url , OOOOoO00o0O , I1I1I1IIi1III , iIiIiIiI in Ii1i :
  II1I ( i1I1i111Ii , url , 42 , OOOOoO00o0O , I1I1I1IIi1III , iIiIiIiI )
 iiO0o0oOOOoOo ( 'movies' , 'MAIN' )
 if 100 - 100: ooOoO0O00 . ii % Ii11Ii1I
def oOoOo00oo ( url ) :
 O000oo0O = iiI111I1iIiI ( str ( Ii1iIiII1ii1 ) + II11IiIIiiiii ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 Ii1i = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( O000oo0O )
 for i1I1i111Ii , url , OOOOoO00o0O , I1I1I1IIi1III , iIiIiIiI in Ii1i :
  II1I ( i1I1i111Ii , url , 42 , OOOOoO00o0O , I1I1I1IIi1III , iIiIiIiI )
 iiO0o0oOOOoOo ( 'movies' , 'MAIN' )
 if 66 - 66: o0o00Oo0O * I11i / Ii1I
def I1Ii1IiiiII ( url ) :
 O000oo0O = iiI111I1iIiI ( str ( Ii1iIiII1ii1 ) + OoOo00OoOO00 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 Ii1i = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( O000oo0O )
 for i1I1i111Ii , url , OOOOoO00o0O , I1I1I1IIi1III , iIiIiIiI in Ii1i :
  II1I ( i1I1i111Ii , url , 42 , OOOOoO00o0O , I1I1I1IIi1III , iIiIiIiI )
 iiO0o0oOOOoOo ( 'movies' , 'MAIN' )
 if 62 - 62: OOooOOo * ii * I11i
def ii111Ii1i ( url ) :
 O000oo0O = iiI111I1iIiI ( str ( Ii1iIiII1ii1 ) + IiI1I1II ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 Ii1i = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( O000oo0O )
 for i1I1i111Ii , url , OOOOoO00o0O , I1I1I1IIi1III , iIiIiIiI in Ii1i :
  II1I ( i1I1i111Ii , url , 5 , OOOOoO00o0O , I1I1I1IIi1III , iIiIiIiI )
 iiO0o0oOOOoOo ( 'movies' , 'MAIN' )
 if 74 - 74: I1ii11iIi11i + I1ii11iIi11i / iI1iI1I1i1I
 if 21 - 21: ii / OooO0OoOOOO
 if 66 - 66: I11i * oO0o % ooOoO0O00 - iI11I1II1I1I
 if 11 - 11: o0oOO0O00o0O / OoOo00o % ooOoO0O00 . Ii1I
 if 16 - 16: ii - IIIii1II1II + I1ii11iIi11i
 if 67 - 67: Ii1I % ii
 if 41 - 41: oO0o / OooO0OoOOOO + IIIi . IIIi / OoOo00o
 if 74 - 74: Ii11Ii1I % Ii . o0o00Oo0O * oOo0O0Ooo * ooOoO0O00 * ii
 if 22 - 22: IIIi + o0oOO0O00o0O - iI1iI1I1i1I + iI11I1II1I1I / IIIi - ii
def IiII1111I ( ) :
 try :
  if os . path . exists ( iIii1 ) == True :
   i1iiIIiiI111 = xbmcgui . Dialog ( )
   if i1iiIIiiI111 . yesno ( "Delete Thumbnails" , "[COLOR gold][B]##########WARNING ANDROID ONLY##########[/B][/COLOR]" , "This feature deletes your thumbnail folder and textures13.db" , "Are you sure you want to do proceed? This Can NOT Be Undone" ) :
    for I11iiIi1i1 , iiIi1IIiI , i1oO0OO0 in os . walk ( iIii1 ) :
     iiIIii111Ii = 0
     iiIIii111Ii += len ( i1oO0OO0 )
     if iiIIii111Ii > 0 :
      for oO00oo0o00o0o in i1oO0OO0 :
       os . unlink ( os . path . join ( I11iiIi1i1 , oO00oo0o00o0o ) )
  OO000oooOo000 = os . path . join ( iI111I11I1I1 , "Textures13.db" )
  os . unlink ( OO000oooOo000 )
  i1iiIIiiI111 . ok ( "Restart KODI" , "Please restart KODI to rebuild thumbnail library" )
 except :
  i1iiIIiiI111 = xbmcgui . Dialog ( )
  i1iiIIiiI111 . ok ( o0oOoO00o , "Error Deleting Thumbnails please visit Kodi Support Group, GenieTv on facebook" )
 return
 if 97 - 97: IIIi % o0o00Oo0O
 if 61 - 61: OooO0OoOOOO . ii + ii * I11i / IIIi
 if 49 - 49: ooOoO0O00 . oO0o / Ii + Ii11Ii1I % o0o00Oo0O + Ii1I
 if 14 - 14: iI1iI1I1i1I - I1ii11iIi11i . I1ii11iIi11i * IIIii1II1II . oOo0O0Ooo % o0oOO0O00o0O
 if 86 - 86: oOo0O0Ooo + iI1iI1I1i1I * OOooOOo - IIIi / IIIi
 if 9 - 9: I11i / o0oOO0O00o0O . iI11I1II1I1I % o0o00Oo0O
 if 38 - 38: o0oOO0O00o0O
 if 78 - 78: Ii . OooO0OoOOOO % ii - OooO0OoOOOO - OooO0OoOOOO + Ii11Ii1I
 if 11 - 11: iI1iI1I1i1I
def IioooooOOo0Oo ( url ) :
 print '############################################################       DELETING STANDARD CACHE             ###############################################################'
 IiiiiiiI111i = os . path . join ( xbmc . translatePath ( 'special://home' ) , 'cache' )
 if os . path . exists ( IiiiiiiI111i ) == True :
  for I11iiIi1i1 , iiIi1IIiI , i1oO0OO0 in os . walk ( IiiiiiiI111i ) :
   iiIIii111Ii = 0
   iiIIii111Ii += len ( i1oO0OO0 )
   if 19 - 19: ii * OoOo00o
   if 60 - 60: IIiIiII11i - o0oOO0O00o0O + I11i % IIIii1II1II
   if iiIIii111Ii > 0 :
    if 97 - 97: o0o00Oo0O % o0o00Oo0O
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    if i1iiIIiiI111 . yesno ( "Delete KODI Cache Files" , str ( iiIIii111Ii ) + " files found" , "Do you want to delete them?" ) :
     if 35 - 35: o0oOO0O00o0O - Ii11Ii1I . Ii % o0o00Oo0O % Ii1I
     for oO00oo0o00o0o in i1oO0OO0 :
      try :
       os . unlink ( os . path . join ( I11iiIi1i1 , oO00oo0o00o0o ) )
      except :
       pass
     for O0Oo0o000oO in iiIi1IIiI :
      try :
       shutil . rmtree ( os . path . join ( I11iiIi1i1 , O0Oo0o000oO ) )
      except :
       pass
       if 92 - 92: IIIii1II1II % IIiIiII11i . o0oOO0O00o0O
   else :
    pass
 if xbmc . getCondVisibility ( 'system.platform.ATV2' ) :
  II1i1iI = os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'Other' )
  if 5 - 5: OOooOOo + o0oOO0O00o0O * O0OoO
  for I11iiIi1i1 , iiIi1IIiI , i1oO0OO0 in os . walk ( II1i1iI ) :
   iiIIii111Ii = 0
   iiIIii111Ii += len ( i1oO0OO0 )
   if 47 - 47: iI11I1II1I1I + oO0o % iI11I1II1I1I . O0OoO / I1ii11iIi11i - Ii
   if iiIIii111Ii > 0 :
    if 80 - 80: Ii1I / o0o00Oo0O / iI11I1II1I1I + oOo0O0Ooo
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    if i1iiIIiiI111 . yesno ( "Delete ATV2 Cache Files" , str ( iiIIii111Ii ) + " files found in 'Other'" , "Do you want to delete them?" ) :
     if 3 - 3: O0OoO / ooOoO0O00 - OOooOOo
     for oO00oo0o00o0o in i1oO0OO0 :
      os . unlink ( os . path . join ( I11iiIi1i1 , oO00oo0o00o0o ) )
     for O0Oo0o000oO in iiIi1IIiI :
      shutil . rmtree ( os . path . join ( I11iiIi1i1 , O0Oo0o000oO ) )
      if 73 - 73: ii * o0o00Oo0O * O0OoO
   else :
    pass
  iii11Ii = os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'LocalAndRental' )
  if 31 - 31: OoOo00o
  for I11iiIi1i1 , iiIi1IIiI , i1oO0OO0 in os . walk ( iii11Ii ) :
   iiIIii111Ii = 0
   iiIIii111Ii += len ( i1oO0OO0 )
   if 69 - 69: iI11I1II1I1I . iI1iI1I1i1I / o0oOO0O00o0O
   if iiIIii111Ii > 0 :
    if 87 - 87: o0o00Oo0O * oO0o + ooOoO0O00
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    if i1iiIIiiI111 . yesno ( "Delete ATV2 Cache Files" , str ( iiIIii111Ii ) + " files found in 'LocalAndRental'" , "Do you want to delete them?" ) :
     if 33 - 33: oOo0O0Ooo * IIIi
     for oO00oo0o00o0o in i1oO0OO0 :
      os . unlink ( os . path . join ( I11iiIi1i1 , oO00oo0o00o0o ) )
     for O0Oo0o000oO in iiIi1IIiI :
      shutil . rmtree ( os . path . join ( I11iiIi1i1 , O0Oo0o000oO ) )
      if 98 - 98: Ii1I - ii / oOo0O0Ooo . O0OoO - ooOoO0O00
   else :
    pass
    if 60 - 60: OOooOOo % OOooOOo
    if 2 - 2: Ii11Ii1I . o0o00Oo0O - OoOo00o + OooO0OoOOOO
    if 96 - 96: Ii11Ii1I + Ii11Ii1I
    if 28 - 28: o0oOO0O00o0O
 ii1Iiii1I = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.whatthefurk/cache' ) , '' )
 if os . path . exists ( ii1Iiii1I ) == True :
  for I11iiIi1i1 , iiIi1IIiI , i1oO0OO0 in os . walk ( ii1Iiii1I ) :
   iiIIii111Ii = 0
   iiIIii111Ii += len ( i1oO0OO0 )
   if 54 - 54: O0OoO - iI11I1II1I1I - iI1iI1I1i1I % Ii11Ii1I / IIiIiII11i
   if 80 - 80: Ii % iI11I1II1I1I / Ii
   if iiIIii111Ii > 0 :
    if 66 - 66: OOooOOo . iI11I1II1I1I * Ii1I - Ii11Ii1I - iI11I1II1I1I
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    if i1iiIIiiI111 . yesno ( "Delete WTF Cache Files" , str ( iiIIii111Ii ) + " files found" , "Do you want to delete them?" ) :
     if 28 - 28: OOooOOo % ii
     for oO00oo0o00o0o in i1oO0OO0 :
      os . unlink ( os . path . join ( I11iiIi1i1 , oO00oo0o00o0o ) )
     for O0Oo0o000oO in iiIi1IIiI :
      shutil . rmtree ( os . path . join ( I11iiIi1i1 , O0Oo0o000oO ) )
      if 13 - 13: OooO0OoOOOO . I1ii11iIi11i - iI1iI1I1i1I / OoOo00o - I1ii11iIi11i - oOo0O0Ooo
   else :
    pass
    if 84 - 84: IIiIiII11i
    if 57 - 57: o0o00Oo0O * iI11I1II1I1I % o0o00Oo0O . ii
 O00O = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.4od/cache' ) , '' )
 if os . path . exists ( O00O ) == True :
  for I11iiIi1i1 , iiIi1IIiI , i1oO0OO0 in os . walk ( O00O ) :
   iiIIii111Ii = 0
   iiIIii111Ii += len ( i1oO0OO0 )
   if 42 - 42: I11i + OoOo00o - ii + o0oOO0O00o0O % oO0o
   if 12 - 12: ooOoO0O00 / Ii1I - o0oOO0O00o0O . Ii / ooOoO0O00 / ii
   if iiIIii111Ii > 0 :
    if 88 - 88: Ii11Ii1I / Ii % OOooOOo % IIIii1II1II
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    if i1iiIIiiI111 . yesno ( "Delete 4oD Cache Files" , str ( iiIIii111Ii ) + " files found" , "Do you want to delete them?" ) :
     if 70 - 70: Ii1I . Ii1I / iI1iI1I1i1I . Ii1I
     for oO00oo0o00o0o in i1oO0OO0 :
      os . unlink ( os . path . join ( I11iiIi1i1 , oO00oo0o00o0o ) )
     for O0Oo0o000oO in iiIi1IIiI :
      shutil . rmtree ( os . path . join ( I11iiIi1i1 , O0Oo0o000oO ) )
      if 37 - 37: ooOoO0O00 . IIIi - IIiIiII11i % I11i - ooOoO0O00 . OoOo00o
   else :
    pass
    if 34 - 34: iI11I1II1I1I / IIiIiII11i
    if 3 - 3: I11i - ii + o0oOO0O00o0O . iI1iI1I1i1I
 o00000Oo = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.iplayer/iplayer_http_cache' ) , '' )
 if os . path . exists ( o00000Oo ) == True :
  for I11iiIi1i1 , iiIi1IIiI , i1oO0OO0 in os . walk ( o00000Oo ) :
   iiIIii111Ii = 0
   iiIIii111Ii += len ( i1oO0OO0 )
   if 63 - 63: IIiIiII11i * oOo0O0Ooo - ii / oOo0O0Ooo
   if 50 - 50: OOooOOo % Ii11Ii1I + OOooOOo * Ii11Ii1I - IIIii1II1II
   if iiIIii111Ii > 0 :
    if 94 - 94: iI11I1II1I1I
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    if i1iiIIiiI111 . yesno ( "Delete BBC iPlayer Cache Files" , str ( iiIIii111Ii ) + " files found" , "Do you want to delete them?" ) :
     if 1 - 1: o0o00Oo0O
     for oO00oo0o00o0o in i1oO0OO0 :
      os . unlink ( os . path . join ( I11iiIi1i1 , oO00oo0o00o0o ) )
     for O0Oo0o000oO in iiIi1IIiI :
      shutil . rmtree ( os . path . join ( I11iiIi1i1 , O0Oo0o000oO ) )
      if 2 - 2: oO0o . iI1iI1I1i1I
   else :
    pass
    if 97 - 97: I1ii11iIi11i
    if 65 - 65: I1ii11iIi11i % IIIii1II1II / Ii / iI11I1II1I1I . IIIi + O0OoO
    if 92 - 92: OoOo00o
 O0oo0O00ooOo = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/script.module.simple.downloader' ) , '' )
 if os . path . exists ( O0oo0O00ooOo ) == True :
  for I11iiIi1i1 , iiIi1IIiI , i1oO0OO0 in os . walk ( O0oo0O00ooOo ) :
   iiIIii111Ii = 0
   iiIIii111Ii += len ( i1oO0OO0 )
   if 70 - 70: I1ii11iIi11i + Ii
   if 44 - 44: Ii / IIIii1II1II * O0OoO
   if iiIIii111Ii > 0 :
    if 88 - 88: ooOoO0O00 % IIIii1II1II / ii * o0oOO0O00o0O % O0OoO
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    if i1iiIIiiI111 . yesno ( "Delete Simple Downloader Cache Files" , str ( iiIIii111Ii ) + " files found" , "Do you want to delete them?" ) :
     if 5 - 5: Ii1I * Ii11Ii1I % iI1iI1I1i1I % IIiIiII11i
     for oO00oo0o00o0o in i1oO0OO0 :
      os . unlink ( os . path . join ( I11iiIi1i1 , oO00oo0o00o0o ) )
     for O0Oo0o000oO in iiIi1IIiI :
      shutil . rmtree ( os . path . join ( I11iiIi1i1 , O0Oo0o000oO ) )
      if 9 - 9: I11i % IIIi + iI1iI1I1i1I
   else :
    pass
    if 55 - 55: oO0o - Ii1I
    if 38 - 38: iI11I1II1I1I % OooO0OoOOOO % oO0o % o0o00Oo0O * iI11I1II1I1I / IIIi
 o00O00oO = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.itv/Images' ) , '' )
 if os . path . exists ( o00O00oO ) == True :
  for I11iiIi1i1 , iiIi1IIiI , i1oO0OO0 in os . walk ( o00O00oO ) :
   iiIIii111Ii = 0
   iiIIii111Ii += len ( i1oO0OO0 )
   if 64 - 64: Ii1I * Ii11Ii1I * I1ii11iIi11i % OooO0OoOOOO % O0OoO
   if 55 - 55: IIiIiII11i - IIIi - IIIii1II1II % Ii11Ii1I
   if iiIIii111Ii > 0 :
    if 49 - 49: I1ii11iIi11i * IIIi
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    if i1iiIIiiI111 . yesno ( "Delete ITV Cache Files" , str ( iiIIii111Ii ) + " files found" , "Do you want to delete them?" ) :
     if 53 - 53: I1ii11iIi11i / Ii11Ii1I + OoOo00o . o0oOO0O00o0O + OooO0OoOOOO
     for oO00oo0o00o0o in i1oO0OO0 :
      os . unlink ( os . path . join ( I11iiIi1i1 , oO00oo0o00o0o ) )
     for O0Oo0o000oO in iiIi1IIiI :
      shutil . rmtree ( os . path . join ( I11iiIi1i1 , O0Oo0o000oO ) )
      if 19 - 19: Ii11Ii1I
   else :
    pass
    if 51 - 51: iI11I1II1I1I
    if 8 - 8: oO0o / I11i % o0oOO0O00o0O . Ii . ii . Ii11Ii1I
 iIII1iIiIIIIi = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.movies4me/cache' ) , '' )
 if os . path . exists ( o00O00oO ) == True :
  for I11iiIi1i1 , iiIi1IIiI , i1oO0OO0 in os . walk ( iIII1iIiIIIIi ) :
   iiIIii111Ii = 0
   iiIIii111Ii += len ( i1oO0OO0 )
   if 50 - 50: oOo0O0Ooo
   if 4 - 4: I1ii11iIi11i * o0o00Oo0O - OoOo00o % O0OoO + OOooOOo
   if iiIIii111Ii > 0 :
    if 3 - 3: OOooOOo
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    if i1iiIIiiI111 . yesno ( "Delete Movies4me Cache Files" , str ( iiIIii111Ii ) + " files found" , "Do you want to delete them?" ) :
     if 91 - 91: o0o00Oo0O - iI1iI1I1i1I % IIIi
     for oO00oo0o00o0o in i1oO0OO0 :
      os . unlink ( os . path . join ( I11iiIi1i1 , oO00oo0o00o0o ) )
     for O0Oo0o000oO in iiIi1IIiI :
      shutil . rmtree ( os . path . join ( I11iiIi1i1 , O0Oo0o000oO ) )
      if 46 - 46: O0OoO / oOo0O0Ooo . OooO0OoOOOO % oO0o / Ii
   else :
    pass
    if 13 - 13: IIIi % I11i + IIIii1II1II + IIIi + Ii - Ii1I
    if 70 - 70: IIiIiII11i * IIiIiII11i . oOo0O0Ooo
 iiIi1111iiI1 = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.phstreams/Cache' ) , '' )
 if os . path . exists ( o00O00oO ) == True :
  for I11iiIi1i1 , iiIi1IIiI , i1oO0OO0 in os . walk ( iiIi1111iiI1 ) :
   iiIIii111Ii = 0
   iiIIii111Ii += len ( i1oO0OO0 )
   if 85 - 85: iI1iI1I1i1I + IIIi
   if 11 - 11: iI1iI1I1i1I
   if iiIIii111Ii > 0 :
    if 95 - 95: I1ii11iIi11i + Ii % IIIii1II1II - OoOo00o
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    if i1iiIIiiI111 . yesno ( "Delete Phoenix Cache Files" , str ( iiIIii111Ii ) + " files found" , "Do you want to delete them?" ) :
     if 11 - 11: Ii1I / o0o00Oo0O + IIiIiII11i
     for oO00oo0o00o0o in i1oO0OO0 :
      os . unlink ( os . path . join ( I11iiIi1i1 , oO00oo0o00o0o ) )
     for O0Oo0o000oO in iiIi1IIiI :
      shutil . rmtree ( os . path . join ( I11iiIi1i1 , O0Oo0o000oO ) )
      if 95 - 95: IIIi + OooO0OoOOOO * iI11I1II1I1I
   else :
    pass
    if 17 - 17: oO0o - I1ii11iIi11i * o0o00Oo0O / Ii11Ii1I
    if 19 - 19: ooOoO0O00 - iI11I1II1I1I . iI1iI1I1i1I
 iiIIi1i111i = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.spotitube/cache' ) , '' )
 if os . path . exists ( o00O00oO ) == True :
  for I11iiIi1i1 , iiIi1IIiI , i1oO0OO0 in os . walk ( iiIIi1i111i ) :
   iiIIii111Ii = 0
   iiIIii111Ii += len ( i1oO0OO0 )
   if 48 - 48: I1ii11iIi11i . I11i - o0oOO0O00o0O
   if 15 - 15: I11i
   if iiIIii111Ii > 0 :
    if 87 - 87: I11i
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    if i1iiIIiiI111 . yesno ( "Delete YouTube Music Cache Files" , str ( iiIIii111Ii ) + " files found" , "Do you want to delete them?" ) :
     if 99 - 99: Ii11Ii1I / I1ii11iIi11i * IIiIiII11i / o0o00Oo0O
     for oO00oo0o00o0o in i1oO0OO0 :
      os . unlink ( os . path . join ( I11iiIi1i1 , oO00oo0o00o0o ) )
     for O0Oo0o000oO in iiIi1IIiI :
      shutil . rmtree ( os . path . join ( I11iiIi1i1 , O0Oo0o000oO ) )
      if 44 - 44: Ii % IIIi % OoOo00o + iI1iI1I1i1I * OoOo00o . Ii11Ii1I
   else :
    pass
    if 89 - 89: ii % IIiIiII11i - oO0o % Ii
    if 7 - 7: OooO0OoOOOO
 III11i = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.supercartoons/cache' ) , '' )
 if os . path . exists ( o00O00oO ) == True :
  for I11iiIi1i1 , iiIi1IIiI , i1oO0OO0 in os . walk ( III11i ) :
   iiIIii111Ii = 0
   iiIIii111Ii += len ( i1oO0OO0 )
   if 54 - 54: IIIi / I11i
   if 39 - 39: IIIii1II1II % OoOo00o * Ii1I - o0o00Oo0O + oOo0O0Ooo + I11i
   if iiIIii111Ii > 0 :
    if 64 - 64: IIiIiII11i / IIiIiII11i
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    if i1iiIIiiI111 . yesno ( "Delete SuperCartoons Cache Files" , str ( iiIIii111Ii ) + " files found" , "Do you want to delete them?" ) :
     if 52 - 52: IIIi * Ii1I
     for oO00oo0o00o0o in i1oO0OO0 :
      os . unlink ( os . path . join ( I11iiIi1i1 , oO00oo0o00o0o ) )
     for O0Oo0o000oO in iiIi1IIiI :
      shutil . rmtree ( os . path . join ( I11iiIi1i1 , O0Oo0o000oO ) )
      if 35 - 35: I11i % oO0o
   else :
    pass
    if 27 - 27: Ii11Ii1I - iI11I1II1I1I * Ii11Ii1I
    if 30 - 30: I11i + Ii11Ii1I / ii - OooO0OoOOOO % OoOo00o
 IiIIiIiIIiI = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.tvonline.cc/cache' ) , '' )
 if os . path . exists ( o00O00oO ) == True :
  for I11iiIi1i1 , iiIi1IIiI , i1oO0OO0 in os . walk ( IiIIiIiIIiI ) :
   iiIIii111Ii = 0
   iiIIii111Ii += len ( i1oO0OO0 )
   if 26 - 26: O0OoO % ii . IIIi * O0OoO + IIiIiII11i - Ii1I
   if 20 - 20: oO0o
   if iiIIii111Ii > 0 :
    if 99 - 99: I1ii11iIi11i + ii . o0oOO0O00o0O + o0o00Oo0O
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    if i1iiIIiiI111 . yesno ( "Delete TVonline Cache Files" , str ( iiIIii111Ii ) + " files found" , "Do you want to delete them?" ) :
     if 85 - 85: IIiIiII11i - Ii11Ii1I
     for oO00oo0o00o0o in i1oO0OO0 :
      os . unlink ( os . path . join ( I11iiIi1i1 , oO00oo0o00o0o ) )
     for O0Oo0o000oO in iiIi1IIiI :
      shutil . rmtree ( os . path . join ( I11iiIi1i1 , O0Oo0o000oO ) )
      if 93 - 93: OooO0OoOOOO / Ii - OoOo00o + oO0o / ooOoO0O00
   else :
    pass
    if 62 - 62: Ii1I / ii * oOo0O0Ooo - ooOoO0O00
    if 81 - 81: OoOo00o / o0o00Oo0O * O0OoO % OOooOOo / o0o00Oo0O
 ooooooo = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.youtube/kodion' ) , '' )
 if os . path . exists ( o00O00oO ) == True :
  for I11iiIi1i1 , iiIi1IIiI , i1oO0OO0 in os . walk ( ooooooo ) :
   iiIIii111Ii = 0
   iiIIii111Ii += len ( i1oO0OO0 )
   if 58 - 58: ooOoO0O00 + o0o00Oo0O . oO0o % iI1iI1I1i1I
   if 39 - 39: I11i + OooO0OoOOOO / Ii11Ii1I + I11i
   if iiIIii111Ii > 0 :
    if 33 - 33: o0oOO0O00o0O - I1ii11iIi11i - iI1iI1I1i1I
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    if i1iiIIiiI111 . yesno ( "Delete YouTube Cache Files" , str ( iiIIii111Ii ) + " files found" , "Do you want to delete them?" ) :
     if 61 - 61: Ii11Ii1I + oOo0O0Ooo / ooOoO0O00 + ooOoO0O00 / OoOo00o
     for oO00oo0o00o0o in i1oO0OO0 :
      os . unlink ( os . path . join ( I11iiIi1i1 , oO00oo0o00o0o ) )
     for O0Oo0o000oO in iiIi1IIiI :
      shutil . rmtree ( os . path . join ( I11iiIi1i1 , O0Oo0o000oO ) )
      if 47 - 47: IIIi
   else :
    pass
    if 25 - 25: o0oOO0O00o0O + oOo0O0Ooo + OOooOOo + IIIi % o0o00Oo0O
    if 26 - 26: O0OoO + OOooOOo
    if 17 - 17: Ii1I - o0oOO0O00o0O % I1ii11iIi11i * o0o00Oo0O % o0o00Oo0O * IIIii1II1II
 iIi1i1iiIiiiI = xbmc . translatePath ( 'special://masterprofile/addon_data/plugin.video.genesis' )
 i1iiIIiiI111 = xbmcgui . Dialog ( )
 try :
  if i1iiIIiiI111 . yesno ( "Delete Genesis Cache Files" , "Do you want to delete cache" ) :
   OoO00o0o0oo0o = os . path . join ( iIi1i1iiIiiiI , "cache.db" )
   os . unlink ( OoO00o0o0oo0o )
   if 13 - 13: iI1iI1I1i1I % IIIi . ooOoO0O00
 except :
  pass
  if 1 - 1: I11i % I11i . iI11I1II1I1I . ii . OooO0OoOOOO . o0oOO0O00o0O
 i1iiIIiiI111 = xbmcgui . Dialog ( )
 i1iiIIiiI111 . ok ( "GenieTv" , "                               Finished Deleting Cache " , "                          [COLOR gold]Brought To You By GenieTv[/COLOR]" )
 if 58 - 58: ii / iI11I1II1I1I
 if 25 - 25: o0o00Oo0O % Ii + Ii11Ii1I + IIIii1II1II
 if 40 - 40: I11i + IIIi * OoOo00o + iI1iI1I1i1I
 if 75 - 75: oO0o - OOooOOo - ooOoO0O00 % I1ii11iIi11i - IIiIiII11i
 if 61 - 61: I1ii11iIi11i + ii / Ii
 if 44 - 44: OooO0OoOOOO . iI1iI1I1i1I % oOo0O0Ooo - ooOoO0O00
 if 2 - 2: OOooOOo + OOooOOo
 if 47 - 47: oO0o + IIIi . IIIi * o0o00Oo0O / I1ii11iIi11i + IIIii1II1II
 if 44 - 44: I11i + IIIi + OOooOOo * I1ii11iIi11i
def I1ioo ( url ) :
 print '###' + o0oOoO00o + ' - DELETING PACKAGES###'
 o0OOoo = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' , '' ) )
 try :
  for I11iiIi1i1 , iiIi1IIiI , i1oO0OO0 in os . walk ( o0OOoo ) :
   iiIIii111Ii = 0
   iiIIii111Ii += len ( i1oO0OO0 )
   if 52 - 52: oO0o
   if 49 - 49: Ii11Ii1I . Ii1I % O0OoO . I1ii11iIi11i * IIIii1II1II
   if iiIIii111Ii > 0 :
    if 44 - 44: iI11I1II1I1I / o0o00Oo0O * I1ii11iIi11i + oOo0O0Ooo . O0OoO
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    if i1iiIIiiI111 . yesno ( "Delete Package Cache Files" , str ( iiIIii111Ii ) + " files found" , "Do you want to delete them?" ) :
     if 20 - 20: o0oOO0O00o0O + I11i . IIIi / Ii
     for oO00oo0o00o0o in i1oO0OO0 :
      os . unlink ( os . path . join ( I11iiIi1i1 , oO00oo0o00o0o ) )
     for O0Oo0o000oO in iiIi1IIiI :
      shutil . rmtree ( os . path . join ( I11iiIi1i1 , O0Oo0o000oO ) )
     i1iiIIiiI111 = xbmcgui . Dialog ( )
     i1iiIIiiI111 . ok ( o0oOoO00o , "       Deleting Packages all done" )
    else :
     pass
   else :
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    i1iiIIiiI111 . ok ( o0oOoO00o , "       No Packages to DELETE" )
 except :
  i1iiIIiiI111 = xbmcgui . Dialog ( )
  i1iiIIiiI111 . ok ( o0oOoO00o , "Error Deleting Packages please visit Kodi Support Group, GenieTv on facebook" )
 return
 if 7 - 7: OOooOOo / OOooOOo . IIIi * o0o00Oo0O + OooO0OoOOOO + OoOo00o
 if 98 - 98: IIiIiII11i * OooO0OoOOOO - oOo0O0Ooo % I11i - o0oOO0O00o0O % Ii1I
 if 69 - 69: ooOoO0O00 % oO0o % IIIi / O0OoO / O0OoO
 if 6 - 6: IIiIiII11i % Ii1I % ooOoO0O00 * O0OoO
 if 47 - 47: o0o00Oo0O
 if 55 - 55: oO0o % o0o00Oo0O / ii
 if 49 - 49: oOo0O0Ooo . oO0o * ii % Ii + iI11I1II1I1I * ooOoO0O00
 if 88 - 88: Ii1I * o0oOO0O00o0O + IIiIiII11i
 if 62 - 62: ii
def iioOo00O0o ( url ) :
 print '###' + o0oOoO00o + ' - DELETING PACKAGES###'
 o0OOoo = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' , '' ) )
 try :
  for I11iiIi1i1 , iiIi1IIiI , i1oO0OO0 in os . walk ( o0OOoo ) :
   iiIIii111Ii = 0
   iiIIii111Ii += len ( i1oO0OO0 )
   if 18 - 18: O0OoO
   if 37 - 37: I1ii11iIi11i % Ii - oOo0O0Ooo * Ii1I . O0OoO
   if iiIIii111Ii > 0 :
    if 62 - 62: ii / O0OoO + Ii1I . I11i - o0oOO0O00o0O
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    if i1iiIIiiI111 . yesno ( "Delete Package Cache Files" , str ( iiIIii111Ii ) + " files found" , "Do you want to delete them?" ) :
     if 29 - 29: OoOo00o
     for oO00oo0o00o0o in i1oO0OO0 :
      os . unlink ( os . path . join ( I11iiIi1i1 , oO00oo0o00o0o ) )
     for O0Oo0o000oO in iiIi1IIiI :
      shutil . rmtree ( os . path . join ( I11iiIi1i1 , O0Oo0o000oO ) )
     i1iiIIiiI111 = xbmcgui . Dialog ( )
     i1iiIIiiI111 . ok ( o0oOoO00o , "       Deleting Packages all done" )
    else :
     pass
   else :
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    i1iiIIiiI111 . ok ( o0oOoO00o , "       No Packages to DELETE" )
 except :
  i1iiIIiiI111 = xbmcgui . Dialog ( )
  i1iiIIiiI111 . ok ( o0oOoO00o , "Error Deleting Packages please visit Kodi Support Group, GenieTv on facebook" )
 return
 IioooooOOo0Oo ( url )
 if 26 - 26: o0o00Oo0O % IIIii1II1II - OooO0OoOOOO . IIIii1II1II
 if 70 - 70: I11i + iI1iI1I1i1I / o0oOO0O00o0O + O0OoO / oOo0O0Ooo
 if 33 - 33: ii . o0o00Oo0O
 if 59 - 59: iI11I1II1I1I
 if 45 - 45: o0o00Oo0O
 if 78 - 78: iI1iI1I1i1I - iI11I1II1I1I + IIIi - Ii1I - IIIi
 if 21 - 21: ii . o0o00Oo0O / Ii
 if 86 - 86: OOooOOo / IIIii1II1II
 if 40 - 40: iI11I1II1I1I / O0OoO / oOo0O0Ooo + Ii1I * IIIii1II1II
def III1i1iI111I1 ( url , name ) :
 O00OoOO0oo0 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 OOoO0OooO0O = os . path . join ( O00OoOO0oo0 , 'advancedsettings.xml' )
 i1iiIIiiI111 = xbmcgui . Dialog ( )
 OOOO00O0OO0oo = os . path . join ( O00OoOO0oo0 , 'advancedsettings.xml.bak' )
 if os . path . exists ( OOOO00O0OO0oo ) == False :
  if i1iiIIiiI111 . yesno ( "Back Up Original" , 'Have You Backed Up Your Original?' , '' , "[B][COLOR red]     AS YOU CANNOT GO BACK !!![/B][/COLOR]" ) :
   print '###' + o0oOoO00o + ' - ADVANCED XML###'
   O00OoOO0oo0 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
   OOoO0OooO0O = os . path . join ( O00OoOO0oo0 , 'advancedsettings.xml' )
   try :
    os . remove ( OOoO0OooO0O )
    print '=== GenieTv - REMOVING    ' + str ( OOoO0OooO0O ) + '    ==='
   except :
    pass
   O000oo0O = i1 . http_GET ( url ) . content
   IiIIIIIi = open ( OOoO0OooO0O , "w" )
   IiIIIIIi . write ( O000oo0O )
   IiIIIIIi . close ( )
   print '=== GenieTv - WRITING NEW    ' + str ( OOoO0OooO0O ) + '    ==='
   i1iiIIiiI111 = xbmcgui . Dialog ( )
   i1iiIIiiI111 . ok ( o0oOoO00o , "       Done Adding new Advanced XML" )
 else :
  print '###' + o0oOoO00o + ' - ADVANCED XML###'
  O00OoOO0oo0 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
  OOoO0OooO0O = os . path . join ( O00OoOO0oo0 , 'advancedsettings.xml' )
  try :
   os . remove ( OOoO0OooO0O )
   print '=== GenieTv - REMOVING    ' + str ( OOoO0OooO0O ) + '    ==='
  except :
   pass
  O000oo0O = i1 . http_GET ( url ) . content
  IiIIIIIi = open ( OOoO0OooO0O , "w" )
  IiIIIIIi . write ( O000oo0O )
  IiIIIIIi . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( OOoO0OooO0O ) + '    ==='
  i1iiIIiiI111 = xbmcgui . Dialog ( )
  i1iiIIiiI111 . ok ( o0oOoO00o , "       Done Adding new Advanced XML" )
 return
 if 41 - 41: OOooOOo % IIIi * OoOo00o * ooOoO0O00
def IiIii1i ( url , name ) :
 print '###' + o0oOoO00o + ' - CHECK ADVANCE XML###'
 O00OoOO0oo0 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 OOoO0OooO0O = os . path . join ( O00OoOO0oo0 , 'advancedsettings.xml' )
 try :
  IiIIIIIi = open ( OOoO0OooO0O ) . read ( )
  if 'zero' in IiIIIIIi :
   name = '0CACHE'
  elif 'tuxen' in IiIIIIIi :
   name = 'TUXENS'
  elif 'muckys' in IiIIIIIi :
   name = 'MUCKYS'
  elif 'p2p1' in IiIIIIIi :
   name = '1st P2P RECOMMENDED'
  elif 'p2p2' in IiIIIIIi :
   name = '2nd P2P RECOMMENDED'
  elif 'mikey' in IiIIIIIi :
   name = 'MIKEY1234'
 except :
  name = "NO ADVANCED"
 i1iiIIiiI111 = xbmcgui . Dialog ( )
 i1iiIIiiI111 . ok ( o0oOoO00o , "[COLOR yellow]YOU HAVE[/COLOR] " + name + "[COLOR yellow] XML SETTINGS SETUP[/COLOR]" )
 return
 if 27 - 27: O0OoO . I1ii11iIi11i + O0OoO + o0oOO0O00o0O
def III11IiI ( url ) :
 print '###' + o0oOoO00o + ' - DELETING ADVANCE XML###'
 O00OoOO0oo0 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 OOoO0OooO0O = os . path . join ( O00OoOO0oo0 , 'advancedsettings.xml' )
 try :
  os . remove ( OOoO0OooO0O )
  i1iiIIiiI111 = xbmcgui . Dialog ( )
  print '=== GenieTv - DELETING    ' + str ( OOoO0OooO0O ) + '    ==='
  i1iiIIiiI111 . ok ( o0oOoO00o , "       Remove Advanced Settings Sucessfull" )
 except :
  i1iiIIiiI111 = xbmcgui . Dialog ( )
  i1iiIIiiI111 . ok ( o0oOoO00o , "       No Advanced Settings To Remove" )
 return
 if 6 - 6: IIIii1II1II / iI11I1II1I1I / O0OoO / oOo0O0Ooo - ooOoO0O00 - IIIii1II1II
 if 8 - 8: Ii * iI1iI1I1i1I . IIIii1II1II / IIIii1II1II
 if 42 - 42: ii / IIIi . I11i / o0o00Oo0O - OooO0OoOOOO * OooO0OoOOOO
 if 1 - 1: Ii11Ii1I % IIIi
 if 97 - 97: OOooOOo
 if 13 - 13: OOooOOo % IIIii1II1II . o0o00Oo0O / I1ii11iIi11i % I1ii11iIi11i
 if 19 - 19: IIIi % O0OoO - O0OoO % oOo0O0Ooo . IIIii1II1II - ii
 if 100 - 100: oOo0O0Ooo + Ii11Ii1I + I11i . ooOoO0O00 % ii
 if 64 - 64: o0o00Oo0O % ooOoO0O00 * IIIi - Ii11Ii1I + I1ii11iIi11i
 if 65 - 65: OOooOOo . Ii
def III111i1IIiiI ( url = 'http://www.iplocation.net/' , inc = 1 ) :
 Ii1i = re . compile ( "<td width='80'>(.+?)</td><td>(.+?)</td><td>(.+?)</td><td>.+?</td><td>(.+?)</td>" ) . findall ( i1 . http_GET ( url ) . content )
 for OOo0oo , ooo0ooOoOOoO , ii1i1 , O0OooO0oo in Ii1i :
  if inc < 2 : i1iiIIiiI111 = xbmcgui . Dialog ( ) ; i1iiIIiiI111 . ok ( 'Check My IP' , "[B][COLOR gold]Your IP Address is: [/COLOR][/B] %s" % OOo0oo , '[B][COLOR gold]Your IP is based in: [/COLOR][/B] %s' % ii1i1 , '[B][COLOR gold]Your Service Provider is:[/COLOR][/B] %s' % O0OooO0oo )
  inc = inc + 1
  if 81 - 81: o0oOO0O00o0O / Ii1I
  if 55 - 55: I11i % IIIii1II1II - Ii1I / OooO0OoOOOO / Ii % IIIi
  if 43 - 43: o0o00Oo0O / IIIi . iI11I1II1I1I - OOooOOo
  if 47 - 47: IIiIiII11i - Ii1I - Ii11Ii1I
  if 9 - 9: Ii1I - OooO0OoOOOO
  if 64 - 64: ooOoO0O00
  if 71 - 71: OooO0OoOOOO * I11i
  if 99 - 99: I11i
  if 28 - 28: ii % o0o00Oo0O - IIIii1II1II / I11i / oOo0O0Ooo
def Iii1iIII1Iii ( url , name ) :
 i1iiIIiiI111 = xbmcgui . Dialog ( )
 if i1iiIIiiI111 . yesno ( "GenieTv" , '                                    Install Latest .ini File' ) :
  print '###' + o0oOoO00o + ' - CUSTOM FTV INI###'
  O00OoOO0oo0 = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/plugin.video.GenieTv' , '' ) )
  OOoO0OooO0O = os . path . join ( O00OoOO0oo0 , 'addons2.ini' )
  O000oo0O = i1 . http_GET ( url ) . content
  IiIIIIIi = open ( OOoO0OooO0O , "w" )
  IiIIIIIi . write ( O000oo0O )
  IiIIIIIi . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( OOoO0OooO0O ) + '    ==='
  i1iiIIiiI111 = xbmcgui . Dialog ( )
  i1iiIIiiI111 . ok ( o0oOoO00o , "                               Done Adding New .ini File" )
 return
 if 13 - 13: iI11I1II1I1I - IIIii1II1II
def i111ii1II11ii ( url , name ) :
 i1iiIIiiI111 = xbmcgui . Dialog ( )
 if i1iiIIiiI111 . yesno ( "GenieTv" , '                               Install Custom Settings' ) :
  print '###' + o0oOoO00o + ' - CUSTOM FTV SETTINGS###'
  O00OoOO0oo0 = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/plugin.video.GenieTv' , '' ) )
  OOoO0OooO0O = os . path . join ( O00OoOO0oo0 , 'settings.xml' )
  O000oo0O = i1 . http_GET ( url ) . content
  IiIIIIIi = open ( OOoO0OooO0O , "w" )
  IiIIIIIi . write ( O000oo0O )
  IiIIIIIi . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( OOoO0OooO0O ) + '    ==='
  i1iiIIiiI111 = xbmcgui . Dialog ( )
  i1iiIIiiI111 . ok ( o0oOoO00o , "                               Done Adding New Settings" )
 return
 if 21 - 21: iI1iI1I1i1I
 if 79 - 79: oO0o / IIIii1II1II - ooOoO0O00 + ooOoO0O00 - OooO0OoOOOO + OooO0OoOOOO
def oOoOo000Ooooo ( ) :
 try :
  I1iIiii = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/plugin.video.GenieTv' , '' ) )
  if os . path . exists ( I1iIiii ) == True :
   i1iiIIiiI111 = xbmcgui . Dialog ( )
   if i1iiIIiiI111 . yesno ( "GenieTv" , "                               Delete FTV Guide Database" ) :
    OoOOo0OO0OOoo = os . path . join ( I1iIiii , "source.db" )
    os . unlink ( OoOOo0OO0OOoo )
  i1iiIIiiI111 . ok ( "GenieTv" , "                                     FTV Database Reset" )
 except :
  i1iiIIiiI111 = xbmcgui . Dialog ( )
  i1iiIIiiI111 . ok ( o0oOoO00o , "               Error Deleting Database No Database To Delete" )
 return
 if 38 - 38: OooO0OoOOOO . I11i
 if 32 - 32: O0OoO . OooO0OoOOOO . IIiIiII11i
 if 25 - 25: OooO0OoOOOO * IIIi - OoOo00o * Ii * oOo0O0Ooo * IIIii1II1II
 if 56 - 56: ii . oOo0O0Ooo . IIiIiII11i % o0oOO0O00o0O
 if 59 - 59: O0OoO % I1ii11iIi11i - OoOo00o + OooO0OoOOOO
def iiI111I1iIiI ( url ) :
 I11iii1Ii = urllib2 . Request ( url )
 I11iii1Ii . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
 I1IIiiIiii = urllib2 . urlopen ( I11iii1Ii )
 O000oo0O = I1IIiiIiii . read ( )
 I1IIiiIiii . close ( )
 return O000oo0O
 if 33 - 33: Ii11Ii1I + OOooOOo - Ii1I + iI11I1II1I1I % ooOoO0O00 * OooO0OoOOOO
 if 21 - 21: o0o00Oo0O * O0OoO % oO0o
 if 14 - 14: o0o00Oo0O / IIIi / O0OoO + OooO0OoOOOO - OooO0OoOOOO
 if 10 - 10: o0o00Oo0O - Ii1I / IIIi % OOooOOo / ii / Ii11Ii1I
 if 73 - 73: O0OoO + OooO0OoOOOO % I11i . Ii1I / IIIii1II1II . IIIi
 if 76 - 76: iI1iI1I1i1I . Ii1I * ii % o0oOO0O00o0O
 if 24 - 24: ii
def ooOOo ( params ) :
 plugintools . log ( "freshstart.main_list " + repr ( params ) ) ; O000O0 = plugintools . message_yes_no ( o0oOoO00o , "Do you wish to restore your" , "Kodi configuration to default settings?" )
 if O000O0 :
  oooo0O = xbmcaddon . Addon ( id = o00 ) . getAddonInfo ( 'path' ) ; oooo0O = xbmc . translatePath ( oooo0O ) ;
  iII11 = os . path . join ( oooo0O , ".." , ".." ) ; iII11 = os . path . abspath ( iII11 ) ; plugintools . log ( "freshstart.main_list xbmcPath=" + iII11 ) ; OO0OoO0OOoOo = False
  try :
   for I11iiIi1i1 , iiIi1IIiI , i1oO0OO0 in os . walk ( iII11 , topdown = True ) :
    iiIi1IIiI [ : ] = [ O0Oo0o000oO for O0Oo0o000oO in iiIi1IIiI if O0Oo0o000oO not in iiIIIII1i1iI ]
    for i1I1i111Ii in i1oO0OO0 :
     try : os . remove ( os . path . join ( I11iiIi1i1 , i1I1i111Ii ) )
     except :
      if i1I1i111Ii not in [ "Addons15.db" , "MyVideos75.db" , "Textures13.db" , "xbmc.log" ] : OO0OoO0OOoOo = True
      plugintools . log ( "Error removing " + I11iiIi1i1 + " " + i1I1i111Ii )
    for i1I1i111Ii in iiIi1IIiI :
     try : os . rmdir ( os . path . join ( I11iiIi1i1 , i1I1i111Ii ) )
     except :
      if i1I1i111Ii not in [ "Database" , "userdata" ] : OO0OoO0OOoOo = True
      plugintools . log ( "Error removing " + I11iiIi1i1 + " " + i1I1i111Ii )
   if not OO0OoO0OOoOo : plugintools . log ( "freshstart.main_list All user files removed, you now have a clean install" ) ; plugintools . message ( o0oOoO00o , "The process is complete, you're now back to a fresh Kodi configuration with GenieTv!" , "Please reboot your system or restart Kodi in order for the changes to be applied." )
   else : plugintools . log ( "freshstart.main_list User files partially removed" ) ; plugintools . message ( o0oOoO00o , "The process is complete, you're now back to a fresh Kodi configuration with GenieTv" , "Please reboot your system or restart Kodi in order for the changes to be applied." )
  except : plugintools . message ( o0oOoO00o , "Problem found" , "Your settings has not been changed" ) ; import traceback ; plugintools . log ( traceback . format_exc ( ) ) ; plugintools . log ( "freshstart.main_list NOT removed" )
  plugintools . add_item ( action = "" , title = "Now Exit Kodi" , folder = False )
 else : plugintools . message ( o0oOoO00o , "Your settings" , "has not been changed" ) ; plugintools . add_item ( action = "" , title = "Done" , folder = False )
 iiIii1I ( )
 if 84 - 84: OoOo00o / Ii11Ii1I * o0oOO0O00o0O
 if 20 - 20: OOooOOo % o0o00Oo0O
 if 59 - 59: o0o00Oo0O . I11i % Ii1I * OoOo00o + iI1iI1I1i1I
def o00oIiIiIiiI ( ) :
 o0o00oo = [ ]
 ii1I11Iii = sys . argv [ 2 ]
 if len ( ii1I11Iii ) >= 2 :
  I1i1Iii1i1II1 = sys . argv [ 2 ]
  O0o00OoooO = I1i1Iii1i1II1 . replace ( '?' , '' )
  if ( I1i1Iii1i1II1 [ len ( I1i1Iii1i1II1 ) - 1 ] == '/' ) :
   I1i1Iii1i1II1 = I1i1Iii1i1II1 [ 0 : len ( I1i1Iii1i1II1 ) - 2 ]
  IiI1i1iI = O0o00OoooO . split ( '&' )
  o0o00oo = { }
  for ii1ii1I1IIi1 in range ( len ( IiI1i1iI ) ) :
   iIIi = { }
   iIIi = IiI1i1iI [ ii1ii1I1IIi1 ] . split ( '=' )
   if ( len ( iIIi ) ) == 2 :
    o0o00oo [ iIIi [ 0 ] ] = iIIi [ 1 ]
    if 25 - 25: I1ii11iIi11i + I11i - oO0o
 return o0o00oo
 if 57 - 57: IIiIiII11i . ooOoO0O00
IIiI1I1 = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkbw==' )
ii1II = base64 . decodestring ( 'L3N0b3JhZ2UvZW11bGF0ZWQvMA==' )
I11I1IIiiII1 = base64 . decodestring ( 'L2dlbmllLnR4dA==' )
I11Ii1 = base64 . decodestring ( 'LmFyY2hpdGVjdHMueDEwaG9zdC5jb20vdGVzdC93aC50eHQ=' )
iii1 = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby9maXhlcy9maXhlcy50eHQ=' )
oO0OOO = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby9hcHBzL2FwcHMueG1s' )
IIiIi1II1IiI = base64 . decodestring ( 'L2FkZG9ucy9uZXcudHh0' )
OoooooO0oOOoO = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby92b2Qvdm9kLnBocA==' )
IiI1O000oo0o = base64 . decodestring ( 'L2FkZG9ucy9pcHR2LnR4dA==' )
iII = base64 . decodestring ( 'L2FkZG9ucy92aWRlby50eHQ=' )
oOo0Oii = base64 . decodestring ( 'L2FkZG9ucy9zcG9ydHMudHh0' )
o00OoO00o00 = base64 . decodestring ( 'L2FkZG9ucy9raWRzLnR4dA==' )
OO0Oo00 = base64 . decodestring ( 'L2FkZG9ucy9tdXNpYy50eHQ=' )
IIIiIii111IIi = base64 . decodestring ( 'L2FkZG9ucy9wcm9ncmFtcy50eHQ=' )
II11IiIIiiiii = base64 . decodestring ( 'L2FkZG9ucy94eHgudHh0' )
OoOo00OoOO00 = base64 . decodestring ( 'L2FkZG9ucy9yZXBvLnR4dA==' )
o0Ooo0o0ooo0 = base64 . decodestring ( 'L2FkZG9ucy9wYWNrcy50eHQ=' )
I1I1oOoooo0OooO = base64 . decodestring ( 'L2FkZG9ucy9za2lucy50eHQ=' )
OO0oIII111i11IiI = base64 . decodestring ( 'L2FkZG9ucy9hcnQudHh0' )
ooOooo000OO00 = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2dvdGhhbS50eHQ=' )
oO0O = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2hlbGl4LnR4dA==' )
iIIII1i = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2lzZW5nYXJkLnR4dA==' )
IiI1I1II = base64 . decodestring ( 'L2FkZG9ucy9SU1MudHh0' )
OO0o0oO0O000o = base64 . decodestring ( 'Q1VOVA==' )
def II1I ( name , url , mode , iconimage , fanart , description , showcontext = True , allinfo = { } ) :
 O00oO0o = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 I1i1iii = True
 IiI1iI1 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 IiI1iI1 . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 IiI1iI1 . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  oO0OOo = [ ]
  if showcontext == 'fav' :
   oO0OOo . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in OOO00 :
   oO0OOo . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fanart=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , urllib . quote_plus ( fanart ) , mode ) ) )
  IiI1iI1 . addContextMenuItems ( oO0OOo )
 I1i1iii = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = O00oO0o , listitem = IiI1iI1 , isFolder = True )
 return I1i1iii
 if 67 - 67: ii + oO0o / I1ii11iIi11i % I11i % ooOoO0O00
def ooOOoooooo ( name , url , mode , iconimage , fanart , description ) :
 O00oO0o = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 I1i1iii = True
 IiI1iI1 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 IiI1iI1 . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 IiI1iI1 . setProperty ( "Fanart_Image" , fanart )
 I1i1iii = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = O00oO0o , listitem = IiI1iI1 , isFolder = False )
 return I1i1iii
 if 31 - 31: OooO0OoOOOO . IIiIiII11i % I1ii11iIi11i * Ii11Ii1I + Ii11Ii1I
 if 87 - 87: oO0o
I1i1Iii1i1II1 = o00oIiIiIiiI ( )
iIII = None
i1I1i111Ii = None
OOoOoo00Oo = None
OOOOoO00o0O = None
I1I1I1IIi1III = None
iIiIiIiI = None
I1i11i = None
if 9 - 9: IIiIiII11i + Ii1I / o0oOO0O00o0O
if 51 - 51: iI1iI1I1i1I % Ii1I + ii - oOo0O0Ooo * OOooOOo * o0oOO0O00o0O
try :
 I1i11i = int ( I1i1Iii1i1II1 [ "fav_mode" ] )
except :
 pass
 if 7 - 7: IIIii1II1II . OooO0OoOOOO . IIIi / Ii11Ii1I / I1ii11iIi11i
try :
 iIII = urllib . unquote_plus ( I1i1Iii1i1II1 [ "url" ] )
except :
 pass
try :
 i1I1i111Ii = urllib . unquote_plus ( I1i1Iii1i1II1 [ "name" ] )
except :
 pass
try :
 OOOOoO00o0O = urllib . unquote_plus ( I1i1Iii1i1II1 [ "iconimage" ] )
except :
 pass
try :
 OOoOoo00Oo = int ( I1i1Iii1i1II1 [ "mode" ] )
except :
 pass
try :
 I1I1I1IIi1III = urllib . unquote_plus ( I1i1Iii1i1II1 [ "fanart" ] )
except :
 pass
try :
 iIiIiIiI = urllib . unquote_plus ( I1i1Iii1i1II1 [ "description" ] )
except :
 pass
 if 83 - 83: iI1iI1I1i1I / I1ii11iIi11i
 if 23 - 23: iI11I1II1I1I
print str ( oOOoO0 ) + ': ' + str ( IiiIII111iI )
print "Mode: " + str ( OOoOoo00Oo )
print "URL: " + str ( iIII )
print "Name: " + str ( i1I1i111Ii )
print "IconImage: " + str ( OOOOoO00o0O )
if 10 - 10: iI1iI1I1i1I - I11i % ii - Ii1I
if 64 - 64: oO0o / oOo0O0Ooo
def iiO0o0oOOOoOo ( content , viewType ) :
 if 23 - 23: iI1iI1I1i1I * IIIi * I11i - oOo0O0Ooo % OOooOOo + I11i
 if content :
  xbmcplugin . setContent ( int ( sys . argv [ 1 ] ) , content )
 if o0oO0 . getSetting ( 'auto-view' ) == 'true' :
  xbmc . executebuiltin ( "Container.SetViewMode(%s)" % o0oO0 . getSetting ( viewType ) )
  if 41 - 41: OooO0OoOOOO * ii . O0OoO % Ii
if OOOOoO00o0O == None : OOOOoO00o0O = i1iIIi1
if I1I1I1IIi1III == None : I1I1I1IIi1III = i1iiIII111ii
if OOoOoo00Oo == None :
 ooOOO00Ooo ( )
 if 11 - 11: iI11I1II1I1I . IIIi - I1ii11iIi11i / iI1iI1I1i1I + IIiIiII11i
elif OOoOoo00Oo == 1 :
 o0O ( iIII )
 if 29 - 29: iI1iI1I1i1I . Ii + ooOoO0O00 - Ii11Ii1I + o0o00Oo0O . oOo0O0Ooo
elif OOoOoo00Oo == 44 :
 ooOoO ( iIII )
 if 8 - 8: I11i
elif OOoOoo00Oo == 2 :
 I11Ii11iI1 ( )
 if 78 - 78: ooOoO0O00 - I1ii11iIi11i
elif OOoOoo00Oo == 3 :
 o00OO00O0oOO ( )
 if 48 - 48: Ii11Ii1I - ii + IIIi % I11i - OOooOOo . oOo0O0Ooo
elif OOoOoo00Oo == 21 :
 iI1Ii11111iIi ( )
 if 42 - 42: IIIi
elif OOoOoo00Oo == 4 :
 III ( )
 if 70 - 70: I11i / iI1iI1I1i1I + OoOo00o % oOo0O0Ooo % I1ii11iIi11i + oO0o
elif OOoOoo00Oo == 5 :
 OOoOOo0O00O ( i1I1i111Ii , iIII , iIiIiIiI )
 if 80 - 80: IIIii1II1II
elif OOoOoo00Oo == 6 :
 I1ioo ( iIII )
 if 12 - 12: Ii11Ii1I
elif OOoOoo00Oo == 7 :
 III1i1iI111I1 ( iIII , i1I1i111Ii )
 if 2 - 2: ii
elif OOoOoo00Oo == 8 :
 IiIii1i ( iIII , i1I1i111Ii )
 if 100 - 100: I1ii11iIi11i / o0o00Oo0O * Ii * ii
elif OOoOoo00Oo == 9 :
 FIXREPOSADDONS ( iIII )
 if 46 - 46: o0o00Oo0O % ii
elif OOoOoo00Oo == 10 :
 i1ioOOoo00O00o ( )
 if 22 - 22: o0oOO0O00o0O + ii - OOooOOo - oO0o * IIIi - OoOo00o
elif OOoOoo00Oo == 11 :
 III11IiI ( iIII )
 if 99 - 99: O0OoO / oOo0O0Ooo . Ii11Ii1I - Ii11Ii1I * oOo0O0Ooo
elif OOoOoo00Oo == 12 :
 III111i1IIiiI ( )
 if 24 - 24: iI1iI1I1i1I * oO0o - OoOo00o / iI11I1II1I1I - I1ii11iIi11i . IIIii1II1II
elif OOoOoo00Oo == 13 :
 IiII1111I ( )
 if 2 - 2: O0OoO - o0o00Oo0O - Ii1I / iI1iI1I1i1I * OOooOOo
elif OOoOoo00Oo == 14 :
 IioooooOOo0Oo ( iIII )
 if 26 - 26: Ii1I + IIIi - OoOo00o + OooO0OoOOOO % IIIii1II1II
elif OOoOoo00Oo == 15 :
 oOo0oO ( )
 if 84 - 84: iI1iI1I1i1I % Ii11Ii1I % o0o00Oo0O * I11i
elif OOoOoo00Oo == 16 :
 Iii1iIII1Iii ( iIII , i1I1i111Ii )
 if 15 - 15: OoOo00o - iI11I1II1I1I - IIiIiII11i - OooO0OoOOOO % Ii1I
elif OOoOoo00Oo == 17 :
 i111ii1II11ii ( iIII , i1I1i111Ii )
 if 80 - 80: OooO0OoOOOO * o0oOO0O00o0O . ooOoO0O00 % Ii11Ii1I % Ii1I + O0OoO
elif OOoOoo00Oo == 18 :
 oOoOo000Ooooo ( )
 if 6 - 6: Ii1I . OoOo00o . oO0o + OooO0OoOOOO
elif OOoOoo00Oo == 19 :
 oOoOoo0 ( i1I1i111Ii , iIII , iIiIiIiI )
 if 65 - 65: Ii1I / O0OoO
elif OOoOoo00Oo == 40 :
 Iii111Ii ( i1I1i111Ii , iIII , iIiIiIiI )
 if 23 - 23: IIIii1II1II / IIIii1II1II * I11i * IIIii1II1II
elif OOoOoo00Oo == 42 :
 I11iIiI1 ( i1I1i111Ii , iIII , iIiIiIiI )
 if 57 - 57: o0oOO0O00o0O
elif OOoOoo00Oo == 43 :
 OOoOO ( i1I1i111Ii , iIII , iIiIiIiI )
 if 29 - 29: oOo0O0Ooo
elif OOoOoo00Oo == 20 :
 OooO0ooo0o ( iIII )
 if 41 - 41: IIIi * oO0o - o0oOO0O00o0O . Ii11Ii1I
elif OOoOoo00Oo == 22 :
 OO0oOo ( iIII )
 if 41 - 41: iI11I1II1I1I - o0o00Oo0O - Ii1I - OoOo00o + IIIi
elif OOoOoo00Oo == 23 :
 IiIi1I11 ( iIII )
 if 22 - 22: o0o00Oo0O % OooO0OoOOOO % o0oOO0O00o0O % oOo0O0Ooo
elif OOoOoo00Oo == 24 :
 OO0000O ( iIII )
 if 34 - 34: o0oOO0O00o0O . I1ii11iIi11i % Ii1I . o0oOO0O00o0O % OooO0OoOOOO / OooO0OoOOOO
elif OOoOoo00Oo == 25 :
 I1111iIIiIIII ( iIII )
 if 84 - 84: Ii11Ii1I
elif OOoOoo00Oo == 26 :
 o0OO0Oooo ( iIII )
 if 1 - 1: OoOo00o - I1ii11iIi11i * iI11I1II1I1I * I1ii11iIi11i * ooOoO0O00
elif OOoOoo00Oo == 27 :
 I1Iii11111I1iii ( iIII )
 if 9 - 9: o0oOO0O00o0O - o0oOO0O00o0O
elif OOoOoo00Oo == 28 :
 ooOo0Ooo0 ( iIII )
 if 3 - 3: o0o00Oo0O + o0o00Oo0O - o0o00Oo0O - o0o00Oo0O % ii + OoOo00o
elif OOoOoo00Oo == 29 :
 oOoOo00oo ( iIII )
 if 20 - 20: oO0o + iI1iI1I1i1I . IIiIiII11i / Ii
elif OOoOoo00Oo == 30 :
 II1I1iiIII1I1 ( iIII )
 if 50 - 50: ii / oO0o % iI11I1II1I1I
elif OOoOoo00Oo == 31 :
 I1Ii1IiiiII ( iIII )
 if 41 - 41: Ii1I % Ii1I + OooO0OoOOOO . o0oOO0O00o0O % IIIi * O0OoO
elif OOoOoo00Oo == 32 :
 iIi1i ( )
 if 57 - 57: Ii11Ii1I . IIIi . IIiIiII11i % ii * o0o00Oo0O + iI11I1II1I1I
elif OOoOoo00Oo == 33 :
 ooO0oO00O0o ( )
 if 94 - 94: ooOoO0O00 * oO0o * OOooOOo
elif OOoOoo00Oo == 35 :
 I11IIIiIi11 ( iIII )
 if 93 - 93: O0OoO / IIIii1II1II * o0o00Oo0O
elif OOoOoo00Oo == 34 :
 OOO0oOOo00O ( iIII )
 if 17 - 17: oO0o / O0OoO % oOo0O0Ooo
elif OOoOoo00Oo == 36 :
 i11iIIi11 ( iIII )
 if 47 - 47: I1ii11iIi11i * oO0o / I11i * oOo0O0Ooo
elif OOoOoo00Oo == 37 :
 OoOo000oOo0oo ( iIII )
 if 60 - 60: Ii1I / OooO0OoOOOO . Ii / oO0o % IIiIiII11i
elif OOoOoo00Oo == 38 :
 oOOI11I ( iIII )
 if 6 - 6: o0oOO0O00o0O % I11i + IIIi
elif OOoOoo00Oo == 41 :
 ooOOo ( I1i1Iii1i1II1 )
 if 91 - 91: I11i + o0o00Oo0O * OoOo00o * OooO0OoOOOO * Ii1I
elif OOoOoo00Oo == 39 :
 ii111Ii1i ( iIII )
 if 83 - 83: ii
elif OOoOoo00Oo == 45 :
 TEXTS ( )
 if 52 - 52: I11i / OOooOOo % OoOo00o % oO0o / OooO0OoOOOO % I11i
elif OOoOoo00Oo == 46 :
 o00oooo ( )
 if 88 - 88: IIIii1II1II / Ii / Ii11Ii1I / Ii * Ii1I % iI1iI1I1i1I
elif OOoOoo00Oo == 47 :
 GEVID ( )
 if 43 - 43: OOooOOo * oO0o % ooOoO0O00 * Ii11Ii1I + iI11I1II1I1I
elif OOoOoo00Oo == 48 :
 i1ii11 ( i1I1i111Ii , iIII , iIiIiIiI )
 if 80 - 80: I11i . o0oOO0O00o0O . ii
elif OOoOoo00Oo == 49 :
 oOOIi1II ( )
 if 63 - 63: O0OoO . IIIii1II1II
elif OOoOoo00Oo == 222 :
 I1III1111iIi ( iIII )
 if 66 - 66: oOo0O0Ooo
elif OOoOoo00Oo == 333 :
 Ii1o0OOOoo0000 ( iIII )
 if 99 - 99: oO0o % o0o00Oo0O . IIIi - Ii1I . I1ii11iIi11i / OOooOOo
 if 60 - 60: Ii1I
elif OOoOoo00Oo == 1020 :
 OOoo0 ( )
 if 78 - 78: OoOo00o + IIiIiII11i
elif OOoOoo00Oo == 1021 :
 ANIMEEP ( )
 if 55 - 55: ii
elif OOoOoo00Oo == 1022 :
 ANIMEPLAY ( iIII )
 if 90 - 90: oOo0O0Ooo
elif OOoOoo00Oo == 1001 :
 OoOoO00O ( )
 if 4 - 4: IIIii1II1II % O0OoO - IIIii1II1II - I11i
elif OOoOoo00Oo == 1005 :
 o00O0O ( )
 if 30 - 30: OooO0OoOOOO
elif OOoOoo00Oo == 1007 :
 oooOoOIiiIi1IiiiI ( iIII )
 if 34 - 34: OoOo00o - IIiIiII11i - I11i + o0oOO0O00o0O + IIIi
elif OOoOoo00Oo == 1010 :
 ooo00 ( iIII )
 if 70 - 70: ii + oO0o * I1ii11iIi11i
elif OOoOoo00Oo == 1011 :
 o00000O ( iIII )
 if 20 - 20: Ii - IIiIiII11i - O0OoO % OoOo00o . O0OoO
elif OOoOoo00Oo == 1030 :
 iIiiiII11 ( )
 if 50 - 50: iI11I1II1I1I + IIIi - iI1iI1I1i1I - ii
elif OOoOoo00Oo == 1031 :
 ooo00Oo0 ( iIII , OOOOoO00o0O )
 if 84 - 84: OOooOOo - iI1iI1I1i1I
elif OOoOoo00Oo == 1006 :
 Parse . ParseURL ( iIII )
 if 80 - 80: Ii % IIIii1II1II - I1ii11iIi11i % IIIii1II1II
elif OOoOoo00Oo == 2030 :
 Parse . addonParseURL ( iIII )
 if 89 - 89: Ii11Ii1I * iI1iI1I1i1I + OOooOOo / Ii
elif OOoOoo00Oo == 2031 :
 Parse . apkParseURL ( iIII )
 if 68 - 68: ii * iI1iI1I1i1I
elif OOoOoo00Oo == 1002 :
 oooOoo0oOO0 ( iIII )
 if 86 - 86: I11i / OOooOOo
elif OOoOoo00Oo == 1003 :
 o0o0oooO00O0 ( iIII , OOOOoO00o0O )
 if 40 - 40: o0oOO0O00o0O
elif OOoOoo00Oo == 1004 :
 iiiI ( iIII )
 if 62 - 62: O0OoO / IIIii1II1II
elif OOoOoo00Oo == 1008 :
 o00O0o ( )
 if 74 - 74: o0oOO0O00o0O % IIIi / IIIi - iI11I1II1I1I - IIiIiII11i + IIIii1II1II
elif OOoOoo00Oo == 1009 :
 M3UPLAY ( iIII )
 if 92 - 92: iI1iI1I1i1I % IIIi
elif OOoOoo00Oo == 2001 :
 OoOoO ( iIII )
 if 18 - 18: O0OoO + IIIi / IIIii1II1II / OoOo00o + iI11I1II1I1I % OooO0OoOOOO
elif OOoOoo00Oo == 1013 :
 II1IIIiiI11 ( )
 if 94 - 94: iI1iI1I1i1I
elif OOoOoo00Oo == 1014 :
 oOoo0OO0 ( )
 if 37 - 37: OoOo00o
elif OOoOoo00Oo == 1015 :
 iiIiIi1111iI1 ( iIII )
 if 52 - 52: Ii1I * oOo0O0Ooo . IIIii1II1II + ooOoO0O00 % OoOo00o / iI11I1II1I1I
elif OOoOoo00Oo == 1016 :
 III1I11Iiii ( iIII , OOOOoO00o0O , i1I1i111Ii )
 if 68 - 68: IIIi - OOooOOo . Ii + I11i
elif OOoOoo00Oo == 1023 :
 IIIii ( )
 if 71 - 71: Ii / ooOoO0O00 * oOo0O0Ooo / OOooOOo
elif OOoOoo00Oo == 1024 :
 Oo00oo00o00Oo ( )
 if 33 - 33: iI1iI1I1i1I . I1ii11iIi11i
elif OOoOoo00Oo == 1025 :
 iiiiiii11III ( iIII )
 if 89 - 89: o0oOO0O00o0O + ooOoO0O00 - OooO0OoOOOO + O0OoO . IIiIiII11i
elif OOoOoo00Oo == 4001 :
 iI1I ( )
 if 85 - 85: iI11I1II1I1I - Ii11Ii1I * I1ii11iIi11i . OoOo00o + IIIi
elif OOoOoo00Oo == 4002 :
 I11I1II ( )
 if 13 - 13: o0o00Oo0O + iI11I1II1I1I % IIiIiII11i + iI11I1II1I1I
elif OOoOoo00Oo == 4003 :
 oOOoo0o0OOOO ( )
 if 85 - 85: oOo0O0Ooo * iI11I1II1I1I . o0oOO0O00o0O / o0oOO0O00o0O
elif OOoOoo00Oo == 4004 :
 iiOOooooO0Oo ( )
 if 43 - 43: oOo0O0Ooo
elif OOoOoo00Oo == 4005 :
 oO0OOOO0 ( )
 if 78 - 78: oO0o % IIiIiII11i + OOooOOo / oOo0O0Ooo
elif OOoOoo00Oo == 4006 :
 iI1I11iiI1i ( )
 if 34 - 34: I11i % Ii1I + Ii11Ii1I * iI1iI1I1i1I / OoOo00o
elif OOoOoo00Oo == 4007 :
 oOo0O0o00o ( )
 if 18 - 18: O0OoO
elif OOoOoo00Oo == 4008 :
 o00oO0oo0OO ( )
 if 92 - 92: oO0o % iI11I1II1I1I / OooO0OoOOOO * o0oOO0O00o0O . ooOoO0O00 + OoOo00o
elif OOoOoo00Oo == 4009 : OO ( )
elif OOoOoo00Oo == 4010 : Ii1II1I11i1 ( )
elif OOoOoo00Oo == 3000 :
 OO0 ( )
 if 24 - 24: OooO0OoOOOO . o0oOO0O00o0O * OooO0OoOOOO % Ii . Ii + ooOoO0O00
elif OOoOoo00Oo == 3001 :
 IIiiiiIiI1III ( )
 if 64 - 64: iI11I1II1I1I / OooO0OoOOOO / I1ii11iIi11i - Ii1I
elif OOoOoo00Oo == 3002 :
 iIiI ( iIII )
 if 100 - 100: OooO0OoOOOO + ooOoO0O00 * oO0o
elif OOoOoo00Oo == 3003 :
 OO0OOoooo0o ( iIII )
 if 64 - 64: OoOo00o * Ii . I1ii11iIi11i
elif OOoOoo00Oo == 3004 :
 iiIIiI11II1 ( iIII )
 if 52 - 52: I1ii11iIi11i / O0OoO / o0oOO0O00o0O - I11i / o0oOO0O00o0O
elif OOoOoo00Oo == 404 :
 oOOo00ooO ( i1I1i111Ii , iIII , OOOOoO00o0O )
 if 74 - 74: ooOoO0O00 . iI11I1II1I1I
elif OOoOoo00Oo == 405 :
 IIiIIiI1iIII ( iIII )
 if 85 - 85: oOo0O0Ooo
elif OOoOoo00Oo == 7030 :
 I111Ii11i11I ( )
 if 10 - 10: o0o00Oo0O . IIiIiII11i / ii
elif OOoOoo00Oo == 7021 :
 o00o0O0 ( i1I1i111Ii )
 if 72 - 72: ii . I11i + o0o00Oo0O
elif OOoOoo00Oo == 7022 :
 iII1iiiiI1i ( i1I1i111Ii )
 if 46 - 46: OOooOOo * iI1iI1I1i1I / OoOo00o + I1ii11iIi11i + OooO0OoOOOO
elif OOoOoo00Oo == 7000 :
 O0Ooo0o ( i1I1i111Ii , iIII , img )
 if 95 - 95: I11i - Ii11Ii1I
elif OOoOoo00Oo == 7050 :
 O00 ( iIII )
 if 67 - 67: Ii1I * I1ii11iIi11i % I11i
elif OOoOoo00Oo == 7051 :
 iI1iIIII1 ( iIII )
 if 19 - 19: OOooOOo . IIIii1II1II . ii
elif OOoOoo00Oo == 7052 :
 oOOoOO0O00o ( iIII )
 if 79 - 79: IIIii1II1II * O0OoO * oOo0O0Ooo * Ii1I / Ii1I
elif OOoOoo00Oo == 7053 :
 Iii1Iii ( iIII )
 if 62 - 62: O0OoO * Ii11Ii1I % Ii1I - ooOoO0O00 - Ii1I
elif OOoOoo00Oo == 7054 :
 CoolPlay ( iIII )
 if 24 - 24: IIIii1II1II
elif OOoOoo00Oo == 7060 :
 oOOo0OO00OoO ( )
 if 71 - 71: OooO0OoOOOO - ooOoO0O00
elif OOoOoo00Oo == 7061 :
 iiII1IIii1i1 ( iIII )
 if 56 - 56: OOooOOo + OoOo00o
elif OOoOoo00Oo == 7063 :
 oOOo0oO0oOOOo ( iIII )
 if 74 - 74: o0oOO0O00o0O / IIIi / IIiIiII11i - o0oOO0O00o0O / OoOo00o % iI1iI1I1i1I
elif OOoOoo00Oo == 7062 :
 IIiiiI ( iIII )
 if 19 - 19: OooO0OoOOOO % ii + ii
elif OOoOoo00Oo == 7064 :
 NATatozcat ( )
 if 7 - 7: ooOoO0O00
elif OOoOoo00Oo == 7067 :
 ii1I ( iIII )
 if 91 - 91: OOooOOo - OOooOOo . OooO0OoOOOO
elif OOoOoo00Oo == 7066 :
 NATatozA ( iIII )
 if 33 - 33: IIIi - iI11I1II1I1I / Ii11Ii1I % o0o00Oo0O
elif OOoOoo00Oo == 7065 :
 I1iiiiIIIIIiiI11i1 ( iIII )
 if 80 - 80: OooO0OoOOOO % ii - OooO0OoOOOO
elif OOoOoo00Oo == 7070 :
 III11i1iI11 ( )
 if 27 - 27: IIIi - I11i * Ii1I - oOo0O0Ooo
elif OOoOoo00Oo == 7071 :
 DIZIlist ( iIII )
 if 22 - 22: I1ii11iIi11i % ii - I1ii11iIi11i - o0oOO0O00o0O . Ii11Ii1I
elif OOoOoo00Oo == 7072 :
 DIZIpull ( iIII )
 if 100 - 100: IIiIiII11i / IIIi / o0oOO0O00o0O - Ii1I * iI11I1II1I1I
elif OOoOoo00Oo == 7073 :
 WATCHDIZI ( iIII )
 if 7 - 7: ooOoO0O00 . OooO0OoOOOO % Ii * Ii1I . iI1iI1I1i1I % Ii1I
elif OOoOoo00Oo == 7002 :
 Oo0OOOOOOO0oo ( )
 if 35 - 35: oOo0O0Ooo
elif OOoOoo00Oo == 7003 :
 Iii1 ( iIII )
 if 48 - 48: ii % ii - oO0o . OOooOOo
elif OOoOoo00Oo == 7004 :
 Iii1II1 ( iIII )
 if 22 - 22: O0OoO . Ii . ii . ooOoO0O00
elif OOoOoo00Oo == 7020 :
 iIiiII1Ii1ii ( iIII )
 if 12 - 12: OOooOOo % IIIii1II1II + OoOo00o . o0o00Oo0O % iI11I1II1I1I
elif OOoOoo00Oo == 7001 :
 iiI11I1ii11 ( )
 if 41 - 41: ii
elif OOoOoo00Oo == 7010 :
 o00oo ( iIII )
 if 13 - 13: iI1iI1I1i1I + IIIi - IIIi % OoOo00o / iI1iI1I1i1I
elif OOoOoo00Oo == 7011 :
 OoOooO ( iIII )
 if 4 - 4: oOo0O0Ooo + IIIii1II1II - OooO0OoOOOO + o0oOO0O00o0O
elif OOoOoo00Oo == 7012 :
 oOOooI1I1i11 ( iIII )
 if 78 - 78: Ii11Ii1I
elif OOoOoo00Oo == 7013 :
 cnfTVPlay2 ( iIII )
elif OOoOoo00Oo == 7014 :
 CNF_Studio_Indexer . MV_Movies ( iIII )
elif OOoOoo00Oo == 7015 :
 CNF_Studio_Indexer . Movie_ByYear ( iIII )
elif OOoOoo00Oo == 7016 :
 CNF_Studio_Indexer . Resolve_CNF_Link ( i1I1i111Ii , iIII , OOOOoO00o0O )
elif OOoOoo00Oo == 7017 :
 CNF_Studio_Indexer . Search_Movie ( )
elif OOoOoo00Oo == 7018 :
 IiI1IIiiiii ( )
elif OOoOoo00Oo == 7019 :
 CNF_Studio_Indexer . List_Movies ( iIII )
elif OOoOoo00Oo == 7020 :
 CNF_Studio_Indexer . Get_Movie_Page ( iIII )
elif OOoOoo00Oo == 7024 :
 CNF_Studio_Indexer . Box_Office ( iIII )
 if 29 - 29: IIiIiII11i
elif OOoOoo00Oo == 8000 :
 I1I1i1I1I1I1 ( )
elif OOoOoo00Oo == 8001 :
 oo0O0oOOO0o ( )
elif OOoOoo00Oo == 8002 :
 iiII1Ii ( )
elif OOoOoo00Oo == 8003 :
 oOo000o ( )
elif OOoOoo00Oo == 8004 :
 IiI11I1Ii11II ( )
elif OOoOoo00Oo == 8005 :
 I1Io0oO0oo ( )
elif OOoOoo00Oo == 8006 :
 O0I11IIIII ( i1I1i111Ii , iIII )
elif OOoOoo00Oo == 8030 :
 Iiii11iIi1 ( iIII )
elif OOoOoo00Oo == 8045 :
 I1i ( iIII )
elif OOoOoo00Oo == 8046 :
 I11I ( iIII )
elif OOoOoo00Oo == 8047 :
 iiiiiI ( iIII )
elif OOoOoo00Oo == 8020 :
 o00o0o0oOo0 ( )
elif OOoOoo00Oo == 8021 :
 IiI1iI1I1 ( iIII )
elif OOoOoo00Oo == 8022 :
 I1IiIIiIiI ( iIII )
elif OOoOoo00Oo == 8023 :
 o0oooo ( iIII )
elif OOoOoo00Oo == 8040 :
 Ii1 ( )
elif OOoOoo00Oo == 8041 :
 oOooOOOOo0o ( iIII )
elif OOoOoo00Oo == 8042 :
 o0OOOOOo0 ( iIII )
elif OOoOoo00Oo == 8043 :
 yt . PlayVideo ( iIII )
elif OOoOoo00Oo == 8044 :
 oooOoO ( iIII )
elif OOoOoo00Oo == 8060 :
 Ii1iiI1 ( )
elif OOoOoo00Oo == 8061 :
 o0ooOOoO0oO0 ( iIII )
elif OOoOoo00Oo == 8064 :
 OOoO0OOoO0ooo ( )
elif OOoOoo00Oo == 8065 :
 ii11i1ii1 ( iIII )
elif OOoOoo00Oo == 8070 :
 iI1i ( )
elif OOoOoo00Oo == 8071 :
 i11I ( iIII )
elif OOoOoo00Oo == 7080 :
 o0oO0o0oo0O0 ( iIII )
elif OOoOoo00Oo == 8090 :
 ooOOo00 ( )
elif OOoOoo00Oo == 8091 :
 IIii1i1IiIi1 ( iIII )
elif OOoOoo00Oo == 8092 :
 IiiiiIIi11iI ( iIII )
elif OOoOoo00Oo == 8081 :
 I11IiI1i ( )
elif OOoOoo00Oo == 8062 :
 iiIiI11IiI1ii ( iIII )
elif OOoOoo00Oo == 8063 :
 o0oOooO0oo00 ( iIII )
elif OOoOoo00Oo == 8050 :
 OO00OOoO0o ( )
elif OOoOoo00Oo == 8051 :
 Iiiiiii1 ( iIII )
elif OOoOoo00Oo == 8052 :
 oOO0oo ( iIII )
elif OOoOoo00Oo == 8085 :
 Ooo000O00 ( )
elif OOoOoo00Oo == 8086 :
 o0O0 ( iIII )
elif OOoOoo00Oo == 8087 :
 iio0o000Oo ( iIII )
elif OOoOoo00Oo == 8088 :
 oO0o0O0o0OO00 ( iIII , i1I1i111Ii )
elif OOoOoo00Oo == 9000 :
 OO00 ( )
elif OOoOoo00Oo == 1111 :
 oOooOOOO0oOo ( )
elif OOoOoo00Oo == 9001 :
 oO0OIIIiIi1iiI ( )
elif OOoOoo00Oo == 9002 :
 o0OO0OO000OO ( )
elif OOoOoo00Oo == 9003 :
 i1iIOo ( )
elif OOoOoo00Oo == 50 :
 iI111i1I1II ( iIII )
elif OOoOoo00Oo == 9020 :
 champlist ( )
elif OOoOoo00Oo == 9021 :
 oOo ( )
elif OOoOoo00Oo == 9022 :
 OOOOoO0 ( )
elif OOoOoo00Oo == 9023 :
 IiiIiIIi1 ( )
elif OOoOoo00Oo == 9024 :
 IIiiIii11 ( iIII )
elif OOoOoo00Oo == 9030 :
 I1iO0o0O0OooOoo ( iIII )
elif OOoOoo00Oo == 9031 :
 IiII1i11III ( iIII )
elif OOoOoo00Oo == 9032 :
 i1II1IIIII ( iIII )
elif OOoOoo00Oo == 9033 :
 iIii1ii ( iIII )
elif OOoOoo00Oo == 7085 :
 iIiiI111I11 ( iIII )
elif OOoOoo00Oo == 7086 :
 o00O0 ( iIII )
elif OOoOoo00Oo == 7087 :
 o0OOOO ( iIiIiIiI )
elif OOoOoo00Oo == 9666 :
 iioOo00O0o ( iIII )
elif OOoOoo00Oo == 10100 : iiI1ii111 ( )
elif OOoOoo00Oo == 10105 : I1111ii11IIII ( iIII )
elif OOoOoo00Oo == 10106 : iI1Iii11i1 ( iIII )
elif OOoOoo00Oo == 10104 : iIIIII1iI ( iIII )
elif OOoOoo00Oo == 10107 : IiI ( )
elif OOoOoo00Oo == 10103 : i1IiI1Iiii ( iIII )
elif OOoOoo00Oo == 10108 : iiI ( iIII )
elif OOoOoo00Oo == 10107 : IiI ( )
elif OOoOoo00Oo == 10000 : Origin_Menu ( )
elif OOoOoo00Oo == 10001 : IiI1ii1Ii ( )
elif OOoOoo00Oo == 10002 : iII1i1IIiI1I ( )
elif OOoOoo00Oo == 10003 : iIi1iIIIiIiI ( )
elif OOoOoo00Oo == 10004 : Ooo0 ( iIII )
elif OOoOoo00Oo == 10005 : I1I1 ( )
elif OOoOoo00Oo == 10006 : Oo0Oo00o00oO ( iIII )
elif OOoOoo00Oo == 10007 : I1i111IiIiIi1 ( iIII , OOOOoO00o0O )
elif OOoOoo00Oo == 10008 : o0iIIIIi ( )
elif OOoOoo00Oo == 10009 : iIII11Iiii1 ( )
elif OOoOoo00Oo == 10010 : o0OoO0OOoO0Oo0 ( iIII )
elif OOoOoo00Oo == 10011 : IiiI11I1IIiI ( iIII )
elif OOoOoo00Oo == 10012 : oo0000o ( iIII )
elif OOoOoo00Oo == 10013 : oOoO0OOO00O ( iIII )
elif OOoOoo00Oo == 10014 : iI1IiiiI11 ( )
elif OOoOoo00Oo == 10015 : III1I ( )
elif OOoOoo00Oo == 10016 : i1iii11 ( iIII )
elif OOoOoo00Oo == 10017 : I1I1iII1i ( )
elif OOoOoo00Oo == 10018 : iIi11i ( )
elif OOoOoo00Oo == 10019 : oOO0OO0oOO ( )
elif OOoOoo00Oo == 10020 : iiiii1I1III1 ( )
elif OOoOoo00Oo == 10021 : i1I1i ( )
elif OOoOoo00Oo == 10022 : ooo0O0o0OoOO ( iIII )
elif OOoOoo00Oo == 10023 : oOOoO ( i1I1i111Ii , iIII )
elif OOoOoo00Oo == 10024 : iiiO0 ( iIII )
elif OOoOoo00Oo == 10025 : ooo0oo ( )
elif OOoOoo00Oo == 10026 : iIii11iI1II ( )
elif OOoOoo00Oo == 10027 : IiIi1III ( )
elif OOoOoo00Oo == 10028 : oO0O0oO0 ( )
elif OOoOoo00Oo == 10029 : OOOoo0ooOo00O ( )
elif OOoOoo00Oo == 423 : O0o0O0OO0o ( iIII )
elif OOoOoo00Oo == 426 : I1I11IiiI ( iIII )
elif OOoOoo00Oo == 10030 : Izle_Films ( )
elif OOoOoo00Oo == 10031 : Latest_Izle_Movies ( )
elif OOoOoo00Oo == 10032 : Izle_Genres ( )
elif OOoOoo00Oo == 10033 : Izle_Pop_Movies ( )
elif OOoOoo00Oo == 10034 : Izle_Boxsets ( )
elif OOoOoo00Oo == 10035 : Izle_Search ( )
elif OOoOoo00Oo == 10036 : Izle_Genres_Movie ( iIII )
elif OOoOoo00Oo == 10037 : Izle_Boxset_single ( iIII )
elif OOoOoo00Oo == 10038 : Izle_IFRAME ( )
elif OOoOoo00Oo == 10039 : Izle_Boxsets_Next ( iIII )
elif OOoOoo00Oo == 10040 : i11Iii1Ii1i1 ( )
elif OOoOoo00Oo == 10041 : i11i11II11i ( iIII )
elif OOoOoo00Oo == 10042 : i111i1I1ii1i ( iIII )
elif OOoOoo00Oo == 10043 : II1Iiii11111 ( )
elif OOoOoo00Oo == 10044 : OOooOooo0OOo0 ( iIII )
elif OOoOoo00Oo == 10045 : III1III11II ( i1I1i111Ii )
elif OOoOoo00Oo == 10046 : o0o ( iIII )
elif OOoOoo00Oo == 10047 : OoOOoooO000 ( iIII )
elif OOoOoo00Oo == 10048 : i11i11II11i1 ( iIII )
elif OOoOoo00Oo == 10049 : I1I1i1i ( iIII )
elif OOoOoo00Oo == 10050 : iIiOo ( )
elif OOoOoo00Oo == 10051 : iI1IIi ( )
elif OOoOoo00Oo == 10052 : O00O0 ( )
elif OOoOoo00Oo == 10053 : Addon ( iIII )
elif OOoOoo00Oo == 10054 : ooOooOooOOO ( iIII , i1I1i111Ii )
elif OOoOoo00Oo == 10055 :
 Oo00ooO0OoOo ( "addFavorite" )
 try :
  i1I1i111Ii = i1I1i111Ii . split ( '\\ ' ) [ 1 ]
 except :
  pass
 try :
  i1I1i111Ii = i1I1i111Ii . split ( '  - ' ) [ 0 ]
 except :
  pass
 oO00OoOo ( i1I1i111Ii , iIII , OOOOoO00o0O , I1I1I1IIi1III , I1i11i )
elif OOoOoo00Oo == 10056 :
 Oo00ooO0OoOo ( "rmFavorite" )
 try :
  i1I1i111Ii = i1I1i111Ii . split ( '\\ ' ) [ 1 ]
 except :
  pass
 try :
  i1I1i111Ii = i1I1i111Ii . split ( '  - ' ) [ 0 ]
 except :
  pass
 iii ( i1I1i111Ii )
elif OOoOoo00Oo == 10057 :
 Oo00ooO0OoOo ( "getFavorites" )
 IiI1 ( )
elif OOoOoo00Oo == 10058 : iiI1I1 ( )
elif OOoOoo00Oo == 10059 : Donators_Guide ( )
elif OOoOoo00Oo == 10060 : iIi1i1iIi1iI ( )
elif OOoOoo00Oo == 10061 : IIIii1 ( )
elif OOoOoo00Oo == 10062 : OO0oOOoo ( i1I1i111Ii , iIII , iIiIiIiI )
elif OOoOoo00Oo == 10063 : iiIi1i ( )
elif OOoOoo00Oo == 10064 : iIIIiiI1i1i ( )
elif OOoOoo00Oo == 10065 : oOo0O ( iIII )
elif OOoOoo00Oo == 10066 : Ii11 ( iIII )
elif OOoOoo00Oo == 10068 : ii1 ( iIII )
elif OOoOoo00Oo == 10069 : i1i11I11 ( iIII )
elif OOoOoo00Oo == 10070 : I1i11 ( iIII )
elif OOoOoo00Oo == 10071 : Genie_Watch ( )
elif OOoOoo00Oo == 10072 : Oo0OO ( )
elif OOoOoo00Oo == 10073 : I1II1 ( iIII )
elif OOoOoo00Oo == 10074 : oo00OO0000oO ( iIII )
elif OOoOoo00Oo == 10075 : ooO000OO0O00O ( OOOOoO00o0O , i1I1i111Ii , iIII )
elif OOoOoo00Oo == 10076 : i1iI ( iIII )
elif OOoOoo00Oo == 10077 : o0oooOO00 ( iIII )
elif OOoOoo00Oo == 10078 : iiI11ii1I1 ( )
elif OOoOoo00Oo == 10079 : Genie_Watch_Tv_Shows ( )
elif OOoOoo00Oo == 10080 : Genie_Watch_Tv_Genre ( iIII )
elif OOoOoo00Oo == 10081 : Genie_Watch_TV_PlayRun ( iIII )
elif OOoOoo00Oo == 10082 : Genie_Watch_TV_Episodes ( iIII , OOOOoO00o0O )
elif OOoOoo00Oo == 10083 : Genie_Watch_Tv_Recent ( iIII )
elif OOoOoo00Oo == 10084 : iiI1Ii1iI1 ( )
elif OOoOoo00Oo == 10085 : oo00O00oO ( )
elif OOoOoo00Oo == 10086 : oo0OOo ( )
elif OOoOoo00Oo == 20000 : i1i1 ( )
elif OOoOoo00Oo == 20001 : iiIIi1 ( )
elif OOoOoo00Oo == 20002 : O0Oo0Ooo ( iIII )
elif OOoOoo00Oo == 20003 : O0iI ( iIII )
elif OOoOoo00Oo == 20004 : oOOo0oo0o0o0 ( iIII )
elif OOoOoo00Oo == 21004 : o0OooooOoOO ( )
elif OOoOoo00Oo == 21005 : i1i1IIIIIIIi ( iIII )
elif OOoOoo00Oo == 21006 : OO0oOOo0o ( iIII )
elif OOoOoo00Oo == 21007 : iiI1I1IIi11i1 ( iIII )
elif OOoOoo00Oo == 30000 : I111I11I111 ( )
elif OOoOoo00Oo == 30001 : ooO00O00oOO ( )
elif OOoOoo00Oo == 10012 : Resolve ( iIII )
elif OOoOoo00Oo == 30003 : oOOII1i11i1iIi11 ( )
elif OOoOoo00Oo == 30004 : oo00ooOoo ( iIII )
elif OOoOoo00Oo == 30005 : iIIIiiiI11I ( iIII )
elif OOoOoo00Oo == 30006 : iIiI1iiiI1ii ( )
elif OOoOoo00Oo == 30007 : OO00o ( )
elif OOoOoo00Oo == 30008 : iiiII ( iIII )
elif OOoOoo00Oo == 30009 : OOOo ( iIII )
elif OOoOoo00Oo == 30010 : iIiI1 ( iIII )
elif OOoOoo00Oo == 30011 : o0o000 ( )
elif OOoOoo00Oo == 30012 : iii11II1I ( )
elif OOoOoo00Oo == 30013 : II1iiIiIiI ( )
elif OOoOoo00Oo == 30014 : o0O0ooOOoO ( )
if 79 - 79: iI11I1II1I1I - Ii + O0OoO - IIiIiII11i . iI11I1II1I1I
xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
