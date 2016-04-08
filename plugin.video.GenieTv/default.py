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
iI111I11I1I1 = "2.5.5"
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
iIi1ii1I1 = xbmc . translatePath ( 'special://home/userdata/' )
o0 = xbmc . translatePath ( 'special://home/userdatabroke/' )
I11II1i = ( oOOoo00O0O ( 'aHR0cDovL3NlZWR1cmdyZWVkLngxMGhvc3QuY29tL29yaWdpbi8=' ) )
IIIII = xbmc . translatePath ( os . path . join ( 'special://home/userdata/addon_data/script.ivueguide/master.db' ) )
ooooooO0oo = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , 'favourites.xml' ) )
IIiiiiiiIi1I1 = xbmc . translatePath ( os . path . join ( 'special://home/userdata/addon_data/plugin.video.GenieTv/favorites' ) )
if os . path . exists ( I11i1 ) == True :
 I1IIIii = open ( I11i1 ) . read ( )
else : I1IIIii = [ ]
oOoOooOo0o0 = iiIIIII1i1iI . getSetting ( 'debug' )
if os . path . exists ( iIii1 ) == False :
 os . makedirs ( iIii1 )
 if 61 - 61: o00oOO0 / iiiiiIIii * o00OO0OOO0 % i1Iii % OOOooOooo00O0
def Oo0OO ( ) :
 if not os . path . exists ( O00ooOO ) :
  i1 . ok ( "[COLOR=white]Incompatible[/COLOR]" , "Unfortunately GenieTv will only work with" , 'its official repo please install from trusted source' , '' )
  oOOoOo00o = 'genie tv repo not being installed '
  o0OOoo0OO0OOO ( oOOoOo00o )
 iI1iI1I1i1I ( )
 iIi11Ii1 ( )
 if iiIIIII1i1iI . getSetting ( 'My Build' ) == 'true' :
  Ii11iII1 ( '[COLORgreen]WIZARD[/COLOR]' , iiI1IiI , 4001 , i1iIIi1 + 'MB.png' , oooOOOOO , '' )
 if iiIIIII1i1iI . getSetting ( 'Streams' ) == 'true' :
  Ii11iII1 ( '[COLORgreen]STREAMS[/COLOR]' , iiI1IiI , 4002 , i1iIIi1 + 'streams.png' , oooOOOOO , '' )
 if iiIIIII1i1iI . getSetting ( 'Music' ) == 'true' :
  Ii11iII1 ( '[COLORgreen]Music[/COLOR]' , iiI1IiI , 4003 , i1iIIi1 + 'MUSIC.png' , oooOOOOO , '' )
  if 51 - 51: I1I1ii * oOO - oo0Oo - i11iIiiIii % o00OO0OOO0 % OOOooOooo00O0
 if iiIIIII1i1iI . getSetting ( 'Builders Toolbox' ) == 'true' :
  Ii11iII1 ( '[COLORgreen]BUILDERS TOOLBOX[/COLOR]' , iiI1IiI , 32 , i1iIIi1 + 'builderstoolbox.png' , oooOOOOO , '' )
 if iiIIIII1i1iI . getSetting ( 'Source List' ) == 'true' :
  Ii11iII1 ( '[COLORgreen]SOURCE LIST[/COLOR]' , iiI1IiI , 46 , i1iIIi1 + 'sources.png' , oooOOOOO , '' )
 if iiIIIII1i1iI . getSetting ( 'Maintainance' ) == 'true' :
  Ii11iII1 ( '[COLORgreen]MAINTENANCE[/COLOR]' , iiI1IiI , 3 , i1iIIi1 + 'MAIN6.png' , oooOOOOO , '' )
 if iiIIIII1i1iI . getSetting ( 'Addons' ) == 'true' :
  Ii11iII1 ( '[COLORgreen]ADDONS[/COLOR]' , '' , 10050 , i1iIIi1 + 'ADDONS.png' , oooOOOOO , '' )
 if iiIIIII1i1iI . getSetting ( 'APK Tool' ) == 'true' :
  Ii11iII1 ( '[COLORgreen]APK TOOL[/COLOR]' , iiI1IiI , 2 , i1iIIi1 + 'APK.png' , oooOOOOO , '' )
 if iiIIIII1i1iI . getSetting ( 'Rss Feed' ) == 'true' :
  Ii11iII1 ( '[COLORgreen]GenieTv RSS Feed[/COLOR]' , iiI1IiI , 39 , i1iIIi1 + 'RSS.png' , oooOOOOO , '' )
 if iiIIIII1i1iI . getSetting ( 'Addons Packs' ) == 'true' :
  Ii11iII1 ( '[COLORgreen]ADDONS PACKS[/COLOR]' , iiI1IiI , 30 , i1iIIi1 + 'ADDONP.png' , oooOOOOO , '' )
 I1IiII11III ( 'movies' , 'MAIN' )
 if 73 - 73: OoooooooOO - oo0Oo + OOOo0
def O00Oo000ooO0 ( ) :
 Ii11iII1 ( '[COLORgreen]BACKUP MY BUILD[/COLOR]' , iiI1IiI , 10060 , i1iIIi1 + 'MB.png' , oooOOOOO , '' )
 Ii11iII1 ( '[COLORgreen]RESTORE MY BUILD[/COLOR]' , iiI1IiI , 49 , i1iIIi1 + 'MB.png' , oooOOOOO , '' )
 Ii11iII1 ( '[COLORgreen]WIPE GENIE[/COLOR]' , iiI1IiI , 41 , i1iIIi1 + 'wipegenie.png' , oooOOOOO , '' )
 Ii11iII1 ( '[COLORgreen]WISHES PC[/COLOR]' , iiI1IiI , 1 , i1iIIi1 + 'WISHESPC.png' , oooOOOOO , '' )
 Ii11iII1 ( '[COLORgreen]WISHES ANDROID[/COLOR]' , iiI1IiI , 44 , i1iIIi1 + 'WISHESAN.png' , oooOOOOO , '' )
 I1IiII11III ( 'movies' , 'MAIN' )
def OoO0O00 ( ) :
 if oo0o0O00 == '5knuckleshuffle' :
  Ii11iII1 ( '[COLORgreen]XVID[/COLOR]' , iiI1IiI , 10100 , i1iIIi1 + 'JIZBOX.png' , oooOOOOO , '' )
 if iiIIIII1i1iI . getSetting ( 'TV GUIDE' ) == 'true' :
  IIiII ( '[COLORgreen]TV GUIDE[/COLOR]' , '' , 10063 , i1iIIi1 + 'GTVIPTV.png' , oooOOOOO , '' )
  if iiIIIII1i1iI . getSetting ( 'Favourites' ) == 'true' :
   Ii11iII1 ( '[COLORgreen]FAVOURITES[/COLOR]' , iiI1IiI , 10057 , i1iIIi1 + 'FAVORITES.png' , oooOOOOO , '' )
 if iiIIIII1i1iI . getSetting ( 'Search' ) == 'true' :
  Ii11iII1 ( '[COLORgreen]SEARCH[/COLOR]' , iiI1IiI , 9000 , i1iIIi1 + 'search.png' , oooOOOOO , '' )
 if iiIIIII1i1iI . getSetting ( 'G-tv' ) == 'true' :
  Ii11iII1 ( '[COLORgreen]G-Tv PRIVATE LIST[/COLOR]' , '' , 10058 , i1iIIi1 + 'GTVIPTV.png' , oooOOOOO , '' )
 Ii11iII1 ( '[COLORgreen]MOVIES[/COLOR]' , iiI1IiI , 4004 , i1iIIi1 + 'MOVIESv.png' , oooOOOOO , '' )
 Ii11iII1 ( '[COLORgreen]TV SHOWS[/COLOR]' , iiI1IiI , 4005 , i1iIIi1 + 'TVSHOWSv.png' , oooOOOOO , '' )
 Ii11iII1 ( '[COLORgreen]STREAM TEAM[/COLOR]' , iiI1IiI , 4006 , i1iIIi1 + 'streamteam.png' , oooOOOOO , '' )
 Ii11iII1 ( '[COLORgreen]KIDS[/COLOR]' , iiI1IiI , 4007 , i1iIIi1 + 'KIDSv.png' , oooOOOOO , '' )
 Ii11iII1 ( '[COLORgreen]HOBBIES[/COLOR]' , iiI1IiI , 4008 , i1iIIi1 + 'hobbies.png' , oooOOOOO , '' )
 if iiIIIII1i1iI . getSetting ( 'YOUTUBE' ) == 'true' :
  Ii11iII1 ( '[COLORgreen]SEARCH YOUTUBE[/COLOR]' , iiI1IiI , 10064 , i1iIIi1 + 'youtube.png' , oooOOOOO , '' )
 if iiIIIII1i1iI . getSetting ( 'REQUESTS' ) == 'true' :
  Ii11iII1 ( '[COLORgreen]REQUESTS[/COLOR]' , iiI1IiI + ( oOOoo00O0O ( 'L1JFUVVFU1RTLnBocA==' ) ) , 10066 , i1iIIi1 + 'requests.png' , oooOOOOO , '' )
 if iiIIIII1i1iI . getSetting ( 'Stand Up' ) == 'true' :
  Ii11iII1 ( '[COLORgreen]STAND UP[/COLOR]' , '' , 10003 , i1iIIi1 + 'ORIGINSTANDUP.png' , oooOOOOO , '' )
 if iiIIIII1i1iI . getSetting ( 'Documentaries' ) == 'true' :
  Ii11iII1 ( '[COLORgreen]DOCUMENTARIES[/COLOR]' , iiI1IiI , 8040 , i1iIIi1 + 'documentary.png' , oooOOOOO , '' )
 if iiIIIII1i1iI . getSetting ( 'Disclose' ) == 'true' :
  Ii11iII1 ( '[COLORgreen]DISCLOSE TV[/COLOR]' , iiI1IiI , 7001 , i1iIIi1 + 'disclose.png' , oooOOOOO , '' )
  if 80 - 80: I1I1ii . o00oOO0
  if 25 - 25: I1IiI . OoOoOO00 / OOOooOooo00O0 . iiiiiIIii * Ooo00oOo00o . OOOo0
 if iiIIIII1i1iI . getSetting ( 'Playlist Loader' ) == 'true' :
  Ii11iII1 ( '[COLORgreen]PLAYLIST LOADER[/COLOR]' , iiI1IiI , 3000 , i1iIIi1 + 'loader.png' , oooOOOOO , '' )
  if 59 - 59: OoOoOO00 + OoooooooOO * I1IiI + i1IIi
  if 58 - 58: OoOoOO00 * iiiiiIIii * ii11ii1ii / iiiiiIIii
  if 75 - 75: o00oOO0
  if 50 - 50: i1Iii / Oo - o00oOO0 - o00OO0OOO0 % OOOooOooo00O0 - o00oOO0
  if 91 - 91: Ooo00oOo00o / o00OO0OOO0 - OoOoOO00 . o00OO0OOO0
  if 18 - 18: OOooOOo
  if 98 - 98: OOOooOooo00O0 * OOOooOooo00O0 / OOOooOooo00O0 + o00OO0OOO0
  if 34 - 34: oo0Oo
  if 15 - 15: o00OO0OOO0 * oo0Oo * Oo % i11iIiiIii % I1IiI - iiiiiIIii
  if 68 - 68: oOO % i1IIi . I1I1ii . ii11ii1ii
  if 92 - 92: OOOooOooo00O0 . oOO
  if 31 - 31: oOO . I1IiI / O0
 I1IiII11III ( 'movies' , 'MAIN' )
 if 89 - 89: I1IiI
def OO0oOoOO0oOO0 ( ) :
 Ii11iII1 ( '[COLORgreen]SEARCH MOVIES[/COLOR]' , iiI1IiI , 9001 , i1iIIi1 + 'MOVIESv.png' , oooOOOOO , '' )
 Ii11iII1 ( '[COLORgreen]Genie Vision[/COLOR]' , '' , 10072 , i1iIIi1 + 'genievision.png' , oooOOOOO , '' )
 if iiIIIII1i1iI . getSetting ( 'Popcorn Box' ) == 'true' :
  Ii11iII1 ( '[COLORgreen]POPCORN BOX[/COLOR]' , iiI1IiI , 7061 , i1iIIi1 + 'popcorn.png' , oooOOOOO , '' )
 Ii11iII1 ( '[COLORgreen]Film Trailers[/COLOR]' , oOOoo00O0O ( 'aHR0cDovL3RoZW1vdmllYm94Lm5ldC9leHBsb3Jl' ) , 10068 , i1iIIi1 + 'movietrailers.png' , oooOOOOO , '' )
 if iiIIIII1i1iI . getSetting ( 'CLASSIC MOVIES' ) == 'true' :
  Ii11iII1 ( '[COLORgreen]CLASSIC MOVIES[/COLOR]' , '' , 8060 , i1iIIi1 + 'classicmovies.png' , oooOOOOO , '' )
 I1IiII11III ( 'movies' , 'MAIN' )
def oO0OOoo0OO ( ) :
 Ii11iII1 ( '[COLORgreen]SEARCH SERIES[/COLOR]' , iiI1IiI , 9002 , i1iIIi1 + 'TVSHOWSv.png' , oooOOOOO , '' )
 if iiIIIII1i1iI . getSetting ( 'Dizzy Tv' ) == 'true' :
  Ii11iII1 ( '[COLORgreen]DIZZY TV[/COLOR]' , '' , 10018 , i1iIIi1 + 'dtv.png' , oooOOOOO , '' )
 if iiIIIII1i1iI . getSetting ( 'Watch Series' ) == 'true' :
  Ii11iII1 ( '[COLORgreen]WATCH SERIES[/COLOR]' , '' , 10040 , i1iIIi1 + 'WATCHSERIES.png' , oooOOOOO , '' )
 Ii11iII1 ( '[COLORgreen]iWATCH SERIES[/COLOR]' , '' , 8020 , i1iIIi1 + 'iwatch.png' , oooOOOOO , '' )
 if iiIIIII1i1iI . getSetting ( 'Recent Episodes' ) == 'true' :
  Ii11iII1 ( '[COLORgreen]RECENT EPISODES[/COLOR]' , iiI1IiI , 8081 , i1iIIi1 + 'recent.png' , oooOOOOO , '' )
 if iiIIIII1i1iI . getSetting ( 'CLASSIC TV' ) == 'true' :
  Ii11iII1 ( '[COLORgreen]CLASSIC TV[/COLOR]' , iiI1IiI , 8064 , i1iIIi1 + 'classictv.png' , oooOOOOO , '' )
 Ii11iII1 ( '[COLORgreen]TV Show Trailers[/COLOR]' , oOOoo00O0O ( 'aHR0cHM6Ly93d3cueW91dHViZS5jb20vd2F0Y2g/dj03WkZJUzJBcUF6OCZsaXN0PVBMM2t4NWgyVHJZR3dwVzBWYk5lbnBqLUJLTUJUR2dKUEU=' ) , 10069 , i1iIIi1 + 'tvtrailers.png' , oooOOOOO , '' )
 Ii11iII1 ( '[COLORgreen]TV Show Schedule[/COLOR]' , oOOoo00O0O ( 'aHR0cDovL3d3dy5wb2dkZXNpZ24uY28udWsvY2F0Lw==' ) , 10070 , i1iIIi1 + 'tvschedule.png' , oooOOOOO , '' )
 I1IiII11III ( 'movies' , 'MAIN' )
def O0ii1ii1ii ( ) :
 if iiIIIII1i1iI . getSetting ( 'Scooby Streams' ) == 'true' :
  Ii11iII1 ( '[COLORgreen]SCOOBY STREAMS[/COLOR]' , iiI1IiI , 1023 , i1iIIi1 + 'scoob.png' , oooOOOOO , '' )
 if iiIIIII1i1iI . getSetting ( 'The Reaper' ) == 'true' :
  Ii11iII1 ( '[COLORgreen]THE REAPER[/COLOR]' , ( oOOoo00O0O ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9UaGVfUmVhcGVyL21haW4ucGhw' ) ) , 1016 , i1iIIi1 + 'reap.png' , oooOOOOO , '' )
 if iiIIIII1i1iI . getSetting ( 'Pandoras Box' ) == 'true' :
  Ii11iII1 ( '[COLORgreen]PANDORAS BOX[/COLOR]' , iiI1IiI , 10025 , i1iIIi1 + 'PANDORASBOX.png' , oooOOOOO , '' )
 if iiIIIII1i1iI . getSetting ( 'HeroVision' ) == 'true' :
  Ii11iII1 ( '[COLORgreen]HEROVISION[/COLOR]' , ( oOOoo00O0O ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC9tYWluLnBocA==' ) ) , 1016 , i1iIIi1 + 'hero.png' , oooOOOOO , '' )
 if iiIIIII1i1iI . getSetting ( 'Silent Hunter' ) == 'true' :
  Ii11iII1 ( '[COLORgreen]SILENT HUNTER[/COLOR]' , ( oOOoo00O0O ( 'aHR0cDovLzUuMTM1LjIwNy45Ni8=' ) ) , 1006 , i1iIIi1 + 'SILENTHUNTER.png' , oooOOOOO , '' )
 if iiIIIII1i1iI . getSetting ( 'Redemption Streams' ) == 'true' :
  Ii11iII1 ( '[COLORgreen]Redemption Streams[/COLOR]' , ( oOOoo00O0O ( 'aHR0cDovL3JlZGVtcHRpb25idWlsZC4xNm1iLmNvbS9SZWRlbXB0aW9uL21haW4ucGhw' ) ) , 1016 , i1iIIi1 + 'redemption.png' , oooOOOOO , '' )
 I1IiII11III ( 'movies' , 'MAIN' )
def oooooOoo0ooo ( ) :
 Ii11iII1 ( '[COLORgreen]SEARCH CARTOONS[/COLOR]' , '' , 10005 , i1iIIi1 + 'ORIGINCARTOON' , oooOOOOO , '' )
 if iiIIIII1i1iI . getSetting ( 'WCO' ) == 'true' :
  Ii11iII1 ( '[COLORgreen]WATCH CARTOONS ONLINE[/COLOR]' , iiI1IiI , 21004 , i1iIIi1 + 'watchcartoons.png' , oooOOOOO , '' )
 if iiIIIII1i1iI . getSetting ( 'Cartoons' ) == 'true' :
  Ii11iII1 ( '[COLORgreen]CARTOONS[/COLOR]' , '' , 10001 , i1iIIi1 + 'ORIGINCARTOON.png' , oooOOOOO , '' )
 if iiIIIII1i1iI . getSetting ( 'Anime' ) == 'true' :
  Ii11iII1 ( '[COLORgreen]AnimeLand[/COLOR]' , ( oOOoo00O0O ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2R1YmJlZC1hbmltZQ==' ) ) , 10004 , i1iIIi1 + 'anime.png' , oooOOOOO , '' )
 I1IiII11III ( 'movies' , 'MAIN' )
def I1I1IiI1 ( ) :
 if iiIIIII1i1iI . getSetting ( 'Football' ) == 'true' :
  Ii11iII1 ( '[COLORgreen]FOOTBALL[/COLOR]' , '' , 10002 , i1iIIi1 + 'ORIGINFOOTBALL.png' , oooOOOOO , '' )
 if iiIIIII1i1iI . getSetting ( 'Fitness' ) == 'true' :
  Ii11iII1 ( '[COLORgreen]FITNESS[/COLOR]' , ( oOOoo00O0O ( 'aHR0cHM6Ly93d3cuZml0bmVzc2JsZW5kZXIuY29tL3ZpZGVvcw==' ) ) , 7085 , i1iIIi1 + 'FITNESS.png' , oooOOOOO , '' )
 if iiIIIII1i1iI . getSetting ( 'Go Fishing' ) == 'true' :
  Ii11iII1 ( '[COLORgreen]Go Fishing[/COLOR]' , iiI1IiI , 8090 , i1iIIi1 + 'gofish.png' , oooOOOOO , '' )
 if iiIIIII1i1iI . getSetting ( 'GenieTv Kitchen' ) == 'true' :
  Ii11iII1 ( '[COLORgreen]GenieTv Kitchen[/COLOR]' , ( oOOoo00O0O ( 'aHR0cDovL2Zvb2QubmR0di5jb20vdmlkZW9z' ) ) , 8045 , i1iIIi1 + 'geniekitchen.png' , oooOOOOO , '' )
 I1IiII11III ( 'movies' , 'MAIN' )
 if 5 - 5: OOooOOo * oo0Oo + I1IiI . iiiiiIIii + I1IiI
 if 91 - 91: O0
 if 61 - 61: OoOoOO00
 if 64 - 64: oo0Oo / I1IiI - O0 - o00OO0OOO0
def iIi11Ii1 ( ) :
 O0oOoOOOoOO = ii1ii11IIIiiI ( 'http://architects.x10host.com/wizarddelete.txt' )
 O00OOOoOoo0O = re . compile ( '<unwanted_wizard =(.+?)</unwanted_wizard>' ) . findall ( O0oOoOOOoOO )
 for O000OOo00oo in O00OOOoOoo0O :
  print O000OOo00oo
  O000OOo00oo = ( str ( O000OOo00oo ) )
  if os . path . exists ( xbmc . translatePath ( O000OOo00oo ) ) :
   oo0OOo = os . path . join ( iIi1ii1I1 , 'guisettings.xml' )
   ooOOO00Ooo = open ( oo0OOo , "w+" )
   if 16 - 16: OoOoOO00 % I1IiI - OoOoOO00 + i1Iii
   ooOOO00Ooo . write ( r'.' )
   i1I1i ( )
  else :
   pass
   if 40 - 40: OOOo0 . iIii1I11I1II1 / OOOo0 / i11iIiiIii
def iI1iI1I1i1I ( ) :
 O0oOoOOOoOO = ii1ii11IIIiiI ( 'http://architects.x10host.com/testdelete.txt' )
 O00OOOoOoo0O = re . compile ( '<unwanted_addon =(.+?)</unwanted_addon>' ) . findall ( O0oOoOOOoOO )
 for oOOoOo00o in O00OOOoOoo0O :
  oOOoOo00o = ( str ( oOOoOo00o ) )
  if os . path . exists ( xbmc . translatePath ( oOOoOo00o ) ) :
   o0OOoo0OO0OOO ( oOOoOo00o )
   o0O00o ( )
  else :
   pass
   if 87 - 87: i11iIiiIii
def o0OOoo0OO0OOO ( addon ) :
 i1 . ok ( "[COLOR=white]Incompatible[/COLOR]" , "Unfortunately GenieTv will not work with" , addon , 'please remove then reinstall genie' )
 oo0OOo = os . path . join ( II , 'default.py' )
 ooOOO00Ooo = open ( oo0OOo , "w+" )
 if 93 - 93: ii11ii1ii - Ooo00oOo00o % i11iIiiIii . OOOooOooo00O0 / OOOooOooo00O0 - oOO
 ooOOO00Ooo . write ( r'Genie Tv will not work with certain addons in an attempt to bring you original content from the best developers' )
 ooOOO00Ooo . write ( r'and not those simply out to profit or make a name for themselves off others work' )
 ooOOO00Ooo . write ( r'Please remove' + unwanted_addons + 'if you would like to use genie tv then uninstall and reinstall from official repo' )
 if 9 - 9: ii11ii1ii / Oo - OOOo0 / OoooooooOO / iIii1I11I1II1 - OOooOOo
 if 91 - 91: OOOooOooo00O0 % i1IIi % iIii1I11I1II1
def i1I1i ( ) :
 O0oOoOOOoOO = ii1ii11IIIiiI ( oOOoo00O0O ( 'aHR0cDovL3d3dy5wb2dkZXNpZ24uY28udWsvY2F0Lw==' ) )
 IIi1I11I1II = re . compile ( '<tr>.+?title="(.+?)">(.+?)</tr>' , re . DOTALL ) . findall ( O0oOoOOOoOO )
 for OooOoooOo , IIi1I11I1II in IIi1I11I1II :
  OooOoooOo = OooOoooOo
  O00OOOoOoo0O = re . compile ( '<p><a href=".+?" rel=".+?">(.+?)\n</a>.+?<br /><a href=".+?">(.+?)</a>.+?</p>' , re . DOTALL ) . findall ( str ( IIi1I11I1II ) )
  for ii11IIII11I , OOooo in O00OOOoOoo0O :
   oOooOOOoOo ( OooOoooOo , ii11IIII11I , OOooo )
   if 41 - 41: i1Iii - O0 - O0
   if 68 - 68: iiiiiIIii % oOO
   if 88 - 88: iIii1I11I1II1 - oo0Oo + iiiiiIIii
   if 40 - 40: OOOo0 * i1Iii + iiiiiIIii % OOOooOooo00O0
   if 74 - 74: o00oOO0 - Oo + OoooooooOO + oOO / I1IiI
   if 23 - 23: O0
   if 85 - 85: i1Iii
   if 84 - 84: OOOo0 . iIii1I11I1II1 % OoooooooOO + i1Iii % OoooooooOO % Ooo00oOo00o
   if 42 - 42: Ooo00oOo00o / o00OO0OOO0 / OOooOOo + OOOooOooo00O0 / I1IiI
   if 84 - 84: oo0Oo * OoOoOO00 + Oo
   if 53 - 53: OOOooOooo00O0 % OoOoOO00 . I1I1ii - iIii1I11I1II1 - I1I1ii * OoOoOO00
   if 77 - 77: iIii1I11I1II1 * Ooo00oOo00o
   if 95 - 95: OOOo0 + i11iIiiIii
   if 6 - 6: oo0Oo / i11iIiiIii + OOOooOooo00O0 * o00oOO0
   if 80 - 80: OoOoOO00
   if 83 - 83: o00OO0OOO0 . i11iIiiIii + OoOoOO00 . OOooOOo * o00OO0OOO0
   if 53 - 53: OoOoOO00
def i1Ii1Ii ( ) :
 Ii11iII1 ( 'Genre' , oOOoo00O0O ( 'aHR0cDovL2ltb3ZpZW1heC5zZS9tb3ZpZXMv' ) , 10073 , i1iIIi1 + 'genievision.png' , oooOOOOO , '' )
 Ii11iII1 ( 'Most Viewed' , oOOoo00O0O ( 'aHR0cDovL2ltb3ZpZW1heC5zZS9tb3ZpZXMv' ) , 10077 , i1iIIi1 + 'genievision.png' , oooOOOOO , '' )
 Ii11iII1 ( 'Box Office' , oOOoo00O0O ( 'aHR0cDovL2ltb3ZpZW1heC5zZS9jYXRlZ29yeS9ib3gtb2ZmaWNlLw==' ) , 10074 , i1iIIi1 + 'genievision.png' , oooOOOOO , '' )
 Ii11iII1 ( 'Search' , '' , 10078 , i1iIIi1 + 'genievision.png' , oooOOOOO , '' )
 if 52 - 52: Ooo00oOo00o . o00oOO0
def ii1iII1II ( ) :
 Iii1I1I11iiI1 = i1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 I1I1i1I = 'http://imoviemax.se/?s=' + ( Iii1I1I11iiI1 ) . replace ( ' ' , '+' )
 ii1I = I1I1i1I . lower ( )
 O0oO0 ( ii1I )
def oO0 ( url ) :
 O0OO0O = [ ]
 O0oOoOOOoOO = ii1ii11IIIiiI ( url )
 O00OOOoOoo0O = re . compile ( '<li class="cat-item cat-item-.+? "><a href="(.+?)">(.+?)</a><i>(.+?)</i></li>' ) . findall ( O0oOoOOOoOO )
 for url , ii11IIII11I , OO in O00OOOoOoo0O :
  if ii11IIII11I in O0OO0O :
   pass
  else :
   Ii11iII1 ( ii11IIII11I + ' - ' + OO + ' Films' , url , 10074 , i1iIIi1 + 'genievision.png' , oooOOOOO , '' )
   O0OO0O . append ( ii11IIII11I )
   if 83 - 83: O0 / OOOo0 - Ooo00oOo00o - iiiiiIIii
def iI1i11iII111 ( url ) :
 O0oOoOOOoOO = ii1ii11IIIiiI ( url )
 O00OOOoOoo0O = re . compile ( '<li>.+?<b>.+?</b>.+?<a href="(.+?)">(.+?)</a>.+?<span>(.+?)</span>' , re . DOTALL ) . findall ( O0oOoOOOoOO )
 for url , ii11IIII11I , Iii1IIII11I in O00OOOoOoo0O :
  Ii11iII1 ( ii11IIII11I + ' - Views:' + Iii1IIII11I , url , 10075 , i1iIIi1 + 'genievision.png' , oooOOOOO , '' )
  if 77 - 77: Oo - i1IIi - o00OO0OOO0 . I1IiI
  if 39 - 39: OoOoOO00 / oo0Oo + oOO / I1IiI
def O0oO0 ( url ) :
 I1Ii11i = [ ]
 O0oOoOOOoOO = ii1ii11IIIiiI ( url )
 next = re . compile ( "<link rel='next' href='(.+?)' />" ) . findall ( O0oOoOOOoOO )
 for next in next :
  Ii11iII1 ( 'NEXT PAGE' , next , 10074 , i1iIIi1 + 'Next.png' , oooOOOOO , '' )
 O00OOOoOoo0O = re . compile ( '<div class="movie">.+?<img src="(.+?)" alt="(.+?)" />.+?<a href="(.+?)"><span class="player"></span></a>' , re . DOTALL ) . findall ( O0oOoOOOoOO )
 for i1111I1I , ii11IIII11I , url in O00OOOoOoo0O :
  Ii11iII1 ( ii11IIII11I , url , 10075 , i1111I1I , i1111I1I , '' )
  I1Ii11i . append ( ii11IIII11I )
  if 13 - 13: i1Iii . i11iIiiIii
def oOOoo00O00o ( img , name , url ) :
 img = img
 name = name
 O0oOoOOOoOO = ii1ii11IIIiiI ( url )
 O00OOOoOoo0O = re . compile ( '<div id="(.+?)" class="player-content"><iframe class="playerframe" src="(.+?)" scrolling="no".+?</iframe></div>' ) . findall ( O0oOoOOOoOO )
 for O0O00Oo , url in O00OOOoOoo0O :
  print '>>>>>>>>>>>>>>>>>>>>>>>>>>> before' + url
  oooooo0O000o = ( url ) . replace ( 'player' , 'watch' ) + '&fv=&sou='
  print '<<<<<<<<<<<<<<<<<<<<<<<<<<< after' + oooooo0O000o
  OoO = ( O0O00Oo ) . replace ( 'play-' , 'Server ' )
  IIiII ( OoO , oooooo0O000o , 10076 , img , img , '' )
  if 51 - 51: OoooooooOO * iiiiiIIii
def OO0ooOOO0OOO ( url ) :
 O0oOoOOOoOO = ii1ii11IIIiiI ( url )
 O00OOOoOoo0O = re . compile ( '<source src="(.+?)" type="video/mp4">' ) . findall ( O0oOoOOOoOO )
 for oO00oooOOoOo0 in O00OOOoOoo0O :
  if '=m' in oO00oooOOoOo0 :
   OoOOoOooooOOo ( oO00oooOOoOo0 )
  elif 'php' in oO00oooOOoOo0 :
   OO0ooOOO0OOO ( url )
  else :
   O0oOoOOOoOO = ii1ii11IIIiiI ( oO00oooOOoOo0 )
   O00OOOoOoo0O = re . compile ( 'content="(.+?)">' ) . findall ( O0oOoOOOoOO )
   for oOo0O in O00OOOoOoo0O :
    OoOOoOooooOOo ( oO00oooOOoOo0 )
    if 52 - 52: i11iIiiIii / OOooOOo * oo0Oo
    if 22 - 22: I1IiI . iiiiiIIii * I1IiI
    if 54 - 54: I1I1ii + i1Iii % Ooo00oOo00o + OoooooooOO - O0 - OOooOOo
def o0o0O0O00oOOo ( url ) :
 O0oOoOOOoOO = ii1ii11IIIiiI ( url )
 iIIIiIi = re . compile ( '<td id=".+?" class="today">.+?title="(.+?)">(.+?)</td>' , re . DOTALL ) . findall ( O0oOoOOOoOO )
 for OooOoooOo , OO0O0 in iIIIiIi :
  print 'there ><><><><><><><><><><><><'
  OooOoooOo = OooOoooOo
  O00OOOoOoo0O = re . compile ( '<p><a href=".+?" rel=".+?">(.+?)</a>.+?<br /><a href=".+?">(.+?)</a>.+?</p>' , re . DOTALL ) . findall ( str ( OO0O0 ) )
  for ii11IIII11I , OOooo in O00OOOoOoo0O :
   print 'here <><><><><><><><><><><><>'
   Ii11iII1 ( '[COLORred]' + OooOoooOo + '[/COLOR] - ' + ii11IIII11I + ' - [COLORgreen]' + OOooo + '[/COLOR]' , oOOoo00O0O ( 'aHR0cDovL3d3dy5wb2dkZXNpZ24uY28udWsvY2F0Lw==' ) , 10070 , i1iIIi1 + 'loader.png' , oooOOOOO , '' )
 IIi1I11I1II = re . compile ( '<td id=".+?" class="day">.+?title="(.+?)">(.+?)</td>' , re . DOTALL ) . findall ( O0oOoOOOoOO )
 for OooOoooOo , I11I11 in IIi1I11I1II :
  print 'there ><><><><><><><><><><><><'
  OooOoooOo = OooOoooOo
  O00OOOoOoo0O = re . compile ( '<p><a href=".+?" rel=".+?">(.+?)</a>.+?<br /><a href=".+?">(.+?)</a>.+?</p>' , re . DOTALL ) . findall ( str ( I11I11 ) )
  for ii11IIII11I , OOooo in O00OOOoOoo0O :
   print 'here <><><><><><><><><><><><>'
   Ii11iII1 ( '[COLORred]' + OooOoooOo + '[/COLOR] - ' + ii11IIII11I + ' - [COLORgreen]' + OOooo + '[/COLOR]' , oOOoo00O0O ( 'aHR0cDovL3d3dy5wb2dkZXNpZ24uY28udWsvY2F0Lw==' ) , 10070 , i1iIIi1 + 'loader.png' , oooOOOOO , '' )
   if 69 - 69: I1IiI
   if 97 - 97: ii11ii1ii % ii11ii1ii % o00oOO0 / OOOooOooo00O0 - iIii1I11I1II1
   if 69 - 69: oOO
def ii1I1 ( url ) :
 O0oOoOOOoOO = ii1ii11IIIiiI ( url )
 IIi1I11I1II = re . compile ( '<li class="yt-uix-scroller-scroll-unit "(.+?)</li>' , re . DOTALL ) . findall ( O0oOoOOOoOO )
 for IIi1I11I1II in IIi1I11I1II :
  ii11IIII11I = re . compile ( 'data-video-title="(.+?)"' ) . findall ( str ( IIi1I11I1II ) )
  for ii11IIII11I in ii11IIII11I :
   ii11IIII11I = ( ii11IIII11I ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&amp;' , '&' )
  url = re . compile ( '<a href="/w(.+?)&' ) . findall ( str ( IIi1I11I1II ) )
  for url in url :
   url = 'https://www.youtube.com/w' + url
  OooooOOoo0 = re . compile ( '<img.+?="(.+?)"' ) . findall ( str ( IIi1I11I1II ) )
  for OooooOOoo0 in OooooOOoo0 :
   OooooOOoo0 = 'http:' + OooooOOoo0
  IIiII ( '[COLORgreen]' + ii11IIII11I + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , OooooOOoo0 , '' , '' )
  if 35 - 35: o00OO0OOO0 % iiiiiIIii - o00oOO0
  if 20 - 20: i1IIi - oo0Oo
  if 30 - 30: o00OO0OOO0 / OOOo0
  if 35 - 35: OoOoOO00 % iiiiiIIii . oo0Oo + oo0Oo % OoOoOO00 % OoOoOO00
def ooOoO00 ( url ) :
 if 14 - 14: i1IIi - OOooOOo % O0 - Ooo00oOo00o
 ooO0O00Oo0o = [ ]
 O0oOoOOOoOO = ii1ii11IIIiiI ( url )
 O00OOOoOoo0O = re . compile ( '<div class="explore-list">.+?<div class="el-img"><a href="(.+?)" class=".+?"><img src="(.+?)" alt=".+?<h3>(.+?)</h3><p>(.+?)</p></div>' , re . DOTALL ) . findall ( O0oOoOOOoOO )
 for oO00oooOOoOo0 , i1111I1I , ii11IIII11I , OOO in O00OOOoOoo0O :
  ii11IIII11I = ( ii11IIII11I ) . replace ( '&#039;' , '\'' ) . replace ( '&amp;' , '&' ) . replace ( '&quot;' , '"' )
  Oo0o00OO0000 = ii1ii11IIIiiI ( oO00oooOOoOo0 )
  I1i = re . compile ( '<!-- # player # -->.+?<iframe title=".+?".+?src="http://www.youtube.com/embed/(.+?)?autohide.+?<!-- detail box -->(.+?)</div>' , re . DOTALL ) . findall ( Oo0o00OO0000 )
  for O00Oooo , i11I in I1i :
   o00Oo0oooooo = re . compile ( '<p>(.+?)</p>' , re . DOTALL ) . findall ( str ( i11I ) )
   for O0oO0iII11 in o00Oo0oooooo :
    if ii11IIII11I in ooO0O00Oo0o :
     pass
    else :
     IIiII ( ii11IIII11I , O00Oooo , 8043 , i1111I1I , i1111I1I , O0oO0iII11 )
     I1IiII11III ( 'movies' , 'INFO' )
     ooO0O00Oo0o . append ( ii11IIII11I )
     if 32 - 32: oOO
     if 30 - 30: iIii1I11I1II1 / o00OO0OOO0 . Ooo00oOo00o - OOooOOo
def Iii11iI1i ( url ) :
 oOOooOoo = o0OOOoO0 ( url )
 O00OOOoOoo0O = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( oOOooOoo )
 for url , o0OoOo00o0o , O0oO0iII11 , I1II1I11I1I , ii11IIII11I in O00OOOoOoo0O :
  Ii11iII1 ( ii11IIII11I , url , 10065 , o0OoOo00o0o , I1II1I11I1I , O0oO0iII11 )
 I1IiII11III ( 'movies' , 'INFO' )
 if 54 - 54: OoooooooOO + OOooOOo - i1IIi % i11iIiiIii
def iII1iIi11i ( ) :
 Iii1I1I11iiI1 = i1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 I1I1i1I = 'https://www.youtube.com/results?search_query=' + ( Iii1I1I11iiI1 ) . replace ( ' ' , '+' )
 ii1I = I1I1i1I . lower ( )
 O0oOoOOOoOO = ii1ii11IIIiiI ( ii1I )
 O00OOOoOoo0O = re . compile ( '<img src="(.+?)" alt=.+?yt-lockup-title "><a href="(.+?)".+?data-sessionlink=.+?" title="(.+?)".+?<span class="accessible-description".+?>(.+?)</span>.+?<div class="yt-lockup-description yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr">(.+?)</div>' , re . DOTALL ) . findall ( O0oOoOOOoOO )
 next = re . compile ( '<a href="(.+?)" class="yt-uix-button.+?class="yt-uix-button-content">Next.+?</span></a>' ) . findall ( O0oOoOOOoOO )
 for o0ooooO0o0O in next :
  o0ooooO0o0O = 'https://www.youtube.com' + o0ooooO0o0O
  Ii11iII1 ( '[COLORgreen] NEXT [/COLOR]' , o0ooooO0o0O , 10065 , i1iIIi1 + 'Next.png' , oooOOOOO , '' )
 for i1111I1I , o0ooooO0o0O , ii11IIII11I , iiIi11iI1iii , i11I in O00OOOoOoo0O :
  OO0o . append ( ii11IIII11I )
  I1IiII11III ( 'tvshows' , 'INFO' )
  OooooOOoo0 = 'http:' + ( i1111I1I ) . replace ( 'https:' , '' )
  print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>' + OooooOOoo0
  o0ooooO0o0O = 'http://www.youtube.com' + o0ooooO0o0O
  IIiII ( '[COLORred]' + iiIi11iI1iii + '[/COLOR]' + '[COLORgreen]' + ii11IIII11I + '[/COLOR]' , ( o0ooooO0o0O ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , OooooOOoo0 , OooooOOoo0 , i11I )
 else :
  O00OOOoOoo0O = re . compile ( '<img src="(.+?)" alt=.+?yt-lockup-title "><a href="(.+?)".+?data-sessionlink=.+?" title="(.+?)".+?<span class="accessible-description".+?>(.+?)</span>' , re . DOTALL ) . findall ( O0oOoOOOoOO )
  for i1111I1I , o0ooooO0o0O , ii11IIII11I , iiIi11iI1iii in O00OOOoOoo0O :
   print 'im doing it'
   I1IiII11III ( 'tvshows' , 'INFO' )
   OooooOOoo0 = 'http:' + ( i1111I1I ) . replace ( 'https:' , '' )
   o0ooooO0o0O = 'http://www.youtube.com' + o0ooooO0o0O
   if '&' in o0ooooO0o0O :
    print ' i got here'
    O0oOoOOOoOO = ii1ii11IIIiiI ( o0ooooO0o0O )
    IIi1I11I1II = re . compile ( '<li class="yt-uix-scroller-scroll-unit "(.+?)</li>' , re . DOTALL ) . findall ( O0oOoOOOoOO )
    for IIi1I11I1II in IIi1I11I1II :
     ii11IIII11I = re . compile ( 'data-video-title="(.+?)"' ) . findall ( str ( IIi1I11I1II ) )
     for ii11IIII11I in ii11IIII11I :
      ii11IIII11I = ( ii11IIII11I ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&amp;' , '&' )
     o0ooooO0o0O = re . compile ( '<a href="/w(.+?)&' ) . findall ( str ( IIi1I11I1II ) )
     for o0ooooO0o0O in o0ooooO0o0O :
      o0ooooO0o0O = 'https://www.youtube.com/w' + o0ooooO0o0O
     OooooOOoo0 = re . compile ( '<img.+?="(.+?)"' ) . findall ( str ( IIi1I11I1II ) )
     for OooooOOoo0 in OooooOOoo0 :
      OooooOOoo0 = 'http:' + OooooOOoo0
     IIiII ( '[COLORred]' + iiIi11iI1iii + '[/COLOR]' + '[COLORgreen]' + ii11IIII11I + '[/COLOR]' , ( o0ooooO0o0O ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , OooooOOoo0 , oooOOOOO , '' )
   elif ii11IIII11I in OO0o :
    pass
   elif 'user' in o0ooooO0o0O or 'elete' in ii11IIII11I :
    pass
   elif 'hannel' in o0ooooO0o0O :
    print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' + o0ooooO0o0O
    O0oOoOOOoOO = ii1ii11IIIiiI ( o0ooooO0o0O )
    oo000 = re . compile ( 'data-thumb="(.+?)".+?href="(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( O0oOoOOOoOO )
    for i1111I1I , o0ooooO0o0O , ii11IIII11I in oo000 :
     if 'outube' in o0ooooO0o0O or 'list' in o0ooooO0o0O :
      pass
     elif 'atch' in o0ooooO0o0O :
      o0ooooO0o0O = ( o0ooooO0o0O ) . replace ( '/watch?v=' , '' )
      IIiII ( '[COLORred]' + iiIi11iI1iii + '[/COLOR]' + '[COLORgreen]' + ii11IIII11I + '[/COLOR]' , ( o0ooooO0o0O ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , 'http:' + i1111I1I , 'http:' + i1111I1I , '' )
     else :
      pass
   else :
    IIiII ( '[COLORred]' + iiIi11iI1iii + '[/COLOR]' + '[COLORgreen]' + ii11IIII11I + '[/COLOR]' , ( o0ooooO0o0O ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , OooooOOoo0 , OooooOOoo0 , '' )
    if 63 - 63: oo0Oo + iiiiiIIii * i1Iii
def iI1 ( url ) :
 O0oOoOOOoOO = ii1ii11IIIiiI ( url )
 O00OOOoOoo0O = re . compile ( '<img src="(.+?)" alt=.+?yt-lockup-title "><a href="(.+?)".+?data-sessionlink=.+?" title="(.+?)".+?<span class="accessible-description".+?>(.+?)</span>.+?<div class="yt-lockup-description yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr">(.+?)</div>' , re . DOTALL ) . findall ( O0oOoOOOoOO )
 next = re . compile ( '<a href="(.+?)" class="yt-uix-button.+?class="yt-uix-button-content">Next.+?</span></a>' ) . findall ( O0oOoOOOoOO )
 for url in next :
  url = 'https://www.youtube.com' + url
  Ii11iII1 ( '[COLORgreen] NEXT [/COLOR]' , url , 10065 , i1iIIi1 + 'Next.png' , oooOOOOO , '' )
 for i1111I1I , url , ii11IIII11I , iiIi11iI1iii , i11I in O00OOOoOoo0O :
  OO0o . append ( ii11IIII11I )
  I1IiII11III ( 'tvshows' , 'INFO' )
  OooooOOoo0 = 'http:' + ( i1111I1I ) . replace ( 'https:' , '' )
  print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>' + OooooOOoo0
  url = 'http://www.youtube.com' + url
  IIiII ( '[COLORred]' + iiIi11iI1iii + '[/COLOR]' + '[COLORgreen]' + ii11IIII11I + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , OooooOOoo0 , OooooOOoo0 , i11I )
 else :
  O00OOOoOoo0O = re . compile ( '<img src="(.+?)" alt=.+?yt-lockup-title "><a href="(.+?)".+?data-sessionlink=.+?" title="(.+?)".+?<span class="accessible-description".+?>(.+?)</span>' , re . DOTALL ) . findall ( O0oOoOOOoOO )
  for i1111I1I , url , ii11IIII11I , iiIi11iI1iii in O00OOOoOoo0O :
   I1IiII11III ( 'tvshows' , 'INFO' )
   OooooOOoo0 = 'http:' + ( i1111I1I ) . replace ( 'https:' , '' )
   url = 'http://www.youtube.com' + url
   if '&' in url :
    O0oOoOOOoOO = ii1ii11IIIiiI ( url )
    IIi1I11I1II = re . compile ( '<li class="yt-uix-scroller-scroll-unit "(.+?)</li>' , re . DOTALL ) . findall ( O0oOoOOOoOO )
    for IIi1I11I1II in IIi1I11I1II :
     ii11IIII11I = re . compile ( 'data-video-title="(.+?)"' ) . findall ( str ( IIi1I11I1II ) )
     for ii11IIII11I in ii11IIII11I :
      ii11IIII11I = ( ii11IIII11I ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&amp;' , '&' )
     url = re . compile ( '<a href="/w(.+?)&' ) . findall ( str ( IIi1I11I1II ) )
     for url in url :
      url = 'https://www.youtube.com/w' + url
     OooooOOoo0 = re . compile ( '<img.+?="(.+?)"' ) . findall ( str ( IIi1I11I1II ) )
     for OooooOOoo0 in OooooOOoo0 :
      OooooOOoo0 = 'http:' + OooooOOoo0
     IIiII ( '[COLORred]' + iiIi11iI1iii + '[/COLOR]' + '[COLORgreen]' + ii11IIII11I + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , OooooOOoo0 , oooOOOOO , '' )
   elif ii11IIII11I in OO0o :
    pass
   elif 'user' in url or 'elete' in ii11IIII11I :
    pass
   elif 'hannel' in url :
    print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' + url
    O0oOoOOOoOO = ii1ii11IIIiiI ( url )
    oo000 = re . compile ( 'data-thumb="(.+?)".+?href="(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( O0oOoOOOoOO )
    for i1111I1I , url , ii11IIII11I in oo000 :
     if 'outube' in url or 'list' in url :
      pass
     elif 'atch' in url :
      url = ( url ) . replace ( '/watch?v=' , '' )
      IIiII ( '[COLORred]' + iiIi11iI1iii + '[/COLOR]' + '[COLORgreen]' + ii11IIII11I + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , 'http:' + i1111I1I , 'http:' + i1111I1I , '' )
     else :
      pass
   else :
    IIiII ( '[COLORred]' + iiIi11iI1iii + '[/COLOR]' + '[COLORgreen]' + ii11IIII11I + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , OooooOOoo0 , OooooOOoo0 , '' )
    if 48 - 48: o00OO0OOO0 / oOO % oo0Oo - iIii1I11I1II1 - i1IIi / o00oOO0
    if 93 - 93: o00OO0OOO0 . OoOoOO00 / o00oOO0 % OoooooooOO * o00OO0OOO0 % ii11ii1ii
def I1i11 ( ) :
 if oO0o0o0ooO0oO == 'insert_password' :
  i1 . ok ( '[COLORgreen]Donators Login[/COLOR]' , 'You need to set username and password to access this' , 'These are unique and provided to donators to help with server and stream costs' , 'Donate @ [COLORgreen]http://architects.x10host.com[/COLOR]' )
  iiIIIII1i1iI . openSettings ( sys . argv [ 0 ] )
 else :
  Ii11iII1 ( '[COLORgreen]DONATORS LIST[/COLOR]' , iiI1IiI + '/thelist.m3u' , 7080 , i1iIIi1 + 'GTVIPTV.png' , oooOOOOO , '' )
  if 12 - 12: i1IIi + i1IIi - ii11ii1ii * Oo % Oo - OoOoOO00
def o0O ( ) :
 try :
  OOOooo = gui . TVGuide ( )
  OOOooo . doModal ( )
  del OOOooo
  if 94 - 94: OoooooooOO + Oo / I1IiI * iiiiiIIii
 except :
  import sys
  import traceback as tb
  ( o0OOo0o0O0O , o0OO0o0oOOO0O , traceback ) = sys . exc_info ( )
  tb . print_exception ( o0OOo0o0O0O , o0OO0o0oOOO0O , traceback )
  if 49 - 49: ii11ii1ii . OOooOOo . OoOoOO00
def o000ooooO0o ( ) :
 Ii11iII1 ( 'Full Backup' , '' , 10061 , i1iIIi1 + 'Backup.png' , oooOOOOO , 'Back Up Your Full System' )
 if os . path . exists ( IIiiiiiiIi1I1 ) :
  Ii11iII1 ( 'Backup Genie Favourites' , o0ooooO0o0O , 10062 , i1iIIi1 + 'Backup.png' , oooOOOOO , 'Back Up Your favourites' )
 if os . path . exists ( IIIII ) :
  Ii11iII1 ( 'Backup Ivue Config' , IIIII , 10062 , i1iIIi1 + 'Backup.png' , oooOOOOO , 'Back Up Your master.db' )
 if os . path . exists ( ooooooO0oo ) :
  Ii11iII1 ( 'Backup Kodi Favourites' , ooooooO0oo , 10062 , i1iIIi1 + 'Backup.png' , oooOOOOO , 'Back Up Your favourites.xml' )
  if 40 - 40: ii11ii1ii + i1IIi * iiiiiIIii
  if 85 - 85: i1Iii * Oo . O0 - i11iIiiIii
  if 18 - 18: i1Iii + I1I1ii - O0
zip = iiIIIII1i1iI . getSetting ( 'zip' )
o00O = xbmc . translatePath ( os . path . join ( zip ) )
def i1Ii1i1I11Iii ( ) :
 I1i1i1 = xbmc . translatePath ( os . path . join ( zip , 'testCBFolder' ) )
 if not os . path . exists ( zip ) :
  oO . ok ( '[COLOR=white]Origin[/COLOR]' , 'The download location you have stored does not exist .\nPlease update the addon settings and try again.' , '' , '' )
  iiIIIII1i1iI . openSettings ( sys . argv [ 0 ] )
  if 73 - 73: O0 * OOOooOooo00O0 + i1Iii + oo0Oo
  if 40 - 40: OoOoOO00 . I1IiI * oOO + iiiiiIIii + iiiiiIIii
  if 9 - 9: o00OO0OOO0 % OoooooooOO . o00oOO0 % o00OO0OOO0
def ii ( name , url , description ) :
 if 'Backup' in name :
  if 'Genie' in name :
   url = IIiiiiiiIi1I1
  elif 'Ivue' in name :
   url = IIIII
  elif 'Kodi' in name :
   url = ooooooO0oo
  i1Ii1i1I11Iii ( )
  iiI = open ( url ) . read ( )
  oOIIiIi = os . path . join ( o00O , description . split ( 'Your ' ) [ 1 ] )
  OOoOooOoOOOoo = open ( oOIIiIi , mode = 'w' )
  OOoOooOoOOOoo . write ( iiI )
  OOoOooOoOOOoo . close ( )
 else :
  if 'guisettings.xml' in description :
   Iiii1iI1i = open ( os . path . join ( o00O , description . split ( 'Your ' ) [ 1 ] ) ) . read ( )
   I1ii1ii11i1I = '<setting type="(.+?)" name="%s.(.+?)">(.+?)</setting>' % skin
   O00OOOoOoo0O = re . compile ( I1ii1ii11i1I ) . findall ( Iiii1iI1i )
   for type , o0OoOO , O0O0Oo00 in O00OOOoOoo0O :
    O0O0Oo00 = O0O0Oo00 . replace ( '&quot;' , '' ) . replace ( '&amp;' , '&' )
    xbmc . executebuiltin ( "Skin.Se	t%s(%s,%s)" % ( type . title ( ) , o0OoOO , O0O0Oo00 ) )
  else :
   oOIIiIi = os . path . join ( url )
   iiI = open ( os . path . join ( o00O , description . split ( 'Your ' ) [ 1 ] ) ) . read ( )
   OOoOooOoOOOoo = open ( oOIIiIi , mode = 'w' )
   OOoOooOoOOOoo . write ( iiI )
   OOoOooOoOOOoo . close ( )
 oO . ok ( "[COLOR=white]Origin[/COLOR]" , "" , 'All Done !' , '' )
 if 80 - 80: o00oOO0 + iiiiiIIii / o00OO0OOO0
 if 79 - 79: oo0Oo
 if 48 - 48: oOO - OOooOOo % i1Iii
 if 36 - 36: o00oOO0 - i1Iii . Oo - i11iIiiIii - iiiiiIIii * Oo
def OooOOOO ( ) :
 iIIIiiI1i1i = 1
 i1Ii1i1I11Iii ( )
 iIII = xbmc . translatePath ( os . path . join ( o00O , 'Build Backup' , 'Full Backup' , '' ) )
 o0o0O = xbmc . translatePath ( os . path . join ( o00O , 'Build Backup' , 'my_full_backup.zip' ) )
 ooooO0oOoOOoO = xbmc . translatePath ( os . path . join ( o00O , 'Build Backup' , 'my_full_backup_GUI_Settings.zip' ) )
 if not os . path . exists ( iIII ) :
  os . makedirs ( iIII )
 I1i11i = i1 . input ( 'Enter a name for this backup' , type = xbmcgui . INPUT_ALPHANUM )
 if ( not I1i11i ) : return False , 0
 IiIi = I1i11i
 OOOOO0O00 = xbmc . translatePath ( os . path . join ( iIII , IiIi + '.zip' ) )
 Iii = [ 'plugin.video.GenieTv' ]
 iIIiIiI1I1 = [ "xbmc.log" , "xbmc.old.log" , "kodi.log" , "kodi.old.log" , '.DS_Store' , '.setup_complete' , 'XBMCHelper.conf' ]
 ooO = [ 'plugin.video.GenieTv' , 'repository.origin' , 'cache' , 'system' , 'Thumbnails' , "peripheral_data" , 'library' , 'keymaps' ]
 iiOO0O0Ooo = [ "xbmc.log" , "xbmc.old.log" , "kodi.log" , "kodi.old.log" , "Textures13.db" , '.DS_Store' , '.setup_complete' , 'XBMCHelper.conf' , 'advancedsettings.xml' ]
 oOoO0 = "Creating full backup of existing build"
 Oo0 = "Creating Community Build"
 oo0O0o00o0O = "Archiving..."
 I11i1II = ""
 OooiiIi1i = "Please Wait"
 I1i11111i1i11 ( i1iiIIiiI111 , OOOOO0O00 , Oo0 , oo0O0o00o0O , I11i1II , OooiiIi1i , ooO , iiOO0O0Ooo )
 time . sleep ( 1 )
 OOoOOO0 = xbmc . translatePath ( os . path . join ( iIII , IiIi + '_guisettings.zip' ) )
 I1I1i = zipfile . ZipFile ( OOoOOO0 , mode = 'w' )
 try :
  I1I1i . write ( xbmc . translatePath ( os . path . join ( i1iiIIiiI111 , 'userdata' , 'profiles.xml' ) ) , 'profiles.xml' , zipfile . ZIP_DEFLATED )
 except : pass
 I1I1i . close ( )
 if iIIIiiI1i1i == 0 :
  oO . ok ( "FAILED!" , 'The guisettings.xml file could not be found on your' , 'system, please reboot and try again.' , '' )
 else :
  oO . ok ( "SUCCESS!" , 'You Are Now Backed Up. If you\'d like to share this build with' , 'the community please post details on the forum at' , '[COLOR=blue][B]http://rh-project.info[/COLOR][/B]' )
  oO . ok ( "Build Locations" , 'Full Backup (only used to restore on this device): [COLOR=yellow]' + o0o0O , '[/COLOR]Universal Backup (can be used on any device): [COLOR=yellow]' + OOOOO0O00 + '[/COLOR]' )
  if 1 - 1: o00OO0OOO0 % iiiiiIIii + O0 + i1IIi - Ooo00oOo00o
def I1i11111i1i11 ( sourcefile , destfile , message_header , message1 , message2 , message3 , exclude_dirs , exclude_files ) :
 iIIIII1ii1I = zipfile . ZipFile ( destfile , 'w' , zipfile . ZIP_DEFLATED )
 Ii1i1iI = len ( sourcefile )
 IIiI1 = [ ]
 i1iI1 = [ ]
 o00 . create ( message_header , message1 , message2 , message3 )
 for ii1 , I1IiiI1ii1i , O0o in os . walk ( sourcefile ) :
  for file in O0o :
   i1iI1 . append ( file )
 oO0OoO00o = len ( i1iI1 )
 for ii1 , I1IiiI1ii1i , O0o in os . walk ( sourcefile ) :
  I1IiiI1ii1i [ : ] = [ II1iiiiII for II1iiiiII in I1IiiI1ii1i if II1iiiiII not in exclude_dirs ]
  O0o [ : ] = [ OOoOooOoOOOoo for OOoOooOoOOOoo in O0o if OOoOooOoOOOoo not in exclude_files ]
  for file in O0o :
   IIiI1 . append ( file )
   O0OoOO0oo0 = len ( IIiI1 ) / float ( oO0OoO00o ) * 100
   o00 . update ( int ( O0OoOO0oo0 ) , "Backing Up" , '[COLOR yellow]%s[/COLOR]' % file , 'Please Wait' )
   oOOO0o0OO0000ooo = os . path . join ( ii1 , file )
   if not 'temp' in I1IiiI1ii1i :
    if not 'plugin.program.originwizard' in I1IiiI1ii1i :
     import time
     iIIII1iIIii = '01/01/1980'
     oOOO00o000o = time . strftime ( '%d/%m/%Y' , time . gmtime ( os . path . getmtime ( oOOO0o0OO0000ooo ) ) )
     if oOOO00o000o > iIIII1iIIii :
      iIIIII1ii1I . write ( oOOO0o0OO0000ooo , oOOO0o0OO0000ooo [ Ii1i1iI : ] )
 iIIIII1ii1I . close ( )
 o00 . close ( )
 if 9 - 9: o00oOO0 + o00OO0OOO0 / o00OO0OOO0
 if 12 - 12: OoooooooOO % OOooOOo * o00OO0OOO0 % iIii1I11I1II1 / i1Iii
def Ii1ii1IiIII ( ) :
 Ii11iII1 ( '[COLORgreen]SCOOBY STREAMS[/COLOR]' , ( oOOoo00O0O ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvdHZjYXRzLnBocA==' ) ) , 1016 , i1iIIi1 + 'scoob.png' , oooOOOOO , '' )
 Ii11iII1 ( '[COLORgreen]SCOOBY SCRAPES[/COLOR]' , iiI1IiI , 1024 , i1iIIi1 + 'scoob.png' , oooOOOOO , '' )
 if 57 - 57: iIii1I11I1II1 / o00OO0OOO0 - i1IIi
 if 51 - 51: I1I1ii
def ii11I1 ( ) :
 Ii11iII1 ( '[COLORgreen]SEARCH MOVIES[/COLOR]' , iiI1IiI , 9001 , i1iIIi1 + 'MOVIESv.png' , oooOOOOO , '' )
 Ii11iII1 ( '[COLORgreen]SEARCH SERIES[/COLOR]' , iiI1IiI , 9002 , i1iIIi1 + 'TVSHOWSv.png' , oooOOOOO , '' )
 Ii11iII1 ( '[COLORgreen]SEARCH CARTOONS[/COLOR]' , '' , 10005 , i1iIIi1 + 'ORIGINCARTOON' , oooOOOOO , '' )
 if 75 - 75: Ooo00oOo00o / OoOoOO00 % O0
 if 38 - 38: OoooooooOO * oo0Oo % O0 * I1IiI
 if 29 - 29: ii11ii1ii / i1IIi . OOOo0 - I1IiI - I1IiI - i1Iii
 if 20 - 20: i1IIi % Ooo00oOo00o . OOOo0 / I1I1ii * i11iIiiIii * iiiiiIIii
def OOo ( ) :
 Ii11iII1 ( '[COLORgreen]RADIO[/COLOR]' , iiI1IiI , 1013 , i1iIIi1 + 'radio.png' , oooOOOOO , '' )
 if iiIIIII1i1iI . getSetting ( 'CONCERTS' ) == 'true' :
  Ii11iII1 ( '[COLORgreen]CONCERTS[/COLOR]' , ( oOOoo00O0O ( 'aHR0cHM6Ly93d3cucmVkZGl0LmNvbS9yL2Z1bGxjb25jZXJ0cy8=' ) ) , 7050 , i1iIIi1 + 'concerts.png' , oooOOOOO , '' )
 Ii11iII1 ( '[COLORgreen]MUSIC[/COLOR]' , iiI1IiI , 1030 , i1iIIi1 + 'MUSIC.png' , oooOOOOO , '' )
 Ii11iII1 ( '[COLORgreen]MUSIC ARCHIVE[/COLOR]' , iiI1IiI + ( oOOoo00O0O ( 'L3ZvZC91cmxzL211c2ljLnBocA==' ) ) , 1010 , i1iIIi1 + 'MUSIC.png' , oooOOOOO , '' )
 Ii11iII1 ( '[COLORgreen]MUSIC SEARCH[/COLOR]' , iiI1IiI , 1111 , i1iIIi1 + 'search.png' , oooOOOOO , '' )
 Ii11iII1 ( '[COLORgreen]KODIBLE AUDIO BOOKS[/COLOR]' , 'http://doremisa.com/audiobooks/' , 30000 , i1iIIi1 + 'kodible.png' , oooOOOOO , '' )
 if 50 - 50: oo0Oo
 I1IiII11III ( 'movies' , 'MAIN' )
 if 72 - 72: oOO
def OO0ooo0oOO ( ) :
 if 97 - 97: OOOo0 / OOOooOooo00O0
 IIiII ( 'DELETE CACHE' , 'url' , 14 , i1iIIi1 + 'MAIN5.png' , oooOOOOO , '' )
 IIiII ( 'DELETE PACKAGES' , 'url' , 6 , i1iIIi1 + 'MAIN4.png' , oooOOOOO , '' )
 IIiII ( 'FORCE REFRESH' , 'url' , 10 , i1iIIi1 + 'MAIN3.png' , oooOOOOO , 'Force Refresh All Repos' )
 if 71 - 71: OoOoOO00 / i1IIi . ii11ii1ii % OoooooooOO . I1IiI
 IIiII ( 'CHECK MY IP' , 'url' , 12 , i1iIIi1 + 'MAIN2.png' , oooOOOOO , '' )
 IIiII ( 'ANDROID ONLY DELETE TEXTURE13.DB&THUBMNAIL FOLDER' , 'url' , 13 , i1iIIi1 + 'MAIN1.png' , oooOOOOO , 'Only Works On Android On Windows It Deletes Your Thumnails Folder But Does Not Delete The Textures13.db' )
 Ii11iII1 ( '[COLORgreen]ADVANCED SETTINGS XML[/COLOR]' , iiI1IiI , 4 , i1iIIi1 + 'XML.png' , oooOOOOO , '' )
 Ii11iII1 ( '[COLORgreen]URL FIXES[/COLOR]' , iiI1IiI , 20 , i1iIIi1 + 'URLFIX.png' , oooOOOOO , '' )
 I1IiII11III ( 'movies' , 'MAIN' )
 if 41 - 41: i1IIi * OoOoOO00 / OoooooooOO . iiiiiIIii
 if 83 - 83: OOOooOooo00O0 . O0 / Oo / iiiiiIIii - OoOoOO00
def I1iII1iiII ( ) :
 Ii11iII1 ( '[COLORgreen]REPOS[/COLOR]' , ( oOOoo00O0O ( 'aHR0cDovL21pcnJvcnMua29kaS50di9hZGRvbnMv' ) ) , 2030 , i1iIIi1 + 'repos.png' , oooOOOOO , '' )
 Ii11iII1 ( '[COLORgreen]NEW[/COLOR]' , iiI1IiI , 22 , i1iIIi1 + 'NEW.png' , oooOOOOO , '' )
 Ii11iII1 ( '[COLORgreen]IPTV[/COLOR]' , iiI1IiI , 23 , i1iIIi1 + 'IPTV.png' , oooOOOOO , '' )
 Ii11iII1 ( '[COLORgreen]VIDEO[/COLOR]' , iiI1IiI , 24 , i1iIIi1 + 'VIDEO.png' , oooOOOOO , '' )
 Ii11iII1 ( '[COLORgreen]SPORTS[/COLOR]' , iiI1IiI , 25 , i1iIIi1 + 'SPORTS.png' , oooOOOOO , '' )
 Ii11iII1 ( '[COLORgreen]KIDS[/COLOR]' , iiI1IiI , 26 , i1iIIi1 + 'KIDS.png' , oooOOOOO , '' )
 Ii11iII1 ( '[COLORgreen]MUSIC[/COLOR]' , iiI1IiI , 27 , i1iIIi1 + 'MUSIC.png' , oooOOOOO , '' )
 Ii11iII1 ( '[COLORgreen]PROGRAMS[/COLOR]' , iiI1IiI , 28 , i1iIIi1 + 'PROGRAMS.png' , oooOOOOO , '' )
 Ii11iII1 ( '[COLORgreen]XXX[/COLOR]' , 'URL' , 29 , i1iIIi1 + 'XXX.png' , oooOOOOO , '' )
 I1IiII11III ( 'movies' , 'MAIN' )
 if 100 - 100: Ooo00oOo00o
 if 46 - 46: I1IiI / iIii1I11I1II1 % OOOooOooo00O0 . iIii1I11I1II1 * OOOooOooo00O0
def IIi1ii1Ii ( ) :
 IIiII ( 'CHECK ADVANCED XML' , iiI1IiI , 8 , i1iIIi1 + 'XML.png' , oooOOOOO , '' )
 IIiII ( 'MUCKYS XML' , iiI1IiI + '/wizard/muckys.xml' , 7 , i1iIIi1 + 'XML.png' , oooOOOOO , '' )
 IIiII ( '0CACHE XML' , iiI1IiI + '/wizard/0cache.xml' , 7 , i1iIIi1 + 'XML.png' , oooOOOOO , '' )
 IIiII ( 'MIKEY1234 XML' , iiI1IiI + '/wizard/mikey.xml' , 7 , i1iIIi1 + 'XML.png' , oooOOOOO , '' )
 IIiII ( 'TUXENS XML' , iiI1IiI + '/wizard/tuxens.xml' , 7 , i1iIIi1 + 'XML.png' , oooOOOOO , '' )
 IIiII ( 'P2P RECOMMENDED XML1' , iiI1IiI + '/wizard/p2p1.xml' , 7 , i1iIIi1 + 'XML.png' , oooOOOOO , '' )
 IIiII ( 'P2P RECOMMENDED XML2' , iiI1IiI + '/wizard/p2p2.xml' , 7 , i1iIIi1 + 'XML.png' , oooOOOOO , '' )
 IIiII ( 'DELETE XML' , iiI1IiI , 11 , i1iIIi1 + 'XML.png' , oooOOOOO , '' )
 I1IiII11III ( 'movies' , 'MAIN' )
 if 91 - 91: i11iIiiIii / OoooooooOO + OOOooOooo00O0 - i11iIiiIii + iiiiiIIii
def ii1i ( ) :
 IIiII ( '[COLORgreen]My Local Zip[/COLOR]' , i11 , 48 , i1iIIi1 + 'MB.png' , oooOOOOO , '' )
 IIiII ( '[COLORgreen]My Online Zip[/COLOR]' , i1111 , 43 , i1iIIi1 + 'MB.png' , oooOOOOO , '' )
 if 62 - 62: Ooo00oOo00o / ii11ii1ii
def ii1O000OOO0OOo ( ) :
 IIiII ( 'INSTALL FTV GUIDE AND OTHER ADDONS REQUIRED' , iiI1IiI + '/wizard/customftv/ftvguide-addons.zip' , 5 , i1iIIi1 + 'FTV4.png' , oooOOOOO , '' )
 IIiII ( 'FTV GUIDE FIRST RUN SETTINGS' , iiI1IiI + '/wizard/customftv/settings.xml' , 17 , i1iIIi1 + 'FTV3.png' , oooOOOOO , '' )
 IIiII ( 'FTV GUIDE ADDONS2.INI UPDATE DAILY' , 'http://ren.byethost12.com/addons2.ini' , 16 , i1iIIi1 + 'FTV1.png' , oooOOOOO , '' )
 IIiII ( 'RESET FTV DATABASE' , 'url' , 18 , i1iIIi1 + 'FTV2.png' , oooOOOOO , '' )
 if 32 - 32: i1Iii * O0
 if 100 - 100: oo0Oo % iIii1I11I1II1 * OoOoOO00 - OOOooOooo00O0
 if 92 - 92: oo0Oo
def II11iI111i1 ( ) :
 Ii11iII1 ( '[COLORgreen]SKINS[/COLOR]' , iiI1IiI , 33 , i1iIIi1 + 'skinp.png' , oooOOOOO , '' )
 Ii11iII1 ( '[COLORgreen]ARTWORK PACKS[/COLOR]' , iiI1IiI , 34 , i1iIIi1 + 'artp.png' , oooOOOOO , '' )
 Ii11iII1 ( '[COLORgreen]CREATE UNIVERSAL PATHS[/COLOR]' , i1iiIIiiI111 , 35 , i1iIIi1 + 'GUI.png' , oooOOOOO , '' )
 I1IiII11III ( 'movies' , 'MAIN' )
 if 95 - 95: OoooooooOO - I1I1ii * OOOo0 + I1IiI
def iIi1 ( url ) :
 i11iiI1111 = ii1ii11IIIiiI ( oOoooo000Oo00 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 O00OOOoOoo0O = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( i11iiI1111 )
 for ii11IIII11I , url , o0OoOo00o0o , I1II1I11I1I , i11I in O00OOOoOoo0O :
  Ii11iII1 ( ii11IIII11I , url , 5 , o0OoOo00o0o , I1II1I11I1I , i11I )
 I1IiII11III ( 'movies' , 'MAIN' )
 if 93 - 93: ii11ii1ii / OOOo0 / iIii1I11I1II1 % oOO % oOO
def IiI11iI1i1i1i ( ) :
 Ii11iII1 ( '[COLORgreen]GOTHAM SKINS[/COLOR]' , iiI1IiI , 36 , i1iIIi1 + 'GSKIN.png' , oooOOOOO , '' )
 Ii11iII1 ( '[COLORgreen]HELIX SKINS[/COLOR]' , iiI1IiI , 37 , i1iIIi1 + 'HSKIN.png' , oooOOOOO , '' )
 Ii11iII1 ( '[COLORgreen]ISENGAARD SKINS[/COLOR]' , i1iiIIiiI111 , 38 , i1iIIi1 + 'ISKIN.png' , oooOOOOO , '' )
 I1IiII11III ( 'movies' , 'MAIN' )
 if 89 - 89: o00OO0OOO0
def Ooooooo ( url ) :
 i11iiI1111 = ii1ii11IIIiiI ( iiI1IiI + I1IIIiI1I1ii1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 O00OOOoOoo0O = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( i11iiI1111 )
 for ii11IIII11I , url , o0OoOo00o0o , I1II1I11I1I , i11I in O00OOOoOoo0O :
  Ii11iII1 ( ii11IIII11I , url , 42 , o0OoOo00o0o , I1II1I11I1I , i11I )
 I1IiII11III ( 'movies' , 'MAIN' )
 if 30 - 30: O0 * OoooooooOO
def I1iIIIi1 ( url ) :
 i11iiI1111 = ii1ii11IIIiiI ( iiI1IiI + IiiI1iiiiI1iI ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 O00OOOoOoo0O = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( i11iiI1111 )
 for ii11IIII11I , url , o0OoOo00o0o , I1II1I11I1I , i11I in O00OOOoOoo0O :
  Ii11iII1 ( ii11IIII11I , url , 42 , o0OoOo00o0o , I1II1I11I1I , i11I )
 I1IiII11III ( 'movies' , 'MAIN' )
 if 43 - 43: o00oOO0 - OoooooooOO
def ii1iI ( url ) :
 i11iiI1111 = ii1ii11IIIiiI ( iiI1IiI + IIi ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 O00OOOoOoo0O = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( i11iiI1111 )
 for ii11IIII11I , url , o0OoOo00o0o , I1II1I11I1I , i11I in O00OOOoOoo0O :
  Ii11iII1 ( ii11IIII11I , url , 42 , o0OoOo00o0o , I1II1I11I1I , i11I )
 I1IiII11III ( 'movies' , 'MAIN' )
 if 89 - 89: OoOoOO00 + i1IIi + OoOoOO00
def IiII1II11I ( url ) :
 i11iiI1111 = ii1ii11IIIiiI ( oOOoo00O0O ( 'aHR0cHM6Ly9kbC5kcm9wYm94dXNlcmNvbnRlbnQuY29tL3MvN2ZrMjhndDlwb3QxMjJhL0JVSUxEUy50eHQ/ZGw9MA==' ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 O00OOOoOoo0O = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( i11iiI1111 )
 for ii11IIII11I , url , o0OoOo00o0o , I1II1I11I1I , i11I in O00OOOoOoo0O :
  Ii11iII1 ( ii11IIII11I , url , 42 , o0OoOo00o0o , I1II1I11I1I , i11I )
 I1IiII11III ( 'movies' , 'MAIN' )
 if 54 - 54: I1I1ii + O0 + o00OO0OOO0 * oOO - iiiiiIIii % o00oOO0
def I111 ( url ) :
 i11iiI1111 = ii1ii11IIIiiI ( iiI1IiI + iI1I1i11iIIii ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 O00OOOoOoo0O = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( i11iiI1111 )
 for ii11IIII11I , url , o0OoOo00o0o , I1II1I11I1I , i11I in O00OOOoOoo0O :
  Ii11iII1 ( ii11IIII11I , url , 40 , o0OoOo00o0o , I1II1I11I1I , i11I )
 I1IiII11III ( 'movies' , 'MAIN' )
 if 46 - 46: o00oOO0 % Ooo00oOo00o - iIii1I11I1II1 + i1Iii - oOO * ii11ii1ii
def iIIIIIii ( url ) :
 i11iiI1111 = ii1ii11IIIiiI ( iiI1IiI + Ii1ii111i1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 O00OOOoOoo0O = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( i11iiI1111 )
 for ii11IIII11I , url , o0OoOo00o0o , I1II1I11I1I , i11I in O00OOOoOoo0O :
  Ii11iII1 ( ii11IIII11I , url , 5 , o0OoOo00o0o , I1II1I11I1I , i11I )
 I1IiII11III ( 'movies' , 'MAIN' )
 if 31 - 31: iiiiiIIii + O0
def oO0oOOoo00000 ( ) :
 oOOooOoo = o0OOOoO0 ( oOOoo00O0O ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vYXBrdG9vbC9hcGsucGhw' ) )
 O00OOOoOoo0O = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( oOOooOoo )
 for o0ooooO0o0O , OooooOOoo0 , ii11IIII11I in O00OOOoOoo0O :
  oOo00 ( ii11IIII11I , o0ooooO0o0O , 2031 , OooooOOoo0 )
  if 3 - 3: OOOooOooo00O0 % i1IIi
def Ii1IIiiIIi ( name , url , description ) :
 I1i1i1 = xbmc . translatePath ( os . path . join ( Oo000o , 'Download' ) )
 o00 = xbmcgui . DialogProgress ( )
 o00 . create ( "Your App Is Downloading" , "Why not check out our website" , '' , 'Http://architects.x10host.com' )
 i11I1iIi = os . path . join ( I1i1i1 , name + '.apk' )
 try :
  os . remove ( i11I1iIi )
 except :
  pass
 downloader . download ( url , i11I1iIi , o00 )
 oO = xbmcgui . Dialog ( )
 oO . ok ( "GenieTv" , "[COLORred]Please press ok, exit kodi and go to your downloads folder to install your app[/COLOR]" , "[COLORblue]Tool Brought To You By Architects@Work[/COLOR]" )
 if 79 - 79: oOO . o00oOO0 - OoOoOO00 . OOOo0 % oo0Oo
def oOoO00 ( url ) :
 I1i1i1 = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/resources/downloads' ) )
 o00 = xbmcgui . DialogProgress ( )
 o00 . create ( "Your fILM Is Downloading" , "Why not check out our website" , '' , 'Http://architects.x10host.com' )
 i11I1iIi = os . path . join ( I1i1i1 , ii11IIII11I + '.mp4' )
 try :
  os . remove ( i11I1iIi )
 except :
  pass
 downloader . download ( url , i11I1iIi , o00 )
 oO = xbmcgui . Dialog ( )
 oO . ok ( "GenieTv" , "[COLORred]Please press ok, Your download With Be Avaiilable Via The My Downloads Button[/COLOR]" , "[COLORblue]Tool Brought To You By Architects@Work[/COLOR]" )
 if 40 - 40: OOooOOo
 if 67 - 67: o00oOO0 + OoOoOO00 - O0 . o00oOO0 * OoOoOO00 * o00OO0OOO0
def o00OO00O0oOO ( name , url , description ) :
 I1i1i1 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 o00 = xbmcgui . DialogProgress ( )
 o00 . create ( "Your Art Pack Is Downloading" , "Why not check out our website" , '' , 'Http://architects.x10host.com' )
 i11I1iIi = os . path . join ( I1i1i1 , name )
 try :
  os . remove ( i11I1iIi )
 except :
  pass
 downloader . download ( url , i11I1iIi , o00 )
 Ii1iI111 = xbmc . translatePath ( os . path . join ( o0oO0 ) )
 time . sleep ( 2 )
 o00 . update ( 0 , "" , "Placing Your Art Please Wait" )
 print '======================================='
 print Ii1iI111
 print '======================================='
 extract . all ( i11I1iIi , Ii1iI111 , o00 )
 oO = xbmcgui . Dialog ( )
 oO . ok ( "GenieTv" , "[COLORred]Once complete your artwork will be stored in your Media folder, Accessible via the Homefolder, Enjoy[/COLOR]" )
 if 51 - 51: I1I1ii * O0 / OoOoOO00 . i1Iii % iiiiiIIii / OOOo0
 if 9 - 9: OOOo0 % OOOo0 % OoOoOO00
def I1I1i1Ioo0oo ( url ) :
 i11iiI1111 = ii1ii11IIIiiI ( oOOoo00O0O ( 'aHR0cDovL2dlbmlldHYuYXJjaGl0ZWN0cy54MTBob3N0LmNvbS90ZXN0L3doLnR4dA==' ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 O00OOOoOoo0O = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( i11iiI1111 )
 for ii11IIII11I , url , o0OoOo00o0o , I1II1I11I1I , i11I in O00OOOoOoo0O :
  Ii11iII1 ( ii11IIII11I , url , 5 , o0OoOo00o0o , I1II1I11I1I , i11I )
 try :
  i11iiI1111 = ii1ii11IIIiiI ( IIi11IIiIii1 + oOo0oooo00o + I1iIII1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
  O00OOOoOoo0O = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( i11iiI1111 )
  for ii11IIII11I , url , o0OoOo00o0o , I1II1I11I1I , i11I in O00OOOoOoo0O :
   Ii11iII1 ( ii11IIII11I , url , 5 , o0OoOo00o0o , I1II1I11I1I , i11I )
 except : pass
 I1IiII11III ( 'movies' , 'INFO' )
 if 39 - 39: OoooooooOO
 if 38 - 38: OOOo0
def oOo0OoOOo0 ( url ) :
 i11iiI1111 = ii1ii11IIIiiI ( oOOoo00O0O ( 'aHR0cDovL2dlbmlldHYuYXJjaGl0ZWN0cy54MTBob3N0LmNvbS90ZXN0L3doLnR4dA==' ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 O00OOOoOoo0O = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( i11iiI1111 )
 for ii11IIII11I , url , o0OoOo00o0o , I1II1I11I1I , i11I in O00OOOoOoo0O :
  Ii11iII1 ( ii11IIII11I , url , 43 , o0OoOo00o0o , I1II1I11I1I , i11I )
 try :
  i11iiI1111 = ii1ii11IIIiiI ( IIi11IIiIii1 + oOo0oooo00o + I1iIII1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
  O00OOOoOoo0O = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( i11iiI1111 )
  for ii11IIII11I , url , o0OoOo00o0o , I1II1I11I1I , i11I in O00OOOoOoo0O :
   Ii11iII1 ( ii11IIII11I , url , 43 , o0OoOo00o0o , I1II1I11I1I , i11I )
 except : pass
 I1IiII11III ( 'movies' , 'INFO' )
 if 30 - 30: ii11ii1ii % OOOo0
 if 89 - 89: oOO + OoooooooOO + oOO * i1IIi + iIii1I11I1II1 % o00OO0OOO0
def oOo0oO ( name , url , description ) :
 I1i1i1 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 o00 = xbmcgui . DialogProgress ( )
 o00 . create ( "GenieTv" , "Downloading Content" , '' , 'Please Wait' )
 i11I1iIi = os . path . join ( I1i1i1 , name + '.zip' )
 try :
  os . remove ( i11I1iIi )
 except :
  pass
 downloader . download ( url , i11I1iIi , o00 )
 IIi1IIIIi = xbmc . translatePath ( os . path . join ( 'special://home' , 'addons' ) )
 time . sleep ( 2 )
 o00 . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print IIi1IIIIi
 print '======================================='
 extract . all ( i11I1iIi , IIi1IIIIi , o00 )
 oO = xbmcgui . Dialog ( )
 oO . ok ( "GenieTv" , "Press ok to finish install" , "[COLOR yellow]Brought To You By Architects@Work[/COLOR]" )
 o0O00o ( )
 if 70 - 70: iiiiiIIii / OoOoOO00 - iIii1I11I1II1 - OOOooOooo00O0
 if 11 - 11: iIii1I11I1II1 . OoooooooOO . OoOoOO00 / i1IIi - o00OO0OOO0
def ii1ii11 ( name , url , description ) :
 I1i1i1 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 o00 = xbmcgui . DialogProgress ( )
 o00 . create ( "GenieTv" , "Downloading " , '' , 'Please Wait' )
 i11I1iIi = os . path . join ( I1i1i1 , 'plugin.program.GenieTv.install' + '.zip' )
 try :
  os . remove ( i11I1iIi )
 except :
  pass
 downloader . download ( url , i11I1iIi , o00 )
 IIi1IIIIi = xbmc . translatePath ( os . path . join ( 'special://' , 'home' ) )
 time . sleep ( 2 )
 o00 . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print IIi1IIIIi
 print '======================================='
 extract . all ( i11I1iIi , IIi1IIIIi , o00 )
 oO = xbmcgui . Dialog ( )
 oO . ok ( "GenieTv" , "Press ok to force close kodi, if unsuccessful using windows Please kill kodi via taskmanager" , "[COLOR yellow]Brought To You By Architects@Work[/COLOR]" )
 OoOoo0oO ( )
 if 10 - 10: OoOoOO00 . OOOooOooo00O0
def I1iOOOO ( name , url , description ) :
 I1i1i1 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 o00 = xbmcgui . DialogProgress ( )
 o00 . create ( "GenieTv" , "Downloading " , '' , 'Please Wait' )
 i11I1iIi = os . path . join ( I1i1i1 , 'plugin.program.GenieTv.install' + '.zip' )
 try :
  os . remove ( i11I1iIi )
 except :
  pass
 downloader . download ( url , i11I1iIi , o00 )
 IIi1IIIIi = xbmc . translatePath ( os . path . join ( 'special://' , 'home' ) )
 time . sleep ( 2 )
 o00 . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print IIi1IIIIi
 print '======================================='
 extract . all ( i11I1iIi , IIi1IIIIi , o00 )
 oO = xbmcgui . Dialog ( )
 oO . ok ( "GenieTv" , "Please Disconnect The Power From Your Device. DO NOT EXIT CLEANLY VIA SHUTDOWN" , "[COLOR yellow]Brought To You By Architects@Work[/COLOR]" )
 if 88 - 88: OOOooOooo00O0
 if 19 - 19: OoOoOO00 * I1I1ii + i1Iii
def O0ooO00oO ( name , url , description ) :
 IIi1IIIIi = xbmc . translatePath ( os . path . join ( 'special://' , 'home' ) )
 o00 = xbmcgui . DialogProgress ( )
 i11I1iIi = os . path . join ( i11 )
 time . sleep ( 2 )
 o00 . create ( "GenieTv" , "Restoring" , '' , 'Please Wait' )
 print '======================================='
 print IIi1IIIIi
 print '======================================='
 extract . all ( i11I1iIi , IIi1IIIIi , o00 )
 oO = xbmcgui . Dialog ( )
 oO . ok ( "GenieTv" , "Please Disconnect The Power From Your Device. DO NOT EXIT CLEANLY VIA SHUTDOWN" , "[COLOR yellow]Brought To You By Architects@Work[/COLOR]" )
 if 36 - 36: iiiiiIIii
 if 84 - 84: oOO . Ooo00oOo00o . OoOoOO00 . o00OO0OOO0 / i1Iii % ii11ii1ii
def OoOoo0oO ( ) :
 OOO0oOoO0O = xbmcgui . Dialog ( ) . yesno ( 'Force Close Kodi' , 'You are about to close Kodi' , 'Would you like to continue?' , nolabel = 'No, Cancel' , yeslabel = 'Yes, Close' )
 if OOO0oOoO0O == 0 :
  return
 elif OOO0oOoO0O == 1 :
  pass
 OoOo000oOo0oo = oO0O ( )
 print "Platform: " + str ( OoOo000oOo0oo )
 if OoOo000oOo0oo == 'osx' :
  print "############   try osx force close  #################"
  try : os . system ( 'killall -9 XBMC' )
  except : pass
  try : os . system ( 'killall -9 Kodi' )
  except : pass
  oO . ok ( "[COLOR=red][B]WARNING  !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu." , '' )
 elif OoOo000oOo0oo == 'linux' :
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
 elif OoOo000oOo0oo == 'android' :
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
 elif OoOo000oOo0oo == 'windows' :
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
  if 86 - 86: I1IiI . iIii1I11I1II1 - Ooo00oOo00o
def oO0O ( ) :
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
  if 56 - 56: O0
  if 61 - 61: OOooOOo / iiiiiIIii / Oo * O0
  if 23 - 23: o00oOO0 - iiiiiIIii + o00OO0OOO0
def II11 ( url ) :
 o00 . create ( "[COLOR=green]GenieTv[/COLOR]" , "Renaming paths..." , '' , 'Please Wait' )
 for Iiii11iIi1 , I1IiiI1ii1i , O0o in os . walk ( url ) :
  for file in O0o :
   if file . endswith ( ".xml" ) :
    o00 . update ( 0 , "Fixing" , file , 'Please Wait' )
    Iiii1iI1i = open ( ( os . path . join ( Iiii11iIi1 , file ) ) ) . read ( )
    i1iI11I1II1 = Iiii1iI1i . replace ( i1iiIIiiI111 , 'special://home/' )
    OOoOooOoOOOoo = open ( ( os . path . join ( Iiii11iIi1 , file ) ) , mode = 'w' )
    OOoOooOoOOOoo . write ( str ( i1iI11I1II1 ) )
    OOoOooOoOOOoo . close ( )
 OoOoo0oO ( )
 if 14 - 14: i11iIiiIii - OOOooOooo00O0 * I1IiI
def OO0oIII111i11IiI ( ) :
 oOOooOoo = o0OOOoO0 ( oOOoo00O0O ( 'aHR0cDovL3d3dy5saXN0ZW5saXZlLmV1L3VrLmh0bWw=' ) )
 O00OOOoOoo0O = re . compile ( '<tr>.+?<td><a href=".+?"><b>(.+?)</b>.+?<td><a href="(.+?)">' , re . DOTALL ) . findall ( oOOooOoo )
 for ii11IIII11I , o0ooooO0o0O in O00OOOoOoo0O :
  O0000 ( ii11IIII11I , o0ooooO0o0O , 222 , i1iIIi1 + 'radio.png' )
  if 64 - 64: OoOoOO00 - OOOo0
def O0O0ooOOO ( ) :
 oOOooOoo = o0OOOoO0 ( oOOoo00O0O ( 'aHR0cDovL3d3dy50b29uamV0LmNvbS8=' ) )
 O00OOOoOoo0O = re . compile ( '<a href="(.+?)" style="font-size:.8em;">(.+?)</a>' ) . findall ( oOOooOoo )
 for o0ooooO0o0O , ii11IIII11I in O00OOOoOoo0O :
  oOo00 ( '[COLORgreen]' + ii11IIII11I + '[/COLOR]' , 'http://www.toonjet.com/' + o0ooooO0o0O , 8051 , i1iIIi1 + 'classictoons.png' )
def o0o00Ooo0o ( url ) :
 oOOooOoo = o0OOOoO0 ( url )
 O00OOOoOoo0O = re . compile ( '<a href="(.+?)"><img src="(.+?)"' ) . findall ( oOOooOoo )
 I1i = re . compile ( '<a href="(.+?)">.+?</a></td></tr></table>' ) . findall ( oOOooOoo )
 for url , i1111I1I in O00OOOoOoo0O :
  if 'ol.gif' in i1111I1I :
   pass
  elif 'link_block_' in i1111I1I :
   pass
  elif '.png' in i1111I1I :
   pass
  else :
   oOo00 ( ( i1111I1I ) . replace ( 'http://www.toonjet.com/images/icons/' , '' ) . replace ( 'images/icons/' , '' ) . replace ( '.jpg' , '' ) . replace ( '_icon' , '' ) . replace ( '_' , ' ' ) , 'http://www.toonjet.com/' + url , 8052 , i1iIIi1 + 'vod.png' )
 for url in I1i :
  oOo00 ( 'NEXT PAGE' , 'http://www.toonjet.com/' + url , 8051 , i1iIIi1 + 'Next.png' )
def oo00o ( url ) :
 oOOooOoo = o0OOOoO0 ( url )
 O00OOOoOoo0O = re . compile ( '<iframe width="640" height="480" src="(.+?)" frameborder="0" allowfullscreen></iframe>' ) . findall ( oOOooOoo )
 for url in O00OOOoOoo0O :
  O0000 ( '[COLORgreen]PLAY[/COLOR]' , ( url ) . replace ( 'http://www.youtube.com/embed/' , '' ) . replace ( '?autoplay=0' , '' ) , 8043 , i1iIIi1 + 'classictoons.png' )
  if 76 - 76: OOOooOooo00O0
  if 11 - 11: I1I1ii % ii11ii1ii % i1Iii / OoOoOO00 % oOO - Oo
def OOooO ( ) :
 O00O0OO00oo ( 'Audio Books' , '' , 30011 , i1iIIi1 + 'audiobooks.png' , i1iIIi1 + 'audiobooks.png' , '' )
 O00O0OO00oo ( 'Kids Audio Books' , '' , 30006 , i1iIIi1 + 'kidsaudiobooks.png' , i1iIIi1 + 'kidsaudiobooks.png' , '' )
 if 69 - 69: OOooOOo / Oo
def IIiIii ( ) :
 O00O0OO00oo ( 'All' , '' , 30001 , i1iIIi1 + 'kodible.png' , i1iIIi1 + 'kodible.png' , '' )
 O00O0OO00oo ( 'Popular' , '' , 30012 , i1iIIi1 + 'POPULARv.png' , i1iIIi1 + 'POPULARv.png' , '' )
 O00O0OO00oo ( 'Search' , '' , 30013 , i1iIIi1 + 'search.png' , i1iIIi1 + 'search.png' , '' )
 if 6 - 6: iiiiiIIii - ii11ii1ii + i1Iii + i1IIi / O0 / OOooOOo
def Iiii1I1 ( ) :
 O0oOoOOOoOO = ii1ii11IIIiiI ( II11iiii1Ii + 'books' + OooO0 )
 O00OOOoOoo0O = re . compile ( '<NAME=>(.*?)</NAME><URL=>(.*?)</URL><CAT=>(.*?)</CAT>' ) . findall ( O0oOoOOOoOO )
 for ii11IIII11I , o0ooooO0o0O , O0II11i11II in O00OOOoOoo0O :
  if 'Parent' in ii11IIII11I :
   pass
  elif '2' in O0II11i11II :
   O00O0OO00oo ( ( ii11IIII11I ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , o0ooooO0o0O , 30010 , i1iIIi1 + 'kodible.png' , i1iIIi1 + 'kodible.png' , '' )
   if 29 - 29: Oo % Ooo00oOo00o % I1I1ii . OOooOOo / OoooooooOO * oo0Oo
def o0OoO000O ( ) :
 Iii1I1I11iiI1 = i1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 ii1I = Iii1I1I11iiI1 . lower ( )
 O0oOoOOOoOO = ii1ii11IIIiiI ( II11iiii1Ii + 'books' + OooO0 )
 O00OOOoOoo0O = re . compile ( '<NAME=>(.*?)</NAME><URL=>(.*?)</URL><CAT=>(.*?)</CAT>' ) . findall ( O0oOoOOOoOO )
 for ii11IIII11I , o0ooooO0o0O , O0II11i11II in O00OOOoOoo0O :
  if Iii1I1I11iiI1 in ii11IIII11I . lower ( ) :
   if '1' in O0II11i11II :
    O00O0OO00oo ( ( ii11IIII11I ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , o0ooooO0o0O , 30010 , i1iIIi1 + 'kodible.png' , i1iIIi1 + 'kodible.png' , '' )
   elif '2' in O0II11i11II :
    O00O0OO00oo ( ( ii11IIII11I ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , o0ooooO0o0O , 30010 , i1iIIi1 + 'kodible.png' , i1iIIi1 + 'kodible.png' , '' )
   elif '3' in O0II11i11II :
    O00O0OO00oo ( ( ii11IIII11I ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , o0ooooO0o0O , 30009 , i1iIIi1 + 'kodible.png' , i1iIIi1 + 'kodible.png' , '' )
    if 94 - 94: I1IiI . O0 / i1Iii . ii11ii1ii - i1IIi
    if 26 - 26: Ooo00oOo00o - iiiiiIIii . OOooOOo
def OO0o0o0oo0O ( ) :
 O0oOoOOOoOO = ii1ii11IIIiiI ( II11iiii1Ii + 'books' + OooO0 )
 O00OOOoOoo0O = re . compile ( '<NAME=>(.*?)</NAME><URL=>(.*?)</URL><CAT=>(.*?)</CAT>' ) . findall ( O0oOoOOOoOO )
 for ii11IIII11I , o0ooooO0o0O , O0II11i11II in O00OOOoOoo0O :
  if '1' in O0II11i11II :
   O00O0OO00oo ( ( ii11IIII11I ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , o0ooooO0o0O , 3010 , i1iIIi1 + 'kodible.png' , i1iIIi1 + 'kodible.png' , '' )
  elif '2' in O0II11i11II :
   O00O0OO00oo ( ( ii11IIII11I ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , o0ooooO0o0O , 30010 , i1iIIi1 + 'kodible.png' , i1iIIi1 + 'kodible.png' , '' )
  elif '3' in O0II11i11II :
   O00O0OO00oo ( ( ii11IIII11I ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , o0ooooO0o0O , 30009 , i1iIIi1 + 'kodible.png' , i1iIIi1 + 'kodible.png' , '' )
   if 40 - 40: OOooOOo + Oo . OOooOOo % oo0Oo
 xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 15 - 15: i1Iii * Oo % ii11ii1ii * iIii1I11I1II1 - i11iIiiIii
def Oo00OOOOoo0oo ( url ) :
 oO00oooOOoOo0 = url
 O0oOoOOOoOO = ii1ii11IIIiiI ( url )
 I1i = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( O0oOoOOOoOO )
 for url , ii11IIII11I in I1i :
  if 'mp3' in ii11IIII11I :
   Ii11iII1 ( ( ii11IIII11I ) . replace ( '%20' , ' ' ) , oO00oooOOoOo0 + url , 10012 , i1iIIi1 + 'kodible.png' , i1iIIi1 + 'kodible.png' , '' )
  if 'wma' in ii11IIII11I :
   Ii11iII1 ( ( ii11IIII11I ) . replace ( '%20' , ' ' ) , oO00oooOOoOo0 + url , 10012 , i1iIIi1 + 'kodible.png' , i1iIIi1 + 'kodible.png' , '' )
  if 'm4b' in ii11IIII11I :
   Ii11iII1 ( ( ii11IIII11I ) . replace ( '%20' , ' ' ) , oO00oooOOoOo0 + url , 10012 , i1iIIi1 + 'kodible.png' , i1iIIi1 + 'kodible.png' , '' )
  elif '/' in ii11IIII11I :
   O00O0OO00oo ( ( ii11IIII11I ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , oO00oooOOoOo0 + url , 30009 , i1iIIi1 + 'kodible.png' , i1iIIi1 + 'kodible.png' , '' )
   if 80 - 80: oOO * I1IiI * OoOoOO00 - O0 . I1IiI % OOOo0
   if 13 - 13: o00oOO0 . OOOo0 * o00oOO0 + OOOo0
   if 59 - 59: OOOo0 + i11iIiiIii + i1IIi / o00OO0OOO0
def I11iIiI1 ( url ) :
 O0oOoOOOoOO = ii1ii11IIIiiI ( url )
 oO00oooOOoOo0 = url
 O00OOOoOoo0O = re . compile ( '<li><a href="(.+?)">(.+?)</a></li>' ) . findall ( O0oOoOOOoOO )
 for url , ii11IIII11I in O00OOOoOoo0O :
  if 'Parent' in ii11IIII11I :
   pass
  elif '.db' in ii11IIII11I :
   pass
  elif '.jpg' in ii11IIII11I :
   pass
  elif '.html' in ii11IIII11I :
   pass
  elif '.doc' in ii11IIII11I :
   pass
  elif 'mp3' in ii11IIII11I :
   Ii11iII1 ( ( ii11IIII11I ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , oO00oooOOoOo0 + url , 10012 , i1iIIi1 + 'kodible.png' , i1iIIi1 + 'kodible.png' , '' )
  elif 'm4a' in ii11IIII11I :
   Ii11iII1 ( ( ii11IIII11I ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , oO00oooOOoOo0 + url , 10012 , i1iIIi1 + 'kodible.png' , i1iIIi1 + 'kodible.png' , '' )
  else :
   O00O0OO00oo ( ( ii11IIII11I ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , oO00oooOOoOo0 + url , 30010 , i1iIIi1 + 'kodible.png' , i1iIIi1 + 'kodible.png' , '' )
   if 86 - 86: OOooOOo
   if 27 - 27: O0 . OOooOOo . ii11ii1ii . ii11ii1ii + ii11ii1ii * OOooOOo
def oOo00oOOOOO ( ) :
 O00O0OO00oo ( 'A-Z' , '' , 7 , i1iIIi1 + 'kodible.png' , i1iIIi1 + 'kodible.png' , '' )
 O00O0OO00oo ( 'All' , '' , 3 , i1iIIi1 + 'kodible.png' , i1iIIi1 + 'kodible.png' , '' )
 O00O0OO00oo ( 'Search' , '' , 14 , i1iIIi1 + 'kodible.png' , i1iIIi1 + 'kodible.png' , '' )
 if 85 - 85: OoooooooOO - Ooo00oOo00o - oOO / oo0Oo - o00OO0OOO0
def iIiI ( ) :
 O0oOoOOOoOO = ii1ii11IIIiiI ( oOOoo00O0O ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9tcDNfZG93bmxvYWRzLmh0bQ==' ) )
 O00OOOoOoo0O = re . compile ( '<td width=".+?" align="center">.+?<a href="(.*?)">.+?<img border="0" src="images/Squeeze%20(.*?).gif" width="74" height=".*?"></a></td>' , re . DOTALL ) . findall ( O0oOoOOOoOO )
 for o0ooooO0o0O , i1111I1I in O00OOOoOoo0O :
  print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<' + o0ooooO0o0O + '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
  if '-x' in i1111I1I :
   pass
  else :
   O00O0OO00oo ( i1111I1I , ( oOOoo00O0O ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) ) + ( o0ooooO0o0O ) . replace ( 'colour_it' , 'books_audio/audio_books_a' ) , 30008 , ( oOOoo00O0O ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9pbWFnZXMvU3F1ZWV6ZSUyMA==' ) ) + i1111I1I + '.gif' , i1iIIi1 + 'kodible.png' , '' )
   if 5 - 5: Oo * I1IiI
 xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 46 - 46: oo0Oo
 if 33 - 33: OOOooOooo00O0 - OoOoOO00 * OoooooooOO - Oo - iiiiiIIii
def O0OO0OIiiiIiiI ( url ) :
 O0oOoOOOoOO = ii1ii11IIIiiI ( url )
 O00OOOoOoo0O = re . compile ( '<td width=".*?" height=".*?"><b>.*?<a href="(.*?)">(.*?)</a></b></td>' , re . DOTALL ) . findall ( O0oOoOOOoOO )
 for url , ii11IIII11I in O00OOOoOoo0O :
  if '</a>' in ii11IIII11I :
   pass
  elif '(' in ii11IIII11I :
   O00O0OO00oo ( ( ii11IIII11I ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '.mp3' , '' ) , oOOoo00O0O ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) + url , 30005 , i1iIIi1 + 'kodible.png' , i1iIIi1 + 'kodible.png' , '' )
  else :
   Ii11iII1 ( ( ii11IIII11I ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '.mp3' , '' ) , oOOoo00O0O ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) + url , 30004 , i1iIIi1 + 'kodible.png' , i1iIIi1 + 'kodible.png' , '' )
   if 72 - 72: i1IIi
 xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 82 - 82: I1IiI + OoooooooOO / i11iIiiIii * ii11ii1ii . OoooooooOO
def oooo0OOo ( ) :
 Iii1I1I11iiI1 = i1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 ii1I = Iii1I1I11iiI1 . lower ( )
 O0oOoOOOoOO = ii1ii11IIIiiI ( oOOoo00O0O ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9jb21wbGV0ZV9saXN0Lmh0bQ==' ) )
 O00OOOoOoo0O = re . compile ( '<td width=".+?">.*?<b>.+?<a href="(.*?)">(.*?)</a></b></td>' , re . DOTALL ) . findall ( O0oOoOOOoOO )
 for o0ooooO0o0O , ii11IIII11I in O00OOOoOoo0O :
  if Iii1I1I11iiI1 in ii11IIII11I . lower ( ) :
   if '</a>' in ii11IIII11I :
    pass
   elif '(' in ii11IIII11I :
    O00O0OO00oo ( ( ii11IIII11I ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , oOOoo00O0O ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + o0ooooO0o0O , 30005 , i1iIIi1 + 'kodible.png' , i1iIIi1 + 'kodible.png' , '' )
   else :
    Ii11iII1 ( ( ii11IIII11I ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , oOOoo00O0O ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + o0ooooO0o0O , 30004 , i1iIIi1 + 'kodible.png' , i1iIIi1 + 'kodible.png' , '' )
    if 72 - 72: O0 / oo0Oo + OoooooooOO * OOOooOooo00O0
    if 61 - 61: OoooooooOO % OoOoOO00 - OOOo0 % ii11ii1ii + i1IIi
def i1II ( ) :
 O0oOoOOOoOO = ii1ii11IIIiiI ( oOOoo00O0O ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9jb21wbGV0ZV9saXN0Lmh0bQ==' ) )
 O00OOOoOoo0O = re . compile ( '<td width=".+?">.*?<b>.+?<a href="(.*?)">(.*?)</a></b></td>' , re . DOTALL ) . findall ( O0oOoOOOoOO )
 for o0ooooO0o0O , ii11IIII11I in O00OOOoOoo0O :
  if '</a>' in ii11IIII11I :
   pass
  elif '(' in ii11IIII11I :
   O00O0OO00oo ( ( ii11IIII11I ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , oOOoo00O0O ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + o0ooooO0o0O , 30005 , i1iIIi1 + 'kodible.png' , i1iIIi1 + 'kodible.png' , '' )
  else :
   Ii11iII1 ( ( ii11IIII11I ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , oOOoo00O0O ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + o0ooooO0o0O , 30004 , i1iIIi1 + 'kodible.png' , i1iIIi1 + 'kodible.png' , '' )
   if 15 - 15: I1IiI
 xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 62 - 62: i1Iii
 if 51 - 51: I1IiI
def I11IIIiIi11 ( url ) :
 O0oOoOOOoOO = ii1ii11IIIiiI ( url )
 O00OOOoOoo0O = re . compile ( '<a href="(.+?)">Download</a></b></td>' ) . findall ( O0oOoOOOoOO )
 for url in O00OOOoOoo0O :
  oO00oooOOoOo0 = ( oOOoo00O0O ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) ) + url
  Resolve ( oO00oooOOoOo0 )
  if 39 - 39: i1Iii % O0 % I1IiI . i1IIi
def oOo00OooO0oO ( url ) :
 O0oOoOOOoOO = ii1ii11IIIiiI ( url )
 O00OOOoOoo0O = re . compile ( '<td width="247">(.*?)</td>.*?<a href="(.+?)">' , re . DOTALL ) . findall ( O0oOoOOOoOO )
 for ii11IIII11I , url in O00OOOoOoo0O :
  if '<p align' in ii11IIII11I :
   pass
  elif '&nbsp;' in ii11IIII11I :
   pass
  else :
   Ii11iII1 ( ( ii11IIII11I ) . replace ( '&nbsp;' , '' ) , oOOoo00O0O ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) + url , 10012 , i1iIIi1 + 'kodible.png' , i1iIIi1 + 'kodible.png' , '' )
   if 16 - 16: I1I1ii / Oo + iiiiiIIii / i1Iii
 xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 42 - 42: Oo + OoOoOO00 - OOOo0 / o00OO0OOO0 % I1I1ii
 if 66 - 66: iiiiiIIii + i1IIi . OOOo0 + iiiiiIIii - o00OO0OOO0
def Ii ( ) :
 O0oOoOOOoOO = cloudflare . source ( oOOoo00O0O ( 'aHR0cDovL3dhdGNoY2FydG9vbnNvbmxpbmUuZXUv' ) )
 O00OOOoOoo0O = re . compile ( 'class="menu-item menu-item-type-.+?><a href="([^"]*)">(.+?)</a></li>' , re . DOTALL ) . findall ( O0oOoOOOoOO )
 for o0ooooO0o0O , ii11IIII11I in O00OOOoOoo0O :
  if 'ongoing' in o0ooooO0o0O :
   Ii11iII1 ( '[COLORgreen]' + ii11IIII11I + '[/COLOR]' , o0ooooO0o0O , 21005 , i1iIIi1 + 'on-going.png' , '' , '' )
  if 'cartoon-series' in o0ooooO0o0O :
   Ii11iII1 ( '[COLORgreen]' + ii11IIII11I + '[/COLOR]' , o0ooooO0o0O , 21005 , i1iIIi1 + 'cartoonseries.png' , '' , '' )
  if 'disney' in o0ooooO0o0O :
   Ii11iII1 ( '[COLORgreen]' + ii11IIII11I + '[/COLOR]' , o0ooooO0o0O , 21005 , i1iIIi1 + 'disneytoons.png' , '' , '' )
  if 'genre' in o0ooooO0o0O :
   Ii11iII1 ( '[COLORgreen]' + ii11IIII11I + '[/COLOR]' , o0ooooO0o0O , 21005 , i1iIIi1 + 'cartoongenre.png' , '' , '' )
  if 'years' in o0ooooO0o0O :
   Ii11iII1 ( '[COLORgreen]' + ii11IIII11I + '[/COLOR]' , o0ooooO0o0O , 21005 , i1iIIi1 + 'years.png' , '' , '' )
def IiiiiI1 ( url ) :
 O0oOoOOOoOO = cloudflare . source ( url )
 O00OOOoOoo0O = re . compile ( '<a href="([^"]*)" title="([^"]*)" rel="nofollow" id="featured-thumbnail">.+?<div class="featured-thumbnail"><img width="140" height="200" src="([^"]*)"' , re . DOTALL ) . findall ( O0oOoOOOoOO )
 OO00OOoO0o = re . compile ( '<button type="button"><a href="([^"]*)" target="_blank">(.+?)</a>' ) . findall ( O0oOoOOOoOO )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' ) . findall ( O0oOoOOOoOO )
 for url , ii11IIII11I , i1111I1I in O00OOOoOoo0O :
  Ii11iII1 ( '[COLORgreen]' + ii11IIII11I + '[/COLOR]' , url , 21006 , i1111I1I , i1111I1I , ii11IIII11I )
 for url , ii11IIII11I in OO00OOoO0o :
  Ii11iII1 ( '[COLORgreen]' + ii11IIII11I + '[/COLOR]' , url , 21005 , i1iIIi1 + 'watchcartoons.png' , '' , '' )
 for url in next :
  Ii11iII1 ( '[COLORgreen]NEXT[/COLOR]' , url , 21005 , i1iIIi1 + 'Next.png' , '' , '' )
def Iiiiiii1 ( url ) :
 O0oOoOOOoOO = cloudflare . source ( url )
 O00OOOoOoo0O = re . compile ( '<li><a href="([^"]*)" >(.+?)</a></li>' , re . DOTALL ) . findall ( O0oOoOOOoOO )
 oOO0oo = re . compile ( 'file:"([^"]*)",type:"mp4",label:"([^"]*)"' , re . DOTALL ) . findall ( O0oOoOOOoOO )
 II1iIi1IiIii = re . compile ( 'src="([^"]*)" frameborder=' ) . findall ( O0oOoOOOoOO )
 I111I11I111 = re . compile ( '<iframe src="([^"]*)"' ) . findall ( O0oOoOOOoOO )
 for url , ii11IIII11I in O00OOOoOoo0O :
  Ii11iII1 ( '[COLORgreen]' + ii11IIII11I + '[/COLOR]' , url , 21007 , i1iIIi1 + 'watchcartoons.png' , '' , '' )
 for url in II1iIi1IiIii :
  Ii11iII1 ( '[COLORgreen]PLAY[/COLOR]' , 'http:' + url , 222 , i1iIIi1 + 'watchcartoons.png' , '' , '' )
 for url , ii11IIII11I in oOO0oo :
  IIiII ( '[COLORgreen]' + ii11IIII11I + '[/COLOR]' , url , 222 , i1iIIi1 + 'watchcartoons.png' , '' , '' )
 else :
  Ii11iII1 ( '[COLORgreen]NO STREAMS AVAILABLE[/COLOR]' , url , 21005 , i1iIIi1 + 'watchcartoons.png' , '' , '' )
def iiiiI11ii ( url ) :
 O0oOoOOOoOO = cloudflare . source ( url )
 O00OOOoOoo0O = re . compile ( 'file:"([^"]*)",type:"mp4",label:"([^"]*)"' , re . DOTALL ) . findall ( O0oOoOOOoOO )
 for url , ii11IIII11I in O00OOOoOoo0O :
  IIiII ( '[COLORgreen]' + ii11IIII11I + '[/COLOR]' , url , 222 , i1iIIi1 + 'watchcartoons.png' , '' , '' )
  if 96 - 96: OOOooOooo00O0 . O0 / OOOooOooo00O0 % O0
def o0o000 ( ) :
 oOo00 ( '[COLORgreen]CARTOONS[/COLOR]' , '' , 20001 , i1iIIi1 + 'ORIGINCARTOON.png' )
 oOo00 ( '[COLORgreen]ANIME[/COLOR]' , 'https://kissanime.to/AnimeList' , 20001 , i1iIIi1 + 'ORIGINCARTOON.png' )
 if 50 - 50: I1I1ii % i1IIi
def iii11II1I ( ) :
 oOo00 ( '[COLORgreen]BY NAME[/COLOR]' , 'http://kisscartoon.me/CartoonList' , 20002 , i1iIIi1 + 'ORIGINCARTOON.png' )
 oOo00 ( '[COLORgreen]BY GENRE[/COLOR]' , 'http://kisscartoon.me/CartoonList' , 20003 , i1iIIi1 + 'ORIGINCARTOON.png' )
 if 5 - 5: I1IiI - I1I1ii * I1I1ii
def IiiIi1IIII1i ( url ) :
 O0oOoOOOoOO = cloudflare . source ( url )
 O00OOOoOoo0O = re . compile ( 'href="(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( O0oOoOOOoOO )
 for url , ii11IIII11I in O00OOOoOoo0O :
  if '?c=' in url :
   oOo00 ( '[COLORgreen]' + ii11IIII11I + '[/COLOR]' , 'http://kisscartoon.me' + url , 20004 , i1iIIi1 + 'ORIGINCARTOON.png' )
   if 98 - 98: iiiiiIIii + i1IIi . OOOo0 - OoOoOO00 - OOooOOo
def iIIi1I1ii ( url ) :
 O0oOoOOOoOO = cloudflare . source ( url )
 O00OOOoOoo0O = re . compile ( 'href="(.+?)" title="(.+?)">/n(.+?)</a><br/>' , re . DOTALL ) . findall ( O0oOoOOOoOO )
 for url , Iiii , ii11IIII11I in O00OOOoOoo0O :
  if 'Genre' in url :
   oOo00 ( '[COLORgreen]' + ii11IIII11I + '[/COLOR]' , 'http://kisscartoon.me' + url , 20004 , i1iIIi1 + 'ORIGINCARTOON.png' )
   if 44 - 44: oo0Oo . OOOooOooo00O0 . OoooooooOO
def II11iIII1i1I ( url ) :
 O0oOoOOOoOO = cloudflare . source ( url )
 O00OOOoOoo0O = re . compile ( 'src="(.+?)" style=.+?<a class="bigChar" href="(.+?)">(.+?)</a>.+?<p>(.+?)</p>' , re . DOTALL ) . findall ( O0oOoOOOoOO )
 for url , Iiii , ii11IIII11I in O00OOOoOoo0O :
  Ii11iII1 ( '[COLORgreen]' + ii11IIII11I + '[/COLOR]' , 'http://kisscartoon.me' + url , 20005 , img , '' , Iiii )
  if 63 - 63: Oo + oOO - OoOoOO00
def i1iIIi1I1I11 ( url ) :
 O0oOoOOOoOO = cloudflare . source ( url )
 O00OOOoOoo0O = re . compile ( '<img width="120" height="165" src="(.+?)" style=.+?<a class="bigChar" href="(.+?)">(.+?)</a>.+?<p>(.+?)</p>' , re . DOTALL ) . findall ( O0oOoOOOoOO )
 for url , Iiii , ii11IIII11I in O00OOOoOoo0O :
  Ii11iII1 ( '[COLORgreen]' + ii11IIII11I + '[/COLOR]' , 'http://kisscartoon.me' + url , 20005 , img , '' , Iiii )
  if 39 - 39: iIii1I11I1II1 - OoooooooOO
  if 81 - 81: ii11ii1ii - O0 * OoooooooOO
  if 23 - 23: OoOoOO00 / o00oOO0
  if 28 - 28: Oo * oo0Oo - Ooo00oOo00o
  if 19 - 19: o00OO0OOO0
def Ooooo0OoO0 ( ) :
 if 9 - 9: iiiiiIIii . I1I1ii
 Ii11iII1 ( '[COLORgreen]Cartoons[/COLOR]' , oOOoo00O0O ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2NhcnRvb24=' ) , 10004 , i1iIIi1 + 'ORIGINCARTOON.png' , oooOOOOO , '' )
 Ii11iII1 ( '[COLORgreen]Search Cartoons[/COLOR]' , '' , 10005 , i1iIIi1 + 'ORIGINCARTOON.png' , oooOOOOO , '' )
 if 31 - 31: o00oOO0 / iIii1I11I1II1
def o0oO0OoO0 ( ) :
 Iii1I1I11iiI1 = i1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 ii1I = Iii1I1I11iiI1 . lower ( )
 O0oOoOOOoOO = ii1ii11IIIiiI ( oOOoo00O0O ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2NhcnRvb24=' ) )
 O00OOOoOoo0O = re . compile ( '<td><a href="(.+?)">(.+)</a></td>' ) . findall ( O0oOoOOOoOO )
 for o0ooooO0o0O , ii11IIII11I in O00OOOoOoo0O :
  if Iii1I1I11iiI1 in ii11IIII11I . lower ( ) :
   if 'Dad!' in ii11IIII11I :
    pass
   elif 'Family Guy' in ii11IIII11I :
    pass
   elif '2 Stupid' in ii11IIII11I :
    pass
   elif 'The Zelfs' in ii11IIII11I :
    pass
   elif 'A Clone' in ii11IIII11I :
    pass
   elif 'A.T.O.M' in ii11IIII11I :
    pass
   elif 'Almost Naked' in ii11IIII11I :
    pass
   elif 'Angry Kid' in ii11IIII11I :
    pass
   elif 'Annoying Orange' in ii11IIII11I :
    pass
   elif 'Aqua Teen' in ii11IIII11I :
    pass
   elif 'Assy Mcgee' in ii11IIII11I :
    pass
   elif 'Astroblast' in ii11IIII11I :
    pass
   elif 'Atomic Betty' in ii11IIII11I :
    pass
   elif 'Axe Cop' in ii11IIII11I :
    pass
   elif 'Baby Playpen' in ii11IIII11I :
    pass
   elif 'Beavis and Butt' in ii11IIII11I :
    pass
   elif 'Celebrity Deathmatch' in ii11IIII11I :
    pass
   elif 'Clerks The' in ii11IIII11I :
    pass
   elif 'Crapston Villas' in ii11IIII11I :
    pass
   elif 'Duckman:' in ii11IIII11I :
    pass
   elif 'Stripperella' in ii11IIII11I :
    pass
   elif 'Vixen' in ii11IIII11I :
    pass
   else :
    Ii11iII1 ( '[COLORgreen]' + ii11IIII11I + '[/COLOR]' , o0ooooO0o0O , 10006 , i1iIIi1 + 'ORIGINCARTOON.png' , oooOOOOO , '' )
  xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 70 - 70: o00oOO0 - o00oOO0
def OoOO0OOoo ( url ) :
 oOOooOoo = ii1ii11IIIiiI ( url )
 O00OOOoOoo0O = re . compile ( '<td><a href="(.+?)">(.+)</a></td>' ) . findall ( oOOooOoo )
 for url , ii11IIII11I in O00OOOoOoo0O :
  if 'Dad!' in ii11IIII11I :
   pass
  elif 'Family Guy' in ii11IIII11I :
   pass
  elif '2 Stupid' in ii11IIII11I :
   pass
  elif 'The Zelfs' in ii11IIII11I :
   pass
  elif 'A Clone' in ii11IIII11I :
   pass
  elif 'A.T.O.M' in ii11IIII11I :
   pass
  elif 'Almost Naked' in ii11IIII11I :
   pass
  elif 'Angry Kid' in ii11IIII11I :
   pass
  elif 'Annoying Orange' in ii11IIII11I :
   pass
  elif 'Aqua Teen' in ii11IIII11I :
   pass
  elif 'Assy Mcgee' in ii11IIII11I :
   pass
  elif 'Astroblast' in ii11IIII11I :
   pass
  elif 'Atomic Betty' in ii11IIII11I :
   pass
  elif 'Axe Cop' in ii11IIII11I :
   pass
  elif 'Baby Playpen' in ii11IIII11I :
   pass
  elif 'Beavis and Butt' in ii11IIII11I :
   pass
  elif 'Celebrity Deathmatch' in ii11IIII11I :
   pass
  elif 'Clerks The' in ii11IIII11I :
   pass
  elif 'Crapston Villas' in ii11IIII11I :
   pass
  elif 'Duckman:' in ii11IIII11I :
   pass
  elif 'Stripperella' in ii11IIII11I :
   pass
  elif 'Vixen' in ii11IIII11I :
   pass
  else :
   Ii11iII1 ( '[COLORgreen]' + ii11IIII11I + '[/COLOR]' , url , 10006 , i1iIIi1 + 'ORIGINCARTOON.png' , oooOOOOO , '' )
 xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 1 - 1: OOOo0 * i11iIiiIii + oOO * i11iIiiIii + Ooo00oOo00o
def iI ( url ) :
 oOOooOoo = ii1ii11IIIiiI ( url )
 I1i = re . compile ( '<img src="(.+?)" id="series_image" width="250" height="370" alt=".+?" />' ) . findall ( oOOooOoo )
 for i1111I1I in I1i :
  Ii1IIi = i1111I1I
 i111i11I1ii = re . compile ( '<li><a href="(.+?)">Next</a></li>' ) . findall ( oOOooOoo )
 for url in i111i11I1ii :
  Ii11iII1 ( '[COLORgreen]NEXT PAGE[/COLOR]' , url , 10006 , i1iIIi1 + 'Next.png' , oooOOOOO , '' )
 O00OOOoOoo0O = re . compile ( '&nbsp;<a href="(.+?)">(.+?)</a>' ) . findall ( oOOooOoo )
 for url , ii11IIII11I in O00OOOoOoo0O :
  O0000 ( '[COLORgreen]' + ii11IIII11I + '[/COLOR]' , url , 10007 , Ii1IIi )
  if 64 - 64: o00oOO0 / i11iIiiIii / OOooOOo . OoooooooOO
  if 11 - 11: o00OO0OOO0 % i1IIi
 xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 16 - 16: OOOo0 + oo0Oo % I1IiI
def o0o0oOo000o0 ( url , IMAGE ) :
 oOOooOoo = ii1ii11IIIiiI ( url )
 O00OOOoOoo0O = re . compile ( '"playlist">(.+?)</span></div><div><iframe src="(.+?)"' ) . findall ( oOOooOoo )
 for ii11IIII11I , url in O00OOOoOoo0O :
  print ii11IIII11I + '     ' + url
  if 'easy' in url :
   I1iI1I1 ( url )
   if 48 - 48: OOOo0 / i11iIiiIii - OOooOOo * o00oOO0 / OoooooooOO
   if 89 - 89: iIii1I11I1II1 / OOOo0 - OoOoOO00 / i1Iii . i11iIiiIii . i1Iii
  xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 48 - 48: O0 + O0 . oOO - oo0Oo
def I1iI1I1 ( url ) :
 oOOooOoo = ii1ii11IIIiiI ( url )
 O00OOOoOoo0O = re . compile ( "url: '(.+?)'," ) . findall ( oOOooOoo )
 for url in O00OOOoOoo0O :
  o00oo0000 ( url )
  if 44 - 44: Oo % iIii1I11I1II1
  if 90 - 90: OoOoOO00 + OoooooooOO % OoooooooOO
  if 35 - 35: OOOooOooo00O0 / ii11ii1ii * OoooooooOO . OoOoOO00 / Oo
def Iii11i ( ) :
 if 73 - 73: Oo - I1IiI - o00oOO0 - OOOo0
 Ii11iII1 ( '[COLORgreen]Stand Up[/COLOR]' , '' , 10014 , i1iIIi1 + 'ORIGINSTANDUP.png' , oooOOOOO , '' )
 Ii11iII1 ( '[COLORgreen]Search Comedian[/COLOR]' , '' , 10015 , i1iIIi1 + 'ORIGINSTANDUP.png' , oooOOOOO , '' )
 Ii11iII1 ( '[COLORgreen]Others[/COLOR]' , '' , 10017 , i1iIIi1 + 'ORIGINSTANDUP.png' , oooOOOOO , '' )
 if 65 - 65: OOooOOo
def I1ii1II1iII ( ) :
 O0oOoOOOoOO = ii1ii11IIIiiI ( ( oOOoo00O0O ( 'aHR0cDovL2JhY2syYmFzaWNzYnVpbGQuY28udWsvdGVzdC9zdGFuZHVwbGlzdC5waHA=' ) ) )
 O00OOOoOoo0O = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( O0oOoOOOoOO )
 for o0ooooO0o0O , i1111I1I , ii11IIII11I in O00OOOoOoo0O :
  if 'elete' in ii11IIII11I :
   pass
  else :
   O0000 ( '[COLORgreen]' + ii11IIII11I + '[/COLOR]' , o0ooooO0o0O , 222 , i1111I1I )
   if 8 - 8: I1IiI / O0 * O0 % oOO - Oo + o00OO0OOO0
def ooIi1IiIiIi1IiI ( ) :
 Iii1I1I11iiI1 = i1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 ii1I = Iii1I1I11iiI1 . lower ( )
 O0oOoOOOoOO = ii1ii11IIIiiI ( ( oOOoo00O0O ( 'aHR0cDovL3d3dy5jb3VjaHRyaXBwZXIuY29tL2ZvcnVtMi9wYWdlLnBocD9wYWdlPTM=' ) ) )
 i1iiIIi1I = re . compile ( '<tr>.+?<td width=".+?" align=".+?">.+?<img border=".+?" src="..(.+?)" width=".+?" height=".+?"></td>.+?<td width=".+?" valign=".+?" align=".+?"><font size=".+?">(.+?)</font></td>.+?<td width=".+?">(.+?)</td>' , re . DOTALL ) . findall ( O0oOoOOOoOO )
 for i1111I1I , iiI1I1IIi11i1 , iIiiiI1IiI1I1 in i1iiIIi1I :
  for Iii1I1I11iiI1 in iiI1I1IIi11i1 :
   print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< img >>>>>>>>>>>>>>>>>>>>>>>>>>'
   i1II1iii1i = re . compile ( '<a href="(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( iIiiiI1IiI1I1 )
   for o0ooooO0o0O , ii11IIII11I in i1II1iii1i :
    if 'tube' in o0ooooO0o0O :
     pass
    elif 'stage' in o0ooooO0o0O :
     O0000 ( '[COLORgreen]' + iiI1I1IIi11i1 + '   -   ' + ii11IIII11I + '[/COLOR]' , ( o0ooooO0o0O ) . replace ( '" target="_blank' , '' ) , 10016 , 'http://couchtripper.com/' + i1111I1I , )
    elif 'vee' in o0ooooO0o0O :
     pass
     if 83 - 83: ii11ii1ii / oOO - i11iIiiIii . iIii1I11I1II1 + Oo
def ooO0000o00O ( ) :
 O0oOoOOOoOO = ii1ii11IIIiiI ( ( oOOoo00O0O ( 'aHR0cDovL3d3dy5jb3VjaHRyaXBwZXIuY29tL2ZvcnVtMi9wYWdlLnBocD9wYWdlPTM=' ) ) )
 i1iiIIi1I = re . compile ( '<tr>.+?<td width=".+?" align=".+?">.+?<img border=".+?" src="..(.+?)" width=".+?" height=".+?"></td>.+?<td width=".+?" valign=".+?" align=".+?"><font size=".+?">(.+?)</font></td>.+?<td width=".+?">(.+?)</td>' , re . DOTALL ) . findall ( O0oOoOOOoOO )
 for i1111I1I , iiI1I1IIi11i1 , iIiiiI1IiI1I1 in i1iiIIi1I :
  i1II1iii1i = re . compile ( '<a href="(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( iIiiiI1IiI1I1 )
  for o0ooooO0o0O , ii11IIII11I in i1II1iii1i :
   if 'tube' in o0ooooO0o0O :
    pass
   elif 'stage' in o0ooooO0o0O :
    O0000 ( '[COLORgreen]' + iiI1I1IIi11i1 + '   -   ' + ii11IIII11I + '[/COLOR]' , ( o0ooooO0o0O ) . replace ( '" target="_blank' , '' ) , 10016 , 'http://couchtripper.com/' + i1111I1I )
   elif 'vee' in o0ooooO0o0O :
    pass
    if 91 - 91: o00OO0OOO0 / O0 - i1Iii . OOOo0
    if 82 - 82: I1I1ii * iiiiiIIii / o00oOO0
 xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 2 - 2: OOOo0 + OOooOOo . OOooOOo . O0 / o00OO0OOO0
def iIiiIiiIi ( url ) :
 O0oOoOOOoOO = ii1ii11IIIiiI ( url )
 print '>>>>>>>>>>>>>>>>>>>>>>>>' + url + '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'
 O00Oooo = re . compile ( "url\[.+?\] = '(.+?)';" ) . findall ( O0oOoOOOoOO )
 print '>>>>>>>>>>>>>>>>>>>>>>>' + ( str ( O00Oooo ) ) + '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
 for url in O00Oooo :
  o00oo0000 ( ( url ) . replace ( '[' , '' ) . replace ( ']' , '' ) . replace ( '\'' , '' ) )
  if 40 - 40: OOooOOo
  if 78 - 78: iIii1I11I1II1
  if 56 - 56: OoooooooOO - o00OO0OOO0 - i1IIi
  if 8 - 8: oOO / iiiiiIIii . OOOo0 + ii11ii1ii / i11iIiiIii
  if 31 - 31: oo0Oo - iIii1I11I1II1 + OOOooOooo00O0 . Oo / I1I1ii % iIii1I11I1II1
  if 6 - 6: I1I1ii * i11iIiiIii % iIii1I11I1II1 % i11iIiiIii + OOooOOo / i1IIi
  if 53 - 53: o00OO0OOO0 + iIii1I11I1II1
def oOooo0Oo ( ) :
 if 66 - 66: Oo
 I1i1IiI1i ( '[COLOR darkgoldenrod]Open Pandora\'s Box[/COLOR]' , '' , 10029 , 'https://encrypted-tbn1.gstatic.com/images?q=tbn%3AANd9GcTQ9r4TA8yIw9ggxuwsHxWojo6tPVfgTe8QIOxOQwzNR2TavtCi6Q' , oooOOOOO , '' )
 I1i1IiI1i ( '[COLOR darkgoldenrod]Search[/COLOR]' , '' , 10026 , 'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png' , oooOOOOO , '' )
 if 32 - 32: OoooooooOO - I1IiI - i11iIiiIii * OOooOOo / Oo + OoooooooOO
 I1IiII11III ( 'movies' , 'MAIN' )
 if 35 - 35: i1IIi - OOooOOo * OOOooOooo00O0
def O0oOoo0OoO0O ( ) :
 I1i1IiI1i ( 'Search Pandoras Films' , '' , 10027 , i1iIIi1 + 'PANDORASBOX.png' , oooOOOOO , '' )
 I1i1IiI1i ( 'Search Pandoras TV' , '' , 10028 , i1iIIi1 + 'PANDORASBOX.png' , oooOOOOO , '' )
 if 63 - 63: OoooooooOO / oo0Oo
 I1IiII11III ( 'movies' , 'MAIN' )
def oooO00o0 ( ) :
 if 53 - 53: oo0Oo
 Iii1I1I11iiI1 = i1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 ii1I = Iii1I1I11iiI1 . lower ( )
 o0oO0oo0000OO = [ 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' ]
 if 45 - 45: oOO * i1Iii / OoooooooOO . o00oOO0 % ii11ii1ii / i1IIi
 for I1III1 in o0oO0oo0000OO :
  Iiii1ii = I11II1i + I1III1 + OooO0
  O0oOoOOOoOO = ii1ii11IIIiiI ( Iiii1ii )
  O00OOOoOoo0O = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( O0oOoOOOoOO )
  for o0ooooO0o0O , o0OoOo00o0o , O0oO0iII11 , I1II1I11I1I , ii11IIII11I in O00OOOoOoo0O :
   if Iii1I1I11iiI1 in ii11IIII11I . lower ( ) :
    I1i111IiIiIi1 ( ii11IIII11I , o0ooooO0o0O , 222 , o0OoOo00o0o , I1II1I11I1I , O0oO0iII11 )
    if 39 - 39: o00OO0OOO0 - ii11ii1ii
    I1IiII11III ( 'movies' , 'MAIN' )
    xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
    if 53 - 53: OOooOOo % OOOooOooo00O0 + oo0Oo . Oo - ii11ii1ii % OOooOOo
    if 64 - 64: OoOoOO00
def iIIIiIi1I1i ( ) :
 if 78 - 78: iIii1I11I1II1 % I1IiI + ii11ii1ii / i1IIi % OoOoOO00 + iiiiiIIii
 Iii1I1I11iiI1 = i1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 ii1I = Iii1I1I11iiI1 . lower ( )
 o0oO0oo0000OO = [ 'a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' , 'p' , 'q' , 'r' , 's' , 't' , 'u' , 'v' , 'w' , 'x' , 'y' , 'z' ]
 if 91 - 91: iIii1I11I1II1 % Ooo00oOo00o . OOooOOo + i1Iii + OOooOOo
 for I1III1 in o0oO0oo0000OO :
  o00OOo = I11II1i + I1III1 + OooO0
  O0oOoOOOoOO = ii1ii11IIIiiI ( o00OOo )
  O00OOOoOoo0O = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( O0oOoOOOoOO )
  for ii11IIII11I , O0oO0iII11 , o0ooooO0o0O , i1111I1I , I1II1I11I1I , oOo0OOoooO in O00OOOoOoo0O :
   if Iii1I1I11iiI1 in ii11IIII11I . lower ( ) :
    I1i1IiI1i ( ii11IIII11I , o0ooooO0o0O , oOo0OOoooO , i1111I1I , I1II1I11I1I , O0oO0iII11 )
    if 26 - 26: OOooOOo * I1I1ii . i1IIi
    I1IiII11III ( 'movies' , 'MAIN' )
    xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
    if 59 - 59: O0 + i1IIi - OOooOOo
    if 62 - 62: i11iIiiIii % iiiiiIIii . I1I1ii . iiiiiIIii
def ooOo0O0O0oOO0 ( ) :
 if 10 - 10: Oo + O0
 oOOooOoo = ii1ii11IIIiiI ( oOOoo00O0O ( 'aHR0cDovL3NlZWR1cmdyZWVkLngxMGhvc3QuY29tL29yaWdpbi9zcG9uZ2VtYWluLnBocA==' ) )
 O00OOOoOoo0O = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( oOOooOoo )
 for ii11IIII11I , O0oO0iII11 , o0ooooO0o0O , i1111I1I , I1II1I11I1I , oOo0OOoooO in O00OOOoOoo0O :
  I1i1IiI1i ( ii11IIII11I , o0ooooO0o0O , oOo0OOoooO , i1111I1I , I1II1I11I1I , O0oO0iII11 )
  I1IiII11III ( 'movies' , 'MAIN' )
def Ii1iI ( url ) :
 if 53 - 53: iIii1I11I1II1 - o00oOO0 % I1IiI * oOO % oo0Oo
 xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
 II1Ii = ( '%s%s' % ( OOoO00ooO , url ) )
 i11iiI1111 = ii1ii11IIIiiI ( url )
 O00OOOoOoo0O = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( i11iiI1111 )
 for url , o0OoOo00o0o , O0oO0iII11 , I1IIIIiii1i , ii11IIII11I in O00OOOoOoo0O :
  I1i111IiIiIi1 ( ii11IIII11I , url , 222 , o0OoOo00o0o , I1IIIIiii1i , O0oO0iII11 )
  if 51 - 51: iiiiiIIii . OOOo0
  I1IiII11III ( 'movies' , 'MAIN' )
  if 73 - 73: OoooooooOO . OOOo0 / oOO % i1Iii
  xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 65 - 65: I1I1ii - OOOo0 - i1Iii
  if 42 - 42: OoOoOO00 * OOOo0 % i1IIi - i1Iii % I1I1ii
def Ii1I1 ( url ) :
 if 58 - 58: I1I1ii - o00OO0OOO0 % OOOo0
 oOOooOoo = ii1ii11IIIiiI ( url )
 O00OOOoOoo0O = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( oOOooOoo )
 for ii11IIII11I , O0oO0iII11 , url , i1111I1I , I1II1I11I1I , oOo0OOoooO in O00OOOoOoo0O :
  I1i1IiI1i ( ii11IIII11I , url , oOo0OOoooO , i1111I1I , I1II1I11I1I , O0oO0iII11 )
  if 4 - 4: i1IIi + oo0Oo + i1IIi
  I1IiII11III ( 'movies' , 'MAIN' )
  if 31 - 31: i1Iii
  if 78 - 78: i11iIiiIii + OOooOOo + oOO / OOooOOo % iIii1I11I1II1 % I1I1ii
 xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 83 - 83: iIii1I11I1II1 % I1IiI % OOooOOo % oOO . ii11ii1ii % O0
def I1i111IiIiIi1 ( name , url , mode , iconimage , fanart , description ) :
 if 47 - 47: OOooOOo
 oo0ooooO = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 iiIIi = True
 i1i = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 i1i . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 i1i . setProperty ( "Fanart_Image" , fanart )
 iiIIi = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = oo0ooooO , listitem = i1i , isFolder = False )
 return iiIIi
 if 25 - 25: o00oOO0
def I1i1IiI1i ( name , url , mode , iconimage , fanart , description ) :
 if 34 - 34: I1IiI . iIii1I11I1II1 % O0
 oo0ooooO = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 iiIIi = True
 i1i = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 i1i . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 i1i . setProperty ( "Fanart_Image" , fanart )
 iiIIi = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = oo0ooooO , listitem = i1i , isFolder = True )
 return iiIIi
if 43 - 43: ii11ii1ii - OOOooOooo00O0
if 70 - 70: OOOooOooo00O0 / iiiiiIIii % oo0Oo - i1Iii
if 47 - 47: OOOooOooo00O0
if 92 - 92: iiiiiIIii + I1IiI % i1IIi
if 23 - 23: oOO - iiiiiIIii + i1Iii - I1IiI * I1IiI . Oo
if 47 - 47: o00oOO0 % iIii1I11I1II1
if 11 - 11: OOOo0 % i1Iii - Ooo00oOo00o - o00oOO0 + OOooOOo
if 98 - 98: OOOooOooo00O0 + i1Iii - Ooo00oOo00o
if 79 - 79: iiiiiIIii / oOO . I1IiI - ii11ii1ii
if 47 - 47: OoooooooOO % O0 * OOOooOooo00O0 . i1Iii
if 38 - 38: O0 - I1I1ii % oOO
if 64 - 64: iIii1I11I1II1
if 15 - 15: ii11ii1ii + iiiiiIIii / ii11ii1ii / oOO
if 31 - 31: oo0Oo + O0 + oo0Oo . iIii1I11I1II1 + Oo / OOooOOo
if 6 - 6: Oo % I1I1ii * o00OO0OOO0 / OOOo0 + Oo
def IIiI11i11 ( string ) :
 if oOoOooOo0o0 == 'true' :
  xbmc . log ( "[addon.live.GenieTV-%s]: %s" % ( addon_version , string ) )
  if 14 - 14: i11iIiiIii
def o0oOOO0 ( name , url , iconimage , fanart , mode , playlist = None , regexs = None ) :
 oOOO = [ ]
 try :
  if 36 - 36: ii11ii1ii - OOOooOooo00O0
  name = name . encode ( 'utf-8' , 'ignore' )
 except :
  pass
 if os . path . exists ( I11i1 ) == False :
  IIiI11i11 ( 'Making Favorites File' )
  oOOO . append ( ( name , url , iconimage , fanart , mode , playlist , regexs ) )
  Iiii1iI1i = open ( I11i1 , "w" )
  Iiii1iI1i . write ( json . dumps ( oOOO ) )
  Iiii1iI1i . close ( )
 else :
  IIiI11i11 ( 'Appending Favorites' )
  Iiii1iI1i = open ( I11i1 ) . read ( )
  III1I1 = json . loads ( Iiii1iI1i )
  III1I1 . append ( ( name , url , iconimage , fanart , mode ) )
  i1iI11I1II1 = open ( I11i1 , "w" )
  i1iI11I1II1 . write ( json . dumps ( III1I1 ) )
  i1iI11I1II1 . close ( )
  if 12 - 12: iIii1I11I1II1 % oo0Oo % oo0Oo
  if 78 - 78: I1I1ii . I1IiI . o00OO0OOO0
def o0ooO0OOO ( ) :
 o0oo000OoOoo0 = json . loads ( open ( I11i1 ) . read ( ) )
 OoO0o = len ( o0oo000OoOoo0 )
 for iiiiIiI1i1I1 in o0oo000OoOoo0 :
  ii11IIII11I = iiiiIiI1i1I1 [ 0 ]
  o0ooooO0o0O = iiiiIiI1i1I1 [ 1 ]
  o0OoOo00o0o = iiiiIiI1i1I1 [ 2 ]
  try :
   oo0 = iiiiIiI1i1I1 [ 3 ]
   if oo0 == None :
    raise
  except :
   if iiIIIII1i1iI . getSetting ( 'use_thumb' ) == "true" :
    oo0 = o0OoOo00o0o
   else :
    oo0 = I1II1I11I1I
  try : i1iIIi1II1iiI = iiiiIiI1i1I1 [ 5 ]
  except : i1iIIi1II1iiI = None
  try : III1Ii1i1I1 = iiiiIiI1i1I1 [ 6 ]
  except : III1Ii1i1I1 = None
  if 97 - 97: oOO . oo0Oo - oOO + OOOo0 * OoOoOO00
  if iiiiIiI1i1I1 [ 4 ] == 0 :
   Ii11iII1 ( ii11IIII11I , o0ooooO0o0O , '' , o0OoOo00o0o , I1II1I11I1I , '' , 'fav' )
  else :
   Ii11iII1 ( ii11IIII11I , o0ooooO0o0O , iiiiIiI1i1I1 [ 4 ] , o0OoOo00o0o , I1II1I11I1I , '' , 'fav' )
   if 10 - 10: i1Iii + o00OO0OOO0 % OoooooooOO - OOOo0
def o00oooOo ( name ) :
 III1I1 = json . loads ( open ( I11i1 ) . read ( ) )
 for iiO0O0o0oO0O00 in range ( len ( III1I1 ) ) :
  if III1I1 [ iiO0O0o0oO0O00 ] [ 0 ] == name :
   del III1I1 [ iiO0O0o0oO0O00 ]
   i1iI11I1II1 = open ( I11i1 , "w" )
   i1iI11I1II1 . write ( json . dumps ( III1I1 ) )
   i1iI11I1II1 . close ( )
   break
 xbmc . executebuiltin ( "XBMC.Container.Refresh" )
 if 70 - 70: oOO + o00oOO0
 if 93 - 93: oOO + i1Iii
 if 33 - 33: O0
def oo0oO ( ) :
 if 50 - 50: OoooooooOO - iIii1I11I1II1 + i1IIi % oOO - iIii1I11I1II1 % O0
 Ii11iII1 ( '[COLORgreen]Recent Episodes[/COLOR]' , '' , 10019 , i1iIIi1 + 'dtv.png' , oooOOOOO , '' )
 Ii11iII1 ( '[COLORgreen]Genres[/COLOR]' , '' , 10020 , i1iIIi1 + 'dtv.png' , oooOOOOO , '' )
 Ii11iII1 ( '[COLORgreen]Search[/COLOR]' , '' , 10021 , i1iIIi1 + 'dtv.png' , oooOOOOO , '' )
 if 58 - 58: I1I1ii + iIii1I11I1II1
def Oo00OO0OO ( ) :
 if 85 - 85: OOooOOo % oo0Oo . I1IiI % oOO - Oo
 oOOooOoo = cloudflare . source ( oOOoo00O0O ( 'aHR0cDovL2RpemlsYWIuY29t' ) )
 O00OOOoOoo0O = re . compile ( '<li id=".+?">.+?<a href="(.+?)">.+?<img width="40" height="40" src="(.+?)" alt=""/>.+?<span class="title">\n(.+?)</span>.+?<span class="alt-title">\n(.+?)</span>.+?</a>.+?</li>' , re . DOTALL ) . findall ( oOOooOoo )
 for o0ooooO0o0O , i1111I1I , ii11IIII11I , OOooo in O00OOOoOoo0O :
  Ii11iII1 ( ii11IIII11I + '  -  ' + ( OOooo ) . replace ( 'sezon' , 'Season' ) . replace ( 'bölüm' , 'Episode' ) , o0ooooO0o0O , 10023 , i1iIIi1 + 'dtv.png' , oooOOOOO , '' )
  if 69 - 69: oo0Oo - OOooOOo . oo0Oo
  if 9 - 9: o00oOO0 % i11iIiiIii / Oo
  if 20 - 20: o00oOO0 * O0 + o00OO0OOO0 - OoooooooOO . o00OO0OOO0
def oOII1ii1ii11I1 ( ) :
 if 88 - 88: ii11ii1ii
 Ii11iII1 ( '[COLORgreen]Action[/COLOR]' , 'Aksiyon' , 10024 , i1iIIi1 + 'dtv.png' , oooOOOOO , '' )
 Ii11iII1 ( '[COLORgreen]Adventure[/COLOR]' , 'Macera' , 10024 , i1iIIi1 + 'dtv.png' , oooOOOOO , '' )
 Ii11iII1 ( '[COLORgreen]Animation[/COLOR]' , 'Animasyon' , 10024 , i1iIIi1 + 'dtv.png' , oooOOOOO , '' )
 Ii11iII1 ( '[COLORgreen]Anime[/COLOR]' , 'Anime' , 10024 , i1iIIi1 + 'dtv.png' , oooOOOOO , '' )
 Ii11iII1 ( '[COLORgreen]Biography[/COLOR]' , 'Biyografi' , 10024 , i1iIIi1 + 'dtv.png' , oooOOOOO , '' )
 Ii11iII1 ( '[COLORgreen]Comedy[/COLOR]' , 'Komedi' , 10024 , i1iIIi1 + 'dtv.png' , oooOOOOO , '' )
 Ii11iII1 ( '[COLORgreen]Crime[/COLOR]' , 'Su%C3%A7' , 10024 , i1iIIi1 + 'dtv.png' , oooOOOOO , '' )
 Ii11iII1 ( '[COLORgreen]Documentary[/COLOR]' , 'Belgesel' , 10024 , i1iIIi1 + 'dtv.png' , oooOOOOO , '' )
 Ii11iII1 ( '[COLORgreen]Drama[/COLOR]' , 'Dram' , 10024 , i1iIIi1 + 'dtv.png' , oooOOOOO , '' )
 Ii11iII1 ( '[COLORgreen]Family[/COLOR]' , 'Aile' , 10024 , i1iIIi1 + 'dtv.png' , oooOOOOO , '' )
 Ii11iII1 ( '[COLORgreen]Fantasy[/COLOR]' , 'Fantastik' , 10024 , i1iIIi1 + 'dtv.png' , oooOOOOO , '' )
 Ii11iII1 ( '[COLORgreen]History[/COLOR]' , 'Tarih' , 10024 , i1iIIi1 + 'dtv.png' , oooOOOOO , '' )
 Ii11iII1 ( '[COLORgreen]Horror[/COLOR]' , 'Korku' , 10024 , i1iIIi1 + 'dtv.png' , oooOOOOO , '' )
 Ii11iII1 ( '[COLORgreen]Mini-Series[/COLOR]' , 'Mini%20Dizi' , 10024 , i1iIIi1 + 'dtv.png' , oooOOOOO , '' )
 Ii11iII1 ( '[COLORgreen]Musical[/COLOR]' , 'M%C3%BCzikal' , 10024 , i1iIIi1 + 'dtv.png' , oooOOOOO , '' )
 Ii11iII1 ( '[COLORgreen]Mystery[/COLOR]' , 'Gizem' , 10024 , i1iIIi1 + 'dtv.png' , oooOOOOO , '' )
 Ii11iII1 ( '[COLORgreen]Romance[/COLOR]' , 'Romantik' , 10024 , i1iIIi1 + 'dtv.png' , oooOOOOO , '' )
 Ii11iII1 ( '[COLORgreen]Science Fiction[/COLOR]' , 'Bilim%20Kurgu' , 10024 , i1iIIi1 + 'dtv.png' , oooOOOOO , '' )
 Ii11iII1 ( '[COLORgreen]Sport[/COLOR]' , 'Spor' , 10024 , i1iIIi1 + 'dtv.png' , oooOOOOO , '' )
 Ii11iII1 ( '[COLORgreen]Thriller[/COLOR]' , 'Gerilim' , 10024 , i1iIIi1 + 'dtv.png' , oooOOOOO , '' )
 Ii11iII1 ( '[COLORgreen]War[/COLOR]' , 'Sava%C5%9F' , 10024 , i1iIIi1 + 'dtv.png' , oooOOOOO , '' )
 Ii11iII1 ( '[COLORgreen]Western[/COLOR]' , 'Tarih' , 10024 , i1iIIi1 + 'dtv.png' , oooOOOOO , '' )
 Ii11iII1 ( '[COLORgreen]Youth[/COLOR]' , 'Gen%C3%A7lik' , 10024 , i1iIIi1 + 'dtv.png' , oooOOOOO , '' )
 if 93 - 93: iIii1I11I1II1
def oo0oooo0OoO0o ( url ) :
 oooooo0O000o = 'http://dizilab.com/arsiv?limit=100&tur=' + url + '&orderby=&ulke=&order=&yil=&dizi_adi='
 O0oOoOOOoOO = cloudflare . source ( oooooo0O000o )
 O00OOOoOoo0O = re . compile ( '<div class="tv-series-single">.+?<a href="(.+?)" class="film-image">.+?<img src="(.+?)" alt=""/>.+?<span class="position">.+?</span>\n(.+?)</a>' , re . DOTALL ) . findall ( O0oOoOOOoOO )
 for url , i1111I1I , ii11IIII11I in O00OOOoOoo0O :
  Ii11iII1 ( '[COLORgreen]' + ii11IIII11I + '[/COLOR]' , url , 10022 , i1iIIi1 + 'dtv.png' , oooOOOOO , '' )
  if 50 - 50: OOOooOooo00O0 / OOOooOooo00O0 + iiiiiIIii * oo0Oo / ii11ii1ii
  if 14 - 14: i1Iii % OOOo0 - iIii1I11I1II1 . iiiiiIIii + Ooo00oOo00o - oOO
  if 5 - 5: OOOooOooo00O0
  if 62 - 62: I1IiI . OoooooooOO . iiiiiIIii . Ooo00oOo00o * OOOooOooo00O0
def OOOO ( ) :
 if 94 - 94: OoooooooOO . oo0Oo + i1Iii - OOOo0
 Iii1I1I11iiI1 = i1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 ii1I = Iii1I1I11iiI1 . lower ( )
 o0ooooO0o0O = ( oOOoo00O0O ( 'aHR0cDovL2RpemlsYWIuY29tL2Fyc2l2P2xpbWl0PSZ0dXI9Jm9yZGVyYnk9JnVsa2U9Jm9yZGVyPSZ5aWw9JmRpemlfYWRpPQ==' ) ) + ( Iii1I1I11iiI1 ) . replace ( ' ' , '+' )
 O0oOoOOOoOO = cloudflare . source ( o0ooooO0o0O )
 O00OOOoOoo0O = re . compile ( '<a href="(.+?)" class="film-image">\n<img src="(.+?)" alt=""/>\n</a>\n<div class="tss-detail">\n<a class="title" style="" href=".+?">\n<span class="position">.+?</span>\n(.+?)</a>' ) . findall ( O0oOoOOOoOO )
 for o0ooooO0o0O , i1111I1I , ii11IIII11I in O00OOOoOoo0O :
  if Iii1I1I11iiI1 in ii11IIII11I . lower ( ) :
   Ii11iII1 ( '[COLORgreen]' + ii11IIII11I + '[/COLOR]' , o0ooooO0o0O , 10022 , i1iIIi1 + 'dtv.png' )
   if 1 - 1: OOooOOo . O0
   if 37 - 37: i1IIi - iiiiiIIii % OoooooooOO / iiiiiIIii % oo0Oo
   if 48 - 48: i11iIiiIii % o00oOO0
def i11i11 ( url ) :
 O0oOoOOOoOO = cloudflare . source ( url )
 O00OOOoOoo0O = re . compile ( '<a class="season" href="(.+?)">\n(.+?)\n</a>.+?<a class="episode" href=".+?">\n(.+?)\n</a>.+?<a class="episode-name" href=".+?">\n(.+?)</a>' , re . DOTALL ) . findall ( O0oOoOOOoOO )
 for oO00oooOOoOo0 , Ii11Iii , ooo00OoOO0o , ii11IIII11I in O00OOOoOoo0O :
  oo0O0o = ( ooo00OoOO0o ) . replace ( 'Sezon' , '' ) . replace ( 'bölüm' , '' ) . replace ( 'Bölüm' , '' ) . replace ( 'BÃ¶lÃ¼m' , '' ) . replace ( '.' , '' )
  IioO0O = ( Ii11Iii ) . replace ( 'bölüm' , '' ) . replace ( 'Sezon' , '' ) . replace ( 'Bölüm' , '' ) . replace ( 'BÃ¶lÃ¼m' , '' ) . replace ( '.' , '' )
  Oo00o0O0O = 'Season ' + IioO0O + 'Episode ' + oo0O0o + ii11IIII11I
  o0ooO0OoOo ( Oo00o0O0O , oO00oooOOoOo0 )
  if 99 - 99: I1IiI
  xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 77 - 77: OOooOOo
  if 48 - 48: I1IiI % ii11ii1ii / o00OO0OOO0 . iIii1I11I1II1 * OoOoOO00
def o0ooO0OoOo ( name , url ) :
 oO00oooOOoOo0 = url
 oo000oO = name
 Oo0o00OO0000 = cloudflare . source ( oO00oooOOoOo0 )
 I1i = re . compile ( 'file: "(.+?)",.+?label: "(.+?)",' , re . DOTALL ) . findall ( Oo0o00OO0000 )
 for O00Oooo , O0OOO0 in I1i :
  O0000 ( '[COLORgreen]' + oo000oO + O0OOO0 + '[/COLOR]' , O00Oooo , 10012 , i1iIIi1 + 'dtv.png' )
  if 8 - 8: i11iIiiIii / OoOoOO00 + OOooOOo * i1Iii % I1I1ii . o00OO0OOO0
 xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 6 - 6: I1I1ii % Oo . Oo - ii11ii1ii / o00OO0OOO0 . i1IIi
 if 99 - 99: I1IiI . oOO
def O0oO ( ) :
 if 27 - 27: O0 / I1IiI + iIii1I11I1II1 - iiiiiIIii % OOooOOo
 if 30 - 30: oOO % oOO % I1I1ii . I1IiI
 if 9 - 9: oo0Oo / OoOoOO00 . I1IiI % OOooOOo * OoOoOO00 - oo0Oo
 if 55 - 55: OOOo0
 if 45 - 45: O0 / i1IIi * o00oOO0 * Ooo00oOo00o
 if 35 - 35: ii11ii1ii / OOOooOooo00O0 % OOOo0 + iIii1I11I1II1
 if 79 - 79: I1IiI / oo0Oo
 if 77 - 77: Oo
 if 46 - 46: oOO
 if 72 - 72: OOOooOooo00O0 * iiiiiIIii
 if 67 - 67: i1IIi
 if 5 - 5: OoOoOO00 . OoooooooOO
 if 57 - 57: OOOo0
 if 35 - 35: OoooooooOO - oOO / Ooo00oOo00o
 if 50 - 50: I1IiI
 Ii11iII1 ( '[COLORgreen]Newest Episodes Added[/COLOR]' , 'http://www.watchseries.li/latest' , 10046 , i1iIIi1 + 'WATCHSERIES.png' , '' , '' )
 Ii11iII1 ( '[COLORgreen]This Week\'s Popular Episodes[/COLOR]' , 'http://www.watchseries.li/new' , 10042 , i1iIIi1 + 'WATCHSERIES.png' , '' , '' )
 Ii11iII1 ( '[COLORgreen]Search Program[/COLOR]' , '' , 10043 , i1iIIi1 + 'WATCHSERIES.png' , '' , '' )
 if 33 - 33: o00OO0OOO0
 if 98 - 98: I1IiI % OoOoOO00
def OoO0O000 ( url ) :
 O0oOoOOOoOO = ii1ii11IIIiiI ( url )
 IIi1I11I1II = re . compile ( '<ul class="pagination" style="line-height: 3;">(.+?)</ul>' , re . DOTALL ) . findall ( O0oOoOOOoOO )
 O00OOOoOoo0O = re . compile ( '<li><a href="/letters/(.+?)">(.+?)</a></li>' ) . findall ( str ( IIi1I11I1II ) )
 for url , ii11IIII11I in O00OOOoOoo0O :
  Ii11iII1 ( '[COLORgreen]' + ii11IIII11I + '[/COLOR]' , 'http://watchseries.li/letters/' + url , 10049 , i1iIIi1 + 'WATCHSERIES.png' , '' , '' )
  if 14 - 14: Ooo00oOo00o / Ooo00oOo00o * O0 . o00oOO0
def oooOO0oOooO00 ( url ) :
 O0oOoOOOoOO = ii1ii11IIIiiI ( url )
 O00OOOoOoo0O = re . compile ( '<a href="(.+?)" class="sr-header">(.+?)</a>' ) . findall ( O0oOoOOOoOO )
 for url , ii11IIII11I in O00OOOoOoo0O :
  Ii11iII1 ( '[COLORgreen]' + ii11IIII11I + '[/COLOR]' , 'http://watchseries.li/' + url , 10049 , i1iIIi1 + 'WATCHSERIES.png' , '' , '' )
  if 37 - 37: I1I1ii
def iI11i ( url ) :
 O0oOoOOOoOO = ii1ii11IIIiiI ( url )
 O00OOOoOoo0O = re . compile ( '<li class="col-md-6 col-xs-12 list-movies-li"><a href="(.+?)" title=".+?">(.+?)<span class="epnum">.+?</span></a></li>' , re . DOTALL ) . findall ( O0oOoOOOoOO )
 I1i = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="(.+?)">Next</a></li></ul>' , re . DOTALL ) . findall ( O0oOoOOOoOO )
 for url , ii11IIII11I in O00OOOoOoo0O :
  Ii11iII1 ( '[COLORgreen]' + ( ii11IIII11I ) . replace ( '&nbsp;' , ' ' ) . replace ( '&amp;' , '&' ) . replace ( '&#039;' , '\'' ) + '[/COLOR]' , 'http://www.watchseries.li' + url , 10044 , i1iIIi1 + 'WATCHSERIES.png' , '' , '' )
 for url in I1i :
  Ii11iII1 ( '[COLORgreen]' + 'NEXT' + '[/COLOR]' , 'http://www.watchseries.li' + url , 10049 , i1iIIi1 + 'Next.png' , '' , '' )
  if 73 - 73: OOOooOooo00O0 * OOOooOooo00O0 / oo0Oo
  if 43 - 43: ii11ii1ii . i1IIi . I1I1ii + O0 * i1Iii * O0
def II11ii ( ) :
 Iii1I1I11iiI1 = i1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 I1 = 'http://www.watchseries.li/search/' + Iii1I1I11iiI1 . replace ( ' ' , '%20' )
 O0oOoOOOoOO = ii1ii11IIIiiI ( I1 )
 O00OOOoOoo0O = re . compile ( '<img src="(.+?)".+?<a href="(.+?)" title=".+?"><b>(.+?)</b>' , re . DOTALL ) . findall ( O0oOoOOOoOO )
 for i1111I1I , o0ooooO0o0O , ii11IIII11I in O00OOOoOoo0O :
  if 'watch online' in ii11IIII11I :
   pass
  else :
   print o0ooooO0o0O
   Ii11iII1 ( '[COLORgreen]' + ii11IIII11I + '[/COLOR]' , 'http://www.watchseries.li' + o0ooooO0o0O , 10044 , i1111I1I , '' , '' )
   if 84 - 84: I1IiI - i11iIiiIii
   xbmcplugin . setContent ( O0O , 'movies' )
   if 1 - 1: OOOooOooo00O0 * I1IiI
def OO0ooo0 ( url ) :
 O0oOoOOOoOO = ii1ii11IIIiiI ( url )
 O00OOOoOoo0O = re . compile ( '<img src="(.+?)".+?<div class="block-left-home-inside-text">.+?<a href="(.+?)" title=".+?"><b>(.+?)</b> <br>.+?<span class=".+?">(.+?)</span></a><br>(.+?)<br>' , re . DOTALL ) . findall ( O0oOoOOOoOO )
 for i1111I1I , url , ii11IIII11I , ooo00OoOO0o , O0oO0iII11 in O00OOOoOoo0O :
  II1II1iI = ( ii11IIII11I ) . replace ( '&nbsp;' , ' ' ) . replace ( '&amp;' , '&' ) . replace ( '&#039;' , '\'' ) + ' - ' + ( ooo00OoOO0o ) . replace ( '&amp;' , '&' ) . replace ( '&#039;' , '\'' )
  Ii11iII1 ( '[COLORgreen]' + II1II1iI + '[/COLOR]' , 'http://www.watchseries.li' + url , 10045 , i1111I1I , '' , O0oO0iII11 )
  if 58 - 58: O0 . I1I1ii / OoooooooOO . Ooo00oOo00o / Oo * OoOoOO00
def O0oo0O00 ( url ) :
 O0oOoOOOoOO = ii1ii11IIIiiI ( url )
 O00OOOoOoo0O = re . compile ( '<li class="col-md-6 col-xs-12 list-movies-li"><a href="(.+?)" title=".+?">(.+?)<span class="epnum">.+?</span></a></li>' , re . DOTALL ) . findall ( O0oOoOOOoOO )
 I1i = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="(.+?)">Next</a></li></ul>' , re . DOTALL ) . findall ( O0oOoOOOoOO )
 for url , ii11IIII11I in O00OOOoOoo0O :
  II1II1iI = ( ii11IIII11I ) . replace ( '&nbsp;' , ' ' ) . replace ( '&amp;' , '&' ) . replace ( '&#039;' , '\'' )
  Ii11iII1 ( '[COLORgreen]' + II1II1iI + '[/COLOR]' , 'http://www.watchseries.li' + url , 10045 , i1iIIi1 + 'WATCHSERIES.png' , '' , '' )
 for url in I1i :
  Ii11iII1 ( '[COLORgreen]' + 'NEXT' + '[/COLOR]' , 'http://www.watchseries.li' + url , 10046 , i1iIIi1 + 'Next.png' , '' , '' )
  if 69 - 69: iiiiiIIii % O0
def OOi1iiii ( url ) :
 O0oOoOOOoOO = ii1ii11IIIiiI ( url )
 O00OOOoOoo0O = re . compile ( '<div class="mask">.+?<a href="(.+?)" title="(.+?)">.+?<img src="(.+?)"' , re . DOTALL ) . findall ( O0oOoOOOoOO )
 I1i = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="(.+?)">Next</a></li></ul>' , re . DOTALL ) . findall ( O0oOoOOOoOO )
 for url , ii11IIII11I , i1111I1I in O00OOOoOoo0O :
  Ii11iII1 ( '[COLORgreen]' + ( ii11IIII11I ) . replace ( '&nbsp;' , ' ' ) . replace ( '&amp;' , '&' ) . replace ( '&#039;' , '\'' ) + '[/COLOR]' , 'http://www.watchseries.li' + url , 10044 , i1111I1I , '' , '' )
 for url in I1i :
  Ii11iII1 ( '[COLORgreen]' + 'NEXT' + '[/COLOR]' , 'http://www.watchseries.li' + url , 10041 , i1iIIi1 + 'Next.png' , '' , '' )
  if 90 - 90: OOooOOo % ii11ii1ii - iIii1I11I1II1 % I1IiI
def IIiI11I1I1i1i ( url ) :
 O0oOoOOOoOO = ii1ii11IIIiiI ( url )
 IIi1I11I1II = re . compile ( '<div class="col-md-6 col-xs-12".+?<a href=".+?" itemprop="url"><span itemprop="name">(.+?)</span>(.+?)</ul>' , re . DOTALL ) . findall ( O0oOoOOOoOO )
 for Ii11Iii , i1iiIIi1I in IIi1I11I1II :
  O00OOOoOoo0O = re . compile ( '<li itemprop="episode".+?<meta itemprop="url" content="(.+?)">.+?<span class="" itemprop="name">\n(.+?)\n' , re . DOTALL ) . findall ( str ( i1iiIIi1I ) )
  for url , ii11IIII11I in O00OOOoOoo0O :
   II1II1iI = ( Ii11Iii ) . replace ( '  ' , '' ) + ' ' + ( ii11IIII11I ) . replace ( '&nbsp;' , ' ' ) . replace ( '&#039;' , '\'' ) . replace ( '  ' , '' )
   Ii11iII1 ( '[COLORgreen]' + II1II1iI + '[/COLOR]' , 'http://www.watchseries.li' + url , 10045 , i1iIIi1 + 'WATCHSERIES.png' , '' , '' )
 I1i = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="(.+?)">Next</a></li></ul>' , re . DOTALL ) . findall ( O0oOoOOOoOO )
 for url in I1i :
  Ii11iII1 ( '[COLORgreen]' + 'NEXT' + '[/COLOR]' , 'http://www.watchseries.li' + url , 10044 , i1iIIi1 + 'Next.png' , '' , '' )
  if 86 - 86: i1IIi
  if 13 - 13: O0
class O0o0O ( ) :
 if 6 - 6: OoOoOO00
 List = [ ]
 source_list = [ ]
 def __init__ ( self , name ) :
  if 7 - 7: i1Iii % i1IIi * OoooooooOO * O0 + OOOooOooo00O0
  II1II1iI = name
  self . Get_Sources ( o0ooooO0o0O , II1II1iI )
  if 95 - 95: OoooooooOO + o00OO0OOO0 - ii11ii1ii / ii11ii1ii . i1IIi . OoooooooOO
  if 29 - 29: oo0Oo - i1IIi . o00OO0OOO0 - ii11ii1ii + oo0Oo + OoooooooOO
 def Get_Sources ( self , URL , season_name ) :
  o00 = xbmcgui . DialogProgress ( )
  O0oOoOOOoOO = ii1ii11IIIiiI ( URL )
  O00OOOoOoo0O = re . compile ( '<td>.+?<a href="/link/(.+?)".+?height="16px">(.+?)\n' , re . DOTALL ) . findall ( O0oOoOOOoOO )
  for o0ooooO0o0O , ii11IIII11I in O00OOOoOoo0O :
   URL = 'http://www.watchseries.li/link/' + o0ooooO0o0O
   self . Get_site_link ( URL , season_name )
   if 36 - 36: i1IIi / oo0Oo . iIii1I11I1II1
 def Get_site_link ( self , url , season_name ) :
  O0oOoOOOoOO = ii1ii11IIIiiI ( url )
  O00OOOoOoo0O = re . compile ( '<iframe style=.+?" src="(.+?)"' ) . findall ( O0oOoOOOoOO )
  I1i = re . compile ( '<IFRAME SRC="(.+?)"' ) . findall ( O0oOoOOOoOO )
  i111i11I1ii = re . compile ( '<IFRAME style=".+?" SRC="(.+?)"' ) . findall ( O0oOoOOOoOO )
  for url in O00OOOoOoo0O :
   self . main ( url , season_name )
  for url in I1i :
   self . main ( url , season_name )
  for url in i111i11I1ii :
   self . main ( url , season_name )
   if 12 - 12: i1Iii
 def main ( self , url , season_name ) :
  o00 . create ( "[COLORwhite]Origin[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
  if 'daclips.in' in url :
   Ooii1IIi1ii = 'DACLIPS'
   if Ooii1IIi1ii in O0o0O . source_list :
    pass
   else :
    self . daclips ( url , season_name , Ooii1IIi1ii )
    o00 . update ( 0 , "" , "Getting Daclips Links" )
  else :
   if 'filehoot.com' in url :
    Ooii1IIi1ii = 'FILEHOOT'
    if Ooii1IIi1ii in O0o0O . source_list :
     pass
    else :
     o00 . update ( 0 , "" , "Getting Filehoot Links" )
     self . filehoot ( url , season_name , Ooii1IIi1ii )
   else :
    if 'thevideo.me' in url :
     Ooii1IIi1ii = 'THEVIDEO'
     if Ooii1IIi1ii in O0o0O . source_list :
      pass
     else :
      self . thevideo ( url , season_name , Ooii1IIi1ii )
      o00 . update ( 0 , "" , "Getting Thevideo Links" )
    else :
     if 'allmyvideos.net' in url :
      Ooii1IIi1ii = 'ALLMYVIDEOS'
      if Ooii1IIi1ii in O0o0O . source_list :
       pass
      else :
       self . allmyvid ( url , season_name , Ooii1IIi1ii )
       o00 . update ( 0 , "" , "Getting Allmyvideo Links" )
     else :
      if 'vidspot.net' in url :
       Ooii1IIi1ii = 'VIDSPOT'
       if Ooii1IIi1ii in O0o0O . source_list :
        pass
       else :
        self . vidspot ( url , season_name , Ooii1IIi1ii )
        o00 . update ( 0 , "" , "Getting Vidspot Links" )
      else :
       if 'vodlocker' in url :
        Ooii1IIi1ii = 'VODLOCKER'
        if Ooii1IIi1ii in O0o0O . source_list :
         pass
        else :
         self . vodlocker ( url , season_name , Ooii1IIi1ii )
         o00 . update ( 0 , "" , "Getting Vodlocker Links" )
         if 85 - 85: OoooooooOO % I1IiI * iIii1I11I1II1
         if 44 - 44: iIii1I11I1II1 . ii11ii1ii + oOO . oo0Oo
 def allmyvid ( self , url , season_name , source_name ) :
  O0oOoOOOoOO = ii1ii11IIIiiI ( url )
  O00OOOoOoo0O = re . compile ( '"file" : "(.+?)",\n.+?"default" : .+?,\n.+?"label" : "(.+?)"' , re . DOTALL ) . findall ( O0oOoOOOoOO )
  for II1i11 , ii11IIII11I in O00OOOoOoo0O :
   self . Printer ( II1i11 , season_name , source_name )
   if 28 - 28: OoOoOO00 - o00oOO0 % I1IiI + Ooo00oOo00o - I1IiI
 def vidspot ( self , url , season_name , source_name ) :
  O0oOoOOOoOO = ii1ii11IIIiiI ( url )
  O00OOOoOoo0O = re . compile ( '"file" : "(.+?)",\n.+?"default" : .+?,\n.+?"label" : "(.+?)"' ) . findall ( O0oOoOOOoOO )
  for II1i11 , ii11IIII11I in O00OOOoOoo0O :
   self . Printer ( II1i11 , season_name , source_name )
   if 28 - 28: OoOoOO00 . o00oOO0 + O0 . O0 . iiiiiIIii
 def thevideo ( self , url , season_name , source_name ) :
  O0oOoOOOoOO = ii1ii11IIIiiI ( url )
  O00OOOoOoo0O = re . compile ( "{ label: '.+?', file: '(.+?)' }" ) . findall ( O0oOoOOOoOO )
  for II1i11 in O00OOOoOoo0O :
   self . Printer ( II1i11 , season_name , source_name )
   if 98 - 98: OoooooooOO % O0 - O0
 def vodlocker ( self , url , season_name , source_name ) :
  O0oOoOOOoOO = ii1ii11IIIiiI ( url )
  O00OOOoOoo0O = re . compile ( 'file: "(.+?)",.+?skin' , re . DOTALL ) . findall ( O0oOoOOOoOO )
  for II1i11 in O00OOOoOoo0O :
   self . Printer ( II1i11 , season_name , source_name )
   if 76 - 76: i1IIi % I1IiI - OOOo0 / OOooOOo * oo0Oo
 def daclips ( self , url , season_name , source_name ) :
  O0oOoOOOoOO = ii1ii11IIIiiI ( url )
  O00OOOoOoo0O = re . compile ( '{ file: "(.+?)", type:"video" }' ) . findall ( O0oOoOOOoOO )
  for II1i11 in O00OOOoOoo0O :
   self . Printer ( II1i11 , season_name , source_name )
   if 4 - 4: Oo * Oo / I1IiI
 def filehoot ( self , url , season_name , source_name ) :
  O0oOoOOOoOO = ii1ii11IIIiiI ( url )
  O00OOOoOoo0O = re . compile ( 'file: "(.+?)",.+?skin' , re . DOTALL ) . findall ( O0oOoOOOoOO )
  for II1i11 in O00OOOoOoo0O :
   self . Printer ( II1i11 , season_name , source_name )
   if 4 - 4: OOOo0 * I1IiI % o00OO0OOO0 . I1IiI
 def Printer ( self , Link , season_name , source_name ) :
  if 11 - 11: iiiiiIIii - I1IiI - OOooOOo * I1IiI + oo0Oo
  if Link in O0o0O . List :
   pass
  elif source_name in O0o0O . source_list :
   pass
  else :
   O0000 ( '[COLORgreen]' + source_name + '[/COLOR]' , Link , 10012 , i1iIIi1 + 'WATCHSERIES.png' )
   o00 . update ( 100 , "" , "Got Source" )
   O0o0O . List . append ( Link )
   O0o0O . source_list . append ( source_name )
   if 62 - 62: OOOo0 * i11iIiiIii . OOOooOooo00O0
   xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
   if 35 - 35: I1I1ii . O0 + Oo + iiiiiIIii + i1IIi
   if 65 - 65: O0 * OOOo0 / OOOo0 . I1IiI
   if 87 - 87: OoOoOO00 * ii11ii1ii % Oo * Oo
   if 58 - 58: iiiiiIIii . OOooOOo + OOOo0 % Oo - Ooo00oOo00o
   if 50 - 50: OOOooOooo00O0 % OoOoOO00 - oo0Oo . i1IIi + O0 % OOOooOooo00O0
def i1iIi1IIiIII1 ( ) :
 Ii11iII1 ( '[COLORgreen]Highlights[/COLOR]' , '' , 10008 , i1iIIi1 + 'ORIGINFOOTBALL.png' , oooOOOOO , '' )
 Ii11iII1 ( '[COLORgreen]Fixtures[/COLOR]' , '' , 10009 , i1iIIi1 + 'ORIGINFOOTBALL.png' , oooOOOOO , '' )
 if 19 - 19: o00OO0OOO0
def O00O ( ) :
 oOOooOoo = ii1ii11IIIiiI ( oOOoo00O0O ( 'aHR0cDovL2xpdmVvbnNhdC5jb20vcXVpY2tpbmRleC5odG1s' ) )
 O00OOOoOoo0O = re . compile ( '<a target="_self" href="(.+?)".+?src="(.+?)" alt="(.+?)"' , re . DOTALL ) . findall ( oOOooOoo )
 for o0ooooO0o0O , i1111I1I , ii11IIII11I in O00OOOoOoo0O :
  Ii11iII1 ( '[COLORgreen]' + ( ii11IIII11I ) . replace ( 'amp;' , '' ) + '[/COLOR]' , oOOoo00O0O ( 'aHR0cDovL2xpdmVvbnNhdC5jb20v' ) + o0ooooO0o0O , 10010 , oOOoo00O0O ( 'aHR0cDovL2xpdmVvbnNhdC5jb20v' ) + i1111I1I , oooOOOOO , '' )
  if 94 - 94: i1Iii - ii11ii1ii + OOooOOo - Oo
def iiIi1iiI1I ( url ) :
 O0oOoOOOoOO = ii1ii11IIIiiI ( url )
 IIi1I11I1II = re . compile ( 'AndClearL.+?><h2.+?head>(.*?)float' , re . DOTALL ) . findall ( O0oOoOOOoOO )
 for IIi1I11I1II in IIi1I11I1II :
  Iiii1I = re . compile ( '(.*?)</h2>' ) . findall ( str ( IIi1I11I1II ) )
  for ooooo0Oo0 in Iiii1I :
   ooooo0Oo0 = ooooo0Oo0
  o0I1IIIi11ii11 = re . compile ( 'comp_head>(.*?)</span>.*?<div class = fLeft width = ".*?"><img src="(.*?)">.*?</div>.*?ST:(.*?)</div>(.+?)<!-- around all of channel types ENDS 2-->' , re . DOTALL ) . findall ( str ( IIi1I11I1II ) )
  for O0o0oo0oOO0oO , i1111I1I , time , iIiIII1iI1111 in o0I1IIIi11ii11 :
   oo000 = re . compile ( ",CAPTION, '(.+?)&nbsp" ) . findall ( iIiIII1iI1111 )
   Ii11iII1 ( '[COLORgreen]' + ooooo0Oo0 + ' - ' + O0o0oo0oOO0oO + ' - ' + time + '[/COLOR]' , '' , 10010 , oOOoo00O0O ( 'aHR0cDovL2xpdmVvbnNhdC5jb20=' ) + i1111I1I , oooOOOOO , ( str ( oo000 ) ) )
   if 37 - 37: i11iIiiIii % o00oOO0 * iiiiiIIii * iiiiiIIii * i1Iii
 I1IiII11III ( 'tvshows' , 'Media Info 3' )
 if 24 - 24: oo0Oo / OOOooOooo00O0 + I1I1ii . I1I1ii
def I1ii1i ( ) :
 if 22 - 22: o00oOO0 * i1Iii * i11iIiiIii + OOOooOooo00O0 * I1IiI * Ooo00oOo00o
 Ii11iII1 ( '[COLORgreen]Shows[/COLOR]' , 'http://www.fullmatchesandshows.com/category/show/' , 10011 , 'http://www.fm-base.co.uk/forum/attachments/club-competition-logos/3885-soccer-am-logo-socceram.png' , i1iIIi1 + 'fanart.jpg' , '' )
 Ii11iII1 ( '[COLORgreen]Premier League[/COLOR]' , 'http://www.fullmatchesandshows.com/premier-league/' , 10011 , 'https://footballseasons.files.wordpress.com/2013/05/premier-league.png' , i1iIIi1 + 'fanart.jpg' , '' )
 Ii11iII1 ( '[COLORgreen]La Liga[/COLOR]' , 'http://www.fullmatchesandshows.com/la-liga/' , 10011 , 'http://1.bp.blogspot.com/-c6kQ40ryhyo/U19cUlz25sI/AAAAAAAABak/qtn5chSFZm0/s1600/la-liga-logo_display_image.png' , i1iIIi1 + 'fanart.jpg' , '' )
 Ii11iII1 ( '[COLORgreen]Bundesliga[/COLOR]' , 'http://www.fullmatchesandshows.com/bundesliga/' , 10011 , 'http://m.img.brothersoft.com/iphone/189/518670189_icon175x175.jpg' , i1iIIi1 + 'fanart.jpg' , '' )
 Ii11iII1 ( '[COLORgreen]Champions League[/COLOR]' , 'http://www.fullmatchesandshows.com/champions-league/' , 10011 , 'http://www.ecursuri.ro/images/teste/test-champions-league.jpg' , i1iIIi1 + 'fanart.jpg' , '' )
 Ii11iII1 ( '[COLORgreen]Serie A[/COLOR]' , 'http://www.fullmatchesandshows.com/category/serie-a/' , 10011 , 'http://files.jcriccione.it/200000223-2484526782/serie%20a.png' , i1iIIi1 + 'fanart.jpg' , '' )
 Ii11iII1 ( '[COLORgreen]Ligue 1[/COLOR]' , 'http://www.fullmatchesandshows.com/category/ligue-1/' , 10011 , 'http://a1.mzstatic.com/us/r30/Purple5/v4/37/c7/44/37c744ae-5824-42b7-6ce0-5f471f52baab/icon180x180.jpeg' , i1iIIi1 + 'fanart.jpg' , '' )
 Ii11iII1 ( '[COLORgreen]Copa America 2015[/COLOR]' , 'http://www.fullmatchesandshows.com/copa-america-2015/' , 10011 , 'https://pbs.twimg.com/profile_images/521966985907691520/Nq9OAPIo_400x400.png' , i1iIIi1 + 'fanart.jpg' , '' )
 Ii11iII1 ( '[COLORgreen]CONCACAF[/COLOR]' , 'http://www.fullmatchesandshows.com/category/concacaf/' , 10011 , 'http://a3.mzstatic.com/us/r30/Purple3/v4/40/26/14/4026147c-7022-4ca3-504e-e78950cc3f1c/icon175x175.png' , i1iIIi1 + 'fanart.jpg' , '' )
 Ii11iII1 ( '[COLORgreen]Women World Cup[/COLOR]' , 'http://www.fullmatchesandshows.com/category/women-world-cup/' , 10011 , 'https://upload.wikimedia.org/wikipedia/en/thumb/7/76/2015_FIFA_Women\'s_World_Cup_logo.svg/967px-2015_FIFA_Women\'s_World_Cup_logo.svg.png' , i1iIIi1 + 'fanart.jpg' , '' )
 if 85 - 85: OOOooOooo00O0 * iiiiiIIii % Oo - OOOooOooo00O0 - o00OO0OOO0
def iIOOO ( url ) :
 O0oOoOOOoOO = ii1ii11IIIiiI ( url )
 O00OOOoOoo0O = re . compile ( 'itemprop="image" class="entry-thumb" src="(.+?)".+?<h3 itemprop="name" class="entry-title td-module-title"><a itemprop="url" href="(.+?)" rel="bookmark" title=".+?">(.+?)</a></h3>' , re . DOTALL ) . findall ( O0oOoOOOoOO )
 for i1111I1I , url , ii11IIII11I in O00OOOoOoo0O :
  iI1O00oO0o000oO = ii11IIII11I . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' )
  O0000 ( '[COLORgreen]' + iI1O00oO0o000oO + '[/COLOR]' , url , 10013 , i1111I1I )
  if 19 - 19: I1I1ii * oOO / o00oOO0 * oOO - OoooooooOO * o00OO0OOO0
def iiiI1i1 ( url ) :
 O0oOoOOOoOO = ii1ii11IIIiiI ( url )
 O00OOOoOoo0O = re . compile ( '<script data-config="(.+?)" data-height' ) . findall ( O0oOoOOOoOO )
 for O00Oooo in O00OOOoOoo0O :
  I1i1i11 = ( O00Oooo ) . replace ( '/v2' , '' ) . replace ( 'zeus.json' , 'video-sd.mp4?hosting_id=21772' ) . replace ( 'config.playwire.com' , 'cdn.video.playwire.com' )
  o00oo0000 ( 'http:' + I1i1i11 )
  if 29 - 29: I1I1ii . oo0Oo - OoOoOO00
  if 68 - 68: iIii1I11I1II1 + OoOoOO00 / o00oOO0
def oOooo00000 ( url ) :
 oOOooOoo = o0OOOoO0 ( url )
 O00OOOoOoo0O = re . compile ( '<a href="([^"]*)" title="([^"]*)"><img itemprop="image" content="([^"]*)"' , re . DOTALL ) . findall ( oOOooOoo )
 I1i = re . compile ( "<a rel='next' href=([^=]*)=" , re . DOTALL ) . findall ( oOOooOoo )
 for url , ii11IIII11I , i1111I1I in O00OOOoOoo0O :
  O0000 ( ii11IIII11I , url , 8046 , i1111I1I )
 for url in I1i :
  oOo00 ( 'NEXT PAGE' , ( url ) . replace ( ' class' , '' ) , 8045 , i1iIIi1 + 'Next.png' )
def iiI11I1iiIiII1I ( url ) :
 oOOooOoo = o0OOOoO0 ( url )
 O00OOOoOoo0O = re . compile ( "__filename='([^']*)',.+?__fullimage='([^']*)',.+?__title='([^']*)'," , re . DOTALL ) . findall ( oOOooOoo )
 for url , i1111I1I , ii11IIII11I in O00OOOoOoo0O :
  o00oo0000 ( 'http://bitcast-b.bitgravity.com/ndtvod/23372/ndtv/' + url )
  if 59 - 59: oOO - I1I1ii
def iiiii111 ( url ) :
 oOOooOoo = o0OOOoO0 ( url )
 O00OOOoOoo0O = re . compile ( "src='http://www.youtube.com/embed/(.+?)?version=3&#038;rel=1&#038;fs=1&#038;autohide=2&#038;showsearch=0&#038;showinfo=1&#038;iv_load_policy=1&#038;wmode=transparent' frameborder='0' allowfullscreen='true'></iframe>" ) . findall ( oOOooOoo )
 for url in O00OOOoOoo0O :
  yt . PlayVideo ( url )
  if 93 - 93: o00oOO0 * i1Iii
def ii11i1I1iiii ( ) :
 oOOooOoo = o0OOOoO0 ( oOOoo00O0O ( 'aHR0cDovL3RvcGRvY3VtZW50YXJ5ZmlsbXMuY29tLw==' ) )
 O00OOOoOoo0O = re . compile ( '<a href="(.+?)" >(.+?)</a></li><li>' ) . findall ( oOOooOoo )
 for o0ooooO0o0O , ii11IIII11I in O00OOOoOoo0O :
  oOo00 ( ii11IIII11I , o0ooooO0o0O , 8041 , i1iIIi1 + 'documentary.png' )
def I11iI1I ( url ) :
 oOOooOoo = o0OOOoO0 ( url )
 O00OOOoOoo0O = re . compile ( '<h2><a href="(.+?)" title="(.+?)">.+?</a></h2>.+?src="(.+?)"' , re . DOTALL ) . findall ( oOOooOoo )
 I1i = re . compile ( 'class="inactive">.+?</a><a href="(.+?)">Next</a></div>' , re . DOTALL ) . findall ( oOOooOoo )
 for url , ii11IIII11I , i1111I1I in O00OOOoOoo0O :
  oOo00 ( ( ii11IIII11I ) . replace ( '&#039;s' , '' ) , url , 8042 , i1111I1I )
 for url in I1i :
  oOo00 ( 'NEXT PAGE' , url , 8041 , i1iIIi1 + 'Next.png' )
  if 50 - 50: iIii1I11I1II1 * I1I1ii . OoooooooOO / OoOoOO00 - ii11ii1ii * ii11ii1ii
  if 98 - 98: Ooo00oOo00o - i1Iii . I1I1ii % i11iIiiIii
def OO00oo ( url ) :
 oOOooOoo = o0OOOoO0 ( url )
 O00OOOoOoo0O = re . compile ( '<meta itemprop="name" content="(.+?)".+?<meta itemprop="thumbnailUrl" content="(.+?)".+?<meta itemprop="embedUrl" content="(.+?)".+?<meta itemprop="description" content="(.+?)" />' , re . DOTALL ) . findall ( oOOooOoo )
 I1i = re . compile ( '<div class="video new-video"><iframe width="766" height="431" src="(.+?)&amp;iv_load_policy=3&amp;showinfo=0&amp;autohide=1"' , re . DOTALL ) . findall ( oOOooOoo )
 for ii11IIII11I , i1111I1I , url , Iiii in O00OOOoOoo0O :
  O0000 ( ( ii11IIII11I ) . replace ( '&#039;s' , '' ) , url . replace ( 'https://www.youtube.com/embed/' , '' ) , 8043 , i1111I1I )
 for url in I1i :
  O0Oo0O0 ( ( url ) . replace ( '//' , 'http://' ) )
  if 33 - 33: oo0Oo % i1IIi - o00oOO0 . O0 / O0
def O0Oo0O0 ( url ) :
 oOOooOoo = o0OOOoO0 ( url )
 O00OOOoOoo0O = re . compile ( '<link rel="canonical" href="(.+?)">  <link rel="stylesheet"' ) . findall ( oOOooOoo )
 for url in O00OOOoOoo0O :
  O0000 ( 'PLAY' , ( url ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , i1iIIi1 + 'documentary.png' )
  if 96 - 96: OoooooooOO + I1I1ii * O0
def oo0OoOO0o0o ( ) :
 O0oOoOOOoOO = o0OOOoO0 ( 'http://www.stream2watch.co/live-tv' )
 O00OOOoOoo0O = re . compile ( '<a href="(.+?)">.+?<img src="(.+?)" alt=".+?"/>.+?<span class="country_name">(.+?)<br />(.+?)</span>' , re . DOTALL ) . findall ( O0oOoOOOoOO )
 for o0ooooO0o0O , i1111I1I , ii11IIII11I , OO0OOO00 in O00OOOoOoo0O :
  oOo00 ( ( ii11IIII11I + '[COLORgreen]' + OO0OOO00 + '[/COLOR]' ) , o0ooooO0o0O , 8086 , i1111I1I )
  if 62 - 62: i11iIiiIii + I1IiI + i1IIi
def oOOoO0O ( url ) :
 O0oOoOOOoOO = o0OOOoO0 ( url )
 O00OOOoOoo0O = re . compile ( '<a class="front_channel_href" href="(.+?)" title=".+?">.+?<img class="front_channel_thumb" src="(.+?)" alt=".+?"/>.+?<span class="front_channel_name">(.+?)</span>' , re . DOTALL ) . findall ( O0oOoOOOoOO )
 for url , i1111I1I , ii11IIII11I in O00OOOoOoo0O :
  oOo00 ( '[COLORgreen]' + ii11IIII11I + '[/COLOR]' , url , 8087 , i1111I1I )
  if 15 - 15: oOO
def Ooooo ( url ) :
 O0oOoOOOoOO = ii1ii11IIIiiI ( url )
 O00OOOoOoo0O = re . compile ( 'a id="code_.+?data-f-href="(.+?)" data-code-embed="">(.+?)</a>' , re . DOTALL ) . findall ( O0oOoOOOoOO )
 for url , ii11IIII11I in O00OOOoOoo0O :
  iIiiiIiIi ( url , ii11IIII11I )
  if 19 - 19: I1I1ii . ii11ii1ii / I1IiI
def iIiiiIiIi ( url , name ) :
 O0oOoOOOoOO = ii1ii11IIIiiI ( url )
 O00OOOoOoo0O = re . compile ( "playStream\('.+?', '(.+?)'\);" , re . DOTALL ) . findall ( O0oOoOOOoOO )
 for url in O00OOOoOoo0O :
  print url
  O0000 ( '[COLORgreen]' + name + '[/COLOR]' , url , 222 , '' )
  if 68 - 68: oo0Oo / OoooooooOO * o00OO0OOO0 / o00oOO0
def ooooO000 ( ) :
 oOOooOoo = o0OOOoO0 ( oOOoo00O0O ( 'aHR0cDovL3d3dy5zb2xpZS5vcmcvYWxpYnJhcnkvaW5kZXguaHRtbA==' ) )
 O00OOOoOoo0O = re . compile ( '<td align="center" valign="top">.+?<a href="(.+?)">.+?<img src="(.+?)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( oOOooOoo )
 for o0ooooO0o0O , i1111I1I , ii11IIII11I in O00OOOoOoo0O :
  oOo00 ( ( '[COLORgreen]' + ii11IIII11I + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + o0ooooO0o0O , 3002 , 'http://www.solie.org/alibrary/' + i1111I1I )
def o0O00Oooo ( url ) :
 oOOooOoo = o0OOOoO0 ( url )
 O00OOOoOoo0O = re . compile ( '<td align="center" valign="top">.+?<a href="(.+?)">.+?<img src="(.+?)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( oOOooOoo )
 for url , i1111I1I , ii11IIII11I in O00OOOoOoo0O :
  oOo00 ( ( '[COLORgreen]' + ii11IIII11I + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3003 , 'http://www.solie.org/alibrary/' + i1111I1I )
def i1iIIII1iiIIi ( url ) :
 oOOooOoo = o0OOOoO0 ( url )
 O00OOOoOoo0O = re . compile ( '<br><a href="([^"]*)">(.+?)</a>' ) . findall ( oOOooOoo )
 i1I1IiI1ii = re . compile ( 'href="([^"]*)">Season(.+?)</a>' ) . findall ( oOOooOoo )
 next = re . compile ( '<a href="([^"]*)">Episodes</a>' ) . findall ( oOOooOoo )
 I1i = re . compile ( '<td align="center" valign="top">.+?<a href="(.+?)">.+?<img src="(.+?)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( oOOooOoo )
 for url , ii11IIII11I in O00OOOoOoo0O :
  O0000 ( ( '[COLORgreen]' + ii11IIII11I + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3004 , i1iIIi1 + 'classicmovies.png' )
 for url , ii11IIII11I in i1I1IiI1ii :
  oOo00 ( '[COLORgreen]Season- ' + ii11IIII11I + '[/COLOR]' , 'http://www.solie.org/alibrary/' + url , 3003 , i1iIIi1 + 'classicmovies.png' )
 for url in next :
  oOo00 ( '[COLORgreen]NEXT[/COLOR]' , 'http://www.solie.org/alibrary/' + url , 3003 , i1iIIi1 + 'Next.png' )
 for url , i1111I1I , ii11IIII11I in I1i :
  oOo00 ( ( '[COLORgreen]' + ii11IIII11I + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3003 , 'http://www.solie.org/alibrary/' + i1111I1I )
def O00OOoOOOO00O ( url ) :
 oOOooOoo = o0OOOoO0 ( url )
 O00OOOoOoo0O = re . compile ( '<iframe.+?src="([^"]*)"' ) . findall ( oOOooOoo )
 for url in O00OOOoOoo0O :
  Ooo0OOO ( url )
def Ooo0OOO ( url ) :
 oOOooOoo = o0OOOoO0 ( url )
 O00OOOoOoo0O = re . compile ( '<meta property="og:video" content="([^"]*)"/>' ) . findall ( oOOooOoo )
 for url in O00OOOoOoo0O :
  o00oo0000 ( url )
  if 94 - 94: i11iIiiIii % OoooooooOO / OOOo0
def iII1Iii11111 ( ) :
 oOOooOoo = o0OOOoO0 ( oOOoo00O0O ( 'aHR0cDovL3JldHJvdmlzaW9uLnR2L2FsbC8=' ) )
 O00OOOoOoo0O = re . compile ( '<a href="([^"]*)"><h2><font color=".+?"><h2>(.+?)</font></h2></a>' ) . findall ( oOOooOoo )
 for o0ooooO0o0O , ii11IIII11I in O00OOOoOoo0O :
  O0000 ( ( '[COLORgreen]' + ii11IIII11I + '[/COLOR]' ) . replace ( '&#8211;' , ':' ) , o0ooooO0o0O , 8061 , i1iIIi1 + 'classicmovies.png' )
def OOo00ooOoO0o ( url ) :
 oOOooOoo = o0OOOoO0 ( url )
 O00OOOoOoo0O = re . compile ( "v.src = '([^']*)';" ) . findall ( oOOooOoo )
 for url in O00OOOoOoo0O :
  o00oo0000 ( url )
  if 21 - 21: i11iIiiIii
def o00iIiiiII ( ) :
 oOOooOoo = o0OOOoO0 ( oOOoo00O0O ( 'aHR0cDovL3JldHJvdmlzaW9uLnR2L2NsYXNzaWMtdHYv' ) )
 O00OOOoOoo0O = re . compile ( '<a href="([^"]*)"><h2><font color=".+?"><h2>(.+?)</font></h2></a>' ) . findall ( oOOooOoo )
 for o0ooooO0o0O , ii11IIII11I in O00OOOoOoo0O :
  O0000 ( ( '[COLORgreen]' + ii11IIII11I + '[/COLOR]' ) . replace ( '&#8211;' , ':' ) , o0ooooO0o0O , 8061 , i1iIIi1 + 'classictv.png' )
def Ii1I1OO0ooO0 ( url ) :
 oOOooOoo = o0OOOoO0 ( url )
 O00OOOoOoo0O = re . compile ( "v.src = '([^']*)';" ) . findall ( oOOooOoo )
 for url in O00OOOoOoo0O :
  o00oo0000 ( url )
  if 95 - 95: iIii1I11I1II1 . I1I1ii - OoooooooOO * Ooo00oOo00o / OOooOOo
def oOo0OO0o0 ( ) :
 O0oOoOOOoOO = ii1ii11IIIiiI ( oOOoo00O0O ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vbTN1c3RyZWFtcw==' ) )
 O00OOOoOoo0O = re . compile ( '<li><a href="(.+?)"> (.+?).m3u</a></li>' ) . findall ( O0oOoOOOoOO )
 for o0ooooO0o0O , ii11IIII11I in O00OOOoOoo0O :
  oOo00 ( ( '[COLORgreen]' + ii11IIII11I + '[/COLOR]' ) . replace ( '-' , ' ' ) . replace ( '_' , ' ' ) , ( oOOoo00O0O ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vbTN1c3RyZWFtcy8=' ) ) + o0ooooO0o0O , 8071 , i1iIIi1 + 'streams.png' )
def II1 ( url ) :
 O0oOoOOOoOO = o0OOOoO0 ( url )
 O00OOOoOoo0O = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( O0oOoOOOoOO )
 for ii11IIII11I , url in O00OOOoOoo0O :
  O0000 ( ( '[COLORgreen]' + ii11IIII11I + '[/COLOR]' ) . replace ( '_' , ' ' ) , ( url ) . strip ( ) , 404 , i1iIIi1 + 'streams.png' )
def I1I ( url ) :
 O0oOoOOOoOO = o0OOOoO0 ( url )
 O00OOOoOoo0O = re . compile ( 'EXTINF:(.+?),(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( O0oOoOOOoOO )
 for i1111I1I , ii11IIII11I , url in O00OOOoOoo0O :
  url = ( ( oOOoo00O0O ( 'aHR0cDovL2dlbmlldHYuaXB0di5yZTo4MDAwL2xpdmUv' ) ) + oOo0oooo00o + '/' + oO0o0o0ooO0oO + url ) . strip ( )
  O0000 ( ( '[COLORgreen]' + ii11IIII11I + '[/COLOR]' ) . replace ( '_' , ' ' ) , url , 222 , i1111I1I )
  if 23 - 23: Ooo00oOo00o + I1I1ii + Oo % iIii1I11I1II1 . i11iIiiIii
def Oo0iII1iI1IIiI ( ) :
 O00O0OO00oo ( 'Best Videos' , 'http://www.xvideos.com/best' , 10105 , i1iIIi1 + 'JIZBOX.png' , '' , '' )
 O00O0OO00oo ( 'Genres' , 'http://www.xvideos.com' , 10106 , i1iIIi1 + 'JIZBOX.png' , '' , '' )
 O00O0OO00oo ( 'Recently Uploaded' , 'http://xvideos.com' , 10105 , i1iIIi1 + 'JIZBOX.png' , '' , '' )
 O00O0OO00oo ( 'Tags' , 'http://www.xvideos.com/tags' , 10103 , i1iIIi1 + 'JIZBOX.png' , '' , '' )
 O00O0OO00oo ( 'Search' , '' , 10107 , i1iIIi1 + 'JIZBOX.png' , '' , '' , )
 if 69 - 69: o00OO0OOO0 / i11iIiiIii * OOooOOo / oOO
def oO0OOOoooO00o0o ( url ) :
 O0oOoOOOoOO = ii1ii11IIIiiI ( url )
 I1ii1Ii1 = re . compile ( '<li><a class=".+?".+?href="(.+?)">Next</a></li>' ) . findall ( O0oOoOOOoOO )
 for url in I1ii1Ii1 :
  O00O0OO00oo ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10103 , i1iIIi1 + 'JIZBOX.png' , '' , '' )
 O00OOOoOoo0O = re . compile ( '<li><a href="(.+?)"><b>(.+?)</b><span class="navbadge default"(.+?)</span>' ) . findall ( O0oOoOOOoOO )
 for url , ii11IIII11I , OO in O00OOOoOoo0O :
  O00O0OO00oo ( ii11IIII11I + ' - No of Videos : ' + ( OO ) . replace ( '>' , '' ) , 'http://www.xvideos.com' + url , 10105 , i1iIIi1 + 'JIZBOX.png' , '' , '' )
  if 73 - 73: O0 . o00oOO0 + i11iIiiIii + iIii1I11I1II1 - o00OO0OOO0 / I1IiI
def OO0OOOOo0000O ( url ) :
 O0oOoOOOoOO = ii1ii11IIIiiI ( url )
 I1ii1Ii1 = re . compile ( 'href="([^"]*)">Next</a></li>' ) . findall ( O0oOoOOOoOO )
 for url in I1ii1Ii1 :
  O00O0OO00oo ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10104 , i1iIIi1 + 'Next.png' , '' , '' )
 O00OOOoOoo0O = re . compile ( ':"([^"]*)".+?;</script></a></div></div><p class="profile-name"><a href="([^"]*)">(.+?)</a></p><p class="profile-counts">\n(.+?)\n' , re . DOTALL ) . findall ( O0oOoOOOoOO )
 for i1111I1I , url , ii11IIII11I , i1Ii11ii in O00OOOoOoo0O :
  O00O0OO00oo ( ii11IIII11I + '--' + i1Ii11ii , 'http://www.xvideos.com' + url + '#_tabVideos,videos-best' , 10105 , ( i1111I1I ) . replace ( 'http:\/\/' , 'http://' ) , '' , '' )
  if 89 - 89: Oo + ii11ii1ii - OOooOOo
  if 40 - 40: Ooo00oOo00o + Ooo00oOo00o
def o0oo0o00ooO00 ( url ) :
 O0oOoOOOoOO = ii1ii11IIIiiI ( url )
 O00OOOoOoo0O = re . compile ( '<div class="thumb-inside"><script>.+?<img src="(.+?)".+?<a href="(.+?)" title=".+?">(.+?)</a></p>.+?uration">(.+?)</span>.+?Porn quality:(.+?)</span>' , re . DOTALL ) . findall ( O0oOoOOOoOO )
 for i1111I1I , url , ii11IIII11I , iiIi11iI1iii , IIiIiiI1i in O00OOOoOoo0O :
  IIiII ( ii11IIII11I + ' - Porn Quality : ' + IIiIiiI1i + ' - ' + iiIi11iI1iii , 'http://www.xvideos.com' + url , 10108 , i1111I1I , i1111I1I , IIiIiiI1i + ' - ' + iiIi11iI1iii )
 IIiO0Oo = re . compile ( '<li><a href="([^"]*)" class="no-page">Next</a></li></ul></div>' ) . findall ( O0oOoOOOoOO )
 for url in IIiO0Oo :
  O00O0OO00oo ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10105 , i1iIIi1 + 'Next.png' , '' , '' )
  if 35 - 35: ii11ii1ii + oOO - I1IiI % o00oOO0 % OOooOOo % I1IiI
def ii1IIiII111I ( url ) :
 O0oOoOOOoOO = ii1ii11IIIiiI ( url )
 IIi1I11I1II = re . compile ( '<div class="main-categories">(.+?)</div>' , re . DOTALL ) . findall ( O0oOoOOOoOO )
 I1ii1Ii1 = re . compile ( '<li><a class=".+?".+?href="(.+?)">Next</a></li>' ) . findall ( O0oOoOOOoOO )
 for url in I1ii1Ii1 :
  O00O0OO00oo ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10106 , i1iIIi1 + 'Next.png' , '' , '' )
 O00OOOoOoo0O = re . compile ( '<li><a href="(.+?)" class="btn btn-default">(.+?)</a>' ) . findall ( str ( IIi1I11I1II ) )
 for url , ii11IIII11I in O00OOOoOoo0O :
  O00O0OO00oo ( ii11IIII11I , 'http://www.xvideos.com' + url , 10105 , i1iIIi1 + 'JIZBOX.png' , '' , '' )
  if 87 - 87: i1Iii - ii11ii1ii % ii11ii1ii . o00oOO0 / ii11ii1ii
  if 6 - 6: I1IiI / iIii1I11I1II1 * OoooooooOO * i11iIiiIii
def o0O0OOo0oO ( ) :
 Iii1I1I11iiI1 = i1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 Iiiii = ( Iii1I1I11iiI1 ) . replace ( ' ' , '+' ) . replace ( '&amp;' , '&' )
 ii1I = Iiiii . lower ( )
 iiIIiiIi = 'http://www.xvideos.com/?k=' + ii1I
 print iiIIiiIi + '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'
 O0oOoOOOoOO = ii1ii11IIIiiI ( iiIIiiIi )
 O00OOOoOoo0O = re . compile ( '<div class="thumb-inside"><script>.+?<img src="(.+?)".+?<a href="(.+?)" title=".+?">(.+?)</a></p>.+?uration">(.+?)</span>.+?Porn quality:(.+?)</span>' , re . DOTALL ) . findall ( O0oOoOOOoOO )
 for i1111I1I , o0ooooO0o0O , ii11IIII11I , iiIi11iI1iii , IIiIiiI1i in O00OOOoOoo0O :
  IIiII ( ii11IIII11I + ' - Porn Quality : ' + IIiIiiI1i + ' - ' + iiIi11iI1iii , 'http://www.xvideos.com' + o0ooooO0o0O , 10108 , i1111I1I , i1111I1I , IIiIiiI1i + ' - ' + iiIi11iI1iii )
 IIiO0Oo = re . compile ( '<li><a href="([^"]*)" class="no-page">Next</a></li></ul></div>' ) . findall ( O0oOoOOOoOO )
 for o0ooooO0o0O in IIiO0Oo :
  O00O0OO00oo ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + o0ooooO0o0O , 10105 , i1iIIi1 + 'Next.png' , '' , '' )
  if 42 - 42: OOOooOooo00O0 + iIii1I11I1II1
def II1IiiIII ( url ) :
 O0oOoOOOoOO = ii1ii11IIIiiI ( url )
 O00OOOoOoo0O = re . compile ( 'flv_url=(.+?)\;' ) . findall ( O0oOoOOOoOO )
 for url in O00OOOoOoo0O :
  ii11iI1iIiIi = ( url ) . replace ( '%3A' , ':' ) . replace ( '%2F' , '/' ) . replace ( '%3F' , '?' ) . replace ( '%3D' , '=' ) . replace ( '%26' , '&' ) . replace ( '&amp' , '' )
  o0OO0OoO0o0o0 ( ii11iI1iIiIi )
  if 49 - 49: Oo * o00oOO0 + OOooOOo - i11iIiiIii
def o0OO0OoO0o0o0 ( url ) :
 oOO0oo = xbmc . Player ( OOooOi1i1Ii1Ii ( ) )
 import urlresolver
 try : oOO0oo . play ( url )
 except : pass
 if 99 - 99: ii11ii1ii + iiiiiIIii . o00oOO0
 if 1 - 1: iiiiiIIii * I1I1ii + o00OO0OOO0
def OOoo000O00O ( ) :
 O0oOoOOOoOO = ii1ii11IIIiiI ( oOOoo00O0O ( 'aHR0cDovL3d3dy5nb2Zpc2hpbmcuY28udWsvQW5nbGluZy1UaW1lcy9TZWN0aW9uL1ZpZGVvcy8=' ) )
 O00OOOoOoo0O = re . compile ( 'class="item.+?"><a href="(.+?)">(.+?)</a></li>' ) . findall ( O0oOoOOOoOO )
 for o0ooooO0o0O , ii11IIII11I in O00OOOoOoo0O :
  oOo00 ( '[COLORgreen]' + ii11IIII11I + '[/COLOR]' , ( 'http://www.gofishing.co.uk' + o0ooooO0o0O ) . replace ( 'http://www.gofishing.co.ukhttp://www.gofishing.co.uk' , 'http://www.gofishing.co.uk' ) , 8091 , i1iIIi1 + 'gofish.png' )
def IiI1Iiii1I ( url ) :
 O0oOoOOOoOO = o0OOOoO0 ( url )
 O00OOOoOoo0O = re . compile ( '<h2><a id=.+?href="([^"]*)">(.+?)</a></h2>' , re . DOTALL ) . findall ( O0oOoOOOoOO )
 I1i = re . compile ( '<h3><a href="([^"]*)" id=.+?>(.+?)</a> </h3>.+?<img src="([^"]*)"' , re . DOTALL ) . findall ( O0oOoOOOoOO )
 next = re . compile ( 'href="([^"]*)">next</a>&gt;</li>' , re . DOTALL ) . findall ( O0oOoOOOoOO )
 for url , ii11IIII11I in O00OOOoOoo0O :
  O0000 ( '[COLORgreen]' + ii11IIII11I + '[/COLOR]' , 'http://www.gofishing.co.uk/' + url , 8092 , i1iIIi1 + 'gofish.png' )
 for url , ii11IIII11I , i1111I1I in I1i :
  O0000 ( '[COLORgreen]' + ii11IIII11I + '[/COLOR]' , 'http://www.gofishing.co.uk/' + url , 8092 , 'http://www.gofishing.co.uk/' + i1111I1I )
 for url in next :
  oOo00 ( '[COLORgreen]NEXT[/COLOR]' , url . replace ( ' ' , '+' ) , 8091 , i1iIIi1 + 'Next.png' )
def I1iII ( url ) :
 O0oOoOOOoOO = o0OOOoO0 ( url )
 O00OOOoOoo0O = re . compile ( 'src="https://www.youtube.com/embed/(.+?)"' ) . findall ( O0oOoOOOoOO )
 for url in O00OOOoOoo0O :
  yt . PlayVideo ( url )
  if 29 - 29: i1IIi % OOOooOooo00O0 / I1I1ii + I1IiI - iiiiiIIii - ii11ii1ii
def OoiiI1i111 ( url ) :
 oO0O0o0O = urllib2 . Request ( url )
 oO0O0o0O . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
 oOO00ooOOo = ''
 i11iiI1111 = ''
 try :
  oOO00ooOOo = urllib2 . urlopen ( oO0O0o0O )
  i11iiI1111 = oOO00ooOOo . read ( )
  oOO00ooOOo . close ( )
 except : pass
 if i11iiI1111 != '' :
  return i11iiI1111
 else :
  i11iiI1111 = 'Failed'
  return i11iiI1111
  if 20 - 20: ii11ii1ii
  if 3 - 3: Ooo00oOo00o * i1IIi . OOOo0 . O0 - I1IiI
def OOoooOoO0 ( ) :
 O0OOoooo0 = ( oOOoo00O0O ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 Iii1I1I11iiI1 = i1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 ii1I = Iii1I1I11iiI1 . lower ( )
 o0ooooO0o0O = ( oOOoo00O0O ( 'aHR0cDovL2RsNC5tb3ZpZWZhcnNpLmNvbS9maWxtLzIwMTUtNy8=' ) )
 oO00oooOOoOo0 = ( oOOoo00O0O ( 'aHR0cDovL2RsLmF2YWRsLmNvbS9OZXcvTW92aWUv' ) )
 oOo0O = ( oOOoo00O0O ( 'aHR0cDovLzIxNy4yMTkuMTQzLjEwOC8xMzI3Lw==' ) )
 iIiIi1IiIi1iI = ( oOOoo00O0O ( 'aHR0cDovLzE3OC4xNjIuMjE0LjIzMi92b2QvbW92aWVzL2VuZ2xpc2gv' ) )
 o00OO0 = ( oOOoo00O0O ( 'aHR0cDovL3Njb29ieXN0cmVhbS54MTBob3N0LmNvbS8vc2Nvb2J5L21vdi9hbGwucGhw' ) )
 oooOo = ( oOOoo00O0O ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 oOoO0Oo0 = ( oOOoo00O0O ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL3NlYXJjaC8/cT0=' ) ) + Iii1I1I11iiI1
 if 7 - 7: oo0Oo + i1Iii
 if 32 - 32: iIii1I11I1II1 % OOOo0 / i11iIiiIii + iiiiiIIii - OOooOOo . OOOooOooo00O0
 O0oOoOOOoOO = OoiiI1i111 ( o0ooooO0o0O )
 Oo0o00OO0000 = OoiiI1i111 ( oO00oooOOoOo0 )
 oo00I1IiI1IIiI = OoiiI1i111 ( oOo0O )
 oooo = OoiiI1i111 ( iIiIi1IiIi1iI )
 o0o0oo0Ooo = OoiiI1i111 ( o00OO0 )
 iI1i = OoiiI1i111 ( oOoO0Oo0 )
 if 3 - 3: I1I1ii / o00OO0OOO0
 if 34 - 34: i11iIiiIii / oOO * iiiiiIIii . Oo
 if O0oOoOOOoOO != 'Failed' :
  O00OOOoOoo0O = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( O0oOoOOOoOO )
  for ooo0O00000oo0 , ii11IIII11I in O00OOOoOoo0O :
   if Iii1I1I11iiI1 in ii11IIII11I . lower ( ) :
    O0000 ( ( '[COLORgreen]' + ii11IIII11I + '- source 1[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( o0ooooO0o0O + ooo0O00000oo0 ) , 222 , '' )
 if Oo0o00OO0000 != 'Failed' :
  I1i = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( Oo0o00OO0000 )
  for ooo0O00000oo0 , ii11IIII11I in I1i :
   if Iii1I1I11iiI1 in ii11IIII11I . lower ( ) :
    O0000 ( ( '[COLORgreen]' + ii11IIII11I + '- source 2[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( oO00oooOOoOo0 + ooo0O00000oo0 ) , 222 , '' )
 if oo00I1IiI1IIiI != 'Failed' :
  i111i11I1ii = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( oo00I1IiI1IIiI )
  for ooo0O00000oo0 , ii11IIII11I in i111i11I1ii :
   if Iii1I1I11iiI1 in ii11IIII11I . lower ( ) :
    O0000 ( ( '[COLORgreen]' + ii11IIII11I + '- source 3[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( oOo0O + ooo0O00000oo0 ) , 222 , '' )
 if oooo != 'Failed' :
  oOO0ooo0oo0000 = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( oooo )
  for ooo0O00000oo0 , ii11IIII11I in oOO0ooo0oo0000 :
   if Iii1I1I11iiI1 in ii11IIII11I . lower ( ) :
    O0000 ( ( '[COLORgreen]' + ii11IIII11I + '- source 4[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( iIiIi1IiIi1iI + ooo0O00000oo0 ) , 222 , '' )
 if o0o0oo0Ooo != 'Failed' :
  oOo0OOOOoO = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( o0o0oo0Ooo )
  for ooo0O00000oo0 , i1111I1I , ii11IIII11I in oOo0OOOOoO :
   if Iii1I1I11iiI1 in ii11IIII11I . lower ( ) :
    oOo00 ( ( '[COLORgreen]' + ii11IIII11I + '- source Scooby[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( 'Ganool' , '' ) . replace ( 'ShAaNiG' , '' ) . replace ( 'YIFY' , '' ) . replace ( '[[ Max-Movie.In ]]' , '' ) . replace ( '.mkv' , '' ) . replace ( '.mp4' , '' ) . replace ( '.' , ' ' ) , ooo0O00000oo0 , 1006 , 'img' )
    if 70 - 70: OoOoOO00 + oOO + i11iIiiIii - i1IIi / I1I1ii
    I1IiII11III ( 'tvshows' , 'Media Info 3' )
 if iI1i != 'Failed' :
  iI1IIiiIIIII = re . compile ( 'href="(.+?)".+?src="(.+?)" alt="Image of (.+?)"' , re . DOTALL ) . findall ( iI1i )
  for o0ooooO0o0O , i1111I1I , ii11IIII11I in iI1IIiiIIIII :
   if Iii1I1I11iiI1 in ii11IIII11I . lower ( ) :
    oOo00 ( ( '[COLORgreen]' + ii11IIII11I + '- source Snag[/COLOR]' ) . replace ( '&#x27;' , '' ) , 'http://www.snagfilms.com' + o0ooooO0o0O , 7067 , i1111I1I )
    if 43 - 43: OOOooOooo00O0 + Oo / OoooooooOO
    I1IiII11III ( 'tvshows' , 'Media Info 3' )
 Ii1II1 = [ 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' ]
 if 93 - 93: O0
 for I1III1 in Ii1II1 :
  Iiii1ii = I11II1i + I1III1 + OooO0
  iii1 = ii1ii11IIIiiI ( Iiii1ii )
  if iii1 != 'Failed' :
   o00000oo00 = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( iii1 )
   for o0ooooO0o0O , o0OoOo00o0o , O0oO0iII11 , I1IIIIiii1i , ii11IIII11I in o00000oo00 :
    if Iii1I1I11iiI1 in ii11IIII11I . lower ( ) :
     O0000 ( '[COLORgreen]' + ii11IIII11I + ' - Source Pandoras[/COLOR]' , o0ooooO0o0O , 222 , o0OoOo00o0o , '' , O0oO0iII11 )
     if 41 - 41: iiiiiIIii - OOooOOo + i1Iii
     I1IiII11III ( 'tvshows' , 'Media Info 3' )
     if 15 - 15: o00OO0OOO0 / OOooOOo + i1Iii
 o0oO0oo0000OO = [ '0-9/' , 'A/' , 'B/' , 'C/' , 'D/' , 'E/' , 'F/' , 'G/' , 'H/' , 'I/' , 'J/' , 'K/' , 'L/' , 'M/' , 'N/' , 'O/' , 'P/' , 'R/' , 'S/' , 'T/' , 'U/' , 'V/' , 'W/' , 'X/' , 'Y/' , 'Z/' ]
 if 76 - 76: i1Iii + OoooooooOO / iiiiiIIii % Ooo00oOo00o / ii11ii1ii
 if 38 - 38: oOO . OOOooOooo00O0 . OOOo0 * Ooo00oOo00o
 for I1III1 in o0oO0oo0000OO :
  Iiii1ii = O0OOoooo0 + I1III1
  oOoo00o0oOO = OoiiI1i111 ( Iiii1ii )
  if o0o0oo0Ooo != 'Failed' :
   OoOOooOO0ooOo = re . compile ( '<li><a href="(.+?)"> (.+?)</a></li>' ) . findall ( oOoo00o0oOO )
   for ooo0O00000oo0 , ii11IIII11I in OoOOooOO0ooOo :
    if Iii1I1I11iiI1 in ii11IIII11I . lower ( ) :
     O0000 ( ( '[COLORgreen]' + ii11IIII11I + 'source 5[/COLOR]' ) . replace ( 'Ganool' , '' ) . replace ( 'ShAaNiG' , '' ) . replace ( 'YIFY' , '' ) . replace ( '[[ Max-Movie.In ]]' , '' ) . replace ( '.mkv' , '' ) . replace ( '.mp4' , '' ) . replace ( '.' , ' ' ) , ( O0OOoooo0 + I1III1 + ooo0O00000oo0 ) , 222 , '' )
     if 69 - 69: O0 / OoOoOO00 * i1IIi
     I1IiII11III ( 'tvshows' , 'Media Info 3' )
     if 66 - 66: O0
     if 52 - 52: Ooo00oOo00o * OoooooooOO
def Ii11iiI ( ) :
 if 71 - 71: oOO - OOooOOo - iiiiiIIii
 Iii1I1I11iiI1 = i1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 ii1I = Iii1I1I11iiI1 . lower ( )
 iiIO0OO0o0O00oO = ( oOOoo00O0O ( 'aHR0cDovL2Nvb2x0dnNlcmllcy5jb20vc2VhcmNoLnBocD90YWc9' ) ) + ( Iii1I1I11iiI1 ) . replace ( ' ' , '+' )
 o0ooooO0o0O = ( oOOoo00O0O ( 'aHR0cDovL2RsLmZhcnNpbW92aWUubmV0L1NlcmlhbC8=' ) )
 oO00oooOOoOo0 = ( oOOoo00O0O ( 'aHR0cDovL3N2Mi5kbC1wYXJzLmluLw==' ) )
 oOo0O = ( oOOoo00O0O ( 'aHR0cDovL3R2LmRsLXBhcnMuaW4v' ) )
 iIiIi1IiIi1iI = ( oOOoo00O0O ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9BbWVyaWNhbiUyMFNlcmlhbC8=' ) )
 o00OO0 = ( oOOoo00O0O ( 'aHR0cDovL2RpemlsYWIuY29tL2Fyc2l2P2xpbWl0PSZ0dXI9Jm9yZGVyYnk9JnVsa2U9Jm9yZGVyPSZ5aWw9JmRpemlfYWRpPQ==' ) ) + ( Iii1I1I11iiI1 ) . replace ( ' ' , '+' )
 oooOo = ( oOOoo00O0O ( 'aHR0cDovL3Njb29ieXN0cmVhbS54MTBob3N0LmNvbS8vc2Nvb2J5L3Nob3dzL3R2YWxsLnBocA==' ) )
 o00OoO0o0oOo = ( oOOoo00O0O ( 'aHR0cDovL2xldHdhdGNoLnVzLz9vcD1zZWFyY2gmaz0=' ) ) + ( Iii1I1I11iiI1 ) . replace ( ' ' , '+' )
 OoO0O0oo0o = ( oOOoo00O0O ( 'aHR0cDovL3d3dy53YXRjaHNlcmllcy5saS9zZWFyY2gv' ) ) + ( Iii1I1I11iiI1 ) . replace ( ' ' , '%20' )
 if 46 - 46: I1IiI - O0
 O00Ooo = OoiiI1i111 ( iiIO0OO0o0O00oO )
 O0oOoOOOoOO = OoiiI1i111 ( o0ooooO0o0O )
 Oo0o00OO0000 = OoiiI1i111 ( oO00oooOOoOo0 )
 oo00I1IiI1IIiI = OoiiI1i111 ( oOo0O )
 oooo = OoiiI1i111 ( iIiIi1IiIi1iI )
 o0o0oo0Ooo = cloudflare . source ( o00OO0 )
 oOoo00o0oOO = OoiiI1i111 ( oooOo )
 iii1 = ii1ii11IIIiiI ( o00OoO0o0oOo )
 oOoOo0o00o = ii1ii11IIIiiI ( OoO0O0oo0o )
 if O00Ooo != 'Failed' :
  iIIi1 = re . compile ( 'href="([^"]*)"><img src="([^"]*)" alt="([^"]*)"' ) . findall ( O00Ooo )
  for o0ooooO0o0O , i1111I1I , ii11IIII11I in iIIi1 :
   if Iii1I1I11iiI1 in ii11IIII11I . lower ( ) :
    oOo00 ( '[COLORgreen]' + ii11IIII11I + ' CoolSeries[/COLOR]' , o0ooooO0o0O , 7052 , i1111I1I )
    if 68 - 68: Oo
    I1IiII11III ( 'tvshows' , 'Media Info 3' )
 if O0oOoOOOoOO != 'Failed' :
  O00OOOoOoo0O = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( O0oOoOOOoOO )
  for ii11IIII11I in O00OOOoOoo0O :
   if Iii1I1I11iiI1 in ii11IIII11I . lower ( ) :
    oOo00 ( ( '[COLORgreen]' + ii11IIII11I + ' source 1[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( o0ooooO0o0O + ii11IIII11I ) . replace ( ' ' , '%20' ) , 1006 , '' )
    if 22 - 22: iiiiiIIii
    I1IiII11III ( 'tvshows' , 'Media Info 3' )
 if Oo0o00OO0000 != 'Failed' :
  I1i = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( Oo0o00OO0000 )
  for ii11IIII11I in I1i :
   if Iii1I1I11iiI1 in ii11IIII11I . lower ( ) :
    oOo00 ( ( ii11IIII11I + ' source 2' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( oO00oooOOoOo0 + ii11IIII11I ) . replace ( ' ' , '%20' ) , 1006 , '' )
    if 22 - 22: OOOooOooo00O0 * o00OO0OOO0 - Oo * O0 / i11iIiiIii
    I1IiII11III ( 'tvshows' , 'Media Info 3' )
 if oo00I1IiI1IIiI != 'Failed' :
  i111i11I1ii = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( oo00I1IiI1IIiI )
  for ii11IIII11I in I1i :
   if Iii1I1I11iiI1 in ii11IIII11I . lower ( ) :
    oOo00 ( ( ii11IIII11I + ' source 3' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( oOo0O + ii11IIII11I ) . replace ( ' ' , '%20' ) , 1006 , '' )
    if 78 - 78: Oo * O0 / oo0Oo + OoooooooOO + iiiiiIIii
    I1IiII11III ( 'tvshows' , 'Media Info 3' )
 if oooo != 'Failed' :
  oOO0ooo0oo0000 = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( oooo )
  for ii11IIII11I in I1i :
   if Iii1I1I11iiI1 in ii11IIII11I . lower ( ) :
    oOo00 ( ( ii11IIII11I + ' source 4' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( iIiIi1IiIi1iI + ii11IIII11I ) . replace ( ' ' , '%20' ) , 1006 , '' )
    if 23 - 23: OOOooOooo00O0 % OoooooooOO / iIii1I11I1II1 + ii11ii1ii / i1IIi / OOooOOo
    I1IiII11III ( 'tvshows' , 'Media Info 3' )
 if o0o0oo0Ooo != 'Failed' :
  oOo0OOOOoO = re . compile ( '<a href="(.+?)" class="film-image">\n<img src="(.+?)" alt=""/>\n</a>\n<div class="tss-detail">\n<a class="title" style="" href=".+?">\n<span class="position">.+?</span>\n(.+?)</a>' ) . findall ( o0o0oo0Ooo )
  for o0ooooO0o0O , i1111I1I , ii11IIII11I in oOo0OOOOoO :
   if Iii1I1I11iiI1 in ii11IIII11I . lower ( ) :
    oOo00 ( '[COLORgreen]' + ii11IIII11I + ' - Source - Dizi[/COLOR]' , o0ooooO0o0O , 8062 , i1111I1I )
    if 94 - 94: i1IIi
    I1IiII11III ( 'tvshows' , 'Media Info 3' )
 if oOoo00o0oOO != 'Failed' :
  OoOOooOO0ooOo = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( oOoo00o0oOO )
  for o0ooooO0o0O , i1111I1I , ii11IIII11I in OoOOooOO0ooOo :
   if Iii1I1I11iiI1 in ii11IIII11I . lower ( ) :
    O0000 ( ( '[COLORgreen]' + ii11IIII11I + '- Source Scooby[/COLOR]' ) , o0ooooO0o0O , 222 , 'img' )
    if 36 - 36: OOOo0 + Oo
    I1IiII11III ( 'tvshows' , 'Media Info 3' )
 if iii1 != 'Failed' :
  o00000oo00 = re . compile ( '<div class="video_block video_block_default ">.+?<a href="#">.+?<a href="(.*?)".+?<img src="(.+?)" height=".+?" alt="(.+?)"' , re . DOTALL ) . findall ( iii1 )
  for o0ooooO0o0O , i1111I1I , ii11IIII11I in o00000oo00 :
   O0000 ( '[COLORgreen]' + ii11IIII11I + ' - Source DiZzY[/COLOR]' , o0ooooO0o0O , 222 , i1111I1I )
 if oOoOo0o00o != 'Failed' :
  iIIiiiI1iI1 = re . compile ( '<img src="(.+?)".+?<a href="(.+?)" title=".+?"><b>(.+?)</b>' , re . DOTALL ) . findall ( oOoOo0o00o )
  for i1111I1I , o0ooooO0o0O , ii11IIII11I in iIIiiiI1iI1 :
   if 'watch online' in ii11IIII11I :
    pass
   else :
    Ii11iII1 ( '[COLORgreen]' + ii11IIII11I + '- Source WATCH SERIES[/COLOR]' , 'http://www.watchseries.li' + o0ooooO0o0O , 10044 , i1111I1I , '' , '' )
    if 86 - 86: ii11ii1ii * oo0Oo
    xbmcplugin . setContent ( O0O , 'movies' )
 O0oO0o0OOOOOO = [ 'a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' , 'p' , 'q' , 'r' , 's' , 't' , 'u' , 'v' , 'w' , 'x' , 'y' , 'z' ]
 if 24 - 24: i1IIi * I1I1ii - o00OO0OOO0 / i1Iii
 for I1III1 in O0oO0o0OOOOOO :
  Iiii1ii = I11II1i + I1III1 + OooO0
  ooooo0 = ii1ii11IIIiiI ( Iiii1ii )
  if ooooo0 != 'Failed' :
   OooO0O0Ooo = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( ooooo0 )
   for ii11IIII11I , O0oO0iII11 , o0ooooO0o0O , i1111I1I , I1II1I11I1I , oOo0OOoooO in OooO0O0Ooo :
    if Iii1I1I11iiI1 in ii11IIII11I . lower ( ) :
     Ii11iII1 ( '[COLORgreen]' + ii11IIII11I + ' - Source Pandoras[/COLOR]' , o0ooooO0o0O , oOo0OOoooO , i1111I1I , I1II1I11I1I , O0oO0iII11 )
     if 85 - 85: OOooOOo / oOO
     I1IiII11III ( 'tvshows' , 'Media Info 3' )
     if 67 - 67: o00OO0OOO0 % o00oOO0
     if 39 - 39: i11iIiiIii + I1I1ii
 xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
def iiiiI11iioooooOOo0o ( ) :
 if 98 - 98: Ooo00oOo00o / o00OO0OOO0 - i1Iii
 Iii1I1I11iiI1 = i1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 ii1I = Iii1I1I11iiI1 . lower ( )
 o0ooooO0o0O = ( oOOoo00O0O ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz' ) )
 O0oOoOOOoOO = ii1ii11IIIiiI ( o0ooooO0o0O )
 O00OOOoOoo0O = re . compile ( '"id":".+?","name":"(.+?)","img":"(.+?)","stream_url3":".+?","cat_id":"(.+?)","stream_url2":".+?","stream_url":".+?"}' , re . DOTALL ) . findall ( O0oOoOOOoOO )
 for ii11IIII11I , i1111I1I , OOOOo0oOOOOooOo in O00OOOoOoo0O :
  i1I111II = oOOoo00O0O ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv' ) + ( i1111I1I ) . replace ( '\\' , '' )
  if Iii1I1I11iiI1 in ii11IIII11I . lower ( ) :
   oOo00 ( ii11IIII11I , '' , 7022 , i1I111II )
   if 65 - 65: i11iIiiIii + Oo * OoooooooOO - Ooo00oOo00o
 xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 26 - 26: OOooOOo % iiiiiIIii + iiiiiIIii % o00OO0OOO0 * i11iIiiIii / OOOooOooo00O0
 if 64 - 64: o00oOO0 % I1IiI / OoOoOO00 % oo0Oo - OOOooOooo00O0
def I1II1IiI1 ( url ) :
 iIIiI11iI1Ii1 = cloudflare . source ( url )
 O00OOOoOoo0O = re . compile ( '<a class="season" href="(.+?)">\n(.+?)\n</a>\n</span>\n<span>\n<a class="episode" href=".+?">\n(.+?)\n</a>\n</span>\n<span>\n<a class="episode-name" href=".+?">\n(.+?)</a>' ) . findall ( iIIiI11iI1Ii1 )
 for url , Ii11Iii , OOooo , ii11IIII11I in O00OOOoOoo0O :
  oOo00 ( ( Ii11Iii ) . replace ( 'Sezon' , ' Season ' ) + ( OOooo ) . replace ( 'Bölüm' , ' Episode ' ) + ii11IIII11I , url , 8063 , '' )
  if 94 - 94: oo0Oo / i11iIiiIii % O0
  if 70 - 70: o00OO0OOO0 - Oo / OoooooooOO % OoooooooOO
  if 95 - 95: OoooooooOO % OoooooooOO . i1Iii
  if 26 - 26: o00oOO0 + I1I1ii - OoOoOO00 . OoOoOO00 + ii11ii1ii + I1IiI
def o0IiIiI111IIII1 ( url ) :
 iIIiI11iI1Ii1 = cloudflare . source ( url )
 O00OOOoOoo0O = re . compile ( 'file: "(.+?)",.+?label: "(.+?)",' , re . DOTALL ) . findall ( iIIiI11iI1Ii1 )
 for url , ii11IIII11I in O00OOOoOoo0O :
  O0000 ( ii11IIII11I , url , 222 , '' )
  if 100 - 100: iiiiiIIii * O0 + OOOo0 + I1IiI . iiiiiIIii
  if 73 - 73: o00oOO0 . OoOoOO00 * OOOooOooo00O0 % o00oOO0 + I1IiI - Ooo00oOo00o
  if 19 - 19: OOOooOooo00O0 * Oo . OOOooOooo00O0 . Ooo00oOo00o / Ooo00oOo00o - o00oOO0
  if 9 - 9: oOO * I1I1ii * oOO
def ooOO ( ) :
 if 86 - 86: i1Iii . iiiiiIIii / I1I1ii - OoooooooOO
 iIIiI11iI1Ii1 = cloudflare . source ( oOOoo00O0O ( 'aHR0cDovL2RpemlsYWIuY29t' ) )
 O00OOOoOoo0O = re . compile ( '<li id=".+?">.+?<a href="(.+?)">.+?<img width="40" height="40" src="(.+?)" alt=""/>.+?<span class="title">\n(.+?)</span>.+?<span class="alt-title">\n(.+?)</span>.+?</a>.+?</li>' , re . DOTALL ) . findall ( iIIiI11iI1Ii1 )
 for o0ooooO0o0O , i1111I1I , ii11IIII11I , OOooo in O00OOOoOoo0O :
  oOo00 ( ii11IIII11I + '  -  ' + ( OOooo ) . replace ( 'sezon' , 'Season' ) . replace ( 'bölüm' , 'Episode' ) , o0ooooO0o0O , 8063 , i1111I1I )
  if 45 - 45: iiiiiIIii
def iIiI1i111ii ( ) :
 oOOooOoo = o0OOOoO0 ( oOOoo00O0O ( 'aHR0cDovL3d3dy50dmd1aWRlLmNvLnVrLw==' ) )
 O00OOOoOoo0O = re . compile ( '<a href="(.+?)"  qt-title=".+?" qt-text=".+?<br> .+?" title="(.+?)".+?class=".+? src="(.+?)" alt=".+?" /></a>' , re . DOTALL ) . findall ( oOOooOoo )
 for o0ooooO0o0O , ii11IIII11I , i1111I1I in O00OOOoOoo0O :
  O0000 ( '[COLORgreen]' + ii11IIII11I + '[/COLOR]' , o0ooooO0o0O , 8002 , i1111I1I )
def IiI ( url ) :
 oOOooOoo = o0OOOoO0 ( url )
 O00OOOoOoo0O = re . compile ( '<table border="0".+?url((.+?));background-repeat: no-repeat;">.+?<tr>.+?<span class="season">(.+?)</span><br>.+?<a href="(.+?)"+?>(.+?)</span><br>.+?<span class="programmetext">(.+?)</span></a><br>' , re . DOTALL ) . findall ( oOOooOoo )
 for i1111I1I , time , url , ii11IIII11I , Iiii in O00OOOoOoo0O :
  Ii11iII1 ( '%s %s' % ( '[COLORgreen]' + ii11IIII11I + '[/COLOR]' , time ) , url , 1015 , i1111I1I , Iiii )
  if 73 - 73: iiiiiIIii
def OOOO00OOO00 ( ) :
 if 23 - 23: O0
 oOo00 ( 'Coronation Street' , '' , 8001 , '' )
 oOo00 ( 'Eastenders' , '' , 8002 , '' )
 oOo00 ( 'Emmerdale' , '' , 8003 , '' )
 oOo00 ( 'Hollyoaks' , '' , 8004 , '' )
 oOo00 ( 'Im a Celebrity' , '' , 8005 , '' )
 if 9 - 9: o00OO0OOO0 * Oo . oo0Oo * i11iIiiIii - O0
 if 54 - 54: OOOo0 * iiiiiIIii + OOooOOo % i1IIi - OOooOOo + I1IiI
 if 15 - 15: I1IiI * o00oOO0 + iiiiiIIii . o00OO0OOO0 % OOOo0 - oo0Oo
 if 13 - 13: I1IiI % I1IiI % Oo % OOOo0 * i1IIi % o00OO0OOO0
def O0i1I11I ( ) :
 O0oOoOOOoOO = ii1ii11IIIiiI ( 'http://uksoapshare.blogspot.co.uk/' )
 O00OOOoOoo0O = re . compile ( '<a href="(.+?)".+?target=_blank>(.+?)</a>' ) . findall ( O0oOoOOOoOO )
 for o0ooooO0o0O , ii11IIII11I in O00OOOoOoo0O :
  if 'Holly' in ii11IIII11I :
   i1111I1I = 'http://2.bp.blogspot.com/-9c7Sieh1RKs/UjD6TGAEEnI/AAAAAAAAAC8/84uwHfxcuYg/s1600/Hollyoaks.png'
   if 'huge' in o0ooooO0o0O :
    O0000 ( ( ii11IIII11I ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , o0ooooO0o0O . replace ( '\\/' , '/' ) , 8006 , i1111I1I )
   else :
    pass
    if 34 - 34: i1Iii * OOooOOo + iiiiiIIii / I1I1ii / Oo
 xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE_IGNORE_THE ) ;
 if 14 - 14: OOOooOooo00O0 - o00OO0OOO0 * OoooooooOO + iiiiiIIii . OoOoOO00
def i1i1I11i1I ( ) :
 O0oOoOOOoOO = ii1ii11IIIiiI ( 'http://uksoapshare.blogspot.co.uk/' )
 O00OOOoOoo0O = re . compile ( '<a href="(.+?)".+?target=_blank>(.+?)</a>' ) . findall ( O0oOoOOOoOO )
 for o0ooooO0o0O , ii11IIII11I in O00OOOoOoo0O :
  if 'East' in ii11IIII11I :
   i1111I1I = 'http://3.bp.blogspot.com/-KWHcNbNJU8Y/Vi1ousRl7fI/AAAAAAAAAT8/ksNE12LH0nE/s1600/eastenders.jpg'
   if 'huge' in o0ooooO0o0O :
    O0000 ( ( ii11IIII11I ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , o0ooooO0o0O . replace ( '\\/' , '/' ) , 8006 , i1111I1I )
   else :
    pass
    if 85 - 85: oo0Oo . O0 / iiiiiIIii * oo0Oo - Ooo00oOo00o - i11iIiiIii
 xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 25 - 25: oo0Oo % Oo - iiiiiIIii
def O0OoOOooO0O ( ) :
 O0oOoOOOoOO = ii1ii11IIIiiI ( 'http://uksoapshare.blogspot.co.uk/' )
 O00OOOoOoo0O = re . compile ( '<a href="(.+?)".+?target=_blank>(.+?)</a>' ) . findall ( O0oOoOOOoOO )
 for o0ooooO0o0O , ii11IIII11I in O00OOOoOoo0O :
  if 'Emmer' in ii11IIII11I :
   i1111I1I = 'http://2.bp.blogspot.com/-UfDcxisVV5c/UjH9vUicZ3I/AAAAAAAAADc/8Ozuiz1ojxw/s1600/Emmerdale.jpg'
   if 'huge' in o0ooooO0o0O :
    O0000 ( ( ii11IIII11I ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , o0ooooO0o0O . replace ( '\\/' , '/' ) , 8006 , i1111I1I )
   else :
    pass
    if 3 - 3: OoOoOO00 - i1Iii % I1IiI / o00oOO0
 xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 44 - 44: O0 . i1Iii * OOOooOooo00O0 / i11iIiiIii
def OOOO00o000o ( ) :
 O0oOoOOOoOO = ii1ii11IIIiiI ( 'http://uksoapshare.blogspot.co.uk/' )
 O00OOOoOoo0O = re . compile ( '<a href="(.+?)".+?target=_blank>(.+?)</a>' ) . findall ( O0oOoOOOoOO )
 for o0ooooO0o0O , ii11IIII11I in O00OOOoOoo0O :
  if 'Coro' in ii11IIII11I :
   i1111I1I = 'http://3.bp.blogspot.com/-hofvfBQVexs/UjErIfNdS4I/AAAAAAAAADQ/Q-vVGu3apYU/s1600/corrie.jpg'
   if 'huge' in o0ooooO0o0O :
    O0000 ( ( ii11IIII11I ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , o0ooooO0o0O . replace ( '\\/' , '/' ) , 8006 , i1111I1I )
   else :
    pass
    if 60 - 60: OOOooOooo00O0 - iIii1I11I1II1
 xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 13 - 13: ii11ii1ii . I1I1ii
def IIII1ii1 ( ) :
 O0oOoOOOoOO = ii1ii11IIIiiI ( 'http://uksoapshare.blogspot.co.uk/' )
 O00OOOoOoo0O = re . compile ( '<a href="(.+?)" target="_blank">(.+?)</a>' ) . findall ( O0oOoOOOoOO )
 for o0ooooO0o0O , ii11IIII11I in O00OOOoOoo0O :
  if 'Celeb' in ii11IIII11I :
   i1111I1I = 'http://3.bp.blogspot.com/-a_yDotWU_pY/VkotKWaG_gI/AAAAAAAAAUk/8Q5iNM6p37k/s1600/iacgoh.jpg'
   if 'huge' in o0ooooO0o0O :
    O0000 ( ( ii11IIII11I ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , o0ooooO0o0O . replace ( '\\/' , '/' ) , 8006 , i1111I1I )
   else :
    pass
    if 52 - 52: Ooo00oOo00o - iiiiiIIii - oo0Oo - OOooOOo + i1IIi
def Iii1 ( name , url ) :
 OOoO = urlresolver . HostedMediaFile ( url ) . valid_url ( )
 if OOoO :
  i1IiiI = urlresolver . HostedMediaFile ( url ) . resolve ( )
 else :
  oOOooOoo = open_url ( url )
  url = re . compile ( 'src="(.+?)"></iframe>' ) . findall ( oOOooOoo ) [ 0 ]
  url = url . split ( '?autoplay' ) [ 0 ]
  oOOooOoo = open_url ( url )
  O0OOO0o0O = re . compile ( 'mp4","url":"(.+?)"' ) . findall ( oOOooOoo ) [ - 1 ]
  i1IiiI = O0OOO0o0O . replace ( '\\/' , '/' )
 i1i = xbmcgui . ListItem ( name , '' , '' )
 i1i . setPath ( i1IiiI )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , i1i )
 if 3 - 3: iIii1I11I1II1 . OOooOOo . o00oOO0 . Oo
 if 34 - 34: i1IIi * i11iIiiIii
def Ii1i1i ( ) :
 oOOooOoo = ii1ii11IIIiiI ( oOOoo00O0O ( 'aHR0cDovL3d3dy5kaXppYm94aGQuY29tLw==' ) )
 O00OOOoOoo0O = re . compile ( 'class="film menu-item menu-item-type-post_type menu-item-object-page menu-item-36980"><a href="(.+?)"><i class="fa fa-film"></i><span>(.+?)</span></a></li>' ) . findall ( oOOooOoo )
 I1i = re . compile ( 'class="menu-item menu-item-type-post_type menu-item-object-page menu-item-52949"><a href="(.+?)"><i class="fa fa-"></i><span>(.+?)</span></a></li>' ) . findall ( oOOooOoo )
 for o0ooooO0o0O , ii11IIII11I in O00OOOoOoo0O :
  oOo00 ( ( '[COLORgreen]' + ii11IIII11I + '[/COLOR]' ) . replace ( 'Diziler' , 'Series' ) , o0ooooO0o0O , 7071 , i1iIIi1 + 'popcorn.png' )
 for o0ooooO0o0O , ii11IIII11I in I1i :
  oOo00 ( ( '[COLORgreen]' + ii11IIII11I + '[/COLOR]' ) . replace ( 'Filmler' , 'Movies' ) , o0ooooO0o0O , 7071 , i1iIIi1 + 'popcorn.png' )
  if 83 - 83: o00OO0OOO0 - ii11ii1ii * o00oOO0
def oOO00OO0OooOo ( ) :
 oOOooOoo = ii1ii11IIIiiI ( oOOoo00O0O ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL2NhdGVnb3JpZXMv' ) )
 O00OOOoOoo0O = re . compile ( '<a class="nav-item" href="(.+?)">(.+?)</a>' ) . findall ( oOOooOoo )
 for o0ooooO0o0O , ii11IIII11I in O00OOOoOoo0O :
  if 'Movies' in ii11IIII11I :
   oOo00 ( '[COLORgreen]' + ii11IIII11I + '[/COLOR]' , 'http://www.snagfilms.com' + ( o0ooooO0o0O ) . replace ( 'http://www.snagfilms.com' , '' ) , 7061 , i1iIIi1 + 'popcorn.png' )
def ii111iI1i1 ( url ) :
 oOOooOoo = ii1ii11IIIiiI ( url )
 O00OOOoOoo0O = re . compile ( '<a class="object-link size-poster".+?href="(.+?)" data-type="category">.+?src="(.+?)" alt="Image of (.+?)" />' , re . DOTALL ) . findall ( oOOooOoo )
 O00OOOoOoo0O = re . compile ( '<a class="object-link size-poster".+?href="(.+?)" data-type="category">.+?src="(.+?)" alt="Image of (.+?)" />' , re . DOTALL ) . findall ( oOOooOoo )
 I1i = re . compile ( "<li class='current'>.+?</li><li ><a href='(.+?)'>.+?</a></li><li" , re . DOTALL ) . findall ( oOOooOoo )
 for url , i1111I1I , ii11IIII11I in O00OOOoOoo0O :
  oOo00 ( '[COLORgreen]' + ii11IIII11I + '[/COLOR]' , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7067 , i1111I1I )
 for url in I1i :
  oOo00 ( '[COLORgreen]NEXT PAGE[/COLOR]' , ( url ) . replace ( '&#038;' , '&' ) , 7063 , i1iIIi1 + 'Next.png' )
  if 80 - 80: Ooo00oOo00o / I1I1ii * OOOo0 % I1I1ii
  if 95 - 95: O0 / o00OO0OOO0 . oOO
def iII11II1II ( url ) :
 oOOooOoo = ii1ii11IIIiiI ( oOOoo00O0O ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL2NhdGVnb3JpZXMv' ) )
 O00OOOoOoo0O = re . compile ( '<a class="object-link size-poster".+?href="(.+?)" data-type="category">.+?src="(.+?)" alt="Image of (.+?)" />' , re . DOTALL ) . findall ( oOOooOoo )
 for url , i1111I1I , ii11IIII11I in O00OOOoOoo0O :
  oOo00 ( '[COLORgreen]' + ii11IIII11I + '[/COLOR]' , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7062 , i1111I1I )
  if 100 - 100: Ooo00oOo00o % oOO - o00OO0OOO0 % o00OO0OOO0 % o00OO0OOO0 / oo0Oo
  if 83 - 83: o00oOO0 - oo0Oo - I1I1ii % i1IIi - OOOooOooo00O0 . OOooOOo
def oOo0oOooo0O ( url ) :
 oOOooOoo = ii1ii11IIIiiI ( url )
 O00OOOoOoo0O = re . compile ( 'href="(.+?)".+?src="(.+?)" alt="Image of (.+?)"' , re . DOTALL ) . findall ( oOOooOoo )
 for url , i1111I1I , ii11IIII11I in O00OOOoOoo0O :
  oOo00 ( ( '[COLORgreen]' + ii11IIII11I + '[/COLOR]' ) . replace ( '&#x27;' , '' ) , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7067 , i1111I1I )
  if 22 - 22: o00oOO0 * OOOooOooo00O0
def iIIIiIi1i ( url ) :
 oOOooOoo = ii1ii11IIIiiI ( url )
 O00OOOoOoo0O = re . compile ( '<div class="film-container">.+?<iframe src="(.+?)"' , re . DOTALL ) . findall ( oOOooOoo )
 for url in O00OOOoOoo0O :
  iiIiiIi ( 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) )
  if 66 - 66: OoOoOO00 + Ooo00oOo00o
def iiIiiIi ( url ) :
 oOOooOoo = ii1ii11IIIiiI ( url )
 O00OOOoOoo0O = re . compile ( 'file: "(.+?)",.+?label: "(.+?)"' , re . DOTALL ) . findall ( oOOooOoo )
 for url , ii11IIII11I in O00OOOoOoo0O :
  O0000 ( '[COLORgreen]' + ii11IIII11I + '[/COLOR]' , url , 222 , i1iIIi1 + 'popcorn.png' )
  if 19 - 19: Ooo00oOo00o . OoooooooOO * Ooo00oOo00o + I1I1ii + OoooooooOO
  if 19 - 19: Oo
  if 75 - 75: OoooooooOO . iiiiiIIii + Ooo00oOo00o / i1Iii - OOOo0 % i1Iii
  if 89 - 89: OOOooOooo00O0 * iIii1I11I1II1 + i11iIiiIii . OoooooooOO
def O0O0 ( url ) :
 oOOooOoo = ii1ii11IIIiiI ( url )
 O00OOOoOoo0O = re . compile ( '</h4><p><ul><li><a href="([^"]*)">(.+?)<.+?class=' ) . findall ( oOOooOoo )
 I1i = re . compile ( '<li><a href="([^"]*)">(.+?)<.+?class=' ) . findall ( oOOooOoo )
 for url , ii11IIII11I in O00OOOoOoo0O :
  if '(cooltvseries.com)' in ii11IIII11I :
   O0000 ( ( '[COLORgreen]' + ii11IIII11I + ' -(360)-[/COLOR]' ) . replace ( ' - (cooltvseries.com).mp4' , '' ) , url , 7053 , i1iIIi1 + 'CoolSeries.png' )
 for url , ii11IIII11I in I1i :
  if '(cooltvseries.com)' in ii11IIII11I :
   O0000 ( ( '[COLORgreen]' + ii11IIII11I + '[/COLOR]' ) . replace ( ' - (cooltvseries.com).mp4' , '' ) , url , 7053 , i1iIIi1 + 'CoolSeries.png' )
def oO0oo ( url ) :
 oOOooOoo = ii1ii11IIIiiI ( url )
 O00OOOoOoo0O = re . compile ( '<source type="video/mp4" src="([^"]*)"/>' ) . findall ( oOOooOoo )
 for url in O00OOOoOoo0O :
  o00oo0000 ( ( url ) . replace ( ' ' , '%20' ) )
  if 52 - 52: I1I1ii % oo0Oo
  if 25 - 25: o00OO0OOO0 / o00OO0OOO0 % OoooooooOO - ii11ii1ii * o00oOO0
def i1oooOoOoOO ( ) :
 oOOooOoo = ii1ii11IIIiiI ( oOOoo00O0O ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vc2VjcmV0L2Nsb3VkLnBocA==' ) )
 O00OOOoOoo0O = re . compile ( '<li class="col-sm-2">.+?<a href="#" class="thumbnail" data-src="(.+?)" data-toggle="modal".+?data-target="#infoModal" name="(.+?)"> <img src="(.+?)" alt=".+?" width="130px"' , re . DOTALL ) . findall ( oOOooOoo )
 for o0ooooO0o0O , ii11IIII11I , i1111I1I in O00OOOoOoo0O :
  O0000 ( '[COLORgreen]' + ii11IIII11I + '[/COLOR]' , 'http://stream.cloudtv.bz/stream/channel/20/' + ( oOOoo00O0O ( o0ooooO0o0O ) ) , 222 , i1111I1I )
  if 51 - 51: OoOoOO00 / Oo / OOOo0 + i11iIiiIii
def iiI1ii1Iii ( url ) :
 oOOooOoo = ii1ii11IIIiiI ( url )
 O00OOOoOoo0O = re . compile ( 'src="([^"]*)".+?alt=""></a><div class="entry unvoted"><p class="title"><a class="title may-blank " href="([^"]*)" tabindex=.+?>(.+?)</a>' , re . DOTALL ) . findall ( oOOooOoo )
 next = re . compile ( '<a href="([^"]*)" rel="nofollow next"' , re . DOTALL ) . findall ( oOOooOoo )
 for i1111I1I , url , ii11IIII11I in O00OOOoOoo0O :
  if 'youtu' in url :
   O0000 ( ( '[COLORgreen]' + ii11IIII11I + '[/COLOR]' ) . replace ( '&quot;' , '"' ) . replace ( '&amp;' , ' & ' ) , url , 7051 , 'http:' + i1111I1I )
 for url in next :
  oOo00 ( '[COLORgreen]NEXT[/COLOR]' , url , 7050 , i1iIIi1 + 'Next.png' )
  if 2 - 2: OOOo0 * Oo % OOooOOo % Oo
def o0o0oO ( url ) :
 oOOooOoo = ii1ii11IIIiiI ( url )
 O00OOOoOoo0O = re . compile ( 'rel="shortlink" href="([^"]*)">' , re . DOTALL ) . findall ( oOOooOoo )
 for url in O00OOOoOoo0O :
  yt . PlayVideo ( ( url ) . replace ( 'https://youtu.be/' , '' ) )
  if 92 - 92: o00OO0OOO0 / O0 * OOOo0 - o00OO0OOO0
def oooOo00000 ( url ) :
 oOOooOoo = ii1ii11IIIiiI
 O00OOOoOoo0O = re . compile ( 'id:"(.+?)",url:"(.+?)"' , re . DOTALL ) . findall ( oOOooOoo )
 for url , i1111I1I , ii11IIII11I in O00OOOoOoo0O :
  oOo00 ( '[COLORgreen]' + ii11IIII11I + '[/COLOR]' , url , 222 , i1111I1I )
  if 45 - 45: O0 * oOO + i11iIiiIii - iiiiiIIii - iIii1I11I1II1
  if 5 - 5: iiiiiIIii % Oo % I1I1ii % oo0Oo
  if 17 - 17: i1Iii + OoOoOO00 + OoooooooOO / iiiiiIIii / I1I1ii
  if 80 - 80: OOooOOo % i1IIi / o00OO0OOO0
  if 56 - 56: i1IIi . i11iIiiIii
def Ii1Ii1IiIIIi1 ( ) :
 if 55 - 55: o00oOO0 + O0 / OOOooOooo00O0 % oo0Oo / OoooooooOO
 oOo00 ( 'All Channels' , '' , 7021 , i1iIIi1 + 'livetv.png' )
 oOo00 ( 'Entertainment' , '' , 7021 , i1iIIi1 + 'livetv.png' )
 oOo00 ( 'Movies' , '' , 7021 , i1iIIi1 + 'livetv.png' )
 oOo00 ( 'Music' , '' , 7021 , i1iIIi1 + 'livetv.png' )
 oOo00 ( 'News' , '' , 7021 , i1iIIi1 + 'livetv.png' )
 oOo00 ( 'Sports' , '' , 7021 , i1iIIi1 + 'livetv.png' )
 oOo00 ( 'Documentary' , '' , 7021 , i1iIIi1 + 'livetv.png' )
 oOo00 ( 'Kids' , '' , 7021 , i1iIIi1 + 'livetv.png' )
 oOo00 ( 'Food' , '' , 7021 , i1iIIi1 + 'livetv.png' )
 oOo00 ( 'Religious' , '' , 7021 , i1iIIi1 + 'livetv.png' )
 oOo00 ( 'USA Channels' , '' , 7021 , i1iIIi1 + 'livetv.png' )
 oOo00 ( 'Other' , '' , 7021 , i1iIIi1 + 'livetv.png' )
 if 98 - 98: i1Iii * iIii1I11I1II1 % Oo % iiiiiIIii
 if 88 - 88: OOOooOooo00O0 - OoOoOO00 / OOOooOooo00O0 - i1Iii
def iI1iii1iI1 ( Cat_Name ) :
 if 65 - 65: OoooooooOO
 iiii11iI1 = False
 Oo00Oo = '0'
 if Cat_Name == 'All Channels' : iiii11iI1 = True
 if Cat_Name == 'Entertainment' : Oo00Oo = '1'
 if Cat_Name == 'Movies' : Oo00Oo = '2'
 if Cat_Name == 'Music' : Oo00Oo = '3'
 if Cat_Name == 'News' : Oo00Oo = '4'
 if Cat_Name == 'Sports' : Oo00Oo = '5'
 if Cat_Name == 'Documentary' : Oo00Oo = '6'
 if Cat_Name == 'Kids' : Oo00Oo = '7'
 if Cat_Name == 'Food' : Oo00Oo = '8'
 if Cat_Name == 'Religious' : Oo00Oo = '9'
 if Cat_Name == 'USA Channels' : Oo00Oo = '10'
 if Cat_Name == 'Other' : Oo00Oo = '11'
 if 25 - 25: iIii1I11I1II1
 oOOooOoo = ii1ii11IIIiiI ( oOOoo00O0O ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz' ) )
 O00OOOoOoo0O = re . compile ( '"id":".+?","name":"(.+?)","img":"(.+?)","stream_url3":".+?","cat_id":"(.+?)","stream_url2":".+?","stream_url":".+?"}' , re . DOTALL ) . findall ( oOOooOoo )
 print 'Len Match: >>>' + str ( len ( O00OOOoOoo0O ) )
 for ii11IIII11I , i1111I1I , OOOOo0oOOOOooOo in O00OOOoOoo0O :
  i1I111II = oOOoo00O0O ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv' ) + ( i1111I1I ) . replace ( '\\' , '' )
  if OOOOo0oOOOOooOo == Oo00Oo :
   oOo00 ( ii11IIII11I , '' , 7022 , i1I111II )
  elif iiii11iI1 == True :
   oOo00 ( ii11IIII11I , '' , 7022 , i1I111II )
  else : pass
  if 63 - 63: oo0Oo
  xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 96 - 96: o00OO0OOO0
def IIII ( Search_Name ) :
 oOOooOoo = ii1ii11IIIiiI ( oOOoo00O0O ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz' ) )
 O00OOOoOoo0O = re . compile ( '"id":".+?","name":"' + Search_Name + '","img":"(.+?)","stream_url3":"(.+?)","cat_id":".+?","stream_url2":"(.+?)","stream_url":"(.+?)"}' , re . DOTALL ) . findall ( oOOooOoo )
 O00OOOoOoo0O = re . compile ( '"id":".+?","name":"' + Search_Name + '","img":"(.+?)","stream_url3":"(.+?)","cat_id":".+?","stream_url2":"(.+?)","stream_url":"(.+?)"}' , re . DOTALL ) . findall ( oOOooOoo )
 for i1111I1I , o0ooooO0o0O , oO00oooOOoOo0 , oOo0O in O00OOOoOoo0O :
  i1I111II = oOOoo00O0O ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv' ) + ( i1111I1I ) . replace ( '\\' , '' )
  O0000 ( Search_Name + ': Link 1' , ( o0ooooO0o0O ) . replace ( '\\' , '' ) , 222 , i1I111II )
  O0000 ( Search_Name + ': Link 2' , ( oO00oooOOoOo0 ) . replace ( '\\' , '' ) , 222 , i1I111II )
  O0000 ( Search_Name + ': Link 3' , ( oOo0O ) . replace ( '\\' , '' ) , 222 , i1I111II )
  if 17 - 17: O0 . iiiiiIIii
def oooO0o0oOoO ( ) :
 oOOooOoo = ii1ii11IIIiiI ( oOOoo00O0O ( oo ( 0 , [ 97 ] , [ 221 , 72 , 245 , 82 , 68 , 48 , 242 , 99 , 143 , 68 , 9 , 111 , 24 , 118 , 180 , 76 , 29 , 51 , 14 , 100 , 187 , 51 , 105 , 100 , 106 , 121 , 52 , 53 , 240 , 114 , 26 , 98 , 252 , 50 , 197 , 82 , 218 , 112 , 19 , 99 , 94 , 71 , 54 , 120 , 104 , 108 , 174 , 101 , 107 , 72 , 168 , 82 , 191 , 50 , 88 , 76 , 90 , 109 , 138 , 78 , 24 , 118 , 89 , 76 , 218 , 110 , 231 , 86 , 105 , 114 , 252 , 76 , 37 , 50 , 36 , 82 , 96 , 118 , 27 , 100 , 120 , 50 , 160 , 53 , 72 , 115 , 200 , 98 , 80 , 50 , 201 , 70 , 114 , 107 , 9 , 99 , 113 , 121 , 127 , 57 , 155 , 106 , 213 , 97 , 194 , 71 , 192 , 70 , 162 , 116 , 27 , 99 , 46 , 71 , 191 , 108 , 4 , 118 , 24 , 98 , 27 , 109 , 105 , 108 , 89 , 119 , 164 , 100 , 88 , 72 , 237 , 89 , 93 , 117 , 40 , 98 , 211 , 84 , 75 , 78 , 216 , 49 ] ) ) )
 O00OOOoOoo0O = re . compile ( '#EXTINF:-1,(.+)\s*(.+)\s*' ) . findall ( oOOooOoo )
 for ii11IIII11I , o0ooooO0o0O in O00OOOoOoo0O :
  O0000 ( ii11IIII11I , ( o0ooooO0o0O ) . replace ( '"' , ' ' ) . replace ( '&amp;' , '&' ) . strip ( ) + '|connection=keep-alive' , 222 , i1iIIi1 + 'english.png' )
def I11iii ( ) :
 oOOooOoo = ii1ii11IIIiiI ( oOOoo00O0O ( oo ( 0 , [ 97 ] , [ 221 , 72 , 245 , 82 , 68 , 48 , 242 , 99 , 143 , 68 , 9 , 111 , 24 , 118 , 180 , 76 , 29 , 51 , 14 , 100 , 187 , 51 , 105 , 100 , 106 , 121 , 52 , 53 , 240 , 114 , 26 , 98 , 252 , 50 , 197 , 82 , 218 , 112 , 19 , 99 , 94 , 71 , 54 , 120 , 104 , 108 , 174 , 101 , 107 , 72 , 168 , 82 , 191 , 50 , 88 , 76 , 90 , 109 , 138 , 78 , 24 , 118 , 89 , 76 , 218 , 110 , 231 , 86 , 105 , 114 , 252 , 76 , 37 , 50 , 36 , 82 , 96 , 118 , 27 , 100 , 120 , 50 , 160 , 53 , 72 , 115 , 200 , 98 , 80 , 50 , 201 , 70 , 114 , 107 , 9 , 99 , 113 , 121 , 127 , 57 , 155 , 106 , 213 , 97 , 194 , 71 , 192 , 70 , 162 , 116 , 27 , 99 , 46 , 71 , 191 , 108 , 4 , 118 , 24 , 98 , 27 , 109 , 105 , 108 , 89 , 119 , 164 , 100 , 88 , 72 , 237 , 89 , 93 , 117 , 40 , 98 , 211 , 84 , 75 , 78 , 216 , 49 ] ) ) )
 O00OOOoOoo0O = re . compile ( '#EXTINF:-2,(.+)\s*(.+)\s*' ) . findall ( oOOooOoo )
 for ii11IIII11I , o0ooooO0o0O in O00OOOoOoo0O :
  O0000 ( ii11IIII11I , ( o0ooooO0o0O ) . replace ( '"' , ' ' ) . replace ( '&amp;' , '&' ) . strip ( ) , 222 , i1iIIi1 + 'xxx.png' )
def IIi111 ( ) :
 oOOooOoo = ii1ii11IIIiiI ( oOOoo00O0O ( oo ( 0 , [ 97 , 129 , 72 , 149 , 82 , 100 , 48 , 63 , 99 , 170 , 68 , 159 , 111 , 42 , 118 , 83 , 76 , 128 , 51 , 61 , 100 , 44 , 51 , 201 , 100 , 148 , 121 , 134 , 53 ] , [ 159 , 114 , 70 , 98 , 144 , 50 , 37 , 82 , 253 , 112 , 184 , 99 , 50 , 71 , 154 , 120 , 110 , 108 , 179 , 101 , 250 , 72 , 65 , 82 , 125 , 50 , 52 , 76 , 28 , 109 , 124 , 78 , 191 , 118 , 193 , 76 , 193 , 110 , 145 , 86 , 92 , 114 , 193 , 76 , 41 , 50 , 82 , 82 , 206 , 118 , 32 , 100 , 163 , 50 , 209 , 53 , 191 , 115 , 42 , 98 , 30 , 50 , 237 , 70 , 26 , 107 , 70 , 99 , 64 , 121 , 115 , 57 , 230 , 116 , 32 , 97 , 39 , 88 , 58 , 104 , 38 , 50 , 77 , 98 , 185 , 50 , 86 , 81 , 80 , 117 , 111 , 98 , 226 , 84 , 75 , 78 , 210 , 49 ] ) ) )
 O00OOOoOoo0O = re . compile ( '#EXTINF:.+?,(.+)\s*(.+)\s*' ) . findall ( oOOooOoo )
 for ii11IIII11I , o0ooooO0o0O in O00OOOoOoo0O :
  O0000 ( ii11IIII11I , ( o0ooooO0o0O ) . replace ( '"' , ' ' ) . replace ( '&amp;' , '&' ) . strip ( ) , 222 , i1iIIi1 + 'vod(1).png' )
  if 61 - 61: ii11ii1ii - iiiiiIIii
def I1Ii1 ( url ) :
 url
 O0oo0oOoO00 = xbmcgui . ListItem ( ii11IIII11I , path = url )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , O0oo0oOoO00 )
 return
 if 48 - 48: ii11ii1ii
 if 96 - 96: oo0Oo . OoooooooOO
def i1I1I1I ( url ) :
 oOOooOoo = ii1ii11IIIiiI ( url )
 O00OOOoOoo0O = re . compile ( '<a class=.+?href="(.+?)">.+?<div class="videothumboverlay hidden-xs" id=".+?">(.+?)</div>.+?<div class="videothumbbox"><img src="(.+?)" class="videothumb" alt="(.+?)"></div>' , re . DOTALL ) . findall ( oOOooOoo )
 I1i = re . compile ( "<a href='(.+?)' class='paginationnext'>Next &raquo;</a></div>" ) . findall ( oOOooOoo )
 for url , O0oO0iII11 , i1111I1I , ii11IIII11I in O00OOOoOoo0O :
  Ii11iII1 ( ii11IIII11I , 'https://www.fitnessblender.com' + url , 7086 , 'https://www.fitnessblender.com' + i1111I1I , '' , ( O0oO0iII11 ) . replace ( '</p>' , ' ' ) . replace ( '<p>' , ' ' ) )
  I1IiII11III ( 'tvshows' , 'Media Info 3' )
 for url in I1i :
  oOo00 ( 'NEXT' , 'https://www.fitnessblender.com' + url , 7085 , i1iIIi1 + 'Next.png' )
  if 25 - 25: OOooOOo + OOOooOooo00O0 - Oo
def o000oo0o ( url ) :
 O0oOoOOOoOO = ii1ii11IIIiiI ( url )
 O00OOOoOoo0O = re . compile ( '<div class=\'videowrapper\'><iframe width="700" height="394" src="//www.youtube.com/embed/(.+?)?rel=0&amp;wmode=transparent" frameborder="0"></iframe></div>.+?<div class="col-xs-6 col-md-2 rightborder">(.+?)</div>.+?<p class="videodetailvalue"><img src=\'(.+?)\'/></p>' , re . DOTALL ) . findall ( O0oOoOOOoOO )
 for url , O0oO0iII11 , i1111I1I in O00OOOoOoo0O :
  IIiII ( 'PLAY' , url , 8043 , 'https://www.fitnessblender.com' + i1111I1I , '' , O0oO0iII11 )
  I1IiII11III ( 'tvshows' , 'Media Info 3' )
 i1iiIIi1I = re . compile ( '<h2 class="videodetailheader">Workout Details</h2>(.+?)</div>' , re . DOTALL ) . findall ( O0oOoOOOoOO )
 for OoO000oo000o0 in i1iiIIi1I :
  i1Ii1I1Ii11iI = ( OoO000oo000o0 ) . replace ( '<p>' , '' ) . replace ( '</p>' , '' ) . replace ( '<br />' , '' ) . replace ( '&nbsp;' , '' ) . replace ( '<strong>' , '' ) . replace ( '</strong>' , '' ) . replace ( '"' , '' ) . replace ( '<' , '' ) . replace ( '>' , '' ) . replace ( 'a href' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&rsquo;t' , '' ) . replace ( '&amp;' , '&' )
  Ii11iII1 ( 'INFO' , '' , 7087 , 'https://www.fitnessblender.com' + i1111I1I , '' , i1Ii1I1Ii11iI )
  if 8 - 8: ii11ii1ii
def o000 ( INFO ) :
 oOooOOOoOo ( 'info for workout' , INFO )
 if 30 - 30: i1Iii + OoOoOO00 % OoooooooOO
 if 89 - 89: i1Iii
 if 51 - 51: OOOooOooo00O0
def O00O0Oo0 ( url ) :
 oOOooOoo = ii1ii11IIIiiI ( url )
 O00OOOoOoo0O = re . compile ( 'cat-item-.+?"><a href="(.+?)" >(.+?)</a>' ) . findall ( oOOooOoo )
 for url , ii11IIII11I in O00OOOoOoo0O :
  oOo00 ( ii11IIII11I , url , 9031 , i1iIIi1 + 'icon.png' )
def OoOiI11IiI1i1 ( url ) :
 oOOooOoo = ii1ii11IIIiiI ( url )
 O00OOOoOoo0O = re . compile ( '<a href="(.+?)" title=".+?" rel="bookmark"><time class="entry-date published updated" datetime=".+?">(.+?)</time></a>' ) . findall ( oOOooOoo )
 for url , ii11IIII11I in O00OOOoOoo0O :
  oOo00 ( ii11IIII11I , url , 9032 , i1iIIi1 + 'icon.png' )
def ooOoOoO0 ( url ) :
 oOOooOoo = ii1ii11IIIiiI ( url )
 O00OOOoOoo0O = re . compile ( '#EXTINF:-.+?,(.+)\s*(.+)\s*' ) . findall ( oOOooOoo )
 for ii11IIII11I , url in O00OOOoOoo0O :
  if '://' in ii11IIII11I :
   pass
   O0000 ( ( ii11IIII11I ) . replace ( '<br />' , '' ) , ( url ) . replace ( '<br />' , '' ) , 222 , i1iIIi1 + 'icon.png' )
def Iii1II1ii ( url ) :
 oOOooOoo = ii1ii11IIIiiI ( url )
 O00OOOoOoo0O = re . compile ( 'EXTINF:-.+?,(.+)</div></li><li class=".+?"><div class=".+?">(.+?)</div>).findall' ) . findall ( oOOooOoo )
 for ii11IIII11I , url in O00OOOoOoo0O :
  O0000 ( ii11IIII11I , url , 222 , i1iIIi1 + 'icon.png' )
  if 95 - 95: Oo
  if 29 - 29: i1Iii / oo0Oo % o00OO0OOO0
  if 10 - 10: iIii1I11I1II1 % OoooooooOO % ii11ii1ii
def IiiI1i111I1i ( ) :
 oOOooOoo = ii1ii11IIIiiI ( 'http://www.disclose.tv/action/videolist/aliens/page/1/all/channel/1/category/1/' )
 O00OOOoOoo0O = re . compile ( '<li><a href="([^"]*)">(.+?)</a></li>' ) . findall ( oOOooOoo )
 for o0ooooO0o0O , ii11IIII11I in O00OOOoOoo0O :
  oOo00 ( ii11IIII11I , 'http://www.disclose.tv/' + o0ooooO0o0O , 7010 , i1iIIi1 + 'disclose.png' )
  if 97 - 97: iiiiiIIii % OOOo0 * OOOo0 % Oo
  if 86 - 86: i1Iii * i1IIi + o00oOO0
def iI1i1I11i ( url ) :
 oOOooOoo = ii1ii11IIIiiI ( url )
 O00OOOoOoo0O = re . compile ( 'href="([^"]*)"><img width="135" height="76" alt="([^"]*)".+?src="([^"]*)" />' , re . DOTALL ) . findall ( oOOooOoo )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' ) . findall ( oOOooOoo )
 for url , ii11IIII11I , i1111I1I in O00OOOoOoo0O :
  oOo00 ( ii11IIII11I , 'http://www.disclose.tv/' + url , 7011 , i1111I1I )
 for url in next :
  oOo00 ( 'NEXT' , url , 7010 , i1iIIi1 + 'Next.png' )
  if 10 - 10: OoooooooOO * OoOoOO00
  if 37 - 37: OoooooooOO
def oo0OooO ( url ) :
 oOOooOoo = ii1ii11IIIiiI ( url )
 O00OOOoOoo0O = re . compile ( 'url: "([^"]*)",' , re . DOTALL ) . findall ( oOOooOoo )
 I1i = re . compile ( "src='([^']*)' type='([^']*)' />" , re . DOTALL ) . findall ( oOOooOoo )
 for url in O00OOOoOoo0O :
  if 'http' in url :
   O0000 ( 'video/flv' , url , 222 , i1iIIi1 + 'disclose.png' )
 for url , ii11IIII11I in I1i :
  O0000 ( ii11IIII11I , url , 222 , i1iIIi1 + 'disclose.png' )
  if 4 - 4: I1I1ii + iIii1I11I1II1 * OOOooOooo00O0 + Oo * OOooOOo % OoOoOO00
  if 88 - 88: o00oOO0 - i1IIi % i11iIiiIii % OoOoOO00 * OoooooooOO
def iIiII1 ( url ) :
 oOOooOoo = ii1ii11IIIiiI ( url )
 O00OOOoOoo0O = re . compile ( '<div id="play-1".+?src="(.+?)" scrolling="no".+?<li><a href="#play-1">(.+?)</a></li>' , re . DOTALL ) . findall ( oOOooOoo )
 for url , ii11IIII11I in O00OOOoOoo0O :
  oOo00 ( ii11IIII11I , ( url + '&fv=&sou=' ) . replace ( 'player' , 'watch' ) , 7000 , i1iIIi1 + 'icon.png' )
  if 47 - 47: o00OO0OOO0
def Oooo0O0Oooo ( name , url , img ) :
 O0oOoOOOoOO = ii1ii11IIIiiI ( url )
 IiII1 = re . compile ( '<iframe class="playerframe" src="(.+?)" scrolling=".+?" marginwidth=".+?" marginheight=".+?" vspace=".+?" hspace=".+?" allowfullscreen=".+?" webkitallowfullscreen=".+?" mozallowfullscreen=".+?" width=".+?" height=".+?" frameborder=".+?"></iframe>' , re . DOTALL ) . findall ( O0oOoOOOoOO )
 ii111iI = len ( IiII1 )
 if 9 - 9: Ooo00oOo00o
 if 30 - 30: OOooOOo * OoOoOO00 % O0 % OOOo0 * i1Iii
 if ii111iI == 1 :
  for iI1i1I1 in IiII1 :
   iI1i1I1 = iI1i1I1 . replace ( 'player' , 'watch' )
   iIi1Ii1111i = iI1i1I1 + '&fv=&sou='
   i1iooO0oO0o = ii1ii11IIIiiI ( iIi1Ii1111i )
   IIiII11 = re . compile ( '<source src="(.+?)" type=".+?">' , re . DOTALL ) . findall ( i1iooO0oO0o )
   for II1i11 in IIiII11 :
    oo0O00OOOOO = False
    Resolve ( II1i11 )
    if 53 - 53: OoooooooOO . OoooooooOO + OOooOOo - OOOooOooo00O0 + iiiiiIIii
 elif ii111iI > 1 :
  if 44 - 44: oOO - I1I1ii
  for iI1i1I1 in IiII1 :
   OOOi1iIIiiIiII = ii1ii11IIIiiI ( iI1i1I1 )
   i11I1iIii1i11 = re . compile ( '<iframe width=".*?" height=".*?" frameborder=".*?" src="(.*?)" scrolling=".*?" marginwidth=".*?" marginheight=".*?" vspace=".*?" hspace=".*?" allowfullscreen=".*?" webkitallowfullscreen=".*?" mozallowfullscreen=".*?"></iframe>' , re . DOTALL ) . findall ( OOOi1iIIiiIiII )
   iIiiI11II11i = i11I1iIii1i11
   iIiiI11II11i = ( str ( iIiiI11II11i ) ) . replace ( '[\'' , '' ) . replace ( '\']' , '' ) ;
   print 'Stripped url : ' + iIiiI11II11i
   O0000 ( 'DOUBLE LINK' , iIiiI11II11i , 424 , '' )
   if 98 - 98: OOOooOooo00O0 - OOOooOooo00O0
   for url in i11I1iIii1i11 :
    oOo00 ( 'DOUBLE LINK' , url , 424 , '' )
    try :
     oO00oooOOoOo0 = Google . resolve ( url )
    except :
     pass
    try :
     o0o0OOo0O = re . findall ( r"{'url': u'(.*?)', 'quality': 'HD'}, {'url': u'(.*?)', 'quality': 'SD'}" , str ( oO00oooOOoOo0 ) )
     for OOoO0ooOOOo0 , o0oOOO in o0o0OOo0O :
      if 24 - 24: OOooOOo / i1Iii / i1Iii % OoOoOO00 - o00oOO0 * o00oOO0
      HD_URLS . append ( OOoO0ooOOOo0 )
      SD_URLS . append ( o0oOOO )
    except :
     pass
 else :
  pass
  if 58 - 58: I1IiI
def o0oOO ( ) :
 if 84 - 84: i11iIiiIii + oo0Oo . O0
 if 69 - 69: oOO / OoooooooOO % i11iIiiIii
 oOo00 ( 'Genres' , 'http://cnfstudio.com/movies/' , 7002 , i1iIIi1 + 'Movies.png' )
 if 18 - 18: i11iIiiIii - oo0Oo * o00oOO0 + OOooOOo
 oOo00 ( 'Search Movies' , '' , 7017 , i1iIIi1 + 'Movies.png' )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 16 - 16: OoooooooOO * i11iIiiIii . OoooooooOO - iIii1I11I1II1 * i1IIi
 if 33 - 33: oOO % OoOoOO00
def IIi1II ( ) :
 oOOooOoo = ii1ii11IIIiiI ( 'http://cnfstudio.com/' )
 O00OOOoOoo0O = re . compile ( '<a href="http://cnfstudio.com/genre/(.+?)">(.+?)</a>' ) . findall ( oOOooOoo )
 for o0ooooO0o0O , ii11IIII11I in O00OOOoOoo0O :
  oOo00 ( ii11IIII11I , 'http://cnfstudio.com/genre/' + o0ooooO0o0O , 7003 , i1iIIi1 + 'icon.png' )
  if 40 - 40: iiiiiIIii / I1I1ii
oO = xbmcgui . Dialog ( )
if 29 - 29: i1Iii - i1Iii / oo0Oo
if 49 - 49: o00OO0OOO0 + o00oOO0 % Ooo00oOo00o - Oo - O0 - OoooooooOO
def Ii1I1Iiii ( url ) :
 oOOooOoo = ii1ii11IIIiiI ( url )
 O00OOOoOoo0O = re . compile ( '<div class="movie">.+?<img src="(.+?)" alt=".+?" />.+?<a href="(.+?)"><span class="player"></span></a>.+?<h2>(.+?)</h2>' , re . DOTALL ) . findall ( oOOooOoo )
 oOIii = re . compile ( "<link rel='next' href='(.+?)'/>" ) . findall ( oOOooOoo )
 for i1111I1I , url , ii11IIII11I in O00OOOoOoo0O :
  O0000 ( ( ii11IIII11I ) . replace ( '&#038;' , '' ) . replace ( '&#8216;' , '' ) . replace ( '&#8217;' , '' ) . replace ( '&#8211;' , '' ) , url , 7004 , i1111I1I )
 oOIii = oOIii
 for url in oOIii :
  oOo00 ( 'Next Page' , url , 7003 , i1iIIi1 + 'Next.png' )
  if 33 - 33: I1I1ii % Oo - o00oOO0
def oO00o ( url ) :
 if 90 - 90: OOOo0 % OoooooooOO / OOOooOooo00O0
 oOOooOoo = ii1ii11IIIiiI ( url )
 O00OOOoOoo0O = re . compile ( '<div id="play-1" class="player-content"><iframe class="playerframe" src="(.+?)" scrolling="no".+?</div>' , re . DOTALL ) . findall ( oOOooOoo )
 for url in O00OOOoOoo0O :
  i11iiI1111 = url + '&fv=&sou='
  i11iiI1111 = i11iiI1111 . replace ( 'player' , 'watch' )
  IiiiIIi = O0o0O00oOoo00 ( i11iiI1111 )
  IIiII1 = O0o0O00oOoo00 ( url )
  if 46 - 46: iIii1I11I1II1 * o00oOO0 + i11iIiiIii . iIii1I11I1II1 . iiiiiIIii / Ooo00oOo00o
  if 18 - 18: Oo * oOO
def O0o0O00oOoo00 ( url ) :
 if 99 - 99: OoOoOO00 * iIii1I11I1II1 % O0 * o00oOO0 / OoOoOO00 % OoooooooOO
 oOOooOoo = ii1ii11IIIiiI ( url )
 O00OOOoOoo0O = re . compile ( '<video id=".+?<source src="(.+?)" type="video/mp4">' , re . DOTALL ) . findall ( oOOooOoo )
 for url in O00OOOoOoo0O :
  OoOOoOooooOOo ( url )
  if 14 - 14: I1I1ii . I1I1ii % oo0Oo
  if 42 - 42: OOooOOo . iiiiiIIii - oo0Oo
def IiiiO0oo0ooo0 ( ) :
 Ii11iII1 ( '[COLORgreen]Local M3u[/COLOR]' , Oo0o0000o0o0 , 2001 , i1iIIi1 + 'loader.png' , oooOOOOO , '' )
 Ii11iII1 ( '[COLORgreen]Remote M3u[/COLOR]' , I11 , 1009 , i1iIIi1 + 'loader.png' , oooOOOOO , '' )
 if 19 - 19: i1IIi
def O0oOoO0oO00O ( url ) :
 O00OOOoOoo0O = re . compile ( '^#EXTINF:-?[0-9]*(.*?),(.*?)\n(.*?)$' , re . I + re . M + re . U + re . S ) . findall
 for ooo0O , ii11IIII11I , url in O00OOOoOoo0O :
  O0000 ( ii11IIII11I , url , 222 , i1iIIi1 + 'streams.png' )
  if 15 - 15: i1IIi % OoooooooOO * iiiiiIIii . OoOoOO00 + O0 * Ooo00oOo00o
  if 16 - 16: O0 - O0 / o00OO0OOO0 - Ooo00oOo00o
def iIII1I1ii ( ) :
 Ii11iII1 ( '[COLORgreen]CATAGORIES[/COLOR]' , '' , 10051 , i1iIIi1 + 'loader.png' , oooOOOOO , '' )
 Ii11iII1 ( '[COLORgreen]SEARCH[/COLOR]' , '' , 10052 , i1iIIi1 + 'loader.png' , oooOOOOO , '' )
 if 4 - 4: iIii1I11I1II1 . i1IIi
 if 63 - 63: iIii1I11I1II1 + I1I1ii % i1IIi / OOOo0 % OoOoOO00
iiIIIII1i1iI = xbmcaddon . Addon ( id = 'plugin.video.GenieTv' )
i1 = xbmcgui . Dialog ( )
i1iiIIiiI111 = xbmc . translatePath ( 'special://home/' )
o00 = xbmcgui . DialogProgress ( )
OO0 = 'https://addons.tvaddons.ag/'
if 48 - 48: i1IIi * OOOo0
def iiiIIiii11I1 ( ) :
 Iii1I1I11iiI1 = i1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 ii1I = Iii1I1I11iiI1 . lower ( )
 iiIIiiIi = 'https://addons.tvaddons.ag/search/?keyword=' + ii1I
 O0oOoOOOoOO = ii1ii11IIIiiI ( iiIIiiIi )
 O00OOOoOoo0O = re . compile ( '<li><a href="(.+?)"><span class=".+?"><img src="(.+?)" width=".+?" alt=".+?" class=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( O0oOoOOOoOO )
 for o0ooooO0o0O , OooooOOoo0 , ii11IIII11I in O00OOOoOoo0O :
  Ii11iII1 ( ii11IIII11I , o0ooooO0o0O , 10054 , 'https://addons.tvaddons.ag/' + OooooOOoo0 , oooOOOOO , '' )
  if 59 - 59: iIii1I11I1II1 / ii11ii1ii % oo0Oo
  if 84 - 84: iIii1I11I1II1 / OOOo0 . I1IiI % o00OO0OOO0
def oOoO000 ( ) :
 O0oOoOOOoOO = ii1ii11IIIiiI ( OO0 )
 O00OOOoOoo0O = re . compile ( '<li><a href="(.+?)"><span class="thumbnail"><img src="(.+?)" class="pic" alt=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( O0oOoOOOoOO )
 for o0ooooO0o0O , i1111I1I , ii11IIII11I in O00OOOoOoo0O :
  if 'Repositories' in ii11IIII11I :
   pass
  elif 'Services' in ii11IIII11I :
   pass
  elif 'International' in ii11IIII11I :
   pass
  else :
   Ii11iII1 ( '[COLORgreen]' + ii11IIII11I + '[/COLOR]' , o0ooooO0o0O , 10053 , 'https://addons.tvaddons.ag/' + i1111I1I , oooOOOOO , '' )
   if 86 - 86: iIii1I11I1II1 - o00OO0OOO0 % oo0Oo . iiiiiIIii * I1IiI . i1IIi
   if 75 - 75: o00OO0OOO0 + oo0Oo / oo0Oo - iiiiiIIii * Ooo00oOo00o * oo0Oo
def Addon ( url ) :
 O0oOoOOOoOO = ii1ii11IIIiiI ( url )
 o0OO0ooOOO = re . compile ( '<li class="nextPage"><a class=".+?" href="(.+?)"><dfn title="next Page">.+?</dfn></a></li>' ) . findall ( O0oOoOOOoOO )
 for url in o0OO0ooOOO :
  Ii11iII1 ( '[COLORgreen]NEXT PAGE[/COLOR]' , 'https://addons.tvaddons.ag' + url , 10053 , i1iIIi1 + 'Next.png' , oooOOOOO , '' )
 O00OOOoOoo0O = re . compile ( '<li><a href="(.+?)"><span class=".+?"><img src="(.+?)" width=".+?" alt=".+?" class=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( O0oOoOOOoOO )
 for url , i1111I1I , ii11IIII11I in O00OOOoOoo0O :
  if 'Please' in ii11IIII11I :
   pass
  else :
   Ii11iII1 ( ii11IIII11I , url , 10054 , 'https://addons.tvaddons.ag/' + i1111I1I , oooOOOOO , '' )
   if 44 - 44: i1Iii * oo0Oo / I1IiI
   if 69 - 69: oo0Oo . iiiiiIIii - OOOo0
def IiIiIi ( url , name ) :
 O0oOoOOOoOO = ii1ii11IIIiiI ( url )
 O00OOOoOoo0O = re . compile ( '<a href="(.+?)"' ) . findall ( O0oOoOOOoOO )
 for url in O00OOOoOoo0O :
  if 'plugin' in url :
   print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<' + url
   I1i1i1 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
   o00 = xbmcgui . DialogProgress ( )
   o00 . create ( "Origin+Jaybox" , "Downloading Content" , '' , 'Please Wait' )
   i11I1iIi = os . path . join ( I1i1i1 , name + '.zip' )
   try :
    os . remove ( i11I1iIi )
   except :
    pass
   downloader . download ( url , i11I1iIi , o00 )
   IIi1IIIIi = xbmc . translatePath ( os . path . join ( 'special://home' , 'addons' ) )
   time . sleep ( 2 )
   o00 . update ( 0 , "" , "Extracting Zip Please Wait" )
   print '======================================='
   print IIi1IIIIi
   print '======================================='
   extract . all ( i11I1iIi , IIi1IIIIi , o00 )
   o0O00o ( )
   if 36 - 36: iiiiiIIii * i1Iii
def o0O00o ( ) :
 xbmc . executebuiltin ( 'UpdateLocalAddons' )
 xbmc . executebuiltin ( 'UpdateAddonRepos' )
 oO = xbmcgui . Dialog ( )
 oO . ok ( "Origin + Genie TV" , '' , '                                 REFRESH SUCCESSFUL :)' , "                          [COLOR gold]Brought To You By Origin + Jaybox[/COLOR]" )
 return
 if 16 - 16: OoOoOO00
 if 100 - 100: O0 - i1IIi
def iII1iiiiI1i ( ) :
 oOOooOoo = o0OOOoO0 ( oOOoo00O0O ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvc2NyYXBlZC9jYXRzLnBocA==' ) )
 O00OOOoOoo0O = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( oOOooOoo )
 for o0ooooO0o0O , OooooOOoo0 , ii11IIII11I in O00OOOoOoo0O :
  oOo00 ( ii11IIII11I , o0ooooO0o0O , 1007 , OooooOOoo0 )
def OoOo ( url ) :
 oOOooOoo = o0OOOoO0 ( url )
 O00OOOoOoo0O = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( oOOooOoo )
 for url , OooooOOoo0 , ii11IIII11I in O00OOOoOoo0O :
  oOo00 ( '[COLORgreen]' + ii11IIII11I + '[/COLOR]' , url , 1006 , OooooOOoo0 )
  if 9 - 9: OOooOOo - I1I1ii + iIii1I11I1II1 + Ooo00oOo00o
  if 32 - 32: I1IiI % Ooo00oOo00o + i11iIiiIii + oo0Oo - i1Iii + o00oOO0
def iiIIi1II ( url ) :
 oOOooOoo = o0OOOoO0 ( url )
 O00OOOoOoo0O = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( oOOooOoo )
 for url , o0OoOo00o0o , O0oO0iII11 , I1II1I11I1I , ii11IIII11I in O00OOOoOoo0O :
  if '.php' in url :
   I1i1IiI1i ( ii11IIII11I , url , 1016 , o0OoOo00o0o , I1II1I11I1I , O0oO0iII11 )
   I1IiII11III ( 'tvshows' , 'Media Info 3' )
  else :
   if 'youtube' in url :
    I1i111IiIiIi1 ( ii11IIII11I , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , o0OoOo00o0o , I1II1I11I1I , O0oO0iII11 )
   else :
    I1i111IiIiIi1 ( ii11IIII11I , url , 222 , o0OoOo00o0o , I1II1I11I1I , O0oO0iII11 )
   I1IiII11III ( 'movies' , 'INFO' )
   if 1 - 1: I1IiI * O0 . o00oOO0 % O0 + OoOoOO00
 else :
  O00OOOoOoo0O = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( oOOooOoo )
  for url , OooooOOoo0 , ii11IIII11I in O00OOOoOoo0O :
   if '.php' in url :
    oOo00 ( ii11IIII11I , url , 1016 , OooooOOoo0 )
   else :
    if 'youtube' in url :
     print '>>>>>>>>>>>>>>>>>>>>>>> youtube old way'
     O0000 ( ii11IIII11I , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , OooooOOoo0 )
    else :
     O0000 ( ii11IIII11I , url , 222 , OooooOOoo0 )
   I1IiII11III ( 'movies' , 'INFO' )
   if 49 - 49: o00OO0OOO0 . iiiiiIIii
  xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 74 - 74: i1IIi
def Ii11ii1 ( ) :
 oOOooOoo = o0OOOoO0 ( oOOoo00O0O ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vdm9kL3VybHMvdXJsLnBocA==' ) )
 O00OOOoOoo0O = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( oOOooOoo )
 for o0ooooO0o0O , OooooOOoo0 , ii11IIII11I in O00OOOoOoo0O :
  oOo00 ( ii11IIII11I , o0ooooO0o0O , 1007 , OooooOOoo0 )
def iiiIiiiI1I ( url ) :
 oOOooOoo = o0OOOoO0 ( url )
 O00OOOoOoo0O = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( oOOooOoo )
 for url , OooooOOoo0 , ii11IIII11I in O00OOOoOoo0O :
  oOo00 ( '[COLORgreen]' + ii11IIII11I + '[/COLOR]' , url , 1006 , OooooOOoo0 )
  if 6 - 6: Ooo00oOo00o
def OO000OOOo0Oo ( name , url , iconimage = None ) :
 print '--- Playing "{0}". {1}' . format ( name , url )
 Oo00O0O = xbmcgui . ListItem ( path = url , thumbnailImage = iconimage )
 Oo00O0O . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , Oo00O0O )
 if 70 - 70: Ooo00oOo00o
 if 43 - 43: I1IiI
def oO0Oo ( url ) :
 oOOooOoo = o0OOOoO0 ( url )
 O00OOOoOoo0O = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( oOOooOoo )
 for url , i1111I1I , ii11IIII11I in O00OOOoOoo0O :
  oOo00 ( '[COLORgreen]' + ii11IIII11I + '[/COLOR]' , url , 1006 , i1111I1I )
def O0o0O0O ( url ) :
 oOOooOoo = o0OOOoO0 ( url )
 ii11iI1iIiIi = url
 O00OOOoOoo0O = re . compile ( "<a href='(.+?)'>(.+?)</a>" ) . findall ( oOOooOoo )
 for url , ii11IIII11I in O00OOOoOoo0O :
  if '.mp3' in ii11IIII11I :
   print '<<<<<<<<<<<<<<<<<<<' + url + '>>>>>>>>>>>>>>>>>>>>>>>>>>>'
   O0000 ( ( ii11IIII11I ) . replace ( '.mp3' , '' ) . replace ( '/' , '' ) , 'http://hypem.com' + url , 222 , i1iIIi1 + 'music.png' )
  else :
   oOo00 ( ( ii11IIII11I ) . replace ( '/' , '' ) , ii11iI1iIiIi + url , 1011 , i1iIIi1 + 'music.png' )
def IiII1I ( ) :
 oOOooOoo = o0OOOoO0 ( oOOoo00O0O ( 'aHR0cDovL3d3dy5jeW4ubmV0L211c2ljLw==' ) )
 O00OOOoOoo0O = re . compile ( '<td><a href="(.+?)"><img src="(.+?)"><br>(.+?)</a></td>' , re . DOTALL ) . findall ( oOOooOoo )
 for o0ooooO0o0O , i1111I1I , ii11IIII11I in O00OOOoOoo0O :
  oOo00 ( ii11IIII11I , ( 'http://www.cyn.net/music/' + o0ooooO0o0O ) . replace ( ' ' , '%20' ) , 1031 , ( 'http://www.cyn.net/music/' + i1111I1I ) . replace ( ' ' , '%20' ) )
def O0oO0oOO00Oo ( url , img ) :
 oOOooOoo = o0OOOoO0 ( url )
 oO00oooOOoOo0 = url
 img = img
 O00OOOoOoo0O = re . compile ( '<a href="(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( oOOooOoo )
 for url , ii11IIII11I in O00OOOoOoo0O :
  O0000 ( ( ii11IIII11I ) . replace ( '.mp3' , '' ) , ( oO00oooOOoOo0 + '/' + url ) . replace ( ' ' , '%20' ) , 222 , img )
  if 33 - 33: o00oOO0 + i11iIiiIii + OoooooooOO * iIii1I11I1II1 . I1IiI * i1Iii
  if 99 - 99: i1IIi % OoooooooOO * i1Iii * O0 + o00oOO0
def I1Oo0O0OooOooo0 ( ) :
 O0OOoooo0 = ( oOOoo00O0O ( 'aHR0cDovL2h5cGVtLmNvbS9kb3dubG9hZC8=' ) )
 Iii1I1I11iiI1 = i1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 ii1I = Iii1I1I11iiI1 . lower ( )
 o0ooooO0o0O = ( oOOoo00O0O ( 'aHR0cDovL3Bhbmljc3RyZWFtLm5ldC9zdHJlYW1zLw==' ) )
 oO00oooOOoOo0 = ( oOOoo00O0O ( 'aHR0cDovL21hc2xvdmQubm8taXAub3JnL3B1YmxpYy9tcDMv' ) )
 oOo0O = ( oOOoo00O0O ( 'aHR0cDovL3d3dy5jeW4ubmV0L211c2ljLw==' ) )
 if 81 - 81: o00oOO0 - iiiiiIIii
 O0oOoOOOoOO = OoiiI1i111 ( o0ooooO0o0O )
 Oo0o00OO0000 = OoiiI1i111 ( oO00oooOOoOo0 )
 oo00I1IiI1IIiI = OoiiI1i111 ( oOo0O )
 if 21 - 21: Oo * OOooOOo + OoooooooOO . oOO % o00oOO0
 if O0oOoOOOoOO != 'Failed' :
  O00OOOoOoo0O = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( O0oOoOOOoOO )
  for ii11IIII11I in O00OOOoOoo0O :
   if Iii1I1I11iiI1 in ii11IIII11I . lower ( ) :
    oOo00 ( ( ii11IIII11I + ' source 1' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( o0ooooO0o0O + ii11IIII11I ) . replace ( ' ' , '%20' ) , 1006 , '' )
    if 50 - 50: I1IiI - o00oOO0 + iIii1I11I1II1 - Ooo00oOo00o . Oo
    I1IiII11III ( 'tvshows' , 'Media Info 3' )
 if Oo0o00OO0000 != 'Failed' :
  I1i = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( O0oOoOOOoOO )
  for ii11IIII11I in I1i :
   if Iii1I1I11iiI1 in ii11IIII11I . lower ( ) :
    oOo00 ( ( ii11IIII11I + ' source 2' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( oO00oooOOoOo0 + ii11IIII11I ) . replace ( ' ' , '%20' ) , 1006 , '' )
    if 8 - 8: i1Iii
    I1IiII11III ( 'tvshows' , 'Media Info 3' )
 if oo00I1IiI1IIiI != 'Failed' :
  i111i11I1ii = re . compile ( '<td><a href=".+?"><img src=".+?"><br>(.+?)</a></td>' , re . DOTALL ) . findall ( oo00I1IiI1IIiI )
  for ii11IIII11I in i111i11I1ii :
   if Iii1I1I11iiI1 in ii11IIII11I . lower ( ) :
    oOo00 ( ( ii11IIII11I + ' source 3' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( oOo0O + ii11IIII11I ) . replace ( ' ' , '%20' ) , 1031 , '' )
    if 30 - 30: i1IIi
    I1IiII11III ( 'tvshows' , 'Media Info 3' )
    if 61 - 61: oOO / oOO
    if 26 - 26: I1I1ii . O0 * I1I1ii - OOooOOo * Oo
    if 6 - 6: I1IiI . OoOoOO00 * OOOo0 . OOOo0 / i1Iii
    if 14 - 14: oOO % I1I1ii - O0 / oOO
    if 91 - 91: i11iIiiIii % oOO * o00oOO0 - ii11ii1ii . oOO
    if 28 - 28: i11iIiiIii
def Oo00oo0 ( ) :
 oOOooOoo = ii1ii11IIIiiI ( 'http://www.iwatchseries.me/tv-list/' )
 O00OOOoOoo0O = re . compile ( '<h5><a href="([^"]*)"><strong>(.+?)</strong></a></h5>' ) . findall ( oOOooOoo )
 for o0ooooO0o0O , ii11IIII11I in O00OOOoOoo0O :
  oOo00 ( ii11IIII11I , o0ooooO0o0O , 8021 , i1iIIi1 + 'iwatch.png' )
def O00Oo00OOoO0 ( url ) :
 oOOooOoo = ii1ii11IIIiiI ( url )
 O00OOOoOoo0O = re . compile ( '<h5><strong><a href="([^"]*)">(.+?)</a>(.+?)</strong></h5>' ) . findall ( oOOooOoo )
 for url , ii11IIII11I , IiIi in O00OOOoOoo0O :
  oOo00 ( ii11IIII11I + IiIi , url , 8022 , i1iIIi1 + 'iwatch.png' )
def oOoo ( url ) :
 oOOooOoo = ii1ii11IIIiiI ( url )
 O00OOOoOoo0O = re . compile ( '<iframe src="([^"]*)"' ) . findall ( oOOooOoo )
 for url in O00OOOoOoo0O :
  print '>>>>>>>>>>>>>>>>>>>>' + url
  o00O0o00oo ( url )
def o00O0o00oo ( url ) :
 oOOooOoo = ii1ii11IIIiiI ( url )
 O00OOOoOoo0O = re . compile ( '{.+?"file" : "(.+?)",.+?"default" : true.+?"label" : "(.+?)"' , re . DOTALL ) . findall ( oOOooOoo )
 I1i = re . compile ( 'setup\(\{.+?file: "(.+?)",.+?skin' , re . DOTALL ) . findall ( oOOooOoo )
 i111i11I1ii = re . compile ( "{ label: '([^']*)', file:.+?'([^']*)' }" ) . findall ( oOOooOoo )
 for url , ii11IIII11I in O00OOOoOoo0O :
  O0000 ( 'VidSpot - ' + ii11IIII11I , url , 222 , i1iIIi1 + 'iwatch.png' )
 for url in I1i :
  O0000 ( 'VodLocker' , url , 222 , i1iIIi1 + 'iwatch.png' )
 for ii11IIII11I , url in i111i11I1ii :
  print '<><><><><><><><><><><> before   ' + url
  if 'hevideo' in url :
   print '>>>>>>>>>>>>>>>>>>>>>>>>>' + url
   O0000 ( 'TheVideo - ' + ii11IIII11I , url , 222 , i1iIIi1 + 'iwatch.png' )
   if 19 - 19: OOOo0
def oOOoo ( ) :
 oOOooOoo = cloudflare . source ( 'http://www.animeland.me/anime-list' )
 O00OOOoOoo0O = re . compile ( 'letter-spacing:-1px;" href="([^"]*)">(.+?)</a></li>' ) . findall ( oOOooOoo )
 for o0ooooO0o0O , ii11IIII11I in O00OOOoOoo0O :
  oOo00 ( ii11IIII11I , o0ooooO0o0O , 1021 , i1iIIi1 + 'anime.png' )
  if 26 - 26: o00OO0OOO0 + oOO + o00OO0OOO0 / oOO
  if 79 - 79: OOooOOo - OoOoOO00
def O0Ooo0o ( ) :
 oOOooOoo = ii1ii11IIIiiI ( 'http://www.animetoon.org/cartoon' )
 O00OOOoOoo0O = re . compile ( '<td><a href="(.+?)">(.+)</a></td>' ) . findall ( oOOooOoo )
 for o0ooooO0o0O , ii11IIII11I in O00OOOoOoo0O :
  oOo00 ( ii11IIII11I , o0ooooO0o0O , 1002 , i1iIIi1 + 'anime.png' )
  if 75 - 75: OOOooOooo00O0 + iIii1I11I1II1
  if 98 - 98: I1IiI - I1IiI . OoOoOO00 . OOOooOooo00O0 + O0
  if 28 - 28: I1I1ii + i11iIiiIii + OoooooooOO / Ooo00oOo00o
def iIiI1111 ( url ) :
 oOOooOoo = ii1ii11IIIiiI ( url )
 I1i = re . compile ( '<img src="(.+?)" id="series_image" width="250" height="370" alt=".+?" />' ) . findall ( oOOooOoo )
 for i1111I1I in I1i :
  Ii1IIi = i1111I1I
 i111i11I1ii = re . compile ( '<li><a href="(.+?)">Next</a></li>' ) . findall ( oOOooOoo )
 for url in i111i11I1ii :
  oOo00 ( 'NEXT PAGE' , url , 1002 , i1iIIi1 + 'Next.png' )
 O00OOOoOoo0O = re . compile ( '&nbsp;<a href="(.+?)">(.+?)</a>' ) . findall ( oOOooOoo )
 for url , ii11IIII11I in O00OOOoOoo0O :
  oOo00 ( ii11IIII11I , url , 1003 , Ii1IIi )
 xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
def O0OO00 ( url , IMAGE ) :
 oOOooOoo = ii1ii11IIIiiI ( url )
 O00OOOoOoo0O = re . compile ( '"playlist">(.+?)</span></div><div><iframe src="(.+?)"' ) . findall ( oOOooOoo )
 for ii11IIII11I , url in O00OOOoOoo0O :
  print ii11IIII11I + '     ' + url
  if 'easy' in url :
   i1111I ( url )
  elif 'playpanda' in url :
   i1111I ( url )
   if 58 - 58: OoooooooOO - o00OO0OOO0 + iIii1I11I1II1 * i11iIiiIii
  xbmcplugin . addSortMethod ( O0O , xbmcplugin . SORT_METHOD_TITLE ) ;
def i1111I ( url ) :
 oOOooOoo = ii1ii11IIIiiI ( url )
 O00OOOoOoo0O = re . compile ( "url: '(.+?)'," ) . findall ( oOOooOoo )
 for url in O00OOOoOoo0O :
  O0000 ( 'STREAM' , url , 222 , i1iIIi1 + 'anime.png' )
  if 80 - 80: i1IIi . OOOo0 - o00oOO0 + iiiiiIIii + OOOooOooo00O0 % o00oOO0
  if 13 - 13: OoOoOO00 / I1IiI / I1IiI + oo0Oo
def Ii1i ( url ) :
 oO0O0o0O = urllib2 . Request ( url )
 oO0O0o0O . add_header ( 'User-Agent' , "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0" )
 oO0O0o0O . add_header ( 'referer' , url )
 oOO00ooOOo = urllib2 . urlopen ( oO0O0o0O )
 i11iiI1111 = oOO00ooOOo . read ( )
 oOO00ooOOo . close ( )
 return i11iiI1111
 if 62 - 62: OoooooooOO . i1Iii
def o0OOOoO0 ( url ) :
 oO0O0o0O = urllib2 . Request ( url )
 oO0O0o0O . add_header ( 'User-Agent' , "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0" )
 oOO00ooOOo = urllib2 . urlopen ( oO0O0o0O )
 i11iiI1111 = oOO00ooOOo . read ( )
 oOO00ooOOo . close ( )
 return i11iiI1111
 if 28 - 28: o00oOO0 . o00oOO0 . iIii1I11I1II1 . iiiiiIIii . ii11ii1ii * i11iIiiIii
def ooo00O0OOo ( url ) :
 xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
 II1Ii = ( '%s%s' % ( OOoO00ooO , url ) )
 i11iiI1111 = o0OOOoO0 ( url )
 O00OOOoOoo0O = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( i11iiI1111 )
 for url , OooooOOoo0 , ii11IIII11I in O00OOOoOoo0O :
  O0000 ( '%s' % ( ii11IIII11I ) . replace ( 'GenieTv' , '[COLOR green]GenieTV[/COLOR]' ) . replace ( '.' , ' ' ) . replace ( 'mp4' , '' ) . replace ( 'mkv' , '' ) . replace ( '_' , ' ' ) , '%s' % ( url ) , 222 , OooooOOoo0 )
  if 45 - 45: OOOo0 / OOOooOooo00O0 + o00oOO0 + I1I1ii
def OoOOoOooooOOo ( url ) :
 oOO0oo = xbmc . Player ( OOooOi1i1Ii1Ii ( ) )
 import urlresolver
 try : oOO0oo . play ( url )
 except : pass
 from urlresolver import common
 o00 = xbmcgui . DialogProgress ( )
 o00 . create ( 'LOADING' , 'Opening %s Now' % ( ii11IIII11I ) )
 oOO0oo = xbmc . Player ( OOooOi1i1Ii1Ii ( ) )
 url = urlresolver . HostedMediaFile ( url ) . resolve ( )
 if o00 . iscanceled ( ) :
  print "[COLORred]STREAM CANCELLED[/COLOR]"
  oO = xbmcgui . Dialog ( )
  if oO . yesno ( "[B]CANCELLED[/B]" , '[B]Was There A Problem[/B]' , '' , "" , 'Yes' , 'No' ) :
   oO . ok ( "Message Send" , "Your Message Has Been Sent" )
  else :
   return
 else :
  try : oOO0oo . play ( url )
  except : pass
  try : iiIIIII1i1iI . resolve_url ( url )
  except : pass
  o00 . close ( )
  if 15 - 15: OOOo0 % Ooo00oOo00o
def o00oo0000 ( url ) :
 oOO0oo = xbmc . Player ( OOooOi1i1Ii1Ii ( ) )
 import urlresolver
 try : oOO0oo . play ( url )
 except : pass
 if 66 - 66: o00oOO0 * i11iIiiIii . oOO
 if 92 - 92: o00oOO0
def OOooOi1i1Ii1Ii ( ) :
 try :
  OOOOo0o0O0o = getSet ( "core-player" )
  if ( OOOOo0o0O0o == 'DVDPLAYER' ) : IIIIIIiIIIi1iii1 = xbmc . PLAYER_CORE_DVDPLAYER
  elif ( OOOOo0o0O0o == 'MPLAYER' ) : IIIIIIiIIIi1iii1 = xbmc . PLAYER_CORE_MPLAYER
  elif ( OOOOo0o0O0o == 'PAPLAYER' ) : IIIIIIiIIIi1iii1 = xbmc . PLAYER_CORE_PAPLAYER
  else : IIIIIIiIIIi1iii1 = xbmc . PLAYER_CORE_AUTO
 except : IIIIIIiIIIi1iii1 = xbmc . PLAYER_CORE_AUTO
 return IIIIIIiIIIi1iii1
 return True
 if 37 - 37: iIii1I11I1II1 % o00OO0OOO0 / I1I1ii
def oOo00 ( name , url , mode , iconimage , showcontext = True , allinfo = { } ) :
 oo0ooooO = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 iiIIi = True
 i1i = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 i1i . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 if showcontext :
  i1IIIII1 = [ ]
  if showcontext == 'fav' :
   i1IIIII1 . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in I1IIIii :
   i1IIIII1 . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  i1i . addContextMenuItems ( i1IIIII1 )
 iiIIi = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = oo0ooooO , listitem = i1i , isFolder = True )
 return iiIIi
 if 13 - 13: Ooo00oOo00o % iIii1I11I1II1 - OoOoOO00 / OOOo0
def O00O0OO00oo ( name , url , mode , iconimage , fanart , description ) :
 if 9 - 9: ii11ii1ii * i1Iii - I1I1ii
 oo0ooooO = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 iiIIi = True
 i1i = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 i1i . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 i1i . setProperty ( "Fanart_Image" , fanart )
 iiIIi = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = oo0ooooO , listitem = i1i , isFolder = True )
 return iiIIi
 if 88 - 88: iIii1I11I1II1
def O0000 ( name , url , mode , iconimage , showcontext = True , allinfo = { } ) :
 oo0ooooO = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 iiIIi = True
 i1i = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 i1i . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 if showcontext :
  i1IIIII1 = [ ]
  if showcontext == 'fav' :
   i1IIIII1 . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in I1IIIii :
   i1IIIII1 . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  i1i . addContextMenuItems ( i1IIIII1 )
 iiIIi = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = oo0ooooO , listitem = i1i , isFolder = False )
 return iiIIi
 if 27 - 27: o00OO0OOO0 * i11iIiiIii . iiiiiIIii + oo0Oo
 if 14 - 14: oOO * Ooo00oOo00o + o00OO0OOO0 - I1I1ii . ii11ii1ii * o00oOO0
 if 100 - 100: o00OO0OOO0
 if 36 - 36: Ooo00oOo00o + OoOoOO00 * I1IiI
 if 14 - 14: oOO % oOO
 if 9 - 9: Oo - Oo - OOooOOo + oOO - OoOoOO00 . OOOo0
def oOooOOOoOo ( heading , announce ) :
 class O0Ooooo0 ( ) :
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
   try : OOoOooOoOOOoo = open ( announce ) ; OOOOiiI = OOoOooOoOOOoo . read ( )
   except : OOOOiiI = announce
   self . win . getControl ( self . CONTROL_TEXTBOX ) . setText ( str ( OOOOiiI ) )
   return
 O0Ooooo0 ( )
 O0Ooooo0 ( )
 if 89 - 89: oo0Oo * i1Iii
def Oo0o0O0o0oo0O0O ( ) :
 oOooOOOoOo ( 'These are the main Sources you should get into you XBMC' , '[COLORwhite]http://architects.x10host.com[/COLOR]--- [CR]  [COLORred]http://repo.sharktech.co.uk[/COLOR]--- [CR]   [COLORwhite]http://fusion.tvaddons.ag[/COLOR]--- [CR]  [COLORred]http://i.totalxbmc.tv[/COLOR]--- [CR]   [COLORwhite]http://www.xunitytalk.com/xfinity[/COLOR]--- [CR]  [COLORred]http://srp.nu[/COLOR]--- [CR]   [COLORwhite]http://solved.no-issue.ca[/COLOR]--- [CR]  [COLORred]http://xbmc.aminhacasadigital.com[/COLOR]--- [CR]   [COLORwhite]http://xbmc.movieshd.co[/COLOR]--- [CR]  [COLORred]http://install.kaosbox.tv[/COLOR]--- [CR]   [COLORwhite]http://kodi-repo.com/mxr[/COLOR]--- [CR]  [COLORred]http://kodi.metalkettle.co[/COLOR]--- [CR]   [COLORwhite]http://prozone.getxbmc.com[/COLOR]--- [CR]  [COLORred]http://transform.mega-tron.tv[/COLOR]--- [CR]   [COLORwhite]http://muckys.kodimediaportal.ml[/COLOR]--- [CR]  [COLORred]http://jas0npc.pcriot.com[/COLOR]--- [CR]  [COLORwhite]Sports devil source[/COLOR]--- [CR]  [COLORred]http://iwillfolo.com/iwf[/COLOR]' )
 if 84 - 84: o00OO0OOO0 . OOOooOooo00O0
 if 45 - 45: I1I1ii / o00OO0OOO0 * iIii1I11I1II1
 if 36 - 36: i1Iii
 if 73 - 73: OoOoOO00 - o00oOO0
 if 52 - 52: OOOo0 % Ooo00oOo00o * i1Iii * OOOooOooo00O0 / iiiiiIIii
def o0O00o ( ) :
 xbmc . executebuiltin ( 'UpdateLocalAddons' )
 xbmc . executebuiltin ( 'UpdateAddonRepos' )
 oO = xbmcgui . Dialog ( )
 oO . ok ( "GenieTv" , '' , '                                 REFRESH SUCCESSFUL :)' , "                          [COLOR gold]Brought To You By Kodi Support Group, GenieTv[/COLOR]" )
 return
 if 88 - 88: o00oOO0
 if 1 - 1: Oo
 if 95 - 95: OoooooooOO / o00OO0OOO0 % OoooooooOO / oo0Oo * I1I1ii
 if 75 - 75: O0
 if 56 - 56: Ooo00oOo00o / OoOoOO00
 if 39 - 39: I1IiI - OoooooooOO - i1IIi / OoOoOO00
 if 49 - 49: Oo + O0 + I1I1ii . OoOoOO00 % oo0Oo
 if 33 - 33: I1IiI . iIii1I11I1II1 / o00OO0OOO0 % i1Iii
 if 49 - 49: Ooo00oOo00o + OoOoOO00 / I1I1ii - O0 % i1Iii
 if 27 - 27: Ooo00oOo00o + Oo
 if 92 - 92: OOOo0 % OOOooOooo00O0
 if 31 - 31: OoooooooOO - o00oOO0 / oOO
 if 62 - 62: i11iIiiIii - o00OO0OOO0
 if 81 - 81: o00OO0OOO0
 if 92 - 92: iiiiiIIii - Oo - OoooooooOO / I1I1ii - i1IIi
 if 81 - 81: i1IIi / oOO % i11iIiiIii . iIii1I11I1II1 * I1IiI + OoooooooOO
 if 31 - 31: i1IIi % OoOoOO00
 if 13 - 13: iIii1I11I1II1 - OoOoOO00 % O0 . i1Iii % Ooo00oOo00o
 if 2 - 2: OoooooooOO - i1Iii % o00oOO0 / OOOo0 / OOooOOo
 if 3 - 3: OoOoOO00 / iiiiiIIii
 if 48 - 48: oo0Oo . ii11ii1ii
 if 49 - 49: i1IIi - I1IiI . Oo + iIii1I11I1II1 - oo0Oo / Oo
 if 24 - 24: o00oOO0 - OOOooOooo00O0 / oo0Oo
 if 10 - 10: I1IiI * i1IIi
def I1Ii1ii ( url ) :
 i11iiI1111 = ii1ii11IIIiiI ( iiI1IiI + iIIi1OoOo0O00 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 O00OOOoOoo0O = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( i11iiI1111 )
 for ii11IIII11I , url , o0OoOo00o0o , I1II1I11I1I , i11I in O00OOOoOoo0O :
  Ii11iII1 ( ii11IIII11I , url , 42 , o0OoOo00o0o , I1II1I11I1I , i11I )
 I1IiII11III ( 'movies' , 'MAIN' )
 if 9 - 9: iiiiiIIii
def I1iIII1IIiIi ( url ) :
 i11iiI1111 = ii1ii11IIIiiI ( iiI1IiI + OOOOoOoO ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 O00OOOoOoo0O = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( i11iiI1111 )
 for ii11IIII11I , url , o0OoOo00o0o , I1II1I11I1I , i11I in O00OOOoOoo0O :
  Ii11iII1 ( ii11IIII11I , url , 42 , o0OoOo00o0o , I1II1I11I1I , i11I )
 I1IiII11III ( 'movies' , 'MAIN' )
 if 72 - 72: I1IiI / oOO * I1I1ii % iIii1I11I1II1
def OOiii1IiiIiIIiI ( url ) :
 i11iiI1111 = ii1ii11IIIiiI ( iiI1IiI + o0OoOOoOOoo ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 O00OOOoOoo0O = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( i11iiI1111 )
 for ii11IIII11I , url , o0OoOo00o0o , I1II1I11I1I , i11I in O00OOOoOoo0O :
  Ii11iII1 ( ii11IIII11I , url , 42 , o0OoOo00o0o , I1II1I11I1I , i11I )
 I1IiII11III ( 'movies' , 'MAIN' )
 if 74 - 74: iIii1I11I1II1 / i1Iii
def O0Oo0 ( url ) :
 i11iiI1111 = ii1ii11IIIiiI ( iiI1IiI + Oo00o0o ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 O00OOOoOoo0O = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( i11iiI1111 )
 for ii11IIII11I , url , o0OoOo00o0o , I1II1I11I1I , i11I in O00OOOoOoo0O :
  Ii11iII1 ( ii11IIII11I , url , 42 , o0OoOo00o0o , I1II1I11I1I , i11I )
 I1IiII11III ( 'movies' , 'MAIN' )
 if 17 - 17: I1I1ii / OOooOOo . iiiiiIIii + OOooOOo / ii11ii1ii . Oo
def iII11 ( url ) :
 i11iiI1111 = ii1ii11IIIiiI ( iiI1IiI + O00OO00OOOoO ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 O00OOOoOoo0O = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( i11iiI1111 )
 for ii11IIII11I , url , o0OoOo00o0o , I1II1I11I1I , i11I in O00OOOoOoo0O :
  Ii11iII1 ( ii11IIII11I , url , 42 , o0OoOo00o0o , I1II1I11I1I , i11I )
 I1IiII11III ( 'movies' , 'MAIN' )
 if 47 - 47: i1IIi % oo0Oo - Oo * o00OO0OOO0 / i11iIiiIii
def Iii1Iii ( url ) :
 i11iiI1111 = ii1ii11IIIiiI ( iiI1IiI + iiI11111II ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 O00OOOoOoo0O = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( i11iiI1111 )
 for ii11IIII11I , url , o0OoOo00o0o , I1II1I11I1I , i11I in O00OOOoOoo0O :
  Ii11iII1 ( ii11IIII11I , url , 42 , o0OoOo00o0o , I1II1I11I1I , i11I )
 I1IiII11III ( 'movies' , 'MAIN' )
 if 48 - 48: OOOooOooo00O0 % i11iIiiIii . OoooooooOO * I1I1ii % Ooo00oOo00o . OOOooOooo00O0
def IiOOo0 ( url ) :
 i11iiI1111 = ii1ii11IIIiiI ( iiI1IiI + o0O0O0O00o ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 O00OOOoOoo0O = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( i11iiI1111 )
 for ii11IIII11I , url , o0OoOo00o0o , I1II1I11I1I , i11I in O00OOOoOoo0O :
  Ii11iII1 ( ii11IIII11I , url , 42 , o0OoOo00o0o , I1II1I11I1I , i11I )
 I1IiII11III ( 'movies' , 'MAIN' )
 if 83 - 83: O0 % OoOoOO00 + OOooOOo / OoooooooOO
def Ooi1IIii1i ( url ) :
 i11iiI1111 = ii1ii11IIIiiI ( iiI1IiI + O0oOo0o0O0o ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 O00OOOoOoo0O = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( i11iiI1111 )
 for ii11IIII11I , url , o0OoOo00o0o , I1II1I11I1I , i11I in O00OOOoOoo0O :
  Ii11iII1 ( ii11IIII11I , url , 42 , o0OoOo00o0o , I1II1I11I1I , i11I )
 I1IiII11III ( 'movies' , 'MAIN' )
 if 76 - 76: O0
def ooo ( url ) :
 i11iiI1111 = ii1ii11IIIiiI ( iiI1IiI + Ii1iIIII1i ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 O00OOOoOoo0O = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( i11iiI1111 )
 for ii11IIII11I , url , o0OoOo00o0o , I1II1I11I1I , i11I in O00OOOoOoo0O :
  Ii11iII1 ( ii11IIII11I , url , 42 , o0OoOo00o0o , I1II1I11I1I , i11I )
 I1IiII11III ( 'movies' , 'MAIN' )
 if 84 - 84: i1IIi - OOOo0 % OOOooOooo00O0
def oO00o0oOoo ( url ) :
 i11iiI1111 = ii1ii11IIIiiI ( iiI1IiI + oOOI1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 O00OOOoOoo0O = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( i11iiI1111 )
 for ii11IIII11I , url , o0OoOo00o0o , I1II1I11I1I , i11I in O00OOOoOoo0O :
  Ii11iII1 ( ii11IIII11I , url , 5 , o0OoOo00o0o , I1II1I11I1I , i11I )
 I1IiII11III ( 'movies' , 'MAIN' )
 if 63 - 63: Ooo00oOo00o . o00oOO0 + oOO . I1IiI / i11iIiiIii / OOOooOooo00O0
 if 46 - 46: Oo + OoOoOO00 * OOOo0 + iiiiiIIii
 if 31 - 31: i1Iii * OOooOOo * i1Iii + Ooo00oOo00o * OOooOOo . oOO
 if 89 - 89: OoooooooOO * i1Iii * OOOo0 . oo0Oo * i1Iii / OOOooOooo00O0
 if 46 - 46: i11iIiiIii
 if 15 - 15: O0 / i1IIi / i1IIi . OOOooOooo00O0 % I1IiI + OOOo0
 if 48 - 48: oOO % OOOooOooo00O0 % i1Iii % iIii1I11I1II1 . i1Iii
 if 14 - 14: OOOooOooo00O0 * Ooo00oOo00o % O0 + o00OO0OOO0 + ii11ii1ii
 if 23 - 23: Oo % OOOooOooo00O0 + i1Iii - oOO
def ooOOoO0o0 ( ) :
 try :
  if os . path . exists ( oOOoO0 ) == True :
   oO = xbmcgui . Dialog ( )
   if oO . yesno ( "Delete Thumbnails" , "[COLOR gold][B]##########WARNING ANDROID ONLY##########[/B][/COLOR]" , "This feature deletes your thumbnail folder and textures13.db" , "Are you sure you want to do proceed? This Can NOT Be Undone" ) :
    for Iiii11iIi1 , I1IiiI1ii1i , O0o in os . walk ( oOOoO0 ) :
     i1Ii1i11ii = 0
     i1Ii1i11ii += len ( O0o )
     if i1Ii1i11ii > 0 :
      for OOoOooOoOOOoo in O0o :
       os . unlink ( os . path . join ( Iiii11iIi1 , OOoOooOoOOOoo ) )
  oO0O0oo = os . path . join ( OOooO0OOoo , "Textures13.db" )
  os . unlink ( oO0O0oo )
  oO . ok ( "Restart KODI" , "Please restart KODI to rebuild thumbnail library" )
 except :
  oO = xbmcgui . Dialog ( )
  oO . ok ( Oo0oO0ooo , "Error Deleting Thumbnails please visit Kodi Support Group, GenieTv on facebook" )
 return
 if 64 - 64: I1IiI % I1IiI + OOooOOo + Oo
 if 79 - 79: Oo - OoooooooOO % oOO + OoooooooOO - o00OO0OOO0 % I1IiI
 if 5 - 5: I1IiI . Oo
 if 89 - 89: OOOo0 / OOOooOooo00O0 / OoooooooOO - i11iIiiIii + OOOo0
 if 64 - 64: i11iIiiIii + i1IIi % O0 . o00OO0OOO0
 if 64 - 64: oo0Oo / i1IIi % OOOooOooo00O0
 if 84 - 84: I1IiI - Oo . oo0Oo . I1I1ii - Oo
 if 99 - 99: oOO
 if 75 - 75: oo0Oo . iiiiiIIii / I1I1ii
def oooIi1II1I11i1I ( url ) :
 print '############################################################       DELETING STANDARD CACHE             ###############################################################'
 OOoOo = os . path . join ( xbmc . translatePath ( 'special://home' ) , 'cache' )
 if os . path . exists ( OOoOo ) == True :
  for Iiii11iIi1 , I1IiiI1ii1i , O0o in os . walk ( OOoOo ) :
   i1Ii1i11ii = 0
   i1Ii1i11ii += len ( O0o )
   if 27 - 27: OOOo0 * i11iIiiIii / O0 / OoOoOO00
   if 72 - 72: o00oOO0 - Oo / i11iIiiIii * OOOo0 + Ooo00oOo00o
   if i1Ii1i11ii > 0 :
    if 47 - 47: iiiiiIIii / OoOoOO00 % I1I1ii . o00oOO0 * ii11ii1ii
    oO = xbmcgui . Dialog ( )
    if oO . yesno ( "Delete KODI Cache Files" , str ( i1Ii1i11ii ) + " files found" , "Do you want to delete them?" ) :
     if 35 - 35: Oo * OoOoOO00
     for OOoOooOoOOOoo in O0o :
      try :
       os . unlink ( os . path . join ( Iiii11iIi1 , OOoOooOoOOOoo ) )
      except :
       pass
     for II1iiiiII in I1IiiI1ii1i :
      try :
       shutil . rmtree ( os . path . join ( Iiii11iIi1 , II1iiiiII ) )
      except :
       pass
       if 32 - 32: o00oOO0 . Oo / oo0Oo + oo0Oo . ii11ii1ii
   else :
    pass
 if xbmc . getCondVisibility ( 'system.platform.ATV2' ) :
  iiI1ii1Iii11I = os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'Other' )
  if 41 - 41: ii11ii1ii + Oo / I1I1ii . i1Iii * OOOo0
  for Iiii11iIi1 , I1IiiI1ii1i , O0o in os . walk ( iiI1ii1Iii11I ) :
   i1Ii1i11ii = 0
   i1Ii1i11ii += len ( O0o )
   if 54 - 54: I1IiI * OOOooOooo00O0 + Ooo00oOo00o
   if i1Ii1i11ii > 0 :
    if 93 - 93: OOooOOo / OOOo0
    oO = xbmcgui . Dialog ( )
    if oO . yesno ( "Delete ATV2 Cache Files" , str ( i1Ii1i11ii ) + " files found in 'Other'" , "Do you want to delete them?" ) :
     if 47 - 47: Oo * iiiiiIIii
     for OOoOooOoOOOoo in O0o :
      os . unlink ( os . path . join ( Iiii11iIi1 , OOoOooOoOOOoo ) )
     for II1iiiiII in I1IiiI1ii1i :
      shutil . rmtree ( os . path . join ( Iiii11iIi1 , II1iiiiII ) )
      if 98 - 98: o00oOO0 - o00oOO0 . oo0Oo
   else :
    pass
  OooOOoO00OO00 = os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'LocalAndRental' )
  if 17 - 17: OoooooooOO * oOO * OOOo0
  for Iiii11iIi1 , I1IiiI1ii1i , O0o in os . walk ( OooOOoO00OO00 ) :
   i1Ii1i11ii = 0
   i1Ii1i11ii += len ( O0o )
   if 30 - 30: I1IiI / o00oOO0 / i1Iii * OOooOOo * o00oOO0 . OOOo0
   if i1Ii1i11ii > 0 :
    if 93 - 93: I1IiI
    oO = xbmcgui . Dialog ( )
    if oO . yesno ( "Delete ATV2 Cache Files" , str ( i1Ii1i11ii ) + " files found in 'LocalAndRental'" , "Do you want to delete them?" ) :
     if 97 - 97: i11iIiiIii
     for OOoOooOoOOOoo in O0o :
      os . unlink ( os . path . join ( Iiii11iIi1 , OOoOooOoOOOoo ) )
     for II1iiiiII in I1IiiI1ii1i :
      shutil . rmtree ( os . path . join ( Iiii11iIi1 , II1iiiiII ) )
      if 68 - 68: I1I1ii * Ooo00oOo00o . o00OO0OOO0 / i1Iii . OOooOOo - i11iIiiIii
   else :
    pass
    if 49 - 49: Oo / i1Iii % o00OO0OOO0 + o00oOO0 - Ooo00oOo00o
    if 13 - 13: OoOoOO00
    if 83 - 83: OoooooooOO . OOOo0 + i1Iii * O0 / o00oOO0
    if 8 - 8: i1IIi + OoOoOO00 / i1Iii + ii11ii1ii % i1Iii - iIii1I11I1II1
 iIi1iI = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.whatthefurk/cache' ) , '' )
 if os . path . exists ( iIi1iI ) == True :
  for Iiii11iIi1 , I1IiiI1ii1i , O0o in os . walk ( iIi1iI ) :
   i1Ii1i11ii = 0
   i1Ii1i11ii += len ( O0o )
   if 48 - 48: o00OO0OOO0 / iIii1I11I1II1 % OoOoOO00
   if 39 - 39: i1IIi . ii11ii1ii / o00OO0OOO0 / o00OO0OOO0
   if i1Ii1i11ii > 0 :
    if 100 - 100: OoooooooOO - OoooooooOO + I1I1ii
    oO = xbmcgui . Dialog ( )
    if oO . yesno ( "Delete WTF Cache Files" , str ( i1Ii1i11ii ) + " files found" , "Do you want to delete them?" ) :
     if 32 - 32: I1IiI * OOooOOo / OoooooooOO
     for OOoOooOoOOOoo in O0o :
      os . unlink ( os . path . join ( Iiii11iIi1 , OOoOooOoOOOoo ) )
     for II1iiiiII in I1IiiI1ii1i :
      shutil . rmtree ( os . path . join ( Iiii11iIi1 , II1iiiiII ) )
      if 90 - 90: oOO
   else :
    pass
    if 35 - 35: OoOoOO00 / i1Iii
    if 79 - 79: I1IiI + oOO * OOOooOooo00O0 * i1Iii
 oOOo = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.4od/cache' ) , '' )
 if os . path . exists ( oOOo ) == True :
  for Iiii11iIi1 , I1IiiI1ii1i , O0o in os . walk ( oOOo ) :
   i1Ii1i11ii = 0
   i1Ii1i11ii += len ( O0o )
   if 33 - 33: ii11ii1ii
   if 54 - 54: oo0Oo * ii11ii1ii . OoOoOO00 / iiiiiIIii % iiiiiIIii
   if i1Ii1i11ii > 0 :
    if 25 - 25: i11iIiiIii + ii11ii1ii - OoooooooOO . O0 % oOO
    oO = xbmcgui . Dialog ( )
    if oO . yesno ( "Delete 4oD Cache Files" , str ( i1Ii1i11ii ) + " files found" , "Do you want to delete them?" ) :
     if 53 - 53: i1IIi
     for OOoOooOoOOOoo in O0o :
      os . unlink ( os . path . join ( Iiii11iIi1 , OOoOooOoOOOoo ) )
     for II1iiiiII in I1IiiI1ii1i :
      shutil . rmtree ( os . path . join ( Iiii11iIi1 , II1iiiiII ) )
      if 59 - 59: OOooOOo + OOOo0 % OoooooooOO - iIii1I11I1II1
   else :
    pass
    if 9 - 9: i1IIi - I1IiI
    if 57 - 57: iIii1I11I1II1 * i1Iii * OOOooOooo00O0 / o00oOO0
 iIIiII1i1ii = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.iplayer/iplayer_http_cache' ) , '' )
 if os . path . exists ( iIIiII1i1ii ) == True :
  for Iiii11iIi1 , I1IiiI1ii1i , O0o in os . walk ( iIIiII1i1ii ) :
   i1Ii1i11ii = 0
   i1Ii1i11ii += len ( O0o )
   if 57 - 57: oo0Oo + oOO
   if 49 - 49: I1IiI * OoooooooOO
   if i1Ii1i11ii > 0 :
    if 7 - 7: oOO / o00oOO0 + OOooOOo
    oO = xbmcgui . Dialog ( )
    if oO . yesno ( "Delete BBC iPlayer Cache Files" , str ( i1Ii1i11ii ) + " files found" , "Do you want to delete them?" ) :
     if 19 - 19: i1IIi % OOOo0 - iIii1I11I1II1 - o00oOO0 / ii11ii1ii
     for OOoOooOoOOOoo in O0o :
      os . unlink ( os . path . join ( Iiii11iIi1 , OOoOooOoOOOoo ) )
     for II1iiiiII in I1IiiI1ii1i :
      shutil . rmtree ( os . path . join ( Iiii11iIi1 , II1iiiiII ) )
      if 16 - 16: i1Iii
   else :
    pass
    if 79 - 79: OoooooooOO - oo0Oo * i1Iii - OoOoOO00 % I1IiI * I1I1ii
    if 31 - 31: OOOo0
    if 36 - 36: Ooo00oOo00o + Ooo00oOo00o + Ooo00oOo00o % Oo * OOOooOooo00O0
 O0IIi1i = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/script.module.simple.downloader' ) , '' )
 if os . path . exists ( O0IIi1i ) == True :
  for Iiii11iIi1 , I1IiiI1ii1i , O0o in os . walk ( O0IIi1i ) :
   i1Ii1i11ii = 0
   i1Ii1i11ii += len ( O0o )
   if 56 - 56: OOooOOo / I1I1ii
   if 11 - 11: I1IiI / o00OO0OOO0
   if i1Ii1i11ii > 0 :
    if 47 - 47: iiiiiIIii . oOO % OoOoOO00 + Oo - o00oOO0 . OoOoOO00
    oO = xbmcgui . Dialog ( )
    if oO . yesno ( "Delete Simple Downloader Cache Files" , str ( i1Ii1i11ii ) + " files found" , "Do you want to delete them?" ) :
     if 37 - 37: iIii1I11I1II1 . OOOo0 % Ooo00oOo00o % OoooooooOO . OoooooooOO / O0
     for OOoOooOoOOOoo in O0o :
      os . unlink ( os . path . join ( Iiii11iIi1 , OOoOooOoOOOoo ) )
     for II1iiiiII in I1IiiI1ii1i :
      shutil . rmtree ( os . path . join ( Iiii11iIi1 , II1iiiiII ) )
      if 25 - 25: OoOoOO00 % OoOoOO00 - i1Iii . O0
   else :
    pass
    if 79 - 79: I1I1ii / Ooo00oOo00o * OoooooooOO * I1IiI + OOOo0
    if 68 - 68: o00OO0OOO0 / iIii1I11I1II1 . Oo + i11iIiiIii + OOooOOo
 OOI1III1I11I1 = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.itv/Images' ) , '' )
 if os . path . exists ( OOI1III1I11I1 ) == True :
  for Iiii11iIi1 , I1IiiI1ii1i , O0o in os . walk ( OOI1III1I11I1 ) :
   i1Ii1i11ii = 0
   i1Ii1i11ii += len ( O0o )
   if 85 - 85: oOO
   if 62 - 62: i1Iii % OoOoOO00 + I1I1ii + iiiiiIIii % o00oOO0 . OOOo0
   if i1Ii1i11ii > 0 :
    if 53 - 53: Ooo00oOo00o % ii11ii1ii . OOOooOooo00O0 . i1IIi . Ooo00oOo00o
    oO = xbmcgui . Dialog ( )
    if oO . yesno ( "Delete ITV Cache Files" , str ( i1Ii1i11ii ) + " files found" , "Do you want to delete them?" ) :
     if 26 - 26: OOOo0 % I1IiI
     for OOoOooOoOOOoo in O0o :
      os . unlink ( os . path . join ( Iiii11iIi1 , OOoOooOoOOOoo ) )
     for II1iiiiII in I1IiiI1ii1i :
      shutil . rmtree ( os . path . join ( Iiii11iIi1 , II1iiiiII ) )
      if 67 - 67: Oo - I1I1ii * i1Iii . OoooooooOO / i11iIiiIii
   else :
    pass
    if 61 - 61: OOooOOo % OOOo0 * i1IIi / OOOo0 / OoOoOO00 + oOO
    if 22 - 22: I1I1ii . OOOooOooo00O0 + Oo
 IIIIiI1ii1 = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.movies4me/cache' ) , '' )
 if os . path . exists ( OOI1III1I11I1 ) == True :
  for Iiii11iIi1 , I1IiiI1ii1i , O0o in os . walk ( IIIIiI1ii1 ) :
   i1Ii1i11ii = 0
   i1Ii1i11ii += len ( O0o )
   if 73 - 73: i1Iii
   if 13 - 13: o00OO0OOO0 - OoooooooOO / oo0Oo
   if i1Ii1i11ii > 0 :
    if 80 - 80: iIii1I11I1II1 / i11iIiiIii + OOOooOooo00O0
    oO = xbmcgui . Dialog ( )
    if oO . yesno ( "Delete Movies4me Cache Files" , str ( i1Ii1i11ii ) + " files found" , "Do you want to delete them?" ) :
     if 41 - 41: oOO + Ooo00oOo00o * OOOo0 * O0 * Oo - I1IiI
     for OOoOooOoOOOoo in O0o :
      os . unlink ( os . path . join ( Iiii11iIi1 , OOoOooOoOOOoo ) )
     for II1iiiiII in I1IiiI1ii1i :
      shutil . rmtree ( os . path . join ( Iiii11iIi1 , II1iiiiII ) )
      if 96 - 96: OOOo0 - iIii1I11I1II1
   else :
    pass
    if 25 - 25: OoooooooOO . i1Iii % OOOooOooo00O0 . I1I1ii
    if 67 - 67: OoooooooOO + oOO / oo0Oo
 O0oo = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.phstreams/Cache' ) , '' )
 if os . path . exists ( OOI1III1I11I1 ) == True :
  for Iiii11iIi1 , I1IiiI1ii1i , O0o in os . walk ( O0oo ) :
   i1Ii1i11ii = 0
   i1Ii1i11ii += len ( O0o )
   if 50 - 50: oOO - OoOoOO00
   if 33 - 33: I1I1ii / I1I1ii . i11iIiiIii * ii11ii1ii + OOooOOo
   if i1Ii1i11ii > 0 :
    if 16 - 16: I1I1ii
    oO = xbmcgui . Dialog ( )
    if oO . yesno ( "Delete Phoenix Cache Files" , str ( i1Ii1i11ii ) + " files found" , "Do you want to delete them?" ) :
     if 10 - 10: I1IiI . I1I1ii * iIii1I11I1II1 - o00oOO0 - I1IiI / oOO
     for OOoOooOoOOOoo in O0o :
      os . unlink ( os . path . join ( Iiii11iIi1 , OOoOooOoOOOoo ) )
     for II1iiiiII in I1IiiI1ii1i :
      shutil . rmtree ( os . path . join ( Iiii11iIi1 , II1iiiiII ) )
      if 13 - 13: o00oOO0 + I1IiI % I1I1ii % OoooooooOO
   else :
    pass
    if 22 - 22: oOO
    if 23 - 23: O0
 Iiio0OO00oOOO0o0 = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.spotitube/cache' ) , '' )
 if os . path . exists ( OOI1III1I11I1 ) == True :
  for Iiii11iIi1 , I1IiiI1ii1i , O0o in os . walk ( Iiio0OO00oOOO0o0 ) :
   i1Ii1i11ii = 0
   i1Ii1i11ii += len ( O0o )
   if 39 - 39: OoooooooOO
   if 19 - 19: i11iIiiIii
   if i1Ii1i11ii > 0 :
    if 80 - 80: OOOo0
    oO = xbmcgui . Dialog ( )
    if oO . yesno ( "Delete YouTube Music Cache Files" , str ( i1Ii1i11ii ) + " files found" , "Do you want to delete them?" ) :
     if 58 - 58: o00oOO0 + ii11ii1ii % I1IiI
     for OOoOooOoOOOoo in O0o :
      os . unlink ( os . path . join ( Iiii11iIi1 , OOoOooOoOOOoo ) )
     for II1iiiiII in I1IiiI1ii1i :
      shutil . rmtree ( os . path . join ( Iiii11iIi1 , II1iiiiII ) )
      if 22 - 22: iIii1I11I1II1 - i1Iii / OOOo0 * I1I1ii
   else :
    pass
    if 26 - 26: OOooOOo + iiiiiIIii - OOooOOo + Oo . o00oOO0
    if 97 - 97: i1IIi
 ii1iI1i1 = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.supercartoons/cache' ) , '' )
 if os . path . exists ( OOI1III1I11I1 ) == True :
  for Iiii11iIi1 , I1IiiI1ii1i , O0o in os . walk ( ii1iI1i1 ) :
   i1Ii1i11ii = 0
   i1Ii1i11ii += len ( O0o )
   if 51 - 51: oo0Oo * OOOooOooo00O0 / i1IIi
   if 2 - 2: o00oOO0 + I1I1ii . OOOooOooo00O0 - i1IIi + oOO
   if i1Ii1i11ii > 0 :
    if 54 - 54: OoooooooOO . o00oOO0 - OOOooOooo00O0
    oO = xbmcgui . Dialog ( )
    if oO . yesno ( "Delete SuperCartoons Cache Files" , str ( i1Ii1i11ii ) + " files found" , "Do you want to delete them?" ) :
     if 76 - 76: oOO
     for OOoOooOoOOOoo in O0o :
      os . unlink ( os . path . join ( Iiii11iIi1 , OOoOooOoOOOoo ) )
     for II1iiiiII in I1IiiI1ii1i :
      shutil . rmtree ( os . path . join ( Iiii11iIi1 , II1iiiiII ) )
      if 61 - 61: oo0Oo / OoOoOO00 * oo0Oo * I1IiI * oOO . i11iIiiIii
   else :
    pass
    if 26 - 26: oOO / oo0Oo - Ooo00oOo00o . iIii1I11I1II1
    if 83 - 83: oo0Oo % i1Iii / Oo - OOOooOooo00O0 / O0
 oo00oO00oooo = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.tvonline.cc/cache' ) , '' )
 if os . path . exists ( OOI1III1I11I1 ) == True :
  for Iiii11iIi1 , I1IiiI1ii1i , O0o in os . walk ( oo00oO00oooo ) :
   i1Ii1i11ii = 0
   i1Ii1i11ii += len ( O0o )
   if 63 - 63: OoOoOO00 - o00OO0OOO0 . I1IiI
   if 8 - 8: OOOo0 * oo0Oo / I1I1ii + I1IiI . I1I1ii - iiiiiIIii
   if i1Ii1i11ii > 0 :
    if 80 - 80: iIii1I11I1II1 / o00oOO0 * Oo - iiiiiIIii * OOOooOooo00O0
    oO = xbmcgui . Dialog ( )
    if oO . yesno ( "Delete TVonline Cache Files" , str ( i1Ii1i11ii ) + " files found" , "Do you want to delete them?" ) :
     if 97 - 97: I1I1ii - o00OO0OOO0 / OoOoOO00
     for OOoOooOoOOOoo in O0o :
      os . unlink ( os . path . join ( Iiii11iIi1 , OOoOooOoOOOoo ) )
     for II1iiiiII in I1IiiI1ii1i :
      shutil . rmtree ( os . path . join ( Iiii11iIi1 , II1iiiiII ) )
      if 26 - 26: OOOooOooo00O0 + O0 * OOOooOooo00O0 . i1IIi
   else :
    pass
    if 50 - 50: iIii1I11I1II1 - o00OO0OOO0 % OOOooOooo00O0 - Oo
    if 52 - 52: o00oOO0 + i1Iii - ii11ii1ii * i1Iii . iiiiiIIii + oOO
 iI11II11I1 = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.youtube/kodion' ) , '' )
 if os . path . exists ( OOI1III1I11I1 ) == True :
  for Iiii11iIi1 , I1IiiI1ii1i , O0o in os . walk ( iI11II11I1 ) :
   i1Ii1i11ii = 0
   i1Ii1i11ii += len ( O0o )
   if 67 - 67: ii11ii1ii
   if 3 - 3: oOO . o00OO0OOO0 % OoOoOO00 * OOOo0 % i1IIi * Ooo00oOo00o
   if i1Ii1i11ii > 0 :
    if 5 - 5: OoOoOO00 * i1IIi % i1Iii
    oO = xbmcgui . Dialog ( )
    if oO . yesno ( "Delete YouTube Cache Files" , str ( i1Ii1i11ii ) + " files found" , "Do you want to delete them?" ) :
     if 55 - 55: OOOo0 + OOOooOooo00O0
     for OOoOooOoOOOoo in O0o :
      os . unlink ( os . path . join ( Iiii11iIi1 , OOoOooOoOOOoo ) )
     for II1iiiiII in I1IiiI1ii1i :
      shutil . rmtree ( os . path . join ( Iiii11iIi1 , II1iiiiII ) )
      if 85 - 85: o00oOO0 + OOOooOooo00O0 % OOOooOooo00O0 / o00OO0OOO0 . OOOo0 - I1IiI
   else :
    pass
    if 19 - 19: o00OO0OOO0 / OOOooOooo00O0 + I1I1ii
    if 76 - 76: iIii1I11I1II1 / oOO - ii11ii1ii % OOooOOo % iiiiiIIii + OoooooooOO
    if 10 - 10: Ooo00oOo00o * o00OO0OOO0 / Oo - oOO
 I1iIi1IiI1i = xbmc . translatePath ( 'special://masterprofile/addon_data/plugin.video.genesis' )
 oO = xbmcgui . Dialog ( )
 try :
  if oO . yesno ( "Delete Genesis Cache Files" , "Do you want to delete cache" ) :
   IiiIiiiiI1III = os . path . join ( I1iIi1IiI1i , "cache.db" )
   os . unlink ( IiiIiiiiI1III )
   if 42 - 42: o00oOO0 - oo0Oo * o00OO0OOO0 % OOOooOooo00O0 * Oo / oOO
 except :
  pass
  if 94 - 94: oo0Oo + iIii1I11I1II1
 oO = xbmcgui . Dialog ( )
 oO . ok ( "GenieTv" , "                               Finished Deleting Cache " , "                          [COLOR gold]Brought To You By GenieTv[/COLOR]" )
 if 86 - 86: OOooOOo / oo0Oo . OOooOOo % OOOo0 + o00oOO0 % o00OO0OOO0
 if 72 - 72: oo0Oo - ii11ii1ii + o00oOO0 . I1IiI
 if 44 - 44: ii11ii1ii / O0 - I1I1ii + iiiiiIIii . o00OO0OOO0 . ii11ii1ii
 if 95 - 95: I1IiI % oOO % i1IIi * OOooOOo + iiiiiIIii
 if 34 - 34: oOO * OOooOOo . OOOo0 % i11iIiiIii
 if 61 - 61: iIii1I11I1II1 + o00oOO0 * o00OO0OOO0 - i1IIi % o00oOO0
 if 76 - 76: o00oOO0 / I1IiI
 if 12 - 12: oOO
 if 58 - 58: Ooo00oOo00o + iIii1I11I1II1 % O0 + o00OO0OOO0 + I1IiI * OoooooooOO
def iII1IiI1iIi1I ( url ) :
 print '###' + Oo0oO0ooo + ' - DELETING PACKAGES###'
 i1OoOooO00OO000 = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' , '' ) )
 try :
  for Iiii11iIi1 , I1IiiI1ii1i , O0o in os . walk ( i1OoOooO00OO000 ) :
   i1Ii1i11ii = 0
   i1Ii1i11ii += len ( O0o )
   if 18 - 18: OOOooOooo00O0
   if 4 - 4: OOooOOo
   if i1Ii1i11ii > 0 :
    if 96 - 96: OOOo0 % OOOo0 / OOooOOo / I1IiI * oo0Oo - oOO
    oO = xbmcgui . Dialog ( )
    if oO . yesno ( "Delete Package Cache Files" , str ( i1Ii1i11ii ) + " files found" , "Do you want to delete them?" ) :
     if 94 - 94: Oo - iIii1I11I1II1 + OOOo0 - i1IIi + OoooooooOO % Ooo00oOo00o
     for OOoOooOoOOOoo in O0o :
      os . unlink ( os . path . join ( Iiii11iIi1 , OOoOooOoOOOoo ) )
     for II1iiiiII in I1IiiI1ii1i :
      shutil . rmtree ( os . path . join ( Iiii11iIi1 , II1iiiiII ) )
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
 if 36 - 36: OOOooOooo00O0 * o00OO0OOO0 * O0 * iiiiiIIii - OOooOOo / ii11ii1ii
 if 54 - 54: i1IIi - Ooo00oOo00o / OoooooooOO
 if 95 - 95: O0 + iIii1I11I1II1 . ii11ii1ii
 if 61 - 61: i1Iii * i1Iii
 if 70 - 70: oOO . ii11ii1ii / OOooOOo * o00oOO0
 if 74 - 74: OOOo0 . oo0Oo / OOOooOooo00O0 . I1I1ii
 if 74 - 74: Oo / oOO % oOO . I1I1ii
 if 72 - 72: i1IIi
 if 21 - 21: oOO . iiiiiIIii / i11iIiiIii * i1IIi
def O00O0ooo00OO0 ( url ) :
 print '###' + Oo0oO0ooo + ' - DELETING PACKAGES###'
 i1OoOooO00OO000 = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' , '' ) )
 try :
  for Iiii11iIi1 , I1IiiI1ii1i , O0o in os . walk ( i1OoOooO00OO000 ) :
   i1Ii1i11ii = 0
   i1Ii1i11ii += len ( O0o )
   if 63 - 63: o00OO0OOO0 * OoOoOO00
   if 70 - 70: OoOoOO00 + OOOooOooo00O0 * I1IiI
   if i1Ii1i11ii > 0 :
    if 61 - 61: iiiiiIIii + iiiiiIIii + o00oOO0 / iIii1I11I1II1
    oO = xbmcgui . Dialog ( )
    if oO . yesno ( "Delete Package Cache Files" , str ( i1Ii1i11ii ) + " files found" , "Do you want to delete them?" ) :
     if 91 - 91: OOOo0 / OoOoOO00 * iiiiiIIii
     for OOoOooOoOOOoo in O0o :
      os . unlink ( os . path . join ( Iiii11iIi1 , OOoOooOoOOOoo ) )
     for II1iiiiII in I1IiiI1ii1i :
      shutil . rmtree ( os . path . join ( Iiii11iIi1 , II1iiiiII ) )
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
 oooIi1II1I11i1I ( url )
 if 94 - 94: OoOoOO00 - iIii1I11I1II1 - iIii1I11I1II1
 if 83 - 83: ii11ii1ii * iIii1I11I1II1 + I1IiI * i1IIi . OoooooooOO % i1Iii
 if 81 - 81: Ooo00oOo00o - iIii1I11I1II1
 if 60 - 60: oOO
 if 77 - 77: OOOo0 / ii11ii1ii
 if 95 - 95: oOO * i1IIi + o00oOO0
 if 40 - 40: OoOoOO00
 if 7 - 7: iiiiiIIii / Ooo00oOo00o
 if 88 - 88: i1IIi
def O0ooOo0Oooo ( url , name ) :
 I1i1i1 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 I1iiIIiI11I = os . path . join ( I1i1i1 , 'advancedsettings.xml' )
 oO = xbmcgui . Dialog ( )
 I11II1I = os . path . join ( I1i1i1 , 'advancedsettings.xml.bak' )
 if os . path . exists ( I11II1I ) == False :
  if oO . yesno ( "Back Up Original" , 'Have You Backed Up Your Original?' , '' , "[B][COLOR red]     AS YOU CANNOT GO BACK !!![/B][/COLOR]" ) :
   print '###' + Oo0oO0ooo + ' - ADVANCED XML###'
   I1i1i1 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
   I1iiIIiI11I = os . path . join ( I1i1i1 , 'advancedsettings.xml' )
   try :
    os . remove ( I1iiIIiI11I )
    print '=== GenieTv - REMOVING    ' + str ( I1iiIIiI11I ) + '    ==='
   except :
    pass
   i11iiI1111 = o0oOoO00o . http_GET ( url ) . content
   Iiii1iI1i = open ( I1iiIIiI11I , "w" )
   Iiii1iI1i . write ( i11iiI1111 )
   Iiii1iI1i . close ( )
   print '=== GenieTv - WRITING NEW    ' + str ( I1iiIIiI11I ) + '    ==='
   oO = xbmcgui . Dialog ( )
   oO . ok ( Oo0oO0ooo , "       Done Adding new Advanced XML" )
 else :
  print '###' + Oo0oO0ooo + ' - ADVANCED XML###'
  I1i1i1 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
  I1iiIIiI11I = os . path . join ( I1i1i1 , 'advancedsettings.xml' )
  try :
   os . remove ( I1iiIIiI11I )
   print '=== GenieTv - REMOVING    ' + str ( I1iiIIiI11I ) + '    ==='
  except :
   pass
  i11iiI1111 = o0oOoO00o . http_GET ( url ) . content
  Iiii1iI1i = open ( I1iiIIiI11I , "w" )
  Iiii1iI1i . write ( i11iiI1111 )
  Iiii1iI1i . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( I1iiIIiI11I ) + '    ==='
  oO = xbmcgui . Dialog ( )
  oO . ok ( Oo0oO0ooo , "       Done Adding new Advanced XML" )
 return
 if 92 - 92: OOooOOo
def ii111Ii1i ( url , name ) :
 print '###' + Oo0oO0ooo + ' - CHECK ADVANCE XML###'
 I1i1i1 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 I1iiIIiI11I = os . path . join ( I1i1i1 , 'advancedsettings.xml' )
 try :
  Iiii1iI1i = open ( I1iiIIiI11I ) . read ( )
  if 'zero' in Iiii1iI1i :
   name = '0CACHE'
  elif 'tuxen' in Iiii1iI1i :
   name = 'TUXENS'
  elif 'muckys' in Iiii1iI1i :
   name = 'MUCKYS'
  elif 'p2p1' in Iiii1iI1i :
   name = '1st P2P RECOMMENDED'
  elif 'p2p2' in Iiii1iI1i :
   name = '2nd P2P RECOMMENDED'
  elif 'mikey' in Iiii1iI1i :
   name = 'MIKEY1234'
 except :
  name = "NO ADVANCED"
 oO = xbmcgui . Dialog ( )
 oO . ok ( Oo0oO0ooo , "[COLOR yellow]YOU HAVE[/COLOR] " + name + "[COLOR yellow] XML SETTINGS SETUP[/COLOR]" )
 return
 if 46 - 46: i1IIi - OOOooOooo00O0 + oOO + Ooo00oOo00o + o00OO0OOO0
def iiI1ii ( url ) :
 print '###' + Oo0oO0ooo + ' - DELETING ADVANCE XML###'
 I1i1i1 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 I1iiIIiI11I = os . path . join ( I1i1i1 , 'advancedsettings.xml' )
 try :
  os . remove ( I1iiIIiI11I )
  oO = xbmcgui . Dialog ( )
  print '=== GenieTv - DELETING    ' + str ( I1iiIIiI11I ) + '    ==='
  oO . ok ( Oo0oO0ooo , "       Remove Advanced Settings Sucessfull" )
 except :
  oO = xbmcgui . Dialog ( )
  oO . ok ( Oo0oO0ooo , "       No Advanced Settings To Remove" )
 return
 if 20 - 20: iiiiiIIii * o00oOO0
 if 91 - 91: Ooo00oOo00o % i1IIi - iIii1I11I1II1 . iiiiiIIii
 if 31 - 31: o00oOO0 % i1IIi . OoooooooOO - OOooOOo + OoooooooOO
 if 45 - 45: iiiiiIIii + o00OO0OOO0 / OoooooooOO - i1Iii + OoooooooOO
 if 42 - 42: iIii1I11I1II1 * OOOo0 * oOO
 if 62 - 62: iiiiiIIii * O0 % I1I1ii . I1I1ii . OOOo0
 if 91 - 91: i1IIi . OOOooOooo00O0
 if 37 - 37: OOOooOooo00O0 - o00OO0OOO0 + iIii1I11I1II1 / oOO - Ooo00oOo00o . OOooOOo
 if 62 - 62: ii11ii1ii
 if 47 - 47: oOO % iiiiiIIii * Ooo00oOo00o . iIii1I11I1II1 % Oo + OoooooooOO
def I1Ii111I111 ( url = 'http://www.iplocation.net/' , inc = 1 ) :
 O00OOOoOoo0O = re . compile ( "<td width='80'>(.+?)</td><td>(.+?)</td><td>(.+?)</td><td>.+?</td><td>(.+?)</td>" ) . findall ( o0oOoO00o . http_GET ( url ) . content )
 for iIi11 , O00oO , oOo0ooO0O0oo , ii11IiI in O00OOOoOoo0O :
  if inc < 2 : oO = xbmcgui . Dialog ( ) ; oO . ok ( 'Check My IP' , "[B][COLOR gold]Your IP Address is: [/COLOR][/B] %s" % iIi11 , '[B][COLOR gold]Your IP is based in: [/COLOR][/B] %s' % oOo0ooO0O0oo , '[B][COLOR gold]Your Service Provider is:[/COLOR][/B] %s' % ii11IiI )
  inc = inc + 1
  if 14 - 14: o00OO0OOO0 - Oo . Oo * iiiiiIIii . OOOo0 % OOOooOooo00O0
  if 86 - 86: OOOo0 + o00OO0OOO0 * I1IiI - oOO / oOO
  if 9 - 9: OOooOOo / OOOooOooo00O0 . iIii1I11I1II1 % O0
  if 38 - 38: OOOooOooo00O0
  if 78 - 78: i11iIiiIii . I1I1ii % OoooooooOO - I1I1ii - I1I1ii + i1Iii
  if 11 - 11: o00OO0OOO0
  if 20 - 20: O0 . i11iIiiIii * i1IIi % O0 . OOOo0
  if 53 - 53: oo0Oo / OoooooooOO - OoOoOO00
  if 68 - 68: OoooooooOO . OoooooooOO . iIii1I11I1II1 / oo0Oo - o00OO0OOO0 % O0
def iiIIIIiI11II1 ( url , name ) :
 oO = xbmcgui . Dialog ( )
 if oO . yesno ( "GenieTv" , '                                    Install Latest .ini File' ) :
  print '###' + Oo0oO0ooo + ' - CUSTOM FTV INI###'
  I1i1i1 = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/plugin.video.GenieTv' , '' ) )
  I1iiIIiI11I = os . path . join ( I1i1i1 , 'addons2.ini' )
  i11iiI1111 = o0oOoO00o . http_GET ( url ) . content
  Iiii1iI1i = open ( I1iiIIiI11I , "w" )
  Iiii1iI1i . write ( i11iiI1111 )
  Iiii1iI1i . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( I1iiIIiI11I ) + '    ==='
  oO = xbmcgui . Dialog ( )
  oO . ok ( Oo0oO0ooo , "                               Done Adding New .ini File" )
 return
 if 26 - 26: O0 . o00OO0OOO0 + OOOooOooo00O0 - i1Iii . o00OO0OOO0
def II1Iii1I1II1i ( url , name ) :
 oO = xbmcgui . Dialog ( )
 if oO . yesno ( "GenieTv" , '                               Install Custom Settings' ) :
  print '###' + Oo0oO0ooo + ' - CUSTOM FTV SETTINGS###'
  I1i1i1 = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/plugin.video.GenieTv' , '' ) )
  I1iiIIiI11I = os . path . join ( I1i1i1 , 'settings.xml' )
  i11iiI1111 = o0oOoO00o . http_GET ( url ) . content
  Iiii1iI1i = open ( I1iiIIiI11I , "w" )
  Iiii1iI1i . write ( i11iiI1111 )
  Iiii1iI1i . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( I1iiIIiI11I ) + '    ==='
  oO = xbmcgui . Dialog ( )
  oO . ok ( Oo0oO0ooo , "                               Done Adding New Settings" )
 return
 if 100 - 100: i11iIiiIii - Oo
 if 47 - 47: OOOooOooo00O0 * I1IiI * I1I1ii
def iIiii1IIi1I ( ) :
 try :
  IiIiii1IiI = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/plugin.video.GenieTv' , '' ) )
  if os . path . exists ( IiIiii1IiI ) == True :
   oO = xbmcgui . Dialog ( )
   if oO . yesno ( "GenieTv" , "                               Delete FTV Guide Database" ) :
    oo0o0ooOoo00O = os . path . join ( IiIiii1IiI , "source.db" )
    os . unlink ( oo0o0ooOoo00O )
  oO . ok ( "GenieTv" , "                                     FTV Database Reset" )
 except :
  oO = xbmcgui . Dialog ( )
  oO . ok ( Oo0oO0ooo , "               Error Deleting Database No Database To Delete" )
 return
 if 2 - 2: o00oOO0 . iiiiiIIii
 if 43 - 43: iIii1I11I1II1
 if 29 - 29: I1I1ii % oo0Oo + Ooo00oOo00o . i1IIi + OOOo0
 if 24 - 24: oOO / i1Iii * ii11ii1ii - OoooooooOO / OOOo0 . o00oOO0
 if 98 - 98: i1IIi - OOOooOooo00O0
def ii1ii11IIIiiI ( url ) :
 oO0O0o0O = urllib2 . Request ( url )
 oO0O0o0O . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
 oOO00ooOOo = urllib2 . urlopen ( oO0O0o0O )
 i11iiI1111 = oOO00ooOOo . read ( )
 oOO00ooOOo . close ( )
 return i11iiI1111
 if 49 - 49: OOooOOo . i1Iii . o00oOO0
 if 9 - 9: I1I1ii - OoOoOO00 * Ooo00oOo00o
 if 78 - 78: iIii1I11I1II1 / O0 * o00oOO0 / OOOooOooo00O0 / I1IiI
 if 15 - 15: oo0Oo / o00oOO0
 if 54 - 54: oo0Oo - iIii1I11I1II1 - o00OO0OOO0 % i1Iii / OoOoOO00
 if 80 - 80: i11iIiiIii % iIii1I11I1II1 / i11iIiiIii
 if 66 - 66: I1IiI . iIii1I11I1II1 * ii11ii1ii - i1Iii - iIii1I11I1II1
def iIii1i1IIi ( params ) :
 plugintools . log ( "freshstart.main_list " + repr ( params ) ) ; OOOo0ooOO = plugintools . message_yes_no ( Oo0oO0ooo , "Do you wish to restore your" , "Kodi configuration to default settings?" )
 if OOOo0ooOO :
  oooooO0o00 = xbmcaddon . Addon ( id = oo00 ) . getAddonInfo ( 'path' ) ; oooooO0o00 = xbmc . translatePath ( oooooO0o00 ) ;
  iIIIIIi11Ii = os . path . join ( oooooO0o00 , ".." , ".." ) ; iIIIIIi11Ii = os . path . abspath ( iIIIIIi11Ii ) ; plugintools . log ( "freshstart.main_list xbmcPath=" + iIIIIIi11Ii ) ; oOOooo = False
  try :
   for Iiii11iIi1 , I1IiiI1ii1i , O0o in os . walk ( iIIIIIi11Ii , topdown = True ) :
    I1IiiI1ii1i [ : ] = [ II1iiiiII for II1iiiiII in I1IiiI1ii1i if II1iiiiII not in I1i1iiI1 ]
    for ii11IIII11I in O0o :
     try : os . remove ( os . path . join ( Iiii11iIi1 , ii11IIII11I ) )
     except :
      if ii11IIII11I not in [ "Addons15.db" , "MyVideos75.db" , "Textures13.db" , "xbmc.log" ] : oOOooo = True
      plugintools . log ( "Error removing " + Iiii11iIi1 + " " + ii11IIII11I )
    for ii11IIII11I in I1IiiI1ii1i :
     try : os . rmdir ( os . path . join ( Iiii11iIi1 , ii11IIII11I ) )
     except :
      if ii11IIII11I not in [ "Database" , "userdata" ] : oOOooo = True
      plugintools . log ( "Error removing " + Iiii11iIi1 + " " + ii11IIII11I )
   if not oOOooo : plugintools . log ( "freshstart.main_list All user files removed, you now have a clean install" ) ; plugintools . message ( Oo0oO0ooo , "The process is complete, you're now back to a fresh Kodi configuration with GenieTv!" , "Please reboot your system or restart Kodi in order for the changes to be applied." )
   else : plugintools . log ( "freshstart.main_list User files partially removed" ) ; plugintools . message ( Oo0oO0ooo , "The process is complete, you're now back to a fresh Kodi configuration with GenieTv" , "Please reboot your system or restart Kodi in order for the changes to be applied." )
  except : plugintools . message ( Oo0oO0ooo , "Problem found" , "Your settings has not been changed" ) ; import traceback ; plugintools . log ( traceback . format_exc ( ) ) ; plugintools . log ( "freshstart.main_list NOT removed" )
  plugintools . add_item ( action = "" , title = "Now Exit Kodi" , folder = False )
 else : plugintools . message ( Oo0oO0ooo , "Your settings" , "has not been changed" ) ; plugintools . add_item ( action = "" , title = "Done" , folder = False )
 OoOoo0oO ( )
 if 24 - 24: I1I1ii
 if 51 - 51: iiiiiIIii % i11iIiiIii
 if 77 - 77: iiiiiIIii % i11iIiiIii - ii11ii1ii
def I1oooO00oOOooO ( ) :
 iiiiI = [ ]
 Ooo000 = sys . argv [ 2 ]
 if len ( Ooo000 ) >= 2 :
  I1111IiII1 = sys . argv [ 2 ]
  IiiII = I1111IiII1 . replace ( '?' , '' )
  if ( I1111IiII1 [ len ( I1111IiII1 ) - 1 ] == '/' ) :
   I1111IiII1 = I1111IiII1 [ 0 : len ( I1111IiII1 ) - 2 ]
  OO00OO0 = IiiII . split ( '&' )
  iiiiI = { }
  for iiiiIiI1i1I1 in range ( len ( OO00OO0 ) ) :
   Ooii = { }
   Ooii = OO00OO0 [ iiiiIiI1i1I1 ] . split ( '=' )
   if ( len ( Ooii ) ) == 2 :
    iiiiI [ Ooii [ 0 ] ] = Ooii [ 1 ]
    if 28 - 28: Ooo00oOo00o
 return iiiiI
 if 73 - 73: Oo . oo0Oo - Oo % iiiiiIIii / i11iIiiIii / iIii1I11I1II1
IIi11IIiIii1 = base64 . decodestring ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20v' )
Oo000o = base64 . decodestring ( 'L3N0b3JhZ2UvZW11bGF0ZWQvMA==' )
I1iIII1 = base64 . decodestring ( 'L2dlbmllLnR4dA==' )
i11iI1111ii1I = base64 . decodestring ( 'LmFyY2hpdGVjdHMueDEwaG9zdC5jb20vdGVzdC93aC50eHQ=' )
oOoooo000Oo00 = base64 . decodestring ( 'aHR0cDovL2ZpeGVzLmFyY2hpdGVjdHMueDEwaG9zdC5jb20vZml4ZXMudHh0' )
OoOo0 = base64 . decodestring ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vYXBwcy9hcHBzLnhtbA==' )
iIIi1OoOo0O00 = base64 . decodestring ( 'L2FkZG9ucy9uZXcudHh0' )
iiIIii = base64 . decodestring ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vdm9kL3ZvZC5waHA=' )
OOOOoOoO = base64 . decodestring ( 'L2FkZG9ucy9pcHR2LnR4dA==' )
o0OoOOoOOoo = base64 . decodestring ( 'L2FkZG9ucy92aWRlby50eHQ=' )
Oo00o0o = base64 . decodestring ( 'L2FkZG9ucy9zcG9ydHMudHh0' )
O00OO00OOOoO = base64 . decodestring ( 'L2FkZG9ucy9raWRzLnR4dA==' )
iiI11111II = base64 . decodestring ( 'L2FkZG9ucy9tdXNpYy50eHQ=' )
o0O0O0O00o = base64 . decodestring ( 'L2FkZG9ucy9wcm9ncmFtcy50eHQ=' )
O0oOo0o0O0o = base64 . decodestring ( 'L2FkZG9ucy94eHgudHh0' )
Ii1iIIII1i = base64 . decodestring ( 'L2FkZG9ucy9yZXBvLnR4dA==' )
Ii1ii111i1 = base64 . decodestring ( 'L2FkZG9ucy9wYWNrcy50eHQ=' )
O000oo00o000o = base64 . decodestring ( 'L2FkZG9ucy9za2lucy50eHQ=' )
iI1I1i11iIIii = base64 . decodestring ( 'L2FkZG9ucy9hcnQudHh0' )
I1IIIiI1I1ii1 = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2dvdGhhbS50eHQ=' )
IiiI1iiiiI1iI = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2hlbGl4LnR4dA==' )
IIi = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2lzZW5nYXJkLnR4dA==' )
oOOI1 = base64 . decodestring ( 'L2FkZG9ucy9SU1MudHh0' )
OOoO00ooO = base64 . decodestring ( 'Q1VOVA==' )
def Ii11iII1 ( name , url , mode , iconimage , fanart , description , showcontext = True , allinfo = { } ) :
 oo0ooooO = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 iiIIi = True
 i1i = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 i1i . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 i1i . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  i1IIIII1 = [ ]
  if showcontext == 'fav' :
   i1IIIII1 . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in I1IIIii :
   i1IIIII1 . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fanart=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , urllib . quote_plus ( fanart ) , mode ) ) )
  i1i . addContextMenuItems ( i1IIIII1 )
 iiIIi = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = oo0ooooO , listitem = i1i , isFolder = True )
 return iiIIi
 if 57 - 57: o00OO0OOO0 - o00OO0OOO0 % OoOoOO00 % Oo . OOooOOo % Oo
def IIiII ( name , url , mode , iconimage , fanart , description ) :
 oo0ooooO = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 iiIIi = True
 i1i = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 i1i . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 i1i . setProperty ( "Fanart_Image" , fanart )
 iiIIi = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = oo0ooooO , listitem = i1i , isFolder = False )
 return iiIIi
 if 91 - 91: OOOo0 - Ooo00oOo00o - Oo - i1Iii * iIii1I11I1II1
 if 68 - 68: Ooo00oOo00o % O0 * iIii1I11I1II1 / o00oOO0 * OOooOOo + iiiiiIIii
I1111IiII1 = I1oooO00oOOooO ( )
o0ooooO0o0O = None
ii11IIII11I = None
oOo0OOoooO = None
o0OoOo00o0o = None
I1II1I11I1I = None
i11I = None
o0oOO00O000O0 = None
if 89 - 89: OOooOOo - OoOoOO00 - oOO - iiiiiIIii % I1IiI % OOOo0
if 84 - 84: OOooOOo * i1IIi % Oo
try :
 o0oOO00O000O0 = int ( I1111IiII1 [ "fav_mode" ] )
except :
 pass
 if 41 - 41: o00oOO0 . OOOooOooo00O0 + OoooooooOO * i1Iii . OOooOOo
try :
 o0ooooO0o0O = urllib . unquote_plus ( I1111IiII1 [ "url" ] )
except :
 pass
try :
 ii11IIII11I = urllib . unquote_plus ( I1111IiII1 [ "name" ] )
except :
 pass
try :
 o0OoOo00o0o = urllib . unquote_plus ( I1111IiII1 [ "iconimage" ] )
except :
 pass
try :
 oOo0OOoooO = int ( I1111IiII1 [ "mode" ] )
except :
 pass
try :
 I1II1I11I1I = urllib . unquote_plus ( I1111IiII1 [ "fanart" ] )
except :
 pass
try :
 i11I = urllib . unquote_plus ( I1111IiII1 [ "description" ] )
except :
 pass
 if 11 - 11: O0
 if 96 - 96: OOOooOooo00O0 + OOooOOo
print str ( O0OoO000O0OO ) + ': ' + str ( iI111I11I1I1 )
print "Mode: " + str ( oOo0OOoooO )
print "URL: " + str ( o0ooooO0o0O )
print "Name: " + str ( ii11IIII11I )
print "IconImage: " + str ( o0OoOo00o0o )
if 10 - 10: i11iIiiIii . OoooooooOO . O0 % oo0Oo / Ooo00oOo00o
if 36 - 36: OOOo0 % i1IIi + Ooo00oOo00o
def I1IiII11III ( content , viewType ) :
 if 59 - 59: i11iIiiIii - i11iIiiIii + OOOo0
 if content :
  xbmcplugin . setContent ( int ( sys . argv [ 1 ] ) , content )
 if iiIIIII1i1iI . getSetting ( 'auto-view' ) == 'true' :
  xbmc . executebuiltin ( "Container.SetViewMode(%s)" % iiIIIII1i1iI . getSetting ( viewType ) )
  if 4 - 4: Oo * O0 - o00oOO0 % oo0Oo + I1IiI
  if 3 - 3: I1IiI
if oOo0OOoooO == None :
 Oo0OO ( )
 if 91 - 91: O0 - o00OO0OOO0 % oOO
elif oOo0OOoooO == 1 :
 I1I1i1Ioo0oo ( o0ooooO0o0O )
 if 46 - 46: oo0Oo / OOOo0 . I1I1ii % Ooo00oOo00o / i11iIiiIii
elif oOo0OOoooO == 44 :
 oOo0OoOOo0 ( o0ooooO0o0O )
 if 13 - 13: oOO % OOooOOo + iiiiiIIii + oOO + i11iIiiIii - ii11ii1ii
elif oOo0OOoooO == 2 :
 oO0oOOoo00000 ( )
 if 70 - 70: OoOoOO00 * OoOoOO00 . OOOo0
elif oOo0OOoooO == 3 :
 OO0ooo0oOO ( )
 if 11 - 11: OOOooOooo00O0
elif oOo0OOoooO == 21 :
 I1iII1iiII ( )
 if 20 - 20: i1Iii . oOO % i1Iii
elif oOo0OOoooO == 4 :
 IIi1ii1Ii ( )
 if 5 - 5: iiiiiIIii + OOOooOooo00O0
elif oOo0OOoooO == 5 :
 ii1ii11 ( ii11IIII11I , o0ooooO0o0O , i11I )
 if 23 - 23: oOO % iIii1I11I1II1 . o00OO0OOO0
elif oOo0OOoooO == 6 :
 iII1IiI1iIi1I ( o0ooooO0o0O )
 if 95 - 95: Oo + i11iIiiIii % iiiiiIIii - o00oOO0
elif oOo0OOoooO == 7 :
 O0ooOo0Oooo ( o0ooooO0o0O , ii11IIII11I )
 if 11 - 11: ii11ii1ii / O0 + OoOoOO00
elif oOo0OOoooO == 8 :
 ii111Ii1i ( o0ooooO0o0O , ii11IIII11I )
 if 95 - 95: oOO + I1I1ii * iIii1I11I1II1
elif oOo0OOoooO == 9 :
 FIXREPOSADDONS ( o0ooooO0o0O )
 if 17 - 17: Ooo00oOo00o - Oo * O0 / i1Iii
elif oOo0OOoooO == 10 :
 o0O00o ( )
 if 19 - 19: i1IIi - iIii1I11I1II1 . o00OO0OOO0
elif oOo0OOoooO == 11 :
 iiI1ii ( o0ooooO0o0O )
 if 2 - 2: i1Iii
elif oOo0OOoooO == 12 :
 I1Ii111I111 ( )
 if 12 - 12: i11iIiiIii - iIii1I11I1II1 * I1I1ii * OOOooOooo00O0
elif oOo0OOoooO == 13 :
 ooOOoO0o0 ( )
 if 19 - 19: O0 + o00oOO0 + OOooOOo
elif oOo0OOoooO == 14 :
 oooIi1II1I11i1I ( o0ooooO0o0O )
 if 81 - 81: iIii1I11I1II1
elif oOo0OOoooO == 15 :
 ii1O000OOO0OOo ( )
 if 51 - 51: OOooOOo . ii11ii1ii * i1Iii / Oo * OoOoOO00 / O0
elif oOo0OOoooO == 16 :
 iiIIIIiI11II1 ( o0ooooO0o0O , ii11IIII11I )
 if 44 - 44: i11iIiiIii % oOO % o00oOO0 + o00OO0OOO0 * o00oOO0 . i1Iii
elif oOo0OOoooO == 17 :
 II1Iii1I1II1i ( o0ooooO0o0O , ii11IIII11I )
 if 89 - 89: OoooooooOO % OoOoOO00 - Ooo00oOo00o % i11iIiiIii
elif oOo0OOoooO == 18 :
 iIiii1IIi1I ( )
 if 7 - 7: I1I1ii
elif oOo0OOoooO == 19 :
 Ii1IIiiIIi ( ii11IIII11I , o0ooooO0o0O , i11I )
 if 15 - 15: Oo + OOOooOooo00O0 + OOOo0 * OOooOOo
elif oOo0OOoooO == 40 :
 o00OO00O0oOO ( ii11IIII11I , o0ooooO0o0O , i11I )
 if 33 - 33: OOooOOo * Oo
elif oOo0OOoooO == 42 :
 oOo0oO ( ii11IIII11I , o0ooooO0o0O , i11I )
 if 88 - 88: oOO % iiiiiIIii - I1IiI - I1IiI . OOOo0
elif oOo0OOoooO == 43 :
 I1iOOOO ( ii11IIII11I , o0ooooO0o0O , i11I )
 if 52 - 52: OoOoOO00 / OoOoOO00 / OOOo0 - oOO
elif oOo0OOoooO == 20 :
 iIi1 ( o0ooooO0o0O )
 if 91 - 91: OOOo0 + OOooOOo % OoOoOO00 + Ooo00oOo00o
elif oOo0OOoooO == 22 :
 I1Ii1ii ( o0ooooO0o0O )
 if 66 - 66: iIii1I11I1II1 * OoOoOO00 % Oo % OOOo0 - i1Iii
elif oOo0OOoooO == 23 :
 I1iIII1IIiIi ( o0ooooO0o0O )
 if 59 - 59: I1I1ii % o00oOO0
elif oOo0OOoooO == 24 :
 OOiii1IiiIiIIiI ( o0ooooO0o0O )
 if 21 - 21: OoooooooOO % I1IiI - I1IiI / ii11ii1ii / OOooOOo
elif oOo0OOoooO == 25 :
 O0Oo0 ( o0ooooO0o0O )
 if 15 - 15: oo0Oo / oo0Oo % OoooooooOO . oOO
elif oOo0OOoooO == 26 :
 iII11 ( o0ooooO0o0O )
 if 93 - 93: ii11ii1ii * ii11ii1ii / OoooooooOO
elif oOo0OOoooO == 27 :
 Iii1Iii ( o0ooooO0o0O )
 if 6 - 6: ii11ii1ii * Oo + iIii1I11I1II1
elif oOo0OOoooO == 28 :
 IiOOo0 ( o0ooooO0o0O )
 if 19 - 19: O0 % OoOoOO00 * OOooOOo
elif oOo0OOoooO == 29 :
 Ooi1IIii1i ( o0ooooO0o0O )
 if 27 - 27: iiiiiIIii * I1I1ii / i11iIiiIii - o00oOO0 + OoOoOO00
elif oOo0OOoooO == 30 :
 iIIIIIii ( o0ooooO0o0O )
 if 43 - 43: ii11ii1ii - OoOoOO00
elif oOo0OOoooO == 31 :
 ooo ( o0ooooO0o0O )
 if 56 - 56: ii11ii1ii . i1IIi / OOOooOooo00O0 % o00oOO0 / O0 * o00OO0OOO0
elif oOo0OOoooO == 32 :
 II11iI111i1 ( )
 if 98 - 98: O0 + OOOooOooo00O0
elif oOo0OOoooO == 33 :
 IiI11iI1i1i1i ( )
 if 23 - 23: OoooooooOO . iIii1I11I1II1 / i1IIi
elif oOo0OOoooO == 35 :
 II11 ( o0ooooO0o0O )
 if 31 - 31: Oo - iIii1I11I1II1 / o00OO0OOO0 . Ooo00oOo00o
elif oOo0OOoooO == 34 :
 I111 ( o0ooooO0o0O )
 if 74 - 74: Oo - OoOoOO00 - I1I1ii
elif oOo0OOoooO == 36 :
 Ooooooo ( o0ooooO0o0O )
 if 50 - 50: OOOo0 - o00oOO0 + o00oOO0 * o00OO0OOO0 + o00oOO0
elif oOo0OOoooO == 37 :
 I1iIIIi1 ( o0ooooO0o0O )
 if 70 - 70: i1IIi % Ooo00oOo00o / i1IIi
elif oOo0OOoooO == 38 :
 ii1iI ( o0ooooO0o0O )
 if 30 - 30: I1IiI - i11iIiiIii
elif oOo0OOoooO == 41 :
 iIii1i1IIi ( I1111IiII1 )
 if 94 - 94: I1IiI % OOOooOooo00O0
elif oOo0OOoooO == 39 :
 oO00o0oOoo ( o0ooooO0o0O )
 if 39 - 39: I1IiI + oOO % O0
elif oOo0OOoooO == 45 :
 TEXTS ( )
 if 26 - 26: oo0Oo + I1IiI
elif oOo0OOoooO == 46 :
 Oo0o0O0o0oo0O0O ( )
 if 17 - 17: ii11ii1ii - OOOooOooo00O0 % Oo * O0 % O0 * iiiiiIIii
elif oOo0OOoooO == 47 :
 GEVID ( )
 if 6 - 6: oOO
elif oOo0OOoooO == 48 :
 O0ooO00oO ( ii11IIII11I , o0ooooO0o0O , i11I )
 if 46 - 46: OoOoOO00 * oOO
elif oOo0OOoooO == 49 :
 ii1i ( )
 if 23 - 23: i1IIi - O0
elif oOo0OOoooO == 222 :
 OoOOoOooooOOo ( o0ooooO0o0O )
 if 6 - 6: oo0Oo % OoooooooOO * oOO - I1I1ii
elif oOo0OOoooO == 333 :
 ooo00O0OOo ( o0ooooO0o0O )
 if 24 - 24: o00OO0OOO0 / iIii1I11I1II1 . OoooooooOO % I1IiI . i1Iii
 if 73 - 73: oOO
elif oOo0OOoooO == 1020 :
 oOOoo ( )
 if 25 - 25: I1I1ii
elif oOo0OOoooO == 1021 :
 ANIMEEP ( )
 if 77 - 77: OOooOOo . iIii1I11I1II1 . OoooooooOO . iIii1I11I1II1
elif oOo0OOoooO == 1022 :
 ANIMEPLAY ( o0ooooO0o0O )
 if 87 - 87: OoOoOO00 - OoooooooOO / i1IIi . i1Iii - Oo . i11iIiiIii
elif oOo0OOoooO == 1001 :
 O0Ooo0o ( )
 if 47 - 47: Oo % Ooo00oOo00o - oo0Oo - Oo * o00oOO0
elif oOo0OOoooO == 1005 :
 Ii11ii1 ( )
 if 72 - 72: OOooOOo % OOooOOo + OOOooOooo00O0 + ii11ii1ii / Oo
elif oOo0OOoooO == 1007 :
 iiiIiiiI1I ( o0ooooO0o0O )
 if 30 - 30: Oo + OOOo0 + i11iIiiIii / Ooo00oOo00o
elif oOo0OOoooO == 1010 :
 oO0Oo ( o0ooooO0o0O )
 if 64 - 64: I1I1ii
elif oOo0OOoooO == 1011 :
 O0o0O0O ( o0ooooO0o0O )
 if 80 - 80: OOOo0 - i11iIiiIii / Ooo00oOo00o / I1IiI + I1IiI
elif oOo0OOoooO == 1030 :
 IiII1I ( )
 if 89 - 89: O0 + I1I1ii * oOO
elif oOo0OOoooO == 1031 :
 O0oO0oOO00Oo ( o0ooooO0o0O , o0OoOo00o0o )
 if 30 - 30: I1IiI
elif oOo0OOoooO == 1006 :
 Parse . ParseURL ( o0ooooO0o0O )
 if 39 - 39: ii11ii1ii + OOooOOo + oOO + I1I1ii
elif oOo0OOoooO == 2030 :
 Parse . addonParseURL ( o0ooooO0o0O )
 if 48 - 48: oOO / oo0Oo . iIii1I11I1II1
elif oOo0OOoooO == 2031 :
 Parse . apkParseURL ( o0ooooO0o0O )
 if 72 - 72: i1IIi . OOooOOo
elif oOo0OOoooO == 1002 :
 iIiI1111 ( o0ooooO0o0O )
 if 3 - 3: I1IiI % OoOoOO00 - O0
elif oOo0OOoooO == 1003 :
 O0OO00 ( o0ooooO0o0O , o0OoOo00o0o )
 if 52 - 52: Ooo00oOo00o
elif oOo0OOoooO == 1004 :
 i1111I ( o0ooooO0o0O )
 if 49 - 49: i1Iii . ii11ii1ii % oo0Oo . Oo * iiiiiIIii
elif oOo0OOoooO == 1008 :
 i1oooOoOoOO ( )
 if 44 - 44: iIii1I11I1II1 / O0 * Oo + OOOo0 . oo0Oo
elif oOo0OOoooO == 1009 :
 M3UPLAY ( o0ooooO0o0O )
 if 20 - 20: OOOooOooo00O0 + OOooOOo . oOO / i11iIiiIii
elif oOo0OOoooO == 2001 :
 O0oOoO0oO00O ( o0ooooO0o0O )
 if 7 - 7: I1IiI / I1IiI . oOO * O0 + I1I1ii + o00oOO0
elif oOo0OOoooO == 1013 :
 OO0oIII111i11IiI ( )
 if 98 - 98: OoOoOO00 * I1I1ii - OOOo0 % OOooOOo - OOOooOooo00O0 % ii11ii1ii
elif oOo0OOoooO == 1014 :
 iIiI1i111ii ( )
 if 69 - 69: i1IIi % Ooo00oOo00o % oOO / oo0Oo / oo0Oo
elif oOo0OOoooO == 1015 :
 IiI ( o0ooooO0o0O )
 if 6 - 6: OoOoOO00 % ii11ii1ii % i1IIi * oo0Oo
elif oOo0OOoooO == 1016 :
 iiIIi1II ( o0ooooO0o0O )
 if 47 - 47: O0
elif oOo0OOoooO == 1023 :
 Ii1ii1IiIII ( )
 if 55 - 55: Ooo00oOo00o % O0 / OoooooooOO
elif oOo0OOoooO == 1024 :
 iII1iiiiI1i ( )
 if 49 - 49: OOOo0 . Ooo00oOo00o * OoooooooOO % i11iIiiIii + iIii1I11I1II1 * i1IIi
elif oOo0OOoooO == 1025 :
 OoOo ( o0ooooO0o0O )
 if 88 - 88: ii11ii1ii * OOOooOooo00O0 + OoOoOO00
elif oOo0OOoooO == 4001 :
 O00Oo000ooO0 ( )
 if 62 - 62: OoooooooOO
elif oOo0OOoooO == 4002 :
 OoO0O00 ( )
 if 33 - 33: O0 . i11iIiiIii % OOooOOo
elif oOo0OOoooO == 4004 :
 OO0oOoOO0oOO0 ( )
 if 50 - 50: oo0Oo
elif oOo0OOoooO == 4005 :
 oO0OOoo0OO ( )
 if 81 - 81: i11iIiiIii * iIii1I11I1II1 / Oo * iiiiiIIii
elif oOo0OOoooO == 4006 :
 O0ii1ii1ii ( )
 if 83 - 83: i11iIiiIii - OOOo0 * i11iIiiIii
elif oOo0OOoooO == 4007 :
 oooooOoo0ooo ( )
 if 59 - 59: OOOooOooo00O0 - OoooooooOO / oo0Oo + ii11ii1ii . OOooOOo - OOOooOooo00O0
elif oOo0OOoooO == 4008 :
 I1I1IiI1 ( )
 if 29 - 29: o00oOO0
elif oOo0OOoooO == 4003 :
 OOo ( )
 if 26 - 26: O0 % iiiiiIIii - I1I1ii . iiiiiIIii
elif oOo0OOoooO == 3000 :
 IiiiO0oo0ooo0 ( )
 if 70 - 70: OOooOOo + o00OO0OOO0 / OOOooOooo00O0 + oo0Oo / OOOo0
elif oOo0OOoooO == 3001 :
 ooooO000 ( )
 if 33 - 33: OoooooooOO . O0
elif oOo0OOoooO == 3002 :
 o0O00Oooo ( o0ooooO0o0O )
 if 59 - 59: iIii1I11I1II1
elif oOo0OOoooO == 3003 :
 i1iIIII1iiIIi ( o0ooooO0o0O )
 if 45 - 45: O0
elif oOo0OOoooO == 3004 :
 O00OOoOOOO00O ( o0ooooO0o0O )
 if 78 - 78: o00OO0OOO0 - iIii1I11I1II1 + oOO - ii11ii1ii - oOO
elif oOo0OOoooO == 404 :
 OO000OOOo0Oo ( ii11IIII11I , o0ooooO0o0O , o0OoOo00o0o )
 if 21 - 21: OoooooooOO . O0 / i11iIiiIii
elif oOo0OOoooO == 7030 :
 Ii1Ii1IiIIIi1 ( )
 if 86 - 86: I1IiI / iiiiiIIii
elif oOo0OOoooO == 7021 :
 iI1iii1iI1 ( ii11IIII11I )
 if 40 - 40: iIii1I11I1II1 / oo0Oo / OOOo0 + ii11ii1ii * iiiiiIIii
elif oOo0OOoooO == 7022 :
 IIII ( ii11IIII11I )
 if 1 - 1: Ooo00oOo00o * oo0Oo + I1I1ii . o00oOO0 / oo0Oo
elif oOo0OOoooO == 7000 :
 Oooo0O0Oooo ( ii11IIII11I , o0ooooO0o0O , img )
 if 91 - 91: i1Iii + o00OO0OOO0 - Oo % I1IiI . OOOooOooo00O0
elif oOo0OOoooO == 7050 :
 iiI1ii1Iii ( o0ooooO0o0O )
 if 51 - 51: iiiiiIIii / o00OO0OOO0
elif oOo0OOoooO == 7051 :
 o0o0oO ( o0ooooO0o0O )
 if 51 - 51: oo0Oo * o00oOO0 - oOO + OOOooOooo00O0
elif oOo0OOoooO == 7052 :
 O0O0 ( o0ooooO0o0O )
 if 46 - 46: OOooOOo - i11iIiiIii % Ooo00oOo00o / i1Iii - I1IiI
elif oOo0OOoooO == 7053 :
 oO0oo ( o0ooooO0o0O )
 if 88 - 88: o00oOO0 * OOOo0 / Ooo00oOo00o - iiiiiIIii / i1IIi . oOO
elif oOo0OOoooO == 7054 :
 CoolPlay ( o0ooooO0o0O )
 if 26 - 26: i11iIiiIii - oo0Oo
elif oOo0OOoooO == 7060 :
 oOO00OO0OooOo ( )
 if 45 - 45: oo0Oo + OoOoOO00 % OOOooOooo00O0
elif oOo0OOoooO == 7061 :
 iII11II1II ( o0ooooO0o0O )
 if 55 - 55: oo0Oo - o00oOO0 % OOOo0
elif oOo0OOoooO == 7063 :
 ii111iI1i1 ( o0ooooO0o0O )
 if 61 - 61: oo0Oo
elif oOo0OOoooO == 7062 :
 oOo0oOooo0O ( o0ooooO0o0O )
 if 22 - 22: iIii1I11I1II1 / oo0Oo / OOOo0 - OOooOOo
elif oOo0OOoooO == 7064 :
 NATatozcat ( )
 if 21 - 21: o00oOO0 . i11iIiiIii * o00OO0OOO0 . iiiiiIIii / iiiiiIIii
elif oOo0OOoooO == 7067 :
 iIIIiIi1i ( o0ooooO0o0O )
 if 42 - 42: OoooooooOO / oOO . OOooOOo / O0 - I1I1ii * I1I1ii
elif oOo0OOoooO == 7066 :
 NATatozA ( o0ooooO0o0O )
 if 1 - 1: i1Iii % oOO
elif oOo0OOoooO == 7065 :
 iiIiiIi ( o0ooooO0o0O )
 if 97 - 97: I1IiI
elif oOo0OOoooO == 7070 :
 Ii1i1i ( )
 if 13 - 13: I1IiI % iiiiiIIii . O0 / Oo % Oo
elif oOo0OOoooO == 7071 :
 DIZIlist ( o0ooooO0o0O )
 if 19 - 19: oOO % oo0Oo - oo0Oo % OOOo0 . iiiiiIIii - OoooooooOO
elif oOo0OOoooO == 7072 :
 DIZIpull ( o0ooooO0o0O )
 if 100 - 100: OOOo0 + i1Iii + OOooOOo . i1IIi % OoooooooOO
elif oOo0OOoooO == 7073 :
 WATCHDIZI ( o0ooooO0o0O )
 if 64 - 64: O0 % i1IIi * oOO - i1Iii + Oo
elif oOo0OOoooO == 7002 :
 IIi1II ( )
 if 65 - 65: I1IiI . i11iIiiIii
elif oOo0OOoooO == 7003 :
 Ii1I1Iiii ( o0ooooO0o0O )
 if 36 - 36: o00oOO0 * OOOooOooo00O0 + I1I1ii * OOOooOooo00O0 . ii11ii1ii - iIii1I11I1II1
elif oOo0OOoooO == 7004 :
 oO00o ( o0ooooO0o0O )
 if 14 - 14: o00OO0OOO0 * o00oOO0 + i11iIiiIii
elif oOo0OOoooO == 7020 :
 O0o0O00oOoo00 ( o0ooooO0o0O )
 if 84 - 84: OOOooOooo00O0 / OoOoOO00
elif oOo0OOoooO == 7001 :
 IiiI1i111I1i ( )
 if 86 - 86: OOOo0
elif oOo0OOoooO == 7010 :
 iI1i1I11i ( o0ooooO0o0O )
 if 97 - 97: OoOoOO00
elif oOo0OOoooO == 7011 :
 oo0OooO ( o0ooooO0o0O )
 if 38 - 38: OOOo0
elif oOo0OOoooO == 7012 :
 iIiII1 ( o0ooooO0o0O )
 if 42 - 42: OOooOOo
elif oOo0OOoooO == 7013 :
 cnfTVPlay2 ( o0ooooO0o0O )
elif oOo0OOoooO == 7014 :
 CNF_Studio_Indexer . MV_Movies ( o0ooooO0o0O )
elif oOo0OOoooO == 7015 :
 CNF_Studio_Indexer . Movie_ByYear ( o0ooooO0o0O )
elif oOo0OOoooO == 7016 :
 CNF_Studio_Indexer . Resolve_CNF_Link ( ii11IIII11I , o0ooooO0o0O , o0OoOo00o0o )
elif oOo0OOoooO == 7017 :
 CNF_Studio_Indexer . Search_Movie ( )
elif oOo0OOoooO == 7018 :
 o0oOO ( )
elif oOo0OOoooO == 7019 :
 CNF_Studio_Indexer . List_Movies ( o0ooooO0o0O )
elif oOo0OOoooO == 7020 :
 CNF_Studio_Indexer . Get_Movie_Page ( o0ooooO0o0O )
elif oOo0OOoooO == 7024 :
 CNF_Studio_Indexer . Box_Office ( o0ooooO0o0O )
 if 8 - 8: i11iIiiIii / oo0Oo
elif oOo0OOoooO == 8000 :
 OOOO00OOO00 ( )
elif oOo0OOoooO == 8001 :
 OOOO00o000o ( )
elif oOo0OOoooO == 8002 :
 i1i1I11i1I ( )
elif oOo0OOoooO == 8003 :
 O0OoOOooO0O ( )
elif oOo0OOoooO == 8004 :
 O0i1I11I ( )
elif oOo0OOoooO == 8005 :
 IIII1ii1 ( )
elif oOo0OOoooO == 8006 :
 Iii1 ( ii11IIII11I , o0ooooO0o0O )
elif oOo0OOoooO == 8030 :
 IiII1II11I ( o0ooooO0o0O )
elif oOo0OOoooO == 8045 :
 oOooo00000 ( o0ooooO0o0O )
elif oOo0OOoooO == 8046 :
 iiI11I1iiIiII1I ( o0ooooO0o0O )
elif oOo0OOoooO == 8047 :
 iiiii111 ( o0ooooO0o0O )
elif oOo0OOoooO == 8020 :
 Oo00oo0 ( )
elif oOo0OOoooO == 8021 :
 O00Oo00OOoO0 ( o0ooooO0o0O )
elif oOo0OOoooO == 8022 :
 oOoo ( o0ooooO0o0O )
elif oOo0OOoooO == 8023 :
 o00O0o00oo ( o0ooooO0o0O )
elif oOo0OOoooO == 8040 :
 ii11i1I1iiii ( )
elif oOo0OOoooO == 8041 :
 I11iI1I ( o0ooooO0o0O )
elif oOo0OOoooO == 8042 :
 OO00oo ( o0ooooO0o0O )
elif oOo0OOoooO == 8043 :
 yt . PlayVideo ( o0ooooO0o0O )
elif oOo0OOoooO == 8044 :
 O0Oo0O0 ( o0ooooO0o0O )
elif oOo0OOoooO == 8060 :
 iII1Iii11111 ( )
elif oOo0OOoooO == 8061 :
 OOo00ooOoO0o ( o0ooooO0o0O )
elif oOo0OOoooO == 8064 :
 o00iIiiiII ( )
elif oOo0OOoooO == 8065 :
 Ii1I1OO0ooO0 ( o0ooooO0o0O )
elif oOo0OOoooO == 8070 :
 oOo0OO0o0 ( )
elif oOo0OOoooO == 8071 :
 II1 ( o0ooooO0o0O )
elif oOo0OOoooO == 7080 :
 I1I ( o0ooooO0o0O )
elif oOo0OOoooO == 8090 :
 OOoo000O00O ( )
elif oOo0OOoooO == 8091 :
 IiI1Iiii1I ( o0ooooO0o0O )
elif oOo0OOoooO == 8092 :
 I1iII ( o0ooooO0o0O )
elif oOo0OOoooO == 8081 :
 ooOO ( )
elif oOo0OOoooO == 8062 :
 I1II1IiI1 ( o0ooooO0o0O )
elif oOo0OOoooO == 8063 :
 o0IiIiI111IIII1 ( o0ooooO0o0O )
elif oOo0OOoooO == 8050 :
 O0O0ooOOO ( )
elif oOo0OOoooO == 8051 :
 o0o00Ooo0o ( o0ooooO0o0O )
elif oOo0OOoooO == 8052 :
 oo00o ( o0ooooO0o0O )
elif oOo0OOoooO == 8085 :
 oo0OoOO0o0o ( )
elif oOo0OOoooO == 8086 :
 oOOoO0O ( o0ooooO0o0O )
elif oOo0OOoooO == 8087 :
 Ooooo ( o0ooooO0o0O )
elif oOo0OOoooO == 8088 :
 iIiiiIiIi ( o0ooooO0o0O , ii11IIII11I )
elif oOo0OOoooO == 9000 :
 ii11I1 ( )
elif oOo0OOoooO == 1111 :
 I1Oo0O0OooOooo0 ( )
elif oOo0OOoooO == 9001 :
 OOoooOoO0 ( )
elif oOo0OOoooO == 9002 :
 Ii11iiI ( )
elif oOo0OOoooO == 9003 :
 iiiiI11iioooooOOo0o ( )
elif oOo0OOoooO == 50 :
 oOoO00 ( o0ooooO0o0O )
elif oOo0OOoooO == 9020 :
 champlist ( )
elif oOo0OOoooO == 9021 :
 oooO0o0oOoO ( )
elif oOo0OOoooO == 9022 :
 I11iii ( )
elif oOo0OOoooO == 9023 :
 IIi111 ( )
elif oOo0OOoooO == 9024 :
 I1Ii1 ( o0ooooO0o0O )
elif oOo0OOoooO == 9030 :
 O00O0Oo0 ( o0ooooO0o0O )
elif oOo0OOoooO == 9031 :
 OoOiI11IiI1i1 ( o0ooooO0o0O )
elif oOo0OOoooO == 9032 :
 ooOoOoO0 ( o0ooooO0o0O )
elif oOo0OOoooO == 9033 :
 Iii1II1ii ( o0ooooO0o0O )
elif oOo0OOoooO == 7085 :
 i1I1I1I ( o0ooooO0o0O )
elif oOo0OOoooO == 7086 :
 o000oo0o ( o0ooooO0o0O )
elif oOo0OOoooO == 7087 :
 o000 ( i11I )
elif oOo0OOoooO == 9666 :
 O00O0ooo00OO0 ( o0ooooO0o0O )
elif oOo0OOoooO == 10100 : Oo0iII1iI1IIiI ( )
elif oOo0OOoooO == 10105 : o0oo0o00ooO00 ( o0ooooO0o0O )
elif oOo0OOoooO == 10106 : ii1IIiII111I ( o0ooooO0o0O )
elif oOo0OOoooO == 10104 : OO0OOOOo0000O ( o0ooooO0o0O )
elif oOo0OOoooO == 10107 : o0O0OOo0oO ( )
elif oOo0OOoooO == 10103 : oO0OOOoooO00o0o ( o0ooooO0o0O )
elif oOo0OOoooO == 10108 : II1IiiIII ( o0ooooO0o0O )
elif oOo0OOoooO == 10107 : o0O0OOo0oO ( )
elif oOo0OOoooO == 10000 : Origin_Menu ( )
elif oOo0OOoooO == 10001 : Ooooo0OoO0 ( )
elif oOo0OOoooO == 10002 : i1iIi1IIiIII1 ( )
elif oOo0OOoooO == 10003 : Iii11i ( )
elif oOo0OOoooO == 10004 : OoOO0OOoo ( o0ooooO0o0O )
elif oOo0OOoooO == 10005 : o0oO0OoO0 ( )
elif oOo0OOoooO == 10006 : iI ( o0ooooO0o0O )
elif oOo0OOoooO == 10007 : o0o0oOo000o0 ( o0ooooO0o0O , o0OoOo00o0o )
elif oOo0OOoooO == 10008 : I1ii1i ( )
elif oOo0OOoooO == 10009 : O00O ( )
elif oOo0OOoooO == 10010 : iiIi1iiI1I ( o0ooooO0o0O )
elif oOo0OOoooO == 10011 : iIOOO ( o0ooooO0o0O )
elif oOo0OOoooO == 10012 : o00oo0000 ( o0ooooO0o0O )
elif oOo0OOoooO == 10013 : iiiI1i1 ( o0ooooO0o0O )
elif oOo0OOoooO == 10014 : ooO0000o00O ( )
elif oOo0OOoooO == 10015 : ooIi1IiIiIi1IiI ( )
elif oOo0OOoooO == 10016 : iIiiIiiIi ( o0ooooO0o0O )
elif oOo0OOoooO == 10017 : I1ii1II1iII ( )
elif oOo0OOoooO == 10018 : oo0oO ( )
elif oOo0OOoooO == 10019 : Oo00OO0OO ( )
elif oOo0OOoooO == 10020 : oOII1ii1ii11I1 ( )
elif oOo0OOoooO == 10021 : OOOO ( )
elif oOo0OOoooO == 10022 : i11i11 ( o0ooooO0o0O )
elif oOo0OOoooO == 10023 : o0ooO0OoOo ( ii11IIII11I , o0ooooO0o0O )
elif oOo0OOoooO == 10024 : oo0oooo0OoO0o ( o0ooooO0o0O )
elif oOo0OOoooO == 10025 : oOooo0Oo ( )
elif oOo0OOoooO == 10026 : O0oOoo0OoO0O ( )
elif oOo0OOoooO == 10027 : oooO00o0 ( )
elif oOo0OOoooO == 10028 : iIIIiIi1I1i ( )
elif oOo0OOoooO == 10029 : ooOo0O0O0oOO0 ( )
elif oOo0OOoooO == 423 : Ii1I1 ( o0ooooO0o0O )
elif oOo0OOoooO == 426 : Ii1iI ( o0ooooO0o0O )
elif oOo0OOoooO == 10030 : Izle_Films ( )
elif oOo0OOoooO == 10031 : Latest_Izle_Movies ( )
elif oOo0OOoooO == 10032 : Izle_Genres ( )
elif oOo0OOoooO == 10033 : Izle_Pop_Movies ( )
elif oOo0OOoooO == 10034 : Izle_Boxsets ( )
elif oOo0OOoooO == 10035 : Izle_Search ( )
elif oOo0OOoooO == 10036 : Izle_Genres_Movie ( o0ooooO0o0O )
elif oOo0OOoooO == 10037 : Izle_Boxset_single ( o0ooooO0o0O )
elif oOo0OOoooO == 10038 : Izle_IFRAME ( )
elif oOo0OOoooO == 10039 : Izle_Boxsets_Next ( o0ooooO0o0O )
elif oOo0OOoooO == 10040 : O0oO ( )
elif oOo0OOoooO == 10041 : OOi1iiii ( o0ooooO0o0O )
elif oOo0OOoooO == 10042 : OO0ooo0 ( o0ooooO0o0O )
elif oOo0OOoooO == 10043 : II11ii ( )
elif oOo0OOoooO == 10044 : IIiI11I1I1i1i ( o0ooooO0o0O )
elif oOo0OOoooO == 10045 : O0o0O ( ii11IIII11I )
elif oOo0OOoooO == 10046 : O0oo0O00 ( o0ooooO0o0O )
elif oOo0OOoooO == 10047 : OoO0O000 ( o0ooooO0o0O )
elif oOo0OOoooO == 10048 : oooOO0oOooO00 ( o0ooooO0o0O )
elif oOo0OOoooO == 10049 : iI11i ( o0ooooO0o0O )
elif oOo0OOoooO == 10050 : iIII1I1ii ( )
elif oOo0OOoooO == 10051 : oOoO000 ( )
elif oOo0OOoooO == 10052 : iiiIIiii11I1 ( )
elif oOo0OOoooO == 10053 : Addon ( o0ooooO0o0O )
elif oOo0OOoooO == 10054 : IiIiIi ( o0ooooO0o0O , ii11IIII11I )
elif oOo0OOoooO == 10055 :
 IIiI11i11 ( "addFavorite" )
 try :
  ii11IIII11I = ii11IIII11I . split ( '\\ ' ) [ 1 ]
 except :
  pass
 try :
  ii11IIII11I = ii11IIII11I . split ( '  - ' ) [ 0 ]
 except :
  pass
 o0oOOO0 ( ii11IIII11I , o0ooooO0o0O , o0OoOo00o0o , I1II1I11I1I , o0oOO00O000O0 )
elif oOo0OOoooO == 10056 :
 IIiI11i11 ( "rmFavorite" )
 try :
  ii11IIII11I = ii11IIII11I . split ( '\\ ' ) [ 1 ]
 except :
  pass
 try :
  ii11IIII11I = ii11IIII11I . split ( '  - ' ) [ 0 ]
 except :
  pass
 o00oooOo ( ii11IIII11I )
elif oOo0OOoooO == 10057 :
 IIiI11i11 ( "getFavorites" )
 o0ooO0OOO ( )
elif oOo0OOoooO == 10058 : I1i11 ( )
elif oOo0OOoooO == 10059 : Donators_Guide ( )
elif oOo0OOoooO == 10060 : o000ooooO0o ( )
elif oOo0OOoooO == 10061 : OooOOOO ( )
elif oOo0OOoooO == 10062 : ii ( ii11IIII11I , o0ooooO0o0O , i11I )
elif oOo0OOoooO == 10063 : o0O ( )
elif oOo0OOoooO == 10064 : iII1iIi11i ( )
elif oOo0OOoooO == 10065 : iI1 ( o0ooooO0o0O )
elif oOo0OOoooO == 10066 : Iii11iI1i ( o0ooooO0o0O )
elif oOo0OOoooO == 10068 : ooOoO00 ( o0ooooO0o0O )
elif oOo0OOoooO == 10069 : ii1I1 ( o0ooooO0o0O )
elif oOo0OOoooO == 10070 : o0o0O0O00oOOo ( o0ooooO0o0O )
elif oOo0OOoooO == 10071 : Genie_Watch ( )
elif oOo0OOoooO == 10072 : i1Ii1Ii ( )
elif oOo0OOoooO == 10073 : oO0 ( o0ooooO0o0O )
elif oOo0OOoooO == 10074 : O0oO0 ( o0ooooO0o0O )
elif oOo0OOoooO == 10075 : oOOoo00O00o ( o0OoOo00o0o , ii11IIII11I , o0ooooO0o0O )
elif oOo0OOoooO == 10076 : OO0ooOOO0OOO ( o0ooooO0o0O )
elif oOo0OOoooO == 10077 : iI1i11iII111 ( o0ooooO0o0O )
elif oOo0OOoooO == 10078 : ii1iII1II ( )
elif oOo0OOoooO == 10079 : Genie_Watch_Tv_Shows ( )
elif oOo0OOoooO == 10080 : Genie_Watch_Tv_Genre ( o0ooooO0o0O )
elif oOo0OOoooO == 10081 : Genie_Watch_TV_PlayRun ( o0ooooO0o0O )
elif oOo0OOoooO == 10082 : Genie_Watch_TV_Episodes ( o0ooooO0o0O , o0OoOo00o0o )
elif oOo0OOoooO == 10083 : Genie_Watch_Tv_Recent ( o0ooooO0o0O )
elif oOo0OOoooO == 20000 : o0o000 ( )
elif oOo0OOoooO == 20001 : iii11II1I ( )
elif oOo0OOoooO == 20002 : IiiIi1IIII1i ( o0ooooO0o0O )
elif oOo0OOoooO == 20003 : iIIi1I1ii ( o0ooooO0o0O )
elif oOo0OOoooO == 20004 : II11iIII1i1I ( o0ooooO0o0O )
elif oOo0OOoooO == 21004 : Ii ( )
elif oOo0OOoooO == 21005 : IiiiiI1 ( o0ooooO0o0O )
elif oOo0OOoooO == 21006 : Iiiiiii1 ( o0ooooO0o0O )
elif oOo0OOoooO == 21007 : iiiiI11ii ( o0ooooO0o0O )
elif oOo0OOoooO == 30000 : OOooO ( )
elif oOo0OOoooO == 30001 : OO0o0o0oo0O ( )
elif oOo0OOoooO == 10012 : Resolve ( o0ooooO0o0O )
elif oOo0OOoooO == 30003 : i1II ( )
elif oOo0OOoooO == 30004 : I11IIIiIi11 ( o0ooooO0o0O )
elif oOo0OOoooO == 30005 : oOo00OooO0oO ( o0ooooO0o0O )
elif oOo0OOoooO == 30006 : oOo00oOOOOO ( )
elif oOo0OOoooO == 30007 : iIiI ( )
elif oOo0OOoooO == 30008 : O0OO0OIiiiIiiI ( o0ooooO0o0O )
elif oOo0OOoooO == 30009 : Oo00OOOOoo0oo ( o0ooooO0o0O )
elif oOo0OOoooO == 30010 : I11iIiI1 ( o0ooooO0o0O )
elif oOo0OOoooO == 30011 : IIiIii ( )
elif oOo0OOoooO == 30012 : Iiii1I1 ( )
elif oOo0OOoooO == 30013 : o0OoO000O ( )
elif oOo0OOoooO == 30014 : oooo0OOo ( )
if 33 - 33: oOO * I1I1ii - O0 + OOOo0 / I1I1ii
xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
