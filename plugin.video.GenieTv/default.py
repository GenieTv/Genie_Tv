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
iiiiiIIii = 'http://architects.x10host.com/safety/index.php?mode=XxX&password=fordfiesta'
if 71 - 71: OOO0OOO00oo + Oo000 / iI - i1I111ii1II1i / OoOo00o
if 70 - 70: Ooo0OO0 * OoO0O0
def II1i1IiiIIi11 ( ) :
 if not os . path . exists ( I1iII1iiII ) :
  oOOoo00O0O . ok ( "[COLOR=white]Incompatible[/COLOR]" , "Unfortunately GenieTv will only work with" , 'its official repo please install from trusted source' , '' )
  iI1Ii11iII1 = 'genie tv repo not being installed '
  Oo0O0O0ooO0O ( iI1Ii11iII1 )
 else :
  if not os . path . exists ( xbmc . translatePath ( os . path . join ( 'special://home/addons/service.xbmc.cleanse' ) ) ) :
   iI1Ii11iII1 = 'genie tv repo not being installed '
   Oo0O0O0ooO0O ( iI1Ii11iII1 )
  else :
   pass
def IIIIii ( ) :
 II1i1IiiIIi11 ( )
 O0o0 ( )
 OO00Oo ( )
 O0OOO0OOoO0O ( )
 if o0oO0 . getSetting ( 'My Build' ) == 'true' :
  O00Oo000ooO0 ( '[COLORgreen]WIZARD[/COLOR]' , iiI1IiI , 4001 , ii11iIi1I + 'MB.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Streams' ) == 'true' :
  O00Oo000ooO0 ( '[COLORgreen]STREAMS[/COLOR]' , iiI1IiI , 4002 , ii11iIi1I + 'streams.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Music' ) == 'true' :
  O00Oo000ooO0 ( '[COLORgreen]Music[/COLOR]' , iiI1IiI , 4003 , ii11iIi1I + 'MUSIC.png' , i1iiIII111ii , '' )
  if 100 - 100: II11i1iIiII1 + O0 / OOO0OOO00oo * OoO0O0 / iIii1I11I1II1
 if o0oO0 . getSetting ( 'Builders Toolbox' ) == 'true' :
  O00Oo000ooO0 ( '[COLORgreen]BUILDERS TOOLBOX[/COLOR]' , iiI1IiI , 32 , ii11iIi1I + 'builderstoolbox.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Source List' ) == 'true' :
  O00Oo000ooO0 ( '[COLORgreen]SOURCE LIST[/COLOR]' , iiI1IiI , 46 , ii11iIi1I + 'sources.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Maintainance' ) == 'true' :
  O00Oo000ooO0 ( '[COLORgreen]MAINTENANCE[/COLOR]' , iiI1IiI , 3 , ii11iIi1I + 'MAIN6.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Addons' ) == 'true' :
  O00Oo000ooO0 ( '[COLORgreen]ADDONS[/COLOR]' , '' , 10050 , ii11iIi1I + 'ADDONS.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'APK Tool' ) == 'true' :
  O00Oo000ooO0 ( '[COLORgreen]APK TOOL[/COLOR]' , iiI1IiI , 2 , ii11iIi1I + 'APK.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Rss Feed' ) == 'true' :
  O00Oo000ooO0 ( '[COLORgreen]GenieTv RSS Feed[/COLOR]' , iiI1IiI , 39 , ii11iIi1I + 'RSS.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Addons Packs' ) == 'true' :
  O00Oo000ooO0 ( '[COLORgreen]ADDONS PACKS[/COLOR]' , iiI1IiI , 30 , ii11iIi1I + 'ADDONP.png' , i1iiIII111ii , '' )
 ii111 ( 'movies' , 'MAIN' )
 if 16 - 16: ii11ii1ii + Ooo00oOo00o - OoOoOO00
def oOoOO0 ( ) :
 II1i1IiiIIi11 ( )
 O00Oo000ooO0 ( '[COLORgreen]BACKUP MY BUILD[/COLOR]' , iiI1IiI , 10060 , ii11iIi1I + 'MB.png' , i1iiIII111ii , '' )
 O00Oo000ooO0 ( '[COLORgreen]RESTORE MY BUILD[/COLOR]' , iiI1IiI , 49 , ii11iIi1I + 'MB.png' , i1iiIII111ii , '' )
 O00Oo000ooO0 ( '[COLORgreen]WIPE GENIE[/COLOR]' , iiI1IiI , 41 , ii11iIi1I + 'wipegenie.png' , i1iiIII111ii , '' )
 O00Oo000ooO0 ( '[COLORgreen]WISHES PC[/COLOR]' , iiI1IiI , 1 , ii11iIi1I + 'WISHESPC.png' , i1iiIII111ii , '' )
 O00Oo000ooO0 ( '[COLORgreen]WISHES ANDROID[/COLOR]' , iiI1IiI , 44 , ii11iIi1I + 'WISHESAN.png' , i1iiIII111ii , '' )
 ii111 ( 'movies' , 'MAIN' )
def IiI11iII1 ( ) :
 II1i1IiiIIi11 ( )
 if oO == '5knuckleshuffle' :
  O00Oo000ooO0 ( '[COLORgreen]XVID[/COLOR]' , iiI1IiI , 10100 , ii11iIi1I + 'JIZBOX.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Favourites' ) == 'true' :
  O00Oo000ooO0 ( '[COLORgreen]FAVOURITES[/COLOR]' , iiI1IiI , 10057 , ii11iIi1I + 'FAVORITES.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Search' ) == 'true' :
  O00Oo000ooO0 ( '[COLORgreen]SEARCH[/COLOR]' , iiI1IiI , 9000 , ii11iIi1I + 'search.png' , i1iiIII111ii , '' )
 O00Oo000ooO0 ( '[COLORgreen]Live TV[/COLOR]' , iiI1IiI , 4009 , ii11iIi1I + 'GTVIPTV.png' , i1iiIII111ii , '' )
 O00Oo000ooO0 ( '[COLORgreen]MOVIES[/COLOR]' , iiI1IiI , 4004 , ii11iIi1I + 'MOVIESv.png' , i1iiIII111ii , '' )
 O00Oo000ooO0 ( '[COLORgreen]TV SHOWS[/COLOR]' , iiI1IiI , 4005 , ii11iIi1I + 'TVSHOWSv.png' , i1iiIII111ii , '' )
 O00Oo000ooO0 ( '[COLORgreen]STREAM TEAM[/COLOR]' , iiI1IiI , 4006 , ii11iIi1I + 'streamteam.png' , i1iiIII111ii , '' )
 O00Oo000ooO0 ( '[COLORgreen]KIDS[/COLOR]' , iiI1IiI , 4007 , ii11iIi1I + 'KIDSv.png' , i1iiIII111ii , '' )
 O00Oo000ooO0 ( '[COLORgreen]HOBBIES[/COLOR]' , iiI1IiI , 4008 , ii11iIi1I + 'hobbies.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'YOUTUBE' ) == 'true' :
  O00Oo000ooO0 ( '[COLORgreen]SEARCH YOUTUBE[/COLOR]' , iiI1IiI , 10064 , ii11iIi1I + 'youtube.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'REQUESTS' ) == 'true' :
  O00Oo000ooO0 ( '[COLORgreen]REQUESTS[/COLOR]' , iiI1IiI + ( i1111 ( 'L1JFUVVFU1RTLnBocA==' ) ) , 10066 , ii11iIi1I + 'requests.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Stand Up' ) == 'true' :
  O00Oo000ooO0 ( '[COLORgreen]STAND UP[/COLOR]' , '' , 10003 , ii11iIi1I + 'ORIGINSTANDUP.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Documentaries' ) == 'true' :
  O00Oo000ooO0 ( '[COLORgreen]DOCUMENTARIES[/COLOR]' , iiI1IiI , 8040 , ii11iIi1I + 'documentary.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Disclose' ) == 'true' :
  O00Oo000ooO0 ( '[COLORgreen]DISCLOSE TV[/COLOR]' , iiI1IiI , 7001 , ii11iIi1I + 'disclose.png' , i1iiIII111ii , '' )
  if 29 - 29: Oo - OOO0OOO00oo - iI % OoOo00o - OOO0OOO00oo
  if 91 - 91: Ooo00oOo00o / iI - OoOoOO00 . iI
 if o0oO0 . getSetting ( 'Playlist Loader' ) == 'true' :
  O00Oo000ooO0 ( '[COLORgreen]PLAYLIST LOADER[/COLOR]' , iiI1IiI , 3000 , ii11iIi1I + 'loader.png' , i1iiIII111ii , '' )
  if 18 - 18: OOooOOo
  if 98 - 98: OoOo00o * OoOo00o / OoOo00o + iI
  if 34 - 34: II11i1iIiII1
  if 15 - 15: iI * II11i1iIiII1 * Oo % i11iIiiIii % I1IiI - Oo000
  if 68 - 68: OoO0O0 % i1IIi . Ooo0OO0 . ii11ii1ii
  if 92 - 92: OoOo00o . OoO0O0
  if 31 - 31: OoO0O0 . I1IiI / O0
  if 89 - 89: I1IiI
  if 68 - 68: Ooo00oOo00o * OoooooooOO % O0 + Ooo00oOo00o + II11i1iIiII1
  if 4 - 4: II11i1iIiII1 + O0 * Oo000
  if 55 - 55: Oo + iIii1I11I1II1 / I1IiI * OOO0OOO00oo - i11iIiiIii - i1I111ii1II1i
  if 25 - 25: ii11ii1ii
  if 7 - 7: i1IIi / OOOo0 * OoO0O0 . Ooo0OO0 . iIii1I11I1II1
 ii111 ( 'movies' , 'MAIN' )
 if 13 - 13: Oo000 / i11iIiiIii
def O0o0 ( ) :
 if not os . path . exists ( ooOoOoo0O ) :
  Iiii ( 'Change Log 24/04/16 - v2.7.1' , 'Just a little one to add in [COLORred]ITV section[/COLOR] into [COLORblue]streams - stream team[/COLOR], it is a film noir section for you fans. Hope you enjoy' )
  os . makedirs ( ooOoOoo0O )
  if 75 - 75: I1IiI % OOooOOo % OOooOOo . OoO0O0
  if 5 - 5: OOooOOo * II11i1iIiII1 + I1IiI . Oo000 + I1IiI
def oOiIi1IIIi1 ( ) :
 II1i1IiiIIi11 ( )
 O00Oo000ooO0 ( '[COLORgreen]SEARCH MOVIES[/COLOR]' , iiI1IiI , 9001 , ii11iIi1I + 'search.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Popcorn Box' ) == 'true' :
  O00Oo000ooO0 ( '[COLORgreen]POPCORN BOX[/COLOR]' , iiI1IiI , 7061 , ii11iIi1I + 'popcorn.png' , i1iiIII111ii , '' )
 O00Oo000ooO0 ( '[COLORgreen]Film Trailers[/COLOR]' , i1111 ( 'aHR0cDovL3RoZW1vdmllYm94Lm5ldC9leHBsb3Jl' ) , 10068 , ii11iIi1I + 'movietrailers.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'CLASSIC MOVIES' ) == 'true' :
  O00Oo000ooO0 ( '[COLORgreen]CLASSIC MOVIES[/COLOR]' , '' , 8060 , ii11iIi1I + 'classicmovies.png' , i1iiIII111ii , '' )
 ii111 ( 'movies' , 'MAIN' )
def O0oOoOOOoOO ( ) :
 II1i1IiiIIi11 ( )
 if o0oO0 . getSetting ( 'G-tv' ) == 'true' :
  O00Oo000ooO0 ( '[COLORgreen]G-Tv PRIVATE LIST[/COLOR]' , '' , 10058 , ii11iIi1I + 'GTVIPTV.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'TV GUIDE' ) == 'true' :
  ii1ii11IIIiiI ( '[COLORgreen]TV GUIDE[/COLOR]' , '' , 10063 , ii11iIi1I + 'GTVIPTV.png' , i1iiIII111ii , '' )
 ii1ii11IIIiiI ( '[COLORgreen]Link GTV Donators Username and Password to Guide[/COLOR]' , '' , 4010 , ii11iIi1I + 'GTVIPTV.png' , i1iiIII111ii , '' )
 if 67 - 67: iI * OOO0OOO00oo * ii11ii1ii + Oo000 / i1IIi
 if 11 - 11: i1I111ii1II1i + OoOo00o - II11i1iIiII1 * OOO0OOO00oo % i11iIiiIii - OoO0O0
def o0oO ( ) :
 II1i1IiiIIi11 ( )
 O00Oo000ooO0 ( '[COLORgreen]SEARCH SERIES[/COLOR]' , iiI1IiI , 9002 , ii11iIi1I + 'search.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Dizzy Tv' ) == 'true' :
  O00Oo000ooO0 ( '[COLORgreen]DIZZY TV[/COLOR]' , '' , 10018 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Watch Series' ) == 'true' :
  O00Oo000ooO0 ( '[COLORgreen]WATCH SERIES[/COLOR]' , '' , 10040 , ii11iIi1I + 'WATCHSERIES.png' , i1iiIII111ii , '' )
 O00Oo000ooO0 ( '[COLORgreen]iWATCH SERIES[/COLOR]' , '' , 8020 , ii11iIi1I + 'iwatch.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Recent Episodes' ) == 'true' :
  O00Oo000ooO0 ( '[COLORgreen]RECENT EPISODES[/COLOR]' , iiI1IiI , 8081 , ii11iIi1I + 'recent.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'CLASSIC TV' ) == 'true' :
  O00Oo000ooO0 ( '[COLORgreen]CLASSIC TV[/COLOR]' , iiI1IiI , 8064 , ii11iIi1I + 'classictv.png' , i1iiIII111ii , '' )
 O00Oo000ooO0 ( '[COLORgreen]TV Show Trailers[/COLOR]' , i1111 ( 'aHR0cHM6Ly93d3cueW91dHViZS5jb20vd2F0Y2g/dj03WkZJUzJBcUF6OCZsaXN0PVBMM2t4NWgyVHJZR3dwVzBWYk5lbnBqLUJLTUJUR2dKUEU=' ) , 10069 , ii11iIi1I + 'tvtrailers.png' , i1iiIII111ii , '' )
 O00Oo000ooO0 ( '[COLORgreen]TV Show Schedule[/COLOR]' , i1111 ( 'aHR0cDovL3d3dy5wb2dkZXNpZ24uY28udWsvY2F0Lw==' ) , 10070 , ii11iIi1I + 'tvschedule.png' , i1iiIII111ii , '' )
 ii111 ( 'movies' , 'MAIN' )
def IIiIi1iI ( ) :
 II1i1IiiIIi11 ( )
 if o0oO0 . getSetting ( 'Scooby Streams' ) == 'true' :
  O00Oo000ooO0 ( '[COLORgreen]SCOOBY STREAMS[/COLOR]' , iiI1IiI , 1023 , ii11iIi1I + 'scoob.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'The Reaper' ) == 'true' :
  O00Oo000ooO0 ( '[COLORgreen]THE REAPER[/COLOR]' , ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9UaGVfUmVhcGVyL21haW4ucGhw' ) ) , 1016 , ii11iIi1I + 'reap.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Pandoras Box' ) == 'true' :
  O00Oo000ooO0 ( '[COLORgreen]PANDORAS BOX[/COLOR]' , iiI1IiI , 10025 , ii11iIi1I + 'PANDORASBOX.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'HeroVision' ) == 'true' :
  O00Oo000ooO0 ( '[COLORgreen]HEROVISION[/COLOR]' , ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC9tYWluLnBocA==' ) ) , 1016 , ii11iIi1I + 'hero.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Silent Hunter' ) == 'true' :
  O00Oo000ooO0 ( '[COLORgreen]SILENT HUNTER[/COLOR]' , ( i1111 ( 'aHR0cDovLzUuMTM1LjIwNy45Ni8=' ) ) , 10084 , ii11iIi1I + 'SILENTHUNTER.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Redemption Streams' ) == 'true' :
  O00Oo000ooO0 ( '[COLORgreen]Redemption Streams[/COLOR]' , ( i1111 ( 'aHR0cDovL3JlZGVtcHRpb25idWlsZC4xNm1iLmNvbS9SZWRlbXB0aW9uL21haW4ucGhw' ) ) , 1016 , ii11iIi1I + 'redemption.png' , i1iiIII111ii , '' )
 O00Oo000ooO0 ( '[COLORgreen]ITV[/COLOR]' , ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9pVHZfU3RyZWFtcy9tYWluLnBocA==' ) ) , 1016 , ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9pVHZfU3RyZWFtcy9pdHZzdHJlYW1zLnBuZw==' ) ) , i1iiIII111ii , '' )
 ii111 ( 'movies' , 'MAIN' )
 if 35 - 35: i1I111ii1II1i % O0 - O0
def IiIIIi1iIi ( ) :
 II1i1IiiIIi11 ( )
 O00Oo000ooO0 ( '[COLORgreen]SILENT HUNTER[/COLOR]' , ( i1111 ( 'aHR0cDovLzUuMTM1LjIwNy45Ni8=' ) ) , 1006 , ii11iIi1I + 'SILENTHUNTER.png' , i1iiIII111ii , '' )
 O00Oo000ooO0 ( '[COLORgreen]SILENT HUNTER SCRAPES[/COLOR]' , ( i1111 ( 'aHR0cDovLzUuMTM1LjIwNy45Ni9TY3JhcGVzL21haW4ucGhw' ) ) , 1016 , ii11iIi1I + 'SILENTHUNTER.png' , i1iiIII111ii , '' )
 if 68 - 68: i11iIiiIii % ii11ii1ii + i11iIiiIii
 if 31 - 31: OoOoOO00 . OOOo0
 if 1 - 1: Oo / OOooOOo % OoOo00o * Ooo0OO0 . i11iIiiIii
def III1Iiii1I11 ( ) :
 II1i1IiiIIi11 ( )
 O00Oo000ooO0 ( '[COLORgreen]SEARCH CARTOONS[/COLOR]' , '' , 10005 , ii11iIi1I + 'search.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'WCO' ) == 'true' :
  O00Oo000ooO0 ( '[COLORgreen]WATCH CARTOONS ONLINE[/COLOR]' , iiI1IiI , 21004 , ii11iIi1I + 'watchcartoons.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Cartoons' ) == 'true' :
  O00Oo000ooO0 ( '[COLORgreen]CARTOONS[/COLOR]' , '' , 10001 , ii11iIi1I + 'ORIGINCARTOON.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Anime' ) == 'true' :
  O00Oo000ooO0 ( '[COLORgreen]AnimeLand[/COLOR]' , ( i1111 ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2R1YmJlZC1hbmltZQ==' ) ) , 10004 , ii11iIi1I + 'anime.png' , i1iiIII111ii , '' )
 ii111 ( 'movies' , 'MAIN' )
def IIII ( ) :
 II1i1IiiIIi11 ( )
 if o0oO0 . getSetting ( 'Football' ) == 'true' :
  O00Oo000ooO0 ( '[COLORgreen]FOOTBALL[/COLOR]' , '' , 10002 , ii11iIi1I + 'ORIGINFOOTBALL.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Fitness' ) == 'true' :
  O00Oo000ooO0 ( '[COLORgreen]FITNESS[/COLOR]' , ( i1111 ( 'aHR0cHM6Ly93d3cuZml0bmVzc2JsZW5kZXIuY29tL3ZpZGVvcw==' ) ) , 7085 , ii11iIi1I + 'FITNESS.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'Go Fishing' ) == 'true' :
  O00Oo000ooO0 ( '[COLORgreen]Go Fishing[/COLOR]' , iiI1IiI , 8090 , ii11iIi1I + 'gofish.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'GenieTv Kitchen' ) == 'true' :
  O00Oo000ooO0 ( '[COLORgreen]GenieTv Kitchen[/COLOR]' , ( i1111 ( 'aHR0cDovL2Zvb2QubmR0di5jb20vdmlkZW9z' ) ) , 8045 , ii11iIi1I + 'geniekitchen.png' , i1iiIII111ii , '' )
 ii111 ( 'movies' , 'MAIN' )
 if 32 - 32: OoooooooOO / iIii1I11I1II1 - OOooOOo
 if 91 - 91: OoOo00o % i1IIi % iIii1I11I1II1
 if 20 - 20: Oo000 % i1I111ii1II1i / i1I111ii1II1i + i1I111ii1II1i
def O0OOO0OOoO0O ( ) :
 III1IiiI = iIi1 ( 'http://architects.x10host.com/wizarddelete.txt' )
 IIIII11I1IiI = re . compile ( '<unwanted_wizard =(.+?)</unwanted_wizard>' ) . findall ( III1IiiI )
 for i1I in IIIII11I1IiI :
  print i1I
  i1I = ( str ( i1I ) )
  if os . path . exists ( xbmc . translatePath ( i1I ) ) :
   OoOO = os . path . join ( I11II1i , 'guisettings.xml' )
   ooOOO0 = open ( OoOO , "w+" )
   if 65 - 65: O0
   ooOOO0 . write ( r'.' )
   oO00OOoO00 ( )
  else :
   pass
   if 40 - 40: OOOo0 * i1I111ii1II1i + Oo000 % OoOo00o
def OO00Oo ( ) :
 III1IiiI = iIi1 ( 'http://architects.x10host.com/testdelete.txt' )
 IIIII11I1IiI = re . compile ( '<unwanted_addon =(.+?)</unwanted_addon>' ) . findall ( III1IiiI )
 for iI1Ii11iII1 in IIIII11I1IiI :
  iI1Ii11iII1 = ( str ( iI1Ii11iII1 ) )
  if os . path . exists ( xbmc . translatePath ( iI1Ii11iII1 ) ) :
   Oo0O0O0ooO0O ( iI1Ii11iII1 )
   OOOOOoo0 ( )
  else :
   pass
   if 49 - 49: O0 . OoOo00o
def Oo0O0O0ooO0O ( addon ) :
 oOOoo00O0O . ok ( "[COLOR=white]Incompatible[/COLOR]" , "Unfortunately GenieTv will not work with" , addon , 'please remove then reinstall genie' )
 OoOO = os . path . join ( II , 'default.py' )
 ooOOO0 = open ( OoOO , "w+" )
 if 11 - 11: Ooo0OO0 * OOOo0 . iIii1I11I1II1 % OoooooooOO + OoOo00o
 ooOOO0 . write ( r'Genie Tv will not work with certain addons in an attempt to bring you original content from the best developers' )
 ooOOO0 . write ( r'and not those simply out to profit or make a name for themselves off others work' )
 ooOOO0 . write ( r'Please remove' + unwanted_addons + 'if you would like to use genie tv then uninstall and reinstall from official repo' )
 if 78 - 78: Ooo00oOo00o . Oo000 + Ooo00oOo00o / iI / Ooo00oOo00o
 if 54 - 54: I1IiI % OoOo00o
def oO00OOoO00 ( ) :
 III1IiiI = iIi1 ( i1111 ( 'aHR0cDovL3d3dy5wb2dkZXNpZ24uY28udWsvY2F0Lw==' ) )
 IIiII111iiI1I = re . compile ( '<tr>.+?title="(.+?)">(.+?)</tr>' , re . DOTALL ) . findall ( III1IiiI )
 for Ii1i1iI1iIIi , IIiII111iiI1I in IIiII111iiI1I :
  Ii1i1iI1iIIi = Ii1i1iI1iIIi
  IIIII11I1IiI = re . compile ( '<p><a href=".+?" rel=".+?">(.+?)\n</a>.+?<br /><a href=".+?">(.+?)</a>.+?</p>' , re . DOTALL ) . findall ( str ( IIiII111iiI1I ) )
  for I1Ii , O0oo00o0O in IIIII11I1IiI :
   Iiii ( Ii1i1iI1iIIi , I1Ii , O0oo00o0O )
   if 1 - 1: OoOoOO00
   if 84 - 84: OOooOOo % OoOoOO00 . i11iIiiIii / Ooo00oOo00o
   if 80 - 80: OoO0O0 . i11iIiiIii - OOooOOo
   if 25 - 25: Ooo00oOo00o
   if 62 - 62: Oo000 + O0
   if 98 - 98: OOooOOo
   if 51 - 51: Oo - OOO0OOO00oo + OoOoOO00 * i1I111ii1II1i . iI + OOO0OOO00oo
   if 78 - 78: i11iIiiIii / OoOo00o - i1I111ii1II1i / Oo000 + OOO0OOO00oo
   if 82 - 82: i1I111ii1II1i
   if 46 - 46: OoooooooOO . i11iIiiIii
   if 94 - 94: OOooOOo * i1I111ii1II1i / Oo / i1I111ii1II1i
   if 87 - 87: Oo . Ooo0OO0
   if 75 - 75: II11i1iIiII1 + I1IiI + OOooOOo * iI % OOO0OOO00oo . OoOo00o
   if 55 - 55: Oo000 . OOOo0
   if 61 - 61: Oo % Ooo0OO0 . Oo
   if 100 - 100: OoO0O0 * O0
   if 64 - 64: Oo000 % iIii1I11I1II1 * OOO0OOO00oo
def o0iI11I1II ( ) :
 O00Oo000ooO0 ( 'Genre' , i1111 ( 'aHR0cDovL2ltb3ZpZW1heC5zZS9tb3ZpZXMv' ) , 10073 , ii11iIi1I + 'genievision.png' , i1iiIII111ii , '' )
 O00Oo000ooO0 ( 'Most Viewed' , i1111 ( 'aHR0cDovL2ltb3ZpZW1heC5zZS9tb3ZpZXMv' ) , 10077 , ii11iIi1I + 'genievision.png' , i1iiIII111ii , '' )
 O00Oo000ooO0 ( 'Box Office' , i1111 ( 'aHR0cDovL2ltb3ZpZW1heC5zZS9jYXRlZ29yeS9ib3gtb2ZmaWNlLw==' ) , 10074 , ii11iIi1I + 'genievision.png' , i1iiIII111ii , '' )
 O00Oo000ooO0 ( 'Search' , '' , 10078 , ii11iIi1I + 'genievision.png' , i1iiIII111ii , '' )
 if 40 - 40: iIii1I11I1II1 / I1IiI % ii11ii1ii + OoOoOO00
def ii1Ii1I1Ii11i ( ) :
 i1111I1I = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 i1i = 'http://imoviemax.se/?s=' + ( i1111I1I ) . replace ( ' ' , '+' )
 oOOoo00O00o = i1i . lower ( )
 O0O00Oo ( oOOoo00O00o )
def oooooo0O000o ( url ) :
 OoO = [ ]
 III1IiiI = iIi1 ( url )
 IIIII11I1IiI = re . compile ( '<li class="cat-item cat-item-.+? "><a href="(.+?)">(.+?)</a><i>(.+?)</i></li>' ) . findall ( III1IiiI )
 for url , I1Ii , ooO0O0O0ooOOO in IIIII11I1IiI :
  if I1Ii in OoO :
   pass
  else :
   O00Oo000ooO0 ( I1Ii + ' - ' + ooO0O0O0ooOOO + ' Films' , url , 10074 , ii11iIi1I + 'genievision.png' , i1iiIII111ii , '' )
   OoO . append ( I1Ii )
   if 77 - 77: I1IiI - OoOoOO00 - II11i1iIiII1
def IiiiIIiIi1 ( url ) :
 III1IiiI = iIi1 ( url )
 IIIII11I1IiI = re . compile ( '<li>.+?<b>.+?</b>.+?<a href="(.+?)">(.+?)</a>.+?<span>(.+?)</span>' , re . DOTALL ) . findall ( III1IiiI )
 for url , I1Ii , OoOOoOooooOOo in IIIII11I1IiI :
  O00Oo000ooO0 ( I1Ii + ' - Views:' + OoOOoOooooOOo , url , 10075 , ii11iIi1I + 'genievision.png' , i1iiIII111ii , '' )
  if 87 - 87: OOOo0
  if 58 - 58: I1IiI % OOooOOo
def O0O00Oo ( url ) :
 i1OOoO = [ ]
 III1IiiI = iIi1 ( url )
 next = re . compile ( "<link rel='next' href='(.+?)' />" ) . findall ( III1IiiI )
 for next in next :
  O00Oo000ooO0 ( 'NEXT PAGE' , next , 10074 , ii11iIi1I + 'Next.png' , i1iiIII111ii , '' )
 IIIII11I1IiI = re . compile ( '<div class="movie">.+?<img src="(.+?)" alt="(.+?)" />.+?<a href="(.+?)"><span class="player"></span></a>' , re . DOTALL ) . findall ( III1IiiI )
 for OO0O000 , I1Ii , url in IIIII11I1IiI :
  O00Oo000ooO0 ( I1Ii , url , 10075 , OO0O000 , OO0O000 , '' )
  i1OOoO . append ( I1Ii )
  if 37 - 37: OoooooooOO - O0 - OOooOOo
def o0o0O0O00oOOo ( img , name , url ) :
 img = img
 name = name
 III1IiiI = iIi1 ( url )
 IIIII11I1IiI = re . compile ( '<div id="(.+?)" class="player-content"><iframe class="playerframe" src="(.+?)" scrolling="no".+?</iframe></div>' ) . findall ( III1IiiI )
 for iIIIiIi , url in IIIII11I1IiI :
  print '>>>>>>>>>>>>>>>>>>>>>>>>>>> before' + url
  OO0O0 = ( url ) . replace ( 'player' , 'watch' ) + '&fv=&sou='
  print '<<<<<<<<<<<<<<<<<<<<<<<<<<< after' + OO0O0
  I11I11 = ( iIIIiIi ) . replace ( 'play-' , 'Server ' )
  ii1ii11IIIiiI ( I11I11 , OO0O0 , 10076 , img , img , '' )
  if 69 - 69: I1IiI
def OO0OoOO0o0o ( url ) :
 III1IiiI = iIi1 ( url )
 IIIII11I1IiI = re . compile ( '<source src="(.+?)" type="video/mp4">' ) . findall ( III1IiiI )
 for ooI1111i in IIIII11I1IiI :
  if '=m' in ooI1111i :
   iIIii ( ooI1111i )
  elif 'php' in ooI1111i :
   OO0OoOO0o0o ( url )
  else :
   III1IiiI = iIi1 ( ooI1111i )
   IIIII11I1IiI = re . compile ( 'content="(.+?)">' ) . findall ( III1IiiI )
   for o00O0O in IIIII11I1IiI :
    iIIii ( ooI1111i )
    if 20 - 20: i1IIi - II11i1iIiII1
    if 30 - 30: iI / OOOo0
    if 35 - 35: OoOoOO00 % Oo000 . II11i1iIiII1 + II11i1iIiII1 % OoOoOO00 % OoOoOO00
def ooOoO00 ( url ) :
 III1IiiI = iIi1 ( url )
 Ii1IIiI1i = re . compile ( '<td id=".+?" class="today">.+?title="(.+?)">(.+?)</td>' , re . DOTALL ) . findall ( III1IiiI )
 for Ii1i1iI1iIIi , o0O00Oo0 in Ii1IIiI1i :
  print 'there ><><><><><><><><><><><><'
  Ii1i1iI1iIIi = Ii1i1iI1iIIi
  IIIII11I1IiI = re . compile ( '<p><a href=".+?" rel=".+?">(.+?)</a>.+?<br /><a href=".+?">(.+?)</a>.+?</p>' , re . DOTALL ) . findall ( str ( o0O00Oo0 ) )
  for I1Ii , O0oo00o0O in IIIII11I1IiI :
   print 'here <><><><><><><><><><><><>'
   O00Oo000ooO0 ( '[COLORred]' + Ii1i1iI1iIIi + '[/COLOR] - ' + I1Ii + ' - [COLORgreen]' + O0oo00o0O + '[/COLOR]' , i1111 ( 'aHR0cDovL3d3dy5wb2dkZXNpZ24uY28udWsvY2F0Lw==' ) , 10070 , ii11iIi1I + 'loader.png' , i1iiIII111ii , '' )
 IIiII111iiI1I = re . compile ( '<td id=".+?" class="day">.+?title="(.+?)">(.+?)</td>' , re . DOTALL ) . findall ( III1IiiI )
 for Ii1i1iI1iIIi , IiII111i1i11 in IIiII111iiI1I :
  print 'there ><><><><><><><><><><><><'
  Ii1i1iI1iIIi = Ii1i1iI1iIIi
  IIIII11I1IiI = re . compile ( '<p><a href=".+?" rel=".+?">(.+?)</a>.+?<br /><a href=".+?">(.+?)</a>.+?</p>' , re . DOTALL ) . findall ( str ( IiII111i1i11 ) )
  for I1Ii , O0oo00o0O in IIIII11I1IiI :
   print 'here <><><><><><><><><><><><>'
   O00Oo000ooO0 ( '[COLORred]' + Ii1i1iI1iIIi + '[/COLOR] - ' + I1Ii + ' - [COLORgreen]' + O0oo00o0O + '[/COLOR]' , i1111 ( 'aHR0cDovL3d3dy5wb2dkZXNpZ24uY28udWsvY2F0Lw==' ) , 10070 , ii11iIi1I + 'loader.png' , i1iiIII111ii , '' )
   if 40 - 40: II11i1iIiII1 * Ooo0OO0 * i11iIiiIii
   if 57 - 57: II11i1iIiII1
   if 29 - 29: I1IiI - Ooo0OO0 * OoooooooOO + OoooooooOO . OoOoOO00 + OoooooooOO
def O0o000Oo ( url ) :
 III1IiiI = iIi1 ( url )
 IIiII111iiI1I = re . compile ( '<li class="yt-uix-scroller-scroll-unit "(.+?)</li>' , re . DOTALL ) . findall ( III1IiiI )
 for IIiII111iiI1I in IIiII111iiI1I :
  I1Ii = re . compile ( 'data-video-title="(.+?)"' ) . findall ( str ( IIiII111iiI1I ) )
  for I1Ii in I1Ii :
   I1Ii = ( I1Ii ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&amp;' , '&' )
  url = re . compile ( '<a href="/w(.+?)&' ) . findall ( str ( IIiII111iiI1I ) )
  for url in url :
   url = 'https://www.youtube.com/w' + url
  ooo = re . compile ( '<img.+?="(.+?)"' ) . findall ( str ( IIiII111iiI1I ) )
  for ooo in ooo :
   ooo = 'http:' + ooo
  ii1ii11IIIiiI ( '[COLORgreen]' + I1Ii + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , ooo , '' , '' )
  if 27 - 27: II11i1iIiII1 % OOOo0
  if 73 - 73: Oo000
  if 70 - 70: iIii1I11I1II1
  if 31 - 31: Ooo0OO0 - OOOo0 % iIii1I11I1II1
def oooo0OOOO ( url ) :
 if 54 - 54: i1IIi / Ooo0OO0 % Ooo00oOo00o . iI
 IIOoO = [ ]
 III1IiiI = iIi1 ( url )
 IIIII11I1IiI = re . compile ( '<div class="explore-list">.+?<div class="el-img"><a href="(.+?)" class=".+?"><img src="(.+?)" alt=".+?<h3>(.+?)</h3><p>(.+?)</p></div>' , re . DOTALL ) . findall ( III1IiiI )
 for ooI1111i , OO0O000 , I1Ii , iiI1IIIi in IIIII11I1IiI :
  I1Ii = ( I1Ii ) . replace ( '&#039;' , '\'' ) . replace ( '&amp;' , '&' ) . replace ( '&quot;' , '"' )
  II11IiIi11 = iIi1 ( ooI1111i )
  IIOOO0O00O0OOOO = re . compile ( '<!-- # player # -->.+?<iframe title=".+?".+?src="http://www.youtube.com/embed/(.+?)?autohide.+?<!-- detail box -->(.+?)</div>' , re . DOTALL ) . findall ( II11IiIi11 )
  for I1iiii1I , OOo0 in IIOOO0O00O0OOOO :
   oO00ooooO0o = re . compile ( '<p>(.+?)</p>' , re . DOTALL ) . findall ( str ( OOo0 ) )
   for oo0o in oO00ooooO0o :
    if I1Ii in IIOoO :
     pass
    else :
     ii1ii11IIIiiI ( I1Ii , I1iiii1I , 8043 , OO0O000 , OO0O000 , oo0o )
     ii111 ( 'movies' , 'INFO' )
     IIOoO . append ( I1Ii )
     if 51 - 51: iI % OOOo0
     if 60 - 60: OOOo0 / Oo000 . OOOo0 / OoO0O0 . Ooo0OO0
def OO0000o ( url ) :
 i1I1i1 = O0OoooO0 ( url )
 IIIII11I1IiI = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( i1I1i1 )
 for url , ooo0O0o00O , oo0o , I1i11 , I1Ii in IIIII11I1IiI :
  O00Oo000ooO0 ( I1Ii , url , 10065 , ooo0O0o00O , I1i11 , oo0o )
 ii111 ( 'movies' , 'INFO' )
 if 12 - 12: i1IIi + i1IIi - ii11ii1ii * Oo % Oo - OoOoOO00
def o0O ( ) :
 i1111I1I = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 i1i = 'https://www.youtube.com/results?search_query=' + ( i1111I1I ) . replace ( ' ' , '+' )
 oOOoo00O00o = i1i . lower ( )
 III1IiiI = iIi1 ( oOOoo00O00o )
 IIIII11I1IiI = re . compile ( '<img src="(.+?)" alt=.+?yt-lockup-title "><a href="(.+?)".+?data-sessionlink=.+?" title="(.+?)".+?<span class="accessible-description".+?>(.+?)</span>.+?<div class="yt-lockup-description yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr">(.+?)</div>' , re . DOTALL ) . findall ( III1IiiI )
 next = re . compile ( '<a href="(.+?)" class="yt-uix-button.+?class="yt-uix-button-content">Next.+?</span></a>' ) . findall ( III1IiiI )
 for OOOooo in next :
  OOOooo = 'https://www.youtube.com' + OOOooo
  O00Oo000ooO0 ( '[COLORgreen] NEXT [/COLOR]' , OOOooo , 10065 , ii11iIi1I + 'Next.png' , i1iiIII111ii , '' )
 for OO0O000 , OOOooo , I1Ii , OooO0OO , OOo0 in IIIII11I1IiI :
  Ooo . append ( I1Ii )
  ii111 ( 'tvshows' , 'INFO' )
  ooo = 'http:' + ( OO0O000 ) . replace ( 'https:' , '' )
  print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>' + ooo
  OOOooo = 'http://www.youtube.com' + OOOooo
  ii1ii11IIIiiI ( '[COLORred]' + OooO0OO + '[/COLOR]' + '[COLORgreen]' + I1Ii + '[/COLOR]' , ( OOOooo ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , ooo , ooo , OOo0 )
 else :
  IIIII11I1IiI = re . compile ( '<img src="(.+?)" alt=.+?yt-lockup-title "><a href="(.+?)".+?data-sessionlink=.+?" title="(.+?)".+?<span class="accessible-description".+?>(.+?)</span>' , re . DOTALL ) . findall ( III1IiiI )
  for OO0O000 , OOOooo , I1Ii , OooO0OO in IIIII11I1IiI :
   print 'im doing it'
   ii111 ( 'tvshows' , 'INFO' )
   ooo = 'http:' + ( OO0O000 ) . replace ( 'https:' , '' )
   OOOooo = 'http://www.youtube.com' + OOOooo
   if '&' in OOOooo :
    print ' i got here'
    III1IiiI = iIi1 ( OOOooo )
    IIiII111iiI1I = re . compile ( '<li class="yt-uix-scroller-scroll-unit "(.+?)</li>' , re . DOTALL ) . findall ( III1IiiI )
    for IIiII111iiI1I in IIiII111iiI1I :
     I1Ii = re . compile ( 'data-video-title="(.+?)"' ) . findall ( str ( IIiII111iiI1I ) )
     for I1Ii in I1Ii :
      I1Ii = ( I1Ii ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&amp;' , '&' )
     OOOooo = re . compile ( '<a href="/w(.+?)&' ) . findall ( str ( IIiII111iiI1I ) )
     for OOOooo in OOOooo :
      OOOooo = 'https://www.youtube.com/w' + OOOooo
     ooo = re . compile ( '<img.+?="(.+?)"' ) . findall ( str ( IIiII111iiI1I ) )
     for ooo in ooo :
      ooo = 'http:' + ooo
     ii1ii11IIIiiI ( '[COLORred]' + OooO0OO + '[/COLOR]' + '[COLORgreen]' + I1Ii + '[/COLOR]' , ( OOOooo ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , ooo , i1iiIII111ii , '' )
   elif I1Ii in Ooo :
    pass
   elif 'user' in OOOooo or 'elete' in I1Ii :
    pass
   elif 'hannel' in OOOooo :
    print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' + OOOooo
    III1IiiI = iIi1 ( OOOooo )
    o0OOo0o0O0O = re . compile ( 'data-thumb="(.+?)".+?href="(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( III1IiiI )
    for OO0O000 , OOOooo , I1Ii in o0OOo0o0O0O :
     if 'outube' in OOOooo or 'list' in OOOooo :
      pass
     elif 'atch' in OOOooo :
      OOOooo = ( OOOooo ) . replace ( '/watch?v=' , '' )
      ii1ii11IIIiiI ( '[COLORred]' + OooO0OO + '[/COLOR]' + '[COLORgreen]' + I1Ii + '[/COLOR]' , ( OOOooo ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , 'http:' + OO0O000 , 'http:' + OO0O000 , '' )
     else :
      pass
   else :
    ii1ii11IIIiiI ( '[COLORred]' + OooO0OO + '[/COLOR]' + '[COLORgreen]' + I1Ii + '[/COLOR]' , ( OOOooo ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , ooo , ooo , '' )
    if 65 - 65: i11iIiiIii
def O0O0o0oOOO ( url ) :
 III1IiiI = iIi1 ( url )
 IIIII11I1IiI = re . compile ( '<img src="(.+?)" alt=.+?yt-lockup-title "><a href="(.+?)".+?data-sessionlink=.+?" title="(.+?)".+?<span class="accessible-description".+?>(.+?)</span>.+?<div class="yt-lockup-description yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr">(.+?)</div>' , re . DOTALL ) . findall ( III1IiiI )
 next = re . compile ( '<a href="(.+?)" class="yt-uix-button.+?class="yt-uix-button-content">Next.+?</span></a>' ) . findall ( III1IiiI )
 for url in next :
  url = 'https://www.youtube.com' + url
  O00Oo000ooO0 ( '[COLORgreen] NEXT [/COLOR]' , url , 10065 , ii11iIi1I + 'Next.png' , i1iiIII111ii , '' )
 for OO0O000 , url , I1Ii , OooO0OO , OOo0 in IIIII11I1IiI :
  Ooo . append ( I1Ii )
  ii111 ( 'tvshows' , 'INFO' )
  ooo = 'http:' + ( OO0O000 ) . replace ( 'https:' , '' )
  print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>' + ooo
  url = 'http://www.youtube.com' + url
  ii1ii11IIIiiI ( '[COLORred]' + OooO0OO + '[/COLOR]' + '[COLORgreen]' + I1Ii + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , ooo , ooo , OOo0 )
 else :
  IIIII11I1IiI = re . compile ( '<img src="(.+?)" alt=.+?yt-lockup-title "><a href="(.+?)".+?data-sessionlink=.+?" title="(.+?)".+?<span class="accessible-description".+?>(.+?)</span>' , re . DOTALL ) . findall ( III1IiiI )
  for OO0O000 , url , I1Ii , OooO0OO in IIIII11I1IiI :
   ii111 ( 'tvshows' , 'INFO' )
   ooo = 'http:' + ( OO0O000 ) . replace ( 'https:' , '' )
   url = 'http://www.youtube.com' + url
   if '&' in url :
    III1IiiI = iIi1 ( url )
    IIiII111iiI1I = re . compile ( '<li class="yt-uix-scroller-scroll-unit "(.+?)</li>' , re . DOTALL ) . findall ( III1IiiI )
    for IIiII111iiI1I in IIiII111iiI1I :
     I1Ii = re . compile ( 'data-video-title="(.+?)"' ) . findall ( str ( IIiII111iiI1I ) )
     for I1Ii in I1Ii :
      I1Ii = ( I1Ii ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&amp;' , '&' )
     url = re . compile ( '<a href="/w(.+?)&' ) . findall ( str ( IIiII111iiI1I ) )
     for url in url :
      url = 'https://www.youtube.com/w' + url
     ooo = re . compile ( '<img.+?="(.+?)"' ) . findall ( str ( IIiII111iiI1I ) )
     for ooo in ooo :
      ooo = 'http:' + ooo
     ii1ii11IIIiiI ( '[COLORred]' + OooO0OO + '[/COLOR]' + '[COLORgreen]' + I1Ii + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , ooo , i1iiIII111ii , '' )
   elif I1Ii in Ooo :
    pass
   elif 'user' in url or 'elete' in I1Ii :
    pass
   elif 'hannel' in url :
    print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' + url
    III1IiiI = iIi1 ( url )
    o0OOo0o0O0O = re . compile ( 'data-thumb="(.+?)".+?href="(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( III1IiiI )
    for OO0O000 , url , I1Ii in o0OOo0o0O0O :
     if 'outube' in url or 'list' in url :
      pass
     elif 'atch' in url :
      url = ( url ) . replace ( '/watch?v=' , '' )
      ii1ii11IIIiiI ( '[COLORred]' + OooO0OO + '[/COLOR]' + '[COLORgreen]' + I1Ii + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , 'http:' + OO0O000 , 'http:' + OO0O000 , '' )
     else :
      pass
   else :
    ii1ii11IIIiiI ( '[COLORred]' + OooO0OO + '[/COLOR]' + '[COLORgreen]' + I1Ii + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , ooo , ooo , '' )
    if 67 - 67: I1IiI + ii11ii1ii . OOooOOo . OoOoOO00
    if 98 - 98: OoOo00o
def OooooO0oOOOO ( ) :
 if oo0o0O00 == 'insert_password' :
  oOOoo00O0O . ok ( '[COLORgreen]Donators Login[/COLOR]' , 'You need to set username and password to access this' , 'These are unique and provided to donators to help with server and stream costs' , 'Donate @ [COLORgreen]http://architects.x10host.com[/COLOR]' )
  o0oO0 . openSettings ( sys . argv [ 0 ] )
 else :
  o0O00oOOoo = open ( o0 )
  IIIII11I1IiI = re . compile ( 'plugin.video.GenieTv.+?2Flive%2F(.+?)%2F(.+?)%2F' ) . findall ( str ( o0O00oOOoo ) )
  for i1I1iIi , IIii11Ii1i1I in IIIII11I1IiI :
   if i1I1iIi == 'needs replacing' or IIii11Ii1i1I == 'needs replacing' :
    Oooo0O ( )
  O00Oo000ooO0 ( '[COLORgreen]DONATORS LIST[/COLOR]' , iiI1IiI + '/thelistnew.m3u' , 7080 , ii11iIi1I + 'GTVIPTV.png' , i1iiIII111ii , '' )
  if 90 - 90: iIii1I11I1II1 % II11i1iIiII1
def OoO0O00O0oo0O ( ) :
 i1iiIIiiI111 . ok ( '[COLOR=white]ReCreate Addons.ini[/COLOR]' , 'If it doesnt work ensure login details are correct and retry' , '' , 'This will allow access to streams in guide without linking to favourites' )
 i1iiIIiiI111 . ok ( '[COLOR=red]Reset Any Previous linked streams[/COLOR]' , 'For best results you\'ll need to clear previous linked streams' , 'Go to TVGuide tab then reset database at the bottom' , 'Then go back and guide should be all linked up and ready to go' )
 o0oO0 . openSettings ( sys . argv [ 0 ] )
 Oooo0O ( )
 i1iiIIiiI111 . ok ( '[COLOR=yellow]Done[/COLOR]' , 'Done' , 'Easy as that' , 'Now Go to guide and it should link your GTV streams' )
 if 36 - 36: Oo000 + O0 - i1I111ii1II1i - O0 % iI . OOO0OOO00oo
def oooiiI ( ) :
 try :
  oOIIiIi = gui . TVGuide ( )
  oOIIiIi . doModal ( )
  del oOIIiIi
  if 91 - 91: ii11ii1ii * Oo / OOOo0 . O0 + Ooo00oOo00o + I1IiI
 except :
  import sys
  import traceback as tb
  ( iIIi , iiI1iI111ii1i , traceback ) = sys . exc_info ( )
  tb . print_exception ( iIIi , iiI1iI111ii1i , traceback )
  if 32 - 32: OoOoOO00 * I1IiI % i1IIi - OoOo00o + iIii1I11I1II1 + ii11ii1ii
def OO0O0Oo000 ( ) :
 O00Oo000ooO0 ( 'Full Backup' , '' , 10061 , ii11iIi1I + 'Backup.png' , i1iiIII111ii , 'Back Up Your Full System' )
 if os . path . exists ( oOoOooOo0o0 ) :
  O00Oo000ooO0 ( 'Backup Genie Favourites' , OOOooo , 10062 , ii11iIi1I + 'Backup.png' , i1iiIII111ii , 'Back Up Your favourites' )
 if os . path . exists ( IIiiiiiiIi1I1 ) :
  O00Oo000ooO0 ( 'Backup Ivue Config' , IIiiiiiiIi1I1 , 10062 , ii11iIi1I + 'Backup.png' , i1iiIII111ii , 'Back Up Your master.db' )
 if os . path . exists ( I1IIIii ) :
  O00Oo000ooO0 ( 'Backup Kodi Favourites' , I1IIIii , 10062 , ii11iIi1I + 'Backup.png' , i1iiIII111ii , 'Back Up Your favourites.xml' )
  if 41 - 41: i1IIi - iI - i1I111ii1II1i
  if 8 - 8: Ooo00oOo00o + OoO0O0 - OOooOOo % Oo % OOooOOo * OOO0OOO00oo
  if 9 - 9: Oo - i11iIiiIii - Oo000 * i1I111ii1II1i + II11i1iIiII1
zip = o0oO0 . getSetting ( 'zip' )
iIIII = xbmc . translatePath ( os . path . join ( zip ) )
def iIIIiiI1i1i ( ) :
 iIII = xbmc . translatePath ( os . path . join ( zip , 'testCBFolder' ) )
 if not os . path . exists ( zip ) :
  i1iiIIiiI111 . ok ( '[COLOR=white]Origin[/COLOR]' , 'The download location you have stored does not exist .\nPlease update the addon settings and try again.' , '' , '' )
  o0oO0 . openSettings ( sys . argv [ 0 ] )
  if 70 - 70: OoOo00o / iIii1I11I1II1
  if 85 - 85: OoooooooOO % i1IIi * OoooooooOO / ii11ii1ii
  if 96 - 96: OoooooooOO + OOO0OOO00oo
def iiII1i11i ( name , url , description ) :
 if 'Backup' in name :
  if 'Genie' in name :
   url = oOoOooOo0o0
  elif 'Ivue' in name :
   url = IIiiiiiiIi1I1
  elif 'Kodi' in name :
   url = I1IIIii
  iIIIiiI1i1i ( )
  IiIi = open ( url ) . read ( )
  OOOOO0O00 = os . path . join ( iIIII , description . split ( 'Your ' ) [ 1 ] )
  Iii = open ( OOOOO0O00 , mode = 'w' )
  Iii . write ( IiIi )
  Iii . close ( )
 else :
  if 'guisettings.xml' in description :
   iIIiIiI1I1 = open ( os . path . join ( iIIII , description . split ( 'Your ' ) [ 1 ] ) ) . read ( )
   ooO = '<setting type="(.+?)" name="%s.(.+?)">(.+?)</setting>' % skin
   IIIII11I1IiI = re . compile ( ooO ) . findall ( iIIiIiI1I1 )
   for type , ii , OO0O0Ooo in IIIII11I1IiI :
    OO0O0Ooo = OO0O0Ooo . replace ( '&quot;' , '' ) . replace ( '&amp;' , '&' )
    xbmc . executebuiltin ( "Skin.Se	t%s(%s,%s)" % ( type . title ( ) , ii , OO0O0Ooo ) )
  else :
   OOOOO0O00 = os . path . join ( url )
   IiIi = open ( os . path . join ( iIIII , description . split ( 'Your ' ) [ 1 ] ) ) . read ( )
   Iii = open ( OOOOO0O00 , mode = 'w' )
   Iii . write ( IiIi )
   Iii . close ( )
 i1iiIIiiI111 . ok ( "[COLOR=white]Origin[/COLOR]" , "" , 'All Done !' , '' )
 if 77 - 77: OOooOOo / OoooooooOO
 if 46 - 46: OOooOOo % iIii1I11I1II1 . OoOo00o % OoOo00o + i11iIiiIii
 if 72 - 72: iIii1I11I1II1 * i1I111ii1II1i % II11i1iIiII1 / Ooo00oOo00o
 if 35 - 35: II11i1iIiII1 + i1IIi % ii11ii1ii % iI + OOO0OOO00oo
def iiiI ( ) :
 I1ii1 = 1
 iIIIiiI1i1i ( )
 O00 = xbmc . translatePath ( os . path . join ( iIIII , 'Build Backup' , 'Full Backup' , '' ) )
 Oo0o0000OOoO = xbmc . translatePath ( os . path . join ( iIIII , 'Build Backup' , 'my_full_backup.zip' ) )
 IiIi1I1ii111 = xbmc . translatePath ( os . path . join ( iIIII , 'Build Backup' , 'my_full_backup_GUI_Settings.zip' ) )
 if not os . path . exists ( O00 ) :
  os . makedirs ( O00 )
 IiIiIi = oOOoo00O0O . input ( 'Enter a name for this backup' , type = xbmcgui . INPUT_ALPHANUM )
 if ( not IiIiIi ) : return False , 0
 IIIII1 = IiIiIi
 iIi1Ii1i1iI = xbmc . translatePath ( os . path . join ( O00 , IIIII1 + '.zip' ) )
 IIiI1 = [ 'plugin.video.GenieTv' ]
 i1iI1 = [ "xbmc.log" , "xbmc.old.log" , "kodi.log" , "kodi.old.log" , '.DS_Store' , '.setup_complete' , 'XBMCHelper.conf' ]
 ii1 = [ 'plugin.video.GenieTv' , 'repository.origin' , 'cache' , 'system' , 'Thumbnails' , "peripheral_data" , 'library' , 'keymaps' ]
 I1IiiI1ii1i = [ "xbmc.log" , "xbmc.old.log" , "kodi.log" , "kodi.old.log" , "Textures13.db" , '.DS_Store' , '.setup_complete' , 'XBMCHelper.conf' , 'advancedsettings.xml' ]
 O0o = "Creating full backup of existing build"
 oO0OoO00o = "Creating Community Build"
 II1iiiiII = "Archiving..."
 O0OoOO0oo0 = ""
 oOO = "Please Wait"
 O0o0OO0000ooo ( oooOOOOO , iIi1Ii1i1iI , oO0OoO00o , II1iiiiII , O0OoOO0oo0 , oOO , ii1 , I1IiiI1ii1i )
 time . sleep ( 1 )
 iIIII1iIIii = xbmc . translatePath ( os . path . join ( O00 , IIIII1 + '_guisettings.zip' ) )
 oOOO00o000o = zipfile . ZipFile ( iIIII1iIIii , mode = 'w' )
 try :
  oOOO00o000o . write ( xbmc . translatePath ( os . path . join ( oooOOOOO , 'userdata' , 'profiles.xml' ) ) , 'profiles.xml' , zipfile . ZIP_DEFLATED )
 except : pass
 oOOO00o000o . close ( )
 if I1ii1 == 0 :
  i1iiIIiiI111 . ok ( "FAILED!" , 'The guisettings.xml file could not be found on your' , 'system, please reboot and try again.' , '' )
 else :
  i1iiIIiiI111 . ok ( "SUCCESS!" , 'You Are Now Backed Up. If you\'d like to share this build with' , 'the community please post details on the forum at' , '[COLOR=blue][B]http://rh-project.info[/COLOR][/B]' )
  i1iiIIiiI111 . ok ( "Build Locations" , 'Full Backup (only used to restore on this device): [COLOR=yellow]' + Oo0o0000OOoO , '[/COLOR]Universal Backup (can be used on any device): [COLOR=yellow]' + iIi1Ii1i1iI + '[/COLOR]' )
  if 9 - 9: OOO0OOO00oo + iI / iI
def O0o0OO0000ooo ( sourcefile , destfile , message_header , message1 , message2 , message3 , exclude_dirs , exclude_files ) :
 Ii1I11ii1i = zipfile . ZipFile ( destfile , 'w' , zipfile . ZIP_DEFLATED )
 O0iIiIIIIIii = len ( sourcefile )
 OOo0ii11I1 = [ ]
 oO0oo = [ ]
 Oo0oO0ooo . create ( message_header , message1 , message2 , message3 )
 for Ii111iIi1iIi , IIIIIo0ooOoO000oO , OOo in os . walk ( sourcefile ) :
  for file in OOo :
   oO0oo . append ( file )
 i1i11I1I1iii1 = len ( oO0oo )
 for Ii111iIi1iIi , IIIIIo0ooOoO000oO , OOo in os . walk ( sourcefile ) :
  IIIIIo0ooOoO000oO [ : ] = [ I1iii11 for I1iii11 in IIIIIo0ooOoO000oO if I1iii11 not in exclude_dirs ]
  OOo [ : ] = [ Iii for Iii in OOo if Iii not in exclude_files ]
  for file in OOo :
   OOo0ii11I1 . append ( file )
   ooo0O = len ( OOo0ii11I1 ) / float ( i1i11I1I1iii1 ) * 100
   Oo0oO0ooo . update ( int ( ooo0O ) , "Backing Up" , '[COLOR yellow]%s[/COLOR]' % file , 'Please Wait' )
   iII1iii = os . path . join ( Ii111iIi1iIi , file )
   if not 'temp' in IIIIIo0ooOoO000oO :
    if not 'plugin.program.originwizard' in IIIIIo0ooOoO000oO :
     import time
     i11i1iiiII = '01/01/1980'
     ooOO0oO0oo00o = time . strftime ( '%d/%m/%Y' , time . gmtime ( os . path . getmtime ( iII1iii ) ) )
     if ooOO0oO0oo00o > i11i1iiiII :
      Ii1I11ii1i . write ( iII1iii , iII1iii [ O0iIiIIIIIii : ] )
 Ii1I11ii1i . close ( )
 Oo0oO0ooo . close ( )
 if 83 - 83: OOO0OOO00oo - OoOoOO00 - OoOo00o
 if 3 - 3: OoO0O0
def i1iiIiI1Ii1i ( ) :
 II1i1IiiIIi11 ( )
 O00Oo000ooO0 ( '[COLORgreen]SCOOBY STREAMS[/COLOR]' , ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvdHZjYXRzLnBocA==' ) ) , 1016 , ii11iIi1I + 'scoob.png' , i1iiIII111ii , '' )
 O00Oo000ooO0 ( '[COLORgreen]SCOOBY SCRAPES[/COLOR]' , iiI1IiI , 1024 , ii11iIi1I + 'scoob.png' , i1iiIII111ii , '' )
 if 22 - 22: Ooo0OO0 / i11iIiiIii
 if 62 - 62: Ooo00oOo00o / ii11ii1ii
def ii1O000OOO0OOo ( ) :
 II1i1IiiIIi11 ( )
 O00Oo000ooO0 ( '[COLORgreen]SEARCH MOVIES[/COLOR]' , iiI1IiI , 9001 , ii11iIi1I + 'MOVIESv.png' , i1iiIII111ii , '' )
 O00Oo000ooO0 ( '[COLORgreen]SEARCH SERIES[/COLOR]' , iiI1IiI , 9002 , ii11iIi1I + 'TVSHOWSv.png' , i1iiIII111ii , '' )
 O00Oo000ooO0 ( '[COLORgreen]SEARCH CARTOONS[/COLOR]' , '' , 10005 , ii11iIi1I + 'ORIGINCARTOON' , i1iiIII111ii , '' )
 if 32 - 32: i1I111ii1II1i * O0
 if 100 - 100: II11i1iIiII1 % iIii1I11I1II1 * OoOoOO00 - OoOo00o
 if 92 - 92: II11i1iIiII1
 if 22 - 22: Oo % OoOo00o * ii11ii1ii / Oo000 % i11iIiiIii * iI
def Oo00OoOo ( ) :
 II1i1IiiIIi11 ( )
 O00Oo000ooO0 ( '[COLORgreen]RADIO[/COLOR]' , iiI1IiI , 1013 , ii11iIi1I + 'radio.png' , i1iiIII111ii , '' )
 if o0oO0 . getSetting ( 'CONCERTS' ) == 'true' :
  O00Oo000ooO0 ( '[COLORgreen]CONCERTS[/COLOR]' , ( i1111 ( 'aHR0cHM6Ly93d3cucmVkZGl0LmNvbS9yL2Z1bGxjb25jZXJ0cy8=' ) ) , 7050 , ii11iIi1I + 'concerts.png' , i1iiIII111ii , '' )
 O00Oo000ooO0 ( '[COLORgreen]MUSIC[/COLOR]' , iiI1IiI , 1030 , ii11iIi1I + 'MUSIC.png' , i1iiIII111ii , '' )
 O00Oo000ooO0 ( '[COLORgreen]MUSIC ARCHIVE[/COLOR]' , iiI1IiI + ( i1111 ( 'L3ZvZC91cmxzL211c2ljLnBocA==' ) ) , 1010 , ii11iIi1I + 'MUSIC.png' , i1iiIII111ii , '' )
 O00Oo000ooO0 ( '[COLORgreen]MUSIC SEARCH[/COLOR]' , iiI1IiI , 1111 , ii11iIi1I + 'search.png' , i1iiIII111ii , '' )
 O00Oo000ooO0 ( '[COLORgreen]KODIBLE AUDIO BOOKS[/COLOR]' , 'http://doremisa.com/audiobooks/' , 30000 , ii11iIi1I + 'kodible.png' , i1iiIII111ii , '' )
 if 24 - 24: i11iIiiIii - OoO0O0
 ii111 ( 'movies' , 'MAIN' )
 if 21 - 21: iI
def OoO00 ( ) :
 II1i1IiiIIi11 ( )
 if 85 - 85: Oo * Oo * OOOo0 . OoooooooOO . i1I111ii1II1i * II11i1iIiII1
 ii1ii11IIIiiI ( 'DELETE CACHE' , 'url' , 14 , ii11iIi1I + 'MAIN5.png' , i1iiIII111ii , '' )
 ii1ii11IIIiiI ( 'DELETE PACKAGES' , 'url' , 6 , ii11iIi1I + 'MAIN4.png' , i1iiIII111ii , '' )
 ii1ii11IIIiiI ( 'FORCE REFRESH' , 'url' , 10 , ii11iIi1I + 'MAIN3.png' , i1iiIII111ii , 'Force Refresh All Repos' )
 if 65 - 65: Oo000 * OoO0O0
 ii1ii11IIIiiI ( 'CHECK MY IP' , 'url' , 12 , ii11iIi1I + 'MAIN2.png' , i1iiIII111ii , '' )
 ii1ii11IIIiiI ( 'ANDROID ONLY DELETE TEXTURE13.DB&THUBMNAIL FOLDER' , 'url' , 13 , ii11iIi1I + 'MAIN1.png' , i1iiIII111ii , 'Only Works On Android On Windows It Deletes Your Thumnails Folder But Does Not Delete The Textures13.db' )
 O00Oo000ooO0 ( '[COLORgreen]ADVANCED SETTINGS XML[/COLOR]' , iiI1IiI , 4 , ii11iIi1I + 'XML.png' , i1iiIII111ii , '' )
 O00Oo000ooO0 ( '[COLORgreen]URL FIXES[/COLOR]' , iiI1IiI , 20 , ii11iIi1I + 'URLFIX.png' , i1iiIII111ii , '' )
 ii111 ( 'movies' , 'MAIN' )
 if 79 - 79: OoooooooOO - OOOo0
 if 69 - 69: iI
def iI1Ii11111iIi ( ) :
 II1i1IiiIIi11 ( )
 O00Oo000ooO0 ( '[COLORgreen]REPOS[/COLOR]' , ( i1111 ( 'aHR0cDovL21pcnJvcnMua29kaS50di9hZGRvbnMv' ) ) , 2030 , ii11iIi1I + 'repos.png' , i1iiIII111ii , '' )
 O00Oo000ooO0 ( '[COLORgreen]NEW[/COLOR]' , iiI1IiI , 22 , ii11iIi1I + 'NEW.png' , i1iiIII111ii , '' )
 O00Oo000ooO0 ( '[COLORgreen]IPTV[/COLOR]' , iiI1IiI , 23 , ii11iIi1I + 'IPTV.png' , i1iiIII111ii , '' )
 O00Oo000ooO0 ( '[COLORgreen]VIDEO[/COLOR]' , iiI1IiI , 24 , ii11iIi1I + 'VIDEO.png' , i1iiIII111ii , '' )
 O00Oo000ooO0 ( '[COLORgreen]SPORTS[/COLOR]' , iiI1IiI , 25 , ii11iIi1I + 'SPORTS.png' , i1iiIII111ii , '' )
 O00Oo000ooO0 ( '[COLORgreen]KIDS[/COLOR]' , iiI1IiI , 26 , ii11iIi1I + 'KIDS.png' , i1iiIII111ii , '' )
 O00Oo000ooO0 ( '[COLORgreen]MUSIC[/COLOR]' , iiI1IiI , 27 , ii11iIi1I + 'MUSIC.png' , i1iiIII111ii , '' )
 O00Oo000ooO0 ( '[COLORgreen]PROGRAMS[/COLOR]' , iiI1IiI , 28 , ii11iIi1I + 'PROGRAMS.png' , i1iiIII111ii , '' )
 O00Oo000ooO0 ( '[COLORgreen]XXX[/COLOR]' , 'URL' , 29 , ii11iIi1I + 'XXX.png' , i1iiIII111ii , '' )
 ii111 ( 'movies' , 'MAIN' )
 if 95 - 95: II11i1iIiII1 + i11iIiiIii * OoO0O0 - i1IIi * OoO0O0 - iIii1I11I1II1
 if 75 - 75: OoooooooOO * Ooo0OO0
def I1Iiiiiii ( ) :
 II1i1IiiIIi11 ( )
 ii1ii11IIIiiI ( 'CHECK ADVANCED XML' , iiI1IiI , 8 , ii11iIi1I + 'XML.png' , i1iiIII111ii , '' )
 ii1ii11IIIiiI ( 'MUCKYS XML' , iiI1IiI + '/wizard/muckys.xml' , 7 , ii11iIi1I + 'XML.png' , i1iiIII111ii , '' )
 ii1ii11IIIiiI ( '0CACHE XML' , iiI1IiI + '/wizard/0cache.xml' , 7 , ii11iIi1I + 'XML.png' , i1iiIII111ii , '' )
 ii1ii11IIIiiI ( 'MIKEY1234 XML' , iiI1IiI + '/wizard/mikey.xml' , 7 , ii11iIi1I + 'XML.png' , i1iiIII111ii , '' )
 ii1ii11IIIiiI ( 'TUXENS XML' , iiI1IiI + '/wizard/tuxens.xml' , 7 , ii11iIi1I + 'XML.png' , i1iiIII111ii , '' )
 ii1ii11IIIiiI ( 'P2P RECOMMENDED XML1' , iiI1IiI + '/wizard/p2p1.xml' , 7 , ii11iIi1I + 'XML.png' , i1iiIII111ii , '' )
 ii1ii11IIIiiI ( 'P2P RECOMMENDED XML2' , iiI1IiI + '/wizard/p2p2.xml' , 7 , ii11iIi1I + 'XML.png' , i1iiIII111ii , '' )
 ii1ii11IIIiiI ( 'DELETE XML' , iiI1IiI , 11 , ii11iIi1I + 'XML.png' , i1iiIII111ii , '' )
 ii111 ( 'movies' , 'MAIN' )
 if 39 - 39: Ooo0OO0 * Oo + iIii1I11I1II1 - Ooo0OO0 + Oo000
def o0iiiI1I1iIIIi1 ( ) :
 II1i1IiiIIi11 ( )
 ii1ii11IIIiiI ( '[COLORgreen]My Local Zip[/COLOR]' , I11 , 48 , ii11iIi1I + 'MB.png' , i1iiIII111ii , '' )
 ii1ii11IIIiiI ( '[COLORgreen]My Online Zip[/COLOR]' , i11 , 43 , ii11iIi1I + 'MB.png' , i1iiIII111ii , '' )
 if 17 - 17: iIii1I11I1II1 . OoooooooOO / iI % OoOoOO00 % i1IIi / i11iIiiIii
def OOO ( ) :
 II1i1IiiIIi11 ( )
 ii1ii11IIIiiI ( 'INSTALL FTV GUIDE AND OTHER ADDONS REQUIRED' , iiI1IiI + '/wizard/customftv/ftvguide-addons.zip' , 5 , ii11iIi1I + 'FTV4.png' , i1iiIII111ii , '' )
 ii1ii11IIIiiI ( 'FTV GUIDE FIRST RUN SETTINGS' , iiI1IiI + '/wizard/customftv/settings.xml' , 17 , ii11iIi1I + 'FTV3.png' , i1iiIII111ii , '' )
 ii1ii11IIIiiI ( 'FTV GUIDE ADDONS2.INI UPDATE DAILY' , 'http://ren.byethost12.com/addons2.ini' , 16 , ii11iIi1I + 'FTV1.png' , i1iiIII111ii , '' )
 ii1ii11IIIiiI ( 'RESET FTV DATABASE' , 'url' , 18 , ii11iIi1I + 'FTV2.png' , i1iiIII111ii , '' )
 if 30 - 30: OoooooooOO - OoooooooOO . O0 / OoOo00o
 if 31 - 31: Oo000 + OOooOOo . OoooooooOO
 if 89 - 89: OoOoOO00 + i1IIi + OoOoOO00
def IiII1II11I ( ) :
 II1i1IiiIIi11 ( )
 O00Oo000ooO0 ( '[COLORgreen]SKINS[/COLOR]' , iiI1IiI , 33 , ii11iIi1I + 'skinp.png' , i1iiIII111ii , '' )
 O00Oo000ooO0 ( '[COLORgreen]ARTWORK PACKS[/COLOR]' , iiI1IiI , 34 , ii11iIi1I + 'artp.png' , i1iiIII111ii , '' )
 O00Oo000ooO0 ( '[COLORgreen]CREATE UNIVERSAL PATHS[/COLOR]' , oooOOOOO , 35 , ii11iIi1I + 'GUI.png' , i1iiIII111ii , '' )
 ii111 ( 'movies' , 'MAIN' )
 if 54 - 54: Ooo0OO0 + O0 + iI * OoO0O0 - Oo000 % OOO0OOO00oo
def I111 ( url ) :
 iI1I1i11iIIii = iIi1 ( IIIIIiI111I ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIIII11I1IiI = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( iI1I1i11iIIii )
 for I1Ii , url , ooo0O0o00O , I1i11 , OOo0 in IIIII11I1IiI :
  O00Oo000ooO0 ( I1Ii , url , 5 , ooo0O0o00O , I1i11 , OOo0 )
 ii111 ( 'movies' , 'MAIN' )
 if 11 - 11: OOOo0 - Ooo00oOo00o
def iiiiI1i1i ( ) :
 II1i1IiiIIi11 ( )
 O00Oo000ooO0 ( '[COLORgreen]GOTHAM SKINS[/COLOR]' , iiI1IiI , 36 , ii11iIi1I + 'GSKIN.png' , i1iiIII111ii , '' )
 O00Oo000ooO0 ( '[COLORgreen]HELIX SKINS[/COLOR]' , iiI1IiI , 37 , ii11iIi1I + 'HSKIN.png' , i1iiIII111ii , '' )
 O00Oo000ooO0 ( '[COLORgreen]ISENGAARD SKINS[/COLOR]' , oooOOOOO , 38 , ii11iIi1I + 'ISKIN.png' , i1iiIII111ii , '' )
 ii111 ( 'movies' , 'MAIN' )
 if 24 - 24: Ooo0OO0 * OoOo00o . OoOoOO00 / Oo000 + O0
def oO0oOOoo00000 ( url ) :
 iI1I1i11iIIii = iIi1 ( iiI1IiI + oOo00 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIIII11I1IiI = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( iI1I1i11iIIii )
 for I1Ii , url , ooo0O0o00O , I1i11 , OOo0 in IIIII11I1IiI :
  O00Oo000ooO0 ( I1Ii , url , 42 , ooo0O0o00O , I1i11 , OOo0 )
 ii111 ( 'movies' , 'MAIN' )
 if 3 - 3: OoOo00o % i1IIi
def Ii1IIiiIIi ( url ) :
 iI1I1i11iIIii = iIi1 ( iiI1IiI + Oo000o ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIIII11I1IiI = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( iI1I1i11iIIii )
 for I1Ii , url , ooo0O0o00O , I1i11 , OOo0 in IIIII11I1IiI :
  O00Oo000ooO0 ( I1Ii , url , 42 , ooo0O0o00O , I1i11 , OOo0 )
 ii111 ( 'movies' , 'MAIN' )
 if 39 - 39: ii11ii1ii
def O0oOo00o0 ( url ) :
 iI1I1i11iIIii = iIi1 ( iiI1IiI + OooOOOOoO00OoOO ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIIII11I1IiI = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( iI1I1i11iIIii )
 for I1Ii , url , ooo0O0o00O , I1i11 , OOo0 in IIIII11I1IiI :
  O00Oo000ooO0 ( I1Ii , url , 42 , ooo0O0o00O , I1i11 , OOo0 )
 ii111 ( 'movies' , 'MAIN' )
 if 85 - 85: OOO0OOO00oo - iIii1I11I1II1 / O0
def Oo00oo0000OO ( url ) :
 iI1I1i11iIIii = iIi1 ( i1111 ( 'aHR0cHM6Ly9kbC5kcm9wYm94dXNlcmNvbnRlbnQuY29tL3MvN2ZrMjhndDlwb3QxMjJhL0JVSUxEUy50eHQ/ZGw9MA==' ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIIII11I1IiI = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( iI1I1i11iIIii )
 for I1Ii , url , ooo0O0o00O , I1i11 , OOo0 in IIIII11I1IiI :
  O00Oo000ooO0 ( I1Ii , url , 42 , ooo0O0o00O , I1i11 , OOo0 )
 ii111 ( 'movies' , 'MAIN' )
 if 69 - 69: II11i1iIiII1 - Ooo00oOo00o / i11iIiiIii + ii11ii1ii % OoooooooOO
def o000O000 ( url ) :
 iI1I1i11iIIii = iIi1 ( iiI1IiI + ii1oOoO0o0ooo ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIIII11I1IiI = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( iI1I1i11iIIii )
 for I1Ii , url , ooo0O0o00O , I1i11 , OOo0 in IIIII11I1IiI :
  O00Oo000ooO0 ( I1Ii , url , 40 , ooo0O0o00O , I1i11 , OOo0 )
 ii111 ( 'movies' , 'MAIN' )
 if 86 - 86: ii11ii1ii * O0 * Ooo0OO0
def Ooo0oo ( url ) :
 iI1I1i11iIIii = iIi1 ( iiI1IiI + IIi11IIiIii1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIIII11I1IiI = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( iI1I1i11iIIii )
 for I1Ii , url , ooo0O0o00O , I1i11 , OOo0 in IIIII11I1IiI :
  O00Oo000ooO0 ( I1Ii , url , 5 , ooo0O0o00O , I1i11 , OOo0 )
 ii111 ( 'movies' , 'MAIN' )
 if 17 - 17: i1I111ii1II1i + OOO0OOO00oo . Ooo00oOo00o - Oo * i11iIiiIii
def iioOo0OoOOo0 ( ) :
 i1I1i1 = O0OoooO0 ( i1111 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vYXBrdG9vbC9hcGsucGhw' ) )
 IIIII11I1IiI = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( i1I1i1 )
 for OOOooo , ooo , I1Ii in IIIII11I1IiI :
  iII11I1Ii1 ( I1Ii , OOOooo , 2031 , ooo )
  if 92 - 92: iI / iI . ii11ii1ii
def ii1iIi1II ( name , url , description ) :
 iIII = xbmc . translatePath ( os . path . join ( IIIIi1I , 'Download' ) )
 Oo0oO0ooo = xbmcgui . DialogProgress ( )
 Oo0oO0ooo . create ( "Your App Is Downloading" , "Why not check out our website" , '' , 'Http://architects.x10host.com' )
 IiIi1i1ii = os . path . join ( iIII , name + '.apk' )
 try :
  os . remove ( IiIi1i1ii )
 except :
  pass
 downloader . download ( url , IiIi1i1ii , Oo0oO0ooo )
 i1iiIIiiI111 = xbmcgui . Dialog ( )
 i1iiIIiiI111 . ok ( "GenieTv" , "[COLORred]Please press ok, exit kodi and go to your downloads folder to install your app[/COLOR]" , "[COLORblue]Tool Brought To You By Architects@Work[/COLOR]" )
 if 11 - 11: OoOoOO00 / OOooOOo
def IiIi1 ( url ) :
 iIII = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/resources/downloads' ) )
 Oo0oO0ooo = xbmcgui . DialogProgress ( )
 Oo0oO0ooo . create ( "Your fILM Is Downloading" , "Why not check out our website" , '' , 'Http://architects.x10host.com' )
 IiIi1i1ii = os . path . join ( iIII , I1Ii + '.mp4' )
 try :
  os . remove ( IiIi1i1ii )
 except :
  pass
 downloader . download ( url , IiIi1i1ii , Oo0oO0ooo )
 i1iiIIiiI111 = xbmcgui . Dialog ( )
 i1iiIIiiI111 . ok ( "GenieTv" , "[COLORred]Please press ok, Your download With Be Avaiilable Via The My Downloads Button[/COLOR]" , "[COLORblue]Tool Brought To You By Architects@Work[/COLOR]" )
 if 34 - 34: Oo000
 if 91 - 91: iIii1I11I1II1 % OOooOOo . iIii1I11I1II1 % i1IIi / OoOoOO00 * I1IiI
def iioo0o0OoOOO ( name , url , description ) :
 iIII = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 Oo0oO0ooo = xbmcgui . DialogProgress ( )
 Oo0oO0ooo . create ( "Your Art Pack Is Downloading" , "Why not check out our website" , '' , 'Http://architects.x10host.com' )
 IiIi1i1ii = os . path . join ( iIII , name )
 try :
  os . remove ( IiIi1i1ii )
 except :
  pass
 downloader . download ( url , IiIi1i1ii , Oo0oO0ooo )
 ooO0oO00O0o = xbmc . translatePath ( os . path . join ( oo00 ) )
 time . sleep ( 2 )
 Oo0oO0ooo . update ( 0 , "" , "Placing Your Art Please Wait" )
 print '======================================='
 print ooO0oO00O0o
 print '======================================='
 extract . all ( IiIi1i1ii , ooO0oO00O0o , Oo0oO0ooo )
 i1iiIIiiI111 = xbmcgui . Dialog ( )
 i1iiIIiiI111 . ok ( "GenieTv" , "[COLORred]Once complete your artwork will be stored in your Media folder, Accessible via the Homefolder, Enjoy[/COLOR]" )
 if 70 - 70: OoO0O0
 if 16 - 16: OoOo00o - OoooooooOO % Oo
def i11i1iIiii ( url ) :
 iI1I1i11iIIii = iIi1 ( i1111 ( 'aHR0cDovL2dlbmlldHYuYXJjaGl0ZWN0cy54MTBob3N0LmNvbS90ZXN0L3doLnR4dA==' ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIIII11I1IiI = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( iI1I1i11iIIii )
 for I1Ii , url , ooo0O0o00O , I1i11 , OOo0 in IIIII11I1IiI :
  O00Oo000ooO0 ( I1Ii , url , 5 , ooo0O0o00O , I1i11 , OOo0 )
 try :
  iI1I1i11iIIii = iIi1 ( OOO00OO0oOo + oO0o0o0ooO0oO + I1I1iI ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
  IIIII11I1IiI = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( iI1I1i11iIIii )
  for I1Ii , url , ooo0O0o00O , I1i11 , OOo0 in IIIII11I1IiI :
   O00Oo000ooO0 ( I1Ii , url , 5 , ooo0O0o00O , I1i11 , OOo0 )
 except : pass
 ii111 ( 'movies' , 'INFO' )
 if 16 - 16: Ooo0OO0 * I1IiI . II11i1iIiII1 / i1IIi . Ooo00oOo00o - i1IIi
 if 46 - 46: Ooo0OO0 + iIii1I11I1II1 + Oo000 + Ooo00oOo00o . ii11ii1ii
def iIiIi11Ii ( url ) :
 iI1I1i11iIIii = iIi1 ( i1111 ( 'aHR0cDovL2dlbmlldHYuYXJjaGl0ZWN0cy54MTBob3N0LmNvbS90ZXN0L3doLnR4dA==' ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIIII11I1IiI = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( iI1I1i11iIIii )
 for I1Ii , url , ooo0O0o00O , I1i11 , OOo0 in IIIII11I1IiI :
  O00Oo000ooO0 ( I1Ii , url , 43 , ooo0O0o00O , I1i11 , OOo0 )
 try :
  iI1I1i11iIIii = iIi1 ( OOO00OO0oOo + oO0o0o0ooO0oO + I1I1iI ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
  IIIII11I1IiI = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( iI1I1i11iIIii )
  for I1Ii , url , ooo0O0o00O , I1i11 , OOo0 in IIIII11I1IiI :
   O00Oo000ooO0 ( I1Ii , url , 43 , ooo0O0o00O , I1i11 , OOo0 )
 except : pass
 ii111 ( 'movies' , 'INFO' )
 if 23 - 23: OOO0OOO00oo - Oo000 + iI
 if 12 - 12: OOOo0 / II11i1iIiII1 % OOooOOo / i11iIiiIii % OoooooooOO
def IiIi1II11i ( name , url , description ) :
 iIII = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 Oo0oO0ooo = xbmcgui . DialogProgress ( )
 Oo0oO0ooo . create ( "GenieTv" , "Downloading Content" , '' , 'Please Wait' )
 IiIi1i1ii = os . path . join ( iIII , name + '.zip' )
 try :
  os . remove ( IiIi1i1ii )
 except :
  pass
 downloader . download ( url , IiIi1i1ii , Oo0oO0ooo )
 II1II1iIIi11 = xbmc . translatePath ( os . path . join ( 'special://home' , 'addons' ) )
 time . sleep ( 2 )
 Oo0oO0ooo . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print II1II1iIIi11
 print '======================================='
 extract . all ( IiIi1i1ii , II1II1iIIi11 , Oo0oO0ooo )
 i1iiIIiiI111 = xbmcgui . Dialog ( )
 i1iiIIiiI111 . ok ( "GenieTv" , "Press ok to finish install" , "[COLOR yellow]Brought To You By Architects@Work[/COLOR]" )
 OOOOOoo0 ( )
 if 49 - 49: OoooooooOO * iI - Oo . OOO0OOO00oo
 if 89 - 89: II11i1iIiII1 + i1I111ii1II1i * II11i1iIiII1 / II11i1iIiII1
def i11i11 ( name , url , description ) :
 iIII = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 Oo0oO0ooo = xbmcgui . DialogProgress ( )
 Oo0oO0ooo . create ( "GenieTv" , "Downloading " , '' , 'Please Wait' )
 IiIi1i1ii = os . path . join ( iIII , 'plugin.program.GenieTv.install' + '.zip' )
 try :
  os . remove ( IiIi1i1ii )
 except :
  pass
 downloader . download ( url , IiIi1i1ii , Oo0oO0ooo )
 II1II1iIIi11 = xbmc . translatePath ( os . path . join ( 'special://' , 'home' ) )
 time . sleep ( 2 )
 Oo0oO0ooo . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print II1II1iIIi11
 print '======================================='
 extract . all ( IiIi1i1ii , II1II1iIIi11 , Oo0oO0ooo )
 i1iiIIiiI111 = xbmcgui . Dialog ( )
 i1iiIIiiI111 . ok ( "GenieTv" , "Press ok to force close kodi, if unsuccessful using windows Please kill kodi via taskmanager" , "[COLOR yellow]Brought To You By Architects@Work[/COLOR]" )
 OoOoO00O0 ( )
 if 51 - 51: iIii1I11I1II1 / I1IiI + Oo000 - iI + OoOo00o
def IIii1i1iii1 ( name , url , description ) :
 iIII = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 Oo0oO0ooo = xbmcgui . DialogProgress ( )
 Oo0oO0ooo . create ( "GenieTv" , "Downloading " , '' , 'Please Wait' )
 IiIi1i1ii = os . path . join ( iIII , 'plugin.program.GenieTv.install' + '.zip' )
 try :
  os . remove ( IiIi1i1ii )
 except :
  pass
 downloader . download ( url , IiIi1i1ii , Oo0oO0ooo )
 II1II1iIIi11 = xbmc . translatePath ( os . path . join ( 'special://' , 'home' ) )
 time . sleep ( 2 )
 Oo0oO0ooo . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print II1II1iIIi11
 print '======================================='
 extract . all ( IiIi1i1ii , II1II1iIIi11 , Oo0oO0ooo )
 i1iiIIiiI111 = xbmcgui . Dialog ( )
 i1iiIIiiI111 . ok ( "GenieTv" , "Please Disconnect The Power From Your Device. DO NOT EXIT CLEANLY VIA SHUTDOWN" , "[COLOR yellow]Brought To You By Architects@Work[/COLOR]" )
 if 70 - 70: i11iIiiIii % OoOo00o
 if 11 - 11: Ooo0OO0 % ii11ii1ii % i1I111ii1II1i / OoOoOO00 % OoO0O0 - Oo
def OOooO ( name , url , description ) :
 II1II1iIIi11 = xbmc . translatePath ( os . path . join ( 'special://' , 'home' ) )
 Oo0oO0ooo = xbmcgui . DialogProgress ( )
 IiIi1i1ii = os . path . join ( I11 )
 time . sleep ( 2 )
 Oo0oO0ooo . create ( "GenieTv" , "Restoring" , '' , 'Please Wait' )
 print '======================================='
 print II1II1iIIi11
 print '======================================='
 extract . all ( IiIi1i1ii , II1II1iIIi11 , Oo0oO0ooo )
 i1iiIIiiI111 = xbmcgui . Dialog ( )
 i1iiIIiiI111 . ok ( "GenieTv" , "Please Disconnect The Power From Your Device. DO NOT EXIT CLEANLY VIA SHUTDOWN" , "[COLOR yellow]Brought To You By Architects@Work[/COLOR]" )
 if 79 - 79: OoO0O0 % OOO0OOO00oo % OOooOOo % i1I111ii1II1i - OoOoOO00 * OoooooooOO
 if 69 - 69: OOooOOo / Oo
def OoOoO00O0 ( ) :
 IIi = xbmcgui . Dialog ( ) . yesno ( 'Force Close Kodi' , 'You are about to close Kodi' , 'Would you like to continue?' , nolabel = 'No, Cancel' , yeslabel = 'Yes, Close' )
 if IIi == 0 :
  return
 elif IIi == 1 :
  pass
 IiiIIIII1iii = IIiiii ( )
 print "Platform: " + str ( IiiIIIII1iii )
 if IiiIIIII1iii == 'osx' :
  print "############   try osx force close  #################"
  try : os . system ( 'killall -9 XBMC' )
  except : pass
  try : os . system ( 'killall -9 Kodi' )
  except : pass
  i1iiIIiiI111 . ok ( "[COLOR=red][B]WARNING  !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu." , '' )
 elif IiiIIIII1iii == 'linux' :
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
 elif IiiIIIII1iii == 'android' :
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
 elif IiiIIIII1iii == 'windows' :
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
  if 37 - 37: OOooOOo % II11i1iIiII1
def IIiiii ( ) :
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
  if 83 - 83: Oo000 . OoO0O0 + OOO0OOO00oo - Oo000 * OoO0O0 / OoO0O0
  if 39 - 39: OoO0O0 / Oo % Ooo00oOo00o % i11iIiiIii
  if 90 - 90: OoO0O0 - OoooooooOO
def OoOOoO000O00oO ( url ) :
 Oo0oO0ooo . create ( "[COLOR=green]GenieTv[/COLOR]" , "Renaming paths..." , '' , 'Please Wait' )
 for i1OoOO , IIIIIo0ooOoO000oO , OOo in os . walk ( url ) :
  for file in OOo :
   if file . endswith ( ".xml" ) :
    Oo0oO0ooo . update ( 0 , "Fixing" , file , 'Please Wait' )
    iIIiIiI1I1 = open ( ( os . path . join ( i1OoOO , file ) ) ) . read ( )
    iIII1I1i1i = iIIiIiI1I1 . replace ( oooOOOOO , 'special://home/' )
    Iii = open ( ( os . path . join ( i1OoOO , file ) ) , mode = 'w' )
    Iii . write ( str ( iIII1I1i1i ) )
    Iii . close ( )
 OoOoO00O0 ( )
 if 79 - 79: i1I111ii1II1i . Ooo00oOo00o
def IIiI1I1 ( ) :
 i1I1i1 = O0OoooO0 ( i1111 ( 'aHR0cDovL3d3dy5saXN0ZW5saXZlLmV1L3VrLmh0bWw=' ) )
 IIIII11I1IiI = re . compile ( '<tr>.+?<td><a href=".+?"><b>(.+?)</b>.+?<td><a href="(.+?)">' , re . DOTALL ) . findall ( i1I1i1 )
 for I1Ii , OOOooo in IIIII11I1IiI :
  I11I1IIiiII1 ( I1Ii , OOOooo , 222 , ii11iIi1I + 'radio.png' )
  if 31 - 31: OOOo0 * OOO0OOO00oo + OoooooooOO - OoOo00o / OoooooooOO
def I111IIiii1Ii ( ) :
 i1I1i1 = O0OoooO0 ( i1111 ( 'aHR0cDovL3d3dy50b29uamV0LmNvbS8=' ) )
 IIIII11I1IiI = re . compile ( '<a href="(.+?)" style="font-size:.8em;">(.+?)</a>' ) . findall ( i1I1i1 )
 for OOOooo , I1Ii in IIIII11I1IiI :
  iII11I1Ii1 ( '[COLORgreen]' + I1Ii + '[/COLOR]' , 'http://www.toonjet.com/' + OOOooo , 8051 , ii11iIi1I + 'classictoons.png' )
def II1 ( url ) :
 i1I1i1 = O0OoooO0 ( url )
 IIIII11I1IiI = re . compile ( '<a href="(.+?)"><img src="(.+?)"' ) . findall ( i1I1i1 )
 IIOOO0O00O0OOOO = re . compile ( '<a href="(.+?)">.+?</a></td></tr></table>' ) . findall ( i1I1i1 )
 for url , OO0O000 in IIIII11I1IiI :
  if 'ol.gif' in OO0O000 :
   pass
  elif 'link_block_' in OO0O000 :
   pass
  elif '.png' in OO0O000 :
   pass
  else :
   iII11I1Ii1 ( ( OO0O000 ) . replace ( 'http://www.toonjet.com/images/icons/' , '' ) . replace ( 'images/icons/' , '' ) . replace ( '.jpg' , '' ) . replace ( '_icon' , '' ) . replace ( '_' , ' ' ) , 'http://www.toonjet.com/' + url , 8052 , ii11iIi1I + 'vod.png' )
 for url in IIOOO0O00O0OOOO :
  iII11I1Ii1 ( 'NEXT PAGE' , 'http://www.toonjet.com/' + url , 8051 , ii11iIi1I + 'Next.png' )
def iiIIIiIii ( url ) :
 i1I1i1 = O0OoooO0 ( url )
 IIIII11I1IiI = re . compile ( '<iframe width="640" height="480" src="(.+?)" frameborder="0" allowfullscreen></iframe>' ) . findall ( i1I1i1 )
 for url in IIIII11I1IiI :
  I11I1IIiiII1 ( '[COLORgreen]PLAY[/COLOR]' , ( url ) . replace ( 'http://www.youtube.com/embed/' , '' ) . replace ( '?autoplay=0' , '' ) , 8043 , ii11iIi1I + 'classictoons.png' )
  if 23 - 23: OoOo00o + iI . I1IiI * OOOo0 + ii11ii1ii
  if 18 - 18: Ooo0OO0 * OOooOOo . Ooo0OO0 / O0
def iiIII1II ( ) :
 oOo00oOOOOO ( 'Audio Books' , '' , 30011 , ii11iIi1I + 'audiobooks.png' , ii11iIi1I + 'audiobooks.png' , '' )
 oOo00oOOOOO ( 'Kids Audio Books' , '' , 30006 , ii11iIi1I + 'kidsaudiobooks.png' , ii11iIi1I + 'kidsaudiobooks.png' , '' )
 if 85 - 85: OoooooooOO - Ooo00oOo00o - OoO0O0 / II11i1iIiII1 - iI
def iIiI ( ) :
 oOo00oOOOOO ( 'All' , '' , 30001 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
 oOo00oOOOOO ( 'Popular' , '' , 30012 , ii11iIi1I + 'POPULARv.png' , ii11iIi1I + 'POPULARv.png' , '' )
 oOo00oOOOOO ( 'Search' , '' , 30013 , ii11iIi1I + 'search.png' , ii11iIi1I + 'search.png' , '' )
 if 5 - 5: Oo * I1IiI
def ii1I11iIiIII1 ( ) :
 III1IiiI = iIi1 ( OO0o + 'books' + II11iiii1Ii )
 IIIII11I1IiI = re . compile ( '<NAME=>(.*?)</NAME><URL=>(.*?)</URL><CAT=>(.*?)</CAT>' ) . findall ( III1IiiI )
 for I1Ii , OOOooo , oOO0OOOOoooO in IIIII11I1IiI :
  if 'Parent' in I1Ii :
   pass
  elif '2' in oOO0OOOOoooO :
   oOo00oOOOOO ( ( I1Ii ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , OOOooo , 30010 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
   if 22 - 22: iI + iIii1I11I1II1
def IIIii1iiIi ( ) :
 i1111I1I = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oOOoo00O00o = i1111I1I . lower ( )
 III1IiiI = iIi1 ( OO0o + 'books' + II11iiii1Ii )
 IIIII11I1IiI = re . compile ( '<NAME=>(.*?)</NAME><URL=>(.*?)</URL><CAT=>(.*?)</CAT>' ) . findall ( III1IiiI )
 for I1Ii , OOOooo , oOO0OOOOoooO in IIIII11I1IiI :
  if i1111I1I in I1Ii . lower ( ) :
   if '1' in oOO0OOOOoooO :
    oOo00oOOOOO ( ( I1Ii ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , OOOooo , 30010 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
   elif '2' in oOO0OOOOoooO :
    oOo00oOOOOO ( ( I1Ii ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , OOOooo , 30010 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
   elif '3' in oOO0OOOOoooO :
    oOo00oOOOOO ( ( I1Ii ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , OOOooo , 30009 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
    if 63 - 63: ii11ii1ii
    if 6 - 6: II11i1iIiII1 / ii11ii1ii
def oOooO00o0O ( ) :
 III1IiiI = iIi1 ( OO0o + 'books' + II11iiii1Ii )
 IIIII11I1IiI = re . compile ( '<NAME=>(.*?)</NAME><URL=>(.*?)</URL><CAT=>(.*?)</CAT>' ) . findall ( III1IiiI )
 for I1Ii , OOOooo , oOO0OOOOoooO in IIIII11I1IiI :
  if '1' in oOO0OOOOoooO :
   oOo00oOOOOO ( ( I1Ii ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , OOOooo , 3010 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
  elif '2' in oOO0OOOOoooO :
   oOo00oOOOOO ( ( I1Ii ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , OOOooo , 30010 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
  elif '3' in oOO0OOOOoooO :
   oOo00oOOOOO ( ( I1Ii ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , OOOooo , 30009 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
   if 80 - 80: Oo000 / iI / I1IiI + i1IIi - Oo
 xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 11 - 11: OOooOOo * Ooo00oOo00o
def iIi1IiI ( url ) :
 ooI1111i = url
 III1IiiI = iIi1 ( url )
 IIOOO0O00O0OOOO = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( III1IiiI )
 for url , I1Ii in IIOOO0O00O0OOOO :
  if 'mp3' in I1Ii :
   O00Oo000ooO0 ( ( I1Ii ) . replace ( '%20' , ' ' ) , ooI1111i + url , 10012 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
  if 'wma' in I1Ii :
   O00Oo000ooO0 ( ( I1Ii ) . replace ( '%20' , ' ' ) , ooI1111i + url , 10012 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
  if 'm4b' in I1Ii :
   O00Oo000ooO0 ( ( I1Ii ) . replace ( '%20' , ' ' ) , ooI1111i + url , 10012 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
  elif '/' in I1Ii :
   oOo00oOOOOO ( ( I1Ii ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , ooI1111i + url , 30009 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
   if 14 - 14: Ooo0OO0 % OOO0OOO00oo % Oo - i11iIiiIii
   if 53 - 53: i1I111ii1II1i % Oo
   if 59 - 59: Oo000 % iIii1I11I1II1 . i1IIi + OoOoOO00 * Ooo0OO0
def i1IiiI1iIi ( url ) :
 III1IiiI = iIi1 ( url )
 ooI1111i = url
 IIIII11I1IiI = re . compile ( '<li><a href="(.+?)">(.+?)</a></li>' ) . findall ( III1IiiI )
 for url , I1Ii in IIIII11I1IiI :
  if 'Parent' in I1Ii :
   pass
  elif '.db' in I1Ii :
   pass
  elif '.jpg' in I1Ii :
   pass
  elif '.html' in I1Ii :
   pass
  elif '.doc' in I1Ii :
   pass
  elif 'mp3' in I1Ii :
   O00Oo000ooO0 ( ( I1Ii ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , ooI1111i + url , 10012 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
  elif 'm4a' in I1Ii :
   O00Oo000ooO0 ( ( I1Ii ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , ooI1111i + url , 10012 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
  else :
   oOo00oOOOOO ( ( I1Ii ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , ooI1111i + url , 30010 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
   if 66 - 66: Ooo00oOo00o * Oo
   if 28 - 28: Ooo00oOo00o % I1IiI % ii11ii1ii + OOOo0 / OOOo0
def OO0O0ooOOO00 ( ) :
 oOo00oOOOOO ( 'A-Z' , '' , 7 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
 oOo00oOOOOO ( 'All' , '' , 3 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
 oOo00oOOOOO ( 'Search' , '' , 14 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
 if 17 - 17: O0 . OoO0O0 . O0 + O0 / Oo . II11i1iIiII1
def OO00OOoO0o ( ) :
 III1IiiI = iIi1 ( i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9tcDNfZG93bmxvYWRzLmh0bQ==' ) )
 IIIII11I1IiI = re . compile ( '<td width=".+?" align="center">.+?<a href="(.*?)">.+?<img border="0" src="images/Squeeze%20(.*?).gif" width="74" height=".*?"></a></td>' , re . DOTALL ) . findall ( III1IiiI )
 for OOOooo , OO0O000 in IIIII11I1IiI :
  print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<' + OOOooo + '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
  if '-x' in OO0O000 :
   pass
  else :
   oOo00oOOOOO ( OO0O000 , ( i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) ) + ( OOOooo ) . replace ( 'colour_it' , 'books_audio/audio_books_a' ) , 30008 , ( i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9pbWFnZXMvU3F1ZWV6ZSUyMA==' ) ) + OO0O000 + '.gif' , ii11iIi1I + 'kodible.png' , '' )
   if 4 - 4: i1IIi - i11iIiiIii / i11iIiiIii / OoooooooOO
 xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 100 - 100: Oo + OOooOOo - O0 % OoOoOO00 . OoOo00o
 if 92 - 92: OoOoOO00 * OoooooooOO - OoO0O0
def oooo00 ( url ) :
 III1IiiI = iIi1 ( url )
 IIIII11I1IiI = re . compile ( '<td width=".*?" height=".*?"><b>.*?<a href="(.*?)">(.*?)</a></b></td>' , re . DOTALL ) . findall ( III1IiiI )
 for url , I1Ii in IIIII11I1IiI :
  if '</a>' in I1Ii :
   pass
  elif '(' in I1Ii :
   oOo00oOOOOO ( ( I1Ii ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '.mp3' , '' ) , i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) + url , 30005 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
  else :
   O00Oo000ooO0 ( ( I1Ii ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '.mp3' , '' ) , i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) + url , 30004 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
   if 96 - 96: ii11ii1ii % II11i1iIiII1 % i1I111ii1II1i - II11i1iIiII1 % I1IiI + ii11ii1ii
 xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 3 - 3: O0
def Ooo0Oo0oo0 ( ) :
 i1111I1I = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oOOoo00O00o = i1111I1I . lower ( )
 III1IiiI = iIi1 ( i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9jb21wbGV0ZV9saXN0Lmh0bQ==' ) )
 IIIII11I1IiI = re . compile ( '<td width=".+?">.*?<b>.+?<a href="(.*?)">(.*?)</a></b></td>' , re . DOTALL ) . findall ( III1IiiI )
 for OOOooo , I1Ii in IIIII11I1IiI :
  if i1111I1I in I1Ii . lower ( ) :
   if '</a>' in I1Ii :
    pass
   elif '(' in I1Ii :
    oOo00oOOOOO ( ( I1Ii ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + OOOooo , 30005 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
   else :
    O00Oo000ooO0 ( ( I1Ii ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + OOOooo , 30004 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
    if 83 - 83: OoO0O0
    if 48 - 48: OoOoOO00 * Oo000 * OoO0O0
def i1iiiIii11 ( ) :
 III1IiiI = iIi1 ( i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9jb21wbGV0ZV9saXN0Lmh0bQ==' ) )
 IIIII11I1IiI = re . compile ( '<td width=".+?">.*?<b>.+?<a href="(.*?)">(.*?)</a></b></td>' , re . DOTALL ) . findall ( III1IiiI )
 for OOOooo , I1Ii in IIIII11I1IiI :
  if '</a>' in I1Ii :
   pass
  elif '(' in I1Ii :
   oOo00oOOOOO ( ( I1Ii ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + OOOooo , 30005 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
  else :
   O00Oo000ooO0 ( ( I1Ii ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + OOOooo , 30004 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
   if 67 - 67: OOooOOo % I1IiI . I1IiI - II11i1iIiII1
 xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 90 - 90: II11i1iIiII1 + OoOoOO00 * ii11ii1ii / i1I111ii1II1i . OOooOOo + OOooOOo
 if 40 - 40: II11i1iIiII1 / I1IiI % i11iIiiIii % ii11ii1ii / OOOo0
def ooOOOOo0 ( url ) :
 III1IiiI = iIi1 ( url )
 IIIII11I1IiI = re . compile ( '<a href="(.+?)">Download</a></b></td>' ) . findall ( III1IiiI )
 for url in IIIII11I1IiI :
  ooI1111i = ( i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) ) + url
  Resolve ( ooI1111i )
  if 38 - 38: OoooooooOO / ii11ii1ii . O0 / i1IIi / Oo + iIii1I11I1II1
def ooO00O00oOO ( url ) :
 III1IiiI = iIi1 ( url )
 IIIII11I1IiI = re . compile ( '<td width="247">(.*?)</td>.*?<a href="(.+?)">' , re . DOTALL ) . findall ( III1IiiI )
 for I1Ii , url in IIIII11I1IiI :
  if '<p align' in I1Ii :
   pass
  elif '&nbsp;' in I1Ii :
   pass
  else :
   O00Oo000ooO0 ( ( I1Ii ) . replace ( '&nbsp;' , '' ) , i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) + url , 10012 , ii11iIi1I + 'kodible.png' , ii11iIi1I + 'kodible.png' , '' )
   if 40 - 40: OoOo00o . OOO0OOO00oo + OOOo0 + ii11ii1ii + OoO0O0
 xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 26 - 26: iIii1I11I1II1
 if 87 - 87: ii11ii1ii / OoooooooOO - Oo % I1IiI % Ooo0OO0 % Oo
def Ii1 ( ) :
 III1IiiI = cloudflare . source ( i1111 ( 'aHR0cDovL3dhdGNoY2FydG9vbnNvbmxpbmUuZXUv' ) )
 IIIII11I1IiI = re . compile ( 'class="menu-item menu-item-type-.+?><a href="([^"]*)">(.+?)</a></li>' , re . DOTALL ) . findall ( III1IiiI )
 for OOOooo , I1Ii in IIIII11I1IiI :
  if 'ongoing' in OOOooo :
   O00Oo000ooO0 ( '[COLORgreen]' + I1Ii + '[/COLOR]' , OOOooo , 21005 , ii11iIi1I + 'on-going.png' , '' , '' )
  if 'cartoon-series' in OOOooo :
   O00Oo000ooO0 ( '[COLORgreen]' + I1Ii + '[/COLOR]' , OOOooo , 21005 , ii11iIi1I + 'cartoonseries.png' , '' , '' )
  if 'disney' in OOOooo :
   O00Oo000ooO0 ( '[COLORgreen]' + I1Ii + '[/COLOR]' , OOOooo , 21005 , ii11iIi1I + 'disneytoons.png' , '' , '' )
  if 'genre' in OOOooo :
   O00Oo000ooO0 ( '[COLORgreen]' + I1Ii + '[/COLOR]' , OOOooo , 21005 , ii11iIi1I + 'cartoongenre.png' , '' , '' )
  if 'years' in OOOooo :
   O00Oo000ooO0 ( '[COLORgreen]' + I1Ii + '[/COLOR]' , OOOooo , 21005 , ii11iIi1I + 'years.png' , '' , '' )
def I1iiiiii ( url ) :
 III1IiiI = cloudflare . source ( url )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)" title="([^"]*)" rel="nofollow" id="featured-thumbnail">.+?<div class="featured-thumbnail"><img width="140" height="200" src="([^"]*)"' , re . DOTALL ) . findall ( III1IiiI )
 o0OO0Oo = re . compile ( '<button type="button"><a href="([^"]*)" target="_blank">(.+?)</a>' ) . findall ( III1IiiI )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' ) . findall ( III1IiiI )
 for url , I1Ii , OO0O000 in IIIII11I1IiI :
  O00Oo000ooO0 ( '[COLORgreen]' + I1Ii + '[/COLOR]' , url , 21006 , OO0O000 , OO0O000 , I1Ii )
 for url , I1Ii in o0OO0Oo :
  O00Oo000ooO0 ( '[COLORgreen]' + I1Ii + '[/COLOR]' , url , 21005 , ii11iIi1I + 'watchcartoons.png' , '' , '' )
 for url in next :
  O00Oo000ooO0 ( '[COLORgreen]NEXT[/COLOR]' , url , 21005 , ii11iIi1I + 'Next.png' , '' , '' )
def I11iiii1I ( url ) :
 III1IiiI = cloudflare . source ( url )
 IIIII11I1IiI = re . compile ( '<li><a href="([^"]*)" >(.+?)</a></li>' , re . DOTALL ) . findall ( III1IiiI )
 iiiiI1iiiIi = re . compile ( 'file:"([^"]*)",type:"mp4",label:"([^"]*)"' , re . DOTALL ) . findall ( III1IiiI )
 o0oO0OoO0 = re . compile ( 'src="([^"]*)" frameborder=' ) . findall ( III1IiiI )
 oOOOOOoOO = re . compile ( '<iframe src="([^"]*)"' ) . findall ( III1IiiI )
 for url , I1Ii in IIIII11I1IiI :
  O00Oo000ooO0 ( '[COLORgreen]' + I1Ii + '[/COLOR]' , url , 21007 , ii11iIi1I + 'watchcartoons.png' , '' , '' )
 for url in o0oO0OoO0 :
  O00Oo000ooO0 ( '[COLORgreen]PLAY[/COLOR]' , 'http:' + url , 222 , ii11iIi1I + 'watchcartoons.png' , '' , '' )
 for url , I1Ii in iiiiI1iiiIi :
  ii1ii11IIIiiI ( '[COLORgreen]' + I1Ii + '[/COLOR]' , url , 222 , ii11iIi1I + 'watchcartoons.png' , '' , '' )
 else :
  O00Oo000ooO0 ( '[COLORgreen]NO STREAMS AVAILABLE[/COLOR]' , url , 21005 , ii11iIi1I + 'watchcartoons.png' , '' , '' )
def oooo00i1 ( url ) :
 III1IiiI = cloudflare . source ( url )
 IIIII11I1IiI = re . compile ( 'file:"([^"]*)",type:"mp4",label:"([^"]*)"' , re . DOTALL ) . findall ( III1IiiI )
 for url , I1Ii in IIIII11I1IiI :
  ii1ii11IIIiiI ( '[COLORgreen]' + I1Ii + '[/COLOR]' , url , 222 , ii11iIi1I + 'watchcartoons.png' , '' , '' )
  if 95 - 95: Ooo00oOo00o . i1IIi / i11iIiiIii
def iIi1IIiI ( ) :
 iII11I1Ii1 ( '[COLORgreen]CARTOONS[/COLOR]' , '' , 20001 , ii11iIi1I + 'ORIGINCARTOON.png' )
 iII11I1Ii1 ( '[COLORgreen]ANIME[/COLOR]' , 'https://kissanime.to/AnimeList' , 20001 , ii11iIi1I + 'ORIGINCARTOON.png' )
 if 24 - 24: OoOo00o * OoOoOO00 % OoOo00o % Ooo0OO0 + OoooooooOO
def IiIiiiIii ( ) :
 iII11I1Ii1 ( '[COLORgreen]BY NAME[/COLOR]' , 'http://kisscartoon.me/CartoonList' , 20002 , ii11iIi1I + 'ORIGINCARTOON.png' )
 iII11I1Ii1 ( '[COLORgreen]BY GENRE[/COLOR]' , 'http://kisscartoon.me/CartoonList' , 20003 , ii11iIi1I + 'ORIGINCARTOON.png' )
 if 27 - 27: i1IIi % I1IiI . OOOo0 + II11i1iIiII1 % I1IiI
def o0o0oOo000o0 ( url ) :
 III1IiiI = cloudflare . source ( url )
 IIIII11I1IiI = re . compile ( 'href="(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( III1IiiI )
 for url , I1Ii in IIIII11I1IiI :
  if '?c=' in url :
   iII11I1Ii1 ( '[COLORgreen]' + I1Ii + '[/COLOR]' , 'http://kisscartoon.me' + url , 20004 , ii11iIi1I + 'ORIGINCARTOON.png' )
   if 25 - 25: iI + I1IiI . OOooOOo % I1IiI * Oo000
def ii1IiIi11 ( url ) :
 III1IiiI = cloudflare . source ( url )
 IIIII11I1IiI = re . compile ( 'href="(.+?)" title="(.+?)">/n(.+?)</a><br/>' , re . DOTALL ) . findall ( III1IiiI )
 for url , iiiii1ii1 , I1Ii in IIIII11I1IiI :
  if 'Genre' in url :
   iII11I1Ii1 ( '[COLORgreen]' + I1Ii + '[/COLOR]' , 'http://kisscartoon.me' + url , 20004 , ii11iIi1I + 'ORIGINCARTOON.png' )
   if 48 - 48: O0 + O0 . OoO0O0 - II11i1iIiII1
def o00oo0000 ( url ) :
 III1IiiI = cloudflare . source ( url )
 IIIII11I1IiI = re . compile ( 'src="(.+?)" style=.+?<a class="bigChar" href="(.+?)">(.+?)</a>.+?<p>(.+?)</p>' , re . DOTALL ) . findall ( III1IiiI )
 for url , iiiii1ii1 , I1Ii in IIIII11I1IiI :
  O00Oo000ooO0 ( '[COLORgreen]' + I1Ii + '[/COLOR]' , 'http://kisscartoon.me' + url , 20005 , img , '' , iiiii1ii1 )
  if 44 - 44: Oo % iIii1I11I1II1
def oo0ooO0 ( url ) :
 III1IiiI = cloudflare . source ( url )
 IIIII11I1IiI = re . compile ( '<img width="120" height="165" src="(.+?)" style=.+?<a class="bigChar" href="(.+?)">(.+?)</a>.+?<p>(.+?)</p>' , re . DOTALL ) . findall ( III1IiiI )
 for url , iiiii1ii1 , I1Ii in IIIII11I1IiI :
  O00Oo000ooO0 ( '[COLORgreen]' + I1Ii + '[/COLOR]' , 'http://kisscartoon.me' + url , 20005 , img , '' , iiiii1ii1 )
  if 28 - 28: ii11ii1ii * OoooooooOO . OoOoOO00 / i11iIiiIii + OOO0OOO00oo
  if 38 - 38: Ooo0OO0 . i1I111ii1II1i
  if 24 - 24: OOooOOo - OOooOOo + ii11ii1ii + OOOo0 - OOO0OOO00oo
  if 12 - 12: OoOo00o . Ooo0OO0 . I1IiI / O0
  if 58 - 58: OOooOOo - OoOoOO00 % OOO0OOO00oo + OoO0O0 . I1IiI / Ooo0OO0
def IIo00ooo ( ) :
 if 31 - 31: O0 * OOooOOo % OOooOOo / OOO0OOO00oo / iI / Ooo00oOo00o
 O00Oo000ooO0 ( '[COLORgreen]Cartoons[/COLOR]' , i1111 ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2NhcnRvb24=' ) , 10004 , ii11iIi1I + 'ORIGINCARTOON.png' , i1iiIII111ii , '' )
 O00Oo000ooO0 ( '[COLORgreen]Search Cartoons[/COLOR]' , '' , 10005 , ii11iIi1I + 'ORIGINCARTOON.png' , i1iiIII111ii , '' )
 if 11 - 11: I1IiI + Ooo0OO0 - OoooooooOO / Ooo00oOo00o
def iIIi1iI1I1IIi ( ) :
 i1111I1I = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oOOoo00O00o = i1111I1I . lower ( )
 III1IiiI = iIi1 ( i1111 ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2NhcnRvb24=' ) )
 IIIII11I1IiI = re . compile ( '<td><a href="(.+?)">(.+)</a></td>' ) . findall ( III1IiiI )
 for OOOooo , I1Ii in IIIII11I1IiI :
  if i1111I1I in I1Ii . lower ( ) :
   if 'Dad!' in I1Ii :
    pass
   elif 'Family Guy' in I1Ii :
    pass
   elif '2 Stupid' in I1Ii :
    pass
   elif 'The Zelfs' in I1Ii :
    pass
   elif 'A Clone' in I1Ii :
    pass
   elif 'A.T.O.M' in I1Ii :
    pass
   elif 'Almost Naked' in I1Ii :
    pass
   elif 'Angry Kid' in I1Ii :
    pass
   elif 'Annoying Orange' in I1Ii :
    pass
   elif 'Aqua Teen' in I1Ii :
    pass
   elif 'Assy Mcgee' in I1Ii :
    pass
   elif 'Astroblast' in I1Ii :
    pass
   elif 'Atomic Betty' in I1Ii :
    pass
   elif 'Axe Cop' in I1Ii :
    pass
   elif 'Baby Playpen' in I1Ii :
    pass
   elif 'Beavis and Butt' in I1Ii :
    pass
   elif 'Celebrity Deathmatch' in I1Ii :
    pass
   elif 'Clerks The' in I1Ii :
    pass
   elif 'Crapston Villas' in I1Ii :
    pass
   elif 'Duckman:' in I1Ii :
    pass
   elif 'Stripperella' in I1Ii :
    pass
   elif 'Vixen' in I1Ii :
    pass
   else :
    O00Oo000ooO0 ( '[COLORgreen]' + I1Ii + '[/COLOR]' , OOOooo , 10006 , ii11iIi1I + 'ORIGINCARTOON.png' , i1iiIII111ii , '' )
  xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 77 - 77: II11i1iIiII1 / Oo + II11i1iIiII1 % OOooOOo - OOOo0 * OOOo0
def I1 ( url ) :
 i1I1i1 = iIi1 ( url )
 IIIII11I1IiI = re . compile ( '<td><a href="(.+?)">(.+)</a></td>' ) . findall ( i1I1i1 )
 for url , I1Ii in IIIII11I1IiI :
  if 'Dad!' in I1Ii :
   pass
  elif 'Family Guy' in I1Ii :
   pass
  elif '2 Stupid' in I1Ii :
   pass
  elif 'The Zelfs' in I1Ii :
   pass
  elif 'A Clone' in I1Ii :
   pass
  elif 'A.T.O.M' in I1Ii :
   pass
  elif 'Almost Naked' in I1Ii :
   pass
  elif 'Angry Kid' in I1Ii :
   pass
  elif 'Annoying Orange' in I1Ii :
   pass
  elif 'Aqua Teen' in I1Ii :
   pass
  elif 'Assy Mcgee' in I1Ii :
   pass
  elif 'Astroblast' in I1Ii :
   pass
  elif 'Atomic Betty' in I1Ii :
   pass
  elif 'Axe Cop' in I1Ii :
   pass
  elif 'Baby Playpen' in I1Ii :
   pass
  elif 'Beavis and Butt' in I1Ii :
   pass
  elif 'Celebrity Deathmatch' in I1Ii :
   pass
  elif 'Clerks The' in I1Ii :
   pass
  elif 'Crapston Villas' in I1Ii :
   pass
  elif 'Duckman:' in I1Ii :
   pass
  elif 'Stripperella' in I1Ii :
   pass
  elif 'Vixen' in I1Ii :
   pass
  else :
   O00Oo000ooO0 ( '[COLORgreen]' + I1Ii + '[/COLOR]' , url , 10006 , ii11iIi1I + 'ORIGINCARTOON.png' , i1iiIII111ii , '' )
 xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 69 - 69: ii11ii1ii - OoO0O0
def iiIIi1 ( url ) :
 i1I1i1 = iIi1 ( url )
 IIOOO0O00O0OOOO = re . compile ( '<img src="(.+?)" id="series_image" width="250" height="370" alt=".+?" />' ) . findall ( i1I1i1 )
 for OO0O000 in IIOOO0O00O0OOOO :
  i111i11I1Ii1I = OO0O000
 iI1I11iIIi1 = re . compile ( '<li><a href="(.+?)">Next</a></li>' ) . findall ( i1I1i1 )
 for url in iI1I11iIIi1 :
  O00Oo000ooO0 ( '[COLORgreen]NEXT PAGE[/COLOR]' , url , 10006 , ii11iIi1I + 'Next.png' , i1iiIII111ii , '' )
 IIIII11I1IiI = re . compile ( '&nbsp;<a href="(.+?)">(.+?)</a>' ) . findall ( i1I1i1 )
 for url , I1Ii in IIIII11I1IiI :
  I11I1IIiiII1 ( '[COLORgreen]' + I1Ii + '[/COLOR]' , url , 10007 , i111i11I1Ii1I )
  if 39 - 39: OOooOOo . iIii1I11I1II1
  if 51 - 51: iI . Oo
 xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 45 - 45: i1IIi - Oo / O0 . ii11ii1ii
def iI1 ( url , IMAGE ) :
 i1I1i1 = iIi1 ( url )
 IIIII11I1IiI = re . compile ( '"playlist">(.+?)</span></div><div><iframe src="(.+?)"' ) . findall ( i1I1i1 )
 for I1Ii , url in IIIII11I1IiI :
  print I1Ii + '     ' + url
  if 'easy' in url :
   iIIiI1ii ( url )
   if 78 - 78: O0 * Oo000
   if 43 - 43: ii11ii1ii / OOOo0 . II11i1iIiII1
  xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 62 - 62: iIii1I11I1II1 + OoOo00o . Oo / Ooo0OO0 % O0 . OoO0O0
def iIIiI1ii ( url ) :
 i1I1i1 = iIi1 ( url )
 IIIII11I1IiI = re . compile ( "url: '(.+?)'," ) . findall ( i1I1i1 )
 for url in IIIII11I1IiI :
  Oo0oOooOoOo ( url )
  if 49 - 49: Oo000 . ii11ii1ii . i11iIiiIii - OoOoOO00 / i1I111ii1II1i
  if 62 - 62: Oo000
  if 1 - 1: Ooo0OO0 / Ooo0OO0 - i11iIiiIii
def OO0oIiII1iiI ( ) :
 if 34 - 34: OOOo0 . OOO0OOO00oo + i1IIi
 O00Oo000ooO0 ( '[COLORgreen]Stand Up[/COLOR]' , '' , 10014 , ii11iIi1I + 'ORIGINSTANDUP.png' , i1iiIII111ii , '' )
 O00Oo000ooO0 ( '[COLORgreen]Search Comedian[/COLOR]' , '' , 10015 , ii11iIi1I + 'ORIGINSTANDUP.png' , i1iiIII111ii , '' )
 O00Oo000ooO0 ( '[COLORgreen]Others[/COLOR]' , '' , 10017 , ii11iIi1I + 'ORIGINSTANDUP.png' , i1iiIII111ii , '' )
 if 98 - 98: OOO0OOO00oo % Ooo0OO0 * i11iIiiIii % ii11ii1ii
def iIiI1IIiii11 ( ) :
 III1IiiI = iIi1 ( ( i1111 ( 'aHR0cDovL2JhY2syYmFzaWNzYnVpbGQuY28udWsvdGVzdC9zdGFuZHVwbGlzdC5waHA=' ) ) )
 IIIII11I1IiI = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( III1IiiI )
 for OOOooo , OO0O000 , I1Ii in IIIII11I1IiI :
  if 'elete' in I1Ii :
   pass
  else :
   I11I1IIiiII1 ( '[COLORgreen]' + I1Ii + '[/COLOR]' , OOOooo , 222 , OO0O000 )
   if 33 - 33: iIii1I11I1II1 / OoOo00o - OOOo0 * iI
def o0o00oO0oo000 ( ) :
 i1111I1I = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oOOoo00O00o = i1111I1I . lower ( )
 III1IiiI = iIi1 ( ( i1111 ( 'aHR0cDovL3d3dy5jb3VjaHRyaXBwZXIuY29tL2ZvcnVtMi9wYWdlLnBocD9wYWdlPTM=' ) ) )
 oO000o = re . compile ( '<tr>.+?<td width=".+?" align=".+?">.+?<img border=".+?" src="..(.+?)" width=".+?" height=".+?"></td>.+?<td width=".+?" valign=".+?" align=".+?"><font size=".+?">(.+?)</font></td>.+?<td width=".+?">(.+?)</td>' , re . DOTALL ) . findall ( III1IiiI )
 for OO0O000 , o0Oo , iIiiiI1IiI1I1 in oO000o :
  for i1111I1I in o0Oo :
   print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< img >>>>>>>>>>>>>>>>>>>>>>>>>>'
   o0O0 = re . compile ( '<a href="(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( iIiiiI1IiI1I1 )
   for OOOooo , I1Ii in o0O0 :
    if 'tube' in OOOooo :
     pass
    elif 'stage' in OOOooo :
     I11I1IIiiII1 ( '[COLORgreen]' + o0Oo + '   -   ' + I1Ii + '[/COLOR]' , ( OOOooo ) . replace ( '" target="_blank' , '' ) , 10016 , 'http://couchtripper.com/' + OO0O000 , )
    elif 'vee' in OOOooo :
     pass
     if 48 - 48: iI - Ooo0OO0 + iIii1I11I1II1 + OoooooooOO
def Ii ( ) :
 III1IiiI = iIi1 ( ( i1111 ( 'aHR0cDovL3d3dy5jb3VjaHRyaXBwZXIuY29tL2ZvcnVtMi9wYWdlLnBocD9wYWdlPTM=' ) ) )
 oO000o = re . compile ( '<tr>.+?<td width=".+?" align=".+?">.+?<img border=".+?" src="..(.+?)" width=".+?" height=".+?"></td>.+?<td width=".+?" valign=".+?" align=".+?"><font size=".+?">(.+?)</font></td>.+?<td width=".+?">(.+?)</td>' , re . DOTALL ) . findall ( III1IiiI )
 for OO0O000 , o0Oo , iIiiiI1IiI1I1 in oO000o :
  o0O0 = re . compile ( '<a href="(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( iIiiiI1IiI1I1 )
  for OOOooo , I1Ii in o0O0 :
   if 'tube' in OOOooo :
    pass
   elif 'stage' in OOOooo :
    I11I1IIiiII1 ( '[COLORgreen]' + o0Oo + '   -   ' + I1Ii + '[/COLOR]' , ( OOOooo ) . replace ( '" target="_blank' , '' ) , 10016 , 'http://couchtripper.com/' + OO0O000 )
   elif 'vee' in OOOooo :
    pass
    if 42 - 42: i1I111ii1II1i * OoO0O0 . Ooo0OO0 * OOOo0 + I1IiI
    if 25 - 25: iI . OOOo0 + OOO0OOO00oo
 xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 75 - 75: Ooo0OO0 - OOooOOo % OoOo00o + i11iIiiIii
def O0OOOo ( url ) :
 III1IiiI = iIi1 ( url )
 print '>>>>>>>>>>>>>>>>>>>>>>>>' + url + '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'
 I1iiii1I = re . compile ( "url\[.+?\] = '(.+?)';" ) . findall ( III1IiiI )
 print '>>>>>>>>>>>>>>>>>>>>>>>' + ( str ( I1iiii1I ) ) + '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
 for url in I1iiii1I :
  Oo0oOooOoOo ( ( url ) . replace ( '[' , '' ) . replace ( ']' , '' ) . replace ( '\'' , '' ) )
  if 30 - 30: OoOo00o / Ooo00oOo00o + OOO0OOO00oo
  if 6 - 6: OoOo00o . iI + i1I111ii1II1i . OoO0O0
  if 70 - 70: Ooo00oOo00o
  if 46 - 46: iI - i1IIi
  if 46 - 46: OoO0O0 % i1I111ii1II1i
  if 72 - 72: iIii1I11I1II1
  if 45 - 45: Oo - OOooOOo % OoO0O0
def i1IIi1i1Ii1 ( ) :
 if 45 - 45: iIii1I11I1II1 . OOO0OOO00oo / I1IiI / Ooo0OO0
 ooOOOoOoOOO0 ( '[COLOR darkgoldenrod]Open Pandora\'s Box[/COLOR]' , '' , 10029 , 'https://encrypted-tbn1.gstatic.com/images?q=tbn%3AANd9GcTQ9r4TA8yIw9ggxuwsHxWojo6tPVfgTe8QIOxOQwzNR2TavtCi6Q' , i1iiIII111ii , '' )
 ooOOOoOoOOO0 ( '[COLOR darkgoldenrod]Search[/COLOR]' , '' , 10026 , 'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png' , i1iiIII111ii , '' )
 if 5 - 5: Oo000
 ii111 ( 'movies' , 'MAIN' )
 if 4 - 4: OoOo00o % OoO0O0 / Ooo00oOo00o . Oo000 / Oo000 - ii11ii1ii
def oO0ooOO ( ) :
 ooOOOoOoOOO0 ( 'Search Pandoras Films' , '' , 10027 , 'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png' , i1iiIII111ii , '' )
 ooOOOoOoOOO0 ( 'Search Pandoras TV' , '' , 10028 , 'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png' , i1iiIII111ii , '' )
 if 7 - 7: OoOoOO00 - Oo000 . OoOoOO00
 ii111 ( 'movies' , 'MAIN' )
def OOo0O0O000 ( ) :
 if 29 - 29: OOooOOo / Oo * ii11ii1ii . OOooOOo
 i1111I1I = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oOOoo00O00o = i1111I1I . lower ( )
 oO00 = [ 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' ]
 if 1 - 1: OOO0OOO00oo
 for I1IIIIiii1i in oO00 :
  o0IiiiI111I = ooooooO0oo + I1IIIIiii1i + II11iiii1Ii
  III1IiiI = iIi1 ( o0IiiiI111I )
  IIIII11I1IiI = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( III1IiiI )
  for OOOooo , ooo0O0o00O , oo0o , I1i11 , I1Ii in IIIII11I1IiI :
   if i1111I1I in I1Ii . lower ( ) :
    III1I11i1iIi ( I1Ii , OOOooo , 222 , ooo0O0o00O , I1i11 , oo0o )
    if 69 - 69: Oo * OoOoOO00 * II11i1iIiII1 . OoOo00o - ii11ii1ii
    ii111 ( 'movies' , 'MAIN' )
    xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
    if 39 - 39: i1I111ii1II1i * OOOo0 % Ooo00oOo00o . I1IiI
    if 24 - 24: i1IIi * iIii1I11I1II1 / i1I111ii1II1i
def OoOOo00 ( ) :
 if 53 - 53: Ooo0OO0 . OoO0O0 % iIii1I11I1II1 % I1IiI % iI
 i1111I1I = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oOOoo00O00o = i1111I1I . lower ( )
 oO00 = [ 'a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' , 'p' , 'q' , 'r' , 's' , 't' , 'u' , 'v' , 'w' , 'x' , 'y' , 'z' ]
 if 53 - 53: OoO0O0
 for I1IIIIiii1i in oO00 :
  OOoOOo0o = ooooooO0oo + I1IIIIiii1i + II11iiii1Ii
  III1IiiI = iIi1 ( OOoOOo0o )
  IIIII11I1IiI = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( III1IiiI )
  for I1Ii , oo0o , OOOooo , OO0O000 , I1i11 , iIiii in IIIII11I1IiI :
   if i1111I1I in I1Ii . lower ( ) :
    ooOOOoOoOOO0 ( I1Ii , OOOooo , iIiii , OO0O000 , I1i11 , oo0o )
    if 2 - 2: i1IIi - OOOo0 + iI . OoOoOO00
    ii111 ( 'movies' , 'MAIN' )
    xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
    if 25 - 25: OOO0OOO00oo
    if 34 - 34: I1IiI . iIii1I11I1II1 % O0
def iI11Ii111 ( ) :
 if 54 - 54: I1IiI % OoOo00o . I1IiI * Oo000 + I1IiI % i1IIi
 i1I1i1 = iIi1 ( ooooooO0oo + 'spongemain.php' )
 IIIII11I1IiI = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( i1I1i1 )
 for I1Ii , oo0o , OOOooo , OO0O000 , I1i11 , iIiii in IIIII11I1IiI :
  ooOOOoOoOOO0 ( I1Ii , OOOooo , iIiii , OO0O000 , I1i11 , oo0o )
  ii111 ( 'movies' , 'MAIN' )
def I1I1I11Ii ( url ) :
 if 48 - 48: OoooooooOO + OOO0OOO00oo % iIii1I11I1II1
 xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
 IiI1IIIII1I = ( '%s%s' % ( I1I1IiIi1 , url ) )
 iI1I1i11iIIii = iIi1 ( url )
 IIIII11I1IiI = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( iI1I1i11iIIii )
 for url , ooo0O0o00O , oo0o , oOO0o0oo0 , I1Ii in IIIII11I1IiI :
  III1I11i1iIi ( I1Ii , url , 222 , ooo0O0o00O , oOO0o0oo0 , oo0o )
  if 78 - 78: Oo000 + OoOo00o . Ooo0OO0
  ii111 ( 'movies' , 'MAIN' )
  if 91 - 91: iIii1I11I1II1 . OOooOOo . ii11ii1ii + OoooooooOO
  xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 69 - 69: OoO0O0 - OOOo0
  if 95 - 95: OOOo0 * i11iIiiIii . II11i1iIiII1
def iIIi1 ( url ) :
 if 83 - 83: Ooo0OO0 * iI / Oo
 i1I1i1 = iIi1 ( url )
 IIIII11I1IiI = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( i1I1i1 )
 for I1Ii , oo0o , url , OO0O000 , I1i11 , iIiii in IIIII11I1IiI :
  ooOOOoOoOOO0 ( I1Ii , url , iIiii , OO0O000 , I1i11 , oo0o )
  if 32 - 32: OOooOOo + I1IiI - OoooooooOO
  ii111 ( 'movies' , 'MAIN' )
  if 39 - 39: OoooooooOO * Oo000 * O0 . iI . Ooo00oOo00o + II11i1iIiII1
  if 9 - 9: I1IiI + OOO0OOO00oo % OoooooooOO + OOooOOo
 xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 56 - 56: OoooooooOO + ii11ii1ii - OoOo00o
def III1I11i1iIi ( name , url , mode , iconimage , fanart , description ) :
 if 24 - 24: OOooOOo + II11i1iIiII1 + iI - iIii1I11I1II1
 I11Oo0oO00 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 IiiI1III1I1 = True
 o0OoOoo00O = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 o0OoOoo00O . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 o0OoOoo00O . setProperty ( "Fanart_Image" , fanart )
 IiiI1III1I1 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = I11Oo0oO00 , listitem = o0OoOoo00O , isFolder = False )
 return IiiI1III1I1
 if 29 - 29: OOooOOo
def ooOOOoOoOOO0 ( name , url , mode , iconimage , fanart , description ) :
 if 86 - 86: OoOoOO00 . Ooo0OO0
 I11Oo0oO00 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 IiiI1III1I1 = True
 o0OoOoo00O = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 o0OoOoo00O . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 o0OoOoo00O . setProperty ( "Fanart_Image" , fanart )
 IiiI1III1I1 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = I11Oo0oO00 , listitem = o0OoOoo00O , isFolder = True )
 return IiiI1III1I1
if 2 - 2: OoooooooOO
if 60 - 60: Ooo00oOo00o
if 81 - 81: I1IiI % i1I111ii1II1i
if 87 - 87: iIii1I11I1II1 . OoooooooOO * I1IiI
if 100 - 100: Ooo00oOo00o / i1IIi - OOOo0 % i1I111ii1II1i - iIii1I11I1II1
if 17 - 17: iI / OOooOOo % Oo
if 71 - 71: Ooo0OO0 . OoO0O0 . Ooo00oOo00o
if 68 - 68: i11iIiiIii % OOO0OOO00oo * Ooo00oOo00o * Ooo0OO0 * OoOoOO00 + O0
if 66 - 66: iI % ii11ii1ii % OoooooooOO
if 34 - 34: OOooOOo / OoOo00o % O0 . Ooo00oOo00o . i1IIi
if 29 - 29: O0 . OoO0O0
if 66 - 66: OOO0OOO00oo * iIii1I11I1II1 % iIii1I11I1II1 * Ooo0OO0 - II11i1iIiII1 - Ooo0OO0
if 70 - 70: OoO0O0 + OOO0OOO00oo
if 93 - 93: OoO0O0 + i1I111ii1II1i
if 33 - 33: O0
def oo0oO ( string ) :
 if OOO00 == 'true' :
  xbmc . log ( "[addon.live.GenieTV-%s]: %s" % ( addon_version , string ) )
  if 50 - 50: OoooooooOO - iIii1I11I1II1 + i1IIi % OoO0O0 - iIii1I11I1II1 % O0
def o0oO0Oo ( name , url , iconimage , fanart , mode , playlist = None , regexs = None ) :
 OO0OO000 = [ ]
 try :
  if 55 - 55: II11i1iIiII1
  name = name . encode ( 'utf-8' , 'ignore' )
 except :
  pass
 if os . path . exists ( iIi1ii1I1 ) == False :
  oo0oO ( 'Making Favorites File' )
  OO0OO000 . append ( ( name , url , iconimage , fanart , mode , playlist , regexs ) )
  iIIiIiI1I1 = open ( iIi1ii1I1 , "w" )
  iIIiIiI1I1 . write ( json . dumps ( OO0OO000 ) )
  iIIiIiI1I1 . close ( )
 else :
  oo0oO ( 'Appending Favorites' )
  iIIiIiI1I1 = open ( iIi1ii1I1 ) . read ( )
  o0O0OO0o = json . loads ( iIIiIiI1I1 )
  o0O0OO0o . append ( ( name , url , iconimage , fanart , mode ) )
  iIII1I1i1i = open ( iIi1ii1I1 , "w" )
  iIII1I1i1i . write ( json . dumps ( o0O0OO0o ) )
  iIII1I1i1i . close ( )
  if 54 - 54: I1IiI . OOO0OOO00oo % i11iIiiIii / OoooooooOO + Ooo0OO0 % OOO0OOO00oo
  if 36 - 36: OOO0OOO00oo
def o0OO ( ) :
 II1I1 = json . loads ( open ( iIi1ii1I1 ) . read ( ) )
 iii11I11iI1 = len ( II1I1 )
 for iI1i1iiii in II1I1 :
  I1Ii = iI1i1iiii [ 0 ]
  OOOooo = iI1i1iiii [ 1 ]
  ooo0O0o00O = iI1i1iiii [ 2 ]
  try :
   oO0o = iI1i1iiii [ 3 ]
   if oO0o == None :
    raise
  except :
   if o0oO0 . getSetting ( 'use_thumb' ) == "true" :
    oO0o = ooo0O0o00O
   else :
    oO0o = I1i11
  try : I1I1 = iI1i1iiii [ 5 ]
  except : I1I1 = None
  try : O0Oo0 = iI1i1iiii [ 6 ]
  except : O0Oo0 = None
  if 80 - 80: OOOo0 - iIii1I11I1II1 . Oo000 + Ooo00oOo00o - OoO0O0
  if iI1i1iiii [ 4 ] == 0 :
   O00Oo000ooO0 ( I1Ii , OOOooo , '' , ooo0O0o00O , I1i11 , '' , 'fav' )
  else :
   O00Oo000ooO0 ( I1Ii , OOOooo , iI1i1iiii [ 4 ] , ooo0O0o00O , I1i11 , '' , 'fav' )
   if 5 - 5: OoOo00o
def OO ( name ) :
 o0O0OO0o = json . loads ( open ( iIi1ii1I1 ) . read ( ) )
 for iI1I1iIII1IiiI in range ( len ( o0O0OO0o ) ) :
  if o0O0OO0o [ iI1I1iIII1IiiI ] [ 0 ] == name :
   del o0O0OO0o [ iI1I1iIII1IiiI ]
   iIII1I1i1i = open ( iIi1ii1I1 , "w" )
   iIII1I1i1i . write ( json . dumps ( o0O0OO0o ) )
   iIII1I1i1i . close ( )
   break
 xbmc . executebuiltin ( "XBMC.Container.Refresh" )
 if 96 - 96: OOOo0 % i1IIi . OOooOOo . O0
 if 37 - 37: i1IIi - Oo000 % OoooooooOO / Oo000 % II11i1iIiII1
def Oooo0O ( ) :
 iiIiII11i1 = os . path . join ( iIii1 , 'addons.ini' )
 oOo00Ooo0o0 = open ( iiIiII11i1 , "w+" )
 if 33 - 33: iI
 oOo00Ooo0o0 . write ( r'# This file contains the "built-in" channels' + '\n' )
 oOo00Ooo0o0 . write ( r'# It is parsed by Pythons ConfigParser' + '\n\n' )
 oOo00Ooo0o0 . write ( r'[plugin.video.GenieTv]' + '\n' )
 oOo00Ooo0o0 . write ( r'BBC One=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F394.m3u8&mode=10012&name=[COLORgreen]BBC+One+UK%0D[/COLOR]' + '\n' )
 oOo00Ooo0o0 . write ( r'BBC Two=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F190.m3u8&mode=10012&name=[COLORgreen]BBC+Two+UK%0D[/COLOR]' + '\n' )
 oOo00Ooo0o0 . write ( r'BBC Four=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F188.m3u8&mode=10012&name=[COLORgreen]BBC+Four+UK%0D[/COLOR]' + '\n' )
 oOo00Ooo0o0 . write ( r'BBC Ent MX=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F435.m3u8&mode=10012&name=[COLORgreen]BBC+Entertainment+MX%0D[/COLOR]' + '\n' )
 oOo00Ooo0o0 . write ( r'ITV=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F208.m3u8&mode=10012&name=[COLORgreen]ITV1+UK%0D[/COLOR]' + '\n' )
 oOo00Ooo0o0 . write ( r'ITV2=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F207.m3u8&mode=10012&name=[COLORgreen]ITV2+UK%0D[/COLOR]' + '\n' )
 oOo00Ooo0o0 . write ( r'ITV3=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F206.m3u8&mode=10012&name=[COLORgreen]ITV3+UK%0D[/COLOR]' + '\n' )
 oOo00Ooo0o0 . write ( r'ITV4=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F205.m3u8&mode=10012&name=[COLORgreen]ITV4+UK%0D[/COLOR]' + '\n' )
 oOo00Ooo0o0 . write ( r'Channel 4=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F183.m3u8&mode=10012&name=[COLORgreen]Channel+4+UK%0D[/COLOR]' + '\n' )
 oOo00Ooo0o0 . write ( r'Channel 5=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F185.m3u8&mode=10012&name=[COLORgreen]Channel+5+UK%0D[/COLOR]' + '\n' )
 oOo00Ooo0o0 . write ( r'Sky1=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F32.m3u8&mode=10012&name=[COLORgreen]Sky+1+UK%0D[/COLOR]' + '\n' )
 oOo00Ooo0o0 . write ( r'Sky2=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F33.m3u8&mode=10012&name=[COLORgreen]Sky+2+UK%0D[/COLOR]' + '\n' )
 oOo00Ooo0o0 . write ( r'Sky Atlantic=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F34.m3u8&mode=10012&name=[COLORgreen]Sky+Atlantic+UK%0D[/COLOR]' + '\n' )
 oOo00Ooo0o0 . write ( r'Sky Living=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F35.m3u8&mode=10012&name=[COLORgreen]Sky+Living+UK%0D[/COLOR]' + '\n' )
 oOo00Ooo0o0 . write ( r'5STAR=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F187.m3u8&mode=10012&name=[COLORgreen]5%2A+UK%0D[/COLOR]' + '\n' )
 oOo00Ooo0o0 . write ( r'5 USA=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F186.m3u8&mode=10012&name=[COLORgreen]5USA+UK%0D[/COLOR]' + '\n' )
 oOo00Ooo0o0 . write ( r'Watch HD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F408.m3u8&mode=10012&name=[COLORgreen]Watch+UK%0D[/COLOR]' + '\n' )
 oOo00Ooo0o0 . write ( r'Pick=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F410.m3u8&mode=10012&name=[COLORgreen]Pick+UK%0D[/COLOR]' + '\n' )
 oOo00Ooo0o0 . write ( r'GOLD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F430.m3u8&mode=10012&name=[COLORgreen]Gold+UK%0D[/COLOR]' + '\n' )
 oOo00Ooo0o0 . write ( r'YESTERDAY=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F411.m3u8&mode=10012&name=[COLORgreen]Yesterday+UK%0D[/COLOR]' + '\n' )
 oOo00Ooo0o0 . write ( r'TG4=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F192.m3u8&mode=10012&name=[COLORgreen]TG4%0D[/COLOR]' + '\n' )
 oOo00Ooo0o0 . write ( r'RTE One=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F194.m3u8&mode=10012&name=[COLORgreen]RTE+One+UK%0D[/COLOR]' + '\n' )
 oOo00Ooo0o0 . write ( r'RTE Two=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F193.m3u8&mode=10012&name=[COLORgreen]RTE+Two+UK%0D[/COLOR]' + '\n' )
 oOo00Ooo0o0 . write ( r'Disney Chnl=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F398.m3u8&mode=10012&name=[COLORgreen]Disney+Channel+UK%0D[/COLOR]' + '\n' )
 oOo00Ooo0o0 . write ( r'Disney Junior=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F397.m3u8&mode=10012&name=[COLORgreen]Disney+Junior+UK%0D[/COLOR]' + '\n' )
 oOo00Ooo0o0 . write ( r'Discovery=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F395.m3u8&mode=10012&name=[COLORgreen]Discovery+UK%0D[/COLOR]' + '\n' )
 oOo00Ooo0o0 . write ( r'Discovery Science=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F396.m3u8&mode=10012&name=[COLORgreen]Discovery+Science+UK%0D[/COLOR]' + '\n' )
 oOo00Ooo0o0 . write ( r'Animal Planet=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F428.m3u8&mode=10012&name=[COLORgreen]Animal+Planet+UK%0D[/COLOR]' + '\n' )
 oOo00Ooo0o0 . write ( r'Disc.Turbo=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F431.m3u8&mode=10012&name=[COLORgreen]Discovery+Turbo+UK%0D[/COLOR]' + '\n' )
 oOo00Ooo0o0 . write ( r'Nat Geo=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F429.m3u8&mode=10012&name=[COLORgreen]National+Geographic+Channel+UK%0D[/COLOR]' + '\n' )
 oOo00Ooo0o0 . write ( r'MTV MUSIC=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F409.m3u8&mode=10012&name=[COLORgreen]MTV+Music+UK%0D[/COLOR]' + '\n' )
 oOo00Ooo0o0 . write ( r'MTV Canada=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F417.m3u8&mode=10012&name=[COLORgreen]MTV+2+Ca%0D[/COLOR]' + '\n' )
 oOo00Ooo0o0 . write ( r'SkyPremiereHD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F37.m3u8&mode=10012&name=[COLORgreen]Sky+Movies+Premiere+UK%0D[/COLOR]' + '\n' )
 oOo00Ooo0o0 . write ( r'Sky Action=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F39.m3u8&mode=10012&name=[COLORgreen]Sky+Movies+Action+%26+Adventure+UK%0D[/COLOR]' + '\n' )
 oOo00Ooo0o0 . write ( r'Sky Thriller=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F40.m3u8&mode=10012&name=[COLORgreen]Sky+Movies+Crime+%26+Thriller+UK%0D[/COLOR]' + '\n' )
 oOo00Ooo0o0 . write ( r'Sky Comedy=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F43.m3u8&mode=10012&name=[COLORgreen]Sky+Movies+Comedy+UK%0D[/COLOR]' + '\n' )
 oOo00Ooo0o0 . write ( r'Sky Greats=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F41.m3u8&mode=10012&name=[COLORgreen]Sky+Movies+Greats+UK%0D[/COLOR]' + '\n' )
 oOo00Ooo0o0 . write ( r'Sky ScFiHorror=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F44.m3u8&mode=10012&name=[COLORgreen]Sky+Movies+Sci-Fi+%26+Horror+UK%0D[/COLOR]' + '\n' )
 oOo00Ooo0o0 . write ( r'Sky Showcase=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F46.m3u8&mode=10012&name=[COLORgreen]Sky+Movies+Showcase+UK%0D[/COLOR]' + '\n' )
 oOo00Ooo0o0 . write ( r'Sky Select=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F45.m3u8&mode=10012&name=[COLORgreen]Sky+Movies+Select+UK%0D[/COLOR]' + '\n' )
 oOo00Ooo0o0 . write ( r'Sky DramaRom=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F47.m3u8&mode=10012&name=[COLORgreen]Sky+Movies+Drama+%26+Romance+UK%0D[/COLOR]' + '\n' )
 oOo00Ooo0o0 . write ( r'Sky Family=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F48.m3u8&mode=10012&name=[COLORgreen]Sky+Movies+Family+UK%0D[/COLOR]' + '\n' )
 oOo00Ooo0o0 . write ( r'Sky Disney=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F195.m3u8&mode=10012&name=[COLORgreen]Sky+Movies+Disney+UK%0D[/COLOR]' + '\n' )
 oOo00Ooo0o0 . write ( r'Fox Movies HD MX=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F436.m3u8&mode=10012&name=[COLORgreen]Fox+Movies+HD+MX%0D[/COLOR]' + '\n' )
 oOo00Ooo0o0 . write ( r'Film Zone MX HD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F437.m3u8&mode=10012&name=[COLORgreen]Film+Zone+MX+HD%0D[/COLOR]' + '\n' )
 oOo00Ooo0o0 . write ( r'Eurosport=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F269.m3u8&mode=10012&name=[COLORgreen]Eurosport+1+UK%0D[/COLOR]' + '\n' )
 oOo00Ooo0o0 . write ( r'Sky Sports 1=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F403.m3u8&mode=10012&name=[COLORgreen]Sky+Sports+1+UK%0D[/COLOR]' + '\n' )
 oOo00Ooo0o0 . write ( r'Sky Sports 2=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F404.m3u8&mode=10012&name=[COLORgreen]Sky+Sports+2+UK%0D[/COLOR]' + '\n' )
 oOo00Ooo0o0 . write ( r'Sky Sports 3=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F405.m3u8&mode=10012&name=[COLORgreen]Sky+Sports+3+UK%0D[/COLOR]' + '\n' )
 oOo00Ooo0o0 . write ( r'Sky Sports 4=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F406.m3u8&mode=10012&name=[COLORgreen]Sky+Sports+4+UK%0D[/COLOR]' + '\n' )
 oOo00Ooo0o0 . write ( r'Sky Sports 5=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F407.m3u8&mode=10012&name=[COLORgreen]Sky+Sports+5+UK%0D[/COLOR]' + '\n' )
 oOo00Ooo0o0 . write ( r'Sky Sports F1=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F412.m3u8&mode=10012&name=[COLORgreen]Sky+Sports+F1%0D[/COLOR]' + '\n' )
 oOo00Ooo0o0 . write ( r'BT Sport 1=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F423.m3u8&mode=10012&name=[COLORgreen]BT+Sports+1%0D[/COLOR]' + '\n' )
 oOo00Ooo0o0 . write ( r'BT Sport 2=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F413.m3u8&mode=10012&name=[COLORgreen]BT+Sports+2%0D[/COLOR]' + '\n' )
 oOo00Ooo0o0 . write ( r'Fox Sports 1 HD MX=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F439.m3u8&mode=10012&name=[COLORgreen]Fox+Sports+1+HD+MX%0D[/COLOR]' + '\n' )
 oOo00Ooo0o0 . write ( r'ESPN 1 HD ES=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F440.m3u8&mode=10012&name=[COLORgreen]ESPN+1+HD+ES%0D[/COLOR]' + '\n' )
 oOo00Ooo0o0 . write ( r'ESPN 2 HD ES=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F441.m3u8&mode=10012&name=[COLORgreen]ESPN+2+HD+ES%0D[/COLOR]' + '\n' )
 oOo00Ooo0o0 . write ( r'At The Races=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F427.m3u8&mode=10012&name=[COLORgreen]At+The+Races+UK%0D[/COLOR]' + '\n' )
 oOo00Ooo0o0 . write ( r'Racing UK=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oO0o0o0ooO0oO + '%2F' + oo0o0O00 + '%2F426.m3u8&mode=10012&name=[COLORgreen]Racing+UK%0D[/COLOR]' + '\n' )
 if 87 - 87: I1IiI / Ooo0OO0 + iIii1I11I1II1
 if 93 - 93: iIii1I11I1II1 + OOO0OOO00oo % II11i1iIiII1
 if 21 - 21: Oo000
def iIiI1I1IIi11 ( ) :
 if 9 - 9: II11i1iIiII1 + OoOo00o - iI / i1IIi % ii11ii1ii / Ooo0OO0
 O00Oo000ooO0 ( '[COLORgreen]Recent Episodes[/COLOR]' , '' , 10019 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 O00Oo000ooO0 ( '[COLORgreen]Genres[/COLOR]' , '' , 10020 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 O00Oo000ooO0 ( '[COLORgreen]Search[/COLOR]' , '' , 10021 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 if 60 - 60: ii11ii1ii
def IIoO00OoOo ( ) :
 if 74 - 74: OoOoOO00 . O0 - OOOo0 + Ooo0OO0 % i11iIiiIii % I1IiI
 i1I1i1 = cloudflare . source ( i1111 ( 'aHR0cDovL2RpemlsYWIuY29t' ) )
 IIIII11I1IiI = re . compile ( '<li id=".+?">.+?<a href="(.+?)">.+?<img width="40" height="40" src="(.+?)" alt=""/>.+?<span class="title">\n(.+?)</span>.+?<span class="alt-title">\n(.+?)</span>.+?</a>.+?</li>' , re . DOTALL ) . findall ( i1I1i1 )
 for OOOooo , OO0O000 , I1Ii , O0oo00o0O in IIIII11I1IiI :
  O00Oo000ooO0 ( I1Ii + '  -  ' + ( O0oo00o0O ) . replace ( 'sezon' , 'Season' ) . replace ( 'bölüm' , 'Episode' ) , OOOooo , 10023 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
  if 78 - 78: i1I111ii1II1i + I1IiI + Ooo0OO0 - Ooo0OO0 . i11iIiiIii / Ooo00oOo00o
  if 27 - 27: i1I111ii1II1i - O0 % iI * OoO0O0 . Ooo0OO0 % iIii1I11I1II1
  if 37 - 37: OoooooooOO + O0 - i1IIi % II11i1iIiII1
def i1I1i1i ( ) :
 if 36 - 36: OoOoOO00 % O0
 O00Oo000ooO0 ( '[COLORgreen]Action[/COLOR]' , 'Aksiyon' , 10024 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 O00Oo000ooO0 ( '[COLORgreen]Adventure[/COLOR]' , 'Macera' , 10024 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 O00Oo000ooO0 ( '[COLORgreen]Animation[/COLOR]' , 'Animasyon' , 10024 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 O00Oo000ooO0 ( '[COLORgreen]Anime[/COLOR]' , 'Anime' , 10024 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 O00Oo000ooO0 ( '[COLORgreen]Biography[/COLOR]' , 'Biyografi' , 10024 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 O00Oo000ooO0 ( '[COLORgreen]Comedy[/COLOR]' , 'Komedi' , 10024 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 O00Oo000ooO0 ( '[COLORgreen]Crime[/COLOR]' , 'Su%C3%A7' , 10024 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 O00Oo000ooO0 ( '[COLORgreen]Documentary[/COLOR]' , 'Belgesel' , 10024 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 O00Oo000ooO0 ( '[COLORgreen]Drama[/COLOR]' , 'Dram' , 10024 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 O00Oo000ooO0 ( '[COLORgreen]Family[/COLOR]' , 'Aile' , 10024 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 O00Oo000ooO0 ( '[COLORgreen]Fantasy[/COLOR]' , 'Fantastik' , 10024 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 O00Oo000ooO0 ( '[COLORgreen]History[/COLOR]' , 'Tarih' , 10024 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 O00Oo000ooO0 ( '[COLORgreen]Horror[/COLOR]' , 'Korku' , 10024 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 O00Oo000ooO0 ( '[COLORgreen]Mini-Series[/COLOR]' , 'Mini%20Dizi' , 10024 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 O00Oo000ooO0 ( '[COLORgreen]Musical[/COLOR]' , 'M%C3%BCzikal' , 10024 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 O00Oo000ooO0 ( '[COLORgreen]Mystery[/COLOR]' , 'Gizem' , 10024 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 O00Oo000ooO0 ( '[COLORgreen]Romance[/COLOR]' , 'Romantik' , 10024 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 O00Oo000ooO0 ( '[COLORgreen]Science Fiction[/COLOR]' , 'Bilim%20Kurgu' , 10024 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 O00Oo000ooO0 ( '[COLORgreen]Sport[/COLOR]' , 'Spor' , 10024 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 O00Oo000ooO0 ( '[COLORgreen]Thriller[/COLOR]' , 'Gerilim' , 10024 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 O00Oo000ooO0 ( '[COLORgreen]War[/COLOR]' , 'Sava%C5%9F' , 10024 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 O00Oo000ooO0 ( '[COLORgreen]Western[/COLOR]' , 'Tarih' , 10024 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 O00Oo000ooO0 ( '[COLORgreen]Youth[/COLOR]' , 'Gen%C3%A7lik' , 10024 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
 if 35 - 35: iIii1I11I1II1 - Oo000 % OOooOOo
def I111i1Ii1i1 ( url ) :
 OO0O0 = 'http://dizilab.com/arsiv?limit=100&tur=' + url + '&orderby=&ulke=&order=&yil=&dizi_adi='
 III1IiiI = cloudflare . source ( OO0O0 )
 IIIII11I1IiI = re . compile ( '<div class="tv-series-single">.+?<a href="(.+?)" class="film-image">.+?<img src="(.+?)" alt=""/>.+?<span class="position">.+?</span>\n(.+?)</a>' , re . DOTALL ) . findall ( III1IiiI )
 for url , OO0O000 , I1Ii in IIIII11I1IiI :
  O00Oo000ooO0 ( '[COLORgreen]' + I1Ii + '[/COLOR]' , url , 10022 , ii11iIi1I + 'dtv.png' , i1iiIII111ii , '' )
  if 11 - 11: I1IiI % Ooo0OO0
  if 53 - 53: II11i1iIiII1 / iIii1I11I1II1 - Ooo00oOo00o + OOO0OOO00oo
  if 30 - 30: Ooo0OO0
  if 24 - 24: Ooo00oOo00o - OOO0OOO00oo + ii11ii1ii / OoOo00o % OOOo0 + iIii1I11I1II1
def oO00o ( ) :
 if 36 - 36: OoO0O0 . OoOoOO00 % II11i1iIiII1
 i1111I1I = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oOOoo00O00o = i1111I1I . lower ( )
 OOOooo = ( i1111 ( 'aHR0cDovL2RpemlsYWIuY29tL2Fyc2l2P2xpbWl0PSZ0dXI9Jm9yZGVyYnk9JnVsa2U9Jm9yZGVyPSZ5aWw9JmRpemlfYWRpPQ==' ) ) + ( i1111I1I ) . replace ( ' ' , '+' )
 III1IiiI = cloudflare . source ( OOOooo )
 IIIII11I1IiI = re . compile ( '<a href="(.+?)" class="film-image">\n<img src="(.+?)" alt=""/>\n</a>\n<div class="tss-detail">\n<a class="title" style="" href=".+?">\n<span class="position">.+?</span>\n(.+?)</a>' ) . findall ( III1IiiI )
 for OOOooo , OO0O000 , I1Ii in IIIII11I1IiI :
  if i1111I1I in I1Ii . lower ( ) :
   O00Oo000ooO0 ( '[COLORgreen]' + I1Ii + '[/COLOR]' , OOOooo , 10022 , ii11iIi1I + 'dtv.png' )
   if 84 - 84: OoooooooOO - i11iIiiIii / iIii1I11I1II1 / OoooooooOO / ii11ii1ii
   if 4 - 4: Oo + OOooOOo
   if 17 - 17: Ooo00oOo00o * I1IiI
def ii11i ( url ) :
 III1IiiI = cloudflare . source ( url )
 IIIII11I1IiI = re . compile ( '<a class="season" href="(.+?)">\n(.+?)\n</a>.+?<a class="episode" href=".+?">\n(.+?)\n</a>.+?<a class="episode-name" href=".+?">\n(.+?)</a>' , re . DOTALL ) . findall ( III1IiiI )
 for ooI1111i , o00Oo , O000oOo , I1Ii in IIIII11I1IiI :
  IiiIIi1 = ( O000oOo ) . replace ( 'Sezon' , '' ) . replace ( 'bölüm' , '' ) . replace ( 'Bölüm' , '' ) . replace ( 'BÃ¶lÃ¼m' , '' ) . replace ( '.' , '' )
  iI1iIiiI = ( o00Oo ) . replace ( 'bölüm' , '' ) . replace ( 'Sezon' , '' ) . replace ( 'Bölüm' , '' ) . replace ( 'BÃ¶lÃ¼m' , '' ) . replace ( '.' , '' )
  Oo0OOo = 'Season ' + iI1iIiiI + 'Episode ' + IiiIIi1 + I1Ii
  Ii1I11i11I1i ( Oo0OOo , ooI1111i )
  if 59 - 59: i1IIi
  xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 48 - 48: O0 * i1I111ii1II1i * Ooo00oOo00o . Ooo00oOo00o * iI - i1I111ii1II1i
  if 14 - 14: ii11ii1ii + i11iIiiIii
def Ii1I11i11I1i ( name , url ) :
 ooI1111i = url
 OOOoo = name
 II11IiIi11 = cloudflare . source ( ooI1111i )
 IIOOO0O00O0OOOO = re . compile ( 'file: "(.+?)",.+?label: "(.+?)",' , re . DOTALL ) . findall ( II11IiIi11 )
 for I1iiii1I , III1II1iii1i in IIOOO0O00O0OOOO :
  I11I1IIiiII1 ( '[COLORgreen]' + OOOoo + III1II1iii1i + '[/COLOR]' , I1iiii1I , 10012 , ii11iIi1I + 'dtv.png' )
  if 75 - 75: Ooo0OO0 - I1IiI - iIii1I11I1II1 % OOooOOo
 xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 58 - 58: O0 . Ooo0OO0 / OoooooooOO . Ooo00oOo00o / Oo * OoOoOO00
 if 53 - 53: i1I111ii1II1i - O0 / OOooOOo % OoOo00o * OOOo0 % Oo000
def o0oOOOO0 ( ) :
 if 11 - 11: i1IIi
 if 19 - 19: OoOo00o - OOooOOo - i1I111ii1II1i - I1IiI . OoOo00o . OoO0O0
 if 48 - 48: OoOo00o + Ooo0OO0
 if 60 - 60: iI + OoOo00o . Ooo0OO0 / i1IIi . iIii1I11I1II1
 if 14 - 14: Oo000
 if 79 - 79: i1I111ii1II1i
 if 76 - 76: iIii1I11I1II1
 if 80 - 80: iIii1I11I1II1 . O0 / i1I111ii1II1i % i1I111ii1II1i
 if 93 - 93: OoooooooOO * Oo
 if 10 - 10: OoO0O0 * OoooooooOO + iI - ii11ii1ii / ii11ii1ii . i11iIiiIii
 if 22 - 22: OoO0O0 / OOooOOo
 if 98 - 98: i1IIi
 if 51 - 51: ii11ii1ii + II11i1iIiII1 + Oo / i1IIi + i1IIi
 if 12 - 12: iIii1I11I1II1 . i1I111ii1II1i . ii11ii1ii % OOOo0 . OoOoOO00 . OOO0OOO00oo
 if 32 - 32: ii11ii1ii + Ooo0OO0 / O0 / I1IiI * OoooooooOO % II11i1iIiII1
 O00Oo000ooO0 ( '[COLORgreen]Newest Episodes Added[/COLOR]' , 'http://www.watchseries.li/latest' , 10046 , ii11iIi1I + 'WATCHSERIES.png' , '' , '' )
 O00Oo000ooO0 ( '[COLORgreen]This Week\'s Popular Episodes[/COLOR]' , 'http://www.watchseries.li/new' , 10042 , ii11iIi1I + 'WATCHSERIES.png' , '' , '' )
 O00Oo000ooO0 ( '[COLORgreen]Search Program[/COLOR]' , '' , 10043 , ii11iIi1I + 'WATCHSERIES.png' , '' , '' )
 if 50 - 50: Ooo00oOo00o
 if 66 - 66: iIii1I11I1II1
def I11II1i11 ( url ) :
 III1IiiI = iIi1 ( url )
 IIiII111iiI1I = re . compile ( '<ul class="pagination" style="line-height: 3;">(.+?)</ul>' , re . DOTALL ) . findall ( III1IiiI )
 IIIII11I1IiI = re . compile ( '<li><a href="/letters/(.+?)">(.+?)</a></li>' ) . findall ( str ( IIiII111iiI1I ) )
 for url , I1Ii in IIIII11I1IiI :
  O00Oo000ooO0 ( '[COLORgreen]' + I1Ii + '[/COLOR]' , 'http://watchseries.li/letters/' + url , 10049 , ii11iIi1I + 'WATCHSERIES.png' , '' , '' )
  if 28 - 28: OoOoOO00 - OOO0OOO00oo % I1IiI + Ooo00oOo00o - I1IiI
def IiI ( url ) :
 III1IiiI = iIi1 ( url )
 IIIII11I1IiI = re . compile ( '<a href="(.+?)" class="sr-header">(.+?)</a>' ) . findall ( III1IiiI )
 for url , I1Ii in IIIII11I1IiI :
  O00Oo000ooO0 ( '[COLORgreen]' + I1Ii + '[/COLOR]' , 'http://watchseries.li/' + url , 10049 , ii11iIi1I + 'WATCHSERIES.png' , '' , '' )
  if 63 - 63: O0
def i1I1iIii11 ( url ) :
 III1IiiI = iIi1 ( url )
 IIIII11I1IiI = re . compile ( '<li class="col-md-6 col-xs-12 list-movies-li"><a href="(.+?)" title=".+?">(.+?)<span class="epnum">.+?</span></a></li>' , re . DOTALL ) . findall ( III1IiiI )
 IIOOO0O00O0OOOO = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="(.+?)">Next</a></li></ul>' , re . DOTALL ) . findall ( III1IiiI )
 for url , I1Ii in IIIII11I1IiI :
  O00Oo000ooO0 ( '[COLORgreen]' + ( I1Ii ) . replace ( '&nbsp;' , ' ' ) . replace ( '&amp;' , '&' ) . replace ( '&#039;' , '\'' ) + '[/COLOR]' , 'http://www.watchseries.li' + url , 10044 , ii11iIi1I + 'WATCHSERIES.png' , '' , '' )
 for url in IIOOO0O00O0OOOO :
  O00Oo000ooO0 ( '[COLORgreen]' + 'NEXT' + '[/COLOR]' , 'http://www.watchseries.li' + url , 10049 , ii11iIi1I + 'Next.png' , '' , '' )
  if 80 - 80: I1IiI - OoOoOO00
  if 35 - 35: II11i1iIiII1 - Ooo00oOo00o . Oo * Oo / i11iIiiIii + ii11ii1ii
def oOo0Oo0O0O ( ) :
 i1111I1I = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 III1II1i = 'http://www.watchseries.li/search/' + i1111I1I . replace ( ' ' , '%20' )
 III1IiiI = iIi1 ( III1II1i )
 IIIII11I1IiI = re . compile ( '<img src="(.+?)".+?<a href="(.+?)" title=".+?"><b>(.+?)</b>' , re . DOTALL ) . findall ( III1IiiI )
 for OO0O000 , OOOooo , I1Ii in IIIII11I1IiI :
  if 'watch online' in I1Ii :
   pass
  else :
   print OOOooo
   O00Oo000ooO0 ( '[COLORgreen]' + I1Ii + '[/COLOR]' , 'http://www.watchseries.li' + OOOooo , 10044 , OO0O000 , '' , '' )
   if 3 - 3: OoOo00o
   xbmcplugin . setContent ( O00o0OO , 'movies' )
   if 35 - 35: Ooo0OO0 . O0 + Oo + Oo000 + i1IIi
def OooOooO0O0o0 ( url ) :
 III1IiiI = iIi1 ( url )
 IIIII11I1IiI = re . compile ( '<img src="(.+?)".+?<div class="block-left-home-inside-text">.+?<a href="(.+?)" title=".+?"><b>(.+?)</b> <br>.+?<span class=".+?">(.+?)</span></a><br>(.+?)<br>' , re . DOTALL ) . findall ( III1IiiI )
 for OO0O000 , url , I1Ii , O000oOo , oo0o in IIIII11I1IiI :
  OOO0o0 = ( I1Ii ) . replace ( '&nbsp;' , ' ' ) . replace ( '&amp;' , '&' ) . replace ( '&#039;' , '\'' ) + ' - ' + ( O000oOo ) . replace ( '&amp;' , '&' ) . replace ( '&#039;' , '\'' )
  O00Oo000ooO0 ( '[COLORgreen]' + OOO0o0 + '[/COLOR]' , 'http://www.watchseries.li' + url , 10045 , OO0O000 , '' , oo0o )
  if 34 - 34: OOOo0 % Oo - I1IiI + OoOo00o
def Ooo0Oo0o ( url ) :
 III1IiiI = iIi1 ( url )
 IIIII11I1IiI = re . compile ( '<li class="col-md-6 col-xs-12 list-movies-li"><a href="(.+?)" title=".+?">(.+?)<span class="epnum">.+?</span></a></li>' , re . DOTALL ) . findall ( III1IiiI )
 IIOOO0O00O0OOOO = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="(.+?)">Next</a></li></ul>' , re . DOTALL ) . findall ( III1IiiI )
 for url , I1Ii in IIIII11I1IiI :
  OOO0o0 = ( I1Ii ) . replace ( '&nbsp;' , ' ' ) . replace ( '&amp;' , '&' ) . replace ( '&#039;' , '\'' )
  O00Oo000ooO0 ( '[COLORgreen]' + OOO0o0 + '[/COLOR]' , 'http://www.watchseries.li' + url , 10045 , ii11iIi1I + 'WATCHSERIES.png' , '' , '' )
 for url in IIOOO0O00O0OOOO :
  O00Oo000ooO0 ( '[COLORgreen]' + 'NEXT' + '[/COLOR]' , 'http://www.watchseries.li' + url , 10046 , ii11iIi1I + 'Next.png' , '' , '' )
  if 85 - 85: OOOo0
def Ii1Ii1I ( url ) :
 III1IiiI = iIi1 ( url )
 IIIII11I1IiI = re . compile ( '<div class="mask">.+?<a href="(.+?)" title="(.+?)">.+?<img src="(.+?)"' , re . DOTALL ) . findall ( III1IiiI )
 IIOOO0O00O0OOOO = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="(.+?)">Next</a></li></ul>' , re . DOTALL ) . findall ( III1IiiI )
 for url , I1Ii , OO0O000 in IIIII11I1IiI :
  O00Oo000ooO0 ( '[COLORgreen]' + ( I1Ii ) . replace ( '&nbsp;' , ' ' ) . replace ( '&amp;' , '&' ) . replace ( '&#039;' , '\'' ) + '[/COLOR]' , 'http://www.watchseries.li' + url , 10044 , OO0O000 , '' , '' )
 for url in IIOOO0O00O0OOOO :
  O00Oo000ooO0 ( '[COLORgreen]' + 'NEXT' + '[/COLOR]' , 'http://www.watchseries.li' + url , 10041 , ii11iIi1I + 'Next.png' , '' , '' )
  if 54 - 54: OOO0OOO00oo + I1IiI
def o0O00O ( url ) :
 III1IiiI = iIi1 ( url )
 IIiII111iiI1I = re . compile ( '<div class="col-md-6 col-xs-12".+?<a href=".+?" itemprop="url"><span itemprop="name">(.+?)</span>(.+?)</ul>' , re . DOTALL ) . findall ( III1IiiI )
 for o00Oo , oO000o in IIiII111iiI1I :
  IIIII11I1IiI = re . compile ( '<li itemprop="episode".+?<meta itemprop="url" content="(.+?)">.+?<span class="" itemprop="name">\n(.+?)\n' , re . DOTALL ) . findall ( str ( oO000o ) )
  for url , I1Ii in IIIII11I1IiI :
   OOO0o0 = ( o00Oo ) . replace ( '  ' , '' ) + ' ' + ( I1Ii ) . replace ( '&nbsp;' , ' ' ) . replace ( '&#039;' , '\'' ) . replace ( '  ' , '' )
   O00Oo000ooO0 ( '[COLORgreen]' + OOO0o0 + '[/COLOR]' , 'http://www.watchseries.li' + url , 10045 , ii11iIi1I + 'WATCHSERIES.png' , '' , '' )
 IIOOO0O00O0OOOO = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="(.+?)">Next</a></li></ul>' , re . DOTALL ) . findall ( III1IiiI )
 for url in IIOOO0O00O0OOOO :
  O00Oo000ooO0 ( '[COLORgreen]' + 'NEXT' + '[/COLOR]' , 'http://www.watchseries.li' + url , 10044 , ii11iIi1I + 'Next.png' , '' , '' )
  if 94 - 94: i1I111ii1II1i - ii11ii1ii + OOooOOo - Oo
  if 15 - 15: Oo000
class i1iiI ( ) :
 if 83 - 83: OOO0OOO00oo / iIii1I11I1II1 + i1IIi / OoOo00o
 List = [ ]
 source_list = [ ]
 def __init__ ( self , name ) :
  if 47 - 47: OOO0OOO00oo + OoooooooOO . OoOoOO00 . OoOo00o
  OOO0o0 = name
  self . Get_Sources ( OOOooo , OOO0o0 )
  if 66 - 66: II11i1iIiII1 * I1IiI
  if 2 - 2: OOO0OOO00oo . OoO0O0 * Oo + O0 - iI * iIii1I11I1II1
 def Get_Sources ( self , URL , season_name ) :
  Oo0oO0ooo = xbmcgui . DialogProgress ( )
  III1IiiI = iIi1 ( URL )
  IIIII11I1IiI = re . compile ( '<td>.+?<a href="/link/(.+?)".+?height="16px">(.+?)\n' , re . DOTALL ) . findall ( III1IiiI )
  for OOOooo , I1Ii in IIIII11I1IiI :
   URL = 'http://www.watchseries.li/link/' + OOOooo
   self . Get_site_link ( URL , season_name )
   if 12 - 12: OOooOOo * OoO0O0 % OoOoOO00 * i1IIi * iIii1I11I1II1
 def Get_site_link ( self , url , season_name ) :
  III1IiiI = iIi1 ( url )
  IIIII11I1IiI = re . compile ( '<iframe style=.+?" src="(.+?)"' ) . findall ( III1IiiI )
  IIOOO0O00O0OOOO = re . compile ( '<IFRAME SRC="(.+?)"' ) . findall ( III1IiiI )
  iI1I11iIIi1 = re . compile ( '<IFRAME style=".+?" SRC="(.+?)"' ) . findall ( III1IiiI )
  for url in IIIII11I1IiI :
   self . main ( url , season_name )
  for url in IIOOO0O00O0OOOO :
   self . main ( url , season_name )
  for url in iI1I11iIIi1 :
   self . main ( url , season_name )
   if 81 - 81: Oo - iI
 def main ( self , url , season_name ) :
  Oo0oO0ooo . create ( "[COLORwhite]Origin[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
  if 'daclips.in' in url :
   ii1iII1iI111 = 'DACLIPS'
   if ii1iII1iI111 in i1iiI . source_list :
    pass
   else :
    self . daclips ( url , season_name , ii1iII1iI111 )
    Oo0oO0ooo . update ( 0 , "" , "Getting Daclips Links" )
  else :
   if 'filehoot.com' in url :
    ii1iII1iI111 = 'FILEHOOT'
    if ii1iII1iI111 in i1iiI . source_list :
     pass
    else :
     Oo0oO0ooo . update ( 0 , "" , "Getting Filehoot Links" )
     self . filehoot ( url , season_name , ii1iII1iI111 )
   else :
    if 'thevideo.me' in url :
     ii1iII1iI111 = 'THEVIDEO'
     if ii1iII1iI111 in i1iiI . source_list :
      pass
     else :
      self . thevideo ( url , season_name , ii1iII1iI111 )
      Oo0oO0ooo . update ( 0 , "" , "Getting Thevideo Links" )
    else :
     if 'allmyvideos.net' in url :
      ii1iII1iI111 = 'ALLMYVIDEOS'
      if ii1iII1iI111 in i1iiI . source_list :
       pass
      else :
       self . allmyvid ( url , season_name , ii1iII1iI111 )
       Oo0oO0ooo . update ( 0 , "" , "Getting Allmyvideo Links" )
     else :
      if 'vidspot.net' in url :
       ii1iII1iI111 = 'VIDSPOT'
       if ii1iII1iI111 in i1iiI . source_list :
        pass
       else :
        self . vidspot ( url , season_name , ii1iII1iI111 )
        Oo0oO0ooo . update ( 0 , "" , "Getting Vidspot Links" )
      else :
       if 'vodlocker' in url :
        ii1iII1iI111 = 'VODLOCKER'
        if ii1iII1iI111 in i1iiI . source_list :
         pass
        else :
         self . vodlocker ( url , season_name , ii1iII1iI111 )
         Oo0oO0ooo . update ( 0 , "" , "Getting Vodlocker Links" )
         if 94 - 94: OoOo00o % II11i1iIiII1 . OOO0OOO00oo
         if 85 - 85: Oo000 * i1IIi % OOOo0 - II11i1iIiII1
 def allmyvid ( self , url , season_name , source_name ) :
  III1IiiI = iIi1 ( url )
  IIIII11I1IiI = re . compile ( '"file" : "(.+?)",\n.+?"default" : .+?,\n.+?"label" : "(.+?)"' , re . DOTALL ) . findall ( III1IiiI )
  for I11I1ii1i , I1Ii in IIIII11I1IiI :
   self . Printer ( I11I1ii1i , season_name , source_name )
   if 22 - 22: OOO0OOO00oo * i1I111ii1II1i * i11iIiiIii + OoOo00o * I1IiI * Ooo00oOo00o
 def vidspot ( self , url , season_name , source_name ) :
  III1IiiI = iIi1 ( url )
  IIIII11I1IiI = re . compile ( '"file" : "(.+?)",\n.+?"default" : .+?,\n.+?"label" : "(.+?)"' ) . findall ( III1IiiI )
  for I11I1ii1i , I1Ii in IIIII11I1IiI :
   self . Printer ( I11I1ii1i , season_name , source_name )
   if 85 - 85: OoOo00o * Oo000 % Oo - OoOo00o - iI
 def thevideo ( self , url , season_name , source_name ) :
  III1IiiI = iIi1 ( url )
  IIIII11I1IiI = re . compile ( "{ label: '.+?', file: '(.+?)' }" ) . findall ( III1IiiI )
  for I11I1ii1i in IIIII11I1IiI :
   self . Printer ( I11I1ii1i , season_name , source_name )
   if 46 - 46: O0
 def vodlocker ( self , url , season_name , source_name ) :
  III1IiiI = iIi1 ( url )
  IIIII11I1IiI = re . compile ( 'file: "(.+?)",.+?skin' , re . DOTALL ) . findall ( III1IiiI )
  for I11I1ii1i in IIIII11I1IiI :
   self . Printer ( I11I1ii1i , season_name , source_name )
   if 65 - 65: iIii1I11I1II1 % OOO0OOO00oo + O0 / OoooooooOO
 def daclips ( self , url , season_name , source_name ) :
  III1IiiI = iIi1 ( url )
  IIIII11I1IiI = re . compile ( '{ file: "(.+?)", type:"video" }' ) . findall ( III1IiiI )
  for I11I1ii1i in IIIII11I1IiI :
   self . Printer ( I11I1ii1i , season_name , source_name )
   if 52 - 52: i1I111ii1II1i % Oo000 * OOOo0 % iI + Oo000 / OoOo00o
 def filehoot ( self , url , season_name , source_name ) :
  III1IiiI = iIi1 ( url )
  IIIII11I1IiI = re . compile ( 'file: "(.+?)",.+?skin' , re . DOTALL ) . findall ( III1IiiI )
  for I11I1ii1i in IIIII11I1IiI :
   self . Printer ( I11I1ii1i , season_name , source_name )
   if 80 - 80: OoooooooOO + Ooo0OO0
 def Printer ( self , Link , season_name , source_name ) :
  if 95 - 95: OoO0O0 / OOO0OOO00oo * OoO0O0 - OoooooooOO * OoooooooOO % Ooo00oOo00o
  if Link in i1iiI . List :
   pass
  elif source_name in i1iiI . source_list :
   pass
  else :
   I11I1IIiiII1 ( '[COLORgreen]' + source_name + '[/COLOR]' , Link , 10012 , ii11iIi1I + 'WATCHSERIES.png' )
   Oo0oO0ooo . update ( 100 , "" , "Got Source" )
   i1iiI . List . append ( Link )
   i1iiI . source_list . append ( source_name )
   if 43 - 43: Oo . OoO0O0
   xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
   if 12 - 12: OoO0O0 + Oo000 + iI . Ooo0OO0 / i1I111ii1II1i
   if 29 - 29: Ooo0OO0 . II11i1iIiII1 - OoOoOO00
   if 68 - 68: iIii1I11I1II1 + OoOoOO00 / OOO0OOO00oo
   if 91 - 91: I1IiI % iIii1I11I1II1 . OOOo0
   if 70 - 70: iI % OoOoOO00 % O0 . i1IIi / OoO0O0
def OO0ooOoOO0OOo ( ) :
 O00Oo000ooO0 ( '[COLORgreen]Highlights[/COLOR]' , '' , 10008 , ii11iIi1I + 'ORIGINFOOTBALL.png' , i1iiIII111ii , '' )
 O00Oo000ooO0 ( '[COLORgreen]Fixtures[/COLOR]' , '' , 10009 , ii11iIi1I + 'ORIGINFOOTBALL.png' , i1iiIII111ii , '' )
 if 51 - 51: iIii1I11I1II1 * OOooOOo / iIii1I11I1II1 . iIii1I11I1II1 . OoOo00o * iI
def oO0oo0o00o0O ( ) :
 i1I1i1 = iIi1 ( i1111 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20vcXVpY2tpbmRleC5odG1s' ) )
 IIIII11I1IiI = re . compile ( '<a target="_self" href="(.+?)".+?src="(.+?)" alt="(.+?)"' , re . DOTALL ) . findall ( i1I1i1 )
 for OOOooo , OO0O000 , I1Ii in IIIII11I1IiI :
  O00Oo000ooO0 ( '[COLORgreen]' + ( I1Ii ) . replace ( 'amp;' , '' ) + '[/COLOR]' , i1111 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20v' ) + OOOooo , 10010 , i1111 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20v' ) + OO0O000 , i1iiIII111ii , '' )
  if 80 - 80: iIii1I11I1II1
def i1I11 ( url ) :
 III1IiiI = iIi1 ( url )
 IIiII111iiI1I = re . compile ( 'AndClearL.+?><h2.+?head>(.*?)float' , re . DOTALL ) . findall ( III1IiiI )
 for IIiII111iiI1I in IIiII111iiI1I :
  iII11ii1ii = re . compile ( '(.*?)</h2>' ) . findall ( str ( IIiII111iiI1I ) )
  for oOO0OOOo000o in iII11ii1ii :
   oOO0OOOo000o = oOO0OOOo000o
  OO00oo = re . compile ( 'comp_head>(.*?)</span>.*?<div class = fLeft width = ".*?"><img src="(.*?)">.*?</div>.*?ST:(.*?)</div>(.+?)<!-- around all of channel types ENDS 2-->' , re . DOTALL ) . findall ( str ( IIiII111iiI1I ) )
  for O0Oo0O0 , OO0O000 , time , I1IiiIiii1 in OO00oo :
   o0OOo0o0O0O = re . compile ( ",CAPTION, '(.+?)&nbsp" ) . findall ( I1IiiIiii1 )
   O00Oo000ooO0 ( '[COLORgreen]' + oOO0OOOo000o + ' - ' + O0Oo0O0 + ' - ' + time + '[/COLOR]' , '' , 10010 , i1111 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20=' ) + OO0O000 , i1iiIII111ii , ( str ( o0OOo0o0O0O ) ) )
   if 39 - 39: II11i1iIiII1 / O0 * Ooo0OO0
 ii111 ( 'tvshows' , 'Media Info 3' )
 if 17 - 17: i1I111ii1II1i / iIii1I11I1II1 - Ooo00oOo00o + OOOo0 % Oo000
def III1III11II ( ) :
 if 43 - 43: OOOo0
 O00Oo000ooO0 ( '[COLORgreen]Shows[/COLOR]' , 'http://www.fullmatchesandshows.com/category/show/' , 10011 , 'http://www.fm-base.co.uk/forum/attachments/club-competition-logos/3885-soccer-am-logo-socceram.png' , ii11iIi1I + 'fanart.jpg' , '' )
 O00Oo000ooO0 ( '[COLORgreen]Premier League[/COLOR]' , 'http://www.fullmatchesandshows.com/premier-league/' , 10011 , 'https://footballseasons.files.wordpress.com/2013/05/premier-league.png' , ii11iIi1I + 'fanart.jpg' , '' )
 O00Oo000ooO0 ( '[COLORgreen]La Liga[/COLOR]' , 'http://www.fullmatchesandshows.com/la-liga/' , 10011 , 'http://1.bp.blogspot.com/-c6kQ40ryhyo/U19cUlz25sI/AAAAAAAABak/qtn5chSFZm0/s1600/la-liga-logo_display_image.png' , ii11iIi1I + 'fanart.jpg' , '' )
 O00Oo000ooO0 ( '[COLORgreen]Bundesliga[/COLOR]' , 'http://www.fullmatchesandshows.com/bundesliga/' , 10011 , 'http://m.img.brothersoft.com/iphone/189/518670189_icon175x175.jpg' , ii11iIi1I + 'fanart.jpg' , '' )
 O00Oo000ooO0 ( '[COLORgreen]Champions League[/COLOR]' , 'http://www.fullmatchesandshows.com/champions-league/' , 10011 , 'http://www.ecursuri.ro/images/teste/test-champions-league.jpg' , ii11iIi1I + 'fanart.jpg' , '' )
 O00Oo000ooO0 ( '[COLORgreen]Serie A[/COLOR]' , 'http://www.fullmatchesandshows.com/category/serie-a/' , 10011 , 'http://files.jcriccione.it/200000223-2484526782/serie%20a.png' , ii11iIi1I + 'fanart.jpg' , '' )
 O00Oo000ooO0 ( '[COLORgreen]Ligue 1[/COLOR]' , 'http://www.fullmatchesandshows.com/category/ligue-1/' , 10011 , 'http://a1.mzstatic.com/us/r30/Purple5/v4/37/c7/44/37c744ae-5824-42b7-6ce0-5f471f52baab/icon180x180.jpeg' , ii11iIi1I + 'fanart.jpg' , '' )
 O00Oo000ooO0 ( '[COLORgreen]Copa America 2015[/COLOR]' , 'http://www.fullmatchesandshows.com/copa-america-2015/' , 10011 , 'https://pbs.twimg.com/profile_images/521966985907691520/Nq9OAPIo_400x400.png' , ii11iIi1I + 'fanart.jpg' , '' )
 O00Oo000ooO0 ( '[COLORgreen]CONCACAF[/COLOR]' , 'http://www.fullmatchesandshows.com/category/concacaf/' , 10011 , 'http://a3.mzstatic.com/us/r30/Purple3/v4/40/26/14/4026147c-7022-4ca3-504e-e78950cc3f1c/icon175x175.png' , ii11iIi1I + 'fanart.jpg' , '' )
 O00Oo000ooO0 ( '[COLORgreen]Women World Cup[/COLOR]' , 'http://www.fullmatchesandshows.com/category/women-world-cup/' , 10011 , 'https://upload.wikimedia.org/wikipedia/en/thumb/7/76/2015_FIFA_Women\'s_World_Cup_logo.svg/967px-2015_FIFA_Women\'s_World_Cup_logo.svg.png' , ii11iIi1I + 'fanart.jpg' , '' )
 if 47 - 47: OoooooooOO % I1IiI
def OO0Oo ( url ) :
 III1IiiI = iIi1 ( url )
 IIIII11I1IiI = re . compile ( 'itemprop="image" class="entry-thumb" src="(.+?)".+?<h3 itemprop="name" class="entry-title td-module-title"><a itemprop="url" href="(.+?)" rel="bookmark" title=".+?">(.+?)</a></h3>' , re . DOTALL ) . findall ( III1IiiI )
 for OO0O000 , url , I1Ii in IIIII11I1IiI :
  IIiiiiiIiIIi = I1Ii . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' )
  I11I1IIiiII1 ( '[COLORgreen]' + IIiiiiiIiIIi + '[/COLOR]' , url , 10013 , OO0O000 )
  if 26 - 26: OOooOOo
def IiIioO0Oo00oo ( url ) :
 III1IiiI = iIi1 ( url )
 IIIII11I1IiI = re . compile ( '<script data-config="(.+?)" data-height' ) . findall ( III1IiiI )
 for I1iiii1I in IIIII11I1IiI :
  OoOoooO000OO = ( I1iiii1I ) . replace ( '/v2' , '' ) . replace ( 'zeus.json' , 'video-sd.mp4?hosting_id=21772' ) . replace ( 'config.playwire.com' , 'cdn.video.playwire.com' )
  Oo0oOooOoOo ( 'http:' + OoOoooO000OO )
  if 62 - 62: Oo000 + Oo % iIii1I11I1II1 / iIii1I11I1II1 . II11i1iIiII1 . Ooo0OO0
  if 21 - 21: Ooo00oOo00o - i1I111ii1II1i - OOOo0 / I1IiI
def ii1oOoO0ooO0000 ( url ) :
 i1I1i1 = O0OoooO0 ( url )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)" title="([^"]*)"><img itemprop="image" content="([^"]*)"' , re . DOTALL ) . findall ( i1I1i1 )
 IIOOO0O00O0OOOO = re . compile ( "<a rel='next' href=([^=]*)=" , re . DOTALL ) . findall ( i1I1i1 )
 for url , I1Ii , OO0O000 in IIIII11I1IiI :
  I11I1IIiiII1 ( I1Ii , url , 8046 , OO0O000 )
 for url in IIOOO0O00O0OOOO :
  iII11I1Ii1 ( 'NEXT PAGE' , ( url ) . replace ( ' class' , '' ) , 8045 , ii11iIi1I + 'Next.png' )
def OOOOO ( url ) :
 i1I1i1 = O0OoooO0 ( url )
 IIIII11I1IiI = re . compile ( "__filename='([^']*)',.+?__fullimage='([^']*)',.+?__title='([^']*)'," , re . DOTALL ) . findall ( i1I1i1 )
 for url , OO0O000 , I1Ii in IIIII11I1IiI :
  Oo0oOooOoOo ( 'http://bitcast-b.bitgravity.com/ndtvod/23372/ndtv/' + url )
  if 68 - 68: iI + Ooo00oOo00o - O0 / Ooo00oOo00o * I1IiI
def I1iiiI ( url ) :
 i1I1i1 = O0OoooO0 ( url )
 IIIII11I1IiI = re . compile ( "src='http://www.youtube.com/embed/(.+?)?version=3&#038;rel=1&#038;fs=1&#038;autohide=2&#038;showsearch=0&#038;showinfo=1&#038;iv_load_policy=1&#038;wmode=transparent' frameborder='0' allowfullscreen='true'></iframe>" ) . findall ( i1I1i1 )
 for url in IIIII11I1IiI :
  yt . PlayVideo ( url )
  if 24 - 24: OOOo0 * OOO0OOO00oo
def Oo0 ( ) :
 i1I1i1 = O0OoooO0 ( i1111 ( 'aHR0cDovL3RvcGRvY3VtZW50YXJ5ZmlsbXMuY29tLw==' ) )
 IIIII11I1IiI = re . compile ( '<a href="(.+?)" >(.+?)</a></li><li>' ) . findall ( i1I1i1 )
 for OOOooo , I1Ii in IIIII11I1IiI :
  iII11I1Ii1 ( I1Ii , OOOooo , 8041 , ii11iIi1I + 'documentary.png' )
def O0000Oo00o ( url ) :
 i1I1i1 = O0OoooO0 ( url )
 IIIII11I1IiI = re . compile ( '<h2><a href="(.+?)" title="(.+?)">.+?</a></h2>.+?src="(.+?)"' , re . DOTALL ) . findall ( i1I1i1 )
 IIOOO0O00O0OOOO = re . compile ( 'class="inactive">.+?</a><a href="(.+?)">Next</a></div>' , re . DOTALL ) . findall ( i1I1i1 )
 for url , I1Ii , OO0O000 in IIIII11I1IiI :
  iII11I1Ii1 ( ( I1Ii ) . replace ( '&#039;s' , '' ) , url , 8042 , OO0O000 )
 for url in IIOOO0O00O0OOOO :
  iII11I1Ii1 ( 'NEXT PAGE' , url , 8041 , ii11iIi1I + 'Next.png' )
  if 20 - 20: Ooo00oOo00o . OOOo0 * i11iIiiIii / i11iIiiIii
  if 89 - 89: OoOo00o . i11iIiiIii * O0
def Iiii1 ( url ) :
 i1I1i1 = O0OoooO0 ( url )
 IIIII11I1IiI = re . compile ( '<meta itemprop="name" content="(.+?)".+?<meta itemprop="thumbnailUrl" content="(.+?)".+?<meta itemprop="embedUrl" content="(.+?)".+?<meta itemprop="description" content="(.+?)" />' , re . DOTALL ) . findall ( i1I1i1 )
 IIOOO0O00O0OOOO = re . compile ( '<div class="video new-video"><iframe width="766" height="431" src="(.+?)&amp;iv_load_policy=3&amp;showinfo=0&amp;autohide=1"' , re . DOTALL ) . findall ( i1I1i1 )
 for I1Ii , OO0O000 , url , iiiii1ii1 in IIIII11I1IiI :
  I11I1IIiiII1 ( ( I1Ii ) . replace ( '&#039;s' , '' ) , url . replace ( 'https://www.youtube.com/embed/' , '' ) , 8043 , OO0O000 )
 for url in IIOOO0O00O0OOOO :
  iI111II1ii ( ( url ) . replace ( '//' , 'http://' ) )
  if 62 - 62: OoOo00o * iIii1I11I1II1 . Ooo0OO0 - OoooooooOO * OoOoOO00
def iI111II1ii ( url ) :
 i1I1i1 = O0OoooO0 ( url )
 IIIII11I1IiI = re . compile ( '<link rel="canonical" href="(.+?)">  <link rel="stylesheet"' ) . findall ( i1I1i1 )
 for url in IIIII11I1IiI :
  I11I1IIiiII1 ( 'PLAY' , ( url ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , ii11iIi1I + 'documentary.png' )
  if 45 - 45: O0 % OOOo0 - OoOo00o . Ooo00oOo00o
def I1II ( ) :
 III1IiiI = O0OoooO0 ( 'http://www.stream2watch.co/live-tv' )
 IIIII11I1IiI = re . compile ( '<a href="(.+?)">.+?<img src="(.+?)" alt=".+?"/>.+?<span class="country_name">(.+?)<br />(.+?)</span>' , re . DOTALL ) . findall ( III1IiiI )
 for OOOooo , OO0O000 , I1Ii , iIIi1Ii1III in IIIII11I1IiI :
  iII11I1Ii1 ( ( I1Ii + '[COLORgreen]' + iIIi1Ii1III + '[/COLOR]' ) , OOOooo , 8086 , OO0O000 )
  if 86 - 86: i11iIiiIii + i11iIiiIii . OoO0O0 % OOOo0 . II11i1iIiII1
def iII1iI1IIiI ( url ) :
 III1IiiI = O0OoooO0 ( url )
 IIIII11I1IiI = re . compile ( '<a class="front_channel_href" href="(.+?)" title=".+?">.+?<img class="front_channel_thumb" src="(.+?)" alt=".+?"/>.+?<span class="front_channel_name">(.+?)</span>' , re . DOTALL ) . findall ( III1IiiI )
 for url , OO0O000 , I1Ii in IIIII11I1IiI :
  iII11I1Ii1 ( '[COLORgreen]' + I1Ii + '[/COLOR]' , url , 8087 , OO0O000 )
  if 69 - 69: iI / i11iIiiIii * OOooOOo / OoO0O0
def oO0O ( url ) :
 III1IiiI = iIi1 ( url )
 IIIII11I1IiI = re . compile ( 'a id="code_.+?data-f-href="(.+?)" data-code-embed="">(.+?)</a>' , re . DOTALL ) . findall ( III1IiiI )
 for url , I1Ii in IIIII11I1IiI :
  OOoooO00o0o ( url , I1Ii )
  if 10 - 10: i1I111ii1II1i - i11iIiiIii . ii11ii1ii % i1IIi
def OOoooO00o0o ( url , name ) :
 III1IiiI = iIi1 ( url )
 IIIII11I1IiI = re . compile ( "playStream\('.+?', '(.+?)'\);" , re . DOTALL ) . findall ( III1IiiI )
 for url in IIIII11I1IiI :
  print url
  I11I1IIiiII1 ( '[COLORgreen]' + name + '[/COLOR]' , url , 222 , '' )
  if 78 - 78: iIii1I11I1II1 * Oo . Oo - Oo000 . iIii1I11I1II1
def I111I1I ( ) :
 i1I1i1 = O0OoooO0 ( i1111 ( 'aHR0cDovL3d3dy5zb2xpZS5vcmcvYWxpYnJhcnkvaW5kZXguaHRtbA==' ) )
 IIIII11I1IiI = re . compile ( '<td align="center" valign="top">.+?<a href="(.+?)">.+?<img src="(.+?)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( i1I1i1 )
 for OOOooo , OO0O000 , I1Ii in IIIII11I1IiI :
  iII11I1Ii1 ( ( '[COLORgreen]' + I1Ii + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + OOOooo , 3002 , 'http://www.solie.org/alibrary/' + OO0O000 )
def Oo0000 ( url ) :
 i1I1i1 = O0OoooO0 ( url )
 IIIII11I1IiI = re . compile ( '<td align="center" valign="top">.+?<a href="(.+?)">.+?<img src="(.+?)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( i1I1i1 )
 for url , OO0O000 , I1Ii in IIIII11I1IiI :
  iII11I1Ii1 ( ( '[COLORgreen]' + I1Ii + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3003 , 'http://www.solie.org/alibrary/' + OO0O000 )
def oO0Oo ( url ) :
 i1I1i1 = O0OoooO0 ( url )
 IIIII11I1IiI = re . compile ( '<br><a href="([^"]*)">(.+?)</a>' ) . findall ( i1I1i1 )
 OooOOOOOo = re . compile ( 'href="([^"]*)">Season(.+?)</a>' ) . findall ( i1I1i1 )
 next = re . compile ( '<a href="([^"]*)">Episodes</a>' ) . findall ( i1I1i1 )
 IIOOO0O00O0OOOO = re . compile ( '<td align="center" valign="top">.+?<a href="(.+?)">.+?<img src="(.+?)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( i1I1i1 )
 for url , I1Ii in IIIII11I1IiI :
  I11I1IIiiII1 ( ( '[COLORgreen]' + I1Ii + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3004 , ii11iIi1I + 'classicmovies.png' )
 for url , I1Ii in OooOOOOOo :
  iII11I1Ii1 ( '[COLORgreen]Season- ' + I1Ii + '[/COLOR]' , 'http://www.solie.org/alibrary/' + url , 3003 , ii11iIi1I + 'classicmovies.png' )
 for url in next :
  iII11I1Ii1 ( '[COLORgreen]NEXT[/COLOR]' , 'http://www.solie.org/alibrary/' + url , 3003 , ii11iIi1I + 'Next.png' )
 for url , OO0O000 , I1Ii in IIOOO0O00O0OOOO :
  iII11I1Ii1 ( ( '[COLORgreen]' + I1Ii + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3003 , 'http://www.solie.org/alibrary/' + OO0O000 )
def i1I11ii ( url ) :
 i1I1i1 = O0OoooO0 ( url )
 IIIII11I1IiI = re . compile ( '<iframe.+?src="([^"]*)"' ) . findall ( i1I1i1 )
 for url in IIIII11I1IiI :
  o0ooO00O0O ( url )
def o0ooO00O0O ( url ) :
 i1I1i1 = O0OoooO0 ( url )
 IIIII11I1IiI = re . compile ( '<meta property="og:video" content="([^"]*)"/>' ) . findall ( i1I1i1 )
 for url in IIIII11I1IiI :
  Oo0oOooOoOo ( url )
  if 41 - 41: ii11ii1ii
def i1iI1i ( ) :
 i1I1i1 = O0OoooO0 ( i1111 ( 'aHR0cDovL3JldHJvdmlzaW9uLnR2L2FsbC8=' ) )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)"><h2><font color=".+?"><h2>(.+?)</font></h2></a>' ) . findall ( i1I1i1 )
 for OOOooo , I1Ii in IIIII11I1IiI :
  I11I1IIiiII1 ( ( '[COLORgreen]' + I1Ii + '[/COLOR]' ) . replace ( '&#8211;' , ':' ) , OOOooo , 8061 , ii11iIi1I + 'classicmovies.png' )
def o0o0OoO0OOO0 ( url ) :
 i1I1i1 = O0OoooO0 ( url )
 IIIII11I1IiI = re . compile ( "v.src = '([^']*)';" ) . findall ( i1I1i1 )
 for url in IIIII11I1IiI :
  Oo0oOooOoOo ( url )
  if 79 - 79: OOO0OOO00oo % OOooOOo % I1IiI
def ii1IIiII111I ( ) :
 i1I1i1 = O0OoooO0 ( i1111 ( 'aHR0cDovL3JldHJvdmlzaW9uLnR2L2NsYXNzaWMtdHYv' ) )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)"><h2><font color=".+?"><h2>(.+?)</font></h2></a>' ) . findall ( i1I1i1 )
 for OOOooo , I1Ii in IIIII11I1IiI :
  I11I1IIiiII1 ( ( '[COLORgreen]' + I1Ii + '[/COLOR]' ) . replace ( '&#8211;' , ':' ) , OOOooo , 8061 , ii11iIi1I + 'classictv.png' )
def O00OoOoO ( url ) :
 i1I1i1 = O0OoooO0 ( url )
 IIIII11I1IiI = re . compile ( "v.src = '([^']*)';" ) . findall ( i1I1i1 )
 for url in IIIII11I1IiI :
  Oo0oOooOoOo ( url )
  if 58 - 58: ii11ii1ii
def ii1ii1i11I1I ( ) :
 III1IiiI = iIi1 ( i1111 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vbTN1c3RyZWFtcw==' ) )
 IIIII11I1IiI = re . compile ( '<li><a href="(.+?)"> (.+?).m3u</a></li>' ) . findall ( III1IiiI )
 for OOOooo , I1Ii in IIIII11I1IiI :
  iII11I1Ii1 ( ( '[COLORgreen]' + I1Ii + '[/COLOR]' ) . replace ( '-' , ' ' ) . replace ( '_' , ' ' ) , ( i1111 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vbTN1c3RyZWFtcy8=' ) ) + OOOooo , 8071 , ii11iIi1I + 'streams.png' )
def iiII1iiiiiii ( url ) :
 III1IiiI = O0OoooO0 ( url )
 IIIII11I1IiI = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( III1IiiI )
 for I1Ii , url in IIIII11I1IiI :
  I11I1IIiiII1 ( ( '[COLORgreen]' + I1Ii + '[/COLOR]' ) . replace ( '_' , ' ' ) , ( url ) . strip ( ) , 404 , ii11iIi1I + 'streams.png' )
def iiIiii ( url ) :
 III1IiiI = O0OoooO0 ( url )
 IIIII11I1IiI = re . compile ( 'EXTINF:(.+?),(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( III1IiiI )
 for OO0O000 , I1Ii , url in IIIII11I1IiI :
  url = ( ( i1111 ( 'aHR0cDovL3BpZXN1c3R2Lm5ldDo4MDAwL2xpdmUv' ) ) + oO0o0o0ooO0oO + '/' + oo0o0O00 + url ) . strip ( )
  I11I1IIiiII1 ( ( '[COLORgreen]' + I1Ii + '[/COLOR]' ) . replace ( '_' , ' ' ) , url , 10012 , OO0O000 )
  if 39 - 39: OOOo0 + Oo
def o0OOooO ( ) :
 oOo00oOOOOO ( 'Best Videos' , 'http://www.xvideos.com/best' , 10105 , ii11iIi1I + 'JIZBOX.png' , '' , '' )
 oOo00oOOOOO ( 'Genres' , 'http://www.xvideos.com' , 10106 , ii11iIi1I + 'JIZBOX.png' , '' , '' )
 oOo00oOOOOO ( 'Recently Uploaded' , 'http://xvideos.com' , 10105 , ii11iIi1I + 'JIZBOX.png' , '' , '' )
 oOo00oOOOOO ( 'Tags' , 'http://www.xvideos.com/tags' , 10103 , ii11iIi1I + 'JIZBOX.png' , '' , '' )
 oOo00oOOOOO ( 'Search' , '' , 10107 , ii11iIi1I + 'JIZBOX.png' , '' , '' , )
 if 41 - 41: i1IIi + OoOoOO00 * II11i1iIiII1
def o0oOoOo0 ( url ) :
 III1IiiI = iIi1 ( url )
 III1IiI1i1i = re . compile ( '<li><a class=".+?".+?href="(.+?)">Next</a></li>' ) . findall ( III1IiiI )
 for url in III1IiI1i1i :
  oOo00oOOOOO ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10103 , ii11iIi1I + 'JIZBOX.png' , '' , '' )
 IIIII11I1IiI = re . compile ( '<li><a href="(.+?)"><b>(.+?)</b><span class="navbadge default"(.+?)</span>' ) . findall ( III1IiiI )
 for url , I1Ii , ooO0O0O0ooOOO in IIIII11I1IiI :
  oOo00oOOOOO ( I1Ii + ' - No of Videos : ' + ( ooO0O0O0ooOOO ) . replace ( '>' , '' ) , 'http://www.xvideos.com' + url , 10105 , ii11iIi1I + 'JIZBOX.png' , '' , '' )
  if 94 - 94: OoOo00o - Oo + OOO0OOO00oo
def O0oooOoO ( url ) :
 III1IiiI = iIi1 ( url )
 III1IiI1i1i = re . compile ( 'href="([^"]*)">Next</a></li>' ) . findall ( III1IiiI )
 for url in III1IiI1i1i :
  oOo00oOOOOO ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10104 , ii11iIi1I + 'Next.png' , '' , '' )
 IIIII11I1IiI = re . compile ( ':"([^"]*)".+?;</script></a></div></div><p class="profile-name"><a href="([^"]*)">(.+?)</a></p><p class="profile-counts">\n(.+?)\n' , re . DOTALL ) . findall ( III1IiiI )
 for OO0O000 , url , I1Ii , O0Oo0iIIIi1IiI11I1 in IIIII11I1IiI :
  oOo00oOOOOO ( I1Ii + '--' + O0Oo0iIIIi1IiI11I1 , 'http://www.xvideos.com' + url + '#_tabVideos,videos-best' , 10105 , ( OO0O000 ) . replace ( 'http:\/\/' , 'http://' ) , '' , '' )
  if 71 - 71: i1I111ii1II1i - O0 - OoOo00o . Oo000 % Oo
  if 82 - 82: OoooooooOO + Oo000 % I1IiI . Ooo00oOo00o * i1IIi
def iIiIi1iIIi11i ( url ) :
 III1IiiI = iIi1 ( url )
 IIIII11I1IiI = re . compile ( '<div class="thumb-inside"><script>.+?<img src="(.+?)".+?<a href="(.+?)" title=".+?">(.+?)</a></p>.+?uration">(.+?)</span>.+?Porn quality:(.+?)</span>' , re . DOTALL ) . findall ( III1IiiI )
 for OO0O000 , url , I1Ii , OooO0OO , I1IIII in IIIII11I1IiI :
  ii1ii11IIIiiI ( I1Ii + ' - Porn Quality : ' + I1IIII + ' - ' + OooO0OO , 'http://www.xvideos.com' + url , 10108 , OO0O000 , OO0O000 , I1IIII + ' - ' + OooO0OO )
 OooooOoO = re . compile ( '<li><a href="([^"]*)" class="no-page">Next</a></li></ul></div>' ) . findall ( III1IiiI )
 for url in OooooOoO :
  oOo00oOOOOO ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10105 , ii11iIi1I + 'Next.png' , '' , '' )
  if 79 - 79: II11i1iIiII1 % Oo000
def oO0O0o0O ( url ) :
 III1IiiI = iIi1 ( url )
 IIiII111iiI1I = re . compile ( '<div class="main-categories">(.+?)</div>' , re . DOTALL ) . findall ( III1IiiI )
 III1IiI1i1i = re . compile ( '<li><a class=".+?".+?href="(.+?)">Next</a></li>' ) . findall ( III1IiiI )
 for url in III1IiI1i1i :
  oOo00oOOOOO ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10106 , ii11iIi1I + 'Next.png' , '' , '' )
 IIIII11I1IiI = re . compile ( '<li><a href="(.+?)" class="btn btn-default">(.+?)</a>' ) . findall ( str ( IIiII111iiI1I ) )
 for url , I1Ii in IIIII11I1IiI :
  oOo00oOOOOO ( I1Ii , 'http://www.xvideos.com' + url , 10105 , ii11iIi1I + 'JIZBOX.png' , '' , '' )
  if 100 - 100: I1IiI % Oo
  if 76 - 76: OoOoOO00 / Ooo00oOo00o + OoooooooOO . ii11ii1ii . iI . II11i1iIiII1
def iiiIiIIIiiiIiI1 ( ) :
 i1111I1I = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 O0OOoooo0 = ( i1111I1I ) . replace ( ' ' , '+' ) . replace ( '&amp;' , '&' )
 oOOoo00O00o = O0OOoooo0 . lower ( )
 iIiIi1IiIi1iI = 'http://www.xvideos.com/?k=' + oOOoo00O00o
 print iIiIi1IiIi1iI + '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'
 III1IiiI = iIi1 ( iIiIi1IiIi1iI )
 IIIII11I1IiI = re . compile ( '<div class="thumb-inside"><script>.+?<img src="(.+?)".+?<a href="(.+?)" title=".+?">(.+?)</a></p>.+?uration">(.+?)</span>.+?Porn quality:(.+?)</span>' , re . DOTALL ) . findall ( III1IiiI )
 for OO0O000 , OOOooo , I1Ii , OooO0OO , I1IIII in IIIII11I1IiI :
  ii1ii11IIIiiI ( I1Ii + ' - Porn Quality : ' + I1IIII + ' - ' + OooO0OO , 'http://www.xvideos.com' + OOOooo , 10108 , OO0O000 , OO0O000 , I1IIII + ' - ' + OooO0OO )
 OooooOoO = re . compile ( '<li><a href="([^"]*)" class="no-page">Next</a></li></ul></div>' ) . findall ( III1IiiI )
 for OOOooo in OooooOoO :
  oOo00oOOOOO ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + OOOooo , 10105 , ii11iIi1I + 'Next.png' , '' , '' )
  if 66 - 66: Oo
def OO00OoooO ( url ) :
 III1IiiI = iIi1 ( url )
 IIIII11I1IiI = re . compile ( 'flv_url=(.+?)\;' ) . findall ( III1IiiI )
 for url in IIIII11I1IiI :
  IIIi = ( url ) . replace ( '%3A' , ':' ) . replace ( '%2F' , '/' ) . replace ( '%3F' , '?' ) . replace ( '%3D' , '=' ) . replace ( '%26' , '&' ) . replace ( '&amp' , '' )
  Ii1iiI1 ( IIIi )
  if 76 - 76: i1I111ii1II1i * iIii1I11I1II1
def Ii1iiI1 ( url ) :
 iiiiI1iiiIi = xbmc . Player ( iiI1iI ( ) )
 import urlresolver
 try : iiiiI1iiiIi . play ( url )
 except : pass
 if 84 - 84: OoooooooOO + OoO0O0 / OOOo0 % Oo000 % ii11ii1ii * OOOo0
 if 58 - 58: Ooo00oOo00o - I1IiI . i11iIiiIii % i11iIiiIii / i1IIi / OOO0OOO00oo
def Ii1ii1IiiiiiI ( ) :
 III1IiiI = iIi1 ( i1111 ( 'aHR0cDovL3d3dy5nb2Zpc2hpbmcuY28udWsvQW5nbGluZy1UaW1lcy9TZWN0aW9uL1ZpZGVvcy8=' ) )
 IIIII11I1IiI = re . compile ( 'class="item.+?"><a href="(.+?)">(.+?)</a></li>' ) . findall ( III1IiiI )
 for OOOooo , I1Ii in IIIII11I1IiI :
  iII11I1Ii1 ( '[COLORgreen]' + I1Ii + '[/COLOR]' , ( 'http://www.gofishing.co.uk' + OOOooo ) . replace ( 'http://www.gofishing.co.ukhttp://www.gofishing.co.uk' , 'http://www.gofishing.co.uk' ) , 8091 , ii11iIi1I + 'gofish.png' )
def ooIIIii11i1I ( url ) :
 III1IiiI = O0OoooO0 ( url )
 IIIII11I1IiI = re . compile ( '<h2><a id=.+?href="([^"]*)">(.+?)</a></h2>' , re . DOTALL ) . findall ( III1IiiI )
 IIOOO0O00O0OOOO = re . compile ( '<h3><a href="([^"]*)" id=.+?>(.+?)</a> </h3>.+?<img src="([^"]*)"' , re . DOTALL ) . findall ( III1IiiI )
 next = re . compile ( 'href="([^"]*)">next</a>&gt;</li>' , re . DOTALL ) . findall ( III1IiiI )
 for url , I1Ii in IIIII11I1IiI :
  I11I1IIiiII1 ( '[COLORgreen]' + I1Ii + '[/COLOR]' , 'http://www.gofishing.co.uk/' + url , 8092 , ii11iIi1I + 'gofish.png' )
 for url , I1Ii , OO0O000 in IIOOO0O00O0OOOO :
  I11I1IIiiII1 ( '[COLORgreen]' + I1Ii + '[/COLOR]' , 'http://www.gofishing.co.uk/' + url , 8092 , 'http://www.gofishing.co.uk/' + OO0O000 )
 for url in next :
  iII11I1Ii1 ( '[COLORgreen]NEXT[/COLOR]' , url . replace ( ' ' , '+' ) , 8091 , ii11iIi1I + 'Next.png' )
def ooo0O00000oo0 ( url ) :
 III1IiiI = O0OoooO0 ( url )
 IIIII11I1IiI = re . compile ( 'src="https://www.youtube.com/embed/(.+?)"' ) . findall ( III1IiiI )
 for url in IIIII11I1IiI :
  yt . PlayVideo ( url )
  if 80 - 80: Oo + ii11ii1ii
def oOIii11111iiI ( url ) :
 o0OOOOoO = urllib2 . Request ( url )
 o0OOOOoO . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
 OoO0Ooo = ''
 iI1I1i11iIIii = ''
 try :
  OoO0Ooo = urllib2 . urlopen ( o0OOOOoO )
  iI1I1i11iIIii = OoO0Ooo . read ( )
  OoO0Ooo . close ( )
 except : pass
 if iI1I1i11iIIii != '' :
  return iI1I1i11iIIii
 else :
  iI1I1i11iIIii = 'Failed'
  return iI1I1i11iIIii
  if 21 - 21: OOOo0 + ii11ii1ii * Oo * iIii1I11I1II1 - Ooo00oOo00o . Oo
  if 59 - 59: Ooo00oOo00o - Ooo00oOo00o + OoOo00o
def iiII ( ) :
 II11iiii = ( i1111 ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 i1111I1I = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oOOoo00O00o = i1111I1I . lower ( )
 OOOooo = ( i1111 ( 'aHR0cDovL2RsNC5tb3ZpZWZhcnNpLmNvbS9maWxtLzIwMTUtNy8=' ) )
 ooI1111i = ( i1111 ( 'aHR0cDovL2RsLmF2YWRsLmNvbS9OZXcvTW92aWUv' ) )
 o00O0O = ( i1111 ( 'aHR0cDovLzIxNy4yMTkuMTQzLjEwOC8xMzI3Lw==' ) )
 i11i1 = ( i1111 ( 'aHR0cDovLzE3OC4xNjIuMjE0LjIzMi92b2QvbW92aWVzL2VuZ2xpc2gv' ) )
 O00oo00OOOO = ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvbW92L2FsbC5waHA=' ) )
 IiIi1II111I = ( i1111 ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 o00o = ( i1111 ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL3NlYXJjaC8/cT0=' ) ) + i1111I1I
 IIi1i1 = ( i1111 ( 'aHR0cDovL3JlZGVtcHRpb25idWlsZC4xNm1iLmNvbS9SZWRlbXB0aW9uL21vdmllcy9hbGxtb3ZpZS5waHA=' ) )
 o0O0Ooo = ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9UaGVfUmVhcGVyL2FsbG1vdmllcy5waHA=' ) )
 O0oO00oOOooO = ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC9tb3ZmdWxsLnBocA==' ) )
 IiIIii1iiI = ( i1111 ( 'aHR0cDovLzUuMTM1LjIwNy45Ni9TY3JhcGVzL1NILnBocA==' ) )
 if 7 - 7: OOooOOo
 III1IiiI = oOIii11111iiI ( OOOooo )
 II11IiIi11 = oOIii11111iiI ( ooI1111i )
 IiiIIi = oOIii11111iiI ( o00O0O )
 OoOo0OO0oooo = oOIii11111iiI ( i11i1 )
 I11II1i1 = oOIii11111iiI ( O00oo00OOOO )
 IiI1ii11I1 = oOIii11111iiI ( o00o )
 I1i1iI = oOIii11111iiI ( IIi1i1 )
 I1iI1I1ii1 = oOIii11111iiI ( o0O0Ooo )
 iIIi1o0Ooo0o0Oo = oOIii11111iiI ( O0oO00oOOooO )
 oo00ooooOOo00 = oOIii11111iiI ( IiIIii1iiI )
 Oo0oO0ooo = xbmcgui . DialogProgress ( )
 if 16 - 16: i11iIiiIii / i1IIi % Oo000
 if 84 - 84: iI - Oo * O0 / i1I111ii1II1i . i1I111ii1II1i
 if III1IiiI != 'Failed' :
  IIIII11I1IiI = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( III1IiiI )
  for ooO0 , I1Ii in IIIII11I1IiI :
   if i1111I1I in I1Ii . lower ( ) :
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    I11I1IIiiII1 ( ( '[COLORgreen]' + I1Ii + '- source 1[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( OOOooo + ooO0 ) , 222 , '' )
    Oo0oO0ooo . update ( 0 , "" , "Getting Source 1 Links" )
 if II11IiIi11 != 'Failed' :
  IIOOO0O00O0OOOO = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( II11IiIi11 )
  for ooO0 , I1Ii in IIOOO0O00O0OOOO :
   if i1111I1I in I1Ii . lower ( ) :
    I11I1IIiiII1 ( ( '[COLORgreen]' + I1Ii + '- source 2[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( ooI1111i + ooO0 ) , 222 , '' )
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 9 , "" , "Getting Source 2 Links" )
 if IiiIIi != 'Failed' :
  iI1I11iIIi1 = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( IiiIIi )
  for ooO0 , I1Ii in iI1I11iIIi1 :
   if i1111I1I in I1Ii . lower ( ) :
    iII11I1Ii1 ( ( '[COLORgreen]' + I1Ii + '- source 3[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( o00O0O + ooO0 ) , 1006 , '' )
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 18 , "" , "Getting Source 3 Links" )
 if OoOo0OO0oooo != 'Failed' :
  ii111iiIii = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( OoOo0OO0oooo )
  for ooO0 , I1Ii in ii111iiIii :
   if i1111I1I in I1Ii . lower ( ) :
    I11I1IIiiII1 ( ( '[COLORgreen]' + I1Ii + '- source 4[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( i11i1 + ooO0 ) , 222 , '' )
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 27 , "" , "Getting Source 4 Links" )
 if I11II1i1 != 'Failed' :
  oO0oiIiI = [ ]
  iIIiiiI1iI1 = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( I11II1i1 )
  for OOOooo , ooo0O0o00O , oo0o , oOO0o0oo0 , I1Ii in iIIiiiI1iI1 :
   if i1111I1I in I1Ii . lower ( ) :
    if I1Ii in oO0oiIiI :
     pass
    else :
     O00Oo000ooO0 ( ( '[COLORgreen]' + I1Ii + '- source Scooby[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( 'Ganool' , '' ) . replace ( 'ShAaNiG' , '' ) . replace ( 'YIFY' , '' ) . replace ( '[[ Max-Movie.In ]]' , '' ) . replace ( '.mkv' , '' ) . replace ( '.mp4' , '' ) . replace ( '.' , ' ' ) , OOOooo , 1016 , ooo0O0o00O , oOO0o0oo0 , oo0o )
     oO0oiIiI . append ( I1Ii )
     Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     Oo0oO0ooo . update ( 36 , "" , "Getting Scooby Links" )
     ii111 ( 'tvshows' , 'Media Info 3' )
 if IiI1ii11I1 != 'Failed' :
  oO00000oO0o0O = re . compile ( 'href="(.+?)".+?src="(.+?)" alt="Image of (.+?)"' , re . DOTALL ) . findall ( IiI1ii11I1 )
  for OOOooo , OO0O000 , I1Ii in oO00000oO0o0O :
   if i1111I1I in I1Ii . lower ( ) :
    iII11I1Ii1 ( ( '[COLORgreen]' + I1Ii + '- source Snag[/COLOR]' ) . replace ( '&#x27;' , '' ) , 'http://www.snagfilms.com' + OOOooo , 7067 , OO0O000 )
    Oo0oO0ooo . update ( 45 , "" , "Getting Snag Links" )
    if 34 - 34: Oo - i1IIi - II11i1iIiII1 - i1IIi
    ii111 ( 'tvshows' , 'Media Info 3' )
 if I1i1iI != 'Failed' :
  O00Oo = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( I1i1iI )
  for OOOooo , ooo0O0o00O , oo0o , oOO0o0oo0 , I1Ii in O00Oo :
   if i1111I1I in I1Ii . lower ( ) :
    ii1ii11IIIiiI ( ( '[COLORgreen]' + I1Ii + '- source Redemption[/COLOR]' ) , OOOooo , 222 , ooo0O0o00O , oOO0o0oo0 , oo0o )
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 53 , "" , "Getting Redemption Links" )
    if 38 - 38: i1IIi . i11iIiiIii
    ii111 ( 'tvshows' , 'Media Info 3' )
 if I1iI1I1ii1 != 'Failed' :
  O0ooO0O0Ooo0o = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( I1iI1I1ii1 )
  for OOOooo , ooo0O0o00O , oo0o , oOO0o0oo0 , I1Ii in O0ooO0O0Ooo0o :
   if i1111I1I in I1Ii . lower ( ) :
    ii1ii11IIIiiI ( ( '[COLORgreen]' + I1Ii + '- source Reaper[/COLOR]' ) , OOOooo , 222 , ooo0O0o00O , oOO0o0oo0 , oo0o )
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 61 , "" , "Getting Reaper Links" )
    if 25 - 25: Oo000 * Oo000 / OOO0OOO00oo % Oo
    ii111 ( 'tvshows' , 'Media Info 3' )
 if iIIi1o0Ooo0o0Oo != 'Failed' :
  i1iiiiI11ii = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( iIIi1o0Ooo0o0Oo )
  for OOOooo , ooo0O0o00O , oo0o , oOO0o0oo0 , I1Ii in i1iiiiI11ii :
   if i1111I1I in I1Ii . lower ( ) :
    ii1ii11IIIiiI ( ( '[COLORgreen]' + I1Ii + '- source Herovision[/COLOR]' ) , OOOooo , 222 , ooo0O0o00O , oOO0o0oo0 , oo0o )
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 70 , "" , "Getting Herovision Links" )
    if 73 - 73: i1IIi % OoooooooOO
    ii111 ( 'tvshows' , 'Media Info 3' )
    if 25 - 25: OOO0OOO00oo + OoOoOO00
 if oo00ooooOOo00 != 'Failed' :
  oOoOO0000oO00 = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( oo00ooooOOo00 )
  for OOOooo , ooo0O0o00O , I1Ii in oOoOO0000oO00 :
   if i1111I1I in I1Ii . lower ( ) :
    iII11I1Ii1 ( ( '[COLORgreen]' + I1Ii + '- source Silent Hunter[/COLOR]' ) , OOOooo , 222 , ooo0O0o00O )
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 78 , "" , "Getting Silent Hunter Links" )
    if 93 - 93: iI . I1IiI / Oo + OOO0OOO00oo
    ii111 ( 'tvshows' , 'Media Info 3' )
 iiiiI1I = [ '480p' , '720p' , '1080p' , 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' ]
 if 93 - 93: Oo * OOO0OOO00oo + Ooo00oOo00o - OoO0O0 . ii11ii1ii + OoooooooOO
 for I1IIIIiii1i in iiiiI1I :
  o0IiiiI111I = ooooooO0oo + I1IIIIiii1i + II11iiii1Ii
  i1II11I11ii1 = iIi1 ( o0IiiiI111I )
  if i1II11I11ii1 != 'Failed' :
   OOoO0oO00o = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( i1II11I11ii1 )
   for OOOooo , ooo0O0o00O , oo0o , oOO0o0oo0 , I1Ii in OOoO0oO00o :
    if i1111I1I in I1Ii . lower ( ) :
     ii1ii11IIIiiI ( '[COLORgreen]' + I1Ii + ' - Source Pandoras[/COLOR]' , OOOooo , 222 , ooo0O0o00O , oOO0o0oo0 , oo0o )
     Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     Oo0oO0ooo . update ( 89 , "" , "Getting Pandoras Links" )
     if 78 - 78: Oo * OoO0O0 - OoooooooOO - Ooo00oOo00o
     ii111 ( 'tvshows' , 'Media Info 3' )
     if 83 - 83: II11i1iIiII1 / Oo000
 oO00 = [ '0-9/' , 'A/' , 'B/' , 'C/' , 'D/' , 'E/' , 'F/' , 'G/' , 'H/' , 'I/' , 'J/' , 'K/' , 'L/' , 'M/' , 'N/' , 'O/' , 'P/' , 'R/' , 'S/' , 'T/' , 'U/' , 'V/' , 'W/' , 'X/' , 'Y/' , 'Z/' ]
 if 39 - 39: Ooo0OO0 + iI
 if 9 - 9: OOOo0 % iI . Oo * OOOo0
 for I1IIIIiii1i in oO00 :
  o0IiiiI111I = II11iiii + I1IIIIiii1i
  OoO0oO0oo0O = oOIii11111iiI ( o0IiiiI111I )
  if I11II1i1 != 'Failed' :
   oooOOO0ooOoOOO = re . compile ( '<li><a href="(.+?)"> (.+?)</a></li>' ) . findall ( OoO0oO0oo0O )
   for ooO0 , I1Ii in oooOOO0ooOoOOO :
    if i1111I1I in I1Ii . lower ( ) :
     I11I1IIiiII1 ( ( '[COLORgreen]' + I1Ii + 'source 5[/COLOR]' ) . replace ( 'Ganool' , '' ) . replace ( 'ShAaNiG' , '' ) . replace ( 'YIFY' , '' ) . replace ( '[[ Max-Movie.In ]]' , '' ) . replace ( '.mkv' , '' ) . replace ( '.mp4' , '' ) . replace ( '.' , ' ' ) , ( II11iiii + I1IIIIiii1i + ooO0 ) , 222 , '' )
     Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     Oo0oO0ooo . update ( 100 , "" , "Getting Source 5 Links" )
     if 68 - 68: O0
     ii111 ( 'tvshows' , 'Media Info 3' )
     if 76 - 76: ii11ii1ii
     if 99 - 99: OOooOOo
def I11IIII1111II ( ) :
 if 6 - 6: iIii1I11I1II1 / Oo000 + iI
 i1111I1I = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oOOoo00O00o = i1111I1I . lower ( )
 o0O0Ooo = ( i1111 ( 'aHR0cDovL2Nvb2x0dnNlcmllcy5jb20vc2VhcmNoLnBocD90YWc9' ) ) + ( i1111I1I ) . replace ( ' ' , '+' )
 OOOooo = ( i1111 ( 'aHR0cDovL2RsLmZhcnNpbW92aWUubmV0L1NlcmlhbC8=' ) )
 ooI1111i = ( i1111 ( 'aHR0cDovL3N2Mi5kbC1wYXJzLmluLw==' ) )
 o00O0O = ( i1111 ( 'aHR0cDovL3R2LmRsLXBhcnMuaW4v' ) )
 i11i1 = ( i1111 ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9BbWVyaWNhbiUyMFNlcmlhbC8=' ) )
 O00oo00OOOO = ( i1111 ( 'aHR0cDovL2RpemlsYWIuY29tL2Fyc2l2P2xpbWl0PSZ0dXI9Jm9yZGVyYnk9JnVsa2U9Jm9yZGVyPSZ5aWw9JmRpemlfYWRpPQ==' ) ) + ( i1111I1I ) . replace ( ' ' , '+' )
 IiIi1II111I = ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvc2hvd3MvdHZhbGwucGhw' ) )
 o00o = ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9UaGVfUmVhcGVyL2FsbHR2LnBocA==' ) )
 IIi1i1 = ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC90dmZ1bGwucGhw' ) )
 if 89 - 89: OOO0OOO00oo
 I1iI1I1ii1 = oOIii11111iiI ( o0O0Ooo )
 III1IiiI = oOIii11111iiI ( OOOooo )
 II11IiIi11 = oOIii11111iiI ( ooI1111i )
 IiiIIi = oOIii11111iiI ( o00O0O )
 OoOo0OO0oooo = oOIii11111iiI ( i11i1 )
 I11II1i1 = cloudflare . source ( O00oo00OOOO )
 OoO0oO0oo0O = oOIii11111iiI ( IiIi1II111I )
 IiI1ii11I1 = oOIii11111iiI ( o00o )
 I1i1iI = oOIii11111iiI ( IIi1i1 )
 if 87 - 87: OoOo00o % Oo
 if I1i1iI != 'Failed' :
  O00Oo = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( I1i1iI )
  for OOOooo , ooo0O0o00O , oo0o , oOO0o0oo0 , I1Ii in O00Oo :
   if i1111I1I in I1Ii . lower ( ) :
    O00Oo000ooO0 ( ( '[COLORgreen]' + I1Ii + '- source HeroVision[/COLOR]' ) , OOOooo , 1016 , ooo0O0o00O , oOO0o0oo0 , oo0o )
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 10 , "" , "Getting Herovision Links" )
    if 62 - 62: Ooo00oOo00o + II11i1iIiII1 / OoOo00o * i11iIiiIii
    ii111 ( 'tvshows' , 'Media Info 3' )
    if 37 - 37: OoOo00o
 if IiI1ii11I1 != 'Failed' :
  oO00000oO0o0O = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( IiI1ii11I1 )
  for OOOooo , ooo0O0o00O , oo0o , oOO0o0oo0 , I1Ii in oO00000oO0o0O :
   if i1111I1I in I1Ii . lower ( ) :
    O00Oo000ooO0 ( ( '[COLORgreen]' + I1Ii + '- source Reaper[/COLOR]' ) , OOOooo , 1016 , ooo0O0o00O , oOO0o0oo0 , oo0o )
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 20 , "" , "Getting Reaper Links" )
    if 33 - 33: Ooo00oOo00o - O0 - Ooo00oOo00o
    ii111 ( 'tvshows' , 'Media Info 3' )
    if 94 - 94: Ooo0OO0 * iI * OoooooooOO / OOooOOo . Ooo0OO0 - OOooOOo
 if I1iI1I1ii1 != 'Failed' :
  O0ooO0O0Ooo0o = re . compile ( 'href="([^"]*)"><img src="([^"]*)" alt="([^"]*)"' ) . findall ( I1iI1I1ii1 )
  for OOOooo , OO0O000 , I1Ii in O0ooO0O0Ooo0o :
   if i1111I1I in I1Ii . lower ( ) :
    iII11I1Ii1 ( '[COLORgreen]' + I1Ii + ' CoolSeries[/COLOR]' , OOOooo , 7052 , OO0O000 )
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 30 , "" , "Getting CoolSeries Links" )
    if 13 - 13: Oo000 / Ooo0OO0 - Ooo00oOo00o / Oo000 . i1IIi
    ii111 ( 'tvshows' , 'Media Info 3' )
 if III1IiiI != 'Failed' :
  IIIII11I1IiI = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( III1IiiI )
  for I1Ii in IIIII11I1IiI :
   if i1111I1I in I1Ii . lower ( ) :
    iII11I1Ii1 ( '[COLORgreen]' + ( I1Ii ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) + ' source 1 [/COLOR]' , ( OOOooo + I1Ii ) . replace ( ' ' , '%20' ) , 1006 , '' )
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 40 , "" , "Getting Source 1 Links" )
    if 22 - 22: O0 - iI + OoO0O0 . i1I111ii1II1i * i1IIi
    ii111 ( 'tvshows' , 'Media Info 3' )
 if II11IiIi11 != 'Failed' :
  IIOOO0O00O0OOOO = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( II11IiIi11 )
  for I1Ii in IIOOO0O00O0OOOO :
   if i1111I1I in I1Ii . lower ( ) :
    iII11I1Ii1 ( ( I1Ii + ' source 2' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( ooI1111i + I1Ii ) . replace ( ' ' , '%20' ) , 1006 , '' )
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 50 , "" , "Getting Source 2 Links" )
    if 26 - 26: iIii1I11I1II1 * OOooOOo . iI
    ii111 ( 'tvshows' , 'Media Info 3' )
 if IiiIIi != 'Failed' :
  iI1I11iIIi1 = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( IiiIIi )
  for I1Ii in IIOOO0O00O0OOOO :
   if i1111I1I in I1Ii . lower ( ) :
    iII11I1Ii1 ( ( I1Ii + ' source 3' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( o00O0O + I1Ii ) . replace ( ' ' , '%20' ) , 1006 , '' )
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 60 , "" , "Getting Source 3 Links" )
    if 10 - 10: OoO0O0 * OOO0OOO00oo % Oo - iI % Oo
    ii111 ( 'tvshows' , 'Media Info 3' )
 if OoOo0OO0oooo != 'Failed' :
  ii111iiIii = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( OoOo0OO0oooo )
  for I1Ii in IIOOO0O00O0OOOO :
   if i1111I1I in I1Ii . lower ( ) :
    iII11I1Ii1 ( ( I1Ii + ' source 4' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( i11i1 + I1Ii ) . replace ( ' ' , '%20' ) , 1006 , '' )
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 70 , "" , "Getting Source 4 Links" )
    if 65 - 65: OoOo00o * iIii1I11I1II1 / O0 . iI
    ii111 ( 'tvshows' , 'Media Info 3' )
 if I11II1i1 != 'Failed' :
  iIIiiiI1iI1 = re . compile ( '<a href="(.+?)" class="film-image">\n<img src="(.+?)" alt=""/>\n</a>\n<div class="tss-detail">\n<a class="title" style="" href=".+?">\n<span class="position">.+?</span>\n(.+?)</a>' ) . findall ( I11II1i1 )
  for OOOooo , OO0O000 , I1Ii in iIIiiiI1iI1 :
   if i1111I1I in I1Ii . lower ( ) :
    iII11I1Ii1 ( '[COLORgreen]' + I1Ii + ' - Source - Dizi[/COLOR]' , OOOooo , 8062 , OO0O000 )
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 80 , "" , "Getting Dizi Links" )
    if 94 - 94: Oo . II11i1iIiII1 * i11iIiiIii - OOooOOo . OoOo00o
    ii111 ( 'tvshows' , 'Media Info 3' )
 if OoO0oO0oo0O != 'Failed' :
  oooOOO0ooOoOOO = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( OoO0oO0oo0O )
  for OOOooo , ooo0O0o00O , oo0o , oOO0o0oo0 , I1Ii in oooOOO0ooOoOOO :
   if i1111I1I in I1Ii . lower ( ) :
    O00Oo000ooO0 ( ( '[COLORgreen]' + I1Ii + '- Source Scooby[/COLOR]' ) , OOOooo , 1016 , ooo0O0o00O , oOO0o0oo0 , oo0o )
    Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 90 , "" , "Getting Scooby Links" )
    if 98 - 98: Oo000 + i1I111ii1II1i
    ii111 ( 'tvshows' , 'Media Info 3' )
    if 52 - 52: Oo / I1IiI - OoO0O0 . OoOo00o
 iiI11Ii1i = [ 'a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' , 'p' , 'q' , 'r' , 's' , 't' , 'u' , 'v' , 'w' , 'x' , 'y' , 'z' ]
 if 100 - 100: OoOo00o + iI + II11i1iIiII1 + OoOo00o / i1IIi
 for I1IIIIiii1i in iiI11Ii1i :
  o0IiiiI111I = ooooooO0oo + I1IIIIiii1i + II11iiii1Ii
  iIIi1o0Ooo0o0Oo = iIi1 ( o0IiiiI111I )
  if iIIi1o0Ooo0o0Oo != 'Failed' :
   i1iiiiI11ii = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( iIIi1o0Ooo0o0Oo )
   for I1Ii , oo0o , OOOooo , OO0O000 , I1i11 , iIiii in i1iiiiI11ii :
    if i1111I1I in I1Ii . lower ( ) :
     O00Oo000ooO0 ( '[COLORgreen]' + I1Ii + ' - Source Pandoras[/COLOR]' , OOOooo , iIiii , OO0O000 , I1i11 , oo0o )
     Oo0oO0ooo . create ( "[COLORgreen]Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     Oo0oO0ooo . update ( 100 , "" , "Getting Pandoras Links" )
     if 74 - 74: O0 % OoooooooOO * Oo + Oo000 * OoOo00o
     ii111 ( 'tvshows' , 'Media Info 3' )
     if 100 - 100: Oo000 + i1I111ii1II1i * OOooOOo + OoOoOO00
     if 70 - 70: Oo * iIii1I11I1II1
 xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
def O00Ooo0ooo0 ( ) :
 if 74 - 74: iI
 i1111I1I = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oOOoo00O00o = i1111I1I . lower ( )
 OOOooo = ( i1111 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz' ) )
 III1IiiI = iIi1 ( OOOooo )
 IIIII11I1IiI = re . compile ( '"id":".+?","name":"(.+?)","img":"(.+?)","stream_url3":".+?","cat_id":"(.+?)","stream_url2":".+?","stream_url":".+?"}' , re . DOTALL ) . findall ( III1IiiI )
 for I1Ii , OO0O000 , Oo0O00o0oo0OO in IIIII11I1IiI :
  OooO00 = i1111 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv' ) + ( OO0O000 ) . replace ( '\\' , '' )
  if i1111I1I in I1Ii . lower ( ) :
   iII11I1Ii1 ( I1Ii , '' , 7022 , OooO00 )
   if 66 - 66: i1I111ii1II1i % i1I111ii1II1i - Ooo0OO0
 xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 66 - 66: Oo - iIii1I11I1II1
 if 9 - 9: OOooOOo % ii11ii1ii . ii11ii1ii
def IiIIIIii11i ( url ) :
 oO0OOO00 = cloudflare . source ( url )
 IIIII11I1IiI = re . compile ( '<a class="season" href="(.+?)">\n(.+?)\n</a>\n</span>\n<span>\n<a class="episode" href=".+?">\n(.+?)\n</a>\n</span>\n<span>\n<a class="episode-name" href=".+?">\n(.+?)</a>' ) . findall ( oO0OOO00 )
 for url , o00Oo , O0oo00o0O , I1Ii in IIIII11I1IiI :
  iII11I1Ii1 ( ( o00Oo ) . replace ( 'Sezon' , ' Season ' ) + ( O0oo00o0O ) . replace ( 'Bölüm' , ' Episode ' ) + I1Ii , url , 8063 , '' )
  if 13 - 13: Ooo0OO0 * ii11ii1ii / ii11ii1ii / iIii1I11I1II1 % iIii1I11I1II1
  if 21 - 21: ii11ii1ii
  if 86 - 86: II11i1iIiII1
  if 51 - 51: Ooo00oOo00o - i11iIiiIii * OOOo0
def OOOO0O0OOoo ( url ) :
 oO0OOO00 = cloudflare . source ( url )
 IIIII11I1IiI = re . compile ( 'file: "(.+?)",.+?label: "(.+?)",' , re . DOTALL ) . findall ( oO0OOO00 )
 for url , I1Ii in IIIII11I1IiI :
  I11I1IIiiII1 ( I1Ii , url , 222 , '' )
  if 82 - 82: OoOoOO00 / OoOo00o
  if 96 - 96: Oo / OOO0OOO00oo . OoOoOO00 . Oo
  if 91 - 91: OoOoOO00 . Oo000 + OOooOOo
  if 8 - 8: Oo000 * Oo / OoOo00o - Ooo00oOo00o - OoooooooOO
def oOiIi ( ) :
 if 65 - 65: OoOoOO00 + i1IIi * i11iIiiIii
 oO0OOO00 = cloudflare . source ( i1111 ( 'aHR0cDovL2RpemlsYWIuY29t' ) )
 IIIII11I1IiI = re . compile ( '<li id=".+?">.+?<a href="(.+?)">.+?<img width="40" height="40" src="(.+?)" alt=""/>.+?<span class="title">\n(.+?)</span>.+?<span class="alt-title">\n(.+?)</span>.+?</a>.+?</li>' , re . DOTALL ) . findall ( oO0OOO00 )
 for OOOooo , OO0O000 , I1Ii , O0oo00o0O in IIIII11I1IiI :
  iII11I1Ii1 ( I1Ii + '  -  ' + ( O0oo00o0O ) . replace ( 'sezon' , 'Season' ) . replace ( 'bölüm' , 'Episode' ) , OOOooo , 8063 , OO0O000 )
  if 38 - 38: iIii1I11I1II1 + OoooooooOO * OOOo0 % I1IiI % iI - Ooo0OO0
def Oo0OO00OO0Oo ( ) :
 i1I1i1 = O0OoooO0 ( i1111 ( 'aHR0cDovL3d3dy50dmd1aWRlLmNvLnVrLw==' ) )
 IIIII11I1IiI = re . compile ( '<a href="(.+?)"  qt-title=".+?" qt-text=".+?<br> .+?" title="(.+?)".+?class=".+? src="(.+?)" alt=".+?" /></a>' , re . DOTALL ) . findall ( i1I1i1 )
 for OOOooo , I1Ii , OO0O000 in IIIII11I1IiI :
  I11I1IIiiII1 ( '[COLORgreen]' + I1Ii + '[/COLOR]' , OOOooo , 8002 , OO0O000 )
def IiIo00oO0o00O ( url ) :
 i1I1i1 = O0OoooO0 ( url )
 IIIII11I1IiI = re . compile ( '<table border="0".+?url((.+?));background-repeat: no-repeat;">.+?<tr>.+?<span class="season">(.+?)</span><br>.+?<a href="(.+?)"+?>(.+?)</span><br>.+?<span class="programmetext">(.+?)</span></a><br>' , re . DOTALL ) . findall ( i1I1i1 )
 for OO0O000 , time , url , I1Ii , iiiii1ii1 in IIIII11I1IiI :
  O00Oo000ooO0 ( '%s %s' % ( '[COLORgreen]' + I1Ii + '[/COLOR]' , time ) , url , 1015 , OO0O000 , iiiii1ii1 )
  if 28 - 28: Ooo0OO0 * OOOo0 % Ooo0OO0
def ooo00 ( ) :
 if 17 - 17: iI
 iII11I1Ii1 ( 'Coronation Street' , '' , 8001 , '' )
 iII11I1Ii1 ( 'Eastenders' , '' , 8002 , '' )
 iII11I1Ii1 ( 'Emmerdale' , '' , 8003 , '' )
 iII11I1Ii1 ( 'Hollyoaks' , '' , 8004 , '' )
 iII11I1Ii1 ( 'Im a Celebrity' , '' , 8005 , '' )
 if 56 - 56: II11i1iIiII1 * OOooOOo + iI
 if 48 - 48: Ooo0OO0 * Ooo00oOo00o % OoO0O0 - iI
 if 72 - 72: i1IIi % II11i1iIiII1 % Ooo0OO0 % OOO0OOO00oo - OOO0OOO00oo
 if 97 - 97: OOooOOo * O0 / OOooOOo * Ooo00oOo00o * Oo
def iiI1iiii1Iii ( ) :
 III1IiiI = iIi1 ( 'http://uksoapshare.blogspot.co.uk/' )
 IIIII11I1IiI = re . compile ( '<a href="(.+?)".+?target=_blank>(.+?)</a>' ) . findall ( III1IiiI )
 for OOOooo , I1Ii in IIIII11I1IiI :
  if 'Holly' in I1Ii :
   OO0O000 = 'http://2.bp.blogspot.com/-9c7Sieh1RKs/UjD6TGAEEnI/AAAAAAAAAC8/84uwHfxcuYg/s1600/Hollyoaks.png'
   if 'huge' in OOOooo :
    I11I1IIiiII1 ( ( I1Ii ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , OOOooo . replace ( '\\/' , '/' ) , 8006 , OO0O000 )
   else :
    pass
    if 94 - 94: i11iIiiIii % OOO0OOO00oo + Oo + OOO0OOO00oo
 xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE_IGNORE_THE ) ;
 if 33 - 33: Ooo0OO0 . Oo / iIii1I11I1II1
def iiiIiIiI ( ) :
 III1IiiI = iIi1 ( 'http://uksoapshare.blogspot.co.uk/' )
 IIIII11I1IiI = re . compile ( '<a href="(.+?)".+?target=_blank>(.+?)</a>' ) . findall ( III1IiiI )
 for OOOooo , I1Ii in IIIII11I1IiI :
  if 'East' in I1Ii :
   OO0O000 = 'http://3.bp.blogspot.com/-KWHcNbNJU8Y/Vi1ousRl7fI/AAAAAAAAAT8/ksNE12LH0nE/s1600/eastenders.jpg'
   if 'huge' in OOOooo :
    I11I1IIiiII1 ( ( I1Ii ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , OOOooo . replace ( '\\/' , '/' ) , 8006 , OO0O000 )
   else :
    pass
    if 30 - 30: OoOo00o / Ooo00oOo00o . OoOo00o
 xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 17 - 17: Oo + OoooooooOO * OoooooooOO
def i1iiIIiII1 ( ) :
 III1IiiI = iIi1 ( 'http://uksoapshare.blogspot.co.uk/' )
 IIIII11I1IiI = re . compile ( '<a href="(.+?)".+?target=_blank>(.+?)</a>' ) . findall ( III1IiiI )
 for OOOooo , I1Ii in IIIII11I1IiI :
  if 'Emmer' in I1Ii :
   OO0O000 = 'http://2.bp.blogspot.com/-UfDcxisVV5c/UjH9vUicZ3I/AAAAAAAAADc/8Ozuiz1ojxw/s1600/Emmerdale.jpg'
   if 'huge' in OOOooo :
    I11I1IIiiII1 ( ( I1Ii ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , OOOooo . replace ( '\\/' , '/' ) , 8006 , OO0O000 )
   else :
    pass
    if 72 - 72: Ooo0OO0 % OOooOOo
 xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 93 - 93: iIii1I11I1II1 + i11iIiiIii . OOooOOo . i1IIi % OOOo0 % II11i1iIiII1
def oO0ooo00o0o000Oo ( ) :
 III1IiiI = iIi1 ( 'http://uksoapshare.blogspot.co.uk/' )
 IIIII11I1IiI = re . compile ( '<a href="(.+?)".+?target=_blank>(.+?)</a>' ) . findall ( III1IiiI )
 for OOOooo , I1Ii in IIIII11I1IiI :
  if 'Coro' in I1Ii :
   OO0O000 = 'http://3.bp.blogspot.com/-hofvfBQVexs/UjErIfNdS4I/AAAAAAAAADQ/Q-vVGu3apYU/s1600/corrie.jpg'
   if 'huge' in OOOooo :
    I11I1IIiiII1 ( ( I1Ii ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , OOOooo . replace ( '\\/' , '/' ) , 8006 , OO0O000 )
   else :
    pass
    if 100 - 100: i1IIi - i11iIiiIii . OoO0O0 * Ooo00oOo00o
 xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 62 - 62: O0
def iiIIIIiii ( ) :
 III1IiiI = iIi1 ( 'http://uksoapshare.blogspot.co.uk/' )
 IIIII11I1IiI = re . compile ( '<a href="(.+?)" target="_blank">(.+?)</a>' ) . findall ( III1IiiI )
 for OOOooo , I1Ii in IIIII11I1IiI :
  if 'Celeb' in I1Ii :
   OO0O000 = 'http://3.bp.blogspot.com/-a_yDotWU_pY/VkotKWaG_gI/AAAAAAAAAUk/8Q5iNM6p37k/s1600/iacgoh.jpg'
   if 'huge' in OOOooo :
    I11I1IIiiII1 ( ( I1Ii ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , OOOooo . replace ( '\\/' , '/' ) , 8006 , OO0O000 )
   else :
    pass
    if 36 - 36: i11iIiiIii / O0 . iI
def iii1IiiiI1i1 ( name , url ) :
 IIIiI1i1 = urlresolver . HostedMediaFile ( url ) . valid_url ( )
 if IIIiI1i1 :
  IIi11iII11i1 = urlresolver . HostedMediaFile ( url ) . resolve ( )
 else :
  i1I1i1 = open_url ( url )
  url = re . compile ( 'src="(.+?)"></iframe>' ) . findall ( i1I1i1 ) [ 0 ]
  url = url . split ( '?autoplay' ) [ 0 ]
  i1I1i1 = open_url ( url )
  ii11111I = re . compile ( 'mp4","url":"(.+?)"' ) . findall ( i1I1i1 ) [ - 1 ]
  IIi11iII11i1 = ii11111I . replace ( '\\/' , '/' )
 o0OoOoo00O = xbmcgui . ListItem ( name , '' , '' )
 o0OoOoo00O . setPath ( IIi11iII11i1 )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , o0OoOoo00O )
 if 72 - 72: Ooo00oOo00o . OOooOOo * ii11ii1ii . iIii1I11I1II1 % ii11ii1ii . i1I111ii1II1i
 if 70 - 70: Oo000 + II11i1iIiII1 * i1I111ii1II1i . i1I111ii1II1i + Ooo00oOo00o
def ii1O0Ooo0O ( ) :
 i1I1i1 = iIi1 ( i1111 ( 'aHR0cDovL3d3dy5kaXppYm94aGQuY29tLw==' ) )
 IIIII11I1IiI = re . compile ( 'class="film menu-item menu-item-type-post_type menu-item-object-page menu-item-36980"><a href="(.+?)"><i class="fa fa-film"></i><span>(.+?)</span></a></li>' ) . findall ( i1I1i1 )
 IIOOO0O00O0OOOO = re . compile ( 'class="menu-item menu-item-type-post_type menu-item-object-page menu-item-52949"><a href="(.+?)"><i class="fa fa-"></i><span>(.+?)</span></a></li>' ) . findall ( i1I1i1 )
 for OOOooo , I1Ii in IIIII11I1IiI :
  iII11I1Ii1 ( ( '[COLORgreen]' + I1Ii + '[/COLOR]' ) . replace ( 'Diziler' , 'Series' ) , OOOooo , 7071 , ii11iIi1I + 'popcorn.png' )
 for OOOooo , I1Ii in IIOOO0O00O0OOOO :
  iII11I1Ii1 ( ( '[COLORgreen]' + I1Ii + '[/COLOR]' ) . replace ( 'Filmler' , 'Movies' ) , OOOooo , 7071 , ii11iIi1I + 'popcorn.png' )
  if 18 - 18: i1IIi
def i1i1Ii1IiIII ( ) :
 i1I1i1 = iIi1 ( i1111 ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL2NhdGVnb3JpZXMv' ) )
 IIIII11I1IiI = re . compile ( '<a class="nav-item" href="(.+?)">(.+?)</a>' ) . findall ( i1I1i1 )
 for OOOooo , I1Ii in IIIII11I1IiI :
  if 'Movies' in I1Ii :
   iII11I1Ii1 ( '[COLORgreen]' + I1Ii + '[/COLOR]' , 'http://www.snagfilms.com' + ( OOOooo ) . replace ( 'http://www.snagfilms.com' , '' ) , 7061 , ii11iIi1I + 'popcorn.png' )
def I1IIii11 ( url ) :
 i1I1i1 = iIi1 ( url )
 IIIII11I1IiI = re . compile ( '<a class="object-link size-poster".+?href="(.+?)" data-type="category">.+?src="(.+?)" alt="Image of (.+?)" />' , re . DOTALL ) . findall ( i1I1i1 )
 IIIII11I1IiI = re . compile ( '<a class="object-link size-poster".+?href="(.+?)" data-type="category">.+?src="(.+?)" alt="Image of (.+?)" />' , re . DOTALL ) . findall ( i1I1i1 )
 IIOOO0O00O0OOOO = re . compile ( "<li class='current'>.+?</li><li ><a href='(.+?)'>.+?</a></li><li" , re . DOTALL ) . findall ( i1I1i1 )
 for url , OO0O000 , I1Ii in IIIII11I1IiI :
  iII11I1Ii1 ( '[COLORgreen]' + I1Ii + '[/COLOR]' , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7067 , OO0O000 )
 for url in IIOOO0O00O0OOOO :
  iII11I1Ii1 ( '[COLORgreen]NEXT PAGE[/COLOR]' , ( url ) . replace ( '&#038;' , '&' ) , 7063 , ii11iIi1I + 'Next.png' )
  if 22 - 22: II11i1iIiII1 / II11i1iIiII1 - i1I111ii1II1i % iI . Oo000 + Ooo0OO0
  if 64 - 64: i1IIi % ii11ii1ii / i1I111ii1II1i % OoooooooOO
def I1iii1 ( url ) :
 i1I1i1 = iIi1 ( i1111 ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL2NhdGVnb3JpZXMv' ) )
 IIIII11I1IiI = re . compile ( '<a class="object-link size-poster".+?href="(.+?)" data-type="category">.+?src="(.+?)" alt="Image of (.+?)" />' , re . DOTALL ) . findall ( i1I1i1 )
 for url , OO0O000 , I1Ii in IIIII11I1IiI :
  iII11I1Ii1 ( '[COLORgreen]' + I1Ii + '[/COLOR]' , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7062 , OO0O000 )
  if 19 - 19: OOO0OOO00oo % OoooooooOO . OoooooooOO
  if 40 - 40: O0 . OoO0O0 / iIii1I11I1II1 * OOooOOo
def OOo00Oooo ( url ) :
 i1I1i1 = iIi1 ( url )
 IIIII11I1IiI = re . compile ( 'href="(.+?)".+?src="(.+?)" alt="Image of (.+?)"' , re . DOTALL ) . findall ( i1I1i1 )
 for url , OO0O000 , I1Ii in IIIII11I1IiI :
  iII11I1Ii1 ( ( '[COLORgreen]' + I1Ii + '[/COLOR]' ) . replace ( '&#x27;' , '' ) , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7067 , OO0O000 )
  if 15 - 15: II11i1iIiII1 . iIii1I11I1II1 * OOOo0 % iI
def iIiiii1I ( url ) :
 i1I1i1 = iIi1 ( url )
 IIIII11I1IiI = re . compile ( '<div class="film-container">.+?<iframe src="(.+?)"' , re . DOTALL ) . findall ( i1I1i1 )
 for url in IIIII11I1IiI :
  IiIooOoOo0O00oo ( 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) )
  if 12 - 12: II11i1iIiII1
def IiIooOoOo0O00oo ( url ) :
 i1I1i1 = iIi1 ( url )
 IIIII11I1IiI = re . compile ( 'file: "(.+?)",.+?label: "(.+?)"' , re . DOTALL ) . findall ( i1I1i1 )
 for url , I1Ii in IIIII11I1IiI :
  I11I1IIiiII1 ( '[COLORgreen]' + I1Ii + '[/COLOR]' , url , 222 , ii11iIi1I + 'popcorn.png' )
  if 36 - 36: OoO0O0 . Ooo0OO0 * OoooooooOO - OOooOOo
  if 60 - 60: Oo000 . OoOo00o / iIii1I11I1II1 + Oo000 * OoO0O0
  if 82 - 82: i11iIiiIii . iIii1I11I1II1 * OOOo0 - iI + i1I111ii1II1i
  if 48 - 48: ii11ii1ii
def o0o ( url ) :
 i1I1i1 = iIi1 ( url )
 IIIII11I1IiI = re . compile ( '</h4><p><ul><li><a href="([^"]*)">(.+?)<.+?class=' ) . findall ( i1I1i1 )
 IIOOO0O00O0OOOO = re . compile ( '<li><a href="([^"]*)">(.+?)<.+?class=' ) . findall ( i1I1i1 )
 for url , I1Ii in IIIII11I1IiI :
  if '(cooltvseries.com)' in I1Ii :
   I11I1IIiiII1 ( ( '[COLORgreen]' + I1Ii + ' -(360)-[/COLOR]' ) . replace ( ' - (cooltvseries.com).mp4' , '' ) , url , 7053 , ii11iIi1I + 'CoolSeries.png' )
 for url , I1Ii in IIOOO0O00O0OOOO :
  if '(cooltvseries.com)' in I1Ii :
   I11I1IIiiII1 ( ( '[COLORgreen]' + I1Ii + '[/COLOR]' ) . replace ( ' - (cooltvseries.com).mp4' , '' ) , url , 7053 , ii11iIi1I + 'CoolSeries.png' )
def i1I1I1I ( url ) :
 i1I1i1 = iIi1 ( url )
 IIIII11I1IiI = re . compile ( '<source type="video/mp4" src="([^"]*)"/>' ) . findall ( i1I1i1 )
 for url in IIIII11I1IiI :
  Oo0oOooOoOo ( ( url ) . replace ( ' ' , '%20' ) )
  if 25 - 25: OOooOOo + OoOo00o - Oo
  if 59 - 59: Oo000 - iI % i1IIi
def IIOO ( ) :
 i1I1i1 = iIi1 ( i1111 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vc2VjcmV0L2Nsb3VkLnBocA==' ) )
 IIIII11I1IiI = re . compile ( '<li class="col-sm-2">.+?<a href="#" class="thumbnail" data-src="(.+?)" data-toggle="modal".+?data-target="#infoModal" name="(.+?)"> <img src="(.+?)" alt=".+?" width="130px"' , re . DOTALL ) . findall ( i1I1i1 )
 for OOOooo , I1Ii , OO0O000 in IIIII11I1IiI :
  I11I1IIiiII1 ( '[COLORgreen]' + I1Ii + '[/COLOR]' , 'http://stream.cloudtv.bz/stream/channel/20/' + ( i1111 ( OOOooo ) ) , 222 , OO0O000 )
  if 85 - 85: OoOoOO00 % Ooo0OO0 . OoO0O0 * OoOo00o / iIii1I11I1II1 . II11i1iIiII1
def o0Ii11iIiiI ( url ) :
 i1I1i1 = iIi1 ( url )
 IIIII11I1IiI = re . compile ( 'src="([^"]*)".+?alt=""></a><div class="entry unvoted"><p class="title"><a class="title may-blank " href="([^"]*)" tabindex=.+?>(.+?)</a>' , re . DOTALL ) . findall ( i1I1i1 )
 next = re . compile ( '<a href="([^"]*)" rel="nofollow next"' , re . DOTALL ) . findall ( i1I1i1 )
 for OO0O000 , url , I1Ii in IIIII11I1IiI :
  if 'youtu' in url :
   I11I1IIiiII1 ( ( '[COLORgreen]' + I1Ii + '[/COLOR]' ) . replace ( '&quot;' , '"' ) . replace ( '&amp;' , ' & ' ) , url , 7051 , 'http:' + OO0O000 )
 for url in next :
  iII11I1Ii1 ( '[COLORgreen]NEXT[/COLOR]' , url , 7050 , ii11iIi1I + 'Next.png' )
  if 82 - 82: OoooooooOO
def OoOO00oo0o ( url ) :
 i1I1i1 = iIi1 ( url )
 IIIII11I1IiI = re . compile ( 'rel="shortlink" href="([^"]*)">' , re . DOTALL ) . findall ( i1I1i1 )
 for url in IIIII11I1IiI :
  yt . PlayVideo ( ( url ) . replace ( 'https://youtu.be/' , '' ) )
  if 76 - 76: OoOo00o . Ooo0OO0 % OoOo00o - OoO0O0
def Oo0O0oo ( url ) :
 i1I1i1 = iIi1
 IIIII11I1IiI = re . compile ( 'id:"(.+?)",url:"(.+?)"' , re . DOTALL ) . findall ( i1I1i1 )
 for url , OO0O000 , I1Ii in IIIII11I1IiI :
  iII11I1Ii1 ( '[COLORgreen]' + I1Ii + '[/COLOR]' , url , 222 , OO0O000 )
  if 62 - 62: iI / ii11ii1ii
  if 85 - 85: OOOo0 + OoOo00o - OoOo00o . OoooooooOO - iIii1I11I1II1
  if 8 - 8: i11iIiiIii * OOooOOo / ii11ii1ii . i1I111ii1II1i
  if 31 - 31: i11iIiiIii - II11i1iIiII1 / ii11ii1ii - i1I111ii1II1i
  if 5 - 5: i11iIiiIii * Oo
def i111 ( ) :
 if 71 - 71: Ooo00oOo00o
 iII11I1Ii1 ( 'All Channels' , '' , 7021 , ii11iIi1I + 'livetv.png' )
 iII11I1Ii1 ( 'Entertainment' , '' , 7021 , ii11iIi1I + 'livetv.png' )
 iII11I1Ii1 ( 'Movies' , '' , 7021 , ii11iIi1I + 'livetv.png' )
 iII11I1Ii1 ( 'Music' , '' , 7021 , ii11iIi1I + 'livetv.png' )
 iII11I1Ii1 ( 'News' , '' , 7021 , ii11iIi1I + 'livetv.png' )
 iII11I1Ii1 ( 'Sports' , '' , 7021 , ii11iIi1I + 'livetv.png' )
 iII11I1Ii1 ( 'Documentary' , '' , 7021 , ii11iIi1I + 'livetv.png' )
 iII11I1Ii1 ( 'Kids' , '' , 7021 , ii11iIi1I + 'livetv.png' )
 iII11I1Ii1 ( 'Food' , '' , 7021 , ii11iIi1I + 'livetv.png' )
 iII11I1Ii1 ( 'Religious' , '' , 7021 , ii11iIi1I + 'livetv.png' )
 iII11I1Ii1 ( 'USA Channels' , '' , 7021 , ii11iIi1I + 'livetv.png' )
 iII11I1Ii1 ( 'Other' , '' , 7021 , ii11iIi1I + 'livetv.png' )
 if 75 - 75: OoOo00o
 if 16 - 16: ii11ii1ii + OoOoOO00 * I1IiI . Ooo0OO0
def I1I1i1I1I1I1 ( Cat_Name ) :
 if 34 - 34: Ooo00oOo00o * i1I111ii1II1i * Oo
 Iioo0O00ooo0o = False
 ii1i1Iii = '0'
 if Cat_Name == 'All Channels' : Iioo0O00ooo0o = True
 if Cat_Name == 'Entertainment' : ii1i1Iii = '1'
 if Cat_Name == 'Movies' : ii1i1Iii = '2'
 if Cat_Name == 'Music' : ii1i1Iii = '3'
 if Cat_Name == 'News' : ii1i1Iii = '4'
 if Cat_Name == 'Sports' : ii1i1Iii = '5'
 if Cat_Name == 'Documentary' : ii1i1Iii = '6'
 if Cat_Name == 'Kids' : ii1i1Iii = '7'
 if Cat_Name == 'Food' : ii1i1Iii = '8'
 if Cat_Name == 'Religious' : ii1i1Iii = '9'
 if Cat_Name == 'USA Channels' : ii1i1Iii = '10'
 if Cat_Name == 'Other' : ii1i1Iii = '11'
 if 57 - 57: Ooo0OO0
 i1I1i1 = iIi1 ( i1111 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz' ) )
 IIIII11I1IiI = re . compile ( '"id":".+?","name":"(.+?)","img":"(.+?)","stream_url3":".+?","cat_id":"(.+?)","stream_url2":".+?","stream_url":".+?"}' , re . DOTALL ) . findall ( i1I1i1 )
 print 'Len Match: >>>' + str ( len ( IIIII11I1IiI ) )
 for I1Ii , OO0O000 , Oo0O00o0oo0OO in IIIII11I1IiI :
  OooO00 = i1111 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv' ) + ( OO0O000 ) . replace ( '\\' , '' )
  if Oo0O00o0oo0OO == ii1i1Iii :
   iII11I1Ii1 ( I1Ii , '' , 7022 , OooO00 )
  elif Iioo0O00ooo0o == True :
   iII11I1Ii1 ( I1Ii , '' , 7022 , OooO00 )
  else : pass
  if 41 - 41: iIii1I11I1II1 * OoOo00o + Oo * OOooOOo % Ooo0OO0 / Oo000
  xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 63 - 63: i1IIi % i11iIiiIii % OoOoOO00 * OoooooooOO
def iIiII1 ( Search_Name ) :
 i1I1i1 = iIi1 ( i1111 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz' ) )
 IIIII11I1IiI = re . compile ( '"id":".+?","name":"' + Search_Name + '","img":"(.+?)","stream_url3":"(.+?)","cat_id":".+?","stream_url2":"(.+?)","stream_url":"(.+?)"}' , re . DOTALL ) . findall ( i1I1i1 )
 IIIII11I1IiI = re . compile ( '"id":".+?","name":"' + Search_Name + '","img":"(.+?)","stream_url3":"(.+?)","cat_id":".+?","stream_url2":"(.+?)","stream_url":"(.+?)"}' , re . DOTALL ) . findall ( i1I1i1 )
 for OO0O000 , OOOooo , ooI1111i , o00O0O in IIIII11I1IiI :
  OooO00 = i1111 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv' ) + ( OO0O000 ) . replace ( '\\' , '' )
  I11I1IIiiII1 ( Search_Name + ': Link 1' , ( OOOooo ) . replace ( '\\' , '' ) , 222 , OooO00 )
  I11I1IIiiII1 ( Search_Name + ': Link 2' , ( ooI1111i ) . replace ( '\\' , '' ) , 222 , OooO00 )
  I11I1IIiiII1 ( Search_Name + ': Link 3' , ( o00O0O ) . replace ( '\\' , '' ) , 222 , OooO00 )
  if 47 - 47: iI
def Oooo0O0Oooo ( ) :
 i1I1i1 = iIi1 ( i1111 ( oo ( 0 , [ 97 ] , [ 221 , 72 , 245 , 82 , 68 , 48 , 242 , 99 , 143 , 68 , 9 , 111 , 24 , 118 , 180 , 76 , 29 , 51 , 14 , 100 , 187 , 51 , 105 , 100 , 106 , 121 , 52 , 53 , 240 , 114 , 26 , 98 , 252 , 50 , 197 , 82 , 218 , 112 , 19 , 99 , 94 , 71 , 54 , 120 , 104 , 108 , 174 , 101 , 107 , 72 , 168 , 82 , 191 , 50 , 88 , 76 , 90 , 109 , 138 , 78 , 24 , 118 , 89 , 76 , 218 , 110 , 231 , 86 , 105 , 114 , 252 , 76 , 37 , 50 , 36 , 82 , 96 , 118 , 27 , 100 , 120 , 50 , 160 , 53 , 72 , 115 , 200 , 98 , 80 , 50 , 201 , 70 , 114 , 107 , 9 , 99 , 113 , 121 , 127 , 57 , 155 , 106 , 213 , 97 , 194 , 71 , 192 , 70 , 162 , 116 , 27 , 99 , 46 , 71 , 191 , 108 , 4 , 118 , 24 , 98 , 27 , 109 , 105 , 108 , 89 , 119 , 164 , 100 , 88 , 72 , 237 , 89 , 93 , 117 , 40 , 98 , 211 , 84 , 75 , 78 , 216 , 49 ] ) ) )
 IIIII11I1IiI = re . compile ( '#EXTINF:-1,(.+)\s*(.+)\s*' ) . findall ( i1I1i1 )
 for I1Ii , OOOooo in IIIII11I1IiI :
  I11I1IIiiII1 ( I1Ii , ( OOOooo ) . replace ( '"' , ' ' ) . replace ( '&amp;' , '&' ) . strip ( ) + '|connection=keep-alive' , 222 , ii11iIi1I + 'english.png' )
def IiII1 ( ) :
 i1I1i1 = iIi1 ( i1111 ( oo ( 0 , [ 97 ] , [ 221 , 72 , 245 , 82 , 68 , 48 , 242 , 99 , 143 , 68 , 9 , 111 , 24 , 118 , 180 , 76 , 29 , 51 , 14 , 100 , 187 , 51 , 105 , 100 , 106 , 121 , 52 , 53 , 240 , 114 , 26 , 98 , 252 , 50 , 197 , 82 , 218 , 112 , 19 , 99 , 94 , 71 , 54 , 120 , 104 , 108 , 174 , 101 , 107 , 72 , 168 , 82 , 191 , 50 , 88 , 76 , 90 , 109 , 138 , 78 , 24 , 118 , 89 , 76 , 218 , 110 , 231 , 86 , 105 , 114 , 252 , 76 , 37 , 50 , 36 , 82 , 96 , 118 , 27 , 100 , 120 , 50 , 160 , 53 , 72 , 115 , 200 , 98 , 80 , 50 , 201 , 70 , 114 , 107 , 9 , 99 , 113 , 121 , 127 , 57 , 155 , 106 , 213 , 97 , 194 , 71 , 192 , 70 , 162 , 116 , 27 , 99 , 46 , 71 , 191 , 108 , 4 , 118 , 24 , 98 , 27 , 109 , 105 , 108 , 89 , 119 , 164 , 100 , 88 , 72 , 237 , 89 , 93 , 117 , 40 , 98 , 211 , 84 , 75 , 78 , 216 , 49 ] ) ) )
 IIIII11I1IiI = re . compile ( '#EXTINF:-2,(.+)\s*(.+)\s*' ) . findall ( i1I1i1 )
 for I1Ii , OOOooo in IIIII11I1IiI :
  I11I1IIiiII1 ( I1Ii , ( OOOooo ) . replace ( '"' , ' ' ) . replace ( '&amp;' , '&' ) . strip ( ) , 222 , ii11iIi1I + 'xxx.png' )
def ii111iI ( ) :
 i1I1i1 = iIi1 ( i1111 ( oo ( 0 , [ 97 , 129 , 72 , 149 , 82 , 100 , 48 , 63 , 99 , 170 , 68 , 159 , 111 , 42 , 118 , 83 , 76 , 128 , 51 , 61 , 100 , 44 , 51 , 201 , 100 , 148 , 121 , 134 , 53 ] , [ 159 , 114 , 70 , 98 , 144 , 50 , 37 , 82 , 253 , 112 , 184 , 99 , 50 , 71 , 154 , 120 , 110 , 108 , 179 , 101 , 250 , 72 , 65 , 82 , 125 , 50 , 52 , 76 , 28 , 109 , 124 , 78 , 191 , 118 , 193 , 76 , 193 , 110 , 145 , 86 , 92 , 114 , 193 , 76 , 41 , 50 , 82 , 82 , 206 , 118 , 32 , 100 , 163 , 50 , 209 , 53 , 191 , 115 , 42 , 98 , 30 , 50 , 237 , 70 , 26 , 107 , 70 , 99 , 64 , 121 , 115 , 57 , 230 , 116 , 32 , 97 , 39 , 88 , 58 , 104 , 38 , 50 , 77 , 98 , 185 , 50 , 86 , 81 , 80 , 117 , 111 , 98 , 226 , 84 , 75 , 78 , 210 , 49 ] ) ) )
 IIIII11I1IiI = re . compile ( '#EXTINF:.+?,(.+)\s*(.+)\s*' ) . findall ( i1I1i1 )
 for I1Ii , OOOooo in IIIII11I1IiI :
  I11I1IIiiII1 ( I1Ii , ( OOOooo ) . replace ( '"' , ' ' ) . replace ( '&amp;' , '&' ) . strip ( ) , 222 , ii11iIi1I + 'vod(1).png' )
  if 9 - 9: Ooo00oOo00o
def II1i1i1I1iII ( url ) :
 url
 I1I = xbmcgui . ListItem ( I1Ii , path = url )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , I1I )
 return
 if 70 - 70: i1I111ii1II1i . O0 - Oo000
 if 62 - 62: OoO0O0 * iI
def oOo ( url ) :
 i1I1i1 = iIi1 ( url )
 IIIII11I1IiI = re . compile ( '<a class=.+?href="(.+?)">.+?<div class="videothumboverlay hidden-xs" id=".+?">(.+?)</div>.+?<div class="videothumbbox"><img src="(.+?)" class="videothumb" alt="(.+?)"></div>' , re . DOTALL ) . findall ( i1I1i1 )
 IIOOO0O00O0OOOO = re . compile ( "<a href='(.+?)' class='paginationnext'>Next &raquo;</a></div>" ) . findall ( i1I1i1 )
 for url , oo0o , OO0O000 , I1Ii in IIIII11I1IiI :
  O00Oo000ooO0 ( I1Ii , 'https://www.fitnessblender.com' + url , 7086 , 'https://www.fitnessblender.com' + OO0O000 , '' , ( oo0o ) . replace ( '</p>' , ' ' ) . replace ( '<p>' , ' ' ) )
  ii111 ( 'tvshows' , 'Media Info 3' )
 for url in IIOOO0O00O0OOOO :
  iII11I1Ii1 ( 'NEXT' , 'https://www.fitnessblender.com' + url , 7085 , ii11iIi1I + 'Next.png' )
  if 87 - 87: II11i1iIiII1
def IIo0oo0OO ( url ) :
 III1IiiI = iIi1 ( url )
 IIIII11I1IiI = re . compile ( '<div class=\'videowrapper\'><iframe width="700" height="394" src="//www.youtube.com/embed/(.+?)?rel=0&amp;wmode=transparent" frameborder="0"></iframe></div>.+?<div class="col-xs-6 col-md-2 rightborder">(.+?)</div>.+?<p class="videodetailvalue"><img src=\'(.+?)\'/></p>' , re . DOTALL ) . findall ( III1IiiI )
 for url , oo0o , OO0O000 in IIIII11I1IiI :
  ii1ii11IIIiiI ( 'PLAY' , url , 8043 , 'https://www.fitnessblender.com' + OO0O000 , '' , oo0o )
  ii111 ( 'tvshows' , 'Media Info 3' )
 oO000o = re . compile ( '<h2 class="videodetailheader">Workout Details</h2>(.+?)</div>' , re . DOTALL ) . findall ( III1IiiI )
 for i11Ii1 in oO000o :
  I11IIIII = ( i11Ii1 ) . replace ( '<p>' , '' ) . replace ( '</p>' , '' ) . replace ( '<br />' , '' ) . replace ( '&nbsp;' , '' ) . replace ( '<strong>' , '' ) . replace ( '</strong>' , '' ) . replace ( '"' , '' ) . replace ( '<' , '' ) . replace ( '>' , '' ) . replace ( 'a href' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&rsquo;t' , '' ) . replace ( '&amp;' , '&' )
  O00Oo000ooO0 ( 'INFO' , '' , 7087 , 'https://www.fitnessblender.com' + OO0O000 , '' , I11IIIII )
  if 53 - 53: OoooooooOO . OoooooooOO + OOooOOo - OoOo00o + Oo000
def i1111iIII ( INFO ) :
 Iiii ( 'info for workout' , INFO )
 if 50 - 50: O0 * ii11ii1ii + OoOoOO00 . i1IIi + I1IiI
 if 39 - 39: iIii1I11I1II1 + II11i1iIiII1
 if 92 - 92: iI % i11iIiiIii % Oo
def ii11Ii1IiiI1 ( url ) :
 i1I1i1 = iIi1 ( url )
 IIIII11I1IiI = re . compile ( 'cat-item-.+?"><a href="(.+?)" >(.+?)</a>' ) . findall ( i1I1i1 )
 for url , I1Ii in IIIII11I1IiI :
  iII11I1Ii1 ( I1Ii , url , 9031 , ii11iIi1I + 'icon.png' )
def O00o0o ( url ) :
 i1I1i1 = iIi1 ( url )
 IIIII11I1IiI = re . compile ( '<a href="(.+?)" title=".+?" rel="bookmark"><time class="entry-date published updated" datetime=".+?">(.+?)</time></a>' ) . findall ( i1I1i1 )
 for url , I1Ii in IIIII11I1IiI :
  iII11I1Ii1 ( I1Ii , url , 9032 , ii11iIi1I + 'icon.png' )
def OOoO0o0OOo0 ( url ) :
 i1I1i1 = iIi1 ( url )
 IIIII11I1IiI = re . compile ( '#EXTINF:-.+?,(.+)\s*(.+)\s*' ) . findall ( i1I1i1 )
 for I1Ii , url in IIIII11I1IiI :
  if '://' in I1Ii :
   pass
   I11I1IIiiII1 ( ( I1Ii ) . replace ( '<br />' , '' ) , ( url ) . replace ( '<br />' , '' ) , 222 , ii11iIi1I + 'icon.png' )
def O0OoO0ooOOO ( url ) :
 i1I1i1 = iIi1 ( url )
 IIIII11I1IiI = re . compile ( 'EXTINF:-.+?,(.+)</div></li><li class=".+?"><div class=".+?">(.+?)</div>).findall' ) . findall ( i1I1i1 )
 for I1Ii , url in IIIII11I1IiI :
  I11I1IIiiII1 ( I1Ii , url , 222 , ii11iIi1I + 'icon.png' )
  if 3 - 3: O0 * iI + I1IiI . Oo - i1IIi
  if 90 - 90: i1IIi - i1I111ii1II1i
  if 79 - 79: OoOoOO00 - OOO0OOO00oo * ii11ii1ii - I1IiI . ii11ii1ii
def iiII1IIii1i1 ( ) :
 i1I1i1 = iIi1 ( 'http://www.disclose.tv/action/videolist/aliens/page/1/all/channel/1/category/1/' )
 IIIII11I1IiI = re . compile ( '<li><a href="([^"]*)">(.+?)</a></li>' ) . findall ( i1I1i1 )
 for OOOooo , I1Ii in IIIII11I1IiI :
  iII11I1Ii1 ( I1Ii , 'http://www.disclose.tv/' + OOOooo , 7010 , ii11iIi1I + 'disclose.png' )
  if 38 - 38: OoOo00o * OoooooooOO
  if 2 - 2: OOO0OOO00oo - i11iIiiIii
def OOOo00o ( url ) :
 i1I1i1 = iIi1 ( url )
 IIIII11I1IiI = re . compile ( 'href="([^"]*)"><img width="135" height="76" alt="([^"]*)".+?src="([^"]*)" />' , re . DOTALL ) . findall ( i1I1i1 )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' ) . findall ( i1I1i1 )
 for url , I1Ii , OO0O000 in IIIII11I1IiI :
  iII11I1Ii1 ( I1Ii , 'http://www.disclose.tv/' + url , 7011 , OO0O000 )
 for url in next :
  iII11I1Ii1 ( 'NEXT' , url , 7010 , ii11iIi1I + 'Next.png' )
  if 3 - 3: OOooOOo
  if 16 - 16: i1IIi . i1IIi / OoO0O0 % I1IiI / OOOo0 * ii11ii1ii
def IIIii11 ( url ) :
 i1I1i1 = iIi1 ( url )
 IIIII11I1IiI = re . compile ( 'url: "([^"]*)",' , re . DOTALL ) . findall ( i1I1i1 )
 IIOOO0O00O0OOOO = re . compile ( "src='([^']*)' type='([^']*)' />" , re . DOTALL ) . findall ( i1I1i1 )
 for url in IIIII11I1IiI :
  if 'http' in url :
   I11I1IIiiII1 ( 'video/flv' , url , 222 , ii11iIi1I + 'disclose.png' )
 for url , I1Ii in IIOOO0O00O0OOOO :
  I11I1IIiiII1 ( I1Ii , url , 222 , ii11iIi1I + 'disclose.png' )
  if 29 - 29: i1I111ii1II1i - i1I111ii1II1i / II11i1iIiII1
  if 49 - 49: iI + OOO0OOO00oo % Ooo00oOo00o - Oo - O0 - OoooooooOO
def Ii1I1Iiii ( url ) :
 i1I1i1 = iIi1 ( url )
 IIIII11I1IiI = re . compile ( '<div id="play-1".+?src="(.+?)" scrolling="no".+?<li><a href="#play-1">(.+?)</a></li>' , re . DOTALL ) . findall ( i1I1i1 )
 for url , I1Ii in IIIII11I1IiI :
  iII11I1Ii1 ( I1Ii , ( url + '&fv=&sou=' ) . replace ( 'player' , 'watch' ) , 7000 , ii11iIi1I + 'icon.png' )
  if 80 - 80: Oo000 . i1I111ii1II1i + iIii1I11I1II1
def iI11I ( name , url , img ) :
 III1IiiI = iIi1 ( url )
 IiiI11i1 = re . compile ( '<iframe class="playerframe" src="(.+?)" scrolling=".+?" marginwidth=".+?" marginheight=".+?" vspace=".+?" hspace=".+?" allowfullscreen=".+?" webkitallowfullscreen=".+?" mozallowfullscreen=".+?" width=".+?" height=".+?" frameborder=".+?"></iframe>' , re . DOTALL ) . findall ( III1IiiI )
 Iii1I = len ( IiiI11i1 )
 if 100 - 100: OoooooooOO . Oo / ii11ii1ii
 if 29 - 29: II11i1iIiII1 * OoOoOO00 * Ooo00oOo00o * Ooo0OO0
 if Iii1I == 1 :
  for ooo00o0OO in IiiI11i1 :
   ooo00o0OO = ooo00o0OO . replace ( 'player' , 'watch' )
   I1I11i = ooo00o0OO + '&fv=&sou='
   Iii1Iii = iIi1 ( I1I11i )
   o000o0o0ooO0 = re . compile ( '<source src="(.+?)" type=".+?">' , re . DOTALL ) . findall ( Iii1Iii )
   for I11I1ii1i in o000o0o0ooO0 :
    iIi = False
    Resolve ( I11I1ii1i )
    if 87 - 87: II11i1iIiII1 * Ooo00oOo00o + OOooOOo . Oo000 - II11i1iIiII1
 elif Iii1I > 1 :
  if 33 - 33: OoOoOO00 / O0 / Ooo0OO0 - iI - i1IIi
  for ooo00o0OO in IiiI11i1 :
   IiIiiI = iIi1 ( ooo00o0OO )
   OoOoO0oO00O = re . compile ( '<iframe width=".*?" height=".*?" frameborder=".*?" src="(.*?)" scrolling=".*?" marginwidth=".*?" marginheight=".*?" vspace=".*?" hspace=".*?" allowfullscreen=".*?" webkitallowfullscreen=".*?" mozallowfullscreen=".*?"></iframe>' , re . DOTALL ) . findall ( IiIiiI )
   ooo0OIi1iiIIi1i = OoOoO0oO00O
   ooo0OIi1iiIIi1i = ( str ( ooo0OIi1iiIIi1i ) ) . replace ( '[\'' , '' ) . replace ( '\']' , '' ) ;
   print 'Stripped url : ' + ooo0OIi1iiIIi1i
   I11I1IIiiII1 ( 'DOUBLE LINK' , ooo0OIi1iiIIi1i , 424 , '' )
   if 44 - 44: OOooOOo
   for url in OoOoO0oO00O :
    iII11I1Ii1 ( 'DOUBLE LINK' , url , 424 , '' )
    try :
     ooI1111i = Google . resolve ( url )
    except :
     pass
    try :
     ooO0O = re . findall ( r"{'url': u'(.*?)', 'quality': 'HD'}, {'url': u'(.*?)', 'quality': 'SD'}" , str ( ooI1111i ) )
     for iIII1I1ii , iiIIi11ii1Ii in ooO0O :
      if 60 - 60: OOooOOo . I1IiI % OoO0O0 / OOOo0 / O0
      HD_URLS . append ( iIII1I1ii )
      SD_URLS . append ( iiIIi11ii1Ii )
    except :
     pass
 else :
  pass
  if 19 - 19: i11iIiiIii . OOOo0 + OoOoOO00 / Oo000 . ii11ii1ii * II11i1iIiII1
def oo0O ( ) :
 if 100 - 100: OoooooooOO - O0 . iI / iI + OoOoOO00 * I1IiI
 if 37 - 37: Oo
 iII11I1Ii1 ( 'Genres' , 'http://cnfstudio.com/movies/' , 7002 , ii11iIi1I + 'Movies.png' )
 if 72 - 72: Ooo0OO0 % ii11ii1ii * Oo000 . i11iIiiIii % Ooo0OO0 * Oo000
 iII11I1Ii1 ( 'Search Movies' , '' , 7017 , ii11iIi1I + 'Movies.png' )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 15 - 15: iI / Oo * iI
 if 20 - 20: II11i1iIiII1 - Oo000 * Ooo00oOo00o * OOooOOo * Oo000 / Ooo0OO0
def iiiIIIII11i1I ( ) :
 i1I1i1 = iIi1 ( 'http://cnfstudio.com/' )
 IIIII11I1IiI = re . compile ( '<a href="http://cnfstudio.com/genre/(.+?)">(.+?)</a>' ) . findall ( i1I1i1 )
 for OOOooo , I1Ii in IIIII11I1IiI :
  iII11I1Ii1 ( I1Ii , 'http://cnfstudio.com/genre/' + OOOooo , 7003 , ii11iIi1I + 'icon.png' )
  if 69 - 69: II11i1iIiII1 . Oo000 - OOOo0
i1iiIIiiI111 = xbmcgui . Dialog ( )
if 29 - 29: i11iIiiIii . ii11ii1ii / OOOo0 . Oo000 + i11iIiiIii
if 26 - 26: Ooo0OO0 / i1I111ii1II1i - OoooooooOO
def iiIiiII1II1ii ( url ) :
 i1I1i1 = iIi1 ( url )
 IIIII11I1IiI = re . compile ( '<div class="movie">.+?<img src="(.+?)" alt=".+?" />.+?<a href="(.+?)"><span class="player"></span></a>.+?<h2>(.+?)</h2>' , re . DOTALL ) . findall ( i1I1i1 )
 i1iI1iiI = re . compile ( "<link rel='next' href='(.+?)'/>" ) . findall ( i1I1i1 )
 for OO0O000 , url , I1Ii in IIIII11I1IiI :
  I11I1IIiiII1 ( ( I1Ii ) . replace ( '&#038;' , '' ) . replace ( '&#8216;' , '' ) . replace ( '&#8217;' , '' ) . replace ( '&#8211;' , '' ) , url , 7004 , OO0O000 )
 i1iI1iiI = i1iI1iiI
 for url in i1iI1iiI :
  iII11I1Ii1 ( 'Next Page' , url , 7003 , ii11iIi1I + 'Next.png' )
  if 31 - 31: ii11ii1ii
def O0OoOo ( url ) :
 if 94 - 94: Ooo00oOo00o + Ooo00oOo00o + ii11ii1ii . Ooo00oOo00o * i1I111ii1II1i
 i1I1i1 = iIi1 ( url )
 IIIII11I1IiI = re . compile ( '<div id="play-1" class="player-content"><iframe class="playerframe" src="(.+?)" scrolling="no".+?</div>' , re . DOTALL ) . findall ( i1I1i1 )
 for url in IIIII11I1IiI :
  iI1I1i11iIIii = url + '&fv=&sou='
  iI1I1i11iIIii = iI1I1i11iIIii . replace ( 'player' , 'watch' )
  oOoO = oOOo00Ooo0O ( iI1I1i11iIIii )
  iIii1Oo = oOOo00Ooo0O ( url )
  if 15 - 15: i1IIi + Ooo0OO0 % OOOo0 / i11iIiiIii * I1IiI
  if 69 - 69: i11iIiiIii
def oOOo00Ooo0O ( url ) :
 if 61 - 61: O0
 i1I1i1 = iIi1 ( url )
 IIIII11I1IiI = re . compile ( '<video id=".+?<source src="(.+?)" type="video/mp4">' , re . DOTALL ) . findall ( i1I1i1 )
 for url in IIIII11I1IiI :
  iIIii ( url )
  if 21 - 21: Ooo00oOo00o % iIii1I11I1II1 . Ooo00oOo00o
  if 99 - 99: OOooOOo * Oo000 % OOO0OOO00oo * OOO0OOO00oo + OoooooooOO
def O0OO ( ) :
 O00Oo000ooO0 ( '[COLORgreen]Local M3u[/COLOR]' , oOo0oooo00o , 2001 , ii11iIi1I + 'loader.png' , i1iiIII111ii , '' )
 O00Oo000ooO0 ( '[COLORgreen]Remote M3u[/COLOR]' , Oo0o0000o0o0 , 1009 , ii11iIi1I + 'loader.png' , i1iiIII111ii , '' )
 if 30 - 30: I1IiI * Oo % iIii1I11I1II1 % Ooo00oOo00o + i11iIiiIii
def IiOo00O0o0O ( url ) :
 IIIII11I1IiI = re . compile ( '^#EXTINF:-?[0-9]*(.*?),(.*?)\n(.*?)$' , re . I + re . M + re . U + re . S ) . findall
 for O0OoOO , I1Ii , url in IIIII11I1IiI :
  I11I1IIiiII1 ( I1Ii , url , 222 , ii11iIi1I + 'streams.png' )
  if 72 - 72: i1I111ii1II1i % i1I111ii1II1i / OOOo0
  if 40 - 40: Oo - Oo000 + OoO0O0 - OOooOOo % OOOo0 . II11i1iIiII1
def Ii1iii ( ) :
 O00Oo000ooO0 ( '[COLORgreen]CATAGORIES[/COLOR]' , '' , 10051 , ii11iIi1I + 'loader.png' , i1iiIII111ii , '' )
 O00Oo000ooO0 ( '[COLORgreen]SEARCH[/COLOR]' , '' , 10052 , ii11iIi1I + 'loader.png' , i1iiIII111ii , '' )
 if 94 - 94: II11i1iIiII1 % iI % i1IIi
 if 90 - 90: i1I111ii1II1i * Ooo00oOo00o
o0oO0 = xbmcaddon . Addon ( id = 'plugin.video.GenieTv' )
oOOoo00O0O = xbmcgui . Dialog ( )
oooOOOOO = xbmc . translatePath ( 'special://home/' )
Oo0oO0ooo = xbmcgui . DialogProgress ( )
I1i = 'https://addons.tvaddons.ag/'
if 77 - 77: OoO0O0 * Oo000 / II11i1iIiII1 + ii11ii1ii
def iiii11i ( ) :
 i1111I1I = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oOOoo00O00o = i1111I1I . lower ( )
 iIiIi1IiIi1iI = 'https://addons.tvaddons.ag/search/?keyword=' + oOOoo00O00o
 III1IiiI = iIi1 ( iIiIi1IiIi1iI )
 IIIII11I1IiI = re . compile ( '<li><a href="(.+?)"><span class=".+?"><img src="(.+?)" width=".+?" alt=".+?" class=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( III1IiiI )
 for OOOooo , ooo , I1Ii in IIIII11I1IiI :
  O00Oo000ooO0 ( I1Ii , OOOooo , 10054 , 'https://addons.tvaddons.ag/' + ooo , i1iiIII111ii , '' )
  if 59 - 59: i1IIi % Ooo0OO0 % Ooo00oOo00o + OOooOOo
  if 8 - 8: OoO0O0 % OOO0OOO00oo
def IIIIIiiI ( ) :
 III1IiiI = iIi1 ( I1i )
 IIIII11I1IiI = re . compile ( '<li><a href="(.+?)"><span class="thumbnail"><img src="(.+?)" class="pic" alt=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( III1IiiI )
 for OOOooo , OO0O000 , I1Ii in IIIII11I1IiI :
  if 'Repositories' in I1Ii :
   pass
  elif 'Services' in I1Ii :
   pass
  elif 'International' in I1Ii :
   pass
  else :
   O00Oo000ooO0 ( '[COLORgreen]' + I1Ii + '[/COLOR]' , OOOooo , 10053 , 'https://addons.tvaddons.ag/' + OO0O000 , i1iiIII111ii , '' )
   if 38 - 38: O0
   if 79 - 79: i1IIi . OOO0OOO00oo
def Addon ( url ) :
 III1IiiI = iIi1 ( url )
 i1i1i11iI11II = re . compile ( '<li class="nextPage"><a class=".+?" href="(.+?)"><dfn title="next Page">.+?</dfn></a></li>' ) . findall ( III1IiiI )
 for url in i1i1i11iI11II :
  O00Oo000ooO0 ( '[COLORgreen]NEXT PAGE[/COLOR]' , 'https://addons.tvaddons.ag' + url , 10053 , ii11iIi1I + 'Next.png' , i1iiIII111ii , '' )
 IIIII11I1IiI = re . compile ( '<li><a href="(.+?)"><span class=".+?"><img src="(.+?)" width=".+?" alt=".+?" class=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( III1IiiI )
 for url , OO0O000 , I1Ii in IIIII11I1IiI :
  if 'Please' in I1Ii :
   pass
  else :
   O00Oo000ooO0 ( I1Ii , url , 10054 , 'https://addons.tvaddons.ag/' + OO0O000 , i1iiIII111ii , '' )
   if 6 - 6: I1IiI . OoOoOO00 * OOOo0 . OOOo0 / i1I111ii1II1i
   if 14 - 14: OoO0O0 % Ooo0OO0 - O0 / OoO0O0
def Oo00OOoO0oo ( url , name ) :
 III1IiiI = iIi1 ( url )
 IIIII11I1IiI = re . compile ( '<a href="(.+?)"' ) . findall ( III1IiiI )
 for url in IIIII11I1IiI :
  if 'plugin' in url :
   print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<' + url
   iIII = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
   Oo0oO0ooo = xbmcgui . DialogProgress ( )
   Oo0oO0ooo . create ( "Origin+Jaybox" , "Downloading Content" , '' , 'Please Wait' )
   IiIi1i1ii = os . path . join ( iIII , name + '.zip' )
   try :
    os . remove ( IiIi1i1ii )
   except :
    pass
   downloader . download ( url , IiIi1i1ii , Oo0oO0ooo )
   II1II1iIIi11 = xbmc . translatePath ( os . path . join ( 'special://home' , 'addons' ) )
   time . sleep ( 2 )
   Oo0oO0ooo . update ( 0 , "" , "Extracting Zip Please Wait" )
   print '======================================='
   print II1II1iIIi11
   print '======================================='
   extract . all ( IiIi1i1ii , II1II1iIIi11 , Oo0oO0ooo )
   OOOOOoo0 ( )
   if 4 - 4: Ooo00oOo00o - OoOo00o / i11iIiiIii * O0
def OOOOOoo0 ( ) :
 xbmc . executebuiltin ( 'UpdateLocalAddons' )
 xbmc . executebuiltin ( 'UpdateAddonRepos' )
 i1iiIIiiI111 = xbmcgui . Dialog ( )
 i1iiIIiiI111 . ok ( "Origin + Genie TV" , '' , '                                 REFRESH SUCCESSFUL :)' , "                          [COLOR gold]Brought To You By Origin + Jaybox[/COLOR]" )
 return
 if 78 - 78: Ooo0OO0 - iI % O0 - Oo000 % Ooo00oOo00o
 if 43 - 43: Ooo00oOo00o
def OoOooO ( ) :
 i1I1i1 = O0OoooO0 ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvc2NyYXBlZC9jYXRzLnBocA==' ) )
 IIIII11I1IiI = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( i1I1i1 )
 for OOOooo , ooo , I1Ii in IIIII11I1IiI :
  iII11I1Ii1 ( I1Ii , OOOooo , 1007 , ooo )
def I1I1i11iiiiI ( url ) :
 i1I1i1 = O0OoooO0 ( url )
 IIIII11I1IiI = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( i1I1i1 )
 for url , ooo , I1Ii in IIIII11I1IiI :
  iII11I1Ii1 ( '[COLORgreen]' + I1Ii + '[/COLOR]' , url , 1006 , ooo )
  if 66 - 66: OOO0OOO00oo / I1IiI
  if 13 - 13: OoOoOO00
def oO0o000oOO ( url ) :
 i1I1i1 = O0OoooO0 ( url )
 IIIII11I1IiI = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( i1I1i1 )
 for url , ooo0O0o00O , oo0o , I1i11 , I1Ii in IIIII11I1IiI :
  if '.php' in url :
   ooOOOoOoOOO0 ( I1Ii , url , 1016 , ooo0O0o00O , I1i11 , oo0o )
  else :
   if 'youtube' in url :
    III1I11i1iIi ( I1Ii , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , ooo0O0o00O , I1i11 , oo0o )
   else :
    III1I11i1iIi ( I1Ii , url , 222 , ooo0O0o00O , I1i11 , oo0o )
    ii111 ( 'movies' , 'INFO' )
    if 27 - 27: O0 - iI * OoOoOO00 - iIii1I11I1II1 / II11i1iIiII1
 else :
  IIIII11I1IiI = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( i1I1i1 )
  for url , ooo , I1Ii in IIIII11I1IiI :
   if '.php' in url :
    iII11I1Ii1 ( I1Ii , url , 1016 , ooo )
   else :
    if 'youtube' in url :
     print '>>>>>>>>>>>>>>>>>>>>>>> youtube old way'
     I11I1IIiiII1 ( I1Ii , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , ooo )
    else :
     I11I1IIiiII1 ( I1Ii , url , 222 , ooo )
     ii111 ( 'movies' , 'INFO' )
     if 24 - 24: Oo / iIii1I11I1II1 % Oo000 * I1IiI - iIii1I11I1II1
  xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 50 - 50: OoOoOO00
def IiIIiiiIi ( ) :
 i1I1i1 = O0OoooO0 ( i1111 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vdm9kL3VybHMvdXJsLnBocA==' ) )
 IIIII11I1IiI = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( i1I1i1 )
 for OOOooo , ooo , I1Ii in IIIII11I1IiI :
  iII11I1Ii1 ( I1Ii , OOOooo , 1007 , ooo )
def IiI111 ( url ) :
 i1I1i1 = O0OoooO0 ( url )
 IIIII11I1IiI = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( i1I1i1 )
 for url , ooo , I1Ii in IIIII11I1IiI :
  iII11I1Ii1 ( '[COLORgreen]' + I1Ii + '[/COLOR]' , url , 1006 , ooo )
  if 82 - 82: OOOo0 % Ooo00oOo00o % iI + iI
def i1111I ( name , url , iconimage = None ) :
 print '--- Playing "{0}". {1}' . format ( name , url )
 OoO00oo0 = xbmcgui . ListItem ( path = url , thumbnailImage = iconimage )
 OoO00oo0 . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , OoO00oo0 )
 if 96 - 96: i1IIi
 if 55 - 55: OOO0OOO00oo + Oo000 + i1I111ii1II1i
def OOoiII1I1i ( url ) :
 i1I1i1 = O0OoooO0 ( url )
 IIIII11I1IiI = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( i1I1i1 )
 for url , OO0O000 , I1Ii in IIIII11I1IiI :
  iII11I1Ii1 ( '[COLORgreen]' + I1Ii + '[/COLOR]' , url , 1006 , OO0O000 )
def IIiii ( url ) :
 i1I1i1 = O0OoooO0 ( url )
 IIIi = url
 IIIII11I1IiI = re . compile ( "<a href='(.+?)'>(.+?)</a>" ) . findall ( i1I1i1 )
 for url , I1Ii in IIIII11I1IiI :
  if '.mp3' in I1Ii :
   print '<<<<<<<<<<<<<<<<<<<' + url + '>>>>>>>>>>>>>>>>>>>>>>>>>>>'
   I11I1IIiiII1 ( ( I1Ii ) . replace ( '.mp3' , '' ) . replace ( '/' , '' ) , 'http://hypem.com' + url , 222 , ii11iIi1I + 'music.png' )
  else :
   iII11I1Ii1 ( ( I1Ii ) . replace ( '/' , '' ) , IIIi + url , 1011 , ii11iIi1I + 'music.png' )
def ooOoOooo00Oo ( ) :
 i1I1i1 = O0OoooO0 ( i1111 ( 'aHR0cDovL3d3dy5jeW4ubmV0L211c2ljLw==' ) )
 IIIII11I1IiI = re . compile ( '<td><a href="(.+?)"><img src="(.+?)"><br>(.+?)</a></td>' , re . DOTALL ) . findall ( i1I1i1 )
 for OOOooo , OO0O000 , I1Ii in IIIII11I1IiI :
  iII11I1Ii1 ( I1Ii , ( 'http://www.cyn.net/music/' + OOOooo ) . replace ( ' ' , '%20' ) , 1031 , ( 'http://www.cyn.net/music/' + OO0O000 ) . replace ( ' ' , '%20' ) )
def ooo00O0OOo ( url , img ) :
 i1I1i1 = O0OoooO0 ( url )
 ooI1111i = url
 img = img
 IIIII11I1IiI = re . compile ( '<a href="(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( i1I1i1 )
 for url , I1Ii in IIIII11I1IiI :
  I11I1IIiiII1 ( ( I1Ii ) . replace ( '.mp3' , '' ) , ( ooI1111i + '/' + url ) . replace ( ' ' , '%20' ) , 222 , img )
  if 45 - 45: OOOo0 / OoOo00o + OOO0OOO00oo + Ooo0OO0
  if 15 - 15: OOOo0 % Ooo00oOo00o
def oOoo00oO0O0OO ( ) :
 II11iiii = ( i1111 ( 'aHR0cDovL2h5cGVtLmNvbS9kb3dubG9hZC8=' ) )
 i1111I1I = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oOOoo00O00o = i1111I1I . lower ( )
 OOOooo = ( i1111 ( 'aHR0cDovL3Bhbmljc3RyZWFtLm5ldC9zdHJlYW1zLw==' ) )
 ooI1111i = ( i1111 ( 'aHR0cDovL21hc2xvdmQubm8taXAub3JnL3B1YmxpYy9tcDMv' ) )
 o00O0O = ( i1111 ( 'aHR0cDovL3d3dy5jeW4ubmV0L211c2ljLw==' ) )
 if 35 - 35: i11iIiiIii % iI
 III1IiiI = oOIii11111iiI ( OOOooo )
 II11IiIi11 = oOIii11111iiI ( ooI1111i )
 IiiIIi = oOIii11111iiI ( o00O0O )
 if 39 - 39: O0 . i1IIi * ii11ii1ii - Ooo00oOo00o - OoOo00o % OOooOOo
 if III1IiiI != 'Failed' :
  IIIII11I1IiI = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( III1IiiI )
  for I1Ii in IIIII11I1IiI :
   if i1111I1I in I1Ii . lower ( ) :
    iII11I1Ii1 ( ( I1Ii + ' source 1' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( OOOooo + I1Ii ) . replace ( ' ' , '%20' ) , 1006 , '' )
    if 6 - 6: Ooo00oOo00o - OoOo00o / OoOoOO00
    ii111 ( 'tvshows' , 'Media Info 3' )
 if II11IiIi11 != 'Failed' :
  IIOOO0O00O0OOOO = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( III1IiiI )
  for I1Ii in IIOOO0O00O0OOOO :
   if i1111I1I in I1Ii . lower ( ) :
    iII11I1Ii1 ( ( I1Ii + ' source 2' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( ooI1111i + I1Ii ) . replace ( ' ' , '%20' ) , 1006 , '' )
    if 25 - 25: Oo % I1IiI
    ii111 ( 'tvshows' , 'Media Info 3' )
 if IiiIIi != 'Failed' :
  iI1I11iIIi1 = re . compile ( '<td><a href=".+?"><img src=".+?"><br>(.+?)</a></td>' , re . DOTALL ) . findall ( IiiIIi )
  for I1Ii in iI1I11iIIi1 :
   if i1111I1I in I1Ii . lower ( ) :
    iII11I1Ii1 ( ( I1Ii + ' source 3' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( o00O0O + I1Ii ) . replace ( ' ' , '%20' ) , 1031 , '' )
    if 75 - 75: i1IIi
    ii111 ( 'tvshows' , 'Media Info 3' )
    if 74 - 74: Oo + OoO0O0 - OOO0OOO00oo - Ooo00oOo00o + OoOo00o - iIii1I11I1II1
    if 54 - 54: ii11ii1ii + OoOoOO00 . OOOo0 / Ooo00oOo00o . II11i1iIiII1
    if 58 - 58: Ooo0OO0 % i11iIiiIii * OoOoOO00 . ii11ii1ii
    if 94 - 94: i11iIiiIii . Oo000 + iIii1I11I1II1 * OoO0O0 * OoO0O0
    if 36 - 36: iI - Ooo0OO0 . Ooo0OO0
    if 60 - 60: i11iIiiIii * Oo % Ooo00oOo00o + Ooo00oOo00o
def ooo000o ( ) :
 i1I1i1 = iIi1 ( 'http://www.iwatchseries.me/tv-list/' )
 IIIII11I1IiI = re . compile ( '<h5><a href="([^"]*)"><strong>(.+?)</strong></a></h5>' ) . findall ( i1I1i1 )
 for OOOooo , I1Ii in IIIII11I1IiI :
  iII11I1Ii1 ( I1Ii , OOOooo , 8021 , ii11iIi1I + 'iwatch.png' )
def OOOOOO ( url ) :
 i1I1i1 = iIi1 ( url )
 IIIII11I1IiI = re . compile ( '<h5><strong><a href="([^"]*)">(.+?)</a>(.+?)</strong></h5>' ) . findall ( i1I1i1 )
 for url , I1Ii , IIIII1 in IIIII11I1IiI :
  iII11I1Ii1 ( I1Ii + IIIII1 , url , 8022 , ii11iIi1I + 'iwatch.png' )
def oOO0O ( url ) :
 i1I1i1 = iIi1 ( url )
 IIIII11I1IiI = re . compile ( '<iframe src="([^"]*)"' ) . findall ( i1I1i1 )
 for url in IIIII11I1IiI :
  print '>>>>>>>>>>>>>>>>>>>>' + url
  oooo0 ( url )
def oooo0 ( url ) :
 i1I1i1 = iIi1 ( url )
 IIIII11I1IiI = re . compile ( '{.+?"file" : "(.+?)",.+?"default" : true.+?"label" : "(.+?)"' , re . DOTALL ) . findall ( i1I1i1 )
 IIOOO0O00O0OOOO = re . compile ( 'setup\(\{.+?file: "(.+?)",.+?skin' , re . DOTALL ) . findall ( i1I1i1 )
 iI1I11iIIi1 = re . compile ( "{ label: '([^']*)', file:.+?'([^']*)' }" ) . findall ( i1I1i1 )
 for url , I1Ii in IIIII11I1IiI :
  I11I1IIiiII1 ( 'VidSpot - ' + I1Ii , url , 222 , ii11iIi1I + 'iwatch.png' )
 for url in IIOOO0O00O0OOOO :
  I11I1IIiiII1 ( 'VodLocker' , url , 222 , ii11iIi1I + 'iwatch.png' )
 for I1Ii , url in iI1I11iIIi1 :
  print '<><><><><><><><><><><> before   ' + url
  if 'hevideo' in url :
   print '>>>>>>>>>>>>>>>>>>>>>>>>>' + url
   I11I1IIiiII1 ( 'TheVideo - ' + I1Ii , url , 222 , ii11iIi1I + 'iwatch.png' )
   if 74 - 74: OOooOOo / OOO0OOO00oo - OoOoOO00 . OoOoOO00 . Ooo0OO0 + OoOoOO00
def O0Ooo00o00O ( ) :
 i1I1i1 = cloudflare . source ( 'http://www.animeland.me/anime-list' )
 IIIII11I1IiI = re . compile ( 'letter-spacing:-1px;" href="([^"]*)">(.+?)</a></li>' ) . findall ( i1I1i1 )
 for OOOooo , I1Ii in IIIII11I1IiI :
  iII11I1Ii1 ( I1Ii , OOOooo , 1021 , ii11iIi1I + 'anime.png' )
  if 80 - 80: OoOo00o
  if 3 - 3: ii11ii1ii * iI
def Oo00O ( ) :
 i1I1i1 = iIi1 ( 'http://www.animetoon.org/cartoon' )
 IIIII11I1IiI = re . compile ( '<td><a href="(.+?)">(.+)</a></td>' ) . findall ( i1I1i1 )
 for OOOooo , I1Ii in IIIII11I1IiI :
  iII11I1Ii1 ( I1Ii , OOOooo , 1002 , ii11iIi1I + 'anime.png' )
  if 44 - 44: II11i1iIiII1 * iI
  if 12 - 12: i1I111ii1II1i . OOOo0 % OOooOOo
  if 28 - 28: i1I111ii1II1i - OOOo0 % Ooo00oOo00o * OoO0O0
def oO0oOooO00oo ( url ) :
 i1I1i1 = iIi1 ( url )
 IIOOO0O00O0OOOO = re . compile ( '<img src="(.+?)" id="series_image" width="250" height="370" alt=".+?" />' ) . findall ( i1I1i1 )
 for OO0O000 in IIOOO0O00O0OOOO :
  i111i11I1Ii1I = OO0O000
 iI1I11iIIi1 = re . compile ( '<li><a href="(.+?)">Next</a></li>' ) . findall ( i1I1i1 )
 for url in iI1I11iIIi1 :
  iII11I1Ii1 ( 'NEXT PAGE' , url , 1002 , ii11iIi1I + 'Next.png' )
 IIIII11I1IiI = re . compile ( '&nbsp;<a href="(.+?)">(.+?)</a>' ) . findall ( i1I1i1 )
 for url , I1Ii in IIIII11I1IiI :
  iII11I1Ii1 ( I1Ii , url , 1003 , i111i11I1Ii1I )
 xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
def Oo000oO ( url , IMAGE ) :
 i1I1i1 = iIi1 ( url )
 IIIII11I1IiI = re . compile ( '"playlist">(.+?)</span></div><div><iframe src="(.+?)"' ) . findall ( i1I1i1 )
 for I1Ii , url in IIIII11I1IiI :
  print I1Ii + '     ' + url
  if 'easy' in url :
   iiIIIII ( url )
  elif 'playpanda' in url :
   iiIIIII ( url )
   if 19 - 19: OoOoOO00 / I1IiI
  xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
def iiIIIII ( url ) :
 i1I1i1 = iIi1 ( url )
 IIIII11I1IiI = re . compile ( "url: '(.+?)'," ) . findall ( i1I1i1 )
 for url in IIIII11I1IiI :
  I11I1IIiiII1 ( 'STREAM' , url , 222 , ii11iIi1I + 'anime.png' )
  if 80 - 80: I1IiI + iIii1I11I1II1 . Ooo0OO0
  if 76 - 76: OOOo0 * Oo000
def ii111IIiiI11 ( url ) :
 o0OOOOoO = urllib2 . Request ( url )
 o0OOOOoO . add_header ( 'User-Agent' , "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0" )
 o0OOOOoO . add_header ( 'referer' , url )
 OoO0Ooo = urllib2 . urlopen ( o0OOOOoO )
 iI1I1i11iIIii = OoO0Ooo . read ( )
 OoO0Ooo . close ( )
 return iI1I1i11iIIii
 if 7 - 7: OOOo0 / Ooo00oOo00o + OoO0O0 + iI / OOOo0
def O0OoooO0 ( url ) :
 o0OOOOoO = urllib2 . Request ( url )
 o0OOOOoO . add_header ( 'User-Agent' , "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0" )
 OoO0Ooo = urllib2 . urlopen ( o0OOOOoO )
 iI1I1i11iIIii = OoO0Ooo . read ( )
 OoO0Ooo . close ( )
 return iI1I1i11iIIii
 if 82 - 82: ii11ii1ii + OoooooooOO
def IIiIi11i111II ( url ) :
 xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
 IiI1IIIII1I = ( '%s%s' % ( I1I1IiIi1 , url ) )
 iI1I1i11iIIii = O0OoooO0 ( url )
 IIIII11I1IiI = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( iI1I1i11iIIii )
 for url , ooo , I1Ii in IIIII11I1IiI :
  I11I1IIiiII1 ( '%s' % ( I1Ii ) . replace ( 'GenieTv' , '[COLOR green]GenieTV[/COLOR]' ) . replace ( '.' , ' ' ) . replace ( 'mp4' , '' ) . replace ( 'mkv' , '' ) . replace ( '_' , ' ' ) , '%s' % ( url ) , 222 , ooo )
  if 52 - 52: OoooooooOO / Ooo0OO0 - i1IIi
def iIIii ( url ) :
 iiiiI1iiiIi = xbmc . Player ( iiI1iI ( ) )
 import urlresolver
 try : iiiiI1iiiIi . play ( url )
 except : pass
 from urlresolver import common
 Oo0oO0ooo = xbmcgui . DialogProgress ( )
 Oo0oO0ooo . create ( 'LOADING' , 'Opening %s Now' % ( I1Ii ) )
 iiiiI1iiiIi = xbmc . Player ( iiI1iI ( ) )
 url = urlresolver . HostedMediaFile ( url ) . resolve ( )
 if Oo0oO0ooo . iscanceled ( ) :
  print "[COLORred]STREAM CANCELLED[/COLOR]"
  i1iiIIiiI111 = xbmcgui . Dialog ( )
  if i1iiIIiiI111 . yesno ( "[B]CANCELLED[/B]" , '[B]Was There A Problem[/B]' , '' , "" , 'Yes' , 'No' ) :
   i1iiIIiiI111 . ok ( "Message Send" , "Your Message Has Been Sent" )
  else :
   return
 else :
  try : iiiiI1iiiIi . play ( url )
  except : pass
  try : o0oO0 . resolve_url ( url )
  except : pass
  Oo0oO0ooo . close ( )
  if 81 - 81: i1IIi / OoO0O0 % i11iIiiIii . iIii1I11I1II1 * I1IiI + OoooooooOO
def iiii1Ii1iii ( url ) :
 Oo0oO0ooo = xbmcgui . DialogProgress ( )
 Oo0oO0ooo . create ( 'Featching Your Video' , 'Featching Your Video' )
 Oo0oO0ooo . update ( 0 , '%s' % I1Ii )
 xbmc . sleep ( 1 )
 iiiiI1iiiIi = xbmc . Player ( iiI1iI ( ) )
 Oo0oO0ooo . update ( 100 , '%s' % I1Ii )
 xbmc . sleep ( 1 )
 iiiiI1iiiIi . play ( url ) . strip ( )
 Oo0oO0ooo . close ( )
 if 73 - 73: i11iIiiIii + OOO0OOO00oo % iI . OoooooooOO % OOO0OOO00oo
def Oo0oOooOoOo ( url ) :
 iiiiI1iiiIi = xbmc . Player ( iiI1iI ( ) )
 import urlresolver
 url = ( url ) . strip ( )
 try : iiiiI1iiiIi . play ( url ) . strip ( )
 except : pass
 if 32 - 32: i11iIiiIii - OoOoOO00
 if 21 - 21: I1IiI - OoOoOO00
def iiI1iI ( ) :
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
def iII11I1Ii1 ( name , url , mode , iconimage , showcontext = True , allinfo = { } ) :
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
def oOo00oOOOOO ( name , url , mode , iconimage , fanart , description ) :
 if 57 - 57: Oo000 . i1I111ii1II1i % OOooOOo
 I11Oo0oO00 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 IiiI1III1I1 = True
 o0OoOoo00O = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 o0OoOoo00O . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 o0OoOoo00O . setProperty ( "Fanart_Image" , fanart )
 IiiI1III1I1 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = I11Oo0oO00 , listitem = o0OoOoo00O , isFolder = True )
 return IiiI1III1I1
 if 32 - 32: iI / Ooo0OO0 - O0 * iIii1I11I1II1
def I11I1IIiiII1 ( name , url , mode , iconimage , showcontext = True , allinfo = { } ) :
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
 if 18 - 18: iI + Oo - Ooo00oOo00o / OoO0O0 / Oo000
 if 53 - 53: Oo000 + OOooOOo . OOO0OOO00oo / iI
 if 52 - 52: OoO0O0 + OoO0O0
 if 73 - 73: OOooOOo . i11iIiiIii % OoooooooOO + II11i1iIiII1 . OoooooooOO / Oo000
def Iiii ( heading , announce ) :
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
   try : Iii = open ( announce ) ; IiIIii = Iii . read ( )
   except : IiIIii = announce
   self . win . getControl ( self . CONTROL_TEXTBOX ) . setText ( str ( IiIIii ) )
   return
 oOiiI1i11I ( )
 oOiiI1i11I ( )
 if 74 - 74: iIii1I11I1II1 / i1I111ii1II1i
def O0Oo0Oo00o0o ( ) :
 Iiii ( 'These are the main Sources you should get into you XBMC' , '[COLORwhite]http://architects.x10host.com[/COLOR]--- [CR]  [COLORred]http://repo.sharktech.co.uk[/COLOR]--- [CR]   [COLORwhite]http://fusion.tvaddons.ag[/COLOR]--- [CR]  [COLORred]http://i.totalxbmc.tv[/COLOR]--- [CR]   [COLORwhite]http://www.xunitytalk.com/xfinity[/COLOR]--- [CR]  [COLORred]http://srp.nu[/COLOR]--- [CR]   [COLORwhite]http://solved.no-issue.ca[/COLOR]--- [CR]  [COLORred]http://xbmc.aminhacasadigital.com[/COLOR]--- [CR]   [COLORwhite]http://xbmc.movieshd.co[/COLOR]--- [CR]  [COLORred]http://install.kaosbox.tv[/COLOR]--- [CR]   [COLORwhite]http://kodi-repo.com/mxr[/COLOR]--- [CR]  [COLORred]http://kodi.metalkettle.co[/COLOR]--- [CR]   [COLORwhite]http://prozone.getxbmc.com[/COLOR]--- [CR]  [COLORred]http://transform.mega-tron.tv[/COLOR]--- [CR]   [COLORwhite]http://muckys.kodimediaportal.ml[/COLOR]--- [CR]  [COLORred]http://jas0npc.pcriot.com[/COLOR]--- [CR]  [COLORwhite]Sports devil source[/COLOR]--- [CR]  [COLORred]http://iwillfolo.com/iwf[/COLOR]' )
 if 17 - 17: Ooo0OO0 / OOooOOo . Oo000 + OOooOOo / ii11ii1ii . Oo
 if 39 - 39: OOooOOo / Ooo0OO0 - OoOo00o
 if 96 - 96: iI * ii11ii1ii * i1I111ii1II1i + ii11ii1ii % OOOo0 + i11iIiiIii
 if 37 - 37: iI % ii11ii1ii / II11i1iIiII1
 if 94 - 94: iI / Ooo00oOo00o . OOooOOo
def OOOOOoo0 ( ) :
 xbmc . executebuiltin ( 'UpdateLocalAddons' )
 xbmc . executebuiltin ( 'UpdateAddonRepos' )
 i1iiIIiiI111 = xbmcgui . Dialog ( )
 i1iiIIiiI111 . ok ( "GenieTv" , '' , '                                 REFRESH SUCCESSFUL :)' , "                          [COLOR gold]Brought To You By Kodi Support Group, GenieTv[/COLOR]" )
 return
 if 1 - 1: Oo . OoOoOO00
 if 93 - 93: OoOoOO00 . i11iIiiIii + OoOoOO00 % OOO0OOO00oo
 if 98 - 98: OoO0O0 * OOO0OOO00oo * I1IiI + i1I111ii1II1i * OoOo00o
 if 4 - 4: Ooo0OO0
 if 16 - 16: iIii1I11I1II1 * OoOo00o + OOO0OOO00oo . O0 . OOooOOo
 if 99 - 99: i11iIiiIii - OoOo00o
 if 85 - 85: OoO0O0 % ii11ii1ii
 if 95 - 95: Ooo00oOo00o * Oo000 * OoOo00o . OOooOOo
 if 73 - 73: Ooo00oOo00o
 if 28 - 28: OoooooooOO - iI
 if 84 - 84: OoOoOO00
 if 36 - 36: Oo000 - I1IiI - iIii1I11I1II1
 if 10 - 10: ii11ii1ii / i1I111ii1II1i * i1IIi % O0 + iI
 if 25 - 25: OoO0O0 - i1I111ii1II1i / O0 . OoooooooOO % OOOo0 . i1IIi
 if 19 - 19: OoOoOO00 / OoOoOO00 % ii11ii1ii + OOO0OOO00oo + OOO0OOO00oo + OoOo00o
 if 4 - 4: OOooOOo + iI / OoOo00o + i1IIi % OOooOOo % OoOo00o
 if 80 - 80: i1I111ii1II1i
 if 26 - 26: iIii1I11I1II1 . OoooooooOO - iIii1I11I1II1
 if 59 - 59: ii11ii1ii + iI . OOO0OOO00oo
 if 87 - 87: Ooo00oOo00o
 if 34 - 34: OoO0O0 . I1IiI / i11iIiiIii / OoOo00o
 if 46 - 46: Oo + OoOoOO00 * OOOo0 + Oo000
 if 31 - 31: i1I111ii1II1i * OOooOOo * i1I111ii1II1i + Ooo00oOo00o * OOooOOo . OoO0O0
 if 89 - 89: OoooooooOO * i1I111ii1II1i * OOOo0 . II11i1iIiII1 * i1I111ii1II1i / OoOo00o
def iioo ( url ) :
 iI1I1i11iIIii = iIi1 ( iiI1IiI + i11I ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIIII11I1IiI = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( iI1I1i11iIIii )
 for I1Ii , url , ooo0O0o00O , I1i11 , OOo0 in IIIII11I1IiI :
  O00Oo000ooO0 ( I1Ii , url , 42 , ooo0O0o00O , I1i11 , OOo0 )
 ii111 ( 'movies' , 'MAIN' )
 if 48 - 48: Oo000 + OoO0O0 % Oo000
def Ooo0o0000OO ( url ) :
 iI1I1i11iIIii = iIi1 ( iiI1IiI + iIiI1II1I1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIIII11I1IiI = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( iI1I1i11iIIii )
 for I1Ii , url , ooo0O0o00O , I1i11 , OOo0 in IIIII11I1IiI :
  O00Oo000ooO0 ( I1Ii , url , 42 , ooo0O0o00O , I1i11 , OOo0 )
 ii111 ( 'movies' , 'MAIN' )
 if 92 - 92: OoooooooOO . Ooo00oOo00o / Oo000 + Ooo00oOo00o
def ii1Ii11Ii1i ( url ) :
 iI1I1i11iIIii = iIi1 ( iiI1IiI + OooO0O0oo ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIIII11I1IiI = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( iI1I1i11iIIii )
 for I1Ii , url , ooo0O0o00O , I1i11 , OOo0 in IIIII11I1IiI :
  O00Oo000ooO0 ( I1Ii , url , 42 , ooo0O0o00O , I1i11 , OOo0 )
 ii111 ( 'movies' , 'MAIN' )
 if 64 - 64: I1IiI % I1IiI + OOooOOo + Oo
def OO0oO0Oo ( url ) :
 iI1I1i11iIIii = iIi1 ( iiI1IiI + OoooOO0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIIII11I1IiI = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( iI1I1i11iIIii )
 for I1Ii , url , ooo0O0o00O , I1i11 , OOo0 in IIIII11I1IiI :
  O00Oo000ooO0 ( I1Ii , url , 42 , ooo0O0o00O , I1i11 , OOo0 )
 ii111 ( 'movies' , 'MAIN' )
 if 69 - 69: OoOoOO00 + OoOo00o
def oooOOO ( url ) :
 iI1I1i11iIIii = iIi1 ( iiI1IiI + Iii1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIIII11I1IiI = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( iI1I1i11iIIii )
 for I1Ii , url , ooo0O0o00O , I1i11 , OOo0 in IIIII11I1IiI :
  O00Oo000ooO0 ( I1Ii , url , 42 , ooo0O0o00O , I1i11 , OOo0 )
 ii111 ( 'movies' , 'MAIN' )
 if 64 - 64: II11i1iIiII1 / i1IIi % OoOo00o
def OOoOo0O0 ( url ) :
 iI1I1i11iIIii = iIi1 ( iiI1IiI + I1o0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIIII11I1IiI = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( iI1I1i11iIIii )
 for I1Ii , url , ooo0O0o00O , I1i11 , OOo0 in IIIII11I1IiI :
  O00Oo000ooO0 ( I1Ii , url , 42 , ooo0O0o00O , I1i11 , OOo0 )
 ii111 ( 'movies' , 'MAIN' )
 if 26 - 26: OoOo00o * iIii1I11I1II1 + OoOoOO00 / OOOo0
def O0OOo0o0O00oOo ( url ) :
 iI1I1i11iIIii = iIi1 ( iiI1IiI + iI1ii ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIIII11I1IiI = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( iI1I1i11iIIii )
 for I1Ii , url , ooo0O0o00O , I1i11 , OOo0 in IIIII11I1IiI :
  O00Oo000ooO0 ( I1Ii , url , 42 , ooo0O0o00O , I1i11 , OOo0 )
 ii111 ( 'movies' , 'MAIN' )
 if 2 - 2: OoOoOO00 . iI
def OoO0oOOOO ( url ) :
 iI1I1i11iIIii = iIi1 ( iiI1IiI + o0oo00OOOo ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIIII11I1IiI = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( iI1I1i11iIIii )
 for I1Ii , url , ooo0O0o00O , I1i11 , OOo0 in IIIII11I1IiI :
  O00Oo000ooO0 ( I1Ii , url , 42 , ooo0O0o00O , I1i11 , OOo0 )
 ii111 ( 'movies' , 'MAIN' )
 if 99 - 99: OOOo0 / i11iIiiIii % OOO0OOO00oo
def i1i1IIi ( url ) :
 iI1I1i11iIIii = iIi1 ( iiI1IiI + o0oo0Ooo0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIIII11I1IiI = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( iI1I1i11iIIii )
 for I1Ii , url , ooo0O0o00O , I1i11 , OOo0 in IIIII11I1IiI :
  O00Oo000ooO0 ( I1Ii , url , 42 , ooo0O0o00O , I1i11 , OOo0 )
 ii111 ( 'movies' , 'MAIN' )
 if 74 - 74: i1I111ii1II1i + ii11ii1ii + OOOo0
def i11iII1II1I1 ( url ) :
 iI1I1i11iIIii = iIi1 ( iiI1IiI + iIIi1II1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIIII11I1IiI = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( iI1I1i11iIIii )
 for I1Ii , url , ooo0O0o00O , I1i11 , OOo0 in IIIII11I1IiI :
  O00Oo000ooO0 ( I1Ii , url , 5 , ooo0O0o00O , I1i11 , OOo0 )
 ii111 ( 'movies' , 'MAIN' )
 if 42 - 42: iIii1I11I1II1 - II11i1iIiII1 - iI - OoO0O0
 if 33 - 33: I1IiI - O0
 if 38 - 38: Oo000 * Ooo0OO0 - OoooooooOO * Ooo0OO0 + OoooooooOO
 if 94 - 94: OoOoOO00 / i1IIi * i1IIi + II11i1iIiII1 - II11i1iIiII1 % OOooOOo
 if 12 - 12: OoO0O0 / I1IiI . i11iIiiIii * i11iIiiIii
 if 68 - 68: Ooo0OO0 * Ooo00oOo00o . iI / i1I111ii1II1i . OOooOOo - i11iIiiIii
 if 49 - 49: Oo / i1I111ii1II1i % iI + OOO0OOO00oo - Ooo00oOo00o
 if 13 - 13: OoOoOO00
 if 83 - 83: OoooooooOO . OOOo0 + i1I111ii1II1i * O0 / OOO0OOO00oo
def IiiiI11 ( ) :
 try :
  if os . path . exists ( oOOoO0 ) == True :
   i1iiIIiiI111 = xbmcgui . Dialog ( )
   if i1iiIIiiI111 . yesno ( "Delete Thumbnails" , "[COLOR gold][B]##########WARNING ANDROID ONLY##########[/B][/COLOR]" , "This feature deletes your thumbnail folder and textures13.db" , "Are you sure you want to do proceed? This Can NOT Be Undone" ) :
    for i1OoOO , IIIIIo0ooOoO000oO , OOo in os . walk ( oOOoO0 ) :
     OoooOOo0oOO = 0
     OoooOOo0oOO += len ( OOo )
     if OoooOOo0oOO > 0 :
      for Iii in OOo :
       os . unlink ( os . path . join ( i1OoOO , Iii ) )
  i1iiIIiiiI = os . path . join ( OOooO0OOoo , "Textures13.db" )
  os . unlink ( i1iiIIiiiI )
  i1iiIIiiI111 . ok ( "Restart KODI" , "Please restart KODI to rebuild thumbnail library" )
 except :
  i1iiIIiiI111 = xbmcgui . Dialog ( )
  i1iiIIiiI111 . ok ( o0oOoO00o , "Error Deleting Thumbnails please visit Kodi Support Group, GenieTv on facebook" )
 return
 if 26 - 26: II11i1iIiII1 % OOO0OOO00oo + OOOo0 / Ooo0OO0 . OOOo0
 if 38 - 38: OoooooooOO + OoooooooOO - i11iIiiIii * OOOo0 * i1IIi / OoOoOO00
 if 78 - 78: Oo - OoO0O0 + OoOo00o * i1I111ii1II1i * OOooOOo
 if 23 - 23: Oo - O0
 if 33 - 33: ii11ii1ii
 if 54 - 54: II11i1iIiII1 * ii11ii1ii . OoOoOO00 / Oo000 % Oo000
 if 25 - 25: i11iIiiIii + ii11ii1ii - OoooooooOO . O0 % OoO0O0
 if 53 - 53: i1IIi
 if 59 - 59: OOooOOo + OOOo0 % OoooooooOO - iIii1I11I1II1
def iiIII1i1 ( url ) :
 print '############################################################       DELETING STANDARD CACHE             ###############################################################'
 oOOo0OOoOO0 = os . path . join ( xbmc . translatePath ( 'special://home' ) , 'cache' )
 if os . path . exists ( oOOo0OOoOO0 ) == True :
  for i1OoOO , IIIIIo0ooOoO000oO , OOo in os . walk ( oOOo0OOoOO0 ) :
   OoooOOo0oOO = 0
   OoooOOo0oOO += len ( OOo )
   if 30 - 30: OoOoOO00 / OOOo0 - II11i1iIiII1 + I1IiI * II11i1iIiII1 / I1IiI
   if 17 - 17: Ooo00oOo00o
   if OoooOOo0oOO > 0 :
    if 31 - 31: OOO0OOO00oo + OoooooooOO - i1I111ii1II1i % OOooOOo / OOooOOo / iIii1I11I1II1
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    if i1iiIIiiI111 . yesno ( "Delete KODI Cache Files" , str ( OoooOOo0oOO ) + " files found" , "Do you want to delete them?" ) :
     if 31 - 31: OoooooooOO - i1I111ii1II1i . Ooo0OO0 % OOO0OOO00oo
     for Iii in OOo :
      try :
       os . unlink ( os . path . join ( i1OoOO , Iii ) )
      except :
       pass
     for I1iii11 in IIIIIo0ooOoO000oO :
      try :
       shutil . rmtree ( os . path . join ( i1OoOO , I1iii11 ) )
      except :
       pass
       if 16 - 16: Oo000 * i1I111ii1II1i % OoO0O0 / Ooo0OO0 + iIii1I11I1II1 / OOOo0
   else :
    pass
 if xbmc . getCondVisibility ( 'system.platform.ATV2' ) :
  IIII1I1 = os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'Other' )
  if 36 - 36: i1I111ii1II1i * iI . iI / Oo / OOOo0
  for i1OoOO , IIIIIo0ooOoO000oO , OOo in os . walk ( IIII1I1 ) :
   OoooOOo0oOO = 0
   OoooOOo0oOO += len ( OOo )
   if 80 - 80: OoooooooOO - i1IIi
   if OoooOOo0oOO > 0 :
    if 51 - 51: i1IIi . I1IiI / I1IiI % i11iIiiIii * Oo000 - OoO0O0
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    if i1iiIIiiI111 . yesno ( "Delete ATV2 Cache Files" , str ( OoooOOo0oOO ) + " files found in 'Other'" , "Do you want to delete them?" ) :
     if 49 - 49: Oo - iIii1I11I1II1
     for Iii in OOo :
      os . unlink ( os . path . join ( i1OoOO , Iii ) )
     for I1iii11 in IIIIIo0ooOoO000oO :
      shutil . rmtree ( os . path . join ( i1OoOO , I1iii11 ) )
      if 64 - 64: OoO0O0 + iIii1I11I1II1
   else :
    pass
  I1Iii = os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'LocalAndRental' )
  if 30 - 30: i1IIi . ii11ii1ii
  for i1OoOO , IIIIIo0ooOoO000oO , OOo in os . walk ( I1Iii ) :
   OoooOOo0oOO = 0
   OoooOOo0oOO += len ( OOo )
   if 77 - 77: OoOoOO00 - i11iIiiIii
   if OoooOOo0oOO > 0 :
    if 78 - 78: i1I111ii1II1i
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    if i1iiIIiiI111 . yesno ( "Delete ATV2 Cache Files" , str ( OoooOOo0oOO ) + " files found in 'LocalAndRental'" , "Do you want to delete them?" ) :
     if 72 - 72: OoO0O0 * Ooo00oOo00o
     for Iii in OOo :
      os . unlink ( os . path . join ( i1OoOO , Iii ) )
     for I1iii11 in IIIIIo0ooOoO000oO :
      shutil . rmtree ( os . path . join ( i1OoOO , I1iii11 ) )
      if 89 - 89: I1IiI + OOOo0
   else :
    pass
    if 68 - 68: iI / iIii1I11I1II1 . Oo + i11iIiiIii + OOooOOo
    if 92 - 92: Ooo00oOo00o . OOooOOo . i1I111ii1II1i % I1IiI
    if 58 - 58: ii11ii1ii % i1I111ii1II1i * i1I111ii1II1i - OoOo00o
    if 9 - 9: II11i1iIiII1 - i1I111ii1II1i % OoOoOO00 + Ooo0OO0 + Oo000 % O0
 o00OoOo0 = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.whatthefurk/cache' ) , '' )
 if os . path . exists ( o00OoOo0 ) == True :
  for i1OoOO , IIIIIo0ooOoO000oO , OOo in os . walk ( o00OoOo0 ) :
   OoooOOo0oOO = 0
   OoooOOo0oOO += len ( OOo )
   if 2 - 2: OoOoOO00 + i1IIi
   if 68 - 68: Oo000 + i1I111ii1II1i
   if OoooOOo0oOO > 0 :
    if 58 - 58: Ooo0OO0 * i1I111ii1II1i . i1IIi
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    if i1iiIIiiI111 . yesno ( "Delete WTF Cache Files" , str ( OoooOOo0oOO ) + " files found" , "Do you want to delete them?" ) :
     if 19 - 19: OOO0OOO00oo
     for Iii in OOo :
      os . unlink ( os . path . join ( i1OoOO , Iii ) )
     for I1iii11 in IIIIIo0ooOoO000oO :
      shutil . rmtree ( os . path . join ( i1OoOO , I1iii11 ) )
      if 85 - 85: II11i1iIiII1 - OOOo0 / i1IIi / Ooo00oOo00o / OoOoOO00
   else :
    pass
    if 94 - 94: iIii1I11I1II1 + Ooo0OO0
    if 44 - 44: Ooo00oOo00o + iI % Ooo00oOo00o + i1IIi + OoOo00o + O0
 Ii1iII1ii1 = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.4od/cache' ) , '' )
 if os . path . exists ( Ii1iII1ii1 ) == True :
  for i1OoOO , IIIIIo0ooOoO000oO , OOo in os . walk ( Ii1iII1ii1 ) :
   OoooOOo0oOO = 0
   OoooOOo0oOO += len ( OOo )
   if 80 - 80: iIii1I11I1II1 / i11iIiiIii + OoOo00o
   if 41 - 41: OoO0O0 + Ooo00oOo00o * OOOo0 * O0 * Oo - I1IiI
   if OoooOOo0oOO > 0 :
    if 96 - 96: OOOo0 - iIii1I11I1II1
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    if i1iiIIiiI111 . yesno ( "Delete 4oD Cache Files" , str ( OoooOOo0oOO ) + " files found" , "Do you want to delete them?" ) :
     if 25 - 25: OoooooooOO . i1I111ii1II1i % OoOo00o . Ooo0OO0
     for Iii in OOo :
      os . unlink ( os . path . join ( i1OoOO , Iii ) )
     for I1iii11 in IIIIIo0ooOoO000oO :
      shutil . rmtree ( os . path . join ( i1OoOO , I1iii11 ) )
      if 67 - 67: OoooooooOO + OoO0O0 / II11i1iIiII1
   else :
    pass
    if 75 - 75: Ooo0OO0 / OoooooooOO . OOOo0 + OoO0O0 - OoOoOO00
    if 33 - 33: Ooo0OO0 / Ooo0OO0 . i11iIiiIii * ii11ii1ii + OOooOOo
 ii1iI11IiIIi = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.iplayer/iplayer_http_cache' ) , '' )
 if os . path . exists ( ii1iI11IiIIi ) == True :
  for i1OoOO , IIIIIo0ooOoO000oO , OOo in os . walk ( ii1iI11IiIIi ) :
   OoooOOo0oOO = 0
   OoooOOo0oOO += len ( OOo )
   if 47 - 47: Oo000 . OOO0OOO00oo + I1IiI % Ooo0OO0 % i1IIi / iIii1I11I1II1
   if 95 - 95: O0 . Ooo00oOo00o
   if OoooOOo0oOO > 0 :
    if 89 - 89: i1IIi
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    if i1iiIIiiI111 . yesno ( "Delete BBC iPlayer Cache Files" , str ( OoooOOo0oOO ) + " files found" , "Do you want to delete them?" ) :
     if 19 - 19: II11i1iIiII1 / OOooOOo % Ooo0OO0 - i1I111ii1II1i
     for Iii in OOo :
      os . unlink ( os . path . join ( i1OoOO , Iii ) )
     for I1iii11 in IIIIIo0ooOoO000oO :
      shutil . rmtree ( os . path . join ( i1OoOO , I1iii11 ) )
      if 14 - 14: ii11ii1ii - i11iIiiIii * OoO0O0
   else :
    pass
    if 39 - 39: OoooooooOO
    if 19 - 19: i11iIiiIii
    if 80 - 80: OOOo0
 oO0OOo = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/script.module.simple.downloader' ) , '' )
 if os . path . exists ( oO0OOo ) == True :
  for i1OoOO , IIIIIo0ooOoO000oO , OOo in os . walk ( oO0OOo ) :
   OoooOOo0oOO = 0
   OoooOOo0oOO += len ( OOo )
   if 63 - 63: OoOoOO00 . OoO0O0 % Ooo0OO0 + OoOoOO00
   if 81 - 81: Oo000 - OOOo0 % OOooOOo
   if OoooOOo0oOO > 0 :
    if 7 - 7: II11i1iIiII1 - i1IIi . I1IiI
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    if i1iiIIiiI111 . yesno ( "Delete Simple Downloader Cache Files" , str ( OoooOOo0oOO ) + " files found" , "Do you want to delete them?" ) :
     if 12 - 12: Ooo0OO0 / Ooo00oOo00o / O0 * Ooo0OO0
     for Iii in OOo :
      os . unlink ( os . path . join ( i1OoOO , Iii ) )
     for I1iii11 in IIIIIo0ooOoO000oO :
      shutil . rmtree ( os . path . join ( i1OoOO , I1iii11 ) )
      if 51 - 51: II11i1iIiII1 * OoOo00o / i1IIi
   else :
    pass
    if 2 - 2: OOO0OOO00oo + Ooo0OO0 . OoOo00o - i1IIi + OoO0O0
    if 54 - 54: OoooooooOO . OOO0OOO00oo - OoOo00o
 oO0o00o000Oo0 = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.itv/Images' ) , '' )
 if os . path . exists ( oO0o00o000Oo0 ) == True :
  for i1OoOO , IIIIIo0ooOoO000oO , OOo in os . walk ( oO0o00o000Oo0 ) :
   OoooOOo0oOO = 0
   OoooOOo0oOO += len ( OOo )
   if 1 - 1: OOOo0 - OoO0O0
   if 62 - 62: Ooo00oOo00o . OoOo00o . OoOo00o % i1IIi * OOO0OOO00oo % Oo
   if OoooOOo0oOO > 0 :
    if 20 - 20: II11i1iIiII1 . Ooo0OO0 / iI . OoooooooOO * Oo000 + i1I111ii1II1i
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    if i1iiIIiiI111 . yesno ( "Delete ITV Cache Files" , str ( OoooOOo0oOO ) + " files found" , "Do you want to delete them?" ) :
     if 2 - 2: OOOo0
     for Iii in OOo :
      os . unlink ( os . path . join ( i1OoOO , Iii ) )
     for I1iii11 in IIIIIo0ooOoO000oO :
      shutil . rmtree ( os . path . join ( i1OoOO , I1iii11 ) )
      if 11 - 11: Oo000 + iIii1I11I1II1 / I1IiI % O0
   else :
    pass
    if 98 - 98: OoOoOO00 + Oo * iIii1I11I1II1 * ii11ii1ii + Oo000 * i1I111ii1II1i
    if 76 - 76: II11i1iIiII1 . OOO0OOO00oo
 oO00OO0o0ooO = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.movies4me/cache' ) , '' )
 if os . path . exists ( oO0o00o000Oo0 ) == True :
  for i1OoOO , IIIIIo0ooOoO000oO , OOo in os . walk ( oO00OO0o0ooO ) :
   OoooOOo0oOO = 0
   OoooOOo0oOO += len ( OOo )
   if 42 - 42: O0 * OoOo00o . I1IiI / Oo000 - i1I111ii1II1i . iI
   if 57 - 57: OOooOOo + Oo * ii11ii1ii - II11i1iIiII1 % iIii1I11I1II1 - i1I111ii1II1i
   if OoooOOo0oOO > 0 :
    if 37 - 37: Ooo00oOo00o * iI + i1I111ii1II1i + ii11ii1ii * OOooOOo
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    if i1iiIIiiI111 . yesno ( "Delete Movies4me Cache Files" , str ( OoooOOo0oOO ) + " files found" , "Do you want to delete them?" ) :
     if 95 - 95: i1I111ii1II1i - i11iIiiIii % i11iIiiIii - O0 * OoO0O0
     for Iii in OOo :
      os . unlink ( os . path . join ( i1OoOO , Iii ) )
     for I1iii11 in IIIIIo0ooOoO000oO :
      shutil . rmtree ( os . path . join ( i1OoOO , I1iii11 ) )
      if 81 - 81: OoOoOO00 * OOOo0 % i1IIi * i11iIiiIii + I1IiI
   else :
    pass
    if 100 - 100: i1IIi % i1I111ii1II1i
    if 55 - 55: OOOo0 + OoOo00o
 OO00o0 = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.phstreams/Cache' ) , '' )
 if os . path . exists ( oO0o00o000Oo0 ) == True :
  for i1OoOO , IIIIIo0ooOoO000oO , OOo in os . walk ( OO00o0 ) :
   OoooOOo0oOO = 0
   OoooOOo0oOO += len ( OOo )
   if 11 - 11: OOOo0 - OoooooooOO + OoOoOO00 + Oo % OoOo00o
   if 90 - 90: OOOo0 * ii11ii1ii . iI * i1I111ii1II1i - OOooOOo
   if OoooOOo0oOO > 0 :
    if 40 - 40: O0 / Ooo0OO0 - OoOoOO00 + OOooOOo % Oo
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    if i1iiIIiiI111 . yesno ( "Delete Phoenix Cache Files" , str ( OoooOOo0oOO ) + " files found" , "Do you want to delete them?" ) :
     if 93 - 93: II11i1iIiII1
     for Iii in OOo :
      os . unlink ( os . path . join ( i1OoOO , Iii ) )
     for I1iii11 in IIIIIo0ooOoO000oO :
      shutil . rmtree ( os . path . join ( i1OoOO , I1iii11 ) )
      if 82 - 82: ii11ii1ii / II11i1iIiII1 . i11iIiiIii + Oo000 - I1IiI / OoOo00o
   else :
    pass
    if 99 - 99: OOO0OOO00oo / i1IIi
    if 2 - 2: OOO0OOO00oo . OoOo00o
 II1II111 = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.spotitube/cache' ) , '' )
 if os . path . exists ( oO0o00o000Oo0 ) == True :
  for i1OoOO , IIIIIo0ooOoO000oO , OOo in os . walk ( II1II111 ) :
   OoooOOo0oOO = 0
   OoooOOo0oOO += len ( OOo )
   if 71 - 71: OoOoOO00 % OoO0O0 + OOOo0 * II11i1iIiII1 + Ooo0OO0 . II11i1iIiII1
   if 25 - 25: II11i1iIiII1 . OOooOOo % OOOo0 + OoOo00o
   if OoooOOo0oOO > 0 :
    if 61 - 61: OOO0OOO00oo % II11i1iIiII1 - ii11ii1ii + OOO0OOO00oo . I1IiI
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    if i1iiIIiiI111 . yesno ( "Delete YouTube Music Cache Files" , str ( OoooOOo0oOO ) + " files found" , "Do you want to delete them?" ) :
     if 44 - 44: ii11ii1ii / O0 - Ooo0OO0 + Oo000 . iI . ii11ii1ii
     for Iii in OOo :
      os . unlink ( os . path . join ( i1OoOO , Iii ) )
     for I1iii11 in IIIIIo0ooOoO000oO :
      shutil . rmtree ( os . path . join ( i1OoOO , I1iii11 ) )
      if 95 - 95: I1IiI % OoO0O0 % i1IIi * OOooOOo + Oo000
   else :
    pass
    if 34 - 34: OoO0O0 * OOooOOo . OOOo0 % i11iIiiIii
    if 61 - 61: iIii1I11I1II1 + OOO0OOO00oo * iI - i1IIi % OOO0OOO00oo
 oOOo = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.supercartoons/cache' ) , '' )
 if os . path . exists ( oO0o00o000Oo0 ) == True :
  for i1OoOO , IIIIIo0ooOoO000oO , OOo in os . walk ( oOOo ) :
   OoooOOo0oOO = 0
   OoooOOo0oOO += len ( OOo )
   if 9 - 9: OoO0O0 - Ooo00oOo00o + iIii1I11I1II1 % O0 + iI + Ooo0OO0
   if 50 - 50: i1IIi + II11i1iIiII1
   if OoooOOo0oOO > 0 :
    if 64 - 64: OOooOOo % OOO0OOO00oo . II11i1iIiII1
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    if i1iiIIiiI111 . yesno ( "Delete SuperCartoons Cache Files" , str ( OoooOOo0oOO ) + " files found" , "Do you want to delete them?" ) :
     if 6 - 6: II11i1iIiII1 / i11iIiiIii - Oo
     for Iii in OOo :
      os . unlink ( os . path . join ( i1OoOO , Iii ) )
     for I1iii11 in IIIIIo0ooOoO000oO :
      shutil . rmtree ( os . path . join ( i1OoOO , I1iii11 ) )
      if 3 - 3: Ooo0OO0 - OoooooooOO * OoooooooOO - OOOo0 / OoO0O0 * ii11ii1ii
   else :
    pass
    if 58 - 58: Ooo0OO0 % iIii1I11I1II1 / i11iIiiIii % OOooOOo . OoO0O0 * OoOo00o
    if 32 - 32: OoooooooOO + OOooOOo
 o0000OOOo = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.tvonline.cc/cache' ) , '' )
 if os . path . exists ( oO0o00o000Oo0 ) == True :
  for i1OoOO , IIIIIo0ooOoO000oO , OOo in os . walk ( o0000OOOo ) :
   OoooOOo0oOO = 0
   OoooOOo0oOO += len ( OOo )
   if 56 - 56: i1IIi + OoooooooOO % Ooo00oOo00o
   if 36 - 36: OoOo00o * iI * O0 * Oo000 - OOooOOo / ii11ii1ii
   if OoooOOo0oOO > 0 :
    if 54 - 54: i1IIi - Ooo00oOo00o / OoooooooOO
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    if i1iiIIiiI111 . yesno ( "Delete TVonline Cache Files" , str ( OoooOOo0oOO ) + " files found" , "Do you want to delete them?" ) :
     if 95 - 95: O0 + iIii1I11I1II1 . ii11ii1ii
     for Iii in OOo :
      os . unlink ( os . path . join ( i1OoOO , Iii ) )
     for I1iii11 in IIIIIo0ooOoO000oO :
      shutil . rmtree ( os . path . join ( i1OoOO , I1iii11 ) )
      if 61 - 61: i1I111ii1II1i * i1I111ii1II1i
   else :
    pass
    if 70 - 70: OoO0O0 . ii11ii1ii / OOooOOo * OOO0OOO00oo
    if 74 - 74: OOOo0 . II11i1iIiII1 / OoOo00o . Ooo0OO0
 OO00 = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.youtube/kodion' ) , '' )
 if os . path . exists ( oO0o00o000Oo0 ) == True :
  for i1OoOO , IIIIIo0ooOoO000oO , OOo in os . walk ( OO00 ) :
   OoooOOo0oOO = 0
   OoooOOo0oOO += len ( OOo )
   if 10 - 10: iI * i1IIi . OOO0OOO00oo / OoO0O0 . Oo000 / OoO0O0
   if 1 - 1: OoOo00o % II11i1iIiII1
   if OoooOOo0oOO > 0 :
    if 99 - 99: OoOo00o + iIii1I11I1II1 . Oo000 / Ooo00oOo00o * ii11ii1ii
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    if i1iiIIiiI111 . yesno ( "Delete YouTube Cache Files" , str ( OoooOOo0oOO ) + " files found" , "Do you want to delete them?" ) :
     if 87 - 87: Ooo0OO0 / OoOoOO00 % Ooo00oOo00o % Ooo00oOo00o
     for Iii in OOo :
      os . unlink ( os . path . join ( i1OoOO , Iii ) )
     for I1iii11 in IIIIIo0ooOoO000oO :
      shutil . rmtree ( os . path . join ( i1OoOO , I1iii11 ) )
      if 28 - 28: I1IiI % OOO0OOO00oo - Oo000 + Oo000 + OOO0OOO00oo / iIii1I11I1II1
   else :
    pass
    if 91 - 91: OOOo0 / OoOoOO00 * Oo000
    if 94 - 94: OoOoOO00 - iIii1I11I1II1 - iIii1I11I1II1
    if 83 - 83: ii11ii1ii * iIii1I11I1II1 + I1IiI * i1IIi . OoooooooOO % i1I111ii1II1i
 oOoOo00oo = xbmc . translatePath ( 'special://masterprofile/addon_data/plugin.video.genesis' )
 i1iiIIiiI111 = xbmcgui . Dialog ( )
 try :
  if i1iiIIiiI111 . yesno ( "Delete Genesis Cache Files" , "Do you want to delete cache" ) :
   II11IiIIiiiii = os . path . join ( oOoOo00oo , "cache.db" )
   os . unlink ( II11IiIIiiiii )
   if 66 - 66: O0 * OOooOOo / ii11ii1ii
 except :
  pass
  if 15 - 15: Oo000 . OOooOOo + OoooooooOO - Oo * iIii1I11I1II1 . i1IIi
 i1iiIIiiI111 = xbmcgui . Dialog ( )
 i1iiIIiiI111 . ok ( "GenieTv" , "                               Finished Deleting Cache " , "                          [COLOR gold]Brought To You By GenieTv[/COLOR]" )
 if 39 - 39: i1I111ii1II1i % i1IIi . ii11ii1ii - O0
 if 65 - 65: OOO0OOO00oo * OOO0OOO00oo / iI + OOO0OOO00oo % II11i1iIiII1 + I1IiI
 if 92 - 92: OOooOOo
 if 37 - 37: OOO0OOO00oo
 if 18 - 18: Ooo0OO0 * i11iIiiIii + iIii1I11I1II1 % iI + i1IIi - Ooo00oOo00o
 if 85 - 85: Ooo00oOo00o * iI + Ooo00oOo00o
 if 39 - 39: Oo / i1IIi % i1IIi
 if 20 - 20: Oo000 * OOO0OOO00oo
 if 91 - 91: Ooo00oOo00o % i1IIi - iIii1I11I1II1 . Oo000
def IIiiIiIIiI1 ( url ) :
 print '###' + o0oOoO00o + ' - DELETING PACKAGES###'
 I1IiIoO0o0o = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' , '' ) )
 try :
  for i1OoOO , IIIIIo0ooOoO000oO , OOo in os . walk ( I1IiIoO0o0o ) :
   OoooOOo0oOO = 0
   OoooOOo0oOO += len ( OOo )
   if 94 - 94: Ooo0OO0 % i1I111ii1II1i % i11iIiiIii . Ooo0OO0
   if 6 - 6: OoO0O0 / OoooooooOO / OoOo00o / OoO0O0 + OoOo00o - I1IiI
   if OoooOOo0oOO > 0 :
    if 71 - 71: ii11ii1ii . OoO0O0
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    if i1iiIIiiI111 . yesno ( "Delete Package Cache Files" , str ( OoooOOo0oOO ) + " files found" , "Do you want to delete them?" ) :
     if 16 - 16: OOO0OOO00oo - ii11ii1ii . I1IiI
     for Iii in OOo :
      os . unlink ( os . path . join ( i1OoOO , Iii ) )
     for I1iii11 in IIIIIo0ooOoO000oO :
      shutil . rmtree ( os . path . join ( i1OoOO , I1iii11 ) )
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
 if 99 - 99: II11i1iIiII1 * iIii1I11I1II1 - i1I111ii1II1i + Oo . Oo
 if 18 - 18: Oo000
 if 82 - 82: OoooooooOO - II11i1iIiII1 * ii11ii1ii * II11i1iIiII1 * O0 * iIii1I11I1II1
 if 31 - 31: II11i1iIiII1 . Oo000 % II11i1iIiII1
 if 33 - 33: O0 * i1I111ii1II1i - Ooo0OO0 . OoooooooOO + Ooo0OO0
 if 20 - 20: OoO0O0 - I1IiI
 if 91 - 91: i1IIi
 if 31 - 31: i11iIiiIii + i1I111ii1II1i % I1IiI
 if 9 - 9: II11i1iIiII1 . iI - Oo . OoO0O0
def i1I111II11 ( url ) :
 print '###' + o0oOoO00o + ' - DELETING PACKAGES###'
 I1IiIoO0o0o = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' , '' ) )
 try :
  for i1OoOO , IIIIIo0ooOoO000oO , OOo in os . walk ( I1IiIoO0o0o ) :
   OoooOOo0oOO = 0
   OoooOOo0oOO += len ( OOo )
   if 56 - 56: OoO0O0 / O0 * Oo000
   if 32 - 32: OoOo00o . iIii1I11I1II1 % Oo . OoooooooOO
   if OoooOOo0oOO > 0 :
    if 81 - 81: i11iIiiIii * OoOo00o . OOO0OOO00oo * OOO0OOO00oo . Ooo0OO0
    i1iiIIiiI111 = xbmcgui . Dialog ( )
    if i1iiIIiiI111 . yesno ( "Delete Package Cache Files" , str ( OoooOOo0oOO ) + " files found" , "Do you want to delete them?" ) :
     if 47 - 47: iIii1I11I1II1 % iI . iI / O0 . i11iIiiIii * i1I111ii1II1i
     for Iii in OOo :
      os . unlink ( os . path . join ( i1OoOO , Iii ) )
     for I1iii11 in IIIIIo0ooOoO000oO :
      shutil . rmtree ( os . path . join ( i1OoOO , I1iii11 ) )
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
 if 33 - 33: OoooooooOO + OOO0OOO00oo * OoOoOO00 / Oo000
 if 87 - 87: OoooooooOO
 if 1 - 1: iIii1I11I1II1 / OOooOOo
 if 98 - 98: O0 % OOOo0 / OoooooooOO * ii11ii1ii - OOO0OOO00oo
 if 51 - 51: OoOo00o + iI
 if 54 - 54: OoOoOO00 * O0 % OOOo0 . iI
 if 62 - 62: i1I111ii1II1i . i11iIiiIii % O0 % OoO0O0 - Oo
 if 69 - 69: OoOoOO00 . I1IiI * I1IiI % i1I111ii1II1i + OOOo0
def ooOOO000O ( url , name ) :
 iIII = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 o0Oi1IIi = os . path . join ( iIII , 'advancedsettings.xml' )
 i1iiIIiiI111 = xbmcgui . Dialog ( )
 OOoo = os . path . join ( iIII , 'advancedsettings.xml.bak' )
 if os . path . exists ( OOoo ) == False :
  if i1iiIIiiI111 . yesno ( "Back Up Original" , 'Have You Backed Up Your Original?' , '' , "[B][COLOR red]     AS YOU CANNOT GO BACK !!![/B][/COLOR]" ) :
   print '###' + o0oOoO00o + ' - ADVANCED XML###'
   iIII = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
   o0Oi1IIi = os . path . join ( iIII , 'advancedsettings.xml' )
   try :
    os . remove ( o0Oi1IIi )
    print '=== GenieTv - REMOVING    ' + str ( o0Oi1IIi ) + '    ==='
   except :
    pass
   iI1I1i11iIIii = i1 . http_GET ( url ) . content
   iIIiIiI1I1 = open ( o0Oi1IIi , "w" )
   iIIiIiI1I1 . write ( iI1I1i11iIIii )
   iIIiIiI1I1 . close ( )
   print '=== GenieTv - WRITING NEW    ' + str ( o0Oi1IIi ) + '    ==='
   i1iiIIiiI111 = xbmcgui . Dialog ( )
   i1iiIIiiI111 . ok ( o0oOoO00o , "       Done Adding new Advanced XML" )
 else :
  print '###' + o0oOoO00o + ' - ADVANCED XML###'
  iIII = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
  o0Oi1IIi = os . path . join ( iIII , 'advancedsettings.xml' )
  try :
   os . remove ( o0Oi1IIi )
   print '=== GenieTv - REMOVING    ' + str ( o0Oi1IIi ) + '    ==='
  except :
   pass
  iI1I1i11iIIii = i1 . http_GET ( url ) . content
  iIIiIiI1I1 = open ( o0Oi1IIi , "w" )
  iIIiIiI1I1 . write ( iI1I1i11iIIii )
  iIIiIiI1I1 . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( o0Oi1IIi ) + '    ==='
  i1iiIIiiI111 = xbmcgui . Dialog ( )
  i1iiIIiiI111 . ok ( o0oOoO00o , "       Done Adding new Advanced XML" )
 return
 if 40 - 40: OOOo0
def i1IiI ( url , name ) :
 print '###' + o0oOoO00o + ' - CHECK ADVANCE XML###'
 iIII = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 o0Oi1IIi = os . path . join ( iIII , 'advancedsettings.xml' )
 try :
  iIIiIiI1I1 = open ( o0Oi1IIi ) . read ( )
  if 'zero' in iIIiIiI1I1 :
   name = '0CACHE'
  elif 'tuxen' in iIIiIiI1I1 :
   name = 'TUXENS'
  elif 'muckys' in iIIiIiI1I1 :
   name = 'MUCKYS'
  elif 'p2p1' in iIIiIiI1I1 :
   name = '1st P2P RECOMMENDED'
  elif 'p2p2' in iIIiIiI1I1 :
   name = '2nd P2P RECOMMENDED'
  elif 'mikey' in iIIiIiI1I1 :
   name = 'MIKEY1234'
 except :
  name = "NO ADVANCED"
 i1iiIIiiI111 = xbmcgui . Dialog ( )
 i1iiIIiiI111 . ok ( o0oOoO00o , "[COLOR yellow]YOU HAVE[/COLOR] " + name + "[COLOR yellow] XML SETTINGS SETUP[/COLOR]" )
 return
 if 73 - 73: OoooooooOO * O0 * II11i1iIiII1
def iii11Ii ( url ) :
 print '###' + o0oOoO00o + ' - DELETING ADVANCE XML###'
 iIII = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 o0Oi1IIi = os . path . join ( iIII , 'advancedsettings.xml' )
 try :
  os . remove ( o0Oi1IIi )
  i1iiIIiiI111 = xbmcgui . Dialog ( )
  print '=== GenieTv - DELETING    ' + str ( o0Oi1IIi ) + '    ==='
  i1iiIIiiI111 . ok ( o0oOoO00o , "       Remove Advanced Settings Sucessfull" )
 except :
  i1iiIIiiI111 = xbmcgui . Dialog ( )
  i1iiIIiiI111 . ok ( o0oOoO00o , "       No Advanced Settings To Remove" )
 return
 if 31 - 31: OOO0OOO00oo
 if 69 - 69: iIii1I11I1II1 . iI / OoOo00o
 if 87 - 87: O0 * Ooo00oOo00o + i1IIi
 if 33 - 33: OOOo0 * OoO0O0
 if 98 - 98: ii11ii1ii - OoooooooOO / OOOo0 . II11i1iIiII1 - i1IIi
 if 60 - 60: I1IiI % I1IiI
 if 2 - 2: i1I111ii1II1i . O0 - OOO0OOO00oo + Ooo0OO0
 if 96 - 96: i1I111ii1II1i + i1I111ii1II1i
 if 28 - 28: OoOo00o
 if 6 - 6: OOOo0 - OoOo00o
def ii1II ( url = 'http://www.iplocation.net/' , inc = 1 ) :
 IIIII11I1IiI = re . compile ( "<td width='80'>(.+?)</td><td>(.+?)</td><td>(.+?)</td><td>.+?</td><td>(.+?)</td>" ) . findall ( i1 . http_GET ( url ) . content )
 for OOo00o0o0O0oo , i1iI1iIII , oo0Oo , I1IiIIIIi1iiI in IIIII11I1IiI :
  if inc < 2 : i1iiIIiiI111 = xbmcgui . Dialog ( ) ; i1iiIIiiI111 . ok ( 'Check My IP' , "[B][COLOR gold]Your IP Address is: [/COLOR][/B] %s" % OOo00o0o0O0oo , '[B][COLOR gold]Your IP is based in: [/COLOR][/B] %s' % oo0Oo , '[B][COLOR gold]Your Service Provider is:[/COLOR][/B] %s' % I1IiIIIIi1iiI )
  inc = inc + 1
  if 57 - 57: iI . O0 . OoooooooOO . OoO0O0 - i1I111ii1II1i / II11i1iIiII1
  if 34 - 34: I1IiI % OOooOOo - OOO0OOO00oo
  if 40 - 40: OoOo00o
  if 82 - 82: OoO0O0 . i1IIi / OOO0OOO00oo
  if 56 - 56: OoOo00o
  if 23 - 23: i1IIi
  if 24 - 24: Ooo0OO0
  if 51 - 51: Oo000 % i11iIiiIii
  if 77 - 77: Oo000 % i11iIiiIii - ii11ii1ii
def I1oooO00oOOooO ( url , name ) :
 i1iiIIiiI111 = xbmcgui . Dialog ( )
 if i1iiIIiiI111 . yesno ( "GenieTv" , '                                    Install Latest .ini File' ) :
  print '###' + o0oOoO00o + ' - CUSTOM FTV INI###'
  iIII = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/plugin.video.GenieTv' , '' ) )
  o0Oi1IIi = os . path . join ( iIII , 'addons2.ini' )
  iI1I1i11iIIii = i1 . http_GET ( url ) . content
  iIIiIiI1I1 = open ( o0Oi1IIi , "w" )
  iIIiIiI1I1 . write ( iI1I1i11iIIii )
  iIIiIiI1I1 . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( o0Oi1IIi ) + '    ==='
  i1iiIIiiI111 = xbmcgui . Dialog ( )
  i1iiIIiiI111 . ok ( o0oOoO00o , "                               Done Adding New .ini File" )
 return
 if 34 - 34: iIii1I11I1II1 / OoOoOO00
def IIIii111i ( url , name ) :
 i1iiIIiiI111 = xbmcgui . Dialog ( )
 if i1iiIIiiI111 . yesno ( "GenieTv" , '                               Install Custom Settings' ) :
  print '###' + o0oOoO00o + ' - CUSTOM FTV SETTINGS###'
  iIII = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/plugin.video.GenieTv' , '' ) )
  o0Oi1IIi = os . path . join ( iIII , 'settings.xml' )
  iI1I1i11iIIii = i1 . http_GET ( url ) . content
  iIIiIiI1I1 = open ( o0Oi1IIi , "w" )
  iIIiIiI1I1 . write ( iI1I1i11iIIii )
  iIIiIiI1I1 . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( o0Oi1IIi ) + '    ==='
  i1iiIIiiI111 = xbmcgui . Dialog ( )
  i1iiIIiiI111 . ok ( o0oOoO00o , "                               Done Adding New Settings" )
 return
 if 58 - 58: Oo000 % OoOo00o * O0 + ii11ii1ii - Ooo0OO0
 if 26 - 26: i1IIi / OOOo0 / iI + iI
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
 if 15 - 15: II11i1iIiII1 * iIii1I11I1II1 * OOO0OOO00oo
 if 96 - 96: OoO0O0 * iIii1I11I1II1 / I1IiI % Oo000 * OoOoOO00
 if 3 - 3: Oo000 . Oo / i11iIiiIii + Ooo00oOo00o
 if 47 - 47: Ooo0OO0 . Oo000
 if 96 - 96: iI % OoOoOO00 / II11i1iIiII1 % Oo000 / II11i1iIiII1 % i11iIiiIii
def iIi1 ( url ) :
 o0OOOOoO = urllib2 . Request ( url )
 o0OOOOoO . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
 OoO0Ooo = urllib2 . urlopen ( o0OOOOoO )
 iI1I1i11iIIii = OoO0Ooo . read ( )
 OoO0Ooo . close ( )
 return iI1I1i11iIIii
 if 57 - 57: iI - iI % OoOoOO00 % Oo . OOooOOo % Oo
 if 91 - 91: OOOo0 - Ooo00oOo00o - Oo - i1I111ii1II1i * iIii1I11I1II1
 if 68 - 68: Ooo00oOo00o % O0 * iIii1I11I1II1 / OOO0OOO00oo * OOooOOo + Oo000
 if 89 - 89: II11i1iIiII1 * OOOo0 . OOO0OOO00oo
 if 75 - 75: II11i1iIiII1 - OoOo00o % OoOo00o + II11i1iIiII1 * OOooOOo - ii11ii1ii
 if 26 - 26: iI * i1I111ii1II1i % OOOo0 + OoOo00o
 if 38 - 38: OoOo00o - Oo / i1I111ii1II1i + OOO0OOO00oo . OoOo00o + Ooo0OO0
def iIiii1iI1Ii ( params ) :
 plugintools . log ( "freshstart.main_list " + repr ( params ) ) ; ooIi = plugintools . message_yes_no ( o0oOoO00o , "Do you wish to restore your" , "Kodi configuration to default settings?" )
 if ooIi :
  oO0oOo = xbmcaddon . Addon ( id = o00 ) . getAddonInfo ( 'path' ) ; oO0oOo = xbmc . translatePath ( oO0oOo ) ;
  IIiIiii = os . path . join ( oO0oOo , ".." , ".." ) ; IIiIiii = os . path . abspath ( IIiIiii ) ; plugintools . log ( "freshstart.main_list xbmcPath=" + IIiIiii ) ; OOo0OO = False
  try :
   for i1OoOO , IIIIIo0ooOoO000oO , OOo in os . walk ( IIiIiii , topdown = True ) :
    IIIIIo0ooOoO000oO [ : ] = [ I1iii11 for I1iii11 in IIIIIo0ooOoO000oO if I1iii11 not in iiIIIII1i1iI ]
    for I1Ii in OOo :
     try : os . remove ( os . path . join ( i1OoOO , I1Ii ) )
     except :
      if I1Ii not in [ "Addons15.db" , "MyVideos75.db" , "Textures13.db" , "xbmc.log" ] : OOo0OO = True
      plugintools . log ( "Error removing " + i1OoOO + " " + I1Ii )
    for I1Ii in IIIIIo0ooOoO000oO :
     try : os . rmdir ( os . path . join ( i1OoOO , I1Ii ) )
     except :
      if I1Ii not in [ "Database" , "userdata" ] : OOo0OO = True
      plugintools . log ( "Error removing " + i1OoOO + " " + I1Ii )
   if not OOo0OO : plugintools . log ( "freshstart.main_list All user files removed, you now have a clean install" ) ; plugintools . message ( o0oOoO00o , "The process is complete, you're now back to a fresh Kodi configuration with GenieTv!" , "Please reboot your system or restart Kodi in order for the changes to be applied." )
   else : plugintools . log ( "freshstart.main_list User files partially removed" ) ; plugintools . message ( o0oOoO00o , "The process is complete, you're now back to a fresh Kodi configuration with GenieTv" , "Please reboot your system or restart Kodi in order for the changes to be applied." )
  except : plugintools . message ( o0oOoO00o , "Problem found" , "Your settings has not been changed" ) ; import traceback ; plugintools . log ( traceback . format_exc ( ) ) ; plugintools . log ( "freshstart.main_list NOT removed" )
  plugintools . add_item ( action = "" , title = "Now Exit Kodi" , folder = False )
 else : plugintools . message ( o0oOoO00o , "Your settings" , "has not been changed" ) ; plugintools . add_item ( action = "" , title = "Done" , folder = False )
 OoOoO00O0 ( )
 if 98 - 98: i11iIiiIii . OoO0O0 + I1IiI
 if 55 - 55: iI
 if 72 - 72: iI + II11i1iIiII1 / OOOo0 . Ooo0OO0 % Ooo00oOo00o / i11iIiiIii
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
  for iI1i1iiii in range ( len ( OoOoOoo0oOOooo0o ) ) :
   III = { }
   III = OoOoOoo0oOOooo0o [ iI1i1iiii ] . split ( '=' )
   if ( len ( III ) ) == 2 :
    ooooooo0oOo0 [ III [ 0 ] ] = III [ 1 ]
    if 1 - 1: OoO0O0 . OoOo00o * I1IiI / O0 + OOO0OOO00oo + OOooOOo
 return ooooooo0oOo0
 if 81 - 81: iIii1I11I1II1
OOO00OO0oOo = base64 . decodestring ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20v' )
IIIIi1I = base64 . decodestring ( 'L3N0b3JhZ2UvZW11bGF0ZWQvMA==' )
I1I1iI = base64 . decodestring ( 'L2dlbmllLnR4dA==' )
OOO00O = base64 . decodestring ( 'LmFyY2hpdGVjdHMueDEwaG9zdC5jb20vdGVzdC93aC50eHQ=' )
IIIIIiI111I = base64 . decodestring ( 'aHR0cDovL2ZpeGVzLmFyY2hpdGVjdHMueDEwaG9zdC5jb20vZml4ZXMudHh0' )
iIO0 = base64 . decodestring ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vYXBwcy9hcHBzLnhtbA==' )
i11I = base64 . decodestring ( 'L2FkZG9ucy9uZXcudHh0' )
o00oO00O0 = base64 . decodestring ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vdm9kL3ZvZC5waHA=' )
iIiI1II1I1 = base64 . decodestring ( 'L2FkZG9ucy9pcHR2LnR4dA==' )
OooO0O0oo = base64 . decodestring ( 'L2FkZG9ucy92aWRlby50eHQ=' )
OoooOO0 = base64 . decodestring ( 'L2FkZG9ucy9zcG9ydHMudHh0' )
Iii1 = base64 . decodestring ( 'L2FkZG9ucy9raWRzLnR4dA==' )
I1o0 = base64 . decodestring ( 'L2FkZG9ucy9tdXNpYy50eHQ=' )
iI1ii = base64 . decodestring ( 'L2FkZG9ucy9wcm9ncmFtcy50eHQ=' )
o0oo00OOOo = base64 . decodestring ( 'L2FkZG9ucy94eHgudHh0' )
o0oo0Ooo0 = base64 . decodestring ( 'L2FkZG9ucy9yZXBvLnR4dA==' )
IIi11IIiIii1 = base64 . decodestring ( 'L2FkZG9ucy9wYWNrcy50eHQ=' )
I1IiiIII = base64 . decodestring ( 'L2FkZG9ucy9za2lucy50eHQ=' )
ii1oOoO0o0ooo = base64 . decodestring ( 'L2FkZG9ucy9hcnQudHh0' )
oOo00 = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2dvdGhhbS50eHQ=' )
Oo000o = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2hlbGl4LnR4dA==' )
OooOOOOoO00OoOO = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2lzZW5nYXJkLnR4dA==' )
iIIi1II1 = base64 . decodestring ( 'L2FkZG9ucy9SU1MudHh0' )
I1I1IiIi1 = base64 . decodestring ( 'Q1VOVA==' )
def O00Oo000ooO0 ( name , url , mode , iconimage , fanart , description , showcontext = True , allinfo = { } ) :
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
 if 40 - 40: OoO0O0 % OOooOOo / OOOo0
def ii1ii11IIIiiI ( name , url , mode , iconimage , fanart , description ) :
 I11Oo0oO00 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 IiiI1III1I1 = True
 o0OoOoo00O = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 o0OoOoo00O . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 o0OoOoo00O . setProperty ( "Fanart_Image" , fanart )
 IiiI1III1I1 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = I11Oo0oO00 , listitem = o0OoOoo00O , isFolder = False )
 return IiiI1III1I1
 if 31 - 31: Oo - Oo000 * OoO0O0 % Oo000 - I1IiI - O0
 if 49 - 49: OOO0OOO00oo - OoOoOO00 / OoOoOO00
IIII1iI1IiIiI = I1III1I1IiI ( )
OOOooo = None
I1Ii = None
iIiii = None
ooo0O0o00O = None
I1i11 = None
OOo0 = None
I11II = None
if 31 - 31: Ooo00oOo00o - Ooo00oOo00o / i1I111ii1II1i - iIii1I11I1II1 * i1I111ii1II1i
if 30 - 30: OOooOOo + i1I111ii1II1i / OoooooooOO - Ooo0OO0 % OOO0OOO00oo
try :
 I11II = int ( IIII1iI1IiIiI [ "fav_mode" ] )
except :
 pass
 if 21 - 21: OoooooooOO % I1IiI - I1IiI / ii11ii1ii / OOooOOo
try :
 OOOooo = urllib . unquote_plus ( IIII1iI1IiIiI [ "url" ] )
except :
 pass
try :
 I1Ii = urllib . unquote_plus ( IIII1iI1IiIiI [ "name" ] )
except :
 pass
try :
 ooo0O0o00O = urllib . unquote_plus ( IIII1iI1IiIiI [ "iconimage" ] )
except :
 pass
try :
 iIiii = int ( IIII1iI1IiIiI [ "mode" ] )
except :
 pass
try :
 I1i11 = urllib . unquote_plus ( IIII1iI1IiIiI [ "fanart" ] )
except :
 pass
try :
 OOo0 = urllib . unquote_plus ( IIII1iI1IiIiI [ "description" ] )
except :
 pass
 if 15 - 15: II11i1iIiII1 / II11i1iIiII1 % OoooooooOO . OoO0O0
 if 93 - 93: ii11ii1ii * ii11ii1ii / OoooooooOO
print str ( O0OoO000O0OO ) + ': ' + str ( O00ooOO )
print "Mode: " + str ( iIiii )
print "URL: " + str ( OOOooo )
print "Name: " + str ( I1Ii )
print "IconImage: " + str ( ooo0O0o00O )
if 6 - 6: ii11ii1ii * Oo + iIii1I11I1II1
if 19 - 19: O0 % OoOoOO00 * OOooOOo
def ii111 ( content , viewType ) :
 if 27 - 27: Oo000 * Ooo0OO0 / i11iIiiIii - OOO0OOO00oo + OoOoOO00
 if content :
  xbmcplugin . setContent ( int ( sys . argv [ 1 ] ) , content )
 if o0oO0 . getSetting ( 'auto-view' ) == 'true' :
  xbmc . executebuiltin ( "Container.SetViewMode(%s)" % o0oO0 . getSetting ( viewType ) )
  if 43 - 43: ii11ii1ii - OoOoOO00
  if 56 - 56: ii11ii1ii . i1IIi / OoOo00o % OOO0OOO00oo / O0 * iI
if iIiii == None :
 IIIIii ( )
 if 98 - 98: O0 + OoOo00o
elif iIiii == 1 :
 i11i1iIiii ( OOOooo )
 if 23 - 23: OoooooooOO . iIii1I11I1II1 / i1IIi
elif iIiii == 44 :
 iIiIi11Ii ( OOOooo )
 if 31 - 31: Oo - iIii1I11I1II1 / iI . Ooo00oOo00o
elif iIiii == 2 :
 iioOo0OoOOo0 ( )
 if 74 - 74: Oo - OoOoOO00 - Ooo0OO0
elif iIiii == 3 :
 OoO00 ( )
 if 50 - 50: OOOo0 - OOO0OOO00oo + OOO0OOO00oo * iI + OOO0OOO00oo
elif iIiii == 21 :
 iI1Ii11111iIi ( )
 if 70 - 70: i1IIi % Ooo00oOo00o / i1IIi
elif iIiii == 4 :
 I1Iiiiiii ( )
 if 30 - 30: I1IiI - i11iIiiIii
elif iIiii == 5 :
 i11i11 ( I1Ii , OOOooo , OOo0 )
 if 94 - 94: I1IiI % OoOo00o
elif iIiii == 6 :
 IIiiIiIIiI1 ( OOOooo )
 if 39 - 39: I1IiI + OoO0O0 % O0
elif iIiii == 7 :
 ooOOO000O ( OOOooo , I1Ii )
 if 26 - 26: II11i1iIiII1 + I1IiI
elif iIiii == 8 :
 i1IiI ( OOOooo , I1Ii )
 if 17 - 17: ii11ii1ii - OoOo00o % Oo * O0 % O0 * Oo000
elif iIiii == 9 :
 FIXREPOSADDONS ( OOOooo )
 if 6 - 6: OoO0O0
elif iIiii == 10 :
 OOOOOoo0 ( )
 if 46 - 46: OoOoOO00 * OoO0O0
elif iIiii == 11 :
 iii11Ii ( OOOooo )
 if 23 - 23: i1IIi - O0
elif iIiii == 12 :
 ii1II ( )
 if 6 - 6: II11i1iIiII1 % OoooooooOO * OoO0O0 - Ooo0OO0
elif iIiii == 13 :
 IiiiI11 ( )
 if 24 - 24: iI / iIii1I11I1II1 . OoooooooOO % I1IiI . i1I111ii1II1i
elif iIiii == 14 :
 iiIII1i1 ( OOOooo )
 if 73 - 73: OoO0O0
elif iIiii == 15 :
 OOO ( )
 if 25 - 25: Ooo0OO0
elif iIiii == 16 :
 I1oooO00oOOooO ( OOOooo , I1Ii )
 if 77 - 77: OOooOOo . iIii1I11I1II1 . OoooooooOO . iIii1I11I1II1
elif iIiii == 17 :
 IIIii111i ( OOOooo , I1Ii )
 if 87 - 87: OoOoOO00 - OoooooooOO / i1IIi . i1I111ii1II1i - Oo . i11iIiiIii
elif iIiii == 18 :
 i1II111iiii ( )
 if 47 - 47: Oo % Ooo00oOo00o - II11i1iIiII1 - Oo * OOO0OOO00oo
elif iIiii == 19 :
 ii1iIi1II ( I1Ii , OOOooo , OOo0 )
 if 72 - 72: OOooOOo % OOooOOo + OoOo00o + ii11ii1ii / Oo
elif iIiii == 40 :
 iioo0o0OoOOO ( I1Ii , OOOooo , OOo0 )
 if 30 - 30: Oo + OOOo0 + i11iIiiIii / Ooo00oOo00o
elif iIiii == 42 :
 IiIi1II11i ( I1Ii , OOOooo , OOo0 )
 if 64 - 64: Ooo0OO0
elif iIiii == 43 :
 IIii1i1iii1 ( I1Ii , OOOooo , OOo0 )
 if 80 - 80: OOOo0 - i11iIiiIii / Ooo00oOo00o / I1IiI + I1IiI
elif iIiii == 20 :
 I111 ( OOOooo )
 if 89 - 89: O0 + Ooo0OO0 * OoO0O0
elif iIiii == 22 :
 iioo ( OOOooo )
 if 30 - 30: I1IiI
elif iIiii == 23 :
 Ooo0o0000OO ( OOOooo )
 if 39 - 39: ii11ii1ii + OOooOOo + OoO0O0 + Ooo0OO0
elif iIiii == 24 :
 ii1Ii11Ii1i ( OOOooo )
 if 48 - 48: OoO0O0 / II11i1iIiII1 . iIii1I11I1II1
elif iIiii == 25 :
 OO0oO0Oo ( OOOooo )
 if 72 - 72: i1IIi . OOooOOo
elif iIiii == 26 :
 oooOOO ( OOOooo )
 if 3 - 3: I1IiI % OoOoOO00 - O0
elif iIiii == 27 :
 OOoOo0O0 ( OOOooo )
 if 52 - 52: Ooo00oOo00o
elif iIiii == 28 :
 O0OOo0o0O00oOo ( OOOooo )
 if 49 - 49: i1I111ii1II1i . ii11ii1ii % II11i1iIiII1 . Oo * Oo000
elif iIiii == 29 :
 OoO0oOOOO ( OOOooo )
 if 44 - 44: iIii1I11I1II1 / O0 * Oo + OOOo0 . II11i1iIiII1
elif iIiii == 30 :
 Ooo0oo ( OOOooo )
 if 20 - 20: OoOo00o + OOooOOo . OoO0O0 / i11iIiiIii
elif iIiii == 31 :
 i1i1IIi ( OOOooo )
 if 7 - 7: I1IiI / I1IiI . OoO0O0 * O0 + Ooo0OO0 + OOO0OOO00oo
elif iIiii == 32 :
 IiII1II11I ( )
 if 98 - 98: OoOoOO00 * Ooo0OO0 - OOOo0 % OOooOOo - OoOo00o % ii11ii1ii
elif iIiii == 33 :
 iiiiI1i1i ( )
 if 69 - 69: i1IIi % Ooo00oOo00o % OoO0O0 / II11i1iIiII1 / II11i1iIiII1
elif iIiii == 35 :
 OoOOoO000O00oO ( OOOooo )
 if 6 - 6: OoOoOO00 % ii11ii1ii % i1IIi * II11i1iIiII1
elif iIiii == 34 :
 o000O000 ( OOOooo )
 if 47 - 47: O0
elif iIiii == 36 :
 oO0oOOoo00000 ( OOOooo )
 if 55 - 55: Ooo00oOo00o % O0 / OoooooooOO
elif iIiii == 37 :
 Ii1IIiiIIi ( OOOooo )
 if 49 - 49: OOOo0 . Ooo00oOo00o * OoooooooOO % i11iIiiIii + iIii1I11I1II1 * i1IIi
elif iIiii == 38 :
 O0oOo00o0 ( OOOooo )
 if 88 - 88: ii11ii1ii * OoOo00o + OoOoOO00
elif iIiii == 41 :
 iIiii1iI1Ii ( IIII1iI1IiIiI )
 if 62 - 62: OoooooooOO
elif iIiii == 39 :
 i11iII1II1I1 ( OOOooo )
 if 33 - 33: O0 . i11iIiiIii % OOooOOo
elif iIiii == 45 :
 TEXTS ( )
 if 50 - 50: II11i1iIiII1
elif iIiii == 46 :
 O0Oo0Oo00o0o ( )
 if 81 - 81: i11iIiiIii * iIii1I11I1II1 / Oo * Oo000
elif iIiii == 47 :
 GEVID ( )
 if 83 - 83: i11iIiiIii - OOOo0 * i11iIiiIii
elif iIiii == 48 :
 OOooO ( I1Ii , OOOooo , OOo0 )
 if 59 - 59: OoOo00o - OoooooooOO / II11i1iIiII1 + ii11ii1ii . OOooOOo - OoOo00o
elif iIiii == 49 :
 o0iiiI1I1iIIIi1 ( )
 if 29 - 29: OOO0OOO00oo
elif iIiii == 222 :
 iIIii ( OOOooo )
 if 26 - 26: O0 % Oo000 - Ooo0OO0 . Oo000
elif iIiii == 333 :
 IIiIi11i111II ( OOOooo )
 if 70 - 70: OOooOOo + iI / OoOo00o + II11i1iIiII1 / OOOo0
 if 33 - 33: OoooooooOO . O0
elif iIiii == 1020 :
 O0Ooo00o00O ( )
 if 59 - 59: iIii1I11I1II1
elif iIiii == 1021 :
 ANIMEEP ( )
 if 45 - 45: O0
elif iIiii == 1022 :
 ANIMEPLAY ( OOOooo )
 if 78 - 78: iI - iIii1I11I1II1 + OoO0O0 - ii11ii1ii - OoO0O0
elif iIiii == 1001 :
 Oo00O ( )
 if 21 - 21: OoooooooOO . O0 / i11iIiiIii
elif iIiii == 1005 :
 IiIIiiiIi ( )
 if 86 - 86: I1IiI / Oo000
elif iIiii == 1007 :
 IiI111 ( OOOooo )
 if 40 - 40: iIii1I11I1II1 / II11i1iIiII1 / OOOo0 + ii11ii1ii * Oo000
elif iIiii == 1010 :
 OOoiII1I1i ( OOOooo )
 if 1 - 1: Ooo00oOo00o * II11i1iIiII1 + Ooo0OO0 . OOO0OOO00oo / II11i1iIiII1
elif iIiii == 1011 :
 IIiii ( OOOooo )
 if 91 - 91: i1I111ii1II1i + iI - Oo % I1IiI . OoOo00o
elif iIiii == 1030 :
 ooOoOooo00Oo ( )
 if 51 - 51: Oo000 / iI
elif iIiii == 1031 :
 ooo00O0OOo ( OOOooo , ooo0O0o00O )
 if 51 - 51: II11i1iIiII1 * OOO0OOO00oo - OoO0O0 + OoOo00o
elif iIiii == 1006 :
 Parse . ParseURL ( OOOooo )
 if 46 - 46: OOooOOo - i11iIiiIii % Ooo00oOo00o / i1I111ii1II1i - I1IiI
elif iIiii == 2030 :
 Parse . addonParseURL ( OOOooo )
 if 88 - 88: OOO0OOO00oo * OOOo0 / Ooo00oOo00o - Oo000 / i1IIi . OoO0O0
elif iIiii == 2031 :
 Parse . apkParseURL ( OOOooo )
 if 26 - 26: i11iIiiIii - II11i1iIiII1
elif iIiii == 1002 :
 oO0oOooO00oo ( OOOooo )
 if 45 - 45: II11i1iIiII1 + OoOoOO00 % OoOo00o
elif iIiii == 1003 :
 Oo000oO ( OOOooo , ooo0O0o00O )
 if 55 - 55: II11i1iIiII1 - OOO0OOO00oo % OOOo0
elif iIiii == 1004 :
 iiIIIII ( OOOooo )
 if 61 - 61: II11i1iIiII1
elif iIiii == 1008 :
 IIOO ( )
 if 22 - 22: iIii1I11I1II1 / II11i1iIiII1 / OOOo0 - OOooOOo
elif iIiii == 1009 :
 M3UPLAY ( OOOooo )
 if 21 - 21: OOO0OOO00oo . i11iIiiIii * iI . Oo000 / Oo000
elif iIiii == 2001 :
 IiOo00O0o0O ( OOOooo )
 if 42 - 42: OoooooooOO / OoO0O0 . OOooOOo / O0 - Ooo0OO0 * Ooo0OO0
elif iIiii == 1013 :
 IIiI1I1 ( )
 if 1 - 1: i1I111ii1II1i % OoO0O0
elif iIiii == 1014 :
 Oo0OO00OO0Oo ( )
 if 97 - 97: I1IiI
elif iIiii == 1015 :
 IiIo00oO0o00O ( OOOooo )
 if 13 - 13: I1IiI % Oo000 . O0 / Oo % Oo
elif iIiii == 1016 :
 oO0o000oOO ( OOOooo )
 if 19 - 19: OoO0O0 % II11i1iIiII1 - II11i1iIiII1 % OOOo0 . Oo000 - OoooooooOO
elif iIiii == 1023 :
 i1iiIiI1Ii1i ( )
 if 100 - 100: OOOo0 + i1I111ii1II1i + OOooOOo . i1IIi % OoooooooOO
elif iIiii == 1024 :
 OoOooO ( )
 if 64 - 64: O0 % i1IIi * OoO0O0 - i1I111ii1II1i + Oo
elif iIiii == 1025 :
 I1I1i11iiiiI ( OOOooo )
 if 65 - 65: I1IiI . i11iIiiIii
elif iIiii == 4001 :
 oOoOO0 ( )
 if 36 - 36: OOO0OOO00oo * OoOo00o + Ooo0OO0 * OoOo00o . ii11ii1ii - iIii1I11I1II1
elif iIiii == 4002 :
 IiI11iII1 ( )
 if 14 - 14: iI * OOO0OOO00oo + i11iIiiIii
elif iIiii == 4003 :
 Oo00OoOo ( )
 if 84 - 84: OoOo00o / OoOoOO00
elif iIiii == 4004 :
 oOiIi1IIIi1 ( )
 if 86 - 86: OOOo0
elif iIiii == 4005 :
 o0oO ( )
 if 97 - 97: OoOoOO00
elif iIiii == 4006 :
 IIiIi1iI ( )
 if 38 - 38: OOOo0
elif iIiii == 4007 :
 III1Iiii1I11 ( )
 if 42 - 42: OOooOOo
elif iIiii == 4008 :
 IIII ( )
 if 8 - 8: i11iIiiIii / II11i1iIiII1
elif iIiii == 4009 : O0oOoOOOoOO ( )
elif iIiii == 4010 : OoO0O00O0oo0O ( )
elif iIiii == 3000 :
 O0OO ( )
 if 33 - 33: OoO0O0 * Ooo0OO0 - O0 + OOOo0 / Ooo0OO0
elif iIiii == 3001 :
 I111I1I ( )
 if 19 - 19: i1IIi % OoOoOO00
elif iIiii == 3002 :
 Oo0000 ( OOOooo )
 if 85 - 85: Ooo0OO0 - OOooOOo % Oo000 - OoOoOO00
elif iIiii == 3003 :
 oO0Oo ( OOOooo )
 if 56 - 56: i1I111ii1II1i * i11iIiiIii
elif iIiii == 3004 :
 i1I11ii ( OOOooo )
 if 92 - 92: OoOoOO00 - O0 . OoO0O0
elif iIiii == 404 :
 i1111I ( I1Ii , OOOooo , ooo0O0o00O )
 if 59 - 59: I1IiI
elif iIiii == 405 :
 iiii1Ii1iii ( OOOooo )
 if 47 - 47: OoOoOO00 - ii11ii1ii - i1I111ii1II1i
elif iIiii == 7030 :
 i111 ( )
 if 9 - 9: ii11ii1ii - Ooo0OO0
elif iIiii == 7021 :
 I1I1i1I1I1I1 ( I1Ii )
 if 64 - 64: i1IIi
elif iIiii == 7022 :
 iIiII1 ( I1Ii )
 if 71 - 71: Ooo0OO0 * OOooOOo
elif iIiii == 7000 :
 iI11I ( I1Ii , OOOooo , img )
 if 99 - 99: OOooOOo
elif iIiii == 7050 :
 o0Ii11iIiiI ( OOOooo )
 if 28 - 28: OoooooooOO % O0 - Oo000 / OOooOOo / OOOo0
elif iIiii == 7051 :
 OoOO00oo0o ( OOOooo )
 if 41 - 41: OoOoOO00 * Ooo0OO0 / Ooo00oOo00o . OOO0OOO00oo
elif iIiii == 7052 :
 o0o ( OOOooo )
 if 50 - 50: OoooooooOO + iIii1I11I1II1 / OOO0OOO00oo / Oo000 . i11iIiiIii . II11i1iIiII1
elif iIiii == 7053 :
 i1I1I1I ( OOOooo )
 if 75 - 75: iIii1I11I1II1 % II11i1iIiII1 / Oo000 - OoOo00o % i11iIiiIii
elif iIiii == 7054 :
 CoolPlay ( OOOooo )
 if 11 - 11: iI . i1I111ii1II1i
elif iIiii == 7060 :
 i1i1Ii1IiIII ( )
 if 87 - 87: Oo000 + Oo000
elif iIiii == 7061 :
 I1iii1 ( OOOooo )
 if 45 - 45: i1IIi - Oo
elif iIiii == 7063 :
 I1IIii11 ( OOOooo )
 if 87 - 87: I1IiI - Ooo00oOo00o * Ooo00oOo00o / i1I111ii1II1i . iI * OOooOOo
elif iIiii == 7062 :
 OOo00Oooo ( OOOooo )
 if 21 - 21: OoOoOO00
elif iIiii == 7064 :
 NATatozcat ( )
 if 29 - 29: I1IiI % i1I111ii1II1i
elif iIiii == 7067 :
 iIiiii1I ( OOOooo )
 if 7 - 7: i1IIi / Ooo0OO0 / OoOo00o
elif iIiii == 7066 :
 NATatozA ( OOOooo )
 if 97 - 97: Ooo00oOo00o + iIii1I11I1II1
elif iIiii == 7065 :
 IiIooOoOo0O00oo ( OOOooo )
 if 79 - 79: II11i1iIiII1 + OOO0OOO00oo - OoOoOO00 . Oo
elif iIiii == 7070 :
 ii1O0Ooo0O ( )
 if 26 - 26: Ooo0OO0
elif iIiii == 7071 :
 DIZIlist ( OOOooo )
 if 52 - 52: O0 + II11i1iIiII1
elif iIiii == 7072 :
 DIZIpull ( OOOooo )
 if 11 - 11: i1IIi / OoO0O0 * ii11ii1ii * OoO0O0 * II11i1iIiII1 - i11iIiiIii
elif iIiii == 7073 :
 WATCHDIZI ( OOOooo )
 if 96 - 96: ii11ii1ii % ii11ii1ii
elif iIiii == 7002 :
 iiiIIIII11i1I ( )
 if 1 - 1: OOOo0 . i1I111ii1II1i
elif iIiii == 7003 :
 iiIiiII1II1ii ( OOOooo )
 if 26 - 26: OOO0OOO00oo - II11i1iIiII1 % Oo - OOO0OOO00oo + Ooo0OO0
elif iIiii == 7004 :
 O0OoOo ( OOOooo )
 if 33 - 33: i1I111ii1II1i + I1IiI - ii11ii1ii + iIii1I11I1II1 % i1IIi * Ooo0OO0
elif iIiii == 7020 :
 oOOo00Ooo0O ( OOOooo )
 if 21 - 21: O0 * II11i1iIiII1 % Ooo00oOo00o
elif iIiii == 7001 :
 iiII1IIii1i1 ( )
 if 14 - 14: O0 / OoO0O0 / II11i1iIiII1 + Ooo0OO0 - Ooo0OO0
elif iIiii == 7010 :
 OOOo00o ( OOOooo )
 if 10 - 10: O0 - ii11ii1ii / OoO0O0 % I1IiI / OoooooooOO / i1I111ii1II1i
elif iIiii == 7011 :
 IIIii11 ( OOOooo )
 if 73 - 73: II11i1iIiII1 + Ooo0OO0 % OOooOOo . ii11ii1ii / Oo000 . OoO0O0
elif iIiii == 7012 :
 Ii1I1Iiii ( OOOooo )
 if 76 - 76: iI . ii11ii1ii * OoooooooOO % OoOo00o
elif iIiii == 7013 :
 cnfTVPlay2 ( OOOooo )
elif iIiii == 7014 :
 CNF_Studio_Indexer . MV_Movies ( OOOooo )
elif iIiii == 7015 :
 CNF_Studio_Indexer . Movie_ByYear ( OOOooo )
elif iIiii == 7016 :
 CNF_Studio_Indexer . Resolve_CNF_Link ( I1Ii , OOOooo , ooo0O0o00O )
elif iIiii == 7017 :
 CNF_Studio_Indexer . Search_Movie ( )
elif iIiii == 7018 :
 oo0O ( )
elif iIiii == 7019 :
 CNF_Studio_Indexer . List_Movies ( OOOooo )
elif iIiii == 7020 :
 CNF_Studio_Indexer . Get_Movie_Page ( OOOooo )
elif iIiii == 7024 :
 CNF_Studio_Indexer . Box_Office ( OOOooo )
 if 24 - 24: OoooooooOO
elif iIiii == 8000 :
 ooo00 ( )
elif iIiii == 8001 :
 oO0ooo00o0o000Oo ( )
elif iIiii == 8002 :
 iiiIiIiI ( )
elif iIiii == 8003 :
 i1iiIIiII1 ( )
elif iIiii == 8004 :
 iiI1iiii1Iii ( )
elif iIiii == 8005 :
 iiIIIIiii ( )
elif iIiii == 8006 :
 iii1IiiiI1i1 ( I1Ii , OOOooo )
elif iIiii == 8030 :
 Oo00oo0000OO ( OOOooo )
elif iIiii == 8045 :
 ii1oOoO0ooO0000 ( OOOooo )
elif iIiii == 8046 :
 OOOOO ( OOOooo )
elif iIiii == 8047 :
 I1iiiI ( OOOooo )
elif iIiii == 8020 :
 ooo000o ( )
elif iIiii == 8021 :
 OOOOOO ( OOOooo )
elif iIiii == 8022 :
 oOO0O ( OOOooo )
elif iIiii == 8023 :
 oooo0 ( OOOooo )
elif iIiii == 8040 :
 Oo0 ( )
elif iIiii == 8041 :
 O0000Oo00o ( OOOooo )
elif iIiii == 8042 :
 Iiii1 ( OOOooo )
elif iIiii == 8043 :
 yt . PlayVideo ( OOOooo )
elif iIiii == 8044 :
 iI111II1ii ( OOOooo )
elif iIiii == 8060 :
 i1iI1i ( )
elif iIiii == 8061 :
 o0o0OoO0OOO0 ( OOOooo )
elif iIiii == 8064 :
 ii1IIiII111I ( )
elif iIiii == 8065 :
 O00OoOoO ( OOOooo )
elif iIiii == 8070 :
 ii1ii1i11I1I ( )
elif iIiii == 8071 :
 iiII1iiiiiii ( OOOooo )
elif iIiii == 7080 :
 iiIiii ( OOOooo )
elif iIiii == 8090 :
 Ii1ii1IiiiiiI ( )
elif iIiii == 8091 :
 ooIIIii11i1I ( OOOooo )
elif iIiii == 8092 :
 ooo0O00000oo0 ( OOOooo )
elif iIiii == 8081 :
 oOiIi ( )
elif iIiii == 8062 :
 IiIIIIii11i ( OOOooo )
elif iIiii == 8063 :
 OOOO0O0OOoo ( OOOooo )
elif iIiii == 8050 :
 I111IIiii1Ii ( )
elif iIiii == 8051 :
 II1 ( OOOooo )
elif iIiii == 8052 :
 iiIIIiIii ( OOOooo )
elif iIiii == 8085 :
 I1II ( )
elif iIiii == 8086 :
 iII1iI1IIiI ( OOOooo )
elif iIiii == 8087 :
 oO0O ( OOOooo )
elif iIiii == 8088 :
 OOoooO00o0o ( OOOooo , I1Ii )
elif iIiii == 9000 :
 ii1O000OOO0OOo ( )
elif iIiii == 1111 :
 oOoo00oO0O0OO ( )
elif iIiii == 9001 :
 iiII ( )
elif iIiii == 9002 :
 I11IIII1111II ( )
elif iIiii == 9003 :
 O00Ooo0ooo0 ( )
elif iIiii == 50 :
 IiIi1 ( OOOooo )
elif iIiii == 9020 :
 champlist ( )
elif iIiii == 9021 :
 Oooo0O0Oooo ( )
elif iIiii == 9022 :
 IiII1 ( )
elif iIiii == 9023 :
 ii111iI ( )
elif iIiii == 9024 :
 II1i1i1I1iII ( OOOooo )
elif iIiii == 9030 :
 ii11Ii1IiiI1 ( OOOooo )
elif iIiii == 9031 :
 O00o0o ( OOOooo )
elif iIiii == 9032 :
 OOoO0o0OOo0 ( OOOooo )
elif iIiii == 9033 :
 O0OoO0ooOOO ( OOOooo )
elif iIiii == 7085 :
 oOo ( OOOooo )
elif iIiii == 7086 :
 IIo0oo0OO ( OOOooo )
elif iIiii == 7087 :
 i1111iIII ( OOo0 )
elif iIiii == 9666 :
 i1I111II11 ( OOOooo )
elif iIiii == 10100 : o0OOooO ( )
elif iIiii == 10105 : iIiIi1iIIi11i ( OOOooo )
elif iIiii == 10106 : oO0O0o0O ( OOOooo )
elif iIiii == 10104 : O0oooOoO ( OOOooo )
elif iIiii == 10107 : iiiIiIIIiiiIiI1 ( )
elif iIiii == 10103 : o0oOoOo0 ( OOOooo )
elif iIiii == 10108 : OO00OoooO ( OOOooo )
elif iIiii == 10107 : iiiIiIIIiiiIiI1 ( )
elif iIiii == 10000 : Origin_Menu ( )
elif iIiii == 10001 : IIo00ooo ( )
elif iIiii == 10002 : OO0ooOoOO0OOo ( )
elif iIiii == 10003 : OO0oIiII1iiI ( )
elif iIiii == 10004 : I1 ( OOOooo )
elif iIiii == 10005 : iIIi1iI1I1IIi ( )
elif iIiii == 10006 : iiIIi1 ( OOOooo )
elif iIiii == 10007 : iI1 ( OOOooo , ooo0O0o00O )
elif iIiii == 10008 : III1III11II ( )
elif iIiii == 10009 : oO0oo0o00o0O ( )
elif iIiii == 10010 : i1I11 ( OOOooo )
elif iIiii == 10011 : OO0Oo ( OOOooo )
elif iIiii == 10012 : Oo0oOooOoOo ( OOOooo )
elif iIiii == 10013 : IiIioO0Oo00oo ( OOOooo )
elif iIiii == 10014 : Ii ( )
elif iIiii == 10015 : o0o00oO0oo000 ( )
elif iIiii == 10016 : O0OOOo ( OOOooo )
elif iIiii == 10017 : iIiI1IIiii11 ( )
elif iIiii == 10018 : iIiI1I1IIi11 ( )
elif iIiii == 10019 : IIoO00OoOo ( )
elif iIiii == 10020 : i1I1i1i ( )
elif iIiii == 10021 : oO00o ( )
elif iIiii == 10022 : ii11i ( OOOooo )
elif iIiii == 10023 : Ii1I11i11I1i ( I1Ii , OOOooo )
elif iIiii == 10024 : I111i1Ii1i1 ( OOOooo )
elif iIiii == 10025 : i1IIi1i1Ii1 ( )
elif iIiii == 10026 : oO0ooOO ( )
elif iIiii == 10027 : OOo0O0O000 ( )
elif iIiii == 10028 : OoOOo00 ( )
elif iIiii == 10029 : iI11Ii111 ( )
elif iIiii == 423 : iIIi1 ( OOOooo )
elif iIiii == 426 : I1I1I11Ii ( OOOooo )
elif iIiii == 10030 : Izle_Films ( )
elif iIiii == 10031 : Latest_Izle_Movies ( )
elif iIiii == 10032 : Izle_Genres ( )
elif iIiii == 10033 : Izle_Pop_Movies ( )
elif iIiii == 10034 : Izle_Boxsets ( )
elif iIiii == 10035 : Izle_Search ( )
elif iIiii == 10036 : Izle_Genres_Movie ( OOOooo )
elif iIiii == 10037 : Izle_Boxset_single ( OOOooo )
elif iIiii == 10038 : Izle_IFRAME ( )
elif iIiii == 10039 : Izle_Boxsets_Next ( OOOooo )
elif iIiii == 10040 : o0oOOOO0 ( )
elif iIiii == 10041 : Ii1Ii1I ( OOOooo )
elif iIiii == 10042 : OooOooO0O0o0 ( OOOooo )
elif iIiii == 10043 : oOo0Oo0O0O ( )
elif iIiii == 10044 : o0O00O ( OOOooo )
elif iIiii == 10045 : i1iiI ( I1Ii )
elif iIiii == 10046 : Ooo0Oo0o ( OOOooo )
elif iIiii == 10047 : I11II1i11 ( OOOooo )
elif iIiii == 10048 : IiI ( OOOooo )
elif iIiii == 10049 : i1I1iIii11 ( OOOooo )
elif iIiii == 10050 : Ii1iii ( )
elif iIiii == 10051 : IIIIIiiI ( )
elif iIiii == 10052 : iiii11i ( )
elif iIiii == 10053 : Addon ( OOOooo )
elif iIiii == 10054 : Oo00OOoO0oo ( OOOooo , I1Ii )
elif iIiii == 10055 :
 oo0oO ( "addFavorite" )
 try :
  I1Ii = I1Ii . split ( '\\ ' ) [ 1 ]
 except :
  pass
 try :
  I1Ii = I1Ii . split ( '  - ' ) [ 0 ]
 except :
  pass
 o0oO0Oo ( I1Ii , OOOooo , ooo0O0o00O , I1i11 , I11II )
elif iIiii == 10056 :
 oo0oO ( "rmFavorite" )
 try :
  I1Ii = I1Ii . split ( '\\ ' ) [ 1 ]
 except :
  pass
 try :
  I1Ii = I1Ii . split ( '  - ' ) [ 0 ]
 except :
  pass
 OO ( I1Ii )
elif iIiii == 10057 :
 oo0oO ( "getFavorites" )
 o0OO ( )
elif iIiii == 10058 : OooooO0oOOOO ( )
elif iIiii == 10059 : Donators_Guide ( )
elif iIiii == 10060 : OO0O0Oo000 ( )
elif iIiii == 10061 : iiiI ( )
elif iIiii == 10062 : iiII1i11i ( I1Ii , OOOooo , OOo0 )
elif iIiii == 10063 : oooiiI ( )
elif iIiii == 10064 : o0O ( )
elif iIiii == 10065 : O0O0o0oOOO ( OOOooo )
elif iIiii == 10066 : OO0000o ( OOOooo )
elif iIiii == 10068 : oooo0OOOO ( OOOooo )
elif iIiii == 10069 : O0o000Oo ( OOOooo )
elif iIiii == 10070 : ooOoO00 ( OOOooo )
elif iIiii == 10071 : Genie_Watch ( )
elif iIiii == 10072 : o0iI11I1II ( )
elif iIiii == 10073 : oooooo0O000o ( OOOooo )
elif iIiii == 10074 : O0O00Oo ( OOOooo )
elif iIiii == 10075 : o0o0O0O00oOOo ( ooo0O0o00O , I1Ii , OOOooo )
elif iIiii == 10076 : OO0OoOO0o0o ( OOOooo )
elif iIiii == 10077 : IiiiIIiIi1 ( OOOooo )
elif iIiii == 10078 : ii1Ii1I1Ii11i ( )
elif iIiii == 10079 : Genie_Watch_Tv_Shows ( )
elif iIiii == 10080 : Genie_Watch_Tv_Genre ( OOOooo )
elif iIiii == 10081 : Genie_Watch_TV_PlayRun ( OOOooo )
elif iIiii == 10082 : Genie_Watch_TV_Episodes ( OOOooo , ooo0O0o00O )
elif iIiii == 10083 : Genie_Watch_Tv_Recent ( OOOooo )
elif iIiii == 10084 : IiIIIi1iIi ( )
elif iIiii == 20000 : iIi1IIiI ( )
elif iIiii == 20001 : IiIiiiIii ( )
elif iIiii == 20002 : o0o0oOo000o0 ( OOOooo )
elif iIiii == 20003 : ii1IiIi11 ( OOOooo )
elif iIiii == 20004 : o00oo0000 ( OOOooo )
elif iIiii == 21004 : Ii1 ( )
elif iIiii == 21005 : I1iiiiii ( OOOooo )
elif iIiii == 21006 : I11iiii1I ( OOOooo )
elif iIiii == 21007 : oooo00i1 ( OOOooo )
elif iIiii == 30000 : iiIII1II ( )
elif iIiii == 30001 : oOooO00o0O ( )
elif iIiii == 10012 : Resolve ( OOOooo )
elif iIiii == 30003 : i1iiiIii11 ( )
elif iIiii == 30004 : ooOOOOo0 ( OOOooo )
elif iIiii == 30005 : ooO00O00oOO ( OOOooo )
elif iIiii == 30006 : OO0O0ooOOO00 ( )
elif iIiii == 30007 : OO00OOoO0o ( )
elif iIiii == 30008 : oooo00 ( OOOooo )
elif iIiii == 30009 : iIi1IiI ( OOOooo )
elif iIiii == 30010 : i1IiiI1iIi ( OOOooo )
elif iIiii == 30011 : iIiI ( )
elif iIiii == 30012 : ii1I11iIiIII1 ( )
elif iIiii == 30013 : IIIii1iiIi ( )
elif iIiii == 30014 : Ooo0Oo0oo0 ( )
if 83 - 83: O0 / Ooo00oOo00o
xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
