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
iiI1IiI = "2.5.1"
II = xbmc . translatePath ( 'special://database' )
ooOoOoo0O = xbmc . translatePath ( 'special://home/userdata/addon_data/plugin.video.GenieTV' )
OooO0 = xbmc . translatePath ( 'special://thumbnails' ) ;
II11iiii1Ii = "GenieTv"
OO0o = ( oOo0oooo00o ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20=' ) )
Ooo = 'http://'
O0o0Oo = o0oOoO00o . getLocalizedString
Oo00OOOOO = CookieJar ( )
O0O = urllib2 . build_opener ( urllib2 . HTTPCookieProcessor ( Oo00OOOOO ) )
O0O . addheaders = [ ( 'User-Agent' , 'Mozilla/5.0' ) ]
O00o0OO = int ( sys . argv [ 1 ] )
I11i1 = xbmc . translatePath ( o0oOoO00o . getAddonInfo ( 'profile' ) . decode ( 'utf-8' ) )
iIi1ii1I1 = os . path . join ( I11i1 , 'favorites' )
o0 = xbmc . translatePath ( os . path . join ( 'special://home/userdata/addon_data/script.ivueguide/master.db' ) )
I11II1i = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , 'favourites.xml' ) )
IIIII = xbmc . translatePath ( os . path . join ( 'special://home/userdata/addon_data/plugin.video.GenieTv/favorites' ) )
if os . path . exists ( iIi1ii1I1 ) == True :
 ooooooO0oo = open ( iIi1ii1I1 ) . read ( )
else : ooooooO0oo = [ ]
IIiiiiiiIi1I1 = o0oOoO00o . getSetting ( 'debug' )
if os . path . exists ( ooOoOoo0O ) == False :
 os . makedirs ( ooOoOoo0O )
def I1IIIii ( ) :
 if o0oOoO00o . getSetting ( 'My Build' ) == 'true' :
  oOoOooOo0o0 ( '[COLORgreen]WIZARD[/COLOR]' , OO0o , 4001 , oOOoO0 + 'MB.png' , OOooO0OOoo , '' )
 if o0oOoO00o . getSetting ( 'Streams' ) == 'true' :
  oOoOooOo0o0 ( '[COLORgreen]STREAMS[/COLOR]' , OO0o , 4002 , oOOoO0 + 'streams.png' , OOooO0OOoo , '' )
 if o0oOoO00o . getSetting ( 'Music' ) == 'true' :
  oOoOooOo0o0 ( '[COLORgreen]Music[/COLOR]' , OO0o , 4003 , oOOoO0 + 'MUSIC.png' , OOooO0OOoo , '' )
  if 61 - 61: OOooOOo / Ooo00oOo00o + o0oO0 * OoOO / OoOO
 if o0oOoO00o . getSetting ( 'Builders Toolbox' ) == 'true' :
  oOoOooOo0o0 ( '[COLORgreen]BUILDERS TOOLBOX[/COLOR]' , OO0o , 32 , oOOoO0 + 'builderstoolbox.png' , OOooO0OOoo , '' )
 if o0oOoO00o . getSetting ( 'Source List' ) == 'true' :
  oOoOooOo0o0 ( '[COLORgreen]SOURCE LIST[/COLOR]' , OO0o , 46 , oOOoO0 + 'sources.png' , OOooO0OOoo , '' )
 if o0oOoO00o . getSetting ( 'Maintainance' ) == 'true' :
  oOoOooOo0o0 ( '[COLORgreen]MAINTENANCE[/COLOR]' , OO0o , 3 , oOOoO0 + 'MAIN6.png' , OOooO0OOoo , '' )
 if o0oOoO00o . getSetting ( 'Addons' ) == 'true' :
  oOoOooOo0o0 ( '[COLORgreen]ADDONS[/COLOR]' , '' , 10050 , oOOoO0 + 'ADDONS.png' , OOooO0OOoo , '' )
 if o0oOoO00o . getSetting ( 'APK Tool' ) == 'true' :
  oOoOooOo0o0 ( '[COLORgreen]APK TOOL[/COLOR]' , OO0o , 2 , oOOoO0 + 'APK.png' , OOooO0OOoo , '' )
 if o0oOoO00o . getSetting ( 'Rss Feed' ) == 'true' :
  oOoOooOo0o0 ( '[COLORgreen]GenieTv RSS Feed[/COLOR]' , OO0o , 39 , oOOoO0 + 'RSS.png' , OOooO0OOoo , '' )
 if o0oOoO00o . getSetting ( 'Addons Packs' ) == 'true' :
  oOoOooOo0o0 ( '[COLORgreen]ADDONS PACKS[/COLOR]' , OO0o , 30 , oOOoO0 + 'ADDONP.png' , OOooO0OOoo , '' )
 OoOo ( 'movies' , 'MAIN' )
 if 18 - 18: i11iIiiIii
def Ii11I ( ) :
 oOoOooOo0o0 ( '[COLORgreen]BACKUP MY BUILD[/COLOR]' , OO0o , 10060 , oOOoO0 + 'MB.png' , OOooO0OOoo , '' )
 oOoOooOo0o0 ( '[COLORgreen]RESTORE MY BUILD[/COLOR]' , OO0o , 49 , oOOoO0 + 'MB.png' , OOooO0OOoo , '' )
 oOoOooOo0o0 ( '[COLORgreen]WIPE GENIE[/COLOR]' , OO0o , 41 , oOOoO0 + 'wipegenie.png' , OOooO0OOoo , '' )
 oOoOooOo0o0 ( '[COLORgreen]WISHES PC[/COLOR]' , OO0o , 1 , oOOoO0 + 'WISHESPC.png' , OOooO0OOoo , '' )
 oOoOooOo0o0 ( '[COLORgreen]WISHES ANDROID[/COLOR]' , OO0o , 44 , oOOoO0 + 'WISHESAN.png' , OOooO0OOoo , '' )
 OoOo ( 'movies' , 'MAIN' )
def OOO0OOO00oo ( ) :
 if i1iIIi1 == '5knuckleshuffle' :
  oOoOooOo0o0 ( '[COLORgreen]XVID[/COLOR]' , OO0o , 10100 , oOOoO0 + 'JIZBOX.png' , OOooO0OOoo , '' )
 if o0oOoO00o . getSetting ( 'TV GUIDE' ) == 'true' :
  Iii111II ( '[COLORgreen]TV GUIDE[/COLOR]' , '' , 10063 , oOOoO0 + 'GTVIPTV.png' , OOooO0OOoo , '' )
  if o0oOoO00o . getSetting ( 'Favourites' ) == 'true' :
   oOoOooOo0o0 ( '[COLORgreen]FAVOURITES[/COLOR]' , OO0o , 10057 , oOOoO0 + 'FAVORITES.png' , OOooO0OOoo , '' )
 if o0oOoO00o . getSetting ( 'Search' ) == 'true' :
  oOoOooOo0o0 ( '[COLORgreen]SEARCH[/COLOR]' , OO0o , 9000 , oOOoO0 + 'search.png' , OOooO0OOoo , '' )
 if o0oOoO00o . getSetting ( 'G-tv' ) == 'true' :
  oOoOooOo0o0 ( '[COLORgreen]G-Tv PRIVATE LIST[/COLOR]' , '' , 10058 , oOOoO0 + 'GTVIPTV.png' , OOooO0OOoo , '' )
 if o0oOoO00o . getSetting ( 'Popcorn Box' ) == 'true' :
  oOoOooOo0o0 ( '[COLORgreen]POPCORN BOX[/COLOR]' , OO0o , 7061 , oOOoO0 + 'popcorn.png' , OOooO0OOoo , '' )
 if o0oOoO00o . getSetting ( 'Dizzy Tv' ) == 'true' :
  oOoOooOo0o0 ( '[COLORgreen]DIZZY TV[/COLOR]' , '' , 10018 , oOOoO0 + 'dtv.png' , OOooO0OOoo , '' )
 if o0oOoO00o . getSetting ( 'Watch Series' ) == 'true' :
  oOoOooOo0o0 ( '[COLORgreen]WATCH SERIES[/COLOR]' , '' , 10040 , oOOoO0 + 'WATCHSERIES.png' , OOooO0OOoo , '' )
 if o0oOoO00o . getSetting ( 'Recent Episodes' ) == 'true' :
  oOoOooOo0o0 ( '[COLORgreen]RECENT EPISODES[/COLOR]' , OO0o , 8081 , oOOoO0 + 'recent.png' , OOooO0OOoo , '' )
 if o0oOoO00o . getSetting ( 'Scooby Streams' ) == 'true' :
  oOoOooOo0o0 ( '[COLORgreen]SCOOBY STREAMS[/COLOR]' , OO0o , 1023 , oOOoO0 + 'scoob.png' , OOooO0OOoo , '' )
 if o0oOoO00o . getSetting ( 'The Reaper' ) == 'true' :
  oOoOooOo0o0 ( '[COLORgreen]THE REAPER[/COLOR]' , ( oOo0oooo00o ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9UaGVfUmVhcGVyL21haW4ucGhw' ) ) , 1016 , oOOoO0 + 'reap.png' , OOooO0OOoo , '' )
 if o0oOoO00o . getSetting ( 'Pandoras Box' ) == 'true' :
  oOoOooOo0o0 ( '[COLORgreen]PANDORAS BOX[/COLOR]' , OO0o , 10025 , oOOoO0 + 'PANDORASBOX.png' , OOooO0OOoo , '' )
 if o0oOoO00o . getSetting ( 'HeroVision' ) == 'true' :
  oOoOooOo0o0 ( '[COLORgreen]HEROVISION[/COLOR]' , ( oOo0oooo00o ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC9tYWluLnBocA==' ) ) , 1016 , oOOoO0 + 'hero.png' , OOooO0OOoo , '' )
 if o0oOoO00o . getSetting ( 'Silent Hunter' ) == 'true' :
  oOoOooOo0o0 ( '[COLORgreen]SILENT HUNTER[/COLOR]' , ( oOo0oooo00o ( 'aHR0cDovLzUuMTM1LjIwNy45Ni8=' ) ) , 1006 , oOOoO0 + 'SILENTHUNTER.png' , OOooO0OOoo , '' )
 if o0oOoO00o . getSetting ( 'Stand Up' ) == 'true' :
  oOoOooOo0o0 ( '[COLORgreen]STAND UP[/COLOR]' , '' , 10003 , oOOoO0 + 'ORIGINSTANDUP.png' , OOooO0OOoo , '' )
 if o0oOoO00o . getSetting ( 'Football' ) == 'true' :
  oOoOooOo0o0 ( '[COLORgreen]FOOTBALL[/COLOR]' , '' , 10002 , oOOoO0 + 'ORIGINFOOTBALL.png' , OOooO0OOoo , '' )
 if o0oOoO00o . getSetting ( 'Fitness' ) == 'true' :
  oOoOooOo0o0 ( '[COLORgreen]FITNESS[/COLOR]' , ( oOo0oooo00o ( 'aHR0cHM6Ly93d3cuZml0bmVzc2JsZW5kZXIuY29tL3ZpZGVvcw==' ) ) , 7085 , oOOoO0 + 'FITNESS.png' , OOooO0OOoo , '' )
 if o0oOoO00o . getSetting ( 'Documentaries' ) == 'true' :
  oOoOooOo0o0 ( '[COLORgreen]DOCUMENTARIES[/COLOR]' , OO0o , 8040 , oOOoO0 + 'documentary.png' , OOooO0OOoo , '' )
 if o0oOoO00o . getSetting ( 'CLASSIC MOVIES' ) == 'true' :
  oOoOooOo0o0 ( '[COLORgreen]CLASSIC MOVIES[/COLOR]' , '' , 8060 , oOOoO0 + 'classicmovies.png' , OOooO0OOoo , '' )
 if o0oOoO00o . getSetting ( 'CLASSIC TV' ) == 'true' :
  oOoOooOo0o0 ( '[COLORgreen]CLASSIC TV[/COLOR]' , OO0o , 8064 , oOOoO0 + 'classictv.png' , OOooO0OOoo , '' )
 if o0oOoO00o . getSetting ( 'Disclose' ) == 'true' :
  oOoOooOo0o0 ( '[COLORgreen]DISCLOSE TV[/COLOR]' , OO0o , 7001 , oOOoO0 + 'disclose.png' , OOooO0OOoo , '' )
 if o0oOoO00o . getSetting ( 'Go Fishing' ) == 'true' :
  oOoOooOo0o0 ( '[COLORgreen]Go Fishing[/COLOR]' , OO0o , 8090 , oOOoO0 + 'gofish.png' , OOooO0OOoo , '' )
 if o0oOoO00o . getSetting ( 'GenieTv Kitchen' ) == 'true' :
  oOoOooOo0o0 ( '[COLORgreen]GenieTv Kitchen[/COLOR]' , ( oOo0oooo00o ( 'aHR0cDovL2Zvb2QubmR0di5jb20vdmlkZW9z' ) ) , 8045 , oOOoO0 + 'geniekitchen.png' , OOooO0OOoo , '' )
 if o0oOoO00o . getSetting ( 'Cartoons' ) == 'true' :
  oOoOooOo0o0 ( '[COLORgreen]CARTOONS[/COLOR]' , '' , 10001 , oOOoO0 + 'ORIGINCARTOON.png' , OOooO0OOoo , '' )
 if o0oOoO00o . getSetting ( 'Anime' ) == 'true' :
  oOoOooOo0o0 ( '[COLORgreen]ANIME[/COLOR]' , OO0o , 1001 , oOOoO0 + 'anime.png' , OOooO0OOoo , '' )
 if o0oOoO00o . getSetting ( 'CONCERTS' ) == 'true' :
  oOoOooOo0o0 ( '[COLORgreen]CONCERTS[/COLOR]' , ( oOo0oooo00o ( 'aHR0cHM6Ly93d3cucmVkZGl0LmNvbS9yL2Z1bGxjb25jZXJ0cy8=' ) ) , 7050 , oOOoO0 + 'concerts.png' , OOooO0OOoo , '' )
 if o0oOoO00o . getSetting ( 'M3u Streams' ) == 'true' :
  oOoOooOo0o0 ( '[COLORgreen]M3U STREAMS[/COLOR]' , OO0o , 8070 , oOOoO0 + 'streams.png' , OOooO0OOoo , '' )
 if o0oOoO00o . getSetting ( 'Playlist Loader' ) == 'true' :
  oOoOooOo0o0 ( '[COLORgreen]PLAYLIST LOADER[/COLOR]' , OO0o , 3000 , oOOoO0 + 'loader.png' , OOooO0OOoo , '' )
 if o0oOoO00o . getSetting ( 'CLASSICS' ) == 'true' :
  oOoOooOo0o0 ( '[COLORgreen]CLASSICS[/COLOR]' , OO0o , 3001 , oOOoO0 + 'loader.png' , OOooO0OOoo , '' )
 oOoOooOo0o0 ( '[COLORgreen]WATCH CARTOONS ONLINE[/COLOR]' , OO0o , 21004 , oOOoO0 + 'loader.png' , OOooO0OOoo , '' )
 if 9 - 9: Ooo00oOo00o
 if 33 - 33: o0oO0 . oO0o0ooO0
 if 58 - 58: OoOO0ooOOoo0O * i11iIiiIii / I1IiI % O0oO - ii11ii1ii / OoOO
 if 50 - 50: OOOo0
 if 34 - 34: OOOo0 * OoOoOO00 % oO0o0ooO0 * I1IiI - OOOo0
 if 33 - 33: OOooOOo + OoOO0ooOOoo0O * Ooo00oOo00o - Oo / OoOO % o00O0oo
 if 21 - 21: Ooo00oOo00o * iIii1I11I1II1 % OoOO * i1IIi
 if 16 - 16: O0 - O0oO * iIii1I11I1II1 + oO0o0ooO0
 if 50 - 50: OoOoOO00 - o0oO0 * ii11ii1ii / O0oO + OOooOOo
 if 88 - 88: o00O0oo / O0oO + oO0o0ooO0 - OoOoOO00 / o0oO0 - I1IiI
 if 15 - 15: ii11ii1ii + I1IiI - OoooooooOO / OoOO0ooOOoo0O
 if 58 - 58: i11iIiiIii % o0000oOoOoO0o
 OoOo ( 'movies' , 'MAIN' )
 if 71 - 71: OoOO0ooOOoo0O + o0oO0 % i11iIiiIii + ii11ii1ii - IIII
 if 88 - 88: I1IiI - Ooo00oOo00o % OoOO0ooOOoo0O
 if 16 - 16: OOOo0 * OoOO % IIII
 if 86 - 86: OOOo0 + o00O0oo % i11iIiiIii * OoOO . o0oO0 * o0000oOoOoO0o
def i1I11i1iI ( ) :
 if 15 - 15: o00O0oo - O0 / OoOO * i1IIi
 oooo000 = Oo0o0000o0o0 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 iIIIi1 = 'https://www.youtube.com/results?search_query=' + ( oooo000 ) . replace ( ' ' , '+' )
 iiII1i1 = iIIIi1 . lower ( )
 o00oOO0o = OOO00O ( iiII1i1 )
 OOoOO0oo0ooO = re . compile ( 'yt-lockup-title "><a href="(.+?)".+?data-sessionlink=.+?" title="(.+?)"' , re . DOTALL ) . findall ( o00oOO0o )
 next = re . compile ( '<a href="(.+?)" class="yt-uix-button.+?class="yt-uix-button-content">Next.+?</span></a>' ) . findall ( o00oOO0o )
 for O0o0O00Oo0o0 in next :
  O0o0O00Oo0o0 = 'https://www.youtube.com' + O0o0O00Oo0o0
  oOoOooOo0o0 ( '[COLORgreen] NEXT [/COLOR]' , O0o0O00Oo0o0 , 10065 , oOOoO0 + 'youtube.png' , OOooO0OOoo , '' )
 for O0o0O00Oo0o0 , O00O0oOO00O00 in OOoOO0oo0ooO :
  O0o0O00Oo0o0 = 'http://www.youtube.com' + O0o0O00Oo0o0
  if '&' in O0o0O00Oo0o0 :
   o00oOO0o = OOO00O ( O0o0O00Oo0o0 )
   i1Oo00 = re . compile ( '<li class="yt-uix-scroller-scroll-unit "(.+?)</li>' , re . DOTALL ) . findall ( o00oOO0o )
   for i1Oo00 in i1Oo00 :
    O00O0oOO00O00 = re . compile ( 'data-video-title="(.+?)"' ) . findall ( str ( i1Oo00 ) )
    for O00O0oOO00O00 in O00O0oOO00O00 :
     if 'elete' in O00O0oOO00O00 :
      pass
     else :
      O00O0oOO00O00 = ( O00O0oOO00O00 ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&amp;' , '&' )
    O0o0O00Oo0o0 = re . compile ( '<a href="/w(.+?)&' ) . findall ( str ( i1Oo00 ) )
    for O0o0O00Oo0o0 in O0o0O00Oo0o0 :
     O0o0O00Oo0o0 = 'https://www.youtube.com/w' + O0o0O00Oo0o0
    Iii111II ( '[COLORgreen]' + O00O0oOO00O00 + '[/COLOR]' , ( O0o0O00Oo0o0 ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , oOOoO0 + 'youtube.png' , OOooO0OOoo , '' )
  else :
   Iii111II ( '[COLORgreen]' + O00O0oOO00O00 + '[/COLOR]' , ( O0o0O00Oo0o0 ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , oOOoO0 + 'youtube.png' , OOooO0OOoo , '' )
   if 31 - 31: O0oO . I1IiI / O0
def o000O0o ( url ) :
 o00oOO0o = OOO00O ( url )
 OOoOO0oo0ooO = re . compile ( 'yt-lockup-title "><a href="(.+?)".+?data-sessionlink=.+?" title="(.+?)"' , re . DOTALL ) . findall ( o00oOO0o )
 next = re . compile ( '<a href="(.+?)" class="yt-uix-button.+?class="yt-uix-button-content">Next.+?</span></a>' ) . findall ( o00oOO0o )
 for url in next :
  url = 'http://www.youtube.com' + url
  oOoOooOo0o0 ( '[COLORgreen] NEXT [/COLOR]' , url , 10065 , oOOoO0 + 'youtube.png' , OOooO0OOoo , '' )
 for url , O00O0oOO00O00 in OOoOO0oo0ooO :
  url = 'http://www.youtube.com' + url
  if '&' in url :
   o00oOO0o = OOO00O ( url )
   i1Oo00 = re . compile ( '<li class="yt-uix-scroller-scroll-unit "(.+?)</li>' , re . DOTALL ) . findall ( o00oOO0o )
   for i1Oo00 in i1Oo00 :
    O00O0oOO00O00 = re . compile ( 'data-video-title="(.+?)"' ) . findall ( str ( i1Oo00 ) )
    for O00O0oOO00O00 in O00O0oOO00O00 :
     if 'elete' in O00O0oOO00O00 :
      pass
     else :
      O00O0oOO00O00 = ( O00O0oOO00O00 ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&amp;' , '&' )
    url = re . compile ( '<a href="/w(.+?)&' ) . findall ( str ( i1Oo00 ) )
    for url in url :
     url = 'https://www.youtube.com/w' + url
    Iii111II ( '[COLORgreen]' + O00O0oOO00O00 + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , oOOoO0 + 'youtube.png' , OOooO0OOoo , '' )
  else :
   Iii111II ( '[COLORgreen]' + O00O0oOO00O00 + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , oOOoO0 + 'youtube.png' , OOooO0OOoo , '' )
   if 42 - 42: I1IiI
   if 41 - 41: Oo . o0oO0 + O0 * OOooOOo % Oo * Oo
def iIIIIi1iiIi1 ( ) :
 if i1iiIII111ii == 'insert_password' :
  Oo0o0000o0o0 . ok ( '[COLORgreen]Donators Login[/COLOR]' , 'You need to set username and password to access this' , 'These are unique and provided to donators to help with server and stream costs' , 'Donate @ [COLORgreen]http://architects.x10host.com[/COLOR]' )
  o0oOoO00o . openSettings ( sys . argv [ 0 ] )
 else :
  oOoOooOo0o0 ( '[COLORgreen]DONATORS LIST[/COLOR]' , OO0o + '/thelist.m3u' , 7080 , oOOoO0 + 'GTVIPTV.png' , OOooO0OOoo , '' )
  if 21 - 21: OOOo0 * iIii1I11I1II1
def oooooOoo0ooo ( ) :
 buggalo . SUBMIT_URL = 'http://tommy.winther.nu/exception/submit.php'
 try :
  I1I1IiI1 = gui . TVGuide ( )
  I1I1IiI1 . doModal ( )
  del I1I1IiI1
  print 'Deleted *W*'
 except Exception :
  print buggalo . onExceptionRaised ( )
  if 5 - 5: OOooOOo * o0oO0 + I1IiI . OoOO0ooOOoo0O + I1IiI
  if 91 - 91: O0
def oOOo0 ( ) :
 oOoOooOo0o0 ( 'Full Backup' , '' , 10061 , oOOoO0 + 'Backup.png' , OOooO0OOoo , 'Back Up Your Full System' )
 if os . path . exists ( IIIII ) :
  oOoOooOo0o0 ( 'Backup Genie Favourites' , O0o0O00Oo0o0 , 10062 , oOOoO0 + 'Backup.png' , OOooO0OOoo , 'Back Up Your favourites' )
 if os . path . exists ( o0 ) :
  oOoOooOo0o0 ( 'Backup Ivue Config' , o0 , 10062 , oOOoO0 + 'Backup.png' , OOooO0OOoo , 'Back Up Your master.db' )
 if os . path . exists ( I11II1i ) :
  oOoOooOo0o0 ( 'Backup Kodi Favourites' , I11II1i , 10062 , oOOoO0 + 'Backup.png' , OOooO0OOoo , 'Back Up Your favourites.xml' )
  if 54 - 54: O0 - IIII % OoOO0ooOOoo0O
  if 77 - 77: I1IiI / OOOo0 / Ooo00oOo00o + Ooo00oOo00o . OoOO0ooOOoo0O
  if 38 - 38: O0oO
zip = o0oOoO00o . getSetting ( 'zip' )
Ii1 = xbmc . translatePath ( os . path . join ( zip ) )
def OOooOO000 ( ) :
 OOoOoo = xbmc . translatePath ( os . path . join ( zip , 'testCBFolder' ) )
 if not os . path . exists ( zip ) :
  ii11iIi1I . ok ( '[COLOR=white]Origin[/COLOR]' , 'The download location you have stored does not exist .\nPlease update the addon settings and try again.' , '' , '' )
  o0oOoO00o . openSettings ( sys . argv [ 0 ] )
  if 85 - 85: ii11ii1ii % oO0o0ooO0 % o0oO0
  if 82 - 82: i11iIiiIii - oO0o0ooO0 * OoooooooOO / o0000oOoOoO0o
  if 31 - 31: IIII . Ooo00oOo00o - iIii1I11I1II1
def ooOOO00Ooo ( name , url , description ) :
 if 'Backup' in name :
  if 'Genie' in name :
   url = IIIII
  elif 'Ivue' in name :
   url = o0
  elif 'Kodi' in name :
   url = I11II1i
  OOooOO000 ( )
  IiIIIi1iIi = open ( url ) . read ( )
  ooOOoooooo = os . path . join ( Ii1 , description . split ( 'Your ' ) [ 1 ] )
  II1I = open ( ooOOoooooo , mode = 'w' )
  II1I . write ( IiIIIi1iIi )
  II1I . close ( )
 else :
  if 'guisettings.xml' in description :
   O0i1II1Iiii1I11 = open ( os . path . join ( Ii1 , description . split ( 'Your ' ) [ 1 ] ) ) . read ( )
   IIIIiiIiI = '<setting type="(.+?)" name="%s.(.+?)">(.+?)</setting>' % skin
   OOoOO0oo0ooO = re . compile ( IIIIiiIiI ) . findall ( O0i1II1Iiii1I11 )
   for type , o00oooO0Oo , o0O0OOO0Ooo in OOoOO0oo0ooO :
    o0O0OOO0Ooo = o0O0OOO0Ooo . replace ( '&quot;' , '' ) . replace ( '&amp;' , '&' )
    xbmc . executebuiltin ( "Skin.Se	t%s(%s,%s)" % ( type . title ( ) , o00oooO0Oo , o0O0OOO0Ooo ) )
  else :
   ooOOoooooo = os . path . join ( url )
   IiIIIi1iIi = open ( os . path . join ( Ii1 , description . split ( 'Your ' ) [ 1 ] ) ) . read ( )
   II1I = open ( ooOOoooooo , mode = 'w' )
   II1I . write ( IiIIIi1iIi )
   II1I . close ( )
 ii11iIi1I . ok ( "[COLOR=white]Origin[/COLOR]" , "" , 'All Done !' , '' )
 if 45 - 45: O0 / OOooOOo
 if 32 - 32: oO0o0ooO0 . IIII . IIII
 if 62 - 62: ii11ii1ii + IIII % oO0o0ooO0 + OoOO0ooOOoo0O
 if 33 - 33: O0 . IIII . OOOo0
def OoOOooOOO0 ( ) :
 o0o = 1
 OOooOO000 ( )
 O0OOoO00OO0o = xbmc . translatePath ( os . path . join ( Ii1 , 'Build Backup' , 'Full Backup' , '' ) )
 I1111IIIIIi = xbmc . translatePath ( os . path . join ( Ii1 , 'Build Backup' , 'my_full_backup.zip' ) )
 Iiii1i1 = xbmc . translatePath ( os . path . join ( Ii1 , 'Build Backup' , 'my_full_backup_GUI_Settings.zip' ) )
 if not os . path . exists ( O0OOoO00OO0o ) :
  os . makedirs ( O0OOoO00OO0o )
 OO = Oo0o0000o0o0 . input ( 'Enter a name for this backup' , type = xbmcgui . INPUT_ALPHANUM )
 if ( not OO ) : return False , 0
 oo000o = OO
 iiIi1IIi1I = xbmc . translatePath ( os . path . join ( O0OOoO00OO0o , oo000o + '.zip' ) )
 o0OoOO000ooO0 = [ 'plugin.video.GenieTv' ]
 o0o0o0oO0oOO = [ "xbmc.log" , "xbmc.old.log" , "kodi.log" , "kodi.old.log" , '.DS_Store' , '.setup_complete' , 'XBMCHelper.conf' ]
 ii1Ii11I = [ 'plugin.video.GenieTv' , 'repository.origin' , 'cache' , 'system' , 'Thumbnails' , "peripheral_data" , 'library' , 'keymaps' ]
 o00o0 = [ "xbmc.log" , "xbmc.old.log" , "kodi.log" , "kodi.old.log" , "Textures13.db" , '.DS_Store' , '.setup_complete' , 'XBMCHelper.conf' , 'advancedsettings.xml' ]
 ii = "Creating full backup of existing build"
 OOooooO0Oo = "Creating Community Build"
 OOiIiIIi1 = "Archiving..."
 I1IIII1i = ""
 I1I11i = "Please Wait"
 Ii1I1I1i1Ii ( iI111I11I1I1 , iiIi1IIi1I , OOooooO0Oo , OOiIiIIi1 , I1IIII1i , I1I11i , ii1Ii11I , o00o0 )
 time . sleep ( 1 )
 i1Oo0oO00o = xbmc . translatePath ( os . path . join ( O0OOoO00OO0o , oo000o + '_guisettings.zip' ) )
 i11I1II1I11i = zipfile . ZipFile ( i1Oo0oO00o , mode = 'w' )
 try :
  i11I1II1I11i . write ( xbmc . translatePath ( os . path . join ( iI111I11I1I1 , 'userdata' , 'profiles.xml' ) ) , 'profiles.xml' , zipfile . ZIP_DEFLATED )
 except : pass
 i11I1II1I11i . close ( )
 if o0o == 0 :
  ii11iIi1I . ok ( "FAILED!" , 'The guisettings.xml file could not be found on your' , 'system, please reboot and try again.' , '' )
 else :
  ii11iIi1I . ok ( "SUCCESS!" , 'You Are Now Backed Up. If you\'d like to share this build with' , 'the community please post details on the forum at' , '[COLOR=blue][B]http://rh-project.info[/COLOR][/B]' )
  ii11iIi1I . ok ( "Build Locations" , 'Full Backup (only used to restore on this device): [COLOR=yellow]' + I1111IIIIIi , '[/COLOR]Universal Backup (can be used on any device): [COLOR=yellow]' + iiIi1IIi1I + '[/COLOR]' )
  if 61 - 61: OOOo0 - OoOO0ooOOoo0O . OoOO / OoOO0ooOOoo0O + Oo
def Ii1I1I1i1Ii ( sourcefile , destfile , message_header , message1 , message2 , message3 , exclude_dirs , exclude_files ) :
 I1i11i = zipfile . ZipFile ( destfile , 'w' , zipfile . ZIP_DEFLATED )
 o00oO0oo0OO = len ( sourcefile )
 O0O0OOOOoo = [ ]
 oOooO0 = [ ]
 i1111 . create ( message_header , message1 , message2 , message3 )
 for Ii1I1Ii , OOoO0 , OO0Oooo0oOO0O in os . walk ( sourcefile ) :
  for file in OO0Oooo0oOO0O :
   oOooO0 . append ( file )
 o00O0 = len ( oOooO0 )
 for Ii1I1Ii , OOoO0 , OO0Oooo0oOO0O in os . walk ( sourcefile ) :
  OOoO0 [ : ] = [ oOO0O00Oo0O0o for oOO0O00Oo0O0o in OOoO0 if oOO0O00Oo0O0o not in exclude_dirs ]
  OO0Oooo0oOO0O [ : ] = [ II1I for II1I in OO0Oooo0oOO0O if II1I not in exclude_files ]
  for file in OO0Oooo0oOO0O :
   O0O0OOOOoo . append ( file )
   ii1 = len ( O0O0OOOOoo ) / float ( o00O0 ) * 100
   i1111 . update ( int ( ii1 ) , "Backing Up" , '[COLOR yellow]%s[/COLOR]' % file , 'Please Wait' )
   I1iIIiiIIi1i = os . path . join ( Ii1I1Ii , file )
   if not 'temp' in OOoO0 :
    if not 'plugin.program.originwizard' in OOoO0 :
     import time
     O0O0ooOOO = '01/01/1980'
     oOOo0O00o = time . strftime ( '%d/%m/%Y' , time . gmtime ( os . path . getmtime ( I1iIIiiIIi1i ) ) )
     if oOOo0O00o > O0O0ooOOO :
      I1i11i . write ( I1iIIiiIIi1i , I1iIIiiIIi1i [ o00oO0oo0OO : ] )
 I1i11i . close ( )
 i1111 . close ( )
 if 8 - 8: Ooo00oOo00o
 if 49 - 49: OOOo0 - o0000oOoOoO0o
def OoOOoOooooOOo ( ) :
 oOoOooOo0o0 ( '[COLORgreen]SCOOBY STREAMS[/COLOR]' , ( oOo0oooo00o ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvdHZjYXRzLnBocA==' ) ) , 1016 , oOOoO0 + 'scoob.png' , OOooO0OOoo , '' )
 oOoOooOo0o0 ( '[COLORgreen]SCOOBY SCRAPES[/COLOR]' , OO0o , 1024 , oOOoO0 + 'scoob.png' , OOooO0OOoo , '' )
 if 87 - 87: OOOo0
 if 58 - 58: I1IiI % OOooOOo
def i1OOoO ( ) :
 oOoOooOo0o0 ( '[COLORgreen]SEARCH MOVIES[/COLOR]' , OO0o , 9001 , oOOoO0 + 'MOVIESv.png' , OOooO0OOoo , '' )
 oOoOooOo0o0 ( '[COLORgreen]SEARCH SERIES[/COLOR]' , OO0o , 9002 , oOOoO0 + 'TVSHOWSv.png' , OOooO0OOoo , '' )
 oOoOooOo0o0 ( '[COLORgreen]SEARCH CARTOONS[/COLOR]' , '' , 10005 , oOOoO0 + 'ORIGINCARTOON' , OOooO0OOoo , '' )
 oOoOooOo0o0 ( '[COLORgreen]SEARCH YOUTUBE[/COLOR]' , OO0o , 10064 , oOOoO0 + 'youtube.png' , OOooO0OOoo , '' )
 if 89 - 89: OOooOOo + Ooo00oOo00o * o0000oOoOoO0o * o00O0oo
 if 37 - 37: OoooooooOO - O0 - OOooOOo
 if 77 - 77: OoOO0ooOOoo0O * iIii1I11I1II1
 if 98 - 98: OOOo0 % o00O0oo * OoooooooOO
def OoiIIiIi1 ( ) :
 oOoOooOo0o0 ( '[COLORgreen]RADIO[/COLOR]' , OO0o , 1013 , oOOoO0 + 'radio.png' , OOooO0OOoo , '' )
 oOoOooOo0o0 ( '[COLORgreen]MUSIC[/COLOR]' , OO0o , 1030 , oOOoO0 + 'MUSIC.png' , OOooO0OOoo , '' )
 oOoOooOo0o0 ( '[COLORgreen]MUSIC ARCHIVE[/COLOR]' , OO0o + ( oOo0oooo00o ( 'L3ZvZC91cmxzL211c2ljLnBocA==' ) ) , 1010 , oOOoO0 + 'MUSIC.png' , OOooO0OOoo , '' )
 oOoOooOo0o0 ( '[COLORgreen]MUSIC SEARCH[/COLOR]' , OO0o , 1111 , oOOoO0 + 'search.png' , OOooO0OOoo , '' )
 oOoOooOo0o0 ( '[COLORgreen]AUDIO BOOKS[/COLOR]' , 'http://doremisa.com/audiobooks/' , 1006 , oOOoO0 + 'search.png' , OOooO0OOoo , '' )
 if 74 - 74: oO0o0ooO0 + OOooOOo
 OoOo ( 'movies' , 'MAIN' )
 if 71 - 71: Oo % OoOO0ooOOoo0O
def O00oO000O0O ( ) :
 if 18 - 18: oO0o0ooO0 - OoOO0ooOOoo0O . O0oO . iIii1I11I1II1
 Iii111II ( 'DELETE CACHE' , 'url' , 14 , oOOoO0 + 'MAIN5.png' , OOooO0OOoo , '' )
 Iii111II ( 'DELETE PACKAGES' , 'url' , 6 , oOOoO0 + 'MAIN4.png' , OOooO0OOoo , '' )
 Iii111II ( 'FORCE REFRESH' , 'url' , 10 , oOOoO0 + 'MAIN3.png' , OOooO0OOoo , 'Force Refresh All Repos' )
 if 2 - 2: OoOO0ooOOoo0O . Ooo00oOo00o
 Iii111II ( 'CHECK MY IP' , 'url' , 12 , oOOoO0 + 'MAIN2.png' , OOooO0OOoo , '' )
 Iii111II ( 'ANDROID ONLY DELETE TEXTURE13.DB&THUBMNAIL FOLDER' , 'url' , 13 , oOOoO0 + 'MAIN1.png' , OOooO0OOoo , 'Only Works On Android On Windows It Deletes Your Thumnails Folder But Does Not Delete The Textures13.db' )
 oOoOooOo0o0 ( '[COLORgreen]ADVANCED SETTINGS XML[/COLOR]' , OO0o , 4 , oOOoO0 + 'XML.png' , OOooO0OOoo , '' )
 oOoOooOo0o0 ( '[COLORgreen]URL FIXES[/COLOR]' , OO0o , 20 , oOOoO0 + 'URLFIX.png' , OOooO0OOoo , '' )
 OoOo ( 'movies' , 'MAIN' )
 if 78 - 78: o0000oOoOoO0o * iIii1I11I1II1 . OOOo0 / OOooOOo - OoooooooOO / O0oO
 if 35 - 35: o0000oOoOoO0o % OoOO0ooOOoo0O - OoOO
def ii1iii1i ( ) :
 oOoOooOo0o0 ( '[COLORgreen]REPOS[/COLOR]' , ( oOo0oooo00o ( 'aHR0cDovL21pcnJvcnMua29kaS50di9hZGRvbnMv' ) ) , 2030 , oOOoO0 + 'repos.png' , OOooO0OOoo , '' )
 oOoOooOo0o0 ( '[COLORgreen]NEW[/COLOR]' , OO0o , 22 , oOOoO0 + 'NEW.png' , OOooO0OOoo , '' )
 oOoOooOo0o0 ( '[COLORgreen]IPTV[/COLOR]' , OO0o , 23 , oOOoO0 + 'IPTV.png' , OOooO0OOoo , '' )
 oOoOooOo0o0 ( '[COLORgreen]VIDEO[/COLOR]' , OO0o , 24 , oOOoO0 + 'VIDEO.png' , OOooO0OOoo , '' )
 oOoOooOo0o0 ( '[COLORgreen]SPORTS[/COLOR]' , OO0o , 25 , oOOoO0 + 'SPORTS.png' , OOooO0OOoo , '' )
 oOoOooOo0o0 ( '[COLORgreen]KIDS[/COLOR]' , OO0o , 26 , oOOoO0 + 'KIDS.png' , OOooO0OOoo , '' )
 oOoOooOo0o0 ( '[COLORgreen]MUSIC[/COLOR]' , OO0o , 27 , oOOoO0 + 'MUSIC.png' , OOooO0OOoo , '' )
 oOoOooOo0o0 ( '[COLORgreen]PROGRAMS[/COLOR]' , OO0o , 28 , oOOoO0 + 'PROGRAMS.png' , OOooO0OOoo , '' )
 oOoOooOo0o0 ( '[COLORgreen]XXX[/COLOR]' , 'URL' , 29 , oOOoO0 + 'XXX.png' , OOooO0OOoo , '' )
 OoOo ( 'movies' , 'MAIN' )
 if 35 - 35: OoOoOO00 % OoOO0ooOOoo0O . o0oO0 + o0oO0 % OoOoOO00 % OoOoOO00
 if 72 - 72: OoOoOO00 + i1IIi + OOooOOo
def OOO ( ) :
 Iii111II ( 'CHECK ADVANCED XML' , OO0o , 8 , oOOoO0 + 'XML.png' , OOooO0OOoo , '' )
 Iii111II ( 'MUCKYS XML' , OO0o + '/wizard/muckys.xml' , 7 , oOOoO0 + 'XML.png' , OOooO0OOoo , '' )
 Iii111II ( '0CACHE XML' , OO0o + '/wizard/0cache.xml' , 7 , oOOoO0 + 'XML.png' , OOooO0OOoo , '' )
 Iii111II ( 'MIKEY1234 XML' , OO0o + '/wizard/mikey.xml' , 7 , oOOoO0 + 'XML.png' , OOooO0OOoo , '' )
 Iii111II ( 'TUXENS XML' , OO0o + '/wizard/tuxens.xml' , 7 , oOOoO0 + 'XML.png' , OOooO0OOoo , '' )
 Iii111II ( 'P2P RECOMMENDED XML1' , OO0o + '/wizard/p2p1.xml' , 7 , oOOoO0 + 'XML.png' , OOooO0OOoo , '' )
 Iii111II ( 'P2P RECOMMENDED XML2' , OO0o + '/wizard/p2p2.xml' , 7 , oOOoO0 + 'XML.png' , OOooO0OOoo , '' )
 Iii111II ( 'DELETE XML' , OO0o , 11 , oOOoO0 + 'XML.png' , OOooO0OOoo , '' )
 OoOo ( 'movies' , 'MAIN' )
 if 25 - 25: OoOO - Ooo00oOo00o . iIii1I11I1II1 % i11iIiiIii % ii11ii1ii
def o0Oo0oO0oOO00 ( ) :
 Iii111II ( '[COLORgreen]My Local Zip[/COLOR]' , oo0o0O00 , 48 , oOOoO0 + 'MB.png' , OOooO0OOoo , '' )
 Iii111II ( '[COLORgreen]My Online Zip[/COLOR]' , oO0o0o0ooO0oO , 43 , oOOoO0 + 'MB.png' , OOooO0OOoo , '' )
 if 92 - 92: OoooooooOO * O0oO
def o0000oO ( ) :
 Iii111II ( 'INSTALL FTV GUIDE AND OTHER ADDONS REQUIRED' , OO0o + '/wizard/customftv/ftvguide-addons.zip' , 5 , oOOoO0 + 'FTV4.png' , OOooO0OOoo , '' )
 Iii111II ( 'FTV GUIDE FIRST RUN SETTINGS' , OO0o + '/wizard/customftv/settings.xml' , 17 , oOOoO0 + 'FTV3.png' , OOooO0OOoo , '' )
 Iii111II ( 'FTV GUIDE ADDONS2.INI UPDATE DAILY' , 'http://ren.byethost12.com/addons2.ini' , 16 , oOOoO0 + 'FTV1.png' , OOooO0OOoo , '' )
 Iii111II ( 'RESET FTV DATABASE' , 'url' , 18 , oOOoO0 + 'FTV2.png' , OOooO0OOoo , '' )
 if 11 - 11: o0oO0 / I1IiI - IIII * OoooooooOO + OoooooooOO . I1IiI
 if 26 - 26: o00O0oo % ii11ii1ii
 if 76 - 76: IIII * oO0o0ooO0
def ooooooo00o ( ) :
 oOoOooOo0o0 ( '[COLORgreen]SKINS[/COLOR]' , OO0o , 33 , oOOoO0 + 'skinp.png' , OOooO0OOoo , '' )
 oOoOooOo0o0 ( '[COLORgreen]ARTWORK PACKS[/COLOR]' , OO0o , 34 , oOOoO0 + 'artp.png' , OOooO0OOoo , '' )
 oOoOooOo0o0 ( '[COLORgreen]CREATE UNIVERSAL PATHS[/COLOR]' , iI111I11I1I1 , 35 , oOOoO0 + 'GUI.png' , OOooO0OOoo , '' )
 OoOo ( 'movies' , 'MAIN' )
 if 73 - 73: OoOO0ooOOoo0O
def ooO ( url ) :
 Ooo0oOooo0 = OOO00O ( oOOOoo00 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 OOoOO0oo0ooO = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( Ooo0oOooo0 )
 for O00O0oOO00O00 , url , iiIiIIIiiI , iiI1IIIi , II11IiIi11 in OOoOO0oo0ooO :
  oOoOooOo0o0 ( O00O0oOO00O00 , url , 5 , iiIiIIIiiI , iiI1IIIi , II11IiIi11 )
 OoOo ( 'movies' , 'MAIN' )
 if 7 - 7: Ooo00oOo00o . o00O0oo % OoOO * o0oO0 + IIII + O0oO
def IIIIiII1i ( ) :
 oOoOooOo0o0 ( '[COLORgreen]GOTHAM SKINS[/COLOR]' , OO0o , 36 , oOOoO0 + 'GSKIN.png' , OOooO0OOoo , '' )
 oOoOooOo0o0 ( '[COLORgreen]HELIX SKINS[/COLOR]' , OO0o , 37 , oOOoO0 + 'HSKIN.png' , OOooO0OOoo , '' )
 oOoOooOo0o0 ( '[COLORgreen]ISENGAARD SKINS[/COLOR]' , iI111I11I1I1 , 38 , oOOoO0 + 'ISKIN.png' , OOooO0OOoo , '' )
 OoOo ( 'movies' , 'MAIN' )
 if 1 - 1: OoOoOO00
def O0oOo00o ( url ) :
 Ooo0oOooo0 = OOO00O ( OO0o + o0ooooO0o0O ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 OOoOO0oo0ooO = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( Ooo0oOooo0 )
 for O00O0oOO00O00 , url , iiIiIIIiiI , iiI1IIIi , II11IiIi11 in OOoOO0oo0ooO :
  oOoOooOo0o0 ( O00O0oOO00O00 , url , 42 , iiIiIIIiiI , iiI1IIIi , II11IiIi11 )
 OoOo ( 'movies' , 'MAIN' )
 if 24 - 24: O0 * OOooOOo
def IiI1iiiIii ( url ) :
 Ooo0oOooo0 = OOO00O ( OO0o + I1III1111iIi ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 OOoOO0oo0ooO = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( Ooo0oOooo0 )
 for O00O0oOO00O00 , url , iiIiIIIiiI , iiI1IIIi , II11IiIi11 in OOoOO0oo0ooO :
  oOoOooOo0o0 ( O00O0oOO00O00 , url , 42 , iiIiIIIiiI , iiI1IIIi , II11IiIi11 )
 OoOo ( 'movies' , 'MAIN' )
 if 38 - 38: oO0o0ooO0 + o0000oOoOoO0o / O0oO % o0oO0 - ii11ii1ii
def iI11 ( url ) :
 Ooo0oOooo0 = OOO00O ( OO0o + Ii1I ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 OOoOO0oo0ooO = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( Ooo0oOooo0 )
 for O00O0oOO00O00 , url , iiIiIIIiiI , iiI1IIIi , II11IiIi11 in OOoOO0oo0ooO :
  oOoOooOo0o0 ( O00O0oOO00O00 , url , 42 , iiIiIIIiiI , iiI1IIIi , II11IiIi11 )
 OoOo ( 'movies' , 'MAIN' )
 if 88 - 88: o0000oOoOoO0o % ii11ii1ii
def I1i11 ( url ) :
 Ooo0oOooo0 = OOO00O ( oOo0oooo00o ( 'aHR0cHM6Ly9kbC5kcm9wYm94dXNlcmNvbnRlbnQuY29tL3MvN2ZrMjhndDlwb3QxMjJhL0JVSUxEUy50eHQ/ZGw9MA==' ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 OOoOO0oo0ooO = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( Ooo0oOooo0 )
 for O00O0oOO00O00 , url , iiIiIIIiiI , iiI1IIIi , II11IiIi11 in OOoOO0oo0ooO :
  oOoOooOo0o0 ( O00O0oOO00O00 , url , 42 , iiIiIIIiiI , iiI1IIIi , II11IiIi11 )
 OoOo ( 'movies' , 'MAIN' )
 if 12 - 12: i1IIi + i1IIi - ii11ii1ii * Oo % Oo - OoOoOO00
def o0O ( url ) :
 Ooo0oOooo0 = OOO00O ( OO0o + OOOooo ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 OOoOO0oo0ooO = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( Ooo0oOooo0 )
 for O00O0oOO00O00 , url , iiIiIIIiiI , iiI1IIIi , II11IiIi11 in OOoOO0oo0ooO :
  oOoOooOo0o0 ( O00O0oOO00O00 , url , 40 , iiIiIIIiiI , iiI1IIIi , II11IiIi11 )
 OoOo ( 'movies' , 'MAIN' )
 if 94 - 94: OoooooooOO + Oo / I1IiI * OoOO0ooOOoo0O
def o0OOo0o0O0O ( url ) :
 Ooo0oOooo0 = OOO00O ( OO0o + o0OO0o0oOOO0O ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 OOoOO0oo0ooO = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( Ooo0oOooo0 )
 for O00O0oOO00O00 , url , iiIiIIIiiI , iiI1IIIi , II11IiIi11 in OOoOO0oo0ooO :
  oOoOooOo0o0 ( O00O0oOO00O00 , url , 5 , iiIiIIIiiI , iiI1IIIi , II11IiIi11 )
 OoOo ( 'movies' , 'MAIN' )
 if 49 - 49: ii11ii1ii . OOooOOo . OoOoOO00
def o000ooooO0o ( ) :
 iI1i11 = OoOOoooOO0O ( oOo0oooo00o ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vYXBrdG9vbC9hcGsucGhw' ) )
 OOoOO0oo0ooO = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( iI1i11 )
 for O0o0O00Oo0o0 , ooo00Ooo , O00O0oOO00O00 in OOoOO0oo0ooO :
  Oo0o0O00 ( O00O0oOO00O00 , O0o0O00Oo0o0 , 2031 , ooo00Ooo )
  if 40 - 40: OoooooooOO
def I1i1i1 ( name , url , description ) :
 OOoOoo = xbmc . translatePath ( os . path . join ( OoO0O00O0oo0O , 'Download' ) )
 i1111 = xbmcgui . DialogProgress ( )
 i1111 . create ( "Your App Is Downloading" , "Why not check out our website" , '' , 'Http://architects.x10host.com' )
 I1IiI11 = os . path . join ( OOoOoo , name + '.apk' )
 try :
  os . remove ( I1IiI11 )
 except :
  pass
 downloader . download ( url , I1IiI11 , i1111 )
 ii11iIi1I = xbmcgui . Dialog ( )
 ii11iIi1I . ok ( "GenieTv" , "[COLORred]Please press ok, exit kodi and go to your downloads folder to install your app[/COLOR]" , "[COLORblue]Tool Brought To You By Architects@Work[/COLOR]" )
 if 9 - 9: o0000oOoOoO0o
def OoooO ( url ) :
 OOoOoo = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/resources/downloads' ) )
 i1111 = xbmcgui . DialogProgress ( )
 i1111 . create ( "Your fILM Is Downloading" , "Why not check out our website" , '' , 'Http://architects.x10host.com' )
 I1IiI11 = os . path . join ( OOoOoo , O00O0oOO00O00 + '.mp4' )
 try :
  os . remove ( I1IiI11 )
 except :
  pass
 downloader . download ( url , I1IiI11 , i1111 )
 ii11iIi1I = xbmcgui . Dialog ( )
 ii11iIi1I . ok ( "GenieTv" , "[COLORred]Please press ok, Your download With Be Avaiilable Via The My Downloads Button[/COLOR]" , "[COLORblue]Tool Brought To You By Architects@Work[/COLOR]" )
 if 27 - 27: OoooooooOO
 if 45 - 45: i11iIiiIii + O0 + OOOo0 - Oo
def i11OOoo ( name , url , description ) :
 OOoOoo = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 i1111 = xbmcgui . DialogProgress ( )
 i1111 . create ( "Your Art Pack Is Downloading" , "Why not check out our website" , '' , 'Http://architects.x10host.com' )
 I1IiI11 = os . path . join ( OOoOoo , name )
 try :
  os . remove ( I1IiI11 )
 except :
  pass
 downloader . download ( url , I1IiI11 , i1111 )
 iIIiiiI = xbmc . translatePath ( os . path . join ( i1 ) )
 time . sleep ( 2 )
 i1111 . update ( 0 , "" , "Placing Your Art Please Wait" )
 print '======================================='
 print iIIiiiI
 print '======================================='
 extract . all ( I1IiI11 , iIIiiiI , i1111 )
 ii11iIi1I = xbmcgui . Dialog ( )
 ii11iIi1I . ok ( "GenieTv" , "[COLORred]Once complete your artwork will be stored in your Media folder, Accessible via the Homefolder, Enjoy[/COLOR]" )
 if 60 - 60: OOOo0 . O0oO
 if 34 - 34: OOOo0 % oO0o0ooO0 + o0oO0 * iIii1I11I1II1
def Ii11 ( url ) :
 Ooo0oOooo0 = OOO00O ( oOo0oooo00o ( 'aHR0cDovL2dlbmlldHYuYXJjaGl0ZWN0cy54MTBob3N0LmNvbS90ZXN0L3doLnR4dA==' ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 OOoOO0oo0ooO = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( Ooo0oOooo0 )
 for O00O0oOO00O00 , url , iiIiIIIiiI , iiI1IIIi , II11IiIi11 in OOoOO0oo0ooO :
  oOoOooOo0o0 ( O00O0oOO00O00 , url , 5 , iiIiIIIiiI , iiI1IIIi , II11IiIi11 )
 try :
  Ooo0oOooo0 = OOO00O ( IIiI1Ii + oooOOOOO + O0O0O0Oo ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
  OOoOO0oo0ooO = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( Ooo0oOooo0 )
  for O00O0oOO00O00 , url , iiIiIIIiiI , iiI1IIIi , II11IiIi11 in OOoOO0oo0ooO :
   oOoOooOo0o0 ( O00O0oOO00O00 , url , 5 , iiIiIIIiiI , iiI1IIIi , II11IiIi11 )
 except : pass
 OoOo ( 'movies' , 'INFO' )
 if 70 - 70: Ooo00oOo00o % OoOO + OoOO0ooOOoo0O / o00O0oo % O0
 if 100 - 100: OOooOOo + OoOO0ooOOoo0O * OOooOOo
def oOOo0OOOo00O ( url ) :
 Ooo0oOooo0 = OOO00O ( oOo0oooo00o ( 'aHR0cDovL2dlbmlldHYuYXJjaGl0ZWN0cy54MTBob3N0LmNvbS90ZXN0L3doLnR4dA==' ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 OOoOO0oo0ooO = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( Ooo0oOooo0 )
 for O00O0oOO00O00 , url , iiIiIIIiiI , iiI1IIIi , II11IiIi11 in OOoOO0oo0ooO :
  oOoOooOo0o0 ( O00O0oOO00O00 , url , 43 , iiIiIIIiiI , iiI1IIIi , II11IiIi11 )
 try :
  Ooo0oOooo0 = OOO00O ( IIiI1Ii + oooOOOOO + O0O0O0Oo ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
  OOoOO0oo0ooO = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( Ooo0oOooo0 )
  for O00O0oOO00O00 , url , iiIiIIIiiI , iiI1IIIi , II11IiIi11 in OOoOO0oo0ooO :
   oOoOooOo0o0 ( O00O0oOO00O00 , url , 43 , iiIiIIIiiI , iiI1IIIi , II11IiIi11 )
 except : pass
 OoOo ( 'movies' , 'INFO' )
 if 76 - 76: i11iIiiIii + OOooOOo / ii11ii1ii - Ooo00oOo00o - o00O0oo + ii11ii1ii
 if 51 - 51: iIii1I11I1II1 . o0oO0 + iIii1I11I1II1
def oOoOO ( name , url , description ) :
 OOoOoo = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 i1111 = xbmcgui . DialogProgress ( )
 i1111 . create ( "GenieTv" , "Downloading Content" , '' , 'Please Wait' )
 I1IiI11 = os . path . join ( OOoOoo , name + '.zip' )
 try :
  os . remove ( I1IiI11 )
 except :
  pass
 downloader . download ( url , I1IiI11 , i1111 )
 Ii1i1 = xbmc . translatePath ( os . path . join ( 'special://home' , 'addons' ) )
 time . sleep ( 2 )
 i1111 . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print Ii1i1
 print '======================================='
 extract . all ( I1IiI11 , Ii1i1 , i1111 )
 ii11iIi1I = xbmcgui . Dialog ( )
 ii11iIi1I . ok ( "GenieTv" , "Press ok to finish install" , "[COLOR yellow]Brought To You By Architects@Work[/COLOR]" )
 O0o ( )
 if 18 - 18: ii11ii1ii
 if 96 - 96: OoooooooOO + OoOO
def iiII1i11i ( name , url , description ) :
 OOoOoo = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 i1111 = xbmcgui . DialogProgress ( )
 i1111 . create ( "GenieTv" , "Downloading " , '' , 'Please Wait' )
 I1IiI11 = os . path . join ( OOoOoo , 'plugin.program.GenieTv.install' + '.zip' )
 try :
  os . remove ( I1IiI11 )
 except :
  pass
 downloader . download ( url , I1IiI11 , i1111 )
 Ii1i1 = xbmc . translatePath ( os . path . join ( 'special://' , 'home' ) )
 time . sleep ( 2 )
 i1111 . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print Ii1i1
 print '======================================='
 extract . all ( I1IiI11 , Ii1i1 , i1111 )
 ii11iIi1I = xbmcgui . Dialog ( )
 ii11iIi1I . ok ( "GenieTv" , "Press ok to force close kodi, if unsuccessful using windows Please kill kodi via taskmanager" , "[COLOR yellow]Brought To You By Architects@Work[/COLOR]" )
 IiIi ( )
 if 87 - 87: ii11ii1ii - ii11ii1ii - oO0o0ooO0 + OoOO
def OOooo ( name , url , description ) :
 OOoOoo = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 i1111 = xbmcgui . DialogProgress ( )
 i1111 . create ( "GenieTv" , "Downloading " , '' , 'Please Wait' )
 I1IiI11 = os . path . join ( OOoOoo , 'plugin.program.GenieTv.install' + '.zip' )
 try :
  os . remove ( I1IiI11 )
 except :
  pass
 downloader . download ( url , I1IiI11 , i1111 )
 Ii1i1 = xbmc . translatePath ( os . path . join ( 'special://' , 'home' ) )
 time . sleep ( 2 )
 i1111 . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print Ii1i1
 print '======================================='
 extract . all ( I1IiI11 , Ii1i1 , i1111 )
 ii11iIi1I = xbmcgui . Dialog ( )
 ii11iIi1I . ok ( "GenieTv" , "Please Disconnect The Power From Your Device. DO NOT EXIT CLEANLY VIA SHUTDOWN" , "[COLOR yellow]Brought To You By Architects@Work[/COLOR]" )
 if 31 - 31: OOooOOo % Ooo00oOo00o
 if 14 - 14: OoOO / OoOO % o0oO0
def ooOii ( name , url , description ) :
 Ii1i1 = xbmc . translatePath ( os . path . join ( 'special://' , 'home' ) )
 i1111 = xbmcgui . DialogProgress ( )
 I1IiI11 = os . path . join ( oo0o0O00 )
 time . sleep ( 2 )
 i1111 . create ( "GenieTv" , "Restoring" , '' , 'Please Wait' )
 print '======================================='
 print Ii1i1
 print '======================================='
 extract . all ( I1IiI11 , Ii1i1 , i1111 )
 ii11iIi1I = xbmcgui . Dialog ( )
 ii11iIi1I . ok ( "GenieTv" , "Please Disconnect The Power From Your Device. DO NOT EXIT CLEANLY VIA SHUTDOWN" , "[COLOR yellow]Brought To You By Architects@Work[/COLOR]" )
 if 82 - 82: I1IiI - Ooo00oOo00o % I1IiI * i11iIiiIii . OoOoOO00 % OoOoOO00
 if 54 - 54: o0000oOoOoO0o + o00O0oo
def IiIi ( ) :
 o00I1 = xbmcgui . Dialog ( ) . yesno ( 'Force Close Kodi' , 'You are about to close Kodi' , 'Would you like to continue?' , nolabel = 'No, Cancel' , yeslabel = 'Yes, Close' )
 if o00I1 == 0 :
  return
 elif o00I1 == 1 :
  pass
 O00 = II1I11i ( )
 print "Platform: " + str ( O00 )
 if O00 == 'osx' :
  print "############   try osx force close  #################"
  try : os . system ( 'killall -9 XBMC' )
  except : pass
  try : os . system ( 'killall -9 Kodi' )
  except : pass
  ii11iIi1I . ok ( "[COLOR=red][B]WARNING  !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu." , '' )
 elif O00 == 'linux' :
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
 elif O00 == 'android' :
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
 elif O00 == 'windows' :
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
  if 82 - 82: o0000oOoOoO0o + OoooooooOO - i1IIi . i1IIi
def II1I11i ( ) :
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
  if 6 - 6: OOooOOo / o0000oOoOoO0o / OoOoOO00
  if 27 - 27: OoOO0ooOOoo0O * o0oO0 . O0oO % IIII * IIII . i1IIi
  if 72 - 72: OoOO0ooOOoo0O % ii11ii1ii + Ooo00oOo00o / OoOO + IIII
def I1I1i ( url ) :
 i1111 . create ( "[COLOR=green]GenieTv[/COLOR]" , "Renaming paths..." , '' , 'Please Wait' )
 for I1IIIiIiIi , OOoO0 , OO0Oooo0oOO0O in os . walk ( url ) :
  for file in OO0Oooo0oOO0O :
   if file . endswith ( ".xml" ) :
    i1111 . update ( 0 , "Fixing" , file , 'Please Wait' )
    O0i1II1Iiii1I11 = open ( ( os . path . join ( I1IIIiIiIi , file ) ) ) . read ( )
    IIIII1 = O0i1II1Iiii1I11 . replace ( iI111I11I1I1 , 'special://home/' )
    II1I = open ( ( os . path . join ( I1IIIiIiIi , file ) ) , mode = 'w' )
    II1I . write ( str ( IIIII1 ) )
    II1I . close ( )
 IiIi ( )
 if 5 - 5: o00O0oo
def iIi1i1iIi1iI ( ) :
 iI1i11 = OoOOoooOO0O ( oOo0oooo00o ( 'aHR0cDovL3d3dy5saXN0ZW5saXZlLmV1L3VrLmh0bWw=' ) )
 OOoOO0oo0ooO = re . compile ( '<tr>.+?<td><a href=".+?"><b>(.+?)</b>.+?<td><a href="(.+?)">' , re . DOTALL ) . findall ( iI1i11 )
 for O00O0oOO00O00 , O0o0O00Oo0o0 in OOoOO0oo0ooO :
  iiIi1iI1iIii ( O00O0oOO00O00 , O0o0O00Oo0o0 , 222 , oOOoO0 + 'radio.png' )
  if 68 - 68: OoOO0ooOOoo0O
def OooO0oo ( ) :
 iI1i11 = OoOOoooOO0O ( oOo0oooo00o ( 'aHR0cDovL3d3dy50b29uamV0LmNvbS8=' ) )
 OOoOO0oo0ooO = re . compile ( '<a href="(.+?)" style="font-size:.8em;">(.+?)</a>' ) . findall ( iI1i11 )
 for O0o0O00Oo0o0 , O00O0oOO00O00 in OOoOO0oo0ooO :
  Oo0o0O00 ( '[COLORgreen]' + O00O0oOO00O00 + '[/COLOR]' , 'http://www.toonjet.com/' + O0o0O00Oo0o0 , 8051 , oOOoO0 + 'classictoons.png' )
def o0o0oOoOO0O ( url ) :
 iI1i11 = OoOOoooOO0O ( url )
 OOoOO0oo0ooO = re . compile ( '<a href="(.+?)"><img src="(.+?)"' ) . findall ( iI1i11 )
 i1ii1II1ii = re . compile ( '<a href="(.+?)">.+?</a></td></tr></table>' ) . findall ( iI1i11 )
 for url , iII111Ii in OOoOO0oo0ooO :
  if 'ol.gif' in iII111Ii :
   pass
  elif 'link_block_' in iII111Ii :
   pass
  elif '.png' in iII111Ii :
   pass
  else :
   Oo0o0O00 ( ( iII111Ii ) . replace ( 'http://www.toonjet.com/images/icons/' , '' ) . replace ( 'images/icons/' , '' ) . replace ( '.jpg' , '' ) . replace ( '_icon' , '' ) . replace ( '_' , ' ' ) , 'http://www.toonjet.com/' + url , 8052 , oOOoO0 + 'vod.png' )
 for url in i1ii1II1ii :
  Oo0o0O00 ( 'NEXT PAGE' , 'http://www.toonjet.com/' + url , 8051 , oOOoO0 + 'documentary.png' )
def Ooo00OoOOO ( url ) :
 iI1i11 = OoOOoooOO0O ( url )
 OOoOO0oo0ooO = re . compile ( '<iframe width="640" height="480" src="(.+?)" frameborder="0" allowfullscreen></iframe>' ) . findall ( iI1i11 )
 for url in OOoOO0oo0ooO :
  iiIi1iI1iIii ( '[COLORgreen]PLAY[/COLOR]' , ( url ) . replace ( 'http://www.youtube.com/embed/' , '' ) . replace ( '?autoplay=0' , '' ) , 8043 , oOOoO0 + 'classictoons.png' )
  if 98 - 98: iIii1I11I1II1 * ii11ii1ii * OoOO0ooOOoo0O + o0oO0 % i11iIiiIii % O0
  if 27 - 27: O0
  if 79 - 79: OOooOOo - o0000oOoOoO0o + OOooOOo . OoOO
def ii1III11 ( ) :
 o00oOO0o = OoOOoooOO0O ( oOo0oooo00o ( 'aHR0cDovL3dhdGNoY2FydG9vbnNvbmxpbmUuZXUv' ) )
 OOoOO0oo0ooO = re . compile ( 'src="(.+?)" style=.+?<a class="bigChar" href="(.+?)">(.+?)</a>.+?<p>(.+?)</p>' , re . DOTALL ) . findall ( o00oOO0o )
 for O0o0O00Oo0o0 , I1iiIIIi11 , O00O0oOO00O00 in OOoOO0oo0ooO :
  oOoOooOo0o0 ( '[COLORgreen]' + O00O0oOO00O00 + '[/COLOR]' , 'http://kisscartoon.me' + O0o0O00Oo0o0 , 21005 , img , '' , I1iiIIIi11 )
  if 12 - 12: OoooooooOO % OOooOOo * o0000oOoOoO0o % iIii1I11I1II1 / o00O0oo
  if 27 - 27: i11iIiiIii % OoOoOO00 % o0000oOoOoO0o . O0 - Oo + I1IiI
def ooO0o ( ) :
 Oo0o0O00 ( '[COLORgreen]CARTOONS[/COLOR]' , '' , 20001 , oOOoO0 + 'ORIGINCARTOON.png' )
 Oo0o0O00 ( '[COLORgreen]ANIME[/COLOR]' , 'https://kissanime.to/AnimeList' , 20001 , oOOoO0 + 'ORIGINCARTOON.png' )
 if 51 - 51: IIII
def ii11I1 ( ) :
 Oo0o0O00 ( '[COLORgreen]BY NAME[/COLOR]' , 'http://kisscartoon.me/CartoonList' , 20002 , oOOoO0 + 'ORIGINCARTOON.png' )
 Oo0o0O00 ( '[COLORgreen]BY GENRE[/COLOR]' , 'http://kisscartoon.me/CartoonList' , 20003 , oOOoO0 + 'ORIGINCARTOON.png' )
 if 75 - 75: Ooo00oOo00o / OoOoOO00 % O0
def Ii111iIi1iIi ( url ) :
 o00oOO0o = cloudflare . source ( url )
 OOoOO0oo0ooO = re . compile ( 'href="(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( o00oOO0o )
 for url , O00O0oOO00O00 in OOoOO0oo0ooO :
  if '?c=' in url :
   Oo0o0O00 ( '[COLORgreen]' + O00O0oOO00O00 + '[/COLOR]' , 'http://kisscartoon.me' + url , 20004 , oOOoO0 + 'ORIGINCARTOON.png' )
   if 21 - 21: OoOO / ii11ii1ii + o00O0oo + OoooooooOO
def OoOoI1iI11iIiIi1 ( url ) :
 o00oOO0o = cloudflare . source ( url )
 OOoOO0oo0ooO = re . compile ( 'href="(.+?)" title="(.+?)">/n(.+?)</a><br/>' , re . DOTALL ) . findall ( o00oOO0o )
 for url , I1iiIIIi11 , O00O0oOO00O00 in OOoOO0oo0ooO :
  if 'Genre' in url :
   Oo0o0O00 ( '[COLORgreen]' + O00O0oOO00O00 + '[/COLOR]' , 'http://kisscartoon.me' + url , 20004 , oOOoO0 + 'ORIGINCARTOON.png' )
   if 72 - 72: O0oO
def OO0ooo0oOO ( url ) :
 o00oOO0o = cloudflare . source ( url )
 OOoOO0oo0ooO = re . compile ( 'src="(.+?)" style=.+?<a class="bigChar" href="(.+?)">(.+?)</a>.+?<p>(.+?)</p>' , re . DOTALL ) . findall ( o00oOO0o )
 for url , I1iiIIIi11 , O00O0oOO00O00 in OOoOO0oo0ooO :
  oOoOooOo0o0 ( '[COLORgreen]' + O00O0oOO00O00 + '[/COLOR]' , 'http://kisscartoon.me' + url , 20005 , img , '' , I1iiIIIi11 )
  if 97 - 97: OOOo0 / oO0o0ooO0
def Oooo0 ( url ) :
 o00oOO0o = cloudflare . source ( url )
 OOoOO0oo0ooO = re . compile ( '<img width="120" height="165" src="(.+?)" style=.+?<a class="bigChar" href="(.+?)">(.+?)</a>.+?<p>(.+?)</p>' , re . DOTALL ) . findall ( o00oOO0o )
 for url , I1iiIIIi11 , O00O0oOO00O00 in OOoOO0oo0ooO :
  oOoOooOo0o0 ( '[COLORgreen]' + O00O0oOO00O00 + '[/COLOR]' , 'http://kisscartoon.me' + url , 20005 , img , '' , I1iiIIIi11 )
  if 59 - 59: OoooooooOO
  if 47 - 47: o0oO0 - OOOo0 / OoOoOO00
  if 12 - 12: OoOO0ooOOoo0O
  if 83 - 83: oO0o0ooO0 . O0 / Oo / OoOO0ooOOoo0O - OoOoOO00
  if 100 - 100: Ooo00oOo00o
def II1i ( ) :
 if 2 - 2: iIii1I11I1II1 * Oo % OoOO - OoOoOO00 - oO0o0ooO0
 oOoOooOo0o0 ( '[COLORgreen]Cartoons[/COLOR]' , '' , 10004 , oOOoO0 + 'ORIGINCARTOON.png' , OOooO0OOoo , '' )
 oOoOooOo0o0 ( '[COLORgreen]Search Cartoons[/COLOR]' , '' , 10005 , oOOoO0 + 'ORIGINCARTOON.png' , OOooO0OOoo , '' )
 if 3 - 3: O0oO
def i1iiIiI1Ii1i ( ) :
 oooo000 = Oo0o0000o0o0 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 iiII1i1 = oooo000 . lower ( )
 o00oOO0o = OOO00O ( oOo0oooo00o ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2NhcnRvb24=' ) )
 OOoOO0oo0ooO = re . compile ( '<td><a href="(.+?)">(.+)</a></td>' ) . findall ( o00oOO0o )
 for O0o0O00Oo0o0 , O00O0oOO00O00 in OOoOO0oo0ooO :
  if oooo000 in O00O0oOO00O00 . lower ( ) :
   if 'Dad!' in O00O0oOO00O00 :
    pass
   elif 'Family Guy' in O00O0oOO00O00 :
    pass
   elif '2 Stupid' in O00O0oOO00O00 :
    pass
   elif 'The Zelfs' in O00O0oOO00O00 :
    pass
   elif 'A Clone' in O00O0oOO00O00 :
    pass
   elif 'A.T.O.M' in O00O0oOO00O00 :
    pass
   elif 'Almost Naked' in O00O0oOO00O00 :
    pass
   elif 'Angry Kid' in O00O0oOO00O00 :
    pass
   elif 'Annoying Orange' in O00O0oOO00O00 :
    pass
   elif 'Aqua Teen' in O00O0oOO00O00 :
    pass
   elif 'Assy Mcgee' in O00O0oOO00O00 :
    pass
   elif 'Astroblast' in O00O0oOO00O00 :
    pass
   elif 'Atomic Betty' in O00O0oOO00O00 :
    pass
   elif 'Axe Cop' in O00O0oOO00O00 :
    pass
   elif 'Baby Playpen' in O00O0oOO00O00 :
    pass
   elif 'Beavis and Butt' in O00O0oOO00O00 :
    pass
   elif 'Celebrity Deathmatch' in O00O0oOO00O00 :
    pass
   elif 'Clerks The' in O00O0oOO00O00 :
    pass
   elif 'Crapston Villas' in O00O0oOO00O00 :
    pass
   elif 'Duckman:' in O00O0oOO00O00 :
    pass
   elif 'Stripperella' in O00O0oOO00O00 :
    pass
   elif 'Vixen' in O00O0oOO00O00 :
    pass
   else :
    oOoOooOo0o0 ( '[COLORgreen]' + O00O0oOO00O00 + '[/COLOR]' , O0o0O00Oo0o0 , 10006 , oOOoO0 + 'ORIGINCARTOON.png' , OOooO0OOoo , '' )
  xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 22 - 22: IIII / i11iIiiIii
def oOOoo ( ) :
 iI1i11 = OOO00O ( oOo0oooo00o ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2NhcnRvb24=' ) )
 OOoOO0oo0ooO = re . compile ( '<td><a href="(.+?)">(.+)</a></td>' ) . findall ( iI1i11 )
 for O0o0O00Oo0o0 , O00O0oOO00O00 in OOoOO0oo0ooO :
  if 'Dad!' in O00O0oOO00O00 :
   pass
  elif 'Family Guy' in O00O0oOO00O00 :
   pass
  elif '2 Stupid' in O00O0oOO00O00 :
   pass
  elif 'The Zelfs' in O00O0oOO00O00 :
   pass
  elif 'A Clone' in O00O0oOO00O00 :
   pass
  elif 'A.T.O.M' in O00O0oOO00O00 :
   pass
  elif 'Almost Naked' in O00O0oOO00O00 :
   pass
  elif 'Angry Kid' in O00O0oOO00O00 :
   pass
  elif 'Annoying Orange' in O00O0oOO00O00 :
   pass
  elif 'Aqua Teen' in O00O0oOO00O00 :
   pass
  elif 'Assy Mcgee' in O00O0oOO00O00 :
   pass
  elif 'Astroblast' in O00O0oOO00O00 :
   pass
  elif 'Atomic Betty' in O00O0oOO00O00 :
   pass
  elif 'Axe Cop' in O00O0oOO00O00 :
   pass
  elif 'Baby Playpen' in O00O0oOO00O00 :
   pass
  elif 'Beavis and Butt' in O00O0oOO00O00 :
   pass
  elif 'Celebrity Deathmatch' in O00O0oOO00O00 :
   pass
  elif 'Clerks The' in O00O0oOO00O00 :
   pass
  elif 'Crapston Villas' in O00O0oOO00O00 :
   pass
  elif 'Duckman:' in O00O0oOO00O00 :
   pass
  elif 'Stripperella' in O00O0oOO00O00 :
   pass
  elif 'Vixen' in O00O0oOO00O00 :
   pass
  else :
   oOoOooOo0o0 ( '[COLORgreen]' + O00O0oOO00O00 + '[/COLOR]' , O0o0O00Oo0o0 , 10006 , oOOoO0 + 'ORIGINCARTOON.png' , OOooO0OOoo , '' )
 xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 14 - 14: OOooOOo * OoOO
def O0OOO0OOooo00 ( url ) :
 iI1i11 = OOO00O ( url )
 i1ii1II1ii = re . compile ( '<img src="(.+?)" id="series_image" width="250" height="370" alt=".+?" />' ) . findall ( iI1i11 )
 for iII111Ii in i1ii1II1ii :
  I111iIi1 = iII111Ii
 oo00O00oO000o = re . compile ( '<li><a href="(.+?)">Next</a></li>' ) . findall ( iI1i11 )
 for url in oo00O00oO000o :
  oOoOooOo0o0 ( '[COLORgreen]NEXT PAGE[/COLOR]' , url , 10006 , I111iIi1 , OOooO0OOoo , '' )
 OOoOO0oo0ooO = re . compile ( '&nbsp;<a href="(.+?)">(.+?)</a>' ) . findall ( iI1i11 )
 for url , O00O0oOO00O00 in OOoOO0oo0ooO :
  iiIi1iI1iIii ( '[COLORgreen]' + O00O0oOO00O00 + '[/COLOR]' , url , 10007 , I111iIi1 )
  if 71 - 71: ii11ii1ii - o0oO0 / I1IiI * I1IiI / i1IIi . i1IIi
  if 53 - 53: O0oO
 xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 21 - 21: o0000oOoOoO0o
def OoO00 ( url , IMAGE ) :
 iI1i11 = OOO00O ( url )
 OOoOO0oo0ooO = re . compile ( '"playlist">(.+?)</span></div><div><iframe src="(.+?)"' ) . findall ( iI1i11 )
 for O00O0oOO00O00 , url in OOoOO0oo0ooO :
  print O00O0oOO00O00 + '     ' + url
  if 'easy' in url :
   OO0Ooooo000Oo ( url )
   if 97 - 97: o00O0oo * ii11ii1ii / OOOo0 / iIii1I11I1II1 % o0000oOoOoO0o
   if 95 - 95: o0oO0 + i11iIiiIii * O0oO - i1IIi * O0oO - iIii1I11I1II1
  xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 75 - 75: OoooooooOO * IIII
def OO0Ooooo000Oo ( url ) :
 iI1i11 = OOO00O ( url )
 OOoOO0oo0ooO = re . compile ( "url: '(.+?)'," ) . findall ( iI1i11 )
 for url in OOoOO0oo0ooO :
  I1Iiiiiii ( url )
  if 39 - 39: IIII * Oo + iIii1I11I1II1 - IIII + OoOO0ooOOoo0O
  if 69 - 69: O0
  if 85 - 85: o0oO0 / O0
def iI1iIIIi1i ( ) :
 if 89 - 89: iIii1I11I1II1
 oOoOooOo0o0 ( '[COLORgreen]Stand Up[/COLOR]' , '' , 10014 , oOOoO0 + 'ORIGINSTANDUP.png' , OOooO0OOoo , '' )
 oOoOooOo0o0 ( '[COLORgreen]Search Comedian[/COLOR]' , '' , 10015 , oOOoO0 + 'ORIGINSTANDUP.png' , OOooO0OOoo , '' )
 oOoOooOo0o0 ( '[COLORgreen]Others[/COLOR]' , '' , 10017 , oOOoO0 + 'ORIGINSTANDUP.png' , OOooO0OOoo , '' )
 if 21 - 21: o0000oOoOoO0o % o0000oOoOoO0o
def iiI1 ( ) :
 o00oOO0o = OOO00O ( ( oOo0oooo00o ( 'aHR0cDovL2JhY2syYmFzaWNzYnVpbGQuY28udWsvdGVzdC9zdGFuZHVwbGlzdC5waHA=' ) ) )
 OOoOO0oo0ooO = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( o00oOO0o )
 for O0o0O00Oo0o0 , iII111Ii , O00O0oOO00O00 in OOoOO0oo0ooO :
  iiIi1iI1iIii ( '[COLORgreen]' + O00O0oOO00O00 + '[/COLOR]' , O0o0O00Oo0o0 , 222 , iII111Ii )
  if 16 - 16: OoOoOO00 + OoOO - OoooooooOO
def ii1iI ( ) :
 oooo000 = Oo0o0000o0o0 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 iiII1i1 = oooo000 . lower ( )
 o00oOO0o = OOO00O ( ( oOo0oooo00o ( 'aHR0cDovL3d3dy5jb3VjaHRyaXBwZXIuY29tL2ZvcnVtMi9wYWdlLnBocD9wYWdlPTM=' ) ) )
 IIi = re . compile ( '<tr>.+?<td width=".+?" align=".+?">.+?<img border=".+?" src="..(.+?)" width=".+?" height=".+?"></td>.+?<td width=".+?" valign=".+?" align=".+?"><font size=".+?">(.+?)</font></td>.+?<td width=".+?">(.+?)</td>' , re . DOTALL ) . findall ( o00oOO0o )
 for iII111Ii , ooOooo0 , iIiiiI1IiI1I1 in IIi :
  for oooo000 in ooOooo0 :
   print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< img >>>>>>>>>>>>>>>>>>>>>>>>>>'
   oO0OO0 = re . compile ( '<a href="(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( iIiiiI1IiI1I1 )
   for O0o0O00Oo0o0 , O00O0oOO00O00 in oO0OO0 :
    if 'tube' in O0o0O00Oo0o0 :
     pass
    elif 'stage' in O0o0O00Oo0o0 :
     iiIi1iI1iIii ( '[COLORgreen]' + ooOooo0 + '   -   ' + O00O0oOO00O00 + '[/COLOR]' , ( O0o0O00Oo0o0 ) . replace ( '" target="_blank' , '' ) , 10016 , 'http://couchtripper.com/' + iII111Ii , )
    elif 'vee' in O0o0O00Oo0o0 :
     pass
     if 82 - 82: IIII - IIII + I1IiI
def II111Ii1i1 ( ) :
 o00oOO0o = OOO00O ( ( oOo0oooo00o ( 'aHR0cDovL3d3dy5jb3VjaHRyaXBwZXIuY29tL2ZvcnVtMi9wYWdlLnBocD9wYWdlPTM=' ) ) )
 IIi = re . compile ( '<tr>.+?<td width=".+?" align=".+?">.+?<img border=".+?" src="..(.+?)" width=".+?" height=".+?"></td>.+?<td width=".+?" valign=".+?" align=".+?"><font size=".+?">(.+?)</font></td>.+?<td width=".+?">(.+?)</td>' , re . DOTALL ) . findall ( o00oOO0o )
 for iII111Ii , ooOooo0 , iIiiiI1IiI1I1 in IIi :
  oO0OO0 = re . compile ( '<a href="(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( iIiiiI1IiI1I1 )
  for O0o0O00Oo0o0 , O00O0oOO00O00 in oO0OO0 :
   if 'tube' in O0o0O00Oo0o0 :
    pass
   elif 'stage' in O0o0O00Oo0o0 :
    iiIi1iI1iIii ( '[COLORgreen]' + ooOooo0 + '   -   ' + O00O0oOO00O00 + '[/COLOR]' , ( O0o0O00Oo0o0 ) . replace ( '" target="_blank' , '' ) , 10016 , 'http://couchtripper.com/' + iII111Ii )
   elif 'vee' in O0o0O00Oo0o0 :
    pass
    if 98 - 98: Ooo00oOo00o . Ooo00oOo00o * OoOO * OoOoOO00 * O0oO
    if 92 - 92: Oo
 xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 40 - 40: I1IiI / IIII
def OOOoO000 ( url ) :
 o00oOO0o = OOO00O ( url )
 print '>>>>>>>>>>>>>>>>>>>>>>>>' + url + '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'
 oOOOO = re . compile ( "url\[.+?\] = '(.+?)';" ) . findall ( o00oOO0o )
 print '>>>>>>>>>>>>>>>>>>>>>>>' + ( str ( oOOOO ) ) + '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
 for url in oOOOO :
  I1Iiiiiii ( ( url ) . replace ( '[' , '' ) . replace ( ']' , '' ) . replace ( '\'' , '' ) )
  if 49 - 49: OoOoOO00 . OoOO . i11iIiiIii % IIII
  if 34 - 34: O0oO % IIII
  if 3 - 3: OoOoOO00 / OoOO0ooOOoo0O + IIII . o0oO0 . Ooo00oOo00o
  if 83 - 83: OoOO + OoooooooOO
  if 22 - 22: o00O0oo % oO0o0ooO0 * OoooooooOO - OOooOOo / iIii1I11I1II1
  if 86 - 86: OoooooooOO . oO0o0ooO0 % I1IiI / o0000oOoOoO0o * oO0o0ooO0 / OOooOOo
  if 64 - 64: i11iIiiIii
def I1II ( ) :
 if 17 - 17: OoOO0ooOOoo0O % Oo / ii11ii1ii . IIII * OoOO0ooOOoo0O - OoOoOO00
 i1i1IIii1i1 ( '[COLOR darkgoldenrod]Open Pandora\'s Box[/COLOR]' , '' , 10029 , 'https://encrypted-tbn1.gstatic.com/images?q=tbn%3AANd9GcTQ9r4TA8yIw9ggxuwsHxWojo6tPVfgTe8QIOxOQwzNR2TavtCi6Q' , OOooO0OOoo , '' )
 i1i1IIii1i1 ( '[COLOR darkgoldenrod]Search[/COLOR]' , '' , 10026 , 'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png' , OOooO0OOoo , '' )
 if 65 - 65: OOOo0 + I1IiI / OoOO0ooOOoo0O
 OoOo ( 'movies' , 'MAIN' )
 if 83 - 83: OOooOOo . oO0o0ooO0 - Oo
def Ooo0O ( ) :
 i1i1IIii1i1 ( 'Search Pandoras Films' , '' , 10027 , oOOoO0 + 'PANDORASBOX.png' , OOooO0OOoo , '' )
 i1i1IIii1i1 ( 'Search Pandoras TV' , '' , 10028 , oOOoO0 + 'PANDORASBOX.png' , OOooO0OOoo , '' )
 if 87 - 87: IIII % OoOoOO00
 OoOo ( 'movies' , 'MAIN' )
def I11II11I1iII ( ) :
 if 4 - 4: OoooooooOO - i1IIi % o00O0oo - OoOO0ooOOoo0O * OOooOOo
 oooo000 = Oo0o0000o0o0 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 iiII1i1 = oooo000 . lower ( )
 Ooooo00o0OoO = [ 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' ]
 if 75 - 75: OOOo0 % OoOoOO00
 for I1I1i1I in Ooooo00o0OoO :
  oo0oo = Base_Pand + I1I1i1I + CAT
  o00oOO0o = OOO00O ( oo0oo )
  OOoOO0oo0ooO = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( o00oOO0o )
  for O0o0O00Oo0o0 , iiIiIIIiiI , IIi11IIiIii1 , iiI1IIIi , O00O0oOO00O00 in OOoOO0oo0ooO :
   if oooo000 in O00O0oOO00O00 . lower ( ) :
    I1iIII1 ( O00O0oOO00O00 , O0o0O00Oo0o0 , 222 , iiIiIIIiiI , iiI1IIIi , IIi11IIiIii1 )
    if 39 - 39: OoooooooOO
    OoOo ( 'movies' , 'MAIN' )
    xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
    if 38 - 38: OOOo0
    if 84 - 84: OoOO % i1IIi
def oOO ( ) :
 if 17 - 17: OoOoOO00 / ii11ii1ii % IIII + OOOo0 * O0oO
 oooo000 = Oo0o0000o0o0 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 iiII1i1 = oooo000 . lower ( )
 Ooooo00o0OoO = [ 'a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' , 'p' , 'q' , 'r' , 's' , 't' , 'u' , 'v' , 'w' , 'x' , 'y' , 'z' ]
 if 36 - 36: O0oO * Ooo00oOo00o
 for I1I1i1I in Ooooo00o0OoO :
  I1I = Base_Pand + I1I1i1I + CAT
  o00oOO0o = OOO00O ( I1I )
  OOoOO0oo0ooO = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( o00oOO0o )
  for O00O0oOO00O00 , IIi11IIiIii1 , O0o0O00Oo0o0 , iII111Ii , iiI1IIIi , ii1iIi1II in OOoOO0oo0ooO :
   if oooo000 in O00O0oOO00O00 . lower ( ) :
    i1i1IIii1i1 ( O00O0oOO00O00 , O0o0O00Oo0o0 , ii1iIi1II , iII111Ii , iiI1IIIi , IIi11IIiIii1 )
    if 2 - 2: Oo + I1IiI - OoOO0ooOOoo0O . OOOo0 - OoOO0ooOOoo0O
    OoOo ( 'movies' , 'MAIN' )
    xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
    if 67 - 67: iIii1I11I1II1 - oO0o0ooO0
    if 11 - 11: iIii1I11I1II1 . OoooooooOO . OoOoOO00 / i1IIi - o0000oOoOoO0o
def ii1ii11 ( ) :
 if 84 - 84: O0 . o0000oOoOoO0o - OoOoOO00 . o0oO0 / OoOoOO00
 iI1i11 = OOO00O ( oOo0oooo00o ( 'aHR0cDovL3NlZWR1cmdyZWVkLngxMGhvc3QuY29tL29yaWdpbi9zcG9uZ2VtYWluLnBocA==' ) )
 OOoOO0oo0ooO = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( iI1i11 )
 for O00O0oOO00O00 , IIi11IIiIii1 , O0o0O00Oo0o0 , iII111Ii , iiI1IIIi , ii1iIi1II in OOoOO0oo0ooO :
  i1i1IIii1i1 ( O00O0oOO00O00 , O0o0O00Oo0o0 , ii1iIi1II , iII111Ii , iiI1IIIi , IIi11IIiIii1 )
  OoOo ( 'movies' , 'MAIN' )
def iii1 ( url ) :
 if 32 - 32: o00O0oo . IIII . OoooooooOO - Ooo00oOo00o + OoOO
 xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
 ooO0oO00O0o = ( '%s%s' % ( ooOO00oOOo000 , url ) )
 Ooo0oOooo0 = OOO00O ( url )
 OOoOO0oo0ooO = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( Ooo0oOooo0 )
 for url , iiIiIIIiiI , IIi11IIiIii1 , IIii11II11II1 , O00O0oOO00O00 in OOoOO0oo0ooO :
  I1iIII1 ( O00O0oOO00O00 , url , 222 , iiIiIIIiiI , IIii11II11II1 , IIi11IIiIii1 )
  if 10 - 10: OOOo0 / Oo % ii11ii1ii * o0oO0
  OoOo ( 'movies' , 'MAIN' )
  if 6 - 6: oO0o0ooO0 . IIII * I1IiI . i1IIi
  xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 98 - 98: i1IIi
  if 65 - 65: I1IiI / Ooo00oOo00o % IIII
def iIiIIii ( url ) :
 if 61 - 61: OOooOOo / OoOO0ooOOoo0O / Oo * O0
 iI1i11 = OOO00O ( url )
 OOoOO0oo0ooO = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( iI1i11 )
 for O00O0oOO00O00 , IIi11IIiIii1 , url , iII111Ii , iiI1IIIi , ii1iIi1II in OOoOO0oo0ooO :
  i1i1IIii1i1 ( O00O0oOO00O00 , url , ii1iIi1II , iII111Ii , iiI1IIIi , IIi11IIiIii1 )
  if 23 - 23: OoOO - OoOO0ooOOoo0O + o0000oOoOoO0o
  OoOo ( 'movies' , 'MAIN' )
  if 12 - 12: OOOo0 / o0oO0 % OOooOOo / i11iIiiIii % OoooooooOO
  if 15 - 15: iIii1I11I1II1 % OoooooooOO - Oo * o00O0oo + o0000oOoOoO0o
 xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 11 - 11: oO0o0ooO0 * o00O0oo - I1IiI
def I1iIII1 ( name , url , mode , iconimage , fanart , description ) :
 if 66 - 66: I1IiI . i11iIiiIii - oO0o0ooO0 * OOooOOo + OoooooooOO * ii11ii1ii
 oO0OO0O00Oo = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 Ii1111IiIi = True
 II1I1iiIII1I1 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 II1I1iiIII1I1 . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 II1I1iiIII1I1 . setProperty ( "Fanart_Image" , fanart )
 Ii1111IiIi = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = oO0OO0O00Oo , listitem = II1I1iiIII1I1 , isFolder = False )
 return Ii1111IiIi
 if 85 - 85: oO0o0ooO0 * OOooOOo
def i1i1IIii1i1 ( name , url , mode , iconimage , fanart , description ) :
 if 3 - 3: OoOO0ooOOoo0O
 oO0OO0O00Oo = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 Ii1111IiIi = True
 II1I1iiIII1I1 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 II1I1iiIII1I1 . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 II1I1iiIII1I1 . setProperty ( "Fanart_Image" , fanart )
 Ii1111IiIi = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = oO0OO0O00Oo , listitem = II1I1iiIII1I1 , isFolder = True )
 return Ii1111IiIi
if 20 - 20: OoOoOO00 . oO0o0ooO0 / OoOoOO00 % i11iIiiIii % oO0o0ooO0
if 11 - 11: IIII % ii11ii1ii % o00O0oo / OoOoOO00 % O0oO - Oo
if 96 - 96: ii11ii1ii / OoOoOO00 . o00O0oo - oO0o0ooO0 * o0000oOoOoO0o * OoOO
if 76 - 76: o00O0oo - OoOoOO00 * OoOO0ooOOoo0O / OoooooooOO
if 18 - 18: Ooo00oOo00o + iIii1I11I1II1 - OoOoOO00 - OOOo0
if 71 - 71: OoooooooOO
if 33 - 33: O0oO
if 62 - 62: ii11ii1ii + o00O0oo + i1IIi / OoooooooOO
if 7 - 7: OOooOOo + i1IIi . OOOo0 / Oo
if 22 - 22: o0oO0 - o0oO0 % OoOO0ooOOoo0O . O0oO + OoOO
if 63 - 63: OOOo0 % O0oO * OOooOOo + O0oO / Oo % oO0o0ooO0
if 45 - 45: IIII
if 20 - 20: OoooooooOO * OOooOOo * O0 . OoOO0ooOOoo0O
if 78 - 78: iIii1I11I1II1 + o0000oOoOoO0o - o00O0oo * O0oO - OoooooooOO % I1IiI
if 34 - 34: O0
def OooOOOo0 ( string ) :
 if IIiiiiiiIi1I1 == 'true' :
  xbmc . log ( "[addon.live.GenieTV-%s]: %s" % ( addon_version , string ) )
  if 54 - 54: o00O0oo - o0000oOoOoO0o - O0oO . iIii1I11I1II1
def o0OIIiI1I1 ( name , url , iconimage , fanart , mode , playlist = None , regexs = None ) :
 I11I1IIiiII1 = [ ]
 try :
  if 31 - 31: OOOo0 * OoOO + OoooooooOO - oO0o0ooO0 / OoooooooOO
  name = name . encode ( 'utf-8' , 'ignore' )
 except :
  pass
 if os . path . exists ( iIi1ii1I1 ) == False :
  OooOOOo0 ( 'Making Favorites File' )
  I11I1IIiiII1 . append ( ( name , url , iconimage , fanart , mode , playlist , regexs ) )
  O0i1II1Iiii1I11 = open ( iIi1ii1I1 , "w" )
  O0i1II1Iiii1I11 . write ( json . dumps ( I11I1IIiiII1 ) )
  O0i1II1Iiii1I11 . close ( )
 else :
  OooOOOo0 ( 'Appending Favorites' )
  O0i1II1Iiii1I11 = open ( iIi1ii1I1 ) . read ( )
  I111IIiii1Ii = json . loads ( O0i1II1Iiii1I11 )
  I111IIiii1Ii . append ( ( name , url , iconimage , fanart , mode ) )
  IIIII1 = open ( iIi1ii1I1 , "w" )
  IIIII1 . write ( json . dumps ( I111IIiii1Ii ) )
  IIIII1 . close ( )
  if 13 - 13: OoOO . OOOo0 * OoOO + OOOo0
  if 59 - 59: OOOo0 + i11iIiiIii + i1IIi / o0000oOoOoO0o
def I11iIiI1 ( ) :
 oo0oooOo = json . loads ( open ( iIi1ii1I1 ) . read ( ) )
 o0OO0O0Oo = len ( oo0oooOo )
 for OOOOO in oo0oooOo :
  O00O0oOO00O00 = OOOOO [ 0 ]
  O0o0O00Oo0o0 = OOOOO [ 1 ]
  iiIiIIIiiI = OOOOO [ 2 ]
  try :
   OOoOOo0O00O = OOOOO [ 3 ]
   if OOoOOo0O00O == None :
    raise
  except :
   if o0oOoO00o . getSetting ( 'use_thumb' ) == "true" :
    OOoOOo0O00O = iiIiIIIiiI
   else :
    OOoOOo0O00O = iiI1IIIi
  try : iiIii1I = OOOOO [ 5 ]
  except : iiIii1I = None
  try : i1I11iIiII = OOOOO [ 6 ]
  except : i1I11iIiII = None
  if 66 - 66: Oo - OOooOOo * IIII + I1IiI + OOooOOo - iIii1I11I1II1
  if OOOOO [ 4 ] == 0 :
   oOoOooOo0o0 ( O00O0oOO00O00 , O0o0O00Oo0o0 , '' , iiIiIIIiiI , iiI1IIIi , '' , 'fav' )
  else :
   oOoOooOo0o0 ( O00O0oOO00O00 , O0o0O00Oo0o0 , OOOOO [ 4 ] , iiIiIIIiiI , iiI1IIIi , '' , 'fav' )
   if 17 - 17: OoOO
def i1ii11 ( name ) :
 I111IIiii1Ii = json . loads ( open ( iIi1ii1I1 ) . read ( ) )
 for ii1i in range ( len ( I111IIiii1Ii ) ) :
  if I111IIiii1Ii [ ii1i ] [ 0 ] == name :
   del I111IIiii1Ii [ ii1i ]
   IIIII1 = open ( iIi1ii1I1 , "w" )
   IIIII1 . write ( json . dumps ( I111IIiii1Ii ) )
   IIIII1 . close ( )
   break
 xbmc . executebuiltin ( "XBMC.Container.Refresh" )
 if 5 - 5: OoOO . ii11ii1ii . OoOoOO00 . OoooooooOO
 if 96 - 96: i11iIiiIii - OoOO0ooOOoo0O % O0 / Ooo00oOo00o
 if 100 - 100: oO0o0ooO0 / o00O0oo - OoooooooOO % OoOoOO00 - OOOo0 % I1IiI
def ooo0OO ( ) :
 if 15 - 15: I1IiI
 oOoOooOo0o0 ( '[COLORgreen]Recent Episodes[/COLOR]' , '' , 10019 , oOOoO0 + 'dtv.png' , OOooO0OOoo , '' )
 oOoOooOo0o0 ( '[COLORgreen]Genres[/COLOR]' , '' , 10020 , oOOoO0 + 'dtv.png' , OOooO0OOoo , '' )
 oOoOooOo0o0 ( '[COLORgreen]Search[/COLOR]' , '' , 10021 , oOOoO0 + 'dtv.png' , OOooO0OOoo , '' )
 if 62 - 62: o00O0oo
def ooO000O ( ) :
 if 53 - 53: OOooOOo . oO0o0ooO0 / o00O0oo
 iI1i11 = cloudflare . source ( oOo0oooo00o ( 'aHR0cDovL2RpemlsYWIuY29t' ) )
 OOoOO0oo0ooO = re . compile ( '<li id=".+?">.+?<a href="(.+?)">.+?<img width="40" height="40" src="(.+?)" alt=""/>.+?<span class="title">\n(.+?)</span>.+?<span class="alt-title">\n(.+?)</span>.+?</a>.+?</li>' , re . DOTALL ) . findall ( iI1i11 )
 for O0o0O00Oo0o0 , iII111Ii , O00O0oOO00O00 , I11iiIi1i1 in OOoOO0oo0ooO :
  oOoOooOo0o0 ( O00O0oOO00O00 + '  -  ' + ( I11iiIi1i1 ) . replace ( 'sezon' , 'Season' ) . replace ( 'bölüm' , 'Episode' ) , O0o0O00Oo0o0 , 10023 , oOOoO0 + 'dtv.png' , OOooO0OOoo , '' )
  if 41 - 41: o00O0oo % ii11ii1ii
  if 12 - 12: OoOO0ooOOoo0O
  if 69 - 69: OoooooooOO + OoOO0ooOOoo0O
def IIi11I1 ( ) :
 if 49 - 49: OoOoOO00 - OOOo0 / o0000oOoOoO0o
 oOoOooOo0o0 ( '[COLORgreen]Action[/COLOR]' , 'Aksiyon' , 10024 , oOOoO0 + 'dtv.png' , OOooO0OOoo , '' )
 oOoOooOo0o0 ( '[COLORgreen]Adventure[/COLOR]' , 'Macera' , 10024 , oOOoO0 + 'dtv.png' , OOooO0OOoo , '' )
 oOoOooOo0o0 ( '[COLORgreen]Animation[/COLOR]' , 'Animasyon' , 10024 , oOOoO0 + 'dtv.png' , OOooO0OOoo , '' )
 oOoOooOo0o0 ( '[COLORgreen]Anime[/COLOR]' , 'Anime' , 10024 , oOOoO0 + 'dtv.png' , OOooO0OOoo , '' )
 oOoOooOo0o0 ( '[COLORgreen]Biography[/COLOR]' , 'Biyografi' , 10024 , oOOoO0 + 'dtv.png' , OOooO0OOoo , '' )
 oOoOooOo0o0 ( '[COLORgreen]Comedy[/COLOR]' , 'Komedi' , 10024 , oOOoO0 + 'dtv.png' , OOooO0OOoo , '' )
 oOoOooOo0o0 ( '[COLORgreen]Crime[/COLOR]' , 'Su%C3%A7' , 10024 , oOOoO0 + 'dtv.png' , OOooO0OOoo , '' )
 oOoOooOo0o0 ( '[COLORgreen]Documentary[/COLOR]' , 'Belgesel' , 10024 , oOOoO0 + 'dtv.png' , OOooO0OOoo , '' )
 oOoOooOo0o0 ( '[COLORgreen]Drama[/COLOR]' , 'Dram' , 10024 , oOOoO0 + 'dtv.png' , OOooO0OOoo , '' )
 oOoOooOo0o0 ( '[COLORgreen]Family[/COLOR]' , 'Aile' , 10024 , oOOoO0 + 'dtv.png' , OOooO0OOoo , '' )
 oOoOooOo0o0 ( '[COLORgreen]Fantasy[/COLOR]' , 'Fantastik' , 10024 , oOOoO0 + 'dtv.png' , OOooO0OOoo , '' )
 oOoOooOo0o0 ( '[COLORgreen]History[/COLOR]' , 'Tarih' , 10024 , oOOoO0 + 'dtv.png' , OOooO0OOoo , '' )
 oOoOooOo0o0 ( '[COLORgreen]Horror[/COLOR]' , 'Korku' , 10024 , oOOoO0 + 'dtv.png' , OOooO0OOoo , '' )
 oOoOooOo0o0 ( '[COLORgreen]Mini-Series[/COLOR]' , 'Mini%20Dizi' , 10024 , oOOoO0 + 'dtv.png' , OOooO0OOoo , '' )
 oOoOooOo0o0 ( '[COLORgreen]Musical[/COLOR]' , 'M%C3%BCzikal' , 10024 , oOOoO0 + 'dtv.png' , OOooO0OOoo , '' )
 oOoOooOo0o0 ( '[COLORgreen]Mystery[/COLOR]' , 'Gizem' , 10024 , oOOoO0 + 'dtv.png' , OOooO0OOoo , '' )
 oOoOooOo0o0 ( '[COLORgreen]Romance[/COLOR]' , 'Romantik' , 10024 , oOOoO0 + 'dtv.png' , OOooO0OOoo , '' )
 oOoOooOo0o0 ( '[COLORgreen]Science Fiction[/COLOR]' , 'Bilim%20Kurgu' , 10024 , oOOoO0 + 'dtv.png' , OOooO0OOoo , '' )
 oOoOooOo0o0 ( '[COLORgreen]Sport[/COLOR]' , 'Spor' , 10024 , oOOoO0 + 'dtv.png' , OOooO0OOoo , '' )
 oOoOooOo0o0 ( '[COLORgreen]Thriller[/COLOR]' , 'Gerilim' , 10024 , oOOoO0 + 'dtv.png' , OOooO0OOoo , '' )
 oOoOooOo0o0 ( '[COLORgreen]War[/COLOR]' , 'Sava%C5%9F' , 10024 , oOOoO0 + 'dtv.png' , OOooO0OOoo , '' )
 oOoOooOo0o0 ( '[COLORgreen]Western[/COLOR]' , 'Tarih' , 10024 , oOOoO0 + 'dtv.png' , OOooO0OOoo , '' )
 oOoOooOo0o0 ( '[COLORgreen]Youth[/COLOR]' , 'Gen%C3%A7lik' , 10024 , oOOoO0 + 'dtv.png' , OOooO0OOoo , '' )
 if 74 - 74: o0000oOoOoO0o - OoOO0ooOOoo0O + i1IIi . OOOo0 + OoOO0ooOOoo0O - o0000oOoOoO0o
def Ii ( url ) :
 IiiiiI1 = 'http://dizilab.com/arsiv?limit=100&tur=' + url + '&orderby=&ulke=&order=&yil=&dizi_adi='
 o00oOO0o = cloudflare . source ( IiiiiI1 )
 OOoOO0oo0ooO = re . compile ( '<div class="tv-series-single">.+?<a href="(.+?)" class="film-image">.+?<img src="(.+?)" alt=""/>.+?<span class="position">.+?</span>\n(.+?)</a>' , re . DOTALL ) . findall ( o00oOO0o )
 for url , iII111Ii , O00O0oOO00O00 in OOoOO0oo0ooO :
  oOoOooOo0o0 ( '[COLORgreen]' + O00O0oOO00O00 + '[/COLOR]' , url , 10022 , oOOoO0 + 'dtv.png' , OOooO0OOoo , '' )
  if 62 - 62: ii11ii1ii % oO0o0ooO0 * Ooo00oOo00o - i1IIi
  if 66 - 66: i11iIiiIii / OOooOOo - OoooooooOO / i1IIi . i11iIiiIii
  if 16 - 16: Oo % ii11ii1ii + o0000oOoOoO0o - O0 . oO0o0ooO0 / O0oO
  if 35 - 35: OoOO / O0oO / OoOoOO00 - iIii1I11I1II1 + OoOoOO00 . O0oO
def O0O00O000OOO ( ) :
 if 3 - 3: O0
 oooo000 = Oo0o0000o0o0 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 iiII1i1 = oooo000 . lower ( )
 O0o0O00Oo0o0 = ( oOo0oooo00o ( 'aHR0cDovL2RpemlsYWIuY29tL2Fyc2l2P2xpbWl0PSZ0dXI9Jm9yZGVyYnk9JnVsa2U9Jm9yZGVyPSZ5aWw9JmRpemlfYWRpPQ==' ) ) + ( oooo000 ) . replace ( ' ' , '+' )
 o00oOO0o = cloudflare . source ( O0o0O00Oo0o0 )
 OOoOO0oo0ooO = re . compile ( '<a href="(.+?)" class="film-image">\n<img src="(.+?)" alt=""/>\n</a>\n<div class="tss-detail">\n<a class="title" style="" href=".+?">\n<span class="position">.+?</span>\n(.+?)</a>' ) . findall ( o00oOO0o )
 for O0o0O00Oo0o0 , iII111Ii , O00O0oOO00O00 in OOoOO0oo0ooO :
  if oooo000 in O00O0oOO00O00 . lower ( ) :
   oOoOooOo0o0 ( '[COLORgreen]' + O00O0oOO00O00 + '[/COLOR]' , O0o0O00Oo0o0 , 10022 , oOOoO0 + 'dtv.png' )
   if 64 - 64: i1IIi % o0oO0 / i11iIiiIii - i1IIi % OoOO0ooOOoo0O . oO0o0ooO0
   if 8 - 8: Oo + OoOoOO00 * OoOO0ooOOoo0O * I1IiI * o0000oOoOoO0o / IIII
   if 21 - 21: OoOO / OoooooooOO
def III1IiIII1 ( url ) :
 o00oOO0o = cloudflare . source ( url )
 OOoOO0oo0ooO = re . compile ( '<a class="season" href="(.+?)">\n(.+?)\n</a>.+?<a class="episode" href=".+?">\n(.+?)\n</a>.+?<a class="episode-name" href=".+?">\n(.+?)</a>' , re . DOTALL ) . findall ( o00oOO0o )
 for O00ooOo , oOO0o00O , oOoO , O00O0oOO00O00 in OOoOO0oo0ooO :
  IIIIiI1iiiIiii = ( oOoO ) . replace ( 'Sezon' , '' ) . replace ( 'bölüm' , '' ) . replace ( 'Bölüm' , '' ) . replace ( 'BÃ¶lÃ¼m' , '' ) . replace ( '.' , '' )
  ii1i1i = ( oOO0o00O ) . replace ( 'bölüm' , '' ) . replace ( 'Sezon' , '' ) . replace ( 'Bölüm' , '' ) . replace ( 'BÃ¶lÃ¼m' , '' ) . replace ( '.' , '' )
  II11iIII1i1I = 'Season ' + ii1i1i + 'Episode ' + IIIIiI1iiiIiii + O00O0oOO00O00
  oOO0oo ( II11iIII1i1I , O00ooOo )
  if 13 - 13: OoooooooOO * OoOO - o00O0oo / OoOO0ooOOoo0O + o0000oOoOoO0o + IIII
  xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 39 - 39: iIii1I11I1II1 - OoooooooOO
  if 81 - 81: ii11ii1ii - O0 * OoooooooOO
def oOO0oo ( name , url ) :
 O00ooOo = url
 iiIiI = name
 o0Ooo0O00 = cloudflare . source ( O00ooOo )
 i1ii1II1ii = re . compile ( 'file: "(.+?)",.+?label: "(.+?)",' , re . DOTALL ) . findall ( o0Ooo0O00 )
 for oOOOO , ii1o0oooO in i1ii1II1ii :
  iiIi1iI1iIii ( '[COLORgreen]' + iiIiI + ii1o0oooO + '[/COLOR]' , oOOOO , 10012 , oOOoO0 + 'dtv.png' )
  if 89 - 89: OoOoOO00 / OoOO
 xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 14 - 14: OoOO0ooOOoo0O . OOOo0 * o0oO0 + OoOoOO00 - o0oO0 + OoOO0ooOOoo0O
 if 18 - 18: OoOO - OOooOOo - OOOo0 - OOOo0
def OOooo00 ( ) :
 if 35 - 35: O0oO . I1IiI * i11iIiiIii
 if 44 - 44: i11iIiiIii / Oo
 if 42 - 42: OoooooooOO + Oo % OoOoOO00 + Ooo00oOo00o
 if 24 - 24: oO0o0ooO0 * OoOoOO00 % oO0o0ooO0 % IIII + OoooooooOO
 if 29 - 29: OoOoOO00 - OoooooooOO - i11iIiiIii . OOooOOo
 if 19 - 19: OoOoOO00
 if 72 - 72: OoooooooOO / OOOo0 + o00O0oo / I1IiI * o00O0oo
 if 34 - 34: O0 * O0 % OoooooooOO + oO0o0ooO0 * iIii1I11I1II1 % o00O0oo
 if 25 - 25: o0000oOoOoO0o + I1IiI . OOooOOo % I1IiI * OoOO0ooOOoo0O
 if 32 - 32: i11iIiiIii - O0oO
 if 53 - 53: OoooooooOO - IIII
 if 87 - 87: OoOO . OOOo0
 if 17 - 17: o00O0oo . i11iIiiIii
 if 5 - 5: ii11ii1ii + O0 + O0 . O0oO - o0oO0
 if 63 - 63: OoOO
 oOoOooOo0o0 ( '[COLORgreen]Newest Episodes Added[/COLOR]' , 'http://www.watchseries.li/latest' , 10046 , oOOoO0 + 'WATCHSERIES.png' , '' , '' )
 oOoOooOo0o0 ( '[COLORgreen]This Week\'s Popular Episodes[/COLOR]' , 'http://www.watchseries.li/new' , 10042 , oOOoO0 + 'WATCHSERIES.png' , '' , '' )
 oOoOooOo0o0 ( '[COLORgreen]Search Program[/COLOR]' , '' , 10043 , oOOoO0 + 'WATCHSERIES.png' , '' , '' )
 if 71 - 71: i1IIi . o00O0oo * oO0o0ooO0 % OoooooooOO + OoOO0ooOOoo0O
 if 36 - 36: IIII
def i1iiI ( url ) :
 o00oOO0o = OOO00O ( url )
 i1Oo00 = re . compile ( '<ul class="pagination" style="line-height: 3;">(.+?)</ul>' , re . DOTALL ) . findall ( o00oOO0o )
 OOoOO0oo0ooO = re . compile ( '<li><a href="/letters/(.+?)">(.+?)</a></li>' ) . findall ( str ( i1Oo00 ) )
 for url , O00O0oOO00O00 in OOoOO0oo0ooO :
  oOoOooOo0o0 ( '[COLORgreen]' + O00O0oOO00O00 + '[/COLOR]' , 'http://watchseries.li/letters/' + url , 10049 , oOOoO0 + 'WATCHSERIES.png' , '' , '' )
  if 74 - 74: O0oO % ii11ii1ii
def iiIiIi1 ( url ) :
 o00oOO0o = OOO00O ( url )
 OOoOO0oo0ooO = re . compile ( '<a href="(.+?)" class="sr-header">(.+?)</a>' ) . findall ( o00oOO0o )
 for url , O00O0oOO00O00 in OOoOO0oo0ooO :
  oOoOooOo0o0 ( '[COLORgreen]' + O00O0oOO00O00 + '[/COLOR]' , 'http://watchseries.li/' + url , 10049 , oOOoO0 + 'WATCHSERIES.png' , '' , '' )
  if 78 - 78: OoOO0ooOOoo0O % OOooOOo
def IIIiIiI ( url ) :
 o00oOO0o = OOO00O ( url )
 OOoOO0oo0ooO = re . compile ( '<li class="col-md-6 col-xs-12 list-movies-li"><a href="(.+?)" title=".+?">(.+?)<span class="epnum">.+?</span></a></li>' , re . DOTALL ) . findall ( o00oOO0o )
 i1ii1II1ii = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="(.+?)">Next</a></li></ul>' , re . DOTALL ) . findall ( o00oOO0o )
 for url , O00O0oOO00O00 in OOoOO0oo0ooO :
  oOoOooOo0o0 ( '[COLORgreen]' + ( O00O0oOO00O00 ) . replace ( '&nbsp;' , ' ' ) . replace ( '&amp;' , '&' ) . replace ( '&#039;' , '\'' ) + '[/COLOR]' , 'http://www.watchseries.li' + url , 10044 , oOOoO0 + 'WATCHSERIES.png' , '' , '' )
 for url in i1ii1II1ii :
  oOoOooOo0o0 ( '[COLORgreen]' + 'NEXT' + '[/COLOR]' , 'http://www.watchseries.li' + url , 10049 , '' , '' , '' )
  if 7 - 7: IIII . I1IiI / ii11ii1ii . OoOO0ooOOoo0O * o0000oOoOoO0o - OoOoOO00
  if 37 - 37: O0oO . I1IiI / O0 * oO0o0ooO0
def III11iiii11i1 ( ) :
 oooo000 = Oo0o0000o0o0 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 ooOo0OoO = 'http://www.watchseries.li/search/' + oooo000 . replace ( ' ' , '%20' )
 o00oOO0o = OOO00O ( ooOo0OoO )
 OOoOO0oo0ooO = re . compile ( '<img src="(.+?)".+?<a href="(.+?)" title=".+?"><b>(.+?)</b>' , re . DOTALL ) . findall ( o00oOO0o )
 for iII111Ii , O0o0O00Oo0o0 , O00O0oOO00O00 in OOoOO0oo0ooO :
  if 'watch online' in O00O0oOO00O00 :
   pass
  else :
   print O0o0O00Oo0o0
   oOoOooOo0o0 ( '[COLORgreen]' + O00O0oOO00O00 + '[/COLOR]' , 'http://www.watchseries.li' + O0o0O00Oo0o0 , 10044 , iII111Ii , '' , '' )
   if 36 - 36: IIII - OoooooooOO / Ooo00oOo00o
   xbmcplugin . setContent ( O00o0OO , 'movies' )
   if 34 - 34: o0oO0
def i1iI1 ( url ) :
 o00oOO0o = OOO00O ( url )
 OOoOO0oo0ooO = re . compile ( '<img src="(.+?)".+?<div class="block-left-home-inside-text">.+?<a href="(.+?)" title=".+?"><b>(.+?)</b> <br>.+?<span class=".+?">(.+?)</span></a><br>(.+?)<br>' , re . DOTALL ) . findall ( o00oOO0o )
 for iII111Ii , url , O00O0oOO00O00 , oOoO , IIi11IIiIii1 in OOoOO0oo0ooO :
  IIi11i1II = ( O00O0oOO00O00 ) . replace ( '&nbsp;' , ' ' ) . replace ( '&amp;' , '&' ) . replace ( '&#039;' , '\'' ) + ' - ' + ( oOoO ) . replace ( '&amp;' , '&' ) . replace ( '&#039;' , '\'' )
  oOoOooOo0o0 ( '[COLORgreen]' + IIi11i1II + '[/COLOR]' , 'http://www.watchseries.li' + url , 10045 , iII111Ii , '' , IIi11IIiIii1 )
  if 73 - 73: OOooOOo - OOOo0 * i1IIi / i11iIiiIii * OoOO0ooOOoo0O % OoOoOO00
def OooOoOOo0oO00 ( url ) :
 o00oOO0o = OOO00O ( url )
 OOoOO0oo0ooO = re . compile ( '<li class="col-md-6 col-xs-12 list-movies-li"><a href="(.+?)" title=".+?">(.+?)<span class="epnum">.+?</span></a></li>' , re . DOTALL ) . findall ( o00oOO0o )
 i1ii1II1ii = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="(.+?)">Next</a></li></ul>' , re . DOTALL ) . findall ( o00oOO0o )
 for url , O00O0oOO00O00 in OOoOO0oo0ooO :
  IIi11i1II = ( O00O0oOO00O00 ) . replace ( '&nbsp;' , ' ' ) . replace ( '&amp;' , '&' ) . replace ( '&#039;' , '\'' )
  oOoOooOo0o0 ( '[COLORgreen]' + IIi11i1II + '[/COLOR]' , 'http://www.watchseries.li' + url , 10045 , oOOoO0 + 'WATCHSERIES.png' , '' , '' )
 for url in i1ii1II1ii :
  oOoOooOo0o0 ( '[COLORgreen]' + 'NEXT' + '[/COLOR]' , 'http://www.watchseries.li' + url , 10046 , '' , '' , '' )
  if 73 - 73: oO0o0ooO0 / ii11ii1ii % ii11ii1ii * o0000oOoOoO0o / ii11ii1ii
def iI1I11iIIi1 ( url ) :
 o00oOO0o = OOO00O ( url )
 OOoOO0oo0ooO = re . compile ( '<div class="mask">.+?<a href="(.+?)" title="(.+?)">.+?<img src="(.+?)"' , re . DOTALL ) . findall ( o00oOO0o )
 i1ii1II1ii = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="(.+?)">Next</a></li></ul>' , re . DOTALL ) . findall ( o00oOO0o )
 for url , O00O0oOO00O00 , iII111Ii in OOoOO0oo0ooO :
  oOoOooOo0o0 ( '[COLORgreen]' + ( O00O0oOO00O00 ) . replace ( '&nbsp;' , ' ' ) . replace ( '&amp;' , '&' ) . replace ( '&#039;' , '\'' ) + '[/COLOR]' , 'http://www.watchseries.li' + url , 10044 , iII111Ii , '' , '' )
 for url in i1ii1II1ii :
  oOoOooOo0o0 ( '[COLORgreen]' + 'NEXT' + '[/COLOR]' , 'http://www.watchseries.li' + url , 10041 , '' , '' , '' )
  if 39 - 39: OOooOOo . iIii1I11I1II1
def o0iIiiIiiIi ( url ) :
 o00oOO0o = OOO00O ( url )
 i1Oo00 = re . compile ( '<div class="col-md-6 col-xs-12".+?<a href=".+?" itemprop="url"><span itemprop="name">(.+?)</span>(.+?)</ul>' , re . DOTALL ) . findall ( o00oOO0o )
 for oOO0o00O , IIi in i1Oo00 :
  OOoOO0oo0ooO = re . compile ( '<li itemprop="episode".+?<meta itemprop="url" content="(.+?)">.+?<span class="" itemprop="name">\n(.+?)\n' , re . DOTALL ) . findall ( str ( IIi ) )
  for url , O00O0oOO00O00 in OOoOO0oo0ooO :
   IIi11i1II = ( oOO0o00O ) . replace ( '  ' , '' ) + ' ' + ( O00O0oOO00O00 ) . replace ( '&nbsp;' , ' ' ) . replace ( '&#039;' , '\'' ) . replace ( '  ' , '' )
   oOoOooOo0o0 ( '[COLORgreen]' + IIi11i1II + '[/COLOR]' , 'http://www.watchseries.li' + url , 10045 , oOOoO0 + 'WATCHSERIES.png' , '' , '' )
 i1ii1II1ii = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="(.+?)">Next</a></li></ul>' , re . DOTALL ) . findall ( o00oOO0o )
 for url in i1ii1II1ii :
  oOoOooOo0o0 ( '[COLORgreen]' + 'NEXT' + '[/COLOR]' , 'http://www.watchseries.li' + url , 10044 , '' , '' , '' )
  if 40 - 40: OOooOOo
  if 78 - 78: iIii1I11I1II1
class ooO0oo0o0 ( ) :
 if 9 - 9: OOOo0 + ii11ii1ii / OOOo0 . OoOO * o0oO0
 List = [ ]
 source_list = [ ]
 def __init__ ( self , name ) :
  if 45 - 45: i11iIiiIii
  IIi11i1II = name
  self . Get_Sources ( O0o0O00Oo0o0 , IIi11i1II )
  if 82 - 82: o00O0oo + IIII
  if 12 - 12: O0oO
 def Get_Sources ( self , URL , season_name ) :
  i1111 = xbmcgui . DialogProgress ( )
  o00oOO0o = OOO00O ( URL )
  OOoOO0oo0ooO = re . compile ( '<td>.+?<a href="/link/(.+?)".+?height="16px">(.+?)\n' , re . DOTALL ) . findall ( o00oOO0o )
  for O0o0O00Oo0o0 , O00O0oOO00O00 in OOoOO0oo0ooO :
   URL = 'http://www.watchseries.li/link/' + O0o0O00Oo0o0
   self . Get_site_link ( URL , season_name )
   if 93 - 93: i11iIiiIii % iIii1I11I1II1 % i11iIiiIii + OOooOOo / OOooOOo / OoOoOO00
 def Get_site_link ( self , url , season_name ) :
  o00oOO0o = OOO00O ( url )
  OOoOO0oo0ooO = re . compile ( '<iframe style=.+?" src="(.+?)"' ) . findall ( o00oOO0o )
  i1ii1II1ii = re . compile ( '<IFRAME SRC="(.+?)"' ) . findall ( o00oOO0o )
  oo00O00oO000o = re . compile ( '<IFRAME style=".+?" SRC="(.+?)"' ) . findall ( o00oOO0o )
  for url in OOoOO0oo0ooO :
   self . main ( url , season_name )
  for url in i1ii1II1ii :
   self . main ( url , season_name )
  for url in oo00O00oO000o :
   self . main ( url , season_name )
   if 49 - 49: OoOO0ooOOoo0O . ii11ii1ii . i11iIiiIii - OoOoOO00 / o00O0oo
 def main ( self , url , season_name ) :
  i1111 . create ( "[COLORwhite]Origin[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
  if 'daclips.in' in url :
   ooOo0O0o0 = 'DACLIPS'
   if ooOo0O0o0 in ooO0oo0o0 . source_list :
    pass
   else :
    self . daclips ( url , season_name , ooOo0O0o0 )
    i1111 . update ( 0 , "" , "Getting Daclips Links" )
  else :
   if 'filehoot.com' in url :
    ooOo0O0o0 = 'FILEHOOT'
    if ooOo0O0o0 in ooO0oo0o0 . source_list :
     pass
    else :
     i1111 . update ( 0 , "" , "Getting Filehoot Links" )
     self . filehoot ( url , season_name , ooOo0O0o0 )
   else :
    if 'thevideo.me' in url :
     ooOo0O0o0 = 'THEVIDEO'
     if ooOo0O0o0 in ooO0oo0o0 . source_list :
      pass
     else :
      self . thevideo ( url , season_name , ooOo0O0o0 )
      i1111 . update ( 0 , "" , "Getting Thevideo Links" )
    else :
     if 'allmyvideos.net' in url :
      ooOo0O0o0 = 'ALLMYVIDEOS'
      if ooOo0O0o0 in ooO0oo0o0 . source_list :
       pass
      else :
       self . allmyvid ( url , season_name , ooOo0O0o0 )
       i1111 . update ( 0 , "" , "Getting Allmyvideo Links" )
     else :
      if 'vidspot.net' in url :
       ooOo0O0o0 = 'VIDSPOT'
       if ooOo0O0o0 in ooO0oo0o0 . source_list :
        pass
       else :
        self . vidspot ( url , season_name , ooOo0O0o0 )
        i1111 . update ( 0 , "" , "Getting Vidspot Links" )
      else :
       if 'vodlocker' in url :
        ooOo0O0o0 = 'VODLOCKER'
        if ooOo0O0o0 in ooO0oo0o0 . source_list :
         pass
        else :
         self . vodlocker ( url , season_name , ooOo0O0o0 )
         i1111 . update ( 0 , "" , "Getting Vodlocker Links" )
         if 65 - 65: o0oO0 + O0
         if 32 - 32: OoooooooOO - I1IiI - i11iIiiIii * OOooOOo / Oo + OoooooooOO
 def allmyvid ( self , url , season_name , source_name ) :
  o00oOO0o = OOO00O ( url )
  OOoOO0oo0ooO = re . compile ( '"file" : "(.+?)",\n.+?"default" : .+?,\n.+?"label" : "(.+?)"' , re . DOTALL ) . findall ( o00oOO0o )
  for ii1I1I111 , O00O0oOO00O00 in OOoOO0oo0ooO :
   self . Printer ( ii1I1I111 , season_name , source_name )
   if 3 - 3: OoooooooOO / OoOO0ooOOoo0O * Oo . o0oO0
 def vidspot ( self , url , season_name , source_name ) :
  o00oOO0o = OOO00O ( url )
  OOoOO0oo0ooO = re . compile ( '"file" : "(.+?)",\n.+?"default" : .+?,\n.+?"label" : "(.+?)"' ) . findall ( o00oOO0o )
  for ii1I1I111 , O00O0oOO00O00 in OOoOO0oo0ooO :
   self . Printer ( ii1I1I111 , season_name , source_name )
   if 62 - 62: i1IIi / o0oO0 . OOOo0 * OOooOOo
 def thevideo ( self , url , season_name , source_name ) :
  o00oOO0o = OOO00O ( url )
  OOoOO0oo0ooO = re . compile ( "{ label: '.+?', file: '(.+?)' }" ) . findall ( o00oOO0o )
  for ii1I1I111 in OOoOO0oo0ooO :
   self . Printer ( ii1I1I111 , season_name , source_name )
   if 21 - 21: OOooOOo
 def vodlocker ( self , url , season_name , source_name ) :
  o00oOO0o = OOO00O ( url )
  OOoOO0oo0ooO = re . compile ( 'file: "(.+?)",.+?skin' , re . DOTALL ) . findall ( o00oOO0o )
  for ii1I1I111 in OOoOO0oo0ooO :
   self . Printer ( ii1I1I111 , season_name , source_name )
   if 81 - 81: o0000oOoOoO0o / iIii1I11I1II1 - o0oO0 * O0oO . OOOo0 * ii11ii1ii
 def daclips ( self , url , season_name , source_name ) :
  o00oOO0o = OOO00O ( url )
  OOoOO0oo0ooO = re . compile ( '{ file: "(.+?)", type:"video" }' ) . findall ( o00oOO0o )
  for ii1I1I111 in OOoOO0oo0ooO :
   self . Printer ( ii1I1I111 , season_name , source_name )
   if 95 - 95: OOOo0
 def filehoot ( self , url , season_name , source_name ) :
  o00oOO0o = OOO00O ( url )
  OOoOO0oo0ooO = re . compile ( 'file: "(.+?)",.+?skin' , re . DOTALL ) . findall ( o00oOO0o )
  for ii1I1I111 in OOoOO0oo0ooO :
   self . Printer ( ii1I1I111 , season_name , source_name )
   if 88 - 88: IIII % Ooo00oOo00o + O0oO + O0oO * OoOoOO00
 def Printer ( self , Link , season_name , source_name ) :
  if 78 - 78: OoooooooOO
  if Link in ooO0oo0o0 . List :
   pass
  elif source_name in ooO0oo0o0 . source_list :
   pass
  else :
   iiIi1iI1iIii ( '[COLORgreen]' + source_name + '[/COLOR]' , Link , 10012 , oOOoO0 + 'WATCHSERIES.png' )
   i1111 . update ( 100 , "" , "Got Source" )
   ooO0oo0o0 . List . append ( Link )
   ooO0oo0o0 . source_list . append ( source_name )
   if 77 - 77: ii11ii1ii / i1IIi / Oo % OoOO0ooOOoo0O
   xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
   if 48 - 48: o0000oOoOoO0o - IIII + iIii1I11I1II1 + OoooooooOO
   if 4 - 4: OoOoOO00 . o0000oOoOoO0o + o00O0oo * O0oO . o0oO0
   if 87 - 87: I1IiI / Ooo00oOo00o / i11iIiiIii
   if 74 - 74: OoOO / ii11ii1ii % OOooOOo
   if 88 - 88: I1IiI - i11iIiiIii % OOooOOo * o0000oOoOoO0o + ii11ii1ii
def OoiIIIiIi1I1i ( ) :
 oOoOooOo0o0 ( '[COLORgreen]Highlights[/COLOR]' , '' , 10008 , oOOoO0 + 'ORIGINFOOTBALL.png' , OOooO0OOoo , '' )
 oOoOooOo0o0 ( '[COLORgreen]Fixtures[/COLOR]' , '' , 10009 , oOOoO0 + 'ORIGINFOOTBALL.png' , OOooO0OOoo , '' )
 if 78 - 78: iIii1I11I1II1 % I1IiI + ii11ii1ii / i1IIi % OoOoOO00 + OoOO0ooOOoo0O
def OooOOOO0O0 ( ) :
 iI1i11 = OOO00O ( oOo0oooo00o ( 'aHR0cDovL2xpdmVvbnNhdC5jb20vcXVpY2tpbmRleC5odG1s' ) )
 OOoOO0oo0ooO = re . compile ( '<a target="_self" href="(.+?)".+?src="(.+?)" alt="(.+?)"' , re . DOTALL ) . findall ( iI1i11 )
 for O0o0O00Oo0o0 , iII111Ii , O00O0oOO00O00 in OOoOO0oo0ooO :
  oOoOooOo0o0 ( '[COLORgreen]' + ( O00O0oOO00O00 ) . replace ( 'amp;' , '' ) + '[/COLOR]' , oOo0oooo00o ( 'aHR0cDovL2xpdmVvbnNhdC5jb20v' ) + O0o0O00Oo0o0 , 10010 , oOo0oooo00o ( 'aHR0cDovL2xpdmVvbnNhdC5jb20v' ) + iII111Ii , OOooO0OOoo , '' )
  if 38 - 38: O0oO % OoOO0ooOOoo0O - OoooooooOO
def oOo0OOoooO ( url ) :
 o00oOO0o = OOO00O ( url )
 i1Oo00 = re . compile ( 'AndClearL.+?><h2.+?head>(.*?)float' , re . DOTALL ) . findall ( o00oOO0o )
 for i1Oo00 in i1Oo00 :
  iIi1iIIIiIiI = re . compile ( '(.*?)</h2>' ) . findall ( str ( i1Oo00 ) )
  for OooOo000o0o in iIi1iIIIiIiI :
   OooOo000o0o = OooOo000o0o
  iI1I1iII1i = re . compile ( 'comp_head>(.*?)</span>.*?<div class = fLeft width = ".*?"><img src="(.*?)">.*?</div>.*?ST:(.*?)</div>(.+?)<!-- around all of channel types ENDS 2-->' , re . DOTALL ) . findall ( str ( i1Oo00 ) )
  for iiIIii , iII111Ii , time , oO0Oo0O0 in iI1I1iII1i :
   I1iIiI1IiIIII = re . compile ( ",CAPTION, '(.+?)&nbsp" ) . findall ( oO0Oo0O0 )
   oOoOooOo0o0 ( '[COLORgreen]' + OooOo000o0o + ' - ' + iiIIii + ' - ' + time + '[/COLOR]' , '' , 10010 , oOo0oooo00o ( 'aHR0cDovL2xpdmVvbnNhdC5jb20=' ) + iII111Ii , OOooO0OOoo , ( str ( I1iIiI1IiIIII ) ) )
   if 18 - 18: o0oO0 % i11iIiiIii . iIii1I11I1II1 - oO0o0ooO0
 OoOo ( 'tvshows' , 'Media Info 3' )
 if 80 - 80: OOOo0 + OoOO - i1IIi . o00O0oo / OOooOOo / OOOo0
def I1Iiii ( ) :
 if 34 - 34: o00O0oo * I1IiI - IIII - OOOo0 - o00O0oo
 oOoOooOo0o0 ( '[COLORgreen]Shows[/COLOR]' , 'http://www.fullmatchesandshows.com/category/show/' , 10011 , 'http://www.fm-base.co.uk/forum/attachments/club-competition-logos/3885-soccer-am-logo-socceram.png' , oOOoO0 + 'fanart.jpg' , '' )
 oOoOooOo0o0 ( '[COLORgreen]Premier League[/COLOR]' , 'http://www.fullmatchesandshows.com/premier-league/' , 10011 , 'https://footballseasons.files.wordpress.com/2013/05/premier-league.png' , oOOoO0 + 'fanart.jpg' , '' )
 oOoOooOo0o0 ( '[COLORgreen]La Liga[/COLOR]' , 'http://www.fullmatchesandshows.com/la-liga/' , 10011 , 'http://1.bp.blogspot.com/-c6kQ40ryhyo/U19cUlz25sI/AAAAAAAABak/qtn5chSFZm0/s1600/la-liga-logo_display_image.png' , oOOoO0 + 'fanart.jpg' , '' )
 oOoOooOo0o0 ( '[COLORgreen]Bundesliga[/COLOR]' , 'http://www.fullmatchesandshows.com/bundesliga/' , 10011 , 'http://m.img.brothersoft.com/iphone/189/518670189_icon175x175.jpg' , oOOoO0 + 'fanart.jpg' , '' )
 oOoOooOo0o0 ( '[COLORgreen]Champions League[/COLOR]' , 'http://www.fullmatchesandshows.com/champions-league/' , 10011 , 'http://www.ecursuri.ro/images/teste/test-champions-league.jpg' , oOOoO0 + 'fanart.jpg' , '' )
 oOoOooOo0o0 ( '[COLORgreen]Serie A[/COLOR]' , 'http://www.fullmatchesandshows.com/category/serie-a/' , 10011 , 'http://files.jcriccione.it/200000223-2484526782/serie%20a.png' , oOOoO0 + 'fanart.jpg' , '' )
 oOoOooOo0o0 ( '[COLORgreen]Ligue 1[/COLOR]' , 'http://www.fullmatchesandshows.com/category/ligue-1/' , 10011 , 'http://a1.mzstatic.com/us/r30/Purple5/v4/37/c7/44/37c744ae-5824-42b7-6ce0-5f471f52baab/icon180x180.jpeg' , oOOoO0 + 'fanart.jpg' , '' )
 oOoOooOo0o0 ( '[COLORgreen]Copa America 2015[/COLOR]' , 'http://www.fullmatchesandshows.com/copa-america-2015/' , 10011 , 'https://pbs.twimg.com/profile_images/521966985907691520/Nq9OAPIo_400x400.png' , oOOoO0 + 'fanart.jpg' , '' )
 oOoOooOo0o0 ( '[COLORgreen]CONCACAF[/COLOR]' , 'http://www.fullmatchesandshows.com/category/concacaf/' , 10011 , 'http://a3.mzstatic.com/us/r30/Purple3/v4/40/26/14/4026147c-7022-4ca3-504e-e78950cc3f1c/icon175x175.png' , oOOoO0 + 'fanart.jpg' , '' )
 oOoOooOo0o0 ( '[COLORgreen]Women World Cup[/COLOR]' , 'http://www.fullmatchesandshows.com/category/women-world-cup/' , 10011 , 'https://upload.wikimedia.org/wikipedia/en/thumb/7/76/2015_FIFA_Women\'s_World_Cup_logo.svg/967px-2015_FIFA_Women\'s_World_Cup_logo.svg.png' , oOOoO0 + 'fanart.jpg' , '' )
 if 42 - 42: OoOoOO00 * OOOo0 % i1IIi - o00O0oo % IIII
def Ii1I1 ( url ) :
 o00oOO0o = OOO00O ( url )
 OOoOO0oo0ooO = re . compile ( 'itemprop="image" class="entry-thumb" src="(.+?)".+?<h3 itemprop="name" class="entry-title td-module-title"><a itemprop="url" href="(.+?)" rel="bookmark" title=".+?">(.+?)</a></h3>' , re . DOTALL ) . findall ( o00oOO0o )
 for iII111Ii , url , O00O0oOO00O00 in OOoOO0oo0ooO :
  o000ooOOo = O00O0oOO00O00 . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' )
  iiIi1iI1iIii ( '[COLORgreen]' + o000ooOOo + '[/COLOR]' , url , 10013 , iII111Ii )
  if 46 - 46: OOOo0 / o00O0oo . O0oO % i11iIiiIii + OOooOOo + OoooooooOO
def O0o0000o ( url ) :
 o00oOO0o = OOO00O ( url )
 OOoOO0oo0ooO = re . compile ( '<script data-config="(.+?)" data-height' ) . findall ( o00oOO0o )
 for oOOOO in OOoOO0oo0ooO :
  oOo00OoOoO = ( oOOOO ) . replace ( '/v2' , '' ) . replace ( 'zeus.json' , 'video-sd.mp4?hosting_id=21772' ) . replace ( 'config.playwire.com' , 'cdn.video.playwire.com' )
  I1Iiiiiii ( 'http:' + oOo00OoOoO )
  if 66 - 66: OOOo0 - IIII
  if 33 - 33: OOOo0 / Ooo00oOo00o
def iiIIi ( url ) :
 iI1i11 = OoOOoooOO0O ( url )
 OOoOO0oo0ooO = re . compile ( '<a href="([^"]*)" title="([^"]*)"><img itemprop="image" content="([^"]*)"' , re . DOTALL ) . findall ( iI1i11 )
 i1ii1II1ii = re . compile ( "<a rel='next' href=([^=]*)=" , re . DOTALL ) . findall ( iI1i11 )
 for url , O00O0oOO00O00 , iII111Ii in OOoOO0oo0ooO :
  iiIi1iI1iIii ( O00O0oOO00O00 , url , 8046 , iII111Ii )
 for url in i1ii1II1ii :
  Oo0o0O00 ( 'NEXT PAGE' , ( url ) . replace ( ' class' , '' ) , 8045 , oOOoO0 + 'geniekitchen.png' )
def i1i ( url ) :
 iI1i11 = OoOOoooOO0O ( url )
 OOoOO0oo0ooO = re . compile ( "__filename='([^']*)',.+?__fullimage='([^']*)',.+?__title='([^']*)'," , re . DOTALL ) . findall ( iI1i11 )
 for url , iII111Ii , O00O0oOO00O00 in OOoOO0oo0ooO :
  I1Iiiiiii ( 'http://bitcast-b.bitgravity.com/ndtvod/23372/ndtv/' + url )
  if 25 - 25: OoOO
def iI1 ( url ) :
 iI1i11 = OoOOoooOO0O ( url )
 OOoOO0oo0ooO = re . compile ( "src='http://www.youtube.com/embed/(.+?)?version=3&#038;rel=1&#038;fs=1&#038;autohide=2&#038;showsearch=0&#038;showinfo=1&#038;iv_load_policy=1&#038;wmode=transparent' frameborder='0' allowfullscreen='true'></iframe>" ) . findall ( iI1i11 )
 for url in OOoOO0oo0ooO :
  yt . PlayVideo ( url )
  if 11 - 11: Ooo00oOo00o
def I11Ii111I ( ) :
 iI1i11 = OoOOoooOO0O ( oOo0oooo00o ( 'aHR0cDovL3RvcGRvY3VtZW50YXJ5ZmlsbXMuY29tLw==' ) )
 OOoOO0oo0ooO = re . compile ( '<a href="(.+?)" >(.+?)</a></li><li>' ) . findall ( iI1i11 )
 for O0o0O00Oo0o0 , O00O0oOO00O00 in OOoOO0oo0ooO :
  Oo0o0O00 ( O00O0oOO00O00 , O0o0O00Oo0o0 , 8041 , oOOoO0 + 'documentary.png' )
def Oo00OO0 ( url ) :
 iI1i11 = OoOOoooOO0O ( url )
 OOoOO0oo0ooO = re . compile ( '<h2><a href="(.+?)" title="(.+?)">.+?</a></h2>.+?src="(.+?)"' , re . DOTALL ) . findall ( iI1i11 )
 i1ii1II1ii = re . compile ( 'class="inactive">.+?</a><a href="(.+?)">Next</a></div>' , re . DOTALL ) . findall ( iI1i11 )
 for url , O00O0oOO00O00 , iII111Ii in OOoOO0oo0ooO :
  Oo0o0O00 ( ( O00O0oOO00O00 ) . replace ( '&#039;s' , '' ) , url , 8042 , iII111Ii )
 for url in i1ii1II1ii :
  Oo0o0O00 ( 'NEXT PAGE' , url , 8041 , oOOoO0 + 'documentary.png' )
  if 72 - 72: i1IIi / OoOO * O0oO
  if 40 - 40: o00O0oo - I1IiI * I1IiI . I1IiI + OoooooooOO
def Oo0 ( url ) :
 iI1i11 = OoOOoooOO0O ( url )
 OOoOO0oo0ooO = re . compile ( '<meta itemprop="name" content="(.+?)".+?<meta itemprop="thumbnailUrl" content="(.+?)".+?<meta itemprop="embedUrl" content="(.+?)".+?<meta itemprop="description" content="(.+?)" />' , re . DOTALL ) . findall ( iI1i11 )
 i1ii1II1ii = re . compile ( '<div class="video new-video"><iframe width="766" height="431" src="(.+?)&amp;iv_load_policy=3&amp;showinfo=0&amp;autohide=1"' , re . DOTALL ) . findall ( iI1i11 )
 for O00O0oOO00O00 , iII111Ii , url , I1iiIIIi11 in OOoOO0oo0ooO :
  iiIi1iI1iIii ( ( O00O0oOO00O00 ) . replace ( '&#039;s' , '' ) , url . replace ( 'https://www.youtube.com/embed/' , '' ) , 8043 , iII111Ii )
 for url in i1ii1II1ii :
  o0OOOOO0O ( ( url ) . replace ( '//' , 'http://' ) )
  if 35 - 35: o00O0oo - o00O0oo + i1IIi - O0 - O0oO
def o0OOOOO0O ( url ) :
 iI1i11 = OoOOoooOO0O ( url )
 OOoOO0oo0ooO = re . compile ( '<link rel="canonical" href="(.+?)">  <link rel="stylesheet"' ) . findall ( iI1i11 )
 for url in OOoOO0oo0ooO :
  iiIi1iI1iIii ( 'PLAY' , ( url ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , oOOoO0 + 'documentary.png' )
  if 58 - 58: I1IiI - oO0o0ooO0 - OoooooooOO
def o00ii111Iiii ( ) :
 o00oOO0o = OoOOoooOO0O ( 'http://www.stream2watch.co/live-tv' )
 OOoOO0oo0ooO = re . compile ( '<a href="(.+?)">.+?<img src="(.+?)" alt=".+?"/>.+?<span class="country_name">(.+?)<br />(.+?)</span>' , re . DOTALL ) . findall ( o00oOO0o )
 for O0o0O00Oo0o0 , iII111Ii , O00O0oOO00O00 , oo0oO0o0 in OOoOO0oo0ooO :
  Oo0o0O00 ( ( O00O0oOO00O00 + '[COLORgreen]' + oo0oO0o0 + '[/COLOR]' ) , O0o0O00Oo0o0 , 8086 , iII111Ii )
  if 44 - 44: O0 + o0oO0 . iIii1I11I1II1 + Oo / O0 - o0000oOoOoO0o
def o0o0OoOOOOOo ( url ) :
 o00oOO0o = OoOOoooOO0O ( url )
 OOoOO0oo0ooO = re . compile ( '<a class="front_channel_href" href="(.+?)" title=".+?">.+?<img class="front_channel_thumb" src="(.+?)" alt=".+?"/>.+?<span class="front_channel_name">(.+?)</span>' , re . DOTALL ) . findall ( o00oOO0o )
 for url , iII111Ii , O00O0oOO00O00 in OOoOO0oo0ooO :
  Oo0o0O00 ( '[COLORgreen]' + O00O0oOO00O00 + '[/COLOR]' , url , 8087 , iII111Ii )
  if 39 - 39: OoooooooOO * OoOO0ooOOoo0O * O0 . o0000oOoOoO0o . Ooo00oOo00o + o0oO0
def II1IIi ( url ) :
 o00oOO0o = OOO00O ( url )
 OOoOO0oo0ooO = re . compile ( 'a id="code_.+?data-f-href="(.+?)" data-code-embed="">(.+?)</a>' , re . DOTALL ) . findall ( o00oOO0o )
 for url , O00O0oOO00O00 in OOoOO0oo0ooO :
  OOoOO0o ( url , O00O0oOO00O00 )
  if 51 - 51: Oo - ii11ii1ii * o0000oOoOoO0o
def OOoOO0o ( url , name ) :
 o00oOO0o = OOO00O ( url )
 OOoOO0oo0ooO = re . compile ( "playStream\('.+?', '(.+?)'\);" , re . DOTALL ) . findall ( o00oOO0o )
 for url in OOoOO0oo0ooO :
  print url
  iiIi1iI1iIii ( '[COLORgreen]' + name + '[/COLOR]' , url , 222 , '' )
  if 12 - 12: iIii1I11I1II1 % o0oO0 % o0oO0
def o0i1iI1iiI1I ( ) :
 iI1i11 = OoOOoooOO0O ( oOo0oooo00o ( 'aHR0cDovL3d3dy5zb2xpZS5vcmcvYWxpYnJhcnkvaW5kZXguaHRtbA==' ) )
 OOoOO0oo0ooO = re . compile ( '<td align="center" valign="top">.+?<a href="(.+?)">.+?<img src="(.+?)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( iI1i11 )
 for O0o0O00Oo0o0 , iII111Ii , O00O0oOO00O00 in OOoOO0oo0ooO :
  Oo0o0O00 ( ( '[COLORgreen]' + O00O0oOO00O00 + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + O0o0O00Oo0o0 , 3002 , 'http://www.solie.org/alibrary/' + iII111Ii )
def oO00oo000O ( url ) :
 iI1i11 = OoOOoooOO0O ( url )
 OOoOO0oo0ooO = re . compile ( '<td align="center" valign="top">.+?<a href="(.+?)">.+?<img src="(.+?)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( iI1i11 )
 for url , iII111Ii , O00O0oOO00O00 in OOoOO0oo0ooO :
  Oo0o0O00 ( ( '[COLORgreen]' + O00O0oOO00O00 + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3003 , 'http://www.solie.org/alibrary/' + iII111Ii )
def ii11 ( url ) :
 iI1i11 = OoOOoooOO0O ( url )
 OOoOO0oo0ooO = re . compile ( '<br><a href="([^"]*)">(.+?)</a>' ) . findall ( iI1i11 )
 oOoo0 = re . compile ( 'href="([^"]*)">Season(.+?)</a>' ) . findall ( iI1i11 )
 next = re . compile ( '<a href="([^"]*)">Episodes</a>' ) . findall ( iI1i11 )
 i1ii1II1ii = re . compile ( '<td align="center" valign="top">.+?<a href="(.+?)">.+?<img src="(.+?)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( iI1i11 )
 for url , O00O0oOO00O00 in OOoOO0oo0ooO :
  iiIi1iI1iIii ( ( '[COLORgreen]' + O00O0oOO00O00 + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3004 , oOOoO0 + 'classicmovies.png' )
 for url , O00O0oOO00O00 in oOoo0 :
  Oo0o0O00 ( '[COLORgreen]Season- ' + O00O0oOO00O00 + '[/COLOR]' , 'http://www.solie.org/alibrary/' + url , 3003 , oOOoO0 + 'classicmovies.png' )
 for url in next :
  Oo0o0O00 ( '[COLORgreen]NEXT[/COLOR]' , 'http://www.solie.org/alibrary/' + url , 3003 , oOOoO0 + 'classicmovies.png' )
 for url , iII111Ii , O00O0oOO00O00 in i1ii1II1ii :
  Oo0o0O00 ( ( '[COLORgreen]' + O00O0oOO00O00 + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3003 , 'http://www.solie.org/alibrary/' + iII111Ii )
def iIiI ( url ) :
 iI1i11 = OoOOoooOO0O ( url )
 OOoOO0oo0ooO = re . compile ( '<iframe.+?src="([^"]*)"' ) . findall ( iI1i11 )
 for url in OOoOO0oo0ooO :
  oO00Ooo0oO ( url )
def oO00Ooo0oO ( url ) :
 iI1i11 = OoOOoooOO0O ( url )
 OOoOO0oo0ooO = re . compile ( '<meta property="og:video" content="([^"]*)"/>' ) . findall ( iI1i11 )
 for url in OOoOO0oo0ooO :
  I1Iiiiiii ( url )
  if 100 - 100: Ooo00oOo00o / i1IIi - OOOo0 % o00O0oo - iIii1I11I1II1
def i11II ( ) :
 iI1i11 = OoOOoooOO0O ( oOo0oooo00o ( 'aHR0cDovL3JldHJvdmlzaW9uLnR2L2FsbC8=' ) )
 OOoOO0oo0ooO = re . compile ( '<a href="([^"]*)"><h2><font color=".+?"><h2>(.+?)</font></h2></a>' ) . findall ( iI1i11 )
 for O0o0O00Oo0o0 , O00O0oOO00O00 in OOoOO0oo0ooO :
  iiIi1iI1iIii ( ( '[COLORgreen]' + O00O0oOO00O00 + '[/COLOR]' ) . replace ( '&#8211;' , ':' ) , O0o0O00Oo0o0 , 8061 , oOOoO0 + 'classicmovies.png' )
def o0oo00o0O0O00 ( url ) :
 iI1i11 = OoOOoooOO0O ( url )
 OOoOO0oo0ooO = re . compile ( "v.src = '([^']*)';" ) . findall ( iI1i11 )
 for url in OOoOO0oo0ooO :
  I1Iiiiiii ( url )
  if 34 - 34: OoOO0ooOOoo0O . Oo
def OOoO0oO00o ( ) :
 iI1i11 = OoOOoooOO0O ( oOo0oooo00o ( 'aHR0cDovL3JldHJvdmlzaW9uLnR2L2NsYXNzaWMtdHYv' ) )
 OOoOO0oo0ooO = re . compile ( '<a href="([^"]*)"><h2><font color=".+?"><h2>(.+?)</font></h2></a>' ) . findall ( iI1i11 )
 for O0o0O00Oo0o0 , O00O0oOO00O00 in OOoOO0oo0ooO :
  iiIi1iI1iIii ( ( '[COLORgreen]' + O00O0oOO00O00 + '[/COLOR]' ) . replace ( '&#8211;' , ':' ) , O0o0O00Oo0o0 , 8061 , oOOoO0 + 'classictv.png' )
def iiiiii1 ( url ) :
 iI1i11 = OoOOoooOO0O ( url )
 OOoOO0oo0ooO = re . compile ( "v.src = '([^']*)';" ) . findall ( iI1i11 )
 for url in OOoOO0oo0ooO :
  I1Iiiiiii ( url )
  if 66 - 66: OoOO * iIii1I11I1II1 % iIii1I11I1II1 * IIII - o0oO0 - IIII
def o0O0oO0 ( ) :
 o00oOO0o = OOO00O ( oOo0oooo00o ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vbTN1c3RyZWFtcw==' ) )
 OOoOO0oo0ooO = re . compile ( '<li><a href="(.+?)"> (.+?).m3u</a></li>' ) . findall ( o00oOO0o )
 for O0o0O00Oo0o0 , O00O0oOO00O00 in OOoOO0oo0ooO :
  Oo0o0O00 ( ( '[COLORgreen]' + O00O0oOO00O00 + '[/COLOR]' ) . replace ( '-' , ' ' ) . replace ( '_' , ' ' ) , ( oOo0oooo00o ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vbTN1c3RyZWFtcy8=' ) ) + O0o0O00Oo0o0 , 8071 , oOOoO0 + 'streams.png' )
def oo0 ( url ) :
 o00oOO0o = OoOOoooOO0O ( url )
 OOoOO0oo0ooO = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( o00oOO0o )
 for O00O0oOO00O00 , url in OOoOO0oo0ooO :
  iiIi1iI1iIii ( ( '[COLORgreen]' + O00O0oOO00O00 + '[/COLOR]' ) . replace ( '_' , ' ' ) , ( url ) . strip ( ) , 404 , oOOoO0 + 'streams.png' )
def i1i1IiIi1 ( url ) :
 o00oOO0o = OoOOoooOO0O ( url )
 OOoOO0oo0ooO = re . compile ( 'EXTINF:(.+?),(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( o00oOO0o )
 for iII111Ii , O00O0oOO00O00 , url in OOoOO0oo0ooO :
  url = ( ( oOo0oooo00o ( 'aHR0cDovL2dlbmlldHYuaXB0di5yZTo4MDAwL2xpdmUv' ) ) + oooOOOOO + '/' + i1iiIII111ii + url ) . strip ( )
  iiIi1iI1iIii ( ( '[COLORgreen]' + O00O0oOO00O00 + '[/COLOR]' ) . replace ( '_' , ' ' ) , url , 222 , iII111Ii )
  if 22 - 22: o0000oOoOoO0o * O0 . OoOoOO00 - Ooo00oOo00o
def o0Oo00OO0 ( ) :
 i11Ii11II1I1 ( 'Best Videos' , 'http://www.xvideos.com/best' , 10105 , oOOoO0 + 'JIZBOX.png' , '' , '' )
 i11Ii11II1I1 ( 'Genres' , 'http://www.xvideos.com' , 10106 , oOOoO0 + 'JIZBOX.png' , '' , '' )
 i11Ii11II1I1 ( 'Recently Uploaded' , 'http://xvideos.com' , 10105 , oOOoO0 + 'JIZBOX.png' , '' , '' )
 i11Ii11II1I1 ( 'Tags' , 'http://www.xvideos.com/tags' , 10103 , oOOoO0 + 'JIZBOX.png' , '' , '' )
 i11Ii11II1I1 ( 'Search' , '' , 10107 , oOOoO0 + 'JIZBOX.png' , '' , '' , )
 if 41 - 41: O0 * o0oO0 - I1IiI . o00O0oo
def oOIIIiI1ii1IIi ( url ) :
 o00oOO0o = OOO00O ( url )
 o0O0oo0o = re . compile ( '<li><a class=".+?".+?href="(.+?)">Next</a></li>' ) . findall ( o00oOO0o )
 for url in o0O0oo0o :
  i11Ii11II1I1 ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10103 , oOOoO0 + 'JIZBOX.png' , '' , '' )
 OOoOO0oo0ooO = re . compile ( '<li><a href="(.+?)"><b>(.+?)</b><span class="navbadge default"(.+?)</span>' ) . findall ( o00oOO0o )
 for url , O00O0oOO00O00 , II11iI1iiI in OOoOO0oo0ooO :
  i11Ii11II1I1 ( O00O0oOO00O00 + ' - No of Videos : ' + ( II11iI1iiI ) . replace ( '>' , '' ) , 'http://www.xvideos.com' + url , 10105 , oOOoO0 + 'JIZBOX.png' , '' , '' )
  if 48 - 48: o0000oOoOoO0o . OoooooooOO . OOOo0 . I1IiI % ii11ii1ii / oO0o0ooO0
def ii1I111i1Ii ( url ) :
 o00oOO0o = OOO00O ( url )
 o0O0oo0o = re . compile ( 'href="([^"]*)">Next</a></li>' ) . findall ( o00oOO0o )
 for url in o0O0oo0o :
  i11Ii11II1I1 ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10104 , oOOoO0 + 'JIZBOX.png' , '' , '' )
 OOoOO0oo0ooO = re . compile ( ':"([^"]*)".+?;</script></a></div></div><p class="profile-name"><a href="([^"]*)">(.+?)</a></p><p class="profile-counts">\n(.+?)\n' , re . DOTALL ) . findall ( o00oOO0o )
 for iII111Ii , url , O00O0oOO00O00 , OOOooO0OO0o in OOoOO0oo0ooO :
  i11Ii11II1I1 ( O00O0oOO00O00 + '--' + OOOooO0OO0o , 'http://www.xvideos.com' + url + '#_tabVideos,videos-best' , 10105 , ( iII111Ii ) . replace ( 'http:\/\/' , 'http://' ) , '' , '' )
  if 10 - 10: o00O0oo - I1IiI . OoooooooOO . OoOO0ooOOoo0O . Ooo00oOo00o * oO0o0ooO0
  if 78 - 78: OoOO / Ooo00oOo00o - OoOO * OoooooooOO . I1IiI
def OOoooOoO0Oo ( url ) :
 o00oOO0o = OOO00O ( url )
 OOoOO0oo0ooO = re . compile ( '<div class="thumb-inside"><script>.+?<img src="(.+?)".+?<a href="(.+?)" title=".+?">(.+?)</a></p>.+?uration">(.+?)</span>.+?Porn quality:(.+?)</span>' , re . DOTALL ) . findall ( o00oOO0o )
 for iII111Ii , url , O00O0oOO00O00 , Oo000 , iiIiII11i1 in OOoOO0oo0ooO :
  Iii111II ( O00O0oOO00O00 + ' - Porn Quality : ' + iiIiII11i1 + ' - ' + Oo000 , 'http://www.xvideos.com' + url , 10108 , iII111Ii , iII111Ii , iiIiII11i1 + ' - ' + Oo000 )
 oOo00Ooo0o0 = re . compile ( '<li><a href="([^"]*)" class="no-page">Next</a></li></ul></div>' ) . findall ( o00oOO0o )
 for url in oOo00Ooo0o0 :
  i11Ii11II1I1 ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10105 , oOOoO0 + 'JIZBOX.png' , '' , '' )
  if 33 - 33: o0000oOoOoO0o
def oOO0 ( url ) :
 o00oOO0o = OOO00O ( url )
 i1Oo00 = re . compile ( '<div class="main-categories">(.+?)</div>' , re . DOTALL ) . findall ( o00oOO0o )
 o0O0oo0o = re . compile ( '<li><a class=".+?".+?href="(.+?)">Next</a></li>' ) . findall ( o00oOO0o )
 for url in o0O0oo0o :
  i11Ii11II1I1 ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10106 , oOOoO0 + 'JIZBOX.png' , '' , '' )
 OOoOO0oo0ooO = re . compile ( '<li><a href="(.+?)" class="btn btn-default">(.+?)</a>' ) . findall ( str ( i1Oo00 ) )
 for url , O00O0oOO00O00 in OOoOO0oo0ooO :
  i11Ii11II1I1 ( O00O0oOO00O00 , 'http://www.xvideos.com' + url , 10105 , oOOoO0 + 'JIZBOX.png' , '' , '' )
  if 15 - 15: Oo + o0000oOoOoO0o . o0oO0 - iIii1I11I1II1 / O0 % iIii1I11I1II1
  if 86 - 86: OOOo0 / OoOO * o00O0oo
def O00o ( ) :
 oooo000 = Oo0o0000o0o0 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oO0o00ooO0OoO = ( oooo000 ) . replace ( ' ' , '+' ) . replace ( '&amp;' , '&' )
 iiII1i1 = oO0o00ooO0OoO . lower ( )
 IIoO00OoOo = 'http://www.xvideos.com/?k=' + iiII1i1
 print IIoO00OoOo + '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'
 o00oOO0o = OOO00O ( IIoO00OoOo )
 OOoOO0oo0ooO = re . compile ( '<div class="thumb-inside"><script>.+?<img src="(.+?)".+?<a href="(.+?)" title=".+?">(.+?)</a></p>.+?uration">(.+?)</span>.+?Porn quality:(.+?)</span>' , re . DOTALL ) . findall ( o00oOO0o )
 for iII111Ii , O0o0O00Oo0o0 , O00O0oOO00O00 , Oo000 , iiIiII11i1 in OOoOO0oo0ooO :
  Iii111II ( O00O0oOO00O00 + ' - Porn Quality : ' + iiIiII11i1 + ' - ' + Oo000 , 'http://www.xvideos.com' + O0o0O00Oo0o0 , 10108 , iII111Ii , iII111Ii , iiIiII11i1 + ' - ' + Oo000 )
 oOo00Ooo0o0 = re . compile ( '<li><a href="([^"]*)" class="no-page">Next</a></li></ul></div>' ) . findall ( o00oOO0o )
 for O0o0O00Oo0o0 in oOo00Ooo0o0 :
  i11Ii11II1I1 ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + O0o0O00Oo0o0 , 10105 , oOOoO0 + 'JIZBOX.png' , '' , '' )
  if 74 - 74: OoOoOO00 . O0 - OOOo0 + IIII % i11iIiiIii % I1IiI
def O0OOO0 ( url ) :
 o00oOO0o = OOO00O ( url )
 OOoOO0oo0ooO = re . compile ( 'flv_url=(.+?)\;' ) . findall ( o00oOO0o )
 for url in OOoOO0oo0ooO :
  IiIi1 = ( url ) . replace ( '%3A' , ':' ) . replace ( '%2F' , '/' ) . replace ( '%3F' , '?' ) . replace ( '%3D' , '=' ) . replace ( '%26' , '&' ) . replace ( '&amp' , '' )
  Oo00o000oOO ( IiIi1 )
  if 37 - 37: O0 - o0000oOoOoO0o
def Oo00o000oOO ( url ) :
 IiI1 = xbmc . Player ( O0oOIiIII ( ) )
 import urlresolver
 try : IiI1 . play ( url )
 except : pass
 if 13 - 13: OOooOOo % OoOO / O0oO % O0oO % O0
 if 90 - 90: IIII . o0oO0 / iIii1I11I1II1
def I1IIi1I ( ) :
 o00oOO0o = OOO00O ( oOo0oooo00o ( 'aHR0cDovL3d3dy5nb2Zpc2hpbmcuY28udWsvQW5nbGluZy1UaW1lcy9TZWN0aW9uL1ZpZGVvcy8=' ) )
 OOoOO0oo0ooO = re . compile ( 'class="item.+?"><a href="(.+?)">(.+?)</a></li>' ) . findall ( o00oOO0o )
 for O0o0O00Oo0o0 , O00O0oOO00O00 in OOoOO0oo0ooO :
  Oo0o0O00 ( '[COLORgreen]' + O00O0oOO00O00 + '[/COLOR]' , ( 'http://www.gofishing.co.uk' + O0o0O00Oo0o0 ) . replace ( 'http://www.gofishing.co.ukhttp://www.gofishing.co.uk' , 'http://www.gofishing.co.uk' ) , 8091 , oOOoO0 + 'gofish.png' )
def iIii1i1 ( url ) :
 o00oOO0o = OoOOoooOO0O ( url )
 OOoOO0oo0ooO = re . compile ( '<h2><a id=.+?href="([^"]*)">(.+?)</a></h2>' , re . DOTALL ) . findall ( o00oOO0o )
 i1ii1II1ii = re . compile ( '<h3><a href="([^"]*)" id=.+?>(.+?)</a> </h3>.+?<img src="([^"]*)"' , re . DOTALL ) . findall ( o00oOO0o )
 next = re . compile ( 'href="([^"]*)">next</a>&gt;</li>' , re . DOTALL ) . findall ( o00oOO0o )
 for url , O00O0oOO00O00 in OOoOO0oo0ooO :
  iiIi1iI1iIii ( '[COLORgreen]' + O00O0oOO00O00 + '[/COLOR]' , 'http://www.gofishing.co.uk/' + url , 8092 , oOOoO0 + 'gofish.png' )
 for url , O00O0oOO00O00 , iII111Ii in i1ii1II1ii :
  iiIi1iI1iIii ( '[COLORgreen]' + O00O0oOO00O00 + '[/COLOR]' , 'http://www.gofishing.co.uk/' + url , 8092 , 'http://www.gofishing.co.uk/' + iII111Ii )
 for url in next :
  Oo0o0O00 ( '[COLORgreen]NEXT[/COLOR]' , url . replace ( ' ' , '+' ) , 8091 , oOOoO0 + 'gofish.png' )
def oOoO00 ( url ) :
 o00oOO0o = OoOOoooOO0O ( url )
 OOoOO0oo0ooO = re . compile ( 'src="https://www.youtube.com/embed/(.+?)"' ) . findall ( o00oOO0o )
 for url in OOoOO0oo0ooO :
  yt . PlayVideo ( url )
  if 45 - 45: o00O0oo . OoooooooOO
def i1iIIi11i111I ( url ) :
 iiiIii = urllib2 . Request ( url )
 iiiIii . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
 iii1IIiI = ''
 Ooo0oOooo0 = ''
 try :
  iii1IIiI = urllib2 . urlopen ( iiiIii )
  Ooo0oOooo0 = iii1IIiI . read ( )
  iii1IIiI . close ( )
 except : pass
 if Ooo0oOooo0 != '' :
  return Ooo0oOooo0
 else :
  Ooo0oOooo0 = 'Failed'
  return Ooo0oOooo0
  if 33 - 33: o0000oOoOoO0o
def oOo00OoO0O ( ) :
 OoOoO0OooOOo = ( oOo0oooo00o ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 oooo000 = Oo0o0000o0o0 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 iiII1i1 = oooo000 . lower ( )
 O0o0O00Oo0o0 = ( oOo0oooo00o ( 'aHR0cDovL2RsNC5tb3ZpZWZhcnNpLmNvbS9maWxtLzIwMTUtNy8=' ) )
 O00ooOo = ( oOo0oooo00o ( 'aHR0cDovL2RsLmF2YWRsLmNvbS9OZXcvTW92aWUv' ) )
 oOIIi = ( oOo0oooo00o ( 'aHR0cDovLzIxNy4yMTkuMTQzLjEwOC8xMzI3Lw==' ) )
 I1Ii1IIiI11i1 = ( oOo0oooo00o ( 'aHR0cDovLzE3OC4xNjIuMjE0LjIzMi92b2QvbW92aWVzL2VuZ2xpc2gv' ) )
 Ii11I1iIiiI = ( oOo0oooo00o ( 'aHR0cDovL3Njb29ieXN0cmVhbS54MTBob3N0LmNvbS8vc2Nvb2J5L21vdi9hbGwucGhw' ) )
 O0o0OO00 = ( oOo0oooo00o ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 iIi11i = ( oOo0oooo00o ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL3NlYXJjaC8/cT0=' ) ) + oooo000
 ooIII1II1iii1i = ( oOo0oooo00o ( 'aHR0cDovL2xldHdhdGNoLnVzLz9vcD1zZWFyY2gmaz0=' ) ) + ( oooo000 ) . replace ( ' ' , '+' )
 if 75 - 75: IIII - I1IiI - iIii1I11I1II1 % OOooOOo
 o00oOO0o = i1iIIi11i111I ( O0o0O00Oo0o0 )
 o0Ooo0O00 = i1iIIi11i111I ( O00ooOo )
 OooooO = i1iIIi11i111I ( oOIIi )
 oO0O0 = i1iIIi11i111I ( I1Ii1IIiI11i1 )
 iI111i11iI1 = i1iIIi11i111I ( Ii11I1iIiiI )
 III1ii = i1iIIi11i111I ( iIi11i )
 iI1III1iIi11 = OOO00O ( ooIII1II1iii1i )
 if 48 - 48: oO0o0ooO0 + IIII
 if o00oOO0o != 'Failed' :
  OOoOO0oo0ooO = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( o00oOO0o )
  for O0o0o0 , O00O0oOO00O00 in OOoOO0oo0ooO :
   if oooo000 in O00O0oOO00O00 . lower ( ) :
    iiIi1iI1iIii ( ( '[COLORgreen]' + O00O0oOO00O00 + '- source 1[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( O0o0O00Oo0o0 + O0o0o0 ) , 222 , '' )
 if o0Ooo0O00 != 'Failed' :
  i1ii1II1ii = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( o0Ooo0O00 )
  for O0o0o0 , O00O0oOO00O00 in i1ii1II1ii :
   if oooo000 in O00O0oOO00O00 . lower ( ) :
    iiIi1iI1iIii ( ( '[COLORgreen]' + O00O0oOO00O00 + '- source 2[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( O00ooOo + O0o0o0 ) , 222 , '' )
 if OooooO != 'Failed' :
  oo00O00oO000o = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( OooooO )
  for O0o0o0 , O00O0oOO00O00 in oo00O00oO000o :
   if oooo000 in O00O0oOO00O00 . lower ( ) :
    iiIi1iI1iIii ( ( '[COLORgreen]' + O00O0oOO00O00 + '- source 3[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( oOIIi + O0o0o0 ) , 222 , '' )
 if oO0O0 != 'Failed' :
  iii = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( oO0O0 )
  for O0o0o0 , O00O0oOO00O00 in iii :
   if oooo000 in O00O0oOO00O00 . lower ( ) :
    iiIi1iI1iIii ( ( '[COLORgreen]' + O00O0oOO00O00 + '- source 4[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( I1Ii1IIiI11i1 + O0o0o0 ) , 222 , '' )
 if iI111i11iI1 != 'Failed' :
  O0o0O = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( iI111i11iI1 )
  for O0o0o0 , iII111Ii , O00O0oOO00O00 in O0o0O :
   if oooo000 in O00O0oOO00O00 . lower ( ) :
    Oo0o0O00 ( ( '[COLORgreen]' + O00O0oOO00O00 + '- source Scooby[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( 'Ganool' , '' ) . replace ( 'ShAaNiG' , '' ) . replace ( 'YIFY' , '' ) . replace ( '[[ Max-Movie.In ]]' , '' ) . replace ( '.mkv' , '' ) . replace ( '.mp4' , '' ) . replace ( '.' , ' ' ) , O0o0o0 , 1006 , 'img' )
    if 6 - 6: OoOoOO00
    OoOo ( 'tvshows' , 'Media Info 3' )
 if III1ii != 'Failed' :
  I11i1iIi111 = re . compile ( 'href="(.+?)".+?src="(.+?)" alt="Image of (.+?)"' , re . DOTALL ) . findall ( III1ii )
  for O0o0O00Oo0o0 , iII111Ii , O00O0oOO00O00 in I11i1iIi111 :
   if oooo000 in O00O0oOO00O00 . lower ( ) :
    Oo0o0O00 ( ( '[COLORgreen]' + O00O0oOO00O00 + '- source Snag[/COLOR]' ) . replace ( '&#x27;' , '' ) , 'http://www.snagfilms.com' + O0o0O00Oo0o0 , 7067 , iII111Ii )
    if 35 - 35: OOooOOo
    OoOo ( 'tvshows' , 'Media Info 3' )
 if iI1III1iIi11 != 'Failed' :
  ooOoooo0 = re . compile ( '<div class="video_block video_block_default ">.+?<a href="#">.+?<a href="(.*?)".+?<img src="(.+?)" height=".+?" alt="(.+?)"' , re . DOTALL ) . findall ( iI1III1iIi11 )
  for O0o0O00Oo0o0 , iII111Ii , O00O0oOO00O00 in ooOoooo0 :
   iiIi1iI1iIii ( '[COLORgreen]' + O00O0oOO00O00 + '- Source 7[/COLOR]' , O0o0O00Oo0o0 , 222 , iII111Ii )
 Ooooo00o0OoO = [ '0-9/' , 'A/' , 'B/' , 'C/' , 'D/' , 'E/' , 'F/' , 'G/' , 'H/' , 'I/' , 'J/' , 'K/' , 'L/' , 'M/' , 'N/' , 'O/' , 'P/' , 'R/' , 'S/' , 'T/' , 'U/' , 'V/' , 'W/' , 'X/' , 'Y/' , 'Z/' ]
 if 54 - 54: i1IIi . o0000oOoOoO0o - ii11ii1ii + o0oO0 + Oo / Oo
 if 22 - 22: o0oO0 . iIii1I11I1II1
 for I1I1i1I in Ooooo00o0OoO :
  oo0oo = OoOoO0OooOOo + I1I1i1I
  i1IiiiiIi1I = i1iIIi11i111I ( oo0oo )
  if iI111i11iI1 != 'Failed' :
   ooo0O0o0OoOO = re . compile ( '<li><a href="(.+?)"> (.+?)</a></li>' ) . findall ( i1IiiiiIi1I )
   for O0o0o0 , O00O0oOO00O00 in ooo0O0o0OoOO :
    if oooo000 in O00O0oOO00O00 . lower ( ) :
     iiIi1iI1iIii ( ( '[COLORgreen]' + O00O0oOO00O00 + 'source 5[/COLOR]' ) . replace ( 'Ganool' , '' ) . replace ( 'ShAaNiG' , '' ) . replace ( 'YIFY' , '' ) . replace ( '[[ Max-Movie.In ]]' , '' ) . replace ( '.mkv' , '' ) . replace ( '.mp4' , '' ) . replace ( '.' , ' ' ) , ( OoOoO0OooOOo + I1I1i1I + O0o0o0 ) , 222 , '' )
     if 9 - 9: Ooo00oOo00o
     OoOo ( 'tvshows' , 'Media Info 3' )
     if 60 - 60: O0oO
     if 98 - 98: o0oO0
def Ii11i1Ii1IIII ( ) :
 if 41 - 41: o00O0oo / OoOoOO00 . I1IiI
 oooo000 = Oo0o0000o0o0 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 iiII1i1 = oooo000 . lower ( )
 ooo = ( oOo0oooo00o ( 'aHR0cDovL2Nvb2x0dnNlcmllcy5jb20vc2VhcmNoLnBocD90YWc9' ) ) + ( oooo000 ) . replace ( ' ' , '+' )
 O0o0O00Oo0o0 = ( oOo0oooo00o ( 'aHR0cDovL2RsLmZhcnNpbW92aWUubmV0L1NlcmlhbC8=' ) )
 O00ooOo = ( oOo0oooo00o ( 'aHR0cDovL3N2Mi5kbC1wYXJzLmluLw==' ) )
 oOIIi = ( oOo0oooo00o ( 'aHR0cDovL3R2LmRsLXBhcnMuaW4v' ) )
 I1Ii1IIiI11i1 = ( oOo0oooo00o ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9BbWVyaWNhbiUyMFNlcmlhbC8=' ) )
 Ii11I1iIiiI = ( oOo0oooo00o ( 'aHR0cDovL2RpemlsYWIuY29tL2Fyc2l2P2xpbWl0PSZ0dXI9Jm9yZGVyYnk9JnVsa2U9Jm9yZGVyPSZ5aWw9JmRpemlfYWRpPQ==' ) ) + ( oooo000 ) . replace ( ' ' , '+' )
 O0o0OO00 = ( oOo0oooo00o ( 'aHR0cDovL3Njb29ieXN0cmVhbS54MTBob3N0LmNvbS8vc2Nvb2J5L3Nob3dzL3R2YWxsLnBocA==' ) )
 ooIII1II1iii1i = ( oOo0oooo00o ( 'aHR0cDovL2xldHdhdGNoLnVzLz9vcD1zZWFyY2gmaz0=' ) ) + ( oooo000 ) . replace ( ' ' , '+' )
 O0oOoo = ( oOo0oooo00o ( 'aHR0cDovL3d3dy53YXRjaHNlcmllcy5saS9zZWFyY2gv' ) ) + ( oooo000 ) . replace ( ' ' , '%20' )
 if 76 - 76: i1IIi % I1IiI - OOOo0 / OOooOOo * o0oO0
 iIiIIiI1i1Ii = i1iIIi11i111I ( ooo )
 o00oOO0o = i1iIIi11i111I ( O0o0O00Oo0o0 )
 o0Ooo0O00 = i1iIIi11i111I ( O00ooOo )
 OooooO = i1iIIi11i111I ( oOIIi )
 oO0O0 = i1iIIi11i111I ( I1Ii1IIiI11i1 )
 iI111i11iI1 = cloudflare . source ( Ii11I1iIiiI )
 i1IiiiiIi1I = i1iIIi11i111I ( O0o0OO00 )
 iI1III1iIi11 = OOO00O ( ooIII1II1iii1i )
 o0OO0OOO0O = OOO00O ( O0oOoo )
 if iIiIIiI1i1Ii != 'Failed' :
  Iii1I = re . compile ( 'href="([^"]*)"><img src="([^"]*)" alt="([^"]*)"' ) . findall ( iIiIIiI1i1Ii )
  for O0o0O00Oo0o0 , iII111Ii , O00O0oOO00O00 in Iii1I :
   if oooo000 in O00O0oOO00O00 . lower ( ) :
    Oo0o0O00 ( '[COLORgreen]' + O00O0oOO00O00 + ' CoolSeries[/COLOR]' , O0o0O00Oo0o0 , 7052 , iII111Ii )
    if 75 - 75: IIII
    OoOo ( 'tvshows' , 'Media Info 3' )
 if o00oOO0o != 'Failed' :
  OOoOO0oo0ooO = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( o00oOO0o )
  for O00O0oOO00O00 in OOoOO0oo0ooO :
   if oooo000 in O00O0oOO00O00 . lower ( ) :
    Oo0o0O00 ( ( '[COLORgreen]' + O00O0oOO00O00 + ' source 1[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( O0o0O00Oo0o0 + O00O0oOO00O00 ) . replace ( ' ' , '%20' ) , 1006 , '' )
    if 35 - 35: OOOo0
    OoOo ( 'tvshows' , 'Media Info 3' )
 if o0Ooo0O00 != 'Failed' :
  i1ii1II1ii = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( o0Ooo0O00 )
  for O00O0oOO00O00 in i1ii1II1ii :
   if oooo000 in O00O0oOO00O00 . lower ( ) :
    Oo0o0O00 ( ( O00O0oOO00O00 + ' source 2' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( O00ooOo + O00O0oOO00O00 ) . replace ( ' ' , '%20' ) , 1006 , '' )
    if 36 - 36: i1IIi - ii11ii1ii - O0oO
    OoOo ( 'tvshows' , 'Media Info 3' )
 if OooooO != 'Failed' :
  oo00O00oO000o = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( OooooO )
  for O00O0oOO00O00 in i1ii1II1ii :
   if oooo000 in O00O0oOO00O00 . lower ( ) :
    Oo0o0O00 ( ( O00O0oOO00O00 + ' source 3' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( oOIIi + O00O0oOO00O00 ) . replace ( ' ' , '%20' ) , 1006 , '' )
    if 7 - 7: i11iIiiIii + OOOo0
    OoOo ( 'tvshows' , 'Media Info 3' )
 if oO0O0 != 'Failed' :
  iii = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( oO0O0 )
  for O00O0oOO00O00 in i1ii1II1ii :
   if oooo000 in O00O0oOO00O00 . lower ( ) :
    Oo0o0O00 ( ( O00O0oOO00O00 + ' source 4' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( I1Ii1IIiI11i1 + O00O0oOO00O00 ) . replace ( ' ' , '%20' ) , 1006 , '' )
    if 47 - 47: O0oO - OoOO0ooOOoo0O / o0oO0 - Oo + oO0o0ooO0 - iIii1I11I1II1
    OoOo ( 'tvshows' , 'Media Info 3' )
 if iI111i11iI1 != 'Failed' :
  O0o0O = re . compile ( '<a href="(.+?)" class="film-image">\n<img src="(.+?)" alt=""/>\n</a>\n<div class="tss-detail">\n<a class="title" style="" href=".+?">\n<span class="position">.+?</span>\n(.+?)</a>' ) . findall ( iI111i11iI1 )
  for O0o0O00Oo0o0 , iII111Ii , O00O0oOO00O00 in O0o0O :
   if oooo000 in O00O0oOO00O00 . lower ( ) :
    Oo0o0O00 ( '[COLORgreen]' + O00O0oOO00O00 + ' - Source - Dizi[/COLOR]' , O0o0O00Oo0o0 , 8062 , iII111Ii )
    if 68 - 68: o00O0oo - OoOO + Oo
    OoOo ( 'tvshows' , 'Media Info 3' )
 if i1IiiiiIi1I != 'Failed' :
  ooo0O0o0OoOO = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( i1IiiiiIi1I )
  for O0o0O00Oo0o0 , iII111Ii , O00O0oOO00O00 in ooo0O0o0OoOO :
   if oooo000 in O00O0oOO00O00 . lower ( ) :
    iiIi1iI1iIii ( ( '[COLORgreen]' + O00O0oOO00O00 + '- Source Scooby[/COLOR]' ) , O0o0O00Oo0o0 , 222 , 'img' )
    if 44 - 44: o00O0oo * OOooOOo * OoOoOO00
    OoOo ( 'tvshows' , 'Media Info 3' )
 if iI1III1iIi11 != 'Failed' :
  ooOoooo0 = re . compile ( '<div class="video_block video_block_default ">.+?<a href="#">.+?<a href="(.*?)".+?<img src="(.+?)" height=".+?" alt="(.+?)"' , re . DOTALL ) . findall ( iI1III1iIi11 )
  for O0o0O00Oo0o0 , iII111Ii , O00O0oOO00O00 in ooOoooo0 :
   iiIi1iI1iIii ( '[COLORgreen]' + O00O0oOO00O00 + ' - Source DiZzY[/COLOR]' , O0o0O00Oo0o0 , 222 , iII111Ii )
 if o0OO0OOO0O != 'Failed' :
  Ii1i1i = re . compile ( '<img src="(.+?)".+?<a href="(.+?)" title=".+?"><b>(.+?)</b>' , re . DOTALL ) . findall ( o0OO0OOO0O )
  for iII111Ii , O0o0O00Oo0o0 , O00O0oOO00O00 in Ii1i1i :
   if 'watch online' in O00O0oOO00O00 :
    pass
   else :
    oOoOooOo0o0 ( '[COLORgreen]' + O00O0oOO00O00 + '- Source WATCH SERIES[/COLOR]' , 'http://www.watchseries.li' + O0o0O00Oo0o0 , 10044 , iII111Ii , '' , '' )
    if 34 - 34: oO0o0ooO0
    xbmcplugin . setContent ( O00o0OO , 'movies' )
    if 48 - 48: OoOO0ooOOoo0O % OOOo0
def ooOOO0oo ( ) :
 if 71 - 71: i1IIi - o0000oOoOoO0o * O0oO + OoOO - Ooo00oOo00o % ii11ii1ii
 oooo000 = Oo0o0000o0o0 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 iiII1i1 = oooo000 . lower ( )
 O0o0O00Oo0o0 = ( oOo0oooo00o ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz' ) )
 o00oOO0o = OOO00O ( O0o0O00Oo0o0 )
 OOoOO0oo0ooO = re . compile ( '"id":".+?","name":"(.+?)","img":"(.+?)","stream_url3":".+?","cat_id":"(.+?)","stream_url2":".+?","stream_url":".+?"}' , re . DOTALL ) . findall ( o00oOO0o )
 for O00O0oOO00O00 , iII111Ii , Ooo0oO in OOoOO0oo0ooO :
  IiIiIIiii1I = oOo0oooo00o ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv' ) + ( iII111Ii ) . replace ( '\\' , '' )
  if oooo000 in O00O0oOO00O00 . lower ( ) :
   Oo0o0O00 ( O00O0oOO00O00 , '' , 7022 , IiIiIIiii1I )
   if 56 - 56: i11iIiiIii - iIii1I11I1II1 . OoOoOO00
 xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 81 - 81: IIII / I1IiI * IIII . O0
 if 61 - 61: Ooo00oOo00o * OoOO0ooOOoo0O + O0oO . iIii1I11I1II1 % o0000oOoOoO0o . O0oO
def O0o0oo0oOO0oO ( url ) :
 iIiIII1iI1111 = cloudflare . source ( url )
 OOoOO0oo0ooO = re . compile ( '<a class="season" href="(.+?)">\n(.+?)\n</a>\n</span>\n<span>\n<a class="episode" href=".+?">\n(.+?)\n</a>\n</span>\n<span>\n<a class="episode-name" href=".+?">\n(.+?)</a>' ) . findall ( iIiIII1iI1111 )
 for url , oOO0o00O , I11iiIi1i1 , O00O0oOO00O00 in OOoOO0oo0ooO :
  Oo0o0O00 ( ( oOO0o00O ) . replace ( 'Sezon' , ' Season ' ) + ( I11iiIi1i1 ) . replace ( 'Bölüm' , ' Episode ' ) + O00O0oOO00O00 , url , 8063 , '' )
  if 37 - 37: i11iIiiIii % OoOO * OoOO0ooOOoo0O * OoOO0ooOOoo0O * o00O0oo
  if 24 - 24: o0oO0 / oO0o0ooO0 + IIII . IIII
  if 39 - 39: o0oO0 + O0 / i1IIi % IIII / OoOO * IIII
  if 77 - 77: IIII . O0oO % I1IiI
def I1111III11 ( url ) :
 iIiIII1iI1111 = cloudflare . source ( url )
 OOoOO0oo0ooO = re . compile ( 'file: "(.+?)",.+?label: "(.+?)",' , re . DOTALL ) . findall ( iIiIII1iI1111 )
 for url , O00O0oOO00O00 in OOoOO0oo0ooO :
  iiIi1iI1iIii ( O00O0oOO00O00 , url , 222 , '' )
  if 46 - 46: O0
  if 65 - 65: iIii1I11I1II1 % OoOO + O0 / OoooooooOO
  if 52 - 52: o00O0oo % OoOO0ooOOoo0O * OOOo0 % o0000oOoOoO0o + OoOO0ooOOoo0O / oO0o0ooO0
  if 80 - 80: OoooooooOO + IIII
def O00O ( ) :
 if 63 - 63: OoooooooOO * OoooooooOO % Ooo00oOo00o + O0 / O0oO + iIii1I11I1II1
 iIiIII1iI1111 = cloudflare . source ( oOo0oooo00o ( 'aHR0cDovL2RpemlsYWIuY29t' ) )
 OOoOO0oo0ooO = re . compile ( '<li id=".+?">.+?<a href="(.+?)">.+?<img width="40" height="40" src="(.+?)" alt=""/>.+?<span class="title">\n(.+?)</span>.+?<span class="alt-title">\n(.+?)</span>.+?</a>.+?</li>' , re . DOTALL ) . findall ( iIiIII1iI1111 )
 for O0o0O00Oo0o0 , iII111Ii , O00O0oOO00O00 , I11iiIi1i1 in OOoOO0oo0ooO :
  Oo0o0O00 ( O00O0oOO00O00 + '  -  ' + ( I11iiIi1i1 ) . replace ( 'sezon' , 'Season' ) . replace ( 'bölüm' , 'Episode' ) , O0o0O00Oo0o0 , 8063 , iII111Ii )
  if 72 - 72: I1IiI * iIii1I11I1II1 % o0000oOoOoO0o
def IiIi1I1i1II ( ) :
 iI1i11 = OoOOoooOO0O ( oOo0oooo00o ( 'aHR0cDovL3d3dy50dmd1aWRlLmNvLnVrLw==' ) )
 OOoOO0oo0ooO = re . compile ( '<a href="(.+?)"  qt-title=".+?" qt-text=".+?<br> .+?" title="(.+?)".+?class=".+? src="(.+?)" alt=".+?" /></a>' , re . DOTALL ) . findall ( iI1i11 )
 for O0o0O00Oo0o0 , O00O0oOO00O00 , iII111Ii in OOoOO0oo0ooO :
  iiIi1iI1iIii ( '[COLORgreen]' + O00O0oOO00O00 + '[/COLOR]' , O0o0O00Oo0o0 , 8002 , iII111Ii )
def iI1I1 ( url ) :
 iI1i11 = OoOOoooOO0O ( url )
 OOoOO0oo0ooO = re . compile ( '<table border="0".+?url((.+?));background-repeat: no-repeat;">.+?<tr>.+?<span class="season">(.+?)</span><br>.+?<a href="(.+?)"+?>(.+?)</span><br>.+?<span class="programmetext">(.+?)</span></a><br>' , re . DOTALL ) . findall ( iI1i11 )
 for iII111Ii , time , url , O00O0oOO00O00 , I1iiIIIi11 in OOoOO0oo0ooO :
  oOoOooOo0o0 ( '%s %s' % ( '[COLORgreen]' + O00O0oOO00O00 + '[/COLOR]' , time ) , url , 1015 , iII111Ii , I1iiIIIi11 )
  if 46 - 46: iIii1I11I1II1
def I111iiiii1 ( ) :
 if 100 - 100: ii11ii1ii * i11iIiiIii % OoOO / Oo / o0oO0 + ii11ii1ii
 Oo0o0O00 ( 'Coronation Street' , '' , 8001 , '' )
 Oo0o0O00 ( 'Eastenders' , '' , 8002 , '' )
 Oo0o0O00 ( 'Emmerdale' , '' , 8003 , '' )
 Oo0o0O00 ( 'Hollyoaks' , '' , 8004 , '' )
 Oo0o0O00 ( 'Im a Celebrity' , '' , 8005 , '' )
 if 59 - 59: O0oO - IIII
 if 14 - 14: iIii1I11I1II1 - iIii1I11I1II1
 if 5 - 5: IIII
 if 84 - 84: OoOoOO00 * OoOO * OoOoOO00 % IIII / OOOo0
def O0Oooo ( ) :
 o00oOO0o = OOO00O ( 'http://uksoapshare.blogspot.co.uk/' )
 OOoOO0oo0ooO = re . compile ( '<a href="(.+?)".+?target=_blank>(.+?)</a>' ) . findall ( o00oOO0o )
 for O0o0O00Oo0o0 , O00O0oOO00O00 in OOoOO0oo0ooO :
  if 'Holly' in O00O0oOO00O00 :
   iII111Ii = 'http://2.bp.blogspot.com/-9c7Sieh1RKs/UjD6TGAEEnI/AAAAAAAAAC8/84uwHfxcuYg/s1600/Hollyoaks.png'
   if 'huge' in O0o0O00Oo0o0 :
    iiIi1iI1iIii ( ( O00O0oOO00O00 ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , O0o0O00Oo0o0 . replace ( '\\/' , '/' ) , 8006 , iII111Ii )
   else :
    pass
    if 27 - 27: o0oO0 + i11iIiiIii * o0000oOoOoO0o + I1IiI + oO0o0ooO0
 xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE_IGNORE_THE ) ;
 if 87 - 87: O0
def oOo0 ( ) :
 o00oOO0o = OOO00O ( 'http://uksoapshare.blogspot.co.uk/' )
 OOoOO0oo0ooO = re . compile ( '<a href="(.+?)".+?target=_blank>(.+?)</a>' ) . findall ( o00oOO0o )
 for O0o0O00Oo0o0 , O00O0oOO00O00 in OOoOO0oo0ooO :
  if 'East' in O00O0oOO00O00 :
   iII111Ii = 'http://3.bp.blogspot.com/-KWHcNbNJU8Y/Vi1ousRl7fI/AAAAAAAAAT8/ksNE12LH0nE/s1600/eastenders.jpg'
   if 'huge' in O0o0O00Oo0o0 :
    iiIi1iI1iIii ( ( O00O0oOO00O00 ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , O0o0O00Oo0o0 . replace ( '\\/' , '/' ) , 8006 , iII111Ii )
   else :
    pass
    if 59 - 59: OOooOOo * Ooo00oOo00o - o00O0oo . OoOO0ooOOoo0O
 xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 89 - 89: OoOO0ooOOoo0O
def o00oo0OO0 ( ) :
 o00oOO0o = OOO00O ( 'http://uksoapshare.blogspot.co.uk/' )
 OOoOO0oo0ooO = re . compile ( '<a href="(.+?)".+?target=_blank>(.+?)</a>' ) . findall ( o00oOO0o )
 for O0o0O00Oo0o0 , O00O0oOO00O00 in OOoOO0oo0ooO :
  if 'Emmer' in O00O0oOO00O00 :
   iII111Ii = 'http://2.bp.blogspot.com/-UfDcxisVV5c/UjH9vUicZ3I/AAAAAAAAADc/8Ozuiz1ojxw/s1600/Emmerdale.jpg'
   if 'huge' in O0o0O00Oo0o0 :
    iiIi1iI1iIii ( ( O00O0oOO00O00 ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , O0o0O00Oo0o0 . replace ( '\\/' , '/' ) , 8006 , iII111Ii )
   else :
    pass
    if 60 - 60: o0oO0
 xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 66 - 66: o0000oOoOoO0o / o0oO0 % i1IIi - OoOO . O0 / O0
def oo00o0 ( ) :
 o00oOO0o = OOO00O ( 'http://uksoapshare.blogspot.co.uk/' )
 OOoOO0oo0ooO = re . compile ( '<a href="(.+?)".+?target=_blank>(.+?)</a>' ) . findall ( o00oOO0o )
 for O0o0O00Oo0o0 , O00O0oOO00O00 in OOoOO0oo0ooO :
  if 'Coro' in O00O0oOO00O00 :
   iII111Ii = 'http://3.bp.blogspot.com/-hofvfBQVexs/UjErIfNdS4I/AAAAAAAAADQ/Q-vVGu3apYU/s1600/corrie.jpg'
   if 'huge' in O0o0O00Oo0o0 :
    iiIi1iI1iIii ( ( O00O0oOO00O00 ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , O0o0O00Oo0o0 . replace ( '\\/' , '/' ) , 8006 , iII111Ii )
   else :
    pass
    if 17 - 17: o00O0oo / iIii1I11I1II1 - Ooo00oOo00o + OOOo0 % OoOO0ooOOoo0O
 xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 14 - 14: OOooOOo % IIII + ii11ii1ii + Ooo00oOo00o
def OOOoOOo0o ( ) :
 o00oOO0o = OOO00O ( 'http://uksoapshare.blogspot.co.uk/' )
 OOoOO0oo0ooO = re . compile ( '<a href="(.+?)" target="_blank">(.+?)</a>' ) . findall ( o00oOO0o )
 for O0o0O00Oo0o0 , O00O0oOO00O00 in OOoOO0oo0ooO :
  if 'Celeb' in O00O0oOO00O00 :
   iII111Ii = 'http://3.bp.blogspot.com/-a_yDotWU_pY/VkotKWaG_gI/AAAAAAAAAUk/8Q5iNM6p37k/s1600/iacgoh.jpg'
   if 'huge' in O0o0O00Oo0o0 :
    iiIi1iI1iIii ( ( O00O0oOO00O00 ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , O0o0O00Oo0o0 . replace ( '\\/' , '/' ) , 8006 , iII111Ii )
   else :
    pass
    if 50 - 50: OoOoOO00 - O0oO + iIii1I11I1II1 + iIii1I11I1II1
def OoooooOo ( name , url ) :
 OooOo = urlresolver . HostedMediaFile ( url ) . valid_url ( )
 if OooOo :
  oOo0I1Ii11i = urlresolver . HostedMediaFile ( url ) . resolve ( )
 else :
  iI1i11 = open_url ( url )
  url = re . compile ( 'src="(.+?)"></iframe>' ) . findall ( iI1i11 ) [ 0 ]
  url = url . split ( '?autoplay' ) [ 0 ]
  iI1i11 = open_url ( url )
  I1iIiiiI1 = re . compile ( 'mp4","url":"(.+?)"' ) . findall ( iI1i11 ) [ - 1 ]
  oOo0I1Ii11i = I1iIiiiI1 . replace ( '\\/' , '/' )
 II1I1iiIII1I1 = xbmcgui . ListItem ( name , '' , '' )
 II1I1iiIII1I1 . setPath ( oOo0I1Ii11i )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , II1I1iiIII1I1 )
 if 87 - 87: I1IiI - o0oO0 - OoOO0ooOOoo0O + Oo % iIii1I11I1II1 / i11iIiiIii
 if 12 - 12: o0oO0
def oOOO0ooOO ( ) :
 iI1i11 = OOO00O ( oOo0oooo00o ( 'aHR0cDovL3d3dy5kaXppYm94aGQuY29tLw==' ) )
 OOoOO0oo0ooO = re . compile ( 'class="film menu-item menu-item-type-post_type menu-item-object-page menu-item-36980"><a href="(.+?)"><i class="fa fa-film"></i><span>(.+?)</span></a></li>' ) . findall ( iI1i11 )
 i1ii1II1ii = re . compile ( 'class="menu-item menu-item-type-post_type menu-item-object-page menu-item-52949"><a href="(.+?)"><i class="fa fa-"></i><span>(.+?)</span></a></li>' ) . findall ( iI1i11 )
 for O0o0O00Oo0o0 , O00O0oOO00O00 in OOoOO0oo0ooO :
  Oo0o0O00 ( ( '[COLORgreen]' + O00O0oOO00O00 + '[/COLOR]' ) . replace ( 'Diziler' , 'Series' ) , O0o0O00Oo0o0 , 7071 , oOOoO0 + 'popcorn.png' )
 for O0o0O00Oo0o0 , O00O0oOO00O00 in i1ii1II1ii :
  Oo0o0O00 ( ( '[COLORgreen]' + O00O0oOO00O00 + '[/COLOR]' ) . replace ( 'Filmler' , 'Movies' ) , O0o0O00Oo0o0 , 7071 , oOOoO0 + 'popcorn.png' )
  if 3 - 3: OoooooooOO
def O0OoO0o ( ) :
 iI1i11 = OOO00O ( oOo0oooo00o ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL2NhdGVnb3JpZXMv' ) )
 OOoOO0oo0ooO = re . compile ( '<a class="nav-item" href="(.+?)">(.+?)</a>' ) . findall ( iI1i11 )
 for O0o0O00Oo0o0 , O00O0oOO00O00 in OOoOO0oo0ooO :
  if 'Movies' in O00O0oOO00O00 :
   Oo0o0O00 ( '[COLORgreen]' + O00O0oOO00O00 + '[/COLOR]' , 'http://www.snagfilms.com' + ( O0o0O00Oo0o0 ) . replace ( 'http://www.snagfilms.com' , '' ) , 7061 , oOOoO0 + 'popcorn.png' )
def I111IIiIII ( url ) :
 iI1i11 = OOO00O ( url )
 OOoOO0oo0ooO = re . compile ( '<a class="object-link size-poster".+?href="(.+?)" data-type="category">.+?src="(.+?)" alt="Image of (.+?)" />' , re . DOTALL ) . findall ( iI1i11 )
 OOoOO0oo0ooO = re . compile ( '<a class="object-link size-poster".+?href="(.+?)" data-type="category">.+?src="(.+?)" alt="Image of (.+?)" />' , re . DOTALL ) . findall ( iI1i11 )
 i1ii1II1ii = re . compile ( "<li class='current'>.+?</li><li ><a href='(.+?)'>.+?</a></li><li" , re . DOTALL ) . findall ( iI1i11 )
 for url , iII111Ii , O00O0oOO00O00 in OOoOO0oo0ooO :
  Oo0o0O00 ( '[COLORgreen]' + O00O0oOO00O00 + '[/COLOR]' , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7067 , iII111Ii )
 for url in i1ii1II1ii :
  Oo0o0O00 ( '[COLORgreen]NEXT PAGE[/COLOR]' , ( url ) . replace ( '&#038;' , '&' ) , 7063 , oOOoO0 + 'popcorn.png' )
  if 62 - 62: I1IiI % OOooOOo % OOOo0 + IIII . Ooo00oOo00o
  if 48 - 48: OOOo0 * i11iIiiIii % OoOoOO00
def ii1I ( url ) :
 iI1i11 = OOO00O ( oOo0oooo00o ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL2NhdGVnb3JpZXMv' ) )
 OOoOO0oo0ooO = re . compile ( '<a class="object-link size-poster".+?href="(.+?)" data-type="category">.+?src="(.+?)" alt="Image of (.+?)" />' , re . DOTALL ) . findall ( iI1i11 )
 for url , iII111Ii , O00O0oOO00O00 in OOoOO0oo0ooO :
  Oo0o0O00 ( '[COLORgreen]' + O00O0oOO00O00 + '[/COLOR]' , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7062 , iII111Ii )
  if 61 - 61: iIii1I11I1II1 - o0000oOoOoO0o / oO0o0ooO0 * o0000oOoOoO0o % o00O0oo % oO0o0ooO0
  if 63 - 63: OoOO0ooOOoo0O % iIii1I11I1II1
def II1 ( url ) :
 iI1i11 = OOO00O ( url )
 OOoOO0oo0ooO = re . compile ( 'href="(.+?)".+?src="(.+?)" alt="Image of (.+?)"' , re . DOTALL ) . findall ( iI1i11 )
 for url , iII111Ii , O00O0oOO00O00 in OOoOO0oo0ooO :
  Oo0o0O00 ( ( '[COLORgreen]' + O00O0oOO00O00 + '[/COLOR]' ) . replace ( '&#x27;' , '' ) , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7067 , iII111Ii )
  if 31 - 31: i11iIiiIii . IIII
def i1iiIIiiiII ( url ) :
 iI1i11 = OOO00O ( url )
 OOoOO0oo0ooO = re . compile ( '<div class="film-container">.+?<iframe src="(.+?)"' , re . DOTALL ) . findall ( iI1i11 )
 for url in OOoOO0oo0ooO :
  Ii1I1OO0ooO0 ( 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) )
  if 95 - 95: iIii1I11I1II1 . IIII - OoooooooOO * Ooo00oOo00o / OOooOOo
def Ii1I1OO0ooO0 ( url ) :
 iI1i11 = OOO00O ( url )
 OOoOO0oo0ooO = re . compile ( 'file: "(.+?)",.+?label: "(.+?)"' , re . DOTALL ) . findall ( iI1i11 )
 for url , O00O0oOO00O00 in OOoOO0oo0ooO :
  iiIi1iI1iIii ( '[COLORgreen]' + O00O0oOO00O00 + '[/COLOR]' , url , 222 , oOOoO0 + 'popcorn.png' )
  if 74 - 74: OoOO
  if 34 - 34: oO0o0ooO0
  if 44 - 44: i1IIi % OOOo0 % OOooOOo
  if 9 - 9: Oo % OoooooooOO - o00O0oo
def iIII11Iiii1 ( url ) :
 iI1i11 = OOO00O ( url )
 OOoOO0oo0ooO = re . compile ( '</h4><p><ul><li><a href="([^"]*)">(.+?)<.+?class=' ) . findall ( iI1i11 )
 i1ii1II1ii = re . compile ( '<li><a href="([^"]*)">(.+?)<.+?class=' ) . findall ( iI1i11 )
 for url , O00O0oOO00O00 in OOoOO0oo0ooO :
  if '(cooltvseries.com)' in O00O0oOO00O00 :
   iiIi1iI1iIii ( ( '[COLORgreen]' + O00O0oOO00O00 + ' -(360)-[/COLOR]' ) . replace ( ' - (cooltvseries.com).mp4' , '' ) , url , 7053 , oOOoO0 + 'CoolSeries.png' )
 for url , O00O0oOO00O00 in i1ii1II1ii :
  if '(cooltvseries.com)' in O00O0oOO00O00 :
   iiIi1iI1iIii ( ( '[COLORgreen]' + O00O0oOO00O00 + '[/COLOR]' ) . replace ( ' - (cooltvseries.com).mp4' , '' ) , url , 7053 , oOOoO0 + 'CoolSeries.png' )
def o0oo0 ( url ) :
 iI1i11 = OOO00O ( url )
 OOoOO0oo0ooO = re . compile ( '<source type="video/mp4" src="([^"]*)"/>' ) . findall ( iI1i11 )
 for url in OOoOO0oo0ooO :
  I1Iiiiiii ( ( url ) . replace ( ' ' , '%20' ) )
  if 67 - 67: O0 * o0000oOoOoO0o - OOooOOo - OoOoOO00
  if 41 - 41: OOOo0 - O0oO % OoOoOO00 . O0oO - o0000oOoOoO0o
def i1I111Ii ( ) :
 iI1i11 = OOO00O ( oOo0oooo00o ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vc2VjcmV0L2Nsb3VkLnBocA==' ) )
 OOoOO0oo0ooO = re . compile ( '<li class="col-sm-2">.+?<a href="#" class="thumbnail" data-src="(.+?)" data-toggle="modal".+?data-target="#infoModal" name="(.+?)"> <img src="(.+?)" alt=".+?" width="130px"' , re . DOTALL ) . findall ( iI1i11 )
 for O0o0O00Oo0o0 , O00O0oOO00O00 , iII111Ii in OOoOO0oo0ooO :
  iiIi1iI1iIii ( '[COLORgreen]' + O00O0oOO00O00 + '[/COLOR]' , 'http://stream.cloudtv.bz/stream/channel/20/' + ( oOo0oooo00o ( O0o0O00Oo0o0 ) ) , 222 , iII111Ii )
  if 31 - 31: OOOo0
def O0oI1ii1Ii1 ( url ) :
 iI1i11 = OOO00O ( url )
 OOoOO0oo0ooO = re . compile ( 'src="([^"]*)".+?alt=""></a><div class="entry unvoted"><p class="title"><a class="title may-blank " href="([^"]*)" tabindex=.+?>(.+?)</a>' , re . DOTALL ) . findall ( iI1i11 )
 next = re . compile ( '<a href="([^"]*)" rel="nofollow next"' , re . DOTALL ) . findall ( iI1i11 )
 for iII111Ii , url , O00O0oOO00O00 in OOoOO0oo0ooO :
  if 'youtu' in url :
   iiIi1iI1iIii ( ( '[COLORgreen]' + O00O0oOO00O00 + '[/COLOR]' ) . replace ( '&quot;' , '"' ) . replace ( '&amp;' , ' & ' ) , url , 7051 , 'http:' + iII111Ii )
 for url in next :
  Oo0o0O00 ( '[COLORgreen]NEXT[/COLOR]' , url , 7050 , oOOoO0 + 'concerts.png' )
  if 73 - 73: O0 . OoOO + i11iIiiIii + iIii1I11I1II1 - o0000oOoOoO0o / I1IiI
def OO0OOOOo0000O ( url ) :
 iI1i11 = OOO00O ( url )
 OOoOO0oo0ooO = re . compile ( 'rel="shortlink" href="([^"]*)">' , re . DOTALL ) . findall ( iI1i11 )
 for url in OOoOO0oo0ooO :
  yt . PlayVideo ( ( url ) . replace ( 'https://youtu.be/' , '' ) )
  if 25 - 25: oO0o0ooO0 - Oo
def Iii1IIIIIII ( url ) :
 iI1i11 = OOO00O
 OOoOO0oo0ooO = re . compile ( 'id:"(.+?)",url:"(.+?)"' , re . DOTALL ) . findall ( iI1i11 )
 for url , iII111Ii , O00O0oOO00O00 in OOoOO0oo0ooO :
  Oo0o0O00 ( '[COLORgreen]' + O00O0oOO00O00 + '[/COLOR]' , url , 222 , iII111Ii )
  if 27 - 27: Ooo00oOo00o + I1IiI * o0oO0
  if 83 - 83: iIii1I11I1II1
  if 72 - 72: o0000oOoOoO0o
  if 87 - 87: i1IIi
  if 48 - 48: Oo * OoOO * iIii1I11I1II1 + i11iIiiIii - OoooooooOO
def II1iI ( ) :
 if 5 - 5: i1IIi * I1IiI % OOOo0 . Ooo00oOo00o * ii11ii1ii - O0oO
 Oo0o0O00 ( 'All Channels' , '' , 7021 , oOOoO0 + 'livetv.png' )
 Oo0o0O00 ( 'Entertainment' , '' , 7021 , oOOoO0 + 'livetv.png' )
 Oo0o0O00 ( 'Movies' , '' , 7021 , oOOoO0 + 'livetv.png' )
 Oo0o0O00 ( 'Music' , '' , 7021 , oOOoO0 + 'livetv.png' )
 Oo0o0O00 ( 'News' , '' , 7021 , oOOoO0 + 'livetv.png' )
 Oo0o0O00 ( 'Sports' , '' , 7021 , oOOoO0 + 'livetv.png' )
 Oo0o0O00 ( 'Documentary' , '' , 7021 , oOOoO0 + 'livetv.png' )
 Oo0o0O00 ( 'Kids' , '' , 7021 , oOOoO0 + 'livetv.png' )
 Oo0o0O00 ( 'Food' , '' , 7021 , oOOoO0 + 'livetv.png' )
 Oo0o0O00 ( 'Religious' , '' , 7021 , oOOoO0 + 'livetv.png' )
 Oo0o0O00 ( 'USA Channels' , '' , 7021 , oOOoO0 + 'livetv.png' )
 Oo0o0O00 ( 'Other' , '' , 7021 , oOOoO0 + 'livetv.png' )
 if 79 - 79: OoOO % OOooOOo % I1IiI
 if 45 - 45: OOOo0 * OoOO0ooOOoo0O % Ooo00oOo00o
def i111I11I ( Cat_Name ) :
 if 80 - 80: iIii1I11I1II1 - OoooooooOO - ii11ii1ii - ii11ii1ii . OoooooooOO
 I1i = False
 I11I = '0'
 if Cat_Name == 'All Channels' : I1i = True
 if Cat_Name == 'Entertainment' : I11I = '1'
 if Cat_Name == 'Movies' : I11I = '2'
 if Cat_Name == 'Music' : I11I = '3'
 if Cat_Name == 'News' : I11I = '4'
 if Cat_Name == 'Sports' : I11I = '5'
 if Cat_Name == 'Documentary' : I11I = '6'
 if Cat_Name == 'Kids' : I11I = '7'
 if Cat_Name == 'Food' : I11I = '8'
 if Cat_Name == 'Religious' : I11I = '9'
 if Cat_Name == 'USA Channels' : I11I = '10'
 if Cat_Name == 'Other' : I11I = '11'
 if 81 - 81: i11iIiiIii + i11iIiiIii * Ooo00oOo00o + IIII
 iI1i11 = OOO00O ( oOo0oooo00o ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz' ) )
 OOoOO0oo0ooO = re . compile ( '"id":".+?","name":"(.+?)","img":"(.+?)","stream_url3":".+?","cat_id":"(.+?)","stream_url2":".+?","stream_url":".+?"}' , re . DOTALL ) . findall ( iI1i11 )
 print 'Len Match: >>>' + str ( len ( OOoOO0oo0ooO ) )
 for O00O0oOO00O00 , iII111Ii , Ooo0oO in OOoOO0oo0ooO :
  IiIiIIiii1I = oOo0oooo00o ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv' ) + ( iII111Ii ) . replace ( '\\' , '' )
  if Ooo0oO == I11I :
   Oo0o0O00 ( O00O0oOO00O00 , '' , 7022 , IiIiIIiii1I )
  elif I1i == True :
   Oo0o0O00 ( O00O0oOO00O00 , '' , 7022 , IiIiIIiii1I )
  else : pass
  if 32 - 32: O0 . OoooooooOO
  xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 15 - 15: OOOo0 . Ooo00oOo00o
def IiiIi ( Search_Name ) :
 iI1i11 = OOO00O ( oOo0oooo00o ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz' ) )
 OOoOO0oo0ooO = re . compile ( '"id":".+?","name":"' + Search_Name + '","img":"(.+?)","stream_url3":"(.+?)","cat_id":".+?","stream_url2":"(.+?)","stream_url":"(.+?)"}' , re . DOTALL ) . findall ( iI1i11 )
 OOoOO0oo0ooO = re . compile ( '"id":".+?","name":"' + Search_Name + '","img":"(.+?)","stream_url3":"(.+?)","cat_id":".+?","stream_url2":"(.+?)","stream_url":"(.+?)"}' , re . DOTALL ) . findall ( iI1i11 )
 for iII111Ii , O0o0O00Oo0o0 , O00ooOo , oOIIi in OOoOO0oo0ooO :
  IiIiIIiii1I = oOo0oooo00o ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv' ) + ( iII111Ii ) . replace ( '\\' , '' )
  iiIi1iI1iIii ( Search_Name + ': Link 1' , ( O0o0O00Oo0o0 ) . replace ( '\\' , '' ) , 222 , IiIiIIiii1I )
  iiIi1iI1iIii ( Search_Name + ': Link 2' , ( O00ooOo ) . replace ( '\\' , '' ) , 222 , IiIiIIiii1I )
  iiIi1iI1iIii ( Search_Name + ': Link 3' , ( oOIIi ) . replace ( '\\' , '' ) , 222 , IiIiIIiii1I )
  if 42 - 42: oO0o0ooO0 + iIii1I11I1II1
def II1IiiIII ( ) :
 iI1i11 = OOO00O ( oOo0oooo00o ( oo ( 0 , [ 97 ] , [ 221 , 72 , 245 , 82 , 68 , 48 , 242 , 99 , 143 , 68 , 9 , 111 , 24 , 118 , 180 , 76 , 29 , 51 , 14 , 100 , 187 , 51 , 105 , 100 , 106 , 121 , 52 , 53 , 240 , 114 , 26 , 98 , 252 , 50 , 197 , 82 , 218 , 112 , 19 , 99 , 94 , 71 , 54 , 120 , 104 , 108 , 174 , 101 , 107 , 72 , 168 , 82 , 191 , 50 , 88 , 76 , 90 , 109 , 138 , 78 , 24 , 118 , 89 , 76 , 218 , 110 , 231 , 86 , 105 , 114 , 252 , 76 , 37 , 50 , 36 , 82 , 96 , 118 , 27 , 100 , 120 , 50 , 160 , 53 , 72 , 115 , 200 , 98 , 80 , 50 , 201 , 70 , 114 , 107 , 9 , 99 , 113 , 121 , 127 , 57 , 155 , 106 , 213 , 97 , 194 , 71 , 192 , 70 , 162 , 116 , 27 , 99 , 46 , 71 , 191 , 108 , 4 , 118 , 24 , 98 , 27 , 109 , 105 , 108 , 89 , 119 , 164 , 100 , 88 , 72 , 237 , 89 , 93 , 117 , 40 , 98 , 211 , 84 , 75 , 78 , 216 , 49 ] ) ) )
 OOoOO0oo0ooO = re . compile ( '#EXTINF:-1,(.+)\s*(.+)\s*' ) . findall ( iI1i11 )
 for O00O0oOO00O00 , O0o0O00Oo0o0 in OOoOO0oo0ooO :
  iiIi1iI1iIii ( O00O0oOO00O00 , ( O0o0O00Oo0o0 ) . replace ( '"' , ' ' ) . replace ( '&amp;' , '&' ) . strip ( ) + '|connection=keep-alive' , 222 , oOOoO0 + 'english.png' )
def ii11iI1iIiIi ( ) :
 iI1i11 = OOO00O ( oOo0oooo00o ( oo ( 0 , [ 97 ] , [ 221 , 72 , 245 , 82 , 68 , 48 , 242 , 99 , 143 , 68 , 9 , 111 , 24 , 118 , 180 , 76 , 29 , 51 , 14 , 100 , 187 , 51 , 105 , 100 , 106 , 121 , 52 , 53 , 240 , 114 , 26 , 98 , 252 , 50 , 197 , 82 , 218 , 112 , 19 , 99 , 94 , 71 , 54 , 120 , 104 , 108 , 174 , 101 , 107 , 72 , 168 , 82 , 191 , 50 , 88 , 76 , 90 , 109 , 138 , 78 , 24 , 118 , 89 , 76 , 218 , 110 , 231 , 86 , 105 , 114 , 252 , 76 , 37 , 50 , 36 , 82 , 96 , 118 , 27 , 100 , 120 , 50 , 160 , 53 , 72 , 115 , 200 , 98 , 80 , 50 , 201 , 70 , 114 , 107 , 9 , 99 , 113 , 121 , 127 , 57 , 155 , 106 , 213 , 97 , 194 , 71 , 192 , 70 , 162 , 116 , 27 , 99 , 46 , 71 , 191 , 108 , 4 , 118 , 24 , 98 , 27 , 109 , 105 , 108 , 89 , 119 , 164 , 100 , 88 , 72 , 237 , 89 , 93 , 117 , 40 , 98 , 211 , 84 , 75 , 78 , 216 , 49 ] ) ) )
 OOoOO0oo0ooO = re . compile ( '#EXTINF:-2,(.+)\s*(.+)\s*' ) . findall ( iI1i11 )
 for O00O0oOO00O00 , O0o0O00Oo0o0 in OOoOO0oo0ooO :
  iiIi1iI1iIii ( O00O0oOO00O00 , ( O0o0O00Oo0o0 ) . replace ( '"' , ' ' ) . replace ( '&amp;' , '&' ) . strip ( ) , 222 , oOOoO0 + 'xxx.png' )
def o0OO0OoO0o0o0 ( ) :
 iI1i11 = OOO00O ( oOo0oooo00o ( oo ( 0 , [ 97 , 129 , 72 , 149 , 82 , 100 , 48 , 63 , 99 , 170 , 68 , 159 , 111 , 42 , 118 , 83 , 76 , 128 , 51 , 61 , 100 , 44 , 51 , 201 , 100 , 148 , 121 , 134 , 53 ] , [ 159 , 114 , 70 , 98 , 144 , 50 , 37 , 82 , 253 , 112 , 184 , 99 , 50 , 71 , 154 , 120 , 110 , 108 , 179 , 101 , 250 , 72 , 65 , 82 , 125 , 50 , 52 , 76 , 28 , 109 , 124 , 78 , 191 , 118 , 193 , 76 , 193 , 110 , 145 , 86 , 92 , 114 , 193 , 76 , 41 , 50 , 82 , 82 , 206 , 118 , 32 , 100 , 163 , 50 , 209 , 53 , 191 , 115 , 42 , 98 , 30 , 50 , 237 , 70 , 26 , 107 , 70 , 99 , 64 , 121 , 115 , 57 , 230 , 116 , 32 , 97 , 39 , 88 , 58 , 104 , 38 , 50 , 77 , 98 , 185 , 50 , 86 , 81 , 80 , 117 , 111 , 98 , 226 , 84 , 75 , 78 , 210 , 49 ] ) ) )
 OOoOO0oo0ooO = re . compile ( '#EXTINF:.+?,(.+)\s*(.+)\s*' ) . findall ( iI1i11 )
 for O00O0oOO00O00 , O0o0O00Oo0o0 in OOoOO0oo0ooO :
  iiIi1iI1iIii ( O00O0oOO00O00 , ( O0o0O00Oo0o0 ) . replace ( '"' , ' ' ) . replace ( '&amp;' , '&' ) . strip ( ) , 222 , oOOoO0 + 'vod(1).png' )
  if 49 - 49: Oo * OoOO + OOooOOo - i11iIiiIii
def OOooO ( url ) :
 url
 i1i1Ii1Ii = xbmcgui . ListItem ( O00O0oOO00O00 , path = url )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , i1i1Ii1Ii )
 return
 if 99 - 99: ii11ii1ii + OoOO0ooOOoo0O . OoOO
 if 1 - 1: OoOO0ooOOoo0O * IIII + o0000oOoOoO0o
def OOoo000O00O ( url ) :
 iI1i11 = OOO00O ( url )
 OOoOO0oo0ooO = re . compile ( '<a class=.+?href="(.+?)">.+?<div class="videothumboverlay hidden-xs" id=".+?">(.+?)</div>.+?<div class="videothumbbox"><img src="(.+?)" class="videothumb" alt="(.+?)"></div>' , re . DOTALL ) . findall ( iI1i11 )
 i1ii1II1ii = re . compile ( "<a href='(.+?)' class='paginationnext'>Next &raquo;</a></div>" ) . findall ( iI1i11 )
 for url , IIi11IIiIii1 , iII111Ii , O00O0oOO00O00 in OOoOO0oo0ooO :
  oOoOooOo0o0 ( O00O0oOO00O00 , 'https://www.fitnessblender.com' + url , 7086 , 'https://www.fitnessblender.com' + iII111Ii , '' , ( IIi11IIiIii1 ) . replace ( '</p>' , ' ' ) . replace ( '<p>' , ' ' ) )
  OoOo ( 'tvshows' , 'Media Info 3' )
 for url in i1ii1II1ii :
  Oo0o0O00 ( 'NEXT' , 'https://www.fitnessblender.com' + url , 7085 , oOOoO0 + 'FITNESS.png' )
  if 18 - 18: i11iIiiIii % O0oO + i1IIi + OoOoOO00 . O0oO
def ii1iIIi11 ( url ) :
 o00oOO0o = OOO00O ( url )
 OOoOO0oo0ooO = re . compile ( '<div class=\'videowrapper\'><iframe width="700" height="394" src="//www.youtube.com/embed/(.+?)?rel=0&amp;wmode=transparent" frameborder="0"></iframe></div>.+?<div class="col-xs-6 col-md-2 rightborder">(.+?)</div>.+?<p class="videodetailvalue"><img src=\'(.+?)\'/></p>' , re . DOTALL ) . findall ( o00oOO0o )
 for url , IIi11IIiIii1 , iII111Ii in OOoOO0oo0ooO :
  Iii111II ( 'PLAY' , url , 8043 , 'https://www.fitnessblender.com' + iII111Ii , '' , IIi11IIiIii1 )
  OoOo ( 'tvshows' , 'Media Info 3' )
 IIi = re . compile ( '<h2 class="videodetailheader">Workout Details</h2>(.+?)</div>' , re . DOTALL ) . findall ( o00oOO0o )
 for iI1IIIII1Ii in IIi :
  iIiI1 = ( iI1IIIII1Ii ) . replace ( '<p>' , '' ) . replace ( '</p>' , '' ) . replace ( '<br />' , '' ) . replace ( '&nbsp;' , '' ) . replace ( '<strong>' , '' ) . replace ( '</strong>' , '' ) . replace ( '"' , '' ) . replace ( '<' , '' ) . replace ( '>' , '' ) . replace ( 'a href' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&rsquo;t' , '' ) . replace ( '&amp;' , '&' )
  oOoOooOo0o0 ( 'INFO' , '' , 7087 , 'https://www.fitnessblender.com' + iII111Ii , '' , iIiI1 )
  if 20 - 20: OoOO0ooOOoo0O * OoOoOO00 - I1IiI - OoOO * O0oO
def I1i1II1 ( INFO ) :
 oOOooI1 ( 'info for workout' , INFO )
 if 98 - 98: i1IIi . OOOo0 . OoOO
 if 10 - 10: ii11ii1ii % OOOo0 - OoOoOO00
 if 11 - 11: O0 + OOOo0
def OO0OOoooo0o ( url ) :
 iI1i11 = OOO00O ( url )
 OOoOO0oo0ooO = re . compile ( 'cat-item-.+?"><a href="(.+?)" >(.+?)</a>' ) . findall ( iI1i11 )
 for url , O00O0oOO00O00 in OOoOO0oo0ooO :
  Oo0o0O00 ( O00O0oOO00O00 , url , 9031 , oOOoO0 + 'icon.png' )
def IiIi1Ii ( url ) :
 iI1i11 = OOO00O ( url )
 OOoOO0oo0ooO = re . compile ( '<a href="(.+?)" title=".+?" rel="bookmark"><time class="entry-date published updated" datetime=".+?">(.+?)</time></a>' ) . findall ( iI1i11 )
 for url , O00O0oOO00O00 in OOoOO0oo0ooO :
  Oo0o0O00 ( O00O0oOO00O00 , url , 9032 , oOOoO0 + 'icon.png' )
def iiIIiI11II1 ( url ) :
 iI1i11 = OOO00O ( url )
 OOoOO0oo0ooO = re . compile ( '#EXTINF:-.+?,(.+)\s*(.+)\s*' ) . findall ( iI1i11 )
 for O00O0oOO00O00 , url in OOoOO0oo0ooO :
  if '://' in O00O0oOO00O00 :
   pass
   iiIi1iI1iIii ( ( O00O0oOO00O00 ) . replace ( '<br />' , '' ) , ( url ) . replace ( '<br />' , '' ) , 222 , oOOoO0 + 'icon.png' )
def oooOo ( url ) :
 iI1i11 = OOO00O ( url )
 OOoOO0oo0ooO = re . compile ( 'EXTINF:-.+?,(.+)</div></li><li class=".+?"><div class=".+?">(.+?)</div>).findall' ) . findall ( iI1i11 )
 for O00O0oOO00O00 , url in OOoOO0oo0ooO :
  iiIi1iI1iIii ( O00O0oOO00O00 , url , 222 , oOOoO0 + 'icon.png' )
  if 79 - 79: OoOO - OoOoOO00
  if 43 - 43: i1IIi + O0 % Ooo00oOo00o / o00O0oo * OOOo0
  if 89 - 89: OOOo0 . Oo + ii11ii1ii . O0 % OOooOOo
def Ooo00O0 ( ) :
 iI1i11 = OOO00O ( 'http://www.disclose.tv/action/videolist/aliens/page/1/all/channel/1/category/1/' )
 OOoOO0oo0ooO = re . compile ( '<li><a href="([^"]*)">(.+?)</a></li>' ) . findall ( iI1i11 )
 for O0o0O00Oo0o0 , O00O0oOO00O00 in OOoOO0oo0ooO :
  Oo0o0O00 ( O00O0oOO00O00 , 'http://www.disclose.tv/' + O0o0O00Oo0o0 , 7010 , oOOoO0 + 'disclose.png' )
  if 70 - 70: OOOo0 - o0oO0 - Ooo00oOo00o - I1IiI . i11iIiiIii % i1IIi
  if 1 - 1: OoOO / i1IIi
def O0oo0 ( url ) :
 iI1i11 = OOO00O ( url )
 OOoOO0oo0ooO = re . compile ( 'href="([^"]*)"><img width="135" height="76" alt="([^"]*)".+?src="([^"]*)" />' , re . DOTALL ) . findall ( iI1i11 )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' ) . findall ( iI1i11 )
 for url , O00O0oOO00O00 , iII111Ii in OOoOO0oo0ooO :
  Oo0o0O00 ( O00O0oOO00O00 , 'http://www.disclose.tv/' + url , 7011 , iII111Ii )
 for url in next :
  Oo0o0O00 ( 'NEXT' , url , 7010 , iII111Ii )
  if 37 - 37: i11iIiiIii
  if 12 - 12: ii11ii1ii / o00O0oo
def ii11Ii11 ( url ) :
 iI1i11 = OOO00O ( url )
 OOoOO0oo0ooO = re . compile ( 'url: "([^"]*)",' , re . DOTALL ) . findall ( iI1i11 )
 i1ii1II1ii = re . compile ( "src='([^']*)' type='([^']*)' />" , re . DOTALL ) . findall ( iI1i11 )
 for url in OOoOO0oo0ooO :
  if 'http' in url :
   iiIi1iI1iIii ( 'video/flv' , url , 222 , oOOoO0 + 'disclose.png' )
 for url , O00O0oOO00O00 in i1ii1II1ii :
  iiIi1iI1iIii ( O00O0oOO00O00 , url , 222 , oOOoO0 + 'disclose.png' )
  if 3 - 3: o00O0oo + O0oO . i1IIi / OoOO0ooOOoo0O % O0oO
  if 98 - 98: IIII * iIii1I11I1II1 . o00O0oo * Oo / ii11ii1ii + o0oO0
def iiI1ii111 ( url ) :
 iI1i11 = OOO00O ( url )
 OOoOO0oo0ooO = re . compile ( '<div id="play-1".+?src="(.+?)" scrolling="no".+?<li><a href="#play-1">(.+?)</a></li>' , re . DOTALL ) . findall ( iI1i11 )
 for url , O00O0oOO00O00 in OOoOO0oo0ooO :
  Oo0o0O00 ( O00O0oOO00O00 , ( url + '&fv=&sou=' ) . replace ( 'player' , 'watch' ) , 7000 , oOOoO0 + 'icon.png' )
  if 97 - 97: O0 / OoOO0ooOOoo0O + OOooOOo . OoOO % I1IiI - I1IiI
def i1IiI1Iiii ( name , url , img ) :
 o00oOO0o = OOO00O ( url )
 o0O0O = re . compile ( '<iframe class="playerframe" src="(.+?)" scrolling=".+?" marginwidth=".+?" marginheight=".+?" vspace=".+?" hspace=".+?" allowfullscreen=".+?" webkitallowfullscreen=".+?" mozallowfullscreen=".+?" width=".+?" height=".+?" frameborder=".+?"></iframe>' , re . DOTALL ) . findall ( o00oOO0o )
 oOOoOOO0oOoo = len ( o0O0O )
 if 65 - 65: oO0o0ooO0 . OoOO - o00O0oo
 if 93 - 93: O0
 if oOOoOOO0oOoo == 1 :
  for iii1o00000oo00 in o0O0O :
   iii1o00000oo00 = iii1o00000oo00 . replace ( 'player' , 'watch' )
   iIII1iIi = iii1o00000oo00 + '&fv=&sou='
   o000O0oo = OOO00O ( iIII1iIi )
   OOOO = re . compile ( '<source src="(.+?)" type=".+?">' , re . DOTALL ) . findall ( o000O0oo )
   for ii1I1I111 in OOOO :
    oo00OO0O0Ooo0 = False
    Resolve ( ii1I1I111 )
    if 93 - 93: o0oO0
 elif oOOoOOO0oOoo > 1 :
  if 34 - 34: OoOO - o0oO0 * Oo / OOooOOo
  for iii1o00000oo00 in o0O0O :
   iI1iiIi1 = OOO00O ( iii1o00000oo00 )
   i1iiiIi1Iii = re . compile ( '<iframe width=".*?" height=".*?" frameborder=".*?" src="(.*?)" scrolling=".*?" marginwidth=".*?" marginheight=".*?" vspace=".*?" hspace=".*?" allowfullscreen=".*?" webkitallowfullscreen=".*?" mozallowfullscreen=".*?"></iframe>' , re . DOTALL ) . findall ( iI1iiIi1 )
   o0oO0O = i1iiiIi1Iii
   o0oO0O = ( str ( o0oO0O ) ) . replace ( '[\'' , '' ) . replace ( '\']' , '' ) ;
   print 'Stripped url : ' + o0oO0O
   iiIi1iI1iIii ( 'DOUBLE LINK' , o0oO0O , 424 , '' )
   if 61 - 61: OOooOOo - OoOoOO00 % iIii1I11I1II1 . Oo . OOooOOo % O0oO
   for url in i1iiiIi1Iii :
    Oo0o0O00 ( 'DOUBLE LINK' , url , 424 , '' )
    try :
     O00ooOo = Google . resolve ( url )
    except :
     pass
    try :
     o0o0O00o = re . findall ( r"{'url': u'(.*?)', 'quality': 'HD'}, {'url': u'(.*?)', 'quality': 'SD'}" , str ( O00ooOo ) )
     for Oo00 , III1 in o0o0O00o :
      if 24 - 24: OoOO / O0oO / o0000oOoOoO0o % I1IiI / ii11ii1ii * o0oO0
      HD_URLS . append ( Oo00 )
      SD_URLS . append ( III1 )
    except :
     pass
 else :
  pass
  if 8 - 8: o00O0oo
def iIIi1 ( ) :
 if 75 - 75: IIII % i11iIiiIii + iIii1I11I1II1
 if 92 - 92: I1IiI % O0
 Oo0o0O00 ( 'Genres' , 'http://cnfstudio.com/movies/' , 7002 , oOOoO0 + 'Movies.png' )
 if 55 - 55: iIii1I11I1II1 * oO0o0ooO0
 Oo0o0O00 ( 'Search Movies' , '' , 7017 , oOOoO0 + 'Movies.png' )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 85 - 85: iIii1I11I1II1 . OoOoOO00
 if 54 - 54: o00O0oo . OoooooooOO % Oo
def ii111I11Ii ( ) :
 iI1i11 = OOO00O ( 'http://cnfstudio.com/' )
 OOoOO0oo0ooO = re . compile ( '<a href="http://cnfstudio.com/genre/(.+?)">(.+?)</a>' ) . findall ( iI1i11 )
 for O0o0O00Oo0o0 , O00O0oOO00O00 in OOoOO0oo0ooO :
  Oo0o0O00 ( O00O0oOO00O00 , 'http://cnfstudio.com/genre/' + O0o0O00Oo0o0 , 7003 , oOOoO0 + 'icon.png' )
  if 6 - 6: o00O0oo
ii11iIi1I = xbmcgui . Dialog ( )
if 77 - 77: i1IIi + Ooo00oOo00o . OOOo0 * OoOO0ooOOoo0O / IIII / o00O0oo
if 84 - 84: Ooo00oOo00o / iIii1I11I1II1
def IiI1iiIiII ( url ) :
 iI1i11 = OOO00O ( url )
 OOoOO0oo0ooO = re . compile ( '<div class="movie">.+?<img src="(.+?)" alt=".+?" />.+?<a href="(.+?)"><span class="player"></span></a>.+?<h2>(.+?)</h2>' , re . DOTALL ) . findall ( iI1i11 )
 IIiiiI1iI = re . compile ( "<link rel='next' href='(.+?)'/>" ) . findall ( iI1i11 )
 for iII111Ii , url , O00O0oOO00O00 in OOoOO0oo0ooO :
  iiIi1iI1iIii ( ( O00O0oOO00O00 ) . replace ( '&#038;' , '' ) . replace ( '&#8216;' , '' ) . replace ( '&#8217;' , '' ) . replace ( '&#8211;' , '' ) , url , 7004 , iII111Ii )
 IIiiiI1iI = IIiiiI1iI
 for url in IIiiiI1iI :
  Oo0o0O00 ( 'Next Page' , url , 7003 , '' )
  if 100 - 100: o0oO0 / o0oO0 - OoOO0ooOOoo0O % OoOO0ooOOoo0O * OoOO / IIII
def IIIIIIi ( url ) :
 if 59 - 59: OoOO / OOOo0 * o00O0oo % O0 - OoOoOO00 + OoooooooOO
 iI1i11 = OOO00O ( url )
 OOoOO0oo0ooO = re . compile ( '<div id="play-1" class="player-content"><iframe class="playerframe" src="(.+?)" scrolling="no".+?</div>' , re . DOTALL ) . findall ( iI1i11 )
 for url in OOoOO0oo0ooO :
  Ooo0oOooo0 = url + '&fv=&sou='
  Ooo0oOooo0 = Ooo0oOooo0 . replace ( 'player' , 'watch' )
  iI11iiI1I1Iii = oO0O ( Ooo0oOooo0 )
  IIIiIi1iiI = oO0O ( url )
  if 15 - 15: ii11ii1ii . oO0o0ooO0
  if 94 - 94: o0000oOoOoO0o . OOOo0
def oO0O ( url ) :
 if 73 - 73: i1IIi / OoOoOO00
 iI1i11 = OOO00O ( url )
 OOoOO0oo0ooO = re . compile ( '<video id=".+?<source src="(.+?)" type="video/mp4">' , re . DOTALL ) . findall ( iI1i11 )
 for url in OOoOO0oo0ooO :
  I1i1I ( url )
  if 17 - 17: o0000oOoOoO0o - oO0o0ooO0 % o00O0oo
  if 2 - 2: o00O0oo * ii11ii1ii * OoooooooOO
def oOOOooO ( ) :
 oOoOooOo0o0 ( '[COLORgreen]Local M3u[/COLOR]' , i1iiIIiiI111 , 2001 , oOOoO0 + 'loader.png' , OOooO0OOoo , '' )
 oOoOooOo0o0 ( '[COLORgreen]Remote M3u[/COLOR]' , oO , 1009 , oOOoO0 + 'loader.png' , OOooO0OOoo , '' )
 if 16 - 16: OOooOOo . o0000oOoOoO0o
def I1IIIIIi1IIiI ( url ) :
 OOoOO0oo0ooO = re . compile ( '^#EXTINF:-?[0-9]*(.*?),(.*?)\n(.*?)$' , re . I + re . M + re . U + re . S ) . findall
 for III11I11ii , O00O0oOO00O00 , url in OOoOO0oo0ooO :
  iiIi1iI1iIii ( O00O0oOO00O00 , url , 222 , oOOoO0 + 'streams.png' )
  if 82 - 82: OoOO0ooOOoo0O % OoOoOO00 - OoOO0ooOOoo0O + OoOoOO00
  if 61 - 61: i11iIiiIii * OoOO % Oo * O0oO - OoooooooOO - Ooo00oOo00o
def o0OOo ( ) :
 oOoOooOo0o0 ( '[COLORgreen]CATAGORIES[/COLOR]' , '' , 10051 , oOOoO0 + 'loader.png' , OOooO0OOoo , '' )
 oOoOooOo0o0 ( '[COLORgreen]SEARCH[/COLOR]' , '' , 10052 , oOOoO0 + 'loader.png' , OOooO0OOoo , '' )
 if 42 - 42: O0 % o00O0oo - iIii1I11I1II1 + O0oO % OOOo0 + o0oO0
 if 82 - 82: O0
o0oOoO00o = xbmcaddon . Addon ( id = 'plugin.video.GenieTv' )
Oo0o0000o0o0 = xbmcgui . Dialog ( )
iI111I11I1I1 = xbmc . translatePath ( 'special://home/' )
i1111 = xbmcgui . DialogProgress ( )
O0oO0oo0O = 'https://addons.tvaddons.ag/'
if 82 - 82: OoooooooOO . o00O0oo
def III1iiiII1ii ( ) :
 oooo000 = Oo0o0000o0o0 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 iiII1i1 = oooo000 . lower ( )
 IIoO00OoOo = 'https://addons.tvaddons.ag/search/?keyword=' + iiII1i1
 o00oOO0o = OOO00O ( IIoO00OoOo )
 OOoOO0oo0ooO = re . compile ( '<li><a href="(.+?)"><span class=".+?"><img src="(.+?)" width=".+?" alt=".+?" class=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( o00oOO0o )
 for O0o0O00Oo0o0 , ooo00Ooo , O00O0oOO00O00 in OOoOO0oo0ooO :
  oOoOooOo0o0 ( O00O0oOO00O00 , O0o0O00Oo0o0 , 10054 , 'https://addons.tvaddons.ag/' + ooo00Ooo , OOooO0OOoo , '' )
  if 76 - 76: ii11ii1ii
  if 99 - 99: OOooOOo
def I11IIII1111II ( ) :
 o00oOO0o = OOO00O ( O0oO0oo0O )
 OOoOO0oo0ooO = re . compile ( '<li><a href="(.+?)"><span class="thumbnail"><img src="(.+?)" class="pic" alt=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( o00oOO0o )
 for O0o0O00Oo0o0 , iII111Ii , O00O0oOO00O00 in OOoOO0oo0ooO :
  if 'Repositories' in O00O0oOO00O00 :
   pass
  elif 'Services' in O00O0oOO00O00 :
   pass
  elif 'International' in O00O0oOO00O00 :
   pass
  else :
   oOoOooOo0o0 ( '[COLORgreen]' + O00O0oOO00O00 + '[/COLOR]' , O0o0O00Oo0o0 , 10053 , 'https://addons.tvaddons.ag/' + iII111Ii , OOooO0OOoo , '' )
   if 6 - 6: iIii1I11I1II1 / OoOO0ooOOoo0O + o0000oOoOoO0o
   if 89 - 89: OoOO
def Addon ( url ) :
 o00oOO0o = OOO00O ( url )
 o0OOOOOo00 = re . compile ( '<li class="nextPage"><a class=".+?" href="(.+?)"><dfn title="next Page">.+?</dfn></a></li>' ) . findall ( o00oOO0o )
 for url in o0OOOOOo00 :
  oOoOooOo0o0 ( '[COLORgreen]NEXT PAGE[/COLOR]' , 'https://addons.tvaddons.ag' + url , 10053 , oOOoO0 + 'streams.png' , OOooO0OOoo , '' )
 OOoOO0oo0ooO = re . compile ( '<li><a href="(.+?)"><span class=".+?"><img src="(.+?)" width=".+?" alt=".+?" class=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( o00oOO0o )
 for url , iII111Ii , O00O0oOO00O00 in OOoOO0oo0ooO :
  if 'Please' in O00O0oOO00O00 :
   pass
  else :
   oOoOooOo0o0 ( O00O0oOO00O00 , url , 10054 , 'https://addons.tvaddons.ag/' + iII111Ii , OOooO0OOoo , '' )
   if 82 - 82: Oo
   if 5 - 5: Ooo00oOo00o / Ooo00oOo00o - O0 - O0oO + O0oO
def O0oooOO0Oo0o ( url , name ) :
 o00oOO0o = OOO00O ( url )
 OOoOO0oo0ooO = re . compile ( '<a href="(.+?)"' ) . findall ( o00oOO0o )
 for url in OOoOO0oo0ooO :
  if 'plugin' in url :
   print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<' + url
   OOoOoo = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
   i1111 = xbmcgui . DialogProgress ( )
   i1111 . create ( "Origin+Jaybox" , "Downloading Content" , '' , 'Please Wait' )
   I1IiI11 = os . path . join ( OOoOoo , name + '.zip' )
   try :
    os . remove ( I1IiI11 )
   except :
    pass
   downloader . download ( url , I1IiI11 , i1111 )
   Ii1i1 = xbmc . translatePath ( os . path . join ( 'special://home' , 'addons' ) )
   time . sleep ( 2 )
   i1111 . update ( 0 , "" , "Extracting Zip Please Wait" )
   print '======================================='
   print Ii1i1
   print '======================================='
   extract . all ( I1IiI11 , Ii1i1 , i1111 )
   O0o ( )
   if 68 - 68: OoooooooOO * iIii1I11I1II1 + i1IIi - i1IIi
def O0o ( ) :
 xbmc . executebuiltin ( 'UpdateLocalAddons' )
 xbmc . executebuiltin ( 'UpdateAddonRepos' )
 ii11iIi1I = xbmcgui . Dialog ( )
 ii11iIi1I . ok ( "Origin + Genie TV" , '' , '                                 REFRESH SUCCESSFUL :)' , "                          [COLOR gold]Brought To You By Origin + Jaybox[/COLOR]" )
 return
 if 76 - 76: Ooo00oOo00o . OoooooooOO % O0oO * o00O0oo
 if 23 - 23: IIII + iIii1I11I1II1
def Ii1111III1 ( ) :
 iI1i11 = OoOOoooOO0O ( oOo0oooo00o ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvc2NyYXBlZC9jYXRzLnBocA==' ) )
 OOoOO0oo0ooO = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( iI1i11 )
 for O0o0O00Oo0o0 , ooo00Ooo , O00O0oOO00O00 in OOoOO0oo0ooO :
  Oo0o0O00 ( O00O0oOO00O00 , O0o0O00Oo0o0 , 1007 , ooo00Ooo )
def oO00oooo0 ( url ) :
 iI1i11 = OoOOoooOO0O ( url )
 OOoOO0oo0ooO = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( iI1i11 )
 for url , ooo00Ooo , O00O0oOO00O00 in OOoOO0oo0ooO :
  Oo0o0O00 ( '[COLORgreen]' + O00O0oOO00O00 + '[/COLOR]' , url , 1006 , ooo00Ooo )
  if 94 - 94: Oo . o0oO0 * i11iIiiIii - OOooOOo . oO0o0ooO0
  if 98 - 98: OoOO0ooOOoo0O + o00O0oo
def OOOOIIIIiI11Ii1i ( url ) :
 iI1i11 = OoOOoooOO0O ( url )
 OOoOO0oo0ooO = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( iI1i11 )
 for url , iiIiIIIiiI , IIi11IIiIii1 , iiI1IIIi , O00O0oOO00O00 in OOoOO0oo0ooO :
  if '.php' in url :
   i1i1IIii1i1 ( O00O0oOO00O00 , url , 1016 , iiIiIIIiiI , iiI1IIIi , IIi11IIiIii1 )
   OoOo ( 'tvshows' , 'Media Info 3' )
  else :
   if 'youtube' in url :
    I1iIII1 ( O00O0oOO00O00 , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , iiIiIIIiiI , iiI1IIIi , IIi11IIiIii1 )
   else :
    I1iIII1 ( O00O0oOO00O00 , url , 222 , iiIiIIIiiI , iiI1IIIi , IIi11IIiIii1 )
   OoOo ( 'tvshows' , 'Media Info 3' )
   if 100 - 100: oO0o0ooO0 + o0000oOoOoO0o + o0oO0 + oO0o0ooO0 / i1IIi
 else :
  OOoOO0oo0ooO = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( iI1i11 )
  for url , ooo00Ooo , O00O0oOO00O00 in OOoOO0oo0ooO :
   if '.php' in url :
    Oo0o0O00 ( O00O0oOO00O00 , url , 1016 , ooo00Ooo )
   else :
    if 'youtube' in url :
     print '>>>>>>>>>>>>>>>>>>>>>>> youtube old way'
     iiIi1iI1iIii ( O00O0oOO00O00 , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , ooo00Ooo )
    else :
     iiIi1iI1iIii ( O00O0oOO00O00 , url , 222 , ooo00Ooo )
     if 74 - 74: O0 % OoooooooOO * Oo + OoOO0ooOOoo0O * oO0o0ooO0
     if 100 - 100: OoOO0ooOOoo0O + o00O0oo * OOooOOo + OoOoOO00
  xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 70 - 70: Oo * iIii1I11I1II1
def O00Ooo0ooo0 ( ) :
 iI1i11 = OoOOoooOO0O ( oOo0oooo00o ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vdm9kL3VybHMvdXJsLnBocA==' ) )
 OOoOO0oo0ooO = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( iI1i11 )
 for O0o0O00Oo0o0 , ooo00Ooo , O00O0oOO00O00 in OOoOO0oo0ooO :
  Oo0o0O00 ( O00O0oOO00O00 , O0o0O00Oo0o0 , 1007 , ooo00Ooo )
def oO00o0O00o ( url ) :
 iI1i11 = OoOOoooOO0O ( url )
 OOoOO0oo0ooO = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( iI1i11 )
 for url , ooo00Ooo , O00O0oOO00O00 in OOoOO0oo0ooO :
  Oo0o0O00 ( '[COLORgreen]' + O00O0oOO00O00 + '[/COLOR]' , url , 1006 , ooo00Ooo )
  if 98 - 98: o0oO0 . OoOO0ooOOoo0O
def OOooO00OO ( name , url , iconimage = None ) :
 print '--- Playing "{0}". {1}' . format ( name , url )
 O00OoOOoo = xbmcgui . ListItem ( path = url , thumbnailImage = iconimage )
 O00OoOOoo . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , O00OoOOoo )
 if 49 - 49: i11iIiiIii - ii11ii1ii - o0000oOoOoO0o / OoooooooOO % I1IiI
 if 65 - 65: O0 - O0oO . o00O0oo
def IIOOO00o0 ( url ) :
 iI1i11 = OoOOoooOO0O ( url )
 OOoOO0oo0ooO = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( iI1i11 )
 for url , iII111Ii , O00O0oOO00O00 in OOoOO0oo0ooO :
  Oo0o0O00 ( '[COLORgreen]' + O00O0oOO00O00 + '[/COLOR]' , url , 1006 , iII111Ii )
def OOoO ( url ) :
 iI1i11 = OoOOoooOO0O ( url )
 IiIi1 = url
 OOoOO0oo0ooO = re . compile ( "<a href='(.+?)'>(.+?)</a>" ) . findall ( iI1i11 )
 for url , O00O0oOO00O00 in OOoOO0oo0ooO :
  if '.mp3' in O00O0oOO00O00 :
   print '<<<<<<<<<<<<<<<<<<<' + url + '>>>>>>>>>>>>>>>>>>>>>>>>>>>'
   iiIi1iI1iIii ( ( O00O0oOO00O00 ) . replace ( '.mp3' , '' ) . replace ( '/' , '' ) , 'http://hypem.com' + url , 222 , oOOoO0 + 'music.png' )
  else :
   Oo0o0O00 ( ( O00O0oOO00O00 ) . replace ( '/' , '' ) , IiIi1 + url , 1011 , oOOoO0 + 'music.png' )
def oooO0 ( ) :
 iI1i11 = OoOOoooOO0O ( oOo0oooo00o ( 'aHR0cDovL3d3dy5jeW4ubmV0L211c2ljLw==' ) )
 OOoOO0oo0ooO = re . compile ( '<td><a href="(.+?)"><img src="(.+?)"><br>(.+?)</a></td>' , re . DOTALL ) . findall ( iI1i11 )
 for O0o0O00Oo0o0 , iII111Ii , O00O0oOO00O00 in OOoOO0oo0ooO :
  Oo0o0O00 ( O00O0oOO00O00 , ( 'http://www.cyn.net/music/' + O0o0O00Oo0o0 ) . replace ( ' ' , '%20' ) , 1031 , ( 'http://www.cyn.net/music/' + iII111Ii ) . replace ( ' ' , '%20' ) )
def oO0oo0O0 ( url , img ) :
 iI1i11 = OoOOoooOO0O ( url )
 O00ooOo = url
 img = img
 OOoOO0oo0ooO = re . compile ( '<a href="(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( iI1i11 )
 for url , O00O0oOO00O00 in OOoOO0oo0ooO :
  iiIi1iI1iIii ( ( O00O0oOO00O00 ) . replace ( '.mp3' , '' ) , ( O00ooOo + '/' + url ) . replace ( ' ' , '%20' ) , 222 , img )
  if 66 - 66: OoOO0ooOOoo0O - o0oO0 - Oo
  if 54 - 54: oO0o0ooO0 . i1IIi
def i1IiIiIiiI1 ( ) :
 OoOoO0OooOOo = ( oOo0oooo00o ( 'aHR0cDovL2h5cGVtLmNvbS9kb3dubG9hZC8=' ) )
 oooo000 = Oo0o0000o0o0 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 iiII1i1 = oooo000 . lower ( )
 O0o0O00Oo0o0 = ( oOo0oooo00o ( 'aHR0cDovL3Bhbmljc3RyZWFtLm5ldC9zdHJlYW1zLw==' ) )
 O00ooOo = ( oOo0oooo00o ( 'aHR0cDovL21hc2xvdmQubm8taXAub3JnL3B1YmxpYy9tcDMv' ) )
 oOIIi = ( oOo0oooo00o ( 'aHR0cDovL3d3dy5jeW4ubmV0L211c2ljLw==' ) )
 if 41 - 41: OoOoOO00
 o00oOO0o = i1iIIi11i111I ( O0o0O00Oo0o0 )
 o0Ooo0O00 = i1iIIi11i111I ( O00ooOo )
 OooooO = i1iIIi11i111I ( oOIIi )
 if 43 - 43: O0 - o0oO0 % OoooooooOO % OoOO0ooOOoo0O + oO0o0ooO0
 if o00oOO0o != 'Failed' :
  OOoOO0oo0ooO = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( o00oOO0o )
  for O00O0oOO00O00 in OOoOO0oo0ooO :
   if oooo000 in O00O0oOO00O00 . lower ( ) :
    Oo0o0O00 ( ( O00O0oOO00O00 + ' source 1' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( O0o0O00Oo0o0 + O00O0oOO00O00 ) . replace ( ' ' , '%20' ) , 1006 , '' )
    if 61 - 61: o0oO0 . i11iIiiIii + OoOO
    OoOo ( 'tvshows' , 'Media Info 3' )
 if o0Ooo0O00 != 'Failed' :
  i1ii1II1ii = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( o00oOO0o )
  for O00O0oOO00O00 in i1ii1II1ii :
   if oooo000 in O00O0oOO00O00 . lower ( ) :
    Oo0o0O00 ( ( O00O0oOO00O00 + ' source 2' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( O00ooOo + O00O0oOO00O00 ) . replace ( ' ' , '%20' ) , 1006 , '' )
    if 8 - 8: iIii1I11I1II1
    OoOo ( 'tvshows' , 'Media Info 3' )
 if OooooO != 'Failed' :
  oo00O00oO000o = re . compile ( '<td><a href=".+?"><img src=".+?"><br>(.+?)</a></td>' , re . DOTALL ) . findall ( OooooO )
  for O00O0oOO00O00 in oo00O00oO000o :
   if oooo000 in O00O0oOO00O00 . lower ( ) :
    Oo0o0O00 ( ( O00O0oOO00O00 + ' source 3' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( oOIIi + O00O0oOO00O00 ) . replace ( ' ' , '%20' ) , 1031 , '' )
    if 55 - 55: OoOO
    OoOo ( 'tvshows' , 'Media Info 3' )
    if 37 - 37: IIII / i11iIiiIii / Oo
    if 97 - 97: O0oO . o0000oOoOoO0o / OOOo0
    if 83 - 83: o0000oOoOoO0o - ii11ii1ii * OoOO
    if 90 - 90: Oo * OOOo0
    if 75 - 75: ii11ii1ii - I1IiI * i11iIiiIii . OoooooooOO - Oo . o0000oOoOoO0o
    if 6 - 6: o0000oOoOoO0o * OoOO / OoooooooOO % o00O0oo * OOooOOo
def i11i11Iiii11i ( ) :
 iI1i11 = OOO00O ( 'http://www.animetoon.org/cartoon' )
 OOoOO0oo0ooO = re . compile ( '<td><a href="(.+?)">(.+)</a></td>' ) . findall ( iI1i11 )
 for O0o0O00Oo0o0 , O00O0oOO00O00 in OOoOO0oo0ooO :
  Oo0o0O00 ( O00O0oOO00O00 , O0o0O00Oo0o0 , 1002 , oOOoO0 + 'anime.png' )
  if 6 - 6: I1IiI - o0oO0 * OOooOOo + I1IiI % OOooOOo
  if 100 - 100: Ooo00oOo00o % O0oO - o0000oOoOoO0o % o0000oOoOoO0o % o0000oOoOoO0o / o0oO0
  if 83 - 83: OoOO - o0oO0 - IIII % i1IIi - oO0o0ooO0 . OOooOOo
def oOo0oO ( url ) :
 iI1i11 = OOO00O ( url )
 i1ii1II1ii = re . compile ( '<img src="(.+?)" id="series_image" width="250" height="370" alt=".+?" />' ) . findall ( iI1i11 )
 for iII111Ii in i1ii1II1ii :
  I111iIi1 = iII111Ii
 oo00O00oO000o = re . compile ( '<li><a href="(.+?)">Next</a></li>' ) . findall ( iI1i11 )
 for url in oo00O00oO000o :
  Oo0o0O00 ( 'NEXT PAGE' , url , 1002 , I111iIi1 )
 OOoOO0oo0ooO = re . compile ( '&nbsp;<a href="(.+?)">(.+?)</a>' ) . findall ( iI1i11 )
 for url , O00O0oOO00O00 in OOoOO0oo0ooO :
  Oo0o0O00 ( O00O0oOO00O00 , url , 1003 , I111iIi1 )
 xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
def ooo0O ( url , IMAGE ) :
 iI1i11 = OOO00O ( url )
 OOoOO0oo0ooO = re . compile ( '"playlist">(.+?)</span></div><div><iframe src="(.+?)"' ) . findall ( iI1i11 )
 for O00O0oOO00O00 , url in OOoOO0oo0ooO :
  print O00O0oOO00O00 + '     ' + url
  if 'easy' in url :
   iI1iIIIIIiIi1 ( url )
  elif 'playpanda' in url :
   iI1iIIIIIiIi1 ( url )
   if 19 - 19: I1IiI . OOooOOo . OoooooooOO
  xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
def iI1iIIIIIiIi1 ( url ) :
 iI1i11 = OOO00O ( url )
 OOoOO0oo0ooO = re . compile ( "url: '(.+?)'," ) . findall ( iI1i11 )
 for url in OOoOO0oo0ooO :
  iiIi1iI1iIii ( 'STREAM' , url , 222 , oOOoO0 + 'anime.png' )
  if 13 - 13: OoOO0ooOOoo0O . Oo / OoOoOO00
  if 43 - 43: iIii1I11I1II1 % Ooo00oOo00o
def oOO0ooi1iiIIiII1 ( url ) :
 iiiIii = urllib2 . Request ( url )
 iiiIii . add_header ( 'User-Agent' , "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0" )
 iiiIii . add_header ( 'referer' , url )
 iii1IIiI = urllib2 . urlopen ( iiiIii )
 Ooo0oOooo0 = iii1IIiI . read ( )
 iii1IIiI . close ( )
 return Ooo0oOooo0
 if 72 - 72: IIII % OOooOOo
def OoOOoooOO0O ( url ) :
 iiiIii = urllib2 . Request ( url )
 iiiIii . add_header ( 'User-Agent' , "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0" )
 iii1IIiI = urllib2 . urlopen ( iiiIii )
 Ooo0oOooo0 = iii1IIiI . read ( )
 iii1IIiI . close ( )
 return Ooo0oOooo0
 if 93 - 93: iIii1I11I1II1 + i11iIiiIii . OOooOOo . i1IIi % OOOo0 % o0oO0
def oO0oo ( url ) :
 xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
 ooO0oO00O0o = ( '%s%s' % ( ooOO00oOOo000 , url ) )
 Ooo0oOooo0 = OoOOoooOO0O ( url )
 OOoOO0oo0ooO = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( Ooo0oOooo0 )
 for url , ooo00Ooo , O00O0oOO00O00 in OOoOO0oo0ooO :
  iiIi1iI1iIii ( '%s' % ( O00O0oOO00O00 ) . replace ( 'GenieTv' , '[COLOR green]GenieTV[/COLOR]' ) . replace ( '.' , ' ' ) . replace ( 'mp4' , '' ) . replace ( 'mkv' , '' ) . replace ( '_' , ' ' ) , '%s' % ( url ) , 222 , ooo00Ooo )
  if 52 - 52: IIII % o0oO0
def I1i1I ( url ) :
 IiI1 = xbmc . Player ( O0oOIiIII ( ) )
 import urlresolver
 try : IiI1 . play ( url )
 except : pass
 from urlresolver import common
 i1111 = xbmcgui . DialogProgress ( )
 i1111 . create ( 'LOADING' , 'Opening %s Now' % ( O00O0oOO00O00 ) )
 IiI1 = xbmc . Player ( O0oOIiIII ( ) )
 url = urlresolver . HostedMediaFile ( url ) . resolve ( )
 if i1111 . iscanceled ( ) :
  print "[COLORred]STREAM CANCELLED[/COLOR]"
  ii11iIi1I = xbmcgui . Dialog ( )
  if ii11iIi1I . yesno ( "[B]CANCELLED[/B]" , '[B]Was There A Problem[/B]' , '' , "" , 'Yes' , 'No' ) :
   ii11iIi1I . ok ( "Message Send" , "Your Message Has Been Sent" )
  else :
   return
 else :
  try : IiI1 . play ( url )
  except : pass
  try : o0oOoO00o . resolve_url ( url )
  except : pass
  i1111 . close ( )
  if 25 - 25: o0000oOoOoO0o / o0000oOoOoO0o % OoooooooOO - ii11ii1ii * OoOO
def I1Iiiiiii ( url ) :
 IiI1 = xbmc . Player ( O0oOIiIII ( ) )
 import urlresolver
 try : IiI1 . play ( url )
 except : pass
 if 23 - 23: i11iIiiIii
 if 100 - 100: OoOO + O0 . OOOo0 + i1IIi - I1IiI + OOooOOo
def O0oOIiIII ( ) :
 try :
  ooOOo = getSet ( "core-player" )
  if ( ooOOo == 'DVDPLAYER' ) : i1iii1IiiiI1i1 = xbmc . PLAYER_CORE_DVDPLAYER
  elif ( ooOOo == 'MPLAYER' ) : i1iii1IiiiI1i1 = xbmc . PLAYER_CORE_MPLAYER
  elif ( ooOOo == 'PAPLAYER' ) : i1iii1IiiiI1i1 = xbmc . PLAYER_CORE_PAPLAYER
  else : i1iii1IiiiI1i1 = xbmc . PLAYER_CORE_AUTO
 except : i1iii1IiiiI1i1 = xbmc . PLAYER_CORE_AUTO
 return i1iii1IiiiI1i1
 return True
 if 37 - 37: Oo - i1IIi - IIII + o0000oOoOoO0o . iIii1I11I1II1
def Oo0o0O00 ( name , url , mode , iconimage , showcontext = True , allinfo = { } ) :
 oO0OO0O00Oo = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 Ii1111IiIi = True
 II1I1iiIII1I1 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 II1I1iiIII1I1 . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 if showcontext :
  Oo00oOO00 = [ ]
  if showcontext == 'fav' :
   Oo00oOO00 . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in ooooooO0oo :
   Oo00oOO00 . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  II1I1iiIII1I1 . addContextMenuItems ( Oo00oOO00 )
 Ii1111IiIi = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = oO0OO0O00Oo , listitem = II1I1iiIII1I1 , isFolder = True )
 return Ii1111IiIi
 if 21 - 21: OoooooooOO . OoOoOO00 - IIII * o0oO0 * IIII
def i11Ii11II1I1 ( name , url , mode , iconimage , fanart , description ) :
 if 45 - 45: O0 * O0oO + i11iIiiIii - OoOO0ooOOoo0O - iIii1I11I1II1
 oO0OO0O00Oo = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 Ii1111IiIi = True
 II1I1iiIII1I1 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 II1I1iiIII1I1 . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 II1I1iiIII1I1 . setProperty ( "Fanart_Image" , fanart )
 Ii1111IiIi = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = oO0OO0O00Oo , listitem = II1I1iiIII1I1 , isFolder = True )
 return Ii1111IiIi
 if 5 - 5: OoOO0ooOOoo0O % Oo % IIII % o0oO0
def iiIi1iI1iIii ( name , url , mode , iconimage , showcontext = True , allinfo = { } ) :
 oO0OO0O00Oo = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 Ii1111IiIi = True
 II1I1iiIII1I1 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 II1I1iiIII1I1 . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 if showcontext :
  Oo00oOO00 = [ ]
  if showcontext == 'fav' :
   Oo00oOO00 . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in ooooooO0oo :
   Oo00oOO00 . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  II1I1iiIII1I1 . addContextMenuItems ( Oo00oOO00 )
 Ii1111IiIi = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = oO0OO0O00Oo , listitem = II1I1iiIII1I1 , isFolder = False )
 return Ii1111IiIi
 if 17 - 17: o00O0oo + OoOoOO00 + OoooooooOO / OoOO0ooOOoo0O / IIII
 if 80 - 80: OOooOOo % i1IIi / o0000oOoOoO0o
 if 56 - 56: i1IIi . i11iIiiIii
 if 15 - 15: OoOoOO00 * OoOO % oO0o0ooO0 / i11iIiiIii - OoOO + Oo
 if 9 - 9: o0000oOoOoO0o - OoOO + O0 / oO0o0ooO0 % i1IIi
 if 97 - 97: OOooOOo * o0oO0
def oOOooI1 ( heading , announce ) :
 class O0OOO0ooO00o ( ) :
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
   try : II1I = open ( announce ) ; I1iii1 = II1I . read ( )
   except : I1iii1 = announce
   self . win . getControl ( self . CONTROL_TEXTBOX ) . setText ( str ( I1iii1 ) )
   return
 O0OOO0ooO00o ( )
 O0OOO0ooO00o ( )
 if 19 - 19: OoOO % OoooooooOO . OoooooooOO
def IiIiI11IIi11Iii ( ) :
 oOOooI1 ( 'These are the main Sources you should get into you XBMC' , '[COLORwhite]http://architects.x10host.com[/COLOR]--- [CR]  [COLORred]http://repo.sharktech.co.uk[/COLOR]--- [CR]   [COLORwhite]http://fusion.tvaddons.ag[/COLOR]--- [CR]  [COLORred]http://i.totalxbmc.tv[/COLOR]--- [CR]   [COLORwhite]http://www.xunitytalk.com/xfinity[/COLOR]--- [CR]  [COLORred]http://srp.nu[/COLOR]--- [CR]   [COLORwhite]http://solved.no-issue.ca[/COLOR]--- [CR]  [COLORred]http://xbmc.aminhacasadigital.com[/COLOR]--- [CR]   [COLORwhite]http://xbmc.movieshd.co[/COLOR]--- [CR]  [COLORred]http://install.kaosbox.tv[/COLOR]--- [CR]   [COLORwhite]http://kodi-repo.com/mxr[/COLOR]--- [CR]  [COLORred]http://kodi.metalkettle.co[/COLOR]--- [CR]   [COLORwhite]http://prozone.getxbmc.com[/COLOR]--- [CR]  [COLORred]http://transform.mega-tron.tv[/COLOR]--- [CR]   [COLORwhite]http://muckys.kodimediaportal.ml[/COLOR]--- [CR]  [COLORred]http://jas0npc.pcriot.com[/COLOR]--- [CR]  [COLORwhite]Sports devil source[/COLOR]--- [CR]  [COLORred]http://iwillfolo.com/iwf[/COLOR]' )
 if 9 - 9: OoOO
 if 2 - 2: iIii1I11I1II1 * OOOo0 % i1IIi % ii11ii1ii + OoooooooOO + OOOo0
 if 16 - 16: OoOO0ooOOoo0O
 if 63 - 63: oO0o0ooO0
 if 11 - 11: oO0o0ooO0 - iIii1I11I1II1
def O0o ( ) :
 xbmc . executebuiltin ( 'UpdateLocalAddons' )
 xbmc . executebuiltin ( 'UpdateAddonRepos' )
 ii11iIi1I = xbmcgui . Dialog ( )
 ii11iIi1I . ok ( "GenieTv" , '' , '                                 REFRESH SUCCESSFUL :)' , "                          [COLOR gold]Brought To You By Kodi Support Group, GenieTv[/COLOR]" )
 return
 if 92 - 92: Ooo00oOo00o
 if 15 - 15: IIII / IIII + iIii1I11I1II1 % OoooooooOO
 if 12 - 12: o0oO0
 if 36 - 36: O0oO . IIII * OoooooooOO - OOooOOo
 if 60 - 60: OoOO0ooOOoo0O . oO0o0ooO0 / iIii1I11I1II1 + OoOO0ooOOoo0O * O0oO
 if 82 - 82: i11iIiiIii . iIii1I11I1II1 * OOOo0 - o0000oOoOoO0o + o00O0oo
 if 48 - 48: ii11ii1ii
 if 96 - 96: o0oO0 . OoooooooOO
 if 39 - 39: OoOO0ooOOoo0O + Ooo00oOo00o
 if 80 - 80: OoOO0ooOOoo0O % Ooo00oOo00o / I1IiI
 if 54 - 54: Oo % Ooo00oOo00o - OoOO0ooOOoo0O - o0000oOoOoO0o
 if 71 - 71: o0oO0 . i11iIiiIii
 if 56 - 56: O0 * oO0o0ooO0 + oO0o0ooO0 * iIii1I11I1II1 / o0oO0 * O0oO
 if 25 - 25: iIii1I11I1II1 . o0000oOoOoO0o * i11iIiiIii + Oo * o0000oOoOoO0o
 if 67 - 67: oO0o0ooO0
 if 88 - 88: Oo
 if 8 - 8: ii11ii1ii
 if 82 - 82: OoooooooOO
 if 75 - 75: OoOoOO00 % OOOo0 + OoOO0ooOOoo0O % OoooooooOO / IIII
 if 4 - 4: i11iIiiIii - OoOO0ooOOoo0O % ii11ii1ii * O0oO % OOooOOo
 if 71 - 71: o0oO0 . o0oO0 - iIii1I11I1II1
 if 22 - 22: OoooooooOO / ii11ii1ii % oO0o0ooO0 * I1IiI
 if 32 - 32: OoooooooOO % OoOO % iIii1I11I1II1 / O0
 if 61 - 61: OoOoOO00 . O0 - o00O0oo - ii11ii1ii / i11iIiiIii - OoOoOO00
def O0oo0oOo ( url ) :
 Ooo0oOooo0 = OOO00O ( OO0o + i111iI1i1iI ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 OOoOO0oo0ooO = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( Ooo0oOooo0 )
 for O00O0oOO00O00 , url , iiIiIIIiiI , iiI1IIIi , II11IiIi11 in OOoOO0oo0ooO :
  oOoOooOo0o0 ( O00O0oOO00O00 , url , 42 , iiIiIIIiiI , iiI1IIIi , II11IiIi11 )
 OoOo ( 'movies' , 'MAIN' )
 if 39 - 39: OoOoOO00 * I1IiI . O0 * o0000oOoOoO0o
def O0o0O0O0O ( url ) :
 Ooo0oOooo0 = OOO00O ( OO0o + o0O00O ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 OOoOO0oo0ooO = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( Ooo0oOooo0 )
 for O00O0oOO00O00 , url , iiIiIIIiiI , iiI1IIIi , II11IiIi11 in OOoOO0oo0ooO :
  oOoOooOo0o0 ( O00O0oOO00O00 , url , 42 , iiIiIIIiiI , iiI1IIIi , II11IiIi11 )
 OoOo ( 'movies' , 'MAIN' )
 if 21 - 21: OoooooooOO . I1IiI - iIii1I11I1II1 % IIII
def Oooo0ooOoo0 ( url ) :
 Ooo0oOooo0 = OOO00O ( OO0o + i1Iii ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 OOoOO0oo0ooO = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( Ooo0oOooo0 )
 for O00O0oOO00O00 , url , iiIiIIIiiI , iiI1IIIi , II11IiIi11 in OOoOO0oo0ooO :
  oOoOooOo0o0 ( O00O0oOO00O00 , url , 42 , iiIiIIIiiI , iiI1IIIi , II11IiIi11 )
 OoOo ( 'movies' , 'MAIN' )
 if 57 - 57: IIII
def IiI11I1Ii11II ( url ) :
 Ooo0oOooo0 = OOO00O ( OO0o + oo0ooOoOOoO ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 OOoOO0oo0ooO = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( Ooo0oOooo0 )
 for O00O0oOO00O00 , url , iiIiIIIiiI , iiI1IIIi , II11IiIi11 in OOoOO0oo0ooO :
  oOoOooOo0o0 ( O00O0oOO00O00 , url , 42 , iiIiIIIiiI , iiI1IIIi , II11IiIi11 )
 OoOo ( 'movies' , 'MAIN' )
 if 65 - 65: O0 + O0oO % o00O0oo * OOOo0 / o0oO0 / I1IiI
def oooOO ( url ) :
 Ooo0oOooo0 = OOO00O ( OO0o + iI1IIIi11 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 OOoOO0oo0ooO = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( Ooo0oOooo0 )
 for O00O0oOO00O00 , url , iiIiIIIiiI , iiI1IIIi , II11IiIi11 in OOoOO0oo0ooO :
  oOoOooOo0o0 ( O00O0oOO00O00 , url , 42 , iiIiIIIiiI , iiI1IIIi , II11IiIi11 )
 OoOo ( 'movies' , 'MAIN' )
 if 69 - 69: O0 - O0
def i1I1i1i1I1 ( url ) :
 Ooo0oOooo0 = OOO00O ( OO0o + iI1i1I1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 OOoOO0oo0ooO = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( Ooo0oOooo0 )
 for O00O0oOO00O00 , url , iiIiIIIiiI , iiI1IIIi , II11IiIi11 in OOoOO0oo0ooO :
  oOoOooOo0o0 ( O00O0oOO00O00 , url , 42 , iiIiIIIiiI , iiI1IIIi , II11IiIi11 )
 OoOo ( 'movies' , 'MAIN' )
 if 39 - 39: o00O0oo
def oOo0000ooO ( url ) :
 Ooo0oOooo0 = OOO00O ( OO0o + I1Io0oO0oo ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 OOoOO0oo0ooO = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( Ooo0oOooo0 )
 for O00O0oOO00O00 , url , iiIiIIIiiI , iiI1IIIi , II11IiIi11 in OOoOO0oo0ooO :
  oOoOooOo0o0 ( O00O0oOO00O00 , url , 42 , iiIiIIIiiI , iiI1IIIi , II11IiIi11 )
 OoOo ( 'movies' , 'MAIN' )
 if 98 - 98: OoooooooOO - OOOo0 + o0oO0
def O0I11IIIII ( url ) :
 Ooo0oOooo0 = OOO00O ( OO0o + OoO ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 OOoOO0oo0ooO = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( Ooo0oOooo0 )
 for O00O0oOO00O00 , url , iiIiIIIiiI , iiI1IIIi , II11IiIi11 in OOoOO0oo0ooO :
  oOoOooOo0o0 ( O00O0oOO00O00 , url , 42 , iiIiIIIiiI , iiI1IIIi , II11IiIi11 )
 OoOo ( 'movies' , 'MAIN' )
 if 18 - 18: Oo - OoOO0ooOOoo0O * OoOoOO00 + OoOO
def O0oOOOO00oOOo ( url ) :
 Ooo0oOooo0 = OOO00O ( OO0o + iIIi ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 OOoOO0oo0ooO = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( Ooo0oOooo0 )
 for O00O0oOO00O00 , url , iiIiIIIiiI , iiI1IIIi , II11IiIi11 in OOoOO0oo0ooO :
  oOoOooOo0o0 ( O00O0oOO00O00 , url , 42 , iiIiIIIiiI , iiI1IIIi , II11IiIi11 )
 OoOo ( 'movies' , 'MAIN' )
 if 47 - 47: o0oO0
def o00oOoo0o00 ( url ) :
 Ooo0oOooo0 = OOO00O ( OO0o + iIiiI11II11i ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 OOoOO0oo0ooO = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( Ooo0oOooo0 )
 for O00O0oOO00O00 , url , iiIiIIIiiI , iiI1IIIi , II11IiIi11 in OOoOO0oo0ooO :
  oOoOooOo0o0 ( O00O0oOO00O00 , url , 5 , iiIiIIIiiI , iiI1IIIi , II11IiIi11 )
 OoOo ( 'movies' , 'MAIN' )
 if 98 - 98: oO0o0ooO0 - oO0o0ooO0
 if 58 - 58: OoOO
 if 98 - 98: OOooOOo * Ooo00oOo00o
 if 10 - 10: OoOO - oO0o0ooO0 % OoOoOO00 - O0oO - i1IIi
 if 10 - 10: ii11ii1ii - o0000oOoOoO0o . O0oO
 if 8 - 8: iIii1I11I1II1 % OoOO + Oo
 if 24 - 24: OOooOOo / o00O0oo / o00O0oo % OoOoOO00 - OoOO * OoOO
 if 58 - 58: I1IiI
 if 60 - 60: OoOoOO00
def oO0OOoo ( ) :
 try :
  if os . path . exists ( OooO0 ) == True :
   ii11iIi1I = xbmcgui . Dialog ( )
   if ii11iIi1I . yesno ( "Delete Thumbnails" , "[COLOR gold][B]##########WARNING ANDROID ONLY##########[/B][/COLOR]" , "This feature deletes your thumbnail folder and textures13.db" , "Are you sure you want to do proceed? This Can NOT Be Undone" ) :
    for I1IIIiIiIi , OOoO0 , OO0Oooo0oOO0O in os . walk ( OooO0 ) :
     oOo00oooOO = 0
     oOo00oooOO += len ( OO0Oooo0oOO0O )
     if oOo00oooOO > 0 :
      for II1I in OO0Oooo0oOO0O :
       os . unlink ( os . path . join ( I1IIIiIiIi , II1I ) )
  IIIIi11iiiIi1 = os . path . join ( II , "Textures13.db" )
  os . unlink ( IIIIi11iiiIi1 )
  ii11iIi1I . ok ( "Restart KODI" , "Please restart KODI to rebuild thumbnail library" )
 except :
  ii11iIi1I = xbmcgui . Dialog ( )
  ii11iIi1I . ok ( i11 , "Error Deleting Thumbnails please visit Kodi Support Group, GenieTv on facebook" )
 return
 if 12 - 12: i1IIi / o0000oOoOoO0o
 if 94 - 94: o0oO0 + OOOo0
 if 56 - 56: I1IiI % OOooOOo
 if 40 - 40: OoOO0ooOOoo0O / IIII
 if 29 - 29: o00O0oo - o00O0oo / o0oO0
 if 49 - 49: o0000oOoOoO0o + OoOO % Ooo00oOo00o - Oo - O0 - OoooooooOO
 if 4 - 4: OoOoOO00 - OoOO % Oo * i11iIiiIii
 if 18 - 18: Oo % O0
 if 66 - 66: iIii1I11I1II1 % i11iIiiIii / OOOo0
def IIIIIiiI11i1 ( url ) :
 print '############################################################       DELETING STANDARD CACHE             ###############################################################'
 Iii1Iooo = os . path . join ( xbmc . translatePath ( 'special://home' ) , 'cache' )
 if os . path . exists ( Iii1Iooo ) == True :
  for I1IIIiIiIi , OOoO0 , OO0Oooo0oOO0O in os . walk ( Iii1Iooo ) :
   oOo00oooOO = 0
   oOo00oooOO += len ( OO0Oooo0oOO0O )
   if 39 - 39: OoOO / o0oO0 * OoOoOO00 * oO0o0ooO0
   if 41 - 41: i11iIiiIii * O0 - oO0o0ooO0 . OoOoOO00 % Ooo00oOo00o % ii11ii1ii
   if oOo00oooOO > 0 :
    if 32 - 32: OoOO0ooOOoo0O + oO0o0ooO0 + iIii1I11I1II1 * Oo
    ii11iIi1I = xbmcgui . Dialog ( )
    if ii11iIi1I . yesno ( "Delete KODI Cache Files" , str ( oOo00oooOO ) + " files found" , "Do you want to delete them?" ) :
     if 62 - 62: i11iIiiIii
     for II1I in OO0Oooo0oOO0O :
      try :
       os . unlink ( os . path . join ( I1IIIiIiIi , II1I ) )
      except :
       pass
     for oOO0O00Oo0O0o in OOoO0 :
      try :
       shutil . rmtree ( os . path . join ( I1IIIiIiIi , oOO0O00Oo0O0o ) )
      except :
       pass
       if 2 - 2: OOOo0
   else :
    pass
 if xbmc . getCondVisibility ( 'system.platform.ATV2' ) :
  oo0O = os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'Other' )
  if 91 - 91: IIII * o00O0oo / O0oO . OOOo0 . oO0o0ooO0 - OoOoOO00
  for I1IIIiIiIi , OOoO0 , OO0Oooo0oOO0O in os . walk ( oo0O ) :
   oOo00oooOO = 0
   oOo00oooOO += len ( OO0Oooo0oOO0O )
   if 18 - 18: I1IiI
   if oOo00oooOO > 0 :
    if 13 - 13: IIII % Ooo00oOo00o * iIii1I11I1II1 + ii11ii1ii - o0oO0 - OOOo0
    ii11iIi1I = xbmcgui . Dialog ( )
    if ii11iIi1I . yesno ( "Delete ATV2 Cache Files" , str ( oOo00oooOO ) + " files found in 'Other'" , "Do you want to delete them?" ) :
     if 74 - 74: OoOoOO00 / O0
     for II1I in OO0Oooo0oOO0O :
      os . unlink ( os . path . join ( I1IIIiIiIi , II1I ) )
     for oOO0O00Oo0O0o in OOoO0 :
      shutil . rmtree ( os . path . join ( I1IIIiIiIi , oOO0O00Oo0O0o ) )
      if 56 - 56: o0000oOoOoO0o - O0 / O0 * i1IIi . OoooooooOO % iIii1I11I1II1
   else :
    pass
  I11iIiI1i1I1iiii1Ii11 = os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'LocalAndRental' )
  if 25 - 25: i11iIiiIii / I1IiI - O0oO / Ooo00oOo00o . OOooOOo . OOooOOo
  for I1IIIiIiIi , OOoO0 , OO0Oooo0oOO0O in os . walk ( I11iIiI1i1I1iiii1Ii11 ) :
   oOo00oooOO = 0
   oOo00oooOO += len ( OO0Oooo0oOO0O )
   if 6 - 6: OoOO . o0000oOoOoO0o
   if oOo00oooOO > 0 :
    if 43 - 43: ii11ii1ii + OOooOOo
    ii11iIi1I = xbmcgui . Dialog ( )
    if ii11iIi1I . yesno ( "Delete ATV2 Cache Files" , str ( oOo00oooOO ) + " files found in 'LocalAndRental'" , "Do you want to delete them?" ) :
     if 50 - 50: OoOO % i1IIi * O0
     for II1I in OO0Oooo0oOO0O :
      os . unlink ( os . path . join ( I1IIIiIiIi , II1I ) )
     for oOO0O00Oo0O0o in OOoO0 :
      shutil . rmtree ( os . path . join ( I1IIIiIiIi , oOO0O00Oo0O0o ) )
      if 4 - 4: iIii1I11I1II1 . i1IIi
   else :
    pass
    if 63 - 63: iIii1I11I1II1 + IIII % i1IIi / OOOo0 % OoOoOO00
    if 60 - 60: OOooOOo . I1IiI % O0oO / OOOo0 / O0
    if 19 - 19: i11iIiiIii . OOOo0 + OoOoOO00 / OoOO0ooOOoo0O . ii11ii1ii * o0oO0
    if 59 - 59: iIii1I11I1II1 / ii11ii1ii % o0oO0
 Oooo = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.whatthefurk/cache' ) , '' )
 if os . path . exists ( Oooo ) == True :
  for I1IIIiIiIi , OOoO0 , OO0Oooo0oOO0O in os . walk ( Oooo ) :
   oOo00oooOO = 0
   oOo00oooOO += len ( OO0Oooo0oOO0O )
   if 74 - 74: o0oO0 % I1IiI / Oo
   if 2 - 2: IIII % IIII % O0oO
   if oOo00oooOO > 0 :
    if 60 - 60: OoOO0ooOOoo0O
    ii11iIi1I = xbmcgui . Dialog ( )
    if ii11iIi1I . yesno ( "Delete WTF Cache Files" , str ( oOo00oooOO ) + " files found" , "Do you want to delete them?" ) :
     if 73 - 73: o0oO0
     for II1I in OO0Oooo0oOO0O :
      os . unlink ( os . path . join ( I1IIIiIiIi , II1I ) )
     for oOO0O00Oo0O0o in OOoO0 :
      shutil . rmtree ( os . path . join ( I1IIIiIiIi , oOO0O00Oo0O0o ) )
      if 86 - 86: I1IiI . o0000oOoOoO0o / Oo * o0000oOoOoO0o
   else :
    pass
    if 20 - 20: o0oO0 - OoOO0ooOOoo0O * Ooo00oOo00o * OOooOOo * OoOO0ooOOoo0O / IIII
    if 40 - 40: OOOo0 * OOooOOo . OOOo0
 o00o0O0 = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.4od/cache' ) , '' )
 if os . path . exists ( o00o0O0 ) == True :
  for I1IIIiIiIi , OOoO0 , OO0Oooo0oOO0O in os . walk ( o00o0O0 ) :
   oOo00oooOO = 0
   oOo00oooOO += len ( OO0Oooo0oOO0O )
   if 47 - 47: o0oO0
   if 63 - 63: OoOoOO00 / i11iIiiIii % OoOoOO00 . ii11ii1ii
   if oOo00oooOO > 0 :
    if 6 - 6: OoOO0ooOOoo0O + i11iIiiIii
    ii11iIi1I = xbmcgui . Dialog ( )
    if ii11iIi1I . yesno ( "Delete 4oD Cache Files" , str ( oOo00oooOO ) + " files found" , "Do you want to delete them?" ) :
     if 26 - 26: IIII / o00O0oo - OoooooooOO
     for II1I in OO0Oooo0oOO0O :
      os . unlink ( os . path . join ( I1IIIiIiIi , II1I ) )
     for oOO0O00Oo0O0o in OOoO0 :
      shutil . rmtree ( os . path . join ( I1IIIiIiIi , oOO0O00Oo0O0o ) )
      if 9 - 9: OoooooooOO * ii11ii1ii
   else :
    pass
    if 9 - 9: Oo + oO0o0ooO0
    if 64 - 64: O0 * OOOo0 / OOOo0
 OO0oo = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.iplayer/iplayer_http_cache' ) , '' )
 if os . path . exists ( OO0oo ) == True :
  for I1IIIiIiIi , OOoO0 , OO0Oooo0oOO0O in os . walk ( OO0oo ) :
   oOo00oooOO = 0
   oOo00oooOO += len ( OO0Oooo0oOO0O )
   if 56 - 56: ii11ii1ii . OoOO
   if 55 - 55: Ooo00oOo00o * Ooo00oOo00o . OOOo0
   if oOo00oooOO > 0 :
    if 94 - 94: Ooo00oOo00o + Ooo00oOo00o + ii11ii1ii . Ooo00oOo00o * o00O0oo
    ii11iIi1I = xbmcgui . Dialog ( )
    if ii11iIi1I . yesno ( "Delete BBC iPlayer Cache Files" , str ( oOo00oooOO ) + " files found" , "Do you want to delete them?" ) :
     if 62 - 62: OOooOOo / iIii1I11I1II1
     for II1I in OO0Oooo0oOO0O :
      os . unlink ( os . path . join ( I1IIIiIiIi , II1I ) )
     for oOO0O00Oo0O0o in OOoO0 :
      shutil . rmtree ( os . path . join ( I1IIIiIiIi , oOO0O00Oo0O0o ) )
      if 55 - 55: o00O0oo / Ooo00oOo00o + oO0o0ooO0 . IIII
   else :
    pass
    if 47 - 47: O0
    if 83 - 83: O0 + I1IiI / O0 / o0000oOoOoO0o
    if 68 - 68: i1IIi . o0000oOoOoO0o . i1IIi + IIII % OOOo0
 IIoO = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/script.module.simple.downloader' ) , '' )
 if os . path . exists ( IIoO ) == True :
  for I1IIIiIiIi , OOoO0 , OO0Oooo0oOO0O in os . walk ( IIoO ) :
   oOo00oooOO = 0
   oOo00oooOO += len ( OO0Oooo0oOO0O )
   if 13 - 13: i1IIi
   if 48 - 48: O0 + Ooo00oOo00o . oO0o0ooO0 * OOooOOo * oO0o0ooO0
   if oOo00oooOO > 0 :
    if 69 - 69: Ooo00oOo00o - OoooooooOO - OoOO0ooOOoo0O % o0000oOoOoO0o / I1IiI - OoOoOO00
    ii11iIi1I = xbmcgui . Dialog ( )
    if ii11iIi1I . yesno ( "Delete Simple Downloader Cache Files" , str ( oOo00oooOO ) + " files found" , "Do you want to delete them?" ) :
     if 67 - 67: OoOO0ooOOoo0O + OoOO0ooOOoo0O + Ooo00oOo00o . i11iIiiIii + ii11ii1ii + i11iIiiIii
     for II1I in OO0Oooo0oOO0O :
      os . unlink ( os . path . join ( I1IIIiIiIi , II1I ) )
     for oOO0O00Oo0O0o in OOoO0 :
      shutil . rmtree ( os . path . join ( I1IIIiIiIi , oOO0O00Oo0O0o ) )
      if 31 - 31: OoOO * O0oO . I1IiI * o0000oOoOoO0o
   else :
    pass
    if 28 - 28: IIII + OOOo0 - Oo % OoOO0ooOOoo0O . o0000oOoOoO0o + OOOo0
    if 72 - 72: o00O0oo / Oo / OoOO * I1IiI + OoOO0ooOOoo0O
 OOoo0OOOo0o = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.itv/Images' ) , '' )
 if os . path . exists ( OOoo0OOOo0o ) == True :
  for I1IIIiIiIi , OOoO0 , OO0Oooo0oOO0O in os . walk ( OOoo0OOOo0o ) :
   oOo00oooOO = 0
   oOo00oooOO += len ( OO0Oooo0oOO0O )
   if 10 - 10: O0oO
   if 48 - 48: oO0o0ooO0 * i1IIi % OoooooooOO * o00O0oo * Ooo00oOo00o
   if oOo00oooOO > 0 :
    if 7 - 7: oO0o0ooO0 . o00O0oo . oO0o0ooO0 - O0oO
    ii11iIi1I = xbmcgui . Dialog ( )
    if ii11iIi1I . yesno ( "Delete ITV Cache Files" , str ( oOo00oooOO ) + " files found" , "Do you want to delete them?" ) :
     if 33 - 33: o0oO0 + OoooooooOO - Ooo00oOo00o / i1IIi / OoooooooOO
     for II1I in OO0Oooo0oOO0O :
      os . unlink ( os . path . join ( I1IIIiIiIi , II1I ) )
     for oOO0O00Oo0O0o in OOoO0 :
      shutil . rmtree ( os . path . join ( I1IIIiIiIi , oOO0O00Oo0O0o ) )
      if 82 - 82: ii11ii1ii / OoOO0ooOOoo0O - oO0o0ooO0 / Oo * Ooo00oOo00o
   else :
    pass
    if 55 - 55: OoooooooOO
    if 73 - 73: I1IiI - ii11ii1ii % Oo + ii11ii1ii - O0 . Ooo00oOo00o
 i1iIii = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.movies4me/cache' ) , '' )
 if os . path . exists ( OOoo0OOOo0o ) == True :
  for I1IIIiIiIi , OOoO0 , OO0Oooo0oOO0O in os . walk ( i1iIii ) :
   oOo00oooOO = 0
   oOo00oooOO += len ( OO0Oooo0oOO0O )
   if 95 - 95: o0000oOoOoO0o / IIII . O0 * IIII - OOooOOo * Oo
   if 6 - 6: I1IiI . OoOoOO00 * OOOo0 . OOOo0 / o00O0oo
   if oOo00oooOO > 0 :
    if 14 - 14: O0oO % IIII - O0 / O0oO
    ii11iIi1I = xbmcgui . Dialog ( )
    if ii11iIi1I . yesno ( "Delete Movies4me Cache Files" , str ( oOo00oooOO ) + " files found" , "Do you want to delete them?" ) :
     if 91 - 91: i11iIiiIii % O0oO * OoOO - ii11ii1ii . O0oO
     for II1I in OO0Oooo0oOO0O :
      os . unlink ( os . path . join ( I1IIIiIiIi , II1I ) )
     for oOO0O00Oo0O0o in OOoO0 :
      shutil . rmtree ( os . path . join ( I1IIIiIiIi , oOO0O00Oo0O0o ) )
      if 28 - 28: i11iIiiIii
   else :
    pass
    if 51 - 51: OOOo0 + o0oO0 * O0 . o00O0oo
    if 82 - 82: OoOO0ooOOoo0O * ii11ii1ii % o00O0oo . OoOO0ooOOoo0O
 iI1oOoo = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.phstreams/Cache' ) , '' )
 if os . path . exists ( OOoo0OOOo0o ) == True :
  for I1IIIiIiIi , OOoO0 , OO0Oooo0oOO0O in os . walk ( iI1oOoo ) :
   oOo00oooOO = 0
   oOo00oooOO += len ( OO0Oooo0oOO0O )
   if 59 - 59: IIII % o00O0oo
   if 57 - 57: o0000oOoOoO0o . O0 % OoooooooOO . OOOo0 . i1IIi - OoOoOO00
   if oOo00oooOO > 0 :
    if 61 - 61: O0 . OOooOOo / I1IiI
    ii11iIi1I = xbmcgui . Dialog ( )
    if ii11iIi1I . yesno ( "Delete Phoenix Cache Files" , str ( oOo00oooOO ) + " files found" , "Do you want to delete them?" ) :
     if 74 - 74: i1IIi * O0oO % o00O0oo
     for II1I in OO0Oooo0oOO0O :
      os . unlink ( os . path . join ( I1IIIiIiIi , II1I ) )
     for oOO0O00Oo0O0o in OOoO0 :
      shutil . rmtree ( os . path . join ( I1IIIiIiIi , oOO0O00Oo0O0o ) )
      if 30 - 30: OoOoOO00 - OOooOOo % O0oO . o0000oOoOoO0o
   else :
    pass
    if 63 - 63: iIii1I11I1II1 / o0oO0
    if 24 - 24: Oo / iIii1I11I1II1 % OoOO0ooOOoo0O * I1IiI - iIii1I11I1II1
 iI1ii = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.spotitube/cache' ) , '' )
 if os . path . exists ( OOoo0OOOo0o ) == True :
  for I1IIIiIiIi , OOoO0 , OO0Oooo0oOO0O in os . walk ( iI1ii ) :
   oOo00oooOO = 0
   oOo00oooOO += len ( OO0Oooo0oOO0O )
   if 61 - 61: Oo * i1IIi . OoooooooOO
   if 44 - 44: OOOo0
   if oOo00oooOO > 0 :
    if 55 - 55: OoOO . O0oO * O0oO
    ii11iIi1I = xbmcgui . Dialog ( )
    if ii11iIi1I . yesno ( "Delete YouTube Music Cache Files" , str ( oOo00oooOO ) + " files found" , "Do you want to delete them?" ) :
     if 82 - 82: OOOo0 % Ooo00oOo00o % o0000oOoOoO0o + o0000oOoOoO0o
     for II1I in OO0Oooo0oOO0O :
      os . unlink ( os . path . join ( I1IIIiIiIi , II1I ) )
     for oOO0O00Oo0O0o in OOoO0 :
      shutil . rmtree ( os . path . join ( I1IIIiIiIi , oOO0O00Oo0O0o ) )
      if 6 - 6: Oo
   else :
    pass
    if 73 - 73: O0oO * ii11ii1ii + OOooOOo - Oo . o0000oOoOoO0o
    if 93 - 93: i11iIiiIii
 OoOiII11IiIi = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.supercartoons/cache' ) , '' )
 if os . path . exists ( OOoo0OOOo0o ) == True :
  for I1IIIiIiIi , OOoO0 , OO0Oooo0oOO0O in os . walk ( OoOiII11IiIi ) :
   oOo00oooOO = 0
   oOo00oooOO += len ( OO0Oooo0oOO0O )
   if 27 - 27: Ooo00oOo00o + I1IiI
   if 97 - 97: i1IIi * O0oO . OoOoOO00
   if oOo00oooOO > 0 :
    if 62 - 62: OoooooooOO . o00O0oo
    ii11iIi1I = xbmcgui . Dialog ( )
    if ii11iIi1I . yesno ( "Delete SuperCartoons Cache Files" , str ( oOo00oooOO ) + " files found" , "Do you want to delete them?" ) :
     if 28 - 28: OoOO . OoOO . iIii1I11I1II1 . OoOO0ooOOoo0O . ii11ii1ii * i11iIiiIii
     for II1I in OO0Oooo0oOO0O :
      os . unlink ( os . path . join ( I1IIIiIiIi , II1I ) )
     for oOO0O00Oo0O0o in OOoO0 :
      shutil . rmtree ( os . path . join ( I1IIIiIiIi , oOO0O00Oo0O0o ) )
      if 72 - 72: o0000oOoOoO0o
   else :
    pass
    if 26 - 26: IIII % Oo
    if 72 - 72: O0 + OOooOOo + OOOo0 / Oo
 o0oo0OOOO = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.tvonline.cc/cache' ) , '' )
 if os . path . exists ( OOoo0OOOo0o ) == True :
  for I1IIIiIiIi , OOoO0 , OO0Oooo0oOO0O in os . walk ( o0oo0OOOO ) :
   oOo00oooOO = 0
   oOo00oooOO += len ( OO0Oooo0oOO0O )
   if 98 - 98: i11iIiiIii . O0oO * OoOO . oO0o0ooO0
   if 52 - 52: ii11ii1ii - i1IIi + i11iIiiIii % Oo % o0oO0
   if oOo00oooOO > 0 :
    if 8 - 8: O0oO
    ii11iIi1I = xbmcgui . Dialog ( )
    if ii11iIi1I . yesno ( "Delete TVonline Cache Files" , str ( oOo00oooOO ) + " files found" , "Do you want to delete them?" ) :
     if 23 - 23: OOooOOo - o0000oOoOoO0o + OOooOOo * O0
     for II1I in OO0Oooo0oOO0O :
      os . unlink ( os . path . join ( I1IIIiIiIi , II1I ) )
     for oOO0O00Oo0O0o in OOoO0 :
      shutil . rmtree ( os . path . join ( I1IIIiIiIi , oOO0O00Oo0O0o ) )
      if 48 - 48: OoOoOO00 + OoOoOO00 * i1IIi / o00O0oo
   else :
    pass
    if 37 - 37: iIii1I11I1II1 % o0000oOoOoO0o / IIII
    if 37 - 37: O0oO - OoOO - Ooo00oOo00o
 IiI1IIiiiii = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.youtube/kodion' ) , '' )
 if os . path . exists ( OOoo0OOOo0o ) == True :
  for I1IIIiIiIi , OOoO0 , OO0Oooo0oOO0O in os . walk ( IiI1IIiiiii ) :
   oOo00oooOO = 0
   oOo00oooOO += len ( OO0Oooo0oOO0O )
   if 43 - 43: OoOO - IIII % i11iIiiIii * OoOoOO00 . O0oO - o0000oOoOoO0o
   if 13 - 13: Ooo00oOo00o
   if oOo00oooOO > 0 :
    if 70 - 70: IIII . O0oO * Ooo00oOo00o + o0000oOoOoO0o - IIII . IIII
    ii11iIi1I = xbmcgui . Dialog ( )
    if ii11iIi1I . yesno ( "Delete YouTube Cache Files" , str ( oOo00oooOO ) + " files found" , "Do you want to delete them?" ) :
     if 60 - 60: i11iIiiIii * Oo % Ooo00oOo00o + Ooo00oOo00o
     for II1I in OO0Oooo0oOO0O :
      os . unlink ( os . path . join ( I1IIIiIiIi , II1I ) )
     for oOO0O00Oo0O0o in OOoO0 :
      shutil . rmtree ( os . path . join ( I1IIIiIiIi , oOO0O00Oo0O0o ) )
      if 84 - 84: iIii1I11I1II1 + OoooooooOO
   else :
    pass
    if 77 - 77: O0 * ii11ii1ii * OoOO + Ooo00oOo00o + ii11ii1ii - O0oO
    if 10 - 10: ii11ii1ii + IIII
    if 58 - 58: OOOo0 + OoooooooOO / oO0o0ooO0 . o0oO0 % OOooOOo / ii11ii1ii
 oooO0I11Iii11i11I1 = xbmc . translatePath ( 'special://masterprofile/addon_data/plugin.video.genesis' )
 ii11iIi1I = xbmcgui . Dialog ( )
 try :
  if ii11iIi1I . yesno ( "Delete Genesis Cache Files" , "Do you want to delete cache" ) :
   IiOO0oo00OOo = os . path . join ( oooO0I11Iii11i11I1 , "cache.db" )
   os . unlink ( IiOO0oo00OOo )
   if 87 - 87: iIii1I11I1II1 % O0 + o0000oOoOoO0o % OOooOOo / OoOO / OOooOOo
 except :
  pass
  if 78 - 78: O0oO / O0oO + OOOo0 % OoOO0ooOOoo0O * IIII
 ii11iIi1I = xbmcgui . Dialog ( )
 ii11iIi1I . ok ( "GenieTv" , "                               Finished Deleting Cache " , "                          [COLOR gold]Brought To You By GenieTv[/COLOR]" )
 if 4 - 4: iIii1I11I1II1 . O0oO + OoOoOO00 % OoooooooOO
 if 82 - 82: OoooooooOO / o0oO0 * o0000oOoOoO0o * O0 . ii11ii1ii
 if 21 - 21: OoOoOO00 + Oo
 if 59 - 59: OoOO0ooOOoo0O + OOOo0 / OoOoOO00 / I1IiI
 if 80 - 80: I1IiI + iIii1I11I1II1 . IIII
 if 76 - 76: OOOo0 * OoOO0ooOOoo0O
 if 12 - 12: iIii1I11I1II1 / o0000oOoOoO0o % o00O0oo
 if 49 - 49: Ooo00oOo00o + OoOoOO00 / IIII - O0 % o00O0oo
 if 27 - 27: Ooo00oOo00o + Oo
def oO0oOOooO0 ( url ) :
 print '###' + i11 + ' - DELETING PACKAGES###'
 oo00o000O = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' , '' ) )
 try :
  for I1IIIiIiIi , OOoO0 , OO0Oooo0oOO0O in os . walk ( oo00o000O ) :
   oOo00oooOO = 0
   oOo00oooOO += len ( OO0Oooo0oOO0O )
   if 66 - 66: OoooooooOO + OOooOOo . i1IIi * oO0o0ooO0
   if 92 - 92: o0000oOoOoO0o / O0oO
   if oOo00oooOO > 0 :
    if 4 - 4: O0oO
    ii11iIi1I = xbmcgui . Dialog ( )
    if ii11iIi1I . yesno ( "Delete Package Cache Files" , str ( oOo00oooOO ) + " files found" , "Do you want to delete them?" ) :
     if 11 - 11: OoooooooOO + i1IIi / o00O0oo
     for II1I in OO0Oooo0oOO0O :
      os . unlink ( os . path . join ( I1IIIiIiIi , II1I ) )
     for oOO0O00Oo0O0o in OOoO0 :
      shutil . rmtree ( os . path . join ( I1IIIiIiIi , oOO0O00Oo0O0o ) )
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
 if 25 - 25: o00O0oo . OoOO0ooOOoo0O
 if 14 - 14: O0 / o0000oOoOoO0o . Ooo00oOo00o % oO0o0ooO0 . OoOO
 if 16 - 16: OoooooooOO % OOOo0 - OOooOOo / OoOoOO00 . i1IIi
 if 27 - 27: OoOoOO00 + o0oO0 . I1IiI - O0oO
 if 54 - 54: I1IiI . Oo
 if 38 - 38: i1IIi . Oo * Oo / ii11ii1ii
 if 65 - 65: o0oO0 % O0
 if 17 - 17: i1IIi + OoOO . o0000oOoOoO0o + i1IIi - OoOoOO00 % OOOo0
 if 34 - 34: OOOo0
def o0OoOo0O00 ( url ) :
 print '###' + i11 + ' - DELETING PACKAGES###'
 oo00o000O = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' , '' ) )
 try :
  for I1IIIiIiIi , OOoO0 , OO0Oooo0oOO0O in os . walk ( oo00o000O ) :
   oOo00oooOO = 0
   oOo00oooOO += len ( OO0Oooo0oOO0O )
   if 9 - 9: OoOO0ooOOoo0O
   if 38 - 38: o0000oOoOoO0o . Ooo00oOo00o . i11iIiiIii * OoooooooOO + oO0o0ooO0
   if oOo00oooOO > 0 :
    if 49 - 49: Oo - Ooo00oOo00o / O0oO / OOooOOo % OoOO
    ii11iIi1I = xbmcgui . Dialog ( )
    if ii11iIi1I . yesno ( "Delete Package Cache Files" , str ( oOo00oooOO ) + " files found" , "Do you want to delete them?" ) :
     if 38 - 38: OOooOOo . OoOO / OOooOOo % OoOoOO00
     for II1I in OO0Oooo0oOO0O :
      os . unlink ( os . path . join ( I1IIIiIiIi , II1I ) )
     for oOO0O00Oo0O0o in OOoO0 :
      shutil . rmtree ( os . path . join ( I1IIIiIiIi , oOO0O00Oo0O0o ) )
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
 IIIIIiiI11i1 ( url )
 if 47 - 47: o0000oOoOoO0o * iIii1I11I1II1 * oO0o0ooO0 - Ooo00oOo00o . O0 . o0oO0
 if 32 - 32: OOooOOo % OOOo0
 if 7 - 7: Oo . i1IIi - OoOO
 if 93 - 93: IIII % ii11ii1ii
 if 31 - 31: OoOoOO00 + OoOO0ooOOoo0O - OoooooooOO . o0000oOoOoO0o
 if 28 - 28: o00O0oo . ii11ii1ii
 if 77 - 77: ii11ii1ii % OoOoOO00
 if 81 - 81: I1IiI % o00O0oo / O0 * iIii1I11I1II1 % IIII . OOOo0
 if 90 - 90: OOooOOo
def IIiII ( url , name ) :
 OOoOoo = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 iII11 = os . path . join ( OOoOoo , 'advancedsettings.xml' )
 ii11iIi1I = xbmcgui . Dialog ( )
 O00OO00OOOoO = os . path . join ( OOoOoo , 'advancedsettings.xml.bak' )
 if os . path . exists ( O00OO00OOOoO ) == False :
  if ii11iIi1I . yesno ( "Back Up Original" , 'Have You Backed Up Your Original?' , '' , "[B][COLOR red]     AS YOU CANNOT GO BACK !!![/B][/COLOR]" ) :
   print '###' + i11 + ' - ADVANCED XML###'
   OOoOoo = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
   iII11 = os . path . join ( OOoOoo , 'advancedsettings.xml' )
   try :
    os . remove ( iII11 )
    print '=== GenieTv - REMOVING    ' + str ( iII11 ) + '    ==='
   except :
    pass
   Ooo0oOooo0 = I11 . http_GET ( url ) . content
   O0i1II1Iiii1I11 = open ( iII11 , "w" )
   O0i1II1Iiii1I11 . write ( Ooo0oOooo0 )
   O0i1II1Iiii1I11 . close ( )
   print '=== GenieTv - WRITING NEW    ' + str ( iII11 ) + '    ==='
   ii11iIi1I = xbmcgui . Dialog ( )
   ii11iIi1I . ok ( i11 , "       Done Adding new Advanced XML" )
 else :
  print '###' + i11 + ' - ADVANCED XML###'
  OOoOoo = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
  iII11 = os . path . join ( OOoOoo , 'advancedsettings.xml' )
  try :
   os . remove ( iII11 )
   print '=== GenieTv - REMOVING    ' + str ( iII11 ) + '    ==='
  except :
   pass
  Ooo0oOooo0 = I11 . http_GET ( url ) . content
  O0i1II1Iiii1I11 = open ( iII11 , "w" )
  O0i1II1Iiii1I11 . write ( Ooo0oOooo0 )
  O0i1II1Iiii1I11 . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( iII11 ) + '    ==='
  ii11iIi1I = xbmcgui . Dialog ( )
  ii11iIi1I . ok ( i11 , "       Done Adding new Advanced XML" )
 return
 if 47 - 47: i1IIi % o0oO0 - Oo * o0000oOoOoO0o / i11iIiiIii
def Iii1Iii ( url , name ) :
 print '###' + i11 + ' - CHECK ADVANCE XML###'
 OOoOoo = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 iII11 = os . path . join ( OOoOoo , 'advancedsettings.xml' )
 try :
  O0i1II1Iiii1I11 = open ( iII11 ) . read ( )
  if 'zero' in O0i1II1Iiii1I11 :
   name = '0CACHE'
  elif 'tuxen' in O0i1II1Iiii1I11 :
   name = 'TUXENS'
  elif 'muckys' in O0i1II1Iiii1I11 :
   name = 'MUCKYS'
  elif 'p2p1' in O0i1II1Iiii1I11 :
   name = '1st P2P RECOMMENDED'
  elif 'p2p2' in O0i1II1Iiii1I11 :
   name = '2nd P2P RECOMMENDED'
  elif 'mikey' in O0i1II1Iiii1I11 :
   name = 'MIKEY1234'
 except :
  name = "NO ADVANCED"
 ii11iIi1I = xbmcgui . Dialog ( )
 ii11iIi1I . ok ( i11 , "[COLOR yellow]YOU HAVE[/COLOR] " + name + "[COLOR yellow] XML SETTINGS SETUP[/COLOR]" )
 return
 if 48 - 48: OoOO0ooOOoo0O
def I1111III111ii ( url ) :
 print '###' + i11 + ' - DELETING ADVANCE XML###'
 OOoOoo = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 iII11 = os . path . join ( OOoOoo , 'advancedsettings.xml' )
 try :
  os . remove ( iII11 )
  ii11iIi1I = xbmcgui . Dialog ( )
  print '=== GenieTv - DELETING    ' + str ( iII11 ) + '    ==='
  ii11iIi1I . ok ( i11 , "       Remove Advanced Settings Sucessfull" )
 except :
  ii11iIi1I = xbmcgui . Dialog ( )
  ii11iIi1I . ok ( i11 , "       No Advanced Settings To Remove" )
 return
 if 90 - 90: o0000oOoOoO0o
 if 88 - 88: Ooo00oOo00o
 if 85 - 85: OoOO
 if 7 - 7: OOooOOo
 if 99 - 99: i11iIiiIii - oO0o0ooO0
 if 85 - 85: O0oO % ii11ii1ii
 if 95 - 95: Ooo00oOo00o * OoOO0ooOOoo0O * oO0o0ooO0 . OOooOOo
 if 73 - 73: Ooo00oOo00o
 if 28 - 28: OoooooooOO - o0000oOoOoO0o
 if 84 - 84: OoOoOO00
def i1IIii1i ( url = 'http://www.iplocation.net/' , inc = 1 ) :
 OOoOO0oo0ooO = re . compile ( "<td width='80'>(.+?)</td><td>(.+?)</td><td>(.+?)</td><td>.+?</td><td>(.+?)</td>" ) . findall ( I11 . http_GET ( url ) . content )
 for O0oOo0o0O0o , o0iii1i , IIIIIIi1IIi1I11i , O0o0oOooOoo in OOoOO0oo0ooO :
  if inc < 2 : ii11iIi1I = xbmcgui . Dialog ( ) ; ii11iIi1I . ok ( 'Check My IP' , "[B][COLOR gold]Your IP Address is: [/COLOR][/B] %s" % O0oOo0o0O0o , '[B][COLOR gold]Your IP is based in: [/COLOR][/B] %s' % IIIIIIi1IIi1I11i , '[B][COLOR gold]Your Service Provider is:[/COLOR][/B] %s' % O0o0oOooOoo )
  inc = inc + 1
  if 59 - 59: ii11ii1ii + o0000oOoOoO0o . OoOO
  if 87 - 87: Ooo00oOo00o
  if 34 - 34: O0oO . I1IiI / i11iIiiIii / oO0o0ooO0
  if 46 - 46: Oo + OoOoOO00 * OOOo0 + OoOO0ooOOoo0O
  if 31 - 31: o00O0oo * OOooOOo * o00O0oo + Ooo00oOo00o * OOooOOo . O0oO
  if 89 - 89: OoooooooOO * o00O0oo * OOOo0 . o0oO0 * o00O0oo / oO0o0ooO0
  if 46 - 46: i11iIiiIii
  if 15 - 15: O0 / i1IIi / i1IIi . oO0o0ooO0 % I1IiI + OOOo0
  if 48 - 48: O0oO % oO0o0ooO0 % o00O0oo % iIii1I11I1II1 . o00O0oo
def I11IIiI1IiI1 ( url , name ) :
 ii11iIi1I = xbmcgui . Dialog ( )
 if ii11iIi1I . yesno ( "GenieTv" , '                                    Install Latest .ini File' ) :
  print '###' + i11 + ' - CUSTOM FTV INI###'
  OOoOoo = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/script.ftvguide' , '' ) )
  iII11 = os . path . join ( OOoOoo , 'addons2.ini' )
  Ooo0oOooo0 = I11 . http_GET ( url ) . content
  O0i1II1Iiii1I11 = open ( iII11 , "w" )
  O0i1II1Iiii1I11 . write ( Ooo0oOooo0 )
  O0i1II1Iiii1I11 . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( iII11 ) + '    ==='
  ii11iIi1I = xbmcgui . Dialog ( )
  ii11iIi1I . ok ( i11 , "                               Done Adding New .ini File" )
 return
 if 37 - 37: OoOO % O0oO % OoOO
def iIII ( url , name ) :
 ii11iIi1I = xbmcgui . Dialog ( )
 if ii11iIi1I . yesno ( "GenieTv" , '                               Install Custom Settings' ) :
  print '###' + i11 + ' - CUSTOM FTV SETTINGS###'
  OOoOoo = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/script.ftvguide' , '' ) )
  iII11 = os . path . join ( OOoOoo , 'settings.xml' )
  Ooo0oOooo0 = I11 . http_GET ( url ) . content
  O0i1II1Iiii1I11 = open ( iII11 , "w" )
  O0i1II1Iiii1I11 . write ( Ooo0oOooo0 )
  O0i1II1Iiii1I11 . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( iII11 ) + '    ==='
  ii11iIi1I = xbmcgui . Dialog ( )
  ii11iIi1I . ok ( i11 , "                               Done Adding New Settings" )
 return
 if 43 - 43: oO0o0ooO0 + i11iIiiIii
 if 96 - 96: OoOO0ooOOoo0O . I1IiI * O0
def o0ooOOOO0O0o ( ) :
 try :
  I1IIIIII1 = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/script.ftvguide' , '' ) )
  if os . path . exists ( I1IIIIII1 ) == True :
   ii11iIi1I = xbmcgui . Dialog ( )
   if ii11iIi1I . yesno ( "GenieTv" , "                               Delete FTV Guide Database" ) :
    O0oO0O = os . path . join ( I1IIIIII1 , "source.db" )
    os . unlink ( O0oO0O )
  ii11iIi1I . ok ( "GenieTv" , "                                     FTV Database Reset" )
 except :
  ii11iIi1I = xbmcgui . Dialog ( )
  ii11iIi1I . ok ( i11 , "               Error Deleting Database No Database To Delete" )
 return
 if 20 - 20: I1IiI % OoOoOO00 . I1IiI . IIII + OoOO0ooOOoo0O
 if 26 - 26: oO0o0ooO0 / OoooooooOO - Oo
 if 2 - 2: ii11ii1ii - Oo
 if 4 - 4: O0 / o0000oOoOoO0o . Ooo00oOo00o - o0oO0 / OoOO0ooOOoo0O
 if 25 - 25: o0000oOoOoO0o * I1IiI - Oo . o0oO0 . OoOO
def OOO00O ( url ) :
 iiiIii = urllib2 . Request ( url )
 iiiIii . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
 iii1IIiI = urllib2 . urlopen ( iiiIii )
 Ooo0oOooo0 = iii1IIiI . read ( )
 iii1IIiI . close ( )
 return Ooo0oOooo0
 if 89 - 89: O0 * o0000oOoOoO0o * Ooo00oOo00o
 if 3 - 3: OoOO0ooOOoo0O / oO0o0ooO0 * iIii1I11I1II1 + OoOoOO00 / OOooOOo / IIII
 if 25 - 25: I1IiI + Ooo00oOo00o % o00O0oo % OoOO0ooOOoo0O / OoOO
 if 91 - 91: Ooo00oOo00o / Ooo00oOo00o . OoOoOO00 . o0oO0 - OOOo0
 if 23 - 23: OOOo0
 if 7 - 7: oO0o0ooO0 % ii11ii1ii
 if 64 - 64: O0oO + i11iIiiIii
def iI1i11i ( params ) :
 plugintools . log ( "freshstart.main_list " + repr ( params ) ) ; IIIIi1Iii1iIi = plugintools . message_yes_no ( i11 , "Do you wish to restore your" , "Kodi configuration to default settings?" )
 if IIIIi1Iii1iIi :
  ii1IIi1iI1ii1 = xbmcaddon . Addon ( id = oOOoo00O0O ) . getAddonInfo ( 'path' ) ; ii1IIi1iI1ii1 = xbmc . translatePath ( ii1IIi1iI1ii1 ) ;
  o00iIIiIi111iI = os . path . join ( ii1IIi1iI1ii1 , ".." , ".." ) ; o00iIIiIi111iI = os . path . abspath ( o00iIIiIi111iI ) ; plugintools . log ( "freshstart.main_list xbmcPath=" + o00iIIiIi111iI ) ; II1I1ii = False
  try :
   for I1IIIiIiIi , OOoO0 , OO0Oooo0oOO0O in os . walk ( o00iIIiIi111iI , topdown = True ) :
    OOoO0 [ : ] = [ oOO0O00Oo0O0o for oOO0O00Oo0O0o in OOoO0 if oOO0O00Oo0O0o not in Oo0oO0ooo ]
    for O00O0oOO00O00 in OO0Oooo0oOO0O :
     try : os . remove ( os . path . join ( I1IIIiIiIi , O00O0oOO00O00 ) )
     except :
      if O00O0oOO00O00 not in [ "Addons15.db" , "MyVideos75.db" , "Textures13.db" , "xbmc.log" ] : II1I1ii = True
      plugintools . log ( "Error removing " + I1IIIiIiIi + " " + O00O0oOO00O00 )
    for O00O0oOO00O00 in OOoO0 :
     try : os . rmdir ( os . path . join ( I1IIIiIiIi , O00O0oOO00O00 ) )
     except :
      if O00O0oOO00O00 not in [ "Database" , "userdata" ] : II1I1ii = True
      plugintools . log ( "Error removing " + I1IIIiIiIi + " " + O00O0oOO00O00 )
   if not II1I1ii : plugintools . log ( "freshstart.main_list All user files removed, you now have a clean install" ) ; plugintools . message ( i11 , "The process is complete, you're now back to a fresh Kodi configuration with GenieTv!" , "Please reboot your system or restart Kodi in order for the changes to be applied." )
   else : plugintools . log ( "freshstart.main_list User files partially removed" ) ; plugintools . message ( i11 , "The process is complete, you're now back to a fresh Kodi configuration with GenieTv" , "Please reboot your system or restart Kodi in order for the changes to be applied." )
  except : plugintools . message ( i11 , "Problem found" , "Your settings has not been changed" ) ; import traceback ; plugintools . log ( traceback . format_exc ( ) ) ; plugintools . log ( "freshstart.main_list NOT removed" )
  plugintools . add_item ( action = "" , title = "Now Exit Kodi" , folder = False )
 else : plugintools . message ( i11 , "Your settings" , "has not been changed" ) ; plugintools . add_item ( action = "" , title = "Done" , folder = False )
 IiIi ( )
 if 54 - 54: OoooooooOO + Oo * OoOO0ooOOoo0O
 if 98 - 98: OoOO - OoOO . o0oO0
 if 60 - 60: OOOo0 * ii11ii1ii / O0 + o0000oOoOoO0o + IIII
def O0oO0o00oo0o ( ) :
 i111IiIi1 = [ ]
 iii1111iIi1i1 = sys . argv [ 2 ]
 if len ( iii1111iIi1i1 ) >= 2 :
  OOo00O0O = sys . argv [ 2 ]
  oooOoO = OOo00O0O . replace ( '?' , '' )
  if ( OOo00O0O [ len ( OOo00O0O ) - 1 ] == '/' ) :
   OOo00O0O = OOo00O0O [ 0 : len ( OOo00O0O ) - 2 ]
  IiiIi1IiiiI = oooOoO . split ( '&' )
  i111IiIi1 = { }
  for OOOOO in range ( len ( IiiIi1IiiiI ) ) :
   OO0oooOO = { }
   OO0oooOO = IiiIi1IiiiI [ OOOOO ] . split ( '=' )
   if ( len ( OO0oooOO ) ) == 2 :
    i111IiIi1 [ OO0oooOO [ 0 ] ] = OO0oooOO [ 1 ]
    if 30 - 30: OoOO . Ooo00oOo00o + o0000oOoOoO0o / iIii1I11I1II1 % Oo / OoOO
 return i111IiIi1
 if 3 - 3: ii11ii1ii / OoOoOO00
IIiI1Ii = base64 . decodestring ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20v' )
OoO0O00O0oo0O = base64 . decodestring ( 'L3N0b3JhZ2UvZW11bGF0ZWQvMA==' )
O0O0O0Oo = base64 . decodestring ( 'L2dlbmllLnR4dA==' )
OOOoOo0oO0OoO = base64 . decodestring ( 'LmFyY2hpdGVjdHMueDEwaG9zdC5jb20vdGVzdC93aC50eHQ=' )
oOOOoo00 = base64 . decodestring ( 'aHR0cDovL2ZpeGVzLmFyY2hpdGVjdHMueDEwaG9zdC5jb20vZml4ZXMudHh0' )
I1 = base64 . decodestring ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vYXBwcy9hcHBzLnhtbA==' )
i111iI1i1iI = base64 . decodestring ( 'L2FkZG9ucy9uZXcudHh0' )
ii11o00000O = base64 . decodestring ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vdm9kL3ZvZC5waHA=' )
o0O00O = base64 . decodestring ( 'L2FkZG9ucy9pcHR2LnR4dA==' )
i1Iii = base64 . decodestring ( 'L2FkZG9ucy92aWRlby50eHQ=' )
oo0ooOoOOoO = base64 . decodestring ( 'L2FkZG9ucy9zcG9ydHMudHh0' )
iI1IIIi11 = base64 . decodestring ( 'L2FkZG9ucy9raWRzLnR4dA==' )
iI1i1I1 = base64 . decodestring ( 'L2FkZG9ucy9tdXNpYy50eHQ=' )
I1Io0oO0oo = base64 . decodestring ( 'L2FkZG9ucy9wcm9ncmFtcy50eHQ=' )
OoO = base64 . decodestring ( 'L2FkZG9ucy94eHgudHh0' )
iIIi = base64 . decodestring ( 'L2FkZG9ucy9yZXBvLnR4dA==' )
o0OO0o0oOOO0O = base64 . decodestring ( 'L2FkZG9ucy9wYWNrcy50eHQ=' )
iIiiiII11 = base64 . decodestring ( 'L2FkZG9ucy9za2lucy50eHQ=' )
OOOooo = base64 . decodestring ( 'L2FkZG9ucy9hcnQudHh0' )
o0ooooO0o0O = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2dvdGhhbS50eHQ=' )
I1III1111iIi = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2hlbGl4LnR4dA==' )
Ii1I = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2lzZW5nYXJkLnR4dA==' )
iIiiI11II11i = base64 . decodestring ( 'L2FkZG9ucy9SU1MudHh0' )
ooOO00oOOo000 = base64 . decodestring ( 'Q1VOVA==' )
def oOoOooOo0o0 ( name , url , mode , iconimage , fanart , description , showcontext = True , allinfo = { } ) :
 oO0OO0O00Oo = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 Ii1111IiIi = True
 II1I1iiIII1I1 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 II1I1iiIII1I1 . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 II1I1iiIII1I1 . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  Oo00oOO00 = [ ]
  if showcontext == 'fav' :
   Oo00oOO00 . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in ooooooO0oo :
   Oo00oOO00 . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fanart=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , urllib . quote_plus ( fanart ) , mode ) ) )
  II1I1iiIII1I1 . addContextMenuItems ( Oo00oOO00 )
 Ii1111IiIi = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = oO0OO0O00Oo , listitem = II1I1iiIII1I1 , isFolder = True )
 return Ii1111IiIi
 if 98 - 98: ii11ii1ii
def Iii111II ( name , url , mode , iconimage , fanart , description ) :
 oO0OO0O00Oo = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 Ii1111IiIi = True
 II1I1iiIII1I1 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 II1I1iiIII1I1 . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 II1I1iiIII1I1 . setProperty ( "Fanart_Image" , fanart )
 Ii1111IiIi = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = oO0OO0O00Oo , listitem = II1I1iiIII1I1 , isFolder = False )
 return Ii1111IiIi
 if 25 - 25: OoOO0ooOOoo0O % OoOO0ooOOoo0O
 if 25 - 25: i11iIiiIii + ii11ii1ii - OoooooooOO . O0 % O0oO
OOo00O0O = O0oO0o00oo0o ( )
O0o0O00Oo0o0 = None
O00O0oOO00O00 = None
ii1iIi1II = None
iiIiIIIiiI = None
iiI1IIIi = None
II11IiIi11 = None
oOOO = None
if 54 - 54: OoOO / iIii1I11I1II1 / OoooooooOO . i1IIi - I1IiI
if 57 - 57: iIii1I11I1II1 * o00O0oo * oO0o0ooO0 / OoOO
try :
 oOOO = int ( OOo00O0O [ "fav_mode" ] )
except :
 pass
 if 46 - 46: o00O0oo
try :
 O0o0O00Oo0o0 = urllib . unquote_plus ( OOo00O0O [ "url" ] )
except :
 pass
try :
 O00O0oOO00O00 = urllib . unquote_plus ( OOo00O0O [ "name" ] )
except :
 pass
try :
 iiIiIIIiiI = urllib . unquote_plus ( OOo00O0O [ "iconimage" ] )
except :
 pass
try :
 ii1iIi1II = int ( OOo00O0O [ "mode" ] )
except :
 pass
try :
 iiI1IIIi = urllib . unquote_plus ( OOo00O0O [ "fanart" ] )
except :
 pass
try :
 II11IiIi11 = urllib . unquote_plus ( OOo00O0O [ "description" ] )
except :
 pass
 if 61 - 61: OOooOOo / o0oO0 - OoOoOO00
 if 87 - 87: ii11ii1ii / OOOo0
print str ( II11iiii1Ii ) + ': ' + str ( iiI1IiI )
print "Mode: " + str ( ii1iIi1II )
print "URL: " + str ( O0o0O00Oo0o0 )
print "Name: " + str ( O00O0oOO00O00 )
print "IconImage: " + str ( iiIiIIIiiI )
if 45 - 45: I1IiI * o0oO0 / OoooooooOO + Ooo00oOo00o . O0oO / Ooo00oOo00o
if 64 - 64: o00O0oo / i1IIi % OOOo0 - OOooOOo
def OoOo ( content , viewType ) :
 if 11 - 11: ii11ii1ii - OoooooooOO
 if content :
  xbmcplugin . setContent ( int ( sys . argv [ 1 ] ) , content )
 if o0oOoO00o . getSetting ( 'auto-view' ) == 'true' :
  xbmc . executebuiltin ( "Container.SetViewMode(%s)" % o0oOoO00o . getSetting ( viewType ) )
  if 16 - 16: IIII % OoooooooOO - o0oO0 * o00O0oo - o00O0oo
  if 27 - 27: IIII + iIii1I11I1II1 / Oo + Ooo00oOo00o % Oo + Ooo00oOo00o
if ii1iIi1II == None :
 I1IIIii ( )
 if 77 - 77: Oo * o0oO0 % o00O0oo
elif ii1iIi1II == 1 :
 Ii11 ( O0o0O00Oo0o0 )
 if 2 - 2: o0000oOoOoO0o / Oo / o00O0oo / ii11ii1ii / OoooooooOO
elif ii1iIi1II == 44 :
 oOOo0OOOo00O ( O0o0O00Oo0o0 )
 if 22 - 22: iIii1I11I1II1 * OOOo0 / o0000oOoOoO0o + I1IiI
elif ii1iIi1II == 2 :
 o000ooooO0o ( )
 if 98 - 98: OoOO0ooOOoo0O
elif ii1iIi1II == 3 :
 O00oO000O0O ( )
 if 69 - 69: OoOoOO00 + Oo - OoOO . Oo / iIii1I11I1II1 * iIii1I11I1II1
elif ii1iIi1II == 21 :
 ii1iii1i ( )
 if 75 - 75: Ooo00oOo00o % OoooooooOO
elif ii1iIi1II == 4 :
 OOO ( )
 if 16 - 16: O0 / i1IIi
elif ii1iIi1II == 5 :
 iiII1i11i ( O00O0oOO00O00 , O0o0O00Oo0o0 , II11IiIi11 )
 if 58 - 58: OOooOOo / i11iIiiIii / O0 % o0000oOoOoO0o % OOOo0
elif ii1iIi1II == 6 :
 oO0oOOooO0 ( O0o0O00Oo0o0 )
 if 86 - 86: IIII + I1IiI / OOOo0 + o0000oOoOoO0o % o0000oOoOoO0o / i11iIiiIii
elif ii1iIi1II == 7 :
 IIiII ( O0o0O00Oo0o0 , O00O0oOO00O00 )
 if 12 - 12: I1IiI + OOooOOo . O0oO
elif ii1iIi1II == 8 :
 Iii1Iii ( O0o0O00Oo0o0 , O00O0oOO00O00 )
 if 52 - 52: Ooo00oOo00o
elif ii1iIi1II == 9 :
 FIXREPOSADDONS ( O0o0O00Oo0o0 )
 if 4 - 4: o00O0oo % ii11ii1ii + o0000oOoOoO0o - ii11ii1ii
elif ii1iIi1II == 10 :
 O0o ( )
 if 98 - 98: o00O0oo - O0 * OoOO * o00O0oo * o00O0oo
elif ii1iIi1II == 11 :
 I1111III111ii ( O0o0O00Oo0o0 )
 if 44 - 44: IIII + o0000oOoOoO0o
elif ii1iIi1II == 12 :
 i1IIii1i ( )
 if 66 - 66: OoOO
elif ii1iIi1II == 13 :
 oO0OOoo ( )
 if 34 - 34: oO0o0ooO0 % i11iIiiIii + i11iIiiIii - oO0o0ooO0
elif ii1iIi1II == 14 :
 IIIIIiiI11i1 ( O0o0O00Oo0o0 )
 if 2 - 2: OoOoOO00 + i1IIi
elif ii1iIi1II == 15 :
 o0000oO ( )
 if 68 - 68: OoOO0ooOOoo0O + o00O0oo
elif ii1iIi1II == 16 :
 I11IIiI1IiI1 ( O0o0O00Oo0o0 , O00O0oOO00O00 )
 if 58 - 58: IIII * o00O0oo . i1IIi
elif ii1iIi1II == 17 :
 iIII ( O0o0O00Oo0o0 , O00O0oOO00O00 )
 if 19 - 19: OoOO
elif ii1iIi1II == 18 :
 o0ooOOOO0O0o ( )
 if 85 - 85: o0oO0 - OOOo0 / i1IIi / Ooo00oOo00o / OoOoOO00
elif ii1iIi1II == 19 :
 I1i1i1 ( O00O0oOO00O00 , O0o0O00Oo0o0 , II11IiIi11 )
 if 94 - 94: iIii1I11I1II1 + IIII
elif ii1iIi1II == 40 :
 i11OOoo ( O00O0oOO00O00 , O0o0O00Oo0o0 , II11IiIi11 )
 if 44 - 44: Ooo00oOo00o + o0000oOoOoO0o % Ooo00oOo00o + i1IIi + oO0o0ooO0 + O0
elif ii1iIi1II == 42 :
 oOoOO ( O00O0oOO00O00 , O0o0O00Oo0o0 , II11IiIi11 )
 if 18 - 18: iIii1I11I1II1 % iIii1I11I1II1 % OoOO + OOOo0 % o0oO0 / o00O0oo
elif ii1iIi1II == 43 :
 OOooo ( O00O0oOO00O00 , O0o0O00Oo0o0 , II11IiIi11 )
 if 36 - 36: I1IiI . i11iIiiIii
elif ii1iIi1II == 20 :
 ooO ( O0o0O00Oo0o0 )
 if 81 - 81: Oo * oO0o0ooO0 * Ooo00oOo00o
elif ii1iIi1II == 22 :
 O0oo0oOo ( O0o0O00Oo0o0 )
 if 85 - 85: O0 * OoOO
elif ii1iIi1II == 23 :
 O0o0O0O0O ( O0o0O00Oo0o0 )
 if 39 - 39: OoOoOO00 * OOOo0 - iIii1I11I1II1
elif ii1iIi1II == 24 :
 Oooo0ooOoo0 ( O0o0O00Oo0o0 )
 if 25 - 25: OoooooooOO . o00O0oo % oO0o0ooO0 . IIII
elif ii1iIi1II == 25 :
 IiI11I1Ii11II ( O0o0O00Oo0o0 )
 if 67 - 67: OoooooooOO + O0oO / o0oO0
elif ii1iIi1II == 26 :
 oooOO ( O0o0O00Oo0o0 )
 if 75 - 75: IIII / OoooooooOO . OOOo0 + O0oO - OoOoOO00
elif ii1iIi1II == 27 :
 i1I1i1i1I1 ( O0o0O00Oo0o0 )
 if 33 - 33: IIII / IIII . i11iIiiIii * ii11ii1ii + OOooOOo
elif ii1iIi1II == 28 :
 oOo0000ooO ( O0o0O00Oo0o0 )
 if 16 - 16: IIII
elif ii1iIi1II == 29 :
 O0I11IIIII ( O0o0O00Oo0o0 )
 if 10 - 10: I1IiI . IIII * iIii1I11I1II1 - OoOO - I1IiI / O0oO
elif ii1iIi1II == 30 :
 o0OOo0o0O0O ( O0o0O00Oo0o0 )
 if 13 - 13: OoOO + I1IiI % IIII % OoooooooOO
elif ii1iIi1II == 31 :
 O0oOOOO00oOOo ( O0o0O00Oo0o0 )
 if 22 - 22: O0oO
elif ii1iIi1II == 32 :
 ooooooo00o ( )
 if 23 - 23: O0
elif ii1iIi1II == 33 :
 IIIIiII1i ( )
 if 41 - 41: i1IIi . OoOO0ooOOoo0O / o0oO0 / OOooOOo % IIII - o00O0oo
elif ii1iIi1II == 35 :
 I1I1i ( O0o0O00Oo0o0 )
 if 14 - 14: ii11ii1ii - i11iIiiIii * O0oO
elif ii1iIi1II == 34 :
 o0O ( O0o0O00Oo0o0 )
 if 39 - 39: OoooooooOO
elif ii1iIi1II == 36 :
 O0oOo00o ( O0o0O00Oo0o0 )
 if 19 - 19: i11iIiiIii
elif ii1iIi1II == 37 :
 IiI1iiiIii ( O0o0O00Oo0o0 )
 if 80 - 80: OOOo0
elif ii1iIi1II == 38 :
 iI11 ( O0o0O00Oo0o0 )
 if 58 - 58: OoOO + ii11ii1ii % I1IiI
elif ii1iIi1II == 41 :
 iI1i11i ( OOo00O0O )
 if 22 - 22: iIii1I11I1II1 - o00O0oo / OOOo0 * IIII
elif ii1iIi1II == 39 :
 o00oOoo0o00 ( O0o0O00Oo0o0 )
 if 26 - 26: OOooOOo + OoOO0ooOOoo0O - OOooOOo + Oo . OoOO
elif ii1iIi1II == 45 :
 TEXTS ( )
 if 97 - 97: i1IIi
elif ii1iIi1II == 46 :
 IiIiI11IIi11Iii ( )
 if 46 - 46: ii11ii1ii
elif ii1iIi1II == 47 :
 GEVID ( )
 if 30 - 30: Ooo00oOo00o / O0 * OOooOOo * O0oO + OoooooooOO * oO0o0ooO0
elif ii1iIi1II == 48 :
 ooOii ( O00O0oOO00O00 , O0o0O00Oo0o0 , II11IiIi11 )
 if 23 - 23: o0000oOoOoO0o
elif ii1iIi1II == 49 :
 o0Oo0oO0oOO00 ( )
 if 36 - 36: IIII . oO0o0ooO0 - i1IIi + O0oO
elif ii1iIi1II == 222 :
 I1i1I ( O0o0O00Oo0o0 )
 if 54 - 54: OoooooooOO . OoOO - oO0o0ooO0
elif ii1iIi1II == 333 :
 oO0oo ( O0o0O00Oo0o0 )
 if 76 - 76: O0oO
 if 61 - 61: o0oO0 / OoOoOO00 * o0oO0 * I1IiI * O0oO . i11iIiiIii
elif ii1iIi1II == 1001 :
 i11i11Iiii11i ( )
 if 26 - 26: O0oO / o0oO0 - Ooo00oOo00o . iIii1I11I1II1
elif ii1iIi1II == 1005 :
 O00Ooo0ooo0 ( )
 if 83 - 83: o0oO0 % o00O0oo / Oo - oO0o0ooO0 / O0
elif ii1iIi1II == 1007 :
 oO00o0O00o ( O0o0O00Oo0o0 )
 if 97 - 97: iIii1I11I1II1 * o0000oOoOoO0o
elif ii1iIi1II == 1010 :
 IIOOO00o0 ( O0o0O00Oo0o0 )
 if 95 - 95: Ooo00oOo00o
elif ii1iIi1II == 1011 :
 OOoO ( O0o0O00Oo0o0 )
 if 68 - 68: iIii1I11I1II1 . iIii1I11I1II1 / I1IiI - OoOoOO00 - iIii1I11I1II1
elif ii1iIi1II == 1030 :
 oooO0 ( )
 if 75 - 75: o0oO0 . OOOo0 * OoOoOO00
elif ii1iIi1II == 1031 :
 oO0oo0O0 ( O0o0O00Oo0o0 , iiIiIIIiiI )
 if 99 - 99: iIii1I11I1II1 * ii11ii1ii + IIII
elif ii1iIi1II == 1006 :
 Parse . ParseURL ( O0o0O00Oo0o0 )
 if 70 - 70: i1IIi % o0oO0 . ii11ii1ii - IIII + OoOO0ooOOoo0O
elif ii1iIi1II == 2030 :
 Parse . addonParseURL ( O0o0O00Oo0o0 )
 if 84 - 84: OoOO + OoOoOO00 * OoOoOO00 % OOooOOo / oO0o0ooO0 + o0oO0
elif ii1iIi1II == 2031 :
 Parse . apkParseURL ( O0o0O00Oo0o0 )
 if 9 - 9: oO0o0ooO0
elif ii1iIi1II == 1002 :
 oOo0oO ( O0o0O00Oo0o0 )
 if 25 - 25: OoOO0ooOOoo0O - o00O0oo . o0000oOoOoO0o
elif ii1iIi1II == 1003 :
 ooo0O ( O0o0O00Oo0o0 , iiIiIIIiiI )
 if 57 - 57: OOooOOo + Oo * ii11ii1ii - o0oO0 % iIii1I11I1II1 - o00O0oo
elif ii1iIi1II == 1004 :
 iI1iIIIIIiIi1 ( O0o0O00Oo0o0 )
 if 37 - 37: Ooo00oOo00o * o0000oOoOoO0o + o00O0oo + ii11ii1ii * OOooOOo
elif ii1iIi1II == 1008 :
 i1I111Ii ( )
 if 95 - 95: o00O0oo - i11iIiiIii % i11iIiiIii - O0 * O0oO
elif ii1iIi1II == 1009 :
 M3UPLAY ( O0o0O00Oo0o0 )
 if 81 - 81: OoOoOO00 * OOOo0 % i1IIi * i11iIiiIii + I1IiI
elif ii1iIi1II == 2001 :
 I1IIIIIi1IIiI ( O0o0O00Oo0o0 )
 if 100 - 100: i1IIi % o00O0oo
elif ii1iIi1II == 1013 :
 iIi1i1iIi1iI ( )
 if 55 - 55: OOOo0 + oO0o0ooO0
elif ii1iIi1II == 1014 :
 IiIi1I1i1II ( )
 if 85 - 85: OoOO + oO0o0ooO0 % oO0o0ooO0 / o0000oOoOoO0o . OOOo0 - I1IiI
elif ii1iIi1II == 1015 :
 iI1I1 ( O0o0O00Oo0o0 )
 if 19 - 19: o0000oOoOoO0o / oO0o0ooO0 + IIII
elif ii1iIi1II == 1016 :
 OOOOIIIIiI11Ii1i ( O0o0O00Oo0o0 )
 if 76 - 76: iIii1I11I1II1 / O0oO - ii11ii1ii % OOooOOo % OoOO0ooOOoo0O + OoooooooOO
elif ii1iIi1II == 1023 :
 OoOOoOooooOOo ( )
 if 10 - 10: Ooo00oOo00o * o0000oOoOoO0o / Oo - O0oO
elif ii1iIi1II == 1024 :
 Ii1111III1 ( )
 if 11 - 11: IIII % ii11ii1ii / o0oO0 . i11iIiiIii + OoOO0ooOOoo0O - OoOoOO00
elif ii1iIi1II == 1025 :
 oO00oooo0 ( O0o0O00Oo0o0 )
 if 50 - 50: i1IIi * OoOO / i11iIiiIii / i11iIiiIii / OoOO
elif ii1iIi1II == 4001 :
 Ii11I ( )
 if 84 - 84: ii11ii1ii - oO0o0ooO0 + ii11ii1ii
elif ii1iIi1II == 4002 :
 OOO0OOO00oo ( )
 if 63 - 63: o0000oOoOoO0o * o0oO0 % OoOoOO00 % O0oO + OOOo0 * Oo
elif ii1iIi1II == 4003 :
 OoiIIiIi1 ( )
 if 96 - 96: IIII
elif ii1iIi1II == 3000 :
 oOOOooO ( )
 if 99 - 99: iIii1I11I1II1 - o0oO0
elif ii1iIi1II == 3001 :
 o0i1iI1iiI1I ( )
 if 79 - 79: OOOo0 + OoOO % o0000oOoOoO0o % OoOO
elif ii1iIi1II == 3002 :
 oO00oo000O ( O0o0O00Oo0o0 )
 if 56 - 56: ii11ii1ii + OoOO . Ooo00oOo00o + OoooooooOO * ii11ii1ii - O0
elif ii1iIi1II == 3003 :
 ii11 ( O0o0O00Oo0o0 )
 if 35 - 35: OoOO0ooOOoo0O . o0000oOoOoO0o . O0oO - o0000oOoOoO0o % o0000oOoOoO0o + O0oO
elif ii1iIi1II == 3004 :
 iIiI ( O0o0O00Oo0o0 )
 if 99 - 99: OOooOOo + OoOO0ooOOoo0O
elif ii1iIi1II == 404 :
 OOooO00OO ( O00O0oOO00O00 , O0o0O00Oo0o0 , iiIiIIIiiI )
 if 34 - 34: O0oO * OOooOOo . OOOo0 % i11iIiiIii
elif ii1iIi1II == 7030 :
 II1iI ( )
 if 61 - 61: iIii1I11I1II1 + OoOO * o0000oOoOoO0o - i1IIi % OoOO
elif ii1iIi1II == 7021 :
 i111I11I ( O00O0oOO00O00 )
 if 76 - 76: OoOO / I1IiI
elif ii1iIi1II == 7022 :
 IiiIi ( O00O0oOO00O00 )
 if 12 - 12: O0oO
elif ii1iIi1II == 7000 :
 i1IiI1Iiii ( O00O0oOO00O00 , O0o0O00Oo0o0 , img )
 if 58 - 58: Ooo00oOo00o + iIii1I11I1II1 % O0 + o0000oOoOoO0o + I1IiI * OoooooooOO
elif ii1iIi1II == 7050 :
 O0oI1ii1Ii1 ( O0o0O00Oo0o0 )
 if 41 - 41: OoOO * OOOo0
elif ii1iIi1II == 7051 :
 OO0OOOOo0000O ( O0o0O00Oo0o0 )
 if 76 - 76: OoOO . O0 * OoooooooOO + o0oO0
elif ii1iIi1II == 7052 :
 iIII11Iiii1 ( O0o0O00Oo0o0 )
 if 53 - 53: Oo
elif ii1iIi1II == 7053 :
 o0oo0 ( O0o0O00Oo0o0 )
 if 3 - 3: IIII - OoooooooOO * OoooooooOO - OOOo0 / O0oO * ii11ii1ii
elif ii1iIi1II == 7054 :
 CoolPlay ( O0o0O00Oo0o0 )
 if 58 - 58: IIII % iIii1I11I1II1 / i11iIiiIii % OOooOOo . O0oO * oO0o0ooO0
elif ii1iIi1II == 7060 :
 O0OoO0o ( )
 if 32 - 32: OoooooooOO + OOooOOo
elif ii1iIi1II == 7061 :
 ii1I ( O0o0O00Oo0o0 )
 if 91 - 91: o0oO0 - O0oO * O0oO
elif ii1iIi1II == 7063 :
 I111IIiIII ( O0o0O00Oo0o0 )
 if 55 - 55: iIii1I11I1II1 + OOOo0 - Oo
elif ii1iIi1II == 7062 :
 II1 ( O0o0O00Oo0o0 )
 if 24 - 24: Ooo00oOo00o / O0oO + oO0o0ooO0 * o0000oOoOoO0o * oO0o0ooO0
elif ii1iIi1II == 7064 :
 NATatozcat ( )
 if 10 - 10: OOOo0 - ii11ii1ii - Oo - OOooOOo
elif ii1iIi1II == 7067 :
 i1iiIIiiiII ( O0o0O00Oo0o0 )
 if 21 - 21: OoooooooOO + O0oO
elif ii1iIi1II == 7066 :
 NATatozA ( O0o0O00Oo0o0 )
 if 43 - 43: i11iIiiIii . ii11ii1ii . OoOO
elif ii1iIi1II == 7065 :
 Ii1I1OO0ooO0 ( O0o0O00Oo0o0 )
 if 31 - 31: o00O0oo % OOooOOo % O0oO . ii11ii1ii / OOooOOo * OoOO
elif ii1iIi1II == 7070 :
 oOOO0ooOO ( )
 if 74 - 74: OOOo0 . o0oO0 / oO0o0ooO0 . IIII
elif ii1iIi1II == 7071 :
 DIZIlist ( O0o0O00Oo0o0 )
 if 74 - 74: Oo / O0oO % O0oO . IIII
elif ii1iIi1II == 7072 :
 DIZIpull ( O0o0O00Oo0o0 )
 if 72 - 72: i1IIi
elif ii1iIi1II == 7073 :
 WATCHDIZI ( O0o0O00Oo0o0 )
 if 21 - 21: O0oO . OoOO0ooOOoo0O / i11iIiiIii * i1IIi
elif ii1iIi1II == 7002 :
 ii111I11Ii ( )
 if 82 - 82: o0oO0 * Oo % i11iIiiIii * i1IIi . OoOO0ooOOoo0O
elif ii1iIi1II == 7003 :
 IiI1iiIiII ( O0o0O00Oo0o0 )
 if 89 - 89: IIII - i1IIi - IIII
elif ii1iIi1II == 7004 :
 IIIIIIi ( O0o0O00Oo0o0 )
 if 74 - 74: Ooo00oOo00o % Ooo00oOo00o
elif ii1iIi1II == 7020 :
 oO0O ( O0o0O00Oo0o0 )
 if 28 - 28: I1IiI % OoOO - OoOO0ooOOoo0O + OoOO0ooOOoo0O + OoOO / iIii1I11I1II1
elif ii1iIi1II == 7001 :
 Ooo00O0 ( )
 if 91 - 91: OOOo0 / OoOoOO00 * OoOO0ooOOoo0O
elif ii1iIi1II == 7010 :
 O0oo0 ( O0o0O00Oo0o0 )
 if 94 - 94: OoOoOO00 - iIii1I11I1II1 - iIii1I11I1II1
elif ii1iIi1II == 7011 :
 ii11Ii11 ( O0o0O00Oo0o0 )
 if 83 - 83: ii11ii1ii * iIii1I11I1II1 + I1IiI * i1IIi . OoooooooOO % o00O0oo
elif ii1iIi1II == 7012 :
 iiI1ii111 ( O0o0O00Oo0o0 )
 if 81 - 81: Ooo00oOo00o - iIii1I11I1II1
elif ii1iIi1II == 7013 :
 cnfTVPlay2 ( O0o0O00Oo0o0 )
elif ii1iIi1II == 7014 :
 CNF_Studio_Indexer . MV_Movies ( O0o0O00Oo0o0 )
elif ii1iIi1II == 7015 :
 CNF_Studio_Indexer . Movie_ByYear ( O0o0O00Oo0o0 )
elif ii1iIi1II == 7016 :
 CNF_Studio_Indexer . Resolve_CNF_Link ( O00O0oOO00O00 , O0o0O00Oo0o0 , iiIiIIIiiI )
elif ii1iIi1II == 7017 :
 CNF_Studio_Indexer . Search_Movie ( )
elif ii1iIi1II == 7018 :
 iIIi1 ( )
elif ii1iIi1II == 7019 :
 CNF_Studio_Indexer . List_Movies ( O0o0O00Oo0o0 )
elif ii1iIi1II == 7020 :
 CNF_Studio_Indexer . Get_Movie_Page ( O0o0O00Oo0o0 )
elif ii1iIi1II == 7024 :
 CNF_Studio_Indexer . Box_Office ( O0o0O00Oo0o0 )
 if 60 - 60: O0oO
elif ii1iIi1II == 8000 :
 I111iiiii1 ( )
elif ii1iIi1II == 8001 :
 oo00o0 ( )
elif ii1iIi1II == 8002 :
 oOo0 ( )
elif ii1iIi1II == 8003 :
 o00oo0OO0 ( )
elif ii1iIi1II == 8004 :
 O0Oooo ( )
elif ii1iIi1II == 8005 :
 OOOoOOo0o ( )
elif ii1iIi1II == 8006 :
 OoooooOo ( O00O0oOO00O00 , O0o0O00Oo0o0 )
elif ii1iIi1II == 8030 :
 I1i11 ( O0o0O00Oo0o0 )
elif ii1iIi1II == 8045 :
 iiIIi ( O0o0O00Oo0o0 )
elif ii1iIi1II == 8046 :
 i1i ( O0o0O00Oo0o0 )
elif ii1iIi1II == 8047 :
 iI1 ( O0o0O00Oo0o0 )
elif ii1iIi1II == 8040 :
 I11Ii111I ( )
elif ii1iIi1II == 8041 :
 Oo00OO0 ( O0o0O00Oo0o0 )
elif ii1iIi1II == 8042 :
 Oo0 ( O0o0O00Oo0o0 )
elif ii1iIi1II == 8043 :
 yt . PlayVideo ( O0o0O00Oo0o0 )
elif ii1iIi1II == 8044 :
 o0OOOOO0O ( O0o0O00Oo0o0 )
elif ii1iIi1II == 8060 :
 i11II ( )
elif ii1iIi1II == 8061 :
 o0oo00o0O0O00 ( O0o0O00Oo0o0 )
elif ii1iIi1II == 8064 :
 OOoO0oO00o ( )
elif ii1iIi1II == 8065 :
 iiiiii1 ( O0o0O00Oo0o0 )
elif ii1iIi1II == 8070 :
 o0O0oO0 ( )
elif ii1iIi1II == 8071 :
 oo0 ( O0o0O00Oo0o0 )
elif ii1iIi1II == 7080 :
 i1i1IiIi1 ( O0o0O00Oo0o0 )
elif ii1iIi1II == 8090 :
 I1IIi1I ( )
elif ii1iIi1II == 8091 :
 iIii1i1 ( O0o0O00Oo0o0 )
elif ii1iIi1II == 8092 :
 oOoO00 ( O0o0O00Oo0o0 )
elif ii1iIi1II == 8081 :
 O00O ( )
elif ii1iIi1II == 8062 :
 O0o0oo0oOO0oO ( O0o0O00Oo0o0 )
elif ii1iIi1II == 8063 :
 I1111III11 ( O0o0O00Oo0o0 )
elif ii1iIi1II == 8050 :
 OooO0oo ( )
elif ii1iIi1II == 8051 :
 o0o0oOoOO0O ( O0o0O00Oo0o0 )
elif ii1iIi1II == 8052 :
 Ooo00OoOOO ( O0o0O00Oo0o0 )
elif ii1iIi1II == 8085 :
 o00ii111Iiii ( )
elif ii1iIi1II == 8086 :
 o0o0OoOOOOOo ( O0o0O00Oo0o0 )
elif ii1iIi1II == 8087 :
 II1IIi ( O0o0O00Oo0o0 )
elif ii1iIi1II == 8088 :
 OOoOO0o ( O0o0O00Oo0o0 , O00O0oOO00O00 )
elif ii1iIi1II == 9000 :
 i1OOoO ( )
elif ii1iIi1II == 1111 :
 i1IiIiIiiI1 ( )
elif ii1iIi1II == 9001 :
 oOo00OoO0O ( )
elif ii1iIi1II == 9002 :
 Ii11i1Ii1IIII ( )
elif ii1iIi1II == 9003 :
 ooOOO0oo ( )
elif ii1iIi1II == 50 :
 OoooO ( O0o0O00Oo0o0 )
elif ii1iIi1II == 9020 :
 champlist ( )
elif ii1iIi1II == 9021 :
 II1IiiIII ( )
elif ii1iIi1II == 9022 :
 ii11iI1iIiIi ( )
elif ii1iIi1II == 9023 :
 o0OO0OoO0o0o0 ( )
elif ii1iIi1II == 9024 :
 OOooO ( O0o0O00Oo0o0 )
elif ii1iIi1II == 9030 :
 OO0OOoooo0o ( O0o0O00Oo0o0 )
elif ii1iIi1II == 9031 :
 IiIi1Ii ( O0o0O00Oo0o0 )
elif ii1iIi1II == 9032 :
 iiIIiI11II1 ( O0o0O00Oo0o0 )
elif ii1iIi1II == 9033 :
 oooOo ( O0o0O00Oo0o0 )
elif ii1iIi1II == 7085 :
 OOoo000O00O ( O0o0O00Oo0o0 )
elif ii1iIi1II == 7086 :
 ii1iIIi11 ( O0o0O00Oo0o0 )
elif ii1iIi1II == 7087 :
 I1i1II1 ( II11IiIi11 )
elif ii1iIi1II == 9666 :
 o0OoOo0O00 ( O0o0O00Oo0o0 )
elif ii1iIi1II == 10100 : o0Oo00OO0 ( )
elif ii1iIi1II == 10105 : OOoooOoO0Oo ( O0o0O00Oo0o0 )
elif ii1iIi1II == 10106 : oOO0 ( O0o0O00Oo0o0 )
elif ii1iIi1II == 10104 : ii1I111i1Ii ( O0o0O00Oo0o0 )
elif ii1iIi1II == 10107 : O00o ( )
elif ii1iIi1II == 10103 : oOIIIiI1ii1IIi ( O0o0O00Oo0o0 )
elif ii1iIi1II == 10108 : O0OOO0 ( O0o0O00Oo0o0 )
elif ii1iIi1II == 10107 : O00o ( )
elif ii1iIi1II == 10000 : Origin_Menu ( )
elif ii1iIi1II == 10001 : II1i ( )
elif ii1iIi1II == 10002 : OoiIIIiIi1I1i ( )
elif ii1iIi1II == 10003 : iI1iIIIi1i ( )
elif ii1iIi1II == 10004 : oOOoo ( )
elif ii1iIi1II == 10005 : i1iiIiI1Ii1i ( )
elif ii1iIi1II == 10006 : O0OOO0OOooo00 ( O0o0O00Oo0o0 )
elif ii1iIi1II == 10007 : OoO00 ( O0o0O00Oo0o0 , iiIiIIIiiI )
elif ii1iIi1II == 10008 : I1Iiii ( )
elif ii1iIi1II == 10009 : OooOOOO0O0 ( )
elif ii1iIi1II == 10010 : oOo0OOoooO ( O0o0O00Oo0o0 )
elif ii1iIi1II == 10011 : Ii1I1 ( O0o0O00Oo0o0 )
elif ii1iIi1II == 10012 : I1Iiiiiii ( O0o0O00Oo0o0 )
elif ii1iIi1II == 10013 : O0o0000o ( O0o0O00Oo0o0 )
elif ii1iIi1II == 10014 : II111Ii1i1 ( )
elif ii1iIi1II == 10015 : ii1iI ( )
elif ii1iIi1II == 10016 : OOOoO000 ( O0o0O00Oo0o0 )
elif ii1iIi1II == 10017 : iiI1 ( )
elif ii1iIi1II == 10018 : ooo0OO ( )
elif ii1iIi1II == 10019 : ooO000O ( )
elif ii1iIi1II == 10020 : IIi11I1 ( )
elif ii1iIi1II == 10021 : O0O00O000OOO ( )
elif ii1iIi1II == 10022 : III1IiIII1 ( O0o0O00Oo0o0 )
elif ii1iIi1II == 10023 : oOO0oo ( O00O0oOO00O00 , O0o0O00Oo0o0 )
elif ii1iIi1II == 10024 : Ii ( O0o0O00Oo0o0 )
elif ii1iIi1II == 10025 : I1II ( )
elif ii1iIi1II == 10026 : Ooo0O ( )
elif ii1iIi1II == 10027 : I11II11I1iII ( )
elif ii1iIi1II == 10028 : oOO ( )
elif ii1iIi1II == 10029 : ii1ii11 ( )
elif ii1iIi1II == 423 : iIiIIii ( O0o0O00Oo0o0 )
elif ii1iIi1II == 426 : iii1 ( O0o0O00Oo0o0 )
elif ii1iIi1II == 10030 : Izle_Films ( )
elif ii1iIi1II == 10031 : Latest_Izle_Movies ( )
elif ii1iIi1II == 10032 : Izle_Genres ( )
elif ii1iIi1II == 10033 : Izle_Pop_Movies ( )
elif ii1iIi1II == 10034 : Izle_Boxsets ( )
elif ii1iIi1II == 10035 : Izle_Search ( )
elif ii1iIi1II == 10036 : Izle_Genres_Movie ( O0o0O00Oo0o0 )
elif ii1iIi1II == 10037 : Izle_Boxset_single ( O0o0O00Oo0o0 )
elif ii1iIi1II == 10038 : Izle_IFRAME ( )
elif ii1iIi1II == 10039 : Izle_Boxsets_Next ( O0o0O00Oo0o0 )
elif ii1iIi1II == 10040 : OOooo00 ( )
elif ii1iIi1II == 10041 : iI1I11iIIi1 ( O0o0O00Oo0o0 )
elif ii1iIi1II == 10042 : i1iI1 ( O0o0O00Oo0o0 )
elif ii1iIi1II == 10043 : III11iiii11i1 ( )
elif ii1iIi1II == 10044 : o0iIiiIiiIi ( O0o0O00Oo0o0 )
elif ii1iIi1II == 10045 : ooO0oo0o0 ( O00O0oOO00O00 )
elif ii1iIi1II == 10046 : OooOoOOo0oO00 ( O0o0O00Oo0o0 )
elif ii1iIi1II == 10047 : i1iiI ( O0o0O00Oo0o0 )
elif ii1iIi1II == 10048 : iiIiIi1 ( O0o0O00Oo0o0 )
elif ii1iIi1II == 10049 : IIIiIiI ( O0o0O00Oo0o0 )
elif ii1iIi1II == 10050 : o0OOo ( )
elif ii1iIi1II == 10051 : I11IIII1111II ( )
elif ii1iIi1II == 10052 : III1iiiII1ii ( )
elif ii1iIi1II == 10053 : Addon ( O0o0O00Oo0o0 )
elif ii1iIi1II == 10054 : O0oooOO0Oo0o ( O0o0O00Oo0o0 , O00O0oOO00O00 )
elif ii1iIi1II == 10055 :
 OooOOOo0 ( "addFavorite" )
 try :
  O00O0oOO00O00 = O00O0oOO00O00 . split ( '\\ ' ) [ 1 ]
 except :
  pass
 try :
  O00O0oOO00O00 = O00O0oOO00O00 . split ( '  - ' ) [ 0 ]
 except :
  pass
 o0OIIiI1I1 ( O00O0oOO00O00 , O0o0O00Oo0o0 , iiIiIIIiiI , iiI1IIIi , oOOO )
elif ii1iIi1II == 10056 :
 OooOOOo0 ( "rmFavorite" )
 try :
  O00O0oOO00O00 = O00O0oOO00O00 . split ( '\\ ' ) [ 1 ]
 except :
  pass
 try :
  O00O0oOO00O00 = O00O0oOO00O00 . split ( '  - ' ) [ 0 ]
 except :
  pass
 i1ii11 ( O00O0oOO00O00 )
elif ii1iIi1II == 10057 :
 OooOOOo0 ( "getFavorites" )
 I11iIiI1 ( )
elif ii1iIi1II == 10058 : iIIIIi1iiIi1 ( )
elif ii1iIi1II == 10059 : Donators_Guide ( )
elif ii1iIi1II == 10060 : oOOo0 ( )
elif ii1iIi1II == 10061 : OoOOooOOO0 ( )
elif ii1iIi1II == 10062 : ooOOO00Ooo ( O00O0oOO00O00 , O0o0O00Oo0o0 , II11IiIi11 )
elif ii1iIi1II == 10063 : oooooOoo0ooo ( )
elif ii1iIi1II == 10064 : i1I11i1iI ( )
elif ii1iIi1II == 10065 : o000O0o ( O0o0O00Oo0o0 )
elif ii1iIi1II == 20000 : ooO0o ( )
elif ii1iIi1II == 20001 : ii11I1 ( )
elif ii1iIi1II == 20002 : Ii111iIi1iIi ( O0o0O00Oo0o0 )
elif ii1iIi1II == 20003 : OoOoI1iI11iIiIi1 ( O0o0O00Oo0o0 )
elif ii1iIi1II == 20004 : OO0ooo0oOO ( O0o0O00Oo0o0 )
elif ii1iIi1II == 21004 : ii1III11 ( )
elif ii1iIi1II == 21005 : WCO_SHOWS ( O0o0O00Oo0o0 )
elif ii1iIi1II == 21006 : WCO_PLAY ( O0o0O00Oo0o0 )
if 77 - 77: OOOo0 / ii11ii1ii
xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
