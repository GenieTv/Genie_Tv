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
import buggalo
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
O00ooOO = "2.6.12"
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
ooOoOoo0O = 'http://'
OooO0 = base64 . decodestring ( 'LnBocA==' )
II11iiii1Ii = base64 . decodestring ( 'aHR0cDovL2JhY2syYmFzaWNzYnVpbGQuY28udWsvdGVzdC8=' )
OO0o = [ ]
Ooo = o0oO0 . getLocalizedString
O0o0Oo = CookieJar ( )
Oo00OOOOO = urllib2 . build_opener ( urllib2 . HTTPCookieProcessor ( O0o0Oo ) )
Oo00OOOOO . addheaders = [ ( 'User-Agent' , 'Mozilla/5.0' ) ]
O0O = int ( sys . argv [ 1 ] )
O00o0OO = xbmc . translatePath ( o0oO0 . getAddonInfo ( 'profile' ) . decode ( 'utf-8' ) )
I11i1 = os . path . join ( O00o0OO , 'favorites' )
iIi1ii1I1 = iIii1 + '/addons.ini'
o0 = xbmc . translatePath ( 'special://home/userdata/' )
I11II1i = xbmc . translatePath ( 'special://home/userdatabroke/' )
IIIII = ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9QYW5zQm94L09SSUdJTlMv' ) )
ooooooO0oo = xbmc . translatePath ( os . path . join ( 'special://home/userdata/addon_data/script.ivueguide/master.db' ) )
IIiiiiiiIi1I1 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , 'favourites.xml' ) )
I1IIIii = xbmc . translatePath ( os . path . join ( 'special://home/userdata/addon_data/plugin.video.GenieTv/favorites' ) )
if os . path . exists ( I11i1 ) == True :
 oOoOooOo0o0 = open ( I11i1 ) . read ( )
else : oOoOooOo0o0 = [ ]
OOOO = o0oO0 . getSetting ( 'debug' )
if os . path . exists ( iIii1 ) == False :
 os . makedirs ( iIii1 )
 if 87 - 87: O0ooOooooO / i1I111II1I - Oooo0Ooo000 - iI - i1I111ii1II1i / OoOo00o
def o0OOoo0OO0OOO ( ) :
 if not os . path . exists ( I1iII1iiII ) :
  oOOoo00O0O . ok ( "[COLOR=white]Incompatible[/COLOR]" , "Unfortunately GenieTv will only work with" , 'its official repo please install from trusted source' , '' )
  iI1iI1I1i1I = 'genie tv repo not being installed '
  iIi11Ii1 ( iI1iI1I1i1I )
 Ii11iII1 ( )
 Oo0O0O0ooO0O ( )
 if o0oO0 . getSetting ( 'My Build' ) == 'true' :
  IIIIii ( '[COLORgreen]WIZARD[/COLOR]' , iiI1IiI , 4001 , ii11iIi1I + 'MB.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Streams' ) == 'true' :
  IIIIii ( '[COLORgreen]STREAMS[/COLOR]' , iiI1IiI , 4002 , ii11iIi1I + 'streams.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Music' ) == 'true' :
  IIIIii ( '[COLORgreen]Music[/COLOR]' , iiI1IiI , 4003 , ii11iIi1I + 'MUSIC.png' , i1iiIII111ii , '' )
  if 70 - 70: o00OO00OoO / OOO0OOo - OOO0OOo + OOOo0
 if o0oO0 . getSetting ( 'Builders Toolbox' ) == 'true' :
  IIIIii ( '[COLORgreen]BUILDERS TOOLBOX[/COLOR]' , iiI1IiI , 32 , ii11iIi1I + 'builderstoolbox.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Source List' ) == 'true' :
  IIIIii ( '[COLORgreen]SOURCE LIST[/COLOR]' , iiI1IiI , 46 , ii11iIi1I + 'sources.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Maintainance' ) == 'true' :
  IIIIii ( '[COLORgreen]MAINTENANCE[/COLOR]' , iiI1IiI , 3 , ii11iIi1I + 'MAIN6.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Addons' ) == 'true' :
  IIIIii ( '[COLORgreen]ADDONS[/COLOR]' , '' , 10050 , ii11iIi1I + 'ADDONS.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'APK Tool' ) == 'true' :
  IIIIii ( '[COLORgreen]APK TOOL[/COLOR]' , iiI1IiI , 2 , ii11iIi1I + 'APK.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Rss Feed' ) == 'true' :
  IIIIii ( '[COLORgreen]GenieTv RSS Feed[/COLOR]' , iiI1IiI , 39 , ii11iIi1I + 'RSS.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Addons Packs' ) == 'true' :
  IIIIii ( '[COLORgreen]ADDONS PACKS[/COLOR]' , iiI1IiI , 30 , ii11iIi1I + 'ADDONP.png' , i1iiIII111ii , '' )
 O00Oo000ooO0 ( 'movies' , 'MAIN' )
 if 100 - 100: O0 + OoOo00o - i1I111II1I + i11iIiiIii * iI
def iII ( ) :
 IIIIii ( '[COLORgreen]BACKUP MY BUILD[/COLOR]' , iiI1IiI , 10060 , ii11iIi1I + 'MB.png' , i1iiIII111ii , '' )
 IIIIii ( '[COLORgreen]RESTORE MY BUILD[/COLOR]' , iiI1IiI , 49 , ii11iIi1I + 'MB.png' , i1iiIII111ii , '' )
 IIIIii ( '[COLORgreen]WIPE GENIE[/COLOR]' , iiI1IiI , 41 , ii11iIi1I + 'wipegenie.png' , i1iiIII111ii , '' )
 IIIIii ( '[COLORgreen]WISHES PC[/COLOR]' , iiI1IiI , 1 , ii11iIi1I + 'WISHESPC.png' , i1iiIII111ii , '' )
 IIIIii ( '[COLORgreen]WISHES ANDROID[/COLOR]' , iiI1IiI , 44 , ii11iIi1I + 'WISHESAN.png' , i1iiIII111ii , '' )
 O00Oo000ooO0 ( 'movies' , 'MAIN' )
def o0ooOooo000oOO ( ) :
 if oO == '5knuckleshuffle' :
  IIIIii ( '[COLORgreen]XVID[/COLOR]' , iiI1IiI , 10100 , ii11iIi1I + 'JIZBOX.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Favourites' ) == 'true' :
  IIIIii ( '[COLORgreen]FAVOURITES[/COLOR]' , iiI1IiI , 10057 , ii11iIi1I + 'FAVORITES.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Search' ) == 'true' :
  IIIIii ( '[COLORgreen]SEARCH[/COLOR]' , iiI1IiI , 9000 , ii11iIi1I + 'search.png' , i1iiIII111ii , '' )
 IIIIii ( '[COLORgreen]Live TV[/COLOR]' , iiI1IiI , 4009 , ii11iIi1I + 'GTVIPTV.png' , i1iiIII111ii , '' )
 IIIIii ( '[COLORgreen]MOVIES[/COLOR]' , iiI1IiI , 4004 , ii11iIi1I + 'MOVIESv.png' , i1iiIII111ii , '' )
 IIIIii ( '[COLORgreen]TV SHOWS[/COLOR]' , iiI1IiI , 4005 , ii11iIi1I + 'TVSHOWSv.png' , i1iiIII111ii , '' )
 IIIIii ( '[COLORgreen]STREAM TEAM[/COLOR]' , iiI1IiI , 4006 , ii11iIi1I + 'streamteam.png' , i1iiIII111ii , '' )
 IIIIii ( '[COLORgreen]KIDS[/COLOR]' , iiI1IiI , 4007 , ii11iIi1I + 'KIDSv.png' , i1iiIII111ii , '' )
 IIIIii ( '[COLORgreen]HOBBIES[/COLOR]' , iiI1IiI , 4008 , ii11iIi1I + 'hobbies.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'YOUTUBE' ) == 'true' :
  IIIIii ( '[COLORgreen]SEARCH YOUTUBE[/COLOR]' , iiI1IiI , 10064 , ii11iIi1I + 'youtube.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'REQUESTS' ) == 'true' :
  IIIIii ( '[COLORgreen]REQUESTS[/COLOR]' , iiI1IiI + ( i1111 ( 'L1JFUVVFU1RTLnBocA==' ) ) , 10066 , ii11iIi1I + 'requests.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Stand Up' ) == 'true' :
  IIIIii ( '[COLORgreen]STAND UP[/COLOR]' , '' , 10003 , ii11iIi1I + 'ORIGINSTANDUP.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Documentaries' ) == 'true' :
  IIIIii ( '[COLORgreen]DOCUMENTARIES[/COLOR]' , iiI1IiI , 8040 , ii11iIi1I + 'documentary.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Disclose' ) == 'true' :
  IIIIii ( '[COLORgreen]DISCLOSE TV[/COLOR]' , iiI1IiI , 7001 , ii11iIi1I + 'disclose.png' , i1iiIII111ii , '' )
  if 59 - 59: OoOoOO00 + OoooooooOO * I1IiI + i1IIi
  if 58 - 58: OoOoOO00 * i1I111II1I * ii11ii1ii / i1I111II1I
 if o0oO0 . getSetting ( 'Playlist Loader' ) == 'true' :
  IIIIii ( '[COLORgreen]PLAYLIST LOADER[/COLOR]' , iiI1IiI , 3000 , ii11iIi1I + 'loader.png' , i1iiIII111ii , '' )
  if 75 - 75: O0ooOooooO
  if 50 - 50: iI / Oo - O0ooOooooO - Oooo0Ooo000 % i1I111ii1II1i - O0ooOooooO
  if 91 - 91: Ooo00oOo00o / Oooo0Ooo000 - OoOoOO00 . Oooo0Ooo000
  if 18 - 18: OOooOOo
  if 98 - 98: i1I111ii1II1i * i1I111ii1II1i / i1I111ii1II1i + Oooo0Ooo000
  if 34 - 34: OOO0OOo
  if 15 - 15: Oooo0Ooo000 * OOO0OOo * Oo % i11iIiiIii % I1IiI - i1I111II1I
  if 68 - 68: o00OO00OoO % i1IIi . OoOo00o . ii11ii1ii
  if 92 - 92: i1I111ii1II1i . o00OO00OoO
  if 31 - 31: o00OO00OoO . I1IiI / O0
  if 89 - 89: I1IiI
  if 68 - 68: Ooo00oOo00o * OoooooooOO % O0 + Ooo00oOo00o + OOO0OOo
  if 4 - 4: OOO0OOo + O0 * i1I111II1I
 O00Oo000ooO0 ( 'movies' , 'MAIN' )
 if 55 - 55: Oo + iIii1I11I1II1 / I1IiI * O0ooOooooO - i11iIiiIii - iI
def ii1ii1ii ( ) :
 IIIIii ( '[COLORgreen]SEARCH MOVIES[/COLOR]' , iiI1IiI , 9001 , ii11iIi1I + 'search.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Popcorn Box' ) == 'true' :
  IIIIii ( '[COLORgreen]POPCORN BOX[/COLOR]' , iiI1IiI , 7061 , ii11iIi1I + 'popcorn.png' , i1iiIII111ii , '' )
 IIIIii ( '[COLORgreen]Film Trailers[/COLOR]' , i1111 ( 'aHR0cDovL3RoZW1vdmllYm94Lm5ldC9leHBsb3Jl' ) , 10068 , ii11iIi1I + 'movietrailers.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'CLASSIC MOVIES' ) == 'true' :
  IIIIii ( '[COLORgreen]CLASSIC MOVIES[/COLOR]' , '' , 8060 , ii11iIi1I + 'classicmovies.png' , i1iiIII111ii , '' )
 O00Oo000ooO0 ( 'movies' , 'MAIN' )
def oooooOoo0ooo ( ) :
 if o0oO0 . getSetting ( 'G-tv' ) == 'true' :
  IIIIii ( '[COLORgreen]G-Tv PRIVATE LIST[/COLOR]' , '' , 10058 , ii11iIi1I + 'GTVIPTV.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'TV GUIDE' ) == 'true' :
  I1I1IiI1 ( '[COLORgreen]TV GUIDE[/COLOR]' , '' , 10063 , ii11iIi1I + 'GTVIPTV.png' , i1iiIII111ii , '' )
 I1I1IiI1 ( '[COLORgreen]Link GTV Donators Username and Password to Guide[/COLOR]' , '' , 4010 , ii11iIi1I + 'GTVIPTV.png' , i1iiIII111ii , '' )
 if 5 - 5: OOooOOo * OOO0OOo + I1IiI . i1I111II1I + I1IiI
 if 91 - 91: O0
def oOOo0 ( ) :
 IIIIii ( '[COLORgreen]SEARCH SERIES[/COLOR]' , iiI1IiI , 9002 , ii11iIi1I + 'search.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Dizzy Tv' ) == 'true' :
  IIIIii ( '[COLORgreen]DIZZY TV[/COLOR]' , '' , 10018 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Watch Series' ) == 'true' :
  IIIIii ( '[COLORgreen]WATCH SERIES[/COLOR]' , '' , 10040 , ii11iIi1I + 'WATCHSERIES.png' , i1iiIII111ii , '' )
 IIIIii ( '[COLORgreen]iWATCH SERIES[/COLOR]' , '' , 8020 , ii11iIi1I + 'iwatch.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Recent Episodes' ) == 'true' :
  IIIIii ( '[COLORgreen]RECENT EPISODES[/COLOR]' , iiI1IiI , 8081 , ii11iIi1I + 'recent.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'CLASSIC TV' ) == 'true' :
  IIIIii ( '[COLORgreen]CLASSIC TV[/COLOR]' , iiI1IiI , 8064 , ii11iIi1I + 'classictv.png' , i1iiIII111ii , '' )
 IIIIii ( '[COLORgreen]TV Show Trailers[/COLOR]' , i1111 ( 'aHR0cHM6Ly93d3cueW91dHViZS5jb20vd2F0Y2g/dj03WkZJUzJBcUF6OCZsaXN0PVBMM2t4NWgyVHJZR3dwVzBWYk5lbnBqLUJLTUJUR2dKUEU=' ) , 10069 , ii11iIi1I + 'tvtrailers.png' , i1iiIII111ii , '' )
 IIIIii ( '[COLORgreen]TV Show Schedule[/COLOR]' , i1111 ( 'aHR0cDovL3d3dy5wb2dkZXNpZ24uY28udWsvY2F0Lw==' ) , 10070 , ii11iIi1I + 'tvschedule.png' , i1iiIII111ii , '' )
 O00Oo000ooO0 ( 'movies' , 'MAIN' )
def oo00O00oO ( ) :
 if o0oO0 . getSetting ( 'Scooby Streams' ) == 'true' :
  IIIIii ( '[COLORgreen]SCOOBY STREAMS[/COLOR]' , iiI1IiI , 1023 , ii11iIi1I + 'scoob.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'The Reaper' ) == 'true' :
  IIIIii ( '[COLORgreen]THE REAPER[/COLOR]' , ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9UaGVfUmVhcGVyL21haW4ucGhw' ) ) , 1016 , ii11iIi1I + 'reap.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Pandoras Box' ) == 'true' :
  IIIIii ( '[COLORgreen]PANDORAS BOX[/COLOR]' , iiI1IiI , 10025 , ii11iIi1I + 'PANDORASBOX.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'HeroVision' ) == 'true' :
  IIIIii ( '[COLORgreen]HEROVISION[/COLOR]' , ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC9tYWluLnBocA==' ) ) , 1016 , ii11iIi1I + 'hero.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Silent Hunter' ) == 'true' :
  IIIIii ( '[COLORgreen]SILENT HUNTER[/COLOR]' , ( i1111 ( 'aHR0cDovLzUuMTM1LjIwNy45Ni8=' ) ) , 10084 , ii11iIi1I + 'SILENTHUNTER.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Redemption Streams' ) == 'true' :
  IIIIii ( '[COLORgreen]Redemption Streams[/COLOR]' , ( i1111 ( 'aHR0cDovL3JlZGVtcHRpb25idWlsZC4xNm1iLmNvbS9SZWRlbXB0aW9uL21haW4ucGhw' ) ) , 1016 , ii11iIi1I + 'redemption.png' , i1iiIII111ii , '' )
 O00Oo000ooO0 ( 'movies' , 'MAIN' )
 if 23 - 23: Ooo00oOo00o + Ooo00oOo00o . i1I111II1I
def ii1ii11IIIiiI ( ) :
 IIIIii ( '[COLORgreen]SILENT HUNTER[/COLOR]' , ( i1111 ( 'aHR0cDovLzUuMTM1LjIwNy45Ni8=' ) ) , 1006 , ii11iIi1I + 'SILENTHUNTER.png' , i1iiIII111ii , '' )
 IIIIii ( '[COLORgreen]SILENT HUNTER SCRAPES[/COLOR]' , ( i1111 ( 'http://5.135.207.96/Scrapes/main.php' ) ) , 1016 , ii11iIi1I + 'SILENTHUNTER.png' , i1iiIII111ii , '' )
 if 67 - 67: Oooo0Ooo000 * O0ooOooooO * ii11ii1ii + i1I111II1I / i1IIi
 if 11 - 11: iI + i1I111ii1II1i - OOO0OOo * O0ooOooooO % i11iIiiIii - o00OO00OoO
 if 83 - 83: Oooo0Ooo000 / OOOo0
def iIIiIi1iIII1 ( ) :
 IIIIii ( '[COLORgreen]SEARCH CARTOONS[/COLOR]' , '' , 10005 , ii11iIi1I + 'search.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'WCO' ) == 'true' :
  IIIIii ( '[COLORgreen]WATCH CARTOONS ONLINE[/COLOR]' , iiI1IiI , 21004 , ii11iIi1I + 'watchcartoons.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Cartoons' ) == 'true' :
  IIIIii ( '[COLORgreen]CARTOONS[/COLOR]' , '' , 10001 , ii11iIi1I + 'ORIGINCARTOON.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Anime' ) == 'true' :
  IIIIii ( '[COLORgreen]AnimeLand[/COLOR]' , ( i1111 ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2R1YmJlZC1hbmltZQ==' ) ) , 10004 , ii11iIi1I + 'anime.png' , i1iiIII111ii , '' )
 O00Oo000ooO0 ( 'movies' , 'MAIN' )
def OooOOOOo ( ) :
 if o0oO0 . getSetting ( 'Football' ) == 'true' :
  IIIIii ( '[COLORgreen]FOOTBALL[/COLOR]' , '' , 10002 , ii11iIi1I + 'ORIGINFOOTBALL.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Fitness' ) == 'true' :
  IIIIii ( '[COLORgreen]FITNESS[/COLOR]' , ( i1111 ( 'aHR0cHM6Ly93d3cuZml0bmVzc2JsZW5kZXIuY29tL3ZpZGVvcw==' ) ) , 7085 , ii11iIi1I + 'FITNESS.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Go Fishing' ) == 'true' :
  IIIIii ( '[COLORgreen]Go Fishing[/COLOR]' , iiI1IiI , 8090 , ii11iIi1I + 'gofish.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'GenieTv Kitchen' ) == 'true' :
  IIIIii ( '[COLORgreen]GenieTv Kitchen[/COLOR]' , ( i1111 ( 'aHR0cDovL2Zvb2QubmR0di5jb20vdmlkZW9z' ) ) , 8045 , ii11iIi1I + 'geniekitchen.png' , i1iiIII111ii , '' )
 O00Oo000ooO0 ( 'movies' , 'MAIN' )
 if 76 - 76: Ooo00oOo00o
 if 29 - 29: i1I111II1I + Oo . i11iIiiIii - i1IIi / iIii1I11I1II1
 if 26 - 26: Oooo0Ooo000 . OoooooooOO
def Oo0O0O0ooO0O ( ) :
 I11i1ii1 = O0Oooo0O ( 'http://architects.x10host.com/wizarddelete.txt' )
 O0o = re . compile ( '<unwanted_wizard =(.+?)</unwanted_wizard>' ) . findall ( I11i1ii1 )
 for OoOooO in O0o :
  print OoOooO
  OoOooO = ( str ( OoOooO ) )
  if os . path . exists ( xbmc . translatePath ( OoOooO ) ) :
   II111iiiI1Ii = os . path . join ( o0 , 'guisettings.xml' )
   o0O0OOO0Ooo = open ( II111iiiI1Ii , "w+" )
   if 45 - 45: O0 / OOooOOo
   o0O0OOO0Ooo . write ( r'.' )
   i1IIIII11I1IiI ( )
  else :
   pass
   if 16 - 16: iIii1I11I1II1
def Ii11iII1 ( ) :
 I11i1ii1 = O0Oooo0O ( 'http://architects.x10host.com/testdelete.txt' )
 O0o = re . compile ( '<unwanted_addon =(.+?)</unwanted_addon>' ) . findall ( I11i1ii1 )
 for iI1iI1I1i1I in O0o :
  iI1iI1I1i1I = ( str ( iI1iI1I1i1I ) )
  if os . path . exists ( xbmc . translatePath ( iI1iI1I1i1I ) ) :
   iIi11Ii1 ( iI1iI1I1i1I )
   oOooOOOoOo ( )
  else :
   pass
   if 41 - 41: iI - O0 - O0
def iIi11Ii1 ( addon ) :
 oOOoo00O0O . ok ( "[COLOR=white]Incompatible[/COLOR]" , "Unfortunately GenieTv will not work with" , addon , 'please remove then reinstall genie' )
 II111iiiI1Ii = os . path . join ( II , 'default.py' )
 o0O0OOO0Ooo = open ( II111iiiI1Ii , "w+" )
 if 68 - 68: i1I111II1I % o00OO00OoO
 o0O0OOO0Ooo . write ( r'Genie Tv will not work with certain addons in an attempt to bring you original content from the best developers' )
 o0O0OOO0Ooo . write ( r'and not those simply out to profit or make a name for themselves off others work' )
 o0O0OOO0Ooo . write ( r'Please remove' + unwanted_addons + 'if you would like to use genie tv then uninstall and reinstall from official repo' )
 if 88 - 88: iIii1I11I1II1 - OOO0OOo + i1I111II1I
 if 40 - 40: OOOo0 * iI + i1I111II1I % i1I111ii1II1i
def i1IIIII11I1IiI ( ) :
 I11i1ii1 = O0Oooo0O ( i1111 ( 'aHR0cDovL3d3dy5wb2dkZXNpZ24uY28udWsvY2F0Lw==' ) )
 OOOOOoo0 = re . compile ( '<tr>.+?title="(.+?)">(.+?)</tr>' , re . DOTALL ) . findall ( I11i1ii1 )
 for ii1 , OOOOOoo0 in OOOOOoo0 :
  ii1 = ii1
  O0o = re . compile ( '<p><a href=".+?" rel=".+?">(.+?)\n</a>.+?<br /><a href=".+?">(.+?)</a>.+?</p>' , re . DOTALL ) . findall ( str ( OOOOOoo0 ) )
  for I1iI1iIi111i , iiIi1IIi1I in O0o :
   o0OoOO000ooO0 ( ii1 , I1iI1iIi111i , iiIi1IIi1I )
   if 56 - 56: i1I111ii1II1i
   if 86 - 86: OoOoOO00 % o00OO00OoO
   if 15 - 15: i1IIi * OOOo0 + i11iIiiIii
   if 6 - 6: OOO0OOo / i11iIiiIii + i1I111ii1II1i * O0ooOooooO
   if 80 - 80: OoOoOO00
   if 83 - 83: Oooo0Ooo000 . i11iIiiIii + OoOoOO00 . OOooOOo * Oooo0Ooo000
   if 53 - 53: OoOoOO00
   if 31 - 31: Ooo00oOo00o
   if 80 - 80: o00OO00OoO . i11iIiiIii - OOooOOo
   if 25 - 25: Ooo00oOo00o
   if 62 - 62: i1I111II1I + O0
   if 98 - 98: OOooOOo
   if 51 - 51: Oo - O0ooOooooO + OoOoOO00 * iI . Oooo0Ooo000 + O0ooOooooO
   if 78 - 78: i11iIiiIii / i1I111ii1II1i - iI / i1I111II1I + O0ooOooooO
   if 82 - 82: iI
   if 46 - 46: OoooooooOO . i11iIiiIii
   if 94 - 94: OOooOOo * iI / Oo / iI
def oO0 ( ) :
 IIIIii ( 'Genre' , i1111 ( 'aHR0cDovL2ltb3ZpZW1heC5zZS9tb3ZpZXMv' ) , 10073 , ii11iIi1I + 'genievision.png' , i1iiIII111ii , '' )
 IIIIii ( 'Most Viewed' , i1111 ( 'aHR0cDovL2ltb3ZpZW1heC5zZS9tb3ZpZXMv' ) , 10077 , ii11iIi1I + 'genievision.png' , i1iiIII111ii , '' )
 IIIIii ( 'Box Office' , i1111 ( 'aHR0cDovL2ltb3ZpZW1heC5zZS9jYXRlZ29yeS9ib3gtb2ZmaWNlLw==' ) , 10074 , ii11iIi1I + 'genievision.png' , i1iiIII111ii , '' )
 IIIIii ( 'Search' , '' , 10078 , ii11iIi1I + 'genievision.png' , i1iiIII111ii , '' )
 if 75 - 75: OOO0OOo + I1IiI + OOooOOo * Oooo0Ooo000 % O0ooOooooO . i1I111ii1II1i
def oOI1Ii1I1 ( ) :
 IiII111iI1ii1 = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 iI11I1II = 'http://imoviemax.se/?s=' + ( IiII111iI1ii1 ) . replace ( ' ' , '+' )
 Ii1I = iI11I1II . lower ( )
 IiI1i ( Ii1I )
def o0O ( url ) :
 o00iI = [ ]
 I11i1ii1 = O0Oooo0O ( url )
 O0o = re . compile ( '<li class="cat-item cat-item-.+? "><a href="(.+?)">(.+?)</a><i>(.+?)</i></li>' ) . findall ( I11i1ii1 )
 for url , I1iI1iIi111i , O0O0Oooo0o in O0o :
  if I1iI1iIi111i in o00iI :
   pass
  else :
   IIIIii ( I1iI1iIi111i + ' - ' + O0O0Oooo0o + ' Films' , url , 10074 , ii11iIi1I + 'genievision.png' , i1iiIII111ii , '' )
   o00iI . append ( I1iI1iIi111i )
   if 56 - 56: ii11ii1ii % O0 - OOOo0
def O00o0OO0 ( url ) :
 I11i1ii1 = O0Oooo0O ( url )
 O0o = re . compile ( '<li>.+?<b>.+?</b>.+?<a href="(.+?)">(.+?)</a>.+?<span>(.+?)</span>' , re . DOTALL ) . findall ( I11i1ii1 )
 for url , I1iI1iIi111i , IIi1I1iiiii in O0o :
  IIIIii ( I1iI1iIi111i + ' - Views:' + IIi1I1iiiii , url , 10075 , ii11iIi1I + 'genievision.png' , i1iiIII111ii , '' )
  if 71 - 71: OoOo00o * OoOoOO00 * O0ooOooooO
  if 56 - 56: OOOo0
def IiI1i ( url ) :
 O0oO = [ ]
 I11i1ii1 = O0Oooo0O ( url )
 next = re . compile ( "<link rel='next' href='(.+?)' />" ) . findall ( I11i1ii1 )
 for next in next :
  IIIIii ( 'NEXT PAGE' , next , 10074 , ii11iIi1I + 'Next.png' , i1iiIII111ii , '' )
 O0o = re . compile ( '<div class="movie">.+?<img src="(.+?)" alt="(.+?)" />.+?<a href="(.+?)"><span class="player"></span></a>' , re . DOTALL ) . findall ( I11i1ii1 )
 for OO0ooOOO0OOO , I1iI1iIi111i , url in O0o :
  IIIIii ( I1iI1iIi111i , url , 10075 , OO0ooOOO0OOO , OO0ooOOO0OOO , '' )
  O0oO . append ( I1iI1iIi111i )
  if 63 - 63: I1IiI * i1I111ii1II1i
def ooiIi1 ( img , name , url ) :
 img = img
 name = name
 I11i1ii1 = O0Oooo0O ( url )
 O0o = re . compile ( '<div id="(.+?)" class="player-content"><iframe class="playerframe" src="(.+?)" scrolling="no".+?</iframe></div>' ) . findall ( I11i1ii1 )
 for OoOOoOooooOOo , url in O0o :
  print '>>>>>>>>>>>>>>>>>>>>>>>>>>> before' + url
  oOo0O = ( url ) . replace ( 'player' , 'watch' ) + '&fv=&sou='
  print '<<<<<<<<<<<<<<<<<<<<<<<<<<< after' + oOo0O
  oo0O0 = ( OoOOoOooooOOo ) . replace ( 'play-' , 'Server ' )
  I1I1IiI1 ( oo0O0 , oOo0O , 10076 , img , img , '' )
  if 22 - 22: I1IiI . i1I111II1I * I1IiI
def O000OOO ( url ) :
 I11i1ii1 = O0Oooo0O ( url )
 O0o = re . compile ( '<source src="(.+?)" type="video/mp4">' ) . findall ( I11i1ii1 )
 for IIo0o0O0O00oOOo in O0o :
  if '=m' in IIo0o0O0O00oOOo :
   iIIIiIi ( IIo0o0O0O00oOOo )
  elif 'php' in IIo0o0O0O00oOOo :
   O000OOO ( url )
  else :
   I11i1ii1 = O0Oooo0O ( IIo0o0O0O00oOOo )
   O0o = re . compile ( 'content="(.+?)">' ) . findall ( I11i1ii1 )
   for OO0O0 in O0o :
    iIIIiIi ( IIo0o0O0O00oOOo )
    if 30 - 30: i1I111II1I + ii11ii1ii * Oooo0Ooo000 % i11iIiiIii % I1IiI
    if 97 - 97: ii11ii1ii % ii11ii1ii % O0ooOooooO / i1I111ii1II1i - iIii1I11I1II1
    if 69 - 69: o00OO00OoO
def ii1I1 ( url ) :
 I11i1ii1 = O0Oooo0O ( url )
 OooooOOoo0 = re . compile ( '<td id=".+?" class="today">.+?title="(.+?)">(.+?)</td>' , re . DOTALL ) . findall ( I11i1ii1 )
 for ii1 , i1I1IiiIi1i in OooooOOoo0 :
  print 'there ><><><><><><><><><><><><'
  ii1 = ii1
  O0o = re . compile ( '<p><a href=".+?" rel=".+?">(.+?)</a>.+?<br /><a href=".+?">(.+?)</a>.+?</p>' , re . DOTALL ) . findall ( str ( i1I1IiiIi1i ) )
  for I1iI1iIi111i , iiIi1IIi1I in O0o :
   print 'here <><><><><><><><><><><><>'
   IIIIii ( '[COLORred]' + ii1 + '[/COLOR] - ' + I1iI1iIi111i + ' - [COLORgreen]' + iiIi1IIi1I + '[/COLOR]' , i1111 ( 'aHR0cDovL3d3dy5wb2dkZXNpZ24uY28udWsvY2F0Lw==' ) , 10070 , ii11iIi1I + 'loader.png' , i1iiIII111ii , '' )
 OOOOOoo0 = re . compile ( '<td id=".+?" class="day">.+?title="(.+?)">(.+?)</td>' , re . DOTALL ) . findall ( I11i1ii1 )
 for ii1 , iiI11ii1I1 in OOOOOoo0 :
  print 'there ><><><><><><><><><><><><'
  ii1 = ii1
  O0o = re . compile ( '<p><a href=".+?" rel=".+?">(.+?)</a>.+?<br /><a href=".+?">(.+?)</a>.+?</p>' , re . DOTALL ) . findall ( str ( iiI11ii1I1 ) )
  for I1iI1iIi111i , iiIi1IIi1I in O0o :
   print 'here <><><><><><><><><><><><>'
   IIIIii ( '[COLORred]' + ii1 + '[/COLOR] - ' + I1iI1iIi111i + ' - [COLORgreen]' + iiIi1IIi1I + '[/COLOR]' , i1111 ( 'aHR0cDovL3d3dy5wb2dkZXNpZ24uY28udWsvY2F0Lw==' ) , 10070 , ii11iIi1I + 'loader.png' , i1iiIII111ii , '' )
   if 82 - 82: OoOoOO00 % Oooo0Ooo000 / Ooo00oOo00o + I1IiI / OOooOOo / o00OO00OoO
   if 70 - 70: O0ooOooooO
   if 59 - 59: OOooOOo % O0ooOooooO
def ii1iI1I11I ( url ) :
 I11i1ii1 = O0Oooo0O ( url )
 OOOOOoo0 = re . compile ( '<li class="yt-uix-scroller-scroll-unit "(.+?)</li>' , re . DOTALL ) . findall ( I11i1ii1 )
 for OOOOOoo0 in OOOOOoo0 :
  I1iI1iIi111i = re . compile ( 'data-video-title="(.+?)"' ) . findall ( str ( OOOOOoo0 ) )
  for I1iI1iIi111i in I1iI1iIi111i :
   I1iI1iIi111i = ( I1iI1iIi111i ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&amp;' , '&' )
  url = re . compile ( '<a href="/w(.+?)&' ) . findall ( str ( OOOOOoo0 ) )
  for url in url :
   url = 'https://www.youtube.com/w' + url
  II1iI = re . compile ( '<img.+?="(.+?)"' ) . findall ( str ( OOOOOoo0 ) )
  for II1iI in II1iI :
   II1iI = 'http:' + II1iI
  I1I1IiI1 ( '[COLORgreen]' + I1iI1iIi111i + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , II1iI , '' , '' )
  if 54 - 54: o00OO00OoO * OoOo00o / o00OO00OoO / Oo * I1IiI
  if 94 - 94: OoOo00o * ii11ii1ii . OOO0OOo . OOO0OOo / I1IiI - o00OO00OoO
  if 86 - 86: iIii1I11I1II1 / I1IiI . OoOoOO00
  if 19 - 19: ii11ii1ii % OoooooooOO % OoOo00o * OOooOOo % O0
def ooo ( url ) :
 if 27 - 27: OOO0OOo % OOOo0
 o0oooOO00 = [ ]
 I11i1ii1 = O0Oooo0O ( url )
 O0o = re . compile ( '<div class="explore-list">.+?<div class="el-img"><a href="(.+?)" class=".+?"><img src="(.+?)" alt=".+?<h3>(.+?)</h3><p>(.+?)</p></div>' , re . DOTALL ) . findall ( I11i1ii1 )
 for IIo0o0O0O00oOOo , OO0ooOOO0OOO , I1iI1iIi111i , iiIiii1IIIII in O0o :
  I1iI1iIi111i = ( I1iI1iIi111i ) . replace ( '&#039;' , '\'' ) . replace ( '&amp;' , '&' ) . replace ( '&quot;' , '"' )
  o00o = O0Oooo0O ( IIo0o0O0O00oOOo )
  IIIIiiIiiI = re . compile ( '<!-- # player # -->.+?<iframe title=".+?".+?src="http://www.youtube.com/embed/(.+?)?autohide.+?<!-- detail box -->(.+?)</div>' , re . DOTALL ) . findall ( o00o )
  for IIIIiI11I11 , oo00o0 in IIIIiiIiiI :
   i11II1I11I1 = re . compile ( '<p>(.+?)</p>' , re . DOTALL ) . findall ( str ( oo00o0 ) )
   for OOoOO0ooo in i11II1I11I1 :
    if I1iI1iIi111i in o0oooOO00 :
     pass
    else :
     I1I1IiI1 ( I1iI1iIi111i , IIIIiI11I11 , 8043 , OO0ooOOO0OOO , OO0ooOOO0OOO , OOoOO0ooo )
     O00Oo000ooO0 ( 'movies' , 'INFO' )
     o0oooOO00 . append ( I1iI1iIi111i )
     if 30 - 30: OOooOOo - i1IIi % OoOoOO00 + Oooo0Ooo000 * iIii1I11I1II1
     if 81 - 81: OoOo00o % i1IIi . iIii1I11I1II1
def Ii1Iii1iIi ( url ) :
 OO0oo = Iii1 ( url )
 O0o = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( OO0oo )
 for url , OOO0000oO , OOoOO0ooo , iI1i111I1Ii , I1iI1iIi111i in O0o :
  IIIIii ( I1iI1iIi111i , url , 10065 , OOO0000oO , iI1i111I1Ii , OOoOO0ooo )
 O00Oo000ooO0 ( 'movies' , 'INFO' )
 if 25 - 25: o00OO00OoO - i1I111ii1II1i
def Ii1Io0OO0o0o00o ( ) :
 IiII111iI1ii1 = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 iI11I1II = 'https://www.youtube.com/results?search_query=' + ( IiII111iI1ii1 ) . replace ( ' ' , '+' )
 Ii1I = iI11I1II . lower ( )
 I11i1ii1 = O0Oooo0O ( Ii1I )
 O0o = re . compile ( '<img src="(.+?)" alt=.+?yt-lockup-title "><a href="(.+?)".+?data-sessionlink=.+?" title="(.+?)".+?<span class="accessible-description".+?>(.+?)</span>.+?<div class="yt-lockup-description yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr">(.+?)</div>' , re . DOTALL ) . findall ( I11i1ii1 )
 next = re . compile ( '<a href="(.+?)" class="yt-uix-button.+?class="yt-uix-button-content">Next.+?</span></a>' ) . findall ( I11i1ii1 )
 for oOo0 in next :
  oOo0 = 'https://www.youtube.com' + oOo0
  IIIIii ( '[COLORgreen] NEXT [/COLOR]' , oOo0 , 10065 , ii11iIi1I + 'Next.png' , i1iiIII111ii , '' )
 for OO0ooOOO0OOO , oOo0 , I1iI1iIi111i , OOOoOO , oo00o0 in O0o :
  OO0o . append ( I1iI1iIi111i )
  O00Oo000ooO0 ( 'tvshows' , 'INFO' )
  II1iI = 'http:' + ( OO0ooOOO0OOO ) . replace ( 'https:' , '' )
  print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>' + II1iI
  oOo0 = 'http://www.youtube.com' + oOo0
  I1I1IiI1 ( '[COLORred]' + OOOoOO + '[/COLOR]' + '[COLORgreen]' + I1iI1iIi111i + '[/COLOR]' , ( oOo0 ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , II1iI , II1iI , oo00o0 )
 else :
  O0o = re . compile ( '<img src="(.+?)" alt=.+?yt-lockup-title "><a href="(.+?)".+?data-sessionlink=.+?" title="(.+?)".+?<span class="accessible-description".+?>(.+?)</span>' , re . DOTALL ) . findall ( I11i1ii1 )
  for OO0ooOOO0OOO , oOo0 , I1iI1iIi111i , OOOoOO in O0o :
   print 'im doing it'
   O00Oo000ooO0 ( 'tvshows' , 'INFO' )
   II1iI = 'http:' + ( OO0ooOOO0OOO ) . replace ( 'https:' , '' )
   oOo0 = 'http://www.youtube.com' + oOo0
   if '&' in oOo0 :
    print ' i got here'
    I11i1ii1 = O0Oooo0O ( oOo0 )
    OOOOOoo0 = re . compile ( '<li class="yt-uix-scroller-scroll-unit "(.+?)</li>' , re . DOTALL ) . findall ( I11i1ii1 )
    for OOOOOoo0 in OOOOOoo0 :
     I1iI1iIi111i = re . compile ( 'data-video-title="(.+?)"' ) . findall ( str ( OOOOOoo0 ) )
     for I1iI1iIi111i in I1iI1iIi111i :
      I1iI1iIi111i = ( I1iI1iIi111i ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&amp;' , '&' )
     oOo0 = re . compile ( '<a href="/w(.+?)&' ) . findall ( str ( OOOOOoo0 ) )
     for oOo0 in oOo0 :
      oOo0 = 'https://www.youtube.com/w' + oOo0
     II1iI = re . compile ( '<img.+?="(.+?)"' ) . findall ( str ( OOOOOoo0 ) )
     for II1iI in II1iI :
      II1iI = 'http:' + II1iI
     I1I1IiI1 ( '[COLORred]' + OOOoOO + '[/COLOR]' + '[COLORgreen]' + I1iI1iIi111i + '[/COLOR]' , ( oOo0 ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , II1iI , i1iiIII111ii , '' )
   elif I1iI1iIi111i in OO0o :
    pass
   elif 'user' in oOo0 or 'elete' in I1iI1iIi111i :
    pass
   elif 'hannel' in oOo0 :
    print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' + oOo0
    I11i1ii1 = O0Oooo0O ( oOo0 )
    I11IIIi = re . compile ( 'data-thumb="(.+?)".+?href="(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( I11i1ii1 )
    for OO0ooOOO0OOO , oOo0 , I1iI1iIi111i in I11IIIi :
     if 'outube' in oOo0 or 'list' in oOo0 :
      pass
     elif 'atch' in oOo0 :
      oOo0 = ( oOo0 ) . replace ( '/watch?v=' , '' )
      I1I1IiI1 ( '[COLORred]' + OOOoOO + '[/COLOR]' + '[COLORgreen]' + I1iI1iIi111i + '[/COLOR]' , ( oOo0 ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , 'http:' + OO0ooOOO0OOO , 'http:' + OO0ooOOO0OOO , '' )
     else :
      pass
   else :
    I1I1IiI1 ( '[COLORred]' + OOOoOO + '[/COLOR]' + '[COLORgreen]' + I1iI1iIi111i + '[/COLOR]' , ( oOo0 ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , II1iI , II1iI , '' )
    if 15 - 15: ii11ii1ii * Ooo00oOo00o
def i1II1i ( url ) :
 I11i1ii1 = O0Oooo0O ( url )
 O0o = re . compile ( '<img src="(.+?)" alt=.+?yt-lockup-title "><a href="(.+?)".+?data-sessionlink=.+?" title="(.+?)".+?<span class="accessible-description".+?>(.+?)</span>.+?<div class="yt-lockup-description yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr">(.+?)</div>' , re . DOTALL ) . findall ( I11i1ii1 )
 next = re . compile ( '<a href="(.+?)" class="yt-uix-button.+?class="yt-uix-button-content">Next.+?</span></a>' ) . findall ( I11i1ii1 )
 for url in next :
  url = 'https://www.youtube.com' + url
  IIIIii ( '[COLORgreen] NEXT [/COLOR]' , url , 10065 , ii11iIi1I + 'Next.png' , i1iiIII111ii , '' )
 for OO0ooOOO0OOO , url , I1iI1iIi111i , OOOoOO , oo00o0 in O0o :
  OO0o . append ( I1iI1iIi111i )
  O00Oo000ooO0 ( 'tvshows' , 'INFO' )
  II1iI = 'http:' + ( OO0ooOOO0OOO ) . replace ( 'https:' , '' )
  print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>' + II1iI
  url = 'http://www.youtube.com' + url
  I1I1IiI1 ( '[COLORred]' + OOOoOO + '[/COLOR]' + '[COLORgreen]' + I1iI1iIi111i + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , II1iI , II1iI , oo00o0 )
 else :
  O0o = re . compile ( '<img src="(.+?)" alt=.+?yt-lockup-title "><a href="(.+?)".+?data-sessionlink=.+?" title="(.+?)".+?<span class="accessible-description".+?>(.+?)</span>' , re . DOTALL ) . findall ( I11i1ii1 )
  for OO0ooOOO0OOO , url , I1iI1iIi111i , OOOoOO in O0o :
   O00Oo000ooO0 ( 'tvshows' , 'INFO' )
   II1iI = 'http:' + ( OO0ooOOO0OOO ) . replace ( 'https:' , '' )
   url = 'http://www.youtube.com' + url
   if '&' in url :
    I11i1ii1 = O0Oooo0O ( url )
    OOOOOoo0 = re . compile ( '<li class="yt-uix-scroller-scroll-unit "(.+?)</li>' , re . DOTALL ) . findall ( I11i1ii1 )
    for OOOOOoo0 in OOOOOoo0 :
     I1iI1iIi111i = re . compile ( 'data-video-title="(.+?)"' ) . findall ( str ( OOOOOoo0 ) )
     for I1iI1iIi111i in I1iI1iIi111i :
      I1iI1iIi111i = ( I1iI1iIi111i ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&amp;' , '&' )
     url = re . compile ( '<a href="/w(.+?)&' ) . findall ( str ( OOOOOoo0 ) )
     for url in url :
      url = 'https://www.youtube.com/w' + url
     II1iI = re . compile ( '<img.+?="(.+?)"' ) . findall ( str ( OOOOOoo0 ) )
     for II1iI in II1iI :
      II1iI = 'http:' + II1iI
     I1I1IiI1 ( '[COLORred]' + OOOoOO + '[/COLOR]' + '[COLORgreen]' + I1iI1iIi111i + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , II1iI , i1iiIII111ii , '' )
   elif I1iI1iIi111i in OO0o :
    pass
   elif 'user' in url or 'elete' in I1iI1iIi111i :
    pass
   elif 'hannel' in url :
    print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' + url
    I11i1ii1 = O0Oooo0O ( url )
    I11IIIi = re . compile ( 'data-thumb="(.+?)".+?href="(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( I11i1ii1 )
    for OO0ooOOO0OOO , url , I1iI1iIi111i in I11IIIi :
     if 'outube' in url or 'list' in url :
      pass
     elif 'atch' in url :
      url = ( url ) . replace ( '/watch?v=' , '' )
      I1I1IiI1 ( '[COLORred]' + OOOoOO + '[/COLOR]' + '[COLORgreen]' + I1iI1iIi111i + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , 'http:' + OO0ooOOO0OOO , 'http:' + OO0ooOOO0OOO , '' )
     else :
      pass
   else :
    I1I1IiI1 ( '[COLORred]' + OOOoOO + '[/COLOR]' + '[COLORgreen]' + I1iI1iIi111i + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , II1iI , II1iI , '' )
    if 83 - 83: I1IiI - iI / Oooo0Ooo000 / o00OO00OoO + O0ooOooooO - O0
    if 4 - 4: i1I111II1I * Ooo00oOo00o % i1IIi * i11iIiiIii % Oo - O0ooOooooO
def OOoOoOo ( ) :
 if oo0o0O00 == 'insert_password' :
  oOOoo00O0O . ok ( '[COLORgreen]Donators Login[/COLOR]' , 'You need to set username and password to access this' , 'These are unique and provided to donators to help with server and stream costs' , 'Donate @ [COLORgreen]http://architects.x10host.com[/COLOR]' )
  o0oO0 . openSettings ( sys . argv [ 0 ] )
 else :
  o000ooooO0o = open ( iIi1ii1I1 )
  O0o = re . compile ( 'plugin.video.GenieTv.+?2Flive%2F(.+?)%2F(.+?)%2F' ) . findall ( str ( o000ooooO0o ) )
  for iI1i11 , OoOOoooOO0O in O0o :
   if iI1i11 == 'needs replacing' or OoOOoooOO0O == 'needs replacing' :
    ooo00Ooo ( )
  IIIIii ( '[COLORgreen]DONATORS LIST[/COLOR]' , iiI1IiI + '/thelist.m3u' , 7080 , ii11iIi1I + 'GTVIPTV.png' , i1iiIII111ii , '' )
  if 93 - 93: i11iIiiIii - OOOo0 * ii11ii1ii * Oooo0Ooo000 % O0 + OoooooooOO
def I1i1i1 ( ) :
 i1iiIIiiI111 . ok ( '[COLOR=white]ReCreate Addons.ini[/COLOR]' , 'If it doesnt work ensure login details are correct and retry' , '' , 'This will allow access to streams in guide without linking to favourites' )
 i1iiIIiiI111 . ok ( '[COLOR=red]Reset Any Previous linked streams[/COLOR]' , 'For best results you\'ll need to clear previous linked streams' , 'Go to TVGuide tab then reset database at the bottom' , 'Then go back and guide should be all linked up and ready to go' )
 o0oO0 . openSettings ( sys . argv [ 0 ] )
 ooo00Ooo ( )
 i1iiIIiiI111 . ok ( '[COLOR=yellow]Done[/COLOR]' , 'Done' , 'Easy as that' , 'Now Go to guide and it should link your GTV streams' )
 if 73 - 73: O0 * i1I111ii1II1i + iI + OOO0OOo
def Ii ( ) :
 try :
  o0O0Oo = gui . TVGuide ( )
  o0O0Oo . doModal ( )
  del o0O0Oo
  if 62 - 62: O0 % Oooo0Ooo000 . Oooo0Ooo000 - iIii1I11I1II1 / i11iIiiIii
 except :
  import sys
  import traceback as tb
  ( iiiII , iiIiIi , traceback ) = sys . exc_info ( )
  tb . print_exception ( iiiII , iiIiIi , traceback )
  if 39 - 39: o00OO00OoO
def OoOooOoO ( ) :
 IIIIii ( 'Full Backup' , '' , 10061 , ii11iIi1I + 'Backup.png' , i1iiIII111ii , 'Back Up Your Full System' )
 if os . path . exists ( I1IIIii ) :
  IIIIii ( 'Backup Genie Favourites' , oOo0 , 10062 , ii11iIi1I + 'Backup.png' , i1iiIII111ii , 'Back Up Your favourites' )
 if os . path . exists ( ooooooO0oo ) :
  IIIIii ( 'Backup Ivue Config' , ooooooO0oo , 10062 , ii11iIi1I + 'Backup.png' , i1iiIII111ii , 'Back Up Your master.db' )
 if os . path . exists ( IIiiiiiiIi1I1 ) :
  IIIIii ( 'Backup Kodi Favourites' , IIiiiiiiIi1I1 , 10062 , ii11iIi1I + 'Backup.png' , i1iiIII111ii , 'Back Up Your favourites.xml' )
  if 43 - 43: OoOoOO00 . O0ooOooooO / ii11ii1ii
  if 20 - 20: OOOo0
  if 95 - 95: i1I111ii1II1i - OOOo0
zip = o0oO0 . getSetting ( 'zip' )
I1ii1ii11i1I = xbmc . translatePath ( os . path . join ( zip ) )
def o0OoOO ( ) :
 O0O0Oo00 = xbmc . translatePath ( os . path . join ( zip , 'testCBFolder' ) )
 if not os . path . exists ( zip ) :
  i1iiIIiiI111 . ok ( '[COLOR=white]Origin[/COLOR]' , 'The download location you have stored does not exist .\nPlease update the addon settings and try again.' , '' , '' )
  o0oO0 . openSettings ( sys . argv [ 0 ] )
  if 80 - 80: O0ooOooooO + i1I111II1I / Oooo0Ooo000
  if 79 - 79: OOO0OOo
  if 48 - 48: o00OO00OoO - OOooOOo % iI
def IIi1IIIi ( name , url , description ) :
 if 'Backup' in name :
  if 'Genie' in name :
   url = I1IIIii
  elif 'Ivue' in name :
   url = ooooooO0oo
  elif 'Kodi' in name :
   url = IIiiiiiiIi1I1
  o0OoOO ( )
  O00Ooo = open ( url ) . read ( )
  OOOO0OOO = os . path . join ( I1ii1ii11i1I , description . split ( 'Your ' ) [ 1 ] )
  i1i1ii = open ( OOOO0OOO , mode = 'w' )
  i1i1ii . write ( O00Ooo )
  i1i1ii . close ( )
 else :
  if 'guisettings.xml' in description :
   iII1ii1 = open ( os . path . join ( I1ii1ii11i1I , description . split ( 'Your ' ) [ 1 ] ) ) . read ( )
   I1i1iiiI1 = '<setting type="(.+?)" name="%s.(.+?)">(.+?)</setting>' % skin
   O0o = re . compile ( I1i1iiiI1 ) . findall ( iII1ii1 )
   for type , iIIi , oO0o00oo0 in O0o :
    oO0o00oo0 = oO0o00oo0 . replace ( '&quot;' , '' ) . replace ( '&amp;' , '&' )
    xbmc . executebuiltin ( "Skin.Se	t%s(%s,%s)" % ( type . title ( ) , iIIi , oO0o00oo0 ) )
  else :
   OOOO0OOO = os . path . join ( url )
   O00Ooo = open ( os . path . join ( I1ii1ii11i1I , description . split ( 'Your ' ) [ 1 ] ) ) . read ( )
   i1i1ii = open ( OOOO0OOO , mode = 'w' )
   i1i1ii . write ( O00Ooo )
   i1i1ii . close ( )
 i1iiIIiiI111 . ok ( "[COLOR=white]Origin[/COLOR]" , "" , 'All Done !' , '' )
 if 19 - 19: OoOoOO00 + OoOo00o
 if 53 - 53: O0ooOooooO - OOOo0 - O0ooOooooO * i1I111ii1II1i
 if 71 - 71: O0 - iIii1I11I1II1
 if 12 - 12: i1I111II1I / OOooOOo
def iiI1I1 ( ) :
 ooO = 1
 o0OoOO ( )
 ii = xbmc . translatePath ( os . path . join ( I1ii1ii11i1I , 'Build Backup' , 'Full Backup' , '' ) )
 OO0O0Ooo = xbmc . translatePath ( os . path . join ( I1ii1ii11i1I , 'Build Backup' , 'my_full_backup.zip' ) )
 oOoO0 = xbmc . translatePath ( os . path . join ( I1ii1ii11i1I , 'Build Backup' , 'my_full_backup_GUI_Settings.zip' ) )
 if not os . path . exists ( ii ) :
  os . makedirs ( ii )
 Oo0 = oOOoo00O0O . input ( 'Enter a name for this backup' , type = xbmcgui . INPUT_ALPHANUM )
 if ( not Oo0 ) : return False , 0
 oo0O0o00o0O = Oo0
 I11i1II = xbmc . translatePath ( os . path . join ( ii , oo0O0o00o0O + '.zip' ) )
 OooiiIi1i = [ 'plugin.video.GenieTv' ]
 I1i11111i1i11 = [ "xbmc.log" , "xbmc.old.log" , "kodi.log" , "kodi.old.log" , '.DS_Store' , '.setup_complete' , 'XBMCHelper.conf' ]
 OOoOOO0 = [ 'plugin.video.GenieTv' , 'repository.origin' , 'cache' , 'system' , 'Thumbnails' , "peripheral_data" , 'library' , 'keymaps' ]
 I1I1i = [ "xbmc.log" , "xbmc.old.log" , "kodi.log" , "kodi.old.log" , "Textures13.db" , '.DS_Store' , '.setup_complete' , 'XBMCHelper.conf' , 'advancedsettings.xml' ]
 I1IIIiIiIi = "Creating full backup of existing build"
 IIIII1 = "Creating Community Build"
 iIi1Ii1i1iI = "Archiving..."
 IIiI1 = ""
 i1iI1 = "Please Wait"
 ii1I1IiiI1ii1i ( oooOOOOO , I11i1II , IIIII1 , iIi1Ii1i1iI , IIiI1 , i1iI1 , OOoOOO0 , I1I1i )
 time . sleep ( 1 )
 O0ooO0OoO00o = xbmc . translatePath ( os . path . join ( ii , oo0O0o00o0O + '_guisettings.zip' ) )
 II1iiiiII = zipfile . ZipFile ( O0ooO0OoO00o , mode = 'w' )
 try :
  II1iiiiII . write ( xbmc . translatePath ( os . path . join ( oooOOOOO , 'userdata' , 'profiles.xml' ) ) , 'profiles.xml' , zipfile . ZIP_DEFLATED )
 except : pass
 II1iiiiII . close ( )
 if ooO == 0 :
  i1iiIIiiI111 . ok ( "FAILED!" , 'The guisettings.xml file could not be found on your' , 'system, please reboot and try again.' , '' )
 else :
  i1iiIIiiI111 . ok ( "SUCCESS!" , 'You Are Now Backed Up. If you\'d like to share this build with' , 'the community please post details on the forum at' , '[COLOR=blue][B]http://rh-project.info[/COLOR][/B]' )
  i1iiIIiiI111 . ok ( "Build Locations" , 'Full Backup (only used to restore on this device): [COLOR=yellow]' + OO0O0Ooo , '[/COLOR]Universal Backup (can be used on any device): [COLOR=yellow]' + I11i1II + '[/COLOR]' )
  if 61 - 61: i1I111ii1II1i % OOOo0 - OOooOOo - OoOoOO00 % O0
def ii1I1IiiI1ii1i ( sourcefile , destfile , message_header , message1 , message2 , message3 , exclude_dirs , exclude_files ) :
 OoOOO00 = zipfile . ZipFile ( destfile , 'w' , zipfile . ZIP_DEFLATED )
 oOO0000ooooo = len ( sourcefile )
 OOO0oOOoo = [ ]
 oOOO00o000o = [ ]
 Oo0oO0ooo . create ( message_header , message1 , message2 , message3 )
 for iIi11i1 , oO00oo0o00o0o , IiIIIIIi in os . walk ( sourcefile ) :
  for file in IiIIIIIi :
   oOOO00o000o . append ( file )
 IiIi1iIIi1 = len ( oOOO00o000o )
 for iIi11i1 , oO00oo0o00o0o , IiIIIIIi in os . walk ( sourcefile ) :
  oO00oo0o00o0o [ : ] = [ O0OoO0ooOO0o for O0OoO0ooOO0o in oO00oo0o00o0o if O0OoO0ooOO0o not in exclude_dirs ]
  IiIIIIIi [ : ] = [ i1i1ii for i1i1ii in IiIIIIIi if i1i1ii not in exclude_files ]
  for file in IiIIIIIi :
   OOO0oOOoo . append ( file )
   OoOo0oOooOoOO = len ( OOO0oOOoo ) / float ( IiIi1iIIi1 ) * 100
   Oo0oO0ooo . update ( int ( OoOo0oOooOoOO ) , "Backing Up" , '[COLOR yellow]%s[/COLOR]' % file , 'Please Wait' )
   oo00ooOoO00 = os . path . join ( iIi11i1 , file )
   if not 'temp' in oO00oo0o00o0o :
    if not 'plugin.program.originwizard' in oO00oo0o00o0o :
     import time
     o00oOoOo0 = '01/01/1980'
     o0O0O0ooo0oOO = time . strftime ( '%d/%m/%Y' , time . gmtime ( os . path . getmtime ( oo00ooOoO00 ) ) )
     if o0O0O0ooo0oOO > o00oOoOo0 :
      OoOOO00 . write ( oo00ooOoO00 , oo00ooOoO00 [ oOO0000ooooo : ] )
 OoOOO00 . close ( )
 Oo0oO0ooo . close ( )
 if 97 - 97: OOOo0 / i1I111ii1II1i
 if 71 - 71: OoOoOO00 / i1IIi . ii11ii1ii % OoooooooOO . I1IiI
def Iiiiii111i1ii ( ) :
 IIIIii ( '[COLORgreen]SCOOBY STREAMS[/COLOR]' , ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvdHZjYXRzLnBocA==' ) ) , 1016 , ii11iIi1I + 'scoob.png' , i1iiIII111ii , '' )
 IIIIii ( '[COLORgreen]SCOOBY SCRAPES[/COLOR]' , iiI1IiI , 1024 , ii11iIi1I + 'scoob.png' , i1iiIII111ii , '' )
 if 25 - 25: i1I111II1I - OOO0OOo / i11iIiiIii
 if 41 - 41: i1IIi % i1I111ii1II1i + iIii1I11I1II1
def Ii1IIIIi1ii1I ( ) :
 IIIIii ( '[COLORgreen]SEARCH MOVIES[/COLOR]' , iiI1IiI , 9001 , ii11iIi1I + 'MOVIESv.png' , i1iiIII111ii , '' )
 IIIIii ( '[COLORgreen]SEARCH SERIES[/COLOR]' , iiI1IiI , 9002 , ii11iIi1I + 'TVSHOWSv.png' , i1iiIII111ii , '' )
 IIIIii ( '[COLORgreen]SEARCH CARTOONS[/COLOR]' , '' , 10005 , ii11iIi1I + 'ORIGINCARTOON' , i1iiIII111ii , '' )
 if 13 - 13: OOOo0 % I1IiI . ii11ii1ii / Oo % i1I111II1I . OoooooooOO
 if 22 - 22: OoOo00o / i11iIiiIii
 if 62 - 62: Ooo00oOo00o / ii11ii1ii
 if 7 - 7: OoooooooOO . OoOo00o
def O000OOO0OOo ( ) :
 IIIIii ( '[COLORgreen]RADIO[/COLOR]' , iiI1IiI , 1013 , ii11iIi1I + 'radio.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'CONCERTS' ) == 'true' :
  IIIIii ( '[COLORgreen]CONCERTS[/COLOR]' , ( i1111 ( 'aHR0cHM6Ly93d3cucmVkZGl0LmNvbS9yL2Z1bGxjb25jZXJ0cy8=' ) ) , 7050 , ii11iIi1I + 'concerts.png' , i1iiIII111ii , '' )
 IIIIii ( '[COLORgreen]MUSIC[/COLOR]' , iiI1IiI , 1030 , ii11iIi1I + 'MUSIC.png' , i1iiIII111ii , '' )
 IIIIii ( '[COLORgreen]MUSIC ARCHIVE[/COLOR]' , iiI1IiI + ( i1111 ( 'L3ZvZC91cmxzL211c2ljLnBocA==' ) ) , 1010 , ii11iIi1I + 'MUSIC.png' , i1iiIII111ii , '' )
 IIIIii ( '[COLORgreen]MUSIC SEARCH[/COLOR]' , iiI1IiI , 1111 , ii11iIi1I + 'search.png' , i1iiIII111ii , '' )
 IIIIii ( '[COLORgreen]KODIBLE AUDIO BOOKS[/COLOR]' , 'http://doremisa.com/audiobooks/' , 30000 , ii11iIi1I + 'kodible.png' , i1iiIII111ii , '' )
 if 32 - 32: iI * O0
 O00Oo000ooO0 ( 'movies' , 'MAIN' )
 if 100 - 100: OOO0OOo % iIii1I11I1II1 * OoOoOO00 - i1I111ii1II1i
def oo00O00oO000o ( ) :
 if 71 - 71: ii11ii1ii - OOO0OOo / I1IiI * I1IiI / i1IIi . i1IIi
 I1I1IiI1 ( 'DELETE CACHE' , 'url' , 14 , ii11iIi1I + 'MAIN5.png' , i1iiIII111ii , '' )
 I1I1IiI1 ( 'DELETE PACKAGES' , 'url' , 6 , ii11iIi1I + 'MAIN4.png' , i1iiIII111ii , '' )
 I1I1IiI1 ( 'FORCE REFRESH' , 'url' , 10 , ii11iIi1I + 'MAIN3.png' , i1iiIII111ii , 'Force Refresh All Repos' )
 if 53 - 53: o00OO00OoO
 I1I1IiI1 ( 'CHECK MY IP' , 'url' , 12 , ii11iIi1I + 'MAIN2.png' , i1iiIII111ii , '' )
 I1I1IiI1 ( 'ANDROID ONLY DELETE TEXTURE13.DB&THUBMNAIL FOLDER' , 'url' , 13 , ii11iIi1I + 'MAIN1.png' , i1iiIII111ii , 'Only Works On Android On Windows It Deletes Your Thumnails Folder But Does Not Delete The Textures13.db' )
 IIIIii ( '[COLORgreen]ADVANCED SETTINGS XML[/COLOR]' , iiI1IiI , 4 , ii11iIi1I + 'XML.png' , i1iiIII111ii , '' )
 IIIIii ( '[COLORgreen]URL FIXES[/COLOR]' , iiI1IiI , 20 , ii11iIi1I + 'URLFIX.png' , i1iiIII111ii , '' )
 O00Oo000ooO0 ( 'movies' , 'MAIN' )
 if 21 - 21: Oooo0Ooo000
 if 92 - 92: i11iIiiIii / o00OO00OoO - i1I111ii1II1i % OOO0OOo * o00OO00OoO + Oo
def iI1Ii11111iIi ( ) :
 IIIIii ( '[COLORgreen]REPOS[/COLOR]' , ( i1111 ( 'aHR0cDovL21pcnJvcnMua29kaS50di9hZGRvbnMv' ) ) , 2030 , ii11iIi1I + 'repos.png' , i1iiIII111ii , '' )
 IIIIii ( '[COLORgreen]NEW[/COLOR]' , iiI1IiI , 22 , ii11iIi1I + 'NEW.png' , i1iiIII111ii , '' )
 IIIIii ( '[COLORgreen]IPTV[/COLOR]' , iiI1IiI , 23 , ii11iIi1I + 'IPTV.png' , i1iiIII111ii , '' )
 IIIIii ( '[COLORgreen]VIDEO[/COLOR]' , iiI1IiI , 24 , ii11iIi1I + 'VIDEO.png' , i1iiIII111ii , '' )
 IIIIii ( '[COLORgreen]SPORTS[/COLOR]' , iiI1IiI , 25 , ii11iIi1I + 'SPORTS.png' , i1iiIII111ii , '' )
 IIIIii ( '[COLORgreen]KIDS[/COLOR]' , iiI1IiI , 26 , ii11iIi1I + 'KIDS.png' , i1iiIII111ii , '' )
 IIIIii ( '[COLORgreen]MUSIC[/COLOR]' , iiI1IiI , 27 , ii11iIi1I + 'MUSIC.png' , i1iiIII111ii , '' )
 IIIIii ( '[COLORgreen]PROGRAMS[/COLOR]' , iiI1IiI , 28 , ii11iIi1I + 'PROGRAMS.png' , i1iiIII111ii , '' )
 IIIIii ( '[COLORgreen]XXX[/COLOR]' , 'URL' , 29 , ii11iIi1I + 'XXX.png' , i1iiIII111ii , '' )
 O00Oo000ooO0 ( 'movies' , 'MAIN' )
 if 11 - 11: OoooooooOO . o00OO00OoO
 if 80 - 80: OoooooooOO - i1I111II1I * iI * ii11ii1ii / OOOo0 / i1I111II1I
def I1I11iI11iI1i ( ) :
 I1I1IiI1 ( 'CHECK ADVANCED XML' , iiI1IiI , 8 , ii11iIi1I + 'XML.png' , i1iiIII111ii , '' )
 I1I1IiI1 ( 'MUCKYS XML' , iiI1IiI + '/wizard/muckys.xml' , 7 , ii11iIi1I + 'XML.png' , i1iiIII111ii , '' )
 I1I1IiI1 ( '0CACHE XML' , iiI1IiI + '/wizard/0cache.xml' , 7 , ii11iIi1I + 'XML.png' , i1iiIII111ii , '' )
 I1I1IiI1 ( 'MIKEY1234 XML' , iiI1IiI + '/wizard/mikey.xml' , 7 , ii11iIi1I + 'XML.png' , i1iiIII111ii , '' )
 I1I1IiI1 ( 'TUXENS XML' , iiI1IiI + '/wizard/tuxens.xml' , 7 , ii11iIi1I + 'XML.png' , i1iiIII111ii , '' )
 I1I1IiI1 ( 'P2P RECOMMENDED XML1' , iiI1IiI + '/wizard/p2p1.xml' , 7 , ii11iIi1I + 'XML.png' , i1iiIII111ii , '' )
 I1I1IiI1 ( 'P2P RECOMMENDED XML2' , iiI1IiI + '/wizard/p2p2.xml' , 7 , ii11iIi1I + 'XML.png' , i1iiIII111ii , '' )
 I1I1IiI1 ( 'DELETE XML' , iiI1IiI , 11 , ii11iIi1I + 'XML.png' , i1iiIII111ii , '' )
 O00Oo000ooO0 ( 'movies' , 'MAIN' )
 if 75 - 75: OoooooooOO * OoOo00o
def I1Iiiiiii ( ) :
 I1I1IiI1 ( '[COLORgreen]My Local Zip[/COLOR]' , I11 , 48 , ii11iIi1I + 'MB.png' , i1iiIII111ii , '' )
 I1I1IiI1 ( '[COLORgreen]My Online Zip[/COLOR]' , i11 , 43 , ii11iIi1I + 'MB.png' , i1iiIII111ii , '' )
 if 39 - 39: OoOo00o * Oo + iIii1I11I1II1 - OoOo00o + i1I111II1I
def o0iiiI1I1iIIIi1 ( ) :
 I1I1IiI1 ( 'INSTALL FTV GUIDE AND OTHER ADDONS REQUIRED' , iiI1IiI + '/wizard/customftv/ftvguide-addons.zip' , 5 , ii11iIi1I + 'FTV4.png' , i1iiIII111ii , '' )
 I1I1IiI1 ( 'FTV GUIDE FIRST RUN SETTINGS' , iiI1IiI + '/wizard/customftv/settings.xml' , 17 , ii11iIi1I + 'FTV3.png' , i1iiIII111ii , '' )
 I1I1IiI1 ( 'FTV GUIDE ADDONS2.INI UPDATE DAILY' , 'http://ren.byethost12.com/addons2.ini' , 16 , ii11iIi1I + 'FTV1.png' , i1iiIII111ii , '' )
 I1I1IiI1 ( 'RESET FTV DATABASE' , 'url' , 18 , ii11iIi1I + 'FTV2.png' , i1iiIII111ii , '' )
 if 17 - 17: iIii1I11I1II1 . OoooooooOO / Oooo0Ooo000 % OoOoOO00 % i1IIi / i11iIiiIii
 if 58 - 58: Oo . OoOoOO00 + O0ooOooooO - i11iIiiIii / OoOoOO00 / O0
 if 85 - 85: I1IiI + i1I111II1I
def I1II ( ) :
 IIIIii ( '[COLORgreen]SKINS[/COLOR]' , iiI1IiI , 33 , ii11iIi1I + 'skinp.png' , i1iiIII111ii , '' )
 IIIIii ( '[COLORgreen]ARTWORK PACKS[/COLOR]' , iiI1IiI , 34 , ii11iIi1I + 'artp.png' , i1iiIII111ii , '' )
 IIIIii ( '[COLORgreen]CREATE UNIVERSAL PATHS[/COLOR]' , oooOOOOO , 35 , ii11iIi1I + 'GUI.png' , i1iiIII111ii , '' )
 O00Oo000ooO0 ( 'movies' , 'MAIN' )
 if 27 - 27: OoOoOO00 / iI . i1I111II1I
def i1II11II ( url ) :
 oOo00O000Oo0 = O0Oooo0O ( I1iI1I1I1i11i ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 O0o = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( oOo00O000Oo0 )
 for I1iI1iIi111i , url , OOO0000oO , iI1i111I1Ii , oo00o0 in O0o :
  IIIIii ( I1iI1iIi111i , url , 5 , OOO0000oO , iI1i111I1Ii , oo00o0 )
 O00Oo000ooO0 ( 'movies' , 'MAIN' )
 if 39 - 39: OoOoOO00 / OoOo00o + iI
def OOoO000 ( ) :
 IIIIii ( '[COLORgreen]GOTHAM SKINS[/COLOR]' , iiI1IiI , 36 , ii11iIi1I + 'GSKIN.png' , i1iiIII111ii , '' )
 IIIIii ( '[COLORgreen]HELIX SKINS[/COLOR]' , iiI1IiI , 37 , ii11iIi1I + 'HSKIN.png' , i1iiIII111ii , '' )
 IIIIii ( '[COLORgreen]ISENGAARD SKINS[/COLOR]' , oooOOOOO , 38 , ii11iIi1I + 'ISKIN.png' , i1iiIII111ii , '' )
 O00Oo000ooO0 ( 'movies' , 'MAIN' )
 if 57 - 57: OoOoOO00
def oOOOoo ( url ) :
 oOo00O000Oo0 = O0Oooo0O ( iiI1IiI + Ii1ii111i1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 O0o = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( oOo00O000Oo0 )
 for I1iI1iIi111i , url , OOO0000oO , iI1i111I1Ii , oo00o0 in O0o :
  IIIIii ( I1iI1iIi111i , url , 42 , OOO0000oO , iI1i111I1Ii , oo00o0 )
 O00Oo000ooO0 ( 'movies' , 'MAIN' )
 if 31 - 31: i1I111II1I + O0
def oO0oOOoo00000 ( url ) :
 oOo00O000Oo0 = O0Oooo0O ( iiI1IiI + oOo00 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 O0o = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( oOo00O000Oo0 )
 for I1iI1iIi111i , url , OOO0000oO , iI1i111I1Ii , oo00o0 in O0o :
  IIIIii ( I1iI1iIi111i , url , 42 , OOO0000oO , iI1i111I1Ii , oo00o0 )
 O00Oo000ooO0 ( 'movies' , 'MAIN' )
 if 3 - 3: i1I111ii1II1i % i1IIi
def Ii1IIiiIIi ( url ) :
 oOo00O000Oo0 = O0Oooo0O ( iiI1IiI + Oo000o ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 O0o = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( oOo00O000Oo0 )
 for I1iI1iIi111i , url , OOO0000oO , iI1i111I1Ii , oo00o0 in O0o :
  IIIIii ( I1iI1iIi111i , url , 42 , OOO0000oO , iI1i111I1Ii , oo00o0 )
 O00Oo000ooO0 ( 'movies' , 'MAIN' )
 if 39 - 39: ii11ii1ii
def O0oOo00o0 ( url ) :
 oOo00O000Oo0 = O0Oooo0O ( i1111 ( 'aHR0cHM6Ly9kbC5kcm9wYm94dXNlcmNvbnRlbnQuY29tL3MvN2ZrMjhndDlwb3QxMjJhL0JVSUxEUy50eHQ/ZGw9MA==' ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 O0o = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( oOo00O000Oo0 )
 for I1iI1iIi111i , url , OOO0000oO , iI1i111I1Ii , oo00o0 in O0o :
  IIIIii ( I1iI1iIi111i , url , 42 , OOO0000oO , iI1i111I1Ii , oo00o0 )
 O00Oo000ooO0 ( 'movies' , 'MAIN' )
 if 65 - 65: OoOoOO00 . OOOo0 % O0ooOooooO * Ooo00oOo00o
def iI11I ( url ) :
 oOo00O000Oo0 = O0Oooo0O ( iiI1IiI + I1IIIiii1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 O0o = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( oOo00O000Oo0 )
 for I1iI1iIi111i , url , OOO0000oO , iI1i111I1Ii , oo00o0 in O0o :
  IIIIii ( I1iI1iIi111i , url , 40 , OOO0000oO , iI1i111I1Ii , oo00o0 )
 O00Oo000ooO0 ( 'movies' , 'MAIN' )
 if 65 - 65: Oooo0Ooo000 / OoOoOO00 * iI . i1I111ii1II1i * O0ooOooooO % i1I111II1I
def O0oOOo0Oo ( url ) :
 oOo00O000Oo0 = O0Oooo0O ( iiI1IiI + o000O000 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 O0o = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( oOo00O000Oo0 )
 for I1iI1iIi111i , url , OOO0000oO , iI1i111I1Ii , oo00o0 in O0o :
  IIIIii ( I1iI1iIi111i , url , 5 , OOO0000oO , iI1i111I1Ii , oo00o0 )
 O00Oo000ooO0 ( 'movies' , 'MAIN' )
 if 19 - 19: iIii1I11I1II1
def Ii1IiI1i1ii ( ) :
 OO0oo = Iii1 ( i1111 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vYXBrdG9vbC9hcGsucGhw' ) )
 O0o = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( OO0oo )
 for oOo0 , II1iI , I1iI1iIi111i in O0o :
  I1I1i1I ( I1iI1iIi111i , oOo0 , 2031 , II1iI )
  if 87 - 87: O0 / iIii1I11I1II1 * i1IIi
def IIi11IIiIii1 ( name , url , description ) :
 O0O0Oo00 = xbmc . translatePath ( os . path . join ( I1iIII1 , 'Download' ) )
 Oo0oO0ooo = xbmcgui . DialogProgress ( )
 Oo0oO0ooo . create ( "Your App Is Downloading" , "Why not check out our website" , '' , 'Http://architects.x10host.com' )
 iIii = os . path . join ( O0O0Oo00 , name + '.apk' )
 try :
  os . remove ( iIii )
 except :
  pass
 downloader . download ( url , iIii , Oo0oO0ooo )
 i1iiIIiiI111 = xbmcgui . Dialog ( )
 i1iiIIiiI111 . ok ( "GenieTv" , "[COLORred]Please press ok, exit kodi and go to your downloads folder to install your app[/COLOR]" , "[COLORblue]Tool Brought To You By Architects@Work[/COLOR]" )
 if 84 - 84: O0ooOooooO % i1IIi
def oOO ( url ) :
 O0O0Oo00 = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/resources/downloads' ) )
 Oo0oO0ooo = xbmcgui . DialogProgress ( )
 Oo0oO0ooo . create ( "Your fILM Is Downloading" , "Why not check out our website" , '' , 'Http://architects.x10host.com' )
 iIii = os . path . join ( O0O0Oo00 , I1iI1iIi111i + '.mp4' )
 try :
  os . remove ( iIii )
 except :
  pass
 downloader . download ( url , iIii , Oo0oO0ooo )
 i1iiIIiiI111 = xbmcgui . Dialog ( )
 i1iiIIiiI111 . ok ( "GenieTv" , "[COLORred]Please press ok, Your download With Be Avaiilable Via The My Downloads Button[/COLOR]" , "[COLORblue]Tool Brought To You By Architects@Work[/COLOR]" )
 if 17 - 17: OoOoOO00 / ii11ii1ii % OoOo00o + OOOo0 * o00OO00OoO
 if 36 - 36: o00OO00OoO * Ooo00oOo00o
def I1I ( name , url , description ) :
 O0O0Oo00 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 Oo0oO0ooo = xbmcgui . DialogProgress ( )
 Oo0oO0ooo . create ( "Your Art Pack Is Downloading" , "Why not check out our website" , '' , 'Http://architects.x10host.com' )
 iIii = os . path . join ( O0O0Oo00 , name )
 try :
  os . remove ( iIii )
 except :
  pass
 downloader . download ( url , iIii , Oo0oO0ooo )
 ii1iIi1II = xbmc . translatePath ( os . path . join ( oo00 ) )
 time . sleep ( 2 )
 Oo0oO0ooo . update ( 0 , "" , "Placing Your Art Please Wait" )
 print '======================================='
 print ii1iIi1II
 print '======================================='
 extract . all ( iIii , ii1iIi1II , Oo0oO0ooo )
 i1iiIIiiI111 = xbmcgui . Dialog ( )
 i1iiIIiiI111 . ok ( "GenieTv" , "[COLORred]Once complete your artwork will be stored in your Media folder, Accessible via the Homefolder, Enjoy[/COLOR]" )
 if 2 - 2: Oo + I1IiI - i1I111II1I . OOOo0 - i1I111II1I
 if 67 - 67: iIii1I11I1II1 - i1I111ii1II1i
def Iii ( url ) :
 oOo00O000Oo0 = O0Oooo0O ( i1111 ( 'aHR0cDovL2dlbmlldHYuYXJjaGl0ZWN0cy54MTBob3N0LmNvbS90ZXN0L3doLnR4dA==' ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 O0o = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( oOo00O000Oo0 )
 for I1iI1iIi111i , url , OOO0000oO , iI1i111I1Ii , oo00o0 in O0o :
  IIIIii ( I1iI1iIi111i , url , 5 , OOO0000oO , iI1i111I1Ii , oo00o0 )
 try :
  oOo00O000Oo0 = O0Oooo0O ( iIi1i + oO0o0o0ooO0oO + i1ii ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
  O0o = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( oOo00O000Oo0 )
  for I1iI1iIi111i , url , OOO0000oO , iI1i111I1Ii , oo00o0 in O0o :
   IIIIii ( I1iI1iIi111i , url , 5 , OOO0000oO , iI1i111I1Ii , oo00o0 )
 except : pass
 O00Oo000ooO0 ( 'movies' , 'INFO' )
 if 68 - 68: i1I111II1I * O0 . Oooo0Ooo000 - OoOoOO00 . OOO0OOo / OoOoOO00
 if 47 - 47: OoooooooOO
def ii1i1i1IiII ( url ) :
 oOo00O000Oo0 = O0Oooo0O ( i1111 ( 'aHR0cDovL2dlbmlldHYuYXJjaGl0ZWN0cy54MTBob3N0LmNvbS90ZXN0L3doLnR4dA==' ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 O0o = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( oOo00O000Oo0 )
 for I1iI1iIi111i , url , OOO0000oO , iI1i111I1Ii , oo00o0 in O0o :
  IIIIii ( I1iI1iIi111i , url , 43 , OOO0000oO , iI1i111I1Ii , oo00o0 )
 try :
  oOo00O000Oo0 = O0Oooo0O ( iIi1i + oO0o0o0ooO0oO + i1ii ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
  O0o = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( oOo00O000Oo0 )
  for I1iI1iIi111i , url , OOO0000oO , iI1i111I1Ii , oo00o0 in O0o :
   IIIIii ( I1iI1iIi111i , url , 43 , OOO0000oO , iI1i111I1Ii , oo00o0 )
 except : pass
 O00Oo000ooO0 ( 'movies' , 'INFO' )
 if 63 - 63: i1I111ii1II1i . Ooo00oOo00o / OoOoOO00 * OoOo00o + O0ooOooooO % iI
 if 12 - 12: o00OO00OoO . Ooo00oOo00o . i1I111ii1II1i - OoooooooOO % Oo
def i11i1iIiii ( name , url , description ) :
 O0O0Oo00 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 Oo0oO0ooo = xbmcgui . DialogProgress ( )
 Oo0oO0ooo . create ( "GenieTv" , "Downloading Content" , '' , 'Please Wait' )
 iIii = os . path . join ( O0O0Oo00 , name + '.zip' )
 try :
  os . remove ( iIii )
 except :
  pass
 downloader . download ( url , iIii , Oo0oO0ooo )
 OOO00OO0oOo = xbmc . translatePath ( os . path . join ( 'special://home' , 'addons' ) )
 time . sleep ( 2 )
 Oo0oO0ooo . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print OOO00OO0oOo
 print '======================================='
 extract . all ( iIii , OOO00OO0oOo , Oo0oO0ooo )
 i1iiIIiiI111 = xbmcgui . Dialog ( )
 i1iiIIiiI111 . ok ( "GenieTv" , "Press ok to finish install" , "[COLOR yellow]Brought To You By Architects@Work[/COLOR]" )
 oOooOOOoOo ( )
 if 35 - 35: i1I111ii1II1i + OOO0OOo - O0ooOooooO . i1I111ii1II1i . OoOo00o
 if 87 - 87: I1IiI
def IioO0O ( name , url , description ) :
 O0O0Oo00 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 Oo0oO0ooo = xbmcgui . DialogProgress ( )
 Oo0oO0ooo . create ( "GenieTv" , "Downloading " , '' , 'Please Wait' )
 iIii = os . path . join ( O0O0Oo00 , 'plugin.program.GenieTv.install' + '.zip' )
 try :
  os . remove ( iIii )
 except :
  pass
 downloader . download ( url , iIii , Oo0oO0ooo )
 OOO00OO0oOo = xbmc . translatePath ( os . path . join ( 'special://' , 'home' ) )
 time . sleep ( 2 )
 Oo0oO0ooo . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print OOO00OO0oOo
 print '======================================='
 extract . all ( iIii , OOO00OO0oOo , Oo0oO0ooo )
 i1iiIIiiI111 = xbmcgui . Dialog ( )
 i1iiIIiiI111 . ok ( "GenieTv" , "Press ok to force close kodi, if unsuccessful using windows Please kill kodi via taskmanager" , "[COLOR yellow]Brought To You By Architects@Work[/COLOR]" )
 oOOiiiIIiIi ( )
 if 68 - 68: O0 + I1IiI / O0ooOooooO - i1I111II1I + iIii1I11I1II1 % iI
def i1iI1iii11i ( name , url , description ) :
 O0O0Oo00 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 Oo0oO0ooo = xbmcgui . DialogProgress ( )
 Oo0oO0ooo . create ( "GenieTv" , "Downloading " , '' , 'Please Wait' )
 iIii = os . path . join ( O0O0Oo00 , 'plugin.program.GenieTv.install' + '.zip' )
 try :
  os . remove ( iIii )
 except :
  pass
 downloader . download ( url , iIii , Oo0oO0ooo )
 OOO00OO0oOo = xbmc . translatePath ( os . path . join ( 'special://' , 'home' ) )
 time . sleep ( 2 )
 Oo0oO0ooo . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print OOO00OO0oOo
 print '======================================='
 extract . all ( iIii , OOO00OO0oOo , Oo0oO0ooo )
 i1iiIIiiI111 = xbmcgui . Dialog ( )
 i1iiIIiiI111 . ok ( "GenieTv" , "Please Disconnect The Power From Your Device. DO NOT EXIT CLEANLY VIA SHUTDOWN" , "[COLOR yellow]Brought To You By Architects@Work[/COLOR]" )
 if 62 - 62: Oo * I1IiI
 if 79 - 79: Ooo00oOo00o . i1I111ii1II1i * iI - i1I111II1I + OOO0OOo
def ii11II1i ( name , url , description ) :
 OOO00OO0oOo = xbmc . translatePath ( os . path . join ( 'special://' , 'home' ) )
 Oo0oO0ooo = xbmcgui . DialogProgress ( )
 iIii = os . path . join ( I11 )
 time . sleep ( 2 )
 Oo0oO0ooo . create ( "GenieTv" , "Restoring" , '' , 'Please Wait' )
 print '======================================='
 print OOO00OO0oOo
 print '======================================='
 extract . all ( iIii , OOO00OO0oOo , Oo0oO0ooo )
 i1iiIIiiI111 = xbmcgui . Dialog ( )
 i1iiIIiiI111 . ok ( "GenieTv" , "Please Disconnect The Power From Your Device. DO NOT EXIT CLEANLY VIA SHUTDOWN" , "[COLOR yellow]Brought To You By Architects@Work[/COLOR]" )
 if 58 - 58: Oo . OoOo00o - Oo - o00OO00OoO * iI
 if 28 - 28: I1IiI * Ooo00oOo00o . Oooo0Ooo000 % Oooo0Ooo000 / Oooo0Ooo000 * o00OO00OoO
def oOOiiiIIiIi ( ) :
 ooO00O0O0 = xbmcgui . Dialog ( ) . yesno ( 'Force Close Kodi' , 'You are about to close Kodi' , 'Would you like to continue?' , nolabel = 'No, Cancel' , yeslabel = 'Yes, Close' )
 if ooO00O0O0 == 0 :
  return
 elif ooO00O0O0 == 1 :
  pass
 iII1I1 = o0Ooo0o0ooo0 ( )
 print "Platform: " + str ( iII1I1 )
 if iII1I1 == 'osx' :
  print "############   try osx force close  #################"
  try : os . system ( 'killall -9 XBMC' )
  except : pass
  try : os . system ( 'killall -9 Kodi' )
  except : pass
  i1iiIIiiI111 . ok ( "[COLOR=red][B]WARNING  !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu." , '' )
 elif iII1I1 == 'linux' :
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
 elif iII1I1 == 'android' :
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
 elif iII1I1 == 'windows' :
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
  if 70 - 70: i11iIiiIii % i1I111ii1II1i
def o0Ooo0o0ooo0 ( ) :
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
  if 11 - 11: OoOo00o % ii11ii1ii % iI / OoOoOO00 % o00OO00OoO - Oo
  if 96 - 96: ii11ii1ii / OoOoOO00 . iI - i1I111ii1II1i * Oooo0Ooo000 * O0ooOooooO
  if 76 - 76: iI - OoOoOO00 * i1I111II1I / OoooooooOO
def IIIiIi ( url ) :
 Oo0oO0ooo . create ( "[COLOR=green]GenieTv[/COLOR]" , "Renaming paths..." , '' , 'Please Wait' )
 for IiiIIIII1iii , oO00oo0o00o0o , IiIIIIIi in os . walk ( url ) :
  for file in IiIIIIIi :
   if file . endswith ( ".xml" ) :
    Oo0oO0ooo . update ( 0 , "Fixing" , file , 'Please Wait' )
    iII1ii1 = open ( ( os . path . join ( IiiIIIII1iii , file ) ) ) . read ( )
    IIiiii = iII1ii1 . replace ( oooOOOOO , 'special://home/' )
    i1i1ii = open ( ( os . path . join ( IiiIIIII1iii , file ) ) , mode = 'w' )
    i1i1ii . write ( str ( IIiiii ) )
    i1i1ii . close ( )
 oOOiiiIIiIi ( )
 if 37 - 37: OOooOOo % OOO0OOo
def O0II11i11II ( ) :
 OO0oo = Iii1 ( i1111 ( 'aHR0cDovL3d3dy5saXN0ZW5saXZlLmV1L3VrLmh0bWw=' ) )
 O0o = re . compile ( '<tr>.+?<td><a href=".+?"><b>(.+?)</b>.+?<td><a href="(.+?)">' , re . DOTALL ) . findall ( OO0oo )
 for I1iI1iIi111i , oOo0 in O0o :
  II1Ii1iI1i1 ( I1iI1iIi111i , oOo0 , 222 , ii11iIi1I + 'radio.png' )
  if 54 - 54: O0
def OOoO000O00oO ( ) :
 OO0oo = Iii1 ( i1111 ( 'aHR0cDovL3d3dy50b29uamV0LmNvbS8=' ) )
 O0o = re . compile ( '<a href="(.+?)" style="font-size:.8em;">(.+?)</a>' ) . findall ( OO0oo )
 for oOo0 , I1iI1iIi111i in O0o :
  I1I1i1I ( '[COLORgreen]' + I1iI1iIi111i + '[/COLOR]' , 'http://www.toonjet.com/' + oOo0 , 8051 , ii11iIi1I + 'classictoons.png' )
def i1OoOO ( url ) :
 OO0oo = Iii1 ( url )
 O0o = re . compile ( '<a href="(.+?)"><img src="(.+?)"' ) . findall ( OO0oo )
 IIIIiiIiiI = re . compile ( '<a href="(.+?)">.+?</a></td></tr></table>' ) . findall ( OO0oo )
 for url , OO0ooOOO0OOO in O0o :
  if 'ol.gif' in OO0ooOOO0OOO :
   pass
  elif 'link_block_' in OO0ooOOO0OOO :
   pass
  elif '.png' in OO0ooOOO0OOO :
   pass
  else :
   I1I1i1I ( ( OO0ooOOO0OOO ) . replace ( 'http://www.toonjet.com/images/icons/' , '' ) . replace ( 'images/icons/' , '' ) . replace ( '.jpg' , '' ) . replace ( '_icon' , '' ) . replace ( '_' , ' ' ) , 'http://www.toonjet.com/' + url , 8052 , ii11iIi1I + 'vod.png' )
 for url in IIIIiiIiiI :
  I1I1i1I ( 'NEXT PAGE' , 'http://www.toonjet.com/' + url , 8051 , ii11iIi1I + 'Next.png' )
def iIII1I1i1i ( url ) :
 OO0oo = Iii1 ( url )
 O0o = re . compile ( '<iframe width="640" height="480" src="(.+?)" frameborder="0" allowfullscreen></iframe>' ) . findall ( OO0oo )
 for url in O0o :
  II1Ii1iI1i1 ( '[COLORgreen]PLAY[/COLOR]' , ( url ) . replace ( 'http://www.youtube.com/embed/' , '' ) . replace ( '?autoplay=0' , '' ) , 8043 , ii11iIi1I + 'classictoons.png' )
  if 79 - 79: iI . Ooo00oOo00o
  if 40 - 40: OOooOOo + Oo . OOooOOo % OOO0OOo
def I11I1IIiiII1 ( ) :
 IIIIIii1ii11 ( 'Audio Books' , '' , 30011 , ii11iIi1I + 'audiobooks.png' , ii11iIi1I + 'audiobooks.png' , '' )
 IIIIIii1ii11 ( 'Kids Audio Books' , '' , 30006 , ii11iIi1I + 'kidsaudiobooks.png' , ii11iIi1I + 'kidsaudiobooks.png' , '' )
 if 86 - 86: I1IiI * OoOoOO00 - O0 . I1IiI % iIii1I11I1II1 / i1I111II1I
def IiIIiIIIiIii ( ) :
 IIIIIii1ii11 ( 'All' , '' , 30001 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
 IIIIIii1ii11 ( 'Popular' , '' , 30012 , ii11iIi1I + 'POPULARv.png' , ii11iIi1I + 'POPULARv.png' , '' )
 IIIIIii1ii11 ( 'Search' , '' , 30013 , ii11iIi1I + 'search.png' , ii11iIi1I + 'search.png' , '' )
 if 23 - 23: i1I111ii1II1i + Oooo0Ooo000 . I1IiI * OOOo0 + ii11ii1ii
def I1iIi1iiiIiI ( ) :
 I11i1ii1 = O0Oooo0O ( II11iiii1Ii + 'books' + OooO0 )
 O0o = re . compile ( '<NAME=>(.*?)</NAME><URL=>(.*?)</URL><CAT=>(.*?)</CAT>' ) . findall ( I11i1ii1 )
 for I1iI1iIi111i , oOo0 , III1I1Ii11iI in O0o :
  if 'Parent' in I1iI1iIi111i :
   pass
  elif '2' in III1I1Ii11iI :
   IIIIIii1ii11 ( ( I1iI1iIi111i ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , oOo0 , 30010 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
   if 52 - 52: i1I111II1I - i1I111ii1II1i * O0ooOooooO
def Ii1I11I ( ) :
 IiII111iI1ii1 = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 Ii1I = IiII111iI1ii1 . lower ( )
 I11i1ii1 = O0Oooo0O ( II11iiii1Ii + 'books' + OooO0 )
 O0o = re . compile ( '<NAME=>(.*?)</NAME><URL=>(.*?)</URL><CAT=>(.*?)</CAT>' ) . findall ( I11i1ii1 )
 for I1iI1iIi111i , oOo0 , III1I1Ii11iI in O0o :
  if IiII111iI1ii1 in I1iI1iIi111i . lower ( ) :
   if '1' in III1I1Ii11iI :
    IIIIIii1ii11 ( ( I1iI1iIi111i ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , oOo0 , 30010 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
   elif '2' in III1I1Ii11iI :
    IIIIIii1ii11 ( ( I1iI1iIi111i ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , oOo0 , 30010 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
   elif '3' in III1I1Ii11iI :
    IIIIIii1ii11 ( ( I1iI1iIi111i ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , oOo0 , 30009 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
    if 36 - 36: O0 + Oo
    if 5 - 5: Oo * I1IiI
def ii1I11iIiIII1 ( ) :
 I11i1ii1 = O0Oooo0O ( II11iiii1Ii + 'books' + OooO0 )
 O0o = re . compile ( '<NAME=>(.*?)</NAME><URL=>(.*?)</URL><CAT=>(.*?)</CAT>' ) . findall ( I11i1ii1 )
 for I1iI1iIi111i , oOo0 , III1I1Ii11iI in O0o :
  if '1' in III1I1Ii11iI :
   IIIIIii1ii11 ( ( I1iI1iIi111i ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , oOo0 , 3010 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
  elif '2' in III1I1Ii11iI :
   IIIIIii1ii11 ( ( I1iI1iIi111i ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , oOo0 , 30010 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
  elif '3' in III1I1Ii11iI :
   IIIIIii1ii11 ( ( I1iI1iIi111i ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , oOo0 , 30009 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
   if 52 - 52: OOooOOo * OoOo00o + I1IiI
 xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 49 - 49: iIii1I11I1II1 - O0 . i1IIi - OoooooooOO
def Ii1 ( url ) :
 IIo0o0O0O00oOOo = url
 I11i1ii1 = O0Oooo0O ( url )
 IIIIiiIiiI = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( I11i1ii1 )
 for url , I1iI1iIi111i in IIIIiiIiiI :
  if 'mp3' in I1iI1iIi111i :
   IIIIii ( ( I1iI1iIi111i ) . replace ( '%20' , ' ' ) , IIo0o0O0O00oOOo + url , 10012 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
  if 'wma' in I1iI1iIi111i :
   IIIIii ( ( I1iI1iIi111i ) . replace ( '%20' , ' ' ) , IIo0o0O0O00oOOo + url , 10012 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
  if 'm4b' in I1iI1iIi111i :
   IIIIii ( ( I1iI1iIi111i ) . replace ( '%20' , ' ' ) , IIo0o0O0O00oOOo + url , 10012 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
  elif '/' in I1iI1iIi111i :
   IIIIIii1ii11 ( ( I1iI1iIi111i ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , IIo0o0O0O00oOOo + url , 30009 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
   if 73 - 73: i1IIi + i1I111ii1II1i . i11iIiiIii
   if 5 - 5: O0ooOooooO . ii11ii1ii . OoOoOO00 . OoooooooOO
   if 96 - 96: i11iIiiIii - i1I111II1I % O0 / Ooo00oOo00o
def O0O0 ( url ) :
 I11i1ii1 = O0Oooo0O ( url )
 IIo0o0O0O00oOOo = url
 O0o = re . compile ( '<li><a href="(.+?)">(.+?)</a></li>' ) . findall ( I11i1ii1 )
 for url , I1iI1iIi111i in O0o :
  if 'Parent' in I1iI1iIi111i :
   pass
  elif '.db' in I1iI1iIi111i :
   pass
  elif '.jpg' in I1iI1iIi111i :
   pass
  elif '.html' in I1iI1iIi111i :
   pass
  elif '.doc' in I1iI1iIi111i :
   pass
  elif 'mp3' in I1iI1iIi111i :
   IIIIii ( ( I1iI1iIi111i ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , IIo0o0O0O00oOOo + url , 10012 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
  elif 'm4a' in I1iI1iIi111i :
   IIIIii ( ( I1iI1iIi111i ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , IIo0o0O0O00oOOo + url , 10012 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
  else :
   IIIIIii1ii11 ( ( I1iI1iIi111i ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , IIo0o0O0O00oOOo + url , 30010 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
   if 83 - 83: OoOoOO00 - Oooo0Ooo000
   if 35 - 35: i1IIi - iIii1I11I1II1 + i1IIi
def OooOOo0 ( ) :
 IIIIIii1ii11 ( 'A-Z' , '' , 7 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
 IIIIIii1ii11 ( 'All' , '' , 3 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
 IIIIIii1ii11 ( 'Search' , '' , 14 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
 if 51 - 51: I1IiI
def I11IIIiIi11 ( ) :
 I11i1ii1 = O0Oooo0O ( i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9tcDNfZG93bmxvYWRzLmh0bQ==' ) )
 O0o = re . compile ( '<td width=".+?" align="center">.+?<a href="(.*?)">.+?<img border="0" src="images/Squeeze%20(.*?).gif" width="74" height=".*?"></a></td>' , re . DOTALL ) . findall ( I11i1ii1 )
 for oOo0 , OO0ooOOO0OOO in O0o :
  print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<' + oOo0 + '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
  if '-x' in OO0ooOOO0OOO :
   pass
  else :
   IIIIIii1ii11 ( OO0ooOOO0OOO , ( i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) ) + ( oOo0 ) . replace ( 'colour_it' , 'books_audio/audio_books_a' ) , 30008 , ( i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9pbWFnZXMvU3F1ZWV6ZSUyMA==' ) ) + OO0ooOOO0OOO + '.gif' , ii11iIi1I + 'kodible.png' , '' )
   if 39 - 39: iI % O0 % I1IiI . i1IIi
 xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 86 - 86: Ooo00oOo00o * OoooooooOO
 if 71 - 71: iIii1I11I1II1 - i1I111II1I . OOOo0 % OoooooooOO + i1I111II1I
def IIi11I1 ( url ) :
 I11i1ii1 = O0Oooo0O ( url )
 O0o = re . compile ( '<td width=".*?" height=".*?"><b>.*?<a href="(.*?)">(.*?)</a></b></td>' , re . DOTALL ) . findall ( I11i1ii1 )
 for url , I1iI1iIi111i in O0o :
  if '</a>' in I1iI1iIi111i :
   pass
  elif '(' in I1iI1iIi111i :
   IIIIIii1ii11 ( ( I1iI1iIi111i ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '.mp3' , '' ) , i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) + url , 30005 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
  else :
   IIIIii ( ( I1iI1iIi111i ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '.mp3' , '' ) , i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) + url , 30004 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
   if 49 - 49: OoOoOO00 - OOOo0 / Oooo0Ooo000
 xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 74 - 74: Oooo0Ooo000 - i1I111II1I + i1IIi . OOOo0 + i1I111II1I - Oooo0Ooo000
def IiIiiiiI1 ( ) :
 IiII111iI1ii1 = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 Ii1I = IiII111iI1ii1 . lower ( )
 I11i1ii1 = O0Oooo0O ( i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9jb21wbGV0ZV9saXN0Lmh0bQ==' ) )
 O0o = re . compile ( '<td width=".+?">.*?<b>.+?<a href="(.*?)">(.*?)</a></b></td>' , re . DOTALL ) . findall ( I11i1ii1 )
 for oOo0 , I1iI1iIi111i in O0o :
  if IiII111iI1ii1 in I1iI1iIi111i . lower ( ) :
   if '</a>' in I1iI1iIi111i :
    pass
   elif '(' in I1iI1iIi111i :
    IIIIIii1ii11 ( ( I1iI1iIi111i ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + oOo0 , 30005 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
   else :
    IIIIii ( ( I1iI1iIi111i ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + oOo0 , 30004 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
    if 62 - 62: ii11ii1ii % i1I111ii1II1i * Ooo00oOo00o - i1IIi
    if 66 - 66: i11iIiiIii / OOooOOo - OoooooooOO / i1IIi . i11iIiiIii
def IIIII1iii11 ( ) :
 I11i1ii1 = O0Oooo0O ( i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9jb21wbGV0ZV9saXN0Lmh0bQ==' ) )
 O0o = re . compile ( '<td width=".+?">.*?<b>.+?<a href="(.*?)">(.*?)</a></b></td>' , re . DOTALL ) . findall ( I11i1ii1 )
 for oOo0 , I1iI1iIi111i in O0o :
  if '</a>' in I1iI1iIi111i :
   pass
  elif '(' in I1iI1iIi111i :
   IIIIIii1ii11 ( ( I1iI1iIi111i ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + oOo0 , 30005 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
  else :
   IIIIii ( ( I1iI1iIi111i ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + oOo0 , 30004 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
   if 35 - 35: O0ooOooooO / o00OO00OoO / OoOoOO00 - iIii1I11I1II1 + OoOoOO00 . o00OO00OoO
 xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 81 - 81: i1I111ii1II1i * i1I111II1I - ii11ii1ii * iI % I1IiI * I1IiI
 if 59 - 59: iIii1I11I1II1
def I1ii1Ii1ii11i ( url ) :
 I11i1ii1 = O0Oooo0O ( url )
 O0o = re . compile ( '<a href="(.+?)">Download</a></b></td>' ) . findall ( I11i1ii1 )
 for url in O0o :
  IIo0o0O0O00oOOo = ( i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) ) + url
  Resolve ( IIo0o0O0O00oOOo )
  if 94 - 94: OoOo00o + o00OO00OoO / i1I111II1I
def o00oiii11II1I ( url ) :
 I11i1ii1 = O0Oooo0O ( url )
 O0o = re . compile ( '<td width="247">(.*?)</td>.*?<a href="(.+?)">' , re . DOTALL ) . findall ( I11i1ii1 )
 for I1iI1iIi111i , url in O0o :
  if '<p align' in I1iI1iIi111i :
   pass
  elif '&nbsp;' in I1iI1iIi111i :
   pass
  else :
   IIIIii ( ( I1iI1iIi111i ) . replace ( '&nbsp;' , '' ) , i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) + url , 10012 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
   if 5 - 5: I1IiI - OoOo00o * OoOo00o
 xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 50 - 50: OoOoOO00 * ii11ii1ii / iI . OOooOOo + Oo - i1I111II1I
 if 18 - 18: I1IiI % i11iIiiIii % ii11ii1ii / O0ooOooooO / OOooOOo / i1IIi
def IIi1I1 ( ) :
 I11i1ii1 = cloudflare . source ( i1111 ( 'aHR0cDovL3dhdGNoY2FydG9vbnNvbmxpbmUuZXUv' ) )
 O0o = re . compile ( 'class="menu-item menu-item-type-.+?><a href="([^"]*)">(.+?)</a></li>' , re . DOTALL ) . findall ( I11i1ii1 )
 for oOo0 , I1iI1iIi111i in O0o :
  if 'ongoing' in oOo0 :
   IIIIii ( '[COLORgreen]' + I1iI1iIi111i + '[/COLOR]' , oOo0 , 21005 , ii11iIi1I + 'on-going.png' , '' , '' )
  if 'cartoon-series' in oOo0 :
   IIIIii ( '[COLORgreen]' + I1iI1iIi111i + '[/COLOR]' , oOo0 , 21005 , ii11iIi1I + 'cartoonseries.png' , '' , '' )
  if 'disney' in oOo0 :
   IIIIii ( '[COLORgreen]' + I1iI1iIi111i + '[/COLOR]' , oOo0 , 21005 , ii11iIi1I + 'disneytoons.png' , '' , '' )
  if 'genre' in oOo0 :
   IIIIii ( '[COLORgreen]' + I1iI1iIi111i + '[/COLOR]' , oOo0 , 21005 , ii11iIi1I + 'cartoongenre.png' , '' , '' )
  if 'years' in oOo0 :
   IIIIii ( '[COLORgreen]' + I1iI1iIi111i + '[/COLOR]' , oOo0 , 21005 , ii11iIi1I + 'years.png' , '' , '' )
def iIi ( url ) :
 I11i1ii1 = cloudflare . source ( url )
 O0o = re . compile ( '<a href="([^"]*)" title="([^"]*)" rel="nofollow" id="featured-thumbnail">.+?<div class="featured-thumbnail"><img width="140" height="200" src="([^"]*)"' , re . DOTALL ) . findall ( I11i1ii1 )
 iIIiooO00O00oOO = re . compile ( '<button type="button"><a href="([^"]*)" target="_blank">(.+?)</a>' ) . findall ( I11i1ii1 )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' ) . findall ( I11i1ii1 )
 for url , I1iI1iIi111i , OO0ooOOO0OOO in O0o :
  IIIIii ( '[COLORgreen]' + I1iI1iIi111i + '[/COLOR]' , url , 21006 , OO0ooOOO0OOO , OO0ooOOO0OOO , I1iI1iIi111i )
 for url , I1iI1iIi111i in iIIiooO00O00oOO :
  IIIIii ( '[COLORgreen]' + I1iI1iIi111i + '[/COLOR]' , url , 21005 , ii11iIi1I + 'watchcartoons.png' , '' , '' )
 for url in next :
  IIIIii ( '[COLORgreen]NEXT[/COLOR]' , url , 21005 , ii11iIi1I + 'Next.png' , '' , '' )
def I1 ( url ) :
 I11i1ii1 = cloudflare . source ( url )
 O0o = re . compile ( '<li><a href="([^"]*)" >(.+?)</a></li>' , re . DOTALL ) . findall ( I11i1ii1 )
 IIII1ii = re . compile ( 'file:"([^"]*)",type:"mp4",label:"([^"]*)"' , re . DOTALL ) . findall ( I11i1ii1 )
 IiIIi1I1I11Ii = re . compile ( 'src="([^"]*)" frameborder=' ) . findall ( I11i1ii1 )
 o0OO = re . compile ( '<iframe src="([^"]*)"' ) . findall ( I11i1ii1 )
 for url , I1iI1iIi111i in O0o :
  IIIIii ( '[COLORgreen]' + I1iI1iIi111i + '[/COLOR]' , url , 21007 , ii11iIi1I + 'watchcartoons.png' , '' , '' )
 for url in IiIIi1I1I11Ii :
  IIIIii ( '[COLORgreen]PLAY[/COLOR]' , 'http:' + url , 222 , ii11iIi1I + 'watchcartoons.png' , '' , '' )
 for url , I1iI1iIi111i in IIII1ii :
  I1I1IiI1 ( '[COLORgreen]' + I1iI1iIi111i + '[/COLOR]' , url , 222 , ii11iIi1I + 'watchcartoons.png' , '' , '' )
 else :
  IIIIii ( '[COLORgreen]NO STREAMS AVAILABLE[/COLOR]' , url , 21005 , ii11iIi1I + 'watchcartoons.png' , '' , '' )
def OoiiIiI ( url ) :
 I11i1ii1 = cloudflare . source ( url )
 O0o = re . compile ( 'file:"([^"]*)",type:"mp4",label:"([^"]*)"' , re . DOTALL ) . findall ( I11i1ii1 )
 for url , I1iI1iIi111i in O0o :
  I1I1IiI1 ( '[COLORgreen]' + I1iI1iIi111i + '[/COLOR]' , url , 222 , ii11iIi1I + 'watchcartoons.png' , '' , '' )
  if 87 - 87: OOO0OOo - OoooooooOO + i11iIiiIii
def O0oooo0OoO0oo ( ) :
 I1I1i1I ( '[COLORgreen]CARTOONS[/COLOR]' , '' , 20001 , ii11iIi1I + 'ORIGINCARTOON.png' )
 I1I1i1I ( '[COLORgreen]ANIME[/COLOR]' , 'https://kissanime.to/AnimeList' , 20001 , ii11iIi1I + 'ORIGINCARTOON.png' )
 if 16 - 16: OOOo0 * OoOoOO00 / iIii1I11I1II1 - i1I111ii1II1i
def IiI1IiI11iII ( ) :
 I1I1i1I ( '[COLORgreen]BY NAME[/COLOR]' , 'http://kisscartoon.me/CartoonList' , 20002 , ii11iIi1I + 'ORIGINCARTOON.png' )
 I1I1i1I ( '[COLORgreen]BY GENRE[/COLOR]' , 'http://kisscartoon.me/CartoonList' , 20003 , ii11iIi1I + 'ORIGINCARTOON.png' )
 if 64 - 64: O0ooOooooO - OOOo0 / i1I111ii1II1i - Ooo00oOo00o
def ii11I ( url ) :
 I11i1ii1 = cloudflare . source ( url )
 O0o = re . compile ( 'href="(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( I11i1ii1 )
 for url , I1iI1iIi111i in O0o :
  if '?c=' in url :
   I1I1i1I ( '[COLORgreen]' + I1iI1iIi111i + '[/COLOR]' , 'http://kisscartoon.me' + url , 20004 , ii11iIi1I + 'ORIGINCARTOON.png' )
   if 47 - 47: o00OO00OoO
def oOiI ( url ) :
 I11i1ii1 = cloudflare . source ( url )
 O0o = re . compile ( 'href="(.+?)" title="(.+?)">/n(.+?)</a><br/>' , re . DOTALL ) . findall ( I11i1ii1 )
 for url , Ii1IIi , I1iI1iIi111i in O0o :
  if 'Genre' in url :
   I1I1i1I ( '[COLORgreen]' + I1iI1iIi111i + '[/COLOR]' , 'http://kisscartoon.me' + url , 20004 , ii11iIi1I + 'ORIGINCARTOON.png' )
   if 43 - 43: o00OO00OoO % i1I111ii1II1i
def o0O0ooOOoO ( url ) :
 I11i1ii1 = cloudflare . source ( url )
 O0o = re . compile ( 'src="(.+?)" style=.+?<a class="bigChar" href="(.+?)">(.+?)</a>.+?<p>(.+?)</p>' , re . DOTALL ) . findall ( I11i1ii1 )
 for url , Ii1IIi , I1iI1iIi111i in O0o :
  IIIIii ( '[COLORgreen]' + I1iI1iIi111i + '[/COLOR]' , 'http://kisscartoon.me' + url , 20005 , img , '' , Ii1IIi )
  if 19 - 19: i11iIiiIii
def oo0 ( url ) :
 I11i1ii1 = cloudflare . source ( url )
 O0o = re . compile ( '<img width="120" height="165" src="(.+?)" style=.+?<a class="bigChar" href="(.+?)">(.+?)</a>.+?<p>(.+?)</p>' , re . DOTALL ) . findall ( I11i1ii1 )
 for url , Ii1IIi , I1iI1iIi111i in O0o :
  IIIIii ( '[COLORgreen]' + I1iI1iIi111i + '[/COLOR]' , 'http://kisscartoon.me' + url , 20005 , img , '' , Ii1IIi )
  if 73 - 73: I1IiI . OOOo0
  if 32 - 32: I1IiI * OOOo0 % OOO0OOo * iI . O0
  if 48 - 48: i1I111ii1II1i * i1I111ii1II1i
  if 13 - 13: iI / Oooo0Ooo000 + I1IiI . OOooOOo % OOO0OOo
  if 48 - 48: OOOo0 / i11iIiiIii - OOooOOo * O0ooOooooO / OoooooooOO
def OoOo ( ) :
 if 17 - 17: iI . i11iIiiIii
 IIIIii ( '[COLORgreen]Cartoons[/COLOR]' , i1111 ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2NhcnRvb24=' ) , 10004 , ii11iIi1I + 'ORIGINCARTOON.png' , i1iiIII111ii , '' )
 IIIIii ( '[COLORgreen]Search Cartoons[/COLOR]' , '' , 10005 , ii11iIi1I + 'ORIGINCARTOON.png' , i1iiIII111ii , '' )
 if 5 - 5: ii11ii1ii + O0 + O0 . o00OO00OoO - OOO0OOo
def o00oo0000 ( ) :
 IiII111iI1ii1 = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 Ii1I = IiII111iI1ii1 . lower ( )
 I11i1ii1 = O0Oooo0O ( i1111 ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2NhcnRvb24=' ) )
 O0o = re . compile ( '<td><a href="(.+?)">(.+)</a></td>' ) . findall ( I11i1ii1 )
 for oOo0 , I1iI1iIi111i in O0o :
  if IiII111iI1ii1 in I1iI1iIi111i . lower ( ) :
   if 'Dad!' in I1iI1iIi111i :
    pass
   elif 'Family Guy' in I1iI1iIi111i :
    pass
   elif '2 Stupid' in I1iI1iIi111i :
    pass
   elif 'The Zelfs' in I1iI1iIi111i :
    pass
   elif 'A Clone' in I1iI1iIi111i :
    pass
   elif 'A.T.O.M' in I1iI1iIi111i :
    pass
   elif 'Almost Naked' in I1iI1iIi111i :
    pass
   elif 'Angry Kid' in I1iI1iIi111i :
    pass
   elif 'Annoying Orange' in I1iI1iIi111i :
    pass
   elif 'Aqua Teen' in I1iI1iIi111i :
    pass
   elif 'Assy Mcgee' in I1iI1iIi111i :
    pass
   elif 'Astroblast' in I1iI1iIi111i :
    pass
   elif 'Atomic Betty' in I1iI1iIi111i :
    pass
   elif 'Axe Cop' in I1iI1iIi111i :
    pass
   elif 'Baby Playpen' in I1iI1iIi111i :
    pass
   elif 'Beavis and Butt' in I1iI1iIi111i :
    pass
   elif 'Celebrity Deathmatch' in I1iI1iIi111i :
    pass
   elif 'Clerks The' in I1iI1iIi111i :
    pass
   elif 'Crapston Villas' in I1iI1iIi111i :
    pass
   elif 'Duckman:' in I1iI1iIi111i :
    pass
   elif 'Stripperella' in I1iI1iIi111i :
    pass
   elif 'Vixen' in I1iI1iIi111i :
    pass
   else :
    IIIIii ( '[COLORgreen]' + I1iI1iIi111i + '[/COLOR]' , oOo0 , 10006 , ii11iIi1I + 'ORIGINCARTOON.png' , i1iiIII111ii , '' )
  xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 44 - 44: Oo % iIii1I11I1II1
def oo0ooO0 ( url ) :
 OO0oo = O0Oooo0O ( url )
 O0o = re . compile ( '<td><a href="(.+?)">(.+)</a></td>' ) . findall ( OO0oo )
 for url , I1iI1iIi111i in O0o :
  if 'Dad!' in I1iI1iIi111i :
   pass
  elif 'Family Guy' in I1iI1iIi111i :
   pass
  elif '2 Stupid' in I1iI1iIi111i :
   pass
  elif 'The Zelfs' in I1iI1iIi111i :
   pass
  elif 'A Clone' in I1iI1iIi111i :
   pass
  elif 'A.T.O.M' in I1iI1iIi111i :
   pass
  elif 'Almost Naked' in I1iI1iIi111i :
   pass
  elif 'Angry Kid' in I1iI1iIi111i :
   pass
  elif 'Annoying Orange' in I1iI1iIi111i :
   pass
  elif 'Aqua Teen' in I1iI1iIi111i :
   pass
  elif 'Assy Mcgee' in I1iI1iIi111i :
   pass
  elif 'Astroblast' in I1iI1iIi111i :
   pass
  elif 'Atomic Betty' in I1iI1iIi111i :
   pass
  elif 'Axe Cop' in I1iI1iIi111i :
   pass
  elif 'Baby Playpen' in I1iI1iIi111i :
   pass
  elif 'Beavis and Butt' in I1iI1iIi111i :
   pass
  elif 'Celebrity Deathmatch' in I1iI1iIi111i :
   pass
  elif 'Clerks The' in I1iI1iIi111i :
   pass
  elif 'Crapston Villas' in I1iI1iIi111i :
   pass
  elif 'Duckman:' in I1iI1iIi111i :
   pass
  elif 'Stripperella' in I1iI1iIi111i :
   pass
  elif 'Vixen' in I1iI1iIi111i :
   pass
  else :
   IIIIii ( '[COLORgreen]' + I1iI1iIi111i + '[/COLOR]' , url , 10006 , ii11iIi1I + 'ORIGINCARTOON.png' , i1iiIII111ii , '' )
 xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 28 - 28: ii11ii1ii * OoooooooOO . OoOoOO00 / i11iIiiIii + O0ooOooooO
def i1oOOOOOOOoO ( url ) :
 OO0oo = O0Oooo0O ( url )
 IIIIiiIiiI = re . compile ( '<img src="(.+?)" id="series_image" width="250" height="370" alt=".+?" />' ) . findall ( OO0oo )
 for OO0ooOOO0OOO in IIIIiiIiiI :
  I1IIiI = OO0ooOOO0OOO
 O0oOOo0o = re . compile ( '<li><a href="(.+?)">Next</a></li>' ) . findall ( OO0oo )
 for url in O0oOOo0o :
  IIIIii ( '[COLORgreen]NEXT PAGE[/COLOR]' , url , 10006 , ii11iIi1I + 'Next.png' , i1iiIII111ii , '' )
 O0o = re . compile ( '&nbsp;<a href="(.+?)">(.+?)</a>' ) . findall ( OO0oo )
 for url , I1iI1iIi111i in O0o :
  II1Ii1iI1i1 ( '[COLORgreen]' + I1iI1iIi111i + '[/COLOR]' , url , 10007 , I1IIiI )
  if 50 - 50: i1I111ii1II1i . ii11ii1ii . Ooo00oOo00o * Oooo0Ooo000 + OoOoOO00 % i11iIiiIii
  if 8 - 8: OOO0OOo * O0
 xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 73 - 73: OOooOOo / O0ooOooooO / Oooo0Ooo000 / Ooo00oOo00o
def III1ii ( url , IMAGE ) :
 OO0oo = O0Oooo0O ( url )
 O0o = re . compile ( '"playlist">(.+?)</span></div><div><iframe src="(.+?)"' ) . findall ( OO0oo )
 for I1iI1iIi111i , url in O0o :
  print I1iI1iIi111i + '     ' + url
  if 'easy' in url :
   i1I ( url )
   if 36 - 36: OOOo0 * Oo
   if 77 - 77: O0ooOooooO % i1IIi - iI
  xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 93 - 93: Ooo00oOo00o * Oo
def i1I ( url ) :
 OO0oo = O0Oooo0O ( url )
 O0o = re . compile ( "url: '(.+?)'," ) . findall ( OO0oo )
 for url in O0o :
  OO0ooo0o0 ( url )
  if 69 - 69: ii11ii1ii - o00OO00OoO
  if 16 - 16: Oo
  if 14 - 14: i1IIi - O0 % Oo
def O0o00O0Oo0 ( ) :
 if 58 - 58: O0
 IIIIii ( '[COLORgreen]Stand Up[/COLOR]' , '' , 10014 , ii11iIi1I + 'ORIGINSTANDUP.png' , i1iiIII111ii , '' )
 IIIIii ( '[COLORgreen]Search Comedian[/COLOR]' , '' , 10015 , ii11iIi1I + 'ORIGINSTANDUP.png' , i1iiIII111ii , '' )
 IIIIii ( '[COLORgreen]Others[/COLOR]' , '' , 10017 , ii11iIi1I + 'ORIGINSTANDUP.png' , i1iiIII111ii , '' )
 if 78 - 78: Ooo00oOo00o % OoOo00o * i1IIi
def O0iI ( ) :
 I11i1ii1 = O0Oooo0O ( ( i1111 ( 'aHR0cDovL2JhY2syYmFzaWNzYnVpbGQuY28udWsvdGVzdC9zdGFuZHVwbGlzdC5waHA=' ) ) )
 O0o = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( I11i1ii1 )
 for oOo0 , OO0ooOOO0OOO , I1iI1iIi111i in O0o :
  if 'elete' in I1iI1iIi111i :
   pass
  else :
   II1Ii1iI1i1 ( '[COLORgreen]' + I1iI1iIi111i + '[/COLOR]' , oOo0 , 222 , OO0ooOOO0OOO )
   if 15 - 15: O0 / Oo % ii11ii1ii + OOooOOo
def iiiIiI ( ) :
 IiII111iI1ii1 = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 Ii1I = IiII111iI1ii1 . lower ( )
 I11i1ii1 = O0Oooo0O ( ( i1111 ( 'aHR0cDovL3d3dy5jb3VjaHRyaXBwZXIuY29tL2ZvcnVtMi9wYWdlLnBocD9wYWdlPTM=' ) ) )
 IiiIIIiI1ii = re . compile ( '<tr>.+?<td width=".+?" align=".+?">.+?<img border=".+?" src="..(.+?)" width=".+?" height=".+?"></td>.+?<td width=".+?" valign=".+?" align=".+?"><font size=".+?">(.+?)</font></td>.+?<td width=".+?">(.+?)</td>' , re . DOTALL ) . findall ( I11i1ii1 )
 for OO0ooOOO0OOO , oo0OOoOoo0O0O , iIiiiI1IiI1I1 in IiiIIIiI1ii :
  for IiII111iI1ii1 in oo0OOoOoo0O0O :
   print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< img >>>>>>>>>>>>>>>>>>>>>>>>>>'
   iiI11ii1111 = re . compile ( '<a href="(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( iIiiiI1IiI1I1 )
   for oOo0 , I1iI1iIi111i in iiI11ii1111 :
    if 'tube' in oOo0 :
     pass
    elif 'stage' in oOo0 :
     II1Ii1iI1i1 ( '[COLORgreen]' + oo0OOoOoo0O0O + '   -   ' + I1iI1iIi111i + '[/COLOR]' , ( oOo0 ) . replace ( '" target="_blank' , '' ) , 10016 , 'http://couchtripper.com/' + OO0ooOOO0OOO , )
    elif 'vee' in oOo0 :
     pass
     if 2 - 2: I1IiI . i1IIi . i1IIi - OoOoOO00 - I1IiI
def ooOOooo0Oo ( ) :
 I11i1ii1 = O0Oooo0O ( ( i1111 ( 'aHR0cDovL3d3dy5jb3VjaHRyaXBwZXIuY29tL2ZvcnVtMi9wYWdlLnBocD9wYWdlPTM=' ) ) )
 IiiIIIiI1ii = re . compile ( '<tr>.+?<td width=".+?" align=".+?">.+?<img border=".+?" src="..(.+?)" width=".+?" height=".+?"></td>.+?<td width=".+?" valign=".+?" align=".+?"><font size=".+?">(.+?)</font></td>.+?<td width=".+?">(.+?)</td>' , re . DOTALL ) . findall ( I11i1ii1 )
 for OO0ooOOO0OOO , oo0OOoOoo0O0O , iIiiiI1IiI1I1 in IiiIIIiI1ii :
  iiI11ii1111 = re . compile ( '<a href="(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( iIiiiI1IiI1I1 )
  for oOo0 , I1iI1iIi111i in iiI11ii1111 :
   if 'tube' in oOo0 :
    pass
   elif 'stage' in oOo0 :
    II1Ii1iI1i1 ( '[COLORgreen]' + oo0OOoOoo0O0O + '   -   ' + I1iI1iIi111i + '[/COLOR]' , ( oOo0 ) . replace ( '" target="_blank' , '' ) , 10016 , 'http://couchtripper.com/' + OO0ooOOO0OOO )
   elif 'vee' in oOo0 :
    pass
    if 66 - 66: Oo
    if 28 - 28: OoOo00o - OoOo00o . i1IIi - OOO0OOo + OOOo0 . OoOo00o
 xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 54 - 54: I1IiI - o00OO00OoO
def iIIiIIIi ( url ) :
 I11i1ii1 = O0Oooo0O ( url )
 print '>>>>>>>>>>>>>>>>>>>>>>>>' + url + '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'
 IIIIiI11I11 = re . compile ( "url\[.+?\] = '(.+?)';" ) . findall ( I11i1ii1 )
 print '>>>>>>>>>>>>>>>>>>>>>>>' + ( str ( IIIIiI11I11 ) ) + '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
 for url in IIIIiI11I11 :
  OO0ooo0o0 ( ( url ) . replace ( '[' , '' ) . replace ( ']' , '' ) . replace ( '\'' , '' ) )
  if 98 - 98: O0ooOooooO % OoOo00o * i11iIiiIii % ii11ii1ii
  if 29 - 29: OoOo00o
  if 66 - 66: Oo
  if 97 - 97: i1IIi - OoooooooOO / o00OO00OoO * OOOo0
  if 55 - 55: OOooOOo . i1I111ii1II1i
  if 87 - 87: OOooOOo % iIii1I11I1II1
  if 100 - 100: o00OO00OoO . OOOo0 * o00OO00OoO - OOOo0 . Oooo0Ooo000 * iI
def oO000o ( ) :
 if 78 - 78: OoooooooOO
 OOoo0 ( '[COLOR darkgoldenrod]Open Pandora\'s Box[/COLOR]' , '' , 10029 , 'https://encrypted-tbn1.gstatic.com/images?q=tbn%3AANd9GcTQ9r4TA8yIw9ggxuwsHxWojo6tPVfgTe8QIOxOQwzNR2TavtCi6Q' , i1iiIII111ii , '' )
 OOoo0 ( '[COLOR darkgoldenrod]Search[/COLOR]' , '' , 10026 , 'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png' , i1iiIII111ii , '' )
 if 36 - 36: OOooOOo + Oooo0Ooo000 - OoOo00o + iIii1I11I1II1 + OoooooooOO
 O00Oo000ooO0 ( 'movies' , 'MAIN' )
 if 4 - 4: OoOoOO00 . Oooo0Ooo000 + iI * o00OO00OoO . OOO0OOo
def oOoOo ( ) :
 OOoo0 ( 'Search Pandoras Films' , '' , 10027 , 'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png' , i1iiIII111ii , '' )
 OOoo0 ( 'Search Pandoras TV' , '' , 10028 , 'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png' , i1iiIII111ii , '' )
 if 74 - 74: O0ooOooooO / ii11ii1ii % OOooOOo
 O00Oo000ooO0 ( 'movies' , 'MAIN' )
def OO0o0OO0 ( ) :
 if 56 - 56: i11iIiiIii - Oo / i1I111ii1II1i / I1IiI
 IiII111iI1ii1 = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 Ii1I = IiII111iI1ii1 . lower ( )
 III1i111i = [ 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' ]
 if 42 - 42: ii11ii1ii / i1IIi % I1IiI
 for I11iiIIII1I1 in III1i111i :
  i1IIi1i1Ii1 = IIIII + I11iiIIII1I1 + OooO0
  I11i1ii1 = O0Oooo0O ( i1IIi1i1Ii1 )
  O0o = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( I11i1ii1 )
  for oOo0 , OOO0000oO , OOoOO0ooo , iI1i111I1Ii , I1iI1iIi111i in O0o :
   if IiII111iI1ii1 in I1iI1iIi111i . lower ( ) :
    Iiio0Oo0oO ( I1iI1iIi111i , oOo0 , 222 , OOO0000oO , iI1i111I1Ii , OOoOO0ooo )
    if 48 - 48: O0ooOooooO . OOooOOo / O0ooOooooO
    O00Oo000ooO0 ( 'movies' , 'MAIN' )
    xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
    if 56 - 56: iIii1I11I1II1 . i11iIiiIii - i1I111II1I * OoOoOO00 * o00OO00OoO
    if 5 - 5: i1I111II1I / i1I111II1I - ii11ii1ii
def oO0ooOO ( ) :
 if 7 - 7: OoOoOO00 - i1I111II1I . OoOoOO00
 IiII111iI1ii1 = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 Ii1I = IiII111iI1ii1 . lower ( )
 III1i111i = [ 'a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' , 'p' , 'q' , 'r' , 's' , 't' , 'u' , 'v' , 'w' , 'x' , 'y' , 'z' ]
 if 53 - 53: O0ooOooooO % Oooo0Ooo000 . OOO0OOo - I1IiI
 for I11iiIIII1I1 in III1i111i :
  OoOoO0OoOOOOo = IIIII + I11iiIIII1I1 + OooO0
  I11i1ii1 = O0Oooo0O ( OoOoO0OoOOOOo )
  O0o = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( I11i1ii1 )
  for I1iI1iIi111i , OOoOO0ooo , oOo0 , OO0ooOOO0OOO , iI1i111I1Ii , OooOo000OOOOo in O0o :
   if IiII111iI1ii1 in I1iI1iIi111i . lower ( ) :
    OOoo0 ( I1iI1iIi111i , oOo0 , OooOo000OOOOo , OO0ooOOO0OOO , iI1i111I1Ii , OOoOO0ooo )
    if 21 - 21: OOOo0 % OOooOOo
    O00Oo000ooO0 ( 'movies' , 'MAIN' )
    xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
    if 33 - 33: i1I111II1I
    if 35 - 35: i11iIiiIii - OOOo0 / i1I111II1I + iI * O0ooOooooO
def III1I11i1iIi ( ) :
 if 69 - 69: Oo * OoOoOO00 * OOO0OOo . i1I111ii1II1i - ii11ii1ii
 OO0oo = O0Oooo0O ( IIIII + 'spongemain.php' )
 O0o = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( OO0oo )
 for I1iI1iIi111i , OOoOO0ooo , oOo0 , OO0ooOOO0OOO , iI1i111I1Ii , OooOo000OOOOo in O0o :
  OOoo0 ( I1iI1iIi111i , oOo0 , OooOo000OOOOo , OO0ooOOO0OOO , iI1i111I1Ii , OOoOO0ooo )
  O00Oo000ooO0 ( 'movies' , 'MAIN' )
def I11iiIIiI1ii ( url ) :
 if 12 - 12: o00OO00OoO % i11iIiiIii + OOooOOo + o00OO00OoO / Oooo0Ooo000
 xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
 O00 = ( '%s%s' % ( O0OO0 , url ) )
 oOo00O000Oo0 = O0Oooo0O ( url )
 O0o = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( oOo00O000Oo0 )
 for url , OOO0000oO , OOoOO0ooo , OOo , I1iI1iIi111i in O0o :
  Iiio0Oo0oO ( I1iI1iIi111i , url , 222 , OOO0000oO , OOo , OOoOO0ooo )
  if 53 - 53: ii11ii1ii / OoOo00o / OoooooooOO / OoOoOO00
  O00Oo000ooO0 ( 'movies' , 'MAIN' )
  if 32 - 32: iIii1I11I1II1 . i11iIiiIii / O0ooOooooO
  xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 52 - 52: OOOo0 + iIii1I11I1II1
  if 71 - 71: O0 / O0ooOooooO
def iI1 ( url ) :
 if 11 - 11: Ooo00oOo00o
 OO0oo = O0Oooo0O ( url )
 O0o = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( OO0oo )
 for I1iI1iIi111i , OOoOO0ooo , url , OO0ooOOO0OOO , iI1i111I1Ii , OooOo000OOOOo in O0o :
  OOoo0 ( I1iI1iIi111i , url , OooOo000OOOOo , OO0ooOOO0OOO , iI1i111I1Ii , OOoOO0ooo )
  if 18 - 18: i1I111ii1II1i - O0ooOooooO % i1I111ii1II1i / Oooo0Ooo000
  O00Oo000ooO0 ( 'movies' , 'MAIN' )
  if 68 - 68: iI * iIii1I11I1II1 + o00OO00OoO % I1IiI
  if 46 - 46: I1IiI % i1IIi / O0ooOooooO * Oo * i1I111II1I
 xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 67 - 67: I1IiI * I1IiI . I1IiI + iI / O0ooOooooO
def Iiio0Oo0oO ( name , url , mode , iconimage , fanart , description ) :
 if 13 - 13: i1I111ii1II1i
 o0OOOOO0O = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 I1I1IiIi1 = True
 oOO0o0oo0 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 oOO0o0oo0 . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 oOO0o0oo0 . setProperty ( "Fanart_Image" , fanart )
 I1I1IiIi1 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = o0OOOOO0O , listitem = oOO0o0oo0 , isFolder = False )
 return I1I1IiIi1
 if 78 - 78: i1I111II1I + i1I111ii1II1i . OoOo00o
def OOoo0 ( name , url , mode , iconimage , fanart , description ) :
 if 91 - 91: iIii1I11I1II1 . OOooOOo . ii11ii1ii + OoooooooOO
 o0OOOOO0O = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 I1I1IiIi1 = True
 oOO0o0oo0 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 oOO0o0oo0 . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 oOO0o0oo0 . setProperty ( "Fanart_Image" , fanart )
 I1I1IiIi1 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = o0OOOOO0O , listitem = oOO0o0oo0 , isFolder = True )
 return I1I1IiIi1
if 69 - 69: o00OO00OoO - OOOo0
if 95 - 95: OOOo0 * i11iIiiIii . OOO0OOo
if 41 - 41: OoOoOO00
if 37 - 37: Oooo0Ooo000 . Oo % OoOo00o * i1IIi
if 71 - 71: Oo / OOooOOo + i1I111II1I
if 48 - 48: o00OO00OoO + i1I111ii1II1i
if 16 - 16: iIii1I11I1II1 % i11iIiiIii . I1IiI % OOO0OOo + O0ooOooooO . Ooo00oOo00o
if 46 - 46: Ooo00oOo00o - OOooOOo / I1IiI - OoooooooOO + O0ooOooooO
if 58 - 58: OOooOOo / OOooOOo + OOO0OOo + Oooo0Ooo000 - I1IiI . i1I111II1I
if 15 - 15: OOO0OOo * I1IiI % OoOo00o . I1IiI . Oooo0Ooo000
if 97 - 97: O0ooOooooO
if 80 - 80: OOOo0 . iI
if 47 - 47: Oooo0Ooo000 + OOO0OOo + OoOoOO00 % i11iIiiIii
if 93 - 93: ii11ii1ii % I1IiI . O0 / i1I111ii1II1i * O0ooOooooO
if 29 - 29: OOooOOo
def oo0iIiI ( string ) :
 if OOOO == 'true' :
  xbmc . log ( "[addon.live.GenieTV-%s]: %s" % ( addon_version , string ) )
  if 81 - 81: I1IiI % iI
def oo0i1iIIi1II1iiI ( name , url , iconimage , fanart , mode , playlist = None , regexs = None ) :
 III1Ii1i1I1 = [ ]
 try :
  if 97 - 97: o00OO00OoO . OOO0OOo - o00OO00OoO + OOOo0 * OoOoOO00
  name = name . encode ( 'utf-8' , 'ignore' )
 except :
  pass
 if os . path . exists ( I11i1 ) == False :
  oo0iIiI ( 'Making Favorites File' )
  III1Ii1i1I1 . append ( ( name , url , iconimage , fanart , mode , playlist , regexs ) )
  iII1ii1 = open ( I11i1 , "w" )
  iII1ii1 . write ( json . dumps ( III1Ii1i1I1 ) )
  iII1ii1 . close ( )
 else :
  oo0iIiI ( 'Appending Favorites' )
  iII1ii1 = open ( I11i1 ) . read ( )
  I111Ii = json . loads ( iII1ii1 )
  I111Ii . append ( ( name , url , iconimage , fanart , mode ) )
  IIiiii = open ( I11i1 , "w" )
  IIiiii . write ( json . dumps ( I111Ii ) )
  IIiiii . close ( )
  if 34 - 34: OOooOOo / i1I111ii1II1i % O0 . Ooo00oOo00o . i1IIi
  if 29 - 29: O0 . o00OO00OoO
def OO0o0oO0O000o ( ) :
 I1iI11iii = json . loads ( open ( I11i1 ) . read ( ) )
 oo0oO = len ( I1iI11iii )
 for IiIi1iI11 in I1iI11iii :
  I1iI1iIi111i = IiIi1iI11 [ 0 ]
  oOo0 = IiIi1iI11 [ 1 ]
  OOO0000oO = IiIi1iI11 [ 2 ]
  try :
   iiI1iI1I = IiIi1iI11 [ 3 ]
   if iiI1iI1I == None :
    raise
  except :
   if o0oO0 . getSetting ( 'use_thumb' ) == "true" :
    iiI1iI1I = OOO0000oO
   else :
    iiI1iI1I = iI1i111I1Ii
  try : III1II111Ii1 = IiIi1iI11 [ 5 ]
  except : III1II111Ii1 = None
  try : o0O0OO0o = IiIi1iI11 [ 6 ]
  except : o0O0OO0o = None
  if 54 - 54: I1IiI . O0ooOooooO % i11iIiiIii / OoooooooOO + OoOo00o % O0ooOooooO
  if IiIi1iI11 [ 4 ] == 0 :
   IIIIii ( I1iI1iIi111i , oOo0 , '' , OOO0000oO , iI1i111I1Ii , '' , 'fav' )
  else :
   IIIIii ( I1iI1iIi111i , oOo0 , IiIi1iI11 [ 4 ] , OOO0000oO , iI1i111I1Ii , '' , 'fav' )
   if 36 - 36: O0ooOooooO
def o0OOII1I1 ( name ) :
 I111Ii = json . loads ( open ( I11i1 ) . read ( ) )
 for iii11I11iI1 in range ( len ( I111Ii ) ) :
  if I111Ii [ iii11I11iI1 ] [ 0 ] == name :
   del I111Ii [ iii11I11iI1 ]
   IIiiii = open ( I11i1 , "w" )
   IIiiii . write ( json . dumps ( I111Ii ) )
   IIiiii . close ( )
   break
 xbmc . executebuiltin ( "XBMC.Container.Refresh" )
 if 4 - 4: i1I111II1I
 if 48 - 48: Oooo0Ooo000 . OoooooooOO . OOOo0 . I1IiI % ii11ii1ii / i1I111ii1II1i
def ooo00Ooo ( ) :
 ii1I111i1Ii = os . path . join ( iIii1 , 'addons.ini' )
 OOOooO0OO0o = open ( ii1I111i1Ii , "w+" )
 if 10 - 10: iI - I1IiI . OoooooooOO . i1I111II1I . Ooo00oOo00o * i1I111ii1II1i
 OOOooO0OO0o . write ( r'# This file contains the "built-in" channels' + '\n' )
 OOOooO0OO0o . write ( r'# It is parsed by Pythons ConfigParser' + '\n\n' )
 OOOooO0OO0o . write ( r'[plugin.video.GenieTv]' + '\n' )
 OOOooO0OO0o . write ( r'BBC One=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F394.m3u8&mode=10012&name=[COLORgreen]BBC+One+UK%0D[/COLOR]' + '\n' )
 OOOooO0OO0o . write ( r'BBC Two=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F190.m3u8&mode=10012&name=[COLORgreen]BBC+Two+UK%0D[/COLOR]' + '\n' )
 OOOooO0OO0o . write ( r'BBC Four=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F188.m3u8&mode=10012&name=[COLORgreen]BBC+Four+UK%0D[/COLOR]' + '\n' )
 OOOooO0OO0o . write ( r'BBC Ent MX=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F435.m3u8&mode=10012&name=[COLORgreen]BBC+Entertainment+MX%0D[/COLOR]' + '\n' )
 OOOooO0OO0o . write ( r'ITV=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F208.m3u8&mode=10012&name=[COLORgreen]ITV1+UK%0D[/COLOR]' + '\n' )
 OOOooO0OO0o . write ( r'ITV2=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F207.m3u8&mode=10012&name=[COLORgreen]ITV2+UK%0D[/COLOR]' + '\n' )
 OOOooO0OO0o . write ( r'ITV3=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F206.m3u8&mode=10012&name=[COLORgreen]ITV3+UK%0D[/COLOR]' + '\n' )
 OOOooO0OO0o . write ( r'ITV4=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F205.m3u8&mode=10012&name=[COLORgreen]ITV4+UK%0D[/COLOR]' + '\n' )
 OOOooO0OO0o . write ( r'Channel 4=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F183.m3u8&mode=10012&name=[COLORgreen]Channel+4+UK%0D[/COLOR]' + '\n' )
 OOOooO0OO0o . write ( r'Channel 5=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F185.m3u8&mode=10012&name=[COLORgreen]Channel+5+UK%0D[/COLOR]' + '\n' )
 OOOooO0OO0o . write ( r'Sky1=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F32.m3u8&mode=10012&name=[COLORgreen]Sky+1+UK%0D[/COLOR]' + '\n' )
 OOOooO0OO0o . write ( r'Sky2=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F33.m3u8&mode=10012&name=[COLORgreen]Sky+2+UK%0D[/COLOR]' + '\n' )
 OOOooO0OO0o . write ( r'Sky Atlantic=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F34.m3u8&mode=10012&name=[COLORgreen]Sky+Atlantic+UK%0D[/COLOR]' + '\n' )
 OOOooO0OO0o . write ( r'Sky Living=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F35.m3u8&mode=10012&name=[COLORgreen]Sky+Living+UK%0D[/COLOR]' + '\n' )
 OOOooO0OO0o . write ( r'5STAR=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F187.m3u8&mode=10012&name=[COLORgreen]5%2A+UK%0D[/COLOR]' + '\n' )
 OOOooO0OO0o . write ( r'5 USA=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F186.m3u8&mode=10012&name=[COLORgreen]5USA+UK%0D[/COLOR]' + '\n' )
 OOOooO0OO0o . write ( r'Watch HD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F408.m3u8&mode=10012&name=[COLORgreen]Watch+UK%0D[/COLOR]' + '\n' )
 OOOooO0OO0o . write ( r'Pick=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F410.m3u8&mode=10012&name=[COLORgreen]Pick+UK%0D[/COLOR]' + '\n' )
 OOOooO0OO0o . write ( r'GOLD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F430.m3u8&mode=10012&name=[COLORgreen]Gold+UK%0D[/COLOR]' + '\n' )
 OOOooO0OO0o . write ( r'YESTERDAY=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F411.m3u8&mode=10012&name=[COLORgreen]Yesterday+UK%0D[/COLOR]' + '\n' )
 OOOooO0OO0o . write ( r'TG4=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F192.m3u8&mode=10012&name=[COLORgreen]TG4%0D[/COLOR]' + '\n' )
 OOOooO0OO0o . write ( r'RTE One=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F194.m3u8&mode=10012&name=[COLORgreen]RTE+One+UK%0D[/COLOR]' + '\n' )
 OOOooO0OO0o . write ( r'RTE Two=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F193.m3u8&mode=10012&name=[COLORgreen]RTE+Two+UK%0D[/COLOR]' + '\n' )
 OOOooO0OO0o . write ( r'Disney Chnl=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F398.m3u8&mode=10012&name=[COLORgreen]Disney+Channel+UK%0D[/COLOR]' + '\n' )
 OOOooO0OO0o . write ( r'Disney Junior=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F397.m3u8&mode=10012&name=[COLORgreen]Disney+Junior+UK%0D[/COLOR]' + '\n' )
 OOOooO0OO0o . write ( r'Discovery=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F395.m3u8&mode=10012&name=[COLORgreen]Discovery+UK%0D[/COLOR]' + '\n' )
 OOOooO0OO0o . write ( r'Discovery Science=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F396.m3u8&mode=10012&name=[COLORgreen]Discovery+Science+UK%0D[/COLOR]' + '\n' )
 OOOooO0OO0o . write ( r'Animal Planet=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F428.m3u8&mode=10012&name=[COLORgreen]Animal+Planet+UK%0D[/COLOR]' + '\n' )
 OOOooO0OO0o . write ( r'Disc.Turbo=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F431.m3u8&mode=10012&name=[COLORgreen]Discovery+Turbo+UK%0D[/COLOR]' + '\n' )
 OOOooO0OO0o . write ( r'Nat Geo=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F429.m3u8&mode=10012&name=[COLORgreen]National+Geographic+Channel+UK%0D[/COLOR]' + '\n' )
 OOOooO0OO0o . write ( r'MTV MUSIC=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F409.m3u8&mode=10012&name=[COLORgreen]MTV+Music+UK%0D[/COLOR]' + '\n' )
 OOOooO0OO0o . write ( r'MTV Canada=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F417.m3u8&mode=10012&name=[COLORgreen]MTV+2+Ca%0D[/COLOR]' + '\n' )
 OOOooO0OO0o . write ( r'SkyPremiereHD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F37.m3u8&mode=10012&name=[COLORgreen]Sky+Movies+Premiere+UK%0D[/COLOR]' + '\n' )
 OOOooO0OO0o . write ( r'Sky Action=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F39.m3u8&mode=10012&name=[COLORgreen]Sky+Movies+Action+%26+Adventure+UK%0D[/COLOR]' + '\n' )
 OOOooO0OO0o . write ( r'Sky Thriller=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F40.m3u8&mode=10012&name=[COLORgreen]Sky+Movies+Crime+%26+Thriller+UK%0D[/COLOR]' + '\n' )
 OOOooO0OO0o . write ( r'Sky Comedy=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F43.m3u8&mode=10012&name=[COLORgreen]Sky+Movies+Comedy+UK%0D[/COLOR]' + '\n' )
 OOOooO0OO0o . write ( r'Sky Greats=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F41.m3u8&mode=10012&name=[COLORgreen]Sky+Movies+Greats+UK%0D[/COLOR]' + '\n' )
 OOOooO0OO0o . write ( r'Sky ScFiHorror=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F44.m3u8&mode=10012&name=[COLORgreen]Sky+Movies+Sci-Fi+%26+Horror+UK%0D[/COLOR]' + '\n' )
 OOOooO0OO0o . write ( r'Sky Showcase=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F46.m3u8&mode=10012&name=[COLORgreen]Sky+Movies+Showcase+UK%0D[/COLOR]' + '\n' )
 OOOooO0OO0o . write ( r'Sky Select=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F45.m3u8&mode=10012&name=[COLORgreen]Sky+Movies+Select+UK%0D[/COLOR]' + '\n' )
 OOOooO0OO0o . write ( r'Sky DramaRom=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F47.m3u8&mode=10012&name=[COLORgreen]Sky+Movies+Drama+%26+Romance+UK%0D[/COLOR]' + '\n' )
 OOOooO0OO0o . write ( r'Sky Family=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F48.m3u8&mode=10012&name=[COLORgreen]Sky+Movies+Family+UK%0D[/COLOR]' + '\n' )
 OOOooO0OO0o . write ( r'Sky Disney=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F195.m3u8&mode=10012&name=[COLORgreen]Sky+Movies+Disney+UK%0D[/COLOR]' + '\n' )
 OOOooO0OO0o . write ( r'Fox Movies HD MX=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F436.m3u8&mode=10012&name=[COLORgreen]Fox+Movies+HD+MX%0D[/COLOR]' + '\n' )
 OOOooO0OO0o . write ( r'Film Zone MX HD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F437.m3u8&mode=10012&name=[COLORgreen]Film+Zone+MX+HD%0D[/COLOR]' + '\n' )
 OOOooO0OO0o . write ( r'Eurosport=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F269.m3u8&mode=10012&name=[COLORgreen]Eurosport+1+UK%0D[/COLOR]' + '\n' )
 OOOooO0OO0o . write ( r'Sky Sports 1=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F403.m3u8&mode=10012&name=[COLORgreen]Sky+Sports+1+UK%0D[/COLOR]' + '\n' )
 OOOooO0OO0o . write ( r'Sky Sports 2=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F404.m3u8&mode=10012&name=[COLORgreen]Sky+Sports+2+UK%0D[/COLOR]' + '\n' )
 OOOooO0OO0o . write ( r'Sky Sports 3=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F405.m3u8&mode=10012&name=[COLORgreen]Sky+Sports+3+UK%0D[/COLOR]' + '\n' )
 OOOooO0OO0o . write ( r'Sky Sports 4=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F406.m3u8&mode=10012&name=[COLORgreen]Sky+Sports+4+UK%0D[/COLOR]' + '\n' )
 OOOooO0OO0o . write ( r'Sky Sports 5=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F407.m3u8&mode=10012&name=[COLORgreen]Sky+Sports+5+UK%0D[/COLOR]' + '\n' )
 OOOooO0OO0o . write ( r'Sky Sports F1=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F412.m3u8&mode=10012&name=[COLORgreen]Sky+Sports+F1%0D[/COLOR]' + '\n' )
 OOOooO0OO0o . write ( r'BT Sport 1=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F423.m3u8&mode=10012&name=[COLORgreen]BT+Sports+1%0D[/COLOR]' + '\n' )
 OOOooO0OO0o . write ( r'BT Sport 2=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F413.m3u8&mode=10012&name=[COLORgreen]BT+Sports+2%0D[/COLOR]' + '\n' )
 OOOooO0OO0o . write ( r'Fox Sports 1 HD MX=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F439.m3u8&mode=10012&name=[COLORgreen]Fox+Sports+1+HD+MX%0D[/COLOR]' + '\n' )
 OOOooO0OO0o . write ( r'ESPN 1 HD ES=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F440.m3u8&mode=10012&name=[COLORgreen]ESPN+1+HD+ES%0D[/COLOR]' + '\n' )
 OOOooO0OO0o . write ( r'ESPN 2 HD ES=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F441.m3u8&mode=10012&name=[COLORgreen]ESPN+2+HD+ES%0D[/COLOR]' + '\n' )
 OOOooO0OO0o . write ( r'At The Races=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F427.m3u8&mode=10012&name=[COLORgreen]At+The+Races+UK%0D[/COLOR]' + '\n' )
 OOOooO0OO0o . write ( r'Racing UK=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F426.m3u8&mode=10012&name=[COLORgreen]Racing+UK%0D[/COLOR]' + '\n' )
 if 78 - 78: O0ooOooooO / Ooo00oOo00o - O0ooOooooO * OoooooooOO . I1IiI
 if 96 - 96: OOOo0 % i1IIi . OOooOOo . O0
 if 37 - 37: i1IIi - i1I111II1I % OoooooooOO / i1I111II1I % OOO0OOo
def iiIiII11i1 ( ) :
 if 93 - 93: I1IiI % iIii1I11I1II1
 IIIIii ( '[COLORgreen]Recent Episodes[/COLOR]' , '' , 10019 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 IIIIii ( '[COLORgreen]Genres[/COLOR]' , '' , 10020 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 IIIIii ( '[COLORgreen]Search[/COLOR]' , '' , 10021 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 if 90 - 90: OOOo0 - i1I111II1I / iI / O0 / Oooo0Ooo000
def oOO0 ( ) :
 if 15 - 15: Oo + Oooo0Ooo000 . OOO0OOo - iIii1I11I1II1 / O0 % iIii1I11I1II1
 OO0oo = cloudflare . source ( i1111 ( 'aHR0cDovL2RpemlsYWIuY29t' ) )
 O0o = re . compile ( '<li id=".+?">.+?<a href="(.+?)">.+?<img width="40" height="40" src="(.+?)" alt=""/>.+?<span class="title">\n(.+?)</span>.+?<span class="alt-title">\n(.+?)</span>.+?</a>.+?</li>' , re . DOTALL ) . findall ( OO0oo )
 for oOo0 , OO0ooOOO0OOO , I1iI1iIi111i , iiIi1IIi1I in O0o :
  IIIIii ( I1iI1iIi111i + '  -  ' + ( iiIi1IIi1I ) . replace ( 'sezon' , 'Season' ) . replace ( 'bölüm' , 'Episode' ) , oOo0 , 10023 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
  if 86 - 86: OOOo0 / O0ooOooooO * iI
  if 64 - 64: OOO0OOo / O0 * I1IiI * OOO0OOo
  if 60 - 60: Oooo0Ooo000 / i1IIi % ii11ii1ii / ii11ii1ii * ii11ii1ii . i11iIiiIii
def o0oOO00 ( ) :
 if 46 - 46: i11iIiiIii - Oooo0Ooo000
 IIIIii ( '[COLORgreen]Action[/COLOR]' , 'Aksiyon' , 10024 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 IIIIii ( '[COLORgreen]Adventure[/COLOR]' , 'Macera' , 10024 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 IIIIii ( '[COLORgreen]Animation[/COLOR]' , 'Animasyon' , 10024 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 IIIIii ( '[COLORgreen]Anime[/COLOR]' , 'Anime' , 10024 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 IIIIii ( '[COLORgreen]Biography[/COLOR]' , 'Biyografi' , 10024 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 IIIIii ( '[COLORgreen]Comedy[/COLOR]' , 'Komedi' , 10024 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 IIIIii ( '[COLORgreen]Crime[/COLOR]' , 'Su%C3%A7' , 10024 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 IIIIii ( '[COLORgreen]Documentary[/COLOR]' , 'Belgesel' , 10024 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 IIIIii ( '[COLORgreen]Drama[/COLOR]' , 'Dram' , 10024 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 IIIIii ( '[COLORgreen]Family[/COLOR]' , 'Aile' , 10024 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 IIIIii ( '[COLORgreen]Fantasy[/COLOR]' , 'Fantastik' , 10024 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 IIIIii ( '[COLORgreen]History[/COLOR]' , 'Tarih' , 10024 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 IIIIii ( '[COLORgreen]Horror[/COLOR]' , 'Korku' , 10024 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 IIIIii ( '[COLORgreen]Mini-Series[/COLOR]' , 'Mini%20Dizi' , 10024 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 IIIIii ( '[COLORgreen]Musical[/COLOR]' , 'M%C3%BCzikal' , 10024 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 IIIIii ( '[COLORgreen]Mystery[/COLOR]' , 'Gizem' , 10024 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 IIIIii ( '[COLORgreen]Romance[/COLOR]' , 'Romantik' , 10024 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 IIIIii ( '[COLORgreen]Science Fiction[/COLOR]' , 'Bilim%20Kurgu' , 10024 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 IIIIii ( '[COLORgreen]Sport[/COLOR]' , 'Spor' , 10024 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 IIIIii ( '[COLORgreen]Thriller[/COLOR]' , 'Gerilim' , 10024 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 IIIIii ( '[COLORgreen]War[/COLOR]' , 'Sava%C5%9F' , 10024 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 IIIIii ( '[COLORgreen]Western[/COLOR]' , 'Tarih' , 10024 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 IIIIii ( '[COLORgreen]Youth[/COLOR]' , 'Gen%C3%A7lik' , 10024 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 if 95 - 95: OoOoOO00
def oo000oO ( url ) :
 oOo0O = 'http://dizilab.com/arsiv?limit=100&tur=' + url + '&orderby=&ulke=&order=&yil=&dizi_adi='
 I11i1ii1 = cloudflare . source ( oOo0O )
 O0o = re . compile ( '<div class="tv-series-single">.+?<a href="(.+?)" class="film-image">.+?<img src="(.+?)" alt=""/>.+?<span class="position">.+?</span>\n(.+?)</a>' , re . DOTALL ) . findall ( I11i1ii1 )
 for url , OO0ooOOO0OOO , I1iI1iIi111i in O0o :
  IIIIii ( '[COLORgreen]' + I1iI1iIi111i + '[/COLOR]' , url , 10022 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
  if 78 - 78: iI + I1IiI + OoOo00o - OoOo00o . i11iIiiIii / Ooo00oOo00o
  if 27 - 27: iI - O0 % Oooo0Ooo000 * o00OO00OoO . OoOo00o % iIii1I11I1II1
  if 37 - 37: OoooooooOO + O0 - i1IIi % OOO0OOo
  if 24 - 24: I1IiI
def Oo0oOo0ooOOOo ( ) :
 if 71 - 71: OoOoOO00 - iI - i1I111ii1II1i * O0 * OoOo00o
 IiII111iI1ii1 = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 Ii1I = IiII111iI1ii1 . lower ( )
 oOo0 = ( i1111 ( 'aHR0cDovL2RpemlsYWIuY29tL2Fyc2l2P2xpbWl0PSZ0dXI9Jm9yZGVyYnk9JnVsa2U9Jm9yZGVyPSZ5aWw9JmRpemlfYWRpPQ==' ) ) + ( IiII111iI1ii1 ) . replace ( ' ' , '+' )
 I11i1ii1 = cloudflare . source ( oOo0 )
 O0o = re . compile ( '<a href="(.+?)" class="film-image">\n<img src="(.+?)" alt=""/>\n</a>\n<div class="tss-detail">\n<a class="title" style="" href=".+?">\n<span class="position">.+?</span>\n(.+?)</a>' ) . findall ( I11i1ii1 )
 for oOo0 , OO0ooOOO0OOO , I1iI1iIi111i in O0o :
  if IiII111iI1ii1 in I1iI1iIi111i . lower ( ) :
   IIIIii ( '[COLORgreen]' + I1iI1iIi111i + '[/COLOR]' , oOo0 , 10022 , ii11iIi1I + 'dtv.png' )
   if 46 - 46: OoOo00o
   if 29 - 29: OoOoOO00 . I1IiI % OOooOOo * OoOoOO00 - OOooOOo * iIii1I11I1II1
   if 35 - 35: OoOoOO00 - OoOo00o . i1IIi
def OOOoO0 ( url ) :
 I11i1ii1 = cloudflare . source ( url )
 O0o = re . compile ( '<a class="season" href="(.+?)">\n(.+?)\n</a>.+?<a class="episode" href=".+?">\n(.+?)\n</a>.+?<a class="episode-name" href=".+?">\n(.+?)</a>' , re . DOTALL ) . findall ( I11i1ii1 )
 for IIo0o0O0O00oOOo , oo0oo , IiIIi11i111 , I1iI1iIi111i in O0o :
  oooo = ( IiIIi11i111 ) . replace ( 'Sezon' , '' ) . replace ( 'bölüm' , '' ) . replace ( 'Bölüm' , '' ) . replace ( 'BÃ¶lÃ¼m' , '' ) . replace ( '.' , '' )
  iiiIIIii = ( oo0oo ) . replace ( 'bölüm' , '' ) . replace ( 'Sezon' , '' ) . replace ( 'Bölüm' , '' ) . replace ( 'BÃ¶lÃ¼m' , '' ) . replace ( '.' , '' )
  ooOoo00 = 'Season ' + iiiIIIii + 'Episode ' + oooo + I1iI1iIi111i
  Ii11IiI ( ooOoo00 , IIo0o0O0O00oOOo )
  if 91 - 91: Oooo0Ooo000 % iIii1I11I1II1 * ii11ii1ii
  xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 31 - 31: Ooo00oOo00o * O0 . O0ooOooooO
  if 59 - 59: OoOoOO00 * i11iIiiIii
def Ii11IiI ( name , url ) :
 IIo0o0O0O00oOOo = url
 ooOooO00Oo = name
 o00o = cloudflare . source ( IIo0o0O0O00oOOo )
 IIIIiiIiiI = re . compile ( 'file: "(.+?)",.+?label: "(.+?)",' , re . DOTALL ) . findall ( o00o )
 for IIIIiI11I11 , ooO00o in IIIIiiIiiI :
  II1Ii1iI1i1 ( '[COLORgreen]' + ooOooO00Oo + ooO00o + '[/COLOR]' , IIIIiI11I11 , 10012 , ii11iIi1I + 'dtv.png' )
  if 73 - 73: i1I111ii1II1i * i1I111ii1II1i / OOO0OOo
 xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 43 - 43: ii11ii1ii . i1IIi . OoOo00o + O0 * iI * O0
 if 41 - 41: ii11ii1ii + iI % OoooooooOO . ii11ii1ii + i1I111ii1II1i . i1I111ii1II1i
def Iiii11I ( ) :
 if 66 - 66: I1IiI + i1IIi % OoOoOO00 . O0 * ii11ii1ii % ii11ii1ii
 if 87 - 87: i1I111II1I + OOooOOo . i1I111ii1II1i - OoooooooOO
 if 6 - 6: iIii1I11I1II1 * OoooooooOO
 if 28 - 28: Oo * OOooOOo / o00OO00OoO
 if 52 - 52: O0 / OOooOOo % i1I111ii1II1i * OOOo0 % i1I111II1I
 if 69 - 69: ii11ii1ii
 if 83 - 83: OOooOOo
 if 38 - 38: o00OO00OoO + OoooooooOO . i1IIi
 if 19 - 19: i1I111ii1II1i - OOooOOo - iI - I1IiI . i1I111ii1II1i . o00OO00OoO
 if 48 - 48: i1I111ii1II1i + OoOo00o
 if 60 - 60: Oooo0Ooo000 + i1I111ii1II1i . OoOo00o / i1IIi . iIii1I11I1II1
 if 14 - 14: i1I111II1I
 if 79 - 79: iI
 if 76 - 76: iIii1I11I1II1
 if 80 - 80: iIii1I11I1II1 . O0 / iI % iI
 IIIIii ( '[COLORgreen]Newest Episodes Added[/COLOR]' , 'http://www.watchseries.li/latest' , 10046 , ii11iIi1I + 'WATCHSERIES.png' , '' , '' )
 IIIIii ( '[COLORgreen]This Week\'s Popular Episodes[/COLOR]' , 'http://www.watchseries.li/new' , 10042 , ii11iIi1I + 'WATCHSERIES.png' , '' , '' )
 IIIIii ( '[COLORgreen]Search Program[/COLOR]' , '' , 10043 , ii11iIi1I + 'WATCHSERIES.png' , '' , '' )
 if 93 - 93: OoooooooOO * Oo
 if 10 - 10: o00OO00OoO * OoooooooOO + Oooo0Ooo000 - ii11ii1ii / ii11ii1ii . i11iIiiIii
def i1I1i ( url ) :
 I11i1ii1 = O0Oooo0O ( url )
 OOOOOoo0 = re . compile ( '<ul class="pagination" style="line-height: 3;">(.+?)</ul>' , re . DOTALL ) . findall ( I11i1ii1 )
 O0o = re . compile ( '<li><a href="/letters/(.+?)">(.+?)</a></li>' ) . findall ( str ( OOOOOoo0 ) )
 for url , I1iI1iIi111i in O0o :
  IIIIii ( '[COLORgreen]' + I1iI1iIi111i + '[/COLOR]' , 'http://watchseries.li/letters/' + url , 10049 , ii11iIi1I + 'WATCHSERIES.png' , '' , '' )
  if 22 - 22: Oo % Ooo00oOo00o - OoooooooOO * Oo
def ii1i ( url ) :
 I11i1ii1 = O0Oooo0O ( url )
 O0o = re . compile ( '<a href="(.+?)" class="sr-header">(.+?)</a>' ) . findall ( I11i1ii1 )
 for url , I1iI1iIi111i in O0o :
  IIIIii ( '[COLORgreen]' + I1iI1iIi111i + '[/COLOR]' , 'http://watchseries.li/' + url , 10049 , ii11iIi1I + 'WATCHSERIES.png' , '' , '' )
  if 12 - 12: iI
def Ooii1IIi1ii ( url ) :
 I11i1ii1 = O0Oooo0O ( url )
 O0o = re . compile ( '<li class="col-md-6 col-xs-12 list-movies-li"><a href="(.+?)" title=".+?">(.+?)<span class="epnum">.+?</span></a></li>' , re . DOTALL ) . findall ( I11i1ii1 )
 IIIIiiIiiI = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="(.+?)">Next</a></li></ul>' , re . DOTALL ) . findall ( I11i1ii1 )
 for url , I1iI1iIi111i in O0o :
  IIIIii ( '[COLORgreen]' + ( I1iI1iIi111i ) . replace ( '&nbsp;' , ' ' ) . replace ( '&amp;' , '&' ) . replace ( '&#039;' , '\'' ) + '[/COLOR]' , 'http://www.watchseries.li' + url , 10044 , ii11iIi1I + 'WATCHSERIES.png' , '' , '' )
 for url in IIIIiiIiiI :
  IIIIii ( '[COLORgreen]' + 'NEXT' + '[/COLOR]' , 'http://www.watchseries.li' + url , 10049 , ii11iIi1I + 'Next.png' , '' , '' )
  if 85 - 85: OoooooooOO % I1IiI * iIii1I11I1II1
  if 44 - 44: iIii1I11I1II1 . ii11ii1ii + o00OO00OoO . OOO0OOo
def II1i11 ( ) :
 IiII111iI1ii1 = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 Ii1IIIII = 'http://www.watchseries.li/search/' + IiII111iI1ii1 . replace ( ' ' , '%20' )
 I11i1ii1 = O0Oooo0O ( Ii1IIIII )
 O0o = re . compile ( '<img src="(.+?)".+?<a href="(.+?)" title=".+?"><b>(.+?)</b>' , re . DOTALL ) . findall ( I11i1ii1 )
 for OO0ooOOO0OOO , oOo0 , I1iI1iIi111i in O0o :
  if 'watch online' in I1iI1iIi111i :
   pass
  else :
   print oOo0
   IIIIii ( '[COLORgreen]' + I1iI1iIi111i + '[/COLOR]' , 'http://www.watchseries.li' + oOo0 , 10044 , OO0ooOOO0OOO , '' , '' )
   if 49 - 49: iIii1I11I1II1 % OoOoOO00
   xbmcplugin . setContent ( O0O , 'movies' )
   if 50 - 50: O0 . O0 . OOO0OOo % Oo
def ooo000oOO ( url ) :
 I11i1ii1 = O0Oooo0O ( url )
 O0o = re . compile ( '<img src="(.+?)".+?<div class="block-left-home-inside-text">.+?<a href="(.+?)" title=".+?"><b>(.+?)</b> <br>.+?<span class=".+?">(.+?)</span></a><br>(.+?)<br>' , re . DOTALL ) . findall ( I11i1ii1 )
 for OO0ooOOO0OOO , url , I1iI1iIi111i , IiIIi11i111 , OOoOO0ooo in O0o :
  iI1iI1IiIIiI = ( I1iI1iIi111i ) . replace ( '&nbsp;' , ' ' ) . replace ( '&amp;' , '&' ) . replace ( '&#039;' , '\'' ) + ' - ' + ( IiIIi11i111 ) . replace ( '&amp;' , '&' ) . replace ( '&#039;' , '\'' )
  IIIIii ( '[COLORgreen]' + iI1iI1IiIIiI + '[/COLOR]' , 'http://www.watchseries.li' + url , 10045 , OO0ooOOO0OOO , '' , OOoOO0ooo )
  if 87 - 87: I1IiI % iIii1I11I1II1
def o0OO0OOO0O ( url ) :
 I11i1ii1 = O0Oooo0O ( url )
 O0o = re . compile ( '<li class="col-md-6 col-xs-12 list-movies-li"><a href="(.+?)" title=".+?">(.+?)<span class="epnum">.+?</span></a></li>' , re . DOTALL ) . findall ( I11i1ii1 )
 IIIIiiIiiI = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="(.+?)">Next</a></li></ul>' , re . DOTALL ) . findall ( I11i1ii1 )
 for url , I1iI1iIi111i in O0o :
  iI1iI1IiIIiI = ( I1iI1iIi111i ) . replace ( '&nbsp;' , ' ' ) . replace ( '&amp;' , '&' ) . replace ( '&#039;' , '\'' )
  IIIIii ( '[COLORgreen]' + iI1iI1IiIIiI + '[/COLOR]' , 'http://www.watchseries.li' + url , 10045 , ii11iIi1I + 'WATCHSERIES.png' , '' , '' )
 for url in IIIIiiIiiI :
  IIIIii ( '[COLORgreen]' + 'NEXT' + '[/COLOR]' , 'http://www.watchseries.li' + url , 10046 , ii11iIi1I + 'Next.png' , '' , '' )
  if 36 - 36: i11iIiiIii / i1I111ii1II1i . Oooo0Ooo000 + OoOo00o . O0 + OOOo0
def iiII1iiIi ( url ) :
 I11i1ii1 = O0Oooo0O ( url )
 O0o = re . compile ( '<div class="mask">.+?<a href="(.+?)" title="(.+?)">.+?<img src="(.+?)"' , re . DOTALL ) . findall ( I11i1ii1 )
 IIIIiiIiiI = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="(.+?)">Next</a></li></ul>' , re . DOTALL ) . findall ( I11i1ii1 )
 for url , I1iI1iIi111i , OO0ooOOO0OOO in O0o :
  IIIIii ( '[COLORgreen]' + ( I1iI1iIi111i ) . replace ( '&nbsp;' , ' ' ) . replace ( '&amp;' , '&' ) . replace ( '&#039;' , '\'' ) + '[/COLOR]' , 'http://www.watchseries.li' + url , 10044 , OO0ooOOO0OOO , '' , '' )
 for url in IIIIiiIiiI :
  IIIIii ( '[COLORgreen]' + 'NEXT' + '[/COLOR]' , 'http://www.watchseries.li' + url , 10041 , ii11iIi1I + 'Next.png' , '' , '' )
  if 33 - 33: ii11ii1ii * OoOoOO00 * i1I111II1I
def OOO0o0 ( url ) :
 I11i1ii1 = O0Oooo0O ( url )
 OOOOOoo0 = re . compile ( '<div class="col-md-6 col-xs-12".+?<a href=".+?" itemprop="url"><span itemprop="name">(.+?)</span>(.+?)</ul>' , re . DOTALL ) . findall ( I11i1ii1 )
 for oo0oo , IiiIIIiI1ii in OOOOOoo0 :
  O0o = re . compile ( '<li itemprop="episode".+?<meta itemprop="url" content="(.+?)">.+?<span class="" itemprop="name">\n(.+?)\n' , re . DOTALL ) . findall ( str ( IiiIIIiI1ii ) )
  for url , I1iI1iIi111i in O0o :
   iI1iI1IiIIiI = ( oo0oo ) . replace ( '  ' , '' ) + ' ' + ( I1iI1iIi111i ) . replace ( '&nbsp;' , ' ' ) . replace ( '&#039;' , '\'' ) . replace ( '  ' , '' )
   IIIIii ( '[COLORgreen]' + iI1iI1IiIIiI + '[/COLOR]' , 'http://www.watchseries.li' + url , 10045 , ii11iIi1I + 'WATCHSERIES.png' , '' , '' )
 IIIIiiIiiI = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="(.+?)">Next</a></li></ul>' , re . DOTALL ) . findall ( I11i1ii1 )
 for url in IIIIiiIiiI :
  IIIIii ( '[COLORgreen]' + 'NEXT' + '[/COLOR]' , 'http://www.watchseries.li' + url , 10044 , ii11iIi1I + 'Next.png' , '' , '' )
  if 34 - 34: OOOo0 % Oo - I1IiI + i1I111ii1II1i
  if 79 - 79: OoOoOO00 - OOO0OOo . i1IIi + O0 % O0 * OOOo0
class Ii1Ii1I ( ) :
 if 54 - 54: O0ooOooooO + I1IiI
 List = [ ]
 source_list = [ ]
 def __init__ ( self , name ) :
  if 77 - 77: Oooo0Ooo000 . OoOo00o
  iI1iI1IiIIiI = name
  self . Get_Sources ( oOo0 , iI1iI1IiIIiI )
  if 58 - 58: Oooo0Ooo000 * I1IiI
  if 94 - 94: iI - ii11ii1ii + OOooOOo - Oo
 def Get_Sources ( self , URL , season_name ) :
  Oo0oO0ooo = xbmcgui . DialogProgress ( )
  I11i1ii1 = O0Oooo0O ( URL )
  O0o = re . compile ( '<td>.+?<a href="/link/(.+?)".+?height="16px">(.+?)\n' , re . DOTALL ) . findall ( I11i1ii1 )
  for oOo0 , I1iI1iIi111i in O0o :
   URL = 'http://www.watchseries.li/link/' + oOo0
   self . Get_site_link ( URL , season_name )
   if 15 - 15: i1I111II1I
 def Get_site_link ( self , url , season_name ) :
  I11i1ii1 = O0Oooo0O ( url )
  O0o = re . compile ( '<iframe style=.+?" src="(.+?)"' ) . findall ( I11i1ii1 )
  IIIIiiIiiI = re . compile ( '<IFRAME SRC="(.+?)"' ) . findall ( I11i1ii1 )
  O0oOOo0o = re . compile ( '<IFRAME style=".+?" SRC="(.+?)"' ) . findall ( I11i1ii1 )
  for url in O0o :
   self . main ( url , season_name )
  for url in IIIIiiIiiI :
   self . main ( url , season_name )
  for url in O0oOOo0o :
   self . main ( url , season_name )
   if 31 - 31: i1I111ii1II1i / i1IIi . Ooo00oOo00o
 def main ( self , url , season_name ) :
  Oo0oO0ooo . create ( "[COLORwhite]Origin[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
  if 'daclips.in' in url :
   OOOoo = 'DACLIPS'
   if OOOoo in Ii1Ii1I . source_list :
    pass
   else :
    self . daclips ( url , season_name , OOOoo )
    Oo0oO0ooo . update ( 0 , "" , "Getting Daclips Links" )
  else :
   if 'filehoot.com' in url :
    OOOoo = 'FILEHOOT'
    if OOOoo in Ii1Ii1I . source_list :
     pass
    else :
     Oo0oO0ooo . update ( 0 , "" , "Getting Filehoot Links" )
     self . filehoot ( url , season_name , OOOoo )
   else :
    if 'thevideo.me' in url :
     OOOoo = 'THEVIDEO'
     if OOOoo in Ii1Ii1I . source_list :
      pass
     else :
      self . thevideo ( url , season_name , OOOoo )
      Oo0oO0ooo . update ( 0 , "" , "Getting Thevideo Links" )
    else :
     if 'allmyvideos.net' in url :
      OOOoo = 'ALLMYVIDEOS'
      if OOOoo in Ii1Ii1I . source_list :
       pass
      else :
       self . allmyvid ( url , season_name , OOOoo )
       Oo0oO0ooo . update ( 0 , "" , "Getting Allmyvideo Links" )
     else :
      if 'vidspot.net' in url :
       OOOoo = 'VIDSPOT'
       if OOOoo in Ii1Ii1I . source_list :
        pass
       else :
        self . vidspot ( url , season_name , OOOoo )
        Oo0oO0ooo . update ( 0 , "" , "Getting Vidspot Links" )
      else :
       if 'vodlocker' in url :
        OOOoo = 'VODLOCKER'
        if OOOoo in Ii1Ii1I . source_list :
         pass
        else :
         self . vodlocker ( url , season_name , OOOoo )
         Oo0oO0ooo . update ( 0 , "" , "Getting Vodlocker Links" )
         if 25 - 25: ii11ii1ii + O0ooOooooO + OoooooooOO . OoOoOO00 . i1I111ii1II1i
         if 66 - 66: OOO0OOo * I1IiI
 def allmyvid ( self , url , season_name , source_name ) :
  I11i1ii1 = O0Oooo0O ( url )
  O0o = re . compile ( '"file" : "(.+?)",\n.+?"default" : .+?,\n.+?"label" : "(.+?)"' , re . DOTALL ) . findall ( I11i1ii1 )
  for II1 , I1iI1iIi111i in O0o :
   self . Printer ( II1 , season_name , source_name )
   if 91 - 91: i1I111II1I + o00OO00OoO . Oooo0Ooo000
 def vidspot ( self , url , season_name , source_name ) :
  I11i1ii1 = O0Oooo0O ( url )
  O0o = re . compile ( '"file" : "(.+?)",\n.+?"default" : .+?,\n.+?"label" : "(.+?)"' ) . findall ( I11i1ii1 )
  for II1 , I1iI1iIi111i in O0o :
   self . Printer ( II1 , season_name , source_name )
   if 15 - 15: Oooo0Ooo000
 def thevideo ( self , url , season_name , source_name ) :
  I11i1ii1 = O0Oooo0O ( url )
  O0o = re . compile ( "{ label: '.+?', file: '(.+?)' }" ) . findall ( I11i1ii1 )
  for II1 in O0o :
   self . Printer ( II1 , season_name , source_name )
   if 94 - 94: o00OO00OoO % OoOoOO00 * i1IIi * iIii1I11I1II1
 def vodlocker ( self , url , season_name , source_name ) :
  I11i1ii1 = O0Oooo0O ( url )
  O0o = re . compile ( 'file: "(.+?)",.+?skin' , re . DOTALL ) . findall ( I11i1ii1 )
  for II1 in O0o :
   self . Printer ( II1 , season_name , source_name )
   if 81 - 81: Oo - Oooo0Ooo000
 def daclips ( self , url , season_name , source_name ) :
  I11i1ii1 = O0Oooo0O ( url )
  O0o = re . compile ( '{ file: "(.+?)", type:"video" }' ) . findall ( I11i1ii1 )
  for II1 in O0o :
   self . Printer ( II1 , season_name , source_name )
   if 24 - 24: OoooooooOO . Ooo00oOo00o * OoOoOO00
 def filehoot ( self , url , season_name , source_name ) :
  I11i1ii1 = O0Oooo0O ( url )
  O0o = re . compile ( 'file: "(.+?)",.+?skin' , re . DOTALL ) . findall ( I11i1ii1 )
  for II1 in O0o :
   self . Printer ( II1 , season_name , source_name )
   if 59 - 59: o00OO00OoO + Ooo00oOo00o / i1I111II1I
 def Printer ( self , Link , season_name , source_name ) :
  if 97 - 97: Oo * i1I111ii1II1i % OOO0OOo . i1I111ii1II1i - o00OO00OoO - i1I111II1I
  if Link in Ii1Ii1I . List :
   pass
  elif source_name in Ii1Ii1I . source_list :
   pass
  else :
   II1Ii1iI1i1 ( '[COLORgreen]' + source_name + '[/COLOR]' , Link , 10012 , ii11iIi1I + 'WATCHSERIES.png' )
   Oo0oO0ooo . update ( 100 , "" , "Got Source" )
   Ii1Ii1I . List . append ( Link )
   Ii1Ii1I . source_list . append ( source_name )
   if 79 - 79: OOOo0 - OOO0OOo
   xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
   if 37 - 37: OoOo00o . Oo * Oo * OoOoOO00 * O0
   if 83 - 83: OoOo00o / o00OO00OoO
   if 64 - 64: Ooo00oOo00o % OoOo00o . o00OO00OoO % Ooo00oOo00o + Oooo0Ooo000 * OoOo00o
   if 83 - 83: OOooOOo % O0ooOooooO + Oooo0Ooo000 % i11iIiiIii + O0
   if 65 - 65: iIii1I11I1II1 % O0ooOooooO + O0 / OoooooooOO
def O0000oO0o00 ( ) :
 IIIIii ( '[COLORgreen]Highlights[/COLOR]' , '' , 10008 , ii11iIi1I + 'ORIGINFOOTBALL.png' , i1iiIII111ii , '' )
 IIIIii ( '[COLORgreen]Fixtures[/COLOR]' , '' , 10009 , ii11iIi1I + 'ORIGINFOOTBALL.png' , i1iiIII111ii , '' )
 if 80 - 80: OoooooooOO + OoOo00o
def O00O ( ) :
 OO0oo = O0Oooo0O ( i1111 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20vcXVpY2tpbmRleC5odG1s' ) )
 O0o = re . compile ( '<a target="_self" href="(.+?)".+?src="(.+?)" alt="(.+?)"' , re . DOTALL ) . findall ( OO0oo )
 for oOo0 , OO0ooOOO0OOO , I1iI1iIi111i in O0o :
  IIIIii ( '[COLORgreen]' + ( I1iI1iIi111i ) . replace ( 'amp;' , '' ) + '[/COLOR]' , i1111 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20v' ) + oOo0 , 10010 , i1111 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20v' ) + OO0ooOOO0OOO , i1iiIII111ii , '' )
  if 63 - 63: OoooooooOO * OoooooooOO % Ooo00oOo00o + O0 / o00OO00OoO + iIii1I11I1II1
def oO0o0o00oOo0O ( url ) :
 I11i1ii1 = O0Oooo0O ( url )
 OOOOOoo0 = re . compile ( 'AndClearL.+?><h2.+?head>(.*?)float' , re . DOTALL ) . findall ( I11i1ii1 )
 for OOOOOoo0 in OOOOOoo0 :
  oOOoooO0O0 = re . compile ( '(.*?)</h2>' ) . findall ( str ( OOOOOoo0 ) )
  for ii1O0ooooo000 in oOOoooO0O0 :
   ii1O0ooooo000 = ii1O0ooooo000
  OooOoOO0OO = re . compile ( 'comp_head>(.*?)</span>.*?<div class = fLeft width = ".*?"><img src="(.*?)">.*?</div>.*?ST:(.*?)</div>(.+?)<!-- around all of channel types ENDS 2-->' , re . DOTALL ) . findall ( str ( OOOOOoo0 ) )
  for I1iiIiiii1111 , OO0ooOOO0OOO , time , I1ii1i11i in OooOoOO0OO :
   I11IIIi = re . compile ( ",CAPTION, '(.+?)&nbsp" ) . findall ( I1ii1i11i )
   IIIIii ( '[COLORgreen]' + ii1O0ooooo000 + ' - ' + I1iiIiiii1111 + ' - ' + time + '[/COLOR]' , '' , 10010 , i1111 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20=' ) + OO0ooOOO0OOO , i1iiIII111ii , ( str ( I11IIIi ) ) )
   if 86 - 86: O0 % i1IIi . OoOoOO00 . Oooo0Ooo000
 O00Oo000ooO0 ( 'tvshows' , 'Media Info 3' )
 if 44 - 44: i11iIiiIii * Oooo0Ooo000 + I1IiI + OoOo00o * O0 . OoOo00o
def ii1II1II ( ) :
 if 42 - 42: iI
 IIIIii ( '[COLORgreen]Shows[/COLOR]' , 'http://www.fullmatchesandshows.com/category/show/' , 10011 , 'http://www.fm-base.co.uk/forum/attachments/club-competition-logos/3885-soccer-am-logo-socceram.png' , ii11iIi1I + 'fanart.jpg' , '' )
 IIIIii ( '[COLORgreen]Premier League[/COLOR]' , 'http://www.fullmatchesandshows.com/premier-league/' , 10011 , 'https://footballseasons.files.wordpress.com/2013/05/premier-league.png' , ii11iIi1I + 'fanart.jpg' , '' )
 IIIIii ( '[COLORgreen]La Liga[/COLOR]' , 'http://www.fullmatchesandshows.com/la-liga/' , 10011 , 'http://1.bp.blogspot.com/-c6kQ40ryhyo/U19cUlz25sI/AAAAAAAABak/qtn5chSFZm0/s1600/la-liga-logo_display_image.png' , ii11iIi1I + 'fanart.jpg' , '' )
 IIIIii ( '[COLORgreen]Bundesliga[/COLOR]' , 'http://www.fullmatchesandshows.com/bundesliga/' , 10011 , 'http://m.img.brothersoft.com/iphone/189/518670189_icon175x175.jpg' , ii11iIi1I + 'fanart.jpg' , '' )
 IIIIii ( '[COLORgreen]Champions League[/COLOR]' , 'http://www.fullmatchesandshows.com/champions-league/' , 10011 , 'http://www.ecursuri.ro/images/teste/test-champions-league.jpg' , ii11iIi1I + 'fanart.jpg' , '' )
 IIIIii ( '[COLORgreen]Serie A[/COLOR]' , 'http://www.fullmatchesandshows.com/category/serie-a/' , 10011 , 'http://files.jcriccione.it/200000223-2484526782/serie%20a.png' , ii11iIi1I + 'fanart.jpg' , '' )
 IIIIii ( '[COLORgreen]Ligue 1[/COLOR]' , 'http://www.fullmatchesandshows.com/category/ligue-1/' , 10011 , 'http://a1.mzstatic.com/us/r30/Purple5/v4/37/c7/44/37c744ae-5824-42b7-6ce0-5f471f52baab/icon180x180.jpeg' , ii11iIi1I + 'fanart.jpg' , '' )
 IIIIii ( '[COLORgreen]Copa America 2015[/COLOR]' , 'http://www.fullmatchesandshows.com/copa-america-2015/' , 10011 , 'https://pbs.twimg.com/profile_images/521966985907691520/Nq9OAPIo_400x400.png' , ii11iIi1I + 'fanart.jpg' , '' )
 IIIIii ( '[COLORgreen]CONCACAF[/COLOR]' , 'http://www.fullmatchesandshows.com/category/concacaf/' , 10011 , 'http://a3.mzstatic.com/us/r30/Purple3/v4/40/26/14/4026147c-7022-4ca3-504e-e78950cc3f1c/icon175x175.png' , ii11iIi1I + 'fanart.jpg' , '' )
 IIIIii ( '[COLORgreen]Women World Cup[/COLOR]' , 'http://www.fullmatchesandshows.com/category/women-world-cup/' , 10011 , 'https://upload.wikimedia.org/wikipedia/en/thumb/7/76/2015_FIFA_Women\'s_World_Cup_logo.svg/967px-2015_FIFA_Women\'s_World_Cup_logo.svg.png' , ii11iIi1I + 'fanart.jpg' , '' )
 if 68 - 68: i1I111II1I . Oo % OOO0OOo - OoooooooOO * i1I111ii1II1i . i1I111II1I
def Ii1I1i111 ( url ) :
 I11i1ii1 = O0Oooo0O ( url )
 O0o = re . compile ( 'itemprop="image" class="entry-thumb" src="(.+?)".+?<h3 itemprop="name" class="entry-title td-module-title"><a itemprop="url" href="(.+?)" rel="bookmark" title=".+?">(.+?)</a></h3>' , re . DOTALL ) . findall ( I11i1ii1 )
 for OO0ooOOO0OOO , url , I1iI1iIi111i in O0o :
  oOi1 = I1iI1iIi111i . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' )
  II1Ii1iI1i1 ( '[COLORgreen]' + oOi1 + '[/COLOR]' , url , 10013 , OO0ooOOO0OOO )
  if 39 - 39: OOO0OOo / O0 * OoOo00o
def I1IiII1iI1 ( url ) :
 I11i1ii1 = O0Oooo0O ( url )
 O0o = re . compile ( '<script data-config="(.+?)" data-height' ) . findall ( I11i1ii1 )
 for IIIIiI11I11 in O0o :
  oOOO00OOOoOO = ( IIIIiI11I11 ) . replace ( '/v2' , '' ) . replace ( 'zeus.json' , 'video-sd.mp4?hosting_id=21772' ) . replace ( 'config.playwire.com' , 'cdn.video.playwire.com' )
  OO0ooo0o0 ( 'http:' + oOOO00OOOoOO )
  if 23 - 23: I1IiI . OOooOOo - Ooo00oOo00o / I1IiI * iIii1I11I1II1
  if 13 - 13: OOooOOo * i11iIiiIii / i11iIiiIii . Ooo00oOo00o . i1I111II1I . ii11ii1ii
def iIIiIi ( url ) :
 OO0oo = Iii1 ( url )
 O0o = re . compile ( '<a href="([^"]*)" title="([^"]*)"><img itemprop="image" content="([^"]*)"' , re . DOTALL ) . findall ( OO0oo )
 IIIIiiIiiI = re . compile ( "<a rel='next' href=([^=]*)=" , re . DOTALL ) . findall ( OO0oo )
 for url , I1iI1iIi111i , OO0ooOOO0OOO in O0o :
  II1Ii1iI1i1 ( I1iI1iIi111i , url , 8046 , OO0ooOOO0OOO )
 for url in IIIIiiIiiI :
  I1I1i1I ( 'NEXT PAGE' , ( url ) . replace ( ' class' , '' ) , 8045 , ii11iIi1I + 'Next.png' )
def oO0Oo00oo ( url ) :
 OO0oo = Iii1 ( url )
 O0o = re . compile ( "__filename='([^']*)',.+?__fullimage='([^']*)',.+?__title='([^']*)'," , re . DOTALL ) . findall ( OO0oo )
 for url , OO0ooOOO0OOO , I1iI1iIi111i in O0o :
  OO0ooo0o0 ( 'http://bitcast-b.bitgravity.com/ndtvod/23372/ndtv/' + url )
  if 75 - 75: iIii1I11I1II1 * i11iIiiIii - OoooooooOO . I1IiI
def OOOO0O00Ooooo ( url ) :
 OO0oo = Iii1 ( url )
 O0o = re . compile ( "src='http://www.youtube.com/embed/(.+?)?version=3&#038;rel=1&#038;fs=1&#038;autohide=2&#038;showsearch=0&#038;showinfo=1&#038;iv_load_policy=1&#038;wmode=transparent' frameborder='0' allowfullscreen='true'></iframe>" ) . findall ( OO0oo )
 for url in O0o :
  yt . PlayVideo ( url )
  if 2 - 2: i1IIi * O0ooOooooO - O0ooOooooO + OoooooooOO % I1IiI / I1IiI
def i11IiI1iiI11 ( ) :
 OO0oo = Iii1 ( i1111 ( 'aHR0cDovL3RvcGRvY3VtZW50YXJ5ZmlsbXMuY29tLw==' ) )
 O0o = re . compile ( '<a href="(.+?)" >(.+?)</a></li><li>' ) . findall ( OO0oo )
 for oOo0 , I1iI1iIi111i in O0o :
  I1I1i1I ( I1iI1iIi111i , oOo0 , 8041 , ii11iIi1I + 'documentary.png' )
def OOoOOOO00 ( url ) :
 OO0oo = Iii1 ( url )
 O0o = re . compile ( '<h2><a href="(.+?)" title="(.+?)">.+?</a></h2>.+?src="(.+?)"' , re . DOTALL ) . findall ( OO0oo )
 IIIIiiIiiI = re . compile ( 'class="inactive">.+?</a><a href="(.+?)">Next</a></div>' , re . DOTALL ) . findall ( OO0oo )
 for url , I1iI1iIi111i , OO0ooOOO0OOO in O0o :
  I1I1i1I ( ( I1iI1iIi111i ) . replace ( '&#039;s' , '' ) , url , 8042 , OO0ooOOO0OOO )
 for url in IIIIiiIiiI :
  I1I1i1I ( 'NEXT PAGE' , url , 8041 , ii11iIi1I + 'Next.png' )
  if 49 - 49: Ooo00oOo00o - O0 / Ooo00oOo00o * I1IiI + o00OO00OoO
  if 35 - 35: OoOoOO00 . OOOo0 / i1IIi / OOOo0 * O0ooOooooO
def Oo0O0000Oo00o ( url ) :
 OO0oo = Iii1 ( url )
 O0o = re . compile ( '<meta itemprop="name" content="(.+?)".+?<meta itemprop="thumbnailUrl" content="(.+?)".+?<meta itemprop="embedUrl" content="(.+?)".+?<meta itemprop="description" content="(.+?)" />' , re . DOTALL ) . findall ( OO0oo )
 IIIIiiIiiI = re . compile ( '<div class="video new-video"><iframe width="766" height="431" src="(.+?)&amp;iv_load_policy=3&amp;showinfo=0&amp;autohide=1"' , re . DOTALL ) . findall ( OO0oo )
 for I1iI1iIi111i , OO0ooOOO0OOO , url , Ii1IIi in O0o :
  II1Ii1iI1i1 ( ( I1iI1iIi111i ) . replace ( '&#039;s' , '' ) , url . replace ( 'https://www.youtube.com/embed/' , '' ) , 8043 , OO0ooOOO0OOO )
 for url in IIIIiiIiiI :
  II1ii ( ( url ) . replace ( '//' , 'http://' ) )
  if 89 - 89: i1I111ii1II1i . i11iIiiIii * O0
def II1ii ( url ) :
 OO0oo = Iii1 ( url )
 O0o = re . compile ( '<link rel="canonical" href="(.+?)">  <link rel="stylesheet"' ) . findall ( OO0oo )
 for url in O0o :
  II1Ii1iI1i1 ( 'PLAY' , ( url ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , ii11iIi1I + 'documentary.png' )
  if 44 - 44: i1IIi . OOOo0 / i11iIiiIii + OoOo00o
def iI111II1ii ( ) :
 I11i1ii1 = Iii1 ( 'http://www.stream2watch.co/live-tv' )
 O0o = re . compile ( '<a href="(.+?)">.+?<img src="(.+?)" alt=".+?"/>.+?<span class="country_name">(.+?)<br />(.+?)</span>' , re . DOTALL ) . findall ( I11i1ii1 )
 for oOo0 , OO0ooOOO0OOO , I1iI1iIi111i , O0ooO00ooOO0o in O0o :
  I1I1i1I ( ( I1iI1iIi111i + '[COLORgreen]' + O0ooO00ooOO0o + '[/COLOR]' ) , oOo0 , 8086 , OO0ooOOO0OOO )
  if 65 - 65: i1I111ii1II1i . Ooo00oOo00o + iI
def IIiI1I ( url ) :
 I11i1ii1 = Iii1 ( url )
 O0o = re . compile ( '<a class="front_channel_href" href="(.+?)" title=".+?">.+?<img class="front_channel_thumb" src="(.+?)" alt=".+?"/>.+?<span class="front_channel_name">(.+?)</span>' , re . DOTALL ) . findall ( I11i1ii1 )
 for url , OO0ooOOO0OOO , I1iI1iIi111i in O0o :
  I1I1i1I ( '[COLORgreen]' + I1iI1iIi111i + '[/COLOR]' , url , 8087 , OO0ooOOO0OOO )
  if 67 - 67: iI
def iIII11Iiii1 ( url ) :
 I11i1ii1 = O0Oooo0O ( url )
 O0o = re . compile ( 'a id="code_.+?data-f-href="(.+?)" data-code-embed="">(.+?)</a>' , re . DOTALL ) . findall ( I11i1ii1 )
 for url , I1iI1iIi111i in O0o :
  o0oo0 ( url , I1iI1iIi111i )
  if 67 - 67: O0 * Oooo0Ooo000 - OOooOOo - OoOoOO00
def o0oo0 ( url , name ) :
 I11i1ii1 = O0Oooo0O ( url )
 O0o = re . compile ( "playStream\('.+?', '(.+?)'\);" , re . DOTALL ) . findall ( I11i1ii1 )
 for url in O0o :
  print url
  II1Ii1iI1i1 ( '[COLORgreen]' + name + '[/COLOR]' , url , 222 , '' )
  if 41 - 41: OOOo0 - o00OO00OoO % OoOoOO00 . o00OO00OoO - Oooo0Ooo000
def i1I111Ii ( ) :
 OO0oo = Iii1 ( i1111 ( 'aHR0cDovL3d3dy5zb2xpZS5vcmcvYWxpYnJhcnkvaW5kZXguaHRtbA==' ) )
 O0o = re . compile ( '<td align="center" valign="top">.+?<a href="(.+?)">.+?<img src="(.+?)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( OO0oo )
 for oOo0 , OO0ooOOO0OOO , I1iI1iIi111i in O0o :
  I1I1i1I ( ( '[COLORgreen]' + I1iI1iIi111i + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + oOo0 , 3002 , 'http://www.solie.org/alibrary/' + OO0ooOOO0OOO )
def i11i1i ( url ) :
 OO0oo = Iii1 ( url )
 O0o = re . compile ( '<td align="center" valign="top">.+?<a href="(.+?)">.+?<img src="(.+?)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( OO0oo )
 for url , OO0ooOOO0OOO , I1iI1iIi111i in O0o :
  I1I1i1I ( ( '[COLORgreen]' + I1iI1iIi111i + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3003 , 'http://www.solie.org/alibrary/' + OO0ooOOO0OOO )
def I1ii1Ii1 ( url ) :
 OO0oo = Iii1 ( url )
 O0o = re . compile ( '<br><a href="([^"]*)">(.+?)</a>' ) . findall ( OO0oo )
 OoO = re . compile ( 'href="([^"]*)">Season(.+?)</a>' ) . findall ( OO0oo )
 next = re . compile ( '<a href="([^"]*)">Episodes</a>' ) . findall ( OO0oo )
 IIIIiiIiiI = re . compile ( '<td align="center" valign="top">.+?<a href="(.+?)">.+?<img src="(.+?)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( OO0oo )
 for url , I1iI1iIi111i in O0o :
  II1Ii1iI1i1 ( ( '[COLORgreen]' + I1iI1iIi111i + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3004 , ii11iIi1I + 'classicmovies.png' )
 for url , I1iI1iIi111i in OoO :
  I1I1i1I ( '[COLORgreen]Season- ' + I1iI1iIi111i + '[/COLOR]' , 'http://www.solie.org/alibrary/' + url , 3003 , ii11iIi1I + 'classicmovies.png' )
 for url in next :
  I1I1i1I ( '[COLORgreen]NEXT[/COLOR]' , 'http://www.solie.org/alibrary/' + url , 3003 , ii11iIi1I + 'Next.png' )
 for url , OO0ooOOO0OOO , I1iI1iIi111i in IIIIiiIiiI :
  I1I1i1I ( ( '[COLORgreen]' + I1iI1iIi111i + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3003 , 'http://www.solie.org/alibrary/' + OO0ooOOO0OOO )
def oOiI111I1III ( url ) :
 OO0oo = Iii1 ( url )
 O0o = re . compile ( '<iframe.+?src="([^"]*)"' ) . findall ( OO0oo )
 for url in O0o :
  i111IiiI1Ii ( url )
def i111IiiI1Ii ( url ) :
 OO0oo = Iii1 ( url )
 O0o = re . compile ( '<meta property="og:video" content="([^"]*)"/>' ) . findall ( OO0oo )
 for url in O0o :
  OO0ooo0o0 ( url )
  if 72 - 72: O0 . I1IiI * Oo + ii11ii1ii - OOooOOo
def iII1I11 ( ) :
 OO0oo = Iii1 ( i1111 ( 'aHR0cDovL3JldHJvdmlzaW9uLnR2L2FsbC8=' ) )
 O0o = re . compile ( '<a href="([^"]*)"><h2><font color=".+?"><h2>(.+?)</font></h2></a>' ) . findall ( OO0oo )
 for oOo0 , I1iI1iIi111i in O0o :
  II1Ii1iI1i1 ( ( '[COLORgreen]' + I1iI1iIi111i + '[/COLOR]' ) . replace ( '&#8211;' , ':' ) , oOo0 , 8061 , ii11iIi1I + 'classicmovies.png' )
def ii11iiI11I ( url ) :
 OO0oo = Iii1 ( url )
 O0o = re . compile ( "v.src = '([^']*)';" ) . findall ( OO0oo )
 for url in O0o :
  OO0ooo0o0 ( url )
  if 96 - 96: iIii1I11I1II1 + i11iIiiIii - Oo . OOO0OOo
def iiIi11i1IiI ( ) :
 OO0oo = Iii1 ( i1111 ( 'aHR0cDovL3JldHJvdmlzaW9uLnR2L2NsYXNzaWMtdHYv' ) )
 O0o = re . compile ( '<a href="([^"]*)"><h2><font color=".+?"><h2>(.+?)</font></h2></a>' ) . findall ( OO0oo )
 for oOo0 , I1iI1iIi111i in O0o :
  II1Ii1iI1i1 ( ( '[COLORgreen]' + I1iI1iIi111i + '[/COLOR]' ) . replace ( '&#8211;' , ':' ) , oOo0 , 8061 , ii11iIi1I + 'classictv.png' )
def oO00O0O0 ( url ) :
 OO0oo = Iii1 ( url )
 O0o = re . compile ( "v.src = '([^']*)';" ) . findall ( OO0oo )
 for url in O0o :
  OO0ooo0o0 ( url )
  if 51 - 51: Ooo00oOo00o + OOOo0 * iI
def oOO0O00O00OoO ( ) :
 I11i1ii1 = O0Oooo0O ( i1111 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vbTN1c3RyZWFtcw==' ) )
 O0o = re . compile ( '<li><a href="(.+?)"> (.+?).m3u</a></li>' ) . findall ( I11i1ii1 )
 for oOo0 , I1iI1iIi111i in O0o :
  I1I1i1I ( ( '[COLORgreen]' + I1iI1iIi111i + '[/COLOR]' ) . replace ( '-' , ' ' ) . replace ( '_' , ' ' ) , ( i1111 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vbTN1c3RyZWFtcy8=' ) ) + oOo0 , 8071 , ii11iIi1I + 'streams.png' )
def IiIiI1i1 ( url ) :
 I11i1ii1 = Iii1 ( url )
 O0o = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( I11i1ii1 )
 for I1iI1iIi111i , url in O0o :
  II1Ii1iI1i1 ( ( '[COLORgreen]' + I1iI1iIi111i + '[/COLOR]' ) . replace ( '_' , ' ' ) , ( url ) . strip ( ) , 404 , ii11iIi1I + 'streams.png' )
def ii11I1IIi1i ( url ) :
 I11i1ii1 = Iii1 ( url )
 O0o = re . compile ( 'EXTINF:(.+?),(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( I11i1ii1 )
 for OO0ooOOO0OOO , I1iI1iIi111i , url in O0o :
  url = ( ( i1111 ( 'aHR0cDovL2dlbmlldHYuaXB0di5yZTo4MDAwL2xpdmUv' ) ) + oO0o0o0ooO0oO + '/' + oo0o0O00 + url ) . strip ( )
  II1Ii1iI1i1 ( ( '[COLORgreen]' + I1iI1iIi111i + '[/COLOR]' ) . replace ( '_' , ' ' ) , ( url ) . replace ( '.ts' , '.m3u8' ) , 10012 , OO0ooOOO0OOO )
  if 44 - 44: OOOo0 * iIii1I11I1II1 / O0
def iiiIi ( ) :
 IIIIIii1ii11 ( 'Best Videos' , 'http://www.xvideos.com/best' , 10105 , ii11iIi1I + 'JIZBOX.png' , '' , '' )
 IIIIIii1ii11 ( 'Genres' , 'http://www.xvideos.com' , 10106 , ii11iIi1I + 'JIZBOX.png' , '' , '' )
 IIIIIii1ii11 ( 'Recently Uploaded' , 'http://xvideos.com' , 10105 , ii11iIi1I + 'JIZBOX.png' , '' , '' )
 IIIIIii1ii11 ( 'Tags' , 'http://www.xvideos.com/tags' , 10103 , ii11iIi1I + 'JIZBOX.png' , '' , '' )
 IIIIIii1ii11 ( 'Search' , '' , 10107 , ii11iIi1I + 'JIZBOX.png' , '' , '' , )
 if 62 - 62: O0 . Oo
def iI1ii ( url ) :
 I11i1ii1 = O0Oooo0O ( url )
 O0OooOO = re . compile ( '<li><a class=".+?".+?href="(.+?)">Next</a></li>' ) . findall ( I11i1ii1 )
 for url in O0OooOO :
  IIIIIii1ii11 ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10103 , ii11iIi1I + 'JIZBOX.png' , '' , '' )
 O0o = re . compile ( '<li><a href="(.+?)"><b>(.+?)</b><span class="navbadge default"(.+?)</span>' ) . findall ( I11i1ii1 )
 for url , I1iI1iIi111i , O0O0Oooo0o in O0o :
  IIIIIii1ii11 ( I1iI1iIi111i + ' - No of Videos : ' + ( O0O0Oooo0o ) . replace ( '>' , '' ) , 'http://www.xvideos.com' + url , 10105 , ii11iIi1I + 'JIZBOX.png' , '' , '' )
  if 49 - 49: OoOo00o / OOO0OOo / i1I111II1I
def IiIiIi1I11I ( url ) :
 I11i1ii1 = O0Oooo0O ( url )
 O0OooOO = re . compile ( 'href="([^"]*)">Next</a></li>' ) . findall ( I11i1ii1 )
 for url in O0OooOO :
  IIIIIii1ii11 ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10104 , ii11iIi1I + 'Next.png' , '' , '' )
 O0o = re . compile ( ':"([^"]*)".+?;</script></a></div></div><p class="profile-name"><a href="([^"]*)">(.+?)</a></p><p class="profile-counts">\n(.+?)\n' , re . DOTALL ) . findall ( I11i1ii1 )
 for OO0ooOOO0OOO , url , I1iI1iIi111i , IiI1i1i in O0o :
  IIIIIii1ii11 ( I1iI1iIi111i + '--' + IiI1i1i , 'http://www.xvideos.com' + url + '#_tabVideos,videos-best' , 10105 , ( OO0ooOOO0OOO ) . replace ( 'http:\/\/' , 'http://' ) , '' , '' )
  if 94 - 94: i1I111ii1II1i - Oo + O0ooOooooO
  if 59 - 59: Oooo0Ooo000 . OOOo0 - iIii1I11I1II1 + iIii1I11I1II1
def oO0o0Oo ( url ) :
 I11i1ii1 = O0Oooo0O ( url )
 O0o = re . compile ( '<div class="thumb-inside"><script>.+?<img src="(.+?)".+?<a href="(.+?)" title=".+?">(.+?)</a></p>.+?uration">(.+?)</span>.+?Porn quality:(.+?)</span>' , re . DOTALL ) . findall ( I11i1ii1 )
 for OO0ooOOO0OOO , url , I1iI1iIi111i , OOOoOO , o0OOoOoO00O000 in O0o :
  I1I1IiI1 ( I1iI1iIi111i + ' - Porn Quality : ' + o0OOoOoO00O000 + ' - ' + OOOoOO , 'http://www.xvideos.com' + url , 10108 , OO0ooOOO0OOO , OO0ooOOO0OOO , o0OOoOoO00O000 + ' - ' + OOOoOO )
 Ooo000O00 = re . compile ( '<li><a href="([^"]*)" class="no-page">Next</a></li></ul></div>' ) . findall ( I11i1ii1 )
 for url in Ooo000O00 :
  IIIIIii1ii11 ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10105 , ii11iIi1I + 'Next.png' , '' , '' )
  if 36 - 36: i1I111II1I % i11iIiiIii
def Iiii1Ii ( url ) :
 I11i1ii1 = O0Oooo0O ( url )
 OOOOOoo0 = re . compile ( '<div class="main-categories">(.+?)</div>' , re . DOTALL ) . findall ( I11i1ii1 )
 O0OooOO = re . compile ( '<li><a class=".+?".+?href="(.+?)">Next</a></li>' ) . findall ( I11i1ii1 )
 for url in O0OooOO :
  IIIIIii1ii11 ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10106 , ii11iIi1I + 'Next.png' , '' , '' )
 O0o = re . compile ( '<li><a href="(.+?)" class="btn btn-default">(.+?)</a>' ) . findall ( str ( OOOOOoo0 ) )
 for url , I1iI1iIi111i in O0o :
  IIIIIii1ii11 ( I1iI1iIi111i , 'http://www.xvideos.com' + url , 10105 , ii11iIi1I + 'JIZBOX.png' , '' , '' )
  if 62 - 62: i1IIi % I1IiI
  if 37 - 37: Oooo0Ooo000 * i1IIi
def I1IIII ( ) :
 IiII111iI1ii1 = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OooooOoO = ( IiII111iI1ii1 ) . replace ( ' ' , '+' ) . replace ( '&amp;' , '&' )
 Ii1I = OooooOoO . lower ( )
 o00OoOO0O0 = 'http://www.xvideos.com/?k=' + Ii1I
 print o00OoOO0O0 + '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'
 I11i1ii1 = O0Oooo0O ( o00OoOO0O0 )
 O0o = re . compile ( '<div class="thumb-inside"><script>.+?<img src="(.+?)".+?<a href="(.+?)" title=".+?">(.+?)</a></p>.+?uration">(.+?)</span>.+?Porn quality:(.+?)</span>' , re . DOTALL ) . findall ( I11i1ii1 )
 for OO0ooOOO0OOO , oOo0 , I1iI1iIi111i , OOOoOO , o0OOoOoO00O000 in O0o :
  I1I1IiI1 ( I1iI1iIi111i + ' - Porn Quality : ' + o0OOoOoO00O000 + ' - ' + OOOoOO , 'http://www.xvideos.com' + oOo0 , 10108 , OO0ooOOO0OOO , OO0ooOOO0OOO , o0OOoOoO00O000 + ' - ' + OOOoOO )
 Ooo000O00 = re . compile ( '<li><a href="([^"]*)" class="no-page">Next</a></li></ul></div>' ) . findall ( I11i1ii1 )
 for oOo0 in Ooo000O00 :
  IIIIIii1ii11 ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + oOo0 , 10105 , ii11iIi1I + 'Next.png' , '' , '' )
  if 6 - 6: OOO0OOo + i1I111II1I / Oo + OoOo00o % OoOoOO00 / Ooo00oOo00o
def iiIi ( url ) :
 I11i1ii1 = O0Oooo0O ( url )
 O0o = re . compile ( 'flv_url=(.+?)\;' ) . findall ( I11i1ii1 )
 for url in O0o :
  OooooOo = ( url ) . replace ( '%3A' , ':' ) . replace ( '%2F' , '/' ) . replace ( '%3F' , '?' ) . replace ( '%3D' , '=' ) . replace ( '%26' , '&' ) . replace ( '&amp' , '' )
  IIIiiiIiI ( OooooOo )
  if 80 - 80: O0ooOooooO % O0ooOooooO % O0 - i11iIiiIii . i1I111ii1II1i / O0
def IIIiiiIiI ( url ) :
 IIII1ii = xbmc . Player ( IiIi1Ii ( ) )
 import urlresolver
 try : IIII1ii . play ( url )
 except : pass
 if 39 - 39: iI
 if 24 - 24: i11iIiiIii - iI + O0ooOooooO * OOOo0
def OoooOo0 ( ) :
 I11i1ii1 = O0Oooo0O ( i1111 ( 'aHR0cDovL3d3dy5nb2Zpc2hpbmcuY28udWsvQW5nbGluZy1UaW1lcy9TZWN0aW9uL1ZpZGVvcy8=' ) )
 O0o = re . compile ( 'class="item.+?"><a href="(.+?)">(.+?)</a></li>' ) . findall ( I11i1ii1 )
 for oOo0 , I1iI1iIi111i in O0o :
  I1I1i1I ( '[COLORgreen]' + I1iI1iIi111i + '[/COLOR]' , ( 'http://www.gofishing.co.uk' + oOo0 ) . replace ( 'http://www.gofishing.co.ukhttp://www.gofishing.co.uk' , 'http://www.gofishing.co.uk' ) , 8091 , ii11iIi1I + 'gofish.png' )
def IiI1Ii1ii ( url ) :
 I11i1ii1 = Iii1 ( url )
 O0o = re . compile ( '<h2><a id=.+?href="([^"]*)">(.+?)</a></h2>' , re . DOTALL ) . findall ( I11i1ii1 )
 IIIIiiIiiI = re . compile ( '<h3><a href="([^"]*)" id=.+?>(.+?)</a> </h3>.+?<img src="([^"]*)"' , re . DOTALL ) . findall ( I11i1ii1 )
 next = re . compile ( 'href="([^"]*)">next</a>&gt;</li>' , re . DOTALL ) . findall ( I11i1ii1 )
 for url , I1iI1iIi111i in O0o :
  II1Ii1iI1i1 ( '[COLORgreen]' + I1iI1iIi111i + '[/COLOR]' , 'http://www.gofishing.co.uk/' + url , 8092 , ii11iIi1I + 'gofish.png' )
 for url , I1iI1iIi111i , OO0ooOOO0OOO in IIIIiiIiiI :
  II1Ii1iI1i1 ( '[COLORgreen]' + I1iI1iIi111i + '[/COLOR]' , 'http://www.gofishing.co.uk/' + url , 8092 , 'http://www.gofishing.co.uk/' + OO0ooOOO0OOO )
 for url in next :
  I1I1i1I ( '[COLORgreen]NEXT[/COLOR]' , url . replace ( ' ' , '+' ) , 8091 , ii11iIi1I + 'Next.png' )
def Ii11iiIIiI1 ( url ) :
 I11i1ii1 = Iii1 ( url )
 O0o = re . compile ( 'src="https://www.youtube.com/embed/(.+?)"' ) . findall ( I11i1ii1 )
 for url in O0o :
  yt . PlayVideo ( url )
  if 6 - 6: OoOo00o * OoooooooOO + o00OO00OoO / iI
def I1IiI1IIiI ( url ) :
 ooooo0o0oo0Ooo = urllib2 . Request ( url )
 ooooo0o0oo0Ooo . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
 iI1i = ''
 oOo00O000Oo0 = ''
 try :
  iI1i = urllib2 . urlopen ( ooooo0o0oo0Ooo )
  oOo00O000Oo0 = iI1i . read ( )
  iI1i . close ( )
 except : pass
 if oOo00O000Oo0 != '' :
  return oOo00O000Oo0
 else :
  oOo00O000Oo0 = 'Failed'
  return oOo00O000Oo0
  if 3 - 3: OoOo00o / Oooo0Ooo000
  if 34 - 34: i11iIiiIii / o00OO00OoO * i1I111II1I . Oo
def ooo0O00000oo0 ( ) :
 oOO0oo = ( i1111 ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 IiII111iI1ii1 = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 Ii1I = IiII111iI1ii1 . lower ( )
 oOo0 = ( i1111 ( 'aHR0cDovL2RsNC5tb3ZpZWZhcnNpLmNvbS9maWxtLzIwMTUtNy8=' ) )
 IIo0o0O0O00oOOo = ( i1111 ( 'aHR0cDovL2RsLmF2YWRsLmNvbS9OZXcvTW92aWUv' ) )
 OO0O0 = ( i1111 ( 'aHR0cDovLzIxNy4yMTkuMTQzLjEwOC8xMzI3Lw==' ) )
 o0oo0000 = ( i1111 ( 'aHR0cDovLzE3OC4xNjIuMjE0LjIzMi92b2QvbW92aWVzL2VuZ2xpc2gv' ) )
 oOo0OOOOoO = ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvbW92L2FsbC5waHA=' ) )
 OoO0Ooo = ( i1111 ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 Ii1I1I = ( i1111 ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL3NlYXJjaC8/cT0=' ) ) + IiII111iI1ii1
 oOOoOOO0oOoo = ( i1111 ( 'aHR0cDovL3JlZGVtcHRpb25idWlsZC4xNm1iLmNvbS9SZWRlbXB0aW9uL21vdmllcy9hbGxtb3ZpZS5waHA=' ) )
 o0O0ooooooo00 = ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9UaGVfUmVhcGVyL2FsbG1vdmllcy5waHA=' ) )
 I1111ii11IIII = ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC9tb3ZmdWxsLnBocA==' ) )
 IiIi1II111I = ( i1111 ( 'aHR0cDovLzUuMTM1LjIwNy45Ni9TY3JhcGVzL1NILnBocA==' ) )
 if 80 - 80: iI / i1I111II1I
 I11i1ii1 = I1IiI1IIiI ( oOo0 )
 o00o = I1IiI1IIiI ( IIo0o0O0O00oOOo )
 iIIi1i11 = I1IiI1IIiI ( OO0O0 )
 iI1Iii11i1 = I1IiI1IIiI ( o0oo0000 )
 II11iIIii = I1IiI1IIiI ( oOo0OOOOoO )
 oooOo0Ooo0oo = I1IiI1IIiI ( Ii1I1I )
 oOIiiIIi = I1IiI1IIiI ( oOOoOOO0oOoo )
 OoOo0OO0oooo = I1IiI1IIiI ( o0O0ooooooo00 )
 I11II1i1 = I1IiI1IIiI ( I1111ii11IIII )
 IiI1ii11I1 = I1IiI1IIiI ( IiIi1II111I )
 Oo0oO0ooo = xbmcgui . DialogProgress ( )
 if 19 - 19: o00OO00OoO + OoOo00o / O0ooOooooO / OoOoOO00
 if 92 - 92: i1IIi % OOO0OOo + OOO0OOo - iIii1I11I1II1 . iI
 if I11i1ii1 != 'Failed' :
  O0o = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( I11i1ii1 )
  for iIIi1 , I1iI1iIi111i in O0o :
   if IiII111iI1ii1 in I1iI1iIi111i . lower ( ) :
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    II1Ii1iI1i1 ( ( '[COLORgreen]' + I1iI1iIi111i + '- source 1[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( oOo0 + iIIi1 ) , 222 , '' )
    Oo0oO0ooo . update ( 0 , "" , "Getting Source 1 Links" )
 if o00o != 'Failed' :
  IIIIiiIiiI = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( o00o )
  for iIIi1 , I1iI1iIi111i in IIIIiiIiiI :
   if IiII111iI1ii1 in I1iI1iIi111i . lower ( ) :
    II1Ii1iI1i1 ( ( '[COLORgreen]' + I1iI1iIi111i + '- source 2[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( IIo0o0O0O00oOOo + iIIi1 ) , 222 , '' )
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 9 , "" , "Getting Source 2 Links" )
 if iIIi1i11 != 'Failed' :
  O0oOOo0o = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( iIIi1i11 )
  for iIIi1 , I1iI1iIi111i in O0oOOo0o :
   if IiII111iI1ii1 in I1iI1iIi111i . lower ( ) :
    I1I1i1I ( ( '[COLORgreen]' + I1iI1iIi111i + '- source 3[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( OO0O0 + iIIi1 ) , 1006 , '' )
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 18 , "" , "Getting Source 3 Links" )
 if iI1Iii11i1 != 'Failed' :
  o0Ooo0o0Oo = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( iI1Iii11i1 )
  for iIIi1 , I1iI1iIi111i in o0Ooo0o0Oo :
   if IiII111iI1ii1 in I1iI1iIi111i . lower ( ) :
    II1Ii1iI1i1 ( ( '[COLORgreen]' + I1iI1iIi111i + '- source 4[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( o0oo0000 + iIIi1 ) , 222 , '' )
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 27 , "" , "Getting Source 4 Links" )
 if II11iIIii != 'Failed' :
  oo00ooooOOo00 = [ ]
  ii1iOO00Oooo000 = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( II11iIIii )
  for oOo0 , OOO0000oO , OOoOO0ooo , OOo , I1iI1iIi111i in ii1iOO00Oooo000 :
   if IiII111iI1ii1 in I1iI1iIi111i . lower ( ) :
    if I1iI1iIi111i in oo00ooooOOo00 :
     pass
    else :
     IIIIii ( ( '[COLORgreen]' + I1iI1iIi111i + '- source Scooby[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( 'Ganool' , '' ) . replace ( 'ShAaNiG' , '' ) . replace ( 'YIFY' , '' ) . replace ( '[[ Max-Movie.In ]]' , '' ) . replace ( '.mkv' , '' ) . replace ( '.mp4' , '' ) . replace ( '.' , ' ' ) , oOo0 , 1016 , OOO0000oO , OOo , OOoOO0ooo )
     oo00ooooOOo00 . append ( I1iI1iIi111i )
     Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     Oo0oO0ooo . update ( 36 , "" , "Getting Scooby Links" )
     O00Oo000ooO0 ( 'tvshows' , 'Media Info 3' )
 if oooOo0Ooo0oo != 'Failed' :
  iI1ii111iiIii = re . compile ( 'href="(.+?)".+?src="(.+?)" alt="Image of (.+?)"' , re . DOTALL ) . findall ( oooOo0Ooo0oo )
  for oOo0 , OO0ooOOO0OOO , I1iI1iIi111i in iI1ii111iiIii :
   if IiII111iI1ii1 in I1iI1iIi111i . lower ( ) :
    I1I1i1I ( ( '[COLORgreen]' + I1iI1iIi111i + '- source Snag[/COLOR]' ) . replace ( '&#x27;' , '' ) , 'http://www.snagfilms.com' + oOo0 , 7067 , OO0ooOOO0OOO )
    Oo0oO0ooo . update ( 45 , "" , "Getting Snag Links" )
    if 57 - 57: OOooOOo / o00OO00OoO
    O00Oo000ooO0 ( 'tvshows' , 'Media Info 3' )
 if oOIiiIIi != 'Failed' :
  iiIiII = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( oOIiiIIi )
  for oOo0 , OOO0000oO , OOoOO0ooo , OOo , I1iI1iIi111i in iiIiII :
   if IiII111iI1ii1 in I1iI1iIi111i . lower ( ) :
    I1I1IiI1 ( ( '[COLORgreen]' + I1iI1iIi111i + '- source Redemption[/COLOR]' ) , oOo0 , 222 , OOO0000oO , OOo , OOoOO0ooo )
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 53 , "" , "Getting Redemption Links" )
    if 7 - 7: Oo - i1IIi . ii11ii1ii / iIii1I11I1II1 * OOooOOo
    O00Oo000ooO0 ( 'tvshows' , 'Media Info 3' )
 if OoOo0OO0oooo != 'Failed' :
  O0O0O0oO0o0OOOOOO = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( OoOo0OO0oooo )
  for oOo0 , OOO0000oO , OOoOO0ooo , OOo , I1iI1iIi111i in O0O0O0oO0o0OOOOOO :
   if IiII111iI1ii1 in I1iI1iIi111i . lower ( ) :
    I1I1IiI1 ( ( '[COLORgreen]' + I1iI1iIi111i + '- source Reaper[/COLOR]' ) , oOo0 , 222 , OOO0000oO , OOo , OOoOO0ooo )
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 61 , "" , "Getting Reaper Links" )
    if 24 - 24: i1IIi * OoOo00o - Oooo0Ooo000 / iI
    O00Oo000ooO0 ( 'tvshows' , 'Media Info 3' )
 if I11II1i1 != 'Failed' :
  ooooo0 = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( I11II1i1 )
  for oOo0 , OOO0000oO , OOoOO0ooo , OOo , I1iI1iIi111i in ooooo0 :
   if IiII111iI1ii1 in I1iI1iIi111i . lower ( ) :
    I1I1IiI1 ( ( '[COLORgreen]' + I1iI1iIi111i + '- source Herovision[/COLOR]' ) , oOo0 , 222 , OOO0000oO , OOo , OOoOO0ooo )
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 70 , "" , "Getting Herovision Links" )
    if 60 - 60: OOOo0 % O0ooOooooO / OOooOOo % O0ooOooooO * i11iIiiIii / i1I111ii1II1i
    O00Oo000ooO0 ( 'tvshows' , 'Media Info 3' )
    if 34 - 34: o00OO00OoO - i1I111II1I
 if IiI1ii11I1 != 'Failed' :
  IIIiIi1iiI = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( IiI1ii11I1 )
  for oOo0 , OOO0000oO , I1iI1iIi111i in IIIiIi1iiI :
   if IiII111iI1ii1 in I1iI1iIi111i . lower ( ) :
    I1I1i1I ( ( '[COLORgreen]' + I1iI1iIi111i + '- source Silent Hunter[/COLOR]' ) , oOo0 , 222 , OOO0000oO )
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 78 , "" , "Getting Silent Hunter Links" )
    if 15 - 15: ii11ii1ii . i1I111ii1II1i
    O00Oo000ooO0 ( 'tvshows' , 'Media Info 3' )
 o0Iiii = [ '480p' , '720p' , '1080p' , 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' ]
 if 45 - 45: iI / OOO0OOo . OoooooooOO + Ooo00oOo00o
 for I11iiIIII1I1 in o0Iiii :
  i1IIi1i1Ii1 = IIIII + I11iiIIII1I1 + OooO0
  O00oO000Oo0 = O0Oooo0O ( i1IIi1i1Ii1 )
  if O00oO000Oo0 != 'Failed' :
   iIIiiIi = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( O00oO000Oo0 )
   for oOo0 , OOO0000oO , OOoOO0ooo , OOo , I1iI1iIi111i in iIIiiIi :
    if IiII111iI1ii1 in I1iI1iIi111i . lower ( ) :
     I1I1IiI1 ( '[COLORgreen]' + I1iI1iIi111i + ' - Source Pandoras[/COLOR]' , oOo0 , 222 , OOO0000oO , OOo , OOoOO0ooo )
     Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     Oo0oO0ooo . update ( 89 , "" , "Getting Pandoras Links" )
     if 19 - 19: OOooOOo
     O00Oo000ooO0 ( 'tvshows' , 'Media Info 3' )
     if 73 - 73: o00OO00OoO * Oo * I1IiI
 III1i111i = [ '0-9/' , 'A/' , 'B/' , 'C/' , 'D/' , 'E/' , 'F/' , 'G/' , 'H/' , 'I/' , 'J/' , 'K/' , 'L/' , 'M/' , 'N/' , 'O/' , 'P/' , 'R/' , 'S/' , 'T/' , 'U/' , 'V/' , 'W/' , 'X/' , 'Y/' , 'Z/' ]
 if 65 - 65: i11iIiiIii + Oo * OoooooooOO - Ooo00oOo00o
 if 26 - 26: OOooOOo % i1I111II1I + i1I111II1I % Oooo0Ooo000 * i11iIiiIii / i1I111ii1II1i
 for I11iiIIII1I1 in III1i111i :
  i1IIi1i1Ii1 = oOO0oo + I11iiIIII1I1
  OOoO0oO00o = I1IiI1IIiI ( i1IIi1i1Ii1 )
  if II11iIIii != 'Failed' :
   OOO0OoO0oo0OO = re . compile ( '<li><a href="(.+?)"> (.+?)</a></li>' ) . findall ( OOoO0oO00o )
   for iIIi1 , I1iI1iIi111i in OOO0OoO0oo0OO :
    if IiII111iI1ii1 in I1iI1iIi111i . lower ( ) :
     II1Ii1iI1i1 ( ( '[COLORgreen]' + I1iI1iIi111i + 'source 5[/COLOR]' ) . replace ( 'Ganool' , '' ) . replace ( 'ShAaNiG' , '' ) . replace ( 'YIFY' , '' ) . replace ( '[[ Max-Movie.In ]]' , '' ) . replace ( '.mkv' , '' ) . replace ( '.mp4' , '' ) . replace ( '.' , ' ' ) , ( oOO0oo + I11iiIIII1I1 + iIIi1 ) , 222 , '' )
     Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     Oo0oO0ooo . update ( 100 , "" , "Getting Source 5 Links" )
     if 31 - 31: Oooo0Ooo000 * O0ooOooooO . iI
     O00Oo000ooO0 ( 'tvshows' , 'Media Info 3' )
     if 35 - 35: Oooo0Ooo000
     if 94 - 94: OOO0OOo / i11iIiiIii % O0
def O0oO0oo0O ( ) :
 if 82 - 82: OoooooooOO . iI
 IiII111iI1ii1 = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 Ii1I = IiII111iI1ii1 . lower ( )
 o0O0ooooooo00 = ( i1111 ( 'aHR0cDovL2Nvb2x0dnNlcmllcy5jb20vc2VhcmNoLnBocD90YWc9' ) ) + ( IiII111iI1ii1 ) . replace ( ' ' , '+' )
 oOo0 = ( i1111 ( 'aHR0cDovL2RsLmZhcnNpbW92aWUubmV0L1NlcmlhbC8=' ) )
 IIo0o0O0O00oOOo = ( i1111 ( 'aHR0cDovL3N2Mi5kbC1wYXJzLmluLw==' ) )
 OO0O0 = ( i1111 ( 'aHR0cDovL3R2LmRsLXBhcnMuaW4v' ) )
 o0oo0000 = ( i1111 ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9BbWVyaWNhbiUyMFNlcmlhbC8=' ) )
 oOo0OOOOoO = ( i1111 ( 'aHR0cDovL2RpemlsYWIuY29tL2Fyc2l2P2xpbWl0PSZ0dXI9Jm9yZGVyYnk9JnVsa2U9Jm9yZGVyPSZ5aWw9JmRpemlfYWRpPQ==' ) ) + ( IiII111iI1ii1 ) . replace ( ' ' , '+' )
 OoO0Ooo = ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvc2hvd3MvdHZhbGwucGhw' ) )
 Ii1I1I = ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9UaGVfUmVhcGVyL2FsbHR2LnBocA==' ) )
 oOOoOOO0oOoo = ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC90dmZ1bGwucGhw' ) )
 if 26 - 26: O0ooOooooO + OoOo00o - OoOoOO00 . OoOoOO00 + ii11ii1ii + I1IiI
 OoOo0OO0oooo = I1IiI1IIiI ( o0O0ooooooo00 )
 I11i1ii1 = I1IiI1IIiI ( oOo0 )
 o00o = I1IiI1IIiI ( IIo0o0O0O00oOOo )
 iIIi1i11 = I1IiI1IIiI ( OO0O0 )
 iI1Iii11i1 = I1IiI1IIiI ( o0oo0000 )
 II11iIIii = cloudflare . source ( oOo0OOOOoO )
 OOoO0oO00o = I1IiI1IIiI ( OoO0Ooo )
 oooOo0Ooo0oo = I1IiI1IIiI ( Ii1I1I )
 oOIiiIIi = I1IiI1IIiI ( oOOoOOO0oOoo )
 if 68 - 68: O0
 if oOIiiIIi != 'Failed' :
  iiIiII = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( oOIiiIIi )
  for oOo0 , OOO0000oO , OOoOO0ooo , OOo , I1iI1iIi111i in iiIiII :
   if IiII111iI1ii1 in I1iI1iIi111i . lower ( ) :
    IIIIii ( ( '[COLORgreen]' + I1iI1iIi111i + '- source HeroVision[/COLOR]' ) , oOo0 , 1016 , OOO0000oO , OOo , OOoOO0ooo )
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 10 , "" , "Getting Herovision Links" )
    if 76 - 76: ii11ii1ii
    O00Oo000ooO0 ( 'tvshows' , 'Media Info 3' )
    if 99 - 99: OOooOOo
 if oooOo0Ooo0oo != 'Failed' :
  iI1ii111iiIii = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( oooOo0Ooo0oo )
  for oOo0 , OOO0000oO , OOoOO0ooo , OOo , I1iI1iIi111i in iI1ii111iiIii :
   if IiII111iI1ii1 in I1iI1iIi111i . lower ( ) :
    IIIIii ( ( '[COLORgreen]' + I1iI1iIi111i + '- source Reaper[/COLOR]' ) , oOo0 , 1016 , OOO0000oO , OOo , OOoOO0ooo )
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 20 , "" , "Getting Reaper Links" )
    if 1 - 1: iI * I1IiI * Ooo00oOo00o + Oo
    O00Oo000ooO0 ( 'tvshows' , 'Media Info 3' )
    if 90 - 90: o00OO00OoO % Oo - Oo . iIii1I11I1II1 / i1I111II1I + Oooo0Ooo000
 if OoOo0OO0oooo != 'Failed' :
  O0O0O0oO0o0OOOOOO = re . compile ( 'href="([^"]*)"><img src="([^"]*)" alt="([^"]*)"' ) . findall ( OoOo0OO0oooo )
  for oOo0 , OO0ooOOO0OOO , I1iI1iIi111i in O0O0O0oO0o0OOOOOO :
   if IiII111iI1ii1 in I1iI1iIi111i . lower ( ) :
    I1I1i1I ( '[COLORgreen]' + I1iI1iIi111i + ' CoolSeries[/COLOR]' , oOo0 , 7052 , OO0ooOOO0OOO )
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 30 , "" , "Getting CoolSeries Links" )
    if 89 - 89: O0ooOooooO
    O00Oo000ooO0 ( 'tvshows' , 'Media Info 3' )
 if I11i1ii1 != 'Failed' :
  O0o = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( I11i1ii1 )
  for I1iI1iIi111i in O0o :
   if IiII111iI1ii1 in I1iI1iIi111i . lower ( ) :
    I1I1i1I ( '[COLORgreen]' + ( I1iI1iIi111i ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) + ' source 1 [/COLOR]' , ( oOo0 + I1iI1iIi111i ) . replace ( ' ' , '%20' ) , 1006 , '' )
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 40 , "" , "Getting Source 1 Links" )
    if 87 - 87: i1I111ii1II1i % Oo
    O00Oo000ooO0 ( 'tvshows' , 'Media Info 3' )
 if o00o != 'Failed' :
  IIIIiiIiiI = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( o00o )
  for I1iI1iIi111i in IIIIiiIiiI :
   if IiII111iI1ii1 in I1iI1iIi111i . lower ( ) :
    I1I1i1I ( ( I1iI1iIi111i + ' source 2' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( IIo0o0O0O00oOOo + I1iI1iIi111i ) . replace ( ' ' , '%20' ) , 1006 , '' )
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 50 , "" , "Getting Source 2 Links" )
    if 62 - 62: Ooo00oOo00o + OOO0OOo / i1I111ii1II1i * i11iIiiIii
    O00Oo000ooO0 ( 'tvshows' , 'Media Info 3' )
 if iIIi1i11 != 'Failed' :
  O0oOOo0o = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( iIIi1i11 )
  for I1iI1iIi111i in IIIIiiIiiI :
   if IiII111iI1ii1 in I1iI1iIi111i . lower ( ) :
    I1I1i1I ( ( I1iI1iIi111i + ' source 3' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( OO0O0 + I1iI1iIi111i ) . replace ( ' ' , '%20' ) , 1006 , '' )
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 60 , "" , "Getting Source 3 Links" )
    if 37 - 37: i1I111ii1II1i
    O00Oo000ooO0 ( 'tvshows' , 'Media Info 3' )
 if iI1Iii11i1 != 'Failed' :
  o0Ooo0o0Oo = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( iI1Iii11i1 )
  for I1iI1iIi111i in IIIIiiIiiI :
   if IiII111iI1ii1 in I1iI1iIi111i . lower ( ) :
    I1I1i1I ( ( I1iI1iIi111i + ' source 4' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( o0oo0000 + I1iI1iIi111i ) . replace ( ' ' , '%20' ) , 1006 , '' )
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 70 , "" , "Getting Source 4 Links" )
    if 33 - 33: Ooo00oOo00o - O0 - Ooo00oOo00o
    O00Oo000ooO0 ( 'tvshows' , 'Media Info 3' )
 if II11iIIii != 'Failed' :
  ii1iOO00Oooo000 = re . compile ( '<a href="(.+?)" class="film-image">\n<img src="(.+?)" alt=""/>\n</a>\n<div class="tss-detail">\n<a class="title" style="" href=".+?">\n<span class="position">.+?</span>\n(.+?)</a>' ) . findall ( II11iIIii )
  for oOo0 , OO0ooOOO0OOO , I1iI1iIi111i in ii1iOO00Oooo000 :
   if IiII111iI1ii1 in I1iI1iIi111i . lower ( ) :
    I1I1i1I ( '[COLORgreen]' + I1iI1iIi111i + ' - Source - Dizi[/COLOR]' , oOo0 , 8062 , OO0ooOOO0OOO )
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 80 , "" , "Getting Dizi Links" )
    if 94 - 94: OoOo00o * Oooo0Ooo000 * OoooooooOO / OOooOOo . OoOo00o - OOooOOo
    O00Oo000ooO0 ( 'tvshows' , 'Media Info 3' )
 if OOoO0oO00o != 'Failed' :
  OOO0OoO0oo0OO = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( OOoO0oO00o )
  for oOo0 , OOO0000oO , OOoOO0ooo , OOo , I1iI1iIi111i in OOO0OoO0oo0OO :
   if IiII111iI1ii1 in I1iI1iIi111i . lower ( ) :
    IIIIii ( ( '[COLORgreen]' + I1iI1iIi111i + '- Source Scooby[/COLOR]' ) , oOo0 , 1016 , OOO0000oO , OOo , OOoOO0ooo )
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 90 , "" , "Getting Scooby Links" )
    if 13 - 13: i1I111II1I / OoOo00o - Ooo00oOo00o / i1I111II1I . i1IIi
    O00Oo000ooO0 ( 'tvshows' , 'Media Info 3' )
    if 22 - 22: O0 - Oooo0Ooo000 + o00OO00OoO . iI * i1IIi
 iiiI1i1111II = [ 'a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' , 'p' , 'q' , 'r' , 's' , 't' , 'u' , 'v' , 'w' , 'x' , 'y' , 'z' ]
 if 38 - 38: Oo % ii11ii1ii - i1I111ii1II1i * iIii1I11I1II1 / O0
 for I11iiIIII1I1 in iiiI1i1111II :
  i1IIi1i1Ii1 = IIIII + I11iiIIII1I1 + OooO0
  I11II1i1 = O0Oooo0O ( i1IIi1i1Ii1 )
  if I11II1i1 != 'Failed' :
   ooooo0 = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( I11II1i1 )
   for I1iI1iIi111i , OOoOO0ooo , oOo0 , OO0ooOOO0OOO , iI1i111I1Ii , OooOo000OOOOo in ooooo0 :
    if IiII111iI1ii1 in I1iI1iIi111i . lower ( ) :
     IIIIii ( '[COLORgreen]' + I1iI1iIi111i + ' - Source Pandoras[/COLOR]' , oOo0 , OooOo000OOOOo , OO0ooOOO0OOO , iI1i111I1Ii , OOoOO0ooo )
     Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     Oo0oO0ooo . update ( 100 , "" , "Getting Pandoras Links" )
     if 9 - 9: Oooo0Ooo000 * Oo . OOO0OOo * i11iIiiIii - O0
     O00Oo000ooO0 ( 'tvshows' , 'Media Info 3' )
     if 54 - 54: OOOo0 * i1I111II1I + OOooOOo % i1IIi - OOooOOo + I1IiI
     if 15 - 15: I1IiI * O0ooOooooO + i1I111II1I . Oooo0Ooo000 % OOOo0 - OOO0OOo
 xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
def II1I1I1i1i ( ) :
 if 74 - 74: O0 % OoooooooOO * Oo + i1I111II1I * i1I111ii1II1i
 IiII111iI1ii1 = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 Ii1I = IiII111iI1ii1 . lower ( )
 oOo0 = ( i1111 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz' ) )
 I11i1ii1 = O0Oooo0O ( oOo0 )
 O0o = re . compile ( '"id":".+?","name":"(.+?)","img":"(.+?)","stream_url3":".+?","cat_id":"(.+?)","stream_url2":".+?","stream_url":".+?"}' , re . DOTALL ) . findall ( I11i1ii1 )
 for I1iI1iIi111i , OO0ooOOO0OOO , O000OO in O0o :
  I1Ii = i1111 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv' ) + ( OO0ooOOO0OOO ) . replace ( '\\' , '' )
  if IiII111iI1ii1 in I1iI1iIi111i . lower ( ) :
   I1I1i1I ( I1iI1iIi111i , '' , 7022 , I1Ii )
   if 76 - 76: i1I111ii1II1i % I1IiI % iIii1I11I1II1 . i1I111II1I
 xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 30 - 30: i1IIi
 if 75 - 75: Oooo0Ooo000 . i1I111II1I - iIii1I11I1II1 * Ooo00oOo00o * i1I111ii1II1i
def ooo0OO0OOooO0 ( url ) :
 O00O00 = cloudflare . source ( url )
 O0o = re . compile ( '<a class="season" href="(.+?)">\n(.+?)\n</a>\n</span>\n<span>\n<a class="episode" href=".+?">\n(.+?)\n</a>\n</span>\n<span>\n<a class="episode-name" href=".+?">\n(.+?)</a>' ) . findall ( O00O00 )
 for url , oo0oo , iiIi1IIi1I , I1iI1iIi111i in O0o :
  I1I1i1I ( ( oo0oo ) . replace ( 'Sezon' , ' Season ' ) + ( iiIi1IIi1I ) . replace ( 'Bölüm' , ' Episode ' ) + I1iI1iIi111i , url , 8063 , '' )
  if 66 - 66: Oo - iIii1I11I1II1
  if 9 - 9: OOooOOo % ii11ii1ii . ii11ii1ii
  if 28 - 28: OoooooooOO % O0ooOooooO + ii11ii1ii + O0 . o00OO00OoO
  if 80 - 80: i11iIiiIii % ii11ii1ii
def OOO00o0 ( url ) :
 O00O00 = cloudflare . source ( url )
 O0o = re . compile ( 'file: "(.+?)",.+?label: "(.+?)",' , re . DOTALL ) . findall ( O00O00 )
 for url , I1iI1iIi111i in O0o :
  II1Ii1iI1i1 ( I1iI1iIi111i , url , 222 , '' )
  if 97 - 97: ii11ii1ii / ii11ii1ii / iIii1I11I1II1 % i1IIi . ii11ii1ii . OoOo00o
  if 4 - 4: Oo - Ooo00oOo00o - i11iIiiIii * o00OO00OoO / iI - i1I111II1I
  if 45 - 45: OOooOOo % Oo * i1IIi - O0
  if 82 - 82: OoOoOO00 / i1I111ii1II1i
def OOoO ( ) :
 if 8 - 8: o00OO00OoO + Ooo00oOo00o
 O00O00 = cloudflare . source ( i1111 ( 'aHR0cDovL2RpemlsYWIuY29t' ) )
 O0o = re . compile ( '<li id=".+?">.+?<a href="(.+?)">.+?<img width="40" height="40" src="(.+?)" alt=""/>.+?<span class="title">\n(.+?)</span>.+?<span class="alt-title">\n(.+?)</span>.+?</a>.+?</li>' , re . DOTALL ) . findall ( O00O00 )
 for oOo0 , OO0ooOOO0OOO , I1iI1iIi111i , iiIi1IIi1I in O0o :
  I1I1i1I ( I1iI1iIi111i + '  -  ' + ( iiIi1IIi1I ) . replace ( 'sezon' , 'Season' ) . replace ( 'bölüm' , 'Episode' ) , oOo0 , 8063 , OO0ooOOO0OOO )
  if 9 - 9: i1I111II1I + OOooOOo
def I1iII1IIi1IiI ( ) :
 OO0oo = Iii1 ( i1111 ( 'aHR0cDovL3d3dy50dmd1aWRlLmNvLnVrLw==' ) )
 O0o = re . compile ( '<a href="(.+?)"  qt-title=".+?" qt-text=".+?<br> .+?" title="(.+?)".+?class=".+? src="(.+?)" alt=".+?" /></a>' , re . DOTALL ) . findall ( OO0oo )
 for oOo0 , I1iI1iIi111i , OO0ooOOO0OOO in O0o :
  II1Ii1iI1i1 ( '[COLORgreen]' + I1iI1iIi111i + '[/COLOR]' , oOo0 , 8002 , OO0ooOOO0OOO )
def iIioo0ooO ( url ) :
 OO0oo = Iii1 ( url )
 O0o = re . compile ( '<table border="0".+?url((.+?));background-repeat: no-repeat;">.+?<tr>.+?<span class="season">(.+?)</span><br>.+?<a href="(.+?)"+?>(.+?)</span><br>.+?<span class="programmetext">(.+?)</span></a><br>' , re . DOTALL ) . findall ( OO0oo )
 for OO0ooOOO0OOO , time , url , I1iI1iIi111i , Ii1IIi in O0o :
  IIIIii ( '%s %s' % ( '[COLORgreen]' + I1iI1iIi111i + '[/COLOR]' , time ) , url , 1015 , OO0ooOOO0OOO , Ii1IIi )
  if 97 - 97: o00OO00OoO . Oooo0Ooo000 / OOOo0
def o00OO0o0 ( ) :
 if 39 - 39: OOO0OOo % ii11ii1ii - i1I111ii1II1i
 I1I1i1I ( 'Coronation Street' , '' , 8001 , '' )
 I1I1i1I ( 'Eastenders' , '' , 8002 , '' )
 I1I1i1I ( 'Emmerdale' , '' , 8003 , '' )
 I1I1i1I ( 'Hollyoaks' , '' , 8004 , '' )
 I1I1i1I ( 'Im a Celebrity' , '' , 8005 , '' )
 if 48 - 48: i11iIiiIii
 if 52 - 52: iIii1I11I1II1
 if 38 - 38: Oooo0Ooo000 . Oooo0Ooo000 * O0ooOooooO / OoooooooOO % OOO0OOo
 if 80 - 80: Ooo00oOo00o / OoOo00o * OOOo0 % OoOo00o
def ooo00 ( ) :
 I11i1ii1 = O0Oooo0O ( 'http://uksoapshare.blogspot.co.uk/' )
 O0o = re . compile ( '<a href="(.+?)".+?target=_blank>(.+?)</a>' ) . findall ( I11i1ii1 )
 for oOo0 , I1iI1iIi111i in O0o :
  if 'Holly' in I1iI1iIi111i :
   OO0ooOOO0OOO = 'http://2.bp.blogspot.com/-9c7Sieh1RKs/UjD6TGAEEnI/AAAAAAAAAC8/84uwHfxcuYg/s1600/Hollyoaks.png'
   if 'huge' in oOo0 :
    II1Ii1iI1i1 ( ( I1iI1iIi111i ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , oOo0 . replace ( '\\/' , '/' ) , 8006 , OO0ooOOO0OOO )
   else :
    pass
    if 17 - 17: Oooo0Ooo000
 xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE_IGNORE_THE ) ;
 if 56 - 56: OOO0OOo * OOooOOo + Oooo0Ooo000
def I11II11111i11 ( ) :
 I11i1ii1 = O0Oooo0O ( 'http://uksoapshare.blogspot.co.uk/' )
 O0o = re . compile ( '<a href="(.+?)".+?target=_blank>(.+?)</a>' ) . findall ( I11i1ii1 )
 for oOo0 , I1iI1iIi111i in O0o :
  if 'East' in I1iI1iIi111i :
   OO0ooOOO0OOO = 'http://3.bp.blogspot.com/-KWHcNbNJU8Y/Vi1ousRl7fI/AAAAAAAAAT8/ksNE12LH0nE/s1600/eastenders.jpg'
   if 'huge' in oOo0 :
    II1Ii1iI1i1 ( ( I1iI1iIi111i ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , oOo0 . replace ( '\\/' , '/' ) , 8006 , OO0ooOOO0OOO )
   else :
    pass
    if 83 - 83: O0ooOooooO - OOO0OOo - OoOo00o % i1IIi - i1I111ii1II1i . OOooOOo
 xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 96 - 96: Oo + o00OO00OoO . i1IIi
def OooIii1I1iI ( ) :
 I11i1ii1 = O0Oooo0O ( 'http://uksoapshare.blogspot.co.uk/' )
 O0o = re . compile ( '<a href="(.+?)".+?target=_blank>(.+?)</a>' ) . findall ( I11i1ii1 )
 for oOo0 , I1iI1iIi111i in O0o :
  if 'Emmer' in I1iI1iIi111i :
   OO0ooOOO0OOO = 'http://2.bp.blogspot.com/-UfDcxisVV5c/UjH9vUicZ3I/AAAAAAAAADc/8Ozuiz1ojxw/s1600/Emmerdale.jpg'
   if 'huge' in oOo0 :
    II1Ii1iI1i1 ( ( I1iI1iIi111i ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , oOo0 . replace ( '\\/' , '/' ) , 8006 , OO0ooOOO0OOO )
   else :
    pass
    if 62 - 62: O0ooOooooO + Oo / i11iIiiIii
 xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 90 - 90: iIii1I11I1II1 + I1IiI
def IiI ( ) :
 I11i1ii1 = O0Oooo0O ( 'http://uksoapshare.blogspot.co.uk/' )
 O0o = re . compile ( '<a href="(.+?)".+?target=_blank>(.+?)</a>' ) . findall ( I11i1ii1 )
 for oOo0 , I1iI1iIi111i in O0o :
  if 'Coro' in I1iI1iIi111i :
   OO0ooOOO0OOO = 'http://3.bp.blogspot.com/-hofvfBQVexs/UjErIfNdS4I/AAAAAAAAADQ/Q-vVGu3apYU/s1600/corrie.jpg'
   if 'huge' in oOo0 :
    II1Ii1iI1i1 ( ( I1iI1iIi111i ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , oOo0 . replace ( '\\/' , '/' ) , 8006 , OO0ooOOO0OOO )
   else :
    pass
    if 16 - 16: Oo / Ooo00oOo00o / i1I111ii1II1i / iIii1I11I1II1
 xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 44 - 44: Oo . Oo + OoooooooOO * i11iIiiIii / Oooo0Ooo000 + o00OO00OoO
def iIiII11 ( ) :
 I11i1ii1 = O0Oooo0O ( 'http://uksoapshare.blogspot.co.uk/' )
 O0o = re . compile ( '<a href="(.+?)" target="_blank">(.+?)</a>' ) . findall ( I11i1ii1 )
 for oOo0 , I1iI1iIi111i in O0o :
  if 'Celeb' in I1iI1iIi111i :
   OO0ooOOO0OOO = 'http://3.bp.blogspot.com/-a_yDotWU_pY/VkotKWaG_gI/AAAAAAAAAUk/8Q5iNM6p37k/s1600/iacgoh.jpg'
   if 'huge' in oOo0 :
    II1Ii1iI1i1 ( ( I1iI1iIi111i ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , oOo0 . replace ( '\\/' , '/' ) , 8006 , OO0ooOOO0OOO )
   else :
    pass
    if 33 - 33: OOooOOo * i1I111ii1II1i * iIii1I11I1II1 + i11iIiiIii . OoooooooOO
def O0O0oO0oo ( name , url ) :
 o00o0o000Oo = urlresolver . HostedMediaFile ( url ) . valid_url ( )
 if o00o0o000Oo :
  Oooo00OOo = urlresolver . HostedMediaFile ( url ) . resolve ( )
 else :
  OO0oo = open_url ( url )
  url = re . compile ( 'src="(.+?)"></iframe>' ) . findall ( OO0oo ) [ 0 ]
  url = url . split ( '?autoplay' ) [ 0 ]
  OO0oo = open_url ( url )
  iIiII = re . compile ( 'mp4","url":"(.+?)"' ) . findall ( OO0oo ) [ - 1 ]
  Oooo00OOo = iIiII . replace ( '\\/' , '/' )
 oOO0o0oo0 = xbmcgui . ListItem ( name , '' , '' )
 oOO0o0oo0 . setPath ( Oooo00OOo )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , oOO0o0oo0 )
 if 51 - 51: OoOoOO00 / Oo / OOOo0 + i11iIiiIii
 if 5 - 5: Oooo0Ooo000
def iii1IiiiI1i1 ( ) :
 OO0oo = O0Oooo0O ( i1111 ( 'aHR0cDovL3d3dy5kaXppYm94aGQuY29tLw==' ) )
 O0o = re . compile ( 'class="film menu-item menu-item-type-post_type menu-item-object-page menu-item-36980"><a href="(.+?)"><i class="fa fa-film"></i><span>(.+?)</span></a></li>' ) . findall ( OO0oo )
 IIIIiiIiiI = re . compile ( 'class="menu-item menu-item-type-post_type menu-item-object-page menu-item-52949"><a href="(.+?)"><i class="fa fa-"></i><span>(.+?)</span></a></li>' ) . findall ( OO0oo )
 for oOo0 , I1iI1iIi111i in O0o :
  I1I1i1I ( ( '[COLORgreen]' + I1iI1iIi111i + '[/COLOR]' ) . replace ( 'Diziler' , 'Series' ) , oOo0 , 7071 , ii11iIi1I + 'popcorn.png' )
 for oOo0 , I1iI1iIi111i in IIIIiiIiiI :
  I1I1i1I ( ( '[COLORgreen]' + I1iI1iIi111i + '[/COLOR]' ) . replace ( 'Filmler' , 'Movies' ) , oOo0 , 7071 , ii11iIi1I + 'popcorn.png' )
  if 37 - 37: Oo - i1IIi - OoOo00o + Oooo0Ooo000 . iIii1I11I1II1
def Oo00oOO00 ( ) :
 OO0oo = O0Oooo0O ( i1111 ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL2NhdGVnb3JpZXMv' ) )
 O0o = re . compile ( '<a class="nav-item" href="(.+?)">(.+?)</a>' ) . findall ( OO0oo )
 for oOo0 , I1iI1iIi111i in O0o :
  if 'Movies' in I1iI1iIi111i :
   I1I1i1I ( '[COLORgreen]' + I1iI1iIi111i + '[/COLOR]' , 'http://www.snagfilms.com' + ( oOo0 ) . replace ( 'http://www.snagfilms.com' , '' ) , 7061 , ii11iIi1I + 'popcorn.png' )
def Iio0000O00oO0O ( url ) :
 OO0oo = O0Oooo0O ( url )
 O0o = re . compile ( '<a class="object-link size-poster".+?href="(.+?)" data-type="category">.+?src="(.+?)" alt="Image of (.+?)" />' , re . DOTALL ) . findall ( OO0oo )
 O0o = re . compile ( '<a class="object-link size-poster".+?href="(.+?)" data-type="category">.+?src="(.+?)" alt="Image of (.+?)" />' , re . DOTALL ) . findall ( OO0oo )
 IIIIiiIiiI = re . compile ( "<li class='current'>.+?</li><li ><a href='(.+?)'>.+?</a></li><li" , re . DOTALL ) . findall ( OO0oo )
 for url , OO0ooOOO0OOO , I1iI1iIi111i in O0o :
  I1I1i1I ( '[COLORgreen]' + I1iI1iIi111i + '[/COLOR]' , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7067 , OO0ooOOO0OOO )
 for url in IIIIiiIiiI :
  I1I1i1I ( '[COLORgreen]NEXT PAGE[/COLOR]' , ( url ) . replace ( '&#038;' , '&' ) , 7063 , ii11iIi1I + 'Next.png' )
  if 3 - 3: iIii1I11I1II1 % ii11ii1ii . i1I111II1I % Oooo0Ooo000
  if 40 - 40: OOO0OOo * iI . iI + OoOoOO00 + OoooooooOO
def i11I1Iii1I ( url ) :
 OO0oo = O0Oooo0O ( i1111 ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL2NhdGVnb3JpZXMv' ) )
 O0o = re . compile ( '<a class="object-link size-poster".+?href="(.+?)" data-type="category">.+?src="(.+?)" alt="Image of (.+?)" />' , re . DOTALL ) . findall ( OO0oo )
 for url , OO0ooOOO0OOO , I1iI1iIi111i in O0o :
  I1I1i1I ( '[COLORgreen]' + I1iI1iIi111i + '[/COLOR]' , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7062 , OO0ooOOO0OOO )
  if 18 - 18: i1IIi
  if 4 - 4: OoOo00o
def oOo0OoOOOo0 ( url ) :
 OO0oo = O0Oooo0O ( url )
 O0o = re . compile ( 'href="(.+?)".+?src="(.+?)" alt="Image of (.+?)"' , re . DOTALL ) . findall ( OO0oo )
 for url , OO0ooOOO0OOO , I1iI1iIi111i in O0o :
  I1I1i1I ( ( '[COLORgreen]' + I1iI1iIi111i + '[/COLOR]' ) . replace ( '&#x27;' , '' ) , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7067 , OO0ooOOO0OOO )
  if 55 - 55: O0ooOooooO + O0 / i1I111ii1II1i % OOO0OOo / OoooooooOO
def O00o0OO0OO0oo ( url ) :
 OO0oo = O0Oooo0O ( url )
 O0o = re . compile ( '<div class="film-container">.+?<iframe src="(.+?)"' , re . DOTALL ) . findall ( OO0oo )
 for url in O0o :
  Ooo0O0ooo0o ( 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) )
  if 50 - 50: i11iIiiIii - OoooooooOO . O0ooOooooO + O0 . i1IIi
def Ooo0O0ooo0o ( url ) :
 OO0oo = O0Oooo0O ( url )
 O0o = re . compile ( 'file: "(.+?)",.+?label: "(.+?)"' , re . DOTALL ) . findall ( OO0oo )
 for url , I1iI1iIi111i in O0o :
  II1Ii1iI1i1 ( '[COLORgreen]' + I1iI1iIi111i + '[/COLOR]' , url , 222 , ii11iIi1I + 'popcorn.png' )
  if 91 - 91: OOooOOo . i1I111ii1II1i % Oo - i1I111ii1II1i . O0ooOooooO % i11iIiiIii
  if 25 - 25: iIii1I11I1II1
  if 63 - 63: OOO0OOo
  if 96 - 96: Oooo0Ooo000
def IIII ( url ) :
 OO0oo = O0Oooo0O ( url )
 O0o = re . compile ( '</h4><p><ul><li><a href="([^"]*)">(.+?)<.+?class=' ) . findall ( OO0oo )
 IIIIiiIiiI = re . compile ( '<li><a href="([^"]*)">(.+?)<.+?class=' ) . findall ( OO0oo )
 for url , I1iI1iIi111i in O0o :
  if '(cooltvseries.com)' in I1iI1iIi111i :
   II1Ii1iI1i1 ( ( '[COLORgreen]' + I1iI1iIi111i + ' -(360)-[/COLOR]' ) . replace ( ' - (cooltvseries.com).mp4' , '' ) , url , 7053 , ii11iIi1I + 'CoolSeries.png' )
 for url , I1iI1iIi111i in IIIIiiIiiI :
  if '(cooltvseries.com)' in I1iI1iIi111i :
   II1Ii1iI1i1 ( ( '[COLORgreen]' + I1iI1iIi111i + '[/COLOR]' ) . replace ( ' - (cooltvseries.com).mp4' , '' ) , url , 7053 , ii11iIi1I + 'CoolSeries.png' )
def ii1oooO0o0oOoO ( url ) :
 OO0oo = O0Oooo0O ( url )
 O0o = re . compile ( '<source type="video/mp4" src="([^"]*)"/>' ) . findall ( OO0oo )
 for url in O0o :
  OO0ooo0o0 ( ( url ) . replace ( ' ' , '%20' ) )
  if 23 - 23: OoOo00o + iIii1I11I1II1 % iIii1I11I1II1 / OOO0OOo . O0ooOooooO + iIii1I11I1II1
  if 93 - 93: O0ooOooooO * OOooOOo / i1I111II1I - i1I111II1I . i1I111ii1II1i / OOOo0
def I111ii1iI ( ) :
 OO0oo = O0Oooo0O ( i1111 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vc2VjcmV0L2Nsb3VkLnBocA==' ) )
 O0o = re . compile ( '<li class="col-sm-2">.+?<a href="#" class="thumbnail" data-src="(.+?)" data-toggle="modal".+?data-target="#infoModal" name="(.+?)"> <img src="(.+?)" alt=".+?" width="130px"' , re . DOTALL ) . findall ( OO0oo )
 for oOo0 , I1iI1iIi111i , OO0ooOOO0OOO in O0o :
  II1Ii1iI1i1 ( '[COLORgreen]' + I1iI1iIi111i + '[/COLOR]' , 'http://stream.cloudtv.bz/stream/channel/20/' + ( i1111 ( oOo0 ) ) , 222 , OO0ooOOO0OOO )
  if 33 - 33: iI % O0 + ii11ii1ii
def o0o ( url ) :
 OO0oo = O0Oooo0O ( url )
 O0o = re . compile ( 'src="([^"]*)".+?alt=""></a><div class="entry unvoted"><p class="title"><a class="title may-blank " href="([^"]*)" tabindex=.+?>(.+?)</a>' , re . DOTALL ) . findall ( OO0oo )
 next = re . compile ( '<a href="([^"]*)" rel="nofollow next"' , re . DOTALL ) . findall ( OO0oo )
 for OO0ooOOO0OOO , url , I1iI1iIi111i in O0o :
  if 'youtu' in url :
   II1Ii1iI1i1 ( ( '[COLORgreen]' + I1iI1iIi111i + '[/COLOR]' ) . replace ( '&quot;' , '"' ) . replace ( '&amp;' , ' & ' ) , url , 7051 , 'http:' + OO0ooOOO0OOO )
 for url in next :
  I1I1i1I ( '[COLORgreen]NEXT[/COLOR]' , url , 7050 , ii11iIi1I + 'Next.png' )
  if 39 - 39: i1I111II1I + Ooo00oOo00o
def oOoOOOO0OOO ( url ) :
 OO0oo = O0Oooo0O ( url )
 O0o = re . compile ( 'rel="shortlink" href="([^"]*)">' , re . DOTALL ) . findall ( OO0oo )
 for url in O0o :
  yt . PlayVideo ( ( url ) . replace ( 'https://youtu.be/' , '' ) )
  if 58 - 58: Oooo0Ooo000 % i11iIiiIii / i11iIiiIii * OOO0OOo - o00OO00OoO
def i11ii111i1ii ( url ) :
 OO0oo = O0Oooo0O
 O0o = re . compile ( 'id:"(.+?)",url:"(.+?)"' , re . DOTALL ) . findall ( OO0oo )
 for url , OO0ooOOO0OOO , I1iI1iIi111i in O0o :
  I1I1i1I ( '[COLORgreen]' + I1iI1iIi111i + '[/COLOR]' , url , 222 , OO0ooOOO0OOO )
  if 97 - 97: i11iIiiIii + Oo * i1I111II1I % i1I111ii1II1i . OoOo00o
  if 4 - 4: O0 . i1I111ii1II1i - iIii1I11I1II1
  if 19 - 19: i1I111II1I % Ooo00oOo00o / iI + OoOoOO00 % OoooooooOO
  if 89 - 89: iI
  if 51 - 51: i1I111ii1II1i
def O00O0Oo0 ( ) :
 if 53 - 53: i1IIi . i1IIi - Oooo0Ooo000 / i1I111ii1II1i - I1IiI % OOOo0
 I1I1i1I ( 'All Channels' , '' , 7021 , ii11iIi1I + 'livetv.png' )
 I1I1i1I ( 'Entertainment' , '' , 7021 , ii11iIi1I + 'livetv.png' )
 I1I1i1I ( 'Movies' , '' , 7021 , ii11iIi1I + 'livetv.png' )
 I1I1i1I ( 'Music' , '' , 7021 , ii11iIi1I + 'livetv.png' )
 I1I1i1I ( 'News' , '' , 7021 , ii11iIi1I + 'livetv.png' )
 I1I1i1I ( 'Sports' , '' , 7021 , ii11iIi1I + 'livetv.png' )
 I1I1i1I ( 'Documentary' , '' , 7021 , ii11iIi1I + 'livetv.png' )
 I1I1i1I ( 'Kids' , '' , 7021 , ii11iIi1I + 'livetv.png' )
 I1I1i1I ( 'Food' , '' , 7021 , ii11iIi1I + 'livetv.png' )
 I1I1i1I ( 'Religious' , '' , 7021 , ii11iIi1I + 'livetv.png' )
 I1I1i1I ( 'USA Channels' , '' , 7021 , ii11iIi1I + 'livetv.png' )
 I1I1i1I ( 'Other' , '' , 7021 , ii11iIi1I + 'livetv.png' )
 if 65 - 65: i1I111ii1II1i . OoooooooOO - O0 . i1I111ii1II1i - i11iIiiIii
 if 29 - 29: ii11ii1ii . OOOo0 % O0ooOooooO - i11iIiiIii
def II1ii1iI ( Cat_Name ) :
 if 29 - 29: iI / OOO0OOo % Oooo0Ooo000
 ii1iIII1ii = False
 I11Oo0O0O0O0OO = '0'
 if Cat_Name == 'All Channels' : ii1iIII1ii = True
 if Cat_Name == 'Entertainment' : I11Oo0O0O0O0OO = '1'
 if Cat_Name == 'Movies' : I11Oo0O0O0O0OO = '2'
 if Cat_Name == 'Music' : I11Oo0O0O0O0OO = '3'
 if Cat_Name == 'News' : I11Oo0O0O0O0OO = '4'
 if Cat_Name == 'Sports' : I11Oo0O0O0O0OO = '5'
 if Cat_Name == 'Documentary' : I11Oo0O0O0O0OO = '6'
 if Cat_Name == 'Kids' : I11Oo0O0O0O0OO = '7'
 if Cat_Name == 'Food' : I11Oo0O0O0O0OO = '8'
 if Cat_Name == 'Religious' : I11Oo0O0O0O0OO = '9'
 if Cat_Name == 'USA Channels' : I11Oo0O0O0O0OO = '10'
 if Cat_Name == 'Other' : I11Oo0O0O0O0OO = '11'
 if 86 - 86: iI * i1IIi + O0ooOooooO
 OO0oo = O0Oooo0O ( i1111 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz' ) )
 O0o = re . compile ( '"id":".+?","name":"(.+?)","img":"(.+?)","stream_url3":".+?","cat_id":"(.+?)","stream_url2":".+?","stream_url":".+?"}' , re . DOTALL ) . findall ( OO0oo )
 print 'Len Match: >>>' + str ( len ( O0o ) )
 for I1iI1iIi111i , OO0ooOOO0OOO , O000OO in O0o :
  I1Ii = i1111 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv' ) + ( OO0ooOOO0OOO ) . replace ( '\\' , '' )
  if O000OO == I11Oo0O0O0O0OO :
   I1I1i1I ( I1iI1iIi111i , '' , 7022 , I1Ii )
  elif ii1iIII1ii == True :
   I1I1i1I ( I1iI1iIi111i , '' , 7022 , I1Ii )
  else : pass
  if 8 - 8: O0ooOooooO
  xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 50 - 50: OoOo00o . OOO0OOo - O0 % OOOo0 . o00OO00OoO
def iii1iI ( Search_Name ) :
 OO0oo = O0Oooo0O ( i1111 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz' ) )
 O0o = re . compile ( '"id":".+?","name":"' + Search_Name + '","img":"(.+?)","stream_url3":"(.+?)","cat_id":".+?","stream_url2":"(.+?)","stream_url":"(.+?)"}' , re . DOTALL ) . findall ( OO0oo )
 O0o = re . compile ( '"id":".+?","name":"' + Search_Name + '","img":"(.+?)","stream_url3":"(.+?)","cat_id":".+?","stream_url2":"(.+?)","stream_url":"(.+?)"}' , re . DOTALL ) . findall ( OO0oo )
 for OO0ooOOO0OOO , oOo0 , IIo0o0O0O00oOOo , OO0O0 in O0o :
  I1Ii = i1111 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv' ) + ( OO0ooOOO0OOO ) . replace ( '\\' , '' )
  II1Ii1iI1i1 ( Search_Name + ': Link 1' , ( oOo0 ) . replace ( '\\' , '' ) , 222 , I1Ii )
  II1Ii1iI1i1 ( Search_Name + ': Link 2' , ( IIo0o0O0O00oOOo ) . replace ( '\\' , '' ) , 222 , I1Ii )
  II1Ii1iI1i1 ( Search_Name + ': Link 3' , ( OO0O0 ) . replace ( '\\' , '' ) , 222 , I1Ii )
  if 26 - 26: iIii1I11I1II1 - ii11ii1ii . OoOo00o . OoOo00o + iIii1I11I1II1 * Oo
def O0Oo00 ( ) :
 OO0oo = O0Oooo0O ( i1111 ( oo ( 0 , [ 97 ] , [ 221 , 72 , 245 , 82 , 68 , 48 , 242 , 99 , 143 , 68 , 9 , 111 , 24 , 118 , 180 , 76 , 29 , 51 , 14 , 100 , 187 , 51 , 105 , 100 , 106 , 121 , 52 , 53 , 240 , 114 , 26 , 98 , 252 , 50 , 197 , 82 , 218 , 112 , 19 , 99 , 94 , 71 , 54 , 120 , 104 , 108 , 174 , 101 , 107 , 72 , 168 , 82 , 191 , 50 , 88 , 76 , 90 , 109 , 138 , 78 , 24 , 118 , 89 , 76 , 218 , 110 , 231 , 86 , 105 , 114 , 252 , 76 , 37 , 50 , 36 , 82 , 96 , 118 , 27 , 100 , 120 , 50 , 160 , 53 , 72 , 115 , 200 , 98 , 80 , 50 , 201 , 70 , 114 , 107 , 9 , 99 , 113 , 121 , 127 , 57 , 155 , 106 , 213 , 97 , 194 , 71 , 192 , 70 , 162 , 116 , 27 , 99 , 46 , 71 , 191 , 108 , 4 , 118 , 24 , 98 , 27 , 109 , 105 , 108 , 89 , 119 , 164 , 100 , 88 , 72 , 237 , 89 , 93 , 117 , 40 , 98 , 211 , 84 , 75 , 78 , 216 , 49 ] ) ) )
 O0o = re . compile ( '#EXTINF:-1,(.+)\s*(.+)\s*' ) . findall ( OO0oo )
 for I1iI1iIi111i , oOo0 in O0o :
  II1Ii1iI1i1 ( I1iI1iIi111i , ( oOo0 ) . replace ( '"' , ' ' ) . replace ( '&amp;' , '&' ) . strip ( ) + '|connection=keep-alive' , 222 , ii11iIi1I + 'english.png' )
def Oo0o0ooOoO ( ) :
 OO0oo = O0Oooo0O ( i1111 ( oo ( 0 , [ 97 ] , [ 221 , 72 , 245 , 82 , 68 , 48 , 242 , 99 , 143 , 68 , 9 , 111 , 24 , 118 , 180 , 76 , 29 , 51 , 14 , 100 , 187 , 51 , 105 , 100 , 106 , 121 , 52 , 53 , 240 , 114 , 26 , 98 , 252 , 50 , 197 , 82 , 218 , 112 , 19 , 99 , 94 , 71 , 54 , 120 , 104 , 108 , 174 , 101 , 107 , 72 , 168 , 82 , 191 , 50 , 88 , 76 , 90 , 109 , 138 , 78 , 24 , 118 , 89 , 76 , 218 , 110 , 231 , 86 , 105 , 114 , 252 , 76 , 37 , 50 , 36 , 82 , 96 , 118 , 27 , 100 , 120 , 50 , 160 , 53 , 72 , 115 , 200 , 98 , 80 , 50 , 201 , 70 , 114 , 107 , 9 , 99 , 113 , 121 , 127 , 57 , 155 , 106 , 213 , 97 , 194 , 71 , 192 , 70 , 162 , 116 , 27 , 99 , 46 , 71 , 191 , 108 , 4 , 118 , 24 , 98 , 27 , 109 , 105 , 108 , 89 , 119 , 164 , 100 , 88 , 72 , 237 , 89 , 93 , 117 , 40 , 98 , 211 , 84 , 75 , 78 , 216 , 49 ] ) ) )
 O0o = re . compile ( '#EXTINF:-2,(.+)\s*(.+)\s*' ) . findall ( OO0oo )
 for I1iI1iIi111i , oOo0 in O0o :
  II1Ii1iI1i1 ( I1iI1iIi111i , ( oOo0 ) . replace ( '"' , ' ' ) . replace ( '&amp;' , '&' ) . strip ( ) , 222 , ii11iIi1I + 'xxx.png' )
def iI1Ii11 ( ) :
 OO0oo = O0Oooo0O ( i1111 ( oo ( 0 , [ 97 , 129 , 72 , 149 , 82 , 100 , 48 , 63 , 99 , 170 , 68 , 159 , 111 , 42 , 118 , 83 , 76 , 128 , 51 , 61 , 100 , 44 , 51 , 201 , 100 , 148 , 121 , 134 , 53 ] , [ 159 , 114 , 70 , 98 , 144 , 50 , 37 , 82 , 253 , 112 , 184 , 99 , 50 , 71 , 154 , 120 , 110 , 108 , 179 , 101 , 250 , 72 , 65 , 82 , 125 , 50 , 52 , 76 , 28 , 109 , 124 , 78 , 191 , 118 , 193 , 76 , 193 , 110 , 145 , 86 , 92 , 114 , 193 , 76 , 41 , 50 , 82 , 82 , 206 , 118 , 32 , 100 , 163 , 50 , 209 , 53 , 191 , 115 , 42 , 98 , 30 , 50 , 237 , 70 , 26 , 107 , 70 , 99 , 64 , 121 , 115 , 57 , 230 , 116 , 32 , 97 , 39 , 88 , 58 , 104 , 38 , 50 , 77 , 98 , 185 , 50 , 86 , 81 , 80 , 117 , 111 , 98 , 226 , 84 , 75 , 78 , 210 , 49 ] ) ) )
 O0o = re . compile ( '#EXTINF:.+?,(.+)\s*(.+)\s*' ) . findall ( OO0oo )
 for I1iI1iIi111i , oOo0 in O0o :
  II1Ii1iI1i1 ( I1iI1iIi111i , ( oOo0 ) . replace ( '"' , ' ' ) . replace ( '&amp;' , '&' ) . strip ( ) , 222 , ii11iIi1I + 'vod(1).png' )
  if 93 - 93: OOOo0 / OOO0OOo / Oooo0Ooo000 + OoOoOO00 + i11iIiiIii
def iiiII1III ( url ) :
 url
 I1iIiiIi11I1i = xbmcgui . ListItem ( I1iI1iIi111i , path = url )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , I1iIiiIi11I1i )
 return
 if 84 - 84: o00OO00OoO
 if 35 - 35: OOOo0 . I1IiI + OoooooooOO % Oo % i1I111II1I
def iIi1Ii1111i ( url ) :
 OO0oo = O0Oooo0O ( url )
 O0o = re . compile ( '<a class=.+?href="(.+?)">.+?<div class="videothumboverlay hidden-xs" id=".+?">(.+?)</div>.+?<div class="videothumbbox"><img src="(.+?)" class="videothumb" alt="(.+?)"></div>' , re . DOTALL ) . findall ( OO0oo )
 IIIIiiIiiI = re . compile ( "<a href='(.+?)' class='paginationnext'>Next &raquo;</a></div>" ) . findall ( OO0oo )
 for url , OOoOO0ooo , OO0ooOOO0OOO , I1iI1iIi111i in O0o :
  IIIIii ( I1iI1iIi111i , 'https://www.fitnessblender.com' + url , 7086 , 'https://www.fitnessblender.com' + OO0ooOOO0OOO , '' , ( OOoOO0ooo ) . replace ( '</p>' , ' ' ) . replace ( '<p>' , ' ' ) )
  O00Oo000ooO0 ( 'tvshows' , 'Media Info 3' )
 for url in IIIIiiIiiI :
  I1I1i1I ( 'NEXT' , 'https://www.fitnessblender.com' + url , 7085 , ii11iIi1I + 'Next.png' )
  if 16 - 16: OoOo00o . OOO0OOo . Ooo00oOo00o
def o0oO0oo ( url ) :
 I11i1ii1 = O0Oooo0O ( url )
 O0o = re . compile ( '<div class=\'videowrapper\'><iframe width="700" height="394" src="//www.youtube.com/embed/(.+?)?rel=0&amp;wmode=transparent" frameborder="0"></iframe></div>.+?<div class="col-xs-6 col-md-2 rightborder">(.+?)</div>.+?<p class="videodetailvalue"><img src=\'(.+?)\'/></p>' , re . DOTALL ) . findall ( I11i1ii1 )
 for url , OOoOO0ooo , OO0ooOOO0OOO in O0o :
  I1I1IiI1 ( 'PLAY' , url , 8043 , 'https://www.fitnessblender.com' + OO0ooOOO0OOO , '' , OOoOO0ooo )
  O00Oo000ooO0 ( 'tvshows' , 'Media Info 3' )
 IiiIIIiI1ii = re . compile ( '<h2 class="videodetailheader">Workout Details</h2>(.+?)</div>' , re . DOTALL ) . findall ( I11i1ii1 )
 for ooOO00Oo in IiiIIIiI1ii :
  oO00OOOOOO0o = ( ooOO00Oo ) . replace ( '<p>' , '' ) . replace ( '</p>' , '' ) . replace ( '<br />' , '' ) . replace ( '&nbsp;' , '' ) . replace ( '<strong>' , '' ) . replace ( '</strong>' , '' ) . replace ( '"' , '' ) . replace ( '<' , '' ) . replace ( '>' , '' ) . replace ( 'a href' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&rsquo;t' , '' ) . replace ( '&amp;' , '&' )
  IIIIii ( 'INFO' , '' , 7087 , 'https://www.fitnessblender.com' + OO0ooOOO0OOO , '' , oO00OOOOOO0o )
  if 18 - 18: ii11ii1ii / Oo - i1I111ii1II1i
def oO000 ( INFO ) :
 o0OoOO000ooO0 ( 'info for workout' , INFO )
 if 81 - 81: O0ooOooooO
 if 62 - 62: iI + O0 * Ooo00oOo00o
 if 59 - 59: OoOoOO00
def iIiIi11 ( url ) :
 OO0oo = O0Oooo0O ( url )
 O0o = re . compile ( 'cat-item-.+?"><a href="(.+?)" >(.+?)</a>' ) . findall ( OO0oo )
 for url , I1iI1iIi111i in O0o :
  I1I1i1I ( I1iI1iIi111i , url , 9031 , ii11iIi1I + 'icon.png' )
def I1iIii1i11 ( url ) :
 OO0oo = O0Oooo0O ( url )
 O0o = re . compile ( '<a href="(.+?)" title=".+?" rel="bookmark"><time class="entry-date published updated" datetime=".+?">(.+?)</time></a>' ) . findall ( OO0oo )
 for url , I1iI1iIi111i in O0o :
  I1I1i1I ( I1iI1iIi111i , url , 9032 , ii11iIi1I + 'icon.png' )
def iIiiI11II11i ( url ) :
 OO0oo = O0Oooo0O ( url )
 O0o = re . compile ( '#EXTINF:-.+?,(.+)\s*(.+)\s*' ) . findall ( OO0oo )
 for I1iI1iIi111i , url in O0o :
  if '://' in I1iI1iIi111i :
   pass
   II1Ii1iI1i1 ( ( I1iI1iIi111i ) . replace ( '<br />' , '' ) , ( url ) . replace ( '<br />' , '' ) , 222 , ii11iIi1I + 'icon.png' )
def o00OoO0o0 ( url ) :
 OO0oo = O0Oooo0O ( url )
 O0o = re . compile ( 'EXTINF:-.+?,(.+)</div></li><li class=".+?"><div class=".+?">(.+?)</div>).findall' ) . findall ( OO0oo )
 for I1iI1iIi111i , url in O0o :
  II1Ii1iI1i1 ( I1iI1iIi111i , url , 222 , ii11iIi1I + 'icon.png' )
  if 52 - 52: i1I111ii1II1i . O0ooOooooO - iI
  if 85 - 85: ii11ii1ii / i1IIi * Ooo00oOo00o . O0ooOooooO
  if 60 - 60: Oooo0Ooo000
def o0oOOO ( ) :
 OO0oo = O0Oooo0O ( 'http://www.disclose.tv/action/videolist/aliens/page/1/all/channel/1/category/1/' )
 O0o = re . compile ( '<li><a href="([^"]*)">(.+?)</a></li>' ) . findall ( OO0oo )
 for oOo0 , I1iI1iIi111i in O0o :
  I1I1i1I ( I1iI1iIi111i , 'http://www.disclose.tv/' + oOo0 , 7010 , ii11iIi1I + 'disclose.png' )
  if 24 - 24: OOooOOo / iI / iI % OoOoOO00 - O0ooOooooO * O0ooOooooO
  if 58 - 58: I1IiI
def o0oOO ( url ) :
 OO0oo = O0Oooo0O ( url )
 O0o = re . compile ( 'href="([^"]*)"><img width="135" height="76" alt="([^"]*)".+?src="([^"]*)" />' , re . DOTALL ) . findall ( OO0oo )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' ) . findall ( OO0oo )
 for url , I1iI1iIi111i , OO0ooOOO0OOO in O0o :
  I1I1i1I ( I1iI1iIi111i , 'http://www.disclose.tv/' + url , 7011 , OO0ooOOO0OOO )
 for url in next :
  I1I1i1I ( 'NEXT' , url , 7010 , ii11iIi1I + 'Next.png' )
  if 84 - 84: i11iIiiIii + OOO0OOo . O0
  if 69 - 69: o00OO00OoO / OoooooooOO % i11iIiiIii
def Ii11IIIi1 ( url ) :
 OO0oo = O0Oooo0O ( url )
 O0o = re . compile ( 'url: "([^"]*)",' , re . DOTALL ) . findall ( OO0oo )
 IIIIiiIiiI = re . compile ( "src='([^']*)' type='([^']*)' />" , re . DOTALL ) . findall ( OO0oo )
 for url in O0o :
  if 'http' in url :
   II1Ii1iI1i1 ( 'video/flv' , url , 222 , ii11iIi1I + 'disclose.png' )
 for url , I1iI1iIi111i in IIIIiiIiiI :
  II1Ii1iI1i1 ( I1iI1iIi111i , url , 222 , ii11iIi1I + 'disclose.png' )
  if 93 - 93: i11iIiiIii . OOooOOo
  if 16 - 16: i1IIi . i1IIi / o00OO00OoO % I1IiI / OOOo0 * ii11ii1ii
def IIIii11 ( url ) :
 OO0oo = O0Oooo0O ( url )
 O0o = re . compile ( '<div id="play-1".+?src="(.+?)" scrolling="no".+?<li><a href="#play-1">(.+?)</a></li>' , re . DOTALL ) . findall ( OO0oo )
 for url , I1iI1iIi111i in O0o :
  I1I1i1I ( I1iI1iIi111i , ( url + '&fv=&sou=' ) . replace ( 'player' , 'watch' ) , 7000 , ii11iIi1I + 'icon.png' )
  if 29 - 29: iI - iI / OOO0OOo
def I11IIII ( name , url , img ) :
 I11i1ii1 = O0Oooo0O ( url )
 IiIi1I1Iiii = re . compile ( '<iframe class="playerframe" src="(.+?)" scrolling=".+?" marginwidth=".+?" marginheight=".+?" vspace=".+?" hspace=".+?" allowfullscreen=".+?" webkitallowfullscreen=".+?" mozallowfullscreen=".+?" width=".+?" height=".+?" frameborder=".+?"></iframe>' , re . DOTALL ) . findall ( I11i1ii1 )
 oOIii = len ( IiIi1I1Iiii )
 if 33 - 33: OoOo00o % Oo - O0ooOooooO
 if 53 - 53: OoOoOO00
 if oOIii == 1 :
  for Oo0O0ooo0O0O in IiIi1I1Iiii :
   Oo0O0ooo0O0O = Oo0O0ooo0O0O . replace ( 'player' , 'watch' )
   iIIiI = Oo0O0ooo0O0O + '&fv=&sou='
   Oo0O00oOoo00 = O0Oooo0O ( iIIiI )
   IIiII1 = re . compile ( '<source src="(.+?)" type=".+?">' , re . DOTALL ) . findall ( Oo0O00oOoo00 )
   for II1 in IIiII1 :
    IiIIiiiii1Iii = False
    Resolve ( II1 )
    if 91 - 91: OOO0OOo * OoOo00o * OoOoOO00
 elif oOIii > 1 :
  if 79 - 79: o00OO00OoO
  for Oo0O0ooo0O0O in IiIi1I1Iiii :
   i1iiiIi11 = O0Oooo0O ( Oo0O0ooo0O0O )
   OOoOOO = re . compile ( '<iframe width=".*?" height=".*?" frameborder=".*?" src="(.*?)" scrolling=".*?" marginwidth=".*?" marginheight=".*?" vspace=".*?" hspace=".*?" allowfullscreen=".*?" webkitallowfullscreen=".*?" mozallowfullscreen=".*?"></iframe>' , re . DOTALL ) . findall ( i1iiiIi11 )
   oooooO0O0o = OOoOOO
   oooooO0O0o = ( str ( oooooO0O0o ) ) . replace ( '[\'' , '' ) . replace ( '\']' , '' ) ;
   print 'Stripped url : ' + oooooO0O0o
   II1Ii1iI1i1 ( 'DOUBLE LINK' , oooooO0O0o , 424 , '' )
   if 8 - 8: i11iIiiIii . i1I111ii1II1i / iIii1I11I1II1 / ii11ii1ii / OoOo00o - iI
   for url in OOoOOO :
    I1I1i1I ( 'DOUBLE LINK' , url , 424 , '' )
    try :
     IIo0o0O0O00oOOo = Google . resolve ( url )
    except :
     pass
    try :
     iI1i1I1iiii1Ii11 = re . findall ( r"{'url': u'(.*?)', 'quality': 'HD'}, {'url': u'(.*?)', 'quality': 'SD'}" , str ( IIo0o0O0O00oOOo ) )
     for IiII , IIi in iI1i1I1iiii1Ii11 :
      if 51 - 51: OoOoOO00 . O0ooOooooO . Ooo00oOo00o % OoOoOO00
      HD_URLS . append ( IiII )
      SD_URLS . append ( IIi )
    except :
     pass
 else :
  pass
  if 41 - 41: I1IiI - i1I111II1I + OOO0OOo - i1IIi
def iiiiI ( ) :
 if 72 - 72: Oooo0Ooo000 . OoOoOO00 * i1IIi
 if 79 - 79: ii11ii1ii / O0 % OOooOOo
 I1I1i1I ( 'Genres' , 'http://cnfstudio.com/movies/' , 7002 , ii11iIi1I + 'Movies.png' )
 if 71 - 71: o00OO00OoO / OOOo0 / O0
 I1I1i1I ( 'Search Movies' , '' , 7017 , ii11iIi1I + 'Movies.png' )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 19 - 19: i11iIiiIii . OOOo0 + OoOoOO00 / i1I111II1I . ii11ii1ii * OOO0OOo
 if 59 - 59: iIii1I11I1II1 / ii11ii1ii % OOO0OOo
def Oooo ( ) :
 OO0oo = O0Oooo0O ( 'http://cnfstudio.com/' )
 O0o = re . compile ( '<a href="http://cnfstudio.com/genre/(.+?)">(.+?)</a>' ) . findall ( OO0oo )
 for oOo0 , I1iI1iIi111i in O0o :
  I1I1i1I ( I1iI1iIi111i , 'http://cnfstudio.com/genre/' + oOo0 , 7003 , ii11iIi1I + 'icon.png' )
  if 74 - 74: OOO0OOo % I1IiI / Oo
i1iiIIiiI111 = xbmcgui . Dialog ( )
if 2 - 2: OoOo00o % OoOo00o % o00OO00OoO
if 60 - 60: i1I111II1I
def o0OoOo00O0o0O ( url ) :
 OO0oo = O0Oooo0O ( url )
 O0o = re . compile ( '<div class="movie">.+?<img src="(.+?)" alt=".+?" />.+?<a href="(.+?)"><span class="player"></span></a>.+?<h2>(.+?)</h2>' , re . DOTALL ) . findall ( OO0oo )
 O0O0Oo00OO = re . compile ( "<link rel='next' href='(.+?)'/>" ) . findall ( OO0oo )
 for OO0ooOOO0OOO , url , I1iI1iIi111i in O0o :
  II1Ii1iI1i1 ( ( I1iI1iIi111i ) . replace ( '&#038;' , '' ) . replace ( '&#8216;' , '' ) . replace ( '&#8217;' , '' ) . replace ( '&#8211;' , '' ) , url , 7004 , OO0ooOOO0OOO )
 O0O0Oo00OO = O0O0Oo00OO
 for url in O0O0Oo00OO :
  I1I1i1I ( 'Next Page' , url , 7003 , ii11iIi1I + 'Next.png' )
  if 100 - 100: OOooOOo . OOOo0
def o00o0O0 ( url ) :
 if 47 - 47: OOO0OOo
 OO0oo = O0Oooo0O ( url )
 O0o = re . compile ( '<div id="play-1" class="player-content"><iframe class="playerframe" src="(.+?)" scrolling="no".+?</div>' , re . DOTALL ) . findall ( OO0oo )
 for url in O0o :
  oOo00O000Oo0 = url + '&fv=&sou='
  oOo00O000Oo0 = oOo00O000Oo0 . replace ( 'player' , 'watch' )
  Oo0oo = IiIi ( oOo00O000Oo0 )
  iI1iii1iIiiI = IiIi ( url )
  if 36 - 36: Ooo00oOo00o - O0 * OOOo0 / ii11ii1ii / i1I111II1I
  if 33 - 33: OoooooooOO % ii11ii1ii . O0 / ii11ii1ii
def IiIi ( url ) :
 if 63 - 63: OoOo00o + iIii1I11I1II1 + OOOo0 + o00OO00OoO
 OO0oo = O0Oooo0O ( url )
 O0o = re . compile ( '<video id=".+?<source src="(.+?)" type="video/mp4">' , re . DOTALL ) . findall ( OO0oo )
 for url in O0o :
  iIIIiIi ( url )
  if 72 - 72: Ooo00oOo00o + i11iIiiIii + ii11ii1ii
  if 96 - 96: O0ooOooooO % i1IIi / OOooOOo
def Ii1IIi11 ( ) :
 IIIIii ( '[COLORgreen]Local M3u[/COLOR]' , oOo0oooo00o , 2001 , ii11iIi1I + 'loader.png' , i1iiIII111ii , '' )
 IIIIii ( '[COLORgreen]Remote M3u[/COLOR]' , Oo0o0000o0o0 , 1009 , ii11iIi1I + 'loader.png' , i1iiIII111ii , '' )
 if 47 - 47: O0
def OooOoo ( url ) :
 O0o = re . compile ( '^#EXTINF:-?[0-9]*(.*?),(.*?)\n(.*?)$' , re . I + re . M + re . U + re . S ) . findall
 for Oooo0Oo00o , I1iI1iIi111i , url in O0o :
  II1Ii1iI1i1 ( I1iI1iIi111i , url , 222 , ii11iIi1I + 'streams.png' )
  if 32 - 32: I1IiI . iIii1I11I1II1 % O0ooOooooO . O0 . I1IiI / i1I111ii1II1i
  if 45 - 45: iIii1I11I1II1
def I1I111IIIi1 ( ) :
 IIIIii ( '[COLORgreen]CATAGORIES[/COLOR]' , '' , 10051 , ii11iIi1I + 'loader.png' , i1iiIII111ii , '' )
 IIIIii ( '[COLORgreen]SEARCH[/COLOR]' , '' , 10052 , ii11iIi1I + 'loader.png' , i1iiIII111ii , '' )
 if 66 - 66: OOooOOo % I1IiI
 if 30 - 30: I1IiI * Oo % iIii1I11I1II1 % Ooo00oOo00o + i11iIiiIii
o0oO0 = xbmcaddon . Addon ( id = 'plugin.video.GenieTv' )
oOOoo00O0O = xbmcgui . Dialog ( )
oooOOOOO = xbmc . translatePath ( 'special://home/' )
Oo0oO0ooo = xbmcgui . DialogProgress ( )
IiOo00O0o0O = 'https://addons.tvaddons.ag/'
if 86 - 86: Oooo0Ooo000 + O0 + Oo - Oooo0Ooo000
def Ii1iI1IIIII ( ) :
 IiII111iI1ii1 = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 Ii1I = IiII111iI1ii1 . lower ( )
 o00OoOO0O0 = 'https://addons.tvaddons.ag/search/?keyword=' + Ii1I
 I11i1ii1 = O0Oooo0O ( o00OoOO0O0 )
 O0o = re . compile ( '<li><a href="(.+?)"><span class=".+?"><img src="(.+?)" width=".+?" alt=".+?" class=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( I11i1ii1 )
 for oOo0 , II1iI , I1iI1iIi111i in O0o :
  IIIIii ( I1iI1iIi111i , oOo0 , 10054 , 'https://addons.tvaddons.ag/' + II1iI , i1iiIII111ii , '' )
  if 93 - 93: iIii1I11I1II1 - OOO0OOo / O0ooOooooO + i11iIiiIii + OoOo00o
  if 16 - 16: iIii1I11I1II1
def o000o0o00Oo ( ) :
 I11i1ii1 = O0Oooo0O ( IiOo00O0o0O )
 O0o = re . compile ( '<li><a href="(.+?)"><span class="thumbnail"><img src="(.+?)" class="pic" alt=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( I11i1ii1 )
 for oOo0 , OO0ooOOO0OOO , I1iI1iIi111i in O0o :
  if 'Repositories' in I1iI1iIi111i :
   pass
  elif 'Services' in I1iI1iIi111i :
   pass
  elif 'International' in I1iI1iIi111i :
   pass
  else :
   IIIIii ( '[COLORgreen]' + I1iI1iIi111i + '[/COLOR]' , oOo0 , 10053 , 'https://addons.tvaddons.ag/' + OO0ooOOO0OOO , i1iiIII111ii , '' )
   if 62 - 62: i1I111ii1II1i
   if 8 - 8: i1I111ii1II1i - OOOo0 * Oo % ii11ii1ii * OoooooooOO
def Addon ( url ) :
 I11i1ii1 = O0Oooo0O ( url )
 iii11 = re . compile ( '<li class="nextPage"><a class=".+?" href="(.+?)"><dfn title="next Page">.+?</dfn></a></li>' ) . findall ( I11i1ii1 )
 for url in iii11 :
  IIIIii ( '[COLORgreen]NEXT PAGE[/COLOR]' , 'https://addons.tvaddons.ag' + url , 10053 , ii11iIi1I + 'Next.png' , i1iiIII111ii , '' )
 O0o = re . compile ( '<li><a href="(.+?)"><span class=".+?"><img src="(.+?)" width=".+?" alt=".+?" class=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( I11i1ii1 )
 for url , OO0ooOOO0OOO , I1iI1iIi111i in O0o :
  if 'Please' in I1iI1iIi111i :
   pass
  else :
   IIIIii ( I1iI1iIi111i , url , 10054 , 'https://addons.tvaddons.ag/' + OO0ooOOO0OOO , i1iiIII111ii , '' )
   if 20 - 20: i1I111II1I - i1I111ii1II1i / Oo * Ooo00oOo00o
   if 55 - 55: OoooooooOO
def OO0OOOOOo ( url , name ) :
 I11i1ii1 = O0Oooo0O ( url )
 O0o = re . compile ( '<a href="(.+?)"' ) . findall ( I11i1ii1 )
 for url in O0o :
  if 'plugin' in url :
   print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<' + url
   O0O0Oo00 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
   Oo0oO0ooo = xbmcgui . DialogProgress ( )
   Oo0oO0ooo . create ( "Origin+Jaybox" , "Downloading Content" , '' , 'Please Wait' )
   iIii = os . path . join ( O0O0Oo00 , name + '.zip' )
   try :
    os . remove ( iIii )
   except :
    pass
   downloader . download ( url , iIii , Oo0oO0ooo )
   OOO00OO0oOo = xbmc . translatePath ( os . path . join ( 'special://home' , 'addons' ) )
   time . sleep ( 2 )
   Oo0oO0ooo . update ( 0 , "" , "Extracting Zip Please Wait" )
   print '======================================='
   print OOO00OO0oOo
   print '======================================='
   extract . all ( iIii , OOO00OO0oOo , Oo0oO0ooo )
   oOooOOOoOo ( )
   if 7 - 7: O0 + iI . OoOoOO00
def oOooOOOoOo ( ) :
 xbmc . executebuiltin ( 'UpdateLocalAddons' )
 xbmc . executebuiltin ( 'UpdateAddonRepos' )
 i1iiIIiiI111 = xbmcgui . Dialog ( )
 i1iiIIiiI111 . ok ( "Origin + Genie TV" , '' , '                                 REFRESH SUCCESSFUL :)' , "                          [COLOR gold]Brought To You By Origin + Jaybox[/COLOR]" )
 return
 if 12 - 12: OOOo0 - i1IIi
 if 95 - 95: Oooo0Ooo000 / OoOo00o . O0 * OoOo00o - OOooOOo * Oo
def II1iiI1iI ( ) :
 OO0oo = Iii1 ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvc2NyYXBlZC9jYXRzLnBocA==' ) )
 O0o = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( OO0oo )
 for oOo0 , II1iI , I1iI1iIi111i in O0o :
  I1I1i1I ( I1iI1iIi111i , oOo0 , 1007 , II1iI )
def O0oo0000o ( url ) :
 OO0oo = Iii1 ( url )
 O0o = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( OO0oo )
 for url , II1iI , I1iI1iIi111i in O0o :
  I1I1i1I ( '[COLORgreen]' + I1iI1iIi111i + '[/COLOR]' , url , 1006 , II1iI )
  if 99 - 99: O0ooOooooO - ii11ii1ii . OoOoOO00 * i11iIiiIii . i1I111II1I - Ooo00oOo00o
  if 31 - 31: i11iIiiIii * iI . OOooOOo % i1I111II1I * ii11ii1ii % O0
def OOoO00O ( url ) :
 OO0oo = Iii1 ( url )
 O0o = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( OO0oo )
 for url , OOO0000oO , OOoOO0ooo , iI1i111I1Ii , I1iI1iIi111i in O0o :
  if '.php' in url :
   OOoo0 ( I1iI1iIi111i , url , 1016 , OOO0000oO , iI1i111I1Ii , OOoOO0ooo )
  else :
   if 'youtube' in url :
    Iiio0Oo0oO ( I1iI1iIi111i , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , OOO0000oO , iI1i111I1Ii , OOoOO0ooo )
   else :
    Iiio0Oo0oO ( I1iI1iIi111i , url , 222 , OOO0000oO , iI1i111I1Ii , OOoOO0ooo )
    O00Oo000ooO0 ( 'movies' , 'INFO' )
    if 20 - 20: i1IIi . i1IIi - Oooo0Ooo000
 else :
  O0o = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( OO0oo )
  for url , II1iI , I1iI1iIi111i in O0o :
   if '.php' in url :
    I1I1i1I ( I1iI1iIi111i , url , 1016 , II1iI )
   else :
    if 'youtube' in url :
     print '>>>>>>>>>>>>>>>>>>>>>>> youtube old way'
     II1Ii1iI1i1 ( I1iI1iIi111i , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , II1iI )
    else :
     II1Ii1iI1i1 ( I1iI1iIi111i , url , 222 , II1iI )
     O00Oo000ooO0 ( 'movies' , 'INFO' )
     if 89 - 89: OOO0OOo - Oooo0Ooo000 . O0 % OoooooooOO . i11iIiiIii
  xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 35 - 35: OoOoOO00 / I1IiI - O0 . OoOoOO00
def oO0o000oOO ( ) :
 OO0oo = Iii1 ( i1111 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vdm9kL3VybHMvdXJsLnBocA==' ) )
 O0o = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( OO0oo )
 for oOo0 , II1iI , I1iI1iIi111i in O0o :
  I1I1i1I ( I1iI1iIi111i , oOo0 , 1007 , II1iI )
def Ii11Iiii ( url ) :
 OO0oo = Iii1 ( url )
 O0o = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( OO0oo )
 for url , II1iI , I1iI1iIi111i in O0o :
  I1I1i1I ( '[COLORgreen]' + I1iI1iIi111i + '[/COLOR]' , url , 1006 , II1iI )
  if 98 - 98: i1IIi % Oo
def o0OOoOooO0ooO ( name , url , iconimage = None ) :
 print '--- Playing "{0}". {1}' . format ( name , url )
 IiiiIi = xbmcgui . ListItem ( path = url , thumbnailImage = iconimage )
 IiiiIi . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , IiiiIi )
 if 31 - 31: i11iIiiIii + OoOo00o - o00OO00OoO * i1I111ii1II1i
 if 60 - 60: i1I111ii1II1i + Ooo00oOo00o + Oooo0Ooo000 % iIii1I11I1II1 . Oo
def O0OOOOoO00oo ( url ) :
 OO0oo = Iii1 ( url )
 O0o = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( OO0oo )
 for url , OO0ooOOO0OOO , I1iI1iIi111i in O0o :
  I1I1i1I ( '[COLORgreen]' + I1iI1iIi111i + '[/COLOR]' , url , 1006 , OO0ooOOO0OOO )
def OoOiII11IiIi ( url ) :
 OO0oo = Iii1 ( url )
 OooooOo = url
 O0o = re . compile ( "<a href='(.+?)'>(.+?)</a>" ) . findall ( OO0oo )
 for url , I1iI1iIi111i in O0o :
  if '.mp3' in I1iI1iIi111i :
   print '<<<<<<<<<<<<<<<<<<<' + url + '>>>>>>>>>>>>>>>>>>>>>>>>>>>'
   II1Ii1iI1i1 ( ( I1iI1iIi111i ) . replace ( '.mp3' , '' ) . replace ( '/' , '' ) , 'http://hypem.com' + url , 222 , ii11iIi1I + 'music.png' )
  else :
   I1I1i1I ( ( I1iI1iIi111i ) . replace ( '/' , '' ) , OooooOo + url , 1011 , ii11iIi1I + 'music.png' )
def iII1I1i ( ) :
 OO0oo = Iii1 ( i1111 ( 'aHR0cDovL3d3dy5jeW4ubmV0L211c2ljLw==' ) )
 O0o = re . compile ( '<td><a href="(.+?)"><img src="(.+?)"><br>(.+?)</a></td>' , re . DOTALL ) . findall ( OO0oo )
 for oOo0 , OO0ooOOO0OOO , I1iI1iIi111i in O0o :
  I1I1i1I ( I1iI1iIi111i , ( 'http://www.cyn.net/music/' + oOo0 ) . replace ( ' ' , '%20' ) , 1031 , ( 'http://www.cyn.net/music/' + OO0ooOOO0OOO ) . replace ( ' ' , '%20' ) )
def IIiii ( url , img ) :
 OO0oo = Iii1 ( url )
 IIo0o0O0O00oOOo = url
 img = img
 O0o = re . compile ( '<a href="(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( OO0oo )
 for url , I1iI1iIi111i in O0o :
  II1Ii1iI1i1 ( ( I1iI1iIi111i ) . replace ( '.mp3' , '' ) , ( IIo0o0O0O00oOOo + '/' + url ) . replace ( ' ' , '%20' ) , 222 , img )
  if 77 - 77: iIii1I11I1II1 * O0ooOooooO
  if 15 - 15: iIii1I11I1II1 . i1I111II1I . ii11ii1ii * i11iIiiIii
def ooo00O0OOo ( ) :
 oOO0oo = ( i1111 ( 'aHR0cDovL2h5cGVtLmNvbS9kb3dubG9hZC8=' ) )
 IiII111iI1ii1 = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 Ii1I = IiII111iI1ii1 . lower ( )
 oOo0 = ( i1111 ( 'aHR0cDovL3Bhbmljc3RyZWFtLm5ldC9zdHJlYW1zLw==' ) )
 IIo0o0O0O00oOOo = ( i1111 ( 'aHR0cDovL21hc2xvdmQubm8taXAub3JnL3B1YmxpYy9tcDMv' ) )
 OO0O0 = ( i1111 ( 'aHR0cDovL3d3dy5jeW4ubmV0L211c2ljLw==' ) )
 if 45 - 45: OOOo0 / i1I111ii1II1i + O0ooOooooO + OoOo00o
 I11i1ii1 = I1IiI1IIiI ( oOo0 )
 o00o = I1IiI1IIiI ( IIo0o0O0O00oOOo )
 iIIi1i11 = I1IiI1IIiI ( OO0O0 )
 if 15 - 15: OOOo0 % Ooo00oOo00o
 if I11i1ii1 != 'Failed' :
  O0o = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( I11i1ii1 )
  for I1iI1iIi111i in O0o :
   if IiII111iI1ii1 in I1iI1iIi111i . lower ( ) :
    I1I1i1I ( ( I1iI1iIi111i + ' source 1' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( oOo0 + I1iI1iIi111i ) . replace ( ' ' , '%20' ) , 1006 , '' )
    if 66 - 66: O0ooOooooO * i11iIiiIii . o00OO00OoO
    O00Oo000ooO0 ( 'tvshows' , 'Media Info 3' )
 if o00o != 'Failed' :
  IIIIiiIiiI = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( I11i1ii1 )
  for I1iI1iIi111i in IIIIiiIiiI :
   if IiII111iI1ii1 in I1iI1iIi111i . lower ( ) :
    I1I1i1I ( ( I1iI1iIi111i + ' source 2' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( IIo0o0O0O00oOOo + I1iI1iIi111i ) . replace ( ' ' , '%20' ) , 1006 , '' )
    if 92 - 92: O0ooOooooO
    O00Oo000ooO0 ( 'tvshows' , 'Media Info 3' )
 if iIIi1i11 != 'Failed' :
  O0oOOo0o = re . compile ( '<td><a href=".+?"><img src=".+?"><br>(.+?)</a></td>' , re . DOTALL ) . findall ( iIIi1i11 )
  for I1iI1iIi111i in O0oOOo0o :
   if IiII111iI1ii1 in I1iI1iIi111i . lower ( ) :
    I1I1i1I ( ( I1iI1iIi111i + ' source 3' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( OO0O0 + I1iI1iIi111i ) . replace ( ' ' , '%20' ) , 1031 , '' )
    if 81 - 81: OOooOOo % OOOo0 - i1I111ii1II1i / i11iIiiIii
    O00Oo000ooO0 ( 'tvshows' , 'Media Info 3' )
    if 73 - 73: O0 * o00OO00OoO . i1IIi
    if 51 - 51: Ooo00oOo00o - i1I111ii1II1i % O0 - I1IiI
    if 53 - 53: i1I111ii1II1i / i1IIi / i1IIi
    if 77 - 77: Oooo0Ooo000 + i1IIi . Oooo0Ooo000
    if 89 - 89: OOooOOo + i1I111II1I * O0ooOooooO
    if 45 - 45: i1I111ii1II1i - OOooOOo . iI
def Iiii1II111 ( ) :
 OO0oo = O0Oooo0O ( 'http://www.iwatchseries.me/tv-list/' )
 O0o = re . compile ( '<h5><a href="([^"]*)"><strong>(.+?)</strong></a></h5>' ) . findall ( OO0oo )
 for oOo0 , I1iI1iIi111i in O0o :
  I1I1i1I ( I1iI1iIi111i , oOo0 , 8021 , ii11iIi1I + 'iwatch.png' )
def iI11i ( url ) :
 OO0oo = O0Oooo0O ( url )
 O0o = re . compile ( '<h5><strong><a href="([^"]*)">(.+?)</a>(.+?)</strong></h5>' ) . findall ( OO0oo )
 for url , I1iI1iIi111i , oo0O0o00o0O in O0o :
  I1I1i1I ( I1iI1iIi111i + oo0O0o00o0O , url , 8022 , ii11iIi1I + 'iwatch.png' )
def i1i111III1 ( url ) :
 OO0oo = O0Oooo0O ( url )
 O0o = re . compile ( '<iframe src="([^"]*)"' ) . findall ( OO0oo )
 for url in O0o :
  print '>>>>>>>>>>>>>>>>>>>>' + url
  III1i1IIII1i ( url )
def III1i1IIII1i ( url ) :
 OO0oo = O0Oooo0O ( url )
 O0o = re . compile ( '{.+?"file" : "(.+?)",.+?"default" : true.+?"label" : "(.+?)"' , re . DOTALL ) . findall ( OO0oo )
 IIIIiiIiiI = re . compile ( 'setup\(\{.+?file: "(.+?)",.+?skin' , re . DOTALL ) . findall ( OO0oo )
 O0oOOo0o = re . compile ( "{ label: '([^']*)', file:.+?'([^']*)' }" ) . findall ( OO0oo )
 for url , I1iI1iIi111i in O0o :
  II1Ii1iI1i1 ( 'VidSpot - ' + I1iI1iIi111i , url , 222 , ii11iIi1I + 'iwatch.png' )
 for url in IIIIiiIiiI :
  II1Ii1iI1i1 ( 'VodLocker' , url , 222 , ii11iIi1I + 'iwatch.png' )
 for I1iI1iIi111i , url in O0oOOo0o :
  print '<><><><><><><><><><><> before   ' + url
  if 'hevideo' in url :
   print '>>>>>>>>>>>>>>>>>>>>>>>>>' + url
   II1Ii1iI1i1 ( 'TheVideo - ' + I1iI1iIi111i , url , 222 , ii11iIi1I + 'iwatch.png' )
   if 48 - 48: OoooooooOO
def Oo0OOOOOOO0oo ( ) :
 OO0oo = cloudflare . source ( 'http://www.animeland.me/anime-list' )
 O0o = re . compile ( 'letter-spacing:-1px;" href="([^"]*)">(.+?)</a></li>' ) . findall ( OO0oo )
 for oOo0 , I1iI1iIi111i in O0o :
  I1I1i1I ( I1iI1iIi111i , oOo0 , 1021 , ii11iIi1I + 'anime.png' )
  if 35 - 35: ii11ii1ii * Ooo00oOo00o * OOOo0 / OoooooooOO
  if 15 - 15: OOO0OOo % OOooOOo / O0ooOooooO - OoOoOO00 . iIii1I11I1II1
def ii1111Iii11i ( ) :
 OO0oo = O0Oooo0O ( 'http://www.animetoon.org/cartoon' )
 O0o = re . compile ( '<td><a href="(.+?)">(.+)</a></td>' ) . findall ( OO0oo )
 for oOo0 , I1iI1iIi111i in O0o :
  I1I1i1I ( I1iI1iIi111i , oOo0 , 1002 , ii11iIi1I + 'anime.png' )
  if 91 - 91: iI - i1I111ii1II1i . i1IIi . ii11ii1ii * OOooOOo % i1I111ii1II1i
  if 30 - 30: Oooo0Ooo000
  if 85 - 85: OoOoOO00 + OOO0OOo * Oooo0Ooo000
def i1ooOO00o0 ( url ) :
 OO0oo = O0Oooo0O ( url )
 IIIIiiIiiI = re . compile ( '<img src="(.+?)" id="series_image" width="250" height="370" alt=".+?" />' ) . findall ( OO0oo )
 for OO0ooOOO0OOO in IIIIiiIiiI :
  I1IIiI = OO0ooOOO0OOO
 O0oOOo0o = re . compile ( '<li><a href="(.+?)">Next</a></li>' ) . findall ( OO0oo )
 for url in O0oOOo0o :
  I1I1i1I ( 'NEXT PAGE' , url , 1002 , ii11iIi1I + 'Next.png' )
 O0o = re . compile ( '&nbsp;<a href="(.+?)">(.+?)</a>' ) . findall ( OO0oo )
 for url , I1iI1iIi111i in O0o :
  I1I1i1I ( I1iI1iIi111i , url , 1003 , I1IIiI )
 xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
def Ii1I1iIiiI1 ( url , IMAGE ) :
 OO0oo = O0Oooo0O ( url )
 O0o = re . compile ( '"playlist">(.+?)</span></div><div><iframe src="(.+?)"' ) . findall ( OO0oo )
 for I1iI1iIi111i , url in O0o :
  print I1iI1iIi111i + '     ' + url
  if 'easy' in url :
   o00i111iiIiiIiI ( url )
  elif 'playpanda' in url :
   o00i111iiIiiIiI ( url )
   if 59 - 59: i1I111II1I + OOOo0 / OoOoOO00 / I1IiI
  xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
def o00i111iiIiiIiI ( url ) :
 OO0oo = O0Oooo0O ( url )
 O0o = re . compile ( "url: '(.+?)'," ) . findall ( OO0oo )
 for url in O0o :
  II1Ii1iI1i1 ( 'STREAM' , url , 222 , ii11iIi1I + 'anime.png' )
  if 80 - 80: I1IiI + iIii1I11I1II1 . OoOo00o
  if 76 - 76: OOOo0 * i1I111II1I
def ii111 ( url ) :
 ooooo0o0oo0Ooo = urllib2 . Request ( url )
 ooooo0o0oo0Ooo . add_header ( 'User-Agent' , "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0" )
 ooooo0o0oo0Ooo . add_header ( 'referer' , url )
 iI1i = urllib2 . urlopen ( ooooo0o0oo0Ooo )
 oOo00O000Oo0 = iI1i . read ( )
 iI1i . close ( )
 return oOo00O000Oo0
 if 49 - 49: Ooo00oOo00o + OoOoOO00 / OoOo00o - O0 % iI
def Iii1 ( url ) :
 ooooo0o0oo0Ooo = urllib2 . Request ( url )
 ooooo0o0oo0Ooo . add_header ( 'User-Agent' , "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0" )
 iI1i = urllib2 . urlopen ( ooooo0o0oo0Ooo )
 oOo00O000Oo0 = iI1i . read ( )
 iI1i . close ( )
 return oOo00O000Oo0
 if 27 - 27: Ooo00oOo00o + Oo
def oO0oOOooO0 ( url ) :
 xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
 O00 = ( '%s%s' % ( O0OO0 , url ) )
 oOo00O000Oo0 = Iii1 ( url )
 O0o = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( oOo00O000Oo0 )
 for url , II1iI , I1iI1iIi111i in O0o :
  II1Ii1iI1i1 ( '%s' % ( I1iI1iIi111i ) . replace ( 'GenieTv' , '[COLOR green]GenieTV[/COLOR]' ) . replace ( '.' , ' ' ) . replace ( 'mp4' , '' ) . replace ( 'mkv' , '' ) . replace ( '_' , ' ' ) , '%s' % ( url ) , 222 , II1iI )
  if 62 - 62: i11iIiiIii - Oooo0Ooo000
def iIIIiIi ( url ) :
 IIII1ii = xbmc . Player ( IiIi1Ii ( ) )
 import urlresolver
 try : IIII1ii . play ( url )
 except : pass
 from urlresolver import common
 Oo0oO0ooo = xbmcgui . DialogProgress ( )
 Oo0oO0ooo . create ( 'LOADING' , 'Opening %s Now' % ( I1iI1iIi111i ) )
 IIII1ii = xbmc . Player ( IiIi1Ii ( ) )
 url = urlresolver . HostedMediaFile ( url ) . resolve ( )
 if Oo0oO0ooo . iscanceled ( ) :
  print "[COLORred]STREAM CANCELLED[/COLOR]"
  i1iiIIiiI111 = xbmcgui . Dialog ( )
  if i1iiIIiiI111 . yesno ( "[B]CANCELLED[/B]" , '[B]Was There A Problem[/B]' , '' , "" , 'Yes' , 'No' ) :
   i1iiIIiiI111 . ok ( "Message Send" , "Your Message Has Been Sent" )
  else :
   return
 else :
  try : IIII1ii . play ( url )
  except : pass
  try : o0oO0 . resolve_url ( url )
  except : pass
  Oo0oO0ooo . close ( )
  if 81 - 81: Oooo0Ooo000
def OOOOooO0 ( url ) :
 Oo0oO0ooo = xbmcgui . DialogProgress ( )
 Oo0oO0ooo . create ( 'Featching Your Video' , 'Featching Your Video' )
 Oo0oO0ooo . update ( 0 , '%s' % I1iI1iIi111i )
 xbmc . sleep ( 1 )
 IIII1ii = xbmc . Player ( IiIi1Ii ( ) )
 Oo0oO0ooo . update ( 100 , '%s' % I1iI1iIi111i )
 xbmc . sleep ( 1 )
 IIII1ii . play ( url ) . strip ( )
 Oo0oO0ooo . close ( )
 if 23 - 23: OOOo0 * Oooo0Ooo000 / i11iIiiIii * o00OO00OoO . iIii1I11I1II1
def OO0ooo0o0 ( url ) :
 IIII1ii = xbmc . Player ( IiIi1Ii ( ) )
 import urlresolver
 url = ( url ) . strip ( )
 try : IIII1ii . play ( url ) . strip ( )
 except : pass
 if 40 - 40: OOOo0 . iI / i1IIi
 if 28 - 28: iI
def IiIi1Ii ( ) :
 try :
  oooo00Oo0O = getSet ( "core-player" )
  if ( oooo00Oo0O == 'DVDPLAYER' ) : IiIiiIiiiiI = xbmc . PLAYER_CORE_DVDPLAYER
  elif ( oooo00Oo0O == 'MPLAYER' ) : IiIiiIiiiiI = xbmc . PLAYER_CORE_MPLAYER
  elif ( oooo00Oo0O == 'PAPLAYER' ) : IiIiiIiiiiI = xbmc . PLAYER_CORE_PAPLAYER
  else : IiIiiIiiiiI = xbmc . PLAYER_CORE_AUTO
 except : IiIiiIiiiiI = xbmc . PLAYER_CORE_AUTO
 return IiIiiIiiiiI
 return True
 if 48 - 48: OOO0OOo . ii11ii1ii
def I1I1i1I ( name , url , mode , iconimage , showcontext = True , allinfo = { } ) :
 o0OOOOO0O = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 I1I1IiIi1 = True
 oOO0o0oo0 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 oOO0o0oo0 . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 if showcontext :
  IiiIIIIi = [ ]
  if showcontext == 'fav' :
   IiiIIIIi . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in oOoOooOo0o0 :
   IiiIIIIi . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  oOO0o0oo0 . addContextMenuItems ( IiiIIIIi )
 I1I1IiIi1 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = o0OOOOO0O , listitem = oOO0o0oo0 , isFolder = True )
 return I1I1IiIi1
 if 23 - 23: i1IIi + ii11ii1ii + OOOo0 - OOO0OOo % OoooooooOO . OoOo00o
def IIIIIii1ii11 ( name , url , mode , iconimage , fanart , description ) :
 if 49 - 49: O0ooOooooO . I1IiI
 o0OOOOO0O = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 I1I1IiIi1 = True
 oOO0o0oo0 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 oOO0o0oo0 . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 oOO0o0oo0 . setProperty ( "Fanart_Image" , fanart )
 I1I1IiIi1 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = o0OOOOO0O , listitem = oOO0o0oo0 , isFolder = True )
 return I1I1IiIi1
 if 73 - 73: iI / OOOo0 / OoooooooOO + OOOo0
def II1Ii1iI1i1 ( name , url , mode , iconimage , showcontext = True , allinfo = { } ) :
 o0OOOOO0O = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 I1I1IiIi1 = True
 oOO0o0oo0 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 oOO0o0oo0 . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 if showcontext :
  IiiIIIIi = [ ]
  if showcontext == 'fav' :
   IiiIIIIi . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in oOoOooOo0o0 :
   IiiIIIIi . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  oOO0o0oo0 . addContextMenuItems ( IiiIIIIi )
 I1I1IiIi1 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = o0OOOOO0O , listitem = oOO0o0oo0 , isFolder = False )
 return I1I1IiIi1
 if 57 - 57: i1I111II1I . iI % OOooOOo
 if 32 - 32: Oooo0Ooo000 / OoOo00o - O0 * iIii1I11I1II1
 if 70 - 70: OoooooooOO % OoooooooOO % Ooo00oOo00o
 if 98 - 98: Ooo00oOo00o
 if 18 - 18: Oooo0Ooo000 + Oo - Ooo00oOo00o / o00OO00OoO / i1I111II1I
 if 53 - 53: i1I111II1I + OOooOOo . O0ooOooooO / Oooo0Ooo000
def o0OoOO000ooO0 ( heading , announce ) :
 class o0000oO ( ) :
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
   try : i1i1ii = open ( announce ) ; ooo0oo = i1i1ii . read ( )
   except : ooo0oo = announce
   self . win . getControl ( self . CONTROL_TEXTBOX ) . setText ( str ( ooo0oo ) )
   return
 o0000oO ( )
 o0000oO ( )
 if 70 - 70: O0 / OoooooooOO + ii11ii1ii + i1IIi
def O00Oo ( ) :
 o0OoOO000ooO0 ( 'These are the main Sources you should get into you XBMC' , '[COLORwhite]http://architects.x10host.com[/COLOR]--- [CR]  [COLORred]http://repo.sharktech.co.uk[/COLOR]--- [CR]   [COLORwhite]http://fusion.tvaddons.ag[/COLOR]--- [CR]  [COLORred]http://i.totalxbmc.tv[/COLOR]--- [CR]   [COLORwhite]http://www.xunitytalk.com/xfinity[/COLOR]--- [CR]  [COLORred]http://srp.nu[/COLOR]--- [CR]   [COLORwhite]http://solved.no-issue.ca[/COLOR]--- [CR]  [COLORred]http://xbmc.aminhacasadigital.com[/COLOR]--- [CR]   [COLORwhite]http://xbmc.movieshd.co[/COLOR]--- [CR]  [COLORred]http://install.kaosbox.tv[/COLOR]--- [CR]   [COLORwhite]http://kodi-repo.com/mxr[/COLOR]--- [CR]  [COLORred]http://kodi.metalkettle.co[/COLOR]--- [CR]   [COLORwhite]http://prozone.getxbmc.com[/COLOR]--- [CR]  [COLORred]http://transform.mega-tron.tv[/COLOR]--- [CR]   [COLORwhite]http://muckys.kodimediaportal.ml[/COLOR]--- [CR]  [COLORred]http://jas0npc.pcriot.com[/COLOR]--- [CR]  [COLORwhite]Sports devil source[/COLOR]--- [CR]  [COLORred]http://iwillfolo.com/iwf[/COLOR]' )
 if 63 - 63: OOooOOo / O0 - OoooooooOO
 if 74 - 74: iIii1I11I1II1 / iI
 if 59 - 59: iI / OoOoOO00 - OoOo00o % I1IiI % OoooooooOO
 if 79 - 79: i1I111ii1II1i . OoooooooOO . OOOo0 * O0 * Ooo00oOo00o - i1I111II1I
 if 33 - 33: ii11ii1ii . Oo + OOOo0 + OOooOOo
def oOooOOOoOo ( ) :
 xbmc . executebuiltin ( 'UpdateLocalAddons' )
 xbmc . executebuiltin ( 'UpdateAddonRepos' )
 i1iiIIiiI111 = xbmcgui . Dialog ( )
 i1iiIIiiI111 . ok ( "GenieTv" , '' , '                                 REFRESH SUCCESSFUL :)' , "                          [COLOR gold]Brought To You By Kodi Support Group, GenieTv[/COLOR]" )
 return
 if 54 - 54: OOO0OOo * i1I111ii1II1i * i1I111ii1II1i % I1IiI - i1I111II1I % ii11ii1ii
 if 44 - 44: Oo . i1I111II1I + Oooo0Ooo000
 if 22 - 22: o00OO00OoO * OoooooooOO + i11iIiiIii % Ooo00oOo00o
 if 53 - 53: OOOo0
 if 10 - 10: o00OO00OoO / i11iIiiIii - OoOoOO00
 if 48 - 48: i1I111II1I
 if 26 - 26: i1I111ii1II1i * o00OO00OoO * O0ooOooooO * I1IiI
 if 48 - 48: i1I111ii1II1i % i11iIiiIii . OoooooooOO * OoOo00o % Ooo00oOo00o . i1I111ii1II1i
 if 6 - 6: O0 . OOO0OOo - O0ooOooooO / i11iIiiIii
 if 84 - 84: Oooo0Ooo000 / ii11ii1ii * OOooOOo * Ooo00oOo00o * i1I111II1I * O0
 if 83 - 83: O0 % OoOoOO00 + OOooOOo / OoooooooOO
 if 75 - 75: OoOoOO00 . OOOo0 + i1I111II1I - I1IiI - O0 . Oooo0Ooo000
 if 19 - 19: iI * i1IIi % O0 + Oooo0Ooo000
 if 25 - 25: o00OO00OoO - iI / O0 . OoooooooOO % OOOo0 . i1IIi
 if 19 - 19: OoOoOO00 / OoOoOO00 % ii11ii1ii + O0ooOooooO + O0ooOooooO + i1I111ii1II1i
 if 4 - 4: OOooOOo + Oooo0Ooo000 / i1I111ii1II1i + i1IIi % OOooOOo % i1I111ii1II1i
 if 80 - 80: iI
 if 26 - 26: iIii1I11I1II1 . OoooooooOO - iIii1I11I1II1
 if 59 - 59: ii11ii1ii + Oooo0Ooo000 . O0ooOooooO
 if 87 - 87: Ooo00oOo00o
 if 34 - 34: o00OO00OoO . I1IiI / i11iIiiIii / i1I111ii1II1i
 if 46 - 46: Oo + OoOoOO00 * OOOo0 + i1I111II1I
 if 31 - 31: iI * OOooOOo * iI + Ooo00oOo00o * OOooOOo . o00OO00OoO
 if 89 - 89: OoooooooOO * iI * OOOo0 . OOO0OOo * iI / i1I111ii1II1i
def iioo ( url ) :
 oOo00O000Oo0 = O0Oooo0O ( iiI1IiI + i11I ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 O0o = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( oOo00O000Oo0 )
 for I1iI1iIi111i , url , OOO0000oO , iI1i111I1Ii , oo00o0 in O0o :
  IIIIii ( I1iI1iIi111i , url , 42 , OOO0000oO , iI1i111I1Ii , oo00o0 )
 O00Oo000ooO0 ( 'movies' , 'MAIN' )
 if 48 - 48: i1I111II1I + o00OO00OoO % i1I111II1I
def Ooo0o0000OO ( url ) :
 oOo00O000Oo0 = O0Oooo0O ( iiI1IiI + iIiI1II1I1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 O0o = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( oOo00O000Oo0 )
 for I1iI1iIi111i , url , OOO0000oO , iI1i111I1Ii , oo00o0 in O0o :
  IIIIii ( I1iI1iIi111i , url , 42 , OOO0000oO , iI1i111I1Ii , oo00o0 )
 O00Oo000ooO0 ( 'movies' , 'MAIN' )
 if 92 - 92: OoooooooOO . Ooo00oOo00o / i1I111II1I + Ooo00oOo00o
def ii1Ii11Ii1i ( url ) :
 oOo00O000Oo0 = O0Oooo0O ( iiI1IiI + OooO0O0oo ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 O0o = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( oOo00O000Oo0 )
 for I1iI1iIi111i , url , OOO0000oO , iI1i111I1Ii , oo00o0 in O0o :
  IIIIii ( I1iI1iIi111i , url , 42 , OOO0000oO , iI1i111I1Ii , oo00o0 )
 O00Oo000ooO0 ( 'movies' , 'MAIN' )
 if 64 - 64: I1IiI % I1IiI + OOooOOo + Oo
def OO0oO0Oo ( url ) :
 oOo00O000Oo0 = O0Oooo0O ( iiI1IiI + OoooOO0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 O0o = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( oOo00O000Oo0 )
 for I1iI1iIi111i , url , OOO0000oO , iI1i111I1Ii , oo00o0 in O0o :
  IIIIii ( I1iI1iIi111i , url , 42 , OOO0000oO , iI1i111I1Ii , oo00o0 )
 O00Oo000ooO0 ( 'movies' , 'MAIN' )
 if 69 - 69: OoOoOO00 + i1I111ii1II1i
def oooOOO ( url ) :
 oOo00O000Oo0 = O0Oooo0O ( iiI1IiI + Iii1o00o0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 O0o = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( oOo00O000Oo0 )
 for I1iI1iIi111i , url , OOO0000oO , iI1i111I1Ii , oo00o0 in O0o :
  IIIIii ( I1iI1iIi111i , url , 42 , OOO0000oO , iI1i111I1Ii , oo00o0 )
 O00Oo000ooO0 ( 'movies' , 'MAIN' )
 if 84 - 84: I1IiI - Oo . OOO0OOo . OoOo00o - Oo
def o0Oo0oO00Oooo ( url ) :
 oOo00O000Oo0 = O0Oooo0O ( iiI1IiI + Ii1II1I11i1I ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 O0o = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( oOo00O000Oo0 )
 for I1iI1iIi111i , url , OOO0000oO , iI1i111I1Ii , oo00o0 in O0o :
  IIIIii ( I1iI1iIi111i , url , 42 , OOO0000oO , iI1i111I1Ii , oo00o0 )
 O00Oo000ooO0 ( 'movies' , 'MAIN' )
 if 91 - 91: Ooo00oOo00o / Ooo00oOo00o . OoOoOO00 . OOO0OOo - OOOo0
def iii11OO0oO ( url ) :
 oOo00O000Oo0 = O0Oooo0O ( iiI1IiI + i1i11ii ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 O0o = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( oOo00O000Oo0 )
 for I1iI1iIi111i , url , OOO0000oO , iI1i111I1Ii , oo00o0 in O0o :
  IIIIii ( I1iI1iIi111i , url , 42 , OOO0000oO , iI1i111I1Ii , oo00o0 )
 O00Oo000ooO0 ( 'movies' , 'MAIN' )
 if 86 - 86: ii11ii1ii - i1IIi + Oo * OOOo0 / i11iIiiIii % O0ooOooooO
def i1i1IIi ( url ) :
 oOo00O000Oo0 = O0Oooo0O ( iiI1IiI + o0oo0Ooo0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 O0o = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( oOo00O000Oo0 )
 for I1iI1iIi111i , url , OOO0000oO , iI1i111I1Ii , oo00o0 in O0o :
  IIIIii ( I1iI1iIi111i , url , 42 , OOO0000oO , iI1i111I1Ii , oo00o0 )
 O00Oo000ooO0 ( 'movies' , 'MAIN' )
 if 74 - 74: iI + ii11ii1ii + OOOo0
def i11iII1II1I1 ( url ) :
 oOo00O000Oo0 = O0Oooo0O ( iiI1IiI + iIIi1II1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 O0o = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( oOo00O000Oo0 )
 for I1iI1iIi111i , url , OOO0000oO , iI1i111I1Ii , oo00o0 in O0o :
  IIIIii ( I1iI1iIi111i , url , 42 , OOO0000oO , iI1i111I1Ii , oo00o0 )
 O00Oo000ooO0 ( 'movies' , 'MAIN' )
 if 42 - 42: iIii1I11I1II1 - OOO0OOo - Oooo0Ooo000 - o00OO00OoO
def iIiI11II ( url ) :
 oOo00O000Oo0 = O0Oooo0O ( iiI1IiI + OO0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 O0o = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( oOo00O000Oo0 )
 for I1iI1iIi111i , url , OOO0000oO , iI1i111I1Ii , oo00o0 in O0o :
  IIIIii ( I1iI1iIi111i , url , 5 , OOO0000oO , iI1i111I1Ii , oo00o0 )
 O00Oo000ooO0 ( 'movies' , 'MAIN' )
 if 18 - 18: OOOo0 * OoOo00o / I1IiI / O0ooOooooO / iI * OOO0OOo
 if 51 - 51: O0ooOooooO
 if 34 - 34: I1IiI . i11iIiiIii * i1I111II1I . OOO0OOo * O0 * Ooo00oOo00o
 if 27 - 27: iI . OOooOOo - I1IiI . OoOoOO00 % Oo
 if 83 - 83: Oooo0Ooo000 + O0ooOooooO - iIii1I11I1II1 + OoOoOO00 . i1I111ii1II1i
 if 76 - 76: OoooooooOO
 if 42 - 42: iI * O0 / O0ooOooooO
 if 8 - 8: i1IIi + OoOoOO00 / iI + ii11ii1ii % iI - iIii1I11I1II1
 if 29 - 29: Oo + OoOoOO00
def oOOo00ooO ( ) :
 try :
  if os . path . exists ( oOOoO0 ) == True :
   i1iiIIiiI111 = xbmcgui . Dialog ( )
   if i1iiIIiiI111 . yesno ( "Delete Thumbnails" , "[COLOR gold][B]##########WARNING ANDROID ONLY##########[/B][/COLOR]" , "This feature deletes your thumbnail folder and textures13.db" , "Are you sure you want to do proceed? This Can NOT Be Undone" ) :
    for IiiIIIII1iii , oO00oo0o00o0o , IiIIIIIi in os . walk ( oOOoO0 ) :
     ooOo = 0
     ooOo += len ( IiIIIIIi )
     if ooOo > 0 :
      for i1i1ii in IiIIIIIi :
       os . unlink ( os . path . join ( IiiIIIII1iii , i1i1ii ) )
  OOOoOo0oO0OoO = os . path . join ( OOooO0OOoo , "Textures13.db" )
  os . unlink ( OOOoOo0oO0OoO )
  i1iiIIiiI111 . ok ( "Restart KODI" , "Please restart KODI to rebuild thumbnail library" )
 except :
  i1iiIIiiI111 = xbmcgui . Dialog ( )
  i1iiIIiiI111 . ok ( o0oOoO00o , "Error Deleting Thumbnails please visit Kodi Support Group, GenieTv on facebook" )
 return
 if 18 - 18: o00OO00OoO . OOOo0 + OoOoOO00 / iI % Oo - I1IiI
 if 92 - 92: i1I111ii1II1i * OOooOOo % i1IIi / Oo - OOOo0 . O0
 if 56 - 56: OoOo00o % O0 * i1IIi - OoOoOO00
 if 74 - 74: i1IIi - I1IiI % O0ooOooooO . O0 - OoooooooOO
 if 84 - 84: o00OO00OoO
 if 53 - 53: i1IIi
 if 59 - 59: OOooOOo + OOOo0 % OoooooooOO - iIii1I11I1II1
 if 9 - 9: i1IIi - I1IiI
 if 57 - 57: iIii1I11I1II1 * iI * i1I111ii1II1i / O0ooOooooO
def iIIiII1i1ii ( url ) :
 print '############################################################       DELETING STANDARD CACHE             ###############################################################'
 o00Oo0O = os . path . join ( xbmc . translatePath ( 'special://home' ) , 'cache' )
 if os . path . exists ( o00Oo0O ) == True :
  for IiiIIIII1iii , oO00oo0o00o0o , IiIIIIIi in os . walk ( o00Oo0O ) :
   ooOo = 0
   ooOo += len ( IiIIIIIi )
   if 17 - 17: Ooo00oOo00o
   if 31 - 31: O0ooOooooO + OoooooooOO - iI % OOooOOo / OOooOOo / iIii1I11I1II1
   if ooOo > 0 :
    if 31 - 31: OoooooooOO - iI . OoOo00o % O0ooOooooO
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    if i1iiIIiiI111 . yesno ( "Delete KODI Cache Files" , str ( ooOo ) + " files found" , "Do you want to delete them?" ) :
     if 16 - 16: i1I111II1I * iI % o00OO00OoO / OoOo00o + iIii1I11I1II1 / OOOo0
     for i1i1ii in IiIIIIIi :
      try :
       os . unlink ( os . path . join ( IiiIIIII1iii , i1i1ii ) )
      except :
       pass
     for O0OoO0ooOO0o in oO00oo0o00o0o :
      try :
       shutil . rmtree ( os . path . join ( IiiIIIII1iii , O0OoO0ooOO0o ) )
      except :
       pass
       if 36 - 36: Ooo00oOo00o + Ooo00oOo00o + Ooo00oOo00o % Oo * i1I111ii1II1i
   else :
    pass
 if xbmc . getCondVisibility ( 'system.platform.ATV2' ) :
  O0IIi1i = os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'Other' )
  if 56 - 56: OOooOOo / OoOo00o
  for IiiIIIII1iii , oO00oo0o00o0o , IiIIIIIi in os . walk ( O0IIi1i ) :
   ooOo = 0
   ooOo += len ( IiIIIIIi )
   if 11 - 11: I1IiI / Oooo0Ooo000
   if ooOo > 0 :
    if 47 - 47: i1I111II1I . o00OO00OoO % OoOoOO00 + Oo - O0ooOooooO . OoOoOO00
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    if i1iiIIiiI111 . yesno ( "Delete ATV2 Cache Files" , str ( ooOo ) + " files found in 'Other'" , "Do you want to delete them?" ) :
     if 37 - 37: iIii1I11I1II1 . OOOo0 % Ooo00oOo00o % OoooooooOO . OoooooooOO / O0
     for i1i1ii in IiIIIIIi :
      os . unlink ( os . path . join ( IiiIIIII1iii , i1i1ii ) )
     for O0OoO0ooOO0o in oO00oo0o00o0o :
      shutil . rmtree ( os . path . join ( IiiIIIII1iii , O0OoO0ooOO0o ) )
      if 25 - 25: OoOoOO00 % OoOoOO00 - iI . O0
   else :
    pass
  O00O0 = os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'LocalAndRental' )
  if 19 - 19: OOOo0 + Oooo0Ooo000 % OoOoOO00
  for IiiIIIII1iii , oO00oo0o00o0o , IiIIIIIi in os . walk ( O00O0 ) :
   ooOo = 0
   ooOo += len ( IiIIIIIi )
   if 75 - 75: iIii1I11I1II1
   if ooOo > 0 :
    if 42 - 42: i11iIiiIii + o00OO00OoO - OOooOOo
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    if i1iiIIiiI111 . yesno ( "Delete ATV2 Cache Files" , str ( ooOo ) + " files found in 'LocalAndRental'" , "Do you want to delete them?" ) :
     if 2 - 2: OOooOOo . iI % I1IiI
     for i1i1ii in IiIIIIIi :
      os . unlink ( os . path . join ( IiiIIIII1iii , i1i1ii ) )
     for O0OoO0ooOO0o in oO00oo0o00o0o :
      shutil . rmtree ( os . path . join ( IiiIIIII1iii , O0OoO0ooOO0o ) )
      if 58 - 58: ii11ii1ii % iI * iI - i1I111ii1II1i
   else :
    pass
    if 9 - 9: OOO0OOo - iI % OoOoOO00 + OoOo00o + i1I111II1I % O0
    if 65 - 65: i1I111II1I - Ooo00oOo00o % i11iIiiIii
    if 58 - 58: i1I111ii1II1i
    if 2 - 2: OoOoOO00 + i1IIi
 oO0OO00 = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.whatthefurk/cache' ) , '' )
 if os . path . exists ( oO0OO00 ) == True :
  for IiiIIIII1iii , oO00oo0o00o0o , IiIIIIIi in os . walk ( oO0OO00 ) :
   ooOo = 0
   ooOo += len ( IiIIIIIi )
   if 16 - 16: OoooooooOO / O0ooOooooO . iI * OOO0OOo - OOOo0
   if 32 - 32: OOOo0 / Ooo00oOo00o
   if ooOo > 0 :
    if 28 - 28: Oo / OoOo00o . i1I111ii1II1i + Ooo00oOo00o + Oooo0Ooo000 % Oo
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    if i1iiIIiiI111 . yesno ( "Delete WTF Cache Files" , str ( ooOo ) + " files found" , "Do you want to delete them?" ) :
     if 45 - 45: Oo / O0 % OoooooooOO
     for i1i1ii in IiIIIIIi :
      os . unlink ( os . path . join ( IiiIIIII1iii , i1i1ii ) )
     for O0OoO0ooOO0o in oO00oo0o00o0o :
      shutil . rmtree ( os . path . join ( IiiIIIII1iii , O0OoO0ooOO0o ) )
      if 92 - 92: iI . I1IiI . Oooo0Ooo000 - OoooooooOO / OOO0OOo
   else :
    pass
    if 80 - 80: iIii1I11I1II1 / i11iIiiIii + i1I111ii1II1i
    if 41 - 41: o00OO00OoO + Ooo00oOo00o * OOOo0 * O0 * Oo - I1IiI
 ooooOoo00 = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.4od/cache' ) , '' )
 if os . path . exists ( ooooOoo00 ) == True :
  for IiiIIIII1iii , oO00oo0o00o0o , IiIIIIIi in os . walk ( ooooOoo00 ) :
   ooOo = 0
   ooOo += len ( IiIIIIIi )
   if 7 - 7: i1I111II1I * Ooo00oOo00o + OoooooooOO . OOO0OOo * Oooo0Ooo000
   if 82 - 82: iIii1I11I1II1 * OoooooooOO
   if ooOo > 0 :
    if 50 - 50: o00OO00OoO - OoOoOO00
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    if i1iiIIiiI111 . yesno ( "Delete 4oD Cache Files" , str ( ooOo ) + " files found" , "Do you want to delete them?" ) :
     if 33 - 33: OoOo00o / OoOo00o . i11iIiiIii * ii11ii1ii + OOooOOo
     for i1i1ii in IiIIIIIi :
      os . unlink ( os . path . join ( IiiIIIII1iii , i1i1ii ) )
     for O0OoO0ooOO0o in oO00oo0o00o0o :
      shutil . rmtree ( os . path . join ( IiiIIIII1iii , O0OoO0ooOO0o ) )
      if 16 - 16: OoOo00o
   else :
    pass
    if 10 - 10: I1IiI . OoOo00o * iIii1I11I1II1 - O0ooOooooO - I1IiI / o00OO00OoO
    if 13 - 13: O0ooOooooO + I1IiI % OoOo00o % OoooooooOO
 iiiiI1iiiIi11 = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.iplayer/iplayer_http_cache' ) , '' )
 if os . path . exists ( iiiiI1iiiIi11 ) == True :
  for IiiIIIII1iii , oO00oo0o00o0o , IiIIIIIi in os . walk ( iiiiI1iiiIi11 ) :
   ooOo = 0
   ooOo += len ( IiIIIIIi )
   if 52 - 52: iI * Ooo00oOo00o . ii11ii1ii - o00OO00OoO
   if 4 - 4: i11iIiiIii + OoooooooOO / i11iIiiIii . OoooooooOO % ii11ii1ii / I1IiI
   if ooOo > 0 :
    if 35 - 35: ii11ii1ii % i1IIi + OOooOOo - iIii1I11I1II1
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    if i1iiIIiiI111 . yesno ( "Delete BBC iPlayer Cache Files" , str ( ooOo ) + " files found" , "Do you want to delete them?" ) :
     if 28 - 28: OOOo0 * OoOoOO00 * I1IiI % i1I111II1I - i1I111II1I
     for i1i1ii in IiIIIIIi :
      os . unlink ( os . path . join ( IiiIIIII1iii , i1i1ii ) )
     for O0OoO0ooOO0o in oO00oo0o00o0o :
      shutil . rmtree ( os . path . join ( IiiIIIII1iii , O0OoO0ooOO0o ) )
      if 35 - 35: Oo . OOO0OOo - i1IIi . I1IiI
   else :
    pass
    if 12 - 12: OoOo00o / Ooo00oOo00o / O0 * OoOo00o
    if 51 - 51: OOO0OOo * i1I111ii1II1i / i1IIi
    if 2 - 2: O0ooOooooO + OoOo00o . i1I111ii1II1i - i1IIi + o00OO00OoO
 ooOOo0O0o00o00 = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/script.module.simple.downloader' ) , '' )
 if os . path . exists ( ooOOo0O0o00o00 ) == True :
  for IiiIIIII1iii , oO00oo0o00o0o , IiIIIIIi in os . walk ( ooOOo0O0o00o00 ) :
   ooOo = 0
   ooOo += len ( IiIIIIIi )
   if 90 - 90: o00OO00OoO . OoOoOO00 . ii11ii1ii
   if 32 - 32: OOO0OOo - Ooo00oOo00o . i1I111ii1II1i . i1I111ii1II1i % i1IIi * iI
   if ooOo > 0 :
    if 65 - 65: i1I111ii1II1i / OOO0OOo . OoOoOO00
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    if i1iiIIiiI111 . yesno ( "Delete Simple Downloader Cache Files" , str ( ooOo ) + " files found" , "Do you want to delete them?" ) :
     if 90 - 90: Oooo0Ooo000
     for i1i1ii in IiIIIIIi :
      os . unlink ( os . path . join ( IiiIIIII1iii , i1i1ii ) )
     for O0OoO0ooOO0o in oO00oo0o00o0o :
      shutil . rmtree ( os . path . join ( IiiIIIII1iii , O0OoO0ooOO0o ) )
      if 95 - 95: Ooo00oOo00o
   else :
    pass
    if 68 - 68: iIii1I11I1II1 . iIii1I11I1II1 / I1IiI - OoOoOO00 - iIii1I11I1II1
    if 75 - 75: OOO0OOo . OOOo0 * OoOoOO00
 ooOO0000oo0O = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.itv/Images' ) , '' )
 if os . path . exists ( ooOO0000oo0O ) == True :
  for IiiIIIII1iii , oO00oo0o00o0o , IiIIIIIi in os . walk ( ooOO0000oo0O ) :
   ooOo = 0
   ooOo += len ( IiIIIIIi )
   if 60 - 60: i1I111II1I * OOO0OOo * Ooo00oOo00o
   if 64 - 64: Oooo0Ooo000 / OoOoOO00 / Ooo00oOo00o - OOO0OOo * iIii1I11I1II1 . i1I111ii1II1i
   if ooOo > 0 :
    if 25 - 25: i1I111II1I - iI . Oooo0Ooo000
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    if i1iiIIiiI111 . yesno ( "Delete ITV Cache Files" , str ( ooOo ) + " files found" , "Do you want to delete them?" ) :
     if 57 - 57: OOooOOo + Oo * ii11ii1ii - OOO0OOo % iIii1I11I1II1 - iI
     for i1i1ii in IiIIIIIi :
      os . unlink ( os . path . join ( IiiIIIII1iii , i1i1ii ) )
     for O0OoO0ooOO0o in oO00oo0o00o0o :
      shutil . rmtree ( os . path . join ( IiiIIIII1iii , O0OoO0ooOO0o ) )
      if 37 - 37: Ooo00oOo00o * Oooo0Ooo000 + iI + ii11ii1ii * OOooOOo
   else :
    pass
    if 95 - 95: iI - i11iIiiIii % i11iIiiIii - O0 * o00OO00OoO
    if 81 - 81: OoOoOO00 * OOOo0 % i1IIi * i11iIiiIii + I1IiI
 oo0OoOO000O = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.movies4me/cache' ) , '' )
 if os . path . exists ( ooOO0000oo0O ) == True :
  for IiiIIIII1iii , oO00oo0o00o0o , IiIIIIIi in os . walk ( oo0OoOO000O ) :
   ooOo = 0
   ooOo += len ( IiIIIIIi )
   if 62 - 62: i1IIi * iIii1I11I1II1 % O0ooOooooO % I1IiI / OoooooooOO
   if 39 - 39: Oo % i1I111ii1II1i
   if ooOo > 0 :
    if 90 - 90: OOOo0 * ii11ii1ii . Oooo0Ooo000 * iI - OOooOOo
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    if i1iiIIiiI111 . yesno ( "Delete Movies4me Cache Files" , str ( ooOo ) + " files found" , "Do you want to delete them?" ) :
     if 40 - 40: O0 / OoOo00o - OoOoOO00 + OOooOOo % Oo
     for i1i1ii in IiIIIIIi :
      os . unlink ( os . path . join ( IiiIIIII1iii , i1i1ii ) )
     for O0OoO0ooOO0o in oO00oo0o00o0o :
      shutil . rmtree ( os . path . join ( IiiIIIII1iii , O0OoO0ooOO0o ) )
      if 93 - 93: OOO0OOo
   else :
    pass
    if 82 - 82: ii11ii1ii / OOO0OOo . i11iIiiIii + i1I111II1I - I1IiI / i1I111ii1II1i
    if 99 - 99: O0ooOooooO / i1IIi
 iIoOO0OO00 = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.phstreams/Cache' ) , '' )
 if os . path . exists ( ooOO0000oo0O ) == True :
  for IiiIIIII1iii , oO00oo0o00o0o , IiIIIIIi in os . walk ( iIoOO0OO00 ) :
   ooOo = 0
   ooOo += len ( IiIIIIIi )
   if 75 - 75: i1I111ii1II1i * Oo / o00OO00OoO * Oo / OOO0OOo
   if 14 - 14: i1IIi * iIii1I11I1II1 - iI * I1IiI - i1I111ii1II1i / O0ooOooooO
   if ooOo > 0 :
    if 73 - 73: ii11ii1ii - I1IiI * O0 - I1IiI - Ooo00oOo00o
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    if i1iiIIiiI111 . yesno ( "Delete Phoenix Cache Files" , str ( ooOo ) + " files found" , "Do you want to delete them?" ) :
     if 96 - 96: ii11ii1ii - O0
     for i1i1ii in IiIIIIIi :
      os . unlink ( os . path . join ( IiiIIIII1iii , i1i1ii ) )
     for O0OoO0ooOO0o in oO00oo0o00o0o :
      shutil . rmtree ( os . path . join ( IiiIIIII1iii , O0OoO0ooOO0o ) )
      if 35 - 35: i1I111II1I . Oooo0Ooo000 . o00OO00OoO - Oooo0Ooo000 % Oooo0Ooo000 + o00OO00OoO
   else :
    pass
    if 99 - 99: OOooOOo + i1I111II1I
    if 34 - 34: o00OO00OoO * OOooOOo . OOOo0 % i11iIiiIii
 Oo0OO0 = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.spotitube/cache' ) , '' )
 if os . path . exists ( ooOO0000oo0O ) == True :
  for IiiIIIII1iii , oO00oo0o00o0o , IiIIIIIi in os . walk ( Oo0OO0 ) :
   ooOo = 0
   ooOo += len ( IiIIIIIi )
   if 74 - 74: iI - OoooooooOO
   if 19 - 19: iIii1I11I1II1 + o00OO00OoO . o00OO00OoO - Oo
   if ooOo > 0 :
    if 41 - 41: OOOo0 . Oo . OoOo00o % OoooooooOO + Ooo00oOo00o
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    if i1iiIIiiI111 . yesno ( "Delete YouTube Music Cache Files" , str ( ooOo ) + " files found" , "Do you want to delete them?" ) :
     if 23 - 23: OOOo0 - OOooOOo % O0ooOooooO . O0 * OoooooooOO + OOO0OOo
     for i1i1ii in IiIIIIIi :
      os . unlink ( os . path . join ( IiiIIIII1iii , i1i1ii ) )
     for O0OoO0ooOO0o in oO00oo0o00o0o :
      shutil . rmtree ( os . path . join ( IiiIIIII1iii , O0OoO0ooOO0o ) )
      if 53 - 53: Oo
   else :
    pass
    if 3 - 3: OoOo00o - OoooooooOO * OoooooooOO - OOOo0 / o00OO00OoO * ii11ii1ii
    if 58 - 58: OoOo00o % iIii1I11I1II1 / i11iIiiIii % OOooOOo . o00OO00OoO * i1I111ii1II1i
 iiI1II = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.supercartoons/cache' ) , '' )
 if os . path . exists ( ooOO0000oo0O ) == True :
  for IiiIIIII1iii , oO00oo0o00o0o , IiIIIIIi in os . walk ( iiI1II ) :
   ooOo = 0
   ooOo += len ( IiIIIIIi )
   if 100 - 100: o00OO00OoO * Oo - iIii1I11I1II1 + OOOo0 - i1IIi + i1I111ii1II1i
   if 19 - 19: o00OO00OoO + i1I111ii1II1i * o00OO00OoO
   if ooOo > 0 :
    if 71 - 71: OOooOOo . OOOo0 - ii11ii1ii - Oo - i1IIi - OOOo0
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    if i1iiIIiiI111 . yesno ( "Delete SuperCartoons Cache Files" , str ( ooOo ) + " files found" , "Do you want to delete them?" ) :
     if 45 - 45: Ooo00oOo00o * Ooo00oOo00o
     for i1i1ii in IiIIIIIi :
      os . unlink ( os . path . join ( IiiIIIII1iii , i1i1ii ) )
     for O0OoO0ooOO0o in oO00oo0o00o0o :
      shutil . rmtree ( os . path . join ( IiiIIIII1iii , O0OoO0ooOO0o ) )
      if 9 - 9: iIii1I11I1II1
   else :
    pass
    if 57 - 57: OOO0OOo / iI % OOooOOo % i11iIiiIii
    if 95 - 95: o00OO00OoO - OOooOOo
 Oooo0o00 = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.tvonline.cc/cache' ) , '' )
 if os . path . exists ( ooOO0000oo0O ) == True :
  for IiiIIIII1iii , oO00oo0o00o0o , IiIIIIIi in os . walk ( Oooo0o00 ) :
   ooOo = 0
   ooOo += len ( IiIIIIIi )
   if 74 - 74: Oo / o00OO00OoO % o00OO00OoO . OoOo00o
   if 72 - 72: i1IIi
   if ooOo > 0 :
    if 21 - 21: o00OO00OoO . i1I111II1I / i11iIiiIii * i1IIi
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    if i1iiIIiiI111 . yesno ( "Delete TVonline Cache Files" , str ( ooOo ) + " files found" , "Do you want to delete them?" ) :
     if 82 - 82: OOO0OOo * Oo % i11iIiiIii * i1IIi . i1I111II1I
     for i1i1ii in IiIIIIIi :
      os . unlink ( os . path . join ( IiiIIIII1iii , i1i1ii ) )
     for O0OoO0ooOO0o in oO00oo0o00o0o :
      shutil . rmtree ( os . path . join ( IiiIIIII1iii , O0OoO0ooOO0o ) )
      if 89 - 89: OoOo00o - i1IIi - OoOo00o
   else :
    pass
    if 74 - 74: Ooo00oOo00o % Ooo00oOo00o
    if 28 - 28: I1IiI % O0ooOooooO - i1I111II1I + i1I111II1I + O0ooOooooO / iIii1I11I1II1
 oo0o = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.youtube/kodion' ) , '' )
 if os . path . exists ( ooOO0000oo0O ) == True :
  for IiiIIIII1iii , oO00oo0o00o0o , IiIIIIIi in os . walk ( oo0o ) :
   ooOo = 0
   ooOo += len ( IiIIIIIi )
   if 69 - 69: OOooOOo + ii11ii1ii / iIii1I11I1II1 . OoOo00o % ii11ii1ii * I1IiI
   if 13 - 13: iIii1I11I1II1 + i1I111ii1II1i / iI / i1IIi % Ooo00oOo00o - iIii1I11I1II1
   if ooOo > 0 :
    if 60 - 60: o00OO00OoO
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    if i1iiIIiiI111 . yesno ( "Delete YouTube Cache Files" , str ( ooOo ) + " files found" , "Do you want to delete them?" ) :
     if 77 - 77: OOOo0 / ii11ii1ii
     for i1i1ii in IiIIIIIi :
      os . unlink ( os . path . join ( IiiIIIII1iii , i1i1ii ) )
     for O0OoO0ooOO0o in oO00oo0o00o0o :
      shutil . rmtree ( os . path . join ( IiiIIIII1iii , O0OoO0ooOO0o ) )
      if 95 - 95: o00OO00OoO * i1IIi + O0ooOooooO
   else :
    pass
    if 40 - 40: OoOoOO00
    if 7 - 7: i1I111II1I / Ooo00oOo00o
    if 88 - 88: i1IIi
 O0ooOo0Oooo = xbmc . translatePath ( 'special://masterprofile/addon_data/plugin.video.genesis' )
 i1iiIIiiI111 = xbmcgui . Dialog ( )
 try :
  if i1iiIIiiI111 . yesno ( "Delete Genesis Cache Files" , "Do you want to delete cache" ) :
   I1iiIIiI11I = os . path . join ( O0ooOo0Oooo , "cache.db" )
   os . unlink ( I1iiIIiI11I )
   if 29 - 29: Oooo0Ooo000 + O0ooOooooO % OOO0OOo + I1IiI
 except :
  pass
  if 92 - 92: OOooOOo
 i1iiIIiiI111 = xbmcgui . Dialog ( )
 i1iiIIiiI111 . ok ( "GenieTv" , "                               Finished Deleting Cache " , "                          [COLOR gold]Brought To You By GenieTv[/COLOR]" )
 if 37 - 37: O0ooOooooO
 if 18 - 18: OoOo00o * i11iIiiIii + iIii1I11I1II1 % Oooo0Ooo000 + i1IIi - Ooo00oOo00o
 if 85 - 85: Ooo00oOo00o * Oooo0Ooo000 + Ooo00oOo00o
 if 39 - 39: Oo / i1IIi % i1IIi
 if 20 - 20: i1I111II1I * O0ooOooooO
 if 91 - 91: Ooo00oOo00o % i1IIi - iIii1I11I1II1 . i1I111II1I
 if 31 - 31: O0ooOooooO % i1IIi . OoooooooOO - OOooOOo + OoooooooOO
 if 45 - 45: i1I111II1I + Oooo0Ooo000 / OoooooooOO - iI + OoooooooOO
 if 42 - 42: iIii1I11I1II1 * OOOo0 * o00OO00OoO
def O00oo0o0o0oo ( url ) :
 print '###' + o0oOoO00o + ' - DELETING PACKAGES###'
 I1I1I1 = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' , '' ) )
 try :
  for IiiIIIII1iii , oO00oo0o00o0o , IiIIIIIi in os . walk ( I1I1I1 ) :
   ooOo = 0
   ooOo += len ( IiIIIIIi )
   if 29 - 29: ii11ii1ii
   if 91 - 91: Ooo00oOo00o
   if ooOo > 0 :
    if 54 - 54: ii11ii1ii . OOO0OOo + o00OO00OoO % OOO0OOo
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    if i1iiIIiiI111 . yesno ( "Delete Package Cache Files" , str ( ooOo ) + " files found" , "Do you want to delete them?" ) :
     if 67 - 67: Ooo00oOo00o
     for i1i1ii in IiIIIIIi :
      os . unlink ( os . path . join ( IiiIIIII1iii , i1i1ii ) )
     for O0OoO0ooOO0o in oO00oo0o00o0o :
      shutil . rmtree ( os . path . join ( IiiIIIII1iii , O0OoO0ooOO0o ) )
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
 if 76 - 76: Oo
 if 38 - 38: i1I111II1I . i1I111ii1II1i
 if 94 - 94: OoOo00o / o00OO00OoO * OoOo00o - OOO0OOo
 if 89 - 89: iIii1I11I1II1
 if 31 - 31: OOO0OOo . i1I111II1I % OOO0OOo
 if 33 - 33: O0 * iI - OoOo00o . OoooooooOO + OoOo00o
 if 20 - 20: o00OO00OoO - I1IiI
 if 91 - 91: i1IIi
 if 31 - 31: i11iIiiIii + iI % I1IiI
def I1Io0Oo00 ( url ) :
 print '###' + o0oOoO00o + ' - DELETING PACKAGES###'
 I1I1I1 = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' , '' ) )
 try :
  for IiiIIIII1iii , oO00oo0o00o0o , IiIIIIIi in os . walk ( I1I1I1 ) :
   ooOo = 0
   ooOo += len ( IiIIIIIi )
   if 34 - 34: iI * OOOo0 + Oooo0Ooo000 * I1IiI - OoOoOO00
   if 92 - 92: i1I111II1I . OOooOOo / i1I111ii1II1i . iIii1I11I1II1 % Oo . OoooooooOO
   if ooOo > 0 :
    if 81 - 81: i11iIiiIii * i1I111ii1II1i . O0ooOooooO * O0ooOooooO . OoOo00o
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    if i1iiIIiiI111 . yesno ( "Delete Package Cache Files" , str ( ooOo ) + " files found" , "Do you want to delete them?" ) :
     if 47 - 47: iIii1I11I1II1 % Oooo0Ooo000 . Oooo0Ooo000 / O0 . i11iIiiIii * iI
     for i1i1ii in IiIIIIIi :
      os . unlink ( os . path . join ( IiiIIIII1iii , i1i1ii ) )
     for O0OoO0ooOO0o in oO00oo0o00o0o :
      shutil . rmtree ( os . path . join ( IiiIIIII1iii , O0OoO0ooOO0o ) )
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
 iIIiII1i1ii ( url )
 if 24 - 24: O0
 if 33 - 33: OoooooooOO + O0ooOooooO * OoOoOO00 / i1I111II1I
 if 87 - 87: OoooooooOO
 if 1 - 1: iIii1I11I1II1 / OOooOOo
 if 98 - 98: O0 % OOOo0 / OoooooooOO * ii11ii1ii - O0ooOooooO
 if 51 - 51: i1I111ii1II1i + Oooo0Ooo000
 if 54 - 54: OoOoOO00 * O0 % OOOo0 . Oooo0Ooo000
 if 62 - 62: iI . i11iIiiIii % O0 % o00OO00OoO - Oo
 if 69 - 69: OoOoOO00 . I1IiI * I1IiI % iI + OOOo0
def ooOOO000O ( url , name ) :
 O0O0Oo00 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 o0Oi1IIi = os . path . join ( O0O0Oo00 , 'advancedsettings.xml' )
 i1iiIIiiI111 = xbmcgui . Dialog ( )
 OOoo = os . path . join ( O0O0Oo00 , 'advancedsettings.xml.bak' )
 if os . path . exists ( OOoo ) == False :
  if i1iiIIiiI111 . yesno ( "Back Up Original" , 'Have You Backed Up Your Original?' , '' , "[B][COLOR red]     AS YOU CANNOT GO BACK !!![/B][/COLOR]" ) :
   print '###' + o0oOoO00o + ' - ADVANCED XML###'
   O0O0Oo00 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
   o0Oi1IIi = os . path . join ( O0O0Oo00 , 'advancedsettings.xml' )
   try :
    os . remove ( o0Oi1IIi )
    print '=== GenieTv - REMOVING    ' + str ( o0Oi1IIi ) + '    ==='
   except :
    pass
   oOo00O000Oo0 = i1 . http_GET ( url ) . content
   iII1ii1 = open ( o0Oi1IIi , "w" )
   iII1ii1 . write ( oOo00O000Oo0 )
   iII1ii1 . close ( )
   print '=== GenieTv - WRITING NEW    ' + str ( o0Oi1IIi ) + '    ==='
   i1iiIIiiI111 = xbmcgui . Dialog ( )
   i1iiIIiiI111 . ok ( o0oOoO00o , "       Done Adding new Advanced XML" )
 else :
  print '###' + o0oOoO00o + ' - ADVANCED XML###'
  O0O0Oo00 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
  o0Oi1IIi = os . path . join ( O0O0Oo00 , 'advancedsettings.xml' )
  try :
   os . remove ( o0Oi1IIi )
   print '=== GenieTv - REMOVING    ' + str ( o0Oi1IIi ) + '    ==='
  except :
   pass
  oOo00O000Oo0 = i1 . http_GET ( url ) . content
  iII1ii1 = open ( o0Oi1IIi , "w" )
  iII1ii1 . write ( oOo00O000Oo0 )
  iII1ii1 . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( o0Oi1IIi ) + '    ==='
  i1iiIIiiI111 = xbmcgui . Dialog ( )
  i1iiIIiiI111 . ok ( o0oOoO00o , "       Done Adding new Advanced XML" )
 return
 if 40 - 40: OOOo0
def i1IiI ( url , name ) :
 print '###' + o0oOoO00o + ' - CHECK ADVANCE XML###'
 O0O0Oo00 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 o0Oi1IIi = os . path . join ( O0O0Oo00 , 'advancedsettings.xml' )
 try :
  iII1ii1 = open ( o0Oi1IIi ) . read ( )
  if 'zero' in iII1ii1 :
   name = '0CACHE'
  elif 'tuxen' in iII1ii1 :
   name = 'TUXENS'
  elif 'muckys' in iII1ii1 :
   name = 'MUCKYS'
  elif 'p2p1' in iII1ii1 :
   name = '1st P2P RECOMMENDED'
  elif 'p2p2' in iII1ii1 :
   name = '2nd P2P RECOMMENDED'
  elif 'mikey' in iII1ii1 :
   name = 'MIKEY1234'
 except :
  name = "NO ADVANCED"
 i1iiIIiiI111 = xbmcgui . Dialog ( )
 i1iiIIiiI111 . ok ( o0oOoO00o , "[COLOR yellow]YOU HAVE[/COLOR] " + name + "[COLOR yellow] XML SETTINGS SETUP[/COLOR]" )
 return
 if 73 - 73: OoooooooOO * O0 * OOO0OOo
def iii11Ii ( url ) :
 print '###' + o0oOoO00o + ' - DELETING ADVANCE XML###'
 O0O0Oo00 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 o0Oi1IIi = os . path . join ( O0O0Oo00 , 'advancedsettings.xml' )
 try :
  os . remove ( o0Oi1IIi )
  i1iiIIiiI111 = xbmcgui . Dialog ( )
  print '=== GenieTv - DELETING    ' + str ( o0Oi1IIi ) + '    ==='
  i1iiIIiiI111 . ok ( o0oOoO00o , "       Remove Advanced Settings Sucessfull" )
 except :
  i1iiIIiiI111 = xbmcgui . Dialog ( )
  i1iiIIiiI111 . ok ( o0oOoO00o , "       No Advanced Settings To Remove" )
 return
 if 31 - 31: O0ooOooooO
 if 69 - 69: iIii1I11I1II1 . Oooo0Ooo000 / i1I111ii1II1i
 if 87 - 87: O0 * Ooo00oOo00o + i1IIi
 if 33 - 33: OOOo0 * o00OO00OoO
 if 98 - 98: ii11ii1ii - OoooooooOO / OOOo0 . OOO0OOo - i1IIi
 if 60 - 60: I1IiI % I1IiI
 if 2 - 2: iI . O0 - O0ooOooooO + OoOo00o
 if 96 - 96: iI + iI
 if 28 - 28: i1I111ii1II1i
 if 6 - 6: OOOo0 - i1I111ii1II1i
def ii1II ( url = 'http://www.iplocation.net/' , inc = 1 ) :
 O0o = re . compile ( "<td width='80'>(.+?)</td><td>(.+?)</td><td>(.+?)</td><td>.+?</td><td>(.+?)</td>" ) . findall ( i1 . http_GET ( url ) . content )
 for OOo00o0o0O0oo , i1iI1iIII , oo0Oo , I1IiIIIIi1iiI in O0o :
  if inc < 2 : i1iiIIiiI111 = xbmcgui . Dialog ( ) ; i1iiIIiiI111 . ok ( 'Check My IP' , "[B][COLOR gold]Your IP Address is: [/COLOR][/B] %s" % OOo00o0o0O0oo , '[B][COLOR gold]Your IP is based in: [/COLOR][/B] %s' % oo0Oo , '[B][COLOR gold]Your Service Provider is:[/COLOR][/B] %s' % I1IiIIIIi1iiI )
  inc = inc + 1
  if 57 - 57: Oooo0Ooo000 . O0 . OoooooooOO . o00OO00OoO - iI / OOO0OOo
  if 34 - 34: I1IiI % OOooOOo - O0ooOooooO
  if 40 - 40: i1I111ii1II1i
  if 82 - 82: o00OO00OoO . i1IIi / O0ooOooooO
  if 56 - 56: i1I111ii1II1i
  if 23 - 23: i1IIi
  if 24 - 24: OoOo00o
  if 51 - 51: i1I111II1I % i11iIiiIii
  if 77 - 77: i1I111II1I % i11iIiiIii - ii11ii1ii
def I1oooO00oOOooO ( url , name ) :
 i1iiIIiiI111 = xbmcgui . Dialog ( )
 if i1iiIIiiI111 . yesno ( "GenieTv" , '                                    Install Latest .ini File' ) :
  print '###' + o0oOoO00o + ' - CUSTOM FTV INI###'
  O0O0Oo00 = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/plugin.video.GenieTv' , '' ) )
  o0Oi1IIi = os . path . join ( O0O0Oo00 , 'addons2.ini' )
  oOo00O000Oo0 = i1 . http_GET ( url ) . content
  iII1ii1 = open ( o0Oi1IIi , "w" )
  iII1ii1 . write ( oOo00O000Oo0 )
  iII1ii1 . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( o0Oi1IIi ) + '    ==='
  i1iiIIiiI111 = xbmcgui . Dialog ( )
  i1iiIIiiI111 . ok ( o0oOoO00o , "                               Done Adding New .ini File" )
 return
 if 34 - 34: iIii1I11I1II1 / OoOoOO00
def IIIii111i ( url , name ) :
 i1iiIIiiI111 = xbmcgui . Dialog ( )
 if i1iiIIiiI111 . yesno ( "GenieTv" , '                               Install Custom Settings' ) :
  print '###' + o0oOoO00o + ' - CUSTOM FTV SETTINGS###'
  O0O0Oo00 = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/plugin.video.GenieTv' , '' ) )
  o0Oi1IIi = os . path . join ( O0O0Oo00 , 'settings.xml' )
  oOo00O000Oo0 = i1 . http_GET ( url ) . content
  iII1ii1 = open ( o0Oi1IIi , "w" )
  iII1ii1 . write ( oOo00O000Oo0 )
  iII1ii1 . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( o0Oi1IIi ) + '    ==='
  i1iiIIiiI111 = xbmcgui . Dialog ( )
  i1iiIIiiI111 . ok ( o0oOoO00o , "                               Done Adding New Settings" )
 return
 if 58 - 58: i1I111II1I % i1I111ii1II1i * O0 + ii11ii1ii - OoOo00o
 if 26 - 26: i1IIi / OOOo0 / Oooo0Ooo000 + Oooo0Ooo000
def i1II111iiii ( ) :
 try :
  iiI11 = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/plugin.video.GenieTv' , '' ) )
  if os . path . exists ( iiI11 ) == True :
   i1iiIIiiI111 = xbmcgui . Dialog ( )
   if i1iiIIiiI111 . yesno ( "GenieTv" , "                               Delete FTV Guide Database" ) :
    i11IiIiii = os . path . join ( iiI11 , "source.db" )
    os . unlink ( i11IiIiii )
  i1iiIIiiI111 . ok ( "GenieTv" , "                                     FTV Database Reset" )
 except :
  i1iiIIiiI111 = xbmcgui . Dialog ( )
  i1iiIIiiI111 . ok ( o0oOoO00o , "               Error Deleting Database No Database To Delete" )
 return
 if 15 - 15: OOO0OOo * iIii1I11I1II1 * O0ooOooooO
 if 96 - 96: o00OO00OoO * iIii1I11I1II1 / I1IiI % i1I111II1I * OoOoOO00
 if 3 - 3: i1I111II1I . Oo / i11iIiiIii + Ooo00oOo00o
 if 47 - 47: OoOo00o . i1I111II1I
 if 96 - 96: Oooo0Ooo000 % OoOoOO00 / OOO0OOo % i1I111II1I / OOO0OOo % i11iIiiIii
def O0Oooo0O ( url ) :
 ooooo0o0oo0Ooo = urllib2 . Request ( url )
 ooooo0o0oo0Ooo . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
 iI1i = urllib2 . urlopen ( ooooo0o0oo0Ooo )
 oOo00O000Oo0 = iI1i . read ( )
 iI1i . close ( )
 return oOo00O000Oo0
 if 57 - 57: Oooo0Ooo000 - Oooo0Ooo000 % OoOoOO00 % Oo . OOooOOo % Oo
 if 91 - 91: OOOo0 - Ooo00oOo00o - Oo - iI * iIii1I11I1II1
 if 68 - 68: Ooo00oOo00o % O0 * iIii1I11I1II1 / O0ooOooooO * OOooOOo + i1I111II1I
 if 89 - 89: OOO0OOo * OOOo0 . O0ooOooooO
 if 75 - 75: OOO0OOo - i1I111ii1II1i % i1I111ii1II1i + OOO0OOo * OOooOOo - ii11ii1ii
 if 26 - 26: Oooo0Ooo000 * iI % OOOo0 + i1I111ii1II1i
 if 38 - 38: i1I111ii1II1i - Oo / iI + O0ooOooooO . i1I111ii1II1i + OoOo00o
def iIiii1iI1Ii ( params ) :
 plugintools . log ( "freshstart.main_list " + repr ( params ) ) ; ooIi = plugintools . message_yes_no ( o0oOoO00o , "Do you wish to restore your" , "Kodi configuration to default settings?" )
 if ooIi :
  oO0oOo = xbmcaddon . Addon ( id = o00 ) . getAddonInfo ( 'path' ) ; oO0oOo = xbmc . translatePath ( oO0oOo ) ;
  IIiIiii = os . path . join ( oO0oOo , ".." , ".." ) ; IIiIiii = os . path . abspath ( IIiIiii ) ; plugintools . log ( "freshstart.main_list xbmcPath=" + IIiIiii ) ; OOo0OO = False
  try :
   for IiiIIIII1iii , oO00oo0o00o0o , IiIIIIIi in os . walk ( IIiIiii , topdown = True ) :
    oO00oo0o00o0o [ : ] = [ O0OoO0ooOO0o for O0OoO0ooOO0o in oO00oo0o00o0o if O0OoO0ooOO0o not in iiIIIII1i1iI ]
    for I1iI1iIi111i in IiIIIIIi :
     try : os . remove ( os . path . join ( IiiIIIII1iii , I1iI1iIi111i ) )
     except :
      if I1iI1iIi111i not in [ "Addons15.db" , "MyVideos75.db" , "Textures13.db" , "xbmc.log" ] : OOo0OO = True
      plugintools . log ( "Error removing " + IiiIIIII1iii + " " + I1iI1iIi111i )
    for I1iI1iIi111i in oO00oo0o00o0o :
     try : os . rmdir ( os . path . join ( IiiIIIII1iii , I1iI1iIi111i ) )
     except :
      if I1iI1iIi111i not in [ "Database" , "userdata" ] : OOo0OO = True
      plugintools . log ( "Error removing " + IiiIIIII1iii + " " + I1iI1iIi111i )
   if not OOo0OO : plugintools . log ( "freshstart.main_list All user files removed, you now have a clean install" ) ; plugintools . message ( o0oOoO00o , "The process is complete, you're now back to a fresh Kodi configuration with GenieTv!" , "Please reboot your system or restart Kodi in order for the changes to be applied." )
   else : plugintools . log ( "freshstart.main_list User files partially removed" ) ; plugintools . message ( o0oOoO00o , "The process is complete, you're now back to a fresh Kodi configuration with GenieTv" , "Please reboot your system or restart Kodi in order for the changes to be applied." )
  except : plugintools . message ( o0oOoO00o , "Problem found" , "Your settings has not been changed" ) ; import traceback ; plugintools . log ( traceback . format_exc ( ) ) ; plugintools . log ( "freshstart.main_list NOT removed" )
  plugintools . add_item ( action = "" , title = "Now Exit Kodi" , folder = False )
 else : plugintools . message ( o0oOoO00o , "Your settings" , "has not been changed" ) ; plugintools . add_item ( action = "" , title = "Done" , folder = False )
 oOOiiiIIiIi ( )
 if 98 - 98: i11iIiiIii . o00OO00OoO + I1IiI
 if 55 - 55: Oooo0Ooo000
 if 72 - 72: Oooo0Ooo000 + OOO0OOo / OOOo0 . OoOo00o % Ooo00oOo00o / i11iIiiIii
def I1III1I1IiI ( ) :
 ooooooo0oOo0 = [ ]
 OooO00oO00o = sys . argv [ 2 ]
 if len ( OooO00oO00o ) >= 2 :
  IIII1iI1IiIiI = sys . argv [ 2 ]
  i1II1 = IIII1iI1IiIiI . replace ( '?' , '' )
  if ( IIII1iI1IiIiI [ len ( IIII1iI1IiIiI ) - 1 ] == '/' ) :
   IIII1iI1IiIiI = IIII1iI1IiIiI [ 0 : len ( IIII1iI1IiIiI ) - 2 ]
  OoOoOoo0oOOooo0o = i1II1 . split ( '&' )
  ooooooo0oOo0 = { }
  for IiIi1iI11 in range ( len ( OoOoOoo0oOOooo0o ) ) :
   III = { }
   III = OoOoOoo0oOOooo0o [ IiIi1iI11 ] . split ( '=' )
   if ( len ( III ) ) == 2 :
    ooooooo0oOo0 [ III [ 0 ] ] = III [ 1 ]
    if 1 - 1: o00OO00OoO . i1I111ii1II1i * I1IiI / O0 + O0ooOooooO + OOooOOo
 return ooooooo0oOo0
 if 81 - 81: iIii1I11I1II1
iIi1i = base64 . decodestring ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20v' )
I1iIII1 = base64 . decodestring ( 'L3N0b3JhZ2UvZW11bGF0ZWQvMA==' )
i1ii = base64 . decodestring ( 'L2dlbmllLnR4dA==' )
OO = base64 . decodestring ( 'LmFyY2hpdGVjdHMueDEwaG9zdC5jb20vdGVzdC93aC50eHQ=' )
I1iI1I1I1i11i = base64 . decodestring ( 'aHR0cDovL2ZpeGVzLmFyY2hpdGVjdHMueDEwaG9zdC5jb20vZml4ZXMudHh0' )
O00OiI = base64 . decodestring ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vYXBwcy9hcHBzLnhtbA==' )
i11I = base64 . decodestring ( 'L2FkZG9ucy9uZXcudHh0' )
O0o00oO00O0 = base64 . decodestring ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vdm9kL3ZvZC5waHA=' )
iIiI1II1I1 = base64 . decodestring ( 'L2FkZG9ucy9pcHR2LnR4dA==' )
OooO0O0oo = base64 . decodestring ( 'L2FkZG9ucy92aWRlby50eHQ=' )
OoooOO0 = base64 . decodestring ( 'L2FkZG9ucy9zcG9ydHMudHh0' )
Iii1o00o0 = base64 . decodestring ( 'L2FkZG9ucy9raWRzLnR4dA==' )
Ii1II1I11i1I = base64 . decodestring ( 'L2FkZG9ucy9tdXNpYy50eHQ=' )
i1i11ii = base64 . decodestring ( 'L2FkZG9ucy9wcm9ncmFtcy50eHQ=' )
o0oo0Ooo0 = base64 . decodestring ( 'L2FkZG9ucy94eHgudHh0' )
iIIi1II1 = base64 . decodestring ( 'L2FkZG9ucy9yZXBvLnR4dA==' )
o000O000 = base64 . decodestring ( 'L2FkZG9ucy9wYWNrcy50eHQ=' )
I1Iii = base64 . decodestring ( 'L2FkZG9ucy9za2lucy50eHQ=' )
I1IIIiii1 = base64 . decodestring ( 'L2FkZG9ucy9hcnQudHh0' )
Ii1ii111i1 = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2dvdGhhbS50eHQ=' )
oOo00 = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2hlbGl4LnR4dA==' )
Oo000o = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2lzZW5nYXJkLnR4dA==' )
OO0 = base64 . decodestring ( 'L2FkZG9ucy9SU1MudHh0' )
O0OO0 = base64 . decodestring ( 'Q1VOVA==' )
def IIIIii ( name , url , mode , iconimage , fanart , description , showcontext = True , allinfo = { } ) :
 o0OOOOO0O = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 I1I1IiIi1 = True
 oOO0o0oo0 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 oOO0o0oo0 . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 oOO0o0oo0 . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  IiiIIIIi = [ ]
  if showcontext == 'fav' :
   IiiIIIIi . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in oOoOooOo0o0 :
   IiiIIIIi . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fanart=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , urllib . quote_plus ( fanart ) , mode ) ) )
  oOO0o0oo0 . addContextMenuItems ( IiiIIIIi )
 I1I1IiIi1 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = o0OOOOO0O , listitem = oOO0o0oo0 , isFolder = True )
 return I1I1IiIi1
 if 9 - 9: O0ooOooooO . Oo + i1I111ii1II1i + OOOo0 * OOOo0 - OOOo0
def I1I1IiI1 ( name , url , mode , iconimage , fanart , description ) :
 o0OOOOO0O = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 I1I1IiIi1 = True
 oOO0o0oo0 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 oOO0o0oo0 . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 oOO0o0oo0 . setProperty ( "Fanart_Image" , fanart )
 I1I1IiIi1 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = o0OOOOO0O , listitem = oOO0o0oo0 , isFolder = False )
 return I1I1IiIi1
 if 95 - 95: OoOo00o + i1I111II1I % O0ooOooooO * i1I111II1I
 if 58 - 58: I1IiI . OOooOOo + O0ooOooooO
IIII1iI1IiIiI = I1III1I1IiI ( )
oOo0 = None
I1iI1iIi111i = None
OooOo000OOOOo = None
OOO0000oO = None
iI1i111I1Ii = None
oo00o0 = None
iiIi1 = None
if 91 - 91: OOOo0 + OOooOOo % OoOoOO00 + Ooo00oOo00o
if 66 - 66: iIii1I11I1II1 * OoOoOO00 % Oo % OOOo0 - iI
try :
 iiIi1 = int ( IIII1iI1IiIiI [ "fav_mode" ] )
except :
 pass
 if 59 - 59: OoOo00o % O0ooOooooO
try :
 oOo0 = urllib . unquote_plus ( IIII1iI1IiIiI [ "url" ] )
except :
 pass
try :
 I1iI1iIi111i = urllib . unquote_plus ( IIII1iI1IiIiI [ "name" ] )
except :
 pass
try :
 OOO0000oO = urllib . unquote_plus ( IIII1iI1IiIiI [ "iconimage" ] )
except :
 pass
try :
 OooOo000OOOOo = int ( IIII1iI1IiIiI [ "mode" ] )
except :
 pass
try :
 iI1i111I1Ii = urllib . unquote_plus ( IIII1iI1IiIiI [ "fanart" ] )
except :
 pass
try :
 oo00o0 = urllib . unquote_plus ( IIII1iI1IiIiI [ "description" ] )
except :
 pass
 if 21 - 21: OoooooooOO % I1IiI - I1IiI / ii11ii1ii / OOooOOo
 if 15 - 15: OOO0OOo / OOO0OOo % OoooooooOO . o00OO00OoO
print str ( O0OoO000O0OO ) + ': ' + str ( O00ooOO )
print "Mode: " + str ( OooOo000OOOOo )
print "URL: " + str ( oOo0 )
print "Name: " + str ( I1iI1iIi111i )
print "IconImage: " + str ( OOO0000oO )
if 93 - 93: ii11ii1ii * ii11ii1ii / OoooooooOO
if 6 - 6: ii11ii1ii * Oo + iIii1I11I1II1
def O00Oo000ooO0 ( content , viewType ) :
 if 19 - 19: O0 % OoOoOO00 * OOooOOo
 if content :
  xbmcplugin . setContent ( int ( sys . argv [ 1 ] ) , content )
 if o0oO0 . getSetting ( 'auto-view' ) == 'true' :
  xbmc . executebuiltin ( "Container.SetViewMode(%s)" % o0oO0 . getSetting ( viewType ) )
  if 27 - 27: i1I111II1I * OoOo00o / i11iIiiIii - O0ooOooooO + OoOoOO00
  if 43 - 43: ii11ii1ii - OoOoOO00
if OooOo000OOOOo == None :
 o0OOoo0OO0OOO ( )
 if 56 - 56: ii11ii1ii . i1IIi / i1I111ii1II1i % O0ooOooooO / O0 * Oooo0Ooo000
elif OooOo000OOOOo == 1 :
 Iii ( oOo0 )
 if 98 - 98: O0 + i1I111ii1II1i
elif OooOo000OOOOo == 44 :
 ii1i1i1IiII ( oOo0 )
 if 23 - 23: OoooooooOO . iIii1I11I1II1 / i1IIi
elif OooOo000OOOOo == 2 :
 Ii1IiI1i1ii ( )
 if 31 - 31: Oo - iIii1I11I1II1 / Oooo0Ooo000 . Ooo00oOo00o
elif OooOo000OOOOo == 3 :
 oo00O00oO000o ( )
 if 74 - 74: Oo - OoOoOO00 - OoOo00o
elif OooOo000OOOOo == 21 :
 iI1Ii11111iIi ( )
 if 50 - 50: OOOo0 - O0ooOooooO + O0ooOooooO * Oooo0Ooo000 + O0ooOooooO
elif OooOo000OOOOo == 4 :
 I1I11iI11iI1i ( )
 if 70 - 70: i1IIi % Ooo00oOo00o / i1IIi
elif OooOo000OOOOo == 5 :
 IioO0O ( I1iI1iIi111i , oOo0 , oo00o0 )
 if 30 - 30: I1IiI - i11iIiiIii
elif OooOo000OOOOo == 6 :
 O00oo0o0o0oo ( oOo0 )
 if 94 - 94: I1IiI % i1I111ii1II1i
elif OooOo000OOOOo == 7 :
 ooOOO000O ( oOo0 , I1iI1iIi111i )
 if 39 - 39: I1IiI + o00OO00OoO % O0
elif OooOo000OOOOo == 8 :
 i1IiI ( oOo0 , I1iI1iIi111i )
 if 26 - 26: OOO0OOo + I1IiI
elif OooOo000OOOOo == 9 :
 FIXREPOSADDONS ( oOo0 )
 if 17 - 17: ii11ii1ii - i1I111ii1II1i % Oo * O0 % O0 * i1I111II1I
elif OooOo000OOOOo == 10 :
 oOooOOOoOo ( )
 if 6 - 6: o00OO00OoO
elif OooOo000OOOOo == 11 :
 iii11Ii ( oOo0 )
 if 46 - 46: OoOoOO00 * o00OO00OoO
elif OooOo000OOOOo == 12 :
 ii1II ( )
 if 23 - 23: i1IIi - O0
elif OooOo000OOOOo == 13 :
 oOOo00ooO ( )
 if 6 - 6: OOO0OOo % OoooooooOO * o00OO00OoO - OoOo00o
elif OooOo000OOOOo == 14 :
 iIIiII1i1ii ( oOo0 )
 if 24 - 24: Oooo0Ooo000 / iIii1I11I1II1 . OoooooooOO % I1IiI . iI
elif OooOo000OOOOo == 15 :
 o0iiiI1I1iIIIi1 ( )
 if 73 - 73: o00OO00OoO
elif OooOo000OOOOo == 16 :
 I1oooO00oOOooO ( oOo0 , I1iI1iIi111i )
 if 25 - 25: OoOo00o
elif OooOo000OOOOo == 17 :
 IIIii111i ( oOo0 , I1iI1iIi111i )
 if 77 - 77: OOooOOo . iIii1I11I1II1 . OoooooooOO . iIii1I11I1II1
elif OooOo000OOOOo == 18 :
 i1II111iiii ( )
 if 87 - 87: OoOoOO00 - OoooooooOO / i1IIi . iI - Oo . i11iIiiIii
elif OooOo000OOOOo == 19 :
 IIi11IIiIii1 ( I1iI1iIi111i , oOo0 , oo00o0 )
 if 47 - 47: Oo % Ooo00oOo00o - OOO0OOo - Oo * O0ooOooooO
elif OooOo000OOOOo == 40 :
 I1I ( I1iI1iIi111i , oOo0 , oo00o0 )
 if 72 - 72: OOooOOo % OOooOOo + i1I111ii1II1i + ii11ii1ii / Oo
elif OooOo000OOOOo == 42 :
 i11i1iIiii ( I1iI1iIi111i , oOo0 , oo00o0 )
 if 30 - 30: Oo + OOOo0 + i11iIiiIii / Ooo00oOo00o
elif OooOo000OOOOo == 43 :
 i1iI1iii11i ( I1iI1iIi111i , oOo0 , oo00o0 )
 if 64 - 64: OoOo00o
elif OooOo000OOOOo == 20 :
 i1II11II ( oOo0 )
 if 80 - 80: OOOo0 - i11iIiiIii / Ooo00oOo00o / I1IiI + I1IiI
elif OooOo000OOOOo == 22 :
 iioo ( oOo0 )
 if 89 - 89: O0 + OoOo00o * o00OO00OoO
elif OooOo000OOOOo == 23 :
 Ooo0o0000OO ( oOo0 )
 if 30 - 30: I1IiI
elif OooOo000OOOOo == 24 :
 ii1Ii11Ii1i ( oOo0 )
 if 39 - 39: ii11ii1ii + OOooOOo + o00OO00OoO + OoOo00o
elif OooOo000OOOOo == 25 :
 OO0oO0Oo ( oOo0 )
 if 48 - 48: o00OO00OoO / OOO0OOo . iIii1I11I1II1
elif OooOo000OOOOo == 26 :
 oooOOO ( oOo0 )
 if 72 - 72: i1IIi . OOooOOo
elif OooOo000OOOOo == 27 :
 o0Oo0oO00Oooo ( oOo0 )
 if 3 - 3: I1IiI % OoOoOO00 - O0
elif OooOo000OOOOo == 28 :
 iii11OO0oO ( oOo0 )
 if 52 - 52: Ooo00oOo00o
elif OooOo000OOOOo == 29 :
 i1i1IIi ( oOo0 )
 if 49 - 49: iI . ii11ii1ii % OOO0OOo . Oo * i1I111II1I
elif OooOo000OOOOo == 30 :
 O0oOOo0Oo ( oOo0 )
 if 44 - 44: iIii1I11I1II1 / O0 * Oo + OOOo0 . OOO0OOo
elif OooOo000OOOOo == 31 :
 i11iII1II1I1 ( oOo0 )
 if 20 - 20: i1I111ii1II1i + OOooOOo . o00OO00OoO / i11iIiiIii
elif OooOo000OOOOo == 32 :
 I1II ( )
 if 7 - 7: I1IiI / I1IiI . o00OO00OoO * O0 + OoOo00o + O0ooOooooO
elif OooOo000OOOOo == 33 :
 OOoO000 ( )
 if 98 - 98: OoOoOO00 * OoOo00o - OOOo0 % OOooOOo - i1I111ii1II1i % ii11ii1ii
elif OooOo000OOOOo == 35 :
 IIIiIi ( oOo0 )
 if 69 - 69: i1IIi % Ooo00oOo00o % o00OO00OoO / OOO0OOo / OOO0OOo
elif OooOo000OOOOo == 34 :
 iI11I ( oOo0 )
 if 6 - 6: OoOoOO00 % ii11ii1ii % i1IIi * OOO0OOo
elif OooOo000OOOOo == 36 :
 oOOOoo ( oOo0 )
 if 47 - 47: O0
elif OooOo000OOOOo == 37 :
 oO0oOOoo00000 ( oOo0 )
 if 55 - 55: Ooo00oOo00o % O0 / OoooooooOO
elif OooOo000OOOOo == 38 :
 Ii1IIiiIIi ( oOo0 )
 if 49 - 49: OOOo0 . Ooo00oOo00o * OoooooooOO % i11iIiiIii + iIii1I11I1II1 * i1IIi
elif OooOo000OOOOo == 41 :
 iIiii1iI1Ii ( IIII1iI1IiIiI )
 if 88 - 88: ii11ii1ii * i1I111ii1II1i + OoOoOO00
elif OooOo000OOOOo == 39 :
 iIiI11II ( oOo0 )
 if 62 - 62: OoooooooOO
elif OooOo000OOOOo == 45 :
 TEXTS ( )
 if 33 - 33: O0 . i11iIiiIii % OOooOOo
elif OooOo000OOOOo == 46 :
 O00Oo ( )
 if 50 - 50: OOO0OOo
elif OooOo000OOOOo == 47 :
 GEVID ( )
 if 81 - 81: i11iIiiIii * iIii1I11I1II1 / Oo * i1I111II1I
elif OooOo000OOOOo == 48 :
 ii11II1i ( I1iI1iIi111i , oOo0 , oo00o0 )
 if 83 - 83: i11iIiiIii - OOOo0 * i11iIiiIii
elif OooOo000OOOOo == 49 :
 I1Iiiiiii ( )
 if 59 - 59: i1I111ii1II1i - OoooooooOO / OOO0OOo + ii11ii1ii . OOooOOo - i1I111ii1II1i
elif OooOo000OOOOo == 222 :
 iIIIiIi ( oOo0 )
 if 29 - 29: O0ooOooooO
elif OooOo000OOOOo == 333 :
 oO0oOOooO0 ( oOo0 )
 if 26 - 26: O0 % i1I111II1I - OoOo00o . i1I111II1I
 if 70 - 70: OOooOOo + Oooo0Ooo000 / i1I111ii1II1i + OOO0OOo / OOOo0
elif OooOo000OOOOo == 1020 :
 Oo0OOOOOOO0oo ( )
 if 33 - 33: OoooooooOO . O0
elif OooOo000OOOOo == 1021 :
 ANIMEEP ( )
 if 59 - 59: iIii1I11I1II1
elif OooOo000OOOOo == 1022 :
 ANIMEPLAY ( oOo0 )
 if 45 - 45: O0
elif OooOo000OOOOo == 1001 :
 ii1111Iii11i ( )
 if 78 - 78: Oooo0Ooo000 - iIii1I11I1II1 + o00OO00OoO - ii11ii1ii - o00OO00OoO
elif OooOo000OOOOo == 1005 :
 oO0o000oOO ( )
 if 21 - 21: OoooooooOO . O0 / i11iIiiIii
elif OooOo000OOOOo == 1007 :
 Ii11Iiii ( oOo0 )
 if 86 - 86: I1IiI / i1I111II1I
elif OooOo000OOOOo == 1010 :
 O0OOOOoO00oo ( oOo0 )
 if 40 - 40: iIii1I11I1II1 / OOO0OOo / OOOo0 + ii11ii1ii * i1I111II1I
elif OooOo000OOOOo == 1011 :
 OoOiII11IiIi ( oOo0 )
 if 1 - 1: Ooo00oOo00o * OOO0OOo + OoOo00o . O0ooOooooO / OOO0OOo
elif OooOo000OOOOo == 1030 :
 iII1I1i ( )
 if 91 - 91: iI + Oooo0Ooo000 - Oo % I1IiI . i1I111ii1II1i
elif OooOo000OOOOo == 1031 :
 IIiii ( oOo0 , OOO0000oO )
 if 51 - 51: i1I111II1I / Oooo0Ooo000
elif OooOo000OOOOo == 1006 :
 Parse . ParseURL ( oOo0 )
 if 51 - 51: OOO0OOo * O0ooOooooO - o00OO00OoO + i1I111ii1II1i
elif OooOo000OOOOo == 2030 :
 Parse . addonParseURL ( oOo0 )
 if 46 - 46: OOooOOo - i11iIiiIii % Ooo00oOo00o / iI - I1IiI
elif OooOo000OOOOo == 2031 :
 Parse . apkParseURL ( oOo0 )
 if 88 - 88: O0ooOooooO * OOOo0 / Ooo00oOo00o - i1I111II1I / i1IIi . o00OO00OoO
elif OooOo000OOOOo == 1002 :
 i1ooOO00o0 ( oOo0 )
 if 26 - 26: i11iIiiIii - OOO0OOo
elif OooOo000OOOOo == 1003 :
 Ii1I1iIiiI1 ( oOo0 , OOO0000oO )
 if 45 - 45: OOO0OOo + OoOoOO00 % i1I111ii1II1i
elif OooOo000OOOOo == 1004 :
 o00i111iiIiiIiI ( oOo0 )
 if 55 - 55: OOO0OOo - O0ooOooooO % OOOo0
elif OooOo000OOOOo == 1008 :
 I111ii1iI ( )
 if 61 - 61: OOO0OOo
elif OooOo000OOOOo == 1009 :
 M3UPLAY ( oOo0 )
 if 22 - 22: iIii1I11I1II1 / OOO0OOo / OOOo0 - OOooOOo
elif OooOo000OOOOo == 2001 :
 OooOoo ( oOo0 )
 if 21 - 21: O0ooOooooO . i11iIiiIii * Oooo0Ooo000 . i1I111II1I / i1I111II1I
elif OooOo000OOOOo == 1013 :
 O0II11i11II ( )
 if 42 - 42: OoooooooOO / o00OO00OoO . OOooOOo / O0 - OoOo00o * OoOo00o
elif OooOo000OOOOo == 1014 :
 I1iII1IIi1IiI ( )
 if 1 - 1: iI % o00OO00OoO
elif OooOo000OOOOo == 1015 :
 iIioo0ooO ( oOo0 )
 if 97 - 97: I1IiI
elif OooOo000OOOOo == 1016 :
 OOoO00O ( oOo0 )
 if 13 - 13: I1IiI % i1I111II1I . O0 / Oo % Oo
elif OooOo000OOOOo == 1023 :
 Iiiiii111i1ii ( )
 if 19 - 19: o00OO00OoO % OOO0OOo - OOO0OOo % OOOo0 . i1I111II1I - OoooooooOO
elif OooOo000OOOOo == 1024 :
 II1iiI1iI ( )
 if 100 - 100: OOOo0 + iI + OOooOOo . i1IIi % OoooooooOO
elif OooOo000OOOOo == 1025 :
 O0oo0000o ( oOo0 )
 if 64 - 64: O0 % i1IIi * o00OO00OoO - iI + Oo
elif OooOo000OOOOo == 4001 :
 iII ( )
 if 65 - 65: I1IiI . i11iIiiIii
elif OooOo000OOOOo == 4002 :
 o0ooOooo000oOO ( )
 if 36 - 36: O0ooOooooO * i1I111ii1II1i + OoOo00o * i1I111ii1II1i . ii11ii1ii - iIii1I11I1II1
elif OooOo000OOOOo == 4003 :
 O000OOO0OOo ( )
 if 14 - 14: Oooo0Ooo000 * O0ooOooooO + i11iIiiIii
elif OooOo000OOOOo == 4004 :
 ii1ii1ii ( )
 if 84 - 84: i1I111ii1II1i / OoOoOO00
elif OooOo000OOOOo == 4005 :
 oOOo0 ( )
 if 86 - 86: OOOo0
elif OooOo000OOOOo == 4006 :
 oo00O00oO ( )
 if 97 - 97: OoOoOO00
elif OooOo000OOOOo == 4007 :
 iIIiIi1iIII1 ( )
 if 38 - 38: OOOo0
elif OooOo000OOOOo == 4008 :
 OooOOOOo ( )
 if 42 - 42: OOooOOo
elif OooOo000OOOOo == 4009 : oooooOoo0ooo ( )
elif OooOo000OOOOo == 4010 : I1i1i1 ( )
elif OooOo000OOOOo == 3000 :
 Ii1IIi11 ( )
 if 8 - 8: i11iIiiIii / OOO0OOo
elif OooOo000OOOOo == 3001 :
 i1I111Ii ( )
 if 33 - 33: o00OO00OoO * OoOo00o - O0 + OOOo0 / OoOo00o
elif OooOo000OOOOo == 3002 :
 i11i1i ( oOo0 )
 if 19 - 19: i1IIi % OoOoOO00
elif OooOo000OOOOo == 3003 :
 I1ii1Ii1 ( oOo0 )
 if 85 - 85: OoOo00o - OOooOOo % i1I111II1I - OoOoOO00
elif OooOo000OOOOo == 3004 :
 oOiI111I1III ( oOo0 )
 if 56 - 56: iI * i11iIiiIii
elif OooOo000OOOOo == 404 :
 o0OOoOooO0ooO ( I1iI1iIi111i , oOo0 , OOO0000oO )
 if 92 - 92: OoOoOO00 - O0 . o00OO00OoO
elif OooOo000OOOOo == 405 :
 OOOOooO0 ( oOo0 )
 if 59 - 59: I1IiI
elif OooOo000OOOOo == 7030 :
 O00O0Oo0 ( )
 if 47 - 47: OoOoOO00 - ii11ii1ii - iI
elif OooOo000OOOOo == 7021 :
 II1ii1iI ( I1iI1iIi111i )
 if 9 - 9: ii11ii1ii - OoOo00o
elif OooOo000OOOOo == 7022 :
 iii1iI ( I1iI1iIi111i )
 if 64 - 64: i1IIi
elif OooOo000OOOOo == 7000 :
 I11IIII ( I1iI1iIi111i , oOo0 , img )
 if 71 - 71: OoOo00o * OOooOOo
elif OooOo000OOOOo == 7050 :
 o0o ( oOo0 )
 if 99 - 99: OOooOOo
elif OooOo000OOOOo == 7051 :
 oOoOOOO0OOO ( oOo0 )
 if 28 - 28: OoooooooOO % O0 - i1I111II1I / OOooOOo / OOOo0
elif OooOo000OOOOo == 7052 :
 IIII ( oOo0 )
 if 41 - 41: OoOoOO00 * OoOo00o / Ooo00oOo00o . O0ooOooooO
elif OooOo000OOOOo == 7053 :
 ii1oooO0o0oOoO ( oOo0 )
 if 50 - 50: OoooooooOO + iIii1I11I1II1 / O0ooOooooO / i1I111II1I . i11iIiiIii . OOO0OOo
elif OooOo000OOOOo == 7054 :
 CoolPlay ( oOo0 )
 if 75 - 75: iIii1I11I1II1 % OOO0OOo / i1I111II1I - i1I111ii1II1i % i11iIiiIii
elif OooOo000OOOOo == 7060 :
 Oo00oOO00 ( )
 if 11 - 11: Oooo0Ooo000 . iI
elif OooOo000OOOOo == 7061 :
 i11I1Iii1I ( oOo0 )
 if 87 - 87: i1I111II1I + i1I111II1I
elif OooOo000OOOOo == 7063 :
 Iio0000O00oO0O ( oOo0 )
 if 45 - 45: i1IIi - Oo
elif OooOo000OOOOo == 7062 :
 oOo0OoOOOo0 ( oOo0 )
 if 87 - 87: I1IiI - Ooo00oOo00o * Ooo00oOo00o / iI . Oooo0Ooo000 * OOooOOo
elif OooOo000OOOOo == 7064 :
 NATatozcat ( )
 if 21 - 21: OoOoOO00
elif OooOo000OOOOo == 7067 :
 O00o0OO0OO0oo ( oOo0 )
 if 29 - 29: I1IiI % iI
elif OooOo000OOOOo == 7066 :
 NATatozA ( oOo0 )
 if 7 - 7: i1IIi / OoOo00o / i1I111ii1II1i
elif OooOo000OOOOo == 7065 :
 Ooo0O0ooo0o ( oOo0 )
 if 97 - 97: Ooo00oOo00o + iIii1I11I1II1
elif OooOo000OOOOo == 7070 :
 iii1IiiiI1i1 ( )
 if 79 - 79: OOO0OOo + O0ooOooooO - OoOoOO00 . Oo
elif OooOo000OOOOo == 7071 :
 DIZIlist ( oOo0 )
 if 26 - 26: OoOo00o
elif OooOo000OOOOo == 7072 :
 DIZIpull ( oOo0 )
 if 52 - 52: O0 + OOO0OOo
elif OooOo000OOOOo == 7073 :
 WATCHDIZI ( oOo0 )
 if 11 - 11: i1IIi / o00OO00OoO * ii11ii1ii * o00OO00OoO * OOO0OOo - i11iIiiIii
elif OooOo000OOOOo == 7002 :
 Oooo ( )
 if 96 - 96: ii11ii1ii % ii11ii1ii
elif OooOo000OOOOo == 7003 :
 o0OoOo00O0o0O ( oOo0 )
 if 1 - 1: OOOo0 . iI
elif OooOo000OOOOo == 7004 :
 o00o0O0 ( oOo0 )
 if 26 - 26: O0ooOooooO - OOO0OOo % Oo - O0ooOooooO + OoOo00o
elif OooOo000OOOOo == 7020 :
 IiIi ( oOo0 )
 if 33 - 33: iI + I1IiI - ii11ii1ii + iIii1I11I1II1 % i1IIi * OoOo00o
elif OooOo000OOOOo == 7001 :
 o0oOOO ( )
 if 21 - 21: O0 * OOO0OOo % Ooo00oOo00o
elif OooOo000OOOOo == 7010 :
 o0oOO ( oOo0 )
 if 14 - 14: O0 / o00OO00OoO / OOO0OOo + OoOo00o - OoOo00o
elif OooOo000OOOOo == 7011 :
 Ii11IIIi1 ( oOo0 )
 if 10 - 10: O0 - ii11ii1ii / o00OO00OoO % I1IiI / OoooooooOO / iI
elif OooOo000OOOOo == 7012 :
 IIIii11 ( oOo0 )
 if 73 - 73: OOO0OOo + OoOo00o % OOooOOo . ii11ii1ii / i1I111II1I . o00OO00OoO
elif OooOo000OOOOo == 7013 :
 cnfTVPlay2 ( oOo0 )
elif OooOo000OOOOo == 7014 :
 CNF_Studio_Indexer . MV_Movies ( oOo0 )
elif OooOo000OOOOo == 7015 :
 CNF_Studio_Indexer . Movie_ByYear ( oOo0 )
elif OooOo000OOOOo == 7016 :
 CNF_Studio_Indexer . Resolve_CNF_Link ( I1iI1iIi111i , oOo0 , OOO0000oO )
elif OooOo000OOOOo == 7017 :
 CNF_Studio_Indexer . Search_Movie ( )
elif OooOo000OOOOo == 7018 :
 iiiiI ( )
elif OooOo000OOOOo == 7019 :
 CNF_Studio_Indexer . List_Movies ( oOo0 )
elif OooOo000OOOOo == 7020 :
 CNF_Studio_Indexer . Get_Movie_Page ( oOo0 )
elif OooOo000OOOOo == 7024 :
 CNF_Studio_Indexer . Box_Office ( oOo0 )
 if 76 - 76: Oooo0Ooo000 . ii11ii1ii * OoooooooOO % i1I111ii1II1i
elif OooOo000OOOOo == 8000 :
 o00OO0o0 ( )
elif OooOo000OOOOo == 8001 :
 IiI ( )
elif OooOo000OOOOo == 8002 :
 I11II11111i11 ( )
elif OooOo000OOOOo == 8003 :
 OooIii1I1iI ( )
elif OooOo000OOOOo == 8004 :
 ooo00 ( )
elif OooOo000OOOOo == 8005 :
 iIiII11 ( )
elif OooOo000OOOOo == 8006 :
 O0O0oO0oo ( I1iI1iIi111i , oOo0 )
elif OooOo000OOOOo == 8030 :
 O0oOo00o0 ( oOo0 )
elif OooOo000OOOOo == 8045 :
 iIIiIi ( oOo0 )
elif OooOo000OOOOo == 8046 :
 oO0Oo00oo ( oOo0 )
elif OooOo000OOOOo == 8047 :
 OOOO0O00Ooooo ( oOo0 )
elif OooOo000OOOOo == 8020 :
 Iiii1II111 ( )
elif OooOo000OOOOo == 8021 :
 iI11i ( oOo0 )
elif OooOo000OOOOo == 8022 :
 i1i111III1 ( oOo0 )
elif OooOo000OOOOo == 8023 :
 III1i1IIII1i ( oOo0 )
elif OooOo000OOOOo == 8040 :
 i11IiI1iiI11 ( )
elif OooOo000OOOOo == 8041 :
 OOoOOOO00 ( oOo0 )
elif OooOo000OOOOo == 8042 :
 Oo0O0000Oo00o ( oOo0 )
elif OooOo000OOOOo == 8043 :
 yt . PlayVideo ( oOo0 )
elif OooOo000OOOOo == 8044 :
 II1ii ( oOo0 )
elif OooOo000OOOOo == 8060 :
 iII1I11 ( )
elif OooOo000OOOOo == 8061 :
 ii11iiI11I ( oOo0 )
elif OooOo000OOOOo == 8064 :
 iiIi11i1IiI ( )
elif OooOo000OOOOo == 8065 :
 oO00O0O0 ( oOo0 )
elif OooOo000OOOOo == 8070 :
 oOO0O00O00OoO ( )
elif OooOo000OOOOo == 8071 :
 IiIiI1i1 ( oOo0 )
elif OooOo000OOOOo == 7080 :
 ii11I1IIi1i ( oOo0 )
elif OooOo000OOOOo == 8090 :
 OoooOo0 ( )
elif OooOo000OOOOo == 8091 :
 IiI1Ii1ii ( oOo0 )
elif OooOo000OOOOo == 8092 :
 Ii11iiIIiI1 ( oOo0 )
elif OooOo000OOOOo == 8081 :
 OOoO ( )
elif OooOo000OOOOo == 8062 :
 ooo0OO0OOooO0 ( oOo0 )
elif OooOo000OOOOo == 8063 :
 OOO00o0 ( oOo0 )
elif OooOo000OOOOo == 8050 :
 OOoO000O00oO ( )
elif OooOo000OOOOo == 8051 :
 i1OoOO ( oOo0 )
elif OooOo000OOOOo == 8052 :
 iIII1I1i1i ( oOo0 )
elif OooOo000OOOOo == 8085 :
 iI111II1ii ( )
elif OooOo000OOOOo == 8086 :
 IIiI1I ( oOo0 )
elif OooOo000OOOOo == 8087 :
 iIII11Iiii1 ( oOo0 )
elif OooOo000OOOOo == 8088 :
 o0oo0 ( oOo0 , I1iI1iIi111i )
elif OooOo000OOOOo == 9000 :
 Ii1IIIIi1ii1I ( )
elif OooOo000OOOOo == 1111 :
 ooo00O0OOo ( )
elif OooOo000OOOOo == 9001 :
 ooo0O00000oo0 ( )
elif OooOo000OOOOo == 9002 :
 O0oO0oo0O ( )
elif OooOo000OOOOo == 9003 :
 II1I1I1i1i ( )
elif OooOo000OOOOo == 50 :
 oOO ( oOo0 )
elif OooOo000OOOOo == 9020 :
 champlist ( )
elif OooOo000OOOOo == 9021 :
 O0Oo00 ( )
elif OooOo000OOOOo == 9022 :
 Oo0o0ooOoO ( )
elif OooOo000OOOOo == 9023 :
 iI1Ii11 ( )
elif OooOo000OOOOo == 9024 :
 iiiII1III ( oOo0 )
elif OooOo000OOOOo == 9030 :
 iIiIi11 ( oOo0 )
elif OooOo000OOOOo == 9031 :
 I1iIii1i11 ( oOo0 )
elif OooOo000OOOOo == 9032 :
 iIiiI11II11i ( oOo0 )
elif OooOo000OOOOo == 9033 :
 o00OoO0o0 ( oOo0 )
elif OooOo000OOOOo == 7085 :
 iIi1Ii1111i ( oOo0 )
elif OooOo000OOOOo == 7086 :
 o0oO0oo ( oOo0 )
elif OooOo000OOOOo == 7087 :
 oO000 ( oo00o0 )
elif OooOo000OOOOo == 9666 :
 I1Io0Oo00 ( oOo0 )
elif OooOo000OOOOo == 10100 : iiiIi ( )
elif OooOo000OOOOo == 10105 : oO0o0Oo ( oOo0 )
elif OooOo000OOOOo == 10106 : Iiii1Ii ( oOo0 )
elif OooOo000OOOOo == 10104 : IiIiIi1I11I ( oOo0 )
elif OooOo000OOOOo == 10107 : I1IIII ( )
elif OooOo000OOOOo == 10103 : iI1ii ( oOo0 )
elif OooOo000OOOOo == 10108 : iiIi ( oOo0 )
elif OooOo000OOOOo == 10107 : I1IIII ( )
elif OooOo000OOOOo == 10000 : Origin_Menu ( )
elif OooOo000OOOOo == 10001 : OoOo ( )
elif OooOo000OOOOo == 10002 : O0000oO0o00 ( )
elif OooOo000OOOOo == 10003 : O0o00O0Oo0 ( )
elif OooOo000OOOOo == 10004 : oo0ooO0 ( oOo0 )
elif OooOo000OOOOo == 10005 : o00oo0000 ( )
elif OooOo000OOOOo == 10006 : i1oOOOOOOOoO ( oOo0 )
elif OooOo000OOOOo == 10007 : III1ii ( oOo0 , OOO0000oO )
elif OooOo000OOOOo == 10008 : ii1II1II ( )
elif OooOo000OOOOo == 10009 : O00O ( )
elif OooOo000OOOOo == 10010 : oO0o0o00oOo0O ( oOo0 )
elif OooOo000OOOOo == 10011 : Ii1I1i111 ( oOo0 )
elif OooOo000OOOOo == 10012 : OO0ooo0o0 ( oOo0 )
elif OooOo000OOOOo == 10013 : I1IiII1iI1 ( oOo0 )
elif OooOo000OOOOo == 10014 : ooOOooo0Oo ( )
elif OooOo000OOOOo == 10015 : iiiIiI ( )
elif OooOo000OOOOo == 10016 : iIIiIIIi ( oOo0 )
elif OooOo000OOOOo == 10017 : O0iI ( )
elif OooOo000OOOOo == 10018 : iiIiII11i1 ( )
elif OooOo000OOOOo == 10019 : oOO0 ( )
elif OooOo000OOOOo == 10020 : o0oOO00 ( )
elif OooOo000OOOOo == 10021 : Oo0oOo0ooOOOo ( )
elif OooOo000OOOOo == 10022 : OOOoO0 ( oOo0 )
elif OooOo000OOOOo == 10023 : Ii11IiI ( I1iI1iIi111i , oOo0 )
elif OooOo000OOOOo == 10024 : oo000oO ( oOo0 )
elif OooOo000OOOOo == 10025 : oO000o ( )
elif OooOo000OOOOo == 10026 : oOoOo ( )
elif OooOo000OOOOo == 10027 : OO0o0OO0 ( )
elif OooOo000OOOOo == 10028 : oO0ooOO ( )
elif OooOo000OOOOo == 10029 : III1I11i1iIi ( )
elif OooOo000OOOOo == 423 : iI1 ( oOo0 )
elif OooOo000OOOOo == 426 : I11iiIIiI1ii ( oOo0 )
elif OooOo000OOOOo == 10030 : Izle_Films ( )
elif OooOo000OOOOo == 10031 : Latest_Izle_Movies ( )
elif OooOo000OOOOo == 10032 : Izle_Genres ( )
elif OooOo000OOOOo == 10033 : Izle_Pop_Movies ( )
elif OooOo000OOOOo == 10034 : Izle_Boxsets ( )
elif OooOo000OOOOo == 10035 : Izle_Search ( )
elif OooOo000OOOOo == 10036 : Izle_Genres_Movie ( oOo0 )
elif OooOo000OOOOo == 10037 : Izle_Boxset_single ( oOo0 )
elif OooOo000OOOOo == 10038 : Izle_IFRAME ( )
elif OooOo000OOOOo == 10039 : Izle_Boxsets_Next ( oOo0 )
elif OooOo000OOOOo == 10040 : Iiii11I ( )
elif OooOo000OOOOo == 10041 : iiII1iiIi ( oOo0 )
elif OooOo000OOOOo == 10042 : ooo000oOO ( oOo0 )
elif OooOo000OOOOo == 10043 : II1i11 ( )
elif OooOo000OOOOo == 10044 : OOO0o0 ( oOo0 )
elif OooOo000OOOOo == 10045 : Ii1Ii1I ( I1iI1iIi111i )
elif OooOo000OOOOo == 10046 : o0OO0OOO0O ( oOo0 )
elif OooOo000OOOOo == 10047 : i1I1i ( oOo0 )
elif OooOo000OOOOo == 10048 : ii1i ( oOo0 )
elif OooOo000OOOOo == 10049 : Ooii1IIi1ii ( oOo0 )
elif OooOo000OOOOo == 10050 : I1I111IIIi1 ( )
elif OooOo000OOOOo == 10051 : o000o0o00Oo ( )
elif OooOo000OOOOo == 10052 : Ii1iI1IIIII ( )
elif OooOo000OOOOo == 10053 : Addon ( oOo0 )
elif OooOo000OOOOo == 10054 : OO0OOOOOo ( oOo0 , I1iI1iIi111i )
elif OooOo000OOOOo == 10055 :
 oo0iIiI ( "addFavorite" )
 try :
  I1iI1iIi111i = I1iI1iIi111i . split ( '\\ ' ) [ 1 ]
 except :
  pass
 try :
  I1iI1iIi111i = I1iI1iIi111i . split ( '  - ' ) [ 0 ]
 except :
  pass
 oo0i1iIIi1II1iiI ( I1iI1iIi111i , oOo0 , OOO0000oO , iI1i111I1Ii , iiIi1 )
elif OooOo000OOOOo == 10056 :
 oo0iIiI ( "rmFavorite" )
 try :
  I1iI1iIi111i = I1iI1iIi111i . split ( '\\ ' ) [ 1 ]
 except :
  pass
 try :
  I1iI1iIi111i = I1iI1iIi111i . split ( '  - ' ) [ 0 ]
 except :
  pass
 o0OOII1I1 ( I1iI1iIi111i )
elif OooOo000OOOOo == 10057 :
 oo0iIiI ( "getFavorites" )
 OO0o0oO0O000o ( )
elif OooOo000OOOOo == 10058 : OOoOoOo ( )
elif OooOo000OOOOo == 10059 : Donators_Guide ( )
elif OooOo000OOOOo == 10060 : OoOooOoO ( )
elif OooOo000OOOOo == 10061 : iiI1I1 ( )
elif OooOo000OOOOo == 10062 : IIi1IIIi ( I1iI1iIi111i , oOo0 , oo00o0 )
elif OooOo000OOOOo == 10063 : Ii ( )
elif OooOo000OOOOo == 10064 : Ii1Io0OO0o0o00o ( )
elif OooOo000OOOOo == 10065 : i1II1i ( oOo0 )
elif OooOo000OOOOo == 10066 : Ii1Iii1iIi ( oOo0 )
elif OooOo000OOOOo == 10068 : ooo ( oOo0 )
elif OooOo000OOOOo == 10069 : ii1iI1I11I ( oOo0 )
elif OooOo000OOOOo == 10070 : ii1I1 ( oOo0 )
elif OooOo000OOOOo == 10071 : Genie_Watch ( )
elif OooOo000OOOOo == 10072 : oO0 ( )
elif OooOo000OOOOo == 10073 : o0O ( oOo0 )
elif OooOo000OOOOo == 10074 : IiI1i ( oOo0 )
elif OooOo000OOOOo == 10075 : ooiIi1 ( OOO0000oO , I1iI1iIi111i , oOo0 )
elif OooOo000OOOOo == 10076 : O000OOO ( oOo0 )
elif OooOo000OOOOo == 10077 : O00o0OO0 ( oOo0 )
elif OooOo000OOOOo == 10078 : oOI1Ii1I1 ( )
elif OooOo000OOOOo == 10079 : Genie_Watch_Tv_Shows ( )
elif OooOo000OOOOo == 10080 : Genie_Watch_Tv_Genre ( oOo0 )
elif OooOo000OOOOo == 10081 : Genie_Watch_TV_PlayRun ( oOo0 )
elif OooOo000OOOOo == 10082 : Genie_Watch_TV_Episodes ( oOo0 , OOO0000oO )
elif OooOo000OOOOo == 10083 : Genie_Watch_Tv_Recent ( oOo0 )
elif OooOo000OOOOo == 10084 : ii1ii11IIIiiI ( )
elif OooOo000OOOOo == 20000 : O0oooo0OoO0oo ( )
elif OooOo000OOOOo == 20001 : IiI1IiI11iII ( )
elif OooOo000OOOOo == 20002 : ii11I ( oOo0 )
elif OooOo000OOOOo == 20003 : oOiI ( oOo0 )
elif OooOo000OOOOo == 20004 : o0O0ooOOoO ( oOo0 )
elif OooOo000OOOOo == 21004 : IIi1I1 ( )
elif OooOo000OOOOo == 21005 : iIi ( oOo0 )
elif OooOo000OOOOo == 21006 : I1 ( oOo0 )
elif OooOo000OOOOo == 21007 : OoiiIiI ( oOo0 )
elif OooOo000OOOOo == 30000 : I11I1IIiiII1 ( )
elif OooOo000OOOOo == 30001 : ii1I11iIiIII1 ( )
elif OooOo000OOOOo == 10012 : Resolve ( oOo0 )
elif OooOo000OOOOo == 30003 : IIIII1iii11 ( )
elif OooOo000OOOOo == 30004 : I1ii1Ii1ii11i ( oOo0 )
elif OooOo000OOOOo == 30005 : o00oiii11II1I ( oOo0 )
elif OooOo000OOOOo == 30006 : OooOOo0 ( )
elif OooOo000OOOOo == 30007 : I11IIIiIi11 ( )
elif OooOo000OOOOo == 30008 : IIi11I1 ( oOo0 )
elif OooOo000OOOOo == 30009 : Ii1 ( oOo0 )
elif OooOo000OOOOo == 30010 : O0O0 ( oOo0 )
elif OooOo000OOOOo == 30011 : IiIIiIIIiIii ( )
elif OooOo000OOOOo == 30012 : I1iIi1iiiIiI ( )
elif OooOo000OOOOo == 30013 : Ii1I11I ( )
elif OooOo000OOOOo == 30014 : IiIiiiiI1 ( )
if 24 - 24: OoooooooOO
xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
