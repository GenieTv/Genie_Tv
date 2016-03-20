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
iiI1IiI = "2.5.0"
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
 if o0oOoO00o . getSetting ( 'CLASSIC MOVIES' ) == 'true' :
  ooooooO0oo ( '[COLORgreen]CLASSIC MOVIES[/COLOR]' , '' , 8060 , oOOoO0 + 'classicmovies.png' , OOooO0OOoo , '' )
 if o0oOoO00o . getSetting ( 'CLASSIC TV' ) == 'true' :
  ooooooO0oo ( '[COLORgreen]CLASSIC TV[/COLOR]' , OO0o , 8064 , oOOoO0 + 'classictv.png' , OOooO0OOoo , '' )
 if o0oOoO00o . getSetting ( 'Disclose' ) == 'true' :
  ooooooO0oo ( '[COLORgreen]DISCLOSE TV[/COLOR]' , OO0o , 7001 , oOOoO0 + 'disclose.png' , OOooO0OOoo , '' )
 if o0oOoO00o . getSetting ( 'Go Fishing' ) == 'true' :
  ooooooO0oo ( '[COLORgreen]Go Fishing[/COLOR]' , OO0o , 8090 , oOOoO0 + 'gofish.png' , OOooO0OOoo , '' )
 if o0oOoO00o . getSetting ( 'GenieTv Kitchen' ) == 'true' :
  ooooooO0oo ( '[COLORgreen]GenieTv Kitchen[/COLOR]' , ( oOo0oooo00o ( 'aHR0cDovL2Zvb2QubmR0di5jb20vdmlkZW9z' ) ) , 8045 , oOOoO0 + 'geniekitchen.png' , OOooO0OOoo , '' )
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
 I1i1I1II ( 'movies' , 'MAIN' )
 if 21 - 21: Ooo00oOo00o * iIii1I11I1II1 % OoOO * i1IIi
def Ii11Ii1I ( ) :
 if i1iiIII111ii == 'insert_password' :
  Oo0o0000o0o0 . ok ( '[COLORgreen]Donators Login[/COLOR]' , 'You need to set username and password to access this' , 'These are unique and provided to donators to help with server and stream costs' , 'Donate @ [COLORgreen]http://architects.x10host.com[/COLOR]' )
  o0oOoO00o . openSettings ( sys . argv [ 0 ] )
 else :
  ooooooO0oo ( '[COLORgreen]DONATORS LIST[/COLOR]' , OO0o + '/thelist.m3u' , 7080 , oOOoO0 + 'GTVIPTV.png' , OOooO0OOoo , '' )
  if 72 - 72: oO0o0ooO0 / i1IIi * Oo - O0oO
  if 51 - 51: OoOoOO00 * Ooo00oOo00o % OOooOOo * OoOoOO00 % ii11ii1ii / o0oO0
def iIIIIii1 ( ) :
 ooooooO0oo ( '[COLORgreen]Cartoons[/COLOR]' , '' , 10001 , oOOoO0 + 'ORIGINCARTOON.png' , OOooO0OOoo , '' )
 ooooooO0oo ( '[COLORgreen]Dizzy TV[/COLOR]' , '' , 10018 , oOOoO0 + 'dtv.png' , OOooO0OOoo , '' )
 ooooooO0oo ( '[COLORgreen]Football[/COLOR]' , '' , 10002 , oOOoO0 + 'ORIGINFOOTBALL.png' , OOooO0OOoo , '' )
 ooooooO0oo ( '[COLORgreen]Izle Films[/COLOR]' , '' , 10030 , oOOoO0 + 'IZLEFILMS.png' , OOooO0OOoo , '' )
 ooooooO0oo ( '[COLORgreen]Stand Up[/COLOR]' , '' , 10003 , oOOoO0 + 'ORIGINSTANDUP.png' , OOooO0OOoo , '' )
 if 58 - 58: i11iIiiIii % o0000oOoOoO0o
 if 71 - 71: OoOO0ooOOoo0O + o0oO0 % i11iIiiIii + ii11ii1ii - IIII
def oO0OOoO0 ( ) :
 ooooooO0oo ( '[COLORgreen]SCOOBY STREAMS[/COLOR]' , ( oOo0oooo00o ( 'aHR0cDovL3Njb29ieXN0cmVhbS54MTBob3N0LmNvbS9zY29vYnkvdHZjYXRzLnBocA==' ) ) , 1016 , oOOoO0 + 'scoob.png' , OOooO0OOoo , '' )
 ooooooO0oo ( '[COLORgreen]SCOOBY SCRAPES[/COLOR]' , OO0o , 1024 , oOOoO0 + 'scoob.png' , OOooO0OOoo , '' )
 if 34 - 34: IIII - IIII * OOOo0 + o00O0oo % IIII
def i111IiI1I ( ) :
 ooooooO0oo ( '[COLORgreen]Live Tv[/COLOR]' , OO0o , 9021 , oOOoO0 + 'english.png' , OOooO0OOoo , '' )
 ooooooO0oo ( '[COLORgreen]XXX[/COLOR]' , OO0o , 9022 , oOOoO0 + 'xxx.png' , OOooO0OOoo , '' )
 ooooooO0oo ( '[COLORgreen]Hd VOD[/COLOR]' , OO0o , 9023 , oOOoO0 + 'vod(1).png' , OOooO0OOoo , '' )
 if 70 - 70: o00O0oo . Oo / OOooOOo . o00O0oo - O0 / IIII
 if 62 - 62: iIii1I11I1II1 * I1IiI
def i1OOO ( ) :
 ooooooO0oo ( '[COLORgreen]SEARCH MOVIES[/COLOR]' , OO0o , 9001 , oOOoO0 + 'MOVIESv.png' , OOooO0OOoo , '' )
 ooooooO0oo ( '[COLORgreen]SEARCH SERIES[/COLOR]' , OO0o , 9002 , oOOoO0 + 'TVSHOWSv.png' , OOooO0OOoo , '' )
 ooooooO0oo ( '[COLORgreen]SEARCH CARTOONS[/COLOR]' , '' , 10005 , oOOoO0 + 'ORIGINCARTOON' , OOooO0OOoo , '' )
 ooooooO0oo ( '[COLORgreen]SEARCH LiveTv[/COLOR]' , OO0o , 9003 , oOOoO0 + 'livetv.png' , OOooO0OOoo , '' )
 if 59 - 59: OoOoOO00 + OoooooooOO * I1IiI + i1IIi
 if 58 - 58: OoOoOO00 * OoOO0ooOOoo0O * ii11ii1ii / OoOO0ooOOoo0O
def oO0o0OOOO ( ) :
 ooooooO0oo ( '[COLORgreen]RADIO[/COLOR]' , OO0o , 1013 , oOOoO0 + 'radio.png' , OOooO0OOoo , '' )
 ooooooO0oo ( '[COLORgreen]MUSIC[/COLOR]' , OO0o , 1030 , oOOoO0 + 'MUSIC.png' , OOooO0OOoo , '' )
 ooooooO0oo ( '[COLORgreen]MUSIC ARCHIVE[/COLOR]' , OO0o + ( oOo0oooo00o ( 'L3ZvZC91cmxzL211c2ljLnBocA==' ) ) , 1010 , oOOoO0 + 'MUSIC.png' , OOooO0OOoo , '' )
 ooooooO0oo ( '[COLORgreen]MUSIC SEARCH[/COLOR]' , OO0o , 1111 , oOOoO0 + 'search.png' , OOooO0OOoo , '' )
 ooooooO0oo ( '[COLORgreen]AUDIO BOOKS[/COLOR]' , 'http://doremisa.com/audiobooks/' , 1006 , oOOoO0 + 'search.png' , OOooO0OOoo , '' )
 if 68 - 68: oO0o0ooO0 - O0oO - OOOo0 - ii11ii1ii + o0000oOoOoO0o
 I1i1I1II ( 'movies' , 'MAIN' )
 if 10 - 10: OoooooooOO % iIii1I11I1II1
def O00o0O00 ( ) :
 if 34 - 34: o0oO0
 I1111I1iII11 ( 'DELETE CACHE' , 'url' , 14 , oOOoO0 + 'MAIN5.png' , OOooO0OOoo , '' )
 I1111I1iII11 ( 'DELETE PACKAGES' , 'url' , 6 , oOOoO0 + 'MAIN4.png' , OOooO0OOoo , '' )
 I1111I1iII11 ( 'FORCE REFRESH' , 'url' , 10 , oOOoO0 + 'MAIN3.png' , OOooO0OOoo , 'Force Refresh All Repos' )
 if 59 - 59: iIii1I11I1II1 * i11iIiiIii / ii11ii1ii * i1IIi * O0
 I1111I1iII11 ( 'CHECK MY IP' , 'url' , 12 , oOOoO0 + 'MAIN2.png' , OOooO0OOoo , '' )
 I1111I1iII11 ( 'ANDROID ONLY DELETE TEXTURE13.DB&THUBMNAIL FOLDER' , 'url' , 13 , oOOoO0 + 'MAIN1.png' , OOooO0OOoo , 'Only Works On Android On Windows It Deletes Your Thumnails Folder But Does Not Delete The Textures13.db' )
 ooooooO0oo ( '[COLORgreen]ADVANCED SETTINGS XML[/COLOR]' , OO0o , 4 , oOOoO0 + 'XML.png' , OOooO0OOoo , '' )
 ooooooO0oo ( '[COLORgreen]URL FIXES[/COLOR]' , OO0o , 20 , oOOoO0 + 'URLFIX.png' , OOooO0OOoo , '' )
 I1i1I1II ( 'movies' , 'MAIN' )
 if 83 - 83: Ooo00oOo00o / O0oO . I1IiI / IIII . I1IiI . OoOO0ooOOoo0O
 if 75 - 75: o0000oOoOoO0o + Ooo00oOo00o . I1IiI . o0oO0 + Oo . Ooo00oOo00o
def O0Oooo0OO ( ) :
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
 if 65 - 65: o00O0oo . iIii1I11I1II1 / O0 - o00O0oo
 if 21 - 21: OOOo0 * iIii1I11I1II1
def oooooOoo0ooo ( ) :
 I1111I1iII11 ( 'CHECK ADVANCED XML' , OO0o , 8 , oOOoO0 + 'XML.png' , OOooO0OOoo , '' )
 I1111I1iII11 ( 'MUCKYS XML' , OO0o + '/wizard/muckys.xml' , 7 , oOOoO0 + 'XML.png' , OOooO0OOoo , '' )
 I1111I1iII11 ( '0CACHE XML' , OO0o + '/wizard/0cache.xml' , 7 , oOOoO0 + 'XML.png' , OOooO0OOoo , '' )
 I1111I1iII11 ( 'MIKEY1234 XML' , OO0o + '/wizard/mikey.xml' , 7 , oOOoO0 + 'XML.png' , OOooO0OOoo , '' )
 I1111I1iII11 ( 'TUXENS XML' , OO0o + '/wizard/tuxens.xml' , 7 , oOOoO0 + 'XML.png' , OOooO0OOoo , '' )
 I1111I1iII11 ( 'P2P RECOMMENDED XML1' , OO0o + '/wizard/p2p1.xml' , 7 , oOOoO0 + 'XML.png' , OOooO0OOoo , '' )
 I1111I1iII11 ( 'P2P RECOMMENDED XML2' , OO0o + '/wizard/p2p2.xml' , 7 , oOOoO0 + 'XML.png' , OOooO0OOoo , '' )
 I1111I1iII11 ( 'DELETE XML' , OO0o , 11 , oOOoO0 + 'XML.png' , OOooO0OOoo , '' )
 I1i1I1II ( 'movies' , 'MAIN' )
 if 6 - 6: o0000oOoOoO0o - o00O0oo + iIii1I11I1II1 - O0oO - i11iIiiIii
def OO0oOO0O ( ) :
 I1111I1iII11 ( '[COLORgreen]My Local Zip[/COLOR]' , oo0o0O00 , 48 , oOOoO0 + 'MB.png' , OOooO0OOoo , '' )
 I1111I1iII11 ( '[COLORgreen]My Online Zip[/COLOR]' , oO0o0o0ooO0oO , 43 , oOOoO0 + 'MB.png' , OOooO0OOoo , '' )
 if 91 - 91: O0
def oOOo0 ( ) :
 I1111I1iII11 ( 'INSTALL FTV GUIDE AND OTHER ADDONS REQUIRED' , OO0o + '/wizard/customftv/ftvguide-addons.zip' , 5 , oOOoO0 + 'FTV4.png' , OOooO0OOoo , '' )
 I1111I1iII11 ( 'FTV GUIDE FIRST RUN SETTINGS' , OO0o + '/wizard/customftv/settings.xml' , 17 , oOOoO0 + 'FTV3.png' , OOooO0OOoo , '' )
 I1111I1iII11 ( 'FTV GUIDE ADDONS2.INI UPDATE DAILY' , 'http://ren.byethost12.com/addons2.ini' , 16 , oOOoO0 + 'FTV1.png' , OOooO0OOoo , '' )
 I1111I1iII11 ( 'RESET FTV DATABASE' , 'url' , 18 , oOOoO0 + 'FTV2.png' , OOooO0OOoo , '' )
 if 54 - 54: O0 - IIII % OoOO0ooOOoo0O
 if 77 - 77: I1IiI / OOOo0 / Ooo00oOo00o + Ooo00oOo00o . OoOO0ooOOoo0O
 if 38 - 38: O0oO
def Ii1 ( ) :
 ooooooO0oo ( '[COLORgreen]SKINS[/COLOR]' , OO0o , 33 , oOOoO0 + 'skinp.png' , OOooO0OOoo , '' )
 ooooooO0oo ( '[COLORgreen]ARTWORK PACKS[/COLOR]' , OO0o , 34 , oOOoO0 + 'artp.png' , OOooO0OOoo , '' )
 ooooooO0oo ( '[COLORgreen]CREATE UNIVERSAL PATHS[/COLOR]' , iI111I11I1I1 , 35 , oOOoO0 + 'GUI.png' , OOooO0OOoo , '' )
 I1i1I1II ( 'movies' , 'MAIN' )
 if 82 - 82: ii11ii1ii - iIii1I11I1II1 / OoOO0ooOOoo0O + o00O0oo
