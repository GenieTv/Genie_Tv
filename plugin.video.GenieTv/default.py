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
iiI1IiI = "2.5.3"
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
 if 26 - 26: oO0o0ooO0
def OOO ( ) :
 Oo0oOOo = Oo0o0000o0o0 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 Oo0OoO00oOO0o = 'https://www.youtube.com/results?search_query=' + ( Oo0oOOo ) . replace ( ' ' , '+' )
 OOO00O = Oo0OoO00oOO0o . lower ( )
 OOoOO0oo0ooO = O0o0O00Oo0o0 ( OOO00O )
 O00O0oOO00O00 = re . compile ( '<img src="(.+?)" alt=.+?yt-lockup-title "><a href="(.+?)".+?data-sessionlink=.+?" title="(.+?)".+?<span class="accessible-description".+?>(.+?)</span>.+?<div class="yt-lockup-description yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr">(.+?)</div>' , re . DOTALL ) . findall ( OOoOO0oo0ooO )
 next = re . compile ( '<a href="(.+?)" class="yt-uix-button.+?class="yt-uix-button-content">Next.+?</span></a>' ) . findall ( OOoOO0oo0ooO )
 for i1Oo00 in next :
  i1Oo00 = 'https://www.youtube.com' + i1Oo00
  iiiiiIIii ( '[COLORgreen] NEXT [/COLOR]' , i1Oo00 , 10065 , oOOoO0 + 'youtube.png' , OOooO0OOoo , '' )
 for i1i , i1Oo00 , iiI111I1iIiI , IIIi1I1IIii1II , O0ii1ii1ii in O00O0oOO00O00 :
  O0O . append ( iiI111I1iIiI )
  Oooo0Ooo000 ( 'tvshows' , 'INFO' )
  oooooOoo0ooo = 'http:' + ( i1i ) . replace ( 'https:' , '' )
  print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>' + oooooOoo0ooo
  i1Oo00 = 'http://www.youtube.com' + i1Oo00
  o0OOoo0OO0OOO ( '[COLORred]' + IIIi1I1IIii1II + '[/COLOR]' + '[COLORgreen]' + iiI111I1iIiI + '[/COLOR]' , ( i1Oo00 ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , oooooOoo0ooo , oooooOoo0ooo , O0ii1ii1ii )
 else :
  O00O0oOO00O00 = re . compile ( '<img src="(.+?)" alt=.+?yt-lockup-title "><a href="(.+?)".+?data-sessionlink=.+?" title="(.+?)".+?<span class="accessible-description".+?>(.+?)</span>' , re . DOTALL ) . findall ( OOoOO0oo0ooO )
  for i1i , i1Oo00 , iiI111I1iIiI , IIIi1I1IIii1II in O00O0oOO00O00 :
   Oooo0Ooo000 ( 'tvshows' , 'INFO' )
   oooooOoo0ooo = 'http:' + ( i1i ) . replace ( 'https:' , '' )
   i1Oo00 = 'http://www.youtube.com' + i1Oo00
   if iiI111I1iIiI in O0O :
    pass
   elif 'user' in i1Oo00 or 'elete' in iiI111I1iIiI :
    pass
   elif 'hannel' in i1Oo00 :
    print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' + i1Oo00
    OOoOO0oo0ooO = O0o0O00Oo0o0 ( i1Oo00 )
    I1I1IiI1 = re . compile ( 'data-thumb="(.+?)".+?href="(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( OOoOO0oo0ooO )
    for i1i , i1Oo00 , iiI111I1iIiI in I1I1IiI1 :
     if 'outube' in i1Oo00 or 'list' in i1Oo00 :
      pass
     elif 'atch' in i1Oo00 :
      i1Oo00 = ( i1Oo00 ) . replace ( '/watch?v=' , '' )
      o0OOoo0OO0OOO ( '[COLORred]' + IIIi1I1IIii1II + '[/COLOR]' + '[COLORgreen]' + iiI111I1iIiI + '[/COLOR]' , ( i1Oo00 ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , 'http:' + i1i , 'http:' + i1i , '' )
     else :
      pass
   elif '&' in i1Oo00 :
    OOoOO0oo0ooO = O0o0O00Oo0o0 ( i1Oo00 )
    III1iII1I1ii = re . compile ( '<li class="yt-uix-scroller-scroll-unit "(.+?)</li>' , re . DOTALL ) . findall ( OOoOO0oo0ooO )
    for III1iII1I1ii in III1iII1I1ii :
     iiI111I1iIiI = re . compile ( 'data-video-title="(.+?)"' ) . findall ( str ( III1iII1I1ii ) )
     for iiI111I1iIiI in iiI111I1iIiI :
      iiI111I1iIiI = ( iiI111I1iIiI ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&amp;' , '&' )
     i1Oo00 = re . compile ( '<a href="/w(.+?)&' ) . findall ( str ( III1iII1I1ii ) )
     for i1Oo00 in i1Oo00 :
      i1Oo00 = 'https://www.youtube.com/w' + i1Oo00
     o0OOoo0OO0OOO ( '[COLORred]' + IIIi1I1IIii1II + '[/COLOR]' + '[COLORgreen]' + iiI111I1iIiI + '[/COLOR]' , ( i1Oo00 ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , '' , '' , '' )
   else :
    o0OOoo0OO0OOO ( '[COLORred]' + IIIi1I1IIii1II + '[/COLOR]' + '[COLORgreen]' + iiI111I1iIiI + '[/COLOR]' , ( i1Oo00 ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , oooooOoo0ooo , oooooOoo0ooo , '' )
    if 61 - 61: OoOoOO00
def O0OOO ( url ) :
 OOoOO0oo0ooO = O0o0O00Oo0o0 ( url )
 O00O0oOO00O00 = re . compile ( '<img src="(.+?)" alt=.+?yt-lockup-title "><a href="(.+?)".+?data-sessionlink=.+?" title="(.+?)".+?<span class="accessible-description".+?>(.+?)</span>.+?<div class="yt-lockup-description yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr">(.+?)</div>' , re . DOTALL ) . findall ( OOoOO0oo0ooO )
 next = re . compile ( '<a href="(.+?)" class="yt-uix-button.+?class="yt-uix-button-content">Next.+?</span></a>' ) . findall ( OOoOO0oo0ooO )
 for url in next :
  url = 'https://www.youtube.com' + url
  iiiiiIIii ( '[COLORgreen] NEXT [/COLOR]' , url , 10065 , oOOoO0 + 'youtube.png' , OOooO0OOoo , '' )
 for i1i , url , iiI111I1iIiI , IIIi1I1IIii1II , O0ii1ii1ii in O00O0oOO00O00 :
  O0O . append ( iiI111I1iIiI )
  Oooo0Ooo000 ( 'tvshows' , 'INFO' )
  oooooOoo0ooo = 'http:' + ( i1i ) . replace ( 'https:' , '' )
  print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>' + oooooOoo0ooo
  url = 'http://www.youtube.com' + url
  o0OOoo0OO0OOO ( '[COLORred]' + IIIi1I1IIii1II + '[/COLOR]' + '[COLORgreen]' + iiI111I1iIiI + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , oooooOoo0ooo , oooooOoo0ooo , O0ii1ii1ii )
 else :
  O00O0oOO00O00 = re . compile ( '<img src="(.+?)" alt=.+?yt-lockup-title "><a href="(.+?)".+?data-sessionlink=.+?" title="(.+?)".+?<span class="accessible-description".+?>(.+?)</span>' , re . DOTALL ) . findall ( OOoOO0oo0ooO )
  for i1i , url , iiI111I1iIiI , IIIi1I1IIii1II in O00O0oOO00O00 :
   Oooo0Ooo000 ( 'tvshows' , 'INFO' )
   oooooOoo0ooo = 'http:' + ( i1i ) . replace ( 'https:' , '' )
   url = 'http://www.youtube.com' + url
   if iiI111I1iIiI in O0O :
    pass
   elif 'user' in url or 'elete' in iiI111I1iIiI :
    pass
   elif 'hannel' in url :
    print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' + url
    OOoOO0oo0ooO = O0o0O00Oo0o0 ( url )
    I1I1IiI1 = re . compile ( 'data-thumb="(.+?)".+?href="(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( OOoOO0oo0ooO )
    for i1i , url , iiI111I1iIiI in I1I1IiI1 :
     if 'outube' in url or 'list' in url :
      pass
     elif 'atch' in url :
      url = ( url ) . replace ( '/watch?v=' , '' )
      o0OOoo0OO0OOO ( '[COLORred]' + IIIi1I1IIii1II + '[/COLOR]' + '[COLORgreen]' + iiI111I1iIiI + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , 'http:' + i1i , 'http:' + i1i , '' )
     else :
      pass
   elif '&' in url :
    OOoOO0oo0ooO = O0o0O00Oo0o0 ( url )
    III1iII1I1ii = re . compile ( '<li class="yt-uix-scroller-scroll-unit "(.+?)</li>' , re . DOTALL ) . findall ( OOoOO0oo0ooO )
    for III1iII1I1ii in III1iII1I1ii :
     iiI111I1iIiI = re . compile ( 'data-video-title="(.+?)"' ) . findall ( str ( III1iII1I1ii ) )
     for iiI111I1iIiI in iiI111I1iIiI :
      iiI111I1iIiI = ( iiI111I1iIiI ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&amp;' , '&' )
     url = re . compile ( '<a href="/w(.+?)&' ) . findall ( str ( III1iII1I1ii ) )
     for url in url :
      url = 'https://www.youtube.com/w' + url
     o0OOoo0OO0OOO ( '[COLORred]' + IIIi1I1IIii1II + '[/COLOR]' + '[COLORgreen]' + iiI111I1iIiI + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , '' , '' , '' )
   else :
    o0OOoo0OO0OOO ( '[COLORred]' + IIIi1I1IIii1II + '[/COLOR]' + '[COLORgreen]' + iiI111I1iIiI + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , oooooOoo0ooo , oooooOoo0ooo , '' )
    if 10 - 10: OoOO0ooOOoo0O * o0000oOoOoO0o % I1IiI / OOOo0 / I1IiI
    if 42 - 42: Ooo00oOo00o
def o0o ( ) :
 if i1iiIII111ii == 'insert_password' :
  Oo0o0000o0o0 . ok ( '[COLORgreen]Donators Login[/COLOR]' , 'You need to set username and password to access this' , 'These are unique and provided to donators to help with server and stream costs' , 'Donate @ [COLORgreen]http://architects.x10host.com[/COLOR]' )
  o0oOoO00o . openSettings ( sys . argv [ 0 ] )
 else :
  iiiiiIIii ( '[COLORgreen]DONATORS LIST[/COLOR]' , OO0o + '/thelist.m3u' , 7080 , oOOoO0 + 'GTVIPTV.png' , OOooO0OOoo , '' )
  if 84 - 84: O0
def OOOooOO0 ( ) :
 buggalo . SUBMIT_URL = 'http://tommy.winther.nu/exception/submit.php'
 try :
  OOOOoOoo0O0O0 = gui . TVGuide ( )
  OOOOoOoo0O0O0 . doModal ( )
  del OOOOoOoo0O0O0
  print 'Deleted *W*'
 except Exception :
  print buggalo . onExceptionRaised ( )
  if 85 - 85: OoOO % i11iIiiIii - oO0o0ooO0 * OoooooooOO / OOOo0 % OOOo0
  if 1 - 1: Ooo00oOo00o - OoOO . o0000oOoOoO0o . Ooo00oOo00o / Oo + o0000oOoOoO0o
def OooOOOOo ( ) :
 iiiiiIIii ( 'Full Backup' , '' , 10061 , oOOoO0 + 'Backup.png' , OOooO0OOoo , 'Back Up Your Full System' )
 if os . path . exists ( I1IIIii ) :
  iiiiiIIii ( 'Backup Genie Favourites' , i1Oo00 , 10062 , oOOoO0 + 'Backup.png' , OOooO0OOoo , 'Back Up Your favourites' )
 if os . path . exists ( ooooooO0oo ) :
  iiiiiIIii ( 'Backup Ivue Config' , ooooooO0oo , 10062 , oOOoO0 + 'Backup.png' , OOooO0OOoo , 'Back Up Your master.db' )
 if os . path . exists ( IIiiiiiiIi1I1 ) :
  iiiiiIIii ( 'Backup Kodi Favourites' , IIiiiiiiIi1I1 , 10062 , oOOoO0 + 'Backup.png' , OOooO0OOoo , 'Back Up Your favourites.xml' )
  if 76 - 76: Ooo00oOo00o
  if 29 - 29: OoOO0ooOOoo0O + Oo . i11iIiiIii - i1IIi / iIii1I11I1II1
  if 26 - 26: o0000oOoOoO0o . OoooooooOO
zip = o0oOoO00o . getSetting ( 'zip' )
I11i1ii1 = xbmc . translatePath ( os . path . join ( zip ) )
def O0Oooo0O ( ) :
 O0o = xbmc . translatePath ( os . path . join ( zip , 'testCBFolder' ) )
 if not os . path . exists ( zip ) :
  ii11iIi1I . ok ( '[COLOR=white]Origin[/COLOR]' , 'The download location you have stored does not exist .\nPlease update the addon settings and try again.' , '' , '' )
  o0oOoO00o . openSettings ( sys . argv [ 0 ] )
  if 59 - 59: OOOo0 + OOOo0 + OOooOOo / iIii1I11I1II1
  if 51 - 51: o0000oOoOoO0o + oO0o0ooO0 % iIii1I11I1II1 / OoOO / OoOO0ooOOoo0O % OoooooooOO
  if 78 - 78: o00O0oo % O0oO + ii11ii1ii
def OOooOoooOoOo ( name , url , description ) :
 if 'Backup' in name :
  if 'Genie' in name :
   url = I1IIIii
  elif 'Ivue' in name :
   url = ooooooO0oo
  elif 'Kodi' in name :
   url = IIiiiiiiIi1I1
  O0Oooo0O ( )
  o0OOOO00O0Oo = open ( url ) . read ( )
  ii = os . path . join ( I11i1ii1 , description . split ( 'Your ' ) [ 1 ] )
  oOooOOOoOo = open ( ii , mode = 'w' )
  oOooOOOoOo . write ( o0OOOO00O0Oo )
  oOooOOOoOo . close ( )
 else :
  if 'guisettings.xml' in description :
   i1Iii1i1I = open ( os . path . join ( I11i1ii1 , description . split ( 'Your ' ) [ 1 ] ) ) . read ( )
   OOoO00 = '<setting type="(.+?)" name="%s.(.+?)">(.+?)</setting>' % skin
   O00O0oOO00O00 = re . compile ( OOoO00 ) . findall ( i1Iii1i1I )
   for type , IiI111111IIII , i1Ii in O00O0oOO00O00 :
    i1Ii = i1Ii . replace ( '&quot;' , '' ) . replace ( '&amp;' , '&' )
    xbmc . executebuiltin ( "Skin.Se	t%s(%s,%s)" % ( type . title ( ) , IiI111111IIII , i1Ii ) )
  else :
   ii = os . path . join ( url )
   o0OOOO00O0Oo = open ( os . path . join ( I11i1ii1 , description . split ( 'Your ' ) [ 1 ] ) ) . read ( )
   oOooOOOoOo = open ( ii , mode = 'w' )
   oOooOOOoOo . write ( o0OOOO00O0Oo )
   oOooOOOoOo . close ( )
 ii11iIi1I . ok ( "[COLOR=white]Origin[/COLOR]" , "" , 'All Done !' , '' )
 if 14 - 14: oO0o0ooO0
 if 11 - 11: IIII * OOOo0 . iIii1I11I1II1 % OoooooooOO + oO0o0ooO0
 if 78 - 78: Ooo00oOo00o . OoOO0ooOOoo0O + Ooo00oOo00o / o0000oOoOoO0o / Ooo00oOo00o
 if 54 - 54: I1IiI % oO0o0ooO0
def IIiII111iiI1I ( ) :
 Ii1i1iI1iIIi = 1
 O0Oooo0O ( )
 I1Ii = xbmc . translatePath ( os . path . join ( I11i1ii1 , 'Build Backup' , 'Full Backup' , '' ) )
 O0oo00o0O = xbmc . translatePath ( os . path . join ( I11i1ii1 , 'Build Backup' , 'my_full_backup.zip' ) )
 i1I1I = xbmc . translatePath ( os . path . join ( I11i1ii1 , 'Build Backup' , 'my_full_backup_GUI_Settings.zip' ) )
 if not os . path . exists ( I1Ii ) :
  os . makedirs ( I1Ii )
 iiI1I = Oo0o0000o0o0 . input ( 'Enter a name for this backup' , type = xbmcgui . INPUT_ALPHANUM )
 if ( not iiI1I ) : return False , 0
 IiIiiIIiI = iiI1I
 ooOO0OOOO0oo0 = xbmc . translatePath ( os . path . join ( I1Ii , IiIiiIIiI + '.zip' ) )
 I11iiI1i1 = [ 'plugin.video.GenieTv' ]
 I1i1Iiiii = [ "xbmc.log" , "xbmc.old.log" , "kodi.log" , "kodi.old.log" , '.DS_Store' , '.setup_complete' , 'XBMCHelper.conf' ]
 OOo0oO00ooO00 = [ 'plugin.video.GenieTv' , 'repository.origin' , 'cache' , 'system' , 'Thumbnails' , "peripheral_data" , 'library' , 'keymaps' ]
 oOO0O00oO0Ooo = [ "xbmc.log" , "xbmc.old.log" , "kodi.log" , "kodi.old.log" , "Textures13.db" , '.DS_Store' , '.setup_complete' , 'XBMCHelper.conf' , 'advancedsettings.xml' ]
 oO0Oo0O0o = "Creating full backup of existing build"
 OO = "Creating Community Build"
 I1iI1ii1II = "Archiving..."
 O0O0OOOOoo = ""
 oOooO0 = "Please Wait"
 Ii1I1Ii ( iI111I11I1I1 , ooOO0OOOO0oo0 , OO , I1iI1ii1II , O0O0OOOOoo , oOooO0 , OOo0oO00ooO00 , oOO0O00oO0Ooo )
 time . sleep ( 1 )
 OOoO0 = xbmc . translatePath ( os . path . join ( I1Ii , IiIiiIIiI + '_guisettings.zip' ) )
 OO0Oooo0oOO0O = zipfile . ZipFile ( OOoO0 , mode = 'w' )
 try :
  OO0Oooo0oOO0O . write ( xbmc . translatePath ( os . path . join ( iI111I11I1I1 , 'userdata' , 'profiles.xml' ) ) , 'profiles.xml' , zipfile . ZIP_DEFLATED )
 except : pass
 OO0Oooo0oOO0O . close ( )
 if Ii1i1iI1iIIi == 0 :
  ii11iIi1I . ok ( "FAILED!" , 'The guisettings.xml file could not be found on your' , 'system, please reboot and try again.' , '' )
 else :
  ii11iIi1I . ok ( "SUCCESS!" , 'You Are Now Backed Up. If you\'d like to share this build with' , 'the community please post details on the forum at' , '[COLOR=blue][B]http://rh-project.info[/COLOR][/B]' )
  ii11iIi1I . ok ( "Build Locations" , 'Full Backup (only used to restore on this device): [COLOR=yellow]' + O0oo00o0O , '[/COLOR]Universal Backup (can be used on any device): [COLOR=yellow]' + ooOO0OOOO0oo0 + '[/COLOR]' )
  if 62 - 62: OOOo0
def Ii1I1Ii ( sourcefile , destfile , message_header , message1 , message2 , message3 , exclude_dirs , exclude_files ) :
 O00o0OO0 = zipfile . ZipFile ( destfile , 'w' , zipfile . ZIP_DEFLATED )
 IIi1I1iiiii = len ( sourcefile )
 o00oOOooOOo0o = [ ]
 O0O0ooOOO = [ ]
 i1111 . create ( message_header , message1 , message2 , message3 )
 for oOOo0O00o , iIiIi11 , OOOiiiiI in os . walk ( sourcefile ) :
  for file in OOOiiiiI :
   O0O0ooOOO . append ( file )
 oooOo0OOOoo0 = len ( O0O0ooOOO )
 for oOOo0O00o , iIiIi11 , OOOiiiiI in os . walk ( sourcefile ) :
  iIiIi11 [ : ] = [ OOoO for OOoO in iIiIi11 if OOoO not in exclude_dirs ]
  OOOiiiiI [ : ] = [ oOooOOOoOo for oOooOOOoOo in OOOiiiiI if oOooOOOoOo not in exclude_files ]
  for file in OOOiiiiI :
   o00oOOooOOo0o . append ( file )
   OO0O000 = len ( o00oOOooOOo0o ) / float ( oooOo0OOOoo0 ) * 100
   i1111 . update ( int ( OO0O000 ) , "Backing Up" , '[COLOR yellow]%s[/COLOR]' % file , 'Please Wait' )
   iiIiI1i1 = os . path . join ( oOOo0O00o , file )
   if not 'temp' in iIiIi11 :
    if not 'plugin.program.originwizard' in iIiIi11 :
     import time
     oO0O00oOOoooO = '01/01/1980'
     IiIi11iI = time . strftime ( '%d/%m/%Y' , time . gmtime ( os . path . getmtime ( iiIiI1i1 ) ) )
     if IiIi11iI > oO0O00oOOoooO :
      O00o0OO0 . write ( iiIiI1i1 , iiIiI1i1 [ IIi1I1iiiii : ] )
 O00o0OO0 . close ( )
 i1111 . close ( )
 if 83 - 83: OoOoOO00 % Oo % o0oO0 % ii11ii1ii
 if 80 - 80: i11iIiiIii % o0oO0 + o00O0oo % o0000oOoOoO0o - ii11ii1ii
def I1i1i1iii ( ) :
 iiiiiIIii ( '[COLORgreen]SCOOBY STREAMS[/COLOR]' , ( oOo0oooo00o ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvdHZjYXRzLnBocA==' ) ) , 1016 , oOOoO0 + 'scoob.png' , OOooO0OOoo , '' )
 iiiiiIIii ( '[COLORgreen]SCOOBY SCRAPES[/COLOR]' , OO0o , 1024 , oOOoO0 + 'scoob.png' , OOooO0OOoo , '' )
 if 16 - 16: o00O0oo + IIII * O0 % i1IIi . OOOo0
 if 67 - 67: OoooooooOO / OOOo0 * o00O0oo + o0000oOoOoO0o
def OooOo0ooo ( ) :
 iiiiiIIii ( '[COLORgreen]SEARCH MOVIES[/COLOR]' , OO0o , 9001 , oOOoO0 + 'MOVIESv.png' , OOooO0OOoo , '' )
 iiiiiIIii ( '[COLORgreen]SEARCH SERIES[/COLOR]' , OO0o , 9002 , oOOoO0 + 'TVSHOWSv.png' , OOooO0OOoo , '' )
 iiiiiIIii ( '[COLORgreen]SEARCH CARTOONS[/COLOR]' , '' , 10005 , oOOoO0 + 'ORIGINCARTOON' , OOooO0OOoo , '' )
 if 71 - 71: O0oO + o00O0oo
 if 28 - 28: OoOO0ooOOoo0O
 if 38 - 38: o0oO0 % OoOoOO00 % o0000oOoOoO0o / Ooo00oOo00o + I1IiI / i1IIi
 if 54 - 54: iIii1I11I1II1 % ii11ii1ii - OoOO0ooOOoo0O / OoOO - Ooo00oOo00o . o0000oOoOoO0o
def IIo0Oo0oO0oOO00 ( ) :
 iiiiiIIii ( '[COLORgreen]RADIO[/COLOR]' , OO0o , 1013 , oOOoO0 + 'radio.png' , OOooO0OOoo , '' )
 iiiiiIIii ( '[COLORgreen]MUSIC[/COLOR]' , OO0o , 1030 , oOOoO0 + 'MUSIC.png' , OOooO0OOoo , '' )
 iiiiiIIii ( '[COLORgreen]MUSIC ARCHIVE[/COLOR]' , OO0o + ( oOo0oooo00o ( 'L3ZvZC91cmxzL211c2ljLnBocA==' ) ) , 1010 , oOOoO0 + 'MUSIC.png' , OOooO0OOoo , '' )
 iiiiiIIii ( '[COLORgreen]MUSIC SEARCH[/COLOR]' , OO0o , 1111 , oOOoO0 + 'search.png' , OOooO0OOoo , '' )
 iiiiiIIii ( '[COLORgreen]KODIBLE AUDIO BOOKS[/COLOR]' , 'http://doremisa.com/audiobooks/' , 30000 , oOOoO0 + 'kodible.png' , OOooO0OOoo , '' )
 if 92 - 92: OoooooooOO * O0oO
 Oooo0Ooo000 ( 'movies' , 'MAIN' )
 if 100 - 100: O0oO + O0oO * IIII
def I1i ( ) :
 if 99 - 99: O0oO + I1IiI * iIii1I11I1II1 / OoooooooOO
 o0OOoo0OO0OOO ( 'DELETE CACHE' , 'url' , 14 , oOOoO0 + 'MAIN5.png' , OOooO0OOoo , '' )
 o0OOoo0OO0OOO ( 'DELETE PACKAGES' , 'url' , 6 , oOOoO0 + 'MAIN4.png' , OOooO0OOoo , '' )
 o0OOoo0OO0OOO ( 'FORCE REFRESH' , 'url' , 10 , oOOoO0 + 'MAIN3.png' , OOooO0OOoo , 'Force Refresh All Repos' )
 if 46 - 46: o0000oOoOoO0o / o00O0oo
 o0OOoo0OO0OOO ( 'CHECK MY IP' , 'url' , 12 , oOOoO0 + 'MAIN2.png' , OOooO0OOoo , '' )
 o0OOoo0OO0OOO ( 'ANDROID ONLY DELETE TEXTURE13.DB&THUBMNAIL FOLDER' , 'url' , 13 , oOOoO0 + 'MAIN1.png' , OOooO0OOoo , 'Only Works On Android On Windows It Deletes Your Thumnails Folder But Does Not Delete The Textures13.db' )
 iiiiiIIii ( '[COLORgreen]ADVANCED SETTINGS XML[/COLOR]' , OO0o , 4 , oOOoO0 + 'XML.png' , OOooO0OOoo , '' )
 iiiiiIIii ( '[COLORgreen]URL FIXES[/COLOR]' , OO0o , 20 , oOOoO0 + 'URLFIX.png' , OOooO0OOoo , '' )
 Oooo0Ooo000 ( 'movies' , 'MAIN' )
 if 57 - 57: IIII / oO0o0ooO0 * O0 - OoooooooOO % iIii1I11I1II1
 if 33 - 33: i1IIi / o00O0oo
def ooO0oooOO0 ( ) :
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
 if 71 - 71: O0oO . OoOoOO00
 if 62 - 62: OoooooooOO . o0000oOoOoO0o
def oOOOoo00 ( ) :
 o0OOoo0OO0OOO ( 'CHECK ADVANCED XML' , OO0o , 8 , oOOoO0 + 'XML.png' , OOooO0OOoo , '' )
 o0OOoo0OO0OOO ( 'MUCKYS XML' , OO0o + '/wizard/muckys.xml' , 7 , oOOoO0 + 'XML.png' , OOooO0OOoo , '' )
 o0OOoo0OO0OOO ( '0CACHE XML' , OO0o + '/wizard/0cache.xml' , 7 , oOOoO0 + 'XML.png' , OOooO0OOoo , '' )
 o0OOoo0OO0OOO ( 'MIKEY1234 XML' , OO0o + '/wizard/mikey.xml' , 7 , oOOoO0 + 'XML.png' , OOooO0OOoo , '' )
 o0OOoo0OO0OOO ( 'TUXENS XML' , OO0o + '/wizard/tuxens.xml' , 7 , oOOoO0 + 'XML.png' , OOooO0OOoo , '' )
 o0OOoo0OO0OOO ( 'P2P RECOMMENDED XML1' , OO0o + '/wizard/p2p1.xml' , 7 , oOOoO0 + 'XML.png' , OOooO0OOoo , '' )
 o0OOoo0OO0OOO ( 'P2P RECOMMENDED XML2' , OO0o + '/wizard/p2p2.xml' , 7 , oOOoO0 + 'XML.png' , OOooO0OOoo , '' )
 o0OOoo0OO0OOO ( 'DELETE XML' , OO0o , 11 , oOOoO0 + 'XML.png' , OOooO0OOoo , '' )
 Oooo0Ooo000 ( 'movies' , 'MAIN' )
 if 9 - 9: O0 % O0 - OOooOOo
def OoO ( ) :
 o0OOoo0OO0OOO ( '[COLORgreen]My Local Zip[/COLOR]' , oo0o0O00 , 48 , oOOoO0 + 'MB.png' , OOooO0OOoo , '' )
 o0OOoo0OO0OOO ( '[COLORgreen]My Online Zip[/COLOR]' , oO0o0o0ooO0oO , 43 , oOOoO0 + 'MB.png' , OOooO0OOoo , '' )
 if 12 - 12: O0 - OOooOOo
def oOoO00O0 ( ) :
 o0OOoo0OO0OOO ( 'INSTALL FTV GUIDE AND OTHER ADDONS REQUIRED' , OO0o + '/wizard/customftv/ftvguide-addons.zip' , 5 , oOOoO0 + 'FTV4.png' , OOooO0OOoo , '' )
 o0OOoo0OO0OOO ( 'FTV GUIDE FIRST RUN SETTINGS' , OO0o + '/wizard/customftv/settings.xml' , 17 , oOOoO0 + 'FTV3.png' , OOooO0OOoo , '' )
 o0OOoo0OO0OOO ( 'FTV GUIDE ADDONS2.INI UPDATE DAILY' , 'http://ren.byethost12.com/addons2.ini' , 16 , oOOoO0 + 'FTV1.png' , OOooO0OOoo , '' )
 o0OOoo0OO0OOO ( 'RESET FTV DATABASE' , 'url' , 18 , oOOoO0 + 'FTV2.png' , OOooO0OOoo , '' )
 if 75 - 75: OOOo0 . o0oO0 . O0 * O0oO
 if 4 - 4: o00O0oo % OoOO * Ooo00oOo00o
 if 100 - 100: O0oO * OoOO0ooOOoo0O + OoOO0ooOOoo0O
def OoOO0o ( ) :
 iiiiiIIii ( '[COLORgreen]SKINS[/COLOR]' , OO0o , 33 , oOOoO0 + 'skinp.png' , OOooO0OOoo , '' )
 iiiiiIIii ( '[COLORgreen]ARTWORK PACKS[/COLOR]' , OO0o , 34 , oOOoO0 + 'artp.png' , OOooO0OOoo , '' )
 iiiiiIIii ( '[COLORgreen]CREATE UNIVERSAL PATHS[/COLOR]' , iI111I11I1I1 , 35 , oOOoO0 + 'GUI.png' , OOooO0OOoo , '' )
 Oooo0Ooo000 ( 'movies' , 'MAIN' )
 if 1 - 1: OoOoOO00
def O0oOo00o ( url ) :
 o0ooooO0o0O = O0o0O00Oo0o0 ( iiIi11iI1iii ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 O00O0oOO00O00 = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( o0ooooO0o0O )
 for iiI111I1iIiI , url , oo000 , o0000oO , O0ii1ii1ii in O00O0oOO00O00 :
  iiiiiIIii ( iiI111I1iIiI , url , 5 , oo000 , o0000oO , O0ii1ii1ii )
 Oooo0Ooo000 ( 'movies' , 'MAIN' )
 if 15 - 15: I1IiI % OOOo0 * o0000oOoOoO0o
def O0OoooO0 ( ) :
 iiiiiIIii ( '[COLORgreen]GOTHAM SKINS[/COLOR]' , OO0o , 36 , oOOoO0 + 'GSKIN.png' , OOooO0OOoo , '' )
 iiiiiIIii ( '[COLORgreen]HELIX SKINS[/COLOR]' , OO0o , 37 , oOOoO0 + 'HSKIN.png' , OOooO0OOoo , '' )
 iiiiiIIii ( '[COLORgreen]ISENGAARD SKINS[/COLOR]' , iI111I11I1I1 , 38 , oOOoO0 + 'ISKIN.png' , OOooO0OOoo , '' )
 Oooo0Ooo000 ( 'movies' , 'MAIN' )
 if 85 - 85: o0000oOoOoO0o
def iI1i11II1i ( url ) :
 o0ooooO0o0O = O0o0O00Oo0o0 ( OO0o + o0o0OoOo0O0OO ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 O00O0oOO00O00 = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( o0ooooO0o0O )
 for iiI111I1iIiI , url , oo000 , o0000oO , O0ii1ii1ii in O00O0oOO00O00 :
  iiiiiIIii ( iiI111I1iIiI , url , 42 , oo000 , o0000oO , O0ii1ii1ii )
 Oooo0Ooo000 ( 'movies' , 'MAIN' )
 if 36 - 36: I1IiI - O0
def o0OOOooo0OOo ( url ) :
 o0ooooO0o0O = O0o0O00Oo0o0 ( OO0o + iII1i11IIi1i ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 O00O0oOO00O00 = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( o0ooooO0o0O )
 for iiI111I1iIiI , url , oo000 , o0000oO , O0ii1ii1ii in O00O0oOO00O00 :
  iiiiiIIii ( iiI111I1iIiI , url , 42 , oo000 , o0000oO , O0ii1ii1ii )
 Oooo0Ooo000 ( 'movies' , 'MAIN' )
 if 73 - 73: OOooOOo * O0 - i11iIiiIii
def O0O0o0oOOO ( url ) :
 o0ooooO0o0O = O0o0O00Oo0o0 ( OO0o + OOoOoOo ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 O00O0oOO00O00 = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( o0ooooO0o0O )
 for iiI111I1iIiI , url , oo000 , o0000oO , O0ii1ii1ii in O00O0oOO00O00 :
  iiiiiIIii ( iiI111I1iIiI , url , 42 , oo000 , o0000oO , O0ii1ii1ii )
 Oooo0Ooo000 ( 'movies' , 'MAIN' )
 if 98 - 98: oO0o0ooO0
def OooooO0oOOOO ( url ) :
 o0ooooO0o0O = O0o0O00Oo0o0 ( oOo0oooo00o ( 'aHR0cHM6Ly9kbC5kcm9wYm94dXNlcmNvbnRlbnQuY29tL3MvN2ZrMjhndDlwb3QxMjJhL0JVSUxEUy50eHQ/ZGw9MA==' ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 O00O0oOO00O00 = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( o0ooooO0o0O )
 for iiI111I1iIiI , url , oo000 , o0000oO , O0ii1ii1ii in O00O0oOO00O00 :
  iiiiiIIii ( iiI111I1iIiI , url , 42 , oo000 , o0000oO , O0ii1ii1ii )
 Oooo0Ooo000 ( 'movies' , 'MAIN' )
 if 100 - 100: oO0o0ooO0 % OoOO0ooOOoo0O
def OOOiII1 ( url ) :
 o0ooooO0o0O = O0o0O00Oo0o0 ( OO0o + OOo ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 O00O0oOO00O00 = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( o0ooooO0o0O )
 for iiI111I1iIiI , url , oo000 , o0000oO , O0ii1ii1ii in O00O0oOO00O00 :
  iiiiiIIii ( iiI111I1iIiI , url , 40 , oo000 , o0000oO , O0ii1ii1ii )
 Oooo0Ooo000 ( 'movies' , 'MAIN' )
 if 22 - 22: I1IiI * O0 . IIII * i11iIiiIii - OOOo0 * o0oO0
def OOooo0O0o0 ( url ) :
 o0ooooO0o0O = O0o0O00Oo0o0 ( OO0o + II1iI1I11I ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 O00O0oOO00O00 = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( o0ooooO0o0O )
 for iiI111I1iIiI , url , oo000 , o0000oO , O0ii1ii1ii in O00O0oOO00O00 :
  iiiiiIIii ( iiI111I1iIiI , url , 5 , oo000 , o0000oO , O0ii1ii1ii )
 Oooo0Ooo000 ( 'movies' , 'MAIN' )
 if 78 - 78: OoOoOO00
def o0O0Oo ( ) :
 Ooo0O0oooo = iiI ( oOo0oooo00o ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vYXBrdG9vbC9hcGsucGhw' ) )
 O00O0oOO00O00 = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( Ooo0O0oooo )
 for i1Oo00 , oooooOoo0ooo , iiI111I1iIiI in O00O0oOO00O00 :
  oOIIiIi ( iiI111I1iIiI , i1Oo00 , 2031 , oooooOoo0ooo )
  if 91 - 91: ii11ii1ii * Oo / OOOo0 . O0 + Ooo00oOo00o + I1IiI
def iIIi ( name , url , description ) :
 O0o = xbmc . translatePath ( os . path . join ( iiI1iI111ii1i , 'Download' ) )
 i1111 = xbmcgui . DialogProgress ( )
 i1111 . create ( "Your App Is Downloading" , "Why not check out our website" , '' , 'Http://architects.x10host.com' )
 Ii1IIiI1IiIII = os . path . join ( O0o , name + '.apk' )
 try :
  os . remove ( Ii1IIiI1IiIII )
 except :
  pass
 downloader . download ( url , Ii1IIiI1IiIII , i1111 )
 ii11iIi1I = xbmcgui . Dialog ( )
 ii11iIi1I . ok ( "GenieTv" , "[COLORred]Please press ok, exit kodi and go to your downloads folder to install your app[/COLOR]" , "[COLORblue]Tool Brought To You By Architects@Work[/COLOR]" )
 if 69 - 69: I1IiI * Ooo00oOo00o % OoOO0ooOOoo0O / oO0o0ooO0
def oOoO00o ( url ) :
 O0o = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/resources/downloads' ) )
 i1111 = xbmcgui . DialogProgress ( )
 i1111 . create ( "Your fILM Is Downloading" , "Why not check out our website" , '' , 'Http://architects.x10host.com' )
 Ii1IIiI1IiIII = os . path . join ( O0o , iiI111I1iIiI + '.mp4' )
 try :
  os . remove ( Ii1IIiI1IiIII )
 except :
  pass
 downloader . download ( url , Ii1IIiI1IiIII , i1111 )
 ii11iIi1I = xbmcgui . Dialog ( )
 ii11iIi1I . ok ( "GenieTv" , "[COLORred]Please press ok, Your download With Be Avaiilable Via The My Downloads Button[/COLOR]" , "[COLORblue]Tool Brought To You By Architects@Work[/COLOR]" )
 if 100 - 100: OOooOOo + OoOO0ooOOoo0O * OOooOOo
 if 80 - 80: OOooOOo * O0 - o00O0oo
def oo00O00Oo ( name , url , description ) :
 O0o = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 i1111 = xbmcgui . DialogProgress ( )
 i1111 . create ( "Your Art Pack Is Downloading" , "Why not check out our website" , '' , 'Http://architects.x10host.com' )
 Ii1IIiI1IiIII = os . path . join ( O0o , name )
 try :
  os . remove ( Ii1IIiI1IiIII )
 except :
  pass
 downloader . download ( url , Ii1IIiI1IiIII , i1111 )
 IIIII1II = xbmc . translatePath ( os . path . join ( i1 ) )
 time . sleep ( 2 )
 i1111 . update ( 0 , "" , "Placing Your Art Please Wait" )
 print '======================================='
 print IIIII1II
 print '======================================='
 extract . all ( Ii1IIiI1IiIII , IIIII1II , i1111 )
 ii11iIi1I = xbmcgui . Dialog ( )
 ii11iIi1I . ok ( "GenieTv" , "[COLORred]Once complete your artwork will be stored in your Media folder, Accessible via the Homefolder, Enjoy[/COLOR]" )
 if 35 - 35: iIii1I11I1II1
 if 42 - 42: O0oO . OOOo0 . i1IIi + I1IiI + OoOO0ooOOoo0O + OOOo0
def I1I ( url ) :
 o0ooooO0o0O = O0o0O00Oo0o0 ( oOo0oooo00o ( 'aHR0cDovL2dlbmlldHYuYXJjaGl0ZWN0cy54MTBob3N0LmNvbS90ZXN0L3doLnR4dA==' ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 O00O0oOO00O00 = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( o0ooooO0o0O )
 for iiI111I1iIiI , url , oo000 , o0000oO , O0ii1ii1ii in O00O0oOO00O00 :
  iiiiiIIii ( iiI111I1iIiI , url , 5 , oo000 , o0000oO , O0ii1ii1ii )
 try :
  o0ooooO0o0O = O0o0O00Oo0o0 ( ooooO0oOoOOoO + oooOOOOO + I1i11i ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
  O00O0oOO00O00 = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( o0ooooO0o0O )
  for iiI111I1iIiI , url , oo000 , o0000oO , O0ii1ii1ii in O00O0oOO00O00 :
   iiiiiIIii ( iiI111I1iIiI , url , 5 , oo000 , o0000oO , O0ii1ii1ii )
 except : pass
 Oooo0Ooo000 ( 'movies' , 'INFO' )
 if 11 - 11: OOOo0 / OoOoOO00 + OOooOOo * ii11ii1ii - ii11ii1ii - OOOo0
 if 85 - 85: o0000oOoOoO0o % OoOO / iIii1I11I1II1 . iIii1I11I1II1
def iIIiIiI1I1 ( url ) :
 o0ooooO0o0O = O0o0O00Oo0o0 ( oOo0oooo00o ( 'aHR0cDovL2dlbmlldHYuYXJjaGl0ZWN0cy54MTBob3N0LmNvbS90ZXN0L3doLnR4dA==' ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 O00O0oOO00O00 = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( o0ooooO0o0O )
 for iiI111I1iIiI , url , oo000 , o0000oO , O0ii1ii1ii in O00O0oOO00O00 :
  iiiiiIIii ( iiI111I1iIiI , url , 43 , oo000 , o0000oO , O0ii1ii1ii )
 try :
  o0ooooO0o0O = O0o0O00Oo0o0 ( ooooO0oOoOOoO + oooOOOOO + I1i11i ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
  O00O0oOO00O00 = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( o0ooooO0o0O )
  for iiI111I1iIiI , url , oo000 , o0000oO , O0ii1ii1ii in O00O0oOO00O00 :
   iiiiiIIii ( iiI111I1iIiI , url , 43 , oo000 , o0000oO , O0ii1ii1ii )
 except : pass
 Oooo0Ooo000 ( 'movies' , 'INFO' )
 if 56 - 56: OOOo0 . O0 + Oo
 if 1 - 1: oO0o0ooO0
def O0O0Ooo ( name , url , description ) :
 O0o = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 i1111 = xbmcgui . DialogProgress ( )
 i1111 . create ( "GenieTv" , "Downloading Content" , '' , 'Please Wait' )
 Ii1IIiI1IiIII = os . path . join ( O0o , name + '.zip' )
 try :
  os . remove ( Ii1IIiI1IiIII )
 except :
  pass
 downloader . download ( url , Ii1IIiI1IiIII , i1111 )
 oOoO0 = xbmc . translatePath ( os . path . join ( 'special://home' , 'addons' ) )
 time . sleep ( 2 )
 i1111 . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print oOoO0
 print '======================================='
 extract . all ( Ii1IIiI1IiIII , oOoO0 , i1111 )
 ii11iIi1I = xbmcgui . Dialog ( )
 ii11iIi1I . ok ( "GenieTv" , "Press ok to finish install" , "[COLOR yellow]Brought To You By Architects@Work[/COLOR]" )
 Oo0 ( )
 if 83 - 83: i11iIiiIii % OOooOOo % o0oO0
 if 11 - 11: OoOoOO00 % Ooo00oOo00o * oO0o0ooO0 + o0oO0 + o00O0oo
def II1Iiiiii ( name , url , description ) :
 O0o = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 i1111 = xbmcgui . DialogProgress ( )
 i1111 . create ( "GenieTv" , "Downloading " , '' , 'Please Wait' )
 Ii1IIiI1IiIII = os . path . join ( O0o , 'plugin.program.GenieTv.install' + '.zip' )
 try :
  os . remove ( Ii1IIiI1IiIII )
 except :
  pass
 downloader . download ( url , Ii1IIiI1IiIII , i1111 )
 oOoO0 = xbmc . translatePath ( os . path . join ( 'special://' , 'home' ) )
 time . sleep ( 2 )
 i1111 . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print oOoO0
 print '======================================='
 extract . all ( Ii1IIiI1IiIII , oOoO0 , i1111 )
 ii11iIi1I = xbmcgui . Dialog ( )
 ii11iIi1I . ok ( "GenieTv" , "Press ok to force close kodi, if unsuccessful using windows Please kill kodi via taskmanager" , "[COLOR yellow]Brought To You By Architects@Work[/COLOR]" )
 ii1ii111 ( )
 if 10 - 10: O0oO % IIII * IIII . o0000oOoOoO0o / o00O0oo % OoOO0ooOOoo0O
def IIII1 ( name , url , description ) :
 O0o = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 i1111 = xbmcgui . DialogProgress ( )
 i1111 . create ( "GenieTv" , "Downloading " , '' , 'Please Wait' )
 Ii1IIiI1IiIII = os . path . join ( O0o , 'plugin.program.GenieTv.install' + '.zip' )
 try :
  os . remove ( Ii1IIiI1IiIII )
 except :
  pass
 downloader . download ( url , Ii1IIiI1IiIII , i1111 )
 oOoO0 = xbmc . translatePath ( os . path . join ( 'special://' , 'home' ) )
 time . sleep ( 2 )
 i1111 . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print oOoO0
 print '======================================='
 extract . all ( Ii1IIiI1IiIII , oOoO0 , i1111 )
 ii11iIi1I = xbmcgui . Dialog ( )
 ii11iIi1I . ok ( "GenieTv" , "Please Disconnect The Power From Your Device. DO NOT EXIT CLEANLY VIA SHUTDOWN" , "[COLOR yellow]Brought To You By Architects@Work[/COLOR]" )
 if 10 - 10: O0oO / o0oO0 + i11iIiiIii / o00O0oo
 if 74 - 74: OoOO0ooOOoo0O + O0 + i1IIi - i1IIi + OoOoOO00
def oOOO0oo0 ( name , url , description ) :
 oOoO0 = xbmc . translatePath ( os . path . join ( 'special://' , 'home' ) )
 i1111 = xbmcgui . DialogProgress ( )
 Ii1IIiI1IiIII = os . path . join ( oo0o0O00 )
 time . sleep ( 2 )
 i1111 . create ( "GenieTv" , "Restoring" , '' , 'Please Wait' )
 print '======================================='
 print oOoO0
 print '======================================='
 extract . all ( Ii1IIiI1IiIII , oOoO0 , i1111 )
 ii11iIi1I = xbmcgui . Dialog ( )
 ii11iIi1I . ok ( "GenieTv" , "Please Disconnect The Power From Your Device. DO NOT EXIT CLEANLY VIA SHUTDOWN" , "[COLOR yellow]Brought To You By Architects@Work[/COLOR]" )
 if 46 - 46: IIII
 if 45 - 45: o0oO0
def ii1ii111 ( ) :
 IIi = xbmcgui . Dialog ( ) . yesno ( 'Force Close Kodi' , 'You are about to close Kodi' , 'Would you like to continue?' , nolabel = 'No, Cancel' , yeslabel = 'Yes, Close' )
 if IIi == 0 :
  return
 elif IIi == 1 :
  pass
 ooO0oOo0o = OOii111IiiI1 ( )
 print "Platform: " + str ( ooO0oOo0o )
 if ooO0oOo0o == 'osx' :
  print "############   try osx force close  #################"
  try : os . system ( 'killall -9 XBMC' )
  except : pass
  try : os . system ( 'killall -9 Kodi' )
  except : pass
  ii11iIi1I . ok ( "[COLOR=red][B]WARNING  !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu." , '' )
 elif ooO0oOo0o == 'linux' :
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
 elif ooO0oOo0o == 'android' :
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
 elif ooO0oOo0o == 'windows' :
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
  if 11 - 11: iIii1I11I1II1 * o00O0oo
def OOii111IiiI1 ( ) :
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
  if 76 - 76: o0oO0
  if 15 - 15: OoOO0ooOOoo0O . o0000oOoOoO0o + OoooooooOO - Ooo00oOo00o
  if 69 - 69: iIii1I11I1II1 . ii11ii1ii % o0oO0 + iIii1I11I1II1 / O0 / ii11ii1ii
def O00OoOO0oo0 ( url ) :
 i1111 . create ( "[COLOR=green]GenieTv[/COLOR]" , "Renaming paths..." , '' , 'Please Wait' )
 for oOO , iIiIi11 , OOOiiiiI in os . walk ( url ) :
  for file in OOOiiiiI :
   if file . endswith ( ".xml" ) :
    i1111 . update ( 0 , "Fixing" , file , 'Please Wait' )
    i1Iii1i1I = open ( ( os . path . join ( oOO , file ) ) ) . read ( )
    O0o0OO0000ooo = i1Iii1i1I . replace ( iI111I11I1I1 , 'special://home/' )
    oOooOOOoOo = open ( ( os . path . join ( oOO , file ) ) , mode = 'w' )
    oOooOOOoOo . write ( str ( O0o0OO0000ooo ) )
    oOooOOOoOo . close ( )
 ii1ii111 ( )
 if 4 - 4: o00O0oo
def OO0oOOoo ( ) :
 Ooo0O0oooo = iiI ( oOo0oooo00o ( 'aHR0cDovL3d3dy5saXN0ZW5saXZlLmV1L3VrLmh0bWw=' ) )
 O00O0oOO00O00 = re . compile ( '<tr>.+?<td><a href=".+?"><b>(.+?)</b>.+?<td><a href="(.+?)">' , re . DOTALL ) . findall ( Ooo0O0oooo )
 for iiI111I1iIiI , i1Oo00 in O00O0oOO00O00 :
  oOOO00o000o ( iiI111I1iIiI , i1Oo00 , 222 , oOOoO0 + 'radio.png' )
  if 9 - 9: OoOO + o0000oOoOoO0o / o0000oOoOoO0o
def Ii1I11ii1i ( ) :
 Ooo0O0oooo = iiI ( oOo0oooo00o ( 'aHR0cDovL3d3dy50b29uamV0LmNvbS8=' ) )
 O00O0oOO00O00 = re . compile ( '<a href="(.+?)" style="font-size:.8em;">(.+?)</a>' ) . findall ( Ooo0O0oooo )
 for i1Oo00 , iiI111I1iIiI in O00O0oOO00O00 :
  oOIIiIi ( '[COLORgreen]' + iiI111I1iIiI + '[/COLOR]' , 'http://www.toonjet.com/' + i1Oo00 , 8051 , oOOoO0 + 'classictoons.png' )
def O0iIiIIIIIii ( url ) :
 Ooo0O0oooo = iiI ( url )
 O00O0oOO00O00 = re . compile ( '<a href="(.+?)"><img src="(.+?)"' ) . findall ( Ooo0O0oooo )
 OOo0 = re . compile ( '<a href="(.+?)">.+?</a></td></tr></table>' ) . findall ( Ooo0O0oooo )
 for url , i1i in O00O0oOO00O00 :
  if 'ol.gif' in i1i :
   pass
  elif 'link_block_' in i1i :
   pass
  elif '.png' in i1i :
   pass
  else :
   oOIIiIi ( ( i1i ) . replace ( 'http://www.toonjet.com/images/icons/' , '' ) . replace ( 'images/icons/' , '' ) . replace ( '.jpg' , '' ) . replace ( '_icon' , '' ) . replace ( '_' , ' ' ) , 'http://www.toonjet.com/' + url , 8052 , oOOoO0 + 'vod.png' )
 for url in OOo0 :
  oOIIiIi ( 'NEXT PAGE' , 'http://www.toonjet.com/' + url , 8051 , oOOoO0 + 'documentary.png' )
def ii11I1 ( url ) :
 Ooo0O0oooo = iiI ( url )
 O00O0oOO00O00 = re . compile ( '<iframe width="640" height="480" src="(.+?)" frameborder="0" allowfullscreen></iframe>' ) . findall ( Ooo0O0oooo )
 for url in O00O0oOO00O00 :
  oOOO00o000o ( '[COLORgreen]PLAY[/COLOR]' , ( url ) . replace ( 'http://www.youtube.com/embed/' , '' ) . replace ( '?autoplay=0' , '' ) , 8043 , oOOoO0 + 'classictoons.png' )
  if 75 - 75: Ooo00oOo00o / OoOoOO00 % O0
  if 38 - 38: OoooooooOO * o0oO0 % O0 * I1IiI
def IIiiI ( ) :
 III1i11 ( 'Audio Books' , '' , 30011 , oOOoO0 + 'audiobooks.png' , oOOoO0 + 'audiobooks.png' , '' )
 III1i11 ( 'Kids Audio Books' , '' , 30006 , oOOoO0 + 'kidsaudiobooks.png' , oOOoO0 + 'kidsaudiobooks.png' , '' )
 if 25 - 25: Ooo00oOo00o
def i11iI11iIiIi ( ) :
 III1i11 ( 'All' , '' , 30001 , oOOoO0 + 'kodible.png' , oOOoO0 + 'kodible.png' , '' )
 III1i11 ( 'Popular' , '' , 30012 , oOOoO0 + 'POPULARv.png' , oOOoO0 + 'POPULARv.png' , '' )
 III1i11 ( 'Search' , '' , 30013 , oOOoO0 + 'search.png' , oOOoO0 + 'search.png' , '' )
 if 100 - 100: O0oO . OOooOOo * Oo % O0 * O0
def IIIii1 ( ) :
 OOoOO0oo0ooO = O0o0O00Oo0o0 ( Oo00OOOOO + 'books' + O0o0Oo )
 O00O0oOO00O00 = re . compile ( '<NAME=>(.*?)</NAME><URL=>(.*?)</URL><CAT=>(.*?)</CAT>' ) . findall ( OOoOO0oo0ooO )
 for iiI111I1iIiI , i1Oo00 , Oooo0 in O00O0oOO00O00 :
  if 'Parent' in iiI111I1iIiI :
   pass
  elif '2' in Oooo0 :
   III1i11 ( ( iiI111I1iIiI ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , i1Oo00 , 30010 , oOOoO0 + 'kodible.png' , oOOoO0 + 'kodible.png' , '' )
   if 59 - 59: OoooooooOO
def i1iiiii1 ( ) :
 Oo0oOOo = Oo0o0000o0o0 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OOO00O = Oo0oOOo . lower ( )
 OOoOO0oo0ooO = O0o0O00Oo0o0 ( Oo00OOOOO + 'books' + O0o0Oo )
 O00O0oOO00O00 = re . compile ( '<NAME=>(.*?)</NAME><URL=>(.*?)</URL><CAT=>(.*?)</CAT>' ) . findall ( OOoOO0oo0ooO )
 for iiI111I1iIiI , i1Oo00 , Oooo0 in O00O0oOO00O00 :
  if Oo0oOOo in iiI111I1iIiI . lower ( ) :
   if '1' in Oooo0 :
    III1i11 ( ( iiI111I1iIiI ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , i1Oo00 , 30010 , oOOoO0 + 'kodible.png' , oOOoO0 + 'kodible.png' , '' )
   elif '2' in Oooo0 :
    III1i11 ( ( iiI111I1iIiI ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , i1Oo00 , 30010 , oOOoO0 + 'kodible.png' , oOOoO0 + 'kodible.png' , '' )
   elif '3' in Oooo0 :
    III1i11 ( ( iiI111I1iIiI ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , i1Oo00 , 30009 , oOOoO0 + 'kodible.png' , oOOoO0 + 'kodible.png' , '' )
    if 83 - 83: oO0o0ooO0 . O0 / Oo / OoOO0ooOOoo0O - OoOoOO00
    if 100 - 100: Ooo00oOo00o
def II1i ( ) :
 OOoOO0oo0ooO = O0o0O00Oo0o0 ( Oo00OOOOO + 'books' + O0o0Oo )
 O00O0oOO00O00 = re . compile ( '<NAME=>(.*?)</NAME><URL=>(.*?)</URL><CAT=>(.*?)</CAT>' ) . findall ( OOoOO0oo0ooO )
 for iiI111I1iIiI , i1Oo00 , Oooo0 in O00O0oOO00O00 :
  if '1' in Oooo0 :
   III1i11 ( ( iiI111I1iIiI ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , i1Oo00 , 3010 , oOOoO0 + 'kodible.png' , oOOoO0 + 'kodible.png' , '' )
  elif '2' in Oooo0 :
   III1i11 ( ( iiI111I1iIiI ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , i1Oo00 , 30010 , oOOoO0 + 'kodible.png' , oOOoO0 + 'kodible.png' , '' )
  elif '3' in Oooo0 :
   III1i11 ( ( iiI111I1iIiI ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , i1Oo00 , 30009 , oOOoO0 + 'kodible.png' , oOOoO0 + 'kodible.png' , '' )
   if 2 - 2: iIii1I11I1II1 * Oo % OoOO - OoOoOO00 - oO0o0ooO0
 xbmcplugin . addSortMethod ( o0 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 3 - 3: O0oO
def i1iiIiI1Ii1i ( url ) :
 i1iIi = url
 OOoOO0oo0ooO = O0o0O00Oo0o0 ( url )
 OOo0 = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( OOoOO0oo0ooO )
 for url , iiI111I1iIiI in OOo0 :
  if 'mp3' in iiI111I1iIiI :
   iiiiiIIii ( ( iiI111I1iIiI ) . replace ( '%20' , ' ' ) , i1iIi + url , 10012 , oOOoO0 + 'kodible.png' , oOOoO0 + 'kodible.png' , '' )
  if 'wma' in iiI111I1iIiI :
   iiiiiIIii ( ( iiI111I1iIiI ) . replace ( '%20' , ' ' ) , i1iIi + url , 10012 , oOOoO0 + 'kodible.png' , oOOoO0 + 'kodible.png' , '' )
  if 'm4b' in iiI111I1iIiI :
   iiiiiIIii ( ( iiI111I1iIiI ) . replace ( '%20' , ' ' ) , i1iIi + url , 10012 , oOOoO0 + 'kodible.png' , oOOoO0 + 'kodible.png' , '' )
  elif '/' in iiI111I1iIiI :
   III1i11 ( ( iiI111I1iIiI ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , i1iIi + url , 30009 , oOOoO0 + 'kodible.png' , oOOoO0 + 'kodible.png' , '' )
   if 30 - 30: O0 - iIii1I11I1II1 / OoooooooOO
   if 89 - 89: oO0o0ooO0 - o0oO0 % Oo % OOooOOo
   if 49 - 49: Oo - OOOo0 / IIII / O0 % OOooOOo * o00O0oo
def OOoO0II11iI111i1 ( url ) :
 OOoOO0oo0ooO = O0o0O00Oo0o0 ( url )
 i1iIi = url
 O00O0oOO00O00 = re . compile ( '<li><a href="(.+?)">(.+?)</a></li>' ) . findall ( OOoOO0oo0ooO )
 for url , iiI111I1iIiI in O00O0oOO00O00 :
  if 'Parent' in iiI111I1iIiI :
   pass
  elif '.db' in iiI111I1iIiI :
   pass
  elif '.jpg' in iiI111I1iIiI :
   pass
  elif '.html' in iiI111I1iIiI :
   pass
  elif '.doc' in iiI111I1iIiI :
   pass
  elif 'mp3' in iiI111I1iIiI :
   iiiiiIIii ( ( iiI111I1iIiI ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , i1iIi + url , 10012 , oOOoO0 + 'kodible.png' , oOOoO0 + 'kodible.png' , '' )
  elif 'm4a' in iiI111I1iIiI :
   iiiiiIIii ( ( iiI111I1iIiI ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , i1iIi + url , 10012 , oOOoO0 + 'kodible.png' , oOOoO0 + 'kodible.png' , '' )
  else :
   III1i11 ( ( iiI111I1iIiI ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , i1iIi + url , 30010 , oOOoO0 + 'kodible.png' , oOOoO0 + 'kodible.png' , '' )
   if 95 - 95: OoooooooOO - IIII * OOOo0 + I1IiI
   if 10 - 10: OOooOOo / i11iIiiIii
def o00oO ( ) :
 III1i11 ( 'A-Z' , '' , 7 , oOOoO0 + 'kodible.png' , oOOoO0 + 'kodible.png' , '' )
 III1i11 ( 'All' , '' , 3 , oOOoO0 + 'kodible.png' , oOOoO0 + 'kodible.png' , '' )
 III1i11 ( 'Search' , '' , 14 , oOOoO0 + 'kodible.png' , oOOoO0 + 'kodible.png' , '' )
 if 92 - 92: IIII * Oo * Oo * OOOo0 . iIii1I11I1II1
def I1Ii1111iIi ( ) :
 OOoOO0oo0ooO = O0o0O00Oo0o0 ( oOo0oooo00o ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9tcDNfZG93bmxvYWRzLmh0bQ==' ) )
 O00O0oOO00O00 = re . compile ( '<td width=".+?" align="center">.+?<a href="(.*?)">.+?<img border="0" src="images/Squeeze%20(.*?).gif" width="74" height=".*?"></a></td>' , re . DOTALL ) . findall ( OOoOO0oo0ooO )
 for i1Oo00 , i1i in O00O0oOO00O00 :
  print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<' + i1Oo00 + '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
  if '-x' in i1i :
   pass
  else :
   III1i11 ( i1i , ( oOo0oooo00o ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) ) + ( i1Oo00 ) . replace ( 'colour_it' , 'books_audio/audio_books_a' ) , 30008 , ( oOo0oooo00o ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9pbWFnZXMvU3F1ZWV6ZSUyMA==' ) ) + i1i + '.gif' , oOOoO0 + 'kodible.png' , '' )
   if 31 - 31: o0000oOoOoO0o . O0oO * o0oO0 + i11iIiiIii * OoOO
 xbmcplugin . addSortMethod ( o0 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 93 - 93: ii11ii1ii / iIii1I11I1II1 * i1IIi % OoooooooOO * O0 * o0000oOoOoO0o
 if 64 - 64: OoOoOO00 + O0 / iIii1I11I1II1 / Oo . o0oO0 % IIII
def iiI1I1ii ( url ) :
 OOoOO0oo0ooO = O0o0O00Oo0o0 ( url )
 O00O0oOO00O00 = re . compile ( '<td width=".*?" height=".*?"><b>.*?<a href="(.*?)">(.*?)</a></b></td>' , re . DOTALL ) . findall ( OOoOO0oo0ooO )
 for url , iiI111I1iIiI in O00O0oOO00O00 :
  if '</a>' in iiI111I1iIiI :
   pass
  elif '(' in iiI111I1iIiI :
   III1i11 ( ( iiI111I1iIiI ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '.mp3' , '' ) , oOo0oooo00o ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) + url , 30005 , oOOoO0 + 'kodible.png' , oOOoO0 + 'kodible.png' , '' )
  else :
   iiiiiIIii ( ( iiI111I1iIiI ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '.mp3' , '' ) , oOo0oooo00o ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) + url , 30004 , oOOoO0 + 'kodible.png' , oOOoO0 + 'kodible.png' , '' )
   if 85 - 85: o0oO0 / O0
 xbmcplugin . addSortMethod ( o0 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 18 - 18: OOooOOo % O0 * ii11ii1ii
def o0Iii ( ) :
 Oo0oOOo = Oo0o0000o0o0 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OOO00O = Oo0oOOo . lower ( )
 OOoOO0oo0ooO = O0o0O00Oo0o0 ( oOo0oooo00o ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9jb21wbGV0ZV9saXN0Lmh0bQ==' ) )
 O00O0oOO00O00 = re . compile ( '<td width=".+?">.*?<b>.+?<a href="(.*?)">(.*?)</a></b></td>' , re . DOTALL ) . findall ( OOoOO0oo0ooO )
 for i1Oo00 , iiI111I1iIiI in O00O0oOO00O00 :
  if Oo0oOOo in iiI111I1iIiI . lower ( ) :
   if '</a>' in iiI111I1iIiI :
    pass
   elif '(' in iiI111I1iIiI :
    III1i11 ( ( iiI111I1iIiI ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , oOo0oooo00o ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + i1Oo00 , 30005 , oOOoO0 + 'kodible.png' , oOOoO0 + 'kodible.png' , '' )
   else :
    iiiiiIIii ( ( iiI111I1iIiI ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , oOo0oooo00o ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + i1Oo00 , 30004 , oOOoO0 + 'kodible.png' , oOOoO0 + 'kodible.png' , '' )
    if 19 - 19: o0000oOoOoO0o % OoOoOO00 / i11iIiiIii / oO0o0ooO0 - OoooooooOO
    if 37 - 37: OoOO0ooOOoo0O / OoooooooOO - i11iIiiIii
def i1iIiIi1I ( ) :
 OOoOO0oo0ooO = O0o0O00Oo0o0 ( oOo0oooo00o ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9jb21wbGV0ZV9saXN0Lmh0bQ==' ) )
 O00O0oOO00O00 = re . compile ( '<td width=".+?">.*?<b>.+?<a href="(.*?)">(.*?)</a></b></td>' , re . DOTALL ) . findall ( OOoOO0oo0ooO )
 for i1Oo00 , iiI111I1iIiI in O00O0oOO00O00 :
  if '</a>' in iiI111I1iIiI :
   pass
  elif '(' in iiI111I1iIiI :
   III1i11 ( ( iiI111I1iIiI ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , oOo0oooo00o ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + i1Oo00 , 30005 , oOOoO0 + 'kodible.png' , oOOoO0 + 'kodible.png' , '' )
  else :
   iiiiiIIii ( ( iiI111I1iIiI ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , oOo0oooo00o ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + i1Oo00 , 30004 , oOOoO0 + 'kodible.png' , oOOoO0 + 'kodible.png' , '' )
   if 45 - 45: i1IIi + OoOoOO00
 xbmcplugin . addSortMethod ( o0 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 7 - 7: O0 % OOooOOo + ii11ii1ii * oO0o0ooO0 - oO0o0ooO0
 if 42 - 42: I1IiI * I1IiI * O0oO . o0000oOoOoO0o
def O0Oo0o000oO ( url ) :
 OOoOO0oo0ooO = O0o0O00Oo0o0 ( url )
 O00O0oOO00O00 = re . compile ( '<a href="(.+?)">Download</a></b></td>' ) . findall ( OOoOO0oo0ooO )
 for url in O00O0oOO00O00 :
  i1iIi = ( oOo0oooo00o ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) ) + url
  Resolve ( i1iIi )
  if 99 - 99: OoOO * OoOoOO00 * O0oO
def oOooO0OOOoO000 ( url ) :
 OOoOO0oo0ooO = O0o0O00Oo0o0 ( url )
 O00O0oOO00O00 = re . compile ( '<td width="247">(.*?)</td>.*?<a href="(.+?)">' , re . DOTALL ) . findall ( OOoOO0oo0ooO )
 for iiI111I1iIiI , url in O00O0oOO00O00 :
  if '<p align' in iiI111I1iIiI :
   pass
  elif '&nbsp;' in iiI111I1iIiI :
   pass
  else :
   iiiiiIIii ( ( iiI111I1iIiI ) . replace ( '&nbsp;' , '' ) , oOo0oooo00o ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) + url , 10012 , oOOoO0 + 'kodible.png' , oOOoO0 + 'kodible.png' , '' )
   if 57 - 57: OoOoOO00
 xbmcplugin . addSortMethod ( o0 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 54 - 54: Oo + OoOO + i11iIiiIii
 if 28 - 28: OoOO
def ooo000o0ooO0 ( ) :
 OOoOO0oo0ooO = cloudflare . source ( oOo0oooo00o ( 'aHR0cDovL3dhdGNoY2FydG9vbnNvbmxpbmUuZXUv' ) )
 O00O0oOO00O00 = re . compile ( 'class="menu-item menu-item-type-.+?><a href="([^"]*)">(.+?)</a></li>' , re . DOTALL ) . findall ( OOoOO0oo0ooO )
 for i1Oo00 , iiI111I1iIiI in O00O0oOO00O00 :
  if 'ongoing' in i1Oo00 :
   iiiiiIIii ( '[COLORgreen]' + iiI111I1iIiI + '[/COLOR]' , i1Oo00 , 21005 , oOOoO0 + 'on-going.png' , '' , '' )
  if 'cartoon-series' in i1Oo00 :
   iiiiiIIii ( '[COLORgreen]' + iiI111I1iIiI + '[/COLOR]' , i1Oo00 , 21005 , oOOoO0 + 'cartoonseries.png' , '' , '' )
  if 'disney' in i1Oo00 :
   iiiiiIIii ( '[COLORgreen]' + iiI111I1iIiI + '[/COLOR]' , i1Oo00 , 21005 , oOOoO0 + 'disneytoons.png' , '' , '' )
  if 'genre' in i1Oo00 :
   iiiiiIIii ( '[COLORgreen]' + iiI111I1iIiI + '[/COLOR]' , i1Oo00 , 21005 , oOOoO0 + 'cartoongenre.png' , '' , '' )
  if 'years' in i1Oo00 :
   iiiiiIIii ( '[COLORgreen]' + iiI111I1iIiI + '[/COLOR]' , i1Oo00 , 21005 , oOOoO0 + 'years.png' , '' , '' )
def I1IoOoo000 ( url ) :
 OOoOO0oo0ooO = cloudflare . source ( url )
 O00O0oOO00O00 = re . compile ( '<a href="([^"]*)" title="([^"]*)" rel="nofollow" id="featured-thumbnail">.+?<div class="featured-thumbnail"><img width="140" height="200" src="([^"]*)"' , re . DOTALL ) . findall ( OOoOO0oo0ooO )
 OooOo00o = re . compile ( '<button type="button"><a href="([^"]*)" target="_blank">(.+?)</a>' ) . findall ( OOoOO0oo0ooO )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' ) . findall ( OOoOO0oo0ooO )
 for url , iiI111I1iIiI , i1i in O00O0oOO00O00 :
  iiiiiIIii ( '[COLORgreen]' + iiI111I1iIiI + '[/COLOR]' , url , 21006 , i1i , i1i , iiI111I1iIiI )
 for url , iiI111I1iIiI in OooOo00o :
  iiiiiIIii ( '[COLORgreen]' + iiI111I1iIiI + '[/COLOR]' , url , 21005 , oOOoO0 + 'watchcartoons.png' , '' , '' )
 for url in next :
  iiiiiIIii ( '[COLORgreen]NEXT[/COLOR]' , url , 21005 , oOOoO0 + 'watchcartoons.png' , '' , '' )
def IiI11i1IIiiI ( url ) :
 OOoOO0oo0ooO = cloudflare . source ( url )
 O00O0oOO00O00 = re . compile ( '<li><a href="([^"]*)" >(.+?)</a></li>' , re . DOTALL ) . findall ( OOoOO0oo0ooO )
 oOOo000oOoO0 = re . compile ( 'file:"([^"]*)",type:"mp4",label:"([^"]*)"' , re . DOTALL ) . findall ( OOoOO0oo0ooO )
 OoOo00o0OO = re . compile ( 'src="([^"]*)" frameborder=' ) . findall ( OOoOO0oo0ooO )
 ii1IIIIiI11 = re . compile ( '<iframe src="([^"]*)"' ) . findall ( OOoOO0oo0ooO )
 for url , iiI111I1iIiI in O00O0oOO00O00 :
  iiiiiIIii ( '[COLORgreen]' + iiI111I1iIiI + '[/COLOR]' , url , 21007 , oOOoO0 + 'watchcartoons.png' , '' , '' )
 for url in OoOo00o0OO :
  iiiiiIIii ( '[COLORgreen]PLAY[/COLOR]' , 'http:' + url , 222 , oOOoO0 + 'watchcartoons.png' , '' , '' )
 for url , iiI111I1iIiI in oOOo000oOoO0 :
  o0OOoo0OO0OOO ( '[COLORgreen]' + iiI111I1iIiI + '[/COLOR]' , url , 222 , oOOoO0 + 'watchcartoons.png' , '' , '' )
 else :
  iiiiiIIii ( '[COLORgreen]NO STREAMS AVAILABLE[/COLOR]' , url , 21005 , oOOoO0 + 'watchcartoons.png' , '' , '' )
def iI1IIIii ( url ) :
 OOoOO0oo0ooO = cloudflare . source ( url )
 O00O0oOO00O00 = re . compile ( 'file:"([^"]*)",type:"mp4",label:"([^"]*)"' , re . DOTALL ) . findall ( OOoOO0oo0ooO )
 for url , iiI111I1iIiI in O00O0oOO00O00 :
  o0OOoo0OO0OOO ( '[COLORgreen]' + iiI111I1iIiI + '[/COLOR]' , url , 222 , oOOoO0 + 'watchcartoons.png' , '' , '' )
  if 7 - 7: IIII - o0000oOoOoO0o / OoOoOO00 * o00O0oo . oO0o0ooO0 * oO0o0ooO0
def O0O0oOOo0O ( ) :
 oOIIiIi ( '[COLORgreen]CARTOONS[/COLOR]' , '' , 20001 , oOOoO0 + 'ORIGINCARTOON.png' )
 oOIIiIi ( '[COLORgreen]ANIME[/COLOR]' , 'https://kissanime.to/AnimeList' , 20001 , oOOoO0 + 'ORIGINCARTOON.png' )
 if 19 - 19: OOooOOo / O0oO % OOooOOo % oO0o0ooO0 * IIII
def ii1 ( ) :
 oOIIiIi ( '[COLORgreen]BY NAME[/COLOR]' , 'http://kisscartoon.me/CartoonList' , 20002 , oOOoO0 + 'ORIGINCARTOON.png' )
 oOIIiIi ( '[COLORgreen]BY GENRE[/COLOR]' , 'http://kisscartoon.me/CartoonList' , 20003 , oOOoO0 + 'ORIGINCARTOON.png' )
 if 77 - 77: OOOo0 % O0
def I1iii ( url ) :
 OOoOO0oo0ooO = cloudflare . source ( url )
 O00O0oOO00O00 = re . compile ( 'href="(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( OOoOO0oo0ooO )
 for url , iiI111I1iIiI in O00O0oOO00O00 :
  if '?c=' in url :
   oOIIiIi ( '[COLORgreen]' + iiI111I1iIiI + '[/COLOR]' , 'http://kisscartoon.me' + url , 20004 , oOOoO0 + 'ORIGINCARTOON.png' )
   if 86 - 86: ii11ii1ii * O0 * IIII
def Ooo0oo ( url ) :
 OOoOO0oo0ooO = cloudflare . source ( url )
 O00O0oOO00O00 = re . compile ( 'href="(.+?)" title="(.+?)">/n(.+?)</a><br/>' , re . DOTALL ) . findall ( OOoOO0oo0ooO )
 for url , IIi11IIiIii1 , iiI111I1iIiI in O00O0oOO00O00 :
  if 'Genre' in url :
   oOIIiIi ( '[COLORgreen]' + iiI111I1iIiI + '[/COLOR]' , 'http://kisscartoon.me' + url , 20004 , oOOoO0 + 'ORIGINCARTOON.png' )
   if 17 - 17: o00O0oo + OoOO . Ooo00oOo00o - Oo * i11iIiiIii
def iioOo0OoOOo0 ( url ) :
 OOoOO0oo0ooO = cloudflare . source ( url )
 O00O0oOO00O00 = re . compile ( 'src="(.+?)" style=.+?<a class="bigChar" href="(.+?)">(.+?)</a>.+?<p>(.+?)</p>' , re . DOTALL ) . findall ( OOoOO0oo0ooO )
 for url , IIi11IIiIii1 , iiI111I1iIiI in O00O0oOO00O00 :
  iiiiiIIii ( '[COLORgreen]' + iiI111I1iIiI + '[/COLOR]' , 'http://kisscartoon.me' + url , 20005 , img , '' , IIi11IIiIii1 )
  if 30 - 30: ii11ii1ii % OOOo0
def O0Oo00 ( url ) :
 OOoOO0oo0ooO = cloudflare . source ( url )
 O00O0oOO00O00 = re . compile ( '<img width="120" height="165" src="(.+?)" style=.+?<a class="bigChar" href="(.+?)">(.+?)</a>.+?<p>(.+?)</p>' , re . DOTALL ) . findall ( OOoOO0oo0ooO )
 for url , IIi11IIiIii1 , iiI111I1iIiI in O00O0oOO00O00 :
  iiiiiIIii ( '[COLORgreen]' + iiI111I1iIiI + '[/COLOR]' , 'http://kisscartoon.me' + url , 20005 , img , '' , IIi11IIiIii1 )
  if 41 - 41: iIii1I11I1II1 % o0000oOoOoO0o
  if 59 - 59: OoOO0ooOOoo0O + i11iIiiIii
  if 88 - 88: i11iIiiIii - o0oO0
  if 67 - 67: OoOO0ooOOoo0O . Oo + I1IiI - OoooooooOO
  if 70 - 70: OoOO0ooOOoo0O / OoOoOO00 - iIii1I11I1II1 - oO0o0ooO0
def Iii ( ) :
 if 20 - 20: OOooOOo / i1IIi
 iiiiiIIii ( '[COLORgreen]Cartoons[/COLOR]' , '' , 10004 , oOOoO0 + 'ORIGINCARTOON.png' , OOooO0OOoo , '' )
 iiiiiIIii ( '[COLORgreen]Search Cartoons[/COLOR]' , '' , 10005 , oOOoO0 + 'ORIGINCARTOON.png' , OOooO0OOoo , '' )
 if 71 - 71: I1IiI . i1IIi
def o0OooO0ooo0o ( ) :
 Oo0oOOo = Oo0o0000o0o0 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OOO00O = Oo0oOOo . lower ( )
 OOoOO0oo0ooO = O0o0O00Oo0o0 ( oOo0oooo00o ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2NhcnRvb24=' ) )
 O00O0oOO00O00 = re . compile ( '<td><a href="(.+?)">(.+)</a></td>' ) . findall ( OOoOO0oo0ooO )
 for i1Oo00 , iiI111I1iIiI in O00O0oOO00O00 :
  if Oo0oOOo in iiI111I1iIiI . lower ( ) :
   if 'Dad!' in iiI111I1iIiI :
    pass
   elif 'Family Guy' in iiI111I1iIiI :
    pass
   elif '2 Stupid' in iiI111I1iIiI :
    pass
   elif 'The Zelfs' in iiI111I1iIiI :
    pass
   elif 'A Clone' in iiI111I1iIiI :
    pass
   elif 'A.T.O.M' in iiI111I1iIiI :
    pass
   elif 'Almost Naked' in iiI111I1iIiI :
    pass
   elif 'Angry Kid' in iiI111I1iIiI :
    pass
   elif 'Annoying Orange' in iiI111I1iIiI :
    pass
   elif 'Aqua Teen' in iiI111I1iIiI :
    pass
   elif 'Assy Mcgee' in iiI111I1iIiI :
    pass
   elif 'Astroblast' in iiI111I1iIiI :
    pass
   elif 'Atomic Betty' in iiI111I1iIiI :
    pass
   elif 'Axe Cop' in iiI111I1iIiI :
    pass
   elif 'Baby Playpen' in iiI111I1iIiI :
    pass
   elif 'Beavis and Butt' in iiI111I1iIiI :
    pass
   elif 'Celebrity Deathmatch' in iiI111I1iIiI :
    pass
   elif 'Clerks The' in iiI111I1iIiI :
    pass
   elif 'Crapston Villas' in iiI111I1iIiI :
    pass
   elif 'Duckman:' in iiI111I1iIiI :
    pass
   elif 'Stripperella' in iiI111I1iIiI :
    pass
   elif 'Vixen' in iiI111I1iIiI :
    pass
   else :
    iiiiiIIii ( '[COLORgreen]' + iiI111I1iIiI + '[/COLOR]' , i1Oo00 , 10006 , oOOoO0 + 'ORIGINCARTOON.png' , OOooO0OOoo , '' )
  xbmcplugin . addSortMethod ( o0 , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 47 - 47: OoooooooOO
def ii1i1i1IiII ( ) :
 Ooo0O0oooo = O0o0O00Oo0o0 ( oOo0oooo00o ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2NhcnRvb24=' ) )
 O00O0oOO00O00 = re . compile ( '<td><a href="(.+?)">(.+)</a></td>' ) . findall ( Ooo0O0oooo )
 for i1Oo00 , iiI111I1iIiI in O00O0oOO00O00 :
  if 'Dad!' in iiI111I1iIiI :
   pass
  elif 'Family Guy' in iiI111I1iIiI :
   pass
  elif '2 Stupid' in iiI111I1iIiI :
   pass
  elif 'The Zelfs' in iiI111I1iIiI :
   pass
  elif 'A Clone' in iiI111I1iIiI :
   pass
  elif 'A.T.O.M' in iiI111I1iIiI :
   pass
  elif 'Almost Naked' in iiI111I1iIiI :
   pass
  elif 'Angry Kid' in iiI111I1iIiI :
   pass
  elif 'Annoying Orange' in iiI111I1iIiI :
   pass
  elif 'Aqua Teen' in iiI111I1iIiI :
   pass
  elif 'Assy Mcgee' in iiI111I1iIiI :
   pass
  elif 'Astroblast' in iiI111I1iIiI :
   pass
  elif 'Atomic Betty' in iiI111I1iIiI :
   pass
  elif 'Axe Cop' in iiI111I1iIiI :
   pass
  elif 'Baby Playpen' in iiI111I1iIiI :
   pass
  elif 'Beavis and Butt' in iiI111I1iIiI :
   pass
  elif 'Celebrity Deathmatch' in iiI111I1iIiI :
   pass
  elif 'Clerks The' in iiI111I1iIiI :
   pass
  elif 'Crapston Villas' in iiI111I1iIiI :
   pass
  elif 'Duckman:' in iiI111I1iIiI :
   pass
  elif 'Stripperella' in iiI111I1iIiI :
   pass
  elif 'Vixen' in iiI111I1iIiI :
   pass
  else :
   iiiiiIIii ( '[COLORgreen]' + iiI111I1iIiI + '[/COLOR]' , i1Oo00 , 10006 , oOOoO0 + 'ORIGINCARTOON.png' , OOooO0OOoo , '' )
 xbmcplugin . addSortMethod ( o0 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 63 - 63: oO0o0ooO0 . Ooo00oOo00o / OoOoOO00 * IIII + OoOO % o00O0oo
def I1 ( url ) :
 Ooo0O0oooo = O0o0O00Oo0o0 ( url )
 OOo0 = re . compile ( '<img src="(.+?)" id="series_image" width="250" height="370" alt=".+?" />' ) . findall ( Ooo0O0oooo )
 for i1i in OOo0 :
  i11iIIi11 = i1i
 ooOooo000OO00 = re . compile ( '<li><a href="(.+?)">Next</a></li>' ) . findall ( Ooo0O0oooo )
 for url in ooOooo000OO00 :
  iiiiiIIii ( '[COLORgreen]NEXT PAGE[/COLOR]' , url , 10006 , i11iIIi11 , OOooO0OOoo , '' )
 O00O0oOO00O00 = re . compile ( '&nbsp;<a href="(.+?)">(.+?)</a>' ) . findall ( Ooo0O0oooo )
 for url , iiI111I1iIiI in O00O0oOO00O00 :
  oOOO00o000o ( '[COLORgreen]' + iiI111I1iIiI + '[/COLOR]' , url , 10007 , i11iIIi11 )
  if 34 - 34: O0 % i1IIi - OoOO0ooOOoo0O + Oo
  if 84 - 84: O0 * OoooooooOO - IIII * IIII
 xbmcplugin . addSortMethod ( o0 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 8 - 8: o0oO0 / i1IIi . OoOO
def i1I1IiI ( url , IMAGE ) :
 Ooo0O0oooo = O0o0O00Oo0o0 ( url )
 O00O0oOO00O00 = re . compile ( '"playlist">(.+?)</span></div><div><iframe src="(.+?)"' ) . findall ( Ooo0O0oooo )
 for iiI111I1iIiI , url in O00O0oOO00O00 :
  print iiI111I1iIiI + '     ' + url
  if 'easy' in url :
   oOooOO ( url )
   if 31 - 31: OoOO0ooOOoo0O / Oo * i1IIi . I1IiI
   if 57 - 57: OoOO0ooOOoo0O + iIii1I11I1II1 % i1IIi % OOOo0
  xbmcplugin . addSortMethod ( o0 , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 83 - 83: OOooOOo / i11iIiiIii % iIii1I11I1II1 . o0000oOoOoO0o % OoOO . OoooooooOO
def oOooOO ( url ) :
 Ooo0O0oooo = O0o0O00Oo0o0 ( url )
 O00O0oOO00O00 = re . compile ( "url: '(.+?)'," ) . findall ( Ooo0O0oooo )
 for url in O00O0oOO00O00 :
  o00oO00 ( url )
  if 59 - 59: OoOO0ooOOoo0O + iIii1I11I1II1 * OOooOOo + O0oO . oO0o0ooO0
  if 49 - 49: OoooooooOO * o0000oOoOoO0o - Oo . OoOO
  if 89 - 89: o0oO0 + o00O0oo * o0oO0 / o0oO0
def i11i11 ( ) :
 if 72 - 72: i1IIi - OoOoOO00 - OoOO0ooOOoo0O + OoOO0ooOOoo0O * OOooOOo * OoOO0ooOOoo0O
 iiiiiIIii ( '[COLORgreen]Stand Up[/COLOR]' , '' , 10014 , oOOoO0 + 'ORIGINSTANDUP.png' , OOooO0OOoo , '' )
 iiiiiIIii ( '[COLORgreen]Search Comedian[/COLOR]' , '' , 10015 , oOOoO0 + 'ORIGINSTANDUP.png' , OOooO0OOoo , '' )
 iiiiiIIii ( '[COLORgreen]Others[/COLOR]' , '' , 10017 , oOOoO0 + 'ORIGINSTANDUP.png' , OOooO0OOoo , '' )
 if 33 - 33: Oo
def II11i11Iii ( ) :
 OOoOO0oo0ooO = O0o0O00Oo0o0 ( ( oOo0oooo00o ( 'aHR0cDovL2JhY2syYmFzaWNzYnVpbGQuY28udWsvdGVzdC9zdGFuZHVwbGlzdC5waHA=' ) ) )
 O00O0oOO00O00 = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( OOoOO0oo0ooO )
 for i1Oo00 , i1i , iiI111I1iIiI in O00O0oOO00O00 :
  oOOO00o000o ( '[COLORgreen]' + iiI111I1iIiI + '[/COLOR]' , i1Oo00 , 222 , i1i )
  if 68 - 68: OoooooooOO % OoOoOO00
def Ii1i1i1111 ( ) :
 Oo0oOOo = Oo0o0000o0o0 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OOO00O = Oo0oOOo . lower ( )
 OOoOO0oo0ooO = O0o0O00Oo0o0 ( ( oOo0oooo00o ( 'aHR0cDovL3d3dy5jb3VjaHRyaXBwZXIuY29tL2ZvcnVtMi9wYWdlLnBocD9wYWdlPTM=' ) ) )
 o0oO0O00oOo = re . compile ( '<tr>.+?<td width=".+?" align=".+?">.+?<img border=".+?" src="..(.+?)" width=".+?" height=".+?"></td>.+?<td width=".+?" valign=".+?" align=".+?"><font size=".+?">(.+?)</font></td>.+?<td width=".+?">(.+?)</td>' , re . DOTALL ) . findall ( OOoOO0oo0ooO )
 for i1i , I1111I1II11 , iIiiiI1IiI1I1 in o0oO0O00oOo :
  for Oo0oOOo in I1111I1II11 :
   print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< img >>>>>>>>>>>>>>>>>>>>>>>>>>'
   iiiIIIIiIi = re . compile ( '<a href="(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( iIiiiI1IiI1I1 )
   for i1Oo00 , iiI111I1iIiI in iiiIIIIiIi :
    if 'tube' in i1Oo00 :
     pass
    elif 'stage' in i1Oo00 :
     oOOO00o000o ( '[COLORgreen]' + I1111I1II11 + '   -   ' + iiI111I1iIiI + '[/COLOR]' , ( i1Oo00 ) . replace ( '" target="_blank' , '' ) , 10016 , 'http://couchtripper.com/' + i1i , )
    elif 'vee' in i1Oo00 :
     pass
     if 34 - 34: OoooooooOO . O0 / OoOO * I1IiI - ii11ii1ii
def IiiiI ( ) :
 OOoOO0oo0ooO = O0o0O00Oo0o0 ( ( oOo0oooo00o ( 'aHR0cDovL3d3dy5jb3VjaHRyaXBwZXIuY29tL2ZvcnVtMi9wYWdlLnBocD9wYWdlPTM=' ) ) )
 o0oO0O00oOo = re . compile ( '<tr>.+?<td width=".+?" align=".+?">.+?<img border=".+?" src="..(.+?)" width=".+?" height=".+?"></td>.+?<td width=".+?" valign=".+?" align=".+?"><font size=".+?">(.+?)</font></td>.+?<td width=".+?">(.+?)</td>' , re . DOTALL ) . findall ( OOoOO0oo0ooO )
 for i1i , I1111I1II11 , iIiiiI1IiI1I1 in o0oO0O00oOo :
  iiiIIIIiIi = re . compile ( '<a href="(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( iIiiiI1IiI1I1 )
  for i1Oo00 , iiI111I1iIiI in iiiIIIIiIi :
   if 'tube' in i1Oo00 :
    pass
   elif 'stage' in i1Oo00 :
    oOOO00o000o ( '[COLORgreen]' + I1111I1II11 + '   -   ' + iiI111I1iIiI + '[/COLOR]' , ( i1Oo00 ) . replace ( '" target="_blank' , '' ) , 10016 , 'http://couchtripper.com/' + i1i )
   elif 'vee' in i1Oo00 :
    pass
    if 42 - 42: i1IIi . OOOo0 / i1IIi + o00O0oo
    if 54 - 54: o0oO0 % OoOO0ooOOoo0O . O0oO + OoOO - OoOO0ooOOoo0O * OOOo0
 xbmcplugin . addSortMethod ( o0 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 92 - 92: OOooOOo + O0oO / Oo % Ooo00oOo00o % IIII . OoooooooOO
def O0Oo ( url ) :
 OOoOO0oo0ooO = O0o0O00Oo0o0 ( url )
 print '>>>>>>>>>>>>>>>>>>>>>>>>' + url + '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'
 I1IiI111I11 = re . compile ( "url\[.+?\] = '(.+?)';" ) . findall ( OOoOO0oo0ooO )
 print '>>>>>>>>>>>>>>>>>>>>>>>' + ( str ( I1IiI111I11 ) ) + '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
 for url in I1IiI111I11 :
  o00oO00 ( ( url ) . replace ( '[' , '' ) . replace ( ']' , '' ) . replace ( '\'' , '' ) )
  if 16 - 16: O0 / o00O0oo . ii11ii1ii
  if 58 - 58: Oo / OoOO
  if 44 - 44: OoOO0ooOOoo0O
  if 54 - 54: o00O0oo - o0000oOoOoO0o - O0oO . iIii1I11I1II1
  if 79 - 79: o00O0oo . Ooo00oOo00o
  if 40 - 40: OOooOOo + Oo . OOooOOo % o0oO0
  if 15 - 15: o00O0oo * Oo % ii11ii1ii * iIii1I11I1II1 - i11iIiiIii
def Oo00OOOOoo0oo ( ) :
 if 80 - 80: O0oO * I1IiI * OoOoOO00 - O0 . I1IiI % OOOo0
 II1 ( '[COLOR darkgoldenrod]Open Pandora\'s Box[/COLOR]' , '' , 10029 , 'https://encrypted-tbn1.gstatic.com/images?q=tbn%3AANd9GcTQ9r4TA8yIw9ggxuwsHxWojo6tPVfgTe8QIOxOQwzNR2TavtCi6Q' , OOooO0OOoo , '' )
 II1 ( '[COLOR darkgoldenrod]Search[/COLOR]' , '' , 10026 , 'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png' , OOooO0OOoo , '' )
 if 32 - 32: OOOo0 - ii11ii1ii - Oo
 Oooo0Ooo000 ( 'movies' , 'MAIN' )
 if 32 - 32: i1IIi . o0000oOoOoO0o / Ooo00oOo00o
def o0OOoOoO00 ( ) :
 II1 ( 'Search Pandoras Films' , '' , 10027 , oOOoO0 + 'PANDORASBOX.png' , OOooO0OOoo , '' )
 II1 ( 'Search Pandoras TV' , '' , 10028 , oOOoO0 + 'PANDORASBOX.png' , OOooO0OOoo , '' )
 if 15 - 15: IIII / O0 . OOooOOo . i11iIiiIii
 Oooo0Ooo000 ( 'movies' , 'MAIN' )
def o0OO0O0Oo ( ) :
 if 78 - 78: I1IiI / Oo - OoOO0ooOOoo0O - oO0o0ooO0 * OoOO
 Oo0oOOo = Oo0o0000o0o0 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OOO00O = Oo0oOOo . lower ( )
 Ii1I11I = [ 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' ]
 if 36 - 36: O0 + Oo
 for iIIIi1i1I11i in Ii1I11I :
  oOO0OO0OO = Base_Pand + iIIIi1i1I11i + O0o0Oo
  OOoOO0oo0ooO = O0o0O00Oo0o0 ( oOO0OO0OO )
  O00O0oOO00O00 = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( OOoOO0oo0ooO )
  for i1Oo00 , oo000 , oOOoooO , o0000oO , iiI111I1iIiI in O00O0oOO00O00 :
   if Oo0oOOo in iiI111I1iIiI . lower ( ) :
    i1ii11 ( iiI111I1iIiI , i1Oo00 , 222 , oo000 , o0000oO , oOOoooO )
    if 49 - 49: OoooooooOO / i11iIiiIii * i11iIiiIii
    Oooo0Ooo000 ( 'movies' , 'MAIN' )
    xbmcplugin . addSortMethod ( o0 , xbmcplugin . SORT_METHOD_TITLE ) ;
    if 58 - 58: OoOO
    if 4 - 4: OoOoOO00 . o0oO0 / ii11ii1ii - i11iIiiIii
def OoO00 ( ) :
 if 18 - 18: o00O0oo - OoooooooOO % OoOoOO00 - OOOo0 % I1IiI
 Oo0oOOo = Oo0o0000o0o0 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OOO00O = Oo0oOOo . lower ( )
 Ii1I11I = [ 'a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' , 'p' , 'q' , 'r' , 's' , 't' , 'u' , 'v' , 'w' , 'x' , 'y' , 'z' ]
 if 60 - 60: iIii1I11I1II1 + i1IIi
 for iIIIi1i1I11i in Ii1I11I :
  OooOOo0 = Base_Pand + iIIIi1i1I11i + O0o0Oo
  OOoOO0oo0ooO = O0o0O00Oo0o0 ( OooOOo0 )
  O00O0oOO00O00 = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( OOoOO0oo0ooO )
  for iiI111I1iIiI , oOOoooO , i1Oo00 , i1i , o0000oO , ooO000O in O00O0oOO00O00 :
   if Oo0oOOo in iiI111I1iIiI . lower ( ) :
    II1 ( iiI111I1iIiI , i1Oo00 , ooO000O , i1i , o0000oO , oOOoooO )
    if 53 - 53: OOooOOo . oO0o0ooO0 / o00O0oo
    Oooo0Ooo000 ( 'movies' , 'MAIN' )
    xbmcplugin . addSortMethod ( o0 , xbmcplugin . SORT_METHOD_TITLE ) ;
    if 39 - 39: o00O0oo % O0 % I1IiI . i1IIi
    if 86 - 86: Ooo00oOo00o * OoooooooOO
def OooO0oOo ( ) :
 if 66 - 66: Ooo00oOo00o * Oo
 Ooo0O0oooo = O0o0O00Oo0o0 ( oOo0oooo00o ( 'aHR0cDovL3NlZWR1cmdyZWVkLngxMGhvc3QuY29tL29yaWdpbi9zcG9uZ2VtYWluLnBocA==' ) )
 O00O0oOO00O00 = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( Ooo0O0oooo )
 for iiI111I1iIiI , oOOoooO , i1Oo00 , i1i , o0000oO , ooO000O in O00O0oOO00O00 :
  II1 ( iiI111I1iIiI , i1Oo00 , ooO000O , i1i , o0000oO , oOOoooO )
  Oooo0Ooo000 ( 'movies' , 'MAIN' )
def II1IIIiiI11 ( url ) :
 if 86 - 86: Ooo00oOo00o % OoooooooOO % Ooo00oOo00o / OOOo0
 xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
 Oo0ooo0Ooo = ( '%s%s' % ( i1II1I , url ) )
 o0ooooO0o0O = O0o0O00Oo0o0 ( url )
 O00O0oOO00O00 = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( o0ooooO0o0O )
 for url , oo000 , oOOoooO , OOoO0ooOO , iiI111I1iIiI in O00O0oOO00O00 :
  i1ii11 ( iiI111I1iIiI , url , 222 , oo000 , OOoO0ooOO , oOOoooO )
  if 24 - 24: i1IIi . i11iIiiIii
  Oooo0Ooo000 ( 'movies' , 'MAIN' )
  if 16 - 16: Oo % ii11ii1ii + o0000oOoOoO0o - O0 . oO0o0ooO0 / O0oO
  xbmcplugin . addSortMethod ( o0 , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 35 - 35: OoOO / O0oO / OoOoOO00 - iIii1I11I1II1 + OoOoOO00 . O0oO
  if 81 - 81: oO0o0ooO0 * OoOO0ooOOoo0O - ii11ii1ii * o00O0oo % I1IiI * I1IiI
def ooO ( url ) :
 if 100 - 100: OOOo0 / OOooOOo * oO0o0ooO0 . O0 / OoOO0ooOOoo0O
 Ooo0O0oooo = O0o0O00Oo0o0 ( url )
 O00O0oOO00O00 = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( Ooo0O0oooo )
 for iiI111I1iIiI , oOOoooO , url , i1i , o0000oO , ooO000O in O00O0oOO00O00 :
  II1 ( iiI111I1iIiI , url , ooO000O , i1i , o0000oO , oOOoooO )
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
def II1 ( name , url , mode , iconimage , fanart , description ) :
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
 o0O = [ ]
 try :
  if 38 - 38: i1IIi + o00O0oo
  name = name . encode ( 'utf-8' , 'ignore' )
 except :
  pass
 if os . path . exists ( IIIII ) == False :
  OOooo00 ( 'Making Favorites File' )
  o0O . append ( ( name , url , iconimage , fanart , mode , playlist , regexs ) )
  i1Iii1i1I = open ( IIIII , "w" )
  i1Iii1i1I . write ( json . dumps ( o0O ) )
  i1Iii1i1I . close ( )
 else :
  OOooo00 ( 'Appending Favorites' )
  i1Iii1i1I = open ( IIIII ) . read ( )
  Oo00O0ooOO = json . loads ( i1Iii1i1I )
  Oo00O0ooOO . append ( ( name , url , iconimage , fanart , mode ) )
  O0o0OO0000ooo = open ( IIIII , "w" )
  O0o0OO0000ooo . write ( json . dumps ( Oo00O0ooOO ) )
  O0o0OO0000ooo . close ( )
  if 28 - 28: i11iIiiIii / OOooOOo . iIii1I11I1II1 / OoOoOO00
  if 72 - 72: OoooooooOO / OOOo0 + o00O0oo / I1IiI * o00O0oo
def Ii1iIi111i1i1 ( ) :
 IIOO0ooOo0OoOo0 = json . loads ( open ( IIIII ) . read ( ) )
 oOo = len ( IIOO0ooOo0OoOo0 )
 for i1iIIIiiiI in IIOO0ooOo0OoOo0 :
  iiI111I1iIiI = i1iIIIiiiI [ 0 ]
  i1Oo00 = i1iIIIiiiI [ 1 ]
  oo000 = i1iIIIiiiI [ 2 ]
  try :
   OoO00oo00 = i1iIIIiiiI [ 3 ]
   if OoO00oo00 == None :
    raise
  except :
   if o0oOoO00o . getSetting ( 'use_thumb' ) == "true" :
    OoO00oo00 = oo000
   else :
    OoO00oo00 = o0000oO
  try : Oo0Oo0O = i1iIIIiiiI [ 5 ]
  except : Oo0Oo0O = None
  try : iiiI1i11Ii = i1iIIIiiiI [ 6 ]
  except : iiiI1i11Ii = None
  if 16 - 16: Oo / i11iIiiIii
  if i1iIIIiiiI [ 4 ] == 0 :
   iiiiiIIii ( iiI111I1iIiI , i1Oo00 , '' , oo000 , o0000oO , '' , 'fav' )
  else :
   iiiiiIIii ( iiI111I1iIiI , i1Oo00 , i1iIIIiiiI [ 4 ] , oo000 , o0000oO , '' , 'fav' )
   if 64 - 64: i11iIiiIii / o00O0oo * i1IIi
def OOOOOOoO ( name ) :
 Oo00O0ooOO = json . loads ( open ( IIIII ) . read ( ) )
 for I1IIiI in range ( len ( Oo00O0ooOO ) ) :
  if Oo00O0ooOO [ I1IIiI ] [ 0 ] == name :
   del Oo00O0ooOO [ I1IIiI ]
   O0o0OO0000ooo = open ( IIIII , "w" )
   O0o0OO0000ooo . write ( json . dumps ( Oo00O0ooOO ) )
   O0o0OO0000ooo . close ( )
   break
 xbmc . executebuiltin ( "XBMC.Container.Refresh" )
 if 84 - 84: o0000oOoOoO0o - Oo / O0 - O0oO
 if 21 - 21: O0 * O0 % ii11ii1ii
 if 94 - 94: o0000oOoOoO0o + OoOoOO00 % i11iIiiIii
def i1i1IiIiIi1Ii ( ) :
 if 64 - 64: OoOO0ooOOoo0O + OoooooooOO * OoooooooOO
 iiiiiIIii ( '[COLORgreen]Recent Episodes[/COLOR]' , '' , 10019 , oOOoO0 + 'dtv.png' , OOooO0OOoo , '' )
 iiiiiIIii ( '[COLORgreen]Genres[/COLOR]' , '' , 10020 , oOOoO0 + 'dtv.png' , OOooO0OOoo , '' )
 iiiiiIIii ( '[COLORgreen]Search[/COLOR]' , '' , 10021 , oOOoO0 + 'dtv.png' , OOooO0OOoo , '' )
 if 41 - 41: o0oO0 . Oo + OOOo0
def o0O0OO ( ) :
 if 22 - 22: OoOoOO00 * Ooo00oOo00o * o0000oOoOoO0o + ii11ii1ii * OOooOOo
 Ooo0O0oooo = cloudflare . source ( oOo0oooo00o ( 'aHR0cDovL2RpemlsYWIuY29t' ) )
 O00O0oOO00O00 = re . compile ( '<li id=".+?">.+?<a href="(.+?)">.+?<img width="40" height="40" src="(.+?)" alt=""/>.+?<span class="title">\n(.+?)</span>.+?<span class="alt-title">\n(.+?)</span>.+?</a>.+?</li>' , re . DOTALL ) . findall ( Ooo0O0oooo )
 for i1Oo00 , i1i , iiI111I1iIiI , oo0o0 in O00O0oOO00O00 :
  iiiiiIIii ( iiI111I1iIiI + '  -  ' + ( oo0o0 ) . replace ( 'sezon' , 'Season' ) . replace ( 'bölüm' , 'Episode' ) , i1Oo00 , 10023 , oOOoO0 + 'dtv.png' , OOooO0OOoo , '' )
  if 69 - 69: ii11ii1ii - O0oO
  if 16 - 16: Oo
  if 14 - 14: i1IIi - O0 % Oo
def O0o00O0Oo0 ( ) :
 if 58 - 58: O0
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
 if 78 - 78: Ooo00oOo00o % IIII * i1IIi
def O0iI ( url ) :
 Ii1I = 'http://dizilab.com/arsiv?limit=100&tur=' + url + '&orderby=&ulke=&order=&yil=&dizi_adi='
 OOoOO0oo0ooO = cloudflare . source ( Ii1I )
 O00O0oOO00O00 = re . compile ( '<div class="tv-series-single">.+?<a href="(.+?)" class="film-image">.+?<img src="(.+?)" alt=""/>.+?<span class="position">.+?</span>\n(.+?)</a>' , re . DOTALL ) . findall ( OOoOO0oo0ooO )
 for url , i1i , iiI111I1iIiI in O00O0oOO00O00 :
  iiiiiIIii ( '[COLORgreen]' + iiI111I1iIiI + '[/COLOR]' , url , 10022 , oOOoO0 + 'dtv.png' , OOooO0OOoo , '' )
  if 45 - 45: i1IIi - Oo / O0 . ii11ii1ii
  if 5 - 5: OOooOOo . iIii1I11I1II1 % iIii1I11I1II1
  if 56 - 56: OoooooooOO - o0000oOoOoO0o - i1IIi
  if 8 - 8: O0oO / OoOO0ooOOoo0O . OOOo0 + ii11ii1ii / i11iIiiIii
def I1Iii1iI1 ( ) :
 if 86 - 86: O0
 Oo0oOOo = Oo0o0000o0o0 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OOO00O = Oo0oOOo . lower ( )
 i1Oo00 = ( oOo0oooo00o ( 'aHR0cDovL2RpemlsYWIuY29tL2Fyc2l2P2xpbWl0PSZ0dXI9Jm9yZGVyYnk9JnVsa2U9Jm9yZGVyPSZ5aWw9JmRpemlfYWRpPQ==' ) ) + ( Oo0oOOo ) . replace ( ' ' , '+' )
 OOoOO0oo0ooO = cloudflare . source ( i1Oo00 )
 O00O0oOO00O00 = re . compile ( '<a href="(.+?)" class="film-image">\n<img src="(.+?)" alt=""/>\n</a>\n<div class="tss-detail">\n<a class="title" style="" href=".+?">\n<span class="position">.+?</span>\n(.+?)</a>' ) . findall ( OOoOO0oo0ooO )
 for i1Oo00 , i1i , iiI111I1iIiI in O00O0oOO00O00 :
  if Oo0oOOo in iiI111I1iIiI . lower ( ) :
   iiiiiIIii ( '[COLORgreen]' + iiI111I1iIiI + '[/COLOR]' , i1Oo00 , 10022 , oOOoO0 + 'dtv.png' )
   if 95 - 95: oO0o0ooO0 * OoOO0ooOOoo0O . I1IiI . i1IIi . i1IIi - OOooOOo
   if 26 - 26: iIii1I11I1II1 % i11iIiiIii % ii11ii1ii
   if 67 - 67: OoooooooOO
def IiIiIi1I1 ( url ) :
 OOoOO0oo0ooO = cloudflare . source ( url )
 O00O0oOO00O00 = re . compile ( '<a class="season" href="(.+?)">\n(.+?)\n</a>.+?<a class="episode" href=".+?">\n(.+?)\n</a>.+?<a class="episode-name" href=".+?">\n(.+?)</a>' , re . DOTALL ) . findall ( OOoOO0oo0ooO )
 for i1iIi , IiI1ii1Ii , oooOOOoOOOo0O , iiI111I1iIiI in O00O0oOO00O00 :
  O00oOoo0OoO0 = ( oooOOOoOOOo0O ) . replace ( 'Sezon' , '' ) . replace ( 'bölüm' , '' ) . replace ( 'Bölüm' , '' ) . replace ( 'BÃ¶lÃ¼m' , '' ) . replace ( '.' , '' )
  Ooo0 = ( IiI1ii1Ii ) . replace ( 'bölüm' , '' ) . replace ( 'Sezon' , '' ) . replace ( 'Bölüm' , '' ) . replace ( 'BÃ¶lÃ¼m' , '' ) . replace ( '.' , '' )
  oooO00o0 = 'Season ' + Ooo0 + 'Episode ' + O00oOoo0OoO0 + iiI111I1iIiI
  o0o00oO0oo000 ( oooO00o0 , i1iIi )
  if 89 - 89: Ooo00oOo00o + IIII * O0oO
  xbmcplugin . addSortMethod ( o0 , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 28 - 28: OoooooooOO . OoOO % ii11ii1ii / i1IIi / OoOO0ooOOoo0O
  if 36 - 36: OOooOOo + o0000oOoOoO0o - IIII + iIii1I11I1II1 + OoooooooOO
def o0o00oO0oo000 ( name , url ) :
 i1iIi = url
 Ii = name
 I1i111IiIiIi1 = cloudflare . source ( i1iIi )
 OOo0 = re . compile ( 'file: "(.+?)",.+?label: "(.+?)",' , re . DOTALL ) . findall ( I1i111IiIiIi1 )
 for I1IiI111I11 , i1II11II1 in OOo0 :
  oOOO00o000o ( '[COLORgreen]' + Ii + i1II11II1 + '[/COLOR]' , I1IiI111I11 , 10012 , oOOoO0 + 'dtv.png' )
  if 5 - 5: Oo - ii11ii1ii % OoOO - OoOoOO00 . OOOo0 + oO0o0ooO0
 xbmcplugin . addSortMethod ( o0 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 47 - 47: O0 - iIii1I11I1II1 - oO0o0ooO0
 if 46 - 46: o00O0oo . OoOO0ooOOoo0O * Ooo00oOo00o . OoooooooOO + ii11ii1ii
def oo0000o ( ) :
 if 12 - 12: OOooOOo + o00O0oo + OOooOOo
 if 95 - 95: o00O0oo + ii11ii1ii * OoOO0ooOOoo0O
 if 16 - 16: o0000oOoOoO0o / OOOo0 + Ooo00oOo00o % iIii1I11I1II1 - i1IIi . OoOO
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
 iiiiiIIii ( '[COLORgreen]Newest Episodes Added[/COLOR]' , 'http://www.watchseries.li/latest' , 10046 , oOOoO0 + 'WATCHSERIES.png' , '' , '' )
 iiiiiIIii ( '[COLORgreen]This Week\'s Popular Episodes[/COLOR]' , 'http://www.watchseries.li/new' , 10042 , oOOoO0 + 'WATCHSERIES.png' , '' , '' )
 iiiiiIIii ( '[COLORgreen]Search Program[/COLOR]' , '' , 10043 , oOOoO0 + 'WATCHSERIES.png' , '' , '' )
 if 18 - 18: OoOO0ooOOoo0O + O0oO
 if 80 - 80: OoOO + OOooOOo * o00O0oo + Ooo00oOo00o
def O0oOo ( url ) :
 OOoOO0oo0ooO = O0o0O00Oo0o0 ( url )
 III1iII1I1ii = re . compile ( '<ul class="pagination" style="line-height: 3;">(.+?)</ul>' , re . DOTALL ) . findall ( OOoOO0oo0ooO )
 O00O0oOO00O00 = re . compile ( '<li><a href="/letters/(.+?)">(.+?)</a></li>' ) . findall ( str ( III1iII1I1ii ) )
 for url , iiI111I1iIiI in O00O0oOO00O00 :
  iiiiiIIii ( '[COLORgreen]' + iiI111I1iIiI + '[/COLOR]' , 'http://watchseries.li/letters/' + url , 10049 , oOOoO0 + 'WATCHSERIES.png' , '' , '' )
  if 69 - 69: Oo * OoOoOO00 * o0oO0 . oO0o0ooO0 - ii11ii1ii
def I11iiIIiI1ii ( url ) :
 OOoOO0oo0ooO = O0o0O00Oo0o0 ( url )
 O00O0oOO00O00 = re . compile ( '<a href="(.+?)" class="sr-header">(.+?)</a>' ) . findall ( OOoOO0oo0ooO )
 for url , iiI111I1iIiI in O00O0oOO00O00 :
  iiiiiIIii ( '[COLORgreen]' + iiI111I1iIiI + '[/COLOR]' , 'http://watchseries.li/' + url , 10049 , oOOoO0 + 'WATCHSERIES.png' , '' , '' )
  if 12 - 12: O0oO % i11iIiiIii + OOooOOo + O0oO / o0000oOoOoO0o
def O00 ( url ) :
 OOoOO0oo0ooO = O0o0O00Oo0o0 ( url )
 O00O0oOO00O00 = re . compile ( '<li class="col-md-6 col-xs-12 list-movies-li"><a href="(.+?)" title=".+?">(.+?)<span class="epnum">.+?</span></a></li>' , re . DOTALL ) . findall ( OOoOO0oo0ooO )
 OOo0 = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="(.+?)">Next</a></li></ul>' , re . DOTALL ) . findall ( OOoOO0oo0ooO )
 for url , iiI111I1iIiI in O00O0oOO00O00 :
  iiiiiIIii ( '[COLORgreen]' + ( iiI111I1iIiI ) . replace ( '&nbsp;' , ' ' ) . replace ( '&amp;' , '&' ) . replace ( '&#039;' , '\'' ) + '[/COLOR]' , 'http://www.watchseries.li' + url , 10044 , oOOoO0 + 'WATCHSERIES.png' , '' , '' )
 for url in OOo0 :
  iiiiiIIii ( '[COLORgreen]' + 'NEXT' + '[/COLOR]' , 'http://www.watchseries.li' + url , 10049 , '' , '' , '' )
  if 94 - 94: o0000oOoOoO0o . o0000oOoOoO0o + i11iIiiIii - OoOO0ooOOoo0O * ii11ii1ii
  if 9 - 9: OOooOOo . OOOo0 - ii11ii1ii
def IiiiIiiIIi ( ) :
 Oo0oOOo = Oo0o0000o0o0 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 i1iiIIiI1iiI = 'http://www.watchseries.li/search/' + Oo0oOOo . replace ( ' ' , '%20' )
 OOoOO0oo0ooO = O0o0O00Oo0o0 ( i1iiIIiI1iiI )
 O00O0oOO00O00 = re . compile ( '<img src="(.+?)".+?<a href="(.+?)" title=".+?"><b>(.+?)</b>' , re . DOTALL ) . findall ( OOoOO0oo0ooO )
 for i1i , i1Oo00 , iiI111I1iIiI in O00O0oOO00O00 :
  if 'watch online' in iiI111I1iIiI :
   pass
  else :
   print i1Oo00
   iiiiiIIii ( '[COLORgreen]' + iiI111I1iIiI + '[/COLOR]' , 'http://www.watchseries.li' + i1Oo00 , 10044 , i1i , '' , '' )
   if 18 - 18: oO0o0ooO0 - OoOO % oO0o0ooO0 / o0000oOoOoO0o
   xbmcplugin . setContent ( o0 , 'movies' )
   if 68 - 68: o00O0oo * iIii1I11I1II1 + O0oO % I1IiI
def IIii1I1I1I ( url ) :
 OOoOO0oo0ooO = O0o0O00Oo0o0 ( url )
 O00O0oOO00O00 = re . compile ( '<img src="(.+?)".+?<div class="block-left-home-inside-text">.+?<a href="(.+?)" title=".+?"><b>(.+?)</b> <br>.+?<span class=".+?">(.+?)</span></a><br>(.+?)<br>' , re . DOTALL ) . findall ( OOoOO0oo0ooO )
 for i1i , url , iiI111I1iIiI , oooOOOoOOOo0O , oOOoooO in O00O0oOO00O00 :
  OoOOOo0 = ( iiI111I1iIiI ) . replace ( '&nbsp;' , ' ' ) . replace ( '&amp;' , '&' ) . replace ( '&#039;' , '\'' ) + ' - ' + ( oooOOOoOOOo0O ) . replace ( '&amp;' , '&' ) . replace ( '&#039;' , '\'' )
  iiiiiIIii ( '[COLORgreen]' + OoOOOo0 + '[/COLOR]' , 'http://www.watchseries.li' + url , 10045 , i1i , '' , oOOoooO )
  if 61 - 61: iIii1I11I1II1
def OO0OO ( url ) :
 OOoOO0oo0ooO = O0o0O00Oo0o0 ( url )
 O00O0oOO00O00 = re . compile ( '<li class="col-md-6 col-xs-12 list-movies-li"><a href="(.+?)" title=".+?">(.+?)<span class="epnum">.+?</span></a></li>' , re . DOTALL ) . findall ( OOoOO0oo0ooO )
 OOo0 = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="(.+?)">Next</a></li></ul>' , re . DOTALL ) . findall ( OOoOO0oo0ooO )
 for url , iiI111I1iIiI in O00O0oOO00O00 :
  OoOOOo0 = ( iiI111I1iIiI ) . replace ( '&nbsp;' , ' ' ) . replace ( '&amp;' , '&' ) . replace ( '&#039;' , '\'' )
  iiiiiIIii ( '[COLORgreen]' + OoOOOo0 + '[/COLOR]' , 'http://www.watchseries.li' + url , 10045 , oOOoO0 + 'WATCHSERIES.png' , '' , '' )
 for url in OOo0 :
  iiiiiIIii ( '[COLORgreen]' + 'NEXT' + '[/COLOR]' , 'http://www.watchseries.li' + url , 10046 , '' , '' , '' )
  if 42 - 42: o0oO0 - OOOo0 + ii11ii1ii % o00O0oo
def IiIi1III ( url ) :
 OOoOO0oo0ooO = O0o0O00Oo0o0 ( url )
 O00O0oOO00O00 = re . compile ( '<div class="mask">.+?<a href="(.+?)" title="(.+?)">.+?<img src="(.+?)"' , re . DOTALL ) . findall ( OOoOO0oo0ooO )
 OOo0 = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="(.+?)">Next</a></li></ul>' , re . DOTALL ) . findall ( OOoOO0oo0ooO )
 for url , iiI111I1iIiI , i1i in O00O0oOO00O00 :
  iiiiiIIii ( '[COLORgreen]' + ( iiI111I1iIiI ) . replace ( '&nbsp;' , ' ' ) . replace ( '&amp;' , '&' ) . replace ( '&#039;' , '\'' ) + '[/COLOR]' , 'http://www.watchseries.li' + url , 10044 , i1i , '' , '' )
 for url in OOo0 :
  iiiiiIIii ( '[COLORgreen]' + 'NEXT' + '[/COLOR]' , 'http://www.watchseries.li' + url , 10041 , '' , '' , '' )
  if 47 - 47: OoooooooOO % O0 * oO0o0ooO0 . o00O0oo
def ii111Iiii ( url ) :
 OOoOO0oo0ooO = O0o0O00Oo0o0 ( url )
 III1iII1I1ii = re . compile ( '<div class="col-md-6 col-xs-12".+?<a href=".+?" itemprop="url"><span itemprop="name">(.+?)</span>(.+?)</ul>' , re . DOTALL ) . findall ( OOoOO0oo0ooO )
 for IiI1ii1Ii , o0oO0O00oOo in III1iII1I1ii :
  O00O0oOO00O00 = re . compile ( '<li itemprop="episode".+?<meta itemprop="url" content="(.+?)">.+?<span class="" itemprop="name">\n(.+?)\n' , re . DOTALL ) . findall ( str ( o0oO0O00oOo ) )
  for url , iiI111I1iIiI in O00O0oOO00O00 :
   OoOOOo0 = ( IiI1ii1Ii ) . replace ( '  ' , '' ) + ' ' + ( iiI111I1iIiI ) . replace ( '&nbsp;' , ' ' ) . replace ( '&#039;' , '\'' ) . replace ( '  ' , '' )
   iiiiiIIii ( '[COLORgreen]' + OoOOOo0 + '[/COLOR]' , 'http://www.watchseries.li' + url , 10045 , oOOoO0 + 'WATCHSERIES.png' , '' , '' )
 OOo0 = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="(.+?)">Next</a></li></ul>' , re . DOTALL ) . findall ( OOoOO0oo0ooO )
 for url in OOo0 :
  iiiiiIIii ( '[COLORgreen]' + 'NEXT' + '[/COLOR]' , 'http://www.watchseries.li' + url , 10044 , '' , '' , '' )
  if 54 - 54: OoooooooOO - OOOo0 % ii11ii1ii
  if 92 - 92: Ooo00oOo00o * o0oO0
class i1iIIi1o0o0OoOOOOOo ( ) :
 if 39 - 39: OoooooooOO * OoOO0ooOOoo0O * O0 . o0000oOoOoO0o . Ooo00oOo00o + o0oO0
 List = [ ]
 source_list = [ ]
 def __init__ ( self , name ) :
  if 9 - 9: I1IiI + OoOO % OoooooooOO + OOooOOo
  OoOOOo0 = name
  self . Get_Sources ( i1Oo00 , OoOOOo0 )
  if 56 - 56: OoooooooOO + ii11ii1ii - oO0o0ooO0
  if 24 - 24: OOooOOo + o0oO0 + o0000oOoOoO0o - iIii1I11I1II1
 def Get_Sources ( self , URL , season_name ) :
  i1111 = xbmcgui . DialogProgress ( )
  OOoOO0oo0ooO = O0o0O00Oo0o0 ( URL )
  O00O0oOO00O00 = re . compile ( '<td>.+?<a href="/link/(.+?)".+?height="16px">(.+?)\n' , re . DOTALL ) . findall ( OOoOO0oo0ooO )
  for i1Oo00 , iiI111I1iIiI in O00O0oOO00O00 :
   URL = 'http://www.watchseries.li/link/' + i1Oo00
   self . Get_site_link ( URL , season_name )
   if 49 - 49: o0000oOoOoO0o . o0oO0 * I1IiI % IIII . O0
 def Get_site_link ( self , url , season_name ) :
  OOoOO0oo0ooO = O0o0O00Oo0o0 ( url )
  O00O0oOO00O00 = re . compile ( '<iframe style=.+?" src="(.+?)"' ) . findall ( OOoOO0oo0ooO )
  OOo0 = re . compile ( '<IFRAME SRC="(.+?)"' ) . findall ( OOoOO0oo0ooO )
  ooOooo000OO00 = re . compile ( '<IFRAME style=".+?" SRC="(.+?)"' ) . findall ( OOoOO0oo0ooO )
  for url in O00O0oOO00O00 :
   self . main ( url , season_name )
  for url in OOo0 :
   self . main ( url , season_name )
  for url in ooOooo000OO00 :
   self . main ( url , season_name )
   if 48 - 48: O0 * o00O0oo - O0 / o00O0oo + I1IiI
 def main ( self , url , season_name ) :
  i1111 . create ( "[COLORwhite]Origin[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
  if 'daclips.in' in url :
   oO00oo000O = 'DACLIPS'
   if oO00oo000O in i1iIIi1o0o0OoOOOOOo . source_list :
    pass
   else :
    self . daclips ( url , season_name , oO00oo000O )
    i1111 . update ( 0 , "" , "Getting Daclips Links" )
  else :
   if 'filehoot.com' in url :
    oO00oo000O = 'FILEHOOT'
    if oO00oo000O in i1iIIi1o0o0OoOOOOOo . source_list :
     pass
    else :
     i1111 . update ( 0 , "" , "Getting Filehoot Links" )
     self . filehoot ( url , season_name , oO00oo000O )
   else :
    if 'thevideo.me' in url :
     oO00oo000O = 'THEVIDEO'
     if oO00oo000O in i1iIIi1o0o0OoOOOOOo . source_list :
      pass
     else :
      self . thevideo ( url , season_name , oO00oo000O )
      i1111 . update ( 0 , "" , "Getting Thevideo Links" )
    else :
     if 'allmyvideos.net' in url :
      oO00oo000O = 'ALLMYVIDEOS'
      if oO00oo000O in i1iIIi1o0o0OoOOOOOo . source_list :
       pass
      else :
       self . allmyvid ( url , season_name , oO00oo000O )
       i1111 . update ( 0 , "" , "Getting Allmyvideo Links" )
     else :
      if 'vidspot.net' in url :
       oO00oo000O = 'VIDSPOT'
       if oO00oo000O in i1iIIi1o0o0OoOOOOOo . source_list :
        pass
       else :
        self . vidspot ( url , season_name , oO00oo000O )
        i1111 . update ( 0 , "" , "Getting Vidspot Links" )
      else :
       if 'vodlocker' in url :
        oO00oo000O = 'VODLOCKER'
        if oO00oo000O in i1iIIi1o0o0OoOOOOOo . source_list :
         pass
        else :
         self . vodlocker ( url , season_name , oO00oo000O )
         i1111 . update ( 0 , "" , "Getting Vodlocker Links" )
         if 7 - 7: O0 / oO0o0ooO0 * OoOO
         if 29 - 29: OOooOOo
 def allmyvid ( self , url , season_name , source_name ) :
  OOoOO0oo0ooO = O0o0O00Oo0o0 ( url )
  O00O0oOO00O00 = re . compile ( '"file" : "(.+?)",\n.+?"default" : .+?,\n.+?"label" : "(.+?)"' , re . DOTALL ) . findall ( OOoOO0oo0ooO )
  for oo0 , iiI111I1iIiI in O00O0oOO00O00 :
   self . Printer ( oo0 , season_name , source_name )
   if 2 - 2: OoooooooOO
 def vidspot ( self , url , season_name , source_name ) :
  OOoOO0oo0ooO = O0o0O00Oo0o0 ( url )
  O00O0oOO00O00 = re . compile ( '"file" : "(.+?)",\n.+?"default" : .+?,\n.+?"label" : "(.+?)"' ) . findall ( OOoOO0oo0ooO )
  for oo0 , iiI111I1iIiI in O00O0oOO00O00 :
   self . Printer ( oo0 , season_name , source_name )
   if 60 - 60: Ooo00oOo00o
 def thevideo ( self , url , season_name , source_name ) :
  OOoOO0oo0ooO = O0o0O00Oo0o0 ( url )
  O00O0oOO00O00 = re . compile ( "{ label: '.+?', file: '(.+?)' }" ) . findall ( OOoOO0oo0ooO )
  for oo0 in O00O0oOO00O00 :
   self . Printer ( oo0 , season_name , source_name )
   if 81 - 81: I1IiI % o00O0oo
 def vodlocker ( self , url , season_name , source_name ) :
  OOoOO0oo0ooO = O0o0O00Oo0o0 ( url )
  O00O0oOO00O00 = re . compile ( 'file: "(.+?)",.+?skin' , re . DOTALL ) . findall ( OOoOO0oo0ooO )
  for oo0 in O00O0oOO00O00 :
   self . Printer ( oo0 , season_name , source_name )
   if 87 - 87: iIii1I11I1II1 . OoooooooOO * I1IiI
 def daclips ( self , url , season_name , source_name ) :
  OOoOO0oo0ooO = O0o0O00Oo0o0 ( url )
  O00O0oOO00O00 = re . compile ( '{ file: "(.+?)", type:"video" }' ) . findall ( OOoOO0oo0ooO )
  for oo0 in O00O0oOO00O00 :
   self . Printer ( oo0 , season_name , source_name )
   if 100 - 100: Ooo00oOo00o / i1IIi - OOOo0 % o00O0oo - iIii1I11I1II1
 def filehoot ( self , url , season_name , source_name ) :
  OOoOO0oo0ooO = O0o0O00Oo0o0 ( url )
  O00O0oOO00O00 = re . compile ( 'file: "(.+?)",.+?skin' , re . DOTALL ) . findall ( OOoOO0oo0ooO )
  for oo0 in O00O0oOO00O00 :
   self . Printer ( oo0 , season_name , source_name )
   if 17 - 17: o0000oOoOoO0o / OOooOOo % Oo
 def Printer ( self , Link , season_name , source_name ) :
  if 71 - 71: IIII . O0oO . Ooo00oOo00o
  if Link in i1iIIi1o0o0OoOOOOOo . List :
   pass
  elif source_name in i1iIIi1o0o0OoOOOOOo . source_list :
   pass
  else :
   oOOO00o000o ( '[COLORgreen]' + source_name + '[/COLOR]' , Link , 10012 , oOOoO0 + 'WATCHSERIES.png' )
   i1111 . update ( 100 , "" , "Got Source" )
   i1iIIi1o0o0OoOOOOOo . List . append ( Link )
   i1iIIi1o0o0OoOOOOOo . source_list . append ( source_name )
   if 68 - 68: i11iIiiIii % OoOO * Ooo00oOo00o * IIII * OoOoOO00 + O0
   xbmcplugin . addSortMethod ( o0 , xbmcplugin . SORT_METHOD_TITLE ) ;
   if 66 - 66: o0000oOoOoO0o % ii11ii1ii % OoooooooOO
   if 34 - 34: OOooOOo / oO0o0ooO0 % O0 . Ooo00oOo00o . i1IIi
   if 29 - 29: O0 . O0oO
   if 66 - 66: OoOO * iIii1I11I1II1 % iIii1I11I1II1 * IIII - o0oO0 - IIII
   if 70 - 70: O0oO + OoOO
def o00ooo0 ( ) :
 iiiiiIIii ( '[COLORgreen]Highlights[/COLOR]' , '' , 10008 , oOOoO0 + 'ORIGINFOOTBALL.png' , OOooO0OOoo , '' )
 iiiiiIIii ( '[COLORgreen]Fixtures[/COLOR]' , '' , 10009 , oOOoO0 + 'ORIGINFOOTBALL.png' , OOooO0OOoo , '' )
 if 39 - 39: o0oO0 . OoOoOO00
def iIiIi1iI11iiI ( ) :
 Ooo0O0oooo = O0o0O00Oo0o0 ( oOo0oooo00o ( 'aHR0cDovL2xpdmVvbnNhdC5jb20vcXVpY2tpbmRleC5odG1s' ) )
 O00O0oOO00O00 = re . compile ( '<a target="_self" href="(.+?)".+?src="(.+?)" alt="(.+?)"' , re . DOTALL ) . findall ( Ooo0O0oooo )
 for i1Oo00 , i1i , iiI111I1iIiI in O00O0oOO00O00 :
  iiiiiIIii ( '[COLORgreen]' + ( iiI111I1iIiI ) . replace ( 'amp;' , '' ) + '[/COLOR]' , oOo0oooo00o ( 'aHR0cDovL2xpdmVvbnNhdC5jb20v' ) + i1Oo00 , 10010 , oOo0oooo00o ( 'aHR0cDovL2xpdmVvbnNhdC5jb20v' ) + i1i , OOooO0OOoo , '' )
  if 26 - 26: iIii1I11I1II1 * O0oO - OoOO0ooOOoo0O
def III1II111Ii1 ( url ) :
 OOoOO0oo0ooO = O0o0O00Oo0o0 ( url )
 III1iII1I1ii = re . compile ( 'AndClearL.+?><h2.+?head>(.*?)float' , re . DOTALL ) . findall ( OOoOO0oo0ooO )
 for III1iII1I1ii in III1iII1I1ii :
  o0O0OO0o = re . compile ( '(.*?)</h2>' ) . findall ( str ( III1iII1I1ii ) )
  for OOOoOo in o0O0OO0o :
   OOOoOo = OOOoOo
  OOoO0oo0O = re . compile ( 'comp_head>(.*?)</span>.*?<div class = fLeft width = ".*?"><img src="(.*?)">.*?</div>.*?ST:(.*?)</div>(.+?)<!-- around all of channel types ENDS 2-->' , re . DOTALL ) . findall ( str ( III1iII1I1ii ) )
  for iiI1I1iio00 , i1i , time , IiI1iiII1i1i in OOoO0oo0O :
   I1I1IiI1 = re . compile ( ",CAPTION, '(.+?)&nbsp" ) . findall ( IiI1iiII1i1i )
   iiiiiIIii ( '[COLORgreen]' + OOOoOo + ' - ' + iiI1I1iio00 + ' - ' + time + '[/COLOR]' , '' , 10010 , oOo0oooo00o ( 'aHR0cDovL2xpdmVvbnNhdC5jb20=' ) + i1i , OOooO0OOoo , ( str ( I1I1IiI1 ) ) )
   if 18 - 18: OOOo0
 Oooo0Ooo000 ( 'tvshows' , 'Media Info 3' )
 if 80 - 80: ii11ii1ii / iIii1I11I1II1 % I1IiI
def oO000o0Oo00 ( ) :
 if 77 - 77: iIii1I11I1II1 + Ooo00oOo00o . ii11ii1ii % Ooo00oOo00o
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
 if 93 - 93: O0
def OoOoooO0O00 ( url ) :
 OOoOO0oo0ooO = O0o0O00Oo0o0 ( url )
 O00O0oOO00O00 = re . compile ( 'itemprop="image" class="entry-thumb" src="(.+?)".+?<h3 itemprop="name" class="entry-title td-module-title"><a itemprop="url" href="(.+?)" rel="bookmark" title=".+?">(.+?)</a></h3>' , re . DOTALL ) . findall ( OOoOO0oo0ooO )
 for i1i , url , iiI111I1iIiI in O00O0oOO00O00 :
  oOO0OooO0 = iiI111I1iIiI . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' )
  oOOO00o000o ( '[COLORgreen]' + oOO0OooO0 + '[/COLOR]' , url , 10013 , i1i )
  if 63 - 63: i11iIiiIii + iIii1I11I1II1 / O0 - o00O0oo + OOooOOo
def Iii111Ii1 ( url ) :
 OOoOO0oo0ooO = O0o0O00Oo0o0 ( url )
 O00O0oOO00O00 = re . compile ( '<script data-config="(.+?)" data-height' ) . findall ( OOoOO0oo0ooO )
 for I1IiI111I11 in O00O0oOO00O00 :
  III11 = ( I1IiI111I11 ) . replace ( '/v2' , '' ) . replace ( 'zeus.json' , 'video-sd.mp4?hosting_id=21772' ) . replace ( 'config.playwire.com' , 'cdn.video.playwire.com' )
  o00oO00 ( 'http:' + III11 )
  if 5 - 5: OoooooooOO * I1IiI % IIII . ii11ii1ii % OOOo0
  if 20 - 20: o00O0oo / O0 / IIII % i1IIi + I1IiI
def I1IiI1ii1ii1I ( url ) :
 Ooo0O0oooo = iiI ( url )
 O00O0oOO00O00 = re . compile ( '<a href="([^"]*)" title="([^"]*)"><img itemprop="image" content="([^"]*)"' , re . DOTALL ) . findall ( Ooo0O0oooo )
 OOo0 = re . compile ( "<a rel='next' href=([^=]*)=" , re . DOTALL ) . findall ( Ooo0O0oooo )
 for url , iiI111I1iIiI , i1i in O00O0oOO00O00 :
  oOOO00o000o ( iiI111I1iIiI , url , 8046 , i1i )
 for url in OOo0 :
  oOIIiIi ( 'NEXT PAGE' , ( url ) . replace ( ' class' , '' ) , 8045 , oOOoO0 + 'geniekitchen.png' )
def iI1IIi11i1I1 ( url ) :
 Ooo0O0oooo = iiI ( url )
 O00O0oOO00O00 = re . compile ( "__filename='([^']*)',.+?__fullimage='([^']*)',.+?__title='([^']*)'," , re . DOTALL ) . findall ( Ooo0O0oooo )
 for url , i1i , iiI111I1iIiI in O00O0oOO00O00 :
  o00oO00 ( 'http://bitcast-b.bitgravity.com/ndtvod/23372/ndtv/' + url )
  if 60 - 60: o0000oOoOoO0o / i1IIi % ii11ii1ii / ii11ii1ii * ii11ii1ii . i11iIiiIii
def o0oOO00 ( url ) :
 Ooo0O0oooo = iiI ( url )
 O00O0oOO00O00 = re . compile ( "src='http://www.youtube.com/embed/(.+?)?version=3&#038;rel=1&#038;fs=1&#038;autohide=2&#038;showsearch=0&#038;showinfo=1&#038;iv_load_policy=1&#038;wmode=transparent' frameborder='0' allowfullscreen='true'></iframe>" ) . findall ( Ooo0O0oooo )
 for url in O00O0oOO00O00 :
  yt . PlayVideo ( url )
  if 46 - 46: i11iIiiIii - o0000oOoOoO0o
def oOoOo ( ) :
 Ooo0O0oooo = iiI ( oOo0oooo00o ( 'aHR0cDovL3RvcGRvY3VtZW50YXJ5ZmlsbXMuY29tLw==' ) )
 O00O0oOO00O00 = re . compile ( '<a href="(.+?)" >(.+?)</a></li><li>' ) . findall ( Ooo0O0oooo )
 for i1Oo00 , iiI111I1iIiI in O00O0oOO00O00 :
  oOIIiIi ( iiI111I1iIiI , i1Oo00 , 8041 , oOOoO0 + 'documentary.png' )
def OoO00O0OOO ( url ) :
 Ooo0O0oooo = iiI ( url )
 O00O0oOO00O00 = re . compile ( '<h2><a href="(.+?)" title="(.+?)">.+?</a></h2>.+?src="(.+?)"' , re . DOTALL ) . findall ( Ooo0O0oooo )
 OOo0 = re . compile ( 'class="inactive">.+?</a><a href="(.+?)">Next</a></div>' , re . DOTALL ) . findall ( Ooo0O0oooo )
 for url , iiI111I1iIiI , i1i in O00O0oOO00O00 :
  oOIIiIi ( ( iiI111I1iIiI ) . replace ( '&#039;s' , '' ) , url , 8042 , i1i )
 for url in OOo0 :
  oOIIiIi ( 'NEXT PAGE' , url , 8041 , oOOoO0 + 'documentary.png' )
  if 87 - 87: IIII
  if 34 - 34: Ooo00oOo00o
def I11i11i1 ( url ) :
 Ooo0O0oooo = iiI ( url )
 O00O0oOO00O00 = re . compile ( '<meta itemprop="name" content="(.+?)".+?<meta itemprop="thumbnailUrl" content="(.+?)".+?<meta itemprop="embedUrl" content="(.+?)".+?<meta itemprop="description" content="(.+?)" />' , re . DOTALL ) . findall ( Ooo0O0oooo )
 OOo0 = re . compile ( '<div class="video new-video"><iframe width="766" height="431" src="(.+?)&amp;iv_load_policy=3&amp;showinfo=0&amp;autohide=1"' , re . DOTALL ) . findall ( Ooo0O0oooo )
 for iiI111I1iIiI , i1i , url , IIi11IIiIii1 in O00O0oOO00O00 :
  oOOO00o000o ( ( iiI111I1iIiI ) . replace ( '&#039;s' , '' ) , url . replace ( 'https://www.youtube.com/embed/' , '' ) , 8043 , i1i )
 for url in OOo0 :
  OOOii1i1iiI ( ( url ) . replace ( '//' , 'http://' ) )
  if 94 - 94: i1IIi * i1IIi % OoOoOO00 + OoOO0ooOOoo0O
def OOOii1i1iiI ( url ) :
 Ooo0O0oooo = iiI ( url )
 O00O0oOO00O00 = re . compile ( '<link rel="canonical" href="(.+?)">  <link rel="stylesheet"' ) . findall ( Ooo0O0oooo )
 for url in O00O0oOO00O00 :
  oOOO00o000o ( 'PLAY' , ( url ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , oOOoO0 + 'documentary.png' )
  if 28 - 28: OOOo0
def I11o0000o0Oo ( ) :
 OOoOO0oo0ooO = iiI ( 'http://www.stream2watch.co/live-tv' )
 O00O0oOO00O00 = re . compile ( '<a href="(.+?)">.+?<img src="(.+?)" alt=".+?"/>.+?<span class="country_name">(.+?)<br />(.+?)</span>' , re . DOTALL ) . findall ( OOoOO0oo0ooO )
 for i1Oo00 , i1i , iiI111I1iIiI , ooo0O0OOo0OoO in O00O0oOO00O00 :
  oOIIiIi ( ( iiI111I1iIiI + '[COLORgreen]' + ooo0O0OOo0OoO + '[/COLOR]' ) , i1Oo00 , 8086 , i1i )
  if 45 - 45: O0 / i1IIi * OoOO * Ooo00oOo00o
def II11I ( url ) :
 OOoOO0oo0ooO = iiI ( url )
 O00O0oOO00O00 = re . compile ( '<a class="front_channel_href" href="(.+?)" title=".+?">.+?<img class="front_channel_thumb" src="(.+?)" alt=".+?"/>.+?<span class="front_channel_name">(.+?)</span>' , re . DOTALL ) . findall ( OOoOO0oo0ooO )
 for url , i1i , iiI111I1iIiI in O00O0oOO00O00 :
  oOIIiIi ( '[COLORgreen]' + iiI111I1iIiI + '[/COLOR]' , url , 8087 , i1i )
  if 31 - 31: o00O0oo
def i11iIIi ( url ) :
 OOoOO0oo0ooO = O0o0O00Oo0o0 ( url )
 O00O0oOO00O00 = re . compile ( 'a id="code_.+?data-f-href="(.+?)" data-code-embed="">(.+?)</a>' , re . DOTALL ) . findall ( OOoOO0oo0ooO )
 for url , iiI111I1iIiI in O00O0oOO00O00 :
  O000O ( url , iiI111I1iIiI )
  if 16 - 16: OOOo0 . iIii1I11I1II1
def O000O ( url , name ) :
 OOoOO0oo0ooO = O0o0O00Oo0o0 ( url )
 O00O0oOO00O00 = re . compile ( "playStream\('.+?', '(.+?)'\);" , re . DOTALL ) . findall ( OOoOO0oo0ooO )
 for url in O00O0oOO00O00 :
  print url
  oOOO00o000o ( '[COLORgreen]' + name + '[/COLOR]' , url , 222 , '' )
  if 27 - 27: i11iIiiIii - OOOo0
def iii1IIiI ( ) :
 Ooo0O0oooo = iiI ( oOo0oooo00o ( 'aHR0cDovL3d3dy5zb2xpZS5vcmcvYWxpYnJhcnkvaW5kZXguaHRtbA==' ) )
 O00O0oOO00O00 = re . compile ( '<td align="center" valign="top">.+?<a href="(.+?)">.+?<img src="(.+?)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( Ooo0O0oooo )
 for i1Oo00 , i1i , iiI111I1iIiI in O00O0oOO00O00 :
  oOIIiIi ( ( '[COLORgreen]' + iiI111I1iIiI + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + i1Oo00 , 3002 , 'http://www.solie.org/alibrary/' + i1i )
def i1i1Ii11Ii ( url ) :
 Ooo0O0oooo = iiI ( url )
 O00O0oOO00O00 = re . compile ( '<td align="center" valign="top">.+?<a href="(.+?)">.+?<img src="(.+?)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( Ooo0O0oooo )
 for url , i1i , iiI111I1iIiI in O00O0oOO00O00 :
  oOIIiIi ( ( '[COLORgreen]' + iiI111I1iIiI + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3003 , 'http://www.solie.org/alibrary/' + i1i )
def O000oOo ( url ) :
 Ooo0O0oooo = iiI ( url )
 O00O0oOO00O00 = re . compile ( '<br><a href="([^"]*)">(.+?)</a>' ) . findall ( Ooo0O0oooo )
 IiiIIi1 = re . compile ( 'href="([^"]*)">Season(.+?)</a>' ) . findall ( Ooo0O0oooo )
 next = re . compile ( '<a href="([^"]*)">Episodes</a>' ) . findall ( Ooo0O0oooo )
 OOo0 = re . compile ( '<td align="center" valign="top">.+?<a href="(.+?)">.+?<img src="(.+?)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( Ooo0O0oooo )
 for url , iiI111I1iIiI in O00O0oOO00O00 :
  oOOO00o000o ( ( '[COLORgreen]' + iiI111I1iIiI + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3004 , oOOoO0 + 'classicmovies.png' )
 for url , iiI111I1iIiI in IiiIIi1 :
  oOIIiIi ( '[COLORgreen]Season- ' + iiI111I1iIiI + '[/COLOR]' , 'http://www.solie.org/alibrary/' + url , 3003 , oOOoO0 + 'classicmovies.png' )
 for url in next :
  oOIIiIi ( '[COLORgreen]NEXT[/COLOR]' , 'http://www.solie.org/alibrary/' + url , 3003 , oOOoO0 + 'classicmovies.png' )
 for url , i1i , iiI111I1iIiI in OOo0 :
  oOIIiIi ( ( '[COLORgreen]' + iiI111I1iIiI + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3003 , 'http://www.solie.org/alibrary/' + i1i )
def iI1iIiiI ( url ) :
 Ooo0O0oooo = iiI ( url )
 O00O0oOO00O00 = re . compile ( '<iframe.+?src="([^"]*)"' ) . findall ( Ooo0O0oooo )
 for url in O00O0oOO00O00 :
  Oo0OOo ( url )
def Oo0OOo ( url ) :
 Ooo0O0oooo = iiI ( url )
 O00O0oOO00O00 = re . compile ( '<meta property="og:video" content="([^"]*)"/>' ) . findall ( Ooo0O0oooo )
 for url in O00O0oOO00O00 :
  o00oO00 ( url )
  if 36 - 36: O0 * Ooo00oOo00o % oO0o0ooO0 * oO0o0ooO0 / Ooo00oOo00o * IIII
def IiI ( ) :
 Ooo0O0oooo = iiI ( oOo0oooo00o ( 'aHR0cDovL3JldHJvdmlzaW9uLnR2L2FsbC8=' ) )
 O00O0oOO00O00 = re . compile ( '<a href="([^"]*)"><h2><font color=".+?"><h2>(.+?)</font></h2></a>' ) . findall ( Ooo0O0oooo )
 for i1Oo00 , iiI111I1iIiI in O00O0oOO00O00 :
  oOOO00o000o ( ( '[COLORgreen]' + iiI111I1iIiI + '[/COLOR]' ) . replace ( '&#8211;' , ':' ) , i1Oo00 , 8061 , oOOoO0 + 'classicmovies.png' )
def O0o0OO00 ( url ) :
 Ooo0O0oooo = iiI ( url )
 O00O0oOO00O00 = re . compile ( "v.src = '([^']*)';" ) . findall ( Ooo0O0oooo )
 for url in O00O0oOO00O00 :
  o00oO00 ( url )
  if 14 - 14: ii11ii1ii + i11iIiiIii
def OOOoo ( ) :
 Ooo0O0oooo = iiI ( oOo0oooo00o ( 'aHR0cDovL3JldHJvdmlzaW9uLnR2L2NsYXNzaWMtdHYv' ) )
 O00O0oOO00O00 = re . compile ( '<a href="([^"]*)"><h2><font color=".+?"><h2>(.+?)</font></h2></a>' ) . findall ( Ooo0O0oooo )
 for i1Oo00 , iiI111I1iIiI in O00O0oOO00O00 :
  oOOO00o000o ( ( '[COLORgreen]' + iiI111I1iIiI + '[/COLOR]' ) . replace ( '&#8211;' , ':' ) , i1Oo00 , 8061 , oOOoO0 + 'classictv.png' )
def III1II1iii1i ( url ) :
 Ooo0O0oooo = iiI ( url )
 O00O0oOO00O00 = re . compile ( "v.src = '([^']*)';" ) . findall ( Ooo0O0oooo )
 for url in O00O0oOO00O00 :
  o00oO00 ( url )
  if 75 - 75: IIII - I1IiI - iIii1I11I1II1 % OOooOOo
def OooooO ( ) :
 OOoOO0oo0ooO = O0o0O00Oo0o0 ( oOo0oooo00o ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vbTN1c3RyZWFtcw==' ) )
 O00O0oOO00O00 = re . compile ( '<li><a href="(.+?)"> (.+?).m3u</a></li>' ) . findall ( OOoOO0oo0ooO )
 for i1Oo00 , iiI111I1iIiI in O00O0oOO00O00 :
  oOIIiIi ( ( '[COLORgreen]' + iiI111I1iIiI + '[/COLOR]' ) . replace ( '-' , ' ' ) . replace ( '_' , ' ' ) , ( oOo0oooo00o ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vbTN1c3RyZWFtcy8=' ) ) + i1Oo00 , 8071 , oOOoO0 + 'streams.png' )
def oO0O0 ( url ) :
 OOoOO0oo0ooO = iiI ( url )
 O00O0oOO00O00 = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( OOoOO0oo0ooO )
 for iiI111I1iIiI , url in O00O0oOO00O00 :
  oOOO00o000o ( ( '[COLORgreen]' + iiI111I1iIiI + '[/COLOR]' ) . replace ( '_' , ' ' ) , ( url ) . strip ( ) , 404 , oOOoO0 + 'streams.png' )
def iI111i11iI1 ( url ) :
 OOoOO0oo0ooO = iiI ( url )
 O00O0oOO00O00 = re . compile ( 'EXTINF:(.+?),(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( OOoOO0oo0ooO )
 for i1i , iiI111I1iIiI , url in O00O0oOO00O00 :
  url = ( ( oOo0oooo00o ( 'aHR0cDovL2dlbmlldHYuaXB0di5yZTo4MDAwL2xpdmUv' ) ) + oooOOOOO + '/' + i1iiIII111ii + url ) . strip ( )
  oOOO00o000o ( ( '[COLORgreen]' + iiI111I1iIiI + '[/COLOR]' ) . replace ( '_' , ' ' ) , url , 222 , i1i )
  if 2 - 2: I1IiI + O0oO + OoooooooOO . i1IIi
def I1III1iIi ( ) :
 III1i11 ( 'Best Videos' , 'http://www.xvideos.com/best' , 10105 , oOOoO0 + 'JIZBOX.png' , '' , '' )
 III1i11 ( 'Genres' , 'http://www.xvideos.com' , 10106 , oOOoO0 + 'JIZBOX.png' , '' , '' )
 III1i11 ( 'Recently Uploaded' , 'http://xvideos.com' , 10105 , oOOoO0 + 'JIZBOX.png' , '' , '' )
 III1i11 ( 'Tags' , 'http://www.xvideos.com/tags' , 10103 , oOOoO0 + 'JIZBOX.png' , '' , '' )
 III1i11 ( 'Search' , '' , 10107 , oOOoO0 + 'JIZBOX.png' , '' , '' , )
 if 82 - 82: OOOo0 + oO0o0ooO0 + ii11ii1ii * OOOo0 % i11iIiiIii % oO0o0ooO0
def Iiii1i11ii1Ii ( url ) :
 OOoOO0oo0ooO = O0o0O00Oo0o0 ( url )
 i1Oo0oOo000OoO0 = re . compile ( '<li><a class=".+?".+?href="(.+?)">Next</a></li>' ) . findall ( OOoOO0oo0ooO )
 for url in i1Oo0oOo000OoO0 :
  III1i11 ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10103 , oOOoO0 + 'JIZBOX.png' , '' , '' )
 O00O0oOO00O00 = re . compile ( '<li><a href="(.+?)"><b>(.+?)</b><span class="navbadge default"(.+?)</span>' ) . findall ( OOoOO0oo0ooO )
 for url , iiI111I1iIiI , IIii1I1i in O00O0oOO00O00 :
  III1i11 ( iiI111I1iIiI + ' - No of Videos : ' + ( IIii1I1i ) . replace ( '>' , '' ) , 'http://www.xvideos.com' + url , 10105 , oOOoO0 + 'JIZBOX.png' , '' , '' )
  if 22 - 22: Oo % Ooo00oOo00o - OoooooooOO * Oo
def ii1i ( url ) :
 OOoOO0oo0ooO = O0o0O00Oo0o0 ( url )
 i1Oo0oOo000OoO0 = re . compile ( 'href="([^"]*)">Next</a></li>' ) . findall ( OOoOO0oo0ooO )
 for url in i1Oo0oOo000OoO0 :
  III1i11 ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10104 , oOOoO0 + 'JIZBOX.png' , '' , '' )
 O00O0oOO00O00 = re . compile ( ':"([^"]*)".+?;</script></a></div></div><p class="profile-name"><a href="([^"]*)">(.+?)</a></p><p class="profile-counts">\n(.+?)\n' , re . DOTALL ) . findall ( OOoOO0oo0ooO )
 for i1i , url , iiI111I1iIiI , i1IiiiiIi1I in O00O0oOO00O00 :
  III1i11 ( iiI111I1iIiI + '--' + i1IiiiiIi1I , 'http://www.xvideos.com' + url + '#_tabVideos,videos-best' , 10105 , ( i1i ) . replace ( 'http:\/\/' , 'http://' ) , '' , '' )
  if 56 - 56: OoooooooOO * O0
  if 85 - 85: OoooooooOO % I1IiI * iIii1I11I1II1
def IiIo0o0OO0o00o0O ( url ) :
 OOoOO0oo0ooO = O0o0O00Oo0o0 ( url )
 O00O0oOO00O00 = re . compile ( '<div class="thumb-inside"><script>.+?<img src="(.+?)".+?<a href="(.+?)" title=".+?">(.+?)</a></p>.+?uration">(.+?)</span>.+?Porn quality:(.+?)</span>' , re . DOTALL ) . findall ( OOoOO0oo0ooO )
 for i1i , url , iiI111I1iIiI , IIIi1I1IIii1II , IIIIIIi1i in O00O0oOO00O00 :
  o0OOoo0OO0OOO ( iiI111I1iIiI + ' - Porn Quality : ' + IIIIIIi1i + ' - ' + IIIi1I1IIii1II , 'http://www.xvideos.com' + url , 10108 , i1i , i1i , IIIIIIi1i + ' - ' + IIIi1I1IIii1II )
 iiiii11I1 = re . compile ( '<li><a href="([^"]*)" class="no-page">Next</a></li></ul></div>' ) . findall ( OOoOO0oo0ooO )
 for url in iiiii11I1 :
  III1i11 ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10105 , oOOoO0 + 'JIZBOX.png' , '' , '' )
  if 16 - 16: O0 . o00O0oo % i1IIi % OoOO0ooOOoo0O
def i1I1iI ( url ) :
 OOoOO0oo0ooO = O0o0O00Oo0o0 ( url )
 III1iII1I1ii = re . compile ( '<div class="main-categories">(.+?)</div>' , re . DOTALL ) . findall ( OOoOO0oo0ooO )
 i1Oo0oOo000OoO0 = re . compile ( '<li><a class=".+?".+?href="(.+?)">Next</a></li>' ) . findall ( OOoOO0oo0ooO )
 for url in i1Oo0oOo000OoO0 :
  III1i11 ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10106 , oOOoO0 + 'JIZBOX.png' , '' , '' )
 O00O0oOO00O00 = re . compile ( '<li><a href="(.+?)" class="btn btn-default">(.+?)</a>' ) . findall ( str ( III1iII1I1ii ) )
 for url , iiI111I1iIiI in O00O0oOO00O00 :
  III1i11 ( iiI111I1iIiI , 'http://www.xvideos.com' + url , 10105 , oOOoO0 + 'JIZBOX.png' , '' , '' )
  if 92 - 92: Oo / i11iIiiIii + ii11ii1ii
  if 87 - 87: I1IiI % iIii1I11I1II1
def o0OO0OOO0O ( ) :
 Oo0oOOo = Oo0o0000o0o0 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 Iii1I = ( Oo0oOOo ) . replace ( ' ' , '+' ) . replace ( '&amp;' , '&' )
 OOO00O = Iii1I . lower ( )
 oOoOOOOoOO0o = 'http://www.xvideos.com/?k=' + OOO00O
 print oOoOOOOoOO0o + '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'
 OOoOO0oo0ooO = O0o0O00Oo0o0 ( oOoOOOOoOO0o )
 O00O0oOO00O00 = re . compile ( '<div class="thumb-inside"><script>.+?<img src="(.+?)".+?<a href="(.+?)" title=".+?">(.+?)</a></p>.+?uration">(.+?)</span>.+?Porn quality:(.+?)</span>' , re . DOTALL ) . findall ( OOoOO0oo0ooO )
 for i1i , i1Oo00 , iiI111I1iIiI , IIIi1I1IIii1II , IIIIIIi1i in O00O0oOO00O00 :
  o0OOoo0OO0OOO ( iiI111I1iIiI + ' - Porn Quality : ' + IIIIIIi1i + ' - ' + IIIi1I1IIii1II , 'http://www.xvideos.com' + i1Oo00 , 10108 , i1i , i1i , IIIIIIi1i + ' - ' + IIIi1I1IIii1II )
 iiiii11I1 = re . compile ( '<li><a href="([^"]*)" class="no-page">Next</a></li></ul></div>' ) . findall ( OOoOO0oo0ooO )
 for i1Oo00 in iiiii11I1 :
  III1i11 ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + i1Oo00 , 10105 , oOOoO0 + 'JIZBOX.png' , '' , '' )
  if 31 - 31: OOOo0 . IIII + ii11ii1ii
def oO0OOO0o0O ( url ) :
 OOoOO0oo0ooO = O0o0O00Oo0o0 ( url )
 O00O0oOO00O00 = re . compile ( 'flv_url=(.+?)\;' ) . findall ( OOoOO0oo0ooO )
 for url in O00O0oOO00O00 :
  OOOOO0 = ( url ) . replace ( '%3A' , ':' ) . replace ( '%2F' , '/' ) . replace ( '%3F' , '?' ) . replace ( '%3D' , '=' ) . replace ( '%26' , '&' ) . replace ( '&amp' , '' )
  Ooo0Oo0o ( OOOOO0 )
  if 85 - 85: OOOo0
def Ooo0Oo0o ( url ) :
 oOOo000oOoO0 = xbmc . Player ( Ii1Ii1I ( ) )
 import urlresolver
 try : oOOo000oOoO0 . play ( url )
 except : pass
 if 54 - 54: OoOO + I1IiI
 if 77 - 77: o0000oOoOoO0o . IIII
def o0O0OO0OOOOOo ( ) :
 OOoOO0oo0ooO = O0o0O00Oo0o0 ( oOo0oooo00o ( 'aHR0cDovL3d3dy5nb2Zpc2hpbmcuY28udWsvQW5nbGluZy1UaW1lcy9TZWN0aW9uL1ZpZGVvcy8=' ) )
 O00O0oOO00O00 = re . compile ( 'class="item.+?"><a href="(.+?)">(.+?)</a></li>' ) . findall ( OOoOO0oo0ooO )
 for i1Oo00 , iiI111I1iIiI in O00O0oOO00O00 :
  oOIIiIi ( '[COLORgreen]' + iiI111I1iIiI + '[/COLOR]' , ( 'http://www.gofishing.co.uk' + i1Oo00 ) . replace ( 'http://www.gofishing.co.ukhttp://www.gofishing.co.uk' , 'http://www.gofishing.co.uk' ) , 8091 , oOOoO0 + 'gofish.png' )
def IIi1i ( url ) :
 OOoOO0oo0ooO = iiI ( url )
 O00O0oOO00O00 = re . compile ( '<h2><a id=.+?href="([^"]*)">(.+?)</a></h2>' , re . DOTALL ) . findall ( OOoOO0oo0ooO )
 OOo0 = re . compile ( '<h3><a href="([^"]*)" id=.+?>(.+?)</a> </h3>.+?<img src="([^"]*)"' , re . DOTALL ) . findall ( OOoOO0oo0ooO )
 next = re . compile ( 'href="([^"]*)">next</a>&gt;</li>' , re . DOTALL ) . findall ( OOoOO0oo0ooO )
 for url , iiI111I1iIiI in O00O0oOO00O00 :
  oOOO00o000o ( '[COLORgreen]' + iiI111I1iIiI + '[/COLOR]' , 'http://www.gofishing.co.uk/' + url , 8092 , oOOoO0 + 'gofish.png' )
 for url , iiI111I1iIiI , i1i in OOo0 :
  oOOO00o000o ( '[COLORgreen]' + iiI111I1iIiI + '[/COLOR]' , 'http://www.gofishing.co.uk/' + url , 8092 , 'http://www.gofishing.co.uk/' + i1i )
 for url in next :
  oOIIiIi ( '[COLORgreen]NEXT[/COLOR]' , url . replace ( ' ' , '+' ) , 8091 , oOOoO0 + 'gofish.png' )
def iIiIIiii1II ( url ) :
 OOoOO0oo0ooO = iiI ( url )
 O00O0oOO00O00 = re . compile ( 'src="https://www.youtube.com/embed/(.+?)"' ) . findall ( OOoOO0oo0ooO )
 for url in O00O0oOO00O00 :
  yt . PlayVideo ( url )
  if 44 - 44: OoooooooOO . OoOoOO00 . OoOO0ooOOoo0O % OoooooooOO
def Oo0oO00 ( url ) :
 ii11ii11I = urllib2 . Request ( url )
 ii11ii11I . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
 Oo0oo0oOO0oOo = ''
 o0ooooO0o0O = ''
 try :
  Oo0oo0oOO0oOo = urllib2 . urlopen ( ii11ii11I )
  o0ooooO0o0O = Oo0oo0oOO0oOo . read ( )
  Oo0oo0oOO0oOo . close ( )
 except : pass
 if o0ooooO0o0O != '' :
  return o0ooooO0o0O
 else :
  o0ooooO0o0O = 'Failed'
  return o0ooooO0o0O
  if 18 - 18: OoOoOO00 + I1IiI - O0oO + Ooo00oOo00o / o0oO0 % IIII
def o0o0O0O000 ( ) :
 I1I1i = ( oOo0oooo00o ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 Oo0oOOo = Oo0o0000o0o0 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OOO00O = Oo0oOOo . lower ( )
 i1Oo00 = ( oOo0oooo00o ( 'aHR0cDovL2RsNC5tb3ZpZWZhcnNpLmNvbS9maWxtLzIwMTUtNy8=' ) )
 i1iIi = ( oOo0oooo00o ( 'aHR0cDovL2RsLmF2YWRsLmNvbS9OZXcvTW92aWUv' ) )
 O0O0oo = ( oOo0oooo00o ( 'aHR0cDovLzIxNy4yMTkuMTQzLjEwOC8xMzI3Lw==' ) )
 o00O = ( oOo0oooo00o ( 'aHR0cDovLzE3OC4xNjIuMjE0LjIzMi92b2QvbW92aWVzL2VuZ2xpc2gv' ) )
 Oo000O = ( oOo0oooo00o ( 'aHR0cDovL3Njb29ieXN0cmVhbS54MTBob3N0LmNvbS8vc2Nvb2J5L21vdi9hbGwucGhw' ) )
 I1111III11 = ( oOo0oooo00o ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 iI = ( oOo0oooo00o ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL3NlYXJjaC8/cT0=' ) ) + Oo0oOOo
 OOOiI1 = ( oOo0oooo00o ( 'aHR0cDovL2xldHdhdGNoLnVzLz9vcD1zZWFyY2gmaz0=' ) ) + ( Oo0oOOo ) . replace ( ' ' , '+' )
 if 84 - 84: OoOO0ooOOoo0O * OOOo0 % o0000oOoOoO0o + OoOO0ooOOoo0O / oO0o0ooO0
 OOoOO0oo0ooO = Oo0oO00 ( i1Oo00 )
 I1i111IiIiIi1 = Oo0oO00 ( i1iIi )
 oo000o = Oo0oO00 ( O0O0oo )
 OO00o0oOO = Oo0oO00 ( o00O )
 i1i1I1 = Oo0oO00 ( Oo000O )
 I1iOOo0O = Oo0oO00 ( iI )
 oOOoooO0O0 = O0o0O00Oo0o0 ( OOOiI1 )
 if 46 - 46: iIii1I11I1II1
 if OOoOO0oo0ooO != 'Failed' :
  O00O0oOO00O00 = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( OOoOO0oo0ooO )
  for I111iiiii1 , iiI111I1iIiI in O00O0oOO00O00 :
   if Oo0oOOo in iiI111I1iIiI . lower ( ) :
    oOOO00o000o ( ( '[COLORgreen]' + iiI111I1iIiI + '- source 1[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( i1Oo00 + I111iiiii1 ) , 222 , '' )
 if I1i111IiIiIi1 != 'Failed' :
  OOo0 = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( I1i111IiIiIi1 )
  for I111iiiii1 , iiI111I1iIiI in OOo0 :
   if Oo0oOOo in iiI111I1iIiI . lower ( ) :
    oOOO00o000o ( ( '[COLORgreen]' + iiI111I1iIiI + '- source 2[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( i1iIi + I111iiiii1 ) , 222 , '' )
 if oo000o != 'Failed' :
  ooOooo000OO00 = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( oo000o )
  for I111iiiii1 , iiI111I1iIiI in ooOooo000OO00 :
   if Oo0oOOo in iiI111I1iIiI . lower ( ) :
    oOOO00o000o ( ( '[COLORgreen]' + iiI111I1iIiI + '- source 3[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( O0O0oo + I111iiiii1 ) , 222 , '' )
 if OO00o0oOO != 'Failed' :
  OO0ooOoOO0OOo = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( OO00o0oOO )
  for I111iiiii1 , iiI111I1iIiI in OO0ooOoOO0OOo :
   if Oo0oOOo in iiI111I1iIiI . lower ( ) :
    oOOO00o000o ( ( '[COLORgreen]' + iiI111I1iIiI + '- source 4[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( o00O + I111iiiii1 ) , 222 , '' )
 if i1i1I1 != 'Failed' :
  OooOoooo0000 = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( i1i1I1 )
  for I111iiiii1 , i1i , iiI111I1iIiI in OooOoooo0000 :
   if Oo0oOOo in iiI111I1iIiI . lower ( ) :
    oOIIiIi ( ( '[COLORgreen]' + iiI111I1iIiI + '- source Scooby[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( 'Ganool' , '' ) . replace ( 'ShAaNiG' , '' ) . replace ( 'YIFY' , '' ) . replace ( '[[ Max-Movie.In ]]' , '' ) . replace ( '.mkv' , '' ) . replace ( '.mp4' , '' ) . replace ( '.' , ' ' ) , I111iiiii1 , 1006 , 'img' )
    if 29 - 29: o00O0oo - OOOo0 / OOOo0 * o00O0oo * IIII . OoOO0ooOOoo0O
    Oooo0Ooo000 ( 'tvshows' , 'Media Info 3' )
 if I1iOOo0O != 'Failed' :
  ooo = re . compile ( 'href="(.+?)".+?src="(.+?)" alt="Image of (.+?)"' , re . DOTALL ) . findall ( I1iOOo0O )
  for i1Oo00 , i1i , iiI111I1iIiI in ooo :
   if Oo0oOOo in iiI111I1iIiI . lower ( ) :
    oOIIiIi ( ( '[COLORgreen]' + iiI111I1iIiI + '- source Snag[/COLOR]' ) . replace ( '&#x27;' , '' ) , 'http://www.snagfilms.com' + i1Oo00 , 7067 , i1i )
    if 27 - 27: o0oO0 + i11iIiiIii * o0000oOoOoO0o + I1IiI + oO0o0ooO0
    Oooo0Ooo000 ( 'tvshows' , 'Media Info 3' )
 if oOOoooO0O0 != 'Failed' :
  o0oI1II1 = re . compile ( '<div class="video_block video_block_default ">.+?<a href="#">.+?<a href="(.*?)".+?<img src="(.+?)" height=".+?" alt="(.+?)"' , re . DOTALL ) . findall ( oOOoooO0O0 )
  for i1Oo00 , i1i , iiI111I1iIiI in o0oI1II1 :
   oOOO00o000o ( '[COLORgreen]' + iiI111I1iIiI + '- Source 7[/COLOR]' , i1Oo00 , 222 , i1i )
 Ii1I11I = [ '0-9/' , 'A/' , 'B/' , 'C/' , 'D/' , 'E/' , 'F/' , 'G/' , 'H/' , 'I/' , 'J/' , 'K/' , 'L/' , 'M/' , 'N/' , 'O/' , 'P/' , 'R/' , 'S/' , 'T/' , 'U/' , 'V/' , 'W/' , 'X/' , 'Y/' , 'Z/' ]
 if 53 - 53: O0 + OoOO0ooOOoo0O % i11iIiiIii * OoOO0ooOOoo0O
 if 69 - 69: o0oO0 - OoooooooOO * O0
 for iIIIi1i1I11i in Ii1I11I :
  oOO0OO0OO = I1I1i + iIIIi1i1I11i
  O0Oo0O0 = Oo0oO00 ( oOO0OO0OO )
  if i1i1I1 != 'Failed' :
   I1IiiIiii1 = re . compile ( '<li><a href="(.+?)"> (.+?)</a></li>' ) . findall ( O0Oo0O0 )
   for I111iiiii1 , iiI111I1iIiI in I1IiiIiii1 :
    if Oo0oOOo in iiI111I1iIiI . lower ( ) :
     oOOO00o000o ( ( '[COLORgreen]' + iiI111I1iIiI + 'source 5[/COLOR]' ) . replace ( 'Ganool' , '' ) . replace ( 'ShAaNiG' , '' ) . replace ( 'YIFY' , '' ) . replace ( '[[ Max-Movie.In ]]' , '' ) . replace ( '.mkv' , '' ) . replace ( '.mp4' , '' ) . replace ( '.' , ' ' ) , ( I1I1i + iIIIi1i1I11i + I111iiiii1 ) , 222 , '' )
     if 39 - 39: o0oO0 / O0 * IIII
     Oooo0Ooo000 ( 'tvshows' , 'Media Info 3' )
     if 17 - 17: o00O0oo / iIii1I11I1II1 - Ooo00oOo00o + OOOo0 % OoOO0ooOOoo0O
     if 14 - 14: OOooOOo % IIII + ii11ii1ii + Ooo00oOo00o
def OOOoOOo0o ( ) :
 if 50 - 50: OoOoOO00 - O0oO + iIii1I11I1II1 + iIii1I11I1II1
 Oo0oOOo = Oo0o0000o0o0 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OOO00O = Oo0oOOo . lower ( )
 OoooooOo = ( oOo0oooo00o ( 'aHR0cDovL2Nvb2x0dnNlcmllcy5jb20vc2VhcmNoLnBocD90YWc9' ) ) + ( Oo0oOOo ) . replace ( ' ' , '+' )
 i1Oo00 = ( oOo0oooo00o ( 'aHR0cDovL2RsLmZhcnNpbW92aWUubmV0L1NlcmlhbC8=' ) )
 i1iIi = ( oOo0oooo00o ( 'aHR0cDovL3N2Mi5kbC1wYXJzLmluLw==' ) )
 O0O0oo = ( oOo0oooo00o ( 'aHR0cDovL3R2LmRsLXBhcnMuaW4v' ) )
 o00O = ( oOo0oooo00o ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9BbWVyaWNhbiUyMFNlcmlhbC8=' ) )
 Oo000O = ( oOo0oooo00o ( 'aHR0cDovL2RpemlsYWIuY29tL2Fyc2l2P2xpbWl0PSZ0dXI9Jm9yZGVyYnk9JnVsa2U9Jm9yZGVyPSZ5aWw9JmRpemlfYWRpPQ==' ) ) + ( Oo0oOOo ) . replace ( ' ' , '+' )
 I1111III11 = ( oOo0oooo00o ( 'aHR0cDovL3Njb29ieXN0cmVhbS54MTBob3N0LmNvbS8vc2Nvb2J5L3Nob3dzL3R2YWxsLnBocA==' ) )
 OOOiI1 = ( oOo0oooo00o ( 'aHR0cDovL2xldHdhdGNoLnVzLz9vcD1zZWFyY2gmaz0=' ) ) + ( Oo0oOOo ) . replace ( ' ' , '+' )
 OooOo = ( oOo0oooo00o ( 'aHR0cDovL3d3dy53YXRjaHNlcmllcy5saS9zZWFyY2gv' ) ) + ( Oo0oOOo ) . replace ( ' ' , '%20' )
 if 67 - 67: Oo / O0
 oO0Oo00oo = Oo0oO00 ( OoooooOo )
 OOoOO0oo0ooO = Oo0oO00 ( i1Oo00 )
 I1i111IiIiIi1 = Oo0oO00 ( i1iIi )
 oo000o = Oo0oO00 ( O0O0oo )
 OO00o0oOO = Oo0oO00 ( o00O )
 i1i1I1 = cloudflare . source ( Oo000O )
 O0Oo0O0 = Oo0oO00 ( I1111III11 )
 oOOoooO0O0 = O0o0O00Oo0o0 ( OOOiI1 )
 OoOoooO000OO = O0o0O00Oo0o0 ( OooOo )
 if oO0Oo00oo != 'Failed' :
  O00Ooo = re . compile ( 'href="([^"]*)"><img src="([^"]*)" alt="([^"]*)"' ) . findall ( oO0Oo00oo )
  for i1Oo00 , i1i , iiI111I1iIiI in O00Ooo :
   if Oo0oOOo in iiI111I1iIiI . lower ( ) :
    oOIIiIi ( '[COLORgreen]' + iiI111I1iIiI + ' CoolSeries[/COLOR]' , i1Oo00 , 7052 , i1i )
    if 2 - 2: i11iIiiIii
    Oooo0Ooo000 ( 'tvshows' , 'Media Info 3' )
 if OOoOO0oo0ooO != 'Failed' :
  O00O0oOO00O00 = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( OOoOO0oo0ooO )
  for iiI111I1iIiI in O00O0oOO00O00 :
   if Oo0oOOo in iiI111I1iIiI . lower ( ) :
    oOIIiIi ( ( '[COLORgreen]' + iiI111I1iIiI + ' source 1[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( i1Oo00 + iiI111I1iIiI ) . replace ( ' ' , '%20' ) , 1006 , '' )
    if 98 - 98: OoOO / Ooo00oOo00o - o00O0oo - OOOo0 / I1IiI + i11iIiiIii
    Oooo0Ooo000 ( 'tvshows' , 'Media Info 3' )
 if I1i111IiIiIi1 != 'Failed' :
  OOo0 = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( I1i111IiIiIi1 )
  for iiI111I1iIiI in OOo0 :
   if Oo0oOOo in iiI111I1iIiI . lower ( ) :
    oOIIiIi ( ( iiI111I1iIiI + ' source 2' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( i1iIi + iiI111I1iIiI ) . replace ( ' ' , '%20' ) , 1006 , '' )
    if 17 - 17: o0000oOoOoO0o
    Oooo0Ooo000 ( 'tvshows' , 'Media Info 3' )
 if oo000o != 'Failed' :
  ooOooo000OO00 = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( oo000o )
  for iiI111I1iIiI in OOo0 :
   if Oo0oOOo in iiI111I1iIiI . lower ( ) :
    oOIIiIi ( ( iiI111I1iIiI + ' source 3' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( O0O0oo + iiI111I1iIiI ) . replace ( ' ' , '%20' ) , 1006 , '' )
    if 97 - 97: ii11ii1ii * ii11ii1ii / oO0o0ooO0
    Oooo0Ooo000 ( 'tvshows' , 'Media Info 3' )
 if OO00o0oOO != 'Failed' :
  OO0ooOoOO0OOo = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( OO00o0oOO )
  for iiI111I1iIiI in OOo0 :
   if Oo0oOOo in iiI111I1iIiI . lower ( ) :
    oOIIiIi ( ( iiI111I1iIiI + ' source 4' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( o00O + iiI111I1iIiI ) . replace ( ' ' , '%20' ) , 1006 , '' )
    if 6 - 6: OoOO
    Oooo0Ooo000 ( 'tvshows' , 'Media Info 3' )
 if i1i1I1 != 'Failed' :
  OooOoooo0000 = re . compile ( '<a href="(.+?)" class="film-image">\n<img src="(.+?)" alt=""/>\n</a>\n<div class="tss-detail">\n<a class="title" style="" href=".+?">\n<span class="position">.+?</span>\n(.+?)</a>' ) . findall ( i1i1I1 )
  for i1Oo00 , i1i , iiI111I1iIiI in OooOoooo0000 :
   if Oo0oOOo in iiI111I1iIiI . lower ( ) :
    oOIIiIi ( '[COLORgreen]' + iiI111I1iIiI + ' - Source - Dizi[/COLOR]' , i1Oo00 , 8062 , i1i )
    if 72 - 72: o0000oOoOoO0o * ii11ii1ii - I1IiI / ii11ii1ii + OoOO0ooOOoo0O - oO0o0ooO0
    Oooo0Ooo000 ( 'tvshows' , 'Media Info 3' )
 if O0Oo0O0 != 'Failed' :
  I1IiiIiii1 = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( O0Oo0O0 )
  for i1Oo00 , i1i , iiI111I1iIiI in I1IiiIiii1 :
   if Oo0oOOo in iiI111I1iIiI . lower ( ) :
    oOOO00o000o ( ( '[COLORgreen]' + iiI111I1iIiI + '- Source Scooby[/COLOR]' ) , i1Oo00 , 222 , 'img' )
    if 49 - 49: Ooo00oOo00o - O0 / Ooo00oOo00o * I1IiI + O0oO
    Oooo0Ooo000 ( 'tvshows' , 'Media Info 3' )
 if oOOoooO0O0 != 'Failed' :
  o0oI1II1 = re . compile ( '<div class="video_block video_block_default ">.+?<a href="#">.+?<a href="(.*?)".+?<img src="(.+?)" height=".+?" alt="(.+?)"' , re . DOTALL ) . findall ( oOOoooO0O0 )
  for i1Oo00 , i1i , iiI111I1iIiI in o0oI1II1 :
   oOOO00o000o ( '[COLORgreen]' + iiI111I1iIiI + ' - Source DiZzY[/COLOR]' , i1Oo00 , 222 , i1i )
 if OoOoooO000OO != 'Failed' :
  Iiii1I = re . compile ( '<img src="(.+?)".+?<a href="(.+?)" title=".+?"><b>(.+?)</b>' , re . DOTALL ) . findall ( OoOoooO000OO )
  for i1i , i1Oo00 , iiI111I1iIiI in Iiii1I :
   if 'watch online' in iiI111I1iIiI :
    pass
   else :
    iiiiiIIii ( '[COLORgreen]' + iiI111I1iIiI + '- Source WATCH SERIES[/COLOR]' , 'http://www.watchseries.li' + i1Oo00 , 10044 , i1i , '' , '' )
    if 61 - 61: iIii1I11I1II1 - o0000oOoOoO0o / oO0o0ooO0 * o0000oOoOoO0o % o00O0oo % oO0o0ooO0
    xbmcplugin . setContent ( o0 , 'movies' )
    if 63 - 63: OoOO0ooOOoo0O % iIii1I11I1II1
def II1ii ( ) :
 if 89 - 89: oO0o0ooO0 . i11iIiiIii * O0
 Oo0oOOo = Oo0o0000o0o0 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OOO00O = Oo0oOOo . lower ( )
 i1Oo00 = ( oOo0oooo00o ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz' ) )
 OOoOO0oo0ooO = O0o0O00Oo0o0 ( i1Oo00 )
 O00O0oOO00O00 = re . compile ( '"id":".+?","name":"(.+?)","img":"(.+?)","stream_url3":".+?","cat_id":"(.+?)","stream_url2":".+?","stream_url":".+?"}' , re . DOTALL ) . findall ( OOoOO0oo0ooO )
 for iiI111I1iIiI , i1i , Iiii1 in O00O0oOO00O00 :
  iI111II1ii = oOo0oooo00o ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv' ) + ( i1i ) . replace ( '\\' , '' )
  if Oo0oOOo in iiI111I1iIiI . lower ( ) :
   oOIIiIi ( iiI111I1iIiI , '' , 7022 , iI111II1ii )
   if 62 - 62: oO0o0ooO0 * iIii1I11I1II1 . IIII - OoooooooOO * OoOoOO00
 xbmcplugin . addSortMethod ( o0 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 45 - 45: O0 % OOOo0 - oO0o0ooO0 . Ooo00oOo00o
 if 42 - 42: oO0o0ooO0 / OOooOOo + Oo . Oo % OoOO0ooOOoo0O
def Ii1III1 ( url ) :
 ooIii1ii1II1iI1 = cloudflare . source ( url )
 O00O0oOO00O00 = re . compile ( '<a class="season" href="(.+?)">\n(.+?)\n</a>\n</span>\n<span>\n<a class="episode" href=".+?">\n(.+?)\n</a>\n</span>\n<span>\n<a class="episode-name" href=".+?">\n(.+?)</a>' ) . findall ( ooIii1ii1II1iI1 )
 for url , IiI1ii1Ii , oo0o0 , iiI111I1iIiI in O00O0oOO00O00 :
  oOIIiIi ( ( IiI1ii1Ii ) . replace ( 'Sezon' , ' Season ' ) + ( oo0o0 ) . replace ( 'Bölüm' , ' Episode ' ) + iiI111I1iIiI , url , 8063 , '' )
  if 67 - 67: Ooo00oOo00o / ii11ii1ii % o0000oOoOoO0o / O0oO
  if 1 - 1: O0oO - o0000oOoOoO0o
  if 45 - 45: o00O0oo - OoOO0ooOOoo0O
  if 70 - 70: Ooo00oOo00o % OOOo0 / OOOo0 . o0000oOoOoO0o % o0oO0 . OoOoOO00
def I1ii1Ii1 ( url ) :
 ooIii1ii1II1iI1 = cloudflare . source ( url )
 O00O0oOO00O00 = re . compile ( 'file: "(.+?)",.+?label: "(.+?)",' , re . DOTALL ) . findall ( ooIii1ii1II1iI1 )
 for url , iiI111I1iIiI in O00O0oOO00O00 :
  oOOO00o000o ( iiI111I1iIiI , url , 222 , '' )
  if 73 - 73: O0 . OoOO + i11iIiiIii + iIii1I11I1II1 - o0000oOoOoO0o / I1IiI
  if 99 - 99: ii11ii1ii * OoOO * ii11ii1ii - OoOoOO00 + o00O0oo
  if 72 - 72: OOooOOo % OOOo0 / oO0o0ooO0 - O0 + o0000oOoOoO0o
  if 83 - 83: O0
def oOOOOOo ( ) :
 if 50 - 50: O0oO + o0oO0 + oO0o0ooO0
 ooIii1ii1II1iI1 = cloudflare . source ( oOo0oooo00o ( 'aHR0cDovL2RpemlsYWIuY29t' ) )
 O00O0oOO00O00 = re . compile ( '<li id=".+?">.+?<a href="(.+?)">.+?<img width="40" height="40" src="(.+?)" alt=""/>.+?<span class="title">\n(.+?)</span>.+?<span class="alt-title">\n(.+?)</span>.+?</a>.+?</li>' , re . DOTALL ) . findall ( ooIii1ii1II1iI1 )
 for i1Oo00 , i1i , iiI111I1iIiI , oo0o0 in O00O0oOO00O00 :
  oOIIiIi ( iiI111I1iIiI + '  -  ' + ( oo0o0 ) . replace ( 'sezon' , 'Season' ) . replace ( 'bölüm' , 'Episode' ) , i1Oo00 , 8063 , i1i )
  if 15 - 15: o0000oOoOoO0o
def IiiI11I1IIiI ( ) :
 Ooo0O0oooo = iiI ( oOo0oooo00o ( 'aHR0cDovL3d3dy50dmd1aWRlLmNvLnVrLw==' ) )
 O00O0oOO00O00 = re . compile ( '<a href="(.+?)"  qt-title=".+?" qt-text=".+?<br> .+?" title="(.+?)".+?class=".+? src="(.+?)" alt=".+?" /></a>' , re . DOTALL ) . findall ( Ooo0O0oooo )
 for i1Oo00 , iiI111I1iIiI , i1i in O00O0oOO00O00 :
  oOOO00o000o ( '[COLORgreen]' + iiI111I1iIiI + '[/COLOR]' , i1Oo00 , 8002 , i1i )
def i1iI1i ( url ) :
 Ooo0O0oooo = iiI ( url )
 O00O0oOO00O00 = re . compile ( '<table border="0".+?url((.+?));background-repeat: no-repeat;">.+?<tr>.+?<span class="season">(.+?)</span><br>.+?<a href="(.+?)"+?>(.+?)</span><br>.+?<span class="programmetext">(.+?)</span></a><br>' , re . DOTALL ) . findall ( Ooo0O0oooo )
 for i1i , time , url , iiI111I1iIiI , IIi11IIiIii1 in O00O0oOO00O00 :
  iiiiiIIii ( '%s %s' % ( '[COLORgreen]' + iiI111I1iIiI + '[/COLOR]' , time ) , url , 1015 , i1i , IIi11IIiIii1 )
  if 59 - 59: IIII
def oOoO0OOO00O ( ) :
 if 73 - 73: OOooOOo % Ooo00oOo00o + IIII + OOOo0
 oOIIiIi ( 'Coronation Street' , '' , 8001 , '' )
 oOIIiIi ( 'Eastenders' , '' , 8002 , '' )
 oOIIiIi ( 'Emmerdale' , '' , 8003 , '' )
 oOIIiIi ( 'Hollyoaks' , '' , 8004 , '' )
 oOIIiIi ( 'Im a Celebrity' , '' , 8005 , '' )
 if 80 - 80: i1IIi + OOooOOo + IIII * o0000oOoOoO0o
 if 65 - 65: ii11ii1ii % o0000oOoOoO0o % iIii1I11I1II1 - OoooooooOO - ii11ii1ii - O0
 if 58 - 58: IIII + iIii1I11I1II1
 if 94 - 94: o00O0oo . i1IIi
def O0OOo0o ( ) :
 OOoOO0oo0ooO = O0o0O00Oo0o0 ( 'http://uksoapshare.blogspot.co.uk/' )
 O00O0oOO00O00 = re . compile ( '<a href="(.+?)".+?target=_blank>(.+?)</a>' ) . findall ( OOoOO0oo0ooO )
 for i1Oo00 , iiI111I1iIiI in O00O0oOO00O00 :
  if 'Holly' in iiI111I1iIiI :
   i1i = 'http://2.bp.blogspot.com/-9c7Sieh1RKs/UjD6TGAEEnI/AAAAAAAAAC8/84uwHfxcuYg/s1600/Hollyoaks.png'
   if 'huge' in i1Oo00 :
    oOOO00o000o ( ( iiI111I1iIiI ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , i1Oo00 . replace ( '\\/' , '/' ) , 8006 , i1i )
   else :
    pass
    if 44 - 44: OOOo0 * iIii1I11I1II1 / O0
 xbmcplugin . addSortMethod ( o0 , xbmcplugin . SORT_METHOD_TITLE_IGNORE_THE ) ;
 if 17 - 17: OoOoOO00
def iiIiii ( ) :
 OOoOO0oo0ooO = O0o0O00Oo0o0 ( 'http://uksoapshare.blogspot.co.uk/' )
 O00O0oOO00O00 = re . compile ( '<a href="(.+?)".+?target=_blank>(.+?)</a>' ) . findall ( OOoOO0oo0ooO )
 for i1Oo00 , iiI111I1iIiI in O00O0oOO00O00 :
  if 'East' in iiI111I1iIiI :
   i1i = 'http://3.bp.blogspot.com/-KWHcNbNJU8Y/Vi1ousRl7fI/AAAAAAAAAT8/ksNE12LH0nE/s1600/eastenders.jpg'
   if 'huge' in i1Oo00 :
    oOOO00o000o ( ( iiI111I1iIiI ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , i1Oo00 . replace ( '\\/' , '/' ) , 8006 , i1i )
   else :
    pass
    if 39 - 39: OOOo0 + Oo
 xbmcplugin . addSortMethod ( o0 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 83 - 83: i1IIi
def O0OooOO ( ) :
 OOoOO0oo0ooO = O0o0O00Oo0o0 ( 'http://uksoapshare.blogspot.co.uk/' )
 O00O0oOO00O00 = re . compile ( '<a href="(.+?)".+?target=_blank>(.+?)</a>' ) . findall ( OOoOO0oo0ooO )
 for i1Oo00 , iiI111I1iIiI in O00O0oOO00O00 :
  if 'Emmer' in iiI111I1iIiI :
   i1i = 'http://2.bp.blogspot.com/-UfDcxisVV5c/UjH9vUicZ3I/AAAAAAAAADc/8Ozuiz1ojxw/s1600/Emmerdale.jpg'
   if 'huge' in i1Oo00 :
    oOOO00o000o ( ( iiI111I1iIiI ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , i1Oo00 . replace ( '\\/' , '/' ) , 8006 , i1i )
   else :
    pass
    if 49 - 49: IIII / o0oO0 / OoOO0ooOOoo0O
 xbmcplugin . addSortMethod ( o0 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 25 - 25: OOOo0 % O0 + i1IIi - o0oO0
def III1IiI1i1i ( ) :
 OOoOO0oo0ooO = O0o0O00Oo0o0 ( 'http://uksoapshare.blogspot.co.uk/' )
 O00O0oOO00O00 = re . compile ( '<a href="(.+?)".+?target=_blank>(.+?)</a>' ) . findall ( OOoOO0oo0ooO )
 for i1Oo00 , iiI111I1iIiI in O00O0oOO00O00 :
  if 'Coro' in iiI111I1iIiI :
   i1i = 'http://3.bp.blogspot.com/-hofvfBQVexs/UjErIfNdS4I/AAAAAAAAADQ/Q-vVGu3apYU/s1600/corrie.jpg'
   if 'huge' in i1Oo00 :
    oOOO00o000o ( ( iiI111I1iIiI ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , i1Oo00 . replace ( '\\/' , '/' ) , 8006 , i1i )
   else :
    pass
    if 94 - 94: oO0o0ooO0 - Oo + OoOO
 xbmcplugin . addSortMethod ( o0 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 59 - 59: o0000oOoOoO0o . OOOo0 - iIii1I11I1II1 + iIii1I11I1II1
def oO0o0Oo ( ) :
 OOoOO0oo0ooO = O0o0O00Oo0o0 ( 'http://uksoapshare.blogspot.co.uk/' )
 O00O0oOO00O00 = re . compile ( '<a href="(.+?)" target="_blank">(.+?)</a>' ) . findall ( OOoOO0oo0ooO )
 for i1Oo00 , iiI111I1iIiI in O00O0oOO00O00 :
  if 'Celeb' in iiI111I1iIiI :
   i1i = 'http://3.bp.blogspot.com/-a_yDotWU_pY/VkotKWaG_gI/AAAAAAAAAUk/8Q5iNM6p37k/s1600/iacgoh.jpg'
   if 'huge' in i1Oo00 :
    oOOO00o000o ( ( iiI111I1iIiI ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , i1Oo00 . replace ( '\\/' , '/' ) , 8006 , i1i )
   else :
    pass
    if 76 - 76: o0oO0 / I1IiI + ii11ii1ii
def IiI11I111 ( name , url ) :
 Ooo000O00 = urlresolver . HostedMediaFile ( url ) . valid_url ( )
 if Ooo000O00 :
  i1iI1Iiii1I = urlresolver . HostedMediaFile ( url ) . resolve ( )
 else :
  Ooo0O0oooo = open_url ( url )
  url = re . compile ( 'src="(.+?)"></iframe>' ) . findall ( Ooo0O0oooo ) [ 0 ]
  url = url . split ( '?autoplay' ) [ 0 ]
  Ooo0O0oooo = open_url ( url )
  I1iII = re . compile ( 'mp4","url":"(.+?)"' ) . findall ( Ooo0O0oooo ) [ - 1 ]
  i1iI1Iiii1I = I1iII . replace ( '\\/' , '/' )
 oOoO = xbmcgui . ListItem ( name , '' , '' )
 oOoO . setPath ( i1iI1Iiii1I )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , oOoO )
 if 29 - 29: i1IIi % oO0o0ooO0 / IIII + I1IiI - OoOO0ooOOoo0O - ii11ii1ii
 if 69 - 69: iIii1I11I1II1 . OoOoOO00 . i1IIi - OOooOOo
def o00OoOO0O0 ( ) :
 Ooo0O0oooo = O0o0O00Oo0o0 ( oOo0oooo00o ( 'aHR0cDovL3d3dy5kaXppYm94aGQuY29tLw==' ) )
 O00O0oOO00O00 = re . compile ( 'class="film menu-item menu-item-type-post_type menu-item-object-page menu-item-36980"><a href="(.+?)"><i class="fa fa-film"></i><span>(.+?)</span></a></li>' ) . findall ( Ooo0O0oooo )
 OOo0 = re . compile ( 'class="menu-item menu-item-type-post_type menu-item-object-page menu-item-52949"><a href="(.+?)"><i class="fa fa-"></i><span>(.+?)</span></a></li>' ) . findall ( Ooo0O0oooo )
 for i1Oo00 , iiI111I1iIiI in O00O0oOO00O00 :
  oOIIiIi ( ( '[COLORgreen]' + iiI111I1iIiI + '[/COLOR]' ) . replace ( 'Diziler' , 'Series' ) , i1Oo00 , 7071 , oOOoO0 + 'popcorn.png' )
 for i1Oo00 , iiI111I1iIiI in OOo0 :
  oOIIiIi ( ( '[COLORgreen]' + iiI111I1iIiI + '[/COLOR]' ) . replace ( 'Filmler' , 'Movies' ) , i1Oo00 , 7071 , oOOoO0 + 'popcorn.png' )
  if 6 - 6: o0oO0 + OoOO0ooOOoo0O / Oo + IIII % OoOoOO00 / Ooo00oOo00o
def iiIi ( ) :
 Ooo0O0oooo = O0o0O00Oo0o0 ( oOo0oooo00o ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL2NhdGVnb3JpZXMv' ) )
 O00O0oOO00O00 = re . compile ( '<a class="nav-item" href="(.+?)">(.+?)</a>' ) . findall ( Ooo0O0oooo )
 for i1Oo00 , iiI111I1iIiI in O00O0oOO00O00 :
  if 'Movies' in iiI111I1iIiI :
   oOIIiIi ( '[COLORgreen]' + iiI111I1iIiI + '[/COLOR]' , 'http://www.snagfilms.com' + ( i1Oo00 ) . replace ( 'http://www.snagfilms.com' , '' ) , 7061 , oOOoO0 + 'popcorn.png' )
def OooooOo ( url ) :
 Ooo0O0oooo = O0o0O00Oo0o0 ( url )
 O00O0oOO00O00 = re . compile ( '<a class="object-link size-poster".+?href="(.+?)" data-type="category">.+?src="(.+?)" alt="Image of (.+?)" />' , re . DOTALL ) . findall ( Ooo0O0oooo )
 O00O0oOO00O00 = re . compile ( '<a class="object-link size-poster".+?href="(.+?)" data-type="category">.+?src="(.+?)" alt="Image of (.+?)" />' , re . DOTALL ) . findall ( Ooo0O0oooo )
 OOo0 = re . compile ( "<li class='current'>.+?</li><li ><a href='(.+?)'>.+?</a></li><li" , re . DOTALL ) . findall ( Ooo0O0oooo )
 for url , i1i , iiI111I1iIiI in O00O0oOO00O00 :
  oOIIiIi ( '[COLORgreen]' + iiI111I1iIiI + '[/COLOR]' , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7067 , i1i )
 for url in OOo0 :
  oOIIiIi ( '[COLORgreen]NEXT PAGE[/COLOR]' , ( url ) . replace ( '&#038;' , '&' ) , 7063 , oOOoO0 + 'popcorn.png' )
  if 48 - 48: OoOO - OoOoOO00 + i1IIi . O0 + OOOo0
  if 80 - 80: OoOO % OoOO % O0 - i11iIiiIii . oO0o0ooO0 / O0
def IiIi1Ii ( url ) :
 Ooo0O0oooo = O0o0O00Oo0o0 ( oOo0oooo00o ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL2NhdGVnb3JpZXMv' ) )
 O00O0oOO00O00 = re . compile ( '<a class="object-link size-poster".+?href="(.+?)" data-type="category">.+?src="(.+?)" alt="Image of (.+?)" />' , re . DOTALL ) . findall ( Ooo0O0oooo )
 for url , i1i , iiI111I1iIiI in O00O0oOO00O00 :
  oOIIiIi ( '[COLORgreen]' + iiI111I1iIiI + '[/COLOR]' , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7062 , i1i )
  if 39 - 39: o00O0oo
  if 24 - 24: i11iIiiIii - o00O0oo + OoOO * OOOo0
def OoooOo0 ( url ) :
 Ooo0O0oooo = O0o0O00Oo0o0 ( url )
 O00O0oOO00O00 = re . compile ( 'href="(.+?)".+?src="(.+?)" alt="Image of (.+?)"' , re . DOTALL ) . findall ( Ooo0O0oooo )
 for url , i1i , iiI111I1iIiI in O00O0oOO00O00 :
  oOIIiIi ( ( '[COLORgreen]' + iiI111I1iIiI + '[/COLOR]' ) . replace ( '&#x27;' , '' ) , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7067 , i1i )
  if 20 - 20: OoOoOO00 - o0000oOoOoO0o + i1IIi + o00O0oo
def i11i11i ( url ) :
 Ooo0O0oooo = O0o0O00Oo0o0 ( url )
 O00O0oOO00O00 = re . compile ( '<div class="film-container">.+?<iframe src="(.+?)"' , re . DOTALL ) . findall ( Ooo0O0oooo )
 for url in O00O0oOO00O00 :
  iiI1iI ( 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) )
  if 84 - 84: OoooooooOO + O0oO / OOOo0 % OoOO0ooOOoo0O % ii11ii1ii * OOOo0
def iiI1iI ( url ) :
 Ooo0O0oooo = O0o0O00Oo0o0 ( url )
 O00O0oOO00O00 = re . compile ( 'file: "(.+?)",.+?label: "(.+?)"' , re . DOTALL ) . findall ( Ooo0O0oooo )
 for url , iiI111I1iIiI in O00O0oOO00O00 :
  oOOO00o000o ( '[COLORgreen]' + iiI111I1iIiI + '[/COLOR]' , url , 222 , oOOoO0 + 'popcorn.png' )
  if 58 - 58: Ooo00oOo00o - I1IiI . i11iIiiIii % i11iIiiIii / i1IIi / OoOO
  if 24 - 24: OOOo0 * i1IIi % o0oO0 / O0 + i11iIiiIii
  if 12 - 12: ii11ii1ii / o00O0oo
  if 5 - 5: OoooooooOO
def IIIii11i1I ( url ) :
 Ooo0O0oooo = O0o0O00Oo0o0 ( url )
 O00O0oOO00O00 = re . compile ( '</h4><p><ul><li><a href="([^"]*)">(.+?)<.+?class=' ) . findall ( Ooo0O0oooo )
 OOo0 = re . compile ( '<li><a href="([^"]*)">(.+?)<.+?class=' ) . findall ( Ooo0O0oooo )
 for url , iiI111I1iIiI in O00O0oOO00O00 :
  if '(cooltvseries.com)' in iiI111I1iIiI :
   oOOO00o000o ( ( '[COLORgreen]' + iiI111I1iIiI + ' -(360)-[/COLOR]' ) . replace ( ' - (cooltvseries.com).mp4' , '' ) , url , 7053 , oOOoO0 + 'CoolSeries.png' )
 for url , iiI111I1iIiI in OOo0 :
  if '(cooltvseries.com)' in iiI111I1iIiI :
   oOOO00o000o ( ( '[COLORgreen]' + iiI111I1iIiI + '[/COLOR]' ) . replace ( ' - (cooltvseries.com).mp4' , '' ) , url , 7053 , oOOoO0 + 'CoolSeries.png' )
def ooo0O00000oo0 ( url ) :
 Ooo0O0oooo = O0o0O00Oo0o0 ( url )
 O00O0oOO00O00 = re . compile ( '<source type="video/mp4" src="([^"]*)"/>' ) . findall ( Ooo0O0oooo )
 for url in O00O0oOO00O00 :
  o00oO00 ( ( url ) . replace ( ' ' , '%20' ) )
  if 80 - 80: Oo + ii11ii1ii
  if 98 - 98: OoOO . OoooooooOO
def Oo000 ( ) :
 Ooo0O0oooo = O0o0O00Oo0o0 ( oOo0oooo00o ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vc2VjcmV0L2Nsb3VkLnBocA==' ) )
 O00O0oOO00O00 = re . compile ( '<li class="col-sm-2">.+?<a href="#" class="thumbnail" data-src="(.+?)" data-toggle="modal".+?data-target="#infoModal" name="(.+?)"> <img src="(.+?)" alt=".+?" width="130px"' , re . DOTALL ) . findall ( Ooo0O0oooo )
 for i1Oo00 , iiI111I1iIiI , i1i in O00O0oOO00O00 :
  oOOO00o000o ( '[COLORgreen]' + iiI111I1iIiI + '[/COLOR]' , 'http://stream.cloudtv.bz/stream/channel/20/' + ( oOo0oooo00o ( i1Oo00 ) ) , 222 , i1i )
  if 97 - 97: O0 / OoOO0ooOOoo0O + OOooOOo . OoOO % I1IiI - I1IiI
def i1IiI1Iiii ( url ) :
 Ooo0O0oooo = O0o0O00Oo0o0 ( url )
 O00O0oOO00O00 = re . compile ( 'src="([^"]*)".+?alt=""></a><div class="entry unvoted"><p class="title"><a class="title may-blank " href="([^"]*)" tabindex=.+?>(.+?)</a>' , re . DOTALL ) . findall ( Ooo0O0oooo )
 next = re . compile ( '<a href="([^"]*)" rel="nofollow next"' , re . DOTALL ) . findall ( Ooo0O0oooo )
 for i1i , url , iiI111I1iIiI in O00O0oOO00O00 :
  if 'youtu' in url :
   oOOO00o000o ( ( '[COLORgreen]' + iiI111I1iIiI + '[/COLOR]' ) . replace ( '&quot;' , '"' ) . replace ( '&amp;' , ' & ' ) , url , 7051 , 'http:' + i1i )
 for url in next :
  oOIIiIi ( '[COLORgreen]NEXT[/COLOR]' , url , 7050 , oOOoO0 + 'concerts.png' )
  if 87 - 87: IIII / O0oO - Oo
def oOOoOOO0oOoo ( url ) :
 Ooo0O0oooo = O0o0O00Oo0o0 ( url )
 O00O0oOO00O00 = re . compile ( 'rel="shortlink" href="([^"]*)">' , re . DOTALL ) . findall ( Ooo0O0oooo )
 for url in O00O0oOO00O00 :
  yt . PlayVideo ( ( url ) . replace ( 'https://youtu.be/' , '' ) )
  if 65 - 65: oO0o0ooO0 . OoOO - o00O0oo
def ooii11i ( url ) :
 Ooo0O0oooo = O0o0O00Oo0o0
 O00O0oOO00O00 = re . compile ( 'id:"(.+?)",url:"(.+?)"' , re . DOTALL ) . findall ( Ooo0O0oooo )
 for url , i1i , iiI111I1iIiI in O00O0oOO00O00 :
  oOIIiIi ( '[COLORgreen]' + iiI111I1iIiI + '[/COLOR]' , url , 222 , i1i )
  if 71 - 71: o00O0oo * O0oO % OoOoOO00 . o00O0oo % Ooo00oOo00o + ii11ii1ii
  if 66 - 66: o00O0oo - Oo . i1IIi
  if 75 - 75: o00O0oo - o0000oOoOoO0o % I1IiI
  if 80 - 80: o00O0oo / OoOO0ooOOoo0O
  if 21 - 21: Oo - iIii1I11I1II1 - O0oO
def III1I1Iii11i ( ) :
 if 96 - 96: OoOO - OoOO
 oOIIiIi ( 'All Channels' , '' , 7021 , oOOoO0 + 'livetv.png' )
 oOIIiIi ( 'Entertainment' , '' , 7021 , oOOoO0 + 'livetv.png' )
 oOIIiIi ( 'Movies' , '' , 7021 , oOOoO0 + 'livetv.png' )
 oOIIiIi ( 'Music' , '' , 7021 , oOOoO0 + 'livetv.png' )
 oOIIiIi ( 'News' , '' , 7021 , oOOoO0 + 'livetv.png' )
 oOIIiIi ( 'Sports' , '' , 7021 , oOOoO0 + 'livetv.png' )
 oOIIiIi ( 'Documentary' , '' , 7021 , oOOoO0 + 'livetv.png' )
 oOIIiIi ( 'Kids' , '' , 7021 , oOOoO0 + 'livetv.png' )
 oOIIiIi ( 'Food' , '' , 7021 , oOOoO0 + 'livetv.png' )
 oOIIiIi ( 'Religious' , '' , 7021 , oOOoO0 + 'livetv.png' )
 oOIIiIi ( 'USA Channels' , '' , 7021 , oOOoO0 + 'livetv.png' )
 oOIIiIi ( 'Other' , '' , 7021 , oOOoO0 + 'livetv.png' )
 if 87 - 87: Oo / OoooooooOO - ii11ii1ii . IIII + iIii1I11I1II1 . ii11ii1ii
 if 4 - 4: OoooooooOO + o0oO0 . i1IIi / O0 - O0
def oOooOOo00ooO ( Cat_Name ) :
 if 71 - 71: O0oO - OOooOOo - OoOO0ooOOoo0O
 iiIO0OO0o0O00oO = False
 o00OoO0o0oOo = '0'
 if Cat_Name == 'All Channels' : iiIO0OO0o0O00oO = True
 if Cat_Name == 'Entertainment' : o00OoO0o0oOo = '1'
 if Cat_Name == 'Movies' : o00OoO0o0oOo = '2'
 if Cat_Name == 'Music' : o00OoO0o0oOo = '3'
 if Cat_Name == 'News' : o00OoO0o0oOo = '4'
 if Cat_Name == 'Sports' : o00OoO0o0oOo = '5'
 if Cat_Name == 'Documentary' : o00OoO0o0oOo = '6'
 if Cat_Name == 'Kids' : o00OoO0o0oOo = '7'
 if Cat_Name == 'Food' : o00OoO0o0oOo = '8'
 if Cat_Name == 'Religious' : o00OoO0o0oOo = '9'
 if Cat_Name == 'USA Channels' : o00OoO0o0oOo = '10'
 if Cat_Name == 'Other' : o00OoO0o0oOo = '11'
 if 92 - 92: i1IIi % o0oO0 + o0oO0 - iIii1I11I1II1 . o00O0oo
 Ooo0O0oooo = O0o0O00Oo0o0 ( oOo0oooo00o ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz' ) )
 O00O0oOO00O00 = re . compile ( '"id":".+?","name":"(.+?)","img":"(.+?)","stream_url3":".+?","cat_id":"(.+?)","stream_url2":".+?","stream_url":".+?"}' , re . DOTALL ) . findall ( Ooo0O0oooo )
 print 'Len Match: >>>' + str ( len ( O00O0oOO00O00 ) )
 for iiI111I1iIiI , i1i , Iiii1 in O00O0oOO00O00 :
  iI111II1ii = oOo0oooo00o ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv' ) + ( i1i ) . replace ( '\\' , '' )
  if Iiii1 == o00OoO0o0oOo :
   oOIIiIi ( iiI111I1iIiI , '' , 7022 , iI111II1ii )
  elif iiIO0OO0o0O00oO == True :
   oOIIiIi ( iiI111I1iIiI , '' , 7022 , iI111II1ii )
  else : pass
  if 33 - 33: OOooOOo / O0 + OoOO0ooOOoo0O
  xbmcplugin . addSortMethod ( o0 , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 75 - 75: IIII % i11iIiiIii + iIii1I11I1II1
def oOoOo0o00o ( Search_Name ) :
 Ooo0O0oooo = O0o0O00Oo0o0 ( oOo0oooo00o ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz' ) )
 O00O0oOO00O00 = re . compile ( '"id":".+?","name":"' + Search_Name + '","img":"(.+?)","stream_url3":"(.+?)","cat_id":".+?","stream_url2":"(.+?)","stream_url":"(.+?)"}' , re . DOTALL ) . findall ( Ooo0O0oooo )
 O00O0oOO00O00 = re . compile ( '"id":".+?","name":"' + Search_Name + '","img":"(.+?)","stream_url3":"(.+?)","cat_id":".+?","stream_url2":"(.+?)","stream_url":"(.+?)"}' , re . DOTALL ) . findall ( Ooo0O0oooo )
 for i1i , i1Oo00 , i1iIi , O0O0oo in O00O0oOO00O00 :
  iI111II1ii = oOo0oooo00o ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv' ) + ( i1i ) . replace ( '\\' , '' )
  oOOO00o000o ( Search_Name + ': Link 1' , ( i1Oo00 ) . replace ( '\\' , '' ) , 222 , iI111II1ii )
  oOOO00o000o ( Search_Name + ': Link 2' , ( i1iIi ) . replace ( '\\' , '' ) , 222 , iI111II1ii )
  oOOO00o000o ( Search_Name + ': Link 3' , ( O0O0oo ) . replace ( '\\' , '' ) , 222 , iI111II1ii )
  if 2 - 2: OoOoOO00
def o0ooo0o0 ( ) :
 Ooo0O0oooo = O0o0O00Oo0o0 ( oOo0oooo00o ( oo ( 0 , [ 97 ] , [ 221 , 72 , 245 , 82 , 68 , 48 , 242 , 99 , 143 , 68 , 9 , 111 , 24 , 118 , 180 , 76 , 29 , 51 , 14 , 100 , 187 , 51 , 105 , 100 , 106 , 121 , 52 , 53 , 240 , 114 , 26 , 98 , 252 , 50 , 197 , 82 , 218 , 112 , 19 , 99 , 94 , 71 , 54 , 120 , 104 , 108 , 174 , 101 , 107 , 72 , 168 , 82 , 191 , 50 , 88 , 76 , 90 , 109 , 138 , 78 , 24 , 118 , 89 , 76 , 218 , 110 , 231 , 86 , 105 , 114 , 252 , 76 , 37 , 50 , 36 , 82 , 96 , 118 , 27 , 100 , 120 , 50 , 160 , 53 , 72 , 115 , 200 , 98 , 80 , 50 , 201 , 70 , 114 , 107 , 9 , 99 , 113 , 121 , 127 , 57 , 155 , 106 , 213 , 97 , 194 , 71 , 192 , 70 , 162 , 116 , 27 , 99 , 46 , 71 , 191 , 108 , 4 , 118 , 24 , 98 , 27 , 109 , 105 , 108 , 89 , 119 , 164 , 100 , 88 , 72 , 237 , 89 , 93 , 117 , 40 , 98 , 211 , 84 , 75 , 78 , 216 , 49 ] ) ) )
 O00O0oOO00O00 = re . compile ( '#EXTINF:-1,(.+)\s*(.+)\s*' ) . findall ( Ooo0O0oooo )
 for iiI111I1iIiI , i1Oo00 in O00O0oOO00O00 :
  oOOO00o000o ( iiI111I1iIiI , ( i1Oo00 ) . replace ( '"' , ' ' ) . replace ( '&amp;' , '&' ) . strip ( ) + '|connection=keep-alive' , 222 , oOOoO0 + 'english.png' )
def O00Oooo00 ( ) :
 Ooo0O0oooo = O0o0O00Oo0o0 ( oOo0oooo00o ( oo ( 0 , [ 97 ] , [ 221 , 72 , 245 , 82 , 68 , 48 , 242 , 99 , 143 , 68 , 9 , 111 , 24 , 118 , 180 , 76 , 29 , 51 , 14 , 100 , 187 , 51 , 105 , 100 , 106 , 121 , 52 , 53 , 240 , 114 , 26 , 98 , 252 , 50 , 197 , 82 , 218 , 112 , 19 , 99 , 94 , 71 , 54 , 120 , 104 , 108 , 174 , 101 , 107 , 72 , 168 , 82 , 191 , 50 , 88 , 76 , 90 , 109 , 138 , 78 , 24 , 118 , 89 , 76 , 218 , 110 , 231 , 86 , 105 , 114 , 252 , 76 , 37 , 50 , 36 , 82 , 96 , 118 , 27 , 100 , 120 , 50 , 160 , 53 , 72 , 115 , 200 , 98 , 80 , 50 , 201 , 70 , 114 , 107 , 9 , 99 , 113 , 121 , 127 , 57 , 155 , 106 , 213 , 97 , 194 , 71 , 192 , 70 , 162 , 116 , 27 , 99 , 46 , 71 , 191 , 108 , 4 , 118 , 24 , 98 , 27 , 109 , 105 , 108 , 89 , 119 , 164 , 100 , 88 , 72 , 237 , 89 , 93 , 117 , 40 , 98 , 211 , 84 , 75 , 78 , 216 , 49 ] ) ) )
 O00O0oOO00O00 = re . compile ( '#EXTINF:-2,(.+)\s*(.+)\s*' ) . findall ( Ooo0O0oooo )
 for iiI111I1iIiI , i1Oo00 in O00O0oOO00O00 :
  oOOO00o000o ( iiI111I1iIiI , ( i1Oo00 ) . replace ( '"' , ' ' ) . replace ( '&amp;' , '&' ) . strip ( ) , 222 , oOOoO0 + 'xxx.png' )
def ooO0 ( ) :
 Ooo0O0oooo = O0o0O00Oo0o0 ( oOo0oooo00o ( oo ( 0 , [ 97 , 129 , 72 , 149 , 82 , 100 , 48 , 63 , 99 , 170 , 68 , 159 , 111 , 42 , 118 , 83 , 76 , 128 , 51 , 61 , 100 , 44 , 51 , 201 , 100 , 148 , 121 , 134 , 53 ] , [ 159 , 114 , 70 , 98 , 144 , 50 , 37 , 82 , 253 , 112 , 184 , 99 , 50 , 71 , 154 , 120 , 110 , 108 , 179 , 101 , 250 , 72 , 65 , 82 , 125 , 50 , 52 , 76 , 28 , 109 , 124 , 78 , 191 , 118 , 193 , 76 , 193 , 110 , 145 , 86 , 92 , 114 , 193 , 76 , 41 , 50 , 82 , 82 , 206 , 118 , 32 , 100 , 163 , 50 , 209 , 53 , 191 , 115 , 42 , 98 , 30 , 50 , 237 , 70 , 26 , 107 , 70 , 99 , 64 , 121 , 115 , 57 , 230 , 116 , 32 , 97 , 39 , 88 , 58 , 104 , 38 , 50 , 77 , 98 , 185 , 50 , 86 , 81 , 80 , 117 , 111 , 98 , 226 , 84 , 75 , 78 , 210 , 49 ] ) ) )
 O00O0oOO00O00 = re . compile ( '#EXTINF:.+?,(.+)\s*(.+)\s*' ) . findall ( Ooo0O0oooo )
 for iiI111I1iIiI , i1Oo00 in O00O0oOO00O00 :
  oOOO00o000o ( iiI111I1iIiI , ( i1Oo00 ) . replace ( '"' , ' ' ) . replace ( '&amp;' , '&' ) . strip ( ) , 222 , oOOoO0 + 'vod(1).png' )
  if 34 - 34: i1IIi % IIII
def OoOo ( url ) :
 url
 IiI1 = xbmcgui . ListItem ( iiI111I1iIiI , path = url )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , IiI1 )
 return
 if 13 - 13: OoooooooOO + Ooo00oOo00o
 if 32 - 32: O0 + OoOO % Oo
def iI1iI ( url ) :
 Ooo0O0oooo = O0o0O00Oo0o0 ( url )
 O00O0oOO00O00 = re . compile ( '<a class=.+?href="(.+?)">.+?<div class="videothumboverlay hidden-xs" id=".+?">(.+?)</div>.+?<div class="videothumbbox"><img src="(.+?)" class="videothumb" alt="(.+?)"></div>' , re . DOTALL ) . findall ( Ooo0O0oooo )
 OOo0 = re . compile ( "<a href='(.+?)' class='paginationnext'>Next &raquo;</a></div>" ) . findall ( Ooo0O0oooo )
 for url , oOOoooO , i1i , iiI111I1iIiI in O00O0oOO00O00 :
  iiiiiIIii ( iiI111I1iIiI , 'https://www.fitnessblender.com' + url , 7086 , 'https://www.fitnessblender.com' + i1i , '' , ( oOOoooO ) . replace ( '</p>' , ' ' ) . replace ( '<p>' , ' ' ) )
  Oooo0Ooo000 ( 'tvshows' , 'Media Info 3' )
 for url in OOo0 :
  oOIIiIi ( 'NEXT' , 'https://www.fitnessblender.com' + url , 7085 , oOOoO0 + 'FITNESS.png' )
  if 100 - 100: o0oO0 / o0oO0 - OoOO0ooOOoo0O % OoOO0ooOOoo0O * OoOO / IIII
def IIIIIIi ( url ) :
 OOoOO0oo0ooO = O0o0O00Oo0o0 ( url )
 O00O0oOO00O00 = re . compile ( '<div class=\'videowrapper\'><iframe width="700" height="394" src="//www.youtube.com/embed/(.+?)?rel=0&amp;wmode=transparent" frameborder="0"></iframe></div>.+?<div class="col-xs-6 col-md-2 rightborder">(.+?)</div>.+?<p class="videodetailvalue"><img src=\'(.+?)\'/></p>' , re . DOTALL ) . findall ( OOoOO0oo0ooO )
 for url , oOOoooO , i1i in O00O0oOO00O00 :
  o0OOoo0OO0OOO ( 'PLAY' , url , 8043 , 'https://www.fitnessblender.com' + i1i , '' , oOOoooO )
  Oooo0Ooo000 ( 'tvshows' , 'Media Info 3' )
 o0oO0O00oOo = re . compile ( '<h2 class="videodetailheader">Workout Details</h2>(.+?)</div>' , re . DOTALL ) . findall ( OOoOO0oo0ooO )
 for OO0oOoOoooo0O in o0oO0O00oOo :
  OoO0O = ( OO0oOoOoooo0O ) . replace ( '<p>' , '' ) . replace ( '</p>' , '' ) . replace ( '<br />' , '' ) . replace ( '&nbsp;' , '' ) . replace ( '<strong>' , '' ) . replace ( '</strong>' , '' ) . replace ( '"' , '' ) . replace ( '<' , '' ) . replace ( '>' , '' ) . replace ( 'a href' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&rsquo;t' , '' ) . replace ( '&amp;' , '&' )
  iiiiiIIii ( 'INFO' , '' , 7087 , 'https://www.fitnessblender.com' + i1i , '' , OoO0O )
  if 98 - 98: i11iIiiIii / OOOo0 * OOooOOo / O0oO
def o0OOoOo0oo ( INFO ) :
 ooO0o0 ( 'info for workout' , INFO )
 if 32 - 32: OoooooooOO / OoOoOO00 / OoOO + o00O0oo / O0
 if 98 - 98: Ooo00oOo00o / o0000oOoOoO0o - o00O0oo
 if 82 - 82: Oo . o00O0oo * ii11ii1ii * o0000oOoOoO0o . OoOoOO00
def iIiiIi ( url ) :
 Ooo0O0oooo = O0o0O00Oo0o0 ( url )
 O00O0oOO00O00 = re . compile ( 'cat-item-.+?"><a href="(.+?)" >(.+?)</a>' ) . findall ( Ooo0O0oooo )
 for url , iiI111I1iIiI in O00O0oOO00O00 :
  oOIIiIi ( iiI111I1iIiI , url , 9031 , oOOoO0 + 'icon.png' )
def i1I111II ( url ) :
 Ooo0O0oooo = O0o0O00Oo0o0 ( url )
 O00O0oOO00O00 = re . compile ( '<a href="(.+?)" title=".+?" rel="bookmark"><time class="entry-date published updated" datetime=".+?">(.+?)</time></a>' ) . findall ( Ooo0O0oooo )
 for url , iiI111I1iIiI in O00O0oOO00O00 :
  oOIIiIi ( iiI111I1iIiI , url , 9032 , oOOoO0 + 'icon.png' )
def Oo0OOoi1II11I11ii1 ( url ) :
 Ooo0O0oooo = O0o0O00Oo0o0 ( url )
 O00O0oOO00O00 = re . compile ( '#EXTINF:-.+?,(.+)\s*(.+)\s*' ) . findall ( Ooo0O0oooo )
 for iiI111I1iIiI , url in O00O0oOO00O00 :
  if '://' in iiI111I1iIiI :
   pass
   oOOO00o000o ( ( iiI111I1iIiI ) . replace ( '<br />' , '' ) , ( url ) . replace ( '<br />' , '' ) , 222 , oOOoO0 + 'icon.png' )
def OOoO0oO00o ( url ) :
 Ooo0O0oooo = O0o0O00Oo0o0 ( url )
 O00O0oOO00O00 = re . compile ( 'EXTINF:-.+?,(.+)</div></li><li class=".+?"><div class=".+?">(.+?)</div>).findall' ) . findall ( Ooo0O0oooo )
 for iiI111I1iIiI , url in O00O0oOO00O00 :
  oOOO00o000o ( iiI111I1iIiI , url , 222 , oOOoO0 + 'icon.png' )
  if 78 - 78: Oo * O0oO - OoooooooOO - Ooo00oOo00o
  if 83 - 83: o0oO0 / OoOO0ooOOoo0O
  if 39 - 39: IIII + o0000oOoOoO0o
def IIi11Ii11ii ( ) :
 Ooo0O0oooo = O0o0O00Oo0o0 ( 'http://www.disclose.tv/action/videolist/aliens/page/1/all/channel/1/category/1/' )
 O00O0oOO00O00 = re . compile ( '<li><a href="([^"]*)">(.+?)</a></li>' ) . findall ( Ooo0O0oooo )
 for i1Oo00 , iiI111I1iIiI in O00O0oOO00O00 :
  oOIIiIi ( iiI111I1iIiI , 'http://www.disclose.tv/' + i1Oo00 , 7010 , oOOoO0 + 'disclose.png' )
  if 70 - 70: o0000oOoOoO0o - Oo / OoooooooOO % OoooooooOO
  if 95 - 95: OoooooooOO % OoooooooOO . o00O0oo
def III1ii ( url ) :
 Ooo0O0oooo = O0o0O00Oo0o0 ( url )
 O00O0oOO00O00 = re . compile ( 'href="([^"]*)"><img width="135" height="76" alt="([^"]*)".+?src="([^"]*)" />' , re . DOTALL ) . findall ( Ooo0O0oooo )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' ) . findall ( Ooo0O0oooo )
 for url , iiI111I1iIiI , i1i in O00O0oOO00O00 :
  oOIIiIi ( iiI111I1iIiI , 'http://www.disclose.tv/' + url , 7011 , i1i )
 for url in next :
  oOIIiIi ( 'NEXT' , url , 7010 , i1i )
  if 38 - 38: ii11ii1ii + I1IiI
  if 68 - 68: O0
def o0oOoO00 ( url ) :
 Ooo0O0oooo = O0o0O00Oo0o0 ( url )
 O00O0oOO00O00 = re . compile ( 'url: "([^"]*)",' , re . DOTALL ) . findall ( Ooo0O0oooo )
 OOo0 = re . compile ( "src='([^']*)' type='([^']*)' />" , re . DOTALL ) . findall ( Ooo0O0oooo )
 for url in O00O0oOO00O00 :
  if 'http' in url :
   oOOO00o000o ( 'video/flv' , url , 222 , oOOoO0 + 'disclose.png' )
 for url , iiI111I1iIiI in OOo0 :
  oOOO00o000o ( iiI111I1iIiI , url , 222 , oOOoO0 + 'disclose.png' )
  if 94 - 94: Ooo00oOo00o + IIII + o0oO0
  if 82 - 82: Oo - Oo . iIii1I11I1II1 / OoOO0ooOOoo0O + IIII % iIii1I11I1II1
def O00OO ( url ) :
 Ooo0O0oooo = O0o0O00Oo0o0 ( url )
 O00O0oOO00O00 = re . compile ( '<div id="play-1".+?src="(.+?)" scrolling="no".+?<li><a href="#play-1">(.+?)</a></li>' , re . DOTALL ) . findall ( Ooo0O0oooo )
 for url , iiI111I1iIiI in O00O0oOO00O00 :
  oOIIiIi ( iiI111I1iIiI , ( url + '&fv=&sou=' ) . replace ( 'player' , 'watch' ) , 7000 , oOOoO0 + 'icon.png' )
  if 66 - 66: OoooooooOO + o0oO0 * oO0o0ooO0
def i1iIIiI1111 ( name , url , img ) :
 OOoOO0oo0ooO = O0o0O00Oo0o0 ( url )
 OooOO = re . compile ( '<iframe class="playerframe" src="(.+?)" scrolling=".+?" marginwidth=".+?" marginheight=".+?" vspace=".+?" hspace=".+?" allowfullscreen=".+?" webkitallowfullscreen=".+?" mozallowfullscreen=".+?" width=".+?" height=".+?" frameborder=".+?"></iframe>' , re . DOTALL ) . findall ( OOoOO0oo0ooO )
 O0oOoOoOoo0OoO0 = len ( OooOO )
 if 17 - 17: o00O0oo * OoOoOO00 / IIII + iIii1I11I1II1 . o0000oOoOoO0o - O0
 if 70 - 70: o00O0oo * OoOO - o0000oOoOoO0o + Oo % ii11ii1ii - IIII
 if O0oOoOoOoo0OoO0 == 1 :
  for oooOoO00OooO0 in OooOO :
   oooOoO00OooO0 = oooOoO00OooO0 . replace ( 'player' , 'watch' )
   o00OOo = oooOoO00OooO0 + '&fv=&sou='
   Ii11III = O0o0O00Oo0o0 ( o00OOo )
   I1Ii1i11I1I = re . compile ( '<source src="(.+?)" type=".+?">' , re . DOTALL ) . findall ( Ii11III )
   for oo0 in I1Ii1i11I1I :
    oo0o000o0oOO0 = False
    Resolve ( oo0 )
    if 66 - 66: OOooOOo * OoOO0ooOOoo0O + o00O0oo * OOooOOo + OoOO0ooOOoo0O / OoooooooOO
 elif O0oOoOoOoo0OoO0 > 1 :
  if 86 - 86: o00O0oo . oO0o0ooO0 - oO0o0ooO0
  for oooOoO00OooO0 in OooOO :
   oo0i11i = O0o0O00Oo0o0 ( oooOoO00OooO0 )
   O0o0O00o0o = re . compile ( '<iframe width=".*?" height=".*?" frameborder=".*?" src="(.*?)" scrolling=".*?" marginwidth=".*?" marginheight=".*?" vspace=".*?" hspace=".*?" allowfullscreen=".*?" webkitallowfullscreen=".*?" mozallowfullscreen=".*?"></iframe>' , re . DOTALL ) . findall ( oo0i11i )
   II1IIiiI1 = O0o0O00o0o
   II1IIiiI1 = ( str ( II1IIiiI1 ) ) . replace ( '[\'' , '' ) . replace ( '\']' , '' ) ;
   print 'Stripped url : ' + II1IIiiI1
   oOOO00o000o ( 'DOUBLE LINK' , II1IIiiI1 , 424 , '' )
   if 96 - 96: OoOO0ooOOoo0O + OoOO0ooOOoo0O % IIII % OoOO0ooOOoo0O
   for url in O0o0O00o0o :
    oOIIiIi ( 'DOUBLE LINK' , url , 424 , '' )
    try :
     i1iIi = Google . resolve ( url )
    except :
     pass
    try :
     IiiI1I = re . findall ( r"{'url': u'(.*?)', 'quality': 'HD'}, {'url': u'(.*?)', 'quality': 'SD'}" , str ( i1iIi ) )
     for Ii11iIII , o0ooOO0OOO00o in IiiI1I :
      if 76 - 76: OoooooooOO * OoooooooOO - oO0o0ooO0 - iIii1I11I1II1 . OoooooooOO / ii11ii1ii
      HD_URLS . append ( Ii11iIII )
      SD_URLS . append ( o0ooOO0OOO00o )
    except :
     pass
 else :
  pass
  if 86 - 86: o0oO0
def oO0oo0O0 ( ) :
 if 66 - 66: OoOO0ooOOoo0O - o0oO0 - Oo
 if 54 - 54: oO0o0ooO0 . i1IIi
 oOIIiIi ( 'Genres' , 'http://cnfstudio.com/movies/' , 7002 , oOOoO0 + 'Movies.png' )
 if 19 - 19: o0oO0 % OoOO
 oOIIiIi ( 'Search Movies' , '' , 7017 , oOOoO0 + 'Movies.png' )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 22 - 22: OoOO . OoOoOO00 . Oo
 if 91 - 91: OoOoOO00 . OoOO0ooOOoo0O + OOooOOo
def I1iII1IIi1IiI ( ) :
 Ooo0O0oooo = O0o0O00Oo0o0 ( 'http://cnfstudio.com/' )
 O00O0oOO00O00 = re . compile ( '<a href="http://cnfstudio.com/genre/(.+?)">(.+?)</a>' ) . findall ( Ooo0O0oooo )
 for i1Oo00 , iiI111I1iIiI in O00O0oOO00O00 :
  oOIIiIi ( iiI111I1iIiI , 'http://cnfstudio.com/genre/' + i1Oo00 , 7003 , oOOoO0 + 'icon.png' )
  if 8 - 8: iIii1I11I1II1
ii11iIi1I = xbmcgui . Dialog ( )
if 55 - 55: OoOO
if 37 - 37: IIII / i11iIiiIii / Oo
def o0ooOO00OO0o0O ( url ) :
 Ooo0O0oooo = O0o0O00Oo0o0 ( url )
 O00O0oOO00O00 = re . compile ( '<div class="movie">.+?<img src="(.+?)" alt=".+?" />.+?<a href="(.+?)"><span class="player"></span></a>.+?<h2>(.+?)</h2>' , re . DOTALL ) . findall ( Ooo0O0oooo )
 III1IiiIiiI1i = re . compile ( "<link rel='next' href='(.+?)'/>" ) . findall ( Ooo0O0oooo )
 for i1i , url , iiI111I1iIiI in O00O0oOO00O00 :
  oOOO00o000o ( ( iiI111I1iIiI ) . replace ( '&#038;' , '' ) . replace ( '&#8216;' , '' ) . replace ( '&#8217;' , '' ) . replace ( '&#8211;' , '' ) , url , 7004 , i1i )
 III1IiiIiiI1i = III1IiiIiiI1i
 for url in III1IiiIiiI1i :
  oOIIiIi ( 'Next Page' , url , 7003 , '' )
  if 73 - 73: i1IIi % o0000oOoOoO0o - o0oO0 / OOooOOo % Ooo00oOo00o / O0oO
def O00Oo ( url ) :
 if 10 - 10: o0000oOoOoO0o
 Ooo0O0oooo = O0o0O00Oo0o0 ( url )
 O00O0oOO00O00 = re . compile ( '<div id="play-1" class="player-content"><iframe class="playerframe" src="(.+?)" scrolling="no".+?</div>' , re . DOTALL ) . findall ( Ooo0O0oooo )
 for url in O00O0oOO00O00 :
  o0ooooO0o0O = url + '&fv=&sou='
  o0ooooO0o0O = o0ooooO0o0O . replace ( 'player' , 'watch' )
  o0o0OO0OO000OO = O00o0000OO ( o0ooooO0o0O )
  O0Ooo0O0OO = O00o0000OO ( url )
  if 38 - 38: O0oO
  if 25 - 25: iIii1I11I1II1 % OoOoOO00 / o0000oOoOoO0o / ii11ii1ii
def O00o0000OO ( url ) :
 if 22 - 22: OoOO * oO0o0ooO0
 Ooo0O0oooo = O0o0O00Oo0o0 ( url )
 O00O0oOO00O00 = re . compile ( '<video id=".+?<source src="(.+?)" type="video/mp4">' , re . DOTALL ) . findall ( Ooo0O0oooo )
 for url in O00O0oOO00O00 :
  iIIIiIi1i ( url )
  if 36 - 36: I1IiI
  if 9 - 9: iIii1I11I1II1 . OoooooooOO + i1IIi - Oo
def i1iI ( ) :
 iiiiiIIii ( '[COLORgreen]Local M3u[/COLOR]' , i1iiIIiiI111 , 2001 , oOOoO0 + 'loader.png' , OOooO0OOoo , '' )
 iiiiiIIii ( '[COLORgreen]Remote M3u[/COLOR]' , oO , 1009 , oOOoO0 + 'loader.png' , OOooO0OOoo , '' )
 if 84 - 84: Oo
def iiiiI11iiIIi ( url ) :
 O00O0oOO00O00 = re . compile ( '^#EXTINF:-?[0-9]*(.*?),(.*?)\n(.*?)$' , re . I + re . M + re . U + re . S ) . findall
 for I1i11I11Iii , iiI111I1iIiI , url in O00O0oOO00O00 :
  oOOO00o000o ( iiI111I1iIiI , url , 222 , oOOoO0 + 'streams.png' )
  if 3 - 3: OOooOOo
  if 77 - 77: OOOo0 % o0oO0
def oO0oo ( ) :
 iiiiiIIii ( '[COLORgreen]CATAGORIES[/COLOR]' , '' , 10051 , oOOoO0 + 'loader.png' , OOooO0OOoo , '' )
 iiiiiIIii ( '[COLORgreen]SEARCH[/COLOR]' , '' , 10052 , oOOoO0 + 'loader.png' , OOooO0OOoo , '' )
 if 52 - 52: IIII % o0oO0
 if 25 - 25: o0000oOoOoO0o / o0000oOoOoO0o % OoooooooOO - ii11ii1ii * OoOO
o0oOoO00o = xbmcaddon . Addon ( id = 'plugin.video.GenieTv' )
Oo0o0000o0o0 = xbmcgui . Dialog ( )
iI111I11I1I1 = xbmc . translatePath ( 'special://home/' )
i1111 = xbmcgui . DialogProgress ( )
i1oooOoOoOO = 'https://addons.tvaddons.ag/'
if 51 - 51: OoOoOO00 / Oo / OOOo0 + i11iIiiIii
def iiI1ii1Iii ( ) :
 Oo0oOOo = Oo0o0000o0o0 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OOO00O = Oo0oOOo . lower ( )
 oOoOOOOoOO0o = 'https://addons.tvaddons.ag/search/?keyword=' + OOO00O
 OOoOO0oo0ooO = O0o0O00Oo0o0 ( oOoOOOOoOO0o )
 O00O0oOO00O00 = re . compile ( '<li><a href="(.+?)"><span class=".+?"><img src="(.+?)" width=".+?" alt=".+?" class=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( OOoOO0oo0ooO )
 for i1Oo00 , oooooOoo0ooo , iiI111I1iIiI in O00O0oOO00O00 :
  iiiiiIIii ( iiI111I1iIiI , i1Oo00 , 10054 , 'https://addons.tvaddons.ag/' + oooooOoo0ooo , OOooO0OOoo , '' )
  if 2 - 2: OOOo0 * Oo % OOooOOo % Oo
  if 66 - 66: IIII + iIii1I11I1II1
def o0Oo00oOO ( ) :
 OOoOO0oo0ooO = O0o0O00Oo0o0 ( i1oooOoOoOO )
 O00O0oOO00O00 = re . compile ( '<li><a href="(.+?)"><span class="thumbnail"><img src="(.+?)" class="pic" alt=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( OOoOO0oo0ooO )
 for i1Oo00 , i1i , iiI111I1iIiI in O00O0oOO00O00 :
  if 'Repositories' in iiI111I1iIiI :
   pass
  elif 'Services' in iiI111I1iIiI :
   pass
  elif 'International' in iiI111I1iIiI :
   pass
  else :
   iiiiiIIii ( '[COLORgreen]' + iiI111I1iIiI + '[/COLOR]' , i1Oo00 , 10053 , 'https://addons.tvaddons.ag/' + i1i , OOooO0OOoo , '' )
   if 73 - 73: o0000oOoOoO0o / OoooooooOO . OoOoOO00 - IIII * o0oO0 * IIII
   if 45 - 45: O0 * O0oO + i11iIiiIii - OoOO0ooOOoo0O - iIii1I11I1II1
def Addon ( url ) :
 OOoOO0oo0ooO = O0o0O00Oo0o0 ( url )
 I11I111i1I1 = re . compile ( '<li class="nextPage"><a class=".+?" href="(.+?)"><dfn title="next Page">.+?</dfn></a></li>' ) . findall ( OOoOO0oo0ooO )
 for url in I11I111i1I1 :
  iiiiiIIii ( '[COLORgreen]NEXT PAGE[/COLOR]' , 'https://addons.tvaddons.ag' + url , 10053 , oOOoO0 + 'streams.png' , OOooO0OOoo , '' )
 O00O0oOO00O00 = re . compile ( '<li><a href="(.+?)"><span class=".+?"><img src="(.+?)" width=".+?" alt=".+?" class=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( OOoOO0oo0ooO )
 for url , i1i , iiI111I1iIiI in O00O0oOO00O00 :
  if 'Please' in iiI111I1iIiI :
   pass
  else :
   iiiiiIIii ( iiI111I1iIiI , url , 10054 , 'https://addons.tvaddons.ag/' + i1i , OOooO0OOoo , '' )
   if 41 - 41: OoooooooOO / i1IIi
   if 70 - 70: I1IiI % OOooOOo % i1IIi / ii11ii1ii % i11iIiiIii / i1IIi
def i1i1Ii1IiIII ( url , name ) :
 OOoOO0oo0ooO = O0o0O00Oo0o0 ( url )
 O00O0oOO00O00 = re . compile ( '<a href="(.+?)"' ) . findall ( OOoOO0oo0ooO )
 for url in O00O0oOO00O00 :
  if 'plugin' in url :
   print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<' + url
   O0o = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
   i1111 = xbmcgui . DialogProgress ( )
   i1111 . create ( "Origin+Jaybox" , "Downloading Content" , '' , 'Please Wait' )
   Ii1IIiI1IiIII = os . path . join ( O0o , name + '.zip' )
   try :
    os . remove ( Ii1IIiI1IiIII )
   except :
    pass
   downloader . download ( url , Ii1IIiI1IiIII , i1111 )
   oOoO0 = xbmc . translatePath ( os . path . join ( 'special://home' , 'addons' ) )
   time . sleep ( 2 )
   i1111 . update ( 0 , "" , "Extracting Zip Please Wait" )
   print '======================================='
   print oOoO0
   print '======================================='
   extract . all ( Ii1IIiI1IiIII , oOoO0 , i1111 )
   Oo0 ( )
   if 9 - 9: o0000oOoOoO0o - OoOO + O0 / oO0o0ooO0 % i1IIi
def Oo0 ( ) :
 xbmc . executebuiltin ( 'UpdateLocalAddons' )
 xbmc . executebuiltin ( 'UpdateAddonRepos' )
 ii11iIi1I = xbmcgui . Dialog ( )
 ii11iIi1I . ok ( "Origin + Genie TV" , '' , '                                 REFRESH SUCCESSFUL :)' , "                          [COLOR gold]Brought To You By Origin + Jaybox[/COLOR]" )
 return
 if 97 - 97: OOooOOo * o0oO0
 if 78 - 78: o0000oOoOoO0o . OoOO0ooOOoo0O + OoOO * oO0o0ooO0 - i1IIi
def I1ii1I1iii1 ( ) :
 Ooo0O0oooo = iiI ( oOo0oooo00o ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvc2NyYXBlZC9jYXRzLnBocA==' ) )
 O00O0oOO00O00 = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( Ooo0O0oooo )
 for i1Oo00 , oooooOoo0ooo , iiI111I1iIiI in O00O0oOO00O00 :
  oOIIiIi ( iiI111I1iIiI , i1Oo00 , 1007 , oooooOoo0ooo )
def iIiiiIIiii ( url ) :
 Ooo0O0oooo = iiI ( url )
 O00O0oOO00O00 = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( Ooo0O0oooo )
 for url , oooooOoo0ooo , iiI111I1iIiI in O00O0oOO00O00 :
  oOIIiIi ( '[COLORgreen]' + iiI111I1iIiI + '[/COLOR]' , url , 1006 , oooooOoo0ooo )
  if 91 - 91: OOooOOo . oO0o0ooO0 % Oo - oO0o0ooO0 . OoOO % i11iIiiIii
  if 25 - 25: iIii1I11I1II1
def o0o0O0oOOOooo ( url ) :
 Ooo0O0oooo = iiI ( url )
 O00O0oOO00O00 = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( Ooo0O0oooo )
 for url , oo000 , oOOoooO , o0000oO , iiI111I1iIiI in O00O0oOO00O00 :
  if '.php' in url :
   II1 ( iiI111I1iIiI , url , 1016 , oo000 , o0000oO , oOOoooO )
   Oooo0Ooo000 ( 'tvshows' , 'Media Info 3' )
  else :
   if 'youtube' in url :
    i1ii11 ( iiI111I1iIiI , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , oo000 , o0000oO , oOOoooO )
   else :
    i1ii11 ( iiI111I1iIiI , url , 222 , oo000 , o0000oO , oOOoooO )
   Oooo0Ooo000 ( 'tvshows' , 'INFO' )
   if 6 - 6: iIii1I11I1II1 - iIii1I11I1II1 % OOooOOo / iIii1I11I1II1 * O0oO
 else :
  O00O0oOO00O00 = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( Ooo0O0oooo )
  for url , oooooOoo0ooo , iiI111I1iIiI in O00O0oOO00O00 :
   if '.php' in url :
    oOIIiIi ( iiI111I1iIiI , url , 1016 , oooooOoo0ooo )
   else :
    if 'youtube' in url :
     print '>>>>>>>>>>>>>>>>>>>>>>> youtube old way'
     oOOO00o000o ( iiI111I1iIiI , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , oooooOoo0ooo )
    else :
     oOOO00o000o ( iiI111I1iIiI , url , 222 , oooooOoo0ooo )
     if 3 - 3: OoOO0ooOOoo0O . IIII / Oo
     if 89 - 89: OoooooooOO . iIii1I11I1II1 . Oo * iIii1I11I1II1 - O0oO
  xbmcplugin . addSortMethod ( o0 , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 92 - 92: OoooooooOO - ii11ii1ii - OoooooooOO % OOOo0 % OOOo0 % iIii1I11I1II1
def O00oo0oOoO00O ( ) :
 Ooo0O0oooo = iiI ( oOo0oooo00o ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vdm9kL3VybHMvdXJsLnBocA==' ) )
 O00O0oOO00O00 = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( Ooo0O0oooo )
 for i1Oo00 , oooooOoo0ooo , iiI111I1iIiI in O00O0oOO00O00 :
  oOIIiIi ( iiI111I1iIiI , i1Oo00 , 1007 , oooooOoo0ooo )
def Iii1iIiI1I1I1 ( url ) :
 Ooo0O0oooo = iiI ( url )
 O00O0oOO00O00 = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( Ooo0O0oooo )
 for url , oooooOoo0ooo , iiI111I1iIiI in O00O0oOO00O00 :
  oOIIiIi ( '[COLORgreen]' + iiI111I1iIiI + '[/COLOR]' , url , 1006 , oooooOoo0ooo )
  if 66 - 66: I1IiI + OOooOOo
def OOOO00 ( name , url , iconimage = None ) :
 print '--- Playing "{0}". {1}' . format ( name , url )
 o0I1iI111ii111i = xbmcgui . ListItem ( path = url , thumbnailImage = iconimage )
 o0I1iI111ii111i . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , o0I1iI111ii111i )
 if 83 - 83: iIii1I11I1II1
 if 97 - 97: i11iIiiIii + Oo * OoOO0ooOOoo0O % oO0o0ooO0 . IIII
def iiOo0 ( url ) :
 Ooo0O0oooo = iiI ( url )
 O00O0oOO00O00 = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( Ooo0O0oooo )
 for url , i1i , iiI111I1iIiI in O00O0oOO00O00 :
  oOIIiIi ( '[COLORgreen]' + iiI111I1iIiI + '[/COLOR]' , url , 1006 , i1i )
def OOO00ii1Ii111I11I ( url ) :
 Ooo0O0oooo = iiI ( url )
 OOOOO0 = url
 O00O0oOO00O00 = re . compile ( "<a href='(.+?)'>(.+?)</a>" ) . findall ( Ooo0O0oooo )
 for url , iiI111I1iIiI in O00O0oOO00O00 :
  if '.mp3' in iiI111I1iIiI :
   print '<<<<<<<<<<<<<<<<<<<' + url + '>>>>>>>>>>>>>>>>>>>>>>>>>>>'
   oOOO00o000o ( ( iiI111I1iIiI ) . replace ( '.mp3' , '' ) . replace ( '/' , '' ) , 'http://hypem.com' + url , 222 , oOOoO0 + 'music.png' )
  else :
   oOIIiIi ( ( iiI111I1iIiI ) . replace ( '/' , '' ) , OOOOO0 + url , 1011 , oOOoO0 + 'music.png' )
def o0OoOoo ( ) :
 Ooo0O0oooo = iiI ( oOo0oooo00o ( 'aHR0cDovL3d3dy5jeW4ubmV0L211c2ljLw==' ) )
 O00O0oOO00O00 = re . compile ( '<td><a href="(.+?)"><img src="(.+?)"><br>(.+?)</a></td>' , re . DOTALL ) . findall ( Ooo0O0oooo )
 for i1Oo00 , i1i , iiI111I1iIiI in O00O0oOO00O00 :
  oOIIiIi ( iiI111I1iIiI , ( 'http://www.cyn.net/music/' + i1Oo00 ) . replace ( ' ' , '%20' ) , 1031 , ( 'http://www.cyn.net/music/' + i1i ) . replace ( ' ' , '%20' ) )
def O0OoO0o0Oooo ( url , img ) :
 Ooo0O0oooo = iiI ( url )
 i1iIi = url
 img = img
 O00O0oOO00O00 = re . compile ( '<a href="(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( Ooo0O0oooo )
 for url , iiI111I1iIiI in O00O0oOO00O00 :
  oOOO00o000o ( ( iiI111I1iIiI ) . replace ( '.mp3' , '' ) , ( i1iIi + '/' + url ) . replace ( ' ' , '%20' ) , 222 , img )
  if 61 - 61: OoOoOO00 . O0 - o00O0oo - ii11ii1ii / i11iIiiIii - OoOoOO00
  if 98 - 98: o00O0oo - OOOo0 . i11iIiiIii * Oo
def i111 ( ) :
 I1I1i = ( oOo0oooo00o ( 'aHR0cDovL2h5cGVtLmNvbS9kb3dubG9hZC8=' ) )
 Oo0oOOo = Oo0o0000o0o0 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OOO00O = Oo0oOOo . lower ( )
 i1Oo00 = ( oOo0oooo00o ( 'aHR0cDovL3Bhbmljc3RyZWFtLm5ldC9zdHJlYW1zLw==' ) )
 i1iIi = ( oOo0oooo00o ( 'aHR0cDovL21hc2xvdmQubm8taXAub3JnL3B1YmxpYy9tcDMv' ) )
 O0O0oo = ( oOo0oooo00o ( 'aHR0cDovL3d3dy5jeW4ubmV0L211c2ljLw==' ) )
 if 71 - 71: Ooo00oOo00o
 OOoOO0oo0ooO = Oo0oO00 ( i1Oo00 )
 I1i111IiIiIi1 = Oo0oO00 ( i1iIi )
 oo000o = Oo0oO00 ( O0O0oo )
 if 75 - 75: oO0o0ooO0
 if OOoOO0oo0ooO != 'Failed' :
  O00O0oOO00O00 = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( OOoOO0oo0ooO )
  for iiI111I1iIiI in O00O0oOO00O00 :
   if Oo0oOOo in iiI111I1iIiI . lower ( ) :
    oOIIiIi ( ( iiI111I1iIiI + ' source 1' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( i1Oo00 + iiI111I1iIiI ) . replace ( ' ' , '%20' ) , 1006 , '' )
    if 16 - 16: ii11ii1ii + OoOoOO00 * I1IiI . IIII
    Oooo0Ooo000 ( 'tvshows' , 'Media Info 3' )
 if I1i111IiIiIi1 != 'Failed' :
  OOo0 = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( OOoOO0oo0ooO )
  for iiI111I1iIiI in OOo0 :
   if Oo0oOOo in iiI111I1iIiI . lower ( ) :
    oOIIiIi ( ( iiI111I1iIiI + ' source 2' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( i1iIi + iiI111I1iIiI ) . replace ( ' ' , '%20' ) , 1006 , '' )
    if 10 - 10: oO0o0ooO0 * o00O0oo - o0oO0 . o0000oOoOoO0o - OoOO0ooOOoo0O
    Oooo0Ooo000 ( 'tvshows' , 'Media Info 3' )
 if oo000o != 'Failed' :
  ooOooo000OO00 = re . compile ( '<td><a href=".+?"><img src=".+?"><br>(.+?)</a></td>' , re . DOTALL ) . findall ( oo000o )
  for iiI111I1iIiI in ooOooo000OO00 :
   if Oo0oOOo in iiI111I1iIiI . lower ( ) :
    oOIIiIi ( ( iiI111I1iIiI + ' source 3' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( O0O0oo + iiI111I1iIiI ) . replace ( ' ' , '%20' ) , 1031 , '' )
    if 94 - 94: OOOo0 % IIII + Ooo00oOo00o
    Oooo0Ooo000 ( 'tvshows' , 'Media Info 3' )
    if 90 - 90: i1IIi + O0 - OoOO . oO0o0ooO0 + iIii1I11I1II1
    if 88 - 88: o00O0oo * O0 . O0oO / OoooooooOO
    if 29 - 29: OoooooooOO . OoOoOO00 % I1IiI
    if 26 - 26: iIii1I11I1II1 - ii11ii1ii . IIII . IIII + iIii1I11I1II1 * Oo
    if 85 - 85: OoOO0ooOOoo0O + OoOoOO00 - OoOO0ooOOoo0O * OoOO - i1IIi % oO0o0ooO0
    if 1 - 1: OoooooooOO / O0 + I1IiI + I1IiI . O0oO - I1IiI
def I11iii1I1Iiii ( ) :
 Ooo0O0oooo = O0o0O00Oo0o0 ( 'http://www.animetoon.org/cartoon' )
 O00O0oOO00O00 = re . compile ( '<td><a href="(.+?)">(.+)</a></td>' ) . findall ( Ooo0O0oooo )
 for i1Oo00 , iiI111I1iIiI in O00O0oOO00O00 :
  oOIIiIi ( iiI111I1iIiI , i1Oo00 , 1002 , oOOoO0 + 'anime.png' )
  if 47 - 47: i11iIiiIii / Oo - Oo * Ooo00oOo00o
  if 48 - 48: IIII
  if 96 - 96: OoOO / O0 . OoOoOO00 + IIII % OOooOOo
def oo0O0oOOO0o ( url ) :
 Ooo0O0oooo = O0o0O00Oo0o0 ( url )
 OOo0 = re . compile ( '<img src="(.+?)" id="series_image" width="250" height="370" alt=".+?" />' ) . findall ( Ooo0O0oooo )
 for i1i in OOo0 :
  i11iIIi11 = i1i
 ooOooo000OO00 = re . compile ( '<li><a href="(.+?)">Next</a></li>' ) . findall ( Ooo0O0oooo )
 for url in ooOooo000OO00 :
  oOIIiIi ( 'NEXT PAGE' , url , 1002 , i11iIIi11 )
 O00O0oOO00O00 = re . compile ( '&nbsp;<a href="(.+?)">(.+?)</a>' ) . findall ( Ooo0O0oooo )
 for url , iiI111I1iIiI in O00O0oOO00O00 :
  oOIIiIi ( iiI111I1iIiI , url , 1003 , i11iIIi11 )
 xbmcplugin . addSortMethod ( o0 , xbmcplugin . SORT_METHOD_TITLE ) ;
def oOo0Oo0Oo0 ( url , IMAGE ) :
 Ooo0O0oooo = O0o0O00Oo0o0 ( url )
 O00O0oOO00O00 = re . compile ( '"playlist">(.+?)</span></div><div><iframe src="(.+?)"' ) . findall ( Ooo0O0oooo )
 for iiI111I1iIiI , url in O00O0oOO00O00 :
  print iiI111I1iIiI + '     ' + url
  if 'easy' in url :
   OooOo0o0OO ( url )
  elif 'playpanda' in url :
   OooOo0o0OO ( url )
   if 1 - 1: iIii1I11I1II1 % o0oO0 + O0
  xbmcplugin . addSortMethod ( o0 , xbmcplugin . SORT_METHOD_TITLE ) ;
def OooOo0o0OO ( url ) :
 Ooo0O0oooo = O0o0O00Oo0o0 ( url )
 O00O0oOO00O00 = re . compile ( "url: '(.+?)'," ) . findall ( Ooo0O0oooo )
 for url in O00O0oOO00O00 :
  oOOO00o000o ( 'STREAM' , url , 222 , oOOoO0 + 'anime.png' )
  if 22 - 22: OOooOOo + Oo . o0oO0 + ii11ii1ii * oO0o0ooO0 . i11iIiiIii
  if 90 - 90: OoOO0ooOOoo0O * I1IiI - Oo + OOooOOo
def OoOII11IiI1 ( url ) :
 ii11ii11I = urllib2 . Request ( url )
 ii11ii11I . add_header ( 'User-Agent' , "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0" )
 ii11ii11I . add_header ( 'referer' , url )
 Oo0oo0oOO0oOo = urllib2 . urlopen ( ii11ii11I )
 o0ooooO0o0O = Oo0oo0oOO0oOo . read ( )
 Oo0oo0oOO0oOo . close ( )
 return o0ooooO0o0O
 if 86 - 86: iIii1I11I1II1 % OoOO - I1IiI + O0oO % Ooo00oOo00o . ii11ii1ii
def iiI ( url ) :
 ii11ii11I = urllib2 . Request ( url )
 ii11ii11I . add_header ( 'User-Agent' , "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0" )
 Oo0oo0oOO0oOo = urllib2 . urlopen ( ii11ii11I )
 o0ooooO0o0O = Oo0oo0oOO0oOo . read ( )
 Oo0oo0oOO0oOo . close ( )
 return o0ooooO0o0O
 if 4 - 4: i1IIi + I1IiI
def ii11I11 ( url ) :
 xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
 Oo0ooo0Ooo = ( '%s%s' % ( i1II1I , url ) )
 o0ooooO0o0O = iiI ( url )
 O00O0oOO00O00 = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( o0ooooO0o0O )
 for url , oooooOoo0ooo , iiI111I1iIiI in O00O0oOO00O00 :
  oOOO00o000o ( '%s' % ( iiI111I1iIiI ) . replace ( 'GenieTv' , '[COLOR green]GenieTV[/COLOR]' ) . replace ( '.' , ' ' ) . replace ( 'mp4' , '' ) . replace ( 'mkv' , '' ) . replace ( '_' , ' ' ) , '%s' % ( url ) , 222 , oooooOoo0ooo )
  if 75 - 75: Oo
def iIIIiIi1i ( url ) :
 oOOo000oOoO0 = xbmc . Player ( Ii1Ii1I ( ) )
 import urlresolver
 try : oOOo000oOoO0 . play ( url )
 except : pass
 from urlresolver import common
 i1111 = xbmcgui . DialogProgress ( )
 i1111 . create ( 'LOADING' , 'Opening %s Now' % ( iiI111I1iIiI ) )
 oOOo000oOoO0 = xbmc . Player ( Ii1Ii1I ( ) )
 url = urlresolver . HostedMediaFile ( url ) . resolve ( )
 if i1111 . iscanceled ( ) :
  print "[COLORred]STREAM CANCELLED[/COLOR]"
  ii11iIi1I = xbmcgui . Dialog ( )
  if ii11iIi1I . yesno ( "[B]CANCELLED[/B]" , '[B]Was There A Problem[/B]' , '' , "" , 'Yes' , 'No' ) :
   ii11iIi1I . ok ( "Message Send" , "Your Message Has Been Sent" )
  else :
   return
 else :
  try : oOOo000oOoO0 . play ( url )
  except : pass
  try : o0oOoO00o . resolve_url ( url )
  except : pass
  i1111 . close ( )
  if 23 - 23: OoOoOO00 * oO0o0ooO0
def o00oO00 ( url ) :
 oOOo000oOoO0 = xbmc . Player ( Ii1Ii1I ( ) )
 import urlresolver
 try : oOOo000oOoO0 . play ( url )
 except : pass
 if 80 - 80: O0oO / i11iIiiIii + OoooooooOO
 if 38 - 38: ii11ii1ii % o0oO0 + i1IIi * OoooooooOO * OoOO
def Ii1Ii1I ( ) :
 try :
  OoO0o0OO = getSet ( "core-player" )
  if ( OoO0o0OO == 'DVDPLAYER' ) : II11IiI1 = xbmc . PLAYER_CORE_DVDPLAYER
  elif ( OoO0o0OO == 'MPLAYER' ) : II11IiI1 = xbmc . PLAYER_CORE_MPLAYER
  elif ( OoO0o0OO == 'PAPLAYER' ) : II11IiI1 = xbmc . PLAYER_CORE_PAPLAYER
  else : II11IiI1 = xbmc . PLAYER_CORE_AUTO
 except : II11IiI1 = xbmc . PLAYER_CORE_AUTO
 return II11IiI1
 return True
 if 21 - 21: Ooo00oOo00o
def oOIIiIi ( name , url , mode , iconimage , showcontext = True , allinfo = { } ) :
 O00ooOo = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 oOO0o00O = True
 oOoO = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 oOoO . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 if showcontext :
  O0o0oOOO = [ ]
  if showcontext == 'fav' :
   O0o0oOOO . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in oOoOooOo0o0 :
   O0o0oOOO . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  oOoO . addContextMenuItems ( O0o0oOOO )
 oOO0o00O = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = O00ooOo , listitem = oOoO , isFolder = True )
 return oOO0o00O
 if 24 - 24: OOooOOo / o00O0oo / o00O0oo % OoOoOO00 - OoOO * OoOO
def III1i11 ( name , url , mode , iconimage , fanart , description ) :
 if 58 - 58: I1IiI
 O00ooOo = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 oOO0o00O = True
 oOoO = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 oOoO . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 oOoO . setProperty ( "Fanart_Image" , fanart )
 oOO0o00O = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = O00ooOo , listitem = oOoO , isFolder = True )
 return oOO0o00O
 if 60 - 60: OoOoOO00
def oOOO00o000o ( name , url , mode , iconimage , showcontext = True , allinfo = { } ) :
 O00ooOo = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 oOO0o00O = True
 oOoO = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 oOoO . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 if showcontext :
  O0o0oOOO = [ ]
  if showcontext == 'fav' :
   O0o0oOOO . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in oOoOooOo0o0 :
   O0o0oOOO . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  oOoO . addContextMenuItems ( O0o0oOOO )
 oOO0o00O = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = O00ooOo , listitem = oOoO , isFolder = False )
 return oOO0o00O
 if 90 - 90: I1IiI
 if 37 - 37: I1IiI + O0 . O0 * Oo % O0oO / oO0o0ooO0
 if 18 - 18: OoooooooOO
 if 57 - 57: o0oO0 . I1IiI * OOooOOo - OoooooooOO
 if 75 - 75: i11iIiiIii / OOooOOo . IIII . i1IIi . i1IIi / o0000oOoOoO0o
 if 94 - 94: o0oO0 + OOOo0
def ooO0o0 ( heading , announce ) :
 class oOOOoo00oO ( ) :
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
   try : oOooOOOoOo = open ( announce ) ; O00O0 = oOooOOOoOo . read ( )
   except : O00O0 = announce
   self . win . getControl ( self . CONTROL_TEXTBOX ) . setText ( str ( O00O0 ) )
   return
 oOOOoo00oO ( )
 oOOOoo00oO ( )
 if 43 - 43: OoOO % Ooo00oOo00o - Oo - O0 - OoooooooOO
def Ii1I1Iiii ( ) :
 ooO0o0 ( 'These are the main Sources you should get into you XBMC' , '[COLORwhite]http://architects.x10host.com[/COLOR]--- [CR]  [COLORred]http://repo.sharktech.co.uk[/COLOR]--- [CR]   [COLORwhite]http://fusion.tvaddons.ag[/COLOR]--- [CR]  [COLORred]http://i.totalxbmc.tv[/COLOR]--- [CR]   [COLORwhite]http://www.xunitytalk.com/xfinity[/COLOR]--- [CR]  [COLORred]http://srp.nu[/COLOR]--- [CR]   [COLORwhite]http://solved.no-issue.ca[/COLOR]--- [CR]  [COLORred]http://xbmc.aminhacasadigital.com[/COLOR]--- [CR]   [COLORwhite]http://xbmc.movieshd.co[/COLOR]--- [CR]  [COLORred]http://install.kaosbox.tv[/COLOR]--- [CR]   [COLORwhite]http://kodi-repo.com/mxr[/COLOR]--- [CR]  [COLORred]http://kodi.metalkettle.co[/COLOR]--- [CR]   [COLORwhite]http://prozone.getxbmc.com[/COLOR]--- [CR]  [COLORred]http://transform.mega-tron.tv[/COLOR]--- [CR]   [COLORwhite]http://muckys.kodimediaportal.ml[/COLOR]--- [CR]  [COLORred]http://jas0npc.pcriot.com[/COLOR]--- [CR]  [COLORwhite]Sports devil source[/COLOR]--- [CR]  [COLORred]http://iwillfolo.com/iwf[/COLOR]' )
 if 80 - 80: OoOO0ooOOoo0O . o00O0oo + iIii1I11I1II1
 if 32 - 32: OOOo0
 if 47 - 47: ii11ii1ii * OoOO + iIii1I11I1II1 - OoOO / IIII
 if 86 - 86: IIII
 if 43 - 43: OOOo0 / oO0o0ooO0 / o0oO0 + iIii1I11I1II1 + OoooooooOO
def Oo0 ( ) :
 xbmc . executebuiltin ( 'UpdateLocalAddons' )
 xbmc . executebuiltin ( 'UpdateAddonRepos' )
 ii11iIi1I = xbmcgui . Dialog ( )
 ii11iIi1I . ok ( "GenieTv" , '' , '                                 REFRESH SUCCESSFUL :)' , "                          [COLOR gold]Brought To You By Kodi Support Group, GenieTv[/COLOR]" )
 return
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
 if 4 - 4: iIii1I11I1II1 . i1IIi
 if 63 - 63: iIii1I11I1II1 + IIII % i1IIi / OOOo0 % OoOoOO00
 if 60 - 60: OOooOOo . I1IiI % O0oO / OOOo0 / O0
 if 19 - 19: i11iIiiIii . OOOo0 + OoOoOO00 / OoOO0ooOOoo0O . ii11ii1ii * o0oO0
def oo0O ( url ) :
 o0ooooO0o0O = O0o0O00Oo0o0 ( OO0o + Ooooo0O0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 O00O0oOO00O00 = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( o0ooooO0o0O )
 for iiI111I1iIiI , url , oo000 , o0000oO , O0ii1ii1ii in O00O0oOO00O00 :
  iiiiiIIii ( iiI111I1iIiI , url , 42 , oo000 , o0000oO , O0ii1ii1ii )
 Oooo0Ooo000 ( 'movies' , 'MAIN' )
 if 99 - 99: Oo + i11iIiiIii
def I111Ii11i11I ( url ) :
 o0ooooO0o0O = O0o0O00Oo0o0 ( OO0o + i11I ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 O00O0oOO00O00 = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( o0ooooO0o0O )
 for iiI111I1iIiI , url , oo000 , o0000oO , O0ii1ii1ii in O00O0oOO00O00 :
  iiiiiIIii ( iiI111I1iIiI , url , 42 , oo000 , o0000oO , O0ii1ii1ii )
 Oooo0Ooo000 ( 'movies' , 'MAIN' )
 if 75 - 75: OoOO * o0oO0
def OO0Oo00OO0oo ( url ) :
 o0ooooO0o0O = O0o0O00Oo0o0 ( OO0o + oOO00o0O0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 O00O0oOO00O00 = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( o0ooooO0o0O )
 for iiI111I1iIiI , url , oo000 , o0000oO , O0ii1ii1ii in O00O0oOO00O00 :
  iiiiiIIii ( iiI111I1iIiI , url , 42 , oo000 , o0000oO , O0ii1ii1ii )
 Oooo0Ooo000 ( 'movies' , 'MAIN' )
 if 47 - 47: o0oO0
def Oo0oo ( url ) :
 o0ooooO0o0O = O0o0O00Oo0o0 ( OO0o + IiIi ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 O00O0oOO00O00 = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( o0ooooO0o0O )
 for iiI111I1iIiI , url , oo000 , o0000oO , O0ii1ii1ii in O00O0oOO00O00 :
  iiiiiIIii ( iiI111I1iIiI , url , 42 , oo000 , o0000oO , O0ii1ii1ii )
 Oooo0Ooo000 ( 'movies' , 'MAIN' )
 if 36 - 36: OoOO0ooOOoo0O * o00O0oo
def i1iIii1II1i ( url ) :
 o0ooooO0o0O = O0o0O00Oo0o0 ( OO0o + iI1iIoOo ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 O00O0oOO00O00 = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( o0ooooO0o0O )
 for iiI111I1iIiI , url , oo000 , o0000oO , O0ii1ii1ii in O00O0oOO00O00 :
  iiiiiIIii ( iiI111I1iIiI , url , 42 , oo000 , o0000oO , O0ii1ii1ii )
 Oooo0Ooo000 ( 'movies' , 'MAIN' )
 if 9 - 9: OOooOOo - IIII + iIii1I11I1II1 + Ooo00oOo00o
def IIIIIiI1I1 ( url ) :
 o0ooooO0o0O = O0o0O00Oo0o0 ( OO0o + oOoOoOOo00Ooo0O ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 O00O0oOO00O00 = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( o0ooooO0o0O )
 for iiI111I1iIiI , url , oo000 , o0000oO , O0ii1ii1ii in O00O0oOO00O00 :
  iiiiiIIii ( iiI111I1iIiI , url , 42 , oo000 , o0000oO , O0ii1ii1ii )
 Oooo0Ooo000 ( 'movies' , 'MAIN' )
 if 34 - 34: OoOoOO00
def i1Oo ( url ) :
 o0ooooO0o0O = O0o0O00Oo0o0 ( OO0o + Ii11ii1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 O00O0oOO00O00 = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( o0ooooO0o0O )
 for iiI111I1iIiI , url , oo000 , o0000oO , O0ii1ii1ii in O00O0oOO00O00 :
  iiiiiIIii ( iiI111I1iIiI , url , 42 , oo000 , o0000oO , O0ii1ii1ii )
 Oooo0Ooo000 ( 'movies' , 'MAIN' )
 if 1 - 1: iIii1I11I1II1 % OoOO . iIii1I11I1II1
def i1IiiI1 ( url ) :
 o0ooooO0o0O = O0o0O00Oo0o0 ( OO0o + O000OOOo ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 O00O0oOO00O00 = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( o0ooooO0o0O )
 for iiI111I1iIiI , url , oo000 , o0000oO , O0ii1ii1ii in O00O0oOO00O00 :
  iiiiiIIii ( iiI111I1iIiI , url , 42 , oo000 , o0000oO , O0ii1ii1ii )
 Oooo0Ooo000 ( 'movies' , 'MAIN' )
 if 82 - 82: o0000oOoOoO0o / I1IiI - OoOO0ooOOoo0O / o0oO0
def I1iIIi ( url ) :
 o0ooooO0o0O = O0o0O00Oo0o0 ( OO0o + IiOo00O0o0O ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 O00O0oOO00O00 = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( o0ooooO0o0O )
 for iiI111I1iIiI , url , oo000 , o0000oO , O0ii1ii1ii in O00O0oOO00O00 :
  iiiiiIIii ( iiI111I1iIiI , url , 42 , oo000 , o0000oO , O0ii1ii1ii )
 Oooo0Ooo000 ( 'movies' , 'MAIN' )
 if 86 - 86: o0000oOoOoO0o + O0 + Oo - o0000oOoOoO0o
def Ii1iI1IIIII ( url ) :
 o0ooooO0o0O = O0o0O00Oo0o0 ( OO0o + Ooo0OOOo ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 O00O0oOO00O00 = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( o0ooooO0o0O )
 for iiI111I1iIiI , url , oo000 , o0000oO , O0ii1ii1ii in O00O0oOO00O00 :
  iiiiiIIii ( iiI111I1iIiI , url , 5 , oo000 , o0000oO , O0ii1ii1ii )
 Oooo0Ooo000 ( 'movies' , 'MAIN' )
 if 86 - 86: O0
 if 11 - 11: o00O0oo + oO0o0ooO0 * i1IIi % OoooooooOO * o00O0oo * Ooo00oOo00o
 if 7 - 7: oO0o0ooO0 . o00O0oo . oO0o0ooO0 - O0oO
 if 33 - 33: o0oO0 + OoooooooOO - Ooo00oOo00o / i1IIi / OoooooooOO
 if 82 - 82: ii11ii1ii / OoOO0ooOOoo0O - oO0o0ooO0 / Oo * Ooo00oOo00o
 if 55 - 55: OoooooooOO
 if 73 - 73: I1IiI - ii11ii1ii % Oo + ii11ii1ii - O0 . Ooo00oOo00o
 if 38 - 38: O0
 if 79 - 79: i1IIi . OoOO
def i1i1i11iI11II ( ) :
 try :
  if os . path . exists ( OooO0 ) == True :
   ii11iIi1I = xbmcgui . Dialog ( )
   if ii11iIi1I . yesno ( "Delete Thumbnails" , "[COLOR gold][B]##########WARNING ANDROID ONLY##########[/B][/COLOR]" , "This feature deletes your thumbnail folder and textures13.db" , "Are you sure you want to do proceed? This Can NOT Be Undone" ) :
    for oOO , iIiIi11 , OOOiiiiI in os . walk ( OooO0 ) :
     II1iiI1iI = 0
     II1iiI1iI += len ( OOOiiiiI )
     if II1iiI1iI > 0 :
      for oOooOOOoOo in OOOiiiiI :
       os . unlink ( os . path . join ( oOO , oOooOOOoOo ) )
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
  for oOO , iIiIi11 , OOOiiiiI in os . walk ( I1IiiiI ) :
   II1iiI1iI = 0
   II1iiI1iI += len ( OOOiiiiI )
   if 6 - 6: OOOo0 - i11iIiiIii
   if 61 - 61: O0oO * ii11ii1ii % OOOo0 % Ooo00oOo00o % o0000oOoOoO0o + o0000oOoOoO0o
   if II1iiI1iI > 0 :
    if 6 - 6: Oo
    ii11iIi1I = xbmcgui . Dialog ( )
    if ii11iIi1I . yesno ( "Delete KODI Cache Files" , str ( II1iiI1iI ) + " files found" , "Do you want to delete them?" ) :
     if 73 - 73: O0oO * ii11ii1ii + OOooOOo - Oo . o0000oOoOoO0o
     for oOooOOOoOo in OOOiiiiI :
      try :
       os . unlink ( os . path . join ( oOO , oOooOOOoOo ) )
      except :
       pass
     for OOoO in iIiIi11 :
      try :
       shutil . rmtree ( os . path . join ( oOO , OOoO ) )
      except :
       pass
       if 93 - 93: i11iIiiIii
   else :
    pass
 if xbmc . getCondVisibility ( 'system.platform.ATV2' ) :
  OoOiII11IiIi = os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'Other' )
  if 27 - 27: Ooo00oOo00o + I1IiI
  for oOO , iIiIi11 , OOOiiiiI in os . walk ( OoOiII11IiIi ) :
   II1iiI1iI = 0
   II1iiI1iI += len ( OOOiiiiI )
   if 97 - 97: i1IIi * O0oO . OoOoOO00
   if II1iiI1iI > 0 :
    if 62 - 62: OoooooooOO . o00O0oo
    ii11iIi1I = xbmcgui . Dialog ( )
    if ii11iIi1I . yesno ( "Delete ATV2 Cache Files" , str ( II1iiI1iI ) + " files found in 'Other'" , "Do you want to delete them?" ) :
     if 28 - 28: OoOO . OoOO . iIii1I11I1II1 . OoOO0ooOOoo0O . ii11ii1ii * i11iIiiIii
     for oOooOOOoOo in OOOiiiiI :
      os . unlink ( os . path . join ( oOO , oOooOOOoOo ) )
     for OOoO in iIiIi11 :
      shutil . rmtree ( os . path . join ( oOO , OOoO ) )
      if 72 - 72: o0000oOoOoO0o
   else :
    pass
  i1I1IIiIIi = os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'LocalAndRental' )
  if 33 - 33: Ooo00oOo00o % IIII - iIii1I11I1II1
  for oOO , iIiIi11 , OOOiiiiI in os . walk ( i1I1IIiIIi ) :
   II1iiI1iI = 0
   II1iiI1iI += len ( OOOiiiiI )
   if 33 - 33: Ooo00oOo00o + I1IiI - OoOO * i11iIiiIii . O0oO
   if II1iiI1iI > 0 :
    if 92 - 92: OoOO
    ii11iIi1I = xbmcgui . Dialog ( )
    if ii11iIi1I . yesno ( "Delete ATV2 Cache Files" , str ( II1iiI1iI ) + " files found in 'LocalAndRental'" , "Do you want to delete them?" ) :
     if 81 - 81: OOooOOo % OOOo0 - oO0o0ooO0 / i11iIiiIii
     for oOooOOOoOo in OOOiiiiI :
      os . unlink ( os . path . join ( oOO , oOooOOOoOo ) )
     for OOoO in iIiIi11 :
      shutil . rmtree ( os . path . join ( oOO , OOoO ) )
      if 73 - 73: O0 * O0oO . i1IIi
   else :
    pass
    if 51 - 51: Ooo00oOo00o - oO0o0ooO0 % O0 - I1IiI
    if 53 - 53: oO0o0ooO0 / i1IIi / i1IIi
    if 77 - 77: o0000oOoOoO0o + i1IIi . o0000oOoOoO0o
    if 89 - 89: OOooOOo + OoOO0ooOOoo0O * OoOO
 i1iI1IIi = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.whatthefurk/cache' ) , '' )
 if os . path . exists ( i1iI1IIi ) == True :
  for oOO , iIiIi11 , OOOiiiiI in os . walk ( i1iI1IIi ) :
   II1iiI1iI = 0
   II1iiI1iI += len ( OOOiiiiI )
   if 27 - 27: O0 / Ooo00oOo00o
   if 99 - 99: o00O0oo - IIII * iIii1I11I1II1 . OoOoOO00
   if II1iiI1iI > 0 :
    if 56 - 56: iIii1I11I1II1 % Ooo00oOo00o . o0oO0 % IIII . O0oO * Oo
    ii11iIi1I = xbmcgui . Dialog ( )
    if ii11iIi1I . yesno ( "Delete WTF Cache Files" , str ( II1iiI1iI ) + " files found" , "Do you want to delete them?" ) :
     if 41 - 41: iIii1I11I1II1 % IIII * OoOO - o0oO0
     for oOooOOOoOo in OOOiiiiI :
      os . unlink ( os . path . join ( oOO , oOooOOOoOo ) )
     for OOoO in iIiIi11 :
      shutil . rmtree ( os . path . join ( oOO , OOoO ) )
      if 5 - 5: Ooo00oOo00o + Ooo00oOo00o + OoOoOO00 * iIii1I11I1II1 + OoooooooOO
   else :
    pass
    if 77 - 77: O0 * ii11ii1ii * OoOO + Ooo00oOo00o + ii11ii1ii - O0oO
    if 10 - 10: ii11ii1ii + IIII
 Ooooo00 = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.4od/cache' ) , '' )
 if os . path . exists ( Ooooo00 ) == True :
  for oOO , iIiIi11 , OOOiiiiI in os . walk ( Ooooo00 ) :
   II1iiI1iI = 0
   II1iiI1iI += len ( OOOiiiiI )
   if 99 - 99: ii11ii1ii - OoOO
   if 10 - 10: OoOoOO00 . Ooo00oOo00o
   if II1iiI1iI > 0 :
    if 89 - 89: o0oO0 * o00O0oo
    ii11iIi1I = xbmcgui . Dialog ( )
    if ii11iIi1I . yesno ( "Delete 4oD Cache Files" , str ( II1iiI1iI ) + " files found" , "Do you want to delete them?" ) :
     if 93 - 93: i1IIi . o00O0oo * O0oO . o0oO0
     for oOooOOOoOo in OOOiiiiI :
      os . unlink ( os . path . join ( oOO , oOooOOOoOo ) )
     for OOoO in iIiIi11 :
      shutil . rmtree ( os . path . join ( oOO , OOoO ) )
      if 54 - 54: oO0o0ooO0 . i1IIi . ii11ii1ii * OOooOOo % oO0o0ooO0
   else :
    pass
    if 30 - 30: o0000oOoOoO0o
    if 85 - 85: OoOoOO00 + o0oO0 * o0000oOoOoO0o
 i1ooOO00o0 = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.iplayer/iplayer_http_cache' ) , '' )
 if os . path . exists ( i1ooOO00o0 ) == True :
  for oOO , iIiIi11 , OOOiiiiI in os . walk ( i1ooOO00o0 ) :
   II1iiI1iI = 0
   II1iiI1iI += len ( OOOiiiiI )
   if 44 - 44: OOOo0 % OoOO0ooOOoo0O * i11iIiiIii * i11iIiiIii - Oo . O0oO
   if 68 - 68: oO0o0ooO0 . o0000oOoOoO0o
   if II1iiI1iI > 0 :
    if 29 - 29: o0oO0 * IIII
    ii11iIi1I = xbmcgui . Dialog ( )
    if ii11iIi1I . yesno ( "Delete BBC iPlayer Cache Files" , str ( II1iiI1iI ) + " files found" , "Do you want to delete them?" ) :
     if 75 - 75: O0
     for oOooOOOoOo in OOOiiiiI :
      os . unlink ( os . path . join ( oOO , oOooOOOoOo ) )
     for OOoO in iIiIi11 :
      shutil . rmtree ( os . path . join ( oOO , OOoO ) )
      if 56 - 56: Ooo00oOo00o / OoOoOO00
   else :
    pass
    if 39 - 39: I1IiI - OoooooooOO - i1IIi / OoOoOO00
    if 49 - 49: Oo + O0 + IIII . OoOoOO00 % o0oO0
    if 33 - 33: I1IiI . iIii1I11I1II1 / o0000oOoOoO0o % o00O0oo
 IIiiI11 = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/script.module.simple.downloader' ) , '' )
 if os . path . exists ( IIiiI11 ) == True :
  for oOO , iIiIi11 , OOOiiiiI in os . walk ( IIiiI11 ) :
   II1iiI1iI = 0
   II1iiI1iI += len ( OOOiiiiI )
   if 7 - 7: OOOo0 / Ooo00oOo00o + O0oO + o0000oOoOoO0o / OOOo0
   if 82 - 82: ii11ii1ii + OoooooooOO
   if II1iiI1iI > 0 :
    if 21 - 21: OoOO * OoOO / o0000oOoOoO0o . oO0o0ooO0
    ii11iIi1I = xbmcgui . Dialog ( )
    if ii11iIi1I . yesno ( "Delete Simple Downloader Cache Files" , str ( II1iiI1iI ) + " files found" , "Do you want to delete them?" ) :
     if 10 - 10: o00O0oo * OoOO0ooOOoo0O - Oo - OoooooooOO / OOooOOo
     for oOooOOOoOo in OOOiiiiI :
      os . unlink ( os . path . join ( oOO , oOooOOOoOo ) )
     for OOoO in iIiIi11 :
      shutil . rmtree ( os . path . join ( oOO , OOoO ) )
      if 86 - 86: O0oO % OOOo0
   else :
    pass
    if 22 - 22: i11iIiiIii * O0oO . Oo . OoooooooOO + OOOo0
    if 24 - 24: OoOoOO00 / o00O0oo . iIii1I11I1II1 - OoOoOO00 % O0
 IIi1Ii11iIi = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.itv/Images' ) , '' )
 if os . path . exists ( IIi1Ii11iIi ) == True :
  for oOO , iIiIi11 , OOOiiiiI in os . walk ( IIi1Ii11iIi ) :
   II1iiI1iI = 0
   II1iiI1iI += len ( OOOiiiiI )
   if 33 - 33: OoOoOO00 . OoOoOO00 / I1IiI - OoOoOO00
   if 10 - 10: I1IiI - OOooOOo * i11iIiiIii / Oo + OOooOOo + iIii1I11I1II1
   if II1iiI1iI > 0 :
    if 23 - 23: i1IIi + ii11ii1ii + OOOo0 - o0oO0 % OoooooooOO . IIII
    ii11iIi1I = xbmcgui . Dialog ( )
    if ii11iIi1I . yesno ( "Delete ITV Cache Files" , str ( II1iiI1iI ) + " files found" , "Do you want to delete them?" ) :
     if 49 - 49: OoOO . I1IiI
     for oOooOOOoOo in OOOiiiiI :
      os . unlink ( os . path . join ( oOO , oOooOOOoOo ) )
     for OOoO in iIiIi11 :
      shutil . rmtree ( os . path . join ( oOO , OOoO ) )
      if 73 - 73: o00O0oo / OOOo0 / OoooooooOO + OOOo0
   else :
    pass
    if 57 - 57: OoOO0ooOOoo0O . o00O0oo % OOooOOo
    if 32 - 32: o0000oOoOoO0o / IIII - O0 * iIii1I11I1II1
 oo0oO0oOo0O = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.movies4me/cache' ) , '' )
 if os . path . exists ( IIi1Ii11iIi ) == True :
  for oOO , iIiIi11 , OOOiiiiI in os . walk ( oo0oO0oOo0O ) :
   II1iiI1iI = 0
   II1iiI1iI += len ( OOOiiiiI )
   if 75 - 75: OoOoOO00 + OoOoOO00 + OoOO0ooOOoo0O * OOooOOo
   if 62 - 62: iIii1I11I1II1 - i1IIi - OoOO
   if II1iiI1iI > 0 :
    if 72 - 72: I1IiI / O0oO * IIII % iIii1I11I1II1
    ii11iIi1I = xbmcgui . Dialog ( )
    if ii11iIi1I . yesno ( "Delete Movies4me Cache Files" , str ( II1iiI1iI ) + " files found" , "Do you want to delete them?" ) :
     if 53 - 53: Ooo00oOo00o . O0 . OOOo0 * OoOO0ooOOoo0O / OOooOOo
     for oOooOOOoOo in OOOiiiiI :
      os . unlink ( os . path . join ( oOO , oOooOOOoOo ) )
     for OOoO in iIiIi11 :
      shutil . rmtree ( os . path . join ( oOO , OOoO ) )
      if 34 - 34: I1IiI
   else :
    pass
    if 16 - 16: i1IIi - O0oO - OoOoOO00
    if 83 - 83: OOOo0 - Ooo00oOo00o - OOooOOo / O0 - o0000oOoOoO0o . OoOoOO00
 iI1i1Ii111I = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.phstreams/Cache' ) , '' )
 if os . path . exists ( IIi1Ii11iIi ) == True :
  for oOO , iIiIi11 , OOOiiiiI in os . walk ( iI1i1Ii111I ) :
   II1iiI1iI = 0
   II1iiI1iI += len ( OOOiiiiI )
   if 17 - 17: O0 * iIii1I11I1II1 % IIII . IIII / O0
   if 52 - 52: OOOo0 - iIii1I11I1II1 - ii11ii1ii
   if II1iiI1iI > 0 :
    if 38 - 38: OOOo0 + OOooOOo - IIII
    ii11iIi1I = xbmcgui . Dialog ( )
    if ii11iIi1I . yesno ( "Delete Phoenix Cache Files" , str ( II1iiI1iI ) + " files found" , "Do you want to delete them?" ) :
     if 85 - 85: oO0o0ooO0 * oO0o0ooO0 % I1IiI - OoOO0ooOOoo0O % Ooo00oOo00o - OOOo0
     for oOooOOOoOo in OOOiiiiI :
      os . unlink ( os . path . join ( oOO , oOooOOOoOo ) )
     for OOoO in iIiIi11 :
      shutil . rmtree ( os . path . join ( oOO , OOoO ) )
      if 3 - 3: OoOO0ooOOoo0O + i1IIi % ii11ii1ii
   else :
    pass
    if 100 - 100: OoooooooOO + i11iIiiIii % OOooOOo + OOOo0 . Oo . OoOoOO00
    if 93 - 93: OoOoOO00 . i11iIiiIii + OoOoOO00 % OoOO
 O00OOO000oo0 = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.spotitube/cache' ) , '' )
 if os . path . exists ( IIi1Ii11iIi ) == True :
  for oOO , iIiIi11 , OOOiiiiI in os . walk ( O00OOO000oo0 ) :
   II1iiI1iI = 0
   II1iiI1iI += len ( OOOiiiiI )
   if 16 - 16: iIii1I11I1II1 * oO0o0ooO0 + OoOO . O0 . OOooOOo
   if 99 - 99: i11iIiiIii - oO0o0ooO0
   if II1iiI1iI > 0 :
    if 85 - 85: O0oO % ii11ii1ii
    ii11iIi1I = xbmcgui . Dialog ( )
    if ii11iIi1I . yesno ( "Delete YouTube Music Cache Files" , str ( II1iiI1iI ) + " files found" , "Do you want to delete them?" ) :
     if 95 - 95: Ooo00oOo00o * OoOO0ooOOoo0O * oO0o0ooO0 . OOooOOo
     for oOooOOOoOo in OOOiiiiI :
      os . unlink ( os . path . join ( oOO , oOooOOOoOo ) )
     for OOoO in iIiIi11 :
      shutil . rmtree ( os . path . join ( oOO , OOoO ) )
      if 73 - 73: Ooo00oOo00o
   else :
    pass
    if 28 - 28: OoooooooOO - o0000oOoOoO0o
    if 84 - 84: OoOoOO00
 i1IIii1i = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.supercartoons/cache' ) , '' )
 if os . path . exists ( IIi1Ii11iIi ) == True :
  for oOO , iIiIi11 , OOOiiiiI in os . walk ( i1IIii1i ) :
   II1iiI1iI = 0
   II1iiI1iI += len ( OOOiiiiI )
   if 60 - 60: o00O0oo % Oo / o0000oOoOoO0o . oO0o0ooO0 / O0oO - OoooooooOO
   if 76 - 76: O0
   if II1iiI1iI > 0 :
    if 71 - 71: OOOo0 . i1IIi
    ii11iIi1I = xbmcgui . Dialog ( )
    if ii11iIi1I . yesno ( "Delete SuperCartoons Cache Files" , str ( II1iiI1iI ) + " files found" , "Do you want to delete them?" ) :
     if 19 - 19: OoOoOO00 / OoOoOO00 % ii11ii1ii + OoOO + OoOO + oO0o0ooO0
     for oOooOOOoOo in OOOiiiiI :
      os . unlink ( os . path . join ( oOO , oOooOOOoOo ) )
     for OOoO in iIiIi11 :
      shutil . rmtree ( os . path . join ( oOO , OOoO ) )
      if 4 - 4: OOooOOo + o0000oOoOoO0o / oO0o0ooO0 + i1IIi % OOooOOo % oO0o0ooO0
   else :
    pass
    if 80 - 80: o00O0oo
    if 26 - 26: iIii1I11I1II1 . OoooooooOO - iIii1I11I1II1
 oOo0O0 = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.tvonline.cc/cache' ) , '' )
 if os . path . exists ( IIi1Ii11iIi ) == True :
  for oOO , iIiIi11 , OOOiiiiI in os . walk ( oOo0O0 ) :
   II1iiI1iI = 0
   II1iiI1iI += len ( OOOiiiiI )
   if 1 - 1: OoOO + O0oO . OOOo0
   if 47 - 47: oO0o0ooO0 . I1IiI
   if II1iiI1iI > 0 :
    if 58 - 58: oO0o0ooO0 + Oo / OOOo0
    ii11iIi1I = xbmcgui . Dialog ( )
    if ii11iIi1I . yesno ( "Delete TVonline Cache Files" , str ( II1iiI1iI ) + " files found" , "Do you want to delete them?" ) :
     if 68 - 68: IIII * o00O0oo
     for oOooOOOoOo in OOOiiiiI :
      os . unlink ( os . path . join ( oOO , oOooOOOoOo ) )
     for OOoO in iIiIi11 :
      shutil . rmtree ( os . path . join ( oOO , OOoO ) )
      if 91 - 91: o00O0oo + Ooo00oOo00o * OOooOOo . O0oO
   else :
    pass
    if 89 - 89: OoooooooOO * o00O0oo * OOOo0 . o0oO0 * o00O0oo / oO0o0ooO0
    if 46 - 46: i11iIiiIii
 Iiiii = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.youtube/kodion' ) , '' )
 if os . path . exists ( IIi1Ii11iIi ) == True :
  for oOO , iIiIi11 , OOOiiiiI in os . walk ( Iiiii ) :
   II1iiI1iI = 0
   II1iiI1iI += len ( OOOiiiiI )
   if 25 - 25: Oo * OOOo0 + OoOO0ooOOoo0O + O0oO % OoOO0ooOOoo0O
   if 84 - 84: O0 % o00O0oo . o00O0oo . oO0o0ooO0 * o0000oOoOoO0o
   if II1iiI1iI > 0 :
    if 43 - 43: I1IiI . ii11ii1ii % i1IIi
    ii11iIi1I = xbmcgui . Dialog ( )
    if ii11iIi1I . yesno ( "Delete YouTube Cache Files" , str ( II1iiI1iI ) + " files found" , "Do you want to delete them?" ) :
     if 61 - 61: OOOo0 + OoOO % O0oO % iIii1I11I1II1 - OoooooooOO
     for oOooOOOoOo in OOOiiiiI :
      os . unlink ( os . path . join ( oOO , oOooOOOoOo ) )
     for OOoO in iIiIi11 :
      shutil . rmtree ( os . path . join ( oOO , OOoO ) )
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
  for oOO , iIiIi11 , OOOiiiiI in os . walk ( iI1ii ) :
   II1iiI1iI = 0
   II1iiI1iI += len ( OOOiiiiI )
   if 2 - 2: OoOoOO00 . o0000oOoOoO0o
   if 83 - 83: OOOo0 - O0oO + OOOo0 . OOOo0
   if II1iiI1iI > 0 :
    if 45 - 45: i1IIi % OoOO0ooOOoo0O % OoOoOO00
    ii11iIi1I = xbmcgui . Dialog ( )
    if ii11iIi1I . yesno ( "Delete Package Cache Files" , str ( II1iiI1iI ) + " files found" , "Do you want to delete them?" ) :
     if 4 - 4: OoOO * OOOo0 - o0oO0 / OoOoOO00 + OoOO0ooOOoo0O / i11iIiiIii
     for oOooOOOoOo in OOOiiiiI :
      os . unlink ( os . path . join ( oOO , oOooOOOoOo ) )
     for OOoO in iIiIi11 :
      shutil . rmtree ( os . path . join ( oOO , OOoO ) )
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
  for oOO , iIiIi11 , OOOiiiiI in os . walk ( iI1ii ) :
   II1iiI1iI = 0
   II1iiI1iI += len ( OOOiiiiI )
   if 94 - 94: OoOoOO00 / i1IIi * i1IIi + o0oO0 - o0oO0 % OOooOOo
   if 12 - 12: O0oO / I1IiI . i11iIiiIii * i11iIiiIii
   if II1iiI1iI > 0 :
    if 68 - 68: IIII * Ooo00oOo00o . o0000oOoOoO0o / o00O0oo . OOooOOo - i11iIiiIii
    ii11iIi1I = xbmcgui . Dialog ( )
    if ii11iIi1I . yesno ( "Delete Package Cache Files" , str ( II1iiI1iI ) + " files found" , "Do you want to delete them?" ) :
     if 49 - 49: Oo / o00O0oo % o0000oOoOoO0o + OoOO - Ooo00oOo00o
     for oOooOOOoOo in OOOiiiiI :
      os . unlink ( os . path . join ( oOO , oOooOOOoOo ) )
     for OOoO in iIiIi11 :
      shutil . rmtree ( os . path . join ( oOO , OOoO ) )
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
 O0o = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 OooOOooo = os . path . join ( O0o , 'advancedsettings.xml' )
 ii11iIi1I = xbmcgui . Dialog ( )
 O00oOoo00O = os . path . join ( O0o , 'advancedsettings.xml.bak' )
 if os . path . exists ( O00oOoo00O ) == False :
  if ii11iIi1I . yesno ( "Back Up Original" , 'Have You Backed Up Your Original?' , '' , "[B][COLOR red]     AS YOU CANNOT GO BACK !!![/B][/COLOR]" ) :
   print '###' + i11 + ' - ADVANCED XML###'
   O0o = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
   OooOOooo = os . path . join ( O0o , 'advancedsettings.xml' )
   try :
    os . remove ( OooOOooo )
    print '=== GenieTv - REMOVING    ' + str ( OooOOooo ) + '    ==='
   except :
    pass
   o0ooooO0o0O = I11 . http_GET ( url ) . content
   i1Iii1i1I = open ( OooOOooo , "w" )
   i1Iii1i1I . write ( o0ooooO0o0O )
   i1Iii1i1I . close ( )
   print '=== GenieTv - WRITING NEW    ' + str ( OooOOooo ) + '    ==='
   ii11iIi1I = xbmcgui . Dialog ( )
   ii11iIi1I . ok ( i11 , "       Done Adding new Advanced XML" )
 else :
  print '###' + i11 + ' - ADVANCED XML###'
  O0o = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
  OooOOooo = os . path . join ( O0o , 'advancedsettings.xml' )
  try :
   os . remove ( OooOOooo )
   print '=== GenieTv - REMOVING    ' + str ( OooOOooo ) + '    ==='
  except :
   pass
  o0ooooO0o0O = I11 . http_GET ( url ) . content
  i1Iii1i1I = open ( OooOOooo , "w" )
  i1Iii1i1I . write ( o0ooooO0o0O )
  i1Iii1i1I . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( OooOOooo ) + '    ==='
  ii11iIi1I = xbmcgui . Dialog ( )
  ii11iIi1I . ok ( i11 , "       Done Adding new Advanced XML" )
 return
 if 25 - 25: i11iIiiIii + ii11ii1ii - OoooooooOO . O0 % O0oO
def oOOO ( url , name ) :
 print '###' + i11 + ' - CHECK ADVANCE XML###'
 O0o = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 OooOOooo = os . path . join ( O0o , 'advancedsettings.xml' )
 try :
  i1Iii1i1I = open ( OooOOooo ) . read ( )
  if 'zero' in i1Iii1i1I :
   name = '0CACHE'
  elif 'tuxen' in i1Iii1i1I :
   name = 'TUXENS'
  elif 'muckys' in i1Iii1i1I :
   name = 'MUCKYS'
  elif 'p2p1' in i1Iii1i1I :
   name = '1st P2P RECOMMENDED'
  elif 'p2p2' in i1Iii1i1I :
   name = '2nd P2P RECOMMENDED'
  elif 'mikey' in i1Iii1i1I :
   name = 'MIKEY1234'
 except :
  name = "NO ADVANCED"
 ii11iIi1I = xbmcgui . Dialog ( )
 ii11iIi1I . ok ( i11 , "[COLOR yellow]YOU HAVE[/COLOR] " + name + "[COLOR yellow] XML SETTINGS SETUP[/COLOR]" )
 return
 if 54 - 54: OoOO / iIii1I11I1II1 / OoooooooOO . i1IIi - I1IiI
def Oo00o0OOo0OO ( url ) :
 print '###' + i11 + ' - DELETING ADVANCE XML###'
 O0o = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 OooOOooo = os . path . join ( O0o , 'advancedsettings.xml' )
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
 O00O0oOO00O00 = re . compile ( "<td width='80'>(.+?)</td><td>(.+?)</td><td>(.+?)</td><td>.+?</td><td>(.+?)</td>" ) . findall ( I11 . http_GET ( url ) . content )
 for i1I1iI1 , oOOoO , iii1i1Iiiiiii , OOoo0 in O00O0oOO00O00 :
  if inc < 2 : ii11iIi1I = xbmcgui . Dialog ( ) ; ii11iIi1I . ok ( 'Check My IP' , "[B][COLOR gold]Your IP Address is: [/COLOR][/B] %s" % i1I1iI1 , '[B][COLOR gold]Your IP is based in: [/COLOR][/B] %s' % iii1i1Iiiiiii , '[B][COLOR gold]Your Service Provider is:[/COLOR][/B] %s' % OOoo0 )
  inc = inc + 1
  if 7 - 7: OOOo0 % O0oO * IIII + I1IiI / I1IiI
  if 34 - 34: OoOoOO00 % i11iIiiIii % Ooo00oOo00o . I1IiI + i11iIiiIii
  if 53 - 53: i11iIiiIii - i11iIiiIii + o00O0oo - I1IiI % OoOO - o0000oOoOoO0o
  if 57 - 57: OOooOOo % oO0o0ooO0 % O0oO . o0oO0 - o00O0oo % Ooo00oOo00o
  if 28 - 28: o0000oOoOoO0o * O0 - OoOO
  if 34 - 34: oO0o0ooO0 % i11iIiiIii + i11iIiiIii - oO0o0ooO0
  if 2 - 2: OoOoOO00 + i1IIi
  if 68 - 68: OoOO0ooOOoo0O + o00O0oo
  if 58 - 58: IIII * o00O0oo . i1IIi
def i11I1iiii ( url , name ) :
 ii11iIi1I = xbmcgui . Dialog ( )
 if ii11iIi1I . yesno ( "GenieTv" , '                                    Install Latest .ini File' ) :
  print '###' + i11 + ' - CUSTOM FTV INI###'
  O0o = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/script.ftvguide' , '' ) )
  OooOOooo = os . path . join ( O0o , 'addons2.ini' )
  o0ooooO0o0O = I11 . http_GET ( url ) . content
  i1Iii1i1I = open ( OooOOooo , "w" )
  i1Iii1i1I . write ( o0ooooO0o0O )
  i1Iii1i1I . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( OooOOooo ) + '    ==='
  ii11iIi1I = xbmcgui . Dialog ( )
  ii11iIi1I . ok ( i11 , "                               Done Adding New .ini File" )
 return
 if 31 - 31: O0oO / Oo / iIii1I11I1II1
def oOO00OOOoO0o ( url , name ) :
 ii11iIi1I = xbmcgui . Dialog ( )
 if ii11iIi1I . yesno ( "GenieTv" , '                               Install Custom Settings' ) :
  print '###' + i11 + ' - CUSTOM FTV SETTINGS###'
  O0o = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/script.ftvguide' , '' ) )
  OooOOooo = os . path . join ( O0o , 'settings.xml' )
  o0ooooO0o0O = I11 . http_GET ( url ) . content
  i1Iii1i1I = open ( OooOOooo , "w" )
  i1Iii1i1I . write ( o0ooooO0o0O )
  i1Iii1i1I . close ( )
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
def O0o0O00Oo0o0 ( url ) :
 ii11ii11I = urllib2 . Request ( url )
 ii11ii11I . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
 Oo0oo0oOO0oOo = urllib2 . urlopen ( ii11ii11I )
 o0ooooO0o0O = Oo0oo0oOO0oOo . read ( )
 Oo0oo0oOO0oOo . close ( )
 return o0ooooO0o0O
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
   for oOO , iIiIi11 , OOOiiiiI in os . walk ( o0o0oo0OOo0O0 , topdown = True ) :
    iIiIi11 [ : ] = [ OOoO for OOoO in iIiIi11 if OOoO not in Oo0oO0ooo ]
    for iiI111I1iIiI in OOOiiiiI :
     try : os . remove ( os . path . join ( oOO , iiI111I1iIiI ) )
     except :
      if iiI111I1iIiI not in [ "Addons15.db" , "MyVideos75.db" , "Textures13.db" , "xbmc.log" ] : iIIiiII11i1I1 = True
      plugintools . log ( "Error removing " + oOO + " " + iiI111I1iIiI )
    for iiI111I1iIiI in iIiIi11 :
     try : os . rmdir ( os . path . join ( oOO , iiI111I1iIiI ) )
     except :
      if iiI111I1iIiI not in [ "Database" , "userdata" ] : iIIiiII11i1I1 = True
      plugintools . log ( "Error removing " + oOO + " " + iiI111I1iIiI )
   if not iIIiiII11i1I1 : plugintools . log ( "freshstart.main_list All user files removed, you now have a clean install" ) ; plugintools . message ( i11 , "The process is complete, you're now back to a fresh Kodi configuration with GenieTv!" , "Please reboot your system or restart Kodi in order for the changes to be applied." )
   else : plugintools . log ( "freshstart.main_list User files partially removed" ) ; plugintools . message ( i11 , "The process is complete, you're now back to a fresh Kodi configuration with GenieTv" , "Please reboot your system or restart Kodi in order for the changes to be applied." )
  except : plugintools . message ( i11 , "Problem found" , "Your settings has not been changed" ) ; import traceback ; plugintools . log ( traceback . format_exc ( ) ) ; plugintools . log ( "freshstart.main_list NOT removed" )
  plugintools . add_item ( action = "" , title = "Now Exit Kodi" , folder = False )
 else : plugintools . message ( i11 , "Your settings" , "has not been changed" ) ; plugintools . add_item ( action = "" , title = "Done" , folder = False )
 ii1ii111 ( )
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
  for i1iIIIiiiI in range ( len ( iIi11I1II ) ) :
   oO00Oo0O0 = { }
   oO00Oo0O0 = iIi11I1II [ i1iIIIiiiI ] . split ( '=' )
   if ( len ( oO00Oo0O0 ) ) == 2 :
    ooo0Oo00O [ oO00Oo0O0 [ 0 ] ] = oO00Oo0O0 [ 1 ]
    if 91 - 91: o0000oOoOoO0o + o00O0oo + IIII
 return ooo0Oo00O
 if 58 - 58: oO0o0ooO0 * o00O0oo - i11iIiiIii % ii11ii1ii
ooooO0oOoOOoO = base64 . decodestring ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20v' )
iiI1iI111ii1i = base64 . decodestring ( 'L3N0b3JhZ2UvZW11bGF0ZWQvMA==' )
I1i11i = base64 . decodestring ( 'L2dlbmllLnR4dA==' )
I11O0O0o = base64 . decodestring ( 'LmFyY2hpdGVjdHMueDEwaG9zdC5jb20vdGVzdC93aC50eHQ=' )
iiIi11iI1iii = base64 . decodestring ( 'aHR0cDovL2ZpeGVzLmFyY2hpdGVjdHMueDEwaG9zdC5jb20vZml4ZXMudHh0' )
i1i1i1I = base64 . decodestring ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vYXBwcy9hcHBzLnhtbA==' )
Ooooo0O0 = base64 . decodestring ( 'L2FkZG9ucy9uZXcudHh0' )
i111II = base64 . decodestring ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vdm9kL3ZvZC5waHA=' )
i11I = base64 . decodestring ( 'L2FkZG9ucy9pcHR2LnR4dA==' )
oOO00o0O0 = base64 . decodestring ( 'L2FkZG9ucy92aWRlby50eHQ=' )
IiIi = base64 . decodestring ( 'L2FkZG9ucy9zcG9ydHMudHh0' )
iI1iIoOo = base64 . decodestring ( 'L2FkZG9ucy9raWRzLnR4dA==' )
oOoOoOOo00Ooo0O = base64 . decodestring ( 'L2FkZG9ucy9tdXNpYy50eHQ=' )
Ii11ii1 = base64 . decodestring ( 'L2FkZG9ucy9wcm9ncmFtcy50eHQ=' )
O000OOOo = base64 . decodestring ( 'L2FkZG9ucy94eHgudHh0' )
IiOo00O0o0O = base64 . decodestring ( 'L2FkZG9ucy9yZXBvLnR4dA==' )
II1iI1I11I = base64 . decodestring ( 'L2FkZG9ucy9wYWNrcy50eHQ=' )
O0o0 = base64 . decodestring ( 'L2FkZG9ucy9za2lucy50eHQ=' )
OOo = base64 . decodestring ( 'L2FkZG9ucy9hcnQudHh0' )
o0o0OoOo0O0OO = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2dvdGhhbS50eHQ=' )
iII1i11IIi1i = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2hlbGl4LnR4dA==' )
OOoOoOo = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2lzZW5nYXJkLnR4dA==' )
Ooo0OOOo = base64 . decodestring ( 'L2FkZG9ucy9SU1MudHh0' )
i1II1I = base64 . decodestring ( 'Q1VOVA==' )
def iiiiiIIii ( name , url , mode , iconimage , fanart , description , showcontext = True , allinfo = { } ) :
 O00ooOo = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 oOO0o00O = True
 oOoO = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 oOoO . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 oOoO . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  O0o0oOOO = [ ]
  if showcontext == 'fav' :
   O0o0oOOO . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in oOoOooOo0o0 :
   O0o0oOOO . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fanart=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , urllib . quote_plus ( fanart ) , mode ) ) )
  oOoO . addContextMenuItems ( O0o0oOOO )
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
i1Oo00 = None
iiI111I1iIiI = None
ooO000O = None
oo000 = None
o0000oO = None
O0ii1ii1ii = None
o0OO0 = None
if 11 - 11: IIII % ii11ii1ii / o0oO0 . i11iIiiIii + OoOO0ooOOoo0O - OoOoOO00
if 50 - 50: i1IIi * OoOO / i11iIiiIii / i11iIiiIii / OoOO
try :
 o0OO0 = int ( Ooo0OOO0O00 [ "fav_mode" ] )
except :
 pass
 if 84 - 84: ii11ii1ii - oO0o0ooO0 + ii11ii1ii
try :
 i1Oo00 = urllib . unquote_plus ( Ooo0OOO0O00 [ "url" ] )
except :
 pass
try :
 iiI111I1iIiI = urllib . unquote_plus ( Ooo0OOO0O00 [ "name" ] )
except :
 pass
try :
 oo000 = urllib . unquote_plus ( Ooo0OOO0O00 [ "iconimage" ] )
except :
 pass
try :
 ooO000O = int ( Ooo0OOO0O00 [ "mode" ] )
except :
 pass
try :
 o0000oO = urllib . unquote_plus ( Ooo0OOO0O00 [ "fanart" ] )
except :
 pass
try :
 O0ii1ii1ii = urllib . unquote_plus ( Ooo0OOO0O00 [ "description" ] )
except :
 pass
 if 63 - 63: o0000oOoOoO0o * o0oO0 % OoOoOO00 % O0oO + OOOo0 * Oo
 if 96 - 96: IIII
print str ( II11iiii1Ii ) + ': ' + str ( iiI1IiI )
print "Mode: " + str ( ooO000O )
print "URL: " + str ( i1Oo00 )
print "Name: " + str ( iiI111I1iIiI )
print "IconImage: " + str ( oo000 )
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
 I1I ( i1Oo00 )
 if 61 - 61: iIii1I11I1II1 + OoOO * o0000oOoOoO0o - i1IIi % OoOO
elif ooO000O == 44 :
 iIIiIiI1I1 ( i1Oo00 )
 if 76 - 76: OoOO / I1IiI
elif ooO000O == 2 :
 o0O0Oo ( )
 if 12 - 12: O0oO
elif ooO000O == 3 :
 I1i ( )
 if 58 - 58: Ooo00oOo00o + iIii1I11I1II1 % O0 + o0000oOoOoO0o + I1IiI * OoooooooOO
elif ooO000O == 21 :
 ooO0oooOO0 ( )
 if 41 - 41: OoOO * OOOo0
elif ooO000O == 4 :
 oOOOoo00 ( )
 if 76 - 76: OoOO . O0 * OoooooooOO + o0oO0
elif ooO000O == 5 :
 II1Iiiiii ( iiI111I1iIiI , i1Oo00 , O0ii1ii1ii )
 if 53 - 53: Oo
elif ooO000O == 6 :
 o0o0O00oOo ( i1Oo00 )
 if 3 - 3: IIII - OoooooooOO * OoooooooOO - OOOo0 / O0oO * ii11ii1ii
elif ooO000O == 7 :
 oOooo00OOO000 ( i1Oo00 , iiI111I1iIiI )
 if 58 - 58: IIII % iIii1I11I1II1 / i11iIiiIii % OOooOOo . O0oO * oO0o0ooO0
elif ooO000O == 8 :
 oOOO ( i1Oo00 , iiI111I1iIiI )
 if 32 - 32: OoooooooOO + OOooOOo
elif ooO000O == 9 :
 FIXREPOSADDONS ( i1Oo00 )
 if 91 - 91: o0oO0 - O0oO * O0oO
elif ooO000O == 10 :
 Oo0 ( )
 if 55 - 55: iIii1I11I1II1 + OOOo0 - Oo
elif ooO000O == 11 :
 Oo00o0OOo0OO ( i1Oo00 )
 if 24 - 24: Ooo00oOo00o / O0oO + oO0o0ooO0 * o0000oOoOoO0o * oO0o0ooO0
elif ooO000O == 12 :
 IIi1ioO0o ( )
 if 10 - 10: OOOo0 - ii11ii1ii - Oo - OOooOOo
elif ooO000O == 13 :
 i1i1i11iI11II ( )
 if 21 - 21: OoooooooOO + O0oO
elif ooO000O == 14 :
 II1iOOoOooO0o ( i1Oo00 )
 if 43 - 43: i11iIiiIii . ii11ii1ii . OoOO
elif ooO000O == 15 :
 oOoO00O0 ( )
 if 31 - 31: o00O0oo % OOooOOo % O0oO . ii11ii1ii / OOooOOo * OoOO
elif ooO000O == 16 :
 i11I1iiii ( i1Oo00 , iiI111I1iIiI )
 if 74 - 74: OOOo0 . o0oO0 / oO0o0ooO0 . IIII
elif ooO000O == 17 :
 oOO00OOOoO0o ( i1Oo00 , iiI111I1iIiI )
 if 74 - 74: Oo / O0oO % O0oO . IIII
elif ooO000O == 18 :
 oO00O0o0oOOO ( )
 if 72 - 72: i1IIi
elif ooO000O == 19 :
 iIIi ( iiI111I1iIiI , i1Oo00 , O0ii1ii1ii )
 if 21 - 21: O0oO . OoOO0ooOOoo0O / i11iIiiIii * i1IIi
elif ooO000O == 40 :
 oo00O00Oo ( iiI111I1iIiI , i1Oo00 , O0ii1ii1ii )
 if 82 - 82: o0oO0 * Oo % i11iIiiIii * i1IIi . OoOO0ooOOoo0O
elif ooO000O == 42 :
 O0O0Ooo ( iiI111I1iIiI , i1Oo00 , O0ii1ii1ii )
 if 89 - 89: IIII - i1IIi - IIII
elif ooO000O == 43 :
 IIII1 ( iiI111I1iIiI , i1Oo00 , O0ii1ii1ii )
 if 74 - 74: Ooo00oOo00o % Ooo00oOo00o
elif ooO000O == 20 :
 O0oOo00o ( i1Oo00 )
 if 28 - 28: I1IiI % OoOO - OoOO0ooOOoo0O + OoOO0ooOOoo0O + OoOO / iIii1I11I1II1
elif ooO000O == 22 :
 oo0O ( i1Oo00 )
 if 91 - 91: OOOo0 / OoOoOO00 * OoOO0ooOOoo0O
elif ooO000O == 23 :
 I111Ii11i11I ( i1Oo00 )
 if 94 - 94: OoOoOO00 - iIii1I11I1II1 - iIii1I11I1II1
elif ooO000O == 24 :
 OO0Oo00OO0oo ( i1Oo00 )
 if 83 - 83: ii11ii1ii * iIii1I11I1II1 + I1IiI * i1IIi . OoooooooOO % o00O0oo
elif ooO000O == 25 :
 Oo0oo ( i1Oo00 )
 if 81 - 81: Ooo00oOo00o - iIii1I11I1II1
elif ooO000O == 26 :
 i1iIii1II1i ( i1Oo00 )
 if 60 - 60: O0oO
elif ooO000O == 27 :
 IIIIIiI1I1 ( i1Oo00 )
 if 77 - 77: OOOo0 / ii11ii1ii
elif ooO000O == 28 :
 i1Oo ( i1Oo00 )
 if 95 - 95: O0oO * i1IIi + OoOO
elif ooO000O == 29 :
 i1IiiI1 ( i1Oo00 )
 if 40 - 40: OoOoOO00
elif ooO000O == 30 :
 OOooo0O0o0 ( i1Oo00 )
 if 7 - 7: OoOO0ooOOoo0O / Ooo00oOo00o
elif ooO000O == 31 :
 I1iIIi ( i1Oo00 )
 if 88 - 88: i1IIi
elif ooO000O == 32 :
 OoOO0o ( )
 if 53 - 53: o0oO0 . OoOO0ooOOoo0O . OOooOOo + OoOO
elif ooO000O == 33 :
 O0OoooO0 ( )
 if 17 - 17: iIii1I11I1II1 + i1IIi . ii11ii1ii + o00O0oo % i1IIi . OoOO
elif ooO000O == 35 :
 O00OoOO0oo0 ( i1Oo00 )
 if 57 - 57: OoOO
elif ooO000O == 34 :
 OOOiII1 ( i1Oo00 )
 if 92 - 92: OoOoOO00 - Ooo00oOo00o - OoOO0ooOOoo0O % OOOo0 - I1IiI * O0oO
elif ooO000O == 36 :
 iI1i11II1i ( i1Oo00 )
 if 16 - 16: iIii1I11I1II1 + OoooooooOO - o0oO0 * IIII
elif ooO000O == 37 :
 o0OOOooo0OOo ( i1Oo00 )
 if 37 - 37: oO0o0ooO0
elif ooO000O == 38 :
 O0O0o0oOOO ( i1Oo00 )
 if 15 - 15: OOooOOo % Ooo00oOo00o / oO0o0ooO0
elif ooO000O == 41 :
 oO0OOo ( Ooo0OOO0O00 )
 if 36 - 36: Ooo00oOo00o + Ooo00oOo00o % Oo + Oo / i1IIi % i1IIi
elif ooO000O == 39 :
 Ii1iI1IIIII ( i1Oo00 )
 if 20 - 20: OoOO0ooOOoo0O * OoOO
elif ooO000O == 45 :
 TEXTS ( )
 if 91 - 91: Ooo00oOo00o % i1IIi - iIii1I11I1II1 . OoOO0ooOOoo0O
elif ooO000O == 46 :
 Ii1I1Iiii ( )
 if 31 - 31: OoOO % i1IIi . OoooooooOO - OOooOOo + OoooooooOO
elif ooO000O == 47 :
 GEVID ( )
 if 45 - 45: OoOO0ooOOoo0O + o0000oOoOoO0o / OoooooooOO - o00O0oo + OoooooooOO
elif ooO000O == 48 :
 oOOO0oo0 ( iiI111I1iIiI , i1Oo00 , O0ii1ii1ii )
 if 42 - 42: iIii1I11I1II1 * OOOo0 * O0oO
elif ooO000O == 49 :
 OoO ( )
 if 62 - 62: OoOO0ooOOoo0O * O0 % IIII . IIII . OOOo0
elif ooO000O == 222 :
 iIIIiIi1i ( i1Oo00 )
 if 91 - 91: i1IIi . oO0o0ooO0
elif ooO000O == 333 :
 ii11I11 ( i1Oo00 )
 if 37 - 37: oO0o0ooO0 - o0000oOoOoO0o + iIii1I11I1II1 / O0oO - Ooo00oOo00o . OOooOOo
 if 62 - 62: ii11ii1ii
elif ooO000O == 1001 :
 I11iii1I1Iiii ( )
 if 47 - 47: O0oO % OoOO0ooOOoo0O * Ooo00oOo00o . iIii1I11I1II1 % Oo + OoooooooOO
elif ooO000O == 1005 :
 O00oo0oOoO00O ( )
 if 2 - 2: O0oO % OoooooooOO - o0oO0 * ii11ii1ii * IIII
elif ooO000O == 1007 :
 Iii1iIiI1I1I1 ( i1Oo00 )
 if 99 - 99: iIii1I11I1II1 . Oo / o0oO0 . OoOO0ooOOoo0O % OOOo0 * o0000oOoOoO0o
elif ooO000O == 1010 :
 iiOo0 ( i1Oo00 )
 if 95 - 95: OoOO
elif ooO000O == 1011 :
 OOO00ii1Ii111I11I ( i1Oo00 )
 if 80 - 80: IIII
elif ooO000O == 1030 :
 o0OoOoo ( )
 if 42 - 42: OoooooooOO * OoOoOO00
elif ooO000O == 1031 :
 O0OoO0o0Oooo ( i1Oo00 , oo000 )
 if 53 - 53: O0oO + i1IIi . Ooo00oOo00o / i11iIiiIii + o00O0oo % I1IiI
elif ooO000O == 1006 :
 Parse . ParseURL ( i1Oo00 )
 if 9 - 9: o0oO0 . o0000oOoOoO0o - Oo . O0oO
elif ooO000O == 2030 :
 Parse . addonParseURL ( i1Oo00 )
 if 39 - 39: OoOO0ooOOoo0O
elif ooO000O == 2031 :
 Parse . apkParseURL ( i1Oo00 )
 if 70 - 70: IIII % Ooo00oOo00o % OOOo0
elif ooO000O == 1002 :
 oo0O0oOOO0o ( i1Oo00 )
 if 95 - 95: I1IiI - O0oO / O0 * OOOo0 - OOooOOo
elif ooO000O == 1003 :
 oOo0Oo0Oo0 ( i1Oo00 , oo000 )
 if 12 - 12: iIii1I11I1II1 % Oo . oO0o0ooO0 . IIII % i11iIiiIii
elif ooO000O == 1004 :
 OooOo0o0OO ( i1Oo00 )
 if 2 - 2: OoOO * OoOO . I1IiI * o00O0oo * iIii1I11I1II1
elif ooO000O == 1008 :
 Oo000 ( )
 if 13 - 13: o0000oOoOoO0o / O0 . i11iIiiIii * i1IIi % i11iIiiIii
elif ooO000O == 1009 :
 M3UPLAY ( i1Oo00 )
 if 8 - 8: I1IiI - OoooooooOO
elif ooO000O == 2001 :
 iiiiI11iiIIi ( i1Oo00 )
 if 99 - 99: OoOoOO00 / IIII % OoooooooOO . i11iIiiIii
elif ooO000O == 1013 :
 OO0oOOoo ( )
 if 18 - 18: OOooOOo . o0oO0
elif ooO000O == 1014 :
 IiiI11I1IIiI ( )
 if 70 - 70: OoooooooOO . o0oO0 / OoOO . OoOO - OOooOOo
elif ooO000O == 1015 :
 i1iI1i ( i1Oo00 )
 if 29 - 29: o0000oOoOoO0o % OoOO0ooOOoo0O - o0oO0
elif ooO000O == 1016 :
 o0o0O0oOOOooo ( i1Oo00 )
 if 26 - 26: O0 . o0000oOoOoO0o + oO0o0ooO0 - o00O0oo . o0000oOoOoO0o
elif ooO000O == 1023 :
 I1i1i1iii ( )
 if 2 - 2: ii11ii1ii . Oo * OoOO0ooOOoo0O % OoOoOO00 . oO0o0ooO0
elif ooO000O == 1024 :
 I1ii1I1iii1 ( )
 if 46 - 46: I1IiI + OOOo0 % OoooooooOO * i11iIiiIii - Oo
elif ooO000O == 1025 :
 iIiiiIIiii ( i1Oo00 )
 if 47 - 47: oO0o0ooO0 * I1IiI * IIII
elif ooO000O == 4001 :
 II111ii1II1i ( )
 if 46 - 46: o00O0oo
elif ooO000O == 4002 :
 OoOo00o ( )
 if 42 - 42: iIii1I11I1II1
elif ooO000O == 4003 :
 IIo0Oo0oO0oOO00 ( )
 if 32 - 32: Oo - o00O0oo . OoooooooOO - OoooooooOO - Oo . iIii1I11I1II1
elif ooO000O == 3000 :
 i1iI ( )
 if 34 - 34: Oo
elif ooO000O == 3001 :
 iii1IIiI ( )
 if 31 - 31: i1IIi - o0000oOoOoO0o + O0oO + o0oO0 . o0oO0 . O0
elif ooO000O == 3002 :
 i1i1Ii11Ii ( i1Oo00 )
 if 33 - 33: i1IIi / oO0o0ooO0 * Ooo00oOo00o
elif ooO000O == 3003 :
 O000oOo ( i1Oo00 )
 if 2 - 2: OoOO . OoOO0ooOOoo0O
elif ooO000O == 3004 :
 iI1iIiiI ( i1Oo00 )
 if 43 - 43: iIii1I11I1II1
elif ooO000O == 404 :
 OOOO00 ( iiI111I1iIiI , i1Oo00 , oo000 )
 if 29 - 29: IIII % o0oO0 + Ooo00oOo00o . i1IIi + OOOo0
elif ooO000O == 7030 :
 III1I1Iii11i ( )
 if 24 - 24: O0oO / o00O0oo * ii11ii1ii - OoooooooOO / OOOo0 . OoOO
elif ooO000O == 7021 :
 oOooOOo00ooO ( iiI111I1iIiI )
 if 98 - 98: i1IIi - oO0o0ooO0
elif ooO000O == 7022 :
 oOoOo0o00o ( iiI111I1iIiI )
 if 49 - 49: OOooOOo . o00O0oo . OoOO
elif ooO000O == 7000 :
 i1iIIiI1111 ( iiI111I1iIiI , i1Oo00 , img )
 if 9 - 9: IIII - OoOoOO00 * Ooo00oOo00o
elif ooO000O == 7050 :
 i1IiI1Iiii ( i1Oo00 )
 if 78 - 78: iIii1I11I1II1 / O0 * OoOO / oO0o0ooO0 / I1IiI
elif ooO000O == 7051 :
 oOOoOOO0oOoo ( i1Oo00 )
 if 15 - 15: o0oO0 / OoOO
elif ooO000O == 7052 :
 IIIii11i1I ( i1Oo00 )
 if 54 - 54: o0oO0 - iIii1I11I1II1 - o0000oOoOoO0o % o00O0oo / OoOoOO00
elif ooO000O == 7053 :
 ooo0O00000oo0 ( i1Oo00 )
 if 80 - 80: i11iIiiIii % iIii1I11I1II1 / i11iIiiIii
elif ooO000O == 7054 :
 CoolPlay ( i1Oo00 )
 if 66 - 66: I1IiI . iIii1I11I1II1 * ii11ii1ii - o00O0oo - iIii1I11I1II1
elif ooO000O == 7060 :
 iiIi ( )
 if 28 - 28: I1IiI % OoooooooOO
elif ooO000O == 7061 :
 IiIi1Ii ( i1Oo00 )
 if 13 - 13: IIII . Oo - o0000oOoOoO0o / OoOO - Oo - OOOo0
elif ooO000O == 7063 :
 OooooOo ( i1Oo00 )
 if 84 - 84: OoOoOO00
elif ooO000O == 7062 :
 OoooOo0 ( i1Oo00 )
 if 57 - 57: O0 * iIii1I11I1II1 % O0 . OoooooooOO
elif ooO000O == 7064 :
 NATatozcat ( )
 if 53 - 53: o00O0oo / OOOo0 * o00O0oo + OOooOOo + OoOO - Oo
elif ooO000O == 7067 :
 i11i11i ( i1Oo00 )
 if 16 - 16: Ooo00oOo00o % O0oO . i1IIi / ii11ii1ii - O0
elif ooO000O == 7066 :
 NATatozA ( i1Oo00 )
 if 85 - 85: i1IIi . i1IIi
elif ooO000O == 7065 :
 iiI1iI ( i1Oo00 )
 if 16 - 16: OOOo0 - OoOO0ooOOoo0O % o00O0oo . OoOO0ooOOoo0O + ii11ii1ii % i11iIiiIii
elif ooO000O == 7070 :
 o00OoOO0O0 ( )
 if 59 - 59: i11iIiiIii - o0000oOoOoO0o
elif ooO000O == 7071 :
 DIZIlist ( i1Oo00 )
 if 59 - 59: OoooooooOO * OOooOOo / O0oO
elif ooO000O == 7072 :
 DIZIpull ( i1Oo00 )
 if 75 - 75: OOooOOo - OoooooooOO
elif ooO000O == 7073 :
 WATCHDIZI ( i1Oo00 )
 if 21 - 21: OOOo0 + iIii1I11I1II1 / i11iIiiIii / OoOO
elif ooO000O == 7002 :
 I1iII1IIi1IiI ( )
 if 66 - 66: OoooooooOO + oO0o0ooO0 . IIII % i1IIi
elif ooO000O == 7003 :
 o0ooOO00OO0o0O ( i1Oo00 )
 if 58 - 58: OoOO0ooOOoo0O % oO0o0ooO0 * O0 + ii11ii1ii - IIII
elif ooO000O == 7004 :
 O00Oo ( i1Oo00 )
 if 26 - 26: i1IIi / OOOo0 / o0000oOoOoO0o + o0000oOoOoO0o
elif ooO000O == 7020 :
 O00o0000OO ( i1Oo00 )
 if 46 - 46: O0oO % ii11ii1ii + o00O0oo
elif ooO000O == 7001 :
 IIi11Ii11ii ( )
 if 67 - 67: iIii1I11I1II1 . i11iIiiIii . i11iIiiIii . i11iIiiIii / o0000oOoOoO0o + o0oO0
elif ooO000O == 7010 :
 III1ii ( i1Oo00 )
 if 10 - 10: o0oO0 - Oo % OoOoOO00
elif ooO000O == 7011 :
 o0oOoO00 ( i1Oo00 )
 if 66 - 66: iIii1I11I1II1 . iIii1I11I1II1
elif ooO000O == 7012 :
 O00OO ( i1Oo00 )
 if 46 - 46: O0oO * OoOO . o00O0oo * O0oO * iIii1I11I1II1 / o0000oOoOoO0o
elif ooO000O == 7013 :
 cnfTVPlay2 ( i1Oo00 )
elif ooO000O == 7014 :
 CNF_Studio_Indexer . MV_Movies ( i1Oo00 )
elif ooO000O == 7015 :
 CNF_Studio_Indexer . Movie_ByYear ( i1Oo00 )
elif ooO000O == 7016 :
 CNF_Studio_Indexer . Resolve_CNF_Link ( iiI111I1iIiI , i1Oo00 , oo000 )
elif ooO000O == 7017 :
 CNF_Studio_Indexer . Search_Movie ( )
elif ooO000O == 7018 :
 oO0oo0O0 ( )
elif ooO000O == 7019 :
 CNF_Studio_Indexer . List_Movies ( i1Oo00 )
elif ooO000O == 7020 :
 CNF_Studio_Indexer . Get_Movie_Page ( i1Oo00 )
elif ooO000O == 7024 :
 CNF_Studio_Indexer . Box_Office ( i1Oo00 )
 if 46 - 46: OoOoOO00 % ii11ii1ii . OoOO0ooOOoo0O . Oo / i11iIiiIii + Ooo00oOo00o
elif ooO000O == 8000 :
 oOoO0OOO00O ( )
elif ooO000O == 8001 :
 III1IiI1i1i ( )
elif ooO000O == 8002 :
 iiIiii ( )
elif ooO000O == 8003 :
 O0OooOO ( )
elif ooO000O == 8004 :
 O0OOo0o ( )
elif ooO000O == 8005 :
 oO0o0Oo ( )
elif ooO000O == 8006 :
 IiI11I111 ( iiI111I1iIiI , i1Oo00 )
elif ooO000O == 8030 :
 OooooO0oOOOO ( i1Oo00 )
elif ooO000O == 8045 :
 I1IiI1ii1ii1I ( i1Oo00 )
elif ooO000O == 8046 :
 iI1IIi11i1I1 ( i1Oo00 )
elif ooO000O == 8047 :
 o0oOO00 ( i1Oo00 )
elif ooO000O == 8040 :
 oOoOo ( )
elif ooO000O == 8041 :
 OoO00O0OOO ( i1Oo00 )
elif ooO000O == 8042 :
 I11i11i1 ( i1Oo00 )
elif ooO000O == 8043 :
 yt . PlayVideo ( i1Oo00 )
elif ooO000O == 8044 :
 OOOii1i1iiI ( i1Oo00 )
elif ooO000O == 8060 :
 IiI ( )
elif ooO000O == 8061 :
 O0o0OO00 ( i1Oo00 )
elif ooO000O == 8064 :
 OOOoo ( )
elif ooO000O == 8065 :
 III1II1iii1i ( i1Oo00 )
elif ooO000O == 8070 :
 OooooO ( )
elif ooO000O == 8071 :
 oO0O0 ( i1Oo00 )
elif ooO000O == 7080 :
 iI111i11iI1 ( i1Oo00 )
elif ooO000O == 8090 :
 o0O0OO0OOOOOo ( )
elif ooO000O == 8091 :
 IIi1i ( i1Oo00 )
elif ooO000O == 8092 :
 iIiIIiii1II ( i1Oo00 )
elif ooO000O == 8081 :
 oOOOOOo ( )
elif ooO000O == 8062 :
 Ii1III1 ( i1Oo00 )
elif ooO000O == 8063 :
 I1ii1Ii1 ( i1Oo00 )
elif ooO000O == 8050 :
 Ii1I11ii1i ( )
elif ooO000O == 8051 :
 O0iIiIIIIIii ( i1Oo00 )
elif ooO000O == 8052 :
 ii11I1 ( i1Oo00 )
elif ooO000O == 8085 :
 I11o0000o0Oo ( )
elif ooO000O == 8086 :
 II11I ( i1Oo00 )
elif ooO000O == 8087 :
 i11iIIi ( i1Oo00 )
elif ooO000O == 8088 :
 O000O ( i1Oo00 , iiI111I1iIiI )
elif ooO000O == 9000 :
 OooOo0ooo ( )
elif ooO000O == 1111 :
 i111 ( )
elif ooO000O == 9001 :
 o0o0O0O000 ( )
elif ooO000O == 9002 :
 OOOoOOo0o ( )
elif ooO000O == 9003 :
 II1ii ( )
elif ooO000O == 50 :
 oOoO00o ( i1Oo00 )
elif ooO000O == 9020 :
 champlist ( )
elif ooO000O == 9021 :
 o0ooo0o0 ( )
elif ooO000O == 9022 :
 O00Oooo00 ( )
elif ooO000O == 9023 :
 ooO0 ( )
elif ooO000O == 9024 :
 OoOo ( i1Oo00 )
elif ooO000O == 9030 :
 iIiiIi ( i1Oo00 )
elif ooO000O == 9031 :
 i1I111II ( i1Oo00 )
elif ooO000O == 9032 :
 Oo0OOoi1II11I11ii1 ( i1Oo00 )
elif ooO000O == 9033 :
 OOoO0oO00o ( i1Oo00 )
elif ooO000O == 7085 :
 iI1iI ( i1Oo00 )
elif ooO000O == 7086 :
 IIIIIIi ( i1Oo00 )
elif ooO000O == 7087 :
 o0OOoOo0oo ( O0ii1ii1ii )
elif ooO000O == 9666 :
 i1II11iI1i ( i1Oo00 )
elif ooO000O == 10100 : I1III1iIi ( )
elif ooO000O == 10105 : IiIo0o0OO0o00o0O ( i1Oo00 )
elif ooO000O == 10106 : i1I1iI ( i1Oo00 )
elif ooO000O == 10104 : ii1i ( i1Oo00 )
elif ooO000O == 10107 : o0OO0OOO0O ( )
elif ooO000O == 10103 : Iiii1i11ii1Ii ( i1Oo00 )
elif ooO000O == 10108 : oO0OOO0o0O ( i1Oo00 )
elif ooO000O == 10107 : o0OO0OOO0O ( )
elif ooO000O == 10000 : Origin_Menu ( )
elif ooO000O == 10001 : Iii ( )
elif ooO000O == 10002 : o00ooo0 ( )
elif ooO000O == 10003 : i11i11 ( )
elif ooO000O == 10004 : ii1i1i1IiII ( )
elif ooO000O == 10005 : o0OooO0ooo0o ( )
elif ooO000O == 10006 : I1 ( i1Oo00 )
elif ooO000O == 10007 : i1I1IiI ( i1Oo00 , oo000 )
elif ooO000O == 10008 : oO000o0Oo00 ( )
elif ooO000O == 10009 : iIiIi1iI11iiI ( )
elif ooO000O == 10010 : III1II111Ii1 ( i1Oo00 )
elif ooO000O == 10011 : OoOoooO0O00 ( i1Oo00 )
elif ooO000O == 10012 : o00oO00 ( i1Oo00 )
elif ooO000O == 10013 : Iii111Ii1 ( i1Oo00 )
elif ooO000O == 10014 : IiiiI ( )
elif ooO000O == 10015 : Ii1i1i1111 ( )
elif ooO000O == 10016 : O0Oo ( i1Oo00 )
elif ooO000O == 10017 : II11i11Iii ( )
elif ooO000O == 10018 : i1i1IiIiIi1Ii ( )
elif ooO000O == 10019 : o0O0OO ( )
elif ooO000O == 10020 : O0o00O0Oo0 ( )
elif ooO000O == 10021 : I1Iii1iI1 ( )
elif ooO000O == 10022 : IiIiIi1I1 ( i1Oo00 )
elif ooO000O == 10023 : o0o00oO0oo000 ( iiI111I1iIiI , i1Oo00 )
elif ooO000O == 10024 : O0iI ( i1Oo00 )
elif ooO000O == 10025 : Oo00OOOOoo0oo ( )
elif ooO000O == 10026 : o0OOoOoO00 ( )
elif ooO000O == 10027 : o0OO0O0Oo ( )
elif ooO000O == 10028 : OoO00 ( )
elif ooO000O == 10029 : OooO0oOo ( )
elif ooO000O == 423 : ooO ( i1Oo00 )
elif ooO000O == 426 : II1IIIiiI11 ( i1Oo00 )
elif ooO000O == 10030 : Izle_Films ( )
elif ooO000O == 10031 : Latest_Izle_Movies ( )
elif ooO000O == 10032 : Izle_Genres ( )
elif ooO000O == 10033 : Izle_Pop_Movies ( )
elif ooO000O == 10034 : Izle_Boxsets ( )
elif ooO000O == 10035 : Izle_Search ( )
elif ooO000O == 10036 : Izle_Genres_Movie ( i1Oo00 )
elif ooO000O == 10037 : Izle_Boxset_single ( i1Oo00 )
elif ooO000O == 10038 : Izle_IFRAME ( )
elif ooO000O == 10039 : Izle_Boxsets_Next ( i1Oo00 )
elif ooO000O == 10040 : oo0000o ( )
elif ooO000O == 10041 : IiIi1III ( i1Oo00 )
elif ooO000O == 10042 : IIii1I1I1I ( i1Oo00 )
elif ooO000O == 10043 : IiiiIiiIIi ( )
elif ooO000O == 10044 : ii111Iiii ( i1Oo00 )
elif ooO000O == 10045 : i1iIIi1o0o0OoOOOOOo ( iiI111I1iIiI )
elif ooO000O == 10046 : OO0OO ( i1Oo00 )
elif ooO000O == 10047 : O0oOo ( i1Oo00 )
elif ooO000O == 10048 : I11iiIIiI1ii ( i1Oo00 )
elif ooO000O == 10049 : O00 ( i1Oo00 )
elif ooO000O == 10050 : oO0oo ( )
elif ooO000O == 10051 : o0Oo00oOO ( )
elif ooO000O == 10052 : iiI1ii1Iii ( )
elif ooO000O == 10053 : Addon ( i1Oo00 )
elif ooO000O == 10054 : i1i1Ii1IiIII ( i1Oo00 , iiI111I1iIiI )
elif ooO000O == 10055 :
 OOooo00 ( "addFavorite" )
 try :
  iiI111I1iIiI = iiI111I1iIiI . split ( '\\ ' ) [ 1 ]
 except :
  pass
 try :
  iiI111I1iIiI = iiI111I1iIiI . split ( '  - ' ) [ 0 ]
 except :
  pass
 iiII ( iiI111I1iIiI , i1Oo00 , oo000 , o0000oO , o0OO0 )
elif ooO000O == 10056 :
 OOooo00 ( "rmFavorite" )
 try :
  iiI111I1iIiI = iiI111I1iIiI . split ( '\\ ' ) [ 1 ]
 except :
  pass
 try :
  iiI111I1iIiI = iiI111I1iIiI . split ( '  - ' ) [ 0 ]
 except :
  pass
 OOOOOOoO ( iiI111I1iIiI )
elif ooO000O == 10057 :
 OOooo00 ( "getFavorites" )
 Ii1iIi111i1i1 ( )
elif ooO000O == 10058 : o0o ( )
elif ooO000O == 10059 : Donators_Guide ( )
elif ooO000O == 10060 : OooOOOOo ( )
elif ooO000O == 10061 : IIiII111iiI1I ( )
elif ooO000O == 10062 : OOooOoooOoOo ( iiI111I1iIiI , i1Oo00 , O0ii1ii1ii )
elif ooO000O == 10063 : OOOooOO0 ( )
elif ooO000O == 10064 : OOO ( )
elif ooO000O == 10065 : O0OOO ( i1Oo00 )
elif ooO000O == 20000 : O0O0oOOo0O ( )
elif ooO000O == 20001 : ii1 ( )
elif ooO000O == 20002 : I1iii ( i1Oo00 )
elif ooO000O == 20003 : Ooo0oo ( i1Oo00 )
elif ooO000O == 20004 : iioOo0OoOOo0 ( i1Oo00 )
elif ooO000O == 21004 : ooo000o0ooO0 ( )
elif ooO000O == 21005 : I1IoOoo000 ( i1Oo00 )
elif ooO000O == 21006 : IiI11i1IIiiI ( i1Oo00 )
elif ooO000O == 21007 : iI1IIIii ( i1Oo00 )
elif ooO000O == 30000 : IIiiI ( )
elif ooO000O == 30001 : II1i ( )
elif ooO000O == 10012 : Resolve ( i1Oo00 )
elif ooO000O == 30003 : i1iIiIi1I ( )
elif ooO000O == 30004 : O0Oo0o000oO ( i1Oo00 )
elif ooO000O == 30005 : oOooO0OOOoO000 ( i1Oo00 )
elif ooO000O == 30006 : o00oO ( )
elif ooO000O == 30007 : I1Ii1111iIi ( )
elif ooO000O == 30008 : iiI1I1ii ( i1Oo00 )
elif ooO000O == 30009 : i1iiIiI1Ii1i ( i1Oo00 )
elif ooO000O == 30010 : OOoO0II11iI111i1 ( i1Oo00 )
elif ooO000O == 30011 : i11iI11iIiIi ( )
elif ooO000O == 30012 : IIIii1 ( )
elif ooO000O == 30013 : i1iiiii1 ( )
elif ooO000O == 30014 : o0Iii ( )
if 47 - 47: IIII . OoOO0ooOOoo0O
xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
