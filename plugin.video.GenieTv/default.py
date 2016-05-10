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
IiiIII111iI = "2.8.2"
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
i1iIIi1 = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + I1i1iiI1 , 'icon.png' , i1iiIII111ii , '' ) )
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
I11i1 = os . path . join ( O00o0OO , 'favorites' )
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
def o0oo0oOo ( ) :
 if 89 - 89: OOooOOo
 OO0oOoOO0oOO0 = oO0OOoo0OO ( i1111 ( 'aHR0cHM6Ly9naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvYmxvYi9tYXN0ZXIvVmVyc2lvbl9Mb2cudHh0' ) )
 O0 = open ( oOoOooOo0o0 ) . read ( )
 ii1ii1ii = open ( OOOO ) . read ( )
 if 91 - 91: OooO0OoOOOO
 iiIii = re . compile ( 'version="(.+?)" provider' ) . findall ( O0 )
 ooo0O = re . compile ( 'version="(.+?)" provider-name' ) . findall ( ii1ii1ii )
 oOoO0o00OO0 = re . compile ( 'GENIE TV ADDON - Version = &quot;(.+?)&quot;' ) . findall ( OO0oOoOO0oOO0 )
 i1I1ii = re . compile ( 'GENIE TV REPO - Version = &quot;(.+?)&quot;' ) . findall ( OO0oOoOO0oOO0 )
 for oOOo0 in iiIii :
  oo00O00oO = oOOo0
  for iIiIIIi in oOoO0o00OO0 :
   if not iIiIIIi == oo00O00oO :
    Oo0oO0ooo . create ( 'Incorrect Addon Version' , 'Downloading Correct Version' , )
    xbmc . sleep ( 1000 )
    Oo0oO0ooo . close
    ooo00OOOooO ( )
   if iIiIIIi == oo00O00oO :
    pass
 for O00OOOoOoo0O in ooo0O :
  O000OOo00oo = O00OOOoOoo0O
  for oo0OOo in i1I1ii :
   if not oo0OOo == O000OOo00oo :
    Oo0oO0ooo . create ( 'Incorrect Repo Installed' , 'Installing Correct Version' , '' )
    xbmc . sleep ( 1000 )
    Oo0oO0ooo . close
    ooOOO00Ooo ( )
   if oo0OOo == O000OOo00oo :
    xbmc . sleep ( 100 )
    pass
def IiIIIi1iIi ( ) :
 O0O0O0OoOO ( )
 ooOOoooooo ( )
 O00O0oOO00O00 ( )
 II1I ( )
 O0i1II1Iiii1I11 ( '[COLORgreen]Force Genie Update Kodi 16+[/COLOR]' , i1111 ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVwby9yZXBvc2l0b3J5LkdlbmllVHYtMC4xLjAuemlw' ) , 10085 , ooOooo000oOO + 'updategenie.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'My Build' ) == 'true' :
  IIII ( '[COLORgreen]WIZARD[/COLOR]' , str ( Ii1iIiII1ii1 ) , 4001 , ooOooo000oOO + 'MB.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Streams' ) == 'true' :
  IIII ( '[COLORgreen]STREAMS[/COLOR]' , str ( Ii1iIiII1ii1 ) , 4002 , ooOooo000oOO + 'streams.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Music' ) == 'true' :
  IIII ( '[COLORgreen]Music[/COLOR]' , str ( Ii1iIiII1ii1 ) , 4003 , ooOooo000oOO + 'MUSIC.png' , i1iiIII111ii , '' )
  if 32 - 32: ii / iI11I1II1I1I - I11i
 if o0oO0 . getSetting ( 'Builders Toolbox' ) == 'true' :
  IIII ( '[COLORgreen]BUILDERS TOOLBOX[/COLOR]' , str ( Ii1iIiII1ii1 ) , 32 , ooOooo000oOO + 'builderstoolbox.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Source List' ) == 'true' :
  IIII ( '[COLORgreen]SOURCE LIST[/COLOR]' , str ( Ii1iIiII1ii1 ) , 46 , ooOooo000oOO + 'sources.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Maintainance' ) == 'true' :
  IIII ( '[COLORgreen]MAINTENANCE[/COLOR]' , str ( Ii1iIiII1ii1 ) , 3 , ooOooo000oOO + 'MAIN6.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Addons' ) == 'true' :
  IIII ( '[COLORgreen]ADDONS[/COLOR]' , '' , 10050 , ooOooo000oOO + 'ADDONS.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'APK Tool' ) == 'true' :
  IIII ( '[COLORgreen]APK TOOL[/COLOR]' , str ( Ii1iIiII1ii1 ) , 2 , ooOooo000oOO + 'APK.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Rss Feed' ) == 'true' :
  IIII ( '[COLORgreen]GenieTv RSS Feed[/COLOR]' , str ( Ii1iIiII1ii1 ) , 39 , ooOooo000oOO + 'RSS.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Addons Packs' ) == 'true' :
  IIII ( '[COLORgreen]ADDONS PACKS[/COLOR]' , str ( Ii1iIiII1ii1 ) , 30 , ooOooo000oOO + 'ADDONP.png' , i1iiIII111ii , '' )
 o00oooO0Oo ( 'movies' , 'MAIN' )
 if 78 - 78: Ii11Ii1I % IIIi + Ii1I
def OOooOoooOoOo ( ) :
 O0O0O0OoOO ( )
 IIII ( '[COLORgreen]BACKUP MY BUILD[/COLOR]' , str ( Ii1iIiII1ii1 ) , 10060 , ooOooo000oOO + 'MB.png' , i1iiIII111ii , '' )
 IIII ( '[COLORgreen]RESTORE MY BUILD[/COLOR]' , str ( Ii1iIiII1ii1 ) , 49 , ooOooo000oOO + 'MB.png' , i1iiIII111ii , '' )
 IIII ( '[COLORgreen]WIPE GENIE[/COLOR]' , str ( Ii1iIiII1ii1 ) , 41 , ooOooo000oOO + 'wipegenie.png' , i1iiIII111ii , '' )
 IIII ( '[COLORgreen]WISHES PC[/COLOR]' , str ( Ii1iIiII1ii1 ) , 1 , ooOooo000oOO + 'WISHESPC.png' , i1iiIII111ii , '' )
 IIII ( '[COLORgreen]WISHES ANDROID[/COLOR]' , str ( Ii1iIiII1ii1 ) , 44 , ooOooo000oOO + 'WISHESAN.png' , i1iiIII111ii , '' )
 o00oooO0Oo ( 'movies' , 'MAIN' )
def o0OOOO00O0Oo ( ) :
 O0O0O0OoOO ( )
 if oO == '5knuckleshuffle' :
  IIII ( '[COLORgreen]XVID[/COLOR]' , str ( Ii1iIiII1ii1 ) , 10100 , ooOooo000oOO + 'JIZBOX.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Favourites' ) == 'true' :
  IIII ( '[COLORgreen]FAVOURITES[/COLOR]' , str ( Ii1iIiII1ii1 ) , 10057 , ooOooo000oOO + 'FAVORITES.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Search' ) == 'true' :
  IIII ( '[COLORgreen]SEARCH[/COLOR]' , str ( Ii1iIiII1ii1 ) , 9000 , ooOooo000oOO + 'search.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'TV GUIDE' ) == 'true' :
  O0i1II1Iiii1I11 ( '[COLORgreen]TV GUIDE[/COLOR]' , '' , 10063 , ooOooo000oOO + 'GTVIPTV.png' , i1iiIII111ii , '' )
 IIII ( '[COLORgreen]MOVIES[/COLOR]' , str ( Ii1iIiII1ii1 ) , 4004 , ooOooo000oOO + 'MOVIESv.png' , i1iiIII111ii , '' )
 IIII ( '[COLORgreen]TV SHOWS[/COLOR]' , str ( Ii1iIiII1ii1 ) , 4005 , ooOooo000oOO + 'TVSHOWSv.png' , i1iiIII111ii , '' )
 IIII ( '[COLORgreen]STREAM TEAM[/COLOR]' , str ( Ii1iIiII1ii1 ) , 4006 , ooOooo000oOO + 'streamteam.png' , i1iiIII111ii , '' )
 IIII ( '[COLORgreen]KIDS[/COLOR]' , str ( Ii1iIiII1ii1 ) , 4007 , ooOooo000oOO + 'KIDSv.png' , i1iiIII111ii , '' )
 IIII ( '[COLORgreen]HOBBIES[/COLOR]' , str ( Ii1iIiII1ii1 ) , 4008 , ooOooo000oOO + 'hobbies.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'YOUTUBE' ) == 'true' :
  IIII ( '[COLORgreen]SEARCH YOUTUBE[/COLOR]' , str ( Ii1iIiII1ii1 ) , 10064 , ooOooo000oOO + 'youtube.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'REQUESTS' ) == 'true' :
  IIII ( '[COLORgreen]REQUESTS[/COLOR]' , str ( Ii1iIiII1ii1 ) + ( i1111 ( 'L1JFUVVFU1RTLnBocA==' ) ) , 10066 , ooOooo000oOO + 'requests.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Stand Up' ) == 'true' :
  IIII ( '[COLORgreen]STAND UP[/COLOR]' , '' , 10003 , ooOooo000oOO + 'ORIGINSTANDUP.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Documentaries' ) == 'true' :
  IIII ( '[COLORgreen]DOCUMENTARIES[/COLOR]' , str ( Ii1iIiII1ii1 ) , 8040 , ooOooo000oOO + 'documentary.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Disclose' ) == 'true' :
  IIII ( '[COLORgreen]DISCLOSE TV[/COLOR]' , str ( Ii1iIiII1ii1 ) , 7001 , ooOooo000oOO + 'disclose.png' , i1iiIII111ii , '' )
  if 48 - 48: o0o00Oo0O
  if 11 - 11: iI1iI1I1i1I + ii - oO0o / I11i + I1ii11iIi11i . IIiIiII11i
 if o0oO0 . getSetting ( 'Playlist Loader' ) == 'true' :
  IIII ( '[COLORgreen]PLAYLIST LOADER[/COLOR]' , str ( Ii1iIiII1ii1 ) , 3000 , ooOooo000oOO + 'loader.png' , i1iiIII111ii , '' )
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
  if 95 - 95: oOo0O0Ooo + Ii
 o00oooO0Oo ( 'movies' , 'MAIN' )
 if 6 - 6: O0OoO / Ii + o0oOO0O00o0O * OoOo00o
def ooOOoooooo ( ) :
 if not os . path . exists ( iiI1IiI ) :
  o00o0 ( 'Change Log 01/05/16 - v2.7.9' , 'Fixing Tv Guide Link Button, should have full pics and most channels showing data in guide now \n\n\nAlso taken a bad source out of movie search and added progress bars so wait time doesnt seem so long' )
  os . makedirs ( iiI1IiI )
  if 45 - 45: o0o00Oo0O
  if 26 - 26: iI1iI1I1i1I - iI11I1II1I1I - oOo0O0Ooo / oO0o . OOooOOo % iI11I1II1I1I
def OO ( ) :
 O0O0O0OoOO ( )
 IIII ( '[COLORgreen]SEARCH MOVIES[/COLOR]' , str ( Ii1iIiII1ii1 ) , 9001 , ooOooo000oOO + 'search.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Popcorn Box' ) == 'true' :
  IIII ( '[COLORgreen]POPCORN BOX[/COLOR]' , str ( Ii1iIiII1ii1 ) , 7061 , ooOooo000oOO + 'popcorn.png' , i1iiIII111ii , '' )
 IIII ( '[COLORgreen]Film Trailers[/COLOR]' , i1111 ( 'aHR0cDovL3RoZW1vdmllYm94Lm5ldC9leHBsb3Jl' ) , 10068 , ooOooo000oOO + 'movietrailers.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'CLASSIC MOVIES' ) == 'true' :
  IIII ( '[COLORgreen]CLASSIC MOVIES[/COLOR]' , '' , 8060 , ooOooo000oOO + 'classicmovies.png' , i1iiIII111ii , '' )
 o00oooO0Oo ( 'movies' , 'MAIN' )
def iIiIIi1 ( ) :
 O0O0O0OoOO ( )
 if o0oO0 . getSetting ( 'G-tv' ) == 'true' :
  IIII ( '[COLORgreen]G-Tv PRIVATE LIST[/COLOR]' , '' , 10058 , ooOooo000oOO + 'GTVIPTV.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'TV GUIDE' ) == 'true' :
  O0i1II1Iiii1I11 ( '[COLORgreen]TV GUIDE[/COLOR]' , '' , 10063 , ooOooo000oOO + 'GTVIPTV.png' , i1iiIII111ii , '' )
 O0i1II1Iiii1I11 ( '[COLORgreen]Link GTV Donators Username and Password to Guide[/COLOR]' , '' , 4010 , ooOooo000oOO + 'GTVIPTV.png' , i1iiIII111ii , '' )
 if 7 - 7: O0OoO - I1ii11iIi11i - OoOo00o + O0OoO
 if 26 - 26: Ii11Ii1I
def I11iiI1i1 ( ) :
 O0O0O0OoOO ( )
 IIII ( '[COLORgreen]SEARCH SERIES[/COLOR]' , str ( Ii1iIiII1ii1 ) , 9002 , ooOooo000oOO + 'search.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Dizzy Tv' ) == 'true' :
  IIII ( '[COLORgreen]DIZZY TV[/COLOR]' , '' , 10018 , ooOooo000oOO + 'dtv.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Watch Series' ) == 'true' :
  IIII ( '[COLORgreen]WATCH SERIES[/COLOR]' , '' , 10040 , ooOooo000oOO + 'WATCHSERIES.png' , i1iiIII111ii , '' )
 IIII ( '[COLORgreen]iWATCH SERIES[/COLOR]' , '' , 8020 , ooOooo000oOO + 'iwatch.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Recent Episodes' ) == 'true' :
  IIII ( '[COLORgreen]RECENT EPISODES[/COLOR]' , str ( Ii1iIiII1ii1 ) , 8081 , ooOooo000oOO + 'recent.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'CLASSIC TV' ) == 'true' :
  IIII ( '[COLORgreen]CLASSIC TV[/COLOR]' , str ( Ii1iIiII1ii1 ) , 8064 , ooOooo000oOO + 'classictv.png' , i1iiIII111ii , '' )
 IIII ( '[COLORgreen]TV Show Trailers[/COLOR]' , i1111 ( 'aHR0cHM6Ly93d3cueW91dHViZS5jb20vd2F0Y2g/dj03WkZJUzJBcUF6OCZsaXN0PVBMM2t4NWgyVHJZR3dwVzBWYk5lbnBqLUJLTUJUR2dKUEU=' ) , 10069 , ooOooo000oOO + 'tvtrailers.png' , i1iiIII111ii , '' )
 IIII ( '[COLORgreen]TV Show Schedule[/COLOR]' , i1111 ( 'aHR0cDovL3d3dy5wb2dkZXNpZ24uY28udWsvY2F0Lw==' ) , 10070 , ooOooo000oOO + 'tvschedule.png' , i1iiIII111ii , '' )
 o00oooO0Oo ( 'movies' , 'MAIN' )
def I1i1Iiiii ( ) :
 O0O0O0OoOO ( )
 if o0oO0 . getSetting ( 'Scooby Streams' ) == 'true' :
  IIII ( '[COLORgreen]SCOOBY STREAMS[/COLOR]' , str ( Ii1iIiII1ii1 ) , 1023 , ooOooo000oOO + 'scoob.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'The Reaper' ) == 'true' :
  IIII ( '[COLORgreen]THE REAPER[/COLOR]' , ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9UaGVfUmVhcGVyL21haW4ucGhw' ) ) , 1016 , ooOooo000oOO + 'reap.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Pandoras Box' ) == 'true' :
  IIII ( '[COLORgreen]PANDORAS BOX[/COLOR]' , str ( Ii1iIiII1ii1 ) , 10025 , ooOooo000oOO + 'PANDORASBOX.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'HeroVision' ) == 'true' :
  IIII ( '[COLORgreen]HEROVISION[/COLOR]' , ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC9tYWluLnBocA==' ) ) , 1016 , ooOooo000oOO + 'hero.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Silent Hunter' ) == 'true' :
  IIII ( '[COLORgreen]SILENT HUNTER[/COLOR]' , ( i1111 ( 'aHR0cDovLzUuMTM1LjIwNy45Ni8=' ) ) , 10084 , ooOooo000oOO + 'SILENTHUNTER.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Redemption Streams' ) == 'true' :
  IIII ( '[COLORgreen]Redemption Streams[/COLOR]' , ( i1111 ( 'aHR0cDovL3JlZGVtcHRpb25idWlsZC4xNm1iLmNvbS9SZWRlbXB0aW9uL21haW4ucGhw' ) ) , 1016 , ooOooo000oOO + 'redemption.png' , i1iiIII111ii , '' )
 IIII ( '[COLORgreen]ITV[/COLOR]' , ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9pVHZfU3RyZWFtcy9tYWluLnBocA==' ) ) , 1016 , ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9pVHZfU3RyZWFtcy9pdHZzdHJlYW1zLnBuZw==' ) ) , i1iiIII111ii , '' )
 o00oooO0Oo ( 'movies' , 'MAIN' )
 if 94 - 94: I11i * Ii11Ii1I / I1ii11iIi11i / Ii11Ii1I
def oO0O0OO0O ( ) :
 O0O0O0OoOO ( )
 IIII ( '[COLORgreen]SILENT HUNTER[/COLOR]' , ( i1111 ( 'aHR0cDovLzUuMTM1LjIwNy45Ni8=' ) ) , 1006 , ooOooo000oOO + 'SILENTHUNTER.png' , i1iiIII111ii , '' )
 IIII ( '[COLORgreen]SILENT HUNTER SCRAPES[/COLOR]' , ( i1111 ( 'aHR0cDovLzUuMTM1LjIwNy45Ni9TY3JhcGVzL21haW4ucGhw' ) ) , 1016 , ooOooo000oOO + 'SILENTHUNTER.png' , i1iiIII111ii , '' )
 if 81 - 81: OoOo00o . I11i % o0o00Oo0O / oOo0O0Ooo - OoOo00o
 if 43 - 43: Ii + I1ii11iIi11i * IIiIiII11i * IIIi * o0o00Oo0O
 if 64 - 64: IIIii1II1II % iI11I1II1I1I * OoOo00o
def o0iI11I1II ( ) :
 O0O0O0OoOO ( )
 IIII ( '[COLORgreen]SEARCH CARTOONS[/COLOR]' , '' , 10005 , ooOooo000oOO + 'search.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'WCO' ) == 'true' :
  IIII ( '[COLORgreen]WATCH CARTOONS ONLINE[/COLOR]' , str ( Ii1iIiII1ii1 ) , 21004 , ooOooo000oOO + 'watchcartoons.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Cartoons' ) == 'true' :
  IIII ( '[COLORgreen]CARTOONS[/COLOR]' , '' , 10001 , ooOooo000oOO + 'ORIGINCARTOON.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Anime' ) == 'true' :
  IIII ( '[COLORgreen]AnimeLand[/COLOR]' , ( i1111 ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2R1YmJlZC1hbmltZQ==' ) ) , 10004 , ooOooo000oOO + 'anime.png' , i1iiIII111ii , '' )
 o00oooO0Oo ( 'movies' , 'MAIN' )
def Ii1IIiI1i ( ) :
 O0O0O0OoOO ( )
 if o0oO0 . getSetting ( 'Football' ) == 'true' :
  IIII ( '[COLORgreen]FOOTBALL[/COLOR]' , '' , 10002 , ooOooo000oOO + 'ORIGINFOOTBALL.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Fitness' ) == 'true' :
  IIII ( '[COLORgreen]FITNESS[/COLOR]' , ( i1111 ( 'aHR0cHM6Ly93d3cuZml0bmVzc2JsZW5kZXIuY29tL3ZpZGVvcw==' ) ) , 7085 , ooOooo000oOO + 'FITNESS.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Go Fishing' ) == 'true' :
  IIII ( '[COLORgreen]Go Fishing[/COLOR]' , str ( Ii1iIiII1ii1 ) , 8090 , ooOooo000oOO + 'gofish.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'GenieTv Kitchen' ) == 'true' :
  IIII ( '[COLORgreen]GenieTv Kitchen[/COLOR]' , ( i1111 ( 'aHR0cDovL2Zvb2QubmR0di5jb20vdmlkZW9z' ) ) , 8045 , ooOooo000oOO + 'geniekitchen.png' , i1iiIII111ii , '' )
 o00oooO0Oo ( 'movies' , 'MAIN' )
 if 92 - 92: OooO0OoOOOO . OooO0OoOOOO + oO0o
 if 9 - 9: oOo0O0Ooo * o0o00Oo0O + OooO0OoOOOO - iI1iI1I1i1I * IIIi
 if 64 - 64: iI11I1II1I1I - iI11I1II1I1I / Ii % I1ii11iIi11i - o0oOO0O00o0O
def II1I ( ) :
 o00OO00OoO = oO0OOoo0OO ( 'http://architects.x10host.com/wizarddelete.txt' )
 iiIii = re . compile ( '<unwanted_wizard =(.+?)</unwanted_wizard>' ) . findall ( o00OO00OoO )
 for Oo0 in iiIii :
  print Oo0
  Oo0 = ( str ( Oo0 ) )
  if os . path . exists ( xbmc . translatePath ( Oo0 ) ) :
   O0o0OO0O00O = os . path . join ( o0 , 'guisettings.xml' )
   I1iiiii = open ( O0o0OO0O00O , "w+" )
   if 71 - 71: OooO0OoOOOO * IIiIiII11i * OoOo00o
   I1iiiii . write ( r'.' )
   oOOo0II1I1iiIII ( )
  else :
   pass
   if 77 - 77: OOooOOo - IIiIiII11i - O0OoO
def O00O0oOO00O00 ( ) :
 o00OO00OoO = oO0OOoo0OO ( 'http://genietv.co.uk/genietv_art/testdelete.txt' )
 iiIii = re . compile ( '<unwanted_addon =(.+?)</unwanted_addon>' ) . findall ( o00OO00OoO )
 for o0ooO in iiIii :
  o0ooO = ( str ( o0ooO ) )
  if os . path . exists ( xbmc . translatePath ( o0ooO ) ) :
   IiiiIIiIi1 = ( o0ooO ) . replace ( 'special://home/addons/' , '' )
   o00o0 ( "Please remove any addons or repo's that may alter Genie Tv coding without your knowledge" , "It has been recognised you have \n[COLORred]" + IiiiIIiIi1 + "[/COLOR]\n installed on your system. In order for genie to function this addon must be removed. \n\nThere have been 'creative differences' between ourselves and this addon. Initially we just stopped our addon from working if this addon was installed, but when private talks were undertaken the 'author' (we use this term very lightly) of this addon gave us a choice, either remove our block or they will tamper with our addon, they then saw fit to host our addon and begin pushing unwanted and unauthorised, potentially malicious updates (we've no idea what they altered and with there approach anything could be possible) so we took steps to remove this addon purely for your protection from alterations to code from, self confessed, unskilled individuals. \n\nHowever the approach we took i guess can be seen as malicious because we did not inform you of actions that altered your device without your knowledge (bar a popup telling you this was happening), for this we apologise, it was a major oversight on our part and made us no better than them. \n\nAll are free to continue to use genie tv at no cost but you must make a decision. A box will soon open and you will need to choose remove or close. If you choose remove you are accepting to remove these addons that we believe have the potential to maliciously alter your device from an unofficial source or if you press close it will close genie, it will not be useable until these addons are remove and you can chose to use whatever addon you see fit at your own risk. \n\nThis is not 'playing god' please dont see it that way but merely protecting our hard work and in the end your experience from this.  We hope this issue resolves itself and things return to normality as much as, if not more than, yourself. Please wait to decide what action you wish to take" )
   xbmc . sleep ( 40000 )
   OoOOoOooooOOo = xbmcgui . Dialog ( ) . yesno ( 'Remove Potentially Harmful Addons' , 'Remove will remove addons known to alter genie tv' , 'Close will stop genie tv working to protect' , 'you from any potential unwanted updates' , nolabel = 'Close' , yeslabel = 'Remove' )
   if OoOOoOooooOOo == 0 :
    O0o0O00Oo0o0 ( o0ooO )
    oOo0O ( )
   elif OoOOoOooooOOo == 1 :
    oo0O0 ( o0ooO )
  else :
   pass
   if 22 - 22: OOooOOo . IIIii1II1II * OOooOOo
def oo0O0 ( addon ) :
 IiiiIIiIi1 = ( addon ) . replace ( 'special://home/addons/' , '' )
 Oo0oO0ooo . create ( "[COLOR=white]The addons are being removed as requested[/COLOR]" , 'Please enjoy Genie Tv and we thank you for your support' , '[COLORyellow]Hopefully this may end soon and peace is restored[/COLOR]' )
 xbmc . sleep ( 3000 )
 addon = xbmc . translatePath ( str ( addon ) )
 shutil . rmtree ( addon , ignore_errors = True )
 Oo0oO0ooo . update ( 100 , "" , "Your Device is now clean" )
 xbmc . sleep ( 1000 )
 Oo0oO0ooo . close ( )
 if 54 - 54: OooO0OoOOOO + Ii11Ii1I % oO0o + ii - o0o00Oo0O - I11i
def O0o0O00Oo0o0 ( addon ) :
 oOOoo00O0O . ok ( "[COLOR=white]Incompatible[/COLOR]" , "Unfortunately GenieTv will not work with" , addon , 'please remove then reinstall genie' )
 O0o0OO0O00O = os . path . join ( O0OoO000O0OO , 'default.py' )
 I1iiiii = open ( O0o0OO0O00O , "w+" )
 if 77 - 77: IIIii1II1II * iI11I1II1I1I
 I1iiiii . write ( r'Genie Tv will not work with certain addons in an attempt to bring you original content from the best developers' )
 I1iiiii . write ( r'and not those simply out to profit or make a name for themselves off others work' )
 I1iiiii . write ( r'Please remove' + unwanted_addons + 'if you would like to use genie tv then uninstall and reinstall from official repo' )
 if 98 - 98: oOo0O0Ooo % Ii11Ii1I * ii
 if 51 - 51: iI11I1II1I1I . OOooOOo / OoOo00o + I11i
def oOOo0II1I1iiIII ( ) :
 o00OO00OoO = oO0OOoo0OO ( i1111 ( 'aHR0cDovL3d3dy5wb2dkZXNpZ24uY28udWsvY2F0Lw==' ) )
 I11iI1i1I11I11 = re . compile ( '<tr>.+?title="(.+?)">(.+?)</tr>' , re . DOTALL ) . findall ( o00OO00OoO )
 for o000O0O , I11iI1i1I11I11 in I11iI1i1I11I11 :
  o000O0O = o000O0O
  iiIii = re . compile ( '<p><a href=".+?" rel=".+?">(.+?)\n</a>.+?<br /><a href=".+?">(.+?)</a>.+?</p>' , re . DOTALL ) . findall ( str ( I11iI1i1I11I11 ) )
  for I1i1i1iii , I1111i in iiIii :
   o00o0 ( o000O0O , I1i1i1iii , I1111i )
   if 14 - 14: IIIii1II1II / I11i
   if 32 - 32: oOo0O0Ooo * I1ii11iIi11i
   if 78 - 78: IIIii1II1II - ii - Ii1I / O0OoO / IIiIiII11i
   if 29 - 29: oOo0O0Ooo % oOo0O0Ooo
   if 94 - 94: iI11I1II1I1I / I1ii11iIi11i % o0oOO0O00o0O * o0oOO0O00o0O * IIiIiII11i
   if 29 - 29: oO0o + OOooOOo / I11i / IIIii1II1II * iI11I1II1I1I
   if 62 - 62: IIIii1II1II / OoOo00o - oO0o . iI1iI1I1i1I
   if 11 - 11: Ii1I . oO0o * OooO0OoOOOO * ii + O0OoO
   if 33 - 33: o0o00Oo0O * I11i - IIIi % IIIi
   if 18 - 18: IIIi / I1ii11iIi11i * IIIi + IIIi * Ii * Ii1I
   if 11 - 11: O0OoO / OOooOOo - OooO0OoOOOO * ii + ii . OOooOOo
   if 26 - 26: Ii11Ii1I % Ii1I
   if 76 - 76: OooO0OoOOOO * o0oOO0O00o0O
   if 52 - 52: IIIii1II1II
   if 19 - 19: oOo0O0Ooo
   if 25 - 25: Ii11Ii1I / O0OoO
   if 31 - 31: IIIii1II1II . o0o00Oo0O % oOo0O0Ooo . I11i + OooO0OoOOOO
def o0o ( ) :
 IIII ( 'Genre' , i1111 ( 'aHR0cDovL2ltb3ZpZW1heC5zZS9tb3ZpZXMv' ) , 10073 , ooOooo000oOO + 'genievision.png' , i1iiIII111ii , '' )
 IIII ( 'Most Viewed' , i1111 ( 'aHR0cDovL2ltb3ZpZW1heC5zZS9tb3ZpZXMv' ) , 10077 , ooOooo000oOO + 'genievision.png' , i1iiIII111ii , '' )
 IIII ( 'Box Office' , i1111 ( 'aHR0cDovL2ltb3ZpZW1heC5zZS9jYXRlZ29yeS9ib3gtb2ZmaWNlLw==' ) , 10074 , ooOooo000oOO + 'genievision.png' , i1iiIII111ii , '' )
 IIII ( 'Search' , '' , 10078 , ooOooo000oOO + 'genievision.png' , i1iiIII111ii , '' )
 if 62 - 62: ii . iI1iI1I1i1I
def oOOOoo00 ( ) :
 iiIiIIIiiI = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 iiI1IIIi = 'http://imoviemax.se/?s=' + ( iiIiIIIiiI ) . replace ( ' ' , '+' )
 II11IiIi11 = iiI1IIIi . lower ( )
 IIOOO0O00O0OOOO ( II11IiIi11 )
def I1iiii1I ( url ) :
 OOo0 = [ ]
 o00OO00OoO = oO0OOoo0OO ( url )
 iiIii = re . compile ( '<li class="cat-item cat-item-.+? "><a href="(.+?)">(.+?)</a><i>(.+?)</i></li>' ) . findall ( o00OO00OoO )
 for url , I1i1i1iii , oO00ooooO0o in iiIii :
  if I1i1i1iii in OOo0 :
   pass
  else :
   IIII ( I1i1i1iii + ' - ' + oO00ooooO0o + ' Films' , url , 10074 , ooOooo000oOO + 'genievision.png' , i1iiIII111ii , '' )
   OOo0 . append ( I1i1i1iii )
   if 75 - 75: ooOoO0O00 / o0o00Oo0O * I11i
def IiI1iiiIii ( url ) :
 o00OO00OoO = oO0OOoo0OO ( url )
 iiIii = re . compile ( '<li>.+?<b>.+?</b>.+?<a href="(.+?)">(.+?)</a>.+?<span>(.+?)</span>' , re . DOTALL ) . findall ( o00OO00OoO )
 for url , I1i1i1iii , I1III1111iIi in iiIii :
  IIII ( I1i1i1iii + ' - Views:' + I1III1111iIi , url , 10075 , ooOooo000oOO + 'genievision.png' , i1iiIII111ii , '' )
  if 38 - 38: o0oOO0O00o0O + iI1iI1I1i1I / IIIi % O0OoO - Ii1I
  if 14 - 14: OoOo00o / IIIi
def IIOOO0O00O0OOOO ( url ) :
 ooo0O0o00O = [ ]
 o00OO00OoO = oO0OOoo0OO ( url )
 next = re . compile ( "<link rel='next' href='(.+?)' />" ) . findall ( o00OO00OoO )
 for next in next :
  IIII ( 'NEXT PAGE' , next , 10074 , ooOooo000oOO + 'Next.png' , i1iiIII111ii , '' )
 iiIii = re . compile ( '<div class="movie">.+?<img src="(.+?)" alt="(.+?)" />.+?<a href="(.+?)"><span class="player"></span></a>' , re . DOTALL ) . findall ( o00OO00OoO )
 for I1i11 , I1i1i1iii , url in iiIii :
  IIII ( I1i1i1iii , url , 10075 , I1i11 , I1i11 , '' )
  ooo0O0o00O . append ( I1i1i1iii )
  if 12 - 12: ooOoO0O00 + ooOoO0O00 - Ii1I * I1ii11iIi11i % I1ii11iIi11i - IIiIiII11i
def o0O ( img , name , url ) :
 img = img
 name = name
 o00OO00OoO = oO0OOoo0OO ( url )
 iiIii = re . compile ( '<div id="(.+?)" class="player-content"><iframe class="playerframe" src="(.+?)" scrolling="no".+?</iframe></div>' ) . findall ( o00OO00OoO )
 for OOOooo , url in iiIii :
  print '>>>>>>>>>>>>>>>>>>>>>>>>>>> before' + url
  OooO0OO = ( url ) . replace ( 'player' , 'watch' ) + '&fv=&sou='
  print '<<<<<<<<<<<<<<<<<<<<<<<<<<< after' + OooO0OO
  o0OOo0o0O0O = ( OOOooo ) . replace ( 'play-' , 'Server ' )
  O0i1II1Iiii1I11 ( o0OOo0o0O0O , OooO0OO , 10076 , img , img , '' )
  if 65 - 65: Ii
def O0O0o0oOOO ( url ) :
 o00OO00OoO = oO0OOoo0OO ( url )
 iiIii = re . compile ( '<source src="(.+?)" type="video/mp4">' ) . findall ( o00OO00OoO )
 for OOoOoOo in iiIii :
  if '=m' in OOoOoOo :
   o000ooooO0o ( OOoOoOo )
  elif 'php' in OOoOoOo :
   O0O0o0oOOO ( url )
  else :
   o00OO00OoO = oO0OOoo0OO ( OOoOoOo )
   iiIii = re . compile ( 'content="(.+?)">' ) . findall ( o00OO00OoO )
   for iI1i11 in iiIii :
    o000ooooO0o ( OOoOoOo )
    if 66 - 66: o0o00Oo0O % Ii1I + Ii . OOooOOo / Ii11Ii1I + Ii1I
    if 86 - 86: I11i
    if 5 - 5: OooO0OoOOOO * OOooOOo
def i1Ii1i1I11Iii ( url ) :
 o00OO00OoO = oO0OOoo0OO ( url )
 I1i1i1 = re . compile ( '<td id=".+?" class="today">.+?title="(.+?)">(.+?)</td>' , re . DOTALL ) . findall ( o00OO00OoO )
 for o000O0O , OoO0O00O0oo0O in I1i1i1 :
  print 'there ><><><><><><><><><><><><'
  o000O0O = o000O0O
  iiIii = re . compile ( '<p><a href=".+?" rel=".+?">(.+?)</a>.+?<br /><a href=".+?">(.+?)</a>.+?</p>' , re . DOTALL ) . findall ( str ( OoO0O00O0oo0O ) )
  for I1i1i1iii , I1111i in iiIii :
   print 'here <><><><><><><><><><><><>'
   IIII ( '[COLORred]' + o000O0O + '[/COLOR] - ' + I1i1i1iii + ' - [COLORgreen]' + I1111i + '[/COLOR]' , i1111 ( 'aHR0cDovL3d3dy5wb2dkZXNpZ24uY28udWsvY2F0Lw==' ) , 10070 , ooOooo000oOO + 'loader.png' , i1iiIII111ii , '' )
 I11iI1i1I11I11 = re . compile ( '<td id=".+?" class="day">.+?title="(.+?)">(.+?)</td>' , re . DOTALL ) . findall ( o00OO00OoO )
 for o000O0O , I1IiI11 in I11iI1i1I11I11 :
  print 'there ><><><><><><><><><><><><'
  o000O0O = o000O0O
  iiIii = re . compile ( '<p><a href=".+?" rel=".+?">(.+?)</a>.+?<br /><a href=".+?">(.+?)</a>.+?</p>' , re . DOTALL ) . findall ( str ( I1IiI11 ) )
  for I1i1i1iii , I1111i in iiIii :
   print 'here <><><><><><><><><><><><>'
   IIII ( '[COLORred]' + o000O0O + '[/COLOR] - ' + I1i1i1iii + ' - [COLORgreen]' + I1111i + '[/COLOR]' , i1111 ( 'aHR0cDovL3d3dy5wb2dkZXNpZ24uY28udWsvY2F0Lw==' ) , 10070 , ooOooo000oOO + 'loader.png' , i1iiIII111ii , '' )
   if 9 - 9: iI1iI1I1i1I
   if 64 - 64: iI11I1II1I1I / oOo0O0Ooo . IIiIiII11i + ii . oO0o
   if 56 - 56: I1ii11iIi11i . Ii1I . oOo0O0Ooo
def ii111I ( url ) :
 o00OO00OoO = oO0OOoo0OO ( url )
 I11iI1i1I11I11 = re . compile ( '<li class="yt-uix-scroller-scroll-unit "(.+?)</li>' , re . DOTALL ) . findall ( o00OO00OoO )
 for I11iI1i1I11I11 in I11iI1i1I11I11 :
  I1i1i1iii = re . compile ( 'data-video-title="(.+?)"' ) . findall ( str ( I11iI1i1I11I11 ) )
  for I1i1i1iii in I1i1i1iii :
   I1i1i1iii = ( I1i1i1iii ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&' , '&' )
  url = re . compile ( '<a href="/w(.+?)&' ) . findall ( str ( I11iI1i1I11I11 ) )
  for url in url :
   url = 'https://www.youtube.com/w' + url
  iiI = re . compile ( '<img.+?="(.+?)"' ) . findall ( str ( I11iI1i1I11I11 ) )
  for iiI in iiI :
   iiI = 'http:' + iiI
  O0i1II1Iiii1I11 ( '[COLORgreen]' + I1i1i1iii + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , iiI , '' , '' )
  if 7 - 7: OOooOOo + IIiIiII11i . ooOoO0O00
  if 63 - 63: iI11I1II1I1I / IIIi / OoOo00o / o0oOO0O00o0O
  if 33 - 33: OooO0OoOOOO % iI11I1II1I1I * oOo0O0Ooo
  if 95 - 95: O0OoO / O0OoO
def IIiI1Ii ( url ) :
 if 57 - 57: IIIii1II1II - O0OoO - iI1iI1I1i1I + oO0o
 I1IIIiI11i1 = [ ]
 o00OO00OoO = oO0OOoo0OO ( url )
 iiIii = re . compile ( '<div class="explore-list">.+?<div class="el-img"><a href="(.+?)" class=".+?"><img src="(.+?)" alt=".+?<h3>(.+?)</h3><p>(.+?)</p></div>' , re . DOTALL ) . findall ( o00OO00OoO )
 for OOoOoOo , I1i11 , I1i1i1iii , i11I1I1I in iiIii :
  I1i1i1iii = ( I1i1i1iii ) . replace ( '&#039;' , '\'' ) . replace ( '&' , '&' ) . replace ( '&quot;' , '"' )
  OOOO0OOoO0O0 = oO0OOoo0OO ( OOoOoOo )
  ooo0O = re . compile ( '<!-- # player # -->.+?<iframe title=".+?".+?src="http://www.youtube.com/embed/(.+?)?autohide.+?<!-- detail box -->(.+?)</div>' , re . DOTALL ) . findall ( OOOO0OOoO0O0 )
  for oOOOo00O00O , iIIIII1I in ooo0O :
   ooI1i = re . compile ( '<p>(.+?)</p>' , re . DOTALL ) . findall ( str ( iIIIII1I ) )
   for iIII in ooI1i :
    if I1i1i1iii in I1IIIiI11i1 :
     pass
    else :
     O0i1II1Iiii1I11 ( I1i1i1iii , oOOOo00O00O , 8043 , I1i11 , I1i11 , iIII )
     o00oooO0Oo ( 'movies' , 'INFO' )
     I1IIIiI11i1 . append ( I1i1i1iii )
     if 70 - 70: o0oOO0O00o0O / iI11I1II1I1I
     if 85 - 85: ii % ooOoO0O00 * ii / Ii1I
def ooOOoO ( url ) :
 I1i11i = IiIi ( url )
 iiIii = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( I1i11i )
 for url , OOOOO0O00 , iIII , Iii , I1i1i1iii in iiIii :
  IIII ( I1i1i1iii , url , 10065 , OOOOO0O00 , Iii , iIII )
 o00oooO0Oo ( 'movies' , 'INFO' )
 if 31 - 31: I11i % oO0o
def iI1I ( ) :
 iiIiIIIiiI = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 iiI1IIIi = 'https://www.youtube.com/results?search_query=' + ( iiIiIIIiiI ) . replace ( ' ' , '+' )
 II11IiIi11 = iiI1IIIi . lower ( )
 o00OO00OoO = oO0OOoo0OO ( II11IiIi11 )
 iiIii = re . compile ( '<img src="(.+?)" alt=.+?yt-lockup-title "><a href="(.+?)".+?data-sessionlink=.+?" title="(.+?)".+?<span class="accessible-description".+?>(.+?)</span>.+?<div class="yt-lockup-description yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr">(.+?)</div>' , re . DOTALL ) . findall ( o00OO00OoO )
 next = re . compile ( '<a href="(.+?)" class="yt-uix-button.+?class="yt-uix-button-content">Next.+?</span></a>' ) . findall ( o00OO00OoO )
 for OooOoOo in next :
  OooOoOo = 'https://www.youtube.com' + OooOoOo
  IIII ( '[COLORgreen] NEXT [/COLOR]' , OooOoOo , 10065 , ooOooo000oOO + 'Next.png' , i1iiIII111ii , '' )
 for I1i11 , OooOoOo , I1i1i1iii , III1I1Iii1iiI , iIIIII1I in iiIii :
  II11iiii1Ii . append ( I1i1i1iii )
  o00oooO0Oo ( 'tvshows' , 'INFO' )
  iiI = 'http:' + ( I1i11 ) . replace ( 'https:' , '' )
  print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>' + iiI
  OooOoOo = 'http://www.youtube.com' + OooOoOo
  O0i1II1Iiii1I11 ( '[COLORred]' + III1I1Iii1iiI + '[/COLOR]' + '[COLORgreen]' + I1i1i1iii + '[/COLOR]' , ( OooOoOo ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , iiI , iiI , iIIIII1I )
 else :
  iiIii = re . compile ( '<img src="(.+?)" alt=.+?yt-lockup-title "><a href="(.+?)".+?data-sessionlink=.+?" title="(.+?)".+?<span class="accessible-description".+?>(.+?)</span>' , re . DOTALL ) . findall ( o00OO00OoO )
  for I1i11 , OooOoOo , I1i1i1iii , III1I1Iii1iiI in iiIii :
   print 'im doing it'
   o00oooO0Oo ( 'tvshows' , 'INFO' )
   iiI = 'http:' + ( I1i11 ) . replace ( 'https:' , '' )
   OooOoOo = 'http://www.youtube.com' + OooOoOo
   if '&' in OooOoOo :
    print ' i got here'
    o00OO00OoO = oO0OOoo0OO ( OooOoOo )
    I11iI1i1I11I11 = re . compile ( '<li class="yt-uix-scroller-scroll-unit "(.+?)</li>' , re . DOTALL ) . findall ( o00OO00OoO )
    for I11iI1i1I11I11 in I11iI1i1I11I11 :
     I1i1i1iii = re . compile ( 'data-video-title="(.+?)"' ) . findall ( str ( I11iI1i1I11I11 ) )
     for I1i1i1iii in I1i1i1iii :
      I1i1i1iii = ( I1i1i1iii ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&' , '&' )
     OooOoOo = re . compile ( '<a href="/w(.+?)&' ) . findall ( str ( I11iI1i1I11I11 ) )
     for OooOoOo in OooOoOo :
      OooOoOo = 'https://www.youtube.com/w' + OooOoOo
     iiI = re . compile ( '<img.+?="(.+?)"' ) . findall ( str ( I11iI1i1I11I11 ) )
     for iiI in iiI :
      iiI = 'http:' + iiI
     O0i1II1Iiii1I11 ( '[COLORred]' + III1I1Iii1iiI + '[/COLOR]' + '[COLORgreen]' + I1i1i1iii + '[/COLOR]' , ( OooOoOo ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , iiI , i1iiIII111ii , '' )
   elif I1i1i1iii in II11iiii1Ii :
    pass
   elif 'user' in OooOoOo or 'elete' in I1i1i1iii :
    pass
   elif 'hannel' in OooOoOo :
    print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' + OooOoOo
    o00OO00OoO = oO0OOoo0OO ( OooOoOo )
    i1Iii11I1i = re . compile ( 'data-thumb="(.+?)".+?href="(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( o00OO00OoO )
    for I1i11 , OooOoOo , I1i1i1iii in i1Iii11I1i :
     if 'outube' in OooOoOo or 'list' in OooOoOo :
      pass
     elif 'atch' in OooOoOo :
      OooOoOo = ( OooOoOo ) . replace ( '/watch?v=' , '' )
      O0i1II1Iiii1I11 ( '[COLORred]' + III1I1Iii1iiI + '[/COLOR]' + '[COLORgreen]' + I1i1i1iii + '[/COLOR]' , ( OooOoOo ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , 'http:' + I1i11 , 'http:' + I1i11 , '' )
     else :
      pass
   else :
    O0i1II1Iiii1I11 ( '[COLORred]' + III1I1Iii1iiI + '[/COLOR]' + '[COLORgreen]' + I1i1i1iii + '[/COLOR]' , ( OooOoOo ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , iiI , iiI , '' )
    if 72 - 72: iI11I1II1I1I * Ii11Ii1I % O0OoO / oO0o
def I11i1II ( url ) :
 o00OO00OoO = oO0OOoo0OO ( url )
 iiIii = re . compile ( '<img src="(.+?)" alt=.+?yt-lockup-title "><a href="(.+?)".+?data-sessionlink=.+?" title="(.+?)".+?<span class="accessible-description".+?>(.+?)</span>.+?<div class="yt-lockup-description yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr">(.+?)</div>' , re . DOTALL ) . findall ( o00OO00OoO )
 next = re . compile ( '<a href="(.+?)" class="yt-uix-button.+?class="yt-uix-button-content">Next.+?</span></a>' ) . findall ( o00OO00OoO )
 for url in next :
  url = 'https://www.youtube.com' + url
  IIII ( '[COLORgreen] NEXT [/COLOR]' , url , 10065 , ooOooo000oOO + 'Next.png' , i1iiIII111ii , '' )
 for I1i11 , url , I1i1i1iii , III1I1Iii1iiI , iIIIII1I in iiIii :
  II11iiii1Ii . append ( I1i1i1iii )
  o00oooO0Oo ( 'tvshows' , 'INFO' )
  iiI = 'http:' + ( I1i11 ) . replace ( 'https:' , '' )
  print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>' + iiI
  url = 'http://www.youtube.com' + url
  O0i1II1Iiii1I11 ( '[COLORred]' + III1I1Iii1iiI + '[/COLOR]' + '[COLORgreen]' + I1i1i1iii + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , iiI , iiI , iIIIII1I )
 else :
  iiIii = re . compile ( '<img src="(.+?)" alt=.+?yt-lockup-title "><a href="(.+?)".+?data-sessionlink=.+?" title="(.+?)".+?<span class="accessible-description".+?>(.+?)</span>' , re . DOTALL ) . findall ( o00OO00OoO )
  for I1i11 , url , I1i1i1iii , III1I1Iii1iiI in iiIii :
   o00oooO0Oo ( 'tvshows' , 'INFO' )
   iiI = 'http:' + ( I1i11 ) . replace ( 'https:' , '' )
   url = 'http://www.youtube.com' + url
   if '&' in url :
    o00OO00OoO = oO0OOoo0OO ( url )
    I11iI1i1I11I11 = re . compile ( '<li class="yt-uix-scroller-scroll-unit "(.+?)</li>' , re . DOTALL ) . findall ( o00OO00OoO )
    for I11iI1i1I11I11 in I11iI1i1I11I11 :
     I1i1i1iii = re . compile ( 'data-video-title="(.+?)"' ) . findall ( str ( I11iI1i1I11I11 ) )
     for I1i1i1iii in I1i1i1iii :
      I1i1i1iii = ( I1i1i1iii ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&' , '&' )
     url = re . compile ( '<a href="/w(.+?)&' ) . findall ( str ( I11iI1i1I11I11 ) )
     for url in url :
      url = 'https://www.youtube.com/w' + url
     iiI = re . compile ( '<img.+?="(.+?)"' ) . findall ( str ( I11iI1i1I11I11 ) )
     for iiI in iiI :
      iiI = 'http:' + iiI
     O0i1II1Iiii1I11 ( '[COLORred]' + III1I1Iii1iiI + '[/COLOR]' + '[COLORgreen]' + I1i1i1iii + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , iiI , i1iiIII111ii , '' )
   elif I1i1i1iii in II11iiii1Ii :
    pass
   elif 'user' in url or 'elete' in I1i1i1iii :
    pass
   elif 'hannel' in url :
    print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' + url
    o00OO00OoO = oO0OOoo0OO ( url )
    i1Iii11I1i = re . compile ( 'data-thumb="(.+?)".+?href="(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( o00OO00OoO )
    for I1i11 , url , I1i1i1iii in i1Iii11I1i :
     if 'outube' in url or 'list' in url :
      pass
     elif 'atch' in url :
      url = ( url ) . replace ( '/watch?v=' , '' )
      O0i1II1Iiii1I11 ( '[COLORred]' + III1I1Iii1iiI + '[/COLOR]' + '[COLORgreen]' + I1i1i1iii + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , 'http:' + I1i11 , 'http:' + I1i11 , '' )
     else :
      pass
   else :
    O0i1II1Iiii1I11 ( '[COLORred]' + III1I1Iii1iiI + '[/COLOR]' + '[COLORgreen]' + I1i1i1iii + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , iiI , iiI , '' )
    if 72 - 72: iI11I1II1I1I . ooOoO0O00 / I1ii11iIi11i . IIiIiII11i
    if 54 - 54: IIiIiII11i % IIiIiII11i
def Oo00000o0o ( ) :
 if oo0o0O00 == 'insert_password' :
  oOOoo00O0O . ok ( '[COLORgreen]Donators Login[/COLOR]' , 'You need to set username and password to access this' , 'These are unique and provided to donators to help with server and stream costs' , 'Donate @ [COLORgreen]http://architects.x10host.com[/COLOR]' )
  o0oO0 . openSettings ( sys . argv [ 0 ] )
 else :
  O0OOoOOO0oO = open ( iIi1ii1I1 )
  iiIii = re . compile ( 'plugin.video.GenieTv.+?2Flive%2F(.+?)%2F(.+?)%2F' ) . findall ( str ( O0OOoOOO0oO ) )
  for I1ii11 , oOoOoOoo0 in iiIii :
   if I1ii11 == 'needs replacing' or oOoOoOoo0 == 'needs replacing' :
    III1ii1I ( )
  IIII ( '[COLORgreen]DONATORS LIST[/COLOR]' , str ( Ii1iIiII1ii1 ) + '/thelistnew.m3u' , 7080 , ooOooo000oOO + 'GTVIPTV.png' , i1iiIII111ii , '' )
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
 IIII ( 'Full Backup' , '' , 10061 , ooOooo000oOO + 'Backup.png' , i1iiIII111ii , 'Back Up Your Full System' )
 if os . path . exists ( I1IIIii ) :
  IIII ( 'Backup Genie Favourites' , OooOoOo , 10062 , ooOooo000oOO + 'Backup.png' , i1iiIII111ii , 'Back Up Your favourites' )
 if os . path . exists ( ooooooO0oo ) :
  IIII ( 'Backup Ivue Config' , ooooooO0oo , 10062 , ooOooo000oOO + 'Backup.png' , i1iiIII111ii , 'Back Up Your master.db' )
 if os . path . exists ( IIiiiiiiIi1I1 ) :
  IIII ( 'Backup Kodi Favourites' , IIiiiiiiIi1I1 , 10062 , ooOooo000oOO + 'Backup.png' , i1iiIII111ii , 'Back Up Your favourites.xml' )
  if 52 - 52: I11i % I1ii11iIi11i
  if 64 - 64: o0o00Oo0O % iI1iI1I1i1I % o0o00Oo0O * oO0o . OoOo00o + oOo0O0Ooo
  if 75 - 75: iI1iI1I1i1I . ii % I11i * iI1iI1I1i1I % ii
zip = o0oO0 . getSetting ( 'zip' )
I11i1iIiIIIIIii = xbmc . translatePath ( os . path . join ( zip ) )
def OOo0ii11I1 ( ) :
 oO0oo = xbmc . translatePath ( os . path . join ( zip , 'testCBFolder' ) )
 if not os . path . exists ( zip ) :
  i1iiIIiiI111 . ok ( '[COLOR=white]Origin[/COLOR]' , 'The download location you have stored does not exist .\nPlease update the addon settings and try again.' , '' , '' )
  o0oO0 . openSettings ( sys . argv [ 0 ] )
  if 38 - 38: ii * O0OoO % o0o00Oo0O * OOooOOo
  if 29 - 29: Ii1I / ooOoO0O00 . oOo0O0Ooo - OOooOOo - OOooOOo - Ii11Ii1I
  if 20 - 20: ooOoO0O00 % oO0o . oOo0O0Ooo / OooO0OoOOOO * Ii * IIIii1II1II
def OOo ( name , url , description ) :
 if 'Backup' in name :
  if 'Genie' in name :
   url = I1IIIii
  elif 'Ivue' in name :
   url = ooooooO0oo
  elif 'Kodi' in name :
   url = IIiiiiiiIi1I1
  OOo0ii11I1 ( )
  i1i11I1I1iii1 = open ( url ) . read ( )
  I1iii11 = os . path . join ( I11i1iIiIIIIIii , description . split ( 'Your ' ) [ 1 ] )
  ooo0OiII1iii = open ( I1iii11 , mode = 'w' )
  ooo0OiII1iii . write ( i1i11I1I1iii1 )
  ooo0OiII1iii . close ( )
 else :
  if 'guisettings.xml' in description :
   i11i1iiiII = open ( os . path . join ( I11i1iIiIIIIIii , description . split ( 'Your ' ) [ 1 ] ) ) . read ( )
   ooOO0oO0oo00o = '<setting type="(.+?)" name="%s.(.+?)">(.+?)</setting>' % skin
   iiIii = re . compile ( ooOO0oO0oo00o ) . findall ( i11i1iiiII )
   for type , oOOo0oo0O , IiiIiI1Ii1i in iiIii :
    IiiIiI1Ii1i = IiiIiI1Ii1i . replace ( '&quot;' , '' ) . replace ( '&' , '&' )
    xbmc . executebuiltin ( "Skin.Se	t%s(%s,%s)" % ( type . title ( ) , oOOo0oo0O , IiiIiI1Ii1i ) )
  else :
   I1iii11 = os . path . join ( url )
   i1i11I1I1iii1 = open ( os . path . join ( I11i1iIiIIIIIii , description . split ( 'Your ' ) [ 1 ] ) ) . read ( )
   ooo0OiII1iii = open ( I1iii11 , mode = 'w' )
   ooo0OiII1iii . write ( i1i11I1I1iii1 )
   ooo0OiII1iii . close ( )
 i1iiIIiiI111 . ok ( "[COLOR=white]Origin[/COLOR]" , "" , 'All Done !' , '' )
 if 22 - 22: OooO0OoOOOO / Ii
 if 62 - 62: oO0o / Ii1I
 if 7 - 7: ii . OooO0OoOOOO
 if 53 - 53: Ii11Ii1I % Ii11Ii1I * I11i + OOooOOo
def Oooo00 ( ) :
 I111iIi1 = 1
 OOo0ii11I1 ( )
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
 if I111iIi1 == 0 :
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
  ii1IIi111 [ : ] = [ ooo0OiII1iii for ooo0OiII1iii in ii1IIi111 if ooo0OiII1iii not in exclude_files ]
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
 IIII ( '[COLORgreen]SCOOBY STREAMS[/COLOR]' , ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvdHZjYXRzLnBocA==' ) ) , 1016 , ooOooo000oOO + 'scoob.png' , i1iiIII111ii , '' )
 IIII ( '[COLORgreen]SCOOBY SCRAPES[/COLOR]' , str ( Ii1iIiII1ii1 ) , 1024 , ooOooo000oOO + 'scoob.png' , i1iiIII111ii , '' )
 if 86 - 86: Ii1I * o0o00Oo0O * OooO0OoOOOO
 if 51 - 51: IIiIiII11i + OooO0OoOOOO . ooOoO0O00 . Ii1I + OOooOOo * oOo0O0Ooo
def OOoOoo0 ( ) :
 O0O0O0OoOO ( )
 IIII ( '[COLORgreen]SEARCH MOVIES[/COLOR]' , str ( Ii1iIiII1ii1 ) , 9001 , ooOooo000oOO + 'MOVIESv.png' , i1iiIII111ii , '' )
 IIII ( '[COLORgreen]SEARCH SERIES[/COLOR]' , str ( Ii1iIiII1ii1 ) , 9002 , ooOooo000oOO + 'TVSHOWSv.png' , i1iiIII111ii , '' )
 IIII ( '[COLORgreen]SEARCH CARTOONS[/COLOR]' , '' , 10005 , ooOooo000oOO + 'ORIGINCARTOON' , i1iiIII111ii , '' )
 if 17 - 17: Ii11Ii1I + OoOo00o . oO0o - I1ii11iIi11i * Ii
 if 20 - 20: oOo0O0Ooo . ii % IIIii1II1II
 if 63 - 63: oOo0O0Ooo % iI11I1II1I1I
 if 39 - 39: o0oOO0O00o0O / IIiIiII11i / Ii1I % oOo0O0Ooo
def O0Oo00 ( ) :
 O0O0O0OoOO ( )
 IIII ( '[COLORgreen]RADIO[/COLOR]' , str ( Ii1iIiII1ii1 ) , 1013 , ooOooo000oOO + 'radio.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'CONCERTS' ) == 'true' :
  IIII ( '[COLORgreen]CONCERTS[/COLOR]' , ( i1111 ( 'aHR0cHM6Ly93d3cucmVkZGl0LmNvbS9yL2Z1bGxjb25jZXJ0cy8=' ) ) , 7050 , ooOooo000oOO + 'concerts.png' , i1iiIII111ii , '' )
 IIII ( '[COLORgreen]MUSIC[/COLOR]' , str ( Ii1iIiII1ii1 ) , 1030 , ooOooo000oOO + 'MUSIC.png' , i1iiIII111ii , '' )
 IIII ( '[COLORgreen]MUSIC ARCHIVE[/COLOR]' , str ( Ii1iIiII1ii1 ) + ( i1111 ( 'L3ZvZC91cmxzL211c2ljLnBocA==' ) ) , 1010 , ooOooo000oOO + 'MUSIC.png' , i1iiIII111ii , '' )
 IIII ( '[COLORgreen]MUSIC SEARCH[/COLOR]' , str ( Ii1iIiII1ii1 ) , 1111 , ooOooo000oOO + 'search.png' , i1iiIII111ii , '' )
 IIII ( '[COLORgreen]KODIBLE AUDIO BOOKS[/COLOR]' , 'http://doremisa.com/audiobooks/' , 30000 , ooOooo000oOO + 'kodible.png' , i1iiIII111ii , '' )
 if 41 - 41: iI11I1II1I1I % iI1iI1I1i1I
 o00oooO0Oo ( 'movies' , 'MAIN' )
 if 59 - 59: IIIii1II1II + Ii
def oo0OOo0O ( ) :
 O0O0O0OoOO ( )
 if 39 - 39: ii + OoOo00o % IIIii1II1II / IIIii1II1II
 O0i1II1Iiii1I11 ( 'DELETE CACHE' , 'url' , 14 , ooOooo000oOO + 'MAIN5.png' , i1iiIII111ii , '' )
 O0i1II1Iiii1I11 ( 'DELETE PACKAGES' , 'url' , 6 , ooOooo000oOO + 'MAIN4.png' , i1iiIII111ii , '' )
 O0i1II1Iiii1I11 ( 'FORCE REFRESH' , 'url' , 10 , ooOooo000oOO + 'MAIN3.png' , i1iiIII111ii , 'Force Refresh All Repos' )
 if 27 - 27: o0oOO0O00o0O . iI1iI1I1i1I . iI11I1II1I1I . iI11I1II1I1I
 O0i1II1Iiii1I11 ( 'CHECK MY IP' , 'url' , 12 , ooOooo000oOO + 'MAIN2.png' , i1iiIII111ii , '' )
 O0i1II1Iiii1I11 ( 'ANDROID ONLY DELETE TEXTURE13.DB&THUBMNAIL FOLDER' , 'url' , 13 , ooOooo000oOO + 'MAIN1.png' , i1iiIII111ii , 'Only Works On Android On Windows It Deletes Your Thumnails Folder But Does Not Delete The Textures13.db' )
 IIII ( '[COLORgreen]ADVANCED SETTINGS XML[/COLOR]' , str ( Ii1iIiII1ii1 ) , 4 , ooOooo000oOO + 'XML.png' , i1iiIII111ii , '' )
 IIII ( '[COLORgreen]URL FIXES[/COLOR]' , str ( Ii1iIiII1ii1 ) , 20 , ooOooo000oOO + 'URLFIX.png' , i1iiIII111ii , '' )
 o00oooO0Oo ( 'movies' , 'MAIN' )
 if 20 - 20: I11i / ooOoO0O00
 if 71 - 71: OOooOOo . ooOoO0O00
def iI1Ii11111iIi ( ) :
 O0O0O0OoOO ( )
 IIII ( '[COLORgreen]REPOS[/COLOR]' , ( i1111 ( 'aHR0cDovL21pcnJvcnMua29kaS50di9hZGRvbnMv' ) ) , 2030 , ooOooo000oOO + 'repos.png' , i1iiIII111ii , '' )
 IIII ( '[COLORgreen]NEW[/COLOR]' , str ( Ii1iIiII1ii1 ) , 22 , ooOooo000oOO + 'NEW.png' , i1iiIII111ii , '' )
 IIII ( '[COLORgreen]IPTV[/COLOR]' , str ( Ii1iIiII1ii1 ) , 23 , ooOooo000oOO + 'IPTV.png' , i1iiIII111ii , '' )
 IIII ( '[COLORgreen]VIDEO[/COLOR]' , str ( Ii1iIiII1ii1 ) , 24 , ooOooo000oOO + 'VIDEO.png' , i1iiIII111ii , '' )
 IIII ( '[COLORgreen]SPORTS[/COLOR]' , str ( Ii1iIiII1ii1 ) , 25 , ooOooo000oOO + 'SPORTS.png' , i1iiIII111ii , '' )
 IIII ( '[COLORgreen]KIDS[/COLOR]' , str ( Ii1iIiII1ii1 ) , 26 , ooOooo000oOO + 'KIDS.png' , i1iiIII111ii , '' )
 IIII ( '[COLORgreen]MUSIC[/COLOR]' , str ( Ii1iIiII1ii1 ) , 27 , ooOooo000oOO + 'MUSIC.png' , i1iiIII111ii , '' )
 IIII ( '[COLORgreen]PROGRAMS[/COLOR]' , str ( Ii1iIiII1ii1 ) , 28 , ooOooo000oOO + 'PROGRAMS.png' , i1iiIII111ii , '' )
 IIII ( '[COLORgreen]XXX[/COLOR]' , 'URL' , 29 , ooOooo000oOO + 'XXX.png' , i1iiIII111ii , '' )
 o00oooO0Oo ( 'movies' , 'MAIN' )
 if 94 - 94: IIIii1II1II . IIIi
 if 84 - 84: o0o00Oo0O . iI1iI1I1i1I - IIiIiII11i . O0OoO / IIiIiII11i
def iii1 ( ) :
 O0O0O0OoOO ( )
 O0i1II1Iiii1I11 ( 'CHECK ADVANCED XML' , str ( Ii1iIiII1ii1 ) , 8 , ooOooo000oOO + 'XML.png' , i1iiIII111ii , '' )
 O0i1II1Iiii1I11 ( 'MUCKYS XML' , str ( Ii1iIiII1ii1 ) + '/wizard/muckys.xml' , 7 , ooOooo000oOO + 'XML.png' , i1iiIII111ii , '' )
 O0i1II1Iiii1I11 ( '0CACHE XML' , str ( Ii1iIiII1ii1 ) + '/wizard/0cache.xml' , 7 , ooOooo000oOO + 'XML.png' , i1iiIII111ii , '' )
 O0i1II1Iiii1I11 ( 'MIKEY1234 XML' , str ( Ii1iIiII1ii1 ) + '/wizard/mikey.xml' , 7 , ooOooo000oOO + 'XML.png' , i1iiIII111ii , '' )
 O0i1II1Iiii1I11 ( 'TUXENS XML' , str ( Ii1iIiII1ii1 ) + '/wizard/tuxens.xml' , 7 , ooOooo000oOO + 'XML.png' , i1iiIII111ii , '' )
 O0i1II1Iiii1I11 ( 'P2P RECOMMENDED XML1' , str ( Ii1iIiII1ii1 ) + '/wizard/p2p1.xml' , 7 , ooOooo000oOO + 'XML.png' , i1iiIII111ii , '' )
 O0i1II1Iiii1I11 ( 'P2P RECOMMENDED XML2' , str ( Ii1iIiII1ii1 ) + '/wizard/p2p2.xml' , 7 , ooOooo000oOO + 'XML.png' , i1iiIII111ii , '' )
 O0i1II1Iiii1I11 ( 'DELETE XML' , str ( Ii1iIiII1ii1 ) , 11 , ooOooo000oOO + 'XML.png' , i1iiIII111ii , '' )
 o00oooO0Oo ( 'movies' , 'MAIN' )
 if 32 - 32: Ii11Ii1I . OooO0OoOOOO . ii - oO0o + OoOo00o
def ooO0oO00O0o ( ) :
 O0O0O0OoOO ( )
 O0i1II1Iiii1I11 ( '[COLORgreen]My Local Zip[/COLOR]' , I11 , 48 , ooOooo000oOO + 'MB.png' , i1iiIII111ii , '' )
 O0i1II1Iiii1I11 ( '[COLORgreen]My Online Zip[/COLOR]' , i11 , 43 , ooOooo000oOO + 'MB.png' , i1iiIII111ii , '' )
 if 70 - 70: IIIi
def i11iIIi11 ( ) :
 O0O0O0OoOO ( )
 O0i1II1Iiii1I11 ( 'INSTALL FTV GUIDE AND OTHER ADDONS REQUIRED' , str ( Ii1iIiII1ii1 ) + '/wizard/customftv/ftvguide-addons.zip' , 5 , ooOooo000oOO + 'FTV4.png' , i1iiIII111ii , '' )
 O0i1II1Iiii1I11 ( 'FTV GUIDE FIRST RUN SETTINGS' , str ( Ii1iIiII1ii1 ) + '/wizard/customftv/settings.xml' , 17 , ooOooo000oOO + 'FTV3.png' , i1iiIII111ii , '' )
 O0i1II1Iiii1I11 ( 'FTV GUIDE ADDONS2.INI UPDATE DAILY' , 'http://ren.byethost12.com/addons2.ini' , 16 , ooOooo000oOO + 'FTV1.png' , i1iiIII111ii , '' )
 O0i1II1Iiii1I11 ( 'RESET FTV DATABASE' , 'url' , 18 , ooOooo000oOO + 'FTV2.png' , i1iiIII111ii , '' )
 if 98 - 98: IIIi
 if 12 - 12: IIiIiII11i . iI1iI1I1i1I / IIIii1II1II
 if 77 - 77: O0OoO - oOo0O0Ooo % iI1iI1I1i1I - o0o00Oo0O
def o0O0O0 ( ) :
 O0O0O0OoOO ( )
 IIII ( '[COLORgreen]SKINS[/COLOR]' , str ( Ii1iIiII1ii1 ) , 33 , ooOooo000oOO + 'skinp.png' , i1iiIII111ii , '' )
 IIII ( '[COLORgreen]ARTWORK PACKS[/COLOR]' , str ( Ii1iIiII1ii1 ) , 34 , ooOooo000oOO + 'artp.png' , i1iiIII111ii , '' )
 IIII ( '[COLORgreen]CREATE UNIVERSAL PATHS[/COLOR]' , oooOOOOO , 35 , ooOooo000oOO + 'GUI.png' , i1iiIII111ii , '' )
 o00oooO0Oo ( 'movies' , 'MAIN' )
 if 6 - 6: o0oOO0O00o0O . OooO0OoOOOO * OOooOOo . ooOoO0O00
def oOOo ( url ) :
 O000oo0O = oO0OOoo0OO ( I1IiIIi ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iiIii = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( O000oo0O )
 for I1i1i1iii , url , OOOOO0O00 , Iii , iIIIII1I in iiIii :
  IIII ( I1i1i1iii , url , 5 , OOOOO0O00 , Iii , iIIIII1I )
 o00oooO0Oo ( 'movies' , 'MAIN' )
 if 42 - 42: o0o00Oo0O . OoOo00o - I11i / ooOoO0O00
def OooOOO ( ) :
 O0O0O0OoOO ( )
 IIII ( '[COLORgreen]GOTHAM SKINS[/COLOR]' , str ( Ii1iIiII1ii1 ) , 36 , ooOooo000oOO + 'GSKIN.png' , i1iiIII111ii , '' )
 IIII ( '[COLORgreen]HELIX SKINS[/COLOR]' , str ( Ii1iIiII1ii1 ) , 37 , ooOooo000oOO + 'HSKIN.png' , i1iiIII111ii , '' )
 IIII ( '[COLORgreen]ISENGAARD SKINS[/COLOR]' , oooOOOOO , 38 , ooOooo000oOO + 'ISKIN.png' , i1iiIII111ii , '' )
 o00oooO0Oo ( 'movies' , 'MAIN' )
 if 48 - 48: iI11I1II1I1I % ooOoO0O00 % o0oOO0O00o0O + O0OoO
def Iiii11iIi1 ( url ) :
 O000oo0O = oO0OOoo0OO ( str ( Ii1iIiII1ii1 ) + i1iI11I1II1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iiIii = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( O000oo0O )
 for I1i1i1iii , url , OOOOO0O00 , Iii , iIIIII1I in iiIii :
  IIII ( I1i1i1iii , url , 42 , OOOOO0O00 , Iii , iIIIII1I )
 o00oooO0Oo ( 'movies' , 'MAIN' )
 if 14 - 14: Ii - o0oOO0O00o0O * OOooOOo
def OO0oIII111i11IiI ( url ) :
 O000oo0O = oO0OOoo0OO ( str ( Ii1iIiII1ii1 ) + O0000 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iiIii = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( O000oo0O )
 for I1i1i1iii , url , OOOOO0O00 , Iii , iIIIII1I in iiIii :
  IIII ( I1i1i1iii , url , 42 , OOOOO0O00 , Iii , iIIIII1I )
 o00oooO0Oo ( 'movies' , 'MAIN' )
 if 64 - 64: IIiIiII11i - oOo0O0Ooo
def O0O0ooOOO ( url ) :
 O000oo0O = oO0OOoo0OO ( str ( Ii1iIiII1ii1 ) + o0o00Ooo0o ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iiIii = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( O000oo0O )
 for I1i1i1iii , url , OOOOO0O00 , Iii , iIIIII1I in iiIii :
  IIII ( I1i1i1iii , url , 42 , OOOOO0O00 , Iii , iIIIII1I )
 o00oooO0Oo ( 'movies' , 'MAIN' )
 if 76 - 76: IIiIiII11i
def Ii1i1i1111 ( url ) :
 O000oo0O = oO0OOoo0OO ( i1111 ( 'aHR0cHM6Ly9kbC5kcm9wYm94dXNlcmNvbnRlbnQuY29tL3MvN2ZrMjhndDlwb3QxMjJhL0JVSUxEUy50eHQ/ZGw9MA==' ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iiIii = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( O000oo0O )
 for I1i1i1iii , url , OOOOO0O00 , Iii , iIIIII1I in iiIii :
  IIII ( I1i1i1iii , url , 42 , OOOOO0O00 , Iii , iIIIII1I )
 o00oooO0Oo ( 'movies' , 'MAIN' )
 if 57 - 57: Ii11Ii1I % IIiIiII11i
def O00oOo ( url ) :
 O000oo0O = oO0OOoo0OO ( str ( Ii1iIiII1ii1 ) + I1111I1II11 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iiIii = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( O000oo0O )
 for I1i1i1iii , url , OOOOO0O00 , Iii , iIIIII1I in iiIii :
  IIII ( I1i1i1iii , url , 40 , OOOOO0O00 , Iii , iIIIII1I )
 o00oooO0Oo ( 'movies' , 'MAIN' )
 if 30 - 30: ii % ii
def oOoOoo0 ( url ) :
 O000oo0O = oO0OOoo0OO ( str ( Ii1iIiII1ii1 ) + ii1II ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iiIii = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( O000oo0O )
 for I1i1i1iii , url , OOOOO0O00 , Iii , iIIIII1I in iiIii :
  IIII ( I1i1i1iii , url , 5 , OOOOO0O00 , Iii , iIIIII1I )
 o00oooO0Oo ( 'movies' , 'MAIN' )
 if 50 - 50: Ii11Ii1I + ooOoO0O00 / o0o00Oo0O / I11i
def Iiii1I1 ( ) :
 I1i11i = IiIi ( i1111 ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby9hcGt0b29sL2Fway5waHA=' ) )
 iiIii = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( I1i11i )
 for OooOoOo , iiI , I1i1i1iii in iiIii :
  O0II11i11II ( I1i1i1iii , OooOoOo , 2031 , iiI )
  if 29 - 29: I1ii11iIi11i % oO0o % OooO0OoOOOO . I11i / ii * O0OoO
def o0OoO000O ( name , url , description ) :
 oO0oo = xbmc . translatePath ( os . path . join ( OOoiIIiiIIIi1I , 'Download' ) )
 Oo0oO0ooo = xbmcgui . DialogProgress ( )
 Oo0oO0ooo . create ( "Your App Is Downloading" , "Why not check out our website" , '' , 'Http://architects.x10host.com' )
 OO0o0o0oo0O = os . path . join ( oO0oo , name + '.apk' )
 try :
  os . remove ( OO0o0o0oo0O )
 except :
  pass
 downloader . download ( url , OO0o0o0oo0O , Oo0oO0ooo )
 i1iiIIiiI111 = xbmcgui . Dialog ( )
 i1iiIIiiI111 . ok ( "GenieTv" , "[COLORred]Please press ok, exit kodi and go to your downloads folder to install your app[/COLOR]" , "[COLORblue]Tool Brought To You By Architects@Work[/COLOR]" )
 if 40 - 40: I11i + I1ii11iIi11i . I11i % O0OoO
def I11I1IIiiII1 ( url ) :
 oO0oo = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/resources/downloads' ) )
 Oo0oO0ooo = xbmcgui . DialogProgress ( )
 Oo0oO0ooo . create ( "Your fILM Is Downloading" , "Why not check out our website" , '' , 'Http://architects.x10host.com' )
 OO0o0o0oo0O = os . path . join ( oO0oo , I1i1i1iii + '.mp4' )
 try :
  os . remove ( OO0o0o0oo0O )
 except :
  pass
 downloader . download ( url , OO0o0o0oo0O , Oo0oO0ooo )
 i1iiIIiiI111 = xbmcgui . Dialog ( )
 i1iiIIiiI111 . ok ( "GenieTv" , "[COLORred]Please press ok, Your download With Be Avaiilable Via The My Downloads Button[/COLOR]" , "[COLORblue]Tool Brought To You By Architects@Work[/COLOR]" )
 if 31 - 31: oOo0O0Ooo * OoOo00o + ii - o0oOO0O00o0O / ii
 if 19 - 19: OooO0OoOOOO * O0OoO * I11i + o0o00Oo0O / o0o00Oo0O
def ooOoO ( name , url , description ) :
 oO0oo = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 Oo0oO0ooo = xbmcgui . DialogProgress ( )
 Oo0oO0ooo . create ( "Your Art Pack Is Downloading" , "Why not check out our website" , '' , 'Http://architects.x10host.com' )
 OO0o0o0oo0O = os . path . join ( oO0oo , name )
 try :
  os . remove ( OO0o0o0oo0O )
 except :
  pass
 downloader . download ( url , OO0o0o0oo0O , Oo0oO0ooo )
 oOoOOOo = xbmc . translatePath ( os . path . join ( oo00 ) )
 time . sleep ( 2 )
 Oo0oO0ooo . update ( 0 , "" , "Placing Your Art Please Wait" )
 print '======================================='
 print oOoOOOo
 print '======================================='
 extract . all ( OO0o0o0oo0O , oOoOOOo , Oo0oO0ooo )
 i1iiIIiiI111 = xbmcgui . Dialog ( )
 i1iiIIiiI111 . ok ( "GenieTv" , "[COLORred]Once complete your artwork will be stored in your Media folder, Accessible via the Homefolder, Enjoy[/COLOR]" )
 if 43 - 43: ooOoO0O00
 if 23 - 23: o0oOO0O00o0O + iI1iI1I1i1I . OOooOOo * oOo0O0Ooo + Ii1I
def I1iIi1iiiIiI ( url ) :
 O000oo0O = oO0OOoo0OO ( i1111 ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby9HZW5pZVR2L3Rlc3Qvd2gudHh0' ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iiIii = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( O000oo0O )
 for I1i1i1iii , url , OOOOO0O00 , Iii , iIIIII1I in iiIii :
  IIII ( I1i1i1iii , url , 5 , OOOOO0O00 , Iii , iIIIII1I )
 try :
  O000oo0O = oO0OOoo0OO ( III1I1Ii11iI + oO0o0o0ooO0oO + oO00OoOO ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
  iiIii = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( O000oo0O )
  for I1i1i1iii , url , OOOOO0O00 , Iii , iIIIII1I in iiIii :
   IIII ( I1i1i1iii , url , 5 , OOOOO0O00 , Iii , iIIIII1I )
 except : pass
 o00oooO0Oo ( 'movies' , 'INFO' )
 if 18 - 18: O0OoO - OOooOOo % ooOoO0O00 + o0o00Oo0O + Ii + ooOoO0O00
 if 91 - 91: OOooOOo + O0OoO . oOo0O0Ooo
def O0oOoOOO0OO ( url ) :
 O000oo0O = oO0OOoo0OO ( i1111 ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby9HZW5pZVR2L3Rlc3Qvd2gudHh0' ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iiIii = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( O000oo0O )
 for I1i1i1iii , url , OOOOO0O00 , Iii , iIIIII1I in iiIii :
  IIII ( I1i1i1iii , url , 43 , OOOOO0O00 , Iii , iIIIII1I )
 try :
  O000oo0O = oO0OOoo0OO ( III1I1Ii11iI + oO0o0o0ooO0oO + oO00OoOO ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
  iiIii = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( O000oo0O )
  for I1i1i1iii , url , OOOOO0O00 , Iii , iIIIII1I in iiIii :
   IIII ( I1i1i1iii , url , 43 , OOOOO0O00 , Iii , iIIIII1I )
 except : pass
 o00oooO0Oo ( 'movies' , 'INFO' )
 if 91 - 91: OooO0OoOOOO + OOooOOo + I11i - iI11I1II1I1I
 if 17 - 17: OoOo00o
def i1ii11 ( name , url , description ) :
 oO0oo = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 Oo0oO0ooo = xbmcgui . DialogProgress ( )
 Oo0oO0ooo . create ( "GenieTv" , "Downloading Content" , '' , 'Please Wait' )
 OO0o0o0oo0O = os . path . join ( oO0oo , name + '.zip' )
 try :
  os . remove ( OO0o0o0oo0O )
 except :
  pass
 downloader . download ( url , OO0o0o0oo0O , Oo0oO0ooo )
 ii1i = xbmc . translatePath ( os . path . join ( 'special://home' , 'addons' ) )
 time . sleep ( 2 )
 Oo0oO0ooo . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print ii1i
 print '======================================='
 extract . all ( OO0o0o0oo0O , ii1i , Oo0oO0ooo )
 i1iiIIiiI111 = xbmcgui . Dialog ( )
 i1iiIIiiI111 . ok ( "GenieTv" , "Press ok to finish install" , "[COLOR yellow]Brought To You By Architects@Work[/COLOR]" )
 oOo0O ( )
 if 5 - 5: OoOo00o . Ii1I . IIiIiII11i . ii
 if 96 - 96: Ii - IIIii1II1II % o0o00Oo0O / oO0o
def O0O0 ( name , url , description ) :
 oO0oo = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 Oo0oO0ooo = xbmcgui . DialogProgress ( )
 Oo0oO0ooo . create ( "GenieTv" , "Downloading " , '' , 'Please Wait' )
 OO0o0o0oo0O = os . path . join ( oO0oo , 'plugin.program.GenieTv.install' + '.zip' )
 try :
  os . remove ( OO0o0o0oo0O )
 except :
  pass
 downloader . download ( url , OO0o0o0oo0O , Oo0oO0ooo )
 ii1i = xbmc . translatePath ( os . path . join ( 'special://' , 'home' ) )
 time . sleep ( 2 )
 Oo0oO0ooo . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print ii1i
 print '======================================='
 extract . all ( OO0o0o0oo0O , ii1i , Oo0oO0ooo )
 i1iiIIiiI111 = xbmcgui . Dialog ( )
 i1iiIIiiI111 . ok ( "GenieTv" , "Press ok to force close kodi, if unsuccessful using windows Please kill kodi via taskmanager" , "[COLOR yellow]Brought To You By Architects@Work[/COLOR]" )
 oo0OOOoOo ( )
 if 21 - 21: oO0o - o0o00Oo0O . OoOo00o + Ii11Ii1I . iI11I1II1I1I - OOooOOo
def I11IIIiIi11 ( name , url , description ) :
 oO0oo = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 Oo0oO0ooo = xbmcgui . DialogProgress ( )
 Oo0oO0ooo . create ( "GenieTv" , "Downloading " , '' , 'Please Wait' )
 OO0o0o0oo0O = os . path . join ( oO0oo , 'plugin.program.GenieTv.install' + '.zip' )
 try :
  os . remove ( OO0o0o0oo0O )
 except :
  pass
 downloader . download ( url , OO0o0o0oo0O , Oo0oO0ooo )
 ii1i = xbmc . translatePath ( os . path . join ( 'special://' , 'home' ) )
 time . sleep ( 2 )
 Oo0oO0ooo . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print ii1i
 print '======================================='
 extract . all ( OO0o0o0oo0O , ii1i , Oo0oO0ooo )
 i1iiIIiiI111 = xbmcgui . Dialog ( )
 i1iiIIiiI111 . ok ( "GenieTv" , "Please Disconnect The Power From Your Device. DO NOT EXIT CLEANLY VIA SHUTDOWN" , "[COLOR yellow]Brought To You By Architects@Work[/COLOR]" )
 if 39 - 39: Ii11Ii1I % o0o00Oo0O % OOooOOo . ooOoO0O00
 if 86 - 86: oO0o * ii
def OooO0oOo ( name , url , description ) :
 ii1i = xbmc . translatePath ( os . path . join ( 'special://' , 'home' ) )
 Oo0oO0ooo = xbmcgui . DialogProgress ( )
 OO0o0o0oo0O = os . path . join ( I11 )
 time . sleep ( 2 )
 Oo0oO0ooo . create ( "GenieTv" , "Restoring" , '' , 'Please Wait' )
 print '======================================='
 print ii1i
 print '======================================='
 extract . all ( OO0o0o0oo0O , ii1i , Oo0oO0ooo )
 i1iiIIiiI111 = xbmcgui . Dialog ( )
 i1iiIIiiI111 . ok ( "GenieTv" , "Please Disconnect The Power From Your Device. DO NOT EXIT CLEANLY VIA SHUTDOWN" , "[COLOR yellow]Brought To You By Architects@Work[/COLOR]" )
 if 66 - 66: oO0o * I1ii11iIi11i
 if 28 - 28: oO0o % OOooOOo % Ii1I + oOo0O0Ooo / oOo0O0Ooo
def oo0OOOoOo ( ) :
 OoOOoOooooOOo = xbmcgui . Dialog ( ) . yesno ( 'Force Close Kodi' , 'You are about to close Kodi' , 'Would you like to continue?' , nolabel = 'No, Cancel' , yeslabel = 'Yes, Close' )
 if OoOOoOooooOOo == 0 :
  return
 elif OoOOoOooooOOo == 1 :
  pass
 OO0O0ooOOO00 = IiIiiiiI1 ( )
 print "Platform: " + str ( OO0O0ooOOO00 )
 if OO0O0ooOOO00 == 'osx' :
  print "############   try osx force close  #################"
  try : os . system ( 'killall -9 XBMC' )
  except : pass
  try : os . system ( 'killall -9 Kodi' )
  except : pass
  i1iiIIiiI111 . ok ( "[COLOR=red][B]WARNING  !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu." , '' )
 elif OO0O0ooOOO00 == 'linux' :
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
 elif OO0O0ooOOO00 == 'android' :
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
 elif OO0O0ooOOO00 == 'windows' :
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
  if 62 - 62: Ii1I % o0oOO0O00o0O * oO0o - ooOoO0O00
def IiIiiiiI1 ( ) :
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
  if 66 - 66: Ii / I11i - ii / ooOoO0O00 . Ii
  if 16 - 16: I1ii11iIi11i % Ii1I + iI1iI1I1i1I - o0o00Oo0O . o0oOO0O00o0O / IIIi
  if 35 - 35: OoOo00o / IIIi / IIiIiII11i - iI11I1II1I1I + IIiIiII11i . IIIi
def O0O00O000OOO ( url ) :
 Oo0oO0ooo . create ( "[COLOR=green]GenieTv[/COLOR]" , "Renaming paths..." , '' , 'Please Wait' )
 for iI , i1iI11i1IIi , ii1IIi111 in os . walk ( url ) :
  for file in ii1IIi111 :
   if file . endswith ( ".xml" ) :
    Oo0oO0ooo . update ( 0 , "Fixing" , file , 'Please Wait' )
    i11i1iiiII = open ( ( os . path . join ( iI , file ) ) ) . read ( )
    Oo0O = i11i1iiiII . replace ( oooOOOOO , 'special://home/' )
    ooo0OiII1iii = open ( ( os . path . join ( iI , file ) ) , mode = 'w' )
    ooo0OiII1iii . write ( str ( Oo0O ) )
    ooo0OiII1iii . close ( )
 oo0OOOoOo ( )
 if 1 - 1: o0o00Oo0O / o0oOO0O00o0O % IIIi . I1ii11iIi11i + OooO0OoOOOO
def I1Ii11iiiI ( ) :
 I1i11i = IiIi ( i1111 ( 'aHR0cDovL3d3dy5saXN0ZW5saXZlLmV1L3VrLmh0bWw=' ) )
 iiIii = re . compile ( '<tr>.+?<td><a href=".+?"><b>(.+?)</b>.+?<td><a href="(.+?)">' , re . DOTALL ) . findall ( I1i11i )
 for I1i1i1iii , OooOoOo in iiIii :
  i1II1IiIII111 ( I1i1i1iii , OooOoOo , 222 , ooOooo000oOO + 'radio.png' )
  if 50 - 50: IIiIiII11i * Ii1I / Ii11Ii1I . I11i + I1ii11iIi11i - IIIii1II1II
def II1iiIiIiI ( ) :
 I1i11i = IiIi ( i1111 ( 'aHR0cDovL3d3dy50b29uamV0LmNvbS8=' ) )
 iiIii = re . compile ( '<a href="(.+?)" style="font-size:.8em;">(.+?)</a>' ) . findall ( I1i11i )
 for OooOoOo , I1i1i1iii in iiIii :
  O0II11i11II ( '[COLORgreen]' + I1i1i1iii + '[/COLOR]' , 'http://www.toonjet.com/' + OooOoOo , 8051 , ooOooo000oOO + 'classictoons.png' )
def iIIi1I1ii ( url ) :
 I1i11i = IiIi ( url )
 iiIii = re . compile ( '<a href="(.+?)"><img src="(.+?)"' ) . findall ( I1i11i )
 ooo0O = re . compile ( '<a href="(.+?)">.+?</a></td></tr></table>' ) . findall ( I1i11i )
 for url , I1i11 in iiIii :
  if 'ol.gif' in I1i11 :
   pass
  elif 'link_block_' in I1i11 :
   pass
  elif '.png' in I1i11 :
   pass
  else :
   O0II11i11II ( ( I1i11 ) . replace ( 'http://www.toonjet.com/images/icons/' , '' ) . replace ( 'images/icons/' , '' ) . replace ( '.jpg' , '' ) . replace ( '_icon' , '' ) . replace ( '_' , ' ' ) , 'http://www.toonjet.com/' + url , 8052 , ooOooo000oOO + 'vod.png' )
 for url in ooo0O :
  O0II11i11II ( 'NEXT PAGE' , 'http://www.toonjet.com/' + url , 8051 , ooOooo000oOO + 'Next.png' )
def Iiii ( url ) :
 I1i11i = IiIi ( url )
 iiIii = re . compile ( '<iframe width="640" height="480" src="(.+?)" frameborder="0" allowfullscreen></iframe>' ) . findall ( I1i11i )
 for url in iiIii :
  i1II1IiIII111 ( '[COLORgreen]PLAY[/COLOR]' , ( url ) . replace ( 'http://www.youtube.com/embed/' , '' ) . replace ( '?autoplay=0' , '' ) , 8043 , ooOooo000oOO + 'classictoons.png' )
  if 44 - 44: O0OoO . o0oOO0O00o0O . ii
  if 50 - 50: I11i * Ii11Ii1I % Ii1I / I1ii11iIi11i - o0o00Oo0O % o0oOO0O00o0O
def IIII1ii ( ) :
 IiIIi1I1I11Ii ( 'Audio Books' , '' , 30011 , ooOooo000oOO + 'audiobooks.png' , ooOooo000oOO + 'audiobooks.png' , '' )
 IiIIi1I1I11Ii ( 'Kids Audio Books' , '' , 30006 , ooOooo000oOO + 'kidsaudiobooks.png' , ooOooo000oOO + 'kidsaudiobooks.png' , '' )
 if 64 - 64: ii
def oO0oooooo ( ) :
 IiIIi1I1I11Ii ( 'All' , '' , 30001 , ooOooo000oOO + 'kodible.png' , ooOooo000oOO + 'kodible.png' , '' )
 IiIIi1I1I11Ii ( 'Popular' , '' , 30012 , ooOooo000oOO + 'POPULARv.png' , ooOooo000oOO + 'POPULARv.png' , '' )
 IiIIi1I1I11Ii ( 'Search' , '' , 30013 , ooOooo000oOO + 'search.png' , ooOooo000oOO + 'search.png' , '' )
 if 65 - 65: OooO0OoOOOO + I1ii11iIi11i
def Ooo0O0 ( ) :
 o00OO00OoO = oO0OOoo0OO ( OooO0 + 'books' + ooOoOoo0O )
 iiIii = re . compile ( '<NAME=>(.*?)</NAME><URL=>(.*?)</URL><CAT=>(.*?)</CAT>' ) . findall ( o00OO00OoO )
 for I1i1i1iii , OooOoOo , ooo0 in iiIii :
  if 'Parent' in I1i1i1iii :
   pass
  elif '2' in ooo0 :
   IiIIi1I1I11Ii ( ( I1i1i1iii ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , OooOoOo , 30010 , ooOooo000oOO + 'kodible.png' , ooOooo000oOO + 'kodible.png' , '' )
   if 55 - 55: I1ii11iIi11i
def ooO0o ( ) :
 iiIiIIIiiI = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 II11IiIi11 = iiIiIIIiiI . lower ( )
 o00OO00OoO = oO0OOoo0OO ( OooO0 + 'books' + ooOoOoo0O )
 iiIii = re . compile ( '<NAME=>(.*?)</NAME><URL=>(.*?)</URL><CAT=>(.*?)</CAT>' ) . findall ( o00OO00OoO )
 for I1i1i1iii , OooOoOo , ooo0 in iiIii :
  if iiIiIIIiiI in I1i1i1iii . lower ( ) :
   if '1' in ooo0 :
    IiIIi1I1I11Ii ( ( I1i1i1iii ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , OooOoOo , 30010 , ooOooo000oOO + 'kodible.png' , ooOooo000oOO + 'kodible.png' , '' )
   elif '2' in ooo0 :
    IiIIi1I1I11Ii ( ( I1i1i1iii ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , OooOoOo , 30010 , ooOooo000oOO + 'kodible.png' , ooOooo000oOO + 'kodible.png' , '' )
   elif '3' in ooo0 :
    IiIIi1I1I11Ii ( ( I1i1i1iii ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , OooOoOo , 30009 , ooOooo000oOO + 'kodible.png' , ooOooo000oOO + 'kodible.png' , '' )
    if 25 - 25: iI11I1II1I1I - o0oOO0O00o0O
    if 3 - 3: oOo0O0Ooo * O0OoO + IIiIiII11i - oO0o
def OOOOOoOO0OOoo ( ) :
 o00OO00OoO = oO0OOoo0OO ( OooO0 + 'books' + ooOoOoo0O )
 iiIii = re . compile ( '<NAME=>(.*?)</NAME><URL=>(.*?)</URL><CAT=>(.*?)</CAT>' ) . findall ( o00OO00OoO )
 for I1i1i1iii , OooOoOo , ooo0 in iiIii :
  if '1' in ooo0 :
   IiIIi1I1I11Ii ( ( I1i1i1iii ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , OooOoOo , 3010 , ooOooo000oOO + 'kodible.png' , ooOooo000oOO + 'kodible.png' , '' )
  elif '2' in ooo0 :
   IiIIi1I1I11Ii ( ( I1i1i1iii ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , OooOoOo , 30010 , ooOooo000oOO + 'kodible.png' , ooOooo000oOO + 'kodible.png' , '' )
  elif '3' in ooo0 :
   IiIIi1I1I11Ii ( ( I1i1i1iii ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , OooOoOo , 30009 , ooOooo000oOO + 'kodible.png' , ooOooo000oOO + 'kodible.png' , '' )
   if 1 - 1: oOo0O0Ooo * Ii + IIIi * Ii + oO0o
 xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 30 - 30: I1ii11iIi11i . oO0o
def o0Oii1111i ( url ) :
 OOoOoOo = url
 o00OO00OoO = oO0OOoo0OO ( url )
 ooo0O = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( o00OO00OoO )
 for url , I1i1i1iii in ooo0O :
  if 'mp3' in I1i1i1iii :
   IIII ( ( I1i1i1iii ) . replace ( '%20' , ' ' ) , OOoOoOo + url , 10012 , ooOooo000oOO + 'kodible.png' , ooOooo000oOO + 'kodible.png' , '' )
  if 'wma' in I1i1i1iii :
   IIII ( ( I1i1i1iii ) . replace ( '%20' , ' ' ) , OOoOoOo + url , 10012 , ooOooo000oOO + 'kodible.png' , ooOooo000oOO + 'kodible.png' , '' )
  if 'm4b' in I1i1i1iii :
   IIII ( ( I1i1i1iii ) . replace ( '%20' , ' ' ) , OOoOoOo + url , 10012 , ooOooo000oOO + 'kodible.png' , ooOooo000oOO + 'kodible.png' , '' )
  elif '/' in I1i1i1iii :
   IiIIi1I1I11Ii ( ( I1i1i1iii ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , OOoOoOo + url , 30009 , ooOooo000oOO + 'kodible.png' , ooOooo000oOO + 'kodible.png' , '' )
   if 75 - 75: OooO0OoOOOO + IIiIiII11i / OoOo00o - OoOo00o / ii
   if 2 - 2: I11i
   if 19 - 19: IIiIiII11i
def OoOO ( url ) :
 o00OO00OoO = oO0OOoo0OO ( url )
 OOoOoOo = url
 iiIii = re . compile ( '<li><a href="(.+?)">(.+?)</a></li>' ) . findall ( o00OO00OoO )
 for url , I1i1i1iii in iiIii :
  if 'Parent' in I1i1i1iii :
   pass
  elif '.db' in I1i1i1iii :
   pass
  elif '.jpg' in I1i1i1iii :
   pass
  elif '.html' in I1i1i1iii :
   pass
  elif '.doc' in I1i1i1iii :
   pass
  elif 'mp3' in I1i1i1iii :
   IIII ( ( I1i1i1iii ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , OOoOoOo + url , 10012 , ooOooo000oOO + 'kodible.png' , ooOooo000oOO + 'kodible.png' , '' )
  elif 'm4a' in I1i1i1iii :
   IIII ( ( I1i1i1iii ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , OOoOoOo + url , 10012 , ooOooo000oOO + 'kodible.png' , ooOooo000oOO + 'kodible.png' , '' )
  else :
   IiIIi1I1I11Ii ( ( I1i1i1iii ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , OOoOoOo + url , 30010 , ooOooo000oOO + 'kodible.png' , ooOooo000oOO + 'kodible.png' , '' )
   if 32 - 32: OOooOOo * oOo0O0Ooo % O0OoO * Ii11Ii1I . o0o00Oo0O
   if 48 - 48: o0oOO0O00o0O * o0oOO0O00o0O
def I1I1 ( ) :
 IiIIi1I1I11Ii ( 'A-Z' , '' , 7 , ooOooo000oOO + 'kodible.png' , ooOooo000oOO + 'kodible.png' , '' )
 IiIIi1I1I11Ii ( 'All' , '' , 3 , ooOooo000oOO + 'kodible.png' , ooOooo000oOO + 'kodible.png' , '' )
 IiIIi1I1I11Ii ( 'Search' , '' , 14 , ooOooo000oOO + 'kodible.png' , ooOooo000oOO + 'kodible.png' , '' )
 if 4 - 4: I11i % OOooOOo * IIIii1II1II
def ii1IiIi11 ( ) :
 o00OO00OoO = oO0OOoo0OO ( i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9tcDNfZG93bmxvYWRzLmh0bQ==' ) )
 iiIii = re . compile ( '<td width=".+?" align="center">.+?<a href="(.*?)">.+?<img border="0" src="images/Squeeze%20(.*?).gif" width="74" height=".*?"></a></td>' , re . DOTALL ) . findall ( o00OO00OoO )
 for OooOoOo , I1i11 in iiIii :
  print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<' + OooOoOo + '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
  if '-x' in I1i11 :
   pass
  else :
   IiIIi1I1I11Ii ( I1i11 , ( i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) ) + ( OooOoOo ) . replace ( 'colour_it' , 'books_audio/audio_books_a' ) , 30008 , ( i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9pbWFnZXMvU3F1ZWV6ZSUyMA==' ) ) + I1i11 + '.gif' , ooOooo000oOO + 'kodible.png' , '' )
   if 22 - 22: OoOo00o
 xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 33 - 33: iI11I1II1I1I / Ii11Ii1I
 if 1 - 1: Ii11Ii1I
def IiiiI1 ( url ) :
 o00OO00OoO = oO0OOoo0OO ( url )
 iiIii = re . compile ( '<td width=".*?" height=".*?"><b>.*?<a href="(.*?)">(.*?)</a></b></td>' , re . DOTALL ) . findall ( o00OO00OoO )
 for url , I1i1i1iii in iiIii :
  if '</a>' in I1i1i1iii :
   pass
  elif '(' in I1i1i1iii :
   IiIIi1I1I11Ii ( ( I1i1i1iii ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '.mp3' , '' ) , i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) + url , 30005 , ooOooo000oOO + 'kodible.png' , ooOooo000oOO + 'kodible.png' , '' )
  else :
   IIII ( ( I1i1i1iii ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '.mp3' , '' ) , i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) + url , 30004 , ooOooo000oOO + 'kodible.png' , ooOooo000oOO + 'kodible.png' , '' )
   if 100 - 100: OoOo00o . Ii11Ii1I % ooOoO0O00 . O0OoO
 xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 79 - 79: oO0o % IIIii1II1II / iI11I1II1I1I + OOooOOo * oO0o
def IiI1 ( ) :
 iiIiIIIiiI = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 II11IiIi11 = iiIiIIIiiI . lower ( )
 o00OO00OoO = oO0OOoo0OO ( i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9jb21wbGV0ZV9saXN0Lmh0bQ==' ) )
 iiIii = re . compile ( '<td width=".+?">.*?<b>.+?<a href="(.*?)">(.*?)</a></b></td>' , re . DOTALL ) . findall ( o00OO00OoO )
 for OooOoOo , I1i1i1iii in iiIii :
  if iiIiIIIiiI in I1i1i1iii . lower ( ) :
   if '</a>' in I1i1i1iii :
    pass
   elif '(' in I1i1i1iii :
    IiIIi1I1I11Ii ( ( I1i1i1iii ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + OooOoOo , 30005 , ooOooo000oOO + 'kodible.png' , ooOooo000oOO + 'kodible.png' , '' )
   else :
    IIII ( ( I1i1i1iii ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + OooOoOo , 30004 , ooOooo000oOO + 'kodible.png' , ooOooo000oOO + 'kodible.png' , '' )
    if 28 - 28: Ii1I * ii . IIiIiII11i / Ii + OoOo00o
    if 38 - 38: OooO0OoOOOO . Ii11Ii1I
def IIIIIIIiI ( ) :
 o00OO00OoO = oO0OOoo0OO ( i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9jb21wbGV0ZV9saXN0Lmh0bQ==' ) )
 iiIii = re . compile ( '<td width=".+?">.*?<b>.+?<a href="(.*?)">(.*?)</a></b></td>' , re . DOTALL ) . findall ( o00OO00OoO )
 for OooOoOo , I1i1i1iii in iiIii :
  if '</a>' in I1i1i1iii :
   pass
  elif '(' in I1i1i1iii :
   IiIIi1I1I11Ii ( ( I1i1i1iii ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + OooOoOo , 30005 , ooOooo000oOO + 'kodible.png' , ooOooo000oOO + 'kodible.png' , '' )
  else :
   IIII ( ( I1i1i1iii ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + OooOoOo , 30004 , ooOooo000oOO + 'kodible.png' , ooOooo000oOO + 'kodible.png' , '' )
   if 12 - 12: o0oOO0O00o0O . OooO0OoOOOO . OOooOOo / o0o00Oo0O
 xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 58 - 58: I11i - IIiIiII11i % OoOo00o + IIIi . OOooOOo / OooO0OoOOOO
 if 8 - 8: Ii1I . oO0o * iI1iI1I1i1I + IIiIiII11i % Ii
def i1i1IiIiIi1Ii ( url ) :
 o00OO00OoO = oO0OOoo0OO ( url )
 iiIii = re . compile ( '<a href="(.+?)">Download</a></b></td>' ) . findall ( o00OO00OoO )
 for url in iiIii :
  OOoOoOo = ( i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) ) + url
  Resolve ( OOoOoOo )
  if 64 - 64: IIIii1II1II + ii * ii
def i1I ( url ) :
 o00OO00OoO = oO0OOoo0OO ( url )
 iiIii = re . compile ( '<td width="247">(.*?)</td>.*?<a href="(.+?)">' , re . DOTALL ) . findall ( o00OO00OoO )
 for I1i1i1iii , url in iiIii :
  if '<p align' in I1i1i1iii :
   pass
  elif '&nbsp;' in I1i1i1iii :
   pass
  else :
   IIII ( ( I1i1i1iii ) . replace ( '&nbsp;' , '' ) , i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) + url , 10012 , ooOooo000oOO + 'kodible.png' , ooOooo000oOO + 'kodible.png' , '' )
   if 36 - 36: oOo0O0Ooo * I1ii11iIi11i
 xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 77 - 77: OoOo00o % ooOoO0O00 - Ii11Ii1I
 if 93 - 93: oO0o * I1ii11iIi11i
def OO0ooo0o0 ( ) :
 o00OO00OoO = cloudflare . source ( i1111 ( 'aHR0cDovL3dhdGNoY2FydG9vbnNvbmxpbmUuZXUv' ) )
 iiIii = re . compile ( 'class="menu-item menu-item-type-.+?><a href="([^"]*)">(.+?)</a></li>' , re . DOTALL ) . findall ( o00OO00OoO )
 for OooOoOo , I1i1i1iii in iiIii :
  if 'ongoing' in OooOoOo :
   IIII ( '[COLORgreen]' + I1i1i1iii + '[/COLOR]' , OooOoOo , 21005 , ooOooo000oOO + 'on-going.png' , '' , '' )
  if 'cartoon-series' in OooOoOo :
   IIII ( '[COLORgreen]' + I1i1i1iii + '[/COLOR]' , OooOoOo , 21005 , ooOooo000oOO + 'cartoonseries.png' , '' , '' )
  if 'disney' in OooOoOo :
   IIII ( '[COLORgreen]' + I1i1i1iii + '[/COLOR]' , OooOoOo , 21005 , ooOooo000oOO + 'disneytoons.png' , '' , '' )
  if 'genre' in OooOoOo :
   IIII ( '[COLORgreen]' + I1i1i1iii + '[/COLOR]' , OooOoOo , 21005 , ooOooo000oOO + 'cartoongenre.png' , '' , '' )
  if 'years' in OooOoOo :
   IIII ( '[COLORgreen]' + I1i1i1iii + '[/COLOR]' , OooOoOo , 21005 , ooOooo000oOO + 'years.png' , '' , '' )
def oO0ooOoO ( url ) :
 o00OO00OoO = cloudflare . source ( url )
 iiIii = re . compile ( '<a href="([^"]*)" title="([^"]*)" rel="nofollow" id="featured-thumbnail">.+?<div class="featured-thumbnail"><img width="140" height="200" src="([^"]*)"' , re . DOTALL ) . findall ( o00OO00OoO )
 ooO0000o00O = re . compile ( '<button type="button"><a href="([^"]*)" target="_blank">(.+?)</a>' ) . findall ( o00OO00OoO )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' ) . findall ( o00OO00OoO )
 for url , I1i1i1iii , I1i11 in iiIii :
  IIII ( '[COLORgreen]' + I1i1i1iii + '[/COLOR]' , url , 21006 , I1i11 , I1i11 , I1i1i1iii )
 for url , I1i1i1iii in ooO0000o00O :
  IIII ( '[COLORgreen]' + I1i1i1iii + '[/COLOR]' , url , 21005 , ooOooo000oOO + 'watchcartoons.png' , '' , '' )
 for url in next :
  IIII ( '[COLORgreen]NEXT[/COLOR]' , url , 21005 , ooOooo000oOO + 'Next.png' , '' , '' )
def O0Ooo ( url ) :
 o00OO00OoO = cloudflare . source ( url )
 iiIii = re . compile ( '<li><a href="([^"]*)" >(.+?)</a></li>' , re . DOTALL ) . findall ( o00OO00OoO )
 oO00oOOo0Oo = re . compile ( 'file:"([^"]*)",type:"mp4",label:"([^"]*)"' , re . DOTALL ) . findall ( o00OO00OoO )
 IIi = re . compile ( 'src="([^"]*)" frameborder=' ) . findall ( o00OO00OoO )
 IIIIii = re . compile ( '<iframe src="([^"]*)"' ) . findall ( o00OO00OoO )
 for url , I1i1i1iii in iiIii :
  IIII ( '[COLORgreen]' + I1i1i1iii + '[/COLOR]' , url , 21007 , ooOooo000oOO + 'watchcartoons.png' , '' , '' )
 for url in IIi :
  IIII ( '[COLORgreen]PLAY[/COLOR]' , 'http:' + url , 222 , ooOooo000oOO + 'watchcartoons.png' , '' , '' )
 for url , I1i1i1iii in oO00oOOo0Oo :
  O0i1II1Iiii1I11 ( '[COLORgreen]' + I1i1i1iii + '[/COLOR]' , url , 222 , ooOooo000oOO + 'watchcartoons.png' , '' , '' )
 else :
  IIII ( '[COLORgreen]NO STREAMS AVAILABLE[/COLOR]' , url , 21005 , ooOooo000oOO + 'watchcartoons.png' , '' , '' )
def iIiI1 ( url ) :
 o00OO00OoO = cloudflare . source ( url )
 iiIii = re . compile ( 'file:"([^"]*)",type:"mp4",label:"([^"]*)"' , re . DOTALL ) . findall ( o00OO00OoO )
 for url , I1i1i1iii in iiIii :
  O0i1II1Iiii1I11 ( '[COLORgreen]' + I1i1i1iii + '[/COLOR]' , url , 222 , ooOooo000oOO + 'watchcartoons.png' , '' , '' )
  if 14 - 14: Ii1I
def II1i ( ) :
 O0II11i11II ( '[COLORgreen]CARTOONS[/COLOR]' , '' , 20001 , ooOooo000oOO + 'ORIGINCARTOON.png' )
 O0II11i11II ( '[COLORgreen]ANIME[/COLOR]' , 'https://kissanime.to/AnimeList' , 20001 , ooOooo000oOO + 'ORIGINCARTOON.png' )
 if 8 - 8: IIIi / IIIii1II1II . oOo0O0Ooo + Ii1I / Ii
def I1Iii1iI1 ( ) :
 O0II11i11II ( '[COLORgreen]BY NAME[/COLOR]' , 'http://kisscartoon.me/CartoonList' , 20002 , ooOooo000oOO + 'ORIGINCARTOON.png' )
 O0II11i11II ( '[COLORgreen]BY GENRE[/COLOR]' , 'http://kisscartoon.me/CartoonList' , 20003 , ooOooo000oOO + 'ORIGINCARTOON.png' )
 if 86 - 86: o0o00Oo0O
def O0o0oOooOoOo ( url ) :
 o00OO00OoO = cloudflare . source ( url )
 iiIii = re . compile ( 'href="(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( o00OO00OoO )
 for url , I1i1i1iii in iiIii :
  if '?c=' in url :
   O0II11i11II ( '[COLORgreen]' + I1i1i1iii + '[/COLOR]' , 'http://kisscartoon.me' + url , 20004 , ooOooo000oOO + 'ORIGINCARTOON.png' )
   if 49 - 49: IIIii1II1II . Ii1I . Ii - IIiIiII11i / Ii11Ii1I
def ooOo0O0o0 ( url ) :
 o00OO00OoO = cloudflare . source ( url )
 iiIii = re . compile ( 'href="(.+?)" title="(.+?)">/n(.+?)</a><br/>' , re . DOTALL ) . findall ( o00OO00OoO )
 for url , o0oo0O , I1i1i1iii in iiIii :
  if 'Genre' in url :
   O0II11i11II ( '[COLORgreen]' + I1i1i1iii + '[/COLOR]' , 'http://kisscartoon.me' + url , 20004 , ooOooo000oOO + 'ORIGINCARTOON.png' )
   if 19 - 19: IIIi + ooOoO0O00 . oOo0O0Ooo - I1ii11iIi11i
def iIi1I1 ( url ) :
 o00OO00OoO = cloudflare . source ( url )
 iiIii = re . compile ( 'src="(.+?)" style=.+?<a class="bigChar" href="(.+?)">(.+?)</a>.+?<p>(.+?)</p>' , re . DOTALL ) . findall ( o00OO00OoO )
 for url , o0oo0O , I1i1i1iii in iiIii :
  IIII ( '[COLORgreen]' + I1i1i1iii + '[/COLOR]' , 'http://kisscartoon.me' + url , 20005 , img , '' , o0oo0O )
  if 63 - 63: o0oOO0O00o0O * Ii1I . ii / IIIii1II1II * I1ii11iIi11i . O0OoO
def Ooo0 ( url ) :
 o00OO00OoO = cloudflare . source ( url )
 iiIii = re . compile ( '<img width="120" height="165" src="(.+?)" style=.+?<a class="bigChar" href="(.+?)">(.+?)</a>.+?<p>(.+?)</p>' , re . DOTALL ) . findall ( o00OO00OoO )
 for url , o0oo0O , I1i1i1iii in iiIii :
  IIII ( '[COLORgreen]' + I1i1i1iii + '[/COLOR]' , 'http://kisscartoon.me' + url , 20005 , img , '' , o0oo0O )
  if 91 - 91: ooOoO0O00 - iI11I1II1I1I
  if 55 - 55: oOo0O0Ooo * I11i % O0OoO . iI11I1II1I1I * IIIi
  if 92 - 92: IIIi - iI11I1II1I1I
  if 32 - 32: Ii11Ii1I % oO0o * oO0o + OooO0OoOOOO * IIiIiII11i * Ii11Ii1I
  if 11 - 11: OoOo00o % IIiIiII11i
def o0O0 ( ) :
 if 48 - 48: iI1iI1I1i1I - OooO0OoOOOO + iI11I1II1I1I + ii
 IIII ( '[COLORgreen]Cartoons[/COLOR]' , i1111 ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2NhcnRvb24=' ) , 10004 , ooOooo000oOO + 'ORIGINCARTOON.png' , i1iiIII111ii , '' )
 IIII ( '[COLORgreen]Search Cartoons[/COLOR]' , '' , 10005 , ooOooo000oOO + 'ORIGINCARTOON.png' , i1iiIII111ii , '' )
 if 4 - 4: IIiIiII11i . iI1iI1I1i1I + Ii11Ii1I * IIIi . O0OoO
def oOoOo ( ) :
 iiIiIIIiiI = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 II11IiIi11 = iiIiIIIiiI . lower ( )
 o00OO00OoO = oO0OOoo0OO ( i1111 ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2NhcnRvb24=' ) )
 iiIii = re . compile ( '<td><a href="(.+?)">(.+)</a></td>' ) . findall ( o00OO00OoO )
 for OooOoOo , I1i1i1iii in iiIii :
  if iiIiIIIiiI in I1i1i1iii . lower ( ) :
   if 'Dad!' in I1i1i1iii :
    pass
   elif 'Family Guy' in I1i1i1iii :
    pass
   elif '2 Stupid' in I1i1i1iii :
    pass
   elif 'The Zelfs' in I1i1i1iii :
    pass
   elif 'A Clone' in I1i1i1iii :
    pass
   elif 'A.T.O.M' in I1i1i1iii :
    pass
   elif 'Almost Naked' in I1i1i1iii :
    pass
   elif 'Angry Kid' in I1i1i1iii :
    pass
   elif 'Annoying Orange' in I1i1i1iii :
    pass
   elif 'Aqua Teen' in I1i1i1iii :
    pass
   elif 'Assy Mcgee' in I1i1i1iii :
    pass
   elif 'Astroblast' in I1i1i1iii :
    pass
   elif 'Atomic Betty' in I1i1i1iii :
    pass
   elif 'Axe Cop' in I1i1i1iii :
    pass
   elif 'Baby Playpen' in I1i1i1iii :
    pass
   elif 'Beavis and Butt' in I1i1i1iii :
    pass
   elif 'Celebrity Deathmatch' in I1i1i1iii :
    pass
   elif 'Clerks The' in I1i1i1iii :
    pass
   elif 'Crapston Villas' in I1i1i1iii :
    pass
   elif 'Duckman:' in I1i1i1iii :
    pass
   elif 'Stripperella' in I1i1i1iii :
    pass
   elif 'Vixen' in I1i1i1iii :
    pass
   else :
    IIII ( '[COLORgreen]' + I1i1i1iii + '[/COLOR]' , OooOoOo , 10006 , ooOooo000oOO + 'ORIGINCARTOON.png' , i1iiIII111ii , '' )
  xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 74 - 74: OoOo00o / Ii1I % I11i
def OO0o0OO0 ( url ) :
 I1i11i = oO0OOoo0OO ( url )
 iiIii = re . compile ( '<td><a href="(.+?)">(.+)</a></td>' ) . findall ( I1i11i )
 for url , I1i1i1iii in iiIii :
  if 'Dad!' in I1i1i1iii :
   pass
  elif 'Family Guy' in I1i1i1iii :
   pass
  elif '2 Stupid' in I1i1i1iii :
   pass
  elif 'The Zelfs' in I1i1i1iii :
   pass
  elif 'A Clone' in I1i1i1iii :
   pass
  elif 'A.T.O.M' in I1i1i1iii :
   pass
  elif 'Almost Naked' in I1i1i1iii :
   pass
  elif 'Angry Kid' in I1i1i1iii :
   pass
  elif 'Annoying Orange' in I1i1i1iii :
   pass
  elif 'Aqua Teen' in I1i1i1iii :
   pass
  elif 'Assy Mcgee' in I1i1i1iii :
   pass
  elif 'Astroblast' in I1i1i1iii :
   pass
  elif 'Atomic Betty' in I1i1i1iii :
   pass
  elif 'Axe Cop' in I1i1i1iii :
   pass
  elif 'Baby Playpen' in I1i1i1iii :
   pass
  elif 'Beavis and Butt' in I1i1i1iii :
   pass
  elif 'Celebrity Deathmatch' in I1i1i1iii :
   pass
  elif 'Clerks The' in I1i1i1iii :
   pass
  elif 'Crapston Villas' in I1i1i1iii :
   pass
  elif 'Duckman:' in I1i1i1iii :
   pass
  elif 'Stripperella' in I1i1i1iii :
   pass
  elif 'Vixen' in I1i1i1iii :
   pass
  else :
   IIII ( '[COLORgreen]' + I1i1i1iii + '[/COLOR]' , url , 10006 , ooOooo000oOO + 'ORIGINCARTOON.png' , i1iiIII111ii , '' )
 xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 56 - 56: Ii - I1ii11iIi11i / o0oOO0O00o0O / OOooOOo
def III1i111i ( url ) :
 I1i11i = oO0OOoo0OO ( url )
 ooo0O = re . compile ( '<img src="(.+?)" id="series_image" width="250" height="370" alt=".+?" />' ) . findall ( I1i11i )
 for I1i11 in ooo0O :
  iI1i = I1i11
 i111iiIIII = re . compile ( '<li><a href="(.+?)">Next</a></li>' ) . findall ( I1i11i )
 for url in i111iiIIII :
  IIII ( '[COLORgreen]NEXT PAGE[/COLOR]' , url , 10006 , ooOooo000oOO + 'Next.png' , i1iiIII111ii , '' )
 iiIii = re . compile ( '&nbsp;<a href="(.+?)">(.+?)</a>' ) . findall ( I1i11i )
 for url , I1i1i1iii in iiIii :
  i1II1IiIII111 ( '[COLORgreen]' + I1i1i1iii + '[/COLOR]' , url , 10007 , iI1i )
  if 80 - 80: I1ii11iIi11i * Ii11Ii1I + Ii1I * IIIii1II1II
  if 16 - 16: iI1iI1I1i1I / oOo0O0Ooo + oO0o % iI11I1II1I1I - ooOoO0O00 . OoOo00o
 xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 26 - 26: I11i * OooO0OoOOOO . ooOoO0O00
def ooOoOO ( url , IMAGE ) :
 I1i11i = oO0OOoo0OO ( url )
 iiIii = re . compile ( '"playlist">(.+?)</span></div><div><iframe src="(.+?)"' ) . findall ( I1i11i )
 for I1i1i1iii , url in iiIii :
  print I1i1i1iii + '     ' + url
  if 'easy' in url :
   Oo ( url )
   if 66 - 66: OooO0OoOOOO
   if 67 - 67: IIIi / oO0o . IIIii1II1II / IIIii1II1II - Ii11Ii1I - ii
  xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 46 - 46: o0o00Oo0O * I1ii11iIi11i / o0o00Oo0O + oO0o
def Oo ( url ) :
 I1i11i = oO0OOoo0OO ( url )
 iiIii = re . compile ( "url: '(.+?)'," ) . findall ( I1i11i )
 for url in iiIii :
  o0oOOo0O0O000 ( url )
  if 29 - 29: I11i / I1ii11iIi11i * Ii1I . I11i
  if 64 - 64: OoOo00o / O0OoO % Ii
  if 3 - 3: o0oOO0O00o0O . O0OoO % oOo0O0Ooo + Ii1I
def oo0o ( ) :
 if 51 - 51: IIIii1II1II . oOo0O0Ooo
 IIII ( '[COLORgreen]Stand Up[/COLOR]' , '' , 10014 , ooOooo000oOO + 'ORIGINSTANDUP.png' , i1iiIII111ii , '' )
 IIII ( '[COLORgreen]Search Comedian[/COLOR]' , '' , 10015 , ooOooo000oOO + 'ORIGINSTANDUP.png' , i1iiIII111ii , '' )
 IIII ( '[COLORgreen]Others[/COLOR]' , '' , 10017 , ooOooo000oOO + 'ORIGINSTANDUP.png' , i1iiIII111ii , '' )
 if 73 - 73: ii . oOo0O0Ooo / IIIi % Ii11Ii1I
def o0OO0O00o ( ) :
 o00OO00OoO = oO0OOoo0OO ( ( i1111 ( 'aHR0cDovL2JhY2syYmFzaWNzYnVpbGQuY28udWsvdGVzdC9zdGFuZHVwbGlzdC5waHA=' ) ) )
 iiIii = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( o00OO00OoO )
 for OooOoOo , I1i11 , I1i1i1iii in iiIii :
  if 'elete' in I1i1i1iii :
   pass
  else :
   i1II1IiIII111 ( '[COLORgreen]' + I1i1i1iii + '[/COLOR]' , OooOoOo , 222 , I1i11 )
   if 73 - 73: ooOoO0O00 - IIIii1II1II
def O0oo0O ( ) :
 iiIiIIIiiI = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 II11IiIi11 = iiIiIIIiiI . lower ( )
 o00OO00OoO = oO0OOoo0OO ( ( i1111 ( 'aHR0cDovL3d3dy5jb3VjaHRyaXBwZXIuY29tL2ZvcnVtMi9wYWdlLnBocD9wYWdlPTM=' ) ) )
 OO000o = re . compile ( '<tr>.+?<td width=".+?" align=".+?">.+?<img border=".+?" src="..(.+?)" width=".+?" height=".+?"></td>.+?<td width=".+?" valign=".+?" align=".+?"><font size=".+?">(.+?)</font></td>.+?<td width=".+?">(.+?)</td>' , re . DOTALL ) . findall ( o00OO00OoO )
 for I1i11 , iiI1iii , i1iII1IiiIiI1 in OO000o :
  for iiIiIIIiiI in iiI1iii :
   print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< img >>>>>>>>>>>>>>>>>>>>>>>>>>'
   OOoOOo00O0o0 = re . compile ( '<a href="(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( i1iII1IiiIiI1 )
   for OooOoOo , I1i1i1iii in OOoOOo00O0o0 :
    if 'tube' in OooOoOo :
     pass
    elif 'stage' in OooOoOo :
     i1II1IiIII111 ( '[COLORgreen]' + iiI1iii + '   -   ' + I1i1i1iii + '[/COLOR]' , ( OooOoOo ) . replace ( '" target="_blank' , '' ) , 10016 , 'http://couchtripper.com/' + I1i11 , )
    elif 'vee' in OooOoOo :
     pass
     if 83 - 83: iI11I1II1I1I % OOooOOo % I11i % IIIi . Ii1I % o0o00Oo0O
def iIiIi1ii ( ) :
 o00OO00OoO = oO0OOoo0OO ( ( i1111 ( 'aHR0cDovL3d3dy5jb3VjaHRyaXBwZXIuY29tL2ZvcnVtMi9wYWdlLnBocD9wYWdlPTM=' ) ) )
 OO000o = re . compile ( '<tr>.+?<td width=".+?" align=".+?">.+?<img border=".+?" src="..(.+?)" width=".+?" height=".+?"></td>.+?<td width=".+?" valign=".+?" align=".+?"><font size=".+?">(.+?)</font></td>.+?<td width=".+?">(.+?)</td>' , re . DOTALL ) . findall ( o00OO00OoO )
 for I1i11 , iiI1iii , i1iII1IiiIiI1 in OO000o :
  OOoOOo00O0o0 = re . compile ( '<a href="(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( i1iII1IiiIiI1 )
  for OooOoOo , I1i1i1iii in OOoOOo00O0o0 :
   if 'tube' in OooOoOo :
    pass
   elif 'stage' in OooOoOo :
    i1II1IiIII111 ( '[COLORgreen]' + iiI1iii + '   -   ' + I1i1i1iii + '[/COLOR]' , ( OooOoOo ) . replace ( '" target="_blank' , '' ) , 10016 , 'http://couchtripper.com/' + I1i11 )
   elif 'vee' in OooOoOo :
    pass
    if 28 - 28: iI11I1II1I1I + iI11I1II1I1I
    if 28 - 28: OoOo00o
 xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 52 - 52: oOo0O0Ooo + iI11I1II1I1I
def ooOO ( url ) :
 o00OO00OoO = oO0OOoo0OO ( url )
 print '>>>>>>>>>>>>>>>>>>>>>>>>' + url + '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'
 oOOOo00O00O = re . compile ( "url\[.+?\] = '(.+?)';" ) . findall ( o00OO00OoO )
 print '>>>>>>>>>>>>>>>>>>>>>>>' + ( str ( oOOOo00O00O ) ) + '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
 for url in oOOOo00O00O :
  o0oOOo0O0O000 ( ( url ) . replace ( '[' , '' ) . replace ( ']' , '' ) . replace ( '\'' , '' ) )
  if 45 - 45: OOooOOo
  if 68 - 68: o0o00Oo0O
  if 43 - 43: Ii1I - o0oOO0O00o0O
  if 70 - 70: o0oOO0O00o0O / IIIii1II1II % O0OoO - Ii11Ii1I
  if 47 - 47: o0oOO0O00o0O
  if 92 - 92: IIIii1II1II + OOooOOo % ooOoO0O00
  if 23 - 23: IIIi - IIIii1II1II + Ii11Ii1I - OOooOOo * OOooOOo . I1ii11iIi11i
def iIii11iI1II ( ) :
 if 42 - 42: O0OoO - oOo0O0Ooo + Ii1I % Ii11Ii1I
 IiIi1III ( '[COLOR darkgoldenrod]Open Pandora\'s Box[/COLOR]' , '' , 10029 , 'https://encrypted-tbn1.gstatic.com/images?q=tbn%3AANd9GcTQ9r4TA8yIw9ggxuwsHxWojo6tPVfgTe8QIOxOQwzNR2TavtCi6Q' , i1iiIII111ii , '' )
 IiIi1III ( '[COLOR darkgoldenrod]Search[/COLOR]' , '' , 10026 , 'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png' , i1iiIII111ii , '' )
 if 47 - 47: ii % o0o00Oo0O * o0oOO0O00o0O . Ii11Ii1I
 o00oooO0Oo ( 'movies' , 'MAIN' )
 if 38 - 38: o0o00Oo0O - OooO0OoOOOO % IIIi
def ooO ( ) :
 IiIi1III ( 'Search Pandoras Films' , '' , 10027 , 'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png' , i1iiIII111ii , '' )
 IiIi1III ( 'Search Pandoras TV' , '' , 10028 , 'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png' , i1iiIII111ii , '' )
 if 39 - 39: IIIii1II1II / Ii1I / oOo0O0Ooo * IIIi
 o00oooO0Oo ( 'movies' , 'MAIN' )
def Iii1Ii ( ) :
 if 30 - 30: o0o00Oo0O - o0oOO0O00o0O % I1ii11iIi11i
 iiIiIIIiiI = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 II11IiIi11 = iiIiIIIiiI . lower ( )
 O0Oo = [ '480p' , '720p' , '1080p' , 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' , '720paction' , '720padventure' , '720panimation' , '720pcomedy' , '720pcrime' , '720pdocumentary' , '720pdrama' , '720pfamily' , '720pfantasy' , '720phorror' , '720pmystery' , '720promance' , '720psci-Fi' , '720psport' , '720pthriller' , '720pwestern' , '1080paction' , '1080padventure' , '1080panimation' , '1080pcomedy' , '1080pcrime' , '1080pdocumentary' , '1080pdrama' , '1080pfamily' , '1080pfantasy' , '1080phorror' , '1080pmystery' , '1080promance' , '1080psci-Fi' , '1080psport' , '1080pthriller' , '1080pwestern' ]
 if 39 - 39: IIIii1II1II - ii + I1ii11iIi11i
 for O00 in O0Oo :
  i1iiIII1IIiIIII = IIIII + O00 + ooOoOoo0O
  o00OO00OoO = oO0OOoo0OO ( i1iiIII1IIiIIII )
  iiIii = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( o00OO00OoO )
  for OooOoOo , OOOOO0O00 , iIII , Iii , I1i1i1iii in iiIii :
   if iiIiIIIiiI in I1i1i1iii . lower ( ) :
    I1iIIII1 ( I1i1i1iii , OooOoOo , 222 , OOOOO0O00 , Iii , iIII )
    if 57 - 57: OOooOOo . iI11I1II1I1I % O0OoO % Ii11Ii1I * OOooOOo
    o00oooO0Oo ( 'movies' , 'MAIN' )
    xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
    if 8 - 8: OOooOOo . O0OoO % OoOo00o . oOo0O0Ooo % oOo0O0Ooo . Ii11Ii1I
    if 47 - 47: iI1iI1I1i1I + O0OoO + IIiIiII11i % Ii
def OOoOoo00Oo ( ) :
 if 9 - 9: IIiIiII11i * IIiIiII11i . Ii * iI11I1II1I1I
 iiIiIIIiiI = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 II11IiIi11 = iiIiIIIiiI . lower ( )
 O0Oo = [ 'a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' , 'p' , 'q' , 'r' , 's' , 't' , 'u' , 'v' , 'w' , 'x' , 'y' , 'z' ]
 if 18 - 18: oO0o . IIiIiII11i % OOooOOo % Ii11Ii1I
 for O00 in O0Oo :
  oo0 = IIIII + O00 + ooOoOoo0O
  o00OO00OoO = oO0OOoo0OO ( oo0 )
  iiIii = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( o00OO00OoO )
  for I1i1i1iii , iIII , OooOoOo , I1i11 , Iii , i1iIIi1II1iiI in iiIii :
   if iiIiIIIiiI in I1i1i1iii . lower ( ) :
    IiIi1III ( I1i1i1iii , OooOoOo , i1iIIi1II1iiI , I1i11 , Iii , iIII )
    if 31 - 31: I11i % iI1iI1I1i1I + iI11I1II1I1I + Ii * IIIi
    o00oooO0Oo ( 'movies' , 'MAIN' )
    xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
    if 45 - 45: IIIii1II1II * IIIi . O0OoO - IIIi + OooO0OoOOOO
    if 34 - 34: IIIii1II1II . I1ii11iIi11i
def OOoO0oO00o ( ) :
 if 10 - 10: oO0o
 I1i11i = oO0OOoo0OO ( IIIII + 'spongemain.php' )
 iiIii = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( I1i11i )
 for I1i1i1iii , iIII , OooOoOo , I1i11 , Iii , i1iIIi1II1iiI in iiIii :
  IiIi1III ( I1i1i1iii , OooOoOo , i1iIIi1II1iiI , I1i11 , Iii , iIII )
  o00oooO0Oo ( 'movies' , 'MAIN' )
def iii1OO0o0oO0O000o ( url ) :
 if 47 - 47: IIIi - oO0o / Ii11Ii1I * ii / Ii11Ii1I . I1ii11iIi11i
 xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
 iiII1IiIi1iI1 = ( '%s%s' % ( oOiiI1Ii11II1I , url ) )
 O000oo0O = oO0OOoo0OO ( url )
 iiIii = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( O000oo0O )
 for url , OOOOO0O00 , iIII , I1Ii11II1I1 , I1i1i1iii in iiIii :
  I1iIIII1 ( I1i1i1iii , url , 222 , OOOOO0O00 , I1Ii11II1I1 , iIII )
  if 41 - 41: o0o00Oo0O * O0OoO - OOooOOo . Ii11Ii1I
  o00oooO0Oo ( 'movies' , 'MAIN' )
  if 65 - 65: I1ii11iIi11i . ii
  xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 70 - 70: I1ii11iIi11i - OoOo00o . iI11I1II1I1I % iI1iI1I1i1I / OOooOOo - o0o00Oo0O
  if 55 - 55: o0oOO0O00o0O - oO0o
def o0i1I11iI1iiI ( url ) :
 if 48 - 48: iI1iI1I1i1I . ii . oOo0O0Ooo . OOooOOo % Ii1I / o0oOO0O00o0O
 I1i11i = oO0OOoo0OO ( url )
 iiIii = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( I1i11i )
 for I1i1i1iii , iIII , url , I1i11 , Iii , i1iIIi1II1iiI in iiIii :
  IiIi1III ( I1i1i1iii , url , i1iIIi1II1iiI , I1i11 , Iii , iIII )
  if 11 - 11: ooOoO0O00 % oO0o % o0oOO0O00o0O
  o00oooO0Oo ( 'movies' , 'MAIN' )
  if 99 - 99: O0OoO / iI11I1II1I1I - Ii11Ii1I * Ii1I % oOo0O0Ooo
  if 13 - 13: oO0o
 xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 70 - 70: IIIi + o0o00Oo0O . OoOo00o * Ii11Ii1I
def I1iIIII1 ( name , url , mode , iconimage , fanart , description ) :
 if 2 - 2: ii . IIIii1II1II . OooO0OoOOOO
 I1iIII1IiiI = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 OOoooOoO0Oo = True
 Oo000 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 Oo000 . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 Oo000 . setProperty ( "Fanart_Image" , fanart )
 OOoooOoO0Oo = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = I1iIII1IiiI , listitem = Oo000 , isFolder = False )
 return OOoooOoO0Oo
 if 48 - 48: Ii % OoOo00o
def IiIi1III ( name , url , mode , iconimage , fanart , description ) :
 if 29 - 29: o0oOO0O00o0O + Ii % iI1iI1I1i1I
 I1iIII1IiiI = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 OOoooOoO0Oo = True
 Oo000 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 Oo000 . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 Oo000 . setProperty ( "Fanart_Image" , fanart )
 OOoooOoO0Oo = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = I1iIII1IiiI , listitem = Oo000 , isFolder = True )
 return OOoooOoO0Oo
if 93 - 93: OOooOOo % iI11I1II1I1I
if 90 - 90: oOo0O0Ooo - IIIii1II1II / Ii11Ii1I / o0o00Oo0O / iI1iI1I1i1I
if 87 - 87: OOooOOo / OooO0OoOOOO + iI11I1II1I1I
if 93 - 93: iI11I1II1I1I + OoOo00o % O0OoO
if 21 - 21: IIIii1II1II
if 6 - 6: OooO0OoOOOO
if 46 - 46: OooO0OoOOOO + OoOo00o
if 79 - 79: ii - OooO0OoOOOO * OooO0OoOOOO . OOooOOo
if 100 - 100: IIiIiII11i * iI1iI1I1i1I % oOo0O0Ooo / Ii1I
if 90 - 90: Ii1I . O0OoO . OOooOOo . Ii11Ii1I
if 4 - 4: Ii11Ii1I + OOooOOo % Ii1I / Ii
if 74 - 74: IIiIiII11i . o0o00Oo0O - oOo0O0Ooo + OooO0OoOOOO % Ii % OOooOOo
if 78 - 78: Ii11Ii1I + OOooOOo + OooO0OoOOOO - OooO0OoOOOO . Ii / oO0o
if 27 - 27: Ii11Ii1I - o0o00Oo0O % iI1iI1I1i1I * IIIi . OooO0OoOOOO % iI11I1II1I1I
if 37 - 37: ii + o0o00Oo0O - ooOoO0O00 % O0OoO
def i1I1i1i ( string ) :
 if iiiiiIIii == 'true' :
  xbmc . log ( "[addon.live.GenieTV-%s]: %s" % ( addon_version , string ) )
  if 36 - 36: IIiIiII11i % o0o00Oo0O
def ii11IiI1 ( name , url , iconimage , fanart , mode , playlist = None , regexs = None ) :
 Oo0Oo0o0oo0O0 = [ ]
 try :
  if 53 - 53: O0OoO / iI11I1II1I1I - oO0o + OoOo00o
  name = name . encode ( 'utf-8' , 'ignore' )
 except :
  pass
 if os . path . exists ( I11i1 ) == False :
  i1I1i1i ( 'Making Favorites File' )
  Oo0Oo0o0oo0O0 . append ( ( name , url , iconimage , fanart , mode , playlist , regexs ) )
  i11i1iiiII = open ( I11i1 , "w" )
  i11i1iiiII . write ( json . dumps ( Oo0Oo0o0oo0O0 ) )
  i11i1iiiII . close ( )
 else :
  i1I1i1i ( 'Appending Favorites' )
  i11i1iiiII = open ( I11i1 ) . read ( )
  ii1IIIIiI11I = json . loads ( i11i1iiiII )
  ii1IIIIiI11I . append ( ( name , url , iconimage , fanart , mode ) )
  Oo0O = open ( I11i1 , "w" )
  Oo0O . write ( json . dumps ( ii1IIIIiI11I ) )
  Oo0O . close ( )
  if 31 - 31: Ii11Ii1I
  if 18 - 18: O0OoO + Ii11Ii1I
def ii11i11 ( ) :
 OooiiIii = json . loads ( open ( I11i1 ) . read ( ) )
 iii1IIiI = len ( OooiiIii )
 for i1i1Ii11Ii in OooiiIii :
  I1i1i1iii = i1i1Ii11Ii [ 0 ]
  OooOoOo = i1i1Ii11Ii [ 1 ]
  OOOOO0O00 = i1i1Ii11Ii [ 2 ]
  try :
   O000oOo = i1i1Ii11Ii [ 3 ]
   if O000oOo == None :
    raise
  except :
   if o0oO0 . getSetting ( 'use_thumb' ) == "true" :
    O000oOo = OOOOO0O00
   else :
    O000oOo = Iii
  try : IiiIIi1 = i1i1Ii11Ii [ 5 ]
  except : IiiIIi1 = None
  try : iI1iIiiI = i1i1Ii11Ii [ 6 ]
  except : iI1iIiiI = None
  if 95 - 95: iI11I1II1I1I + I1ii11iIi11i * IIiIiII11i + O0OoO + o0o00Oo0O * iI1iI1I1i1I
  if i1i1Ii11Ii [ 4 ] == 0 :
   IIII ( I1i1i1iii , OooOoOo , '' , OOOOO0O00 , Iii , '' , 'fav' )
  else :
   IIII ( I1i1i1iii , OooOoOo , i1i1Ii11Ii [ 4 ] , OOOOO0O00 , Iii , '' , 'fav' )
   if 45 - 45: IIiIiII11i % O0OoO % OooO0OoOOOO + Ii1I . ooOoO0O00 . OOooOOo
def O0o0OO00 ( name ) :
 ii1IIIIiI11I = json . loads ( open ( I11i1 ) . read ( ) )
 for iIi11i in range ( len ( ii1IIIIiI11I ) ) :
  if ii1IIIIiI11I [ iIi11i ] [ 0 ] == name :
   del ii1IIIIiI11I [ iIi11i ]
   Oo0O = open ( I11i1 , "w" )
   Oo0O . write ( json . dumps ( ii1IIIIiI11I ) )
   Oo0O . close ( )
   break
 xbmc . executebuiltin ( "XBMC.Container.Refresh" )
 if 56 - 56: Ii . O0OoO / o0oOO0O00o0O
 if 48 - 48: oO0o * IIIii1II1II + iI11I1II1I1I / IIiIiII11i
def III1ii1I ( ) :
 oOO0OO0oOO = os . path . join ( OOooO0OOoo , 'addons.ini' )
 ooooO = open ( oOO0OO0oOO , "w+" )
 if 92 - 92: I11i / I11i * Ii11Ii1I
 ooooO . write ( r'# This file contains the "built-in" channels' + '\n' )
 ooooO . write ( r'# It is parsed by Pythons ConfigParser' + '\n\n' )
 ooooO . write ( r'[plugin.video.GenieTv]' + '\n' )
 ooooO . write ( r'BBC One=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F191.m3u8&mode=10012&name=[COLORgreen]BBC+One%0D[%2FCOLOR]' + '\n' )
 ooooO . write ( r'BBC Two=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F190.m3u8&mode=10012&name=[COLORgreen]BBC+Two%0D[%2FCOLOR]' + '\n' )
 ooooO . write ( r'BBC Four=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F188.m3u8&mode=10012&name=[COLORgreen]BBC+Four%0D[%2FCOLOR]' + '\n' )
 ooooO . write ( r'ITV=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F208.m3u8&mode=10012&name=[COLORgreen]ITV1%0D[%2FCOLOR]' + '\n' )
 ooooO . write ( r'ITV2=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F207.m3u8&mode=10012&name=[COLORgreen]ITV2%0D[%2FCOLOR]' + '\n' )
 ooooO . write ( r'ITV3=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F206.m3u8&mode=10012&name=[COLORgreen]ITV3%0D[%2FCOLOR]' + '\n' )
 ooooO . write ( r'ITV4=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F205.m3u8&mode=10012&name=[COLORgreen]ITV4%0D[%2FCOLOR]' + '\n' )
 ooooO . write ( r'Channel 4=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F183.m3u8&mode=10012&name=[COLORgreen]Channel+4%0D[%2FCOLOR]' + '\n' )
 ooooO . write ( r'Channel 5=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F185.m3u8&mode=10012&name=[COLORgreen]Channel+5%0D[%2FCOLOR]' + '\n' )
 ooooO . write ( r'5STAR=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F187.m3u8&mode=10012&name=[COLORgreen]5%2A%0D[%2FCOLOR]' + '\n' )
 ooooO . write ( r'5 USA=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F186.m3u8&mode=10012&name=[COLORgreen]5USA%0D[%2FCOLOR]' + '\n' )
 ooooO . write ( r'RTE One=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F194.m3u8&mode=10012&name=[COLORgreen]RTE+One%0D[%2FCOLOR]' + '\n' )
 ooooO . write ( r'RTE Two=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F193.m3u8&mode=10012&name=[COLORgreen]RTE+Two%0D[%2FCOLOR]' + '\n' )
 ooooO . write ( r'TG4=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F192.m3u8&mode=10012&name=[COLORgreen]TG4%0D[%2FCOLOR]' + '\n' )
 ooooO . write ( r'Sky1=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F32.m3u8&mode=10012&name=[COLORgreen]Sky+1%0D[%2FCOLOR]' + '\n' )
 ooooO . write ( r'Sky2=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F33.m3u8&mode=10012&name=[COLORgreen]Sky+2%0D[%2FCOLOR]' + '\n' )
 ooooO . write ( r'Sky Living=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F35.m3u8&mode=10012&name=[COLORgreen]Sky+Living%0D[%2FCOLOR]' + '\n' )
 ooooO . write ( r'Sky Atlantic=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F34.m3u8&mode=10012&name=[COLORgreen]Sky+Atlantic%0D[%2FCOLOR]' + '\n' )
 ooooO . write ( r'Dave=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F325.m3u8&mode=10012&name=[COLORgreen]Dave%0D[%2FCOLOR]' + '\n' )
 ooooO . write ( r'Pick=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F324.m3u8&mode=10012&name=[COLORgreen]Pick%0D[%2FCOLOR]' + '\n' )
 ooooO . write ( r'GOLD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F326.m3u8&mode=10012&name=[COLORgreen]Gold%0D[%2FCOLOR]' + '\n' )
 ooooO . write ( r'Watch HD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F518.m3u8&mode=10012&name=[COLORgreen]Watch%0D[%2FCOLOR]' + '\n' )
 ooooO . write ( r'YESTERDAY=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F377.m3u8&mode=10012&name=[COLORgreen]Yesterday%0D[%2FCOLOR]' + '\n' )
 ooooO . write ( r'Comedy Central=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F181.m3u8&mode=10012&name=[COLORgreen]Comedy+Central%0D[%2FCOLOR]' + '\n' )
 ooooO . write ( r'London Live=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F830.m3u8&mode=10012&name=[COLORgreen]London+Live%0D[%2FCOLOR]' + '\n' )
 ooooO . write ( r'Disney Junior=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F230.m3u8&mode=10012&name=[COLORgreen]Disney+Jr.%0D[%2FCOLOR]' + '\n' )
 ooooO . write ( r'Disney Chnl=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F231.m3u8&mode=10012&name=[COLORgreen]Disney+Channel%0D[%2FCOLOR]' + '\n' )
 ooooO . write ( r'Animal Planet=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F198.m3u8&mode=10012&name=[COLORgreen]Animal+Planet%0D[%2FCOLOR]' + '\n' )
 ooooO . write ( r'Nat Geo=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F197.m3u8&mode=10012&name=[COLORgreen]National+Geographic+Channel%0D[%2FCOLOR]' + '\n' )
 ooooO . write ( r'Discovery=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F200.m3u8&mode=10012&name=[COLORgreen]Discovery+Channel%0D[%2FCOLOR]' + '\n' )
 ooooO . write ( r'Discovery Science=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F199.m3u8&mode=10012&name=[COLORgreen]Discovery+Science%0D[%2FCOLOR]' + '\n' )
 ooooO . write ( r'Disc.Turbo=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F168.m3u8&mode=10012&name=[COLORgreen]Discovery+Turbo%0D[%2FCOLOR]' + '\n' )
 ooooO . write ( r'Food Network=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F639.m3u8&mode=10012&name=[COLORgreen]Food+Network%0D[%2FCOLOR]' + '\n' )
 ooooO . write ( r'MTV MUSIC=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F234.m3u8&mode=10012&name=[COLORgreen]MTV+Music%0D[%2FCOLOR]' + '\n' )
 ooooO . write ( r'Film4=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F182.m3u8&mode=10012&name=[COLORgreen]Film4%0D[%2FCOLOR]' + '\n' )
 ooooO . write ( r'True Movies=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F853.m3u8&mode=10012&name=[COLORgreen]True+Movies%0D[%2FCOLOR]' + '\n' )
 ooooO . write ( r'True Movies 2=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F852.m3u8&mode=10012&name=[COLORgreen]True+Movies+2%0D[%2FCOLOR]' + '\n' )
 ooooO . write ( r'Sky Action=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F732.m3u8&mode=10012&name=[COLORgreen]Sky+Movies+Action+%26+Adventure%0D[%2FCOLOR]' + '\n' )
 ooooO . write ( r'Sky ScFiHorror=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F511.m3u8&mode=10012&name=[COLORgreen]Sky+Movies+Sci-Fi+%26+Horror%0D[%2FCOLOR]' + '\n' )
 ooooO . write ( r'SkyPremiereHD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F516.m3u8&mode=10012&name=[COLORgreen]Sky+Movies+Premiere%0D[%2FCOLOR]' + '\n' )
 ooooO . write ( r'Sky Greats=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F512.m3u8&mode=10012&name=[COLORgreen]Sky+Movies+Greats%0D[%2FCOLOR]' + '\n' )
 ooooO . write ( r'Sky Family=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F509.m3u8&mode=10012&name=[COLORgreen]Sky+Movies+Family%0D[%2FCOLOR]' + '\n' )
 ooooO . write ( r'Sky DramaRom=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F510.m3u8&mode=10012&name=[COLORgreen]Sky+Movies+Drama+%26+Romance%0D[%2FCOLOR]' + '\n' )
 ooooO . write ( r'Sky Thriller=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F514.m3u8&mode=10012&name=[COLORgreen]Sky+Movies+Crime+%26+Thriller%0D[%2FCOLOR]' + '\n' )
 ooooO . write ( r'Sky Comedy=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F513.m3u8&mode=10012&name=[COLORgreen]Sky+Movies+Comedy%0D[%2FCOLOR]' + '\n' )
 ooooO . write ( r'Sky Showcase=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F46.m3u8&mode=10012&name=[COLORgreen]Sky+Movies+Showcase%0D[%2FCOLOR]' + '\n' )
 ooooO . write ( r'Sky Select=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F45.m3u8&mode=10012&name=[COLORgreen]Sky+Movies+Select%0D[%2FCOLOR]' + '\n' )
 ooooO . write ( r'Sky Disney=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F195.m3u8&mode=10012&name=[COLORgreen]Sky+Movies+Disney%0D[%2FCOLOR]' + '\n' )
 ooooO . write ( r'Sky Sports 1=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F18.m3u8&mode=10012&name=[COLORgreen]Sky+Sports+1%0D[%2FCOLOR]' + '\n' )
 ooooO . write ( r'Sky Sports 2=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F19.m3u8&mode=10012&name=[COLORgreen]Sky+Sports+2%0D[%2FCOLOR]' + '\n' )
 ooooO . write ( r'Sky Sports 3=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F20.m3u8&mode=10012&name=[COLORgreen]Sky+Sports+3%0D[%2FCOLOR]' + '\n' )
 ooooO . write ( r'Sky Sports 4=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F21.m3u8&mode=10012&name=[COLORgreen]Sky+Sports+4%0D[%2FCOLOR]' + '\n' )
 ooooO . write ( r'Sky Sports 5=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F22.m3u8&mode=10012&name=[COLORgreen]Sky+Sports+5%0D[%2FCOLOR]' + '\n' )
 ooooO . write ( r'Sky Sports F1=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F24.m3u8&mode=10012&name=[COLORgreen]Sky+Sports+F1%0D[%2FCOLOR]' + '\n' )
 ooooO . write ( r'Sky Sports News=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F23.m3u8&mode=10012&name=[COLORgreen]Sky+Sports+News%0D[%2FCOLOR]' + '\n' )
 ooooO . write ( r'BT Sport 1=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F309.m3u8&mode=10012&name=[COLORgreen]BT+Sport+1%0D[%2FCOLOR]' + '\n' )
 ooooO . write ( r'BT Sport 2=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F26.m3u8&mode=10012&name=[COLORgreen]BT+Sport+2%0D[%2FCOLOR]' + '\n' )
 ooooO . write ( r'BT Sport Europe=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F705.m3u8&mode=10012&name=[COLORgreen]BT+Sport+Europe%0D[%2FCOLOR]' + '\n' )
 ooooO . write ( r'BT Sport ESPN=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F28.m3u8&mode=10012&name=[COLORgreen]BT+Sport+ESPN%0D[%2FCOLOR]' + '\n' )
 ooooO . write ( r'Box Nation=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F173.m3u8&mode=10012&name=[COLORgreen]Box+Nation%0D[%2FCOLOR]' + '\n' )
 ooooO . write ( r'WWENetwork=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F178.m3u8&mode=10012&name=[COLORgreen]WWENetwork%0D[%2FCOLOR]' + '\n' )
 ooooO . write ( r'Eurosport=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F269.m3u8&mode=10012&name=[COLORgreen]Eurosport+1%0D[%2FCOLOR]' + '\n' )
 ooooO . write ( r'Eurosport 2=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F748.m3u8&mode=10012&name=[COLORgreen]Eurosport+2%0D[%2FCOLOR]' + '\n' )
 ooooO . write ( r'At The Races=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F170.m3u8&mode=10012&name=[COLORgreen]At+the+Races%0D[%2FCOLOR]' + '\n' )
 ooooO . write ( r'Racing UK=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F171.m3u8&mode=10012&name=[COLORgreen]Racing+UK%0D[%2FCOLOR]' + '\n' )
 ooooO . write ( r'Poker central US=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F826.m3u8&mode=10012&name=[COLORgreen]Poker+central+US%0D[%2FCOLOR]' + '\n' )
 if 19 - 19: Ii11Ii1I
 if 55 - 55: IIIii1II1II % IIIii1II1II / o0o00Oo0O % o0oOO0O00o0O - I11i . I1ii11iIi11i
 if 49 - 49: iI11I1II1I1I * ooOoO0O00 . ii
def OOOO0oOo00O ( ) :
 if 32 - 32: OooO0OoOOOO % Ii11Ii1I - oOo0O0Ooo
 IIII ( '[COLORgreen]Recent Episodes[/COLOR]' , '' , 10019 , ooOooo000oOO + 'dtv.png' , i1iiIII111ii , '' )
 IIII ( '[COLORgreen]Genres[/COLOR]' , '' , 10020 , ooOooo000oOO + 'dtv.png' , i1iiIII111ii , '' )
 IIII ( '[COLORgreen]Search[/COLOR]' , '' , 10021 , ooOooo000oOO + 'dtv.png' , i1iiIII111ii , '' )
 if 71 - 71: o0oOO0O00o0O
def Iiii1i11ii1Ii ( ) :
 if 12 - 12: IIIii1II1II . Ii11Ii1I
 I1i11i = cloudflare . source ( i1111 ( 'aHR0cDovL2RpemlsYWIuY29t' ) )
 iiIii = re . compile ( '<li id=".+?">.+?<a href="(.+?)">.+?<img width="40" height="40" src="(.+?)" alt=""/>.+?<span class="title">\n(.+?)</span>.+?<span class="alt-title">\n(.+?)</span>.+?</a>.+?</li>' , re . DOTALL ) . findall ( I1i11i )
 for OooOoOo , I1i11 , I1i1i1iii , I1111i in iiIii :
  IIII ( I1i1i1iii + '  -  ' + ( I1111i ) . replace ( 'sezon' , 'Season' ) . replace ( 'bölüm' , 'Episode' ) , OooOoOo , 10023 , ooOooo000oOO + 'dtv.png' , i1iiIII111ii , '' )
  if 79 - 79: IIIi / I1ii11iIi11i / o0oOO0O00o0O . IIIi * ii + I11i
  if 73 - 73: o0o00Oo0O - Ii1I
  if 2 - 2: IIiIiII11i / IIIi
def OoOoO0oOOooo ( ) :
 if 99 - 99: iI11I1II1I1I
 IIII ( '[COLORgreen]Action[/COLOR]' , 'Aksiyon' , 10024 , ooOooo000oOO + 'dtv.png' , i1iiIII111ii , '' )
 IIII ( '[COLORgreen]Adventure[/COLOR]' , 'Macera' , 10024 , ooOooo000oOO + 'dtv.png' , i1iiIII111ii , '' )
 IIII ( '[COLORgreen]Animation[/COLOR]' , 'Animasyon' , 10024 , ooOooo000oOO + 'dtv.png' , i1iiIII111ii , '' )
 IIII ( '[COLORgreen]Anime[/COLOR]' , 'Anime' , 10024 , ooOooo000oOO + 'dtv.png' , i1iiIII111ii , '' )
 IIII ( '[COLORgreen]Biography[/COLOR]' , 'Biyografi' , 10024 , ooOooo000oOO + 'dtv.png' , i1iiIII111ii , '' )
 IIII ( '[COLORgreen]Comedy[/COLOR]' , 'Komedi' , 10024 , ooOooo000oOO + 'dtv.png' , i1iiIII111ii , '' )
 IIII ( '[COLORgreen]Crime[/COLOR]' , 'Su%C3%A7' , 10024 , ooOooo000oOO + 'dtv.png' , i1iiIII111ii , '' )
 IIII ( '[COLORgreen]Documentary[/COLOR]' , 'Belgesel' , 10024 , ooOooo000oOO + 'dtv.png' , i1iiIII111ii , '' )
 IIII ( '[COLORgreen]Drama[/COLOR]' , 'Dram' , 10024 , ooOooo000oOO + 'dtv.png' , i1iiIII111ii , '' )
 IIII ( '[COLORgreen]Family[/COLOR]' , 'Aile' , 10024 , ooOooo000oOO + 'dtv.png' , i1iiIII111ii , '' )
 IIII ( '[COLORgreen]Fantasy[/COLOR]' , 'Fantastik' , 10024 , ooOooo000oOO + 'dtv.png' , i1iiIII111ii , '' )
 IIII ( '[COLORgreen]History[/COLOR]' , 'Tarih' , 10024 , ooOooo000oOO + 'dtv.png' , i1iiIII111ii , '' )
 IIII ( '[COLORgreen]Horror[/COLOR]' , 'Korku' , 10024 , ooOooo000oOO + 'dtv.png' , i1iiIII111ii , '' )
 IIII ( '[COLORgreen]Mini-Series[/COLOR]' , 'Mini%20Dizi' , 10024 , ooOooo000oOO + 'dtv.png' , i1iiIII111ii , '' )
 IIII ( '[COLORgreen]Musical[/COLOR]' , 'M%C3%BCzikal' , 10024 , ooOooo000oOO + 'dtv.png' , i1iiIII111ii , '' )
 IIII ( '[COLORgreen]Mystery[/COLOR]' , 'Gizem' , 10024 , ooOooo000oOO + 'dtv.png' , i1iiIII111ii , '' )
 IIII ( '[COLORgreen]Romance[/COLOR]' , 'Romantik' , 10024 , ooOooo000oOO + 'dtv.png' , i1iiIII111ii , '' )
 IIII ( '[COLORgreen]Science Fiction[/COLOR]' , 'Bilim%20Kurgu' , 10024 , ooOooo000oOO + 'dtv.png' , i1iiIII111ii , '' )
 IIII ( '[COLORgreen]Sport[/COLOR]' , 'Spor' , 10024 , ooOooo000oOO + 'dtv.png' , i1iiIII111ii , '' )
 IIII ( '[COLORgreen]Thriller[/COLOR]' , 'Gerilim' , 10024 , ooOooo000oOO + 'dtv.png' , i1iiIII111ii , '' )
 IIII ( '[COLORgreen]War[/COLOR]' , 'Sava%C5%9F' , 10024 , ooOooo000oOO + 'dtv.png' , i1iiIII111ii , '' )
 IIII ( '[COLORgreen]Western[/COLOR]' , 'Tarih' , 10024 , ooOooo000oOO + 'dtv.png' , i1iiIII111ii , '' )
 IIII ( '[COLORgreen]Youth[/COLOR]' , 'Gen%C3%A7lik' , 10024 , ooOooo000oOO + 'dtv.png' , i1iiIII111ii , '' )
 if 14 - 14: Ii1I % oOo0O0Ooo . IIiIiII11i . oOo0O0Ooo - O0OoO
def I1ii1 ( url ) :
 OooO0OO = 'http://dizilab.com/arsiv?limit=100&tur=' + url + '&orderby=&ulke=&order=&yil=&dizi_adi='
 o00OO00OoO = cloudflare . source ( OooO0OO )
 iiIii = re . compile ( '<div class="tv-series-single">.+?<a href="(.+?)" class="film-image">.+?<img src="(.+?)" alt=""/>.+?<span class="position">.+?</span>\n(.+?)</a>' , re . DOTALL ) . findall ( o00OO00OoO )
 for url , I1i11 , I1i1i1iii in iiIii :
  IIII ( '[COLORgreen]' + I1i1i1iii + '[/COLOR]' , url , 10022 , ooOooo000oOO + 'dtv.png' , i1iiIII111ii , '' )
  if 48 - 48: O0OoO / iI11I1II1I1I + IIIii1II1II + iI11I1II1I1I . oO0o
  if 60 - 60: IIIi
  if 98 - 98: O0OoO
  if 34 - 34: iI11I1II1I1I * iI1iI1I1i1I * iI1iI1I1i1I / Ii1I
def IIIIIIi1i ( ) :
 if 26 - 26: iI11I1II1I1I - o0o00Oo0O . o0o00Oo0O
 iiIiIIIiiI = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 II11IiIi11 = iiIiIIIiiI . lower ( )
 OooOoOo = ( i1111 ( 'aHR0cDovL2RpemlsYWIuY29tL2Fyc2l2P2xpbWl0PSZ0dXI9Jm9yZGVyYnk9JnVsa2U9Jm9yZGVyPSZ5aWw9JmRpemlfYWRpPQ==' ) ) + ( iiIiIIIiiI ) . replace ( ' ' , '+' )
 o00OO00OoO = cloudflare . source ( OooOoOo )
 iiIii = re . compile ( '<a href="(.+?)" class="film-image">\n<img src="(.+?)" alt=""/>\n</a>\n<div class="tss-detail">\n<a class="title" style="" href=".+?">\n<span class="position">.+?</span>\n(.+?)</a>' ) . findall ( o00OO00OoO )
 for OooOoOo , I1i11 , I1i1i1iii in iiIii :
  if iiIiIIIiiI in I1i1i1iii . lower ( ) :
   IIII ( '[COLORgreen]' + I1i1i1iii + '[/COLOR]' , OooOoOo , 10022 , ooOooo000oOO + 'dtv.png' )
   if 68 - 68: IIIii1II1II + OoOo00o . o0o00Oo0O . Ii11Ii1I % ooOoO0O00 % IIIii1II1II
   if 50 - 50: OooO0OoOOOO + I11i
   if 96 - 96: oO0o
def oOOoO ( url ) :
 o00OO00OoO = cloudflare . source ( url )
 iiIii = re . compile ( '<a class="season" href="(.+?)">\n(.+?)\n</a>.+?<a class="episode" href=".+?">\n(.+?)\n</a>.+?<a class="episode-name" href=".+?">\n(.+?)</a>' , re . DOTALL ) . findall ( o00OO00OoO )
 for OOoOoOo , oOo0Oo0O0O , III1II1i , I1i1i1iii in iiIii :
  iI1i1IiIIIIi = ( III1II1i ) . replace ( 'Sezon' , '' ) . replace ( 'bölüm' , '' ) . replace ( 'Bölüm' , '' ) . replace ( 'BÃ¶lÃ¼m' , '' ) . replace ( '.' , '' )
  OooOooO0O0o0 = ( oOo0Oo0O0O ) . replace ( 'bölüm' , '' ) . replace ( 'Sezon' , '' ) . replace ( 'Bölüm' , '' ) . replace ( 'BÃ¶lÃ¼m' , '' ) . replace ( '.' , '' )
  OOO0o0 = 'Season ' + OooOooO0O0o0 + 'Episode ' + iI1i1IiIIIIi + I1i1i1iii
  IIIIII111Ii ( OOO0o0 , OOoOoOo )
  if 5 - 5: ooOoO0O00 + o0o00Oo0O % o0o00Oo0O * o0o00Oo0O + OOooOOo % ooOoO0O00
  xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 80 - 80: o0oOO0O00o0O / I11i + oO0o / OoOo00o
  if 46 - 46: Ii / OooO0OoOOOO % ooOoO0O00 - iI1iI1I1i1I * OOooOOo
def IIIIII111Ii ( name , url ) :
 OOoOoOo = url
 O0OOOOOoo = name
 OOOO0OOoO0O0 = cloudflare . source ( OOoOoOo )
 ooo0O = re . compile ( 'file: "(.+?)",.+?label: "(.+?)",' , re . DOTALL ) . findall ( OOOO0OOoO0O0 )
 for oOOOo00O00O , oo0ooO0 in ooo0O :
  i1II1IiIII111 ( '[COLORgreen]' + O0OOOOOoo + oo0ooO0 + '[/COLOR]' , oOOOo00O00O , 10012 , ooOooo000oOO + 'dtv.png' )
  if 65 - 65: oO0o - iI11I1II1I1I
 xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 20 - 20: OOooOOo % Ii1I
 if 44 - 44: ii . IIiIiII11i . IIIii1II1II % ii
def Oo0oO00 ( ) :
 if 41 - 41: o0o00Oo0O - iI1iI1I1i1I * iI11I1II1I1I
 if 12 - 12: I11i * IIIi % IIiIiII11i * ooOoO0O00 * iI11I1II1I1I
 if 81 - 81: I1ii11iIi11i - iI1iI1I1i1I
 if 24 - 24: ii . oO0o * IIiIiII11i
 if 59 - 59: IIIi + oO0o / IIIii1II1II
 if 97 - 97: I1ii11iIi11i * o0oOO0O00o0O % O0OoO . o0oOO0O00o0O - IIIi - IIIii1II1II
 if 79 - 79: oOo0O0Ooo - O0OoO
 if 37 - 37: OooO0OoOOOO . I1ii11iIi11i * I1ii11iIi11i * IIiIiII11i * o0o00Oo0O
 if 83 - 83: OooO0OoOOOO / IIIi
 if 64 - 64: oO0o % OooO0OoOOOO . IIIi % oO0o + iI1iI1I1i1I * OooO0OoOOOO
 if 83 - 83: I11i % OoOo00o + iI1iI1I1i1I % Ii + o0o00Oo0O
 if 65 - 65: iI11I1II1I1I % OoOo00o + o0o00Oo0O / ii
 if 52 - 52: Ii11Ii1I % IIIii1II1II * oOo0O0Ooo % iI1iI1I1i1I + IIIii1II1II / o0oOO0O00o0O
 if 80 - 80: ii + OooO0OoOOOO
 if 95 - 95: IIIi / OoOo00o * IIIi - ii * ii % oO0o
 IIII ( '[COLORgreen]Newest Episodes Added[/COLOR]' , 'http://www.watchseries.li/latest' , 10046 , ooOooo000oOO + 'WATCHSERIES.png' , '' , '' )
 IIII ( '[COLORgreen]This Week\'s Popular Episodes[/COLOR]' , 'http://www.watchseries.li/new' , 10042 , ooOooo000oOO + 'WATCHSERIES.png' , '' , '' )
 IIII ( '[COLORgreen]Search Program[/COLOR]' , '' , 10043 , ooOooo000oOO + 'WATCHSERIES.png' , '' , '' )
 if 43 - 43: I1ii11iIi11i . IIIi
 if 12 - 12: IIIi + IIIii1II1II + iI1iI1I1i1I . OooO0OoOOOO / Ii11Ii1I
def i1IoOOoooO0O0 ( url ) :
 o00OO00OoO = oO0OOoo0OO ( url )
 I11iI1i1I11I11 = re . compile ( '<ul class="pagination" style="line-height: 3;">(.+?)</ul>' , re . DOTALL ) . findall ( o00OO00OoO )
 iiIii = re . compile ( '<li><a href="/letters/(.+?)">(.+?)</a></li>' ) . findall ( str ( I11iI1i1I11I11 ) )
 for url , I1i1i1iii in iiIii :
  IIII ( '[COLORgreen]' + I1i1i1iii + '[/COLOR]' , 'http://watchseries.li/letters/' + url , 10049 , ooOooo000oOO + 'WATCHSERIES.png' , '' , '' )
  if 46 - 46: iI11I1II1I1I
def I111iiiii1 ( url ) :
 o00OO00OoO = oO0OOoo0OO ( url )
 iiIii = re . compile ( '<a href="(.+?)" class="sr-header">(.+?)</a>' ) . findall ( o00OO00OoO )
 for url , I1i1i1iii in iiIii :
  IIII ( '[COLORgreen]' + I1i1i1iii + '[/COLOR]' , 'http://watchseries.li/' + url , 10049 , ooOooo000oOO + 'WATCHSERIES.png' , '' , '' )
  if 100 - 100: Ii1I * Ii % OoOo00o / I1ii11iIi11i / O0OoO + Ii1I
def o00ooOoo ( url ) :
 o00OO00OoO = oO0OOoo0OO ( url )
 iiIii = re . compile ( '<li class="col-md-6 col-xs-12 list-movies-li"><a href="(.+?)" title=".+?">(.+?)<span class="epnum">.+?</span></a></li>' , re . DOTALL ) . findall ( o00OO00OoO )
 ooo0O = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="(.+?)">Next</a></li></ul>' , re . DOTALL ) . findall ( o00OO00OoO )
 for url , I1i1i1iii in iiIii :
  IIII ( '[COLORgreen]' + ( I1i1i1iii ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' ) + '[/COLOR]' , 'http://www.watchseries.li' + url , 10044 , ooOooo000oOO + 'WATCHSERIES.png' , '' , '' )
 for url in ooo0O :
  IIII ( '[COLORgreen]' + 'NEXT' + '[/COLOR]' , 'http://www.watchseries.li' + url , 10049 , ooOooo000oOO + 'Next.png' , '' , '' )
  if 5 - 5: OooO0OoOOOO
  if 84 - 84: IIiIiII11i * OoOo00o * IIiIiII11i % OooO0OoOOOO / oOo0O0Ooo
def O0Oooo ( ) :
 iiIiIIIiiI = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 I11iI1I = 'http://www.watchseries.li/search/' + iiIiIIIiiI . replace ( ' ' , '%20' )
 o00OO00OoO = oO0OOoo0OO ( I11iI1I )
 iiIii = re . compile ( '<img src="(.+?)".+?<a href="(.+?)" title=".+?"><b>(.+?)</b>' , re . DOTALL ) . findall ( o00OO00OoO )
 for I1i11 , OooOoOo , I1i1i1iii in iiIii :
  if 'watch online' in I1i1i1iii :
   pass
  else :
   print OooOoOo
   IIII ( '[COLORgreen]' + I1i1i1iii + '[/COLOR]' , 'http://www.watchseries.li' + OooOoOo , 10044 , I1i11 , '' , '' )
   if 50 - 50: iI11I1II1I1I * OooO0OoOOOO . ii / IIiIiII11i - Ii1I * Ii1I
   xbmcplugin . setContent ( O0O , 'movies' )
   if 98 - 98: oO0o - Ii11Ii1I . OooO0OoOOOO % Ii
def OO00oo ( url ) :
 o00OO00OoO = oO0OOoo0OO ( url )
 iiIii = re . compile ( '<img src="(.+?)".+?<div class="block-left-home-inside-text">.+?<a href="(.+?)" title=".+?"><b>(.+?)</b> <br>.+?<span class=".+?">(.+?)</span></a><br>(.+?)<br>' , re . DOTALL ) . findall ( o00OO00OoO )
 for I1i11 , url , I1i1i1iii , III1II1i , iIII in iiIii :
  O0Oo0O0 = ( I1i1i1iii ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' ) + ' - ' + ( III1II1i ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' )
  IIII ( '[COLORgreen]' + O0Oo0O0 + '[/COLOR]' , 'http://www.watchseries.li' + url , 10045 , I1i11 , '' , iIII )
  if 33 - 33: O0OoO % ooOoO0O00 - OoOo00o . o0o00Oo0O / o0o00Oo0O
def oo00o0 ( url ) :
 o00OO00OoO = oO0OOoo0OO ( url )
 iiIii = re . compile ( '<li class="col-md-6 col-xs-12 list-movies-li"><a href="(.+?)" title=".+?">(.+?)<span class="epnum">.+?</span></a></li>' , re . DOTALL ) . findall ( o00OO00OoO )
 ooo0O = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="(.+?)">Next</a></li></ul>' , re . DOTALL ) . findall ( o00OO00OoO )
 for url , I1i1i1iii in iiIii :
  O0Oo0O0 = ( I1i1i1iii ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' )
  IIII ( '[COLORgreen]' + O0Oo0O0 + '[/COLOR]' , 'http://www.watchseries.li' + url , 10045 , ooOooo000oOO + 'WATCHSERIES.png' , '' , '' )
 for url in ooo0O :
  IIII ( '[COLORgreen]' + 'NEXT' + '[/COLOR]' , 'http://www.watchseries.li' + url , 10046 , ooOooo000oOO + 'Next.png' , '' , '' )
  if 17 - 17: Ii11Ii1I / iI11I1II1I1I - oO0o + oOo0O0Ooo % IIIii1II1II
def III1III11II ( url ) :
 o00OO00OoO = oO0OOoo0OO ( url )
 iiIii = re . compile ( '<div class="mask">.+?<a href="(.+?)" title="(.+?)">.+?<img src="(.+?)"' , re . DOTALL ) . findall ( o00OO00OoO )
 ooo0O = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="(.+?)">Next</a></li></ul>' , re . DOTALL ) . findall ( o00OO00OoO )
 for url , I1i1i1iii , I1i11 in iiIii :
  IIII ( '[COLORgreen]' + ( I1i1i1iii ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' ) + '[/COLOR]' , 'http://www.watchseries.li' + url , 10044 , I1i11 , '' , '' )
 for url in ooo0O :
  IIII ( '[COLORgreen]' + 'NEXT' + '[/COLOR]' , 'http://www.watchseries.li' + url , 10041 , ooOooo000oOO + 'Next.png' , '' , '' )
  if 43 - 43: oOo0O0Ooo
def iiIIIiI1Ii ( url ) :
 o00OO00OoO = oO0OOoo0OO ( url )
 I11iI1i1I11I11 = re . compile ( '<div class="col-md-6 col-xs-12".+?<a href=".+?" itemprop="url"><span itemprop="name">(.+?)</span>(.+?)</ul>' , re . DOTALL ) . findall ( o00OO00OoO )
 for oOo0Oo0O0O , OO000o in I11iI1i1I11I11 :
  iiIii = re . compile ( '<li itemprop="episode".+?<meta itemprop="url" content="(.+?)">.+?<span class="" itemprop="name">\n(.+?)\n' , re . DOTALL ) . findall ( str ( OO000o ) )
  for url , I1i1i1iii in iiIii :
   O0Oo0O0 = ( oOo0Oo0O0O ) . replace ( '  ' , '' ) + ' ' + ( I1i1i1iii ) . replace ( '&nbsp;' , ' ' ) . replace ( '&#039;' , '\'' ) . replace ( '  ' , '' )
   IIII ( '[COLORgreen]' + O0Oo0O0 + '[/COLOR]' , 'http://www.watchseries.li' + url , 10045 , ooOooo000oOO + 'WATCHSERIES.png' , '' , '' )
 ooo0O = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="(.+?)">Next</a></li></ul>' , re . DOTALL ) . findall ( o00OO00OoO )
 for url in ooo0O :
  IIII ( '[COLORgreen]' + 'NEXT' + '[/COLOR]' , 'http://www.watchseries.li' + url , 10044 , ooOooo000oOO + 'Next.png' , '' , '' )
  if 13 - 13: I11i * Ii / Ii . oO0o . IIIii1II1II . Ii1I
  if 26 - 26: I11i . iI11I1II1I1I
class oOo0 ( ) :
 if 30 - 30: IIIii1II1II + IIiIiII11i - OooO0OoOOOO * ii
 List = [ ]
 source_list = [ ]
 def __init__ ( self , name ) :
  if 19 - 19: OooO0OoOOOO - I11i . iI11I1II1I1I . OOooOOo / IIIii1II1II
  O0Oo0O0 = name
  self . Get_Sources ( OooOoOo , O0Oo0O0 )
  if 87 - 87: OOooOOo - O0OoO - IIIii1II1II + I1ii11iIi11i % iI11I1II1I1I / Ii
  if 12 - 12: O0OoO
 def Get_Sources ( self , URL , season_name ) :
  Oo0oO0ooo = xbmcgui . DialogProgress ( )
  o00OO00OoO = oO0OOoo0OO ( URL )
  iiIii = re . compile ( '<td>.+?<a href="/link/(.+?)".+?height="16px">(.+?)\n' , re . DOTALL ) . findall ( o00OO00OoO )
  for OooOoOo , I1i1i1iii in iiIii :
   URL = 'http://www.watchseries.li/link/' + OooOoOo
   self . Get_site_link ( URL , season_name )
   if 86 - 86: OoOo00o - oO0o
 def Get_site_link ( self , url , season_name ) :
  o00OO00OoO = oO0OOoo0OO ( url )
  iiIii = re . compile ( '<iframe style=.+?" src="(.+?)"' ) . findall ( o00OO00OoO )
  ooo0O = re . compile ( '<IFRAME SRC="(.+?)"' ) . findall ( o00OO00OoO )
  i111iiIIII = re . compile ( '<IFRAME style=".+?" SRC="(.+?)"' ) . findall ( o00OO00OoO )
  for url in iiIii :
   self . main ( url , season_name )
  for url in ooo0O :
   self . main ( url , season_name )
  for url in i111iiIIII :
   self . main ( url , season_name )
   if 63 - 63: oOo0O0Ooo / OOooOOo + ii . iI1iI1I1i1I . O0OoO
 def main ( self , url , season_name ) :
  Oo0oO0ooo . create ( "[COLORwhite]Origin[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
  if 'daclips.in' in url :
   IiI1iiI11 = 'DACLIPS'
   if IiI1iiI11 in oOo0 . source_list :
    pass
   else :
    self . daclips ( url , season_name , IiI1iiI11 )
    Oo0oO0ooo . update ( 0 , "" , "Getting Daclips Links" )
  else :
   if 'filehoot.com' in url :
    IiI1iiI11 = 'FILEHOOT'
    if IiI1iiI11 in oOo0 . source_list :
     pass
    else :
     Oo0oO0ooo . update ( 0 , "" , "Getting Filehoot Links" )
     self . filehoot ( url , season_name , IiI1iiI11 )
   else :
    if 'thevideo.me' in url :
     IiI1iiI11 = 'THEVIDEO'
     if IiI1iiI11 in oOo0 . source_list :
      pass
     else :
      self . thevideo ( url , season_name , IiI1iiI11 )
      Oo0oO0ooo . update ( 0 , "" , "Getting Thevideo Links" )
    else :
     if 'allmyvideos.net' in url :
      IiI1iiI11 = 'ALLMYVIDEOS'
      if IiI1iiI11 in oOo0 . source_list :
       pass
      else :
       self . allmyvid ( url , season_name , IiI1iiI11 )
       Oo0oO0ooo . update ( 0 , "" , "Getting Allmyvideo Links" )
     else :
      if 'vidspot.net' in url :
       IiI1iiI11 = 'VIDSPOT'
       if IiI1iiI11 in oOo0 . source_list :
        pass
       else :
        self . vidspot ( url , season_name , IiI1iiI11 )
        Oo0oO0ooo . update ( 0 , "" , "Getting Vidspot Links" )
      else :
       if 'vodlocker' in url :
        IiI1iiI11 = 'VODLOCKER'
        if IiI1iiI11 in oOo0 . source_list :
         pass
        else :
         self . vodlocker ( url , season_name , IiI1iiI11 )
         Oo0oO0ooo . update ( 0 , "" , "Getting Vodlocker Links" )
         if 85 - 85: Ii1I - OOooOOo / Ii1I + IIIii1II1II - o0oOO0O00o0O
         if 49 - 49: oO0o - o0o00Oo0O / oO0o * OOooOOo + IIIi
 def allmyvid ( self , url , season_name , source_name ) :
  o00OO00OoO = oO0OOoo0OO ( url )
  iiIii = re . compile ( '"file" : "(.+?)",\n.+?"default" : .+?,\n.+?"label" : "(.+?)"' , re . DOTALL ) . findall ( o00OO00OoO )
  for Iiii1I , I1i1i1iii in iiIii :
   self . Printer ( Iiii1I , season_name , source_name )
   if 61 - 61: iI11I1II1I1I - iI1iI1I1i1I / o0oOO0O00o0O * iI1iI1I1i1I % Ii11Ii1I % o0oOO0O00o0O
 def vidspot ( self , url , season_name , source_name ) :
  o00OO00OoO = oO0OOoo0OO ( url )
  iiIii = re . compile ( '"file" : "(.+?)",\n.+?"default" : .+?,\n.+?"label" : "(.+?)"' ) . findall ( o00OO00OoO )
  for Iiii1I , I1i1i1iii in iiIii :
   self . Printer ( Iiii1I , season_name , source_name )
   if 63 - 63: IIIii1II1II % iI11I1II1I1I
 def thevideo ( self , url , season_name , source_name ) :
  o00OO00OoO = oO0OOoo0OO ( url )
  iiIii = re . compile ( "{ label: '.+?', file: '(.+?)' }" ) . findall ( o00OO00OoO )
  for Iiii1I in iiIii :
   self . Printer ( Iiii1I , season_name , source_name )
   if 20 - 20: oO0o . oOo0O0Ooo * Ii / Ii
 def vodlocker ( self , url , season_name , source_name ) :
  o00OO00OoO = oO0OOoo0OO ( url )
  iiIii = re . compile ( 'file: "(.+?)",.+?skin' , re . DOTALL ) . findall ( o00OO00OoO )
  for Iiii1I in iiIii :
   self . Printer ( Iiii1I , season_name , source_name )
   if 89 - 89: o0oOO0O00o0O . Ii * o0o00Oo0O
 def daclips ( self , url , season_name , source_name ) :
  o00OO00OoO = oO0OOoo0OO ( url )
  iiIii = re . compile ( '{ file: "(.+?)", type:"video" }' ) . findall ( o00OO00OoO )
  for Iiii1I in iiIii :
   self . Printer ( Iiii1I , season_name , source_name )
   if 44 - 44: ooOoO0O00 . oOo0O0Ooo / Ii + OooO0OoOOOO
 def filehoot ( self , url , season_name , source_name ) :
  o00OO00OoO = oO0OOoo0OO ( url )
  iiIii = re . compile ( 'file: "(.+?)",.+?skin' , re . DOTALL ) . findall ( o00OO00OoO )
  for Iiii1I in iiIii :
   self . Printer ( Iiii1I , season_name , source_name )
   if 27 - 27: IIIii1II1II
 def Printer ( self , Link , season_name , source_name ) :
  if 52 - 52: IIIi % OOooOOo + iI11I1II1I1I * OoOo00o . Ii11Ii1I
  if Link in oOo0 . List :
   pass
  elif source_name in oOo0 . source_list :
   pass
  else :
   i1II1IiIII111 ( '[COLORgreen]' + source_name + '[/COLOR]' , Link , 10012 , ooOooo000oOO + 'WATCHSERIES.png' )
   Oo0oO0ooo . update ( 100 , "" , "Got Source" )
   oOo0 . List . append ( Link )
   oOo0 . source_list . append ( source_name )
   if 95 - 95: iI11I1II1I1I . OooO0OoOOOO - ii * oO0o / I11i
   xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
   if 74 - 74: OoOo00o
   if 34 - 34: o0oOO0O00o0O
   if 44 - 44: ooOoO0O00 % oOo0O0Ooo % I11i
   if 9 - 9: I1ii11iIi11i % ii - Ii11Ii1I
   if 43 - 43: oO0o % oO0o
def IIiii11ii1i ( ) :
 IIII ( '[COLORgreen]Highlights[/COLOR]' , '' , 10008 , ooOooo000oOO + 'ORIGINFOOTBALL.png' , i1iiIII111ii , '' )
 IIII ( '[COLORgreen]Fixtures[/COLOR]' , '' , 10009 , ooOooo000oOO + 'ORIGINFOOTBALL.png' , i1iiIII111ii , '' )
 if 7 - 7: OoOo00o - o0o00Oo0O * iI1iI1I1i1I - I11i - IIiIiII11i
def Ii11iiI1 ( ) :
 I1i11i = oO0OOoo0OO ( i1111 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20vcXVpY2tpbmRleC5odG1s' ) )
 iiIii = re . compile ( '<a target="_self" href="(.+?)".+?src="(.+?)" alt="(.+?)"' , re . DOTALL ) . findall ( I1i11i )
 for OooOoOo , I1i11 , I1i1i1iii in iiIii :
  IIII ( '[COLORgreen]' + ( I1i1i1iii ) . replace ( 'amp;' , '' ) + '[/COLOR]' , i1111 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20v' ) + OooOoOo , 10010 , i1111 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20v' ) + I1i11 , i1iiIII111ii , '' )
  if 71 - 71: I11i / IIIii1II1II % IIIii1II1II
def OoooO0 ( url ) :
 o00OO00OoO = oO0OOoo0OO ( url )
 I11iI1i1I11I11 = re . compile ( 'AndClearL.+?><h2.+?head>(.*?)float' , re . DOTALL ) . findall ( o00OO00OoO )
 for I11iI1i1I11I11 in I11iI1i1I11I11 :
  oooOO0oo0Oo00 = re . compile ( '(.*?)</h2>' ) . findall ( str ( I11iI1i1I11I11 ) )
  for oOoO in oooOO0oo0Oo00 :
   oOoO = oOoO
  iI111I1III = re . compile ( 'comp_head>(.*?)</span>.*?<div class = fLeft width = ".*?"><img src="(.*?)">.*?</div>.*?ST:(.*?)</div>(.+?)<!-- around all of channel types ENDS 2-->' , re . DOTALL ) . findall ( str ( I11iI1i1I11I11 ) )
  for i111IiiI1Ii , I1i11 , time , OooOOOOOo in iI111I1III :
   i1Iii11I1i = re . compile ( ",CAPTION, '(.+?)&nbsp" ) . findall ( OooOOOOOo )
   IIII ( '[COLORgreen]' + oOoO + ' - ' + i111IiiI1Ii + ' - ' + time + '[/COLOR]' , '' , 10010 , i1111 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20=' ) + I1i11 , i1iiIII111ii , ( str ( i1Iii11I1i ) ) )
   if 50 - 50: IIIi + O0OoO + o0oOO0O00o0O
 o00oooO0Oo ( 'tvshows' , 'Media Info 3' )
 if 15 - 15: iI1iI1I1i1I
def IiiI11I1IIiI ( ) :
 if 5 - 5: I1ii11iIi11i
 IIII ( '[COLORgreen]Shows[/COLOR]' , 'http://www.fullmatchesandshows.com/category/show/' , 10011 , 'http://www.fm-base.co.uk/forum/attachments/club-competition-logos/3885-soccer-am-logo-socceram.png' , ooOooo000oOO + 'fanart.jpg' , '' )
 IIII ( '[COLORgreen]Premier League[/COLOR]' , 'http://www.fullmatchesandshows.com/premier-league/' , 10011 , 'https://footballseasons.files.wordpress.com/2013/05/premier-league.png' , ooOooo000oOO + 'fanart.jpg' , '' )
 IIII ( '[COLORgreen]La Liga[/COLOR]' , 'http://www.fullmatchesandshows.com/la-liga/' , 10011 , 'http://1.bp.blogspot.com/-c6kQ40ryhyo/U19cUlz25sI/AAAAAAAABak/qtn5chSFZm0/s1600/la-liga-logo_display_image.png' , ooOooo000oOO + 'fanart.jpg' , '' )
 IIII ( '[COLORgreen]Bundesliga[/COLOR]' , 'http://www.fullmatchesandshows.com/bundesliga/' , 10011 , 'http://m.img.brothersoft.com/iphone/189/518670189_icon175x175.jpg' , ooOooo000oOO + 'fanart.jpg' , '' )
 IIII ( '[COLORgreen]Champions League[/COLOR]' , 'http://www.fullmatchesandshows.com/champions-league/' , 10011 , 'http://www.ecursuri.ro/images/teste/test-champions-league.jpg' , ooOooo000oOO + 'fanart.jpg' , '' )
 IIII ( '[COLORgreen]Serie A[/COLOR]' , 'http://www.fullmatchesandshows.com/category/serie-a/' , 10011 , 'http://files.jcriccione.it/200000223-2484526782/serie%20a.png' , ooOooo000oOO + 'fanart.jpg' , '' )
 IIII ( '[COLORgreen]Ligue 1[/COLOR]' , 'http://www.fullmatchesandshows.com/category/ligue-1/' , 10011 , 'http://a1.mzstatic.com/us/r30/Purple5/v4/37/c7/44/37c744ae-5824-42b7-6ce0-5f471f52baab/icon180x180.jpeg' , ooOooo000oOO + 'fanart.jpg' , '' )
 IIII ( '[COLORgreen]Copa America 2015[/COLOR]' , 'http://www.fullmatchesandshows.com/copa-america-2015/' , 10011 , 'https://pbs.twimg.com/profile_images/521966985907691520/Nq9OAPIo_400x400.png' , ooOooo000oOO + 'fanart.jpg' , '' )
 IIII ( '[COLORgreen]CONCACAF[/COLOR]' , 'http://www.fullmatchesandshows.com/category/concacaf/' , 10011 , 'http://a3.mzstatic.com/us/r30/Purple3/v4/40/26/14/4026147c-7022-4ca3-504e-e78950cc3f1c/icon175x175.png' , ooOooo000oOO + 'fanart.jpg' , '' )
 IIII ( '[COLORgreen]Women World Cup[/COLOR]' , 'http://www.fullmatchesandshows.com/category/women-world-cup/' , 10011 , 'https://upload.wikimedia.org/wikipedia/en/thumb/7/76/2015_FIFA_Women\'s_World_Cup_logo.svg/967px-2015_FIFA_Women\'s_World_Cup_logo.svg.png' , ooOooo000oOO + 'fanart.jpg' , '' )
 if 100 - 100: Ii11Ii1I + iI11I1II1I1I
def o0o0OoO0OOO0 ( url ) :
 o00OO00OoO = oO0OOoo0OO ( url )
 iiIii = re . compile ( 'itemprop="image" class="entry-thumb" src="(.+?)".+?<h3 itemprop="name" class="entry-title td-module-title"><a itemprop="url" href="(.+?)" rel="bookmark" title=".+?">(.+?)</a></h3>' , re . DOTALL ) . findall ( o00OO00OoO )
 for I1i11 , url , I1i1i1iii in iiIii :
  oO0OOOO0o0 = I1i1i1iii . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' )
  i1II1IiIII111 ( '[COLORgreen]' + oO0OOOO0o0 + '[/COLOR]' , url , 10013 , I1i11 )
  if 67 - 67: I1ii11iIi11i / O0OoO - OooO0OoOOOO
def O0O00OoOoOOo ( url ) :
 o00OO00OoO = oO0OOoo0OO ( url )
 iiIii = re . compile ( '<script data-config="(.+?)" data-height' ) . findall ( o00OO00OoO )
 for oOOOo00O00O in iiIii :
  o0o0oo0 = ( oOOOo00O00O ) . replace ( '/v2' , '' ) . replace ( 'zeus.json' , 'video-sd.mp4?hosting_id=21772' ) . replace ( 'config.playwire.com' , 'cdn.video.playwire.com' )
  o0oOOo0O0O000 ( 'http:' + o0o0oo0 )
  if 25 - 25: oO0o * OoOo00o % Ii + Ii * oO0o
  if 42 - 42: IIiIiII11i / o0o00Oo0O . iI11I1II1I1I / o0o00Oo0O / oO0o / ii
def ooiiI1ii ( url ) :
 I1i11i = IiIi ( url )
 iiIii = re . compile ( '<a href="([^"]*)" title="([^"]*)"><img itemprop="image" content="([^"]*)"' , re . DOTALL ) . findall ( I1i11i )
 ooo0O = re . compile ( "<a rel='next' href=([^=]*)=" , re . DOTALL ) . findall ( I1i11i )
 for url , I1i1i1iii , I1i11 in iiIii :
  i1II1IiIII111 ( I1i1i1iii , url , 8046 , I1i11 )
 for url in ooo0O :
  O0II11i11II ( 'NEXT PAGE' , ( url ) . replace ( ' class' , '' ) , 8045 , ooOooo000oOO + 'Next.png' )
def O0OooOO ( url ) :
 I1i11i = IiIi ( url )
 iiIii = re . compile ( "__filename='([^']*)',.+?__fullimage='([^']*)',.+?__title='([^']*)'," , re . DOTALL ) . findall ( I1i11i )
 for url , I1i11 , I1i1i1iii in iiIii :
  o0oOOo0O0O000 ( 'http://bitcast-b.bitgravity.com/ndtvod/23372/ndtv/' + url )
  if 49 - 49: OooO0OoOOOO / O0OoO / IIIii1II1II
def IiIiIi1I11I ( url ) :
 I1i11i = IiIi ( url )
 iiIii = re . compile ( "src='http://www.youtube.com/embed/(.+?)?version=3&#038;rel=1&#038;fs=1&#038;autohide=2&#038;showsearch=0&#038;showinfo=1&#038;iv_load_policy=1&#038;wmode=transparent' frameborder='0' allowfullscreen='true'></iframe>" ) . findall ( I1i11i )
 for url in iiIii :
  yt . PlayVideo ( url )
  if 43 - 43: Ii + o0oOO0O00o0O + O0OoO / IIIi . Ii1I + o0oOO0O00o0O
def iIIi1IiIi ( ) :
 I1i11i = IiIi ( i1111 ( 'aHR0cDovL3RvcGRvY3VtZW50YXJ5ZmlsbXMuY29tLw==' ) )
 iiIii = re . compile ( '<a href="(.+?)" >(.+?)</a></li><li>' ) . findall ( I1i11i )
 for OooOoOo , I1i1i1iii in iiIii :
  O0II11i11II ( I1i1i1iii , OooOoOo , 8041 , ooOooo000oOO + 'documentary.png' )
def III1i ( url ) :
 I1i11i = IiIi ( url )
 iiIii = re . compile ( '<h2><a href="(.+?)" title="(.+?)">.+?</a></h2>.+?src="(.+?)"' , re . DOTALL ) . findall ( I1i11i )
 ooo0O = re . compile ( 'class="inactive">.+?</a><a href="(.+?)">Next</a></div>' , re . DOTALL ) . findall ( I1i11i )
 for url , I1i1i1iii , I1i11 in iiIii :
  O0II11i11II ( ( I1i1i1iii ) . replace ( '&#039;s' , '' ) , url , 8042 , I1i11 )
 for url in ooo0O :
  O0II11i11II ( 'NEXT PAGE' , url , 8041 , ooOooo000oOO + 'Next.png' )
  if 69 - 69: Ii11Ii1I / ooOoO0O00 + O0OoO
  if 35 - 35: Ii - OoOo00o % Ii
def II111I1Iii ( url ) :
 I1i11i = IiIi ( url )
 iiIii = re . compile ( '<meta itemprop="name" content="(.+?)".+?<meta itemprop="thumbnailUrl" content="(.+?)".+?<meta itemprop="embedUrl" content="(.+?)".+?<meta itemprop="description" content="(.+?)" />' , re . DOTALL ) . findall ( I1i11i )
 ooo0O = re . compile ( '<div class="video new-video"><iframe width="766" height="431" src="(.+?)&iv_load_policy=3&showinfo=0&autohide=1"' , re . DOTALL ) . findall ( I1i11i )
 for I1i1i1iii , I1i11 , url , o0oo0O in iiIii :
  i1II1IiIII111 ( ( I1i1i1iii ) . replace ( '&#039;s' , '' ) , url . replace ( 'https://www.youtube.com/embed/' , '' ) , 8043 , I1i11 )
 for url in ooo0O :
  OO00Oo00oO ( ( url ) . replace ( '//' , 'http://' ) )
  if 94 - 94: Ii / IIIi / I1ii11iIi11i
def OO00Oo00oO ( url ) :
 I1i11i = IiIi ( url )
 iiIii = re . compile ( '<link rel="canonical" href="(.+?)">  <link rel="stylesheet"' ) . findall ( I1i11i )
 for url in iiIii :
  i1II1IiIII111 ( 'PLAY' , ( url ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , ooOooo000oOO + 'documentary.png' )
  if 9 - 9: iI1iI1I1i1I / OOooOOo / IIiIiII11i + IIIi
def o0O0oOO0Oooo ( ) :
 o00OO00OoO = IiIi ( 'http://www.stream2watch.co/live-tv' )
 iiIii = re . compile ( '<a href="(.+?)">.+?<img src="(.+?)" alt=".+?"/>.+?<span class="country_name">(.+?)<br />(.+?)</span>' , re . DOTALL ) . findall ( o00OO00OoO )
 for OooOoOo , I1i11 , I1i1i1iii , II1iOOoOO0O0o0 in iiIii :
  O0II11i11II ( ( I1i1i1iii + '[COLORgreen]' + II1iOOoOO0O0o0 + '[/COLOR]' ) , OooOoOo , 8086 , I1i11 )
  if 44 - 44: IIIii1II1II / I1ii11iIi11i + OooO0OoOOOO % IIiIiII11i / oO0o + Ii
def ii11Iiii ( url ) :
 o00OO00OoO = IiIi ( url )
 iiIii = re . compile ( '<a class="front_channel_href" href="(.+?)" title=".+?">.+?<img class="front_channel_thumb" src="(.+?)" alt=".+?"/>.+?<span class="front_channel_name">(.+?)</span>' , re . DOTALL ) . findall ( o00OO00OoO )
 for url , I1i11 , I1i1i1iii in iiIii :
  O0II11i11II ( '[COLORgreen]' + I1i1i1iii + '[/COLOR]' , url , 8087 , I1i11 )
  if 32 - 32: OOooOOo . Ii1I % oOo0O0Ooo - IIiIiII11i
def iiI111 ( url ) :
 o00OO00OoO = oO0OOoo0OO ( url )
 iiIii = re . compile ( 'a id="code_.+?data-f-href="(.+?)" data-code-embed="">(.+?)</a>' , re . DOTALL ) . findall ( o00OO00OoO )
 for url , I1i1i1iii in iiIii :
  OOoooo0oo ( url , I1i1i1iii )
  if 92 - 92: OoOo00o / IIIii1II1II . Ii1I
def OOoooo0oo ( url , name ) :
 o00OO00OoO = oO0OOoo0OO ( url )
 iiIii = re . compile ( "playStream\('.+?', '(.+?)'\);" , re . DOTALL ) . findall ( o00OO00OoO )
 for url in iiIii :
  print url
  i1II1IiIII111 ( '[COLORgreen]' + name + '[/COLOR]' , url , 222 , '' )
  if 30 - 30: Ii11Ii1I . Ii1I / IIIii1II1II
def i1II11IiiiI ( ) :
 I1i11i = IiIi ( i1111 ( 'aHR0cDovL3d3dy5zb2xpZS5vcmcvYWxpYnJhcnkvaW5kZXguaHRtbA==' ) )
 iiIii = re . compile ( '<td align="center" valign="top">.+?<a href="(.+?)">.+?<img src="(.+?)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( I1i11i )
 for OooOoOo , I1i11 , I1i1i1iii in iiIii :
  O0II11i11II ( ( '[COLORgreen]' + I1i1i1iii + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + OooOoOo , 3002 , 'http://www.solie.org/alibrary/' + I1i11 )
def IIIiIi1iiI1 ( url ) :
 I1i11i = IiIi ( url )
 iiIii = re . compile ( '<td align="center" valign="top">.+?<a href="(.+?)">.+?<img src="(.+?)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( I1i11i )
 for url , I1i11 , I1i1i1iii in iiIii :
  O0II11i11II ( ( '[COLORgreen]' + I1i1i1iii + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3003 , 'http://www.solie.org/alibrary/' + I1i11 )
def o0ooOOoO0oO0 ( url ) :
 I1i11i = IiIi ( url )
 iiIii = re . compile ( '<br><a href="([^"]*)">(.+?)</a>' ) . findall ( I1i11i )
 oo00I1IiI1IIiI = re . compile ( 'href="([^"]*)">Season(.+?)</a>' ) . findall ( I1i11i )
 next = re . compile ( '<a href="([^"]*)">Episodes</a>' ) . findall ( I1i11i )
 ooo0O = re . compile ( '<td align="center" valign="top">.+?<a href="(.+?)">.+?<img src="(.+?)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( I1i11i )
 for url , I1i1i1iii in iiIii :
  i1II1IiIII111 ( ( '[COLORgreen]' + I1i1i1iii + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3004 , ooOooo000oOO + 'classicmovies.png' )
 for url , I1i1i1iii in oo00I1IiI1IIiI :
  O0II11i11II ( '[COLORgreen]Season- ' + I1i1i1iii + '[/COLOR]' , 'http://www.solie.org/alibrary/' + url , 3003 , ooOooo000oOO + 'classicmovies.png' )
 for url in next :
  O0II11i11II ( '[COLORgreen]NEXT[/COLOR]' , 'http://www.solie.org/alibrary/' + url , 3003 , ooOooo000oOO + 'Next.png' )
 for url , I1i11 , I1i1i1iii in ooo0O :
  O0II11i11II ( ( '[COLORgreen]' + I1i1i1iii + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3003 , 'http://www.solie.org/alibrary/' + I1i11 )
def oooo ( url ) :
 I1i11i = IiIi ( url )
 iiIii = re . compile ( '<iframe.+?src="([^"]*)"' ) . findall ( I1i11i )
 for url in iiIii :
  o0o0oo0Ooo ( url )
def o0o0oo0Ooo ( url ) :
 I1i11i = IiIi ( url )
 iiIii = re . compile ( '<meta property="og:video" content="([^"]*)"/>' ) . findall ( I1i11i )
 for url in iiIii :
  o0oOOo0O0O000 ( url )
  if 12 - 12: Ii1I / Ii11Ii1I
def ii11 ( ) :
 I1i11i = IiIi ( i1111 ( 'aHR0cDovL3JldHJvdmlzaW9uLnR2L2FsbC8=' ) )
 iiIii = re . compile ( '<a href="([^"]*)"><h2><font color=".+?"><h2>(.+?)</font></h2></a>' ) . findall ( I1i11i )
 for OooOoOo , I1i1i1iii in iiIii :
  i1II1IiIII111 ( ( '[COLORgreen]' + I1i1i1iii + '[/COLOR]' ) . replace ( '&#8211;' , ':' ) , OooOoOo , 8061 , ooOooo000oOO + 'classicmovies.png' )
def Ii11 ( url ) :
 I1i11i = IiIi ( url )
 iiIii = re . compile ( "v.src = '([^']*)';" ) . findall ( I1i11i )
 for url in iiIii :
  o0oOOo0O0O000 ( url )
  if 3 - 3: Ii11Ii1I + IIIi . ooOoO0O00 / IIIii1II1II % IIIi
def O0oo00oOOO0o ( ) :
 I1i11i = IiIi ( i1111 ( 'aHR0cDovL3JldHJvdmlzaW9uLnR2L2NsYXNzaWMtdHYv' ) )
 iiIii = re . compile ( '<a href="([^"]*)"><h2><font color=".+?"><h2>(.+?)</font></h2></a>' ) . findall ( I1i11i )
 for OooOoOo , I1i1i1iii in iiIii :
  i1II1IiIII111 ( ( '[COLORgreen]' + I1i1i1iii + '[/COLOR]' ) . replace ( '&#8211;' , ':' ) , OooOoOo , 8061 , ooOooo000oOO + 'classictv.png' )
def II1iI111iiIIiI1I ( url ) :
 I1i11i = IiIi ( url )
 iiIii = re . compile ( "v.src = '([^']*)';" ) . findall ( I1i11i )
 for url in iiIii :
  o0oOOo0O0O000 ( url )
  if 51 - 51: oOo0O0Ooo + IIIii1II1II + iI1iI1I1i1I
def i1Iiii ( ) :
 o00OO00OoO = oO0OOoo0OO ( i1111 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vbTN1c3RyZWFtcw==' ) )
 iiIii = re . compile ( '<li><a href="(.+?)"> (.+?).m3u</a></li>' ) . findall ( o00OO00OoO )
 for OooOoOo , I1i1i1iii in iiIii :
  O0II11i11II ( ( '[COLORgreen]' + I1i1i1iii + '[/COLOR]' ) . replace ( '-' , ' ' ) . replace ( '_' , ' ' ) , ( i1111 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vbTN1c3RyZWFtcy8=' ) ) + OooOoOo , 8071 , ooOooo000oOO + 'streams.png' )
def o0O0O ( url ) :
 o00OO00OoO = IiIi ( url )
 iiIii = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( o00OO00OoO )
 for I1i1i1iii , url in iiIii :
  i1II1IiIII111 ( ( '[COLORgreen]' + I1i1i1iii + '[/COLOR]' ) . replace ( '_' , ' ' ) , ( url ) . strip ( ) , 404 , ooOooo000oOO + 'streams.png' )
def oOO ( url ) :
 o00OO00OoO = IiIi ( url )
 iiIii = re . compile ( 'EXTINF:(.+?),(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( o00OO00OoO )
 for I1i11 , I1i1i1iii , url in iiIii :
  url = ( ( i1111 ( 'aHR0cDovL3BpZXN1c3R2Lm5ldDo4MDAwL2xpdmUv' ) ) + oO0o0o0ooO0oO + '/' + oo0o0O00 + url ) . strip ( )
  i1II1IiIII111 ( ( '[COLORgreen]' + I1i1i1iii + '[/COLOR]' ) . replace ( '_' , ' ' ) , url , 10012 , I1i11 )
  if 59 - 59: oO0o - oO0o + o0oOO0O00o0O
def iiII ( ) :
 IiIIi1I1I11Ii ( 'Best Videos' , 'http://www.xvideos.com/best' , 10105 , ooOooo000oOO + 'JIZBOX.png' , '' , '' )
 IiIIi1I1I11Ii ( 'Genres' , 'http://www.xvideos.com' , 10106 , ooOooo000oOO + 'JIZBOX.png' , '' , '' )
 IiIIi1I1I11Ii ( 'Recently Uploaded' , 'http://xvideos.com' , 10105 , ooOooo000oOO + 'JIZBOX.png' , '' , '' )
 IiIIi1I1I11Ii ( 'Tags' , 'http://www.xvideos.com/tags' , 10103 , ooOooo000oOO + 'JIZBOX.png' , '' , '' )
 IiIIi1I1I11Ii ( 'Search' , '' , 10107 , ooOooo000oOO + 'JIZBOX.png' , '' , '' , )
 if 9 - 9: OoOo00o - IIIi % o0o00Oo0O . ooOoO0O00 . oOo0O0Ooo / oOo0O0Ooo
def O0000Oo ( url ) :
 o00OO00OoO = oO0OOoo0OO ( url )
 OOOOOO = re . compile ( '<li><a class=".+?".+?href="(.+?)">Next</a></li>' ) . findall ( o00OO00OoO )
 for url in OOOOOO :
  IiIIi1I1I11Ii ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10103 , ooOooo000oOO + 'JIZBOX.png' , '' , '' )
 iiIii = re . compile ( '<li><a href="(.+?)"><b>(.+?)</b><span class="navbadge default"(.+?)</span>' ) . findall ( o00OO00OoO )
 for url , I1i1i1iii , oO00ooooO0o in iiIii :
  IiIIi1I1I11Ii ( I1i1i1iii + ' - No of Videos : ' + ( oO00ooooO0o ) . replace ( '>' , '' ) , 'http://www.xvideos.com' + url , 10105 , ooOooo000oOO + 'JIZBOX.png' , '' , '' )
  if 77 - 77: I1ii11iIi11i
def II111I1 ( url ) :
 o00OO00OoO = oO0OOoo0OO ( url )
 OOOOOO = re . compile ( 'href="([^"]*)">Next</a></li>' ) . findall ( o00OO00OoO )
 for url in OOOOOO :
  IiIIi1I1I11Ii ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10104 , ooOooo000oOO + 'Next.png' , '' , '' )
 iiIii = re . compile ( ':"([^"]*)".+?;</script></a></div></div><p class="profile-name"><a href="([^"]*)">(.+?)</a></p><p class="profile-counts">\n(.+?)\n' , re . DOTALL ) . findall ( o00OO00OoO )
 for I1i11 , url , I1i1i1iii , i1iIIIIi1i1 in iiIii :
  IiIIi1I1I11Ii ( I1i1i1iii + '--' + i1iIIIIi1i1 , 'http://www.xvideos.com' + url + '#_tabVideos,videos-best' , 10105 , ( I1i11 ) . replace ( 'http:\/\/' , 'http://' ) , '' , '' )
  if 84 - 84: IIIii1II1II + Ii11Ii1I + I11i
  if 33 - 33: Ii11Ii1I
def ooOOO00oOOooO ( url ) :
 o00OO00OoO = oO0OOoo0OO ( url )
 iiIii = re . compile ( '<div class="thumb-inside"><script>.+?<img src="(.+?)".+?<a href="(.+?)" title=".+?">(.+?)</a></p>.+?uration">(.+?)</span>.+?Porn quality:(.+?)</span>' , re . DOTALL ) . findall ( o00OO00OoO )
 for I1i11 , url , I1i1i1iii , III1I1Iii1iiI , IiI in iiIii :
  O0i1II1Iiii1I11 ( I1i1i1iii + ' - Porn Quality : ' + IiI + ' - ' + III1I1Iii1iiI , 'http://www.xvideos.com' + url , 10108 , I1i11 , I1i11 , IiI + ' - ' + III1I1Iii1iiI )
 Iii1iiI = re . compile ( '<li><a href="([^"]*)" class="no-page">Next</a></li></ul></div>' ) . findall ( o00OO00OoO )
 for url in Iii1iiI :
  IiIIi1I1I11Ii ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10105 , ooOooo000oOO + 'Next.png' , '' , '' )
  if 7 - 7: I11i
def IiiIIi ( url ) :
 o00OO00OoO = oO0OOoo0OO ( url )
 I11iI1i1I11I11 = re . compile ( '<div class="main-categories">(.+?)</div>' , re . DOTALL ) . findall ( o00OO00OoO )
 OOOOOO = re . compile ( '<li><a class=".+?".+?href="(.+?)">Next</a></li>' ) . findall ( o00OO00OoO )
 for url in OOOOOO :
  IiIIi1I1I11Ii ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10106 , ooOooo000oOO + 'Next.png' , '' , '' )
 iiIii = re . compile ( '<li><a href="(.+?)" class="btn btn-default">(.+?)</a>' ) . findall ( str ( I11iI1i1I11I11 ) )
 for url , I1i1i1iii in iiIii :
  IiIIi1I1I11Ii ( I1i1i1iii , 'http://www.xvideos.com' + url , 10105 , ooOooo000oOO + 'JIZBOX.png' , '' , '' )
  if 96 - 96: ooOoO0O00 . iI1iI1I1i1I + OoOo00o + Ii1I * IIIii1II1II - IIiIiII11i
  if 1 - 1: o0o00Oo0O
def I11II1i1 ( ) :
 iiIiIIIiiI = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 IiI1ii11I1 = ( iiIiIIIiiI ) . replace ( ' ' , '+' ) . replace ( '&' , '&' )
 II11IiIi11 = IiI1ii11I1 . lower ( )
 I1i1iI = 'http://www.xvideos.com/?k=' + II11IiIi11
 print I1i1iI + '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'
 o00OO00OoO = oO0OOoo0OO ( I1i1iI )
 iiIii = re . compile ( '<div class="thumb-inside"><script>.+?<img src="(.+?)".+?<a href="(.+?)" title=".+?">(.+?)</a></p>.+?uration">(.+?)</span>.+?Porn quality:(.+?)</span>' , re . DOTALL ) . findall ( o00OO00OoO )
 for I1i11 , OooOoOo , I1i1i1iii , III1I1Iii1iiI , IiI in iiIii :
  O0i1II1Iiii1I11 ( I1i1i1iii + ' - Porn Quality : ' + IiI + ' - ' + III1I1Iii1iiI , 'http://www.xvideos.com' + OooOoOo , 10108 , I1i11 , I1i11 , IiI + ' - ' + III1I1Iii1iiI )
 Iii1iiI = re . compile ( '<li><a href="([^"]*)" class="no-page">Next</a></li></ul></div>' ) . findall ( o00OO00OoO )
 for OooOoOo in Iii1iiI :
  IiIIi1I1I11Ii ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + OooOoOo , 10105 , ooOooo000oOO + 'Next.png' , '' , '' )
  if 30 - 30: iI1iI1I1i1I % OOooOOo / Ii1I * o0o00Oo0O * Ii11Ii1I . oOo0O0Ooo
def iIi11I11 ( url ) :
 o00OO00OoO = oO0OOoo0OO ( url )
 iiIii = re . compile ( 'flv_url=(.+?)\;' ) . findall ( o00OO00OoO )
 for url in iiIii :
  i1i = ( url ) . replace ( '%3A' , ':' ) . replace ( '%2F' , '/' ) . replace ( '%3F' , '?' ) . replace ( '%3D' , '=' ) . replace ( '%26' , '&' ) . replace ( '&amp' , '' )
  oOI11 ( i1i )
  if 18 - 18: iI11I1II1I1I
def oOI11 ( url ) :
 oO00oOOo0Oo = xbmc . Player ( Ii11iI ( ) )
 import urlresolver
 try : oO00oOOo0Oo . play ( url )
 except : pass
 if 22 - 22: IIIii1II1II
 if 22 - 22: o0oOO0O00o0O * iI1iI1I1i1I - I1ii11iIi11i * o0o00Oo0O / Ii
def OOooO0Oo0o000 ( ) :
 o00OO00OoO = oO0OOoo0OO ( i1111 ( 'aHR0cDovL3d3dy5nb2Zpc2hpbmcuY28udWsvQW5nbGluZy1UaW1lcy9TZWN0aW9uL1ZpZGVvcy8=' ) )
 iiIii = re . compile ( 'class="item.+?"><a href="(.+?)">(.+?)</a></li>' ) . findall ( o00OO00OoO )
 for OooOoOo , I1i1i1iii in iiIii :
  O0II11i11II ( '[COLORgreen]' + I1i1i1iii + '[/COLOR]' , ( 'http://www.gofishing.co.uk' + OooOoOo ) . replace ( 'http://www.gofishing.co.ukhttp://www.gofishing.co.uk' , 'http://www.gofishing.co.uk' ) , 8091 , ooOooo000oOO + 'gofish.png' )
def iiiIii ( url ) :
 o00OO00OoO = IiIi ( url )
 iiIii = re . compile ( '<h2><a id=.+?href="([^"]*)">(.+?)</a></h2>' , re . DOTALL ) . findall ( o00OO00OoO )
 ooo0O = re . compile ( '<h3><a href="([^"]*)" id=.+?>(.+?)</a> </h3>.+?<img src="([^"]*)"' , re . DOTALL ) . findall ( o00OO00OoO )
 next = re . compile ( 'href="([^"]*)">next</a>&gt;</li>' , re . DOTALL ) . findall ( o00OO00OoO )
 for url , I1i1i1iii in iiIii :
  i1II1IiIII111 ( '[COLORgreen]' + I1i1i1iii + '[/COLOR]' , 'http://www.gofishing.co.uk/' + url , 8092 , ooOooo000oOO + 'gofish.png' )
 for url , I1i1i1iii , I1i11 in ooo0O :
  i1II1IiIII111 ( '[COLORgreen]' + I1i1i1iii + '[/COLOR]' , 'http://www.gofishing.co.uk/' + url , 8092 , 'http://www.gofishing.co.uk/' + I1i11 )
 for url in next :
  O0II11i11II ( '[COLORgreen]NEXT[/COLOR]' , url . replace ( ' ' , '+' ) , 8091 , ooOooo000oOO + 'Next.png' )
def OoOiIIi1 ( url ) :
 o00OO00OoO = IiIi ( url )
 iiIii = re . compile ( 'src="https://www.youtube.com/embed/(.+?)"' ) . findall ( o00OO00OoO )
 for url in iiIii :
  yt . PlayVideo ( url )
  if 65 - 65: ooOoO0O00 . Ii1I / O0OoO
  if 11 - 11: OooO0OoOOOO * O0OoO / O0OoO - IIIii1II1II
  if 68 - 68: oOo0O0Ooo % OooO0OoOOOO - OooO0OoOOOO / oOo0O0Ooo + Ii1I - I1ii11iIi11i
o0oO0o00O = '{PQ},' ; iiii1 = '{SC},' ; OooO0O0Ooo = '{XG},' ; oO0O = '{JP},' ; IIIiIi1iiI = '{HW},' ; iI1o0 = '{RT},'
def IiiiI1i1I ( ) :
 Oo0oO0ooo = xbmcgui . DialogProgress ( )
 i1111iI1 = ( i1111 ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 iiIiIIIiiI = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 II11IiIi11 = iiIiIIIiiI . lower ( )
 OooOoOo = ( i1111 ( 'aHR0cDovL2RsNC5tb3ZpZWZhcnNpLmNvbS9maWxtLzIwMTUtNy8=' ) )
 OOoOoOo = ( i1111 ( 'aHR0cDovL2RsLmF2YWRsLmNvbS9OZXcvTW92aWUv' ) )
 iI1i11 = ( i1111 ( 'aHR0cDovLzIxNy4yMTkuMTQzLjEwOC8xMzI3Lw==' ) )
 if 76 - 76: ii - IIiIiII11i % OOooOOo + OoOo00o + iI11I1II1I1I . OOooOOo
 iIo00OOOOOo0OOo = ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvbW92L2FsbC5waHA=' ) )
 i1II11I11ii1 = ( i1111 ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 OOoO0oO00oOOO0OoO0oo0OO = ( i1111 ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL3NlYXJjaC8/cT0=' ) ) + iiIiIIIiiI
 i1iI1Ii11Ii1 = ( i1111 ( 'aHR0cDovL3JlZGVtcHRpb25idWlsZC4xNm1iLmNvbS9SZWRlbXB0aW9uL21vdmllcy9hbGxtb3ZpZS5waHA=' ) )
 o0OoO0oo0O0o = ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9UaGVfUmVhcGVyL2FsbG1vdmllcy5waHA=' ) )
 ii1III1iiIi = ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC9tb3ZmdWxsLnBocA==' ) )
 I1ii1iI = ( i1111 ( 'aHR0cDovLzUuMTM1LjIwNy45Ni9TY3JhcGVzL1NILnBocA==' ) )
 if 99 - 99: I11i
 Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Checking Sources" , '' , 'Please Wait' )
 o00OO00OoO = O000OO0 ( OooOoOo )
 Oo0oO0ooo . update ( 0 , "" , "Checking Source 1/9 Links" )
 OOOO0OOoO0O0 = O000OO0 ( OOoOoOo )
 Oo0oO0ooo . update ( 14 , "" , "Checking Source 2/9 Links" )
 O0Oo000ooO00 = O000OO0 ( iI1i11 )
 Oo0oO0ooo . update ( 28 , "" , "Checking Source 3/9 Links" )
 if 1 - 1: Ii11Ii1I * OOooOOo * oO0o + I1ii11iIi11i
 Oo0oO0ooo . update ( 40 , "" , "Checking Source 4/9 Links" )
 O0OOoOooO00 = O000OO0 ( iIo00OOOOOo0OOo )
 Oo0oO0ooo . update ( 52 , "" , "Checking Source 5/9 Links" )
 o0o00OOOO = O000OO0 ( OOoO0oO00oOOO0OoO0oo0OO )
 Oo0oO0ooo . update ( 64 , "" , "Checking Source 6/9 Links" )
 i11iIi1iIIIIi = O000OO0 ( i1iI1Ii11Ii1 )
 Oo0oO0ooo . update ( 76 , "" , "Checking Source 7/9 Links" )
 I1111iiiII1Ii = O000OO0 ( o0OoO0oo0O0o )
 Oo0oO0ooo . update ( 88 , "" , "Checking Source 8/9 Links" )
 oO0oOoOoo0 = O000OO0 ( ii1III1iiIi )
 Oo0oO0ooo . update ( 100 , "" , "Checking Source 9/9 Links" )
 o0o000o = O000OO0 ( I1ii1iI )
 if 26 - 26: iI11I1II1I1I * I11i . iI1iI1I1i1I
 if 10 - 10: IIIi * OoOo00o % I1ii11iIi11i - iI1iI1I1i1I % I1ii11iIi11i
 if o00OO00OoO != 'Failed' :
  iiIii = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( o00OO00OoO )
  for O0oooo000oO0 , I1i1i1iii in iiIii :
   if iiIiIIIiiI in I1i1i1iii . lower ( ) :
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    i1II1IiIII111 ( ( '[COLORgreen]' + I1i1i1iii + '- source 1[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( OooOoOo + O0oooo000oO0 ) , 222 , '' )
    Oo0oO0ooo . update ( 0 , "" , "Getting Source 1 Links" )
 if OOOO0OOoO0O0 != 'Failed' :
  ooo0O = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( OOOO0OOoO0O0 )
  for O0oooo000oO0 , I1i1i1iii in ooo0O :
   if iiIiIIIiiI in I1i1i1iii . lower ( ) :
    i1II1IiIII111 ( ( '[COLORgreen]' + I1i1i1iii + '- source 2[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( OOoOoOo + O0oooo000oO0 ) , 222 , '' )
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 9 , "" , "Getting Source 2 Links" )
 if O0Oo000ooO00 != 'Failed' :
  i111iiIIII = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( O0Oo000ooO00 )
  for O0oooo000oO0 , I1i1i1iii in i111iiIIII :
   if iiIiIIIiiI in I1i1i1iii . lower ( ) :
    O0II11i11II ( ( '[COLORgreen]' + I1i1i1iii + '- source 3[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( iI1i11 + O0oooo000oO0 ) , 1006 , '' )
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 18 , "" , "Getting Source 3 Links" )
    if 96 - 96: o0o00Oo0O . o0oOO0O00o0O - oOo0O0Ooo * I1ii11iIi11i
    if 68 - 68: OoOo00o - I1ii11iIi11i / OOooOOo - IIIi . o0oOO0O00o0O
    if 50 - 50: iI11I1II1I1I - o0oOO0O00o0O - iI1iI1I1i1I
    if 60 - 60: iI11I1II1I1I * O0OoO
    if 71 - 71: OOooOOo % I1ii11iIi11i % O0OoO
    if 34 - 34: iI1iI1I1i1I / iI1iI1I1i1I % OooO0OoOOOO . OOooOOo / I1ii11iIi11i
    if 99 - 99: O0OoO * oOo0O0Ooo - O0OoO % Ii11Ii1I
 if O0OOoOooO00 != 'Failed' :
  I1i1I = [ ]
  I111Iii1 = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( O0OOoOooO00 )
  for OooOoOo , OOOOO0O00 , iIII , I1Ii11II1I1 , I1i1i1iii in I111Iii1 :
   if iiIiIIIiiI in I1i1i1iii . lower ( ) :
    if I1i1i1iii in I1i1I :
     pass
    else :
     IIII ( ( '[COLORgreen]' + I1i1i1iii + '- source Scooby[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( 'Ganool' , '' ) . replace ( 'ShAaNiG' , '' ) . replace ( 'YIFY' , '' ) . replace ( '[[ Max-Movie.In ]]' , '' ) . replace ( '.mkv' , '' ) . replace ( '.mp4' , '' ) . replace ( '.' , ' ' ) , OooOoOo , 1016 , OOOOO0O00 , I1Ii11II1I1 , iIII )
     I1i1I . append ( I1i1i1iii )
     Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     Oo0oO0ooo . update ( 36 , "" , "Getting Scooby Links" )
     o00oooO0Oo ( 'tvshows' , 'Media Info 3' )
 if o0o00OOOO != 'Failed' :
  i11i = re . compile ( 'href="(.+?)".+?src="(.+?)" alt="Image of (.+?)"' , re . DOTALL ) . findall ( o0o00OOOO )
  for OooOoOo , I1i11 , I1i1i1iii in i11i :
   if iiIiIIIiiI in I1i1i1iii . lower ( ) :
    O0II11i11II ( ( '[COLORgreen]' + I1i1i1iii + '- source Snag[/COLOR]' ) . replace ( '&#x27;' , '' ) , 'http://www.snagfilms.com' + OooOoOo , 7067 , I1i11 )
    Oo0oO0ooo . update ( 45 , "" , "Getting Snag Links" )
    if 73 - 73: O0OoO % O0OoO . o0oOO0O00o0O + IIIi
    o00oooO0Oo ( 'tvshows' , 'Media Info 3' )
 if i11iIi1iIIIIi != 'Failed' :
  Ii1IOOooO00OO = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( i11iIi1iIIIIi )
  for OooOoOo , OOOOO0O00 , iIII , I1Ii11II1I1 , I1i1i1iii in Ii1IOOooO00OO :
   if iiIiIIIiiI in I1i1i1iii . lower ( ) :
    O0i1II1Iiii1I11 ( ( '[COLORgreen]' + I1i1i1iii + '- source Redemption[/COLOR]' ) , OooOoOo , 222 , OOOOO0O00 , I1Ii11II1I1 , iIII )
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 53 , "" , "Getting Redemption Links" )
    if 70 - 70: Ii11Ii1I - IIIii1II1II * IIIii1II1II / iI11I1II1I1I + o0o00Oo0O
    o00oooO0Oo ( 'tvshows' , 'Media Info 3' )
 if I1111iiiII1Ii != 'Failed' :
  IiIIi11i = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( I1111iiiII1Ii )
  for OooOoOo , OOOOO0O00 , iIII , I1Ii11II1I1 , I1i1i1iii in IiIIi11i :
   if iiIiIIIiiI in I1i1i1iii . lower ( ) :
    O0i1II1Iiii1I11 ( ( '[COLORgreen]' + I1i1i1iii + '- source Reaper[/COLOR]' ) , OooOoOo , 222 , OOOOO0O00 , I1Ii11II1I1 , iIII )
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 61 , "" , "Getting Reaper Links" )
    if 49 - 49: Ii1I + o0o00Oo0O . Ii11Ii1I * ii
    o00oooO0Oo ( 'tvshows' , 'Media Info 3' )
 if oO0oOoOoo0 != 'Failed' :
  oO0OOO00 = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( oO0oOoOoo0 )
  for OooOoOo , OOOOO0O00 , iIII , I1Ii11II1I1 , I1i1i1iii in oO0OOO00 :
   if iiIiIIIiiI in I1i1i1iii . lower ( ) :
    O0i1II1Iiii1I11 ( ( '[COLORgreen]' + I1i1i1iii + '- source Herovision[/COLOR]' ) , OooOoOo , 222 , OOOOO0O00 , I1Ii11II1I1 , iIII )
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 70 , "" , "Getting Herovision Links" )
    if 13 - 13: OooO0OoOOOO * Ii1I / Ii1I / iI11I1II1I1I % iI11I1II1I1I
    o00oooO0Oo ( 'tvshows' , 'Media Info 3' )
    if 21 - 21: Ii1I
 if o0o000o != 'Failed' :
  oOOOO0oo0O0OO = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( o0o000o )
  for OooOoOo , OOOOO0O00 , I1i1i1iii in oOOOO0oo0O0OO :
   if iiIiIIIiiI in I1i1i1iii . lower ( ) :
    O0II11i11II ( ( '[COLORgreen]' + I1i1i1iii + '- source Silent Hunter[/COLOR]' ) , OooOoOo , 222 , OOOOO0O00 )
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 78 , "" , "Getting Silent Hunter Links" )
    if 58 - 58: O0OoO - I11i + o0o00Oo0O / ooOoO0O00 % ii
    o00oooO0Oo ( 'tvshows' , 'Media Info 3' )
 O0Oo = [ '480p' , '720p' , '1080p' , 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' , '720paction' , '720padventure' , '720panimation' , '720pcomedy' , '720pcrime' , '720pdocumentary' , '720pdrama' , '720pfamily' , '720pfantasy' , '720phorror' , '720pmystery' , '720promance' , '720psci-Fi' , '720psport' , '720pthriller' , '720pwestern' , '1080paction' , '1080padventure' , '1080panimation' , '1080pcomedy' , '1080pcrime' , '1080pdocumentary' , '1080pdrama' , '1080pfamily' , '1080pfantasy' , '1080phorror' , '1080pmystery' , '1080promance' , '1080psci-Fi' , '1080psport' , '1080pthriller' , '1080pwestern' ]
 if 30 - 30: OoOo00o * I1ii11iIi11i / OoOo00o . IIiIiII11i . I1ii11iIi11i
 for O00 in filenames_pand_movie :
  i1iiIII1IIiIIII = IIIII + O00 + ooOoOoo0O
  ooIi111iII = oO0OOoo0OO ( i1iiIII1IIiIIII )
  if ooIi111iII != 'Failed' :
   Oo0OoOo = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( ooIi111iII )
   for OooOoOo , OOOOO0O00 , iIII , I1Ii11II1I1 , I1i1i1iii in Oo0OoOo :
    if iiIiIIIiiI in I1i1i1iii . lower ( ) :
     O0i1II1Iiii1I11 ( '[COLORgreen]' + I1i1i1iii + ' - Source Pandoras[/COLOR]' , OooOoOo , 222 , OOOOO0O00 , I1Ii11II1I1 , iIII )
     Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     Oo0oO0ooo . update ( 89 , "" , "Getting Pandoras Links" )
     if 13 - 13: I11i
     o00oooO0Oo ( 'tvshows' , 'Media Info 3' )
     if 7 - 7: oOo0O0Ooo + OooO0OoOOOO / Ii / I1ii11iIi11i
 O0Oo = [ '0-9/' , 'A/' , 'B/' , 'C/' , 'D/' , 'E/' , 'F/' , 'G/' , 'H/' , 'I/' , 'J/' , 'K/' , 'L/' , 'M/' , 'N/' , 'O/' , 'P/' , 'R/' , 'S/' , 'T/' , 'U/' , 'V/' , 'W/' , 'X/' , 'Y/' , 'Z/' ]
 if 97 - 97: IIIi . iI1iI1I1i1I / oOo0O0Ooo
 if 83 - 83: iI1iI1I1i1I - Ii1I * OoOo00o
 for O00 in O0Oo :
  i1iiIII1IIiIIII = i1111iI1 + O00
  oOO00OO0OooOo = O000OO0 ( i1iiIII1IIiIIII )
  if O0OOoOooO00 != 'Failed' :
   ii111iI1i1 = re . compile ( '<li><a href="(.+?)"> (.+?)</a></li>' ) . findall ( oOO00OO0OooOo )
   for O0oooo000oO0 , I1i1i1iii in ii111iI1i1 :
    if iiIiIIIiiI in I1i1i1iii . lower ( ) :
     i1II1IiIII111 ( ( '[COLORgreen]' + I1i1i1iii + 'source 5[/COLOR]' ) . replace ( 'Ganool' , '' ) . replace ( 'ShAaNiG' , '' ) . replace ( 'YIFY' , '' ) . replace ( '[[ Max-Movie.In ]]' , '' ) . replace ( '.mkv' , '' ) . replace ( '.mp4' , '' ) . replace ( '.' , ' ' ) , ( i1111iI1 + O00 + O0oooo000oO0 ) , 222 , '' )
     Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     Oo0oO0ooo . update ( 100 , "" , "Getting Source 5 Links" )
     if 80 - 80: oO0o / OooO0OoOOOO * oOo0O0Ooo % OooO0OoOOOO
     o00oooO0Oo ( 'tvshows' , 'Media Info 3' )
     if 95 - 95: o0o00Oo0O / iI1iI1I1i1I . IIIi
     if 17 - 17: iI1iI1I1i1I
def o0OO0OO000OO ( ) :
 if 92 - 92: iI1iI1I1i1I % ooOoO0O00 % O0OoO % OooO0OoOOOO % I11i
 iiIiIIIiiI = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 II11IiIi11 = iiIiIIIiiI . lower ( )
 o0OoO0oo0O0o = ( i1111 ( 'aHR0cDovL2Nvb2x0dnNlcmllcy5jb20vc2VhcmNoLnBocD90YWc9' ) ) + ( iiIiIIIiiI ) . replace ( ' ' , '+' )
 OooOoOo = ( i1111 ( 'aHR0cDovL2RsLmZhcnNpbW92aWUubmV0L1NlcmlhbC8=' ) )
 OOoOoOo = ( i1111 ( 'aHR0cDovL3N2Mi5kbC1wYXJzLmluLw==' ) )
 iI1i11 = ( i1111 ( 'aHR0cDovL3R2LmRsLXBhcnMuaW4v' ) )
 O00Ooo0O0OOOo = ( i1111 ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9BbWVyaWNhbiUyMFNlcmlhbC8=' ) )
 iIo00OOOOOo0OOo = ( i1111 ( 'aHR0cDovL2RpemlsYWIuY29tL2Fyc2l2P2xpbWl0PSZ0dXI9Jm9yZGVyYnk9JnVsa2U9Jm9yZGVyPSZ5aWw9JmRpemlfYWRpPQ==' ) ) + ( iiIiIIIiiI ) . replace ( ' ' , '+' )
 i1II11I11ii1 = ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvc2hvd3MvdHZhbGwucGhw' ) )
 OOoO0oO00oOOO0OoO0oo0OO = ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9UaGVfUmVhcGVyL2FsbHR2LnBocA==' ) )
 i1iI1Ii11Ii1 = ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC90dmZ1bGwucGhw' ) )
 if 92 - 92: Ii11Ii1I - iI11I1II1I1I
 Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Checking Sources" , '' , 'Please Wait' )
 I1111iiiII1Ii = O000OO0 ( o0OoO0oo0O0o )
 Oo0oO0ooo . update ( 0 , "" , "Checking Source 1/9 Links" )
 o00OO00OoO = O000OO0 ( OooOoOo )
 Oo0oO0ooo . update ( 14 , "" , "Checking Source 2/9 Links" )
 OOOO0OOoO0O0 = O000OO0 ( OOoOoOo )
 Oo0oO0ooo . update ( 28 , "" , "Checking Source 3/9 Links" )
 O0Oo000ooO00 = O000OO0 ( iI1i11 )
 Oo0oO0ooo . update ( 40 , "" , "Checking Source 4/9 Links" )
 oO0 = O000OO0 ( O00Ooo0O0OOOo )
 Oo0oO0ooo . update ( 52 , "" , "Checking Source 5/9 Links" )
 O0OOoOooO00 = cloudflare . source ( iIo00OOOOOo0OOo )
 Oo0oO0ooo . update ( 64 , "" , "Checking Source 6/9 Links" )
 oOO00OO0OooOo = O000OO0 ( i1II11I11ii1 )
 Oo0oO0ooo . update ( 76 , "" , "Checking Source 7/9 Links" )
 o0o00OOOO = O000OO0 ( OOoO0oO00oOOO0OoO0oo0OO )
 Oo0oO0ooo . update ( 88 , "" , "Checking Source 8/9 Links" )
 i11iIi1iIIIIi = O000OO0 ( i1iI1Ii11Ii1 )
 Oo0oO0ooo . update ( 100 , "" , "Checking Source 9/9 Links" )
 if 30 - 30: iI1iI1I1i1I / Ii1I
 if i11iIi1iIIIIi != 'Failed' :
  Ii1IOOooO00OO = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( i11iIi1iIIIIi )
  for OooOoOo , OOOOO0O00 , iIII , I1Ii11II1I1 , I1i1i1iii in Ii1IOOooO00OO :
   if iiIiIIIiiI in I1i1i1iii . lower ( ) :
    IIII ( ( '[COLORgreen]' + I1i1i1iii + '- source HeroVision[/COLOR]' ) , OooOoOo , 1016 , OOOOO0O00 , I1Ii11II1I1 , iIII )
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 10 , "" , "Getting Herovision Links" )
    if 22 - 22: OoOo00o * o0oOO0O00o0O
    o00oooO0Oo ( 'tvshows' , 'Media Info 3' )
    if 4 - 4: OOooOOo - OoOo00o + oOo0O0Ooo
 if o0o00OOOO != 'Failed' :
  i11i = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( o0o00OOOO )
  for OooOoOo , OOOOO0O00 , iIII , I1Ii11II1I1 , I1i1i1iii in i11i :
   if iiIiIIIiiI in I1i1i1iii . lower ( ) :
    IIII ( ( '[COLORgreen]' + I1i1i1iii + '- source Reaper[/COLOR]' ) , OooOoOo , 1016 , OOOOO0O00 , I1Ii11II1I1 , iIII )
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 20 , "" , "Getting Reaper Links" )
    if 36 - 36: OooO0OoOOOO
    o00oooO0Oo ( 'tvshows' , 'Media Info 3' )
    if 19 - 19: OOooOOo . I11i . ii
 if I1111iiiII1Ii != 'Failed' :
  IiIIi11i = re . compile ( 'href="([^"]*)"><img src="([^"]*)" alt="([^"]*)"' ) . findall ( I1111iiiII1Ii )
  for OooOoOo , I1i11 , I1i1i1iii in IiIIi11i :
   if iiIiIIIiiI in I1i1i1iii . lower ( ) :
    O0II11i11II ( '[COLORgreen]' + I1i1i1iii + ' CoolSeries[/COLOR]' , OooOoOo , 7052 , I1i11 )
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 30 , "" , "Getting CoolSeries Links" )
    if 13 - 13: IIIii1II1II . I1ii11iIi11i / IIiIiII11i
    o00oooO0Oo ( 'tvshows' , 'Media Info 3' )
 if o00OO00OoO != 'Failed' :
  iiIii = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( o00OO00OoO )
  for I1i1i1iii in iiIii :
   if iiIiIIIiiI in I1i1i1iii . lower ( ) :
    O0II11i11II ( '[COLORgreen]' + ( I1i1i1iii ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) + ' source 1 [/COLOR]' , ( OooOoOo + I1i1i1iii ) . replace ( ' ' , '%20' ) , 1006 , '' )
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 40 , "" , "Getting Source 1 Links" )
    if 43 - 43: iI11I1II1I1I % oO0o
    o00oooO0Oo ( 'tvshows' , 'Media Info 3' )
 if OOOO0OOoO0O0 != 'Failed' :
  ooo0O = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( OOOO0OOoO0O0 )
  for I1i1i1iii in ooo0O :
   if iiIiIIIiiI in I1i1i1iii . lower ( ) :
    O0II11i11II ( ( I1i1i1iii + ' source 2' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( OOoOoOo + I1i1i1iii ) . replace ( ' ' , '%20' ) , 1006 , '' )
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 50 , "" , "Getting Source 2 Links" )
    if 84 - 84: I1ii11iIi11i
    o00oooO0Oo ( 'tvshows' , 'Media Info 3' )
 if O0Oo000ooO00 != 'Failed' :
  i111iiIIII = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( O0Oo000ooO00 )
  for I1i1i1iii in ooo0O :
   if iiIiIIIiiI in I1i1i1iii . lower ( ) :
    O0II11i11II ( ( I1i1i1iii + ' source 3' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( iI1i11 + I1i1i1iii ) . replace ( ' ' , '%20' ) , 1006 , '' )
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 60 , "" , "Getting Source 3 Links" )
    if 44 - 44: ii * Ii / I1ii11iIi11i
    o00oooO0Oo ( 'tvshows' , 'Media Info 3' )
 if oO0 != 'Failed' :
  OoOoO00o00 = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( oO0 )
  for I1i1i1iii in ooo0O :
   if iiIiIIIiiI in I1i1i1iii . lower ( ) :
    O0II11i11II ( ( I1i1i1iii + ' source 4' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( O00Ooo0O0OOOo + I1i1i1iii ) . replace ( ' ' , '%20' ) , 1006 , '' )
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 70 , "" , "Getting Source 4 Links" )
    if 51 - 51: I1ii11iIi11i * iI11I1II1I1I . ii . Ii11Ii1I - IIIii1II1II / oOo0O0Ooo
    o00oooO0Oo ( 'tvshows' , 'Media Info 3' )
 if O0OOoOooO00 != 'Failed' :
  I111Iii1 = re . compile ( '<a href="(.+?)" class="film-image">\n<img src="(.+?)" alt=""/>\n</a>\n<div class="tss-detail">\n<a class="title" style="" href=".+?">\n<span class="position">.+?</span>\n(.+?)</a>' ) . findall ( O0OOoOooO00 )
  for OooOoOo , I1i11 , I1i1i1iii in I111Iii1 :
   if iiIiIIIiiI in I1i1i1iii . lower ( ) :
    O0II11i11II ( '[COLORgreen]' + I1i1i1iii + ' - Source - Dizi[/COLOR]' , OooOoOo , 8062 , I1i11 )
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 80 , "" , "Getting Dizi Links" )
    if 98 - 98: IIiIiII11i + Ii11Ii1I + ii / ooOoO0O00 - Ii11Ii1I
    o00oooO0Oo ( 'tvshows' , 'Media Info 3' )
 if oOO00OO0OooOo != 'Failed' :
  ii111iI1i1 = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( oOO00OO0OooOo )
  for OooOoOo , OOOOO0O00 , iIII , I1Ii11II1I1 , I1i1i1iii in ii111iI1i1 :
   if iiIiIIIiiI in I1i1i1iii . lower ( ) :
    IIII ( ( '[COLORgreen]' + I1i1i1iii + '- Source Scooby[/COLOR]' ) , OooOoOo , 1016 , OOOOO0O00 , I1Ii11II1I1 , iIII )
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 90 , "" , "Getting Scooby Links" )
    if 87 - 87: o0oOO0O00o0O / iI1iI1I1i1I / iI1iI1I1i1I % ii - Ii1I * OoOo00o
    o00oooO0Oo ( 'tvshows' , 'Media Info 3' )
    if 23 - 23: Ii
 OOooOoO = [ 'a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' , 'p' , 'q' , 'r' , 's' , 't' , 'u' , 'v' , 'w' , 'x' , 'y' , 'z' ]
 if 24 - 24: I11i + oOo0O0Ooo - IIiIiII11i
 for O00 in OOooOoO :
  i1iiIII1IIiIIII = IIIII + O00 + ooOoOoo0O
  oO0oOoOoo0 = oO0OOoo0OO ( i1iiIII1IIiIIII )
  if oO0oOoOoo0 != 'Failed' :
   oO0OOO00 = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( oO0oOoOoo0 )
   for I1i1i1iii , iIII , OooOoOo , I1i11 , Iii , i1iIIi1II1iiI in oO0OOO00 :
    if iiIiIIIiiI in I1i1i1iii . lower ( ) :
     IIII ( '[COLORgreen]' + I1i1i1iii + ' - Source Pandoras[/COLOR]' , OooOoOo , i1iIIi1II1iiI , I1i11 , Iii , iIII )
     Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     Oo0oO0ooo . update ( 100 , "" , "Getting Pandoras Links" )
     if 29 - 29: oOo0O0Ooo + Ii . o0o00Oo0O
     o00oooO0Oo ( 'tvshows' , 'Media Info 3' )
     if 75 - 75: IIIi + iI11I1II1I1I
     if 19 - 19: oOo0O0Ooo + Ii . OooO0OoOOOO - iI1iI1I1i1I / Ii11Ii1I + I11i
 xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
def II1io0Oo00oOO ( ) :
 if 73 - 73: iI1iI1I1i1I / ii . IIiIiII11i - OooO0OoOOOO * O0OoO * OooO0OoOOOO
 iiIiIIIiiI = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 II11IiIi11 = iiIiIIIiiI . lower ( )
 OooOoOo = ( i1111 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz' ) )
 o00OO00OoO = oO0OOoo0OO ( OooOoOo )
 iiIii = re . compile ( '"id":".+?","name":"(.+?)","img":"(.+?)","stream_url3":".+?","cat_id":"(.+?)","stream_url2":".+?","stream_url":".+?"}' , re . DOTALL ) . findall ( o00OO00OoO )
 for I1i1i1iii , I1i11 , IiI1IiI1iiI1 in iiIii :
  O000o0 = i1111 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv' ) + ( I1i11 ) . replace ( '\\' , '' )
  if iiIiIIIiiI in I1i1i1iii . lower ( ) :
   O0II11i11II ( I1i1i1iii , '' , 7022 , O000o0 )
   if 39 - 39: IIiIiII11i + ii / IIIii1II1II / Ii11Ii1I * OOooOOo
 xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
Oo0Oo = '{ZH},' ; iiO0Oo0 = '{IX},' ; oOOo0O = '{LM},'
if 73 - 73: oOo0O0Ooo - o0oOO0O00o0O . o0oOO0O00o0O
def I1I1O0O ( url ) :
 OO0ooO00o = cloudflare . source ( url )
 iiIii = re . compile ( '<a class="season" href="(.+?)">\n(.+?)\n</a>\n</span>\n<span>\n<a class="episode" href=".+?">\n(.+?)\n</a>\n</span>\n<span>\n<a class="episode-name" href=".+?">\n(.+?)</a>' ) . findall ( OO0ooO00o )
 for url , oOo0Oo0O0O , I1111i , I1i1i1iii in iiIii :
  O0II11i11II ( ( oOo0Oo0O0O ) . replace ( 'Sezon' , ' Season ' ) + ( I1111i ) . replace ( 'Bölüm' , ' Episode ' ) + I1i1i1iii , url , 8063 , '' )
  if 24 - 24: IIIi + ii . OooO0OoOOOO / OOooOOo / iI1iI1I1i1I
  if 65 - 65: ii
  if 18 - 18: o0o00Oo0O - ooOoO0O00 . IIIi
  if 98 - 98: I11i
def OOo00Oooo ( url ) :
 OO0ooO00o = cloudflare . source ( url )
 iiIii = re . compile ( 'file: "(.+?)",.+?label: "(.+?)",' , re . DOTALL ) . findall ( OO0ooO00o )
 for url , I1i1i1iii in iiIii :
  i1II1IiIII111 ( I1i1i1iii , url , 222 , '' )
  if 15 - 15: O0OoO . iI11I1II1I1I * oOo0O0Ooo % iI1iI1I1i1I
  if 21 - 21: oO0o - oOo0O0Ooo . ii
  if 6 - 6: iI11I1II1I1I - iI11I1II1I1I % I11i / iI11I1II1I1I * IIIi
  if 3 - 3: IIIii1II1II . OooO0OoOOOO / I1ii11iIi11i
def OooIIi111 ( ) :
 if 61 - 61: Ii1I - IIIii1II1II
 OO0ooO00o = cloudflare . source ( i1111 ( 'aHR0cDovL2RpemlsYWIuY29t' ) )
 iiIii = re . compile ( '<li id=".+?">.+?<a href="(.+?)">.+?<img width="40" height="40" src="(.+?)" alt=""/>.+?<span class="title">\n(.+?)</span>.+?<span class="alt-title">\n(.+?)</span>.+?</a>.+?</li>' , re . DOTALL ) . findall ( OO0ooO00o )
 for OooOoOo , I1i11 , I1i1i1iii , I1111i in iiIii :
  O0II11i11II ( I1i1i1iii + '  -  ' + ( I1111i ) . replace ( 'sezon' , 'Season' ) . replace ( 'bölüm' , 'Episode' ) , OooOoOo , 8063 , I1i11 )
  if 16 - 16: o0oOO0O00o0O / iI11I1II1I1I + IIIii1II1II * o0oOO0O00o0O * iI1iI1I1i1I
def iiIiI11IiI1ii ( ) :
 I1i11i = IiIi ( i1111 ( 'aHR0cDovL3d3dy50dmd1aWRlLmNvLnVrLw==' ) )
 iiIii = re . compile ( '<a href="(.+?)"  qt-title=".+?" qt-text=".+?<br> .+?" title="(.+?)".+?class=".+? src="(.+?)" alt=".+?" /></a>' , re . DOTALL ) . findall ( I1i11i )
 for OooOoOo , I1i1i1iii , I1i11 in iiIii :
  i1II1IiIII111 ( '[COLORgreen]' + I1i1i1iii + '[/COLOR]' , OooOoOo , 8002 , I1i11 )
def ooO0O0 ( url ) :
 I1i11i = IiIi ( url )
 iiIii = re . compile ( '<table border="0".+?url((.+?));background-repeat: no-repeat;">.+?<tr>.+?<span class="season">(.+?)</span><br>.+?<a href="(.+?)"+?>(.+?)</span><br>.+?<span class="programmetext">(.+?)</span></a><br>' , re . DOTALL ) . findall ( I1i11i )
 for I1i11 , time , url , I1i1i1iii , o0oo0O in iiIii :
  IIII ( '%s %s' % ( '[COLORgreen]' + I1i1i1iii + '[/COLOR]' , time ) , url , 1015 , I1i11 , o0oo0O )
  if 34 - 34: ooOoO0O00 - OOooOOo + I11i - I1ii11iIi11i % Ii1I
def I11ii1iI11 ( ) :
 if 6 - 6: OooO0OoOOOO * IIiIiII11i % iI11I1II1I1I
 O0II11i11II ( 'Coronation Street' , '' , 8001 , '' )
 O0II11i11II ( 'Eastenders' , '' , 8002 , '' )
 O0II11i11II ( 'Emmerdale' , '' , 8003 , '' )
 O0II11i11II ( 'Hollyoaks' , '' , 8004 , '' )
 O0II11i11II ( 'Im a Celebrity' , '' , 8005 , '' )
 if 86 - 86: ooOoO0O00 * o0o00Oo0O % O0OoO . I1ii11iIi11i % O0OoO . I1ii11iIi11i
 if 71 - 71: o0oOO0O00o0O . Ii * o0o00Oo0O + o0o00Oo0O
 if 57 - 57: ii . iI1iI1I1i1I % IIiIiII11i % oOo0O0Ooo + Ii11Ii1I
 if 70 - 70: OooO0OoOOOO . Ii
def O0O00O0Oo0 ( ) :
 o00OO00OoO = oO0OOoo0OO ( 'http://uksoapshare.blogspot.co.uk/' )
 iiIii = re . compile ( '<a href="(.+?)".+?target=_blank>(.+?)</a>' ) . findall ( o00OO00OoO )
 for OooOoOo , I1i1i1iii in iiIii :
  if 'Holly' in I1i1i1iii :
   I1i11 = 'http://2.bp.blogspot.com/-9c7Sieh1RKs/UjD6TGAEEnI/AAAAAAAAAC8/84uwHfxcuYg/s1600/Hollyoaks.png'
   if 'huge' in OooOoOo :
    i1II1IiIII111 ( ( I1i1i1iii ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , OooOoOo . replace ( '\\/' , '/' ) , 8006 , I1i11 )
   else :
    pass
    if 53 - 53: ooOoO0O00 . ooOoO0O00 - iI1iI1I1i1I / o0oOO0O00o0O - OOooOOo % oOo0O0Ooo
 xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE_IGNORE_THE ) ;
 if 65 - 65: o0oOO0O00o0O . ii - o0o00Oo0O . o0oOO0O00o0O - Ii
def IIoOoo0OO0 ( ) :
 o00OO00OoO = oO0OOoo0OO ( 'http://uksoapshare.blogspot.co.uk/' )
 iiIii = re . compile ( '<a href="(.+?)".+?target=_blank>(.+?)</a>' ) . findall ( o00OO00OoO )
 for OooOoOo , I1i1i1iii in iiIii :
  if 'East' in I1i1i1iii :
   I1i11 = 'http://3.bp.blogspot.com/-KWHcNbNJU8Y/Vi1ousRl7fI/AAAAAAAAAT8/ksNE12LH0nE/s1600/eastenders.jpg'
   if 'huge' in OooOoOo :
    i1II1IiIII111 ( ( I1i1i1iii ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , OooOoOo . replace ( '\\/' , '/' ) , 8006 , I1i11 )
   else :
    pass
    if 5 - 5: Ii * I1ii11iIi11i
 xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 29 - 29: Ii11Ii1I / O0OoO % iI1iI1I1i1I
def ii1iIII1ii ( ) :
 o00OO00OoO = oO0OOoo0OO ( 'http://uksoapshare.blogspot.co.uk/' )
 iiIii = re . compile ( '<a href="(.+?)".+?target=_blank>(.+?)</a>' ) . findall ( o00OO00OoO )
 for OooOoOo , I1i1i1iii in iiIii :
  if 'Emmer' in I1i1i1iii :
   I1i11 = 'http://2.bp.blogspot.com/-UfDcxisVV5c/UjH9vUicZ3I/AAAAAAAAADc/8Ozuiz1ojxw/s1600/Emmerdale.jpg'
   if 'huge' in OooOoOo :
    i1II1IiIII111 ( ( I1i1i1iii ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , OooOoOo . replace ( '\\/' , '/' ) , 8006 , I1i11 )
   else :
    pass
    if 47 - 47: iI1iI1I1i1I . o0oOO0O00o0O * Ii11Ii1I - O0OoO . iI1iI1I1i1I - IIIii1II1II
 xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 94 - 94: oOo0O0Ooo % OooO0OoOOOO + oO0o
def OoOooO ( ) :
 o00OO00OoO = oO0OOoo0OO ( 'http://uksoapshare.blogspot.co.uk/' )
 iiIii = re . compile ( '<a href="(.+?)".+?target=_blank>(.+?)</a>' ) . findall ( o00OO00OoO )
 for OooOoOo , I1i1i1iii in iiIii :
  if 'Coro' in I1i1i1iii :
   I1i11 = 'http://3.bp.blogspot.com/-hofvfBQVexs/UjErIfNdS4I/AAAAAAAAADQ/Q-vVGu3apYU/s1600/corrie.jpg'
   if 'huge' in OooOoOo :
    i1II1IiIII111 ( ( I1i1i1iii ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , OooOoOo . replace ( '\\/' , '/' ) , 8006 , I1i11 )
   else :
    pass
    if 50 - 50: OooO0OoOOOO . O0OoO - o0o00Oo0O % oOo0O0Ooo . IIIi
 xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 17 - 17: o0o00Oo0O + ii
def oo0OooO ( ) :
 o00OO00OoO = oO0OOoo0OO ( 'http://uksoapshare.blogspot.co.uk/' )
 iiIii = re . compile ( '<a href="(.+?)" target="_blank">(.+?)</a>' ) . findall ( o00OO00OoO )
 for OooOoOo , I1i1i1iii in iiIii :
  if 'Celeb' in I1i1i1iii :
   I1i11 = 'http://3.bp.blogspot.com/-a_yDotWU_pY/VkotKWaG_gI/AAAAAAAAAUk/8Q5iNM6p37k/s1600/iacgoh.jpg'
   if 'huge' in OooOoOo :
    i1II1IiIII111 ( ( I1i1i1iii ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , OooOoOo . replace ( '\\/' , '/' ) , 8006 , I1i11 )
   else :
    pass
    if 4 - 4: OooO0OoOOOO + iI11I1II1I1I * o0oOO0O00o0O + I1ii11iIi11i * I11i % IIiIiII11i
def OO0o0o0oo ( name , url ) :
 iIiII1 = urlresolver . HostedMediaFile ( url ) . valid_url ( )
 if iIiII1 :
  i111iii1I1 = urlresolver . HostedMediaFile ( url ) . resolve ( )
 else :
  I1i11i = open_url ( url )
  url = re . compile ( 'src="(.+?)"></iframe>' ) . findall ( I1i11i ) [ 0 ]
  url = url . split ( '?autoplay' ) [ 0 ]
  I1i11i = open_url ( url )
  iiIiII1 = re . compile ( 'mp4","url":"(.+?)"' ) . findall ( I1i11i ) [ - 1 ]
  i111iii1I1 = iiIiII1 . replace ( '\\/' , '/' )
 Oo000 = xbmcgui . ListItem ( name , '' , '' )
 Oo000 . setPath ( i111iii1I1 )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , Oo000 )
 if 37 - 37: o0o00Oo0O + O0OoO * IIIii1II1II
 if 27 - 27: o0o00Oo0O . IIiIiII11i + OooO0OoOOOO % I11i
def oo0O0oOOO0o ( ) :
 I1i11i = oO0OOoo0OO ( i1111 ( 'aHR0cDovL3d3dy5kaXppYm94aGQuY29tLw==' ) )
 iiIii = re . compile ( 'class="film menu-item menu-item-type-post_type menu-item-object-page menu-item-36980"><a href="(.+?)"><i class="fa fa-film"></i><span>(.+?)</span></a></li>' ) . findall ( I1i11i )
 ooo0O = re . compile ( 'class="menu-item menu-item-type-post_type menu-item-object-page menu-item-52949"><a href="(.+?)"><i class="fa fa-"></i><span>(.+?)</span></a></li>' ) . findall ( I1i11i )
 for OooOoOo , I1i1i1iii in iiIii :
  O0II11i11II ( ( '[COLORgreen]' + I1i1i1iii + '[/COLOR]' ) . replace ( 'Diziler' , 'Series' ) , OooOoOo , 7071 , ooOooo000oOO + 'popcorn.png' )
 for OooOoOo , I1i1i1iii in ooo0O :
  O0II11i11II ( ( '[COLORgreen]' + I1i1i1iii + '[/COLOR]' ) . replace ( 'Filmler' , 'Movies' ) , OooOoOo , 7071 , ooOooo000oOO + 'popcorn.png' )
  if 70 - 70: I1ii11iIi11i % Ii11Ii1I . Ii1I
def Ii1111iiI ( ) :
 I1i11i = oO0OOoo0OO ( i1111 ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL2NhdGVnb3JpZXMv' ) )
 iiIii = re . compile ( '<a class="nav-item" href="(.+?)">(.+?)</a>' ) . findall ( I1i11i )
 for OooOoOo , I1i1i1iii in iiIii :
  if 'Movies' in I1i1i1iii :
   O0II11i11II ( '[COLORgreen]' + I1i1i1iii + '[/COLOR]' , 'http://www.snagfilms.com' + ( OooOoOo ) . replace ( 'http://www.snagfilms.com' , '' ) , 7061 , ooOooo000oOO + 'popcorn.png' )
def I1I ( url ) :
 I1i11i = oO0OOoo0OO ( url )
 iiIii = re . compile ( '<a class="object-link size-poster".+?href="(.+?)" data-type="category">.+?src="(.+?)" alt="Image of (.+?)" />' , re . DOTALL ) . findall ( I1i11i )
 iiIii = re . compile ( '<a class="object-link size-poster".+?href="(.+?)" data-type="category">.+?src="(.+?)" alt="Image of (.+?)" />' , re . DOTALL ) . findall ( I1i11i )
 ooo0O = re . compile ( "<li class='current'>.+?</li><li ><a href='(.+?)'>.+?</a></li><li" , re . DOTALL ) . findall ( I1i11i )
 for url , I1i11 , I1i1i1iii in iiIii :
  O0II11i11II ( '[COLORgreen]' + I1i1i1iii + '[/COLOR]' , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7067 , I1i11 )
 for url in ooo0O :
  O0II11i11II ( '[COLORgreen]NEXT PAGE[/COLOR]' , ( url ) . replace ( '&#038;' , '&' ) , 7063 , ooOooo000oOO + 'Next.png' )
  if 53 - 53: OOooOOo
  if 84 - 84: oO0o
def o0OO ( url ) :
 I1i11i = oO0OOoo0OO ( i1111 ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL2NhdGVnb3JpZXMv' ) )
 iiIii = re . compile ( '<a class="object-link size-poster".+?href="(.+?)" data-type="category">.+?src="(.+?)" alt="Image of (.+?)" />' , re . DOTALL ) . findall ( I1i11i )
 for url , I1i11 , I1i1i1iii in iiIii :
  O0II11i11II ( '[COLORgreen]' + I1i1i1iii + '[/COLOR]' , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7062 , I1i11 )
  if 17 - 17: O0OoO + Ii1I * Ii
oO00OOOOOO0o = '{UJ},' ; iIIIOoO0000 = '{WE},' ; III11iIIi = '{WP},' ; iIIi = '{PP},'
def i1I111iIii1i1 ( url ) :
 I1i11i = oO0OOoo0OO ( url )
 iiIii = re . compile ( 'href="(.+?)".+?src="(.+?)" alt="Image of (.+?)"' , re . DOTALL ) . findall ( I1i11i )
 for url , I1i11 , I1i1i1iii in iiIii :
  O0II11i11II ( ( '[COLORgreen]' + I1i1i1iii + '[/COLOR]' ) . replace ( '&#x27;' , '' ) , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7067 , I1i11 )
  if 80 - 80: IIIi / Ii + ii
def III11i1iI11 ( url ) :
 I1i11i = oO0OOoo0OO ( url )
 iiIii = re . compile ( '<div class="film-container">.+?<iframe src="(.+?)"' , re . DOTALL ) . findall ( I1i11i )
 for url in iiIii :
  o0o0OOo0O ( 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) )
  if 64 - 64: OoOo00o * Ii1I / ooOoO0O00 * oO0o . OoOo00o
def o0o0OOo0O ( url ) :
 I1i11i = oO0OOoo0OO ( url )
 iiIii = re . compile ( 'file: "(.+?)",.+?label: "(.+?)"' , re . DOTALL ) . findall ( I1i11i )
 for url , I1i1i1iii in iiIii :
  i1II1IiIII111 ( '[COLORgreen]' + I1i1i1iii + '[/COLOR]' , url , 222 , ooOooo000oOO + 'popcorn.png' )
  if 60 - 60: iI1iI1I1i1I
  if 93 - 93: I1ii11iIi11i
  if 75 - 75: OOooOOo
  if 64 - 64: OooO0OoOOOO / I11i / ooOoO0O00
def OOo0OOOoOOo ( url ) :
 I1i11i = oO0OOoo0OO ( url )
 iiIii = re . compile ( '</h4><p><ul><li><a href="([^"]*)">(.+?)<.+?class=' ) . findall ( I1i11i )
 ooo0O = re . compile ( '<li><a href="([^"]*)">(.+?)<.+?class=' ) . findall ( I1i11i )
 for url , I1i1i1iii in iiIii :
  if '(cooltvseries.com)' in I1i1i1iii :
   i1II1IiIII111 ( ( '[COLORgreen]' + I1i1i1iii + ' -(360)-[/COLOR]' ) . replace ( ' - (cooltvseries.com).mp4' , '' ) , url , 7053 , ooOooo000oOO + 'CoolSeries.png' )
 for url , I1i1i1iii in ooo0O :
  if '(cooltvseries.com)' in I1i1i1iii :
   i1II1IiIII111 ( ( '[COLORgreen]' + I1i1i1iii + '[/COLOR]' ) . replace ( ' - (cooltvseries.com).mp4' , '' ) , url , 7053 , ooOooo000oOO + 'CoolSeries.png' )
def III ( url ) :
 I1i11i = oO0OOoo0OO ( url )
 iiIii = re . compile ( '<source type="video/mp4" src="([^"]*)"/>' ) . findall ( I1i11i )
 for url in iiIii :
  o0oOOo0O0O000 ( ( url ) . replace ( ' ' , '%20' ) )
ooo0o0O = '{XX},' ; IiiiIIi11II = '{UD},' ; o0oooOo0oo = '{YT},' ; i1iI1IIi1I = '{JS},' ; oo00i1i11I1I1 = '{PF},'
if 82 - 82: oO0o - I1ii11iIi11i - o0o00Oo0O - ii
def Ii1I1Iiii ( ) :
 I1i11i = oO0OOoo0OO ( i1111 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vc2VjcmV0L2Nsb3VkLnBocA==' ) )
 iiIii = re . compile ( '<li class="col-sm-2">.+?<a href="#" class="thumbnail" data-src="(.+?)" data-toggle="modal".+?data-target="#infoModal" name="(.+?)"> <img src="(.+?)" alt=".+?" width="130px"' , re . DOTALL ) . findall ( I1i11i )
 for OooOoOo , I1i1i1iii , I1i11 in iiIii :
  i1II1IiIII111 ( '[COLORgreen]' + I1i1i1iii + '[/COLOR]' , 'http://stream.cloudtv.bz/stream/channel/20/' + ( i1111 ( OooOoOo ) ) , 222 , I1i11 )
  if 80 - 80: IIIii1II1II . Ii11Ii1I + iI11I1II1I1I
def iI11I ( url ) :
 I1i11i = oO0OOoo0OO ( url )
 iiIii = re . compile ( 'src="([^"]*)".+?alt=""></a><div class="entry unvoted"><p class="title"><a class="title may-blank " href="([^"]*)" tabindex=.+?>(.+?)</a>' , re . DOTALL ) . findall ( I1i11i )
 next = re . compile ( '<a href="([^"]*)" rel="nofollow next"' , re . DOTALL ) . findall ( I1i11i )
 for I1i11 , url , I1i1i1iii in iiIii :
  if 'youtu' in url :
   i1II1IiIII111 ( ( '[COLORgreen]' + I1i1i1iii + '[/COLOR]' ) . replace ( '&quot;' , '"' ) . replace ( '&' , ' & ' ) , url , 7051 , 'http:' + I1i11 )
 for url in next :
  O0II11i11II ( '[COLORgreen]NEXT[/COLOR]' , url , 7050 , ooOooo000oOO + 'Next.png' )
  if 39 - 39: iI11I1II1I1I - OoOo00o / OooO0OoOOOO * o0o00Oo0O
def oooo0O0Oooo ( url ) :
 I1i11i = oO0OOoo0OO ( url )
 iiIii = re . compile ( 'rel="shortlink" href="([^"]*)">' , re . DOTALL ) . findall ( I1i11i )
 for url in iiIii :
  yt . PlayVideo ( ( url ) . replace ( 'https://youtu.be/' , '' ) )
  if 39 - 39: OoOo00o / O0OoO * IIiIiII11i * o0oOO0O00o0O
def IiIii11i1IIiI ( url ) :
 I1i11i = oO0OOoo0OO
 iiIii = re . compile ( 'id:"(.+?)",url:"(.+?)"' , re . DOTALL ) . findall ( I1i11i )
 for url , I1i11 , I1i1i1iii in iiIii :
  O0II11i11II ( '[COLORgreen]' + I1i1i1iii + '[/COLOR]' , url , 222 , I1i11 )
  if 40 - 40: o0oOO0O00o0O + iI11I1II1I1I * OoOo00o + Ii . Ii
  if 11 - 11: oO0o % ii
  if 20 - 20: IIIi + IIIi * IIiIiII11i * iI11I1II1I1I % o0o00Oo0O * oOo0O0Ooo
  if 62 - 62: ii / OOooOOo . OooO0OoOOOO . OooO0OoOOOO % O0OoO
  if 42 - 42: I11i . IIIii1II1II - O0OoO
def IiiiO0oo0ooo0 ( ) :
 if 19 - 19: ooOoO0O00
 O0II11i11II ( 'All Channels' , '' , 7021 , ooOooo000oOO + 'livetv.png' )
 O0II11i11II ( 'Entertainment' , '' , 7021 , ooOooo000oOO + 'livetv.png' )
 O0II11i11II ( 'Movies' , '' , 7021 , ooOooo000oOO + 'livetv.png' )
 O0II11i11II ( 'Music' , '' , 7021 , ooOooo000oOO + 'livetv.png' )
 O0II11i11II ( 'News' , '' , 7021 , ooOooo000oOO + 'livetv.png' )
 O0II11i11II ( 'Sports' , '' , 7021 , ooOooo000oOO + 'livetv.png' )
 O0II11i11II ( 'Documentary' , '' , 7021 , ooOooo000oOO + 'livetv.png' )
 O0II11i11II ( 'Kids' , '' , 7021 , ooOooo000oOO + 'livetv.png' )
 O0II11i11II ( 'Food' , '' , 7021 , ooOooo000oOO + 'livetv.png' )
 O0II11i11II ( 'Religious' , '' , 7021 , ooOooo000oOO + 'livetv.png' )
 O0II11i11II ( 'USA Channels' , '' , 7021 , ooOooo000oOO + 'livetv.png' )
 O0II11i11II ( 'Other' , '' , 7021 , ooOooo000oOO + 'livetv.png' )
 if 60 - 60: Ii11Ii1I * OOooOOo / I11i . IIIi
 if 22 - 22: OooO0OoOOOO * Ii11Ii1I - ii
def i1Ii1 ( Cat_Name ) :
 if 75 - 75: ii * Ii
 o0oOo = False
 OoIIiIIIII1I = '0'
 if Cat_Name == 'All Channels' : o0oOo = True
 if Cat_Name == 'Entertainment' : OoIIiIIIII1I = '1'
 if Cat_Name == 'Movies' : OoIIiIIIII1I = '2'
 if Cat_Name == 'Music' : OoIIiIIIII1I = '3'
 if Cat_Name == 'News' : OoIIiIIIII1I = '4'
 if Cat_Name == 'Sports' : OoIIiIIIII1I = '5'
 if Cat_Name == 'Documentary' : OoIIiIIIII1I = '6'
 if Cat_Name == 'Kids' : OoIIiIIIII1I = '7'
 if Cat_Name == 'Food' : OoIIiIIIII1I = '8'
 if Cat_Name == 'Religious' : OoIIiIIIII1I = '9'
 if Cat_Name == 'USA Channels' : OoIIiIIIII1I = '10'
 if Cat_Name == 'Other' : OoIIiIIIII1I = '11'
 if 96 - 96: Ii . IIiIiII11i
 I1i11i = oO0OOoo0OO ( i1111 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz' ) )
 iiIii = re . compile ( '"id":".+?","name":"(.+?)","img":"(.+?)","stream_url3":".+?","cat_id":"(.+?)","stream_url2":".+?","stream_url":".+?"}' , re . DOTALL ) . findall ( I1i11i )
 print 'Len Match: >>>' + str ( len ( iiIii ) )
 for I1i1i1iii , I1i11 , IiI1IiI1iiI1 in iiIii :
  O000o0 = i1111 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv' ) + ( I1i11 ) . replace ( '\\' , '' )
  if IiI1IiI1iiI1 == OoIIiIIIII1I :
   O0II11i11II ( I1i1i1iii , '' , 7022 , O000o0 )
  elif o0oOo == True :
   O0II11i11II ( I1i1i1iii , '' , 7022 , O000o0 )
  else : pass
  if 7 - 7: ooOoO0O00
  xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 63 - 63: iI11I1II1I1I + OooO0OoOOOO % ooOoO0O00 / oOo0O0Ooo % IIiIiII11i
def OO0 ( Search_Name ) :
 I1i11i = oO0OOoo0OO ( i1111 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz' ) )
 iiIii = re . compile ( '"id":".+?","name":"' + Search_Name + '","img":"(.+?)","stream_url3":"(.+?)","cat_id":".+?","stream_url2":"(.+?)","stream_url":"(.+?)"}' , re . DOTALL ) . findall ( I1i11i )
 iiIii = re . compile ( '"id":".+?","name":"' + Search_Name + '","img":"(.+?)","stream_url3":"(.+?)","cat_id":".+?","stream_url2":"(.+?)","stream_url":"(.+?)"}' , re . DOTALL ) . findall ( I1i11i )
 for I1i11 , OooOoOo , OOoOoOo , iI1i11 in iiIii :
  O000o0 = i1111 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv' ) + ( I1i11 ) . replace ( '\\' , '' )
  i1II1IiIII111 ( Search_Name + ': Link 1' , ( OooOoOo ) . replace ( '\\' , '' ) , 222 , O000o0 )
  i1II1IiIII111 ( Search_Name + ': Link 2' , ( OOoOoOo ) . replace ( '\\' , '' ) , 222 , O000o0 )
  i1II1IiIII111 ( Search_Name + ': Link 3' , ( iI1i11 ) . replace ( '\\' , '' ) , 222 , O000o0 )
  if 48 - 48: ooOoO0O00 * oOo0O0Ooo
def iiiIIiii11I1 ( ) :
 I1i11i = oO0OOoo0OO ( i1111 ( o0OO00 ( 0 , [ 97 ] , [ 221 , 72 , 245 , 82 , 68 , 48 , 242 , 99 , 143 , 68 , 9 , 111 , 24 , 118 , 180 , 76 , 29 , 51 , 14 , 100 , 187 , 51 , 105 , 100 , 106 , 121 , 52 , 53 , 240 , 114 , 26 , 98 , 252 , 50 , 197 , 82 , 218 , 112 , 19 , 99 , 94 , 71 , 54 , 120 , 104 , 108 , 174 , 101 , 107 , 72 , 168 , 82 , 191 , 50 , 88 , 76 , 90 , 109 , 138 , 78 , 24 , 118 , 89 , 76 , 218 , 110 , 231 , 86 , 105 , 114 , 252 , 76 , 37 , 50 , 36 , 82 , 96 , 118 , 27 , 100 , 120 , 50 , 160 , 53 , 72 , 115 , 200 , 98 , 80 , 50 , 201 , 70 , 114 , 107 , 9 , 99 , 113 , 121 , 127 , 57 , 155 , 106 , 213 , 97 , 194 , 71 , 192 , 70 , 162 , 116 , 27 , 99 , 46 , 71 , 191 , 108 , 4 , 118 , 24 , 98 , 27 , 109 , 105 , 108 , 89 , 119 , 164 , 100 , 88 , 72 , 237 , 89 , 93 , 117 , 40 , 98 , 211 , 84 , 75 , 78 , 216 , 49 ] ) ) )
 iiIii = re . compile ( '#EXTINF:-1,(.+)\s*(.+)\s*' ) . findall ( I1i11i )
 for I1i1i1iii , OooOoOo in iiIii :
  i1II1IiIII111 ( I1i1i1iii , ( OooOoOo ) . replace ( '"' , ' ' ) . replace ( '&' , '&' ) . strip ( ) + '|connection=keep-alive' , 222 , ooOooo000oOO + 'english.png' )
def oo0O ( ) :
 I1i11i = oO0OOoo0OO ( i1111 ( o0OO00 ( 0 , [ 97 ] , [ 221 , 72 , 245 , 82 , 68 , 48 , 242 , 99 , 143 , 68 , 9 , 111 , 24 , 118 , 180 , 76 , 29 , 51 , 14 , 100 , 187 , 51 , 105 , 100 , 106 , 121 , 52 , 53 , 240 , 114 , 26 , 98 , 252 , 50 , 197 , 82 , 218 , 112 , 19 , 99 , 94 , 71 , 54 , 120 , 104 , 108 , 174 , 101 , 107 , 72 , 168 , 82 , 191 , 50 , 88 , 76 , 90 , 109 , 138 , 78 , 24 , 118 , 89 , 76 , 218 , 110 , 231 , 86 , 105 , 114 , 252 , 76 , 37 , 50 , 36 , 82 , 96 , 118 , 27 , 100 , 120 , 50 , 160 , 53 , 72 , 115 , 200 , 98 , 80 , 50 , 201 , 70 , 114 , 107 , 9 , 99 , 113 , 121 , 127 , 57 , 155 , 106 , 213 , 97 , 194 , 71 , 192 , 70 , 162 , 116 , 27 , 99 , 46 , 71 , 191 , 108 , 4 , 118 , 24 , 98 , 27 , 109 , 105 , 108 , 89 , 119 , 164 , 100 , 88 , 72 , 237 , 89 , 93 , 117 , 40 , 98 , 211 , 84 , 75 , 78 , 216 , 49 ] ) ) )
 iiIii = re . compile ( '#EXTINF:-2,(.+)\s*(.+)\s*' ) . findall ( I1i11i )
 for I1i1i1iii , OooOoOo in iiIii :
  i1II1IiIII111 ( I1i1i1iii , ( OooOoOo ) . replace ( '"' , ' ' ) . replace ( '&' , '&' ) . strip ( ) , 222 , ooOooo000oOO + 'xxx.png' )
def Ooooo0O0 ( ) :
 I1i11i = oO0OOoo0OO ( i1111 ( o0OO00 ( 0 , [ 97 , 129 , 72 , 149 , 82 , 100 , 48 , 63 , 99 , 170 , 68 , 159 , 111 , 42 , 118 , 83 , 76 , 128 , 51 , 61 , 100 , 44 , 51 , 201 , 100 , 148 , 121 , 134 , 53 ] , [ 159 , 114 , 70 , 98 , 144 , 50 , 37 , 82 , 253 , 112 , 184 , 99 , 50 , 71 , 154 , 120 , 110 , 108 , 179 , 101 , 250 , 72 , 65 , 82 , 125 , 50 , 52 , 76 , 28 , 109 , 124 , 78 , 191 , 118 , 193 , 76 , 193 , 110 , 145 , 86 , 92 , 114 , 193 , 76 , 41 , 50 , 82 , 82 , 206 , 118 , 32 , 100 , 163 , 50 , 209 , 53 , 191 , 115 , 42 , 98 , 30 , 50 , 237 , 70 , 26 , 107 , 70 , 99 , 64 , 121 , 115 , 57 , 230 , 116 , 32 , 97 , 39 , 88 , 58 , 104 , 38 , 50 , 77 , 98 , 185 , 50 , 86 , 81 , 80 , 117 , 111 , 98 , 226 , 84 , 75 , 78 , 210 , 49 ] ) ) )
 iiIii = re . compile ( '#EXTINF:.+?,(.+)\s*(.+)\s*' ) . findall ( I1i11i )
 for I1i1i1iii , OooOoOo in iiIii :
  i1II1IiIII111 ( I1i1i1iii , ( OooOoOo ) . replace ( '"' , ' ' ) . replace ( '&' , '&' ) . strip ( ) , 222 , ooOooo000oOO + 'vod(1).png' )
  if 99 - 99: I1ii11iIi11i + Ii
def I111Ii11i11I ( url ) :
 url
 i11I = xbmcgui . ListItem ( I1i1i1iii , path = url )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , i11I )
 return
 if 75 - 75: OoOo00o * O0OoO
 if 88 - 88: oO0o * I11i * IIIii1II1II / I1ii11iIi11i * oO0o
def oOII11i1I ( url ) :
 I1i11i = oO0OOoo0OO ( url )
 iiIii = re . compile ( '<a class=.+?href="(.+?)">.+?<div class="videothumboverlay hidden-xs" id=".+?">(.+?)</div>.+?<div class="videothumbbox"><img src="(.+?)" class="videothumb" alt="(.+?)"></div>' , re . DOTALL ) . findall ( I1i11i )
 ooo0O = re . compile ( "<a href='(.+?)' class='paginationnext'>Next &raquo;</a></div>" ) . findall ( I1i11i )
 for url , iIII , I1i11 , I1i1i1iii in iiIii :
  IIII ( I1i1i1iii , 'https://www.fitnessblender.com' + url , 7086 , 'https://www.fitnessblender.com' + I1i11 , '' , ( iIII ) . replace ( '</p>' , ' ' ) . replace ( '<p>' , ' ' ) )
  o00oooO0Oo ( 'tvshows' , 'Media Info 3' )
 for url in ooo0O :
  O0II11i11II ( 'NEXT' , 'https://www.fitnessblender.com' + url , 7085 , ooOooo000oOO + 'Next.png' )
  if 69 - 69: O0OoO . IIIii1II1II - oOo0O0Ooo
def IiIiIi ( url ) :
 o00OO00OoO = oO0OOoo0OO ( url )
 iiIii = re . compile ( '<div class=\'videowrapper\'>.+?src="//www.youtube.com/embed/(.+?)?rel=0&amp;wmode=transparent" frameborder="0"></iframe></div>.+?<h3 class="videodetailheader">(.+?)</h3>.+?<p class="videodetailvalue"><img src=\'(.+?)\'/></p>' , re . DOTALL ) . findall ( o00OO00OoO )
 for url , iIII , I1i11 in iiIii :
  O0i1II1Iiii1I11 ( 'PLAY' , url , 8043 , 'https://www.fitnessblender.com' + I1i11 , '' , iIII )
  o00oooO0Oo ( 'tvshows' , 'Media Info 3' )
 OO000o = re . compile ( '<h2 class="videodetailheader">Workout Details</h2>(.+?)</div>' , re . DOTALL ) . findall ( o00OO00OoO )
 for iI1iii1iIiiI in OO000o :
  II1iiiiI1 = ( iI1iii1iIiiI ) . replace ( '<p>' , '' ) . replace ( '</p>' , '' ) . replace ( '<br />' , '' ) . replace ( '&nbsp;' , '' ) . replace ( '<strong>' , '' ) . replace ( '</strong>' , '' ) . replace ( '"' , '' ) . replace ( '<' , '' ) . replace ( '>' , '' ) . replace ( 'a href' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&rsquo;t' , '' ) . replace ( '&' , '&' )
  IIII ( 'INFO' , '' , 7087 , 'https://www.fitnessblender.com' + I1i11 , '' , II1iiiiI1 )
  if 33 - 33: ii % Ii1I . o0o00Oo0O / Ii1I
def O0OoOo ( INFO ) :
 o00o0 ( 'info for workout' , INFO )
 if 94 - 94: oO0o + oO0o + Ii1I . oO0o * Ii11Ii1I
 if 62 - 62: I11i / iI11I1II1I1I
 if 55 - 55: Ii11Ii1I / oO0o + o0oOO0O00o0O . OooO0OoOOOO
def i1ooO ( url ) :
 I1i11i = oO0OOoo0OO ( url )
 iiIii = re . compile ( 'cat-item-.+?"><a href="(.+?)" >(.+?)</a>' ) . findall ( I1i11i )
 for url , I1i1i1iii in iiIii :
  O0II11i11II ( I1i1i1iii , url , 9031 , ooOooo000oOO + 'icon.png' )
def i11iii1Ii1 ( url ) :
 I1i11i = oO0OOoo0OO ( url )
 iiIii = re . compile ( '<a href="(.+?)" title=".+?" rel="bookmark"><time class="entry-date published updated" datetime=".+?">(.+?)</time></a>' ) . findall ( I1i11i )
 for url , I1i1i1iii in iiIii :
  O0II11i11II ( I1i1i1iii , url , 9032 , ooOooo000oOO + 'icon.png' )
def o0oO0iiiiI1Iii ( url ) :
 I1i11i = oO0OOoo0OO ( url )
 iiIii = re . compile ( '#EXTINF:-.+?,(.+)\s*(.+)\s*' ) . findall ( I1i11i )
 for I1i1i1iii , url in iiIii :
  if '://' in I1i1i1iii :
   pass
   i1II1IiIII111 ( ( I1i1i1iii ) . replace ( '<br />' , '' ) , ( url ) . replace ( '<br />' , '' ) , 222 , ooOooo000oOO + 'icon.png' )
def I1I111IIIi1 ( url ) :
 I1i11i = oO0OOoo0OO ( url )
 iiIii = re . compile ( 'EXTINF:-.+?,(.+)</div></li><li class=".+?"><div class=".+?">(.+?)</div>).findall' ) . findall ( I1i11i )
 for I1i1i1iii , url in iiIii :
  i1II1IiIII111 ( I1i1i1iii , url , 222 , ooOooo000oOO + 'icon.png' )
  if 66 - 66: I11i % OOooOOo
  if 30 - 30: OOooOOo * I1ii11iIi11i % iI11I1II1I1I % oO0o + Ii
  if 46 - 46: oOo0O0Ooo . OooO0OoOOOO - Ii - IIIi
def oo0O0OO0Oo ( ) :
 I1i11i = oO0OOoo0OO ( 'http://www.disclose.tv/action/videolist/aliens/page/1/all/channel/1/category/1/' )
 iiIii = re . compile ( '<li><a href="([^"]*)">(.+?)</a></li>' ) . findall ( I1i11i )
 for OooOoOo , I1i1i1iii in iiIii :
  O0II11i11II ( I1i1i1iii , 'http://www.disclose.tv/' + OooOoOo , 7010 , ooOooo000oOO + 'disclose.png' )
  if 66 - 66: oOo0O0Ooo % Ii11Ii1I % IIiIiII11i
  if 77 - 77: IIIi + OoOo00o
def iI11Iii1I ( url ) :
 I1i11i = oO0OOoo0OO ( url )
 iiIii = re . compile ( 'href="([^"]*)"><img width="135" height="76" alt="([^"]*)".+?src="([^"]*)" />' , re . DOTALL ) . findall ( I1i11i )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' ) . findall ( I1i11i )
 for url , I1i1i1iii , I1i11 in iiIii :
  O0II11i11II ( I1i1i1iii , 'http://www.disclose.tv/' + url , 7011 , I1i11 )
 for url in next :
  O0II11i11II ( 'NEXT' , url , 7010 , ooOooo000oOO + 'Next.png' )
  if 62 - 62: OooO0OoOOOO . o0o00Oo0O . iI11I1II1I1I
  if 94 - 94: O0OoO % iI1iI1I1i1I % ooOoO0O00
def o0OoOo0o0O00 ( url ) :
 I1i11i = oO0OOoo0OO ( url )
 iiIii = re . compile ( 'url: "([^"]*)",' , re . DOTALL ) . findall ( I1i11i )
 ooo0O = re . compile ( "src='([^']*)' type='([^']*)' />" , re . DOTALL ) . findall ( I1i11i )
 for url in iiIii :
  if 'http' in url :
   i1II1IiIII111 ( 'video/flv' , url , 222 , ooOooo000oOO + 'disclose.png' )
 for url , I1i1i1iii in ooo0O :
  i1II1IiIII111 ( I1i1i1iii , url , 222 , ooOooo000oOO + 'disclose.png' )
  if 33 - 33: O0OoO + ii - oO0o / ooOoO0O00 / ii
  if 82 - 82: Ii1I / IIIii1II1II - o0oOO0O00o0O / I1ii11iIi11i * oO0o
def o00O ( url ) :
 I1i11i = oO0OOoo0OO ( url )
 iiIii = re . compile ( '<div id="play-1".+?src="(.+?)" scrolling="no".+?<li><a href="#play-1">(.+?)</a></li>' , re . DOTALL ) . findall ( I1i11i )
 for url , I1i1i1iii in iiIii :
  O0II11i11II ( I1i1i1iii , ( url + '&fv=&sou=' ) . replace ( 'player' , 'watch' ) , 7000 , ooOooo000oOO + 'icon.png' )
  if 50 - 50: OOooOOo - OoOo00o + iI11I1II1I1I - oO0o . I1ii11iIi11i
def iiiiIii11i1 ( name , url , img ) :
 o00OO00OoO = oO0OOoo0OO ( url )
 IiI11IIi1iI1i = re . compile ( '<iframe class="playerframe" src="(.+?)" scrolling=".+?" marginwidth=".+?" marginheight=".+?" vspace=".+?" hspace=".+?" allowfullscreen=".+?" webkitallowfullscreen=".+?" mozallowfullscreen=".+?" width=".+?" height=".+?" frameborder=".+?"></iframe>' , re . DOTALL ) . findall ( o00OO00OoO )
 iI1iI = len ( IiI11IIi1iI1i )
 if 74 - 74: OooO0OoOOOO - o0o00Oo0O / IIIi * Ii11Ii1I % O0OoO . IIIi
 if 60 - 60: Ii1I . IIiIiII11i * Ii . I11i
 if iI1iI == 1 :
  for o00oo in IiI11IIi1iI1i :
   o00oo = o00oo . replace ( 'player' , 'watch' )
   O000Oo00 = o00oo + '&fv=&sou='
   iI1oOoo = oO0OOoo0OO ( O000Oo00 )
   o00O0o00oo = re . compile ( '<source src="(.+?)" type=".+?">' , re . DOTALL ) . findall ( iI1oOoo )
   for Iiii1I in o00O0o00oo :
    iIiiII = False
    Resolve ( Iiii1I )
    if 13 - 13: IIiIiII11i
 elif iI1iI > 1 :
  if 55 - 55: I1ii11iIi11i % ooOoO0O00 * iI1iI1I1i1I
  for o00oo in IiI11IIi1iI1i :
   OOOo0 = oO0OOoo0OO ( o00oo )
   o0Oooo0o0oO0 = re . compile ( '<iframe width=".*?" height=".*?" frameborder=".*?" src="(.*?)" scrolling=".*?" marginwidth=".*?" marginheight=".*?" vspace=".*?" hspace=".*?" allowfullscreen=".*?" webkitallowfullscreen=".*?" mozallowfullscreen=".*?"></iframe>' , re . DOTALL ) . findall ( OOOo0 )
   IIIiIiiI1i = o0Oooo0o0oO0
   IIIiIiiI1i = ( str ( IIIiIiiI1i ) ) . replace ( '[\'' , '' ) . replace ( '\']' , '' ) ;
   print 'Stripped url : ' + IIIiIiiI1i
   i1II1IiIII111 ( 'DOUBLE LINK' , IIIiIiiI1i , 424 , '' )
   if 28 - 28: OooO0OoOOOO + Ii + ii / oO0o
   for url in o0Oooo0o0oO0 :
    O0II11i11II ( 'DOUBLE LINK' , url , 424 , '' )
    try :
     OOoOoOo = Google . resolve ( url )
    except :
     pass
    try :
     iIiI1111 = re . findall ( r"{'url': u'(.*?)', 'quality': 'HD'}, {'url': u'(.*?)', 'quality': 'SD'}" , str ( OOoOoOo ) )
     for O0OO00 , i1111I in iIiI1111 :
      if 58 - 58: ii - iI1iI1I1i1I + iI11I1II1I1I * Ii
      HD_URLS . append ( O0OO00 )
      SD_URLS . append ( i1111I )
    except :
     pass
 else :
  pass
  if 80 - 80: ooOoO0O00 . oOo0O0Ooo - OoOo00o + IIIii1II1II + o0oOO0O00o0O % OoOo00o
def IiiII ( ) :
 if 47 - 47: o0oOO0O00o0O + o0o00Oo0O / IIiIiII11i * oOo0O0Ooo - ii . Ii11Ii1I
 if 28 - 28: OoOo00o . OoOo00o . iI11I1II1I1I . IIIii1II1II . Ii1I * Ii
 O0II11i11II ( 'Genres' , 'http://cnfstudio.com/movies/' , 7002 , ooOooo000oOO + 'Movies.png' )
 if 72 - 72: iI1iI1I1i1I
 O0II11i11II ( 'Search Movies' , '' , 7017 , ooOooo000oOO + 'Movies.png' )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 26 - 26: OooO0OoOOOO % I1ii11iIi11i
 if 72 - 72: o0o00Oo0O + I11i + oOo0O0Ooo / I1ii11iIi11i
def o0oo0OOOO ( ) :
 I1i11i = oO0OOoo0OO ( 'http://cnfstudio.com/' )
 iiIii = re . compile ( '<a href="http://cnfstudio.com/genre/(.+?)">(.+?)</a>' ) . findall ( I1i11i )
 for OooOoOo , I1i1i1iii in iiIii :
  O0II11i11II ( I1i1i1iii , 'http://cnfstudio.com/genre/' + OooOoOo , 7003 , ooOooo000oOO + 'icon.png' )
  if 98 - 98: Ii . IIIi * OoOo00o . o0oOO0O00o0O
i1iiIIiiI111 = xbmcgui . Dialog ( )
if 52 - 52: Ii1I - ooOoO0O00 + Ii % I1ii11iIi11i % O0OoO
iiIIII11IiIII = '{UN},' ; Iii1I = '{IG},' ; Ii1 = '{PL},' ; oO0OOO = '{LO},' ; IiI1IIiiiii = '{LP},' ; II111iii = '{HA},' ; OooO00o000 = '{XD},' ; i1i11II1 = '{TA},' ; IIII1i = '{DP},' ; i111 = '{JT},' ; IIIIIII1i = '{JJ},' ; i1I1Iiii = '{MM},' ; I1iIIIiiii = '{FQ},' ; I1111 = '{HH},'
if 67 - 67: ooOoO0O00
def O0Oo0oo0O0O0o ( url ) :
 I1i11i = oO0OOoo0OO ( url )
 iiIii = re . compile ( '<div class="movie">.+?<img src="(.+?)" alt=".+?" />.+?<a href="(.+?)"><span class="player"></span></a>.+?<h2>(.+?)</h2>' , re . DOTALL ) . findall ( I1i11i )
 IIIi111iIi11 = re . compile ( "<link rel='next' href='(.+?)'/>" ) . findall ( I1i11i )
 for I1i11 , url , I1i1i1iii in iiIii :
  i1II1IiIII111 ( ( I1i1i1iii ) . replace ( '&#038;' , '' ) . replace ( '&#8216;' , '' ) . replace ( '&#8217;' , '' ) . replace ( '&#8211;' , '' ) , url , 7004 , I1i11 )
 IIIi111iIi11 = IIIi111iIi11
 for url in IIIi111iIi11 :
  O0II11i11II ( 'Next Page' , url , 7003 , ooOooo000oOO + 'Next.png' )
  if 33 - 33: OoOo00o / Ii11Ii1I - oOo0O0Ooo % IIIi
def Ii1I1iIiiI1 ( url ) :
 if 68 - 68: o0oOO0O00o0O . iI1iI1I1i1I
 I1i11i = oO0OOoo0OO ( url )
 iiIii = re . compile ( '<div id="play-1" class="player-content"><iframe class="playerframe" src="(.+?)" scrolling="no".+?</div>' , re . DOTALL ) . findall ( I1i11i )
 for url in iiIii :
  O000oo0O = url + '&fv=&sou='
  O000oo0O = O000oo0O . replace ( 'player' , 'watch' )
  i111iiIiiIiI = OOooooO ( O000oo0O )
  oOoo00 = OOooooO ( url )
  if 29 - 29: IIIii1II1II / OOooOOo . iI11I1II1I1I / iI1iI1I1i1I % OOooOOo % o0oOO0O00o0O
  if 49 - 49: IIiIiII11i / OooO0OoOOOO - Ii11Ii1I
def OOooooO ( url ) :
 if 7 - 7: oOo0O0Ooo / oO0o + IIIi + iI1iI1I1i1I / oOo0O0Ooo
 I1i11i = oO0OOoo0OO ( url )
 iiIii = re . compile ( '<video id=".+?<source src="(.+?)" type="video/mp4">' , re . DOTALL ) . findall ( I1i11i )
 for url in iiIii :
  o000ooooO0o ( url )
  if 82 - 82: Ii1I + ii
  if 21 - 21: OoOo00o * OoOo00o / iI1iI1I1i1I . o0oOO0O00o0O
def I1IIIIiiI1i1 ( ) :
 IIII ( '[COLORgreen]Local M3u[/COLOR]' , oOo0oooo00o , 2001 , ooOooo000oOO + 'loader.png' , i1iiIII111ii , '' )
 IIII ( '[COLORgreen]Remote M3u[/COLOR]' , Oo0o0000o0o0 , 1009 , ooOooo000oOO + 'loader.png' , i1iiIII111ii , '' )
 if 92 - 92: iI1iI1I1i1I / IIIi
def iiIIiii1iii1I ( url ) :
 iiIii = re . compile ( '^#EXTINF:-?[0-9]*(.*?),(.*?)\n(.*?)$' , re . I + re . M + re . U + re . S ) . findall
 for Iii11 , I1i1i1iii , url in iiIii :
  i1II1IiIII111 ( I1i1i1iii , url , 222 , ooOooo000oOO + 'streams.png' )
  if 42 - 42: o0oOO0O00o0O
  if 61 - 61: iI1iI1I1i1I
def ooo00OOOooO ( ) :
 o00OO00OoO = oO0OOoo0OO ( i1111 ( 'aHR0cHM6Ly9naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvdHJlZS9tYXN0ZXIvX3JlcG8vcGx1Z2luLnZpZGVvLkdlbmllVHY=' ) )
 iiIii = re . compile ( '<span class="css-truncate css-truncate-target"><a href="/GenieTv/Genie_Tv/blob/master/_repo/plugin.video.GenieTv/(.+?)" class="js-navigation-open" id=".+?" title=".+?">.+?</a></span>' ) . findall ( o00OO00OoO )
 for OooOoOo in iiIii :
  OooOoOo = i1111 ( 'aHR0cDovL3Jhdy5naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvbWFzdGVyL19yZXBvL3BsdWdpbi52aWRlby5HZW5pZVR2Lw==' ) + OooOoOo
 I1i1i1iii = 'plugin.video.GenieTv'
 if 80 - 80: oOo0O0Ooo - oOo0O0Ooo
 oooOO ( OooOoOo , I1i1i1iii )
 if 30 - 30: O0OoO
def ooOOO00Ooo ( ) :
 o00OO00OoO = oO0OOoo0OO ( i1111 ( 'aHR0cHM6Ly9naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvdHJlZS9tYXN0ZXIvX3JlcG8vcmVwb3NpdG9yeS5HZW5pZVR2' ) )
 iiIii = re . compile ( '<span class="css-truncate css-truncate-target"><a href="/GenieTv/Genie_Tv/blob/master/_repo/repository.GenieTv/(.+?)" class="js-navigation-open" id=".+?" title=".+?">.+?</a></span>' ) . findall ( o00OO00OoO )
 for OooOoOo in iiIii :
  OooOoOo = i1111 ( 'aHR0cDovL3Jhdy5naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvbWFzdGVyL19yZXBvL3JlcG9zaXRvcnkuR2VuaWVUdi8=' ) + OooOoOo
 I1i1i1iii = 'repository.GenieTv'
 if 57 - 57: I11i * Ii / OOooOOo
 oooOO ( OooOoOo , I1i1i1iii )
 if 40 - 40: iI11I1II1I1I - O0OoO / I1ii11iIi11i
 if 24 - 24: OoOo00o - o0oOO0O00o0O / O0OoO
def iIiiII1Ii1ii ( ) :
 IIII ( '[COLORgreen]CATAGORIES[/COLOR]' , '' , 10051 , ooOooo000oOO + 'loader.png' , i1iiIII111ii , '' )
 IIII ( '[COLORgreen]SEARCH[/COLOR]' , '' , 10052 , ooOooo000oOO + 'loader.png' , i1iiIII111ii , '' )
 if 34 - 34: oOo0O0Ooo
 if 57 - 57: IIIii1II1II . Ii11Ii1I % I11i
o0oO0 = xbmcaddon . Addon ( id = 'plugin.video.GenieTv' )
oOOoo00O0O = xbmcgui . Dialog ( )
oooOOOOO = xbmc . translatePath ( 'special://home/' )
Oo0oO0ooo = xbmcgui . DialogProgress ( )
I1I11 = 'https://addons.tvaddons.ag/'
if 9 - 9: IIIii1II1II
def I1i ( ) :
 iiIiIIIiiI = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 II11IiIi11 = iiIiIIIiiI . lower ( )
 I1i1iI = 'https://addons.tvaddons.ag/search/?keyword=' + II11IiIi11
 o00OO00OoO = oO0OOoo0OO ( I1i1iI )
 iiIii = re . compile ( '<li><a href="(.+?)"><span class=".+?"><img src="(.+?)" width=".+?" alt=".+?" class=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( o00OO00OoO )
 for OooOoOo , iiI , I1i1i1iii in iiIii :
  IIII ( I1i1i1iii , OooOoOo , 10054 , 'https://addons.tvaddons.ag/' + iiI , i1iiIII111ii , '' )
  if 44 - 44: oO0o . o0oOO0O00o0O / iI1iI1I1i1I + I1ii11iIi11i - oO0o / IIiIiII11i
  if 93 - 93: OoOo00o - IIIii1II1II + I11i . OoOo00o / iI1iI1I1i1I
def o0000oO ( ) :
 o00OO00OoO = oO0OOoo0OO ( I1I11 )
 iiIii = re . compile ( '<li><a href="(.+?)"><span class="thumbnail"><img src="(.+?)" class="pic" alt=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( o00OO00OoO )
 for OooOoOo , I1i11 , I1i1i1iii in iiIii :
  if 'Repositories' in I1i1i1iii :
   pass
  elif 'Services' in I1i1i1iii :
   pass
  elif 'International' in I1i1i1iii :
   pass
  else :
   IIII ( '[COLORgreen]' + I1i1i1iii + '[/COLOR]' , OooOoOo , 10053 , 'https://addons.tvaddons.ag/' + I1i11 , i1iiIII111ii , '' )
   if 83 - 83: oO0o
   if 16 - 16: O0OoO
def Addon ( url ) :
 o00OO00OoO = oO0OOoo0OO ( url )
 iIiiIiIIiI = re . compile ( '<li class="nextPage"><a class=".+?" href="(.+?)"><dfn title="next Page">.+?</dfn></a></li>' ) . findall ( o00OO00OoO )
 for url in iIiiIiIIiI :
  IIII ( '[COLORgreen]NEXT PAGE[/COLOR]' , 'https://addons.tvaddons.ag' + url , 10053 , ooOooo000oOO + 'Next.png' , i1iiIII111ii , '' )
 iiIii = re . compile ( '<li><a href="(.+?)"><span class=".+?"><img src="(.+?)" width=".+?" alt=".+?" class=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( o00OO00OoO )
 for url , I1i11 , I1i1i1iii in iiIii :
  if 'Please' in I1i1i1iii :
   pass
  else :
   IIII ( I1i1i1iii , url , 10054 , 'https://addons.tvaddons.ag/' + I1i11 , i1iiIII111ii , '' )
   if 93 - 93: OooO0OoOOOO % Ii1I
   if 31 - 31: IIiIiII11i + IIIii1II1II - ii . iI1iI1I1i1I
def i1IoOo000Oo00o ( url , name ) :
 o00OO00OoO = oO0OOoo0OO ( url )
 iiIii = re . compile ( '<a href="(.+?)"' ) . findall ( o00OO00OoO )
 for url in iiIii :
  if 'plugin' in url :
   print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<' + url
   oO0oo = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
   Oo0oO0ooo = xbmcgui . DialogProgress ( )
   Oo0oO0ooo . create ( "Origin+Jaybox" , "Downloading Content" , '' , 'Please Wait' )
   OO0o0o0oo0O = os . path . join ( oO0oo , name + '.zip' )
   try :
    os . remove ( OO0o0o0oo0O )
   except :
    pass
   downloader . download ( url , OO0o0o0oo0O , Oo0oO0ooo )
   ii1i = xbmc . translatePath ( os . path . join ( 'special://home' , 'addons' ) )
   time . sleep ( 2 )
   Oo0oO0ooo . update ( 0 , "" , "Extracting Zip Please Wait" )
   print '======================================='
   print ii1i
   print '======================================='
   extract . all ( OO0o0o0oo0O , ii1i , Oo0oO0ooo )
   oOo0O ( )
   if 81 - 81: ii
def oooOO ( url , name ) :
 oO0oo = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 Oo0oO0ooo = xbmcgui . DialogProgress ( )
 Oo0oO0ooo . create ( "Origin+Jaybox" , "Downloading Content" , '' , 'Please Wait' )
 OO0o0o0oo0O = os . path . join ( oO0oo , name + '.zip' )
 try :
  os . remove ( OO0o0o0oo0O )
 except :
  pass
 downloader . download ( url , OO0o0o0oo0O , Oo0oO0ooo )
 ii1i = xbmc . translatePath ( os . path . join ( 'special://home' , 'addons' ) )
 time . sleep ( 2 )
 Oo0oO0ooo . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print ii1i
 print '======================================='
 extract . all ( OO0o0o0oo0O , ii1i , Oo0oO0ooo )
 oOo0O ( )
 if 88 - 88: o0o00Oo0O * I11i
def oOo0O ( ) :
 xbmc . executebuiltin ( 'UpdateLocalAddons' )
 xbmc . executebuiltin ( 'UpdateAddonRepos' )
 i1iiIIiiI111 = xbmcgui . Dialog ( )
 i1iiIIiiI111 . ok ( "Origin + Genie TV" , '' , '                                 REFRESH SUCCESSFUL :)' , "                          [COLOR gold]Brought To You By Origin + Jaybox[/COLOR]" )
 return
 if 44 - 44: I11i / Ii1I . I1ii11iIi11i + OOooOOo
 if 32 - 32: OooO0OoOOOO - O0OoO * o0oOO0O00o0O * iI1iI1I1i1I
def O00OOOo ( ) :
 I1i11i = IiIi ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvc2NyYXBlZC9jYXRzLnBocA==' ) )
 iiIii = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( I1i11i )
 for OooOoOo , iiI , I1i1i1iii in iiIii :
  O0II11i11II ( I1i1i1iii , OooOoOo , 1007 , iiI )
def i1iI11Ii1i ( url ) :
 I1i11i = IiIi ( url )
 iiIii = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( I1i11i )
 for url , iiI , I1i1i1iii in iiIii :
  O0II11i11II ( '[COLORgreen]' + I1i1i1iii + '[/COLOR]' , url , 1006 , iiI )
  if 45 - 45: oOo0O0Ooo . I1ii11iIi11i . IIIi / OoOo00o
  if 4 - 4: Ii + IIIii1II1II
def I1111III111ii ( url , iconimage , name ) :
 from imports import cache
 cache = cache . get ( '' , 0 , url )
 I1i11i = IiIi ( url )
 iiIii = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( I1i11i )
 for url , iconimage , iIII , Iii , name in iiIii :
  if 'http' in url :
   if '.php' in url :
    IiIi1III ( name , url , 1016 , iconimage , Iii , iIII )
   else :
    if 'youtube' in url :
     I1iIIII1 ( name , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , iconimage , Iii , iIII )
    else :
     I1iIIII1 ( name , url , 222 , iconimage , Iii , iIII )
     o00oooO0Oo ( 'movies' , 'INFO' )
  else :
   o0oO0oOooO ( url , iconimage , name )
   if 99 - 99: Ii - o0oOO0O00o0O
 else :
  iiIii = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( I1i11i )
  for url , iiI , name in iiIii :
   if 'http' in url :
    if '.php' in url :
     O0II11i11II ( name , url , 1016 , iiI )
    else :
     if 'youtube' in url :
      print '>>>>>>>>>>>>>>>>>>>>>>> youtube old way'
      i1II1IiIII111 ( name , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , iiI )
     else :
      i1II1IiIII111 ( name , url , 222 , iiI )
      o00oooO0Oo ( 'movies' , 'INFO' )
   else :
    o0oO0oOooO ( url , iiI , name )
  xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 return cache
 if 85 - 85: IIIi % Ii1I
def o0oO0oOooO ( url , iconimage , name ) :
 iconimage = iconimage
 name = name
 url = url
 OO00o0O0oOooO = ( url ) . replace ( iiO0Oo0 , 'http' ) . replace ( IiiiIIi11II , '.com' ) ;
 IiiIII1IIii1 = ( OO00o0O0oOooO ) . replace ( oOOo0O , 'a' ) . replace ( OooO0O0Ooo , 'b' ) . replace ( oO0O , 'c' ) . replace ( iIIIOoO0000 , 'd' ) . replace ( Ii1 , 'e' ) . replace ( i111 , 'f' ) ;
 I11iIi1i1I1i1 = ( IiiIII1IIii1 ) . replace ( ooo0o0O , 'g' ) . replace ( II111iii , 'h' ) . replace ( o0oooOo0oo , 'i' ) . replace ( oo00i1i11I1I1 , 'j' ) . replace ( IIIiIi1iiI , 'k' ) . replace ( iI1o0 , 'l' ) ;
 iiiiii1ii1 = ( I11iIi1i1I1i1 ) . replace ( iIIII1i1 , 'm' ) . replace ( I1I1oO00o0oOoo , 'n' ) . replace ( oOOI1 , 'o' ) . replace ( OOI1i , 'p' ) . replace ( i1II1iII1 , 'q' ) . replace ( I11II11IiI11 , 'r' ) ;
 O00o = ( iiiiii1ii1 ) . replace ( Ii11Iiii1iiii , 's' ) . replace ( III11iIIi , 't' ) . replace ( i1IIII1111 , 'u' ) . replace ( Ooo0o0000OO , 'v' ) . replace ( iIiI1II1I1 , 'w' ) . replace ( OooiIiI1i1Ii , 'x' ) ;
 Oo0o00o = ( O00o ) . replace ( III1I1 , 'y' ) . replace ( iI1IIIIII , 'z' ) . replace ( iiIIII11IiIII , '.' ) . replace ( Iii1I , '(' ) . replace ( oO0OOO , ')' ) . replace ( IiI1IIiiiii , '/' ) ;
 OO0oO0Oo = ( Oo0o00o ) . replace ( Oo0Oo , '1' ) . replace ( iIIi , '2' ) . replace ( OoooOO0 , '3' ) . replace ( i1i11II1 , '4' ) . replace ( IIII1i , '5' ) . replace ( i1iI1IIi1I , '6' ) ;
 oo0OoO = ( OO0oO0Oo ) . replace ( IIIIIII1i , '7' ) . replace ( i1I1Iiii , '8' ) . replace ( I1iIIIiiii , '9' ) . replace ( I1111 , '0' ) . replace ( o0oO0o00O , ':' ) . replace ( iiii1 , '%' ) ;
 url = ( oo0OoO ) . replace ( oO00OOOOOO0o , '-' ) . replace ( OooO00o000 , '_' ) ;
 i1II1IiIII111 ( name , url , 222 , iconimage ) ;
 if 2 - 2: Ii1I - I1ii11iIi11i
 if 4 - 4: o0o00Oo0O / iI1iI1I1i1I . oO0o - O0OoO / IIIii1II1II
def I1IIiIi1I1I1 ( ) :
 I1i11i = IiIi ( i1111 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vdm9kL3VybHMvdXJsLnBocA==' ) )
 iiIii = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( I1i11i )
 for OooOoOo , iiI , I1i1i1iii in iiIii :
  O0II11i11II ( I1i1i1iii , OooOoOo , 1007 , iiI )
def IIi1iI11Ii ( url ) :
 I1i11i = IiIi ( url )
 iiIii = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( I1i11i )
 for url , iiI , I1i1i1iii in iiIii :
  O0II11i11II ( '[COLORgreen]' + I1i1i1iii + '[/COLOR]' , url , 1006 , iiI )
  if 20 - 20: I11i / OooO0OoOOOO
def II1I11 ( name , url , iconimage = None ) :
 print '--- Playing "{0}". {1}' . format ( name , url )
 I11iIiIii = xbmcgui . ListItem ( path = url , thumbnailImage = iconimage )
 I11iIiIii . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , I11iIiIii )
 if 60 - 60: ooOoO0O00 / oOo0O0Ooo . IIiIiII11i . o0oOO0O00o0O % OoOo00o - oOo0O0Ooo
 if 39 - 39: oOo0O0Ooo . oO0o + iI1iI1I1i1I + IIIii1II1II / IIiIiII11i % Ii
def OOOo0Ooo0 ( url ) :
 I1i11i = IiIi ( url )
 iiIii = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( I1i11i )
 for url , I1i11 , I1i1i1iii in iiIii :
  O0II11i11II ( '[COLORgreen]' + I1i1i1iii + '[/COLOR]' , url , 1006 , I1i11 )
def III1 ( url ) :
 I1i11i = IiIi ( url )
 i1i = url
 iiIii = re . compile ( "<a href='(.+?)'>(.+?)</a>" ) . findall ( I1i11i )
 for url , I1i1i1iii in iiIii :
  if '.mp3' in I1i1i1iii :
   print '<<<<<<<<<<<<<<<<<<<' + url + '>>>>>>>>>>>>>>>>>>>>>>>>>>>'
   i1II1IiIII111 ( ( I1i1i1iii ) . replace ( '.mp3' , '' ) . replace ( '/' , '' ) , 'http://hypem.com' + url , 222 , ooOooo000oOO + 'music.png' )
  else :
   O0II11i11II ( ( I1i1i1iii ) . replace ( '/' , '' ) , i1i + url , 1011 , ooOooo000oOO + 'music.png' )
def IIi1iI1i ( ) :
 I1i11i = IiIi ( i1111 ( 'aHR0cDovL3d3dy5jeW4ubmV0L211c2ljLw==' ) )
 iiIii = re . compile ( '<td><a href="(.+?)"><img src="(.+?)"><br>(.+?)</a></td>' , re . DOTALL ) . findall ( I1i11i )
 for OooOoOo , I1i11 , I1i1i1iii in iiIii :
  O0II11i11II ( I1i1i1iii , ( 'http://www.cyn.net/music/' + OooOoOo ) . replace ( ' ' , '%20' ) , 1031 , ( 'http://www.cyn.net/music/' + I1i11 ) . replace ( ' ' , '%20' ) )
def Iii11II1 ( url , img ) :
 I1i11i = IiIi ( url )
 OOoOoOo = url
 img = img
 iiIii = re . compile ( '<a href="(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( I1i11i )
 for url , I1i1i1iii in iiIii :
  i1II1IiIII111 ( ( I1i1i1iii ) . replace ( '.mp3' , '' ) , ( OOoOoOo + '/' + url ) . replace ( ' ' , '%20' ) , 222 , img )
  if 42 - 42: I1ii11iIi11i / OooO0OoOOOO . Ii11Ii1I * oOo0O0Ooo
  if 54 - 54: OOooOOo * o0oOO0O00o0O + oO0o
def oOOOo ( ) :
 i1111iI1 = ( i1111 ( 'aHR0cDovL2h5cGVtLmNvbS9kb3dubG9hZC8=' ) )
 iiIiIIIiiI = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 II11IiIi11 = iiIiIIIiiI . lower ( )
 OooOoOo = ( i1111 ( 'aHR0cDovL3Bhbmljc3RyZWFtLm5ldC9zdHJlYW1zLw==' ) )
 OOoOoOo = ( i1111 ( 'aHR0cDovL21hc2xvdmQubm8taXAub3JnL3B1YmxpYy9tcDMv' ) )
 iI1i11 = ( i1111 ( 'aHR0cDovL3d3dy5jeW4ubmV0L211c2ljLw==' ) )
 if 91 - 91: O0OoO - OoOo00o + OoOo00o
 o00OO00OoO = O000OO0 ( OooOoOo )
 OOOO0OOoO0O0 = O000OO0 ( OOoOoOo )
 O0Oo000ooO00 = O000OO0 ( iI1i11 )
 if 14 - 14: Ii1I * IIIi % ooOoO0O00 / Ii1I
 if o00OO00OoO != 'Failed' :
  iiIii = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( o00OO00OoO )
  for I1i1i1iii in iiIii :
   if iiIiIIIiiI in I1i1i1iii . lower ( ) :
    O0II11i11II ( ( I1i1i1iii + ' source 1' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( OooOoOo + I1i1i1iii ) . replace ( ' ' , '%20' ) , 1006 , '' )
    if 48 - 48: I1ii11iIi11i
    o00oooO0Oo ( 'tvshows' , 'Media Info 3' )
 if OOOO0OOoO0O0 != 'Failed' :
  ooo0O = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( o00OO00OoO )
  for I1i1i1iii in ooo0O :
   if iiIiIIIiiI in I1i1i1iii . lower ( ) :
    O0II11i11II ( ( I1i1i1iii + ' source 2' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( OOoOoOo + I1i1i1iii ) . replace ( ' ' , '%20' ) , 1006 , '' )
    if 75 - 75: Ii1I - OooO0OoOOOO * I1ii11iIi11i . ii * IIIi * oOo0O0Ooo
    o00oooO0Oo ( 'tvshows' , 'Media Info 3' )
 if O0Oo000ooO00 != 'Failed' :
  i111iiIIII = re . compile ( '<td><a href=".+?"><img src=".+?"><br>(.+?)</a></td>' , re . DOTALL ) . findall ( O0Oo000ooO00 )
  for I1i1i1iii in i111iiIIII :
   if iiIiIIIiiI in I1i1i1iii . lower ( ) :
    O0II11i11II ( ( I1i1i1iii + ' source 3' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( iI1i11 + I1i1i1iii ) . replace ( ' ' , '%20' ) , 1031 , '' )
    if 30 - 30: OOooOOo / OoOo00o / Ii11Ii1I * I11i * OoOo00o . oOo0O0Ooo
    o00oooO0Oo ( 'tvshows' , 'Media Info 3' )
    if 93 - 93: OOooOOo
    if 97 - 97: Ii
    if 68 - 68: OooO0OoOOOO * oO0o . iI1iI1I1i1I / Ii11Ii1I . I11i - Ii
    if 49 - 49: I1ii11iIi11i / Ii11Ii1I % iI1iI1I1i1I + OoOo00o - oO0o
    if 13 - 13: IIiIiII11i
    if 83 - 83: ii . oOo0O0Ooo + Ii11Ii1I * o0o00Oo0O / OoOo00o
iIIII1i1 = '{SF},' ; I1I1oO00o0oOoo = '{IF},' ; oOOI1 = '{PW},' ; OoooOO0 = '{AM},' ; OOI1i = '{GF},' ; i1II1iII1 = '{DD},' ; I11II11IiI11 = '{UO},' ; Ii11Iiii1iiii = '{LE},' ; i1IIII1111 = '{ZY},' ; Ooo0o0000OO = '{UE},' ; iIiI1II1I1 = '{PE},' ; OooiIiI1i1Ii = '{JE},' ; III1I1 = '{TH},' ; iI1IIIIII = '{LK},'
if 8 - 8: ooOoO0O00 + IIiIiII11i / Ii11Ii1I + Ii1I % Ii11Ii1I - iI11I1II1I1I
if 29 - 29: I1ii11iIi11i + IIiIiII11i
def oOOo00ooO ( ) :
 I1i11i = oO0OOoo0OO ( 'http://www.iwatchseries.me/tv-list/' )
 iiIii = re . compile ( '<h5><a href="([^"]*)"><strong>(.+?)</strong></a></h5>' ) . findall ( I1i11i )
 for OooOoOo , I1i1i1iii in iiIii :
  O0II11i11II ( I1i1i1iii , OooOoOo , 8021 , ooOooo000oOO + 'iwatch.png' )
def ooOo ( url ) :
 I1i11i = oO0OOoo0OO ( url )
 iiIii = re . compile ( '<h5><strong><a href="([^"]*)">(.+?)</a>(.+?)</strong></h5>' ) . findall ( I1i11i )
 for url , I1i1i1iii , oOoooo000Oo00 in iiIii :
  O0II11i11II ( I1i1i1iii + oOoooo000Oo00 , url , 8022 , ooOooo000oOO + 'iwatch.png' )
def OOOoOo0oO0OoO ( url ) :
 I1i11i = oO0OOoo0OO ( url )
 iiIii = re . compile ( '<iframe src="([^"]*)"' ) . findall ( I1i11i )
 for url in iiIii :
  print '>>>>>>>>>>>>>>>>>>>>' + url
  I1 ( url )
def I1 ( url ) :
 I1i11i = oO0OOoo0OO ( url )
 iiIii = re . compile ( '{.+?"file" : "(.+?)",.+?"default" : true.+?"label" : "(.+?)"' , re . DOTALL ) . findall ( I1i11i )
 ooo0O = re . compile ( 'setup\(\{.+?file: "(.+?)",.+?skin' , re . DOTALL ) . findall ( I1i11i )
 i111iiIIII = re . compile ( "{ label: '([^']*)', file:.+?'([^']*)' }" ) . findall ( I1i11i )
 for url , I1i1i1iii in iiIii :
  i1II1IiIII111 ( 'VidSpot - ' + I1i1i1iii , url , 222 , ooOooo000oOO + 'iwatch.png' )
 for url in ooo0O :
  i1II1IiIII111 ( 'VodLocker' , url , 222 , ooOooo000oOO + 'iwatch.png' )
 for I1i1i1iii , url in i111iiIIII :
  print '<><><><><><><><><><><> before   ' + url
  if 'hevideo' in url :
   print '>>>>>>>>>>>>>>>>>>>>>>>>>' + url
   i1II1IiIII111 ( 'TheVideo - ' + I1i1i1iii , url , 222 , ooOooo000oOO + 'iwatch.png' )
   if 35 - 35: IIiIiII11i / Ii11Ii1I
def OO0000 ( ) :
 I1i11i = cloudflare . source ( 'http://www.animeland.me/anime-list' )
 iiIii = re . compile ( 'letter-spacing:-1px;" href="([^"]*)">(.+?)</a></li>' ) . findall ( I1i11i )
 for OooOoOo , I1i1i1iii in iiIii :
  O0II11i11II ( I1i1i1iii , OooOoOo , 1021 , ooOooo000oOO + 'anime.png' )
  if 79 - 79: ooOoO0O00 / I1ii11iIi11i - oOo0O0Ooo . o0o00Oo0O
  if 56 - 56: OooO0OoOOOO % o0o00Oo0O * ooOoO0O00 - IIiIiII11i
def Oo0OoOOoo ( ) :
 I1i11i = oO0OOoo0OO ( 'http://www.animetoon.org/cartoon' )
 iiIii = re . compile ( '<td><a href="(.+?)">(.+)</a></td>' ) . findall ( I1i11i )
 for OooOoOo , I1i1i1iii in iiIii :
  O0II11i11II ( I1i1i1iii , OooOoOo , 1002 , ooOooo000oOO + 'anime.png' )
  if 84 - 84: IIIi
  if 53 - 53: ooOoO0O00
  if 59 - 59: I11i + oOo0O0Ooo % ii - iI11I1II1I1I
def iiIII1i1 ( url ) :
 I1i11i = oO0OOoo0OO ( url )
 ooo0O = re . compile ( '<img src="(.+?)" id="series_image" width="250" height="370" alt=".+?" />' ) . findall ( I1i11i )
 for I1i11 in ooo0O :
  iI1i = I1i11
 i111iiIIII = re . compile ( '<li><a href="(.+?)">Next</a></li>' ) . findall ( I1i11i )
 for url in i111iiIIII :
  O0II11i11II ( 'NEXT PAGE' , url , 1002 , ooOooo000oOO + 'Next.png' )
 iiIii = re . compile ( '&nbsp;<a href="(.+?)">(.+?)</a>' ) . findall ( I1i11i )
 for url , I1i1i1iii in iiIii :
  O0II11i11II ( I1i1i1iii , url , 1003 , iI1i )
 xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
def oOOo0OOoOO0 ( url , IMAGE ) :
 I1i11i = oO0OOoo0OO ( url )
 iiIii = re . compile ( '"playlist">(.+?)</span></div><div><iframe src="(.+?)"' ) . findall ( I1i11i )
 for I1i1i1iii , url in iiIii :
  print I1i1i1iii + '     ' + url
  if 'easy' in url :
   IiIiIIi1IiiIi1III ( url )
  elif 'playpanda' in url :
   IiIiIIi1IiiIi1III ( url )
   if 19 - 19: ooOoO0O00 % oOo0O0Ooo - iI11I1II1I1I - OoOo00o / Ii1I
  xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
def IiIiIIi1IiiIi1III ( url ) :
 I1i11i = oO0OOoo0OO ( url )
 iiIii = re . compile ( "url: '(.+?)'," ) . findall ( I1i11i )
 for url in iiIii :
  i1II1IiIII111 ( 'STREAM' , url , 222 , ooOooo000oOO + 'anime.png' )
  if 16 - 16: Ii11Ii1I
  if 79 - 79: ii - O0OoO * Ii11Ii1I - IIiIiII11i % OOooOOo * OooO0OoOOOO
def iI1III ( url ) :
 I11iii1Ii = urllib2 . Request ( url )
 I11iii1Ii . add_header ( 'User-Agent' , "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0" )
 I11iii1Ii . add_header ( 'referer' , url )
 I1IIiiIiii = urllib2 . urlopen ( I11iii1Ii )
 O000oo0O = I1IIiiIiii . read ( )
 I1IIiiIiii . close ( )
 return O000oo0O
 if 42 - 42: O0OoO + o0oOO0O00o0O + Ii11Ii1I * iI1iI1I1i1I . ooOoO0O00
def IiIi ( url ) :
 I11iii1Ii = urllib2 . Request ( url )
 I11iii1Ii . add_header ( 'User-Agent' , "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0" )
 I1IIiiIiii = urllib2 . urlopen ( I11iii1Ii )
 O000oo0O = I1IIiiIiii . read ( )
 I1IIiiIiii . close ( )
 return O000oo0O
 if 72 - 72: oOo0O0Ooo + Ii11Ii1I
def IiI1iI1I1 ( url ) :
 xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
 iiII1IiIi1iI1 = ( '%s%s' % ( oOiiI1Ii11II1I , url ) )
 O000oo0O = IiIi ( url )
 iiIii = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( O000oo0O )
 for url , iiI , I1i1i1iii in iiIii :
  i1II1IiIII111 ( '%s' % ( I1i1i1iii ) . replace ( 'GenieTv' , '[COLOR green]GenieTV[/COLOR]' ) . replace ( '.' , ' ' ) . replace ( 'mp4' , '' ) . replace ( 'mkv' , '' ) . replace ( '_' , ' ' ) , '%s' % ( url ) , 222 , iiI )
  if 5 - 5: IIIi % IIiIiII11i + I1ii11iIi11i - iI11I1II1I1I
def o000ooooO0o ( url ) :
 oO00oOOo0Oo = xbmc . Player ( Ii11iI ( ) )
 import urlresolver
 try : oO00oOOo0Oo . play ( url )
 except : pass
 from urlresolver import common
 Oo0oO0ooo = xbmcgui . DialogProgress ( )
 Oo0oO0ooo . create ( 'LOADING' , 'Opening %s Now' % ( I1i1i1iii ) )
 oO00oOOo0Oo = xbmc . Player ( Ii11iI ( ) )
 url = urlresolver . HostedMediaFile ( url ) . resolve ( )
 if Oo0oO0ooo . iscanceled ( ) :
  print "[COLORred]STREAM CANCELLED[/COLOR]"
  i1iiIIiiI111 = xbmcgui . Dialog ( )
  if i1iiIIiiI111 . yesno ( "[B]CANCELLED[/B]" , '[B]Was There A Problem[/B]' , '' , "" , 'Yes' , 'No' ) :
   i1iiIIiiI111 . ok ( "Message Send" , "Your Message Has Been Sent" )
  else :
   return
 else :
  try : oO00oOOo0Oo . play ( url )
  except : pass
  try : o0oO0 . resolve_url ( url )
  except : pass
  Oo0oO0ooo . close ( )
  if 64 - 64: IIIi + iI11I1II1I1I
def I1Iii ( url ) :
 Oo0oO0ooo = xbmcgui . DialogProgress ( )
 Oo0oO0ooo . create ( 'Featching Your Video' , 'Featching Your Video' )
 Oo0oO0ooo . update ( 0 , '%s' % I1i1i1iii )
 xbmc . sleep ( 1 )
 oO00oOOo0Oo = xbmc . Player ( Ii11iI ( ) )
 Oo0oO0ooo . update ( 100 , '%s' % I1i1i1iii )
 xbmc . sleep ( 1 )
 oO00oOOo0Oo . play ( url ) . strip ( )
 Oo0oO0ooo . close ( )
 if 30 - 30: ooOoO0O00 . Ii1I
def o0oOOo0O0O000 ( url ) :
 oO00oOOo0Oo = xbmc . Player ( Ii11iI ( ) )
 import urlresolver
 url = ( url ) . strip ( )
 try : oO00oOOo0Oo . play ( url ) . strip ( )
 except : pass
 if 77 - 77: IIiIiII11i - Ii
 if 78 - 78: Ii11Ii1I
def Ii11iI ( ) :
 try :
  o0O0oOOo00o0 = getSet ( "core-player" )
  if ( o0O0oOOo00o0 == 'DVDPLAYER' ) : iIIiI1 = xbmc . PLAYER_CORE_DVDPLAYER
  elif ( o0O0oOOo00o0 == 'MPLAYER' ) : iIIiI1 = xbmc . PLAYER_CORE_MPLAYER
  elif ( o0O0oOOo00o0 == 'PAPLAYER' ) : iIIiI1 = xbmc . PLAYER_CORE_PAPLAYER
  else : iIIiI1 = xbmc . PLAYER_CORE_AUTO
 except : iIIiI1 = xbmc . PLAYER_CORE_AUTO
 return iIIiI1
 return True
 if 52 - 52: oO0o
def O0II11i11II ( name , url , mode , iconimage , showcontext = True , allinfo = { } ) :
 I1iIII1IiiI = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 OOoooOoO0Oo = True
 Oo000 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 Oo000 . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 if showcontext :
  I1III1I11I1 = [ ]
  if showcontext == 'fav' :
   I1III1I11I1 . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in OOO00 :
   I1III1I11I1 . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  Oo000 . addContextMenuItems ( I1III1I11I1 )
 OOoooOoO0Oo = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = I1iIII1IiiI , listitem = Oo000 , isFolder = True )
 return OOoooOoO0Oo
 if 85 - 85: IIIi
def IiIIi1I1I11Ii ( name , url , mode , iconimage , fanart , description ) :
 if 62 - 62: Ii11Ii1I % IIiIiII11i + OooO0OoOOOO + IIIii1II1II % OoOo00o . oOo0O0Ooo
 I1iIII1IiiI = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 OOoooOoO0Oo = True
 Oo000 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 Oo000 . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 Oo000 . setProperty ( "Fanart_Image" , fanart )
 OOoooOoO0Oo = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = I1iIII1IiiI , listitem = Oo000 , isFolder = True )
 return OOoooOoO0Oo
 if 53 - 53: oO0o % Ii1I . o0oOO0O00o0O . ooOoO0O00 . oO0o
def i1II1IiIII111 ( name , url , mode , iconimage , showcontext = True , allinfo = { } ) :
 I1iIII1IiiI = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 OOoooOoO0Oo = True
 Oo000 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 Oo000 . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 if showcontext :
  I1III1I11I1 = [ ]
  if showcontext == 'fav' :
   I1III1I11I1 . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in OOO00 :
   I1III1I11I1 . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  Oo000 . addContextMenuItems ( I1III1I11I1 )
 OOoooOoO0Oo = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = I1iIII1IiiI , listitem = Oo000 , isFolder = False )
 return OOoooOoO0Oo
 if 26 - 26: oOo0O0Ooo % OOooOOo
 if 67 - 67: I1ii11iIi11i - OooO0OoOOOO * Ii11Ii1I . ii / Ii
 if 61 - 61: I11i % oOo0O0Ooo * ooOoO0O00 / oOo0O0Ooo / IIiIiII11i + IIIi
 if 22 - 22: OooO0OoOOOO . o0oOO0O00o0O + I1ii11iIi11i
 if 45 - 45: I1ii11iIi11i % I1ii11iIi11i + I1ii11iIi11i / o0o00Oo0O % ii
 if 92 - 92: Ii11Ii1I . OOooOOo . iI1iI1I1i1I - ii / O0OoO
def o00o0 ( heading , announce ) :
 class ooOo0 ( ) :
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
   try : ooo0OiII1iii = open ( announce ) ; I11I1i = ooo0OiII1iii . read ( )
   except : I11I1i = announce
   self . win . getControl ( self . CONTROL_TEXTBOX ) . setText ( str ( I11I1i ) )
   return
 ooOo0 ( )
 ooOo0 ( )
 if 100 - 100: OoOo00o
def iiIiiiIii11i1 ( ) :
 o00o0 ( 'These are the main Sources you should get into you XBMC' , '[COLORwhite]http://architects.x10host.com[/COLOR]--- [CR]  [COLORred]http://repo.sharktech.co.uk[/COLOR]--- [CR]   [COLORwhite]http://fusion.tvaddons.ag[/COLOR]--- [CR]  [COLORred]http://i.totalxbmc.tv[/COLOR]--- [CR]   [COLORwhite]http://www.xunitytalk.com/xfinity[/COLOR]--- [CR]  [COLORred]http://srp.nu[/COLOR]--- [CR]   [COLORwhite]http://solved.no-issue.ca[/COLOR]--- [CR]  [COLORred]http://xbmc.aminhacasadigital.com[/COLOR]--- [CR]   [COLORwhite]http://xbmc.movieshd.co[/COLOR]--- [CR]  [COLORred]http://install.kaosbox.tv[/COLOR]--- [CR]   [COLORwhite]http://kodi-repo.com/mxr[/COLOR]--- [CR]  [COLORred]http://kodi.metalkettle.co[/COLOR]--- [CR]   [COLORwhite]http://prozone.getxbmc.com[/COLOR]--- [CR]  [COLORred]http://transform.mega-tron.tv[/COLOR]--- [CR]   [COLORwhite]http://muckys.kodimediaportal.ml[/COLOR]--- [CR]  [COLORred]http://jas0npc.pcriot.com[/COLOR]--- [CR]  [COLORwhite]Sports devil source[/COLOR]--- [CR]  [COLORred]http://iwillfolo.com/iwf[/COLOR]' )
 if 87 - 87: oO0o + ii . O0OoO * iI1iI1I1i1I
 if 82 - 82: iI11I1II1I1I * ii
 if 50 - 50: IIIi - IIiIiII11i
 if 33 - 33: OooO0OoOOOO / OooO0OoOOOO . Ii * Ii1I + I11i
 if 16 - 16: OooO0OoOOOO
def oOo0O ( ) :
 xbmc . executebuiltin ( 'UpdateLocalAddons' )
 xbmc . executebuiltin ( 'UpdateAddonRepos' )
 i1iiIIiiI111 = xbmcgui . Dialog ( )
 i1iiIIiiI111 . ok ( "GenieTv" , '' , '                                 REFRESH SUCCESSFUL :)' , "                          [COLOR gold]Brought To You By Kodi Support Group, GenieTv[/COLOR]" )
 return
 if 10 - 10: OOooOOo . OooO0OoOOOO * iI11I1II1I1I - OoOo00o - OOooOOo / IIIi
 if 13 - 13: OoOo00o + OOooOOo % OooO0OoOOOO % ii
 if 22 - 22: IIIi
 if 23 - 23: o0o00Oo0O
 if 41 - 41: ooOoO0O00 . IIIii1II1II / O0OoO / I11i % OooO0OoOOOO - Ii11Ii1I
 if 14 - 14: Ii1I - Ii * IIIi
 if 39 - 39: ii
 if 19 - 19: Ii
 if 80 - 80: oOo0O0Ooo
 if 58 - 58: OoOo00o + Ii1I % OOooOOo
 if 22 - 22: iI11I1II1I1I - Ii11Ii1I / oOo0O0Ooo * OooO0OoOOOO
 if 26 - 26: I11i + IIIii1II1II - I11i + I1ii11iIi11i . OoOo00o
 if 97 - 97: ooOoO0O00
 if 46 - 46: Ii1I
 if 30 - 30: oO0o / o0o00Oo0O * I11i * IIIi + ii * o0oOO0O00o0O
 if 23 - 23: iI1iI1I1i1I
 if 36 - 36: OooO0OoOOOO . o0oOO0O00o0O - ooOoO0O00 + IIIi
 if 54 - 54: ii . OoOo00o - o0oOO0O00o0O
 if 76 - 76: IIIi
 if 61 - 61: O0OoO / IIiIiII11i * O0OoO * OOooOOo * IIIi . Ii
 if 26 - 26: IIIi / O0OoO - oO0o . iI11I1II1I1I
 if 83 - 83: O0OoO % Ii11Ii1I / I1ii11iIi11i - o0oOO0O00o0O / o0o00Oo0O
 if 97 - 97: iI11I1II1I1I * iI1iI1I1i1I
 if 95 - 95: oO0o
def OoiIIii1Ii1 ( url ) :
 O000oo0O = oO0OOoo0OO ( str ( Ii1iIiII1ii1 ) + o0O0o ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iiIii = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( O000oo0O )
 for I1i1i1iii , url , OOOOO0O00 , Iii , iIIIII1I in iiIii :
  IIII ( I1i1i1iii , url , 42 , OOOOO0O00 , Iii , iIIIII1I )
 o00oooO0Oo ( 'movies' , 'MAIN' )
 if 47 - 47: IIIii1II1II * Ii11Ii1I % iI11I1II1I1I / O0OoO
def O0O00O ( url ) :
 O000oo0O = oO0OOoo0OO ( str ( Ii1iIiII1ii1 ) + O0ooO ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iiIii = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( O000oo0O )
 for I1i1i1iii , url , OOOOO0O00 , Iii , iIIIII1I in iiIii :
  IIII ( I1i1i1iii , url , 42 , OOOOO0O00 , Iii , iIIIII1I )
 o00oooO0Oo ( 'movies' , 'MAIN' )
 if 42 - 42: o0o00Oo0O * o0oOO0O00o0O . OOooOOo / IIIii1II1II - Ii11Ii1I . iI1iI1I1i1I
def OO0OOO ( url ) :
 O000oo0O = oO0OOoo0OO ( str ( Ii1iIiII1ii1 ) + Oo0O00OO ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iiIii = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( O000oo0O )
 for I1i1i1iii , url , OOOOO0O00 , Iii , iIIIII1I in iiIii :
  IIII ( I1i1i1iii , url , 42 , OOOOO0O00 , Iii , iIIIII1I )
 o00oooO0Oo ( 'movies' , 'MAIN' )
 if 75 - 75: OooO0OoOOOO % I11i - IIIi
def O0oOo0o0000 ( url ) :
 O000oo0O = oO0OOoo0OO ( str ( Ii1iIiII1ii1 ) + I1iIiI ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iiIii = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( O000oo0O )
 for I1i1i1iii , url , OOOOO0O00 , Iii , iIIIII1I in iiIii :
  IIII ( I1i1i1iii , url , 42 , OOOOO0O00 , Iii , iIIIII1I )
 o00oooO0Oo ( 'movies' , 'MAIN' )
 if 100 - 100: ooOoO0O00 % Ii11Ii1I
def oO000O ( url ) :
 O000oo0O = oO0OOoo0OO ( str ( Ii1iIiII1ii1 ) + Oo0o0OoOoOo0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iiIii = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( O000oo0O )
 for I1i1i1iii , url , OOOOO0O00 , Iii , iIIIII1I in iiIii :
  IIII ( I1i1i1iii , url , 42 , OOOOO0O00 , Iii , iIIIII1I )
 o00oooO0Oo ( 'movies' , 'MAIN' )
 if 36 - 36: Ii11Ii1I * oOo0O0Ooo * Ii1I . iI1iI1I1i1I * Ii1I
def O0ooO0 ( url ) :
 O000oo0O = oO0OOoo0OO ( str ( Ii1iIiII1ii1 ) + iII1i111iI ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iiIii = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( O000oo0O )
 for I1i1i1iii , url , OOOOO0O00 , Iii , iIIIII1I in iiIii :
  IIII ( I1i1i1iii , url , 42 , OOOOO0O00 , Iii , iIIIII1I )
 o00oooO0Oo ( 'movies' , 'MAIN' )
 if 9 - 9: Ii + IIIii1II1II - OOooOOo / O0OoO % ooOoO0O00 / OoOo00o
def iiI1 ( url ) :
 O000oo0O = oO0OOoo0OO ( str ( Ii1iIiII1ii1 ) + II1II111 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iiIii = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( O000oo0O )
 for I1i1i1iii , url , OOOOO0O00 , Iii , iIIIII1I in iiIii :
  IIII ( I1i1i1iii , url , 42 , OOOOO0O00 , Iii , iIIIII1I )
 o00oooO0Oo ( 'movies' , 'MAIN' )
 if 71 - 71: IIiIiII11i % IIIi + oOo0O0Ooo * O0OoO + OooO0OoOOOO . O0OoO
def I11o0O00 ( url ) :
 O000oo0O = oO0OOoo0OO ( str ( Ii1iIiII1ii1 ) + OOOoOOO0oOOoO ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iiIii = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( O000oo0O )
 for I1i1i1iii , url , OOOOO0O00 , Iii , iIIIII1I in iiIii :
  IIII ( I1i1i1iii , url , 42 , OOOOO0O00 , Iii , iIIIII1I )
 o00oooO0Oo ( 'movies' , 'MAIN' )
 if 87 - 87: IIIii1II1II
def I111I111 ( url ) :
 O000oo0O = oO0OOoo0OO ( str ( Ii1iIiII1ii1 ) + i1iI11iI ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iiIii = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( O000oo0O )
 for I1i1i1iii , url , OOOOO0O00 , Iii , iIIIII1I in iiIii :
  IIII ( I1i1i1iii , url , 42 , OOOOO0O00 , Iii , iIIIII1I )
 o00oooO0Oo ( 'movies' , 'MAIN' )
 if 69 - 69: OoOo00o . iI1iI1I1i1I
def iII11iI1iiIIi ( url ) :
 O000oo0O = oO0OOoo0OO ( str ( Ii1iIiII1ii1 ) + I1II1iIi ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iiIii = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( O000oo0O )
 for I1i1i1iii , url , OOOOO0O00 , Iii , iIIIII1I in iiIii :
  IIII ( I1i1i1iii , url , 5 , OOOOO0O00 , Iii , iIIIII1I )
 o00oooO0Oo ( 'movies' , 'MAIN' )
 if 36 - 36: OOooOOo * oO0o / O0OoO / oOo0O0Ooo - Ii11Ii1I
 if 53 - 53: OoOo00o
 if 99 - 99: I1ii11iIi11i
 if 17 - 17: Ii - Ii + Ii1I * O0OoO * OoOo00o / ii
 if 22 - 22: IIIi * Ii1I - OooO0OoOOOO
 if 71 - 71: iI11I1II1I1I / Ii % I11i . IIIi * oOo0O0Ooo % IIiIiII11i
 if 35 - 35: IIIi - OOooOOo
 if 61 - 61: IIIi * I11i * oO0o + Ii1I . I1ii11iIi11i + ooOoO0O00
 if 82 - 82: I1ii11iIi11i + IIIi
def O00oOOoOOOOO ( ) :
 try :
  if os . path . exists ( iIii1 ) == True :
   i1iiIIiiI111 = xbmcgui . Dialog ( )
   if i1iiIIiiI111 . yesno ( "Delete Thumbnails" , "[COLOR gold][B]##########WARNING ANDROID ONLY##########[/B][/COLOR]" , "This feature deletes your thumbnail folder and textures13.db" , "Are you sure you want to do proceed? This Can NOT Be Undone" ) :
    for iI , i1iI11i1IIi , ii1IIi111 in os . walk ( iIii1 ) :
     ii1IIii = 0
     ii1IIii += len ( ii1IIi111 )
     if ii1IIii > 0 :
      for ooo0OiII1iii in ii1IIi111 :
       os . unlink ( os . path . join ( iI , ooo0OiII1iii ) )
  Ii1111Ii1 = os . path . join ( iI111I11I1I1 , "Textures13.db" )
  os . unlink ( Ii1111Ii1 )
  i1iiIIiiI111 . ok ( "Restart KODI" , "Please restart KODI to rebuild thumbnail library" )
 except :
  i1iiIIiiI111 = xbmcgui . Dialog ( )
  i1iiIIiiI111 . ok ( o0oOoO00o , "Error Deleting Thumbnails please visit Kodi Support Group, GenieTv on facebook" )
 return
 if 31 - 31: I11i * iI1iI1I1i1I - Ii - oOo0O0Ooo
 if 19 - 19: o0oOO0O00o0O . iI1iI1I1i1I * ii - IIIii1II1II + o0o00Oo0O * IIIi
 if 90 - 90: ooOoO0O00 . OoOo00o / IIIi . IIIii1II1II / IIIi
 if 1 - 1: o0oOO0O00o0O % O0OoO
 if 99 - 99: o0oOO0O00o0O + iI11I1II1I1I . IIIii1II1II / oO0o * Ii1I
 if 87 - 87: OooO0OoOOOO / IIiIiII11i % oO0o % oO0o
 if 28 - 28: OOooOOo % OoOo00o - IIIii1II1II + IIIii1II1II + OoOo00o / iI11I1II1I1I
 if 91 - 91: oOo0O0Ooo / IIiIiII11i * IIIii1II1II
 if 94 - 94: IIiIiII11i - iI11I1II1I1I - iI11I1II1I1I
def OOOo0Ooo0o00o ( url ) :
 print '############################################################       DELETING STANDARD CACHE             ###############################################################'
 oOo = os . path . join ( xbmc . translatePath ( 'special://home' ) , 'cache' )
 if os . path . exists ( oOo ) == True :
  for iI , i1iI11i1IIi , ii1IIi111 in os . walk ( oOo ) :
   ii1IIii = 0
   ii1IIii += len ( ii1IIi111 )
   if 94 - 94: ooOoO0O00 / Ii1I / oOo0O0Ooo * IIIi * I1ii11iIi11i
   if 21 - 21: ii + o0o00Oo0O / ii / IIIii1II1II
   if ii1IIii > 0 :
    if 44 - 44: ooOoO0O00 . Ii1I - O0OoO . IIIii1II1II . I11i + OoOo00o
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    if i1iiIIiiI111 . yesno ( "Delete KODI Cache Files" , str ( ii1IIii ) + " files found" , "Do you want to delete them?" ) :
     if 17 - 17: iI11I1II1I1I + ooOoO0O00 . Ii1I + Ii11Ii1I % ooOoO0O00 . OoOo00o
     for ooo0OiII1iii in ii1IIi111 :
      try :
       os . unlink ( os . path . join ( iI , ooo0OiII1iii ) )
      except :
       pass
     for OoOo00o0OO in i1iI11i1IIi :
      try :
       shutil . rmtree ( os . path . join ( iI , OoOo00o0OO ) )
      except :
       pass
       if 57 - 57: OoOo00o
   else :
    pass
 if xbmc . getCondVisibility ( 'system.platform.ATV2' ) :
  OoOO00OO0 = os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'Other' )
  if 46 - 46: I11i . iI11I1II1I1I + ii - O0OoO * I1ii11iIi11i * Ii
  for iI , i1iI11i1IIi , ii1IIi111 in os . walk ( OoOO00OO0 ) :
   ii1IIii = 0
   ii1IIii += len ( ii1IIi111 )
   if 81 - 81: OOooOOo
   if ii1IIii > 0 :
    if 72 - 72: oO0o / I1ii11iIi11i * oO0o * oO0o
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    if i1iiIIiiI111 . yesno ( "Delete ATV2 Cache Files" , str ( ii1IIii ) + " files found in 'Other'" , "Do you want to delete them?" ) :
     if 74 - 74: I1ii11iIi11i + I1ii11iIi11i / iI1iI1I1i1I
     for ooo0OiII1iii in ii1IIi111 :
      os . unlink ( os . path . join ( iI , ooo0OiII1iii ) )
     for OoOo00o0OO in i1iI11i1IIi :
      shutil . rmtree ( os . path . join ( iI , OoOo00o0OO ) )
      if 21 - 21: ii / OooO0OoOOOO
   else :
    pass
  OO0OOoooOo00 = os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'LocalAndRental' )
  if 63 - 63: ooOoO0O00
  for iI , i1iI11i1IIi , ii1IIi111 in os . walk ( OO0OOoooOo00 ) :
   ii1IIii = 0
   ii1IIii += len ( ii1IIi111 )
   if 56 - 56: I1ii11iIi11i
   if ii1IIii > 0 :
    if 52 - 52: IIIii1II1II + I1ii11iIi11i
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    if i1iiIIiiI111 . yesno ( "Delete ATV2 Cache Files" , str ( ii1IIii ) + " files found in 'LocalAndRental'" , "Do you want to delete them?" ) :
     if 67 - 67: Ii1I % ii
     for ooo0OiII1iii in ii1IIi111 :
      os . unlink ( os . path . join ( iI , ooo0OiII1iii ) )
     for OoOo00o0OO in i1iI11i1IIi :
      shutil . rmtree ( os . path . join ( iI , OoOo00o0OO ) )
      if 41 - 41: oO0o / OooO0OoOOOO + IIIi . IIIi / OoOo00o
   else :
    pass
    if 74 - 74: Ii11Ii1I % Ii . o0o00Oo0O * oOo0O0Ooo * ooOoO0O00 * ii
    if 22 - 22: IIIi + o0oOO0O00o0O - iI1iI1I1i1I + iI11I1II1I1I / IIIi - ii
    if 42 - 42: ii - OOooOOo - IIIii1II1II * IIIi
    if 98 - 98: oO0o . iI11I1II1I1I % I1ii11iIi11i + ii
 I1Ii111I111 = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.whatthefurk/cache' ) , '' )
 if os . path . exists ( I1Ii111I111 ) == True :
  for iI , i1iI11i1IIi , ii1IIi111 in os . walk ( I1Ii111I111 ) :
   ii1IIii = 0
   ii1IIii += len ( ii1IIi111 )
   if 7 - 7: oOo0O0Ooo
   if 40 - 40: O0OoO
   if ii1IIii > 0 :
    if 80 - 80: oOo0O0Ooo * IIIi % OoOo00o . Ii % OooO0OoOOOO
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    if i1iiIIiiI111 . yesno ( "Delete WTF Cache Files" , str ( ii1IIii ) + " files found" , "Do you want to delete them?" ) :
     if 42 - 42: ii * IIiIiII11i
     for ooo0OiII1iii in ii1IIi111 :
      os . unlink ( os . path . join ( iI , ooo0OiII1iii ) )
     for OoOo00o0OO in i1iI11i1IIi :
      shutil . rmtree ( os . path . join ( iI , OoOo00o0OO ) )
      if 53 - 53: IIIi + ooOoO0O00 . oO0o / Ii + Ii11Ii1I % OOooOOo
   else :
    pass
    if 9 - 9: O0OoO . iI1iI1I1i1I - I1ii11iIi11i . IIIi
    if 39 - 39: IIIii1II1II
 o00OO00OOo0 = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.4od/cache' ) , '' )
 if os . path . exists ( o00OO00OOo0 ) == True :
  for iI , i1iI11i1IIi , ii1IIi111 in os . walk ( o00OO00OOo0 ) :
   ii1IIii = 0
   ii1IIii += len ( ii1IIi111 )
   if 92 - 92: IIIii1II1II
   if 32 - 32: o0oOO0O00o0O . iI11I1II1I1I % I1ii11iIi11i . ii
   if ii1IIii > 0 :
    if 81 - 81: Ii * o0oOO0O00o0O . OoOo00o * OoOo00o . OooO0OoOOOO
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    if i1iiIIiiI111 . yesno ( "Delete 4oD Cache Files" , str ( ii1IIii ) + " files found" , "Do you want to delete them?" ) :
     if 47 - 47: iI11I1II1I1I % iI1iI1I1i1I . iI1iI1I1i1I / o0o00Oo0O . Ii * Ii11Ii1I
     for ooo0OiII1iii in ii1IIi111 :
      os . unlink ( os . path . join ( iI , ooo0OiII1iii ) )
     for OoOo00o0OO in i1iI11i1IIi :
      shutil . rmtree ( os . path . join ( iI , OoOo00o0OO ) )
      if 24 - 24: o0o00Oo0O
   else :
    pass
    if 33 - 33: ii + OoOo00o * IIiIiII11i / IIIii1II1II
    if 87 - 87: ii
 iiI1Oo = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.iplayer/iplayer_http_cache' ) , '' )
 if os . path . exists ( iiI1Oo ) == True :
  for iI , i1iI11i1IIi , ii1IIi111 in os . walk ( iiI1Oo ) :
   ii1IIii = 0
   ii1IIii += len ( ii1IIi111 )
   if 33 - 33: OoOo00o . OoOo00o - IIiIiII11i - o0oOO0O00o0O + I11i % IIIii1II1II
   if 97 - 97: o0o00Oo0O % o0o00Oo0O
   if ii1IIii > 0 :
    if 35 - 35: o0oOO0O00o0O - Ii11Ii1I . Ii % o0o00Oo0O % Ii1I
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    if i1iiIIiiI111 . yesno ( "Delete BBC iPlayer Cache Files" , str ( ii1IIii ) + " files found" , "Do you want to delete them?" ) :
     if 92 - 92: IIIii1II1II % IIiIiII11i . o0oOO0O00o0O
     for ooo0OiII1iii in ii1IIi111 :
      os . unlink ( os . path . join ( iI , ooo0OiII1iii ) )
     for OoOo00o0OO in i1iI11i1IIi :
      shutil . rmtree ( os . path . join ( iI , OoOo00o0OO ) )
      if 46 - 46: OOooOOo + oOo0O0Ooo % ii * Ii - I1ii11iIi11i
   else :
    pass
    if 47 - 47: o0oOO0O00o0O * OOooOOo * OooO0OoOOOO
    if 46 - 46: Ii11Ii1I
    if 42 - 42: iI11I1II1I1I
 IIi1IiIii = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/script.module.simple.downloader' ) , '' )
 if os . path . exists ( IIi1IiIii ) == True :
  for iI , i1iI11i1IIi , ii1IIi111 in os . walk ( IIi1IiIii ) :
   ii1IIii = 0
   ii1IIii += len ( ii1IIi111 )
   if 40 - 40: oOo0O0Ooo
   if 3 - 3: O0OoO / ooOoO0O00 - OOooOOo
   if ii1IIii > 0 :
    if 73 - 73: ii * o0o00Oo0O * O0OoO
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    if i1iiIIiiI111 . yesno ( "Delete Simple Downloader Cache Files" , str ( ii1IIii ) + " files found" , "Do you want to delete them?" ) :
     if 7 - 7: IIiIiII11i + ooOoO0O00
     for ooo0OiII1iii in ii1IIi111 :
      os . unlink ( os . path . join ( iI , ooo0OiII1iii ) )
     for OoOo00o0OO in i1iI11i1IIi :
      shutil . rmtree ( os . path . join ( iI , OoOo00o0OO ) )
      if 95 - 95: Ii + ii / IIIii1II1II - iI11I1II1I1I + iI11I1II1I1I
   else :
    pass
    if 29 - 29: OooO0OoOOOO % O0OoO + oO0o . ooOoO0O00 + oOo0O0Ooo
    if 24 - 24: IIIi / Ii11Ii1I * Ii1I - ii / oOo0O0Ooo . OoOo00o
 oo0OOoOo0 = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.itv/Images' ) , '' )
 if os . path . exists ( oo0OOoOo0 ) == True :
  for iI , i1iI11i1IIi , ii1IIi111 in os . walk ( oo0OOoOo0 ) :
   ii1IIii = 0
   ii1IIii += len ( ii1IIi111 )
   if 63 - 63: OOooOOo
   if 61 - 61: IIiIiII11i * Ii11Ii1I + IIiIiII11i % o0oOO0O00o0O . ooOoO0O00 . OoOo00o
   if ii1IIii > 0 :
    if 33 - 33: iI11I1II1I1I + oOo0O0Ooo / OoOo00o * o0oOO0O00o0O - OoOo00o
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    if i1iiIIiiI111 . yesno ( "Delete ITV Cache Files" , str ( ii1IIii ) + " files found" , "Do you want to delete them?" ) :
     if 96 - 96: iI1iI1I1i1I . ii % IIiIiII11i % Ii11Ii1I
     for ooo0OiII1iii in ii1IIi111 :
      os . unlink ( os . path . join ( iI , ooo0OiII1iii ) )
     for OoOo00o0OO in i1iI11i1IIi :
      shutil . rmtree ( os . path . join ( iI , OoOo00o0OO ) )
      if 43 - 43: IIiIiII11i . Ii . Ii11Ii1I - OOooOOo . IIIi
   else :
    pass
    if 15 - 15: Ii1I - iI11I1II1I1I % IIiIiII11i / iI1iI1I1i1I
    if 46 - 46: iI11I1II1I1I
 oOOo0OOOOo0o = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.movies4me/cache' ) , '' )
 if os . path . exists ( oo0OOoOo0 ) == True :
  for iI , i1iI11i1IIi , ii1IIi111 in os . walk ( oOOo0OOOOo0o ) :
   ii1IIii = 0
   ii1IIii += len ( ii1IIi111 )
   if 29 - 29: OooO0OoOOOO - iI1iI1I1i1I . o0o00Oo0O . o0o00Oo0O
   if 16 - 16: ooOoO0O00 * O0OoO % oO0o + Ii11Ii1I
   if ii1IIii > 0 :
    if 50 - 50: OoOo00o - ii + o0oOO0O00o0O % oO0o
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    if i1iiIIiiI111 . yesno ( "Delete Movies4me Cache Files" , str ( ii1IIii ) + " files found" , "Do you want to delete them?" ) :
     if 12 - 12: ooOoO0O00 / Ii1I - o0oOO0O00o0O . Ii / ooOoO0O00 / ii
     for ooo0OiII1iii in ii1IIi111 :
      os . unlink ( os . path . join ( iI , ooo0OiII1iii ) )
     for OoOo00o0OO in i1iI11i1IIi :
      shutil . rmtree ( os . path . join ( iI , OoOo00o0OO ) )
      if 88 - 88: Ii11Ii1I / Ii % OOooOOo % IIIii1II1II
   else :
    pass
    if 70 - 70: Ii1I . Ii1I / iI1iI1I1i1I . Ii1I
    if 37 - 37: ooOoO0O00 . IIIi - IIiIiII11i % I11i - ooOoO0O00 . OoOo00o
 iiiiI = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.phstreams/Cache' ) , '' )
 if os . path . exists ( oo0OOoOo0 ) == True :
  for iI , i1iI11i1IIi , ii1IIi111 in os . walk ( iiiiI ) :
   ii1IIii = 0
   ii1IIii += len ( ii1IIi111 )
   if 66 - 66: ii + o0oOO0O00o0O . OooO0OoOOOO % ooOoO0O00
   if 58 - 58: IIIii1II1II % o0oOO0O00o0O * o0o00Oo0O + Ii1I - OooO0OoOOOO
   if ii1IIii > 0 :
    if 26 - 26: ooOoO0O00 / oOo0O0Ooo / iI1iI1I1i1I + iI1iI1I1i1I
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    if i1iiIIiiI111 . yesno ( "Delete Phoenix Cache Files" , str ( ii1IIii ) + " files found" , "Do you want to delete them?" ) :
     if 46 - 46: IIIi % Ii1I + Ii11Ii1I
     for ooo0OiII1iii in ii1IIi111 :
      os . unlink ( os . path . join ( iI , ooo0OiII1iii ) )
     for OoOo00o0OO in i1iI11i1IIi :
      shutil . rmtree ( os . path . join ( iI , OoOo00o0OO ) )
      if 67 - 67: iI11I1II1I1I . Ii . Ii . Ii / iI1iI1I1i1I + O0OoO
   else :
    pass
    if 10 - 10: O0OoO - I1ii11iIi11i % IIiIiII11i
    if 66 - 66: iI11I1II1I1I . iI11I1II1I1I
 I1iI1111ii1I1 = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.spotitube/cache' ) , '' )
 if os . path . exists ( oo0OOoOo0 ) == True :
  for iI , i1iI11i1IIi , ii1IIi111 in os . walk ( I1iI1111ii1I1 ) :
   ii1IIii = 0
   ii1IIii += len ( ii1IIi111 )
   if 70 - 70: Ii1I . o0o00Oo0O
   if 70 - 70: I1ii11iIi11i + Ii
   if ii1IIii > 0 :
    if 44 - 44: Ii / IIIii1II1II * O0OoO
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    if i1iiIIiiI111 . yesno ( "Delete YouTube Music Cache Files" , str ( ii1IIii ) + " files found" , "Do you want to delete them?" ) :
     if 88 - 88: ooOoO0O00 % IIIii1II1II / ii * o0oOO0O00o0O % O0OoO
     for ooo0OiII1iii in ii1IIi111 :
      os . unlink ( os . path . join ( iI , ooo0OiII1iii ) )
     for OoOo00o0OO in i1iI11i1IIi :
      shutil . rmtree ( os . path . join ( iI , OoOo00o0OO ) )
      if 5 - 5: Ii1I * Ii11Ii1I % iI1iI1I1i1I % IIiIiII11i
   else :
    pass
    if 9 - 9: I11i % IIIi + iI1iI1I1i1I
    if 55 - 55: oO0o - Ii1I
 Ii111I1iii1 = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.supercartoons/cache' ) , '' )
 if os . path . exists ( oo0OOoOo0 ) == True :
  for iI , i1iI11i1IIi , ii1IIi111 in os . walk ( Ii111I1iii1 ) :
   ii1IIii = 0
   ii1IIii += len ( ii1IIi111 )
   if 65 - 65: IIIii1II1II - oOo0O0Ooo * IIIi
   if 99 - 99: oOo0O0Ooo
   if ii1IIii > 0 :
    if 64 - 64: Ii1I * Ii11Ii1I * I1ii11iIi11i % OooO0OoOOOO % O0OoO
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    if i1iiIIiiI111 . yesno ( "Delete SuperCartoons Cache Files" , str ( ii1IIii ) + " files found" , "Do you want to delete them?" ) :
     if 55 - 55: IIiIiII11i - IIIi - IIIii1II1II % Ii11Ii1I
     for ooo0OiII1iii in ii1IIi111 :
      os . unlink ( os . path . join ( iI , ooo0OiII1iii ) )
     for OoOo00o0OO in i1iI11i1IIi :
      shutil . rmtree ( os . path . join ( iI , OoOo00o0OO ) )
      if 49 - 49: I1ii11iIi11i * IIIi
   else :
    pass
    if 53 - 53: I1ii11iIi11i / Ii11Ii1I + OoOo00o . o0oOO0O00o0O + OooO0OoOOOO
    if 19 - 19: Ii11Ii1I
 oo0iIi1iiii1ii = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.tvonline.cc/cache' ) , '' )
 if os . path . exists ( oo0OOoOo0 ) == True :
  for iI , i1iI11i1IIi , ii1IIi111 in os . walk ( oo0iIi1iiii1ii ) :
   ii1IIii = 0
   ii1IIii += len ( ii1IIi111 )
   if 96 - 96: oO0o + oOo0O0Ooo % I1ii11iIi11i
   if 21 - 21: OOooOOo - Ii - OOooOOo
   if ii1IIii > 0 :
    if 4 - 4: iI1iI1I1i1I . OooO0OoOOOO
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    if i1iiIIiiI111 . yesno ( "Delete TVonline Cache Files" , str ( ii1IIii ) + " files found" , "Do you want to delete them?" ) :
     if 39 - 39: IIIii1II1II . I1ii11iIi11i - OOooOOo * Ii
     for ooo0OiII1iii in ii1IIi111 :
      os . unlink ( os . path . join ( iI , ooo0OiII1iii ) )
     for OoOo00o0OO in i1iI11i1IIi :
      shutil . rmtree ( os . path . join ( iI , OoOo00o0OO ) )
      if 4 - 4: OOooOOo * o0o00Oo0O - iI1iI1I1i1I
   else :
    pass
    if 72 - 72: iI1iI1I1i1I + O0OoO / oOo0O0Ooo . OooO0OoOOOO % oO0o / Ii
    if 13 - 13: IIIi % I11i + IIIii1II1II + IIIi + Ii - Ii1I
 ooooooo0oOo0 = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.youtube/kodion' ) , '' )
 if os . path . exists ( oo0OOoOo0 ) == True :
  for iI , i1iI11i1IIi , ii1IIi111 in os . walk ( ooooooo0oOo0 ) :
   ii1IIii = 0
   ii1IIii += len ( ii1IIi111 )
   if 81 - 81: Ii % oOo0O0Ooo / o0oOO0O00o0O % oO0o / IIIi % iI11I1II1I1I
   if 14 - 14: Ii1I * I1ii11iIi11i + Ii % IIIii1II1II - OoOo00o
   if ii1IIii > 0 :
    if 11 - 11: Ii1I / o0o00Oo0O + IIiIiII11i
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    if i1iiIIiiI111 . yesno ( "Delete YouTube Cache Files" , str ( ii1IIii ) + " files found" , "Do you want to delete them?" ) :
     if 95 - 95: IIIi + OooO0OoOOOO * iI11I1II1I1I
     for ooo0OiII1iii in ii1IIi111 :
      os . unlink ( os . path . join ( iI , ooo0OiII1iii ) )
     for OoOo00o0OO in i1iI11i1IIi :
      shutil . rmtree ( os . path . join ( iI , OoOo00o0OO ) )
      if 17 - 17: oO0o - I1ii11iIi11i * o0o00Oo0O / Ii11Ii1I
   else :
    pass
    if 19 - 19: ooOoO0O00 - iI11I1II1I1I . iI1iI1I1i1I
    if 2 - 2: Ii11Ii1I
    if 12 - 12: Ii - iI11I1II1I1I * OooO0OoOOOO * o0oOO0O00o0O
 iiIII1i = xbmc . translatePath ( 'special://masterprofile/addon_data/plugin.video.genesis' )
 i1iiIIiiI111 = xbmcgui . Dialog ( )
 try :
  if i1iiIIiiI111 . yesno ( "Delete Genesis Cache Files" , "Do you want to delete cache" ) :
   IiI1Ii11Iiii = os . path . join ( iiIII1i , "cache.db" )
   os . unlink ( IiI1Ii11Iiii )
   if 44 - 44: Ii % IIIi % OoOo00o + iI1iI1I1i1I * OoOo00o . Ii11Ii1I
 except :
  pass
  if 89 - 89: ii % IIiIiII11i - oO0o % Ii
 i1iiIIiiI111 = xbmcgui . Dialog ( )
 i1iiIIiiI111 . ok ( "GenieTv" , "                               Finished Deleting Cache " , "                          [COLOR gold]Brought To You By GenieTv[/COLOR]" )
 if 7 - 7: OooO0OoOOOO
 if 15 - 15: I1ii11iIi11i + o0oOO0O00o0O + oOo0O0Ooo * I11i
 if 33 - 33: I11i * I1ii11iIi11i
 if 88 - 88: IIIi % IIIii1II1II - OOooOOo - OOooOOo . oOo0O0Ooo
 if 52 - 52: IIiIiII11i / IIiIiII11i / oOo0O0Ooo - IIIi
 if 91 - 91: oOo0O0Ooo + I11i % IIiIiII11i + oO0o
 if 66 - 66: iI11I1II1I1I * IIiIiII11i % I1ii11iIi11i % oOo0O0Ooo - Ii11Ii1I
 if 59 - 59: OooO0OoOOOO % OoOo00o
 if 21 - 21: ii % OOooOOo - OOooOOo / Ii1I / I11i
def I111i ( url ) :
 print '###' + o0oOoO00o + ' - DELETING PACKAGES###'
 II1IiIiiI1III = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' , '' ) )
 try :
  for iI , i1iI11i1IIi , ii1IIi111 in os . walk ( II1IiIiiI1III ) :
   ii1IIii = 0
   ii1IIii += len ( ii1IIi111 )
   if 12 - 12: o0oOO0O00o0O + o0o00Oo0O
   if 85 - 85: IIiIiII11i - Ii11Ii1I
   if ii1IIii > 0 :
    if 93 - 93: OooO0OoOOOO / Ii - OoOo00o + oO0o / ooOoO0O00
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    if i1iiIIiiI111 . yesno ( "Delete Package Cache Files" , str ( ii1IIii ) + " files found" , "Do you want to delete them?" ) :
     if 62 - 62: Ii1I / ii * oOo0O0Ooo - ooOoO0O00
     for ooo0OiII1iii in ii1IIi111 :
      os . unlink ( os . path . join ( iI , ooo0OiII1iii ) )
     for OoOo00o0OO in i1iI11i1IIi :
      shutil . rmtree ( os . path . join ( iI , OoOo00o0OO ) )
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
 if 81 - 81: OoOo00o / o0o00Oo0O * O0OoO % OOooOOo / o0o00Oo0O
 if 85 - 85: ii + ii
 if 23 - 23: ooOoO0O00
 if 31 - 31: I1ii11iIi11i - iI11I1II1I1I / iI1iI1I1i1I . oO0o
 if 74 - 74: I1ii11iIi11i - IIiIiII11i - OooO0OoOOOO
 if 50 - 50: oOo0O0Ooo - OoOo00o + OoOo00o * iI1iI1I1i1I + OoOo00o
 if 70 - 70: ooOoO0O00 % oO0o / ooOoO0O00
 if 30 - 30: OOooOOo - Ii
 if 94 - 94: OOooOOo % o0oOO0O00o0O
def iI11ii ( url ) :
 print '###' + o0oOoO00o + ' - DELETING PACKAGES###'
 II1IiIiiI1III = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' , '' ) )
 try :
  for iI , i1iI11i1IIi , ii1IIi111 in os . walk ( II1IiIiiI1III ) :
   ii1IIii = 0
   ii1IIii += len ( ii1IIi111 )
   if 23 - 23: OOooOOo * OooO0OoOOOO / OoOo00o
   if 60 - 60: O0OoO * Ii11Ii1I + IIIi . IIIii1II1II . o0o00Oo0O
   if ii1IIii > 0 :
    if 8 - 8: IIiIiII11i + IIiIiII11i * ooOoO0O00 * I11i / o0o00Oo0O / o0o00Oo0O
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    if i1iiIIiiI111 . yesno ( "Delete Package Cache Files" , str ( ii1IIii ) + " files found" , "Do you want to delete them?" ) :
     if 66 - 66: IIIi * I11i / OooO0OoOOOO * o0oOO0O00o0O / ii
     for ooo0OiII1iii in ii1IIi111 :
      os . unlink ( os . path . join ( iI , ooo0OiII1iii ) )
     for OoOo00o0OO in i1iI11i1IIi :
      shutil . rmtree ( os . path . join ( iI , OoOo00o0OO ) )
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
 OOOo0Ooo0o00o ( url )
 if 72 - 72: iI11I1II1I1I
 if 82 - 82: OOooOOo . Ii11Ii1I
 if 73 - 73: IIIi
 if 25 - 25: OooO0OoOOOO
 if 77 - 77: I11i . iI11I1II1I1I . ii . iI11I1II1I1I
 if 87 - 87: IIiIiII11i - ii / ooOoO0O00 . Ii11Ii1I - I1ii11iIi11i . Ii
 if 47 - 47: I1ii11iIi11i % oO0o - O0OoO - I1ii11iIi11i * OoOo00o
 if 72 - 72: I11i % I11i + o0oOO0O00o0O + Ii1I / I1ii11iIi11i
 if 30 - 30: I1ii11iIi11i + oOo0O0Ooo + Ii / oO0o
def o00OooooOOOO ( url , name ) :
 oO0oo = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 oo000o = os . path . join ( oO0oo , 'advancedsettings.xml' )
 i1iiIIiiI111 = xbmcgui . Dialog ( )
 iIIIII = os . path . join ( oO0oo , 'advancedsettings.xml.bak' )
 if os . path . exists ( iIIIII ) == False :
  if i1iiIIiiI111 . yesno ( "Back Up Original" , 'Have You Backed Up Your Original?' , '' , "[B][COLOR red]     AS YOU CANNOT GO BACK !!![/B][/COLOR]" ) :
   print '###' + o0oOoO00o + ' - ADVANCED XML###'
   oO0oo = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
   oo000o = os . path . join ( oO0oo , 'advancedsettings.xml' )
   try :
    os . remove ( oo000o )
    print '=== GenieTv - REMOVING    ' + str ( oo000o ) + '    ==='
   except :
    pass
   O000oo0O = i1 . http_GET ( url ) . content
   i11i1iiiII = open ( oo000o , "w" )
   i11i1iiiII . write ( O000oo0O )
   i11i1iiiII . close ( )
   print '=== GenieTv - WRITING NEW    ' + str ( oo000o ) + '    ==='
   i1iiIIiiI111 = xbmcgui . Dialog ( )
   i1iiIIiiI111 . ok ( o0oOoO00o , "       Done Adding new Advanced XML" )
 else :
  print '###' + o0oOoO00o + ' - ADVANCED XML###'
  oO0oo = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
  oo000o = os . path . join ( oO0oo , 'advancedsettings.xml' )
  try :
   os . remove ( oo000o )
   print '=== GenieTv - REMOVING    ' + str ( oo000o ) + '    ==='
  except :
   pass
  O000oo0O = i1 . http_GET ( url ) . content
  i11i1iiiII = open ( oo000o , "w" )
  i11i1iiiII . write ( O000oo0O )
  i11i1iiiII . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( oo000o ) + '    ==='
  i1iiIIiiI111 = xbmcgui . Dialog ( )
  i1iiIIiiI111 . ok ( o0oOoO00o , "       Done Adding new Advanced XML" )
 return
 if 48 - 48: OOooOOo * ii + ii * iI11I1II1I1I * IIiIiII11i % Ii
def IIoooOoOO0o ( url , name ) :
 print '###' + o0oOoO00o + ' - CHECK ADVANCE XML###'
 oO0oo = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 oo000o = os . path . join ( oO0oo , 'advancedsettings.xml' )
 try :
  i11i1iiiII = open ( oo000o ) . read ( )
  if 'zero' in i11i1iiiII :
   name = '0CACHE'
  elif 'tuxen' in i11i1iiiII :
   name = 'TUXENS'
  elif 'muckys' in i11i1iiiII :
   name = 'MUCKYS'
  elif 'p2p1' in i11i1iiiII :
   name = '1st P2P RECOMMENDED'
  elif 'p2p2' in i11i1iiiII :
   name = '2nd P2P RECOMMENDED'
  elif 'mikey' in i11i1iiiII :
   name = 'MIKEY1234'
 except :
  name = "NO ADVANCED"
 i1iiIIiiI111 = xbmcgui . Dialog ( )
 i1iiIIiiI111 . ok ( o0oOoO00o , "[COLOR yellow]YOU HAVE[/COLOR] " + name + "[COLOR yellow] XML SETTINGS SETUP[/COLOR]" )
 return
 if 78 - 78: o0o00Oo0O - IIIi * IIIii1II1II + iI1iI1I1i1I + IIiIiII11i
def IIIiiII1iIi1ii1i ( url ) :
 print '###' + o0oOoO00o + ' - DELETING ADVANCE XML###'
 oO0oo = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 oo000o = os . path . join ( oO0oo , 'advancedsettings.xml' )
 try :
  os . remove ( oo000o )
  i1iiIIiiI111 = xbmcgui . Dialog ( )
  print '=== GenieTv - DELETING    ' + str ( oo000o ) + '    ==='
  i1iiIIiiI111 . ok ( o0oOoO00o , "       Remove Advanced Settings Sucessfull" )
 except :
  i1iiIIiiI111 = xbmcgui . Dialog ( )
  i1iiIIiiI111 . ok ( o0oOoO00o , "       No Advanced Settings To Remove" )
 return
 if 49 - 49: OOooOOo
 if 99 - 99: o0o00Oo0O + OooO0OoOOOO + O0OoO - O0OoO * Ii1I / OooO0OoOOOO
 if 82 - 82: I11i - IIIii1II1II
 if 84 - 84: o0oOO0O00o0O % ooOoO0O00 % oO0o % IIiIiII11i
 if 94 - 94: O0OoO * o0o00Oo0O
 if 60 - 60: o0oOO0O00o0O / o0oOO0O00o0O - O0OoO / ii + o0o00Oo0O
 if 55 - 55: oO0o % o0o00Oo0O / ii
 if 49 - 49: oOo0O0Ooo . oO0o * ii % Ii + iI11I1II1I1I * ooOoO0O00
 if 88 - 88: Ii1I * o0oOO0O00o0O + IIiIiII11i
 if 62 - 62: ii
def iioOo00O0o ( url = 'http://www.iplocation.net/' , inc = 1 ) :
 iiIii = re . compile ( "<td width='80'>(.+?)</td><td>(.+?)</td><td>(.+?)</td><td>.+?</td><td>(.+?)</td>" ) . findall ( i1 . http_GET ( url ) . content )
 for iI11IIi1iiI1I , oO0oO0ooOoO0 , Ii1I11IIi1 , I1ii in iiIii :
  if inc < 2 : i1iiIIiiI111 = xbmcgui . Dialog ( ) ; i1iiIIiiI111 . ok ( 'Check My IP' , "[B][COLOR gold]Your IP Address is: [/COLOR][/B] %s" % iI11IIi1iiI1I , '[B][COLOR gold]Your IP is based in: [/COLOR][/B] %s' % Ii1I11IIi1 , '[B][COLOR gold]Your Service Provider is:[/COLOR][/B] %s' % I1ii )
  inc = inc + 1
  if 25 - 25: ii
  if 8 - 8: iI11I1II1I1I . iI11I1II1I1I + Ii11Ii1I . IIIii1II1II
  if 58 - 58: iI11I1II1I1I + IIIi - Ii1I - ooOoO0O00 * OOooOOo
  if 4 - 4: ii
  if 7 - 7: OooO0OoOOOO
  if 26 - 26: IIIii1II1II + I1ii11iIi11i
  if 71 - 71: oOo0O0Ooo . O0OoO
  if 43 - 43: Ii1I * IIIii1II1II
  if 1 - 1: oO0o * O0OoO + OooO0OoOOOO . OoOo00o / O0OoO
def O0O00Oo ( url , name ) :
 i1iiIIiiI111 = xbmcgui . Dialog ( )
 if i1iiIIiiI111 . yesno ( "GenieTv" , '                                    Install Latest .ini File' ) :
  print '###' + o0oOoO00o + ' - CUSTOM FTV INI###'
  oO0oo = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/plugin.video.GenieTv' , '' ) )
  oo000o = os . path . join ( oO0oo , 'addons2.ini' )
  O000oo0O = i1 . http_GET ( url ) . content
  i11i1iiiII = open ( oo000o , "w" )
  i11i1iiiII . write ( O000oo0O )
  i11i1iiiII . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( oo000o ) + '    ==='
  i1iiIIiiI111 = xbmcgui . Dialog ( )
  i1iiIIiiI111 . ok ( o0oOoO00o , "                               Done Adding New .ini File" )
 return
 if 49 - 49: ooOoO0O00 - IIIii1II1II / I11i % OooO0OoOOOO - O0OoO
def O00O0OO ( url , name ) :
 i1iiIIiiI111 = xbmcgui . Dialog ( )
 if i1iiIIiiI111 . yesno ( "GenieTv" , '                               Install Custom Settings' ) :
  print '###' + o0oOoO00o + ' - CUSTOM FTV SETTINGS###'
  oO0oo = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/plugin.video.GenieTv' , '' ) )
  oo000o = os . path . join ( oO0oo , 'settings.xml' )
  O000oo0O = i1 . http_GET ( url ) . content
  i11i1iiiII = open ( oo000o , "w" )
  i11i1iiiII . write ( O000oo0O )
  i11i1iiiII . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( oo000o ) + '    ==='
  i1iiIIiiI111 = xbmcgui . Dialog ( )
  i1iiIIiiI111 . ok ( o0oOoO00o , "                               Done Adding New Settings" )
 return
 if 76 - 76: oOo0O0Ooo
 if 41 - 41: OOooOOo % IIIi * OoOo00o * ooOoO0O00
def IiIii1i ( ) :
 try :
  I1i11i1II = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/plugin.video.GenieTv' , '' ) )
  if os . path . exists ( I1i11i1II ) == True :
   i1iiIIiiI111 = xbmcgui . Dialog ( )
   if i1iiIIiiI111 . yesno ( "GenieTv" , "                               Delete FTV Guide Database" ) :
    OOoOo0oOooo = os . path . join ( I1i11i1II , "source.db" )
    os . unlink ( OOoOo0oOooo )
  i1iiIIiiI111 . ok ( "GenieTv" , "                                     FTV Database Reset" )
 except :
  i1iiIIiiI111 = xbmcgui . Dialog ( )
  i1iiIIiiI111 . ok ( o0oOoO00o , "               Error Deleting Database No Database To Delete" )
 return
 if 99 - 99: I11i / IIIii1II1II / OoOo00o . IIIi
 if 3 - 3: iI1iI1I1i1I
 if 26 - 26: oO0o % ooOoO0O00 * o0o00Oo0O . IIIi
 if 31 - 31: o0o00Oo0O - OooO0OoOOOO * Ii * ooOoO0O00
 if 78 - 78: O0OoO * OOooOOo . Ii11Ii1I . OOooOOo % iI11I1II1I1I
def oO0OOoo0OO ( url ) :
 I11iii1Ii = urllib2 . Request ( url )
 I11iii1Ii . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
 I1IIiiIiii = urllib2 . urlopen ( I11iii1Ii )
 O000oo0O = I1IIiiIiii . read ( )
 I1IIiiIiii . close ( )
 return O000oo0O
 if 67 - 67: Ii11Ii1I . I1ii11iIi11i
 if 39 - 39: iI1iI1I1i1I * IIIi
 if 63 - 63: O0OoO % oOo0O0Ooo . IIIii1II1II - O0OoO / I1ii11iIi11i % oOo0O0Ooo
 if 39 - 39: I11i . ooOoO0O00 % OoOo00o / iI1iI1I1i1I % o0o00Oo0O
 if 100 - 100: IIIi - OOooOOo
 if 78 - 78: ii - OOooOOo . Ii
 if 36 - 36: OoOo00o * o0oOO0O00o0O + OooO0OoOOOO * o0oOO0O00o0O . Ii1I - iI11I1II1I1I
def i1IIi1ii1i1ii ( params ) :
 plugintools . log ( "freshstart.main_list " + repr ( params ) ) ; oOoOO = plugintools . message_yes_no ( o0oOoO00o , "Do you wish to restore your" , "Kodi configuration to default settings?" )
 if oOoOO :
  Iiii111I1IiiI1i = xbmcaddon . Addon ( id = o00 ) . getAddonInfo ( 'path' ) ; Iiii111I1IiiI1i = xbmc . translatePath ( Iiii111I1IiiI1i ) ;
  Ii1IOOO0oOo00o0 = os . path . join ( Iiii111I1IiiI1i , ".." , ".." ) ; Ii1IOOO0oOo00o0 = os . path . abspath ( Ii1IOOO0oOo00o0 ) ; plugintools . log ( "freshstart.main_list xbmcPath=" + Ii1IOOO0oOo00o0 ) ; Iii1IiIIiII1 = False
  try :
   for iI , i1iI11i1IIi , ii1IIi111 in os . walk ( Ii1IOOO0oOo00o0 , topdown = True ) :
    i1iI11i1IIi [ : ] = [ OoOo00o0OO for OoOo00o0OO in i1iI11i1IIi if OoOo00o0OO not in iiIIIII1i1iI ]
    for I1i1i1iii in ii1IIi111 :
     try : os . remove ( os . path . join ( iI , I1i1i1iii ) )
     except :
      if I1i1i1iii not in [ "Addons15.db" , "MyVideos75.db" , "Textures13.db" , "xbmc.log" ] : Iii1IiIIiII1 = True
      plugintools . log ( "Error removing " + iI + " " + I1i1i1iii )
    for I1i1i1iii in i1iI11i1IIi :
     try : os . rmdir ( os . path . join ( iI , I1i1i1iii ) )
     except :
      if I1i1i1iii not in [ "Database" , "userdata" ] : Iii1IiIIiII1 = True
      plugintools . log ( "Error removing " + iI + " " + I1i1i1iii )
   if not Iii1IiIIiII1 : plugintools . log ( "freshstart.main_list All user files removed, you now have a clean install" ) ; plugintools . message ( o0oOoO00o , "The process is complete, you're now back to a fresh Kodi configuration with GenieTv!" , "Please reboot your system or restart Kodi in order for the changes to be applied." )
   else : plugintools . log ( "freshstart.main_list User files partially removed" ) ; plugintools . message ( o0oOoO00o , "The process is complete, you're now back to a fresh Kodi configuration with GenieTv" , "Please reboot your system or restart Kodi in order for the changes to be applied." )
  except : plugintools . message ( o0oOoO00o , "Problem found" , "Your settings has not been changed" ) ; import traceback ; plugintools . log ( traceback . format_exc ( ) ) ; plugintools . log ( "freshstart.main_list NOT removed" )
  plugintools . add_item ( action = "" , title = "Now Exit Kodi" , folder = False )
 else : plugintools . message ( o0oOoO00o , "Your settings" , "has not been changed" ) ; plugintools . add_item ( action = "" , title = "Done" , folder = False )
 oo0OOOoOo ( )
 if 9 - 9: Ii1I - OooO0OoOOOO
 if 64 - 64: ooOoO0O00
 if 71 - 71: OooO0OoOOOO * I11i
def oo00oOoo ( ) :
 oOOO0oo0 = [ ]
 iI1IiiiiI = sys . argv [ 2 ]
 if len ( iI1IiiiiI ) >= 2 :
  Ii1Ooo0OO00oo = sys . argv [ 2 ]
  i11iII1IiI = Ii1Ooo0OO00oo . replace ( '?' , '' )
  if ( Ii1Ooo0OO00oo [ len ( Ii1Ooo0OO00oo ) - 1 ] == '/' ) :
   Ii1Ooo0OO00oo = Ii1Ooo0OO00oo [ 0 : len ( Ii1Ooo0OO00oo ) - 2 ]
  i1II1IiIi111 = i11iII1IiI . split ( '&' )
  oOOO0oo0 = { }
  for i1i1Ii11Ii in range ( len ( i1II1IiIi111 ) ) :
   ooo = { }
   ooo = i1II1IiIi111 [ i1i1Ii11Ii ] . split ( '=' )
   if ( len ( ooo ) ) == 2 :
    oOOO0oo0 [ ooo [ 0 ] ] = ooo [ 1 ]
    if 18 - 18: Ii11Ii1I + OOooOOo . ooOoO0O00 / OooO0OoOOOO / o0oOO0O00o0O
 return oOOO0oo0
 if 97 - 97: oO0o + iI11I1II1I1I
III1I1Ii11iI = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkbw==' )
OOoiIIiiIIIi1I = base64 . decodestring ( 'L3N0b3JhZ2UvZW11bGF0ZWQvMA==' )
oO00OoOO = base64 . decodestring ( 'L2dlbmllLnR4dA==' )
O0OOoo = base64 . decodestring ( 'LmFyY2hpdGVjdHMueDEwaG9zdC5jb20vdGVzdC93aC50eHQ=' )
I1IiIIi = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby9maXhlcy9maXhlcy50eHQ=' )
i1Ii1Ii111 = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby9hcHBzL2FwcHMueG1s' )
o0O0o = base64 . decodestring ( 'L2FkZG9ucy9uZXcudHh0' )
OO0o0o0OOoooo = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby92b2Qvdm9kLnBocA==' )
O0ooO = base64 . decodestring ( 'L2FkZG9ucy9pcHR2LnR4dA==' )
Oo0O00OO = base64 . decodestring ( 'L2FkZG9ucy92aWRlby50eHQ=' )
I1iIiI = base64 . decodestring ( 'L2FkZG9ucy9zcG9ydHMudHh0' )
Oo0o0OoOoOo0 = base64 . decodestring ( 'L2FkZG9ucy9raWRzLnR4dA==' )
iII1i111iI = base64 . decodestring ( 'L2FkZG9ucy9tdXNpYy50eHQ=' )
II1II111 = base64 . decodestring ( 'L2FkZG9ucy9wcm9ncmFtcy50eHQ=' )
OOOoOOO0oOOoO = base64 . decodestring ( 'L2FkZG9ucy94eHgudHh0' )
i1iI11iI = base64 . decodestring ( 'L2FkZG9ucy9yZXBvLnR4dA==' )
ii1II = base64 . decodestring ( 'L2FkZG9ucy9wYWNrcy50eHQ=' )
oOO00OOOO0o = base64 . decodestring ( 'L2FkZG9ucy9za2lucy50eHQ=' )
I1111I1II11 = base64 . decodestring ( 'L2FkZG9ucy9hcnQudHh0' )
i1iI11I1II1 = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2dvdGhhbS50eHQ=' )
O0000 = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2hlbGl4LnR4dA==' )
o0o00Ooo0o = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2lzZW5nYXJkLnR4dA==' )
I1II1iIi = base64 . decodestring ( 'L2FkZG9ucy9SU1MudHh0' )
oOiiI1Ii11II1I = base64 . decodestring ( 'Q1VOVA==' )
def IIII ( name , url , mode , iconimage , fanart , description , showcontext = True , allinfo = { } ) :
 I1iIII1IiiI = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 OOoooOoO0Oo = True
 Oo000 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 Oo000 . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 Oo000 . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  I1III1I11I1 = [ ]
  if showcontext == 'fav' :
   I1III1I11I1 . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in OOO00 :
   I1III1I11I1 . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fanart=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , urllib . quote_plus ( fanart ) , mode ) ) )
  Oo000 . addContextMenuItems ( I1III1I11I1 )
 OOoooOoO0Oo = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = I1iIII1IiiI , listitem = Oo000 , isFolder = True )
 return OOoooOoO0Oo
 if 86 - 86: I11i % oO0o + Ii1I
def O0i1II1Iiii1I11 ( name , url , mode , iconimage , fanart , description ) :
 I1iIII1IiiI = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 OOoooOoO0Oo = True
 Oo000 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 Oo000 . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 Oo000 . setProperty ( "Fanart_Image" , fanart )
 OOoooOoO0Oo = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = I1iIII1IiiI , listitem = Oo000 , isFolder = False )
 return OOoooOoO0Oo
 if 69 - 69: OooO0OoOOOO
 if 24 - 24: oO0o / o0o00Oo0O * O0OoO % iI11I1II1I1I + ooOoO0O00 % o0o00Oo0O
Ii1Ooo0OO00oo = oo00oOoo ( )
OooOoOo = None
I1i1i1iii = None
i1iIIi1II1iiI = None
OOOOO0O00 = None
Iii = None
iIIIII1I = None
I1I11i = None
if 93 - 93: IIiIiII11i . iI1iI1I1i1I - ooOoO0O00 * OOooOOo
if 28 - 28: iI1iI1I1i1I % IIIi
try :
 I1I11i = int ( Ii1Ooo0OO00oo [ "fav_mode" ] )
except :
 pass
 if 49 - 49: OooO0OoOOOO % I11i . Ii1I / IIIii1II1II . Ii11Ii1I * Ii1I
try :
 OooOoOo = urllib . unquote_plus ( Ii1Ooo0OO00oo [ "url" ] )
except :
 pass
try :
 I1i1i1iii = urllib . unquote_plus ( Ii1Ooo0OO00oo [ "name" ] )
except :
 pass
try :
 OOOOO0O00 = urllib . unquote_plus ( Ii1Ooo0OO00oo [ "iconimage" ] )
except :
 pass
try :
 i1iIIi1II1iiI = int ( Ii1Ooo0OO00oo [ "mode" ] )
except :
 pass
try :
 Iii = urllib . unquote_plus ( Ii1Ooo0OO00oo [ "fanart" ] )
except :
 pass
try :
 iIIIII1I = urllib . unquote_plus ( Ii1Ooo0OO00oo [ "description" ] )
except :
 pass
 if 17 - 17: Ii1I * ii % ooOoO0O00 % ii . o0oOO0O00o0O
 if 20 - 20: oO0o . OoOo00o
print str ( oOOoO0 ) + ': ' + str ( IiiIII111iI )
print "Mode: " + str ( i1iIIi1II1iiI )
print "URL: " + str ( OooOoOo )
print "Name: " + str ( I1i1i1iii )
print "IconImage: " + str ( OOOOO0O00 )
if 4 - 4: I1ii11iIi11i % Ii11Ii1I % oO0o * o0oOO0O00o0O % ii
if 38 - 38: ii . o0oOO0O00o0O
def o00oooO0Oo ( content , viewType ) :
 if 43 - 43: ii
 if content :
  xbmcplugin . setContent ( int ( sys . argv [ 1 ] ) , content )
 if o0oO0 . getSetting ( 'auto-view' ) == 'true' :
  xbmc . executebuiltin ( "Container.SetViewMode(%s)" % o0oO0 . getSetting ( viewType ) )
  if 8 - 8: IIIii1II1II + iI1iI1I1i1I . iI1iI1I1i1I
  if 89 - 89: Ii1I * Ii1I * OOooOOo / o0oOO0O00o0O
if i1iIIi1II1iiI == None :
 IiIIIi1iIi ( )
 if 60 - 60: oO0o / o0oOO0O00o0O / oOo0O0Ooo + OoOo00o
elif i1iIIi1II1iiI == 1 :
 I1iIi1iiiIiI ( OooOoOo )
 if 93 - 93: ii * Ii11Ii1I / o0o00Oo0O + Ii11Ii1I - iI11I1II1I1I
elif i1iIIi1II1iiI == 44 :
 O0oOoOOO0OO ( OooOoOo )
 if 6 - 6: OooO0OoOOOO - I1ii11iIi11i - iI1iI1I1i1I - o0o00Oo0O % ii
elif i1iIIi1II1iiI == 2 :
 Iiii1I1 ( )
 if 88 - 88: o0o00Oo0O / I11i * I11i . I11i . o0o00Oo0O
elif i1iIIi1II1iiI == 3 :
 oo0OOo0O ( )
 if 27 - 27: Ii % o0oOO0O00o0O + Ii11Ii1I . IIIii1II1II
elif i1iIIi1II1iiI == 21 :
 iI1Ii11111iIi ( )
 if 9 - 9: oO0o
elif i1iIIi1II1iiI == 4 :
 iii1 ( )
 if 43 - 43: Ii11Ii1I . IIIii1II1II + oOo0O0Ooo * Ii
elif i1iIIi1II1iiI == 5 :
 O0O0 ( I1i1i1iii , OooOoOo , iIIIII1I )
 if 2 - 2: IIIii1II1II
elif i1iIIi1II1iiI == 6 :
 I111i ( OooOoOo )
 if 3 - 3: oOo0O0Ooo . o0oOO0O00o0O % o0o00Oo0O - O0OoO / o0o00Oo0O
elif i1iIIi1II1iiI == 7 :
 o00OooooOOOO ( OooOoOo , I1i1i1iii )
 if 79 - 79: Ii11Ii1I + OoOo00o % O0OoO % oOo0O0Ooo
elif i1iIIi1II1iiI == 8 :
 IIoooOoOO0o ( OooOoOo , I1i1i1iii )
 if 68 - 68: IIiIiII11i - ii / iI11I1II1I1I - I11i % IIiIiII11i
elif i1iIIi1II1iiI == 9 :
 FIXREPOSADDONS ( OooOoOo )
 if 53 - 53: o0oOO0O00o0O . OoOo00o / I1ii11iIi11i . oO0o . Ii
elif i1iIIi1II1iiI == 10 :
 oOo0O ( )
 if 60 - 60: IIiIiII11i
elif i1iIIi1II1iiI == 11 :
 IIIiiII1iIi1ii1i ( OooOoOo )
 if 25 - 25: I1ii11iIi11i + I11i - oO0o
elif i1iIIi1II1iiI == 12 :
 iioOo00O0o ( )
 if 57 - 57: IIiIiII11i . ooOoO0O00
elif i1iIIi1II1iiI == 13 :
 O00oOOoOOOOO ( )
 if 33 - 33: o0oOO0O00o0O + I1ii11iIi11i % iI1iI1I1i1I . OoOo00o
elif i1iIIi1II1iiI == 14 :
 OOOo0Ooo0o00o ( OooOoOo )
 if 6 - 6: OooO0OoOOOO + Ii1I
elif i1iIIi1II1iiI == 15 :
 i11iIIi11 ( )
 if 62 - 62: OoOo00o . IIIi - ii * IIiIiII11i . Ii
elif i1iIIi1II1iiI == 16 :
 O0O00Oo ( OooOoOo , I1i1i1iii )
 if 13 - 13: iI11I1II1I1I * I11i - Ii
elif i1iIIi1II1iiI == 17 :
 O00O0OO ( OooOoOo , I1i1i1iii )
 if 63 - 63: ii * IIIi
elif i1iIIi1II1iiI == 18 :
 IiIii1i ( )
 if 50 - 50: I1ii11iIi11i - I11i % IIiIiII11i . o0o00Oo0O . OoOo00o % IIiIiII11i
elif i1iIIi1II1iiI == 19 :
 o0OoO000O ( I1i1i1iii , OooOoOo , iIIIII1I )
 if 18 - 18: iI1iI1I1i1I % ii + oO0o / iI1iI1I1i1I
elif i1iIIi1II1iiI == 40 :
 ooOoO ( I1i1i1iii , OooOoOo , iIIIII1I )
 if 37 - 37: ooOoO0O00 - Ii11Ii1I / OooO0OoOOOO . IIiIiII11i % O0OoO
elif i1iIIi1II1iiI == 42 :
 i1ii11 ( I1i1i1iii , OooOoOo , iIIIII1I )
 if 39 - 39: Ii11Ii1I % Ii * oO0o
elif i1iIIi1II1iiI == 43 :
 I11IIIiIi11 ( I1i1i1iii , OooOoOo , iIIIII1I )
 if 23 - 23: IIIii1II1II + O0OoO / Ii * I1ii11iIi11i . oO0o
elif i1iIIi1II1iiI == 20 :
 oOOo ( OooOoOo )
 if 28 - 28: o0oOO0O00o0O - I11i
elif i1iIIi1II1iiI == 22 :
 OoiIIii1Ii1 ( OooOoOo )
 if 92 - 92: I1ii11iIi11i % I11i - O0OoO / O0OoO / OOooOOo
elif i1iIIi1II1iiI == 23 :
 O0O00O ( OooOoOo )
 if 84 - 84: IIIii1II1II
elif i1iIIi1II1iiI == 24 :
 OO0OOO ( OooOoOo )
 if 4 - 4: OooO0OoOOOO . IIIi / Ii11Ii1I / o0oOO0O00o0O + IIiIiII11i
elif i1iIIi1II1iiI == 25 :
 O0oOo0o0000 ( OooOoOo )
 if 32 - 32: ooOoO0O00 + iI11I1II1I1I . Ii1I . iI1iI1I1i1I - Ii11Ii1I
elif i1iIIi1II1iiI == 26 :
 oO000O ( OooOoOo )
 if 55 - 55: Ii1I / ii - oO0o / oOo0O0Ooo
elif i1iIIi1II1iiI == 27 :
 O0ooO0 ( OooOoOo )
 if 23 - 23: iI1iI1I1i1I * IIIi * I11i - oOo0O0Ooo % OOooOOo + I11i
elif i1iIIi1II1iiI == 28 :
 iiI1 ( OooOoOo )
 if 41 - 41: OooO0OoOOOO * ii . O0OoO % Ii
elif i1iIIi1II1iiI == 29 :
 I11o0O00 ( OooOoOo )
 if 11 - 11: iI11I1II1I1I . IIIi - I1ii11iIi11i / iI1iI1I1i1I + IIiIiII11i
elif i1iIIi1II1iiI == 30 :
 oOoOoo0 ( OooOoOo )
 if 29 - 29: iI1iI1I1i1I . Ii + ooOoO0O00 - Ii11Ii1I + o0o00Oo0O . oOo0O0Ooo
elif i1iIIi1II1iiI == 31 :
 I111I111 ( OooOoOo )
 if 8 - 8: I11i
elif i1iIIi1II1iiI == 32 :
 o0O0O0 ( )
 if 78 - 78: ooOoO0O00 - I1ii11iIi11i
elif i1iIIi1II1iiI == 33 :
 OooOOO ( )
 if 48 - 48: Ii11Ii1I - ii + IIIi % I11i - OOooOOo . oOo0O0Ooo
elif i1iIIi1II1iiI == 35 :
 O0O00O000OOO ( OooOoOo )
 if 42 - 42: IIIi
elif i1iIIi1II1iiI == 34 :
 O00oOo ( OooOoOo )
 if 70 - 70: I11i / iI1iI1I1i1I + OoOo00o % oOo0O0Ooo % I1ii11iIi11i + oO0o
elif i1iIIi1II1iiI == 36 :
 Iiii11iIi1 ( OooOoOo )
 if 80 - 80: IIIii1II1II
elif i1iIIi1II1iiI == 37 :
 OO0oIII111i11IiI ( OooOoOo )
 if 12 - 12: Ii11Ii1I
elif i1iIIi1II1iiI == 38 :
 O0O0ooOOO ( OooOoOo )
 if 2 - 2: ii
elif i1iIIi1II1iiI == 41 :
 i1IIi1ii1i1ii ( Ii1Ooo0OO00oo )
 if 100 - 100: I1ii11iIi11i / o0o00Oo0O * Ii * ii
elif i1iIIi1II1iiI == 39 :
 iII11iI1iiIIi ( OooOoOo )
 if 46 - 46: o0o00Oo0O % ii
elif i1iIIi1II1iiI == 45 :
 TEXTS ( )
 if 22 - 22: o0oOO0O00o0O + ii - OOooOOo - oO0o * IIIi - OoOo00o
elif i1iIIi1II1iiI == 46 :
 iiIiiiIii11i1 ( )
 if 99 - 99: O0OoO / oOo0O0Ooo . Ii11Ii1I - Ii11Ii1I * oOo0O0Ooo
elif i1iIIi1II1iiI == 47 :
 GEVID ( )
 if 24 - 24: iI1iI1I1i1I * oO0o - OoOo00o / iI11I1II1I1I - I1ii11iIi11i . IIIii1II1II
elif i1iIIi1II1iiI == 48 :
 OooO0oOo ( I1i1i1iii , OooOoOo , iIIIII1I )
 if 2 - 2: O0OoO - o0o00Oo0O - Ii1I / iI1iI1I1i1I * OOooOOo
elif i1iIIi1II1iiI == 49 :
 ooO0oO00O0o ( )
 if 26 - 26: Ii1I + IIIi - OoOo00o + OooO0OoOOOO % IIIii1II1II
elif i1iIIi1II1iiI == 222 :
 o000ooooO0o ( OooOoOo )
 if 84 - 84: iI1iI1I1i1I % Ii11Ii1I % o0o00Oo0O * I11i
elif i1iIIi1II1iiI == 333 :
 IiI1iI1I1 ( OooOoOo )
 if 15 - 15: OoOo00o - iI11I1II1I1I - IIiIiII11i - OooO0OoOOOO % Ii1I
 if 80 - 80: OooO0OoOOOO * o0oOO0O00o0O . ooOoO0O00 % Ii11Ii1I % Ii1I + O0OoO
elif i1iIIi1II1iiI == 1020 :
 OO0000 ( )
 if 6 - 6: Ii1I . OoOo00o . oO0o + OooO0OoOOOO
elif i1iIIi1II1iiI == 1021 :
 ANIMEEP ( )
 if 65 - 65: Ii1I / O0OoO
elif i1iIIi1II1iiI == 1022 :
 ANIMEPLAY ( OooOoOo )
 if 23 - 23: IIIii1II1II / IIIii1II1II * I11i * IIIii1II1II
elif i1iIIi1II1iiI == 1001 :
 Oo0OoOOoo ( )
 if 57 - 57: o0oOO0O00o0O
elif i1iIIi1II1iiI == 1005 :
 I1IIiIi1I1I1 ( )
 if 29 - 29: oOo0O0Ooo
elif i1iIIi1II1iiI == 1007 :
 IIi1iI11Ii ( OooOoOo )
 if 41 - 41: IIIi * oO0o - o0oOO0O00o0O . Ii11Ii1I
elif i1iIIi1II1iiI == 1010 :
 OOOo0Ooo0 ( OooOoOo )
 if 41 - 41: iI11I1II1I1I - o0o00Oo0O - Ii1I - OoOo00o + IIIi
elif i1iIIi1II1iiI == 1011 :
 III1 ( OooOoOo )
 if 22 - 22: o0o00Oo0O % OooO0OoOOOO % o0oOO0O00o0O % oOo0O0Ooo
elif i1iIIi1II1iiI == 1030 :
 IIi1iI1i ( )
 if 34 - 34: o0oOO0O00o0O . I1ii11iIi11i % Ii1I . o0oOO0O00o0O % OooO0OoOOOO / OooO0OoOOOO
elif i1iIIi1II1iiI == 1031 :
 Iii11II1 ( OooOoOo , OOOOO0O00 )
 if 84 - 84: Ii11Ii1I
elif i1iIIi1II1iiI == 1006 :
 Parse . ParseURL ( OooOoOo )
 if 1 - 1: OoOo00o - I1ii11iIi11i * iI11I1II1I1I * I1ii11iIi11i * ooOoO0O00
elif i1iIIi1II1iiI == 2030 :
 Parse . addonParseURL ( OooOoOo )
 if 9 - 9: o0oOO0O00o0O - o0oOO0O00o0O
elif i1iIIi1II1iiI == 2031 :
 Parse . apkParseURL ( OooOoOo )
 if 3 - 3: o0o00Oo0O + o0o00Oo0O - o0o00Oo0O - o0o00Oo0O % ii + OoOo00o
elif i1iIIi1II1iiI == 1002 :
 iiIII1i1 ( OooOoOo )
 if 20 - 20: oO0o + iI1iI1I1i1I . IIiIiII11i / Ii
elif i1iIIi1II1iiI == 1003 :
 oOOo0OOoOO0 ( OooOoOo , OOOOO0O00 )
 if 50 - 50: ii / oO0o % iI11I1II1I1I
elif i1iIIi1II1iiI == 1004 :
 IiIiIIi1IiiIi1III ( OooOoOo )
 if 41 - 41: Ii1I % Ii1I + OooO0OoOOOO . o0oOO0O00o0O % IIIi * O0OoO
elif i1iIIi1II1iiI == 1008 :
 Ii1I1Iiii ( )
 if 57 - 57: Ii11Ii1I . IIIi . IIiIiII11i % ii * o0o00Oo0O + iI11I1II1I1I
elif i1iIIi1II1iiI == 1009 :
 M3UPLAY ( OooOoOo )
 if 94 - 94: ooOoO0O00 * oO0o * OOooOOo
elif i1iIIi1II1iiI == 2001 :
 iiIIiii1iii1I ( OooOoOo )
 if 93 - 93: O0OoO / IIIii1II1II * o0o00Oo0O
elif i1iIIi1II1iiI == 1013 :
 I1Ii11iiiI ( )
 if 17 - 17: oO0o / O0OoO % oOo0O0Ooo
elif i1iIIi1II1iiI == 1014 :
 iiIiI11IiI1ii ( )
 if 47 - 47: I1ii11iIi11i * oO0o / I11i * oOo0O0Ooo
elif i1iIIi1II1iiI == 1015 :
 ooO0O0 ( OooOoOo )
 if 60 - 60: Ii1I / OooO0OoOOOO . Ii / oO0o % IIiIiII11i
elif i1iIIi1II1iiI == 1016 :
 I1111III111ii ( OooOoOo , OOOOO0O00 , I1i1i1iii )
 if 6 - 6: o0oOO0O00o0O % I11i + IIIi
elif i1iIIi1II1iiI == 1023 :
 I1iii ( )
 if 91 - 91: I11i + o0o00Oo0O * OoOo00o * OooO0OoOOOO * Ii1I
elif i1iIIi1II1iiI == 1024 :
 O00OOOo ( )
 if 83 - 83: ii
elif i1iIIi1II1iiI == 1025 :
 i1iI11Ii1i ( OooOoOo )
 if 52 - 52: I11i / OOooOOo % OoOo00o % oO0o / OooO0OoOOOO % I11i
elif i1iIIi1II1iiI == 4001 :
 OOooOoooOoOo ( )
 if 88 - 88: IIIii1II1II / Ii / Ii11Ii1I / Ii * Ii1I % iI1iI1I1i1I
elif i1iIIi1II1iiI == 4002 :
 o0OOOO00O0Oo ( )
 if 43 - 43: OOooOOo * oO0o % ooOoO0O00 * Ii11Ii1I + iI11I1II1I1I
elif i1iIIi1II1iiI == 4003 :
 O0Oo00 ( )
 if 80 - 80: I11i . o0oOO0O00o0O . ii
elif i1iIIi1II1iiI == 4004 :
 OO ( )
 if 63 - 63: O0OoO . IIIii1II1II
elif i1iIIi1II1iiI == 4005 :
 I11iiI1i1 ( )
 if 66 - 66: oOo0O0Ooo
elif i1iIIi1II1iiI == 4006 :
 I1i1Iiiii ( )
 if 99 - 99: oO0o % o0o00Oo0O . IIIi - Ii1I . I1ii11iIi11i / OOooOOo
elif i1iIIi1II1iiI == 4007 :
 o0iI11I1II ( )
 if 60 - 60: Ii1I
elif i1iIIi1II1iiI == 4008 :
 Ii1IIiI1i ( )
 if 78 - 78: OoOo00o + IIiIiII11i
elif i1iIIi1II1iiI == 4009 : iIiIIi1 ( )
elif i1iIIi1II1iiI == 4010 : iiIi1iI1iIii ( )
elif i1iIIi1II1iiI == 3000 :
 I1IIIIiiI1i1 ( )
 if 55 - 55: ii
elif i1iIIi1II1iiI == 3001 :
 i1II11IiiiI ( )
 if 90 - 90: oOo0O0Ooo
elif i1iIIi1II1iiI == 3002 :
 IIIiIi1iiI1 ( OooOoOo )
 if 4 - 4: IIIii1II1II % O0OoO - IIIii1II1II - I11i
elif i1iIIi1II1iiI == 3003 :
 o0ooOOoO0oO0 ( OooOoOo )
 if 30 - 30: OooO0OoOOOO
elif i1iIIi1II1iiI == 3004 :
 oooo ( OooOoOo )
 if 34 - 34: OoOo00o - IIiIiII11i - I11i + o0oOO0O00o0O + IIIi
elif i1iIIi1II1iiI == 404 :
 II1I11 ( I1i1i1iii , OooOoOo , OOOOO0O00 )
 if 70 - 70: ii + oO0o * I1ii11iIi11i
elif i1iIIi1II1iiI == 405 :
 I1Iii ( OooOoOo )
 if 20 - 20: Ii - IIiIiII11i - O0OoO % OoOo00o . O0OoO
elif i1iIIi1II1iiI == 7030 :
 IiiiO0oo0ooo0 ( )
 if 50 - 50: iI11I1II1I1I + IIIi - iI1iI1I1i1I - ii
elif i1iIIi1II1iiI == 7021 :
 i1Ii1 ( I1i1i1iii )
 if 84 - 84: OOooOOo - iI1iI1I1i1I
elif i1iIIi1II1iiI == 7022 :
 OO0 ( I1i1i1iii )
 if 80 - 80: Ii % IIIii1II1II - I1ii11iIi11i % IIIii1II1II
elif i1iIIi1II1iiI == 7000 :
 iiiiIii11i1 ( I1i1i1iii , OooOoOo , img )
 if 89 - 89: Ii11Ii1I * iI1iI1I1i1I + OOooOOo / Ii
elif i1iIIi1II1iiI == 7050 :
 iI11I ( OooOoOo )
 if 68 - 68: ii * iI1iI1I1i1I
elif i1iIIi1II1iiI == 7051 :
 oooo0O0Oooo ( OooOoOo )
 if 86 - 86: I11i / OOooOOo
elif i1iIIi1II1iiI == 7052 :
 OOo0OOOoOOo ( OooOoOo )
 if 40 - 40: o0oOO0O00o0O
elif i1iIIi1II1iiI == 7053 :
 III ( OooOoOo )
 if 62 - 62: O0OoO / IIIii1II1II
elif i1iIIi1II1iiI == 7054 :
 CoolPlay ( OooOoOo )
 if 74 - 74: o0oOO0O00o0O % IIIi / IIIi - iI11I1II1I1I - IIiIiII11i + IIIii1II1II
elif i1iIIi1II1iiI == 7060 :
 Ii1111iiI ( )
 if 92 - 92: iI1iI1I1i1I % IIIi
elif i1iIIi1II1iiI == 7061 :
 o0OO ( OooOoOo )
 if 18 - 18: O0OoO + IIIi / IIIii1II1II / OoOo00o + iI11I1II1I1I % OooO0OoOOOO
elif i1iIIi1II1iiI == 7063 :
 I1I ( OooOoOo )
 if 94 - 94: iI1iI1I1i1I
elif i1iIIi1II1iiI == 7062 :
 i1I111iIii1i1 ( OooOoOo )
 if 37 - 37: OoOo00o
elif i1iIIi1II1iiI == 7064 :
 NATatozcat ( )
 if 52 - 52: Ii1I * oOo0O0Ooo . IIIii1II1II + ooOoO0O00 % OoOo00o / iI11I1II1I1I
elif i1iIIi1II1iiI == 7067 :
 III11i1iI11 ( OooOoOo )
 if 68 - 68: IIIi - OOooOOo . Ii + I11i
elif i1iIIi1II1iiI == 7066 :
 NATatozA ( OooOoOo )
 if 71 - 71: Ii / ooOoO0O00 * oOo0O0Ooo / OOooOOo
elif i1iIIi1II1iiI == 7065 :
 o0o0OOo0O ( OooOoOo )
 if 33 - 33: iI1iI1I1i1I . I1ii11iIi11i
elif i1iIIi1II1iiI == 7070 :
 oo0O0oOOO0o ( )
 if 89 - 89: o0oOO0O00o0O + ooOoO0O00 - OooO0OoOOOO + O0OoO . IIiIiII11i
elif i1iIIi1II1iiI == 7071 :
 DIZIlist ( OooOoOo )
 if 85 - 85: iI11I1II1I1I - Ii11Ii1I * I1ii11iIi11i . OoOo00o + IIIi
elif i1iIIi1II1iiI == 7072 :
 DIZIpull ( OooOoOo )
 if 13 - 13: o0o00Oo0O + iI11I1II1I1I % IIiIiII11i + iI11I1II1I1I
elif i1iIIi1II1iiI == 7073 :
 WATCHDIZI ( OooOoOo )
 if 85 - 85: oOo0O0Ooo * iI11I1II1I1I . o0oOO0O00o0O / o0oOO0O00o0O
elif i1iIIi1II1iiI == 7002 :
 o0oo0OOOO ( )
 if 43 - 43: oOo0O0Ooo
elif i1iIIi1II1iiI == 7003 :
 O0Oo0oo0O0O0o ( OooOoOo )
 if 78 - 78: oO0o % IIiIiII11i + OOooOOo / oOo0O0Ooo
elif i1iIIi1II1iiI == 7004 :
 Ii1I1iIiiI1 ( OooOoOo )
 if 34 - 34: I11i % Ii1I + Ii11Ii1I * iI1iI1I1i1I / OoOo00o
elif i1iIIi1II1iiI == 7020 :
 OOooooO ( OooOoOo )
 if 18 - 18: O0OoO
elif i1iIIi1II1iiI == 7001 :
 oo0O0OO0Oo ( )
 if 92 - 92: oO0o % iI11I1II1I1I / OooO0OoOOOO * o0oOO0O00o0O . ooOoO0O00 + OoOo00o
elif i1iIIi1II1iiI == 7010 :
 iI11Iii1I ( OooOoOo )
 if 24 - 24: OooO0OoOOOO . o0oOO0O00o0O * OooO0OoOOOO % Ii . Ii + ooOoO0O00
elif i1iIIi1II1iiI == 7011 :
 o0OoOo0o0O00 ( OooOoOo )
 if 64 - 64: iI11I1II1I1I / OooO0OoOOOO / I1ii11iIi11i - Ii1I
elif i1iIIi1II1iiI == 7012 :
 o00O ( OooOoOo )
 if 100 - 100: OooO0OoOOOO + ooOoO0O00 * oO0o
elif i1iIIi1II1iiI == 7013 :
 cnfTVPlay2 ( OooOoOo )
elif i1iIIi1II1iiI == 7014 :
 CNF_Studio_Indexer . MV_Movies ( OooOoOo )
elif i1iIIi1II1iiI == 7015 :
 CNF_Studio_Indexer . Movie_ByYear ( OooOoOo )
elif i1iIIi1II1iiI == 7016 :
 CNF_Studio_Indexer . Resolve_CNF_Link ( I1i1i1iii , OooOoOo , OOOOO0O00 )
elif i1iIIi1II1iiI == 7017 :
 CNF_Studio_Indexer . Search_Movie ( )
elif i1iIIi1II1iiI == 7018 :
 IiiII ( )
elif i1iIIi1II1iiI == 7019 :
 CNF_Studio_Indexer . List_Movies ( OooOoOo )
elif i1iIIi1II1iiI == 7020 :
 CNF_Studio_Indexer . Get_Movie_Page ( OooOoOo )
elif i1iIIi1II1iiI == 7024 :
 CNF_Studio_Indexer . Box_Office ( OooOoOo )
 if 64 - 64: OoOo00o * Ii . I1ii11iIi11i
elif i1iIIi1II1iiI == 8000 :
 I11ii1iI11 ( )
elif i1iIIi1II1iiI == 8001 :
 OoOooO ( )
elif i1iIIi1II1iiI == 8002 :
 IIoOoo0OO0 ( )
elif i1iIIi1II1iiI == 8003 :
 ii1iIII1ii ( )
elif i1iIIi1II1iiI == 8004 :
 O0O00O0Oo0 ( )
elif i1iIIi1II1iiI == 8005 :
 oo0OooO ( )
elif i1iIIi1II1iiI == 8006 :
 OO0o0o0oo ( I1i1i1iii , OooOoOo )
elif i1iIIi1II1iiI == 8030 :
 Ii1i1i1111 ( OooOoOo )
elif i1iIIi1II1iiI == 8045 :
 ooiiI1ii ( OooOoOo )
elif i1iIIi1II1iiI == 8046 :
 O0OooOO ( OooOoOo )
elif i1iIIi1II1iiI == 8047 :
 IiIiIi1I11I ( OooOoOo )
elif i1iIIi1II1iiI == 8020 :
 oOOo00ooO ( )
elif i1iIIi1II1iiI == 8021 :
 ooOo ( OooOoOo )
elif i1iIIi1II1iiI == 8022 :
 OOOoOo0oO0OoO ( OooOoOo )
elif i1iIIi1II1iiI == 8023 :
 I1 ( OooOoOo )
elif i1iIIi1II1iiI == 8040 :
 iIIi1IiIi ( )
elif i1iIIi1II1iiI == 8041 :
 III1i ( OooOoOo )
elif i1iIIi1II1iiI == 8042 :
 II111I1Iii ( OooOoOo )
elif i1iIIi1II1iiI == 8043 :
 yt . PlayVideo ( OooOoOo )
elif i1iIIi1II1iiI == 8044 :
 OO00Oo00oO ( OooOoOo )
elif i1iIIi1II1iiI == 8060 :
 ii11 ( )
elif i1iIIi1II1iiI == 8061 :
 Ii11 ( OooOoOo )
elif i1iIIi1II1iiI == 8064 :
 O0oo00oOOO0o ( )
elif i1iIIi1II1iiI == 8065 :
 II1iI111iiIIiI1I ( OooOoOo )
elif i1iIIi1II1iiI == 8070 :
 i1Iiii ( )
elif i1iIIi1II1iiI == 8071 :
 o0O0O ( OooOoOo )
elif i1iIIi1II1iiI == 7080 :
 oOO ( OooOoOo )
elif i1iIIi1II1iiI == 8090 :
 OOooO0Oo0o000 ( )
elif i1iIIi1II1iiI == 8091 :
 iiiIii ( OooOoOo )
elif i1iIIi1II1iiI == 8092 :
 OoOiIIi1 ( OooOoOo )
elif i1iIIi1II1iiI == 8081 :
 OooIIi111 ( )
elif i1iIIi1II1iiI == 8062 :
 I1I1O0O ( OooOoOo )
elif i1iIIi1II1iiI == 8063 :
 OOo00Oooo ( OooOoOo )
elif i1iIIi1II1iiI == 8050 :
 II1iiIiIiI ( )
elif i1iIIi1II1iiI == 8051 :
 iIIi1I1ii ( OooOoOo )
elif i1iIIi1II1iiI == 8052 :
 Iiii ( OooOoOo )
elif i1iIIi1II1iiI == 8085 :
 o0O0oOO0Oooo ( )
elif i1iIIi1II1iiI == 8086 :
 ii11Iiii ( OooOoOo )
elif i1iIIi1II1iiI == 8087 :
 iiI111 ( OooOoOo )
elif i1iIIi1II1iiI == 8088 :
 OOoooo0oo ( OooOoOo , I1i1i1iii )
elif i1iIIi1II1iiI == 9000 :
 OOoOoo0 ( )
elif i1iIIi1II1iiI == 1111 :
 oOOOo ( )
elif i1iIIi1II1iiI == 9001 :
 IiiiI1i1I ( )
elif i1iIIi1II1iiI == 9002 :
 o0OO0OO000OO ( )
elif i1iIIi1II1iiI == 9003 :
 II1io0Oo00oOO ( )
elif i1iIIi1II1iiI == 50 :
 I11I1IIiiII1 ( OooOoOo )
elif i1iIIi1II1iiI == 9020 :
 champlist ( )
elif i1iIIi1II1iiI == 9021 :
 iiiIIiii11I1 ( )
elif i1iIIi1II1iiI == 9022 :
 oo0O ( )
elif i1iIIi1II1iiI == 9023 :
 Ooooo0O0 ( )
elif i1iIIi1II1iiI == 9024 :
 I111Ii11i11I ( OooOoOo )
elif i1iIIi1II1iiI == 9030 :
 i1ooO ( OooOoOo )
elif i1iIIi1II1iiI == 9031 :
 i11iii1Ii1 ( OooOoOo )
elif i1iIIi1II1iiI == 9032 :
 o0oO0iiiiI1Iii ( OooOoOo )
elif i1iIIi1II1iiI == 9033 :
 I1I111IIIi1 ( OooOoOo )
elif i1iIIi1II1iiI == 7085 :
 oOII11i1I ( OooOoOo )
elif i1iIIi1II1iiI == 7086 :
 IiIiIi ( OooOoOo )
elif i1iIIi1II1iiI == 7087 :
 O0OoOo ( iIIIII1I )
elif i1iIIi1II1iiI == 9666 :
 iI11ii ( OooOoOo )
elif i1iIIi1II1iiI == 10100 : iiII ( )
elif i1iIIi1II1iiI == 10105 : ooOOO00oOOooO ( OooOoOo )
elif i1iIIi1II1iiI == 10106 : IiiIIi ( OooOoOo )
elif i1iIIi1II1iiI == 10104 : II111I1 ( OooOoOo )
elif i1iIIi1II1iiI == 10107 : I11II1i1 ( )
elif i1iIIi1II1iiI == 10103 : O0000Oo ( OooOoOo )
elif i1iIIi1II1iiI == 10108 : iIi11I11 ( OooOoOo )
elif i1iIIi1II1iiI == 10107 : I11II1i1 ( )
elif i1iIIi1II1iiI == 10000 : Origin_Menu ( )
elif i1iIIi1II1iiI == 10001 : o0O0 ( )
elif i1iIIi1II1iiI == 10002 : IIiii11ii1i ( )
elif i1iIIi1II1iiI == 10003 : oo0o ( )
elif i1iIIi1II1iiI == 10004 : OO0o0OO0 ( OooOoOo )
elif i1iIIi1II1iiI == 10005 : oOoOo ( )
elif i1iIIi1II1iiI == 10006 : III1i111i ( OooOoOo )
elif i1iIIi1II1iiI == 10007 : ooOoOO ( OooOoOo , OOOOO0O00 )
elif i1iIIi1II1iiI == 10008 : IiiI11I1IIiI ( )
elif i1iIIi1II1iiI == 10009 : Ii11iiI1 ( )
elif i1iIIi1II1iiI == 10010 : OoooO0 ( OooOoOo )
elif i1iIIi1II1iiI == 10011 : o0o0OoO0OOO0 ( OooOoOo )
elif i1iIIi1II1iiI == 10012 : o0oOOo0O0O000 ( OooOoOo )
elif i1iIIi1II1iiI == 10013 : O0O00OoOoOOo ( OooOoOo )
elif i1iIIi1II1iiI == 10014 : iIiIi1ii ( )
elif i1iIIi1II1iiI == 10015 : O0oo0O ( )
elif i1iIIi1II1iiI == 10016 : ooOO ( OooOoOo )
elif i1iIIi1II1iiI == 10017 : o0OO0O00o ( )
elif i1iIIi1II1iiI == 10018 : OOOO0oOo00O ( )
elif i1iIIi1II1iiI == 10019 : Iiii1i11ii1Ii ( )
elif i1iIIi1II1iiI == 10020 : OoOoO0oOOooo ( )
elif i1iIIi1II1iiI == 10021 : IIIIIIi1i ( )
elif i1iIIi1II1iiI == 10022 : oOOoO ( OooOoOo )
elif i1iIIi1II1iiI == 10023 : IIIIII111Ii ( I1i1i1iii , OooOoOo )
elif i1iIIi1II1iiI == 10024 : I1ii1 ( OooOoOo )
elif i1iIIi1II1iiI == 10025 : iIii11iI1II ( )
elif i1iIIi1II1iiI == 10026 : ooO ( )
elif i1iIIi1II1iiI == 10027 : Iii1Ii ( )
elif i1iIIi1II1iiI == 10028 : OOoOoo00Oo ( )
elif i1iIIi1II1iiI == 10029 : OOoO0oO00o ( )
elif i1iIIi1II1iiI == 423 : o0i1I11iI1iiI ( OooOoOo )
elif i1iIIi1II1iiI == 426 : iii1OO0o0oO0O000o ( OooOoOo )
elif i1iIIi1II1iiI == 10030 : Izle_Films ( )
elif i1iIIi1II1iiI == 10031 : Latest_Izle_Movies ( )
elif i1iIIi1II1iiI == 10032 : Izle_Genres ( )
elif i1iIIi1II1iiI == 10033 : Izle_Pop_Movies ( )
elif i1iIIi1II1iiI == 10034 : Izle_Boxsets ( )
elif i1iIIi1II1iiI == 10035 : Izle_Search ( )
elif i1iIIi1II1iiI == 10036 : Izle_Genres_Movie ( OooOoOo )
elif i1iIIi1II1iiI == 10037 : Izle_Boxset_single ( OooOoOo )
elif i1iIIi1II1iiI == 10038 : Izle_IFRAME ( )
elif i1iIIi1II1iiI == 10039 : Izle_Boxsets_Next ( OooOoOo )
elif i1iIIi1II1iiI == 10040 : Oo0oO00 ( )
elif i1iIIi1II1iiI == 10041 : III1III11II ( OooOoOo )
elif i1iIIi1II1iiI == 10042 : OO00oo ( OooOoOo )
elif i1iIIi1II1iiI == 10043 : O0Oooo ( )
elif i1iIIi1II1iiI == 10044 : iiIIIiI1Ii ( OooOoOo )
elif i1iIIi1II1iiI == 10045 : oOo0 ( I1i1i1iii )
elif i1iIIi1II1iiI == 10046 : oo00o0 ( OooOoOo )
elif i1iIIi1II1iiI == 10047 : i1IoOOoooO0O0 ( OooOoOo )
elif i1iIIi1II1iiI == 10048 : I111iiiii1 ( OooOoOo )
elif i1iIIi1II1iiI == 10049 : o00ooOoo ( OooOoOo )
elif i1iIIi1II1iiI == 10050 : iIiiII1Ii1ii ( )
elif i1iIIi1II1iiI == 10051 : o0000oO ( )
elif i1iIIi1II1iiI == 10052 : I1i ( )
elif i1iIIi1II1iiI == 10053 : Addon ( OooOoOo )
elif i1iIIi1II1iiI == 10054 : i1IoOo000Oo00o ( OooOoOo , I1i1i1iii )
elif i1iIIi1II1iiI == 10055 :
 i1I1i1i ( "addFavorite" )
 try :
  I1i1i1iii = I1i1i1iii . split ( '\\ ' ) [ 1 ]
 except :
  pass
 try :
  I1i1i1iii = I1i1i1iii . split ( '  - ' ) [ 0 ]
 except :
  pass
 ii11IiI1 ( I1i1i1iii , OooOoOo , OOOOO0O00 , Iii , I1I11i )
elif i1iIIi1II1iiI == 10056 :
 i1I1i1i ( "rmFavorite" )
 try :
  I1i1i1iii = I1i1i1iii . split ( '\\ ' ) [ 1 ]
 except :
  pass
 try :
  I1i1i1iii = I1i1i1iii . split ( '  - ' ) [ 0 ]
 except :
  pass
 O0o0OO00 ( I1i1i1iii )
elif i1iIIi1II1iiI == 10057 :
 i1I1i1i ( "getFavorites" )
 ii11i11 ( )
elif i1iIIi1II1iiI == 10058 : Oo00000o0o ( )
elif i1iIIi1II1iiI == 10059 : Donators_Guide ( )
elif i1iIIi1II1iiI == 10060 : i1OO0oOOoo ( )
elif i1iIIi1II1iiI == 10061 : Oooo00 ( )
elif i1iIIi1II1iiI == 10062 : OOo ( I1i1i1iii , OooOoOo , iIIIII1I )
elif i1iIIi1II1iiI == 10063 : OooO0oo ( )
elif i1iIIi1II1iiI == 10064 : iI1I ( )
elif i1iIIi1II1iiI == 10065 : I11i1II ( OooOoOo )
elif i1iIIi1II1iiI == 10066 : ooOOoO ( OooOoOo )
elif i1iIIi1II1iiI == 10068 : IIiI1Ii ( OooOoOo )
elif i1iIIi1II1iiI == 10069 : ii111I ( OooOoOo )
elif i1iIIi1II1iiI == 10070 : i1Ii1i1I11Iii ( OooOoOo )
elif i1iIIi1II1iiI == 10071 : Genie_Watch ( )
elif i1iIIi1II1iiI == 10072 : o0o ( )
elif i1iIIi1II1iiI == 10073 : I1iiii1I ( OooOoOo )
elif i1iIIi1II1iiI == 10074 : IIOOO0O00O0OOOO ( OooOoOo )
elif i1iIIi1II1iiI == 10075 : o0O ( OOOOO0O00 , I1i1i1iii , OooOoOo )
elif i1iIIi1II1iiI == 10076 : O0O0o0oOOO ( OooOoOo )
elif i1iIIi1II1iiI == 10077 : IiI1iiiIii ( OooOoOo )
elif i1iIIi1II1iiI == 10078 : oOOOoo00 ( )
elif i1iIIi1II1iiI == 10079 : Genie_Watch_Tv_Shows ( )
elif i1iIIi1II1iiI == 10080 : Genie_Watch_Tv_Genre ( OooOoOo )
elif i1iIIi1II1iiI == 10081 : Genie_Watch_TV_PlayRun ( OooOoOo )
elif i1iIIi1II1iiI == 10082 : Genie_Watch_TV_Episodes ( OooOoOo , OOOOO0O00 )
elif i1iIIi1II1iiI == 10083 : Genie_Watch_Tv_Recent ( OooOoOo )
elif i1iIIi1II1iiI == 10084 : oO0O0OO0O ( )
elif i1iIIi1II1iiI == 10085 : ooo00OOOooO ( )
elif i1iIIi1II1iiI == 10086 : ooOOO00Ooo ( )
elif i1iIIi1II1iiI == 20000 : II1i ( )
elif i1iIIi1II1iiI == 20001 : I1Iii1iI1 ( )
elif i1iIIi1II1iiI == 20002 : O0o0oOooOoOo ( OooOoOo )
elif i1iIIi1II1iiI == 20003 : ooOo0O0o0 ( OooOoOo )
elif i1iIIi1II1iiI == 20004 : iIi1I1 ( OooOoOo )
elif i1iIIi1II1iiI == 21004 : OO0ooo0o0 ( )
elif i1iIIi1II1iiI == 21005 : oO0ooOoO ( OooOoOo )
elif i1iIIi1II1iiI == 21006 : O0Ooo ( OooOoOo )
elif i1iIIi1II1iiI == 21007 : iIiI1 ( OooOoOo )
elif i1iIIi1II1iiI == 30000 : IIII1ii ( )
elif i1iIIi1II1iiI == 30001 : OOOOOoOO0OOoo ( )
elif i1iIIi1II1iiI == 10012 : Resolve ( OooOoOo )
elif i1iIIi1II1iiI == 30003 : IIIIIIIiI ( )
elif i1iIIi1II1iiI == 30004 : i1i1IiIiIi1Ii ( OooOoOo )
elif i1iIIi1II1iiI == 30005 : i1I ( OooOoOo )
elif i1iIIi1II1iiI == 30006 : I1I1 ( )
elif i1iIIi1II1iiI == 30007 : ii1IiIi11 ( )
elif i1iIIi1II1iiI == 30008 : IiiiI1 ( OooOoOo )
elif i1iIIi1II1iiI == 30009 : o0Oii1111i ( OooOoOo )
elif i1iIIi1II1iiI == 30010 : OoOO ( OooOoOo )
elif i1iIIi1II1iiI == 30011 : oO0oooooo ( )
elif i1iIIi1II1iiI == 30012 : Ooo0O0 ( )
elif i1iIIi1II1iiI == 30013 : ooO0o ( )
elif i1iIIi1II1iiI == 30014 : IiI1 ( )
if 52 - 52: I1ii11iIi11i / O0OoO / o0oOO0O00o0O - I11i / o0oOO0O00o0O
xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