def OOOOoOoo0O0O0 ( url ) :
 OOOo00oo0oO = IIiIi1iI ( i1IiiiI1iI ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1iIi = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( OOOo00oo0oO )
 for ooOOoooooo , url , II1I , O0i1II1Iiii1I11 , IIIIiiIiI in i1iIi :
  ooooooO0oo ( ooOOoooooo , url , 5 , II1I , O0i1II1Iiii1I11 , IIIIiiIiI )
 I1i1I1II ( 'movies' , 'MAIN' )
 if 91 - 91: oO0o0ooO0 % i1IIi % iIii1I11I1II1
def IIi1I11I1II ( ) :
 ooooooO0oo ( '[COLORgreen]GOTHAM SKINS[/COLOR]' , OO0o , 36 , oOOoO0 + 'GSKIN.png' , OOooO0OOoo , '' )
 ooooooO0oo ( '[COLORgreen]HELIX SKINS[/COLOR]' , OO0o , 37 , oOOoO0 + 'HSKIN.png' , OOooO0OOoo , '' )
 ooooooO0oo ( '[COLORgreen]ISENGAARD SKINS[/COLOR]' , iI111I11I1I1 , 38 , oOOoO0 + 'ISKIN.png' , OOooO0OOoo , '' )
 I1i1I1II ( 'movies' , 'MAIN' )
 if 63 - 63: OoooooooOO - Ooo00oOo00o . OoOoOO00 / OOooOOo . I1IiI / O0
def o0OOOO00O0Oo ( url ) :
 OOOo00oo0oO = IIiIi1iI ( OO0o + ii ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1iIi = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( OOOo00oo0oO )
 for ooOOoooooo , url , II1I , O0i1II1Iiii1I11 , IIIIiiIiI in i1iIi :
  ooooooO0oo ( ooOOoooooo , url , 42 , II1I , O0i1II1Iiii1I11 , IIIIiiIiI )
 I1i1I1II ( 'movies' , 'MAIN' )
 if 90 - 90: OOooOOo % i1IIi / Ooo00oOo00o
def IIi ( url ) :
 OOOo00oo0oO = IIiIi1iI ( OO0o + i1Iii1i1I ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1iIi = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( OOOo00oo0oO )
 for ooOOoooooo , url , II1I , O0i1II1Iiii1I11 , IIIIiiIiI in i1iIi :
  ooooooO0oo ( ooOOoooooo , url , 42 , II1I , O0i1II1Iiii1I11 , IIIIiiIiI )
 I1i1I1II ( 'movies' , 'MAIN' )
 if 91 - 91: ii11ii1ii + OOOo0 . OoOO0ooOOoo0O * ii11ii1ii + OOOo0 * Oo
def O000OOOOOo ( url ) :
 OOOo00oo0oO = IIiIi1iI ( OO0o + Iiii1i1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1iIi = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( OOOo00oo0oO )
 for ooOOoooooo , url , II1I , O0i1II1Iiii1I11 , IIIIiiIiI in i1iIi :
  ooooooO0oo ( ooOOoooooo , url , 42 , II1I , O0i1II1Iiii1I11 , IIIIiiIiI )
 I1i1I1II ( 'movies' , 'MAIN' )
 if 84 - 84: OOOo0 . iIii1I11I1II1 % OoooooooOO + o00O0oo % OoooooooOO % Ooo00oOo00o
def IIi1 ( url ) :
 OOOo00oo0oO = IIiIi1iI ( oOo0oooo00o ( 'aHR0cHM6Ly9kbC5kcm9wYm94dXNlcmNvbnRlbnQuY29tL3MvN2ZrMjhndDlwb3QxMjJhL0JVSUxEUy50eHQ/ZGw9MA==' ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1iIi = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( OOOo00oo0oO )
 for ooOOoooooo , url , II1I , O0i1II1Iiii1I11 , IIIIiiIiI in i1iIi :
  ooooooO0oo ( ooOOoooooo , url , 42 , II1I , O0i1II1Iiii1I11 , IIIIiiIiI )
 I1i1I1II ( 'movies' , 'MAIN' )
 if 45 - 45: oO0o0ooO0 / oO0o0ooO0 + O0oO + o0oO0
def iI111i ( url ) :
 OOOo00oo0oO = IIiIi1iI ( OO0o + IIi11i1i1iI1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1iIi = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( OOOo00oo0oO )
 for ooOOoooooo , url , II1I , O0i1II1Iiii1I11 , IIIIiiIiI in i1iIi :
  ooooooO0oo ( ooOOoooooo , url , 40 , II1I , O0i1II1Iiii1I11 , IIIIiiIiI )
 I1i1I1II ( 'movies' , 'MAIN' )
 if 23 - 23: i11iIiiIii + OOooOOo . i1IIi
def o0Ooo00o0Oooo ( url ) :
 OOOo00oo0oO = IIiIi1iI ( OO0o + OOooooO0Oo ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1iIi = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( OOOo00oo0oO )
 for ooOOoooooo , url , II1I , O0i1II1Iiii1I11 , IIIIiiIiI in i1iIi :
  ooooooO0oo ( ooOOoooooo , url , 5 , II1I , O0i1II1Iiii1I11 , IIIIiiIiI )
 I1i1I1II ( 'movies' , 'MAIN' )
 if 91 - 91: OOooOOo . iIii1I11I1II1 / OoOO + i1IIi
def I1i ( ) :
 OOOOO0oo0O0O0 = oOoO0O0o0Oooo ( oOo0oooo00o ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vYXBrdG9vbC9hcGsucGhw' ) )
 i1iIi = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( OOOOO0oo0O0O0 )
 for I1Ii1iI1 , oO0 , ooOOoooooo in i1iIi :
  O0OO0O ( ooOOoooooo , I1Ii1iI1 , 2031 , oOOoO0 + 'APK.png' )
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
 O0O0OOOOoo = os . path . join ( OO , ooOOoooooo + '.mp4' )
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
 OOOo00oo0oO = IIiIi1iI ( oOo0oooo00o ( 'aHR0cDovL2dlbmlldHYuYXJjaGl0ZWN0cy54MTBob3N0LmNvbS90ZXN0L3doLnR4dA==' ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1iIi = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( OOOo00oo0oO )
 for ooOOoooooo , url , II1I , O0i1II1Iiii1I11 , IIIIiiIiI in i1iIi :
  ooooooO0oo ( ooOOoooooo , url , 5 , II1I , O0i1II1Iiii1I11 , IIIIiiIiI )
 try :
  OOOo00oo0oO = IIiIi1iI ( oO00oooOOoOo0 + oooOOOOO + OoOOoOooooOOo ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
  i1iIi = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( OOOo00oo0oO )
  for ooOOoooooo , url , II1I , O0i1II1Iiii1I11 , IIIIiiIiI in i1iIi :
   ooooooO0oo ( ooOOoooooo , url , 5 , II1I , O0i1II1Iiii1I11 , IIIIiiIiI )
 except : pass
 I1i1I1II ( 'movies' , 'INFO' )
 if 87 - 87: OOOo0
 if 58 - 58: I1IiI % OOooOOo
def i1OOoO ( url ) :
 OOOo00oo0oO = IIiIi1iI ( oOo0oooo00o ( 'aHR0cDovL2dlbmlldHYuYXJjaGl0ZWN0cy54MTBob3N0LmNvbS90ZXN0L3doLnR4dA==' ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1iIi = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( OOOo00oo0oO )
 for ooOOoooooo , url , II1I , O0i1II1Iiii1I11 , IIIIiiIiI in i1iIi :
  ooooooO0oo ( ooOOoooooo , url , 43 , II1I , O0i1II1Iiii1I11 , IIIIiiIiI )
 try :
  OOOo00oo0oO = IIiIi1iI ( oO00oooOOoOo0 + oooOOOOO + OoOOoOooooOOo ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
  i1iIi = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( OOOo00oo0oO )
  for ooOOoooooo , url , II1I , O0i1II1Iiii1I11 , IIIIiiIiI in i1iIi :
   ooooooO0oo ( ooOOoooooo , url , 43 , II1I , O0i1II1Iiii1I11 , IIIIiiIiI )
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
 i1iIi = re . compile ( '<tr>.+?<td><a href=".+?"><b>(.+?)</b>.+?<td><a href="(.+?)">' , re . DOTALL ) . findall ( OOOOO0oo0O0O0 )
 for ooOOoooooo , I1Ii1iI1 in i1iIi :
  IiI1iiiIii ( ooOOoooooo , I1Ii1iI1 , 222 , oOOoO0 + 'radio.png' )
  if 7 - 7: O0oO * Ooo00oOo00o - o0oO0 + OoOO0ooOOoo0O * OOOo0 % Ooo00oOo00o
def iI1i111I1Ii ( ) :
 OOOOO0oo0O0O0 = oOoO0O0o0Oooo ( oOo0oooo00o ( 'aHR0cDovL3d3dy50b29uamV0LmNvbS8=' ) )
 i1iIi = re . compile ( '<a href="(.+?)" style="font-size:.8em;">(.+?)</a>' ) . findall ( OOOOO0oo0O0O0 )
 for I1Ii1iI1 , ooOOoooooo in i1iIi :
  O0OO0O ( '[COLORgreen]' + ooOOoooooo + '[/COLOR]' , 'http://www.toonjet.com/' + I1Ii1iI1 , 8051 , oOOoO0 + 'classictoons.png' )
def i11i1ii1I ( url ) :
 OOOOO0oo0O0O0 = oOoO0O0o0Oooo ( url )
 i1iIi = re . compile ( '<a href="(.+?)"><img src="(.+?)"' ) . findall ( OOOOO0oo0O0O0 )
 o0OO0o0o00o = re . compile ( '<a href="(.+?)">.+?</a></td></tr></table>' ) . findall ( OOOOO0oo0O0O0 )
 for url , oOo0 in i1iIi :
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
 i1iIi = re . compile ( '<iframe width="640" height="480" src="(.+?)" frameborder="0" allowfullscreen></iframe>' ) . findall ( OOOOO0oo0O0O0 )
 for url in i1iIi :
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
 i1iIi = re . compile ( 'href="(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( iiI )
 for url , ooOOoooooo in i1iIi :
  if '?c=' in url :
   O0OO0O ( '[COLORgreen]' + ooOOoooooo + '[/COLOR]' , 'http://kisscartoon.me' + url , 20004 , oOOoO0 + 'ORIGINCARTOON.png' )
   if 82 - 82: Oo + Ooo00oOo00o
def O00O ( url ) :
 iiI = cloudflare . source ( url )
 i1iIi = re . compile ( 'href="(.+?)" title="(.+?)">/n(.+?)</a><br/>' , re . DOTALL ) . findall ( iiI )
 for url , OOO , ooOOoooooo in i1iIi :
  if 'Genre' in url :
   O0OO0O ( '[COLORgreen]' + ooOOoooooo + '[/COLOR]' , 'http://kisscartoon.me' + url , 20004 , oOOoO0 + 'ORIGINCARTOON.png' )
   if 6 - 6: OoooooooOO
def iI1iIii11Ii ( url ) :
 iiI = cloudflare . source ( url )
 i1iIi = re . compile ( 'src="(.+?)" style=.+?<a class="bigChar" href="(.+?)">(.+?)</a>.+?<p>(.+?)</p>' , re . DOTALL ) . findall ( iiI )
 for url , OOO , ooOOoooooo in i1iIi :
  ooooooO0oo ( '[COLORgreen]' + ooOOoooooo + '[/COLOR]' , 'http://kisscartoon.me' + url , 20005 , img , '' , OOO )
  if 8 - 8: ii11ii1ii * O0oO . o0oO0 / o00O0oo - Oo % O0
def iI1i1i11I1iI ( url ) :
 iiI = cloudflare . source ( url )
 i1iIi = re . compile ( '<img width="120" height="165" src="(.+?)" style=.+?<a class="bigChar" href="(.+?)">(.+?)</a>.+?<p>(.+?)</p>' , re . DOTALL ) . findall ( iiI )
 for url , OOO , ooOOoooooo in i1iIi :
  ooooooO0oo ( '[COLORgreen]' + ooOOoooooo + '[/COLOR]' , 'http://kisscartoon.me' + url , 20005 , img , '' , OOO )
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
 iiI = IIiIi1iI ( oOo0oooo00o ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2NhcnRvb24=' ) )
 i1iIi = re . compile ( '<td><a href="(.+?)">(.+)</a></td>' ) . findall ( iiI )
 for I1Ii1iI1 , ooOOoooooo in i1iIi :
  if o00o0 in ooOOoooooo . lower ( ) :
   if 'Dad!' in ooOOoooooo :
    pass
   elif 'Family Guy' in ooOOoooooo :
    pass
   elif '2 Stupid' in ooOOoooooo :
    pass
   elif 'The Zelfs' in ooOOoooooo :
    pass
   elif 'A Clone' in ooOOoooooo :
    pass
   elif 'A.T.O.M' in ooOOoooooo :
    pass
   elif 'Almost Naked' in ooOOoooooo :
    pass
   elif 'Angry Kid' in ooOOoooooo :
    pass
   elif 'Annoying Orange' in ooOOoooooo :
    pass
   elif 'Aqua Teen' in ooOOoooooo :
    pass
   elif 'Assy Mcgee' in ooOOoooooo :
    pass
   elif 'Astroblast' in ooOOoooooo :
    pass
   elif 'Atomic Betty' in ooOOoooooo :
    pass
   elif 'Axe Cop' in ooOOoooooo :
    pass
   elif 'Baby Playpen' in ooOOoooooo :
    pass
   elif 'Beavis and Butt' in ooOOoooooo :
    pass
   elif 'Celebrity Deathmatch' in ooOOoooooo :
    pass
   elif 'Clerks The' in ooOOoooooo :
    pass
   elif 'Crapston Villas' in ooOOoooooo :
    pass
   elif 'Duckman:' in ooOOoooooo :
    pass
   elif 'Stripperella' in ooOOoooooo :
    pass
   elif 'Vixen' in ooOOoooooo :
    pass
   else :
    ooooooO0oo ( '[COLORgreen]' + ooOOoooooo + '[/COLOR]' , I1Ii1iI1 , 10006 , oOOoO0 + 'ORIGINCARTOON.png' , OOooO0OOoo , '' )
  xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 70 - 70: Ooo00oOo00o % OoOO + OoOO0ooOOoo0O / o00O0oo % O0
def oO00O0 ( ) :
 OOOOO0oo0O0O0 = IIiIi1iI ( oOo0oooo00o ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2NhcnRvb24=' ) )
 i1iIi = re . compile ( '<td><a href="(.+?)">(.+)</a></td>' ) . findall ( OOOOO0oo0O0O0 )
 for I1Ii1iI1 , ooOOoooooo in i1iIi :
  if 'Dad!' in ooOOoooooo :
   pass
  elif 'Family Guy' in ooOOoooooo :
   pass
  elif '2 Stupid' in ooOOoooooo :
   pass
  elif 'The Zelfs' in ooOOoooooo :
   pass
  elif 'A Clone' in ooOOoooooo :
   pass
  elif 'A.T.O.M' in ooOOoooooo :
   pass
  elif 'Almost Naked' in ooOOoooooo :
   pass
  elif 'Angry Kid' in ooOOoooooo :
   pass
  elif 'Annoying Orange' in ooOOoooooo :
   pass
  elif 'Aqua Teen' in ooOOoooooo :
   pass
  elif 'Assy Mcgee' in ooOOoooooo :
   pass
  elif 'Astroblast' in ooOOoooooo :
   pass
  elif 'Atomic Betty' in ooOOoooooo :
   pass
  elif 'Axe Cop' in ooOOoooooo :
   pass
  elif 'Baby Playpen' in ooOOoooooo :
   pass
  elif 'Beavis and Butt' in ooOOoooooo :
   pass
  elif 'Celebrity Deathmatch' in ooOOoooooo :
   pass
  elif 'Clerks The' in ooOOoooooo :
   pass
  elif 'Crapston Villas' in ooOOoooooo :
   pass
  elif 'Duckman:' in ooOOoooooo :
   pass
  elif 'Stripperella' in ooOOoooooo :
   pass
  elif 'Vixen' in ooOOoooooo :
   pass
  else :
   ooooooO0oo ( '[COLORgreen]' + ooOOoooooo + '[/COLOR]' , I1Ii1iI1 , 10006 , oOOoO0 + 'ORIGINCARTOON.png' , OOooO0OOoo , '' )
 xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 36 - 36: OoOO - o00O0oo . Oo - i11iIiiIii - OoOO0ooOOoo0O * Oo
def OooOOOO ( url ) :
 OOOOO0oo0O0O0 = IIiIi1iI ( url )
 o0OO0o0o00o = re . compile ( '<img src="(.+?)" id="series_image" width="250" height="370" alt=".+?" />' ) . findall ( OOOOO0oo0O0O0 )
 for oOo0 in o0OO0o0o00o :
  iIIIiiI1i1i = oOo0
 iIII = re . compile ( '<li><a href="(.+?)">Next</a></li>' ) . findall ( OOOOO0oo0O0O0 )
 for url in iIII :
  ooooooO0oo ( '[COLORgreen]NEXT PAGE[/COLOR]' , url , 10006 , iIIIiiI1i1i , OOooO0OOoo , '' )
 i1iIi = re . compile ( '&nbsp;<a href="(.+?)">(.+?)</a>' ) . findall ( OOOOO0oo0O0O0 )
 for url , ooOOoooooo in i1iIi :
  IiI1iiiIii ( '[COLORgreen]' + ooOOoooooo + '[/COLOR]' , url , 10007 , iIIIiiI1i1i )
  if 70 - 70: oO0o0ooO0 / iIii1I11I1II1
  if 85 - 85: OoooooooOO % i1IIi * OoooooooOO / ii11ii1ii
 xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 96 - 96: OoooooooOO + OoOO
def iiII1i11i ( url , IMAGE ) :
 OOOOO0oo0O0O0 = IIiIi1iI ( url )
 i1iIi = re . compile ( '"playlist">(.+?)</span></div><div><iframe src="(.+?)"' ) . findall ( OOOOO0oo0O0O0 )
 for ooOOoooooo , url in i1iIi :
  print ooOOoooooo + '     ' + url
  if 'easy' in url :
   IiIi ( url )
   if 87 - 87: ii11ii1ii - ii11ii1ii - oO0o0ooO0 + OoOO
   if 82 - 82: OoOO / iIii1I11I1II1 . OOOo0 . OoOO0ooOOoo0O / OOooOOo
  xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 42 - 42: Oo
def IiIi ( url ) :
 OOOOO0oo0O0O0 = IIiIi1iI ( url )
 i1iIi = re . compile ( "url: '(.+?)'," ) . findall ( OOOOO0oo0O0O0 )
 for url in i1iIi :
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
 i1iIi = re . compile ( '<li>.+?<a href="(.+?)">.+?<img src="(.+?)" alt=""/>.+?<span class="year">\n(.+?)</span>.+?<span class="video-title">\n(.+?)</span>.+?</li>' , re . DOTALL ) . findall ( iiI )
 for url , oOo0 , II1iiiiII , ooOOoooooo in i1iIi :
  ooOOoooooo = ( ooOOoooooo ) . replace ( '  ' , '' ) + ' ' + ( II1iiiiII ) . replace ( '  ' , '' )
  II1I = oOo0
  url = url
  O0OoOO0oo0 ( ooOOoooooo , II1I , url )
 oOO = re . compile ( '<a href="http://www.izlemeyedeger.com/tur/(.+?)?s=(.+?)&sort=&orderby=">(.+?)</a>' ) . findall ( iiI )
 for url , O0o0OO0000ooo , ooOOoooooo in oOO :
  ooooooO0oo ( '[COLORgold] Page ' + ooOOoooooo + '[/COLOR]' , 'http://www.izlemeyedeger.com/tur/' + url + '?s=' + O0o0OO0000ooo + '&sort=&orderby=' , 10036 , '' , OOooO0OOoo , '' )
  if 4 - 4: o00O0oo
  if 51 - 51: Ooo00oOo00o - O0 % OoOO - OoOoOO00
def I1II ( ) :
 if 64 - 64: O0 % o0000oOoOoO0o % O0 * Ooo00oOo00o . OoOO + OOOo0
 iiI = cloudflare . source ( oOo0oooo00o ( 'aHR0cDovL3d3dy5pemxlbWV5ZWRlZ2VyLmNvbQ==' ) )
 O00 = re . compile ( '<!-- popüler filmler -->(.+?)<!-- content -->' , re . DOTALL ) . findall ( iiI )
 for I11ii1i1 in O00 :
  i1iIi = re . compile ( '<li>.+?<a href="(.+?)">.+?<img width=".+?" height=".+?" src="(.+?)" alt=""/>.+?<span class="year">(.+?)</span>.+?<span class=".+?">(.+?)</span>.+?</li>' , re . DOTALL ) . findall ( str ( O00 ) )
  for I1Ii1iI1 , oOo0 , II1iiiiII , ooOOoooooo in i1iIi :
   ooOOoooooo = ( ooOOoooooo ) . replace ( '  ' , '' ) . replace ( '\\t' , '' ) . replace ( '\\r' , '' ) . replace ( '\\n' , '' ) . replace ( '\\xc3\\x87' , '' ) + ' ' + ( II1iiiiII ) . replace ( '  ' , '' ) . replace ( '\\t' , '' ) . replace ( '\\r' , '' ) . replace ( '\\n' , '' )
   II1I = oOo0
   I1Ii1iI1 = I1Ii1iI1
   O0OoOO0oo0 ( ooOOoooooo , II1I , I1Ii1iI1 )
   if 78 - 78: oO0o0ooO0
   if 28 - 28: o0000oOoOoO0o
def oOOOOoo ( ) :
 iiI = cloudflare . source ( oOo0oooo00o ( 'aHR0cDovL3d3dy5pemxlbWV5ZWRlZ2VyLmNvbS9zZXJpLWZpbG1sZXI=' ) )
 i1iIi = re . compile ( ' <div class="title">.+?</span>\n(.+?)<span style=".+?<img src="(.+?)" alt="" title=".+?<a class="more" href="(.+?)">' , re . DOTALL ) . findall ( iiI )
 for ooOOoooooo , oOo0 , I1Ii1iI1 in i1iIi :
  if 'IMDB' in ooOOoooooo :
   pass
  else :
   ooooooO0oo ( '[COLORgreen]' + ( ooOOoooooo ) . replace ( '  ' , '' ) + '[/COLOR]' , I1Ii1iI1 , 10037 , oOo0 , OOooO0OOoo , '' )
 oOO = re . compile ( '<a href="http://www.izlemeyedeger.com/seri-filmler(.+?)">(.+?)</a>' ) . findall ( iiI )
 for I1Ii1iI1 , ooOOoooooo in oOO :
  ooooooO0oo ( '[COLORgold] Page ' + ooOOoooooo + '[/COLOR]' , 'http://www.izlemeyedeger.com/seri-filmler' + I1Ii1iI1 , 10039 , '' , OOooO0OOoo , '' )
  if 58 - 58: OOooOOo / IIII . I1IiI / OoooooooOO + O0oO
def O0OoO0ooOO0o ( url ) :
 iiI = cloudflare . source ( url )
 i1iIi = re . compile ( ' <div class="title">.+?</span>\n(.+?)<span style=".+?<img src="(.+?)" alt="" title=".+?<a class="more" href="(.+?)">' , re . DOTALL ) . findall ( iiI )
 for ooOOoooooo , oOo0 , url in i1iIi :
  if 'IMDB' in ooOOoooooo :
   pass
  else :
   ooooooO0oo ( '[COLORgreen]' + ( ooOOoooooo ) . replace ( '  ' , '' ) + '[/COLOR]' , url , 10037 , oOo0 , OOooO0OOoo , '' )
 oOO = re . compile ( '<a href="http://www.izlemeyedeger.com/seri-filmler(.+?)">(.+?)</a>' ) . findall ( iiI )
 for url , ooOOoooooo in oOO :
  ooooooO0oo ( '[COLORgold] Page ' + ooOOoooooo + '[/COLOR]' , 'http://www.izlemeyedeger.com/seri-filmler' + url , 10034 , '' , OOooO0OOoo , '' )
  if 81 - 81: O0 * OoOoOO00 + OOOo0 * i11iIiiIii - ii11ii1ii / OOOo0
  if 63 - 63: I1IiI - OoooooooOO % O0oO
def oOi11iI11iIiIi ( url ) :
 iiI = cloudflare . source ( url )
 i1iIi = re . compile ( '<li>.+?<a href="(.+?)">.+?<img src="(.+?)" alt=""/>.+?<span class="year">\n(.+?)</span>.+?<span class="video-title">\n(.+?)</span>.+?</li>' , re . DOTALL ) . findall ( iiI )
 for url , oOo0 , II1iiiiII , ooOOoooooo in i1iIi :
  ooOOoooooo = ( ooOOoooooo ) . replace ( '  ' , '' ) . replace ( '&amp;' , '&' ) . replace ( '\\t' , '' ) . replace ( '\\r' , '' ) . replace ( '\\n' , '' ) . replace ( '\\xc3\\x87' , '' ) + ' ' + ( II1iiiiII ) . replace ( '  ' , '' ) . replace ( '\\t' , '' ) . replace ( '\\r' , '' ) . replace ( '\\n' , '' )
  II1I = oOo0
  url = url
  O0OoOO0oo0 ( ooOOoooooo , II1I , url )
  if 100 - 100: O0oO . OOooOOo * Oo % O0 * O0
def O0OoOO0oo0 ( name , iconimage , url ) :
 iiI = cloudflare . source ( url )
 i1iIi = re . compile ( '<meta itemprop="embedURL" content="(.+?)" />' ) . findall ( iiI )
 for url in i1iIi :
  IIIii1 ( name , iconimage , url )
  if 71 - 71: OoOoOO00 / i1IIi . ii11ii1ii % OoooooooOO . I1IiI
def IIIii1 ( name , iconimage , url ) :
 name = name
 oOo0 = iconimage
 iiI = cloudflare . source ( url )
 i1iIi = re . compile ( 'file: "(.+?)",.+?label: "(.+?)"' , re . DOTALL ) . findall ( iiI )
 for O0o0OO0000ooo , Iiiiii111i1ii in i1iIi :
  IiI1iiiIii ( '[COLORgreen]' + name + ' - ' + Iiiiii111i1ii + '[/COLOR]' , O0o0OO0000ooo , 10012 , oOo0 )
  if 25 - 25: OoOO0ooOOoo0O - o0oO0 / i11iIiiIii
def iiI1ii11i1 ( ) :
 o00o0 = Oo0o0000o0o0 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 II1III1I1I1Ii = o00o0 . lower ( )
 I1Ii1iI1 = 'http://www.izlemeyedeger.com/arama?q=' + o00o0
 iiI = cloudflare . source ( I1Ii1iI1 )
 i1iIi = re . compile ( '<div class="inner">.+?<li>.+?<a href="(.+?)">.+?<img src="(.+?)" alt.+?<span class="year">(.+?)</span>.+?<span class="video-title">(.+?)</span>.+?</li>.+?</div>' , re . DOTALL ) . findall ( iiI )
 for I1Ii1iI1 , oOo0 , II1iiiiII , ooOOoooooo in i1iIi :
  ooOOoooooo = ( ooOOoooooo ) . replace ( '  ' , '' ) . replace ( '\\t' , '' ) . replace ( '\\r' , '' ) . replace ( '\\n' , '' ) . replace ( '\\xc3\\x87' , '' ) + ' ' + ( II1iiiiII ) . replace ( '  ' , '' ) . replace ( '\\t' , '' ) . replace ( '\\r' , '' ) . replace ( '\\n' , '' )
  II1I = oOo0
  I1Ii1iI1 = I1Ii1iI1
  O0OoOO0oo0 ( ooOOoooooo , II1I , I1Ii1iI1 )
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
 iiI = IIiIi1iI ( ( oOo0oooo00o ( 'aHR0cDovL2JhY2syYmFzaWNzYnVpbGQuY28udWsvdGVzdC9zdGFuZHVwbGlzdC5waHA=' ) ) )
 i1iIi = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( iiI )
 for I1Ii1iI1 , oOo0 , ooOOoooooo in i1iIi :
  IiI1iiiIii ( '[COLORgreen]' + ooOOoooooo + '[/COLOR]' , I1Ii1iI1 , 222 , oOo0 )
  if 6 - 6: o00O0oo - o0oO0 * OoOO0ooOOoo0O . oO0o0ooO0 / O0 * o0oO0
def II11iI111i1 ( ) :
 o00o0 = Oo0o0000o0o0 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 II1III1I1I1Ii = o00o0 . lower ( )
 iiI = IIiIi1iI ( ( oOo0oooo00o ( 'aHR0cDovL3d3dy5jb3VjaHRyaXBwZXIuY29tL2ZvcnVtMi9wYWdlLnBocD9wYWdlPTM=' ) ) )
 O00 = re . compile ( '<tr>.+?<td width=".+?" align=".+?">.+?<img border=".+?" src="..(.+?)" width=".+?" height=".+?"></td>.+?<td width=".+?" valign=".+?" align=".+?"><font size=".+?">(.+?)</font></td>.+?<td width=".+?">(.+?)</td>' , re . DOTALL ) . findall ( iiI )
 for oOo0 , Oo00OoOo , iIiiiI1IiI1I1 in O00 :
  for o00o0 in Oo00OoOo :
   print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< img >>>>>>>>>>>>>>>>>>>>>>>>>>'
   ii1ii111 = re . compile ( '<a href="(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( iIiiiI1IiI1I1 )
   for I1Ii1iI1 , ooOOoooooo in ii1ii111 :
    if 'tube' in I1Ii1iI1 :
     pass
    elif 'stage' in I1Ii1iI1 :
     IiI1iiiIii ( '[COLORgreen]' + Oo00OoOo + '   -   ' + ooOOoooooo + '[/COLOR]' , ( I1Ii1iI1 ) . replace ( '" target="_blank' , '' ) , 10016 , 'http://couchtripper.com/' + oOo0 , )
    elif 'vee' in I1Ii1iI1 :
     pass
     if 33 - 33: ii11ii1ii
def O00O0Ooooo00 ( ) :
 iiI = IIiIi1iI ( ( oOo0oooo00o ( 'aHR0cDovL3d3dy5jb3VjaHRyaXBwZXIuY29tL2ZvcnVtMi9wYWdlLnBocD9wYWdlPTM=' ) ) )
 O00 = re . compile ( '<tr>.+?<td width=".+?" align=".+?">.+?<img border=".+?" src="..(.+?)" width=".+?" height=".+?"></td>.+?<td width=".+?" valign=".+?" align=".+?"><font size=".+?">(.+?)</font></td>.+?<td width=".+?">(.+?)</td>' , re . DOTALL ) . findall ( iiI )
 for oOo0 , Oo00OoOo , iIiiiI1IiI1I1 in O00 :
  ii1ii111 = re . compile ( '<a href="(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( iIiiiI1IiI1I1 )
  for I1Ii1iI1 , ooOOoooooo in ii1ii111 :
   if 'tube' in I1Ii1iI1 :
    pass
   elif 'stage' in I1Ii1iI1 :
    IiI1iiiIii ( '[COLORgreen]' + Oo00OoOo + '   -   ' + ooOOoooooo + '[/COLOR]' , ( I1Ii1iI1 ) . replace ( '" target="_blank' , '' ) , 10016 , 'http://couchtripper.com/' + oOo0 )
   elif 'vee' in I1Ii1iI1 :
    pass
    if 97 - 97: o0oO0 / O0oO % i1IIi % ii11ii1ii
    if 18 - 18: iIii1I11I1II1 % o0000oOoOoO0o
 xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 95 - 95: o0oO0 + i11iIiiIii * O0oO - i1IIi * O0oO - iIii1I11I1II1
def oo0o0O0Oooooo ( url ) :
 iiI = IIiIi1iI ( url )
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
  iiI = IIiIi1iI ( iii11111I )
  i1iIi = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( iiI )
  for I1Ii1iI1 , II1I , ii11ii11 , O0i1II1Iiii1I11 , ooOOoooooo in i1iIi :
   if o00o0 in ooOOoooooo . lower ( ) :
    i1i1IIiiIIi1I ( ooOOoooooo , I1Ii1iI1 , 222 , II1I , O0i1II1Iiii1I11 , ii11ii11 )
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
  iiI = IIiIi1iI ( o00OO00O0oOO )
  i1iIi = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( iiI )
  for ooOOoooooo , ii11ii11 , I1Ii1iI1 , oOo0 , O0i1II1Iiii1I11 , Ii1iI111 in i1iIi :
   if o00o0 in ooOOoooooo . lower ( ) :
    IiII1II11I ( ooOOoooooo , I1Ii1iI1 , Ii1iI111 , oOo0 , O0i1II1Iiii1I11 , ii11ii11 )
    if 51 - 51: IIII * O0 / OoOoOO00 . o00O0oo % OoOO0ooOOoo0O / OOOo0
    I1i1I1II ( 'movies' , 'MAIN' )
    xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
    if 9 - 9: OOOo0 % OOOo0 % OoOoOO00
    if 30 - 30: IIII + O0oO - IIII . IIII - OoOoOO00 + O0
def oOO0 ( ) :
 if 46 - 46: o00O0oo % I1IiI
 OOOOO0oo0O0O0 = IIiIi1iI ( oOo0oooo00o ( 'aHR0cDovL3NlZWR1cmdyZWVkLngxMGhvc3QuY29tL29yaWdpbi9zcG9uZ2VtYWluLnBocA==' ) )
 i1iIi = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( OOOOO0oo0O0O0 )
 for ooOOoooooo , ii11ii11 , I1Ii1iI1 , oOo0 , O0i1II1Iiii1I11 , Ii1iI111 in i1iIi :
  IiII1II11I ( ooOOoooooo , I1Ii1iI1 , Ii1iI111 , oOo0 , O0i1II1Iiii1I11 , ii11ii11 )
  I1i1I1II ( 'movies' , 'MAIN' )
def ooo0o0O0o ( url ) :
 if 62 - 62: o0oO0 + i11iIiiIii + Oo / i11iIiiIii
 xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
 I1Ii = ( '%s%s' % ( oOOIi1II , url ) )
 OOOo00oo0oO = IIiIi1iI ( url )
 i1iIi = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( OOOo00oo0oO )
 for url , II1I , ii11ii11 , O0Oo00 , ooOOoooooo in i1iIi :
  i1i1IIiiIIi1I ( ooOOoooooo , url , 222 , II1I , O0Oo00 , ii11ii11 )
  if 41 - 41: iIii1I11I1II1 % o0000oOoOoO0o
  I1i1I1II ( 'movies' , 'MAIN' )
  if 59 - 59: OoOO0ooOOoo0O + i11iIiiIii
  xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 88 - 88: i11iIiiIii - o0oO0
  if 67 - 67: OoOO0ooOOoo0O . Oo + I1IiI - OoooooooOO
def OOOoO ( url ) :
 if 14 - 14: o0000oOoOoO0o . iIii1I11I1II1 . OoooooooOO . OoOoOO00 / OOooOOo
 OOOOO0oo0O0O0 = IIiIi1iI ( url )
 i1iIi = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( OOOOO0oo0O0O0 )
 for ooOOoooooo , ii11ii11 , url , oOo0 , O0i1II1Iiii1I11 , Ii1iI111 in i1iIi :
  IiII1II11I ( ooOOoooooo , url , Ii1iI111 , oOo0 , O0i1II1Iiii1I11 , ii11ii11 )
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
  ooOOoooooo = O0o00OOo00O0O [ 0 ]
  I1Ii1iI1 = O0o00OOo00O0O [ 1 ]
  II1I = O0o00OOo00O0O [ 2 ]
  try :
   II1i = O0o00OOo00O0O [ 3 ]
   if II1i == None :
    raise
  except :
   if o0oOoO00o . getSetting ( 'use_thumb' ) == "true" :
    II1i = II1I
   else :
    II1i = O0i1II1Iiii1I11
  try : OoOOoO000O00oO = O0o00OOo00O0O [ 5 ]
  except : OoOOoO000O00oO = None
  try : i1OoOO = O0o00OOo00O0O [ 6 ]
  except : i1OoOO = None
  if 44 - 44: OoOO0ooOOoo0O
  if O0o00OOo00O0O [ 4 ] == 0 :
   ooooooO0oo ( ooOOoooooo , I1Ii1iI1 , '' , II1I , O0i1II1Iiii1I11 , '' , 'fav' )
  else :
   ooooooO0oo ( ooOOoooooo , I1Ii1iI1 , O0o00OOo00O0O [ 4 ] , II1I , O0i1II1Iiii1I11 , '' , 'fav' )
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
 i1iIi = re . compile ( '<li id=".+?">.+?<a href="(.+?)">.+?<img width="40" height="40" src="(.+?)" alt=""/>.+?<span class="title">\n(.+?)</span>.+?<span class="alt-title">\n(.+?)</span>.+?</a>.+?</li>' , re . DOTALL ) . findall ( OOOOO0oo0O0O0 )
 for I1Ii1iI1 , oOo0 , ooOOoooooo , oooOO0OO0O in i1iIi :
  ooooooO0oo ( ooOOoooooo + '  -  ' + ( oooOO0OO0O ) . replace ( 'sezon' , 'Season' ) . replace ( 'bölüm' , 'Episode' ) , I1Ii1iI1 , 10023 , oOOoO0 + 'dtv.png' , OOooO0OOoo , '' )
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
 i1iIi = re . compile ( '<div class="tv-series-single">.+?<a href="(.+?)" class="film-image">.+?<img src="(.+?)" alt=""/>.+?<span class="position">.+?</span>\n(.+?)</a>' , re . DOTALL ) . findall ( iiI )
 for url , oOo0 , ooOOoooooo in i1iIi :
  ooooooO0oo ( '[COLORgreen]' + ooOOoooooo + '[/COLOR]' , url , 10022 , oOOoO0 + 'dtv.png' , OOooO0OOoo , '' )
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
 i1iIi = re . compile ( '<a href="(.+?)" class="film-image">\n<img src="(.+?)" alt=""/>\n</a>\n<div class="tss-detail">\n<a class="title" style="" href=".+?">\n<span class="position">.+?</span>\n(.+?)</a>' ) . findall ( iiI )
 for I1Ii1iI1 , oOo0 , ooOOoooooo in i1iIi :
  if o00o0 in ooOOoooooo . lower ( ) :
   ooooooO0oo ( '[COLORgreen]' + ooOOoooooo + '[/COLOR]' , I1Ii1iI1 , 10022 , oOOoO0 + 'dtv.png' )
   if 15 - 15: I1IiI
   if 62 - 62: o00O0oo
   if 51 - 51: I1IiI
def I11IIIiIi11 ( url ) :
 iiI = cloudflare . source ( url )
 i1iIi = re . compile ( '<a class="season" href="(.+?)">\n(.+?)\n</a>.+?<a class="episode" href=".+?">\n(.+?)\n</a>.+?<a class="episode-name" href=".+?">\n(.+?)</a>' , re . DOTALL ) . findall ( iiI )
 for O0o0OO0000ooo , I11iiIi1i1 , i1IiiI1iIi , ooOOoooooo in i1iIi :
  oOOo00O0OOOo = ( i1IiiI1iIi ) . replace ( 'Sezon' , '' ) . replace ( 'bölüm' , '' ) . replace ( 'Bölüm' , '' ) . replace ( 'BÃ¶lÃ¼m' , '' ) . replace ( '.' , '' )
  i11I1I1iiI = ( I11iiIi1i1 ) . replace ( 'bölüm' , '' ) . replace ( 'Sezon' , '' ) . replace ( 'Bölüm' , '' ) . replace ( 'BÃ¶lÃ¼m' , '' ) . replace ( '.' , '' )
  I1i1iii1Ii = 'Season ' + i11I1I1iiI + 'Episode ' + oOOo00O0OOOo + ooOOoooooo
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
 iiI = IIiIi1iI ( url )
 I11ii1i1 = re . compile ( '<ul class="pagination" style="line-height: 3;">(.+?)</ul>' , re . DOTALL ) . findall ( iiI )
 i1iIi = re . compile ( '<li><a href="/letters/(.+?)">(.+?)</a></li>' ) . findall ( str ( I11ii1i1 ) )
 for url , ooOOoooooo in i1iIi :
  ooooooO0oo ( '[COLORgreen]' + ooOOoooooo + '[/COLOR]' , 'http://watchseries.li/letters/' + url , 10049 , oOOoO0 + 'WATCHSERIES.png' , '' , '' )
  if 9 - 9: OoOO0ooOOoo0O . IIII
def iIi1i ( url ) :
 iiI = IIiIi1iI ( url )
 i1iIi = re . compile ( '<a href="(.+?)" class="sr-header">(.+?)</a>' ) . findall ( iiI )
 for url , ooOOoooooo in i1iIi :
  ooooooO0oo ( '[COLORgreen]' + ooOOoooooo + '[/COLOR]' , 'http://watchseries.li/' + url , 10049 , oOOoO0 + 'WATCHSERIES.png' , '' , '' )
  if 67 - 67: I1IiI / OOooOOo * Ooo00oOo00o / OoOO0ooOOoo0O * ii11ii1ii / OoOO
def OOoOO0OO ( url ) :
 iiI = IIiIi1iI ( url )
 i1iIi = re . compile ( '<li class="col-md-6 col-xs-12 list-movies-li"><a href="(.+?)" title=".+?">(.+?)<span class="epnum">.+?</span></a></li>' , re . DOTALL ) . findall ( iiI )
 o0OO0o0o00o = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="(.+?)">Next</a></li></ul>' , re . DOTALL ) . findall ( iiI )
 for url , ooOOoooooo in i1iIi :
  ooooooO0oo ( '[COLORgreen]' + ( ooOOoooooo ) . replace ( '&nbsp;' , ' ' ) . replace ( '&amp;' , '&' ) . replace ( '&#039;' , '\'' ) + '[/COLOR]' , 'http://www.watchseries.li' + url , 10044 , oOOoO0 + 'WATCHSERIES.png' , '' , '' )
 for url in o0OO0o0o00o :
  ooooooO0oo ( '[COLORgreen]' + 'NEXT' + '[/COLOR]' , 'http://www.watchseries.li' + url , 10049 , '' , '' , '' )
  if 26 - 26: oO0o0ooO0 . oO0o0ooO0
  if 35 - 35: O0oO . I1IiI * i11iIiiIii
def iiII ( ) :
 o00o0 = Oo0o0000o0o0 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 o0Oii1111i = 'http://www.watchseries.li/search/' + o00o0 . replace ( ' ' , '%20' )
 iiI = IIiIi1iI ( o0Oii1111i )
 i1iIi = re . compile ( '<img src="(.+?)".+?<a href="(.+?)" title=".+?"><b>(.+?)</b>' , re . DOTALL ) . findall ( iiI )
 for oOo0 , I1Ii1iI1 , ooOOoooooo in i1iIi :
  if 'watch online' in ooOOoooooo :
   pass
  else :
   print I1Ii1iI1
   ooooooO0oo ( '[COLORgreen]' + ooOOoooooo + '[/COLOR]' , 'http://www.watchseries.li' + I1Ii1iI1 , 10044 , oOo0 , '' , '' )
   if 75 - 75: IIII + OoOoOO00 / OoOO - OoOO / OoooooooOO
   xbmcplugin . setContent ( O00o0OO , 'movies' )
   if 2 - 2: OOooOOo
def i11ii ( url ) :
 iiI = IIiIi1iI ( url )
 i1iIi = re . compile ( '<img src="(.+?)".+?<div class="block-left-home-inside-text">.+?<a href="(.+?)" title=".+?"><b>(.+?)</b> <br>.+?<span class=".+?">(.+?)</span></a><br>(.+?)<br>' , re . DOTALL ) . findall ( iiI )
 for oOo0 , url , ooOOoooooo , i1IiiI1iIi , ii11ii11 in i1iIi :
  i11I1 = ( ooOOoooooo ) . replace ( '&nbsp;' , ' ' ) . replace ( '&amp;' , '&' ) . replace ( '&#039;' , '\'' ) + ' - ' + ( i1IiiI1iIi ) . replace ( '&amp;' , '&' ) . replace ( '&#039;' , '\'' )
  ooooooO0oo ( '[COLORgreen]' + i11I1 + '[/COLOR]' , 'http://www.watchseries.li' + url , 10045 , oOo0 , '' , ii11ii11 )
  if 34 - 34: O0 * O0 % OoooooooOO + oO0o0ooO0 * iIii1I11I1II1 % o00O0oo
def I1iI1I1 ( url ) :
 iiI = IIiIi1iI ( url )
 i1iIi = re . compile ( '<li class="col-md-6 col-xs-12 list-movies-li"><a href="(.+?)" title=".+?">(.+?)<span class="epnum">.+?</span></a></li>' , re . DOTALL ) . findall ( iiI )
 o0OO0o0o00o = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="(.+?)">Next</a></li></ul>' , re . DOTALL ) . findall ( iiI )
 for url , ooOOoooooo in i1iIi :
  i11I1 = ( ooOOoooooo ) . replace ( '&nbsp;' , ' ' ) . replace ( '&amp;' , '&' ) . replace ( '&#039;' , '\'' )
  ooooooO0oo ( '[COLORgreen]' + i11I1 + '[/COLOR]' , 'http://www.watchseries.li' + url , 10045 , oOOoO0 + 'WATCHSERIES.png' , '' , '' )
 for url in o0OO0o0o00o :
  ooooooO0oo ( '[COLORgreen]' + 'NEXT' + '[/COLOR]' , 'http://www.watchseries.li' + url , 10046 , '' , '' , '' )
  if 48 - 48: OOOo0 / i11iIiiIii - OOooOOo * OoOO / OoooooooOO
def OoOo ( url ) :
 iiI = IIiIi1iI ( url )
 i1iIi = re . compile ( '<div class="mask">.+?<a href="(.+?)" title="(.+?)">.+?<img src="(.+?)"' , re . DOTALL ) . findall ( iiI )
 o0OO0o0o00o = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="(.+?)">Next</a></li></ul>' , re . DOTALL ) . findall ( iiI )
 for url , ooOOoooooo , oOo0 in i1iIi :
  ooooooO0oo ( '[COLORgreen]' + ( ooOOoooooo ) . replace ( '&nbsp;' , ' ' ) . replace ( '&amp;' , '&' ) . replace ( '&#039;' , '\'' ) + '[/COLOR]' , 'http://www.watchseries.li' + url , 10044 , oOo0 , '' , '' )
 for url in o0OO0o0o00o :
  ooooooO0oo ( '[COLORgreen]' + 'NEXT' + '[/COLOR]' , 'http://www.watchseries.li' + url , 10041 , '' , '' , '' )
  if 17 - 17: o00O0oo . i11iIiiIii
def IIIiiiI ( url ) :
 iiI = IIiIi1iI ( url )
 I11ii1i1 = re . compile ( '<div class="col-md-6 col-xs-12".+?<a href=".+?" itemprop="url"><span itemprop="name">(.+?)</span>(.+?)</ul>' , re . DOTALL ) . findall ( iiI )
 for I11iiIi1i1 , O00 in I11ii1i1 :
  i1iIi = re . compile ( '<li itemprop="episode".+?<meta itemprop="url" content="(.+?)">.+?<span class="" itemprop="name">\n(.+?)\n' , re . DOTALL ) . findall ( str ( O00 ) )
  for url , ooOOoooooo in i1iIi :
   i11I1 = ( I11iiIi1i1 ) . replace ( '  ' , '' ) + ' ' + ( ooOOoooooo ) . replace ( '&nbsp;' , ' ' ) . replace ( '&#039;' , '\'' ) . replace ( '  ' , '' )
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
  iiI = IIiIi1iI ( URL )
  i1iIi = re . compile ( '<td>.+?<a href="/link/(.+?)".+?height="16px">(.+?)\n' , re . DOTALL ) . findall ( iiI )
  for I1Ii1iI1 , ooOOoooooo in i1iIi :
   URL = 'http://www.watchseries.li/link/' + I1Ii1iI1
   self . Get_site_link ( URL , season_name )
   if 58 - 58: OOooOOo - OoOoOO00 % OoOO + O0oO . I1IiI / IIII
 def Get_site_link ( self , url , season_name ) :
  iiI = IIiIi1iI ( url )
  i1iIi = re . compile ( '<iframe style=.+?" src="(.+?)"' ) . findall ( iiI )
  o0OO0o0o00o = re . compile ( '<IFRAME SRC="(.+?)"' ) . findall ( iiI )
  iIII = re . compile ( '<IFRAME style=".+?" SRC="(.+?)"' ) . findall ( iiI )
  for url in i1iIi :
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
  iiI = IIiIi1iI ( url )
  i1iIi = re . compile ( '"file" : "(.+?)",\n.+?"default" : .+?,\n.+?"label" : "(.+?)"' , re . DOTALL ) . findall ( iiI )
  for o0O0OO , ooOOoooooo in i1iIi :
   self . Printer ( o0O0OO , season_name , source_name )
   if 22 - 22: OoOoOO00 * Ooo00oOo00o * o0000oOoOoO0o + ii11ii1ii * OOooOOo
 def vidspot ( self , url , season_name , source_name ) :
  iiI = IIiIi1iI ( url )
  i1iIi = re . compile ( '"file" : "(.+?)",\n.+?"default" : .+?,\n.+?"label" : "(.+?)"' ) . findall ( iiI )
  for o0O0OO , ooOOoooooo in i1iIi :
   self . Printer ( o0O0OO , season_name , source_name )
   if 100 - 100: i1IIi / IIII
 def thevideo ( self , url , season_name , source_name ) :
  iiI = IIiIi1iI ( url )
  i1iIi = re . compile ( "{ label: '.+?', file: '(.+?)' }" ) . findall ( iiI )
  for o0O0OO in i1iIi :
   self . Printer ( o0O0OO , season_name , source_name )
   if 3 - 3: OoOoOO00 % ii11ii1ii - OoooooooOO * Oo . iIii1I11I1II1
 def vodlocker ( self , url , season_name , source_name ) :
  iiI = IIiIi1iI ( url )
  i1iIi = re . compile ( 'file: "(.+?)",.+?skin' , re . DOTALL ) . findall ( iiI )
  for o0O0OO in i1iIi :
   self . Printer ( o0O0OO , season_name , source_name )
   if 37 - 37: oO0o0ooO0 / Oo . o0000oOoOoO0o * o0000oOoOoO0o
 def daclips ( self , url , season_name , source_name ) :
  iiI = IIiIi1iI ( url )
  i1iIi = re . compile ( '{ file: "(.+?)", type:"video" }' ) . findall ( iiI )
  for o0O0OO in i1iIi :
   self . Printer ( o0O0OO , season_name , source_name )
   if 80 - 80: OoOO0ooOOoo0O % ii11ii1ii
 def filehoot ( self , url , season_name , source_name ) :
  iiI = IIiIi1iI ( url )
  i1iIi = re . compile ( 'file: "(.+?)",.+?skin' , re . DOTALL ) . findall ( iiI )
  for o0O0OO in i1iIi :
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
 OOOOO0oo0O0O0 = IIiIi1iI ( oOo0oooo00o ( 'aHR0cDovL2xpdmVvbnNhdC5jb20vcXVpY2tpbmRleC5odG1s' ) )
 i1iIi = re . compile ( '<a target="_self" href="(.+?)".+?src="(.+?)" alt="(.+?)"' , re . DOTALL ) . findall ( OOOOO0oo0O0O0 )
 for I1Ii1iI1 , oOo0 , ooOOoooooo in i1iIi :
  ooooooO0oo ( '[COLORgreen]' + ( ooOOoooooo ) . replace ( 'amp;' , '' ) + '[/COLOR]' , oOo0oooo00o ( 'aHR0cDovL2xpdmVvbnNhdC5jb20v' ) + I1Ii1iI1 , 10010 , oOo0oooo00o ( 'aHR0cDovL2xpdmVvbnNhdC5jb20v' ) + oOo0 , OOooO0OOoo , '' )
  if 29 - 29: O0 . O0oO
def OO0o0oO0O000o ( url ) :
 iiI = IIiIi1iI ( url )
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
 iiI = IIiIi1iI ( url )
 i1iIi = re . compile ( 'itemprop="image" class="entry-thumb" src="(.+?)".+?<h3 itemprop="name" class="entry-title td-module-title"><a itemprop="url" href="(.+?)" rel="bookmark" title=".+?">(.+?)</a></h3>' , re . DOTALL ) . findall ( iiI )
 for oOo0 , url , ooOOoooooo in i1iIi :
  I1i1iii = ooOOoooooo . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' )
  IiI1iiiIii ( '[COLORgreen]' + I1i1iii + '[/COLOR]' , url , 10013 , oOo0 )
  if 31 - 31: OoooooooOO + oO0o0ooO0 - I1IiI . i1IIi % oO0o0ooO0
def I1i1Ii111IIii ( url ) :
 iiI = IIiIi1iI ( url )
 i1iIi = re . compile ( '<script data-config="(.+?)" data-height' ) . findall ( iiI )
 for i11IIIiI1I in i1iIi :
  II1ii1I1 = ( i11IIIiI1I ) . replace ( '/v2' , '' ) . replace ( 'zeus.json' , 'video-sd.mp4?hosting_id=21772' ) . replace ( 'config.playwire.com' , 'cdn.video.playwire.com' )
  II1IIiiIiI ( 'http:' + II1ii1I1 )
  if 2 - 2: OoooooooOO . OoOO0ooOOoo0O . IIII
  if 42 - 42: OoOO0ooOOoo0O % OoOO / Ooo00oOo00o - OoOO * i11iIiiIii
def iI1IiiiIiI1Ii ( url ) :
 OOOOO0oo0O0O0 = oOoO0O0o0Oooo ( url )
 i1iIi = re . compile ( '<a href="([^"]*)" title="([^"]*)"><img itemprop="image" content="([^"]*)"' , re . DOTALL ) . findall ( OOOOO0oo0O0O0 )
 o0OO0o0o00o = re . compile ( "<a rel='next' href=([^=]*)=" , re . DOTALL ) . findall ( OOOOO0oo0O0O0 )
 for url , ooOOoooooo , oOo0 in i1iIi :
  IiI1iiiIii ( ooOOoooooo , url , 8046 , oOo0 )
 for url in o0OO0o0o00o :
  O0OO0O ( 'NEXT PAGE' , ( url ) . replace ( ' class' , '' ) , 8045 , oOOoO0 + 'geniekitchen.png' )
def Oo000 ( url ) :
 OOOOO0oo0O0O0 = oOoO0O0o0Oooo ( url )
 i1iIi = re . compile ( "__filename='([^']*)',.+?__fullimage='([^']*)',.+?__title='([^']*)'," , re . DOTALL ) . findall ( OOOOO0oo0O0O0 )
 for url , oOo0 , ooOOoooooo in i1iIi :
  II1IIiiIiI ( 'http://bitcast-b.bitgravity.com/ndtvod/23372/ndtv/' + url )
  if 48 - 48: i11iIiiIii % OoOO
def i11i11 ( url ) :
 OOOOO0oo0O0O0 = oOoO0O0o0Oooo ( url )
 i1iIi = re . compile ( "src='http://www.youtube.com/embed/(.+?)?version=3&#038;rel=1&#038;fs=1&#038;autohide=2&#038;showsearch=0&#038;showinfo=1&#038;iv_load_policy=1&#038;wmode=transparent' frameborder='0' allowfullscreen='true'></iframe>" ) . findall ( OOOOO0oo0O0O0 )
 for url in i1iIi :
  yt . PlayVideo ( url )
  if 18 - 18: iIii1I11I1II1 + o0000oOoOoO0o * OOOo0 - OoOO0ooOOoo0O / OOOo0
def o00iI1i1II ( ) :
 OOOOO0oo0O0O0 = oOoO0O0o0Oooo ( oOo0oooo00o ( 'aHR0cDovL3RvcGRvY3VtZW50YXJ5ZmlsbXMuY29tLw==' ) )
 i1iIi = re . compile ( '<a href="(.+?)" >(.+?)</a></li><li>' ) . findall ( OOOOO0oo0O0O0 )
 for I1Ii1iI1 , ooOOoooooo in i1iIi :
  O0OO0O ( ooOOoooooo , I1Ii1iI1 , 8041 , oOOoO0 + 'documentary.png' )
def I1ii1ii1I ( url ) :
 OOOOO0oo0O0O0 = oOoO0O0o0Oooo ( url )
 i1iIi = re . compile ( '<h2><a href="(.+?)" title="(.+?)">.+?</a></h2>.+?src="(.+?)"' , re . DOTALL ) . findall ( OOOOO0oo0O0O0 )
 o0OO0o0o00o = re . compile ( 'class="inactive">.+?</a><a href="(.+?)">Next</a></div>' , re . DOTALL ) . findall ( OOOOO0oo0O0O0 )
 for url , ooOOoooooo , oOo0 in i1iIi :
  O0OO0O ( ( ooOOoooooo ) . replace ( '&#039;s' , '' ) , url , 8042 , oOo0 )
 for url in o0OO0o0o00o :
  O0OO0O ( 'NEXT PAGE' , url , 8041 , oOOoO0 + 'documentary.png' )
  if 18 - 18: OoOO * OoOO % OoOO
  if 17 - 17: O0 * I1IiI * ii11ii1ii * OoOoOO00 * o0000oOoOoO0o % i1IIi
def IIiIi1iI1iII ( url ) :
 OOOOO0oo0O0O0 = oOoO0O0o0Oooo ( url )
 i1iIi = re . compile ( '<meta itemprop="name" content="(.+?)".+?<meta itemprop="thumbnailUrl" content="(.+?)".+?<meta itemprop="embedUrl" content="(.+?)".+?<meta itemprop="description" content="(.+?)" />' , re . DOTALL ) . findall ( OOOOO0oo0O0O0 )
 o0OO0o0o00o = re . compile ( '<div class="video new-video"><iframe width="766" height="431" src="(.+?)&amp;iv_load_policy=3&amp;showinfo=0&amp;autohide=1"' , re . DOTALL ) . findall ( OOOOO0oo0O0O0 )
 for ooOOoooooo , oOo0 , url , OOO in i1iIi :
  IiI1iiiIii ( ( ooOOoooooo ) . replace ( '&#039;s' , '' ) , url . replace ( 'https://www.youtube.com/embed/' , '' ) , 8043 , oOo0 )
 for url in o0OO0o0o00o :
  OoOo00o ( ( url ) . replace ( '//' , 'http://' ) )
  if 30 - 30: I1IiI . o0000oOoOoO0o / o0000oOoOoO0o * i11iIiiIii
def OoOo00o ( url ) :
 OOOOO0oo0O0O0 = oOoO0O0o0Oooo ( url )
 i1iIi = re . compile ( '<link rel="canonical" href="(.+?)">  <link rel="stylesheet"' ) . findall ( OOOOO0oo0O0O0 )
 for url in i1iIi :
  IiI1iiiIii ( 'PLAY' , ( url ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , oOOoO0 + 'documentary.png' )
  if 46 - 46: Ooo00oOo00o * Oo % OoOO + O0 * IIII
def ii1I11i ( ) :
 iiI = oOoO0O0o0Oooo ( 'http://www.stream2watch.co/live-tv' )
 i1iIi = re . compile ( '<a href="(.+?)">.+?<img src="(.+?)" alt=".+?"/>.+?<span class="country_name">(.+?)<br />(.+?)</span>' , re . DOTALL ) . findall ( iiI )
 for I1Ii1iI1 , oOo0 , ooOOoooooo , O0OOO in i1iIi :
  O0OO0O ( ( ooOOoooooo + '[COLORgreen]' + O0OOO + '[/COLOR]' ) , I1Ii1iI1 , 8086 , oOo0 )
  if 37 - 37: O0 - o0000oOoOoO0o
def IiI1 ( url ) :
 iiI = oOoO0O0o0Oooo ( url )
 i1iIi = re . compile ( '<a class="front_channel_href" href="(.+?)" title=".+?">.+?<img class="front_channel_thumb" src="(.+?)" alt=".+?"/>.+?<span class="front_channel_name">(.+?)</span>' , re . DOTALL ) . findall ( iiI )
 for url , oOo0 , ooOOoooooo in i1iIi :
  O0OO0O ( '[COLORgreen]' + ooOOoooooo + '[/COLOR]' , url , 8087 , oOo0 )
  if 59 - 59: o0000oOoOoO0o / Oo / OoOO0ooOOoo0O / O0 / I1IiI + OOooOOo
def IIiI1111i1 ( url ) :
 iiI = IIiIi1iI ( url )
 i1iIi = re . compile ( 'a id="code_.+?data-f-href="(.+?)" data-code-embed="">(.+?)</a>' , re . DOTALL ) . findall ( iiI )
 for url , ooOOoooooo in i1iIi :
  ii1ii1I1IIi1 ( url , ooOOoooooo )
  if 55 - 55: OOOo0
def ii1ii1I1IIi1 ( url , name ) :
 iiI = IIiIi1iI ( url )
 i1iIi = re . compile ( "playStream\('.+?', '(.+?)'\);" , re . DOTALL ) . findall ( iiI )
 for url in i1iIi :
  print url
  IiI1iiiIii ( '[COLORgreen]' + name + '[/COLOR]' , url , 222 , '' )
  if 45 - 45: O0 / i1IIi * OoOO * Ooo00oOo00o
def II11I ( ) :
 OOOOO0oo0O0O0 = oOoO0O0o0Oooo ( oOo0oooo00o ( 'aHR0cDovL3JldHJvdmlzaW9uLnR2L2FsbC8=' ) )
 i1iIi = re . compile ( '<a href="([^"]*)"><h2><font color=".+?"><h2>(.+?)</font></h2></a>' ) . findall ( OOOOO0oo0O0O0 )
 for I1Ii1iI1 , ooOOoooooo in i1iIi :
  IiI1iiiIii ( ( '[COLORgreen]' + ooOOoooooo + '[/COLOR]' ) . replace ( '&#8211;' , ':' ) , I1Ii1iI1 , 8061 , oOOoO0 + 'classicmovies.png' )
def iiiI11iIIi1 ( url ) :
 OOOOO0oo0O0O0 = oOoO0O0o0Oooo ( url )
 i1iIi = re . compile ( "v.src = '([^']*)';" ) . findall ( OOOOO0oo0O0O0 )
 for url in i1iIi :
  II1IIiiIiI ( url )
  if 72 - 72: oO0o0ooO0 * OoOO0ooOOoo0O
def oooo ( ) :
 OOOOO0oo0O0O0 = oOoO0O0o0Oooo ( oOo0oooo00o ( 'aHR0cDovL3JldHJvdmlzaW9uLnR2L2NsYXNzaWMtdHYv' ) )
 i1iIi = re . compile ( '<a href="([^"]*)"><h2><font color=".+?"><h2>(.+?)</font></h2></a>' ) . findall ( OOOOO0oo0O0O0 )
 for I1Ii1iI1 , ooOOoooooo in i1iIi :
  IiI1iiiIii ( ( '[COLORgreen]' + ooOOoooooo + '[/COLOR]' ) . replace ( '&#8211;' , ':' ) , I1Ii1iI1 , 8061 , oOOoO0 + 'classictv.png' )
def iiiIIIii ( url ) :
 OOOOO0oo0O0O0 = oOoO0O0o0Oooo ( url )
 i1iIi = re . compile ( "v.src = '([^']*)';" ) . findall ( OOOOO0oo0O0O0 )
 for url in i1iIi :
  II1IIiiIiI ( url )
  if 93 - 93: iIii1I11I1II1 + OOOo0 + i11iIiiIii
def O0Oo0 ( ) :
 iiI = IIiIi1iI ( oOo0oooo00o ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vbTN1c3RyZWFtcw==' ) )
 i1iIi = re . compile ( '<li><a href="(.+?)"> (.+?).m3u</a></li>' ) . findall ( iiI )
 for I1Ii1iI1 , ooOOoooooo in i1iIi :
  O0OO0O ( ( '[COLORgreen]' + ooOOoooooo + '[/COLOR]' ) . replace ( '-' , ' ' ) . replace ( '_' , ' ' ) , ( oOo0oooo00o ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vbTN1c3RyZWFtcy8=' ) ) + I1Ii1iI1 , 8071 , oOOoO0 + 'streams.png' )
def OO0 ( url ) :
 iiI = oOoO0O0o0Oooo ( url )
 i1iIi = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( iiI )
 for ooOOoooooo , url in i1iIi :
  IiI1iiiIii ( ( '[COLORgreen]' + ooOOoooooo + '[/COLOR]' ) . replace ( '_' , ' ' ) , ( url ) . strip ( ) , 404 , oOOoO0 + 'streams.png' )
def I1iIiI1Iii ( url ) :
 iiI = oOoO0O0o0Oooo ( url )
 i1iIi = re . compile ( 'EXTINF:(.+?),(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( iiI )
 for oOo0 , ooOOoooooo , url in i1iIi :
  IiI1iiiIii ( ( '[COLORgreen]' + ooOOoooooo + '[/COLOR]' ) . replace ( '_' , ' ' ) , ( ( oOo0oooo00o ( 'aHR0cDovL2dlbmlldHYuaXB0di5yZTo4MDAwL2xpdmUv' ) ) + oooOOOOO + '/' + i1iiIII111ii + url ) . strip ( ) , 222 , oOo0 )
  if 65 - 65: O0oO / i11iIiiIii / Ooo00oOo00o - OoOO0ooOOoo0O
def IiI1o0O ( ) :
 i11i1I ( 'Best Videos' , 'http://www.xvideos.com/best' , 10105 , oOOoO0 + 'JIZBOX.png' , '' , '' )
 i11i1I ( 'Genres' , 'http://www.xvideos.com' , 10106 , oOOoO0 + 'JIZBOX.png' , '' , '' )
 i11i1I ( 'Recently Uploaded' , 'http://xvideos.com' , 10105 , oOOoO0 + 'JIZBOX.png' , '' , '' )
 i11i1I ( 'Tags' , 'http://www.xvideos.com/tags' , 10103 , oOOoO0 + 'JIZBOX.png' , '' , '' )
 i11i1I ( 'Search' , '' , 10107 , oOOoO0 + 'JIZBOX.png' , '' , '' , )
 if 100 - 100: oO0o0ooO0 / Ooo00oOo00o * iIii1I11I1II1 * O0 - i1IIi
def Ii11iI1II11ii ( url ) :
 iiI = IIiIi1iI ( url )
 I1 = re . compile ( '<li><a class=".+?".+?href="(.+?)">Next</a></li>' ) . findall ( iiI )
 for url in I1 :
  i11i1I ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10103 , oOOoO0 + 'JIZBOX.png' , '' , '' )
 i1iIi = re . compile ( '<li><a href="(.+?)"><b>(.+?)</b><span class="navbadge default"(.+?)</span>' ) . findall ( iiI )
 for url , ooOOoooooo , oOooo00O in i1iIi :
  i11i1I ( ooOOoooooo + ' - No of Videos : ' + ( oOooo00O ) . replace ( '>' , '' ) , 'http://www.xvideos.com' + url , 10105 , oOOoO0 + 'JIZBOX.png' , '' , '' )
  if 66 - 66: I1IiI + i1IIi % OoOoOO00 . O0 * ii11ii1ii % ii11ii1ii
def O0oOO0o ( url ) :
 iiI = IIiIi1iI ( url )
 I1 = re . compile ( 'href="([^"]*)">Next</a></li>' ) . findall ( iiI )
 for url in I1 :
  i11i1I ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10104 , oOOoO0 + 'JIZBOX.png' , '' , '' )
 i1iIi = re . compile ( ':"([^"]*)".+?;</script></a></div></div><p class="profile-name"><a href="([^"]*)">(.+?)</a></p><p class="profile-counts">\n(.+?)\n' , re . DOTALL ) . findall ( iiI )
 for oOo0 , url , ooOOoooooo , iiiiI1IiI1I1 in i1iIi :
  i11i1I ( ooOOoooooo + '--' + iiiiI1IiI1I1 , 'http://www.xvideos.com' + url + '#_tabVideos,videos-best' , 10105 , ( oOo0 ) . replace ( 'http:\/\/' , 'http://' ) , '' , '' )
  if 19 - 19: o00O0oo
  if 55 - 55: OoOO0ooOOoo0O % OoOO0ooOOoo0O / O0 % oO0o0ooO0 - OOooOOo . Oo
def iiiii1I1III1 ( url ) :
 iiI = IIiIi1iI ( url )
 i1iIi = re . compile ( '<div class="thumb-inside"><script>.+?<img src="(.+?)".+?<a href="(.+?)" title=".+?">(.+?)</a></p>.+?uration">(.+?)</span>.+?Porn quality:(.+?)</span>' , re . DOTALL ) . findall ( iiI )
 for oOo0 , url , ooOOoooooo , i1oO00O , oo0o0ooooo in i1iIi :
  I1111I1iII11 ( ooOOoooooo + ' - Porn Quality : ' + oo0o0ooooo + ' - ' + i1oO00O , 'http://www.xvideos.com' + url , 10108 , oOo0 , oOo0 , oo0o0ooooo + ' - ' + i1oO00O )
 O0o0O = re . compile ( '<li><a href="([^"]*)" class="no-page">Next</a></li></ul></div>' ) . findall ( iiI )
 for url in O0o0O :
  i11i1I ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10105 , oOOoO0 + 'JIZBOX.png' , '' , '' )
  if 6 - 6: OoOoOO00
def I11i1iIi111 ( url ) :
 iiI = IIiIi1iI ( url )
 I11ii1i1 = re . compile ( '<div class="main-categories">(.+?)</div>' , re . DOTALL ) . findall ( iiI )
 I1 = re . compile ( '<li><a class=".+?".+?href="(.+?)">Next</a></li>' ) . findall ( iiI )
 for url in I1 :
  i11i1I ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10106 , oOOoO0 + 'JIZBOX.png' , '' , '' )
 i1iIi = re . compile ( '<li><a href="(.+?)" class="btn btn-default">(.+?)</a>' ) . findall ( str ( I11ii1i1 ) )
 for url , ooOOoooooo in i1iIi :
  i11i1I ( ooOOoooooo , 'http://www.xvideos.com' + url , 10105 , oOOoO0 + 'JIZBOX.png' , '' , '' )
  if 35 - 35: OOooOOo
  if 73 - 73: O0 - ii11ii1ii
def ii1I ( ) :
 o00o0 = Oo0o0000o0o0 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oO0O = ( o00o0 ) . replace ( ' ' , '+' ) . replace ( '&amp;' , '&' )
 II1III1I1I1Ii = oO0O . lower ( )
 ooOOooo0ooo00 = 'http://www.xvideos.com/?k=' + II1III1I1I1Ii
 print ooOOooo0ooo00 + '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'
 iiI = IIiIi1iI ( ooOOooo0ooo00 )
 i1iIi = re . compile ( '<div class="thumb-inside"><script>.+?<img src="(.+?)".+?<a href="(.+?)" title=".+?">(.+?)</a></p>.+?uration">(.+?)</span>.+?Porn quality:(.+?)</span>' , re . DOTALL ) . findall ( iiI )
 for oOo0 , I1Ii1iI1 , ooOOoooooo , i1oO00O , oo0o0ooooo in i1iIi :
  I1111I1iII11 ( ooOOoooooo + ' - Porn Quality : ' + oo0o0ooooo + ' - ' + i1oO00O , 'http://www.xvideos.com' + I1Ii1iI1 , 10108 , oOo0 , oOo0 , oo0o0ooooo + ' - ' + i1oO00O )
 O0o0O = re . compile ( '<li><a href="([^"]*)" class="no-page">Next</a></li></ul></div>' ) . findall ( iiI )
 for I1Ii1iI1 in O0o0O :
  i11i1I ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + I1Ii1iI1 , 10105 , oOOoO0 + 'JIZBOX.png' , '' , '' )
  if 56 - 56: OOOo0
def ii1IIi1ii ( url ) :
 iiI = IIiIi1iI ( url )
 i1iIi = re . compile ( 'flv_url=(.+?)\;' ) . findall ( iiI )
 for url in i1iIi :
  oo0OoOOooO = ( url ) . replace ( '%3A' , ':' ) . replace ( '%2F' , '/' ) . replace ( '%3F' , '?' ) . replace ( '%3D' , '=' ) . replace ( '%26' , '&' ) . replace ( '&amp' , '' )
  o0o0OO0o00o0O ( oo0OoOOooO )
  if 28 - 28: Ooo00oOo00o - OoOO + I1IiI + o00O0oo / iIii1I11I1II1
def o0o0OO0o00o0O ( url ) :
 iiiii11I1 = xbmc . Player ( Ii1OOOo ( ) )
 import urlresolver
 try : iiiii11I1 . play ( url )
 except : pass
 if 35 - 35: o0oO0 - Ooo00oOo00o . Oo * Oo / i11iIiiIii + ii11ii1ii
 if 87 - 87: I1IiI % iIii1I11I1II1
def o0OO0OOO0O ( ) :
 iiI = IIiIi1iI ( oOo0oooo00o ( 'aHR0cDovL3d3dy5nb2Zpc2hpbmcuY28udWsvQW5nbGluZy1UaW1lcy9TZWN0aW9uL1ZpZGVvcy8=' ) )
 i1iIi = re . compile ( 'class="item.+?"><a href="(.+?)">(.+?)</a></li>' ) . findall ( iiI )
 for I1Ii1iI1 , ooOOoooooo in i1iIi :
  O0OO0O ( '[COLORgreen]' + ooOOoooooo + '[/COLOR]' , ( 'http://www.gofishing.co.uk' + I1Ii1iI1 ) . replace ( 'http://www.gofishing.co.ukhttp://www.gofishing.co.uk' , 'http://www.gofishing.co.uk' ) , 8091 , oOOoO0 + 'gofish.png' )
def Iii1I ( url ) :
 iiI = oOoO0O0o0Oooo ( url )
 i1iIi = re . compile ( '<h2><a id=.+?href="([^"]*)">(.+?)</a></h2>' , re . DOTALL ) . findall ( iiI )
 o0OO0o0o00o = re . compile ( '<h3><a href="([^"]*)" id=.+?>(.+?)</a> </h3>.+?<img src="([^"]*)"' , re . DOTALL ) . findall ( iiI )
 next = re . compile ( 'href="([^"]*)">next</a>&gt;</li>' , re . DOTALL ) . findall ( iiI )
 for url , ooOOoooooo in i1iIi :
  IiI1iiiIii ( '[COLORgreen]' + ooOOoooooo + '[/COLOR]' , 'http://www.gofishing.co.uk/' + url , 8092 , oOOoO0 + 'gofish.png' )
 for url , ooOOoooooo , oOo0 in o0OO0o0o00o :
  IiI1iiiIii ( '[COLORgreen]' + ooOOoooooo + '[/COLOR]' , 'http://www.gofishing.co.uk/' + url , 8092 , 'http://www.gofishing.co.uk/' + oOo0 )
 for url in next :
  O0OO0O ( '[COLORgreen]NEXT[/COLOR]' , url . replace ( ' ' , '+' ) , 8091 , oOOoO0 + 'gofish.png' )
def oOoOOOOoOO0o ( url ) :
 iiI = oOoO0O0o0Oooo ( url )
 i1iIi = re . compile ( 'src="https://www.youtube.com/embed/(.+?)"' ) . findall ( iiI )
 for url in i1iIi :
  yt . PlayVideo ( url )
  if 31 - 31: OOOo0 . IIII + ii11ii1ii
def oO0OOO0o0O ( url ) :
 OOOOO0 = urllib2 . Request ( url )
 OOOOO0 . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
 Ooo0Oo0o = ''
 OOOo00oo0oO = ''
 try :
  Ooo0Oo0o = urllib2 . urlopen ( OOOOO0 )
  OOOo00oo0oO = Ooo0Oo0o . read ( )
  Ooo0Oo0o . close ( )
 except : pass
 if OOOo00oo0oO != '' :
  return OOOo00oo0oO
 else :
  OOOo00oo0oO = 'Failed'
  return OOOo00oo0oO
  if 85 - 85: OOOo0
def Ii1Ii1I ( ) :
 oOO0ooOo00O0OO = ( oOo0oooo00o ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 o00o0 = Oo0o0000o0o0 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 II1III1I1I1Ii = o00o0 . lower ( )
 I1Ii1iI1 = ( oOo0oooo00o ( 'aHR0cDovL2RsNC5tb3ZpZWZhcnNpLmNvbS9maWxtLzIwMTUtNy8=' ) )
 O0o0OO0000ooo = ( oOo0oooo00o ( 'aHR0cDovL2RsLmF2YWRsLmNvbS9OZXcvTW92aWUv' ) )
 oOOOoo0o = ( oOo0oooo00o ( 'aHR0cDovLzIxNy4yMTkuMTQzLjEwOC8xMzI3Lw==' ) )
 iiiI1IiIIii = ( oOo0oooo00o ( 'aHR0cDovLzE3OC4xNjIuMjE0LjIzMi92b2QvbW92aWVzL2VuZ2xpc2gv' ) )
 IIIIiiiIi11Ii1iI = ( oOo0oooo00o ( 'aHR0cDovL3Njb29ieXN0cmVhbS54MTBob3N0LmNvbS8vc2Nvb2J5L21vdi9hbGwucGhw' ) )
 OOOo00 = ( oOo0oooo00o ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 i1I111i1ii = ( oOo0oooo00o ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL3NlYXJjaC8/cT0=' ) ) + o00o0
 oO0oOoo0O = ( oOo0oooo00o ( 'aHR0cDovL2xldHdhdGNoLnVzLz9vcD1zZWFyY2gmaz0=' ) ) + ( o00o0 ) . replace ( ' ' , '+' )
 if 26 - 26: Oo + OOOo0 * OoOO0ooOOoo0O + o0oO0
 iiI = oO0OOO0o0O ( I1Ii1iI1 )
 II1iIi1IiIii = oO0OOO0o0O ( O0o0OO0000ooo )
 O00o0O = oO0OOO0o0O ( oOOOoo0o )
 O00oOo0O0o00O = oO0OOO0o0O ( iiiI1IiIIii )
 ooo0oo00O00Oo = oO0OOO0o0O ( IIIIiiiIi11Ii1iI )
 OOO000000OOO0 = oO0OOO0o0O ( i1I111i1ii )
 ooOoOOoooO000 = IIiIi1iI ( oO0oOoo0O )
 if 85 - 85: OOOo0 % o0000oOoOoO0o + OoOO0ooOOoo0O / o00O0oo % OoooooooOO
 if iiI != 'Failed' :
  i1iIi = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( iiI )
  for i11i11II11i1 , ooOOoooooo in i1iIi :
   if o00o0 in ooOOoooooo . lower ( ) :
    IiI1iiiIii ( ( '[COLORgreen]' + ooOOoooooo + '- source 1[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( I1Ii1iI1 + i11i11II11i1 ) , 222 , '' )
 if II1iIi1IiIii != 'Failed' :
  o0OO0o0o00o = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( II1iIi1IiIii )
  for i11i11II11i1 , ooOOoooooo in o0OO0o0o00o :
   if o00o0 in ooOOoooooo . lower ( ) :
    IiI1iiiIii ( ( '[COLORgreen]' + ooOOoooooo + '- source 2[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( O0o0OO0000ooo + i11i11II11i1 ) , 222 , '' )
 if O00o0O != 'Failed' :
  iIII = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( O00o0O )
  for i11i11II11i1 , ooOOoooooo in iIII :
   if o00o0 in ooOOoooooo . lower ( ) :
    IiI1iiiIii ( ( '[COLORgreen]' + ooOOoooooo + '- source 3[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( oOOOoo0o + i11i11II11i1 ) , 222 , '' )
 if O00oOo0O0o00O != 'Failed' :
  iiiI1i1 = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( O00oOo0O0o00O )
  for i11i11II11i1 , ooOOoooooo in iiiI1i1 :
   if o00o0 in ooOOoooooo . lower ( ) :
    IiI1iiiIii ( ( '[COLORgreen]' + ooOOoooooo + '- source 4[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( iiiI1IiIIii + i11i11II11i1 ) , 222 , '' )
 if ooo0oo00O00Oo != 'Failed' :
  I1i1i11 = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( ooo0oo00O00Oo )
  for i11i11II11i1 , oOo0 , ooOOoooooo in I1i1i11 :
   if o00o0 in ooOOoooooo . lower ( ) :
    O0OO0O ( ( '[COLORgreen]' + ooOOoooooo + '- source Scooby[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( 'Ganool' , '' ) . replace ( 'ShAaNiG' , '' ) . replace ( 'YIFY' , '' ) . replace ( '[[ Max-Movie.In ]]' , '' ) . replace ( '.mkv' , '' ) . replace ( '.mp4' , '' ) . replace ( '.' , ' ' ) , i11i11II11i1 , 1006 , 'img' )
    if 29 - 29: IIII . o0oO0 - OoOoOO00
    I1i1I1II ( 'tvshows' , 'Media Info 3' )
 if OOO000000OOO0 != 'Failed' :
  ooooO0 = re . compile ( 'href="(.+?)".+?src="(.+?)" alt="Image of (.+?)"' , re . DOTALL ) . findall ( OOO000000OOO0 )
  for I1Ii1iI1 , oOo0 , ooOOoooooo in ooooO0 :
   if o00o0 in ooOOoooooo . lower ( ) :
    O0OO0O ( ( '[COLORgreen]' + ooOOoooooo + '- source Snag[/COLOR]' ) . replace ( '&#x27;' , '' ) , 'http://www.snagfilms.com' + I1Ii1iI1 , 7067 , oOo0 )
    if 37 - 37: i11iIiiIii + OOOo0 . OoOO0ooOOoo0O % o0000oOoOoO0o % o0000oOoOoO0o
    I1i1I1II ( 'tvshows' , 'Media Info 3' )
 if ooOoOOoooO000 != 'Failed' :
  iiI11I1iiIiII1I = re . compile ( '<div class="video_block video_block_default ">.+?<a href="#">.+?<a href="(.*?)".+?<img src="(.+?)" height=".+?" alt="(.+?)"' , re . DOTALL ) . findall ( ooOoOOoooO000 )
  for I1Ii1iI1 , oOo0 , ooOOoooooo in iiI11I1iiIiII1I :
   IiI1iiiIii ( '[COLORgreen]' + ooOOoooooo + '- Source 7[/COLOR]' , I1Ii1iI1 , 222 , oOo0 )
 oOOOoo = [ '0-9/' , 'A/' , 'B/' , 'C/' , 'D/' , 'E/' , 'F/' , 'G/' , 'H/' , 'I/' , 'J/' , 'K/' , 'L/' , 'M/' , 'N/' , 'O/' , 'P/' , 'R/' , 'S/' , 'T/' , 'U/' , 'V/' , 'W/' , 'X/' , 'Y/' , 'Z/' ]
 if 59 - 59: O0oO - IIII
 if 14 - 14: iIii1I11I1II1 - iIii1I11I1II1
 for oooO0o0o0O0 in oOOOoo :
  iii11111I = oOO0ooOo00O0OO + oooO0o0o0O0
  i111i1I1ii1i = oO0OOO0o0O ( iii11111I )
  if ooo0oo00O00Oo != 'Failed' :
   O0Oooo = re . compile ( '<li><a href="(.+?)"> (.+?)</a></li>' ) . findall ( i111i1I1ii1i )
   for i11i11II11i1 , ooOOoooooo in O0Oooo :
    if o00o0 in ooOOoooooo . lower ( ) :
     IiI1iiiIii ( ( '[COLORgreen]' + ooOOoooooo + 'source 5[/COLOR]' ) . replace ( 'Ganool' , '' ) . replace ( 'ShAaNiG' , '' ) . replace ( 'YIFY' , '' ) . replace ( '[[ Max-Movie.In ]]' , '' ) . replace ( '.mkv' , '' ) . replace ( '.mp4' , '' ) . replace ( '.' , ' ' ) , ( oOO0ooOo00O0OO + oooO0o0o0O0 + i11i11II11i1 ) , 222 , '' )
     if 27 - 27: o0oO0 + i11iIiiIii * o0000oOoOoO0o + I1IiI + oO0o0ooO0
     I1i1I1II ( 'tvshows' , 'Media Info 3' )
     if 87 - 87: O0
     if 87 - 87: OOooOOo / OoOoOO00
def O0OOOo000 ( ) :
 if 3 - 3: Oo % o0oO0 - OoooooooOO * oO0o0ooO0 . OoOO0ooOOoo0O
 o00o0 = Oo0o0000o0o0 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 II1III1I1I1Ii = o00o0 . lower ( )
 I1Ii1iI1 = ( oOo0oooo00o ( 'aHR0cDovL2RsLmZhcnNpbW92aWUubmV0L1NlcmlhbC8=' ) )
 O0o0OO0000ooo = ( oOo0oooo00o ( 'aHR0cDovL3N2Mi5kbC1wYXJzLmluLw==' ) )
 oOOOoo0o = ( oOo0oooo00o ( 'aHR0cDovL3R2LmRsLXBhcnMuaW4v' ) )
 iiiI1IiIIii = ( oOo0oooo00o ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9BbWVyaWNhbiUyMFNlcmlhbC8=' ) )
 IIIIiiiIi11Ii1iI = ( oOo0oooo00o ( 'aHR0cDovL2RpemlsYWIuY29tL2Fyc2l2P2xpbWl0PSZ0dXI9Jm9yZGVyYnk9JnVsa2U9Jm9yZGVyPSZ5aWw9JmRpemlfYWRpPQ==' ) ) + ( o00o0 ) . replace ( ' ' , '+' )
 OOOo00 = ( oOo0oooo00o ( 'aHR0cDovL3Njb29ieXN0cmVhbS54MTBob3N0LmNvbS8vc2Nvb2J5L3Nob3dzL3R2YWxsLnBocA==' ) )
 oO0oOoo0O = ( oOo0oooo00o ( 'aHR0cDovL2xldHdhdGNoLnVzLz9vcD1zZWFyY2gmaz0=' ) ) + ( o00o0 ) . replace ( ' ' , '+' )
 Ii1I1i111 = ( oOo0oooo00o ( 'aHR0cDovL3d3dy53YXRjaHNlcmllcy5saS9zZWFyY2gv' ) ) + o00o0 . replace ( ' ' , '%20' )
 if 57 - 57: OoOO . OOOo0
 iiI = oO0OOO0o0O ( I1Ii1iI1 )
 II1iIi1IiIii = oO0OOO0o0O ( O0o0OO0000ooo )
 O00o0O = oO0OOO0o0O ( oOOOoo0o )
 O00oOo0O0o00O = oO0OOO0o0O ( iiiI1IiIIii )
 ooo0oo00O00Oo = cloudflare . source ( IIIIiiiIi11Ii1iI )
 i111i1I1ii1i = oO0OOO0o0O ( OOOo00 )
 ooOoOOoooO000 = IIiIi1iI ( oO0oOoo0O )
 iIIi11i1i1i1I = IIiIi1iI ( Ii1I1i111 )
 if iiI != 'Failed' :
  i1iIi = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( iiI )
  for ooOOoooooo in i1iIi :
   if o00o0 in ooOOoooooo . lower ( ) :
    O0OO0O ( ( '[COLORgreen]' + ooOOoooooo + ' source 1[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( I1Ii1iI1 + ooOOoooooo ) . replace ( ' ' , '%20' ) , 1006 , '' )
    if 13 - 13: oO0o0ooO0 + OoOO0ooOOoo0O / iIii1I11I1II1
    I1i1I1II ( 'tvshows' , 'Media Info 3' )
 if II1iIi1IiIii != 'Failed' :
  o0OO0o0o00o = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( II1iIi1IiIii )
  for ooOOoooooo in o0OO0o0o00o :
   if o00o0 in ooOOoooooo . lower ( ) :
    O0OO0O ( ( '[COLORgreen]' + ooOOoooooo + ' source 2[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( O0o0OO0000ooo + ooOOoooooo ) . replace ( ' ' , '%20' ) , 1006 , '' )
    if 67 - 67: I1IiI - I1IiI * Ooo00oOo00o - oO0o0ooO0 % OoOO
    I1i1I1II ( 'tvshows' , 'Media Info 3' )
 if O00o0O != 'Failed' :
  iIII = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( O00o0O )
  for ooOOoooooo in o0OO0o0o00o :
   if o00o0 in ooOOoooooo . lower ( ) :
    O0OO0O ( ( '[COLORgreen]' + ooOOoooooo + ' source 3[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( oOOOoo0o + ooOOoooooo ) . replace ( ' ' , '%20' ) , 1006 , '' )
    if 44 - 44: OOOo0 . i1IIi + OoOO0ooOOoo0O
    I1i1I1II ( 'tvshows' , 'Media Info 3' )
 if O00oOo0O0o00O != 'Failed' :
  iiiI1i1 = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( O00oOo0O0o00O )
  for ooOOoooooo in o0OO0o0o00o :
   if o00o0 in ooOOoooooo . lower ( ) :
    O0OO0O ( ( '[COLORgreen]' + ooOOoooooo + ' source 4[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( iiiI1IiIIii + ooOOoooooo ) . replace ( ' ' , '%20' ) , 1006 , '' )
    if 16 - 16: OOooOOo - Ooo00oOo00o / O0oO
    I1i1I1II ( 'tvshows' , 'Media Info 3' )
 if ooo0oo00O00Oo != 'Failed' :
  I1i1i11 = re . compile ( '<a href="(.+?)" class="film-image">\n<img src="(.+?)" alt=""/>\n</a>\n<div class="tss-detail">\n<a class="title" style="" href=".+?">\n<span class="position">.+?</span>\n(.+?)</a>' ) . findall ( ooo0oo00O00Oo )
  for I1Ii1iI1 , oOo0 , ooOOoooooo in I1i1i11 :
   if o00o0 in ooOOoooooo . lower ( ) :
    O0OO0O ( '[COLORgreen]' + ooOOoooooo + ' - Source - Dizi[/COLOR]' , I1Ii1iI1 , 8062 , oOo0 )
    if 48 - 48: iIii1I11I1II1
    I1i1I1II ( 'tvshows' , 'Media Info 3' )
 if i111i1I1ii1i != 'Failed' :
  O0Oooo = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( i111i1I1ii1i )
  for I1Ii1iI1 , oOo0 , ooOOoooooo in O0Oooo :
   if o00o0 in ooOOoooooo . lower ( ) :
    IiI1iiiIii ( ( '[COLORgreen]' + ooOOoooooo + '- Source Scooby[/COLOR]' ) , I1Ii1iI1 , 222 , 'img' )
    if 91 - 91: OoOoOO00 - O0 . iIii1I11I1II1 . O0 + ii11ii1ii - OoOoOO00
    I1i1I1II ( 'tvshows' , 'Media Info 3' )
 if ooOoOOoooO000 != 'Failed' :
  iiI11I1iiIiII1I = re . compile ( '<div class="video_block video_block_default ">.+?<a href="#">.+?<a href="(.*?)".+?<img src="(.+?)" height=".+?" alt="(.+?)"' , re . DOTALL ) . findall ( ooOoOOoooO000 )
  for I1Ii1iI1 , oOo0 , ooOOoooooo in iiI11I1iiIiII1I :
   IiI1iiiIii ( '[COLORgreen]' + ooOOoooooo + ' - Source DiZzY[/COLOR]' , I1Ii1iI1 , 222 , oOo0 )
 if iIIi11i1i1i1I != 'Failed' :
  iiIiiIi1 = re . compile ( '<img src="(.+?)".+?<a href="(.+?)" title=".+?"><b>(.+?)</b>' , re . DOTALL ) . findall ( iIIi11i1i1i1I )
  for oOo0 , I1Ii1iI1 , ooOOoooooo in iiIiiIi1 :
   if 'watch online' in ooOOoooooo :
    pass
   else :
    ooooooO0oo ( '[COLORgreen]' + ooOOoooooo + '- Source WATCH SERIES[/COLOR]' , 'http://www.watchseries.li' + I1Ii1iI1 , 10044 , oOo0 , '' , '' )
    if 30 - 30: OoOO0ooOOoo0O + OoOoOO00 - IIII * OoooooooOO
    xbmcplugin . setContent ( O00o0OO , 'movies' )
    if 19 - 19: IIII - OOooOOo . iIii1I11I1II1 . I1IiI / OoOO0ooOOoo0O
def OOO0O00Oo ( ) :
 if 13 - 13: iIii1I11I1II1
 o00o0 = Oo0o0000o0o0 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 II1III1I1I1Ii = o00o0 . lower ( )
 I1Ii1iI1 = ( oOo0oooo00o ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz' ) )
 iiI = IIiIi1iI ( I1Ii1iI1 )
 i1iIi = re . compile ( '"id":".+?","name":"(.+?)","img":"(.+?)","stream_url3":".+?","cat_id":"(.+?)","stream_url2":".+?","stream_url":".+?"}' , re . DOTALL ) . findall ( iiI )
 for ooOOoooooo , oOo0 , IiIIII1iiIIi in i1iIi :
  i1I1IiI1ii = oOo0oooo00o ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv' ) + ( oOo0 ) . replace ( '\\' , '' )
  if o00o0 in ooOOoooooo . lower ( ) :
   O0OO0O ( ooOOoooooo , '' , 7022 , i1I1IiI1ii )
   if 64 - 64: oO0o0ooO0 * ii11ii1ii % OoOoOO00 - I1IiI + ii11ii1ii
 xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 62 - 62: I1IiI % OOooOOo % OOOo0 + IIII . Ooo00oOo00o
 if 48 - 48: OOOo0 * i11iIiiIii % OoOoOO00
def ii1IOoo000000 ( url ) :
 Oo00ooOoO = cloudflare . source ( url )
 i1iIi = re . compile ( '<a class="season" href="(.+?)">\n(.+?)\n</a>\n</span>\n<span>\n<a class="episode" href=".+?">\n(.+?)\n</a>\n</span>\n<span>\n<a class="episode-name" href=".+?">\n(.+?)</a>' ) . findall ( Oo00ooOoO )
 for url , I11iiIi1i1 , oooOO0OO0O , ooOOoooooo in i1iIi :
  O0OO0O ( ( I11iiIi1i1 ) . replace ( 'Sezon' , ' Season ' ) + ( oooOO0OO0O ) . replace ( 'Bölüm' , ' Episode ' ) + ooOOoooooo , url , 8063 , '' )
  if 100 - 100: i11iIiiIii / i11iIiiIii
  if 89 - 89: oO0o0ooO0 . i11iIiiIii * O0
  if 44 - 44: i1IIi . OOOo0 / i11iIiiIii + IIII
  if 27 - 27: OoOO0ooOOoo0O
def O0OO0ooO00 ( url ) :
 Oo00ooOoO = cloudflare . source ( url )
 i1iIi = re . compile ( 'file: "(.+?)",.+?label: "(.+?)",' , re . DOTALL ) . findall ( Oo00ooOoO )
 for url , ooOOoooooo in i1iIi :
  IiI1iiiIii ( ooOOoooooo , url , 222 , '' )
  if 83 - 83: iIii1I11I1II1
  if 63 - 63: OoooooooOO * Ooo00oOo00o / o0000oOoOoO0o - OoOO . iIii1I11I1II1 + oO0o0ooO0
  if 44 - 44: i1IIi % OOOo0 % OOooOOo
  if 9 - 9: Oo % OoooooooOO - o00O0oo
def iIII11Iiii1 ( ) :
 if 95 - 95: OOOo0
 Oo00ooOoO = cloudflare . source ( oOo0oooo00o ( 'aHR0cDovL2RpemlsYWIuY29t' ) )
 i1iIi = re . compile ( '<li id=".+?">.+?<a href="(.+?)">.+?<img width="40" height="40" src="(.+?)" alt=""/>.+?<span class="title">\n(.+?)</span>.+?<span class="alt-title">\n(.+?)</span>.+?</a>.+?</li>' , re . DOTALL ) . findall ( Oo00ooOoO )
 for I1Ii1iI1 , oOo0 , ooOOoooooo , oooOO0OO0O in i1iIi :
  O0OO0O ( ooOOoooooo + '  -  ' + ( oooOO0OO0O ) . replace ( 'sezon' , 'Season' ) . replace ( 'bölüm' , 'Episode' ) , I1Ii1iI1 , 8063 , oOo0 )
  if 99 - 99: O0
def O0oO0OOoO ( ) :
 OOOOO0oo0O0O0 = oOoO0O0o0Oooo ( oOo0oooo00o ( 'aHR0cDovL3d3dy50dmd1aWRlLmNvLnVrLw==' ) )
 i1iIi = re . compile ( '<a href="(.+?)"  qt-title=".+?" qt-text=".+?<br> .+?" title="(.+?)".+?class=".+? src="(.+?)" alt=".+?" /></a>' , re . DOTALL ) . findall ( OOOOO0oo0O0O0 )
 for I1Ii1iI1 , ooOOoooooo , oOo0 in i1iIi :
  IiI1iiiIii ( '[COLORgreen]' + ooOOoooooo + '[/COLOR]' , I1Ii1iI1 , 8002 , oOo0 )
def O00oo ( url ) :
 OOOOO0oo0O0O0 = oOoO0O0o0Oooo ( url )
 i1iIi = re . compile ( '<table border="0".+?url((.+?));background-repeat: no-repeat;">.+?<tr>.+?<span class="season">(.+?)</span><br>.+?<a href="(.+?)"+?>(.+?)</span><br>.+?<span class="programmetext">(.+?)</span></a><br>' , re . DOTALL ) . findall ( OOOOO0oo0O0O0 )
 for oOo0 , time , url , ooOOoooooo , OOO in i1iIi :
  ooooooO0oo ( '%s %s' % ( '[COLORgreen]' + ooOOoooooo + '[/COLOR]' , time ) , url , 1015 , oOo0 , OOO )
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
 iiI = IIiIi1iI ( 'http://uksoapshare.blogspot.co.uk/' )
 i1iIi = re . compile ( '<a href="(.+?)".+?target=_blank>(.+?)</a>' ) . findall ( iiI )
 for I1Ii1iI1 , ooOOoooooo in i1iIi :
  if 'Holly' in ooOOoooooo :
   oOo0 = 'http://2.bp.blogspot.com/-9c7Sieh1RKs/UjD6TGAEEnI/AAAAAAAAAC8/84uwHfxcuYg/s1600/Hollyoaks.png'
   if 'huge' in I1Ii1iI1 :
    IiI1iiiIii ( ( ooOOoooooo ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , I1Ii1iI1 . replace ( '\\/' , '/' ) , 8006 , oOo0 )
   else :
    pass
    if 50 - 50: O0oO + o0oO0 + oO0o0ooO0
 xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE_IGNORE_THE ) ;
 if 15 - 15: o0000oOoOoO0o
def IiiI11I1IIiI ( ) :
 iiI = IIiIi1iI ( 'http://uksoapshare.blogspot.co.uk/' )
 i1iIi = re . compile ( '<a href="(.+?)".+?target=_blank>(.+?)</a>' ) . findall ( iiI )
 for I1Ii1iI1 , ooOOoooooo in i1iIi :
  if 'East' in ooOOoooooo :
   oOo0 = 'http://3.bp.blogspot.com/-KWHcNbNJU8Y/Vi1ousRl7fI/AAAAAAAAAT8/ksNE12LH0nE/s1600/eastenders.jpg'
   if 'huge' in I1Ii1iI1 :
    IiI1iiiIii ( ( ooOOoooooo ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , I1Ii1iI1 . replace ( '\\/' , '/' ) , 8006 , oOo0 )
   else :
    pass
    if 5 - 5: Oo
 xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 100 - 100: o00O0oo + iIii1I11I1II1
def o0o0OoO0OOO0 ( ) :
 iiI = IIiIi1iI ( 'http://uksoapshare.blogspot.co.uk/' )
 i1iIi = re . compile ( '<a href="(.+?)".+?target=_blank>(.+?)</a>' ) . findall ( iiI )
 for I1Ii1iI1 , ooOOoooooo in i1iIi :
  if 'Emmer' in ooOOoooooo :
   oOo0 = 'http://2.bp.blogspot.com/-UfDcxisVV5c/UjH9vUicZ3I/AAAAAAAAADc/8Ozuiz1ojxw/s1600/Emmerdale.jpg'
   if 'huge' in I1Ii1iI1 :
    IiI1iiiIii ( ( ooOOoooooo ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , I1Ii1iI1 . replace ( '\\/' , '/' ) , 8006 , oOo0 )
   else :
    pass
    if 79 - 79: OoOO % OOooOOo % I1IiI
 xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 45 - 45: OOOo0 * OoOO0ooOOoo0O % Ooo00oOo00o
def i111I11I ( ) :
 iiI = IIiIi1iI ( 'http://uksoapshare.blogspot.co.uk/' )
 i1iIi = re . compile ( '<a href="(.+?)".+?target=_blank>(.+?)</a>' ) . findall ( iiI )
 for I1Ii1iI1 , ooOOoooooo in i1iIi :
  if 'Coro' in ooOOoooooo :
   oOo0 = 'http://3.bp.blogspot.com/-hofvfBQVexs/UjErIfNdS4I/AAAAAAAAADQ/Q-vVGu3apYU/s1600/corrie.jpg'
   if 'huge' in I1Ii1iI1 :
    IiI1iiiIii ( ( ooOOoooooo ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , I1Ii1iI1 . replace ( '\\/' , '/' ) , 8006 , oOo0 )
   else :
    pass
    if 80 - 80: iIii1I11I1II1 - OoooooooOO - ii11ii1ii - ii11ii1ii . OoooooooOO
 xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 48 - 48: O0oO . i11iIiiIii / i1IIi % IIII % oO0o0ooO0 + OoOO
def iiII1iiiiiii ( ) :
 iiI = IIiIi1iI ( 'http://uksoapshare.blogspot.co.uk/' )
 i1iIi = re . compile ( '<a href="(.+?)" target="_blank">(.+?)</a>' ) . findall ( iiI )
 for I1Ii1iI1 , ooOOoooooo in i1iIi :
  if 'Celeb' in ooOOoooooo :
   oOo0 = 'http://3.bp.blogspot.com/-a_yDotWU_pY/VkotKWaG_gI/AAAAAAAAAUk/8Q5iNM6p37k/s1600/iacgoh.jpg'
   if 'huge' in I1Ii1iI1 :
    IiI1iiiIii ( ( ooOOoooooo ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , I1Ii1iI1 . replace ( '\\/' , '/' ) , 8006 , oOo0 )
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
 OOOOO0oo0O0O0 = IIiIi1iI ( oOo0oooo00o ( 'aHR0cDovL3d3dy5kaXppYm94aGQuY29tLw==' ) )
 i1iIi = re . compile ( 'class="film menu-item menu-item-type-post_type menu-item-object-page menu-item-36980"><a href="(.+?)"><i class="fa fa-film"></i><span>(.+?)</span></a></li>' ) . findall ( OOOOO0oo0O0O0 )
 o0OO0o0o00o = re . compile ( 'class="menu-item menu-item-type-post_type menu-item-object-page menu-item-52949"><a href="(.+?)"><i class="fa fa-"></i><span>(.+?)</span></a></li>' ) . findall ( OOOOO0oo0O0O0 )
 for I1Ii1iI1 , ooOOoooooo in i1iIi :
  O0OO0O ( ( '[COLORgreen]' + ooOOoooooo + '[/COLOR]' ) . replace ( 'Diziler' , 'Series' ) , I1Ii1iI1 , 7071 , oOOoO0 + 'popcorn.png' )
 for I1Ii1iI1 , ooOOoooooo in o0OO0o0o00o :
  O0OO0O ( ( '[COLORgreen]' + ooOOoooooo + '[/COLOR]' ) . replace ( 'Filmler' , 'Movies' ) , I1Ii1iI1 , 7071 , oOOoO0 + 'popcorn.png' )
  if 62 - 62: OoOO0ooOOoo0O / OoOoOO00 + I1IiI % o0oO0 / I1IiI + ii11ii1ii
def IiI11I111 ( ) :
 OOOOO0oo0O0O0 = IIiIi1iI ( oOo0oooo00o ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL2NhdGVnb3JpZXMv' ) )
 i1iIi = re . compile ( '<a class="nav-item" href="(.+?)">(.+?)</a>' ) . findall ( OOOOO0oo0O0O0 )
 for I1Ii1iI1 , ooOOoooooo in i1iIi :
  if 'Movies' in ooOOoooooo :
   O0OO0O ( '[COLORgreen]' + ooOOoooooo + '[/COLOR]' , 'http://www.snagfilms.com' + ( I1Ii1iI1 ) . replace ( 'http://www.snagfilms.com' , '' ) , 7061 , oOOoO0 + 'popcorn.png' )
def Ooo000O00 ( url ) :
 OOOOO0oo0O0O0 = IIiIi1iI ( url )
 i1iIi = re . compile ( '<a class="object-link size-poster".+?href="(.+?)" data-type="category">.+?src="(.+?)" alt="Image of (.+?)" />' , re . DOTALL ) . findall ( OOOOO0oo0O0O0 )
 i1iIi = re . compile ( '<a class="object-link size-poster".+?href="(.+?)" data-type="category">.+?src="(.+?)" alt="Image of (.+?)" />' , re . DOTALL ) . findall ( OOOOO0oo0O0O0 )
 o0OO0o0o00o = re . compile ( "<li class='current'>.+?</li><li ><a href='(.+?)'>.+?</a></li><li" , re . DOTALL ) . findall ( OOOOO0oo0O0O0 )
 for url , oOo0 , ooOOoooooo in i1iIi :
  O0OO0O ( '[COLORgreen]' + ooOOoooooo + '[/COLOR]' , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7067 , oOo0 )
 for url in o0OO0o0o00o :
  O0OO0O ( '[COLORgreen]NEXT PAGE[/COLOR]' , ( url ) . replace ( '&#038;' , '&' ) , 7063 , oOOoO0 + 'popcorn.png' )
  if 36 - 36: OoOO0ooOOoo0O % i11iIiiIii
  if 47 - 47: i1IIi + OoOoOO00 . Oo * OoOO . o0000oOoOoO0o / i1IIi
def i11iioOOOOO0Ooooo ( url ) :
 OOOOO0oo0O0O0 = IIiIi1iI ( oOo0oooo00o ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL2NhdGVnb3JpZXMv' ) )
 i1iIi = re . compile ( '<a class="object-link size-poster".+?href="(.+?)" data-type="category">.+?src="(.+?)" alt="Image of (.+?)" />' , re . DOTALL ) . findall ( OOOOO0oo0O0O0 )
 for url , oOo0 , ooOOoooooo in i1iIi :
  O0OO0O ( '[COLORgreen]' + ooOOoooooo + '[/COLOR]' , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7062 , oOo0 )
  if 57 - 57: o00O0oo - OoooooooOO
  if 68 - 68: OOooOOo % ii11ii1ii / O0oO + O0oO - O0oO . Ooo00oOo00o
def oOO00ooOOo ( url ) :
 OOOOO0oo0O0O0 = IIiIi1iI ( url )
 i1iIi = re . compile ( 'href="(.+?)".+?src="(.+?)" alt="Image of (.+?)"' , re . DOTALL ) . findall ( OOOOO0oo0O0O0 )
 for url , oOo0 , ooOOoooooo in i1iIi :
  O0OO0O ( ( '[COLORgreen]' + ooOOoooooo + '[/COLOR]' ) . replace ( '&#x27;' , '' ) , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7067 , oOo0 )
  if 20 - 20: ii11ii1ii
def IIiiiiIiI1III ( url ) :
 OOOOO0oo0O0O0 = IIiIi1iI ( url )
 i1iIi = re . compile ( '<div class="film-container">.+?<iframe src="(.+?)"' , re . DOTALL ) . findall ( OOOOO0oo0O0O0 )
 for url in i1iIi :
  iIiI ( 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) )
  if 80 - 80: OoOO % OoOO % O0 - i11iIiiIii . oO0o0ooO0 / O0
def iIiI ( url ) :
 OOOOO0oo0O0O0 = IIiIi1iI ( url )
 i1iIi = re . compile ( 'file: "(.+?)",.+?label: "(.+?)"' , re . DOTALL ) . findall ( OOOOO0oo0O0O0 )
 for url , ooOOoooooo in i1iIi :
  IiI1iiiIii ( '[COLORgreen]' + ooOOoooooo + '[/COLOR]' , url , 222 , oOOoO0 + 'popcorn' )
  if 13 - 13: OOOo0 + O0 - ii11ii1ii % Oo / o00O0oo . i1IIi
  if 60 - 60: Oo . IIII % OOOo0 - O0oO
  if 79 - 79: OoooooooOO / ii11ii1ii . O0
  if 79 - 79: OoOO - OoOoOO00
def Ii1iiI1 ( ) :
 OOOOO0oo0O0O0 = IIiIi1iI ( oOo0oooo00o ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vc2VjcmV0L2Nsb3VkLnBocA==' ) )
 i1iIi = re . compile ( '<li class="col-sm-2">.+?<a href="#" class="thumbnail" data-src="(.+?)" data-toggle="modal".+?data-target="#infoModal" name="(.+?)"> <img src="(.+?)" alt=".+?" width="130px"' , re . DOTALL ) . findall ( OOOOO0oo0O0O0 )
 for I1Ii1iI1 , ooOOoooooo , oOo0 in i1iIi :
  IiI1iiiIii ( '[COLORgreen]' + ooOOoooooo + '[/COLOR]' , 'http://stream.cloudtv.bz/stream/channel/20/' + ( oOo0oooo00o ( I1Ii1iI1 ) ) , 222 , oOo0 )
  if 76 - 76: o00O0oo * iIii1I11I1II1
def iiI1iI ( ) :
 OOOOO0oo0O0O0 = IIiIi1iI ( oOo0oooo00o ( 'aHR0cDovL2hkbW92aWUxNC5uZXQv' ) )
 i1iIi = re . compile ( 'title="(.+?)" href="/list/category/(.+?)">' , re . DOTALL ) . findall ( OOOOO0oo0O0O0 )
 for ooOOoooooo , I1Ii1iI1 in i1iIi :
  O0OO0O ( '[COLORgreen]' + ooOOoooooo + '[/COLOR]' , 'http://hdmovie14.net/list/category/' + I1Ii1iI1 , 7051 , oOOoO0 + 'vod.png' )
  if 84 - 84: OoooooooOO + O0oO / OOOo0 % OoOO0ooOOoo0O % ii11ii1ii * OOOo0
def OOoO0oooo ( url ) :
 OOOOO0oo0O0O0 = IIiIi1iI ( url )
 i1iIi = re . compile ( 'href="(.+?)"><h3>(.+?)</h3>' , re . DOTALL ) . findall ( OOOOO0oo0O0O0 )
 for url , ooOOoooooo in i1iIi :
  O0OO0O ( '[COLORgreen]' + ooOOoooooo + '[/COLOR]' , 'http://hdmovie14.net' + url , 7052 , oOOoO0 + 'vod.png' )
  if 24 - 24: o0000oOoOoO0o / OOOo0 * i1IIi % OoooooooOO
def ooiI1i ( url ) :
 OOOOO0oo0O0O0 = IIiIi1iI
 i1iIi = re . compile ( 'id:"(.+?)",url:"(.+?)"' , re . DOTALL ) . findall ( OOOOO0oo0O0O0 )
 for url , oOo0 , ooOOoooooo in i1iIi :
  O0OO0O ( '[COLORgreen]' + ooOOoooooo + '[/COLOR]' , url , 222 , oOo0 )
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
 OOOOO0oo0O0O0 = IIiIi1iI ( oOo0oooo00o ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz' ) )
 i1iIi = re . compile ( '"id":".+?","name":"(.+?)","img":"(.+?)","stream_url3":".+?","cat_id":"(.+?)","stream_url2":".+?","stream_url":".+?"}' , re . DOTALL ) . findall ( OOOOO0oo0O0O0 )
 print 'Len Match: >>>' + str ( len ( i1iIi ) )
 for ooOOoooooo , oOo0 , IiIIII1iiIIi in i1iIi :
  i1I1IiI1ii = oOo0oooo00o ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv' ) + ( oOo0 ) . replace ( '\\' , '' )
  if IiIIII1iiIIi == i11i1O00oo00OOOO :
   O0OO0O ( ooOOoooooo , '' , 7022 , i1I1IiI1ii )
  elif iiIIII11iiii == True :
   O0OO0O ( ooOOoooooo , '' , 7022 , i1I1IiI1ii )
  else : pass
  if 79 - 79: I1IiI % OOOo0 % o00O0oo / i1IIi % Ooo00oOo00o
  xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 56 - 56: iIii1I11I1II1 - i11iIiiIii * oO0o0ooO0
def o0O0Ooo ( Search_Name ) :
 OOOOO0oo0O0O0 = IIiIi1iI ( oOo0oooo00o ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz' ) )
 i1iIi = re . compile ( '"id":".+?","name":"' + Search_Name + '","img":"(.+?)","stream_url3":"(.+?)","cat_id":".+?","stream_url2":"(.+?)","stream_url":"(.+?)"}' , re . DOTALL ) . findall ( OOOOO0oo0O0O0 )
 i1iIi = re . compile ( '"id":".+?","name":"' + Search_Name + '","img":"(.+?)","stream_url3":"(.+?)","cat_id":".+?","stream_url2":"(.+?)","stream_url":"(.+?)"}' , re . DOTALL ) . findall ( OOOOO0oo0O0O0 )
 for oOo0 , I1Ii1iI1 , O0o0OO0000ooo , oOOOoo0o in i1iIi :
  i1I1IiI1ii = oOo0oooo00o ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv' ) + ( oOo0 ) . replace ( '\\' , '' )
  IiI1iiiIii ( Search_Name + ': Link 1' , ( I1Ii1iI1 ) . replace ( '\\' , '' ) , 222 , i1I1IiI1ii )
  IiI1iiiIii ( Search_Name + ': Link 2' , ( O0o0OO0000ooo ) . replace ( '\\' , '' ) , 222 , i1I1IiI1ii )
  IiI1iiiIii ( Search_Name + ': Link 3' , ( oOOOoo0o ) . replace ( '\\' , '' ) , 222 , i1I1IiI1ii )
  if 79 - 79: o0oO0 . OoOO / OoOO - o0oO0 * Oo / OOooOOo
def iI1iiIi1 ( ) :
 OOOOO0oo0O0O0 = IIiIi1iI ( oOo0oooo00o ( oo ( 0 , [ 97 ] , [ 221 , 72 , 245 , 82 , 68 , 48 , 242 , 99 , 143 , 68 , 9 , 111 , 24 , 118 , 180 , 76 , 29 , 51 , 14 , 100 , 187 , 51 , 105 , 100 , 106 , 121 , 52 , 53 , 240 , 114 , 26 , 98 , 252 , 50 , 197 , 82 , 218 , 112 , 19 , 99 , 94 , 71 , 54 , 120 , 104 , 108 , 174 , 101 , 107 , 72 , 168 , 82 , 191 , 50 , 88 , 76 , 90 , 109 , 138 , 78 , 24 , 118 , 89 , 76 , 218 , 110 , 231 , 86 , 105 , 114 , 252 , 76 , 37 , 50 , 36 , 82 , 96 , 118 , 27 , 100 , 120 , 50 , 160 , 53 , 72 , 115 , 200 , 98 , 80 , 50 , 201 , 70 , 114 , 107 , 9 , 99 , 113 , 121 , 127 , 57 , 155 , 106 , 213 , 97 , 194 , 71 , 192 , 70 , 162 , 116 , 27 , 99 , 46 , 71 , 191 , 108 , 4 , 118 , 24 , 98 , 27 , 109 , 105 , 108 , 89 , 119 , 164 , 100 , 88 , 72 , 237 , 89 , 93 , 117 , 40 , 98 , 211 , 84 , 75 , 78 , 216 , 49 ] ) ) )
 i1iIi = re . compile ( '#EXTINF:-1,(.+)\s*(.+)\s*' ) . findall ( OOOOO0oo0O0O0 )
 for ooOOoooooo , I1Ii1iI1 in i1iIi :
  IiI1iiiIii ( ooOOoooooo , ( I1Ii1iI1 ) . replace ( '"' , ' ' ) . replace ( '&amp;' , '&' ) . strip ( ) + '|connection=keep-alive' , 222 , oOOoO0 + 'english.png' )
def i1iiiIi1Iii ( ) :
 OOOOO0oo0O0O0 = IIiIi1iI ( oOo0oooo00o ( oo ( 0 , [ 97 ] , [ 221 , 72 , 245 , 82 , 68 , 48 , 242 , 99 , 143 , 68 , 9 , 111 , 24 , 118 , 180 , 76 , 29 , 51 , 14 , 100 , 187 , 51 , 105 , 100 , 106 , 121 , 52 , 53 , 240 , 114 , 26 , 98 , 252 , 50 , 197 , 82 , 218 , 112 , 19 , 99 , 94 , 71 , 54 , 120 , 104 , 108 , 174 , 101 , 107 , 72 , 168 , 82 , 191 , 50 , 88 , 76 , 90 , 109 , 138 , 78 , 24 , 118 , 89 , 76 , 218 , 110 , 231 , 86 , 105 , 114 , 252 , 76 , 37 , 50 , 36 , 82 , 96 , 118 , 27 , 100 , 120 , 50 , 160 , 53 , 72 , 115 , 200 , 98 , 80 , 50 , 201 , 70 , 114 , 107 , 9 , 99 , 113 , 121 , 127 , 57 , 155 , 106 , 213 , 97 , 194 , 71 , 192 , 70 , 162 , 116 , 27 , 99 , 46 , 71 , 191 , 108 , 4 , 118 , 24 , 98 , 27 , 109 , 105 , 108 , 89 , 119 , 164 , 100 , 88 , 72 , 237 , 89 , 93 , 117 , 40 , 98 , 211 , 84 , 75 , 78 , 216 , 49 ] ) ) )
 i1iIi = re . compile ( '#EXTINF:-2,(.+)\s*(.+)\s*' ) . findall ( OOOOO0oo0O0O0 )
 for ooOOoooooo , I1Ii1iI1 in i1iIi :
  IiI1iiiIii ( ooOOoooooo , ( I1Ii1iI1 ) . replace ( '"' , ' ' ) . replace ( '&amp;' , '&' ) . strip ( ) , 222 , oOOoO0 + 'xxx.png' )
def o0oO0O ( ) :
 OOOOO0oo0O0O0 = IIiIi1iI ( oOo0oooo00o ( oo ( 0 , [ 97 , 129 , 72 , 149 , 82 , 100 , 48 , 63 , 99 , 170 , 68 , 159 , 111 , 42 , 118 , 83 , 76 , 128 , 51 , 61 , 100 , 44 , 51 , 201 , 100 , 148 , 121 , 134 , 53 ] , [ 159 , 114 , 70 , 98 , 144 , 50 , 37 , 82 , 253 , 112 , 184 , 99 , 50 , 71 , 154 , 120 , 110 , 108 , 179 , 101 , 250 , 72 , 65 , 82 , 125 , 50 , 52 , 76 , 28 , 109 , 124 , 78 , 191 , 118 , 193 , 76 , 193 , 110 , 145 , 86 , 92 , 114 , 193 , 76 , 41 , 50 , 82 , 82 , 206 , 118 , 32 , 100 , 163 , 50 , 209 , 53 , 191 , 115 , 42 , 98 , 30 , 50 , 237 , 70 , 26 , 107 , 70 , 99 , 64 , 121 , 115 , 57 , 230 , 116 , 32 , 97 , 39 , 88 , 58 , 104 , 38 , 50 , 77 , 98 , 185 , 50 , 86 , 81 , 80 , 117 , 111 , 98 , 226 , 84 , 75 , 78 , 210 , 49 ] ) ) )
 i1iIi = re . compile ( '#EXTINF:.+?,(.+)\s*(.+)\s*' ) . findall ( OOOOO0oo0O0O0 )
 for ooOOoooooo , I1Ii1iI1 in i1iIi :
  IiI1iiiIii ( ooOOoooooo , ( I1Ii1iI1 ) . replace ( '"' , ' ' ) . replace ( '&amp;' , '&' ) . strip ( ) , 222 , oOOoO0 + 'vod(1).png' )
  if 61 - 61: OOooOOo - OoOoOO00 % iIii1I11I1II1 . Oo . OOooOOo % O0oO
def o0o0O00o ( url ) :
 url
 Oo00 = xbmcgui . ListItem ( ooOOoooooo , path = url )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , Oo00 )
 return
 if 46 - 46: ii11ii1ii / O0oO + IIII / OoOO / O0oO / OoOO0ooOOoo0O
 if 73 - 73: o0oO0 + ii11ii1ii
def o0o ( url ) :
 OOOOO0oo0O0O0 = IIiIi1iI ( url )
 i1iIi = re . compile ( '<a class=.+?href="(.+?)">.+?<div class="videothumboverlay hidden-xs" id=".+?">(.+?)</div>.+?<div class="videothumbbox"><img src="(.+?)" class="videothumb" alt="(.+?)"></div>' , re . DOTALL ) . findall ( OOOOO0oo0O0O0 )
 o0OO0o0o00o = re . compile ( "<a href='(.+?)' class='paginationnext'>Next &raquo;</a></div>" ) . findall ( OOOOO0oo0O0O0 )
 for url , ii11ii11 , oOo0 , ooOOoooooo in i1iIi :
  ooooooO0oo ( ooOOoooooo , 'https://www.fitnessblender.com' + url , 7086 , 'https://www.fitnessblender.com' + oOo0 , '' , ( ii11ii11 ) . replace ( '</p>' , ' ' ) . replace ( '<p>' , ' ' ) )
  I1i1I1II ( 'tvshows' , 'Media Info 3' )
 for url in o0OO0o0o00o :
  O0OO0O ( 'NEXT' , 'https://www.fitnessblender.com' + url , 7085 , oOOoO0 + 'FITNESS.png' )
  if 46 - 46: I1IiI - O0
def O00Ooo ( url ) :
 iiI = IIiIi1iI ( url )
 i1iIi = re . compile ( '<div class=\'videowrapper\'><iframe width="700" height="394" src="//www.youtube.com/embed/(.+?)?rel=0&amp;wmode=transparent" frameborder="0"></iframe></div>.+?<div class="col-xs-6 col-md-2 rightborder">(.+?)</div>.+?<p class="videodetailvalue"><img src=\'(.+?)\'/></p>' , re . DOTALL ) . findall ( iiI )
 for url , ii11ii11 , oOo0 in i1iIi :
  I1111I1iII11 ( 'PLAY' , url , 8043 , 'https://www.fitnessblender.com' + oOo0 , '' , ii11ii11 )
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
 OOOOO0oo0O0O0 = IIiIi1iI ( url )
 i1iIi = re . compile ( 'cat-item-.+?"><a href="(.+?)" >(.+?)</a>' ) . findall ( OOOOO0oo0O0O0 )
 for url , ooOOoooooo in i1iIi :
  O0OO0O ( ooOOoooooo , url , 9031 , oOOoO0 + 'icon.png' )
def oO00000oO0o0O ( url ) :
 OOOOO0oo0O0O0 = IIiIi1iI ( url )
 i1iIi = re . compile ( '<a href="(.+?)" title=".+?" rel="bookmark"><time class="entry-date published updated" datetime=".+?">(.+?)</time></a>' ) . findall ( OOOOO0oo0O0O0 )
 for url , ooOOoooooo in i1iIi :
  O0OO0O ( ooOOoooooo , url , 9032 , oOOoO0 + 'icon.png' )
def IIIiI1iI1 ( url ) :
 OOOOO0oo0O0O0 = IIiIi1iI ( url )
 i1iIi = re . compile ( '#EXTINF:-.+?,(.+)\s*(.+)\s*' ) . findall ( OOOOO0oo0O0O0 )
 for ooOOoooooo , url in i1iIi :
  if '://' in ooOOoooooo :
   pass
   IiI1iiiIii ( ( ooOOoooooo ) . replace ( '<br />' , '' ) , ( url ) . replace ( '<br />' , '' ) , 222 , oOOoO0 + 'icon.png' )
def IIiIiiii1I1 ( url ) :
 OOOOO0oo0O0O0 = IIiIi1iI ( url )
 i1iIi = re . compile ( 'EXTINF:-.+?,(.+)</div></li><li class=".+?"><div class=".+?">(.+?)</div>).findall' ) . findall ( OOOOO0oo0O0O0 )
 for ooOOoooooo , url in i1iIi :
  IiI1iiiIii ( ooOOoooooo , url , 222 , oOOoO0 + 'icon.png' )
  if 74 - 74: OoOO / o00O0oo
  if 53 - 53: OoOoOO00 - oO0o0ooO0 . i1IIi / O0oO - i1IIi - OoOO0ooOOoo0O
  if 72 - 72: OOOo0 + i11iIiiIii + O0 * OoooooooOO
def ooO0 ( ) :
 OOOOO0oo0O0O0 = IIiIi1iI ( 'http://www.disclose.tv/action/videolist/aliens/page/1/all/channel/1/category/1/' )
 i1iIi = re . compile ( '<li><a href="([^"]*)">(.+?)</a></li>' ) . findall ( OOOOO0oo0O0O0 )
 for I1Ii1iI1 , ooOOoooooo in i1iIi :
  O0OO0O ( ooOOoooooo , 'http://www.disclose.tv/' + I1Ii1iI1 , 7010 , oOOoO0 + 'disclose.png' )
  if 94 - 94: o0000oOoOoO0o . OOOo0
  if 73 - 73: i1IIi / OoOoOO00
def I1i1I ( url ) :
 OOOOO0oo0O0O0 = IIiIi1iI ( url )
 i1iIi = re . compile ( 'href="([^"]*)"><img width="135" height="76" alt="([^"]*)".+?src="([^"]*)" />' , re . DOTALL ) . findall ( OOOOO0oo0O0O0 )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' ) . findall ( OOOOO0oo0O0O0 )
 for url , ooOOoooooo , oOo0 in i1iIi :
  O0OO0O ( ooOOoooooo , 'http://www.disclose.tv/' + url , 7011 , oOo0 )
 for url in next :
  O0OO0O ( 'NEXT' , url , 7010 , oOo0 )
  if 17 - 17: o0000oOoOoO0o - oO0o0ooO0 % o00O0oo
  if 2 - 2: o00O0oo * ii11ii1ii * OoooooooOO
def oOOOooO ( url ) :
 OOOOO0oo0O0O0 = IIiIi1iI ( url )
 i1iIi = re . compile ( 'url: "([^"]*)",' , re . DOTALL ) . findall ( OOOOO0oo0O0O0 )
 o0OO0o0o00o = re . compile ( "src='([^']*)' type='([^']*)' />" , re . DOTALL ) . findall ( OOOOO0oo0O0O0 )
 for url in i1iIi :
  if 'http' in url :
   IiI1iiiIii ( 'video/flv' , url , 222 , oOOoO0 + 'disclose.png' )
 for url , ooOOoooooo in o0OO0o0o00o :
  IiI1iiiIii ( ooOOoooooo , url , 222 , oOOoO0 + 'disclose.png' )
  if 16 - 16: OOooOOo . o0000oOoOoO0o
  if 50 - 50: o0oO0 * I1IiI + ii11ii1ii - i11iIiiIii + Oo * ii11ii1ii
def i11II ( url ) :
 OOOOO0oo0O0O0 = IIiIi1iI ( url )
 i1iIi = re . compile ( '<div id="play-1".+?src="(.+?)" scrolling="no".+?<li><a href="#play-1">(.+?)</a></li>' , re . DOTALL ) . findall ( OOOOO0oo0O0O0 )
 for url , ooOOoooooo in i1iIi :
  O0OO0O ( ooOOoooooo , ( url + '&fv=&sou=' ) . replace ( 'player' , 'watch' ) , 7000 , oOOoO0 + 'icon.png' )
  if 69 - 69: O0oO - i1IIi % oO0o0ooO0 . OoOO0ooOOoo0O - OoOO0ooOOoo0O
def o0oO00o ( name , url , img ) :
 iiI = IIiIi1iI ( url )
 OOO0OoO0oo0OO = re . compile ( '<iframe class="playerframe" src="(.+?)" scrolling=".+?" marginwidth=".+?" marginheight=".+?" vspace=".+?" hspace=".+?" allowfullscreen=".+?" webkitallowfullscreen=".+?" mozallowfullscreen=".+?" width=".+?" height=".+?" frameborder=".+?"></iframe>' , re . DOTALL ) . findall ( iiI )
 i1iI1Ii11Ii1 = len ( OOO0OoO0oo0OO )
 if 82 - 82: O0
 if 70 - 70: o0000oOoOoO0o - Oo / OoooooooOO % OoooooooOO
 if i1iI1Ii11Ii1 == 1 :
  for oooo0o0OOO0 in OOO0OoO0oo0OO :
   oooo0o0OOO0 = oooo0o0OOO0 . replace ( 'player' , 'watch' )
   iiIII1 = oooo0o0OOO0 + '&fv=&sou='
   iiI1iIiI111 = IIiIi1iI ( iiIII1 )
   iI1111I = re . compile ( '<source src="(.+?)" type=".+?">' , re . DOTALL ) . findall ( iiI1iIiI111 )
   for o0O0OO in iI1111I :
    iiiI11 = False
    Resolve ( o0O0OO )
    if 89 - 89: OoOO
 elif i1iI1Ii11Ii1 > 1 :
  if 87 - 87: oO0o0ooO0 % Oo
  for oooo0o0OOO0 in OOO0OoO0oo0OO :
   OOo000o = IIiIi1iI ( oooo0o0OOO0 )
   iiIIIIiI111 = re . compile ( '<iframe width=".*?" height=".*?" frameborder=".*?" src="(.*?)" scrolling=".*?" marginwidth=".*?" marginheight=".*?" vspace=".*?" hspace=".*?" allowfullscreen=".*?" webkitallowfullscreen=".*?" mozallowfullscreen=".*?"></iframe>' , re . DOTALL ) . findall ( OOo000o )
   OoooOO0Oo0 = iiIIIIiI111
   OoooOO0Oo0 = ( str ( OoooOO0Oo0 ) ) . replace ( '[\'' , '' ) . replace ( '\']' , '' ) ;
   print 'Stripped url : ' + OoooOO0Oo0
   IiI1iiiIii ( 'DOUBLE LINK' , OoooOO0Oo0 , 424 , '' )
   if 31 - 31: IIII - Ooo00oOo00o / OoOO0ooOOoo0O . i1IIi / o00O0oo
   for url in iiIIIIiI111 :
    O0OO0O ( 'DOUBLE LINK' , url , 424 , '' )
    try :
     O0o0OO0000ooo = Google . resolve ( url )
    except :
     pass
    try :
     o0o000o = re . findall ( r"{'url': u'(.*?)', 'quality': 'HD'}, {'url': u'(.*?)', 'quality': 'SD'}" , str ( O0o0OO0000ooo ) )
     for iiiI1i1111II , IIII11iiii in o0o000o :
      if 75 - 75: iIii1I11I1II1 % IIII + ii11ii1ii * O0 . oO0o0ooO0 - o0oO0
      HD_URLS . append ( iiiI1i1111II )
      SD_URLS . append ( IIII11iiii )
    except :
     pass
 else :
  pass
  if 32 - 32: o00O0oo % OoOO - i1IIi
def Ii11III ( ) :
 if 15 - 15: o0000oOoOoO0o % OOOo0 - iIii1I11I1II1 * o0oO0
 if 71 - 71: I1IiI % Oo % o0oO0
 O0OO0O ( 'Genres' , 'http://cnfstudio.com/movies/' , 7002 , oOOoO0 + 'Movies.png' )
 if 34 - 34: o0000oOoOoO0o / o0000oOoOoO0o % IIII . I1IiI / Oo
 O0OO0O ( 'Search Movies' , '' , 7017 , oOOoO0 + 'Movies.png' )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 99 - 99: o0oO0 * OOOo0 - o0oO0 % o00O0oo
 if 40 - 40: OoOO0ooOOoo0O / IIII / iIii1I11I1II1 + o00O0oo
def O0Ooo0ooo00o ( ) :
 OOOOO0oo0O0O0 = IIiIi1iI ( 'http://cnfstudio.com/' )
 i1iIi = re . compile ( '<a href="http://cnfstudio.com/genre/(.+?)">(.+?)</a>' ) . findall ( OOOOO0oo0O0O0 )
 for I1Ii1iI1 , ooOOoooooo in i1iIi :
  O0OO0O ( ooOOoooooo , 'http://cnfstudio.com/genre/' + I1Ii1iI1 , 7003 , oOOoO0 + 'icon.png' )
  if 73 - 73: o0oO0 % o0oO0 . oO0o0ooO0 + O0oO
ii11iIi1I = xbmcgui . Dialog ( )
if 10 - 10: O0 / OoOO0ooOOoo0O * o0oO0 - Ooo00oOo00o - i1IIi . I1IiI
if 69 - 69: Oo - o00O0oo % o00O0oo - OoOO0ooOOoo0O * OoOO0ooOOoo0O / Oo
def i1IiIIi ( url ) :
 OOOOO0oo0O0O0 = IIiIi1iI ( url )
 i1iIi = re . compile ( '<div class="movie">.+?<img src="(.+?)" alt=".+?" />.+?<a href="(.+?)"><span class="player"></span></a>.+?<h2>(.+?)</h2>' , re . DOTALL ) . findall ( OOOOO0oo0O0O0 )
 OOOO = re . compile ( "<link rel='next' href='(.+?)'/>" ) . findall ( OOOOO0oo0O0O0 )
 for oOo0 , url , ooOOoooooo in i1iIi :
  IiI1iiiIii ( ( ooOOoooooo ) . replace ( '&#038;' , '' ) . replace ( '&#8216;' , '' ) . replace ( '&#8217;' , '' ) . replace ( '&#8211;' , '' ) , url , 7004 , oOo0 )
 OOOO = OOOO
 for url in OOOO :
  O0OO0O ( 'Next Page' , url , 7003 , '' )
  if 58 - 58: O0
def O0oOOOO00o0 ( url ) :
 if 97 - 97: ii11ii1ii / ii11ii1ii / iIii1I11I1II1 % i1IIi . ii11ii1ii . IIII
 OOOOO0oo0O0O0 = IIiIi1iI ( url )
 i1iIi = re . compile ( '<div id="play-1" class="player-content"><iframe class="playerframe" src="(.+?)" scrolling="no".+?</div>' , re . DOTALL ) . findall ( OOOOO0oo0O0O0 )
 for url in i1iIi :
  OOOo00oo0oO = url + '&fv=&sou='
  OOOo00oo0oO = OOOo00oo0oO . replace ( 'player' , 'watch' )
  IIII1ii1 = OOO0O0OOo ( OOOo00oo0oO )
  Iii1 = OOO0O0OOo ( url )
  if 96 - 96: Oo / OoOO . OoOoOO00 . Oo
  if 91 - 91: OoOoOO00 . OoOO0ooOOoo0O + OOooOOo
def OOO0O0OOo ( url ) :
 if 8 - 8: OoOO0ooOOoo0O * Oo / oO0o0ooO0 - Ooo00oOo00o - OoooooooOO
 OOOOO0oo0O0O0 = IIiIi1iI ( url )
 i1iIi = re . compile ( '<video id=".+?<source src="(.+?)" type="video/mp4">' , re . DOTALL ) . findall ( OOOOO0oo0O0O0 )
 for url in i1iIi :
  oOiIi ( url )
  if 65 - 65: OoOoOO00 + i1IIi * i11iIiiIii
  if 38 - 38: iIii1I11I1II1 + OoooooooOO * OOOo0 % I1IiI % o0000oOoOoO0o - IIII
def Oo0OO00OO0Oo ( ) :
 ooooooO0oo ( '[COLORgreen]Local M3u[/COLOR]' , i1iiIIiiI111 , 2001 , oOOoO0 + 'loader.png' , OOooO0OOoo , '' )
 ooooooO0oo ( '[COLORgreen]Remote M3u[/COLOR]' , oO , 1009 , oOOoO0 + 'loader.png' , OOooO0OOoo , '' )
 if 1 - 1: iIii1I11I1II1 . o0000oOoOoO0o + o0000oOoOoO0o . o0oO0
def o0o00OoO0 ( url ) :
 i1iIi = re . compile ( '^#EXTINF:-?[0-9]*(.*?),(.*?)\n(.*?)$' , re . I + re . M + re . U + re . S ) . findall
 for O00Oo , ooOOoooooo , url in i1iIi :
  IiI1iiiIii ( ooOOoooooo , url , 222 , oOOoO0 + 'streams.png' )
  if 10 - 10: o0000oOoOoO0o
  if 95 - 95: O0
def O00OO0O ( ) :
 ooooooO0oo ( '[COLORgreen]CATAGORIES[/COLOR]' , '' , 10051 , oOOoO0 + 'loader.png' , OOooO0OOoo , '' )
 ooooooO0oo ( '[COLORgreen]SEARCH[/COLOR]' , '' , 10052 , oOOoO0 + 'loader.png' , OOooO0OOoo , '' )
 if 52 - 52: OoOO0ooOOoo0O * OoOO + o0000oOoOoO0o * o0000oOoOoO0o % i1IIi % o0000oOoOoO0o
 if 96 - 96: OOooOOo * OoOO - OoOO0ooOOoo0O * OOooOOo * i1IIi
o0oOoO00o = xbmcaddon . Addon ( id = 'plugin.video.GenieTv' )
Oo0o0000o0o0 = xbmcgui . Dialog ( )
iI111I11I1I1 = xbmc . translatePath ( 'special://home/' )
i1111 = xbmcgui . DialogProgress ( )
I1IIIi1i = 'https://addons.tvaddons.ag/'
if 54 - 54: OoOoOO00 . i1IIi / ii11ii1ii % OOOo0 / O0oO
def OOoOoOo0 ( ) :
 o00o0 = Oo0o0000o0o0 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 II1III1I1I1Ii = o00o0 . lower ( )
 ooOOooo0ooo00 = 'https://addons.tvaddons.ag/search/?keyword=' + II1III1I1I1Ii
 iiI = IIiIi1iI ( ooOOooo0ooo00 )
 i1iIi = re . compile ( '<li><a href="(.+?)"><span class=".+?"><img src="(.+?)" width=".+?" alt=".+?" class=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( iiI )
 for I1Ii1iI1 , oO0 , ooOOoooooo in i1iIi :
  ooooooO0oo ( ooOOoooooo , I1Ii1iI1 , 10054 , 'https://addons.tvaddons.ag/' + oO0 , OOooO0OOoo , '' )
  if 19 - 19: I1IiI . OOooOOo . OoooooooOO
  if 13 - 13: OoOO0ooOOoo0O . Oo / OoOoOO00
def iiI1iIII1ii ( ) :
 iiI = IIiIi1iI ( I1IIIi1i )
 i1iIi = re . compile ( '<li><a href="(.+?)"><span class="thumbnail"><img src="(.+?)" class="pic" alt=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( iiI )
 for I1Ii1iI1 , oOo0 , ooOOoooooo in i1iIi :
  if 'Repositories' in ooOOoooooo :
   pass
  elif 'Services' in ooOOoooooo :
   pass
  elif 'International' in ooOOoooooo :
   pass
  else :
   ooooooO0oo ( '[COLORgreen]' + ooOOoooooo + '[/COLOR]' , I1Ii1iI1 , 10053 , 'https://addons.tvaddons.ag/' + oOo0 , OOooO0OOoo , '' )
   if 5 - 5: O0oO % OoooooooOO . I1IiI
   if 67 - 67: ii11ii1ii + o00O0oo
def Addon ( url ) :
 iiI = IIiIi1iI ( url )
 o0O00OooooO = re . compile ( '<li class="nextPage"><a class=".+?" href="(.+?)"><dfn title="next Page">.+?</dfn></a></li>' ) . findall ( iiI )
 for url in o0O00OooooO :
  ooooooO0oo ( '[COLORgreen]NEXT PAGE[/COLOR]' , 'https://addons.tvaddons.ag' + url , 10053 , oOOoO0 + 'streams.png' , OOooO0OOoo , '' )
 i1iIi = re . compile ( '<li><a href="(.+?)"><span class=".+?"><img src="(.+?)" width=".+?" alt=".+?" class=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( iiI )
 for url , oOo0 , ooOOoooooo in i1iIi :
  if 'Please' in ooOOoooooo :
   pass
  else :
   ooooooO0oo ( ooOOoooooo , url , 10054 , 'https://addons.tvaddons.ag/' + oOo0 , OOooO0OOoo , '' )
   if 77 - 77: OOOo0 % o0oO0
   if 74 - 74: I1IiI / i1IIi % OoooooooOO
def o00o0o000Oo ( url , name ) :
 iiI = IIiIi1iI ( url )
 i1iIi = re . compile ( '<a href="(.+?)"' ) . findall ( iiI )
 for url in i1iIi :
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
   if 100 - 100: i1IIi - i11iIiiIii . O0oO * Ooo00oOo00o
def OO0O0 ( ) :
 xbmc . executebuiltin ( 'UpdateLocalAddons' )
 xbmc . executebuiltin ( 'UpdateAddonRepos' )
 ii11iIi1I = xbmcgui . Dialog ( )
 ii11iIi1I . ok ( "Origin + Genie TV" , '' , '                                 REFRESH SUCCESSFUL :)' , "                          [COLOR gold]Brought To You By Origin + Jaybox[/COLOR]" )
 return
 if 62 - 62: O0
 if 41 - 41: i1IIi - OOOo0
def IiiiIIiii ( ) :
 OOOOO0oo0O0O0 = oOoO0O0o0Oooo ( oOo0oooo00o ( 'aHR0cDovL3Njb29ieXN0cmVhbS54MTBob3N0LmNvbS9zY29vYnkvc2NyYXBlZC9jYXRzLnBocA==' ) )
 i1iIi = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( OOOOO0oo0O0O0 )
 for I1Ii1iI1 , oO0 , ooOOoooooo in i1iIi :
  O0OO0O ( ooOOoooooo , I1Ii1iI1 , 1007 , oO0 )
def II1iIiiiI1 ( url ) :
 OOOOO0oo0O0O0 = oOoO0O0o0Oooo ( url )
 i1iIi = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( OOOOO0oo0O0O0 )
 for url , oO0 , ooOOoooooo in i1iIi :
  O0OO0O ( '[COLORgreen]' + ooOOoooooo + '[/COLOR]' , url , 1006 , oO0 )
  if 34 - 34: o00O0oo + Oo - i1IIi - IIII + iIii1I11I1II1
  if 75 - 75: ii11ii1ii
def O00o ( url ) :
 OOOOO0oo0O0O0 = oOoO0O0o0Oooo ( url )
 i1iIi = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( OOOOO0oo0O0O0 )
 for url , II1I , ii11ii11 , O0i1II1Iiii1I11 , ooOOoooooo in i1iIi :
  if '.php' in url :
   IiII1II11I ( ooOOoooooo , url , 1016 , II1I , O0i1II1Iiii1I11 , ii11ii11 )
   I1i1I1II ( 'tvshows' , 'Media Info 3' )
  else :
   i1i1IIiiIIi1I ( ooOOoooooo , url , 222 , II1I , O0i1II1Iiii1I11 , ii11ii11 )
   I1i1I1II ( 'tvshows' , 'Media Info 3' )
   if 55 - 55: o0oO0 % o0000oOoOoO0o / i11iIiiIii
 else :
  i1iIi = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( OOOOO0oo0O0O0 )
  for url , oO0 , ooOOoooooo in i1iIi :
   if '.php' in url :
    O0OO0O ( ooOOoooooo , url , 1016 , oO0 )
   else :
    IiI1iiiIii ( ooOOoooooo , url , 222 , oO0 )
    if 20 - 20: IIII / O0oO * IIII * Ooo00oOo00o
  xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 72 - 72: Ooo00oOo00o . OOooOOo * ii11ii1ii . iIii1I11I1II1 % ii11ii1ii . o00O0oo
def O000o0 ( ) :
 OOOOO0oo0O0O0 = oOoO0O0o0Oooo ( oOo0oooo00o ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vdm9kL3VybHMvdXJsLnBocA==' ) )
 i1iIi = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( OOOOO0oo0O0O0 )
 for I1Ii1iI1 , oO0 , ooOOoooooo in i1iIi :
  O0OO0O ( ooOOoooooo , I1Ii1iI1 , 1007 , oO0 )
def Iiiii1 ( url ) :
 OOOOO0oo0O0O0 = oOoO0O0o0Oooo ( url )
 i1iIi = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( OOOOO0oo0O0O0 )
 for url , oO0 , ooOOoooooo in i1iIi :
  O0OO0O ( '[COLORgreen]' + ooOOoooooo + '[/COLOR]' , url , 1006 , oO0 )
  if 88 - 88: o0000oOoOoO0o + OOOo0 - o0000oOoOoO0o / OoooooooOO - i11iIiiIii
def i11Ii1IiIIIi ( name , url , iconimage = None ) :
 print '--- Playing "{0}". {1}' . format ( name , url )
 OOOoo00o0o = xbmcgui . ListItem ( path = url , thumbnailImage = iconimage )
 OOOoo00o0o . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , OOOoo00o0o )
 if 98 - 98: o00O0oo * iIii1I11I1II1 % Oo % OoOO0ooOOoo0O
 if 88 - 88: oO0o0ooO0 - OoOoOO00 / oO0o0ooO0 - o00O0oo
def iI1iii1iI1 ( url ) :
 OOOOO0oo0O0O0 = oOoO0O0o0Oooo ( url )
 i1iIi = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( OOOOO0oo0O0O0 )
 for url , oOo0 , ooOOoooooo in i1iIi :
  O0OO0O ( '[COLORgreen]' + ooOOoooooo + '[/COLOR]' , url , 1006 , oOo0 )
def ooO ( url ) :
 OOOOO0oo0O0O0 = oOoO0O0o0Oooo ( url )
 oo0OoOOooO = url
 i1iIi = re . compile ( "<a href='(.+?)'>(.+?)</a>" ) . findall ( OOOOO0oo0O0O0 )
 for url , ooOOoooooo in i1iIi :
  if '.mp3' in ooOOoooooo :
   print '<<<<<<<<<<<<<<<<<<<' + url + '>>>>>>>>>>>>>>>>>>>>>>>>>>>'
   IiI1iiiIii ( ( ooOOoooooo ) . replace ( '.mp3' , '' ) . replace ( '/' , '' ) , 'http://hypem.com' + url , 222 , oOOoO0 + 'music.png' )
  else :
   O0OO0O ( ( ooOOoooooo ) . replace ( '/' , '' ) , oo0OoOOooO + url , 1011 , oOOoO0 + 'music.png' )
def ooOO0 ( ) :
 OOOOO0oo0O0O0 = oOoO0O0o0Oooo ( oOo0oooo00o ( 'aHR0cDovL3d3dy5jeW4ubmV0L211c2ljLw==' ) )
 i1iIi = re . compile ( '<td><a href="(.+?)"><img src="(.+?)"><br>(.+?)</a></td>' , re . DOTALL ) . findall ( OOOOO0oo0O0O0 )
 for I1Ii1iI1 , oOo0 , ooOOoooooo in i1iIi :
  O0OO0O ( ooOOoooooo , ( 'http://www.cyn.net/music/' + I1Ii1iI1 ) . replace ( ' ' , '%20' ) , 1031 , ( 'http://www.cyn.net/music/' + oOo0 ) . replace ( ' ' , '%20' ) )
def Oo00Oo ( url , img ) :
 OOOOO0oo0O0O0 = oOoO0O0o0Oooo ( url )
 O0o0OO0000ooo = url
 img = img
 i1iIi = re . compile ( '<a href="(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( OOOOO0oo0O0O0 )
 for url , ooOOoooooo in i1iIi :
  IiI1iiiIii ( ( ooOOoooooo ) . replace ( '.mp3' , '' ) , ( O0o0OO0000ooo + '/' + url ) . replace ( ' ' , '%20' ) , 222 , img )
  if 25 - 25: iIii1I11I1II1
  if 63 - 63: o0oO0
def oO0oOOOooo ( ) :
 oOO0ooOo00O0OO = ( oOo0oooo00o ( 'aHR0cDovL2h5cGVtLmNvbS9kb3dubG9hZC8=' ) )
 o00o0 = Oo0o0000o0o0 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 II1III1I1I1Ii = o00o0 . lower ( )
 I1Ii1iI1 = ( oOo0oooo00o ( 'aHR0cDovL3Bhbmljc3RyZWFtLm5ldC9zdHJlYW1zLw==' ) )
 O0o0OO0000ooo = ( oOo0oooo00o ( 'aHR0cDovL21hc2xvdmQubm8taXAub3JnL3B1YmxpYy9tcDMv' ) )
 oOOOoo0o = ( oOo0oooo00o ( 'aHR0cDovL3d3dy5jeW4ubmV0L211c2ljLw==' ) )
 if 6 - 6: iIii1I11I1II1 - iIii1I11I1II1 % OOooOOo / iIii1I11I1II1 * O0oO
 iiI = oO0OOO0o0O ( I1Ii1iI1 )
 II1iIi1IiIii = oO0OOO0o0O ( O0o0OO0000ooo )
 O00o0O = oO0OOO0o0O ( oOOOoo0o )
 if 3 - 3: OoOO0ooOOoo0O . IIII / Oo
 if iiI != 'Failed' :
  i1iIi = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( iiI )
  for ooOOoooooo in i1iIi :
   if o00o0 in ooOOoooooo . lower ( ) :
    O0OO0O ( ( ooOOoooooo + ' source 1' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( I1Ii1iI1 + ooOOoooooo ) . replace ( ' ' , '%20' ) , 1006 , '' )
    if 89 - 89: OoooooooOO . iIii1I11I1II1 . Oo * iIii1I11I1II1 - O0oO
    I1i1I1II ( 'tvshows' , 'Media Info 3' )
 if II1iIi1IiIii != 'Failed' :
  o0OO0o0o00o = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( iiI )
  for ooOOoooooo in o0OO0o0o00o :
   if o00o0 in ooOOoooooo . lower ( ) :
    O0OO0O ( ( ooOOoooooo + ' source 2' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( O0o0OO0000ooo + ooOOoooooo ) . replace ( ' ' , '%20' ) , 1006 , '' )
    if 92 - 92: OoooooooOO - ii11ii1ii - OoooooooOO % OOOo0 % OOOo0 % iIii1I11I1II1
    I1i1I1II ( 'tvshows' , 'Media Info 3' )
 if O00o0O != 'Failed' :
  iIII = re . compile ( '<td><a href=".+?"><img src=".+?"><br>(.+?)</a></td>' , re . DOTALL ) . findall ( O00o0O )
  for ooOOoooooo in iIII :
   if o00o0 in ooOOoooooo . lower ( ) :
    O0OO0O ( ( ooOOoooooo + ' source 3' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( oOOOoo0o + ooOOoooooo ) . replace ( ' ' , '%20' ) , 1031 , '' )
    if 92 - 92: oO0o0ooO0 * O0 % O0oO . iIii1I11I1II1
    I1i1I1II ( 'tvshows' , 'Media Info 3' )
    if 66 - 66: o0000oOoOoO0o + o00O0oo
    if 48 - 48: ii11ii1ii
    if 96 - 96: o0oO0 . OoooooooOO
    if 39 - 39: OoOO0ooOOoo0O + Ooo00oOo00o
    if 80 - 80: OoOO0ooOOoo0O % Ooo00oOo00o / I1IiI
    if 54 - 54: Oo % Ooo00oOo00o - OoOO0ooOOoo0O - o0000oOoOoO0o
def o0I1iI111ii111i ( ) :
 OOOOO0oo0O0O0 = IIiIi1iI ( 'http://www.animetoon.org/cartoon' )
 i1iIi = re . compile ( '<td><a href="(.+?)">(.+)</a></td>' ) . findall ( OOOOO0oo0O0O0 )
 for I1Ii1iI1 , ooOOoooooo in i1iIi :
  O0OO0O ( ooOOoooooo , I1Ii1iI1 , 1002 , oOOoO0 + 'anime.png' )
  if 83 - 83: iIii1I11I1II1
  if 97 - 97: i11iIiiIii + Oo * OoOO0ooOOoo0O % oO0o0ooO0 . IIII
  if 4 - 4: O0 . oO0o0ooO0 - iIii1I11I1II1
def I1iII11ii1 ( url ) :
 OOOOO0oo0O0O0 = IIiIi1iI ( url )
 o0OO0o0o00o = re . compile ( '<img src="(.+?)" id="series_image" width="250" height="370" alt=".+?" />' ) . findall ( OOOOO0oo0O0O0 )
 for oOo0 in o0OO0o0o00o :
  iIIIiiI1i1i = oOo0
 iIII = re . compile ( '<li><a href="(.+?)">Next</a></li>' ) . findall ( OOOOO0oo0O0O0 )
 for url in iIII :
  O0OO0O ( 'NEXT PAGE' , url , 1002 , iIIIiiI1i1i )
 i1iIi = re . compile ( '&nbsp;<a href="(.+?)">(.+?)</a>' ) . findall ( OOOOO0oo0O0O0 )
 for url , ooOOoooooo in i1iIi :
  O0OO0O ( ooOOoooooo , url , 1003 , iIIIiiI1i1i )
 xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
def Ii111I11 ( url , IMAGE ) :
 OOOOO0oo0O0O0 = IIiIi1iI ( url )
 i1iIi = re . compile ( '"playlist">(.+?)</span></div><div><iframe src="(.+?)"' ) . findall ( OOOOO0oo0O0O0 )
 for ooOOoooooo , url in i1iIi :
  print ooOOoooooo + '     ' + url
  if 'easy' in url :
   Oo0O0oo ( url )
  elif 'playpanda' in url :
   Oo0O0oo ( url )
   if 62 - 62: o0000oOoOoO0o / ii11ii1ii
  xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
def Oo0O0oo ( url ) :
 OOOOO0oo0O0O0 = IIiIi1iI ( url )
 i1iIi = re . compile ( "url: '(.+?)'," ) . findall ( OOOOO0oo0O0O0 )
 for url in i1iIi :
  IiI1iiiIii ( 'STREAM' , url , 222 , oOOoO0 + 'anime.png' )
  if 85 - 85: OOOo0 + oO0o0ooO0 - oO0o0ooO0 . OoooooooOO - iIii1I11I1II1
  if 8 - 8: i11iIiiIii * OOooOOo / ii11ii1ii . o00O0oo
def Iii1II1ii ( url ) :
 OOOOO0 = urllib2 . Request ( url )
 OOOOO0 . add_header ( 'User-Agent' , "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0" )
 OOOOO0 . add_header ( 'referer' , url )
 Ooo0Oo0o = urllib2 . urlopen ( OOOOO0 )
 OOOo00oo0oO = Ooo0Oo0o . read ( )
 Ooo0Oo0o . close ( )
 return OOOo00oo0oO
 if 95 - 95: Oo
def oOoO0O0o0Oooo ( url ) :
 OOOOO0 = urllib2 . Request ( url )
 OOOOO0 . add_header ( 'User-Agent' , "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0" )
 Ooo0Oo0o = urllib2 . urlopen ( OOOOO0 )
 OOOo00oo0oO = Ooo0Oo0o . read ( )
 Ooo0Oo0o . close ( )
 return OOOo00oo0oO
 if 29 - 29: o00O0oo / o0oO0 % o0000oOoOoO0o
def ii1iIII1ii ( url ) :
 xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
 I1Ii = ( '%s%s' % ( oOOIi1II , url ) )
 OOOo00oo0oO = oOoO0O0o0Oooo ( url )
 i1iIi = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( OOOo00oo0oO )
 for url , oO0 , ooOOoooooo in i1iIi :
  IiI1iiiIii ( '%s' % ( ooOOoooooo ) . replace ( 'GenieTv' , '[COLOR green]GenieTV[/COLOR]' ) . replace ( '.' , ' ' ) . replace ( 'mp4' , '' ) . replace ( 'mkv' , '' ) . replace ( '_' , ' ' ) , '%s' % ( url ) , 222 , oO0 )
  if 47 - 47: o0000oOoOoO0o . oO0o0ooO0 * o00O0oo - o0oO0 . o0000oOoOoO0o - OoOO0ooOOoo0O
def oOiIi ( url ) :
 iiiii11I1 = xbmc . Player ( Ii1OOOo ( ) )
 import urlresolver
 try : iiiii11I1 . play ( url )
 except : pass
 from urlresolver import common
 i1111 = xbmcgui . DialogProgress ( )
 i1111 . create ( 'LOADING' , 'Opening %s Now' % ( ooOOoooooo ) )
 iiiii11I1 = xbmc . Player ( Ii1OOOo ( ) )
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
 iiiii11I1 = xbmc . Player ( Ii1OOOo ( ) )
 import urlresolver
 try : iiiii11I1 . play ( url )
 except : pass
 if 90 - 90: i1IIi + O0 - OoOO . oO0o0ooO0 + iIii1I11I1II1
 if 88 - 88: o00O0oo * O0 . O0oO / OoooooooOO
def Ii1OOOo ( ) :
 try :
  ii1 = getSet ( "core-player" )
  if ( ii1 == 'DVDPLAYER' ) : i1Iii = xbmc . PLAYER_CORE_DVDPLAYER
  elif ( ii1 == 'MPLAYER' ) : i1Iii = xbmc . PLAYER_CORE_MPLAYER
  elif ( ii1 == 'PAPLAYER' ) : i1Iii = xbmc . PLAYER_CORE_PAPLAYER
  else : i1Iii = xbmc . PLAYER_CORE_AUTO
 except : i1Iii = xbmc . PLAYER_CORE_AUTO
 return i1Iii
 return True
 if 57 - 57: IIII
def O0OO0O ( name , url , mode , iconimage , showcontext = True , allinfo = { } ) :
 o0oO00 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 O0o = True
 oO00oO = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 oO00oO . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 if showcontext :
  IiI11I1Ii11II = [ ]
  if showcontext == 'fav' :
   IiI11I1Ii11II . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in o0 :
   IiI11I1Ii11II . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  oO00oO . addContextMenuItems ( IiI11I1Ii11II )
 O0o = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = o0oO00 , listitem = oO00oO , isFolder = True )
 return O0o
 if 75 - 75: i11iIiiIii % IIII
def i11i1I ( name , url , mode , iconimage , fanart , description ) :
 if 30 - 30: Oo
 o0oO00 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 O0o = True
 oO00oO = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 oO00oO . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 oO00oO . setProperty ( "Fanart_Image" , fanart )
 O0o = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = o0oO00 , listitem = oO00oO , isFolder = True )
 return O0o
 if 8 - 8: O0 + OoOO + O0oO
def IiI1iiiIii ( name , url , mode , iconimage , showcontext = True , allinfo = { } ) :
 o0oO00 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 O0o = True
 oO00oO = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 oO00oO . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 if showcontext :
  IiI11I1Ii11II = [ ]
  if showcontext == 'fav' :
   IiI11I1Ii11II . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in o0 :
   IiI11I1Ii11II . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  oO00oO . addContextMenuItems ( IiI11I1Ii11II )
 O0o = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = o0oO00 , listitem = oO00oO , isFolder = False )
 return O0o
 if 47 - 47: o0000oOoOoO0o
 if 92 - 92: OoooooooOO % OOOo0 / I1IiI * I1IiI % i11iIiiIii / OoooooooOO
 if 47 - 47: i11iIiiIii / Oo - Oo * Ooo00oOo00o
 if 48 - 48: IIII
 if 96 - 96: OoOO / O0 . OoOoOO00 + IIII % OOooOOo
 if 67 - 67: O0 % O0oO
def i11IiiI1Ii1 ( heading , announce ) :
 class III ( ) :
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
   try : i11i1 = open ( announce ) ; I1I = i11i1 . read ( )
   except : I1I = announce
   self . win . getControl ( self . CONTROL_TEXTBOX ) . setText ( str ( I1I ) )
   return
 III ( )
 III ( )
 if 70 - 70: o00O0oo . O0 - OoOO0ooOOoo0O
def o000ooOo0o0OO ( ) :
 i11IiiI1Ii1 ( 'These are the main Sources you should get into you XBMC' , '[COLORwhite]http://architects.x10host.com[/COLOR]--- [CR]  [COLORred]http://repo.sharktech.co.uk[/COLOR]--- [CR]   [COLORwhite]http://fusion.tvaddons.ag[/COLOR]--- [CR]  [COLORred]http://i.totalxbmc.tv[/COLOR]--- [CR]   [COLORwhite]http://www.xunitytalk.com/xfinity[/COLOR]--- [CR]  [COLORred]http://srp.nu[/COLOR]--- [CR]   [COLORwhite]http://solved.no-issue.ca[/COLOR]--- [CR]  [COLORred]http://xbmc.aminhacasadigital.com[/COLOR]--- [CR]   [COLORwhite]http://xbmc.movieshd.co[/COLOR]--- [CR]  [COLORred]http://install.kaosbox.tv[/COLOR]--- [CR]   [COLORwhite]http://kodi-repo.com/mxr[/COLOR]--- [CR]  [COLORred]http://kodi.metalkettle.co[/COLOR]--- [CR]   [COLORwhite]http://prozone.getxbmc.com[/COLOR]--- [CR]  [COLORred]http://transform.mega-tron.tv[/COLOR]--- [CR]   [COLORwhite]http://muckys.kodimediaportal.ml[/COLOR]--- [CR]  [COLORred]http://jas0npc.pcriot.com[/COLOR]--- [CR]  [COLORwhite]Sports devil source[/COLOR]--- [CR]  [COLORred]http://iwillfolo.com/iwf[/COLOR]' )
 if 1 - 1: iIii1I11I1II1 % o0oO0 + O0
 if 22 - 22: OOooOOo + Oo . o0oO0 + ii11ii1ii * oO0o0ooO0 . i11iIiiIii
 if 90 - 90: OoOO0ooOOoo0O * I1IiI - Oo + OOooOOo
 if 53 - 53: OoooooooOO . OoooooooOO + OOooOOo - oO0o0ooO0 + OoOO0ooOOoo0O
 if 44 - 44: O0oO - IIII
def OO0O0 ( ) :
 xbmc . executebuiltin ( 'UpdateLocalAddons' )
 xbmc . executebuiltin ( 'UpdateAddonRepos' )
 ii11iIi1I = xbmcgui . Dialog ( )
 ii11iIi1I . ok ( "GenieTv" , '' , '                                 REFRESH SUCCESSFUL :)' , "                          [COLOR gold]Brought To You By Kodi Support Group, GenieTv[/COLOR]" )
 return
 if 100 - 100: OoOO . Ooo00oOo00o - o00O0oo + O0 * Ooo00oOo00o
 if 59 - 59: OoOoOO00
 if 43 - 43: Oo + OoooooooOO
 if 47 - 47: o0oO0
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
def Ii1I1Iiii ( url ) :
 OOOo00oo0oO = IIiIi1iI ( OO0o + oOIii ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1iIi = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( OOOo00oo0oO )
 for ooOOoooooo , url , II1I , O0i1II1Iiii1I11 , IIIIiiIiI in i1iIi :
  ooooooO0oo ( ooOOoooooo , url , 42 , II1I , O0i1II1Iiii1I11 , IIIIiiIiI )
 I1i1I1II ( 'movies' , 'MAIN' )
 if 33 - 33: IIII % Oo - OoOO
def oO00o ( url ) :
 OOOo00oo0oO = IIiIi1iI ( OO0o + oooo0O0Oooo ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1iIi = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( OOOo00oo0oO )
 for ooOOoooooo , url , II1I , O0i1II1Iiii1I11 , IIIIiiIiI in i1iIi :
  ooooooO0oo ( ooOOoooooo , url , 42 , II1I , O0i1II1Iiii1I11 , IIIIiiIiI )
 I1i1I1II ( 'movies' , 'MAIN' )
 if 39 - 39: OoOO / o0oO0 * OoOoOO00 * oO0o0ooO0
def IiIii11i1IIiI ( url ) :
 OOOo00oo0oO = IIiIi1iI ( OO0o + I11iIIi ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1iIi = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( OOOo00oo0oO )
 for ooOOoooooo , url , II1I , O0i1II1Iiii1I11 , IIIIiiIiI in i1iIi :
  ooooooO0oo ( ooOOoooooo , url , 42 , II1I , O0i1II1Iiii1I11 , IIIIiiIiI )
 I1i1I1II ( 'movies' , 'MAIN' )
 if 5 - 5: iIii1I11I1II1
def Iii1I11 ( url ) :
 OOOo00oo0oO = IIiIi1iI ( OO0o + O0o0o ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1iIi = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( OOOo00oo0oO )
 for ooOOoooooo , url , II1I , O0i1II1Iiii1I11 , IIIIiiIiI in i1iIi :
  ooooooO0oo ( ooOOoooooo , url , 42 , II1I , O0i1II1Iiii1I11 , IIIIiiIiI )
 I1i1I1II ( 'movies' , 'MAIN' )
 if 33 - 33: OoOoOO00 % iIii1I11I1II1 / iIii1I11I1II1 + IIII
def OOOoOOO0o0ooo ( url ) :
 OOOo00oo0oO = IIiIi1iI ( OO0o + II1ii1iii1ii ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1iIi = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( OOOo00oo0oO )
 for ooOOoooooo , url , II1I , O0i1II1Iiii1I11 , IIIIiiIiI in i1iIi :
  ooooooO0oo ( ooOOoooooo , url , 42 , II1I , O0i1II1Iiii1I11 , IIIIiiIiI )
 I1i1I1II ( 'movies' , 'MAIN' )
 if 21 - 21: IIII - OOOo0 % OoooooooOO + OOooOOo
def o00O0o ( url ) :
 OOOo00oo0oO = IIiIi1iI ( OO0o + i1Ii1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1iIi = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( OOOo00oo0oO )
 for ooOOoooooo , url , II1I , O0i1II1Iiii1I11 , IIIIiiIiI in i1iIi :
  ooooooO0oo ( ooOOoooooo , url , 42 , II1I , O0i1II1Iiii1I11 , IIIIiiIiI )
 I1i1I1II ( 'movies' , 'MAIN' )
 if 75 - 75: OoooooooOO * i11iIiiIii
def o0oOo ( url ) :
 OOOo00oo0oO = IIiIi1iI ( OO0o + OoIIiIIIII1I ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1iIi = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( OOOo00oo0oO )
 for ooOOoooooo , url , II1I , O0i1II1Iiii1I11 , IIIIiiIiI in i1iIi :
  ooooooO0oo ( ooOOoooooo , url , 42 , II1I , O0i1II1Iiii1I11 , IIIIiiIiI )
 I1i1I1II ( 'movies' , 'MAIN' )
 if 96 - 96: i11iIiiIii . OoOoOO00
def iI1I ( url ) :
 OOOo00oo0oO = IIiIi1iI ( OO0o + Iii1IiI1iI1I ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1iIi = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( OOOo00oo0oO )
 for ooOOoooooo , url , II1I , O0i1II1Iiii1I11 , IIIIiiIiI in i1iIi :
  ooooooO0oo ( ooOOoooooo , url , 42 , II1I , O0i1II1Iiii1I11 , IIIIiiIiI )
 I1i1I1II ( 'movies' , 'MAIN' )
 if 31 - 31: OOOo0 / OoooooooOO . iIii1I11I1II1 * I1IiI . OoooooooOO + OoOoOO00
def II1IIii1I11I ( url ) :
 OOOo00oo0oO = IIiIi1iI ( OO0o + ii1IiIIiI11111Ii ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1iIi = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( OOOo00oo0oO )
 for ooOOoooooo , url , II1I , O0i1II1Iiii1I11 , IIIIiiIiI in i1iIi :
  ooooooO0oo ( ooOOoooooo , url , 42 , II1I , O0i1II1Iiii1I11 , IIIIiiIiI )
 I1i1I1II ( 'movies' , 'MAIN' )
 if 69 - 69: o0oO0 . OoOO0ooOOoo0O * I1IiI . o0000oOoOoO0o / o0oO0
def I1I1 ( url ) :
 OOOo00oo0oO = IIiIi1iI ( OO0o + OO0Oo00OO0oo ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1iIi = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( OOOo00oo0oO )
 for ooOOoooooo , url , II1I , O0i1II1Iiii1I11 , IIIIiiIiI in i1iIi :
  ooooooO0oo ( ooOOoooooo , url , 5 , II1I , O0i1II1Iiii1I11 , IIIIiiIiI )
 I1i1I1II ( 'movies' , 'MAIN' )
 if 53 - 53: Ooo00oOo00o - o0oO0 + o00O0oo
 if 29 - 29: OoOO0ooOOoo0O + OoooooooOO + OoOO * OOOo0 - o00O0oo / i11iIiiIii
 if 5 - 5: O0 - OOOo0
 if 44 - 44: OoOoOO00 . OoOoOO00 + OoOO0ooOOoo0O * o00O0oo
 if 16 - 16: OoOoOO00
 if 100 - 100: O0 - i1IIi
 if 48 - 48: OoOO % o0oO0 + O0
 if 27 - 27: ii11ii1ii / OoOO0ooOOoo0O
 if 33 - 33: OoooooooOO % ii11ii1ii . O0 / ii11ii1ii
def O0OoOo ( ) :
 try :
  if os . path . exists ( OooO0 ) == True :
   ii11iIi1I = xbmcgui . Dialog ( )
   if ii11iIi1I . yesno ( "Delete Thumbnails" , "[COLOR gold][B]##########WARNING ANDROID ONLY##########[/B][/COLOR]" , "This feature deletes your thumbnail folder and textures13.db" , "Are you sure you want to do proceed? This Can NOT Be Undone" ) :
    for oOoO , oOoO00O0 , OOIi1iI111II1I1 in os . walk ( OooO0 ) :
     OOOOoO0 = 0
     OOOOoO0 += len ( OOIi1iI111II1I1 )
     if OOOOoO0 > 0 :
      for i11i1 in OOIi1iI111II1I1 :
       os . unlink ( os . path . join ( oOoO , i11i1 ) )
  IiiIiIIi1 = os . path . join ( II , "Textures13.db" )
  os . unlink ( IiiIiIIi1 )
  ii11iIi1I . ok ( "Restart KODI" , "Please restart KODI to rebuild thumbnail library" )
 except :
  ii11iIi1I = xbmcgui . Dialog ( )
  ii11iIi1I . ok ( i11 , "Error Deleting Thumbnails please visit Kodi Support Group, GenieTv on facebook" )
 return
 if 40 - 40: oO0o0ooO0 . I1IiI * O0
 if 6 - 6: OOOo0 - OoOoOO00 . OOOo0 + o0000oOoOoO0o . OoOO0ooOOoo0O
 if 74 - 74: i1IIi
 if 15 - 15: i1IIi + IIII % OOOo0 / i11iIiiIii * I1IiI
 if 69 - 69: i11iIiiIii
 if 61 - 61: O0
 if 21 - 21: Ooo00oOo00o % iIii1I11I1II1 . Ooo00oOo00o
 if 99 - 99: OOooOOo * OoOO0ooOOoo0O % OoOO * OoOO + OoooooooOO
 if 82 - 82: o0000oOoOoO0o / I1IiI - OoOO0ooOOoo0O / o0oO0
def I1iIIi ( url ) :
 print '############################################################       DELETING STANDARD CACHE             ###############################################################'
 Ii = os . path . join ( xbmc . translatePath ( 'special://home' ) , 'cache' )
 if os . path . exists ( Ii ) == True :
  for oOoO , oOoO00O0 , OOIi1iI111II1I1 in os . walk ( Ii ) :
   OOOOoO0 = 0
   OOOOoO0 += len ( OOIi1iI111II1I1 )
   if 65 - 65: i11iIiiIii - o0oO0 * o0000oOoOoO0o + o0oO0 / IIII + OOooOOo
   if 35 - 35: O0 + Oo - OOOo0 % o00O0oo % OoOoOO00
   if OOOOoO0 > 0 :
    if 77 - 77: O0oO + OoOO
    ii11iIi1I = xbmcgui . Dialog ( )
    if ii11iIi1I . yesno ( "Delete KODI Cache Files" , str ( OOOOoO0 ) + " files found" , "Do you want to delete them?" ) :
     if 38 - 38: ii11ii1ii - o00O0oo * OOooOOo
     for i11i1 in OOIi1iI111II1I1 :
      try :
       os . unlink ( os . path . join ( oOoO , i11i1 ) )
      except :
       pass
     for iIIIi1iii1I11 in oOoO00O0 :
      try :
       shutil . rmtree ( os . path . join ( oOoO , iIIIi1iii1I11 ) )
      except :
       pass
       if 81 - 81: IIII / IIII / Ooo00oOo00o % OoOO . iIii1I11I1II1
   else :
    pass
 if xbmc . getCondVisibility ( 'system.platform.ATV2' ) :
  oO00o0O0Ooo = os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'Other' )
  if 44 - 44: OoooooooOO / oO0o0ooO0
  for oOoO , oOoO00O0 , OOIi1iI111II1I1 in os . walk ( oO00o0O0Ooo ) :
   OOOOoO0 = 0
   OOOOoO0 += len ( OOIi1iI111II1I1 )
   if 81 - 81: OoOO - OoOO0ooOOoo0O
   if OOOOoO0 > 0 :
    if 21 - 21: Oo * OOooOOo + OoooooooOO . O0oO % OoOO
    ii11iIi1I = xbmcgui . Dialog ( )
    if ii11iIi1I . yesno ( "Delete ATV2 Cache Files" , str ( OOOOoO0 ) + " files found in 'Other'" , "Do you want to delete them?" ) :
     if 50 - 50: I1IiI - OoOO + iIii1I11I1II1 - Ooo00oOo00o . Oo
     for i11i1 in OOIi1iI111II1I1 :
      os . unlink ( os . path . join ( oOoO , i11i1 ) )
     for iIIIi1iii1I11 in oOoO00O0 :
      shutil . rmtree ( os . path . join ( oOoO , iIIIi1iii1I11 ) )
      if 8 - 8: o00O0oo
   else :
    pass
  iIii = os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'LocalAndRental' )
  if 95 - 95: o0000oOoOoO0o / IIII . O0 * IIII - OOooOOo * Oo
  for oOoO , oOoO00O0 , OOIi1iI111II1I1 in os . walk ( iIii ) :
   OOOOoO0 = 0
   OOOOoO0 += len ( OOIi1iI111II1I1 )
   if 6 - 6: I1IiI . OoOoOO00 * OOOo0 . OOOo0 / o00O0oo
   if OOOOoO0 > 0 :
    if 14 - 14: O0oO % IIII - O0 / O0oO
    ii11iIi1I = xbmcgui . Dialog ( )
    if ii11iIi1I . yesno ( "Delete ATV2 Cache Files" , str ( OOOOoO0 ) + " files found in 'LocalAndRental'" , "Do you want to delete them?" ) :
     if 91 - 91: i11iIiiIii % O0oO * OoOO - ii11ii1ii . O0oO
     for i11i1 in OOIi1iI111II1I1 :
      os . unlink ( os . path . join ( oOoO , i11i1 ) )
     for iIIIi1iii1I11 in oOoO00O0 :
      shutil . rmtree ( os . path . join ( oOoO , iIIIi1iii1I11 ) )
      if 28 - 28: i11iIiiIii
   else :
    pass
    if 51 - 51: OOOo0 + o0oO0 * O0 . o00O0oo
    if 82 - 82: OoOO0ooOOoo0O * ii11ii1ii % o00O0oo . OoOO0ooOOoo0O
    if 43 - 43: Ooo00oOo00o . o0oO0 * Oo
    if 20 - 20: i1IIi . i1IIi - o0000oOoOoO0o
 O0o00ooo = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.whatthefurk/cache' ) , '' )
 if os . path . exists ( O0o00ooo ) == True :
  for oOoO , oOoO00O0 , OOIi1iI111II1I1 in os . walk ( O0o00ooo ) :
   OOOOoO0 = 0
   OOOOoO0 += len ( OOIi1iI111II1I1 )
   if 5 - 5: i1IIi - OoOO / I1IiI
   if 13 - 13: OoOoOO00
   if OOOOoO0 > 0 :
    if 55 - 55: Oo % i1IIi * o0000oOoOoO0o
    ii11iIi1I = xbmcgui . Dialog ( )
    if ii11iIi1I . yesno ( "Delete WTF Cache Files" , str ( OOOOoO0 ) + " files found" , "Do you want to delete them?" ) :
     if 95 - 95: OoOO0ooOOoo0O / OoOoOO00 - OOooOOo % O0oO . o0000oOoOoO0o
     for i11i1 in OOIi1iI111II1I1 :
      os . unlink ( os . path . join ( oOoO , i11i1 ) )
     for iIIIi1iii1I11 in oOoO00O0 :
      shutil . rmtree ( os . path . join ( oOoO , iIIIi1iii1I11 ) )
      if 63 - 63: iIii1I11I1II1 / o0oO0
   else :
    pass
    if 24 - 24: Oo / iIii1I11I1II1 % OoOO0ooOOoo0O * I1IiI - iIii1I11I1II1
    if 50 - 50: OoOoOO00
 IiI = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.4od/cache' ) , '' )
 if os . path . exists ( IiI ) == True :
  for oOoO , oOoO00O0 , OOIi1iI111II1I1 in os . walk ( IiI ) :
   OOOOoO0 = 0
   OOOOoO0 += len ( OOIi1iI111II1I1 )
   if 50 - 50: i11iIiiIii + OoooooooOO / O0 + OOooOOo / i11iIiiIii + OoOO
   if 90 - 90: oO0o0ooO0 * o00O0oo - oO0o0ooO0 + Ooo00oOo00o + o0000oOoOoO0o % O0
   if OOOOoO0 > 0 :
    if 11 - 11: OoOO0ooOOoo0O % O0oO * I1IiI
    ii11iIi1I = xbmcgui . Dialog ( )
    if ii11iIi1I . yesno ( "Delete 4oD Cache Files" , str ( OOOOoO0 ) + " files found" , "Do you want to delete them?" ) :
     if 58 - 58: OoooooooOO - o0000oOoOoO0o + iIii1I11I1II1 * i11iIiiIii
     for i11i1 in OOIi1iI111II1I1 :
      os . unlink ( os . path . join ( oOoO , i11i1 ) )
     for iIIIi1iii1I11 in oOoO00O0 :
      shutil . rmtree ( os . path . join ( oOoO , iIIIi1iii1I11 ) )
      if 80 - 80: i1IIi . OOOo0 - OoOO + OoOO0ooOOoo0O + oO0o0ooO0 % OoOO
   else :
    pass
    if 13 - 13: OoOoOO00 / I1IiI / I1IiI + o0oO0
    if 49 - 49: O0 / OoOoOO00 * OOOo0 - OoooooooOO . OoOoOO00 % IIII
 IIii1Ii1i1ii1 = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.iplayer/iplayer_http_cache' ) , '' )
 if os . path . exists ( IIii1Ii1i1ii1 ) == True :
  for oOoO , oOoO00O0 , OOIi1iI111II1I1 in os . walk ( IIii1Ii1i1ii1 ) :
   OOOOoO0 = 0
   OOOOoO0 += len ( OOIi1iI111II1I1 )
   if 86 - 86: OoOO % O0 + Ooo00oOo00o
   if 52 - 52: Oo / oO0o0ooO0
   if OOOOoO0 > 0 :
    if 42 - 42: iIii1I11I1II1 * o00O0oo / Ooo00oOo00o + OoOO0ooOOoo0O
    ii11iIi1I = xbmcgui . Dialog ( )
    if ii11iIi1I . yesno ( "Delete BBC iPlayer Cache Files" , str ( OOOOoO0 ) + " files found" , "Do you want to delete them?" ) :
     if 48 - 48: OoooooooOO - O0oO . i11iIiiIii * oO0o0ooO0 - o00O0oo - OOooOOo
     for i11i1 in OOIi1iI111II1I1 :
      os . unlink ( os . path . join ( oOoO , i11i1 ) )
     for iIIIi1iii1I11 in oOoO00O0 :
      shutil . rmtree ( os . path . join ( oOoO , iIIIi1iii1I11 ) )
      if 59 - 59: oO0o0ooO0 / o0000oOoOoO0o . Oo
   else :
    pass
    if 100 - 100: O0
    if 94 - 94: ii11ii1ii - OOooOOo
    if 42 - 42: OOooOOo * I1IiI . Ooo00oOo00o - oO0o0ooO0 / OoOoOO00
 iII1ii11III = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/script.module.simple.downloader' ) , '' )
 if os . path . exists ( iII1ii11III ) == True :
  for oOoO , oOoO00O0 , OOIi1iI111II1I1 in os . walk ( iII1ii11III ) :
   OOOOoO0 = 0
   OOOOoO0 += len ( OOIi1iI111II1I1 )
   if 92 - 92: Ooo00oOo00o - ii11ii1ii + iIii1I11I1II1 % OOooOOo
   if 78 - 78: iIii1I11I1II1 - OoOoOO00 / OOOo0
   if OOOOoO0 > 0 :
    if 9 - 9: ii11ii1ii * o00O0oo - IIII
    ii11iIi1I = xbmcgui . Dialog ( )
    if ii11iIi1I . yesno ( "Delete Simple Downloader Cache Files" , str ( OOOOoO0 ) + " files found" , "Do you want to delete them?" ) :
     if 88 - 88: iIii1I11I1II1
     for i11i1 in OOIi1iI111II1I1 :
      os . unlink ( os . path . join ( oOoO , i11i1 ) )
     for iIIIi1iii1I11 in oOoO00O0 :
      shutil . rmtree ( os . path . join ( oOoO , iIIIi1iii1I11 ) )
      if 27 - 27: o0000oOoOoO0o * i11iIiiIii . OoOO0ooOOoo0O + o0oO0
   else :
    pass
    if 14 - 14: O0oO * Ooo00oOo00o + o0000oOoOoO0o - IIII . ii11ii1ii * OoOO
    if 100 - 100: o0000oOoOoO0o
 iI1iIi = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.itv/Images' ) , '' )
 if os . path . exists ( iI1iIi ) == True :
  for oOoO , oOoO00O0 , OOIi1iI111II1I1 in os . walk ( iI1iIi ) :
   OOOOoO0 = 0
   OOOOoO0 += len ( OOIi1iI111II1I1 )
   if 19 - 19: O0oO * IIII . Oo - Oo - Ooo00oOo00o
   if 51 - 51: O0 * OOOo0 / IIII - ii11ii1ii
   if OOOOoO0 > 0 :
    if 85 - 85: OOOo0 / iIii1I11I1II1 / oO0o0ooO0
    ii11iIi1I = xbmcgui . Dialog ( )
    if ii11iIi1I . yesno ( "Delete ITV Cache Files" , str ( OOOOoO0 ) + " files found" , "Do you want to delete them?" ) :
     if 74 - 74: OOooOOo / OoOO - OoOoOO00 . OoOoOO00 . IIII + OoOoOO00
     for i11i1 in OOIi1iI111II1I1 :
      os . unlink ( os . path . join ( oOoO , i11i1 ) )
     for iIIIi1iii1I11 in oOoO00O0 :
      shutil . rmtree ( os . path . join ( oOoO , iIIIi1iii1I11 ) )
      if 92 - 92: O0oO % iIii1I11I1II1 - oO0o0ooO0 / i11iIiiIii % o0oO0 * OOooOOo
   else :
    pass
    if 80 - 80: oO0o0ooO0
    if 3 - 3: ii11ii1ii * o0000oOoOoO0o
 Oo00O = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.movies4me/cache' ) , '' )
 if os . path . exists ( iI1iIi ) == True :
  for oOoO , oOoO00O0 , OOIi1iI111II1I1 in os . walk ( Oo00O ) :
   OOOOoO0 = 0
   OOOOoO0 += len ( OOIi1iI111II1I1 )
   if 44 - 44: o0oO0 * o0000oOoOoO0o
   if 12 - 12: o00O0oo . OOOo0 % OOooOOo
   if OOOOoO0 > 0 :
    if 28 - 28: o00O0oo - OOOo0 % Ooo00oOo00o * O0oO
    ii11iIi1I = xbmcgui . Dialog ( )
    if ii11iIi1I . yesno ( "Delete Movies4me Cache Files" , str ( OOOOoO0 ) + " files found" , "Do you want to delete them?" ) :
     if 80 - 80: OoOO0ooOOoo0O * IIII
     for i11i1 in OOIi1iI111II1I1 :
      os . unlink ( os . path . join ( oOoO , i11i1 ) )
     for iIIIi1iii1I11 in oOoO00O0 :
      shutil . rmtree ( os . path . join ( oOoO , iIIIi1iii1I11 ) )
      if 4 - 4: iIii1I11I1II1 . O0oO + OoOoOO00 % OoooooooOO
   else :
    pass
    if 82 - 82: OoooooooOO / o0oO0 * o0000oOoOoO0o * O0 . ii11ii1ii
    if 21 - 21: OoOoOO00 + Oo
 OOooooO = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.phstreams/Cache' ) , '' )
 if os . path . exists ( iI1iIi ) == True :
  for oOoO , oOoO00O0 , OOIi1iI111II1I1 in os . walk ( OOooooO ) :
   OOOOoO0 = 0
   OOOOoO0 += len ( OOIi1iI111II1I1 )
   if 80 - 80: I1IiI + iIii1I11I1II1 . IIII
   if 76 - 76: OOOo0 * OoOO0ooOOoo0O
   if OOOOoO0 > 0 :
    if 12 - 12: iIii1I11I1II1 / o0000oOoOoO0o % o00O0oo
    ii11iIi1I = xbmcgui . Dialog ( )
    if ii11iIi1I . yesno ( "Delete Phoenix Cache Files" , str ( OOOOoO0 ) + " files found" , "Do you want to delete them?" ) :
     if 49 - 49: Ooo00oOo00o + OoOoOO00 / IIII - O0 % o00O0oo
     for i11i1 in OOIi1iI111II1I1 :
      os . unlink ( os . path . join ( oOoO , i11i1 ) )
     for iIIIi1iii1I11 in oOoO00O0 :
      shutil . rmtree ( os . path . join ( oOoO , iIIIi1iii1I11 ) )
      if 27 - 27: Ooo00oOo00o + Oo
   else :
    pass
    if 92 - 92: OOOo0 % oO0o0ooO0
    if 31 - 31: OoooooooOO - OoOO / O0oO
 oo00o000O = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.spotitube/cache' ) , '' )
 if os . path . exists ( iI1iIi ) == True :
  for oOoO , oOoO00O0 , OOIi1iI111II1I1 in os . walk ( oo00o000O ) :
   OOOOoO0 = 0
   OOOOoO0 += len ( OOIi1iI111II1I1 )
   if 66 - 66: OoooooooOO + OOooOOo . i1IIi * oO0o0ooO0
   if 92 - 92: o0000oOoOoO0o / O0oO
   if OOOOoO0 > 0 :
    if 4 - 4: O0oO
    ii11iIi1I = xbmcgui . Dialog ( )
    if ii11iIi1I . yesno ( "Delete YouTube Music Cache Files" , str ( OOOOoO0 ) + " files found" , "Do you want to delete them?" ) :
     if 11 - 11: OoooooooOO + i1IIi / o00O0oo
     for i11i1 in OOIi1iI111II1I1 :
      os . unlink ( os . path . join ( oOoO , i11i1 ) )
     for iIIIi1iii1I11 in oOoO00O0 :
      shutil . rmtree ( os . path . join ( oOoO , iIIIi1iii1I11 ) )
      if 25 - 25: o00O0oo . OoOO0ooOOoo0O
   else :
    pass
    if 14 - 14: O0 / o0000oOoOoO0o . Ooo00oOo00o % oO0o0ooO0 . OoOO
    if 16 - 16: OoooooooOO % OOOo0 - OOooOOo / OoOoOO00 . i1IIi
 Iii1II1 = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.supercartoons/cache' ) , '' )
 if os . path . exists ( iI1iIi ) == True :
  for oOoO , oOoO00O0 , OOIi1iI111II1I1 in os . walk ( Iii1II1 ) :
   OOOOoO0 = 0
   OOOOoO0 += len ( OOIi1iI111II1I1 )
   if 54 - 54: I1IiI . Oo
   if 38 - 38: i1IIi . Oo * Oo / ii11ii1ii
   if OOOOoO0 > 0 :
    if 65 - 65: o0oO0 % O0
    ii11iIi1I = xbmcgui . Dialog ( )
    if ii11iIi1I . yesno ( "Delete SuperCartoons Cache Files" , str ( OOOOoO0 ) + " files found" , "Do you want to delete them?" ) :
     if 17 - 17: i1IIi + OoOO . o0000oOoOoO0o + i1IIi - OoOoOO00 % OOOo0
     for i11i1 in OOIi1iI111II1I1 :
      os . unlink ( os . path . join ( oOoO , i11i1 ) )
     for iIIIi1iii1I11 in oOoO00O0 :
      shutil . rmtree ( os . path . join ( oOoO , iIIIi1iii1I11 ) )
      if 34 - 34: OOOo0
   else :
    pass
    if 57 - 57: OoOO0ooOOoo0O . o00O0oo % OOooOOo
    if 32 - 32: o0000oOoOoO0o / IIII - O0 * iIii1I11I1II1
 oo0oO0oOo0O = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.tvonline.cc/cache' ) , '' )
 if os . path . exists ( iI1iIi ) == True :
  for oOoO , oOoO00O0 , OOIi1iI111II1I1 in os . walk ( oo0oO0oOo0O ) :
   OOOOoO0 = 0
   OOOOoO0 += len ( OOIi1iI111II1I1 )
   if 75 - 75: OoOoOO00 + OoOoOO00 + OoOO0ooOOoo0O * OOooOOo
   if 62 - 62: iIii1I11I1II1 - i1IIi - OoOO
   if OOOOoO0 > 0 :
    if 72 - 72: I1IiI / O0oO * IIII % iIii1I11I1II1
    ii11iIi1I = xbmcgui . Dialog ( )
    if ii11iIi1I . yesno ( "Delete TVonline Cache Files" , str ( OOOOoO0 ) + " files found" , "Do you want to delete them?" ) :
     if 53 - 53: Ooo00oOo00o . O0 . OOOo0 * OoOO0ooOOoo0O / OOooOOo
     for i11i1 in OOIi1iI111II1I1 :
      os . unlink ( os . path . join ( oOoO , i11i1 ) )
     for iIIIi1iii1I11 in oOoO00O0 :
      shutil . rmtree ( os . path . join ( oOoO , iIIIi1iii1I11 ) )
      if 34 - 34: I1IiI
   else :
    pass
    if 16 - 16: i1IIi - O0oO - OoOoOO00
    if 83 - 83: OOOo0 - Ooo00oOo00o - OOooOOo / O0 - o0000oOoOoO0o . OoOoOO00
 iI1i1Ii111I = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.youtube/kodion' ) , '' )
 if os . path . exists ( iI1iIi ) == True :
  for oOoO , oOoO00O0 , OOIi1iI111II1I1 in os . walk ( iI1i1Ii111I ) :
   OOOOoO0 = 0
   OOOOoO0 += len ( OOIi1iI111II1I1 )
   if 17 - 17: O0 * iIii1I11I1II1 % IIII . IIII / O0
   if 52 - 52: OOOo0 - iIii1I11I1II1 - ii11ii1ii
   if OOOOoO0 > 0 :
    if 38 - 38: OOOo0 + OOooOOo - IIII
    ii11iIi1I = xbmcgui . Dialog ( )
    if ii11iIi1I . yesno ( "Delete YouTube Cache Files" , str ( OOOOoO0 ) + " files found" , "Do you want to delete them?" ) :
     if 85 - 85: oO0o0ooO0 * oO0o0ooO0 % I1IiI - OoOO0ooOOoo0O % Ooo00oOo00o - OOOo0
     for i11i1 in OOIi1iI111II1I1 :
      os . unlink ( os . path . join ( oOoO , i11i1 ) )
     for iIIIi1iii1I11 in oOoO00O0 :
      shutil . rmtree ( os . path . join ( oOoO , iIIIi1iii1I11 ) )
      if 3 - 3: OoOO0ooOOoo0O + i1IIi % ii11ii1ii
   else :
    pass
    if 100 - 100: OoooooooOO + i11iIiiIii % OOooOOo + OOOo0 . Oo . OoOoOO00
    if 93 - 93: OoOoOO00 . i11iIiiIii + OoOoOO00 % OoOO
    if 98 - 98: O0oO * OoOO * I1IiI + o00O0oo * oO0o0ooO0
 ii11iI1iIiiI = xbmc . translatePath ( 'special://masterprofile/addon_data/plugin.video.genesis' )
 ii11iIi1I = xbmcgui . Dialog ( )
 try :
  if ii11iIi1I . yesno ( "Delete Genesis Cache Files" , "Do you want to delete cache" ) :
   oo00o00O0 = os . path . join ( ii11iI1iIiiI , "cache.db" )
   os . unlink ( oo00o00O0 )
   if 52 - 52: oO0o0ooO0 + O0 % OOooOOo % O0 % OoOoOO00 + OoooooooOO
 except :
  pass
  if 51 - 51: oO0o0ooO0 % i11iIiiIii
 ii11iIi1I = xbmcgui . Dialog ( )
 ii11iIi1I . ok ( "GenieTv" , "                               Finished Deleting Cache " , "                          [COLOR gold]Brought To You By GenieTv[/COLOR]" )
 if 28 - 28: ii11ii1ii + ii11ii1ii % I1IiI
 if 12 - 12: o0000oOoOoO0o
 if 19 - 19: o00O0oo * i1IIi % O0 + o0000oOoOoO0o
 if 25 - 25: O0oO - o00O0oo / O0 . OoooooooOO % OOOo0 . i1IIi
 if 19 - 19: OoOoOO00 / OoOoOO00 % ii11ii1ii + OoOO + OoOO + oO0o0ooO0
 if 4 - 4: OOooOOo + o0000oOoOoO0o / oO0o0ooO0 + i1IIi % OOooOOo % oO0o0ooO0
 if 80 - 80: o00O0oo
 if 26 - 26: iIii1I11I1II1 . OoooooooOO - iIii1I11I1II1
 if 59 - 59: ii11ii1ii + o0000oOoOoO0o . OoOO
def oOOo0oO ( url ) :
 print '###' + i11 + ' - DELETING PACKAGES###'
 iIIII1iII1i = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' , '' ) )
 try :
  for oOoO , oOoO00O0 , OOIi1iI111II1I1 in os . walk ( iIIII1iII1i ) :
   OOOOoO0 = 0
   OOOOoO0 += len ( OOIi1iI111II1I1 )
   if 98 - 98: O0oO % Ooo00oOo00o - o0oO0 % i11iIiiIii + O0oO - IIII
   if 97 - 97: o0oO0 / iIii1I11I1II1 % o0oO0 / OOOo0 * oO0o0ooO0 % I1IiI
   if OOOOoO0 > 0 :
    if 17 - 17: iIii1I11I1II1
    ii11iIi1I = xbmcgui . Dialog ( )
    if ii11iIi1I . yesno ( "Delete Package Cache Files" , str ( OOOOoO0 ) + " files found" , "Do you want to delete them?" ) :
     if 89 - 89: i1IIi . i1IIi
     for i11i1 in OOIi1iI111II1I1 :
      os . unlink ( os . path . join ( oOoO , i11i1 ) )
     for iIIIi1iii1I11 in oOoO00O0 :
      shutil . rmtree ( os . path . join ( oOoO , iIIIi1iii1I11 ) )
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
 if 10 - 10: oO0o0ooO0 % Oo
 if 48 - 48: OoOO0ooOOoo0O + O0oO % OoOO0ooOOoo0O
 if 84 - 84: O0 % o00O0oo . o00O0oo . oO0o0ooO0 * o0000oOoOoO0o
 if 43 - 43: I1IiI . ii11ii1ii % i1IIi
 if 61 - 61: OOOo0 + OoOO % O0oO % iIii1I11I1II1 - OoooooooOO
 if 22 - 22: OoOO0ooOOoo0O + OoOoOO00 + Oo
 if 83 - 83: o0oO0
 if 43 - 43: OoOO0ooOOoo0O
 if 84 - 84: OoOO0ooOOoo0O . IIII . oO0o0ooO0
def iIII1I1i ( url ) :
 print '###' + i11 + ' - DELETING PACKAGES###'
 iIIII1iII1i = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' , '' ) )
 try :
  for oOoO , oOoO00O0 , OOIi1iI111II1I1 in os . walk ( iIIII1iII1i ) :
   OOOOoO0 = 0
   OOOOoO0 += len ( OOIi1iI111II1I1 )
   if 26 - 26: oO0o0ooO0 - Oo + OOOo0 + OOooOOo
   if 37 - 37: OOooOOo * OoOO0ooOOoo0O + OOOo0 . ii11ii1ii * OoooooooOO
   if OOOOoO0 > 0 :
    if 82 - 82: i11iIiiIii + iIii1I11I1II1 / Oo + OoOO0ooOOoo0O * OoOoOO00
    ii11iIi1I = xbmcgui . Dialog ( )
    if ii11iIi1I . yesno ( "Delete Package Cache Files" , str ( OOOOoO0 ) + " files found" , "Do you want to delete them?" ) :
     if 34 - 34: OOooOOo % OoooooooOO
     for i11i1 in OOIi1iI111II1I1 :
      os . unlink ( os . path . join ( oOoO , i11i1 ) )
     for iIIIi1iii1I11 in oOoO00O0 :
      shutil . rmtree ( os . path . join ( oOoO , iIIIi1iii1I11 ) )
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
 I1iIIi ( url )
 if 36 - 36: OOOo0
 if 64 - 64: i11iIiiIii + i1IIi % O0 . o0000oOoOoO0o
 if 64 - 64: o0oO0 / i1IIi % oO0o0ooO0
 if 84 - 84: I1IiI - Oo . o0oO0 . IIII - Oo
 if 99 - 99: O0oO
 if 75 - 75: o0oO0 . OoOO0ooOOoo0O / IIII
 if 84 - 84: OoooooooOO . OOOo0 / OOooOOo
 if 86 - 86: Oo % I1IiI
 if 77 - 77: o00O0oo % OoOO0ooOOoo0O / OoOO
def OOoOo ( url , name ) :
 OO = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 Iiiiiii11IIiI = os . path . join ( OO , 'advancedsettings.xml' )
 ii11iIi1I = xbmcgui . Dialog ( )
 oOOO0o = os . path . join ( OO , 'advancedsettings.xml.bak' )
 if os . path . exists ( oOOO0o ) == False :
  if ii11iIi1I . yesno ( "Back Up Original" , 'Have You Backed Up Your Original?' , '' , "[B][COLOR red]     AS YOU CANNOT GO BACK !!![/B][/COLOR]" ) :
   print '###' + i11 + ' - ADVANCED XML###'
   OO = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
   Iiiiiii11IIiI = os . path . join ( OO , 'advancedsettings.xml' )
   try :
    os . remove ( Iiiiiii11IIiI )
    print '=== GenieTv - REMOVING    ' + str ( Iiiiiii11IIiI ) + '    ==='
   except :
    pass
   OOOo00oo0oO = I11 . http_GET ( url ) . content
   oOOOOoOO0o = open ( Iiiiiii11IIiI , "w" )
   oOOOOoOO0o . write ( OOOo00oo0oO )
   oOOOOoOO0o . close ( )
   print '=== GenieTv - WRITING NEW    ' + str ( Iiiiiii11IIiI ) + '    ==='
   ii11iIi1I = xbmcgui . Dialog ( )
   ii11iIi1I . ok ( i11 , "       Done Adding new Advanced XML" )
 else :
  print '###' + i11 + ' - ADVANCED XML###'
  OO = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
  Iiiiiii11IIiI = os . path . join ( OO , 'advancedsettings.xml' )
  try :
   os . remove ( Iiiiiii11IIiI )
   print '=== GenieTv - REMOVING    ' + str ( Iiiiiii11IIiI ) + '    ==='
  except :
   pass
  OOOo00oo0oO = I11 . http_GET ( url ) . content
  oOOOOoOO0o = open ( Iiiiiii11IIiI , "w" )
  oOOOOoOO0o . write ( OOOo00oo0oO )
  oOOOOoOO0o . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( Iiiiiii11IIiI ) + '    ==='
  ii11iIi1I = xbmcgui . Dialog ( )
  ii11iIi1I . ok ( i11 , "       Done Adding new Advanced XML" )
 return
 if 70 - 70: i11iIiiIii / o0oO0 * ii11ii1ii - i1IIi + o0oO0
def i1iIiii1IIi1iI1ii1 ( url , name ) :
 print '###' + i11 + ' - CHECK ADVANCE XML###'
 OO = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 Iiiiiii11IIiI = os . path . join ( OO , 'advancedsettings.xml' )
 try :
  oOOOOoOO0o = open ( Iiiiiii11IIiI ) . read ( )
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
 if 58 - 58: o00O0oo . o0000oOoOoO0o
def iIIiIi111iI ( url ) :
 print '###' + i11 + ' - DELETING ADVANCE XML###'
 OO = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 Iiiiiii11IIiI = os . path . join ( OO , 'advancedsettings.xml' )
 try :
  os . remove ( Iiiiiii11IIiI )
  ii11iIi1I = xbmcgui . Dialog ( )
  print '=== GenieTv - DELETING    ' + str ( Iiiiiii11IIiI ) + '    ==='
  ii11iIi1I . ok ( i11 , "       Remove Advanced Settings Sucessfull" )
 except :
  ii11iIi1I = xbmcgui . Dialog ( )
  ii11iIi1I . ok ( i11 , "       No Advanced Settings To Remove" )
 return
 if 40 - 40: I1IiI + Ooo00oOo00o % OoooooooOO * OOooOOo / I1IiI + OoooooooOO
 if 91 - 91: o0oO0 - OoOO + OoOO
 if 14 - 14: ii11ii1ii * O0oO % i1IIi / ii11ii1ii
 if 48 - 48: Oo
 if 75 - 75: ii11ii1ii - IIII * Oo . OoooooooOO * O0oO * OOOo0
 if 30 - 30: I1IiI / OoOO / o00O0oo * OOooOOo * OoOO . OOOo0
 if 93 - 93: I1IiI
 if 97 - 97: i11iIiiIii
 if 68 - 68: IIII * Ooo00oOo00o . o0000oOoOoO0o / o00O0oo . OOooOOo - i11iIiiIii
 if 49 - 49: Oo / o00O0oo % o0000oOoOoO0o + OoOO - Ooo00oOo00o
def i11iii1iiIi1IiiiI ( url = 'http://www.iplocation.net/' , inc = 1 ) :
 i1iIi = re . compile ( "<td width='80'>(.+?)</td><td>(.+?)</td><td>(.+?)</td><td>.+?</td><td>(.+?)</td>" ) . findall ( I11 . http_GET ( url ) . content )
 for OO0oooOO , IIIi1iiIIiiiI , I1IIiIi1iI , oOo0Iiii11 in i1iIi :
  if inc < 2 : ii11iIi1I = xbmcgui . Dialog ( ) ; ii11iIi1I . ok ( 'Check My IP' , "[B][COLOR gold]Your IP Address is: [/COLOR][/B] %s" % OO0oooOO , '[B][COLOR gold]Your IP is based in: [/COLOR][/B] %s' % I1IIiIi1iI , '[B][COLOR gold]Your Service Provider is:[/COLOR][/B] %s' % oOo0Iiii11 )
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
  Iiiiiii11IIiI = os . path . join ( OO , 'addons2.ini' )
  OOOo00oo0oO = I11 . http_GET ( url ) . content
  oOOOOoOO0o = open ( Iiiiiii11IIiI , "w" )
  oOOOOoOO0o . write ( OOOo00oo0oO )
  oOOOOoOO0o . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( Iiiiiii11IIiI ) + '    ==='
  ii11iIi1I = xbmcgui . Dialog ( )
  ii11iIi1I . ok ( i11 , "                               Done Adding New .ini File" )
 return
 if 57 - 57: o0oO0 + O0oO
def iIiiIi1IIIi11 ( url , name ) :
 ii11iIi1I = xbmcgui . Dialog ( )
 if ii11iIi1I . yesno ( "GenieTv" , '                               Install Custom Settings' ) :
  print '###' + i11 + ' - CUSTOM FTV SETTINGS###'
  OO = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/script.ftvguide' , '' ) )
  Iiiiiii11IIiI = os . path . join ( OO , 'settings.xml' )
  OOOo00oo0oO = I11 . http_GET ( url ) . content
  oOOOOoOO0o = open ( Iiiiiii11IIiI , "w" )
  oOOOOoOO0o . write ( OOOo00oo0oO )
  oOOOOoOO0o . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( Iiiiiii11IIiI ) + '    ==='
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
def IIiIi1iI ( url ) :
 OOOOO0 = urllib2 . Request ( url )
 OOOOO0 . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
 Ooo0Oo0o = urllib2 . urlopen ( OOOOO0 )
 OOOo00oo0oO = Ooo0Oo0o . read ( )
 Ooo0Oo0o . close ( )
 return OOOo00oo0oO
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
    oOoO00O0 [ : ] = [ iIIIi1iii1I11 for iIIIi1iii1I11 in oOoO00O0 if iIIIi1iii1I11 not in Oo0oO0ooo ]
    for ooOOoooooo in OOIi1iI111II1I1 :
     try : os . remove ( os . path . join ( oOoO , ooOOoooooo ) )
     except :
      if ooOOoooooo not in [ "Addons15.db" , "MyVideos75.db" , "Textures13.db" , "xbmc.log" ] : O0oooooO = True
      plugintools . log ( "Error removing " + oOoO + " " + ooOOoooooo )
    for ooOOoooooo in oOoO00O0 :
     try : os . rmdir ( os . path . join ( oOoO , ooOOoooooo ) )
     except :
      if ooOOoooooo not in [ "Database" , "userdata" ] : O0oooooO = True
      plugintools . log ( "Error removing " + oOoO + " " + ooOOoooooo )
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
i1i = base64 . decodestring ( 'LmFyY2hpdGVjdHMueDEwaG9zdC5jb20vdGVzdC93aC50eHQ=' )
i1IiiiI1iI = base64 . decodestring ( 'aHR0cDovL2ZpeGVzLmFyY2hpdGVjdHMueDEwaG9zdC5jb20vZml4ZXMudHh0' )
i1iiiI = base64 . decodestring ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vYXBwcy9hcHBzLnhtbA==' )
oOIii = base64 . decodestring ( 'L2FkZG9ucy9uZXcudHh0' )
III11iIII1 = base64 . decodestring ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vdm9kL3ZvZC5waHA=' )
oooo0O0Oooo = base64 . decodestring ( 'L2FkZG9ucy9pcHR2LnR4dA==' )
I11iIIi = base64 . decodestring ( 'L2FkZG9ucy92aWRlby50eHQ=' )
O0o0o = base64 . decodestring ( 'L2FkZG9ucy9zcG9ydHMudHh0' )
II1ii1iii1ii = base64 . decodestring ( 'L2FkZG9ucy9raWRzLnR4dA==' )
i1Ii1 = base64 . decodestring ( 'L2FkZG9ucy9tdXNpYy50eHQ=' )
OoIIiIIIII1I = base64 . decodestring ( 'L2FkZG9ucy9wcm9ncmFtcy50eHQ=' )
Iii1IiI1iI1I = base64 . decodestring ( 'L2FkZG9ucy94eHgudHh0' )
ii1IiIIiI11111Ii = base64 . decodestring ( 'L2FkZG9ucy9yZXBvLnR4dA==' )
OOooooO0Oo = base64 . decodestring ( 'L2FkZG9ucy9wYWNrcy50eHQ=' )
Iiiiii = base64 . decodestring ( 'L2FkZG9ucy9za2lucy50eHQ=' )
IIi11i1i1iI1 = base64 . decodestring ( 'L2FkZG9ucy9hcnQudHh0' )
ii = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2dvdGhhbS50eHQ=' )
i1Iii1i1I = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2hlbGl4LnR4dA==' )
Iiii1i1 = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2lzZW5nYXJkLnR4dA==' )
OO0Oo00OO0oo = base64 . decodestring ( 'L2FkZG9ucy9SU1MudHh0' )
oOOIi1II = base64 . decodestring ( 'Q1VOVA==' )
def ooooooO0oo ( name , url , mode , iconimage , fanart , description , showcontext = True , allinfo = { } ) :
 o0oO00 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 O0o = True
 oO00oO = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 oO00oO . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 oO00oO . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  IiI11I1Ii11II = [ ]
  if showcontext == 'fav' :
   IiI11I1Ii11II . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in o0 :
   IiI11I1Ii11II . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fanart=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , urllib . quote_plus ( fanart ) , mode ) ) )
  oO00oO . addContextMenuItems ( IiI11I1Ii11II )
 O0o = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = o0oO00 , listitem = oO00oO , isFolder = True )
 return O0o
 if 80 - 80: OOOo0
def I1111I1iII11 ( name , url , mode , iconimage , fanart , description ) :
 o0oO00 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 O0o = True
 oO00oO = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 oO00oO . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 oO00oO . setProperty ( "Fanart_Image" , fanart )
 O0o = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = o0oO00 , listitem = oO00oO , isFolder = False )
 return O0o
 if 58 - 58: OoOO + ii11ii1ii % I1IiI
 if 22 - 22: iIii1I11I1II1 - o00O0oo / OOOo0 * IIII
o00IIIIii1111i1 = ooOo0 ( )
I1Ii1iI1 = None
ooOOoooooo = None
Ii1iI111 = None
II1I = None
O0i1II1Iiii1I11 = None
IIIIiiIiI = None
III1IIi = None
if 37 - 37: iIii1I11I1II1 * I1IiI / ii11ii1ii . OoOoOO00
if 88 - 88: o0oO0 + O0
try :
 III1IIi = int ( o00IIIIii1111i1 [ "fav_mode" ] )
except :
 pass
 if 87 - 87: O0oO + OoooooooOO * i1IIi * i11iIiiIii
try :
 I1Ii1iI1 = urllib . unquote_plus ( o00IIIIii1111i1 [ "url" ] )
except :
 pass
try :
 ooOOoooooo = urllib . unquote_plus ( o00IIIIii1111i1 [ "name" ] )
except :
 pass
try :
 II1I = urllib . unquote_plus ( o00IIIIii1111i1 [ "iconimage" ] )
except :
 pass
try :
 Ii1iI111 = int ( o00IIIIii1111i1 [ "mode" ] )
except :
 pass
try :
 O0i1II1Iiii1I11 = urllib . unquote_plus ( o00IIIIii1111i1 [ "fanart" ] )
except :
 pass
try :
 IIIIiiIiI = urllib . unquote_plus ( o00IIIIii1111i1 [ "description" ] )
except :
 pass
 if 74 - 74: OoooooooOO - OOooOOo * oO0o0ooO0
 if 37 - 37: OOooOOo * Oo
print str ( II11iiii1Ii ) + ': ' + str ( iiI1IiI )
print "Mode: " + str ( Ii1iI111 )
print "URL: " + str ( I1Ii1iI1 )
print "Name: " + str ( ooOOoooooo )
print "IconImage: " + str ( II1I )
if 11 - 11: OoOO
if 62 - 62: OoooooooOO % OoOO * OoOoOO00 * O0oO * O0oO / o0oO0
def I1i1I1II ( content , viewType ) :
 if 90 - 90: O0oO . OoOoOO00 . ii11ii1ii
 if content :
  xbmcplugin . setContent ( int ( sys . argv [ 1 ] ) , content )
 if o0oOoO00o . getSetting ( 'auto-view' ) == 'true' :
  xbmc . executebuiltin ( "Container.SetViewMode(%s)" % o0oOoO00o . getSetting ( viewType ) )
  if 32 - 32: o0oO0 - Ooo00oOo00o . oO0o0ooO0 . oO0o0ooO0 % i1IIi * o00O0oo
  if 65 - 65: oO0o0ooO0 / o0oO0 . OoOoOO00
if Ii1iI111 == None :
 IIIII ( )
 if 90 - 90: o0000oOoOoO0o
elif Ii1iI111 == 1 :
 O0oOOO0ooOOO0OOO ( I1Ii1iI1 )
 if 95 - 95: Ooo00oOo00o
elif Ii1iI111 == 44 :
 i1OOoO ( I1Ii1iI1 )
 if 68 - 68: iIii1I11I1II1 . iIii1I11I1II1 / I1IiI - OoOoOO00 - iIii1I11I1II1
elif Ii1iI111 == 2 :
 I1i ( )
 if 75 - 75: o0oO0 . OOOo0 * OoOoOO00
elif Ii1iI111 == 3 :
 O00o0O00 ( )
 if 99 - 99: iIii1I11I1II1 * ii11ii1ii + IIII
elif Ii1iI111 == 21 :
 O0Oooo0OO ( )
 if 70 - 70: i1IIi % o0oO0 . ii11ii1ii - IIII + OoOO0ooOOoo0O
elif Ii1iI111 == 4 :
 oooooOoo0ooo ( )
 if 84 - 84: OoOO + OoOoOO00 * OoOoOO00 % OOooOOo / oO0o0ooO0 + o0oO0
elif Ii1iI111 == 5 :
 ooooo0O0000oo ( ooOOoooooo , I1Ii1iI1 , IIIIiiIiI )
 if 9 - 9: oO0o0ooO0
elif Ii1iI111 == 6 :
 oOOo0oO ( I1Ii1iI1 )
 if 25 - 25: OoOO0ooOOoo0O - o00O0oo . o0000oOoOoO0o
elif Ii1iI111 == 7 :
 OOoOo ( I1Ii1iI1 , ooOOoooooo )
 if 57 - 57: OOooOOo + Oo * ii11ii1ii - o0oO0 % iIii1I11I1II1 - o00O0oo
elif Ii1iI111 == 8 :
 i1iIiii1IIi1iI1ii1 ( I1Ii1iI1 , ooOOoooooo )
 if 37 - 37: Ooo00oOo00o * o0000oOoOoO0o + o00O0oo + ii11ii1ii * OOooOOo
elif Ii1iI111 == 9 :
 FIXREPOSADDONS ( I1Ii1iI1 )
 if 95 - 95: o00O0oo - i11iIiiIii % i11iIiiIii - O0 * O0oO
elif Ii1iI111 == 10 :
 OO0O0 ( )
 if 81 - 81: OoOoOO00 * OOOo0 % i1IIi * i11iIiiIii + I1IiI
elif Ii1iI111 == 11 :
 iIIiIi111iI ( I1Ii1iI1 )
 if 100 - 100: i1IIi % o00O0oo
elif Ii1iI111 == 12 :
 i11iii1iiIi1IiiiI ( )
 if 55 - 55: OOOo0 + oO0o0ooO0
elif Ii1iI111 == 13 :
 O0OoOo ( )
 if 85 - 85: OoOO + oO0o0ooO0 % oO0o0ooO0 / o0000oOoOoO0o . OOOo0 - I1IiI
elif Ii1iI111 == 14 :
 I1iIIi ( I1Ii1iI1 )
 if 19 - 19: o0000oOoOoO0o / oO0o0ooO0 + IIII
elif Ii1iI111 == 15 :
 oOOo0 ( )
 if 76 - 76: iIii1I11I1II1 / O0oO - ii11ii1ii % OOooOOo % OoOO0ooOOoo0O + OoooooooOO
elif Ii1iI111 == 16 :
 iIIiII1i1ii ( I1Ii1iI1 , ooOOoooooo )
 if 10 - 10: Ooo00oOo00o * o0000oOoOoO0o / Oo - O0oO
elif Ii1iI111 == 17 :
 iIiiIi1IIIi11 ( I1Ii1iI1 , ooOOoooooo )
 if 11 - 11: IIII % ii11ii1ii / o0oO0 . i11iIiiIii + OoOO0ooOOoo0O - OoOoOO00
elif Ii1iI111 == 18 :
 I1iiII1 ( )
 if 50 - 50: i1IIi * OoOO / i11iIiiIii / i11iIiiIii / OoOO
elif Ii1iI111 == 19 :
 Ii1I1i ( ooOOoooooo , I1Ii1iI1 , IIIIiiIiI )
 if 84 - 84: ii11ii1ii - oO0o0ooO0 + ii11ii1ii
elif Ii1iI111 == 40 :
 oOOoo00O00o ( ooOOoooooo , I1Ii1iI1 , IIIIiiIiI )
 if 63 - 63: o0000oOoOoO0o * o0oO0 % OoOoOO00 % O0oO + OOOo0 * Oo
elif Ii1iI111 == 42 :
 o0o0O0O00oOOo ( ooOOoooooo , I1Ii1iI1 , IIIIiiIiI )
 if 96 - 96: IIII
elif Ii1iI111 == 43 :
 o00oo0 ( ooOOoooooo , I1Ii1iI1 , IIIIiiIiI )
 if 99 - 99: iIii1I11I1II1 - o0oO0
elif Ii1iI111 == 20 :
 OOOOoOoo0O0O0 ( I1Ii1iI1 )
 if 79 - 79: OOOo0 + OoOO % o0000oOoOoO0o % OoOO
elif Ii1iI111 == 22 :
 Ii1I1Iiii ( I1Ii1iI1 )
 if 56 - 56: ii11ii1ii + OoOO . Ooo00oOo00o + OoooooooOO * ii11ii1ii - O0
elif Ii1iI111 == 23 :
 oO00o ( I1Ii1iI1 )
 if 35 - 35: OoOO0ooOOoo0O . o0000oOoOoO0o . O0oO - o0000oOoOoO0o % o0000oOoOoO0o + O0oO
elif Ii1iI111 == 24 :
 IiIii11i1IIiI ( I1Ii1iI1 )
 if 99 - 99: OOooOOo + OoOO0ooOOoo0O
elif Ii1iI111 == 25 :
 Iii1I11 ( I1Ii1iI1 )
 if 34 - 34: O0oO * OOooOOo . OOOo0 % i11iIiiIii
elif Ii1iI111 == 26 :
 OOOoOOO0o0ooo ( I1Ii1iI1 )
 if 61 - 61: iIii1I11I1II1 + OoOO * o0000oOoOoO0o - i1IIi % OoOO
elif Ii1iI111 == 27 :
 o00O0o ( I1Ii1iI1 )
 if 76 - 76: OoOO / I1IiI
elif Ii1iI111 == 28 :
 o0oOo ( I1Ii1iI1 )
 if 12 - 12: O0oO
elif Ii1iI111 == 29 :
 iI1I ( I1Ii1iI1 )
 if 58 - 58: Ooo00oOo00o + iIii1I11I1II1 % O0 + o0000oOoOoO0o + I1IiI * OoooooooOO
elif Ii1iI111 == 30 :
 o0Ooo00o0Oooo ( I1Ii1iI1 )
 if 41 - 41: OoOO * OOOo0
elif Ii1iI111 == 31 :
 II1IIii1I11I ( I1Ii1iI1 )
 if 76 - 76: OoOO . O0 * OoooooooOO + o0oO0
elif Ii1iI111 == 32 :
 Ii1 ( )
 if 53 - 53: Oo
elif Ii1iI111 == 33 :
 IIi1I11I1II ( )
 if 3 - 3: IIII - OoooooooOO * OoooooooOO - OOOo0 / O0oO * ii11ii1ii
elif Ii1iI111 == 35 :
 IiI1iIiIIIii ( I1Ii1iI1 )
 if 58 - 58: IIII % iIii1I11I1II1 / i11iIiiIii % OOooOOo . O0oO * oO0o0ooO0
elif Ii1iI111 == 34 :
 iI111i ( I1Ii1iI1 )
 if 32 - 32: OoooooooOO + OOooOOo
elif Ii1iI111 == 36 :
 o0OOOO00O0Oo ( I1Ii1iI1 )
 if 91 - 91: o0oO0 - O0oO * O0oO
elif Ii1iI111 == 37 :
 IIi ( I1Ii1iI1 )
 if 55 - 55: iIii1I11I1II1 + OOOo0 - Oo
elif Ii1iI111 == 38 :
 O000OOOOOo ( I1Ii1iI1 )
 if 24 - 24: Ooo00oOo00o / O0oO + oO0o0ooO0 * o0000oOoOoO0o * oO0o0ooO0
elif Ii1iI111 == 41 :
 i11IiII ( o00IIIIii1111i1 )
 if 10 - 10: OOOo0 - ii11ii1ii - Oo - OOooOOo
elif Ii1iI111 == 39 :
 I1I1 ( I1Ii1iI1 )
 if 21 - 21: OoooooooOO + O0oO
elif Ii1iI111 == 45 :
 TEXTS ( )
 if 43 - 43: i11iIiiIii . ii11ii1ii . OoOO
elif Ii1iI111 == 46 :
 o000ooOo0o0OO ( )
 if 31 - 31: o00O0oo % OOooOOo % O0oO . ii11ii1ii / OOooOOo * OoOO
elif Ii1iI111 == 47 :
 GEVID ( )
 if 74 - 74: OOOo0 . o0oO0 / oO0o0ooO0 . IIII
elif Ii1iI111 == 48 :
 IIo0Oo0oO0oOO00 ( ooOOoooooo , I1Ii1iI1 , IIIIiiIiI )
 if 74 - 74: Oo / O0oO % O0oO . IIII
elif Ii1iI111 == 49 :
 OO0oOO0O ( )
 if 72 - 72: i1IIi
elif Ii1iI111 == 222 :
 oOiIi ( I1Ii1iI1 )
 if 21 - 21: O0oO . OoOO0ooOOoo0O / i11iIiiIii * i1IIi
elif Ii1iI111 == 333 :
 ii1iIII1ii ( I1Ii1iI1 )
 if 82 - 82: o0oO0 * Oo % i11iIiiIii * i1IIi . OoOO0ooOOoo0O
 if 89 - 89: IIII - i1IIi - IIII
elif Ii1iI111 == 1001 :
 o0I1iI111ii111i ( )
 if 74 - 74: Ooo00oOo00o % Ooo00oOo00o
elif Ii1iI111 == 1005 :
 O000o0 ( )
 if 28 - 28: I1IiI % OoOO - OoOO0ooOOoo0O + OoOO0ooOOoo0O + OoOO / iIii1I11I1II1
elif Ii1iI111 == 1007 :
 Iiiii1 ( I1Ii1iI1 )
 if 91 - 91: OOOo0 / OoOoOO00 * OoOO0ooOOoo0O
elif Ii1iI111 == 1010 :
 iI1iii1iI1 ( I1Ii1iI1 )
 if 94 - 94: OoOoOO00 - iIii1I11I1II1 - iIii1I11I1II1
elif Ii1iI111 == 1011 :
 ooO ( I1Ii1iI1 )
 if 83 - 83: ii11ii1ii * iIii1I11I1II1 + I1IiI * i1IIi . OoooooooOO % o00O0oo
elif Ii1iI111 == 1030 :
 ooOO0 ( )
 if 81 - 81: Ooo00oOo00o - iIii1I11I1II1
elif Ii1iI111 == 1031 :
 Oo00Oo ( I1Ii1iI1 , II1I )
 if 60 - 60: O0oO
elif Ii1iI111 == 1006 :
 Parse . ParseURL ( I1Ii1iI1 )
 if 77 - 77: OOOo0 / ii11ii1ii
elif Ii1iI111 == 2030 :
 Parse . addonParseURL ( I1Ii1iI1 )
 if 95 - 95: O0oO * i1IIi + OoOO
elif Ii1iI111 == 2031 :
 Parse . apkParseURL ( I1Ii1iI1 )
 if 40 - 40: OoOoOO00
elif Ii1iI111 == 1002 :
 I1iII11ii1 ( I1Ii1iI1 )
 if 7 - 7: OoOO0ooOOoo0O / Ooo00oOo00o
elif Ii1iI111 == 1003 :
 Ii111I11 ( I1Ii1iI1 , II1I )
 if 88 - 88: i1IIi
elif Ii1iI111 == 1004 :
 Oo0O0oo ( I1Ii1iI1 )
 if 53 - 53: o0oO0 . OoOO0ooOOoo0O . OOooOOo + OoOO
elif Ii1iI111 == 1008 :
 Ii1iiI1 ( )
 if 17 - 17: iIii1I11I1II1 + i1IIi . ii11ii1ii + o00O0oo % i1IIi . OoOO
elif Ii1iI111 == 1009 :
 M3UPLAY ( I1Ii1iI1 )
 if 57 - 57: OoOO
elif Ii1iI111 == 2001 :
 o0o00OoO0 ( I1Ii1iI1 )
 if 92 - 92: OoOoOO00 - Ooo00oOo00o - OoOO0ooOOoo0O % OOOo0 - I1IiI * O0oO
elif Ii1iI111 == 1013 :
 i1iI ( )
 if 16 - 16: iIii1I11I1II1 + OoooooooOO - o0oO0 * IIII
elif Ii1iI111 == 1014 :
 O0oO0OOoO ( )
 if 37 - 37: oO0o0ooO0
elif Ii1iI111 == 1015 :
 O00oo ( I1Ii1iI1 )
 if 15 - 15: OOooOOo % Ooo00oOo00o / oO0o0ooO0
elif Ii1iI111 == 1016 :
 O00o ( I1Ii1iI1 )
 if 36 - 36: Ooo00oOo00o + Ooo00oOo00o % Oo + Oo / i1IIi % i1IIi
elif Ii1iI111 == 1023 :
 oO0OOoO0 ( )
 if 20 - 20: OoOO0ooOOoo0O * OoOO
elif Ii1iI111 == 1024 :
 IiiiIIiii ( )
 if 91 - 91: Ooo00oOo00o % i1IIi - iIii1I11I1II1 . OoOO0ooOOoo0O
elif Ii1iI111 == 1025 :
 II1iIiiiI1 ( I1Ii1iI1 )
 if 31 - 31: OoOO % i1IIi . OoooooooOO - OOooOOo + OoooooooOO
elif Ii1iI111 == 4001 :
 oOii1i1I1i ( )
 if 45 - 45: OoOO0ooOOoo0O + o0000oOoOoO0o / OoooooooOO - o00O0oo + OoooooooOO
elif Ii1iI111 == 4002 :
 o00oOO0 ( )
 if 42 - 42: iIii1I11I1II1 * OOOo0 * O0oO
elif Ii1iI111 == 4003 :
 oO0o0OOOO ( )
 if 62 - 62: OoOO0ooOOoo0O * O0 % IIII . IIII . OOOo0
elif Ii1iI111 == 3000 :
 Oo0OO00OO0Oo ( )
 if 91 - 91: i1IIi . oO0o0ooO0
elif Ii1iI111 == 404 :
 i11Ii1IiIIIi ( ooOOoooooo , I1Ii1iI1 , II1I )
 if 37 - 37: oO0o0ooO0 - o0000oOoOoO0o + iIii1I11I1II1 / O0oO - Ooo00oOo00o . OOooOOo
elif Ii1iI111 == 7030 :
 iiI1ii111 ( )
 if 62 - 62: ii11ii1ii
elif Ii1iI111 == 7021 :
 OOooOO ( ooOOoooooo )
 if 47 - 47: O0oO % OoOO0ooOOoo0O * Ooo00oOo00o . iIii1I11I1II1 % Oo + OoooooooOO
elif Ii1iI111 == 7022 :
 o0O0Ooo ( ooOOoooooo )
 if 2 - 2: O0oO % OoooooooOO - o0oO0 * ii11ii1ii * IIII
elif Ii1iI111 == 7000 :
 o0oO00o ( ooOOoooooo , I1Ii1iI1 , img )
 if 99 - 99: iIii1I11I1II1 . Oo / o0oO0 . OoOO0ooOOoo0O % OOOo0 * o0000oOoOoO0o
elif Ii1iI111 == 7050 :
 iiI1iI ( )
 if 95 - 95: OoOO
elif Ii1iI111 == 7051 :
 OOoO0oooo ( I1Ii1iI1 )
 if 80 - 80: IIII
elif Ii1iI111 == 7060 :
 IiI11I111 ( )
 if 42 - 42: OoooooooOO * OoOoOO00
elif Ii1iI111 == 7061 :
 i11iioOOOOO0Ooooo ( I1Ii1iI1 )
 if 53 - 53: O0oO + i1IIi . Ooo00oOo00o / i11iIiiIii + o00O0oo % I1IiI
elif Ii1iI111 == 7063 :
 Ooo000O00 ( I1Ii1iI1 )
 if 9 - 9: o0oO0 . o0000oOoOoO0o - Oo . O0oO
elif Ii1iI111 == 7062 :
 oOO00ooOOo ( I1Ii1iI1 )
 if 39 - 39: OoOO0ooOOoo0O
elif Ii1iI111 == 7064 :
 NATatozcat ( )
 if 70 - 70: IIII % Ooo00oOo00o % OOOo0
elif Ii1iI111 == 7067 :
 IIiiiiIiI1III ( I1Ii1iI1 )
 if 95 - 95: I1IiI - O0oO / O0 * OOOo0 - OOooOOo
elif Ii1iI111 == 7066 :
 NATatozA ( I1Ii1iI1 )
 if 12 - 12: iIii1I11I1II1 % Oo . oO0o0ooO0 . IIII % i11iIiiIii
elif Ii1iI111 == 7065 :
 iIiI ( I1Ii1iI1 )
 if 2 - 2: OoOO * OoOO . I1IiI * o00O0oo * iIii1I11I1II1
elif Ii1iI111 == 7070 :
 O0oooOoO ( )
 if 13 - 13: o0000oOoOoO0o / O0 . i11iIiiIii * i1IIi % i11iIiiIii
elif Ii1iI111 == 7071 :
 DIZIlist ( I1Ii1iI1 )
 if 8 - 8: I1IiI - OoooooooOO
elif Ii1iI111 == 7072 :
 DIZIpull ( I1Ii1iI1 )
 if 99 - 99: OoOoOO00 / IIII % OoooooooOO . i11iIiiIii
elif Ii1iI111 == 7073 :
 WATCHDIZI ( I1Ii1iI1 )
 if 18 - 18: OOooOOo . o0oO0
elif Ii1iI111 == 7002 :
 O0Ooo0ooo00o ( )
 if 70 - 70: OoooooooOO . o0oO0 / OoOO . OoOO - OOooOOo
elif Ii1iI111 == 7003 :
 i1IiIIi ( I1Ii1iI1 )
 if 29 - 29: o0000oOoOoO0o % OoOO0ooOOoo0O - o0oO0
elif Ii1iI111 == 7004 :
 O0oOOOO00o0 ( I1Ii1iI1 )
 if 26 - 26: O0 . o0000oOoOoO0o + oO0o0ooO0 - o00O0oo . o0000oOoOoO0o
elif Ii1iI111 == 7020 :
 OOO0O0OOo ( I1Ii1iI1 )
 if 2 - 2: ii11ii1ii . Oo * OoOO0ooOOoo0O % OoOoOO00 . oO0o0ooO0
elif Ii1iI111 == 7001 :
 ooO0 ( )
 if 46 - 46: I1IiI + OOOo0 % OoooooooOO * i11iIiiIii - Oo
elif Ii1iI111 == 7010 :
 I1i1I ( I1Ii1iI1 )
 if 47 - 47: oO0o0ooO0 * I1IiI * IIII
elif Ii1iI111 == 7011 :
 oOOOooO ( I1Ii1iI1 )
 if 46 - 46: o00O0oo
elif Ii1iI111 == 7012 :
 i11II ( I1Ii1iI1 )
 if 42 - 42: iIii1I11I1II1
elif Ii1iI111 == 7013 :
 cnfTVPlay2 ( I1Ii1iI1 )
elif Ii1iI111 == 7014 :
 CNF_Studio_Indexer . MV_Movies ( I1Ii1iI1 )
elif Ii1iI111 == 7015 :
 CNF_Studio_Indexer . Movie_ByYear ( I1Ii1iI1 )
elif Ii1iI111 == 7016 :
 CNF_Studio_Indexer . Resolve_CNF_Link ( ooOOoooooo , I1Ii1iI1 , II1I )
elif Ii1iI111 == 7017 :
 CNF_Studio_Indexer . Search_Movie ( )
elif Ii1iI111 == 7018 :
 Ii11III ( )
elif Ii1iI111 == 7019 :
 CNF_Studio_Indexer . List_Movies ( I1Ii1iI1 )
elif Ii1iI111 == 7020 :
 CNF_Studio_Indexer . Get_Movie_Page ( I1Ii1iI1 )
elif Ii1iI111 == 7024 :
 CNF_Studio_Indexer . Box_Office ( I1Ii1iI1 )
 if 32 - 32: Oo - o00O0oo . OoooooooOO - OoooooooOO - Oo . iIii1I11I1II1
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
 iIiI1ii ( ooOOoooooo , I1Ii1iI1 )
elif Ii1iI111 == 8030 :
 IIi1 ( I1Ii1iI1 )
elif Ii1iI111 == 8045 :
 iI1IiiiIiI1Ii ( I1Ii1iI1 )
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
 iiiI11iIIi1 ( I1Ii1iI1 )
elif Ii1iI111 == 8064 :
 oooo ( )
elif Ii1iI111 == 8065 :
 iiiIIIii ( I1Ii1iI1 )
elif Ii1iI111 == 8070 :
 O0Oo0 ( )
elif Ii1iI111 == 8071 :
 OO0 ( I1Ii1iI1 )
elif Ii1iI111 == 7080 :
 I1iIiI1Iii ( I1Ii1iI1 )
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
 ii1ii1I1IIi1 ( I1Ii1iI1 , ooOOoooooo )
elif Ii1iI111 == 9000 :
 i1OOO ( )
elif Ii1iI111 == 1111 :
 oO0oOOOooo ( )
elif Ii1iI111 == 9001 :
 Ii1Ii1I ( )
elif Ii1iI111 == 9002 :
 O0OOOo000 ( )
elif Ii1iI111 == 9003 :
 OOO0O00Oo ( )
elif Ii1iI111 == 50 :
 oOo0O0Oo00oO ( I1Ii1iI1 )
elif Ii1iI111 == 9020 :
 i111IiI1I ( )
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
 ii111I11Ii ( IIIIiiIiI )
elif Ii1iI111 == 9666 :
 iIII1I1i ( I1Ii1iI1 )
elif Ii1iI111 == 10100 : IiI1o0O ( )
elif Ii1iI111 == 10105 : iiiii1I1III1 ( I1Ii1iI1 )
elif Ii1iI111 == 10106 : I11i1iIi111 ( I1Ii1iI1 )
elif Ii1iI111 == 10104 : O0oOO0o ( I1Ii1iI1 )
elif Ii1iI111 == 10107 : ii1I ( )
elif Ii1iI111 == 10103 : Ii11iI1II11ii ( I1Ii1iI1 )
elif Ii1iI111 == 10108 : ii1IIi1ii ( I1Ii1iI1 )
elif Ii1iI111 == 10107 : ii1I ( )
elif Ii1iI111 == 10000 : iIIIIii1 ( )
elif Ii1iI111 == 10001 : I1IiIiiIiIII ( )
elif Ii1iI111 == 10002 : Oo0O0O00Oo ( )
elif Ii1iI111 == 10003 : Oo0ooo ( )
elif Ii1iI111 == 10004 : oO00O0 ( )
elif Ii1iI111 == 10005 : o0oO000oo ( )
elif Ii1iI111 == 10006 : OooOOOO ( I1Ii1iI1 )
elif Ii1iI111 == 10007 : iiII1i11i ( I1Ii1iI1 , II1I )
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
elif Ii1iI111 == 10023 : iI ( ooOOoooooo , I1Ii1iI1 )
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
elif Ii1iI111 == 10045 : oo0ooO0 ( ooOOoooooo )
elif Ii1iI111 == 10046 : I1iI1I1 ( I1Ii1iI1 )
elif Ii1iI111 == 10047 : Ooooo0OoO0 ( I1Ii1iI1 )
elif Ii1iI111 == 10048 : iIi1i ( I1Ii1iI1 )
elif Ii1iI111 == 10049 : OOoOO0OO ( I1Ii1iI1 )
elif Ii1iI111 == 10050 : O00OO0O ( )
elif Ii1iI111 == 10051 : iiI1iIII1ii ( )
elif Ii1iI111 == 10052 : OOoOoOo0 ( )
elif Ii1iI111 == 10053 : Addon ( I1Ii1iI1 )
elif Ii1iI111 == 10054 : o00o0o000Oo ( I1Ii1iI1 , ooOOoooooo )
elif Ii1iI111 == 10055 :
 iII1I1 ( "addFavorite" )
 try :
  ooOOoooooo = ooOOoooooo . split ( '\\ ' ) [ 1 ]
 except :
  pass
 try :
  ooOOoooooo = ooOOoooooo . split ( '  - ' ) [ 0 ]
 except :
  pass
 ii1iii11i1 ( ooOOoooooo , I1Ii1iI1 , II1I , O0i1II1Iiii1I11 , III1IIi )
elif Ii1iI111 == 10056 :
 iII1I1 ( "rmFavorite" )
 try :
  ooOOoooooo = ooOOoooooo . split ( '\\ ' ) [ 1 ]
 except :
  pass
 try :
  ooOOoooooo = ooOOoooooo . split ( '  - ' ) [ 0 ]
 except :
  pass
 o0O ( ooOOoooooo )
elif Ii1iI111 == 10057 :
 iII1I1 ( "getFavorites" )
 iIIIII1iiiiII ( )
elif Ii1iI111 == 10058 : Ii11Ii1I ( )
elif Ii1iI111 == 10059 : Donators_Guide ( )
elif Ii1iI111 == 20000 : II1i11I ( )
elif Ii1iI111 == 20001 : IIii1111 ( )
elif Ii1iI111 == 20002 : oo0o0000 ( I1Ii1iI1 )
elif Ii1iI111 == 20003 : O00O ( I1Ii1iI1 )
elif Ii1iI111 == 20004 : iI1iIii11Ii ( I1Ii1iI1 )
if 34 - 34: Oo
xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
