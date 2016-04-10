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
O00ooOO = xbmc . translatePath ( 'special://home/addons/repository.GenieTv' )
I1iII1iiII = xbmc . translatePath ( 'special://home/addons/' )
iI1Ii11111iIi = xbmc . translatePath ( 'special://home/addonsbroke/' )
i1i1II = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'
O0oo0OO0 = 'plugin.video.GenieTv'
I1i1iiI1 = [ 'plugin.video.GenieTv' , 'script.module.addon.common' , 'repository.GenieTv' ]
iiIIIII1i1iI = xbmcaddon . Addon ( id = O0oo0OO0 )
o0oO0 = xbmc . translatePath ( 'special://home/media' )
oo00 = 'plugin.video.GenieTv'
o00 = xbmcgui . DialogProgress ( )
Oo0oO0ooo = "[COLORgreen]GenieTv[/COLOR]"
o0oOoO00o = Net ( )
i1 = xbmcgui . Dialog ( )
oOOoo00O0O = base64 . decodestring
i1111 = iiIIIII1i1iI . getSetting ( 'Build' )
i11 = iiIIIII1i1iI . getSetting ( 'Local' )
I11 = iiIIIII1i1iI . getSetting ( 'Remote' )
Oo0o0000o0o0 = iiIIIII1i1iI . getSetting ( 'LocalM3u' )
oOo0oooo00o = iiIIIII1i1iI . getSetting ( 'User' )
oO0o0o0ooO0oO = iiIIIII1i1iI . getSetting ( 'Pass' )
oo0o0O00 = iiIIIII1i1iI . getSetting ( 'AdultPass' )
oO = xbmcgui . Dialog ( )
i1iiIIiiI111 = xbmc . translatePath ( 'special://home/' )
oooOOOOO = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + O0oo0OO0 , 'fanart.jpg' ) )
i1iiIII111ii = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + O0oo0OO0 , 'icon.png' , oooOOOOO , '' ) )
i1iIIi1 = ( oOOoo00O0O ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vR2VuaWVBcnQv' ) )
ii11iIi1I = ( oOOoo00O0O ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vR2VuaWVBcnQvb3JpZ2luLnBuZw==' ) )
iI111I11I1I1 = "2.5.7"
OOooO0OOoo = xbmc . translatePath ( 'special://database' )
iIii1 = xbmc . translatePath ( 'special://home/userdata/addon_data/plugin.video.GenieTV' )
oOOoO0 = xbmc . translatePath ( 'special://thumbnails' ) ;
O0OoO000O0OO = "GenieTv"
iiI1IiI = ( oOOoo00O0O ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20=' ) )
II = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv' ) )
ooOoOoo0O = 'http://'
OooO0 = base64 . decodestring ( 'LnBocA==' )
II11iiii1Ii = base64 . decodestring ( 'aHR0cDovL2JhY2syYmFzaWNzYnVpbGQuY28udWsvdGVzdC8=' )
OO0o = [ ]
Ooo = iiIIIII1i1iI . getLocalizedString
O0o0Oo = CookieJar ( )
Oo00OOOOO = urllib2 . build_opener ( urllib2 . HTTPCookieProcessor ( O0o0Oo ) )
Oo00OOOOO . addheaders = [ ( 'User-Agent' , 'Mozilla/5.0' ) ]
O0O = int ( sys . argv [ 1 ] )
O00o0OO = xbmc . translatePath ( iiIIIII1i1iI . getAddonInfo ( 'profile' ) . decode ( 'utf-8' ) )
I11i1 = os . path . join ( O00o0OO , 'favorites' )
iIi1ii1I1 = iIii1 + '/addons.ini'
o0 = xbmc . translatePath ( 'special://home/userdata/' )
I11II1i = xbmc . translatePath ( 'special://home/userdatabroke/' )
IIIII = ( oOOoo00O0O ( 'aHR0cDovL3NlZWR1cmdyZWVkLngxMGhvc3QuY29tL29yaWdpbi8=' ) )
ooooooO0oo = xbmc . translatePath ( os . path . join ( 'special://home/userdata/addon_data/script.ivueguide/master.db' ) )
IIiiiiiiIi1I1 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , 'favourites.xml' ) )
I1IIIii = xbmc . translatePath ( os . path . join ( 'special://home/userdata/addon_data/plugin.video.GenieTv/favorites' ) )
if os . path . exists ( I11i1 ) == True :
 oOoOooOo0o0 = open ( I11i1 ) . read ( )
else : oOoOooOo0o0 = [ ]
OOOO = iiIIIII1i1iI . getSetting ( 'debug' )
if os . path . exists ( iIii1 ) == False :
 os . makedirs ( iIii1 )
 if 87 - 87: O0ooOooooO / i1I111II1I - Oooo0Ooo000 - iI - i1I111ii1II1i / OoOo00o
def o0OOoo0OO0OOO ( ) :
 if not os . path . exists ( O00ooOO ) :
  i1 . ok ( "[COLOR=white]Incompatible[/COLOR]" , "Unfortunately GenieTv will only work with" , 'its official repo please install from trusted source' , '' )
  iI1iI1I1i1I = 'genie tv repo not being installed '
  iIi11Ii1 ( iI1iI1I1i1I )
 Ii11iII1 ( )
 Oo0O0O0ooO0O ( )
 if iiIIIII1i1iI . getSetting ( 'My Build' ) == 'true' :
  IIIIii ( '[COLORgreen]WIZARD[/COLOR]' , iiI1IiI , 4001 , i1iIIi1 + 'MB.png' , oooOOOOO , '' )
 if iiIIIII1i1iI . getSetting ( 'Streams' ) == 'true' :
  IIIIii ( '[COLORgreen]STREAMS[/COLOR]' , iiI1IiI , 4002 , i1iIIi1 + 'streams.png' , oooOOOOO , '' )
 if iiIIIII1i1iI . getSetting ( 'Music' ) == 'true' :
  IIIIii ( '[COLORgreen]Music[/COLOR]' , iiI1IiI , 4003 , i1iIIi1 + 'MUSIC.png' , oooOOOOO , '' )
  if 70 - 70: o00OO00OoO / OOO0OOo - OOO0OOo + OOOo0
 if iiIIIII1i1iI . getSetting ( 'Builders Toolbox' ) == 'true' :
  IIIIii ( '[COLORgreen]BUILDERS TOOLBOX[/COLOR]' , iiI1IiI , 32 , i1iIIi1 + 'builderstoolbox.png' , oooOOOOO , '' )
 if iiIIIII1i1iI . getSetting ( 'Source List' ) == 'true' :
  IIIIii ( '[COLORgreen]SOURCE LIST[/COLOR]' , iiI1IiI , 46 , i1iIIi1 + 'sources.png' , oooOOOOO , '' )
 if iiIIIII1i1iI . getSetting ( 'Maintainance' ) == 'true' :
  IIIIii ( '[COLORgreen]MAINTENANCE[/COLOR]' , iiI1IiI , 3 , i1iIIi1 + 'MAIN6.png' , oooOOOOO , '' )
 if iiIIIII1i1iI . getSetting ( 'Addons' ) == 'true' :
  IIIIii ( '[COLORgreen]ADDONS[/COLOR]' , '' , 10050 , i1iIIi1 + 'ADDONS.png' , oooOOOOO , '' )
 if iiIIIII1i1iI . getSetting ( 'APK Tool' ) == 'true' :
  IIIIii ( '[COLORgreen]APK TOOL[/COLOR]' , iiI1IiI , 2 , i1iIIi1 + 'APK.png' , oooOOOOO , '' )
 if iiIIIII1i1iI . getSetting ( 'Rss Feed' ) == 'true' :
  IIIIii ( '[COLORgreen]GenieTv RSS Feed[/COLOR]' , iiI1IiI , 39 , i1iIIi1 + 'RSS.png' , oooOOOOO , '' )
 if iiIIIII1i1iI . getSetting ( 'Addons Packs' ) == 'true' :
  IIIIii ( '[COLORgreen]ADDONS PACKS[/COLOR]' , iiI1IiI , 30 , i1iIIi1 + 'ADDONP.png' , oooOOOOO , '' )
 O00Oo000ooO0 ( 'movies' , 'MAIN' )
 if 100 - 100: O0 + OoOo00o - i1I111II1I + i11iIiiIii * iI
def iII ( ) :
 IIIIii ( '[COLORgreen]BACKUP MY BUILD[/COLOR]' , iiI1IiI , 10060 , i1iIIi1 + 'MB.png' , oooOOOOO , '' )
 IIIIii ( '[COLORgreen]RESTORE MY BUILD[/COLOR]' , iiI1IiI , 49 , i1iIIi1 + 'MB.png' , oooOOOOO , '' )
 IIIIii ( '[COLORgreen]WIPE GENIE[/COLOR]' , iiI1IiI , 41 , i1iIIi1 + 'wipegenie.png' , oooOOOOO , '' )
 IIIIii ( '[COLORgreen]WISHES PC[/COLOR]' , iiI1IiI , 1 , i1iIIi1 + 'WISHESPC.png' , oooOOOOO , '' )
 IIIIii ( '[COLORgreen]WISHES ANDROID[/COLOR]' , iiI1IiI , 44 , i1iIIi1 + 'WISHESAN.png' , oooOOOOO , '' )
 O00Oo000ooO0 ( 'movies' , 'MAIN' )
def o0ooOooo000oOO ( ) :
 if oo0o0O00 == '5knuckleshuffle' :
  IIIIii ( '[COLORgreen]XVID[/COLOR]' , iiI1IiI , 10100 , i1iIIi1 + 'JIZBOX.png' , oooOOOOO , '' )
  if iiIIIII1i1iI . getSetting ( 'Favourites' ) == 'true' :
   IIIIii ( '[COLORgreen]FAVOURITES[/COLOR]' , iiI1IiI , 10057 , i1iIIi1 + 'FAVORITES.png' , oooOOOOO , '' )
 if iiIIIII1i1iI . getSetting ( 'Search' ) == 'true' :
  IIIIii ( '[COLORgreen]SEARCH[/COLOR]' , iiI1IiI , 9000 , i1iIIi1 + 'search.png' , oooOOOOO , '' )
 IIIIii ( '[COLORgreen]Live TV[/COLOR]' , iiI1IiI , 4009 , i1iIIi1 + 'GTVIPTV.png' , oooOOOOO , '' )
 IIIIii ( '[COLORgreen]MOVIES[/COLOR]' , iiI1IiI , 4004 , i1iIIi1 + 'MOVIESv.png' , oooOOOOO , '' )
 IIIIii ( '[COLORgreen]TV SHOWS[/COLOR]' , iiI1IiI , 4005 , i1iIIi1 + 'TVSHOWSv.png' , oooOOOOO , '' )
 IIIIii ( '[COLORgreen]STREAM TEAM[/COLOR]' , iiI1IiI , 4006 , i1iIIi1 + 'streamteam.png' , oooOOOOO , '' )
 IIIIii ( '[COLORgreen]KIDS[/COLOR]' , iiI1IiI , 4007 , i1iIIi1 + 'KIDSv.png' , oooOOOOO , '' )
 IIIIii ( '[COLORgreen]HOBBIES[/COLOR]' , iiI1IiI , 4008 , i1iIIi1 + 'hobbies.png' , oooOOOOO , '' )
 if iiIIIII1i1iI . getSetting ( 'YOUTUBE' ) == 'true' :
  IIIIii ( '[COLORgreen]SEARCH YOUTUBE[/COLOR]' , iiI1IiI , 10064 , i1iIIi1 + 'youtube.png' , oooOOOOO , '' )
 if iiIIIII1i1iI . getSetting ( 'REQUESTS' ) == 'true' :
  IIIIii ( '[COLORgreen]REQUESTS[/COLOR]' , iiI1IiI + ( oOOoo00O0O ( 'L1JFUVVFU1RTLnBocA==' ) ) , 10066 , i1iIIi1 + 'requests.png' , oooOOOOO , '' )
 if iiIIIII1i1iI . getSetting ( 'Stand Up' ) == 'true' :
  IIIIii ( '[COLORgreen]STAND UP[/COLOR]' , '' , 10003 , i1iIIi1 + 'ORIGINSTANDUP.png' , oooOOOOO , '' )
 if iiIIIII1i1iI . getSetting ( 'Documentaries' ) == 'true' :
  IIIIii ( '[COLORgreen]DOCUMENTARIES[/COLOR]' , iiI1IiI , 8040 , i1iIIi1 + 'documentary.png' , oooOOOOO , '' )
 if iiIIIII1i1iI . getSetting ( 'Disclose' ) == 'true' :
  IIIIii ( '[COLORgreen]DISCLOSE TV[/COLOR]' , iiI1IiI , 7001 , i1iIIi1 + 'disclose.png' , oooOOOOO , '' )
  if 59 - 59: OoOoOO00 + OoooooooOO * I1IiI + i1IIi
  if 58 - 58: OoOoOO00 * i1I111II1I * ii11ii1ii / i1I111II1I
 if iiIIIII1i1iI . getSetting ( 'Playlist Loader' ) == 'true' :
  IIIIii ( '[COLORgreen]PLAYLIST LOADER[/COLOR]' , iiI1IiI , 3000 , i1iIIi1 + 'loader.png' , oooOOOOO , '' )
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
 IIIIii ( '[COLORgreen]SEARCH MOVIES[/COLOR]' , iiI1IiI , 9001 , i1iIIi1 + 'search.png' , oooOOOOO , '' )
 if iiIIIII1i1iI . getSetting ( 'Popcorn Box' ) == 'true' :
  IIIIii ( '[COLORgreen]POPCORN BOX[/COLOR]' , iiI1IiI , 7061 , i1iIIi1 + 'popcorn.png' , oooOOOOO , '' )
 IIIIii ( '[COLORgreen]Film Trailers[/COLOR]' , oOOoo00O0O ( 'aHR0cDovL3RoZW1vdmllYm94Lm5ldC9leHBsb3Jl' ) , 10068 , i1iIIi1 + 'movietrailers.png' , oooOOOOO , '' )
 if iiIIIII1i1iI . getSetting ( 'CLASSIC MOVIES' ) == 'true' :
  IIIIii ( '[COLORgreen]CLASSIC MOVIES[/COLOR]' , '' , 8060 , i1iIIi1 + 'classicmovies.png' , oooOOOOO , '' )
 O00Oo000ooO0 ( 'movies' , 'MAIN' )
def oooooOoo0ooo ( ) :
 if iiIIIII1i1iI . getSetting ( 'G-tv' ) == 'true' :
  IIIIii ( '[COLORgreen]G-Tv PRIVATE LIST[/COLOR]' , '' , 10058 , i1iIIi1 + 'GTVIPTV.png' , oooOOOOO , '' )
 if iiIIIII1i1iI . getSetting ( 'TV GUIDE' ) == 'true' :
  I1I1IiI1 ( '[COLORgreen]TV GUIDE[/COLOR]' , '' , 10063 , i1iIIi1 + 'GTVIPTV.png' , oooOOOOO , '' )
 I1I1IiI1 ( '[COLORgreen]Link GTV Donators Username and Password to Guide[/COLOR]' , '' , 4010 , i1iIIi1 + 'GTVIPTV.png' , oooOOOOO , '' )
 if 5 - 5: OOooOOo * OOO0OOo + I1IiI . i1I111II1I + I1IiI
 if 91 - 91: O0
def oOOo0 ( ) :
 IIIIii ( '[COLORgreen]SEARCH SERIES[/COLOR]' , iiI1IiI , 9002 , i1iIIi1 + 'search.png' , oooOOOOO , '' )
 if iiIIIII1i1iI . getSetting ( 'Dizzy Tv' ) == 'true' :
  IIIIii ( '[COLORgreen]DIZZY TV[/COLOR]' , '' , 10018 , i1iIIi1 + 'dtv.png' , oooOOOOO , '' )
 if iiIIIII1i1iI . getSetting ( 'Watch Series' ) == 'true' :
  IIIIii ( '[COLORgreen]WATCH SERIES[/COLOR]' , '' , 10040 , i1iIIi1 + 'WATCHSERIES.png' , oooOOOOO , '' )
 IIIIii ( '[COLORgreen]iWATCH SERIES[/COLOR]' , '' , 8020 , i1iIIi1 + 'iwatch.png' , oooOOOOO , '' )
 if iiIIIII1i1iI . getSetting ( 'Recent Episodes' ) == 'true' :
  IIIIii ( '[COLORgreen]RECENT EPISODES[/COLOR]' , iiI1IiI , 8081 , i1iIIi1 + 'recent.png' , oooOOOOO , '' )
 if iiIIIII1i1iI . getSetting ( 'CLASSIC TV' ) == 'true' :
  IIIIii ( '[COLORgreen]CLASSIC TV[/COLOR]' , iiI1IiI , 8064 , i1iIIi1 + 'classictv.png' , oooOOOOO , '' )
 IIIIii ( '[COLORgreen]TV Show Trailers[/COLOR]' , oOOoo00O0O ( 'aHR0cHM6Ly93d3cueW91dHViZS5jb20vd2F0Y2g/dj03WkZJUzJBcUF6OCZsaXN0PVBMM2t4NWgyVHJZR3dwVzBWYk5lbnBqLUJLTUJUR2dKUEU=' ) , 10069 , i1iIIi1 + 'tvtrailers.png' , oooOOOOO , '' )
 IIIIii ( '[COLORgreen]TV Show Schedule[/COLOR]' , oOOoo00O0O ( 'aHR0cDovL3d3dy5wb2dkZXNpZ24uY28udWsvY2F0Lw==' ) , 10070 , i1iIIi1 + 'tvschedule.png' , oooOOOOO , '' )
 O00Oo000ooO0 ( 'movies' , 'MAIN' )
def oo00O00oO ( ) :
 if iiIIIII1i1iI . getSetting ( 'Scooby Streams' ) == 'true' :
  IIIIii ( '[COLORgreen]SCOOBY STREAMS[/COLOR]' , iiI1IiI , 1023 , i1iIIi1 + 'scoob.png' , oooOOOOO , '' )
 if iiIIIII1i1iI . getSetting ( 'The Reaper' ) == 'true' :
  IIIIii ( '[COLORgreen]THE REAPER[/COLOR]' , ( oOOoo00O0O ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9UaGVfUmVhcGVyL21haW4ucGhw' ) ) , 1016 , i1iIIi1 + 'reap.png' , oooOOOOO , '' )
 if iiIIIII1i1iI . getSetting ( 'Pandoras Box' ) == 'true' :
  IIIIii ( '[COLORgreen]PANDORAS BOX[/COLOR]' , iiI1IiI , 10025 , i1iIIi1 + 'PANDORASBOX.png' , oooOOOOO , '' )
 if iiIIIII1i1iI . getSetting ( 'HeroVision' ) == 'true' :
  IIIIii ( '[COLORgreen]HEROVISION[/COLOR]' , ( oOOoo00O0O ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC9tYWluLnBocA==' ) ) , 1016 , i1iIIi1 + 'hero.png' , oooOOOOO , '' )
 if iiIIIII1i1iI . getSetting ( 'Silent Hunter' ) == 'true' :
  IIIIii ( '[COLORgreen]SILENT HUNTER[/COLOR]' , ( oOOoo00O0O ( 'aHR0cDovLzUuMTM1LjIwNy45Ni8=' ) ) , 1006 , i1iIIi1 + 'SILENTHUNTER.png' , oooOOOOO , '' )
 if iiIIIII1i1iI . getSetting ( 'Redemption Streams' ) == 'true' :
  IIIIii ( '[COLORgreen]Redemption Streams[/COLOR]' , ( oOOoo00O0O ( 'aHR0cDovL3JlZGVtcHRpb25idWlsZC4xNm1iLmNvbS9SZWRlbXB0aW9uL21haW4ucGhw' ) ) , 1016 , i1iIIi1 + 'redemption.png' , oooOOOOO , '' )
 O00Oo000ooO0 ( 'movies' , 'MAIN' )
def iIiIIIi ( ) :
 IIIIii ( '[COLORgreen]SEARCH CARTOONS[/COLOR]' , '' , 10005 , i1iIIi1 + 'search.png' , oooOOOOO , '' )
 if iiIIIII1i1iI . getSetting ( 'WCO' ) == 'true' :
  IIIIii ( '[COLORgreen]WATCH CARTOONS ONLINE[/COLOR]' , iiI1IiI , 21004 , i1iIIi1 + 'watchcartoons.png' , oooOOOOO , '' )
 if iiIIIII1i1iI . getSetting ( 'Cartoons' ) == 'true' :
  IIIIii ( '[COLORgreen]CARTOONS[/COLOR]' , '' , 10001 , i1iIIi1 + 'ORIGINCARTOON.png' , oooOOOOO , '' )
 if iiIIIII1i1iI . getSetting ( 'Anime' ) == 'true' :
  IIIIii ( '[COLORgreen]AnimeLand[/COLOR]' , ( oOOoo00O0O ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2R1YmJlZC1hbmltZQ==' ) ) , 10004 , i1iIIi1 + 'anime.png' , oooOOOOO , '' )
 O00Oo000ooO0 ( 'movies' , 'MAIN' )
def ooo00OOOooO ( ) :
 if iiIIIII1i1iI . getSetting ( 'Football' ) == 'true' :
  IIIIii ( '[COLORgreen]FOOTBALL[/COLOR]' , '' , 10002 , i1iIIi1 + 'ORIGINFOOTBALL.png' , oooOOOOO , '' )
 if iiIIIII1i1iI . getSetting ( 'Fitness' ) == 'true' :
  IIIIii ( '[COLORgreen]FITNESS[/COLOR]' , ( oOOoo00O0O ( 'aHR0cHM6Ly93d3cuZml0bmVzc2JsZW5kZXIuY29tL3ZpZGVvcw==' ) ) , 7085 , i1iIIi1 + 'FITNESS.png' , oooOOOOO , '' )
 if iiIIIII1i1iI . getSetting ( 'Go Fishing' ) == 'true' :
  IIIIii ( '[COLORgreen]Go Fishing[/COLOR]' , iiI1IiI , 8090 , i1iIIi1 + 'gofish.png' , oooOOOOO , '' )
 if iiIIIII1i1iI . getSetting ( 'GenieTv Kitchen' ) == 'true' :
  IIIIii ( '[COLORgreen]GenieTv Kitchen[/COLOR]' , ( oOOoo00O0O ( 'aHR0cDovL2Zvb2QubmR0di5jb20vdmlkZW9z' ) ) , 8045 , i1iIIi1 + 'geniekitchen.png' , oooOOOOO , '' )
 O00Oo000ooO0 ( 'movies' , 'MAIN' )
 if 67 - 67: Oooo0Ooo000 * O0ooOooooO * ii11ii1ii + i1I111II1I / i1IIi
 if 11 - 11: iI + i1I111ii1II1i - OOO0OOo * O0ooOooooO % i11iIiiIii - o00OO00OoO
 if 83 - 83: Oooo0Ooo000 / OOOo0
def Oo0O0O0ooO0O ( ) :
 iIIiIi1iIII1 = OooOOOOo ( 'http://architects.x10host.com/wizarddelete.txt' )
 oo0O0oO = re . compile ( '<unwanted_wizard =(.+?)</unwanted_wizard>' ) . findall ( iIIiIi1iIII1 )
 for ooooo in oo0O0oO :
  print ooooo
  ooooo = ( str ( ooooo ) )
  if os . path . exists ( xbmc . translatePath ( ooooo ) ) :
   II1I = os . path . join ( o0 , 'guisettings.xml' )
   O0i1II1Iiii1I11 = open ( II1I , "w+" )
   if 9 - 9: ii11ii1ii / Oo - OOOo0 / OoooooooOO / iIii1I11I1II1 - OOooOOo
   O0i1II1Iiii1I11 . write ( r'.' )
   o00oooO0Oo ( )
  else :
   pass
   if 78 - 78: iI % o00OO00OoO + ii11ii1ii
def Ii11iII1 ( ) :
 iIIiIi1iIII1 = OooOOOOo ( 'http://architects.x10host.com/testdelete.txt' )
 oo0O0oO = re . compile ( '<unwanted_addon =(.+?)</unwanted_addon>' ) . findall ( iIIiIi1iIII1 )
 for iI1iI1I1i1I in oo0O0oO :
  iI1iI1I1i1I = ( str ( iI1iI1I1i1I ) )
  if os . path . exists ( xbmc . translatePath ( iI1iI1I1i1I ) ) :
   iIi11Ii1 ( iI1iI1I1i1I )
   OOooOoooOoOo ( )
  else :
   pass
   if 84 - 84: OoOo00o
def iIi11Ii1 ( addon ) :
 i1 . ok ( "[COLOR=white]Incompatible[/COLOR]" , "Unfortunately GenieTv will not work with" , addon , 'please remove then reinstall genie' )
 II1I = os . path . join ( II , 'default.py' )
 O0i1II1Iiii1I11 = open ( II1I , "w+" )
 if 86 - 86: I1IiI - iI - Ooo00oOo00o * i1I111ii1II1i
 O0i1II1Iiii1I11 . write ( r'Genie Tv will not work with certain addons in an attempt to bring you original content from the best developers' )
 O0i1II1Iiii1I11 . write ( r'and not those simply out to profit or make a name for themselves off others work' )
 O0i1II1Iiii1I11 . write ( r'Please remove' + unwanted_addons + 'if you would like to use genie tv then uninstall and reinstall from official repo' )
 if 66 - 66: OoooooooOO + O0
 if 11 - 11: Oooo0Ooo000 + OoooooooOO - Ooo00oOo00o / OOooOOo + Oo . OoOoOO00
def o00oooO0Oo ( ) :
 iIIiIi1iIII1 = OooOOOOo ( oOOoo00O0O ( 'aHR0cDovL3d3dy5wb2dkZXNpZ24uY28udWsvY2F0Lw==' ) )
 i1Iii1i1I = re . compile ( '<tr>.+?title="(.+?)">(.+?)</tr>' , re . DOTALL ) . findall ( iIIiIi1iIII1 )
 for OOoO00 , i1Iii1i1I in i1Iii1i1I :
  OOoO00 = OOoO00
  oo0O0oO = re . compile ( '<p><a href=".+?" rel=".+?">(.+?)\n</a>.+?<br /><a href=".+?">(.+?)</a>.+?</p>' , re . DOTALL ) . findall ( str ( i1Iii1i1I ) )
  for IiI111111IIII , i1Ii in oo0O0oO :
   ii111iI1iIi1 ( OOoO00 , IiI111111IIII , i1Ii )
   if 78 - 78: Ooo00oOo00o . i1I111II1I + Ooo00oOo00o / Oooo0Ooo000 / Ooo00oOo00o
   if 54 - 54: I1IiI % i1I111ii1II1i
   if 37 - 37: I1IiI * Oo / OOO0OOo - i1I111ii1II1i % OoOoOO00 . O0ooOooooO
   if 88 - 88: i1I111ii1II1i . OoOoOO00 * OoOoOO00 % o00OO00OoO
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
def ii ( ) :
 IIIIii ( 'Genre' , oOOoo00O0O ( 'aHR0cDovL2ltb3ZpZW1heC5zZS9tb3ZpZXMv' ) , 10073 , i1iIIi1 + 'genievision.png' , oooOOOOO , '' )
 IIIIii ( 'Most Viewed' , oOOoo00O0O ( 'aHR0cDovL2ltb3ZpZW1heC5zZS9tb3ZpZXMv' ) , 10077 , i1iIIi1 + 'genievision.png' , oooOOOOO , '' )
 IIIIii ( 'Box Office' , oOOoo00O0O ( 'aHR0cDovL2ltb3ZpZW1heC5zZS9jYXRlZ29yeS9ib3gtb2ZmaWNlLw==' ) , 10074 , i1iIIi1 + 'genievision.png' , oooOOOOO , '' )
 IIIIii ( 'Search' , '' , 10078 , i1iIIi1 + 'genievision.png' , oooOOOOO , '' )
 if 5 - 5: OOO0OOo - OoOoOO00 - OoooooooOO % iI + OOOo0 * iIii1I11I1II1
def I1I1II1I11 ( ) :
 IIiiIiII1Ii = i1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oo00oOO000oO0 = 'http://imoviemax.se/?s=' + ( IIiiIiII1Ii ) . replace ( ' ' , '+' )
 iIIII11I1II = oo00oOO000oO0 . lower ( )
 Ii1I ( iIIII11I1II )
def IiI1i ( url ) :
 o0O = [ ]
 iIIiIi1iIII1 = OooOOOOo ( url )
 oo0O0oO = re . compile ( '<li class="cat-item cat-item-.+? "><a href="(.+?)">(.+?)</a><i>(.+?)</i></li>' ) . findall ( iIIiIi1iIII1 )
 for url , IiI111111IIII , o00iI in oo0O0oO :
  if IiI111111IIII in o0O :
   pass
  else :
   IIIIii ( IiI111111IIII + ' - ' + o00iI + ' Films' , url , 10074 , i1iIIi1 + 'genievision.png' , oooOOOOO , '' )
   o0O . append ( IiI111111IIII )
   if 90 - 90: o00OO00OoO % iI - iIii1I11I1II1 - iIii1I11I1II1 / i11iIiiIii % ii11ii1ii
def IIii11I1 ( url ) :
 iIIiIi1iIII1 = OooOOOOo ( url )
 oo0O0oO = re . compile ( '<li>.+?<b>.+?</b>.+?<a href="(.+?)">(.+?)</a>.+?<span>(.+?)</span>' , re . DOTALL ) . findall ( iIIiIi1iIII1 )
 for url , IiI111111IIII , oOO0O00Oo0O0o in oo0O0oO :
  IIIIii ( IiI111111IIII + ' - Views:' + oOO0O00Oo0O0o , url , 10075 , i1iIIi1 + 'genievision.png' , oooOOOOO , '' )
  if 13 - 13: OoooooooOO
  if 33 - 33: o00OO00OoO + i1I111ii1II1i * O0ooOooooO / iIii1I11I1II1 - OOOo0
def Ii1I ( url ) :
 O0oO = [ ]
 iIIiIi1iIII1 = OooOOOOo ( url )
 next = re . compile ( "<link rel='next' href='(.+?)' />" ) . findall ( iIIiIi1iIII1 )
 for next in next :
  IIIIii ( 'NEXT PAGE' , next , 10074 , i1iIIi1 + 'Next.png' , oooOOOOO , '' )
 oo0O0oO = re . compile ( '<div class="movie">.+?<img src="(.+?)" alt="(.+?)" />.+?<a href="(.+?)"><span class="player"></span></a>' , re . DOTALL ) . findall ( iIIiIi1iIII1 )
 for OO0ooOOO0OOO , IiI111111IIII , url in oo0O0oO :
  IIIIii ( IiI111111IIII , url , 10075 , OO0ooOOO0OOO , OO0ooOOO0OOO , '' )
  O0oO . append ( IiI111111IIII )
  if 63 - 63: I1IiI * i1I111ii1II1i
def ooiIi1 ( img , name , url ) :
 img = img
 name = name
 iIIiIi1iIII1 = OooOOOOo ( url )
 oo0O0oO = re . compile ( '<div id="(.+?)" class="player-content"><iframe class="playerframe" src="(.+?)" scrolling="no".+?</iframe></div>' ) . findall ( iIIiIi1iIII1 )
 for OoOOoOooooOOo , url in oo0O0oO :
  print '>>>>>>>>>>>>>>>>>>>>>>>>>>> before' + url
  oOo0O = ( url ) . replace ( 'player' , 'watch' ) + '&fv=&sou='
  print '<<<<<<<<<<<<<<<<<<<<<<<<<<< after' + oOo0O
  oo0O0 = ( OoOOoOooooOOo ) . replace ( 'play-' , 'Server ' )
  I1I1IiI1 ( oo0O0 , oOo0O , 10076 , img , img , '' )
  if 22 - 22: I1IiI . i1I111II1I * I1IiI
def O000OOO ( url ) :
 iIIiIi1iIII1 = OooOOOOo ( url )
 oo0O0oO = re . compile ( '<source src="(.+?)" type="video/mp4">' ) . findall ( iIIiIi1iIII1 )
 for IIo0o0O0O00oOOo in oo0O0oO :
  if '=m' in IIo0o0O0O00oOOo :
   iIIIiIi ( IIo0o0O0O00oOOo )
  elif 'php' in IIo0o0O0O00oOOo :
   O000OOO ( url )
  else :
   iIIiIi1iIII1 = OooOOOOo ( IIo0o0O0O00oOOo )
   oo0O0oO = re . compile ( 'content="(.+?)">' ) . findall ( iIIiIi1iIII1 )
   for OO0O0 in oo0O0oO :
    iIIIiIi ( IIo0o0O0O00oOOo )
    if 30 - 30: i1I111II1I + ii11ii1ii * Oooo0Ooo000 % i11iIiiIii % I1IiI
    if 97 - 97: ii11ii1ii % ii11ii1ii % O0ooOooooO / i1I111ii1II1i - iIii1I11I1II1
    if 69 - 69: o00OO00OoO
def ii1I1 ( url ) :
 iIIiIi1iIII1 = OooOOOOo ( url )
 OooooOOoo0 = re . compile ( '<td id=".+?" class="today">.+?title="(.+?)">(.+?)</td>' , re . DOTALL ) . findall ( iIIiIi1iIII1 )
 for OOoO00 , i1I1IiiIi1i in OooooOOoo0 :
  print 'there ><><><><><><><><><><><><'
  OOoO00 = OOoO00
  oo0O0oO = re . compile ( '<p><a href=".+?" rel=".+?">(.+?)</a>.+?<br /><a href=".+?">(.+?)</a>.+?</p>' , re . DOTALL ) . findall ( str ( i1I1IiiIi1i ) )
  for IiI111111IIII , i1Ii in oo0O0oO :
   print 'here <><><><><><><><><><><><>'
   IIIIii ( '[COLORred]' + OOoO00 + '[/COLOR] - ' + IiI111111IIII + ' - [COLORgreen]' + i1Ii + '[/COLOR]' , oOOoo00O0O ( 'aHR0cDovL3d3dy5wb2dkZXNpZ24uY28udWsvY2F0Lw==' ) , 10070 , i1iIIi1 + 'loader.png' , oooOOOOO , '' )
 i1Iii1i1I = re . compile ( '<td id=".+?" class="day">.+?title="(.+?)">(.+?)</td>' , re . DOTALL ) . findall ( iIIiIi1iIII1 )
 for OOoO00 , iiI11ii1I1 in i1Iii1i1I :
  print 'there ><><><><><><><><><><><><'
  OOoO00 = OOoO00
  oo0O0oO = re . compile ( '<p><a href=".+?" rel=".+?">(.+?)</a>.+?<br /><a href=".+?">(.+?)</a>.+?</p>' , re . DOTALL ) . findall ( str ( iiI11ii1I1 ) )
  for IiI111111IIII , i1Ii in oo0O0oO :
   print 'here <><><><><><><><><><><><>'
   IIIIii ( '[COLORred]' + OOoO00 + '[/COLOR] - ' + IiI111111IIII + ' - [COLORgreen]' + i1Ii + '[/COLOR]' , oOOoo00O0O ( 'aHR0cDovL3d3dy5wb2dkZXNpZ24uY28udWsvY2F0Lw==' ) , 10070 , i1iIIi1 + 'loader.png' , oooOOOOO , '' )
   if 82 - 82: OoOoOO00 % Oooo0Ooo000 / Ooo00oOo00o + I1IiI / OOooOOo / o00OO00OoO
   if 70 - 70: O0ooOooooO
   if 59 - 59: OOooOOo % O0ooOooooO
def ii1iI1I11I ( url ) :
 iIIiIi1iIII1 = OooOOOOo ( url )
 i1Iii1i1I = re . compile ( '<li class="yt-uix-scroller-scroll-unit "(.+?)</li>' , re . DOTALL ) . findall ( iIIiIi1iIII1 )
 for i1Iii1i1I in i1Iii1i1I :
  IiI111111IIII = re . compile ( 'data-video-title="(.+?)"' ) . findall ( str ( i1Iii1i1I ) )
  for IiI111111IIII in IiI111111IIII :
   IiI111111IIII = ( IiI111111IIII ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&amp;' , '&' )
  url = re . compile ( '<a href="/w(.+?)&' ) . findall ( str ( i1Iii1i1I ) )
  for url in url :
   url = 'https://www.youtube.com/w' + url
  II1iI = re . compile ( '<img.+?="(.+?)"' ) . findall ( str ( i1Iii1i1I ) )
  for II1iI in II1iI :
   II1iI = 'http:' + II1iI
  I1I1IiI1 ( '[COLORgreen]' + IiI111111IIII + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , II1iI , '' , '' )
  if 54 - 54: o00OO00OoO * OoOo00o / o00OO00OoO / Oo * I1IiI
  if 94 - 94: OoOo00o * ii11ii1ii . OOO0OOo . OOO0OOo / I1IiI - o00OO00OoO
  if 86 - 86: iIii1I11I1II1 / I1IiI . OoOoOO00
  if 19 - 19: ii11ii1ii % OoooooooOO % OoOo00o * OOooOOo % O0
def ooo ( url ) :
 if 27 - 27: OOO0OOo % OOOo0
 o0oooOO00 = [ ]
 iIIiIi1iIII1 = OooOOOOo ( url )
 oo0O0oO = re . compile ( '<div class="explore-list">.+?<div class="el-img"><a href="(.+?)" class=".+?"><img src="(.+?)" alt=".+?<h3>(.+?)</h3><p>(.+?)</p></div>' , re . DOTALL ) . findall ( iIIiIi1iIII1 )
 for IIo0o0O0O00oOOo , OO0ooOOO0OOO , IiI111111IIII , iiIiii1IIIII in oo0O0oO :
  IiI111111IIII = ( IiI111111IIII ) . replace ( '&#039;' , '\'' ) . replace ( '&amp;' , '&' ) . replace ( '&quot;' , '"' )
  o00o = OooOOOOo ( IIo0o0O0O00oOOo )
  IIIIiiIiiI = re . compile ( '<!-- # player # -->.+?<iframe title=".+?".+?src="http://www.youtube.com/embed/(.+?)?autohide.+?<!-- detail box -->(.+?)</div>' , re . DOTALL ) . findall ( o00o )
  for IIIIiI11I11 , oo00o0 in IIIIiiIiiI :
   i11II1I11I1 = re . compile ( '<p>(.+?)</p>' , re . DOTALL ) . findall ( str ( oo00o0 ) )
   for OOoOO0ooo in i11II1I11I1 :
    if IiI111111IIII in o0oooOO00 :
     pass
    else :
     I1I1IiI1 ( IiI111111IIII , IIIIiI11I11 , 8043 , OO0ooOOO0OOO , OO0ooOOO0OOO , OOoOO0ooo )
     O00Oo000ooO0 ( 'movies' , 'INFO' )
     o0oooOO00 . append ( IiI111111IIII )
     if 30 - 30: OOooOOo - i1IIi % OoOoOO00 + Oooo0Ooo000 * iIii1I11I1II1
     if 81 - 81: OoOo00o % i1IIi . iIii1I11I1II1
def Ii1Iii1iIi ( url ) :
 OO0oo = Iii1 ( url )
 oo0O0oO = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( OO0oo )
 for url , OOO0000oO , OOoOO0ooo , iI1i111I1Ii , IiI111111IIII in oo0O0oO :
  IIIIii ( IiI111111IIII , url , 10065 , OOO0000oO , iI1i111I1Ii , OOoOO0ooo )
 O00Oo000ooO0 ( 'movies' , 'INFO' )
 if 25 - 25: o00OO00OoO - i1I111ii1II1i
def Ii1Io0OO0o0o00o ( ) :
 IIiiIiII1Ii = i1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oo00oOO000oO0 = 'https://www.youtube.com/results?search_query=' + ( IIiiIiII1Ii ) . replace ( ' ' , '+' )
 iIIII11I1II = oo00oOO000oO0 . lower ( )
 iIIiIi1iIII1 = OooOOOOo ( iIIII11I1II )
 oo0O0oO = re . compile ( '<img src="(.+?)" alt=.+?yt-lockup-title "><a href="(.+?)".+?data-sessionlink=.+?" title="(.+?)".+?<span class="accessible-description".+?>(.+?)</span>.+?<div class="yt-lockup-description yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr">(.+?)</div>' , re . DOTALL ) . findall ( iIIiIi1iIII1 )
 next = re . compile ( '<a href="(.+?)" class="yt-uix-button.+?class="yt-uix-button-content">Next.+?</span></a>' ) . findall ( iIIiIi1iIII1 )
 for oOo0 in next :
  oOo0 = 'https://www.youtube.com' + oOo0
  IIIIii ( '[COLORgreen] NEXT [/COLOR]' , oOo0 , 10065 , i1iIIi1 + 'Next.png' , oooOOOOO , '' )
 for OO0ooOOO0OOO , oOo0 , IiI111111IIII , OOOoOO , oo00o0 in oo0O0oO :
  OO0o . append ( IiI111111IIII )
  O00Oo000ooO0 ( 'tvshows' , 'INFO' )
  II1iI = 'http:' + ( OO0ooOOO0OOO ) . replace ( 'https:' , '' )
  print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>' + II1iI
  oOo0 = 'http://www.youtube.com' + oOo0
  I1I1IiI1 ( '[COLORred]' + OOOoOO + '[/COLOR]' + '[COLORgreen]' + IiI111111IIII + '[/COLOR]' , ( oOo0 ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , II1iI , II1iI , oo00o0 )
 else :
  oo0O0oO = re . compile ( '<img src="(.+?)" alt=.+?yt-lockup-title "><a href="(.+?)".+?data-sessionlink=.+?" title="(.+?)".+?<span class="accessible-description".+?>(.+?)</span>' , re . DOTALL ) . findall ( iIIiIi1iIII1 )
  for OO0ooOOO0OOO , oOo0 , IiI111111IIII , OOOoOO in oo0O0oO :
   print 'im doing it'
   O00Oo000ooO0 ( 'tvshows' , 'INFO' )
   II1iI = 'http:' + ( OO0ooOOO0OOO ) . replace ( 'https:' , '' )
   oOo0 = 'http://www.youtube.com' + oOo0
   if '&' in oOo0 :
    print ' i got here'
    iIIiIi1iIII1 = OooOOOOo ( oOo0 )
    i1Iii1i1I = re . compile ( '<li class="yt-uix-scroller-scroll-unit "(.+?)</li>' , re . DOTALL ) . findall ( iIIiIi1iIII1 )
    for i1Iii1i1I in i1Iii1i1I :
     IiI111111IIII = re . compile ( 'data-video-title="(.+?)"' ) . findall ( str ( i1Iii1i1I ) )
     for IiI111111IIII in IiI111111IIII :
      IiI111111IIII = ( IiI111111IIII ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&amp;' , '&' )
     oOo0 = re . compile ( '<a href="/w(.+?)&' ) . findall ( str ( i1Iii1i1I ) )
     for oOo0 in oOo0 :
      oOo0 = 'https://www.youtube.com/w' + oOo0
     II1iI = re . compile ( '<img.+?="(.+?)"' ) . findall ( str ( i1Iii1i1I ) )
     for II1iI in II1iI :
      II1iI = 'http:' + II1iI
     I1I1IiI1 ( '[COLORred]' + OOOoOO + '[/COLOR]' + '[COLORgreen]' + IiI111111IIII + '[/COLOR]' , ( oOo0 ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , II1iI , oooOOOOO , '' )
   elif IiI111111IIII in OO0o :
    pass
   elif 'user' in oOo0 or 'elete' in IiI111111IIII :
    pass
   elif 'hannel' in oOo0 :
    print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' + oOo0
    iIIiIi1iIII1 = OooOOOOo ( oOo0 )
    I11IIIi = re . compile ( 'data-thumb="(.+?)".+?href="(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( iIIiIi1iIII1 )
    for OO0ooOOO0OOO , oOo0 , IiI111111IIII in I11IIIi :
     if 'outube' in oOo0 or 'list' in oOo0 :
      pass
     elif 'atch' in oOo0 :
      oOo0 = ( oOo0 ) . replace ( '/watch?v=' , '' )
      I1I1IiI1 ( '[COLORred]' + OOOoOO + '[/COLOR]' + '[COLORgreen]' + IiI111111IIII + '[/COLOR]' , ( oOo0 ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , 'http:' + OO0ooOOO0OOO , 'http:' + OO0ooOOO0OOO , '' )
     else :
      pass
   else :
    I1I1IiI1 ( '[COLORred]' + OOOoOO + '[/COLOR]' + '[COLORgreen]' + IiI111111IIII + '[/COLOR]' , ( oOo0 ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , II1iI , II1iI , '' )
    if 15 - 15: ii11ii1ii * Ooo00oOo00o
def i1II1i ( url ) :
 iIIiIi1iIII1 = OooOOOOo ( url )
 oo0O0oO = re . compile ( '<img src="(.+?)" alt=.+?yt-lockup-title "><a href="(.+?)".+?data-sessionlink=.+?" title="(.+?)".+?<span class="accessible-description".+?>(.+?)</span>.+?<div class="yt-lockup-description yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr">(.+?)</div>' , re . DOTALL ) . findall ( iIIiIi1iIII1 )
 next = re . compile ( '<a href="(.+?)" class="yt-uix-button.+?class="yt-uix-button-content">Next.+?</span></a>' ) . findall ( iIIiIi1iIII1 )
 for url in next :
  url = 'https://www.youtube.com' + url
  IIIIii ( '[COLORgreen] NEXT [/COLOR]' , url , 10065 , i1iIIi1 + 'Next.png' , oooOOOOO , '' )
 for OO0ooOOO0OOO , url , IiI111111IIII , OOOoOO , oo00o0 in oo0O0oO :
  OO0o . append ( IiI111111IIII )
  O00Oo000ooO0 ( 'tvshows' , 'INFO' )
  II1iI = 'http:' + ( OO0ooOOO0OOO ) . replace ( 'https:' , '' )
  print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>' + II1iI
  url = 'http://www.youtube.com' + url
  I1I1IiI1 ( '[COLORred]' + OOOoOO + '[/COLOR]' + '[COLORgreen]' + IiI111111IIII + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , II1iI , II1iI , oo00o0 )
 else :
  oo0O0oO = re . compile ( '<img src="(.+?)" alt=.+?yt-lockup-title "><a href="(.+?)".+?data-sessionlink=.+?" title="(.+?)".+?<span class="accessible-description".+?>(.+?)</span>' , re . DOTALL ) . findall ( iIIiIi1iIII1 )
  for OO0ooOOO0OOO , url , IiI111111IIII , OOOoOO in oo0O0oO :
   O00Oo000ooO0 ( 'tvshows' , 'INFO' )
   II1iI = 'http:' + ( OO0ooOOO0OOO ) . replace ( 'https:' , '' )
   url = 'http://www.youtube.com' + url
   if '&' in url :
    iIIiIi1iIII1 = OooOOOOo ( url )
    i1Iii1i1I = re . compile ( '<li class="yt-uix-scroller-scroll-unit "(.+?)</li>' , re . DOTALL ) . findall ( iIIiIi1iIII1 )
    for i1Iii1i1I in i1Iii1i1I :
     IiI111111IIII = re . compile ( 'data-video-title="(.+?)"' ) . findall ( str ( i1Iii1i1I ) )
     for IiI111111IIII in IiI111111IIII :
      IiI111111IIII = ( IiI111111IIII ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&amp;' , '&' )
     url = re . compile ( '<a href="/w(.+?)&' ) . findall ( str ( i1Iii1i1I ) )
     for url in url :
      url = 'https://www.youtube.com/w' + url
     II1iI = re . compile ( '<img.+?="(.+?)"' ) . findall ( str ( i1Iii1i1I ) )
     for II1iI in II1iI :
      II1iI = 'http:' + II1iI
     I1I1IiI1 ( '[COLORred]' + OOOoOO + '[/COLOR]' + '[COLORgreen]' + IiI111111IIII + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , II1iI , oooOOOOO , '' )
   elif IiI111111IIII in OO0o :
    pass
   elif 'user' in url or 'elete' in IiI111111IIII :
    pass
   elif 'hannel' in url :
    print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' + url
    iIIiIi1iIII1 = OooOOOOo ( url )
    I11IIIi = re . compile ( 'data-thumb="(.+?)".+?href="(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( iIIiIi1iIII1 )
    for OO0ooOOO0OOO , url , IiI111111IIII in I11IIIi :
     if 'outube' in url or 'list' in url :
      pass
     elif 'atch' in url :
      url = ( url ) . replace ( '/watch?v=' , '' )
      I1I1IiI1 ( '[COLORred]' + OOOoOO + '[/COLOR]' + '[COLORgreen]' + IiI111111IIII + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , 'http:' + OO0ooOOO0OOO , 'http:' + OO0ooOOO0OOO , '' )
     else :
      pass
   else :
    I1I1IiI1 ( '[COLORred]' + OOOoOO + '[/COLOR]' + '[COLORgreen]' + IiI111111IIII + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , II1iI , II1iI , '' )
    if 83 - 83: I1IiI - iI / Oooo0Ooo000 / o00OO00OoO + O0ooOooooO - O0
    if 4 - 4: i1I111II1I * Ooo00oOo00o % i1IIi * i11iIiiIii % Oo - O0ooOooooO
def OOoOoOo ( ) :
 if oO0o0o0ooO0oO == 'insert_password' :
  i1 . ok ( '[COLORgreen]Donators Login[/COLOR]' , 'You need to set username and password to access this' , 'These are unique and provided to donators to help with server and stream costs' , 'Donate @ [COLORgreen]http://architects.x10host.com[/COLOR]' )
  iiIIIII1i1iI . openSettings ( sys . argv [ 0 ] )
 else :
  o000ooooO0o = open ( iIi1ii1I1 )
  oo0O0oO = re . compile ( 'plugin.video.GenieTv.+?2Flive%2F(.+?)%2F(.+?)%2F' ) . findall ( str ( o000ooooO0o ) )
  for iI1i11 , OoOOoooOO0O in oo0O0oO :
   if iI1i11 == 'needs replacing' or OoOOoooOO0O == 'needs replacing' :
    ooo00Ooo ( )
  IIIIii ( '[COLORgreen]DONATORS LIST[/COLOR]' , iiI1IiI + '/thelist.m3u' , 7080 , i1iIIi1 + 'GTVIPTV.png' , oooOOOOO , '' )
  if 93 - 93: i11iIiiIii - OOOo0 * ii11ii1ii * Oooo0Ooo000 % O0 + OoooooooOO
def I1i1i1 ( ) :
 oO . ok ( '[COLOR=white]ReCreate Addons.ini[/COLOR]' , 'If it doesnt work ensure login details are correct and retry' , '' , 'This will allow access to streams in guide without linking to favourites' )
 ooo00Ooo ( )
 oO . ok ( '[COLOR=yellow]Done[/COLOR]' , 'Done' , 'Easy as that' , 'Now Go to guide and it should link your GTV streams' )
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
 IIIIii ( 'Full Backup' , '' , 10061 , i1iIIi1 + 'Backup.png' , oooOOOOO , 'Back Up Your Full System' )
 if os . path . exists ( I1IIIii ) :
  IIIIii ( 'Backup Genie Favourites' , oOo0 , 10062 , i1iIIi1 + 'Backup.png' , oooOOOOO , 'Back Up Your favourites' )
 if os . path . exists ( ooooooO0oo ) :
  IIIIii ( 'Backup Ivue Config' , ooooooO0oo , 10062 , i1iIIi1 + 'Backup.png' , oooOOOOO , 'Back Up Your master.db' )
 if os . path . exists ( IIiiiiiiIi1I1 ) :
  IIIIii ( 'Backup Kodi Favourites' , IIiiiiiiIi1I1 , 10062 , i1iIIi1 + 'Backup.png' , oooOOOOO , 'Back Up Your favourites.xml' )
  if 43 - 43: OoOoOO00 . O0ooOooooO / ii11ii1ii
  if 20 - 20: OOOo0
  if 95 - 95: i1I111ii1II1i - OOOo0
zip = iiIIIII1i1iI . getSetting ( 'zip' )
I1ii1ii11i1I = xbmc . translatePath ( os . path . join ( zip ) )
def o0OoOO ( ) :
 O0O0Oo00 = xbmc . translatePath ( os . path . join ( zip , 'testCBFolder' ) )
 if not os . path . exists ( zip ) :
  oO . ok ( '[COLOR=white]Origin[/COLOR]' , 'The download location you have stored does not exist .\nPlease update the addon settings and try again.' , '' , '' )
  iiIIIII1i1iI . openSettings ( sys . argv [ 0 ] )
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
   oo0O0oO = re . compile ( I1i1iiiI1 ) . findall ( iII1ii1 )
   for type , iIIi , oO0o00oo0 in oo0O0oO :
    oO0o00oo0 = oO0o00oo0 . replace ( '&quot;' , '' ) . replace ( '&amp;' , '&' )
    xbmc . executebuiltin ( "Skin.Se	t%s(%s,%s)" % ( type . title ( ) , iIIi , oO0o00oo0 ) )
  else :
   OOOO0OOO = os . path . join ( url )
   O00Ooo = open ( os . path . join ( I1ii1ii11i1I , description . split ( 'Your ' ) [ 1 ] ) ) . read ( )
   i1i1ii = open ( OOOO0OOO , mode = 'w' )
   i1i1ii . write ( O00Ooo )
   i1i1ii . close ( )
 oO . ok ( "[COLOR=white]Origin[/COLOR]" , "" , 'All Done !' , '' )
 if 19 - 19: OoOoOO00 + OoOo00o
 if 53 - 53: O0ooOooooO - OOOo0 - O0ooOooooO * i1I111ii1II1i
 if 71 - 71: O0 - iIii1I11I1II1
 if 12 - 12: i1I111II1I / OOooOOo
def iiI1I1 ( ) :
 ooO = 1
 o0OoOO ( )
 iiOO0O0Ooo = xbmc . translatePath ( os . path . join ( I1ii1ii11i1I , 'Build Backup' , 'Full Backup' , '' ) )
 oOoO0 = xbmc . translatePath ( os . path . join ( I1ii1ii11i1I , 'Build Backup' , 'my_full_backup.zip' ) )
 Oo0 = xbmc . translatePath ( os . path . join ( I1ii1ii11i1I , 'Build Backup' , 'my_full_backup_GUI_Settings.zip' ) )
 if not os . path . exists ( iiOO0O0Ooo ) :
  os . makedirs ( iiOO0O0Ooo )
 oo0O0o00o0O = i1 . input ( 'Enter a name for this backup' , type = xbmcgui . INPUT_ALPHANUM )
 if ( not oo0O0o00o0O ) : return False , 0
 I11i1II = oo0O0o00o0O
 OooiiIi1i = xbmc . translatePath ( os . path . join ( iiOO0O0Ooo , I11i1II + '.zip' ) )
 I1i11111i1i11 = [ 'plugin.video.GenieTv' ]
 OOoOOO0 = [ "xbmc.log" , "xbmc.old.log" , "kodi.log" , "kodi.old.log" , '.DS_Store' , '.setup_complete' , 'XBMCHelper.conf' ]
 I1I1i = [ 'plugin.video.GenieTv' , 'repository.origin' , 'cache' , 'system' , 'Thumbnails' , "peripheral_data" , 'library' , 'keymaps' ]
 I1IIIiIiIi = [ "xbmc.log" , "xbmc.old.log" , "kodi.log" , "kodi.old.log" , "Textures13.db" , '.DS_Store' , '.setup_complete' , 'XBMCHelper.conf' , 'advancedsettings.xml' ]
 IIIII1 = "Creating full backup of existing build"
 iIi1Ii1i1iI = "Creating Community Build"
 IIiI1 = "Archiving..."
 i1iI1 = ""
 ii1 = "Please Wait"
 I1IiiI1ii1i ( i1iiIIiiI111 , OooiiIi1i , iIi1Ii1i1iI , IIiI1 , i1iI1 , ii1 , I1I1i , I1IIIiIiIi )
 time . sleep ( 1 )
 O0o = xbmc . translatePath ( os . path . join ( iiOO0O0Ooo , I11i1II + '_guisettings.zip' ) )
 oO0OoO00o = zipfile . ZipFile ( O0o , mode = 'w' )
 try :
  oO0OoO00o . write ( xbmc . translatePath ( os . path . join ( i1iiIIiiI111 , 'userdata' , 'profiles.xml' ) ) , 'profiles.xml' , zipfile . ZIP_DEFLATED )
 except : pass
 oO0OoO00o . close ( )
 if ooO == 0 :
  oO . ok ( "FAILED!" , 'The guisettings.xml file could not be found on your' , 'system, please reboot and try again.' , '' )
 else :
  oO . ok ( "SUCCESS!" , 'You Are Now Backed Up. If you\'d like to share this build with' , 'the community please post details on the forum at' , '[COLOR=blue][B]http://rh-project.info[/COLOR][/B]' )
  oO . ok ( "Build Locations" , 'Full Backup (only used to restore on this device): [COLOR=yellow]' + oOoO0 , '[/COLOR]Universal Backup (can be used on any device): [COLOR=yellow]' + OooiiIi1i + '[/COLOR]' )
  if 11 - 11: Oo - OOOo0 * OoOoOO00 . ii11ii1ii . O0ooOooooO
def I1IiiI1ii1i ( sourcefile , destfile , message_header , message1 , message2 , message3 , exclude_dirs , exclude_files ) :
 O0OoOO0oo0 = zipfile . ZipFile ( destfile , 'w' , zipfile . ZIP_DEFLATED )
 oOO = len ( sourcefile )
 O0o0OO0000ooo = [ ]
 iIIII1iIIii = [ ]
 o00 . create ( message_header , message1 , message2 , message3 )
 for oOOO00o000o , iIi11i1 , oO00oo0o00o0o in os . walk ( sourcefile ) :
  for file in oO00oo0o00o0o :
   iIIII1iIIii . append ( file )
 IiIIIIIi = len ( iIIII1iIIii )
 for oOOO00o000o , iIi11i1 , oO00oo0o00o0o in os . walk ( sourcefile ) :
  iIi11i1 [ : ] = [ IiIi1iIIi1 for IiIi1iIIi1 in iIi11i1 if IiIi1iIIi1 not in exclude_dirs ]
  oO00oo0o00o0o [ : ] = [ i1i1ii for i1i1ii in oO00oo0o00o0o if i1i1ii not in exclude_files ]
  for file in oO00oo0o00o0o :
   O0o0OO0000ooo . append ( file )
   O0OoO0ooOO0o = len ( O0o0OO0000ooo ) / float ( IiIIIIIi ) * 100
   o00 . update ( int ( O0OoO0ooOO0o ) , "Backing Up" , '[COLOR yellow]%s[/COLOR]' % file , 'Please Wait' )
   OoOo0oOooOoOO = os . path . join ( oOOO00o000o , file )
   if not 'temp' in iIi11i1 :
    if not 'plugin.program.originwizard' in iIi11i1 :
     import time
     oo00ooOoO00 = '01/01/1980'
     o00oOoOo0 = time . strftime ( '%d/%m/%Y' , time . gmtime ( os . path . getmtime ( OoOo0oOooOoOO ) ) )
     if o00oOoOo0 > oo00ooOoO00 :
      O0OoOO0oo0 . write ( OoOo0oOooOoOO , OoOo0oOooOoOO [ oOO : ] )
 O0OoOO0oo0 . close ( )
 o00 . close ( )
 if 72 - 72: o00OO00OoO
 if 90 - 90: Oo % O0 * iIii1I11I1II1 . i1I111ii1II1i
def I1iii11 ( ) :
 IIIIii ( '[COLORgreen]SCOOBY STREAMS[/COLOR]' , ( oOOoo00O0O ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvdHZjYXRzLnBocA==' ) ) , 1016 , i1iIIi1 + 'scoob.png' , oooOOOOO , '' )
 IIIIii ( '[COLORgreen]SCOOBY SCRAPES[/COLOR]' , iiI1IiI , 1024 , i1iIIi1 + 'scoob.png' , oooOOOOO , '' )
 if 74 - 74: O0 / i1IIi
 if 78 - 78: OoooooooOO . Ooo00oOo00o + OOO0OOo - i1IIi
def ii1O0 ( ) :
 IIIIii ( '[COLORgreen]SEARCH MOVIES[/COLOR]' , iiI1IiI , 9001 , i1iIIi1 + 'MOVIESv.png' , oooOOOOO , '' )
 IIIIii ( '[COLORgreen]SEARCH SERIES[/COLOR]' , iiI1IiI , 9002 , i1iIIi1 + 'TVSHOWSv.png' , oooOOOOO , '' )
 IIIIii ( '[COLORgreen]SEARCH CARTOONS[/COLOR]' , '' , 10005 , i1iIIi1 + 'ORIGINCARTOON' , oooOOOOO , '' )
 if 33 - 33: i1IIi
 if 36 - 36: OoOoOO00 % i11iIiiIii * I1IiI + Oooo0Ooo000
 if 25 - 25: iIii1I11I1II1 % i1I111ii1II1i . OOO0OOo
 if 14 - 14: O0ooOooooO + ii11ii1ii - i1I111ii1II1i / O0 . o00OO00OoO
def i1iiIiI1Ii1i ( ) :
 IIIIii ( '[COLORgreen]RADIO[/COLOR]' , iiI1IiI , 1013 , i1iIIi1 + 'radio.png' , oooOOOOO , '' )
 if iiIIIII1i1iI . getSetting ( 'CONCERTS' ) == 'true' :
  IIIIii ( '[COLORgreen]CONCERTS[/COLOR]' , ( oOOoo00O0O ( 'aHR0cHM6Ly93d3cucmVkZGl0LmNvbS9yL2Z1bGxjb25jZXJ0cy8=' ) ) , 7050 , i1iIIi1 + 'concerts.png' , oooOOOOO , '' )
 IIIIii ( '[COLORgreen]MUSIC[/COLOR]' , iiI1IiI , 1030 , i1iIIi1 + 'MUSIC.png' , oooOOOOO , '' )
 IIIIii ( '[COLORgreen]MUSIC ARCHIVE[/COLOR]' , iiI1IiI + ( oOOoo00O0O ( 'L3ZvZC91cmxzL211c2ljLnBocA==' ) ) , 1010 , i1iIIi1 + 'MUSIC.png' , oooOOOOO , '' )
 IIIIii ( '[COLORgreen]MUSIC SEARCH[/COLOR]' , iiI1IiI , 1111 , i1iIIi1 + 'search.png' , oooOOOOO , '' )
 IIIIii ( '[COLORgreen]KODIBLE AUDIO BOOKS[/COLOR]' , 'http://doremisa.com/audiobooks/' , 30000 , i1iIIi1 + 'kodible.png' , oooOOOOO , '' )
 if 22 - 22: OoOo00o / i11iIiiIii
 O00Oo000ooO0 ( 'movies' , 'MAIN' )
 if 62 - 62: Ooo00oOo00o / ii11ii1ii
def ii1O000OOO0OOo ( ) :
 if 32 - 32: iI * O0
 I1I1IiI1 ( 'DELETE CACHE' , 'url' , 14 , i1iIIi1 + 'MAIN5.png' , oooOOOOO , '' )
 I1I1IiI1 ( 'DELETE PACKAGES' , 'url' , 6 , i1iIIi1 + 'MAIN4.png' , oooOOOOO , '' )
 I1I1IiI1 ( 'FORCE REFRESH' , 'url' , 10 , i1iIIi1 + 'MAIN3.png' , oooOOOOO , 'Force Refresh All Repos' )
 if 100 - 100: OOO0OOo % iIii1I11I1II1 * OoOoOO00 - i1I111ii1II1i
 I1I1IiI1 ( 'CHECK MY IP' , 'url' , 12 , i1iIIi1 + 'MAIN2.png' , oooOOOOO , '' )
 I1I1IiI1 ( 'ANDROID ONLY DELETE TEXTURE13.DB&THUBMNAIL FOLDER' , 'url' , 13 , i1iIIi1 + 'MAIN1.png' , oooOOOOO , 'Only Works On Android On Windows It Deletes Your Thumnails Folder But Does Not Delete The Textures13.db' )
 IIIIii ( '[COLORgreen]ADVANCED SETTINGS XML[/COLOR]' , iiI1IiI , 4 , i1iIIi1 + 'XML.png' , oooOOOOO , '' )
 IIIIii ( '[COLORgreen]URL FIXES[/COLOR]' , iiI1IiI , 20 , i1iIIi1 + 'URLFIX.png' , oooOOOOO , '' )
 O00Oo000ooO0 ( 'movies' , 'MAIN' )
 if 92 - 92: OOO0OOo
 if 22 - 22: Oo % i1I111ii1II1i * ii11ii1ii / i1I111II1I % i11iIiiIii * Oooo0Ooo000
def I1iII1iiII ( ) :
 IIIIii ( '[COLORgreen]REPOS[/COLOR]' , ( oOOoo00O0O ( 'aHR0cDovL21pcnJvcnMua29kaS50di9hZGRvbnMv' ) ) , 2030 , i1iIIi1 + 'repos.png' , oooOOOOO , '' )
 IIIIii ( '[COLORgreen]NEW[/COLOR]' , iiI1IiI , 22 , i1iIIi1 + 'NEW.png' , oooOOOOO , '' )
 IIIIii ( '[COLORgreen]IPTV[/COLOR]' , iiI1IiI , 23 , i1iIIi1 + 'IPTV.png' , oooOOOOO , '' )
 IIIIii ( '[COLORgreen]VIDEO[/COLOR]' , iiI1IiI , 24 , i1iIIi1 + 'VIDEO.png' , oooOOOOO , '' )
 IIIIii ( '[COLORgreen]SPORTS[/COLOR]' , iiI1IiI , 25 , i1iIIi1 + 'SPORTS.png' , oooOOOOO , '' )
 IIIIii ( '[COLORgreen]KIDS[/COLOR]' , iiI1IiI , 26 , i1iIIi1 + 'KIDS.png' , oooOOOOO , '' )
 IIIIii ( '[COLORgreen]MUSIC[/COLOR]' , iiI1IiI , 27 , i1iIIi1 + 'MUSIC.png' , oooOOOOO , '' )
 IIIIii ( '[COLORgreen]PROGRAMS[/COLOR]' , iiI1IiI , 28 , i1iIIi1 + 'PROGRAMS.png' , oooOOOOO , '' )
 IIIIii ( '[COLORgreen]XXX[/COLOR]' , 'URL' , 29 , i1iIIi1 + 'XXX.png' , oooOOOOO , '' )
 O00Oo000ooO0 ( 'movies' , 'MAIN' )
 if 95 - 95: OoooooooOO - OoOo00o * OOOo0 + I1IiI
 if 10 - 10: OOooOOo / i11iIiiIii
def o00oO ( ) :
 I1I1IiI1 ( 'CHECK ADVANCED XML' , iiI1IiI , 8 , i1iIIi1 + 'XML.png' , oooOOOOO , '' )
 I1I1IiI1 ( 'MUCKYS XML' , iiI1IiI + '/wizard/muckys.xml' , 7 , i1iIIi1 + 'XML.png' , oooOOOOO , '' )
 I1I1IiI1 ( '0CACHE XML' , iiI1IiI + '/wizard/0cache.xml' , 7 , i1iIIi1 + 'XML.png' , oooOOOOO , '' )
 I1I1IiI1 ( 'MIKEY1234 XML' , iiI1IiI + '/wizard/mikey.xml' , 7 , i1iIIi1 + 'XML.png' , oooOOOOO , '' )
 I1I1IiI1 ( 'TUXENS XML' , iiI1IiI + '/wizard/tuxens.xml' , 7 , i1iIIi1 + 'XML.png' , oooOOOOO , '' )
 I1I1IiI1 ( 'P2P RECOMMENDED XML1' , iiI1IiI + '/wizard/p2p1.xml' , 7 , i1iIIi1 + 'XML.png' , oooOOOOO , '' )
 I1I1IiI1 ( 'P2P RECOMMENDED XML2' , iiI1IiI + '/wizard/p2p2.xml' , 7 , i1iIIi1 + 'XML.png' , oooOOOOO , '' )
 I1I1IiI1 ( 'DELETE XML' , iiI1IiI , 11 , i1iIIi1 + 'XML.png' , oooOOOOO , '' )
 O00Oo000ooO0 ( 'movies' , 'MAIN' )
 if 92 - 92: OoOo00o * Oo * Oo * OOOo0 . iIii1I11I1II1
def I1Ii1111iIi ( ) :
 I1I1IiI1 ( '[COLORgreen]My Local Zip[/COLOR]' , i11 , 48 , i1iIIi1 + 'MB.png' , oooOOOOO , '' )
 I1I1IiI1 ( '[COLORgreen]My Online Zip[/COLOR]' , i1111 , 43 , i1iIIi1 + 'MB.png' , oooOOOOO , '' )
 if 31 - 31: Oooo0Ooo000 . o00OO00OoO * OOO0OOo + i11iIiiIii * O0ooOooooO
def OO0ooo0o0O0Oooooo ( ) :
 I1I1IiI1 ( 'INSTALL FTV GUIDE AND OTHER ADDONS REQUIRED' , iiI1IiI + '/wizard/customftv/ftvguide-addons.zip' , 5 , i1iIIi1 + 'FTV4.png' , oooOOOOO , '' )
 I1I1IiI1 ( 'FTV GUIDE FIRST RUN SETTINGS' , iiI1IiI + '/wizard/customftv/settings.xml' , 17 , i1iIIi1 + 'FTV3.png' , oooOOOOO , '' )
 I1I1IiI1 ( 'FTV GUIDE ADDONS2.INI UPDATE DAILY' , 'http://ren.byethost12.com/addons2.ini' , 16 , i1iIIi1 + 'FTV1.png' , oooOOOOO , '' )
 I1I1IiI1 ( 'RESET FTV DATABASE' , 'url' , 18 , i1iIIi1 + 'FTV2.png' , oooOOOOO , '' )
 if 1 - 1: OOO0OOo % I1IiI * Oo
 if 55 - 55: I1IiI
 if 87 - 87: OoooooooOO % i1I111ii1II1i . OOOo0 / OOO0OOo
def i1I1iI ( ) :
 IIIIii ( '[COLORgreen]SKINS[/COLOR]' , iiI1IiI , 33 , i1iIIi1 + 'skinp.png' , oooOOOOO , '' )
 IIIIii ( '[COLORgreen]ARTWORK PACKS[/COLOR]' , iiI1IiI , 34 , i1iIIi1 + 'artp.png' , oooOOOOO , '' )
 IIIIii ( '[COLORgreen]CREATE UNIVERSAL PATHS[/COLOR]' , i1iiIIiiI111 , 35 , i1iIIi1 + 'GUI.png' , oooOOOOO , '' )
 O00Oo000ooO0 ( 'movies' , 'MAIN' )
 if 62 - 62: o00OO00OoO . OoOo00o . OoooooooOO
def i111 ( url ) :
 iiI1 = OooOOOOo ( iiIIiii ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 oo0O0oO = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( iiI1 )
 for IiI111111IIII , url , OOO0000oO , iI1i111I1Ii , oo00o0 in oo0O0oO :
  IIIIii ( IiI111111IIII , url , 5 , OOO0000oO , iI1i111I1Ii , oo00o0 )
 O00Oo000ooO0 ( 'movies' , 'MAIN' )
 if 30 - 30: i1I111ii1II1i
def iIiIi1I ( ) :
 IIIIii ( '[COLORgreen]GOTHAM SKINS[/COLOR]' , iiI1IiI , 36 , i1iIIi1 + 'GSKIN.png' , oooOOOOO , '' )
 IIIIii ( '[COLORgreen]HELIX SKINS[/COLOR]' , iiI1IiI , 37 , i1iIIi1 + 'HSKIN.png' , oooOOOOO , '' )
 IIIIii ( '[COLORgreen]ISENGAARD SKINS[/COLOR]' , i1iiIIiiI111 , 38 , i1iIIi1 + 'ISKIN.png' , oooOOOOO , '' )
 O00Oo000ooO0 ( 'movies' , 'MAIN' )
 if 45 - 45: i1IIi + OoOoOO00
def IiII1II11I ( url ) :
 iiI1 = OooOOOOo ( iiI1IiI + O0Oo00O ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 oo0O0oO = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( iiI1 )
 for IiI111111IIII , url , OOO0000oO , iI1i111I1Ii , oo00o0 in oo0O0oO :
  IIIIii ( IiI111111IIII , url , 42 , OOO0000oO , iI1i111I1Ii , oo00o0 )
 O00Oo000ooO0 ( 'movies' , 'MAIN' )
 if 91 - 91: O0ooOooooO % iI . OOO0OOo / i1I111ii1II1i * iIii1I11I1II1
def I1I1i11 ( url ) :
 iiI1 = OooOOOOo ( iiI1IiI + iiiI11 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 oo0O0oO = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( iiI1 )
 for IiI111111IIII , url , OOO0000oO , iI1i111I1Ii , oo00o0 in oo0O0oO :
  IIIIii ( IiI111111IIII , url , 42 , OOO0000oO , iI1i111I1Ii , oo00o0 )
 O00Oo000ooO0 ( 'movies' , 'MAIN' )
 if 63 - 63: Ooo00oOo00o + ii11ii1ii . o00OO00OoO % o00OO00OoO
def oOOOO ( url ) :
 iiI1 = OooOOOOo ( iiI1IiI + IiIi1ii111i1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 oo0O0oO = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( iiI1 )
 for IiI111111IIII , url , OOO0000oO , iI1i111I1Ii , oo00o0 in oo0O0oO :
  IIIIii ( IiI111111IIII , url , 42 , OOO0000oO , iI1i111I1Ii , oo00o0 )
 O00Oo000ooO0 ( 'movies' , 'MAIN' )
 if 31 - 31: i1I111II1I + O0
def oO0oOOoo00000 ( url ) :
 iiI1 = OooOOOOo ( oOOoo00O0O ( 'aHR0cHM6Ly9kbC5kcm9wYm94dXNlcmNvbnRlbnQuY29tL3MvN2ZrMjhndDlwb3QxMjJhL0JVSUxEUy50eHQ/ZGw9MA==' ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 oo0O0oO = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( iiI1 )
 for IiI111111IIII , url , OOO0000oO , iI1i111I1Ii , oo00o0 in oo0O0oO :
  IIIIii ( IiI111111IIII , url , 42 , OOO0000oO , iI1i111I1Ii , oo00o0 )
 O00Oo000ooO0 ( 'movies' , 'MAIN' )
 if 52 - 52: OOOo0
def o0oo00oO00o0 ( url ) :
 iiI1 = OooOOOOo ( iiI1IiI + OoO ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 oo0O0oO = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( iiI1 )
 for IiI111111IIII , url , OOO0000oO , iI1i111I1Ii , oo00o0 in oo0O0oO :
  IIIIii ( IiI111111IIII , url , 40 , OOO0000oO , iI1i111I1Ii , oo00o0 )
 O00Oo000ooO0 ( 'movies' , 'MAIN' )
 if 60 - 60: ii11ii1ii * OOOo0
def I1iIiI11I1 ( url ) :
 iiI1 = OooOOOOo ( iiI1IiI + i1oOOoo0o0OOOO ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 oo0O0oO = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( iiI1 )
 for IiI111111IIII , url , OOO0000oO , iI1i111I1Ii , oo00o0 in oo0O0oO :
  IIIIii ( IiI111111IIII , url , 5 , OOO0000oO , iI1i111I1Ii , oo00o0 )
 O00Oo000ooO0 ( 'movies' , 'MAIN' )
 if 26 - 26: i1I111ii1II1i % iIii1I11I1II1 + OOooOOo
def OOOooo ( ) :
 OO0oo = Iii1 ( oOOoo00O0O ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vYXBrdG9vbC9hcGsucGhw' ) )
 oo0O0oO = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( OO0oo )
 for oOo0 , II1iI , IiI111111IIII in oo0O0oO :
  Oo00oo0000OO ( IiI111111IIII , oOo0 , 2031 , II1iI )
  if 69 - 69: OOO0OOo - Ooo00oOo00o / i11iIiiIii + ii11ii1ii % OoooooooOO
def o000O000 ( name , url , description ) :
 O0O0Oo00 = xbmc . translatePath ( os . path . join ( ii1oOoO0o0ooo , 'Download' ) )
 o00 = xbmcgui . DialogProgress ( )
 o00 . create ( "Your App Is Downloading" , "Why not check out our website" , '' , 'Http://architects.x10host.com' )
 oO0o0O0Ooo0o = os . path . join ( O0O0Oo00 , name + '.apk' )
 try :
  os . remove ( oO0o0O0Ooo0o )
 except :
  pass
 downloader . download ( url , oO0o0O0Ooo0o , o00 )
 oO = xbmcgui . Dialog ( )
 oO . ok ( "GenieTv" , "[COLORred]Please press ok, exit kodi and go to your downloads folder to install your app[/COLOR]" , "[COLORblue]Tool Brought To You By Architects@Work[/COLOR]" )
 if 21 - 21: o00OO00OoO - OOOo0 + Oooo0Ooo000
def ooOoo0o0O ( url ) :
 O0O0Oo00 = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/resources/downloads' ) )
 o00 = xbmcgui . DialogProgress ( )
 o00 . create ( "Your fILM Is Downloading" , "Why not check out our website" , '' , 'Http://architects.x10host.com' )
 oO0o0O0Ooo0o = os . path . join ( O0O0Oo00 , IiI111111IIII + '.mp4' )
 try :
  os . remove ( oO0o0O0Ooo0o )
 except :
  pass
 downloader . download ( url , oO0o0O0Ooo0o , o00 )
 oO = xbmcgui . Dialog ( )
 oO . ok ( "GenieTv" , "[COLORred]Please press ok, Your download With Be Avaiilable Via The My Downloads Button[/COLOR]" , "[COLORblue]Tool Brought To You By Architects@Work[/COLOR]" )
 if 77 - 77: O0ooOooooO
 if 64 - 64: Oo * OoooooooOO . Oo
def ii1Ii1IiIIi ( name , url , description ) :
 O0O0Oo00 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 o00 = xbmcgui . DialogProgress ( )
 o00 . create ( "Your Art Pack Is Downloading" , "Why not check out our website" , '' , 'Http://architects.x10host.com' )
 oO0o0O0Ooo0o = os . path . join ( O0O0Oo00 , name )
 try :
  os . remove ( oO0o0O0Ooo0o )
 except :
  pass
 downloader . download ( url , oO0o0O0Ooo0o , o00 )
 o0OO0 = xbmc . translatePath ( os . path . join ( o0oO0 ) )
 time . sleep ( 2 )
 o00 . update ( 0 , "" , "Placing Your Art Please Wait" )
 print '======================================='
 print o0OO0
 print '======================================='
 extract . all ( oO0o0O0Ooo0o , o0OO0 , o00 )
 oO = xbmcgui . Dialog ( )
 oO . ok ( "GenieTv" , "[COLORred]Once complete your artwork will be stored in your Media folder, Accessible via the Homefolder, Enjoy[/COLOR]" )
 if 100 - 100: Oo * o00OO00OoO / o00OO00OoO
 if 41 - 41: iIii1I11I1II1 % Oooo0Ooo000
def oOo0oO ( url ) :
 iiI1 = OooOOOOo ( oOOoo00O0O ( 'aHR0cDovL2dlbmlldHYuYXJjaGl0ZWN0cy54MTBob3N0LmNvbS90ZXN0L3doLnR4dA==' ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 oo0O0oO = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( iiI1 )
 for IiI111111IIII , url , OOO0000oO , iI1i111I1Ii , oo00o0 in oo0O0oO :
  IIIIii ( IiI111111IIII , url , 5 , OOO0000oO , iI1i111I1Ii , oo00o0 )
 try :
  iiI1 = OooOOOOo ( IIi1IIIIi + oOo0oooo00o + OOOoO ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
  oo0O0oO = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( iiI1 )
  for IiI111111IIII , url , OOO0000oO , iI1i111I1Ii , oo00o0 in oo0O0oO :
   IIIIii ( IiI111111IIII , url , 5 , OOO0000oO , iI1i111I1Ii , oo00o0 )
 except : pass
 O00Oo000ooO0 ( 'movies' , 'INFO' )
 if 14 - 14: Oooo0Ooo000 . iIii1I11I1II1 . OoooooooOO . OoOoOO00 / OOooOOo
 if 21 - 21: i11iIiiIii / i1IIi + OOOo0 * i1I111II1I . o00OO00OoO
def OoOoo0oO ( url ) :
 iiI1 = OooOOOOo ( oOOoo00O0O ( 'aHR0cDovL2dlbmlldHYuYXJjaGl0ZWN0cy54MTBob3N0LmNvbS90ZXN0L3doLnR4dA==' ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 oo0O0oO = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( iiI1 )
 for IiI111111IIII , url , OOO0000oO , iI1i111I1Ii , oo00o0 in oo0O0oO :
  IIIIii ( IiI111111IIII , url , 43 , OOO0000oO , iI1i111I1Ii , oo00o0 )
 try :
  iiI1 = OooOOOOo ( IIi1IIIIi + oOo0oooo00o + OOOoO ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
  oo0O0oO = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( iiI1 )
  for IiI111111IIII , url , OOO0000oO , iI1i111I1Ii , oo00o0 in oo0O0oO :
   IIIIii ( IiI111111IIII , url , 43 , OOO0000oO , iI1i111I1Ii , oo00o0 )
 except : pass
 O00Oo000ooO0 ( 'movies' , 'INFO' )
 if 10 - 10: OoOoOO00 . i1I111ii1II1i
 if 32 - 32: iI . OoOo00o . OoooooooOO - Ooo00oOo00o + O0ooOooooO
def ooO0oO00O0o ( name , url , description ) :
 O0O0Oo00 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 o00 = xbmcgui . DialogProgress ( )
 o00 . create ( "GenieTv" , "Downloading Content" , '' , 'Please Wait' )
 oO0o0O0Ooo0o = os . path . join ( O0O0Oo00 , name + '.zip' )
 try :
  os . remove ( oO0o0O0Ooo0o )
 except :
  pass
 downloader . download ( url , oO0o0O0Ooo0o , o00 )
 ooOO00oOOo000 = xbmc . translatePath ( os . path . join ( 'special://home' , 'addons' ) )
 time . sleep ( 2 )
 o00 . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print ooOO00oOOo000
 print '======================================='
 extract . all ( oO0o0O0Ooo0o , ooOO00oOOo000 , o00 )
 oO = xbmcgui . Dialog ( )
 oO . ok ( "GenieTv" , "Press ok to finish install" , "[COLOR yellow]Brought To You By Architects@Work[/COLOR]" )
 OOooOoooOoOo ( )
 if 14 - 14: Ooo00oOo00o . OoOoOO00 . Oooo0Ooo000 / iI % ii11ii1ii - OOO0OOo
 if 67 - 67: Oooo0Ooo000 - i1I111II1I . i1IIi
def I1I1iI ( name , url , description ) :
 O0O0Oo00 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 o00 = xbmcgui . DialogProgress ( )
 o00 . create ( "GenieTv" , "Downloading " , '' , 'Please Wait' )
 oO0o0O0Ooo0o = os . path . join ( O0O0Oo00 , 'plugin.program.GenieTv.install' + '.zip' )
 try :
  os . remove ( oO0o0O0Ooo0o )
 except :
  pass
 downloader . download ( url , oO0o0O0Ooo0o , o00 )
 ooOO00oOOo000 = xbmc . translatePath ( os . path . join ( 'special://' , 'home' ) )
 time . sleep ( 2 )
 o00 . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print ooOO00oOOo000
 print '======================================='
 extract . all ( oO0o0O0Ooo0o , ooOO00oOOo000 , o00 )
 oO = xbmcgui . Dialog ( )
 oO . ok ( "GenieTv" , "Press ok to force close kodi, if unsuccessful using windows Please kill kodi via taskmanager" , "[COLOR yellow]Brought To You By Architects@Work[/COLOR]" )
 I1iIi1iiIIiI ( )
 if 81 - 81: Ooo00oOo00o * I1IiI . i1I111II1I
def iiiIIiIi ( name , url , description ) :
 O0O0Oo00 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 o00 = xbmcgui . DialogProgress ( )
 o00 . create ( "GenieTv" , "Downloading " , '' , 'Please Wait' )
 oO0o0O0Ooo0o = os . path . join ( O0O0Oo00 , 'plugin.program.GenieTv.install' + '.zip' )
 try :
  os . remove ( oO0o0O0Ooo0o )
 except :
  pass
 downloader . download ( url , oO0o0O0Ooo0o , o00 )
 ooOO00oOOo000 = xbmc . translatePath ( os . path . join ( 'special://' , 'home' ) )
 time . sleep ( 2 )
 o00 . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print ooOO00oOOo000
 print '======================================='
 extract . all ( oO0o0O0Ooo0o , ooOO00oOOo000 , o00 )
 oO = xbmcgui . Dialog ( )
 oO . ok ( "GenieTv" , "Please Disconnect The Power From Your Device. DO NOT EXIT CLEANLY VIA SHUTDOWN" , "[COLOR yellow]Brought To You By Architects@Work[/COLOR]" )
 if 68 - 68: O0 + I1IiI / O0ooOooooO - i1I111II1I + iIii1I11I1II1 % iI
 if 23 - 23: OOO0OOo % OOooOOo / Oooo0Ooo000
def i11I1II ( name , url , description ) :
 ooOO00oOOo000 = xbmc . translatePath ( os . path . join ( 'special://' , 'home' ) )
 o00 = xbmcgui . DialogProgress ( )
 oO0o0O0Ooo0o = os . path . join ( i11 )
 time . sleep ( 2 )
 o00 . create ( "GenieTv" , "Restoring" , '' , 'Please Wait' )
 print '======================================='
 print ooOO00oOOo000
 print '======================================='
 extract . all ( oO0o0O0Ooo0o , ooOO00oOOo000 , o00 )
 oO = xbmcgui . Dialog ( )
 oO . ok ( "GenieTv" , "Please Disconnect The Power From Your Device. DO NOT EXIT CLEANLY VIA SHUTDOWN" , "[COLOR yellow]Brought To You By Architects@Work[/COLOR]" )
 if 79 - 79: Ooo00oOo00o . i1I111ii1II1i * iI - i1I111II1I + OOO0OOo
 if 14 - 14: i11iIiiIii - i1I111ii1II1i * I1IiI
def I1iIi1iiIIiI ( ) :
 OO0oIII111i11IiI = xbmcgui . Dialog ( ) . yesno ( 'Force Close Kodi' , 'You are about to close Kodi' , 'Would you like to continue?' , nolabel = 'No, Cancel' , yeslabel = 'Yes, Close' )
 if OO0oIII111i11IiI == 0 :
  return
 elif OO0oIII111i11IiI == 1 :
  pass
 O0000 = ooO00O0O0 ( )
 print "Platform: " + str ( O0000 )
 if O0000 == 'osx' :
  print "############   try osx force close  #################"
  try : os . system ( 'killall -9 XBMC' )
  except : pass
  try : os . system ( 'killall -9 Kodi' )
  except : pass
  oO . ok ( "[COLOR=red][B]WARNING  !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu." , '' )
 elif O0000 == 'linux' :
  print "############   try linux force close  #################"
  try : os . system ( 'killall XBMC' )
  except : pass
  try : os . system ( 'killall Kodi' )
  except : pass
  try : os . system ( 'killall -9 xbmc.bin' )
  except : pass
  try : os . system ( 'killall -9 kodi.bin' )
  except : pass
  oO . ok ( "[COLOR=red][B]WARNING  !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu." , '' )
 elif O0000 == 'android' :
  print "############   try android force close  #################"
  try : os . system ( 'adb shell am force-stop org.xbmc.kodi' )
  except : pass
  try : os . system ( 'adb shell am force-stop org.kodi' )
  except : pass
  try : os . system ( 'adb shell am force-stop org.xbmc.xbmc' )
  except : pass
  try : os . system ( 'adb shell am force-stop org.xbmc' )
  except : pass
  oO . ok ( "[COLOR=red][B]WARNING  !!![/COLOR][/B]" , "Your system has been detected as Android, you " , "[COLOR=yellow][B]MUST[/COLOR][/B] force close XBMC/Kodi. [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu." , "Pulling the power cable is the simplest method to force close." )
 elif O0000 == 'windows' :
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
  oO . ok ( "[COLOR=red][B]WARNING  !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu." , "Use task manager and NOT ALT F4" )
 else :
  print "############   try atv force close  #################"
  try : os . system ( 'killall AppleTV' )
  except : pass
  print "############   try raspbmc force close  #################"
  try : os . system ( 'sudo initctl stop kodi' )
  except : pass
  try : os . system ( 'sudo initctl stop xbmc' )
  except : pass
  oO . ok ( "[COLOR=red][B]WARNING  !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit via the menu." , "Your platform could not be detected so just pull the power cable." )
  if 33 - 33: Oo
def ooO00O0O0 ( ) :
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
  if 49 - 49: Ooo00oOo00o % i1I111ii1II1i % i1I111ii1II1i / i1I111ii1II1i
  if 53 - 53: iIii1I11I1II1
  if 68 - 68: OoooooooOO % OoOoOO00
def Ii1i1i1111 ( url ) :
 o00 . create ( "[COLOR=green]GenieTv[/COLOR]" , "Renaming paths..." , '' , 'Please Wait' )
 for o0oO0O00oOo , iIi11i1 , oO00oo0o00o0o in os . walk ( url ) :
  for file in oO00oo0o00o0o :
   if file . endswith ( ".xml" ) :
    o00 . update ( 0 , "Fixing" , file , 'Please Wait' )
    iII1ii1 = open ( ( os . path . join ( o0oO0O00oOo , file ) ) ) . read ( )
    I1111I1II11 = iII1ii1 . replace ( i1iiIIiiI111 , 'special://home/' )
    i1i1ii = open ( ( os . path . join ( o0oO0O00oOo , file ) ) , mode = 'w' )
    i1i1ii . write ( str ( I1111I1II11 ) )
    i1i1ii . close ( )
 I1iIi1iiIIiI ( )
 if 30 - 30: OoooooooOO % OoooooooOO
def oOoOoo0 ( ) :
 OO0oo = Iii1 ( oOOoo00O0O ( 'aHR0cDovL3d3dy5saXN0ZW5saXZlLmV1L3VrLmh0bWw=' ) )
 oo0O0oO = re . compile ( '<tr>.+?<td><a href=".+?"><b>(.+?)</b>.+?<td><a href="(.+?)">' , re . DOTALL ) . findall ( OO0oo )
 for IiI111111IIII , oOo0 in oo0O0oO :
  ii1II ( IiI111111IIII , oOo0 , 222 , i1iIIi1 + 'radio.png' )
  if 50 - 50: iI + i1IIi / O0 / OOooOOo
def Iii ( ) :
 OO0oo = Iii1 ( oOOoo00O0O ( 'aHR0cDovL3d3dy50b29uamV0LmNvbS8=' ) )
 oo0O0oO = re . compile ( '<a href="(.+?)" style="font-size:.8em;">(.+?)</a>' ) . findall ( OO0oo )
 for oOo0 , IiI111111IIII in oo0O0oO :
  Oo00oo0000OO ( '[COLORgreen]' + IiI111111IIII + '[/COLOR]' , 'http://www.toonjet.com/' + oOo0 , 8051 , i1iIIi1 + 'classictoons.png' )
def i1I1 ( url ) :
 OO0oo = Iii1 ( url )
 oo0O0oO = re . compile ( '<a href="(.+?)"><img src="(.+?)"' ) . findall ( OO0oo )
 IIIIiiIiiI = re . compile ( '<a href="(.+?)">.+?</a></td></tr></table>' ) . findall ( OO0oo )
 for url , OO0ooOOO0OOO in oo0O0oO :
  if 'ol.gif' in OO0ooOOO0OOO :
   pass
  elif 'link_block_' in OO0ooOOO0OOO :
   pass
  elif '.png' in OO0ooOOO0OOO :
   pass
  else :
   Oo00oo0000OO ( ( OO0ooOOO0OOO ) . replace ( 'http://www.toonjet.com/images/icons/' , '' ) . replace ( 'images/icons/' , '' ) . replace ( '.jpg' , '' ) . replace ( '_icon' , '' ) . replace ( '_' , ' ' ) , 'http://www.toonjet.com/' + url , 8052 , i1iIIi1 + 'vod.png' )
 for url in IIIIiiIiiI :
  Oo00oo0000OO ( 'NEXT PAGE' , 'http://www.toonjet.com/' + url , 8051 , i1iIIi1 + 'Next.png' )
def O0II11i11II ( url ) :
 OO0oo = Iii1 ( url )
 oo0O0oO = re . compile ( '<iframe width="640" height="480" src="(.+?)" frameborder="0" allowfullscreen></iframe>' ) . findall ( OO0oo )
 for url in oo0O0oO :
  ii1II ( '[COLORgreen]PLAY[/COLOR]' , ( url ) . replace ( 'http://www.youtube.com/embed/' , '' ) . replace ( '?autoplay=0' , '' ) , 8043 , i1iIIi1 + 'classictoons.png' )
  if 29 - 29: Oo % Ooo00oOo00o % OoOo00o . OOooOOo / OoooooooOO * OOO0OOo
  if 54 - 54: O0
def OOoO000O00oO ( ) :
 i1OoOO ( 'Audio Books' , '' , 30011 , i1iIIi1 + 'audiobooks.png' , i1iIIi1 + 'audiobooks.png' , '' )
 i1OoOO ( 'Kids Audio Books' , '' , 30006 , i1iIIi1 + 'kidsaudiobooks.png' , i1iIIi1 + 'kidsaudiobooks.png' , '' )
 if 44 - 44: i1I111II1I
def O0O0o0o0o ( ) :
 i1OoOO ( 'All' , '' , 30001 , i1iIIi1 + 'kodible.png' , i1iIIi1 + 'kodible.png' , '' )
 i1OoOO ( 'Popular' , '' , 30012 , i1iIIi1 + 'POPULARv.png' , i1iIIi1 + 'POPULARv.png' , '' )
 i1OoOO ( 'Search' , '' , 30013 , i1iIIi1 + 'search.png' , i1iIIi1 + 'search.png' , '' )
 if 9 - 9: Oo + I1IiI - iIii1I11I1II1 - iI + OOooOOo
def o000O0OOoo ( ) :
 iIIiIi1iIII1 = OooOOOOo ( II11iiii1Ii + 'books' + OooO0 )
 oo0O0oO = re . compile ( '<NAME=>(.*?)</NAME><URL=>(.*?)</URL><CAT=>(.*?)</CAT>' ) . findall ( iIIiIi1iIII1 )
 for IiI111111IIII , oOo0 , Oo00OOOOoo0oo in oo0O0oO :
  if 'Parent' in IiI111111IIII :
   pass
  elif '2' in Oo00OOOOoo0oo :
   i1OoOO ( ( IiI111111IIII ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , oOo0 , 30010 , i1iIIi1 + 'kodible.png' , i1iIIi1 + 'kodible.png' , '' )
   if 80 - 80: o00OO00OoO * I1IiI * OoOoOO00 - O0 . I1IiI % OOOo0
def II1 ( ) :
 IIiiIiII1Ii = i1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 iIIII11I1II = IIiiIiII1Ii . lower ( )
 iIIiIi1iIII1 = OooOOOOo ( II11iiii1Ii + 'books' + OooO0 )
 oo0O0oO = re . compile ( '<NAME=>(.*?)</NAME><URL=>(.*?)</URL><CAT=>(.*?)</CAT>' ) . findall ( iIIiIi1iIII1 )
 for IiI111111IIII , oOo0 , Oo00OOOOoo0oo in oo0O0oO :
  if IIiiIiII1Ii in IiI111111IIII . lower ( ) :
   if '1' in Oo00OOOOoo0oo :
    i1OoOO ( ( IiI111111IIII ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , oOo0 , 30010 , i1iIIi1 + 'kodible.png' , i1iIIi1 + 'kodible.png' , '' )
   elif '2' in Oo00OOOOoo0oo :
    i1OoOO ( ( IiI111111IIII ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , oOo0 , 30010 , i1iIIi1 + 'kodible.png' , i1iIIi1 + 'kodible.png' , '' )
   elif '3' in Oo00OOOOoo0oo :
    i1OoOO ( ( IiI111111IIII ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , oOo0 , 30009 , i1iIIi1 + 'kodible.png' , i1iIIi1 + 'kodible.png' , '' )
    if 32 - 32: OOOo0 - ii11ii1ii - Oo
    if 32 - 32: i1IIi . Oooo0Ooo000 / Ooo00oOo00o
def o0OOoOoO00 ( ) :
 iIIiIi1iIII1 = OooOOOOo ( II11iiii1Ii + 'books' + OooO0 )
 oo0O0oO = re . compile ( '<NAME=>(.*?)</NAME><URL=>(.*?)</URL><CAT=>(.*?)</CAT>' ) . findall ( iIIiIi1iIII1 )
 for IiI111111IIII , oOo0 , Oo00OOOOoo0oo in oo0O0oO :
  if '1' in Oo00OOOOoo0oo :
   i1OoOO ( ( IiI111111IIII ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , oOo0 , 3010 , i1iIIi1 + 'kodible.png' , i1iIIi1 + 'kodible.png' , '' )
  elif '2' in Oo00OOOOoo0oo :
   i1OoOO ( ( IiI111111IIII ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , oOo0 , 30010 , i1iIIi1 + 'kodible.png' , i1iIIi1 + 'kodible.png' , '' )
  elif '3' in Oo00OOOOoo0oo :
   i1OoOO ( ( IiI111111IIII ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , oOo0 , 30009 , i1iIIi1 + 'kodible.png' , i1iIIi1 + 'kodible.png' , '' )
   if 15 - 15: OoOo00o / O0 . OOooOOo . i11iIiiIii
 xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 59 - 59: o00OO00OoO - OOooOOo - OOO0OOo
def Ii11iI ( url ) :
 IIo0o0O0O00oOOo = url
 iIIiIi1iIII1 = OooOOOOo ( url )
 IIIIiiIiiI = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( iIIiIi1iIII1 )
 for url , IiI111111IIII in IIIIiiIiiI :
  if 'mp3' in IiI111111IIII :
   IIIIii ( ( IiI111111IIII ) . replace ( '%20' , ' ' ) , IIo0o0O0O00oOOo + url , 10012 , i1iIIi1 + 'kodible.png' , i1iIIi1 + 'kodible.png' , '' )
  if 'wma' in IiI111111IIII :
   IIIIii ( ( IiI111111IIII ) . replace ( '%20' , ' ' ) , IIo0o0O0O00oOOo + url , 10012 , i1iIIi1 + 'kodible.png' , i1iIIi1 + 'kodible.png' , '' )
  if 'm4b' in IiI111111IIII :
   IIIIii ( ( IiI111111IIII ) . replace ( '%20' , ' ' ) , IIo0o0O0O00oOOo + url , 10012 , i1iIIi1 + 'kodible.png' , i1iIIi1 + 'kodible.png' , '' )
  elif '/' in IiI111111IIII :
   i1OoOO ( ( IiI111111IIII ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , IIo0o0O0O00oOOo + url , 30009 , i1iIIi1 + 'kodible.png' , i1iIIi1 + 'kodible.png' , '' )
   if 52 - 52: i1I111II1I - i1I111ii1II1i * O0ooOooooO
   if 17 - 17: OoooooooOO + i1I111II1I * Oooo0Ooo000 * I1IiI
   if 36 - 36: O0 + Oo
def iIIIi1i1I11i ( url ) :
 iIIiIi1iIII1 = OooOOOOo ( url )
 IIo0o0O0O00oOOo = url
 oo0O0oO = re . compile ( '<li><a href="(.+?)">(.+?)</a></li>' ) . findall ( iIIiIi1iIII1 )
 for url , IiI111111IIII in oo0O0oO :
  if 'Parent' in IiI111111IIII :
   pass
  elif '.db' in IiI111111IIII :
   pass
  elif '.jpg' in IiI111111IIII :
   pass
  elif '.html' in IiI111111IIII :
   pass
  elif '.doc' in IiI111111IIII :
   pass
  elif 'mp3' in IiI111111IIII :
   IIIIii ( ( IiI111111IIII ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , IIo0o0O0O00oOOo + url , 10012 , i1iIIi1 + 'kodible.png' , i1iIIi1 + 'kodible.png' , '' )
  elif 'm4a' in IiI111111IIII :
   IIIIii ( ( IiI111111IIII ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , IIo0o0O0O00oOOo + url , 10012 , i1iIIi1 + 'kodible.png' , i1iIIi1 + 'kodible.png' , '' )
  else :
   i1OoOO ( ( IiI111111IIII ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , IIo0o0O0O00oOOo + url , 30010 , i1iIIi1 + 'kodible.png' , i1iIIi1 + 'kodible.png' , '' )
   if 55 - 55: Oo - i1I111II1I
   if 84 - 84: o00OO00OoO + Oo - I1IiI * I1IiI
def OoooO0o ( ) :
 i1OoOO ( 'A-Z' , '' , 7 , i1iIIi1 + 'kodible.png' , i1iIIi1 + 'kodible.png' , '' )
 i1OoOO ( 'All' , '' , 3 , i1iIIi1 + 'kodible.png' , i1iIIi1 + 'kodible.png' , '' )
 i1OoOO ( 'Search' , '' , 14 , i1iIIi1 + 'kodible.png' , i1iIIi1 + 'kodible.png' , '' )
 if 24 - 24: I1IiI % i1IIi + i1I111ii1II1i . i11iIiiIii . ii11ii1ii
def IIi1II ( ) :
 iIIiIi1iIII1 = OooOOOOo ( oOOoo00O0O ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9tcDNfZG93bmxvYWRzLmh0bQ==' ) )
 oo0O0oO = re . compile ( '<td width=".+?" align="center">.+?<a href="(.*?)">.+?<img border="0" src="images/Squeeze%20(.*?).gif" width="74" height=".*?"></a></td>' , re . DOTALL ) . findall ( iIIiIi1iIII1 )
 for oOo0 , OO0ooOOO0OOO in oo0O0oO :
  print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<' + oOo0 + '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
  if '-x' in OO0ooOOO0OOO :
   pass
  else :
   i1OoOO ( OO0ooOOO0OOO , ( oOOoo00O0O ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) ) + ( oOo0 ) . replace ( 'colour_it' , 'books_audio/audio_books_a' ) , 30008 , ( oOOoo00O0O ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9pbWFnZXMvU3F1ZWV6ZSUyMA==' ) ) + OO0ooOOO0OOO + '.gif' , i1iIIi1 + 'kodible.png' , '' )
   if 2 - 2: OoOoOO00 - Ooo00oOo00o . OoOo00o * i1I111ii1II1i / O0ooOooooO
 xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 80 - 80: i1I111II1I / Oooo0Ooo000 / I1IiI + i1IIi - Oo
 if 11 - 11: OOooOOo * Ooo00oOo00o
def iIi1IiI ( url ) :
 iIIiIi1iIII1 = OooOOOOo ( url )
 oo0O0oO = re . compile ( '<td width=".*?" height=".*?"><b>.*?<a href="(.*?)">(.*?)</a></b></td>' , re . DOTALL ) . findall ( iIIiIi1iIII1 )
 for url , IiI111111IIII in oo0O0oO :
  if '</a>' in IiI111111IIII :
   pass
  elif '(' in IiI111111IIII :
   i1OoOO ( ( IiI111111IIII ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '.mp3' , '' ) , oOOoo00O0O ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) + url , 30005 , i1iIIi1 + 'kodible.png' , i1iIIi1 + 'kodible.png' , '' )
  else :
   IIIIii ( ( IiI111111IIII ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '.mp3' , '' ) , oOOoo00O0O ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) + url , 30004 , i1iIIi1 + 'kodible.png' , i1iIIi1 + 'kodible.png' , '' )
   if 14 - 14: OoOo00o % O0ooOooooO % Oo - i11iIiiIii
 xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 53 - 53: iI % Oo
def O0ooOo0o0Oo ( ) :
 IIiiIiII1Ii = i1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 iIIII11I1II = IIiiIiII1Ii . lower ( )
 iIIiIi1iIII1 = OooOOOOo ( oOOoo00O0O ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9jb21wbGV0ZV9saXN0Lmh0bQ==' ) )
 oo0O0oO = re . compile ( '<td width=".+?">.*?<b>.+?<a href="(.*?)">(.*?)</a></b></td>' , re . DOTALL ) . findall ( iIIiIi1iIII1 )
 for oOo0 , IiI111111IIII in oo0O0oO :
  if IIiiIiII1Ii in IiI111111IIII . lower ( ) :
   if '</a>' in IiI111111IIII :
    pass
   elif '(' in IiI111111IIII :
    i1OoOO ( ( IiI111111IIII ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , oOOoo00O0O ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + oOo0 , 30005 , i1iIIi1 + 'kodible.png' , i1iIIi1 + 'kodible.png' , '' )
   else :
    IIIIii ( ( IiI111111IIII ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , oOOoo00O0O ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + oOo0 , 30004 , i1iIIi1 + 'kodible.png' , i1iIIi1 + 'kodible.png' , '' )
    if 71 - 71: iIii1I11I1II1 - i1I111II1I . OOOo0 % OoooooooOO + i1I111II1I
    if 26 - 26: Oo + i1I111II1I / Ooo00oOo00o % I1IiI % ii11ii1ii + OoOoOO00
def i11I1I1iiI ( ) :
 iIIiIi1iIII1 = OooOOOOo ( oOOoo00O0O ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9jb21wbGV0ZV9saXN0Lmh0bQ==' ) )
 oo0O0oO = re . compile ( '<td width=".+?">.*?<b>.+?<a href="(.*?)">(.*?)</a></b></td>' , re . DOTALL ) . findall ( iIIiIi1iIII1 )
 for oOo0 , IiI111111IIII in oo0O0oO :
  if '</a>' in IiI111111IIII :
   pass
  elif '(' in IiI111111IIII :
   i1OoOO ( ( IiI111111IIII ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , oOOoo00O0O ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + oOo0 , 30005 , i1iIIi1 + 'kodible.png' , i1iIIi1 + 'kodible.png' , '' )
  else :
   IIIIii ( ( IiI111111IIII ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , oOOoo00O0O ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + oOo0 , 30004 , i1iIIi1 + 'kodible.png' , i1iIIi1 + 'kodible.png' , '' )
   if 34 - 34: Oooo0Ooo000 % OOO0OOo . O0 . iIii1I11I1II1
 xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 93 - 93: i1IIi . i11iIiiIii . Oo
 if 99 - 99: Oooo0Ooo000 - o00OO00OoO - O0ooOooooO % Ooo00oOo00o
def IiiIIiiiiii ( url ) :
 iIIiIi1iIII1 = OooOOOOo ( url )
 oo0O0oO = re . compile ( '<a href="(.+?)">Download</a></b></td>' ) . findall ( iIIiIi1iIII1 )
 for url in oo0O0oO :
  IIo0o0O0O00oOOo = ( oOOoo00O0O ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) ) + url
  Resolve ( IIo0o0O0O00oOOo )
  if 100 - 100: Oo + OOooOOo - O0 % OoOoOO00 . i1I111ii1II1i
def ooOo0OoOooo00 ( url ) :
 iIIiIi1iIII1 = OooOOOOo ( url )
 oo0O0oO = re . compile ( '<td width="247">(.*?)</td>.*?<a href="(.+?)">' , re . DOTALL ) . findall ( iIIiIi1iIII1 )
 for IiI111111IIII , url in oo0O0oO :
  if '<p align' in IiI111111IIII :
   pass
  elif '&nbsp;' in IiI111111IIII :
   pass
  else :
   IIIIii ( ( IiI111111IIII ) . replace ( '&nbsp;' , '' ) , oOOoo00O0O ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) + url , 10012 , i1iIIi1 + 'kodible.png' , i1iIIi1 + 'kodible.png' , '' )
   if 96 - 96: ii11ii1ii % OOO0OOo % iI - OOO0OOo % I1IiI + ii11ii1ii
 xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 3 - 3: O0
 if 64 - 64: i1IIi % OOO0OOo / i11iIiiIii - i1IIi % i1I111II1I . i1I111ii1II1i
def II1i111 ( ) :
 iIIiIi1iIII1 = cloudflare . source ( oOOoo00O0O ( 'aHR0cDovL3dhdGNoY2FydG9vbnNvbmxpbmUuZXUv' ) )
 oo0O0oO = re . compile ( 'class="menu-item menu-item-type-.+?><a href="([^"]*)">(.+?)</a></li>' , re . DOTALL ) . findall ( iIIiIi1iIII1 )
 for oOo0 , IiI111111IIII in oo0O0oO :
  if 'ongoing' in oOo0 :
   IIIIii ( '[COLORgreen]' + IiI111111IIII + '[/COLOR]' , oOo0 , 21005 , i1iIIi1 + 'on-going.png' , '' , '' )
  if 'cartoon-series' in oOo0 :
   IIIIii ( '[COLORgreen]' + IiI111111IIII + '[/COLOR]' , oOo0 , 21005 , i1iIIi1 + 'cartoonseries.png' , '' , '' )
  if 'disney' in oOo0 :
   IIIIii ( '[COLORgreen]' + IiI111111IIII + '[/COLOR]' , oOo0 , 21005 , i1iIIi1 + 'disneytoons.png' , '' , '' )
  if 'genre' in oOo0 :
   IIIIii ( '[COLORgreen]' + IiI111111IIII + '[/COLOR]' , oOo0 , 21005 , i1iIIi1 + 'cartoongenre.png' , '' , '' )
  if 'years' in oOo0 :
   IIIIii ( '[COLORgreen]' + IiI111111IIII + '[/COLOR]' , oOo0 , 21005 , i1iIIi1 + 'years.png' , '' , '' )
def i1iiiIii11 ( url ) :
 iIIiIi1iIII1 = cloudflare . source ( url )
 oo0O0oO = re . compile ( '<a href="([^"]*)" title="([^"]*)" rel="nofollow" id="featured-thumbnail">.+?<div class="featured-thumbnail"><img width="140" height="200" src="([^"]*)"' , re . DOTALL ) . findall ( iIIiIi1iIII1 )
 OOoOOO000O0 = re . compile ( '<button type="button"><a href="([^"]*)" target="_blank">(.+?)</a>' ) . findall ( iIIiIi1iIII1 )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' ) . findall ( iIIiIi1iIII1 )
 for url , IiI111111IIII , OO0ooOOO0OOO in oo0O0oO :
  IIIIii ( '[COLORgreen]' + IiI111111IIII + '[/COLOR]' , url , 21006 , OO0ooOOO0OOO , OO0ooOOO0OOO , IiI111111IIII )
 for url , IiI111111IIII in OOoOOO000O0 :
  IIIIii ( '[COLORgreen]' + IiI111111IIII + '[/COLOR]' , url , 21005 , i1iIIi1 + 'watchcartoons.png' , '' , '' )
 for url in next :
  IIIIii ( '[COLORgreen]NEXT[/COLOR]' , url , 21005 , i1iIIi1 + 'Next.png' , '' , '' )
def oOo0II1i11I1 ( url ) :
 iIIiIi1iIII1 = cloudflare . source ( url )
 oo0O0oO = re . compile ( '<li><a href="([^"]*)" >(.+?)</a></li>' , re . DOTALL ) . findall ( iIIiIi1iIII1 )
 iiIiIiII = re . compile ( 'file:"([^"]*)",type:"mp4",label:"([^"]*)"' , re . DOTALL ) . findall ( iIIiIi1iIII1 )
 i1I1iIi = re . compile ( 'src="([^"]*)" frameborder=' ) . findall ( iIIiIi1iIII1 )
 iIIiooO00O00oOO = re . compile ( '<iframe src="([^"]*)"' ) . findall ( iIIiIi1iIII1 )
 for url , IiI111111IIII in oo0O0oO :
  IIIIii ( '[COLORgreen]' + IiI111111IIII + '[/COLOR]' , url , 21007 , i1iIIi1 + 'watchcartoons.png' , '' , '' )
 for url in i1I1iIi :
  IIIIii ( '[COLORgreen]PLAY[/COLOR]' , 'http:' + url , 222 , i1iIIi1 + 'watchcartoons.png' , '' , '' )
 for url , IiI111111IIII in iiIiIiII :
  I1I1IiI1 ( '[COLORgreen]' + IiI111111IIII + '[/COLOR]' , url , 222 , i1iIIi1 + 'watchcartoons.png' , '' , '' )
 else :
  IIIIii ( '[COLORgreen]NO STREAMS AVAILABLE[/COLOR]' , url , 21005 , i1iIIi1 + 'watchcartoons.png' , '' , '' )
def I1 ( url ) :
 iIIiIi1iIII1 = cloudflare . source ( url )
 oo0O0oO = re . compile ( 'file:"([^"]*)",type:"mp4",label:"([^"]*)"' , re . DOTALL ) . findall ( iIIiIi1iIII1 )
 for url , IiI111111IIII in oo0O0oO :
  I1I1IiI1 ( '[COLORgreen]' + IiI111111IIII + '[/COLOR]' , url , 222 , i1iIIi1 + 'watchcartoons.png' , '' , '' )
  if 48 - 48: OOOo0 + ii11ii1ii + OoOoOO00 * i11iIiiIii
def IiIIi1I1I11Ii ( ) :
 Oo00oo0000OO ( '[COLORgreen]CARTOONS[/COLOR]' , '' , 20001 , i1iIIi1 + 'ORIGINCARTOON.png' )
 Oo00oo0000OO ( '[COLORgreen]ANIME[/COLOR]' , 'https://kissanime.to/AnimeList' , 20001 , i1iIIi1 + 'ORIGINCARTOON.png' )
 if 64 - 64: OoooooooOO
def oO0oooooo ( ) :
 Oo00oo0000OO ( '[COLORgreen]BY NAME[/COLOR]' , 'http://kisscartoon.me/CartoonList' , 20002 , i1iIIi1 + 'ORIGINCARTOON.png' )
 Oo00oo0000OO ( '[COLORgreen]BY GENRE[/COLOR]' , 'http://kisscartoon.me/CartoonList' , 20003 , i1iIIi1 + 'ORIGINCARTOON.png' )
 if 65 - 65: OoOo00o + Oo
def Ooo0O0 ( url ) :
 iIIiIi1iIII1 = cloudflare . source ( url )
 oo0O0oO = re . compile ( 'href="(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( iIIiIi1iIII1 )
 for url , IiI111111IIII in oo0O0oO :
  if '?c=' in url :
   Oo00oo0000OO ( '[COLORgreen]' + IiI111111IIII + '[/COLOR]' , 'http://kisscartoon.me' + url , 20004 , i1iIIi1 + 'ORIGINCARTOON.png' )
   if 71 - 71: OoooooooOO
def iIiI1iiiI1ii ( url ) :
 iIIiIi1iIII1 = cloudflare . source ( url )
 oo0O0oO = re . compile ( 'href="(.+?)" title="(.+?)">/n(.+?)</a><br/>' , re . DOTALL ) . findall ( iIIiIi1iIII1 )
 for url , I1i , IiI111111IIII in oo0O0oO :
  if 'Genre' in url :
   Oo00oo0000OO ( '[COLORgreen]' + IiI111111IIII + '[/COLOR]' , 'http://kisscartoon.me' + url , 20004 , i1iIIi1 + 'ORIGINCARTOON.png' )
   if 67 - 67: I1IiI / OOooOOo * Ooo00oOo00o / i1I111II1I * ii11ii1ii / O0ooOooooO
def OOoOO0OO ( url ) :
 iIIiIi1iIII1 = cloudflare . source ( url )
 oo0O0oO = re . compile ( 'src="(.+?)" style=.+?<a class="bigChar" href="(.+?)">(.+?)</a>.+?<p>(.+?)</p>' , re . DOTALL ) . findall ( iIIiIi1iIII1 )
 for url , I1i , IiI111111IIII in oo0O0oO :
  IIIIii ( '[COLORgreen]' + IiI111111IIII + '[/COLOR]' , 'http://kisscartoon.me' + url , 20005 , img , '' , I1i )
  if 26 - 26: i1I111ii1II1i . i1I111ii1II1i
def i1oO ( url ) :
 iIIiIi1iIII1 = cloudflare . source ( url )
 oo0O0oO = re . compile ( '<img width="120" height="165" src="(.+?)" style=.+?<a class="bigChar" href="(.+?)">(.+?)</a>.+?<p>(.+?)</p>' , re . DOTALL ) . findall ( iIIiIi1iIII1 )
 for url , I1i , IiI111111IIII in oo0O0oO :
  IIIIii ( '[COLORgreen]' + IiI111111IIII + '[/COLOR]' , 'http://kisscartoon.me' + url , 20005 , img , '' , I1i )
  if 30 - 30: Oo . Ooo00oOo00o
  if 57 - 57: Oooo0Ooo000 . Oo + OoOoOO00
  if 43 - 43: o00OO00OoO % i1I111ii1II1i
  if 69 - 69: i1I111ii1II1i % Ooo00oOo00o
  if 86 - 86: O0ooOooooO / O0ooOooooO
def IiiI ( ) :
 if 19 - 19: OoOoOO00
 IIIIii ( '[COLORgreen]Cartoons[/COLOR]' , oOOoo00O0O ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2NhcnRvb24=' ) , 10004 , i1iIIi1 + 'ORIGINCARTOON.png' , oooOOOOO , '' )
 IIIIii ( '[COLORgreen]Search Cartoons[/COLOR]' , '' , 10005 , i1iIIi1 + 'ORIGINCARTOON.png' , oooOOOOO , '' )
 if 72 - 72: OoooooooOO / OOOo0 + iI / I1IiI * iI
def Ii1iIi111i1i1 ( ) :
 IIiiIiII1Ii = i1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 iIIII11I1II = IIiiIiII1Ii . lower ( )
 iIIiIi1iIII1 = OooOOOOo ( oOOoo00O0O ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2NhcnRvb24=' ) )
 oo0O0oO = re . compile ( '<td><a href="(.+?)">(.+)</a></td>' ) . findall ( iIIiIi1iIII1 )
 for oOo0 , IiI111111IIII in oo0O0oO :
  if IIiiIiII1Ii in IiI111111IIII . lower ( ) :
   if 'Dad!' in IiI111111IIII :
    pass
   elif 'Family Guy' in IiI111111IIII :
    pass
   elif '2 Stupid' in IiI111111IIII :
    pass
   elif 'The Zelfs' in IiI111111IIII :
    pass
   elif 'A Clone' in IiI111111IIII :
    pass
   elif 'A.T.O.M' in IiI111111IIII :
    pass
   elif 'Almost Naked' in IiI111111IIII :
    pass
   elif 'Angry Kid' in IiI111111IIII :
    pass
   elif 'Annoying Orange' in IiI111111IIII :
    pass
   elif 'Aqua Teen' in IiI111111IIII :
    pass
   elif 'Assy Mcgee' in IiI111111IIII :
    pass
   elif 'Astroblast' in IiI111111IIII :
    pass
   elif 'Atomic Betty' in IiI111111IIII :
    pass
   elif 'Axe Cop' in IiI111111IIII :
    pass
   elif 'Baby Playpen' in IiI111111IIII :
    pass
   elif 'Beavis and Butt' in IiI111111IIII :
    pass
   elif 'Celebrity Deathmatch' in IiI111111IIII :
    pass
   elif 'Clerks The' in IiI111111IIII :
    pass
   elif 'Crapston Villas' in IiI111111IIII :
    pass
   elif 'Duckman:' in IiI111111IIII :
    pass
   elif 'Stripperella' in IiI111111IIII :
    pass
   elif 'Vixen' in IiI111111IIII :
    pass
   else :
    IIIIii ( '[COLORgreen]' + IiI111111IIII + '[/COLOR]' , oOo0 , 10006 , i1iIIi1 + 'ORIGINCARTOON.png' , oooOOOOO , '' )
  xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 45 - 45: I1IiI . OOooOOo % I1IiI * OOOo0 % OOOo0
def oOoOo00ooOooo ( url ) :
 OO0oo = OooOOOOo ( url )
 oo0O0oO = re . compile ( '<td><a href="(.+?)">(.+)</a></td>' ) . findall ( OO0oo )
 for url , IiI111111IIII in oo0O0oO :
  if 'Dad!' in IiI111111IIII :
   pass
  elif 'Family Guy' in IiI111111IIII :
   pass
  elif '2 Stupid' in IiI111111IIII :
   pass
  elif 'The Zelfs' in IiI111111IIII :
   pass
  elif 'A Clone' in IiI111111IIII :
   pass
  elif 'A.T.O.M' in IiI111111IIII :
   pass
  elif 'Almost Naked' in IiI111111IIII :
   pass
  elif 'Angry Kid' in IiI111111IIII :
   pass
  elif 'Annoying Orange' in IiI111111IIII :
   pass
  elif 'Aqua Teen' in IiI111111IIII :
   pass
  elif 'Assy Mcgee' in IiI111111IIII :
   pass
  elif 'Astroblast' in IiI111111IIII :
   pass
  elif 'Atomic Betty' in IiI111111IIII :
   pass
  elif 'Axe Cop' in IiI111111IIII :
   pass
  elif 'Baby Playpen' in IiI111111IIII :
   pass
  elif 'Beavis and Butt' in IiI111111IIII :
   pass
  elif 'Celebrity Deathmatch' in IiI111111IIII :
   pass
  elif 'Clerks The' in IiI111111IIII :
   pass
  elif 'Crapston Villas' in IiI111111IIII :
   pass
  elif 'Duckman:' in IiI111111IIII :
   pass
  elif 'Stripperella' in IiI111111IIII :
   pass
  elif 'Vixen' in IiI111111IIII :
   pass
  else :
   IIIIii ( '[COLORgreen]' + IiI111111IIII + '[/COLOR]' , url , 10006 , i1iIIi1 + 'ORIGINCARTOON.png' , oooOOOOO , '' )
 xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 12 - 12: i11iIiiIii . I1IiI % Oo - OoooooooOO . O0
def OOoO00oo0000O ( url ) :
 OO0oo = OooOOOOo ( url )
 IIIIiiIiiI = re . compile ( '<img src="(.+?)" id="series_image" width="250" height="370" alt=".+?" />' ) . findall ( OO0oo )
 for OO0ooOOO0OOO in IIIIiiIiiI :
  Ii1IIi = OO0ooOOO0OOO
 oO0o = re . compile ( '<li><a href="(.+?)">Next</a></li>' ) . findall ( OO0oo )
 for url in oO0o :
  IIIIii ( '[COLORgreen]NEXT PAGE[/COLOR]' , url , 10006 , i1iIIi1 + 'Next.png' , oooOOOOO , '' )
 oo0O0oO = re . compile ( '&nbsp;<a href="(.+?)">(.+?)</a>' ) . findall ( OO0oo )
 for url , IiI111111IIII in oo0O0oO :
  ii1II ( '[COLORgreen]' + IiI111111IIII + '[/COLOR]' , url , 10007 , Ii1IIi )
  if 84 - 84: O0 - OoOoOO00 . Oo / O0ooOooooO . OoooooooOO + i11iIiiIii
  if 86 - 86: Oooo0Ooo000 / OOooOOo - OOooOOo + ii11ii1ii + O0ooOooooO
 xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 33 - 33: OOooOOo . i1I111ii1II1i . OoOo00o . i1IIi
def i1II1iII ( url , IMAGE ) :
 OO0oo = OooOOOOo ( url )
 oo0O0oO = re . compile ( '"playlist">(.+?)</span></div><div><iframe src="(.+?)"' ) . findall ( OO0oo )
 for IiI111111IIII , url in oo0O0oO :
  print IiI111111IIII + '     ' + url
  if 'easy' in url :
   II1i ( url )
   if 81 - 81: ii11ii1ii
   if 94 - 94: Oooo0Ooo000 + OoOoOO00 % i11iIiiIii
  xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 8 - 8: OOO0OOo * O0
def II1i ( url ) :
 OO0oo = OooOOOOo ( url )
 oo0O0oO = re . compile ( "url: '(.+?)'," ) . findall ( OO0oo )
 for url in oo0O0oO :
  OOoO ( url )
  if 18 - 18: iIii1I11I1II1 + Oo - i1I111II1I + OoooooooOO * OoooooooOO
  if 41 - 41: OOO0OOo . Oo + OOOo0
  if 100 - 100: iI + Ooo00oOo00o
def Oo00o0OO ( ) :
 if 73 - 73: OOooOOo - OOOo0 * i1IIi / i11iIiiIii * i1I111II1I % OoOoOO00
 IIIIii ( '[COLORgreen]Stand Up[/COLOR]' , '' , 10014 , i1iIIi1 + 'ORIGINSTANDUP.png' , oooOOOOO , '' )
 IIIIii ( '[COLORgreen]Search Comedian[/COLOR]' , '' , 10015 , i1iIIi1 + 'ORIGINSTANDUP.png' , oooOOOOO , '' )
 IIIIii ( '[COLORgreen]Others[/COLOR]' , '' , 10017 , i1iIIi1 + 'ORIGINSTANDUP.png' , oooOOOOO , '' )
 if 56 - 56: OoooooooOO * Oo . Oo . ii11ii1ii
def II1Oo00O0Oo0Oo ( ) :
 iIIiIi1iIII1 = OooOOOOo ( ( oOOoo00O0O ( 'aHR0cDovL2JhY2syYmFzaWNzYnVpbGQuY28udWsvdGVzdC9zdGFuZHVwbGlzdC5waHA=' ) ) )
 oo0O0oO = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( iIIiIi1iIII1 )
 for oOo0 , OO0ooOOO0OOO , IiI111111IIII in oo0O0oO :
  if 'elete' in IiI111111IIII :
   pass
  else :
   ii1II ( '[COLORgreen]' + IiI111111IIII + '[/COLOR]' , oOo0 , 222 , OO0ooOOO0OOO )
   if 6 - 6: i1I111ii1II1i + OoOo00o + i1IIi * O0ooOooooO - i11iIiiIii
def ooOoO ( ) :
 IIiiIiII1Ii = i1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 iIIII11I1II = IIiiIiII1Ii . lower ( )
 iIIiIi1iIII1 = OooOOOOo ( ( oOOoo00O0O ( 'aHR0cDovL3d3dy5jb3VjaHRyaXBwZXIuY29tL2ZvcnVtMi9wYWdlLnBocD9wYWdlPTM=' ) ) )
 iIIIIiiIii = re . compile ( '<tr>.+?<td width=".+?" align=".+?">.+?<img border=".+?" src="..(.+?)" width=".+?" height=".+?"></td>.+?<td width=".+?" valign=".+?" align=".+?"><font size=".+?">(.+?)</font></td>.+?<td width=".+?">(.+?)</td>' , re . DOTALL ) . findall ( iIIiIi1iIII1 )
 for OO0ooOOO0OOO , ooO0oo , iIiiiI1IiI1I1 in iIIIIiiIii :
  for IIiiIiII1Ii in ooO0oo :
   print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< img >>>>>>>>>>>>>>>>>>>>>>>>>>'
   ooO0oo0o0 = re . compile ( '<a href="(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( iIiiiI1IiI1I1 )
   for oOo0 , IiI111111IIII in ooO0oo0o0 :
    if 'tube' in oOo0 :
     pass
    elif 'stage' in oOo0 :
     ii1II ( '[COLORgreen]' + ooO0oo + '   -   ' + IiI111111IIII + '[/COLOR]' , ( oOo0 ) . replace ( '" target="_blank' , '' ) , 10016 , 'http://couchtripper.com/' + OO0ooOOO0OOO , )
    elif 'vee' in oOo0 :
     pass
     if 9 - 9: OOOo0 + ii11ii1ii / OOOo0 . O0ooOooooO * OOO0OOo
def i1i1ii1111i1i ( ) :
 iIIiIi1iIII1 = OooOOOOo ( ( oOOoo00O0O ( 'aHR0cDovL3d3dy5jb3VjaHRyaXBwZXIuY29tL2ZvcnVtMi9wYWdlLnBocD9wYWdlPTM=' ) ) )
 iIIIIiiIii = re . compile ( '<tr>.+?<td width=".+?" align=".+?">.+?<img border=".+?" src="..(.+?)" width=".+?" height=".+?"></td>.+?<td width=".+?" valign=".+?" align=".+?"><font size=".+?">(.+?)</font></td>.+?<td width=".+?">(.+?)</td>' , re . DOTALL ) . findall ( iIIiIi1iIII1 )
 for OO0ooOOO0OOO , ooO0oo , iIiiiI1IiI1I1 in iIIIIiiIii :
  ooO0oo0o0 = re . compile ( '<a href="(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( iIiiiI1IiI1I1 )
  for oOo0 , IiI111111IIII in ooO0oo0o0 :
   if 'tube' in oOo0 :
    pass
   elif 'stage' in oOo0 :
    ii1II ( '[COLORgreen]' + ooO0oo + '   -   ' + IiI111111IIII + '[/COLOR]' , ( oOo0 ) . replace ( '" target="_blank' , '' ) , 10016 , 'http://couchtripper.com/' + OO0ooOOO0OOO )
   elif 'vee' in oOo0 :
    pass
    if 46 - 46: i1IIi
    if 54 - 54: OoOoOO00 - I1IiI
 xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 73 - 73: i1I111II1I
def Iiii1IiIi ( url ) :
 iIIiIi1iIII1 = OooOOOOo ( url )
 print '>>>>>>>>>>>>>>>>>>>>>>>>' + url + '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'
 IIIIiI11I11 = re . compile ( "url\[.+?\] = '(.+?)';" ) . findall ( iIIiIi1iIII1 )
 print '>>>>>>>>>>>>>>>>>>>>>>>' + ( str ( IIIIiI11I11 ) ) + '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
 for url in IIIIiI11I11 :
  OOoO ( ( url ) . replace ( '[' , '' ) . replace ( ']' , '' ) . replace ( '\'' , '' ) )
  if 39 - 39: i1I111II1I * OoOo00o
  if 2 - 2: i1IIi - OOO0OOo + OOOo0 . OOooOOo * OOooOOo / I1IiI
  if 93 - 93: i1IIi
  if 53 - 53: OoooooooOO + Oo + O0ooOooooO
  if 24 - 24: i1I111ii1II1i - OoOo00o - i1I111ii1II1i * ii11ii1ii . OoooooooOO / OoOo00o
  if 66 - 66: Oo
  if 97 - 97: i1IIi - OoooooooOO / o00OO00OoO * OOOo0
def oO0 ( ) :
 if 87 - 87: OOooOOo % iIii1I11I1II1
 O00 ( '[COLOR darkgoldenrod]Open Pandora\'s Box[/COLOR]' , '' , 10029 , 'https://encrypted-tbn1.gstatic.com/images?q=tbn%3AANd9GcTQ9r4TA8yIw9ggxuwsHxWojo6tPVfgTe8QIOxOQwzNR2TavtCi6Q' , oooOOOOO , '' )
 O00 ( '[COLOR darkgoldenrod]Search[/COLOR]' , '' , 10026 , 'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png' , oooOOOOO , '' )
 if 32 - 32: iIii1I11I1II1 * OoOo00o / iI % OoOo00o
 O00Oo000ooO0 ( 'movies' , 'MAIN' )
 if 42 - 42: o00OO00OoO + o00OO00OoO * OoOoOO00
def o0Oo ( ) :
 O00 ( 'Search Pandoras Films' , '' , 10027 , i1iIIi1 + 'PANDORASBOX.png' , oooOOOOO , '' )
 O00 ( 'Search Pandoras TV' , '' , 10028 , i1iIIi1 + 'PANDORASBOX.png' , oooOOOOO , '' )
 if 57 - 57: i1I111II1I / Oo
 O00Oo000ooO0 ( 'movies' , 'MAIN' )
def oO0O0Ooo ( ) :
 if 4 - 4: OoOoOO00 . Oooo0Ooo000 + iI * o00OO00OoO . OOO0OOo
 IIiiIiII1Ii = i1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 iIIII11I1II = IIiiIiII1Ii . lower ( )
 oOoOo = [ 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' ]
 if 74 - 74: O0ooOooooO / ii11ii1ii % OOooOOo
 for OO0o0OO0 in oOoOo :
  OooOo0OOO = IIIII + OO0o0OO0 + OooO0
  iIIiIi1iIII1 = OooOOOOo ( OooOo0OOO )
  oo0O0oO = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( iIIiIi1iIII1 )
  for oOo0 , OOO0000oO , OOoOO0ooo , iI1i111I1Ii , IiI111111IIII in oo0O0oO :
   if IIiiIiII1Ii in IiI111111IIII . lower ( ) :
    I1I ( IiI111111IIII , oOo0 , 222 , OOO0000oO , iI1i111I1Ii , OOoOO0ooo )
    if 73 - 73: iI
    O00Oo000ooO0 ( 'movies' , 'MAIN' )
    xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
    if 94 - 94: Ooo00oOo00o . OoooooooOO + Oooo0Ooo000 - I1IiI / OoOoOO00
    if 70 - 70: Oooo0Ooo000 % iIii1I11I1II1 . Oo + Oo - OOooOOo % o00OO00OoO
def i1IIi1i1Ii1 ( ) :
 if 45 - 45: iIii1I11I1II1 . O0ooOooooO / I1IiI / OoOo00o
 IIiiIiII1Ii = i1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 iIIII11I1II = IIiiIiII1Ii . lower ( )
 oOoOo = [ 'a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' , 'p' , 'q' , 'r' , 's' , 't' , 'u' , 'v' , 'w' , 'x' , 'y' , 'z' ]
 if 55 - 55: OoOo00o
 for OO0o0OO0 in oOoOo :
  IIiIiII = IIIII + OO0o0OO0 + OooO0
  iIIiIi1iIII1 = OooOOOOo ( IIiIiII )
  oo0O0oO = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( iIIiIi1iIII1 )
  for IiI111111IIII , OOoOO0ooo , oOo0 , OO0ooOOO0OOO , iI1i111I1Ii , Ooo00o0oOo0O0O in oo0O0oO :
   if IIiiIiII1Ii in IiI111111IIII . lower ( ) :
    O00 ( IiI111111IIII , oOo0 , Ooo00o0oOo0O0O , OO0ooOOO0OOO , iI1i111I1Ii , OOoOO0ooo )
    if 79 - 79: ii11ii1ii + o00OO00OoO
    O00Oo000ooO0 ( 'movies' , 'MAIN' )
    xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
    if 10 - 10: Oo + O0
    if 43 - 43: iIii1I11I1II1 / OoOoOO00 % OOooOOo - i1I111II1I
def oO0O000oOo ( ) :
 if 53 - 53: iIii1I11I1II1 + OOooOOo - I1IiI - O0ooOooooO / OOO0OOo % i11iIiiIii
 OO0oo = OooOOOOo ( oOOoo00O0O ( 'aHR0cDovL3NlZWR1cmdyZWVkLngxMGhvc3QuY29tL29yaWdpbi9zcG9uZ2VtYWluLnBocA==' ) )
 oo0O0oO = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( OO0oo )
 for IiI111111IIII , OOoOO0ooo , oOo0 , OO0ooOOO0OOO , iI1i111I1Ii , Ooo00o0oOo0O0O in oo0O0oO :
  O00 ( IiI111111IIII , oOo0 , Ooo00o0oOo0O0O , OO0ooOOO0OOO , iI1i111I1Ii , OOoOO0ooo )
  O00Oo000ooO0 ( 'movies' , 'MAIN' )
def I11oOOooo ( url ) :
 if 80 - 80: OOOo0 - i11iIiiIii
 xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
 oOoooO000O = ( '%s%s' % ( III1I11i1iIi , url ) )
 iiI1 = OooOOOOo ( url )
 oo0O0oO = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( iiI1 )
 for url , OOO0000oO , OOoOO0ooo , OO0oo0O0OOO0 , IiI111111IIII in oo0O0oO :
  I1I ( IiI111111IIII , url , 222 , OOO0000oO , OO0oo0O0OOO0 , OOoOO0ooo )
  if 76 - 76: i11iIiiIii / I1IiI + I1IiI / i1IIi * OOOo0
  O00Oo000ooO0 ( 'movies' , 'MAIN' )
  if 12 - 12: o00OO00OoO % i11iIiiIii + OOooOOo + o00OO00OoO / Oooo0Ooo000
  xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 53 - 53: OoOo00o . o00OO00OoO % iIii1I11I1II1 % I1IiI % Oooo0Ooo000
  if 53 - 53: o00OO00OoO
def OOo ( url ) :
 if 53 - 53: ii11ii1ii / OoOo00o / OoooooooOO / OoOoOO00
 OO0oo = OooOOOOo ( url )
 oo0O0oO = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( OO0oo )
 for IiI111111IIII , OOoOO0ooo , url , OO0ooOOO0OOO , iI1i111I1Ii , Ooo00o0oOo0O0O in oo0O0oO :
  O00 ( IiI111111IIII , url , Ooo00o0oOo0O0O , OO0ooOOO0OOO , iI1i111I1Ii , OOoOO0ooo )
  if 32 - 32: iIii1I11I1II1 . i11iIiiIii / O0ooOooooO
  O00Oo000ooO0 ( 'movies' , 'MAIN' )
  if 52 - 52: OOOo0 + iIii1I11I1II1
  if 71 - 71: O0 / O0ooOooooO
 xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 34 - 34: I1IiI . iIii1I11I1II1 % O0
def I1I ( name , url , mode , iconimage , fanart , description ) :
 if 43 - 43: ii11ii1ii - i1I111ii1II1i
 O000O = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 Oo00OO0 = True
 oo0O = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 oo0O . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 oo0O . setProperty ( "Fanart_Image" , fanart )
 Oo00OO0 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = O000O , listitem = oo0O , isFolder = False )
 return Oo00OO0
 if 92 - 92: i1I111II1I % OoOo00o % I1IiI
def O00 ( name , url , mode , iconimage , fanart , description ) :
 if 4 - 4: I1IiI + iI / O0ooOooooO
 O000O = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 Oo00OO0 = True
 oo0O = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 oo0O . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 oo0O . setProperty ( "Fanart_Image" , fanart )
 Oo00OO0 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = O000O , listitem = oo0O , isFolder = True )
 return Oo00OO0
if 13 - 13: i1I111ii1II1i
if 80 - 80: iI - OOooOOo
if 41 - 41: OOooOOo - Oo * OOOo0
if 82 - 82: Ooo00oOo00o % OOooOOo % i1I111II1I / O0
if 94 - 94: ii11ii1ii + ii11ii1ii + OoooooooOO % OOO0OOo
if 7 - 7: i1I111ii1II1i
if 78 - 78: i1I111II1I + i1I111ii1II1i . OoOo00o
if 91 - 91: iIii1I11I1II1 . OOooOOo . ii11ii1ii + OoooooooOO
if 69 - 69: o00OO00OoO - OOOo0
if 95 - 95: OOOo0 * i11iIiiIii . OOO0OOo
if 41 - 41: OoOoOO00
if 37 - 37: Oooo0Ooo000 . Oo % OoOo00o * i1IIi
if 71 - 71: Oo / OOooOOo + i1I111II1I
if 48 - 48: o00OO00OoO + i1I111ii1II1i
if 16 - 16: iIii1I11I1II1 % i11iIiiIii . I1IiI % OOO0OOo + O0ooOooooO . Ooo00oOo00o
def IIiIIIIiI ( string ) :
 if OOOO == 'true' :
  xbmc . log ( "[addon.live.GenieTV-%s]: %s" % ( addon_version , string ) )
  if 58 - 58: OOooOOo / OOooOOo + OOO0OOo + Oooo0Ooo000 - I1IiI . i1I111II1I
def I11Ii1iI11iI1 ( name , url , iconimage , fanart , mode , playlist = None , regexs = None ) :
 i1III1 = [ ]
 try :
  if 43 - 43: OoOoOO00 % o00OO00OoO . Oooo0Ooo000 % O0 - OoooooooOO + O0
  name = name . encode ( 'utf-8' , 'ignore' )
 except :
  pass
 if os . path . exists ( I11i1 ) == False :
  IIiIIIIiI ( 'Making Favorites File' )
  i1III1 . append ( ( name , url , iconimage , fanart , mode , playlist , regexs ) )
  iII1ii1 = open ( I11i1 , "w" )
  iII1ii1 . write ( json . dumps ( i1III1 ) )
  iII1ii1 . close ( )
 else :
  IIiIIIIiI ( 'Appending Favorites' )
  iII1ii1 = open ( I11i1 ) . read ( )
  OooO0ooo0 = json . loads ( iII1ii1 )
  OooO0ooo0 . append ( ( name , url , iconimage , fanart , mode ) )
  I1111I1II11 = open ( I11i1 , "w" )
  I1111I1II11 . write ( json . dumps ( OooO0ooo0 ) )
  I1111I1II11 . close ( )
  if 2 - 2: OoooooooOO
  if 60 - 60: Ooo00oOo00o
def oO00Ooo0oO ( ) :
 OOOo = json . loads ( open ( I11i1 ) . read ( ) )
 o0ooOo00O = len ( OOOo )
 for Ii1i1I1 in OOOo :
  IiI111111IIII = Ii1i1I1 [ 0 ]
  oOo0 = Ii1i1I1 [ 1 ]
  OOO0000oO = Ii1i1I1 [ 2 ]
  try :
   O0O00OooO = Ii1i1I1 [ 3 ]
   if O0O00OooO == None :
    raise
  except :
   if iiIIIII1i1iI . getSetting ( 'use_thumb' ) == "true" :
    O0O00OooO = OOO0000oO
   else :
    O0O00OooO = iI1i111I1Ii
  try : I1IiI1iI11 = Ii1i1I1 [ 5 ]
  except : I1IiI1iI11 = None
  try : iIi = Ii1i1I1 [ 6 ]
  except : iIi = None
  if 29 - 29: O0 . o00OO00OoO
  if Ii1i1I1 [ 4 ] == 0 :
   IIIIii ( IiI111111IIII , oOo0 , '' , OOO0000oO , iI1i111I1Ii , '' , 'fav' )
  else :
   IIIIii ( IiI111111IIII , oOo0 , Ii1i1I1 [ 4 ] , OOO0000oO , iI1i111I1Ii , '' , 'fav' )
   if 66 - 66: O0ooOooooO * iIii1I11I1II1 % iIii1I11I1II1 * OoOo00o - OOO0OOo - OoOo00o
def o0O0oO0 ( name ) :
 OooO0ooo0 = json . loads ( open ( I11i1 ) . read ( ) )
 for oo0 in range ( len ( OooO0ooo0 ) ) :
  if OooO0ooo0 [ oo0 ] [ 0 ] == name :
   del OooO0ooo0 [ oo0 ]
   I1111I1II11 = open ( I11i1 , "w" )
   I1111I1II11 . write ( json . dumps ( OooO0ooo0 ) )
   I1111I1II11 . close ( )
   break
 xbmc . executebuiltin ( "XBMC.Container.Refresh" )
 if 39 - 39: OOO0OOo . OoOoOO00
 if 45 - 45: O0ooOooooO * I1IiI / iIii1I11I1II1
def ooo00Ooo ( ) :
 o00ooOoO0 = os . path . join ( iIii1 , 'addons.ini' )
 IIi11II1II111 = open ( o00ooOoO0 , "w+" )
 if 55 - 55: OOO0OOo
 IIi11II1II111 . write ( r'# This file contains the "built-in" channels' + '\n' )
 IIi11II1II111 . write ( r'# It is parsed by Pythons ConfigParser' + '\n\n' )
 IIi11II1II111 . write ( r'[plugin.video.GenieTv]' + '\n' )
 IIi11II1II111 . write ( r'BBC One=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oOo0oooo00o + '%2F' + oO0o0o0ooO0oO + '%2F394.m3u8&mode=10012&name=[COLORgreen]BBC[/COLOR]' + '\n' )
 IIi11II1II111 . write ( r'BBC Two=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oOo0oooo00o + '%2F' + oO0o0o0ooO0oO + '%2F190.m3u8&mode=10012&name=[COLORgreen]BBC Two[/COLOR]' + '\n' )
 IIi11II1II111 . write ( r'BBC Four=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oOo0oooo00o + '%2F' + oO0o0o0ooO0oO + '%2F188.m3u8&mode=10012&name=[COLORgreen]BBC Four UK[/COLOR]' + '\n' )
 IIi11II1II111 . write ( r'ITV=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oOo0oooo00o + '%2F' + oO0o0o0ooO0oO + '%2F208.m3u8&mode=10012&name=[COLORgreen]ITV[/COLOR]' + '\n' )
 IIi11II1II111 . write ( r'ITV2=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oOo0oooo00o + '%2F' + oO0o0o0ooO0oO + '%2F207.m3u8&mode=10012&name=[COLORgreen]ITV2[/COLOR]' + '\n' )
 IIi11II1II111 . write ( r'ITV3=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oOo0oooo00o + '%2F' + oO0o0o0ooO0oO + '%2F206.m3u8&mode=10012&name=[COLORgreen]ITV3[/COLOR]' + '\n' )
 IIi11II1II111 . write ( r'ITV4=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oOo0oooo00o + '%2F' + oO0o0o0ooO0oO + '%2F205.m3u8&mode=10012&name=[COLORgreen]ITV4[/COLOR]' + '\n' )
 IIi11II1II111 . write ( r'Channel 4=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oOo0oooo00o + '%2F' + oO0o0o0ooO0oO + '%2F183.m3u8&mode=10012&name=[COLORgreen]Channel 4[/COLOR]' + '\n' )
 IIi11II1II111 . write ( r'Channel 5=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oOo0oooo00o + '%2F' + oO0o0o0ooO0oO + '%2F185.m3u8&mode=10012&name=[COLORgreen]Channel 5[/COLOR]' + '\n' )
 IIi11II1II111 . write ( r'Sky1=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oOo0oooo00o + '%2F' + oO0o0o0ooO0oO + '%2F32.m3u8&mode=10012&name=[COLORgreen]Sky1[/COLOR]' + '\n' )
 IIi11II1II111 . write ( r'Sky2=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oOo0oooo00o + '%2F' + oO0o0o0ooO0oO + '%2F33.m3u8&mode=10012&name=[COLORgreen]Sky2[/COLOR]' + '\n' )
 IIi11II1II111 . write ( r'Sky Atlantic=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oOo0oooo00o + '%2F' + oO0o0o0ooO0oO + '%2F34.m3u8&mode=10012&name=[COLORgreen]Sky Atlantic[/COLOR]' + '\n' )
 IIi11II1II111 . write ( r'Sky Living=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oOo0oooo00o + '%2F' + oO0o0o0ooO0oO + '%2F35.m3u8&mode=10012&name=[COLORgreen]Sky Living[/COLOR]' + '\n' )
 IIi11II1II111 . write ( r'5*=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oOo0oooo00o + '%2F' + oO0o0o0ooO0oO + '%2F187.m3u8&mode=10012&name=[COLORgreen]5*[/COLOR]' + '\n' )
 IIi11II1II111 . write ( r'5 USA=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oOo0oooo00o + '%2F' + oO0o0o0ooO0oO + '%2F186.m3u8&mode=10012&name=[COLORgreen]5 USA[/COLOR]' + '\n' )
 IIi11II1II111 . write ( r'Watch HD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oOo0oooo00o + '%2F' + oO0o0o0ooO0oO + '%2F408.m3u8&mode=10012&name=[COLORgreen]Watch HD[/COLOR]' + '\n' )
 IIi11II1II111 . write ( r'Pick=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oOo0oooo00o + '%2F' + oO0o0o0ooO0oO + '%2F410.m3u8&mode=10012&name=[COLORgreen]Pick[/COLOR]' + '\n' )
 IIi11II1II111 . write ( r'YESTERDAY=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oOo0oooo00o + '%2F' + oO0o0o0ooO0oO + '%2F411.m3u8&mode=10012&name=[COLORgreen]YESTERDAY/COLOR]' + '\n' )
 IIi11II1II111 . write ( r'Sky Showcase=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oOo0oooo00o + '%2F' + oO0o0o0ooO0oO + '%2F46.m3u8&mode=10012&name=[COLORgreen]Sky Showcase[/COLOR]' + '\n' )
 IIi11II1II111 . write ( r'Sky Disney=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oOo0oooo00o + '%2F' + oO0o0o0ooO0oO + '%2F195.m3u8&mode=10012&name=[COLORgreen]Sky Disney[/COLOR]' + '\n' )
 IIi11II1II111 . write ( r'Sky Family=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oOo0oooo00o + '%2F' + oO0o0o0ooO0oO + '%2F48.m3u8&mode=10012&name=[COLORgreen]Sky Family[/COLOR]' + '\n' )
 IIi11II1II111 . write ( r'Sky Action=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oOo0oooo00o + '%2F' + oO0o0o0ooO0oO + '%2F39.m3u8&mode=10012&name=[COLORgreen]Sky Action[/COLOR]' + '\n' )
 IIi11II1II111 . write ( r'Sky Comedy=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oOo0oooo00o + '%2F' + oO0o0o0ooO0oO + '%2F43.m3u8&mode=10012&name=[COLORgreen]Sky Comedy[/COLOR]' + '\n' )
 IIi11II1II111 . write ( r'Sky Thriller=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oOo0oooo00o + '%2F' + oO0o0o0ooO0oO + '%2F40.m3u8&mode=10012&name=[COLORgreen]Sky Thriller[/COLOR]' + '\n' )
 IIi11II1II111 . write ( r'Sky DramaRom=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oOo0oooo00o + '%2F' + oO0o0o0ooO0oO + '%2F47.m3u8&mode=10012&name=[COLORgreen]Sky DramaRom[/COLOR]' + '\n' )
 IIi11II1II111 . write ( r'Sky Select=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oOo0oooo00o + '%2F' + oO0o0o0ooO0oO + '%2F45.m3u8&mode=10012&name=[COLORgreen]Sky Select[/COLOR]' + '\n' )
 IIi11II1II111 . write ( r'SkyPremiereHD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oOo0oooo00o + '%2F' + oO0o0o0ooO0oO + '%2F37.m3u8&mode=10012&name=[COLORgreen]SkyPremiereHD[/COLOR]' + '\n' )
 IIi11II1II111 . write ( r'Eurosport=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oOo0oooo00o + '%2F' + oO0o0o0ooO0oO + '%2F69.m3u8&mode=10012&name=[COLORgreen]Eurosport[/COLOR]' + '\n' )
 IIi11II1II111 . write ( r'Sky Sports 1=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oOo0oooo00o + '%2F' + oO0o0o0ooO0oO + '%2F403.m3u8&mode=10012&name=[COLORgreen]Sky Sports 1[/COLOR]' + '\n' )
 IIi11II1II111 . write ( r'Sky Spts Ashes=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oOo0oooo00o + '%2F' + oO0o0o0ooO0oO + '%2F404.m3u8&mode=10012&name=[COLORgreen]Sky Spts Ashes[/COLOR]' + '\n' )
 IIi11II1II111 . write ( r'Sky Sports 3=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oOo0oooo00o + '%2F' + oO0o0o0ooO0oO + '%2F405.m3u8&mode=10012&name=[COLORgreen]Sky Sports 3[/COLOR]' + '\n' )
 IIi11II1II111 . write ( r'Sky Sports 4=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oOo0oooo00o + '%2F' + oO0o0o0ooO0oO + '%2F406.m3u8&mode=10012&name=[COLORgreen]Sky Sports 4[/COLOR]' + '\n' )
 IIi11II1II111 . write ( r'Sky Sports 5=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oOo0oooo00o + '%2F' + oO0o0o0ooO0oO + '%2F407.m3u8&mode=10012&name=[COLORgreen]Sky Sports 5[/COLOR]' + '\n' )
 IIi11II1II111 . write ( r'Sky Sports F1=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oOo0oooo00o + '%2F' + oO0o0o0ooO0oO + '%2F412.m3u8&mode=10012&name=[COLORgreen]Sky Sports F1[/COLOR]' + '\n' )
 IIi11II1II111 . write ( r'BT Sport 2=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oOo0oooo00o + '%2F' + oO0o0o0ooO0oO + '%2F413.m3u8&mode=10012&name=[COLORgreen]BT Sport 2[/COLOR]' + '\n' )
 IIi11II1II111 . write ( r'RDS=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oOo0oooo00o + '%2F' + oO0o0o0ooO0oO + '%2F414.m3u8&mode=10012&name=[COLORgreen]RDS[/COLOR]' + '\n' )
 IIi11II1II111 . write ( r'RTE One=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oOo0oooo00o + '%2F' + oO0o0o0ooO0oO + '%2F194.m3u8&mode=10012&name=[COLORgreen]RTE One[/COLOR]' + '\n' )
 IIi11II1II111 . write ( r'RTE Two=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fgenietv.iptv.re%3A8000%2Flive%2F' + oOo0oooo00o + '%2F' + oO0o0o0ooO0oO + '%2F193.m3u8&mode=10012&name=[COLORgreen]RTE Two[/COLOR]' + '\n' )
 if 82 - 82: o00OO00OoO - i1I111II1I + Ooo00oOo00o
 if 64 - 64: OOooOOo . O0 * iI + OoooooooOO - Oo . OoooooooOO
 if 70 - 70: Oo - O0ooOooooO . iIii1I11I1II1 % Oooo0Ooo000 / I1IiI - O0
def o0O0oo0o ( ) :
 if 12 - 12: I1IiI % OoOo00o % ii11ii1ii . i11iIiiIii * iIii1I11I1II1
 IIIIii ( '[COLORgreen]Recent Episodes[/COLOR]' , '' , 10019 , i1iIIi1 + 'dtv.png' , oooOOOOO , '' )
 IIIIii ( '[COLORgreen]Genres[/COLOR]' , '' , 10020 , i1iIIi1 + 'dtv.png' , oooOOOOO , '' )
 IIIIii ( '[COLORgreen]Search[/COLOR]' , '' , 10021 , i1iIIi1 + 'dtv.png' , oooOOOOO , '' )
 if 66 - 66: i11iIiiIii * iIii1I11I1II1 % OoooooooOO
def iIiI1iI1i1I ( ) :
 if 82 - 82: OOOo0 % ii11ii1ii * i1I111ii1II1i . iI % OOOo0 - iIii1I11I1II1
 OO0oo = cloudflare . source ( oOOoo00O0O ( 'aHR0cDovL2RpemlsYWIuY29t' ) )
 oo0O0oO = re . compile ( '<li id=".+?">.+?<a href="(.+?)">.+?<img width="40" height="40" src="(.+?)" alt=""/>.+?<span class="title">\n(.+?)</span>.+?<span class="alt-title">\n(.+?)</span>.+?</a>.+?</li>' , re . DOTALL ) . findall ( OO0oo )
 for oOo0 , OO0ooOOO0OOO , IiI111111IIII , i1Ii in oo0O0oO :
  IIIIii ( IiI111111IIII + '  -  ' + ( i1Ii ) . replace ( 'sezon' , 'Season' ) . replace ( 'bölüm' , 'Episode' ) , oOo0 , 10023 , i1iIIi1 + 'dtv.png' , oooOOOOO , '' )
  if 15 - 15: ii11ii1ii % o00OO00OoO + i11iIiiIii
  if 10 - 10: iI - I1IiI . OoooooooOO . i1I111II1I . Ooo00oOo00o * i1I111ii1II1i
  if 78 - 78: O0ooOooooO / Ooo00oOo00o - O0ooOooooO * OoooooooOO . I1IiI
def OOoooOoO0Oo ( ) :
 if 78 - 78: OoooooooOO / i1I111II1I % I1IiI * OoooooooOO
 IIIIii ( '[COLORgreen]Action[/COLOR]' , 'Aksiyon' , 10024 , i1iIIi1 + 'dtv.png' , oooOOOOO , '' )
 IIIIii ( '[COLORgreen]Adventure[/COLOR]' , 'Macera' , 10024 , i1iIIi1 + 'dtv.png' , oooOOOOO , '' )
 IIIIii ( '[COLORgreen]Animation[/COLOR]' , 'Animasyon' , 10024 , i1iIIi1 + 'dtv.png' , oooOOOOO , '' )
 IIIIii ( '[COLORgreen]Anime[/COLOR]' , 'Anime' , 10024 , i1iIIi1 + 'dtv.png' , oooOOOOO , '' )
 IIIIii ( '[COLORgreen]Biography[/COLOR]' , 'Biyografi' , 10024 , i1iIIi1 + 'dtv.png' , oooOOOOO , '' )
 IIIIii ( '[COLORgreen]Comedy[/COLOR]' , 'Komedi' , 10024 , i1iIIi1 + 'dtv.png' , oooOOOOO , '' )
 IIIIii ( '[COLORgreen]Crime[/COLOR]' , 'Su%C3%A7' , 10024 , i1iIIi1 + 'dtv.png' , oooOOOOO , '' )
 IIIIii ( '[COLORgreen]Documentary[/COLOR]' , 'Belgesel' , 10024 , i1iIIi1 + 'dtv.png' , oooOOOOO , '' )
 IIIIii ( '[COLORgreen]Drama[/COLOR]' , 'Dram' , 10024 , i1iIIi1 + 'dtv.png' , oooOOOOO , '' )
 IIIIii ( '[COLORgreen]Family[/COLOR]' , 'Aile' , 10024 , i1iIIi1 + 'dtv.png' , oooOOOOO , '' )
 IIIIii ( '[COLORgreen]Fantasy[/COLOR]' , 'Fantastik' , 10024 , i1iIIi1 + 'dtv.png' , oooOOOOO , '' )
 IIIIii ( '[COLORgreen]History[/COLOR]' , 'Tarih' , 10024 , i1iIIi1 + 'dtv.png' , oooOOOOO , '' )
 IIIIii ( '[COLORgreen]Horror[/COLOR]' , 'Korku' , 10024 , i1iIIi1 + 'dtv.png' , oooOOOOO , '' )
 IIIIii ( '[COLORgreen]Mini-Series[/COLOR]' , 'Mini%20Dizi' , 10024 , i1iIIi1 + 'dtv.png' , oooOOOOO , '' )
 IIIIii ( '[COLORgreen]Musical[/COLOR]' , 'M%C3%BCzikal' , 10024 , i1iIIi1 + 'dtv.png' , oooOOOOO , '' )
 IIIIii ( '[COLORgreen]Mystery[/COLOR]' , 'Gizem' , 10024 , i1iIIi1 + 'dtv.png' , oooOOOOO , '' )
 IIIIii ( '[COLORgreen]Romance[/COLOR]' , 'Romantik' , 10024 , i1iIIi1 + 'dtv.png' , oooOOOOO , '' )
 IIIIii ( '[COLORgreen]Science Fiction[/COLOR]' , 'Bilim%20Kurgu' , 10024 , i1iIIi1 + 'dtv.png' , oooOOOOO , '' )
 IIIIii ( '[COLORgreen]Sport[/COLOR]' , 'Spor' , 10024 , i1iIIi1 + 'dtv.png' , oooOOOOO , '' )
 IIIIii ( '[COLORgreen]Thriller[/COLOR]' , 'Gerilim' , 10024 , i1iIIi1 + 'dtv.png' , oooOOOOO , '' )
 IIIIii ( '[COLORgreen]War[/COLOR]' , 'Sava%C5%9F' , 10024 , i1iIIi1 + 'dtv.png' , oooOOOOO , '' )
 IIIIii ( '[COLORgreen]Western[/COLOR]' , 'Tarih' , 10024 , i1iIIi1 + 'dtv.png' , oooOOOOO , '' )
 IIIIii ( '[COLORgreen]Youth[/COLOR]' , 'Gen%C3%A7lik' , 10024 , i1iIIi1 + 'dtv.png' , oooOOOOO , '' )
 if 68 - 68: O0ooOooooO
def i11i11 ( url ) :
 oOo0O = 'http://dizilab.com/arsiv?limit=100&tur=' + url + '&orderby=&ulke=&order=&yil=&dizi_adi='
 iIIiIi1iIII1 = cloudflare . source ( oOo0O )
 oo0O0oO = re . compile ( '<div class="tv-series-single">.+?<a href="(.+?)" class="film-image">.+?<img src="(.+?)" alt=""/>.+?<span class="position">.+?</span>\n(.+?)</a>' , re . DOTALL ) . findall ( iIIiIi1iIII1 )
 for url , OO0ooOOO0OOO , IiI111111IIII in oo0O0oO :
  IIIIii ( '[COLORgreen]' + IiI111111IIII + '[/COLOR]' , url , 10022 , i1iIIi1 + 'dtv.png' , oooOOOOO , '' )
  if 18 - 18: iIii1I11I1II1 + Oooo0Ooo000 * OOOo0 - i1I111II1I / OOOo0
  if 78 - 78: Oooo0Ooo000 . OoOo00o
  if 38 - 38: I1IiI + OoOo00o
  if 15 - 15: Oo + Oooo0Ooo000 . OOO0OOo - iIii1I11I1II1 / O0 % iIii1I11I1II1
def oO0O ( ) :
 if 79 - 79: OoooooooOO - OoOo00o * OoOo00o . I1IiI
 IIiiIiII1Ii = i1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 iIIII11I1II = IIiiIiII1Ii . lower ( )
 oOo0 = ( oOOoo00O0O ( 'aHR0cDovL2RpemlsYWIuY29tL2Fyc2l2P2xpbWl0PSZ0dXI9Jm9yZGVyYnk9JnVsa2U9Jm9yZGVyPSZ5aWw9JmRpemlfYWRpPQ==' ) ) + ( IIiiIiII1Ii ) . replace ( ' ' , '+' )
 iIIiIi1iIII1 = cloudflare . source ( oOo0 )
 oo0O0oO = re . compile ( '<a href="(.+?)" class="film-image">\n<img src="(.+?)" alt=""/>\n</a>\n<div class="tss-detail">\n<a class="title" style="" href=".+?">\n<span class="position">.+?</span>\n(.+?)</a>' ) . findall ( iIIiIi1iIII1 )
 for oOo0 , OO0ooOOO0OOO , IiI111111IIII in oo0O0oO :
  if IIiiIiII1Ii in IiI111111IIII . lower ( ) :
   IIIIii ( '[COLORgreen]' + IiI111111IIII + '[/COLOR]' , oOo0 , 10022 , i1iIIi1 + 'dtv.png' )
   if 100 - 100: OoOoOO00 * Oooo0Ooo000 % OOOo0 / ii11ii1ii
   if 90 - 90: ii11ii1ii . OOO0OOo . I1IiI . iI
   if 4 - 4: iI + I1IiI % ii11ii1ii / i11iIiiIii
def OoOi111i ( url ) :
 iIIiIi1iIII1 = cloudflare . source ( url )
 oo0O0oO = re . compile ( '<a class="season" href="(.+?)">\n(.+?)\n</a>.+?<a class="episode" href=".+?">\n(.+?)\n</a>.+?<a class="episode-name" href=".+?">\n(.+?)</a>' , re . DOTALL ) . findall ( iIIiIi1iIII1 )
 for IIo0o0O0O00oOOo , II1III1i1iiI , I11i11i1 , IiI111111IIII in oo0O0oO :
  OOO = ( I11i11i1 ) . replace ( 'Sezon' , '' ) . replace ( 'bölüm' , '' ) . replace ( 'Bölüm' , '' ) . replace ( 'BÃ¶lÃ¼m' , '' ) . replace ( '.' , '' )
  ii1i1iiI = ( II1III1i1iiI ) . replace ( 'bölüm' , '' ) . replace ( 'Sezon' , '' ) . replace ( 'Bölüm' , '' ) . replace ( 'BÃ¶lÃ¼m' , '' ) . replace ( '.' , '' )
  Oo0oOo0ooOOOo = 'Season ' + ii1i1iiI + 'Episode ' + OOO + IiI111111IIII
  OoO0000o ( Oo0oOo0ooOOOo , IIo0o0O0O00oOOo )
  if 90 - 90: OoOo00o . OOO0OOo / iIii1I11I1II1
  xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 28 - 28: OoOo00o + O0ooOooooO - OOO0OOo / iIii1I11I1II1 - OOOo0
  if 45 - 45: O0 / i1IIi * O0ooOooooO * Ooo00oOo00o
def OoO0000o ( name , url ) :
 IIo0o0O0O00oOOo = url
 II11I = name
 o00o = cloudflare . source ( IIo0o0O0O00oOOo )
 IIIIiiIiiI = re . compile ( 'file: "(.+?)",.+?label: "(.+?)",' , re . DOTALL ) . findall ( o00o )
 for IIIIiI11I11 , iiiI11iIIi1 in IIIIiiIiiI :
  ii1II ( '[COLORgreen]' + II11I + iiiI11iIIi1 + '[/COLOR]' , IIIIiI11I11 , 10012 , i1iIIi1 + 'dtv.png' )
  if 72 - 72: i1I111ii1II1i * i1I111II1I
 xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 67 - 67: i1IIi
 if 5 - 5: OoOoOO00 . OoooooooOO
def oOOOo ( ) :
 if 31 - 31: I1IiI + I1IiI . i11iIiiIii / OOO0OOo % Oooo0Ooo000 / I1IiI
 if 29 - 29: ii11ii1ii * ii11ii1ii . Ooo00oOo00o * Oooo0Ooo000 % iIii1I11I1II1 * ii11ii1ii
 if 31 - 31: Ooo00oOo00o * O0 . O0ooOooooO
 if 59 - 59: OoOoOO00 * i11iIiiIii
 if 54 - 54: O0 % OoooooooOO - OOOo0
 if 61 - 61: Oo * OoOo00o . Oo + Oo / OoOo00o * O0
 if 73 - 73: i1I111ii1II1i * i1I111ii1II1i / OOO0OOo
 if 43 - 43: ii11ii1ii . i1IIi . OoOo00o + O0 * iI * O0
 if 41 - 41: ii11ii1ii + iI % OoooooooOO . ii11ii1ii + i1I111ii1II1i . i1I111ii1II1i
 if 31 - 31: i11iIiiIii + OoOoOO00 . i1I111ii1II1i * I1IiI
 if 66 - 66: I1IiI + i1IIi % OoOoOO00 . O0 * ii11ii1ii % ii11ii1ii
 if 87 - 87: i1I111II1I + OOooOOo . i1I111ii1II1i - OoooooooOO
 if 6 - 6: iIii1I11I1II1 * OoooooooOO
 if 28 - 28: Oo * OOooOOo / o00OO00OoO
 if 52 - 52: O0 / OOooOOo % i1I111ii1II1i * OOOo0 % i1I111II1I
 IIIIii ( '[COLORgreen]Newest Episodes Added[/COLOR]' , 'http://www.watchseries.li/latest' , 10046 , i1iIIi1 + 'WATCHSERIES.png' , '' , '' )
 IIIIii ( '[COLORgreen]This Week\'s Popular Episodes[/COLOR]' , 'http://www.watchseries.li/new' , 10042 , i1iIIi1 + 'WATCHSERIES.png' , '' , '' )
 IIIIii ( '[COLORgreen]Search Program[/COLOR]' , '' , 10043 , i1iIIi1 + 'WATCHSERIES.png' , '' , '' )
 if 69 - 69: ii11ii1ii
 if 83 - 83: OOooOOo
def i1iiii ( url ) :
 iIIiIi1iIII1 = OooOOOOo ( url )
 i1Iii1i1I = re . compile ( '<ul class="pagination" style="line-height: 3;">(.+?)</ul>' , re . DOTALL ) . findall ( iIIiIi1iIII1 )
 oo0O0oO = re . compile ( '<li><a href="/letters/(.+?)">(.+?)</a></li>' ) . findall ( str ( i1Iii1i1I ) )
 for url , IiI111111IIII in oo0O0oO :
  IIIIii ( '[COLORgreen]' + IiI111111IIII + '[/COLOR]' , 'http://watchseries.li/letters/' + url , 10049 , i1iIIi1 + 'WATCHSERIES.png' , '' , '' )
  if 90 - 90: OOooOOo % ii11ii1ii - iIii1I11I1II1 % I1IiI
def IIiI11I1I1i1i ( url ) :
 iIIiIi1iIII1 = OooOOOOo ( url )
 oo0O0oO = re . compile ( '<a href="(.+?)" class="sr-header">(.+?)</a>' ) . findall ( iIIiIi1iIII1 )
 for url , IiI111111IIII in oo0O0oO :
  IIIIii ( '[COLORgreen]' + IiI111111IIII + '[/COLOR]' , 'http://watchseries.li/' + url , 10049 , i1iIIi1 + 'WATCHSERIES.png' , '' , '' )
  if 86 - 86: i1IIi
def i1o0oo0Ooooo0 ( url ) :
 iIIiIi1iIII1 = OooOOOOo ( url )
 oo0O0oO = re . compile ( '<li class="col-md-6 col-xs-12 list-movies-li"><a href="(.+?)" title=".+?">(.+?)<span class="epnum">.+?</span></a></li>' , re . DOTALL ) . findall ( iIIiIi1iIII1 )
 IIIIiiIiiI = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="(.+?)">Next</a></li></ul>' , re . DOTALL ) . findall ( iIIiIi1iIII1 )
 for url , IiI111111IIII in oo0O0oO :
  IIIIii ( '[COLORgreen]' + ( IiI111111IIII ) . replace ( '&nbsp;' , ' ' ) . replace ( '&amp;' , '&' ) . replace ( '&#039;' , '\'' ) + '[/COLOR]' , 'http://www.watchseries.li' + url , 10044 , i1iIIi1 + 'WATCHSERIES.png' , '' , '' )
 for url in IIIIiiIiiI :
  IIIIii ( '[COLORgreen]' + 'NEXT' + '[/COLOR]' , 'http://www.watchseries.li' + url , 10049 , i1iIIi1 + 'Next.png' , '' , '' )
  if 76 - 76: i1IIi * OoooooooOO * O0 + o00OO00OoO * o00OO00OoO
  if 35 - 35: OOooOOo
def ooOoooo0 ( ) :
 IIiiIiII1Ii = i1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OoOoO0oOOooo = 'http://www.watchseries.li/search/' + IIiiIiII1Ii . replace ( ' ' , '%20' )
 iIIiIi1iIII1 = OooOOOOo ( OoOoO0oOOooo )
 oo0O0oO = re . compile ( '<img src="(.+?)".+?<a href="(.+?)" title=".+?"><b>(.+?)</b>' , re . DOTALL ) . findall ( iIIiIi1iIII1 )
 for OO0ooOOO0OOO , oOo0 , IiI111111IIII in oo0O0oO :
  if 'watch online' in IiI111111IIII :
   pass
  else :
   print oOo0
   IIIIii ( '[COLORgreen]' + IiI111111IIII + '[/COLOR]' , 'http://www.watchseries.li' + oOo0 , 10044 , OO0ooOOO0OOO , '' , '' )
   if 99 - 99: iIii1I11I1II1
   xbmcplugin . setContent ( O0O , 'movies' )
   if 14 - 14: ii11ii1ii % OOOo0 . OoOoOO00 . OOOo0 - OOO0OOo
def I1ii1 ( url ) :
 iIIiIi1iIII1 = OooOOOOo ( url )
 oo0O0oO = re . compile ( '<img src="(.+?)".+?<div class="block-left-home-inside-text">.+?<a href="(.+?)" title=".+?"><b>(.+?)</b> <br>.+?<span class=".+?">(.+?)</span></a><br>(.+?)<br>' , re . DOTALL ) . findall ( iIIiIi1iIII1 )
 for OO0ooOOO0OOO , url , IiI111111IIII , I11i11i1 , OOoOO0ooo in oo0O0oO :
  I1Ii = ( IiI111111IIII ) . replace ( '&nbsp;' , ' ' ) . replace ( '&amp;' , '&' ) . replace ( '&#039;' , '\'' ) + ' - ' + ( I11i11i1 ) . replace ( '&amp;' , '&' ) . replace ( '&#039;' , '\'' )
  IIIIii ( '[COLORgreen]' + I1Ii + '[/COLOR]' , 'http://www.watchseries.li' + url , 10045 , OO0ooOOO0OOO , '' , OOoOO0ooo )
  if 44 - 44: iIii1I11I1II1 . ii11ii1ii + o00OO00OoO . OOO0OOo
def II1i11 ( url ) :
 iIIiIi1iIII1 = OooOOOOo ( url )
 oo0O0oO = re . compile ( '<li class="col-md-6 col-xs-12 list-movies-li"><a href="(.+?)" title=".+?">(.+?)<span class="epnum">.+?</span></a></li>' , re . DOTALL ) . findall ( iIIiIi1iIII1 )
 IIIIiiIiiI = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="(.+?)">Next</a></li></ul>' , re . DOTALL ) . findall ( iIIiIi1iIII1 )
 for url , IiI111111IIII in oo0O0oO :
  I1Ii = ( IiI111111IIII ) . replace ( '&nbsp;' , ' ' ) . replace ( '&amp;' , '&' ) . replace ( '&#039;' , '\'' )
  IIIIii ( '[COLORgreen]' + I1Ii + '[/COLOR]' , 'http://www.watchseries.li' + url , 10045 , i1iIIi1 + 'WATCHSERIES.png' , '' , '' )
 for url in IIIIiiIiiI :
  IIIIii ( '[COLORgreen]' + 'NEXT' + '[/COLOR]' , 'http://www.watchseries.li' + url , 10046 , i1iIIi1 + 'Next.png' , '' , '' )
  if 28 - 28: OoOoOO00 - O0ooOooooO % I1IiI + Ooo00oOo00o - I1IiI
def IiI ( url ) :
 iIIiIi1iIII1 = OooOOOOo ( url )
 oo0O0oO = re . compile ( '<div class="mask">.+?<a href="(.+?)" title="(.+?)">.+?<img src="(.+?)"' , re . DOTALL ) . findall ( iIIiIi1iIII1 )
 IIIIiiIiiI = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="(.+?)">Next</a></li></ul>' , re . DOTALL ) . findall ( iIIiIi1iIII1 )
 for url , IiI111111IIII , OO0ooOOO0OOO in oo0O0oO :
  IIIIii ( '[COLORgreen]' + ( IiI111111IIII ) . replace ( '&nbsp;' , ' ' ) . replace ( '&amp;' , '&' ) . replace ( '&#039;' , '\'' ) + '[/COLOR]' , 'http://www.watchseries.li' + url , 10044 , OO0ooOOO0OOO , '' , '' )
 for url in IIIIiiIiiI :
  IIIIii ( '[COLORgreen]' + 'NEXT' + '[/COLOR]' , 'http://www.watchseries.li' + url , 10041 , i1iIIi1 + 'Next.png' , '' , '' )
  if 63 - 63: O0
def i1I1iIii11 ( url ) :
 iIIiIi1iIII1 = OooOOOOo ( url )
 i1Iii1i1I = re . compile ( '<div class="col-md-6 col-xs-12".+?<a href=".+?" itemprop="url"><span itemprop="name">(.+?)</span>(.+?)</ul>' , re . DOTALL ) . findall ( iIIiIi1iIII1 )
 for II1III1i1iiI , iIIIIiiIii in i1Iii1i1I :
  oo0O0oO = re . compile ( '<li itemprop="episode".+?<meta itemprop="url" content="(.+?)">.+?<span class="" itemprop="name">\n(.+?)\n' , re . DOTALL ) . findall ( str ( iIIIIiiIii ) )
  for url , IiI111111IIII in oo0O0oO :
   I1Ii = ( II1III1i1iiI ) . replace ( '  ' , '' ) + ' ' + ( IiI111111IIII ) . replace ( '&nbsp;' , ' ' ) . replace ( '&#039;' , '\'' ) . replace ( '  ' , '' )
   IIIIii ( '[COLORgreen]' + I1Ii + '[/COLOR]' , 'http://www.watchseries.li' + url , 10045 , i1iIIi1 + 'WATCHSERIES.png' , '' , '' )
 IIIIiiIiiI = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="(.+?)">Next</a></li></ul>' , re . DOTALL ) . findall ( iIIiIi1iIII1 )
 for url in IIIIiiIiiI :
  IIIIii ( '[COLORgreen]' + 'NEXT' + '[/COLOR]' , 'http://www.watchseries.li' + url , 10044 , i1iIIi1 + 'Next.png' , '' , '' )
  if 80 - 80: I1IiI - OoOoOO00
  if 35 - 35: OOO0OOo - Ooo00oOo00o . Oo * Oo / i11iIiiIii + ii11ii1ii
class oOo0Oo0O0O ( ) :
 if 48 - 48: Oo - OOO0OOo + Oo - OOOo0 * i11iIiiIii . i1I111ii1II1i
 List = [ ]
 source_list = [ ]
 def __init__ ( self , name ) :
  if 35 - 35: OoOo00o . O0 + Oo + i1I111II1I + i1IIi
  I1Ii = name
  self . Get_Sources ( oOo0 , I1Ii )
  if 65 - 65: O0 * OOOo0 / OOOo0 . I1IiI
  if 87 - 87: OoOoOO00 * ii11ii1ii % Oo * Oo
 def Get_Sources ( self , URL , season_name ) :
  o00 = xbmcgui . DialogProgress ( )
  iIIiIi1iIII1 = OooOOOOo ( URL )
  oo0O0oO = re . compile ( '<td>.+?<a href="/link/(.+?)".+?height="16px">(.+?)\n' , re . DOTALL ) . findall ( iIIiIi1iIII1 )
  for oOo0 , IiI111111IIII in oo0O0oO :
   URL = 'http://www.watchseries.li/link/' + oOo0
   self . Get_site_link ( URL , season_name )
   if 58 - 58: i1I111II1I . OOooOOo + OOOo0 % Oo - Ooo00oOo00o
 def Get_site_link ( self , url , season_name ) :
  iIIiIi1iIII1 = OooOOOOo ( url )
  oo0O0oO = re . compile ( '<iframe style=.+?" src="(.+?)"' ) . findall ( iIIiIi1iIII1 )
  IIIIiiIiiI = re . compile ( '<IFRAME SRC="(.+?)"' ) . findall ( iIIiIi1iIII1 )
  oO0o = re . compile ( '<IFRAME style=".+?" SRC="(.+?)"' ) . findall ( iIIiIi1iIII1 )
  for url in oo0O0oO :
   self . main ( url , season_name )
  for url in IIIIiiIiiI :
   self . main ( url , season_name )
  for url in oO0o :
   self . main ( url , season_name )
   if 50 - 50: i1I111ii1II1i % OoOoOO00 - OOO0OOo . i1IIi + O0 % i1I111ii1II1i
 def main ( self , url , season_name ) :
  o00 . create ( "[COLORwhite]Origin[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
  if 'daclips.in' in url :
   i1iIi1IIiIII1 = 'DACLIPS'
   if i1iIi1IIiIII1 in oOo0Oo0O0O . source_list :
    pass
   else :
    self . daclips ( url , season_name , i1iIi1IIiIII1 )
    o00 . update ( 0 , "" , "Getting Daclips Links" )
  else :
   if 'filehoot.com' in url :
    i1iIi1IIiIII1 = 'FILEHOOT'
    if i1iIi1IIiIII1 in oOo0Oo0O0O . source_list :
     pass
    else :
     o00 . update ( 0 , "" , "Getting Filehoot Links" )
     self . filehoot ( url , season_name , i1iIi1IIiIII1 )
   else :
    if 'thevideo.me' in url :
     i1iIi1IIiIII1 = 'THEVIDEO'
     if i1iIi1IIiIII1 in oOo0Oo0O0O . source_list :
      pass
     else :
      self . thevideo ( url , season_name , i1iIi1IIiIII1 )
      o00 . update ( 0 , "" , "Getting Thevideo Links" )
    else :
     if 'allmyvideos.net' in url :
      i1iIi1IIiIII1 = 'ALLMYVIDEOS'
      if i1iIi1IIiIII1 in oOo0Oo0O0O . source_list :
       pass
      else :
       self . allmyvid ( url , season_name , i1iIi1IIiIII1 )
       o00 . update ( 0 , "" , "Getting Allmyvideo Links" )
     else :
      if 'vidspot.net' in url :
       i1iIi1IIiIII1 = 'VIDSPOT'
       if i1iIi1IIiIII1 in oOo0Oo0O0O . source_list :
        pass
       else :
        self . vidspot ( url , season_name , i1iIi1IIiIII1 )
        o00 . update ( 0 , "" , "Getting Vidspot Links" )
      else :
       if 'vodlocker' in url :
        i1iIi1IIiIII1 = 'VODLOCKER'
        if i1iIi1IIiIII1 in oOo0Oo0O0O . source_list :
         pass
        else :
         self . vodlocker ( url , season_name , i1iIi1IIiIII1 )
         o00 . update ( 0 , "" , "Getting Vodlocker Links" )
         if 19 - 19: Oooo0Ooo000
         if 87 - 87: OOO0OOo / I1IiI % OOooOOo * O0ooOooooO
 def allmyvid ( self , url , season_name , source_name ) :
  iIIiIi1iIII1 = OooOOOOo ( url )
  oo0O0oO = re . compile ( '"file" : "(.+?)",\n.+?"default" : .+?,\n.+?"label" : "(.+?)"' , re . DOTALL ) . findall ( iIIiIi1iIII1 )
  for oOOOoo0o , IiI111111IIII in oo0O0oO :
   self . Printer ( oOOOoo0o , season_name , source_name )
   if 44 - 44: O0 % i1IIi
 def vidspot ( self , url , season_name , source_name ) :
  iIIiIi1iIII1 = OooOOOOo ( url )
  oo0O0oO = re . compile ( '"file" : "(.+?)",\n.+?"default" : .+?,\n.+?"label" : "(.+?)"' ) . findall ( iIIiIi1iIII1 )
  for oOOOoo0o , IiI111111IIII in oo0O0oO :
   self . Printer ( oOOOoo0o , season_name , source_name )
   if 42 - 42: OoOoOO00 - Ooo00oOo00o - OoooooooOO . i1I111ii1II1i / I1IiI
 def thevideo ( self , url , season_name , source_name ) :
  iIIiIi1iIII1 = OooOOOOo ( url )
  oo0O0oO = re . compile ( "{ label: '.+?', file: '(.+?)' }" ) . findall ( iIIiIi1iIII1 )
  for oOOOoo0o in oo0O0oO :
   self . Printer ( oOOOoo0o , season_name , source_name )
   if 56 - 56: i11iIiiIii - iIii1I11I1II1 . OoOoOO00
 def vodlocker ( self , url , season_name , source_name ) :
  iIIiIi1iIII1 = OooOOOOo ( url )
  oo0O0oO = re . compile ( 'file: "(.+?)",.+?skin' , re . DOTALL ) . findall ( iIIiIi1iIII1 )
  for oOOOoo0o in oo0O0oO :
   self . Printer ( oOOOoo0o , season_name , source_name )
   if 81 - 81: OoOo00o / I1IiI * OoOo00o . O0
 def daclips ( self , url , season_name , source_name ) :
  iIIiIi1iIII1 = OooOOOOo ( url )
  oo0O0oO = re . compile ( '{ file: "(.+?)", type:"video" }' ) . findall ( iIIiIi1iIII1 )
  for oOOOoo0o in oo0O0oO :
   self . Printer ( oOOOoo0o , season_name , source_name )
   if 61 - 61: Ooo00oOo00o * i1I111II1I + o00OO00OoO . iIii1I11I1II1 % Oooo0Ooo000 . o00OO00OoO
 def filehoot ( self , url , season_name , source_name ) :
  iIIiIi1iIII1 = OooOOOOo ( url )
  oo0O0oO = re . compile ( 'file: "(.+?)",.+?skin' , re . DOTALL ) . findall ( iIIiIi1iIII1 )
  for oOOOoo0o in oo0O0oO :
   self . Printer ( oOOOoo0o , season_name , source_name )
   if 53 - 53: o00OO00OoO * OoOo00o / iIii1I11I1II1 / OOOo0 % ii11ii1ii
 def Printer ( self , Link , season_name , source_name ) :
  if 39 - 39: Ooo00oOo00o / OoooooooOO . Ooo00oOo00o * ii11ii1ii / I1IiI
  if Link in oOo0Oo0O0O . List :
   pass
  elif source_name in oOo0Oo0O0O . source_list :
   pass
  else :
   ii1II ( '[COLORgreen]' + source_name + '[/COLOR]' , Link , 10012 , i1iIIi1 + 'WATCHSERIES.png' )
   o00 . update ( 100 , "" , "Got Source" )
   oOo0Oo0O0O . List . append ( Link )
   oOo0Oo0O0O . source_list . append ( source_name )
   if 38 - 38: Ooo00oOo00o / OOO0OOo % o00OO00OoO * Oooo0Ooo000 + i11iIiiIii % OOO0OOo
   xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
   if 61 - 61: o00OO00OoO - iI % ii11ii1ii / OOO0OOo / i1I111ii1II1i + iIii1I11I1II1
   if 87 - 87: o00OO00OoO + OOO0OOo + O0 / i1IIi % OoOo00o / o00OO00OoO
   if 64 - 64: Ooo00oOo00o % OoOo00o . o00OO00OoO % Ooo00oOo00o + Oooo0Ooo000 * OoOo00o
   if 83 - 83: OOooOOo % O0ooOooooO + Oooo0Ooo000 % i11iIiiIii + O0
   if 65 - 65: iIii1I11I1II1 % O0ooOooooO + O0 / OoooooooOO
def O0000oO0o00 ( ) :
 IIIIii ( '[COLORgreen]Highlights[/COLOR]' , '' , 10008 , i1iIIi1 + 'ORIGINFOOTBALL.png' , oooOOOOO , '' )
 IIIIii ( '[COLORgreen]Fixtures[/COLOR]' , '' , 10009 , i1iIIi1 + 'ORIGINFOOTBALL.png' , oooOOOOO , '' )
 if 80 - 80: OoooooooOO + OoOo00o
def O00O ( ) :
 OO0oo = OooOOOOo ( oOOoo00O0O ( 'aHR0cDovL2xpdmVvbnNhdC5jb20vcXVpY2tpbmRleC5odG1s' ) )
 oo0O0oO = re . compile ( '<a target="_self" href="(.+?)".+?src="(.+?)" alt="(.+?)"' , re . DOTALL ) . findall ( OO0oo )
 for oOo0 , OO0ooOOO0OOO , IiI111111IIII in oo0O0oO :
  IIIIii ( '[COLORgreen]' + ( IiI111111IIII ) . replace ( 'amp;' , '' ) + '[/COLOR]' , oOOoo00O0O ( 'aHR0cDovL2xpdmVvbnNhdC5jb20v' ) + oOo0 , 10010 , oOOoo00O0O ( 'aHR0cDovL2xpdmVvbnNhdC5jb20v' ) + OO0ooOOO0OOO , oooOOOOO , '' )
  if 63 - 63: OoooooooOO * OoooooooOO % Ooo00oOo00o + O0 / o00OO00OoO + iIii1I11I1II1
def oO0o0o00oOo0O ( url ) :
 iIIiIi1iIII1 = OooOOOOo ( url )
 i1Iii1i1I = re . compile ( 'AndClearL.+?><h2.+?head>(.*?)float' , re . DOTALL ) . findall ( iIIiIi1iIII1 )
 for i1Iii1i1I in i1Iii1i1I :
  oOOoooO0O0 = re . compile ( '(.*?)</h2>' ) . findall ( str ( i1Iii1i1I ) )
  for ii1O0ooooo000 in oOOoooO0O0 :
   ii1O0ooooo000 = ii1O0ooooo000
  OooOoOO0OO = re . compile ( 'comp_head>(.*?)</span>.*?<div class = fLeft width = ".*?"><img src="(.*?)">.*?</div>.*?ST:(.*?)</div>(.+?)<!-- around all of channel types ENDS 2-->' , re . DOTALL ) . findall ( str ( i1Iii1i1I ) )
  for I1iiIiiii1111 , OO0ooOOO0OOO , time , I1ii1i11i in OooOoOO0OO :
   I11IIIi = re . compile ( ",CAPTION, '(.+?)&nbsp" ) . findall ( I1ii1i11i )
   IIIIii ( '[COLORgreen]' + ii1O0ooooo000 + ' - ' + I1iiIiiii1111 + ' - ' + time + '[/COLOR]' , '' , 10010 , oOOoo00O0O ( 'aHR0cDovL2xpdmVvbnNhdC5jb20=' ) + OO0ooOOO0OOO , oooOOOOO , ( str ( I11IIIi ) ) )
   if 86 - 86: O0 % i1IIi . OoOoOO00 . Oooo0Ooo000
 O00Oo000ooO0 ( 'tvshows' , 'Media Info 3' )
 if 44 - 44: i11iIiiIii * Oooo0Ooo000 + I1IiI + OoOo00o * O0 . OoOo00o
def ii1II1II ( ) :
 if 42 - 42: iI
 IIIIii ( '[COLORgreen]Shows[/COLOR]' , 'http://www.fullmatchesandshows.com/category/show/' , 10011 , 'http://www.fm-base.co.uk/forum/attachments/club-competition-logos/3885-soccer-am-logo-socceram.png' , i1iIIi1 + 'fanart.jpg' , '' )
 IIIIii ( '[COLORgreen]Premier League[/COLOR]' , 'http://www.fullmatchesandshows.com/premier-league/' , 10011 , 'https://footballseasons.files.wordpress.com/2013/05/premier-league.png' , i1iIIi1 + 'fanart.jpg' , '' )
 IIIIii ( '[COLORgreen]La Liga[/COLOR]' , 'http://www.fullmatchesandshows.com/la-liga/' , 10011 , 'http://1.bp.blogspot.com/-c6kQ40ryhyo/U19cUlz25sI/AAAAAAAABak/qtn5chSFZm0/s1600/la-liga-logo_display_image.png' , i1iIIi1 + 'fanart.jpg' , '' )
 IIIIii ( '[COLORgreen]Bundesliga[/COLOR]' , 'http://www.fullmatchesandshows.com/bundesliga/' , 10011 , 'http://m.img.brothersoft.com/iphone/189/518670189_icon175x175.jpg' , i1iIIi1 + 'fanart.jpg' , '' )
 IIIIii ( '[COLORgreen]Champions League[/COLOR]' , 'http://www.fullmatchesandshows.com/champions-league/' , 10011 , 'http://www.ecursuri.ro/images/teste/test-champions-league.jpg' , i1iIIi1 + 'fanart.jpg' , '' )
 IIIIii ( '[COLORgreen]Serie A[/COLOR]' , 'http://www.fullmatchesandshows.com/category/serie-a/' , 10011 , 'http://files.jcriccione.it/200000223-2484526782/serie%20a.png' , i1iIIi1 + 'fanart.jpg' , '' )
 IIIIii ( '[COLORgreen]Ligue 1[/COLOR]' , 'http://www.fullmatchesandshows.com/category/ligue-1/' , 10011 , 'http://a1.mzstatic.com/us/r30/Purple5/v4/37/c7/44/37c744ae-5824-42b7-6ce0-5f471f52baab/icon180x180.jpeg' , i1iIIi1 + 'fanart.jpg' , '' )
 IIIIii ( '[COLORgreen]Copa America 2015[/COLOR]' , 'http://www.fullmatchesandshows.com/copa-america-2015/' , 10011 , 'https://pbs.twimg.com/profile_images/521966985907691520/Nq9OAPIo_400x400.png' , i1iIIi1 + 'fanart.jpg' , '' )
 IIIIii ( '[COLORgreen]CONCACAF[/COLOR]' , 'http://www.fullmatchesandshows.com/category/concacaf/' , 10011 , 'http://a3.mzstatic.com/us/r30/Purple3/v4/40/26/14/4026147c-7022-4ca3-504e-e78950cc3f1c/icon175x175.png' , i1iIIi1 + 'fanart.jpg' , '' )
 IIIIii ( '[COLORgreen]Women World Cup[/COLOR]' , 'http://www.fullmatchesandshows.com/category/women-world-cup/' , 10011 , 'https://upload.wikimedia.org/wikipedia/en/thumb/7/76/2015_FIFA_Women\'s_World_Cup_logo.svg/967px-2015_FIFA_Women\'s_World_Cup_logo.svg.png' , i1iIIi1 + 'fanart.jpg' , '' )
 if 68 - 68: i1I111II1I . Oo % OOO0OOo - OoooooooOO * i1I111ii1II1i . i1I111II1I
def Ii1I1i111 ( url ) :
 iIIiIi1iIII1 = OooOOOOo ( url )
 oo0O0oO = re . compile ( 'itemprop="image" class="entry-thumb" src="(.+?)".+?<h3 itemprop="name" class="entry-title td-module-title"><a itemprop="url" href="(.+?)" rel="bookmark" title=".+?">(.+?)</a></h3>' , re . DOTALL ) . findall ( iIIiIi1iIII1 )
 for OO0ooOOO0OOO , url , IiI111111IIII in oo0O0oO :
  oOi1 = IiI111111IIII . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' )
  ii1II ( '[COLORgreen]' + oOi1 + '[/COLOR]' , url , 10013 , OO0ooOOO0OOO )
  if 39 - 39: OOO0OOo / O0 * OoOo00o
def I1IiII1iI1 ( url ) :
 iIIiIi1iIII1 = OooOOOOo ( url )
 oo0O0oO = re . compile ( '<script data-config="(.+?)" data-height' ) . findall ( iIIiIi1iIII1 )
 for IIIIiI11I11 in oo0O0oO :
  oOOO00OOOoOO = ( IIIIiI11I11 ) . replace ( '/v2' , '' ) . replace ( 'zeus.json' , 'video-sd.mp4?hosting_id=21772' ) . replace ( 'config.playwire.com' , 'cdn.video.playwire.com' )
  OOoO ( 'http:' + oOOO00OOOoOO )
  if 23 - 23: I1IiI . OOooOOo - Ooo00oOo00o / I1IiI * iIii1I11I1II1
  if 13 - 13: OOooOOo * i11iIiiIii / i11iIiiIii . Ooo00oOo00o . i1I111II1I . ii11ii1ii
def iIIiIi ( url ) :
 OO0oo = Iii1 ( url )
 oo0O0oO = re . compile ( '<a href="([^"]*)" title="([^"]*)"><img itemprop="image" content="([^"]*)"' , re . DOTALL ) . findall ( OO0oo )
 IIIIiiIiiI = re . compile ( "<a rel='next' href=([^=]*)=" , re . DOTALL ) . findall ( OO0oo )
 for url , IiI111111IIII , OO0ooOOO0OOO in oo0O0oO :
  ii1II ( IiI111111IIII , url , 8046 , OO0ooOOO0OOO )
 for url in IIIIiiIiiI :
  Oo00oo0000OO ( 'NEXT PAGE' , ( url ) . replace ( ' class' , '' ) , 8045 , i1iIIi1 + 'Next.png' )
def oO0Oo00oo ( url ) :
 OO0oo = Iii1 ( url )
 oo0O0oO = re . compile ( "__filename='([^']*)',.+?__fullimage='([^']*)',.+?__title='([^']*)'," , re . DOTALL ) . findall ( OO0oo )
 for url , OO0ooOOO0OOO , IiI111111IIII in oo0O0oO :
  OOoO ( 'http://bitcast-b.bitgravity.com/ndtvod/23372/ndtv/' + url )
  if 75 - 75: iIii1I11I1II1 * i11iIiiIii - OoooooooOO . I1IiI
def OOOO0O00Ooooo ( url ) :
 OO0oo = Iii1 ( url )
 oo0O0oO = re . compile ( "src='http://www.youtube.com/embed/(.+?)?version=3&#038;rel=1&#038;fs=1&#038;autohide=2&#038;showsearch=0&#038;showinfo=1&#038;iv_load_policy=1&#038;wmode=transparent' frameborder='0' allowfullscreen='true'></iframe>" ) . findall ( OO0oo )
 for url in oo0O0oO :
  yt . PlayVideo ( url )
  if 2 - 2: i1IIi * O0ooOooooO - O0ooOooooO + OoooooooOO % I1IiI / I1IiI
def i11IiI1iiI11 ( ) :
 OO0oo = Iii1 ( oOOoo00O0O ( 'aHR0cDovL3RvcGRvY3VtZW50YXJ5ZmlsbXMuY29tLw==' ) )
 oo0O0oO = re . compile ( '<a href="(.+?)" >(.+?)</a></li><li>' ) . findall ( OO0oo )
 for oOo0 , IiI111111IIII in oo0O0oO :
  Oo00oo0000OO ( IiI111111IIII , oOo0 , 8041 , i1iIIi1 + 'documentary.png' )
def OOoOOOO00 ( url ) :
 OO0oo = Iii1 ( url )
 oo0O0oO = re . compile ( '<h2><a href="(.+?)" title="(.+?)">.+?</a></h2>.+?src="(.+?)"' , re . DOTALL ) . findall ( OO0oo )
 IIIIiiIiiI = re . compile ( 'class="inactive">.+?</a><a href="(.+?)">Next</a></div>' , re . DOTALL ) . findall ( OO0oo )
 for url , IiI111111IIII , OO0ooOOO0OOO in oo0O0oO :
  Oo00oo0000OO ( ( IiI111111IIII ) . replace ( '&#039;s' , '' ) , url , 8042 , OO0ooOOO0OOO )
 for url in IIIIiiIiiI :
  Oo00oo0000OO ( 'NEXT PAGE' , url , 8041 , i1iIIi1 + 'Next.png' )
  if 49 - 49: Ooo00oOo00o - O0 / Ooo00oOo00o * I1IiI + o00OO00OoO
  if 35 - 35: OoOoOO00 . OOOo0 / i1IIi / OOOo0 * O0ooOooooO
def Oo0O0000Oo00o ( url ) :
 OO0oo = Iii1 ( url )
 oo0O0oO = re . compile ( '<meta itemprop="name" content="(.+?)".+?<meta itemprop="thumbnailUrl" content="(.+?)".+?<meta itemprop="embedUrl" content="(.+?)".+?<meta itemprop="description" content="(.+?)" />' , re . DOTALL ) . findall ( OO0oo )
 IIIIiiIiiI = re . compile ( '<div class="video new-video"><iframe width="766" height="431" src="(.+?)&amp;iv_load_policy=3&amp;showinfo=0&amp;autohide=1"' , re . DOTALL ) . findall ( OO0oo )
 for IiI111111IIII , OO0ooOOO0OOO , url , I1i in oo0O0oO :
  ii1II ( ( IiI111111IIII ) . replace ( '&#039;s' , '' ) , url . replace ( 'https://www.youtube.com/embed/' , '' ) , 8043 , OO0ooOOO0OOO )
 for url in IIIIiiIiiI :
  II1ii ( ( url ) . replace ( '//' , 'http://' ) )
  if 89 - 89: i1I111ii1II1i . i11iIiiIii * O0
def II1ii ( url ) :
 OO0oo = Iii1 ( url )
 oo0O0oO = re . compile ( '<link rel="canonical" href="(.+?)">  <link rel="stylesheet"' ) . findall ( OO0oo )
 for url in oo0O0oO :
  ii1II ( 'PLAY' , ( url ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , i1iIIi1 + 'documentary.png' )
  if 44 - 44: i1IIi . OOOo0 / i11iIiiIii + OoOo00o
def iI111II1ii ( ) :
 iIIiIi1iIII1 = Iii1 ( 'http://www.stream2watch.co/live-tv' )
 oo0O0oO = re . compile ( '<a href="(.+?)">.+?<img src="(.+?)" alt=".+?"/>.+?<span class="country_name">(.+?)<br />(.+?)</span>' , re . DOTALL ) . findall ( iIIiIi1iIII1 )
 for oOo0 , OO0ooOOO0OOO , IiI111111IIII , O0ooO00ooOO0o in oo0O0oO :
  Oo00oo0000OO ( ( IiI111111IIII + '[COLORgreen]' + O0ooO00ooOO0o + '[/COLOR]' ) , oOo0 , 8086 , OO0ooOOO0OOO )
  if 65 - 65: i1I111ii1II1i . Ooo00oOo00o + iI
def IIiI1I ( url ) :
 iIIiIi1iIII1 = Iii1 ( url )
 oo0O0oO = re . compile ( '<a class="front_channel_href" href="(.+?)" title=".+?">.+?<img class="front_channel_thumb" src="(.+?)" alt=".+?"/>.+?<span class="front_channel_name">(.+?)</span>' , re . DOTALL ) . findall ( iIIiIi1iIII1 )
 for url , OO0ooOOO0OOO , IiI111111IIII in oo0O0oO :
  Oo00oo0000OO ( '[COLORgreen]' + IiI111111IIII + '[/COLOR]' , url , 8087 , OO0ooOOO0OOO )
  if 67 - 67: iI
def iIII11Iiii1 ( url ) :
 iIIiIi1iIII1 = OooOOOOo ( url )
 oo0O0oO = re . compile ( 'a id="code_.+?data-f-href="(.+?)" data-code-embed="">(.+?)</a>' , re . DOTALL ) . findall ( iIIiIi1iIII1 )
 for url , IiI111111IIII in oo0O0oO :
  o0oo0 ( url , IiI111111IIII )
  if 67 - 67: O0 * Oooo0Ooo000 - OOooOOo - OoOoOO00
def o0oo0 ( url , name ) :
 iIIiIi1iIII1 = OooOOOOo ( url )
 oo0O0oO = re . compile ( "playStream\('.+?', '(.+?)'\);" , re . DOTALL ) . findall ( iIIiIi1iIII1 )
 for url in oo0O0oO :
  print url
  ii1II ( '[COLORgreen]' + name + '[/COLOR]' , url , 222 , '' )
  if 41 - 41: OOOo0 - o00OO00OoO % OoOoOO00 . o00OO00OoO - Oooo0Ooo000
def i1I111Ii ( ) :
 OO0oo = Iii1 ( oOOoo00O0O ( 'aHR0cDovL3d3dy5zb2xpZS5vcmcvYWxpYnJhcnkvaW5kZXguaHRtbA==' ) )
 oo0O0oO = re . compile ( '<td align="center" valign="top">.+?<a href="(.+?)">.+?<img src="(.+?)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( OO0oo )
 for oOo0 , OO0ooOOO0OOO , IiI111111IIII in oo0O0oO :
  Oo00oo0000OO ( ( '[COLORgreen]' + IiI111111IIII + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + oOo0 , 3002 , 'http://www.solie.org/alibrary/' + OO0ooOOO0OOO )
def i11i1i ( url ) :
 OO0oo = Iii1 ( url )
 oo0O0oO = re . compile ( '<td align="center" valign="top">.+?<a href="(.+?)">.+?<img src="(.+?)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( OO0oo )
 for url , OO0ooOOO0OOO , IiI111111IIII in oo0O0oO :
  Oo00oo0000OO ( ( '[COLORgreen]' + IiI111111IIII + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3003 , 'http://www.solie.org/alibrary/' + OO0ooOOO0OOO )
def I1ii1Ii1 ( url ) :
 OO0oo = Iii1 ( url )
 oo0O0oO = re . compile ( '<br><a href="([^"]*)">(.+?)</a>' ) . findall ( OO0oo )
 OoOoO = re . compile ( 'href="([^"]*)">Season(.+?)</a>' ) . findall ( OO0oo )
 next = re . compile ( '<a href="([^"]*)">Episodes</a>' ) . findall ( OO0oo )
 IIIIiiIiiI = re . compile ( '<td align="center" valign="top">.+?<a href="(.+?)">.+?<img src="(.+?)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( OO0oo )
 for url , IiI111111IIII in oo0O0oO :
  ii1II ( ( '[COLORgreen]' + IiI111111IIII + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3004 , i1iIIi1 + 'classicmovies.png' )
 for url , IiI111111IIII in OoOoO :
  Oo00oo0000OO ( '[COLORgreen]Season- ' + IiI111111IIII + '[/COLOR]' , 'http://www.solie.org/alibrary/' + url , 3003 , i1iIIi1 + 'classicmovies.png' )
 for url in next :
  Oo00oo0000OO ( '[COLORgreen]NEXT[/COLOR]' , 'http://www.solie.org/alibrary/' + url , 3003 , i1iIIi1 + 'Next.png' )
 for url , OO0ooOOO0OOO , IiI111111IIII in IIIIiiIiiI :
  Oo00oo0000OO ( ( '[COLORgreen]' + IiI111111IIII + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3003 , 'http://www.solie.org/alibrary/' + OO0ooOOO0OOO )
def iI111I1III ( url ) :
 OO0oo = Iii1 ( url )
 oo0O0oO = re . compile ( '<iframe.+?src="([^"]*)"' ) . findall ( OO0oo )
 for url in oo0O0oO :
  i111IiiI1Ii ( url )
def i111IiiI1Ii ( url ) :
 OO0oo = Iii1 ( url )
 oo0O0oO = re . compile ( '<meta property="og:video" content="([^"]*)"/>' ) . findall ( OO0oo )
 for url in oo0O0oO :
  OOoO ( url )
  if 72 - 72: O0 . I1IiI * Oo + ii11ii1ii - OOooOOo
def iII1I11 ( ) :
 OO0oo = Iii1 ( oOOoo00O0O ( 'aHR0cDovL3JldHJvdmlzaW9uLnR2L2FsbC8=' ) )
 oo0O0oO = re . compile ( '<a href="([^"]*)"><h2><font color=".+?"><h2>(.+?)</font></h2></a>' ) . findall ( OO0oo )
 for oOo0 , IiI111111IIII in oo0O0oO :
  ii1II ( ( '[COLORgreen]' + IiI111111IIII + '[/COLOR]' ) . replace ( '&#8211;' , ':' ) , oOo0 , 8061 , i1iIIi1 + 'classicmovies.png' )
def ii11iiI11I ( url ) :
 OO0oo = Iii1 ( url )
 oo0O0oO = re . compile ( "v.src = '([^']*)';" ) . findall ( OO0oo )
 for url in oo0O0oO :
  OOoO ( url )
  if 96 - 96: iIii1I11I1II1 + i11iIiiIii - Oo . OOO0OOo
def iiIi11i1IiI ( ) :
 OO0oo = Iii1 ( oOOoo00O0O ( 'aHR0cDovL3JldHJvdmlzaW9uLnR2L2NsYXNzaWMtdHYv' ) )
 oo0O0oO = re . compile ( '<a href="([^"]*)"><h2><font color=".+?"><h2>(.+?)</font></h2></a>' ) . findall ( OO0oo )
 for oOo0 , IiI111111IIII in oo0O0oO :
  ii1II ( ( '[COLORgreen]' + IiI111111IIII + '[/COLOR]' ) . replace ( '&#8211;' , ':' ) , oOo0 , 8061 , i1iIIi1 + 'classictv.png' )
def oO00O0O0 ( url ) :
 OO0oo = Iii1 ( url )
 oo0O0oO = re . compile ( "v.src = '([^']*)';" ) . findall ( OO0oo )
 for url in oo0O0oO :
  OOoO ( url )
  if 51 - 51: Ooo00oOo00o + OOOo0 * iI
def oOO0 ( ) :
 iIIiIi1iIII1 = OooOOOOo ( oOOoo00O0O ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vbTN1c3RyZWFtcw==' ) )
 oo0O0oO = re . compile ( '<li><a href="(.+?)"> (.+?).m3u</a></li>' ) . findall ( iIIiIi1iIII1 )
 for oOo0 , IiI111111IIII in oo0O0oO :
  Oo00oo0000OO ( ( '[COLORgreen]' + IiI111111IIII + '[/COLOR]' ) . replace ( '-' , ' ' ) . replace ( '_' , ' ' ) , ( oOOoo00O0O ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vbTN1c3RyZWFtcy8=' ) ) + oOo0 , 8071 , i1iIIi1 + 'streams.png' )
def O00O00OoO ( url ) :
 iIIiIi1iIII1 = Iii1 ( url )
 oo0O0oO = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( iIIiIi1iIII1 )
 for IiI111111IIII , url in oo0O0oO :
  ii1II ( ( '[COLORgreen]' + IiI111111IIII + '[/COLOR]' ) . replace ( '_' , ' ' ) , ( url ) . strip ( ) , 404 , i1iIIi1 + 'streams.png' )
def IiIiI1i1 ( url ) :
 iIIiIi1iIII1 = Iii1 ( url )
 oo0O0oO = re . compile ( 'EXTINF:(.+?),(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( iIIiIi1iIII1 )
 for OO0ooOOO0OOO , IiI111111IIII , url in oo0O0oO :
  url = ( ( oOOoo00O0O ( 'aHR0cDovL2dlbmlldHYuaXB0di5yZTo4MDAwL2xpdmUv' ) ) + oOo0oooo00o + '/' + oO0o0o0ooO0oO + url ) . strip ( )
  ii1II ( ( '[COLORgreen]' + IiI111111IIII + '[/COLOR]' ) . replace ( '_' , ' ' ) , ( url ) . replace ( '.ts' , '.m3u8' ) , 10012 , OO0ooOOO0OOO )
  if 18 - 18: iI
def II1IIi1iII1i ( ) :
 i1OoOO ( 'Best Videos' , 'http://www.xvideos.com/best' , 10105 , i1iIIi1 + 'JIZBOX.png' , '' , '' )
 i1OoOO ( 'Genres' , 'http://www.xvideos.com' , 10106 , i1iIIi1 + 'JIZBOX.png' , '' , '' )
 i1OoOO ( 'Recently Uploaded' , 'http://xvideos.com' , 10105 , i1iIIi1 + 'JIZBOX.png' , '' , '' )
 i1OoOO ( 'Tags' , 'http://www.xvideos.com/tags' , 10103 , i1iIIi1 + 'JIZBOX.png' , '' , '' )
 i1OoOO ( 'Search' , '' , 10107 , i1iIIi1 + 'JIZBOX.png' , '' , '' , )
 if 26 - 26: O0
def iiiIi ( url ) :
 iIIiIi1iIII1 = OooOOOOo ( url )
 ooiiI1ii = re . compile ( '<li><a class=".+?".+?href="(.+?)">Next</a></li>' ) . findall ( iIIiIi1iIII1 )
 for url in ooiiI1ii :
  i1OoOO ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10103 , i1iIIi1 + 'JIZBOX.png' , '' , '' )
 oo0O0oO = re . compile ( '<li><a href="(.+?)"><b>(.+?)</b><span class="navbadge default"(.+?)</span>' ) . findall ( iIIiIi1iIII1 )
 for url , IiI111111IIII , o00iI in oo0O0oO :
  i1OoOO ( IiI111111IIII + ' - No of Videos : ' + ( o00iI ) . replace ( '>' , '' ) , 'http://www.xvideos.com' + url , 10105 , i1iIIi1 + 'JIZBOX.png' , '' , '' )
  if 76 - 76: iI + iIii1I11I1II1 + I1IiI . Ooo00oOo00o
def i1i1 ( url ) :
 iIIiIi1iIII1 = OooOOOOo ( url )
 ooiiI1ii = re . compile ( 'href="([^"]*)">Next</a></li>' ) . findall ( iIIiIi1iIII1 )
 for url in ooiiI1ii :
  i1OoOO ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10104 , i1iIIi1 + 'Next.png' , '' , '' )
 oo0O0oO = re . compile ( ':"([^"]*)".+?;</script></a></div></div><p class="profile-name"><a href="([^"]*)">(.+?)</a></p><p class="profile-counts">\n(.+?)\n' , re . DOTALL ) . findall ( iIIiIi1iIII1 )
 for OO0ooOOO0OOO , url , IiI111111IIII , o0oOoOo0 in oo0O0oO :
  i1OoOO ( IiI111111IIII + '--' + o0oOoOo0 , 'http://www.xvideos.com' + url + '#_tabVideos,videos-best' , 10105 , ( OO0ooOOO0OOO ) . replace ( 'http:\/\/' , 'http://' ) , '' , '' )
  if 38 - 38: OOooOOo % o00OO00OoO + i11iIiiIii + i1I111ii1II1i + OOO0OOo / i11iIiiIii
  if 94 - 94: i1I111ii1II1i - Oo + O0ooOooooO
def O0oooOoO ( url ) :
 iIIiIi1iIII1 = OooOOOOo ( url )
 oo0O0oO = re . compile ( '<div class="thumb-inside"><script>.+?<img src="(.+?)".+?<a href="(.+?)" title=".+?">(.+?)</a></p>.+?uration">(.+?)</span>.+?Porn quality:(.+?)</span>' , re . DOTALL ) . findall ( iIIiIi1iIII1 )
 for OO0ooOOO0OOO , url , IiI111111IIII , OOOoOO , O0Oo0 in oo0O0oO :
  I1I1IiI1 ( IiI111111IIII + ' - Porn Quality : ' + O0Oo0 + ' - ' + OOOoOO , 'http://www.xvideos.com' + url , 10108 , OO0ooOOO0OOO , OO0ooOOO0OOO , O0Oo0 + ' - ' + OOOoOO )
 iIIIi1IiI11I1 = re . compile ( '<li><a href="([^"]*)" class="no-page">Next</a></li></ul></div>' ) . findall ( iIIiIi1iIII1 )
 for url in iIIIi1IiI11I1 :
  i1OoOO ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10105 , i1iIIi1 + 'Next.png' , '' , '' )
  if 71 - 71: iI - O0 - i1I111ii1II1i . i1I111II1I % Oo
def Oo00oO ( url ) :
 iIIiIi1iIII1 = OooOOOOo ( url )
 i1Iii1i1I = re . compile ( '<div class="main-categories">(.+?)</div>' , re . DOTALL ) . findall ( iIIiIi1iIII1 )
 ooiiI1ii = re . compile ( '<li><a class=".+?".+?href="(.+?)">Next</a></li>' ) . findall ( iIIiIi1iIII1 )
 for url in ooiiI1ii :
  i1OoOO ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10106 , i1iIIi1 + 'Next.png' , '' , '' )
 oo0O0oO = re . compile ( '<li><a href="(.+?)" class="btn btn-default">(.+?)</a>' ) . findall ( str ( i1Iii1i1I ) )
 for url , IiI111111IIII in oo0O0oO :
  i1OoOO ( IiI111111IIII , 'http://www.xvideos.com' + url , 10105 , i1iIIi1 + 'JIZBOX.png' , '' , '' )
  if 94 - 94: i11iIiiIii / o00OO00OoO / Oo
  if 9 - 9: Oooo0Ooo000 / I1IiI / OoOoOO00 + o00OO00OoO
def o0O0 ( ) :
 IIiiIiII1Ii = i1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oOO0Oooo = ( IIiiIiII1Ii ) . replace ( ' ' , '+' ) . replace ( '&amp;' , '&' )
 iIIII11I1II = oOO0Oooo . lower ( )
 II1iOOoOO0O0o0 = 'http://www.xvideos.com/?k=' + iIIII11I1II
 print II1iOOoOO0O0o0 + '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'
 iIIiIi1iIII1 = OooOOOOo ( II1iOOoOO0O0o0 )
 oo0O0oO = re . compile ( '<div class="thumb-inside"><script>.+?<img src="(.+?)".+?<a href="(.+?)" title=".+?">(.+?)</a></p>.+?uration">(.+?)</span>.+?Porn quality:(.+?)</span>' , re . DOTALL ) . findall ( iIIiIi1iIII1 )
 for OO0ooOOO0OOO , oOo0 , IiI111111IIII , OOOoOO , O0Oo0 in oo0O0oO :
  I1I1IiI1 ( IiI111111IIII + ' - Porn Quality : ' + O0Oo0 + ' - ' + OOOoOO , 'http://www.xvideos.com' + oOo0 , 10108 , OO0ooOOO0OOO , OO0ooOOO0OOO , O0Oo0 + ' - ' + OOOoOO )
 iIIIi1IiI11I1 = re . compile ( '<li><a href="([^"]*)" class="no-page">Next</a></li></ul></div>' ) . findall ( iIIiIi1iIII1 )
 for oOo0 in iIIIi1IiI11I1 :
  i1OoOO ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + oOo0 , 10105 , i1iIIi1 + 'Next.png' , '' , '' )
  if 44 - 44: i1I111II1I / Oo + OoOo00o % OoOoOO00 / Ooo00oOo00o + i11iIiiIii
def ii11Iiii ( url ) :
 iIIiIi1iIII1 = OooOOOOo ( url )
 oo0O0oO = re . compile ( 'flv_url=(.+?)\;' ) . findall ( iIIiIi1iIII1 )
 for url in oo0O0oO :
  II1OoooOo = ( url ) . replace ( '%3A' , ':' ) . replace ( '%2F' , '/' ) . replace ( '%3F' , '?' ) . replace ( '%3D' , '=' ) . replace ( '%26' , '&' ) . replace ( '&amp' , '' )
  I1I1IIiiii1ii ( II1OoooOo )
  if 92 - 92: O0ooOooooO / i1I111II1I . ii11ii1ii
def I1I1IIiiii1ii ( url ) :
 iiIiIiII = xbmc . Player ( i1i ( ) )
 import urlresolver
 try : iiIiIiII . play ( url )
 except : pass
 if 60 - 60: Oo . OoOo00o % OOOo0 - o00OO00OoO
 if 79 - 79: OoooooooOO / ii11ii1ii . O0
def oOoO0Oo0 ( ) :
 iIIiIi1iIII1 = OooOOOOo ( oOOoo00O0O ( 'aHR0cDovL3d3dy5nb2Zpc2hpbmcuY28udWsvQW5nbGluZy1UaW1lcy9TZWN0aW9uL1ZpZGVvcy8=' ) )
 oo0O0oO = re . compile ( 'class="item.+?"><a href="(.+?)">(.+?)</a></li>' ) . findall ( iIIiIi1iIII1 )
 for oOo0 , IiI111111IIII in oo0O0oO :
  Oo00oo0000OO ( '[COLORgreen]' + IiI111111IIII + '[/COLOR]' , ( 'http://www.gofishing.co.uk' + oOo0 ) . replace ( 'http://www.gofishing.co.ukhttp://www.gofishing.co.uk' , 'http://www.gofishing.co.uk' ) , 8091 , i1iIIi1 + 'gofish.png' )
def i11i11i ( url ) :
 iIIiIi1iIII1 = Iii1 ( url )
 oo0O0oO = re . compile ( '<h2><a id=.+?href="([^"]*)">(.+?)</a></h2>' , re . DOTALL ) . findall ( iIIiIi1iIII1 )
 IIIIiiIiiI = re . compile ( '<h3><a href="([^"]*)" id=.+?>(.+?)</a> </h3>.+?<img src="([^"]*)"' , re . DOTALL ) . findall ( iIIiIi1iIII1 )
 next = re . compile ( 'href="([^"]*)">next</a>&gt;</li>' , re . DOTALL ) . findall ( iIIiIi1iIII1 )
 for url , IiI111111IIII in oo0O0oO :
  ii1II ( '[COLORgreen]' + IiI111111IIII + '[/COLOR]' , 'http://www.gofishing.co.uk/' + url , 8092 , i1iIIi1 + 'gofish.png' )
 for url , IiI111111IIII , OO0ooOOO0OOO in IIIIiiIiiI :
  ii1II ( '[COLORgreen]' + IiI111111IIII + '[/COLOR]' , 'http://www.gofishing.co.uk/' + url , 8092 , 'http://www.gofishing.co.uk/' + OO0ooOOO0OOO )
 for url in next :
  Oo00oo0000OO ( '[COLORgreen]NEXT[/COLOR]' , url . replace ( ' ' , '+' ) , 8091 , i1iIIi1 + 'Next.png' )
def iiI1iI ( url ) :
 iIIiIi1iIII1 = Iii1 ( url )
 oo0O0oO = re . compile ( 'src="https://www.youtube.com/embed/(.+?)"' ) . findall ( iIIiIi1iIII1 )
 for url in oo0O0oO :
  yt . PlayVideo ( url )
  if 84 - 84: OoooooooOO + o00OO00OoO / OOOo0 % i1I111II1I % ii11ii1ii * OOOo0
def OOoO0oooo ( url ) :
 I11i = urllib2 . Request ( url )
 I11i . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
 o0OoiiI1i = ''
 iiI1 = ''
 try :
  o0OoiiI1i = urllib2 . urlopen ( I11i )
  iiI1 = o0OoiiI1i . read ( )
  o0OoiiI1i . close ( )
 except : pass
 if iiI1 != '' :
  return iiI1
 else :
  iiI1 = 'Failed'
  return iiI1
  if 3 - 3: OoOo00o / Oooo0Ooo000
  if 34 - 34: i11iIiiIii / o00OO00OoO * i1I111II1I . Oo
def ooo0O00000oo0 ( ) :
 oOO0oo = ( oOOoo00O0O ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 IIiiIiII1Ii = i1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 iIIII11I1II = IIiiIiII1Ii . lower ( )
 oOo0 = ( oOOoo00O0O ( 'aHR0cDovL2RsNC5tb3ZpZWZhcnNpLmNvbS9maWxtLzIwMTUtNy8=' ) )
 IIo0o0O0O00oOOo = ( oOOoo00O0O ( 'aHR0cDovL2RsLmF2YWRsLmNvbS9OZXcvTW92aWUv' ) )
 OO0O0 = ( oOOoo00O0O ( 'aHR0cDovLzIxNy4yMTkuMTQzLjEwOC8xMzI3Lw==' ) )
 o0oo0000 = ( oOOoo00O0O ( 'aHR0cDovLzE3OC4xNjIuMjE0LjIzMi92b2QvbW92aWVzL2VuZ2xpc2gv' ) )
 oOo0OOOOoO = ( oOOoo00O0O ( 'aHR0cDovL3Njb29ieXN0cmVhbS54MTBob3N0LmNvbS8vc2Nvb2J5L21vdi9hbGwucGhw' ) )
 OoO0Ooo = ( oOOoo00O0O ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 Ii1I1I = ( oOOoo00O0O ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL3NlYXJjaC8/cT0=' ) ) + IIiiIiII1Ii
 if 56 - 56: O0
 if 45 - 45: I1IiI - Ooo00oOo00o - I1IiI
 iIIiIi1iIII1 = OOoO0oooo ( oOo0 )
 o00o = OOoO0oooo ( IIo0o0O0O00oOOo )
 IIiiI = OOoO0oooo ( OO0O0 )
 iII11iiiiiii = OOoO0oooo ( o0oo0000 )
 O0000Oo = OOoO0oooo ( oOo0OOOOoO )
 OOOOOO = OOoO0oooo ( Ii1I1I )
 if 77 - 77: Oo
 if 23 - 23: OOooOOo + iI % I1IiI % OOOo0 % OoooooooOO
 if iIIiIi1iIII1 != 'Failed' :
  oo0O0oO = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( iIIiIi1iIII1 )
  for OOOOoo00OO0O0Ooo0 , IiI111111IIII in oo0O0oO :
   if IIiiIiII1Ii in IiI111111IIII . lower ( ) :
    ii1II ( ( '[COLORgreen]' + IiI111111IIII + '- source 1[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( oOo0 + OOOOoo00OO0O0Ooo0 ) , 222 , '' )
 if o00o != 'Failed' :
  IIIIiiIiiI = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( o00o )
  for OOOOoo00OO0O0Ooo0 , IiI111111IIII in IIIIiiIiiI :
   if IIiiIiII1Ii in IiI111111IIII . lower ( ) :
    ii1II ( ( '[COLORgreen]' + IiI111111IIII + '- source 2[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( IIo0o0O0O00oOOo + OOOOoo00OO0O0Ooo0 ) , 222 , '' )
 if IIiiI != 'Failed' :
  oO0o = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( IIiiI )
  for OOOOoo00OO0O0Ooo0 , IiI111111IIII in oO0o :
   if IIiiIiII1Ii in IiI111111IIII . lower ( ) :
    ii1II ( ( '[COLORgreen]' + IiI111111IIII + '- source 3[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( OO0O0 + OOOOoo00OO0O0Ooo0 ) , 222 , '' )
 if iII11iiiiiii != 'Failed' :
  ooOOO00oOOooO = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( iII11iiiiiii )
  for OOOOoo00OO0O0Ooo0 , IiI111111IIII in ooOOO00oOOooO :
   if IIiiIiII1Ii in IiI111111IIII . lower ( ) :
    ii1II ( ( '[COLORgreen]' + IiI111111IIII + '- source 4[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( o0oo0000 + OOOOoo00OO0O0Ooo0 ) , 222 , '' )
 if O0000Oo != 'Failed' :
  IiIIii1iiI = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( O0000Oo )
  for OOOOoo00OO0O0Ooo0 , OO0ooOOO0OOO , IiI111111IIII in IiIIii1iiI :
   if IIiiIiII1Ii in IiI111111IIII . lower ( ) :
    Oo00oo0000OO ( ( '[COLORgreen]' + IiI111111IIII + '- source Scooby[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( 'Ganool' , '' ) . replace ( 'ShAaNiG' , '' ) . replace ( 'YIFY' , '' ) . replace ( '[[ Max-Movie.In ]]' , '' ) . replace ( '.mkv' , '' ) . replace ( '.mp4' , '' ) . replace ( '.' , ' ' ) , OOOOoo00OO0O0Ooo0 , 1006 , 'img' )
    if 7 - 7: OOooOOo
    O00Oo000ooO0 ( 'tvshows' , 'Media Info 3' )
 if OOOOOO != 'Failed' :
  IiiIIi = re . compile ( 'href="(.+?)".+?src="(.+?)" alt="Image of (.+?)"' , re . DOTALL ) . findall ( OOOOOO )
  for oOo0 , OO0ooOOO0OOO , IiI111111IIII in IiiIIi :
   if IIiiIiII1Ii in IiI111111IIII . lower ( ) :
    Oo00oo0000OO ( ( '[COLORgreen]' + IiI111111IIII + '- source Snag[/COLOR]' ) . replace ( '&#x27;' , '' ) , 'http://www.snagfilms.com' + oOo0 , 7067 , OO0ooOOO0OOO )
    if 96 - 96: i1IIi . Oooo0Ooo000 + O0ooOooooO + ii11ii1ii * i1I111II1I - OoOoOO00
    O00Oo000ooO0 ( 'tvshows' , 'Media Info 3' )
 iIO0OO0o0O00oO = [ 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' ]
 if 81 - 81: OoOo00o / Oooo0Ooo000
 for OO0o0OO0 in iIO0OO0o0O00oO :
  OooOo0OOO = IIIII + OO0o0OO0 + OooO0
  III1 = OooOOOOo ( OooOo0OOO )
  if III1 != 'Failed' :
   IIi11 = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( III1 )
   for oOo0 , OOO0000oO , OOoOO0ooo , OO0oo0O0OOO0 , IiI111111IIII in IIi11 :
    if IIiiIiII1Ii in IiI111111IIII . lower ( ) :
     ii1II ( '[COLORgreen]' + IiI111111IIII + ' - Source Pandoras[/COLOR]' , oOo0 , 222 , OOO0000oO , '' , OOoOO0ooo )
     if 73 - 73: OOO0OOo + ii11ii1ii
     O00Oo000ooO0 ( 'tvshows' , 'Media Info 3' )
     if 100 - 100: iIii1I11I1II1
 oOoOo = [ '0-9/' , 'A/' , 'B/' , 'C/' , 'D/' , 'E/' , 'F/' , 'G/' , 'H/' , 'I/' , 'J/' , 'K/' , 'L/' , 'M/' , 'N/' , 'O/' , 'P/' , 'R/' , 'S/' , 'T/' , 'U/' , 'V/' , 'W/' , 'X/' , 'Y/' , 'Z/' ]
 if 77 - 77: OoOoOO00 + OOooOOo
 if 47 - 47: i1I111II1I
 for OO0o0OO0 in oOoOo :
  OooOo0OOO = oOO0oo + OO0o0OO0
  o0Ooo0o0Oo = OOoO0oooo ( OooOo0OOO )
  if O0000Oo != 'Failed' :
   oo00ooooOOo00 = re . compile ( '<li><a href="(.+?)"> (.+?)</a></li>' ) . findall ( o0Ooo0o0Oo )
   for OOOOoo00OO0O0Ooo0 , IiI111111IIII in oo00ooooOOo00 :
    if IIiiIiII1Ii in IiI111111IIII . lower ( ) :
     ii1II ( ( '[COLORgreen]' + IiI111111IIII + 'source 5[/COLOR]' ) . replace ( 'Ganool' , '' ) . replace ( 'ShAaNiG' , '' ) . replace ( 'YIFY' , '' ) . replace ( '[[ Max-Movie.In ]]' , '' ) . replace ( '.mkv' , '' ) . replace ( '.mp4' , '' ) . replace ( '.' , ' ' ) , ( oOO0oo + OO0o0OO0 + OOOOoo00OO0O0Ooo0 ) , 222 , '' )
     if 16 - 16: i11iIiiIii / i1IIi % i1I111II1I
     O00Oo000ooO0 ( 'tvshows' , 'Media Info 3' )
     if 84 - 84: Oooo0Ooo000 - Oo * O0 / iI . iI
     if 93 - 93: O0 / OOO0OOo + OOOo0
def I111 ( ) :
 if 17 - 17: iIii1I11I1II1 + OOOo0
 IIiiIiII1Ii = i1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 iIIII11I1II = IIiiIiII1Ii . lower ( )
 oO0oiIiI = ( oOOoo00O0O ( 'aHR0cDovL2Nvb2x0dnNlcmllcy5jb20vc2VhcmNoLnBocD90YWc9' ) ) + ( IIiiIiII1Ii ) . replace ( ' ' , '+' )
 oOo0 = ( oOOoo00O0O ( 'aHR0cDovL2RsLmZhcnNpbW92aWUubmV0L1NlcmlhbC8=' ) )
 IIo0o0O0O00oOOo = ( oOOoo00O0O ( 'aHR0cDovL3N2Mi5kbC1wYXJzLmluLw==' ) )
 OO0O0 = ( oOOoo00O0O ( 'aHR0cDovL3R2LmRsLXBhcnMuaW4v' ) )
 o0oo0000 = ( oOOoo00O0O ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9BbWVyaWNhbiUyMFNlcmlhbC8=' ) )
 oOo0OOOOoO = ( oOOoo00O0O ( 'aHR0cDovL2RpemlsYWIuY29tL2Fyc2l2P2xpbWl0PSZ0dXI9Jm9yZGVyYnk9JnVsa2U9Jm9yZGVyPSZ5aWw9JmRpemlfYWRpPQ==' ) ) + ( IIiiIiII1Ii ) . replace ( ' ' , '+' )
 OoO0Ooo = ( oOOoo00O0O ( 'aHR0cDovL3Njb29ieXN0cmVhbS54MTBob3N0LmNvbS8vc2Nvb2J5L3Nob3dzL3R2YWxsLnBocA==' ) )
 iIIiiiI1iI1 = ( oOOoo00O0O ( 'aHR0cDovL2xldHdhdGNoLnVzLz9vcD1zZWFyY2gmaz0=' ) ) + ( IIiiIiII1Ii ) . replace ( ' ' , '+' )
 oO00000oO0o0O = ( oOOoo00O0O ( 'aHR0cDovL3d3dy53YXRjaHNlcmllcy5saS9zZWFyY2gv' ) ) + ( IIiiIiII1Ii ) . replace ( ' ' , '%20' )
 if 34 - 34: Oo - i1IIi - OOO0OOo - i1IIi
 O00Oo = OOoO0oooo ( oO0oiIiI )
 iIIiIi1iIII1 = OOoO0oooo ( oOo0 )
 o00o = OOoO0oooo ( IIo0o0O0O00oOOo )
 IIiiI = OOoO0oooo ( OO0O0 )
 iII11iiiiiii = OOoO0oooo ( o0oo0000 )
 O0000Oo = cloudflare . source ( oOo0OOOOoO )
 o0Ooo0o0Oo = OOoO0oooo ( OoO0Ooo )
 III1 = OooOOOOo ( iIIiiiI1iI1 )
 iii = OooOOOOo ( oO00000oO0o0O )
 if O00Oo != 'Failed' :
  O0ooO0O0Ooo0o = re . compile ( 'href="([^"]*)"><img src="([^"]*)" alt="([^"]*)"' ) . findall ( O00Oo )
  for oOo0 , OO0ooOOO0OOO , IiI111111IIII in O0ooO0O0Ooo0o :
   if IIiiIiII1Ii in IiI111111IIII . lower ( ) :
    Oo00oo0000OO ( '[COLORgreen]' + IiI111111IIII + ' CoolSeries[/COLOR]' , oOo0 , 7052 , OO0ooOOO0OOO )
    if 25 - 25: i1I111II1I * i1I111II1I / O0ooOooooO % Oo
    O00Oo000ooO0 ( 'tvshows' , 'Media Info 3' )
 if iIIiIi1iIII1 != 'Failed' :
  oo0O0oO = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( iIIiIi1iIII1 )
  for IiI111111IIII in oo0O0oO :
   if IIiiIiII1Ii in IiI111111IIII . lower ( ) :
    Oo00oo0000OO ( ( '[COLORgreen]' + IiI111111IIII + ' source 1[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( oOo0 + IiI111111IIII ) . replace ( ' ' , '%20' ) , 1006 , '' )
    if 33 - 33: OoOo00o . OoooooooOO . O0ooOooooO
    O00Oo000ooO0 ( 'tvshows' , 'Media Info 3' )
 if o00o != 'Failed' :
  IIIIiiIiiI = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( o00o )
  for IiI111111IIII in IIIIiiIiiI :
   if IIiiIiII1Ii in IiI111111IIII . lower ( ) :
    Oo00oo0000OO ( ( IiI111111IIII + ' source 2' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( IIo0o0O0O00oOOo + IiI111111IIII ) . replace ( ' ' , '%20' ) , 1006 , '' )
    if 15 - 15: ii11ii1ii . i1I111ii1II1i
    O00Oo000ooO0 ( 'tvshows' , 'Media Info 3' )
 if IIiiI != 'Failed' :
  oO0o = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( IIiiI )
  for IiI111111IIII in IIIIiiIiiI :
   if IIiiIiII1Ii in IiI111111IIII . lower ( ) :
    Oo00oo0000OO ( ( IiI111111IIII + ' source 3' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( OO0O0 + IiI111111IIII ) . replace ( ' ' , '%20' ) , 1006 , '' )
    if 94 - 94: Oooo0Ooo000 . OOOo0
    O00Oo000ooO0 ( 'tvshows' , 'Media Info 3' )
 if iII11iiiiiii != 'Failed' :
  ooOOO00oOOooO = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( iII11iiiiiii )
  for IiI111111IIII in IIIIiiIiiI :
   if IIiiIiII1Ii in IiI111111IIII . lower ( ) :
    Oo00oo0000OO ( ( IiI111111IIII + ' source 4' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( o0oo0000 + IiI111111IIII ) . replace ( ' ' , '%20' ) , 1006 , '' )
    if 73 - 73: i1IIi / OoOoOO00
    O00Oo000ooO0 ( 'tvshows' , 'Media Info 3' )
 if O0000Oo != 'Failed' :
  IiIIii1iiI = re . compile ( '<a href="(.+?)" class="film-image">\n<img src="(.+?)" alt=""/>\n</a>\n<div class="tss-detail">\n<a class="title" style="" href=".+?">\n<span class="position">.+?</span>\n(.+?)</a>' ) . findall ( O0000Oo )
  for oOo0 , OO0ooOOO0OOO , IiI111111IIII in IiIIii1iiI :
   if IIiiIiII1Ii in IiI111111IIII . lower ( ) :
    Oo00oo0000OO ( '[COLORgreen]' + IiI111111IIII + ' - Source - Dizi[/COLOR]' , oOo0 , 8062 , OO0ooOOO0OOO )
    if 45 - 45: iI / OOO0OOo . OoooooooOO + Ooo00oOo00o
    O00Oo000ooO0 ( 'tvshows' , 'Media Info 3' )
 if o0Ooo0o0Oo != 'Failed' :
  oo00ooooOOo00 = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( o0Ooo0o0Oo )
  for oOo0 , OO0ooOOO0OOO , IiI111111IIII in oo00ooooOOo00 :
   if IIiiIiII1Ii in IiI111111IIII . lower ( ) :
    ii1II ( ( '[COLORgreen]' + IiI111111IIII + '- Source Scooby[/COLOR]' ) , oOo0 , 222 , 'img' )
    if 51 - 51: i1I111ii1II1i % i11iIiiIii % OoOo00o + o00OO00OoO % ii11ii1ii
    O00Oo000ooO0 ( 'tvshows' , 'Media Info 3' )
 if III1 != 'Failed' :
  IIi11 = re . compile ( '<div class="video_block video_block_default ">.+?<a href="#">.+?<a href="(.*?)".+?<img src="(.+?)" height=".+?" alt="(.+?)"' , re . DOTALL ) . findall ( III1 )
  for oOo0 , OO0ooOOO0OOO , IiI111111IIII in IIi11 :
   ii1II ( '[COLORgreen]' + IiI111111IIII + ' - Source DiZzY[/COLOR]' , oOo0 , 222 , OO0ooOOO0OOO )
 if iii != 'Failed' :
  IIIIIiiiiI1I = re . compile ( '<img src="(.+?)".+?<a href="(.+?)" title=".+?"><b>(.+?)</b>' , re . DOTALL ) . findall ( iii )
  for OO0ooOOO0OOO , oOo0 , IiI111111IIII in IIIIIiiiiI1I :
   if 'watch online' in IiI111111IIII :
    pass
   else :
    IIIIii ( '[COLORgreen]' + IiI111111IIII + '- Source WATCH SERIES[/COLOR]' , 'http://www.watchseries.li' + oOo0 , 10044 , OO0ooOOO0OOO , '' , '' )
    if 93 - 93: Oo * O0ooOooooO + Ooo00oOo00o - o00OO00OoO . ii11ii1ii + OoooooooOO
    xbmcplugin . setContent ( O0O , 'movies' )
 i1II11I11ii1 = [ 'a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' , 'p' , 'q' , 'r' , 's' , 't' , 'u' , 'v' , 'w' , 'x' , 'y' , 'z' ]
 if 64 - 64: O0ooOooooO % I1IiI / OoOoOO00 % OOO0OOo - i1I111ii1II1i
 for OO0o0OO0 in i1II11I11ii1 :
  OooOo0OOO = IIIII + OO0o0OO0 + OooO0
  I1II1IiI1 = OooOOOOo ( OooOo0OOO )
  if I1II1IiI1 != 'Failed' :
   iIIiI11iI1Ii1 = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( I1II1IiI1 )
   for IiI111111IIII , OOoOO0ooo , oOo0 , OO0ooOOO0OOO , iI1i111I1Ii , Ooo00o0oOo0O0O in iIIiI11iI1Ii1 :
    if IIiiIiII1Ii in IiI111111IIII . lower ( ) :
     IIIIii ( '[COLORgreen]' + IiI111111IIII + ' - Source Pandoras[/COLOR]' , oOo0 , Ooo00o0oOo0O0O , OO0ooOOO0OOO , iI1i111I1Ii , OOoOO0ooo )
     if 94 - 94: OOO0OOo / i11iIiiIii % O0
     O00Oo000ooO0 ( 'tvshows' , 'Media Info 3' )
     if 70 - 70: Oooo0Ooo000 - Oo / OoooooooOO % OoooooooOO
     if 95 - 95: OoooooooOO % OoooooooOO . iI
 xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
def III1ii ( ) :
 if 38 - 38: ii11ii1ii + I1IiI
 IIiiIiII1Ii = i1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 iIIII11I1II = IIiiIiII1Ii . lower ( )
 oOo0 = ( oOOoo00O0O ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz' ) )
 iIIiIi1iIII1 = OooOOOOo ( oOo0 )
 oo0O0oO = re . compile ( '"id":".+?","name":"(.+?)","img":"(.+?)","stream_url3":".+?","cat_id":"(.+?)","stream_url2":".+?","stream_url":".+?"}' , re . DOTALL ) . findall ( iIIiIi1iIII1 )
 for IiI111111IIII , OO0ooOOO0OOO , o0IiIiI111IIII1 in oo0O0oO :
  OOOoOooO000oO = oOOoo00O0O ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv' ) + ( OO0ooOOO0OOO ) . replace ( '\\' , '' )
  if IIiiIiII1Ii in IiI111111IIII . lower ( ) :
   Oo00oo0000OO ( IiI111111IIII , '' , 7022 , OOOoOooO000oO )
   if 87 - 87: i1I111ii1II1i % Oo
 xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 62 - 62: Ooo00oOo00o + OOO0OOo / i1I111ii1II1i * i11iIiiIii
 if 37 - 37: i1I111ii1II1i
def iIIiI1111 ( url ) :
 OooOO = cloudflare . source ( url )
 oo0O0oO = re . compile ( '<a class="season" href="(.+?)">\n(.+?)\n</a>\n</span>\n<span>\n<a class="episode" href=".+?">\n(.+?)\n</a>\n</span>\n<span>\n<a class="episode-name" href=".+?">\n(.+?)</a>' ) . findall ( OooOO )
 for url , II1III1i1iiI , i1Ii , IiI111111IIII in oo0O0oO :
  Oo00oo0000OO ( ( II1III1i1iiI ) . replace ( 'Sezon' , ' Season ' ) + ( i1Ii ) . replace ( 'Bölüm' , ' Episode ' ) + IiI111111IIII , url , 8063 , '' )
  if 86 - 86: iI . i1I111II1I / OoOo00o - OoooooooOO
  if 45 - 45: i1I111II1I
  if 25 - 25: i1I111II1I % O0
  if 44 - 44: o00OO00OoO . iI * OoOoOO00 / OoOo00o + iIii1I11I1II1
def Ii1111III1 ( url ) :
 OooOO = cloudflare . source ( url )
 oo0O0oO = re . compile ( 'file: "(.+?)",.+?label: "(.+?)",' , re . DOTALL ) . findall ( OooOO )
 for url , IiI111111IIII in oo0O0oO :
  ii1II ( IiI111111IIII , url , 222 , '' )
  if 74 - 74: ii11ii1ii - i1I111ii1II1i * i1IIi
  if 12 - 12: O0
  if 75 - 75: iIii1I11I1II1 % OoOo00o + ii11ii1ii * O0 . i1I111ii1II1i - OOO0OOo
  if 32 - 32: iI % O0ooOooooO - i1IIi
def Ii11III ( ) :
 if 15 - 15: Oooo0Ooo000 % OOOo0 - iIii1I11I1II1 * OOO0OOo
 OooOO = cloudflare . source ( oOOoo00O0O ( 'aHR0cDovL2RpemlsYWIuY29t' ) )
 oo0O0oO = re . compile ( '<li id=".+?">.+?<a href="(.+?)">.+?<img width="40" height="40" src="(.+?)" alt=""/>.+?<span class="title">\n(.+?)</span>.+?<span class="alt-title">\n(.+?)</span>.+?</a>.+?</li>' , re . DOTALL ) . findall ( OooOO )
 for oOo0 , OO0ooOOO0OOO , IiI111111IIII , i1Ii in oo0O0oO :
  Oo00oo0000OO ( IiI111111IIII + '  -  ' + ( i1Ii ) . replace ( 'sezon' , 'Season' ) . replace ( 'bölüm' , 'Episode' ) , oOo0 , 8063 , OO0ooOOO0OOO )
  if 71 - 71: I1IiI % Oo % OOO0OOo
def I111III1 ( ) :
 OO0oo = Iii1 ( oOOoo00O0O ( 'aHR0cDovL3d3dy50dmd1aWRlLmNvLnVrLw==' ) )
 oo0O0oO = re . compile ( '<a href="(.+?)"  qt-title=".+?" qt-text=".+?<br> .+?" title="(.+?)".+?class=".+? src="(.+?)" alt=".+?" /></a>' , re . DOTALL ) . findall ( OO0oo )
 for oOo0 , IiI111111IIII , OO0ooOOO0OOO in oo0O0oO :
  ii1II ( '[COLORgreen]' + IiI111111IIII + '[/COLOR]' , oOo0 , 8002 , OO0ooOOO0OOO )
def OOO000OOo0o0O ( url ) :
 OO0oo = Iii1 ( url )
 oo0O0oO = re . compile ( '<table border="0".+?url((.+?));background-repeat: no-repeat;">.+?<tr>.+?<span class="season">(.+?)</span><br>.+?<a href="(.+?)"+?>(.+?)</span><br>.+?<span class="programmetext">(.+?)</span></a><br>' , re . DOTALL ) . findall ( OO0oo )
 for OO0ooOOO0OOO , time , url , IiI111111IIII , I1i in oo0O0oO :
  IIIIii ( '%s %s' % ( '[COLORgreen]' + IiI111111IIII + '[/COLOR]' , time ) , url , 1015 , OO0ooOOO0OOO , I1i )
  if 14 - 14: i1I111ii1II1i - Oooo0Ooo000 * OoooooooOO + i1I111II1I . OoOoOO00
def i1i1I11i1I ( ) :
 if 85 - 85: OOO0OOo . O0 / i1I111II1I * OOO0OOo - Ooo00oOo00o - i11iIiiIii
 Oo00oo0000OO ( 'Coronation Street' , '' , 8001 , '' )
 Oo00oo0000OO ( 'Eastenders' , '' , 8002 , '' )
 Oo00oo0000OO ( 'Emmerdale' , '' , 8003 , '' )
 Oo00oo0000OO ( 'Hollyoaks' , '' , 8004 , '' )
 Oo00oo0000OO ( 'Im a Celebrity' , '' , 8005 , '' )
 if 25 - 25: OOO0OOo % Oo - i1I111II1I
 if 80 - 80: OoOo00o % OoOoOO00 - Oo - iIii1I11I1II1
 if 9 - 9: OOooOOo % ii11ii1ii . ii11ii1ii
 if 28 - 28: OoooooooOO % O0ooOooooO + ii11ii1ii + O0 . o00OO00OoO
def ooOO0OOO00o ( ) :
 iIIiIi1iIII1 = OooOOOOo ( 'http://uksoapshare.blogspot.co.uk/' )
 oo0O0oO = re . compile ( '<a href="(.+?)".+?target=_blank>(.+?)</a>' ) . findall ( iIIiIi1iIII1 )
 for oOo0 , IiI111111IIII in oo0O0oO :
  if 'Holly' in IiI111111IIII :
   OO0ooOOO0OOO = 'http://2.bp.blogspot.com/-9c7Sieh1RKs/UjD6TGAEEnI/AAAAAAAAAC8/84uwHfxcuYg/s1600/Hollyoaks.png'
   if 'huge' in oOo0 :
    ii1II ( ( IiI111111IIII ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , oOo0 . replace ( '\\/' , '/' ) , 8006 , OO0ooOOO0OOO )
   else :
    pass
    if 76 - 76: OoooooooOO * OoooooooOO - i1I111ii1II1i - iIii1I11I1II1 . OoooooooOO / ii11ii1ii
 xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE_IGNORE_THE ) ;
 if 86 - 86: OOO0OOo
def oO0oo0O0 ( ) :
 iIIiIi1iIII1 = OooOOOOo ( 'http://uksoapshare.blogspot.co.uk/' )
 oo0O0oO = re . compile ( '<a href="(.+?)".+?target=_blank>(.+?)</a>' ) . findall ( iIIiIi1iIII1 )
 for oOo0 , IiI111111IIII in oo0O0oO :
  if 'East' in IiI111111IIII :
   OO0ooOOO0OOO = 'http://3.bp.blogspot.com/-KWHcNbNJU8Y/Vi1ousRl7fI/AAAAAAAAAT8/ksNE12LH0nE/s1600/eastenders.jpg'
   if 'huge' in oOo0 :
    ii1II ( ( IiI111111IIII ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , oOo0 . replace ( '\\/' , '/' ) , 8006 , OO0ooOOO0OOO )
   else :
    pass
    if 66 - 66: i1I111II1I - OOO0OOo - Oo
 xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 54 - 54: i1I111ii1II1i . i1IIi
def i1IiIiIiiI1 ( ) :
 iIIiIi1iIII1 = OooOOOOo ( 'http://uksoapshare.blogspot.co.uk/' )
 oo0O0oO = re . compile ( '<a href="(.+?)".+?target=_blank>(.+?)</a>' ) . findall ( iIIiIi1iIII1 )
 for oOo0 , IiI111111IIII in oo0O0oO :
  if 'Emmer' in IiI111111IIII :
   OO0ooOOO0OOO = 'http://2.bp.blogspot.com/-UfDcxisVV5c/UjH9vUicZ3I/AAAAAAAAADc/8Ozuiz1ojxw/s1600/Emmerdale.jpg'
   if 'huge' in oOo0 :
    ii1II ( ( IiI111111IIII ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , oOo0 . replace ( '\\/' , '/' ) , 8006 , OO0ooOOO0OOO )
   else :
    pass
    if 41 - 41: OoOoOO00
 xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 43 - 43: O0 - OOO0OOo % OoooooooOO % i1I111II1I + i1I111ii1II1i
def o0OIi ( ) :
 iIIiIi1iIII1 = OooOOOOo ( 'http://uksoapshare.blogspot.co.uk/' )
 oo0O0oO = re . compile ( '<a href="(.+?)".+?target=_blank>(.+?)</a>' ) . findall ( iIIiIi1iIII1 )
 for oOo0 , IiI111111IIII in oo0O0oO :
  if 'Coro' in IiI111111IIII :
   OO0ooOOO0OOO = 'http://3.bp.blogspot.com/-hofvfBQVexs/UjErIfNdS4I/AAAAAAAAADQ/Q-vVGu3apYU/s1600/corrie.jpg'
   if 'huge' in oOo0 :
    ii1II ( ( IiI111111IIII ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , oOo0 . replace ( '\\/' , '/' ) , 8006 , OO0ooOOO0OOO )
   else :
    pass
    if 11 - 11: O0ooOooooO . OOOo0 + OoOo00o / i1IIi
 xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 1 - 1: Oo * o00OO00OoO . OoooooooOO
def oOO00OO0o0O ( ) :
 iIIiIi1iIII1 = OooOOOOo ( 'http://uksoapshare.blogspot.co.uk/' )
 oo0O0oO = re . compile ( '<a href="(.+?)" target="_blank">(.+?)</a>' ) . findall ( iIIiIi1iIII1 )
 for oOo0 , IiI111111IIII in oo0O0oO :
  if 'Celeb' in IiI111111IIII :
   OO0ooOOO0OOO = 'http://3.bp.blogspot.com/-a_yDotWU_pY/VkotKWaG_gI/AAAAAAAAAUk/8Q5iNM6p37k/s1600/iacgoh.jpg'
   if 'huge' in oOo0 :
    ii1II ( ( IiI111111IIII ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , oOo0 . replace ( '\\/' , '/' ) , 8006 , OO0ooOOO0OOO )
   else :
    pass
    if 35 - 35: OOooOOo * i1I111ii1II1i - iIii1I11I1II1 + OOooOOo . OoooooooOO
def ii111iI1i1 ( name , url ) :
 OO000 = urlresolver . HostedMediaFile ( url ) . valid_url ( )
 if OO000 :
  IIiii11ii1II1 = urlresolver . HostedMediaFile ( url ) . resolve ( )
 else :
  OO0oo = open_url ( url )
  url = re . compile ( 'src="(.+?)"></iframe>' ) . findall ( OO0oo ) [ 0 ]
  url = url . split ( '?autoplay' ) [ 0 ]
  OO0oo = open_url ( url )
  o0OO000O = re . compile ( 'mp4","url":"(.+?)"' ) . findall ( OO0oo ) [ - 1 ]
  IIiii11ii1II1 = o0OO000O . replace ( '\\/' , '/' )
 oo0O = xbmcgui . ListItem ( name , '' , '' )
 oo0O . setPath ( IIiii11ii1II1 )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , oo0O )
 if 62 - 62: Oooo0Ooo000 % Oooo0Ooo000 % Oooo0Ooo000 / i1I111ii1II1i * OOooOOo * O0ooOooooO
 if 61 - 61: OoOo00o % i1IIi - i1I111ii1II1i . OOO0OOo - Oo + Oo
def II1ii1Ii ( ) :
 OO0oo = OooOOOOo ( oOOoo00O0O ( 'aHR0cDovL3d3dy5kaXppYm94aGQuY29tLw==' ) )
 oo0O0oO = re . compile ( 'class="film menu-item menu-item-type-post_type menu-item-object-page menu-item-36980"><a href="(.+?)"><i class="fa fa-film"></i><span>(.+?)</span></a></li>' ) . findall ( OO0oo )
 IIIIiiIiiI = re . compile ( 'class="menu-item menu-item-type-post_type menu-item-object-page menu-item-52949"><a href="(.+?)"><i class="fa fa-"></i><span>(.+?)</span></a></li>' ) . findall ( OO0oo )
 for oOo0 , IiI111111IIII in oo0O0oO :
  Oo00oo0000OO ( ( '[COLORgreen]' + IiI111111IIII + '[/COLOR]' ) . replace ( 'Diziler' , 'Series' ) , oOo0 , 7071 , i1iIIi1 + 'popcorn.png' )
 for oOo0 , IiI111111IIII in IIIIiiIiiI :
  Oo00oo0000OO ( ( '[COLORgreen]' + IiI111111IIII + '[/COLOR]' ) . replace ( 'Filmler' , 'Movies' ) , oOo0 , 7071 , i1iIIi1 + 'popcorn.png' )
  if 31 - 31: i1I111ii1II1i - I1IiI . I1IiI - O0ooOooooO + Oo / i11iIiiIii
def ooOoOo ( ) :
 OO0oo = OooOOOOo ( oOOoo00O0O ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL2NhdGVnb3JpZXMv' ) )
 oo0O0oO = re . compile ( '<a class="nav-item" href="(.+?)">(.+?)</a>' ) . findall ( OO0oo )
 for oOo0 , IiI111111IIII in oo0O0oO :
  if 'Movies' in IiI111111IIII :
   Oo00oo0000OO ( '[COLORgreen]' + IiI111111IIII + '[/COLOR]' , 'http://www.snagfilms.com' + ( oOo0 ) . replace ( 'http://www.snagfilms.com' , '' ) , 7061 , i1iIIi1 + 'popcorn.png' )
def iIiii1iI1i ( url ) :
 OO0oo = OooOOOOo ( url )
 oo0O0oO = re . compile ( '<a class="object-link size-poster".+?href="(.+?)" data-type="category">.+?src="(.+?)" alt="Image of (.+?)" />' , re . DOTALL ) . findall ( OO0oo )
 oo0O0oO = re . compile ( '<a class="object-link size-poster".+?href="(.+?)" data-type="category">.+?src="(.+?)" alt="Image of (.+?)" />' , re . DOTALL ) . findall ( OO0oo )
 IIIIiiIiiI = re . compile ( "<li class='current'>.+?</li><li ><a href='(.+?)'>.+?</a></li><li" , re . DOTALL ) . findall ( OO0oo )
 for url , OO0ooOOO0OOO , IiI111111IIII in oo0O0oO :
  Oo00oo0000OO ( '[COLORgreen]' + IiI111111IIII + '[/COLOR]' , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7067 , OO0ooOOO0OOO )
 for url in IIIIiiIiiI :
  Oo00oo0000OO ( '[COLORgreen]NEXT PAGE[/COLOR]' , ( url ) . replace ( '&#038;' , '&' ) , 7063 , i1iIIi1 + 'Next.png' )
  if 36 - 36: OoOo00o + OoooooooOO / i11iIiiIii
  if 40 - 40: OoooooooOO * I1IiI / OoOoOO00 - ii11ii1ii + iI
def o0O00OooooO ( url ) :
 OO0oo = OooOOOOo ( oOOoo00O0O ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL2NhdGVnb3JpZXMv' ) )
 oo0O0oO = re . compile ( '<a class="object-link size-poster".+?href="(.+?)" data-type="category">.+?src="(.+?)" alt="Image of (.+?)" />' , re . DOTALL ) . findall ( OO0oo )
 for url , OO0ooOOO0OOO , IiI111111IIII in oo0O0oO :
  Oo00oo0000OO ( '[COLORgreen]' + IiI111111IIII + '[/COLOR]' , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7062 , OO0ooOOO0OOO )
  if 77 - 77: OOOo0 % OOO0OOo
  if 74 - 74: I1IiI / i1IIi % OoooooooOO
def o00o0o000Oo ( url ) :
 OO0oo = OooOOOOo ( url )
 oo0O0oO = re . compile ( 'href="(.+?)".+?src="(.+?)" alt="Image of (.+?)"' , re . DOTALL ) . findall ( OO0oo )
 for url , OO0ooOOO0OOO , IiI111111IIII in oo0O0oO :
  Oo00oo0000OO ( ( '[COLORgreen]' + IiI111111IIII + '[/COLOR]' ) . replace ( '&#x27;' , '' ) , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7067 , OO0ooOOO0OOO )
  if 100 - 100: i1IIi - i11iIiiIii . o00OO00OoO * Ooo00oOo00o
def oOIIII ( url ) :
 OO0oo = OooOOOOo ( url )
 oo0O0oO = re . compile ( '<div class="film-container">.+?<iframe src="(.+?)"' , re . DOTALL ) . findall ( OO0oo )
 for url in oo0O0oO :
  ooOOo ( 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) )
  if 5 - 5: O0
def ooOOo ( url ) :
 OO0oo = OooOOOOo ( url )
 oo0O0oO = re . compile ( 'file: "(.+?)",.+?label: "(.+?)"' , re . DOTALL ) . findall ( OO0oo )
 for url , IiI111111IIII in oo0O0oO :
  ii1II ( '[COLORgreen]' + IiI111111IIII + '[/COLOR]' , url , 222 , i1iIIi1 + 'popcorn.png' )
  if 75 - 75: o00OO00OoO + iIii1I11I1II1
  if 19 - 19: OOOo0 + i11iIiiIii . OoOo00o - Oooo0Ooo000 / iI + OOooOOo
  if 38 - 38: Oo / iIii1I11I1II1 * iIii1I11I1II1 % ii11ii1ii
  if 92 - 92: Oooo0Ooo000 / O0 * OOOo0 - Oooo0Ooo000
def oooOo00000 ( url ) :
 OO0oo = OooOOOOo ( url )
 oo0O0oO = re . compile ( '</h4><p><ul><li><a href="([^"]*)">(.+?)<.+?class=' ) . findall ( OO0oo )
 IIIIiiIiiI = re . compile ( '<li><a href="([^"]*)">(.+?)<.+?class=' ) . findall ( OO0oo )
 for url , IiI111111IIII in oo0O0oO :
  if '(cooltvseries.com)' in IiI111111IIII :
   ii1II ( ( '[COLORgreen]' + IiI111111IIII + ' -(360)-[/COLOR]' ) . replace ( ' - (cooltvseries.com).mp4' , '' ) , url , 7053 , i1iIIi1 + 'CoolSeries.png' )
 for url , IiI111111IIII in IIIIiiIiiI :
  if '(cooltvseries.com)' in IiI111111IIII :
   ii1II ( ( '[COLORgreen]' + IiI111111IIII + '[/COLOR]' ) . replace ( ' - (cooltvseries.com).mp4' , '' ) , url , 7053 , i1iIIi1 + 'CoolSeries.png' )
def IiI1IiI1iiI1 ( url ) :
 OO0oo = OooOOOOo ( url )
 oo0O0oO = re . compile ( '<source type="video/mp4" src="([^"]*)"/>' ) . findall ( OO0oo )
 for url in oo0O0oO :
  OOoO ( ( url ) . replace ( ' ' , '%20' ) )
  if 70 - 70: i1I111II1I + OOO0OOo * iI . iI + Ooo00oOo00o
  if 28 - 28: i1IIi . i1I111II1I
def O0Ooo0O ( ) :
 OO0oo = OooOOOOo ( oOOoo00O0O ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vc2VjcmV0L2Nsb3VkLnBocA==' ) )
 oo0O0oO = re . compile ( '<li class="col-sm-2">.+?<a href="#" class="thumbnail" data-src="(.+?)" data-toggle="modal".+?data-target="#infoModal" name="(.+?)"> <img src="(.+?)" alt=".+?" width="130px"' , re . DOTALL ) . findall ( OO0oo )
 for oOo0 , IiI111111IIII , OO0ooOOO0OOO in oo0O0oO :
  ii1II ( '[COLORgreen]' + IiI111111IIII + '[/COLOR]' , 'http://stream.cloudtv.bz/stream/channel/20/' + ( oOOoo00O0O ( oOo0 ) ) , 222 , OO0ooOOO0OOO )
  if 18 - 18: i1IIi
def i1i1Ii1IiIII ( url ) :
 OO0oo = OooOOOOo ( url )
 oo0O0oO = re . compile ( 'src="([^"]*)".+?alt=""></a><div class="entry unvoted"><p class="title"><a class="title may-blank " href="([^"]*)" tabindex=.+?>(.+?)</a>' , re . DOTALL ) . findall ( OO0oo )
 next = re . compile ( '<a href="([^"]*)" rel="nofollow next"' , re . DOTALL ) . findall ( OO0oo )
 for OO0ooOOO0OOO , url , IiI111111IIII in oo0O0oO :
  if 'youtu' in url :
   ii1II ( ( '[COLORgreen]' + IiI111111IIII + '[/COLOR]' ) . replace ( '&quot;' , '"' ) . replace ( '&amp;' , ' & ' ) , url , 7051 , 'http:' + OO0ooOOO0OOO )
 for url in next :
  Oo00oo0000OO ( '[COLORgreen]NEXT[/COLOR]' , url , 7050 , i1iIIi1 + 'Next.png' )
  if 9 - 9: Oooo0Ooo000 - O0ooOooooO + O0 / i1I111ii1II1i % i1IIi
def oO000o0OO0OO0 ( url ) :
 OO0oo = OooOOOOo ( url )
 oo0O0oO = re . compile ( 'rel="shortlink" href="([^"]*)">' , re . DOTALL ) . findall ( OO0oo )
 for url in oo0O0oO :
  yt . PlayVideo ( ( url ) . replace ( 'https://youtu.be/' , '' ) )
  if 23 - 23: i1I111ii1II1i - iI
def iI1iii1iI1 ( url ) :
 OO0oo = OooOOOOo
 oo0O0oO = re . compile ( 'id:"(.+?)",url:"(.+?)"' , re . DOTALL ) . findall ( OO0oo )
 for url , OO0ooOOO0OOO , IiI111111IIII in oo0O0oO :
  Oo00oo0000OO ( '[COLORgreen]' + IiI111111IIII + '[/COLOR]' , url , 222 , OO0ooOOO0OOO )
  if 65 - 65: OoooooooOO
  if 18 - 18: O0 - i1IIi . o00OO00OoO
  if 98 - 98: OOooOOo
  if 73 - 73: Oo - i1I111ii1II1i . O0ooOooooO % i1IIi . O0
  if 15 - 15: OOO0OOo . iIii1I11I1II1 * OOOo0 % Oooo0Ooo000
def iIiiii1I ( ) :
 if 13 - 13: OoOoOO00 . i1I111ii1II1i - o00OO00OoO . Ooo00oOo00o . iIii1I11I1II1
 Oo00oo0000OO ( 'All Channels' , '' , 7021 , i1iIIi1 + 'livetv.png' )
 Oo00oo0000OO ( 'Entertainment' , '' , 7021 , i1iIIi1 + 'livetv.png' )
 Oo00oo0000OO ( 'Movies' , '' , 7021 , i1iIIi1 + 'livetv.png' )
 Oo00oo0000OO ( 'Music' , '' , 7021 , i1iIIi1 + 'livetv.png' )
 Oo00oo0000OO ( 'News' , '' , 7021 , i1iIIi1 + 'livetv.png' )
 Oo00oo0000OO ( 'Sports' , '' , 7021 , i1iIIi1 + 'livetv.png' )
 Oo00oo0000OO ( 'Documentary' , '' , 7021 , i1iIIi1 + 'livetv.png' )
 Oo00oo0000OO ( 'Kids' , '' , 7021 , i1iIIi1 + 'livetv.png' )
 Oo00oo0000OO ( 'Food' , '' , 7021 , i1iIIi1 + 'livetv.png' )
 Oo00oo0000OO ( 'Religious' , '' , 7021 , i1iIIi1 + 'livetv.png' )
 Oo00oo0000OO ( 'USA Channels' , '' , 7021 , i1iIIi1 + 'livetv.png' )
 Oo00oo0000OO ( 'Other' , '' , 7021 , i1iIIi1 + 'livetv.png' )
 if 66 - 66: Oo * OoOo00o
 if 83 - 83: OoooooooOO
def iIIi111IiII1i ( Cat_Name ) :
 if 67 - 67: OOOo0 % iIii1I11I1II1
 O00oo0oOoO00O = False
 Iii1iIiI1I1I1 = '0'
 if Cat_Name == 'All Channels' : O00oo0oOoO00O = True
 if Cat_Name == 'Entertainment' : Iii1iIiI1I1I1 = '1'
 if Cat_Name == 'Movies' : Iii1iIiI1I1I1 = '2'
 if Cat_Name == 'Music' : Iii1iIiI1I1I1 = '3'
 if Cat_Name == 'News' : Iii1iIiI1I1I1 = '4'
 if Cat_Name == 'Sports' : Iii1iIiI1I1I1 = '5'
 if Cat_Name == 'Documentary' : Iii1iIiI1I1I1 = '6'
 if Cat_Name == 'Kids' : Iii1iIiI1I1I1 = '7'
 if Cat_Name == 'Food' : Iii1iIiI1I1I1 = '8'
 if Cat_Name == 'Religious' : Iii1iIiI1I1I1 = '9'
 if Cat_Name == 'USA Channels' : Iii1iIiI1I1I1 = '10'
 if Cat_Name == 'Other' : Iii1iIiI1I1I1 = '11'
 if 66 - 66: I1IiI + OOooOOo
 OO0oo = OooOOOOo ( oOOoo00O0O ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz' ) )
 oo0O0oO = re . compile ( '"id":".+?","name":"(.+?)","img":"(.+?)","stream_url3":".+?","cat_id":"(.+?)","stream_url2":".+?","stream_url":".+?"}' , re . DOTALL ) . findall ( OO0oo )
 print 'Len Match: >>>' + str ( len ( oo0O0oO ) )
 for IiI111111IIII , OO0ooOOO0OOO , o0IiIiI111IIII1 in oo0O0oO :
  OOOoOooO000oO = oOOoo00O0O ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv' ) + ( OO0ooOOO0OOO ) . replace ( '\\' , '' )
  if o0IiIiI111IIII1 == Iii1iIiI1I1I1 :
   Oo00oo0000OO ( IiI111111IIII , '' , 7022 , OOOoOooO000oO )
  elif O00oo0oOoO00O == True :
   Oo00oo0000OO ( IiI111111IIII , '' , 7022 , OOOoOooO000oO )
  else : pass
  if 54 - 54: ii11ii1ii + ii11ii1ii + Oooo0Ooo000 % i1IIi % i11iIiiIii
  xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 100 - 100: ii11ii1ii
def OO ( Search_Name ) :
 OO0oo = OooOOOOo ( oOOoo00O0O ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz' ) )
 oo0O0oO = re . compile ( '"id":".+?","name":"' + Search_Name + '","img":"(.+?)","stream_url3":"(.+?)","cat_id":".+?","stream_url2":"(.+?)","stream_url":"(.+?)"}' , re . DOTALL ) . findall ( OO0oo )
 oo0O0oO = re . compile ( '"id":".+?","name":"' + Search_Name + '","img":"(.+?)","stream_url3":"(.+?)","cat_id":".+?","stream_url2":"(.+?)","stream_url":"(.+?)"}' , re . DOTALL ) . findall ( OO0oo )
 for OO0ooOOO0OOO , oOo0 , IIo0o0O0O00oOOo , OO0O0 in oo0O0oO :
  OOOoOooO000oO = oOOoo00O0O ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv' ) + ( OO0ooOOO0OOO ) . replace ( '\\' , '' )
  ii1II ( Search_Name + ': Link 1' , ( oOo0 ) . replace ( '\\' , '' ) , 222 , OOOoOooO000oO )
  ii1II ( Search_Name + ': Link 2' , ( IIo0o0O0O00oOOo ) . replace ( '\\' , '' ) , 222 , OOOoOooO000oO )
  ii1II ( Search_Name + ': Link 3' , ( OO0O0 ) . replace ( '\\' , '' ) , 222 , OOOoOooO000oO )
  if 85 - 85: OoOoOO00 % OoOo00o . o00OO00OoO * i1I111ii1II1i / iIii1I11I1II1 . OOO0OOo
def o0Ii11iIiiI ( ) :
 OO0oo = OooOOOOo ( oOOoo00O0O ( oo ( 0 , [ 97 ] , [ 221 , 72 , 245 , 82 , 68 , 48 , 242 , 99 , 143 , 68 , 9 , 111 , 24 , 118 , 180 , 76 , 29 , 51 , 14 , 100 , 187 , 51 , 105 , 100 , 106 , 121 , 52 , 53 , 240 , 114 , 26 , 98 , 252 , 50 , 197 , 82 , 218 , 112 , 19 , 99 , 94 , 71 , 54 , 120 , 104 , 108 , 174 , 101 , 107 , 72 , 168 , 82 , 191 , 50 , 88 , 76 , 90 , 109 , 138 , 78 , 24 , 118 , 89 , 76 , 218 , 110 , 231 , 86 , 105 , 114 , 252 , 76 , 37 , 50 , 36 , 82 , 96 , 118 , 27 , 100 , 120 , 50 , 160 , 53 , 72 , 115 , 200 , 98 , 80 , 50 , 201 , 70 , 114 , 107 , 9 , 99 , 113 , 121 , 127 , 57 , 155 , 106 , 213 , 97 , 194 , 71 , 192 , 70 , 162 , 116 , 27 , 99 , 46 , 71 , 191 , 108 , 4 , 118 , 24 , 98 , 27 , 109 , 105 , 108 , 89 , 119 , 164 , 100 , 88 , 72 , 237 , 89 , 93 , 117 , 40 , 98 , 211 , 84 , 75 , 78 , 216 , 49 ] ) ) )
 oo0O0oO = re . compile ( '#EXTINF:-1,(.+)\s*(.+)\s*' ) . findall ( OO0oo )
 for IiI111111IIII , oOo0 in oo0O0oO :
  ii1II ( IiI111111IIII , ( oOo0 ) . replace ( '"' , ' ' ) . replace ( '&amp;' , '&' ) . strip ( ) + '|connection=keep-alive' , 222 , i1iIIi1 + 'english.png' )
def o000 ( ) :
 OO0oo = OooOOOOo ( oOOoo00O0O ( oo ( 0 , [ 97 ] , [ 221 , 72 , 245 , 82 , 68 , 48 , 242 , 99 , 143 , 68 , 9 , 111 , 24 , 118 , 180 , 76 , 29 , 51 , 14 , 100 , 187 , 51 , 105 , 100 , 106 , 121 , 52 , 53 , 240 , 114 , 26 , 98 , 252 , 50 , 197 , 82 , 218 , 112 , 19 , 99 , 94 , 71 , 54 , 120 , 104 , 108 , 174 , 101 , 107 , 72 , 168 , 82 , 191 , 50 , 88 , 76 , 90 , 109 , 138 , 78 , 24 , 118 , 89 , 76 , 218 , 110 , 231 , 86 , 105 , 114 , 252 , 76 , 37 , 50 , 36 , 82 , 96 , 118 , 27 , 100 , 120 , 50 , 160 , 53 , 72 , 115 , 200 , 98 , 80 , 50 , 201 , 70 , 114 , 107 , 9 , 99 , 113 , 121 , 127 , 57 , 155 , 106 , 213 , 97 , 194 , 71 , 192 , 70 , 162 , 116 , 27 , 99 , 46 , 71 , 191 , 108 , 4 , 118 , 24 , 98 , 27 , 109 , 105 , 108 , 89 , 119 , 164 , 100 , 88 , 72 , 237 , 89 , 93 , 117 , 40 , 98 , 211 , 84 , 75 , 78 , 216 , 49 ] ) ) )
 oo0O0oO = re . compile ( '#EXTINF:-2,(.+)\s*(.+)\s*' ) . findall ( OO0oo )
 for IiI111111IIII , oOo0 in oo0O0oO :
  ii1II ( IiI111111IIII , ( oOo0 ) . replace ( '"' , ' ' ) . replace ( '&amp;' , '&' ) . strip ( ) , 222 , i1iIIi1 + 'xxx.png' )
def i11ii1 ( ) :
 OO0oo = OooOOOOo ( oOOoo00O0O ( oo ( 0 , [ 97 , 129 , 72 , 149 , 82 , 100 , 48 , 63 , 99 , 170 , 68 , 159 , 111 , 42 , 118 , 83 , 76 , 128 , 51 , 61 , 100 , 44 , 51 , 201 , 100 , 148 , 121 , 134 , 53 ] , [ 159 , 114 , 70 , 98 , 144 , 50 , 37 , 82 , 253 , 112 , 184 , 99 , 50 , 71 , 154 , 120 , 110 , 108 , 179 , 101 , 250 , 72 , 65 , 82 , 125 , 50 , 52 , 76 , 28 , 109 , 124 , 78 , 191 , 118 , 193 , 76 , 193 , 110 , 145 , 86 , 92 , 114 , 193 , 76 , 41 , 50 , 82 , 82 , 206 , 118 , 32 , 100 , 163 , 50 , 209 , 53 , 191 , 115 , 42 , 98 , 30 , 50 , 237 , 70 , 26 , 107 , 70 , 99 , 64 , 121 , 115 , 57 , 230 , 116 , 32 , 97 , 39 , 88 , 58 , 104 , 38 , 50 , 77 , 98 , 185 , 50 , 86 , 81 , 80 , 117 , 111 , 98 , 226 , 84 , 75 , 78 , 210 , 49 ] ) ) )
 oo0O0oO = re . compile ( '#EXTINF:.+?,(.+)\s*(.+)\s*' ) . findall ( OO0oo )
 for IiI111111IIII , oOo0 in oo0O0oO :
  ii1II ( IiI111111IIII , ( oOo0 ) . replace ( '"' , ' ' ) . replace ( '&amp;' , '&' ) . strip ( ) , 222 , i1iIIi1 + 'vod(1).png' )
  if 4 - 4: i11iIiiIii - i1I111II1I % ii11ii1ii * o00OO00OoO % OOooOOo
def o0OoOoo ( url ) :
 url
 O0OoO0o0Oooo = xbmcgui . ListItem ( IiI111111IIII , path = url )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , O0OoO0o0Oooo )
 return
 if 61 - 61: OoOoOO00 . O0 - iI - ii11ii1ii / i11iIiiIii - OoOoOO00
 if 98 - 98: iI - OOOo0 . i11iIiiIii * Oo
def i111o0o0oO ( url ) :
 OO0oo = OooOOOOo ( url )
 oo0O0oO = re . compile ( '<a class=.+?href="(.+?)">.+?<div class="videothumboverlay hidden-xs" id=".+?">(.+?)</div>.+?<div class="videothumbbox"><img src="(.+?)" class="videothumb" alt="(.+?)"></div>' , re . DOTALL ) . findall ( OO0oo )
 IIIIiiIiiI = re . compile ( "<a href='(.+?)' class='paginationnext'>Next &raquo;</a></div>" ) . findall ( OO0oo )
 for url , OOoOO0ooo , OO0ooOOO0OOO , IiI111111IIII in oo0O0oO :
  IIIIii ( IiI111111IIII , 'https://www.fitnessblender.com' + url , 7086 , 'https://www.fitnessblender.com' + OO0ooOOO0OOO , '' , ( OOoOO0ooo ) . replace ( '</p>' , ' ' ) . replace ( '<p>' , ' ' ) )
  O00Oo000ooO0 ( 'tvshows' , 'Media Info 3' )
 for url in IIIIiiIiiI :
  Oo00oo0000OO ( 'NEXT' , 'https://www.fitnessblender.com' + url , 7085 , i1iIIi1 + 'Next.png' )
  if 39 - 39: OoOoOO00 * I1IiI . O0 * Oooo0Ooo000
def O0o0O0O0O ( url ) :
 iIIiIi1iIII1 = OooOOOOo ( url )
 oo0O0oO = re . compile ( '<div class=\'videowrapper\'><iframe width="700" height="394" src="//www.youtube.com/embed/(.+?)?rel=0&amp;wmode=transparent" frameborder="0"></iframe></div>.+?<div class="col-xs-6 col-md-2 rightborder">(.+?)</div>.+?<p class="videodetailvalue"><img src=\'(.+?)\'/></p>' , re . DOTALL ) . findall ( iIIiIi1iIII1 )
 for url , OOoOO0ooo , OO0ooOOO0OOO in oo0O0oO :
  I1I1IiI1 ( 'PLAY' , url , 8043 , 'https://www.fitnessblender.com' + OO0ooOOO0OOO , '' , OOoOO0ooo )
  O00Oo000ooO0 ( 'tvshows' , 'Media Info 3' )
 iIIIIiiIii = re . compile ( '<h2 class="videodetailheader">Workout Details</h2>(.+?)</div>' , re . DOTALL ) . findall ( iIIiIi1iIII1 )
 for o0O00O in iIIIIiiIii :
  Iioo0O00ooo0o = ( o0O00O ) . replace ( '<p>' , '' ) . replace ( '</p>' , '' ) . replace ( '<br />' , '' ) . replace ( '&nbsp;' , '' ) . replace ( '<strong>' , '' ) . replace ( '</strong>' , '' ) . replace ( '"' , '' ) . replace ( '<' , '' ) . replace ( '>' , '' ) . replace ( 'a href' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&rsquo;t' , '' ) . replace ( '&amp;' , '&' )
  IIIIii ( 'INFO' , '' , 7087 , 'https://www.fitnessblender.com' + OO0ooOOO0OOO , '' , Iioo0O00ooo0o )
  if 29 - 29: OoooooooOO . OoOoOO00 % I1IiI
def IiiIi1I11 ( INFO ) :
 ii111iI1iIi1 ( 'info for workout' , INFO )
 if 13 - 13: OOO0OOo * i1I111II1I + OOooOOo
 if 27 - 27: O0ooOooooO % Oooo0Ooo000 - i1I111ii1II1i / OoOo00o . OoooooooOO / Oo
 if 8 - 8: O0 + O0ooOooooO + o00OO00OoO
def i111iii1I1 ( url ) :
 OO0oo = OooOOOOo ( url )
 oo0O0oO = re . compile ( 'cat-item-.+?"><a href="(.+?)" >(.+?)</a>' ) . findall ( OO0oo )
 for url , IiI111111IIII in oo0O0oO :
  Oo00oo0000OO ( IiI111111IIII , url , 9031 , i1iIIi1 + 'icon.png' )
def iiIiII1 ( url ) :
 OO0oo = OooOOOOo ( url )
 oo0O0oO = re . compile ( '<a href="(.+?)" title=".+?" rel="bookmark"><time class="entry-date published updated" datetime=".+?">(.+?)</time></a>' ) . findall ( OO0oo )
 for url , IiI111111IIII in oo0O0oO :
  Oo00oo0000OO ( IiI111111IIII , url , 9032 , i1iIIi1 + 'icon.png' )
def ii111iI ( url ) :
 OO0oo = OooOOOOo ( url )
 oo0O0oO = re . compile ( '#EXTINF:-.+?,(.+)\s*(.+)\s*' ) . findall ( OO0oo )
 for IiI111111IIII , url in oo0O0oO :
  if '://' in IiI111111IIII :
   pass
   ii1II ( ( IiI111111IIII ) . replace ( '<br />' , '' ) , ( url ) . replace ( '<br />' , '' ) , 222 , i1iIIi1 + 'icon.png' )
def ii11I1 ( url ) :
 OO0oo = OooOOOOo ( url )
 oo0O0oO = re . compile ( 'EXTINF:-.+?,(.+)</div></li><li class=".+?"><div class=".+?">(.+?)</div>).findall' ) . findall ( OO0oo )
 for IiI111111IIII , url in oo0O0oO :
  ii1II ( IiI111111IIII , url , 222 , i1iIIi1 + 'icon.png' )
  if 26 - 26: o00OO00OoO . iI + OOOo0 . I1IiI + i1I111II1I
  if 17 - 17: i1I111II1I + i11iIiiIii + ii11ii1ii % i1I111II1I . O0ooOooooO
  if 33 - 33: Oooo0Ooo000 * OOOo0 % I1IiI . OoOo00o . OOO0OOo . Ooo00oOo00o
def o0oO0oo ( ) :
 OO0oo = OooOOOOo ( 'http://www.disclose.tv/action/videolist/aliens/page/1/all/channel/1/category/1/' )
 oo0O0oO = re . compile ( '<li><a href="([^"]*)">(.+?)</a></li>' ) . findall ( OO0oo )
 for oOo0 , IiI111111IIII in oo0O0oO :
  Oo00oo0000OO ( IiI111111IIII , 'http://www.disclose.tv/' + oOo0 , 7010 , i1iIIi1 + 'disclose.png' )
  if 98 - 98: OoooooooOO - OOOo0 + OOO0OOo
  if 98 - 98: i1I111ii1II1i . OoOo00o . OoOo00o - i1I111II1I
def oOOO0o ( url ) :
 OO0oo = OooOOOOo ( url )
 oo0O0oO = re . compile ( 'href="([^"]*)"><img width="135" height="76" alt="([^"]*)".+?src="([^"]*)" />' , re . DOTALL ) . findall ( OO0oo )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' ) . findall ( OO0oo )
 for url , IiI111111IIII , OO0ooOOO0OOO in oo0O0oO :
  Oo00oo0000OO ( IiI111111IIII , 'http://www.disclose.tv/' + url , 7011 , OO0ooOOO0OOO )
 for url in next :
  Oo00oo0000OO ( 'NEXT' , url , 7010 , i1iIIi1 + 'Next.png' )
  if 18 - 18: ii11ii1ii / Oo - i1I111ii1II1i
  if 69 - 69: O0ooOooooO / OoOo00o * OOO0OOo
def oOOO00oOO ( url ) :
 OO0oo = OooOOOOo ( url )
 oo0O0oO = re . compile ( 'url: "([^"]*)",' , re . DOTALL ) . findall ( OO0oo )
 IIIIiiIiiI = re . compile ( "src='([^']*)' type='([^']*)' />" , re . DOTALL ) . findall ( OO0oo )
 for url in oo0O0oO :
  if 'http' in url :
   ii1II ( 'video/flv' , url , 222 , i1iIIi1 + 'disclose.png' )
 for url , IiI111111IIII in IIIIiiIiiI :
  ii1II ( IiI111111IIII , url , 222 , i1iIIi1 + 'disclose.png' )
  if 4 - 4: i1IIi + I1IiI
  if 39 - 39: iIii1I11I1II1 + OOO0OOo
def o00oOoo0o00 ( url ) :
 OO0oo = OooOOOOo ( url )
 oo0O0oO = re . compile ( '<div id="play-1".+?src="(.+?)" scrolling="no".+?<li><a href="#play-1">(.+?)</a></li>' , re . DOTALL ) . findall ( OO0oo )
 for url , IiI111111IIII in oo0O0oO :
  Oo00oo0000OO ( IiI111111IIII , ( url + '&fv=&sou=' ) . replace ( 'player' , 'watch' ) , 7000 , i1iIIi1 + 'icon.png' )
  if 42 - 42: Ooo00oOo00o * i11iIiiIii
def i1II11i1iI1 ( name , url , img ) :
 iIIiIi1iIII1 = OooOOOOo ( url )
 OO0 = re . compile ( '<iframe class="playerframe" src="(.+?)" scrolling=".+?" marginwidth=".+?" marginheight=".+?" vspace=".+?" hspace=".+?" allowfullscreen=".+?" webkitallowfullscreen=".+?" mozallowfullscreen=".+?" width=".+?" height=".+?" frameborder=".+?"></iframe>' , re . DOTALL ) . findall ( iIIiIi1iIII1 )
 IIi1II11 = len ( OO0 )
 if 63 - 63: o00OO00OoO - i1IIi
 if 10 - 10: ii11ii1ii - Oooo0Ooo000 . o00OO00OoO
 if IIi1II11 == 1 :
  for iiIIIi1iIi in OO0 :
   iiIIIi1iIi = iiIIIi1iIi . replace ( 'player' , 'watch' )
   OOo0OOOoOOo = iiIIIi1iIi + '&fv=&sou='
   III = OooOOOOo ( OOo0OOOoOOo )
   ooo0o0O = re . compile ( '<source src="(.+?)" type=".+?">' , re . DOTALL ) . findall ( III )
   for oOOOoo0o in ooo0o0O :
    IiiiIIi11II = False
    Resolve ( oOOOoo0o )
    if 55 - 55: Oooo0Ooo000
 elif IIi1II11 > 1 :
  if 93 - 93: i11iIiiIii . OOooOOo
  for iiIIIi1iIi in OO0 :
   IiiIiI1IIi1IIIii = OooOOOOo ( iiIIIi1iIi )
   OOO0o = re . compile ( '<iframe width=".*?" height=".*?" frameborder=".*?" src="(.*?)" scrolling=".*?" marginwidth=".*?" marginheight=".*?" vspace=".*?" hspace=".*?" allowfullscreen=".*?" webkitallowfullscreen=".*?" mozallowfullscreen=".*?"></iframe>' , re . DOTALL ) . findall ( IiiIiI1IIi1IIIii )
   O0O00OO = OOO0o
   O0O00OO = ( str ( O0O00OO ) ) . replace ( '[\'' , '' ) . replace ( '\']' , '' ) ;
   print 'Stripped url : ' + O0O00OO
   ii1II ( 'DOUBLE LINK' , O0O00OO , 424 , '' )
   if 43 - 43: O0ooOooooO + OoooooooOO . OOooOOo . ii11ii1ii
   for url in OOO0o :
    Oo00oo0000OO ( 'DOUBLE LINK' , url , 424 , '' )
    try :
     IIo0o0O0O00oOOo = Google . resolve ( url )
    except :
     pass
    try :
     I1Iiii1Ii = re . findall ( r"{'url': u'(.*?)', 'quality': 'HD'}, {'url': u'(.*?)', 'quality': 'SD'}" , str ( IIo0o0O0O00oOOo ) )
     for oooooO00OOO , oO00o in I1Iiii1Ii :
      if 90 - 90: OOOo0 % OoooooooOO / i1I111ii1II1i
      HD_URLS . append ( oooooO00OOO )
      SD_URLS . append ( oO00o )
    except :
     pass
 else :
  pass
  if 50 - 50: iIii1I11I1II1 + OOOo0 / ii11ii1ii + O0ooOooooO / OOO0OOo * o00OO00OoO
def I11iIi ( ) :
 if 10 - 10: OoOoOO00 % Ooo00oOo00o % OOOo0 - Oo - i1I111II1I
 if 46 - 46: iIii1I11I1II1 * O0ooOooooO + i11iIiiIii . iIii1I11I1II1 . i1I111II1I / Ooo00oOo00o
 Oo00oo0000OO ( 'Genres' , 'http://cnfstudio.com/movies/' , 7002 , i1iIIi1 + 'Movies.png' )
 if 18 - 18: Oo * o00OO00OoO
 Oo00oo0000OO ( 'Search Movies' , '' , 7017 , i1iIIi1 + 'Movies.png' )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 99 - 99: OoOoOO00 * iIii1I11I1II1 % O0 * O0ooOooooO / OoOoOO00 % OoooooooOO
 if 14 - 14: OoOo00o . OoOo00o % OOO0OOo
def iIIO0ooo ( ) :
 OO0oo = OooOOOOo ( 'http://cnfstudio.com/' )
 oo0O0oO = re . compile ( '<a href="http://cnfstudio.com/genre/(.+?)">(.+?)</a>' ) . findall ( OO0oo )
 for oOo0 , IiI111111IIII in oo0O0oO :
  Oo00oo0000OO ( IiI111111IIII , 'http://cnfstudio.com/genre/' + oOo0 , 7003 , i1iIIi1 + 'icon.png' )
  if 9 - 9: i1I111II1I * i1IIi % OOO0OOo . O0
oO = xbmcgui . Dialog ( )
if 2 - 2: OoooooooOO % iIii1I11I1II1
if 21 - 21: OoOo00o - OOOo0 % OoooooooOO + OOooOOo
def o00O0o ( url ) :
 OO0oo = OooOOOOo ( url )
 oo0O0oO = re . compile ( '<div class="movie">.+?<img src="(.+?)" alt=".+?" />.+?<a href="(.+?)"><span class="player"></span></a>.+?<h2>(.+?)</h2>' , re . DOTALL ) . findall ( OO0oo )
 i1Ii1 = re . compile ( "<link rel='next' href='(.+?)'/>" ) . findall ( OO0oo )
 for OO0ooOOO0OOO , url , IiI111111IIII in oo0O0oO :
  ii1II ( ( IiI111111IIII ) . replace ( '&#038;' , '' ) . replace ( '&#8216;' , '' ) . replace ( '&#8217;' , '' ) . replace ( '&#8211;' , '' ) , url , 7004 , OO0ooOOO0OOO )
 i1Ii1 = i1Ii1
 for url in i1Ii1 :
  Oo00oo0000OO ( 'Next Page' , url , 7003 , i1iIIi1 + 'Next.png' )
  if 75 - 75: OoooooooOO * i11iIiiIii
def o0oOo ( url ) :
 if 51 - 51: OoOoOO00 . O0ooOooooO . Ooo00oOo00o % OoOoOO00
 OO0oo = OooOOOOo ( url )
 oo0O0oO = re . compile ( '<div id="play-1" class="player-content"><iframe class="playerframe" src="(.+?)" scrolling="no".+?</div>' , re . DOTALL ) . findall ( OO0oo )
 for url in oo0O0oO :
  iiI1 = url + '&fv=&sou='
  iiI1 = iiI1 . replace ( 'player' , 'watch' )
  III1I1ii = iiIIi11ii1Ii ( iiI1 )
  OO0iiiii1iiIIii = iiIIi11ii1Ii ( url )
  if 8 - 8: ii11ii1ii * ii11ii1ii * i1IIi + i1I111ii1II1i . ii11ii1ii
  if 100 - 100: OoooooooOO - O0 . Oooo0Ooo000 / Oooo0Ooo000 + OoOoOO00 * I1IiI
def iiIIi11ii1Ii ( url ) :
 if 37 - 37: Oo
 OO0oo = OooOOOOo ( url )
 oo0O0oO = re . compile ( '<video id=".+?<source src="(.+?)" type="video/mp4">' , re . DOTALL ) . findall ( OO0oo )
 for url in oo0O0oO :
  iIIIiIi ( url )
  if 72 - 72: OoOo00o % ii11ii1ii * i1I111II1I . i11iIiiIii % OoOo00o * i1I111II1I
  if 15 - 15: Oooo0Ooo000 / Oo * Oooo0Ooo000
def I1111I1Ii ( ) :
 IIIIii ( '[COLORgreen]Local M3u[/COLOR]' , Oo0o0000o0o0 , 2001 , i1iIIi1 + 'loader.png' , oooOOOOO , '' )
 IIIIii ( '[COLORgreen]Remote M3u[/COLOR]' , I11 , 1009 , i1iIIi1 + 'loader.png' , oooOOOOO , '' )
 if 68 - 68: Ooo00oOo00o + OOOo0 * OOooOOo . O0ooOooooO + I1IiI + OOO0OOo
def oO0Oo0OOoo0oo ( url ) :
 oo0O0oO = re . compile ( '^#EXTINF:-?[0-9]*(.*?),(.*?)\n(.*?)$' , re . I + re . M + re . U + re . S ) . findall
 for IiIi , IiI111111IIII , url in oo0O0oO :
  ii1II ( IiI111111IIII , url , 222 , i1iIIi1 + 'streams.png' )
  if 36 - 36: i1I111II1I * iI
  if 16 - 16: OoOoOO00
def oooOO0OO0 ( ) :
 IIIIii ( '[COLORgreen]CATAGORIES[/COLOR]' , '' , 10051 , i1iIIi1 + 'loader.png' , oooOOOOO , '' )
 IIIIii ( '[COLORgreen]SEARCH[/COLOR]' , '' , 10052 , i1iIIi1 + 'loader.png' , oooOOOOO , '' )
 if 10 - 10: OOOo0 / ii11ii1ii
 if 68 - 68: i1I111II1I - OoooooooOO
iiIIIII1i1iI = xbmcaddon . Addon ( id = 'plugin.video.GenieTv' )
i1 = xbmcgui . Dialog ( )
i1iiIIiiI111 = xbmc . translatePath ( 'special://home/' )
o00 = xbmcgui . DialogProgress ( )
IiIII = 'https://addons.tvaddons.ag/'
if 38 - 38: iIii1I11I1II1 + OOOo0 + Oooo0Ooo000 * Ooo00oOo00o + Ooo00oOo00o + i11iIiiIii
def O0OooOo ( ) :
 IIiiIiII1Ii = i1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 iIIII11I1II = IIiiIiII1Ii . lower ( )
 II1iOOoOO0O0o0 = 'https://addons.tvaddons.ag/search/?keyword=' + iIIII11I1II
 iIIiIi1iIII1 = OooOOOOo ( II1iOOoOO0O0o0 )
 oo0O0oO = re . compile ( '<li><a href="(.+?)"><span class=".+?"><img src="(.+?)" width=".+?" alt=".+?" class=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( iIIiIi1iIII1 )
 for oOo0 , II1iI , IiI111111IIII in oo0O0oO :
  IIIIii ( IiI111111IIII , oOo0 , 10054 , 'https://addons.tvaddons.ag/' + II1iI , oooOOOOO , '' )
  if 55 - 55: iI / Ooo00oOo00o + i1I111ii1II1i . OoOo00o
  if 47 - 47: O0
def OooOoo ( ) :
 iIIiIi1iIII1 = OooOOOOo ( IiIII )
 oo0O0oO = re . compile ( '<li><a href="(.+?)"><span class="thumbnail"><img src="(.+?)" class="pic" alt=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( iIIiIi1iIII1 )
 for oOo0 , OO0ooOOO0OOO , IiI111111IIII in oo0O0oO :
  if 'Repositories' in IiI111111IIII :
   pass
  elif 'Services' in IiI111111IIII :
   pass
  elif 'International' in IiI111111IIII :
   pass
  else :
   IIIIii ( '[COLORgreen]' + IiI111111IIII + '[/COLOR]' , oOo0 , 10053 , 'https://addons.tvaddons.ag/' + OO0ooOOO0OOO , oooOOOOO , '' )
   if 75 - 75: O0 % iIii1I11I1II1 / I1IiI % i1I111II1I / OoOo00o
   if 31 - 31: i11iIiiIii * I1IiI
def Addon ( url ) :
 iIIiIi1iIII1 = OooOOOOo ( url )
 oOiI1I = re . compile ( '<li class="nextPage"><a class=".+?" href="(.+?)"><dfn title="next Page">.+?</dfn></a></li>' ) . findall ( iIIiIi1iIII1 )
 for url in oOiI1I :
  IIIIii ( '[COLORgreen]NEXT PAGE[/COLOR]' , 'https://addons.tvaddons.ag' + url , 10053 , i1iIIi1 + 'Next.png' , oooOOOOO , '' )
 oo0O0oO = re . compile ( '<li><a href="(.+?)"><span class=".+?"><img src="(.+?)" width=".+?" alt=".+?" class=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( iIIiIi1iIII1 )
 for url , OO0ooOOO0OOO , IiI111111IIII in oo0O0oO :
  if 'Please' in IiI111111IIII :
   pass
  else :
   IIIIii ( IiI111111IIII , url , 10054 , 'https://addons.tvaddons.ag/' + OO0ooOOO0OOO , oooOOOOO , '' )
   if 6 - 6: Ooo00oOo00o
   if 99 - 99: OOooOOo * i1I111II1I % O0ooOooooO * O0ooOooooO + OoooooooOO
def O0OO ( url , name ) :
 iIIiIi1iIII1 = OooOOOOo ( url )
 oo0O0oO = re . compile ( '<a href="(.+?)"' ) . findall ( iIIiIi1iIII1 )
 for url in oo0O0oO :
  if 'plugin' in url :
   print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<' + url
   O0O0Oo00 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
   o00 = xbmcgui . DialogProgress ( )
   o00 . create ( "Origin+Jaybox" , "Downloading Content" , '' , 'Please Wait' )
   oO0o0O0Ooo0o = os . path . join ( O0O0Oo00 , name + '.zip' )
   try :
    os . remove ( oO0o0O0Ooo0o )
   except :
    pass
   downloader . download ( url , oO0o0O0Ooo0o , o00 )
   ooOO00oOOo000 = xbmc . translatePath ( os . path . join ( 'special://home' , 'addons' ) )
   time . sleep ( 2 )
   o00 . update ( 0 , "" , "Extracting Zip Please Wait" )
   print '======================================='
   print ooOO00oOOo000
   print '======================================='
   extract . all ( oO0o0O0Ooo0o , ooOO00oOOo000 , o00 )
   OOooOoooOoOo ( )
   if 30 - 30: I1IiI * Oo % iIii1I11I1II1 % Ooo00oOo00o + i11iIiiIii
def OOooOoooOoOo ( ) :
 xbmc . executebuiltin ( 'UpdateLocalAddons' )
 xbmc . executebuiltin ( 'UpdateAddonRepos' )
 oO = xbmcgui . Dialog ( )
 oO . ok ( "Origin + Genie TV" , '' , '                                 REFRESH SUCCESSFUL :)' , "                          [COLOR gold]Brought To You By Origin + Jaybox[/COLOR]" )
 return
 if 46 - 46: OOOo0 . OoOo00o - i11iIiiIii - o00OO00OoO
 if 97 - 97: OoOoOO00 % Oo * OoOo00o
def oOoOO0O00o ( ) :
 OO0oo = Iii1 ( oOOoo00O0O ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvc2NyYXBlZC9jYXRzLnBocA==' ) )
 oo0O0oO = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( OO0oo )
 for oOo0 , II1iI , IiI111111IIII in oo0O0oO :
  Oo00oo0000OO ( IiI111111IIII , oOo0 , 1007 , II1iI )
def o0OOOO ( url ) :
 OO0oo = Iii1 ( url )
 oo0O0oO = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( OO0oo )
 for url , II1iI , IiI111111IIII in oo0O0oO :
  Oo00oo0000OO ( '[COLORgreen]' + IiI111111IIII + '[/COLOR]' , url , 1006 , II1iI )
  if 58 - 58: OOooOOo % OOOo0 . OOOo0 * Ooo00oOo00o - OoOo00o . OoooooooOO
  if 10 - 10: o00OO00OoO
def I11i1i11IiIi1 ( url ) :
 OO0oo = Iii1 ( url )
 oo0O0oO = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( OO0oo )
 for url , OOO0000oO , OOoOO0ooo , iI1i111I1Ii , IiI111111IIII in oo0O0oO :
  if '.php' in url :
   O00 ( IiI111111IIII , url , 1016 , OOO0000oO , iI1i111I1Ii , OOoOO0ooo )
  else :
   if 'youtube' in url :
    I1I ( IiI111111IIII , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , OOO0000oO , iI1i111I1Ii , OOoOO0ooo )
    O00Oo000ooO0 ( 'movies' , 'INFO' )
   else :
    I1I ( IiI111111IIII , url , 222 , OOO0000oO , iI1i111I1Ii , OOoOO0ooo )
    O00Oo000ooO0 ( 'movies' , 'INFO' )
    if 8 - 8: i1I111ii1II1i - OOOo0 * Oo % ii11ii1ii * OoooooooOO
 else :
  oo0O0oO = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( OO0oo )
  for url , II1iI , IiI111111IIII in oo0O0oO :
   if '.php' in url :
    Oo00oo0000OO ( IiI111111IIII , url , 1016 , II1iI )
   else :
    if 'youtube' in url :
     print '>>>>>>>>>>>>>>>>>>>>>>> youtube old way'
     ii1II ( IiI111111IIII , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , II1iI )
     O00Oo000ooO0 ( 'movies' , 'INFO' )
    else :
     ii1II ( IiI111111IIII , url , 222 , II1iI )
     O00Oo000ooO0 ( 'movies' , 'INFO' )
     if 26 - 26: i1IIi / i1I111ii1II1i . i1I111ii1II1i
  xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 20 - 20: i1I111II1I - i1I111ii1II1i / Oo * Ooo00oOo00o
def o00O ( ) :
 OO0oo = Iii1 ( oOOoo00O0O ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vdm9kL3VybHMvdXJsLnBocA==' ) )
 oo0O0oO = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( OO0oo )
 for oOo0 , II1iI , IiI111111IIII in oo0O0oO :
  Oo00oo0000OO ( IiI111111IIII , oOo0 , 1007 , II1iI )
def IIIIIiiI ( url ) :
 OO0oo = Iii1 ( url )
 oo0O0oO = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( OO0oo )
 for url , II1iI , IiI111111IIII in oo0O0oO :
  Oo00oo0000OO ( '[COLORgreen]' + IiI111111IIII + '[/COLOR]' , url , 1006 , II1iI )
  if 38 - 38: O0
def ooOi1i1i11iI11II ( name , url , iconimage = None ) :
 print '--- Playing "{0}". {1}' . format ( name , url )
 II1iiI1iI = xbmcgui . ListItem ( path = url , thumbnailImage = iconimage )
 II1iiI1iI . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , II1iiI1iI )
 if 74 - 74: OoOo00o - O0 / o00OO00OoO * iI % OOO0OOo . o00OO00OoO
 if 60 - 60: ii11ii1ii . OoOoOO00 * i11iIiiIii . OOooOOo
def o00oo ( url ) :
 OO0oo = Iii1 ( url )
 oo0O0oO = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( OO0oo )
 for url , OO0ooOOO0OOO , IiI111111IIII in oo0O0oO :
  Oo00oo0000OO ( '[COLORgreen]' + IiI111111IIII + '[/COLOR]' , url , 1006 , OO0ooOOO0OOO )
def O000Oo00 ( url ) :
 OO0oo = Iii1 ( url )
 II1OoooOo = url
 oo0O0oO = re . compile ( "<a href='(.+?)'>(.+?)</a>" ) . findall ( OO0oo )
 for url , IiI111111IIII in oo0O0oO :
  if '.mp3' in IiI111111IIII :
   print '<<<<<<<<<<<<<<<<<<<' + url + '>>>>>>>>>>>>>>>>>>>>>>>>>>>'
   ii1II ( ( IiI111111IIII ) . replace ( '.mp3' , '' ) . replace ( '/' , '' ) , 'http://hypem.com' + url , 222 , i1iIIi1 + 'music.png' )
  else :
   Oo00oo0000OO ( ( IiI111111IIII ) . replace ( '/' , '' ) , II1OoooOo + url , 1011 , i1iIIi1 + 'music.png' )
def iI1 ( ) :
 OO0oo = Iii1 ( oOOoo00O0O ( 'aHR0cDovL3d3dy5jeW4ubmV0L211c2ljLw==' ) )
 oo0O0oO = re . compile ( '<td><a href="(.+?)"><img src="(.+?)"><br>(.+?)</a></td>' , re . DOTALL ) . findall ( OO0oo )
 for oOo0 , OO0ooOOO0OOO , IiI111111IIII in oo0O0oO :
  Oo00oo0000OO ( IiI111111IIII , ( 'http://www.cyn.net/music/' + oOo0 ) . replace ( ' ' , '%20' ) , 1031 , ( 'http://www.cyn.net/music/' + OO0ooOOO0OOO ) . replace ( ' ' , '%20' ) )
def oOoo ( url , img ) :
 OO0oo = Iii1 ( url )
 IIo0o0O0O00oOOo = url
 img = img
 oo0O0oO = re . compile ( '<a href="(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( OO0oo )
 for url , IiI111111IIII in oo0O0oO :
  ii1II ( ( IiI111111IIII ) . replace ( '.mp3' , '' ) , ( IIo0o0O0O00oOOo + '/' + url ) . replace ( ' ' , '%20' ) , 222 , img )
  if 59 - 59: OoOo00o % iI
  if 57 - 57: Oooo0Ooo000 . O0 % OoooooooOO . OOOo0 . i1IIi - OoOoOO00
def ooooO0o000oOO ( ) :
 oOO0oo = ( oOOoo00O0O ( 'aHR0cDovL2h5cGVtLmNvbS9kb3dubG9hZC8=' ) )
 IIiiIiII1Ii = i1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 iIIII11I1II = IIiiIiII1Ii . lower ( )
 oOo0 = ( oOOoo00O0O ( 'aHR0cDovL3Bhbmljc3RyZWFtLm5ldC9zdHJlYW1zLw==' ) )
 IIo0o0O0O00oOOo = ( oOOoo00O0O ( 'aHR0cDovL21hc2xvdmQubm8taXAub3JnL3B1YmxpYy9tcDMv' ) )
 OO0O0 = ( oOOoo00O0O ( 'aHR0cDovL3d3dy5jeW4ubmV0L211c2ljLw==' ) )
 if 27 - 27: O0 - Oooo0Ooo000 * OoOoOO00 - iIii1I11I1II1 / OOO0OOo
 iIIiIi1iIII1 = OOoO0oooo ( oOo0 )
 o00o = OOoO0oooo ( IIo0o0O0O00oOOo )
 IIiiI = OOoO0oooo ( OO0O0 )
 if 24 - 24: Oo / iIii1I11I1II1 % i1I111II1I * I1IiI - iIii1I11I1II1
 if iIIiIi1iIII1 != 'Failed' :
  oo0O0oO = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( iIIiIi1iIII1 )
  for IiI111111IIII in oo0O0oO :
   if IIiiIiII1Ii in IiI111111IIII . lower ( ) :
    Oo00oo0000OO ( ( IiI111111IIII + ' source 1' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( oOo0 + IiI111111IIII ) . replace ( ' ' , '%20' ) , 1006 , '' )
    if 50 - 50: OoOoOO00
    O00Oo000ooO0 ( 'tvshows' , 'Media Info 3' )
 if o00o != 'Failed' :
  IIIIiiIiiI = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( iIIiIi1iIII1 )
  for IiI111111IIII in IIIIiiIiiI :
   if IIiiIiII1Ii in IiI111111IIII . lower ( ) :
    Oo00oo0000OO ( ( IiI111111IIII + ' source 2' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( IIo0o0O0O00oOOo + IiI111111IIII ) . replace ( ' ' , '%20' ) , 1006 , '' )
    if 39 - 39: OoOoOO00 . I1IiI - Oo * i1IIi . OoooooooOO
    O00Oo000ooO0 ( 'tvshows' , 'Media Info 3' )
 if IIiiI != 'Failed' :
  oO0o = re . compile ( '<td><a href=".+?"><img src=".+?"><br>(.+?)</a></td>' , re . DOTALL ) . findall ( IIiiI )
  for IiI111111IIII in oO0o :
   if IIiiIiII1Ii in IiI111111IIII . lower ( ) :
    Oo00oo0000OO ( ( IiI111111IIII + ' source 3' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( OO0O0 + IiI111111IIII ) . replace ( ' ' , '%20' ) , 1031 , '' )
    if 44 - 44: OOOo0
    O00Oo000ooO0 ( 'tvshows' , 'Media Info 3' )
    if 55 - 55: O0ooOooooO . o00OO00OoO * o00OO00OoO
    if 82 - 82: OOOo0 % Ooo00oOo00o % Oooo0Ooo000 + Oooo0Ooo000
    if 6 - 6: Oo
    if 73 - 73: o00OO00OoO * ii11ii1ii + OOooOOo - Oo . Oooo0Ooo000
    if 93 - 93: i11iIiiIii
    if 80 - 80: i1IIi . OOOo0 - O0ooOooooO + i1I111II1I + i1I111ii1II1i % O0ooOooooO
def IiiII ( ) :
 OO0oo = OooOOOOo ( 'http://www.iwatchseries.me/tv-list/' )
 oo0O0oO = re . compile ( '<h5><a href="([^"]*)"><strong>(.+?)</strong></a></h5>' ) . findall ( OO0oo )
 for oOo0 , IiI111111IIII in oo0O0oO :
  Oo00oo0000OO ( IiI111111IIII , oOo0 , 8021 , i1iIIi1 + 'iwatch.png' )
def I1ii1iI ( url ) :
 OO0oo = OooOOOOo ( url )
 oo0O0oO = re . compile ( '<h5><strong><a href="([^"]*)">(.+?)</a>(.+?)</strong></h5>' ) . findall ( OO0oo )
 for url , IiI111111IIII , I11i1II in oo0O0oO :
  Oo00oo0000OO ( IiI111111IIII + I11i1II , url , 8022 , i1iIIi1 + 'iwatch.png' )
def i1i1IIi ( url ) :
 OO0oo = OooOOOOo ( url )
 oo0O0oO = re . compile ( '<iframe src="([^"]*)"' ) . findall ( OO0oo )
 for url in oo0O0oO :
  print '>>>>>>>>>>>>>>>>>>>>' + url
  i1Ii1i1ii1 ( url )
def i1Ii1i1ii1 ( url ) :
 OO0oo = OooOOOOo ( url )
 oo0O0oO = re . compile ( '{.+?"file" : "(.+?)",.+?"default" : true.+?"label" : "(.+?)"' , re . DOTALL ) . findall ( OO0oo )
 IIIIiiIiiI = re . compile ( 'setup\(\{.+?file: "(.+?)",.+?skin' , re . DOTALL ) . findall ( OO0oo )
 oO0o = re . compile ( "{ label: '([^']*)', file:.+?'([^']*)' }" ) . findall ( OO0oo )
 for url , IiI111111IIII in oo0O0oO :
  ii1II ( 'VidSpot - ' + IiI111111IIII , url , 222 , i1iIIi1 + 'iwatch.png' )
 for url in IIIIiiIiiI :
  ii1II ( 'VodLocker' , url , 222 , i1iIIi1 + 'iwatch.png' )
 for IiI111111IIII , url in oO0o :
  print '<><><><><><><><><><><> before   ' + url
  if 'hevideo' in url :
   print '>>>>>>>>>>>>>>>>>>>>>>>>>' + url
   ii1II ( 'TheVideo - ' + IiI111111IIII , url , 222 , i1iIIi1 + 'iwatch.png' )
   if 86 - 86: O0ooOooooO % O0 + Ooo00oOo00o
def oO0OO ( ) :
 OO0oo = cloudflare . source ( 'http://www.animeland.me/anime-list' )
 oo0O0oO = re . compile ( 'letter-spacing:-1px;" href="([^"]*)">(.+?)</a></li>' ) . findall ( OO0oo )
 for oOo0 , IiI111111IIII in oo0O0oO :
  Oo00oo0000OO ( IiI111111IIII , oOo0 , 1021 , i1iIIi1 + 'anime.png' )
  if 88 - 88: OOOo0
  if 79 - 79: i1I111II1I + OOO0OOo + O0ooOooooO
def i1iI1I1IIIi1i ( ) :
 OO0oo = OooOOOOo ( 'http://www.animetoon.org/cartoon' )
 oo0O0oO = re . compile ( '<td><a href="(.+?)">(.+)</a></td>' ) . findall ( OO0oo )
 for oOo0 , IiI111111IIII in oo0O0oO :
  Oo00oo0000OO ( IiI111111IIII , oOo0 , 1002 , i1iIIi1 + 'anime.png' )
  if 73 - 73: O0 * o00OO00OoO . i1IIi
  if 51 - 51: Ooo00oOo00o - i1I111ii1II1i % O0 - I1IiI
  if 53 - 53: i1I111ii1II1i / i1IIi / i1IIi
def o0oo00O ( url ) :
 OO0oo = OooOOOOo ( url )
 IIIIiiIiiI = re . compile ( '<img src="(.+?)" id="series_image" width="250" height="370" alt=".+?" />' ) . findall ( OO0oo )
 for OO0ooOOO0OOO in IIIIiiIiiI :
  Ii1IIi = OO0ooOOO0OOO
 oO0o = re . compile ( '<li><a href="(.+?)">Next</a></li>' ) . findall ( OO0oo )
 for url in oO0o :
  Oo00oo0000OO ( 'NEXT PAGE' , url , 1002 , i1iIIi1 + 'Next.png' )
 oo0O0oO = re . compile ( '&nbsp;<a href="(.+?)">(.+?)</a>' ) . findall ( OO0oo )
 for url , IiI111111IIII in oo0O0oO :
  Oo00oo0000OO ( IiI111111IIII , url , 1003 , Ii1IIi )
 xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
def IIIIII1iI1II ( url , IMAGE ) :
 OO0oo = OooOOOOo ( url )
 oo0O0oO = re . compile ( '"playlist">(.+?)</span></div><div><iframe src="(.+?)"' ) . findall ( OO0oo )
 for IiI111111IIII , url in oo0O0oO :
  print IiI111111IIII + '     ' + url
  if 'easy' in url :
   iiiI1 ( url )
  elif 'playpanda' in url :
   iiiI1 ( url )
   if 58 - 58: OoOo00o % i11iIiiIii * OoOoOO00 . ii11ii1ii
  xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
def iiiI1 ( url ) :
 OO0oo = OooOOOOo ( url )
 oo0O0oO = re . compile ( "url: '(.+?)'," ) . findall ( OO0oo )
 for url in oo0O0oO :
  ii1II ( 'STREAM' , url , 222 , i1iIIi1 + 'anime.png' )
  if 94 - 94: i11iIiiIii . i1I111II1I + iIii1I11I1II1 * o00OO00OoO * o00OO00OoO
  if 36 - 36: Oooo0Ooo000 - OoOo00o . OoOo00o
def Oo0OOOO0oOoo0 ( url ) :
 I11i = urllib2 . Request ( url )
 I11i . add_header ( 'User-Agent' , "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0" )
 I11i . add_header ( 'referer' , url )
 o0OoiiI1i = urllib2 . urlopen ( I11i )
 iiI1 = o0OoiiI1i . read ( )
 o0OoiiI1i . close ( )
 return iiI1
 if 92 - 92: OoOo00o . Oo - Oo - OOooOOo + o00OO00OoO - O0
def Iii1 ( url ) :
 I11i = urllib2 . Request ( url )
 I11i . add_header ( 'User-Agent' , "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0" )
 o0OoiiI1i = urllib2 . urlopen ( I11i )
 iiI1 = o0OoiiI1i . read ( )
 o0OoiiI1i . close ( )
 return iiI1
 if 30 - 30: OoOo00o - i1I111ii1II1i - Ooo00oOo00o
def ii11 ( url ) :
 xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
 oOoooO000O = ( '%s%s' % ( III1I11i1iIi , url ) )
 iiI1 = Iii1 ( url )
 oo0O0oO = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( iiI1 )
 for url , II1iI , IiI111111IIII in oo0O0oO :
  ii1II ( '%s' % ( IiI111111IIII ) . replace ( 'GenieTv' , '[COLOR green]GenieTV[/COLOR]' ) . replace ( '.' , ' ' ) . replace ( 'mp4' , '' ) . replace ( 'mkv' , '' ) . replace ( '_' , ' ' ) , '%s' % ( url ) , 222 , II1iI )
  if 99 - 99: ii11ii1ii - O0ooOooooO
def iIIIiIi ( url ) :
 iiIiIiII = xbmc . Player ( i1i ( ) )
 import urlresolver
 try : iiIiIiII . play ( url )
 except : pass
 from urlresolver import common
 o00 = xbmcgui . DialogProgress ( )
 o00 . create ( 'LOADING' , 'Opening %s Now' % ( IiI111111IIII ) )
 iiIiIiII = xbmc . Player ( i1i ( ) )
 url = urlresolver . HostedMediaFile ( url ) . resolve ( )
 if o00 . iscanceled ( ) :
  print "[COLORred]STREAM CANCELLED[/COLOR]"
  oO = xbmcgui . Dialog ( )
  if oO . yesno ( "[B]CANCELLED[/B]" , '[B]Was There A Problem[/B]' , '' , "" , 'Yes' , 'No' ) :
   oO . ok ( "Message Send" , "Your Message Has Been Sent" )
  else :
   return
 else :
  try : iiIiIiII . play ( url )
  except : pass
  try : iiIIIII1i1iI . resolve_url ( url )
  except : pass
  o00 . close ( )
  if 10 - 10: OoOoOO00 . Ooo00oOo00o
def o000Ooo00o00O ( url ) :
 o00 = xbmcgui . DialogProgress ( )
 o00 . create ( 'Featching Your Video' , 'Featching Your Video' )
 o00 . update ( 0 , '%s' % IiI111111IIII )
 xbmc . sleep ( 1 )
 iiIiIiII = xbmc . Player ( i1i ( ) )
 o00 . update ( 100 , '%s' % IiI111111IIII )
 xbmc . sleep ( 1 )
 iiIiIiII . play ( url ) . strip ( )
 o00 . close ( )
 if 80 - 80: i1I111ii1II1i
def OOoO ( url ) :
 iiIiIiII = xbmc . Player ( i1i ( ) )
 import urlresolver
 url = ( url ) . strip ( )
 try : iiIiIiII . play ( url ) . strip ( )
 except : pass
 if 3 - 3: ii11ii1ii * Oooo0Ooo000
 if 53 - 53: iIii1I11I1II1 / i1I111ii1II1i % Ooo00oOo00o + OoOo00o / OOO0OOo
def i1i ( ) :
 try :
  oo00oO = getSet ( "core-player" )
  if ( oo00oO == 'DVDPLAYER' ) : I11i1I11 = xbmc . PLAYER_CORE_DVDPLAYER
  elif ( oo00oO == 'MPLAYER' ) : I11i1I11 = xbmc . PLAYER_CORE_MPLAYER
  elif ( oo00oO == 'PAPLAYER' ) : I11i1I11 = xbmc . PLAYER_CORE_PAPLAYER
  else : I11i1I11 = xbmc . PLAYER_CORE_AUTO
 except : I11i1I11 = xbmc . PLAYER_CORE_AUTO
 return I11i1I11
 return True
 if 32 - 32: OoOo00o - O0ooOooooO . iIii1I11I1II1 . o00OO00OoO + OoOoOO00 % OoooooooOO
def Oo00oo0000OO ( name , url , mode , iconimage , showcontext = True , allinfo = { } ) :
 O000O = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 Oo00OO0 = True
 oo0O = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 oo0O . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 if showcontext :
  Oo000 = [ ]
  if showcontext == 'fav' :
   Oo000 . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in oOoOooOo0o0 :
   Oo000 . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  oo0O . addContextMenuItems ( Oo000 )
 Oo00OO0 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = O000O , listitem = oo0O , isFolder = True )
 return Oo00OO0
 if 75 - 75: O0
def i1OoOO ( name , url , mode , iconimage , fanart , description ) :
 if 56 - 56: Ooo00oOo00o / OoOoOO00
 O000O = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 Oo00OO0 = True
 oo0O = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 oo0O . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 oo0O . setProperty ( "Fanart_Image" , fanart )
 Oo00OO0 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = O000O , listitem = oo0O , isFolder = True )
 return Oo00OO0
 if 39 - 39: I1IiI - OoooooooOO - i1IIi / OoOoOO00
def ii1II ( name , url , mode , iconimage , showcontext = True , allinfo = { } ) :
 O000O = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 Oo00OO0 = True
 oo0O = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 oo0O . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 if showcontext :
  Oo000 = [ ]
  if showcontext == 'fav' :
   Oo000 . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in oOoOooOo0o0 :
   Oo000 . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  oo0O . addContextMenuItems ( Oo000 )
 Oo00OO0 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = O000O , listitem = oo0O , isFolder = False )
 return Oo00OO0
 if 49 - 49: Oo + O0 + OoOo00o . OoOoOO00 % OOO0OOo
 if 33 - 33: I1IiI . iIii1I11I1II1 / Oooo0Ooo000 % iI
 if 49 - 49: Ooo00oOo00o + OoOoOO00 / OoOo00o - O0 % iI
 if 27 - 27: Ooo00oOo00o + Oo
 if 92 - 92: OOOo0 % i1I111ii1II1i
 if 31 - 31: OoooooooOO - O0ooOooooO / o00OO00OoO
def ii111iI1iIi1 ( heading , announce ) :
 class oo00o000O ( ) :
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
   try : i1i1ii = open ( announce ) ; OooO0o = i1i1ii . read ( )
   except : OooO0o = announce
   self . win . getControl ( self . CONTROL_TEXTBOX ) . setText ( str ( OooO0o ) )
   return
 oo00o000O ( )
 oo00o000O ( )
 if 81 - 81: i1IIi / o00OO00OoO % i11iIiiIii . iIii1I11I1II1 * I1IiI + OoooooooOO
def iiii1Ii1iii ( ) :
 ii111iI1iIi1 ( 'These are the main Sources you should get into you XBMC' , '[COLORwhite]http://architects.x10host.com[/COLOR]--- [CR]  [COLORred]http://repo.sharktech.co.uk[/COLOR]--- [CR]   [COLORwhite]http://fusion.tvaddons.ag[/COLOR]--- [CR]  [COLORred]http://i.totalxbmc.tv[/COLOR]--- [CR]   [COLORwhite]http://www.xunitytalk.com/xfinity[/COLOR]--- [CR]  [COLORred]http://srp.nu[/COLOR]--- [CR]   [COLORwhite]http://solved.no-issue.ca[/COLOR]--- [CR]  [COLORred]http://xbmc.aminhacasadigital.com[/COLOR]--- [CR]   [COLORwhite]http://xbmc.movieshd.co[/COLOR]--- [CR]  [COLORred]http://install.kaosbox.tv[/COLOR]--- [CR]   [COLORwhite]http://kodi-repo.com/mxr[/COLOR]--- [CR]  [COLORred]http://kodi.metalkettle.co[/COLOR]--- [CR]   [COLORwhite]http://prozone.getxbmc.com[/COLOR]--- [CR]  [COLORred]http://transform.mega-tron.tv[/COLOR]--- [CR]   [COLORwhite]http://muckys.kodimediaportal.ml[/COLOR]--- [CR]  [COLORred]http://jas0npc.pcriot.com[/COLOR]--- [CR]  [COLORwhite]Sports devil source[/COLOR]--- [CR]  [COLORred]http://iwillfolo.com/iwf[/COLOR]' )
 if 73 - 73: i11iIiiIii + O0ooOooooO % Oooo0Ooo000 . OoooooooOO % O0ooOooooO
 if 32 - 32: i11iIiiIii - OoOoOO00
 if 21 - 21: I1IiI - OoOoOO00
 if 10 - 10: I1IiI - OOooOOo * i11iIiiIii / Oo + OOooOOo + iIii1I11I1II1
 if 23 - 23: i1IIi + ii11ii1ii + OOOo0 - OOO0OOo % OoooooooOO . OoOo00o
def OOooOoooOoOo ( ) :
 xbmc . executebuiltin ( 'UpdateLocalAddons' )
 xbmc . executebuiltin ( 'UpdateAddonRepos' )
 oO = xbmcgui . Dialog ( )
 oO . ok ( "GenieTv" , '' , '                                 REFRESH SUCCESSFUL :)' , "                          [COLOR gold]Brought To You By Kodi Support Group, GenieTv[/COLOR]" )
 return
 if 49 - 49: O0ooOooooO . I1IiI
 if 73 - 73: iI / OOOo0 / OoooooooOO + OOOo0
 if 57 - 57: i1I111II1I . iI % OOooOOo
 if 32 - 32: Oooo0Ooo000 / OoOo00o - O0 * iIii1I11I1II1
 if 70 - 70: OoooooooOO % OoooooooOO % Ooo00oOo00o
 if 98 - 98: Ooo00oOo00o
 if 18 - 18: Oooo0Ooo000 + Oo - Ooo00oOo00o / o00OO00OoO / i1I111II1I
 if 53 - 53: i1I111II1I + OOooOOo . O0ooOooooO / Oooo0Ooo000
 if 52 - 52: o00OO00OoO + o00OO00OoO
 if 73 - 73: OOooOOo . i11iIiiIii % OoooooooOO + OOO0OOo . OoooooooOO / i1I111II1I
 if 54 - 54: I1IiI . OoooooooOO
 if 36 - 36: O0ooOooooO / OoOoOO00 * OoOo00o % ii11ii1ii
 if 31 - 31: OoOoOO00 + i1I111II1I - OoooooooOO . Oooo0Ooo000
 if 28 - 28: iI . ii11ii1ii
 if 77 - 77: ii11ii1ii % OoOoOO00
 if 81 - 81: I1IiI % iI / O0 * iIii1I11I1II1 % OoOo00o . OOOo0
 if 90 - 90: OOooOOo
 if 44 - 44: OOooOOo / ii11ii1ii . Oo + I1IiI
 if 32 - 32: OoOo00o - OOO0OOo * i1I111ii1II1i * Oooo0Ooo000
 if 84 - 84: iI + ii11ii1ii % OOOo0 + i11iIiiIii
 if 37 - 37: Oooo0Ooo000 % ii11ii1ii / OOO0OOo
 if 94 - 94: Oooo0Ooo000 / Ooo00oOo00o . OOooOOo
 if 1 - 1: Oo . OoOoOO00
 if 93 - 93: OoOoOO00 . i11iIiiIii + OoOoOO00 % O0ooOooooO
def O00OOO000oo0 ( url ) :
 iiI1 = OooOOOOo ( iiI1IiI + IiI1iIiiI1iI ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 oo0O0oO = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( iiI1 )
 for IiI111111IIII , url , OOO0000oO , iI1i111I1Ii , oo00o0 in oo0O0oO :
  IIIIii ( IiI111111IIII , url , 42 , OOO0000oO , iI1i111I1Ii , oo00o0 )
 O00Oo000ooO0 ( 'movies' , 'MAIN' )
 if 2 - 2: OOOo0 * o00OO00OoO % o00OO00OoO - o00OO00OoO - i1I111ii1II1i + i1I111II1I
def I1iIiiIi ( url ) :
 iiI1 = OooOOOOo ( iiI1IiI + Ooi1IIii1i ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 oo0O0oO = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( iiI1 )
 for IiI111111IIII , url , OOO0000oO , iI1i111I1Ii , oo00o0 in oo0O0oO :
  IIIIii ( IiI111111IIII , url , 42 , OOO0000oO , iI1i111I1Ii , oo00o0 )
 O00Oo000ooO0 ( 'movies' , 'MAIN' )
 if 60 - 60: iI % Oo / Oooo0Ooo000 . i1I111ii1II1i / o00OO00OoO - OoooooooOO
def o0iii1i ( url ) :
 iiI1 = OooOOOOo ( iiI1IiI + IIIIIIi1IIi1I11i ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 oo0O0oO = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( iiI1 )
 for IiI111111IIII , url , OOO0000oO , iI1i111I1Ii , oo00o0 in oo0O0oO :
  IIIIii ( IiI111111IIII , url , 42 , OOO0000oO , iI1i111I1Ii , oo00o0 )
 O00Oo000ooO0 ( 'movies' , 'MAIN' )
 if 70 - 70: iI % iI . I1IiI / i11iIiiIii
def IiII ( url ) :
 iiI1 = OooOOOOo ( iiI1IiI + I1OO ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 oo0O0oO = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( iiI1 )
 for IiI111111IIII , url , OOO0000oO , iI1i111I1Ii , oo00o0 in oo0O0oO :
  IIIIii ( IiI111111IIII , url , 42 , OOO0000oO , iI1i111I1Ii , oo00o0 )
 O00Oo000ooO0 ( 'movies' , 'MAIN' )
 if 34 - 34: o00OO00OoO . I1IiI / i11iIiiIii / i1I111ii1II1i
def II1iII1 ( url ) :
 iiI1 = OooOOOOo ( iiI1IiI + I11II11IiI11 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 oo0O0oO = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( iiI1 )
 for IiI111111IIII , url , OOO0000oO , iI1i111I1Ii , oo00o0 in oo0O0oO :
  IIIIii ( IiI111111IIII , url , 42 , OOO0000oO , iI1i111I1Ii , oo00o0 )
 O00Oo000ooO0 ( 'movies' , 'MAIN' )
 if 97 - 97: OOO0OOo / iIii1I11I1II1 % OOO0OOo / OOOo0 * i1I111ii1II1i % I1IiI
def i1iiii1 ( url ) :
 iiI1 = OooOOOOo ( iiI1IiI + oOO0000 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 oo0O0oO = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( iiI1 )
 for IiI111111IIII , url , OOO0000oO , iI1i111I1Ii , oo00o0 in oo0O0oO :
  IIIIii ( IiI111111IIII , url , 42 , OOO0000oO , iI1i111I1Ii , oo00o0 )
 O00Oo000ooO0 ( 'movies' , 'MAIN' )
 if 84 - 84: O0 % iI . iI . i1I111ii1II1i * Oooo0Ooo000
def iIOO0O ( url ) :
 iiI1 = OooOOOOo ( iiI1IiI + I11IiiiII ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 oo0O0oO = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( iiI1 )
 for IiI111111IIII , url , OOO0000oO , iI1i111I1Ii , oo00o0 in oo0O0oO :
  IIIIii ( IiI111111IIII , url , 42 , OOO0000oO , iI1i111I1Ii , oo00o0 )
 O00Oo000ooO0 ( 'movies' , 'MAIN' )
 if 66 - 66: Oo / i11iIiiIii % OOO0OOo
def i1Ii1i11ii ( url ) :
 iiI1 = OooOOOOo ( iiI1IiI + oO0O0oo ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 oo0O0oO = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( iiI1 )
 for IiI111111IIII , url , OOO0000oO , iI1i111I1Ii , oo00o0 in oo0O0oO :
  IIIIii ( IiI111111IIII , url , 42 , OOO0000oO , iI1i111I1Ii , oo00o0 )
 O00Oo000ooO0 ( 'movies' , 'MAIN' )
 if 64 - 64: I1IiI % I1IiI + OOooOOo + Oo
def OO0oO0Oo ( url ) :
 iiI1 = OooOOOOo ( iiI1IiI + OoooOO0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 oo0O0oO = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( iiI1 )
 for IiI111111IIII , url , OOO0000oO , iI1i111I1Ii , oo00o0 in oo0O0oO :
  IIIIii ( IiI111111IIII , url , 42 , OOO0000oO , iI1i111I1Ii , oo00o0 )
 O00Oo000ooO0 ( 'movies' , 'MAIN' )
 if 69 - 69: OoOoOO00 + i1I111ii1II1i
def oooOOO ( url ) :
 iiI1 = OooOOOOo ( iiI1IiI + Iii1o00o0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 oo0O0oO = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( iiI1 )
 for IiI111111IIII , url , OOO0000oO , iI1i111I1Ii , oo00o0 in oo0O0oO :
  IIIIii ( IiI111111IIII , url , 5 , OOO0000oO , iI1i111I1Ii , oo00o0 )
 O00Oo000ooO0 ( 'movies' , 'MAIN' )
 if 84 - 84: I1IiI - Oo . OOO0OOo . OoOo00o - Oo
 if 99 - 99: o00OO00OoO
 if 75 - 75: OOO0OOo . i1I111II1I / OoOo00o
 if 84 - 84: OoooooooOO . OOOo0 / OOooOOo
 if 86 - 86: Oo % I1IiI
 if 77 - 77: iI % i1I111II1I / O0ooOooooO
 if 91 - 91: Ooo00oOo00o / Ooo00oOo00o . OoOoOO00 . OOO0OOo - OOOo0
 if 23 - 23: OOOo0
 if 7 - 7: i1I111ii1II1i % ii11ii1ii
def o0oOOO ( ) :
 try :
  if os . path . exists ( oOOoO0 ) == True :
   oO = xbmcgui . Dialog ( )
   if oO . yesno ( "Delete Thumbnails" , "[COLOR gold][B]##########WARNING ANDROID ONLY##########[/B][/COLOR]" , "This feature deletes your thumbnail folder and textures13.db" , "Are you sure you want to do proceed? This Can NOT Be Undone" ) :
    for o0oO0O00oOo , iIi11i1 , oO00oo0o00o0o in os . walk ( oOOoO0 ) :
     I11iIIIIi1Iii1iIi = 0
     I11iIIIIi1Iii1iIi += len ( oO00oo0o00o0o )
     if I11iIIIIi1Iii1iIi > 0 :
      for i1i1ii in oO00oo0o00o0o :
       os . unlink ( os . path . join ( o0oO0O00oOo , i1i1ii ) )
  ii1IIi1iI1ii1 = os . path . join ( OOooO0OOoo , "Textures13.db" )
  os . unlink ( ii1IIi1iI1ii1 )
  oO . ok ( "Restart KODI" , "Please restart KODI to rebuild thumbnail library" )
 except :
  oO = xbmcgui . Dialog ( )
  oO . ok ( Oo0oO0ooo , "Error Deleting Thumbnails please visit Kodi Support Group, GenieTv on facebook" )
 return
 if 58 - 58: iI . Oooo0Ooo000
 if 41 - 41: Ooo00oOo00o % OOOo0 - Oo
 if 11 - 11: iI * OOooOOo / OoOo00o + I1IiI + Ooo00oOo00o % o00OO00OoO
 if 18 - 18: OOOo0 - I1IiI
 if 18 - 18: i1I111II1I + Ooo00oOo00o * O0ooOooooO - O0ooOooooO . ii11ii1ii * Oooo0Ooo000
 if 95 - 95: ii11ii1ii / I1IiI
 if 10 - 10: OoOo00o % ii11ii1ii - OoOo00o
 if 86 - 86: Oo
 if 88 - 88: o00OO00OoO * OOOo0
def IIiI ( url ) :
 print '############################################################       DELETING STANDARD CACHE             ###############################################################'
 OOoOo0oO0oo00 = os . path . join ( xbmc . translatePath ( 'special://home' ) , 'cache' )
 if os . path . exists ( OOoOo0oO0oo00 ) == True :
  for o0oO0O00oOo , iIi11i1 , oO00oo0o00o0o in os . walk ( OOoOo0oO0oo00 ) :
   I11iIIIIi1Iii1iIi = 0
   I11iIIIIi1Iii1iIi += len ( oO00oo0o00o0o )
   if 100 - 100: Ooo00oOo00o . Oooo0Ooo000 / iI . OOooOOo - I1IiI . Oooo0Ooo000
   if 30 - 30: iI % Oooo0Ooo000 + OOooOOo
   if I11iIIIIi1Iii1iIi > 0 :
    if 65 - 65: iIii1I11I1II1 . i1I111ii1II1i / iI
    oO = xbmcgui . Dialog ( )
    if oO . yesno ( "Delete KODI Cache Files" , str ( I11iIIIIi1Iii1iIi ) + " files found" , "Do you want to delete them?" ) :
     if 12 - 12: OOOo0 + o00OO00OoO
     for i1i1ii in oO00oo0o00o0o :
      try :
       os . unlink ( os . path . join ( o0oO0O00oOo , i1i1ii ) )
      except :
       pass
     for IiIi1iIIi1 in iIi11i1 :
      try :
       shutil . rmtree ( os . path . join ( o0oO0O00oOo , IiIi1iIIi1 ) )
      except :
       pass
       if 80 - 80: O0ooOooooO . O0
   else :
    pass
 if xbmc . getCondVisibility ( 'system.platform.ATV2' ) :
  oooO = os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'Other' )
  if 79 - 79: ii11ii1ii - iIii1I11I1II1 % i1IIi / Oo + OoOoOO00
  for o0oO0O00oOo , iIi11i1 , oO00oo0o00o0o in os . walk ( oooO ) :
   I11iIIIIi1Iii1iIi = 0
   I11iIIIIi1Iii1iIi += len ( oO00oo0o00o0o )
   if 95 - 95: O0ooOooooO
   if I11iIIIIi1Iii1iIi > 0 :
    if 48 - 48: Oooo0Ooo000 / iIii1I11I1II1 % OoOoOO00
    oO = xbmcgui . Dialog ( )
    if oO . yesno ( "Delete ATV2 Cache Files" , str ( I11iIIIIi1Iii1iIi ) + " files found in 'Other'" , "Do you want to delete them?" ) :
     if 39 - 39: i1IIi . ii11ii1ii / Oooo0Ooo000 / Oooo0Ooo000
     for i1i1ii in oO00oo0o00o0o :
      os . unlink ( os . path . join ( o0oO0O00oOo , i1i1ii ) )
     for IiIi1iIIi1 in iIi11i1 :
      shutil . rmtree ( os . path . join ( o0oO0O00oOo , IiIi1iIIi1 ) )
      if 100 - 100: OoooooooOO - OoooooooOO + OoOo00o
   else :
    pass
  iIiIi1i1Iiii = os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'LocalAndRental' )
  if 78 - 78: Oo - o00OO00OoO + i1I111ii1II1i * iI * OOooOOo
  for o0oO0O00oOo , iIi11i1 , oO00oo0o00o0o in os . walk ( iIiIi1i1Iiii ) :
   I11iIIIIi1Iii1iIi = 0
   I11iIIIIi1Iii1iIi += len ( oO00oo0o00o0o )
   if 23 - 23: Oo - O0
   if I11iIIIIi1Iii1iIi > 0 :
    if 33 - 33: ii11ii1ii
    oO = xbmcgui . Dialog ( )
    if oO . yesno ( "Delete ATV2 Cache Files" , str ( I11iIIIIi1Iii1iIi ) + " files found in 'LocalAndRental'" , "Do you want to delete them?" ) :
     if 54 - 54: OOO0OOo * ii11ii1ii . OoOoOO00 / i1I111II1I % i1I111II1I
     for i1i1ii in oO00oo0o00o0o :
      os . unlink ( os . path . join ( o0oO0O00oOo , i1i1ii ) )
     for IiIi1iIIi1 in iIi11i1 :
      shutil . rmtree ( os . path . join ( o0oO0O00oOo , IiIi1iIIi1 ) )
      if 25 - 25: i11iIiiIii + ii11ii1ii - OoooooooOO . O0 % o00OO00OoO
   else :
    pass
    if 53 - 53: i1IIi
    if 59 - 59: OOooOOo + OOOo0 % OoooooooOO - iIii1I11I1II1
    if 9 - 9: i1IIi - I1IiI
    if 57 - 57: iIii1I11I1II1 * iI * i1I111ii1II1i / O0ooOooooO
 iIIiII1i1ii = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.whatthefurk/cache' ) , '' )
 if os . path . exists ( iIIiII1i1ii ) == True :
  for o0oO0O00oOo , iIi11i1 , oO00oo0o00o0o in os . walk ( iIIiII1i1ii ) :
   I11iIIIIi1Iii1iIi = 0
   I11iIIIIi1Iii1iIi += len ( oO00oo0o00o0o )
   if 57 - 57: OOO0OOo + o00OO00OoO
   if 49 - 49: I1IiI * OoooooooOO
   if I11iIIIIi1Iii1iIi > 0 :
    if 7 - 7: o00OO00OoO / O0ooOooooO + OOooOOo
    oO = xbmcgui . Dialog ( )
    if oO . yesno ( "Delete WTF Cache Files" , str ( I11iIIIIi1Iii1iIi ) + " files found" , "Do you want to delete them?" ) :
     if 19 - 19: i1IIi % OOOo0 - iIii1I11I1II1 - O0ooOooooO / ii11ii1ii
     for i1i1ii in oO00oo0o00o0o :
      os . unlink ( os . path . join ( o0oO0O00oOo , i1i1ii ) )
     for IiIi1iIIi1 in iIi11i1 :
      shutil . rmtree ( os . path . join ( o0oO0O00oOo , IiIi1iIIi1 ) )
      if 16 - 16: iI
   else :
    pass
    if 79 - 79: OoooooooOO - OOO0OOo * iI - OoOoOO00 % I1IiI * OoOo00o
    if 31 - 31: OOOo0
 IIII1I1 = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.4od/cache' ) , '' )
 if os . path . exists ( IIII1I1 ) == True :
  for o0oO0O00oOo , iIi11i1 , oO00oo0o00o0o in os . walk ( IIII1I1 ) :
   I11iIIIIi1Iii1iIi = 0
   I11iIIIIi1Iii1iIi += len ( oO00oo0o00o0o )
   if 36 - 36: iI * Oooo0Ooo000 . Oooo0Ooo000 / Oo / OOOo0
   if 80 - 80: OoooooooOO - i1IIi
   if I11iIIIIi1Iii1iIi > 0 :
    if 51 - 51: i1IIi . I1IiI / I1IiI % i11iIiiIii * i1I111II1I - o00OO00OoO
    oO = xbmcgui . Dialog ( )
    if oO . yesno ( "Delete 4oD Cache Files" , str ( I11iIIIIi1Iii1iIi ) + " files found" , "Do you want to delete them?" ) :
     if 49 - 49: Oo - iIii1I11I1II1
     for i1i1ii in oO00oo0o00o0o :
      os . unlink ( os . path . join ( o0oO0O00oOo , i1i1ii ) )
     for IiIi1iIIi1 in iIi11i1 :
      shutil . rmtree ( os . path . join ( o0oO0O00oOo , IiIi1iIIi1 ) )
      if 64 - 64: o00OO00OoO + iIii1I11I1II1
   else :
    pass
    if 14 - 14: iI / OoooooooOO + OoOoOO00 . O0 / i1IIi
    if 58 - 58: OOooOOo / i11iIiiIii / O0 % Oooo0Ooo000 % OOOo0
 O0oOOo0 = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.iplayer/iplayer_http_cache' ) , '' )
 if os . path . exists ( O0oOOo0 ) == True :
  for o0oO0O00oOo , iIi11i1 , oO00oo0o00o0o in os . walk ( O0oOOo0 ) :
   I11iIIIIi1Iii1iIi = 0
   I11iIIIIi1Iii1iIi += len ( oO00oo0o00o0o )
   if 71 - 71: i11iIiiIii % iIii1I11I1II1
   if 42 - 42: i11iIiiIii + o00OO00OoO - OOooOOo
   if I11iIIIIi1Iii1iIi > 0 :
    if 2 - 2: OOooOOo . iI % I1IiI
    oO = xbmcgui . Dialog ( )
    if oO . yesno ( "Delete BBC iPlayer Cache Files" , str ( I11iIIIIi1Iii1iIi ) + " files found" , "Do you want to delete them?" ) :
     if 58 - 58: ii11ii1ii % iI * iI - i1I111ii1II1i
     for i1i1ii in oO00oo0o00o0o :
      os . unlink ( os . path . join ( o0oO0O00oOo , i1i1ii ) )
     for IiIi1iIIi1 in iIi11i1 :
      shutil . rmtree ( os . path . join ( o0oO0O00oOo , IiIi1iIIi1 ) )
      if 9 - 9: OOO0OOo - iI % OoOoOO00 + OoOo00o + i1I111II1I % O0
   else :
    pass
    if 65 - 65: i1I111II1I - Ooo00oOo00o % i11iIiiIii
    if 58 - 58: i1I111ii1II1i
    if 2 - 2: OoOoOO00 + i1IIi
 oO0OO00 = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/script.module.simple.downloader' ) , '' )
 if os . path . exists ( oO0OO00 ) == True :
  for o0oO0O00oOo , iIi11i1 , oO00oo0o00o0o in os . walk ( oO0OO00 ) :
   I11iIIIIi1Iii1iIi = 0
   I11iIIIIi1Iii1iIi += len ( oO00oo0o00o0o )
   if 16 - 16: OoooooooOO / O0ooOooooO . iI * OOO0OOo - OOOo0
   if 32 - 32: OOOo0 / Ooo00oOo00o
   if I11iIIIIi1Iii1iIi > 0 :
    if 28 - 28: Oo / OoOo00o . i1I111ii1II1i + Ooo00oOo00o + Oooo0Ooo000 % Oo
    oO = xbmcgui . Dialog ( )
    if oO . yesno ( "Delete Simple Downloader Cache Files" , str ( I11iIIIIi1Iii1iIi ) + " files found" , "Do you want to delete them?" ) :
     if 45 - 45: Oo / O0 % OoooooooOO
     for i1i1ii in oO00oo0o00o0o :
      os . unlink ( os . path . join ( o0oO0O00oOo , i1i1ii ) )
     for IiIi1iIIi1 in iIi11i1 :
      shutil . rmtree ( os . path . join ( o0oO0O00oOo , IiIi1iIIi1 ) )
      if 92 - 92: iI . I1IiI . Oooo0Ooo000 - OoooooooOO / OOO0OOo
   else :
    pass
    if 80 - 80: iIii1I11I1II1 / i11iIiiIii + i1I111ii1II1i
    if 41 - 41: o00OO00OoO + Ooo00oOo00o * OOOo0 * O0 * Oo - I1IiI
 ooooOoo00 = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.itv/Images' ) , '' )
 if os . path . exists ( ooooOoo00 ) == True :
  for o0oO0O00oOo , iIi11i1 , oO00oo0o00o0o in os . walk ( ooooOoo00 ) :
   I11iIIIIi1Iii1iIi = 0
   I11iIIIIi1Iii1iIi += len ( oO00oo0o00o0o )
   if 7 - 7: i1I111II1I * Ooo00oOo00o + OoooooooOO . OOO0OOo * Oooo0Ooo000
   if 82 - 82: iIii1I11I1II1 * OoooooooOO
   if I11iIIIIi1Iii1iIi > 0 :
    if 50 - 50: o00OO00OoO - OoOoOO00
    oO = xbmcgui . Dialog ( )
    if oO . yesno ( "Delete ITV Cache Files" , str ( I11iIIIIi1Iii1iIi ) + " files found" , "Do you want to delete them?" ) :
     if 33 - 33: OoOo00o / OoOo00o . i11iIiiIii * ii11ii1ii + OOooOOo
     for i1i1ii in oO00oo0o00o0o :
      os . unlink ( os . path . join ( o0oO0O00oOo , i1i1ii ) )
     for IiIi1iIIi1 in iIi11i1 :
      shutil . rmtree ( os . path . join ( o0oO0O00oOo , IiIi1iIIi1 ) )
      if 16 - 16: OoOo00o
   else :
    pass
    if 10 - 10: I1IiI . OoOo00o * iIii1I11I1II1 - O0ooOooooO - I1IiI / o00OO00OoO
    if 13 - 13: O0ooOooooO + I1IiI % OoOo00o % OoooooooOO
 iiiiI1iiiIi11 = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.movies4me/cache' ) , '' )
 if os . path . exists ( ooooOoo00 ) == True :
  for o0oO0O00oOo , iIi11i1 , oO00oo0o00o0o in os . walk ( iiiiI1iiiIi11 ) :
   I11iIIIIi1Iii1iIi = 0
   I11iIIIIi1Iii1iIi += len ( oO00oo0o00o0o )
   if 52 - 52: iI * Ooo00oOo00o . ii11ii1ii - o00OO00OoO
   if 4 - 4: i11iIiiIii + OoooooooOO / i11iIiiIii . OoooooooOO % ii11ii1ii / I1IiI
   if I11iIIIIi1Iii1iIi > 0 :
    if 35 - 35: ii11ii1ii % i1IIi + OOooOOo - iIii1I11I1II1
    oO = xbmcgui . Dialog ( )
    if oO . yesno ( "Delete Movies4me Cache Files" , str ( I11iIIIIi1Iii1iIi ) + " files found" , "Do you want to delete them?" ) :
     if 28 - 28: OOOo0 * OoOoOO00 * I1IiI % i1I111II1I - i1I111II1I
     for i1i1ii in oO00oo0o00o0o :
      os . unlink ( os . path . join ( o0oO0O00oOo , i1i1ii ) )
     for IiIi1iIIi1 in iIi11i1 :
      shutil . rmtree ( os . path . join ( o0oO0O00oOo , IiIi1iIIi1 ) )
      if 35 - 35: Oo . OOO0OOo - i1IIi . I1IiI
   else :
    pass
    if 12 - 12: OoOo00o / Ooo00oOo00o / O0 * OoOo00o
    if 51 - 51: OOO0OOo * i1I111ii1II1i / i1IIi
 IIi1I1 = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.phstreams/Cache' ) , '' )
 if os . path . exists ( ooooOoo00 ) == True :
  for o0oO0O00oOo , iIi11i1 , oO00oo0o00o0o in os . walk ( IIi1I1 ) :
   I11iIIIIi1Iii1iIi = 0
   I11iIIIIi1Iii1iIi += len ( oO00oo0o00o0o )
   if 37 - 37: OOooOOo * Oo
   if 11 - 11: O0ooOooooO
   if I11iIIIIi1Iii1iIi > 0 :
    if 62 - 62: OoooooooOO % O0ooOooooO * OoOoOO00 * o00OO00OoO * o00OO00OoO / OOO0OOo
    oO = xbmcgui . Dialog ( )
    if oO . yesno ( "Delete Phoenix Cache Files" , str ( I11iIIIIi1Iii1iIi ) + " files found" , "Do you want to delete them?" ) :
     if 90 - 90: o00OO00OoO . OoOoOO00 . ii11ii1ii
     for i1i1ii in oO00oo0o00o0o :
      os . unlink ( os . path . join ( o0oO0O00oOo , i1i1ii ) )
     for IiIi1iIIi1 in iIi11i1 :
      shutil . rmtree ( os . path . join ( o0oO0O00oOo , IiIi1iIIi1 ) )
      if 32 - 32: OOO0OOo - Ooo00oOo00o . i1I111ii1II1i . i1I111ii1II1i % i1IIi * iI
   else :
    pass
    if 65 - 65: i1I111ii1II1i / OOO0OOo . OoOoOO00
    if 90 - 90: Oooo0Ooo000
 o00oooo = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.spotitube/cache' ) , '' )
 if os . path . exists ( ooooOoo00 ) == True :
  for o0oO0O00oOo , iIi11i1 , oO00oo0o00o0o in os . walk ( o00oooo ) :
   I11iIIIIi1Iii1iIi = 0
   I11iIIIIi1Iii1iIi += len ( oO00oo0o00o0o )
   if 63 - 63: OoOoOO00 - Oooo0Ooo000 . I1IiI
   if 8 - 8: OOOo0 * OOO0OOo / OoOo00o + I1IiI . OoOo00o - i1I111II1I
   if I11iIIIIi1Iii1iIi > 0 :
    if 80 - 80: iIii1I11I1II1 / O0ooOooooO * Oo - i1I111II1I * i1I111ii1II1i
    oO = xbmcgui . Dialog ( )
    if oO . yesno ( "Delete YouTube Music Cache Files" , str ( I11iIIIIi1Iii1iIi ) + " files found" , "Do you want to delete them?" ) :
     if 97 - 97: OoOo00o - Oooo0Ooo000 / OoOoOO00
     for i1i1ii in oO00oo0o00o0o :
      os . unlink ( os . path . join ( o0oO0O00oOo , i1i1ii ) )
     for IiIi1iIIi1 in iIi11i1 :
      shutil . rmtree ( os . path . join ( o0oO0O00oOo , IiIi1iIIi1 ) )
      if 26 - 26: i1I111ii1II1i + O0 * i1I111ii1II1i . i1IIi
   else :
    pass
    if 50 - 50: iIii1I11I1II1 - Oooo0Ooo000 % i1I111ii1II1i - Oo
    if 52 - 52: O0ooOooooO + iI - ii11ii1ii * iI . i1I111II1I + o00OO00OoO
 iI11II11I1 = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.supercartoons/cache' ) , '' )
 if os . path . exists ( ooooOoo00 ) == True :
  for o0oO0O00oOo , iIi11i1 , oO00oo0o00o0o in os . walk ( iI11II11I1 ) :
   I11iIIIIi1Iii1iIi = 0
   I11iIIIIi1Iii1iIi += len ( oO00oo0o00o0o )
   if 67 - 67: ii11ii1ii
   if 3 - 3: o00OO00OoO . Oooo0Ooo000 % OoOoOO00 * OOOo0 % i1IIi * Ooo00oOo00o
   if I11iIIIIi1Iii1iIi > 0 :
    if 5 - 5: OoOoOO00 * i1IIi % iI
    oO = xbmcgui . Dialog ( )
    if oO . yesno ( "Delete SuperCartoons Cache Files" , str ( I11iIIIIi1Iii1iIi ) + " files found" , "Do you want to delete them?" ) :
     if 55 - 55: OOOo0 + i1I111ii1II1i
     for i1i1ii in oO00oo0o00o0o :
      os . unlink ( os . path . join ( o0oO0O00oOo , i1i1ii ) )
     for IiIi1iIIi1 in iIi11i1 :
      shutil . rmtree ( os . path . join ( o0oO0O00oOo , IiIi1iIIi1 ) )
      if 85 - 85: O0ooOooooO + i1I111ii1II1i % i1I111ii1II1i / Oooo0Ooo000 . OOOo0 - I1IiI
   else :
    pass
    if 19 - 19: Oooo0Ooo000 / i1I111ii1II1i + OoOo00o
    if 76 - 76: iIii1I11I1II1 / o00OO00OoO - ii11ii1ii % OOooOOo % i1I111II1I + OoooooooOO
 IIi1II1i111i = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.tvonline.cc/cache' ) , '' )
 if os . path . exists ( ooooOoo00 ) == True :
  for o0oO0O00oOo , iIi11i1 , oO00oo0o00o0o in os . walk ( IIi1II1i111i ) :
   I11iIIIIi1Iii1iIi = 0
   I11iIIIIi1Iii1iIi += len ( oO00oo0o00o0o )
   if 58 - 58: OOO0OOo
   if 45 - 45: OOooOOo
   if I11iIIIIi1Iii1iIi > 0 :
    if 67 - 67: i1I111ii1II1i + OOO0OOo
    oO = xbmcgui . Dialog ( )
    if oO . yesno ( "Delete TVonline Cache Files" , str ( I11iIIIIi1Iii1iIi ) + " files found" , "Do you want to delete them?" ) :
     if 25 - 25: i1IIi - i11iIiiIii
     for i1i1ii in oO00oo0o00o0o :
      os . unlink ( os . path . join ( o0oO0O00oOo , i1i1ii ) )
     for IiIi1iIIi1 in iIi11i1 :
      shutil . rmtree ( os . path . join ( o0oO0O00oOo , IiIi1iIIi1 ) )
      if 25 - 25: O0ooOooooO
   else :
    pass
    if 84 - 84: ii11ii1ii - i1I111ii1II1i + ii11ii1ii
    if 63 - 63: Oooo0Ooo000 * OOO0OOo % OoOoOO00 % o00OO00OoO + OOOo0 * Oo
 o0oOo00OOo0O = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.youtube/kodion' ) , '' )
 if os . path . exists ( ooooOoo00 ) == True :
  for o0oO0O00oOo , iIi11i1 , oO00oo0o00o0o in os . walk ( o0oOo00OOo0O ) :
   I11iIIIIi1Iii1iIi = 0
   I11iIIIIi1Iii1iIi += len ( oO00oo0o00o0o )
   if 73 - 73: ii11ii1ii - I1IiI * O0 - I1IiI - Ooo00oOo00o
   if 96 - 96: ii11ii1ii - O0
   if I11iIIIIi1Iii1iIi > 0 :
    if 35 - 35: i1I111II1I . Oooo0Ooo000 . o00OO00OoO - Oooo0Ooo000 % Oooo0Ooo000 + o00OO00OoO
    oO = xbmcgui . Dialog ( )
    if oO . yesno ( "Delete YouTube Cache Files" , str ( I11iIIIIi1Iii1iIi ) + " files found" , "Do you want to delete them?" ) :
     if 99 - 99: OOooOOo + i1I111II1I
     for i1i1ii in oO00oo0o00o0o :
      os . unlink ( os . path . join ( o0oO0O00oOo , i1i1ii ) )
     for IiIi1iIIi1 in iIi11i1 :
      shutil . rmtree ( os . path . join ( o0oO0O00oOo , IiIi1iIIi1 ) )
      if 34 - 34: o00OO00OoO * OOooOOo . OOOo0 % i11iIiiIii
   else :
    pass
    if 61 - 61: iIii1I11I1II1 + O0ooOooooO * Oooo0Ooo000 - i1IIi % O0ooOooooO
    if 76 - 76: O0ooOooooO / I1IiI
    if 12 - 12: o00OO00OoO
 OO0oOo = xbmc . translatePath ( 'special://masterprofile/addon_data/plugin.video.genesis' )
 oO = xbmcgui . Dialog ( )
 try :
  if oO . yesno ( "Delete Genesis Cache Files" , "Do you want to delete cache" ) :
   IIiIi1II1IiI = os . path . join ( OO0oOo , "cache.db" )
   os . unlink ( IIiIi1II1IiI )
   if 99 - 99: Oo
 except :
  pass
  if 17 - 17: i11iIiiIii - i11iIiiIii + ii11ii1ii * OOO0OOo * O0ooOooooO / OoooooooOO
 oO = xbmcgui . Dialog ( )
 oO . ok ( "GenieTv" , "                               Finished Deleting Cache " , "                          [COLOR gold]Brought To You By GenieTv[/COLOR]" )
 if 22 - 22: o00OO00OoO * ii11ii1ii - OoOo00o
 if 71 - 71: iIii1I11I1II1 / i11iIiiIii % OOooOOo . o00OO00OoO * OOOo0 % OoOoOO00
 if 35 - 35: o00OO00OoO - I1IiI
 if 61 - 61: o00OO00OoO * OOooOOo * Ooo00oOo00o + ii11ii1ii . Oo + i1IIi
 if 82 - 82: Oo + o00OO00OoO
 if 93 - 93: Oooo0Ooo000 * O0 * i1I111II1I - OOooOOo / ii11ii1ii
 if 54 - 54: i1IIi - Ooo00oOo00o / OoooooooOO
 if 95 - 95: O0 + iIii1I11I1II1 . ii11ii1ii
 if 61 - 61: iI * iI
def O0III1Iiii1i11 ( url ) :
 print '###' + Oo0oO0ooo + ' - DELETING PACKAGES###'
 OO00 = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' , '' ) )
 try :
  for o0oO0O00oOo , iIi11i1 , oO00oo0o00o0o in os . walk ( OO00 ) :
   I11iIIIIi1Iii1iIi = 0
   I11iIIIIi1Iii1iIi += len ( oO00oo0o00o0o )
   if 10 - 10: Oooo0Ooo000 * i1IIi . O0ooOooooO / o00OO00OoO . i1I111II1I / o00OO00OoO
   if 1 - 1: i1I111ii1II1i % OOO0OOo
   if I11iIIIIi1Iii1iIi > 0 :
    if 99 - 99: i1I111ii1II1i + iIii1I11I1II1 . i1I111II1I / Ooo00oOo00o * ii11ii1ii
    oO = xbmcgui . Dialog ( )
    if oO . yesno ( "Delete Package Cache Files" , str ( I11iIIIIi1Iii1iIi ) + " files found" , "Do you want to delete them?" ) :
     if 87 - 87: OoOo00o / OoOoOO00 % Ooo00oOo00o % Ooo00oOo00o
     for i1i1ii in oO00oo0o00o0o :
      os . unlink ( os . path . join ( o0oO0O00oOo , i1i1ii ) )
     for IiIi1iIIi1 in iIi11i1 :
      shutil . rmtree ( os . path . join ( o0oO0O00oOo , IiIi1iIIi1 ) )
     oO = xbmcgui . Dialog ( )
     oO . ok ( Oo0oO0ooo , "       Deleting Packages all done" )
    else :
     pass
   else :
    oO = xbmcgui . Dialog ( )
    oO . ok ( Oo0oO0ooo , "       No Packages to DELETE" )
 except :
  oO = xbmcgui . Dialog ( )
  oO . ok ( Oo0oO0ooo , "Error Deleting Packages please visit Kodi Support Group, GenieTv on facebook" )
 return
 if 28 - 28: I1IiI % O0ooOooooO - i1I111II1I + i1I111II1I + O0ooOooooO / iIii1I11I1II1
 if 91 - 91: OOOo0 / OoOoOO00 * i1I111II1I
 if 94 - 94: OoOoOO00 - iIii1I11I1II1 - iIii1I11I1II1
 if 83 - 83: ii11ii1ii * iIii1I11I1II1 + I1IiI * i1IIi . OoooooooOO % iI
 if 81 - 81: Ooo00oOo00o - iIii1I11I1II1
 if 60 - 60: o00OO00OoO
 if 77 - 77: OOOo0 / ii11ii1ii
 if 95 - 95: o00OO00OoO * i1IIi + O0ooOooooO
 if 40 - 40: OoOoOO00
def iII1 ( url ) :
 print '###' + Oo0oO0ooo + ' - DELETING PACKAGES###'
 OO00 = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' , '' ) )
 try :
  for o0oO0O00oOo , iIi11i1 , oO00oo0o00o0o in os . walk ( OO00 ) :
   I11iIIIIi1Iii1iIi = 0
   I11iIIIIi1Iii1iIi += len ( oO00oo0o00o0o )
   if 7 - 7: ii11ii1ii - iIii1I11I1II1
   if 97 - 97: i1I111II1I
   if I11iIIIIi1Iii1iIi > 0 :
    if 41 - 41: OoooooooOO - Oo * iIii1I11I1II1 . i1IIi
    oO = xbmcgui . Dialog ( )
    if oO . yesno ( "Delete Package Cache Files" , str ( I11iIIIIi1Iii1iIi ) + " files found" , "Do you want to delete them?" ) :
     if 39 - 39: iI % i1IIi . ii11ii1ii - O0
     for i1i1ii in oO00oo0o00o0o :
      os . unlink ( os . path . join ( o0oO0O00oOo , i1i1ii ) )
     for IiIi1iIIi1 in iIi11i1 :
      shutil . rmtree ( os . path . join ( o0oO0O00oOo , IiIi1iIIi1 ) )
     oO = xbmcgui . Dialog ( )
     oO . ok ( Oo0oO0ooo , "       Deleting Packages all done" )
    else :
     pass
   else :
    oO = xbmcgui . Dialog ( )
    oO . ok ( Oo0oO0ooo , "       No Packages to DELETE" )
 except :
  oO = xbmcgui . Dialog ( )
  oO . ok ( Oo0oO0ooo , "Error Deleting Packages please visit Kodi Support Group, GenieTv on facebook" )
 return
 IIiI ( url )
 if 65 - 65: O0ooOooooO * O0ooOooooO / Oooo0Ooo000 + O0ooOooooO % OOO0OOo + I1IiI
 if 92 - 92: OOooOOo
 if 37 - 37: O0ooOooooO
 if 18 - 18: OoOo00o * i11iIiiIii + iIii1I11I1II1 % Oooo0Ooo000 + i1IIi - Ooo00oOo00o
 if 85 - 85: Ooo00oOo00o * Oooo0Ooo000 + Ooo00oOo00o
 if 39 - 39: Oo / i1IIi % i1IIi
 if 20 - 20: i1I111II1I * O0ooOooooO
 if 91 - 91: Ooo00oOo00o % i1IIi - iIii1I11I1II1 . i1I111II1I
 if 31 - 31: O0ooOooooO % i1IIi . OoooooooOO - OOooOOo + OoooooooOO
def I1i1Ii ( url , name ) :
 O0O0Oo00 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 III1I1I11 = os . path . join ( O0O0Oo00 , 'advancedsettings.xml' )
 oO = xbmcgui . Dialog ( )
 Oo0I1iii = os . path . join ( O0O0Oo00 , 'advancedsettings.xml.bak' )
 if os . path . exists ( Oo0I1iii ) == False :
  if oO . yesno ( "Back Up Original" , 'Have You Backed Up Your Original?' , '' , "[B][COLOR red]     AS YOU CANNOT GO BACK !!![/B][/COLOR]" ) :
   print '###' + Oo0oO0ooo + ' - ADVANCED XML###'
   O0O0Oo00 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
   III1I1I11 = os . path . join ( O0O0Oo00 , 'advancedsettings.xml' )
   try :
    os . remove ( III1I1I11 )
    print '=== GenieTv - REMOVING    ' + str ( III1I1I11 ) + '    ==='
   except :
    pass
   iiI1 = o0oOoO00o . http_GET ( url ) . content
   iII1ii1 = open ( III1I1I11 , "w" )
   iII1ii1 . write ( iiI1 )
   iII1ii1 . close ( )
   print '=== GenieTv - WRITING NEW    ' + str ( III1I1I11 ) + '    ==='
   oO = xbmcgui . Dialog ( )
   oO . ok ( Oo0oO0ooo , "       Done Adding new Advanced XML" )
 else :
  print '###' + Oo0oO0ooo + ' - ADVANCED XML###'
  O0O0Oo00 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
  III1I1I11 = os . path . join ( O0O0Oo00 , 'advancedsettings.xml' )
  try :
   os . remove ( III1I1I11 )
   print '=== GenieTv - REMOVING    ' + str ( III1I1I11 ) + '    ==='
  except :
   pass
  iiI1 = o0oOoO00o . http_GET ( url ) . content
  iII1ii1 = open ( III1I1I11 , "w" )
  iII1ii1 . write ( iiI1 )
  iII1ii1 . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( III1I1I11 ) + '    ==='
  oO = xbmcgui . Dialog ( )
  oO . ok ( Oo0oO0ooo , "       Done Adding new Advanced XML" )
 return
 if 85 - 85: ii11ii1ii * I1IiI % Oooo0Ooo000
def i1iIIIiI ( url , name ) :
 print '###' + Oo0oO0ooo + ' - CHECK ADVANCE XML###'
 O0O0Oo00 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 III1I1I11 = os . path . join ( O0O0Oo00 , 'advancedsettings.xml' )
 try :
  iII1ii1 = open ( III1I1I11 ) . read ( )
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
 oO = xbmcgui . Dialog ( )
 oO . ok ( Oo0oO0ooo , "[COLOR yellow]YOU HAVE[/COLOR] " + name + "[COLOR yellow] XML SETTINGS SETUP[/COLOR]" )
 return
 if 47 - 47: o00OO00OoO % i1I111II1I * Ooo00oOo00o . iIii1I11I1II1 % Oo + OoooooooOO
def I1Ii111I111 ( url ) :
 print '###' + Oo0oO0ooo + ' - DELETING ADVANCE XML###'
 O0O0Oo00 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 III1I1I11 = os . path . join ( O0O0Oo00 , 'advancedsettings.xml' )
 try :
  os . remove ( III1I1I11 )
  oO = xbmcgui . Dialog ( )
  print '=== GenieTv - DELETING    ' + str ( III1I1I11 ) + '    ==='
  oO . ok ( Oo0oO0ooo , "       Remove Advanced Settings Sucessfull" )
 except :
  oO = xbmcgui . Dialog ( )
  oO . ok ( Oo0oO0ooo , "       No Advanced Settings To Remove" )
 return
 if 7 - 7: OOOo0
 if 40 - 40: OOO0OOo
 if 80 - 80: OOOo0 * o00OO00OoO % O0ooOooooO . i11iIiiIii % OoOo00o
 if 42 - 42: OoooooooOO * OoOoOO00
 if 53 - 53: o00OO00OoO + i1IIi . Ooo00oOo00o / i11iIiiIii + iI % I1IiI
 if 9 - 9: OOO0OOo . Oooo0Ooo000 - Oo . o00OO00OoO
 if 39 - 39: i1I111II1I
 if 70 - 70: OoOo00o % Ooo00oOo00o % OOOo0
 if 95 - 95: I1IiI - o00OO00OoO / O0 * OOOo0 - OOooOOo
 if 12 - 12: iIii1I11I1II1 % Oo . i1I111ii1II1i . OoOo00o % i11iIiiIii
def IIiI1I11ii1i ( url = 'http://www.iplocation.net/' , inc = 1 ) :
 oo0O0oO = re . compile ( "<td width='80'>(.+?)</td><td>(.+?)</td><td>(.+?)</td><td>.+?</td><td>(.+?)</td>" ) . findall ( o0oOoO00o . http_GET ( url ) . content )
 for o0o , ooIi1Iii1 , oooo , I11iii1iIIIIi in oo0O0oO :
  if inc < 2 : oO = xbmcgui . Dialog ( ) ; oO . ok ( 'Check My IP' , "[B][COLOR gold]Your IP Address is: [/COLOR][/B] %s" % o0o , '[B][COLOR gold]Your IP is based in: [/COLOR][/B] %s' % oooo , '[B][COLOR gold]Your Service Provider is:[/COLOR][/B] %s' % I11iii1iIIIIi )
  inc = inc + 1
  if 43 - 43: OOooOOo % OOO0OOo - iI / O0 . OOOo0
  if 74 - 74: O0 % Oooo0Ooo000 % Oooo0Ooo000 . O0
  if 59 - 59: i1I111II1I + O0 % i1I111ii1II1i / Oooo0Ooo000 + I1IiI + iI
  if 32 - 32: ii11ii1ii / Oo . I1IiI + i1I111ii1II1i * I1IiI * OoOo00o
  if 46 - 46: iI
  if 42 - 42: iIii1I11I1II1
  if 32 - 32: Oo - iI . OoooooooOO - OoooooooOO - Oo . iIii1I11I1II1
  if 34 - 34: Oo
  if 31 - 31: i1IIi - Oooo0Ooo000 + o00OO00OoO + OOO0OOo . OOO0OOo . O0
def ii11I ( url , name ) :
 oO = xbmcgui . Dialog ( )
 if oO . yesno ( "GenieTv" , '                                    Install Latest .ini File' ) :
  print '###' + Oo0oO0ooo + ' - CUSTOM FTV INI###'
  O0O0Oo00 = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/plugin.video.GenieTv' , '' ) )
  III1I1I11 = os . path . join ( O0O0Oo00 , 'addons2.ini' )
  iiI1 = o0oOoO00o . http_GET ( url ) . content
  iII1ii1 = open ( III1I1I11 , "w" )
  iII1ii1 . write ( iiI1 )
  iII1ii1 . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( III1I1I11 ) + '    ==='
  oO = xbmcgui . Dialog ( )
  oO . ok ( Oo0oO0ooo , "                               Done Adding New .ini File" )
 return
 if 2 - 2: O0ooOooooO . i1I111II1I
def ii1O0oOOo ( url , name ) :
 oO = xbmcgui . Dialog ( )
 if oO . yesno ( "GenieTv" , '                               Install Custom Settings' ) :
  print '###' + Oo0oO0ooo + ' - CUSTOM FTV SETTINGS###'
  O0O0Oo00 = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/plugin.video.GenieTv' , '' ) )
  III1I1I11 = os . path . join ( O0O0Oo00 , 'settings.xml' )
  iiI1 = o0oOoO00o . http_GET ( url ) . content
  iII1ii1 = open ( III1I1I11 , "w" )
  iII1ii1 . write ( iiI1 )
  iII1ii1 . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( III1I1I11 ) + '    ==='
  oO = xbmcgui . Dialog ( )
  oO . ok ( Oo0oO0ooo , "                               Done Adding New Settings" )
 return
 if 33 - 33: OOOo0 * o00OO00OoO
 if 98 - 98: ii11ii1ii - OoooooooOO / OOOo0 . OOO0OOo - i1IIi
def oOOoOo0OoOO ( ) :
 try :
  OO00o = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/plugin.video.GenieTv' , '' ) )
  if os . path . exists ( OO00o ) == True :
   oO = xbmcgui . Dialog ( )
   if oO . yesno ( "GenieTv" , "                               Delete FTV Guide Database" ) :
    IioOooo0OO0O0 = os . path . join ( OO00o , "source.db" )
    os . unlink ( IioOooo0OO0O0 )
  oO . ok ( "GenieTv" , "                                     FTV Database Reset" )
 except :
  oO = xbmcgui . Dialog ( )
  oO . ok ( Oo0oO0ooo , "               Error Deleting Database No Database To Delete" )
 return
 if 60 - 60: Oooo0Ooo000
 if 74 - 74: OoOoOO00 % iI
 if 43 - 43: OoOoOO00 . i11iIiiIii . iI - I1IiI . o00OO00OoO
 if 15 - 15: ii11ii1ii - iIii1I11I1II1 % OoOoOO00 / Oooo0Ooo000
 if 46 - 46: iIii1I11I1II1
def OooOOOOo ( url ) :
 I11i = urllib2 . Request ( url )
 I11i . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
 o0OoiiI1i = urllib2 . urlopen ( I11i )
 iiI1 = o0OoiiI1i . read ( )
 o0OoiiI1i . close ( )
 return iiI1
 if 96 - 96: OoOo00o
 if 56 - 56: Oooo0Ooo000 / O0ooOooooO - O0ooOooooO
 if 40 - 40: i11iIiiIii * OoOoOO00
 if 57 - 57: O0 * iIii1I11I1II1 % O0 . OoooooooOO
 if 53 - 53: iI / OOOo0 * iI + OOooOOo + O0ooOooooO - Oo
 if 16 - 16: Ooo00oOo00o % o00OO00OoO . i1IIi / ii11ii1ii - O0
 if 85 - 85: i1IIi . i1IIi
def Ii11i1I1 ( params ) :
 plugintools . log ( "freshstart.main_list " + repr ( params ) ) ; OOI1 = plugintools . message_yes_no ( Oo0oO0ooo , "Do you wish to restore your" , "Kodi configuration to default settings?" )
 if OOI1 :
  oooO00oOOooO = xbmcaddon . Addon ( id = oo00 ) . getAddonInfo ( 'path' ) ; oooO00oOOooO = xbmc . translatePath ( oooO00oOOooO ) ;
  iiiiI = os . path . join ( oooO00oOOooO , ".." , ".." ) ; iiiiI = os . path . abspath ( iiiiI ) ; plugintools . log ( "freshstart.main_list xbmcPath=" + iiiiI ) ; Ooo000 = False
  try :
   for o0oO0O00oOo , iIi11i1 , oO00oo0o00o0o in os . walk ( iiiiI , topdown = True ) :
    iIi11i1 [ : ] = [ IiIi1iIIi1 for IiIi1iIIi1 in iIi11i1 if IiIi1iIIi1 not in I1i1iiI1 ]
    for IiI111111IIII in oO00oo0o00o0o :
     try : os . remove ( os . path . join ( o0oO0O00oOo , IiI111111IIII ) )
     except :
      if IiI111111IIII not in [ "Addons15.db" , "MyVideos75.db" , "Textures13.db" , "xbmc.log" ] : Ooo000 = True
      plugintools . log ( "Error removing " + o0oO0O00oOo + " " + IiI111111IIII )
    for IiI111111IIII in iIi11i1 :
     try : os . rmdir ( os . path . join ( o0oO0O00oOo , IiI111111IIII ) )
     except :
      if IiI111111IIII not in [ "Database" , "userdata" ] : Ooo000 = True
      plugintools . log ( "Error removing " + o0oO0O00oOo + " " + IiI111111IIII )
   if not Ooo000 : plugintools . log ( "freshstart.main_list All user files removed, you now have a clean install" ) ; plugintools . message ( Oo0oO0ooo , "The process is complete, you're now back to a fresh Kodi configuration with GenieTv!" , "Please reboot your system or restart Kodi in order for the changes to be applied." )
   else : plugintools . log ( "freshstart.main_list User files partially removed" ) ; plugintools . message ( Oo0oO0ooo , "The process is complete, you're now back to a fresh Kodi configuration with GenieTv" , "Please reboot your system or restart Kodi in order for the changes to be applied." )
  except : plugintools . message ( Oo0oO0ooo , "Problem found" , "Your settings has not been changed" ) ; import traceback ; plugintools . log ( traceback . format_exc ( ) ) ; plugintools . log ( "freshstart.main_list NOT removed" )
  plugintools . add_item ( action = "" , title = "Now Exit Kodi" , folder = False )
 else : plugintools . message ( Oo0oO0ooo , "Your settings" , "has not been changed" ) ; plugintools . add_item ( action = "" , title = "Done" , folder = False )
 I1iIi1iiIIiI ( )
 if 21 - 21: i1I111ii1II1i % OoOo00o % Oo % O0
 if 63 - 63: OoOoOO00 * OOOo0 - OoooooooOO / OOOo0
 if 50 - 50: I1IiI % iI + I1IiI * iI - i1I111II1I
def oooiiI11 ( ) :
 i11IiIiii = [ ]
 i11iI1111ii1I = sys . argv [ 2 ]
 if len ( i11iI1111ii1I ) >= 2 :
  OoOo0 = sys . argv [ 2 ]
  iiIIii = OoOo0 . replace ( '?' , '' )
  if ( OoOo0 [ len ( OoOo0 ) - 1 ] == '/' ) :
   OoOo0 = OoOo0 [ 0 : len ( OoOo0 ) - 2 ]
  O000oo00o000o = iiIIii . split ( '&' )
  i11IiIiii = { }
  for Ii1i1I1 in range ( len ( O000oo00o000o ) ) :
   O0000ooO = { }
   O0000ooO = O000oo00o000o [ Ii1i1I1 ] . split ( '=' )
   if ( len ( O0000ooO ) ) == 2 :
    i11IiIiii [ O0000ooO [ 0 ] ] = O0000ooO [ 1 ]
    if 83 - 83: o00OO00OoO + OOooOOo % O0ooOooooO / Ooo00oOo00o
 return i11IiIiii
 if 59 - 59: iI * i1I111II1I . OoOo00o
IIi1IIIIi = base64 . decodestring ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20v' )
ii1oOoO0o0ooo = base64 . decodestring ( 'L3N0b3JhZ2UvZW11bGF0ZWQvMA==' )
OOOoO = base64 . decodestring ( 'L2dlbmllLnR4dA==' )
oooo0OOO00O00 = base64 . decodestring ( 'LmFyY2hpdGVjdHMueDEwaG9zdC5jb20vdGVzdC93aC50eHQ=' )
iiIIiii = base64 . decodestring ( 'aHR0cDovL2ZpeGVzLmFyY2hpdGVjdHMueDEwaG9zdC5jb20vZml4ZXMudHh0' )
i11I111I1 = base64 . decodestring ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vYXBwcy9hcHBzLnhtbA==' )
IiI1iIiiI1iI = base64 . decodestring ( 'L2FkZG9ucy9uZXcudHh0' )
OOOoO000 = base64 . decodestring ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vdm9kL3ZvZC5waHA=' )
Ooi1IIii1i = base64 . decodestring ( 'L2FkZG9ucy9pcHR2LnR4dA==' )
IIIIIIi1IIi1I11i = base64 . decodestring ( 'L2FkZG9ucy92aWRlby50eHQ=' )
I1OO = base64 . decodestring ( 'L2FkZG9ucy9zcG9ydHMudHh0' )
I11II11IiI11 = base64 . decodestring ( 'L2FkZG9ucy9raWRzLnR4dA==' )
oOO0000 = base64 . decodestring ( 'L2FkZG9ucy9tdXNpYy50eHQ=' )
I11IiiiII = base64 . decodestring ( 'L2FkZG9ucy9wcm9ncmFtcy50eHQ=' )
oO0O0oo = base64 . decodestring ( 'L2FkZG9ucy94eHgudHh0' )
OoooOO0 = base64 . decodestring ( 'L2FkZG9ucy9yZXBvLnR4dA==' )
i1oOOoo0o0OOOO = base64 . decodestring ( 'L2FkZG9ucy9wYWNrcy50eHQ=' )
o0O0O = base64 . decodestring ( 'L2FkZG9ucy9za2lucy50eHQ=' )
OoO = base64 . decodestring ( 'L2FkZG9ucy9hcnQudHh0' )
O0Oo00O = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2dvdGhhbS50eHQ=' )
iiiI11 = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2hlbGl4LnR4dA==' )
IiIi1ii111i1 = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2lzZW5nYXJkLnR4dA==' )
Iii1o00o0 = base64 . decodestring ( 'L2FkZG9ucy9SU1MudHh0' )
III1I11i1iIi = base64 . decodestring ( 'Q1VOVA==' )
def IIIIii ( name , url , mode , iconimage , fanart , description , showcontext = True , allinfo = { } ) :
 O000O = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 Oo00OO0 = True
 oo0O = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 oo0O . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 oo0O . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  Oo000 = [ ]
  if showcontext == 'fav' :
   Oo000 . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in oOoOooOo0o0 :
   Oo000 . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fanart=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , urllib . quote_plus ( fanart ) , mode ) ) )
  oo0O . addContextMenuItems ( Oo000 )
 Oo00OO0 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = O000O , listitem = oo0O , isFolder = True )
 return Oo00OO0
 if 82 - 82: Ooo00oOo00o + iI
def I1I1IiI1 ( name , url , mode , iconimage , fanart , description ) :
 O000O = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 Oo00OO0 = True
 oo0O = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 oo0O . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 oo0O . setProperty ( "Fanart_Image" , fanart )
 Oo00OO0 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = O000O , listitem = oo0O , isFolder = False )
 return Oo00OO0
 if 11 - 11: i1I111ii1II1i + OoooooooOO * iI . OOooOOo
 if 11 - 11: O0
OoOo0 = oooiiI11 ( )
oOo0 = None
IiI111111IIII = None
Ooo00o0oOo0O0O = None
OOO0000oO = None
iI1i111I1Ii = None
oo00o0 = None
o0Oo0o = None
if 4 - 4: OoooooooOO
if 78 - 78: OoOoOO00
try :
 o0Oo0o = int ( OoOo0 [ "fav_mode" ] )
except :
 pass
 if 96 - 96: Ooo00oOo00o + OOOo0 % Oo
try :
 oOo0 = urllib . unquote_plus ( OoOo0 [ "url" ] )
except :
 pass
try :
 IiI111111IIII = urllib . unquote_plus ( OoOo0 [ "name" ] )
except :
 pass
try :
 OOO0000oO = urllib . unquote_plus ( OoOo0 [ "iconimage" ] )
except :
 pass
try :
 Ooo00o0oOo0O0O = int ( OoOo0 [ "mode" ] )
except :
 pass
try :
 iI1i111I1Ii = urllib . unquote_plus ( OoOo0 [ "fanart" ] )
except :
 pass
try :
 oo00o0 = urllib . unquote_plus ( OoOo0 [ "description" ] )
except :
 pass
 if 21 - 21: I1IiI - i11iIiiIii - I1IiI
 if 4 - 4: Oooo0Ooo000 . OoOo00o
print str ( O0OoO000O0OO ) + ': ' + str ( iI111I11I1I1 )
print "Mode: " + str ( Ooo00o0oOo0O0O )
print "URL: " + str ( oOo0 )
print "Name: " + str ( IiI111111IIII )
print "IconImage: " + str ( OOO0000oO )
if 39 - 39: i1I111II1I . Oo - I1IiI * i11iIiiIii
if 4 - 4: I1IiI * O0 - Oooo0Ooo000
def O00Oo000ooO0 ( content , viewType ) :
 if 72 - 72: Oooo0Ooo000 + OOO0OOo / OOOo0 . OoOo00o % Ooo00oOo00o / i11iIiiIii
 if content :
  xbmcplugin . setContent ( int ( sys . argv [ 1 ] ) , content )
 if iiIIIII1i1iI . getSetting ( 'auto-view' ) == 'true' :
  xbmc . executebuiltin ( "Container.SetViewMode(%s)" % iiIIIII1i1iI . getSetting ( viewType ) )
  if 13 - 13: o00OO00OoO % OOooOOo + i1I111II1I + o00OO00OoO + i11iIiiIii - ii11ii1ii
  if 70 - 70: OoOoOO00 * OoOoOO00 . OOOo0
if Ooo00o0oOo0O0O == None :
 o0OOoo0OO0OOO ( )
 if 11 - 11: i1I111ii1II1i
elif Ooo00o0oOo0O0O == 1 :
 oOo0oO ( oOo0 )
 if 20 - 20: iI . o00OO00OoO % iI
elif Ooo00o0oOo0O0O == 44 :
 OoOoo0oO ( oOo0 )
 if 5 - 5: i1I111II1I + i1I111ii1II1i
elif Ooo00o0oOo0O0O == 2 :
 OOOooo ( )
 if 23 - 23: o00OO00OoO % iIii1I11I1II1 . Oooo0Ooo000
elif Ooo00o0oOo0O0O == 3 :
 ii1O000OOO0OOo ( )
 if 95 - 95: Oo + i11iIiiIii % i1I111II1I - O0ooOooooO
elif Ooo00o0oOo0O0O == 21 :
 I1iII1iiII ( )
 if 11 - 11: ii11ii1ii / O0 + OoOoOO00
elif Ooo00o0oOo0O0O == 4 :
 o00oO ( )
 if 95 - 95: o00OO00OoO + OoOo00o * iIii1I11I1II1
elif Ooo00o0oOo0O0O == 5 :
 I1I1iI ( IiI111111IIII , oOo0 , oo00o0 )
 if 17 - 17: Ooo00oOo00o - Oo * O0 / iI
elif Ooo00o0oOo0O0O == 6 :
 O0III1Iiii1i11 ( oOo0 )
 if 19 - 19: i1IIi - iIii1I11I1II1 . Oooo0Ooo000
elif Ooo00o0oOo0O0O == 7 :
 I1i1Ii ( oOo0 , IiI111111IIII )
 if 2 - 2: iI
elif Ooo00o0oOo0O0O == 8 :
 i1iIIIiI ( oOo0 , IiI111111IIII )
 if 12 - 12: i11iIiiIii - iIii1I11I1II1 * OoOo00o * i1I111ii1II1i
elif Ooo00o0oOo0O0O == 9 :
 FIXREPOSADDONS ( oOo0 )
 if 19 - 19: O0 + O0ooOooooO + OOooOOo
elif Ooo00o0oOo0O0O == 10 :
 OOooOoooOoOo ( )
 if 81 - 81: iIii1I11I1II1
elif Ooo00o0oOo0O0O == 11 :
 I1Ii111I111 ( oOo0 )
 if 51 - 51: OOooOOo . ii11ii1ii * iI / Oo * OoOoOO00 / O0
elif Ooo00o0oOo0O0O == 12 :
 IIiI1I11ii1i ( )
 if 44 - 44: i11iIiiIii % o00OO00OoO % O0ooOooooO + Oooo0Ooo000 * O0ooOooooO . iI
elif Ooo00o0oOo0O0O == 13 :
 o0oOOO ( )
 if 89 - 89: OoooooooOO % OoOoOO00 - Ooo00oOo00o % i11iIiiIii
elif Ooo00o0oOo0O0O == 14 :
 IIiI ( oOo0 )
 if 7 - 7: OoOo00o
elif Ooo00o0oOo0O0O == 15 :
 OO0ooo0o0O0Oooooo ( )
 if 15 - 15: Oo + i1I111ii1II1i + OOOo0 * OOooOOo
elif Ooo00o0oOo0O0O == 16 :
 ii11I ( oOo0 , IiI111111IIII )
 if 33 - 33: OOooOOo * Oo
elif Ooo00o0oOo0O0O == 17 :
 ii1O0oOOo ( oOo0 , IiI111111IIII )
 if 88 - 88: o00OO00OoO % i1I111II1I - I1IiI - I1IiI . OOOo0
elif Ooo00o0oOo0O0O == 18 :
 oOOoOo0OoOO ( )
 if 52 - 52: OoOoOO00 / OoOoOO00 / OOOo0 - o00OO00OoO
elif Ooo00o0oOo0O0O == 19 :
 o000O000 ( IiI111111IIII , oOo0 , oo00o0 )
 if 91 - 91: OOOo0 + OOooOOo % OoOoOO00 + Ooo00oOo00o
elif Ooo00o0oOo0O0O == 40 :
 ii1Ii1IiIIi ( IiI111111IIII , oOo0 , oo00o0 )
 if 66 - 66: iIii1I11I1II1 * OoOoOO00 % Oo % OOOo0 - iI
elif Ooo00o0oOo0O0O == 42 :
 ooO0oO00O0o ( IiI111111IIII , oOo0 , oo00o0 )
 if 59 - 59: OoOo00o % O0ooOooooO
elif Ooo00o0oOo0O0O == 43 :
 iiiIIiIi ( IiI111111IIII , oOo0 , oo00o0 )
 if 21 - 21: OoooooooOO % I1IiI - I1IiI / ii11ii1ii / OOooOOo
elif Ooo00o0oOo0O0O == 20 :
 i111 ( oOo0 )
 if 15 - 15: OOO0OOo / OOO0OOo % OoooooooOO . o00OO00OoO
elif Ooo00o0oOo0O0O == 22 :
 O00OOO000oo0 ( oOo0 )
 if 93 - 93: ii11ii1ii * ii11ii1ii / OoooooooOO
elif Ooo00o0oOo0O0O == 23 :
 I1iIiiIi ( oOo0 )
 if 6 - 6: ii11ii1ii * Oo + iIii1I11I1II1
elif Ooo00o0oOo0O0O == 24 :
 o0iii1i ( oOo0 )
 if 19 - 19: O0 % OoOoOO00 * OOooOOo
elif Ooo00o0oOo0O0O == 25 :
 IiII ( oOo0 )
 if 27 - 27: i1I111II1I * OoOo00o / i11iIiiIii - O0ooOooooO + OoOoOO00
elif Ooo00o0oOo0O0O == 26 :
 II1iII1 ( oOo0 )
 if 43 - 43: ii11ii1ii - OoOoOO00
elif Ooo00o0oOo0O0O == 27 :
 i1iiii1 ( oOo0 )
 if 56 - 56: ii11ii1ii . i1IIi / i1I111ii1II1i % O0ooOooooO / O0 * Oooo0Ooo000
elif Ooo00o0oOo0O0O == 28 :
 iIOO0O ( oOo0 )
 if 98 - 98: O0 + i1I111ii1II1i
elif Ooo00o0oOo0O0O == 29 :
 i1Ii1i11ii ( oOo0 )
 if 23 - 23: OoooooooOO . iIii1I11I1II1 / i1IIi
elif Ooo00o0oOo0O0O == 30 :
 I1iIiI11I1 ( oOo0 )
 if 31 - 31: Oo - iIii1I11I1II1 / Oooo0Ooo000 . Ooo00oOo00o
elif Ooo00o0oOo0O0O == 31 :
 OO0oO0Oo ( oOo0 )
 if 74 - 74: Oo - OoOoOO00 - OoOo00o
elif Ooo00o0oOo0O0O == 32 :
 i1I1iI ( )
 if 50 - 50: OOOo0 - O0ooOooooO + O0ooOooooO * Oooo0Ooo000 + O0ooOooooO
elif Ooo00o0oOo0O0O == 33 :
 iIiIi1I ( )
 if 70 - 70: i1IIi % Ooo00oOo00o / i1IIi
elif Ooo00o0oOo0O0O == 35 :
 Ii1i1i1111 ( oOo0 )
 if 30 - 30: I1IiI - i11iIiiIii
elif Ooo00o0oOo0O0O == 34 :
 o0oo00oO00o0 ( oOo0 )
 if 94 - 94: I1IiI % i1I111ii1II1i
elif Ooo00o0oOo0O0O == 36 :
 IiII1II11I ( oOo0 )
 if 39 - 39: I1IiI + o00OO00OoO % O0
elif Ooo00o0oOo0O0O == 37 :
 I1I1i11 ( oOo0 )
 if 26 - 26: OOO0OOo + I1IiI
elif Ooo00o0oOo0O0O == 38 :
 oOOOO ( oOo0 )
 if 17 - 17: ii11ii1ii - i1I111ii1II1i % Oo * O0 % O0 * i1I111II1I
elif Ooo00o0oOo0O0O == 41 :
 Ii11i1I1 ( OoOo0 )
 if 6 - 6: o00OO00OoO
elif Ooo00o0oOo0O0O == 39 :
 oooOOO ( oOo0 )
 if 46 - 46: OoOoOO00 * o00OO00OoO
elif Ooo00o0oOo0O0O == 45 :
 TEXTS ( )
 if 23 - 23: i1IIi - O0
elif Ooo00o0oOo0O0O == 46 :
 iiii1Ii1iii ( )
 if 6 - 6: OOO0OOo % OoooooooOO * o00OO00OoO - OoOo00o
elif Ooo00o0oOo0O0O == 47 :
 GEVID ( )
 if 24 - 24: Oooo0Ooo000 / iIii1I11I1II1 . OoooooooOO % I1IiI . iI
elif Ooo00o0oOo0O0O == 48 :
 i11I1II ( IiI111111IIII , oOo0 , oo00o0 )
 if 73 - 73: o00OO00OoO
elif Ooo00o0oOo0O0O == 49 :
 I1Ii1111iIi ( )
 if 25 - 25: OoOo00o
elif Ooo00o0oOo0O0O == 222 :
 iIIIiIi ( oOo0 )
 if 77 - 77: OOooOOo . iIii1I11I1II1 . OoooooooOO . iIii1I11I1II1
elif Ooo00o0oOo0O0O == 333 :
 ii11 ( oOo0 )
 if 87 - 87: OoOoOO00 - OoooooooOO / i1IIi . iI - Oo . i11iIiiIii
 if 47 - 47: Oo % Ooo00oOo00o - OOO0OOo - Oo * O0ooOooooO
elif Ooo00o0oOo0O0O == 1020 :
 oO0OO ( )
 if 72 - 72: OOooOOo % OOooOOo + i1I111ii1II1i + ii11ii1ii / Oo
elif Ooo00o0oOo0O0O == 1021 :
 ANIMEEP ( )
 if 30 - 30: Oo + OOOo0 + i11iIiiIii / Ooo00oOo00o
elif Ooo00o0oOo0O0O == 1022 :
 ANIMEPLAY ( oOo0 )
 if 64 - 64: OoOo00o
elif Ooo00o0oOo0O0O == 1001 :
 i1iI1I1IIIi1i ( )
 if 80 - 80: OOOo0 - i11iIiiIii / Ooo00oOo00o / I1IiI + I1IiI
elif Ooo00o0oOo0O0O == 1005 :
 o00O ( )
 if 89 - 89: O0 + OoOo00o * o00OO00OoO
elif Ooo00o0oOo0O0O == 1007 :
 IIIIIiiI ( oOo0 )
 if 30 - 30: I1IiI
elif Ooo00o0oOo0O0O == 1010 :
 o00oo ( oOo0 )
 if 39 - 39: ii11ii1ii + OOooOOo + o00OO00OoO + OoOo00o
elif Ooo00o0oOo0O0O == 1011 :
 O000Oo00 ( oOo0 )
 if 48 - 48: o00OO00OoO / OOO0OOo . iIii1I11I1II1
elif Ooo00o0oOo0O0O == 1030 :
 iI1 ( )
 if 72 - 72: i1IIi . OOooOOo
elif Ooo00o0oOo0O0O == 1031 :
 oOoo ( oOo0 , OOO0000oO )
 if 3 - 3: I1IiI % OoOoOO00 - O0
elif Ooo00o0oOo0O0O == 1006 :
 Parse . ParseURL ( oOo0 )
 if 52 - 52: Ooo00oOo00o
elif Ooo00o0oOo0O0O == 2030 :
 Parse . addonParseURL ( oOo0 )
 if 49 - 49: iI . ii11ii1ii % OOO0OOo . Oo * i1I111II1I
elif Ooo00o0oOo0O0O == 2031 :
 Parse . apkParseURL ( oOo0 )
 if 44 - 44: iIii1I11I1II1 / O0 * Oo + OOOo0 . OOO0OOo
elif Ooo00o0oOo0O0O == 1002 :
 o0oo00O ( oOo0 )
 if 20 - 20: i1I111ii1II1i + OOooOOo . o00OO00OoO / i11iIiiIii
elif Ooo00o0oOo0O0O == 1003 :
 IIIIII1iI1II ( oOo0 , OOO0000oO )
 if 7 - 7: I1IiI / I1IiI . o00OO00OoO * O0 + OoOo00o + O0ooOooooO
elif Ooo00o0oOo0O0O == 1004 :
 iiiI1 ( oOo0 )
 if 98 - 98: OoOoOO00 * OoOo00o - OOOo0 % OOooOOo - i1I111ii1II1i % ii11ii1ii
elif Ooo00o0oOo0O0O == 1008 :
 O0Ooo0O ( )
 if 69 - 69: i1IIi % Ooo00oOo00o % o00OO00OoO / OOO0OOo / OOO0OOo
elif Ooo00o0oOo0O0O == 1009 :
 M3UPLAY ( oOo0 )
 if 6 - 6: OoOoOO00 % ii11ii1ii % i1IIi * OOO0OOo
elif Ooo00o0oOo0O0O == 2001 :
 oO0Oo0OOoo0oo ( oOo0 )
 if 47 - 47: O0
elif Ooo00o0oOo0O0O == 1013 :
 oOoOoo0 ( )
 if 55 - 55: Ooo00oOo00o % O0 / OoooooooOO
elif Ooo00o0oOo0O0O == 1014 :
 I111III1 ( )
 if 49 - 49: OOOo0 . Ooo00oOo00o * OoooooooOO % i11iIiiIii + iIii1I11I1II1 * i1IIi
elif Ooo00o0oOo0O0O == 1015 :
 OOO000OOo0o0O ( oOo0 )
 if 88 - 88: ii11ii1ii * i1I111ii1II1i + OoOoOO00
elif Ooo00o0oOo0O0O == 1016 :
 I11i1i11IiIi1 ( oOo0 )
 if 62 - 62: OoooooooOO
elif Ooo00o0oOo0O0O == 1023 :
 I1iii11 ( )
 if 33 - 33: O0 . i11iIiiIii % OOooOOo
elif Ooo00o0oOo0O0O == 1024 :
 oOoOO0O00o ( )
 if 50 - 50: OOO0OOo
elif Ooo00o0oOo0O0O == 1025 :
 o0OOOO ( oOo0 )
 if 81 - 81: i11iIiiIii * iIii1I11I1II1 / Oo * i1I111II1I
elif Ooo00o0oOo0O0O == 4001 :
 iII ( )
 if 83 - 83: i11iIiiIii - OOOo0 * i11iIiiIii
elif Ooo00o0oOo0O0O == 4002 :
 o0ooOooo000oOO ( )
 if 59 - 59: i1I111ii1II1i - OoooooooOO / OOO0OOo + ii11ii1ii . OOooOOo - i1I111ii1II1i
elif Ooo00o0oOo0O0O == 4003 :
 i1iiIiI1Ii1i ( )
 if 29 - 29: O0ooOooooO
elif Ooo00o0oOo0O0O == 4004 :
 ii1ii1ii ( )
 if 26 - 26: O0 % i1I111II1I - OoOo00o . i1I111II1I
elif Ooo00o0oOo0O0O == 4005 :
 oOOo0 ( )
 if 70 - 70: OOooOOo + Oooo0Ooo000 / i1I111ii1II1i + OOO0OOo / OOOo0
elif Ooo00o0oOo0O0O == 4006 :
 oo00O00oO ( )
 if 33 - 33: OoooooooOO . O0
elif Ooo00o0oOo0O0O == 4007 :
 iIiIIIi ( )
 if 59 - 59: iIii1I11I1II1
elif Ooo00o0oOo0O0O == 4008 :
 ooo00OOOooO ( )
 if 45 - 45: O0
elif Ooo00o0oOo0O0O == 4009 : oooooOoo0ooo ( )
elif Ooo00o0oOo0O0O == 4010 : I1i1i1 ( )
elif Ooo00o0oOo0O0O == 3000 :
 I1111I1Ii ( )
 if 78 - 78: Oooo0Ooo000 - iIii1I11I1II1 + o00OO00OoO - ii11ii1ii - o00OO00OoO
elif Ooo00o0oOo0O0O == 3001 :
 i1I111Ii ( )
 if 21 - 21: OoooooooOO . O0 / i11iIiiIii
elif Ooo00o0oOo0O0O == 3002 :
 i11i1i ( oOo0 )
 if 86 - 86: I1IiI / i1I111II1I
elif Ooo00o0oOo0O0O == 3003 :
 I1ii1Ii1 ( oOo0 )
 if 40 - 40: iIii1I11I1II1 / OOO0OOo / OOOo0 + ii11ii1ii * i1I111II1I
elif Ooo00o0oOo0O0O == 3004 :
 iI111I1III ( oOo0 )
 if 1 - 1: Ooo00oOo00o * OOO0OOo + OoOo00o . O0ooOooooO / OOO0OOo
elif Ooo00o0oOo0O0O == 404 :
 ooOi1i1i11iI11II ( IiI111111IIII , oOo0 , OOO0000oO )
 if 91 - 91: iI + Oooo0Ooo000 - Oo % I1IiI . i1I111ii1II1i
elif Ooo00o0oOo0O0O == 405 :
 o000Ooo00o00O ( oOo0 )
 if 51 - 51: i1I111II1I / Oooo0Ooo000
elif Ooo00o0oOo0O0O == 7030 :
 iIiiii1I ( )
 if 51 - 51: OOO0OOo * O0ooOooooO - o00OO00OoO + i1I111ii1II1i
elif Ooo00o0oOo0O0O == 7021 :
 iIIi111IiII1i ( IiI111111IIII )
 if 46 - 46: OOooOOo - i11iIiiIii % Ooo00oOo00o / iI - I1IiI
elif Ooo00o0oOo0O0O == 7022 :
 OO ( IiI111111IIII )
 if 88 - 88: O0ooOooooO * OOOo0 / Ooo00oOo00o - i1I111II1I / i1IIi . o00OO00OoO
elif Ooo00o0oOo0O0O == 7000 :
 i1II11i1iI1 ( IiI111111IIII , oOo0 , img )
 if 26 - 26: i11iIiiIii - OOO0OOo
elif Ooo00o0oOo0O0O == 7050 :
 i1i1Ii1IiIII ( oOo0 )
 if 45 - 45: OOO0OOo + OoOoOO00 % i1I111ii1II1i
elif Ooo00o0oOo0O0O == 7051 :
 oO000o0OO0OO0 ( oOo0 )
 if 55 - 55: OOO0OOo - O0ooOooooO % OOOo0
elif Ooo00o0oOo0O0O == 7052 :
 oooOo00000 ( oOo0 )
 if 61 - 61: OOO0OOo
elif Ooo00o0oOo0O0O == 7053 :
 IiI1IiI1iiI1 ( oOo0 )
 if 22 - 22: iIii1I11I1II1 / OOO0OOo / OOOo0 - OOooOOo
elif Ooo00o0oOo0O0O == 7054 :
 CoolPlay ( oOo0 )
 if 21 - 21: O0ooOooooO . i11iIiiIii * Oooo0Ooo000 . i1I111II1I / i1I111II1I
elif Ooo00o0oOo0O0O == 7060 :
 ooOoOo ( )
 if 42 - 42: OoooooooOO / o00OO00OoO . OOooOOo / O0 - OoOo00o * OoOo00o
elif Ooo00o0oOo0O0O == 7061 :
 o0O00OooooO ( oOo0 )
 if 1 - 1: iI % o00OO00OoO
elif Ooo00o0oOo0O0O == 7063 :
 iIiii1iI1i ( oOo0 )
 if 97 - 97: I1IiI
elif Ooo00o0oOo0O0O == 7062 :
 o00o0o000Oo ( oOo0 )
 if 13 - 13: I1IiI % i1I111II1I . O0 / Oo % Oo
elif Ooo00o0oOo0O0O == 7064 :
 NATatozcat ( )
 if 19 - 19: o00OO00OoO % OOO0OOo - OOO0OOo % OOOo0 . i1I111II1I - OoooooooOO
elif Ooo00o0oOo0O0O == 7067 :
 oOIIII ( oOo0 )
 if 100 - 100: OOOo0 + iI + OOooOOo . i1IIi % OoooooooOO
elif Ooo00o0oOo0O0O == 7066 :
 NATatozA ( oOo0 )
 if 64 - 64: O0 % i1IIi * o00OO00OoO - iI + Oo
elif Ooo00o0oOo0O0O == 7065 :
 ooOOo ( oOo0 )
 if 65 - 65: I1IiI . i11iIiiIii
elif Ooo00o0oOo0O0O == 7070 :
 II1ii1Ii ( )
 if 36 - 36: O0ooOooooO * i1I111ii1II1i + OoOo00o * i1I111ii1II1i . ii11ii1ii - iIii1I11I1II1
elif Ooo00o0oOo0O0O == 7071 :
 DIZIlist ( oOo0 )
 if 14 - 14: Oooo0Ooo000 * O0ooOooooO + i11iIiiIii
elif Ooo00o0oOo0O0O == 7072 :
 DIZIpull ( oOo0 )
 if 84 - 84: i1I111ii1II1i / OoOoOO00
elif Ooo00o0oOo0O0O == 7073 :
 WATCHDIZI ( oOo0 )
 if 86 - 86: OOOo0
elif Ooo00o0oOo0O0O == 7002 :
 iIIO0ooo ( )
 if 97 - 97: OoOoOO00
elif Ooo00o0oOo0O0O == 7003 :
 o00O0o ( oOo0 )
 if 38 - 38: OOOo0
elif Ooo00o0oOo0O0O == 7004 :
 o0oOo ( oOo0 )
 if 42 - 42: OOooOOo
elif Ooo00o0oOo0O0O == 7020 :
 iiIIi11ii1Ii ( oOo0 )
 if 8 - 8: i11iIiiIii / OOO0OOo
elif Ooo00o0oOo0O0O == 7001 :
 o0oO0oo ( )
 if 33 - 33: o00OO00OoO * OoOo00o - O0 + OOOo0 / OoOo00o
elif Ooo00o0oOo0O0O == 7010 :
 oOOO0o ( oOo0 )
 if 19 - 19: i1IIi % OoOoOO00
elif Ooo00o0oOo0O0O == 7011 :
 oOOO00oOO ( oOo0 )
 if 85 - 85: OoOo00o - OOooOOo % i1I111II1I - OoOoOO00
elif Ooo00o0oOo0O0O == 7012 :
 o00oOoo0o00 ( oOo0 )
 if 56 - 56: iI * i11iIiiIii
elif Ooo00o0oOo0O0O == 7013 :
 cnfTVPlay2 ( oOo0 )
elif Ooo00o0oOo0O0O == 7014 :
 CNF_Studio_Indexer . MV_Movies ( oOo0 )
elif Ooo00o0oOo0O0O == 7015 :
 CNF_Studio_Indexer . Movie_ByYear ( oOo0 )
elif Ooo00o0oOo0O0O == 7016 :
 CNF_Studio_Indexer . Resolve_CNF_Link ( IiI111111IIII , oOo0 , OOO0000oO )
elif Ooo00o0oOo0O0O == 7017 :
 CNF_Studio_Indexer . Search_Movie ( )
elif Ooo00o0oOo0O0O == 7018 :
 I11iIi ( )
elif Ooo00o0oOo0O0O == 7019 :
 CNF_Studio_Indexer . List_Movies ( oOo0 )
elif Ooo00o0oOo0O0O == 7020 :
 CNF_Studio_Indexer . Get_Movie_Page ( oOo0 )
elif Ooo00o0oOo0O0O == 7024 :
 CNF_Studio_Indexer . Box_Office ( oOo0 )
 if 92 - 92: OoOoOO00 - O0 . o00OO00OoO
elif Ooo00o0oOo0O0O == 8000 :
 i1i1I11i1I ( )
elif Ooo00o0oOo0O0O == 8001 :
 o0OIi ( )
elif Ooo00o0oOo0O0O == 8002 :
 oO0oo0O0 ( )
elif Ooo00o0oOo0O0O == 8003 :
 i1IiIiIiiI1 ( )
elif Ooo00o0oOo0O0O == 8004 :
 ooOO0OOO00o ( )
elif Ooo00o0oOo0O0O == 8005 :
 oOO00OO0o0O ( )
elif Ooo00o0oOo0O0O == 8006 :
 ii111iI1i1 ( IiI111111IIII , oOo0 )
elif Ooo00o0oOo0O0O == 8030 :
 oO0oOOoo00000 ( oOo0 )
elif Ooo00o0oOo0O0O == 8045 :
 iIIiIi ( oOo0 )
elif Ooo00o0oOo0O0O == 8046 :
 oO0Oo00oo ( oOo0 )
elif Ooo00o0oOo0O0O == 8047 :
 OOOO0O00Ooooo ( oOo0 )
elif Ooo00o0oOo0O0O == 8020 :
 IiiII ( )
elif Ooo00o0oOo0O0O == 8021 :
 I1ii1iI ( oOo0 )
elif Ooo00o0oOo0O0O == 8022 :
 i1i1IIi ( oOo0 )
elif Ooo00o0oOo0O0O == 8023 :
 i1Ii1i1ii1 ( oOo0 )
elif Ooo00o0oOo0O0O == 8040 :
 i11IiI1iiI11 ( )
elif Ooo00o0oOo0O0O == 8041 :
 OOoOOOO00 ( oOo0 )
elif Ooo00o0oOo0O0O == 8042 :
 Oo0O0000Oo00o ( oOo0 )
elif Ooo00o0oOo0O0O == 8043 :
 yt . PlayVideo ( oOo0 )
elif Ooo00o0oOo0O0O == 8044 :
 II1ii ( oOo0 )
elif Ooo00o0oOo0O0O == 8060 :
 iII1I11 ( )
elif Ooo00o0oOo0O0O == 8061 :
 ii11iiI11I ( oOo0 )
elif Ooo00o0oOo0O0O == 8064 :
 iiIi11i1IiI ( )
elif Ooo00o0oOo0O0O == 8065 :
 oO00O0O0 ( oOo0 )
elif Ooo00o0oOo0O0O == 8070 :
 oOO0 ( )
elif Ooo00o0oOo0O0O == 8071 :
 O00O00OoO ( oOo0 )
elif Ooo00o0oOo0O0O == 7080 :
 IiIiI1i1 ( oOo0 )
elif Ooo00o0oOo0O0O == 8090 :
 oOoO0Oo0 ( )
elif Ooo00o0oOo0O0O == 8091 :
 i11i11i ( oOo0 )
elif Ooo00o0oOo0O0O == 8092 :
 iiI1iI ( oOo0 )
elif Ooo00o0oOo0O0O == 8081 :
 Ii11III ( )
elif Ooo00o0oOo0O0O == 8062 :
 iIIiI1111 ( oOo0 )
elif Ooo00o0oOo0O0O == 8063 :
 Ii1111III1 ( oOo0 )
elif Ooo00o0oOo0O0O == 8050 :
 Iii ( )
elif Ooo00o0oOo0O0O == 8051 :
 i1I1 ( oOo0 )
elif Ooo00o0oOo0O0O == 8052 :
 O0II11i11II ( oOo0 )
elif Ooo00o0oOo0O0O == 8085 :
 iI111II1ii ( )
elif Ooo00o0oOo0O0O == 8086 :
 IIiI1I ( oOo0 )
elif Ooo00o0oOo0O0O == 8087 :
 iIII11Iiii1 ( oOo0 )
elif Ooo00o0oOo0O0O == 8088 :
 o0oo0 ( oOo0 , IiI111111IIII )
elif Ooo00o0oOo0O0O == 9000 :
 ii1O0 ( )
elif Ooo00o0oOo0O0O == 1111 :
 ooooO0o000oOO ( )
elif Ooo00o0oOo0O0O == 9001 :
 ooo0O00000oo0 ( )
elif Ooo00o0oOo0O0O == 9002 :
 I111 ( )
elif Ooo00o0oOo0O0O == 9003 :
 III1ii ( )
elif Ooo00o0oOo0O0O == 50 :
 ooOoo0o0O ( oOo0 )
elif Ooo00o0oOo0O0O == 9020 :
 champlist ( )
elif Ooo00o0oOo0O0O == 9021 :
 o0Ii11iIiiI ( )
elif Ooo00o0oOo0O0O == 9022 :
 o000 ( )
elif Ooo00o0oOo0O0O == 9023 :
 i11ii1 ( )
elif Ooo00o0oOo0O0O == 9024 :
 o0OoOoo ( oOo0 )
elif Ooo00o0oOo0O0O == 9030 :
 i111iii1I1 ( oOo0 )
elif Ooo00o0oOo0O0O == 9031 :
 iiIiII1 ( oOo0 )
elif Ooo00o0oOo0O0O == 9032 :
 ii111iI ( oOo0 )
elif Ooo00o0oOo0O0O == 9033 :
 ii11I1 ( oOo0 )
elif Ooo00o0oOo0O0O == 7085 :
 i111o0o0oO ( oOo0 )
elif Ooo00o0oOo0O0O == 7086 :
 O0o0O0O0O ( oOo0 )
elif Ooo00o0oOo0O0O == 7087 :
 IiiIi1I11 ( oo00o0 )
elif Ooo00o0oOo0O0O == 9666 :
 iII1 ( oOo0 )
elif Ooo00o0oOo0O0O == 10100 : II1IIi1iII1i ( )
elif Ooo00o0oOo0O0O == 10105 : O0oooOoO ( oOo0 )
elif Ooo00o0oOo0O0O == 10106 : Oo00oO ( oOo0 )
elif Ooo00o0oOo0O0O == 10104 : i1i1 ( oOo0 )
elif Ooo00o0oOo0O0O == 10107 : o0O0 ( )
elif Ooo00o0oOo0O0O == 10103 : iiiIi ( oOo0 )
elif Ooo00o0oOo0O0O == 10108 : ii11Iiii ( oOo0 )
elif Ooo00o0oOo0O0O == 10107 : o0O0 ( )
elif Ooo00o0oOo0O0O == 10000 : Origin_Menu ( )
elif Ooo00o0oOo0O0O == 10001 : IiiI ( )
elif Ooo00o0oOo0O0O == 10002 : O0000oO0o00 ( )
elif Ooo00o0oOo0O0O == 10003 : Oo00o0OO ( )
elif Ooo00o0oOo0O0O == 10004 : oOoOo00ooOooo ( oOo0 )
elif Ooo00o0oOo0O0O == 10005 : Ii1iIi111i1i1 ( )
elif Ooo00o0oOo0O0O == 10006 : OOoO00oo0000O ( oOo0 )
elif Ooo00o0oOo0O0O == 10007 : i1II1iII ( oOo0 , OOO0000oO )
elif Ooo00o0oOo0O0O == 10008 : ii1II1II ( )
elif Ooo00o0oOo0O0O == 10009 : O00O ( )
elif Ooo00o0oOo0O0O == 10010 : oO0o0o00oOo0O ( oOo0 )
elif Ooo00o0oOo0O0O == 10011 : Ii1I1i111 ( oOo0 )
elif Ooo00o0oOo0O0O == 10012 : OOoO ( oOo0 )
elif Ooo00o0oOo0O0O == 10013 : I1IiII1iI1 ( oOo0 )
elif Ooo00o0oOo0O0O == 10014 : i1i1ii1111i1i ( )
elif Ooo00o0oOo0O0O == 10015 : ooOoO ( )
elif Ooo00o0oOo0O0O == 10016 : Iiii1IiIi ( oOo0 )
elif Ooo00o0oOo0O0O == 10017 : II1Oo00O0Oo0Oo ( )
elif Ooo00o0oOo0O0O == 10018 : o0O0oo0o ( )
elif Ooo00o0oOo0O0O == 10019 : iIiI1iI1i1I ( )
elif Ooo00o0oOo0O0O == 10020 : OOoooOoO0Oo ( )
elif Ooo00o0oOo0O0O == 10021 : oO0O ( )
elif Ooo00o0oOo0O0O == 10022 : OoOi111i ( oOo0 )
elif Ooo00o0oOo0O0O == 10023 : OoO0000o ( IiI111111IIII , oOo0 )
elif Ooo00o0oOo0O0O == 10024 : i11i11 ( oOo0 )
elif Ooo00o0oOo0O0O == 10025 : oO0 ( )
elif Ooo00o0oOo0O0O == 10026 : o0Oo ( )
elif Ooo00o0oOo0O0O == 10027 : oO0O0Ooo ( )
elif Ooo00o0oOo0O0O == 10028 : i1IIi1i1Ii1 ( )
elif Ooo00o0oOo0O0O == 10029 : oO0O000oOo ( )
elif Ooo00o0oOo0O0O == 423 : OOo ( oOo0 )
elif Ooo00o0oOo0O0O == 426 : I11oOOooo ( oOo0 )
elif Ooo00o0oOo0O0O == 10030 : Izle_Films ( )
elif Ooo00o0oOo0O0O == 10031 : Latest_Izle_Movies ( )
elif Ooo00o0oOo0O0O == 10032 : Izle_Genres ( )
elif Ooo00o0oOo0O0O == 10033 : Izle_Pop_Movies ( )
elif Ooo00o0oOo0O0O == 10034 : Izle_Boxsets ( )
elif Ooo00o0oOo0O0O == 10035 : Izle_Search ( )
elif Ooo00o0oOo0O0O == 10036 : Izle_Genres_Movie ( oOo0 )
elif Ooo00o0oOo0O0O == 10037 : Izle_Boxset_single ( oOo0 )
elif Ooo00o0oOo0O0O == 10038 : Izle_IFRAME ( )
elif Ooo00o0oOo0O0O == 10039 : Izle_Boxsets_Next ( oOo0 )
elif Ooo00o0oOo0O0O == 10040 : oOOOo ( )
elif Ooo00o0oOo0O0O == 10041 : IiI ( oOo0 )
elif Ooo00o0oOo0O0O == 10042 : I1ii1 ( oOo0 )
elif Ooo00o0oOo0O0O == 10043 : ooOoooo0 ( )
elif Ooo00o0oOo0O0O == 10044 : i1I1iIii11 ( oOo0 )
elif Ooo00o0oOo0O0O == 10045 : oOo0Oo0O0O ( IiI111111IIII )
elif Ooo00o0oOo0O0O == 10046 : II1i11 ( oOo0 )
elif Ooo00o0oOo0O0O == 10047 : i1iiii ( oOo0 )
elif Ooo00o0oOo0O0O == 10048 : IIiI11I1I1i1i ( oOo0 )
elif Ooo00o0oOo0O0O == 10049 : i1o0oo0Ooooo0 ( oOo0 )
elif Ooo00o0oOo0O0O == 10050 : oooOO0OO0 ( )
elif Ooo00o0oOo0O0O == 10051 : OooOoo ( )
elif Ooo00o0oOo0O0O == 10052 : O0OooOo ( )
elif Ooo00o0oOo0O0O == 10053 : Addon ( oOo0 )
elif Ooo00o0oOo0O0O == 10054 : O0OO ( oOo0 , IiI111111IIII )
elif Ooo00o0oOo0O0O == 10055 :
 IIiIIIIiI ( "addFavorite" )
 try :
  IiI111111IIII = IiI111111IIII . split ( '\\ ' ) [ 1 ]
 except :
  pass
 try :
  IiI111111IIII = IiI111111IIII . split ( '  - ' ) [ 0 ]
 except :
  pass
 I11Ii1iI11iI1 ( IiI111111IIII , oOo0 , OOO0000oO , iI1i111I1Ii , o0Oo0o )
elif Ooo00o0oOo0O0O == 10056 :
 IIiIIIIiI ( "rmFavorite" )
 try :
  IiI111111IIII = IiI111111IIII . split ( '\\ ' ) [ 1 ]
 except :
  pass
 try :
  IiI111111IIII = IiI111111IIII . split ( '  - ' ) [ 0 ]
 except :
  pass
 o0O0oO0 ( IiI111111IIII )
elif Ooo00o0oOo0O0O == 10057 :
 IIiIIIIiI ( "getFavorites" )
 oO00Ooo0oO ( )
elif Ooo00o0oOo0O0O == 10058 : OOoOoOo ( )
elif Ooo00o0oOo0O0O == 10059 : Donators_Guide ( )
elif Ooo00o0oOo0O0O == 10060 : OoOooOoO ( )
elif Ooo00o0oOo0O0O == 10061 : iiI1I1 ( )
elif Ooo00o0oOo0O0O == 10062 : IIi1IIIi ( IiI111111IIII , oOo0 , oo00o0 )
elif Ooo00o0oOo0O0O == 10063 : Ii ( )
elif Ooo00o0oOo0O0O == 10064 : Ii1Io0OO0o0o00o ( )
elif Ooo00o0oOo0O0O == 10065 : i1II1i ( oOo0 )
elif Ooo00o0oOo0O0O == 10066 : Ii1Iii1iIi ( oOo0 )
elif Ooo00o0oOo0O0O == 10068 : ooo ( oOo0 )
elif Ooo00o0oOo0O0O == 10069 : ii1iI1I11I ( oOo0 )
elif Ooo00o0oOo0O0O == 10070 : ii1I1 ( oOo0 )
elif Ooo00o0oOo0O0O == 10071 : Genie_Watch ( )
elif Ooo00o0oOo0O0O == 10072 : ii ( )
elif Ooo00o0oOo0O0O == 10073 : IiI1i ( oOo0 )
elif Ooo00o0oOo0O0O == 10074 : Ii1I ( oOo0 )
elif Ooo00o0oOo0O0O == 10075 : ooiIi1 ( OOO0000oO , IiI111111IIII , oOo0 )
elif Ooo00o0oOo0O0O == 10076 : O000OOO ( oOo0 )
elif Ooo00o0oOo0O0O == 10077 : IIii11I1 ( oOo0 )
elif Ooo00o0oOo0O0O == 10078 : I1I1II1I11 ( )
elif Ooo00o0oOo0O0O == 10079 : Genie_Watch_Tv_Shows ( )
elif Ooo00o0oOo0O0O == 10080 : Genie_Watch_Tv_Genre ( oOo0 )
elif Ooo00o0oOo0O0O == 10081 : Genie_Watch_TV_PlayRun ( oOo0 )
elif Ooo00o0oOo0O0O == 10082 : Genie_Watch_TV_Episodes ( oOo0 , OOO0000oO )
elif Ooo00o0oOo0O0O == 10083 : Genie_Watch_Tv_Recent ( oOo0 )
elif Ooo00o0oOo0O0O == 20000 : IiIIi1I1I11Ii ( )
elif Ooo00o0oOo0O0O == 20001 : oO0oooooo ( )
elif Ooo00o0oOo0O0O == 20002 : Ooo0O0 ( oOo0 )
elif Ooo00o0oOo0O0O == 20003 : iIiI1iiiI1ii ( oOo0 )
elif Ooo00o0oOo0O0O == 20004 : OOoOO0OO ( oOo0 )
elif Ooo00o0oOo0O0O == 21004 : II1i111 ( )
elif Ooo00o0oOo0O0O == 21005 : i1iiiIii11 ( oOo0 )
elif Ooo00o0oOo0O0O == 21006 : oOo0II1i11I1 ( oOo0 )
elif Ooo00o0oOo0O0O == 21007 : I1 ( oOo0 )
elif Ooo00o0oOo0O0O == 30000 : OOoO000O00oO ( )
elif Ooo00o0oOo0O0O == 30001 : o0OOoOoO00 ( )
elif Ooo00o0oOo0O0O == 10012 : Resolve ( oOo0 )
elif Ooo00o0oOo0O0O == 30003 : i11I1I1iiI ( )
elif Ooo00o0oOo0O0O == 30004 : IiiIIiiiiii ( oOo0 )
elif Ooo00o0oOo0O0O == 30005 : ooOo0OoOooo00 ( oOo0 )
elif Ooo00o0oOo0O0O == 30006 : OoooO0o ( )
elif Ooo00o0oOo0O0O == 30007 : IIi1II ( )
elif Ooo00o0oOo0O0O == 30008 : iIi1IiI ( oOo0 )
elif Ooo00o0oOo0O0O == 30009 : Ii11iI ( oOo0 )
elif Ooo00o0oOo0O0O == 30010 : iIIIi1i1I11i ( oOo0 )
elif Ooo00o0oOo0O0O == 30011 : O0O0o0o0o ( )
elif Ooo00o0oOo0O0O == 30012 : o000O0OOoo ( )
elif Ooo00o0oOo0O0O == 30013 : II1 ( )
elif Ooo00o0oOo0O0O == 30014 : O0ooOo0o0Oo ( )
if 59 - 59: I1IiI
xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
