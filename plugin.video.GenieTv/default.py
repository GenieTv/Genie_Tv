# -*- coding: cp1252 -*-
import xbmc , xbmcaddon , xbmcgui , xbmcplugin , os , base64 , sys , xbmcvfs , unicodedata
import urlresolver
import cloudflare , googleplus , client , cleantitle
import yt
import httplib
import requests
import urlparse
import shutil
import binascii
import subprocess
import urllib2 , urllib , glob , traceback
import re
import extract
import downloader
import plugintools
import zipfile
import time
import ntpath
import cookielib
import Parse , CNF_Studio_Indexer
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
from threading import Thread
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
iiI1IiI = "2.4.7"
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
if os . path . exists ( iIi1ii1I1 ) == True :
 o0 = open ( iIi1ii1I1 ) . read ( )
else : o0 = [ ]
I11II1i = o0oOoO00o . getSetting ( 'debug' )
if os . path . exists ( ooOoOoo0O ) == False :
 os . makedirs ( ooOoOoo0O )
def IIIII ( ) :
 if o0oOoO00o . getSetting ( 'Tidy' ) == 'true' :
  ooooooO0oo ( '[COLORgreen]It Was Just Too Big[/COLOR]' , OO0o , 0000 , oOOoO0 + 'icon.png' , OOooO0OOoo , '' )
 if o0oOoO00o . getSetting ( 'My Build' ) == 'true' :
  ooooooO0oo ( '[COLORgreen]WIZARD[/COLOR]' , OO0o , 4001 , oOOoO0 + 'MB.png' , OOooO0OOoo , '' )
 if o0oOoO00o . getSetting ( 'Streams' ) == 'true' :
  ooooooO0oo ( '[COLORgreen]STREAMS[/COLOR]' , OO0o , 4002 , oOOoO0 + 'streams.png' , OOooO0OOoo , '' )
 if o0oOoO00o . getSetting ( 'Music' ) == 'true' :
  ooooooO0oo ( '[COLORgreen]Music[/COLOR]' , OO0o , 4003 , oOOoO0 + 'MUSIC.png' , OOooO0OOoo , '' )
  if 49 - 49: OOooOOo * iIii1I11I1II1 / i1IIi / i11iIiiIii / OOooOOo
 if o0oOoO00o . getSetting ( 'Builders Toolbox' ) == 'true' :
  ooooooO0oo ( '[COLORgreen]BUILDERS TOOLBOX[/COLOR]' , OO0o , 32 , oOOoO0 + 'builderstoolbox.png' , OOooO0OOoo , '' )
 if o0oOoO00o . getSetting ( 'Source List' ) == 'true' :
  ooooooO0oo ( '[COLORgreen]SOURCE LIST[/COLOR]' , OO0o , 46 , oOOoO0 + 'sources.png' , OOooO0OOoo , '' )
 if o0oOoO00o . getSetting ( 'Maintainance' ) == 'true' :
  ooooooO0oo ( '[COLORgreen]MAINTENANCE[/COLOR]' , OO0o , 3 , oOOoO0 + 'MAIN6.png' , OOooO0OOoo , '' )
 if o0oOoO00o . getSetting ( 'Addons' ) == 'true' :
  ooooooO0oo ( '[COLORgreen]ADDONS[/COLOR]' , '' , 10050 , oOOoO0 + 'ADDONS.png' , OOooO0OOoo , '' )
 if o0oOoO00o . getSetting ( 'APK Tool' ) == 'true' :
  ooooooO0oo ( '[COLORgreen]APK TOOL[/COLOR]' , OO0o , 2 , oOOoO0 + 'APK.png' , OOooO0OOoo , '' )
 if o0oOoO00o . getSetting ( 'Rss Feed' ) == 'true' :
  ooooooO0oo ( '[COLORgreen]GenieTv RSS Feed[/COLOR]' , OO0o , 39 , oOOoO0 + 'RSS.png' , OOooO0OOoo , '' )
 if o0oOoO00o . getSetting ( 'Addons Packs' ) == 'true' :
  ooooooO0oo ( '[COLORgreen]ADDONS PACKS[/COLOR]' , OO0o , 30 , oOOoO0 + 'ADDONP.png' , OOooO0OOoo , '' )
 I1i1I1II ( 'movies' , 'MAIN' )
 if 45 - 45: O0oO . I1IiI
def oOii1i1I1i ( ) :
 ooooooO0oo ( '[COLORgreen]RESTORE MY BUILD[/COLOR]' , OO0o , 49 , oOOoO0 + 'MB.png' , OOooO0OOoo , '' )
 ooooooO0oo ( '[COLORgreen]WIPE GENIE[/COLOR]' , OO0o , 41 , oOOoO0 + 'wipegenie.png' , OOooO0OOoo , '' )
 ooooooO0oo ( '[COLORgreen]WISHES PC[/COLOR]' , OO0o , 1 , oOOoO0 + 'WISHESPC.png' , OOooO0OOoo , '' )
 ooooooO0oo ( '[COLORgreen]WISHES ANDROID[/COLOR]' , OO0o , 44 , oOOoO0 + 'WISHESAN.png' , OOooO0OOoo , '' )
 I1i1I1II ( 'movies' , 'MAIN' )
def o00oOO0 ( ) :
 if i1iIIi1 == '5knuckleshuffle' :
  ooooooO0oo ( '[COLORgreen]XVID[/COLOR]' , OO0o , 10100 , oOOoO0 + 'JIZBOX.png' , OOooO0OOoo , '' )
 if o0oOoO00o . getSetting ( 'Favourites' ) == 'true' :
  ooooooO0oo ( '[COLORgreen]FAVOURITES[/COLOR]' , OO0o , 10057 , oOOoO0 + 'FAVORITES.png' , OOooO0OOoo , '' )
 if o0oOoO00o . getSetting ( 'Search' ) == 'true' :
  ooooooO0oo ( '[COLORgreen]SEARCH[/COLOR]' , OO0o , 9000 , oOOoO0 + 'search.png' , OOooO0OOoo , '' )
 if o0oOoO00o . getSetting ( 'G-tv' ) == 'true' :
  ooooooO0oo ( '[COLORgreen]G-Tv PRIVATE LIST[/COLOR]' , '' , 10058 , oOOoO0 + 'GTVIPTV.png' , OOooO0OOoo , '' )
 if o0oOoO00o . getSetting ( 'Popcorn Box' ) == 'true' :
  ooooooO0oo ( '[COLORgreen]POPCORN BOX[/COLOR]' , OO0o , 7061 , oOOoO0 + 'popcorn.png' , OOooO0OOoo , '' )
 if o0oOoO00o . getSetting ( 'Dizzy Tv' ) == 'true' :
  ooooooO0oo ( '[COLORgreen]DIZZY TV[/COLOR]' , '' , 10018 , oOOoO0 + 'dtv.png' , OOooO0OOoo , '' )
 if o0oOoO00o . getSetting ( 'Watch Series' ) == 'true' :
  ooooooO0oo ( '[COLORgreen]WATCH SERIES[/COLOR]' , '' , 10040 , oOOoO0 + 'WATCHSERIES.png' , OOooO0OOoo , '' )
 if o0oOoO00o . getSetting ( 'Recent Episodes' ) == 'true' :
  ooooooO0oo ( '[COLORgreen]RECENT EPISODES[/COLOR]' , OO0o , 8081 , oOOoO0 + 'recent.png' , OOooO0OOoo , '' )
 if o0oOoO00o . getSetting ( 'Scooby Streams' ) == 'true' :
  ooooooO0oo ( '[COLORgreen]SCOOBY STREAMS[/COLOR]' , OO0o , 1023 , oOOoO0 + 'scoob.png' , OOooO0OOoo , '' )
 if o0oOoO00o . getSetting ( 'The Reaper' ) == 'true' :
  ooooooO0oo ( '[COLORgreen]THE REAPER[/COLOR]' , ( oOo0oooo00o ( 'aHR0cDovL3RoZXJlYXBlci54MTBob3N0LmNvbS9UaGVfUmVhcGVycy9tYWluLnBocA==' ) ) , 1016 , oOOoO0 + 'reap.png' , OOooO0OOoo , '' )
 if o0oOoO00o . getSetting ( 'Pandoras Box' ) == 'true' :
  ooooooO0oo ( '[COLORgreen]PANDORAS BOX[/COLOR]' , OO0o , 10025 , oOOoO0 + 'PANDORASBOX.png' , OOooO0OOoo , '' )
 if o0oOoO00o . getSetting ( 'HeroVision' ) == 'true' :
  ooooooO0oo ( '[COLORgreen]HEROVISION[/COLOR]' , 'http://herovision.x10host.com/vod/main.php' , 1016 , oOOoO0 + 'hero.png' , OOooO0OOoo , '' )
 if o0oOoO00o . getSetting ( 'Silent Hunter' ) == 'true' :
  ooooooO0oo ( '[COLORgreen]SILENT HUNTER[/COLOR]' , ( oOo0oooo00o ( 'aHR0cDovLzUuMTM1LjIwNy45Ni8=' ) ) , 1006 , oOOoO0 + 'SILENTHUNTER.png' , OOooO0OOoo , '' )
 if o0oOoO00o . getSetting ( 'Stand Up' ) == 'true' :
  ooooooO0oo ( '[COLORgreen]STAND UP[/COLOR]' , '' , 10003 , oOOoO0 + 'ORIGINSTANDUP.png' , OOooO0OOoo , '' )
 if o0oOoO00o . getSetting ( 'Football' ) == 'true' :
  ooooooO0oo ( '[COLORgreen]FOOTBALL[/COLOR]' , '' , 10002 , oOOoO0 + 'ORIGINFOOTBALL.png' , OOooO0OOoo , '' )
 if o0oOoO00o . getSetting ( 'Fitness' ) == 'true' :
  ooooooO0oo ( '[COLORgreen]FITNESS[/COLOR]' , ( oOo0oooo00o ( 'aHR0cHM6Ly93d3cuZml0bmVzc2JsZW5kZXIuY29tL3ZpZGVvcw==' ) ) , 7085 , oOOoO0 + 'FITNESS.png' , OOooO0OOoo , '' )
 if o0oOoO00o . getSetting ( 'Documentaries' ) == 'true' :
  ooooooO0oo ( '[COLORgreen]DOCUMENTARIES[/COLOR]' , OO0o , 8040 , oOOoO0 + 'documentary.png' , OOooO0OOoo , '' )
 if o0oOoO00o . getSetting ( 'Cartoons' ) == 'true' :
  ooooooO0oo ( '[COLORgreen]CARTOONS[/COLOR]' , '' , 10001 , oOOoO0 + 'ORIGINCARTOON.png' , OOooO0OOoo , '' )
 if o0oOoO00o . getSetting ( 'Anime' ) == 'true' :
  ooooooO0oo ( '[COLORgreen]ANIME[/COLOR]' , OO0o , 1001 , oOOoO0 + 'anime.png' , OOooO0OOoo , '' )
 if o0oOoO00o . getSetting ( 'M3u Streams' ) == 'true' :
  ooooooO0oo ( '[COLORgreen]M3U STREAMS[/COLOR]' , OO0o , 8070 , oOOoO0 + 'streams.png' , OOooO0OOoo , '' )
 if o0oOoO00o . getSetting ( 'Playlist Loader' ) == 'true' :
  ooooooO0oo ( '[COLORgreen]PLAYLIST LOADER[/COLOR]' , OO0o , 3000 , oOOoO0 + 'loader.png' , OOooO0OOoo , '' )
  if 95 - 95: OoOO0ooOOoo0O / OoooooooOO
  if 18 - 18: i11iIiiIii
  if 46 - 46: i1IIi / o0000oOoOoO0o % OoOO0ooOOoo0O + O0oO
  if 79 - 79: O0oO - OOooOOo + O0oO - oO0o0ooO0
  if 8 - 8: OOOo0
  if 75 - 75: iIii1I11I1II1 / OoOO0ooOOoo0O % OOooOOo * I1IiI
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
 I1i1I1II ( 'movies' , 'MAIN' )
 if 15 - 15: ii11ii1ii + I1IiI - OoooooooOO / OoOO0ooOOoo0O
def oo000OO00Oo ( ) :
 if i1iiIII111ii == 'insert_password' :
  Oo0o0000o0o0 . ok ( '[COLORgreen]Donators Login[/COLOR]' , 'You need to set username and password to access this' , 'These are unique and provided to donators to help with server and stream costs' , 'Donate @ [COLORgreen]http://architects.x10host.com[/COLOR]' )
  o0oOoO00o . openSettings ( sys . argv [ 0 ] )
 else :
  ooooooO0oo ( '[COLORgreen]DONATORS LIST[/COLOR]' , OO0o + '/thelist.m3u' , 7080 , oOOoO0 + 'GTVIPTV.png' , OOooO0OOoo , '' )
  if 51 - 51: IIII * OOooOOo + o0000oOoOoO0o + Ooo00oOo00o
  if 66 - 66: I1IiI
def oO000Oo000 ( ) :
 ooooooO0oo ( '[COLORgreen]Cartoons[/COLOR]' , '' , 10001 , oOOoO0 + 'ORIGINCARTOON.png' , OOooO0OOoo , '' )
 ooooooO0oo ( '[COLORgreen]Dizzy TV[/COLOR]' , '' , 10018 , oOOoO0 + 'dtv.png' , OOooO0OOoo , '' )
 ooooooO0oo ( '[COLORgreen]Football[/COLOR]' , '' , 10002 , oOOoO0 + 'ORIGINFOOTBALL.png' , OOooO0OOoo , '' )
 ooooooO0oo ( '[COLORgreen]Izle Films[/COLOR]' , '' , 10030 , oOOoO0 + 'IZLEFILMS.png' , OOooO0OOoo , '' )
 ooooooO0oo ( '[COLORgreen]Stand Up[/COLOR]' , '' , 10003 , oOOoO0 + 'ORIGINSTANDUP.png' , OOooO0OOoo , '' )
 if 4 - 4: OoOO
 if 93 - 93: Ooo00oOo00o % OoOO . Ooo00oOo00o * O0oO % o00O0oo . OoOoOO00
def iI1ii1Ii ( ) :
 ooooooO0oo ( '[COLORgreen]SCOOBY STREAMS[/COLOR]' , ( oOo0oooo00o ( 'aHR0cDovL3Njb29ieXN0cmVhbS54MTBob3N0LmNvbS9zY29vYnkvdHZjYXRzLnBocA==' ) ) , 1016 , oOOoO0 + 'scoob.png' , OOooO0OOoo , '' )
 ooooooO0oo ( '[COLORgreen]SCOOBY SCRAPES[/COLOR]' , OO0o , 1024 , oOOoO0 + 'scoob.png' , OOooO0OOoo , '' )
 if 92 - 92: I1IiI
def i1OOO ( ) :
 ooooooO0oo ( '[COLORgreen]Live Tv[/COLOR]' , OO0o , 9021 , oOOoO0 + 'english.png' , OOooO0OOoo , '' )
 ooooooO0oo ( '[COLORgreen]XXX[/COLOR]' , OO0o , 9022 , oOOoO0 + 'xxx.png' , OOooO0OOoo , '' )
 ooooooO0oo ( '[COLORgreen]Hd VOD[/COLOR]' , OO0o , 9023 , oOOoO0 + 'vod(1).png' , OOooO0OOoo , '' )
 if 59 - 59: OoOoOO00 + OoooooooOO * I1IiI + i1IIi
 if 58 - 58: OoOoOO00 * OoOO0ooOOoo0O * ii11ii1ii / OoOO0ooOOoo0O
def oO0o0OOOO ( ) :
 ooooooO0oo ( '[COLORgreen]SEARCH MOVIES[/COLOR]' , OO0o , 9001 , oOOoO0 + 'MOVIESv.png' , OOooO0OOoo , '' )
 ooooooO0oo ( '[COLORgreen]SEARCH SERIES[/COLOR]' , OO0o , 9002 , oOOoO0 + 'TVSHOWSv.png' , OOooO0OOoo , '' )
 ooooooO0oo ( '[COLORgreen]SEARCH CARTOONS[/COLOR]' , '' , 10005 , oOOoO0 + 'ORIGINCARTOON' , OOooO0OOoo , '' )
 ooooooO0oo ( '[COLORgreen]SEARCH LiveTv[/COLOR]' , OO0o , 9003 , oOOoO0 + 'livetv.png' , OOooO0OOoo , '' )
 if 68 - 68: oO0o0ooO0 - O0oO - OOOo0 - ii11ii1ii + o0000oOoOoO0o
 if 10 - 10: OoooooooOO % iIii1I11I1II1
def O00o0O00 ( ) :
 ooooooO0oo ( '[COLORgreen]RADIO[/COLOR]' , OO0o , 1013 , oOOoO0 + 'radio.png' , OOooO0OOoo , '' )
 ooooooO0oo ( '[COLORgreen]MUSIC[/COLOR]' , OO0o , 1030 , oOOoO0 + 'MUSIC.png' , OOooO0OOoo , '' )
 ooooooO0oo ( '[COLORgreen]MUSIC ARCHIVE[/COLOR]' , OO0o + ( oOo0oooo00o ( 'L3ZvZC91cmxzL211c2ljLnBocA==' ) ) , 1010 , oOOoO0 + 'MUSIC.png' , OOooO0OOoo , '' )
 ooooooO0oo ( '[COLORgreen]MUSIC SEARCH[/COLOR]' , OO0o , 1111 , oOOoO0 + 'search.png' , OOooO0OOoo , '' )
 ooooooO0oo ( '[COLORgreen]AUDIO BOOKS[/COLOR]' , 'http://doremisa.com/audiobooks/' , 1006 , oOOoO0 + 'search.png' , OOooO0OOoo , '' )
 if 34 - 34: o0oO0
 I1i1I1II ( 'movies' , 'MAIN' )
 if 15 - 15: o0000oOoOoO0o * o0oO0 * Oo % i11iIiiIii % I1IiI - OoOO0ooOOoo0O
def O0ooo0O0oo0 ( ) :
 if 91 - 91: iIii1I11I1II1 + O0oO
 i1i ( 'DELETE CACHE' , 'url' , 14 , oOOoO0 + 'MAIN5.png' , OOooO0OOoo , '' )
 i1i ( 'DELETE PACKAGES' , 'url' , 6 , oOOoO0 + 'MAIN4.png' , OOooO0OOoo , '' )
 i1i ( 'FORCE REFRESH' , 'url' , 10 , oOOoO0 + 'MAIN3.png' , OOooO0OOoo , 'Force Refresh All Repos' )
 if 46 - 46: O0oO % o0000oOoOoO0o + Ooo00oOo00o . I1IiI . Ooo00oOo00o
 i1i ( 'CHECK MY IP' , 'url' , 12 , oOOoO0 + 'MAIN2.png' , OOooO0OOoo , '' )
 i1i ( 'ANDROID ONLY DELETE TEXTURE13.DB&THUBMNAIL FOLDER' , 'url' , 13 , oOOoO0 + 'MAIN1.png' , OOooO0OOoo , 'Only Works On Android On Windows It Deletes Your Thumnails Folder But Does Not Delete The Textures13.db' )
 ooooooO0oo ( '[COLORgreen]ADVANCED SETTINGS XML[/COLOR]' , OO0o , 4 , oOOoO0 + 'XML.png' , OOooO0OOoo , '' )
 ooooooO0oo ( '[COLORgreen]URL FIXES[/COLOR]' , OO0o , 20 , oOOoO0 + 'URLFIX.png' , OOooO0OOoo , '' )
 I1i1I1II ( 'movies' , 'MAIN' )
 if 96 - 96: Oo
 if 45 - 45: O0 * OOooOOo % Oo * OoooooooOO + oO0o0ooO0 . I1IiI
def Oo0ooOo0o ( ) :
 ooooooO0oo ( '[COLORgreen]REPOS[/COLOR]' , ( oOo0oooo00o ( 'aHR0cDovL21pcnJvcnMua29kaS50di9hZGRvbnMv' ) ) , 2030 , oOOoO0 + 'repos.png' , OOooO0OOoo , '' )
 ooooooO0oo ( '[COLORgreen]NEW[/COLOR]' , OO0o , 22 , oOOoO0 + 'NEW.png' , OOooO0OOoo , '' )
 ooooooO0oo ( '[COLORgreen]IPTV[/COLOR]' , OO0o , 23 , oOOoO0 + 'IPTV.png' , OOooO0OOoo , '' )
 ooooooO0oo ( '[COLORgreen]VIDEO[/COLOR]' , OO0o , 24 , oOOoO0 + 'VIDEO.png' , OOooO0OOoo , '' )
 ooooooO0oo ( '[COLORgreen]SPORTS[/COLOR]' , OO0o , 25 , oOOoO0 + 'SPORTS.png' , OOooO0OOoo , '' )
 ooooooO0oo ( '[COLORgreen]KIDS[/COLOR]' , OO0o , 26 , oOOoO0 + 'KIDS.png' , OOooO0OOoo , '' )
 ooooooO0oo ( '[COLORgreen]MUSIC[/COLOR]' , OO0o , 27 , oOOoO0 + 'MUSIC.png' , OOooO0OOoo , '' )
 ooooooO0oo ( '[COLORgreen]PROGRAMS[/COLOR]' , OO0o , 28 , oOOoO0 + 'PROGRAMS.png' , OOooO0OOoo , '' )
 ooooooO0oo ( '[COLORgreen]XXX[/COLOR]' , 'URL' , 29 , oOOoO0 + 'XXX.png' , OOooO0OOoo , '' )
 I1i1I1II ( 'movies' , 'MAIN' )
 if 22 - 22: iIii1I11I1II1 / i11iIiiIii * iIii1I11I1II1 * OoOoOO00 . OoOO0ooOOoo0O / i11iIiiIii
 if 2 - 2: OOOo0 / O0 / OOooOOo % I1IiI % o00O0oo
def o0o00OO0 ( ) :
 i1i ( 'CHECK ADVANCED XML' , OO0o , 8 , oOOoO0 + 'XML.png' , OOooO0OOoo , '' )
 i1i ( 'MUCKYS XML' , OO0o + '/wizard/muckys.xml' , 7 , oOOoO0 + 'XML.png' , OOooO0OOoo , '' )
 i1i ( '0CACHE XML' , OO0o + '/wizard/0cache.xml' , 7 , oOOoO0 + 'XML.png' , OOooO0OOoo , '' )
 i1i ( 'MIKEY1234 XML' , OO0o + '/wizard/mikey.xml' , 7 , oOOoO0 + 'XML.png' , OOooO0OOoo , '' )
 i1i ( 'TUXENS XML' , OO0o + '/wizard/tuxens.xml' , 7 , oOOoO0 + 'XML.png' , OOooO0OOoo , '' )
 i1i ( 'P2P RECOMMENDED XML1' , OO0o + '/wizard/p2p1.xml' , 7 , oOOoO0 + 'XML.png' , OOooO0OOoo , '' )
 i1i ( 'P2P RECOMMENDED XML2' , OO0o + '/wizard/p2p2.xml' , 7 , oOOoO0 + 'XML.png' , OOooO0OOoo , '' )
 i1i ( 'DELETE XML' , OO0o , 11 , oOOoO0 + 'XML.png' , OOooO0OOoo , '' )
 I1i1I1II ( 'movies' , 'MAIN' )
 if 7 - 7: OoOO0ooOOoo0O + O0oO + O0
def Ii ( ) :
 i1i ( '[COLORgreen]My Local Zip[/COLOR]' , oo0o0O00 , 48 , oOOoO0 + 'MB.png' , OOooO0OOoo , '' )
 i1i ( '[COLORgreen]My Online Zip[/COLOR]' , oO0o0o0ooO0oO , 43 , oOOoO0 + 'MB.png' , OOooO0OOoo , '' )
 if 64 - 64: o0oO0 / I1IiI - O0 - o0000oOoOoO0o
def O0oOoOOOoOO ( ) :
 i1i ( 'INSTALL FTV GUIDE AND OTHER ADDONS REQUIRED' , OO0o + '/wizard/customftv/ftvguide-addons.zip' , 5 , oOOoO0 + 'FTV4.png' , OOooO0OOoo , '' )
 i1i ( 'FTV GUIDE FIRST RUN SETTINGS' , OO0o + '/wizard/customftv/settings.xml' , 17 , oOOoO0 + 'FTV3.png' , OOooO0OOoo , '' )
 i1i ( 'FTV GUIDE ADDONS2.INI UPDATE DAILY' , 'http://ren.byethost12.com/addons2.ini' , 16 , oOOoO0 + 'FTV1.png' , OOooO0OOoo , '' )
 i1i ( 'RESET FTV DATABASE' , 'url' , 18 , oOOoO0 + 'FTV2.png' , OOooO0OOoo , '' )
 if 38 - 38: O0oO
 if 7 - 7: O0 . oO0o0ooO0 % ii11ii1ii - OOOo0 - iIii1I11I1II1
 if 36 - 36: IIII % o0oO0 % Oo - ii11ii1ii
def Ii1I ( ) :
 ooooooO0oo ( '[COLORgreen]SKINS[/COLOR]' , OO0o , 33 , oOOoO0 + 'skinp.png' , OOooO0OOoo , '' )
 ooooooO0oo ( '[COLORgreen]ARTWORK PACKS[/COLOR]' , OO0o , 34 , oOOoO0 + 'artp.png' , OOooO0OOoo , '' )
 ooooooO0oo ( '[COLORgreen]CREATE UNIVERSAL PATHS[/COLOR]' , iI111I11I1I1 , 35 , oOOoO0 + 'GUI.png' , OOooO0OOoo , '' )
 I1i1I1II ( 'movies' , 'MAIN' )
 if 77 - 77: oO0o0ooO0 % oO0o0ooO0 * OoOO - i11iIiiIii
def Oo0oO ( url ) :
 IIiIi1iI = i1IiiiI1iI ( i1iIi ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 ooOOoooooo = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( IIiIi1iI )
 for II1I , url , O0i1II1Iiii1I11 , IIIIiiIiI , o00oooO0Oo in ooOOoooooo :
  ooooooO0oo ( II1I , url , 5 , O0i1II1Iiii1I11 , IIIIiiIiI , o00oooO0Oo )
 I1i1I1II ( 'movies' , 'MAIN' )
 if 78 - 78: o00O0oo % O0oO + ii11ii1ii
def OOooOoooOoOo ( ) :
 ooooooO0oo ( '[COLORgreen]GOTHAM SKINS[/COLOR]' , OO0o , 36 , oOOoO0 + 'GSKIN.png' , OOooO0OOoo , '' )
 ooooooO0oo ( '[COLORgreen]HELIX SKINS[/COLOR]' , OO0o , 37 , oOOoO0 + 'HSKIN.png' , OOooO0OOoo , '' )
 ooooooO0oo ( '[COLORgreen]ISENGAARD SKINS[/COLOR]' , iI111I11I1I1 , 38 , oOOoO0 + 'ISKIN.png' , OOooO0OOoo , '' )
 I1i1I1II ( 'movies' , 'MAIN' )
 if 84 - 84: IIII
def OOO00O0O ( url ) :
 IIiIi1iI = i1IiiiI1iI ( OO0o + iii ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 ooOOoooooo = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( IIiIi1iI )
 for II1I , url , O0i1II1Iiii1I11 , IIIIiiIiI , o00oooO0Oo in ooOOoooooo :
  ooooooO0oo ( II1I , url , 42 , O0i1II1Iiii1I11 , IIIIiiIiI , o00oooO0Oo )
 I1i1I1II ( 'movies' , 'MAIN' )
 if 90 - 90: OOooOOo % i1IIi / Ooo00oOo00o
def IIi ( url ) :
 IIiIi1iI = i1IiiiI1iI ( OO0o + i1Iii1i1I ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 ooOOoooooo = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( IIiIi1iI )
 for II1I , url , O0i1II1Iiii1I11 , IIIIiiIiI , o00oooO0Oo in ooOOoooooo :
  ooooooO0oo ( II1I , url , 42 , O0i1II1Iiii1I11 , IIIIiiIiI , o00oooO0Oo )
 I1i1I1II ( 'movies' , 'MAIN' )
 if 91 - 91: ii11ii1ii + OOOo0 . OoOO0ooOOoo0O * ii11ii1ii + OOOo0 * Oo
def O000OOOOOo ( url ) :
 IIiIi1iI = i1IiiiI1iI ( OO0o + Iiii1i1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 ooOOoooooo = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( IIiIi1iI )
 for II1I , url , O0i1II1Iiii1I11 , IIIIiiIiI , o00oooO0Oo in ooOOoooooo :
  ooooooO0oo ( II1I , url , 42 , O0i1II1Iiii1I11 , IIIIiiIiI , o00oooO0Oo )
 I1i1I1II ( 'movies' , 'MAIN' )
 if 84 - 84: OOOo0 . iIii1I11I1II1 % OoooooooOO + o00O0oo % OoooooooOO % Ooo00oOo00o
def IIi1 ( url ) :
 IIiIi1iI = i1IiiiI1iI ( oOo0oooo00o ( 'aHR0cHM6Ly9kbC5kcm9wYm94dXNlcmNvbnRlbnQuY29tL3MvN2ZrMjhndDlwb3QxMjJhL0JVSUxEUy50eHQ/ZGw9MA==' ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 ooOOoooooo = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( IIiIi1iI )
 for II1I , url , O0i1II1Iiii1I11 , IIIIiiIiI , o00oooO0Oo in ooOOoooooo :
  ooooooO0oo ( II1I , url , 42 , O0i1II1Iiii1I11 , IIIIiiIiI , o00oooO0Oo )
 I1i1I1II ( 'movies' , 'MAIN' )
 if 45 - 45: oO0o0ooO0 / oO0o0ooO0 + O0oO + o0oO0
def iI111i ( url ) :
 IIiIi1iI = i1IiiiI1iI ( OO0o + IIi11i1i1iI1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 ooOOoooooo = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( IIiIi1iI )
 for II1I , url , O0i1II1Iiii1I11 , IIIIiiIiI , o00oooO0Oo in ooOOoooooo :
  ooooooO0oo ( II1I , url , 40 , O0i1II1Iiii1I11 , IIIIiiIiI , o00oooO0Oo )
 I1i1I1II ( 'movies' , 'MAIN' )
 if 23 - 23: i11iIiiIii + OOooOOo . i1IIi
def o0Ooo00o0Oooo ( url ) :
 IIiIi1iI = i1IiiiI1iI ( OO0o + OOooooO0Oo ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 ooOOoooooo = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( IIiIi1iI )
 for II1I , url , O0i1II1Iiii1I11 , IIIIiiIiI , o00oooO0Oo in ooOOoooooo :
  ooooooO0oo ( II1I , url , 5 , O0i1II1Iiii1I11 , IIIIiiIiI , o00oooO0Oo )
 I1i1I1II ( 'movies' , 'MAIN' )
 if 91 - 91: OOooOOo . iIii1I11I1II1 / OoOO + i1IIi
def I1i ( ) :
 OOOOO0oo0O0O0 = oOoO0O0o0Oooo ( oOo0oooo00o ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vYXBrdG9vbC9hcGsucGhw' ) )
 ooOOoooooo = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( OOOOO0oo0O0O0 )
 for I1Ii1iI1 , oO0 , II1I in ooOOoooooo :
  O0OO0O ( II1I , I1Ii1iI1 , 2031 , oOOoO0 + 'APK.png' )
  if 81 - 81: OoOO . OOooOOo % O0 / OOOo0 - OoOO
def Ii1I1i ( name , url , description ) :
 OO = xbmc . translatePath ( os . path . join ( I1iI1ii1II , 'Download' ) )
 i1111 = xbmcgui . DialogProgress ( )
 i1111 . create ( "Your App Is Downloading" , "Why not check out our website" , '' , 'Http://architects.x10host.com' )
 O0O0OOOOoo = os . path . join ( OO , name + '.apk' )
 try :
  os . remove ( O0O0OOOOoo )
 except :
  pass
 downloader . download ( url , O0O0OOOOoo , i1111 )
 ii11iIi1I = xbmcgui . Dialog ( )
 ii11iIi1I . ok ( "GenieTv" , "[COLORred]Please press ok, exit kodi and go to your downloads folder to install your app[/COLOR]" , "[COLORblue]Tool Brought To You By Architects@Work[/COLOR]" )
 if 74 - 74: ii11ii1ii + OoOoOO00 / Ooo00oOo00o
def oOo0O0Oo00oO ( url ) :
 OO = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/resources/downloads' ) )
 i1111 = xbmcgui . DialogProgress ( )
 i1111 . create ( "Your fILM Is Downloading" , "Why not check out our website" , '' , 'Http://architects.x10host.com' )
 O0O0OOOOoo = os . path . join ( OO , II1I + '.mp4' )
 try :
  os . remove ( O0O0OOOOoo )
 except :
  pass
 downloader . download ( url , O0O0OOOOoo , i1111 )
 ii11iIi1I = xbmcgui . Dialog ( )
 ii11iIi1I . ok ( "GenieTv" , "[COLORred]Please press ok, Your download With Be Avaiilable Via The My Downloads Button[/COLOR]" , "[COLORblue]Tool Brought To You By Architects@Work[/COLOR]" )
 if 7 - 7: IIII * O0oO % o00O0oo - OOooOOo
 if 13 - 13: o00O0oo . i11iIiiIii
def oOOoo00O00o ( name , url , description ) :
 OO = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 i1111 = xbmcgui . DialogProgress ( )
 i1111 . create ( "Your Art Pack Is Downloading" , "Why not check out our website" , '' , 'Http://architects.x10host.com' )
 O0O0OOOOoo = os . path . join ( OO , name )
 try :
  os . remove ( O0O0OOOOoo )
 except :
  pass
 downloader . download ( url , O0O0OOOOoo , i1111 )
 O0O00Oo = xbmc . translatePath ( os . path . join ( i1 ) )
 time . sleep ( 2 )
 i1111 . update ( 0 , "" , "Placing Your Art Please Wait" )
 print '======================================='
 print O0O00Oo
 print '======================================='
 extract . all ( O0O0OOOOoo , O0O00Oo , i1111 )
 ii11iIi1I = xbmcgui . Dialog ( )
 ii11iIi1I . ok ( "GenieTv" , "[COLORred]Once complete your artwork will be stored in your Media folder, Accessible via the Homefolder, Enjoy[/COLOR]" )
 if 97 - 97: O0 * OoooooooOO . OoooooooOO
 if 33 - 33: O0oO + oO0o0ooO0 * OoOO / iIii1I11I1II1 - OOOo0
def O0oOOO0ooOOO0OOO ( url ) :
 IIiIi1iI = i1IiiiI1iI ( oOo0oooo00o ( 'aHR0cDovL2dlbmlldHYuYXJjaGl0ZWN0cy54MTBob3N0LmNvbS90ZXN0L3doLnR4dA==' ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 ooOOoooooo = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( IIiIi1iI )
 for II1I , url , O0i1II1Iiii1I11 , IIIIiiIiI , o00oooO0Oo in ooOOoooooo :
  ooooooO0oo ( II1I , url , 5 , O0i1II1Iiii1I11 , IIIIiiIiI , o00oooO0Oo )
 try :
  IIiIi1iI = i1IiiiI1iI ( oO00oooOOoOo0 + oooOOOOO + OoOOoOooooOOo ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
  ooOOoooooo = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( IIiIi1iI )
  for II1I , url , O0i1II1Iiii1I11 , IIIIiiIiI , o00oooO0Oo in ooOOoooooo :
   ooooooO0oo ( II1I , url , 5 , O0i1II1Iiii1I11 , IIIIiiIiI , o00oooO0Oo )
 except : pass
 I1i1I1II ( 'movies' , 'INFO' )
 if 87 - 87: OOOo0
 if 58 - 58: I1IiI % OOooOOo
def i1OOoO ( url ) :
 IIiIi1iI = i1IiiiI1iI ( oOo0oooo00o ( 'aHR0cDovL2dlbmlldHYuYXJjaGl0ZWN0cy54MTBob3N0LmNvbS90ZXN0L3doLnR4dA==' ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 ooOOoooooo = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( IIiIi1iI )
 for II1I , url , O0i1II1Iiii1I11 , IIIIiiIiI , o00oooO0Oo in ooOOoooooo :
  ooooooO0oo ( II1I , url , 43 , O0i1II1Iiii1I11 , IIIIiiIiI , o00oooO0Oo )
 try :
  IIiIi1iI = i1IiiiI1iI ( oO00oooOOoOo0 + oooOOOOO + OoOOoOooooOOo ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
  ooOOoooooo = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( IIiIi1iI )
  for II1I , url , O0i1II1Iiii1I11 , IIIIiiIiI , o00oooO0Oo in ooOOoooooo :
   ooooooO0oo ( II1I , url , 43 , O0i1II1Iiii1I11 , IIIIiiIiI , o00oooO0Oo )
 except : pass
 I1i1I1II ( 'movies' , 'INFO' )
 if 89 - 89: OOooOOo + Ooo00oOo00o * o0000oOoOoO0o * o00O0oo
 if 37 - 37: OoooooooOO - O0 - OOooOOo
def o0o0O0O00oOOo ( name , url , description ) :
 OO = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 i1111 = xbmcgui . DialogProgress ( )
 i1111 . create ( "GenieTv" , "Downloading Content" , '' , 'Please Wait' )
 O0O0OOOOoo = os . path . join ( OO , name + '.zip' )
 try :
  os . remove ( O0O0OOOOoo )
 except :
  pass
 downloader . download ( url , O0O0OOOOoo , i1111 )
 iIIIiIi = xbmc . translatePath ( os . path . join ( 'special://home' , 'addons' ) )
 time . sleep ( 2 )
 i1111 . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print iIIIiIi
 print '======================================='
 extract . all ( O0O0OOOOoo , iIIIiIi , i1111 )
 ii11iIi1I = xbmcgui . Dialog ( )
 ii11iIi1I . ok ( "GenieTv" , "Press ok to finish install" , "[COLOR yellow]Brought To You By Architects@Work[/COLOR]" )
 OO0O0 ( )
 if 30 - 30: OoOO0ooOOoo0O + ii11ii1ii * o0000oOoOoO0o % i11iIiiIii % I1IiI
 if 97 - 97: ii11ii1ii % ii11ii1ii % OoOO / oO0o0ooO0 - iIii1I11I1II1
def ooooo0O0000oo ( name , url , description ) :
 OO = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 i1111 = xbmcgui . DialogProgress ( )
 i1111 . create ( "GenieTv" , "Downloading " , '' , 'Please Wait' )
 O0O0OOOOoo = os . path . join ( OO , 'plugin.program.GenieTv.install' + '.zip' )
 try :
  os . remove ( O0O0OOOOoo )
 except :
  pass
 downloader . download ( url , O0O0OOOOoo , i1111 )
 iIIIiIi = xbmc . translatePath ( os . path . join ( 'special://' , 'home' ) )
 time . sleep ( 2 )
 i1111 . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print iIIIiIi
 print '======================================='
 extract . all ( O0O0OOOOoo , iIIIiIi , i1111 )
 ii11iIi1I = xbmcgui . Dialog ( )
 ii11iIi1I . ok ( "GenieTv" , "Press ok to force close kodi, if unsuccessful using windows Please kill kodi via taskmanager" , "[COLOR yellow]Brought To You By Architects@Work[/COLOR]" )
 iIii1II11 ( )
 if 65 - 65: OoooooooOO - ii11ii1ii / o0oO0 / OoOoOO00 / i1IIi
def o00oo0 ( name , url , description ) :
 OO = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 i1111 = xbmcgui . DialogProgress ( )
 i1111 . create ( "GenieTv" , "Downloading " , '' , 'Please Wait' )
 O0O0OOOOoo = os . path . join ( OO , 'plugin.program.GenieTv.install' + '.zip' )
 try :
  os . remove ( O0O0OOOOoo )
 except :
  pass
 downloader . download ( url , O0O0OOOOoo , i1111 )
 iIIIiIi = xbmc . translatePath ( os . path . join ( 'special://' , 'home' ) )
 time . sleep ( 2 )
 i1111 . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print iIIIiIi
 print '======================================='
 extract . all ( O0O0OOOOoo , iIIIiIi , i1111 )
 ii11iIi1I = xbmcgui . Dialog ( )
 ii11iIi1I . ok ( "GenieTv" , "Please Disconnect The Power From Your Device. DO NOT EXIT CLEANLY VIA SHUTDOWN" , "[COLOR yellow]Brought To You By Architects@Work[/COLOR]" )
 if 38 - 38: o0oO0 % OoOoOO00 % o0000oOoOoO0o / Ooo00oOo00o + I1IiI / i1IIi
 if 54 - 54: iIii1I11I1II1 % ii11ii1ii - OoOO0ooOOoo0O / OoOO - Ooo00oOo00o . o0000oOoOoO0o
def IIo0Oo0oO0oOO00 ( name , url , description ) :
 iIIIiIi = xbmc . translatePath ( os . path . join ( 'special://' , 'home' ) )
 i1111 = xbmcgui . DialogProgress ( )
 O0O0OOOOoo = os . path . join ( oo0o0O00 )
 time . sleep ( 2 )
 i1111 . create ( "GenieTv" , "Restoring" , '' , 'Please Wait' )
 print '======================================='
 print iIIIiIi
 print '======================================='
 extract . all ( O0O0OOOOoo , iIIIiIi , i1111 )
 ii11iIi1I = xbmcgui . Dialog ( )
 ii11iIi1I . ok ( "GenieTv" , "Please Disconnect The Power From Your Device. DO NOT EXIT CLEANLY VIA SHUTDOWN" , "[COLOR yellow]Brought To You By Architects@Work[/COLOR]" )
 if 92 - 92: OoooooooOO * O0oO
 if 100 - 100: O0oO + O0oO * IIII
def iIii1II11 ( ) :
 I1iO00Oooo = xbmcgui . Dialog ( ) . yesno ( 'Force Close Kodi' , 'You are about to close Kodi' , 'Would you like to continue?' , nolabel = 'No, Cancel' , yeslabel = 'Yes, Close' )
 if I1iO00Oooo == 0 :
  return
 elif I1iO00Oooo == 1 :
  pass
 i11I = o00Oo0oooooo ( )
 print "Platform: " + str ( i11I )
 if i11I == 'osx' :
  print "############   try osx force close  #################"
  try : os . system ( 'killall -9 XBMC' )
  except : pass
  try : os . system ( 'killall -9 Kodi' )
  except : pass
  ii11iIi1I . ok ( "[COLOR=red][B]WARNING  !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu." , '' )
 elif i11I == 'linux' :
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
 elif i11I == 'android' :
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
 elif i11I == 'windows' :
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
  if 76 - 76: o0000oOoOoO0o / OoOO0ooOOoo0O . O0 % OOOo0 . OOooOOo + IIII
def o00Oo0oooooo ( ) :
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
  if 71 - 71: O0oO . OoOoOO00
  if 62 - 62: OoooooooOO . o0000oOoOoO0o
  if 61 - 61: I1IiI - OoOO0ooOOoo0O - i1IIi
def IiI1iIiIIIii ( url ) :
 i1111 . create ( "[COLOR=green]GenieTv[/COLOR]" , "Renaming paths..." , '' , 'Please Wait' )
 for oOoO , oOoO00O0 , OOIi1iI111II1I1 in os . walk ( url ) :
  for file in OOIi1iI111II1I1 :
   if file . endswith ( ".xml" ) :
    i1111 . update ( 0 , "Fixing" , file , 'Please Wait' )
    oOOOOoOO0o = open ( ( os . path . join ( oOoO , file ) ) ) . read ( )
    i1II1 = oOOOOoOO0o . replace ( iI111I11I1I1 , 'special://home/' )
    i11i1 = open ( ( os . path . join ( oOoO , file ) ) , mode = 'w' )
    i11i1 . write ( str ( i1II1 ) )
    i11i1 . close ( )
 iIii1II11 ( )
 if 42 - 42: i11iIiiIii * iIii1I11I1II1 / ii11ii1ii . i11iIiiIii % o0000oOoOoO0o
def i1iI ( ) :
 OOOOO0oo0O0O0 = oOoO0O0o0Oooo ( oOo0oooo00o ( 'aHR0cDovL3d3dy5saXN0ZW5saXZlLmV1L3VrLmh0bWw=' ) )
 ooOOoooooo = re . compile ( '<tr>.+?<td><a href=".+?"><b>(.+?)</b>.+?<td><a href="(.+?)">' , re . DOTALL ) . findall ( OOOOO0oo0O0O0 )
 for II1I , I1Ii1iI1 in ooOOoooooo :
  IiI1iiiIii ( II1I , I1Ii1iI1 , 222 , oOOoO0 + 'radio.png' )
  if 7 - 7: O0oO * Ooo00oOo00o - o0oO0 + OoOO0ooOOoo0O * OOOo0 % Ooo00oOo00o
def iI1i111I1Ii ( ) :
 OOOOO0oo0O0O0 = oOoO0O0o0Oooo ( oOo0oooo00o ( 'aHR0cDovL3d3dy50b29uamV0LmNvbS8=' ) )
 ooOOoooooo = re . compile ( '<a href="(.+?)" style="font-size:.8em;">(.+?)</a>' ) . findall ( OOOOO0oo0O0O0 )
 for I1Ii1iI1 , II1I in ooOOoooooo :
  O0OO0O ( '[COLORgreen]' + II1I + '[/COLOR]' , 'http://www.toonjet.com/' + I1Ii1iI1 , 8051 , oOOoO0 + 'classictoons.png' )
def i11i1ii1I ( url ) :
 OOOOO0oo0O0O0 = oOoO0O0o0Oooo ( url )
 ooOOoooooo = re . compile ( '<a href="(.+?)"><img src="(.+?)"' ) . findall ( OOOOO0oo0O0O0 )
 o0OO0o0o00o = re . compile ( '<a href="(.+?)">.+?</a></td></tr></table>' ) . findall ( OOOOO0oo0O0O0 )
 for url , oOo0 in ooOOoooooo :
  if 'ol.gif' in oOo0 :
   pass
  elif 'link_block_' in oOo0 :
   pass
  elif '.png' in oOo0 :
   pass
  else :
   O0OO0O ( ( oOo0 ) . replace ( 'http://www.toonjet.com/images/icons/' , '' ) . replace ( 'images/icons/' , '' ) . replace ( '.jpg' , '' ) . replace ( '_icon' , '' ) . replace ( '_' , ' ' ) , 'http://www.toonjet.com/' + url , 8052 , oOOoO0 + 'vod.png' )
 for url in o0OO0o0o00o :
  O0OO0O ( 'NEXT PAGE' , 'http://www.toonjet.com/' + url , 8051 , oOOoO0 + 'documentary.png' )
def OOOoOO ( url ) :
 OOOOO0oo0O0O0 = oOoO0O0o0Oooo ( url )
 ooOOoooooo = re . compile ( '<iframe width="640" height="480" src="(.+?)" frameborder="0" allowfullscreen></iframe>' ) . findall ( OOOOO0oo0O0O0 )
 for url in ooOOoooooo :
  IiI1iiiIii ( '[COLORgreen]PLAY[/COLOR]' , ( url ) . replace ( 'http://www.youtube.com/embed/' , '' ) . replace ( '?autoplay=0' , '' ) , 8043 , oOOoO0 + 'classictoons.png' )
  if 10 - 10: oO0o0ooO0 + Oo * ii11ii1ii + iIii1I11I1II1 / O0oO / ii11ii1ii
  if 42 - 42: OOOo0
def II1i11I ( ) :
 O0OO0O ( '[COLORgreen]CARTOONS[/COLOR]' , '' , 20001 , oOOoO0 + 'ORIGINCARTOON.png' )
 O0OO0O ( '[COLORgreen]ANIME[/COLOR]' , 'https://kissanime.to/AnimeList' , 20001 , oOOoO0 + 'ORIGINCARTOON.png' )
 if 50 - 50: OoooooooOO % o0000oOoOoO0o
def IIii1111 ( ) :
 O0OO0O ( '[COLORgreen]BY NAME[/COLOR]' , 'http://kisscartoon.me/CartoonList' , 20002 , oOOoO0 + 'ORIGINCARTOON.png' )
 O0OO0O ( '[COLORgreen]BY GENRE[/COLOR]' , 'http://kisscartoon.me/CartoonList' , 20003 , oOOoO0 + 'ORIGINCARTOON.png' )
 if 42 - 42: o0000oOoOoO0o / OOooOOo . OoOO + OoOO % I1IiI + i11iIiiIii
def oo0o0000 ( url ) :
 iiI = cloudflare . source ( url )
 ooOOoooooo = re . compile ( 'href="(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( iiI )
 for url , II1I in ooOOoooooo :
  if '?c=' in url :
   O0OO0O ( '[COLORgreen]' + II1I + '[/COLOR]' , 'http://kisscartoon.me' + url , 20004 , oOOoO0 + 'ORIGINCARTOON.png' )
   if 82 - 82: Oo + Ooo00oOo00o
def O00O ( url ) :
 iiI = cloudflare . source ( url )
 ooOOoooooo = re . compile ( 'href="(.+?)" title="(.+?)">/n(.+?)</a><br/>' , re . DOTALL ) . findall ( iiI )
 for url , OOO , II1I in ooOOoooooo :
  if 'Genre' in url :
   O0OO0O ( '[COLORgreen]' + II1I + '[/COLOR]' , 'http://kisscartoon.me' + url , 20004 , oOOoO0 + 'ORIGINCARTOON.png' )
   if 6 - 6: OoooooooOO
def iI1iIii11Ii ( url ) :
 iiI = cloudflare . source ( url )
 ooOOoooooo = re . compile ( 'src="(.+?)" style=.+?<a class="bigChar" href="(.+?)">(.+?)</a>.+?<p>(.+?)</p>' , re . DOTALL ) . findall ( iiI )
 for url , OOO , II1I in ooOOoooooo :
  ooooooO0oo ( '[COLORgreen]' + II1I + '[/COLOR]' , 'http://kisscartoon.me' + url , 20005 , img , '' , OOO )
  if 8 - 8: ii11ii1ii * O0oO . o0oO0 / o00O0oo - Oo % O0
def iI1i1i11I1iI ( url ) :
 iiI = cloudflare . source ( url )
 ooOOoooooo = re . compile ( '<img width="120" height="165" src="(.+?)" style=.+?<a class="bigChar" href="(.+?)">(.+?)</a>.+?<p>(.+?)</p>' , re . DOTALL ) . findall ( iiI )
 for url , OOO , II1I in ooOOoooooo :
  ooooooO0oo ( '[COLORgreen]' + II1I + '[/COLOR]' , 'http://kisscartoon.me' + url , 20005 , img , '' , OOO )
  if 84 - 84: o0oO0 % o00O0oo + i11iIiiIii
  if 28 - 28: Oo + Ooo00oOo00o * OoOO0ooOOoo0O % OoOO . o0000oOoOoO0o % O0
  if 16 - 16: o0000oOoOoO0o - iIii1I11I1II1 / OOOo0 . OoOoOO00 + iIii1I11I1II1
  if 19 - 19: Ooo00oOo00o - Oo . O0
  if 60 - 60: OoOoOO00 + Oo
def I1IiIiiIiIII ( ) :
 if 8 - 8: OoOO / ii11ii1ii
 ooooooO0oo ( '[COLORgreen]Cartoons[/COLOR]' , '' , 10004 , oOOoO0 + 'ORIGINCARTOON.png' , OOooO0OOoo , '' )
 ooooooO0oo ( '[COLORgreen]Search Cartoons[/COLOR]' , '' , 10005 , oOOoO0 + 'ORIGINCARTOON.png' , OOooO0OOoo , '' )
 if 20 - 20: OOOo0
def o0oO000oo ( ) :
 o00o0 = Oo0o0000o0o0 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 II1III1I1I1Ii = o00o0 . lower ( )
 iiI = i1IiiiI1iI ( oOo0oooo00o ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2NhcnRvb24=' ) )
 ooOOoooooo = re . compile ( '<td><a href="(.+?)">(.+)</a></td>' ) . findall ( iiI )
 for I1Ii1iI1 , II1I in ooOOoooooo :
  if o00o0 in II1I . lower ( ) :
   if 'Dad!' in II1I :
    pass
   elif 'Family Guy' in II1I :
    pass
   elif '2 Stupid' in II1I :
    pass
   elif 'The Zelfs' in II1I :
    pass
   elif 'A Clone' in II1I :
    pass
   elif 'A.T.O.M' in II1I :
    pass
   elif 'Almost Naked' in II1I :
    pass
   elif 'Angry Kid' in II1I :
    pass
   elif 'Annoying Orange' in II1I :
    pass
   elif 'Aqua Teen' in II1I :
    pass
   elif 'Assy Mcgee' in II1I :
    pass
   elif 'Astroblast' in II1I :
    pass
   elif 'Atomic Betty' in II1I :
    pass
   elif 'Axe Cop' in II1I :
    pass
   elif 'Baby Playpen' in II1I :
    pass
   elif 'Beavis and Butt' in II1I :
    pass
   elif 'Celebrity Deathmatch' in II1I :
    pass
   elif 'Clerks The' in II1I :
    pass
   elif 'Crapston Villas' in II1I :
    pass
   elif 'Duckman:' in II1I :
    pass
   elif 'Stripperella' in II1I :
    pass
   elif 'Vixen' in II1I :
    pass
   else :
    ooooooO0oo ( '[COLORgreen]' + II1I + '[/COLOR]' , I1Ii1iI1 , 10006 , oOOoO0 + 'ORIGINCARTOON.png' , OOooO0OOoo , '' )
  xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 70 - 70: Ooo00oOo00o % OoOO + OoOO0ooOOoo0O / o00O0oo % O0
def oO00O0 ( ) :
 OOOOO0oo0O0O0 = i1IiiiI1iI ( oOo0oooo00o ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2NhcnRvb24=' ) )
 ooOOoooooo = re . compile ( '<td><a href="(.+?)">(.+)</a></td>' ) . findall ( OOOOO0oo0O0O0 )
 for I1Ii1iI1 , II1I in ooOOoooooo :
  if 'Dad!' in II1I :
   pass
  elif 'Family Guy' in II1I :
   pass
  elif '2 Stupid' in II1I :
   pass
  elif 'The Zelfs' in II1I :
   pass
  elif 'A Clone' in II1I :
   pass
  elif 'A.T.O.M' in II1I :
   pass
  elif 'Almost Naked' in II1I :
   pass
  elif 'Angry Kid' in II1I :
   pass
  elif 'Annoying Orange' in II1I :
   pass
  elif 'Aqua Teen' in II1I :
   pass
  elif 'Assy Mcgee' in II1I :
   pass
  elif 'Astroblast' in II1I :
   pass
  elif 'Atomic Betty' in II1I :
   pass
  elif 'Axe Cop' in II1I :
   pass
  elif 'Baby Playpen' in II1I :
   pass
  elif 'Beavis and Butt' in II1I :
   pass
  elif 'Celebrity Deathmatch' in II1I :
   pass
  elif 'Clerks The' in II1I :
   pass
  elif 'Crapston Villas' in II1I :
   pass
  elif 'Duckman:' in II1I :
   pass
  elif 'Stripperella' in II1I :
   pass
  elif 'Vixen' in II1I :
   pass
  else :
   ooooooO0oo ( '[COLORgreen]' + II1I + '[/COLOR]' , I1Ii1iI1 , 10006 , oOOoO0 + 'ORIGINCARTOON.png' , OOooO0OOoo , '' )
 xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 36 - 36: OoOO - o00O0oo . Oo - i11iIiiIii - OoOO0ooOOoo0O * Oo
def OooOOOO ( url ) :
 OOOOO0oo0O0O0 = i1IiiiI1iI ( url )
 o0OO0o0o00o = re . compile ( '<img src="(.+?)" id="series_image" width="250" height="370" alt=".+?" />' ) . findall ( OOOOO0oo0O0O0 )
 for oOo0 in o0OO0o0o00o :
  iIIIiiI1i1i = oOo0
 iIII = re . compile ( '<li><a href="(.+?)">Next</a></li>' ) . findall ( OOOOO0oo0O0O0 )
 for url in iIII :
  ooooooO0oo ( '[COLORgreen]NEXT PAGE[/COLOR]' , url , 10006 , iIIIiiI1i1i , OOooO0OOoo , '' )
 ooOOoooooo = re . compile ( '&nbsp;<a href="(.+?)">(.+?)</a>' ) . findall ( OOOOO0oo0O0O0 )
 for url , II1I in ooOOoooooo :
  IiI1iiiIii ( '[COLORgreen]' + II1I + '[/COLOR]' , url , 10007 , iIIIiiI1i1i )
  if 70 - 70: oO0o0ooO0 / iIii1I11I1II1
  if 85 - 85: OoooooooOO % i1IIi * OoooooooOO / ii11ii1ii
 xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 96 - 96: OoooooooOO + OoOO
def iiII1i11i ( url , IMAGE ) :
 OOOOO0oo0O0O0 = i1IiiiI1iI ( url )
 ooOOoooooo = re . compile ( '"playlist">(.+?)</span></div><div><iframe src="(.+?)"' ) . findall ( OOOOO0oo0O0O0 )
 for II1I , url in ooOOoooooo :
  print II1I + '     ' + url
  if 'easy' in url :
   IiIi ( url )
   if 87 - 87: ii11ii1ii - ii11ii1ii - oO0o0ooO0 + OoOO
   if 82 - 82: OoOO / iIii1I11I1II1 . OOOo0 . OoOO0ooOOoo0O / OOooOOo
  xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 42 - 42: Oo
def IiIi ( url ) :
 OOOOO0oo0O0O0 = i1IiiiI1iI ( url )
 ooOOoooooo = re . compile ( "url: '(.+?)'," ) . findall ( OOOOO0oo0O0O0 )
 for url in ooOOoooooo :
  II1IIiiIiI ( url )
  if 1 - 1: oO0o0ooO0
  if 97 - 97: OoOO0ooOOoo0O + oO0o0ooO0 + O0 + i11iIiiIii
  if 77 - 77: OOooOOo / OoooooooOO
def IIii11I1i1I ( ) :
 if 99 - 99: oO0o0ooO0
 ooooooO0oo ( '[COLORgreen]Genres[/COLOR]' , '' , 10032 , oOOoO0 + 'IZLEFILMS.png' , OOooO0OOoo , '' )
 ooooooO0oo ( '[COLORgreen]Popular Movies[/COLOR]' , '' , 10033 , oOOoO0 + 'IZLEFILMS.png' , OOooO0OOoo , '' )
 ooooooO0oo ( '[COLORgreen]Boxsets[/COLOR]' , '' , 10034 , oOOoO0 + 'IZLEFILMS.png' , OOooO0OOoo , '' )
 ooooooO0oo ( '[COLORgreen]Search[/COLOR]' , '' , 10035 , oOOoO0 + 'IZLEFILMS.png' , OOooO0OOoo , '' )
if 76 - 76: Ooo00oOo00o * OOOo0
if 82 - 82: o00O0oo * oO0o0ooO0 / ii11ii1ii
if 36 - 36: OoooooooOO - i1IIi . O0 / OoOoOO00 + OOooOOo
if 33 - 33: OoOoOO00 / o0oO0 * O0 % o00O0oo * O0oO
if 100 - 100: IIII . o0000oOoOoO0o / o00O0oo % I1IiI % OoOoOO00 - Ooo00oOo00o
if 46 - 46: O0 * OoOoOO00 - Oo * o0oO0
if 33 - 33: o00O0oo
if 74 - 74: OoOO0ooOOoo0O + O0 + i1IIi - i1IIi + OoOoOO00
if 83 - 83: ii11ii1ii - OOOo0 + OoOO0ooOOoo0O
if 5 - 5: o00O0oo
if 46 - 46: IIII
if 45 - 45: o0oO0
if 21 - 21: OoOO . O0oO . OoOO0ooOOoo0O / Oo / O0oO
if 17 - 17: OoOO0ooOOoo0O / OoOO0ooOOoo0O / o0000oOoOoO0o
if 1 - 1: i1IIi . i11iIiiIii % OoOO0ooOOoo0O
def OooO0oo ( ) :
 ooooooO0oo ( '[COLORgreen]Action[/COLOR]' , 'http://www.izlemeyedeger.com/tur/aksiyon' , 10036 , oOOoO0 + 'IZLEFILMS.png' , OOooO0OOoo , '' )
 ooooooO0oo ( '[COLORgreen]Adventure[/COLOR]' , 'http://www.izlemeyedeger.com/tur/macera' , 10036 , oOOoO0 + 'IZLEFILMS.png' , OOooO0OOoo , '' )
 ooooooO0oo ( '[COLORgreen]Animation[/COLOR]' , 'http://www.izlemeyedeger.com/tur/animasyon' , 10036 , oOOoO0 + 'IZLEFILMS.png' , OOooO0OOoo , '' )
 ooooooO0oo ( '[COLORgreen]Biography[/COLOR]' , 'http://www.izlemeyedeger.com/tur/biyografi' , 10036 , oOOoO0 + 'IZLEFILMS.png' , OOooO0OOoo , '' )
 ooooooO0oo ( '[COLORgreen]Comedy[/COLOR]' , 'http://www.izlemeyedeger.com/tur/komedi' , 10036 , oOOoO0 + 'IZLEFILMS.png' , OOooO0OOoo , '' )
 ooooooO0oo ( '[COLORgreen]Crime[/COLOR]' , 'http://www.izlemeyedeger.com/tur/suc' , 10036 , oOOoO0 + 'IZLEFILMS.png' , OOooO0OOoo , '' )
 ooooooO0oo ( '[COLORgreen]Documentary[/COLOR]' , 'http://www.izlemeyedeger.com/tur/belgesel' , 10036 , oOOoO0 + 'IZLEFILMS.png' , OOooO0OOoo , '' )
 ooooooO0oo ( '[COLORgreen]Drama[/COLOR]' , 'http://www.izlemeyedeger.com/tur/dram' , 10036 , oOOoO0 + 'IZLEFILMS.png' , OOooO0OOoo , '' )
 ooooooO0oo ( '[COLORgreen]Family[/COLOR]' , 'http://www.izlemeyedeger.com/tur/aile' , 10036 , oOOoO0 + 'IZLEFILMS.png' , OOooO0OOoo , '' )
 ooooooO0oo ( '[COLORgreen]Fantasy[/COLOR]' , 'http://www.izlemeyedeger.com/tur/fantastik' , 10036 , oOOoO0 + 'IZLEFILMS.png' , OOooO0OOoo , '' )
 ooooooO0oo ( '[COLORgreen]Far East[/COLOR]' , 'http://www.izlemeyedeger.com/tur/uzak-dogu' , 10036 , oOOoO0 + 'IZLEFILMS.png' , OOooO0OOoo , '' )
 ooooooO0oo ( '[COLORgreen]History[/COLOR]' , 'http://www.izlemeyedeger.com/tur/tarih' , 10036 , oOOoO0 + 'IZLEFILMS.png' , OOooO0OOoo , '' )
 ooooooO0oo ( '[COLORgreen]Horror[/COLOR]' , 'http://www.izlemeyedeger.com/tur/korku' , 10036 , oOOoO0 + 'IZLEFILMS.png' , OOooO0OOoo , '' )
 ooooooO0oo ( '[COLORgreen]Musical[/COLOR]' , 'http://www.izlemeyedeger.com/tur/muzikal' , 10036 , oOOoO0 + 'IZLEFILMS.png' , OOooO0OOoo , '' )
 ooooooO0oo ( '[COLORgreen]Mystery[/COLOR]' , 'http://www.izlemeyedeger.com/tur/gizem' , 10036 , oOOoO0 + 'IZLEFILMS.png' , OOooO0OOoo , '' )
 ooooooO0oo ( '[COLORgreen]Romance[/COLOR]' , 'http://www.izlemeyedeger.com/tur/romantik' , 10036 , oOOoO0 + 'IZLEFILMS.png' , OOooO0OOoo , '' )
 ooooooO0oo ( '[COLORgreen]Science Fiction[/COLOR]' , 'http://www.izlemeyedeger.com/tur/bilimkurgu' , 10036 , oOOoO0 + 'IZLEFILMS.png' , OOooO0OOoo , '' )
 ooooooO0oo ( '[COLORgreen]Sport[/COLOR]' , 'http://www.izlemeyedeger.com/tur/spor' , 10036 , oOOoO0 + 'IZLEFILMS.png' , OOooO0OOoo , '' )
 ooooooO0oo ( '[COLORgreen]Thriller[/COLOR]' , 'http://www.izlemeyedeger.com/tur/gerilim' , 10036 , oOOoO0 + 'IZLEFILMS.png' , OOooO0OOoo , '' )
 ooooooO0oo ( '[COLORgreen]War[/COLOR]' , 'http://www.izlemeyedeger.com/tur/savas' , 10036 , oOOoO0 + 'IZLEFILMS.png' , OOooO0OOoo , '' )
 ooooooO0oo ( '[COLORgreen]Western[/COLOR]' , 'http://www.izlemeyedeger.com/tur/western' , 10036 , oOOoO0 + 'IZLEFILMS.png' , OOooO0OOoo , '' )
 if 89 - 89: o00O0oo
def ooOoOO0OoO00o ( url ) :
 iiI = cloudflare . source ( url )
 ooOOoooooo = re . compile ( '<li>.+?<a href="(.+?)">.+?<img src="(.+?)" alt=""/>.+?<span class="year">\n(.+?)</span>.+?<span class="video-title">\n(.+?)</span>.+?</li>' , re . DOTALL ) . findall ( iiI )
 for url , oOo0 , II1iiiiII , II1I in ooOOoooooo :
  II1I = ( II1I ) . replace ( '  ' , '' ) + ' ' + ( II1iiiiII ) . replace ( '  ' , '' )
  O0i1II1Iiii1I11 = oOo0
  url = url
  O0OoOO0oo0 ( II1I , O0i1II1Iiii1I11 , url )
 oOO = re . compile ( '<a href="http://www.izlemeyedeger.com/tur/(.+?)?s=(.+?)&sort=&orderby=">(.+?)</a>' ) . findall ( iiI )
 for url , O0o0OO0000ooo , II1I in oOO :
  ooooooO0oo ( '[COLORgold] Page ' + II1I + '[/COLOR]' , 'http://www.izlemeyedeger.com/tur/' + url + '?s=' + O0o0OO0000ooo + '&sort=&orderby=' , 10036 , '' , OOooO0OOoo , '' )
  if 4 - 4: o00O0oo
  if 51 - 51: Ooo00oOo00o - O0 % OoOO - OoOoOO00
def I1II ( ) :
 if 64 - 64: O0 % o0000oOoOoO0o % O0 * Ooo00oOo00o . OoOO + OOOo0
 iiI = cloudflare . source ( oOo0oooo00o ( 'aHR0cDovL3d3dy5pemxlbWV5ZWRlZ2VyLmNvbQ==' ) )
 O00 = re . compile ( '<!-- popüler filmler -->(.+?)<!-- content -->' , re . DOTALL ) . findall ( iiI )
 for I11ii1i1 in O00 :
  ooOOoooooo = re . compile ( '<li>.+?<a href="(.+?)">.+?<img width=".+?" height=".+?" src="(.+?)" alt=""/>.+?<span class="year">(.+?)</span>.+?<span class=".+?">(.+?)</span>.+?</li>' , re . DOTALL ) . findall ( str ( O00 ) )
  for I1Ii1iI1 , oOo0 , II1iiiiII , II1I in ooOOoooooo :
   II1I = ( II1I ) . replace ( '  ' , '' ) . replace ( '\\t' , '' ) . replace ( '\\r' , '' ) . replace ( '\\n' , '' ) . replace ( '\\xc3\\x87' , '' ) + ' ' + ( II1iiiiII ) . replace ( '  ' , '' ) . replace ( '\\t' , '' ) . replace ( '\\r' , '' ) . replace ( '\\n' , '' )
   O0i1II1Iiii1I11 = oOo0
   I1Ii1iI1 = I1Ii1iI1
   O0OoOO0oo0 ( II1I , O0i1II1Iiii1I11 , I1Ii1iI1 )
   if 78 - 78: oO0o0ooO0
   if 28 - 28: o0000oOoOoO0o
def oOOOOoo ( ) :
 iiI = cloudflare . source ( oOo0oooo00o ( 'aHR0cDovL3d3dy5pemxlbWV5ZWRlZ2VyLmNvbS9zZXJpLWZpbG1sZXI=' ) )
 ooOOoooooo = re . compile ( ' <div class="title">.+?</span>\n(.+?)<span style=".+?<img src="(.+?)" alt="" title=".+?<a class="more" href="(.+?)">' , re . DOTALL ) . findall ( iiI )
 for II1I , oOo0 , I1Ii1iI1 in ooOOoooooo :
  if 'IMDB' in II1I :
   pass
  else :
   ooooooO0oo ( '[COLORgreen]' + ( II1I ) . replace ( '  ' , '' ) + '[/COLOR]' , I1Ii1iI1 , 10037 , oOo0 , OOooO0OOoo , '' )
 oOO = re . compile ( '<a href="http://www.izlemeyedeger.com/seri-filmler(.+?)">(.+?)</a>' ) . findall ( iiI )
 for I1Ii1iI1 , II1I in oOO :
  ooooooO0oo ( '[COLORgold] Page ' + II1I + '[/COLOR]' , 'http://www.izlemeyedeger.com/seri-filmler' + I1Ii1iI1 , 10039 , '' , OOooO0OOoo , '' )
  if 58 - 58: OOooOOo / IIII . I1IiI / OoooooooOO + O0oO
def O0OoO0ooOO0o ( url ) :
 iiI = cloudflare . source ( url )
 ooOOoooooo = re . compile ( ' <div class="title">.+?</span>\n(.+?)<span style=".+?<img src="(.+?)" alt="" title=".+?<a class="more" href="(.+?)">' , re . DOTALL ) . findall ( iiI )
 for II1I , oOo0 , url in ooOOoooooo :
  if 'IMDB' in II1I :
   pass
  else :
   ooooooO0oo ( '[COLORgreen]' + ( II1I ) . replace ( '  ' , '' ) + '[/COLOR]' , url , 10037 , oOo0 , OOooO0OOoo , '' )
 oOO = re . compile ( '<a href="http://www.izlemeyedeger.com/seri-filmler(.+?)">(.+?)</a>' ) . findall ( iiI )
 for url , II1I in oOO :
  ooooooO0oo ( '[COLORgold] Page ' + II1I + '[/COLOR]' , 'http://www.izlemeyedeger.com/seri-filmler' + url , 10034 , '' , OOooO0OOoo , '' )
  if 81 - 81: O0 * OoOoOO00 + OOOo0 * i11iIiiIii - ii11ii1ii / OOOo0
  if 63 - 63: I1IiI - OoooooooOO % O0oO
def oOi11iI11iIiIi ( url ) :
 iiI = cloudflare . source ( url )
 ooOOoooooo = re . compile ( '<li>.+?<a href="(.+?)">.+?<img src="(.+?)" alt=""/>.+?<span class="year">\n(.+?)</span>.+?<span class="video-title">\n(.+?)</span>.+?</li>' , re . DOTALL ) . findall ( iiI )
 for url , oOo0 , II1iiiiII , II1I in ooOOoooooo :
  II1I = ( II1I ) . replace ( '  ' , '' ) . replace ( '&amp;' , '&' ) . replace ( '\\t' , '' ) . replace ( '\\r' , '' ) . replace ( '\\n' , '' ) . replace ( '\\xc3\\x87' , '' ) + ' ' + ( II1iiiiII ) . replace ( '  ' , '' ) . replace ( '\\t' , '' ) . replace ( '\\r' , '' ) . replace ( '\\n' , '' )
  O0i1II1Iiii1I11 = oOo0
  url = url
  O0OoOO0oo0 ( II1I , O0i1II1Iiii1I11 , url )
  if 100 - 100: O0oO . OOooOOo * Oo % O0 * O0
def O0OoOO0oo0 ( name , iconimage , url ) :
 iiI = cloudflare . source ( url )
 ooOOoooooo = re . compile ( '<meta itemprop="embedURL" content="(.+?)" />' ) . findall ( iiI )
 for url in ooOOoooooo :
  IIIii1 ( name , iconimage , url )
  if 71 - 71: OoOoOO00 / i1IIi . ii11ii1ii % OoooooooOO . I1IiI
def IIIii1 ( name , iconimage , url ) :
 name = name
 oOo0 = iconimage
 iiI = cloudflare . source ( url )
 ooOOoooooo = re . compile ( 'file: "(.+?)",.+?label: "(.+?)"' , re . DOTALL ) . findall ( iiI )
 for O0o0OO0000ooo , Iiiiii111i1ii in ooOOoooooo :
  IiI1iiiIii ( '[COLORgreen]' + name + ' - ' + Iiiiii111i1ii + '[/COLOR]' , O0o0OO0000ooo , 10012 , oOo0 )
  if 25 - 25: OoOO0ooOOoo0O - o0oO0 / i11iIiiIii
def iiI1ii11i1 ( ) :
 o00o0 = Oo0o0000o0o0 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 II1III1I1I1Ii = o00o0 . lower ( )
 I1Ii1iI1 = 'http://www.izlemeyedeger.com/arama?q=' + o00o0
 iiI = cloudflare . source ( I1Ii1iI1 )
 ooOOoooooo = re . compile ( '<div class="inner">.+?<li>.+?<a href="(.+?)">.+?<img src="(.+?)" alt.+?<span class="year">(.+?)</span>.+?<span class="video-title">(.+?)</span>.+?</li>.+?</div>' , re . DOTALL ) . findall ( iiI )
 for I1Ii1iI1 , oOo0 , II1iiiiII , II1I in ooOOoooooo :
  II1I = ( II1I ) . replace ( '  ' , '' ) . replace ( '\\t' , '' ) . replace ( '\\r' , '' ) . replace ( '\\n' , '' ) . replace ( '\\xc3\\x87' , '' ) + ' ' + ( II1iiiiII ) . replace ( '  ' , '' ) . replace ( '\\t' , '' ) . replace ( '\\r' , '' ) . replace ( '\\n' , '' )
  O0i1II1Iiii1I11 = oOo0
  I1Ii1iI1 = I1Ii1iI1
  O0OoOO0oo0 ( II1I , O0i1II1Iiii1I11 , I1Ii1iI1 )
  xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 38 - 38: ii11ii1ii - oO0o0ooO0 / O0 . O0oO
  if 45 - 45: O0oO
  if 83 - 83: I1IiI . OoooooooOO
def Oo0ooo ( ) :
 if 28 - 28: OoOO . OoOoOO00 / ii11ii1ii + OoOoOO00 . OoooooooOO . IIII
 ooooooO0oo ( '[COLORgreen]Stand Up[/COLOR]' , '' , 10014 , oOOoO0 + 'ORIGINSTANDUP.png' , OOooO0OOoo , '' )
 ooooooO0oo ( '[COLORgreen]Search Comedian[/COLOR]' , '' , 10015 , oOOoO0 + 'ORIGINSTANDUP.png' , OOooO0OOoo , '' )
 ooooooO0oo ( '[COLORgreen]Others[/COLOR]' , '' , 10017 , oOOoO0 + 'ORIGINSTANDUP.png' , OOooO0OOoo , '' )
 if 53 - 53: o00O0oo % o00O0oo * OOooOOo + I1IiI
def Oooo00 ( ) :
 iiI = i1IiiiI1iI ( ( oOo0oooo00o ( 'aHR0cDovL2JhY2syYmFzaWNzYnVpbGQuY28udWsvdGVzdC9zdGFuZHVwbGlzdC5waHA=' ) ) )
 ooOOoooooo = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( iiI )
 for I1Ii1iI1 , oOo0 , II1I in ooOOoooooo :
  IiI1iiiIii ( '[COLORgreen]' + II1I + '[/COLOR]' , I1Ii1iI1 , 222 , oOo0 )
  if 6 - 6: o00O0oo - o0oO0 * OoOO0ooOOoo0O . oO0o0ooO0 / O0 * o0oO0
def II11iI111i1 ( ) :
 o00o0 = Oo0o0000o0o0 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 II1III1I1I1Ii = o00o0 . lower ( )
 iiI = i1IiiiI1iI ( ( oOo0oooo00o ( 'aHR0cDovL3d3dy5jb3VjaHRyaXBwZXIuY29tL2ZvcnVtMi9wYWdlLnBocD9wYWdlPTM=' ) ) )
 O00 = re . compile ( '<tr>.+?<td width=".+?" align=".+?">.+?<img border=".+?" src="..(.+?)" width=".+?" height=".+?"></td>.+?<td width=".+?" valign=".+?" align=".+?"><font size=".+?">(.+?)</font></td>.+?<td width=".+?">(.+?)</td>' , re . DOTALL ) . findall ( iiI )
 for oOo0 , Oo00OoOo , iIiiiI1IiI1I1 in O00 :
  for o00o0 in Oo00OoOo :
   print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< img >>>>>>>>>>>>>>>>>>>>>>>>>>'
   ii1ii111 = re . compile ( '<a href="(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( iIiiiI1IiI1I1 )
   for I1Ii1iI1 , II1I in ii1ii111 :
    if 'tube' in I1Ii1iI1 :
     pass
    elif 'stage' in I1Ii1iI1 :
     IiI1iiiIii ( '[COLORgreen]' + Oo00OoOo + '   -   ' + II1I + '[/COLOR]' , ( I1Ii1iI1 ) . replace ( '" target="_blank' , '' ) , 10016 , 'http://couchtripper.com/' + oOo0 , )
    elif 'vee' in I1Ii1iI1 :
     pass
     if 33 - 33: ii11ii1ii
def O00O0Ooooo00 ( ) :
 iiI = i1IiiiI1iI ( ( oOo0oooo00o ( 'aHR0cDovL3d3dy5jb3VjaHRyaXBwZXIuY29tL2ZvcnVtMi9wYWdlLnBocD9wYWdlPTM=' ) ) )
 O00 = re . compile ( '<tr>.+?<td width=".+?" align=".+?">.+?<img border=".+?" src="..(.+?)" width=".+?" height=".+?"></td>.+?<td width=".+?" valign=".+?" align=".+?"><font size=".+?">(.+?)</font></td>.+?<td width=".+?">(.+?)</td>' , re . DOTALL ) . findall ( iiI )
 for oOo0 , Oo00OoOo , iIiiiI1IiI1I1 in O00 :
  ii1ii111 = re . compile ( '<a href="(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( iIiiiI1IiI1I1 )
  for I1Ii1iI1 , II1I in ii1ii111 :
   if 'tube' in I1Ii1iI1 :
    pass
   elif 'stage' in I1Ii1iI1 :
    IiI1iiiIii ( '[COLORgreen]' + Oo00OoOo + '   -   ' + II1I + '[/COLOR]' , ( I1Ii1iI1 ) . replace ( '" target="_blank' , '' ) , 10016 , 'http://couchtripper.com/' + oOo0 )
   elif 'vee' in I1Ii1iI1 :
    pass
    if 97 - 97: o0oO0 / O0oO % i1IIi % ii11ii1ii
    if 18 - 18: iIii1I11I1II1 % o0000oOoOoO0o
 xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 95 - 95: o0oO0 + i11iIiiIii * O0oO - i1IIi * O0oO - iIii1I11I1II1
def oo0o0O0Oooooo ( url ) :
 iiI = i1IiiiI1iI ( url )
 print '>>>>>>>>>>>>>>>>>>>>>>>>' + url + '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'
 i11IIIiI1I = re . compile ( "url\[.+?\] = '(.+?)';" ) . findall ( iiI )
 print '>>>>>>>>>>>>>>>>>>>>>>>' + ( str ( i11IIIiI1I ) ) + '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
 for url in i11IIIiI1I :
  II1IIiiIiI ( ( url ) . replace ( '[' , '' ) . replace ( ']' , '' ) . replace ( '\'' , '' ) )
  if 69 - 69: O0
  if 85 - 85: o0oO0 / O0
  if 18 - 18: OOooOOo % O0 * ii11ii1ii
  if 62 - 62: O0oO . IIII . OoooooooOO
  if 11 - 11: OoOO0ooOOoo0O / o0000oOoOoO0o
  if 73 - 73: i1IIi / i11iIiiIii
  if 58 - 58: Oo . OoOoOO00 + OoOO - i11iIiiIii / OoOoOO00 / O0
def oOOoOo ( ) :
 if 89 - 89: OoOoOO00 + i1IIi + OoOoOO00
 IiII1II11I ( '[COLOR darkgoldenrod]Open Pandora\'s Box[/COLOR]' , '' , 10029 , 'https://encrypted-tbn1.gstatic.com/images?q=tbn%3AANd9GcTQ9r4TA8yIw9ggxuwsHxWojo6tPVfgTe8QIOxOQwzNR2TavtCi6Q' , OOooO0OOoo , '' )
 IiII1II11I ( '[COLOR darkgoldenrod]Search[/COLOR]' , '' , 10026 , 'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png' , OOooO0OOoo , '' )
 if 54 - 54: IIII + O0 + o0000oOoOoO0o * O0oO - OoOO0ooOOoo0O % OoOO
 I1i1I1II ( 'movies' , 'MAIN' )
 if 13 - 13: o0oO0 / oO0o0ooO0 * Ooo00oOo00o . Ooo00oOo00o * o0oO0
def O00oO ( ) :
 IiII1II11I ( 'Search Pandoras Films' , '' , 10027 , oOOoO0 + 'PANDORASBOX.png' , OOooO0OOoo , '' )
 IiII1II11I ( 'Search Pandoras TV' , '' , 10028 , oOOoO0 + 'PANDORASBOX.png' , OOooO0OOoo , '' )
 if 40 - 40: I1IiI / IIII
 I1i1I1II ( 'movies' , 'MAIN' )
def OOOoO000 ( ) :
 if 57 - 57: OoOoOO00
 o00o0 = Oo0o0000o0o0 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 II1III1I1I1Ii = o00o0 . lower ( )
 oOOOoo = [ 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' ]
 if 15 - 15: i11iIiiIii % OOOo0 * o0000oOoOoO0o / O0oO
 for oooO0o0o0O0 in oOOOoo :
  iii11111I = Base_Pand + oooO0o0o0O0 + CAT
  iiI = i1IiiiI1iI ( iii11111I )
  ooOOoooooo = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( iiI )
  for I1Ii1iI1 , O0i1II1Iiii1I11 , ii11ii11 , IIIIiiIiI , II1I in ooOOoooooo :
   if o00o0 in II1I . lower ( ) :
    i1i1IIiiIIi1I ( II1I , I1Ii1iI1 , 222 , O0i1II1Iiii1I11 , IIIIiiIiI , ii11ii11 )
    if 35 - 35: IIII
    I1i1I1II ( 'movies' , 'MAIN' )
    xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
    if 75 - 75: Oo / ii11ii1ii . IIII * OoOO0ooOOoo0O - OoOoOO00
    if 41 - 41: o00O0oo
def oOOoo0o0OOOO ( ) :
 if 26 - 26: oO0o0ooO0 % iIii1I11I1II1 + OOooOOo
 o00o0 = Oo0o0000o0o0 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 II1III1I1I1Ii = o00o0 . lower ( )
 oOOOoo = [ 'a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' , 'p' , 'q' , 'r' , 's' , 't' , 'u' , 'v' , 'w' , 'x' , 'y' , 'z' ]
 if 67 - 67: OoOO + OoOoOO00 - O0 . OoOO * OoOoOO00 * o0000oOoOoO0o
 for oooO0o0o0O0 in oOOOoo :
  o00OO00O0oOO = Base_Pand + oooO0o0o0O0 + CAT
  iiI = i1IiiiI1iI ( o00OO00O0oOO )
  ooOOoooooo = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( iiI )
  for II1I , ii11ii11 , I1Ii1iI1 , oOo0 , IIIIiiIiI , Ii1iI111 in ooOOoooooo :
   if o00o0 in II1I . lower ( ) :
    IiII1II11I ( II1I , I1Ii1iI1 , Ii1iI111 , oOo0 , IIIIiiIiI , ii11ii11 )
    if 51 - 51: IIII * O0 / OoOoOO00 . o00O0oo % OoOO0ooOOoo0O / OOOo0
    I1i1I1II ( 'movies' , 'MAIN' )
    xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
    if 9 - 9: OOOo0 % OOOo0 % OoOoOO00
    if 30 - 30: IIII + O0oO - IIII . IIII - OoOoOO00 + O0
def oOO0 ( ) :
 if 46 - 46: o00O0oo % I1IiI
 OOOOO0oo0O0O0 = i1IiiiI1iI ( oOo0oooo00o ( 'aHR0cDovL3NlZWR1cmdyZWVkLngxMGhvc3QuY29tL29yaWdpbi9zcG9uZ2VtYWluLnBocA==' ) )
 ooOOoooooo = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( OOOOO0oo0O0O0 )
 for II1I , ii11ii11 , I1Ii1iI1 , oOo0 , IIIIiiIiI , Ii1iI111 in ooOOoooooo :
  IiII1II11I ( II1I , I1Ii1iI1 , Ii1iI111 , oOo0 , IIIIiiIiI , ii11ii11 )
  I1i1I1II ( 'movies' , 'MAIN' )
def ooo0o0O0o ( url ) :
 if 62 - 62: o0oO0 + i11iIiiIii + Oo / i11iIiiIii
 xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
 I1Ii = ( '%s%s' % ( oOOIi1II , url ) )
 IIiIi1iI = i1IiiiI1iI ( url )
 ooOOoooooo = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( IIiIi1iI )
 for url , O0i1II1Iiii1I11 , ii11ii11 , O0Oo00 , II1I in ooOOoooooo :
  i1i1IIiiIIi1I ( II1I , url , 222 , O0i1II1Iiii1I11 , O0Oo00 , ii11ii11 )
  if 41 - 41: iIii1I11I1II1 % o0000oOoOoO0o
  I1i1I1II ( 'movies' , 'MAIN' )
  if 59 - 59: OoOO0ooOOoo0O + i11iIiiIii
  xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 88 - 88: i11iIiiIii - o0oO0
  if 67 - 67: OoOO0ooOOoo0O . Oo + I1IiI - OoooooooOO
def OOOoO ( url ) :
 if 14 - 14: o0000oOoOoO0o . iIii1I11I1II1 . OoooooooOO . OoOoOO00 / OOooOOo
 OOOOO0oo0O0O0 = i1IiiiI1iI ( url )
 ooOOoooooo = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( OOOOO0oo0O0O0 )
 for II1I , ii11ii11 , url , oOo0 , IIIIiiIiI , Ii1iI111 in ooOOoooooo :
  IiII1II11I ( II1I , url , Ii1iI111 , oOo0 , IIIIiiIiI , ii11ii11 )
  if 21 - 21: i11iIiiIii / i1IIi + OOOo0 * OoOO0ooOOoo0O . O0oO
  I1i1I1II ( 'movies' , 'MAIN' )
  if 84 - 84: O0 . o0000oOoOoO0o - OoOoOO00 . o0oO0 / OoOoOO00
  if 47 - 47: OoooooooOO
 xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 4 - 4: OOOo0 % o0000oOoOoO0o
def i1i1IIiiIIi1I ( name , url , mode , iconimage , fanart , description ) :
 if 10 - 10: IIII . OoooooooOO - Ooo00oOo00o + IIII - O0
 o0oO00 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 O0o = True
 oO00oO = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 oO00oO . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 oO00oO . setProperty ( "Fanart_Image" , fanart )
 O0o = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = o0oO00 , listitem = oO00oO , isFolder = False )
 return O0o
 if 36 - 36: OoOO0ooOOoo0O
def IiII1II11I ( name , url , mode , iconimage , fanart , description ) :
 if 84 - 84: O0oO . Ooo00oOo00o . OoOoOO00 . o0000oOoOoO0o / o00O0oo % ii11ii1ii
 o0oO00 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 O0o = True
 oO00oO = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 oO00oO . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 oO00oO . setProperty ( "Fanart_Image" , fanart )
 O0o = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = o0oO00 , listitem = oO00oO , isFolder = True )
 return O0o
if 57 - 57: OOOo0 % o0000oOoOoO0o - OoOO0ooOOoo0O . OOOo0 / Oo % oO0o0ooO0
if 56 - 56: OoOO . oO0o0ooO0 . IIII * I1IiI . o0oO0 / O0
if 23 - 23: i1IIi + oO0o0ooO0 + IIII + Ooo00oOo00o
if 12 - 12: iIii1I11I1II1 - ii11ii1ii + i11iIiiIii
if 10 - 10: OOOo0 - i1IIi - o0oO0 % Oo
if 6 - 6: ii11ii1ii + OoOO
if 48 - 48: iIii1I11I1II1 % i1IIi % oO0o0ooO0 + o0oO0
if 30 - 30: i11iIiiIii % iIii1I11I1II1 . o0000oOoOoO0o % iIii1I11I1II1
if 62 - 62: Oo * I1IiI
if 79 - 79: Ooo00oOo00o . oO0o0ooO0 * o00O0oo - OoOO0ooOOoo0O + o0oO0
if 14 - 14: i11iIiiIii - oO0o0ooO0 * I1IiI
if 51 - 51: ii11ii1ii / iIii1I11I1II1 % OoOO + OOooOOo * o0oO0 + O0oO
if 77 - 77: o0oO0 * I1IiI
if 14 - 14: o0000oOoOoO0o % o0000oOoOoO0o / IIII
if 72 - 72: i1IIi - OoOoOO00 - OoOO0ooOOoo0O + OoOO0ooOOoo0O * OOooOOo * OoOO0ooOOoo0O
def iII1I1 ( string ) :
 if I11II1i == 'true' :
  xbmc . log ( "[addon.live.GenieTV-%s]: %s" % ( addon_version , string ) )
  if 85 - 85: oO0o0ooO0 * OOooOOo
def ii1iii11i1 ( name , url , iconimage , fanart , mode , playlist = None , regexs = None ) :
 I11Oo00oO0O = [ ]
 try :
  if 96 - 96: ii11ii1ii / OoOoOO00 . o00O0oo - oO0o0ooO0 * o0000oOoOoO0o * OoOO
  name = name . encode ( 'utf-8' , 'ignore' )
 except :
  pass
 if os . path . exists ( iIi1ii1I1 ) == False :
  iII1I1 ( 'Making Favorites File' )
  I11Oo00oO0O . append ( ( name , url , iconimage , fanart , mode , playlist , regexs ) )
  oOOOOoOO0o = open ( iIi1ii1I1 , "w" )
  oOOOOoOO0o . write ( json . dumps ( I11Oo00oO0O ) )
  oOOOOoOO0o . close ( )
 else :
  iII1I1 ( 'Appending Favorites' )
  oOOOOoOO0o = open ( iIi1ii1I1 ) . read ( )
  O00oo0ooO = json . loads ( oOOOOoOO0o )
  O00oo0ooO . append ( ( name , url , iconimage , fanart , mode ) )
  i1II1 = open ( iIi1ii1I1 , "w" )
  i1II1 . write ( json . dumps ( O00oo0ooO ) )
  i1II1 . close ( )
  if 38 - 38: iIii1I11I1II1 - OoOoOO00 - OOOo0
  if 71 - 71: OoooooooOO
def iIIIII1iiiiII ( ) :
 oooO = json . loads ( open ( iIi1ii1I1 ) . read ( ) )
 I111i1I1 = len ( oooO )
 for O0o00OOo00O0O in oooO :
  II1I = O0o00OOo00O0O [ 0 ]
  I1Ii1iI1 = O0o00OOo00O0O [ 1 ]
  O0i1II1Iiii1I11 = O0o00OOo00O0O [ 2 ]
  try :
   II1i = O0o00OOo00O0O [ 3 ]
   if II1i == None :
    raise
  except :
   if o0oOoO00o . getSetting ( 'use_thumb' ) == "true" :
    II1i = O0i1II1Iiii1I11
   else :
    II1i = IIIIiiIiI
  try : OoOOoO000O00oO = O0o00OOo00O0O [ 5 ]
  except : OoOOoO000O00oO = None
  try : i1OoOO = O0o00OOo00O0O [ 6 ]
  except : i1OoOO = None
  if 44 - 44: OoOO0ooOOoo0O
  if O0o00OOo00O0O [ 4 ] == 0 :
   ooooooO0oo ( II1I , I1Ii1iI1 , '' , O0i1II1Iiii1I11 , IIIIiiIiI , '' , 'fav' )
  else :
   ooooooO0oo ( II1I , I1Ii1iI1 , O0o00OOo00O0O [ 4 ] , O0i1II1Iiii1I11 , IIIIiiIiI , '' , 'fav' )
   if 54 - 54: o00O0oo - o0000oOoOoO0o - O0oO . iIii1I11I1II1
def o0O ( name ) :
 O00oo0ooO = json . loads ( open ( iIi1ii1I1 ) . read ( ) )
 for IIiI1I1 in range ( len ( O00oo0ooO ) ) :
  if O00oo0ooO [ IIiI1I1 ] [ 0 ] == name :
   del O00oo0ooO [ IIiI1I1 ]
   i1II1 = open ( iIi1ii1I1 , "w" )
   i1II1 . write ( json . dumps ( O00oo0ooO ) )
   i1II1 . close ( )
   break
 xbmc . executebuiltin ( "XBMC.Container.Refresh" )
 if 15 - 15: o00O0oo * Oo % ii11ii1ii * iIii1I11I1II1 - i11iIiiIii
 if 60 - 60: OOOo0 * O0oO % Ooo00oOo00o + OoOO
 if 52 - 52: i1IIi
def o000 ( ) :
 if 94 - 94: OOooOOo + O0 / o0000oOoOoO0o . OOOo0 + OoOO0ooOOoo0O . iIii1I11I1II1
 ooooooO0oo ( '[COLORgreen]Recent Episodes[/COLOR]' , '' , 10019 , oOOoO0 + 'dtv.png' , OOooO0OOoo , '' )
 ooooooO0oo ( '[COLORgreen]Genres[/COLOR]' , '' , 10020 , oOOoO0 + 'dtv.png' , OOooO0OOoo , '' )
 ooooooO0oo ( '[COLORgreen]Search[/COLOR]' , '' , 10021 , oOOoO0 + 'dtv.png' , OOooO0OOoo , '' )
 if 62 - 62: I1IiI / OOOo0 - ii11ii1ii - OOOo0 + i11iIiiIii + i1IIi
def I1i11II ( ) :
 if 31 - 31: OoOO / IIII * OOooOOo . OoOoOO00
 OOOOO0oo0O0O0 = cloudflare . source ( oOo0oooo00o ( 'aHR0cDovL2RpemlsYWIuY29t' ) )
 ooOOoooooo = re . compile ( '<li id=".+?">.+?<a href="(.+?)">.+?<img width="40" height="40" src="(.+?)" alt=""/>.+?<span class="title">\n(.+?)</span>.+?<span class="alt-title">\n(.+?)</span>.+?</a>.+?</li>' , re . DOTALL ) . findall ( OOOOO0oo0O0O0 )
 for I1Ii1iI1 , oOo0 , II1I , oooOO0OO0O in ooOOoooooo :
  ooooooO0oo ( II1I + '  -  ' + ( oooOO0OO0O ) . replace ( 'sezon' , 'Season' ) . replace ( 'bölüm' , 'Episode' ) , I1Ii1iI1 , 10023 , oOOoO0 + 'dtv.png' , OOooO0OOoo , '' )
  if 78 - 78: o00O0oo / OoOoOO00 % I1IiI
  if 52 - 52: OoOO0ooOOoo0O - oO0o0ooO0 * OoOO
  if 17 - 17: OoooooooOO + OoOO0ooOOoo0O * o0000oOoOoO0o * I1IiI
def iiIii1I ( ) :
 if 47 - 47: o0oO0 . o0000oOoOoO0o / OOooOOo
 ooooooO0oo ( '[COLORgreen]Action[/COLOR]' , 'Aksiyon' , 10024 , oOOoO0 + 'dtv.png' , OOooO0OOoo , '' )
 ooooooO0oo ( '[COLORgreen]Adventure[/COLOR]' , 'Macera' , 10024 , oOOoO0 + 'dtv.png' , OOooO0OOoo , '' )
 ooooooO0oo ( '[COLORgreen]Animation[/COLOR]' , 'Animasyon' , 10024 , oOOoO0 + 'dtv.png' , OOooO0OOoo , '' )
 ooooooO0oo ( '[COLORgreen]Anime[/COLOR]' , 'Anime' , 10024 , oOOoO0 + 'dtv.png' , OOooO0OOoo , '' )
 ooooooO0oo ( '[COLORgreen]Biography[/COLOR]' , 'Biyografi' , 10024 , oOOoO0 + 'dtv.png' , OOooO0OOoo , '' )
 ooooooO0oo ( '[COLORgreen]Comedy[/COLOR]' , 'Komedi' , 10024 , oOOoO0 + 'dtv.png' , OOooO0OOoo , '' )
 ooooooO0oo ( '[COLORgreen]Crime[/COLOR]' , 'Su%C3%A7' , 10024 , oOOoO0 + 'dtv.png' , OOooO0OOoo , '' )
 ooooooO0oo ( '[COLORgreen]Documentary[/COLOR]' , 'Belgesel' , 10024 , oOOoO0 + 'dtv.png' , OOooO0OOoo , '' )
 ooooooO0oo ( '[COLORgreen]Drama[/COLOR]' , 'Dram' , 10024 , oOOoO0 + 'dtv.png' , OOooO0OOoo , '' )
 ooooooO0oo ( '[COLORgreen]Family[/COLOR]' , 'Aile' , 10024 , oOOoO0 + 'dtv.png' , OOooO0OOoo , '' )
 ooooooO0oo ( '[COLORgreen]Fantasy[/COLOR]' , 'Fantastik' , 10024 , oOOoO0 + 'dtv.png' , OOooO0OOoo , '' )
 ooooooO0oo ( '[COLORgreen]History[/COLOR]' , 'Tarih' , 10024 , oOOoO0 + 'dtv.png' , OOooO0OOoo , '' )
 ooooooO0oo ( '[COLORgreen]Horror[/COLOR]' , 'Korku' , 10024 , oOOoO0 + 'dtv.png' , OOooO0OOoo , '' )
 ooooooO0oo ( '[COLORgreen]Mini-Series[/COLOR]' , 'Mini%20Dizi' , 10024 , oOOoO0 + 'dtv.png' , OOooO0OOoo , '' )
 ooooooO0oo ( '[COLORgreen]Musical[/COLOR]' , 'M%C3%BCzikal' , 10024 , oOOoO0 + 'dtv.png' , OOooO0OOoo , '' )
 ooooooO0oo ( '[COLORgreen]Mystery[/COLOR]' , 'Gizem' , 10024 , oOOoO0 + 'dtv.png' , OOooO0OOoo , '' )
 ooooooO0oo ( '[COLORgreen]Romance[/COLOR]' , 'Romantik' , 10024 , oOOoO0 + 'dtv.png' , OOooO0OOoo , '' )
 ooooooO0oo ( '[COLORgreen]Science Fiction[/COLOR]' , 'Bilim%20Kurgu' , 10024 , oOOoO0 + 'dtv.png' , OOooO0OOoo , '' )
 ooooooO0oo ( '[COLORgreen]Sport[/COLOR]' , 'Spor' , 10024 , oOOoO0 + 'dtv.png' , OOooO0OOoo , '' )
 ooooooO0oo ( '[COLORgreen]Thriller[/COLOR]' , 'Gerilim' , 10024 , oOOoO0 + 'dtv.png' , OOooO0OOoo , '' )
 ooooooO0oo ( '[COLORgreen]War[/COLOR]' , 'Sava%C5%9F' , 10024 , oOOoO0 + 'dtv.png' , OOooO0OOoo , '' )
 ooooooO0oo ( '[COLORgreen]Western[/COLOR]' , 'Tarih' , 10024 , oOOoO0 + 'dtv.png' , OOooO0OOoo , '' )
 ooooooO0oo ( '[COLORgreen]Youth[/COLOR]' , 'Gen%C3%A7lik' , 10024 , oOOoO0 + 'dtv.png' , OOooO0OOoo , '' )
 if 83 - 83: OOooOOo / OoOO0ooOOoo0O / OoOO0ooOOoo0O + OOooOOo * O0oO + OOooOOo
def IIIIiii ( url ) :
 oO0o = 'http://dizilab.com/arsiv?limit=100&tur=' + url + '&orderby=&ulke=&order=&yil=&dizi_adi='
 iiI = cloudflare . source ( oO0o )
 ooOOoooooo = re . compile ( '<div class="tv-series-single">.+?<a href="(.+?)" class="film-image">.+?<img src="(.+?)" alt=""/>.+?<span class="position">.+?</span>\n(.+?)</a>' , re . DOTALL ) . findall ( iiI )
 for url , oOo0 , II1I in ooOOoooooo :
  ooooooO0oo ( '[COLORgreen]' + II1I + '[/COLOR]' , url , 10022 , oOOoO0 + 'dtv.png' , OOooO0OOoo , '' )
  if 24 - 24: I1IiI % i1IIi + oO0o0ooO0 . i11iIiiIii . ii11ii1ii
  if 17 - 17: ii11ii1ii . OoOoOO00 . o0oO0 / ii11ii1ii
  if 57 - 57: o0000oOoOoO0o
  if 67 - 67: Ooo00oOo00o . o0oO0
def oO00oOo0OOO ( ) :
 if 23 - 23: i1IIi . OOooOOo * Ooo00oOo00o
 o00o0 = Oo0o0000o0o0 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 II1III1I1I1Ii = o00o0 . lower ( )
 I1Ii1iI1 = ( oOo0oooo00o ( 'aHR0cDovL2RpemlsYWIuY29tL2Fyc2l2P2xpbWl0PSZ0dXI9Jm9yZGVyYnk9JnVsa2U9Jm9yZGVyPSZ5aWw9JmRpemlfYWRpPQ==' ) ) + ( o00o0 ) . replace ( ' ' , '+' )
 iiI = cloudflare . source ( I1Ii1iI1 )
 ooOOoooooo = re . compile ( '<a href="(.+?)" class="film-image">\n<img src="(.+?)" alt=""/>\n</a>\n<div class="tss-detail">\n<a class="title" style="" href=".+?">\n<span class="position">.+?</span>\n(.+?)</a>' ) . findall ( iiI )
 for I1Ii1iI1 , oOo0 , II1I in ooOOoooooo :
  if o00o0 in II1I . lower ( ) :
   ooooooO0oo ( '[COLORgreen]' + II1I + '[/COLOR]' , I1Ii1iI1 , 10022 , oOOoO0 + 'dtv.png' )
   if 15 - 15: I1IiI
   if 62 - 62: o00O0oo
   if 51 - 51: I1IiI
def I11IIIiIi11 ( url ) :
 iiI = cloudflare . source ( url )
 ooOOoooooo = re . compile ( '<a class="season" href="(.+?)">\n(.+?)\n</a>.+?<a class="episode" href=".+?">\n(.+?)\n</a>.+?<a class="episode-name" href=".+?">\n(.+?)</a>' , re . DOTALL ) . findall ( iiI )
 for O0o0OO0000ooo , I11iiIi1i1 , i1IiiI1iIi , II1I in ooOOoooooo :
  oOOo00O0OOOo = ( i1IiiI1iIi ) . replace ( 'Sezon' , '' ) . replace ( 'bölüm' , '' ) . replace ( 'Bölüm' , '' ) . replace ( 'BÃ¶lÃ¼m' , '' ) . replace ( '.' , '' )
  i11I1I1iiI = ( I11iiIi1i1 ) . replace ( 'bölüm' , '' ) . replace ( 'Sezon' , '' ) . replace ( 'Bölüm' , '' ) . replace ( 'BÃ¶lÃ¼m' , '' ) . replace ( '.' , '' )
  I1i1iii1Ii = 'Season ' + i11I1I1iiI + 'Episode ' + oOOo00O0OOOo + II1I
  iI ( I1i1iii1Ii , O0o0OO0000ooo )
  if 99 - 99: o0000oOoOoO0o - O0oO - OoOO % Ooo00oOo00o
  xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 21 - 21: OoOoOO00 % ii11ii1ii . i1IIi - OoooooooOO
  if 4 - 4: OoooooooOO . o0oO0
def iI ( name , url ) :
 O0o0OO0000ooo = url
 oOO0oo = name
 II1iIi1IiIii = cloudflare . source ( O0o0OO0000ooo )
 o0OO0o0o00o = re . compile ( 'file: "(.+?)",.+?label: "(.+?)",' , re . DOTALL ) . findall ( II1iIi1IiIii )
 for i11IIIiI1I , Iiiiii111i1ii in o0OO0o0o00o :
  IiI1iiiIii ( '[COLORgreen]' + oOO0oo + Iiiiii111i1ii + '[/COLOR]' , i11IIIiI1I , 10012 , oOOoO0 + 'dtv.png' )
  if 30 - 30: o0oO0 % oO0o0ooO0 * OoOO0ooOOoo0O - ii11ii1ii * o00O0oo % o0oO0
 xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 46 - 46: i11iIiiIii - O0 . OoOO
 if 100 - 100: OOOo0 / OOooOOo * oO0o0ooO0 . O0 / OoOO0ooOOoo0O
def oOO0o000Oo00o ( ) :
 if 21 - 21: OoooooooOO - iIii1I11I1II1
 if 93 - 93: OoOO - OOooOOo % I1IiI . I1IiI - o0oO0
 if 90 - 90: o0oO0 + OoOoOO00 * ii11ii1ii / o00O0oo . OOooOOo + OOooOOo
 if 40 - 40: o0oO0 / I1IiI % i11iIiiIii % ii11ii1ii / OOOo0
 if 62 - 62: i1IIi - I1IiI
 if 62 - 62: i1IIi + Oo % IIII
 if 28 - 28: ii11ii1ii . i1IIi
 if 10 - 10: Ooo00oOo00o / Oo
 if 15 - 15: oO0o0ooO0 . I1IiI / oO0o0ooO0 * o0000oOoOoO0o - OOOo0 % ii11ii1ii
 if 57 - 57: O0 % I1IiI % OoOO
 if 45 - 45: ii11ii1ii + OoOoOO00 * i11iIiiIii
 if 13 - 13: OoooooooOO * OoOO - o00O0oo / OoOO0ooOOoo0O + o0000oOoOoO0o + IIII
 if 39 - 39: iIii1I11I1II1 - OoooooooOO
 if 81 - 81: ii11ii1ii - O0 * OoooooooOO
 if 23 - 23: OoOoOO00 / OoOO
 ooooooO0oo ( '[COLORgreen]Newest Episodes Added[/COLOR]' , 'http://www.watchseries.li/latest' , 10046 , oOOoO0 + 'WATCHSERIES.png' , '' , '' )
 ooooooO0oo ( '[COLORgreen]This Week\'s Popular Episodes[/COLOR]' , 'http://www.watchseries.li/new' , 10042 , oOOoO0 + 'WATCHSERIES.png' , '' , '' )
 ooooooO0oo ( '[COLORgreen]Search Program[/COLOR]' , '' , 10043 , oOOoO0 + 'WATCHSERIES.png' , '' , '' )
 if 28 - 28: Oo * o0oO0 - Ooo00oOo00o
 if 19 - 19: o0000oOoOoO0o
def Ooooo0OoO0 ( url ) :
 iiI = i1IiiiI1iI ( url )
 I11ii1i1 = re . compile ( '<ul class="pagination" style="line-height: 3;">(.+?)</ul>' , re . DOTALL ) . findall ( iiI )
 ooOOoooooo = re . compile ( '<li><a href="/letters/(.+?)">(.+?)</a></li>' ) . findall ( str ( I11ii1i1 ) )
 for url , II1I in ooOOoooooo :
  ooooooO0oo ( '[COLORgreen]' + II1I + '[/COLOR]' , 'http://watchseries.li/letters/' + url , 10049 , oOOoO0 + 'WATCHSERIES.png' , '' , '' )
  if 9 - 9: OoOO0ooOOoo0O . IIII
def iIi1i ( url ) :
 iiI = i1IiiiI1iI ( url )
 ooOOoooooo = re . compile ( '<a href="(.+?)" class="sr-header">(.+?)</a>' ) . findall ( iiI )
 for url , II1I in ooOOoooooo :
  ooooooO0oo ( '[COLORgreen]' + II1I + '[/COLOR]' , 'http://watchseries.li/' + url , 10049 , oOOoO0 + 'WATCHSERIES.png' , '' , '' )
  if 67 - 67: I1IiI / OOooOOo * Ooo00oOo00o / OoOO0ooOOoo0O * ii11ii1ii / OoOO
def OOoOO0OO ( url ) :
 iiI = i1IiiiI1iI ( url )
 ooOOoooooo = re . compile ( '<li class="col-md-6 col-xs-12 list-movies-li"><a href="(.+?)" title=".+?">(.+?)<span class="epnum">.+?</span></a></li>' , re . DOTALL ) . findall ( iiI )
 o0OO0o0o00o = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="(.+?)">Next</a></li></ul>' , re . DOTALL ) . findall ( iiI )
 for url , II1I in ooOOoooooo :
  ooooooO0oo ( '[COLORgreen]' + ( II1I ) . replace ( '&nbsp;' , ' ' ) . replace ( '&amp;' , '&' ) . replace ( '&#039;' , '\'' ) + '[/COLOR]' , 'http://www.watchseries.li' + url , 10044 , oOOoO0 + 'WATCHSERIES.png' , '' , '' )
 for url in o0OO0o0o00o :
  ooooooO0oo ( '[COLORgreen]' + 'NEXT' + '[/COLOR]' , 'http://www.watchseries.li' + url , 10049 , '' , '' , '' )
  if 26 - 26: oO0o0ooO0 . oO0o0ooO0
  if 35 - 35: O0oO . I1IiI * i11iIiiIii
def iiII ( ) :
 o00o0 = Oo0o0000o0o0 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 o0Oii1111i = 'http://www.watchseries.li/search/' + o00o0 . replace ( ' ' , '%20' )
 iiI = i1IiiiI1iI ( o0Oii1111i )
 ooOOoooooo = re . compile ( '<img src="(.+?)".+?<a href="(.+?)" title=".+?"><b>(.+?)</b>' , re . DOTALL ) . findall ( iiI )
 for oOo0 , I1Ii1iI1 , II1I in ooOOoooooo :
  if 'watch online' in II1I :
   pass
  else :
   print I1Ii1iI1
   ooooooO0oo ( '[COLORgreen]' + II1I + '[/COLOR]' , 'http://www.watchseries.li' + I1Ii1iI1 , 10044 , oOo0 , '' , '' )
   if 75 - 75: IIII + OoOoOO00 / OoOO - OoOO / OoooooooOO
   xbmcplugin . setContent ( O00o0OO , 'movies' )
   if 2 - 2: OOooOOo
def i11ii ( url ) :
 iiI = i1IiiiI1iI ( url )
 ooOOoooooo = re . compile ( '<img src="(.+?)".+?<div class="block-left-home-inside-text">.+?<a href="(.+?)" title=".+?"><b>(.+?)</b> <br>.+?<span class=".+?">(.+?)</span></a><br>(.+?)<br>' , re . DOTALL ) . findall ( iiI )
 for oOo0 , url , II1I , i1IiiI1iIi , ii11ii11 in ooOOoooooo :
  i11I1 = ( II1I ) . replace ( '&nbsp;' , ' ' ) . replace ( '&amp;' , '&' ) . replace ( '&#039;' , '\'' ) + ' - ' + ( i1IiiI1iIi ) . replace ( '&amp;' , '&' ) . replace ( '&#039;' , '\'' )
  ooooooO0oo ( '[COLORgreen]' + i11I1 + '[/COLOR]' , 'http://www.watchseries.li' + url , 10045 , oOo0 , '' , ii11ii11 )
  if 34 - 34: O0 * O0 % OoooooooOO + oO0o0ooO0 * iIii1I11I1II1 % o00O0oo
def I1iI1I1 ( url ) :
 iiI = i1IiiiI1iI ( url )
 ooOOoooooo = re . compile ( '<li class="col-md-6 col-xs-12 list-movies-li"><a href="(.+?)" title=".+?">(.+?)<span class="epnum">.+?</span></a></li>' , re . DOTALL ) . findall ( iiI )
 o0OO0o0o00o = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="(.+?)">Next</a></li></ul>' , re . DOTALL ) . findall ( iiI )
 for url , II1I in ooOOoooooo :
  i11I1 = ( II1I ) . replace ( '&nbsp;' , ' ' ) . replace ( '&amp;' , '&' ) . replace ( '&#039;' , '\'' )
  ooooooO0oo ( '[COLORgreen]' + i11I1 + '[/COLOR]' , 'http://www.watchseries.li' + url , 10045 , oOOoO0 + 'WATCHSERIES.png' , '' , '' )
 for url in o0OO0o0o00o :
  ooooooO0oo ( '[COLORgreen]' + 'NEXT' + '[/COLOR]' , 'http://www.watchseries.li' + url , 10046 , '' , '' , '' )
  if 48 - 48: OOOo0 / i11iIiiIii - OOooOOo * OoOO / OoooooooOO
def OoOo ( url ) :
 iiI = i1IiiiI1iI ( url )
 ooOOoooooo = re . compile ( '<div class="mask">.+?<a href="(.+?)" title="(.+?)">.+?<img src="(.+?)"' , re . DOTALL ) . findall ( iiI )
 o0OO0o0o00o = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="(.+?)">Next</a></li></ul>' , re . DOTALL ) . findall ( iiI )
 for url , II1I , oOo0 in ooOOoooooo :
  ooooooO0oo ( '[COLORgreen]' + ( II1I ) . replace ( '&nbsp;' , ' ' ) . replace ( '&amp;' , '&' ) . replace ( '&#039;' , '\'' ) + '[/COLOR]' , 'http://www.watchseries.li' + url , 10044 , oOo0 , '' , '' )
 for url in o0OO0o0o00o :
  ooooooO0oo ( '[COLORgreen]' + 'NEXT' + '[/COLOR]' , 'http://www.watchseries.li' + url , 10041 , '' , '' , '' )
  if 17 - 17: o00O0oo . i11iIiiIii
def IIIiiiI ( url ) :
 iiI = i1IiiiI1iI ( url )
 I11ii1i1 = re . compile ( '<div class="col-md-6 col-xs-12".+?<a href=".+?" itemprop="url"><span itemprop="name">(.+?)</span>(.+?)</ul>' , re . DOTALL ) . findall ( iiI )
 for I11iiIi1i1 , O00 in I11ii1i1 :
  ooOOoooooo = re . compile ( '<li itemprop="episode".+?<meta itemprop="url" content="(.+?)">.+?<span class="" itemprop="name">\n(.+?)\n' , re . DOTALL ) . findall ( str ( O00 ) )
  for url , II1I in ooOOoooooo :
   i11I1 = ( I11iiIi1i1 ) . replace ( '  ' , '' ) + ' ' + ( II1I ) . replace ( '&nbsp;' , ' ' ) . replace ( '&#039;' , '\'' ) . replace ( '  ' , '' )
   ooooooO0oo ( '[COLORgreen]' + i11I1 + '[/COLOR]' , 'http://www.watchseries.li' + url , 10045 , oOOoO0 + 'WATCHSERIES.png' , '' , '' )
 o0OO0o0o00o = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="(.+?)">Next</a></li></ul>' , re . DOTALL ) . findall ( iiI )
 for url in o0OO0o0o00o :
  ooooooO0oo ( '[COLORgreen]' + 'NEXT' + '[/COLOR]' , 'http://www.watchseries.li' + url , 10044 , '' , '' , '' )
  if 94 - 94: O0 - o0000oOoOoO0o - iIii1I11I1II1 % o0oO0 / o00O0oo % oO0o0ooO0
  if 44 - 44: Oo % iIii1I11I1II1
class oo0ooO0 ( ) :
 if 28 - 28: ii11ii1ii * OoooooooOO . OoOoOO00 / i11iIiiIii + OoOO
 List = [ ]
 source_list = [ ]
 def __init__ ( self , name ) :
  if 38 - 38: IIII . o00O0oo
  i11I1 = name
  self . Get_Sources ( I1Ii1iI1 , i11I1 )
  if 24 - 24: OOooOOo - OOooOOo + ii11ii1ii + OOOo0 - OoOO
  if 12 - 12: oO0o0ooO0 . IIII . I1IiI / O0
 def Get_Sources ( self , URL , season_name ) :
  i1111 = xbmcgui . DialogProgress ( )
  iiI = i1IiiiI1iI ( URL )
  ooOOoooooo = re . compile ( '<td>.+?<a href="/link/(.+?)".+?height="16px">(.+?)\n' , re . DOTALL ) . findall ( iiI )
  for I1Ii1iI1 , II1I in ooOOoooooo :
   URL = 'http://www.watchseries.li/link/' + I1Ii1iI1
   self . Get_site_link ( URL , season_name )
   if 58 - 58: OOooOOo - OoOoOO00 % OoOO + O0oO . I1IiI / IIII
 def Get_site_link ( self , url , season_name ) :
  iiI = i1IiiiI1iI ( url )
  ooOOoooooo = re . compile ( '<iframe style=.+?" src="(.+?)"' ) . findall ( iiI )
  o0OO0o0o00o = re . compile ( '<IFRAME SRC="(.+?)"' ) . findall ( iiI )
  iIII = re . compile ( '<IFRAME style=".+?" SRC="(.+?)"' ) . findall ( iiI )
  for url in ooOOoooooo :
   self . main ( url , season_name )
  for url in o0OO0o0o00o :
   self . main ( url , season_name )
  for url in iIII :
   self . main ( url , season_name )
   if 8 - 8: ii11ii1ii . Ooo00oOo00o * o0000oOoOoO0o + OoOoOO00 % i11iIiiIii
 def main ( self , url , season_name ) :
  i1111 . create ( "[COLORwhite]Origin[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
  if 'daclips.in' in url :
   i1i1IiIiIi1Ii = 'DACLIPS'
   if i1i1IiIiIi1Ii in oo0ooO0 . source_list :
    pass
   else :
    self . daclips ( url , season_name , i1i1IiIiIi1Ii )
    i1111 . update ( 0 , "" , "Getting Daclips Links" )
  else :
   if 'filehoot.com' in url :
    i1i1IiIiIi1Ii = 'FILEHOOT'
    if i1i1IiIiIi1Ii in oo0ooO0 . source_list :
     pass
    else :
     i1111 . update ( 0 , "" , "Getting Filehoot Links" )
     self . filehoot ( url , season_name , i1i1IiIiIi1Ii )
   else :
    if 'thevideo.me' in url :
     i1i1IiIiIi1Ii = 'THEVIDEO'
     if i1i1IiIiIi1Ii in oo0ooO0 . source_list :
      pass
     else :
      self . thevideo ( url , season_name , i1i1IiIiIi1Ii )
      i1111 . update ( 0 , "" , "Getting Thevideo Links" )
    else :
     if 'allmyvideos.net' in url :
      i1i1IiIiIi1Ii = 'ALLMYVIDEOS'
      if i1i1IiIiIi1Ii in oo0ooO0 . source_list :
       pass
      else :
       self . allmyvid ( url , season_name , i1i1IiIiIi1Ii )
       i1111 . update ( 0 , "" , "Getting Allmyvideo Links" )
     else :
      if 'vidspot.net' in url :
       i1i1IiIiIi1Ii = 'VIDSPOT'
       if i1i1IiIiIi1Ii in oo0ooO0 . source_list :
        pass
       else :
        self . vidspot ( url , season_name , i1i1IiIiIi1Ii )
        i1111 . update ( 0 , "" , "Getting Vidspot Links" )
      else :
       if 'vodlocker' in url :
        i1i1IiIiIi1Ii = 'VODLOCKER'
        if i1i1IiIiIi1Ii in oo0ooO0 . source_list :
         pass
        else :
         self . vodlocker ( url , season_name , i1i1IiIiIi1Ii )
         i1111 . update ( 0 , "" , "Getting Vodlocker Links" )
         if 64 - 64: OoOO0ooOOoo0O + OoooooooOO * OoooooooOO
         if 41 - 41: o0oO0 . Oo + OOOo0
 def allmyvid ( self , url , season_name , source_name ) :
  iiI = i1IiiiI1iI ( url )
  ooOOoooooo = re . compile ( '"file" : "(.+?)",\n.+?"default" : .+?,\n.+?"label" : "(.+?)"' , re . DOTALL ) . findall ( iiI )
  for o0O0OO , II1I in ooOOoooooo :
   self . Printer ( o0O0OO , season_name , source_name )
   if 22 - 22: OoOoOO00 * Ooo00oOo00o * o0000oOoOoO0o + ii11ii1ii * OOooOOo
 def vidspot ( self , url , season_name , source_name ) :
  iiI = i1IiiiI1iI ( url )
  ooOOoooooo = re . compile ( '"file" : "(.+?)",\n.+?"default" : .+?,\n.+?"label" : "(.+?)"' ) . findall ( iiI )
  for o0O0OO , II1I in ooOOoooooo :
   self . Printer ( o0O0OO , season_name , source_name )
   if 100 - 100: i1IIi / IIII
 def thevideo ( self , url , season_name , source_name ) :
  iiI = i1IiiiI1iI ( url )
  ooOOoooooo = re . compile ( "{ label: '.+?', file: '(.+?)' }" ) . findall ( iiI )
  for o0O0OO in ooOOoooooo :
   self . Printer ( o0O0OO , season_name , source_name )
   if 3 - 3: OoOoOO00 % ii11ii1ii - OoooooooOO * Oo . iIii1I11I1II1
 def vodlocker ( self , url , season_name , source_name ) :
  iiI = i1IiiiI1iI ( url )
  ooOOoooooo = re . compile ( 'file: "(.+?)",.+?skin' , re . DOTALL ) . findall ( iiI )
  for o0O0OO in ooOOoooooo :
   self . Printer ( o0O0OO , season_name , source_name )
   if 37 - 37: oO0o0ooO0 / Oo . o0000oOoOoO0o * o0000oOoOoO0o
 def daclips ( self , url , season_name , source_name ) :
  iiI = i1IiiiI1iI ( url )
  ooOOoooooo = re . compile ( '{ file: "(.+?)", type:"video" }' ) . findall ( iiI )
  for o0O0OO in ooOOoooooo :
   self . Printer ( o0O0OO , season_name , source_name )
   if 80 - 80: OoOO0ooOOoo0O % ii11ii1ii
 def filehoot ( self , url , season_name , source_name ) :
  iiI = i1IiiiI1iI ( url )
  ooOOoooooo = re . compile ( 'file: "(.+?)",.+?skin' , re . DOTALL ) . findall ( iiI )
  for o0O0OO in ooOOoooooo :
   self . Printer ( o0O0OO , season_name , source_name )
   if 91 - 91: o0000oOoOoO0o / O0 - o00O0oo . OOOo0
 def Printer ( self , Link , season_name , source_name ) :
  if 82 - 82: IIII * OoOO0ooOOoo0O / OoOO
  if Link in oo0ooO0 . List :
   pass
  elif source_name in oo0ooO0 . source_list :
   pass
  else :
   IiI1iiiIii ( '[COLORgreen]' + source_name + '[/COLOR]' , Link , 10012 , oOOoO0 + 'WATCHSERIES.png' )
   i1111 . update ( 100 , "" , "Got Source" )
   oo0ooO0 . List . append ( Link )
   oo0ooO0 . source_list . append ( source_name )
   if 2 - 2: OOOo0 + OOooOOo . OOooOOo . O0 / o0000oOoOoO0o
   xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
if 40 - 40: OOooOOo - OoOoOO00 / Oo
if 14 - 14: ii11ii1ii
if 5 - 5: OOooOOo . iIii1I11I1II1 % iIii1I11I1II1
if 56 - 56: OoooooooOO - o0000oOoOoO0o - i1IIi
if 8 - 8: O0oO / OoOO0ooOOoo0O . OOOo0 + ii11ii1ii / i11iIiiIii
if 31 - 31: o0oO0 - iIii1I11I1II1 + oO0o0ooO0 . Oo / IIII % iIii1I11I1II1
if 6 - 6: IIII * i11iIiiIii % iIii1I11I1II1 % i11iIiiIii + OOooOOo / i1IIi
if 53 - 53: o0000oOoOoO0o + iIii1I11I1II1
if 70 - 70: ii11ii1ii
if 67 - 67: OoooooooOO
if 29 - 29: O0 - i11iIiiIii - OoOoOO00 + OoOO0ooOOoo0O * IIII
if 2 - 2: i1IIi - o0oO0 + OOOo0 . OOooOOo * OOooOOo / I1IiI
if 93 - 93: i1IIi
if 53 - 53: OoooooooOO + Oo + OoOO
if 24 - 24: oO0o0ooO0 - IIII - oO0o0ooO0 * ii11ii1ii . OoooooooOO / IIII
if 66 - 66: Oo
if 97 - 97: i1IIi - OoooooooOO / O0oO * OOOo0
if 55 - 55: OOooOOo . oO0o0ooO0
if 87 - 87: OOooOOo % iIii1I11I1II1
if 100 - 100: O0oO . OOOo0 * O0oO - OOOo0 . o0000oOoOoO0o * o00O0oo
if 89 - 89: Ooo00oOo00o + IIII * O0oO
if 28 - 28: OoooooooOO . OoOO % ii11ii1ii / i1IIi / OoOO0ooOOoo0O
if 36 - 36: OOooOOo + o0000oOoOoO0o - IIII + iIii1I11I1II1 + OoooooooOO
if 4 - 4: OoOoOO00 . o0000oOoOoO0o + o00O0oo * O0oO . o0oO0
if 87 - 87: I1IiI / Ooo00oOo00o / i11iIiiIii
if 74 - 74: OoOO / ii11ii1ii % OOooOOo
if 88 - 88: I1IiI - i11iIiiIii % OOooOOo * o0000oOoOoO0o + ii11ii1ii
if 52 - 52: OoOoOO00 . OOOo0 + I1IiI % Ooo00oOo00o
if 62 - 62: OOooOOo
if 15 - 15: o0000oOoOoO0o + o00O0oo . OoOO0ooOOoo0O * Ooo00oOo00o . I1IiI
if 18 - 18: i1IIi % OoOoOO00 + O0oO % o00O0oo
if 72 - 72: iIii1I11I1II1
if 45 - 45: Oo - OOooOOo % O0oO
if 38 - 38: O0oO % OoOO0ooOOoo0O - OoooooooOO
if 87 - 87: Ooo00oOo00o % OOOo0
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
if 75 - 75: o0000oOoOoO0o / OOooOOo / OoOO0ooOOoo0O / IIII % o0oO0 + OoOoOO00
if 4 - 4: oO0o0ooO0 - Oo - IIII - o0000oOoOoO0o % i11iIiiIii / Ooo00oOo00o
if 50 - 50: o0oO0 + i1IIi
if 31 - 31: o00O0oo
if 78 - 78: i11iIiiIii + OOooOOo + O0oO / OOooOOo % iIii1I11I1II1 % IIII
if 83 - 83: iIii1I11I1II1 % I1IiI % OOooOOo % O0oO . ii11ii1ii % O0
if 47 - 47: OOooOOo
if 66 - 66: OOOo0 - IIII
if 33 - 33: OOOo0 / Ooo00oOo00o
if 12 - 12: OoOoOO00
if 2 - 2: i1IIi - OOOo0 + o0000oOoOoO0o . OoOoOO00
if 25 - 25: OoOO
if 34 - 34: I1IiI . iIii1I11I1II1 % O0
if 43 - 43: ii11ii1ii - oO0o0ooO0
if 70 - 70: oO0o0ooO0 / OoOO0ooOOoo0O % o0oO0 - o00O0oo
if 47 - 47: oO0o0ooO0
if 92 - 92: OoOO0ooOOoo0O + I1IiI % i1IIi
if 23 - 23: O0oO - OoOO0ooOOoo0O + o00O0oo - I1IiI * I1IiI . Oo
if 47 - 47: OoOO % iIii1I11I1II1
if 11 - 11: OOOo0 % o00O0oo - Ooo00oOo00o - OoOO + OOooOOo
if 98 - 98: oO0o0ooO0 + o00O0oo - Ooo00oOo00o
if 79 - 79: OoOO0ooOOoo0O / O0oO . I1IiI - ii11ii1ii
if 47 - 47: OoooooooOO % O0 * oO0o0ooO0 . o00O0oo
if 38 - 38: O0 - IIII % O0oO
if 64 - 64: iIii1I11I1II1
if 15 - 15: ii11ii1ii + OoOO0ooOOoo0O / ii11ii1ii / O0oO
if 31 - 31: o0oO0 + O0 + o0oO0 . iIii1I11I1II1 + Oo / OOooOOo
if 6 - 6: Oo % IIII * o0000oOoOoO0o / OOOo0 + Oo
if 39 - 39: I1IiI - Oo / oO0o0ooO0 * OoooooooOO
if 100 - 100: O0 . o0000oOoOoO0o . Ooo00oOo00o + O0 * OoOO
if 42 - 42: OoOO % OoooooooOO + OOooOOo
if 56 - 56: OoooooooOO + ii11ii1ii - oO0o0ooO0
if 24 - 24: OOooOOo + o0oO0 + o0000oOoOoO0o - iIii1I11I1II1
if 49 - 49: o0000oOoOoO0o . o0oO0 * I1IiI % IIII . O0
if 48 - 48: O0 * o00O0oo - O0 / o00O0oo + I1IiI
if 52 - 52: Ooo00oOo00o % o00O0oo * OoOoOO00
if 4 - 4: o0000oOoOoO0o % O0 - OoooooooOO + o0oO0 . OoOO % OoOoOO00
if 9 - 9: OoOoOO00 * OoOoOO00 . i11iIiiIii * iIii1I11I1II1
if 18 - 18: Ooo00oOo00o . OoOoOO00 % I1IiI % o00O0oo
if 87 - 87: iIii1I11I1II1 . OoooooooOO * I1IiI
if 100 - 100: Ooo00oOo00o / i1IIi - OOOo0 % o00O0oo - iIii1I11I1II1
if 17 - 17: o0000oOoOoO0o / OOooOOo % Oo
if 71 - 71: IIII . O0oO . Ooo00oOo00o
def Oo0O0O00Oo ( ) :
 ooooooO0oo ( '[COLORgreen]Highlights[/COLOR]' , '' , 10008 , oOOoO0 + 'ORIGINFOOTBALL.png' , OOooO0OOoo , '' )
 ooooooO0oo ( '[COLORgreen]Fixtures[/COLOR]' , '' , 10009 , oOOoO0 + 'ORIGINFOOTBALL.png' , OOooO0OOoo , '' )
 if 10 - 10: o00O0oo + o0000oOoOoO0o % OoooooooOO - OOOo0
def o00oooOo ( ) :
 OOOOO0oo0O0O0 = i1IiiiI1iI ( oOo0oooo00o ( 'aHR0cDovL2xpdmVvbnNhdC5jb20vcXVpY2tpbmRleC5odG1s' ) )
 ooOOoooooo = re . compile ( '<a target="_self" href="(.+?)".+?src="(.+?)" alt="(.+?)"' , re . DOTALL ) . findall ( OOOOO0oo0O0O0 )
 for I1Ii1iI1 , oOo0 , II1I in ooOOoooooo :
  ooooooO0oo ( '[COLORgreen]' + ( II1I ) . replace ( 'amp;' , '' ) + '[/COLOR]' , oOo0oooo00o ( 'aHR0cDovL2xpdmVvbnNhdC5jb20v' ) + I1Ii1iI1 , 10010 , oOo0oooo00o ( 'aHR0cDovL2xpdmVvbnNhdC5jb20v' ) + oOo0 , OOooO0OOoo , '' )
  if 29 - 29: O0 . O0oO
def OO0o0oO0O000o ( url ) :
 iiI = i1IiiiI1iI ( url )
 I11ii1i1 = re . compile ( 'AndClearL.+?><h2.+?head>(.*?)float' , re . DOTALL ) . findall ( iiI )
 for I11ii1i1 in I11ii1i1 :
  I1iI11iii = re . compile ( '(.*?)</h2>' ) . findall ( str ( I11ii1i1 ) )
  for oo0oO in I1iI11iii :
   oo0oO = oo0oO
  IiIi1iI11 = re . compile ( 'comp_head>(.*?)</span>.*?<div class = fLeft width = ".*?"><img src="(.*?)">.*?</div>.*?ST:(.*?)</div>(.+?)<!-- around all of channel types ENDS 2-->' , re . DOTALL ) . findall ( str ( I11ii1i1 ) )
  for iiI1iI1I , oOo0 , time , III1II111Ii1 in IiIi1iI11 :
   o0O0OO0o = re . compile ( ",CAPTION, '(.+?)&nbsp" ) . findall ( III1II111Ii1 )
   ooooooO0oo ( '[COLORgreen]' + oo0oO + ' - ' + iiI1iI1I + ' - ' + time + '[/COLOR]' , '' , 10010 , oOo0oooo00o ( 'aHR0cDovL2xpdmVvbnNhdC5jb20=' ) + oOo0 , OOooO0OOoo , ( str ( o0O0OO0o ) ) )
   if 54 - 54: I1IiI . OoOO % i11iIiiIii / OoooooooOO + IIII % OoOO
 I1i1I1II ( 'tvshows' , 'Media Info 3' )
 if 36 - 36: OoOO
def o0OO ( ) :
 if 7 - 7: OOooOOo / Ooo00oOo00o * i11iIiiIii * O0
 ooooooO0oo ( '[COLORgreen]Shows[/COLOR]' , 'http://www.fullmatchesandshows.com/category/show/' , 10011 , 'http://www.fm-base.co.uk/forum/attachments/club-competition-logos/3885-soccer-am-logo-socceram.png' , oOOoO0 + 'fanart.jpg' , '' )
 ooooooO0oo ( '[COLORgreen]Premier League[/COLOR]' , 'http://www.fullmatchesandshows.com/premier-league/' , 10011 , 'https://footballseasons.files.wordpress.com/2013/05/premier-league.png' , oOOoO0 + 'fanart.jpg' , '' )
 ooooooO0oo ( '[COLORgreen]La Liga[/COLOR]' , 'http://www.fullmatchesandshows.com/la-liga/' , 10011 , 'http://1.bp.blogspot.com/-c6kQ40ryhyo/U19cUlz25sI/AAAAAAAABak/qtn5chSFZm0/s1600/la-liga-logo_display_image.png' , oOOoO0 + 'fanart.jpg' , '' )
 ooooooO0oo ( '[COLORgreen]Bundesliga[/COLOR]' , 'http://www.fullmatchesandshows.com/bundesliga/' , 10011 , 'http://m.img.brothersoft.com/iphone/189/518670189_icon175x175.jpg' , oOOoO0 + 'fanart.jpg' , '' )
 ooooooO0oo ( '[COLORgreen]Champions League[/COLOR]' , 'http://www.fullmatchesandshows.com/champions-league/' , 10011 , 'http://www.ecursuri.ro/images/teste/test-champions-league.jpg' , oOOoO0 + 'fanart.jpg' , '' )
 ooooooO0oo ( '[COLORgreen]Serie A[/COLOR]' , 'http://www.fullmatchesandshows.com/category/serie-a/' , 10011 , 'http://files.jcriccione.it/200000223-2484526782/serie%20a.png' , oOOoO0 + 'fanart.jpg' , '' )
 ooooooO0oo ( '[COLORgreen]Ligue 1[/COLOR]' , 'http://www.fullmatchesandshows.com/category/ligue-1/' , 10011 , 'http://a1.mzstatic.com/us/r30/Purple5/v4/37/c7/44/37c744ae-5824-42b7-6ce0-5f471f52baab/icon180x180.jpeg' , oOOoO0 + 'fanart.jpg' , '' )
 ooooooO0oo ( '[COLORgreen]Copa America 2015[/COLOR]' , 'http://www.fullmatchesandshows.com/copa-america-2015/' , 10011 , 'https://pbs.twimg.com/profile_images/521966985907691520/Nq9OAPIo_400x400.png' , oOOoO0 + 'fanart.jpg' , '' )
 ooooooO0oo ( '[COLORgreen]CONCACAF[/COLOR]' , 'http://www.fullmatchesandshows.com/category/concacaf/' , 10011 , 'http://a3.mzstatic.com/us/r30/Purple3/v4/40/26/14/4026147c-7022-4ca3-504e-e78950cc3f1c/icon175x175.png' , oOOoO0 + 'fanart.jpg' , '' )
 ooooooO0oo ( '[COLORgreen]Women World Cup[/COLOR]' , 'http://www.fullmatchesandshows.com/category/women-world-cup/' , 10011 , 'https://upload.wikimedia.org/wikipedia/en/thumb/7/76/2015_FIFA_Women\'s_World_Cup_logo.svg/967px-2015_FIFA_Women\'s_World_Cup_logo.svg.png' , oOOoO0 + 'fanart.jpg' , '' )
 if 79 - 79: iIii1I11I1II1
def O00oO0o ( url ) :
 iiI = i1IiiiI1iI ( url )
 ooOOoooooo = re . compile ( 'itemprop="image" class="entry-thumb" src="(.+?)".+?<h3 itemprop="name" class="entry-title td-module-title"><a itemprop="url" href="(.+?)" rel="bookmark" title=".+?">(.+?)</a></h3>' , re . DOTALL ) . findall ( iiI )
 for oOo0 , url , II1I in ooOOoooooo :
  I1i1iii = II1I . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' )
  IiI1iiiIii ( '[COLORgreen]' + I1i1iii + '[/COLOR]' , url , 10013 , oOo0 )
  if 31 - 31: OoooooooOO + oO0o0ooO0 - I1IiI . i1IIi % oO0o0ooO0
def I1i1Ii111IIii ( url ) :
 iiI = i1IiiiI1iI ( url )
 ooOOoooooo = re . compile ( '<script data-config="(.+?)" data-height' ) . findall ( iiI )
 for i11IIIiI1I in ooOOoooooo :
  II1ii1I1 = ( i11IIIiI1I ) . replace ( '/v2' , '' ) . replace ( 'zeus.json' , 'video-sd.mp4?hosting_id=21772' ) . replace ( 'config.playwire.com' , 'cdn.video.playwire.com' )
  II1IIiiIiI ( 'http:' + II1ii1I1 )
  if 2 - 2: OoooooooOO . OoOO0ooOOoo0O . IIII
  if 42 - 42: OoOO0ooOOoo0O % OoOO / Ooo00oOo00o - OoOO * i11iIiiIii
def iI1IiiiIiI1Ii ( ) :
 OOOOO0oo0O0O0 = oOoO0O0o0Oooo ( oOo0oooo00o ( 'aHR0cDovL2pvaG5sb2NrZXIuY29tLw==' ) )
 ooOOoooooo = re . compile ( '<li id="menu-item-.+?" class=".+?"><a href="(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( OOOOO0oo0O0O0 )
 for I1Ii1iI1 , II1I in ooOOoooooo :
  O0OO0O ( II1I , I1Ii1iI1 , 8046 , oOOoO0 + 'documentary.png' )
def Oo000 ( url ) :
 OOOOO0oo0O0O0 = oOoO0O0o0Oooo ( url )
 ooOOoooooo = re . compile ( 'data-type="inline" href="(.+?)" >.+?src="(.+?)" class="entry-thumbnail wp-post-image" alt="(.+?)" itemprop="image"' , re . DOTALL ) . findall ( OOOOO0oo0O0O0 )
 o0OO0o0o00o = re . compile ( 'class="inactive">.+?</a><a href="(.+?)">Next</a></div>' , re . DOTALL ) . findall ( OOOOO0oo0O0O0 )
 for url , oOo0 , II1I in ooOOoooooo :
  IiI1iiiIii ( ( II1I ) . replace ( '&#8211;' , '-' ) . replace ( '&#8217;' , '' ) , url , 8047 , oOo0 )
 for url in o0OO0o0o00o :
  O0OO0O ( 'NEXT PAGE' , url , 8046 , oOOoO0 + 'documentary.png' )
  if 48 - 48: i11iIiiIii % OoOO
def i11i11 ( url ) :
 OOOOO0oo0O0O0 = oOoO0O0o0Oooo ( url )
 ooOOoooooo = re . compile ( "src='http://www.youtube.com/embed/(.+?)?version=3&#038;rel=1&#038;fs=1&#038;autohide=2&#038;showsearch=0&#038;showinfo=1&#038;iv_load_policy=1&#038;wmode=transparent' frameborder='0' allowfullscreen='true'></iframe>" ) . findall ( OOOOO0oo0O0O0 )
 for url in ooOOoooooo :
  yt . PlayVideo ( url )
  if 18 - 18: iIii1I11I1II1 + o0000oOoOoO0o * OOOo0 - OoOO0ooOOoo0O / OOOo0
def o00iI1i1II ( ) :
 OOOOO0oo0O0O0 = oOoO0O0o0Oooo ( oOo0oooo00o ( 'aHR0cDovL3RvcGRvY3VtZW50YXJ5ZmlsbXMuY29tLw==' ) )
 ooOOoooooo = re . compile ( '<a href="(.+?)" >(.+?)</a></li><li>' ) . findall ( OOOOO0oo0O0O0 )
 for I1Ii1iI1 , II1I in ooOOoooooo :
  O0OO0O ( II1I , I1Ii1iI1 , 8041 , oOOoO0 + 'documentary.png' )
def I1ii1ii1I ( url ) :
 OOOOO0oo0O0O0 = oOoO0O0o0Oooo ( url )
 ooOOoooooo = re . compile ( '<h2><a href="(.+?)" title="(.+?)">.+?</a></h2>.+?src="(.+?)"' , re . DOTALL ) . findall ( OOOOO0oo0O0O0 )
 o0OO0o0o00o = re . compile ( 'class="inactive">.+?</a><a href="(.+?)">Next</a></div>' , re . DOTALL ) . findall ( OOOOO0oo0O0O0 )
 for url , II1I , oOo0 in ooOOoooooo :
  O0OO0O ( ( II1I ) . replace ( '&#039;s' , '' ) , url , 8042 , oOo0 )
 for url in o0OO0o0o00o :
  O0OO0O ( 'NEXT PAGE' , url , 8041 , oOOoO0 + 'documentary.png' )
  if 18 - 18: OoOO * OoOO % OoOO
  if 17 - 17: O0 * I1IiI * ii11ii1ii * OoOoOO00 * o0000oOoOoO0o % i1IIi
def IIiIi1iI1iII ( url ) :
 OOOOO0oo0O0O0 = oOoO0O0o0Oooo ( url )
 ooOOoooooo = re . compile ( '<meta itemprop="name" content="(.+?)".+?<meta itemprop="thumbnailUrl" content="(.+?)".+?<meta itemprop="embedUrl" content="(.+?)".+?<meta itemprop="description" content="(.+?)" />' , re . DOTALL ) . findall ( OOOOO0oo0O0O0 )
 o0OO0o0o00o = re . compile ( '<div class="video new-video"><iframe width="766" height="431" src="(.+?)&amp;iv_load_policy=3&amp;showinfo=0&amp;autohide=1"' , re . DOTALL ) . findall ( OOOOO0oo0O0O0 )
 for II1I , oOo0 , url , OOO in ooOOoooooo :
  IiI1iiiIii ( ( II1I ) . replace ( '&#039;s' , '' ) , url . replace ( 'https://www.youtube.com/embed/' , '' ) , 8043 , oOo0 )
 for url in o0OO0o0o00o :
  OoOo00o ( ( url ) . replace ( '//' , 'http://' ) )
  if 30 - 30: I1IiI . o0000oOoOoO0o / o0000oOoOoO0o * i11iIiiIii
def OoOo00o ( url ) :
 OOOOO0oo0O0O0 = oOoO0O0o0Oooo ( url )
 ooOOoooooo = re . compile ( '<link rel="canonical" href="(.+?)">  <link rel="stylesheet"' ) . findall ( OOOOO0oo0O0O0 )
 for url in ooOOoooooo :
  IiI1iiiIii ( 'PLAY' , ( url ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , oOOoO0 + 'documentary.png' )
  if 46 - 46: Ooo00oOo00o * Oo % OoOO + O0 * IIII
def ii1I11i ( ) :
 iiI = oOoO0O0o0Oooo ( 'http://www.stream2watch.co/live-tv' )
 ooOOoooooo = re . compile ( '<a href="(.+?)">.+?<img src="(.+?)" alt=".+?"/>.+?<span class="country_name">(.+?)<br />(.+?)</span>' , re . DOTALL ) . findall ( iiI )
 for I1Ii1iI1 , oOo0 , II1I , O0OOO in ooOOoooooo :
  O0OO0O ( ( II1I + '[COLORgreen]' + O0OOO + '[/COLOR]' ) , I1Ii1iI1 , 8086 , oOo0 )
  if 37 - 37: O0 - o0000oOoOoO0o
def IiI1 ( url ) :
 iiI = oOoO0O0o0Oooo ( url )
 ooOOoooooo = re . compile ( '<a class="front_channel_href" href="(.+?)" title=".+?">.+?<img class="front_channel_thumb" src="(.+?)" alt=".+?"/>.+?<span class="front_channel_name">(.+?)</span>' , re . DOTALL ) . findall ( iiI )
 for url , oOo0 , II1I in ooOOoooooo :
  O0OO0O ( '[COLORgreen]' + II1I + '[/COLOR]' , url , 8087 , oOo0 )
  if 59 - 59: o0000oOoOoO0o / Oo / OoOO0ooOOoo0O / O0 / I1IiI + OOooOOo
def IIiI1111i1 ( url ) :
 iiI = i1IiiiI1iI ( url )
 ooOOoooooo = re . compile ( 'a id="code_.+?data-f-href="(.+?)" data-code-embed="">(.+?)</a>' , re . DOTALL ) . findall ( iiI )
 for url , II1I in ooOOoooooo :
  ii1ii1I1IIi1 ( url , II1I )
  if 55 - 55: OOOo0
def ii1ii1I1IIi1 ( url , name ) :
 iiI = i1IiiiI1iI ( url )
 ooOOoooooo = re . compile ( "playStream\('.+?', '(.+?)'\);" , re . DOTALL ) . findall ( iiI )
 for url in ooOOoooooo :
  print url
  IiI1iiiIii ( '[COLORgreen]' + name + '[/COLOR]' , url , 222 , '' )
  if 45 - 45: O0 / i1IIi * OoOO * Ooo00oOo00o
def II11I ( ) :
 OOOOO0oo0O0O0 = oOoO0O0o0Oooo ( oOo0oooo00o ( 'aHR0cDovL2JyYXR1LW1hcmlhbi5yby8=' ) )
 ooOOoooooo = re . compile ( '<tr><td ><img width="25" height="25" src="(.+?)" alt="" /> </td>.+?<td >(.+?)</td>.+?<td >(.+?)</td>.+?<td >(.+?)</td>.+?<td >(.+?)</td>.+?<td >    <a class="wp-colorbox-youtube" href="(.+?)">Watch Online</a></td>.+?</tr>' , re . DOTALL ) . findall ( OOOOO0oo0O0O0 )
 for oOo0 , time , iiiI11iIIi1 , iiI1iI1I , IiIi1iI11 , I1Ii1iI1 in ooOOoooooo :
  O0OO0O ( ( time + '[COLORgreen]' + IiIi1iI11 + '[/COLOR]' + iiI1iI1I ) . replace ( '&#8211;' , ':' ) . replace ( '&ndash;' , '-' ) , I1Ii1iI1 , 8061 , oOo0 )
def o00OoooooooOo ( url ) :
 OOOOO0oo0O0O0 = oOoO0O0o0Oooo ( url )
 ooOOoooooo = re . compile ( 'type:.+?,.+?url: "(.+?)"' , re . DOTALL ) . findall ( OOOOO0oo0O0O0 )
 for url in ooOOoooooo :
  IiI1iiiIii ( '[COLORgreen]LINK 1[/COLOR]' , url , 222 , oOOoO0 + 'documentary.png' )
  if 32 - 32: OOooOOo + OOOo0 . O0oO
def iIi ( ) :
 iiI = i1IiiiI1iI ( oOo0oooo00o ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vbTN1c3RyZWFtcw==' ) )
 ooOOoooooo = re . compile ( '<li><a href="(.+?)"> (.+?).m3u</a></li>' ) . findall ( iiI )
 for I1Ii1iI1 , II1I in ooOOoooooo :
  O0OO0O ( ( '[COLORgreen]' + II1I + '[/COLOR]' ) . replace ( '-' , ' ' ) . replace ( '_' , ' ' ) , ( oOo0oooo00o ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vbTN1c3RyZWFtcy8=' ) ) + I1Ii1iI1 , 8071 , oOOoO0 + 'streams.png' )
def Ii1Ii11IiI1I1 ( url ) :
 iiI = oOoO0O0o0Oooo ( url )
 ooOOoooooo = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( iiI )
 for II1I , url in ooOOoooooo :
  IiI1iiiIii ( ( '[COLORgreen]' + II1I + '[/COLOR]' ) . replace ( '_' , ' ' ) , ( url ) . strip ( ) , 404 , oOOoO0 + 'streams.png' )
def OOo ( url ) :
 iiI = oOoO0O0o0Oooo ( url )
 ooOOoooooo = re . compile ( 'EXTINF:(.+?),(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( iiI )
 for oOo0 , II1I , url in ooOOoooooo :
  IiI1iiiIii ( ( '[COLORgreen]' + II1I + '[/COLOR]' ) . replace ( '_' , ' ' ) , ( ( oOo0oooo00o ( 'aHR0cDovL2dlbmlldHYuaXB0di5yZTo4MDAwL2xpdmUv' ) ) + oooOOOOO + '/' + i1iiIII111ii + url ) . strip ( ) , 222 , oOo0 )
  if 41 - 41: O0 + OoOO . i1IIi - OoOoOO00 * OOooOOo . Ooo00oOo00o
def oooO00Oo ( ) :
 ooO00o ( 'Best Videos' , 'http://www.xvideos.com/best' , 10105 , oOOoO0 + 'JIZBOX.png' , '' , '' )
 ooO00o ( 'Genres' , 'http://www.xvideos.com' , 10106 , oOOoO0 + 'JIZBOX.png' , '' , '' )
 ooO00o ( 'Recently Uploaded' , 'http://xvideos.com' , 10105 , oOOoO0 + 'JIZBOX.png' , '' , '' )
 ooO00o ( 'Tags' , 'http://www.xvideos.com/tags' , 10103 , oOOoO0 + 'JIZBOX.png' , '' , '' )
 ooO00o ( 'Search' , '' , 10107 , oOOoO0 + 'JIZBOX.png' , '' , '' , )
 if 73 - 73: oO0o0ooO0 * oO0o0ooO0 / o0oO0
def IIii1i11iI1II11 ( url ) :
 iiI = i1IiiiI1iI ( url )
 iIi11i = re . compile ( '<li><a class=".+?".+?href="(.+?)">Next</a></li>' ) . findall ( iiI )
 for url in iIi11i :
  ooO00o ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10103 , oOOoO0 + 'JIZBOX.png' , '' , '' )
 ooOOoooooo = re . compile ( '<li><a href="(.+?)"><b>(.+?)</b><span class="navbadge default"(.+?)</span>' ) . findall ( iiI )
 for url , II1I , ooIII1II1iii1i in ooOOoooooo :
  ooO00o ( II1I + ' - No of Videos : ' + ( ooIII1II1iii1i ) . replace ( '>' , '' ) , 'http://www.xvideos.com' + url , 10105 , oOOoO0 + 'JIZBOX.png' , '' , '' )
  if 75 - 75: IIII - I1IiI - iIii1I11I1II1 % OOooOOo
def OooooO ( url ) :
 iiI = i1IiiiI1iI ( url )
 iIi11i = re . compile ( 'href="([^"]*)">Next</a></li>' ) . findall ( iiI )
 for url in iIi11i :
  ooO00o ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10104 , oOOoO0 + 'JIZBOX.png' , '' , '' )
 ooOOoooooo = re . compile ( ':"([^"]*)".+?;</script></a></div></div><p class="profile-name"><a href="([^"]*)">(.+?)</a></p><p class="profile-counts">\n(.+?)\n' , re . DOTALL ) . findall ( iiI )
 for oOo0 , url , II1I , oO0O0 in ooOOoooooo :
  ooO00o ( II1I + '--' + oO0O0 , 'http://www.xvideos.com' + url + '#_tabVideos,videos-best' , 10105 , ( oOo0 ) . replace ( 'http:\/\/' , 'http://' ) , '' , '' )
  if 19 - 19: o00O0oo
  if 55 - 55: OoOO0ooOOoo0O % OoOO0ooOOoo0O / O0 % oO0o0ooO0 - OOooOOo . Oo
def iiiii1I1III1 ( url ) :
 iiI = i1IiiiI1iI ( url )
 ooOOoooooo = re . compile ( '<div class="thumb-inside"><script>.+?<img src="(.+?)".+?<a href="(.+?)" title=".+?">(.+?)</a></p>.+?uration">(.+?)</span>.+?Porn quality:(.+?)</span>' , re . DOTALL ) . findall ( iiI )
 for oOo0 , url , II1I , i1oO00O , oo0o0ooooo in ooOOoooooo :
  i1i ( II1I + ' - Porn Quality : ' + oo0o0ooooo + ' - ' + i1oO00O , 'http://www.xvideos.com' + url , 10108 , oOo0 , oOo0 , oo0o0ooooo + ' - ' + i1oO00O )
 O0o0O = re . compile ( '<li><a href="([^"]*)" class="no-page">Next</a></li></ul></div>' ) . findall ( iiI )
 for url in O0o0O :
  ooO00o ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10105 , oOOoO0 + 'JIZBOX.png' , '' , '' )
  if 6 - 6: OoOoOO00
def I11i1iIi111 ( url ) :
 iiI = i1IiiiI1iI ( url )
 I11ii1i1 = re . compile ( '<div class="main-categories">(.+?)</div>' , re . DOTALL ) . findall ( iiI )
 iIi11i = re . compile ( '<li><a class=".+?".+?href="(.+?)">Next</a></li>' ) . findall ( iiI )
 for url in iIi11i :
  ooO00o ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10106 , oOOoO0 + 'JIZBOX.png' , '' , '' )
 ooOOoooooo = re . compile ( '<li><a href="(.+?)" class="btn btn-default">(.+?)</a>' ) . findall ( str ( I11ii1i1 ) )
 for url , II1I in ooOOoooooo :
  ooO00o ( II1I , 'http://www.xvideos.com' + url , 10105 , oOOoO0 + 'JIZBOX.png' , '' , '' )
  if 35 - 35: OOooOOo
  if 73 - 73: O0 - ii11ii1ii
def ii1I ( ) :
 o00o0 = Oo0o0000o0o0 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oO0O = ( o00o0 ) . replace ( ' ' , '+' ) . replace ( '&amp;' , '&' )
 II1III1I1I1Ii = oO0O . lower ( )
 ooOOooo0ooo00 = 'http://www.xvideos.com/?k=' + II1III1I1I1Ii
 print ooOOooo0ooo00 + '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'
 iiI = i1IiiiI1iI ( ooOOooo0ooo00 )
 ooOOoooooo = re . compile ( '<div class="thumb-inside"><script>.+?<img src="(.+?)".+?<a href="(.+?)" title=".+?">(.+?)</a></p>.+?uration">(.+?)</span>.+?Porn quality:(.+?)</span>' , re . DOTALL ) . findall ( iiI )
 for oOo0 , I1Ii1iI1 , II1I , i1oO00O , oo0o0ooooo in ooOOoooooo :
  i1i ( II1I + ' - Porn Quality : ' + oo0o0ooooo + ' - ' + i1oO00O , 'http://www.xvideos.com' + I1Ii1iI1 , 10108 , oOo0 , oOo0 , oo0o0ooooo + ' - ' + i1oO00O )
 O0o0O = re . compile ( '<li><a href="([^"]*)" class="no-page">Next</a></li></ul></div>' ) . findall ( iiI )
 for I1Ii1iI1 in O0o0O :
  ooO00o ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + I1Ii1iI1 , 10105 , oOOoO0 + 'JIZBOX.png' , '' , '' )
  if 56 - 56: OOOo0
def ii1IIi1ii ( url ) :
 iiI = i1IiiiI1iI ( url )
 ooOOoooooo = re . compile ( 'flv_url=(.+?)\;' ) . findall ( iiI )
 for url in ooOOoooooo :
  oo0OoOOooO = ( url ) . replace ( '%3A' , ':' ) . replace ( '%2F' , '/' ) . replace ( '%3F' , '?' ) . replace ( '%3D' , '=' ) . replace ( '%26' , '&' ) . replace ( '&amp' , '' )
  o0o0OO0o00o0O ( oo0OoOOooO )
  if 28 - 28: Ooo00oOo00o - OoOO + I1IiI + o00O0oo / iIii1I11I1II1
def o0o0OO0o00o0O ( url ) :
 iiiii11I1 = xbmc . Player ( Ii1 ( ) )
 import urlresolver
 try : iiiii11I1 . play ( url )
 except : pass
 if 77 - 77: OoOO0ooOOoo0O / OoOoOO00 + IIII + o0oO0 - i11iIiiIii
 if 44 - 44: OOOo0 + I1IiI + ii11ii1ii . OOOo0 * I1IiI % iIii1I11I1II1
def o0OO0OOO0O ( ) :
 iiI = i1IiiiI1iI ( oOo0oooo00o ( 'aHR0cDovL3d3dy54bnh4LmNvbS8=' ) )
 ooOOoooooo = re . compile ( '<a href="(.+?)">(.+?)</a><br>' ) . findall ( iiI )
 for I1Ii1iI1 , II1I in ooOOoooooo :
  O0OO0O ( '[COLORgreen]' + II1I + '[/COLOR]' , I1Ii1iI1 , 8091 , oOOoO0 + 'streams.png' )
def Iii1I ( url ) :
 iiI = oOoO0O0o0Oooo ( url )
 ooOOoooooo = re . compile ( '<a href="(.+?)".+?src="(.+?)".+?title="(.+?)">' , re . DOTALL ) . findall ( iiI )
 for url , oOo0 , II1I in ooOOoooooo :
  IiI1iiiIii ( '[COLORgreen]' + II1I + '[/COLOR]' , url , 8092 , oOo0 )
def oOoOOOOoOO0o ( url ) :
 iiI = oOoO0O0o0Oooo ( url )
 ooOOoooooo = re . compile ( 'src=&quot;(.+?)&quot;' ) . findall ( iiI )
 for url in ooOOoooooo :
  ii ( url )
  if 47 - 47: O0oO - OoOO0ooOOoo0O / o0oO0 - Oo + oO0o0ooO0 - iIii1I11I1II1
def o0OOOOO0 ( url ) :
 Ooo0Oo0o = urllib2 . Request ( url )
 Ooo0Oo0o . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
 oo0Oo0 = ''
 IIiIi1iI = ''
 try :
  oo0Oo0 = urllib2 . urlopen ( Ooo0Oo0o )
  IIiIi1iI = oo0Oo0 . read ( )
  oo0Oo0 . close ( )
 except : pass
 if IIiIi1iI != '' :
  return IIiIi1iI
 else :
  IIiIi1iI = 'Failed'
  return IIiIi1iI
  if 66 - 66: Ooo00oOo00o % OOooOOo
def iI1ii11Ii ( ) :
 O0OO0OO = ( oOo0oooo00o ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 o00o0 = Oo0o0000o0o0 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 II1III1I1I1Ii = o00o0 . lower ( )
 I1Ii1iI1 = ( oOo0oooo00o ( 'aHR0cDovL2RsNC5tb3ZpZWZhcnNpLmNvbS9maWxtLzIwMTUtNy8=' ) )
 O0o0OO0000ooo = ( oOo0oooo00o ( 'aHR0cDovL2RsLmF2YWRsLmNvbS9OZXcvTW92aWUv' ) )
 Ooo0oO = ( oOo0oooo00o ( 'aHR0cDovLzIxNy4yMTkuMTQzLjEwOC8xMzI3Lw==' ) )
 IiIiIIiii1I = ( oOo0oooo00o ( 'aHR0cDovLzE3OC4xNjIuMjE0LjIzMi92b2QvbW92aWVzL2VuZ2xpc2gv' ) )
 ooooo0Oo0 = ( oOo0oooo00o ( 'aHR0cDovL3Njb29ieXN0cmVhbS54MTBob3N0LmNvbS8vc2Nvb2J5L21vdi9hbGwucGhw' ) )
 o0I1IIIi11ii11 = ( oOo0oooo00o ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 O0o0oo0oOO0oO = ( oOo0oooo00o ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL3NlYXJjaC8/cT0=' ) ) + o00o0
 iIiIII1iI1111 = ( oOo0oooo00o ( 'aHR0cDovL2xldHdhdGNoLnVzLz9vcD1zZWFyY2gmaz0=' ) ) + ( o00o0 ) . replace ( ' ' , '+' )
 if 37 - 37: i11iIiiIii % OoOO * OoOO0ooOOoo0O * OoOO0ooOOoo0O * o00O0oo
 iiI = o0OOOOO0 ( I1Ii1iI1 )
 II1iIi1IiIii = o0OOOOO0 ( O0o0OO0000ooo )
 I1I1i = o0OOOOO0 ( Ooo0oO )
 O0O0oo = o0OOOOO0 ( IiIiIIiii1I )
 o00O = o0OOOOO0 ( ooooo0Oo0 )
 Oo000O = o0OOOOO0 ( O0o0oo0oOO0oO )
 I1111III11 = i1IiiiI1iI ( iIiIII1iI1111 )
 if 46 - 46: O0
 if iiI != 'Failed' :
  ooOOoooooo = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( iiI )
  for OoOOoooO000 , II1I in ooOOoooooo :
   if o00o0 in II1I . lower ( ) :
    IiI1iiiIii ( ( '[COLORgreen]' + II1I + '- source 1[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( I1Ii1iI1 + OoOOoooO000 ) , 222 , '' )
 if II1iIi1IiIii != 'Failed' :
  o0OO0o0o00o = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( II1iIi1IiIii )
  for OoOOoooO000 , II1I in o0OO0o0o00o :
   if o00o0 in II1I . lower ( ) :
    IiI1iiiIii ( ( '[COLORgreen]' + II1I + '- source 2[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( O0o0OO0000ooo + OoOOoooO000 ) , 222 , '' )
 if I1I1i != 'Failed' :
  iIII = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( I1I1i )
  for OoOOoooO000 , II1I in iIII :
   if o00o0 in II1I . lower ( ) :
    IiI1iiiIii ( ( '[COLORgreen]' + II1I + '- source 3[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( Ooo0oO + OoOOoooO000 ) , 222 , '' )
 if O0O0oo != 'Failed' :
  OoO0o000oOo = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( O0O0oo )
  for OoOOoooO000 , II1I in OoO0o000oOo :
   if o00o0 in II1I . lower ( ) :
    IiI1iiiIii ( ( '[COLORgreen]' + II1I + '- source 4[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( IiIiIIiii1I + OoOOoooO000 ) , 222 , '' )
 if o00O != 'Failed' :
  Oo00OO00o0oO = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( o00O )
  for OoOOoooO000 , oOo0 , II1I in Oo00OO00o0oO :
   if o00o0 in II1I . lower ( ) :
    O0OO0O ( ( '[COLORgreen]' + II1I + '- source Scooby[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( 'Ganool' , '' ) . replace ( 'ShAaNiG' , '' ) . replace ( 'YIFY' , '' ) . replace ( '[[ Max-Movie.In ]]' , '' ) . replace ( '.mkv' , '' ) . replace ( '.mp4' , '' ) . replace ( '.' , ' ' ) , OoOOoooO000 , 1006 , 'img' )
    if 43 - 43: Oo . O0oO
    I1i1I1II ( 'tvshows' , 'Media Info 3' )
 if Oo000O != 'Failed' :
  I1I1i1i = re . compile ( 'href="(.+?)".+?src="(.+?)" alt="Image of (.+?)"' , re . DOTALL ) . findall ( Oo000O )
  for I1Ii1iI1 , oOo0 , II1I in I1I1i1i :
   if o00o0 in II1I . lower ( ) :
    O0OO0O ( ( '[COLORgreen]' + II1I + '- source Snag[/COLOR]' ) . replace ( '&#x27;' , '' ) , 'http://www.snagfilms.com' + I1Ii1iI1 , 7067 , oOo0 )
    if 87 - 87: I1IiI / IIII . o0oO0 - OoOO0ooOOoo0O / Ooo00oOo00o
    I1i1I1II ( 'tvshows' , 'Media Info 3' )
 if I1111III11 != 'Failed' :
  iiI1I = re . compile ( '<div class="video_block video_block_default ">.+?<a href="#">.+?<a href="(.*?)".+?<img src="(.+?)" height=".+?" alt="(.+?)"' , re . DOTALL ) . findall ( I1111III11 )
  for I1Ii1iI1 , oOo0 , II1I in iiI1I :
   IiI1iiiIii ( '[COLORgreen]' + II1I + '- Source 7[/COLOR]' , I1Ii1iI1 , 222 , oOo0 )
 oOOOoo = [ '0-9/' , 'A/' , 'B/' , 'C/' , 'D/' , 'E/' , 'F/' , 'G/' , 'H/' , 'I/' , 'J/' , 'K/' , 'L/' , 'M/' , 'N/' , 'O/' , 'P/' , 'R/' , 'S/' , 'T/' , 'U/' , 'V/' , 'W/' , 'X/' , 'Y/' , 'Z/' ]
 if 69 - 69: iIii1I11I1II1 . OoOO0ooOOoo0O / OoOO0ooOOoo0O
 if 72 - 72: OoOoOO00 % O0 . i1IIi / o0oO0 * O0oO
 for oooO0o0o0O0 in oOOOoo :
  iii11111I = O0OO0OO + oooO0o0o0O0
  OooOoOO0OO = o0OOOOO0 ( iii11111I )
  if o00O != 'Failed' :
   I1iiIiiii1111 = re . compile ( '<li><a href="(.+?)"> (.+?)</a></li>' ) . findall ( OooOoOO0OO )
   for OoOOoooO000 , II1I in I1iiIiiii1111 :
    if o00o0 in II1I . lower ( ) :
     IiI1iiiIii ( ( '[COLORgreen]' + II1I + 'source 5[/COLOR]' ) . replace ( 'Ganool' , '' ) . replace ( 'ShAaNiG' , '' ) . replace ( 'YIFY' , '' ) . replace ( '[[ Max-Movie.In ]]' , '' ) . replace ( '.mkv' , '' ) . replace ( '.mp4' , '' ) . replace ( '.' , ' ' ) , ( O0OO0OO + oooO0o0o0O0 + OoOOoooO000 ) , 222 , '' )
     if 29 - 29: o00O0oo - OOOo0 / OOOo0 * o00O0oo * IIII . OoOO0ooOOoo0O
     I1i1I1II ( 'tvshows' , 'Media Info 3' )
     if 80 - 80: iIii1I11I1II1
     if 23 - 23: OoOoOO00
def o0oO0OO00oo0o ( ) :
 if 17 - 17: IIII / ii11ii1ii - OOooOOo * ii11ii1ii
 o00o0 = Oo0o0000o0o0 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 II1III1I1I1Ii = o00o0 . lower ( )
 I1Ii1iI1 = ( oOo0oooo00o ( 'aHR0cDovL2RsLmZhcnNpbW92aWUubmV0L1NlcmlhbC8=' ) )
 O0o0OO0000ooo = ( oOo0oooo00o ( 'aHR0cDovL3N2Mi5kbC1wYXJzLmluLw==' ) )
 Ooo0oO = ( oOo0oooo00o ( 'aHR0cDovL3R2LmRsLXBhcnMuaW4v' ) )
 IiIiIIiii1I = ( oOo0oooo00o ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9BbWVyaWNhbiUyMFNlcmlhbC8=' ) )
 ooooo0Oo0 = ( oOo0oooo00o ( 'aHR0cDovL2RpemlsYWIuY29tL2Fyc2l2P2xpbWl0PSZ0dXI9Jm9yZGVyYnk9JnVsa2U9Jm9yZGVyPSZ5aWw9JmRpemlfYWRpPQ==' ) ) + ( o00o0 ) . replace ( ' ' , '+' )
 o0I1IIIi11ii11 = ( oOo0oooo00o ( 'aHR0cDovL3Njb29ieXN0cmVhbS54MTBob3N0LmNvbS8vc2Nvb2J5L3Nob3dzL3R2YWxsLnBocA==' ) )
 iIiIII1iI1111 = ( oOo0oooo00o ( 'aHR0cDovL2xldHdhdGNoLnVzLz9vcD1zZWFyY2gmaz0=' ) ) + ( o00o0 ) . replace ( ' ' , '+' )
 i11i11II11i = ( oOo0oooo00o ( 'aHR0cDovL3d3dy53YXRjaHNlcmllcy5saS9zZWFyY2gv' ) ) + o00o0 . replace ( ' ' , '%20' )
 if 9 - 9: I1IiI - ii11ii1ii * o0oO0 . o0oO0 - OOOo0
 iiI = o0OOOOO0 ( I1Ii1iI1 )
 II1iIi1IiIii = o0OOOOO0 ( O0o0OO0000ooo )
 I1I1i = o0OOOOO0 ( Ooo0oO )
 O0O0oo = o0OOOOO0 ( IiIiIIiii1I )
 o00O = cloudflare . source ( ooooo0Oo0 )
 OooOoOO0OO = o0OOOOO0 ( o0I1IIIi11ii11 )
 I1111III11 = i1IiiiI1iI ( iIiIII1iI1111 )
 OOooOooo0OOo0 = i1IiiiI1iI ( i11i11II11i )
 if iiI != 'Failed' :
  ooOOoooooo = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( iiI )
  for II1I in ooOOoooooo :
   if o00o0 in II1I . lower ( ) :
    O0OO0O ( ( '[COLORgreen]' + II1I + ' source 1[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( I1Ii1iI1 + II1I ) . replace ( ' ' , '%20' ) , 1006 , '' )
    if 87 - 87: IIII
    I1i1I1II ( 'tvshows' , 'Media Info 3' )
 if II1iIi1IiIii != 'Failed' :
  o0OO0o0o00o = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( II1iIi1IiIii )
  for II1I in o0OO0o0o00o :
   if o00o0 in II1I . lower ( ) :
    O0OO0O ( ( '[COLORgreen]' + II1I + ' source 2[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( O0o0OO0000ooo + II1I ) . replace ( ' ' , '%20' ) , 1006 , '' )
    if 17 - 17: o00O0oo / iIii1I11I1II1 - Ooo00oOo00o + OOOo0 % OoOO0ooOOoo0O
    I1i1I1II ( 'tvshows' , 'Media Info 3' )
 if I1I1i != 'Failed' :
  iIII = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( I1I1i )
  for II1I in o0OO0o0o00o :
   if o00o0 in II1I . lower ( ) :
    O0OO0O ( ( '[COLORgreen]' + II1I + ' source 3[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( Ooo0oO + II1I ) . replace ( ' ' , '%20' ) , 1006 , '' )
    if 14 - 14: OOooOOo % IIII + ii11ii1ii + Ooo00oOo00o
    I1i1I1II ( 'tvshows' , 'Media Info 3' )
 if O0O0oo != 'Failed' :
  OoO0o000oOo = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( O0O0oo )
  for II1I in o0OO0o0o00o :
   if o00o0 in II1I . lower ( ) :
    O0OO0O ( ( '[COLORgreen]' + II1I + ' source 4[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( IiIiIIiii1I + II1I ) . replace ( ' ' , '%20' ) , 1006 , '' )
    if 76 - 76: Ooo00oOo00o - i11iIiiIii + I1IiI + OoOO0ooOOoo0O / OoooooooOO
    I1i1I1II ( 'tvshows' , 'Media Info 3' )
 if o00O != 'Failed' :
  Oo00OO00o0oO = re . compile ( '<a href="(.+?)" class="film-image">\n<img src="(.+?)" alt=""/>\n</a>\n<div class="tss-detail">\n<a class="title" style="" href=".+?">\n<span class="position">.+?</span>\n(.+?)</a>' ) . findall ( o00O )
  for I1Ii1iI1 , oOo0 , II1I in Oo00OO00o0oO :
   if o00o0 in II1I . lower ( ) :
    O0OO0O ( '[COLORgreen]' + II1I + ' - Source - Dizi[/COLOR]' , I1Ii1iI1 , 8062 , oOo0 )
    if 50 - 50: OoOoOO00 - O0oO + iIii1I11I1II1 + iIii1I11I1II1
    I1i1I1II ( 'tvshows' , 'Media Info 3' )
 if OooOoOO0OO != 'Failed' :
  I1iiIiiii1111 = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( OooOoOO0OO )
  for I1Ii1iI1 , oOo0 , II1I in I1iiIiiii1111 :
   if o00o0 in II1I . lower ( ) :
    IiI1iiiIii ( ( '[COLORgreen]' + II1I + '- Source Scooby[/COLOR]' ) , I1Ii1iI1 , 222 , 'img' )
    if 91 - 91: OoOoOO00 - O0 . iIii1I11I1II1 . O0 + ii11ii1ii - OoOoOO00
    I1i1I1II ( 'tvshows' , 'Media Info 3' )
 if I1111III11 != 'Failed' :
  iiI1I = re . compile ( '<div class="video_block video_block_default ">.+?<a href="#">.+?<a href="(.*?)".+?<img src="(.+?)" height=".+?" alt="(.+?)"' , re . DOTALL ) . findall ( I1111III11 )
  for I1Ii1iI1 , oOo0 , II1I in iiI1I :
   IiI1iiiIii ( '[COLORgreen]' + II1I + ' - Source DiZzY[/COLOR]' , I1Ii1iI1 , 222 , oOo0 )
 if OOooOooo0OOo0 != 'Failed' :
  iiIiiIi1 = re . compile ( '<img src="(.+?)".+?<a href="(.+?)" title=".+?"><b>(.+?)</b>' , re . DOTALL ) . findall ( OOooOooo0OOo0 )
  for oOo0 , I1Ii1iI1 , II1I in iiIiiIi1 :
   if 'watch online' in II1I :
    pass
   else :
    ooooooO0oo ( '[COLORgreen]' + II1I + '- Source WATCH SERIES[/COLOR]' , 'http://www.watchseries.li' + I1Ii1iI1 , 10044 , oOo0 , '' , '' )
    if 30 - 30: OoOO0ooOOoo0O + OoOoOO00 - IIII * OoooooooOO
    xbmcplugin . setContent ( O00o0OO , 'movies' )
    if 19 - 19: IIII - OOooOOo . iIii1I11I1II1 . I1IiI / OoOO0ooOOoo0O
def OOO0O00Oo ( ) :
 if 13 - 13: iIii1I11I1II1
 o00o0 = Oo0o0000o0o0 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 II1III1I1I1Ii = o00o0 . lower ( )
 I1Ii1iI1 = ( oOo0oooo00o ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz' ) )
 iiI = i1IiiiI1iI ( I1Ii1iI1 )
 ooOOoooooo = re . compile ( '"id":".+?","name":"(.+?)","img":"(.+?)","stream_url3":".+?","cat_id":"(.+?)","stream_url2":".+?","stream_url":".+?"}' , re . DOTALL ) . findall ( iiI )
 for II1I , oOo0 , IiIIII1iiIIi in ooOOoooooo :
  i1I1IiI1ii = oOo0oooo00o ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv' ) + ( oOo0 ) . replace ( '\\' , '' )
  if o00o0 in II1I . lower ( ) :
   O0OO0O ( II1I , '' , 7022 , i1I1IiI1ii )
   if 64 - 64: oO0o0ooO0 * ii11ii1ii % OoOoOO00 - I1IiI + ii11ii1ii
 xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 62 - 62: I1IiI % OOooOOo % OOOo0 + IIII . Ooo00oOo00o
 if 48 - 48: OOOo0 * i11iIiiIii % OoOoOO00
def ii1IOoo000000 ( url ) :
 Oo00ooOoO = cloudflare . source ( url )
 ooOOoooooo = re . compile ( '<a class="season" href="(.+?)">\n(.+?)\n</a>\n</span>\n<span>\n<a class="episode" href=".+?">\n(.+?)\n</a>\n</span>\n<span>\n<a class="episode-name" href=".+?">\n(.+?)</a>' ) . findall ( Oo00ooOoO )
 for url , I11iiIi1i1 , oooOO0OO0O , II1I in ooOOoooooo :
  O0OO0O ( ( I11iiIi1i1 ) . replace ( 'Sezon' , ' Season ' ) + ( oooOO0OO0O ) . replace ( 'Bölüm' , ' Episode ' ) + II1I , url , 8063 , '' )
  if 100 - 100: i11iIiiIii / i11iIiiIii
  if 89 - 89: oO0o0ooO0 . i11iIiiIii * O0
  if 44 - 44: i1IIi . OOOo0 / i11iIiiIii + IIII
  if 27 - 27: OoOO0ooOOoo0O
def O0OO0ooO00 ( url ) :
 Oo00ooOoO = cloudflare . source ( url )
 ooOOoooooo = re . compile ( 'file: "(.+?)",.+?label: "(.+?)",' , re . DOTALL ) . findall ( Oo00ooOoO )
 for url , II1I in ooOOoooooo :
  IiI1iiiIii ( II1I , url , 222 , '' )
  if 83 - 83: iIii1I11I1II1
  if 63 - 63: OoooooooOO * Ooo00oOo00o / o0000oOoOoO0o - OoOO . iIii1I11I1II1 + oO0o0ooO0
  if 44 - 44: i1IIi % OOOo0 % OOooOOo
  if 9 - 9: Oo % OoooooooOO - o00O0oo
def iIII11Iiii1 ( ) :
 if 95 - 95: OOOo0
 Oo00ooOoO = cloudflare . source ( oOo0oooo00o ( 'aHR0cDovL2RpemlsYWIuY29t' ) )
 ooOOoooooo = re . compile ( '<li id=".+?">.+?<a href="(.+?)">.+?<img width="40" height="40" src="(.+?)" alt=""/>.+?<span class="title">\n(.+?)</span>.+?<span class="alt-title">\n(.+?)</span>.+?</a>.+?</li>' , re . DOTALL ) . findall ( Oo00ooOoO )
 for I1Ii1iI1 , oOo0 , II1I , oooOO0OO0O in ooOOoooooo :
  O0OO0O ( II1I + '  -  ' + ( oooOO0OO0O ) . replace ( 'sezon' , 'Season' ) . replace ( 'bölüm' , 'Episode' ) , I1Ii1iI1 , 8063 , oOo0 )
  if 99 - 99: O0
def O0oO0OOoO ( ) :
 OOOOO0oo0O0O0 = oOoO0O0o0Oooo ( oOo0oooo00o ( 'aHR0cDovL3d3dy50dmd1aWRlLmNvLnVrLw==' ) )
 ooOOoooooo = re . compile ( '<a href="(.+?)"  qt-title=".+?" qt-text=".+?<br> .+?" title="(.+?)".+?class=".+? src="(.+?)" alt=".+?" /></a>' , re . DOTALL ) . findall ( OOOOO0oo0O0O0 )
 for I1Ii1iI1 , II1I , oOo0 in ooOOoooooo :
  IiI1iiiIii ( '[COLORgreen]' + II1I + '[/COLOR]' , I1Ii1iI1 , 8002 , oOo0 )
def O00oo ( url ) :
 OOOOO0oo0O0O0 = oOoO0O0o0Oooo ( url )
 ooOOoooooo = re . compile ( '<table border="0".+?url((.+?));background-repeat: no-repeat;">.+?<tr>.+?<span class="season">(.+?)</span><br>.+?<a href="(.+?)"+?>(.+?)</span><br>.+?<span class="programmetext">(.+?)</span></a><br>' , re . DOTALL ) . findall ( OOOOO0oo0O0O0 )
 for oOo0 , time , url , II1I , OOO in ooOOoooooo :
  ooooooO0oo ( '%s %s' % ( '[COLORgreen]' + II1I + '[/COLOR]' , time ) , url , 1015 , oOo0 , OOO )
  if 53 - 53: Ooo00oOo00o % OOooOOo / OoOO0ooOOoo0O % IIII % Ooo00oOo00o % OoooooooOO
def i11i1i ( ) :
 if 10 - 10: o00O0oo - i11iIiiIii . ii11ii1ii % i1IIi
 O0OO0O ( 'Coronation Street' , '' , 8001 , '' )
 O0OO0O ( 'Eastenders' , '' , 8002 , '' )
 O0OO0O ( 'Emmerdale' , '' , 8003 , '' )
 O0OO0O ( 'Hollyoaks' , '' , 8004 , '' )
 O0OO0O ( 'Im a Celebrity' , '' , 8005 , '' )
 if 78 - 78: iIii1I11I1II1 * Oo . Oo - OoOO0ooOOoo0O . iIii1I11I1II1
 if 30 - 30: o0oO0 + o0oO0 % IIII - OOooOOo - ii11ii1ii
 if 36 - 36: o0000oOoOoO0o % OoOO0ooOOoo0O
 if 72 - 72: OOOo0 / oO0o0ooO0 - O0 + o0000oOoOoO0o
def o0iIIIIi ( ) :
 iiI = i1IiiiI1iI ( 'http://uksoapshare.blogspot.co.uk/' )
 ooOOoooooo = re . compile ( '<a href="(.+?)".+?target=_blank>(.+?)</a>' ) . findall ( iiI )
 for I1Ii1iI1 , II1I in ooOOoooooo :
  if 'Holly' in II1I :
   oOo0 = 'http://2.bp.blogspot.com/-9c7Sieh1RKs/UjD6TGAEEnI/AAAAAAAAAC8/84uwHfxcuYg/s1600/Hollyoaks.png'
   if 'huge' in I1Ii1iI1 :
    IiI1iiiIii ( ( II1I ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , I1Ii1iI1 . replace ( '\\/' , '/' ) , 8006 , oOo0 )
   else :
    pass
    if 50 - 50: O0oO + o0oO0 + oO0o0ooO0
 xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE_IGNORE_THE ) ;
 if 15 - 15: o0000oOoOoO0o
def IiiI11I1IIiI ( ) :
 iiI = i1IiiiI1iI ( 'http://uksoapshare.blogspot.co.uk/' )
 ooOOoooooo = re . compile ( '<a href="(.+?)".+?target=_blank>(.+?)</a>' ) . findall ( iiI )
 for I1Ii1iI1 , II1I in ooOOoooooo :
  if 'East' in II1I :
   oOo0 = 'http://3.bp.blogspot.com/-KWHcNbNJU8Y/Vi1ousRl7fI/AAAAAAAAAT8/ksNE12LH0nE/s1600/eastenders.jpg'
   if 'huge' in I1Ii1iI1 :
    IiI1iiiIii ( ( II1I ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , I1Ii1iI1 . replace ( '\\/' , '/' ) , 8006 , oOo0 )
   else :
    pass
    if 5 - 5: Oo
 xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 100 - 100: o00O0oo + iIii1I11I1II1
def o0o0OoO0OOO0 ( ) :
 iiI = i1IiiiI1iI ( 'http://uksoapshare.blogspot.co.uk/' )
 ooOOoooooo = re . compile ( '<a href="(.+?)".+?target=_blank>(.+?)</a>' ) . findall ( iiI )
 for I1Ii1iI1 , II1I in ooOOoooooo :
  if 'Emmer' in II1I :
   oOo0 = 'http://2.bp.blogspot.com/-UfDcxisVV5c/UjH9vUicZ3I/AAAAAAAAADc/8Ozuiz1ojxw/s1600/Emmerdale.jpg'
   if 'huge' in I1Ii1iI1 :
    IiI1iiiIii ( ( II1I ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , I1Ii1iI1 . replace ( '\\/' , '/' ) , 8006 , oOo0 )
   else :
    pass
    if 79 - 79: OoOO % OOooOOo % I1IiI
 xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 45 - 45: OOOo0 * OoOO0ooOOoo0O % Ooo00oOo00o
def i111I11I ( ) :
 iiI = i1IiiiI1iI ( 'http://uksoapshare.blogspot.co.uk/' )
 ooOOoooooo = re . compile ( '<a href="(.+?)".+?target=_blank>(.+?)</a>' ) . findall ( iiI )
 for I1Ii1iI1 , II1I in ooOOoooooo :
  if 'Coro' in II1I :
   oOo0 = 'http://3.bp.blogspot.com/-hofvfBQVexs/UjErIfNdS4I/AAAAAAAAADQ/Q-vVGu3apYU/s1600/corrie.jpg'
   if 'huge' in I1Ii1iI1 :
    IiI1iiiIii ( ( II1I ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , I1Ii1iI1 . replace ( '\\/' , '/' ) , 8006 , oOo0 )
   else :
    pass
    if 80 - 80: iIii1I11I1II1 - OoooooooOO - ii11ii1ii - ii11ii1ii . OoooooooOO
 xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 48 - 48: O0oO . i11iIiiIii / i1IIi % IIII % oO0o0ooO0 + OoOO
def iiII1iiiiiii ( ) :
 iiI = i1IiiiI1iI ( 'http://uksoapshare.blogspot.co.uk/' )
 ooOOoooooo = re . compile ( '<a href="(.+?)" target="_blank">(.+?)</a>' ) . findall ( iiI )
 for I1Ii1iI1 , II1I in ooOOoooooo :
  if 'Celeb' in II1I :
   oOo0 = 'http://3.bp.blogspot.com/-a_yDotWU_pY/VkotKWaG_gI/AAAAAAAAAUk/8Q5iNM6p37k/s1600/iacgoh.jpg'
   if 'huge' in I1Ii1iI1 :
    IiI1iiiIii ( ( II1I ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , I1Ii1iI1 . replace ( '\\/' , '/' ) , 8006 , oOo0 )
   else :
    pass
    if 9 - 9: OoooooooOO + OoOO
def iIiI1ii ( name , url ) :
 O0OooOO = urlresolver . HostedMediaFile ( url ) . valid_url ( )
 if O0OooOO :
  i1i1 = urlresolver . HostedMediaFile ( url ) . resolve ( )
 else :
  OOOOO0oo0O0O0 = open_url ( url )
  url = re . compile ( 'src="(.+?)"></iframe>' ) . findall ( OOOOO0oo0O0O0 ) [ 0 ]
  url = url . split ( '?autoplay' ) [ 0 ]
  OOOOO0oo0O0O0 = open_url ( url )
  o0oOoOo0 = re . compile ( 'mp4","url":"(.+?)"' ) . findall ( OOOOO0oo0O0O0 ) [ - 1 ]
  i1i1 = o0oOoOo0 . replace ( '\\/' , '/' )
 oO00oO = xbmcgui . ListItem ( name , '' , '' )
 oO00oO . setPath ( i1i1 )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , oO00oO )
 if 38 - 38: OOooOOo % O0oO + i11iIiiIii + oO0o0ooO0 + o0oO0 / i11iIiiIii
 if 94 - 94: oO0o0ooO0 - Oo + OoOO
def O0oooOoO ( ) :
 OOOOO0oo0O0O0 = i1IiiiI1iI ( oOo0oooo00o ( 'aHR0cDovL3d3dy5kaXppYm94aGQuY29tLw==' ) )
 ooOOoooooo = re . compile ( 'class="film menu-item menu-item-type-post_type menu-item-object-page menu-item-36980"><a href="(.+?)"><i class="fa fa-film"></i><span>(.+?)</span></a></li>' ) . findall ( OOOOO0oo0O0O0 )
 o0OO0o0o00o = re . compile ( 'class="menu-item menu-item-type-post_type menu-item-object-page menu-item-52949"><a href="(.+?)"><i class="fa fa-"></i><span>(.+?)</span></a></li>' ) . findall ( OOOOO0oo0O0O0 )
 for I1Ii1iI1 , II1I in ooOOoooooo :
  O0OO0O ( ( '[COLORgreen]' + II1I + '[/COLOR]' ) . replace ( 'Diziler' , 'Series' ) , I1Ii1iI1 , 7071 , oOOoO0 + 'popcorn.png' )
 for I1Ii1iI1 , II1I in o0OO0o0o00o :
  O0OO0O ( ( '[COLORgreen]' + II1I + '[/COLOR]' ) . replace ( 'Filmler' , 'Movies' ) , I1Ii1iI1 , 7071 , oOOoO0 + 'popcorn.png' )
  if 62 - 62: OoOO0ooOOoo0O / OoOoOO00 + I1IiI % o0oO0 / I1IiI + ii11ii1ii
def IiI11I111 ( ) :
 OOOOO0oo0O0O0 = i1IiiiI1iI ( oOo0oooo00o ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL2NhdGVnb3JpZXMv' ) )
 ooOOoooooo = re . compile ( '<a class="nav-item" href="(.+?)">(.+?)</a>' ) . findall ( OOOOO0oo0O0O0 )
 for I1Ii1iI1 , II1I in ooOOoooooo :
  if 'Movies' in II1I :
   O0OO0O ( '[COLORgreen]' + II1I + '[/COLOR]' , 'http://www.snagfilms.com' + ( I1Ii1iI1 ) . replace ( 'http://www.snagfilms.com' , '' ) , 7061 , oOOoO0 + 'popcorn.png' )
def Ooo000O00 ( url ) :
 OOOOO0oo0O0O0 = i1IiiiI1iI ( url )
 ooOOoooooo = re . compile ( '<a class="object-link size-poster".+?href="(.+?)" data-type="category">.+?src="(.+?)" alt="Image of (.+?)" />' , re . DOTALL ) . findall ( OOOOO0oo0O0O0 )
 ooOOoooooo = re . compile ( '<a class="object-link size-poster".+?href="(.+?)" data-type="category">.+?src="(.+?)" alt="Image of (.+?)" />' , re . DOTALL ) . findall ( OOOOO0oo0O0O0 )
 o0OO0o0o00o = re . compile ( "<li class='current'>.+?</li><li ><a href='(.+?)'>.+?</a></li><li" , re . DOTALL ) . findall ( OOOOO0oo0O0O0 )
 for url , oOo0 , II1I in ooOOoooooo :
  O0OO0O ( '[COLORgreen]' + II1I + '[/COLOR]' , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7067 , oOo0 )
 for url in o0OO0o0o00o :
  O0OO0O ( '[COLORgreen]NEXT PAGE[/COLOR]' , ( url ) . replace ( '&#038;' , '&' ) , 7063 , oOOoO0 + 'popcorn.png' )
  if 36 - 36: OoOO0ooOOoo0O % i11iIiiIii
  if 47 - 47: i1IIi + OoOoOO00 . Oo * OoOO . o0000oOoOoO0o / i1IIi
def i11iioOOOOO0Ooooo ( url ) :
 OOOOO0oo0O0O0 = i1IiiiI1iI ( oOo0oooo00o ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL2NhdGVnb3JpZXMv' ) )
 ooOOoooooo = re . compile ( '<a class="object-link size-poster".+?href="(.+?)" data-type="category">.+?src="(.+?)" alt="Image of (.+?)" />' , re . DOTALL ) . findall ( OOOOO0oo0O0O0 )
 for url , oOo0 , II1I in ooOOoooooo :
  O0OO0O ( '[COLORgreen]' + II1I + '[/COLOR]' , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7062 , oOo0 )
  if 57 - 57: o00O0oo - OoooooooOO
  if 68 - 68: OOooOOo % ii11ii1ii / O0oO + O0oO - O0oO . Ooo00oOo00o
def oOO00ooOOo ( url ) :
 OOOOO0oo0O0O0 = i1IiiiI1iI ( url )
 ooOOoooooo = re . compile ( 'href="(.+?)".+?src="(.+?)" alt="Image of (.+?)"' , re . DOTALL ) . findall ( OOOOO0oo0O0O0 )
 for url , oOo0 , II1I in ooOOoooooo :
  O0OO0O ( ( '[COLORgreen]' + II1I + '[/COLOR]' ) . replace ( '&#x27;' , '' ) , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7067 , oOo0 )
  if 20 - 20: ii11ii1ii
def IIiiiiIiI1III ( url ) :
 OOOOO0oo0O0O0 = i1IiiiI1iI ( url )
 ooOOoooooo = re . compile ( '<div class="film-container">.+?<iframe src="(.+?)"' , re . DOTALL ) . findall ( OOOOO0oo0O0O0 )
 for url in ooOOoooooo :
  iIiI ( 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) )
  if 80 - 80: OoOO % OoOO % O0 - i11iIiiIii . oO0o0ooO0 / O0
def iIiI ( url ) :
 OOOOO0oo0O0O0 = i1IiiiI1iI ( url )
 ooOOoooooo = re . compile ( 'file: "(.+?)",.+?label: "(.+?)"' , re . DOTALL ) . findall ( OOOOO0oo0O0O0 )
 for url , II1I in ooOOoooooo :
  IiI1iiiIii ( '[COLORgreen]' + II1I + '[/COLOR]' , url , 222 , oOOoO0 + 'popcorn' )
  if 13 - 13: OOOo0 + O0 - ii11ii1ii % Oo / o00O0oo . i1IIi
  if 60 - 60: Oo . IIII % OOOo0 - O0oO
  if 79 - 79: OoooooooOO / ii11ii1ii . O0
  if 79 - 79: OoOO - OoOoOO00
def Ii1iiI1 ( ) :
 OOOOO0oo0O0O0 = i1IiiiI1iI ( oOo0oooo00o ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vc2VjcmV0L2Nsb3VkLnBocA==' ) )
 ooOOoooooo = re . compile ( '<li class="col-sm-2">.+?<a href="#" class="thumbnail" data-src="(.+?)" data-toggle="modal".+?data-target="#infoModal" name="(.+?)"> <img src="(.+?)" alt=".+?" width="130px"' , re . DOTALL ) . findall ( OOOOO0oo0O0O0 )
 for I1Ii1iI1 , II1I , oOo0 in ooOOoooooo :
  IiI1iiiIii ( '[COLORgreen]' + II1I + '[/COLOR]' , 'http://stream.cloudtv.bz/stream/channel/20/' + ( oOo0oooo00o ( I1Ii1iI1 ) ) , 222 , oOo0 )
  if 76 - 76: o00O0oo * iIii1I11I1II1
def iiI1iI ( ) :
 OOOOO0oo0O0O0 = i1IiiiI1iI ( oOo0oooo00o ( 'aHR0cDovL2hkbW92aWUxNC5uZXQv' ) )
 ooOOoooooo = re . compile ( 'title="(.+?)" href="/list/category/(.+?)">' , re . DOTALL ) . findall ( OOOOO0oo0O0O0 )
 for II1I , I1Ii1iI1 in ooOOoooooo :
  O0OO0O ( '[COLORgreen]' + II1I + '[/COLOR]' , 'http://hdmovie14.net/list/category/' + I1Ii1iI1 , 7051 , oOOoO0 + 'vod.png' )
  if 84 - 84: OoooooooOO + O0oO / OOOo0 % OoOO0ooOOoo0O % ii11ii1ii * OOOo0
def OOoO0oooo ( url ) :
 OOOOO0oo0O0O0 = i1IiiiI1iI ( url )
 ooOOoooooo = re . compile ( 'href="(.+?)"><h3>(.+?)</h3>' , re . DOTALL ) . findall ( OOOOO0oo0O0O0 )
 for url , II1I in ooOOoooooo :
  O0OO0O ( '[COLORgreen]' + II1I + '[/COLOR]' , 'http://hdmovie14.net' + url , 7052 , oOOoO0 + 'vod.png' )
  if 24 - 24: o0000oOoOoO0o / OOOo0 * i1IIi % OoooooooOO
def ooiI1i ( url ) :
 OOOOO0oo0O0O0 = i1IiiiI1iI
 ooOOoooooo = re . compile ( 'id:"(.+?)",url:"(.+?)"' , re . DOTALL ) . findall ( OOOOO0oo0O0O0 )
 for url , oOo0 , II1I in ooOOoooooo :
  O0OO0O ( '[COLORgreen]' + II1I + '[/COLOR]' , url , 222 , oOo0 )
  if 3 - 3: IIII / o0000oOoOoO0o
  if 34 - 34: i11iIiiIii / O0oO * OoOO0ooOOoo0O . Oo
  if 79 - 79: O0oO
  if 31 - 31: OoOO0ooOOoo0O % O0oO
  if 98 - 98: IIII * iIii1I11I1II1 . o00O0oo * Oo / ii11ii1ii + o0oO0
def iiI1ii111 ( ) :
 if 97 - 97: O0 / OoOO0ooOOoo0O + OOooOOo . OoOO % I1IiI - I1IiI
 O0OO0O ( 'All Channels' , '' , 7021 , oOOoO0 + 'livetv.png' )
 O0OO0O ( 'Entertainment' , '' , 7021 , oOOoO0 + 'livetv.png' )
 O0OO0O ( 'Movies' , '' , 7021 , oOOoO0 + 'livetv.png' )
 O0OO0O ( 'Music' , '' , 7021 , oOOoO0 + 'livetv.png' )
 O0OO0O ( 'News' , '' , 7021 , oOOoO0 + 'livetv.png' )
 O0OO0O ( 'Sports' , '' , 7021 , oOOoO0 + 'livetv.png' )
 O0OO0O ( 'Documentary' , '' , 7021 , oOOoO0 + 'livetv.png' )
 O0OO0O ( 'Kids' , '' , 7021 , oOOoO0 + 'livetv.png' )
 O0OO0O ( 'Food' , '' , 7021 , oOOoO0 + 'livetv.png' )
 O0OO0O ( 'Religious' , '' , 7021 , oOOoO0 + 'livetv.png' )
 O0OO0O ( 'USA Channels' , '' , 7021 , oOOoO0 + 'livetv.png' )
 O0OO0O ( 'Other' , '' , 7021 , oOOoO0 + 'livetv.png' )
 if 33 - 33: o0000oOoOoO0o % OoOoOO00 + Ooo00oOo00o
 if 93 - 93: i1IIi . IIII / OOOo0 + IIII
def OOooOO ( Cat_Name ) :
 if 59 - 59: Ooo00oOo00o - Ooo00oOo00o + oO0o0ooO0
 iiIIII11iiii = False
 i11i1O00oo00OOOO = '0'
 if Cat_Name == 'All Channels' : iiIIII11iiii = True
 if Cat_Name == 'Entertainment' : i11i1O00oo00OOOO = '1'
 if Cat_Name == 'Movies' : i11i1O00oo00OOOO = '2'
 if Cat_Name == 'Music' : i11i1O00oo00OOOO = '3'
 if Cat_Name == 'News' : i11i1O00oo00OOOO = '4'
 if Cat_Name == 'Sports' : i11i1O00oo00OOOO = '5'
 if Cat_Name == 'Documentary' : i11i1O00oo00OOOO = '6'
 if Cat_Name == 'Kids' : i11i1O00oo00OOOO = '7'
 if Cat_Name == 'Food' : i11i1O00oo00OOOO = '8'
 if Cat_Name == 'Religious' : i11i1O00oo00OOOO = '9'
 if Cat_Name == 'USA Channels' : i11i1O00oo00OOOO = '10'
 if Cat_Name == 'Other' : i11i1O00oo00OOOO = '11'
 if 48 - 48: iIii1I11I1II1 % i1IIi + I1IiI % OOooOOo
 OOOOO0oo0O0O0 = i1IiiiI1iI ( oOo0oooo00o ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz' ) )
 ooOOoooooo = re . compile ( '"id":".+?","name":"(.+?)","img":"(.+?)","stream_url3":".+?","cat_id":"(.+?)","stream_url2":".+?","stream_url":".+?"}' , re . DOTALL ) . findall ( OOOOO0oo0O0O0 )
 print 'Len Match: >>>' + str ( len ( ooOOoooooo ) )
 for II1I , oOo0 , IiIIII1iiIIi in ooOOoooooo :
  i1I1IiI1ii = oOo0oooo00o ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv' ) + ( oOo0 ) . replace ( '\\' , '' )
  if IiIIII1iiIIi == i11i1O00oo00OOOO :
   O0OO0O ( II1I , '' , 7022 , i1I1IiI1ii )
  elif iiIIII11iiii == True :
   O0OO0O ( II1I , '' , 7022 , i1I1IiI1ii )
  else : pass
  if 79 - 79: I1IiI % OOOo0 % o00O0oo / i1IIi % Ooo00oOo00o
  xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 56 - 56: iIii1I11I1II1 - i11iIiiIii * oO0o0ooO0
def o0O0Ooo ( Search_Name ) :
 OOOOO0oo0O0O0 = i1IiiiI1iI ( oOo0oooo00o ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz' ) )
 ooOOoooooo = re . compile ( '"id":".+?","name":"' + Search_Name + '","img":"(.+?)","stream_url3":"(.+?)","cat_id":".+?","stream_url2":"(.+?)","stream_url":"(.+?)"}' , re . DOTALL ) . findall ( OOOOO0oo0O0O0 )
 ooOOoooooo = re . compile ( '"id":".+?","name":"' + Search_Name + '","img":"(.+?)","stream_url3":"(.+?)","cat_id":".+?","stream_url2":"(.+?)","stream_url":"(.+?)"}' , re . DOTALL ) . findall ( OOOOO0oo0O0O0 )
 for oOo0 , I1Ii1iI1 , O0o0OO0000ooo , Ooo0oO in ooOOoooooo :
  i1I1IiI1ii = oOo0oooo00o ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv' ) + ( oOo0 ) . replace ( '\\' , '' )
  IiI1iiiIii ( Search_Name + ': Link 1' , ( I1Ii1iI1 ) . replace ( '\\' , '' ) , 222 , i1I1IiI1ii )
  IiI1iiiIii ( Search_Name + ': Link 2' , ( O0o0OO0000ooo ) . replace ( '\\' , '' ) , 222 , i1I1IiI1ii )
  IiI1iiiIii ( Search_Name + ': Link 3' , ( Ooo0oO ) . replace ( '\\' , '' ) , 222 , i1I1IiI1ii )
  if 79 - 79: o0oO0 . OoOO / OoOO - o0oO0 * Oo / OOooOOo
def iI1iiIi1 ( ) :
 OOOOO0oo0O0O0 = i1IiiiI1iI ( oOo0oooo00o ( oo ( 0 , [ 97 ] , [ 221 , 72 , 245 , 82 , 68 , 48 , 242 , 99 , 143 , 68 , 9 , 111 , 24 , 118 , 180 , 76 , 29 , 51 , 14 , 100 , 187 , 51 , 105 , 100 , 106 , 121 , 52 , 53 , 240 , 114 , 26 , 98 , 252 , 50 , 197 , 82 , 218 , 112 , 19 , 99 , 94 , 71 , 54 , 120 , 104 , 108 , 174 , 101 , 107 , 72 , 168 , 82 , 191 , 50 , 88 , 76 , 90 , 109 , 138 , 78 , 24 , 118 , 89 , 76 , 218 , 110 , 231 , 86 , 105 , 114 , 252 , 76 , 37 , 50 , 36 , 82 , 96 , 118 , 27 , 100 , 120 , 50 , 160 , 53 , 72 , 115 , 200 , 98 , 80 , 50 , 201 , 70 , 114 , 107 , 9 , 99 , 113 , 121 , 127 , 57 , 155 , 106 , 213 , 97 , 194 , 71 , 192 , 70 , 162 , 116 , 27 , 99 , 46 , 71 , 191 , 108 , 4 , 118 , 24 , 98 , 27 , 109 , 105 , 108 , 89 , 119 , 164 , 100 , 88 , 72 , 237 , 89 , 93 , 117 , 40 , 98 , 211 , 84 , 75 , 78 , 216 , 49 ] ) ) )
 ooOOoooooo = re . compile ( '#EXTINF:-1,(.+)\s*(.+)\s*' ) . findall ( OOOOO0oo0O0O0 )
 for II1I , I1Ii1iI1 in ooOOoooooo :
  IiI1iiiIii ( II1I , ( I1Ii1iI1 ) . replace ( '"' , ' ' ) . replace ( '&amp;' , '&' ) . strip ( ) + '|connection=keep-alive' , 222 , oOOoO0 + 'english.png' )
def i1iiiIi1Iii ( ) :
 OOOOO0oo0O0O0 = i1IiiiI1iI ( oOo0oooo00o ( oo ( 0 , [ 97 ] , [ 221 , 72 , 245 , 82 , 68 , 48 , 242 , 99 , 143 , 68 , 9 , 111 , 24 , 118 , 180 , 76 , 29 , 51 , 14 , 100 , 187 , 51 , 105 , 100 , 106 , 121 , 52 , 53 , 240 , 114 , 26 , 98 , 252 , 50 , 197 , 82 , 218 , 112 , 19 , 99 , 94 , 71 , 54 , 120 , 104 , 108 , 174 , 101 , 107 , 72 , 168 , 82 , 191 , 50 , 88 , 76 , 90 , 109 , 138 , 78 , 24 , 118 , 89 , 76 , 218 , 110 , 231 , 86 , 105 , 114 , 252 , 76 , 37 , 50 , 36 , 82 , 96 , 118 , 27 , 100 , 120 , 50 , 160 , 53 , 72 , 115 , 200 , 98 , 80 , 50 , 201 , 70 , 114 , 107 , 9 , 99 , 113 , 121 , 127 , 57 , 155 , 106 , 213 , 97 , 194 , 71 , 192 , 70 , 162 , 116 , 27 , 99 , 46 , 71 , 191 , 108 , 4 , 118 , 24 , 98 , 27 , 109 , 105 , 108 , 89 , 119 , 164 , 100 , 88 , 72 , 237 , 89 , 93 , 117 , 40 , 98 , 211 , 84 , 75 , 78 , 216 , 49 ] ) ) )
 ooOOoooooo = re . compile ( '#EXTINF:-2,(.+)\s*(.+)\s*' ) . findall ( OOOOO0oo0O0O0 )
 for II1I , I1Ii1iI1 in ooOOoooooo :
  IiI1iiiIii ( II1I , ( I1Ii1iI1 ) . replace ( '"' , ' ' ) . replace ( '&amp;' , '&' ) . strip ( ) , 222 , oOOoO0 + 'xxx.png' )
def o0oO0O ( ) :
 OOOOO0oo0O0O0 = i1IiiiI1iI ( oOo0oooo00o ( oo ( 0 , [ 97 , 129 , 72 , 149 , 82 , 100 , 48 , 63 , 99 , 170 , 68 , 159 , 111 , 42 , 118 , 83 , 76 , 128 , 51 , 61 , 100 , 44 , 51 , 201 , 100 , 148 , 121 , 134 , 53 ] , [ 159 , 114 , 70 , 98 , 144 , 50 , 37 , 82 , 253 , 112 , 184 , 99 , 50 , 71 , 154 , 120 , 110 , 108 , 179 , 101 , 250 , 72 , 65 , 82 , 125 , 50 , 52 , 76 , 28 , 109 , 124 , 78 , 191 , 118 , 193 , 76 , 193 , 110 , 145 , 86 , 92 , 114 , 193 , 76 , 41 , 50 , 82 , 82 , 206 , 118 , 32 , 100 , 163 , 50 , 209 , 53 , 191 , 115 , 42 , 98 , 30 , 50 , 237 , 70 , 26 , 107 , 70 , 99 , 64 , 121 , 115 , 57 , 230 , 116 , 32 , 97 , 39 , 88 , 58 , 104 , 38 , 50 , 77 , 98 , 185 , 50 , 86 , 81 , 80 , 117 , 111 , 98 , 226 , 84 , 75 , 78 , 210 , 49 ] ) ) )
 ooOOoooooo = re . compile ( '#EXTINF:.+?,(.+)\s*(.+)\s*' ) . findall ( OOOOO0oo0O0O0 )
 for II1I , I1Ii1iI1 in ooOOoooooo :
  IiI1iiiIii ( II1I , ( I1Ii1iI1 ) . replace ( '"' , ' ' ) . replace ( '&amp;' , '&' ) . strip ( ) , 222 , oOOoO0 + 'vod(1).png' )
  if 61 - 61: OOooOOo - OoOoOO00 % iIii1I11I1II1 . Oo . OOooOOo % O0oO
def o0o0O00o ( url ) :
 url
 Oo00 = xbmcgui . ListItem ( II1I , path = url )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , Oo00 )
 return
 if 46 - 46: ii11ii1ii / O0oO + IIII / OoOO / O0oO / OoOO0ooOOoo0O
 if 73 - 73: o0oO0 + ii11ii1ii
def o0o ( url ) :
 OOOOO0oo0O0O0 = i1IiiiI1iI ( url )
 ooOOoooooo = re . compile ( '<a class=.+?href="(.+?)">.+?<div class="videothumboverlay hidden-xs" id=".+?">(.+?)</div>.+?<div class="videothumbbox"><img src="(.+?)" class="videothumb" alt="(.+?)"></div>' , re . DOTALL ) . findall ( OOOOO0oo0O0O0 )
 o0OO0o0o00o = re . compile ( "<a href='(.+?)' class='paginationnext'>Next &raquo;</a></div>" ) . findall ( OOOOO0oo0O0O0 )
 for url , ii11ii11 , oOo0 , II1I in ooOOoooooo :
  ooooooO0oo ( II1I , 'https://www.fitnessblender.com' + url , 7086 , 'https://www.fitnessblender.com' + oOo0 , '' , ( ii11ii11 ) . replace ( '</p>' , ' ' ) . replace ( '<p>' , ' ' ) )
  I1i1I1II ( 'tvshows' , 'Media Info 3' )
 for url in o0OO0o0o00o :
  O0OO0O ( 'NEXT' , 'https://www.fitnessblender.com' + url , 7085 , oOOoO0 + 'FITNESS.png' )
  if 46 - 46: I1IiI - O0
def O00Ooo ( url ) :
 iiI = i1IiiiI1iI ( url )
 ooOOoooooo = re . compile ( '<div class=\'videowrapper\'><iframe width="700" height="394" src="//www.youtube.com/embed/(.+?)?rel=0&amp;wmode=transparent" frameborder="0"></iframe></div>.+?<div class="col-xs-6 col-md-2 rightborder">(.+?)</div>.+?<p class="videodetailvalue"><img src=\'(.+?)\'/></p>' , re . DOTALL ) . findall ( iiI )
 for url , ii11ii11 , oOo0 in ooOOoooooo :
  i1i ( 'PLAY' , url , 8043 , 'https://www.fitnessblender.com' + oOo0 , '' , ii11ii11 )
  I1i1I1II ( 'tvshows' , 'Media Info 3' )
 O00 = re . compile ( '<h2 class="videodetailheader">Workout Details</h2>(.+?)</div>' , re . DOTALL ) . findall ( iiI )
 for oOoOo0o00o in O00 :
  iIIi1 = ( oOoOo0o00o ) . replace ( '<p>' , '' ) . replace ( '</p>' , '' ) . replace ( '<br />' , '' ) . replace ( '&nbsp;' , '' ) . replace ( '<strong>' , '' ) . replace ( '</strong>' , '' ) . replace ( '"' , '' ) . replace ( '<' , '' ) . replace ( '>' , '' ) . replace ( 'a href' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&rsquo;t' , '' ) . replace ( '&amp;' , '&' )
  ooooooO0oo ( 'INFO' , '' , 7087 , 'https://www.fitnessblender.com' + oOo0 , '' , iIIi1 )
  if 68 - 68: Oo
def ii111I11Ii ( INFO ) :
 i11IiiI1Ii1 ( 'info for workout' , INFO )
 if 23 - 23: oO0o0ooO0 % OoooooooOO / iIii1I11I1II1 + ii11ii1ii / i1IIi / OOooOOo
 if 94 - 94: i1IIi
 if 36 - 36: OOOo0 + Oo
def iIIiiiI1iI1 ( url ) :
 OOOOO0oo0O0O0 = i1IiiiI1iI ( url )
 ooOOoooooo = re . compile ( 'cat-item-.+?"><a href="(.+?)" >(.+?)</a>' ) . findall ( OOOOO0oo0O0O0 )
 for url , II1I in ooOOoooooo :
  O0OO0O ( II1I , url , 9031 , oOOoO0 + 'icon.png' )
def oO00000oO0o0O ( url ) :
 OOOOO0oo0O0O0 = i1IiiiI1iI ( url )
 ooOOoooooo = re . compile ( '<a href="(.+?)" title=".+?" rel="bookmark"><time class="entry-date published updated" datetime=".+?">(.+?)</time></a>' ) . findall ( OOOOO0oo0O0O0 )
 for url , II1I in ooOOoooooo :
  O0OO0O ( II1I , url , 9032 , oOOoO0 + 'icon.png' )
def IIIiI1iI1 ( url ) :
 OOOOO0oo0O0O0 = i1IiiiI1iI ( url )
 ooOOoooooo = re . compile ( '#EXTINF:-.+?,(.+)\s*(.+)\s*' ) . findall ( OOOOO0oo0O0O0 )
 for II1I , url in ooOOoooooo :
  if '://' in II1I :
   pass
   IiI1iiiIii ( ( II1I ) . replace ( '<br />' , '' ) , ( url ) . replace ( '<br />' , '' ) , 222 , oOOoO0 + 'icon.png' )
def IIiIiiii1I1 ( url ) :
 OOOOO0oo0O0O0 = i1IiiiI1iI ( url )
 ooOOoooooo = re . compile ( 'EXTINF:-.+?,(.+)</div></li><li class=".+?"><div class=".+?">(.+?)</div>).findall' ) . findall ( OOOOO0oo0O0O0 )
 for II1I , url in ooOOoooooo :
  IiI1iiiIii ( II1I , url , 222 , oOOoO0 + 'icon.png' )
  if 74 - 74: OoOO / o00O0oo
  if 53 - 53: OoOoOO00 - oO0o0ooO0 . i1IIi / O0oO - i1IIi - OoOO0ooOOoo0O
  if 72 - 72: OOOo0 + i11iIiiIii + O0 * OoooooooOO
def ooO0 ( ) :
 OOOOO0oo0O0O0 = i1IiiiI1iI ( 'http://tvshows.cnfstudio.com/' )
 ooOOoooooo = re . compile ( '<a href="http://tvshows.cnfstudio.com/genre/(.+?)">(.+?)</a>' ) . findall ( OOOOO0oo0O0O0 )
 for I1Ii1iI1 , II1I in ooOOoooooo :
  O0OO0O ( II1I , 'http://tvshows.cnfstudio.com/genre/' + I1Ii1iI1 , 7010 , oOOoO0 + 'icon.png' )
  print '>>>>>>>>>>' + I1Ii1iI1
  if 94 - 94: o0000oOoOoO0o . OOOo0
def oooOoo0OoOO0000 ( url ) :
 OOOOO0oo0O0O0 = i1IiiiI1iI ( url )
 ooOOoooooo = re . compile ( '<div class="movie">.+?<img src="(.+?)" alt=".+?" />.+?<a href="(.+?)"><span class="player"></span></a>.+?<h2>(.+?)</h2>' , re . DOTALL ) . findall ( OOOOO0oo0O0O0 )
 i11Ii1iIIIIi = re . compile ( "<link rel='prev' href='(.+?)'/>" ) . findall ( OOOOO0oo0O0O0 )
 next = re . compile ( "<link rel='next' href='(.+?)'/>" ) . findall ( OOOOO0oo0O0O0 )
 for oOo0 , url , II1I in ooOOoooooo :
  O0OO0O ( ( II1I ) . replace ( '&#038;' , '' ) . replace ( '&#8216;' , '' ) . replace ( '&#8217;' , '' ) . replace ( '&#8211;' , '' ) , url , 7011 , oOo0 )
 i11Ii1iIIIIi = i11Ii1iIIIIi
 for url in i11Ii1iIIIIi :
  O0OO0O ( 'Prev' , url , 7010 , '' )
 next = next
 for url in next :
  O0OO0O ( 'Next' , url , 7010 , '' )
  if 14 - 14: OoooooooOO . OOooOOo . o0000oOoOoO0o
def I1IIIIIi1IIiI ( url ) :
 OOOOO0oo0O0O0 = i1IiiiI1iI ( url )
 ooOOoooooo = re . compile ( '<li>.+?<a href="(.+?)" target="_blank">.+?<span class="datex">(.+?)</span>.+?</b>(.+?)</span>.+?</li>' , re . DOTALL ) . findall ( OOOOO0oo0O0O0 )
 for url , oooOO0OO0O , II1I in ooOOoooooo :
  IiI1iiiIii ( ( 'Season' ) + oooOO0OO0O + ( '  ' ) + II1I , url , 7004 , oOOoO0 + 'icon.png' )
  if 26 - 26: OOooOOo % OoOO0ooOOoo0O + OoOO0ooOOoo0O % o0000oOoOoO0o * i11iIiiIii / oO0o0ooO0
def OOoO0oO00o ( url ) :
 if 78 - 78: Oo * O0oO - OoooooooOO - Ooo00oOo00o
 OOOOO0oo0O0O0 = i1IiiiI1iI ( url )
 ooOOoooooo = re . compile ( '<div id="play-1".+?src="(.+?)" scrolling="no".+?<li><a href="#play-1">(.+?)</a></li>' , re . DOTALL ) . findall ( OOOOO0oo0O0O0 )
 for url , II1I in ooOOoooooo :
  O0OO0O ( II1I , ( url + '&fv=&sou=' ) . replace ( 'player' , 'watch' ) , 7000 , oOOoO0 + 'icon.png' )
  if 83 - 83: o0oO0 / OoOO0ooOOoo0O
def i11iI1 ( name , url , img ) :
 iiI = i1IiiiI1iI ( url )
 i1Ii11ii1I = re . compile ( '<iframe class="playerframe" src="(.+?)" scrolling=".+?" marginwidth=".+?" marginheight=".+?" vspace=".+?" hspace=".+?" allowfullscreen=".+?" webkitallowfullscreen=".+?" mozallowfullscreen=".+?" width=".+?" height=".+?" frameborder=".+?"></iframe>' , re . DOTALL ) . findall ( iiI )
 OO0oI1iii1i = len ( i1Ii11ii1I )
 if 91 - 91: OoOO - OoooooooOO * OoOoOO00
 if 38 - 38: ii11ii1ii + I1IiI
 if OO0oI1iii1i == 1 :
  for o0IiIiI111IIII1 in i1Ii11ii1I :
   o0IiIiI111IIII1 = o0IiIiI111IIII1 . replace ( 'player' , 'watch' )
   OOOoOooO000oO = o0IiIiI111IIII1 + '&fv=&sou='
   o0OOOOOo00 = i1IiiiI1iI ( OOOoOooO000oO )
   oo0oOO = re . compile ( '<source src="(.+?)" type=".+?">' , re . DOTALL ) . findall ( o0OOOOOo00 )
   for o0O0OO in oo0oOO :
    IIO000oooOO0Oo0 = False
    Resolve ( o0O0OO )
    if 31 - 31: IIII - Ooo00oOo00o / OoOO0ooOOoo0O . i1IIi / o00O0oo
 elif OO0oI1iii1i > 1 :
  if 66 - 66: Ooo00oOo00o
  for o0IiIiI111IIII1 in i1Ii11ii1I :
   o00ooO0ooO0o0 = i1IiiiI1iI ( o0IiIiI111IIII1 )
   OOOO00OOO00 = re . compile ( '<iframe width=".*?" height=".*?" frameborder=".*?" src="(.*?)" scrolling=".*?" marginwidth=".*?" marginheight=".*?" vspace=".*?" hspace=".*?" allowfullscreen=".*?" webkitallowfullscreen=".*?" mozallowfullscreen=".*?"></iframe>' , re . DOTALL ) . findall ( o00ooO0ooO0o0 )
   ii1 = OOOO00OOO00
   ii1 = ( str ( ii1 ) ) . replace ( '[\'' , '' ) . replace ( '\']' , '' ) ;
   print 'Stripped url : ' + ii1
   IiI1iiiIii ( 'DOUBLE LINK' , ii1 , 424 , '' )
   if 94 - 94: Oo . o0oO0 * i11iIiiIii - OOooOOo . oO0o0ooO0
   for url in OOOO00OOO00 :
    O0OO0O ( 'DOUBLE LINK' , url , 424 , '' )
    try :
     O0o0OO0000ooo = Google . resolve ( url )
    except :
     pass
    try :
     o00OOo = re . findall ( r"{'url': u'(.*?)', 'quality': 'HD'}, {'url': u'(.*?)', 'quality': 'SD'}" , str ( O0o0OO0000ooo ) )
     for Ii11III , I1Ii1i11I1I in o00OOo :
      if 71 - 71: OOOo0 * i1IIi % o0000oOoOoO0o
      HD_URLS . append ( Ii11III )
      SD_URLS . append ( I1Ii1i11I1I )
    except :
     pass
 else :
  pass
  if 82 - 82: IIII . I1IiI / o0oO0 + oO0o0ooO0 - o0oO0
def o00OOo0o0O ( ) :
 if 14 - 14: oO0o0ooO0 - o0000oOoOoO0o * OoooooooOO + OoOO0ooOOoo0O . OoOoOO00
 if 15 - 15: o0000oOoOoO0o % i11iIiiIii
 O0OO0O ( 'Genres' , 'http://cnfstudio.com/movies/' , 7002 , oOOoO0 + 'Movies.png' )
 if 73 - 73: o0oO0 % o0oO0 . oO0o0ooO0 + O0oO
 O0OO0O ( 'Search Movies' , '' , 7017 , oOOoO0 + 'Movies.png' )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 10 - 10: O0 / OoOO0ooOOoo0O * o0oO0 - Ooo00oOo00o - i1IIi . I1IiI
 if 69 - 69: Oo - o00O0oo % o00O0oo - OoOO0ooOOoo0O * OoOO0ooOOoo0O / Oo
def i1IiIIi ( ) :
 OOOOO0oo0O0O0 = i1IiiiI1iI ( 'http://cnfstudio.com/' )
 ooOOoooooo = re . compile ( '<a href="http://cnfstudio.com/genre/(.+?)">(.+?)</a>' ) . findall ( OOOOO0oo0O0O0 )
 for I1Ii1iI1 , II1I in ooOOoooooo :
  O0OO0O ( II1I , 'http://cnfstudio.com/genre/' + I1Ii1iI1 , 7003 , oOOoO0 + 'icon.png' )
  if 75 - 75: I1IiI / Ooo00oOo00o - O0 - O0oO . o00O0oo
ii11iIi1I = xbmcgui . Dialog ( )
if 19 - 19: ii11ii1ii . oO0o0ooO0 - OOooOOo + o0000oOoOoO0o - o00O0oo
if 13 - 13: IIII * ii11ii1ii / ii11ii1ii / iIii1I11I1II1 % iIii1I11I1II1
def i1i1IIII ( url ) :
 OOOOO0oo0O0O0 = i1IiiiI1iI ( url )
 ooOOoooooo = re . compile ( '<div class="movie">.+?<img src="(.+?)" alt=".+?" />.+?<a href="(.+?)"><span class="player"></span></a>.+?<h2>(.+?)</h2>' , re . DOTALL ) . findall ( OOOOO0oo0O0O0 )
 i11Ii1iIIIIi = re . compile ( "<link rel='next' href='(.+?)'/>" ) . findall ( OOOOO0oo0O0O0 )
 for oOo0 , url , II1I in ooOOoooooo :
  IiI1iiiIii ( ( II1I ) . replace ( '&#038;' , '' ) . replace ( '&#8216;' , '' ) . replace ( '&#8217;' , '' ) . replace ( '&#8211;' , '' ) , url , 7004 , oOo0 )
 i11Ii1iIIIIi = i11Ii1iIIIIi
 for url in i11Ii1iIIIIi :
  O0OO0O ( 'Next Page' , url , 7003 , '' )
  if 95 - 95: OOOo0
def OOOO0O0OOoo ( url ) :
 if 82 - 82: OoOoOO00 / oO0o0ooO0
 OOOOO0oo0O0O0 = i1IiiiI1iI ( url )
 ooOOoooooo = re . compile ( '<div id="play-1" class="player-content"><iframe class="playerframe" src="(.+?)" scrolling="no".+?</div>' , re . DOTALL ) . findall ( OOOOO0oo0O0O0 )
 for url in ooOOoooooo :
  IIiIi1iI = url + '&fv=&sou='
  IIiIi1iI = IIiIi1iI . replace ( 'player' , 'watch' )
  OOoO = i1IiiI ( IIiIi1iI )
  O0OOO0 = i1IiiI ( url )
  if 61 - 61: o0oO0 . i11iIiiIii + OoOO
  if 8 - 8: iIii1I11I1II1
def i1IiiI ( url ) :
 if 55 - 55: OoOO
 OOOOO0oo0O0O0 = i1IiiiI1iI ( url )
 ooOOoooooo = re . compile ( '<video id=".+?<source src="(.+?)" type="video/mp4">' , re . DOTALL ) . findall ( OOOOO0oo0O0O0 )
 for url in ooOOoooooo :
  ii ( url )
  if 37 - 37: IIII / i11iIiiIii / Oo
  if 97 - 97: O0oO . o0000oOoOoO0o / OOOo0
def o00OO0o0 ( ) :
 ooooooO0oo ( '[COLORgreen]Local M3u[/COLOR]' , i1iiIIiiI111 , 2001 , oOOoO0 + 'loader.png' , OOooO0OOoo , '' )
 ooooooO0oo ( '[COLORgreen]Remote M3u[/COLOR]' , oO , 1009 , oOOoO0 + 'loader.png' , OOooO0OOoo , '' )
 if 39 - 39: o0oO0 % ii11ii1ii - oO0o0ooO0
def iIi1i111 ( url ) :
 ooOOoooooo = re . compile ( '^#EXTINF:-?[0-9]*(.*?),(.*?)\n(.*?)$' , re . I + re . M + re . U + re . S ) . findall
 for Ii11IiI111 , II1I , url in ooOOoooooo :
  IiI1iiiIii ( II1I , url , 222 , oOOoO0 + 'streams.png' )
  if 31 - 31: Ooo00oOo00o * O0 / o0000oOoOoO0o . OoooooooOO * o0000oOoOoO0o . ii11ii1ii
  if 50 - 50: Ooo00oOo00o * o0000oOoOoO0o - OOooOOo + IIII * Ooo00oOo00o % OoOO
def O00o0000OO ( ) :
 ooooooO0oo ( '[COLORgreen]CATAGORIES[/COLOR]' , '' , 10051 , oOOoO0 + 'loader.png' , OOooO0OOoo , '' )
 ooooooO0oo ( '[COLORgreen]SEARCH[/COLOR]' , '' , 10052 , oOOoO0 + 'loader.png' , OOooO0OOoo , '' )
 if 61 - 61: IIII % i1IIi - oO0o0ooO0 . o0oO0 - Oo + Oo
 if 12 - 12: OOooOOo / iIii1I11I1II1 % OoOoOO00 / o0000oOoOoO0o / i1IIi - OOOo0
o0oOoO00o = xbmcaddon . Addon ( id = 'plugin.video.GenieTv' )
Oo0o0000o0o0 = xbmcgui . Dialog ( )
iI111I11I1I1 = xbmc . translatePath ( 'special://home/' )
i1111 = xbmcgui . DialogProgress ( )
OoOOOOOoOo0 = 'https://addons.tvaddons.ag/'
if 19 - 19: I1IiI . OOooOOo . OoooooooOO
def iIiii1iI1i ( ) :
 o00o0 = Oo0o0000o0o0 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 II1III1I1I1Ii = o00o0 . lower ( )
 ooOOooo0ooo00 = 'https://addons.tvaddons.ag/search/?keyword=' + II1III1I1I1Ii
 iiI = i1IiiiI1iI ( ooOOooo0ooo00 )
 ooOOoooooo = re . compile ( '<li><a href="(.+?)"><span class=".+?"><img src="(.+?)" width=".+?" alt=".+?" class=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( iiI )
 for I1Ii1iI1 , oO0 , II1I in ooOOoooooo :
  ooooooO0oo ( II1I , I1Ii1iI1 , 10054 , 'https://addons.tvaddons.ag/' + oO0 , OOooO0OOoo , '' )
  if 36 - 36: IIII + OoooooooOO / i11iIiiIii
  if 40 - 40: OoooooooOO * I1IiI / OoOoOO00 - ii11ii1ii + o00O0oo
def o0O00OooooO ( ) :
 iiI = i1IiiiI1iI ( OoOOOOOoOo0 )
 ooOOoooooo = re . compile ( '<li><a href="(.+?)"><span class="thumbnail"><img src="(.+?)" class="pic" alt=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( iiI )
 for I1Ii1iI1 , oOo0 , II1I in ooOOoooooo :
  if 'Repositories' in II1I :
   pass
  elif 'Services' in II1I :
   pass
  elif 'International' in II1I :
   pass
  else :
   ooooooO0oo ( '[COLORgreen]' + II1I + '[/COLOR]' , I1Ii1iI1 , 10053 , 'https://addons.tvaddons.ag/' + oOo0 , OOooO0OOoo , '' )
   if 77 - 77: OOOo0 % o0oO0
   if 74 - 74: I1IiI / i1IIi % OoooooooOO
def Addon ( url ) :
 iiI = i1IiiiI1iI ( url )
 o00o0o000Oo = re . compile ( '<li class="nextPage"><a class=".+?" href="(.+?)"><dfn title="next Page">.+?</dfn></a></li>' ) . findall ( iiI )
 for url in o00o0o000Oo :
  ooooooO0oo ( '[COLORgreen]NEXT PAGE[/COLOR]' , 'https://addons.tvaddons.ag' + url , 10053 , oOOoO0 + 'streams.png' , OOooO0OOoo , '' )
 ooOOoooooo = re . compile ( '<li><a href="(.+?)"><span class=".+?"><img src="(.+?)" width=".+?" alt=".+?" class=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( iiI )
 for url , oOo0 , II1I in ooOOoooooo :
  if 'Please' in II1I :
   pass
  else :
   ooooooO0oo ( II1I , url , 10054 , 'https://addons.tvaddons.ag/' + oOo0 , OOooO0OOoo , '' )
   if 100 - 100: i1IIi - i11iIiiIii . O0oO * Ooo00oOo00o
   if 62 - 62: O0
def iiIIIIiii ( url , name ) :
 iiI = i1IiiiI1iI ( url )
 ooOOoooooo = re . compile ( '<a href="(.+?)"' ) . findall ( iiI )
 for url in ooOOoooooo :
  if 'plugin' in url :
   print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<' + url
   OO = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
   i1111 = xbmcgui . DialogProgress ( )
   i1111 . create ( "Origin+Jaybox" , "Downloading Content" , '' , 'Please Wait' )
   O0O0OOOOoo = os . path . join ( OO , name + '.zip' )
   try :
    os . remove ( O0O0OOOOoo )
   except :
    pass
   downloader . download ( url , O0O0OOOOoo , i1111 )
   iIIIiIi = xbmc . translatePath ( os . path . join ( 'special://home' , 'addons' ) )
   time . sleep ( 2 )
   i1111 . update ( 0 , "" , "Extracting Zip Please Wait" )
   print '======================================='
   print iIIIiIi
   print '======================================='
   extract . all ( O0O0OOOOoo , iIIIiIi , i1111 )
   OO0O0 ( )
   if 36 - 36: i11iIiiIii / O0 . o0000oOoOoO0o
def OO0O0 ( ) :
 xbmc . executebuiltin ( 'UpdateLocalAddons' )
 xbmc . executebuiltin ( 'UpdateAddonRepos' )
 ii11iIi1I = xbmcgui . Dialog ( )
 ii11iIi1I . ok ( "Origin + Genie TV" , '' , '                                 REFRESH SUCCESSFUL :)' , "                          [COLOR gold]Brought To You By Origin + Jaybox[/COLOR]" )
 return
 if 22 - 22: iIii1I11I1II1 * O0oO / Oo
 if 31 - 31: i11iIiiIii
def O0O0O ( ) :
 OOOOO0oo0O0O0 = oOoO0O0o0Oooo ( oOo0oooo00o ( 'aHR0cDovL3Njb29ieXN0cmVhbS54MTBob3N0LmNvbS9zY29vYnkvc2NyYXBlZC9jYXRzLnBocA==' ) )
 ooOOoooooo = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( OOOOO0oo0O0O0 )
 for I1Ii1iI1 , oO0 , II1I in ooOOoooooo :
  O0OO0O ( II1I , I1Ii1iI1 , 1007 , oO0 )
def II1io0Oo00oOO ( url ) :
 OOOOO0oo0O0O0 = oOoO0O0o0Oooo ( url )
 ooOOoooooo = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( OOOOO0oo0O0O0 )
 for url , oO0 , II1I in ooOOoooooo :
  O0OO0O ( '[COLORgreen]' + II1I + '[/COLOR]' , url , 1006 , oO0 )
  if 73 - 73: o0000oOoOoO0o / OoooooooOO . OoOoOO00 - IIII * o0oO0 * IIII
  if 45 - 45: O0 * O0oO + i11iIiiIii - OoOO0ooOOoo0O - iIii1I11I1II1
def I11I111i1I1 ( url ) :
 OOOOO0oo0O0O0 = oOoO0O0o0Oooo ( url )
 ooOOoooooo = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( OOOOO0oo0O0O0 )
 for url , O0i1II1Iiii1I11 , ii11ii11 , IIIIiiIiI , II1I in ooOOoooooo :
  if '.php' in url :
   IiII1II11I ( II1I , url , 1016 , O0i1II1Iiii1I11 , IIIIiiIiI , ii11ii11 )
   I1i1I1II ( 'tvshows' , 'Media Info 3' )
  else :
   i1i1IIiiIIi1I ( II1I , url , 222 , O0i1II1Iiii1I11 , IIIIiiIiI , ii11ii11 )
   I1i1I1II ( 'tvshows' , 'Media Info 3' )
   if 41 - 41: OoooooooOO / i1IIi
 else :
  ooOOoooooo = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( OOOOO0oo0O0O0 )
  for url , oO0 , II1I in ooOOoooooo :
   if '.php' in url :
    O0OO0O ( II1I , url , 1016 , oO0 )
   else :
    IiI1iiiIii ( II1I , url , 222 , oO0 )
    if 70 - 70: I1IiI % OOooOOo % i1IIi / ii11ii1ii % i11iIiiIii / i1IIi
  xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 4 - 4: IIII
def oOo0OoOOOo0 ( ) :
 OOOOO0oo0O0O0 = oOoO0O0o0Oooo ( oOo0oooo00o ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vdm9kL3VybHMvdXJsLnBocA==' ) )
 ooOOoooooo = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( OOOOO0oo0O0O0 )
 for I1Ii1iI1 , oO0 , II1I in ooOOoooooo :
  O0OO0O ( II1I , I1Ii1iI1 , 1007 , oO0 )
def OOoo00 ( url ) :
 OOOOO0oo0O0O0 = oOoO0O0o0Oooo ( url )
 ooOOoooooo = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( OOOOO0oo0O0O0 )
 for url , oO0 , II1I in ooOOoooooo :
  O0OO0O ( '[COLORgreen]' + II1I + '[/COLOR]' , url , 1006 , oO0 )
  if 22 - 22: o0oO0 / o0oO0 - o00O0oo % o0000oOoOoO0o . OoOO0ooOOoo0O + IIII
def OooO00oo0O0 ( name , url , iconimage = None ) :
 print '--- Playing "{0}". {1}' . format ( name , url )
 i1iIOo = xbmcgui . ListItem ( path = url , thumbnailImage = iconimage )
 i1iIOo . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , i1iIOo )
 if 18 - 18: O0 - i1IIi . O0oO
 if 98 - 98: OOooOOo
def OOo00Oooo ( url ) :
 OOOOO0oo0O0O0 = oOoO0O0o0Oooo ( url )
 ooOOoooooo = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( OOOOO0oo0O0O0 )
 for url , oOo0 , II1I in ooOOoooooo :
  O0OO0O ( '[COLORgreen]' + II1I + '[/COLOR]' , url , 1006 , oOo0 )
def I1 ( url ) :
 OOOOO0oo0O0O0 = oOoO0O0o0Oooo ( url )
 oo0OoOOooO = url
 ooOOoooooo = re . compile ( "<a href='(.+?)'>(.+?)</a>" ) . findall ( OOOOO0oo0O0O0 )
 for url , II1I in ooOOoooooo :
  if '.mp3' in II1I :
   print '<<<<<<<<<<<<<<<<<<<' + url + '>>>>>>>>>>>>>>>>>>>>>>>>>>>'
   IiI1iiiIii ( ( II1I ) . replace ( '.mp3' , '' ) . replace ( '/' , '' ) , 'http://hypem.com' + url , 222 , oOOoO0 + 'music.png' )
  else :
   O0OO0O ( ( II1I ) . replace ( '/' , '' ) , oo0OoOOooO + url , 1011 , oOOoO0 + 'music.png' )
def oO0oOOOooo ( ) :
 OOOOO0oo0O0O0 = oOoO0O0o0Oooo ( oOo0oooo00o ( 'aHR0cDovL3d3dy5jeW4ubmV0L211c2ljLw==' ) )
 ooOOoooooo = re . compile ( '<td><a href="(.+?)"><img src="(.+?)"><br>(.+?)</a></td>' , re . DOTALL ) . findall ( OOOOO0oo0O0O0 )
 for I1Ii1iI1 , oOo0 , II1I in ooOOoooooo :
  O0OO0O ( II1I , ( 'http://www.cyn.net/music/' + I1Ii1iI1 ) . replace ( ' ' , '%20' ) , 1031 , ( 'http://www.cyn.net/music/' + oOo0 ) . replace ( ' ' , '%20' ) )
def Ii1iiI1i1 ( url , img ) :
 OOOOO0oo0O0O0 = oOoO0O0o0Oooo ( url )
 O0o0OO0000ooo = url
 img = img
 ooOOoooooo = re . compile ( '<a href="(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( OOOOO0oo0O0O0 )
 for url , II1I in ooOOoooooo :
  IiI1iiiIii ( ( II1I ) . replace ( '.mp3' , '' ) , ( O0o0OO0000ooo + '/' + url ) . replace ( ' ' , '%20' ) , 222 , img )
  if 3 - 3: OoOO0ooOOoo0O . IIII / Oo
  if 89 - 89: OoooooooOO . iIii1I11I1II1 . Oo * iIii1I11I1II1 - O0oO
def OoOO0o0o0 ( ) :
 O0OO0OO = ( oOo0oooo00o ( 'aHR0cDovL2h5cGVtLmNvbS9kb3dubG9hZC8=' ) )
 o00o0 = Oo0o0000o0o0 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 II1III1I1I1Ii = o00o0 . lower ( )
 I1Ii1iI1 = ( oOo0oooo00o ( 'aHR0cDovL3Bhbmljc3RyZWFtLm5ldC9zdHJlYW1zLw==' ) )
 O0o0OO0000ooo = ( oOo0oooo00o ( 'aHR0cDovL21hc2xvdmQubm8taXAub3JnL3B1YmxpYy9tcDMv' ) )
 Ooo0oO = ( oOo0oooo00o ( 'aHR0cDovL3d3dy5jeW4ubmV0L211c2ljLw==' ) )
 if 35 - 35: O0oO
 iiI = o0OOOOO0 ( I1Ii1iI1 )
 II1iIi1IiIii = o0OOOOO0 ( O0o0OO0000ooo )
 I1I1i = o0OOOOO0 ( Ooo0oO )
 if 67 - 67: o0000oOoOoO0o % i11iIiiIii . iIii1I11I1II1 * OOOo0 - o0000oOoOoO0o + o00O0oo
 if iiI != 'Failed' :
  ooOOoooooo = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( iiI )
  for II1I in ooOOoooooo :
   if o00o0 in II1I . lower ( ) :
    O0OO0O ( ( II1I + ' source 1' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( I1Ii1iI1 + II1I ) . replace ( ' ' , '%20' ) , 1006 , '' )
    if 48 - 48: ii11ii1ii
    I1i1I1II ( 'tvshows' , 'Media Info 3' )
 if II1iIi1IiIii != 'Failed' :
  o0OO0o0o00o = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( iiI )
  for II1I in o0OO0o0o00o :
   if o00o0 in II1I . lower ( ) :
    O0OO0O ( ( II1I + ' source 2' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( O0o0OO0000ooo + II1I ) . replace ( ' ' , '%20' ) , 1006 , '' )
    if 96 - 96: o0oO0 . OoooooooOO
    I1i1I1II ( 'tvshows' , 'Media Info 3' )
 if I1I1i != 'Failed' :
  iIII = re . compile ( '<td><a href=".+?"><img src=".+?"><br>(.+?)</a></td>' , re . DOTALL ) . findall ( I1I1i )
  for II1I in iIII :
   if o00o0 in II1I . lower ( ) :
    O0OO0O ( ( II1I + ' source 3' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( Ooo0oO + II1I ) . replace ( ' ' , '%20' ) , 1031 , '' )
    if 39 - 39: OoOO0ooOOoo0O + Ooo00oOo00o
    I1i1I1II ( 'tvshows' , 'Media Info 3' )
    if 80 - 80: OoOO0ooOOoo0O % Ooo00oOo00o / I1IiI
    if 54 - 54: Oo % Ooo00oOo00o - OoOO0ooOOoo0O - o0000oOoOoO0o
    if 71 - 71: o0oO0 . i11iIiiIii
    if 56 - 56: O0 * oO0o0ooO0 + oO0o0ooO0 * iIii1I11I1II1 / o0oO0 * O0oO
    if 25 - 25: iIii1I11I1II1 . o0000oOoOoO0o * i11iIiiIii + Oo * o0000oOoOoO0o
    if 67 - 67: oO0o0ooO0
def oooO0o ( ) :
 OOOOO0oo0O0O0 = i1IiiiI1iI ( 'http://www.animetoon.org/cartoon' )
 ooOOoooooo = re . compile ( '<td><a href="(.+?)">(.+)</a></td>' ) . findall ( OOOOO0oo0O0O0 )
 for I1Ii1iI1 , II1I in ooOOoooooo :
  O0OO0O ( II1I , I1Ii1iI1 , 1002 , oOOoO0 + 'anime.png' )
  if 19 - 19: OoOO0ooOOoo0O % Ooo00oOo00o / o00O0oo + OoOoOO00 % OoooooooOO
  if 89 - 89: o00O0oo
  if 51 - 51: oO0o0ooO0
def O00O0Oo0 ( url ) :
 OOOOO0oo0O0O0 = i1IiiiI1iI ( url )
 o0OO0o0o00o = re . compile ( '<img src="(.+?)" id="series_image" width="250" height="370" alt=".+?" />' ) . findall ( OOOOO0oo0O0O0 )
 for oOo0 in o0OO0o0o00o :
  iIIIiiI1i1i = oOo0
 iIII = re . compile ( '<li><a href="(.+?)">Next</a></li>' ) . findall ( OOOOO0oo0O0O0 )
 for url in iIII :
  O0OO0O ( 'NEXT PAGE' , url , 1002 , iIIIiiI1i1i )
 ooOOoooooo = re . compile ( '&nbsp;<a href="(.+?)">(.+?)</a>' ) . findall ( OOOOO0oo0O0O0 )
 for url , II1I in ooOOoooooo :
  O0OO0O ( II1I , url , 1003 , iIIIiiI1i1i )
 xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
def OoO ( url , IMAGE ) :
 OOOOO0oo0O0O0 = i1IiiiI1iI ( url )
 ooOOoooooo = re . compile ( '"playlist">(.+?)</span></div><div><iframe src="(.+?)"' ) . findall ( OOOOO0oo0O0O0 )
 for II1I , url in ooOOoooooo :
  print II1I + '     ' + url
  if 'easy' in url :
   iI11IiI1i1 ( url )
  elif 'playpanda' in url :
   iI11IiI1i1 ( url )
   if 65 - 65: O0 . OoOO
  xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
def iI11IiI1i1 ( url ) :
 OOOOO0oo0O0O0 = i1IiiiI1iI ( url )
 ooOOoooooo = re . compile ( "url: '(.+?)'," ) . findall ( OOOOO0oo0O0O0 )
 for url in ooOOoooooo :
  IiI1iiiIii ( 'STREAM' , url , 222 , oOOoO0 + 'anime.png' )
  if 85 - 85: OoOoOO00
  if 55 - 55: ii11ii1ii
def oOoo0OO0 ( url ) :
 Ooo0Oo0o = urllib2 . Request ( url )
 Ooo0Oo0o . add_header ( 'User-Agent' , "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0" )
 Ooo0Oo0o . add_header ( 'referer' , url )
 oo0Oo0 = urllib2 . urlopen ( Ooo0Oo0o )
 IIiIi1iI = oo0Oo0 . read ( )
 oo0Oo0 . close ( )
 return IIiIi1iI
 if 5 - 5: i11iIiiIii * Oo
def oOoO0O0o0Oooo ( url ) :
 Ooo0Oo0o = urllib2 . Request ( url )
 Ooo0Oo0o . add_header ( 'User-Agent' , "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0" )
 oo0Oo0 = urllib2 . urlopen ( Ooo0Oo0o )
 IIiIi1iI = oo0Oo0 . read ( )
 oo0Oo0 . close ( )
 return IIiIi1iI
 if 29 - 29: o00O0oo / o0oO0 % o0000oOoOoO0o
def ii1iIII1ii ( url ) :
 xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
 I1Ii = ( '%s%s' % ( oOOIi1II , url ) )
 IIiIi1iI = oOoO0O0o0Oooo ( url )
 ooOOoooooo = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( IIiIi1iI )
 for url , oO0 , II1I in ooOOoooooo :
  IiI1iiiIii ( '%s' % ( II1I ) . replace ( 'GenieTv' , '[COLOR green]GenieTV[/COLOR]' ) . replace ( '.' , ' ' ) . replace ( 'mp4' , '' ) . replace ( 'mkv' , '' ) . replace ( '_' , ' ' ) , '%s' % ( url ) , 222 , oO0 )
  if 47 - 47: o0000oOoOoO0o . oO0o0ooO0 * o00O0oo - o0oO0 . o0000oOoOoO0o - OoOO0ooOOoo0O
def ii ( url ) :
 iiiii11I1 = xbmc . Player ( Ii1 ( ) )
 import urlresolver
 try : iiiii11I1 . play ( url )
 except : pass
 from urlresolver import common
 i1111 = xbmcgui . DialogProgress ( )
 i1111 . create ( 'LOADING' , 'Opening %s Now' % ( II1I ) )
 iiiii11I1 = xbmc . Player ( Ii1 ( ) )
 url = urlresolver . HostedMediaFile ( url ) . resolve ( )
 if i1111 . iscanceled ( ) :
  print "[COLORred]STREAM CANCELLED[/COLOR]"
  ii11iIi1I = xbmcgui . Dialog ( )
  if ii11iIi1I . yesno ( "[B]CANCELLED[/B]" , '[B]Was There A Problem[/B]' , '' , "" , 'Yes' , 'No' ) :
   ii11iIi1I . ok ( "Message Send" , "Your Message Has Been Sent" )
  else :
   return
 else :
  try : iiiii11I1 . play ( url )
  except : pass
  try : o0oOoO00o . resolve_url ( url )
  except : pass
  i1111 . close ( )
  if 94 - 94: OOOo0 % IIII + Ooo00oOo00o
def II1IIiiIiI ( url ) :
 iiiii11I1 = xbmc . Player ( Ii1 ( ) )
 import urlresolver
 try : iiiii11I1 . play ( url )
 except : pass
 if 90 - 90: i1IIi + O0 - OoOO . oO0o0ooO0 + iIii1I11I1II1
 if 88 - 88: o00O0oo * O0 . O0oO / OoooooooOO
def Ii1 ( ) :
 try :
  ii1i1Iii = getSet ( "core-player" )
  if ( ii1i1Iii == 'DVDPLAYER' ) : oO00oO00O0Oo = xbmc . PLAYER_CORE_DVDPLAYER
  elif ( ii1i1Iii == 'MPLAYER' ) : oO00oO00O0Oo = xbmc . PLAYER_CORE_MPLAYER
  elif ( ii1i1Iii == 'PAPLAYER' ) : oO00oO00O0Oo = xbmc . PLAYER_CORE_PAPLAYER
  else : oO00oO00O0Oo = xbmc . PLAYER_CORE_AUTO
 except : oO00oO00O0Oo = xbmc . PLAYER_CORE_AUTO
 return oO00oO00O0Oo
 return True
 if 88 - 88: OoOO - i1IIi % i11iIiiIii % OoOoOO00 * OoooooooOO
def O0OO0O ( name , url , mode , iconimage , showcontext = True , allinfo = { } ) :
 o0oO00 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 O0o = True
 oO00oO = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 oO00oO . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 if showcontext :
  iIiII1 = [ ]
  if showcontext == 'fav' :
   iIiII1 . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in o0 :
   iIiII1 . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  oO00oO . addContextMenuItems ( iIiII1 )
 O0o = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = o0oO00 , listitem = oO00oO , isFolder = True )
 return O0o
 if 47 - 47: o0000oOoOoO0o
def ooO00o ( name , url , mode , iconimage , fanart , description ) :
 if 92 - 92: OoooooooOO % OOOo0 / I1IiI * I1IiI % i11iIiiIii / OoooooooOO
 o0oO00 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 O0o = True
 oO00oO = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 oO00oO . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 oO00oO . setProperty ( "Fanart_Image" , fanart )
 O0o = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = o0oO00 , listitem = oO00oO , isFolder = True )
 return O0o
 if 47 - 47: i11iIiiIii / Oo - Oo * Ooo00oOo00o
def IiI1iiiIii ( name , url , mode , iconimage , showcontext = True , allinfo = { } ) :
 o0oO00 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 O0o = True
 oO00oO = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 oO00oO . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 if showcontext :
  iIiII1 = [ ]
  if showcontext == 'fav' :
   iIiII1 . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in o0 :
   iIiII1 . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  oO00oO . addContextMenuItems ( iIiII1 )
 O0o = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = o0oO00 , listitem = oO00oO , isFolder = False )
 return O0o
 if 48 - 48: IIII
 if 96 - 96: OoOO / O0 . OoOoOO00 + IIII % OOooOOo
 if 67 - 67: O0 % O0oO
 if 35 - 35: OOOo0 . I1IiI + OoooooooOO % Oo % OoOO0ooOOoo0O
 if 39 - 39: o00O0oo
 if 60 - 60: OoOO0ooOOoo0O
def i11IiiI1Ii1 ( heading , announce ) :
 class o000ooOo0o0OO ( ) :
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
   try : i11i1 = open ( announce ) ; iiI1ii1IIiI = i11i1 . read ( )
   except : iiI1ii1IIiI = announce
   self . win . getControl ( self . CONTROL_TEXTBOX ) . setText ( str ( iiI1ii1IIiI ) )
   return
 o000ooOo0o0OO ( )
 o000ooOo0o0OO ( )
 if 35 - 35: ii11ii1ii * oO0o0ooO0 . IIII . IIII - OoOO % I1IiI
def iI1iiIiI ( ) :
 i11IiiI1Ii1 ( 'These are the main Sources you should get into you XBMC' , '[COLORwhite]http://architects.x10host.com[/COLOR]--- [CR]  [COLORred]http://repo.sharktech.co.uk[/COLOR]--- [CR]   [COLORwhite]http://fusion.tvaddons.ag[/COLOR]--- [CR]  [COLORred]http://i.totalxbmc.tv[/COLOR]--- [CR]   [COLORwhite]http://www.xunitytalk.com/xfinity[/COLOR]--- [CR]  [COLORred]http://srp.nu[/COLOR]--- [CR]   [COLORwhite]http://solved.no-issue.ca[/COLOR]--- [CR]  [COLORred]http://xbmc.aminhacasadigital.com[/COLOR]--- [CR]   [COLORwhite]http://xbmc.movieshd.co[/COLOR]--- [CR]  [COLORred]http://install.kaosbox.tv[/COLOR]--- [CR]   [COLORwhite]http://kodi-repo.com/mxr[/COLOR]--- [CR]  [COLORred]http://kodi.metalkettle.co[/COLOR]--- [CR]   [COLORwhite]http://prozone.getxbmc.com[/COLOR]--- [CR]  [COLORred]http://transform.mega-tron.tv[/COLOR]--- [CR]   [COLORwhite]http://muckys.kodimediaportal.ml[/COLOR]--- [CR]  [COLORred]http://jas0npc.pcriot.com[/COLOR]--- [CR]  [COLORwhite]Sports devil source[/COLOR]--- [CR]  [COLORred]http://iwillfolo.com/iwf[/COLOR]' )
 if 55 - 55: OoOO0ooOOoo0O * OoOoOO00 + OoOO
 if 93 - 93: oO0o0ooO0 * OoOO . Ooo00oOo00o - o00O0oo + O0 * Ooo00oOo00o
 if 59 - 59: OoOoOO00
 if 43 - 43: Oo + OoooooooOO
 if 47 - 47: o0oO0
def OO0O0 ( ) :
 xbmc . executebuiltin ( 'UpdateLocalAddons' )
 xbmc . executebuiltin ( 'UpdateAddonRepos' )
 ii11iIi1I = xbmcgui . Dialog ( )
 ii11iIi1I . ok ( "GenieTv" , '' , '                                 REFRESH SUCCESSFUL :)' , "                          [COLOR gold]Brought To You By Kodi Support Group, GenieTv[/COLOR]" )
 return
 if 92 - 92: o0000oOoOoO0o % i11iIiiIii % Oo
 if 23 - 23: OoOoOO00 * oO0o0ooO0
 if 80 - 80: O0oO / i11iIiiIii + OoooooooOO
 if 38 - 38: ii11ii1ii % o0oO0 + i1IIi * OoooooooOO * OoOO
 if 83 - 83: iIii1I11I1II1 - o0oO0 - O0oO / Ooo00oOo00o - O0
 if 81 - 81: o00O0oo - OoOO * ii11ii1ii / O0oO
 if 21 - 21: Ooo00oOo00o
 if 63 - 63: o0000oOoOoO0o . O0 * o0000oOoOoO0o + iIii1I11I1II1
 if 46 - 46: i1IIi + OoOoOO00 * i1IIi - o00O0oo
 if 79 - 79: OoOoOO00 - OoOO * ii11ii1ii - I1IiI . ii11ii1ii
 if 11 - 11: O0 * I1IiI
 if 37 - 37: I1IiI + O0 . O0 * Oo % O0oO / oO0o0ooO0
 if 18 - 18: OoooooooOO
 if 57 - 57: o0oO0 . I1IiI * OOooOOo - OoooooooOO
 if 75 - 75: i11iIiiIii / OOooOOo . IIII . i1IIi . i1IIi / o0000oOoOoO0o
 if 94 - 94: o0oO0 + OOOo0
 if 56 - 56: I1IiI % OOooOOo
 if 40 - 40: OoOO0ooOOoo0O / IIII
 if 29 - 29: o00O0oo - o00O0oo / o0oO0
 if 49 - 49: o0000oOoOoO0o + OoOO % Ooo00oOo00o - Oo - O0 - OoooooooOO
 if 4 - 4: OoOoOO00 - OoOO % Oo * i11iIiiIii
 if 18 - 18: Oo % O0
 if 66 - 66: iIii1I11I1II1 % i11iIiiIii / OOOo0
 if 47 - 47: ii11ii1ii * OoOO + iIii1I11I1II1 - OoOO / IIII
def oO0ooo0O0Ooo ( url ) :
 IIiIi1iI = i1IiiiI1iI ( OO0o + iiI111i1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 ooOOoooooo = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( IIiIi1iI )
 for II1I , url , O0i1II1Iiii1I11 , IIIIiiIiI , o00oooO0Oo in ooOOoooooo :
  ooooooO0oo ( II1I , url , 42 , O0i1II1Iiii1I11 , IIIIiiIiI , o00oooO0Oo )
 I1i1I1II ( 'movies' , 'MAIN' )
 if 41 - 41: i11iIiiIii * O0 - oO0o0ooO0 . OoOoOO00 % Ooo00oOo00o % ii11ii1ii
def I1I11i ( url ) :
 IIiIi1iI = i1IiiiI1iI ( OO0o + Iii1Iii ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 ooOOoooooo = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( IIiIi1iI )
 for II1I , url , O0i1II1Iiii1I11 , IIIIiiIiI , o00oooO0Oo in ooOOoooooo :
  ooooooO0oo ( II1I , url , 42 , O0i1II1Iiii1I11 , IIIIiiIiI , o00oooO0Oo )
 I1i1I1II ( 'movies' , 'MAIN' )
 if 91 - 91: o0oO0 * IIII * OoOoOO00
def oooO0oooOo000 ( url ) :
 IIiIi1iI = i1IiiiI1iI ( OO0o + ooOOO0o ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 ooOOoooooo = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( IIiIi1iI )
 for II1I , url , O0i1II1Iiii1I11 , IIIIiiIiI , o00oooO0Oo in ooOOoooooo :
  ooooooO0oo ( II1I , url , 42 , O0i1II1Iiii1I11 , IIIIiiIiI , o00oooO0Oo )
 I1i1I1II ( 'movies' , 'MAIN' )
 if 74 - 74: OoOoOO00 / O0
def O0oo0ooo0 ( url ) :
 IIiIi1iI = i1IiiiI1iI ( OO0o + iII1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 ooOOoooooo = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( IIiIi1iI )
 for II1I , url , O0i1II1Iiii1I11 , IIIIiiIiI , o00oooO0Oo in ooOOoooooo :
  ooooooO0oo ( II1I , url , 42 , O0i1II1Iiii1I11 , IIIIiiIiI , o00oooO0Oo )
 I1i1I1II ( 'movies' , 'MAIN' )
 if 77 - 77: OoooooooOO + OOooOOo
def o00O0o ( url ) :
 IIiIi1iI = i1IiiiI1iI ( OO0o + i1Ii1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 ooOOoooooo = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( IIiIi1iI )
 for II1I , url , O0i1II1Iiii1I11 , IIIIiiIiI , o00oooO0Oo in ooOOoooooo :
  ooooooO0oo ( II1I , url , 42 , O0i1II1Iiii1I11 , IIIIiiIiI , o00oooO0Oo )
 I1i1I1II ( 'movies' , 'MAIN' )
 if 75 - 75: OoooooooOO * i11iIiiIii
def o0oOo ( url ) :
 IIiIi1iI = i1IiiiI1iI ( OO0o + OoIIiIIIII1I ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 ooOOoooooo = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( IIiIi1iI )
 for II1I , url , O0i1II1Iiii1I11 , IIIIiiIiI , o00oooO0Oo in ooOOoooooo :
  ooooooO0oo ( II1I , url , 42 , O0i1II1Iiii1I11 , IIIIiiIiI , o00oooO0Oo )
 I1i1I1II ( 'movies' , 'MAIN' )
 if 96 - 96: i11iIiiIii . OoOoOO00
def iI1I ( url ) :
 IIiIi1iI = i1IiiiI1iI ( OO0o + Iii1IiI1iI1I ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 ooOOoooooo = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( IIiIi1iI )
 for II1I , url , O0i1II1Iiii1I11 , IIIIiiIiI , o00oooO0Oo in ooOOoooooo :
  ooooooO0oo ( II1I , url , 42 , O0i1II1Iiii1I11 , IIIIiiIiI , o00oooO0Oo )
 I1i1I1II ( 'movies' , 'MAIN' )
 if 31 - 31: OOOo0 / OoooooooOO . iIii1I11I1II1 * I1IiI . OoooooooOO + OoOoOO00
def II1IIii1I11I ( url ) :
 IIiIi1iI = i1IiiiI1iI ( OO0o + ii1IiIIiI11111Ii ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 ooOOoooooo = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( IIiIi1iI )
 for II1I , url , O0i1II1Iiii1I11 , IIIIiiIiI , o00oooO0Oo in ooOOoooooo :
  ooooooO0oo ( II1I , url , 42 , O0i1II1Iiii1I11 , IIIIiiIiI , o00oooO0Oo )
 I1i1I1II ( 'movies' , 'MAIN' )
 if 69 - 69: o0oO0 . OoOO0ooOOoo0O * I1IiI . o0000oOoOoO0o / o0oO0
def I1I1 ( url ) :
 IIiIi1iI = i1IiiiI1iI ( OO0o + OO0Oo00OO0oo ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 ooOOoooooo = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( IIiIi1iI )
 for II1I , url , O0i1II1Iiii1I11 , IIIIiiIiI , o00oooO0Oo in ooOOoooooo :
  ooooooO0oo ( II1I , url , 42 , O0i1II1Iiii1I11 , IIIIiiIiI , o00oooO0Oo )
 I1i1I1II ( 'movies' , 'MAIN' )
 if 53 - 53: Ooo00oOo00o - o0oO0 + o00O0oo
def I1Ii1II ( url ) :
 IIiIi1iI = i1IiiiI1iI ( OO0o + iiiiIiiIIii ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 ooOOoooooo = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( IIiIi1iI )
 for II1I , url , O0i1II1Iiii1I11 , IIIIiiIiI , o00oooO0Oo in ooOOoooooo :
  ooooooO0oo ( II1I , url , 5 , O0i1II1Iiii1I11 , IIIIiiIiI , o00oooO0Oo )
 I1i1I1II ( 'movies' , 'MAIN' )
 if 36 - 36: OoOO0ooOOoo0O * o00O0oo
 if 16 - 16: OoOoOO00
 if 100 - 100: O0 - i1IIi
 if 48 - 48: OoOO % o0oO0 + O0
 if 27 - 27: ii11ii1ii / OoOO0ooOOoo0O
 if 33 - 33: OoooooooOO % ii11ii1ii . O0 / ii11ii1ii
 if 63 - 63: IIII + iIii1I11I1II1 + OOOo0 + O0oO
 if 72 - 72: Ooo00oOo00o + i11iIiiIii + ii11ii1ii
 if 96 - 96: OoOO % i1IIi / OOooOOo
def Ii1IIi11 ( ) :
 try :
  if os . path . exists ( OooO0 ) == True :
   ii11iIi1I = xbmcgui . Dialog ( )
   if ii11iIi1I . yesno ( "Delete Thumbnails" , "[COLOR gold][B]##########WARNING ANDROID ONLY##########[/B][/COLOR]" , "This feature deletes your thumbnail folder and textures13.db" , "Are you sure you want to do proceed? This Can NOT Be Undone" ) :
    for oOoO , oOoO00O0 , OOIi1iI111II1I1 in os . walk ( OooO0 ) :
     i1ooO = 0
     i1ooO += len ( OOIi1iI111II1I1 )
     if i1ooO > 0 :
      for i11i1 in OOIi1iI111II1I1 :
       os . unlink ( os . path . join ( oOoO , i11i1 ) )
  i11iii1Ii1 = os . path . join ( II , "Textures13.db" )
  os . unlink ( i11iii1Ii1 )
  ii11iIi1I . ok ( "Restart KODI" , "Please restart KODI to rebuild thumbnail library" )
 except :
  ii11iIi1I = xbmcgui . Dialog ( )
  ii11iIi1I . ok ( i11 , "Error Deleting Thumbnails please visit Kodi Support Group, GenieTv on facebook" )
 return
 if 86 - 86: o0oO0 / i11iIiiIii
 if 49 - 49: i11iIiiIii . iIii1I11I1II1 - i1IIi . oO0o0ooO0 + Ooo00oOo00o
 if 6 - 6: Ooo00oOo00o
 if 99 - 99: OOooOOo * OoOO0ooOOoo0O % OoOO * OoOO + OoooooooOO
 if 82 - 82: o0000oOoOoO0o / I1IiI - OoOO0ooOOoo0O / o0oO0
 if 50 - 50: OoOO0ooOOoo0O + Ooo00oOo00o . i11iIiiIii + ii11ii1ii + i11iIiiIii
 if 31 - 31: OoOO * O0oO . I1IiI * o0000oOoOoO0o
 if 28 - 28: IIII + OOOo0 - Oo % OoOO0ooOOoo0O . o0000oOoOoO0o + OOOo0
 if 72 - 72: o00O0oo / Oo / OoOO * I1IiI + OoOO0ooOOoo0O
def OOoo0OOOo0o ( url ) :
 print '############################################################       DELETING STANDARD CACHE             ###############################################################'
 iI1111i1i11Ii = os . path . join ( xbmc . translatePath ( 'special://home' ) , 'cache' )
 if os . path . exists ( iI1111i1i11Ii ) == True :
  for oOoO , oOoO00O0 , OOIi1iI111II1I1 in os . walk ( iI1111i1i11Ii ) :
   i1ooO = 0
   i1ooO += len ( OOIi1iI111II1I1 )
   if 62 - 62: oO0o0ooO0
   if 8 - 8: oO0o0ooO0 - OOOo0 * Oo % ii11ii1ii * OoooooooOO
   if i1ooO > 0 :
    if 26 - 26: i1IIi / oO0o0ooO0 . oO0o0ooO0
    ii11iIi1I = xbmcgui . Dialog ( )
    if ii11iIi1I . yesno ( "Delete KODI Cache Files" , str ( i1ooO ) + " files found" , "Do you want to delete them?" ) :
     if 20 - 20: OoOO0ooOOoo0O - oO0o0ooO0 / Oo * Ooo00oOo00o
     for i11i1 in OOIi1iI111II1I1 :
      try :
       os . unlink ( os . path . join ( oOoO , i11i1 ) )
      except :
       pass
     for o00OIIIIIiiI in oOoO00O0 :
      try :
       shutil . rmtree ( os . path . join ( oOoO , o00OIIIIIiiI ) )
      except :
       pass
       if 38 - 38: O0
   else :
    pass
 if xbmc . getCondVisibility ( 'system.platform.ATV2' ) :
  ooO = os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'Other' )
  if 34 - 34: O0oO * OoOoOO00
  for oOoO , oOoO00O0 , OOIi1iI111II1I1 in os . walk ( ooO ) :
   i1ooO = 0
   i1ooO += len ( OOIi1iI111II1I1 )
   if 71 - 71: IIII
   if i1ooO > 0 :
    if 97 - 97: ii11ii1ii
    ii11iIi1I = xbmcgui . Dialog ( )
    if ii11iIi1I . yesno ( "Delete ATV2 Cache Files" , str ( i1ooO ) + " files found in 'Other'" , "Do you want to delete them?" ) :
     if 86 - 86: Oo - OoOO0ooOOoo0O . I1IiI . OoOoOO00 * OOOo0 . OoOoOO00
     for i11i1 in OOIi1iI111II1I1 :
      os . unlink ( os . path . join ( oOoO , i11i1 ) )
     for o00OIIIIIiiI in oOoO00O0 :
      shutil . rmtree ( os . path . join ( oOoO , o00OIIIIIiiI ) )
      if 34 - 34: OOooOOo . O0oO % IIII - O0 / O0oO
   else :
    pass
  Oo00OOoO0oo = os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'LocalAndRental' )
  if 4 - 4: Ooo00oOo00o - oO0o0ooO0 / i11iIiiIii * O0
  for oOoO , oOoO00O0 , OOIi1iI111II1I1 in os . walk ( Oo00OOoO0oo ) :
   i1ooO = 0
   i1ooO += len ( OOIi1iI111II1I1 )
   if 78 - 78: IIII - o0000oOoOoO0o % O0 - OoOO0ooOOoo0O % Ooo00oOo00o
   if i1ooO > 0 :
    if 43 - 43: Ooo00oOo00o
    ii11iIi1I = xbmcgui . Dialog ( )
    if ii11iIi1I . yesno ( "Delete ATV2 Cache Files" , str ( i1ooO ) + " files found in 'LocalAndRental'" , "Do you want to delete them?" ) :
     if 90 - 90: OoooooooOO + O0 + ii11ii1ii / o0000oOoOoO0o / o00O0oo * ii11ii1ii
     for i11i1 in OOIi1iI111II1I1 :
      os . unlink ( os . path . join ( oOoO , i11i1 ) )
     for o00OIIIIIiiI in oOoO00O0 :
      shutil . rmtree ( os . path . join ( oOoO , o00OIIIIIiiI ) )
      if 100 - 100: o0000oOoOoO0o
   else :
    pass
    if 82 - 82: iIii1I11I1II1
    if 19 - 19: OOOo0
    if 66 - 66: OoOO / I1IiI
    if 13 - 13: OoOoOO00
 oO0o000oOO = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.whatthefurk/cache' ) , '' )
 if os . path . exists ( oO0o000oOO ) == True :
  for oOoO , oOoO00O0 , OOIi1iI111II1I1 in os . walk ( oO0o000oOO ) :
   i1ooO = 0
   i1ooO += len ( OOIi1iI111II1I1 )
   if 27 - 27: O0 - o0000oOoOoO0o * OoOoOO00 - iIii1I11I1II1 / o0oO0
   if 24 - 24: Oo / iIii1I11I1II1 % OoOO0ooOOoo0O * I1IiI - iIii1I11I1II1
   if i1ooO > 0 :
    if 50 - 50: OoOoOO00
    ii11iIi1I = xbmcgui . Dialog ( )
    if ii11iIi1I . yesno ( "Delete WTF Cache Files" , str ( i1ooO ) + " files found" , "Do you want to delete them?" ) :
     if 39 - 39: OoOoOO00 . I1IiI - Oo * i1IIi . OoooooooOO
     for i11i1 in OOIi1iI111II1I1 :
      os . unlink ( os . path . join ( oOoO , i11i1 ) )
     for o00OIIIIIiiI in oOoO00O0 :
      shutil . rmtree ( os . path . join ( oOoO , o00OIIIIIiiI ) )
      if 44 - 44: OOOo0
   else :
    pass
    if 55 - 55: OoOO . O0oO * O0oO
    if 82 - 82: OOOo0 % Ooo00oOo00o % o0000oOoOoO0o + o0000oOoOoO0o
 i1111I = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.4od/cache' ) , '' )
 if os . path . exists ( i1111I ) == True :
  for oOoO , oOoO00O0 , OOIi1iI111II1I1 in os . walk ( i1111I ) :
   i1ooO = 0
   i1ooO += len ( OOIi1iI111II1I1 )
   if 58 - 58: OoooooooOO - o0000oOoOoO0o + iIii1I11I1II1 * i11iIiiIii
   if 80 - 80: i1IIi . OOOo0 - OoOO + OoOO0ooOOoo0O + oO0o0ooO0 % OoOO
   if i1ooO > 0 :
    if 13 - 13: OoOoOO00 / I1IiI / I1IiI + o0oO0
    ii11iIi1I = xbmcgui . Dialog ( )
    if ii11iIi1I . yesno ( "Delete 4oD Cache Files" , str ( i1ooO ) + " files found" , "Do you want to delete them?" ) :
     if 49 - 49: O0 / OoOoOO00 * OOOo0 - OoooooooOO . OoOoOO00 % IIII
     for i11i1 in OOIi1iI111II1I1 :
      os . unlink ( os . path . join ( oOoO , i11i1 ) )
     for o00OIIIIIiiI in oOoO00O0 :
      shutil . rmtree ( os . path . join ( oOoO , o00OIIIIIiiI ) )
      if 13 - 13: OoOO . iIii1I11I1II1 . OoOO0ooOOoo0O . IIII
   else :
    pass
    if 58 - 58: o0000oOoOoO0o
    if 7 - 7: OoOoOO00 / IIII % o0000oOoOoO0o + OOOo0 - O0
 IiI1Iii1IIII1Iii = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.iplayer/iplayer_http_cache' ) , '' )
 if os . path . exists ( IiI1Iii1IIII1Iii ) == True :
  for oOoO , oOoO00O0 , OOIi1iI111II1I1 in os . walk ( IiI1Iii1IIII1Iii ) :
   i1ooO = 0
   i1ooO += len ( OOIi1iI111II1I1 )
   if 94 - 94: OoOO . OOooOOo % OOooOOo % OOOo0 - oO0o0ooO0 / i11iIiiIii
   if 73 - 73: O0 * O0oO . i1IIi
   if i1ooO > 0 :
    if 51 - 51: Ooo00oOo00o - oO0o0ooO0 % O0 - I1IiI
    ii11iIi1I = xbmcgui . Dialog ( )
    if ii11iIi1I . yesno ( "Delete BBC iPlayer Cache Files" , str ( i1ooO ) + " files found" , "Do you want to delete them?" ) :
     if 53 - 53: oO0o0ooO0 / i1IIi / i1IIi
     for i11i1 in OOIi1iI111II1I1 :
      os . unlink ( os . path . join ( oOoO , i11i1 ) )
     for o00OIIIIIiiI in oOoO00O0 :
      shutil . rmtree ( os . path . join ( oOoO , o00OIIIIIiiI ) )
      if 77 - 77: o0000oOoOoO0o + i1IIi . o0000oOoOoO0o
   else :
    pass
    if 89 - 89: OOooOOo + OoOO0ooOOoo0O * OoOO
    if 45 - 45: oO0o0ooO0 - OOooOOo . o00O0oo
    if 41 - 41: OoOoOO00 . OOOo0 / Ooo00oOo00o . o0oO0
 O00oooO00oo = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/script.module.simple.downloader' ) , '' )
 if os . path . exists ( O00oooO00oo ) == True :
  for oOoO , oOoO00O0 , OOIi1iI111II1I1 in os . walk ( O00oooO00oo ) :
   i1ooO = 0
   i1ooO += len ( OOIi1iI111II1I1 )
   if 44 - 44: iIii1I11I1II1 * O0oO * Oo * ii11ii1ii + o0000oOoOoO0o
   if 12 - 12: ii11ii1ii * o0oO0 - o0000oOoOoO0o . Ooo00oOo00o + Ooo00oOo00o + oO0o0ooO0
   if i1ooO > 0 :
    if 29 - 29: OoooooooOO . O0oO % O0oO
    ii11iIi1I = xbmcgui . Dialog ( )
    if ii11iIi1I . yesno ( "Delete Simple Downloader Cache Files" , str ( i1ooO ) + " files found" , "Do you want to delete them?" ) :
     if 9 - 9: Oo - Oo - OOooOOo + O0oO - OoOoOO00 . OOOo0
     for i11i1 in OOIi1iI111II1I1 :
      os . unlink ( os . path . join ( oOoO , i11i1 ) )
     for o00OIIIIIiiI in oOoO00O0 :
      shutil . rmtree ( os . path . join ( oOoO , o00OIIIIIiiI ) )
      if 57 - 57: oO0o0ooO0 - OOOo0 + OoooooooOO / oO0o0ooO0 . o0oO0 % i1IIi
   else :
    pass
    if 52 - 52: O0 - iIii1I11I1II1 / Ooo00oOo00o / IIII
    if 29 - 29: o00O0oo * OoOO0ooOOoo0O * i1IIi . o00O0oo * O0oO . o0oO0
 O0iI1I1ii11IIi1 = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.itv/Images' ) , '' )
 if os . path . exists ( O0iI1I1ii11IIi1 ) == True :
  for oOoO , oOoO00O0 , OOIi1iI111II1I1 in os . walk ( O0iI1I1ii11IIi1 ) :
   i1ooO = 0
   i1ooO += len ( OOIi1iI111II1I1 )
   if 100 - 100: Oo . o00O0oo . OOOo0 % OoOoOO00 - OoOO
   if 52 - 52: OOOo0 % Ooo00oOo00o * o00O0oo * oO0o0ooO0 / OoOO0ooOOoo0O
   if i1ooO > 0 :
    if 88 - 88: OoOO
    ii11iIi1I = xbmcgui . Dialog ( )
    if ii11iIi1I . yesno ( "Delete ITV Cache Files" , str ( i1ooO ) + " files found" , "Do you want to delete them?" ) :
     if 1 - 1: Oo
     for i11i1 in OOIi1iI111II1I1 :
      os . unlink ( os . path . join ( oOoO , i11i1 ) )
     for o00OIIIIIiiI in oOoO00O0 :
      shutil . rmtree ( os . path . join ( oOoO , o00OIIIIIiiI ) )
      if 95 - 95: OoooooooOO / o0000oOoOoO0o % OoooooooOO / o0oO0 * IIII
   else :
    pass
    if 75 - 75: O0
    if 56 - 56: Ooo00oOo00o / OoOoOO00
 IIIiiiiI1 = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.movies4me/cache' ) , '' )
 if os . path . exists ( O0iI1I1ii11IIi1 ) == True :
  for oOoO , oOoO00O0 , OOIi1iI111II1I1 in os . walk ( IIIiiiiI1 ) :
   i1ooO = 0
   i1ooO += len ( OOIi1iI111II1I1 )
   if 40 - 40: O0 + IIII . o00O0oo
   if 29 - 29: OoOO0ooOOoo0O / I1IiI . iIii1I11I1II1 / o0000oOoOoO0o % I1IiI % oO0o0ooO0
   if i1ooO > 0 :
    if 49 - 49: OoOoOO00 / IIII - o00O0oo
    ii11iIi1I = xbmcgui . Dialog ( )
    if ii11iIi1I . yesno ( "Delete Movies4me Cache Files" , str ( i1ooO ) + " files found" , "Do you want to delete them?" ) :
     if 7 - 7: OOOo0 / Ooo00oOo00o + O0oO + o0000oOoOoO0o / OOOo0
     for i11i1 in OOIi1iI111II1I1 :
      os . unlink ( os . path . join ( oOoO , i11i1 ) )
     for o00OIIIIIiiI in oOoO00O0 :
      shutil . rmtree ( os . path . join ( oOoO , o00OIIIIIiiI ) )
      if 82 - 82: ii11ii1ii + OoooooooOO
   else :
    pass
    if 21 - 21: OoOO * OoOO / o0000oOoOoO0o . oO0o0ooO0
    if 10 - 10: o00O0oo * OoOO0ooOOoo0O - Oo - OoooooooOO / OOooOOo
 o0oo00oo0oO = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.phstreams/Cache' ) , '' )
 if os . path . exists ( O0iI1I1ii11IIi1 ) == True :
  for oOoO , oOoO00O0 , OOIi1iI111II1I1 in os . walk ( o0oo00oo0oO ) :
   i1ooO = 0
   i1ooO += len ( OOIi1iI111II1I1 )
   if 49 - 49: OOOo0
   if 24 - 24: OoOoOO00 / o00O0oo . iIii1I11I1II1 - OoOoOO00 % O0
   if i1ooO > 0 :
    if 8 - 8: Ooo00oOo00o % oO0o0ooO0 . OoooooooOO - o00O0oo % OoooooooOO
    ii11iIi1I = xbmcgui . Dialog ( )
    if ii11iIi1I . yesno ( "Delete Phoenix Cache Files" , str ( i1ooO ) + " files found" , "Do you want to delete them?" ) :
     if 61 - 61: OOooOOo / i11iIiiIii
     for i11i1 in OOIi1iI111II1I1 :
      os . unlink ( os . path . join ( oOoO , i11i1 ) )
     for o00OIIIIIiiI in oOoO00O0 :
      shutil . rmtree ( os . path . join ( oOoO , o00OIIIIIiiI ) )
      if 28 - 28: OoOO0ooOOoo0O / I1IiI
   else :
    pass
    if 30 - 30: o0oO0
    if 57 - 57: OOooOOo * i11iIiiIii / I1IiI
 iii1IiII = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.spotitube/cache' ) , '' )
 if os . path . exists ( O0iI1I1ii11IIi1 ) == True :
  for oOoO , oOoO00O0 , OOIi1iI111II1I1 in os . walk ( iii1IiII ) :
   i1ooO = 0
   i1ooO += len ( OOIi1iI111II1I1 )
   if 65 - 65: o0oO0 % O0
   if 17 - 17: i1IIi + OoOO . o0000oOoOoO0o + i1IIi - OoOoOO00 % OOOo0
   if i1ooO > 0 :
    if 34 - 34: OOOo0
    ii11iIi1I = xbmcgui . Dialog ( )
    if ii11iIi1I . yesno ( "Delete YouTube Music Cache Files" , str ( i1ooO ) + " files found" , "Do you want to delete them?" ) :
     if 57 - 57: OoOO0ooOOoo0O . o00O0oo % OOooOOo
     for i11i1 in OOIi1iI111II1I1 :
      os . unlink ( os . path . join ( oOoO , i11i1 ) )
     for o00OIIIIIiiI in oOoO00O0 :
      shutil . rmtree ( os . path . join ( oOoO , o00OIIIIIiiI ) )
      if 32 - 32: o0000oOoOoO0o / IIII - O0 * iIii1I11I1II1
   else :
    pass
    if 70 - 70: OoooooooOO % OoooooooOO % Ooo00oOo00o
    if 98 - 98: Ooo00oOo00o
 I1IIiIi = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.supercartoons/cache' ) , '' )
 if os . path . exists ( O0iI1I1ii11IIi1 ) == True :
  for oOoO , oOoO00O0 , OOIi1iI111II1I1 in os . walk ( I1IIiIi ) :
   i1ooO = 0
   i1ooO += len ( OOIi1iI111II1I1 )
   if 93 - 93: OoOO - OoOO0ooOOoo0O + OOooOOo . OoOO / o0000oOoOoO0o
   if 52 - 52: O0oO + O0oO
   if i1ooO > 0 :
    if 73 - 73: OOooOOo . i11iIiiIii % OoooooooOO + o0oO0 . OoooooooOO / OoOO0ooOOoo0O
    ii11iIi1I = xbmcgui . Dialog ( )
    if ii11iIi1I . yesno ( "Delete SuperCartoons Cache Files" , str ( i1ooO ) + " files found" , "Do you want to delete them?" ) :
     if 54 - 54: I1IiI . OoooooooOO
     for i11i1 in OOIi1iI111II1I1 :
      os . unlink ( os . path . join ( oOoO , i11i1 ) )
     for o00OIIIIIiiI in oOoO00O0 :
      shutil . rmtree ( os . path . join ( oOoO , o00OIIIIIiiI ) )
      if 36 - 36: OoOO / OoOoOO00 * IIII % ii11ii1ii
   else :
    pass
    if 31 - 31: OoOoOO00 + OoOO0ooOOoo0O - OoooooooOO . o0000oOoOoO0o
    if 28 - 28: o00O0oo . ii11ii1ii
 oOo000Oo00o = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.tvonline.cc/cache' ) , '' )
 if os . path . exists ( O0iI1I1ii11IIi1 ) == True :
  for oOoO , oOoO00O0 , OOIi1iI111II1I1 in os . walk ( oOo000Oo00o ) :
   i1ooO = 0
   i1ooO += len ( OOIi1iI111II1I1 )
   if 81 - 81: OoooooooOO
   if 88 - 88: O0 * OOooOOo
   if i1ooO > 0 :
    if 44 - 44: OOooOOo / ii11ii1ii . Oo + I1IiI
    ii11iIi1I = xbmcgui . Dialog ( )
    if ii11iIi1I . yesno ( "Delete TVonline Cache Files" , str ( i1ooO ) + " files found" , "Do you want to delete them?" ) :
     if 32 - 32: IIII - o0oO0 * oO0o0ooO0 * o0000oOoOoO0o
     for i11i1 in OOIi1iI111II1I1 :
      os . unlink ( os . path . join ( oOoO , i11i1 ) )
     for o00OIIIIIiiI in oOoO00O0 :
      shutil . rmtree ( os . path . join ( oOoO , o00OIIIIIiiI ) )
      if 84 - 84: o00O0oo + ii11ii1ii % OOOo0 + i11iIiiIii
   else :
    pass
    if 37 - 37: o0000oOoOoO0o % ii11ii1ii / o0oO0
    if 94 - 94: o0000oOoOoO0o / Ooo00oOo00o . OOooOOo
 iIiOo = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.youtube/kodion' ) , '' )
 if os . path . exists ( O0iI1I1ii11IIi1 ) == True :
  for oOoO , oOoO00O0 , OOIi1iI111II1I1 in os . walk ( iIiOo ) :
   i1ooO = 0
   i1ooO += len ( OOIi1iI111II1I1 )
   if 48 - 48: OoOO0ooOOoo0O
   if 26 - 26: oO0o0ooO0 * O0oO * OoOO * I1IiI
   if i1ooO > 0 :
    if 48 - 48: oO0o0ooO0 % i11iIiiIii . OoooooooOO * IIII % Ooo00oOo00o . oO0o0ooO0
    ii11iIi1I = xbmcgui . Dialog ( )
    if ii11iIi1I . yesno ( "Delete YouTube Cache Files" , str ( i1ooO ) + " files found" , "Do you want to delete them?" ) :
     if 6 - 6: O0 . o0oO0 - OoOO / i11iIiiIii
     for i11i1 in OOIi1iI111II1I1 :
      os . unlink ( os . path . join ( oOoO , i11i1 ) )
     for o00OIIIIIiiI in oOoO00O0 :
      shutil . rmtree ( os . path . join ( oOoO , o00OIIIIIiiI ) )
      if 84 - 84: o0000oOoOoO0o / ii11ii1ii * OOooOOo * Ooo00oOo00o * OoOO0ooOOoo0O * O0
   else :
    pass
    if 83 - 83: O0 % OoOoOO00 + OOooOOo / OoooooooOO
    if 75 - 75: OoOoOO00 . OOOo0 + OoOO0ooOOoo0O - I1IiI - O0 . o0000oOoOoO0o
    if 19 - 19: o00O0oo * i1IIi % O0 + o0000oOoOoO0o
 I1i1ii1ii = xbmc . translatePath ( 'special://masterprofile/addon_data/plugin.video.genesis' )
 ii11iIi1I = xbmcgui . Dialog ( )
 try :
  if ii11iIi1I . yesno ( "Delete Genesis Cache Files" , "Do you want to delete cache" ) :
   i1ii = os . path . join ( I1i1ii1ii , "cache.db" )
   os . unlink ( i1ii )
   if 70 - 70: ii11ii1ii + OOOo0
 except :
  pass
  if 65 - 65: oO0o0ooO0 - oO0o0ooO0 . Oo
 ii11iIi1I = xbmcgui . Dialog ( )
 ii11iIi1I . ok ( "GenieTv" , "                               Finished Deleting Cache " , "                          [COLOR gold]Brought To You By GenieTv[/COLOR]" )
 if 54 - 54: OOOo0 % oO0o0ooO0
 if 80 - 80: OOooOOo % oO0o0ooO0
 if 80 - 80: o00O0oo
 if 26 - 26: iIii1I11I1II1 . OoooooooOO - iIii1I11I1II1
 if 59 - 59: ii11ii1ii + o0000oOoOoO0o . OoOO
 if 87 - 87: Ooo00oOo00o
 if 34 - 34: O0oO . I1IiI / i11iIiiIii / oO0o0ooO0
 if 46 - 46: Oo + OoOoOO00 * OOOo0 + OoOO0ooOOoo0O
 if 31 - 31: o00O0oo * OOooOOo * o00O0oo + Ooo00oOo00o * OOooOOo . O0oO
def Oo00oo00o00Oo ( url ) :
 print '###' + i11 + ' - DELETING PACKAGES###'
 iiiiiii11III = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' , '' ) )
 try :
  for oOoO , oOoO00O0 , OOIi1iI111II1I1 in os . walk ( iiiiiii11III ) :
   i1ooO = 0
   i1ooO += len ( OOIi1iI111II1I1 )
   if 48 - 48: O0oO % oO0o0ooO0 % o00O0oo % iIii1I11I1II1 . o00O0oo
   if 14 - 14: oO0o0ooO0 * Ooo00oOo00o % O0 + o0000oOoOoO0o + ii11ii1ii
   if i1ooO > 0 :
    if 23 - 23: Oo % oO0o0ooO0 + o00O0oo - O0oO
    ii11iIi1I = xbmcgui . Dialog ( )
    if ii11iIi1I . yesno ( "Delete Package Cache Files" , str ( i1ooO ) + " files found" , "Do you want to delete them?" ) :
     if 65 - 65: OoooooooOO
     for i11i1 in OOIi1iI111II1I1 :
      os . unlink ( os . path . join ( oOoO , i11i1 ) )
     for o00OIIIIIiiI in oOoO00O0 :
      shutil . rmtree ( os . path . join ( oOoO , o00OIIIIIiiI ) )
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
 if 22 - 22: OoOO0ooOOoo0O + OoOoOO00 + Oo
 if 83 - 83: o0oO0
 if 43 - 43: OoOO0ooOOoo0O
 if 84 - 84: OoOO0ooOOoo0O . IIII . oO0o0ooO0
 if 2 - 2: Oo - I1IiI
 if 49 - 49: o00O0oo + OoOoOO00 / OoOO - I1IiI % I1IiI + OOOo0
 if 54 - 54: o0oO0 % Oo - OoOO0ooOOoo0O
 if 16 - 16: ii11ii1ii * oO0o0ooO0 / o0000oOoOoO0o
 if 46 - 46: OoOoOO00
def i11iIi ( url ) :
 print '###' + i11 + ' - DELETING PACKAGES###'
 iiiiiii11III = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' , '' ) )
 try :
  for oOoO , oOoO00O0 , OOIi1iI111II1I1 in os . walk ( iiiiiii11III ) :
   i1ooO = 0
   i1ooO += len ( OOIi1iI111II1I1 )
   if 82 - 82: Oo / OOOo0 . ii11ii1ii - Oo
   if 4 - 4: O0 / o0000oOoOoO0o . Ooo00oOo00o - o0oO0 / OoOO0ooOOoo0O
   if i1ooO > 0 :
    if 25 - 25: o0000oOoOoO0o * I1IiI - Oo . o0oO0 . OoOO
    ii11iIi1I = xbmcgui . Dialog ( )
    if ii11iIi1I . yesno ( "Delete Package Cache Files" , str ( i1ooO ) + " files found" , "Do you want to delete them?" ) :
     if 89 - 89: O0 * o0000oOoOoO0o * Ooo00oOo00o
     for i11i1 in OOIi1iI111II1I1 :
      os . unlink ( os . path . join ( oOoO , i11i1 ) )
     for o00OIIIIIiiI in oOoO00O0 :
      shutil . rmtree ( os . path . join ( oOoO , o00OIIIIIiiI ) )
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
 OOoo0OOOo0o ( url )
 if 3 - 3: OoOO0ooOOoo0O / oO0o0ooO0 * iIii1I11I1II1 + OoOoOO00 / OOooOOo / IIII
 if 25 - 25: I1IiI + Ooo00oOo00o % o00O0oo % OoOO0ooOOoo0O / OoOO
 if 91 - 91: Ooo00oOo00o / Ooo00oOo00o . OoOoOO00 . o0oO0 - OOOo0
 if 23 - 23: OOOo0
 if 7 - 7: oO0o0ooO0 % ii11ii1ii
 if 64 - 64: O0oO + i11iIiiIii
 if 35 - 35: I1IiI + i1IIi % OoOO0ooOOoo0O
 if 68 - 68: IIII . o0oO0
 if 64 - 64: i1IIi + Oo * OOOo0 / OoOO0ooOOoo0O
def III1 ( url , name ) :
 OO = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 IIi1iI1i = os . path . join ( OO , 'advancedsettings.xml' )
 ii11iIi1I = xbmcgui . Dialog ( )
 Iii11II1 = os . path . join ( OO , 'advancedsettings.xml.bak' )
 if os . path . exists ( Iii11II1 ) == False :
  if ii11iIi1I . yesno ( "Back Up Original" , 'Have You Backed Up Your Original?' , '' , "[B][COLOR red]     AS YOU CANNOT GO BACK !!![/B][/COLOR]" ) :
   print '###' + i11 + ' - ADVANCED XML###'
   OO = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
   IIi1iI1i = os . path . join ( OO , 'advancedsettings.xml' )
   try :
    os . remove ( IIi1iI1i )
    print '=== GenieTv - REMOVING    ' + str ( IIi1iI1i ) + '    ==='
   except :
    pass
   IIiIi1iI = I11 . http_GET ( url ) . content
   oOOOOoOO0o = open ( IIi1iI1i , "w" )
   oOOOOoOO0o . write ( IIiIi1iI )
   oOOOOoOO0o . close ( )
   print '=== GenieTv - WRITING NEW    ' + str ( IIi1iI1i ) + '    ==='
   ii11iIi1I = xbmcgui . Dialog ( )
   ii11iIi1I . ok ( i11 , "       Done Adding new Advanced XML" )
 else :
  print '###' + i11 + ' - ADVANCED XML###'
  OO = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
  IIi1iI1i = os . path . join ( OO , 'advancedsettings.xml' )
  try :
   os . remove ( IIi1iI1i )
   print '=== GenieTv - REMOVING    ' + str ( IIi1iI1i ) + '    ==='
  except :
   pass
  IIiIi1iI = I11 . http_GET ( url ) . content
  oOOOOoOO0o = open ( IIi1iI1i , "w" )
  oOOOOoOO0o . write ( IIiIi1iI )
  oOOOOoOO0o . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( IIi1iI1i ) + '    ==='
  ii11iIi1I = xbmcgui . Dialog ( )
  ii11iIi1I . ok ( i11 , "       Done Adding new Advanced XML" )
 return
 if 42 - 42: Oo / IIII . o00O0oo * OOOo0
def oOO0O0ooOOOo ( url , name ) :
 print '###' + i11 + ' - CHECK ADVANCE XML###'
 OO = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 IIi1iI1i = os . path . join ( OO , 'advancedsettings.xml' )
 try :
  oOOOOoOO0o = open ( IIi1iI1i ) . read ( )
  if 'zero' in oOOOOoOO0o :
   name = '0CACHE'
  elif 'tuxen' in oOOOOoOO0o :
   name = 'TUXENS'
  elif 'muckys' in oOOOOoOO0o :
   name = 'MUCKYS'
  elif 'p2p1' in oOOOOoOO0o :
   name = '1st P2P RECOMMENDED'
  elif 'p2p2' in oOOOOoOO0o :
   name = '2nd P2P RECOMMENDED'
  elif 'mikey' in oOOOOoOO0o :
   name = 'MIKEY1234'
 except :
  name = "NO ADVANCED"
 ii11iIi1I = xbmcgui . Dialog ( )
 ii11iIi1I . ok ( i11 , "[COLOR yellow]YOU HAVE[/COLOR] " + name + "[COLOR yellow] XML SETTINGS SETUP[/COLOR]" )
 return
 if 91 - 91: o0oO0 - OoOO + OoOO
def II11iiIIiI11I ( url ) :
 print '###' + i11 + ' - DELETING ADVANCE XML###'
 OO = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 IIi1iI1i = os . path . join ( OO , 'advancedsettings.xml' )
 try :
  os . remove ( IIi1iI1i )
  ii11iIi1I = xbmcgui . Dialog ( )
  print '=== GenieTv - DELETING    ' + str ( IIi1iI1i ) + '    ==='
  ii11iIi1I . ok ( i11 , "       Remove Advanced Settings Sucessfull" )
 except :
  ii11iIi1I = xbmcgui . Dialog ( )
  ii11iIi1I . ok ( i11 , "       No Advanced Settings To Remove" )
 return
 if 56 - 56: OoooooooOO * IIII + O0oO / OOOo0 * IIII / i1IIi
 if 47 - 47: o0oO0 - o00O0oo
 if 98 - 98: OoOO . O0oO / I1IiI . o0oO0
 if 1 - 1: OoOO0ooOOoo0O
 if 87 - 87: O0 * OoOoOO00 + iIii1I11I1II1 % OoOO % i11iIiiIii - I1IiI
 if 73 - 73: oO0o0ooO0 + o00O0oo
 if 37 - 37: OoOO - iIii1I11I1II1 + OoOoOO00 . o00O0oo % iIii1I11I1II1
 if 17 - 17: O0oO + i1IIi % O0
 if 65 - 65: IIII
 if 50 - 50: OoOoOO00 / Ooo00oOo00o
def OO0oooOO ( url = 'http://www.iplocation.net/' , inc = 1 ) :
 ooOOoooooo = re . compile ( "<td width='80'>(.+?)</td><td>(.+?)</td><td>(.+?)</td><td>.+?</td><td>(.+?)</td>" ) . findall ( I11 . http_GET ( url ) . content )
 for III , i1iiIIiiiI , I1IIiIi1iI , oOo0Iiii11 in ooOOoooooo :
  if inc < 2 : ii11iIi1I = xbmcgui . Dialog ( ) ; ii11iIi1I . ok ( 'Check My IP' , "[B][COLOR gold]Your IP Address is: [/COLOR][/B] %s" % III , '[B][COLOR gold]Your IP is based in: [/COLOR][/B] %s' % I1IIiIi1iI , '[B][COLOR gold]Your Service Provider is:[/COLOR][/B] %s' % oOo0Iiii11 )
  inc = inc + 1
  if 65 - 65: O0oO + oO0o0ooO0 * oO0o0ooO0
  if 79 - 79: i1IIi / Oo - OOOo0 . O0
  if 56 - 56: IIII % O0 * i1IIi - OoOoOO00
  if 74 - 74: i1IIi - I1IiI % OoOO . O0 - OoooooooOO
  if 84 - 84: O0oO
  if 53 - 53: i1IIi
  if 59 - 59: OOooOOo + OOOo0 % OoooooooOO - iIii1I11I1II1
  if 9 - 9: i1IIi - I1IiI
  if 57 - 57: iIii1I11I1II1 * o00O0oo * oO0o0ooO0 / OoOO
def iIIiII1i1ii ( url , name ) :
 ii11iIi1I = xbmcgui . Dialog ( )
 if ii11iIi1I . yesno ( "GenieTv" , '                                    Install Latest .ini File' ) :
  print '###' + i11 + ' - CUSTOM FTV INI###'
  OO = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/script.ftvguide' , '' ) )
  IIi1iI1i = os . path . join ( OO , 'addons2.ini' )
  IIiIi1iI = I11 . http_GET ( url ) . content
  oOOOOoOO0o = open ( IIi1iI1i , "w" )
  oOOOOoOO0o . write ( IIiIi1iI )
  oOOOOoOO0o . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( IIi1iI1i ) + '    ==='
  ii11iIi1I = xbmcgui . Dialog ( )
  ii11iIi1I . ok ( i11 , "                               Done Adding New .ini File" )
 return
 if 57 - 57: o0oO0 + O0oO
def iIiiIi1IIIi11 ( url , name ) :
 ii11iIi1I = xbmcgui . Dialog ( )
 if ii11iIi1I . yesno ( "GenieTv" , '                               Install Custom Settings' ) :
  print '###' + i11 + ' - CUSTOM FTV SETTINGS###'
  OO = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/script.ftvguide' , '' ) )
  IIi1iI1i = os . path . join ( OO , 'settings.xml' )
  IIiIi1iI = I11 . http_GET ( url ) . content
  oOOOOoOO0o = open ( IIi1iI1i , "w" )
  oOOOOoOO0o . write ( IIiIi1iI )
  oOOOOoOO0o . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( IIi1iI1i ) + '    ==='
  ii11iIi1I = xbmcgui . Dialog ( )
  ii11iIi1I . ok ( i11 , "                               Done Adding New Settings" )
 return
 if 22 - 22: OOooOOo / OOOo0 . ii11ii1ii - OoooooooOO
 if 16 - 16: IIII % OoooooooOO - o0oO0 * o00O0oo - o00O0oo
def I1iiII1 ( ) :
 try :
  iI1I1I = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/script.ftvguide' , '' ) )
  if os . path . exists ( iI1I1I ) == True :
   ii11iIi1I = xbmcgui . Dialog ( )
   if ii11iIi1I . yesno ( "GenieTv" , "                               Delete FTV Guide Database" ) :
    Oo0o0oOo0oO = os . path . join ( iI1I1I , "source.db" )
    os . unlink ( Oo0o0oOo0oO )
  ii11iIi1I . ok ( "GenieTv" , "                                     FTV Database Reset" )
 except :
  ii11iIi1I = xbmcgui . Dialog ( )
  ii11iIi1I . ok ( i11 , "               Error Deleting Database No Database To Delete" )
 return
 if 20 - 20: IIII - iIii1I11I1II1
 if 25 - 25: o0000oOoOoO0o + I1IiI
 if 98 - 98: OoOO0ooOOoo0O
 if 69 - 69: OoOoOO00 + Oo - OoOO . Oo / iIii1I11I1II1 * iIii1I11I1II1
 if 75 - 75: Ooo00oOo00o % OoooooooOO
def i1IiiiI1iI ( url ) :
 Ooo0Oo0o = urllib2 . Request ( url )
 Ooo0Oo0o . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
 oo0Oo0 = urllib2 . urlopen ( Ooo0Oo0o )
 IIiIi1iI = oo0Oo0 . read ( )
 oo0Oo0 . close ( )
 return IIiIi1iI
 if 16 - 16: O0 / i1IIi
 if 58 - 58: OOooOOo / i11iIiiIii / O0 % o0000oOoOoO0o % OOOo0
 if 86 - 86: IIII + I1IiI / OOOo0 + o0000oOoOoO0o % o0000oOoOoO0o / i11iIiiIii
 if 12 - 12: I1IiI + OOooOOo . O0oO
 if 52 - 52: Ooo00oOo00o
 if 4 - 4: o00O0oo % ii11ii1ii + o0000oOoOoO0o - ii11ii1ii
 if 98 - 98: o00O0oo - O0 * OoOO * o00O0oo * o00O0oo
def i11IiII ( params ) :
 plugintools . log ( "freshstart.main_list " + repr ( params ) ) ; OOoOo0ooOoo = plugintools . message_yes_no ( i11 , "Do you wish to restore your" , "Kodi configuration to default settings?" )
 if OOoOo0ooOoo :
  oO0OO00 = xbmcaddon . Addon ( id = oOOoo00O0O ) . getAddonInfo ( 'path' ) ; oO0OO00 = xbmc . translatePath ( oO0OO00 ) ;
  IiiI = os . path . join ( oO0OO00 , ".." , ".." ) ; IiiI = os . path . abspath ( IiiI ) ; plugintools . log ( "freshstart.main_list xbmcPath=" + IiiI ) ; O0oooooO = False
  try :
   for oOoO , oOoO00O0 , OOIi1iI111II1I1 in os . walk ( IiiI , topdown = True ) :
    oOoO00O0 [ : ] = [ o00OIIIIIiiI for o00OIIIIIiiI in oOoO00O0 if o00OIIIIIiiI not in Oo0oO0ooo ]
    for II1I in OOIi1iI111II1I1 :
     try : os . remove ( os . path . join ( oOoO , II1I ) )
     except :
      if II1I not in [ "Addons15.db" , "MyVideos75.db" , "Textures13.db" , "xbmc.log" ] : O0oooooO = True
      plugintools . log ( "Error removing " + oOoO + " " + II1I )
    for II1I in oOoO00O0 :
     try : os . rmdir ( os . path . join ( oOoO , II1I ) )
     except :
      if II1I not in [ "Database" , "userdata" ] : O0oooooO = True
      plugintools . log ( "Error removing " + oOoO + " " + II1I )
   if not O0oooooO : plugintools . log ( "freshstart.main_list All user files removed, you now have a clean install" ) ; plugintools . message ( i11 , "The process is complete, you're now back to a fresh Kodi configuration with GenieTv!" , "Please reboot your system or restart Kodi in order for the changes to be applied." )
   else : plugintools . log ( "freshstart.main_list User files partially removed" ) ; plugintools . message ( i11 , "The process is complete, you're now back to a fresh Kodi configuration with GenieTv" , "Please reboot your system or restart Kodi in order for the changes to be applied." )
  except : plugintools . message ( i11 , "Problem found" , "Your settings has not been changed" ) ; import traceback ; plugintools . log ( traceback . format_exc ( ) ) ; plugintools . log ( "freshstart.main_list NOT removed" )
  plugintools . add_item ( action = "" , title = "Now Exit Kodi" , folder = False )
 else : plugintools . message ( i11 , "Your settings" , "has not been changed" ) ; plugintools . add_item ( action = "" , title = "Done" , folder = False )
 iIii1II11 ( )
 if 28 - 28: Oo / IIII . oO0o0ooO0 + Ooo00oOo00o + o0000oOoOoO0o % Oo
 if 45 - 45: Oo / O0 % OoooooooOO
 if 92 - 92: o00O0oo . I1IiI . o0000oOoOoO0o - OoooooooOO / o0oO0
def ooOo0 ( ) :
 I11I1i = [ ]
 oOO0oOooo = sys . argv [ 2 ]
 if len ( oOO0oOooo ) >= 2 :
  o00IIIIii1111i1 = sys . argv [ 2 ]
  iiI1ii1 = o00IIIIii1111i1 . replace ( '?' , '' )
  if ( o00IIIIii1111i1 [ len ( o00IIIIii1111i1 ) - 1 ] == '/' ) :
   o00IIIIii1111i1 = o00IIIIii1111i1 [ 0 : len ( o00IIIIii1111i1 ) - 2 ]
  I1oOOoo0 = iiI1ii1 . split ( '&' )
  I11I1i = { }
  for O0o00OOo00O0O in range ( len ( I1oOOoo0 ) ) :
   II1 = { }
   II1 = I1oOOoo0 [ O0o00OOo00O0O ] . split ( '=' )
   if ( len ( II1 ) ) == 2 :
    I11I1i [ II1 [ 0 ] ] = II1 [ 1 ]
    if 86 - 86: OoOO . OOOo0 - O0oO + iIii1I11I1II1
 return I11I1i
 if 66 - 66: o0000oOoOoO0o - o0000oOoOoO0o + IIII
oO00oooOOoOo0 = base64 . decodestring ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20v' )
I1iI1ii1II = base64 . decodestring ( 'L3N0b3JhZ2UvZW11bGF0ZWQvMA==' )
OoOOoOooooOOo = base64 . decodestring ( 'L2dlbmllLnR4dA==' )
i1ii1iiiI = base64 . decodestring ( 'LmFyY2hpdGVjdHMueDEwaG9zdC5jb20vdGVzdC93aC50eHQ=' )
i1iIi = base64 . decodestring ( 'aHR0cDovL2ZpeGVzLmFyY2hpdGVjdHMueDEwaG9zdC5jb20vZml4ZXMudHh0' )
III11iIII1 = base64 . decodestring ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vYXBwcy9hcHBzLnhtbA==' )
iiI111i1 = base64 . decodestring ( 'L2FkZG9ucy9uZXcudHh0' )
Iiiiii = base64 . decodestring ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vdm9kL3ZvZC5waHA=' )
Iii1Iii = base64 . decodestring ( 'L2FkZG9ucy9pcHR2LnR4dA==' )
ooOOO0o = base64 . decodestring ( 'L2FkZG9ucy92aWRlby50eHQ=' )
iII1 = base64 . decodestring ( 'L2FkZG9ucy9zcG9ydHMudHh0' )
i1Ii1 = base64 . decodestring ( 'L2FkZG9ucy9raWRzLnR4dA==' )
OoIIiIIIII1I = base64 . decodestring ( 'L2FkZG9ucy9tdXNpYy50eHQ=' )
Iii1IiI1iI1I = base64 . decodestring ( 'L2FkZG9ucy9wcm9ncmFtcy50eHQ=' )
ii1IiIIiI11111Ii = base64 . decodestring ( 'L2FkZG9ucy94eHgudHh0' )
OO0Oo00OO0oo = base64 . decodestring ( 'L2FkZG9ucy9yZXBvLnR4dA==' )
OOooooO0Oo = base64 . decodestring ( 'L2FkZG9ucy9wYWNrcy50eHQ=' )
oOOOO = base64 . decodestring ( 'L2FkZG9ucy9za2lucy50eHQ=' )
IIi11i1i1iI1 = base64 . decodestring ( 'L2FkZG9ucy9hcnQudHh0' )
iii = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2dvdGhhbS50eHQ=' )
i1Iii1i1I = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2hlbGl4LnR4dA==' )
Iiii1i1 = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2lzZW5nYXJkLnR4dA==' )
iiiiIiiIIii = base64 . decodestring ( 'L2FkZG9ucy9SU1MudHh0' )
oOOIi1II = base64 . decodestring ( 'Q1VOVA==' )
def ooooooO0oo ( name , url , mode , iconimage , fanart , description , showcontext = True , allinfo = { } ) :
 o0oO00 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 O0o = True
 oO00oO = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 oO00oO . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 oO00oO . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  iIiII1 = [ ]
  if showcontext == 'fav' :
   iIiII1 . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in o0 :
   iIiII1 . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fanart=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , urllib . quote_plus ( fanart ) , mode ) ) )
  oO00oO . addContextMenuItems ( iIiII1 )
 O0o = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = o0oO00 , listitem = oO00oO , isFolder = True )
 return O0o
 if 82 - 82: i1IIi + OOooOOo - OoOoOO00 . o00O0oo
def i1i ( name , url , mode , iconimage , fanart , description ) :
 o0oO00 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 O0o = True
 oO00oO = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 oO00oO . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 oO00oO . setProperty ( "Fanart_Image" , fanart )
 O0o = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = o0oO00 , listitem = oO00oO , isFolder = False )
 return O0o
 if 93 - 93: OoOoOO00 * I1IiI % OOooOOo
 if 67 - 67: OOooOOo + Oo . o0oO0 - i1IIi . I1IiI
o00IIIIii1111i1 = ooOo0 ( )
I1Ii1iI1 = None
II1I = None
Ii1iI111 = None
O0i1II1Iiii1I11 = None
IIIIiiIiI = None
o00oooO0Oo = None
I1iI1 = None
if 9 - 9: Oo - o0oO0 * oO0o0ooO0 / i11iIiiIii / Oo % OoOO
if 16 - 16: oO0o0ooO0 - i1IIi + OOooOOo * iIii1I11I1II1 + OoOO . OoOO
try :
 I1iI1 = int ( o00IIIIii1111i1 [ "fav_mode" ] )
except :
 pass
 if 85 - 85: O0oO . IIII - o0oO0 / OoOoOO00 * O0oO
try :
 I1Ii1iI1 = urllib . unquote_plus ( o00IIIIii1111i1 [ "url" ] )
except :
 pass
try :
 II1I = urllib . unquote_plus ( o00IIIIii1111i1 [ "name" ] )
except :
 pass
try :
 O0i1II1Iiii1I11 = urllib . unquote_plus ( o00IIIIii1111i1 [ "iconimage" ] )
except :
 pass
try :
 Ii1iI111 = int ( o00IIIIii1111i1 [ "mode" ] )
except :
 pass
try :
 IIIIiiIiI = urllib . unquote_plus ( o00IIIIii1111i1 [ "fanart" ] )
except :
 pass
try :
 o00oooO0Oo = urllib . unquote_plus ( o00IIIIii1111i1 [ "description" ] )
except :
 pass
 if 98 - 98: iIii1I11I1II1 + i11iIiiIii * ii11ii1ii / O0oO / o0oO0 - O0
 if 42 - 42: oO0o0ooO0
print str ( II11iiii1Ii ) + ': ' + str ( iiI1IiI )
print "Mode: " + str ( Ii1iI111 )
print "URL: " + str ( I1Ii1iI1 )
print "Name: " + str ( II1I )
print "IconImage: " + str ( O0i1II1Iiii1I11 )
if 77 - 77: i1IIi * OoOO % OoooooooOO + O0 * o0oO0
if 28 - 28: o0000oOoOoO0o . OoooooooOO * OoOO0ooOOoo0O + i11iIiiIii % OOOo0 . iIii1I11I1II1
def I1i1I1II ( content , viewType ) :
 if 63 - 63: OoOoOO00 - o0000oOoOoO0o . I1IiI
 if content :
  xbmcplugin . setContent ( int ( sys . argv [ 1 ] ) , content )
 if o0oOoO00o . getSetting ( 'auto-view' ) == 'true' :
  xbmc . executebuiltin ( "Container.SetViewMode(%s)" % o0oOoO00o . getSetting ( viewType ) )
  if 8 - 8: OOOo0 * o0oO0 / IIII + I1IiI . IIII - OoOO0ooOOoo0O
  if 80 - 80: iIii1I11I1II1 / OoOO * Oo - OoOO0ooOOoo0O * oO0o0ooO0
if Ii1iI111 == None :
 IIIII ( )
 if 97 - 97: IIII - o0000oOoOoO0o / OoOoOO00
elif Ii1iI111 == 1 :
 O0oOOO0ooOOO0OOO ( I1Ii1iI1 )
 if 26 - 26: oO0o0ooO0 + O0 * oO0o0ooO0 . i1IIi
elif Ii1iI111 == 44 :
 i1OOoO ( I1Ii1iI1 )
 if 50 - 50: iIii1I11I1II1 - o0000oOoOoO0o % oO0o0ooO0 - Oo
elif Ii1iI111 == 2 :
 I1i ( )
 if 52 - 52: OoOO + o00O0oo - ii11ii1ii * o00O0oo . OoOO0ooOOoo0O + O0oO
elif Ii1iI111 == 3 :
 O0ooo0O0oo0 ( )
 if 43 - 43: OOOo0 % IIII % ii11ii1ii
elif Ii1iI111 == 21 :
 Oo0ooOo0o ( )
 if 53 - 53: OoOO % OoOO0ooOOoo0O % ii11ii1ii . O0oO . O0oO . oO0o0ooO0
elif Ii1iI111 == 4 :
 o0o00OO0 ( )
 if 73 - 73: oO0o0ooO0 / o0oO0 + Ooo00oOo00o / I1IiI . OoOoOO00 * o00O0oo
elif Ii1iI111 == 5 :
 ooooo0O0000oo ( II1I , I1Ii1iI1 , o00oooO0Oo )
 if 21 - 21: OOOo0 - OOOo0 + oO0o0ooO0 % OOOo0 * OoOO
elif Ii1iI111 == 6 :
 Oo00oo00o00Oo ( I1Ii1iI1 )
 if 74 - 74: oO0o0ooO0 / o0000oOoOoO0o . OOOo0 - OoooooooOO + OoOoOO00 + o0000oOoOoO0o
elif Ii1iI111 == 7 :
 III1 ( I1Ii1iI1 , II1I )
 if 36 - 36: o00O0oo * OOOo0 * ii11ii1ii . o0000oOoOoO0o * ii11ii1ii
elif Ii1iI111 == 8 :
 oOO0O0ooOOOo ( I1Ii1iI1 , II1I )
 if 76 - 76: OoOO0ooOOoo0O + O0 / IIII - Ooo00oOo00o
elif Ii1iI111 == 9 :
 FIXREPOSADDONS ( I1Ii1iI1 )
 if 27 - 27: Oo - iIii1I11I1II1 * oO0o0ooO0 * OoOoOO00 * ii11ii1ii
elif Ii1iI111 == 10 :
 OO0O0 ( )
 if 9 - 9: i11iIiiIii + OoOO0ooOOoo0O - I1IiI / o0oO0 % i1IIi / OoOO
elif Ii1iI111 == 11 :
 II11iiIIiI11I ( I1Ii1iI1 )
 if 22 - 22: i1IIi
elif Ii1iI111 == 12 :
 OO0oooOO ( )
 if 3 - 3: Ooo00oOo00o * ii11ii1ii - oO0o0ooO0 + ii11ii1ii
elif Ii1iI111 == 13 :
 Ii1IIi11 ( )
 if 63 - 63: o0000oOoOoO0o * o0oO0 % OoOoOO00 % O0oO + OOOo0 * Oo
elif Ii1iI111 == 14 :
 OOoo0OOOo0o ( I1Ii1iI1 )
 if 96 - 96: IIII
elif Ii1iI111 == 15 :
 O0oOoOOOoOO ( )
 if 99 - 99: iIii1I11I1II1 - o0oO0
elif Ii1iI111 == 16 :
 iIIiII1i1ii ( I1Ii1iI1 , II1I )
 if 79 - 79: OOOo0 + OoOO % o0000oOoOoO0o % OoOO
elif Ii1iI111 == 17 :
 iIiiIi1IIIi11 ( I1Ii1iI1 , II1I )
 if 56 - 56: ii11ii1ii + OoOO . Ooo00oOo00o + OoooooooOO * ii11ii1ii - O0
elif Ii1iI111 == 18 :
 I1iiII1 ( )
 if 35 - 35: OoOO0ooOOoo0O . o0000oOoOoO0o . O0oO - o0000oOoOoO0o % o0000oOoOoO0o + O0oO
elif Ii1iI111 == 19 :
 Ii1I1i ( II1I , I1Ii1iI1 , o00oooO0Oo )
 if 99 - 99: OOooOOo + OoOO0ooOOoo0O
elif Ii1iI111 == 40 :
 oOOoo00O00o ( II1I , I1Ii1iI1 , o00oooO0Oo )
 if 34 - 34: O0oO * OOooOOo . OOOo0 % i11iIiiIii
elif Ii1iI111 == 42 :
 o0o0O0O00oOOo ( II1I , I1Ii1iI1 , o00oooO0Oo )
 if 61 - 61: iIii1I11I1II1 + OoOO * o0000oOoOoO0o - i1IIi % OoOO
elif Ii1iI111 == 43 :
 o00oo0 ( II1I , I1Ii1iI1 , o00oooO0Oo )
 if 76 - 76: OoOO / I1IiI
elif Ii1iI111 == 20 :
 Oo0oO ( I1Ii1iI1 )
 if 12 - 12: O0oO
elif Ii1iI111 == 22 :
 oO0ooo0O0Ooo ( I1Ii1iI1 )
 if 58 - 58: Ooo00oOo00o + iIii1I11I1II1 % O0 + o0000oOoOoO0o + I1IiI * OoooooooOO
elif Ii1iI111 == 23 :
 I1I11i ( I1Ii1iI1 )
 if 41 - 41: OoOO * OOOo0
elif Ii1iI111 == 24 :
 oooO0oooOo000 ( I1Ii1iI1 )
 if 76 - 76: OoOO . O0 * OoooooooOO + o0oO0
elif Ii1iI111 == 25 :
 O0oo0ooo0 ( I1Ii1iI1 )
 if 53 - 53: Oo
elif Ii1iI111 == 26 :
 o00O0o ( I1Ii1iI1 )
 if 3 - 3: IIII - OoooooooOO * OoooooooOO - OOOo0 / O0oO * ii11ii1ii
elif Ii1iI111 == 27 :
 o0oOo ( I1Ii1iI1 )
 if 58 - 58: IIII % iIii1I11I1II1 / i11iIiiIii % OOooOOo . O0oO * oO0o0ooO0
elif Ii1iI111 == 28 :
 iI1I ( I1Ii1iI1 )
 if 32 - 32: OoooooooOO + OOooOOo
elif Ii1iI111 == 29 :
 II1IIii1I11I ( I1Ii1iI1 )
 if 91 - 91: o0oO0 - O0oO * O0oO
elif Ii1iI111 == 30 :
 o0Ooo00o0Oooo ( I1Ii1iI1 )
 if 55 - 55: iIii1I11I1II1 + OOOo0 - Oo
elif Ii1iI111 == 31 :
 I1I1 ( I1Ii1iI1 )
 if 24 - 24: Ooo00oOo00o / O0oO + oO0o0ooO0 * o0000oOoOoO0o * oO0o0ooO0
elif Ii1iI111 == 32 :
 Ii1I ( )
 if 10 - 10: OOOo0 - ii11ii1ii - Oo - OOooOOo
elif Ii1iI111 == 33 :
 OOooOoooOoOo ( )
 if 21 - 21: OoooooooOO + O0oO
elif Ii1iI111 == 35 :
 IiI1iIiIIIii ( I1Ii1iI1 )
 if 43 - 43: i11iIiiIii . ii11ii1ii . OoOO
elif Ii1iI111 == 34 :
 iI111i ( I1Ii1iI1 )
 if 31 - 31: o00O0oo % OOooOOo % O0oO . ii11ii1ii / OOooOOo * OoOO
elif Ii1iI111 == 36 :
 OOO00O0O ( I1Ii1iI1 )
 if 74 - 74: OOOo0 . o0oO0 / oO0o0ooO0 . IIII
elif Ii1iI111 == 37 :
 IIi ( I1Ii1iI1 )
 if 74 - 74: Oo / O0oO % O0oO . IIII
elif Ii1iI111 == 38 :
 O000OOOOOo ( I1Ii1iI1 )
 if 72 - 72: i1IIi
elif Ii1iI111 == 41 :
 i11IiII ( o00IIIIii1111i1 )
 if 21 - 21: O0oO . OoOO0ooOOoo0O / i11iIiiIii * i1IIi
elif Ii1iI111 == 39 :
 I1Ii1II ( I1Ii1iI1 )
 if 82 - 82: o0oO0 * Oo % i11iIiiIii * i1IIi . OoOO0ooOOoo0O
elif Ii1iI111 == 45 :
 TEXTS ( )
 if 89 - 89: IIII - i1IIi - IIII
elif Ii1iI111 == 46 :
 iI1iiIiI ( )
 if 74 - 74: Ooo00oOo00o % Ooo00oOo00o
elif Ii1iI111 == 47 :
 GEVID ( )
 if 28 - 28: I1IiI % OoOO - OoOO0ooOOoo0O + OoOO0ooOOoo0O + OoOO / iIii1I11I1II1
elif Ii1iI111 == 48 :
 IIo0Oo0oO0oOO00 ( II1I , I1Ii1iI1 , o00oooO0Oo )
 if 91 - 91: OOOo0 / OoOoOO00 * OoOO0ooOOoo0O
elif Ii1iI111 == 49 :
 Ii ( )
 if 94 - 94: OoOoOO00 - iIii1I11I1II1 - iIii1I11I1II1
elif Ii1iI111 == 222 :
 ii ( I1Ii1iI1 )
 if 83 - 83: ii11ii1ii * iIii1I11I1II1 + I1IiI * i1IIi . OoooooooOO % o00O0oo
elif Ii1iI111 == 333 :
 ii1iIII1ii ( I1Ii1iI1 )
 if 81 - 81: Ooo00oOo00o - iIii1I11I1II1
 if 60 - 60: O0oO
elif Ii1iI111 == 1001 :
 oooO0o ( )
 if 77 - 77: OOOo0 / ii11ii1ii
elif Ii1iI111 == 1005 :
 oOo0OoOOOo0 ( )
 if 95 - 95: O0oO * i1IIi + OoOO
elif Ii1iI111 == 1007 :
 OOoo00 ( I1Ii1iI1 )
 if 40 - 40: OoOoOO00
elif Ii1iI111 == 1010 :
 OOo00Oooo ( I1Ii1iI1 )
 if 7 - 7: OoOO0ooOOoo0O / Ooo00oOo00o
elif Ii1iI111 == 1011 :
 I1 ( I1Ii1iI1 )
 if 88 - 88: i1IIi
elif Ii1iI111 == 1030 :
 oO0oOOOooo ( )
 if 53 - 53: o0oO0 . OoOO0ooOOoo0O . OOooOOo + OoOO
elif Ii1iI111 == 1031 :
 Ii1iiI1i1 ( I1Ii1iI1 , O0i1II1Iiii1I11 )
 if 17 - 17: iIii1I11I1II1 + i1IIi . ii11ii1ii + o00O0oo % i1IIi . OoOO
elif Ii1iI111 == 1006 :
 Parse . ParseURL ( I1Ii1iI1 )
 if 57 - 57: OoOO
elif Ii1iI111 == 2030 :
 Parse . addonParseURL ( I1Ii1iI1 )
 if 92 - 92: OoOoOO00 - Ooo00oOo00o - OoOO0ooOOoo0O % OOOo0 - I1IiI * O0oO
elif Ii1iI111 == 2031 :
 Parse . apkParseURL ( I1Ii1iI1 )
 if 16 - 16: iIii1I11I1II1 + OoooooooOO - o0oO0 * IIII
elif Ii1iI111 == 1002 :
 O00O0Oo0 ( I1Ii1iI1 )
 if 37 - 37: oO0o0ooO0
elif Ii1iI111 == 1003 :
 OoO ( I1Ii1iI1 , O0i1II1Iiii1I11 )
 if 15 - 15: OOooOOo % Ooo00oOo00o / oO0o0ooO0
elif Ii1iI111 == 1004 :
 iI11IiI1i1 ( I1Ii1iI1 )
 if 36 - 36: Ooo00oOo00o + Ooo00oOo00o % Oo + Oo / i1IIi % i1IIi
elif Ii1iI111 == 1008 :
 Ii1iiI1 ( )
 if 20 - 20: OoOO0ooOOoo0O * OoOO
elif Ii1iI111 == 1009 :
 M3UPLAY ( I1Ii1iI1 )
 if 91 - 91: Ooo00oOo00o % i1IIi - iIii1I11I1II1 . OoOO0ooOOoo0O
elif Ii1iI111 == 2001 :
 iIi1i111 ( I1Ii1iI1 )
 if 31 - 31: OoOO % i1IIi . OoooooooOO - OOooOOo + OoooooooOO
elif Ii1iI111 == 1013 :
 i1iI ( )
 if 45 - 45: OoOO0ooOOoo0O + o0000oOoOoO0o / OoooooooOO - o00O0oo + OoooooooOO
elif Ii1iI111 == 1014 :
 O0oO0OOoO ( )
 if 42 - 42: iIii1I11I1II1 * OOOo0 * O0oO
elif Ii1iI111 == 1015 :
 O00oo ( I1Ii1iI1 )
 if 62 - 62: OoOO0ooOOoo0O * O0 % IIII . IIII . OOOo0
elif Ii1iI111 == 1016 :
 I11I111i1I1 ( I1Ii1iI1 )
 if 91 - 91: i1IIi . oO0o0ooO0
elif Ii1iI111 == 1023 :
 iI1ii1Ii ( )
 if 37 - 37: oO0o0ooO0 - o0000oOoOoO0o + iIii1I11I1II1 / O0oO - Ooo00oOo00o . OOooOOo
elif Ii1iI111 == 1024 :
 O0O0O ( )
 if 62 - 62: ii11ii1ii
elif Ii1iI111 == 1025 :
 II1io0Oo00oOO ( I1Ii1iI1 )
 if 47 - 47: O0oO % OoOO0ooOOoo0O * Ooo00oOo00o . iIii1I11I1II1 % Oo + OoooooooOO
elif Ii1iI111 == 4001 :
 oOii1i1I1i ( )
 if 2 - 2: O0oO % OoooooooOO - o0oO0 * ii11ii1ii * IIII
elif Ii1iI111 == 4002 :
 o00oOO0 ( )
 if 99 - 99: iIii1I11I1II1 . Oo / o0oO0 . OoOO0ooOOoo0O % OOOo0 * o0000oOoOoO0o
elif Ii1iI111 == 4003 :
 O00o0O00 ( )
 if 95 - 95: OoOO
elif Ii1iI111 == 3000 :
 o00OO0o0 ( )
 if 80 - 80: IIII
elif Ii1iI111 == 404 :
 OooO00oo0O0 ( II1I , I1Ii1iI1 , O0i1II1Iiii1I11 )
 if 42 - 42: OoooooooOO * OoOoOO00
elif Ii1iI111 == 7030 :
 iiI1ii111 ( )
 if 53 - 53: O0oO + i1IIi . Ooo00oOo00o / i11iIiiIii + o00O0oo % I1IiI
elif Ii1iI111 == 7021 :
 OOooOO ( II1I )
 if 9 - 9: o0oO0 . o0000oOoOoO0o - Oo . O0oO
elif Ii1iI111 == 7022 :
 o0O0Ooo ( II1I )
 if 39 - 39: OoOO0ooOOoo0O
elif Ii1iI111 == 7000 :
 i11iI1 ( II1I , I1Ii1iI1 , img )
 if 70 - 70: IIII % Ooo00oOo00o % OOOo0
elif Ii1iI111 == 7050 :
 iiI1iI ( )
 if 95 - 95: I1IiI - O0oO / O0 * OOOo0 - OOooOOo
elif Ii1iI111 == 7051 :
 OOoO0oooo ( I1Ii1iI1 )
 if 12 - 12: iIii1I11I1II1 % Oo . oO0o0ooO0 . IIII % i11iIiiIii
elif Ii1iI111 == 7060 :
 IiI11I111 ( )
 if 2 - 2: OoOO * OoOO . I1IiI * o00O0oo * iIii1I11I1II1
elif Ii1iI111 == 7061 :
 i11iioOOOOO0Ooooo ( I1Ii1iI1 )
 if 13 - 13: o0000oOoOoO0o / O0 . i11iIiiIii * i1IIi % i11iIiiIii
elif Ii1iI111 == 7063 :
 Ooo000O00 ( I1Ii1iI1 )
 if 8 - 8: I1IiI - OoooooooOO
elif Ii1iI111 == 7062 :
 oOO00ooOOo ( I1Ii1iI1 )
 if 99 - 99: OoOoOO00 / IIII % OoooooooOO . i11iIiiIii
elif Ii1iI111 == 7064 :
 NATatozcat ( )
 if 18 - 18: OOooOOo . o0oO0
elif Ii1iI111 == 7067 :
 IIiiiiIiI1III ( I1Ii1iI1 )
 if 70 - 70: OoooooooOO . o0oO0 / OoOO . OoOO - OOooOOo
elif Ii1iI111 == 7066 :
 NATatozA ( I1Ii1iI1 )
 if 29 - 29: o0000oOoOoO0o % OoOO0ooOOoo0O - o0oO0
elif Ii1iI111 == 7065 :
 iIiI ( I1Ii1iI1 )
 if 26 - 26: O0 . o0000oOoOoO0o + oO0o0ooO0 - o00O0oo . o0000oOoOoO0o
elif Ii1iI111 == 7070 :
 O0oooOoO ( )
 if 2 - 2: ii11ii1ii . Oo * OoOO0ooOOoo0O % OoOoOO00 . oO0o0ooO0
elif Ii1iI111 == 7071 :
 DIZIlist ( I1Ii1iI1 )
 if 46 - 46: I1IiI + OOOo0 % OoooooooOO * i11iIiiIii - Oo
elif Ii1iI111 == 7072 :
 DIZIpull ( I1Ii1iI1 )
 if 47 - 47: oO0o0ooO0 * I1IiI * IIII
elif Ii1iI111 == 7073 :
 WATCHDIZI ( I1Ii1iI1 )
 if 46 - 46: o00O0oo
elif Ii1iI111 == 7002 :
 i1IiIIi ( )
 if 42 - 42: iIii1I11I1II1
elif Ii1iI111 == 7003 :
 i1i1IIII ( I1Ii1iI1 )
 if 32 - 32: Oo - o00O0oo . OoooooooOO - OoooooooOO - Oo . iIii1I11I1II1
elif Ii1iI111 == 7004 :
 OOOO0O0OOoo ( I1Ii1iI1 )
 if 34 - 34: Oo
elif Ii1iI111 == 7020 :
 i1IiiI ( I1Ii1iI1 )
 if 31 - 31: i1IIi - o0000oOoOoO0o + O0oO + o0oO0 . o0oO0 . O0
elif Ii1iI111 == 7001 :
 ooO0 ( )
 if 33 - 33: i1IIi / oO0o0ooO0 * Ooo00oOo00o
elif Ii1iI111 == 7010 :
 oooOoo0OoOO0000 ( I1Ii1iI1 )
 if 2 - 2: OoOO . OoOO0ooOOoo0O
elif Ii1iI111 == 7011 :
 I1IIIIIi1IIiI ( I1Ii1iI1 )
 if 43 - 43: iIii1I11I1II1
elif Ii1iI111 == 7012 :
 OOoO0oO00o ( I1Ii1iI1 )
 if 29 - 29: IIII % o0oO0 + Ooo00oOo00o . i1IIi + OOOo0
elif Ii1iI111 == 7013 :
 cnfTVPlay2 ( I1Ii1iI1 )
elif Ii1iI111 == 7014 :
 CNF_Studio_Indexer . MV_Movies ( I1Ii1iI1 )
elif Ii1iI111 == 7015 :
 CNF_Studio_Indexer . Movie_ByYear ( I1Ii1iI1 )
elif Ii1iI111 == 7016 :
 CNF_Studio_Indexer . Resolve_CNF_Link ( II1I , I1Ii1iI1 , O0i1II1Iiii1I11 )
elif Ii1iI111 == 7017 :
 CNF_Studio_Indexer . Search_Movie ( )
elif Ii1iI111 == 7018 :
 o00OOo0o0O ( )
elif Ii1iI111 == 7019 :
 CNF_Studio_Indexer . List_Movies ( I1Ii1iI1 )
elif Ii1iI111 == 7020 :
 CNF_Studio_Indexer . Get_Movie_Page ( I1Ii1iI1 )
elif Ii1iI111 == 7024 :
 CNF_Studio_Indexer . Box_Office ( I1Ii1iI1 )
 if 24 - 24: O0oO / o00O0oo * ii11ii1ii - OoooooooOO / OOOo0 . OoOO
elif Ii1iI111 == 8000 :
 i11i1i ( )
elif Ii1iI111 == 8001 :
 i111I11I ( )
elif Ii1iI111 == 8002 :
 IiiI11I1IIiI ( )
elif Ii1iI111 == 8003 :
 o0o0OoO0OOO0 ( )
elif Ii1iI111 == 8004 :
 o0iIIIIi ( )
elif Ii1iI111 == 8005 :
 iiII1iiiiiii ( )
elif Ii1iI111 == 8006 :
 iIiI1ii ( II1I , I1Ii1iI1 )
elif Ii1iI111 == 8030 :
 IIi1 ( I1Ii1iI1 )
elif Ii1iI111 == 8045 :
 iI1IiiiIiI1Ii ( )
elif Ii1iI111 == 8046 :
 Oo000 ( I1Ii1iI1 )
elif Ii1iI111 == 8047 :
 i11i11 ( I1Ii1iI1 )
elif Ii1iI111 == 8040 :
 o00iI1i1II ( )
elif Ii1iI111 == 8041 :
 I1ii1ii1I ( I1Ii1iI1 )
elif Ii1iI111 == 8042 :
 IIiIi1iI1iII ( I1Ii1iI1 )
elif Ii1iI111 == 8043 :
 yt . PlayVideo ( I1Ii1iI1 )
elif Ii1iI111 == 8044 :
 OoOo00o ( I1Ii1iI1 )
elif Ii1iI111 == 8060 :
 II11I ( )
elif Ii1iI111 == 8061 :
 o00OoooooooOo ( I1Ii1iI1 )
elif Ii1iI111 == 8070 :
 iIi ( )
elif Ii1iI111 == 8071 :
 Ii1Ii11IiI1I1 ( I1Ii1iI1 )
elif Ii1iI111 == 7080 :
 OOo ( I1Ii1iI1 )
elif Ii1iI111 == 8090 :
 o0OO0OOO0O ( )
elif Ii1iI111 == 8091 :
 Iii1I ( I1Ii1iI1 )
elif Ii1iI111 == 8092 :
 oOoOOOOoOO0o ( I1Ii1iI1 )
elif Ii1iI111 == 8081 :
 iIII11Iiii1 ( )
elif Ii1iI111 == 8062 :
 ii1IOoo000000 ( I1Ii1iI1 )
elif Ii1iI111 == 8063 :
 O0OO0ooO00 ( I1Ii1iI1 )
elif Ii1iI111 == 8050 :
 iI1i111I1Ii ( )
elif Ii1iI111 == 8051 :
 i11i1ii1I ( I1Ii1iI1 )
elif Ii1iI111 == 8052 :
 OOOoOO ( I1Ii1iI1 )
elif Ii1iI111 == 8085 :
 ii1I11i ( )
elif Ii1iI111 == 8086 :
 IiI1 ( I1Ii1iI1 )
elif Ii1iI111 == 8087 :
 IIiI1111i1 ( I1Ii1iI1 )
elif Ii1iI111 == 8088 :
 ii1ii1I1IIi1 ( I1Ii1iI1 , II1I )
elif Ii1iI111 == 9000 :
 oO0o0OOOO ( )
elif Ii1iI111 == 1111 :
 OoOO0o0o0 ( )
elif Ii1iI111 == 9001 :
 iI1ii11Ii ( )
elif Ii1iI111 == 9002 :
 o0oO0OO00oo0o ( )
elif Ii1iI111 == 9003 :
 OOO0O00Oo ( )
elif Ii1iI111 == 50 :
 oOo0O0Oo00oO ( I1Ii1iI1 )
elif Ii1iI111 == 9020 :
 i1OOO ( )
elif Ii1iI111 == 9021 :
 iI1iiIi1 ( )
elif Ii1iI111 == 9022 :
 i1iiiIi1Iii ( )
elif Ii1iI111 == 9023 :
 o0oO0O ( )
elif Ii1iI111 == 9024 :
 o0o0O00o ( I1Ii1iI1 )
elif Ii1iI111 == 9030 :
 iIIiiiI1iI1 ( I1Ii1iI1 )
elif Ii1iI111 == 9031 :
 oO00000oO0o0O ( I1Ii1iI1 )
elif Ii1iI111 == 9032 :
 IIIiI1iI1 ( I1Ii1iI1 )
elif Ii1iI111 == 9033 :
 IIiIiiii1I1 ( I1Ii1iI1 )
elif Ii1iI111 == 7085 :
 o0o ( I1Ii1iI1 )
elif Ii1iI111 == 7086 :
 O00Ooo ( I1Ii1iI1 )
elif Ii1iI111 == 7087 :
 ii111I11Ii ( o00oooO0Oo )
elif Ii1iI111 == 9666 :
 i11iIi ( I1Ii1iI1 )
elif Ii1iI111 == 10100 : oooO00Oo ( )
elif Ii1iI111 == 10105 : iiiii1I1III1 ( I1Ii1iI1 )
elif Ii1iI111 == 10106 : I11i1iIi111 ( I1Ii1iI1 )
elif Ii1iI111 == 10104 : OooooO ( I1Ii1iI1 )
elif Ii1iI111 == 10107 : ii1I ( )
elif Ii1iI111 == 10103 : IIii1i11iI1II11 ( I1Ii1iI1 )
elif Ii1iI111 == 10108 : ii1IIi1ii ( I1Ii1iI1 )
elif Ii1iI111 == 10107 : ii1I ( )
elif Ii1iI111 == 10000 : oO000Oo000 ( )
elif Ii1iI111 == 10001 : I1IiIiiIiIII ( )
elif Ii1iI111 == 10002 : Oo0O0O00Oo ( )
elif Ii1iI111 == 10003 : Oo0ooo ( )
elif Ii1iI111 == 10004 : oO00O0 ( )
elif Ii1iI111 == 10005 : o0oO000oo ( )
elif Ii1iI111 == 10006 : OooOOOO ( I1Ii1iI1 )
elif Ii1iI111 == 10007 : iiII1i11i ( I1Ii1iI1 , O0i1II1Iiii1I11 )
elif Ii1iI111 == 10008 : o0OO ( )
elif Ii1iI111 == 10009 : o00oooOo ( )
elif Ii1iI111 == 10010 : OO0o0oO0O000o ( I1Ii1iI1 )
elif Ii1iI111 == 10011 : O00oO0o ( I1Ii1iI1 )
elif Ii1iI111 == 10012 : II1IIiiIiI ( I1Ii1iI1 )
elif Ii1iI111 == 10013 : I1i1Ii111IIii ( I1Ii1iI1 )
elif Ii1iI111 == 10014 : O00O0Ooooo00 ( )
elif Ii1iI111 == 10015 : II11iI111i1 ( )
elif Ii1iI111 == 10016 : oo0o0O0Oooooo ( I1Ii1iI1 )
elif Ii1iI111 == 10017 : Oooo00 ( )
elif Ii1iI111 == 10018 : o000 ( )
elif Ii1iI111 == 10019 : I1i11II ( )
elif Ii1iI111 == 10020 : iiIii1I ( )
elif Ii1iI111 == 10021 : oO00oOo0OOO ( )
elif Ii1iI111 == 10022 : I11IIIiIi11 ( I1Ii1iI1 )
elif Ii1iI111 == 10023 : iI ( II1I , I1Ii1iI1 )
elif Ii1iI111 == 10024 : IIIIiii ( I1Ii1iI1 )
elif Ii1iI111 == 10025 : oOOoOo ( )
elif Ii1iI111 == 10026 : O00oO ( )
elif Ii1iI111 == 10027 : OOOoO000 ( )
elif Ii1iI111 == 10028 : oOOoo0o0OOOO ( )
elif Ii1iI111 == 10029 : oOO0 ( )
elif Ii1iI111 == 423 : OOOoO ( I1Ii1iI1 )
elif Ii1iI111 == 426 : ooo0o0O0o ( I1Ii1iI1 )
elif Ii1iI111 == 10030 : IIii11I1i1I ( )
elif Ii1iI111 == 10031 : Latest_Izle_Movies ( )
elif Ii1iI111 == 10032 : OooO0oo ( )
elif Ii1iI111 == 10033 : I1II ( )
elif Ii1iI111 == 10034 : oOOOOoo ( )
elif Ii1iI111 == 10035 : iiI1ii11i1 ( )
elif Ii1iI111 == 10036 : ooOoOO0OoO00o ( I1Ii1iI1 )
elif Ii1iI111 == 10037 : oOi11iI11iIiIi ( I1Ii1iI1 )
elif Ii1iI111 == 10038 : O0OoOO0oo0 ( )
elif Ii1iI111 == 10039 : O0OoO0ooOO0o ( I1Ii1iI1 )
elif Ii1iI111 == 10040 : oOO0o000Oo00o ( )
elif Ii1iI111 == 10041 : OoOo ( I1Ii1iI1 )
elif Ii1iI111 == 10042 : i11ii ( I1Ii1iI1 )
elif Ii1iI111 == 10043 : iiII ( )
elif Ii1iI111 == 10044 : IIIiiiI ( I1Ii1iI1 )
elif Ii1iI111 == 10045 : oo0ooO0 ( II1I )
elif Ii1iI111 == 10046 : I1iI1I1 ( I1Ii1iI1 )
elif Ii1iI111 == 10047 : Ooooo0OoO0 ( I1Ii1iI1 )
elif Ii1iI111 == 10048 : iIi1i ( I1Ii1iI1 )
elif Ii1iI111 == 10049 : OOoOO0OO ( I1Ii1iI1 )
elif Ii1iI111 == 10050 : O00o0000OO ( )
elif Ii1iI111 == 10051 : o0O00OooooO ( )
elif Ii1iI111 == 10052 : iIiii1iI1i ( )
elif Ii1iI111 == 10053 : Addon ( I1Ii1iI1 )
elif Ii1iI111 == 10054 : iiIIIIiii ( I1Ii1iI1 , II1I )
elif Ii1iI111 == 10055 :
 iII1I1 ( "addFavorite" )
 try :
  II1I = II1I . split ( '\\ ' ) [ 1 ]
 except :
  pass
 try :
  II1I = II1I . split ( '  - ' ) [ 0 ]
 except :
  pass
 ii1iii11i1 ( II1I , I1Ii1iI1 , O0i1II1Iiii1I11 , IIIIiiIiI , I1iI1 )
elif Ii1iI111 == 10056 :
 iII1I1 ( "rmFavorite" )
 try :
  II1I = II1I . split ( '\\ ' ) [ 1 ]
 except :
  pass
 try :
  II1I = II1I . split ( '  - ' ) [ 0 ]
 except :
  pass
 o0O ( II1I )
elif Ii1iI111 == 10057 :
 iII1I1 ( "getFavorites" )
 iIIIII1iiiiII ( )
elif Ii1iI111 == 10058 : oo000OO00Oo ( )
elif Ii1iI111 == 20000 : II1i11I ( )
elif Ii1iI111 == 20001 : IIii1111 ( )
elif Ii1iI111 == 20002 : oo0o0000 ( I1Ii1iI1 )
elif Ii1iI111 == 20003 : O00O ( I1Ii1iI1 )
elif Ii1iI111 == 20004 : iI1iIii11Ii ( I1Ii1iI1 )
if 98 - 98: i1IIi - oO0o0ooO0
xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
