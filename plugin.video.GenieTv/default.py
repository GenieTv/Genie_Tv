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
 if 94 - 94: OoOO + OoOO0ooOOoo0O + o0000oOoOoO0o * o00O0oo
 if 97 - 97: oO0o0ooO0 - IIII / O0oO - o0oO0
oo00 = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'
o00 = 'plugin.video.GenieTv'
Oo0oO0ooo = [ 'plugin.video.GenieTv' , 'script.module.addon.common' , 'repository.GenieTv' ]
o0oOoO00o = xbmcaddon . Addon ( id = o00 )
i1 = xbmc . translatePath ( 'special://home/media' )
oOOoo00O0O = 'plugin.video.GenieTv'
i1111 = xbmcgui . DialogProgress ( )
i11 = "[COLORgreen]GenieTv[/COLOR]"
I11 = Net ( )
Oo0o0000o0o0 = xbmcgui . Dialog ( )
oOo0oooo00o = base64 . decodestring
oO0o0o0ooO0oO = o0oOoO00o . getSetting ( 'Build' )
oo0o0O00 = o0oOoO00o . getSetting ( 'Local' )
oO = o0oOoO00o . getSetting ( 'Remote' )
i1iiIIiiI111 = o0oOoO00o . getSetting ( 'LocalM3u' )
oooOOOOO = o0oOoO00o . getSetting ( 'User' )
i1iiIII111ii = o0oOoO00o . getSetting ( 'Pass' )
i1iIIi1 = o0oOoO00o . getSetting ( 'AdultPass' )
ii11iIi1I = xbmcgui . Dialog ( )
iI111I11I1I1 = xbmc . translatePath ( 'special://home/' )
OOooO0OOoo = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + o00 , 'fanart.jpg' ) )
iIii1 = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + o00 , 'icon.png' , OOooO0OOoo , '' ) )
oOOoO0 = ( oOo0oooo00o ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vR2VuaWVBcnQv' ) )
O0OoO000O0OO = ( oOo0oooo00o ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vR2VuaWVBcnQvb3JpZ2luLnBuZw==' ) )
iiI1IiI = "2.5.4"
II = xbmc . translatePath ( 'special://database' )
ooOoOoo0O = xbmc . translatePath ( 'special://home/userdata/addon_data/plugin.video.GenieTV' )
OooO0 = xbmc . translatePath ( 'special://thumbnails' ) ;
II11iiii1Ii = "GenieTv"
OO0o = ( oOo0oooo00o ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20=' ) )
Ooo = 'http://'
O0o0Oo = base64 . decodestring ( 'LnBocA==' )
Oo00OOOOO = base64 . decodestring ( 'aHR0cDovL2JhY2syYmFzaWNzYnVpbGQuY28udWsvdGVzdC8=' )
O0O = [ ]
O00o0OO = o0oOoO00o . getLocalizedString
I11i1 = CookieJar ( )
iIi1ii1I1 = urllib2 . build_opener ( urllib2 . HTTPCookieProcessor ( I11i1 ) )
iIi1ii1I1 . addheaders = [ ( 'User-Agent' , 'Mozilla/5.0' ) ]
o0 = int ( sys . argv [ 1 ] )
I11II1i = xbmc . translatePath ( o0oOoO00o . getAddonInfo ( 'profile' ) . decode ( 'utf-8' ) )
IIIII = os . path . join ( I11II1i , 'favorites' )
ooooooO0oo = xbmc . translatePath ( os . path . join ( 'special://home/userdata/addon_data/script.ivueguide/master.db' ) )
IIiiiiiiIi1I1 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , 'favourites.xml' ) )
I1IIIii = xbmc . translatePath ( os . path . join ( 'special://home/userdata/addon_data/plugin.video.GenieTv/favorites' ) )
if os . path . exists ( IIIII ) == True :
 oOoOooOo0o0 = open ( IIIII ) . read ( )
else : oOoOooOo0o0 = [ ]
OOOO = o0oOoO00o . getSetting ( 'debug' )
if os . path . exists ( ooOoOoo0O ) == False :
 os . makedirs ( ooOoOoo0O )
def OOO00 ( ) :
 if o0oOoO00o . getSetting ( 'My Build' ) == 'true' :
  iiiiiIIii ( '[COLORgreen]WIZARD[/COLOR]' , OO0o , 4001 , oOOoO0 + 'MB.png' , OOooO0OOoo , '' )
 if o0oOoO00o . getSetting ( 'Streams' ) == 'true' :
  iiiiiIIii ( '[COLORgreen]STREAMS[/COLOR]' , OO0o , 4002 , oOOoO0 + 'streams.png' , OOooO0OOoo , '' )
 if o0oOoO00o . getSetting ( 'Music' ) == 'true' :
  iiiiiIIii ( '[COLORgreen]Music[/COLOR]' , OO0o , 4003 , oOOoO0 + 'MUSIC.png' , OOooO0OOoo , '' )
  if 71 - 71: OoOO0ooOOoo0O + o00O0oo * OoOO0ooOOoo0O - Ooo00oOo00o * OOooOOo
 if o0oOoO00o . getSetting ( 'Builders Toolbox' ) == 'true' :
  iiiiiIIii ( '[COLORgreen]BUILDERS TOOLBOX[/COLOR]' , OO0o , 32 , oOOoO0 + 'builderstoolbox.png' , OOooO0OOoo , '' )
 if o0oOoO00o . getSetting ( 'Source List' ) == 'true' :
  iiiiiIIii ( '[COLORgreen]SOURCE LIST[/COLOR]' , OO0o , 46 , oOOoO0 + 'sources.png' , OOooO0OOoo , '' )
 if o0oOoO00o . getSetting ( 'Maintainance' ) == 'true' :
  iiiiiIIii ( '[COLORgreen]MAINTENANCE[/COLOR]' , OO0o , 3 , oOOoO0 + 'MAIN6.png' , OOooO0OOoo , '' )
 if o0oOoO00o . getSetting ( 'Addons' ) == 'true' :
  iiiiiIIii ( '[COLORgreen]ADDONS[/COLOR]' , '' , 10050 , oOOoO0 + 'ADDONS.png' , OOooO0OOoo , '' )
 if o0oOoO00o . getSetting ( 'APK Tool' ) == 'true' :
  iiiiiIIii ( '[COLORgreen]APK TOOL[/COLOR]' , OO0o , 2 , oOOoO0 + 'APK.png' , OOooO0OOoo , '' )
 if o0oOoO00o . getSetting ( 'Rss Feed' ) == 'true' :
  iiiiiIIii ( '[COLORgreen]GenieTv RSS Feed[/COLOR]' , OO0o , 39 , oOOoO0 + 'RSS.png' , OOooO0OOoo , '' )
 if o0oOoO00o . getSetting ( 'Addons Packs' ) == 'true' :
  iiiiiIIii ( '[COLORgreen]ADDONS PACKS[/COLOR]' , OO0o , 30 , oOOoO0 + 'ADDONP.png' , OOooO0OOoo , '' )
 Oooo0Ooo000 ( 'movies' , 'MAIN' )
 if 51 - 51: i11iIiiIii . OOOo0 + OoOoOO00
def II111ii1II1i ( ) :
 iiiiiIIii ( '[COLORgreen]BACKUP MY BUILD[/COLOR]' , OO0o , 10060 , oOOoO0 + 'MB.png' , OOooO0OOoo , '' )
 iiiiiIIii ( '[COLORgreen]RESTORE MY BUILD[/COLOR]' , OO0o , 49 , oOOoO0 + 'MB.png' , OOooO0OOoo , '' )
 iiiiiIIii ( '[COLORgreen]WIPE GENIE[/COLOR]' , OO0o , 41 , oOOoO0 + 'wipegenie.png' , OOooO0OOoo , '' )
 iiiiiIIii ( '[COLORgreen]WISHES PC[/COLOR]' , OO0o , 1 , oOOoO0 + 'WISHESPC.png' , OOooO0OOoo , '' )
 iiiiiIIii ( '[COLORgreen]WISHES ANDROID[/COLOR]' , OO0o , 44 , oOOoO0 + 'WISHESAN.png' , OOooO0OOoo , '' )
 Oooo0Ooo000 ( 'movies' , 'MAIN' )
def OoOo00o ( ) :
 if i1iIIi1 == '5knuckleshuffle' :
  iiiiiIIii ( '[COLORgreen]XVID[/COLOR]' , OO0o , 10100 , oOOoO0 + 'JIZBOX.png' , OOooO0OOoo , '' )
 if o0oOoO00o . getSetting ( 'TV GUIDE' ) == 'true' :
  o0OOoo0OO0OOO ( '[COLORgreen]TV GUIDE[/COLOR]' , '' , 10063 , oOOoO0 + 'GTVIPTV.png' , OOooO0OOoo , '' )
  if o0oOoO00o . getSetting ( 'Favourites' ) == 'true' :
   iiiiiIIii ( '[COLORgreen]FAVOURITES[/COLOR]' , OO0o , 10057 , oOOoO0 + 'FAVORITES.png' , OOooO0OOoo , '' )
 if o0oOoO00o . getSetting ( 'Search' ) == 'true' :
  iiiiiIIii ( '[COLORgreen]SEARCH[/COLOR]' , OO0o , 9000 , oOOoO0 + 'search.png' , OOooO0OOoo , '' )
 if o0oOoO00o . getSetting ( 'G-tv' ) == 'true' :
  iiiiiIIii ( '[COLORgreen]G-Tv PRIVATE LIST[/COLOR]' , '' , 10058 , oOOoO0 + 'GTVIPTV.png' , OOooO0OOoo , '' )
 if o0oOoO00o . getSetting ( 'YOUTUBE' ) == 'true' :
  iiiiiIIii ( '[COLORgreen]SEARCH YOUTUBE[/COLOR]' , OO0o , 10064 , oOOoO0 + 'youtube.png' , OOooO0OOoo , '' )
 if o0oOoO00o . getSetting ( 'Popcorn Box' ) == 'true' :
  iiiiiIIii ( '[COLORgreen]POPCORN BOX[/COLOR]' , OO0o , 7061 , oOOoO0 + 'popcorn.png' , OOooO0OOoo , '' )
 if o0oOoO00o . getSetting ( 'Dizzy Tv' ) == 'true' :
  iiiiiIIii ( '[COLORgreen]DIZZY TV[/COLOR]' , '' , 10018 , oOOoO0 + 'dtv.png' , OOooO0OOoo , '' )
 if o0oOoO00o . getSetting ( 'Watch Series' ) == 'true' :
  iiiiiIIii ( '[COLORgreen]WATCH SERIES[/COLOR]' , '' , 10040 , oOOoO0 + 'WATCHSERIES.png' , OOooO0OOoo , '' )
 if o0oOoO00o . getSetting ( 'Recent Episodes' ) == 'true' :
  iiiiiIIii ( '[COLORgreen]RECENT EPISODES[/COLOR]' , OO0o , 8081 , oOOoO0 + 'recent.png' , OOooO0OOoo , '' )
 if o0oOoO00o . getSetting ( 'REQUESTS' ) == 'true' :
  iiiiiIIii ( '[COLORgreen]REQUESTS[/COLOR]' , OO0o + ( oOo0oooo00o ( 'L1JFUVVFU1RTLnBocA==' ) ) , 10066 , oOOoO0 + 'requests.png' , OOooO0OOoo , '' )
 if o0oOoO00o . getSetting ( 'Scooby Streams' ) == 'true' :
  iiiiiIIii ( '[COLORgreen]SCOOBY STREAMS[/COLOR]' , OO0o , 1023 , oOOoO0 + 'scoob.png' , OOooO0OOoo , '' )
 if o0oOoO00o . getSetting ( 'The Reaper' ) == 'true' :
  iiiiiIIii ( '[COLORgreen]THE REAPER[/COLOR]' , ( oOo0oooo00o ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9UaGVfUmVhcGVyL21haW4ucGhw' ) ) , 1016 , oOOoO0 + 'reap.png' , OOooO0OOoo , '' )
 if o0oOoO00o . getSetting ( 'Pandoras Box' ) == 'true' :
  iiiiiIIii ( '[COLORgreen]PANDORAS BOX[/COLOR]' , OO0o , 10025 , oOOoO0 + 'PANDORASBOX.png' , OOooO0OOoo , '' )
 if o0oOoO00o . getSetting ( 'HeroVision' ) == 'true' :
  iiiiiIIii ( '[COLORgreen]HEROVISION[/COLOR]' , ( oOo0oooo00o ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC9tYWluLnBocA==' ) ) , 1016 , oOOoO0 + 'hero.png' , OOooO0OOoo , '' )
 if o0oOoO00o . getSetting ( 'Silent Hunter' ) == 'true' :
  iiiiiIIii ( '[COLORgreen]SILENT HUNTER[/COLOR]' , ( oOo0oooo00o ( 'aHR0cDovLzUuMTM1LjIwNy45Ni8=' ) ) , 1006 , oOOoO0 + 'SILENTHUNTER.png' , OOooO0OOoo , '' )
 if o0oOoO00o . getSetting ( 'Redemption Streams' ) == 'true' :
  iiiiiIIii ( '[COLORgreen]Redemption Streams[/COLOR]' , ( oOo0oooo00o ( 'aHR0cDovL3JlZGVtcHRpb25idWlsZC4xNm1iLmNvbS9SZWRlbXB0aW9uL21haW4ucGhw' ) ) , 1016 , oOOoO0 + 'redemption.png' , OOooO0OOoo , '' )
 if o0oOoO00o . getSetting ( 'Stand Up' ) == 'true' :
  iiiiiIIii ( '[COLORgreen]STAND UP[/COLOR]' , '' , 10003 , oOOoO0 + 'ORIGINSTANDUP.png' , OOooO0OOoo , '' )
 if o0oOoO00o . getSetting ( 'Football' ) == 'true' :
  iiiiiIIii ( '[COLORgreen]FOOTBALL[/COLOR]' , '' , 10002 , oOOoO0 + 'ORIGINFOOTBALL.png' , OOooO0OOoo , '' )
 if o0oOoO00o . getSetting ( 'Fitness' ) == 'true' :
  iiiiiIIii ( '[COLORgreen]FITNESS[/COLOR]' , ( oOo0oooo00o ( 'aHR0cHM6Ly93d3cuZml0bmVzc2JsZW5kZXIuY29tL3ZpZGVvcw==' ) ) , 7085 , oOOoO0 + 'FITNESS.png' , OOooO0OOoo , '' )
 if o0oOoO00o . getSetting ( 'Documentaries' ) == 'true' :
  iiiiiIIii ( '[COLORgreen]DOCUMENTARIES[/COLOR]' , OO0o , 8040 , oOOoO0 + 'documentary.png' , OOooO0OOoo , '' )
 if o0oOoO00o . getSetting ( 'CLASSIC MOVIES' ) == 'true' :
  iiiiiIIii ( '[COLORgreen]CLASSIC MOVIES[/COLOR]' , '' , 8060 , oOOoO0 + 'classicmovies.png' , OOooO0OOoo , '' )
 if o0oOoO00o . getSetting ( 'CLASSIC TV' ) == 'true' :
  iiiiiIIii ( '[COLORgreen]CLASSIC TV[/COLOR]' , OO0o , 8064 , oOOoO0 + 'classictv.png' , OOooO0OOoo , '' )
 if o0oOoO00o . getSetting ( 'Disclose' ) == 'true' :
  iiiiiIIii ( '[COLORgreen]DISCLOSE TV[/COLOR]' , OO0o , 7001 , oOOoO0 + 'disclose.png' , OOooO0OOoo , '' )
 if o0oOoO00o . getSetting ( 'Go Fishing' ) == 'true' :
  iiiiiIIii ( '[COLORgreen]Go Fishing[/COLOR]' , OO0o , 8090 , oOOoO0 + 'gofish.png' , OOooO0OOoo , '' )
 if o0oOoO00o . getSetting ( 'GenieTv Kitchen' ) == 'true' :
  iiiiiIIii ( '[COLORgreen]GenieTv Kitchen[/COLOR]' , ( oOo0oooo00o ( 'aHR0cDovL2Zvb2QubmR0di5jb20vdmlkZW9z' ) ) , 8045 , oOOoO0 + 'geniekitchen.png' , OOooO0OOoo , '' )
 if o0oOoO00o . getSetting ( 'WCO' ) == 'true' :
  iiiiiIIii ( '[COLORgreen]WATCH CARTOONS ONLINE[/COLOR]' , OO0o , 21004 , oOOoO0 + 'watchcartoons.png' , OOooO0OOoo , '' )
 if o0oOoO00o . getSetting ( 'Cartoons' ) == 'true' :
  iiiiiIIii ( '[COLORgreen]CARTOONS[/COLOR]' , '' , 10001 , oOOoO0 + 'ORIGINCARTOON.png' , OOooO0OOoo , '' )
 if o0oOoO00o . getSetting ( 'Anime' ) == 'true' :
  iiiiiIIii ( '[COLORgreen]ANIME[/COLOR]' , OO0o , 1001 , oOOoO0 + 'anime.png' , OOooO0OOoo , '' )
 if o0oOoO00o . getSetting ( 'CONCERTS' ) == 'true' :
  iiiiiIIii ( '[COLORgreen]CONCERTS[/COLOR]' , ( oOo0oooo00o ( 'aHR0cHM6Ly93d3cucmVkZGl0LmNvbS9yL2Z1bGxjb25jZXJ0cy8=' ) ) , 7050 , oOOoO0 + 'concerts.png' , OOooO0OOoo , '' )
 if o0oOoO00o . getSetting ( 'M3u Streams' ) == 'true' :
  iiiiiIIii ( '[COLORgreen]M3U STREAMS[/COLOR]' , OO0o , 8070 , oOOoO0 + 'streams.png' , OOooO0OOoo , '' )
 if o0oOoO00o . getSetting ( 'Playlist Loader' ) == 'true' :
  iiiiiIIii ( '[COLORgreen]PLAYLIST LOADER[/COLOR]' , OO0o , 3000 , oOOoO0 + 'loader.png' , OOooO0OOoo , '' )
 if o0oOoO00o . getSetting ( 'CLASSICS' ) == 'true' :
  iiiiiIIii ( '[COLORgreen]CLASSICS[/COLOR]' , OO0o , 3001 , oOOoO0 + 'loader.png' , OOooO0OOoo , '' )
  if 19 - 19: OoOO % i1IIi % OOooOOo
  if 93 - 93: iIii1I11I1II1 % OoOO * i1IIi
  if 16 - 16: O0 - O0oO * iIii1I11I1II1 + oO0o0ooO0
  if 50 - 50: OoOoOO00 - o0oO0 * ii11ii1ii / O0oO + OOooOOo
  if 88 - 88: o00O0oo / O0oO + oO0o0ooO0 - OoOoOO00 / o0oO0 - I1IiI
  if 15 - 15: ii11ii1ii + I1IiI - OoooooooOO / OoOO0ooOOoo0O
  if 58 - 58: i11iIiiIii % o0000oOoOoO0o
  if 71 - 71: OoOO0ooOOoo0O + o0oO0 % i11iIiiIii + ii11ii1ii - IIII
  if 88 - 88: I1IiI - Ooo00oOo00o % OoOO0ooOOoo0O
  if 16 - 16: OOOo0 * OoOO % IIII
  if 86 - 86: OOOo0 + o00O0oo % i11iIiiIii * OoOO . o0oO0 * o0000oOoOoO0o
  if 44 - 44: OoOO
 Oooo0Ooo000 ( 'movies' , 'MAIN' )
 if 88 - 88: O0oO % o00O0oo . OoOoOO00
 if 38 - 38: OOooOOo
 if 57 - 57: O0 / OoOO * O0oO / I1IiI . OoOoOO00
def i11iIIIIIi1 ( url ) :
 iiII1i1 = o00oOO0o ( url )
 OOO00O = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( iiII1i1 )
 for url , OOoOO0oo0ooO , O0o0O00Oo0o0 , O00O0oOO00O00 , i1Oo00 in OOO00O :
  iiiiiIIii ( i1Oo00 , url , 10067 , OOoOO0oo0ooO , O00O0oOO00O00 , O0o0O00Oo0o0 )
  if 31 - 31: O0oO . I1IiI / O0
  if 89 - 89: I1IiI
def OO0oOoOO0oOO0 ( url ) :
 oO0OOoo0OO = O0ii1ii1ii ( url )
 OOO00O = re . compile ( '<img src="(.+?)" alt=.+?yt-lockup-title "><a href="(.+?)".+?data-sessionlink=.+?" title="(.+?)".+?<span class="accessible-description".+?>(.+?)</span>.+?<div class="yt-lockup-description yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr">(.+?)</div>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 next = re . compile ( '<a href="(.+?)" class="yt-uix-button.+?class="yt-uix-button-content">Next.+?</span></a>' ) . findall ( oO0OOoo0OO )
 for url in next :
  url = 'https://www.youtube.com' + url
  iiiiiIIii ( '[COLORgreen] NEXT [/COLOR]' , url , 10065 , oOOoO0 + 'youtube.png' , OOooO0OOoo , '' )
 for oooooOoo0ooo , url , i1Oo00 , I1I1IiI1 , III1iII1I1ii in OOO00O :
  O0O . append ( i1Oo00 )
  Oooo0Ooo000 ( 'tvshows' , 'INFO' )
  oOOo0 = 'http:' + ( oooooOoo0ooo ) . replace ( 'https:' , '' )
  print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>' + oOOo0
  url = 'http://www.youtube.com' + url
  o0OOoo0OO0OOO ( '[COLORred]' + I1I1IiI1 + '[/COLOR]' + '[COLORgreen]' + i1Oo00 + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , oOOo0 , oOOo0 , III1iII1I1ii )
 else :
  OOO00O = re . compile ( '<img src="(.+?)" alt=.+?yt-lockup-title "><a href="(.+?)".+?data-sessionlink=.+?" title="(.+?)".+?<span class="accessible-description".+?>(.+?)</span>' , re . DOTALL ) . findall ( oO0OOoo0OO )
  for oooooOoo0ooo , url , i1Oo00 , I1I1IiI1 in OOO00O :
   Oooo0Ooo000 ( 'tvshows' , 'INFO' )
   oOOo0 = 'http:' + ( oooooOoo0ooo ) . replace ( 'https:' , '' )
   url = 'http://www.youtube.com' + url
   if i1Oo00 in O0O :
    pass
   elif 'user' in url or 'elete' in i1Oo00 :
    pass
   elif 'hannel' in url :
    print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' + url
    oO0OOoo0OO = O0ii1ii1ii ( url )
    oo00O00oO = re . compile ( 'data-thumb="(.+?)".+?href="(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( oO0OOoo0OO )
    for oooooOoo0ooo , url , i1Oo00 in oo00O00oO :
     if 'outube' in url or 'list' in url :
      pass
     elif 'atch' in url :
      url = ( url ) . replace ( '/watch?v=' , '' )
      o0OOoo0OO0OOO ( '[COLORred]' + I1I1IiI1 + '[/COLOR]' + '[COLORgreen]' + i1Oo00 + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , 'http:' + oooooOoo0ooo , 'http:' + oooooOoo0ooo , '' )
     else :
      pass
   elif '&' in url :
    oO0OOoo0OO = O0ii1ii1ii ( url )
    iIiIIIi = re . compile ( '<li class="yt-uix-scroller-scroll-unit "(.+?)</li>' , re . DOTALL ) . findall ( oO0OOoo0OO )
    for iIiIIIi in iIiIIIi :
     i1Oo00 = re . compile ( 'data-video-title="(.+?)"' ) . findall ( str ( iIiIIIi ) )
     for i1Oo00 in i1Oo00 :
      i1Oo00 = ( i1Oo00 ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&amp;' , '&' )
     url = re . compile ( '<a href="/w(.+?)&' ) . findall ( str ( iIiIIIi ) )
     for url in url :
      url = 'https://www.youtube.com/w' + url
     o0OOoo0OO0OOO ( '[COLORred]' + I1I1IiI1 + '[/COLOR]' + '[COLORgreen]' + i1Oo00 + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , '' , '' , '' )
   else :
    o0OOoo0OO0OOO ( '[COLORred]' + I1I1IiI1 + '[/COLOR]' + '[COLORgreen]' + i1Oo00 + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , oOOo0 , oOOo0 , '' )
def ooo00OOOooO ( ) :
 O00OOOoOoo0O = Oo0o0000o0o0 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 O000OOo00oo = 'https://www.youtube.com/results?search_query=' + ( O00OOOoOoo0O ) . replace ( ' ' , '+' )
 oo0OOo = O000OOo00oo . lower ( )
 oO0OOoo0OO = O0ii1ii1ii ( oo0OOo )
 OOO00O = re . compile ( '<img src="(.+?)" alt=.+?yt-lockup-title "><a href="(.+?)".+?data-sessionlink=.+?" title="(.+?)".+?<span class="accessible-description".+?>(.+?)</span>.+?<div class="yt-lockup-description yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr">(.+?)</div>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 next = re . compile ( '<a href="(.+?)" class="yt-uix-button.+?class="yt-uix-button-content">Next.+?</span></a>' ) . findall ( oO0OOoo0OO )
 for ooOOO00Ooo in next :
  ooOOO00Ooo = 'https://www.youtube.com' + ooOOO00Ooo
  iiiiiIIii ( '[COLORgreen] NEXT [/COLOR]' , ooOOO00Ooo , 10065 , oOOoO0 + 'youtube.png' , OOooO0OOoo , '' )
 for oooooOoo0ooo , ooOOO00Ooo , i1Oo00 , I1I1IiI1 , III1iII1I1ii in OOO00O :
  O0O . append ( i1Oo00 )
  Oooo0Ooo000 ( 'tvshows' , 'INFO' )
  oOOo0 = 'http:' + ( oooooOoo0ooo ) . replace ( 'https:' , '' )
  print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>' + oOOo0
  ooOOO00Ooo = 'http://www.youtube.com' + ooOOO00Ooo
  o0OOoo0OO0OOO ( '[COLORred]' + I1I1IiI1 + '[/COLOR]' + '[COLORgreen]' + i1Oo00 + '[/COLOR]' , ( ooOOO00Ooo ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , oOOo0 , oOOo0 , III1iII1I1ii )
 else :
  OOO00O = re . compile ( '<img src="(.+?)" alt=.+?yt-lockup-title "><a href="(.+?)".+?data-sessionlink=.+?" title="(.+?)".+?<span class="accessible-description".+?>(.+?)</span>' , re . DOTALL ) . findall ( oO0OOoo0OO )
  for oooooOoo0ooo , ooOOO00Ooo , i1Oo00 , I1I1IiI1 in OOO00O :
   Oooo0Ooo000 ( 'tvshows' , 'INFO' )
   oOOo0 = 'http:' + ( oooooOoo0ooo ) . replace ( 'https:' , '' )
   ooOOO00Ooo = 'http://www.youtube.com' + ooOOO00Ooo
   if i1Oo00 in O0O :
    pass
   elif 'user' in ooOOO00Ooo or 'elete' in i1Oo00 :
    pass
   elif 'hannel' in ooOOO00Ooo :
    print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' + ooOOO00Ooo
    oO0OOoo0OO = O0ii1ii1ii ( ooOOO00Ooo )
    oo00O00oO = re . compile ( 'data-thumb="(.+?)".+?href="(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( oO0OOoo0OO )
    for oooooOoo0ooo , ooOOO00Ooo , i1Oo00 in oo00O00oO :
     if 'outube' in ooOOO00Ooo or 'list' in ooOOO00Ooo :
      pass
     elif 'atch' in ooOOO00Ooo :
      ooOOO00Ooo = ( ooOOO00Ooo ) . replace ( '/watch?v=' , '' )
      o0OOoo0OO0OOO ( '[COLORred]' + I1I1IiI1 + '[/COLOR]' + '[COLORgreen]' + i1Oo00 + '[/COLOR]' , ( ooOOO00Ooo ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , 'http:' + oooooOoo0ooo , 'http:' + oooooOoo0ooo , '' )
     else :
      pass
   elif '&' in ooOOO00Ooo :
    oO0OOoo0OO = O0ii1ii1ii ( ooOOO00Ooo )
    iIiIIIi = re . compile ( '<li class="yt-uix-scroller-scroll-unit "(.+?)</li>' , re . DOTALL ) . findall ( oO0OOoo0OO )
    for iIiIIIi in iIiIIIi :
     i1Oo00 = re . compile ( 'data-video-title="(.+?)"' ) . findall ( str ( iIiIIIi ) )
     for i1Oo00 in i1Oo00 :
      i1Oo00 = ( i1Oo00 ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&amp;' , '&' )
     ooOOO00Ooo = re . compile ( '<a href="/w(.+?)&' ) . findall ( str ( iIiIIIi ) )
     for ooOOO00Ooo in ooOOO00Ooo :
      ooOOO00Ooo = 'https://www.youtube.com/w' + ooOOO00Ooo
     o0OOoo0OO0OOO ( '[COLORred]' + I1I1IiI1 + '[/COLOR]' + '[COLORgreen]' + i1Oo00 + '[/COLOR]' , ( ooOOO00Ooo ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , '' , '' , '' )
   else :
    o0OOoo0OO0OOO ( '[COLORred]' + I1I1IiI1 + '[/COLOR]' + '[COLORgreen]' + i1Oo00 + '[/COLOR]' , ( ooOOO00Ooo ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , oOOo0 , oOOo0 , '' )
    if 16 - 16: OoOoOO00 % I1IiI - OoOoOO00 + o00O0oo
def i1I1i ( url ) :
 oO0OOoo0OO = O0ii1ii1ii ( url )
 OOO00O = re . compile ( '<img src="(.+?)" alt=.+?yt-lockup-title "><a href="(.+?)".+?data-sessionlink=.+?" title="(.+?)".+?<span class="accessible-description".+?>(.+?)</span>.+?<div class="yt-lockup-description yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr">(.+?)</div>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 next = re . compile ( '<a href="(.+?)" class="yt-uix-button.+?class="yt-uix-button-content">Next.+?</span></a>' ) . findall ( oO0OOoo0OO )
 for url in next :
  url = 'https://www.youtube.com' + url
  iiiiiIIii ( '[COLORgreen] NEXT [/COLOR]' , url , 10065 , oOOoO0 + 'youtube.png' , OOooO0OOoo , '' )
 for oooooOoo0ooo , url , i1Oo00 , I1I1IiI1 , III1iII1I1ii in OOO00O :
  O0O . append ( i1Oo00 )
  Oooo0Ooo000 ( 'tvshows' , 'INFO' )
  oOOo0 = 'http:' + ( oooooOoo0ooo ) . replace ( 'https:' , '' )
  print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>' + oOOo0
  url = 'http://www.youtube.com' + url
  o0OOoo0OO0OOO ( '[COLORred]' + I1I1IiI1 + '[/COLOR]' + '[COLORgreen]' + i1Oo00 + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , oOOo0 , oOOo0 , III1iII1I1ii )
 else :
  OOO00O = re . compile ( '<img src="(.+?)" alt=.+?yt-lockup-title "><a href="(.+?)".+?data-sessionlink=.+?" title="(.+?)".+?<span class="accessible-description".+?>(.+?)</span>' , re . DOTALL ) . findall ( oO0OOoo0OO )
  for oooooOoo0ooo , url , i1Oo00 , I1I1IiI1 in OOO00O :
   Oooo0Ooo000 ( 'tvshows' , 'INFO' )
   oOOo0 = 'http:' + ( oooooOoo0ooo ) . replace ( 'https:' , '' )
   url = 'http://www.youtube.com' + url
   if i1Oo00 in O0O :
    pass
   elif 'user' in url or 'elete' in i1Oo00 :
    pass
   elif 'hannel' in url :
    print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' + url
    oO0OOoo0OO = O0ii1ii1ii ( url )
    oo00O00oO = re . compile ( 'data-thumb="(.+?)".+?href="(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( oO0OOoo0OO )
    for oooooOoo0ooo , url , i1Oo00 in oo00O00oO :
     if 'outube' in url or 'list' in url :
      pass
     elif 'atch' in url :
      url = ( url ) . replace ( '/watch?v=' , '' )
      o0OOoo0OO0OOO ( '[COLORred]' + I1I1IiI1 + '[/COLOR]' + '[COLORgreen]' + i1Oo00 + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , 'http:' + oooooOoo0ooo , 'http:' + oooooOoo0ooo , '' )
     else :
      pass
   elif '&' in url :
    oO0OOoo0OO = O0ii1ii1ii ( url )
    iIiIIIi = re . compile ( '<li class="yt-uix-scroller-scroll-unit "(.+?)</li>' , re . DOTALL ) . findall ( oO0OOoo0OO )
    for iIiIIIi in iIiIIIi :
     i1Oo00 = re . compile ( 'data-video-title="(.+?)"' ) . findall ( str ( iIiIIIi ) )
     for i1Oo00 in i1Oo00 :
      i1Oo00 = ( i1Oo00 ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&amp;' , '&' )
     url = re . compile ( '<a href="/w(.+?)&' ) . findall ( str ( iIiIIIi ) )
     for url in url :
      url = 'https://www.youtube.com/w' + url
     o0OOoo0OO0OOO ( '[COLORred]' + I1I1IiI1 + '[/COLOR]' + '[COLORgreen]' + i1Oo00 + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , '' , '' , '' )
   else :
    o0OOoo0OO0OOO ( '[COLORred]' + I1I1IiI1 + '[/COLOR]' + '[COLORgreen]' + i1Oo00 + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , oOOo0 , oOOo0 , '' )
    if 40 - 40: OOOo0 . iIii1I11I1II1 / OOOo0 / i11iIiiIii
    if 75 - 75: o0000oOoOoO0o + OOooOOo
def O0i1II1Iiii1I11 ( ) :
 if i1iiIII111ii == 'insert_password' :
  Oo0o0000o0o0 . ok ( '[COLORgreen]Donators Login[/COLOR]' , 'You need to set username and password to access this' , 'These are unique and provided to donators to help with server and stream costs' , 'Donate @ [COLORgreen]http://architects.x10host.com[/COLOR]' )
  o0oOoO00o . openSettings ( sys . argv [ 0 ] )
 else :
  iiiiiIIii ( '[COLORgreen]DONATORS LIST[/COLOR]' , OO0o + '/thelist.m3u' , 7080 , oOOoO0 + 'GTVIPTV.png' , OOooO0OOoo , '' )
  if 9 - 9: ii11ii1ii / Oo - OOOo0 / OoooooooOO / iIii1I11I1II1 - OOooOOo
def o00oooO0Oo ( ) :
 buggalo . SUBMIT_URL = 'http://tommy.winther.nu/exception/submit.php'
 try :
  o0O0OOO0Ooo = gui . TVGuide ( )
  o0O0OOO0Ooo . doModal ( )
  del o0O0OOO0Ooo
  print 'Deleted *W*'
 except Exception :
  print buggalo . onExceptionRaised ( )
  if 45 - 45: O0 / OOooOOo
  if 32 - 32: oO0o0ooO0 . IIII . IIII
def OO00O0O ( ) :
 iiiiiIIii ( 'Full Backup' , '' , 10061 , oOOoO0 + 'Backup.png' , OOooO0OOoo , 'Back Up Your Full System' )
 if os . path . exists ( I1IIIii ) :
  iiiiiIIii ( 'Backup Genie Favourites' , ooOOO00Ooo , 10062 , oOOoO0 + 'Backup.png' , OOooO0OOoo , 'Back Up Your favourites' )
 if os . path . exists ( ooooooO0oo ) :
  iiiiiIIii ( 'Backup Ivue Config' , ooooooO0oo , 10062 , oOOoO0 + 'Backup.png' , OOooO0OOoo , 'Back Up Your master.db' )
 if os . path . exists ( IIiiiiiiIi1I1 ) :
  iiiiiIIii ( 'Backup Kodi Favourites' , IIiiiiiiIi1I1 , 10062 , oOOoO0 + 'Backup.png' , OOooO0OOoo , 'Back Up Your favourites.xml' )
  if 33 - 33: O0 . IIII . OOOo0
  if 72 - 72: i1IIi / Ooo00oOo00o + OoooooooOO - Oo
  if 29 - 29: ii11ii1ii + OoOO % O0
zip = o0oOoO00o . getSetting ( 'zip' )
I1I11 = xbmc . translatePath ( os . path . join ( zip ) )
def II1 ( ) :
 o0oO00000 = xbmc . translatePath ( os . path . join ( zip , 'testCBFolder' ) )
 if not os . path . exists ( zip ) :
  ii11iIi1I . ok ( '[COLOR=white]Origin[/COLOR]' , 'The download location you have stored does not exist .\nPlease update the addon settings and try again.' , '' , '' )
  o0oOoO00o . openSettings ( sys . argv [ 0 ] )
  if 69 - 69: Ooo00oOo00o - Oo + i1IIi / O0oO
  if 49 - 49: O0 . oO0o0ooO0
  if 11 - 11: IIII * OOOo0 . iIii1I11I1II1 % OoooooooOO + oO0o0ooO0
def OOO ( name , url , description ) :
 if 'Backup' in name :
  if 'Genie' in name :
   url = I1IIIii
  elif 'Ivue' in name :
   url = ooooooO0oo
  elif 'Kodi' in name :
   url = IIiiiiiiIi1I1
  II1 ( )
  oo0OOo0 = open ( url ) . read ( )
  I11IiI = os . path . join ( I1I11 , description . split ( 'Your ' ) [ 1 ] )
  O0ooO0Oo00o = open ( I11IiI , mode = 'w' )
  O0ooO0Oo00o . write ( oo0OOo0 )
  O0ooO0Oo00o . close ( )
 else :
  if 'guisettings.xml' in description :
   ooO0oOOooOo0 = open ( os . path . join ( I1I11 , description . split ( 'Your ' ) [ 1 ] ) ) . read ( )
   i1I1ii11i1Iii = '<setting type="(.+?)" name="%s.(.+?)">(.+?)</setting>' % skin
   OOO00O = re . compile ( i1I1ii11i1Iii ) . findall ( ooO0oOOooOo0 )
   for type , I1IiiiiI , o0O in OOO00O :
    o0O = o0O . replace ( '&quot;' , '' ) . replace ( '&amp;' , '&' )
    xbmc . executebuiltin ( "Skin.Se	t%s(%s,%s)" % ( type . title ( ) , I1IiiiiI , o0O ) )
  else :
   I11IiI = os . path . join ( url )
   oo0OOo0 = open ( os . path . join ( I1I11 , description . split ( 'Your ' ) [ 1 ] ) ) . read ( )
   O0ooO0Oo00o = open ( I11IiI , mode = 'w' )
   O0ooO0Oo00o . write ( oo0OOo0 )
   O0ooO0Oo00o . close ( )
 ii11iIi1I . ok ( "[COLOR=white]Origin[/COLOR]" , "" , 'All Done !' , '' )
 if 2 - 2: iIii1I11I1II1 / OoOO + Ooo00oOo00o / OoOO0ooOOoo0O
 if 9 - 9: OOooOOo . o0oO0 - Oo - OoOO + OoOoOO00 * i11iIiiIii
 if 79 - 79: OoOO % o0000oOoOoO0o % OOOo0
 if 5 - 5: OoooooooOO % I1IiI % OoOO % oO0o0ooO0
def Iiiii1I ( ) :
 O0oO0 = 1
 II1 ( )
 oO0 = xbmc . translatePath ( os . path . join ( I1I11 , 'Build Backup' , 'Full Backup' , '' ) )
 O0OO0O = xbmc . translatePath ( os . path . join ( I1I11 , 'Build Backup' , 'my_full_backup.zip' ) )
 OO = xbmc . translatePath ( os . path . join ( I1I11 , 'Build Backup' , 'my_full_backup_GUI_Settings.zip' ) )
 if not os . path . exists ( oO0 ) :
  os . makedirs ( oO0 )
 OoOoO = Oo0o0000o0o0 . input ( 'Enter a name for this backup' , type = xbmcgui . INPUT_ALPHANUM )
 if ( not OoOoO ) : return False , 0
 Ii1I1i = OoOoO
 OOI1iI1ii1II = xbmc . translatePath ( os . path . join ( oO0 , Ii1I1i + '.zip' ) )
 O0O0OOOOoo = [ 'plugin.video.GenieTv' ]
 oOooO0 = [ "xbmc.log" , "xbmc.old.log" , "kodi.log" , "kodi.old.log" , '.DS_Store' , '.setup_complete' , 'XBMCHelper.conf' ]
 Ii1I1Ii = [ 'plugin.video.GenieTv' , 'repository.origin' , 'cache' , 'system' , 'Thumbnails' , "peripheral_data" , 'library' , 'keymaps' ]
 OOoO0 = [ "xbmc.log" , "xbmc.old.log" , "kodi.log" , "kodi.old.log" , "Textures13.db" , '.DS_Store' , '.setup_complete' , 'XBMCHelper.conf' , 'advancedsettings.xml' ]
 OO0Oooo0oOO0O = "Creating full backup of existing build"
 o00O0 = "Creating Community Build"
 oOO0O00Oo0O0o = "Archiving..."
 ii1 = ""
 I1iIIiiIIi1i = "Please Wait"
 O0O0ooOOO ( iI111I11I1I1 , OOI1iI1ii1II , o00O0 , oOO0O00Oo0O0o , ii1 , I1iIIiiIIi1i , Ii1I1Ii , OOoO0 )
 time . sleep ( 1 )
 oOOo0O00o = xbmc . translatePath ( os . path . join ( oO0 , Ii1I1i + '_guisettings.zip' ) )
 iIiIi11 = zipfile . ZipFile ( oOOo0O00o , mode = 'w' )
 try :
  iIiIi11 . write ( xbmc . translatePath ( os . path . join ( iI111I11I1I1 , 'userdata' , 'profiles.xml' ) ) , 'profiles.xml' , zipfile . ZIP_DEFLATED )
 except : pass
 iIiIi11 . close ( )
 if O0oO0 == 0 :
  ii11iIi1I . ok ( "FAILED!" , 'The guisettings.xml file could not be found on your' , 'system, please reboot and try again.' , '' )
 else :
  ii11iIi1I . ok ( "SUCCESS!" , 'You Are Now Backed Up. If you\'d like to share this build with' , 'the community please post details on the forum at' , '[COLOR=blue][B]http://rh-project.info[/COLOR][/B]' )
  ii11iIi1I . ok ( "Build Locations" , 'Full Backup (only used to restore on this device): [COLOR=yellow]' + O0OO0O , '[/COLOR]Universal Backup (can be used on any device): [COLOR=yellow]' + OOI1iI1ii1II + '[/COLOR]' )
  if 87 - 87: Oo . OOOo0 - OoOoOO00 + O0 / Oo / OoOO
def O0O0ooOOO ( sourcefile , destfile , message_header , message1 , message2 , message3 , exclude_dirs , exclude_files ) :
 IiI = zipfile . ZipFile ( destfile , 'w' , zipfile . ZIP_DEFLATED )
 IIIii1I = len ( sourcefile )
 ooO0OO = [ ]
 O000OOO = [ ]
 i1111 . create ( message_header , message1 , message2 , message3 )
 for IIo0o0O0O00oOOo , iIIIiIi , OO0O0 in os . walk ( sourcefile ) :
  for file in OO0O0 :
   O000OOO . append ( file )
 I11I11 = len ( O000OOO )
 for IIo0o0O0O00oOOo , iIIIiIi , OO0O0 in os . walk ( sourcefile ) :
  iIIIiIi [ : ] = [ o000O0O for o000O0O in iIIIiIi if o000O0O not in exclude_dirs ]
  OO0O0 [ : ] = [ O0ooO0Oo00o for O0ooO0Oo00o in OO0O0 if O0ooO0Oo00o not in exclude_files ]
  for file in OO0O0 :
   ooO0OO . append ( file )
   I1i1i1iii = len ( ooO0OO ) / float ( I11I11 ) * 100
   i1111 . update ( int ( I1i1i1iii ) , "Backing Up" , '[COLOR yellow]%s[/COLOR]' % file , 'Please Wait' )
   I1111i = os . path . join ( IIo0o0O0O00oOOo , file )
   if not 'temp' in iIIIiIi :
    if not 'plugin.program.originwizard' in iIIIiIi :
     import time
     iIIii = '01/01/1980'
     o00O0O = time . strftime ( '%d/%m/%Y' , time . gmtime ( os . path . getmtime ( I1111i ) ) )
     if o00O0O > iIIii :
      IiI . write ( I1111i , I1111i [ IIIii1I : ] )
 IiI . close ( )
 i1111 . close ( )
 if 20 - 20: i1IIi - o0oO0
 if 30 - 30: o0000oOoOoO0o / OOOo0
def Iii1I1111ii ( ) :
 iiiiiIIii ( '[COLORgreen]SCOOBY STREAMS[/COLOR]' , ( oOo0oooo00o ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvdHZjYXRzLnBocA==' ) ) , 1016 , oOOoO0 + 'scoob.png' , OOooO0OOoo , '' )
 iiiiiIIii ( '[COLORgreen]SCOOBY SCRAPES[/COLOR]' , OO0o , 1024 , oOOoO0 + 'scoob.png' , OOooO0OOoo , '' )
 if 72 - 72: OoOoOO00 + i1IIi + OOooOOo
 if 94 - 94: OoOO . i1IIi - OOooOOo % O0 - Ooo00oOo00o
def ooO0O00Oo0o ( ) :
 iiiiiIIii ( '[COLORgreen]SEARCH MOVIES[/COLOR]' , OO0o , 9001 , oOOoO0 + 'MOVIESv.png' , OOooO0OOoo , '' )
 iiiiiIIii ( '[COLORgreen]SEARCH SERIES[/COLOR]' , OO0o , 9002 , oOOoO0 + 'TVSHOWSv.png' , OOooO0OOoo , '' )
 iiiiiIIii ( '[COLORgreen]SEARCH CARTOONS[/COLOR]' , '' , 10005 , oOOoO0 + 'ORIGINCARTOON' , OOooO0OOoo , '' )
 if 65 - 65: ii11ii1ii . o0000oOoOoO0o - O0oO * IIII / O0oO / o0oO0
 if 40 - 40: o0oO0 * IIII * i11iIiiIii
 if 57 - 57: o0oO0
 if 29 - 29: I1IiI - IIII * OoooooooOO + OoooooooOO . OoOoOO00 + OoooooooOO
def O0o000Oo ( ) :
 iiiiiIIii ( '[COLORgreen]RADIO[/COLOR]' , OO0o , 1013 , oOOoO0 + 'radio.png' , OOooO0OOoo , '' )
 iiiiiIIii ( '[COLORgreen]MUSIC[/COLOR]' , OO0o , 1030 , oOOoO0 + 'MUSIC.png' , OOooO0OOoo , '' )
 iiiiiIIii ( '[COLORgreen]MUSIC ARCHIVE[/COLOR]' , OO0o + ( oOo0oooo00o ( 'L3ZvZC91cmxzL211c2ljLnBocA==' ) ) , 1010 , oOOoO0 + 'MUSIC.png' , OOooO0OOoo , '' )
 iiiiiIIii ( '[COLORgreen]MUSIC SEARCH[/COLOR]' , OO0o , 1111 , oOOoO0 + 'search.png' , OOooO0OOoo , '' )
 iiiiiIIii ( '[COLORgreen]KODIBLE AUDIO BOOKS[/COLOR]' , 'http://doremisa.com/audiobooks/' , 30000 , oOOoO0 + 'kodible.png' , OOooO0OOoo , '' )
 if 67 - 67: OOOo0 . i1IIi
 Oooo0Ooo000 ( 'movies' , 'MAIN' )
 if 27 - 27: o0oO0 % OOOo0
def o0oooOO00 ( ) :
 if 32 - 32: O0oO
 o0OOoo0OO0OOO ( 'DELETE CACHE' , 'url' , 14 , oOOoO0 + 'MAIN5.png' , OOooO0OOoo , '' )
 o0OOoo0OO0OOO ( 'DELETE PACKAGES' , 'url' , 6 , oOOoO0 + 'MAIN4.png' , OOooO0OOoo , '' )
 o0OOoo0OO0OOO ( 'FORCE REFRESH' , 'url' , 10 , oOOoO0 + 'MAIN3.png' , OOooO0OOoo , 'Force Refresh All Repos' )
 if 30 - 30: iIii1I11I1II1 / o0000oOoOoO0o . Ooo00oOo00o - OOooOOo
 o0OOoo0OO0OOO ( 'CHECK MY IP' , 'url' , 12 , oOOoO0 + 'MAIN2.png' , OOooO0OOoo , '' )
 o0OOoo0OO0OOO ( 'ANDROID ONLY DELETE TEXTURE13.DB&THUBMNAIL FOLDER' , 'url' , 13 , oOOoO0 + 'MAIN1.png' , OOooO0OOoo , 'Only Works On Android On Windows It Deletes Your Thumnails Folder But Does Not Delete The Textures13.db' )
 iiiiiIIii ( '[COLORgreen]ADVANCED SETTINGS XML[/COLOR]' , OO0o , 4 , oOOoO0 + 'XML.png' , OOooO0OOoo , '' )
 iiiiiIIii ( '[COLORgreen]URL FIXES[/COLOR]' , OO0o , 20 , oOOoO0 + 'URLFIX.png' , OOooO0OOoo , '' )
 Oooo0Ooo000 ( 'movies' , 'MAIN' )
 if 48 - 48: i1IIi - o00O0oo / O0 * Ooo00oOo00o
 if 71 - 71: ii11ii1ii
def IIiiIiiI ( ) :
 iiiiiIIii ( '[COLORgreen]REPOS[/COLOR]' , ( oOo0oooo00o ( 'aHR0cDovL21pcnJvcnMua29kaS50di9hZGRvbnMv' ) ) , 2030 , oOOoO0 + 'repos.png' , OOooO0OOoo , '' )
 iiiiiIIii ( '[COLORgreen]NEW[/COLOR]' , OO0o , 22 , oOOoO0 + 'NEW.png' , OOooO0OOoo , '' )
 iiiiiIIii ( '[COLORgreen]IPTV[/COLOR]' , OO0o , 23 , oOOoO0 + 'IPTV.png' , OOooO0OOoo , '' )
 iiiiiIIii ( '[COLORgreen]VIDEO[/COLOR]' , OO0o , 24 , oOOoO0 + 'VIDEO.png' , OOooO0OOoo , '' )
 iiiiiIIii ( '[COLORgreen]SPORTS[/COLOR]' , OO0o , 25 , oOOoO0 + 'SPORTS.png' , OOooO0OOoo , '' )
 iiiiiIIii ( '[COLORgreen]KIDS[/COLOR]' , OO0o , 26 , oOOoO0 + 'KIDS.png' , OOooO0OOoo , '' )
 iiiiiIIii ( '[COLORgreen]MUSIC[/COLOR]' , OO0o , 27 , oOOoO0 + 'MUSIC.png' , OOooO0OOoo , '' )
 iiiiiIIii ( '[COLORgreen]PROGRAMS[/COLOR]' , OO0o , 28 , oOOoO0 + 'PROGRAMS.png' , OOooO0OOoo , '' )
 iiiiiIIii ( '[COLORgreen]XXX[/COLOR]' , 'URL' , 29 , oOOoO0 + 'XXX.png' , OOooO0OOoo , '' )
 Oooo0Ooo000 ( 'movies' , 'MAIN' )
 if 10 - 10: I1IiI % I1IiI - I1IiI . oO0o0ooO0
 if 73 - 73: o0000oOoOoO0o % i11iIiiIii - OOOo0
def Ii1iI111II1I1 ( ) :
 o0OOoo0OO0OOO ( 'CHECK ADVANCED XML' , OO0o , 8 , oOOoO0 + 'XML.png' , OOooO0OOoo , '' )
 o0OOoo0OO0OOO ( 'MUCKYS XML' , OO0o + '/wizard/muckys.xml' , 7 , oOOoO0 + 'XML.png' , OOooO0OOoo , '' )
 o0OOoo0OO0OOO ( '0CACHE XML' , OO0o + '/wizard/0cache.xml' , 7 , oOOoO0 + 'XML.png' , OOooO0OOoo , '' )
 o0OOoo0OO0OOO ( 'MIKEY1234 XML' , OO0o + '/wizard/mikey.xml' , 7 , oOOoO0 + 'XML.png' , OOooO0OOoo , '' )
 o0OOoo0OO0OOO ( 'TUXENS XML' , OO0o + '/wizard/tuxens.xml' , 7 , oOOoO0 + 'XML.png' , OOooO0OOoo , '' )
 o0OOoo0OO0OOO ( 'P2P RECOMMENDED XML1' , OO0o + '/wizard/p2p1.xml' , 7 , oOOoO0 + 'XML.png' , OOooO0OOoo , '' )
 o0OOoo0OO0OOO ( 'P2P RECOMMENDED XML2' , OO0o + '/wizard/p2p2.xml' , 7 , oOOoO0 + 'XML.png' , OOooO0OOoo , '' )
 o0OOoo0OO0OOO ( 'DELETE XML' , OO0o , 11 , oOOoO0 + 'XML.png' , OOooO0OOoo , '' )
 Oooo0Ooo000 ( 'movies' , 'MAIN' )
 if 91 - 91: OoOO0ooOOoo0O % OoOO0ooOOoo0O - OOOo0
def I1iiii1I ( ) :
 o0OOoo0OO0OOO ( '[COLORgreen]My Local Zip[/COLOR]' , oo0o0O00 , 48 , oOOoO0 + 'MB.png' , OOooO0OOoo , '' )
 o0OOoo0OO0OOO ( '[COLORgreen]My Online Zip[/COLOR]' , oO0o0o0ooO0oO , 43 , oOOoO0 + 'MB.png' , OOooO0OOoo , '' )
 if 54 - 54: OOOo0 / O0oO / iIii1I11I1II1 % Ooo00oOo00o % o00O0oo
def oooO ( ) :
 o0OOoo0OO0OOO ( 'INSTALL FTV GUIDE AND OTHER ADDONS REQUIRED' , OO0o + '/wizard/customftv/ftvguide-addons.zip' , 5 , oOOoO0 + 'FTV4.png' , OOooO0OOoo , '' )
 o0OOoo0OO0OOO ( 'FTV GUIDE FIRST RUN SETTINGS' , OO0o + '/wizard/customftv/settings.xml' , 17 , oOOoO0 + 'FTV3.png' , OOooO0OOoo , '' )
 o0OOoo0OO0OOO ( 'FTV GUIDE ADDONS2.INI UPDATE DAILY' , 'http://ren.byethost12.com/addons2.ini' , 16 , oOOoO0 + 'FTV1.png' , OOooO0OOoo , '' )
 o0OOoo0OO0OOO ( 'RESET FTV DATABASE' , 'url' , 18 , oOOoO0 + 'FTV2.png' , OOooO0OOoo , '' )
 if 71 - 71: o0000oOoOoO0o
 if 41 - 41: IIII / O0
 if 51 - 51: o0000oOoOoO0o % OOOo0
def OooOo ( ) :
 iiiiiIIii ( '[COLORgreen]SKINS[/COLOR]' , OO0o , 33 , oOOoO0 + 'skinp.png' , OOooO0OOoo , '' )
 iiiiiIIii ( '[COLORgreen]ARTWORK PACKS[/COLOR]' , OO0o , 34 , oOOoO0 + 'artp.png' , OOooO0OOoo , '' )
 iiiiiIIii ( '[COLORgreen]CREATE UNIVERSAL PATHS[/COLOR]' , iI111I11I1I1 , 35 , oOOoO0 + 'GUI.png' , OOooO0OOoo , '' )
 Oooo0Ooo000 ( 'movies' , 'MAIN' )
 if 31 - 31: O0oO
def OOO0000oO ( url ) :
 iI1i111I1Ii = O0ii1ii1ii ( i11i1ii1I ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 OOO00O = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( iI1i111I1Ii )
 for i1Oo00 , url , OOoOO0oo0ooO , O00O0oOO00O00 , III1iII1I1ii in OOO00O :
  iiiiiIIii ( i1Oo00 , url , 5 , OOoOO0oo0ooO , O00O0oOO00O00 , III1iII1I1ii )
 Oooo0Ooo000 ( 'movies' , 'MAIN' )
 if 88 - 88: o0000oOoOoO0o % ii11ii1ii
def I1i11 ( ) :
 iiiiiIIii ( '[COLORgreen]GOTHAM SKINS[/COLOR]' , OO0o , 36 , oOOoO0 + 'GSKIN.png' , OOooO0OOoo , '' )
 iiiiiIIii ( '[COLORgreen]HELIX SKINS[/COLOR]' , OO0o , 37 , oOOoO0 + 'HSKIN.png' , OOooO0OOoo , '' )
 iiiiiIIii ( '[COLORgreen]ISENGAARD SKINS[/COLOR]' , iI111I11I1I1 , 38 , oOOoO0 + 'ISKIN.png' , OOooO0OOoo , '' )
 Oooo0Ooo000 ( 'movies' , 'MAIN' )
 if 12 - 12: i1IIi + i1IIi - ii11ii1ii * Oo % Oo - OoOoOO00
def o0OOOOooo ( url ) :
 iI1i111I1Ii = O0ii1ii1ii ( OO0o + OooO0OO ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 OOO00O = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( iI1i111I1Ii )
 for i1Oo00 , url , OOoOO0oo0ooO , O00O0oOO00O00 , III1iII1I1ii in OOO00O :
  iiiiiIIii ( i1Oo00 , url , 42 , OOoOO0oo0ooO , O00O0oOO00O00 , III1iII1I1ii )
 Oooo0Ooo000 ( 'movies' , 'MAIN' )
 if 69 - 69: o0oO0 % OoOO
def ii1I1IIii11 ( url ) :
 iI1i111I1Ii = O0ii1ii1ii ( OO0o + O0o0oO ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 OOO00O = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( iI1i111I1Ii )
 for i1Oo00 , url , OOoOO0oo0ooO , O00O0oOO00O00 , III1iII1I1ii in OOO00O :
  iiiiiIIii ( i1Oo00 , url , 42 , OOoOO0oo0ooO , O00O0oOO00O00 , III1iII1I1ii )
 Oooo0Ooo000 ( 'movies' , 'MAIN' )
 if 38 - 38: OoOO % I1IiI + ii11ii1ii . i11iIiiIii
def oo0000ooooO0o ( url ) :
 iI1i111I1Ii = O0ii1ii1ii ( OO0o + iI1i11 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 OOO00O = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( iI1i111I1Ii )
 for i1Oo00 , url , OOoOO0oo0ooO , O00O0oOO00O00 , III1iII1I1ii in OOO00O :
  iiiiiIIii ( i1Oo00 , url , 42 , OOoOO0oo0ooO , O00O0oOO00O00 , III1iII1I1ii )
 Oooo0Ooo000 ( 'movies' , 'MAIN' )
 if 66 - 66: O0 % ii11ii1ii + i11iIiiIii . I1IiI / o00O0oo + ii11ii1ii
def ooo00Ooo ( url ) :
 iI1i111I1Ii = O0ii1ii1ii ( oOo0oooo00o ( 'aHR0cHM6Ly9kbC5kcm9wYm94dXNlcmNvbnRlbnQuY29tL3MvN2ZrMjhndDlwb3QxMjJhL0JVSUxEUy50eHQ/ZGw9MA==' ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 OOO00O = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( iI1i111I1Ii )
 for i1Oo00 , url , OOoOO0oo0ooO , O00O0oOO00O00 , III1iII1I1ii in OOO00O :
  iiiiiIIii ( i1Oo00 , url , 42 , OOoOO0oo0ooO , O00O0oOO00O00 , III1iII1I1ii )
 Oooo0Ooo000 ( 'movies' , 'MAIN' )
 if 93 - 93: i11iIiiIii - OOOo0 * ii11ii1ii * o0000oOoOoO0o % O0 + OoooooooOO
def I1i1i1 ( url ) :
 iI1i111I1Ii = O0ii1ii1ii ( OO0o + OoO0O00O0oo0O ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 OOO00O = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( iI1i111I1Ii )
 for i1Oo00 , url , OOoOO0oo0ooO , O00O0oOO00O00 , III1iII1I1ii in OOO00O :
  iiiiiIIii ( i1Oo00 , url , 40 , OOoOO0oo0ooO , O00O0oOO00O00 , III1iII1I1ii )
 Oooo0Ooo000 ( 'movies' , 'MAIN' )
 if 36 - 36: OoOO0ooOOoo0O + O0 - o00O0oo - O0 % o0000oOoOoO0o . OoOO
def ooo ( url ) :
 iI1i111I1Ii = O0ii1ii1ii ( OO0o + iiI ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 OOO00O = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( iI1i111I1Ii )
 for i1Oo00 , url , OOoOO0oo0ooO , O00O0oOO00O00 , III1iII1I1ii in OOO00O :
  iiiiiIIii ( i1Oo00 , url , 5 , OOoOO0oo0ooO , O00O0oOO00O00 , III1iII1I1ii )
 Oooo0Ooo000 ( 'movies' , 'MAIN' )
 if 56 - 56: Oo . ii11ii1ii . OOOo0
def ii111I ( ) :
 iiII1i1 = o00oOO0o ( oOo0oooo00o ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vYXBrdG9vbC9hcGsucGhw' ) )
 OOO00O = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( iiII1i1 )
 for ooOOO00Ooo , oOOo0 , i1Oo00 in OOO00O :
  iiIiIiiiII ( i1Oo00 , ooOOO00Ooo , 2031 , oOOo0 )
  if 20 - 20: OOOo0
def o0oO000oo ( name , url , description ) :
 o0oO00000 = xbmc . translatePath ( os . path . join ( o00o0 , 'Download' ) )
 i1111 = xbmcgui . DialogProgress ( )
 i1111 . create ( "Your App Is Downloading" , "Why not check out our website" , '' , 'Http://architects.x10host.com' )
 II1I = os . path . join ( o0oO00000 , name + '.apk' )
 try :
  os . remove ( II1I )
 except :
  pass
 downloader . download ( url , II1I , i1111 )
 ii11iIi1I = xbmcgui . Dialog ( )
 ii11iIi1I . ok ( "GenieTv" , "[COLORred]Please press ok, exit kodi and go to your downloads folder to install your app[/COLOR]" , "[COLORblue]Tool Brought To You By Architects@Work[/COLOR]" )
 if 12 - 12: OOooOOo - ii11ii1ii % I1IiI * o0000oOoOoO0o
def i11IIIiI11 ( url ) :
 o0oO00000 = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/resources/downloads' ) )
 i1111 = xbmcgui . DialogProgress ( )
 i1111 . create ( "Your fILM Is Downloading" , "Why not check out our website" , '' , 'Http://architects.x10host.com' )
 II1I = os . path . join ( o0oO00000 , i1Oo00 + '.mp4' )
 try :
  os . remove ( II1I )
 except :
  pass
 downloader . download ( url , II1I , i1111 )
 ii11iIi1I = xbmcgui . Dialog ( )
 ii11iIi1I . ok ( "GenieTv" , "[COLORred]Please press ok, Your download With Be Avaiilable Via The My Downloads Button[/COLOR]" , "[COLORblue]Tool Brought To You By Architects@Work[/COLOR]" )
 if 8 - 8: Ooo00oOo00o + O0oO - OOooOOo % Oo % OOooOOo * OoOO
 if 9 - 9: Oo - i11iIiiIii - OoOO0ooOOoo0O * o00O0oo + o0oO0
def iIIII ( name , url , description ) :
 o0oO00000 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 i1111 = xbmcgui . DialogProgress ( )
 i1111 . create ( "Your Art Pack Is Downloading" , "Why not check out our website" , '' , 'Http://architects.x10host.com' )
 II1I = os . path . join ( o0oO00000 , name )
 try :
  os . remove ( II1I )
 except :
  pass
 downloader . download ( url , II1I , i1111 )
 iIIIiiI1i1i = xbmc . translatePath ( os . path . join ( i1 ) )
 time . sleep ( 2 )
 i1111 . update ( 0 , "" , "Placing Your Art Please Wait" )
 print '======================================='
 print iIIIiiI1i1i
 print '======================================='
 extract . all ( II1I , iIIIiiI1i1i , i1111 )
 ii11iIi1I = xbmcgui . Dialog ( )
 ii11iIi1I . ok ( "GenieTv" , "[COLORred]Once complete your artwork will be stored in your Media folder, Accessible via the Homefolder, Enjoy[/COLOR]" )
 if 32 - 32: I1IiI / Ooo00oOo00o + OoOO0ooOOoo0O
 if 32 - 32: iIii1I11I1II1 % oO0o0ooO0
def O0o ( url ) :
 iI1i111I1Ii = O0ii1ii1ii ( oOo0oooo00o ( 'aHR0cDovL2dlbmlldHYuYXJjaGl0ZWN0cy54MTBob3N0LmNvbS90ZXN0L3doLnR4dA==' ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 OOO00O = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( iI1i111I1Ii )
 for i1Oo00 , url , OOoOO0oo0ooO , O00O0oOO00O00 , III1iII1I1ii in OOO00O :
  iiiiiIIii ( i1Oo00 , url , 5 , OOoOO0oo0ooO , O00O0oOO00O00 , III1iII1I1ii )
 try :
  iI1i111I1Ii = O0ii1ii1ii ( i1iIiIIi + oooOOOOO + oO0o00oo0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
  OOO00O = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( iI1i111I1Ii )
  for i1Oo00 , url , OOoOO0oo0ooO , O00O0oOO00O00 , III1iII1I1ii in OOO00O :
   iiiiiIIii ( i1Oo00 , url , 5 , OOoOO0oo0ooO , O00O0oOO00O00 , III1iII1I1ii )
 except : pass
 Oooo0Ooo000 ( 'movies' , 'INFO' )
 if 19 - 19: OoOoOO00 + IIII
 if 53 - 53: OoOO - OOOo0 - OoOO * oO0o0ooO0
def oooooo0OO ( url ) :
 iI1i111I1Ii = O0ii1ii1ii ( oOo0oooo00o ( 'aHR0cDovL2dlbmlldHYuYXJjaGl0ZWN0cy54MTBob3N0LmNvbS90ZXN0L3doLnR4dA==' ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 OOO00O = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( iI1i111I1Ii )
 for i1Oo00 , url , OOoOO0oo0ooO , O00O0oOO00O00 , III1iII1I1ii in OOO00O :
  iiiiiIIii ( i1Oo00 , url , 43 , OOoOO0oo0ooO , O00O0oOO00O00 , III1iII1I1ii )
 try :
  iI1i111I1Ii = O0ii1ii1ii ( i1iIiIIi + oooOOOOO + oO0o00oo0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
  OOO00O = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( iI1i111I1Ii )
  for i1Oo00 , url , OOoOO0oo0ooO , O00O0oOO00O00 , III1iII1I1ii in OOO00O :
   iiiiiIIii ( i1Oo00 , url , 43 , OOoOO0oo0ooO , O00O0oOO00O00 , III1iII1I1ii )
 except : pass
 Oooo0Ooo000 ( 'movies' , 'INFO' )
 if 14 - 14: OoOO / OoOO % o0oO0
 if 56 - 56: OOOo0 . O0 + Oo
def i1II1I1Iii1 ( name , url , description ) :
 o0oO00000 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 i1111 = xbmcgui . DialogProgress ( )
 i1111 . create ( "GenieTv" , "Downloading Content" , '' , 'Please Wait' )
 II1I = os . path . join ( o0oO00000 , name + '.zip' )
 try :
  os . remove ( II1I )
 except :
  pass
 downloader . download ( url , II1I , i1111 )
 iiI11Iii = xbmc . translatePath ( os . path . join ( 'special://home' , 'addons' ) )
 time . sleep ( 2 )
 i1111 . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print iiI11Iii
 print '======================================='
 extract . all ( II1I , iiI11Iii , i1111 )
 ii11iIi1I = xbmcgui . Dialog ( )
 ii11iIi1I . ok ( "GenieTv" , "Press ok to finish install" , "[COLOR yellow]Brought To You By Architects@Work[/COLOR]" )
 O0o0O0 ( )
 if 11 - 11: OoOoOO00 % Ooo00oOo00o * oO0o0ooO0 + o0oO0 + o00O0oo
 if 24 - 24: Oo - OoOO % iIii1I11I1II1 . i1IIi / O0
def ii1ii111 ( name , url , description ) :
 o0oO00000 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 i1111 = xbmcgui . DialogProgress ( )
 i1111 . create ( "GenieTv" , "Downloading " , '' , 'Please Wait' )
 II1I = os . path . join ( o0oO00000 , 'plugin.program.GenieTv.install' + '.zip' )
 try :
  os . remove ( II1I )
 except :
  pass
 downloader . download ( url , II1I , i1111 )
 iiI11Iii = xbmc . translatePath ( os . path . join ( 'special://' , 'home' ) )
 time . sleep ( 2 )
 i1111 . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print iiI11Iii
 print '======================================='
 extract . all ( II1I , iiI11Iii , i1111 )
 ii11iIi1I = xbmcgui . Dialog ( )
 ii11iIi1I . ok ( "GenieTv" , "Press ok to force close kodi, if unsuccessful using windows Please kill kodi via taskmanager" , "[COLOR yellow]Brought To You By Architects@Work[/COLOR]" )
 I111i1i1111 ( )
 if 49 - 49: Ooo00oOo00o / OoOO + O0 * OOooOOo
def I1ii11 ( name , url , description ) :
 o0oO00000 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 i1111 = xbmcgui . DialogProgress ( )
 i1111 . create ( "GenieTv" , "Downloading " , '' , 'Please Wait' )
 II1I = os . path . join ( o0oO00000 , 'plugin.program.GenieTv.install' + '.zip' )
 try :
  os . remove ( II1I )
 except :
  pass
 downloader . download ( url , II1I , i1111 )
 iiI11Iii = xbmc . translatePath ( os . path . join ( 'special://' , 'home' ) )
 time . sleep ( 2 )
 i1111 . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print iiI11Iii
 print '======================================='
 extract . all ( II1I , iiI11Iii , i1111 )
 ii11iIi1I = xbmcgui . Dialog ( )
 ii11iIi1I . ok ( "GenieTv" , "Please Disconnect The Power From Your Device. DO NOT EXIT CLEANLY VIA SHUTDOWN" , "[COLOR yellow]Brought To You By Architects@Work[/COLOR]" )
 if 74 - 74: Oo - OOooOOo . i1IIi
 if 43 - 43: oO0o0ooO0 / OOOo0
def OO0oo0O ( name , url , description ) :
 iiI11Iii = xbmc . translatePath ( os . path . join ( 'special://' , 'home' ) )
 i1111 = xbmcgui . DialogProgress ( )
 II1I = os . path . join ( oo0o0O00 )
 time . sleep ( 2 )
 i1111 . create ( "GenieTv" , "Restoring" , '' , 'Please Wait' )
 print '======================================='
 print iiI11Iii
 print '======================================='
 extract . all ( II1I , iiI11Iii , i1111 )
 ii11iIi1I = xbmcgui . Dialog ( )
 ii11iIi1I . ok ( "GenieTv" , "Please Disconnect The Power From Your Device. DO NOT EXIT CLEANLY VIA SHUTDOWN" , "[COLOR yellow]Brought To You By Architects@Work[/COLOR]" )
 if 13 - 13: i11iIiiIii + i1IIi * iIii1I11I1II1 % OoooooooOO - OoOoOO00 * OoOO0ooOOoo0O
 if 26 - 26: OoooooooOO * OOOo0 + OoOO0ooOOoo0O
def I111i1i1111 ( ) :
 IiIii1i111 = xbmcgui . Dialog ( ) . yesno ( 'Force Close Kodi' , 'You are about to close Kodi' , 'Would you like to continue?' , nolabel = 'No, Cancel' , yeslabel = 'Yes, Close' )
 if IiIii1i111 == 0 :
  return
 elif IiIii1i111 == 1 :
  pass
 iI = o0o00 ( )
 print "Platform: " + str ( iI )
 if iI == 'osx' :
  print "############   try osx force close  #################"
  try : os . system ( 'killall -9 XBMC' )
  except : pass
  try : os . system ( 'killall -9 Kodi' )
  except : pass
  ii11iIi1I . ok ( "[COLOR=red][B]WARNING  !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu." , '' )
 elif iI == 'linux' :
  print "############   try linux force close  #################"
  try : os . system ( 'killall XBMC' )
  except : pass
  try : os . system ( 'killall Kodi' )
  except : pass
  try : os . system ( 'killall -9 xbmc.bin' )
  except : pass
  try : os . system ( 'killall -9 kodi.bin' )
  except : pass
  ii11iIi1I . ok ( "[COLOR=red][B]WARNING  !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu." , '' )
 elif iI == 'android' :
  print "############   try android force close  #################"
  try : os . system ( 'adb shell am force-stop org.xbmc.kodi' )
  except : pass
  try : os . system ( 'adb shell am force-stop org.kodi' )
  except : pass
  try : os . system ( 'adb shell am force-stop org.xbmc.xbmc' )
  except : pass
  try : os . system ( 'adb shell am force-stop org.xbmc' )
  except : pass
  ii11iIi1I . ok ( "[COLOR=red][B]WARNING  !!![/COLOR][/B]" , "Your system has been detected as Android, you " , "[COLOR=yellow][B]MUST[/COLOR][/B] force close XBMC/Kodi. [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu." , "Pulling the power cable is the simplest method to force close." )
 elif iI == 'windows' :
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
  ii11iIi1I . ok ( "[COLOR=red][B]WARNING  !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu." , "Use task manager and NOT ALT F4" )
 else :
  print "############   try atv force close  #################"
  try : os . system ( 'killall AppleTV' )
  except : pass
  print "############   try raspbmc force close  #################"
  try : os . system ( 'sudo initctl stop kodi' )
  except : pass
  try : os . system ( 'sudo initctl stop xbmc' )
  except : pass
  ii11iIi1I . ok ( "[COLOR=red][B]WARNING  !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit via the menu." , "Your platform could not be detected so just pull the power cable." )
  if 14 - 14: OOooOOo . OoOO0ooOOoo0O . o0000oOoOoO0o + OoooooooOO - OoOO0ooOOoo0O + IIII
def o0o00 ( ) :
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
  if 9 - 9: o00O0oo
  if 59 - 59: OOOo0 * OoOoOO00 . O0
  if 56 - 56: o00O0oo - oO0o0ooO0 % OOOo0 - OOooOOo
def Oo00O ( url ) :
 i1111 . create ( "[COLOR=green]GenieTv[/COLOR]" , "Renaming paths..." , '' , 'Please Wait' )
 for iI111i1II , iIIIiIi , OO0O0 in os . walk ( url ) :
  for file in OO0O0 :
   if file . endswith ( ".xml" ) :
    i1111 . update ( 0 , "Fixing" , file , 'Please Wait' )
    ooO0oOOooOo0 = open ( ( os . path . join ( iI111i1II , file ) ) ) . read ( )
    O0ooooo0OOOO0 = ooO0oOOooOo0 . replace ( iI111I11I1I1 , 'special://home/' )
    O0ooO0Oo00o = open ( ( os . path . join ( iI111i1II , file ) ) , mode = 'w' )
    O0ooO0Oo00o . write ( str ( O0ooooo0OOOO0 ) )
    O0ooO0Oo00o . close ( )
 I111i1i1111 ( )
 if 9 - 9: OoOoOO00 - OOooOOo / oO0o0ooO0 / OOooOOo
def I1i111iiIIIi ( ) :
 iiII1i1 = o00oOO0o ( oOo0oooo00o ( 'aHR0cDovL3d3dy5saXN0ZW5saXZlLmV1L3VrLmh0bWw=' ) )
 OOO00O = re . compile ( '<tr>.+?<td><a href=".+?"><b>(.+?)</b>.+?<td><a href="(.+?)">' , re . DOTALL ) . findall ( iiII1i1 )
 for i1Oo00 , ooOOO00Ooo in OOO00O :
  O00 ( i1Oo00 , ooOOO00Ooo , 222 , oOOoO0 + 'radio.png' )
  if 17 - 17: o00O0oo - OoooooooOO % o00O0oo . IIII / i11iIiiIii % oO0o0ooO0
def iIiIIIIIii ( ) :
 iiII1i1 = o00oOO0o ( oOo0oooo00o ( 'aHR0cDovL3d3dy50b29uamV0LmNvbS8=' ) )
 OOO00O = re . compile ( '<a href="(.+?)" style="font-size:.8em;">(.+?)</a>' ) . findall ( iiII1i1 )
 for ooOOO00Ooo , i1Oo00 in OOO00O :
  iiIiIiiiII ( '[COLORgreen]' + i1Oo00 + '[/COLOR]' , 'http://www.toonjet.com/' + ooOOO00Ooo , 8051 , oOOoO0 + 'classictoons.png' )
def OOo0 ( url ) :
 iiII1i1 = o00oOO0o ( url )
 OOO00O = re . compile ( '<a href="(.+?)"><img src="(.+?)"' ) . findall ( iiII1i1 )
 ii11I1 = re . compile ( '<a href="(.+?)">.+?</a></td></tr></table>' ) . findall ( iiII1i1 )
 for url , oooooOoo0ooo in OOO00O :
  if 'ol.gif' in oooooOoo0ooo :
   pass
  elif 'link_block_' in oooooOoo0ooo :
   pass
  elif '.png' in oooooOoo0ooo :
   pass
  else :
   iiIiIiiiII ( ( oooooOoo0ooo ) . replace ( 'http://www.toonjet.com/images/icons/' , '' ) . replace ( 'images/icons/' , '' ) . replace ( '.jpg' , '' ) . replace ( '_icon' , '' ) . replace ( '_' , ' ' ) , 'http://www.toonjet.com/' + url , 8052 , oOOoO0 + 'vod.png' )
 for url in ii11I1 :
  iiIiIiiiII ( 'NEXT PAGE' , 'http://www.toonjet.com/' + url , 8051 , oOOoO0 + 'documentary.png' )
def oO0oo ( url ) :
 iiII1i1 = o00oOO0o ( url )
 OOO00O = re . compile ( '<iframe width="640" height="480" src="(.+?)" frameborder="0" allowfullscreen></iframe>' ) . findall ( iiII1i1 )
 for url in OOO00O :
  O00 ( '[COLORgreen]PLAY[/COLOR]' , ( url ) . replace ( 'http://www.youtube.com/embed/' , '' ) . replace ( '?autoplay=0' , '' ) , 8043 , oOOoO0 + 'classictoons.png' )
  if 38 - 38: OoooooooOO * o0oO0 % O0 * I1IiI
  if 29 - 29: ii11ii1ii / i1IIi . OOOo0 - I1IiI - I1IiI - o00O0oo
def IiiIiI111iI ( ) :
 OOo ( 'Audio Books' , '' , 30011 , oOOoO0 + 'audiobooks.png' , oOOoO0 + 'audiobooks.png' , '' )
 OOo ( 'Kids Audio Books' , '' , 30006 , oOOoO0 + 'kidsaudiobooks.png' , oOOoO0 + 'kidsaudiobooks.png' , '' )
 if 50 - 50: o0oO0
def o0O0O0ooo0oOO ( ) :
 OOo ( 'All' , '' , 30001 , oOOoO0 + 'kodible.png' , oOOoO0 + 'kodible.png' , '' )
 OOo ( 'Popular' , '' , 30012 , oOOoO0 + 'POPULARv.png' , oOOoO0 + 'POPULARv.png' , '' )
 OOo ( 'Search' , '' , 30013 , oOOoO0 + 'search.png' , oOOoO0 + 'search.png' , '' )
 if 97 - 97: OOOo0 / oO0o0ooO0
def Oooo0 ( ) :
 oO0OOoo0OO = O0ii1ii1ii ( Oo00OOOOO + 'books' + O0o0Oo )
 OOO00O = re . compile ( '<NAME=>(.*?)</NAME><URL=>(.*?)</URL><CAT=>(.*?)</CAT>' ) . findall ( oO0OOoo0OO )
 for i1Oo00 , ooOOO00Ooo , oOO in OOO00O :
  if 'Parent' in i1Oo00 :
   pass
  elif '2' in oOO :
   OOo ( ( i1Oo00 ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , ooOOO00Ooo , 30010 , oOOoO0 + 'kodible.png' , oOOoO0 + 'kodible.png' , '' )
   if 54 - 54: OOOo0 / iIii1I11I1II1 / OoOO0ooOOoo0O . OoOO0ooOOoo0O % oO0o0ooO0 . OOOo0
def iI1i1i ( ) :
 O00OOOoOoo0O = Oo0o0000o0o0 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oo0OOo = O00OOOoOoo0O . lower ( )
 oO0OOoo0OO = O0ii1ii1ii ( Oo00OOOOO + 'books' + O0o0Oo )
 OOO00O = re . compile ( '<NAME=>(.*?)</NAME><URL=>(.*?)</URL><CAT=>(.*?)</CAT>' ) . findall ( oO0OOoo0OO )
 for i1Oo00 , ooOOO00Ooo , oOO in OOO00O :
  if O00OOOoOoo0O in i1Oo00 . lower ( ) :
   if '1' in oOO :
    OOo ( ( i1Oo00 ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , ooOOO00Ooo , 30010 , oOOoO0 + 'kodible.png' , oOOoO0 + 'kodible.png' , '' )
   elif '2' in oOO :
    OOo ( ( i1Oo00 ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , ooOOO00Ooo , 30010 , oOOoO0 + 'kodible.png' , oOOoO0 + 'kodible.png' , '' )
   elif '3' in oOO :
    OOo ( ( i1Oo00 ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , ooOOO00Ooo , 30009 , oOOoO0 + 'kodible.png' , oOOoO0 + 'kodible.png' , '' )
    if 41 - 41: i1IIi % oO0o0ooO0 + iIii1I11I1II1
    if 2 - 2: iIii1I11I1II1 * Oo % OoOO - OoOoOO00 - oO0o0ooO0
def iIi11iiIiI1I ( ) :
 oO0OOoo0OO = O0ii1ii1ii ( Oo00OOOOO + 'books' + O0o0Oo )
 OOO00O = re . compile ( '<NAME=>(.*?)</NAME><URL=>(.*?)</URL><CAT=>(.*?)</CAT>' ) . findall ( oO0OOoo0OO )
 for i1Oo00 , ooOOO00Ooo , oOO in OOO00O :
  if '1' in oOO :
   OOo ( ( i1Oo00 ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , ooOOO00Ooo , 3010 , oOOoO0 + 'kodible.png' , oOOoO0 + 'kodible.png' , '' )
  elif '2' in oOO :
   OOo ( ( i1Oo00 ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , ooOOO00Ooo , 30010 , oOOoO0 + 'kodible.png' , oOOoO0 + 'kodible.png' , '' )
  elif '3' in oOO :
   OOo ( ( i1Oo00 ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , ooOOO00Ooo , 30009 , oOOoO0 + 'kodible.png' , oOOoO0 + 'kodible.png' , '' )
   if 3 - 3: i1IIi / OoOoOO00 / i11iIiiIii * i1IIi - OoOoOO00
 xbmcplugin . addSortMethod ( o0 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 42 - 42: OoOoOO00 . OoooooooOO . OOooOOo * OoOO
def O0OOO0OOooo00 ( url ) :
 I111iIi1 = url
 oO0OOoo0OO = O0ii1ii1ii ( url )
 ii11I1 = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( oO0OOoo0OO )
 for url , i1Oo00 in ii11I1 :
  if 'mp3' in i1Oo00 :
   iiiiiIIii ( ( i1Oo00 ) . replace ( '%20' , ' ' ) , I111iIi1 + url , 10012 , oOOoO0 + 'kodible.png' , oOOoO0 + 'kodible.png' , '' )
  if 'wma' in i1Oo00 :
   iiiiiIIii ( ( i1Oo00 ) . replace ( '%20' , ' ' ) , I111iIi1 + url , 10012 , oOOoO0 + 'kodible.png' , oOOoO0 + 'kodible.png' , '' )
  if 'm4b' in i1Oo00 :
   iiiiiIIii ( ( i1Oo00 ) . replace ( '%20' , ' ' ) , I111iIi1 + url , 10012 , oOOoO0 + 'kodible.png' , oOOoO0 + 'kodible.png' , '' )
  elif '/' in i1Oo00 :
   OOo ( ( i1Oo00 ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , I111iIi1 + url , 30009 , oOOoO0 + 'kodible.png' , oOOoO0 + 'kodible.png' , '' )
   if 92 - 92: o0oO0
   if 22 - 22: Oo % oO0o0ooO0 * ii11ii1ii / OoOO0ooOOoo0O % i11iIiiIii * o0000oOoOoO0o
   if 95 - 95: OoooooooOO - IIII * OOOo0 + I1IiI
def iIi1 ( url ) :
 oO0OOoo0OO = O0ii1ii1ii ( url )
 I111iIi1 = url
 OOO00O = re . compile ( '<li><a href="(.+?)">(.+?)</a></li>' ) . findall ( oO0OOoo0OO )
 for url , i1Oo00 in OOO00O :
  if 'Parent' in i1Oo00 :
   pass
  elif '.db' in i1Oo00 :
   pass
  elif '.jpg' in i1Oo00 :
   pass
  elif '.html' in i1Oo00 :
   pass
  elif '.doc' in i1Oo00 :
   pass
  elif 'mp3' in i1Oo00 :
   iiiiiIIii ( ( i1Oo00 ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , I111iIi1 + url , 10012 , oOOoO0 + 'kodible.png' , oOOoO0 + 'kodible.png' , '' )
  elif 'm4a' in i1Oo00 :
   iiiiiIIii ( ( i1Oo00 ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , I111iIi1 + url , 10012 , oOOoO0 + 'kodible.png' , oOOoO0 + 'kodible.png' , '' )
  else :
   OOo ( ( i1Oo00 ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , I111iIi1 + url , 30010 , oOOoO0 + 'kodible.png' , oOOoO0 + 'kodible.png' , '' )
   if 21 - 21: o0000oOoOoO0o
   if 92 - 92: i11iIiiIii / O0oO - oO0o0ooO0 % o0oO0 * O0oO + Oo
def ii1Oo0000oOo ( ) :
 OOo ( 'A-Z' , '' , 7 , oOOoO0 + 'kodible.png' , oOOoO0 + 'kodible.png' , '' )
 OOo ( 'All' , '' , 3 , oOOoO0 + 'kodible.png' , oOOoO0 + 'kodible.png' , '' )
 OOo ( 'Search' , '' , 14 , oOOoO0 + 'kodible.png' , oOOoO0 + 'kodible.png' , '' )
 if 31 - 31: o0000oOoOoO0o . O0oO * o0oO0 + i11iIiiIii * OoOO
def OO0ooo0o0O0Oooooo ( ) :
 oO0OOoo0OO = O0ii1ii1ii ( oOo0oooo00o ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9tcDNfZG93bmxvYWRzLmh0bQ==' ) )
 OOO00O = re . compile ( '<td width=".+?" align="center">.+?<a href="(.*?)">.+?<img border="0" src="images/Squeeze%20(.*?).gif" width="74" height=".*?"></a></td>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for ooOOO00Ooo , oooooOoo0ooo in OOO00O :
  print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<' + ooOOO00Ooo + '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
  if '-x' in oooooOoo0ooo :
   pass
  else :
   OOo ( oooooOoo0ooo , ( oOo0oooo00o ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) ) + ( ooOOO00Ooo ) . replace ( 'colour_it' , 'books_audio/audio_books_a' ) , 30008 , ( oOo0oooo00o ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9pbWFnZXMvU3F1ZWV6ZSUyMA==' ) ) + oooooOoo0ooo + '.gif' , oOOoO0 + 'kodible.png' , '' )
   if 1 - 1: o0oO0 % I1IiI * Oo
 xbmcplugin . addSortMethod ( o0 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 55 - 55: I1IiI
 if 87 - 87: OoooooooOO % oO0o0ooO0 . OOOo0 / o0oO0
def i1I1iI ( url ) :
 oO0OOoo0OO = O0ii1ii1ii ( url )
 OOO00O = re . compile ( '<td width=".*?" height=".*?"><b>.*?<a href="(.*?)">(.*?)</a></b></td>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for url , i1Oo00 in OOO00O :
  if '</a>' in i1Oo00 :
   pass
  elif '(' in i1Oo00 :
   OOo ( ( i1Oo00 ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '.mp3' , '' ) , oOo0oooo00o ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) + url , 30005 , oOOoO0 + 'kodible.png' , oOOoO0 + 'kodible.png' , '' )
  else :
   iiiiiIIii ( ( i1Oo00 ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '.mp3' , '' ) , oOo0oooo00o ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) + url , 30004 , oOOoO0 + 'kodible.png' , oOOoO0 + 'kodible.png' , '' )
   if 62 - 62: O0oO . IIII . OoooooooOO
 xbmcplugin . addSortMethod ( o0 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 11 - 11: OoOO0ooOOoo0O / o0000oOoOoO0o
def oooO0 ( ) :
 O00OOOoOoo0O = Oo0o0000o0o0 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oo0OOo = O00OOOoOoo0O . lower ( )
 oO0OOoo0OO = O0ii1ii1ii ( oOo0oooo00o ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9jb21wbGV0ZV9saXN0Lmh0bQ==' ) )
 OOO00O = re . compile ( '<td width=".+?">.*?<b>.+?<a href="(.*?)">(.*?)</a></b></td>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for ooOOO00Ooo , i1Oo00 in OOO00O :
  if O00OOOoOoo0O in i1Oo00 . lower ( ) :
   if '</a>' in i1Oo00 :
    pass
   elif '(' in i1Oo00 :
    OOo ( ( i1Oo00 ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , oOo0oooo00o ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + ooOOO00Ooo , 30005 , oOOoO0 + 'kodible.png' , oOOoO0 + 'kodible.png' , '' )
   else :
    iiiiiIIii ( ( i1Oo00 ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , oOo0oooo00o ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + ooOOO00Ooo , 30004 , oOOoO0 + 'kodible.png' , oOOoO0 + 'kodible.png' , '' )
    if 16 - 16: OoOoOO00 + OoOO - OoooooooOO
    if 3 - 3: O0 / oO0o0ooO0
def iIiIi1I ( ) :
 oO0OOoo0OO = O0ii1ii1ii ( oOo0oooo00o ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9jb21wbGV0ZV9saXN0Lmh0bQ==' ) )
 OOO00O = re . compile ( '<td width=".+?">.*?<b>.+?<a href="(.*?)">(.*?)</a></b></td>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for ooOOO00Ooo , i1Oo00 in OOO00O :
  if '</a>' in i1Oo00 :
   pass
  elif '(' in i1Oo00 :
   OOo ( ( i1Oo00 ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , oOo0oooo00o ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + ooOOO00Ooo , 30005 , oOOoO0 + 'kodible.png' , oOOoO0 + 'kodible.png' , '' )
  else :
   iiiiiIIii ( ( i1Oo00 ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , oOo0oooo00o ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + ooOOO00Ooo , 30004 , oOOoO0 + 'kodible.png' , oOOoO0 + 'kodible.png' , '' )
   if 45 - 45: i1IIi + OoOoOO00
 xbmcplugin . addSortMethod ( o0 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 7 - 7: O0 % OOooOOo + ii11ii1ii * oO0o0ooO0 - oO0o0ooO0
 if 42 - 42: I1IiI * I1IiI * O0oO . o0000oOoOoO0o
def O0Oo0o000oO ( url ) :
 oO0OOoo0OO = O0ii1ii1ii ( url )
 OOO00O = re . compile ( '<a href="(.+?)">Download</a></b></td>' ) . findall ( oO0OOoo0OO )
 for url in OOO00O :
  I111iIi1 = ( oOo0oooo00o ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) ) + url
  Resolve ( I111iIi1 )
  if 99 - 99: OoOO * OoOoOO00 * O0oO
def oOooO0OOOoO000 ( url ) :
 oO0OOoo0OO = O0ii1ii1ii ( url )
 OOO00O = re . compile ( '<td width="247">(.*?)</td>.*?<a href="(.+?)">' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for i1Oo00 , url in OOO00O :
  if '<p align' in i1Oo00 :
   pass
  elif '&nbsp;' in i1Oo00 :
   pass
  else :
   iiiiiIIii ( ( i1Oo00 ) . replace ( '&nbsp;' , '' ) , oOo0oooo00o ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) + url , 10012 , oOOoO0 + 'kodible.png' , oOOoO0 + 'kodible.png' , '' )
   if 57 - 57: OoOoOO00
 xbmcplugin . addSortMethod ( o0 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 54 - 54: Oo + OoOO + i11iIiiIii
 if 28 - 28: OoOO
def ooo000o0ooO0 ( ) :
 oO0OOoo0OO = cloudflare . source ( oOo0oooo00o ( 'aHR0cDovL3dhdGNoY2FydG9vbnNvbmxpbmUuZXUv' ) )
 OOO00O = re . compile ( 'class="menu-item menu-item-type-.+?><a href="([^"]*)">(.+?)</a></li>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for ooOOO00Ooo , i1Oo00 in OOO00O :
  if 'ongoing' in ooOOO00Ooo :
   iiiiiIIii ( '[COLORgreen]' + i1Oo00 + '[/COLOR]' , ooOOO00Ooo , 21005 , oOOoO0 + 'on-going.png' , '' , '' )
  if 'cartoon-series' in ooOOO00Ooo :
   iiiiiIIii ( '[COLORgreen]' + i1Oo00 + '[/COLOR]' , ooOOO00Ooo , 21005 , oOOoO0 + 'cartoonseries.png' , '' , '' )
  if 'disney' in ooOOO00Ooo :
   iiiiiIIii ( '[COLORgreen]' + i1Oo00 + '[/COLOR]' , ooOOO00Ooo , 21005 , oOOoO0 + 'disneytoons.png' , '' , '' )
  if 'genre' in ooOOO00Ooo :
   iiiiiIIii ( '[COLORgreen]' + i1Oo00 + '[/COLOR]' , ooOOO00Ooo , 21005 , oOOoO0 + 'cartoongenre.png' , '' , '' )
  if 'years' in ooOOO00Ooo :
   iiiiiIIii ( '[COLORgreen]' + i1Oo00 + '[/COLOR]' , ooOOO00Ooo , 21005 , oOOoO0 + 'years.png' , '' , '' )
def I1I ( url ) :
 oO0OOoo0OO = cloudflare . source ( url )
 OOO00O = re . compile ( '<a href="([^"]*)" title="([^"]*)" rel="nofollow" id="featured-thumbnail">.+?<div class="featured-thumbnail"><img width="140" height="200" src="([^"]*)"' , re . DOTALL ) . findall ( oO0OOoo0OO )
 oOoo000 = re . compile ( '<button type="button"><a href="([^"]*)" target="_blank">(.+?)</a>' ) . findall ( oO0OOoo0OO )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' ) . findall ( oO0OOoo0OO )
 for url , i1Oo00 , oooooOoo0ooo in OOO00O :
  iiiiiIIii ( '[COLORgreen]' + i1Oo00 + '[/COLOR]' , url , 21006 , oooooOoo0ooo , oooooOoo0ooo , i1Oo00 )
 for url , i1Oo00 in oOoo000 :
  iiiiiIIii ( '[COLORgreen]' + i1Oo00 + '[/COLOR]' , url , 21005 , oOOoO0 + 'watchcartoons.png' , '' , '' )
 for url in next :
  iiiiiIIii ( '[COLORgreen]NEXT[/COLOR]' , url , 21005 , oOOoO0 + 'watchcartoons.png' , '' , '' )
def OooOo00o ( url ) :
 oO0OOoo0OO = cloudflare . source ( url )
 OOO00O = re . compile ( '<li><a href="([^"]*)" >(.+?)</a></li>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 IiI11i1IIiiI = re . compile ( 'file:"([^"]*)",type:"mp4",label:"([^"]*)"' , re . DOTALL ) . findall ( oO0OOoo0OO )
 oOOo000oOoO0 = re . compile ( 'src="([^"]*)" frameborder=' ) . findall ( oO0OOoo0OO )
 OoOo00o0OO = re . compile ( '<iframe src="([^"]*)"' ) . findall ( oO0OOoo0OO )
 for url , i1Oo00 in OOO00O :
  iiiiiIIii ( '[COLORgreen]' + i1Oo00 + '[/COLOR]' , url , 21007 , oOOoO0 + 'watchcartoons.png' , '' , '' )
 for url in oOOo000oOoO0 :
  iiiiiIIii ( '[COLORgreen]PLAY[/COLOR]' , 'http:' + url , 222 , oOOoO0 + 'watchcartoons.png' , '' , '' )
 for url , i1Oo00 in IiI11i1IIiiI :
  o0OOoo0OO0OOO ( '[COLORgreen]' + i1Oo00 + '[/COLOR]' , url , 222 , oOOoO0 + 'watchcartoons.png' , '' , '' )
 else :
  iiiiiIIii ( '[COLORgreen]NO STREAMS AVAILABLE[/COLOR]' , url , 21005 , oOOoO0 + 'watchcartoons.png' , '' , '' )
def ii1IIIIiI11 ( url ) :
 oO0OOoo0OO = cloudflare . source ( url )
 OOO00O = re . compile ( 'file:"([^"]*)",type:"mp4",label:"([^"]*)"' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for url , i1Oo00 in OOO00O :
  o0OOoo0OO0OOO ( '[COLORgreen]' + i1Oo00 + '[/COLOR]' , url , 222 , oOOoO0 + 'watchcartoons.png' , '' , '' )
  if 40 - 40: OOooOOo
def OOOooo ( ) :
 iiIiIiiiII ( '[COLORgreen]CARTOONS[/COLOR]' , '' , 20001 , oOOoO0 + 'ORIGINCARTOON.png' )
 iiIiIiiiII ( '[COLORgreen]ANIME[/COLOR]' , 'https://kissanime.to/AnimeList' , 20001 , oOOoO0 + 'ORIGINCARTOON.png' )
 if 99 - 99: OoOoOO00 * IIII % iIii1I11I1II1 / o00O0oo
def OOO00O0oOOo ( ) :
 iiIiIiiiII ( '[COLORgreen]BY NAME[/COLOR]' , 'http://kisscartoon.me/CartoonList' , 20002 , oOOoO0 + 'ORIGINCARTOON.png' )
 iiIiIiiiII ( '[COLORgreen]BY GENRE[/COLOR]' , 'http://kisscartoon.me/CartoonList' , 20003 , oOOoO0 + 'ORIGINCARTOON.png' )
 if 71 - 71: o0000oOoOoO0o / OOooOOo / O0oO % OoOO0ooOOoo0O
def O0oooo00o0Oo ( url ) :
 oO0OOoo0OO = cloudflare . source ( url )
 OOO00O = re . compile ( 'href="(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for url , i1Oo00 in OOO00O :
  if '?c=' in url :
   iiIiIiiiII ( '[COLORgreen]' + i1Oo00 + '[/COLOR]' , 'http://kisscartoon.me' + url , 20004 , oOOoO0 + 'ORIGINCARTOON.png' )
   if 36 - 36: o00O0oo / OoOoOO00 / IIII / IIII + ii11ii1ii
def oO0Ooo0ooOO0 ( url ) :
 oO0OOoo0OO = cloudflare . source ( url )
 OOO00O = re . compile ( 'href="(.+?)" title="(.+?)">/n(.+?)</a><br/>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for url , i1IIiIii1i , i1Oo00 in OOO00O :
  if 'Genre' in url :
   iiIiIiiiII ( '[COLORgreen]' + i1Oo00 + '[/COLOR]' , 'http://kisscartoon.me' + url , 20004 , oOOoO0 + 'ORIGINCARTOON.png' )
   if 77 - 77: O0 % OoOO - Ooo00oOo00o
def ooi1i1I ( url ) :
 oO0OOoo0OO = cloudflare . source ( url )
 OOO00O = re . compile ( 'src="(.+?)" style=.+?<a class="bigChar" href="(.+?)">(.+?)</a>.+?<p>(.+?)</p>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for url , i1IIiIii1i , i1Oo00 in OOO00O :
  iiiiiIIii ( '[COLORgreen]' + i1Oo00 + '[/COLOR]' , 'http://kisscartoon.me' + url , 20005 , img , '' , i1IIiIii1i )
  if 25 - 25: iIii1I11I1II1 + ii11ii1ii + oO0o0ooO0 / OoOoOO00 / o0000oOoOoO0o
def o0O0Oo00Oo0o ( url ) :
 oO0OOoo0OO = cloudflare . source ( url )
 OOO00O = re . compile ( '<img width="120" height="165" src="(.+?)" style=.+?<a class="bigChar" href="(.+?)">(.+?)</a>.+?<p>(.+?)</p>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for url , i1IIiIii1i , i1Oo00 in OOO00O :
  iiiiiIIii ( '[COLORgreen]' + i1Oo00 + '[/COLOR]' , 'http://kisscartoon.me' + url , 20005 , img , '' , i1IIiIii1i )
  if 74 - 74: Oo / i11iIiiIii - OoOoOO00 * OOooOOo
  if 5 - 5: OoOO0ooOOoo0O - OoOO0ooOOoo0O . Oo + I1IiI - OoOO0ooOOoo0O . OoOO
  if 31 - 31: OoOoOO00 - iIii1I11I1II1 - iIii1I11I1II1 % o0000oOoOoO0o
  if 12 - 12: iIii1I11I1II1
  if 20 - 20: OOooOOo / i1IIi
def oOIi111 ( ) :
 if 67 - 67: O0
 iiiiiIIii ( '[COLORgreen]Cartoons[/COLOR]' , '' , 10004 , oOOoO0 + 'ORIGINCARTOON.png' , OOooO0OOoo , '' )
 iiiiiIIii ( '[COLORgreen]Search Cartoons[/COLOR]' , '' , 10005 , oOOoO0 + 'ORIGINCARTOON.png' , OOooO0OOoo , '' )
 if 52 - 52: OoOoOO00 . o0oO0 / I1IiI / OoooooooOO . i11iIiiIii
def I1i1i ( ) :
 O00OOOoOoo0O = Oo0o0000o0o0 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oo0OOo = O00OOOoOoo0O . lower ( )
 oO0OOoo0OO = O0ii1ii1ii ( oOo0oooo00o ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2NhcnRvb24=' ) )
 OOO00O = re . compile ( '<td><a href="(.+?)">(.+)</a></td>' ) . findall ( oO0OOoo0OO )
 for ooOOO00Ooo , i1Oo00 in OOO00O :
  if O00OOOoOoo0O in i1Oo00 . lower ( ) :
   if 'Dad!' in i1Oo00 :
    pass
   elif 'Family Guy' in i1Oo00 :
    pass
   elif '2 Stupid' in i1Oo00 :
    pass
   elif 'The Zelfs' in i1Oo00 :
    pass
   elif 'A Clone' in i1Oo00 :
    pass
   elif 'A.T.O.M' in i1Oo00 :
    pass
   elif 'Almost Naked' in i1Oo00 :
    pass
   elif 'Angry Kid' in i1Oo00 :
    pass
   elif 'Annoying Orange' in i1Oo00 :
    pass
   elif 'Aqua Teen' in i1Oo00 :
    pass
   elif 'Assy Mcgee' in i1Oo00 :
    pass
   elif 'Astroblast' in i1Oo00 :
    pass
   elif 'Atomic Betty' in i1Oo00 :
    pass
   elif 'Axe Cop' in i1Oo00 :
    pass
   elif 'Baby Playpen' in i1Oo00 :
    pass
   elif 'Beavis and Butt' in i1Oo00 :
    pass
   elif 'Celebrity Deathmatch' in i1Oo00 :
    pass
   elif 'Clerks The' in i1Oo00 :
    pass
   elif 'Crapston Villas' in i1Oo00 :
    pass
   elif 'Duckman:' in i1Oo00 :
    pass
   elif 'Stripperella' in i1Oo00 :
    pass
   elif 'Vixen' in i1Oo00 :
    pass
   else :
    iiiiiIIii ( '[COLORgreen]' + i1Oo00 + '[/COLOR]' , ooOOO00Ooo , 10006 , oOOoO0 + 'ORIGINCARTOON.png' , OOooO0OOoo , '' )
  xbmcplugin . addSortMethod ( o0 , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 86 - 86: Oo / OoOO + O0 * oO0o0ooO0
def iiI11I1i1i1iI ( ) :
 iiII1i1 = O0ii1ii1ii ( oOo0oooo00o ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2NhcnRvb24=' ) )
 OOO00O = re . compile ( '<td><a href="(.+?)">(.+)</a></td>' ) . findall ( iiII1i1 )
 for ooOOO00Ooo , i1Oo00 in OOO00O :
  if 'Dad!' in i1Oo00 :
   pass
  elif 'Family Guy' in i1Oo00 :
   pass
  elif '2 Stupid' in i1Oo00 :
   pass
  elif 'The Zelfs' in i1Oo00 :
   pass
  elif 'A Clone' in i1Oo00 :
   pass
  elif 'A.T.O.M' in i1Oo00 :
   pass
  elif 'Almost Naked' in i1Oo00 :
   pass
  elif 'Angry Kid' in i1Oo00 :
   pass
  elif 'Annoying Orange' in i1Oo00 :
   pass
  elif 'Aqua Teen' in i1Oo00 :
   pass
  elif 'Assy Mcgee' in i1Oo00 :
   pass
  elif 'Astroblast' in i1Oo00 :
   pass
  elif 'Atomic Betty' in i1Oo00 :
   pass
  elif 'Axe Cop' in i1Oo00 :
   pass
  elif 'Baby Playpen' in i1Oo00 :
   pass
  elif 'Beavis and Butt' in i1Oo00 :
   pass
  elif 'Celebrity Deathmatch' in i1Oo00 :
   pass
  elif 'Clerks The' in i1Oo00 :
   pass
  elif 'Crapston Villas' in i1Oo00 :
   pass
  elif 'Duckman:' in i1Oo00 :
   pass
  elif 'Stripperella' in i1Oo00 :
   pass
  elif 'Vixen' in i1Oo00 :
   pass
  else :
   iiiiiIIii ( '[COLORgreen]' + i1Oo00 + '[/COLOR]' , ooOOO00Ooo , 10006 , oOOoO0 + 'ORIGINCARTOON.png' , OOooO0OOoo , '' )
 xbmcplugin . addSortMethod ( o0 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 60 - 60: OoooooooOO % Oo + OoOO0ooOOoo0O . o0oO0 * iIii1I11I1II1
def oooo00 ( url ) :
 iiII1i1 = O0ii1ii1ii ( url )
 ii11I1 = re . compile ( '<img src="(.+?)" id="series_image" width="250" height="370" alt=".+?" />' ) . findall ( iiII1i1 )
 for oooooOoo0ooo in ii11I1 :
  O00OO0oO = oooooOoo0ooo
 iI1I1iIi11 = re . compile ( '<li><a href="(.+?)">Next</a></li>' ) . findall ( iiII1i1 )
 for url in iI1I1iIi11 :
  iiiiiIIii ( '[COLORgreen]NEXT PAGE[/COLOR]' , url , 10006 , O00OO0oO , OOooO0OOoo , '' )
 OOO00O = re . compile ( '&nbsp;<a href="(.+?)">(.+?)</a>' ) . findall ( iiII1i1 )
 for url , i1Oo00 in OOO00O :
  O00 ( '[COLORgreen]' + i1Oo00 + '[/COLOR]' , url , 10007 , O00OO0oO )
  if 87 - 87: I1IiI
  if 25 - 25: i1IIi . Ooo00oOo00o - I1IiI / Ooo00oOo00o % Ooo00oOo00o * iIii1I11I1II1
 xbmcplugin . addSortMethod ( o0 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 50 - 50: Ooo00oOo00o . i11iIiiIii - OoOO . OoOO
def I11I ( url , IMAGE ) :
 iiII1i1 = O0ii1ii1ii ( url )
 OOO00O = re . compile ( '"playlist">(.+?)</span></div><div><iframe src="(.+?)"' ) . findall ( iiII1i1 )
 for i1Oo00 , url in OOO00O :
  print i1Oo00 + '     ' + url
  if 'easy' in url :
   iIIII1i ( url )
   if 76 - 76: oO0o0ooO0 + o0oO0
   if 30 - 30: i11iIiiIii % iIii1I11I1II1 . o0000oOoOoO0o % iIii1I11I1II1
  xbmcplugin . addSortMethod ( o0 , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 62 - 62: Oo * I1IiI
def iIIII1i ( url ) :
 iiII1i1 = O0ii1ii1ii ( url )
 OOO00O = re . compile ( "url: '(.+?)'," ) . findall ( iiII1i1 )
 for url in OOO00O :
  OO0 ( url )
  if 84 - 84: I1IiI % o0oO0 - I1IiI . OOooOOo
  if 5 - 5: I1IiI * O0oO - ii11ii1ii / iIii1I11I1II1 % OoOO + IIII
  if 51 - 51: O0oO * OoOoOO00 % o0oO0
def oO0o000OoOoO0 ( ) :
 if 99 - 99: OOooOOo * OOOo0 % Oo . I1IiI
 iiiiiIIii ( '[COLORgreen]Stand Up[/COLOR]' , '' , 10014 , oOOoO0 + 'ORIGINSTANDUP.png' , OOooO0OOoo , '' )
 iiiiiIIii ( '[COLORgreen]Search Comedian[/COLOR]' , '' , 10015 , oOOoO0 + 'ORIGINSTANDUP.png' , OOooO0OOoo , '' )
 iiiiiIIii ( '[COLORgreen]Others[/COLOR]' , '' , 10017 , oOOoO0 + 'ORIGINSTANDUP.png' , OOooO0OOoo , '' )
 if 58 - 58: o0000oOoOoO0o + OoOoOO00 * oO0o0ooO0 * i11iIiiIii - iIii1I11I1II1
def oooo00o0o0o ( ) :
 oO0OOoo0OO = O0ii1ii1ii ( ( oOo0oooo00o ( 'aHR0cDovL2JhY2syYmFzaWNzYnVpbGQuY28udWsvdGVzdC9zdGFuZHVwbGlzdC5waHA=' ) ) )
 OOO00O = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( oO0OOoo0OO )
 for ooOOO00Ooo , oooooOoo0ooo , i1Oo00 in OOO00O :
  O00 ( '[COLORgreen]' + i1Oo00 + '[/COLOR]' , ooOOO00Ooo , 222 , oooooOoo0ooo )
  if 87 - 87: o0000oOoOoO0o * i1IIi - o00O0oo % OoOO0ooOOoo0O / O0oO
def IiIiiI11111I1 ( ) :
 O00OOOoOoo0O = Oo0o0000o0o0 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oo0OOo = O00OOOoOoo0O . lower ( )
 oO0OOoo0OO = O0ii1ii1ii ( ( oOo0oooo00o ( 'aHR0cDovL3d3dy5jb3VjaHRyaXBwZXIuY29tL2ZvcnVtMi9wYWdlLnBocD9wYWdlPTM=' ) ) )
 O0oo0ooOOOO = re . compile ( '<tr>.+?<td width=".+?" align=".+?">.+?<img border=".+?" src="..(.+?)" width=".+?" height=".+?"></td>.+?<td width=".+?" valign=".+?" align=".+?"><font size=".+?">(.+?)</font></td>.+?<td width=".+?">(.+?)</td>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for oooooOoo0ooo , Ii1ii , iIiiiI1IiI1I1 in O0oo0ooOOOO :
  for O00OOOoOoo0O in Ii1ii :
   print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< img >>>>>>>>>>>>>>>>>>>>>>>>>>'
   iIIIII1iiiiII = re . compile ( '<a href="(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( iIiiiI1IiI1I1 )
   for ooOOO00Ooo , i1Oo00 in iIIIII1iiiiII :
    if 'tube' in ooOOO00Ooo :
     pass
    elif 'stage' in ooOOO00Ooo :
     O00 ( '[COLORgreen]' + Ii1ii + '   -   ' + i1Oo00 + '[/COLOR]' , ( ooOOO00Ooo ) . replace ( '" target="_blank' , '' ) , 10016 , 'http://couchtripper.com/' + oooooOoo0ooo , )
    elif 'vee' in ooOOO00Ooo :
     pass
     if 54 - 54: i1IIi
def ii1I11 ( ) :
 oO0OOoo0OO = O0ii1ii1ii ( ( oOo0oooo00o ( 'aHR0cDovL3d3dy5jb3VjaHRyaXBwZXIuY29tL2ZvcnVtMi9wYWdlLnBocD9wYWdlPTM=' ) ) )
 O0oo0ooOOOO = re . compile ( '<tr>.+?<td width=".+?" align=".+?">.+?<img border=".+?" src="..(.+?)" width=".+?" height=".+?"></td>.+?<td width=".+?" valign=".+?" align=".+?"><font size=".+?">(.+?)</font></td>.+?<td width=".+?">(.+?)</td>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for oooooOoo0ooo , Ii1ii , iIiiiI1IiI1I1 in O0oo0ooOOOO :
  iIIIII1iiiiII = re . compile ( '<a href="(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( iIiiiI1IiI1I1 )
  for ooOOO00Ooo , i1Oo00 in iIIIII1iiiiII :
   if 'tube' in ooOOO00Ooo :
    pass
   elif 'stage' in ooOOO00Ooo :
    O00 ( '[COLORgreen]' + Ii1ii + '   -   ' + i1Oo00 + '[/COLOR]' , ( ooOOO00Ooo ) . replace ( '" target="_blank' , '' ) , 10016 , 'http://couchtripper.com/' + oooooOoo0ooo )
   elif 'vee' in ooOOO00Ooo :
    pass
    if 99 - 99: OoOO0ooOOoo0O
    if 45 - 45: OoOO - OoOO0ooOOoo0O * O0oO / Oo * OoOoOO00 - O0oO
 xbmcplugin . addSortMethod ( o0 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 83 - 83: Ooo00oOo00o % IIII . OoooooooOO
def O0Oo ( url ) :
 oO0OOoo0OO = O0ii1ii1ii ( url )
 print '>>>>>>>>>>>>>>>>>>>>>>>>' + url + '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'
 I1IiI111I11 = re . compile ( "url\[.+?\] = '(.+?)';" ) . findall ( oO0OOoo0OO )
 print '>>>>>>>>>>>>>>>>>>>>>>>' + ( str ( I1IiI111I11 ) ) + '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
 for url in I1IiI111I11 :
  OO0 ( ( url ) . replace ( '[' , '' ) . replace ( ']' , '' ) . replace ( '\'' , '' ) )
  if 16 - 16: O0 / o00O0oo . ii11ii1ii
  if 58 - 58: Oo / OoOO
  if 44 - 44: OoOO0ooOOoo0O
  if 54 - 54: o00O0oo - o0000oOoOoO0o - O0oO . iIii1I11I1II1
  if 79 - 79: o00O0oo . Ooo00oOo00o
  if 40 - 40: OOooOOo + Oo . OOooOOo % o0oO0
  if 15 - 15: o00O0oo * Oo % ii11ii1ii * iIii1I11I1II1 - i11iIiiIii
def Oo00OOOOoo0oo ( ) :
 if 80 - 80: O0oO * I1IiI * OoOoOO00 - O0 . I1IiI % OOOo0
 II1iiIIIiIii ( '[COLOR darkgoldenrod]Open Pandora\'s Box[/COLOR]' , '' , 10029 , 'https://encrypted-tbn1.gstatic.com/images?q=tbn%3AANd9GcTQ9r4TA8yIw9ggxuwsHxWojo6tPVfgTe8QIOxOQwzNR2TavtCi6Q' , OOooO0OOoo , '' )
 II1iiIIIiIii ( '[COLOR darkgoldenrod]Search[/COLOR]' , '' , 10026 , 'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png' , OOooO0OOoo , '' )
 if 23 - 23: oO0o0ooO0 + o0000oOoOoO0o . I1IiI * OOOo0 + ii11ii1ii
 Oooo0Ooo000 ( 'movies' , 'MAIN' )
 if 18 - 18: IIII * OOooOOo . IIII / O0
def iiIII1II ( ) :
 II1iiIIIiIii ( 'Search Pandoras Films' , '' , 10027 , oOOoO0 + 'PANDORASBOX.png' , OOooO0OOoo , '' )
 II1iiIIIiIii ( 'Search Pandoras TV' , '' , 10028 , oOOoO0 + 'PANDORASBOX.png' , OOooO0OOoo , '' )
 if 100 - 100: Oo % o00O0oo / o0000oOoOoO0o
 Oooo0Ooo000 ( 'movies' , 'MAIN' )
def iIII11Ii ( ) :
 if 52 - 52: O0oO / o0oO0 - o0000oOoOoO0o
 O00OOOoOoo0O = Oo0o0000o0o0 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oo0OOo = O00OOOoOoo0O . lower ( )
 iIiI = [ 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' ]
 if 5 - 5: Oo * I1IiI
 for ii1I11iIiIII1 in iIiI :
  oOO0OOOOoooO = Base_Pand + ii1I11iIiIII1 + O0o0Oo
  oO0OOoo0OO = O0ii1ii1ii ( oOO0OOOOoooO )
  OOO00O = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( oO0OOoo0OO )
  for ooOOO00Ooo , OOoOO0oo0ooO , O0o0O00Oo0o0 , O00O0oOO00O00 , i1Oo00 in OOO00O :
   if O00OOOoOoo0O in i1Oo00 . lower ( ) :
    i1ii11 ( i1Oo00 , ooOOO00Ooo , 222 , OOoOO0oo0ooO , O00O0oOO00O00 , O0o0O00Oo0o0 )
    if 49 - 49: OoooooooOO / i11iIiiIii * i11iIiiIii
    Oooo0Ooo000 ( 'movies' , 'MAIN' )
    xbmcplugin . addSortMethod ( o0 , xbmcplugin . SORT_METHOD_TITLE ) ;
    if 58 - 58: OoOO
    if 4 - 4: OoOoOO00 . o0oO0 / ii11ii1ii - i11iIiiIii
def OoO00 ( ) :
 if 18 - 18: o00O0oo - OoooooooOO % OoOoOO00 - OOOo0 % I1IiI
 O00OOOoOoo0O = Oo0o0000o0o0 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oo0OOo = O00OOOoOoo0O . lower ( )
 iIiI = [ 'a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' , 'p' , 'q' , 'r' , 's' , 't' , 'u' , 'v' , 'w' , 'x' , 'y' , 'z' ]
 if 60 - 60: iIii1I11I1II1 + i1IIi
 for ii1I11iIiIII1 in iIiI :
  OooOOo0 = Base_Pand + ii1I11iIiIII1 + O0o0Oo
  oO0OOoo0OO = O0ii1ii1ii ( OooOOo0 )
  OOO00O = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( oO0OOoo0OO )
  for i1Oo00 , O0o0O00Oo0o0 , ooOOO00Ooo , oooooOoo0ooo , O00O0oOO00O00 , ooO000O in OOO00O :
   if O00OOOoOoo0O in i1Oo00 . lower ( ) :
    II1iiIIIiIii ( i1Oo00 , ooOOO00Ooo , ooO000O , oooooOoo0ooo , O00O0oOO00O00 , O0o0O00Oo0o0 )
    if 53 - 53: OOooOOo . oO0o0ooO0 / o00O0oo
    Oooo0Ooo000 ( 'movies' , 'MAIN' )
    xbmcplugin . addSortMethod ( o0 , xbmcplugin . SORT_METHOD_TITLE ) ;
    if 39 - 39: o00O0oo % O0 % I1IiI . i1IIi
    if 86 - 86: Ooo00oOo00o * OoooooooOO
def OooO0oOo ( ) :
 if 66 - 66: Ooo00oOo00o * Oo
 iiII1i1 = O0ii1ii1ii ( oOo0oooo00o ( 'aHR0cDovL3NlZWR1cmdyZWVkLngxMGhvc3QuY29tL29yaWdpbi9zcG9uZ2VtYWluLnBocA==' ) )
 OOO00O = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( iiII1i1 )
 for i1Oo00 , O0o0O00Oo0o0 , ooOOO00Ooo , oooooOoo0ooo , O00O0oOO00O00 , ooO000O in OOO00O :
  II1iiIIIiIii ( i1Oo00 , ooOOO00Ooo , ooO000O , oooooOoo0ooo , O00O0oOO00O00 , O0o0O00Oo0o0 )
  Oooo0Ooo000 ( 'movies' , 'MAIN' )
def II1IIIiiI11 ( url ) :
 if 86 - 86: Ooo00oOo00o % OoooooooOO % Ooo00oOo00o / OOOo0
 xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
 Oo0ooo0Ooo = ( '%s%s' % ( i1II1I , url ) )
 iI1i111I1Ii = O0ii1ii1ii ( url )
 OOO00O = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( iI1i111I1Ii )
 for url , OOoOO0oo0ooO , O0o0O00Oo0o0 , OOoO0ooOO , i1Oo00 in OOO00O :
  i1ii11 ( i1Oo00 , url , 222 , OOoOO0oo0ooO , OOoO0ooOO , O0o0O00Oo0o0 )
  if 24 - 24: i1IIi . i11iIiiIii
  Oooo0Ooo000 ( 'movies' , 'MAIN' )
  if 16 - 16: Oo % ii11ii1ii + o0000oOoOoO0o - O0 . oO0o0ooO0 / O0oO
  xbmcplugin . addSortMethod ( o0 , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 35 - 35: OoOO / O0oO / OoOoOO00 - iIii1I11I1II1 + OoOoOO00 . O0oO
  if 81 - 81: oO0o0ooO0 * OoOO0ooOOoo0O - ii11ii1ii * o00O0oo % I1IiI * I1IiI
def ooO ( url ) :
 if 100 - 100: OOOo0 / OOooOOo * oO0o0ooO0 . O0 / OoOO0ooOOoo0O
 iiII1i1 = O0ii1ii1ii ( url )
 OOO00O = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( iiII1i1 )
 for i1Oo00 , O0o0O00Oo0o0 , url , oooooOoo0ooo , O00O0oOO00O00 , ooO000O in OOO00O :
  II1iiIIIiIii ( i1Oo00 , url , ooO000O , oooooOoo0ooo , O00O0oOO00O00 , O0o0O00Oo0o0 )
  if 83 - 83: O0oO
  Oooo0Ooo000 ( 'movies' , 'MAIN' )
  if 48 - 48: OoOoOO00 * OoOO0ooOOoo0O * O0oO
  if 50 - 50: IIII % i1IIi
 xbmcplugin . addSortMethod ( o0 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 21 - 21: OoooooooOO - iIii1I11I1II1
def i1ii11 ( name , url , mode , iconimage , fanart , description ) :
 if 93 - 93: OoOO - OOooOOo % I1IiI . I1IiI - o0oO0
 O00ooOo = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 oOO0o00O = True
 oOoO = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 oOoO . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 oOoO . setProperty ( "Fanart_Image" , fanart )
 oOO0o00O = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = O00ooOo , listitem = oOoO , isFolder = False )
 return oOO0o00O
 if 26 - 26: I1IiI / Oo - i1IIi + o0000oOoOoO0o
def II1iiIIIiIii ( name , url , mode , iconimage , fanart , description ) :
 if 38 - 38: OoooooooOO / ii11ii1ii . O0 / i1IIi / Oo + iIii1I11I1II1
 O00ooOo = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 oOO0o00O = True
 oOoO = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 oOoO . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 oOoO . setProperty ( "Fanart_Image" , fanart )
 oOO0o00O = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = O00ooOo , listitem = oOoO , isFolder = True )
 return oOO0o00O
if 96 - 96: oO0o0ooO0
if 18 - 18: oO0o0ooO0 * o0000oOoOoO0o - o00O0oo
if 31 - 31: Oo - O0 % I1IiI % OoOO
if 45 - 45: ii11ii1ii + OoOoOO00 * i11iIiiIii
if 13 - 13: OoooooooOO * OoOO - o00O0oo / OoOO0ooOOoo0O + o0000oOoOoO0o + IIII
if 39 - 39: iIii1I11I1II1 - OoooooooOO
if 81 - 81: ii11ii1ii - O0 * OoooooooOO
if 23 - 23: OoOoOO00 / OoOO
if 28 - 28: Oo * o0oO0 - Ooo00oOo00o
if 19 - 19: o0000oOoOoO0o
if 67 - 67: O0 % iIii1I11I1II1 / IIII . i11iIiiIii - o00O0oo + O0
if 27 - 27: OoOO0ooOOoo0O
if 89 - 89: OoOoOO00 / OoOO
if 14 - 14: OoOO0ooOOoo0O . OOOo0 * o0oO0 + OoOoOO00 - o0oO0 + OoOO0ooOOoo0O
if 18 - 18: OoOO - OOooOOo - OOOo0 - OOOo0
def OOooo00 ( string ) :
 if OOOO == 'true' :
  xbmc . log ( "[addon.live.GenieTV-%s]: %s" % ( addon_version , string ) )
  if 35 - 35: O0oO . I1IiI * i11iIiiIii
def iiII ( name , url , iconimage , fanart , mode , playlist = None , regexs = None ) :
 o0Oii1111i = [ ]
 try :
  if 75 - 75: IIII + OoOoOO00 / OoOO - OoOO / OoooooooOO
  name = name . encode ( 'utf-8' , 'ignore' )
 except :
  pass
 if os . path . exists ( IIIII ) == False :
  OOooo00 ( 'Making Favorites File' )
  o0Oii1111i . append ( ( name , url , iconimage , fanart , mode , playlist , regexs ) )
  ooO0oOOooOo0 = open ( IIIII , "w" )
  ooO0oOOooOo0 . write ( json . dumps ( o0Oii1111i ) )
  ooO0oOOooOo0 . close ( )
 else :
  OOooo00 ( 'Appending Favorites' )
  ooO0oOOooOo0 = open ( IIIII ) . read ( )
  iiii11ii = json . loads ( ooO0oOOooOo0 )
  iiii11ii . append ( ( name , url , iconimage , fanart , mode ) )
  O0ooooo0OOOO0 = open ( IIIII , "w" )
  O0ooooo0OOOO0 . write ( json . dumps ( iiii11ii ) )
  O0ooooo0OOOO0 . close ( )
  if 50 - 50: o00O0oo / I1IiI * o00O0oo
  if 34 - 34: O0 * O0 % OoooooooOO + oO0o0ooO0 * iIii1I11I1II1 % o00O0oo
def I1iI1I1 ( ) :
 IiIi1 = json . loads ( open ( IIIII ) . read ( ) )
 oo00ooOoo = len ( IiIi1 )
 for iii1IIIiiiI in IiIi1 :
  i1Oo00 = iii1IIIiiiI [ 0 ]
  ooOOO00Ooo = iii1IIIiiiI [ 1 ]
  OOoOO0oo0ooO = iii1IIIiiiI [ 2 ]
  try :
   OoO00oo00 = iii1IIIiiiI [ 3 ]
   if OoO00oo00 == None :
    raise
  except :
   if o0oOoO00o . getSetting ( 'use_thumb' ) == "true" :
    OoO00oo00 = OOoOO0oo0ooO
   else :
    OoO00oo00 = O00O0oOO00O00
  try : Oo0Oo0O = iii1IIIiiiI [ 5 ]
  except : Oo0Oo0O = None
  try : iiiI1i11Ii = iii1IIIiiiI [ 6 ]
  except : iiiI1i11Ii = None
  if 16 - 16: Oo / i11iIiiIii
  if iii1IIIiiiI [ 4 ] == 0 :
   iiiiiIIii ( i1Oo00 , ooOOO00Ooo , '' , OOoOO0oo0ooO , O00O0oOO00O00 , '' , 'fav' )
  else :
   iiiiiIIii ( i1Oo00 , ooOOO00Ooo , iii1IIIiiiI [ 4 ] , OOoOO0oo0ooO , O00O0oOO00O00 , '' , 'fav' )
   if 64 - 64: i11iIiiIii / o00O0oo * i1IIi
def OOOOOOoO ( name ) :
 iiii11ii = json . loads ( open ( IIIII ) . read ( ) )
 for I1 in range ( len ( iiii11ii ) ) :
  if iiii11ii [ I1 ] [ 0 ] == name :
   del iiii11ii [ I1 ]
   O0ooooo0OOOO0 = open ( IIIII , "w" )
   O0ooooo0OOOO0 . write ( json . dumps ( iiii11ii ) )
   O0ooooo0OOOO0 . close ( )
   break
 xbmc . executebuiltin ( "XBMC.Container.Refresh" )
 if 13 - 13: I1IiI / ii11ii1ii . OoOO0ooOOoo0O * o0000oOoOoO0o - Oo / OoOO
 if 8 - 8: I1IiI / O0 * O0 % O0oO - Oo + o0000oOoOoO0o
 if 83 - 83: O0 . OOOo0
def O0OIIi1 ( ) :
 if 42 - 42: OoOO
 iiiiiIIii ( '[COLORgreen]Recent Episodes[/COLOR]' , '' , 10019 , oOOoO0 + 'dtv.png' , OOooO0OOoo , '' )
 iiiiiIIii ( '[COLORgreen]Genres[/COLOR]' , '' , 10020 , oOOoO0 + 'dtv.png' , OOooO0OOoo , '' )
 iiiiiIIii ( '[COLORgreen]Search[/COLOR]' , '' , 10021 , oOOoO0 + 'dtv.png' , OOooO0OOoo , '' )
 if 36 - 36: IIII - OoooooooOO / Ooo00oOo00o
def iIIi1iI1I1IIi ( ) :
 if 77 - 77: o0oO0 / Oo + o0oO0 % OOooOOo - OOOo0 * OOOo0
 iiII1i1 = cloudflare . source ( oOo0oooo00o ( 'aHR0cDovL2RpemlsYWIuY29t' ) )
 OOO00O = re . compile ( '<li id=".+?">.+?<a href="(.+?)">.+?<img width="40" height="40" src="(.+?)" alt=""/>.+?<span class="title">\n(.+?)</span>.+?<span class="alt-title">\n(.+?)</span>.+?</a>.+?</li>' , re . DOTALL ) . findall ( iiII1i1 )
 for ooOOO00Ooo , oooooOoo0ooo , i1Oo00 , I1oO0ooOoO in OOO00O :
  iiiiiIIii ( i1Oo00 + '  -  ' + ( I1oO0ooOoO ) . replace ( 'sezon' , 'Season' ) . replace ( 'bölüm' , 'Episode' ) , ooOOO00Ooo , 10023 , oOOoO0 + 'dtv.png' , OOooO0OOoo , '' )
  if 59 - 59: O0 % Oo
  if 92 - 92: o00O0oo % oO0o0ooO0 / ii11ii1ii % ii11ii1ii * OOOo0
  if 74 - 74: O0 . OOOo0 % Ooo00oOo00o % IIII
def oOo0OooOo ( ) :
 if 51 - 51: o0000oOoOoO0o . Oo
 iiiiiIIii ( '[COLORgreen]Action[/COLOR]' , 'Aksiyon' , 10024 , oOOoO0 + 'dtv.png' , OOooO0OOoo , '' )
 iiiiiIIii ( '[COLORgreen]Adventure[/COLOR]' , 'Macera' , 10024 , oOOoO0 + 'dtv.png' , OOooO0OOoo , '' )
 iiiiiIIii ( '[COLORgreen]Animation[/COLOR]' , 'Animasyon' , 10024 , oOOoO0 + 'dtv.png' , OOooO0OOoo , '' )
 iiiiiIIii ( '[COLORgreen]Anime[/COLOR]' , 'Anime' , 10024 , oOOoO0 + 'dtv.png' , OOooO0OOoo , '' )
 iiiiiIIii ( '[COLORgreen]Biography[/COLOR]' , 'Biyografi' , 10024 , oOOoO0 + 'dtv.png' , OOooO0OOoo , '' )
 iiiiiIIii ( '[COLORgreen]Comedy[/COLOR]' , 'Komedi' , 10024 , oOOoO0 + 'dtv.png' , OOooO0OOoo , '' )
 iiiiiIIii ( '[COLORgreen]Crime[/COLOR]' , 'Su%C3%A7' , 10024 , oOOoO0 + 'dtv.png' , OOooO0OOoo , '' )
 iiiiiIIii ( '[COLORgreen]Documentary[/COLOR]' , 'Belgesel' , 10024 , oOOoO0 + 'dtv.png' , OOooO0OOoo , '' )
 iiiiiIIii ( '[COLORgreen]Drama[/COLOR]' , 'Dram' , 10024 , oOOoO0 + 'dtv.png' , OOooO0OOoo , '' )
 iiiiiIIii ( '[COLORgreen]Family[/COLOR]' , 'Aile' , 10024 , oOOoO0 + 'dtv.png' , OOooO0OOoo , '' )
 iiiiiIIii ( '[COLORgreen]Fantasy[/COLOR]' , 'Fantastik' , 10024 , oOOoO0 + 'dtv.png' , OOooO0OOoo , '' )
 iiiiiIIii ( '[COLORgreen]History[/COLOR]' , 'Tarih' , 10024 , oOOoO0 + 'dtv.png' , OOooO0OOoo , '' )
 iiiiiIIii ( '[COLORgreen]Horror[/COLOR]' , 'Korku' , 10024 , oOOoO0 + 'dtv.png' , OOooO0OOoo , '' )
 iiiiiIIii ( '[COLORgreen]Mini-Series[/COLOR]' , 'Mini%20Dizi' , 10024 , oOOoO0 + 'dtv.png' , OOooO0OOoo , '' )
 iiiiiIIii ( '[COLORgreen]Musical[/COLOR]' , 'M%C3%BCzikal' , 10024 , oOOoO0 + 'dtv.png' , OOooO0OOoo , '' )
 iiiiiIIii ( '[COLORgreen]Mystery[/COLOR]' , 'Gizem' , 10024 , oOOoO0 + 'dtv.png' , OOooO0OOoo , '' )
 iiiiiIIii ( '[COLORgreen]Romance[/COLOR]' , 'Romantik' , 10024 , oOOoO0 + 'dtv.png' , OOooO0OOoo , '' )
 iiiiiIIii ( '[COLORgreen]Science Fiction[/COLOR]' , 'Bilim%20Kurgu' , 10024 , oOOoO0 + 'dtv.png' , OOooO0OOoo , '' )
 iiiiiIIii ( '[COLORgreen]Sport[/COLOR]' , 'Spor' , 10024 , oOOoO0 + 'dtv.png' , OOooO0OOoo , '' )
 iiiiiIIii ( '[COLORgreen]Thriller[/COLOR]' , 'Gerilim' , 10024 , oOOoO0 + 'dtv.png' , OOooO0OOoo , '' )
 iiiiiIIii ( '[COLORgreen]War[/COLOR]' , 'Sava%C5%9F' , 10024 , oOOoO0 + 'dtv.png' , OOooO0OOoo , '' )
 iiiiiIIii ( '[COLORgreen]Western[/COLOR]' , 'Tarih' , 10024 , oOOoO0 + 'dtv.png' , OOooO0OOoo , '' )
 iiiiiIIii ( '[COLORgreen]Youth[/COLOR]' , 'Gen%C3%A7lik' , 10024 , oOOoO0 + 'dtv.png' , OOooO0OOoo , '' )
 if 45 - 45: i1IIi - Oo / O0 . ii11ii1ii
def iI1 ( url ) :
 iIIiI1ii = 'http://dizilab.com/arsiv?limit=100&tur=' + url + '&orderby=&ulke=&order=&yil=&dizi_adi='
 oO0OOoo0OO = cloudflare . source ( iIIiI1ii )
 OOO00O = re . compile ( '<div class="tv-series-single">.+?<a href="(.+?)" class="film-image">.+?<img src="(.+?)" alt=""/>.+?<span class="position">.+?</span>\n(.+?)</a>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for url , oooooOoo0ooo , i1Oo00 in OOO00O :
  iiiiiIIii ( '[COLORgreen]' + i1Oo00 + '[/COLOR]' , url , 10022 , oOOoO0 + 'dtv.png' , OOooO0OOoo , '' )
  if 78 - 78: O0 * OoOO0ooOOoo0O
  if 43 - 43: ii11ii1ii / OOOo0 . o0oO0
  if 62 - 62: iIii1I11I1II1 + oO0o0ooO0 . Oo / IIII % O0 . O0oO
  if 93 - 93: i11iIiiIii % iIii1I11I1II1 % i11iIiiIii + OOooOOo / OOooOOo / OoOoOO00
def I1i ( ) :
 if 59 - 59: OoooooooOO . o00O0oo / O0 - OoOO0ooOOoo0O
 O00OOOoOoo0O = Oo0o0000o0o0 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oo0OOo = O00OOOoOoo0O . lower ( )
 ooOOO00Ooo = ( oOo0oooo00o ( 'aHR0cDovL2RpemlsYWIuY29tL2Fyc2l2P2xpbWl0PSZ0dXI9Jm9yZGVyYnk9JnVsa2U9Jm9yZGVyPSZ5aWw9JmRpemlfYWRpPQ==' ) ) + ( O00OOOoOoo0O ) . replace ( ' ' , '+' )
 oO0OOoo0OO = cloudflare . source ( ooOOO00Ooo )
 OOO00O = re . compile ( '<a href="(.+?)" class="film-image">\n<img src="(.+?)" alt=""/>\n</a>\n<div class="tss-detail">\n<a class="title" style="" href=".+?">\n<span class="position">.+?</span>\n(.+?)</a>' ) . findall ( oO0OOoo0OO )
 for ooOOO00Ooo , oooooOoo0ooo , i1Oo00 in OOO00O :
  if O00OOOoOoo0O in i1Oo00 . lower ( ) :
   iiiiiIIii ( '[COLORgreen]' + i1Oo00 + '[/COLOR]' , ooOOO00Ooo , 10022 , oOOoO0 + 'dtv.png' )
   if 1 - 1: IIII / IIII - i11iIiiIii
   if 87 - 87: Oo / O0 * IIII / OOooOOo
   if 19 - 19: O0oO + i1IIi . OOOo0 - Oo
def iIi1I1 ( url ) :
 oO0OOoo0OO = cloudflare . source ( url )
 OOO00O = re . compile ( '<a class="season" href="(.+?)">\n(.+?)\n</a>.+?<a class="episode" href=".+?">\n(.+?)\n</a>.+?<a class="episode-name" href=".+?">\n(.+?)</a>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for I111iIi1 , O0oOoo0OoO0O , oo00IiI1 , i1Oo00 in OOO00O :
  oOo00o00oO = ( oo00IiI1 ) . replace ( 'Sezon' , '' ) . replace ( 'bölüm' , '' ) . replace ( 'Bölüm' , '' ) . replace ( 'BÃ¶lÃ¼m' , '' ) . replace ( '.' , '' )
  o0000 = ( O0oOoo0OoO0O ) . replace ( 'bölüm' , '' ) . replace ( 'Sezon' , '' ) . replace ( 'Bölüm' , '' ) . replace ( 'BÃ¶lÃ¼m' , '' ) . replace ( '.' , '' )
  i111i1i = 'Season ' + o0000 + 'Episode ' + oOo00o00oO + i1Oo00
  IiIii1I1I ( i111i1i , I111iIi1 )
  if 51 - 51: Oo % I1IiI * OoooooooOO . i11iIiiIii
  xbmcplugin . addSortMethod ( o0 , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 77 - 77: OoOoOO00
  if 42 - 42: o00O0oo * O0oO . IIII * OOOo0 + I1IiI
def IiIii1I1I ( name , url ) :
 I111iIi1 = url
 i1i1II11II1 = name
 II1IIIii = cloudflare . source ( I111iIi1 )
 ii11I1 = re . compile ( 'file: "(.+?)",.+?label: "(.+?)",' , re . DOTALL ) . findall ( II1IIIii )
 for I1IiI111I11 , iIIIiIi1I1i in ii11I1 :
  O00 ( '[COLORgreen]' + i1i1II11II1 + iIIIiIi1I1i + '[/COLOR]' , I1IiI111I11 , 10012 , oOOoO0 + 'dtv.png' )
  if 78 - 78: iIii1I11I1II1 % I1IiI + ii11ii1ii / i1IIi % OoOoOO00 + OoOO0ooOOoo0O
 xbmcplugin . addSortMethod ( o0 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 91 - 91: iIii1I11I1II1 % Ooo00oOo00o . OOooOOo + o00O0oo + OOooOOo
 if 95 - 95: o00O0oo + ii11ii1ii * OoOO0ooOOoo0O
def I1Ii ( ) :
 if 77 - 77: iIii1I11I1II1 - i1IIi . OoOO
 if 26 - 26: OOooOOo * IIII . i1IIi
 if 59 - 59: O0 + i1IIi - OOooOOo
 if 62 - 62: i11iIiiIii % OoOO0ooOOoo0O . IIII . OoOO0ooOOoo0O
 if 84 - 84: i11iIiiIii * Ooo00oOo00o
 if 18 - 18: OoOO0ooOOoo0O - o00O0oo - I1IiI / O0oO - O0
 if 30 - 30: O0 + ii11ii1ii + OoOoOO00
 if 14 - 14: OOooOOo / OoOO0ooOOoo0O - iIii1I11I1II1 - OoOO % o0oO0
 if 49 - 49: o0oO0 * OoOO / OOooOOo / Oo * iIii1I11I1II1
 if 57 - 57: I1IiI - OoOO / o0oO0 % i11iIiiIii
 if 3 - 3: oO0o0ooO0 . o0oO0 % OOOo0 + ii11ii1ii
 if 64 - 64: i1IIi
 if 29 - 29: OOooOOo / i11iIiiIii / OOOo0 % OoOO % i11iIiiIii
 if 18 - 18: OoOO0ooOOoo0O + O0oO
 if 80 - 80: OoOO + OOooOOo * o00O0oo + Ooo00oOo00o
 iiiiiIIii ( '[COLORgreen]Newest Episodes Added[/COLOR]' , 'http://www.watchseries.li/latest' , 10046 , oOOoO0 + 'WATCHSERIES.png' , '' , '' )
 iiiiiIIii ( '[COLORgreen]This Week\'s Popular Episodes[/COLOR]' , 'http://www.watchseries.li/new' , 10042 , oOOoO0 + 'WATCHSERIES.png' , '' , '' )
 iiiiiIIii ( '[COLORgreen]Search Program[/COLOR]' , '' , 10043 , oOOoO0 + 'WATCHSERIES.png' , '' , '' )
 if 75 - 75: o0000oOoOoO0o / OOooOOo / OoOO0ooOOoo0O / IIII % o0oO0 + OoOoOO00
 if 4 - 4: oO0o0ooO0 - Oo - IIII - o0000oOoOoO0o % i11iIiiIii / Ooo00oOo00o
def i1iii11 ( url ) :
 oO0OOoo0OO = O0ii1ii1ii ( url )
 iIiIIIi = re . compile ( '<ul class="pagination" style="line-height: 3;">(.+?)</ul>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 OOO00O = re . compile ( '<li><a href="/letters/(.+?)">(.+?)</a></li>' ) . findall ( str ( iIiIIIi ) )
 for url , i1Oo00 in OOO00O :
  iiiiiIIii ( '[COLORgreen]' + i1Oo00 + '[/COLOR]' , 'http://watchseries.li/letters/' + url , 10049 , oOOoO0 + 'WATCHSERIES.png' , '' , '' )
  if 92 - 92: I1IiI . OoooooooOO - O0oO
def Oo0000o0O0O ( url ) :
 oO0OOoo0OO = O0ii1ii1ii ( url )
 OOO00O = re . compile ( '<a href="(.+?)" class="sr-header">(.+?)</a>' ) . findall ( oO0OOoo0OO )
 for url , i1Oo00 in OOO00O :
  iiiiiIIii ( '[COLORgreen]' + i1Oo00 + '[/COLOR]' , 'http://watchseries.li/' + url , 10049 , oOOoO0 + 'WATCHSERIES.png' , '' , '' )
  if 1 - 1: ii11ii1ii % I1IiI . OOooOOo . OOOo0 - OOOo0 - IIII
def iiIii ( url ) :
 oO0OOoo0OO = O0ii1ii1ii ( url )
 OOO00O = re . compile ( '<li class="col-md-6 col-xs-12 list-movies-li"><a href="(.+?)" title=".+?">(.+?)<span class="epnum">.+?</span></a></li>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 ii11I1 = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="(.+?)">Next</a></li></ul>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for url , i1Oo00 in OOO00O :
  iiiiiIIii ( '[COLORgreen]' + ( i1Oo00 ) . replace ( '&nbsp;' , ' ' ) . replace ( '&amp;' , '&' ) . replace ( '&#039;' , '\'' ) + '[/COLOR]' , 'http://www.watchseries.li' + url , 10044 , oOOoO0 + 'WATCHSERIES.png' , '' , '' )
 for url in ii11I1 :
  iiiiiIIii ( '[COLORgreen]' + 'NEXT' + '[/COLOR]' , 'http://www.watchseries.li' + url , 10049 , '' , '' , '' )
  if 28 - 28: OoOO
  if 52 - 52: OOOo0 + iIii1I11I1II1
def ooOO ( ) :
 O00OOOoOoo0O = Oo0o0000o0o0 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 i1iiIiI = 'http://www.watchseries.li/search/' + O00OOOoOoo0O . replace ( ' ' , '%20' )
 oO0OOoo0OO = O0ii1ii1ii ( i1iiIiI )
 OOO00O = re . compile ( '<img src="(.+?)".+?<a href="(.+?)" title=".+?"><b>(.+?)</b>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for oooooOoo0ooo , ooOOO00Ooo , i1Oo00 in OOO00O :
  if 'watch online' in i1Oo00 :
   pass
  else :
   print ooOOO00Ooo
   iiiiiIIii ( '[COLORgreen]' + i1Oo00 + '[/COLOR]' , 'http://www.watchseries.li' + ooOOO00Ooo , 10044 , oooooOoo0ooo , '' , '' )
   if 60 - 60: OoOO % oO0o0ooO0 / OoOO0ooOOoo0O % o0oO0 - I1IiI % iIii1I11I1II1
   xbmcplugin . setContent ( o0 , 'movies' )
   if 82 - 82: I1IiI + o0000oOoOoO0o % i1IIi + IIII / O0oO - Oo
def O0OoOOOo0Oo ( url ) :
 oO0OOoo0OO = O0ii1ii1ii ( url )
 OOO00O = re . compile ( '<img src="(.+?)".+?<div class="block-left-home-inside-text">.+?<a href="(.+?)" title=".+?"><b>(.+?)</b> <br>.+?<span class=".+?">(.+?)</span></a><br>(.+?)<br>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for oooooOoo0ooo , url , i1Oo00 , oo00IiI1 , O0o0O00Oo0o0 in OOO00O :
  IiI1IIIII1I = ( i1Oo00 ) . replace ( '&nbsp;' , ' ' ) . replace ( '&amp;' , '&' ) . replace ( '&#039;' , '\'' ) + ' - ' + ( oo00IiI1 ) . replace ( '&amp;' , '&' ) . replace ( '&#039;' , '\'' )
  iiiiiIIii ( '[COLORgreen]' + IiI1IIIII1I + '[/COLOR]' , 'http://www.watchseries.li' + url , 10045 , oooooOoo0ooo , '' , O0o0O00Oo0o0 )
  if 35 - 35: o00O0oo - o00O0oo + i1IIi - O0 - O0oO
def oOO0o0oo0 ( url ) :
 oO0OOoo0OO = O0ii1ii1ii ( url )
 OOO00O = re . compile ( '<li class="col-md-6 col-xs-12 list-movies-li"><a href="(.+?)" title=".+?">(.+?)<span class="epnum">.+?</span></a></li>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 ii11I1 = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="(.+?)">Next</a></li></ul>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for url , i1Oo00 in OOO00O :
  IiI1IIIII1I = ( i1Oo00 ) . replace ( '&nbsp;' , ' ' ) . replace ( '&amp;' , '&' ) . replace ( '&#039;' , '\'' )
  iiiiiIIii ( '[COLORgreen]' + IiI1IIIII1I + '[/COLOR]' , 'http://www.watchseries.li' + url , 10045 , oOOoO0 + 'WATCHSERIES.png' , '' , '' )
 for url in ii11I1 :
  iiiiiIIii ( '[COLORgreen]' + 'NEXT' + '[/COLOR]' , 'http://www.watchseries.li' + url , 10046 , '' , '' , '' )
  if 78 - 78: OoOO0ooOOoo0O + oO0o0ooO0 . IIII
def OoIIi1iI ( url ) :
 oO0OOoo0OO = O0ii1ii1ii ( url )
 OOO00O = re . compile ( '<div class="mask">.+?<a href="(.+?)" title="(.+?)">.+?<img src="(.+?)"' , re . DOTALL ) . findall ( oO0OOoo0OO )
 ii11I1 = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="(.+?)">Next</a></li></ul>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for url , i1Oo00 , oooooOoo0ooo in OOO00O :
  iiiiiIIii ( '[COLORgreen]' + ( i1Oo00 ) . replace ( '&nbsp;' , ' ' ) . replace ( '&amp;' , '&' ) . replace ( '&#039;' , '\'' ) + '[/COLOR]' , 'http://www.watchseries.li' + url , 10044 , oooooOoo0ooo , '' , '' )
 for url in ii11I1 :
  iiiiiIIii ( '[COLORgreen]' + 'NEXT' + '[/COLOR]' , 'http://www.watchseries.li' + url , 10041 , '' , '' , '' )
  if 92 - 92: Ooo00oOo00o * o0oO0
def i1iIIi1o0o0OoOOOOOo ( url ) :
 oO0OOoo0OO = O0ii1ii1ii ( url )
 iIiIIIi = re . compile ( '<div class="col-md-6 col-xs-12".+?<a href=".+?" itemprop="url"><span itemprop="name">(.+?)</span>(.+?)</ul>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for O0oOoo0OoO0O , O0oo0ooOOOO in iIiIIIi :
  OOO00O = re . compile ( '<li itemprop="episode".+?<meta itemprop="url" content="(.+?)">.+?<span class="" itemprop="name">\n(.+?)\n' , re . DOTALL ) . findall ( str ( O0oo0ooOOOO ) )
  for url , i1Oo00 in OOO00O :
   IiI1IIIII1I = ( O0oOoo0OoO0O ) . replace ( '  ' , '' ) + ' ' + ( i1Oo00 ) . replace ( '&nbsp;' , ' ' ) . replace ( '&#039;' , '\'' ) . replace ( '  ' , '' )
   iiiiiIIii ( '[COLORgreen]' + IiI1IIIII1I + '[/COLOR]' , 'http://www.watchseries.li' + url , 10045 , oOOoO0 + 'WATCHSERIES.png' , '' , '' )
 ii11I1 = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="(.+?)">Next</a></li></ul>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for url in ii11I1 :
  iiiiiIIii ( '[COLORgreen]' + 'NEXT' + '[/COLOR]' , 'http://www.watchseries.li' + url , 10044 , '' , '' , '' )
  if 39 - 39: OoooooooOO * OoOO0ooOOoo0O * O0 . o0000oOoOoO0o . Ooo00oOo00o + o0oO0
  if 9 - 9: I1IiI + OoOO % OoooooooOO + OOooOOo
class ooOO0o ( ) :
 if 51 - 51: Oo - ii11ii1ii * o0000oOoOoO0o
 List = [ ]
 source_list = [ ]
 def __init__ ( self , name ) :
  if 12 - 12: iIii1I11I1II1 % o0oO0 % o0oO0
  IiI1IIIII1I = name
  self . Get_Sources ( ooOOO00Ooo , IiI1IIIII1I )
  if 78 - 78: IIII . I1IiI . o0000oOoOoO0o
  if 97 - 97: OoOO
 def Get_Sources ( self , URL , season_name ) :
  i1111 = xbmcgui . DialogProgress ( )
  oO0OOoo0OO = O0ii1ii1ii ( URL )
  OOO00O = re . compile ( '<td>.+?<a href="/link/(.+?)".+?height="16px">(.+?)\n' , re . DOTALL ) . findall ( oO0OOoo0OO )
  for ooOOO00Ooo , i1Oo00 in OOO00O :
   URL = 'http://www.watchseries.li/link/' + ooOOO00Ooo
   self . Get_site_link ( URL , season_name )
   if 80 - 80: OOOo0 . o00O0oo
 def Get_site_link ( self , url , season_name ) :
  oO0OOoo0OO = O0ii1ii1ii ( url )
  OOO00O = re . compile ( '<iframe style=.+?" src="(.+?)"' ) . findall ( oO0OOoo0OO )
  ii11I1 = re . compile ( '<IFRAME SRC="(.+?)"' ) . findall ( oO0OOoo0OO )
  iI1I1iIi11 = re . compile ( '<IFRAME style=".+?" SRC="(.+?)"' ) . findall ( oO0OOoo0OO )
  for url in OOO00O :
   self . main ( url , season_name )
  for url in ii11I1 :
   self . main ( url , season_name )
  for url in iI1I1iIi11 :
   self . main ( url , season_name )
   if 47 - 47: o0000oOoOoO0o + o0oO0 + OoOoOO00 % i11iIiiIii
 def main ( self , url , season_name ) :
  i1111 . create ( "[COLORwhite]Origin[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
  if 'daclips.in' in url :
   OOoOoo00Oo = 'DACLIPS'
   if OOoOoo00Oo in ooOO0o . source_list :
    pass
   else :
    self . daclips ( url , season_name , OOoOoo00Oo )
    i1111 . update ( 0 , "" , "Getting Daclips Links" )
  else :
   if 'filehoot.com' in url :
    OOoOoo00Oo = 'FILEHOOT'
    if OOoOoo00Oo in ooOO0o . source_list :
     pass
    else :
     i1111 . update ( 0 , "" , "Getting Filehoot Links" )
     self . filehoot ( url , season_name , OOoOoo00Oo )
   else :
    if 'thevideo.me' in url :
     OOoOoo00Oo = 'THEVIDEO'
     if OOoOoo00Oo in ooOO0o . source_list :
      pass
     else :
      self . thevideo ( url , season_name , OOoOoo00Oo )
      i1111 . update ( 0 , "" , "Getting Thevideo Links" )
    else :
     if 'allmyvideos.net' in url :
      OOoOoo00Oo = 'ALLMYVIDEOS'
      if OOoOoo00Oo in ooOO0o . source_list :
       pass
      else :
       self . allmyvid ( url , season_name , OOoOoo00Oo )
       i1111 . update ( 0 , "" , "Getting Allmyvideo Links" )
     else :
      if 'vidspot.net' in url :
       OOoOoo00Oo = 'VIDSPOT'
       if OOoOoo00Oo in ooOO0o . source_list :
        pass
       else :
        self . vidspot ( url , season_name , OOoOoo00Oo )
        i1111 . update ( 0 , "" , "Getting Vidspot Links" )
      else :
       if 'vodlocker' in url :
        OOoOoo00Oo = 'VODLOCKER'
        if OOoOoo00Oo in ooOO0o . source_list :
         pass
        else :
         self . vodlocker ( url , season_name , OOoOoo00Oo )
         i1111 . update ( 0 , "" , "Getting Vodlocker Links" )
         if 9 - 9: OoOoOO00 * OoOoOO00 . i11iIiiIii * iIii1I11I1II1
         if 18 - 18: Ooo00oOo00o . OoOoOO00 % I1IiI % o00O0oo
 def allmyvid ( self , url , season_name , source_name ) :
  oO0OOoo0OO = O0ii1ii1ii ( url )
  OOO00O = re . compile ( '"file" : "(.+?)",\n.+?"default" : .+?,\n.+?"label" : "(.+?)"' , re . DOTALL ) . findall ( oO0OOoo0OO )
  for oo0 , i1Oo00 in OOO00O :
   self . Printer ( oo0 , season_name , source_name )
   if 16 - 16: o00O0oo * Ooo00oOo00o / OoOO
 def vidspot ( self , url , season_name , source_name ) :
  oO0OOoo0OO = O0ii1ii1ii ( url )
  OOO00O = re . compile ( '"file" : "(.+?)",\n.+?"default" : .+?,\n.+?"label" : "(.+?)"' ) . findall ( oO0OOoo0OO )
  for oo0 , i1Oo00 in OOO00O :
   self . Printer ( oo0 , season_name , source_name )
   if 22 - 22: OoOO + iIii1I11I1II1 % Oo / o0000oOoOoO0o / o00O0oo
 def thevideo ( self , url , season_name , source_name ) :
  oO0OOoo0OO = O0ii1ii1ii ( url )
  OOO00O = re . compile ( "{ label: '.+?', file: '(.+?)' }" ) . findall ( oO0OOoo0OO )
  for oo0 in OOO00O :
   self . Printer ( oo0 , season_name , source_name )
   if 54 - 54: I1IiI % IIII . i11iIiiIii
 def vodlocker ( self , url , season_name , source_name ) :
  oO0OOoo0OO = O0ii1ii1ii ( url )
  OOO00O = re . compile ( 'file: "(.+?)",.+?skin' , re . DOTALL ) . findall ( oO0OOoo0OO )
  for oo0 in OOO00O :
   self . Printer ( oo0 , season_name , source_name )
   if 93 - 93: o0oO0 % i11iIiiIii % O0oO
 def daclips ( self , url , season_name , source_name ) :
  oO0OOoo0OO = O0ii1ii1ii ( url )
  OOO00O = re . compile ( '{ file: "(.+?)", type:"video" }' ) . findall ( oO0OOoo0OO )
  for oo0 in OOO00O :
   self . Printer ( oo0 , season_name , source_name )
   if 64 - 64: O0oO + OOOo0 * O0 / Oo - o0000oOoOoO0o % o0000oOoOoO0o
 def filehoot ( self , url , season_name , source_name ) :
  oO0OOoo0OO = O0ii1ii1ii ( url )
  OOO00O = re . compile ( 'file: "(.+?)",.+?skin' , re . DOTALL ) . findall ( oO0OOoo0OO )
  for oo0 in OOO00O :
   self . Printer ( oo0 , season_name , source_name )
   if 59 - 59: OoOO0ooOOoo0O + OoooooooOO
 def Printer ( self , Link , season_name , source_name ) :
  if 55 - 55: i11iIiiIii % iIii1I11I1II1 . i1IIi + OoooooooOO / i11iIiiIii
  if Link in ooOO0o . List :
   pass
  elif source_name in ooOO0o . source_list :
   pass
  else :
   O00 ( '[COLORgreen]' + source_name + '[/COLOR]' , Link , 10012 , oOOoO0 + 'WATCHSERIES.png' )
   i1111 . update ( 100 , "" , "Got Source" )
   ooOO0o . List . append ( Link )
   ooOO0o . source_list . append ( source_name )
   if 10 - 10: oO0o0ooO0 - OoOO * iIii1I11I1II1 % iIii1I11I1II1 * IIII - ii11ii1ii
   xbmcplugin . addSortMethod ( o0 , xbmcplugin . SORT_METHOD_TITLE ) ;
   if 97 - 97: OoOoOO00 % O0oO + O0oO - Ooo00oOo00o / o00O0oo * OOOo0
   if 17 - 17: o00O0oo
   if 39 - 39: o0oO0 . OoOoOO00
   if 45 - 45: OoOO * I1IiI / iIii1I11I1II1
   if 77 - 77: O0oO - o0000oOoOoO0o
def iiI1iI1I ( ) :
 iiiiiIIii ( '[COLORgreen]Highlights[/COLOR]' , '' , 10008 , oOOoO0 + 'ORIGINFOOTBALL.png' , OOooO0OOoo , '' )
 iiiiiIIii ( '[COLORgreen]Fixtures[/COLOR]' , '' , 10009 , oOOoO0 + 'ORIGINFOOTBALL.png' , OOooO0OOoo , '' )
 if 27 - 27: ii11ii1ii * O0oO - Ooo00oOo00o + o00O0oo * o00O0oo
def o0OO0O0OO0oO0 ( ) :
 iiII1i1 = O0ii1ii1ii ( oOo0oooo00o ( 'aHR0cDovL2xpdmVvbnNhdC5jb20vcXVpY2tpbmRleC5odG1s' ) )
 OOO00O = re . compile ( '<a target="_self" href="(.+?)".+?src="(.+?)" alt="(.+?)"' , re . DOTALL ) . findall ( iiII1i1 )
 for ooOOO00Ooo , oooooOoo0ooo , i1Oo00 in OOO00O :
  iiiiiIIii ( '[COLORgreen]' + ( i1Oo00 ) . replace ( 'amp;' , '' ) + '[/COLOR]' , oOo0oooo00o ( 'aHR0cDovL2xpdmVvbnNhdC5jb20v' ) + ooOOO00Ooo , 10010 , oOo0oooo00o ( 'aHR0cDovL2xpdmVvbnNhdC5jb20v' ) + oooooOoo0ooo , OOooO0OOoo , '' )
  if 9 - 9: OoOO % i11iIiiIii / Oo
def IIIiI1ii1IIi ( url ) :
 oO0OOoo0OO = O0ii1ii1ii ( url )
 iIiIIIi = re . compile ( 'AndClearL.+?><h2.+?head>(.*?)float' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for iIiIIIi in iIiIIIi :
  o0O0oo0o = re . compile ( '(.*?)</h2>' ) . findall ( str ( iIiIIIi ) )
  for II11iI1iiI in o0O0oo0o :
   II11iI1iiI = II11iI1iiI
  I1ii = re . compile ( 'comp_head>(.*?)</span>.*?<div class = fLeft width = ".*?"><img src="(.*?)">.*?</div>.*?ST:(.*?)</div>(.+?)<!-- around all of channel types ENDS 2-->' , re . DOTALL ) . findall ( str ( iIiIIIi ) )
  for oO0o , oooooOoo0ooo , time , I1I1 in I1ii :
   oo00O00oO = re . compile ( ",CAPTION, '(.+?)&nbsp" ) . findall ( I1I1 )
   iiiiiIIii ( '[COLORgreen]' + II11iI1iiI + ' - ' + oO0o + ' - ' + time + '[/COLOR]' , '' , 10010 , oOo0oooo00o ( 'aHR0cDovL2xpdmVvbnNhdC5jb20=' ) + oooooOoo0ooo , OOooO0OOoo , ( str ( oo00O00oO ) ) )
   if 99 - 99: o0oO0 / iIii1I11I1II1 - o00O0oo * ii11ii1ii % OOOo0
 Oooo0Ooo000 ( 'tvshows' , 'Media Info 3' )
 if 13 - 13: Ooo00oOo00o
def O0oo0O0 ( ) :
 if 2 - 2: OoooooooOO . OoOO0ooOOoo0O . IIII
 iiiiiIIii ( '[COLORgreen]Shows[/COLOR]' , 'http://www.fullmatchesandshows.com/category/show/' , 10011 , 'http://www.fm-base.co.uk/forum/attachments/club-competition-logos/3885-soccer-am-logo-socceram.png' , oOOoO0 + 'fanart.jpg' , '' )
 iiiiiIIii ( '[COLORgreen]Premier League[/COLOR]' , 'http://www.fullmatchesandshows.com/premier-league/' , 10011 , 'https://footballseasons.files.wordpress.com/2013/05/premier-league.png' , oOOoO0 + 'fanart.jpg' , '' )
 iiiiiIIii ( '[COLORgreen]La Liga[/COLOR]' , 'http://www.fullmatchesandshows.com/la-liga/' , 10011 , 'http://1.bp.blogspot.com/-c6kQ40ryhyo/U19cUlz25sI/AAAAAAAABak/qtn5chSFZm0/s1600/la-liga-logo_display_image.png' , oOOoO0 + 'fanart.jpg' , '' )
 iiiiiIIii ( '[COLORgreen]Bundesliga[/COLOR]' , 'http://www.fullmatchesandshows.com/bundesliga/' , 10011 , 'http://m.img.brothersoft.com/iphone/189/518670189_icon175x175.jpg' , oOOoO0 + 'fanart.jpg' , '' )
 iiiiiIIii ( '[COLORgreen]Champions League[/COLOR]' , 'http://www.fullmatchesandshows.com/champions-league/' , 10011 , 'http://www.ecursuri.ro/images/teste/test-champions-league.jpg' , oOOoO0 + 'fanart.jpg' , '' )
 iiiiiIIii ( '[COLORgreen]Serie A[/COLOR]' , 'http://www.fullmatchesandshows.com/category/serie-a/' , 10011 , 'http://files.jcriccione.it/200000223-2484526782/serie%20a.png' , oOOoO0 + 'fanart.jpg' , '' )
 iiiiiIIii ( '[COLORgreen]Ligue 1[/COLOR]' , 'http://www.fullmatchesandshows.com/category/ligue-1/' , 10011 , 'http://a1.mzstatic.com/us/r30/Purple5/v4/37/c7/44/37c744ae-5824-42b7-6ce0-5f471f52baab/icon180x180.jpeg' , oOOoO0 + 'fanart.jpg' , '' )
 iiiiiIIii ( '[COLORgreen]Copa America 2015[/COLOR]' , 'http://www.fullmatchesandshows.com/copa-america-2015/' , 10011 , 'https://pbs.twimg.com/profile_images/521966985907691520/Nq9OAPIo_400x400.png' , oOOoO0 + 'fanart.jpg' , '' )
 iiiiiIIii ( '[COLORgreen]CONCACAF[/COLOR]' , 'http://www.fullmatchesandshows.com/category/concacaf/' , 10011 , 'http://a3.mzstatic.com/us/r30/Purple3/v4/40/26/14/4026147c-7022-4ca3-504e-e78950cc3f1c/icon175x175.png' , oOOoO0 + 'fanart.jpg' , '' )
 iiiiiIIii ( '[COLORgreen]Women World Cup[/COLOR]' , 'http://www.fullmatchesandshows.com/category/women-world-cup/' , 10011 , 'https://upload.wikimedia.org/wikipedia/en/thumb/7/76/2015_FIFA_Women\'s_World_Cup_logo.svg/967px-2015_FIFA_Women\'s_World_Cup_logo.svg.png' , oOOoO0 + 'fanart.jpg' , '' )
 if 42 - 42: OoOO0ooOOoo0O % OoOO / Ooo00oOo00o - OoOO * i11iIiiIii
def iI1IiiiIiI1Ii ( url ) :
 oO0OOoo0OO = O0ii1ii1ii ( url )
 OOO00O = re . compile ( 'itemprop="image" class="entry-thumb" src="(.+?)".+?<h3 itemprop="name" class="entry-title td-module-title"><a itemprop="url" href="(.+?)" rel="bookmark" title=".+?">(.+?)</a></h3>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for oooooOoo0ooo , url , i1Oo00 in OOO00O :
  Oo000 = i1Oo00 . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' )
  O00 ( '[COLORgreen]' + Oo000 + '[/COLOR]' , url , 10013 , oooooOoo0ooo )
  if 48 - 48: i11iIiiIii % OoOO
def i11i11 ( url ) :
 oO0OOoo0OO = O0ii1ii1ii ( url )
 OOO00O = re . compile ( '<script data-config="(.+?)" data-height' ) . findall ( oO0OOoo0OO )
 for I1IiI111I11 in OOO00O :
  Ii11Iii = ( I1IiI111I11 ) . replace ( '/v2' , '' ) . replace ( 'zeus.json' , 'video-sd.mp4?hosting_id=21772' ) . replace ( 'config.playwire.com' , 'cdn.video.playwire.com' )
  OO0 ( 'http:' + Ii11Iii )
  if 68 - 68: OOOo0 % O0
  if 74 - 74: i1IIi + I1IiI + iIii1I11I1II1 * I1IiI * iIii1I11I1II1 + o0000oOoOoO0o
def Oo0o ( url ) :
 iiII1i1 = o00oOO0o ( url )
 OOO00O = re . compile ( '<a href="([^"]*)" title="([^"]*)"><img itemprop="image" content="([^"]*)"' , re . DOTALL ) . findall ( iiII1i1 )
 ii11I1 = re . compile ( "<a rel='next' href=([^=]*)=" , re . DOTALL ) . findall ( iiII1i1 )
 for url , i1Oo00 , oooooOoo0ooo in OOO00O :
  O00 ( i1Oo00 , url , 8046 , oooooOoo0ooo )
 for url in ii11I1 :
  iiIiIiiiII ( 'NEXT PAGE' , ( url ) . replace ( ' class' , '' ) , 8045 , oOOoO0 + 'geniekitchen.png' )
def IiI1I1I ( url ) :
 iiII1i1 = o00oOO0o ( url )
 OOO00O = re . compile ( "__filename='([^']*)',.+?__fullimage='([^']*)',.+?__title='([^']*)'," , re . DOTALL ) . findall ( iiII1i1 )
 for url , oooooOoo0ooo , i1Oo00 in OOO00O :
  OO0 ( 'http://bitcast-b.bitgravity.com/ndtvod/23372/ndtv/' + url )
  if 62 - 62: IIII * O0
def oO0o00ooO0OoO ( url ) :
 iiII1i1 = o00oOO0o ( url )
 OOO00O = re . compile ( "src='http://www.youtube.com/embed/(.+?)?version=3&#038;rel=1&#038;fs=1&#038;autohide=2&#038;showsearch=0&#038;showinfo=1&#038;iv_load_policy=1&#038;wmode=transparent' frameborder='0' allowfullscreen='true'></iframe>" ) . findall ( iiII1i1 )
 for url in OOO00O :
  yt . PlayVideo ( url )
  if 1 - 1: I1IiI . i11iIiiIii % I1IiI - oO0o0ooO0 % i1IIi + ii11ii1ii
def IiiIiIi111iI1 ( ) :
 iiII1i1 = o00oOO0o ( oOo0oooo00o ( 'aHR0cDovL3RvcGRvY3VtZW50YXJ5ZmlsbXMuY29tLw==' ) )
 OOO00O = re . compile ( '<a href="(.+?)" >(.+?)</a></li><li>' ) . findall ( iiII1i1 )
 for ooOOO00Ooo , i1Oo00 in OOO00O :
  iiIiIiiiII ( i1Oo00 , ooOOO00Ooo , 8041 , oOOoO0 + 'documentary.png' )
def oOOO0o0ooOo ( url ) :
 iiII1i1 = o00oOO0o ( url )
 OOO00O = re . compile ( '<h2><a href="(.+?)" title="(.+?)">.+?</a></h2>.+?src="(.+?)"' , re . DOTALL ) . findall ( iiII1i1 )
 ii11I1 = re . compile ( 'class="inactive">.+?</a><a href="(.+?)">Next</a></div>' , re . DOTALL ) . findall ( iiII1i1 )
 for url , i1Oo00 , oooooOoo0ooo in OOO00O :
  iiIiIiiiII ( ( i1Oo00 ) . replace ( '&#039;s' , '' ) , url , 8042 , oooooOoo0ooo )
 for url in ii11I1 :
  iiIiIiiiII ( 'NEXT PAGE' , url , 8041 , oOOoO0 + 'documentary.png' )
  if 95 - 95: o00O0oo % IIII . O0 % O0oO
  if 68 - 68: Oo . Oo - ii11ii1ii / o0000oOoOoO0o . o0oO0 / i1IIi
def iI1i1iIi1iiII ( url ) :
 iiII1i1 = o00oOO0o ( url )
 OOO00O = re . compile ( '<meta itemprop="name" content="(.+?)".+?<meta itemprop="thumbnailUrl" content="(.+?)".+?<meta itemprop="embedUrl" content="(.+?)".+?<meta itemprop="description" content="(.+?)" />' , re . DOTALL ) . findall ( iiII1i1 )
 ii11I1 = re . compile ( '<div class="video new-video"><iframe width="766" height="431" src="(.+?)&amp;iv_load_policy=3&amp;showinfo=0&amp;autohide=1"' , re . DOTALL ) . findall ( iiII1i1 )
 for i1Oo00 , oooooOoo0ooo , url , i1IIiIii1i in OOO00O :
  O00 ( ( i1Oo00 ) . replace ( '&#039;s' , '' ) , url . replace ( 'https://www.youtube.com/embed/' , '' ) , 8043 , oooooOoo0ooo )
 for url in ii11I1 :
  o0OoO0000o ( ( url ) . replace ( '//' , 'http://' ) )
  if 90 - 90: IIII . o0oO0 / iIii1I11I1II1
def o0OoO0000o ( url ) :
 iiII1i1 = o00oOO0o ( url )
 OOO00O = re . compile ( '<link rel="canonical" href="(.+?)">  <link rel="stylesheet"' ) . findall ( iiII1i1 )
 for url in OOO00O :
  O00 ( 'PLAY' , ( url ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , oOOoO0 + 'documentary.png' )
  if 28 - 28: IIII + OoOO - o0oO0 / iIii1I11I1II1 - OOOo0
def Ii1i1 ( ) :
 oO0OOoo0OO = o00oOO0o ( 'http://www.stream2watch.co/live-tv' )
 OOO00O = re . compile ( '<a href="(.+?)">.+?<img src="(.+?)" alt=".+?"/>.+?<span class="country_name">(.+?)<br />(.+?)</span>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for ooOOO00Ooo , oooooOoo0ooo , i1Oo00 , oOoO00 in OOO00O :
  iiIiIiiiII ( ( i1Oo00 + '[COLORgreen]' + oOoO00 + '[/COLOR]' ) , ooOOO00Ooo , 8086 , oooooOoo0ooo )
  if 45 - 45: o00O0oo . OoooooooOO
def i1iIIi11i111I ( url ) :
 oO0OOoo0OO = o00oOO0o ( url )
 OOO00O = re . compile ( '<a class="front_channel_href" href="(.+?)" title=".+?">.+?<img class="front_channel_thumb" src="(.+?)" alt=".+?"/>.+?<span class="front_channel_name">(.+?)</span>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for url , oooooOoo0ooo , i1Oo00 in OOO00O :
  iiIiIiiiII ( '[COLORgreen]' + i1Oo00 + '[/COLOR]' , url , 8087 , oooooOoo0ooo )
  if 16 - 16: OOOo0 . iIii1I11I1II1
def iiiIIIii ( url ) :
 oO0OOoo0OO = O0ii1ii1ii ( url )
 OOO00O = re . compile ( 'a id="code_.+?data-f-href="(.+?)" data-code-embed="">(.+?)</a>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for url , i1Oo00 in OOO00O :
  ooOoo00 ( url , i1Oo00 )
  if 34 - 34: OoOoOO00 + o0oO0 * iIii1I11I1II1 - O0oO - Ooo00oOo00o
def ooOoo00 ( url , name ) :
 oO0OOoo0OO = O0ii1ii1ii ( url )
 OOO00O = re . compile ( "playStream\('.+?', '(.+?)'\);" , re . DOTALL ) . findall ( oO0OOoo0OO )
 for url in OOO00O :
  print url
  O00 ( '[COLORgreen]' + name + '[/COLOR]' , url , 222 , '' )
  if 69 - 69: iIii1I11I1II1 * OOOo0 - oO0o0ooO0 + O0 + O0
def O0oo ( ) :
 iiII1i1 = o00oOO0o ( oOo0oooo00o ( 'aHR0cDovL3d3dy5zb2xpZS5vcmcvYWxpYnJhcnkvaW5kZXguaHRtbA==' ) )
 OOO00O = re . compile ( '<td align="center" valign="top">.+?<a href="(.+?)">.+?<img src="(.+?)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( iiII1i1 )
 for ooOOO00Ooo , oooooOoo0ooo , i1Oo00 in OOO00O :
  iiIiIiiiII ( ( '[COLORgreen]' + i1Oo00 + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + ooOOO00Ooo , 3002 , 'http://www.solie.org/alibrary/' + oooooOoo0ooo )
def ooOooO00Oo ( url ) :
 iiII1i1 = o00oOO0o ( url )
 OOO00O = re . compile ( '<td align="center" valign="top">.+?<a href="(.+?)">.+?<img src="(.+?)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( iiII1i1 )
 for url , oooooOoo0ooo , i1Oo00 in OOO00O :
  iiIiIiiiII ( ( '[COLORgreen]' + i1Oo00 + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3003 , 'http://www.solie.org/alibrary/' + oooooOoo0ooo )
def ooO00o ( url ) :
 iiII1i1 = o00oOO0o ( url )
 OOO00O = re . compile ( '<br><a href="([^"]*)">(.+?)</a>' ) . findall ( iiII1i1 )
 o0o00O0oOooO0 = re . compile ( 'href="([^"]*)">Season(.+?)</a>' ) . findall ( iiII1i1 )
 next = re . compile ( '<a href="([^"]*)">Episodes</a>' ) . findall ( iiII1i1 )
 ii11I1 = re . compile ( '<td align="center" valign="top">.+?<a href="(.+?)">.+?<img src="(.+?)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( iiII1i1 )
 for url , i1Oo00 in OOO00O :
  O00 ( ( '[COLORgreen]' + i1Oo00 + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3004 , oOOoO0 + 'classicmovies.png' )
 for url , i1Oo00 in o0o00O0oOooO0 :
  iiIiIiiiII ( '[COLORgreen]Season- ' + i1Oo00 + '[/COLOR]' , 'http://www.solie.org/alibrary/' + url , 3003 , oOOoO0 + 'classicmovies.png' )
 for url in next :
  iiIiIiiiII ( '[COLORgreen]NEXT[/COLOR]' , 'http://www.solie.org/alibrary/' + url , 3003 , oOOoO0 + 'classicmovies.png' )
 for url , oooooOoo0ooo , i1Oo00 in ii11I1 :
  iiIiIiiiII ( ( '[COLORgreen]' + i1Oo00 + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3003 , 'http://www.solie.org/alibrary/' + oooooOoo0ooo )
def o0oO0OO00ooOO ( url ) :
 iiII1i1 = o00oOO0o ( url )
 OOO00O = re . compile ( '<iframe.+?src="([^"]*)"' ) . findall ( iiII1i1 )
 for url in OOO00O :
  IiIIiii11II1 ( url )
def IiIIiii11II1 ( url ) :
 iiII1i1 = o00oOO0o ( url )
 OOO00O = re . compile ( '<meta property="og:video" content="([^"]*)"/>' ) . findall ( iiII1i1 )
 for url in OOO00O :
  OO0 ( url )
  if 42 - 42: i1IIi % OoOoOO00 . o0oO0
def II1II1iI ( ) :
 iiII1i1 = o00oOO0o ( oOo0oooo00o ( 'aHR0cDovL3JldHJvdmlzaW9uLnR2L2FsbC8=' ) )
 OOO00O = re . compile ( '<a href="([^"]*)"><h2><font color=".+?"><h2>(.+?)</font></h2></a>' ) . findall ( iiII1i1 )
 for ooOOO00Ooo , i1Oo00 in OOO00O :
  O00 ( ( '[COLORgreen]' + i1Oo00 + '[/COLOR]' ) . replace ( '&#8211;' , ':' ) , ooOOO00Ooo , 8061 , oOOoO0 + 'classicmovies.png' )
def OooooO ( url ) :
 iiII1i1 = o00oOO0o ( url )
 OOO00O = re . compile ( "v.src = '([^']*)';" ) . findall ( iiII1i1 )
 for url in OOO00O :
  OO0 ( url )
  if 92 - 92: OOooOOo / OOooOOo * o00O0oo
def iI111i11iI1 ( ) :
 iiII1i1 = o00oOO0o ( oOo0oooo00o ( 'aHR0cDovL3JldHJvdmlzaW9uLnR2L2NsYXNzaWMtdHYv' ) )
 OOO00O = re . compile ( '<a href="([^"]*)"><h2><font color=".+?"><h2>(.+?)</font></h2></a>' ) . findall ( iiII1i1 )
 for ooOOO00Ooo , i1Oo00 in OOO00O :
  O00 ( ( '[COLORgreen]' + i1Oo00 + '[/COLOR]' ) . replace ( '&#8211;' , ':' ) , ooOOO00Ooo , 8061 , oOOoO0 + 'classictv.png' )
def III1ii ( url ) :
 iiII1i1 = o00oOO0o ( url )
 OOO00O = re . compile ( "v.src = '([^']*)';" ) . findall ( iiII1i1 )
 for url in OOO00O :
  OO0 ( url )
  if 23 - 23: OoOO * oO0o0ooO0
def O0oOo00O ( ) :
 oO0OOoo0OO = O0ii1ii1ii ( oOo0oooo00o ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vbTN1c3RyZWFtcw==' ) )
 OOO00O = re . compile ( '<li><a href="(.+?)"> (.+?).m3u</a></li>' ) . findall ( oO0OOoo0OO )
 for ooOOO00Ooo , i1Oo00 in OOO00O :
  iiIiIiiiII ( ( '[COLORgreen]' + i1Oo00 + '[/COLOR]' ) . replace ( '-' , ' ' ) . replace ( '_' , ' ' ) , ( oOo0oooo00o ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vbTN1c3RyZWFtcy8=' ) ) + ooOOO00Ooo , 8071 , oOOoO0 + 'streams.png' )
def i1I1I1i1i1i ( url ) :
 oO0OOoo0OO = o00oOO0o ( url )
 OOO00O = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for i1Oo00 , url in OOO00O :
  O00 ( ( '[COLORgreen]' + i1Oo00 + '[/COLOR]' ) . replace ( '_' , ' ' ) , ( url ) . strip ( ) , 404 , oOOoO0 + 'streams.png' )
def ii1o0oo0Ooooo0 ( url ) :
 oO0OOoo0OO = o00oOO0o ( url )
 OOO00O = re . compile ( 'EXTINF:(.+?),(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for oooooOoo0ooo , i1Oo00 , url in OOO00O :
  url = ( ( oOo0oooo00o ( 'aHR0cDovL2dlbmlldHYuaXB0di5yZTo4MDAwL2xpdmUv' ) ) + oooOOOOO + '/' + i1iiIII111ii + url ) . strip ( )
  O00 ( ( '[COLORgreen]' + i1Oo00 + '[/COLOR]' ) . replace ( '_' , ' ' ) , url , 222 , oooooOoo0ooo )
  if 76 - 76: i1IIi * OoooooooOO * O0 + O0oO * O0oO
def i1iIiIii ( ) :
 OOo ( 'Best Videos' , 'http://www.xvideos.com/best' , 10105 , oOOoO0 + 'JIZBOX.png' , '' , '' )
 OOo ( 'Genres' , 'http://www.xvideos.com' , 10106 , oOOoO0 + 'JIZBOX.png' , '' , '' )
 OOo ( 'Recently Uploaded' , 'http://xvideos.com' , 10105 , oOOoO0 + 'JIZBOX.png' , '' , '' )
 OOo ( 'Tags' , 'http://www.xvideos.com/tags' , 10103 , oOOoO0 + 'JIZBOX.png' , '' , '' )
 OOo ( 'Search' , '' , 10107 , oOOoO0 + 'JIZBOX.png' , '' , '' , )
 if 20 - 20: OOooOOo * o0oO0
def i1III1iI ( url ) :
 oO0OOoo0OO = O0ii1ii1ii ( url )
 ii1i = re . compile ( '<li><a class=".+?".+?href="(.+?)">Next</a></li>' ) . findall ( oO0OOoo0OO )
 for url in ii1i :
  OOo ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10103 , oOOoO0 + 'JIZBOX.png' , '' , '' )
 OOO00O = re . compile ( '<li><a href="(.+?)"><b>(.+?)</b><span class="navbadge default"(.+?)</span>' ) . findall ( oO0OOoo0OO )
 for url , i1Oo00 , i1IiiiiIi1I in OOO00O :
  OOo ( i1Oo00 + ' - No of Videos : ' + ( i1IiiiiIi1I ) . replace ( '>' , '' ) , 'http://www.xvideos.com' + url , 10105 , oOOoO0 + 'JIZBOX.png' , '' , '' )
  if 56 - 56: OoooooooOO * O0
def oo0OoOOooO ( url ) :
 oO0OOoo0OO = O0ii1ii1ii ( url )
 ii1i = re . compile ( 'href="([^"]*)">Next</a></li>' ) . findall ( oO0OOoo0OO )
 for url in ii1i :
  OOo ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10104 , oOOoO0 + 'JIZBOX.png' , '' , '' )
 OOO00O = re . compile ( ':"([^"]*)".+?;</script></a></div></div><p class="profile-name"><a href="([^"]*)">(.+?)</a></p><p class="profile-counts">\n(.+?)\n' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for oooooOoo0ooo , url , i1Oo00 , o0o0OO0o00o0O in OOO00O :
  OOo ( i1Oo00 + '--' + o0o0OO0o00o0O , 'http://www.xvideos.com' + url + '#_tabVideos,videos-best' , 10105 , ( oooooOoo0ooo ) . replace ( 'http:\/\/' , 'http://' ) , '' , '' )
  if 28 - 28: Ooo00oOo00o - OoOO + I1IiI + o00O0oo / iIii1I11I1II1
  if 26 - 26: iIii1I11I1II1 - O0 . O0
def O0oOoo ( url ) :
 oO0OOoo0OO = O0ii1ii1ii ( url )
 OOO00O = re . compile ( '<div class="thumb-inside"><script>.+?<img src="(.+?)".+?<a href="(.+?)" title=".+?">(.+?)</a></p>.+?uration">(.+?)</span>.+?Porn quality:(.+?)</span>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for oooooOoo0ooo , url , i1Oo00 , I1I1IiI1 , OoOOoO0O0oO in OOO00O :
  o0OOoo0OO0OOO ( i1Oo00 + ' - Porn Quality : ' + OoOOoO0O0oO + ' - ' + I1I1IiI1 , 'http://www.xvideos.com' + url , 10108 , oooooOoo0ooo , oooooOoo0ooo , OoOOoO0O0oO + ' - ' + I1I1IiI1 )
 oOOoO = re . compile ( '<li><a href="([^"]*)" class="no-page">Next</a></li></ul></div>' ) . findall ( oO0OOoo0OO )
 for url in oOOoO :
  OOo ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10105 , oOOoO0 + 'JIZBOX.png' , '' , '' )
  if 87 - 87: I1IiI % iIii1I11I1II1
def o0OO0OOO0O ( url ) :
 oO0OOoo0OO = O0ii1ii1ii ( url )
 iIiIIIi = re . compile ( '<div class="main-categories">(.+?)</div>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 ii1i = re . compile ( '<li><a class=".+?".+?href="(.+?)">Next</a></li>' ) . findall ( oO0OOoo0OO )
 for url in ii1i :
  OOo ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10106 , oOOoO0 + 'JIZBOX.png' , '' , '' )
 OOO00O = re . compile ( '<li><a href="(.+?)" class="btn btn-default">(.+?)</a>' ) . findall ( str ( iIiIIIi ) )
 for url , i1Oo00 in OOO00O :
  OOo ( i1Oo00 , 'http://www.xvideos.com' + url , 10105 , oOOoO0 + 'JIZBOX.png' , '' , '' )
  if 36 - 36: i11iIiiIii / oO0o0ooO0 . o0000oOoOoO0o + IIII . O0 + OOOo0
  if 36 - 36: i1IIi - ii11ii1ii - O0oO
def iiiI1I ( ) :
 O00OOOoOoo0O = Oo0o0000o0o0 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oO0OOO0o0O = ( O00OOOoOoo0O ) . replace ( ' ' , '+' ) . replace ( '&amp;' , '&' )
 oo0OOo = oO0OOO0o0O . lower ( )
 OOOOO0 = 'http://www.xvideos.com/?k=' + oo0OOo
 print OOOOO0 + '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'
 oO0OOoo0OO = O0ii1ii1ii ( OOOOO0 )
 OOO00O = re . compile ( '<div class="thumb-inside"><script>.+?<img src="(.+?)".+?<a href="(.+?)" title=".+?">(.+?)</a></p>.+?uration">(.+?)</span>.+?Porn quality:(.+?)</span>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for oooooOoo0ooo , ooOOO00Ooo , i1Oo00 , I1I1IiI1 , OoOOoO0O0oO in OOO00O :
  o0OOoo0OO0OOO ( i1Oo00 + ' - Porn Quality : ' + OoOOoO0O0oO + ' - ' + I1I1IiI1 , 'http://www.xvideos.com' + ooOOO00Ooo , 10108 , oooooOoo0ooo , oooooOoo0ooo , OoOOoO0O0oO + ' - ' + I1I1IiI1 )
 oOOoO = re . compile ( '<li><a href="([^"]*)" class="no-page">Next</a></li></ul></div>' ) . findall ( oO0OOoo0OO )
 for ooOOO00Ooo in oOOoO :
  OOo ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + ooOOO00Ooo , 10105 , oOOoO0 + 'JIZBOX.png' , '' , '' )
  if 79 - 79: OoOoOO00 - o0oO0 . i1IIi + O0 % O0 * OOOo0
def Ii1Ii1I ( url ) :
 oO0OOoo0OO = O0ii1ii1ii ( url )
 OOO00O = re . compile ( 'flv_url=(.+?)\;' ) . findall ( oO0OOoo0OO )
 for url in OOO00O :
  oOO0oo = ( url ) . replace ( '%3A' , ':' ) . replace ( '%2F' , '/' ) . replace ( '%3F' , '?' ) . replace ( '%3D' , '=' ) . replace ( '%26' , '&' ) . replace ( '&amp' , '' )
  Oo00O0OO ( oOO0oo )
  if 77 - 77: OoOO - Oo - iIii1I11I1II1
def Oo00O0OO ( url ) :
 IiI11i1IIiiI = xbmc . Player ( IIi1i ( ) )
 import urlresolver
 try : IiI11i1IIiiI . play ( url )
 except : pass
 if 21 - 21: OoOO % OoOO / Ooo00oOo00o
 if 12 - 12: oO0o0ooO0 / I1IiI
def ooooo0Oo0 ( ) :
 oO0OOoo0OO = O0ii1ii1ii ( oOo0oooo00o ( 'aHR0cDovL3d3dy5nb2Zpc2hpbmcuY28udWsvQW5nbGluZy1UaW1lcy9TZWN0aW9uL1ZpZGVvcy8=' ) )
 OOO00O = re . compile ( 'class="item.+?"><a href="(.+?)">(.+?)</a></li>' ) . findall ( oO0OOoo0OO )
 for ooOOO00Ooo , i1Oo00 in OOO00O :
  iiIiIiiiII ( '[COLORgreen]' + i1Oo00 + '[/COLOR]' , ( 'http://www.gofishing.co.uk' + ooOOO00Ooo ) . replace ( 'http://www.gofishing.co.ukhttp://www.gofishing.co.uk' , 'http://www.gofishing.co.uk' ) , 8091 , oOOoO0 + 'gofish.png' )
def o0I1IIIi11ii11 ( url ) :
 oO0OOoo0OO = o00oOO0o ( url )
 OOO00O = re . compile ( '<h2><a id=.+?href="([^"]*)">(.+?)</a></h2>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 ii11I1 = re . compile ( '<h3><a href="([^"]*)" id=.+?>(.+?)</a> </h3>.+?<img src="([^"]*)"' , re . DOTALL ) . findall ( oO0OOoo0OO )
 next = re . compile ( 'href="([^"]*)">next</a>&gt;</li>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for url , i1Oo00 in OOO00O :
  O00 ( '[COLORgreen]' + i1Oo00 + '[/COLOR]' , 'http://www.gofishing.co.uk/' + url , 8092 , oOOoO0 + 'gofish.png' )
 for url , i1Oo00 , oooooOoo0ooo in ii11I1 :
  O00 ( '[COLORgreen]' + i1Oo00 + '[/COLOR]' , 'http://www.gofishing.co.uk/' + url , 8092 , 'http://www.gofishing.co.uk/' + oooooOoo0ooo )
 for url in next :
  iiIiIiiiII ( '[COLORgreen]NEXT[/COLOR]' , url . replace ( ' ' , '+' ) , 8091 , oOOoO0 + 'gofish.png' )
def O0o0oo0oOO0oO ( url ) :
 oO0OOoo0OO = o00oOO0o ( url )
 OOO00O = re . compile ( 'src="https://www.youtube.com/embed/(.+?)"' ) . findall ( oO0OOoo0OO )
 for url in OOO00O :
  yt . PlayVideo ( url )
  if 15 - 15: Ooo00oOo00o * OoOoOO00
def o0oO00 ( url ) :
 O00o0O = urllib2 . Request ( url )
 O00o0O . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
 O00oOo0O0o00O = ''
 iI1i111I1Ii = ''
 try :
  O00oOo0O0o00O = urllib2 . urlopen ( O00o0O )
  iI1i111I1Ii = O00oOo0O0o00O . read ( )
  O00oOo0O0o00O . close ( )
 except : pass
 if iI1i111I1Ii != '' :
  return iI1i111I1Ii
 else :
  iI1i111I1Ii = 'Failed'
  return iI1i111I1Ii
  if 91 - 91: OoOoOO00 * oO0o0ooO0 . i1IIi
def II11Ii111II1 ( ) :
 O00OOO00Ooo = ( oOo0oooo00o ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 O00OOOoOoo0O = Oo0o0000o0o0 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oo0OOo = O00OOOoOoo0O . lower ( )
 ooOOO00Ooo = ( oOo0oooo00o ( 'aHR0cDovL2RsNC5tb3ZpZWZhcnNpLmNvbS9maWxtLzIwMTUtNy8=' ) )
 I111iIi1 = ( oOo0oooo00o ( 'aHR0cDovL2RsLmF2YWRsLmNvbS9OZXcvTW92aWUv' ) )
 OoOOoooO000 = ( oOo0oooo00o ( 'aHR0cDovLzIxNy4yMTkuMTQzLjEwOC8xMzI3Lw==' ) )
 OoO0o000oOo = ( oOo0oooo00o ( 'aHR0cDovLzE3OC4xNjIuMjE0LjIzMi92b2QvbW92aWVzL2VuZ2xpc2gv' ) )
 Oo00OO00o0oO = ( oOo0oooo00o ( 'aHR0cDovL3Njb29ieXN0cmVhbS54MTBob3N0LmNvbS8vc2Nvb2J5L21vdi9hbGwucGhw' ) )
 iI1I1I1i1i = ( oOo0oooo00o ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 OOo0O = ( oOo0oooo00o ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL3NlYXJjaC8/cT0=' ) ) + O00OOOoOoo0O
 oOOoooO0O0 = ( oOo0oooo00o ( 'aHR0cDovL2xldHdhdGNoLnVzLz9vcD1zZWFyY2gmaz0=' ) ) + ( O00OOOoOoo0O ) . replace ( ' ' , '+' )
 if 46 - 46: iIii1I11I1II1
 oO0OOoo0OO = o0oO00 ( ooOOO00Ooo )
 II1IIIii = o0oO00 ( I111iIi1 )
 I111iiiii1 = o0oO00 ( OoOOoooO000 )
 OO0ooOoOO0OOo = o0oO00 ( OoO0o000oOo )
 OooOoooo0000 = o0oO00 ( Oo00OO00o0oO )
 I1ii1i11i = o0oO00 ( OOo0O )
 Oooooo0O00o = O0ii1ii1ii ( oOOoooO0O0 )
 if 36 - 36: I1IiI + IIII * O0 . OoooooooOO * OoooooooOO
 if oO0OOoo0OO != 'Failed' :
  OOO00O = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( oO0OOoo0OO )
  for oOO0OOOo000o , i1Oo00 in OOO00O :
   if O00OOOoOoo0O in i1Oo00 . lower ( ) :
    O00 ( ( '[COLORgreen]' + i1Oo00 + '- source 1[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( ooOOO00Ooo + oOO0OOOo000o ) , 222 , '' )
 if II1IIIii != 'Failed' :
  ii11I1 = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( II1IIIii )
  for oOO0OOOo000o , i1Oo00 in ii11I1 :
   if O00OOOoOoo0O in i1Oo00 . lower ( ) :
    O00 ( ( '[COLORgreen]' + i1Oo00 + '- source 2[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( I111iIi1 + oOO0OOOo000o ) , 222 , '' )
 if I111iiiii1 != 'Failed' :
  iI1I1iIi11 = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( I111iiiii1 )
  for oOO0OOOo000o , i1Oo00 in iI1I1iIi11 :
   if O00OOOoOoo0O in i1Oo00 . lower ( ) :
    O00 ( ( '[COLORgreen]' + i1Oo00 + '- source 3[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( OoOOoooO000 + oOO0OOOo000o ) , 222 , '' )
 if OO0ooOoOO0OOo != 'Failed' :
  OO00oo = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( OO0ooOoOO0OOo )
  for oOO0OOOo000o , i1Oo00 in OO00oo :
   if O00OOOoOoo0O in i1Oo00 . lower ( ) :
    O00 ( ( '[COLORgreen]' + i1Oo00 + '- source 4[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( OoO0o000oOo + oOO0OOOo000o ) , 222 , '' )
 if OooOoooo0000 != 'Failed' :
  O0Oo0O0 = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( OooOoooo0000 )
  for oOO0OOOo000o , oooooOoo0ooo , i1Oo00 in O0Oo0O0 :
   if O00OOOoOoo0O in i1Oo00 . lower ( ) :
    iiIiIiiiII ( ( '[COLORgreen]' + i1Oo00 + '- source Scooby[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( 'Ganool' , '' ) . replace ( 'ShAaNiG' , '' ) . replace ( 'YIFY' , '' ) . replace ( '[[ Max-Movie.In ]]' , '' ) . replace ( '.mkv' , '' ) . replace ( '.mp4' , '' ) . replace ( '.' , ' ' ) , oOO0OOOo000o , 1006 , 'img' )
    if 33 - 33: o0oO0 % i1IIi - OoOO . O0 / O0
    Oooo0Ooo000 ( 'tvshows' , 'Media Info 3' )
 if I1ii1i11i != 'Failed' :
  oo00o0 = re . compile ( 'href="(.+?)".+?src="(.+?)" alt="Image of (.+?)"' , re . DOTALL ) . findall ( I1ii1i11i )
  for ooOOO00Ooo , oooooOoo0ooo , i1Oo00 in oo00o0 :
   if O00OOOoOoo0O in i1Oo00 . lower ( ) :
    iiIiIiiiII ( ( '[COLORgreen]' + i1Oo00 + '- source Snag[/COLOR]' ) . replace ( '&#x27;' , '' ) , 'http://www.snagfilms.com' + ooOOO00Ooo , 7067 , oooooOoo0ooo )
    if 17 - 17: o00O0oo / iIii1I11I1II1 - Ooo00oOo00o + OOOo0 % OoOO0ooOOoo0O
    Oooo0Ooo000 ( 'tvshows' , 'Media Info 3' )
 if Oooooo0O00o != 'Failed' :
  III1III11II = re . compile ( '<div class="video_block video_block_default ">.+?<a href="#">.+?<a href="(.*?)".+?<img src="(.+?)" height=".+?" alt="(.+?)"' , re . DOTALL ) . findall ( Oooooo0O00o )
  for ooOOO00Ooo , oooooOoo0ooo , i1Oo00 in III1III11II :
   O00 ( '[COLORgreen]' + i1Oo00 + '- Source 7[/COLOR]' , ooOOO00Ooo , 222 , oooooOoo0ooo )
 iIiI = [ '0-9/' , 'A/' , 'B/' , 'C/' , 'D/' , 'E/' , 'F/' , 'G/' , 'H/' , 'I/' , 'J/' , 'K/' , 'L/' , 'M/' , 'N/' , 'O/' , 'P/' , 'R/' , 'S/' , 'T/' , 'U/' , 'V/' , 'W/' , 'X/' , 'Y/' , 'Z/' ]
 if 43 - 43: OOOo0
 if 47 - 47: OoooooooOO % I1IiI
 for ii1I11iIiIII1 in iIiI :
  oOO0OOOOoooO = O00OOO00Ooo + ii1I11iIiIII1
  OO0Oo = o0oO00 ( oOO0OOOOoooO )
  if OooOoooo0000 != 'Failed' :
   IIiiiiiIiIIi = re . compile ( '<li><a href="(.+?)"> (.+?)</a></li>' ) . findall ( OO0Oo )
   for oOO0OOOo000o , i1Oo00 in IIiiiiiIiIIi :
    if O00OOOoOoo0O in i1Oo00 . lower ( ) :
     O00 ( ( '[COLORgreen]' + i1Oo00 + 'source 5[/COLOR]' ) . replace ( 'Ganool' , '' ) . replace ( 'ShAaNiG' , '' ) . replace ( 'YIFY' , '' ) . replace ( '[[ Max-Movie.In ]]' , '' ) . replace ( '.mkv' , '' ) . replace ( '.mp4' , '' ) . replace ( '.' , ' ' ) , ( O00OOO00Ooo + ii1I11iIiIII1 + oOO0OOOo000o ) , 222 , '' )
     if 26 - 26: OOooOOo
     Oooo0Ooo000 ( 'tvshows' , 'Media Info 3' )
     if 12 - 12: OoooooooOO / O0 + OoOoOO00 * ii11ii1ii
     if 46 - 46: OoOoOO00 - IIII * OoooooooOO / OoOO % IIII
def Ii ( ) :
 if 18 - 18: IIII % OoOO * I1IiI
 O00OOOoOoo0O = Oo0o0000o0o0 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oo0OOo = O00OOOoOoo0O . lower ( )
 O00Ooo = ( oOo0oooo00o ( 'aHR0cDovL2Nvb2x0dnNlcmllcy5jb20vc2VhcmNoLnBocD90YWc9' ) ) + ( O00OOOoOoo0O ) . replace ( ' ' , '+' )
 ooOOO00Ooo = ( oOo0oooo00o ( 'aHR0cDovL2RsLmZhcnNpbW92aWUubmV0L1NlcmlhbC8=' ) )
 I111iIi1 = ( oOo0oooo00o ( 'aHR0cDovL3N2Mi5kbC1wYXJzLmluLw==' ) )
 OoOOoooO000 = ( oOo0oooo00o ( 'aHR0cDovL3R2LmRsLXBhcnMuaW4v' ) )
 OoO0o000oOo = ( oOo0oooo00o ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9BbWVyaWNhbiUyMFNlcmlhbC8=' ) )
 Oo00OO00o0oO = ( oOo0oooo00o ( 'aHR0cDovL2RpemlsYWIuY29tL2Fyc2l2P2xpbWl0PSZ0dXI9Jm9yZGVyYnk9JnVsa2U9Jm9yZGVyPSZ5aWw9JmRpemlfYWRpPQ==' ) ) + ( O00OOOoOoo0O ) . replace ( ' ' , '+' )
 iI1I1I1i1i = ( oOo0oooo00o ( 'aHR0cDovL3Njb29ieXN0cmVhbS54MTBob3N0LmNvbS8vc2Nvb2J5L3Nob3dzL3R2YWxsLnBocA==' ) )
 oOOoooO0O0 = ( oOo0oooo00o ( 'aHR0cDovL2xldHdhdGNoLnVzLz9vcD1zZWFyY2gmaz0=' ) ) + ( O00OOOoOoo0O ) . replace ( ' ' , '+' )
 i1oOOO0ooOO = ( oOo0oooo00o ( 'aHR0cDovL3d3dy53YXRjaHNlcmllcy5saS9zZWFyY2gv' ) ) + ( O00OOOoOoo0O ) . replace ( ' ' , '%20' )
 if 3 - 3: OoooooooOO
 O0OoO0o = o0oO00 ( O00Ooo )
 oO0OOoo0OO = o0oO00 ( ooOOO00Ooo )
 II1IIIii = o0oO00 ( I111iIi1 )
 I111iiiii1 = o0oO00 ( OoOOoooO000 )
 OO0ooOoOO0OOo = o0oO00 ( OoO0o000oOo )
 OooOoooo0000 = cloudflare . source ( Oo00OO00o0oO )
 OO0Oo = o0oO00 ( iI1I1I1i1i )
 Oooooo0O00o = O0ii1ii1ii ( oOOoooO0O0 )
 I111IIiIII = O0ii1ii1ii ( i1oOOO0ooOO )
 if O0OoO0o != 'Failed' :
  OO0OOoo0OOO = re . compile ( 'href="([^"]*)"><img src="([^"]*)" alt="([^"]*)"' ) . findall ( O0OoO0o )
  for ooOOO00Ooo , oooooOoo0ooo , i1Oo00 in OO0OOoo0OOO :
   if O00OOOoOoo0O in i1Oo00 . lower ( ) :
    iiIiIiiiII ( '[COLORgreen]' + i1Oo00 + ' CoolSeries[/COLOR]' , ooOOO00Ooo , 7052 , oooooOoo0ooo )
    if 94 - 94: i11iIiiIii % OoooooooOO / OOOo0
    Oooo0Ooo000 ( 'tvshows' , 'Media Info 3' )
 if oO0OOoo0OO != 'Failed' :
  OOO00O = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( oO0OOoo0OO )
  for i1Oo00 in OOO00O :
   if O00OOOoOoo0O in i1Oo00 . lower ( ) :
    iiIiIiiiII ( ( '[COLORgreen]' + i1Oo00 + ' source 1[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( ooOOO00Ooo + i1Oo00 ) . replace ( ' ' , '%20' ) , 1006 , '' )
    if 24 - 24: OOOo0 * OoOO
    Oooo0Ooo000 ( 'tvshows' , 'Media Info 3' )
 if II1IIIii != 'Failed' :
  ii11I1 = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( II1IIIii )
  for i1Oo00 in ii11I1 :
   if O00OOOoOoo0O in i1Oo00 . lower ( ) :
    iiIiIiiiII ( ( i1Oo00 + ' source 2' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( I111iIi1 + i1Oo00 ) . replace ( ' ' , '%20' ) , 1006 , '' )
    if 85 - 85: OoOoOO00 . o0oO0 % OoOO0ooOOoo0O % o0000oOoOoO0o
    Oooo0Ooo000 ( 'tvshows' , 'Media Info 3' )
 if I111iiiii1 != 'Failed' :
  iI1I1iIi11 = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( I111iiiii1 )
  for i1Oo00 in ii11I1 :
   if O00OOOoOoo0O in i1Oo00 . lower ( ) :
    iiIiIiiiII ( ( i1Oo00 + ' source 3' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( OoOOoooO000 + i1Oo00 ) . replace ( ' ' , '%20' ) , 1006 , '' )
    if 80 - 80: OoOO * o0000oOoOoO0o / iIii1I11I1II1 % OoOO / iIii1I11I1II1
    Oooo0Ooo000 ( 'tvshows' , 'Media Info 3' )
 if OO0ooOoOO0OOo != 'Failed' :
  OO00oo = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( OO0ooOoOO0OOo )
  for i1Oo00 in ii11I1 :
   if O00OOOoOoo0O in i1Oo00 . lower ( ) :
    iiIiIiiiII ( ( i1Oo00 + ' source 4' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( OoO0o000oOo + i1Oo00 ) . replace ( ' ' , '%20' ) , 1006 , '' )
    if 42 - 42: i1IIi / i11iIiiIii . Oo * oO0o0ooO0 . i11iIiiIii * O0
    Oooo0Ooo000 ( 'tvshows' , 'Media Info 3' )
 if OooOoooo0000 != 'Failed' :
  O0Oo0O0 = re . compile ( '<a href="(.+?)" class="film-image">\n<img src="(.+?)" alt=""/>\n</a>\n<div class="tss-detail">\n<a class="title" style="" href=".+?">\n<span class="position">.+?</span>\n(.+?)</a>' ) . findall ( OooOoooo0000 )
  for ooOOO00Ooo , oooooOoo0ooo , i1Oo00 in O0Oo0O0 :
   if O00OOOoOoo0O in i1Oo00 . lower ( ) :
    iiIiIiiiII ( '[COLORgreen]' + i1Oo00 + ' - Source - Dizi[/COLOR]' , ooOOO00Ooo , 8062 , oooooOoo0ooo )
    if 44 - 44: i1IIi . OOOo0 / i11iIiiIii + IIII
    Oooo0Ooo000 ( 'tvshows' , 'Media Info 3' )
 if OO0Oo != 'Failed' :
  IIiiiiiIiIIi = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( OO0Oo )
  for ooOOO00Ooo , oooooOoo0ooo , i1Oo00 in IIiiiiiIiIIi :
   if O00OOOoOoo0O in i1Oo00 . lower ( ) :
    O00 ( ( '[COLORgreen]' + i1Oo00 + '- Source Scooby[/COLOR]' ) , ooOOO00Ooo , 222 , 'img' )
    if 27 - 27: OoOO0ooOOoo0O
    Oooo0Ooo000 ( 'tvshows' , 'Media Info 3' )
 if Oooooo0O00o != 'Failed' :
  III1III11II = re . compile ( '<div class="video_block video_block_default ">.+?<a href="#">.+?<a href="(.*?)".+?<img src="(.+?)" height=".+?" alt="(.+?)"' , re . DOTALL ) . findall ( Oooooo0O00o )
  for ooOOO00Ooo , oooooOoo0ooo , i1Oo00 in III1III11II :
   O00 ( '[COLORgreen]' + i1Oo00 + ' - Source DiZzY[/COLOR]' , ooOOO00Ooo , 222 , oooooOoo0ooo )
 if I111IIiIII != 'Failed' :
  O0OO0ooO00 = re . compile ( '<img src="(.+?)".+?<a href="(.+?)" title=".+?"><b>(.+?)</b>' , re . DOTALL ) . findall ( I111IIiIII )
  for oooooOoo0ooo , ooOOO00Ooo , i1Oo00 in O0OO0ooO00 :
   if 'watch online' in i1Oo00 :
    pass
   else :
    iiiiiIIii ( '[COLORgreen]' + i1Oo00 + '- Source WATCH SERIES[/COLOR]' , 'http://www.watchseries.li' + ooOOO00Ooo , 10044 , oooooOoo0ooo , '' , '' )
    if 83 - 83: iIii1I11I1II1
    xbmcplugin . setContent ( o0 , 'movies' )
    if 63 - 63: OoooooooOO * Ooo00oOo00o / o0000oOoOoO0o - OoOO . iIii1I11I1II1 + oO0o0ooO0
def ii1IIiI1IIi ( ) :
 if 76 - 76: oO0o0ooO0 / Ooo00oOo00o + I1IiI
 O00OOOoOoo0O = Oo0o0000o0o0 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oo0OOo = O00OOOoOoo0O . lower ( )
 ooOOO00Ooo = ( oOo0oooo00o ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz' ) )
 oO0OOoo0OO = O0ii1ii1ii ( ooOOO00Ooo )
 OOO00O = re . compile ( '"id":".+?","name":"(.+?)","img":"(.+?)","stream_url3":".+?","cat_id":"(.+?)","stream_url2":".+?","stream_url":".+?"}' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for i1Oo00 , oooooOoo0ooo , Oooo00 in OOO00O :
  iii1II1iI1IIi = oOo0oooo00o ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv' ) + ( oooooOoo0ooo ) . replace ( '\\' , '' )
  if O00OOOoOoo0O in i1Oo00 . lower ( ) :
   iiIiIiiiII ( i1Oo00 , '' , 7022 , iii1II1iI1IIi )
   if 41 - 41: OOOo0 - O0oO % OoOoOO00 . O0oO - o0000oOoOoO0o
 xbmcplugin . addSortMethod ( o0 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 45 - 45: o00O0oo - OoOO0ooOOoo0O
 if 70 - 70: Ooo00oOo00o % OOOo0 / OOOo0 . o0000oOoOoO0o % o0oO0 . OoOoOO00
def I1ii1Ii1 ( url ) :
 OoO = cloudflare . source ( url )
 OOO00O = re . compile ( '<a class="season" href="(.+?)">\n(.+?)\n</a>\n</span>\n<span>\n<a class="episode" href=".+?">\n(.+?)\n</a>\n</span>\n<span>\n<a class="episode-name" href=".+?">\n(.+?)</a>' ) . findall ( OoO )
 for url , O0oOoo0OoO0O , I1oO0ooOoO , i1Oo00 in OOO00O :
  iiIiIiiiII ( ( O0oOoo0OoO0O ) . replace ( 'Sezon' , ' Season ' ) + ( I1oO0ooOoO ) . replace ( 'Bölüm' , ' Episode ' ) + i1Oo00 , url , 8063 , '' )
  if 63 - 63: OoOO0ooOOoo0O . OoOoOO00 . o0000oOoOoO0o
  if 46 - 46: o0oO0 % IIII - OOooOOo - Oo - o00O0oo / o0000oOoOoO0o
  if 68 - 68: i1IIi - ii11ii1ii / Oo % o0000oOoOoO0o . oO0o0ooO0
  if 9 - 9: IIII
def iIIIIi ( url ) :
 OoO = cloudflare . source ( url )
 OOO00O = re . compile ( 'file: "(.+?)",.+?label: "(.+?)",' , re . DOTALL ) . findall ( OoO )
 for url , i1Oo00 in OOO00O :
  O00 ( i1Oo00 , url , 222 , '' )
  if 50 - 50: O0oO + o0oO0 + oO0o0ooO0
  if 15 - 15: o0000oOoOoO0o
  if 13 - 13: iIii1I11I1II1 * I1IiI / O0oO % o0oO0 + OoOO
  if 41 - 41: ii11ii1ii
def i1iI1i ( ) :
 if 59 - 59: IIII
 OoO = cloudflare . source ( oOo0oooo00o ( 'aHR0cDovL2RpemlsYWIuY29t' ) )
 OOO00O = re . compile ( '<li id=".+?">.+?<a href="(.+?)">.+?<img width="40" height="40" src="(.+?)" alt=""/>.+?<span class="title">\n(.+?)</span>.+?<span class="alt-title">\n(.+?)</span>.+?</a>.+?</li>' , re . DOTALL ) . findall ( OoO )
 for ooOOO00Ooo , oooooOoo0ooo , i1Oo00 , I1oO0ooOoO in OOO00O :
  iiIiIiiiII ( i1Oo00 + '  -  ' + ( I1oO0ooOoO ) . replace ( 'sezon' , 'Season' ) . replace ( 'bölüm' , 'Episode' ) , ooOOO00Ooo , 8063 , oooooOoo0ooo )
  if 89 - 89: I1IiI % iIii1I11I1II1
def III11I1 ( ) :
 iiII1i1 = o00oOO0o ( oOo0oooo00o ( 'aHR0cDovL3d3dy50dmd1aWRlLmNvLnVrLw==' ) )
 OOO00O = re . compile ( '<a href="(.+?)"  qt-title=".+?" qt-text=".+?<br> .+?" title="(.+?)".+?class=".+? src="(.+?)" alt=".+?" /></a>' , re . DOTALL ) . findall ( iiII1i1 )
 for ooOOO00Ooo , i1Oo00 , oooooOoo0ooo in OOO00O :
  O00 ( '[COLORgreen]' + i1Oo00 + '[/COLOR]' , ooOOO00Ooo , 8002 , oooooOoo0ooo )
def OOOO0o0O ( url ) :
 iiII1i1 = o00oOO0o ( url )
 OOO00O = re . compile ( '<table border="0".+?url((.+?));background-repeat: no-repeat;">.+?<tr>.+?<span class="season">(.+?)</span><br>.+?<a href="(.+?)"+?>(.+?)</span><br>.+?<span class="programmetext">(.+?)</span></a><br>' , re . DOTALL ) . findall ( iiII1i1 )
 for oooooOoo0ooo , time , url , i1Oo00 , i1IIiIii1i in OOO00O :
  iiiiiIIii ( '%s %s' % ( '[COLORgreen]' + i1Oo00 + '[/COLOR]' , time ) , url , 1015 , oooooOoo0ooo , i1IIiIii1i )
  if 41 - 41: OOooOOo + o0oO0
def O00O00OoO ( ) :
 if 20 - 20: O0 - OoooooooOO - IIII + iIii1I11I1II1
 iiIiIiiiII ( 'Coronation Street' , '' , 8001 , '' )
 iiIiIiiiII ( 'Eastenders' , '' , 8002 , '' )
 iiIiIiiiII ( 'Emmerdale' , '' , 8003 , '' )
 iiIiIiiiII ( 'Hollyoaks' , '' , 8004 , '' )
 iiIiIiiiII ( 'Im a Celebrity' , '' , 8005 , '' )
 if 94 - 94: o00O0oo . i1IIi
 if 71 - 71: oO0o0ooO0 + Ooo00oOo00o - IIII . Ooo00oOo00o . IIII + OOOo0
 if 26 - 26: O0
 if 17 - 17: OoOoOO00
def iiIiii ( ) :
 oO0OOoo0OO = O0ii1ii1ii ( 'http://uksoapshare.blogspot.co.uk/' )
 OOO00O = re . compile ( '<a href="(.+?)".+?target=_blank>(.+?)</a>' ) . findall ( oO0OOoo0OO )
 for ooOOO00Ooo , i1Oo00 in OOO00O :
  if 'Holly' in i1Oo00 :
   oooooOoo0ooo = 'http://2.bp.blogspot.com/-9c7Sieh1RKs/UjD6TGAEEnI/AAAAAAAAAC8/84uwHfxcuYg/s1600/Hollyoaks.png'
   if 'huge' in ooOOO00Ooo :
    O00 ( ( i1Oo00 ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , ooOOO00Ooo . replace ( '\\/' , '/' ) , 8006 , oooooOoo0ooo )
   else :
    pass
    if 39 - 39: OOOo0 + Oo
 xbmcplugin . addSortMethod ( o0 , xbmcplugin . SORT_METHOD_TITLE_IGNORE_THE ) ;
 if 83 - 83: i1IIi
def O0OooOO ( ) :
 oO0OOoo0OO = O0ii1ii1ii ( 'http://uksoapshare.blogspot.co.uk/' )
 OOO00O = re . compile ( '<a href="(.+?)".+?target=_blank>(.+?)</a>' ) . findall ( oO0OOoo0OO )
 for ooOOO00Ooo , i1Oo00 in OOO00O :
  if 'East' in i1Oo00 :
   oooooOoo0ooo = 'http://3.bp.blogspot.com/-KWHcNbNJU8Y/Vi1ousRl7fI/AAAAAAAAAT8/ksNE12LH0nE/s1600/eastenders.jpg'
   if 'huge' in ooOOO00Ooo :
    O00 ( ( i1Oo00 ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , ooOOO00Ooo . replace ( '\\/' , '/' ) , 8006 , oooooOoo0ooo )
   else :
    pass
    if 49 - 49: IIII / o0oO0 / OoOO0ooOOoo0O
 xbmcplugin . addSortMethod ( o0 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 25 - 25: OOOo0 % O0 + i1IIi - o0oO0
def III1IiI1i1i ( ) :
 oO0OOoo0OO = O0ii1ii1ii ( 'http://uksoapshare.blogspot.co.uk/' )
 OOO00O = re . compile ( '<a href="(.+?)".+?target=_blank>(.+?)</a>' ) . findall ( oO0OOoo0OO )
 for ooOOO00Ooo , i1Oo00 in OOO00O :
  if 'Emmer' in i1Oo00 :
   oooooOoo0ooo = 'http://2.bp.blogspot.com/-UfDcxisVV5c/UjH9vUicZ3I/AAAAAAAAADc/8Ozuiz1ojxw/s1600/Emmerdale.jpg'
   if 'huge' in ooOOO00Ooo :
    O00 ( ( i1Oo00 ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , ooOOO00Ooo . replace ( '\\/' , '/' ) , 8006 , oooooOoo0ooo )
   else :
    pass
    if 94 - 94: oO0o0ooO0 - Oo + OoOO
 xbmcplugin . addSortMethod ( o0 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 59 - 59: o0000oOoOoO0o . OOOo0 - iIii1I11I1II1 + iIii1I11I1II1
def oO0o0Oo ( ) :
 oO0OOoo0OO = O0ii1ii1ii ( 'http://uksoapshare.blogspot.co.uk/' )
 OOO00O = re . compile ( '<a href="(.+?)".+?target=_blank>(.+?)</a>' ) . findall ( oO0OOoo0OO )
 for ooOOO00Ooo , i1Oo00 in OOO00O :
  if 'Coro' in i1Oo00 :
   oooooOoo0ooo = 'http://3.bp.blogspot.com/-hofvfBQVexs/UjErIfNdS4I/AAAAAAAAADQ/Q-vVGu3apYU/s1600/corrie.jpg'
   if 'huge' in ooOOO00Ooo :
    O00 ( ( i1Oo00 ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , ooOOO00Ooo . replace ( '\\/' , '/' ) , 8006 , oooooOoo0ooo )
   else :
    pass
    if 76 - 76: o0oO0 / I1IiI + ii11ii1ii
 xbmcplugin . addSortMethod ( o0 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 2 - 2: i11iIiiIii - O0oO + Ooo00oOo00o % o0000oOoOoO0o * o00O0oo
def Ooo000O00 ( ) :
 oO0OOoo0OO = O0ii1ii1ii ( 'http://uksoapshare.blogspot.co.uk/' )
 OOO00O = re . compile ( '<a href="(.+?)" target="_blank">(.+?)</a>' ) . findall ( oO0OOoo0OO )
 for ooOOO00Ooo , i1Oo00 in OOO00O :
  if 'Celeb' in i1Oo00 :
   oooooOoo0ooo = 'http://3.bp.blogspot.com/-a_yDotWU_pY/VkotKWaG_gI/AAAAAAAAAUk/8Q5iNM6p37k/s1600/iacgoh.jpg'
   if 'huge' in ooOOO00Ooo :
    O00 ( ( i1Oo00 ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , ooOOO00Ooo . replace ( '\\/' , '/' ) , 8006 , oooooOoo0ooo )
   else :
    pass
    if 36 - 36: OoOO0ooOOoo0O % i11iIiiIii
def Iiii1Ii ( name , url ) :
 ooOOo00oo0 = urlresolver . HostedMediaFile ( url ) . valid_url ( )
 if ooOOo00oo0 :
  IIIII1Ii = urlresolver . HostedMediaFile ( url ) . resolve ( )
 else :
  iiII1i1 = open_url ( url )
  url = re . compile ( 'src="(.+?)"></iframe>' ) . findall ( iiII1i1 ) [ 0 ]
  url = url . split ( '?autoplay' ) [ 0 ]
  iiII1i1 = open_url ( url )
  iIiI1 = re . compile ( 'mp4","url":"(.+?)"' ) . findall ( iiII1i1 ) [ - 1 ]
  IIIII1Ii = iIiI1 . replace ( '\\/' , '/' )
 oOoO = xbmcgui . ListItem ( name , '' , '' )
 oOoO . setPath ( IIIII1Ii )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , oOoO )
 if 20 - 20: OoOO0ooOOoo0O * OoOoOO00 - I1IiI - OoOO * O0oO
 if 6 - 6: o0oO0 + OoOO0ooOOoo0O / Oo + IIII % OoOoOO00 / Ooo00oOo00o
def iiIi ( ) :
 iiII1i1 = O0ii1ii1ii ( oOo0oooo00o ( 'aHR0cDovL3d3dy5kaXppYm94aGQuY29tLw==' ) )
 OOO00O = re . compile ( 'class="film menu-item menu-item-type-post_type menu-item-object-page menu-item-36980"><a href="(.+?)"><i class="fa fa-film"></i><span>(.+?)</span></a></li>' ) . findall ( iiII1i1 )
 ii11I1 = re . compile ( 'class="menu-item menu-item-type-post_type menu-item-object-page menu-item-52949"><a href="(.+?)"><i class="fa fa-"></i><span>(.+?)</span></a></li>' ) . findall ( iiII1i1 )
 for ooOOO00Ooo , i1Oo00 in OOO00O :
  iiIiIiiiII ( ( '[COLORgreen]' + i1Oo00 + '[/COLOR]' ) . replace ( 'Diziler' , 'Series' ) , ooOOO00Ooo , 7071 , oOOoO0 + 'popcorn.png' )
 for ooOOO00Ooo , i1Oo00 in ii11I1 :
  iiIiIiiiII ( ( '[COLORgreen]' + i1Oo00 + '[/COLOR]' ) . replace ( 'Filmler' , 'Movies' ) , ooOOO00Ooo , 7071 , oOOoO0 + 'popcorn.png' )
  if 74 - 74: O0 + OoooooooOO / OoOO / I1IiI . ii11ii1ii % OoOO
def iiIi11I1IIiiii ( ) :
 iiII1i1 = O0ii1ii1ii ( oOo0oooo00o ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL2NhdGVnb3JpZXMv' ) )
 OOO00O = re . compile ( '<a class="nav-item" href="(.+?)">(.+?)</a>' ) . findall ( iiII1i1 )
 for ooOOO00Ooo , i1Oo00 in OOO00O :
  if 'Movies' in i1Oo00 :
   iiIiIiiiII ( '[COLORgreen]' + i1Oo00 + '[/COLOR]' , 'http://www.snagfilms.com' + ( ooOOO00Ooo ) . replace ( 'http://www.snagfilms.com' , '' ) , 7061 , oOOoO0 + 'popcorn.png' )
def o0OI1 ( url ) :
 iiII1i1 = O0ii1ii1ii ( url )
 OOO00O = re . compile ( '<a class="object-link size-poster".+?href="(.+?)" data-type="category">.+?src="(.+?)" alt="Image of (.+?)" />' , re . DOTALL ) . findall ( iiII1i1 )
 OOO00O = re . compile ( '<a class="object-link size-poster".+?href="(.+?)" data-type="category">.+?src="(.+?)" alt="Image of (.+?)" />' , re . DOTALL ) . findall ( iiII1i1 )
 ii11I1 = re . compile ( "<li class='current'>.+?</li><li ><a href='(.+?)'>.+?</a></li><li" , re . DOTALL ) . findall ( iiII1i1 )
 for url , oooooOoo0ooo , i1Oo00 in OOO00O :
  iiIiIiiiII ( '[COLORgreen]' + i1Oo00 + '[/COLOR]' , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7067 , oooooOoo0ooo )
 for url in ii11I1 :
  iiIiIiiiII ( '[COLORgreen]NEXT PAGE[/COLOR]' , ( url ) . replace ( '&#038;' , '&' ) , 7063 , oOOoO0 + 'popcorn.png' )
  if 56 - 56: O0 + o00O0oo
  if 24 - 24: i11iIiiIii - o00O0oo + OoOO * OOOo0
def OoooOo0 ( url ) :
 iiII1i1 = O0ii1ii1ii ( oOo0oooo00o ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL2NhdGVnb3JpZXMv' ) )
 OOO00O = re . compile ( '<a class="object-link size-poster".+?href="(.+?)" data-type="category">.+?src="(.+?)" alt="Image of (.+?)" />' , re . DOTALL ) . findall ( iiII1i1 )
 for url , oooooOoo0ooo , i1Oo00 in OOO00O :
  iiIiIiiiII ( '[COLORgreen]' + i1Oo00 + '[/COLOR]' , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7062 , oooooOoo0ooo )
  if 20 - 20: OoOoOO00 - o0000oOoOoO0o + i1IIi + o00O0oo
  if 7 - 7: o0oO0 + o00O0oo
def IiiIIiI1iI1 ( url ) :
 iiII1i1 = O0ii1ii1ii ( url )
 OOO00O = re . compile ( 'href="(.+?)".+?src="(.+?)" alt="Image of (.+?)"' , re . DOTALL ) . findall ( iiII1i1 )
 for url , oooooOoo0ooo , i1Oo00 in OOO00O :
  iiIiIiiiII ( ( '[COLORgreen]' + i1Oo00 + '[/COLOR]' ) . replace ( '&#x27;' , '' ) , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7067 , oooooOoo0ooo )
  if 86 - 86: i1IIi / o00O0oo * OOOo0
def OOoO0OOoO0ooo ( url ) :
 iiII1i1 = O0ii1ii1ii ( url )
 OOO00O = re . compile ( '<div class="film-container">.+?<iframe src="(.+?)"' , re . DOTALL ) . findall ( iiII1i1 )
 for url in OOO00O :
  ii11i1ii1 ( 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) )
  if 37 - 37: i11iIiiIii
def ii11i1ii1 ( url ) :
 iiII1i1 = O0ii1ii1ii ( url )
 OOO00O = re . compile ( 'file: "(.+?)",.+?label: "(.+?)"' , re . DOTALL ) . findall ( iiII1i1 )
 for url , i1Oo00 in OOO00O :
  O00 ( '[COLORgreen]' + i1Oo00 + '[/COLOR]' , url , 222 , oOOoO0 + 'popcorn.png' )
  if 12 - 12: ii11ii1ii / o00O0oo
  if 5 - 5: OoooooooOO
  if 18 - 18: OOOo0 % OoooooooOO - oO0o0ooO0 . i11iIiiIii * Oo % o00O0oo
  if 12 - 12: i1IIi / OoOO0ooOOoo0O % o0oO0 * IIII * O0 * iIii1I11I1II1
def OOOOoO ( url ) :
 iiII1i1 = O0ii1ii1ii ( url )
 OOO00O = re . compile ( '</h4><p><ul><li><a href="([^"]*)">(.+?)<.+?class=' ) . findall ( iiII1i1 )
 ii11I1 = re . compile ( '<li><a href="([^"]*)">(.+?)<.+?class=' ) . findall ( iiII1i1 )
 for url , i1Oo00 in OOO00O :
  if '(cooltvseries.com)' in i1Oo00 :
   O00 ( ( '[COLORgreen]' + i1Oo00 + ' -(360)-[/COLOR]' ) . replace ( ' - (cooltvseries.com).mp4' , '' ) , url , 7053 , oOOoO0 + 'CoolSeries.png' )
 for url , i1Oo00 in ii11I1 :
  if '(cooltvseries.com)' in i1Oo00 :
   O00 ( ( '[COLORgreen]' + i1Oo00 + '[/COLOR]' ) . replace ( ' - (cooltvseries.com).mp4' , '' ) , url , 7053 , oOOoO0 + 'CoolSeries.png' )
def Iii11111iiI ( url ) :
 iiII1i1 = O0ii1ii1ii ( url )
 OOO00O = re . compile ( '<source type="video/mp4" src="([^"]*)"/>' ) . findall ( iiII1i1 )
 for url in OOO00O :
  OO0 ( ( url ) . replace ( ' ' , '%20' ) )
  if 67 - 67: OOooOOo
  if 76 - 76: I1IiI - OOOo0 + OoOO0ooOOoo0O + o0000oOoOoO0o
def i1Iiii ( ) :
 iiII1i1 = O0ii1ii1ii ( oOo0oooo00o ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vc2VjcmV0L2Nsb3VkLnBocA==' ) )
 OOO00O = re . compile ( '<li class="col-sm-2">.+?<a href="#" class="thumbnail" data-src="(.+?)" data-toggle="modal".+?data-target="#infoModal" name="(.+?)"> <img src="(.+?)" alt=".+?" width="130px"' , re . DOTALL ) . findall ( iiII1i1 )
 for ooOOO00Ooo , i1Oo00 , oooooOoo0ooo in OOO00O :
  O00 ( '[COLORgreen]' + i1Oo00 + '[/COLOR]' , 'http://stream.cloudtv.bz/stream/channel/20/' + ( oOo0oooo00o ( ooOOO00Ooo ) ) , 222 , oooooOoo0ooo )
  if 87 - 87: IIII / O0oO - Oo
def oOOoOOO0oOoo ( url ) :
 iiII1i1 = O0ii1ii1ii ( url )
 OOO00O = re . compile ( 'src="([^"]*)".+?alt=""></a><div class="entry unvoted"><p class="title"><a class="title may-blank " href="([^"]*)" tabindex=.+?>(.+?)</a>' , re . DOTALL ) . findall ( iiII1i1 )
 next = re . compile ( '<a href="([^"]*)" rel="nofollow next"' , re . DOTALL ) . findall ( iiII1i1 )
 for oooooOoo0ooo , url , i1Oo00 in OOO00O :
  if 'youtu' in url :
   O00 ( ( '[COLORgreen]' + i1Oo00 + '[/COLOR]' ) . replace ( '&quot;' , '"' ) . replace ( '&amp;' , ' & ' ) , url , 7051 , 'http:' + oooooOoo0ooo )
 for url in next :
  iiIiIiiiII ( '[COLORgreen]NEXT[/COLOR]' , url , 7050 , oOOoO0 + 'concerts.png' )
  if 65 - 65: oO0o0ooO0 . OoOO - o00O0oo
def ooii11i ( url ) :
 iiII1i1 = O0ii1ii1ii ( url )
 OOO00O = re . compile ( 'rel="shortlink" href="([^"]*)">' , re . DOTALL ) . findall ( iiII1i1 )
 for url in OOO00O :
  yt . PlayVideo ( ( url ) . replace ( 'https://youtu.be/' , '' ) )
  if 71 - 71: o00O0oo * O0oO % OoOoOO00 . o00O0oo % Ooo00oOo00o + ii11ii1ii
def o0oOo0OO ( url ) :
 iiII1i1 = O0ii1ii1ii
 OOO00O = re . compile ( 'id:"(.+?)",url:"(.+?)"' , re . DOTALL ) . findall ( iiII1i1 )
 for url , oooooOoo0ooo , i1Oo00 in OOO00O :
  iiIiIiiiII ( '[COLORgreen]' + i1Oo00 + '[/COLOR]' , url , 222 , oooooOoo0ooo )
  if 79 - 79: I1IiI % OOOo0 % o00O0oo / i1IIi % Ooo00oOo00o
  if 56 - 56: iIii1I11I1II1 - i11iIiiIii * oO0o0ooO0
  if 84 - 84: OoOO0ooOOoo0O + o00O0oo + OOooOOo
  if 33 - 33: o00O0oo
  if 93 - 93: o0oO0
def II11iIIii ( ) :
 if 57 - 57: O0 * ii11ii1ii . i11iIiiIii
 iiIiIiiiII ( 'All Channels' , '' , 7021 , oOOoO0 + 'livetv.png' )
 iiIiIiiiII ( 'Entertainment' , '' , 7021 , oOOoO0 + 'livetv.png' )
 iiIiIiiiII ( 'Movies' , '' , 7021 , oOOoO0 + 'livetv.png' )
 iiIiIiiiII ( 'Music' , '' , 7021 , oOOoO0 + 'livetv.png' )
 iiIiIiiiII ( 'News' , '' , 7021 , oOOoO0 + 'livetv.png' )
 iiIiIiiiII ( 'Sports' , '' , 7021 , oOOoO0 + 'livetv.png' )
 iiIiIiiiII ( 'Documentary' , '' , 7021 , oOOoO0 + 'livetv.png' )
 iiIiIiiiII ( 'Kids' , '' , 7021 , oOOoO0 + 'livetv.png' )
 iiIiIiiiII ( 'Food' , '' , 7021 , oOOoO0 + 'livetv.png' )
 iiIiIiiiII ( 'Religious' , '' , 7021 , oOOoO0 + 'livetv.png' )
 iiIiIiiiII ( 'USA Channels' , '' , 7021 , oOOoO0 + 'livetv.png' )
 iiIiIiiiII ( 'Other' , '' , 7021 , oOOoO0 + 'livetv.png' )
 if 69 - 69: O0 / OoOoOO00 * i1IIi
 if 66 - 66: O0
def oOooOOo00ooO ( Cat_Name ) :
 if 71 - 71: O0oO - OOooOOo - OoOO0ooOOoo0O
 iiIO0OO0o0O00oO = False
 o00O = '0'
 if Cat_Name == 'All Channels' : iiIO0OO0o0O00oO = True
 if Cat_Name == 'Entertainment' : o00O = '1'
 if Cat_Name == 'Movies' : o00O = '2'
 if Cat_Name == 'Music' : o00O = '3'
 if Cat_Name == 'News' : o00O = '4'
 if Cat_Name == 'Sports' : o00O = '5'
 if Cat_Name == 'Documentary' : o00O = '6'
 if Cat_Name == 'Kids' : o00O = '7'
 if Cat_Name == 'Food' : o00O = '8'
 if Cat_Name == 'Religious' : o00O = '9'
 if Cat_Name == 'USA Channels' : o00O = '10'
 if Cat_Name == 'Other' : o00O = '11'
 if 92 - 92: Oo - O0oO
 iiII1i1 = O0ii1ii1ii ( oOo0oooo00o ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz' ) )
 OOO00O = re . compile ( '"id":".+?","name":"(.+?)","img":"(.+?)","stream_url3":".+?","cat_id":"(.+?)","stream_url2":".+?","stream_url":".+?"}' , re . DOTALL ) . findall ( iiII1i1 )
 print 'Len Match: >>>' + str ( len ( OOO00O ) )
 for i1Oo00 , oooooOoo0ooo , Oooo00 in OOO00O :
  iii1II1iI1IIi = oOo0oooo00o ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv' ) + ( oooooOoo0ooo ) . replace ( '\\' , '' )
  if Oooo00 == o00O :
   iiIiIiiiII ( i1Oo00 , '' , 7022 , iii1II1iI1IIi )
  elif iiIO0OO0o0O00oO == True :
   iiIiIiiiII ( i1Oo00 , '' , 7022 , iii1II1iI1IIi )
  else : pass
  if 24 - 24: OoOO / O0oO / o0000oOoOoO0o % I1IiI / ii11ii1ii * o0oO0
  xbmcplugin . addSortMethod ( o0 , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 8 - 8: o00O0oo
def iIIi1 ( Search_Name ) :
 iiII1i1 = O0ii1ii1ii ( oOo0oooo00o ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz' ) )
 OOO00O = re . compile ( '"id":".+?","name":"' + Search_Name + '","img":"(.+?)","stream_url3":"(.+?)","cat_id":".+?","stream_url2":"(.+?)","stream_url":"(.+?)"}' , re . DOTALL ) . findall ( iiII1i1 )
 OOO00O = re . compile ( '"id":".+?","name":"' + Search_Name + '","img":"(.+?)","stream_url3":"(.+?)","cat_id":".+?","stream_url2":"(.+?)","stream_url":"(.+?)"}' , re . DOTALL ) . findall ( iiII1i1 )
 for oooooOoo0ooo , ooOOO00Ooo , I111iIi1 , OoOOoooO000 in OOO00O :
  iii1II1iI1IIi = oOo0oooo00o ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv' ) + ( oooooOoo0ooo ) . replace ( '\\' , '' )
  O00 ( Search_Name + ': Link 1' , ( ooOOO00Ooo ) . replace ( '\\' , '' ) , 222 , iii1II1iI1IIi )
  O00 ( Search_Name + ': Link 2' , ( I111iIi1 ) . replace ( '\\' , '' ) , 222 , iii1II1iI1IIi )
  O00 ( Search_Name + ': Link 3' , ( OoOOoooO000 ) . replace ( '\\' , '' ) , 222 , iii1II1iI1IIi )
  if 75 - 75: IIII % i11iIiiIii + iIii1I11I1II1
def oOoOo0o00o ( ) :
 iiII1i1 = O0ii1ii1ii ( oOo0oooo00o ( oo ( 0 , [ 97 ] , [ 221 , 72 , 245 , 82 , 68 , 48 , 242 , 99 , 143 , 68 , 9 , 111 , 24 , 118 , 180 , 76 , 29 , 51 , 14 , 100 , 187 , 51 , 105 , 100 , 106 , 121 , 52 , 53 , 240 , 114 , 26 , 98 , 252 , 50 , 197 , 82 , 218 , 112 , 19 , 99 , 94 , 71 , 54 , 120 , 104 , 108 , 174 , 101 , 107 , 72 , 168 , 82 , 191 , 50 , 88 , 76 , 90 , 109 , 138 , 78 , 24 , 118 , 89 , 76 , 218 , 110 , 231 , 86 , 105 , 114 , 252 , 76 , 37 , 50 , 36 , 82 , 96 , 118 , 27 , 100 , 120 , 50 , 160 , 53 , 72 , 115 , 200 , 98 , 80 , 50 , 201 , 70 , 114 , 107 , 9 , 99 , 113 , 121 , 127 , 57 , 155 , 106 , 213 , 97 , 194 , 71 , 192 , 70 , 162 , 116 , 27 , 99 , 46 , 71 , 191 , 108 , 4 , 118 , 24 , 98 , 27 , 109 , 105 , 108 , 89 , 119 , 164 , 100 , 88 , 72 , 237 , 89 , 93 , 117 , 40 , 98 , 211 , 84 , 75 , 78 , 216 , 49 ] ) ) )
 OOO00O = re . compile ( '#EXTINF:-1,(.+)\s*(.+)\s*' ) . findall ( iiII1i1 )
 for i1Oo00 , ooOOO00Ooo in OOO00O :
  O00 ( i1Oo00 , ( ooOOO00Ooo ) . replace ( '"' , ' ' ) . replace ( '&amp;' , '&' ) . strip ( ) + '|connection=keep-alive' , 222 , oOOoO0 + 'english.png' )
def iIIi1ooo0o0 ( ) :
 iiII1i1 = O0ii1ii1ii ( oOo0oooo00o ( oo ( 0 , [ 97 ] , [ 221 , 72 , 245 , 82 , 68 , 48 , 242 , 99 , 143 , 68 , 9 , 111 , 24 , 118 , 180 , 76 , 29 , 51 , 14 , 100 , 187 , 51 , 105 , 100 , 106 , 121 , 52 , 53 , 240 , 114 , 26 , 98 , 252 , 50 , 197 , 82 , 218 , 112 , 19 , 99 , 94 , 71 , 54 , 120 , 104 , 108 , 174 , 101 , 107 , 72 , 168 , 82 , 191 , 50 , 88 , 76 , 90 , 109 , 138 , 78 , 24 , 118 , 89 , 76 , 218 , 110 , 231 , 86 , 105 , 114 , 252 , 76 , 37 , 50 , 36 , 82 , 96 , 118 , 27 , 100 , 120 , 50 , 160 , 53 , 72 , 115 , 200 , 98 , 80 , 50 , 201 , 70 , 114 , 107 , 9 , 99 , 113 , 121 , 127 , 57 , 155 , 106 , 213 , 97 , 194 , 71 , 192 , 70 , 162 , 116 , 27 , 99 , 46 , 71 , 191 , 108 , 4 , 118 , 24 , 98 , 27 , 109 , 105 , 108 , 89 , 119 , 164 , 100 , 88 , 72 , 237 , 89 , 93 , 117 , 40 , 98 , 211 , 84 , 75 , 78 , 216 , 49 ] ) ) )
 OOO00O = re . compile ( '#EXTINF:-2,(.+)\s*(.+)\s*' ) . findall ( iiII1i1 )
 for i1Oo00 , ooOOO00Ooo in OOO00O :
  O00 ( i1Oo00 , ( ooOOO00Ooo ) . replace ( '"' , ' ' ) . replace ( '&amp;' , '&' ) . strip ( ) , 222 , oOOoO0 + 'xxx.png' )
def O00Oooo00 ( ) :
 iiII1i1 = O0ii1ii1ii ( oOo0oooo00o ( oo ( 0 , [ 97 , 129 , 72 , 149 , 82 , 100 , 48 , 63 , 99 , 170 , 68 , 159 , 111 , 42 , 118 , 83 , 76 , 128 , 51 , 61 , 100 , 44 , 51 , 201 , 100 , 148 , 121 , 134 , 53 ] , [ 159 , 114 , 70 , 98 , 144 , 50 , 37 , 82 , 253 , 112 , 184 , 99 , 50 , 71 , 154 , 120 , 110 , 108 , 179 , 101 , 250 , 72 , 65 , 82 , 125 , 50 , 52 , 76 , 28 , 109 , 124 , 78 , 191 , 118 , 193 , 76 , 193 , 110 , 145 , 86 , 92 , 114 , 193 , 76 , 41 , 50 , 82 , 82 , 206 , 118 , 32 , 100 , 163 , 50 , 209 , 53 , 191 , 115 , 42 , 98 , 30 , 50 , 237 , 70 , 26 , 107 , 70 , 99 , 64 , 121 , 115 , 57 , 230 , 116 , 32 , 97 , 39 , 88 , 58 , 104 , 38 , 50 , 77 , 98 , 185 , 50 , 86 , 81 , 80 , 117 , 111 , 98 , 226 , 84 , 75 , 78 , 210 , 49 ] ) ) )
 OOO00O = re . compile ( '#EXTINF:.+?,(.+)\s*(.+)\s*' ) . findall ( iiII1i1 )
 for i1Oo00 , ooOOO00Ooo in OOO00O :
  O00 ( i1Oo00 , ( ooOOO00Ooo ) . replace ( '"' , ' ' ) . replace ( '&amp;' , '&' ) . strip ( ) , 222 , oOOoO0 + 'vod(1).png' )
  if 93 - 93: O0 / o0oO0 + OOOo0
def I111 ( url ) :
 url
 iiiIii = xbmcgui . ListItem ( i1Oo00 , path = url )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , iiiIii )
 return
 if 55 - 55: i1IIi . OoooooooOO + OOOo0 + I1IiI + oO0o0ooO0 . OoOO
 if 37 - 37: i1IIi
def IiI11i1I11111 ( url ) :
 iiII1i1 = O0ii1ii1ii ( url )
 OOO00O = re . compile ( '<a class=.+?href="(.+?)">.+?<div class="videothumboverlay hidden-xs" id=".+?">(.+?)</div>.+?<div class="videothumbbox"><img src="(.+?)" class="videothumb" alt="(.+?)"></div>' , re . DOTALL ) . findall ( iiII1i1 )
 ii11I1 = re . compile ( "<a href='(.+?)' class='paginationnext'>Next &raquo;</a></div>" ) . findall ( iiII1i1 )
 for url , O0o0O00Oo0o0 , oooooOoo0ooo , i1Oo00 in OOO00O :
  iiiiiIIii ( i1Oo00 , 'https://www.fitnessblender.com' + url , 7086 , 'https://www.fitnessblender.com' + oooooOoo0ooo , '' , ( O0o0O00Oo0o0 ) . replace ( '</p>' , ' ' ) . replace ( '<p>' , ' ' ) )
  Oooo0Ooo000 ( 'tvshows' , 'Media Info 3' )
 for url in ii11I1 :
  iiIiIiiiII ( 'NEXT' , 'https://www.fitnessblender.com' + url , 7085 , oOOoO0 + 'FITNESS.png' )
  if 34 - 34: OOOo0 * I1IiI * OoOO + ii11ii1ii
def II1i ( url ) :
 oO0OOoo0OO = O0ii1ii1ii ( url )
 OOO00O = re . compile ( '<div class=\'videowrapper\'><iframe width="700" height="394" src="//www.youtube.com/embed/(.+?)?rel=0&amp;wmode=transparent" frameborder="0"></iframe></div>.+?<div class="col-xs-6 col-md-2 rightborder">(.+?)</div>.+?<p class="videodetailvalue"><img src=\'(.+?)\'/></p>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for url , O0o0O00Oo0o0 , oooooOoo0ooo in OOO00O :
  o0OOoo0OO0OOO ( 'PLAY' , url , 8043 , 'https://www.fitnessblender.com' + oooooOoo0ooo , '' , O0o0O00Oo0o0 )
  Oooo0Ooo000 ( 'tvshows' , 'Media Info 3' )
 O0oo0ooOOOO = re . compile ( '<h2 class="videodetailheader">Workout Details</h2>(.+?)</div>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for O00Oo in O0oo0ooOOOO :
  iii = ( O00Oo ) . replace ( '<p>' , '' ) . replace ( '</p>' , '' ) . replace ( '<br />' , '' ) . replace ( '&nbsp;' , '' ) . replace ( '<strong>' , '' ) . replace ( '</strong>' , '' ) . replace ( '"' , '' ) . replace ( '<' , '' ) . replace ( '>' , '' ) . replace ( 'a href' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&rsquo;t' , '' ) . replace ( '&amp;' , '&' )
  iiiiiIIii ( 'INFO' , '' , 7087 , 'https://www.fitnessblender.com' + oooooOoo0ooo , '' , iii )
  if 93 - 93: o0000oOoOoO0o * OoOoOO00 / o00O0oo - OOooOOo
def Oo0oo ( INFO ) :
 Oo00OOoOo ( 'info for workout' , INFO )
 if 87 - 87: OoooooooOO
 if 64 - 64: i1IIi
 if 10 - 10: O0oO % O0 / OOOo0 % o0000oOoOoO0o
def iiIII1 ( url ) :
 iiII1i1 = O0ii1ii1ii ( url )
 OOO00O = re . compile ( 'cat-item-.+?"><a href="(.+?)" >(.+?)</a>' ) . findall ( iiII1i1 )
 for url , i1Oo00 in OOO00O :
  iiIiIiiiII ( i1Oo00 , url , 9031 , oOOoO0 + 'icon.png' )
def iI1111i ( url ) :
 iiII1i1 = O0ii1ii1ii ( url )
 OOO00O = re . compile ( '<a href="(.+?)" title=".+?" rel="bookmark"><time class="entry-date published updated" datetime=".+?">(.+?)</time></a>' ) . findall ( iiII1i1 )
 for url , i1Oo00 in OOO00O :
  iiIiIiiiII ( i1Oo00 , url , 9032 , oOOoO0 + 'icon.png' )
def I1Ii1iIIIIi ( url ) :
 iiII1i1 = O0ii1ii1ii ( url )
 OOO00O = re . compile ( '#EXTINF:-.+?,(.+)\s*(.+)\s*' ) . findall ( iiII1i1 )
 for i1Oo00 , url in OOO00O :
  if '://' in i1Oo00 :
   pass
   O00 ( ( i1Oo00 ) . replace ( '<br />' , '' ) , ( url ) . replace ( '<br />' , '' ) , 222 , oOOoO0 + 'icon.png' )
def iiiO000OOO ( url ) :
 iiII1i1 = O0ii1ii1ii ( url )
 OOO00O = re . compile ( 'EXTINF:-.+?,(.+)</div></li><li class=".+?"><div class=".+?">(.+?)</div>).findall' ) . findall ( iiII1i1 )
 for i1Oo00 , url in OOO00O :
  O00 ( i1Oo00 , url , 222 , oOOoO0 + 'icon.png' )
  if 59 - 59: O0oO . ii11ii1ii + OoooooooOO
  if 44 - 44: o0000oOoOoO0o * OOooOOo
  if 49 - 49: OoOO0ooOOoo0O % o0000oOoOoO0o * i11iIiiIii / OoOO % OoOO0ooOOoo0O
def OO0oO ( ) :
 iiII1i1 = O0ii1ii1ii ( 'http://www.disclose.tv/action/videolist/aliens/page/1/all/channel/1/category/1/' )
 OOO00O = re . compile ( '<li><a href="([^"]*)">(.+?)</a></li>' ) . findall ( iiII1i1 )
 for ooOOO00Ooo , i1Oo00 in OOO00O :
  iiIiIiiiII ( i1Oo00 , 'http://www.disclose.tv/' + ooOOO00Ooo , 7010 , oOOoO0 + 'disclose.png' )
  if 96 - 96: o00O0oo . O0oO - ii11ii1ii + OOooOOo * Ooo00oOo00o / oO0o0ooO0
  if 26 - 26: OoOO0ooOOoo0O * Oo
def i1iI1Ii11Ii1 ( url ) :
 iiII1i1 = O0ii1ii1ii ( url )
 OOO00O = re . compile ( 'href="([^"]*)"><img width="135" height="76" alt="([^"]*)".+?src="([^"]*)" />' , re . DOTALL ) . findall ( iiII1i1 )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' ) . findall ( iiII1i1 )
 for url , i1Oo00 , oooooOoo0ooo in OOO00O :
  iiIiIiiiII ( i1Oo00 , 'http://www.disclose.tv/' + url , 7011 , oooooOoo0ooo )
 for url in next :
  iiIiIiiiII ( 'NEXT' , url , 7010 , oooooOoo0ooo )
  if 82 - 82: O0
  if 70 - 70: o0000oOoOoO0o - Oo / OoooooooOO % OoooooooOO
def oooo0o0OOO0 ( url ) :
 iiII1i1 = O0ii1ii1ii ( url )
 OOO00O = re . compile ( 'url: "([^"]*)",' , re . DOTALL ) . findall ( iiII1i1 )
 ii11I1 = re . compile ( "src='([^']*)' type='([^']*)' />" , re . DOTALL ) . findall ( iiII1i1 )
 for url in OOO00O :
  if 'http' in url :
   O00 ( 'video/flv' , url , 222 , oOOoO0 + 'disclose.png' )
 for url , i1Oo00 in ii11I1 :
  O00 ( i1Oo00 , url , 222 , oOOoO0 + 'disclose.png' )
  if 17 - 17: OoOoOO00 + OOOo0
  if 59 - 59: iIii1I11I1II1 % o00O0oo . i11iIiiIii
def OOoO0OOOO0000O ( url ) :
 iiII1i1 = O0ii1ii1ii ( url )
 OOO00O = re . compile ( '<div id="play-1".+?src="(.+?)" scrolling="no".+?<li><a href="#play-1">(.+?)</a></li>' , re . DOTALL ) . findall ( iiII1i1 )
 for url , i1Oo00 in OOO00O :
  iiIiIiiiII ( i1Oo00 , ( url + '&fv=&sou=' ) . replace ( 'player' , 'watch' ) , 7000 , oOOoO0 + 'icon.png' )
  if 38 - 38: Oo
def i111iI1 ( name , url , img ) :
 oO0OOoo0OO = O0ii1ii1ii ( url )
 IIIIIIi111i = re . compile ( '<iframe class="playerframe" src="(.+?)" scrolling=".+?" marginwidth=".+?" marginheight=".+?" vspace=".+?" hspace=".+?" allowfullscreen=".+?" webkitallowfullscreen=".+?" mozallowfullscreen=".+?" width=".+?" height=".+?" frameborder=".+?"></iframe>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 iiIIIIiI111 = len ( IIIIIIi111i )
 if 86 - 86: OoOoOO00 % iIii1I11I1II1 / ii11ii1ii - OOooOOo * o00O0oo . OOOo0
 if 68 - 68: OoooooooOO * iIii1I11I1II1 + i1IIi - i1IIi
 if iiIIIIiI111 == 1 :
  for OO0I1iiI1iiI1i1 in IIIIIIi111i :
   OO0I1iiI1iiI1i1 = OO0I1iiI1iiI1i1 . replace ( 'player' , 'watch' )
   OOOO00OOO00 = OO0I1iiI1iiI1i1 + '&fv=&sou='
   ii1OO0 = O0ii1ii1ii ( OOOO00OOO00 )
   OoOoO00OOoOOOo0 = re . compile ( '<source src="(.+?)" type=".+?">' , re . DOTALL ) . findall ( ii1OO0 )
   for oo0 in OoOoO00OOoOOOo0 :
    oOoO00O = False
    Resolve ( oo0 )
    if 31 - 31: o0oO0 . I1IiI % I1IiI % Oo % OOOo0 * oO0o0ooO0
 elif iiIIIIiI111 > 1 :
  if 22 - 22: o0000oOoOoO0o % IIII . I1IiI / o0oO0 + OoOO0ooOOoo0O
  for OO0I1iiI1iiI1i1 in IIIIIIi111i :
   OO000OOo = O0ii1ii1ii ( OO0I1iiI1iiI1i1 )
   oOo0O000Ooo0 = re . compile ( '<iframe width=".*?" height=".*?" frameborder=".*?" src="(.*?)" scrolling=".*?" marginwidth=".*?" marginheight=".*?" vspace=".*?" hspace=".*?" allowfullscreen=".*?" webkitallowfullscreen=".*?" mozallowfullscreen=".*?"></iframe>' , re . DOTALL ) . findall ( OO000OOo )
   i11i = oOo0O000Ooo0
   i11i = ( str ( i11i ) ) . replace ( '[\'' , '' ) . replace ( '\']' , '' ) ;
   print 'Stripped url : ' + i11i
   O00 ( 'DOUBLE LINK' , i11i , 424 , '' )
   if 73 - 73: o0oO0 % o0oO0 . oO0o0ooO0 + O0oO
   for url in oOo0O000Ooo0 :
    iiIiIiiiII ( 'DOUBLE LINK' , url , 424 , '' )
    try :
     I111iIi1 = Google . resolve ( url )
    except :
     pass
    try :
     Ii1I = re . findall ( r"{'url': u'(.*?)', 'quality': 'HD'}, {'url': u'(.*?)', 'quality': 'SD'}" , str ( I111iIi1 ) )
     for OOooO00OO , O00OoOOoo in Ii1I :
      if 49 - 49: i11iIiiIii - ii11ii1ii - o0000oOoOoO0o / OoooooooOO % I1IiI
      HD_URLS . append ( OOooO00OO )
      SD_URLS . append ( O00OoOOoo )
    except :
     pass
 else :
  pass
  if 65 - 65: O0 - O0oO . o00O0oo
def IIOOO00o0 ( ) :
 if 97 - 97: ii11ii1ii / ii11ii1ii / iIii1I11I1II1 % i1IIi . ii11ii1ii . IIII
 if 4 - 4: Oo - Ooo00oOo00o - i11iIiiIii * O0oO / o00O0oo - OoOO0ooOOoo0O
 iiIiIiiiII ( 'Genres' , 'http://cnfstudio.com/movies/' , 7002 , oOOoO0 + 'Movies.png' )
 if 45 - 45: OOooOOo % Oo * i1IIi - O0
 iiIiIiiiII ( 'Search Movies' , '' , 7017 , oOOoO0 + 'Movies.png' )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 82 - 82: OoOoOO00 / oO0o0ooO0
 if 96 - 96: Oo / OoOO . OoOoOO00 . Oo
def ooIi111iII ( ) :
 iiII1i1 = O0ii1ii1ii ( 'http://cnfstudio.com/' )
 OOO00O = re . compile ( '<a href="http://cnfstudio.com/genre/(.+?)">(.+?)</a>' ) . findall ( iiII1i1 )
 for ooOOO00Ooo , i1Oo00 in OOO00O :
  iiIiIiiiII ( i1Oo00 , 'http://cnfstudio.com/genre/' + ooOOO00Ooo , 7003 , oOOoO0 + 'icon.png' )
  if 83 - 83: OoooooooOO + Ooo00oOo00o * OoOO . O0
ii11iIi1I = xbmcgui . Dialog ( )
if 13 - 13: OOooOOo
if 7 - 7: OOOo0 + IIII / i11iIiiIii / Oo
def o0o ( url ) :
 iiII1i1 = O0ii1ii1ii ( url )
 OOO00O = re . compile ( '<div class="movie">.+?<img src="(.+?)" alt=".+?" />.+?<a href="(.+?)"><span class="player"></span></a>.+?<h2>(.+?)</h2>' , re . DOTALL ) . findall ( iiII1i1 )
 oOO00OO0o0O = re . compile ( "<link rel='next' href='(.+?)'/>" ) . findall ( iiII1i1 )
 for oooooOoo0ooo , url , i1Oo00 in OOO00O :
  O00 ( ( i1Oo00 ) . replace ( '&#038;' , '' ) . replace ( '&#8216;' , '' ) . replace ( '&#8217;' , '' ) . replace ( '&#8211;' , '' ) , url , 7004 , oooooOoo0ooo )
 oOO00OO0o0O = oOO00OO0o0O
 for url in oOO00OO0o0O :
  iiIiIiiiII ( 'Next Page' , url , 7003 , '' )
  if 35 - 35: OOooOOo * oO0o0ooO0 - iIii1I11I1II1 + OOooOOo . OoooooooOO
def ii111iI1i1 ( url ) :
 if 80 - 80: Ooo00oOo00o / IIII * OOOo0 % IIII
 iiII1i1 = O0ii1ii1ii ( url )
 OOO00O = re . compile ( '<div id="play-1" class="player-content"><iframe class="playerframe" src="(.+?)" scrolling="no".+?</div>' , re . DOTALL ) . findall ( iiII1i1 )
 for url in OOO00O :
  iI1i111I1Ii = url + '&fv=&sou='
  iI1i111I1Ii = iI1i111I1Ii . replace ( 'player' , 'watch' )
  ooo00 = iII11II1II ( iI1i111I1Ii )
  OOO00000o0 = iII11II1II ( url )
  if 96 - 96: OOooOOo * OoOO - OoOO0ooOOoo0O * OOooOOo * i1IIi
  if 8 - 8: o0oO0 - Oo + iIii1I11I1II1 + i1IIi * o00O0oo - iIii1I11I1II1
def iII11II1II ( url ) :
 if 30 - 30: o0000oOoOoO0o / ii11ii1ii
 iiII1i1 = O0ii1ii1ii ( url )
 OOO00O = re . compile ( '<video id=".+?<source src="(.+?)" type="video/mp4">' , re . DOTALL ) . findall ( iiII1i1 )
 for url in OOO00O :
  iI1iIIIIIiIi1 ( url )
  if 19 - 19: I1IiI . OOooOOo . OoooooooOO
  if 13 - 13: OoOO0ooOOoo0O . Oo / OoOoOO00
def iiI1iIII1ii ( ) :
 iiiiiIIii ( '[COLORgreen]Local M3u[/COLOR]' , i1iiIIiiI111 , 2001 , oOOoO0 + 'loader.png' , OOooO0OOoo , '' )
 iiiiiIIii ( '[COLORgreen]Remote M3u[/COLOR]' , oO , 1009 , oOOoO0 + 'loader.png' , OOooO0OOoo , '' )
 if 5 - 5: O0oO % OoooooooOO . I1IiI
def oO00o00 ( url ) :
 OOO00O = re . compile ( '^#EXTINF:-?[0-9]*(.*?),(.*?)\n(.*?)$' , re . I + re . M + re . U + re . S ) . findall
 for OOooooO0o0O0 , i1Oo00 , url in OOO00O :
  O00 ( i1Oo00 , url , 222 , oOOoO0 + 'streams.png' )
  if 74 - 74: I1IiI / i1IIi % OoooooooOO
  if 52 - 52: IIII % o0oO0
def I111oOOooo00OOooO ( ) :
 iiiiiIIii ( '[COLORgreen]CATAGORIES[/COLOR]' , '' , 10051 , oOOoO0 + 'loader.png' , OOooO0OOoo , '' )
 iiiiiIIii ( '[COLORgreen]SEARCH[/COLOR]' , '' , 10052 , oOOoO0 + 'loader.png' , OOooO0OOoo , '' )
 if 31 - 31: OOOo0 / OOooOOo + OOOo0 - OoOoOO00
 if 29 - 29: OOOo0 + i11iIiiIii . O0
o0oOoO00o = xbmcaddon . Addon ( id = 'plugin.video.GenieTv' )
Oo0o0000o0o0 = xbmcgui . Dialog ( )
iI111I11I1I1 = xbmc . translatePath ( 'special://home/' )
i1111 = xbmcgui . DialogProgress ( )
o0oo0Oo = 'https://addons.tvaddons.ag/'
if 10 - 10: ii11ii1ii
def oO0OOOoO0o ( ) :
 O00OOOoOoo0O = Oo0o0000o0o0 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oo0OOo = O00OOOoOoo0O . lower ( )
 OOOOO0 = 'https://addons.tvaddons.ag/search/?keyword=' + oo0OOo
 oO0OOoo0OO = O0ii1ii1ii ( OOOOO0 )
 OOO00O = re . compile ( '<li><a href="(.+?)"><span class=".+?"><img src="(.+?)" width=".+?" alt=".+?" class=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( oO0OOoo0OO )
 for ooOOO00Ooo , oOOo0 , i1Oo00 in OOO00O :
  iiiiiIIii ( i1Oo00 , ooOOO00Ooo , 10054 , 'https://addons.tvaddons.ag/' + oOOo0 , OOooO0OOoo , '' )
  if 75 - 75: ii11ii1ii
  if 92 - 92: o0000oOoOoO0o / O0 * OOOo0 - o0000oOoOoO0o
def oooOo00000 ( ) :
 oO0OOoo0OO = O0ii1ii1ii ( o0oo0Oo )
 OOO00O = re . compile ( '<li><a href="(.+?)"><span class="thumbnail"><img src="(.+?)" class="pic" alt=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( oO0OOoo0OO )
 for ooOOO00Ooo , oooooOoo0ooo , i1Oo00 in OOO00O :
  if 'Repositories' in i1Oo00 :
   pass
  elif 'Services' in i1Oo00 :
   pass
  elif 'International' in i1Oo00 :
   pass
  else :
   iiiiiIIii ( '[COLORgreen]' + i1Oo00 + '[/COLOR]' , ooOOO00Ooo , 10053 , 'https://addons.tvaddons.ag/' + oooooOoo0ooo , OOooO0OOoo , '' )
   if 45 - 45: O0 * O0oO + i11iIiiIii - OoOO0ooOOoo0O - iIii1I11I1II1
   if 5 - 5: OoOO0ooOOoo0O % Oo % IIII % o0oO0
def Addon ( url ) :
 oO0OOoo0OO = O0ii1ii1ii ( url )
 I1Iiii = re . compile ( '<li class="nextPage"><a class=".+?" href="(.+?)"><dfn title="next Page">.+?</dfn></a></li>' ) . findall ( oO0OOoo0OO )
 for url in I1Iiii :
  iiiiiIIii ( '[COLORgreen]NEXT PAGE[/COLOR]' , 'https://addons.tvaddons.ag' + url , 10053 , oOOoO0 + 'streams.png' , OOooO0OOoo , '' )
 OOO00O = re . compile ( '<li><a href="(.+?)"><span class=".+?"><img src="(.+?)" width=".+?" alt=".+?" class=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( oO0OOoo0OO )
 for url , oooooOoo0ooo , i1Oo00 in OOO00O :
  if 'Please' in i1Oo00 :
   pass
  else :
   iiiiiIIii ( i1Oo00 , url , 10054 , 'https://addons.tvaddons.ag/' + oooooOoo0ooo , OOooO0OOoo , '' )
   if 22 - 22: o00O0oo * o0000oOoOoO0o + OOOo0 - o0000oOoOoO0o / ii11ii1ii
   if 18 - 18: i1IIi
def i1i1Ii1IiIII ( url , name ) :
 oO0OOoo0OO = O0ii1ii1ii ( url )
 OOO00O = re . compile ( '<a href="(.+?)"' ) . findall ( oO0OOoo0OO )
 for url in OOO00O :
  if 'plugin' in url :
   print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<' + url
   o0oO00000 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
   i1111 = xbmcgui . DialogProgress ( )
   i1111 . create ( "Origin+Jaybox" , "Downloading Content" , '' , 'Please Wait' )
   II1I = os . path . join ( o0oO00000 , name + '.zip' )
   try :
    os . remove ( II1I )
   except :
    pass
   downloader . download ( url , II1I , i1111 )
   iiI11Iii = xbmc . translatePath ( os . path . join ( 'special://home' , 'addons' ) )
   time . sleep ( 2 )
   i1111 . update ( 0 , "" , "Extracting Zip Please Wait" )
   print '======================================='
   print iiI11Iii
   print '======================================='
   extract . all ( II1I , iiI11Iii , i1111 )
   O0o0O0 ( )
   if 9 - 9: o0000oOoOoO0o - OoOO + O0 / oO0o0ooO0 % i1IIi
def O0o0O0 ( ) :
 xbmc . executebuiltin ( 'UpdateLocalAddons' )
 xbmc . executebuiltin ( 'UpdateAddonRepos' )
 ii11iIi1I = xbmcgui . Dialog ( )
 ii11iIi1I . ok ( "Origin + Genie TV" , '' , '                                 REFRESH SUCCESSFUL :)' , "                          [COLOR gold]Brought To You By Origin + Jaybox[/COLOR]" )
 return
 if 97 - 97: OOooOOo * o0oO0
 if 78 - 78: o0000oOoOoO0o . OoOO0ooOOoo0O + OoOO * oO0o0ooO0 - i1IIi
def I1ii1I1iii1 ( ) :
 iiII1i1 = o00oOO0o ( oOo0oooo00o ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvc2NyYXBlZC9jYXRzLnBocA==' ) )
 OOO00O = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( iiII1i1 )
 for ooOOO00Ooo , oOOo0 , i1Oo00 in OOO00O :
  iiIiIiiiII ( i1Oo00 , ooOOO00Ooo , 1007 , oOOo0 )
def iIiiiIIiii ( url ) :
 iiII1i1 = o00oOO0o ( url )
 OOO00O = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( iiII1i1 )
 for url , oOOo0 , i1Oo00 in OOO00O :
  iiIiIiiiII ( '[COLORgreen]' + i1Oo00 + '[/COLOR]' , url , 1006 , oOOo0 )
  if 91 - 91: OOooOOo . oO0o0ooO0 % Oo - oO0o0ooO0 . OoOO % i11iIiiIii
  if 25 - 25: iIii1I11I1II1
def o0o0O0oOOOooo ( url ) :
 iiII1i1 = o00oOO0o ( url )
 OOO00O = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( iiII1i1 )
 for url , OOoOO0oo0ooO , O0o0O00Oo0o0 , O00O0oOO00O00 , i1Oo00 in OOO00O :
  if '.php' in url :
   II1iiIIIiIii ( i1Oo00 , url , 1016 , OOoOO0oo0ooO , O00O0oOO00O00 , O0o0O00Oo0o0 )
   Oooo0Ooo000 ( 'tvshows' , 'Media Info 3' )
  else :
   if 'youtube' in url :
    i1ii11 ( i1Oo00 , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , OOoOO0oo0ooO , O00O0oOO00O00 , O0o0O00Oo0o0 )
   else :
    i1ii11 ( i1Oo00 , url , 222 , OOoOO0oo0ooO , O00O0oOO00O00 , O0o0O00Oo0o0 )
   Oooo0Ooo000 ( 'tvshows' , 'INFO' )
   if 6 - 6: iIii1I11I1II1 - iIii1I11I1II1 % OOooOOo / iIii1I11I1II1 * O0oO
 else :
  OOO00O = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( iiII1i1 )
  for url , oOOo0 , i1Oo00 in OOO00O :
   if '.php' in url :
    iiIiIiiiII ( i1Oo00 , url , 1016 , oOOo0 )
   else :
    if 'youtube' in url :
     print '>>>>>>>>>>>>>>>>>>>>>>> youtube old way'
     O00 ( i1Oo00 , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , oOOo0 )
    else :
     O00 ( i1Oo00 , url , 222 , oOOo0 )
     if 3 - 3: OoOO0ooOOoo0O . IIII / Oo
     if 89 - 89: OoooooooOO . iIii1I11I1II1 . Oo * iIii1I11I1II1 - O0oO
  xbmcplugin . addSortMethod ( o0 , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 92 - 92: OoooooooOO - ii11ii1ii - OoooooooOO % OOOo0 % OOOo0 % iIii1I11I1II1
def O00oo0oOoO00O ( ) :
 iiII1i1 = o00oOO0o ( oOo0oooo00o ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vdm9kL3VybHMvdXJsLnBocA==' ) )
 OOO00O = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( iiII1i1 )
 for ooOOO00Ooo , oOOo0 , i1Oo00 in OOO00O :
  iiIiIiiiII ( i1Oo00 , ooOOO00Ooo , 1007 , oOOo0 )
def Iii1iIiI1I1I1 ( url ) :
 iiII1i1 = o00oOO0o ( url )
 OOO00O = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( iiII1i1 )
 for url , oOOo0 , i1Oo00 in OOO00O :
  iiIiIiiiII ( '[COLORgreen]' + i1Oo00 + '[/COLOR]' , url , 1006 , oOOo0 )
  if 66 - 66: I1IiI + OOooOOo
def OOOO00 ( name , url , iconimage = None ) :
 print '--- Playing "{0}". {1}' . format ( name , url )
 o0I1iI111ii111i = xbmcgui . ListItem ( path = url , thumbnailImage = iconimage )
 o0I1iI111ii111i . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , o0I1iI111ii111i )
 if 83 - 83: iIii1I11I1II1
 if 97 - 97: i11iIiiIii + Oo * OoOO0ooOOoo0O % oO0o0ooO0 . IIII
def ii ( url ) :
 iiII1i1 = o00oOO0o ( url )
 OOO00O = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( iiII1i1 )
 for url , oooooOoo0ooo , i1Oo00 in OOO00O :
  iiIiIiiiII ( '[COLORgreen]' + i1Oo00 + '[/COLOR]' , url , 1006 , oooooOoo0ooo )
def Oo0 ( url ) :
 iiII1i1 = o00oOO0o ( url )
 oOO0oo = url
 OOO00O = re . compile ( "<a href='(.+?)'>(.+?)</a>" ) . findall ( iiII1i1 )
 for url , i1Oo00 in OOO00O :
  if '.mp3' in i1Oo00 :
   print '<<<<<<<<<<<<<<<<<<<' + url + '>>>>>>>>>>>>>>>>>>>>>>>>>>>'
   O00 ( ( i1Oo00 ) . replace ( '.mp3' , '' ) . replace ( '/' , '' ) , 'http://hypem.com' + url , 222 , oOOoO0 + 'music.png' )
  else :
   iiIiIiiiII ( ( i1Oo00 ) . replace ( '/' , '' ) , oOO0oo + url , 1011 , oOOoO0 + 'music.png' )
def OOO00ii1Ii111I11I ( ) :
 iiII1i1 = o00oOO0o ( oOo0oooo00o ( 'aHR0cDovL3d3dy5jeW4ubmV0L211c2ljLw==' ) )
 OOO00O = re . compile ( '<td><a href="(.+?)"><img src="(.+?)"><br>(.+?)</a></td>' , re . DOTALL ) . findall ( iiII1i1 )
 for ooOOO00Ooo , oooooOoo0ooo , i1Oo00 in OOO00O :
  iiIiIiiiII ( i1Oo00 , ( 'http://www.cyn.net/music/' + ooOOO00Ooo ) . replace ( ' ' , '%20' ) , 1031 , ( 'http://www.cyn.net/music/' + oooooOoo0ooo ) . replace ( ' ' , '%20' ) )
def o0OoOoo ( url , img ) :
 iiII1i1 = o00oOO0o ( url )
 I111iIi1 = url
 img = img
 OOO00O = re . compile ( '<a href="(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( iiII1i1 )
 for url , i1Oo00 in OOO00O :
  O00 ( ( i1Oo00 ) . replace ( '.mp3' , '' ) , ( I111iIi1 + '/' + url ) . replace ( ' ' , '%20' ) , 222 , img )
  if 75 - 75: oO0o0ooO0 * OOOo0 + oO0o0ooO0 - OoooooooOO
  if 81 - 81: iIii1I11I1II1 / OoOO . i11iIiiIii * OoOoOO00
def o0oOOoo0O ( ) :
 O00OOO00Ooo = ( oOo0oooo00o ( 'aHR0cDovL2h5cGVtLmNvbS9kb3dubG9hZC8=' ) )
 O00OOOoOoo0O = Oo0o0000o0o0 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oo0OOo = O00OOOoOoo0O . lower ( )
 ooOOO00Ooo = ( oOo0oooo00o ( 'aHR0cDovL3Bhbmljc3RyZWFtLm5ldC9zdHJlYW1zLw==' ) )
 I111iIi1 = ( oOo0oooo00o ( 'aHR0cDovL21hc2xvdmQubm8taXAub3JnL3B1YmxpYy9tcDMv' ) )
 OoOOoooO000 = ( oOo0oooo00o ( 'aHR0cDovL3d3dy5jeW4ubmV0L211c2ljLw==' ) )
 if 57 - 57: OOOo0 . i11iIiiIii * OoOoOO00 + OoooooooOO + o00O0oo
 oO0OOoo0OO = o0oO00 ( ooOOO00Ooo )
 II1IIIii = o0oO00 ( I111iIi1 )
 I111iiiii1 = o0oO00 ( OoOOoooO000 )
 if 73 - 73: O0 % o0000oOoOoO0o + oO0o0ooO0 . ii11ii1ii . ii11ii1ii + IIII
 if oO0OOoo0OO != 'Failed' :
  OOO00O = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( oO0OOoo0OO )
  for i1Oo00 in OOO00O :
   if O00OOOoOoo0O in i1Oo00 . lower ( ) :
    iiIiIiiiII ( ( i1Oo00 + ' source 1' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( ooOOO00Ooo + i1Oo00 ) . replace ( ' ' , '%20' ) , 1006 , '' )
    if 30 - 30: I1IiI
    Oooo0Ooo000 ( 'tvshows' , 'Media Info 3' )
 if II1IIIii != 'Failed' :
  ii11I1 = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( oO0OOoo0OO )
  for i1Oo00 in ii11I1 :
   if O00OOOoOoo0O in i1Oo00 . lower ( ) :
    iiIiIiiiII ( ( i1Oo00 + ' source 2' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( I111iIi1 + i1Oo00 ) . replace ( ' ' , '%20' ) , 1006 , '' )
    if 89 - 89: o0000oOoOoO0o
    Oooo0Ooo000 ( 'tvshows' , 'Media Info 3' )
 if I111iiiii1 != 'Failed' :
  iI1I1iIi11 = re . compile ( '<td><a href=".+?"><img src=".+?"><br>(.+?)</a></td>' , re . DOTALL ) . findall ( I111iiiii1 )
  for i1Oo00 in iI1I1iIi11 :
   if O00OOOoOoo0O in i1Oo00 . lower ( ) :
    iiIiIiiiII ( ( i1Oo00 + ' source 3' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( OoOOoooO000 + i1Oo00 ) . replace ( ' ' , '%20' ) , 1031 , '' )
    if 89 - 89: o00O0oo - o0oO0 . o0000oOoOoO0o - O0oO - OOOo0
    Oooo0Ooo000 ( 'tvshows' , 'Media Info 3' )
    if 79 - 79: IIII + IIII + o00O0oo
    if 39 - 39: O0 - OoooooooOO
    if 63 - 63: iIii1I11I1II1 % OOooOOo * o0oO0
    if 79 - 79: O0
    if 32 - 32: OoOoOO00 . O0 + o00O0oo / I1IiI / IIII / OoOO0ooOOoo0O
    if 15 - 15: ii11ii1ii
def I11iI1 ( ) :
 iiII1i1 = O0ii1ii1ii ( 'http://www.animetoon.org/cartoon' )
 OOO00O = re . compile ( '<td><a href="(.+?)">(.+)</a></td>' ) . findall ( iiII1i1 )
 for ooOOO00Ooo , i1Oo00 in OOO00O :
  iiIiIiiiII ( i1Oo00 , ooOOO00Ooo , 1002 , oOOoO0 + 'anime.png' )
  if 96 - 96: OOooOOo % IIII / OoOO0ooOOoo0O
  if 63 - 63: i1IIi % i11iIiiIii % OoOoOO00 * OoooooooOO
  if 40 - 40: Oo
def iI1Ii11 ( url ) :
 iiII1i1 = O0ii1ii1ii ( url )
 ii11I1 = re . compile ( '<img src="(.+?)" id="series_image" width="250" height="370" alt=".+?" />' ) . findall ( iiII1i1 )
 for oooooOoo0ooo in ii11I1 :
  O00OO0oO = oooooOoo0ooo
 iI1I1iIi11 = re . compile ( '<li><a href="(.+?)">Next</a></li>' ) . findall ( iiII1i1 )
 for url in iI1I1iIi11 :
  iiIiIiiiII ( 'NEXT PAGE' , url , 1002 , O00OO0oO )
 OOO00O = re . compile ( '&nbsp;<a href="(.+?)">(.+?)</a>' ) . findall ( iiII1i1 )
 for url , i1Oo00 in OOO00O :
  iiIiIiiiII ( i1Oo00 , url , 1003 , O00OO0oO )
 xbmcplugin . addSortMethod ( o0 , xbmcplugin . SORT_METHOD_TITLE ) ;
def Ooo0 ( url , IMAGE ) :
 iiII1i1 = O0ii1ii1ii ( url )
 OOO00O = re . compile ( '"playlist">(.+?)</span></div><div><iframe src="(.+?)"' ) . findall ( iiII1i1 )
 for i1Oo00 , url in OOO00O :
  print i1Oo00 + '     ' + url
  if 'easy' in url :
   IiiiIIi ( url )
  elif 'playpanda' in url :
   IiiiIIi ( url )
   if 4 - 4: O0oO + Ooo00oOo00o + O0 + IIII
  xbmcplugin . addSortMethod ( o0 , xbmcplugin . SORT_METHOD_TITLE ) ;
def IiiiIIi ( url ) :
 iiII1i1 = O0ii1ii1ii ( url )
 OOO00O = re . compile ( "url: '(.+?)'," ) . findall ( iiII1i1 )
 for url in OOO00O :
  O00 ( 'STREAM' , url , 222 , oOOoO0 + 'anime.png' )
  if 96 - 96: OoOO / O0 . OoOoOO00 + IIII % OOooOOo
  if 67 - 67: O0 % O0oO
def III ( url ) :
 O00o0O = urllib2 . Request ( url )
 O00o0O . add_header ( 'User-Agent' , "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0" )
 O00o0O . add_header ( 'referer' , url )
 O00oOo0O0o00O = urllib2 . urlopen ( O00o0O )
 iI1i111I1Ii = O00oOo0O0o00O . read ( )
 O00oOo0O0o00O . close ( )
 return iI1i111I1Ii
 if 48 - 48: OoOO0ooOOoo0O . OoOO0ooOOoo0O + i11iIiiIii + ii11ii1ii % O0
def o00oOO0o ( url ) :
 O00o0O = urllib2 . Request ( url )
 O00o0O . add_header ( 'User-Agent' , "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0" )
 O00oOo0O0o00O = urllib2 . urlopen ( O00o0O )
 iI1i111I1Ii = O00oOo0O0o00O . read ( )
 O00oOo0O0o00O . close ( )
 return iI1i111I1Ii
 if 67 - 67: o0oO0 / o0000oOoOoO0o * OOOo0 % OoooooooOO
def ii1IIiI1iI1i ( url ) :
 xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
 Oo0ooo0Ooo = ( '%s%s' % ( i1II1I , url ) )
 iI1i111I1Ii = o00oOO0o ( url )
 OOO00O = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( iI1i111I1Ii )
 for url , oOOo0 , i1Oo00 in OOO00O :
  O00 ( '%s' % ( i1Oo00 ) . replace ( 'GenieTv' , '[COLOR green]GenieTV[/COLOR]' ) . replace ( '.' , ' ' ) . replace ( 'mp4' , '' ) . replace ( 'mkv' , '' ) . replace ( '_' , ' ' ) , '%s' % ( url ) , 222 , oOOo0 )
  if 22 - 22: OOooOOo + Oo . o0oO0 + ii11ii1ii * oO0o0ooO0 . i11iIiiIii
def iI1iIIIIIiIi1 ( url ) :
 IiI11i1IIiiI = xbmc . Player ( IIi1i ( ) )
 import urlresolver
 try : IiI11i1IIiiI . play ( url )
 except : pass
 from urlresolver import common
 i1111 = xbmcgui . DialogProgress ( )
 i1111 . create ( 'LOADING' , 'Opening %s Now' % ( i1Oo00 ) )
 IiI11i1IIiiI = xbmc . Player ( IIi1i ( ) )
 url = urlresolver . HostedMediaFile ( url ) . resolve ( )
 if i1111 . iscanceled ( ) :
  print "[COLORred]STREAM CANCELLED[/COLOR]"
  ii11iIi1I = xbmcgui . Dialog ( )
  if ii11iIi1I . yesno ( "[B]CANCELLED[/B]" , '[B]Was There A Problem[/B]' , '' , "" , 'Yes' , 'No' ) :
   ii11iIi1I . ok ( "Message Send" , "Your Message Has Been Sent" )
  else :
   return
 else :
  try : IiI11i1IIiiI . play ( url )
  except : pass
  try : o0oOoO00o . resolve_url ( url )
  except : pass
  i1111 . close ( )
  if 90 - 90: OoOO0ooOOoo0O * I1IiI - Oo + OOooOOo
def OO0 ( url ) :
 IiI11i1IIiiI = xbmc . Player ( IIi1i ( ) )
 import urlresolver
 try : IiI11i1IIiiI . play ( url )
 except : pass
 if 53 - 53: OoooooooOO . OoooooooOO + OOooOOo - oO0o0ooO0 + OoOO0ooOOoo0O
 if 44 - 44: O0oO - IIII
def IIi1i ( ) :
 try :
  OOOi1iIIiiIiII = getSet ( "core-player" )
  if ( OOOi1iIIiiIiII == 'DVDPLAYER' ) : i11I1iIii1i11 = xbmc . PLAYER_CORE_DVDPLAYER
  elif ( OOOi1iIIiiIiII == 'MPLAYER' ) : i11I1iIii1i11 = xbmc . PLAYER_CORE_MPLAYER
  elif ( OOOi1iIIiiIiII == 'PAPLAYER' ) : i11I1iIii1i11 = xbmc . PLAYER_CORE_PAPLAYER
  else : i11I1iIii1i11 = xbmc . PLAYER_CORE_AUTO
 except : i11I1iIii1i11 = xbmc . PLAYER_CORE_AUTO
 return i11I1iIii1i11
 return True
 if 42 - 42: Ooo00oOo00o * i11iIiiIii
def iiIiIiiiII ( name , url , mode , iconimage , showcontext = True , allinfo = { } ) :
 O00ooOo = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 oOO0o00O = True
 oOoO = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 oOoO . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 if showcontext :
  i1II11i1iI1 = [ ]
  if showcontext == 'fav' :
   i1II11i1iI1 . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in oOoOooOo0o0 :
   i1II11i1iI1 . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  oOoO . addContextMenuItems ( i1II11i1iI1 )
 oOO0o00O = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = O00ooOo , listitem = oOoO , isFolder = True )
 return oOO0o00O
 if 81 - 81: OoOO . OoooooooOO * OOooOOo * Ooo00oOo00o
def OOo ( name , url , mode , iconimage , fanart , description ) :
 if 10 - 10: OoOO - oO0o0ooO0 % OoOoOO00 - O0oO - i1IIi
 O00ooOo = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 oOO0o00O = True
 oOoO = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 oOoO . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 oOoO . setProperty ( "Fanart_Image" , fanart )
 oOO0o00O = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = O00ooOo , listitem = oOoO , isFolder = True )
 return oOO0o00O
 if 10 - 10: ii11ii1ii - o0000oOoOoO0o . O0oO
def O00 ( name , url , mode , iconimage , showcontext = True , allinfo = { } ) :
 O00ooOo = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 oOO0o00O = True
 oOoO = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 oOoO . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 if showcontext :
  i1II11i1iI1 = [ ]
  if showcontext == 'fav' :
   i1II11i1iI1 . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in oOoOooOo0o0 :
   i1II11i1iI1 . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  oOoO . addContextMenuItems ( i1II11i1iI1 )
 oOO0o00O = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = O00ooOo , listitem = oOoO , isFolder = False )
 return oOO0o00O
 if 8 - 8: iIii1I11I1II1 % OoOO + Oo
 if 24 - 24: OOooOOo / o00O0oo / o00O0oo % OoOoOO00 - OoOO * OoOO
 if 58 - 58: I1IiI
 if 60 - 60: OoOoOO00
 if 90 - 90: I1IiI
 if 37 - 37: I1IiI + O0 . O0 * Oo % O0oO / oO0o0ooO0
def Oo00OOoOo ( heading , announce ) :
 class iIIi ( ) :
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
   try : O0ooO0Oo00o = open ( announce ) ; OOOo00o = O0ooO0Oo00o . read ( )
   except : OOOo00o = announce
   self . win . getControl ( self . CONTROL_TEXTBOX ) . setText ( str ( OOOo00o ) )
   return
 iIIi ( )
 iIIi ( )
 if 3 - 3: OOooOOo
def Iii ( ) :
 Oo00OOoOo ( 'These are the main Sources you should get into you XBMC' , '[COLORwhite]http://architects.x10host.com[/COLOR]--- [CR]  [COLORred]http://repo.sharktech.co.uk[/COLOR]--- [CR]   [COLORwhite]http://fusion.tvaddons.ag[/COLOR]--- [CR]  [COLORred]http://i.totalxbmc.tv[/COLOR]--- [CR]   [COLORwhite]http://www.xunitytalk.com/xfinity[/COLOR]--- [CR]  [COLORred]http://srp.nu[/COLOR]--- [CR]   [COLORwhite]http://solved.no-issue.ca[/COLOR]--- [CR]  [COLORred]http://xbmc.aminhacasadigital.com[/COLOR]--- [CR]   [COLORwhite]http://xbmc.movieshd.co[/COLOR]--- [CR]  [COLORred]http://install.kaosbox.tv[/COLOR]--- [CR]   [COLORwhite]http://kodi-repo.com/mxr[/COLOR]--- [CR]  [COLORred]http://kodi.metalkettle.co[/COLOR]--- [CR]   [COLORwhite]http://prozone.getxbmc.com[/COLOR]--- [CR]  [COLORred]http://transform.mega-tron.tv[/COLOR]--- [CR]   [COLORwhite]http://muckys.kodimediaportal.ml[/COLOR]--- [CR]  [COLORred]http://jas0npc.pcriot.com[/COLOR]--- [CR]  [COLORwhite]Sports devil source[/COLOR]--- [CR]  [COLORred]http://iwillfolo.com/iwf[/COLOR]' )
 if 22 - 22: OoOoOO00 * o0oO0 + ii11ii1ii + o0000oOoOoO0o / I1IiI
 if 52 - 52: OoooooooOO / IIII % OoOoOO00
 if 40 - 40: OOOo0 % o0oO0 % IIII + Ooo00oOo00o
 if 75 - 75: OoOO - ii11ii1ii + OoOO + OoooooooOO . i11iIiiIii
 if 52 - 52: oO0o0ooO0 / o0oO0 - i11iIiiIii + OoooooooOO
def O0o0O0 ( ) :
 xbmc . executebuiltin ( 'UpdateLocalAddons' )
 xbmc . executebuiltin ( 'UpdateAddonRepos' )
 ii11iIi1I = xbmcgui . Dialog ( )
 ii11iIi1I . ok ( "GenieTv" , '' , '                                 REFRESH SUCCESSFUL :)' , "                          [COLOR gold]Brought To You By Kodi Support Group, GenieTv[/COLOR]" )
 return
 if 33 - 33: O0 + Oo - iIii1I11I1II1 % i11iIiiIii / OOOo0
 if 47 - 47: ii11ii1ii * OoOO + iIii1I11I1II1 - OoOO / IIII
 if 86 - 86: IIII
 if 43 - 43: OOOo0 / oO0o0ooO0 / o0oO0 + iIii1I11I1II1 + OoooooooOO
 if 33 - 33: OoOoOO00 - IIII - o0oO0
 if 92 - 92: Ooo00oOo00o * IIII
 if 92 - 92: OoOO
 if 7 - 7: oO0o0ooO0
 if 73 - 73: Ooo00oOo00o % ii11ii1ii
 if 32 - 32: OoOO0ooOOoo0O + oO0o0ooO0 + iIii1I11I1II1 * Oo
 if 62 - 62: i11iIiiIii
 if 2 - 2: OOOo0
 if 69 - 69: OoooooooOO / Oo * O0oO
 if 99 - 99: OoOoOO00 * iIii1I11I1II1 % O0 * OoOO / OoOoOO00 % OoooooooOO
 if 14 - 14: IIII . IIII % o0oO0
 if 42 - 42: OOooOOo . OoOO0ooOOoo0O - o0oO0
 if 33 - 33: OoOoOO00 / O0 / IIII - o0000oOoOoO0o - i1IIi
 if 8 - 8: i11iIiiIii . oO0o0ooO0 / iIii1I11I1II1 / ii11ii1ii / IIII - o00O0oo
 if 32 - 32: OOooOOo . i1IIi * Oo
 if 98 - 98: o00O0oo - OoOoOO00 / OOOo0 . OoOO * IIII . o0000oOoOoO0o
 if 25 - 25: i11iIiiIii / I1IiI - O0oO / Ooo00oOo00o . OOooOOo . OOooOOo
 if 6 - 6: OoOO . o0000oOoOoO0o
 if 43 - 43: ii11ii1ii + OOooOOo
 if 50 - 50: OoOO % i1IIi * O0
def iiIIi11ii1Ii ( url ) :
 iI1i111I1Ii = O0ii1ii1ii ( OO0o + OO0iiiii1iiIIii ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 OOO00O = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( iI1i111I1Ii )
 for i1Oo00 , url , OOoOO0oo0ooO , O00O0oOO00O00 , III1iII1I1ii in OOO00O :
  iiiiiIIii ( i1Oo00 , url , 42 , OOoOO0oo0ooO , O00O0oOO00O00 , III1iII1I1ii )
 Oooo0Ooo000 ( 'movies' , 'MAIN' )
 if 8 - 8: ii11ii1ii * ii11ii1ii * i1IIi + oO0o0ooO0 . ii11ii1ii
def Ooooo0O0 ( url ) :
 iI1i111I1Ii = O0ii1ii1ii ( OO0o + oOoO000 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 OOO00O = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( iI1i111I1Ii )
 for i1Oo00 , url , OOoOO0oo0ooO , O00O0oOO00O00 , III1iII1I1ii in OOO00O :
  iiiiiIIii ( i1Oo00 , url , 42 , OOoOO0oo0ooO , O00O0oOO00O00 , III1iII1I1ii )
 Oooo0Ooo000 ( 'movies' , 'MAIN' )
 if 86 - 86: iIii1I11I1II1 - o0000oOoOoO0o % o0oO0 . OoOO0ooOOoo0O * I1IiI . i1IIi
def O0o0O0OO0Oo00OO0oo ( url ) :
 iI1i111I1Ii = O0ii1ii1ii ( OO0o + oOO00o0O0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 OOO00O = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( iI1i111I1Ii )
 for i1Oo00 , url , OOoOO0oo0ooO , O00O0oOO00O00 , III1iII1I1ii in OOO00O :
  iiiiiIIii ( i1Oo00 , url , 42 , OOoOO0oo0ooO , O00O0oOO00O00 , III1iII1I1ii )
 Oooo0Ooo000 ( 'movies' , 'MAIN' )
 if 47 - 47: o0oO0
def Oo0ooIi ( url ) :
 iI1i111I1Ii = O0ii1ii1ii ( OO0o + IiiI1iii1iIiiI ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 OOO00O = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( iI1i111I1Ii )
 for i1Oo00 , url , OOoOO0oo0ooO , O00O0oOO00O00 , III1iII1I1ii in OOO00O :
  iiiiiIIii ( i1Oo00 , url , 42 , OOoOO0oo0ooO , O00O0oOO00O00 , III1iII1I1ii )
 Oooo0Ooo000 ( 'movies' , 'MAIN' )
 if 36 - 36: Ooo00oOo00o - O0 * OOOo0 / ii11ii1ii / OoOO0ooOOoo0O
def IiiIiiIIII ( url ) :
 iI1i111I1Ii = O0ii1ii1ii ( OO0o + oOo ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 OOO00O = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( iI1i111I1Ii )
 for i1Oo00 , url , OOoOO0oo0ooO , O00O0oOO00O00 , III1iII1I1ii in OOO00O :
  iiiiiIIii ( i1Oo00 , url , 42 , OOoOO0oo0ooO , O00O0oOO00O00 , III1iII1I1ii )
 Oooo0Ooo000 ( 'movies' , 'MAIN' )
 if 94 - 94: Ooo00oOo00o + Ooo00oOo00o + ii11ii1ii . Ooo00oOo00o * o00O0oo
def oOoOoOOo00Ooo0O ( url ) :
 iI1i111I1Ii = O0ii1ii1ii ( OO0o + iIii1Oo ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 OOO00O = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( iI1i111I1Ii )
 for i1Oo00 , url , OOoOO0oo0ooO , O00O0oOO00O00 , III1iII1I1ii in OOO00O :
  iiiiiIIii ( i1Oo00 , url , 42 , OOoOO0oo0ooO , O00O0oOO00O00 , III1iII1I1ii )
 Oooo0Ooo000 ( 'movies' , 'MAIN' )
 if 15 - 15: i1IIi + IIII % OOOo0 / i11iIiiIii * I1IiI
def oOiI1I ( url ) :
 iI1i111I1Ii = O0ii1ii1ii ( OO0o + i111I1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 OOO00O = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( iI1i111I1Ii )
 for i1Oo00 , url , OOoOO0oo0ooO , O00O0oOO00O00 , III1iII1I1ii in OOO00O :
  iiiiiIIii ( i1Oo00 , url , 42 , OOoOO0oo0ooO , O00O0oOO00O00 , III1iII1I1ii )
 Oooo0Ooo000 ( 'movies' , 'MAIN' )
 if 69 - 69: Ooo00oOo00o - OoooooooOO - OoOO0ooOOoo0O % o0000oOoOoO0o / I1IiI - OoOoOO00
def O0O0oOO ( url ) :
 iI1i111I1Ii = O0ii1ii1ii ( OO0o + iiiI1Ii1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 OOO00O = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( iI1i111I1Ii )
 for i1Oo00 , url , OOoOO0oo0ooO , O00O0oOO00O00 , III1iII1I1ii in OOO00O :
  iiiiiIIii ( i1Oo00 , url , 42 , OOoOO0oo0ooO , O00O0oOO00O00 , III1iII1I1ii )
 Oooo0Ooo000 ( 'movies' , 'MAIN' )
 if 97 - 97: OoOoOO00 % Oo * IIII
def oOoOO0O00o ( url ) :
 iI1i111I1Ii = O0ii1ii1ii ( OO0o + o0OOOO ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 OOO00O = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( iI1i111I1Ii )
 for i1Oo00 , url , OOoOO0oo0ooO , O00O0oOO00O00 , III1iII1I1ii in OOO00O :
  iiiiiIIii ( i1Oo00 , url , 42 , OOoOO0oo0ooO , O00O0oOO00O00 , III1iII1I1ii )
 Oooo0Ooo000 ( 'movies' , 'MAIN' )
 if 58 - 58: OOooOOo % OOOo0 . OOOo0 * Ooo00oOo00o - IIII . OoooooooOO
def iI1111i1i11Ii ( url ) :
 iI1i111I1Ii = O0ii1ii1ii ( OO0o + oo0O00o0O0Oo ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 OOO00O = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( iI1i111I1Ii )
 for i1Oo00 , url , OOoOO0oo0ooO , O00O0oOO00O00 , III1iII1I1ii in OOO00O :
  iiiiiIIii ( i1Oo00 , url , 5 , OOoOO0oo0ooO , O00O0oOO00O00 , III1iII1I1ii )
 Oooo0Ooo000 ( 'movies' , 'MAIN' )
 if 26 - 26: i1IIi / oO0o0ooO0 . oO0o0ooO0
 if 20 - 20: OoOO0ooOOoo0O - oO0o0ooO0 / Oo * Ooo00oOo00o
 if 55 - 55: OoooooooOO
 if 73 - 73: I1IiI - ii11ii1ii % Oo + ii11ii1ii - O0 . Ooo00oOo00o
 if 38 - 38: O0
 if 79 - 79: i1IIi . OoOO
 if 34 - 34: O0oO * OoOoOO00
 if 71 - 71: IIII
 if 97 - 97: ii11ii1ii
def OOo0oO0o ( ) :
 try :
  if os . path . exists ( OooO0 ) == True :
   ii11iIi1I = xbmcgui . Dialog ( )
   if ii11iIi1I . yesno ( "Delete Thumbnails" , "[COLOR gold][B]##########WARNING ANDROID ONLY##########[/B][/COLOR]" , "This feature deletes your thumbnail folder and textures13.db" , "Are you sure you want to do proceed? This Can NOT Be Undone" ) :
    for iI111i1II , iIIIiIi , OO0O0 in os . walk ( OooO0 ) :
     iI1iI = 0
     iI1iI += len ( OO0O0 )
     if iI1iI > 0 :
      for O0ooO0Oo00o in OO0O0 :
       os . unlink ( os . path . join ( iI111i1II , O0ooO0Oo00o ) )
  O0oo0000o = os . path . join ( II , "Textures13.db" )
  os . unlink ( O0oo0000o )
  ii11iIi1I . ok ( "Restart KODI" , "Please restart KODI to rebuild thumbnail library" )
 except :
  ii11iIi1I = xbmcgui . Dialog ( )
  ii11iIi1I . ok ( i11 , "Error Deleting Thumbnails please visit Kodi Support Group, GenieTv on facebook" )
 return
 if 99 - 99: OoOO - ii11ii1ii . OoOoOO00 * i11iIiiIii . OoOO0ooOOoo0O - Ooo00oOo00o
 if 31 - 31: i11iIiiIii * o00O0oo . OOooOOo % OoOO0ooOOoo0O * ii11ii1ii % O0
 if 77 - 77: Ooo00oOo00o + Ooo00oOo00o . o0oO0 * OoooooooOO + Ooo00oOo00o
 if 6 - 6: i1IIi - o0000oOoOoO0o
 if 89 - 89: o0oO0 - o0000oOoOoO0o . O0 % OoooooooOO . i11iIiiIii
 if 35 - 35: OoOoOO00 / I1IiI - O0 . OoOoOO00
 if 55 - 55: Oo % i1IIi * o0000oOoOoO0o
 if 95 - 95: OoOO0ooOOoo0O / OoOoOO00 - OOooOOo % O0oO . o0000oOoOoO0o
 if 63 - 63: iIii1I11I1II1 / o0oO0
def II1iOOoOooO0o ( url ) :
 print '############################################################       DELETING STANDARD CACHE             ###############################################################'
 I1IiiiI = os . path . join ( xbmc . translatePath ( 'special://home' ) , 'cache' )
 if os . path . exists ( I1IiiiI ) == True :
  for iI111i1II , iIIIiIi , OO0O0 in os . walk ( I1IiiiI ) :
   iI1iI = 0
   iI1iI += len ( OO0O0 )
   if 6 - 6: OOOo0 - i11iIiiIii
   if 61 - 61: O0oO * ii11ii1ii % OOOo0 % Ooo00oOo00o % o0000oOoOoO0o + o0000oOoOoO0o
   if iI1iI > 0 :
    if 6 - 6: Oo
    ii11iIi1I = xbmcgui . Dialog ( )
    if ii11iIi1I . yesno ( "Delete KODI Cache Files" , str ( iI1iI ) + " files found" , "Do you want to delete them?" ) :
     if 73 - 73: O0oO * ii11ii1ii + OOooOOo - Oo . o0000oOoOoO0o
     for O0ooO0Oo00o in OO0O0 :
      try :
       os . unlink ( os . path . join ( iI111i1II , O0ooO0Oo00o ) )
      except :
       pass
     for o000O0O in iIIIiIi :
      try :
       shutil . rmtree ( os . path . join ( iI111i1II , o000O0O ) )
      except :
       pass
       if 93 - 93: i11iIiiIii
   else :
    pass
 if xbmc . getCondVisibility ( 'system.platform.ATV2' ) :
  OoOiII11IiIi = os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'Other' )
  if 27 - 27: Ooo00oOo00o + I1IiI
  for iI111i1II , iIIIiIi , OO0O0 in os . walk ( OoOiII11IiIi ) :
   iI1iI = 0
   iI1iI += len ( OO0O0 )
   if 97 - 97: i1IIi * O0oO . OoOoOO00
   if iI1iI > 0 :
    if 62 - 62: OoooooooOO . o00O0oo
    ii11iIi1I = xbmcgui . Dialog ( )
    if ii11iIi1I . yesno ( "Delete ATV2 Cache Files" , str ( iI1iI ) + " files found in 'Other'" , "Do you want to delete them?" ) :
     if 28 - 28: OoOO . OoOO . iIii1I11I1II1 . OoOO0ooOOoo0O . ii11ii1ii * i11iIiiIii
     for O0ooO0Oo00o in OO0O0 :
      os . unlink ( os . path . join ( iI111i1II , O0ooO0Oo00o ) )
     for o000O0O in iIIIiIi :
      shutil . rmtree ( os . path . join ( iI111i1II , o000O0O ) )
      if 72 - 72: o0000oOoOoO0o
   else :
    pass
  i1I1IIiIIi = os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'LocalAndRental' )
  if 33 - 33: Ooo00oOo00o % IIII - iIii1I11I1II1
  for iI111i1II , iIIIiIi , OO0O0 in os . walk ( i1I1IIiIIi ) :
   iI1iI = 0
   iI1iI += len ( OO0O0 )
   if 33 - 33: Ooo00oOo00o + I1IiI - OoOO * i11iIiiIii . O0oO
   if iI1iI > 0 :
    if 92 - 92: OoOO
    ii11iIi1I = xbmcgui . Dialog ( )
    if ii11iIi1I . yesno ( "Delete ATV2 Cache Files" , str ( iI1iI ) + " files found in 'LocalAndRental'" , "Do you want to delete them?" ) :
     if 81 - 81: OOooOOo % OOOo0 - oO0o0ooO0 / i11iIiiIii
     for O0ooO0Oo00o in OO0O0 :
      os . unlink ( os . path . join ( iI111i1II , O0ooO0Oo00o ) )
     for o000O0O in iIIIiIi :
      shutil . rmtree ( os . path . join ( iI111i1II , o000O0O ) )
      if 73 - 73: O0 * O0oO . i1IIi
   else :
    pass
    if 51 - 51: Ooo00oOo00o - oO0o0ooO0 % O0 - I1IiI
    if 53 - 53: oO0o0ooO0 / i1IIi / i1IIi
    if 77 - 77: o0000oOoOoO0o + i1IIi . o0000oOoOoO0o
    if 89 - 89: OOooOOo + OoOO0ooOOoo0O * OoOO
 i1iI1IIi = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.whatthefurk/cache' ) , '' )
 if os . path . exists ( i1iI1IIi ) == True :
  for iI111i1II , iIIIiIi , OO0O0 in os . walk ( i1iI1IIi ) :
   iI1iI = 0
   iI1iI += len ( OO0O0 )
   if 27 - 27: O0 / Ooo00oOo00o
   if 99 - 99: o00O0oo - IIII * iIii1I11I1II1 . OoOoOO00
   if iI1iI > 0 :
    if 56 - 56: iIii1I11I1II1 % Ooo00oOo00o . o0oO0 % IIII . O0oO * Oo
    ii11iIi1I = xbmcgui . Dialog ( )
    if ii11iIi1I . yesno ( "Delete WTF Cache Files" , str ( iI1iI ) + " files found" , "Do you want to delete them?" ) :
     if 41 - 41: iIii1I11I1II1 % IIII * OoOO - o0oO0
     for O0ooO0Oo00o in OO0O0 :
      os . unlink ( os . path . join ( iI111i1II , O0ooO0Oo00o ) )
     for o000O0O in iIIIiIi :
      shutil . rmtree ( os . path . join ( iI111i1II , o000O0O ) )
      if 5 - 5: Ooo00oOo00o + Ooo00oOo00o + OoOoOO00 * iIii1I11I1II1 + OoooooooOO
   else :
    pass
    if 77 - 77: O0 * ii11ii1ii * OoOO + Ooo00oOo00o + ii11ii1ii - O0oO
    if 10 - 10: ii11ii1ii + IIII
 Ooooo00 = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.4od/cache' ) , '' )
 if os . path . exists ( Ooooo00 ) == True :
  for iI111i1II , iIIIiIi , OO0O0 in os . walk ( Ooooo00 ) :
   iI1iI = 0
   iI1iI += len ( OO0O0 )
   if 99 - 99: ii11ii1ii - OoOO
   if 10 - 10: OoOoOO00 . Ooo00oOo00o
   if iI1iI > 0 :
    if 89 - 89: o0oO0 * o00O0oo
    ii11iIi1I = xbmcgui . Dialog ( )
    if ii11iIi1I . yesno ( "Delete 4oD Cache Files" , str ( iI1iI ) + " files found" , "Do you want to delete them?" ) :
     if 93 - 93: i1IIi . o00O0oo * O0oO . o0oO0
     for O0ooO0Oo00o in OO0O0 :
      os . unlink ( os . path . join ( iI111i1II , O0ooO0Oo00o ) )
     for o000O0O in iIIIiIi :
      shutil . rmtree ( os . path . join ( iI111i1II , o000O0O ) )
      if 54 - 54: oO0o0ooO0 . i1IIi . ii11ii1ii * OOooOOo % oO0o0ooO0
   else :
    pass
    if 30 - 30: o0000oOoOoO0o
    if 85 - 85: OoOoOO00 + o0oO0 * o0000oOoOoO0o
 i1ooOO00o0 = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.iplayer/iplayer_http_cache' ) , '' )
 if os . path . exists ( i1ooOO00o0 ) == True :
  for iI111i1II , iIIIiIi , OO0O0 in os . walk ( i1ooOO00o0 ) :
   iI1iI = 0
   iI1iI += len ( OO0O0 )
   if 44 - 44: OOOo0 % OoOO0ooOOoo0O * i11iIiiIii * i11iIiiIii - Oo . O0oO
   if 68 - 68: oO0o0ooO0 . o0000oOoOoO0o
   if iI1iI > 0 :
    if 29 - 29: o0oO0 * IIII
    ii11iIi1I = xbmcgui . Dialog ( )
    if ii11iIi1I . yesno ( "Delete BBC iPlayer Cache Files" , str ( iI1iI ) + " files found" , "Do you want to delete them?" ) :
     if 75 - 75: O0
     for O0ooO0Oo00o in OO0O0 :
      os . unlink ( os . path . join ( iI111i1II , O0ooO0Oo00o ) )
     for o000O0O in iIIIiIi :
      shutil . rmtree ( os . path . join ( iI111i1II , o000O0O ) )
      if 56 - 56: Ooo00oOo00o / OoOoOO00
   else :
    pass
    if 39 - 39: I1IiI - OoooooooOO - i1IIi / OoOoOO00
    if 49 - 49: Oo + O0 + IIII . OoOoOO00 % o0oO0
    if 33 - 33: I1IiI . iIii1I11I1II1 / o0000oOoOoO0o % o00O0oo
 IIiiI11 = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/script.module.simple.downloader' ) , '' )
 if os . path . exists ( IIiiI11 ) == True :
  for iI111i1II , iIIIiIi , OO0O0 in os . walk ( IIiiI11 ) :
   iI1iI = 0
   iI1iI += len ( OO0O0 )
   if 7 - 7: OOOo0 / Ooo00oOo00o + O0oO + o0000oOoOoO0o / OOOo0
   if 82 - 82: ii11ii1ii + OoooooooOO
   if iI1iI > 0 :
    if 21 - 21: OoOO * OoOO / o0000oOoOoO0o . oO0o0ooO0
    ii11iIi1I = xbmcgui . Dialog ( )
    if ii11iIi1I . yesno ( "Delete Simple Downloader Cache Files" , str ( iI1iI ) + " files found" , "Do you want to delete them?" ) :
     if 10 - 10: o00O0oo * OoOO0ooOOoo0O - Oo - OoooooooOO / OOooOOo
     for O0ooO0Oo00o in OO0O0 :
      os . unlink ( os . path . join ( iI111i1II , O0ooO0Oo00o ) )
     for o000O0O in iIIIiIi :
      shutil . rmtree ( os . path . join ( iI111i1II , o000O0O ) )
      if 86 - 86: O0oO % OOOo0
   else :
    pass
    if 22 - 22: i11iIiiIii * O0oO . Oo . OoooooooOO + OOOo0
    if 24 - 24: OoOoOO00 / o00O0oo . iIii1I11I1II1 - OoOoOO00 % O0
 IIi1Ii11iIi = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.itv/Images' ) , '' )
 if os . path . exists ( IIi1Ii11iIi ) == True :
  for iI111i1II , iIIIiIi , OO0O0 in os . walk ( IIi1Ii11iIi ) :
   iI1iI = 0
   iI1iI += len ( OO0O0 )
   if 33 - 33: OoOoOO00 . OoOoOO00 / I1IiI - OoOoOO00
   if 10 - 10: I1IiI - OOooOOo * i11iIiiIii / Oo + OOooOOo + iIii1I11I1II1
   if iI1iI > 0 :
    if 23 - 23: i1IIi + ii11ii1ii + OOOo0 - o0oO0 % OoooooooOO . IIII
    ii11iIi1I = xbmcgui . Dialog ( )
    if ii11iIi1I . yesno ( "Delete ITV Cache Files" , str ( iI1iI ) + " files found" , "Do you want to delete them?" ) :
     if 49 - 49: OoOO . I1IiI
     for O0ooO0Oo00o in OO0O0 :
      os . unlink ( os . path . join ( iI111i1II , O0ooO0Oo00o ) )
     for o000O0O in iIIIiIi :
      shutil . rmtree ( os . path . join ( iI111i1II , o000O0O ) )
      if 73 - 73: o00O0oo / OOOo0 / OoooooooOO + OOOo0
   else :
    pass
    if 57 - 57: OoOO0ooOOoo0O . o00O0oo % OOooOOo
    if 32 - 32: o0000oOoOoO0o / IIII - O0 * iIii1I11I1II1
 oo0oO0oOo0O = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.movies4me/cache' ) , '' )
 if os . path . exists ( IIi1Ii11iIi ) == True :
  for iI111i1II , iIIIiIi , OO0O0 in os . walk ( oo0oO0oOo0O ) :
   iI1iI = 0
   iI1iI += len ( OO0O0 )
   if 75 - 75: OoOoOO00 + OoOoOO00 + OoOO0ooOOoo0O * OOooOOo
   if 62 - 62: iIii1I11I1II1 - i1IIi - OoOO
   if iI1iI > 0 :
    if 72 - 72: I1IiI / O0oO * IIII % iIii1I11I1II1
    ii11iIi1I = xbmcgui . Dialog ( )
    if ii11iIi1I . yesno ( "Delete Movies4me Cache Files" , str ( iI1iI ) + " files found" , "Do you want to delete them?" ) :
     if 53 - 53: Ooo00oOo00o . O0 . OOOo0 * OoOO0ooOOoo0O / OOooOOo
     for O0ooO0Oo00o in OO0O0 :
      os . unlink ( os . path . join ( iI111i1II , O0ooO0Oo00o ) )
     for o000O0O in iIIIiIi :
      shutil . rmtree ( os . path . join ( iI111i1II , o000O0O ) )
      if 34 - 34: I1IiI
   else :
    pass
    if 16 - 16: i1IIi - O0oO - OoOoOO00
    if 83 - 83: OOOo0 - Ooo00oOo00o - OOooOOo / O0 - o0000oOoOoO0o . OoOoOO00
 iI1i1Ii111I = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.phstreams/Cache' ) , '' )
 if os . path . exists ( IIi1Ii11iIi ) == True :
  for iI111i1II , iIIIiIi , OO0O0 in os . walk ( iI1i1Ii111I ) :
   iI1iI = 0
   iI1iI += len ( OO0O0 )
   if 17 - 17: O0 * iIii1I11I1II1 % IIII . IIII / O0
   if 52 - 52: OOOo0 - iIii1I11I1II1 - ii11ii1ii
   if iI1iI > 0 :
    if 38 - 38: OOOo0 + OOooOOo - IIII
    ii11iIi1I = xbmcgui . Dialog ( )
    if ii11iIi1I . yesno ( "Delete Phoenix Cache Files" , str ( iI1iI ) + " files found" , "Do you want to delete them?" ) :
     if 85 - 85: oO0o0ooO0 * oO0o0ooO0 % I1IiI - OoOO0ooOOoo0O % Ooo00oOo00o - OOOo0
     for O0ooO0Oo00o in OO0O0 :
      os . unlink ( os . path . join ( iI111i1II , O0ooO0Oo00o ) )
     for o000O0O in iIIIiIi :
      shutil . rmtree ( os . path . join ( iI111i1II , o000O0O ) )
      if 3 - 3: OoOO0ooOOoo0O + i1IIi % ii11ii1ii
   else :
    pass
    if 100 - 100: OoooooooOO + i11iIiiIii % OOooOOo + OOOo0 . Oo . OoOoOO00
    if 93 - 93: OoOoOO00 . i11iIiiIii + OoOoOO00 % OoOO
 O00OOO000oo0 = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.spotitube/cache' ) , '' )
 if os . path . exists ( IIi1Ii11iIi ) == True :
  for iI111i1II , iIIIiIi , OO0O0 in os . walk ( O00OOO000oo0 ) :
   iI1iI = 0
   iI1iI += len ( OO0O0 )
   if 16 - 16: iIii1I11I1II1 * oO0o0ooO0 + OoOO . O0 . OOooOOo
   if 99 - 99: i11iIiiIii - oO0o0ooO0
   if iI1iI > 0 :
    if 85 - 85: O0oO % ii11ii1ii
    ii11iIi1I = xbmcgui . Dialog ( )
    if ii11iIi1I . yesno ( "Delete YouTube Music Cache Files" , str ( iI1iI ) + " files found" , "Do you want to delete them?" ) :
     if 95 - 95: Ooo00oOo00o * OoOO0ooOOoo0O * oO0o0ooO0 . OOooOOo
     for O0ooO0Oo00o in OO0O0 :
      os . unlink ( os . path . join ( iI111i1II , O0ooO0Oo00o ) )
     for o000O0O in iIIIiIi :
      shutil . rmtree ( os . path . join ( iI111i1II , o000O0O ) )
      if 73 - 73: Ooo00oOo00o
   else :
    pass
    if 28 - 28: OoooooooOO - o0000oOoOoO0o
    if 84 - 84: OoOoOO00
 i1IIii1i = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.supercartoons/cache' ) , '' )
 if os . path . exists ( IIi1Ii11iIi ) == True :
  for iI111i1II , iIIIiIi , OO0O0 in os . walk ( i1IIii1i ) :
   iI1iI = 0
   iI1iI += len ( OO0O0 )
   if 60 - 60: o00O0oo % Oo / o0000oOoOoO0o . oO0o0ooO0 / O0oO - OoooooooOO
   if 76 - 76: O0
   if iI1iI > 0 :
    if 71 - 71: OOOo0 . i1IIi
    ii11iIi1I = xbmcgui . Dialog ( )
    if ii11iIi1I . yesno ( "Delete SuperCartoons Cache Files" , str ( iI1iI ) + " files found" , "Do you want to delete them?" ) :
     if 19 - 19: OoOoOO00 / OoOoOO00 % ii11ii1ii + OoOO + OoOO + oO0o0ooO0
     for O0ooO0Oo00o in OO0O0 :
      os . unlink ( os . path . join ( iI111i1II , O0ooO0Oo00o ) )
     for o000O0O in iIIIiIi :
      shutil . rmtree ( os . path . join ( iI111i1II , o000O0O ) )
      if 4 - 4: OOooOOo + o0000oOoOoO0o / oO0o0ooO0 + i1IIi % OOooOOo % oO0o0ooO0
   else :
    pass
    if 80 - 80: o00O0oo
    if 26 - 26: iIii1I11I1II1 . OoooooooOO - iIii1I11I1II1
 oOo0O0 = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.tvonline.cc/cache' ) , '' )
 if os . path . exists ( IIi1Ii11iIi ) == True :
  for iI111i1II , iIIIiIi , OO0O0 in os . walk ( oOo0O0 ) :
   iI1iI = 0
   iI1iI += len ( OO0O0 )
   if 1 - 1: OoOO + O0oO . OOOo0
   if 47 - 47: oO0o0ooO0 . I1IiI
   if iI1iI > 0 :
    if 58 - 58: oO0o0ooO0 + Oo / OOOo0
    ii11iIi1I = xbmcgui . Dialog ( )
    if ii11iIi1I . yesno ( "Delete TVonline Cache Files" , str ( iI1iI ) + " files found" , "Do you want to delete them?" ) :
     if 68 - 68: IIII * o00O0oo
     for O0ooO0Oo00o in OO0O0 :
      os . unlink ( os . path . join ( iI111i1II , O0ooO0Oo00o ) )
     for o000O0O in iIIIiIi :
      shutil . rmtree ( os . path . join ( iI111i1II , o000O0O ) )
      if 91 - 91: o00O0oo + Ooo00oOo00o * OOooOOo . O0oO
   else :
    pass
    if 89 - 89: OoooooooOO * o00O0oo * OOOo0 . o0oO0 * o00O0oo / oO0o0ooO0
    if 46 - 46: i11iIiiIii
 Iiiii = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.youtube/kodion' ) , '' )
 if os . path . exists ( IIi1Ii11iIi ) == True :
  for iI111i1II , iIIIiIi , OO0O0 in os . walk ( Iiiii ) :
   iI1iI = 0
   iI1iI += len ( OO0O0 )
   if 25 - 25: Oo * OOOo0 + OoOO0ooOOoo0O + O0oO % OoOO0ooOOoo0O
   if 84 - 84: O0 % o00O0oo . o00O0oo . oO0o0ooO0 * o0000oOoOoO0o
   if iI1iI > 0 :
    if 43 - 43: I1IiI . ii11ii1ii % i1IIi
    ii11iIi1I = xbmcgui . Dialog ( )
    if ii11iIi1I . yesno ( "Delete YouTube Cache Files" , str ( iI1iI ) + " files found" , "Do you want to delete them?" ) :
     if 61 - 61: OOOo0 + OoOO % O0oO % iIii1I11I1II1 - OoooooooOO
     for O0ooO0Oo00o in OO0O0 :
      os . unlink ( os . path . join ( iI111i1II , O0ooO0Oo00o ) )
     for o000O0O in iIIIiIi :
      shutil . rmtree ( os . path . join ( iI111i1II , o000O0O ) )
      if 22 - 22: OoOO0ooOOoo0O + OoOoOO00 + Oo
   else :
    pass
    if 83 - 83: o0oO0
    if 43 - 43: OoOO0ooOOoo0O
    if 84 - 84: OoOO0ooOOoo0O . IIII . oO0o0ooO0
 iIII1I1i = xbmc . translatePath ( 'special://masterprofile/addon_data/plugin.video.genesis' )
 ii11iIi1I = xbmcgui . Dialog ( )
 try :
  if ii11iIi1I . yesno ( "Delete Genesis Cache Files" , "Do you want to delete cache" ) :
   I1IIIIII1 = os . path . join ( iIII1I1i , "cache.db" )
   os . unlink ( I1IIIIII1 )
   if 99 - 99: OoOO0ooOOoo0O + OOOo0 . ii11ii1ii * OoooooooOO
 except :
  pass
  if 82 - 82: i11iIiiIii + iIii1I11I1II1 / Oo + OoOO0ooOOoo0O * OoOoOO00
 ii11iIi1I = xbmcgui . Dialog ( )
 ii11iIi1I . ok ( "GenieTv" , "                               Finished Deleting Cache " , "                          [COLOR gold]Brought To You By GenieTv[/COLOR]" )
 if 34 - 34: OOooOOo % OoooooooOO
 if 36 - 36: OOOo0
 if 64 - 64: i11iIiiIii + i1IIi % O0 . o0000oOoOoO0o
 if 64 - 64: o0oO0 / i1IIi % oO0o0ooO0
 if 84 - 84: I1IiI - Oo . o0oO0 . IIII - Oo
 if 99 - 99: O0oO
 if 75 - 75: o0oO0 . OoOO0ooOOoo0O / IIII
 if 84 - 84: OoooooooOO . OOOo0 / OOooOOo
 if 86 - 86: Oo % I1IiI
def o0o0O00oOo ( url ) :
 print '###' + i11 + ' - DELETING PACKAGES###'
 iI1ii = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' , '' ) )
 try :
  for iI111i1II , iIIIiIi , OO0O0 in os . walk ( iI1ii ) :
   iI1iI = 0
   iI1iI += len ( OO0O0 )
   if 2 - 2: OoOoOO00 . o0000oOoOoO0o
   if 83 - 83: OOOo0 - O0oO + OOOo0 . OOOo0
   if iI1iI > 0 :
    if 45 - 45: i1IIi % OoOO0ooOOoo0O % OoOoOO00
    ii11iIi1I = xbmcgui . Dialog ( )
    if ii11iIi1I . yesno ( "Delete Package Cache Files" , str ( iI1iI ) + " files found" , "Do you want to delete them?" ) :
     if 4 - 4: OoOO * OOOo0 - o0oO0 / OoOoOO00 + OoOO0ooOOoo0O / i11iIiiIii
     for O0ooO0Oo00o in OO0O0 :
      os . unlink ( os . path . join ( iI111i1II , O0ooO0Oo00o ) )
     for o000O0O in iIIIiIi :
      shutil . rmtree ( os . path . join ( iI111i1II , o000O0O ) )
     ii11iIi1I = xbmcgui . Dialog ( )
     ii11iIi1I . ok ( i11 , "       Deleting Packages all done" )
    else :
     pass
   else :
    ii11iIi1I = xbmcgui . Dialog ( )
    ii11iIi1I . ok ( i11 , "       No Packages to DELETE" )
 except :
  ii11iIi1I = xbmcgui . Dialog ( )
  ii11iIi1I . ok ( i11 , "Error Deleting Packages please visit Kodi Support Group, GenieTv on facebook" )
 return
 if 63 - 63: Ooo00oOo00o + o0oO0
 if 3 - 3: I1IiI - O0oO / OoOO . O0 * o0oO0 / ii11ii1ii
 if 18 - 18: o00O0oo
 if 74 - 74: o00O0oo + ii11ii1ii + OOOo0
 if 37 - 37: IIII
 if 97 - 97: OOooOOo / IIII + I1IiI + Ooo00oOo00o % O0oO
 if 18 - 18: OOOo0 - I1IiI
 if 18 - 18: OoOO0ooOOoo0O + Ooo00oOo00o * OoOO - OoOO . ii11ii1ii * o0000oOoOoO0o
 if 95 - 95: ii11ii1ii / I1IiI
def i1II11iI1i ( url ) :
 print '###' + i11 + ' - DELETING PACKAGES###'
 iI1ii = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' , '' ) )
 try :
  for iI111i1II , iIIIiIi , OO0O0 in os . walk ( iI1ii ) :
   iI1iI = 0
   iI1iI += len ( OO0O0 )
   if 94 - 94: OoOoOO00 / i1IIi * i1IIi + o0oO0 - o0oO0 % OOooOOo
   if 12 - 12: O0oO / I1IiI . i11iIiiIii * i11iIiiIii
   if iI1iI > 0 :
    if 68 - 68: IIII * Ooo00oOo00o . o0000oOoOoO0o / o00O0oo . OOooOOo - i11iIiiIii
    ii11iIi1I = xbmcgui . Dialog ( )
    if ii11iIi1I . yesno ( "Delete Package Cache Files" , str ( iI1iI ) + " files found" , "Do you want to delete them?" ) :
     if 49 - 49: Oo / o00O0oo % o0000oOoOoO0o + OoOO - Ooo00oOo00o
     for O0ooO0Oo00o in OO0O0 :
      os . unlink ( os . path . join ( iI111i1II , O0ooO0Oo00o ) )
     for o000O0O in iIIIiIi :
      shutil . rmtree ( os . path . join ( iI111i1II , o000O0O ) )
     ii11iIi1I = xbmcgui . Dialog ( )
     ii11iIi1I . ok ( i11 , "       Deleting Packages all done" )
    else :
     pass
   else :
    ii11iIi1I = xbmcgui . Dialog ( )
    ii11iIi1I . ok ( i11 , "       No Packages to DELETE" )
 except :
  ii11iIi1I = xbmcgui . Dialog ( )
  ii11iIi1I . ok ( i11 , "Error Deleting Packages please visit Kodi Support Group, GenieTv on facebook" )
 return
 II1iOOoOooO0o ( url )
 if 13 - 13: OoOoOO00
 if 83 - 83: OoooooooOO . OOOo0 + o00O0oo * O0 / OoOO
 if 8 - 8: i1IIi + OoOoOO00 / o00O0oo + ii11ii1ii % o00O0oo - iIii1I11I1II1
 if 29 - 29: Oo + OoOoOO00
 if 95 - 95: OoOO
 if 48 - 48: o0000oOoOoO0o / iIii1I11I1II1 % OoOoOO00
 if 39 - 39: i1IIi . ii11ii1ii / o0000oOoOoO0o / o0000oOoOoO0o
 if 100 - 100: OoooooooOO - OoooooooOO + IIII
 if 32 - 32: I1IiI * OOooOOo / OoooooooOO
def oOooo00OOO000 ( url , name ) :
 o0oO00000 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 OooOOooo = os . path . join ( o0oO00000 , 'advancedsettings.xml' )
 ii11iIi1I = xbmcgui . Dialog ( )
 O00oOoo00O = os . path . join ( o0oO00000 , 'advancedsettings.xml.bak' )
 if os . path . exists ( O00oOoo00O ) == False :
  if ii11iIi1I . yesno ( "Back Up Original" , 'Have You Backed Up Your Original?' , '' , "[B][COLOR red]     AS YOU CANNOT GO BACK !!![/B][/COLOR]" ) :
   print '###' + i11 + ' - ADVANCED XML###'
   o0oO00000 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
   OooOOooo = os . path . join ( o0oO00000 , 'advancedsettings.xml' )
   try :
    os . remove ( OooOOooo )
    print '=== GenieTv - REMOVING    ' + str ( OooOOooo ) + '    ==='
   except :
    pass
   iI1i111I1Ii = I11 . http_GET ( url ) . content
   ooO0oOOooOo0 = open ( OooOOooo , "w" )
   ooO0oOOooOo0 . write ( iI1i111I1Ii )
   ooO0oOOooOo0 . close ( )
   print '=== GenieTv - WRITING NEW    ' + str ( OooOOooo ) + '    ==='
   ii11iIi1I = xbmcgui . Dialog ( )
   ii11iIi1I . ok ( i11 , "       Done Adding new Advanced XML" )
 else :
  print '###' + i11 + ' - ADVANCED XML###'
  o0oO00000 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
  OooOOooo = os . path . join ( o0oO00000 , 'advancedsettings.xml' )
  try :
   os . remove ( OooOOooo )
   print '=== GenieTv - REMOVING    ' + str ( OooOOooo ) + '    ==='
  except :
   pass
  iI1i111I1Ii = I11 . http_GET ( url ) . content
  ooO0oOOooOo0 = open ( OooOOooo , "w" )
  ooO0oOOooOo0 . write ( iI1i111I1Ii )
  ooO0oOOooOo0 . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( OooOOooo ) + '    ==='
  ii11iIi1I = xbmcgui . Dialog ( )
  ii11iIi1I . ok ( i11 , "       Done Adding new Advanced XML" )
 return
 if 25 - 25: i11iIiiIii + ii11ii1ii - OoooooooOO . O0 % O0oO
def oOOO ( url , name ) :
 print '###' + i11 + ' - CHECK ADVANCE XML###'
 o0oO00000 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 OooOOooo = os . path . join ( o0oO00000 , 'advancedsettings.xml' )
 try :
  ooO0oOOooOo0 = open ( OooOOooo ) . read ( )
  if 'zero' in ooO0oOOooOo0 :
   name = '0CACHE'
  elif 'tuxen' in ooO0oOOooOo0 :
   name = 'TUXENS'
  elif 'muckys' in ooO0oOOooOo0 :
   name = 'MUCKYS'
  elif 'p2p1' in ooO0oOOooOo0 :
   name = '1st P2P RECOMMENDED'
  elif 'p2p2' in ooO0oOOooOo0 :
   name = '2nd P2P RECOMMENDED'
  elif 'mikey' in ooO0oOOooOo0 :
   name = 'MIKEY1234'
 except :
  name = "NO ADVANCED"
 ii11iIi1I = xbmcgui . Dialog ( )
 ii11iIi1I . ok ( i11 , "[COLOR yellow]YOU HAVE[/COLOR] " + name + "[COLOR yellow] XML SETTINGS SETUP[/COLOR]" )
 return
 if 54 - 54: OoOO / iIii1I11I1II1 / OoooooooOO . i1IIi - I1IiI
def Oo00o0OOo0OO ( url ) :
 print '###' + i11 + ' - DELETING ADVANCE XML###'
 o0oO00000 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 OooOOooo = os . path . join ( o0oO00000 , 'advancedsettings.xml' )
 try :
  os . remove ( OooOOooo )
  ii11iIi1I = xbmcgui . Dialog ( )
  print '=== GenieTv - DELETING    ' + str ( OooOOooo ) + '    ==='
  ii11iIi1I . ok ( i11 , "       Remove Advanced Settings Sucessfull" )
 except :
  ii11iIi1I = xbmcgui . Dialog ( )
  ii11iIi1I . ok ( i11 , "       No Advanced Settings To Remove" )
 return
 if 18 - 18: o0oO0 - IIII / OoOoOO00 / ii11ii1ii
 if 31 - 31: O0oO * OOOo0 + o0oO0
 if 48 - 48: O0
 if 44 - 44: Ooo00oOo00o * OoOO
 if 54 - 54: o00O0oo % i1IIi
 if 51 - 51: iIii1I11I1II1 - OOOo0
 if 61 - 61: OoooooooOO . o00O0oo % OoOO * OoooooooOO
 if 96 - 96: o00O0oo - OoOoOO00 % I1IiI * OOOo0 * OOOo0 . Oo
 if 75 - 75: Oo + o00O0oo + Ooo00oOo00o
 if 97 - 97: o0oO0 % i11iIiiIii % o0000oOoOoO0o
def IIi1ioO0o ( url = 'http://www.iplocation.net/' , inc = 1 ) :
 OOO00O = re . compile ( "<td width='80'>(.+?)</td><td>(.+?)</td><td>(.+?)</td><td>.+?</td><td>(.+?)</td>" ) . findall ( I11 . http_GET ( url ) . content )
 for i1I1iI1 , oOOoOiii1i1Iiiiiii , OOoo0 , Ii11I1iIIi in OOO00O :
  if inc < 2 : ii11iIi1I = xbmcgui . Dialog ( ) ; ii11iIi1I . ok ( 'Check My IP' , "[B][COLOR gold]Your IP Address is: [/COLOR][/B] %s" % i1I1iI1 , '[B][COLOR gold]Your IP is based in: [/COLOR][/B] %s' % OOoo0 , '[B][COLOR gold]Your Service Provider is:[/COLOR][/B] %s' % Ii11I1iIIi )
  inc = inc + 1
  if 68 - 68: o0000oOoOoO0o / iIii1I11I1II1 . Oo + i11iIiiIii + OOooOOo
  if 92 - 92: Ooo00oOo00o . OOooOOo . o00O0oo % I1IiI
  if 58 - 58: ii11ii1ii % o00O0oo * o00O0oo - oO0o0ooO0
  if 9 - 9: o0oO0 - o00O0oo % OoOoOO00 + IIII + OoOO0ooOOoo0O % O0
  if 65 - 65: OoOO0ooOOoo0O - Ooo00oOo00o % i11iIiiIii
  if 58 - 58: oO0o0ooO0
  if 2 - 2: OoOoOO00 + i1IIi
  if 68 - 68: OoOO0ooOOoo0O + o00O0oo
  if 58 - 58: IIII * o00O0oo . i1IIi
def i11I1iiii ( url , name ) :
 ii11iIi1I = xbmcgui . Dialog ( )
 if ii11iIi1I . yesno ( "GenieTv" , '                                    Install Latest .ini File' ) :
  print '###' + i11 + ' - CUSTOM FTV INI###'
  o0oO00000 = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/script.ftvguide' , '' ) )
  OooOOooo = os . path . join ( o0oO00000 , 'addons2.ini' )
  iI1i111I1Ii = I11 . http_GET ( url ) . content
  ooO0oOOooOo0 = open ( OooOOooo , "w" )
  ooO0oOOooOo0 . write ( iI1i111I1Ii )
  ooO0oOOooOo0 . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( OooOOooo ) + '    ==='
  ii11iIi1I = xbmcgui . Dialog ( )
  ii11iIi1I . ok ( i11 , "                               Done Adding New .ini File" )
 return
 if 31 - 31: O0oO / Oo / iIii1I11I1II1
def oOO00OOOoO0o ( url , name ) :
 ii11iIi1I = xbmcgui . Dialog ( )
 if ii11iIi1I . yesno ( "GenieTv" , '                               Install Custom Settings' ) :
  print '###' + i11 + ' - CUSTOM FTV SETTINGS###'
  o0oO00000 = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/script.ftvguide' , '' ) )
  OooOOooo = os . path . join ( o0oO00000 , 'settings.xml' )
  iI1i111I1Ii = I11 . http_GET ( url ) . content
  ooO0oOOooOo0 = open ( OooOOooo , "w" )
  ooO0oOOooOo0 . write ( iI1i111I1Ii )
  ooO0oOOooOo0 . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( OooOOooo ) + '    ==='
  ii11iIi1I = xbmcgui . Dialog ( )
  ii11iIi1I . ok ( i11 , "                               Done Adding New Settings" )
 return
 if 18 - 18: iIii1I11I1II1 % iIii1I11I1II1 % OoOO + OOOo0 % o0oO0 / o00O0oo
 if 36 - 36: I1IiI . i11iIiiIii
def oO00O0o0oOOO ( ) :
 try :
  ooooOoo00 = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/script.ftvguide' , '' ) )
  if os . path . exists ( ooooOoo00 ) == True :
   ii11iIi1I = xbmcgui . Dialog ( )
   if ii11iIi1I . yesno ( "GenieTv" , "                               Delete FTV Guide Database" ) :
    IIIIii1111i1 = os . path . join ( ooooOoo00 , "source.db" )
    os . unlink ( IIIIii1111i1 )
  ii11iIi1I . ok ( "GenieTv" , "                                     FTV Database Reset" )
 except :
  ii11iIi1I = xbmcgui . Dialog ( )
  ii11iIi1I . ok ( i11 , "               Error Deleting Database No Database To Delete" )
 return
 if 11 - 11: I1IiI
 if 31 - 31: OoOoOO00 * o00O0oo / IIII / i11iIiiIii
 if 88 - 88: Oo . OOooOOo - i11iIiiIii . O0 * iIii1I11I1II1 * I1IiI
 if 99 - 99: iIii1I11I1II1 - OoOO - I1IiI / iIii1I11I1II1 * Oo - OoOO
 if 72 - 72: IIII % i1IIi / iIii1I11I1II1
def O0ii1ii1ii ( url ) :
 O00o0O = urllib2 . Request ( url )
 O00o0O . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
 O00oOo0O0o00O = urllib2 . urlopen ( O00o0O )
 iI1i111I1Ii = O00oOo0O0o00O . read ( )
 O00oOo0O0o00O . close ( )
 return iI1i111I1Ii
 if 95 - 95: O0 . Ooo00oOo00o
 if 89 - 89: i1IIi
 if 19 - 19: o0oO0 / OOooOOo % IIII - o00O0oo
 if 14 - 14: ii11ii1ii - i11iIiiIii * O0oO
 if 39 - 39: OoooooooOO
 if 19 - 19: i11iIiiIii
 if 80 - 80: OOOo0
def oO0OOo ( params ) :
 plugintools . log ( "freshstart.main_list " + repr ( params ) ) ; Oo0oo0OOO0OOoOO = plugintools . message_yes_no ( i11 , "Do you wish to restore your" , "Kodi configuration to default settings?" )
 if Oo0oo0OOO0OOoOO :
  oOoOII1i1 = xbmcaddon . Addon ( id = oOOoo00O0O ) . getAddonInfo ( 'path' ) ; oOoOII1i1 = xbmc . translatePath ( oOoOII1i1 ) ;
  o0o0oo0OOo0O0 = os . path . join ( oOoOII1i1 , ".." , ".." ) ; o0o0oo0OOo0O0 = os . path . abspath ( o0o0oo0OOo0O0 ) ; plugintools . log ( "freshstart.main_list xbmcPath=" + o0o0oo0OOo0O0 ) ; iIIiiII11i1I1 = False
  try :
   for iI111i1II , iIIIiIi , OO0O0 in os . walk ( o0o0oo0OOo0O0 , topdown = True ) :
    iIIIiIi [ : ] = [ o000O0O for o000O0O in iIIIiIi if o000O0O not in Oo0oO0ooo ]
    for i1Oo00 in OO0O0 :
     try : os . remove ( os . path . join ( iI111i1II , i1Oo00 ) )
     except :
      if i1Oo00 not in [ "Addons15.db" , "MyVideos75.db" , "Textures13.db" , "xbmc.log" ] : iIIiiII11i1I1 = True
      plugintools . log ( "Error removing " + iI111i1II + " " + i1Oo00 )
    for i1Oo00 in iIIIiIi :
     try : os . rmdir ( os . path . join ( iI111i1II , i1Oo00 ) )
     except :
      if i1Oo00 not in [ "Database" , "userdata" ] : iIIiiII11i1I1 = True
      plugintools . log ( "Error removing " + iI111i1II + " " + i1Oo00 )
   if not iIIiiII11i1I1 : plugintools . log ( "freshstart.main_list All user files removed, you now have a clean install" ) ; plugintools . message ( i11 , "The process is complete, you're now back to a fresh Kodi configuration with GenieTv!" , "Please reboot your system or restart Kodi in order for the changes to be applied." )
   else : plugintools . log ( "freshstart.main_list User files partially removed" ) ; plugintools . message ( i11 , "The process is complete, you're now back to a fresh Kodi configuration with GenieTv" , "Please reboot your system or restart Kodi in order for the changes to be applied." )
  except : plugintools . message ( i11 , "Problem found" , "Your settings has not been changed" ) ; import traceback ; plugintools . log ( traceback . format_exc ( ) ) ; plugintools . log ( "freshstart.main_list NOT removed" )
  plugintools . add_item ( action = "" , title = "Now Exit Kodi" , folder = False )
 else : plugintools . message ( i11 , "Your settings" , "has not been changed" ) ; plugintools . add_item ( action = "" , title = "Done" , folder = False )
 I111i1i1111 ( )
 if 28 - 28: OoOoOO00 * o0oO0 * I1IiI * O0oO . OoOoOO00 . ii11ii1ii
 if 32 - 32: o0oO0 - Ooo00oOo00o . oO0o0ooO0 . oO0o0ooO0 % i1IIi * o00O0oo
 if 65 - 65: oO0o0ooO0 / o0oO0 . OoOoOO00
def o0oO00oooo ( ) :
 ooo0Oo00O = [ ]
 I1iII1 = sys . argv [ 2 ]
 if len ( I1iII1 ) >= 2 :
  Ooo0OOO0O00 = sys . argv [ 2 ]
  Ii1iiII11ii1 = Ooo0OOO0O00 . replace ( '?' , '' )
  if ( Ooo0OOO0O00 [ len ( Ooo0OOO0O00 ) - 1 ] == '/' ) :
   Ooo0OOO0O00 = Ooo0OOO0O00 [ 0 : len ( Ooo0OOO0O00 ) - 2 ]
  iIi11I1II = Ii1iiII11ii1 . split ( '&' )
  ooo0Oo00O = { }
  for iii1IIIiiiI in range ( len ( iIi11I1II ) ) :
   oO00Oo0O0 = { }
   oO00Oo0O0 = iIi11I1II [ iii1IIIiiiI ] . split ( '=' )
   if ( len ( oO00Oo0O0 ) ) == 2 :
    ooo0Oo00O [ oO00Oo0O0 [ 0 ] ] = oO00Oo0O0 [ 1 ]
    if 91 - 91: o0000oOoOoO0o + o00O0oo + IIII
 return ooo0Oo00O
 if 58 - 58: oO0o0ooO0 * o00O0oo - i11iIiiIii % ii11ii1ii
i1iIiIIi = base64 . decodestring ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20v' )
o00o0 = base64 . decodestring ( 'L3N0b3JhZ2UvZW11bGF0ZWQvMA==' )
oO0o00oo0 = base64 . decodestring ( 'L2dlbmllLnR4dA==' )
I11O0O0o = base64 . decodestring ( 'LmFyY2hpdGVjdHMueDEwaG9zdC5jb20vdGVzdC93aC50eHQ=' )
i11i1ii1I = base64 . decodestring ( 'aHR0cDovL2ZpeGVzLmFyY2hpdGVjdHMueDEwaG9zdC5jb20vZml4ZXMudHh0' )
i1i1i1I = base64 . decodestring ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vYXBwcy9hcHBzLnhtbA==' )
OO0iiiii1iiIIii = base64 . decodestring ( 'L2FkZG9ucy9uZXcudHh0' )
i111II = base64 . decodestring ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vdm9kL3ZvZC5waHA=' )
oOoO000 = base64 . decodestring ( 'L2FkZG9ucy9pcHR2LnR4dA==' )
oOO00o0O0 = base64 . decodestring ( 'L2FkZG9ucy92aWRlby50eHQ=' )
IiiI1iii1iIiiI = base64 . decodestring ( 'L2FkZG9ucy9zcG9ydHMudHh0' )
oOo = base64 . decodestring ( 'L2FkZG9ucy9raWRzLnR4dA==' )
iIii1Oo = base64 . decodestring ( 'L2FkZG9ucy9tdXNpYy50eHQ=' )
i111I1 = base64 . decodestring ( 'L2FkZG9ucy9wcm9ncmFtcy50eHQ=' )
iiiI1Ii1 = base64 . decodestring ( 'L2FkZG9ucy94eHgudHh0' )
o0OOOO = base64 . decodestring ( 'L2FkZG9ucy9yZXBvLnR4dA==' )
iiI = base64 . decodestring ( 'L2FkZG9ucy9wYWNrcy50eHQ=' )
O0o0 = base64 . decodestring ( 'L2FkZG9ucy9za2lucy50eHQ=' )
OoO0O00O0oo0O = base64 . decodestring ( 'L2FkZG9ucy9hcnQudHh0' )
OooO0OO = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2dvdGhhbS50eHQ=' )
O0o0oO = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2hlbGl4LnR4dA==' )
iI1i11 = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2lzZW5nYXJkLnR4dA==' )
oo0O00o0O0Oo = base64 . decodestring ( 'L2FkZG9ucy9SU1MudHh0' )
i1II1I = base64 . decodestring ( 'Q1VOVA==' )
def iiiiiIIii ( name , url , mode , iconimage , fanart , description , showcontext = True , allinfo = { } ) :
 O00ooOo = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 oOO0o00O = True
 oOoO = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 oOoO . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 oOoO . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  i1II11i1iI1 = [ ]
  if showcontext == 'fav' :
   i1II11i1iI1 . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in oOoOooOo0o0 :
   i1II11i1iI1 . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fanart=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , urllib . quote_plus ( fanart ) , mode ) ) )
  oOoO . addContextMenuItems ( i1II11i1iI1 )
 oOO0o00O = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = O00ooOo , listitem = oOoO , isFolder = True )
 return oOO0o00O
 if 64 - 64: OoooooooOO + Oo
def o0OOoo0OO0OOO ( name , url , mode , iconimage , fanart , description ) :
 O00ooOo = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 oOO0o00O = True
 oOoO = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 oOoO . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 oOoO . setProperty ( "Fanart_Image" , fanart )
 oOO0o00O = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = O00ooOo , listitem = oOoO , isFolder = False )
 return oOO0o00O
 if 27 - 27: oO0o0ooO0 + o00O0oo * OOOo0 * ii11ii1ii . O0oO
 if 71 - 71: OOooOOo % OoOO0ooOOoo0O + O0 / ii11ii1ii
Ooo0OOO0O00 = o0oO00oooo ( )
ooOOO00Ooo = None
i1Oo00 = None
ooO000O = None
OOoOO0oo0ooO = None
O00O0oOO00O00 = None
III1iII1I1ii = None
o0OO0 = None
if 11 - 11: IIII % ii11ii1ii / o0oO0 . i11iIiiIii + OoOO0ooOOoo0O - OoOoOO00
if 50 - 50: i1IIi * OoOO / i11iIiiIii / i11iIiiIii / OoOO
try :
 o0OO0 = int ( Ooo0OOO0O00 [ "fav_mode" ] )
except :
 pass
 if 84 - 84: ii11ii1ii - oO0o0ooO0 + ii11ii1ii
try :
 ooOOO00Ooo = urllib . unquote_plus ( Ooo0OOO0O00 [ "url" ] )
except :
 pass
try :
 i1Oo00 = urllib . unquote_plus ( Ooo0OOO0O00 [ "name" ] )
except :
 pass
try :
 OOoOO0oo0ooO = urllib . unquote_plus ( Ooo0OOO0O00 [ "iconimage" ] )
except :
 pass
try :
 ooO000O = int ( Ooo0OOO0O00 [ "mode" ] )
except :
 pass
try :
 O00O0oOO00O00 = urllib . unquote_plus ( Ooo0OOO0O00 [ "fanart" ] )
except :
 pass
try :
 III1iII1I1ii = urllib . unquote_plus ( Ooo0OOO0O00 [ "description" ] )
except :
 pass
 if 63 - 63: o0000oOoOoO0o * o0oO0 % OoOoOO00 % O0oO + OOOo0 * Oo
 if 96 - 96: IIII
print str ( II11iiii1Ii ) + ': ' + str ( iiI1IiI )
print "Mode: " + str ( ooO000O )
print "URL: " + str ( ooOOO00Ooo )
print "Name: " + str ( i1Oo00 )
print "IconImage: " + str ( OOoOO0oo0ooO )
if 99 - 99: iIii1I11I1II1 - o0oO0
if 79 - 79: OOOo0 + OoOO % o0000oOoOoO0o % OoOO
def Oooo0Ooo000 ( content , viewType ) :
 if 56 - 56: ii11ii1ii + OoOO . Ooo00oOo00o + OoooooooOO * ii11ii1ii - O0
 if content :
  xbmcplugin . setContent ( int ( sys . argv [ 1 ] ) , content )
 if o0oOoO00o . getSetting ( 'auto-view' ) == 'true' :
  xbmc . executebuiltin ( "Container.SetViewMode(%s)" % o0oOoO00o . getSetting ( viewType ) )
  if 35 - 35: OoOO0ooOOoo0O . o0000oOoOoO0o . O0oO - o0000oOoOoO0o % o0000oOoOoO0o + O0oO
  if 99 - 99: OOooOOo + OoOO0ooOOoo0O
if ooO000O == None :
 OOO00 ( )
 if 34 - 34: O0oO * OOooOOo . OOOo0 % i11iIiiIii
elif ooO000O == 1 :
 O0o ( ooOOO00Ooo )
 if 61 - 61: iIii1I11I1II1 + OoOO * o0000oOoOoO0o - i1IIi % OoOO
elif ooO000O == 44 :
 oooooo0OO ( ooOOO00Ooo )
 if 76 - 76: OoOO / I1IiI
elif ooO000O == 2 :
 ii111I ( )
 if 12 - 12: O0oO
elif ooO000O == 3 :
 o0oooOO00 ( )
 if 58 - 58: Ooo00oOo00o + iIii1I11I1II1 % O0 + o0000oOoOoO0o + I1IiI * OoooooooOO
elif ooO000O == 21 :
 IIiiIiiI ( )
 if 41 - 41: OoOO * OOOo0
elif ooO000O == 4 :
 Ii1iI111II1I1 ( )
 if 76 - 76: OoOO . O0 * OoooooooOO + o0oO0
elif ooO000O == 5 :
 ii1ii111 ( i1Oo00 , ooOOO00Ooo , III1iII1I1ii )
 if 53 - 53: Oo
elif ooO000O == 6 :
 o0o0O00oOo ( ooOOO00Ooo )
 if 3 - 3: IIII - OoooooooOO * OoooooooOO - OOOo0 / O0oO * ii11ii1ii
elif ooO000O == 7 :
 oOooo00OOO000 ( ooOOO00Ooo , i1Oo00 )
 if 58 - 58: IIII % iIii1I11I1II1 / i11iIiiIii % OOooOOo . O0oO * oO0o0ooO0
elif ooO000O == 8 :
 oOOO ( ooOOO00Ooo , i1Oo00 )
 if 32 - 32: OoooooooOO + OOooOOo
elif ooO000O == 9 :
 FIXREPOSADDONS ( ooOOO00Ooo )
 if 91 - 91: o0oO0 - O0oO * O0oO
elif ooO000O == 10 :
 O0o0O0 ( )
 if 55 - 55: iIii1I11I1II1 + OOOo0 - Oo
elif ooO000O == 11 :
 Oo00o0OOo0OO ( ooOOO00Ooo )
 if 24 - 24: Ooo00oOo00o / O0oO + oO0o0ooO0 * o0000oOoOoO0o * oO0o0ooO0
elif ooO000O == 12 :
 IIi1ioO0o ( )
 if 10 - 10: OOOo0 - ii11ii1ii - Oo - OOooOOo
elif ooO000O == 13 :
 OOo0oO0o ( )
 if 21 - 21: OoooooooOO + O0oO
elif ooO000O == 14 :
 II1iOOoOooO0o ( ooOOO00Ooo )
 if 43 - 43: i11iIiiIii . ii11ii1ii . OoOO
elif ooO000O == 15 :
 oooO ( )
 if 31 - 31: o00O0oo % OOooOOo % O0oO . ii11ii1ii / OOooOOo * OoOO
elif ooO000O == 16 :
 i11I1iiii ( ooOOO00Ooo , i1Oo00 )
 if 74 - 74: OOOo0 . o0oO0 / oO0o0ooO0 . IIII
elif ooO000O == 17 :
 oOO00OOOoO0o ( ooOOO00Ooo , i1Oo00 )
 if 74 - 74: Oo / O0oO % O0oO . IIII
elif ooO000O == 18 :
 oO00O0o0oOOO ( )
 if 72 - 72: i1IIi
elif ooO000O == 19 :
 o0oO000oo ( i1Oo00 , ooOOO00Ooo , III1iII1I1ii )
 if 21 - 21: O0oO . OoOO0ooOOoo0O / i11iIiiIii * i1IIi
elif ooO000O == 40 :
 iIIII ( i1Oo00 , ooOOO00Ooo , III1iII1I1ii )
 if 82 - 82: o0oO0 * Oo % i11iIiiIii * i1IIi . OoOO0ooOOoo0O
elif ooO000O == 42 :
 i1II1I1Iii1 ( i1Oo00 , ooOOO00Ooo , III1iII1I1ii )
 if 89 - 89: IIII - i1IIi - IIII
elif ooO000O == 43 :
 I1ii11 ( i1Oo00 , ooOOO00Ooo , III1iII1I1ii )
 if 74 - 74: Ooo00oOo00o % Ooo00oOo00o
elif ooO000O == 20 :
 OOO0000oO ( ooOOO00Ooo )
 if 28 - 28: I1IiI % OoOO - OoOO0ooOOoo0O + OoOO0ooOOoo0O + OoOO / iIii1I11I1II1
elif ooO000O == 22 :
 iiIIi11ii1Ii ( ooOOO00Ooo )
 if 91 - 91: OOOo0 / OoOoOO00 * OoOO0ooOOoo0O
elif ooO000O == 23 :
 Ooooo0O0 ( ooOOO00Ooo )
 if 94 - 94: OoOoOO00 - iIii1I11I1II1 - iIii1I11I1II1
elif ooO000O == 24 :
 O0o0O0OO0Oo00OO0oo ( ooOOO00Ooo )
 if 83 - 83: ii11ii1ii * iIii1I11I1II1 + I1IiI * i1IIi . OoooooooOO % o00O0oo
elif ooO000O == 25 :
 Oo0ooIi ( ooOOO00Ooo )
 if 81 - 81: Ooo00oOo00o - iIii1I11I1II1
elif ooO000O == 26 :
 IiiIiiIIII ( ooOOO00Ooo )
 if 60 - 60: O0oO
elif ooO000O == 27 :
 oOoOoOOo00Ooo0O ( ooOOO00Ooo )
 if 77 - 77: OOOo0 / ii11ii1ii
elif ooO000O == 28 :
 oOiI1I ( ooOOO00Ooo )
 if 95 - 95: O0oO * i1IIi + OoOO
elif ooO000O == 29 :
 O0O0oOO ( ooOOO00Ooo )
 if 40 - 40: OoOoOO00
elif ooO000O == 30 :
 ooo ( ooOOO00Ooo )
 if 7 - 7: OoOO0ooOOoo0O / Ooo00oOo00o
elif ooO000O == 31 :
 oOoOO0O00o ( ooOOO00Ooo )
 if 88 - 88: i1IIi
elif ooO000O == 32 :
 OooOo ( )
 if 53 - 53: o0oO0 . OoOO0ooOOoo0O . OOooOOo + OoOO
elif ooO000O == 33 :
 I1i11 ( )
 if 17 - 17: iIii1I11I1II1 + i1IIi . ii11ii1ii + o00O0oo % i1IIi . OoOO
elif ooO000O == 35 :
 Oo00O ( ooOOO00Ooo )
 if 57 - 57: OoOO
elif ooO000O == 34 :
 I1i1i1 ( ooOOO00Ooo )
 if 92 - 92: OoOoOO00 - Ooo00oOo00o - OoOO0ooOOoo0O % OOOo0 - I1IiI * O0oO
elif ooO000O == 36 :
 o0OOOOooo ( ooOOO00Ooo )
 if 16 - 16: iIii1I11I1II1 + OoooooooOO - o0oO0 * IIII
elif ooO000O == 37 :
 ii1I1IIii11 ( ooOOO00Ooo )
 if 37 - 37: oO0o0ooO0
elif ooO000O == 38 :
 oo0000ooooO0o ( ooOOO00Ooo )
 if 15 - 15: OOooOOo % Ooo00oOo00o / oO0o0ooO0
elif ooO000O == 41 :
 oO0OOo ( Ooo0OOO0O00 )
 if 36 - 36: Ooo00oOo00o + Ooo00oOo00o % Oo + Oo / i1IIi % i1IIi
elif ooO000O == 39 :
 iI1111i1i11Ii ( ooOOO00Ooo )
 if 20 - 20: OoOO0ooOOoo0O * OoOO
elif ooO000O == 45 :
 TEXTS ( )
 if 91 - 91: Ooo00oOo00o % i1IIi - iIii1I11I1II1 . OoOO0ooOOoo0O
elif ooO000O == 46 :
 Iii ( )
 if 31 - 31: OoOO % i1IIi . OoooooooOO - OOooOOo + OoooooooOO
elif ooO000O == 47 :
 GEVID ( )
 if 45 - 45: OoOO0ooOOoo0O + o0000oOoOoO0o / OoooooooOO - o00O0oo + OoooooooOO
elif ooO000O == 48 :
 OO0oo0O ( i1Oo00 , ooOOO00Ooo , III1iII1I1ii )
 if 42 - 42: iIii1I11I1II1 * OOOo0 * O0oO
elif ooO000O == 49 :
 I1iiii1I ( )
 if 62 - 62: OoOO0ooOOoo0O * O0 % IIII . IIII . OOOo0
elif ooO000O == 222 :
 iI1iIIIIIiIi1 ( ooOOO00Ooo )
 if 91 - 91: i1IIi . oO0o0ooO0
elif ooO000O == 333 :
 ii1IIiI1iI1i ( ooOOO00Ooo )
 if 37 - 37: oO0o0ooO0 - o0000oOoOoO0o + iIii1I11I1II1 / O0oO - Ooo00oOo00o . OOooOOo
 if 62 - 62: ii11ii1ii
elif ooO000O == 1001 :
 I11iI1 ( )
 if 47 - 47: O0oO % OoOO0ooOOoo0O * Ooo00oOo00o . iIii1I11I1II1 % Oo + OoooooooOO
elif ooO000O == 1005 :
 O00oo0oOoO00O ( )
 if 2 - 2: O0oO % OoooooooOO - o0oO0 * ii11ii1ii * IIII
elif ooO000O == 1007 :
 Iii1iIiI1I1I1 ( ooOOO00Ooo )
 if 99 - 99: iIii1I11I1II1 . Oo / o0oO0 . OoOO0ooOOoo0O % OOOo0 * o0000oOoOoO0o
elif ooO000O == 1010 :
 ii ( ooOOO00Ooo )
 if 95 - 95: OoOO
elif ooO000O == 1011 :
 Oo0 ( ooOOO00Ooo )
 if 80 - 80: IIII
elif ooO000O == 1030 :
 OOO00ii1Ii111I11I ( )
 if 42 - 42: OoooooooOO * OoOoOO00
elif ooO000O == 1031 :
 o0OoOoo ( ooOOO00Ooo , OOoOO0oo0ooO )
 if 53 - 53: O0oO + i1IIi . Ooo00oOo00o / i11iIiiIii + o00O0oo % I1IiI
elif ooO000O == 1006 :
 Parse . ParseURL ( ooOOO00Ooo )
 if 9 - 9: o0oO0 . o0000oOoOoO0o - Oo . O0oO
elif ooO000O == 2030 :
 Parse . addonParseURL ( ooOOO00Ooo )
 if 39 - 39: OoOO0ooOOoo0O
elif ooO000O == 2031 :
 Parse . apkParseURL ( ooOOO00Ooo )
 if 70 - 70: IIII % Ooo00oOo00o % OOOo0
elif ooO000O == 1002 :
 iI1Ii11 ( ooOOO00Ooo )
 if 95 - 95: I1IiI - O0oO / O0 * OOOo0 - OOooOOo
elif ooO000O == 1003 :
 Ooo0 ( ooOOO00Ooo , OOoOO0oo0ooO )
 if 12 - 12: iIii1I11I1II1 % Oo . oO0o0ooO0 . IIII % i11iIiiIii
elif ooO000O == 1004 :
 IiiiIIi ( ooOOO00Ooo )
 if 2 - 2: OoOO * OoOO . I1IiI * o00O0oo * iIii1I11I1II1
elif ooO000O == 1008 :
 i1Iiii ( )
 if 13 - 13: o0000oOoOoO0o / O0 . i11iIiiIii * i1IIi % i11iIiiIii
elif ooO000O == 1009 :
 M3UPLAY ( ooOOO00Ooo )
 if 8 - 8: I1IiI - OoooooooOO
elif ooO000O == 2001 :
 oO00o00 ( ooOOO00Ooo )
 if 99 - 99: OoOoOO00 / IIII % OoooooooOO . i11iIiiIii
elif ooO000O == 1013 :
 I1i111iiIIIi ( )
 if 18 - 18: OOooOOo . o0oO0
elif ooO000O == 1014 :
 III11I1 ( )
 if 70 - 70: OoooooooOO . o0oO0 / OoOO . OoOO - OOooOOo
elif ooO000O == 1015 :
 OOOO0o0O ( ooOOO00Ooo )
 if 29 - 29: o0000oOoOoO0o % OoOO0ooOOoo0O - o0oO0
elif ooO000O == 1016 :
 o0o0O0oOOOooo ( ooOOO00Ooo )
 if 26 - 26: O0 . o0000oOoOoO0o + oO0o0ooO0 - o00O0oo . o0000oOoOoO0o
elif ooO000O == 1023 :
 Iii1I1111ii ( )
 if 2 - 2: ii11ii1ii . Oo * OoOO0ooOOoo0O % OoOoOO00 . oO0o0ooO0
elif ooO000O == 1024 :
 I1ii1I1iii1 ( )
 if 46 - 46: I1IiI + OOOo0 % OoooooooOO * i11iIiiIii - Oo
elif ooO000O == 1025 :
 iIiiiIIiii ( ooOOO00Ooo )
 if 47 - 47: oO0o0ooO0 * I1IiI * IIII
elif ooO000O == 4001 :
 II111ii1II1i ( )
 if 46 - 46: o00O0oo
elif ooO000O == 4002 :
 OoOo00o ( )
 if 42 - 42: iIii1I11I1II1
elif ooO000O == 4003 :
 O0o000Oo ( )
 if 32 - 32: Oo - o00O0oo . OoooooooOO - OoooooooOO - Oo . iIii1I11I1II1
elif ooO000O == 3000 :
 iiI1iIII1ii ( )
 if 34 - 34: Oo
elif ooO000O == 3001 :
 O0oo ( )
 if 31 - 31: i1IIi - o0000oOoOoO0o + O0oO + o0oO0 . o0oO0 . O0
elif ooO000O == 3002 :
 ooOooO00Oo ( ooOOO00Ooo )
 if 33 - 33: i1IIi / oO0o0ooO0 * Ooo00oOo00o
elif ooO000O == 3003 :
 ooO00o ( ooOOO00Ooo )
 if 2 - 2: OoOO . OoOO0ooOOoo0O
elif ooO000O == 3004 :
 o0oO0OO00ooOO ( ooOOO00Ooo )
 if 43 - 43: iIii1I11I1II1
elif ooO000O == 404 :
 OOOO00 ( i1Oo00 , ooOOO00Ooo , OOoOO0oo0ooO )
 if 29 - 29: IIII % o0oO0 + Ooo00oOo00o . i1IIi + OOOo0
elif ooO000O == 7030 :
 II11iIIii ( )
 if 24 - 24: O0oO / o00O0oo * ii11ii1ii - OoooooooOO / OOOo0 . OoOO
elif ooO000O == 7021 :
 oOooOOo00ooO ( i1Oo00 )
 if 98 - 98: i1IIi - oO0o0ooO0
elif ooO000O == 7022 :
 iIIi1 ( i1Oo00 )
 if 49 - 49: OOooOOo . o00O0oo . OoOO
elif ooO000O == 7000 :
 i111iI1 ( i1Oo00 , ooOOO00Ooo , img )
 if 9 - 9: IIII - OoOoOO00 * Ooo00oOo00o
elif ooO000O == 7050 :
 oOOoOOO0oOoo ( ooOOO00Ooo )
 if 78 - 78: iIii1I11I1II1 / O0 * OoOO / oO0o0ooO0 / I1IiI
elif ooO000O == 7051 :
 ooii11i ( ooOOO00Ooo )
 if 15 - 15: o0oO0 / OoOO
elif ooO000O == 7052 :
 OOOOoO ( ooOOO00Ooo )
 if 54 - 54: o0oO0 - iIii1I11I1II1 - o0000oOoOoO0o % o00O0oo / OoOoOO00
elif ooO000O == 7053 :
 Iii11111iiI ( ooOOO00Ooo )
 if 80 - 80: i11iIiiIii % iIii1I11I1II1 / i11iIiiIii
elif ooO000O == 7054 :
 CoolPlay ( ooOOO00Ooo )
 if 66 - 66: I1IiI . iIii1I11I1II1 * ii11ii1ii - o00O0oo - iIii1I11I1II1
elif ooO000O == 7060 :
 iiIi11I1IIiiii ( )
 if 28 - 28: I1IiI % OoooooooOO
elif ooO000O == 7061 :
 OoooOo0 ( ooOOO00Ooo )
 if 13 - 13: IIII . Oo - o0000oOoOoO0o / OoOO - Oo - OOOo0
elif ooO000O == 7063 :
 o0OI1 ( ooOOO00Ooo )
 if 84 - 84: OoOoOO00
elif ooO000O == 7062 :
 IiiIIiI1iI1 ( ooOOO00Ooo )
 if 57 - 57: O0 * iIii1I11I1II1 % O0 . OoooooooOO
elif ooO000O == 7064 :
 NATatozcat ( )
 if 53 - 53: o00O0oo / OOOo0 * o00O0oo + OOooOOo + OoOO - Oo
elif ooO000O == 7067 :
 OOoO0OOoO0ooo ( ooOOO00Ooo )
 if 16 - 16: Ooo00oOo00o % O0oO . i1IIi / ii11ii1ii - O0
elif ooO000O == 7066 :
 NATatozA ( ooOOO00Ooo )
 if 85 - 85: i1IIi . i1IIi
elif ooO000O == 7065 :
 ii11i1ii1 ( ooOOO00Ooo )
 if 16 - 16: OOOo0 - OoOO0ooOOoo0O % o00O0oo . OoOO0ooOOoo0O + ii11ii1ii % i11iIiiIii
elif ooO000O == 7070 :
 iiIi ( )
 if 59 - 59: i11iIiiIii - o0000oOoOoO0o
elif ooO000O == 7071 :
 DIZIlist ( ooOOO00Ooo )
 if 59 - 59: OoooooooOO * OOooOOo / O0oO
elif ooO000O == 7072 :
 DIZIpull ( ooOOO00Ooo )
 if 75 - 75: OOooOOo - OoooooooOO
elif ooO000O == 7073 :
 WATCHDIZI ( ooOOO00Ooo )
 if 21 - 21: OOOo0 + iIii1I11I1II1 / i11iIiiIii / OoOO
elif ooO000O == 7002 :
 ooIi111iII ( )
 if 66 - 66: OoooooooOO + oO0o0ooO0 . IIII % i1IIi
elif ooO000O == 7003 :
 o0o ( ooOOO00Ooo )
 if 58 - 58: OoOO0ooOOoo0O % oO0o0ooO0 * O0 + ii11ii1ii - IIII
elif ooO000O == 7004 :
 ii111iI1i1 ( ooOOO00Ooo )
 if 26 - 26: i1IIi / OOOo0 / o0000oOoOoO0o + o0000oOoOoO0o
elif ooO000O == 7020 :
 iII11II1II ( ooOOO00Ooo )
 if 46 - 46: O0oO % ii11ii1ii + o00O0oo
elif ooO000O == 7001 :
 OO0oO ( )
 if 67 - 67: iIii1I11I1II1 . i11iIiiIii . i11iIiiIii . i11iIiiIii / o0000oOoOoO0o + o0oO0
elif ooO000O == 7010 :
 i1iI1Ii11Ii1 ( ooOOO00Ooo )
 if 10 - 10: o0oO0 - Oo % OoOoOO00
elif ooO000O == 7011 :
 oooo0o0OOO0 ( ooOOO00Ooo )
 if 66 - 66: iIii1I11I1II1 . iIii1I11I1II1
elif ooO000O == 7012 :
 OOoO0OOOO0000O ( ooOOO00Ooo )
 if 46 - 46: O0oO * OoOO . o00O0oo * O0oO * iIii1I11I1II1 / o0000oOoOoO0o
elif ooO000O == 7013 :
 cnfTVPlay2 ( ooOOO00Ooo )
elif ooO000O == 7014 :
 CNF_Studio_Indexer . MV_Movies ( ooOOO00Ooo )
elif ooO000O == 7015 :
 CNF_Studio_Indexer . Movie_ByYear ( ooOOO00Ooo )
elif ooO000O == 7016 :
 CNF_Studio_Indexer . Resolve_CNF_Link ( i1Oo00 , ooOOO00Ooo , OOoOO0oo0ooO )
elif ooO000O == 7017 :
 CNF_Studio_Indexer . Search_Movie ( )
elif ooO000O == 7018 :
 IIOOO00o0 ( )
elif ooO000O == 7019 :
 CNF_Studio_Indexer . List_Movies ( ooOOO00Ooo )
elif ooO000O == 7020 :
 CNF_Studio_Indexer . Get_Movie_Page ( ooOOO00Ooo )
elif ooO000O == 7024 :
 CNF_Studio_Indexer . Box_Office ( ooOOO00Ooo )
 if 46 - 46: OoOoOO00 % ii11ii1ii . OoOO0ooOOoo0O . Oo / i11iIiiIii + Ooo00oOo00o
elif ooO000O == 8000 :
 O00O00OoO ( )
elif ooO000O == 8001 :
 oO0o0Oo ( )
elif ooO000O == 8002 :
 O0OooOO ( )
elif ooO000O == 8003 :
 III1IiI1i1i ( )
elif ooO000O == 8004 :
 iiIiii ( )
elif ooO000O == 8005 :
 Ooo000O00 ( )
elif ooO000O == 8006 :
 Iiii1Ii ( i1Oo00 , ooOOO00Ooo )
elif ooO000O == 8030 :
 ooo00Ooo ( ooOOO00Ooo )
elif ooO000O == 8045 :
 Oo0o ( ooOOO00Ooo )
elif ooO000O == 8046 :
 IiI1I1I ( ooOOO00Ooo )
elif ooO000O == 8047 :
 oO0o00ooO0OoO ( ooOOO00Ooo )
elif ooO000O == 8040 :
 IiiIiIi111iI1 ( )
elif ooO000O == 8041 :
 oOOO0o0ooOo ( ooOOO00Ooo )
elif ooO000O == 8042 :
 iI1i1iIi1iiII ( ooOOO00Ooo )
elif ooO000O == 8043 :
 yt . PlayVideo ( ooOOO00Ooo )
elif ooO000O == 8044 :
 o0OoO0000o ( ooOOO00Ooo )
elif ooO000O == 8060 :
 II1II1iI ( )
elif ooO000O == 8061 :
 OooooO ( ooOOO00Ooo )
elif ooO000O == 8064 :
 iI111i11iI1 ( )
elif ooO000O == 8065 :
 III1ii ( ooOOO00Ooo )
elif ooO000O == 8070 :
 O0oOo00O ( )
elif ooO000O == 8071 :
 i1I1I1i1i1i ( ooOOO00Ooo )
elif ooO000O == 7080 :
 ii1o0oo0Ooooo0 ( ooOOO00Ooo )
elif ooO000O == 8090 :
 ooooo0Oo0 ( )
elif ooO000O == 8091 :
 o0I1IIIi11ii11 ( ooOOO00Ooo )
elif ooO000O == 8092 :
 O0o0oo0oOO0oO ( ooOOO00Ooo )
elif ooO000O == 8081 :
 i1iI1i ( )
elif ooO000O == 8062 :
 I1ii1Ii1 ( ooOOO00Ooo )
elif ooO000O == 8063 :
 iIIIIi ( ooOOO00Ooo )
elif ooO000O == 8050 :
 iIiIIIIIii ( )
elif ooO000O == 8051 :
 OOo0 ( ooOOO00Ooo )
elif ooO000O == 8052 :
 oO0oo ( ooOOO00Ooo )
elif ooO000O == 8085 :
 Ii1i1 ( )
elif ooO000O == 8086 :
 i1iIIi11i111I ( ooOOO00Ooo )
elif ooO000O == 8087 :
 iiiIIIii ( ooOOO00Ooo )
elif ooO000O == 8088 :
 ooOoo00 ( ooOOO00Ooo , i1Oo00 )
elif ooO000O == 9000 :
 ooO0O00Oo0o ( )
elif ooO000O == 1111 :
 o0oOOoo0O ( )
elif ooO000O == 9001 :
 II11Ii111II1 ( )
elif ooO000O == 9002 :
 Ii ( )
elif ooO000O == 9003 :
 ii1IIiI1IIi ( )
elif ooO000O == 50 :
 i11IIIiI11 ( ooOOO00Ooo )
elif ooO000O == 9020 :
 champlist ( )
elif ooO000O == 9021 :
 oOoOo0o00o ( )
elif ooO000O == 9022 :
 iIIi1ooo0o0 ( )
elif ooO000O == 9023 :
 O00Oooo00 ( )
elif ooO000O == 9024 :
 I111 ( ooOOO00Ooo )
elif ooO000O == 9030 :
 iiIII1 ( ooOOO00Ooo )
elif ooO000O == 9031 :
 iI1111i ( ooOOO00Ooo )
elif ooO000O == 9032 :
 I1Ii1iIIIIi ( ooOOO00Ooo )
elif ooO000O == 9033 :
 iiiO000OOO ( ooOOO00Ooo )
elif ooO000O == 7085 :
 IiI11i1I11111 ( ooOOO00Ooo )
elif ooO000O == 7086 :
 II1i ( ooOOO00Ooo )
elif ooO000O == 7087 :
 Oo0oo ( III1iII1I1ii )
elif ooO000O == 9666 :
 i1II11iI1i ( ooOOO00Ooo )
elif ooO000O == 10100 : i1iIiIii ( )
elif ooO000O == 10105 : O0oOoo ( ooOOO00Ooo )
elif ooO000O == 10106 : o0OO0OOO0O ( ooOOO00Ooo )
elif ooO000O == 10104 : oo0OoOOooO ( ooOOO00Ooo )
elif ooO000O == 10107 : iiiI1I ( )
elif ooO000O == 10103 : i1III1iI ( ooOOO00Ooo )
elif ooO000O == 10108 : Ii1Ii1I ( ooOOO00Ooo )
elif ooO000O == 10107 : iiiI1I ( )
elif ooO000O == 10000 : Origin_Menu ( )
elif ooO000O == 10001 : oOIi111 ( )
elif ooO000O == 10002 : iiI1iI1I ( )
elif ooO000O == 10003 : oO0o000OoOoO0 ( )
elif ooO000O == 10004 : iiI11I1i1i1iI ( )
elif ooO000O == 10005 : I1i1i ( )
elif ooO000O == 10006 : oooo00 ( ooOOO00Ooo )
elif ooO000O == 10007 : I11I ( ooOOO00Ooo , OOoOO0oo0ooO )
elif ooO000O == 10008 : O0oo0O0 ( )
elif ooO000O == 10009 : o0OO0O0OO0oO0 ( )
elif ooO000O == 10010 : IIIiI1ii1IIi ( ooOOO00Ooo )
elif ooO000O == 10011 : iI1IiiiIiI1Ii ( ooOOO00Ooo )
elif ooO000O == 10012 : OO0 ( ooOOO00Ooo )
elif ooO000O == 10013 : i11i11 ( ooOOO00Ooo )
elif ooO000O == 10014 : ii1I11 ( )
elif ooO000O == 10015 : IiIiiI11111I1 ( )
elif ooO000O == 10016 : O0Oo ( ooOOO00Ooo )
elif ooO000O == 10017 : oooo00o0o0o ( )
elif ooO000O == 10018 : O0OIIi1 ( )
elif ooO000O == 10019 : iIIi1iI1I1IIi ( )
elif ooO000O == 10020 : oOo0OooOo ( )
elif ooO000O == 10021 : I1i ( )
elif ooO000O == 10022 : iIi1I1 ( ooOOO00Ooo )
elif ooO000O == 10023 : IiIii1I1I ( i1Oo00 , ooOOO00Ooo )
elif ooO000O == 10024 : iI1 ( ooOOO00Ooo )
elif ooO000O == 10025 : Oo00OOOOoo0oo ( )
elif ooO000O == 10026 : iiIII1II ( )
elif ooO000O == 10027 : iIII11Ii ( )
elif ooO000O == 10028 : OoO00 ( )
elif ooO000O == 10029 : OooO0oOo ( )
elif ooO000O == 423 : ooO ( ooOOO00Ooo )
elif ooO000O == 426 : II1IIIiiI11 ( ooOOO00Ooo )
elif ooO000O == 10030 : Izle_Films ( )
elif ooO000O == 10031 : Latest_Izle_Movies ( )
elif ooO000O == 10032 : Izle_Genres ( )
elif ooO000O == 10033 : Izle_Pop_Movies ( )
elif ooO000O == 10034 : Izle_Boxsets ( )
elif ooO000O == 10035 : Izle_Search ( )
elif ooO000O == 10036 : Izle_Genres_Movie ( ooOOO00Ooo )
elif ooO000O == 10037 : Izle_Boxset_single ( ooOOO00Ooo )
elif ooO000O == 10038 : Izle_IFRAME ( )
elif ooO000O == 10039 : Izle_Boxsets_Next ( ooOOO00Ooo )
elif ooO000O == 10040 : I1Ii ( )
elif ooO000O == 10041 : OoIIi1iI ( ooOOO00Ooo )
elif ooO000O == 10042 : O0OoOOOo0Oo ( ooOOO00Ooo )
elif ooO000O == 10043 : ooOO ( )
elif ooO000O == 10044 : i1iIIi1o0o0OoOOOOOo ( ooOOO00Ooo )
elif ooO000O == 10045 : ooOO0o ( i1Oo00 )
elif ooO000O == 10046 : oOO0o0oo0 ( ooOOO00Ooo )
elif ooO000O == 10047 : i1iii11 ( ooOOO00Ooo )
elif ooO000O == 10048 : Oo0000o0O0O ( ooOOO00Ooo )
elif ooO000O == 10049 : iiIii ( ooOOO00Ooo )
elif ooO000O == 10050 : I111oOOooo00OOooO ( )
elif ooO000O == 10051 : oooOo00000 ( )
elif ooO000O == 10052 : oO0OOOoO0o ( )
elif ooO000O == 10053 : Addon ( ooOOO00Ooo )
elif ooO000O == 10054 : i1i1Ii1IiIII ( ooOOO00Ooo , i1Oo00 )
elif ooO000O == 10055 :
 OOooo00 ( "addFavorite" )
 try :
  i1Oo00 = i1Oo00 . split ( '\\ ' ) [ 1 ]
 except :
  pass
 try :
  i1Oo00 = i1Oo00 . split ( '  - ' ) [ 0 ]
 except :
  pass
 iiII ( i1Oo00 , ooOOO00Ooo , OOoOO0oo0ooO , O00O0oOO00O00 , o0OO0 )
elif ooO000O == 10056 :
 OOooo00 ( "rmFavorite" )
 try :
  i1Oo00 = i1Oo00 . split ( '\\ ' ) [ 1 ]
 except :
  pass
 try :
  i1Oo00 = i1Oo00 . split ( '  - ' ) [ 0 ]
 except :
  pass
 OOOOOOoO ( i1Oo00 )
elif ooO000O == 10057 :
 OOooo00 ( "getFavorites" )
 I1iI1I1 ( )
elif ooO000O == 10058 : O0i1II1Iiii1I11 ( )
elif ooO000O == 10059 : Donators_Guide ( )
elif ooO000O == 10060 : OO00O0O ( )
elif ooO000O == 10061 : Iiiii1I ( )
elif ooO000O == 10062 : OOO ( i1Oo00 , ooOOO00Ooo , III1iII1I1ii )
elif ooO000O == 10063 : o00oooO0Oo ( )
elif ooO000O == 10064 : ooo00OOOooO ( )
elif ooO000O == 10065 : i1I1i ( ooOOO00Ooo )
elif ooO000O == 10066 : i11iIIIIIi1 ( ooOOO00Ooo )
elif ooO000O == 10067 : OO0oOoOO0oOO0 ( ooOOO00Ooo )
elif ooO000O == 20000 : OOOooo ( )
elif ooO000O == 20001 : OOO00O0oOOo ( )
elif ooO000O == 20002 : O0oooo00o0Oo ( ooOOO00Ooo )
elif ooO000O == 20003 : oO0Ooo0ooOO0 ( ooOOO00Ooo )
elif ooO000O == 20004 : ooi1i1I ( ooOOO00Ooo )
elif ooO000O == 21004 : ooo000o0ooO0 ( )
elif ooO000O == 21005 : I1I ( ooOOO00Ooo )
elif ooO000O == 21006 : OooOo00o ( ooOOO00Ooo )
elif ooO000O == 21007 : ii1IIIIiI11 ( ooOOO00Ooo )
elif ooO000O == 30000 : IiiIiI111iI ( )
elif ooO000O == 30001 : iIi11iiIiI1I ( )
elif ooO000O == 10012 : Resolve ( ooOOO00Ooo )
elif ooO000O == 30003 : iIiIi1I ( )
elif ooO000O == 30004 : O0Oo0o000oO ( ooOOO00Ooo )
elif ooO000O == 30005 : oOooO0OOOoO000 ( ooOOO00Ooo )
elif ooO000O == 30006 : ii1Oo0000oOo ( )
elif ooO000O == 30007 : OO0ooo0o0O0Oooooo ( )
elif ooO000O == 30008 : i1I1iI ( ooOOO00Ooo )
elif ooO000O == 30009 : O0OOO0OOooo00 ( ooOOO00Ooo )
elif ooO000O == 30010 : iIi1 ( ooOOO00Ooo )
elif ooO000O == 30011 : o0O0O0ooo0oOO ( )
elif ooO000O == 30012 : Oooo0 ( )
elif ooO000O == 30013 : iI1i1i ( )
elif ooO000O == 30014 : oooO0 ( )
if 47 - 47: IIII . OoOO0ooOOoo0O
xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
