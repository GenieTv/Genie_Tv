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
i1iIIi1 = xbmcgui . Dialog ( )
ii11iIi1I = xbmc . translatePath ( 'special://home/' )
iI111I11I1I1 = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + o00 , 'fanart.jpg' ) )
OOooO0OOoo = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + o00 , 'icon.png' , iI111I11I1I1 , '' ) )
iIii1 = ( oOo0oooo00o ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vR2VuaWVBcnQv' ) )
oOOoO0 = ( oOo0oooo00o ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vR2VuaWVBcnQvb3JpZ2luLnBuZw==' ) )
O0OoO000O0OO = "2.4.2"
iiI1IiI = xbmc . translatePath ( 'special://database' )
II = xbmc . translatePath ( 'special://thumbnails' ) ;
ooOoOoo0O = "GenieTv"
OooO0 = ( oOo0oooo00o ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20=' ) )
II11iiii1Ii = 'http://'
OO0o = o0oOoO00o . getLocalizedString
Ooo = CookieJar ( )
O0o0Oo = urllib2 . build_opener ( urllib2 . HTTPCookieProcessor ( Ooo ) )
O0o0Oo . addheaders = [ ( 'User-Agent' , 'Mozilla/5.0' ) ]
Oo00OOOOO = int ( sys . argv [ 1 ] )
if 85 - 85: o0oO0 . oO0o0ooO0 - Ooo00oOo00o % o0oO0 % OoOoOO00
def OO0o00o ( ) :
 oOOo0oo ( '[COLORgreen]WIZARD[/COLOR]' , OooO0 , 4001 , iIii1 + 'MB.png' , iI111I11I1I1 , '' )
 oOOo0oo ( '[COLORgreen]STREAMS[/COLOR]' , OooO0 , 4002 , iIii1 + 'streams.png' , iI111I11I1I1 , '' )
 oOOo0oo ( '[COLORgreen]MUSIC[/COLOR]' , OooO0 , 4003 , iIii1 + 'MUSIC.png' , iI111I11I1I1 , '' )
 if 80 - 80: o0000oOoOoO0o * i11iIiiIii / O0oO
 oOOo0oo ( '[COLORgreen]BUILDERS TOOLBOX[/COLOR]' , OooO0 , 32 , iIii1 + 'builderstoolbox.png' , iI111I11I1I1 , '' )
 oOOo0oo ( '[COLORgreen]SOURCE LIST[/COLOR]' , OooO0 , 46 , iIii1 + 'sources.png' , iI111I11I1I1 , '' )
 oOOo0oo ( '[COLORgreen]MAINTENANCE[/COLOR]' , OooO0 , 3 , iIii1 + 'MAIN6.png' , iI111I11I1I1 , '' )
 oOOo0oo ( '[COLORgreen]ADDONS[/COLOR]' , ( oOo0oooo00o ( 'aHR0cDovL21pcnJvcnMua29kaS50di9hZGRvbnMv' ) ) , 2030 , iIii1 + 'ADDONS.png' , iI111I11I1I1 , '' )
 oOOo0oo ( '[COLORgreen]APK TOOL[/COLOR]' , OooO0 , 2 , iIii1 + 'APK.png' , iI111I11I1I1 , '' )
 oOOo0oo ( '[COLORgreen]GenieTv RSS Feed[/COLOR]' , OooO0 , 39 , iIii1 + 'RSS.png' , iI111I11I1I1 , '' )
 oOOo0oo ( '[COLORgreen]ADDONS PACKS[/COLOR]' , OooO0 , 30 , iIii1 + 'ADDONP.png' , iI111I11I1I1 , '' )
 I11II1i ( 'movies' , 'MAIN' )
 if 23 - 23: ii11ii1ii / OOooOOo + o0000oOoOoO0o + o0000oOoOoO0o / OoOoOO00
def iiI1 ( ) :
 oOOo0oo ( '[COLORgreen]RESTORE MY BUILD[/COLOR]' , OooO0 , 49 , iIii1 + 'MB.png' , iI111I11I1I1 , '' )
 oOOo0oo ( '[COLORgreen]WIPE GENIE[/COLOR]' , OooO0 , 41 , iIii1 + 'wipegenie.png' , iI111I11I1I1 , '' )
 oOOo0oo ( '[COLORgreen]WISHES PC[/COLOR]' , OooO0 , 1 , iIii1 + 'WISHESPC.png' , iI111I11I1I1 , '' )
 oOOo0oo ( '[COLORgreen]WISHES ANDROID[/COLOR]' , OooO0 , 44 , iIii1 + 'WISHESAN.png' , iI111I11I1I1 , '' )
 I11II1i ( 'movies' , 'MAIN' )
def i11Iiii ( ) :
 oOOo0oo ( '[COLORgreen]SEARCH[/COLOR]' , OooO0 , 9000 , iIii1 + 'search.png' , iI111I11I1I1 , '' )
 oOOo0oo ( '[COLORgreen]DONATORS LIST[/COLOR]' , OooO0 + '/thelist.m3u' , 7080 , iIii1 + 'GTVIPTV.png' , iI111I11I1I1 , '' )
 oOOo0oo ( '[COLORgreen]POPCORN BOX[/COLOR]' , OooO0 , 7061 , iIii1 + 'popcorn.png' , iI111I11I1I1 , '' )
 oOOo0oo ( '[COLORgreen]DIZZY TV[/COLOR]' , '' , 10018 , iIii1 + 'dtv.png' , iI111I11I1I1 , '' )
 oOOo0oo ( '[COLORgreen]WATCH SERIES[/COLOR]' , '' , 10040 , iIii1 + 'WATCHSERIES.png' , iI111I11I1I1 , '' )
 oOOo0oo ( '[COLORgreen]RECENT EPISODES[/COLOR]' , OooO0 , 8081 , iIii1 + 'recent.png' , iI111I11I1I1 , '' )
 oOOo0oo ( '[COLORgreen]SCOOBY STREAMS[/COLOR]' , OooO0 , 1023 , iIii1 + 'scoob.png' , iI111I11I1I1 , '' )
 oOOo0oo ( '[COLORgreen]THE REAPER[/COLOR]' , ( oOo0oooo00o ( 'aHR0cDovL3RoZXJlYXBlci54MTBob3N0LmNvbS9UaGVfUmVhcGVycy9tYWluLnBocA==' ) ) , 1016 , iIii1 + 'reap.png' , iI111I11I1I1 , '' )
 oOOo0oo ( '[COLORgreen]PANDORAS BOX[/COLOR]' , OooO0 , 10025 , iIii1 + 'PANDORASBOX.png' , iI111I11I1I1 , '' )
 oOOo0oo ( '[COLORgreen]HEROVISION[/COLOR]' , 'http://herovision.x10host.com/vod/main.php' , 1016 , iIii1 + 'hero.png' , iI111I11I1I1 , '' )
 oOOo0oo ( '[COLORgreen]STAND UP[/COLOR]' , '' , 10003 , iIii1 + 'ORIGINSTANDUP.png' , iI111I11I1I1 , '' )
 oOOo0oo ( '[COLORgreen]FOOTBALL[/COLOR]' , '' , 10002 , iIii1 + 'ORIGINFOOTBALL.png' , iI111I11I1I1 , '' )
 oOOo0oo ( '[COLORgreen]FITNESS[/COLOR]' , ( oOo0oooo00o ( 'aHR0cHM6Ly93d3cuZml0bmVzc2JsZW5kZXIuY29tL3ZpZGVvcw==' ) ) , 7085 , iIii1 + 'FITNESS.png' , iI111I11I1I1 , '' )
 oOOo0oo ( '[COLORgreen]DOCUMENTARIES[/COLOR]' , OooO0 , 8040 , iIii1 + 'documentary.png' , iI111I11I1I1 , '' )
 oOOo0oo ( '[COLORgreen]CARTOONS[/COLOR]' , '' , 10001 , iIii1 + 'ORIGINCARTOON.png' , iI111I11I1I1 , '' )
 oOOo0oo ( '[COLORgreen]ANIME[/COLOR]' , OooO0 , 1001 , iIii1 + 'anime.png' , iI111I11I1I1 , '' )
 oOOo0oo ( '[COLORgreen]M3U STREAMS[/COLOR]' , OooO0 , 8070 , iIii1 + 'streams.png' , iI111I11I1I1 , '' )
 oOOo0oo ( '[COLORgreen]PLAYLIST LOADER[/COLOR]' , OooO0 , 3000 , iIii1 + 'loader.png' , iI111I11I1I1 , '' )
 if 23 - 23: OOooOOo . OoOoOO00
 if 98 - 98: iIii1I11I1II1 % I1IiI * ii11ii1ii * I1IiI
 if 45 - 45: O0oO . I1IiI
 if 83 - 83: OoOO . iIii1I11I1II1 . ii11ii1ii
 if 31 - 31: o00O0oo . o00O0oo - OOooOOo / Ooo00oOo00o + o0oO0 * OOOo0
 if 63 - 63: O0oO % i1IIi / OoooooooOO - OoooooooOO
 if 8 - 8: I1IiI
 if 60 - 60: o0000oOoOoO0o / o0000oOoOoO0o
 if 46 - 46: o00O0oo * OoOO0ooOOoo0O - Ooo00oOo00o * OoOO - O0oO
 if 83 - 83: OoooooooOO
 if 31 - 31: OoOoOO00 - OoOO0ooOOoo0O . O0oO % I1IiI - O0
 if 4 - 4: OoOoOO00 / o0oO0 . oO0o0ooO0
 if 58 - 58: OoOO0ooOOoo0O * i11iIiiIii / I1IiI % O0oO - ii11ii1ii / OoOO
 if 50 - 50: OOOo0
 if 34 - 34: OOOo0 * OoOoOO00 % oO0o0ooO0 * I1IiI - OOOo0
 I11II1i ( 'movies' , 'MAIN' )
 if 33 - 33: OOooOOo + OoOO0ooOOoo0O * Ooo00oOo00o - Oo / OoOO % o00O0oo
 if 21 - 21: Ooo00oOo00o * iIii1I11I1II1 % OoOO * i1IIi
def Ii11Ii1I ( ) :
 oOOo0oo ( '[COLORgreen]Cartoons[/COLOR]' , '' , 10001 , iIii1 + 'ORIGINCARTOON.png' , iI111I11I1I1 , '' )
 oOOo0oo ( '[COLORgreen]Dizzy TV[/COLOR]' , '' , 10018 , iIii1 + 'dtv.png' , iI111I11I1I1 , '' )
 oOOo0oo ( '[COLORgreen]Football[/COLOR]' , '' , 10002 , iIii1 + 'ORIGINFOOTBALL.png' , iI111I11I1I1 , '' )
 oOOo0oo ( '[COLORgreen]Izle Films[/COLOR]' , '' , 10030 , iIii1 + 'IZLEFILMS.png' , iI111I11I1I1 , '' )
 oOOo0oo ( '[COLORgreen]Stand Up[/COLOR]' , '' , 10003 , iIii1 + 'ORIGINSTANDUP.png' , iI111I11I1I1 , '' )
 if 72 - 72: oO0o0ooO0 / i1IIi * Oo - O0oO
 if 51 - 51: OoOoOO00 * Ooo00oOo00o % OOooOOo * OoOoOO00 % ii11ii1ii / o0oO0
def iIIIIii1 ( ) :
 oOOo0oo ( '[COLORgreen]SCOOBY STREAMS[/COLOR]' , ( oOo0oooo00o ( 'aHR0cDovL3Njb29ieXN0cmVhbS54MTBob3N0LmNvbS9zY29vYnkvdHZjYXRzLnBocA==' ) ) , 1016 , iIii1 + 'scoob.png' , iI111I11I1I1 , '' )
 oOOo0oo ( '[COLORgreen]SCOOBY SCRAPES[/COLOR]' , OooO0 , 1024 , iIii1 + 'scoob.png' , iI111I11I1I1 , '' )
 if 58 - 58: i11iIiiIii % o0000oOoOoO0o
def OO00Oo ( ) :
 oOOo0oo ( '[COLORgreen]Live Tv[/COLOR]' , OooO0 , 9021 , iIii1 + 'english.png' , iI111I11I1I1 , '' )
 oOOo0oo ( '[COLORgreen]XXX[/COLOR]' , OooO0 , 9022 , iIii1 + 'xxx.png' , iI111I11I1I1 , '' )
 oOOo0oo ( '[COLORgreen]Hd VOD[/COLOR]' , OooO0 , 9023 , iIii1 + 'vod(1).png' , iI111I11I1I1 , '' )
 if 51 - 51: IIII * OOooOOo + o0000oOoOoO0o + Ooo00oOo00o
 if 66 - 66: I1IiI
def oO000Oo000 ( ) :
 oOOo0oo ( '[COLORgreen]SEARCH MOVIES[/COLOR]' , OooO0 , 9001 , iIii1 + 'MOVIESv.png' , iI111I11I1I1 , '' )
 oOOo0oo ( '[COLORgreen]SEARCH SERIES[/COLOR]' , OooO0 , 9002 , iIii1 + 'TVSHOWSv.png' , iI111I11I1I1 , '' )
 oOOo0oo ( '[COLORgreen]SEARCH CARTOONS[/COLOR]' , '' , 10005 , iIii1 + 'ORIGINCARTOON' , iI111I11I1I1 , '' )
 oOOo0oo ( '[COLORgreen]SEARCH LiveTv[/COLOR]' , OooO0 , 9003 , iIii1 + 'livetv.png' , iI111I11I1I1 , '' )
 if 4 - 4: OoOO
 if 93 - 93: Ooo00oOo00o % OoOO . Ooo00oOo00o * O0oO % o00O0oo . OoOoOO00
def iI1ii1Ii ( ) :
 oOOo0oo ( '[COLORgreen]RADIO[/COLOR]' , OooO0 , 1013 , iIii1 + 'radio.png' , iI111I11I1I1 , '' )
 oOOo0oo ( '[COLORgreen]MUSIC[/COLOR]' , OooO0 , 1030 , iIii1 + 'MUSIC.png' , iI111I11I1I1 , '' )
 oOOo0oo ( '[COLORgreen]MUSIC ARCHIVE[/COLOR]' , OooO0 + ( oOo0oooo00o ( 'L3ZvZC91cmxzL211c2ljLnBocA==' ) ) , 1010 , iIii1 + 'MUSIC.png' , iI111I11I1I1 , '' )
 oOOo0oo ( '[COLORgreen]MUSIC SEARCH[/COLOR]' , OooO0 , 1111 , iIii1 + 'search.png' , iI111I11I1I1 , '' )
 oOOo0oo ( '[COLORgreen]AUDIO BOOKS[/COLOR]' , 'http://doremisa.com/audiobooks/' , 1006 , iIii1 + 'search.png' , iI111I11I1I1 , '' )
 if 92 - 92: I1IiI
 I11II1i ( 'movies' , 'MAIN' )
 if 26 - 26: oO0o0ooO0 . O0oO
def oOOOOo0 ( ) :
 iiII1i1 ( 'DELETE CACHE' , 'url' , 14 , iIii1 + 'MAIN5.png' , iI111I11I1I1 , '' )
 iiII1i1 ( 'DELETE PACKAGES' , 'url' , 6 , iIii1 + 'MAIN4.png' , iI111I11I1I1 , '' )
 iiII1i1 ( 'FORCE REFRESH' , 'url' , 10 , iIii1 + 'MAIN3.png' , iI111I11I1I1 , 'Force Refresh All Repos' )
 if 66 - 66: OoOO0ooOOoo0O - o0000oOoOoO0o
 iiII1i1 ( 'CHECK MY IP' , 'url' , 12 , iIii1 + 'MAIN2.png' , iI111I11I1I1 , '' )
 iiII1i1 ( 'ANDROID ONLY DELETE TEXTURE13.DB&THUBMNAIL FOLDER' , 'url' , 13 , iIii1 + 'MAIN1.png' , iI111I11I1I1 , 'Only Works On Android On Windows It Deletes Your Thumnails Folder But Does Not Delete The Textures13.db' )
 oOOo0oo ( '[COLORgreen]ADVANCED SETTINGS XML[/COLOR]' , OooO0 , 4 , iIii1 + 'XML.png' , iI111I11I1I1 , '' )
 oOOo0oo ( '[COLORgreen]URL FIXES[/COLOR]' , OooO0 , 20 , iIii1 + 'URLFIX.png' , iI111I11I1I1 , '' )
 I11II1i ( 'movies' , 'MAIN' )
 if 5 - 5: O0oO + o00O0oo / Oo - OoOO
 if 63 - 63: OoOO0ooOOoo0O % OoOO * OoOO * Ooo00oOo00o / ii11ii1ii
def o0ooO ( ) :
 oOOo0oo ( '[COLORgreen]REPOS[/COLOR]' , ( oOo0oooo00o ( 'aHR0cDovL21pcnJvcnMua29kaS50di9hZGRvbnMv' ) ) , 2030 , iIii1 + 'repos.png' , iI111I11I1I1 , '' )
 oOOo0oo ( '[COLORgreen]NEW[/COLOR]' , OooO0 , 22 , iIii1 + 'NEW.png' , iI111I11I1I1 , '' )
 oOOo0oo ( '[COLORgreen]IPTV[/COLOR]' , OooO0 , 23 , iIii1 + 'IPTV.png' , iI111I11I1I1 , '' )
 oOOo0oo ( '[COLORgreen]VIDEO[/COLOR]' , OooO0 , 24 , iIii1 + 'VIDEO.png' , iI111I11I1I1 , '' )
 oOOo0oo ( '[COLORgreen]SPORTS[/COLOR]' , OooO0 , 25 , iIii1 + 'SPORTS.png' , iI111I11I1I1 , '' )
 oOOo0oo ( '[COLORgreen]KIDS[/COLOR]' , OooO0 , 26 , iIii1 + 'KIDS.png' , iI111I11I1I1 , '' )
 oOOo0oo ( '[COLORgreen]MUSIC[/COLOR]' , OooO0 , 27 , iIii1 + 'MUSIC.png' , iI111I11I1I1 , '' )
 oOOo0oo ( '[COLORgreen]PROGRAMS[/COLOR]' , OooO0 , 28 , iIii1 + 'PROGRAMS.png' , iI111I11I1I1 , '' )
 oOOo0oo ( '[COLORgreen]XXX[/COLOR]' , 'URL' , 29 , iIii1 + 'XXX.png' , iI111I11I1I1 , '' )
 I11II1i ( 'movies' , 'MAIN' )
 if 98 - 98: oO0o0ooO0 * oO0o0ooO0 / oO0o0ooO0 + o0000oOoOoO0o
 if 34 - 34: o0oO0
def I1111I1iII11 ( ) :
 iiII1i1 ( 'CHECK ADVANCED XML' , OooO0 , 8 , iIii1 + 'XML.png' , iI111I11I1I1 , '' )
 iiII1i1 ( 'MUCKYS XML' , OooO0 + '/wizard/muckys.xml' , 7 , iIii1 + 'XML.png' , iI111I11I1I1 , '' )
 iiII1i1 ( '0CACHE XML' , OooO0 + '/wizard/0cache.xml' , 7 , iIii1 + 'XML.png' , iI111I11I1I1 , '' )
 iiII1i1 ( 'MIKEY1234 XML' , OooO0 + '/wizard/mikey.xml' , 7 , iIii1 + 'XML.png' , iI111I11I1I1 , '' )
 iiII1i1 ( 'TUXENS XML' , OooO0 + '/wizard/tuxens.xml' , 7 , iIii1 + 'XML.png' , iI111I11I1I1 , '' )
 iiII1i1 ( 'P2P RECOMMENDED XML1' , OooO0 + '/wizard/p2p1.xml' , 7 , iIii1 + 'XML.png' , iI111I11I1I1 , '' )
 iiII1i1 ( 'P2P RECOMMENDED XML2' , OooO0 + '/wizard/p2p2.xml' , 7 , iIii1 + 'XML.png' , iI111I11I1I1 , '' )
 iiII1i1 ( 'DELETE XML' , OooO0 , 11 , iIii1 + 'XML.png' , iI111I11I1I1 , '' )
 I11II1i ( 'movies' , 'MAIN' )
 if 59 - 59: iIii1I11I1II1 * i11iIiiIii / ii11ii1ii * i1IIi * O0
def OOo0o ( ) :
 iiII1i1 ( '[COLORgreen]My Local Zip[/COLOR]' , oo0o0O00 , 48 , iIii1 + 'MB.png' , iI111I11I1I1 , '' )
 iiII1i1 ( '[COLORgreen]My Online Zip[/COLOR]' , oO0o0o0ooO0oO , 43 , iIii1 + 'MB.png' , iI111I11I1I1 , '' )
 if 50 - 50: IIII
def i11I1iIiII ( ) :
 iiII1i1 ( 'INSTALL FTV GUIDE AND OTHER ADDONS REQUIRED' , OooO0 + '/wizard/customftv/ftvguide-addons.zip' , 5 , iIii1 + 'FTV4.png' , iI111I11I1I1 , '' )
 iiII1i1 ( 'FTV GUIDE FIRST RUN SETTINGS' , OooO0 + '/wizard/customftv/settings.xml' , 17 , iIii1 + 'FTV3.png' , iI111I11I1I1 , '' )
 iiII1i1 ( 'FTV GUIDE ADDONS2.INI UPDATE DAILY' , 'http://ren.byethost12.com/addons2.ini' , 16 , iIii1 + 'FTV1.png' , iI111I11I1I1 , '' )
 iiII1i1 ( 'RESET FTV DATABASE' , 'url' , 18 , iIii1 + 'FTV2.png' , iI111I11I1I1 , '' )
 if 96 - 96: Oo
 if 45 - 45: O0 * OOooOOo % Oo * OoooooooOO + oO0o0ooO0 . I1IiI
 if 67 - 67: i11iIiiIii - i1IIi % ii11ii1ii . O0
def o0oo ( ) :
 oOOo0oo ( '[COLORgreen]SKINS[/COLOR]' , OooO0 , 33 , iIii1 + 'skinp.png' , iI111I11I1I1 , '' )
 oOOo0oo ( '[COLORgreen]ARTWORK PACKS[/COLOR]' , OooO0 , 34 , iIii1 + 'artp.png' , iI111I11I1I1 , '' )
 oOOo0oo ( '[COLORgreen]CREATE UNIVERSAL PATHS[/COLOR]' , ii11iIi1I , 35 , iIii1 + 'GUI.png' , iI111I11I1I1 , '' )
 I11II1i ( 'movies' , 'MAIN' )
 if 91 - 91: IIII
def iiIii ( url ) :
 ooo0O = oOoO0o00OO0 ( i1I1ii ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 oOOo0 = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( ooo0O )
 for oo00O00oO , url , iIiIIIi , ooo00OOOooO , O00OOOoOoo0O in oOOo0 :
  oOOo0oo ( oo00O00oO , url , 5 , iIiIIIi , ooo00OOOooO , O00OOOoOoo0O )
 I11II1i ( 'movies' , 'MAIN' )
 if 77 - 77: oO0o0ooO0 % oO0o0ooO0 * OoOO - i11iIiiIii
def Oo0oO ( ) :
 oOOo0oo ( '[COLORgreen]GOTHAM SKINS[/COLOR]' , OooO0 , 36 , iIii1 + 'GSKIN.png' , iI111I11I1I1 , '' )
 oOOo0oo ( '[COLORgreen]HELIX SKINS[/COLOR]' , OooO0 , 37 , iIii1 + 'HSKIN.png' , iI111I11I1I1 , '' )
 oOOo0oo ( '[COLORgreen]ISENGAARD SKINS[/COLOR]' , ii11iIi1I , 38 , iIii1 + 'ISKIN.png' , iI111I11I1I1 , '' )
 I11II1i ( 'movies' , 'MAIN' )
 if 1 - 1: Ooo00oOo00o - OoOO . o0000oOoOoO0o . Ooo00oOo00o / Oo + o0000oOoOoO0o
def OooOOOOo ( url ) :
 ooo0O = oOoO0o00OO0 ( OooO0 + oo0O0oO ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 oOOo0 = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( ooo0O )
 for oo00O00oO , url , iIiIIIi , ooo00OOOooO , O00OOOoOoo0O in oOOo0 :
  oOOo0oo ( oo00O00oO , url , 42 , iIiIIIi , ooo00OOOooO , O00OOOoOoo0O )
 I11II1i ( 'movies' , 'MAIN' )
 if 60 - 60: OOOo0
def iii1i ( url ) :
 ooo0O = oOoO0o00OO0 ( OooO0 + I11i1ii1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 oOOo0 = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( ooo0O )
 for oo00O00oO , url , iIiIIIi , ooo00OOOooO , O00OOOoOoo0O in oOOo0 :
  oOOo0oo ( oo00O00oO , url , 42 , iIiIIIi , ooo00OOOooO , O00OOOoOoo0O )
 I11II1i ( 'movies' , 'MAIN' )
 if 87 - 87: o0000oOoOoO0o - iIii1I11I1II1 + OOOo0 . oO0o0ooO0
def Oo0oOOOoOooOo ( url ) :
 ooo0O = oOoO0o00OO0 ( OooO0 + O000oo ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 oOOo0 = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( ooo0O )
 for oo00O00oO , url , iIiIIIi , ooo00OOOooO , O00OOOoOoo0O in oOOo0 :
  oOOo0oo ( oo00O00oO , url , 42 , iIiIIIi , ooo00OOOooO , O00OOOoOoo0O )
 I11II1i ( 'movies' , 'MAIN' )
 if 20 - 20: OoOO0ooOOoo0O % o00O0oo / o00O0oo + o00O0oo
def III1IiiI ( url ) :
 ooo0O = oOoO0o00OO0 ( oOo0oooo00o ( 'aHR0cHM6Ly9kbC5kcm9wYm94dXNlcmNvbnRlbnQuY29tL3MvN2ZrMjhndDlwb3QxMjJhL0JVSUxEUy50eHQ/ZGw9MA==' ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 oOOo0 = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( ooo0O )
 for oo00O00oO , url , iIiIIIi , ooo00OOOooO , O00OOOoOoo0O in oOOo0 :
  oOOo0oo ( oo00O00oO , url , 42 , iIiIIIi , ooo00OOOooO , O00OOOoOoo0O )
 I11II1i ( 'movies' , 'MAIN' )
 if 31 - 31: OOooOOo . OOOo0
def ii11IIII11I ( url ) :
 ooo0O = oOoO0o00OO0 ( OooO0 + OOooo ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 oOOo0 = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( ooo0O )
 for oo00O00oO , url , iIiIIIi , ooo00OOOooO , O00OOOoOoo0O in oOOo0 :
  oOOo0oo ( oo00O00oO , url , 40 , iIiIIIi , ooo00OOOooO , O00OOOoOoo0O )
 I11II1i ( 'movies' , 'MAIN' )
 if 90 - 90: OOooOOo % i1IIi / Ooo00oOo00o
def IIi ( url ) :
 ooo0O = oOoO0o00OO0 ( OooO0 + i1Iii1i1I ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 oOOo0 = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( ooo0O )
 for oo00O00oO , url , iIiIIIi , ooo00OOOooO , O00OOOoOoo0O in oOOo0 :
  oOOo0oo ( oo00O00oO , url , 5 , iIiIIIi , ooo00OOOooO , O00OOOoOoo0O )
 I11II1i ( 'movies' , 'MAIN' )
 if 91 - 91: ii11ii1ii + OOOo0 . OoOO0ooOOoo0O * ii11ii1ii + OOOo0 * Oo
def O000OOOOOo ( ) :
 Iiii1i1 = OO ( oOo0oooo00o ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vYXBrdG9vbC9hcGsucGhw' ) )
 oOOo0 = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( Iiii1i1 )
 for oo000o , iiIi1IIi1I , oo00O00oO in oOOo0 :
  o0OoOO000ooO0 ( oo00O00oO , oo000o , 2031 , iIii1 + 'APK.png' )
  if 56 - 56: oO0o0ooO0
def oo0oO0oOOoo ( name , url , description ) :
 oOo00O0oo00o0 = xbmc . translatePath ( os . path . join ( ii , 'Download' ) )
 i1111 = xbmcgui . DialogProgress ( )
 i1111 . create ( "Your App Is Downloading" , "Why not check out our website" , '' , 'Http://architects.x10host.com' )
 OOooooO0Oo = os . path . join ( oOo00O0oo00o0 , name + '.apk' )
 try :
  os . remove ( OOooooO0Oo )
 except :
  pass
 downloader . download ( url , OOooooO0Oo , i1111 )
 i1iIIi1 = xbmcgui . Dialog ( )
 i1iIIi1 . ok ( "GenieTv" , "[COLORred]Please press ok, exit kodi and go to your downloads folder to install your app[/COLOR]" , "[COLORblue]Tool Brought To You By Architects@Work[/COLOR]" )
 if 91 - 91: OOooOOo . iIii1I11I1II1 / OoOO + i1IIi
def I1i ( url ) :
 oOo00O0oo00o0 = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/resources/downloads' ) )
 i1111 = xbmcgui . DialogProgress ( )
 i1111 . create ( "Your fILM Is Downloading" , "Why not check out our website" , '' , 'Http://architects.x10host.com' )
 OOooooO0Oo = os . path . join ( oOo00O0oo00o0 , oo00O00oO + '.mp4' )
 try :
  os . remove ( OOooooO0Oo )
 except :
  pass
 downloader . download ( url , OOooooO0Oo , i1111 )
 i1iIIi1 = xbmcgui . Dialog ( )
 i1iIIi1 . ok ( "GenieTv" , "[COLORred]Please press ok, Your download With Be Avaiilable Via The My Downloads Button[/COLOR]" , "[COLORblue]Tool Brought To You By Architects@Work[/COLOR]" )
 if 53 - 53: ii11ii1ii * I1IiI + o0oO0 - OoOoOO00
 if 2 - 2: o0000oOoOoO0o + o00O0oo - OOOo0 % OOooOOo . oO0o0ooO0
def I1I1i1I ( name , url , description ) :
 oOo00O0oo00o0 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 i1111 = xbmcgui . DialogProgress ( )
 i1111 . create ( "Your Art Pack Is Downloading" , "Why not check out our website" , '' , 'Http://architects.x10host.com' )
 OOooooO0Oo = os . path . join ( oOo00O0oo00o0 , name )
 try :
  os . remove ( OOooooO0Oo )
 except :
  pass
 downloader . download ( url , OOooooO0Oo , i1111 )
 ii1I = xbmc . translatePath ( os . path . join ( i1 ) )
 time . sleep ( 2 )
 i1111 . update ( 0 , "" , "Placing Your Art Please Wait" )
 print '======================================='
 print ii1I
 print '======================================='
 extract . all ( OOooooO0Oo , ii1I , i1111 )
 i1iIIi1 = xbmcgui . Dialog ( )
 i1iIIi1 . ok ( "GenieTv" , "[COLORred]Once complete your artwork will be stored in your Media folder, Accessible via the Homefolder, Enjoy[/COLOR]" )
 if 99 - 99: o00O0oo / Oo / IIII % OOOo0
 if 13 - 13: o0000oOoOoO0o * Oo * o0oO0
def iI11iI1IiiIiI ( url ) :
 ooo0O = oOoO0o00OO0 ( oOo0oooo00o ( 'aHR0cDovL2dlbmlldHYuYXJjaGl0ZWN0cy54MTBob3N0LmNvbS90ZXN0L3doLnR4dA==' ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 oOOo0 = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( ooo0O )
 for oo00O00oO , url , iIiIIIi , ooo00OOOooO , O00OOOoOoo0O in oOOo0 :
  oOOo0oo ( oo00O00oO , url , 5 , iIiIIIi , ooo00OOOooO , O00OOOoOoo0O )
 try :
  ooo0O = oOoO0o00OO0 ( Ii1I1i + oooOOOOO + OOI1iI1ii1II ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
  oOOo0 = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( ooo0O )
  for oo00O00oO , url , iIiIIIi , ooo00OOOooO , O00OOOoOoo0O in oOOo0 :
   oOOo0oo ( oo00O00oO , url , 5 , iIiIIIi , ooo00OOOooO , O00OOOoOoo0O )
 except : pass
 I11II1i ( 'movies' , 'INFO' )
 if 57 - 57: O0oO % o00O0oo + OOooOOo - Oo
 if 65 - 65: o0000oOoOoO0o . I1IiI
def IiI1i ( url ) :
 ooo0O = oOoO0o00OO0 ( oOo0oooo00o ( 'aHR0cDovL2dlbmlldHYuYXJjaGl0ZWN0cy54MTBob3N0LmNvbS90ZXN0L3doLnR4dA==' ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 oOOo0 = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( ooo0O )
 for oo00O00oO , url , iIiIIIi , ooo00OOOooO , O00OOOoOoo0O in oOOo0 :
  oOOo0oo ( oo00O00oO , url , 43 , iIiIIIi , ooo00OOOooO , O00OOOoOoo0O )
 try :
  ooo0O = oOoO0o00OO0 ( Ii1I1i + oooOOOOO + OOI1iI1ii1II ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
  oOOo0 = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( ooo0O )
  for oo00O00oO , url , iIiIIIi , ooo00OOOooO , O00OOOoOoo0O in oOOo0 :
   oOOo0oo ( oo00O00oO , url , 43 , iIiIIIi , ooo00OOOooO , O00OOOoOoo0O )
 except : pass
 I11II1i ( 'movies' , 'INFO' )
 if 92 - 92: IIII . IIII + Ooo00oOo00o
 if 9 - 9: OOOo0 * O0 + IIII - o0000oOoOoO0o * O0oO
def Oooo0oOO ( name , url , description ) :
 oOo00O0oo00o0 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 i1111 = xbmcgui . DialogProgress ( )
 i1111 . create ( "GenieTv" , "Downloading Content" , '' , 'Please Wait' )
 OOooooO0Oo = os . path . join ( oOo00O0oo00o0 , name + '.zip' )
 try :
  os . remove ( OOooooO0Oo )
 except :
  pass
 downloader . download ( url , OOooooO0Oo , i1111 )
 Ooo00O00o = xbmc . translatePath ( os . path . join ( 'special://home' , 'addons' ) )
 time . sleep ( 2 )
 i1111 . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print Ooo00O00o
 print '======================================='
 extract . all ( OOooooO0Oo , Ooo00O00o , i1111 )
 i1iIIi1 = xbmcgui . Dialog ( )
 i1iIIi1 . ok ( "GenieTv" , "Press ok to finish install" , "[COLOR yellow]Brought To You By Architects@Work[/COLOR]" )
 O0O00Oo ( )
 if 97 - 97: O0 * OoooooooOO . OoooooooOO
 if 33 - 33: O0oO + oO0o0ooO0 * OoOO / iIii1I11I1II1 - OOOo0
def O0oOOO0ooOOO0OOO ( name , url , description ) :
 oOo00O0oo00o0 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 i1111 = xbmcgui . DialogProgress ( )
 i1111 . create ( "GenieTv" , "Downloading " , '' , 'Please Wait' )
 OOooooO0Oo = os . path . join ( oOo00O0oo00o0 , 'plugin.program.GenieTv.install' + '.zip' )
 try :
  os . remove ( OOooooO0Oo )
 except :
  pass
 downloader . download ( url , OOooooO0Oo , i1111 )
 Ooo00O00o = xbmc . translatePath ( os . path . join ( 'special://' , 'home' ) )
 time . sleep ( 2 )
 i1111 . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print Ooo00O00o
 print '======================================='
 extract . all ( OOooooO0Oo , Ooo00O00o , i1111 )
 i1iIIi1 = xbmcgui . Dialog ( )
 i1iIIi1 . ok ( "GenieTv" , "Press ok to force close kodi, if unsuccessful using windows Please kill kodi via taskmanager" , "[COLOR yellow]Brought To You By Architects@Work[/COLOR]" )
 oO00oooOOoOo0 ( )
 if 74 - 74: iIii1I11I1II1 * ii11ii1ii + I1IiI / i1IIi / OoOoOO00 . Oo
def oooOo0OOOoo0 ( name , url , description ) :
 oOo00O0oo00o0 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 i1111 = xbmcgui . DialogProgress ( )
 i1111 . create ( "GenieTv" , "Downloading " , '' , 'Please Wait' )
 OOooooO0Oo = os . path . join ( oOo00O0oo00o0 , 'plugin.program.GenieTv.install' + '.zip' )
 try :
  os . remove ( OOooooO0Oo )
 except :
  pass
 downloader . download ( url , OOooooO0Oo , i1111 )
 Ooo00O00o = xbmc . translatePath ( os . path . join ( 'special://' , 'home' ) )
 time . sleep ( 2 )
 i1111 . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print Ooo00O00o
 print '======================================='
 extract . all ( OOooooO0Oo , Ooo00O00o , i1111 )
 i1iIIi1 = xbmcgui . Dialog ( )
 i1iIIi1 . ok ( "GenieTv" , "Please Disconnect The Power From Your Device. DO NOT EXIT CLEANLY VIA SHUTDOWN" , "[COLOR yellow]Brought To You By Architects@Work[/COLOR]" )
 if 51 - 51: Oo / I1IiI . OoOO0ooOOoo0O * OOooOOo + Ooo00oOo00o * IIII
 if 73 - 73: Ooo00oOo00o + OoooooooOO - O0 - o00O0oo - OoOoOO00
def O0O ( name , url , description ) :
 Ooo00O00o = xbmc . translatePath ( os . path . join ( 'special://' , 'home' ) )
 i1111 = xbmcgui . DialogProgress ( )
 OOooooO0Oo = os . path . join ( oo0o0O00 )
 time . sleep ( 2 )
 i1111 . create ( "GenieTv" , "Restoring" , '' , 'Please Wait' )
 print '======================================='
 print Ooo00O00o
 print '======================================='
 extract . all ( OOooooO0Oo , Ooo00O00o , i1111 )
 i1iIIi1 = xbmcgui . Dialog ( )
 i1iIIi1 . ok ( "GenieTv" , "Please Disconnect The Power From Your Device. DO NOT EXIT CLEANLY VIA SHUTDOWN" , "[COLOR yellow]Brought To You By Architects@Work[/COLOR]" )
 if 80 - 80: o00O0oo * OOooOOo / OOooOOo
 if 5 - 5: OOOo0
def oO00oooOOoOo0 ( ) :
 iIiIi11iI = xbmcgui . Dialog ( ) . yesno ( 'Force Close Kodi' , 'You are about to close Kodi' , 'Would you like to continue?' , nolabel = 'No, Cancel' , yeslabel = 'Yes, Close' )
 if iIiIi11iI == 0 :
  return
 elif iIiIi11iI == 1 :
  pass
 Oo0O00O000 = i11I1IiII1i1i ( )
 print "Platform: " + str ( Oo0O00O000 )
 if Oo0O00O000 == 'osx' :
  print "############   try osx force close  #################"
  try : os . system ( 'killall -9 XBMC' )
  except : pass
  try : os . system ( 'killall -9 Kodi' )
  except : pass
  i1iIIi1 . ok ( "[COLOR=red][B]WARNING  !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu." , '' )
 elif Oo0O00O000 == 'linux' :
  print "############   try linux force close  #################"
  try : os . system ( 'killall XBMC' )
  except : pass
  try : os . system ( 'killall Kodi' )
  except : pass
  try : os . system ( 'killall -9 xbmc.bin' )
  except : pass
  try : os . system ( 'killall -9 kodi.bin' )
  except : pass
  i1iIIi1 . ok ( "[COLOR=red][B]WARNING  !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu." , '' )
 elif Oo0O00O000 == 'android' :
  print "############   try android force close  #################"
  try : os . system ( 'adb shell am force-stop org.xbmc.kodi' )
  except : pass
  try : os . system ( 'adb shell am force-stop org.kodi' )
  except : pass
  try : os . system ( 'adb shell am force-stop org.xbmc.xbmc' )
  except : pass
  try : os . system ( 'adb shell am force-stop org.xbmc' )
  except : pass
  i1iIIi1 . ok ( "[COLOR=red][B]WARNING  !!![/COLOR][/B]" , "Your system has been detected as Android, you " , "[COLOR=yellow][B]MUST[/COLOR][/B] force close XBMC/Kodi. [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu." , "Pulling the power cable is the simplest method to force close." )
 elif Oo0O00O000 == 'windows' :
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
  i1iIIi1 . ok ( "[COLOR=red][B]WARNING  !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu." , "Use task manager and NOT ALT F4" )
 else :
  print "############   try atv force close  #################"
  try : os . system ( 'killall AppleTV' )
  except : pass
  print "############   try raspbmc force close  #################"
  try : os . system ( 'sudo initctl stop kodi' )
  except : pass
  try : os . system ( 'sudo initctl stop xbmc' )
  except : pass
  i1iIIi1 . ok ( "[COLOR=red][B]WARNING  !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit via the menu." , "Your platform could not be detected so just pull the power cable." )
  if 95 - 95: i11iIiiIii
def i11I1IiII1i1i ( ) :
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
  if 32 - 32: OoOO0ooOOoo0O
  if 42 - 42: IIII * O0 % i1IIi . OoOO0ooOOoo0O / OOooOOo
  if 32 - 32: OOOo0 * Oo
def O0OooOo0o ( url ) :
 i1111 . create ( "[COLOR=green]GenieTv[/COLOR]" , "Renaming paths..." , '' , 'Please Wait' )
 for iiI11ii1I1 , Ooo0OOoOoO0 , oOo0OOoO0 in os . walk ( url ) :
  for file in oOo0OOoO0 :
   if file . endswith ( ".xml" ) :
    i1111 . update ( 0 , "Fixing" , file , 'Please Wait' )
    IIo0Oo0oO0oOO00 = open ( ( os . path . join ( iiI11ii1I1 , file ) ) ) . read ( )
    oo00OO0000oO = IIo0Oo0oO0oOO00 . replace ( ii11iIi1I , 'special://home/' )
    I1II1 = open ( ( os . path . join ( iiI11ii1I1 , file ) ) , mode = 'w' )
    I1II1 . write ( str ( oo00OO0000oO ) )
    I1II1 . close ( )
 oO00oooOOoOo0 ( )
 if 86 - 86: iIii1I11I1II1 / I1IiI . OoOoOO00
def II1i111Ii1i ( ) :
 Iiii1i1 = OO ( oOo0oooo00o ( 'aHR0cDovL3d3dy5saXN0ZW5saXZlLmV1L3VrLmh0bWw=' ) )
 oOOo0 = re . compile ( '<tr>.+?<td><a href=".+?"><b>(.+?)</b>.+?<td><a href="(.+?)">' , re . DOTALL ) . findall ( Iiii1i1 )
 for oo00O00oO , oo000o in oOOo0 :
  iii1 ( oo00O00oO , oo000o , 222 , iIii1 + 'radio.png' )
  if 96 - 96: i11iIiiIii % OoOO0ooOOoo0O
def ooO ( ) :
 Iiii1i1 = OO ( oOo0oooo00o ( 'aHR0cDovL3d3dy50b29uamV0LmNvbS8=' ) )
 oOOo0 = re . compile ( '<a href="(.+?)" style="font-size:.8em;">(.+?)</a>' ) . findall ( Iiii1i1 )
 for oo000o , oo00O00oO in oOOo0 :
  o0OoOO000ooO0 ( '[COLORgreen]' + oo00O00oO + '[/COLOR]' , 'http://www.toonjet.com/' + oo000o , 8051 , iIii1 + 'classictoons.png' )
def Ooo0oOooo0 ( url ) :
 Iiii1i1 = OO ( url )
 oOOo0 = re . compile ( '<a href="(.+?)"><img src="(.+?)"' ) . findall ( Iiii1i1 )
 oOOOoo00 = re . compile ( '<a href="(.+?)">.+?</a></td></tr></table>' ) . findall ( Iiii1i1 )
 for url , iiIiIIIiiI in oOOo0 :
  if 'ol.gif' in iiIiIIIiiI :
   pass
  elif 'link_block_' in iiIiIIIiiI :
   pass
  elif '.png' in iiIiIIIiiI :
   pass
  else :
   o0OoOO000ooO0 ( ( iiIiIIIiiI ) . replace ( 'http://www.toonjet.com/images/icons/' , '' ) . replace ( 'images/icons/' , '' ) . replace ( '.jpg' , '' ) . replace ( '_icon' , '' ) . replace ( '_' , ' ' ) , 'http://www.toonjet.com/' + url , 8052 , iIii1 + 'vod.png' )
 for url in oOOOoo00 :
  o0OoOO000ooO0 ( 'NEXT PAGE' , 'http://www.toonjet.com/' + url , 8051 , iIii1 + 'documentary.png' )
def iiI1IIIi ( url ) :
 Iiii1i1 = OO ( url )
 oOOo0 = re . compile ( '<iframe width="640" height="480" src="(.+?)" frameborder="0" allowfullscreen></iframe>' ) . findall ( Iiii1i1 )
 for url in oOOo0 :
  iii1 ( '[COLORgreen]PLAY[/COLOR]' , ( url ) . replace ( 'http://www.youtube.com/embed/' , '' ) . replace ( '?autoplay=0' , '' ) , 8043 , iIii1 + 'classictoons.png' )
  if 47 - 47: Oo % o0000oOoOoO0o % i11iIiiIii - O0 + o0oO0
  if 94 - 94: O0oO
  if 4 - 4: o00O0oo % OoOO * Ooo00oOo00o
def o0O0OOOOoOO0 ( ) :
 if 23 - 23: i11iIiiIii
 oOOo0oo ( '[COLORgreen]Cartoons[/COLOR]' , '' , 10004 , iIii1 + 'ORIGINCARTOON.png' , iI111I11I1I1 , '' )
 oOOo0oo ( '[COLORgreen]Search Cartoons[/COLOR]' , '' , 10005 , iIii1 + 'ORIGINCARTOON.png' , iI111I11I1I1 , '' )
 if 30 - 30: OOooOOo - i1IIi % OoOoOO00 + o0000oOoOoO0o * iIii1I11I1II1
def o0ooooO0o0O ( ) :
 iiIi11iI1iii = Oo0o0000o0o0 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oo000 = iiIi11iI1iii . lower ( )
 o0000oO = oOoO0o00OO0 ( oOo0oooo00o ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2NhcnRvb24=' ) )
 oOOo0 = re . compile ( '<td><a href="(.+?)">(.+)</a></td>' ) . findall ( o0000oO )
 for oo000o , oo00O00oO in oOOo0 :
  if iiIi11iI1iii in oo00O00oO . lower ( ) :
   if 'Dad!' in oo00O00oO :
    pass
   elif 'Family Guy' in oo00O00oO :
    pass
   elif '2 Stupid' in oo00O00oO :
    pass
   elif 'The Zelfs' in oo00O00oO :
    pass
   elif 'A Clone' in oo00O00oO :
    pass
   elif 'A.T.O.M' in oo00O00oO :
    pass
   elif 'Almost Naked' in oo00O00oO :
    pass
   elif 'Angry Kid' in oo00O00oO :
    pass
   elif 'Annoying Orange' in oo00O00oO :
    pass
   elif 'Aqua Teen' in oo00O00oO :
    pass
   elif 'Assy Mcgee' in oo00O00oO :
    pass
   elif 'Astroblast' in oo00O00oO :
    pass
   elif 'Atomic Betty' in oo00O00oO :
    pass
   elif 'Axe Cop' in oo00O00oO :
    pass
   elif 'Baby Playpen' in oo00O00oO :
    pass
   elif 'Beavis and Butt' in oo00O00oO :
    pass
   elif 'Celebrity Deathmatch' in oo00O00oO :
    pass
   elif 'Clerks The' in oo00O00oO :
    pass
   elif 'Crapston Villas' in oo00O00oO :
    pass
   elif 'Duckman:' in oo00O00oO :
    pass
   elif 'Stripperella' in oo00O00oO :
    pass
   elif 'Vixen' in oo00O00oO :
    pass
   else :
    oOOo0oo ( '[COLORgreen]' + oo00O00oO + '[/COLOR]' , oo000o , 10006 , iIii1 + 'ORIGINCARTOON.png' , iI111I11I1I1 , '' )
  xbmcplugin . addSortMethod ( Oo00OOOOO , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 15 - 15: I1IiI % OOOo0 * o0000oOoOoO0o
def O0OoooO0 ( ) :
 Iiii1i1 = oOoO0o00OO0 ( oOo0oooo00o ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2NhcnRvb24=' ) )
 oOOo0 = re . compile ( '<td><a href="(.+?)">(.+)</a></td>' ) . findall ( Iiii1i1 )
 for oo000o , oo00O00oO in oOOo0 :
  if 'Dad!' in oo00O00oO :
   pass
  elif 'Family Guy' in oo00O00oO :
   pass
  elif '2 Stupid' in oo00O00oO :
   pass
  elif 'The Zelfs' in oo00O00oO :
   pass
  elif 'A Clone' in oo00O00oO :
   pass
  elif 'A.T.O.M' in oo00O00oO :
   pass
  elif 'Almost Naked' in oo00O00oO :
   pass
  elif 'Angry Kid' in oo00O00oO :
   pass
  elif 'Annoying Orange' in oo00O00oO :
   pass
  elif 'Aqua Teen' in oo00O00oO :
   pass
  elif 'Assy Mcgee' in oo00O00oO :
   pass
  elif 'Astroblast' in oo00O00oO :
   pass
  elif 'Atomic Betty' in oo00O00oO :
   pass
  elif 'Axe Cop' in oo00O00oO :
   pass
  elif 'Baby Playpen' in oo00O00oO :
   pass
  elif 'Beavis and Butt' in oo00O00oO :
   pass
  elif 'Celebrity Deathmatch' in oo00O00oO :
   pass
  elif 'Clerks The' in oo00O00oO :
   pass
  elif 'Crapston Villas' in oo00O00oO :
   pass
  elif 'Duckman:' in oo00O00oO :
   pass
  elif 'Stripperella' in oo00O00oO :
   pass
  elif 'Vixen' in oo00O00oO :
   pass
  else :
   oOOo0oo ( '[COLORgreen]' + oo00O00oO + '[/COLOR]' , oo000o , 10006 , iIii1 + 'ORIGINCARTOON.png' , iI111I11I1I1 , '' )
 xbmcplugin . addSortMethod ( Oo00OOOOO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 85 - 85: o0000oOoOoO0o
def iI1i11II1i ( url ) :
 Iiii1i1 = oOoO0o00OO0 ( url )
 oOOOoo00 = re . compile ( '<img src="(.+?)" id="series_image" width="250" height="370" alt=".+?" />' ) . findall ( Iiii1i1 )
 for iiIiIIIiiI in oOOOoo00 :
  o0o0OoOo0O0OO = iiIiIIIiiI
 iIi1I11I = re . compile ( '<li><a href="(.+?)">Next</a></li>' ) . findall ( Iiii1i1 )
 for url in iIi1I11I :
  oOOo0oo ( '[COLORgreen]NEXT PAGE[/COLOR]' , url , 10007 , o0o0OoOo0O0OO , iI111I11I1I1 , '' )
 oOOo0 = re . compile ( '&nbsp;<a href="(.+?)">(.+?)</a>' ) . findall ( Iiii1i1 )
 for url , oo00O00oO in oOOo0 :
  iii1 ( '[COLORgreen]' + oo00O00oO + '[/COLOR]' , url , 10007 , o0o0OoOo0O0OO )
  if 42 - 42: iIii1I11I1II1 / O0oO / Ooo00oOo00o - OoooooooOO
  if 33 - 33: I1IiI * OoOO0ooOOoo0O - OoOoOO00
 xbmcplugin . addSortMethod ( Oo00OOOOO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 83 - 83: I1IiI - o00O0oo / o0000oOoOoO0o / O0oO + OoOO - O0
def I11I1i1iIII1I ( url , IMAGE ) :
 Iiii1i1 = oOoO0o00OO0 ( url )
 oOOo0 = re . compile ( '"playlist">(.+?)</span></div><div><iframe src="(.+?)"' ) . findall ( Iiii1i1 )
 for oo00O00oO , url in oOOo0 :
  print oo00O00oO + '     ' + url
  if 'easy' in url :
   iI ( url )
   if 2 - 2: o0oO0 / oO0o0ooO0 . oO0o0ooO0 % O0oO
   if 11 - 11: iIii1I11I1II1
  xbmcplugin . addSortMethod ( Oo00OOOOO , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 20 - 20: OoOoOO00 % Oo + ii11ii1ii + o0oO0
def iI ( url ) :
 Iiii1i1 = oOoO0o00OO0 ( url )
 oOOo0 = re . compile ( "url: '(.+?)'," ) . findall ( Iiii1i1 )
 for url in oOOo0 :
  II11iIIiiiII ( url )
  if 79 - 79: O0 * i11iIiiIii - IIII / IIII
  if 48 - 48: O0
  if 93 - 93: i11iIiiIii - OOOo0 * ii11ii1ii * o0000oOoOoO0o % O0 + OoooooooOO
def I1i1i1 ( ) :
 if 73 - 73: O0 * oO0o0ooO0 + o00O0oo + o0oO0
 oOOo0oo ( '[COLORgreen]Genres[/COLOR]' , '' , 10032 , iIii1 + 'IZLEFILMS.png' , iI111I11I1I1 , '' )
 oOOo0oo ( '[COLORgreen]Popular Movies[/COLOR]' , '' , 10033 , iIii1 + 'IZLEFILMS.png' , iI111I11I1I1 , '' )
 oOOo0oo ( '[COLORgreen]Boxsets[/COLOR]' , '' , 10034 , iIii1 + 'IZLEFILMS.png' , iI111I11I1I1 , '' )
 oOOo0oo ( '[COLORgreen]Search[/COLOR]' , '' , 10035 , iIii1 + 'IZLEFILMS.png' , iI111I11I1I1 , '' )
if 40 - 40: OoOoOO00 . I1IiI * O0oO + OoOO0ooOOoo0O + OoOO0ooOOoo0O
if 9 - 9: o0000oOoOoO0o % OoooooooOO . OoOO % o0000oOoOoO0o
if 32 - 32: i11iIiiIii
if 31 - 31: iIii1I11I1II1 / Ooo00oOo00o / ii11ii1ii
if 41 - 41: Oo
if 10 - 10: Oo / Oo / O0oO . O0oO
if 98 - 98: Oo / OOOo0 . O0 + Ooo00oOo00o
if 43 - 43: OoOoOO00 . OoOO / ii11ii1ii
if 20 - 20: OOOo0
if 95 - 95: oO0o0ooO0 - OOOo0
if 34 - 34: o0oO0 * OOOo0 . i1IIi * o0oO0 / o0oO0
if 30 - 30: ii11ii1ii + Oo / Oo % ii11ii1ii . ii11ii1ii
if 55 - 55: o0oO0 - o0000oOoOoO0o + OoOoOO00 + oO0o0ooO0 % o00O0oo
if 41 - 41: i1IIi - o0000oOoOoO0o - o00O0oo
if 8 - 8: Ooo00oOo00o + O0oO - OOooOOo % Oo % OOooOOo * OoOO
def IIIi11I11 ( ) :
 oOOo0oo ( '[COLORgreen]Action[/COLOR]' , 'http://www.izlemeyedeger.com/tur/aksiyon' , 10036 , iIii1 + 'IZLEFILMS.png' , iI111I11I1I1 , '' )
 oOOo0oo ( '[COLORgreen]Adventure[/COLOR]' , 'http://www.izlemeyedeger.com/tur/macera' , 10036 , iIii1 + 'IZLEFILMS.png' , iI111I11I1I1 , '' )
 oOOo0oo ( '[COLORgreen]Animation[/COLOR]' , 'http://www.izlemeyedeger.com/tur/animasyon' , 10036 , iIii1 + 'IZLEFILMS.png' , iI111I11I1I1 , '' )
 oOOo0oo ( '[COLORgreen]Biography[/COLOR]' , 'http://www.izlemeyedeger.com/tur/biyografi' , 10036 , iIii1 + 'IZLEFILMS.png' , iI111I11I1I1 , '' )
 oOOo0oo ( '[COLORgreen]Comedy[/COLOR]' , 'http://www.izlemeyedeger.com/tur/komedi' , 10036 , iIii1 + 'IZLEFILMS.png' , iI111I11I1I1 , '' )
 oOOo0oo ( '[COLORgreen]Crime[/COLOR]' , 'http://www.izlemeyedeger.com/tur/suc' , 10036 , iIii1 + 'IZLEFILMS.png' , iI111I11I1I1 , '' )
 oOOo0oo ( '[COLORgreen]Documentary[/COLOR]' , 'http://www.izlemeyedeger.com/tur/belgesel' , 10036 , iIii1 + 'IZLEFILMS.png' , iI111I11I1I1 , '' )
 oOOo0oo ( '[COLORgreen]Drama[/COLOR]' , 'http://www.izlemeyedeger.com/tur/dram' , 10036 , iIii1 + 'IZLEFILMS.png' , iI111I11I1I1 , '' )
 oOOo0oo ( '[COLORgreen]Family[/COLOR]' , 'http://www.izlemeyedeger.com/tur/aile' , 10036 , iIii1 + 'IZLEFILMS.png' , iI111I11I1I1 , '' )
 oOOo0oo ( '[COLORgreen]Fantasy[/COLOR]' , 'http://www.izlemeyedeger.com/tur/fantastik' , 10036 , iIii1 + 'IZLEFILMS.png' , iI111I11I1I1 , '' )
 oOOo0oo ( '[COLORgreen]Far East[/COLOR]' , 'http://www.izlemeyedeger.com/tur/uzak-dogu' , 10036 , iIii1 + 'IZLEFILMS.png' , iI111I11I1I1 , '' )
 oOOo0oo ( '[COLORgreen]History[/COLOR]' , 'http://www.izlemeyedeger.com/tur/tarih' , 10036 , iIii1 + 'IZLEFILMS.png' , iI111I11I1I1 , '' )
 oOOo0oo ( '[COLORgreen]Horror[/COLOR]' , 'http://www.izlemeyedeger.com/tur/korku' , 10036 , iIii1 + 'IZLEFILMS.png' , iI111I11I1I1 , '' )
 oOOo0oo ( '[COLORgreen]Musical[/COLOR]' , 'http://www.izlemeyedeger.com/tur/muzikal' , 10036 , iIii1 + 'IZLEFILMS.png' , iI111I11I1I1 , '' )
 oOOo0oo ( '[COLORgreen]Mystery[/COLOR]' , 'http://www.izlemeyedeger.com/tur/gizem' , 10036 , iIii1 + 'IZLEFILMS.png' , iI111I11I1I1 , '' )
 oOOo0oo ( '[COLORgreen]Romance[/COLOR]' , 'http://www.izlemeyedeger.com/tur/romantik' , 10036 , iIii1 + 'IZLEFILMS.png' , iI111I11I1I1 , '' )
 oOOo0oo ( '[COLORgreen]Science Fiction[/COLOR]' , 'http://www.izlemeyedeger.com/tur/bilimkurgu' , 10036 , iIii1 + 'IZLEFILMS.png' , iI111I11I1I1 , '' )
 oOOo0oo ( '[COLORgreen]Sport[/COLOR]' , 'http://www.izlemeyedeger.com/tur/spor' , 10036 , iIii1 + 'IZLEFILMS.png' , iI111I11I1I1 , '' )
 oOOo0oo ( '[COLORgreen]Thriller[/COLOR]' , 'http://www.izlemeyedeger.com/tur/gerilim' , 10036 , iIii1 + 'IZLEFILMS.png' , iI111I11I1I1 , '' )
 oOOo0oo ( '[COLORgreen]War[/COLOR]' , 'http://www.izlemeyedeger.com/tur/savas' , 10036 , iIii1 + 'IZLEFILMS.png' , iI111I11I1I1 , '' )
 oOOo0oo ( '[COLORgreen]Western[/COLOR]' , 'http://www.izlemeyedeger.com/tur/western' , 10036 , iIii1 + 'IZLEFILMS.png' , iI111I11I1I1 , '' )
 if 44 - 44: OoOoOO00
def OOOO0OOO ( url ) :
 o0000oO = cloudflare . source ( url )
 oOOo0 = re . compile ( '<li>.+?<a href="(.+?)">.+?<img src="(.+?)" alt=""/>.+?<span class="year">\n(.+?)</span>.+?<span class="video-title">\n(.+?)</span>.+?</li>' , re . DOTALL ) . findall ( o0000oO )
 for url , iiIiIIIiiI , i1i1ii , oo00O00oO in oOOo0 :
  oo00O00oO = ( oo00O00oO ) . replace ( '  ' , '' ) + ' ' + ( i1i1ii ) . replace ( '  ' , '' )
  iIiIIIi = iiIiIIIiiI
  url = url
  iII1ii1 ( oo00O00oO , iIiIIIi , url )
 I1i1iiiI1 = re . compile ( '<a href="http://www.izlemeyedeger.com/tur/(.+?)?s=(.+?)&sort=&orderby=">(.+?)</a>' ) . findall ( o0000oO )
 for url , iIIi , oo00O00oO in I1i1iiiI1 :
  oOOo0oo ( '[COLORgold] Page ' + oo00O00oO + '[/COLOR]' , 'http://www.izlemeyedeger.com/tur/' + url + '?s=' + iIIi + '&sort=&orderby=' , 10036 , '' , iI111I11I1I1 , '' )
  if 62 - 62: Oo - o0000oOoOoO0o
  if 21 - 21: O0 % IIII . OOOo0 / OoOoOO00 + IIII
def OOOO0O00o ( ) :
 if 62 - 62: iIii1I11I1II1
 o0000oO = cloudflare . source ( oOo0oooo00o ( 'aHR0cDovL3d3dy5pemxlbWV5ZWRlZ2VyLmNvbQ==' ) )
 i1II = re . compile ( '<!-- popüler filmler -->(.+?)<!-- content -->' , re . DOTALL ) . findall ( o0000oO )
 for iI1I in i1II :
  oOOo0 = re . compile ( '<li>.+?<a href="(.+?)">.+?<img width=".+?" height=".+?" src="(.+?)" alt=""/>.+?<span class="year">(.+?)</span>.+?<span class=".+?">(.+?)</span>.+?</li>' , re . DOTALL ) . findall ( str ( i1II ) )
  for oo000o , iiIiIIIiiI , i1i1ii , oo00O00oO in oOOo0 :
   oo00O00oO = ( oo00O00oO ) . replace ( '  ' , '' ) . replace ( '\\t' , '' ) . replace ( '\\r' , '' ) . replace ( '\\n' , '' ) . replace ( '\\xc3\\x87' , '' ) + ' ' + ( i1i1ii ) . replace ( '  ' , '' ) . replace ( '\\t' , '' ) . replace ( '\\r' , '' ) . replace ( '\\n' , '' )
   iIiIIIi = iiIiIIIiiI
   oo000o = oo000o
   iII1ii1 ( oo00O00oO , iIiIIIi , oo000o )
   if 100 - 100: iIii1I11I1II1 + I1IiI / Oo . i11iIiiIii
   if 14 - 14: OOooOOo * OoOO0ooOOoo0O + oO0o0ooO0 + O0 + i11iIiiIii
def oOoO0 ( ) :
 o0000oO = cloudflare . source ( oOo0oooo00o ( 'aHR0cDovL3d3dy5pemxlbWV5ZWRlZ2VyLmNvbS9zZXJpLWZpbG1sZXI=' ) )
 oOOo0 = re . compile ( ' <div class="title">.+?</span>\n(.+?)<span style=".+?<img src="(.+?)" alt="" title=".+?<a class="more" href="(.+?)">' , re . DOTALL ) . findall ( o0000oO )
 for oo00O00oO , iiIiIIIiiI , oo000o in oOOo0 :
  if 'IMDB' in oo00O00oO :
   pass
  else :
   oOOo0oo ( '[COLORgreen]' + ( oo00O00oO ) . replace ( '  ' , '' ) + '[/COLOR]' , oo000o , 10037 , iiIiIIIiiI , iI111I11I1I1 , '' )
 I1i1iiiI1 = re . compile ( '<a href="http://www.izlemeyedeger.com/seri-filmler(.+?)">(.+?)</a>' ) . findall ( o0000oO )
 for oo000o , oo00O00oO in I1i1iiiI1 :
  oOOo0oo ( '[COLORgold] Page ' + oo00O00oO + '[/COLOR]' , 'http://www.izlemeyedeger.com/seri-filmler' + oo000o , 10039 , '' , iI111I11I1I1 , '' )
  if 77 - 77: iIii1I11I1II1 . oO0o0ooO0 % oO0o0ooO0 + i11iIiiIii
def Oo00o0OO0O00o ( url ) :
 o0000oO = cloudflare . source ( url )
 oOOo0 = re . compile ( ' <div class="title">.+?</span>\n(.+?)<span style=".+?<img src="(.+?)" alt="" title=".+?<a class="more" href="(.+?)">' , re . DOTALL ) . findall ( o0000oO )
 for oo00O00oO , iiIiIIIiiI , url in oOOo0 :
  if 'IMDB' in oo00O00oO :
   pass
  else :
   oOOo0oo ( '[COLORgreen]' + ( oo00O00oO ) . replace ( '  ' , '' ) + '[/COLOR]' , url , 10037 , iiIiIIIiiI , iI111I11I1I1 , '' )
 I1i1iiiI1 = re . compile ( '<a href="http://www.izlemeyedeger.com/seri-filmler(.+?)">(.+?)</a>' ) . findall ( o0000oO )
 for url , oo00O00oO in I1i1iiiI1 :
  oOOo0oo ( '[COLORgold] Page ' + oo00O00oO + '[/COLOR]' , 'http://www.izlemeyedeger.com/seri-filmler' + url , 10034 , '' , iI111I11I1I1 , '' )
  if 82 - 82: o0000oOoOoO0o + OoooooooOO - i1IIi . i1IIi
  if 6 - 6: OOooOOo / o0000oOoOoO0o / OoOoOO00
def I1i11111i1i11 ( url ) :
 o0000oO = cloudflare . source ( url )
 oOOo0 = re . compile ( '<li>.+?<a href="(.+?)">.+?<img src="(.+?)" alt=""/>.+?<span class="year">\n(.+?)</span>.+?<span class="video-title">\n(.+?)</span>.+?</li>' , re . DOTALL ) . findall ( o0000oO )
 for url , iiIiIIIiiI , i1i1ii , oo00O00oO in oOOo0 :
  oo00O00oO = ( oo00O00oO ) . replace ( '  ' , '' ) . replace ( '&amp;' , '&' ) . replace ( '\\t' , '' ) . replace ( '\\r' , '' ) . replace ( '\\n' , '' ) . replace ( '\\xc3\\x87' , '' ) + ' ' + ( i1i1ii ) . replace ( '  ' , '' ) . replace ( '\\t' , '' ) . replace ( '\\r' , '' ) . replace ( '\\n' , '' )
  iIiIIIi = iiIiIIIiiI
  url = url
  iII1ii1 ( oo00O00oO , iIiIIIi , url )
  if 77 - 77: ii11ii1ii + Ooo00oOo00o / OoOO + O0 * OOooOOo
def iII1ii1 ( name , iconimage , url ) :
 o0000oO = cloudflare . source ( url )
 oOOo0 = re . compile ( '<meta itemprop="embedURL" content="(.+?)" />' ) . findall ( o0000oO )
 for url in oOOo0 :
  I1ii11 ( name , iconimage , url )
  if 74 - 74: Oo - OOooOOo . i1IIi
def I1ii11 ( name , iconimage , url ) :
 name = name
 iiIiIIIiiI = iconimage
 o0000oO = cloudflare . source ( url )
 oOOo0 = re . compile ( 'file: "(.+?)",.+?label: "(.+?)"' , re . DOTALL ) . findall ( o0000oO )
 for iIIi , i1III in oOOo0 :
  iii1 ( '[COLORgreen]' + name + ' - ' + i1III + '[/COLOR]' , iIIi , 10012 , iiIiIIIiiI )
  if 49 - 49: i11iIiiIii % o00O0oo . I1IiI
def Ii1i1iI ( ) :
 iiIi11iI1iii = Oo0o0000o0o0 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oo000 = iiIi11iI1iii . lower ( )
 oo000o = 'http://www.izlemeyedeger.com/arama?q=' + iiIi11iI1iii
 o0000oO = cloudflare . source ( oo000o )
 oOOo0 = re . compile ( '<div class="inner">.+?<li>.+?<a href="(.+?)">.+?<img src="(.+?)" alt.+?<span class="year">(.+?)</span>.+?<span class="video-title">(.+?)</span>.+?</li>.+?</div>' , re . DOTALL ) . findall ( o0000oO )
 for oo000o , iiIiIIIiiI , i1i1ii , oo00O00oO in oOOo0 :
  oo00O00oO = ( oo00O00oO ) . replace ( '  ' , '' ) . replace ( '\\t' , '' ) . replace ( '\\r' , '' ) . replace ( '\\n' , '' ) . replace ( '\\xc3\\x87' , '' ) + ' ' + ( i1i1ii ) . replace ( '  ' , '' ) . replace ( '\\t' , '' ) . replace ( '\\r' , '' ) . replace ( '\\n' , '' )
  iIiIIIi = iiIiIIIiiI
  oo000o = oo000o
  iII1ii1 ( oo00O00oO , iIiIIIi , oo000o )
  xbmcplugin . addSortMethod ( Oo00OOOOO , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 16 - 16: OoOO0ooOOoo0O / Oo / OoooooooOO * OOOo0 + i1IIi % OoOO0ooOOoo0O
  if 71 - 71: I1IiI
  if 14 - 14: i11iIiiIii % OoOO0ooOOoo0O
def OooO0oo ( ) :
 if 89 - 89: o00O0oo
 oOOo0oo ( '[COLORgreen]Stand Up[/COLOR]' , '' , 10014 , iIii1 + 'ORIGINSTANDUP.png' , iI111I11I1I1 , '' )
 oOOo0oo ( '[COLORgreen]Search Comedian[/COLOR]' , '' , 10015 , iIii1 + 'ORIGINSTANDUP.png' , iI111I11I1I1 , '' )
 oOOo0oo ( '[COLORgreen]Others[/COLOR]' , '' , 10017 , iIii1 + 'ORIGINSTANDUP.png' , iI111I11I1I1 , '' )
 if 76 - 76: o0oO0
def IIIiI11ii1I ( ) :
 o0000oO = oOoO0o00OO0 ( ( oOo0oooo00o ( 'aHR0cDovL2JhY2syYmFzaWNzYnVpbGQuY28udWsvdGVzdC9zdGFuZHVwbGlzdC5waHA=' ) ) )
 oOOo0 = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( o0000oO )
 for oo000o , iiIiIIIiiI , oo00O00oO in oOOo0 :
  iii1 ( '[COLORgreen]' + oo00O00oO + '[/COLOR]' , oo000o , 222 , iiIiIIIiiI )
  if 39 - 39: iIii1I11I1II1 / O0 / OoOO - o00O0oo - oO0o0ooO0 % OoOO0ooOOoo0O
def I1ii11Ii ( ) :
 iiIi11iI1iii = Oo0o0000o0o0 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oo000 = iiIi11iI1iii . lower ( )
 o0000oO = oOoO0o00OO0 ( ( oOo0oooo00o ( 'aHR0cDovL3d3dy5jb3VjaHRyaXBwZXIuY29tL2ZvcnVtMi9wYWdlLnBocD9wYWdlPTM=' ) ) )
 i1II = re . compile ( '<tr>.+?<td width=".+?" align=".+?">.+?<img border=".+?" src="..(.+?)" width=".+?" height=".+?"></td>.+?<td width=".+?" valign=".+?" align=".+?"><font size=".+?">(.+?)</font></td>.+?<td width=".+?">(.+?)</td>' , re . DOTALL ) . findall ( o0000oO )
 for iiIiIIIiiI , I111i1II , iIiiiI1IiI1I1 in i1II :
  for iiIi11iI1iii in I111i1II :
   print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< img >>>>>>>>>>>>>>>>>>>>>>>>>>'
   O0ooooo0OOOO0 = re . compile ( '<a href="(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( iIiiiI1IiI1I1 )
   for oo000o , oo00O00oO in O0ooooo0OOOO0 :
    if 'tube' in oo000o :
     pass
    elif 'stage' in oo000o :
     iii1 ( '[COLORgreen]' + I111i1II + '   -   ' + oo00O00oO + '[/COLOR]' , ( oo000o ) . replace ( '" target="_blank' , '' ) , 10016 , 'http://couchtripper.com/' + iiIiIIIiiI , )
    elif 'vee' in oo000o :
     pass
     if 9 - 9: OoOoOO00 - OOooOOo / oO0o0ooO0 / OOooOOo
def I1i111iiIIIi ( ) :
 o0000oO = oOoO0o00OO0 ( ( oOo0oooo00o ( 'aHR0cDovL3d3dy5jb3VjaHRyaXBwZXIuY29tL2ZvcnVtMi9wYWdlLnBocD9wYWdlPTM=' ) ) )
 i1II = re . compile ( '<tr>.+?<td width=".+?" align=".+?">.+?<img border=".+?" src="..(.+?)" width=".+?" height=".+?"></td>.+?<td width=".+?" valign=".+?" align=".+?"><font size=".+?">(.+?)</font></td>.+?<td width=".+?">(.+?)</td>' , re . DOTALL ) . findall ( o0000oO )
 for iiIiIIIiiI , I111i1II , iIiiiI1IiI1I1 in i1II :
  O0ooooo0OOOO0 = re . compile ( '<a href="(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( iIiiiI1IiI1I1 )
  for oo000o , oo00O00oO in O0ooooo0OOOO0 :
   if 'tube' in oo000o :
    pass
   elif 'stage' in oo000o :
    iii1 ( '[COLORgreen]' + I111i1II + '   -   ' + oo00O00oO + '[/COLOR]' , ( oo000o ) . replace ( '" target="_blank' , '' ) , 10016 , 'http://couchtripper.com/' + iiIiIIIiiI )
   elif 'vee' in oo000o :
    pass
    if 75 - 75: o0000oOoOoO0o . OoooooooOO % OOooOOo * o0000oOoOoO0o % OoooooooOO
    if 13 - 13: IIII / i11iIiiIii % OoOoOO00 % o0000oOoOoO0o . ii11ii1ii
 xbmcplugin . addSortMethod ( Oo00OOOOO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 8 - 8: I1IiI + Oo - OoOoOO00
def IiIi1iIIi1 ( url ) :
 o0000oO = oOoO0o00OO0 ( url )
 print '>>>>>>>>>>>>>>>>>>>>>>>>' + url + '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'
 O0OoO0ooOO0o = re . compile ( "url\[.+?\] = '(.+?)';" ) . findall ( o0000oO )
 print '>>>>>>>>>>>>>>>>>>>>>>>' + ( str ( O0OoO0ooOO0o ) ) + '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
 for url in O0OoO0ooOO0o :
  II11iIIiiiII ( ( url ) . replace ( '[' , '' ) . replace ( ']' , '' ) . replace ( '\'' , '' ) )
  if 81 - 81: O0 * OoOoOO00 + OOOo0 * i11iIiiIii - ii11ii1ii / OOOo0
  if 63 - 63: I1IiI - OoooooooOO % O0oO
  if 77 - 77: Ooo00oOo00o . i1IIi
  if 35 - 35: o0oO0 * OoOO0ooOOoo0O . o0000oOoOoO0o * OOooOOo . I1IiI / O0
  if 100 - 100: O0oO . OOooOOo * Oo % O0 * O0
  if 14 - 14: ii11ii1ii . o0oO0 + OoOoOO00 / oO0o0ooO0 / o0000oOoOoO0o
  if 74 - 74: O0 / i1IIi
def OoO ( ) :
 if 41 - 41: i1IIi * OoOoOO00 / OoooooooOO . OoOO0ooOOoo0O
 O0iII1 ( '[COLOR darkgoldenrod]Open Pandora\'s Box[/COLOR]' , '' , 10029 , 'https://encrypted-tbn1.gstatic.com/images?q=tbn%3AANd9GcTQ9r4TA8yIw9ggxuwsHxWojo6tPVfgTe8QIOxOQwzNR2TavtCi6Q' , iI111I11I1I1 , '' )
 O0iII1 ( '[COLOR darkgoldenrod]Search[/COLOR]' , '' , 10026 , 'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png' , iI111I11I1I1 , '' )
 if 27 - 27: Ooo00oOo00o . o0000oOoOoO0o + I1IiI / iIii1I11I1II1 % oO0o0ooO0 . o0oO0
 xbmcplugin . setContent ( Oo00OOOOO , 'movies' )
 if 14 - 14: OoOO + ii11ii1ii - oO0o0ooO0 / O0 . O0oO
def i1iiIiI1Ii1i ( ) :
 O0iII1 ( 'Search Pandoras Films' , '' , 10027 , iIii1 + 'PANDORASBOX.png' , iI111I11I1I1 , '' )
 O0iII1 ( 'Search Pandoras TV' , '' , 10028 , iIii1 + 'PANDORASBOX.png' , iI111I11I1I1 , '' )
 if 22 - 22: IIII / i11iIiiIii
def oOOoo ( ) :
 if 14 - 14: OOooOOo * OoOO
 iiIi11iI1iii = Oo0o0000o0o0 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oo000 = iiIi11iI1iii . lower ( )
 O0OOO0OOooo00 = [ 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' ]
 if 6 - 6: o00O0oo - o0oO0 * OoOO0ooOOoo0O . oO0o0ooO0 / O0 * o0oO0
 for II11iI111i1 in O0OOO0OOooo00 :
  Oo00OoOo = Base_Pand + II11iI111i1 + CAT
  o0000oO = oOoO0o00OO0 ( Oo00OoOo )
  oOOo0 = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( o0000oO )
  for oo000o , iIiIIIi , ii1ii111 , ooo00OOOooO , oo00O00oO in oOOo0 :
   if iiIi11iI1iii in oo00O00oO . lower ( ) :
    i11111I1I ( oo00O00oO , oo000o , 222 , iIiIIIi , ooo00OOOooO , ii1ii111 )
    if 11 - 11: OoooooooOO . O0oO
    xbmcplugin . setContent ( Oo00OOOOO , 'movies' )
    xbmcplugin . addSortMethod ( Oo00OOOOO , xbmcplugin . SORT_METHOD_TITLE ) ;
    if 80 - 80: OoooooooOO - OoOO0ooOOoo0O * o00O0oo * ii11ii1ii / OOOo0 / OoOO0ooOOoo0O
    if 13 - 13: O0oO * o0oO0 + i11iIiiIii * O0oO - o0oO0
def Ii1i1i1i1I1Ii ( ) :
 if 25 - 25: OoOoOO00
 iiIi11iI1iii = Oo0o0000o0o0 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oo000 = iiIi11iI1iii . lower ( )
 O0OOO0OOooo00 = [ 'a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' , 'p' , 'q' , 'r' , 's' , 't' , 'u' , 'v' , 'w' , 'x' , 'y' , 'z' ]
 if 11 - 11: Oo
 for II11iI111i1 in O0OOO0OOooo00 :
  OOOOoO0O0oo0 = Base_Pand + II11iI111i1 + CAT
  o0000oO = oOoO0o00OO0 ( OOOOoO0O0oo0 )
  oOOo0 = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( o0000oO )
  for oo00O00oO , ii1ii111 , oo000o , iiIiIIIiiI , ooo00OOOooO , iiiI1I1iIIIi1 in oOOo0 :
   if iiIi11iI1iii in oo00O00oO . lower ( ) :
    O0iII1 ( oo00O00oO , oo000o , iiiI1I1iIIIi1 , iiIiIIIiiI , ooo00OOOooO , ii1ii111 )
    if 17 - 17: iIii1I11I1II1 . OoooooooOO / o0000oOoOoO0o % OoOoOO00 % i1IIi / i11iIiiIii
    xbmcplugin . setContent ( Oo00OOOOO , 'movies' )
    xbmcplugin . addSortMethod ( Oo00OOOOO , xbmcplugin . SORT_METHOD_TITLE ) ;
    if 58 - 58: Oo . OoOoOO00 + OoOO - i11iIiiIii / OoOoOO00 / O0
    if 85 - 85: I1IiI + OoOO0ooOOoo0O
def I1II ( ) :
 if 27 - 27: OoOoOO00 / o00O0oo . OoOO0ooOOoo0O
 Iiii1i1 = oOoO0o00OO0 ( oOo0oooo00o ( 'aHR0cDovL3NlZWR1cmdyZWVkLngxMGhvc3QuY29tL29yaWdpbi9zcG9uZ2VtYWluLnBocA==' ) )
 oOOo0 = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( Iiii1i1 )
 for oo00O00oO , ii1ii111 , oo000o , iiIiIIIiiI , ooo00OOOooO , iiiI1I1iIIIi1 in oOOo0 :
  O0iII1 ( oo00O00oO , oo000o , iiiI1I1iIIIi1 , iiIiIIIiiI , ooo00OOOooO , ii1ii111 )
  if 9 - 9: o0oO0 - ii11ii1ii - oO0o0ooO0
def o0O0Oo00 ( url ) :
 if 51 - 51: OoOO0ooOOoo0O % iIii1I11I1II1 - OoooooooOO % o0oO0 * iIii1I11I1II1 % Ooo00oOo00o
 xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
 oO0o00oOOooO0 = ( '%s%s' % ( OOOoO000 , url ) )
 ooo0O = oOoO0o00OO0 ( url )
 oOOo0 = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( ooo0O )
 for url , iIiIIIi , ii1ii111 , oOOOO , oo00O00oO in oOOo0 :
  i11111I1I ( oo00O00oO , url , 222 , iIiIIIi , oOOOO , ii1ii111 )
  if 49 - 49: OoOoOO00 . OoOO . i11iIiiIii % IIII
  I11II1i ( 'tvshows' , 'Media Info 3' )
  if 34 - 34: O0oO % IIII
  xbmcplugin . addSortMethod ( Oo00OOOOO , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 3 - 3: OoOoOO00 / OoOO0ooOOoo0O + IIII . o0oO0 . Ooo00oOo00o
  if 83 - 83: OoOO + OoooooooOO
def I111IiiIi1 ( url ) :
 if 88 - 88: OoooooooOO
 Iiii1i1 = oOoO0o00OO0 ( url )
 oOOo0 = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( Iiii1i1 )
 for oo00O00oO , ii1ii111 , url , iiIiIIIiiI , ooo00OOOooO , iiiI1I1iIIIi1 in oOOo0 :
  O0iII1 ( oo00O00oO , url , iiiI1I1iIIIi1 , iiIiIIIiiI , ooo00OOOooO , ii1ii111 )
  if 84 - 84: I1IiI / o0000oOoOoO0o * oO0o0ooO0 / OoOO - i11iIiiIii . Oo
 I11II1i ( 'tvshows' , 'Media Info 3' )
 if 60 - 60: ii11ii1ii * OOOo0
 if 17 - 17: OoOO0ooOOoo0O % Oo / ii11ii1ii . IIII * OoOO0ooOOoo0O - OoOoOO00
 xbmcplugin . addSortMethod ( Oo00OOOOO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 41 - 41: o00O0oo
def i11111I1I ( name , url , mode , iconimage , fanart , description ) :
 if 77 - 77: O0oO
 OooOOOOoO00OoOO = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 oOooo0O0o = True
 Oo000 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 Oo000 . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 Oo000 . setProperty ( "Fanart_Image" , fanart )
 oOooo0O0o = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = OooOOOOoO00OoOO , listitem = Oo000 , isFolder = False )
 return oOooo0O0o
 if 81 - 81: OoOO0ooOOoo0O - OoOO0ooOOoo0O % OoOoOO00 * Ooo00oOo00o
def O0iII1 ( name , url , mode , iconimage , fanart , description ) :
 if 39 - 39: o0000oOoOoO0o
 OooOOOOoO00OoOO = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 oOooo0O0o = True
 Oo000 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 Oo000 . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 Oo000 . setProperty ( "Fanart_Image" , fanart )
 oOooo0O0o = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = OooOOOOoO00OoOO , listitem = Oo000 , isFolder = True )
 return oOooo0O0o
 if 58 - 58: i1IIi % OOooOOo
 if 79 - 79: OOooOOo % oO0o0ooO0 * OoooooooOO * iIii1I11I1II1 . oO0o0ooO0 / o00O0oo
 if 19 - 19: O0 + o0000oOoOoO0o + o00O0oo / OoOoOO00 / OoOoOO00
 if 86 - 86: ii11ii1ii * O0 * IIII
 if 51 - 51: OoOoOO00 + IIII . i1IIi . ii11ii1ii + I1IiI * OOOo0
 if 72 - 72: OoOO + OoOO / OoOoOO00 . OoooooooOO % o00O0oo
 if 49 - 49: OoOO . Ooo00oOo00o - Oo * OoooooooOO . Oo
def ii1Ii1IiIIi ( ) :
 if 83 - 83: o0000oOoOoO0o / ii11ii1ii
 oOOo0oo ( '[COLORgreen]Recent Episodes[/COLOR]' , '' , 10019 , iIii1 + 'dtv.png' , iI111I11I1I1 , '' )
 oOOo0oo ( '[COLORgreen]Genres[/COLOR]' , '' , 10020 , iIii1 + 'dtv.png' , iI111I11I1I1 , '' )
 oOOo0oo ( '[COLORgreen]Search[/COLOR]' , '' , 10021 , iIii1 + 'dtv.png' , iI111I11I1I1 , '' )
 if 34 - 34: OOOo0 * Oo * O0oO / Ooo00oOo00o * o0000oOoOoO0o / iIii1I11I1II1
def OOOo ( ) :
 if 88 - 88: i11iIiiIii - o0oO0
 Iiii1i1 = cloudflare . source ( oOo0oooo00o ( 'aHR0cDovL2RpemlsYWIuY29t' ) )
 oOOo0 = re . compile ( '<li id=".+?">.+?<a href="(.+?)">.+?<img width="40" height="40" src="(.+?)" alt=""/>.+?<span class="title">\n(.+?)</span>.+?<span class="alt-title">\n(.+?)</span>.+?</a>.+?</li>' , re . DOTALL ) . findall ( Iiii1i1 )
 for oo000o , iiIiIIIiiI , oo00O00oO , O0iIi1IiII in oOOo0 :
  oOOo0oo ( oo00O00oO + '  -  ' + ( O0iIi1IiII ) . replace ( 'sezon' , 'Season' ) . replace ( 'bölüm' , 'Episode' ) , oo000o , 10023 , iIii1 + 'dtv.png' , iI111I11I1I1 , '' )
  if 27 - 27: oO0o0ooO0 . o0000oOoOoO0o . iIii1I11I1II1 . iIii1I11I1II1
  if 20 - 20: OOooOOo / i1IIi
  if 71 - 71: I1IiI . i1IIi
def o0 ( ) :
 if 91 - 91: iIii1I11I1II1 % OOooOOo . iIii1I11I1II1 % i1IIi / OoOoOO00 * I1IiI
 oOOo0oo ( '[COLORgreen]Action[/COLOR]' , 'Aksiyon' , 10024 , iIii1 + 'dtv.png' , iI111I11I1I1 , '' )
 oOOo0oo ( '[COLORgreen]Adventure[/COLOR]' , 'Macera' , 10024 , iIii1 + 'dtv.png' , iI111I11I1I1 , '' )
 oOOo0oo ( '[COLORgreen]Animation[/COLOR]' , 'Animasyon' , 10024 , iIii1 + 'dtv.png' , iI111I11I1I1 , '' )
 oOOo0oo ( '[COLORgreen]Anime[/COLOR]' , 'Anime' , 10024 , iIii1 + 'dtv.png' , iI111I11I1I1 , '' )
 oOOo0oo ( '[COLORgreen]Biography[/COLOR]' , 'Biyografi' , 10024 , iIii1 + 'dtv.png' , iI111I11I1I1 , '' )
 oOOo0oo ( '[COLORgreen]Comedy[/COLOR]' , 'Komedi' , 10024 , iIii1 + 'dtv.png' , iI111I11I1I1 , '' )
 oOOo0oo ( '[COLORgreen]Crime[/COLOR]' , 'Su%C3%A7' , 10024 , iIii1 + 'dtv.png' , iI111I11I1I1 , '' )
 oOOo0oo ( '[COLORgreen]Documentary[/COLOR]' , 'Belgesel' , 10024 , iIii1 + 'dtv.png' , iI111I11I1I1 , '' )
 oOOo0oo ( '[COLORgreen]Drama[/COLOR]' , 'Dram' , 10024 , iIii1 + 'dtv.png' , iI111I11I1I1 , '' )
 oOOo0oo ( '[COLORgreen]Family[/COLOR]' , 'Aile' , 10024 , iIii1 + 'dtv.png' , iI111I11I1I1 , '' )
 oOOo0oo ( '[COLORgreen]Fantasy[/COLOR]' , 'Fantastik' , 10024 , iIii1 + 'dtv.png' , iI111I11I1I1 , '' )
 oOOo0oo ( '[COLORgreen]History[/COLOR]' , 'Tarih' , 10024 , iIii1 + 'dtv.png' , iI111I11I1I1 , '' )
 oOOo0oo ( '[COLORgreen]Horror[/COLOR]' , 'Korku' , 10024 , iIii1 + 'dtv.png' , iI111I11I1I1 , '' )
 oOOo0oo ( '[COLORgreen]Mini-Series[/COLOR]' , 'Mini%20Dizi' , 10024 , iIii1 + 'dtv.png' , iI111I11I1I1 , '' )
 oOOo0oo ( '[COLORgreen]Musical[/COLOR]' , 'M%C3%BCzikal' , 10024 , iIii1 + 'dtv.png' , iI111I11I1I1 , '' )
 oOOo0oo ( '[COLORgreen]Mystery[/COLOR]' , 'Gizem' , 10024 , iIii1 + 'dtv.png' , iI111I11I1I1 , '' )
 oOOo0oo ( '[COLORgreen]Romance[/COLOR]' , 'Romantik' , 10024 , iIii1 + 'dtv.png' , iI111I11I1I1 , '' )
 oOOo0oo ( '[COLORgreen]Science Fiction[/COLOR]' , 'Bilim%20Kurgu' , 10024 , iIii1 + 'dtv.png' , iI111I11I1I1 , '' )
 oOOo0oo ( '[COLORgreen]Sport[/COLOR]' , 'Spor' , 10024 , iIii1 + 'dtv.png' , iI111I11I1I1 , '' )
 oOOo0oo ( '[COLORgreen]Thriller[/COLOR]' , 'Gerilim' , 10024 , iIii1 + 'dtv.png' , iI111I11I1I1 , '' )
 oOOo0oo ( '[COLORgreen]War[/COLOR]' , 'Sava%C5%9F' , 10024 , iIii1 + 'dtv.png' , iI111I11I1I1 , '' )
 oOOo0oo ( '[COLORgreen]Western[/COLOR]' , 'Tarih' , 10024 , iIii1 + 'dtv.png' , iI111I11I1I1 , '' )
 oOOo0oo ( '[COLORgreen]Youth[/COLOR]' , 'Gen%C3%A7lik' , 10024 , iIii1 + 'dtv.png' , iI111I11I1I1 , '' )
 if 10 - 10: OoOoOO00 . oO0o0ooO0
def I1iOOOO ( url ) :
 ooO0oO00O0o = 'http://dizilab.com/arsiv?limit=100&tur=' + url + '&orderby=&ulke=&order=&yil=&dizi_adi='
 o0000oO = cloudflare . source ( ooO0oO00O0o )
 oOOo0 = re . compile ( '<div class="tv-series-single">.+?<a href="(.+?)" class="film-image">.+?<img src="(.+?)" alt=""/>.+?<span class="position">.+?</span>\n(.+?)</a>' , re . DOTALL ) . findall ( o0000oO )
 for url , iiIiIIIiiI , oo00O00oO in oOOo0 :
  oOOo0oo ( '[COLORgreen]' + oo00O00oO + '[/COLOR]' , url , 10022 , iIii1 + 'dtv.png' , iI111I11I1I1 , '' )
  if 70 - 70: O0oO
  if 16 - 16: oO0o0ooO0 - OoooooooOO % Oo
  if 36 - 36: OoOO0ooOOoo0O
  if 84 - 84: O0oO . Ooo00oOo00o . OoOoOO00 . o0000oOoOoO0o / o00O0oo % ii11ii1ii
def OOO0oOoO0O ( ) :
 if 84 - 84: O0 * OoooooooOO - IIII * IIII
 iiIi11iI1iii = Oo0o0000o0o0 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oo000 = iiIi11iI1iii . lower ( )
 oo000o = ( oOo0oooo00o ( 'aHR0cDovL2RpemlsYWIuY29tL2Fyc2l2P2xpbWl0PSZ0dXI9Jm9yZGVyYnk9JnVsa2U9Jm9yZGVyPSZ5aWw9JmRpemlfYWRpPQ==' ) ) + ( iiIi11iI1iii ) . replace ( ' ' , '+' )
 o0000oO = cloudflare . source ( oo000o )
 oOOo0 = re . compile ( '<a href="(.+?)" class="film-image">\n<img src="(.+?)" alt=""/>\n</a>\n<div class="tss-detail">\n<a class="title" style="" href=".+?">\n<span class="position">.+?</span>\n(.+?)</a>' ) . findall ( o0000oO )
 for oo000o , iiIiIIIiiI , oo00O00oO in oOOo0 :
  if iiIi11iI1iii in oo00O00oO . lower ( ) :
   oOOo0oo ( '[COLORgreen]' + oo00O00oO + '[/COLOR]' , oo000o , 10022 , iIii1 + 'dtv.png' )
   if 8 - 8: o0oO0 / i1IIi . OoOO
   if 41 - 41: oO0o0ooO0 + Ooo00oOo00o
   if 86 - 86: I1IiI . iIii1I11I1II1 - Ooo00oOo00o
def oOO ( url ) :
 o0000oO = cloudflare . source ( url )
 oOOo0 = re . compile ( '<a class="season" href="(.+?)">\n(.+?)\n</a>.+?<a class="episode" href=".+?">\n(.+?)\n</a>.+?<a class="episode-name" href=".+?">\n(.+?)</a>' , re . DOTALL ) . findall ( o0000oO )
 for iIIi , I11I , iIIII1i , oo00O00oO in oOOo0 :
  o00oO0 = ( iIIII1i ) . replace ( 'Sezon' , '' ) . replace ( 'bölüm' , '' ) . replace ( 'Bölüm' , '' ) . replace ( 'BÃ¶lÃ¼m' , '' ) . replace ( '.' , '' )
  i11I1II = ( I11I ) . replace ( 'bölüm' , '' ) . replace ( 'Sezon' , '' ) . replace ( 'Bölüm' , '' ) . replace ( 'BÃ¶lÃ¼m' , '' ) . replace ( '.' , '' )
  OO0 = 'Season ' + i11I1II + 'Episode ' + o00oO0 + oo00O00oO
  OOO0oOOo00O ( OO0 , iIIi )
  if 51 - 51: ii11ii1ii / iIii1I11I1II1 % OoOO + OOooOOo * o0oO0 + O0oO
  xbmcplugin . addSortMethod ( Oo00OOOOO , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 77 - 77: o0oO0 * I1IiI
  if 14 - 14: o0000oOoOoO0o % o0000oOoOoO0o / IIII
def OOO0oOOo00O ( name , url ) :
 iIIi = url
 OoOoO00O0 = name
 OoOOO = cloudflare . source ( iIIi )
 oOOOoo00 = re . compile ( 'file: "(.+?)",.+?label: "(.+?)",' , re . DOTALL ) . findall ( OoOOO )
 for O0OoO0ooOO0o , i1III in oOOOoo00 :
  iii1 ( '[COLORgreen]' + OoOoO00O0 + i1III + '[/COLOR]' , O0OoO0ooOO0o , 10012 , iIii1 + 'dtv.png' )
  if 67 - 67: oO0o0ooO0 % oO0o0ooO0 / oO0o0ooO0
 xbmcplugin . addSortMethod ( Oo00OOOOO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 53 - 53: iIii1I11I1II1
 if 68 - 68: OoooooooOO % OoOoOO00
def Ii1i1i1111 ( ) :
 if 57 - 57: o00O0oo % OoOoOO00
 if 67 - 67: o0oO0 + OOOo0 * i11iIiiIii - OoOO / IIII % oO0o0ooO0
 if 92 - 92: o00O0oo - OoOO - o0oO0 % OoooooooOO / OoOO0ooOOoo0O
 if 19 - 19: Oo - Ooo00oOo00o
 if 56 - 56: ii11ii1ii
 if 26 - 26: OoooooooOO % OoooooooOO
 if 33 - 33: O0oO
 if 62 - 62: ii11ii1ii + o00O0oo + i1IIi / OoooooooOO
 if 7 - 7: OOooOOo + i1IIi . OOOo0 / Oo
 if 22 - 22: o0oO0 - o0oO0 % OoOO0ooOOoo0O . O0oO + OoOO
 if 63 - 63: OOOo0 % O0oO * OOooOOo + O0oO / Oo % oO0o0ooO0
 if 45 - 45: IIII
 if 20 - 20: OoooooooOO * OOooOOo * O0 . OoOO0ooOOoo0O
 if 78 - 78: iIii1I11I1II1 + o0000oOoOoO0o - o00O0oo * O0oO - OoooooooOO % I1IiI
 oOOo0oo ( '[COLORgreen]Series[/COLOR]' , 'http://www.watchseries.li/series' , 10041 , iIii1 + 'WATCHSERIES.png' , '' , '' )
 oOOo0oo ( '[COLORgreen]Newest Episodes Added[/COLOR]' , 'http://www.watchseries.li/latest' , 10046 , iIii1 + 'WATCHSERIES.png' , '' , '' )
 oOOo0oo ( '[COLORgreen]This Week\'s Popular Episodes[/COLOR]' , 'http://www.watchseries.li/new' , 10042 , iIii1 + 'WATCHSERIES.png' , '' , '' )
 oOOo0oo ( '[COLORgreen]Search Program[/COLOR]' , '' , 10043 , iIii1 + 'WATCHSERIES.png' , '' , '' )
 if 34 - 34: O0
 if 80 - 80: i1IIi - Oo / Ooo00oOo00o - i11iIiiIii
def OO0O0o0o0 ( url ) :
 o0000oO = oOoO0o00OO0 ( url )
 iI1I = re . compile ( '<ul class="pagination" style="line-height: 3;">(.+?)</ul>' , re . DOTALL ) . findall ( o0000oO )
 oOOo0 = re . compile ( '<li><a href="/letters/(.+?)">(.+?)</a></li>' ) . findall ( str ( iI1I ) )
 for url , oo00O00oO in oOOo0 :
  oOOo0oo ( '[COLORgreen]' + oo00O00oO + '[/COLOR]' , 'http://watchseries.li/letters/' + url , 10049 , iIii1 + 'WATCHSERIES.png' , '' , '' )
  if 31 - 31: o00O0oo
def iIIiI1I1i ( url ) :
 o0000oO = oOoO0o00OO0 ( url )
 oOOo0 = re . compile ( '<a href="(.+?)" class="sr-header">(.+?)</a>' ) . findall ( o0000oO )
 for url , oo00O00oO in oOOo0 :
  oOOo0oo ( '[COLORgreen]' + oo00O00oO + '[/COLOR]' , 'http://watchseries.li/' + url , 10049 , iIii1 + 'WATCHSERIES.png' , '' , '' )
  if 68 - 68: o0000oOoOoO0o % O0oO + ii11ii1ii - i11iIiiIii . OOooOOo - O0oO
def IIIIIii1ii11 ( url ) :
 o0000oO = oOoO0o00OO0 ( url )
 oOOo0 = re . compile ( '<li class="col-md-6 col-xs-12 list-movies-li"><a href="(.+?)" title=".+?">(.+?)<span class="epnum">.+?</span></a></li>' , re . DOTALL ) . findall ( o0000oO )
 oOOOoo00 = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="(.+?)">Next</a></li></ul>' , re . DOTALL ) . findall ( o0000oO )
 for url , oo00O00oO in oOOo0 :
  oOOo0oo ( '[COLORgreen]' + ( oo00O00oO ) . replace ( '&nbsp;' , ' ' ) . replace ( '&amp;' , '&' ) . replace ( '&#039;' , '\'' ) + '[/COLOR]' , 'http://www.watchseries.li' + url , 10044 , iIii1 + 'WATCHSERIES.png' , '' , '' )
 for url in oOOOoo00 :
  oOOo0oo ( '[COLORgreen]' + 'NEXT' + '[/COLOR]' , 'http://www.watchseries.li' + url , 10049 , '' , '' , '' )
  if 86 - 86: I1IiI * OoOoOO00 - O0 . I1IiI % iIii1I11I1II1 / OoOO0ooOOoo0O
  if 11 - 11: OOOo0 * OoOO + ii11ii1ii / ii11ii1ii
def iiii1I1 ( ) :
 iiIi11iI1iii = Oo0o0000o0o0 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 IIIiIiI11iIi = 'http://www.watchseries.li/search/' + iiIi11iI1iii . replace ( ' ' , '%20' )
 o0000oO = oOoO0o00OO0 ( IIIiIiI11iIi )
 oOOo0 = re . compile ( '<img src="(.+?)".+?<a href="(.+?)" title=".+?"><b>(.+?)</b>' , re . DOTALL ) . findall ( o0000oO )
 for iiIiIIIiiI , oo000o , oo00O00oO in oOOo0 :
  if 'watch online' in oo00O00oO :
   pass
  else :
   oOOo0oo ( '[COLORgreen]' + oo00O00oO + '[/COLOR]' , 'http://www.watchseries.li' + oo000o , 10044 , iiIiIIIiiI , '' , '' )
   if 89 - 89: O0
   xbmcplugin . setContent ( Oo00OOOOO , 'movies' )
   if 2 - 2: ii11ii1ii . ii11ii1ii + ii11ii1ii * OOooOOo
def oOo00oOOOOO ( url ) :
 o0000oO = oOoO0o00OO0 ( url )
 oOOo0 = re . compile ( '<img src="(.+?)".+?<div class="block-left-home-inside-text">.+?<a href="(.+?)" title=".+?"><b>(.+?)</b> <br>.+?<span class=".+?">(.+?)</span></a><br>(.+?)<br>' , re . DOTALL ) . findall ( o0000oO )
 for iiIiIIIiiI , url , oo00O00oO , iIIII1i , ii1ii111 in oOOo0 :
  oOOo0oo ( '[COLORgreen]' + ( oo00O00oO ) . replace ( '&nbsp;' , ' ' ) . replace ( '&amp;' , '&' ) . replace ( '&#039;' , '\'' ) + ' - ' + ( iIIII1i ) . replace ( '&amp;' , '&' ) . replace ( '&#039;' , '\'' ) + '[/COLOR]' , 'http://www.watchseries.li' + url , 10045 , iiIiIIIiiI , '' , ii1ii111 )
  if 85 - 85: OoooooooOO - Ooo00oOo00o - O0oO / o0oO0 - o0000oOoOoO0o
def iIiI ( url ) :
 o0000oO = oOoO0o00OO0 ( url )
 oOOo0 = re . compile ( '<li class="col-md-6 col-xs-12 list-movies-li"><a href="(.+?)" title=".+?">(.+?)<span class="epnum">.+?</span></a></li>' , re . DOTALL ) . findall ( o0000oO )
 oOOOoo00 = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="(.+?)">Next</a></li></ul>' , re . DOTALL ) . findall ( o0000oO )
 for url , oo00O00oO in oOOo0 :
  oOOo0oo ( '[COLORgreen]' + ( oo00O00oO ) . replace ( '&nbsp;' , ' ' ) . replace ( '&amp;' , '&' ) . replace ( '&#039;' , '\'' ) + '[/COLOR]' , 'http://www.watchseries.li' + url , 10045 , iIii1 + 'WATCHSERIES.png' , '' , '' )
 for url in oOOOoo00 :
  oOOo0oo ( '[COLORgreen]' + 'NEXT' + '[/COLOR]' , 'http://www.watchseries.li' + url , 10046 , '' , '' , '' )
  if 5 - 5: Oo * I1IiI
def ii1I11iIiIII1 ( url ) :
 o0000oO = oOoO0o00OO0 ( url )
 oOOo0 = re . compile ( '<div class="mask">.+?<a href="(.+?)" title="(.+?)">.+?<img src="(.+?)"' , re . DOTALL ) . findall ( o0000oO )
 oOOOoo00 = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="(.+?)">Next</a></li></ul>' , re . DOTALL ) . findall ( o0000oO )
 for url , oo00O00oO , iiIiIIIiiI in oOOo0 :
  oOOo0oo ( '[COLORgreen]' + ( oo00O00oO ) . replace ( '&nbsp;' , ' ' ) . replace ( '&amp;' , '&' ) . replace ( '&#039;' , '\'' ) + '[/COLOR]' , 'http://www.watchseries.li' + url , 10044 , iiIiIIIiiI , '' , '' )
 for url in oOOOoo00 :
  oOOo0oo ( '[COLORgreen]' + 'NEXT' + '[/COLOR]' , 'http://www.watchseries.li' + url , 10041 , '' , '' , '' )
  if 52 - 52: OOooOOo * IIII + I1IiI
  if 49 - 49: iIii1I11I1II1 - O0 . i1IIi - OoooooooOO
def Ii1 ( url ) :
 o0000oO = oOoO0o00OO0 ( url )
 iI1I = re . compile ( '<div class="col-md-6 col-xs-12".+?<a href=".+?" itemprop="url"><span itemprop="name">(.+?)</span>(.+?)</ul>' , re . DOTALL ) . findall ( o0000oO )
 for I11I , i1II in iI1I :
  oOOo0 = re . compile ( '<li itemprop="episode".+?<meta itemprop="url" content="(.+?)">.+?<span class="" itemprop="name">\n(.+?)\n' , re . DOTALL ) . findall ( str ( i1II ) )
  for url , oo00O00oO in oOOo0 :
   oOOo0oo ( '[COLORgreen]' + I11I + ' ' + ( oo00O00oO ) . replace ( '' , '' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&amp;' , '&' ) . replace ( '&#039;' , '\'' ) . replace ( '  ' , '' ) + '[/COLOR]' , 'http://www.watchseries.li' + url , 10045 , iIii1 + 'WATCHSERIES.png' , '' , '' )
 oOOOoo00 = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="(.+?)">Next</a></li></ul>' , re . DOTALL ) . findall ( o0000oO )
 for url in oOOOoo00 :
  oOOo0oo ( '[COLORgreen]' + 'NEXT' + '[/COLOR]' , 'http://www.watchseries.li' + url , 10044 , '' , '' , '' )
  if 73 - 73: i1IIi + oO0o0ooO0 . i11iIiiIii
  if 5 - 5: OoOO . ii11ii1ii . OoOoOO00 . OoooooooOO
def Oo0OooO0 ( url ) :
 oO00oOo0OOO = [ ii1 ( url ) for ooOoOoOoO000OO in xrange ( 1 ) ]
 ii11II11 = [ ]
 if 70 - 70: iIii1I11I1II1
 for ii1Ii11IiiI1 in xrange ( len ( oO00oOo0OOO ) ) :
  iIi = oO00oOo0OOO [ ii1Ii11IiiI1 ]
  ii11II11 . append ( Thread ( target = ii1 ( url ) , args = ( iIi , ) , kwargs = { } ) )
  ii11II11 [ ii1Ii11IiiI1 ] . start ( )
  if 86 - 86: OoOoOO00 + o00O0oo % Ooo00oOo00o
 for oOooO0 in ii11II11 : oOooO0 . join ( )
 if 74 - 74: o0000oOoOoO0o - OoOO0ooOOoo0O + i1IIi . OOOo0 + OoOO0ooOOoo0O - o0000oOoOoO0o
 if 17 - 17: O0 . O0oO . O0 + O0 / Oo . o0oO0
def ii1 ( url ) :
 o0000oO = oOoO0o00OO0 ( url )
 oOOo0 = re . compile ( '<td>.+?<a href="/link/(.+?)".+?height="16px">(.+?)\n' , re . DOTALL ) . findall ( o0000oO )
 for url , oo00O00oO in oOOo0 :
  i1111 . create ( '' , '' , '' )
  ooO0oO00O0o = ooO0oO00O0o = 'http://www.watchseries.li/link/' + url
  if 'allmyvideos' in oo00O00oO :
   OO00OOoO0o ( ooO0oO00O0o )
   i1111 . update ( 15 , "Please Wait" , "Getting Allmyvideos Streams" )
  elif 'vidspot' in oo00O00oO :
   OO00OOoO0o ( ooO0oO00O0o )
   i1111 . update ( 30 , "Please Wait" , "Getting Vidspot Streams" )
  elif 'thevideo' in oo00O00oO :
   OO00OOoO0o ( ooO0oO00O0o )
   i1111 . update ( 45 , "Please Wait" , "Getting Thevideo Streams" )
  elif 'daclips' in oo00O00oO :
   OO00OOoO0o ( ooO0oO00O0o )
   i1111 . update ( 60 , "Please Wait" , "Getting Daclips Streams" )
  elif 'vodlocker' in oo00O00oO :
   OO00OOoO0o ( ooO0oO00O0o )
   i1111 . update ( 80 , "Please Wait" , "Getting Vodlocker Streams" )
  elif 'filehoot' in oo00O00oO :
   OO00OOoO0o ( ooO0oO00O0o )
   i1111 . update ( 100 , "Please Wait" , "Getting Filehoot Streams" )
  else :
   pass
   if 4 - 4: i1IIi - i11iIiiIii / i11iIiiIii / OoooooooOO
   if 100 - 100: Oo + OOooOOo - O0 % OoOoOO00 . oO0o0ooO0
   if 92 - 92: OoOoOO00 * OoooooooOO - O0oO
def OO00OOoO0o ( url ) :
 o0000oO = oOoO0o00OO0 ( url )
 iIi1I11I = re . compile ( '<IFRAME style=".+?" SRC="(.+?)"' ) . findall ( o0000oO )
 oOOOoo00 = re . compile ( '<IFRAME SRC="(.+?)"' ) . findall ( o0000oO )
 oOOo0 = re . compile ( '<iframe style=.+?" src="(.+?)"' ) . findall ( o0000oO )
 for url in iIi1I11I :
  oooo00 ( url )
 for url in oOOOoo00 :
  oooo00 ( url )
 for url in oOOo0 :
  oooo00 ( url )
  if 96 - 96: ii11ii1ii % o0oO0 % o00O0oo - o0oO0 % I1IiI + ii11ii1ii
def oooo00 ( url ) :
 if 'daclips.in' in url :
  o0000oO = oOoO0o00OO0 ( url )
  oOOo0 = re . compile ( '{ file: "(.+?)", type:"video" }' ) . findall ( o0000oO )
  for url in oOOo0 :
   iii1 ( '[COLORgreen]DACLIPS[/COLOR]' , url , 10012 , iIii1 + 'WATCHSERIES.png' )
 elif 'filehoot.com' in url :
  o0000oO = oOoO0o00OO0 ( url )
  oOOo0 = re . compile ( 'file: "(.+?)",.+?skin' , re . DOTALL ) . findall ( o0000oO )
  for url in oOOo0 :
   iii1 ( '[COLORgreen]FILEHOOT[/COLOR]' , url , 10012 , iIii1 + 'WATCHSERIES.png' )
 elif 'thevideo.me' in url :
  o0000oO = oOoO0o00OO0 ( url )
  oOOo0 = re . compile ( "{ label: '.+?', file: '(.+?)' }" ) . findall ( o0000oO )
  for url in oOOo0 :
   iii1 ( '[COLORgreen]THEVIDEO[/COLOR]' , url , 10012 , iIii1 + 'WATCHSERIES.png' )
 elif 'allmyvideos.net' in url :
  o0000oO = oOoO0o00OO0 ( url )
  oOOo0 = re . compile ( '"file" : "(.+?)",\n.+?"default" : .+?,\n.+?"label" : "(.+?)"' , re . DOTALL ) . findall ( o0000oO )
  for url , oo00O00oO in oOOo0 :
   iii1 ( '[COLORgreen]ALLMYVIDEOS - ' + oo00O00oO + '[/COLOR]' , url , 10012 , iIii1 + 'WATCHSERIES.png' )
 elif 'vidspot.net' in url :
  o0000oO = oOoO0o00OO0 ( url )
  oOOo0 = re . compile ( '"file" : "(.+?)",\n.+?"default" : .+?,\n.+?"label" : "(.+?)"' ) . findall ( o0000oO )
  for url , oo00O00oO in oOOo0 :
   iii1 ( '[COLORgreen]VIDSPOT - ' + oo00O00oO + '[/COLOR]' , url , 10012 , iIii1 + 'WATCHSERIES.png' )
 elif 'vodlocker' in url :
  o0000oO = oOoO0o00OO0 ( url )
  oOOo0 = re . compile ( 'file: "(.+?)",.+?skin' , re . DOTALL ) . findall ( o0000oO )
  for url in oOOo0 :
   iii1 ( '[COLORgreen]VODLOCKER[/COLOR]' , url , 10012 , iIii1 + 'WATCHSERIES.png' )
if 3 - 3: O0
if 64 - 64: i1IIi % o0oO0 / i11iIiiIii - i1IIi % OoOO0ooOOoo0O . oO0o0ooO0
if 8 - 8: Oo + OoOoOO00 * OoOO0ooOOoo0O * I1IiI * o0000oOoOoO0o / IIII
if 21 - 21: OoOO / OoooooooOO
if 11 - 11: OoOO0ooOOoo0O % o00O0oo - i11iIiiIii - OoOO + o0oO0 + IIII
if 87 - 87: O0oO * i1IIi / ii11ii1ii
if 6 - 6: OOooOOo + Oo - OoooooooOO % OoOO0ooOOoo0O * I1IiI
if 69 - 69: i1IIi
if 59 - 59: OoOoOO00 - OOooOOo
if 24 - 24: Oo - i1IIi + o0000oOoOoO0o
if 38 - 38: OoooooooOO / ii11ii1ii . O0 / i1IIi / Oo + iIii1I11I1II1
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
if 54 - 54: Oo + OOOo0 / oO0o0ooO0 . OOOo0 * I1IiI
if 1 - 1: I1IiI * Ooo00oOo00o . i1IIi / Oo . ii11ii1ii + Oo
if 17 - 17: Oo + Ooo00oOo00o / o00O0oo / oO0o0ooO0 * OoOO0ooOOoo0O
if 29 - 29: Ooo00oOo00o % OoooooooOO * OoOO / OoOoOO00 - OoOO
if 19 - 19: i11iIiiIii
if 54 - 54: OoOoOO00 . o0000oOoOoO0o
if 73 - 73: I1IiI . OOOo0
if 32 - 32: I1IiI * OOOo0 % o0oO0 * o00O0oo . O0
if 48 - 48: oO0o0ooO0 * oO0o0ooO0
if 13 - 13: o00O0oo / o0000oOoOoO0o + I1IiI . OOooOOo % o0oO0
if 48 - 48: OOOo0 / i11iIiiIii - OOooOOo * OoOO / OoooooooOO
if 89 - 89: iIii1I11I1II1 / OOOo0 - OoOoOO00 / o00O0oo . i11iIiiIii . o00O0oo
if 48 - 48: O0 + O0 . O0oO - o0oO0
if 63 - 63: OoOO
if 71 - 71: i1IIi . o00O0oo * oO0o0ooO0 % OoooooooOO + OoOO0ooOOoo0O
def iIIi1iiI1i11 ( ) :
 oOOo0oo ( '[COLORgreen]Highlights[/COLOR]' , '' , 10008 , iIii1 + 'ORIGINFOOTBALL.png' , iI111I11I1I1 , '' )
 oOOo0oo ( '[COLORgreen]Fixtures[/COLOR]' , '' , 10009 , iIii1 + 'ORIGINFOOTBALL.png' , iI111I11I1I1 , '' )
 if 56 - 56: OoooooooOO
def iiIIii ( ) :
 Iiii1i1 = oOoO0o00OO0 ( oOo0oooo00o ( 'aHR0cDovL2xpdmVvbnNhdC5jb20vcXVpY2tpbmRleC5odG1s' ) )
 oOOo0 = re . compile ( '<a target="_self" href="(.+?)".+?src="(.+?)" alt="(.+?)"' , re . DOTALL ) . findall ( Iiii1i1 )
 for oo000o , iiIiIIIiiI , oo00O00oO in oOOo0 :
  oOOo0oo ( '[COLORgreen]' + ( oo00O00oO ) . replace ( 'amp;' , '' ) + '[/COLOR]' , oOo0oooo00o ( 'aHR0cDovL2xpdmVvbnNhdC5jb20v' ) + oo000o , 10010 , oOo0oooo00o ( 'aHR0cDovL2xpdmVvbnNhdC5jb20v' ) + iiIiIIIiiI , iI111I11I1I1 , '' )
  if 86 - 86: o0000oOoOoO0o / OOooOOo - OOooOOo + ii11ii1ii + OoOO
def IIiooOoO0OO0oOO ( url ) :
 o0000oO = oOoO0o00OO0 ( url )
 iI1I = re . compile ( 'AndClearL.+?><h2.+?head>(.*?)float' , re . DOTALL ) . findall ( o0000oO )
 for iI1I in iI1I :
  II1i = re . compile ( '(.*?)</h2>' ) . findall ( str ( iI1I ) )
  for o0OO00oo in II1i :
   o0OO00oo = o0OO00oo
  i1i1IiIiIi1Ii = re . compile ( 'comp_head>(.*?)</span>.*?<div class = fLeft width = ".*?"><img src="(.*?)">.*?</div>.*?ST:(.*?)</div>(.+?)<!-- around all of channel types ENDS 2-->' , re . DOTALL ) . findall ( str ( iI1I ) )
  for oO0ooOO , iiIiIIIiiI , time , IIi1iI1 in i1i1IiIiIi1Ii :
   IIi11i1II = re . compile ( ",CAPTION, '(.+?)&nbsp" ) . findall ( IIi1iI1 )
   oOOo0oo ( '[COLORgreen]' + o0OO00oo + ' - ' + oO0ooOO + ' - ' + time + '[/COLOR]' , '' , 10010 , oOo0oooo00o ( 'aHR0cDovL2xpdmVvbnNhdC5jb20=' ) + iiIiIIIiiI , iI111I11I1I1 , ( str ( IIi11i1II ) ) )
   if 73 - 73: OOooOOo - OOOo0 * i1IIi / i11iIiiIii * OoOO0ooOOoo0O % OoOoOO00
 I11II1i ( 'tvshows' , 'Media Info 3' )
 if 56 - 56: OoooooooOO * Oo . Oo . ii11ii1ii
def II1 ( ) :
 if 74 - 74: OoooooooOO % OoOO0ooOOoo0O % O0oO - OOOo0 - o0000oOoOoO0o
 oOOo0oo ( '[COLORgreen]Shows[/COLOR]' , 'http://www.fullmatchesandshows.com/category/show/' , 10011 , 'http://www.fm-base.co.uk/forum/attachments/club-competition-logos/3885-soccer-am-logo-socceram.png' , iIii1 + 'fanart.jpg' , '' )
 oOOo0oo ( '[COLORgreen]Premier League[/COLOR]' , 'http://www.fullmatchesandshows.com/premier-league/' , 10011 , 'https://footballseasons.files.wordpress.com/2013/05/premier-league.png' , iIii1 + 'fanart.jpg' , '' )
 oOOo0oo ( '[COLORgreen]La Liga[/COLOR]' , 'http://www.fullmatchesandshows.com/la-liga/' , 10011 , 'http://1.bp.blogspot.com/-c6kQ40ryhyo/U19cUlz25sI/AAAAAAAABak/qtn5chSFZm0/s1600/la-liga-logo_display_image.png' , iIii1 + 'fanart.jpg' , '' )
 oOOo0oo ( '[COLORgreen]Bundesliga[/COLOR]' , 'http://www.fullmatchesandshows.com/bundesliga/' , 10011 , 'http://m.img.brothersoft.com/iphone/189/518670189_icon175x175.jpg' , iIii1 + 'fanart.jpg' , '' )
 oOOo0oo ( '[COLORgreen]Champions League[/COLOR]' , 'http://www.fullmatchesandshows.com/champions-league/' , 10011 , 'http://www.ecursuri.ro/images/teste/test-champions-league.jpg' , iIii1 + 'fanart.jpg' , '' )
 oOOo0oo ( '[COLORgreen]Serie A[/COLOR]' , 'http://www.fullmatchesandshows.com/category/serie-a/' , 10011 , 'http://files.jcriccione.it/200000223-2484526782/serie%20a.png' , iIii1 + 'fanart.jpg' , '' )
 oOOo0oo ( '[COLORgreen]Ligue 1[/COLOR]' , 'http://www.fullmatchesandshows.com/category/ligue-1/' , 10011 , 'http://a1.mzstatic.com/us/r30/Purple5/v4/37/c7/44/37c744ae-5824-42b7-6ce0-5f471f52baab/icon180x180.jpeg' , iIii1 + 'fanart.jpg' , '' )
 oOOo0oo ( '[COLORgreen]Copa America 2015[/COLOR]' , 'http://www.fullmatchesandshows.com/copa-america-2015/' , 10011 , 'https://pbs.twimg.com/profile_images/521966985907691520/Nq9OAPIo_400x400.png' , iIii1 + 'fanart.jpg' , '' )
 oOOo0oo ( '[COLORgreen]CONCACAF[/COLOR]' , 'http://www.fullmatchesandshows.com/category/concacaf/' , 10011 , 'http://a3.mzstatic.com/us/r30/Purple3/v4/40/26/14/4026147c-7022-4ca3-504e-e78950cc3f1c/icon175x175.png' , iIii1 + 'fanart.jpg' , '' )
 oOOo0oo ( '[COLORgreen]Women World Cup[/COLOR]' , 'http://www.fullmatchesandshows.com/category/women-world-cup/' , 10011 , 'https://upload.wikimedia.org/wikipedia/en/thumb/7/76/2015_FIFA_Women\'s_World_Cup_logo.svg/967px-2015_FIFA_Women\'s_World_Cup_logo.svg.png' , iIii1 + 'fanart.jpg' , '' )
 if 58 - 58: O0
def oO00oOOo0Oo ( url ) :
 o0000oO = oOoO0o00OO0 ( url )
 oOOo0 = re . compile ( 'itemprop="image" class="entry-thumb" src="(.+?)".+?<h3 itemprop="name" class="entry-title td-module-title"><a itemprop="url" href="(.+?)" rel="bookmark" title=".+?">(.+?)</a></h3>' , re . DOTALL ) . findall ( o0000oO )
 for iiIiIIIiiI , url , oo00O00oO in oOOo0 :
  IIiIIIIii = oo00O00oO . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' )
  iii1 ( '[COLORgreen]' + IIiIIIIii + '[/COLOR]' , url , 10013 , iiIiIIIiiI )
  if 40 - 40: O0
def ooO0oo ( url ) :
 o0000oO = oOoO0o00OO0 ( url )
 oOOo0 = re . compile ( '<script data-config="(.+?)" data-height' ) . findall ( o0000oO )
 for O0OoO0ooOO0o in oOOo0 :
  ooO0oo0o0 = ( O0OoO0ooOO0o ) . replace ( '/v2' , '' ) . replace ( 'zeus.json' , 'video-sd.mp4?hosting_id=21772' ) . replace ( 'config.playwire.com' , 'cdn.video.playwire.com' )
  II11iIIiiiII ( 'http:' + ooO0oo0o0 )
  if 9 - 9: OOOo0 + ii11ii1ii / OOOo0 . OoOO * o0oO0
  if 45 - 45: i11iIiiIii
def o00oo0 ( ) :
 Iiii1i1 = OO ( oOo0oooo00o ( 'aHR0cDovL2pvaG5sb2NrZXIuY29tLw==' ) )
 oOOo0 = re . compile ( '<li id="menu-item-.+?" class=".+?"><a href="(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( Iiii1i1 )
 for oo000o , oo00O00oO in oOOo0 :
  o0OoOO000ooO0 ( oo00O00oO , oo000o , 8046 , iIii1 + 'documentary.png' )
def Oo0oOooOoOo ( url ) :
 Iiii1i1 = OO ( url )
 oOOo0 = re . compile ( 'data-type="inline" href="(.+?)" >.+?src="(.+?)" class="entry-thumbnail wp-post-image" alt="(.+?)" itemprop="image"' , re . DOTALL ) . findall ( Iiii1i1 )
 oOOOoo00 = re . compile ( 'class="inactive">.+?</a><a href="(.+?)">Next</a></div>' , re . DOTALL ) . findall ( Iiii1i1 )
 for url , iiIiIIIiiI , oo00O00oO in oOOo0 :
  iii1 ( ( oo00O00oO ) . replace ( '&#8211;' , '-' ) . replace ( '&#8217;' , '' ) , url , 8047 , iiIiIIIiiI )
 for url in oOOOoo00 :
  o0OoOO000ooO0 ( 'NEXT PAGE' , url , 8046 , iIii1 + 'documentary.png' )
  if 49 - 49: OoOO0ooOOoo0O . ii11ii1ii . i11iIiiIii - OoOoOO00 / o00O0oo
def ooOo0O0o0 ( url ) :
 Iiii1i1 = OO ( url )
 oOOo0 = re . compile ( "src='http://www.youtube.com/embed/(.+?)?version=3&#038;rel=1&#038;fs=1&#038;autohide=2&#038;showsearch=0&#038;showinfo=1&#038;iv_load_policy=1&#038;wmode=transparent' frameborder='0' allowfullscreen='true'></iframe>" ) . findall ( Iiii1i1 )
 for url in oOOo0 :
  yt . PlayVideo ( url )
  if 65 - 65: o0oO0 + O0
def IiII1iiI ( ) :
 Iiii1i1 = OO ( oOo0oooo00o ( 'aHR0cDovL3RvcGRvY3VtZW50YXJ5ZmlsbXMuY29tLw==' ) )
 oOOo0 = re . compile ( '<a href="(.+?)" >(.+?)</a></li><li>' ) . findall ( Iiii1i1 )
 for oo000o , oo00O00oO in oOOo0 :
  o0OoOO000ooO0 ( oo00O00oO , oo000o , 8041 , iIii1 + 'documentary.png' )
def iII ( url ) :
 Iiii1i1 = OO ( url )
 oOOo0 = re . compile ( '<h2><a href="(.+?)" title="(.+?)">.+?</a></h2>.+?src="(.+?)"' , re . DOTALL ) . findall ( Iiii1i1 )
 oOOOoo00 = re . compile ( 'class="inactive">.+?</a><a href="(.+?)">Next</a></div>' , re . DOTALL ) . findall ( Iiii1i1 )
 for url , oo00O00oO , iiIiIIIiiI in oOOo0 :
  o0OoOO000ooO0 ( ( oo00O00oO ) . replace ( '&#039;s' , '' ) , url , 8042 , iiIiIIIiiI )
 for url in oOOOoo00 :
  o0OoOO000ooO0 ( 'NEXT PAGE' , url , 8041 , iIii1 + 'documentary.png' )
  if 63 - 63: OOooOOo * oO0o0ooO0
  if 63 - 63: oO0o0ooO0 * ii11ii1ii . OoooooooOO / OoOO0ooOOoo0O * Oo . o0oO0
def Ooo0 ( url ) :
 Iiii1i1 = OO ( url )
 oOOo0 = re . compile ( '<meta itemprop="name" content="(.+?)".+?<meta itemprop="thumbnailUrl" content="(.+?)".+?<meta itemprop="embedUrl" content="(.+?)".+?<meta itemprop="description" content="(.+?)" />' , re . DOTALL ) . findall ( Iiii1i1 )
 oOOOoo00 = re . compile ( '<div class="video new-video"><iframe width="766" height="431" src="(.+?)&amp;iv_load_policy=3&amp;showinfo=0&amp;autohide=1"' , re . DOTALL ) . findall ( Iiii1i1 )
 for oo00O00oO , iiIiIIIiiI , url , oooO00o0 in oOOo0 :
  iii1 ( ( oo00O00oO ) . replace ( '&#039;s' , '' ) , url . replace ( 'https://www.youtube.com/embed/' , '' ) , 8043 , iiIiIIIiiI )
 for url in oOOOoo00 :
  o0o00oO0oo000 ( ( url ) . replace ( '//' , 'http://' ) )
  if 89 - 89: Ooo00oOo00o + IIII * O0oO
def o0o00oO0oo000 ( url ) :
 Iiii1i1 = OO ( url )
 oOOo0 = re . compile ( '<link rel="canonical" href="(.+?)">  <link rel="stylesheet"' ) . findall ( Iiii1i1 )
 for url in oOOo0 :
  iii1 ( 'PLAY' , ( url ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , iIii1 + 'documentary.png' )
  if 28 - 28: OoooooooOO . OoOO % ii11ii1ii / i1IIi / OoOO0ooOOoo0O
def III1I1I ( ) :
 o0000oO = OO ( 'http://www.stream2watch.co/live-tv' )
 oOOo0 = re . compile ( '<a href="(.+?)">.+?<img src="(.+?)" alt=".+?"/>.+?<span class="country_name">(.+?)<br />(.+?)</span>' , re . DOTALL ) . findall ( o0000oO )
 for oo000o , iiIiIIIiiI , oo00O00oO , i1i111i1 in oOOo0 :
  o0OoOO000ooO0 ( ( oo00O00oO + '[COLORgreen]' + i1i111i1 + '[/COLOR]' ) , oo000o , 8086 , iiIiIIIiiI )
  if 99 - 99: OOOo0 + i1IIi + i11iIiiIii + Oo % OoOO / o0000oOoOoO0o
def O0OO0o0OO0OO ( url ) :
 o0000oO = OO ( url )
 oOOo0 = re . compile ( '<a class="front_channel_href" href="(.+?)" title=".+?">.+?<img class="front_channel_thumb" src="(.+?)" alt=".+?"/>.+?<span class="front_channel_name">(.+?)</span>' , re . DOTALL ) . findall ( o0000oO )
 for url , iiIiIIIiiI , oo00O00oO in oOOo0 :
  o0OoOO000ooO0 ( '[COLORgreen]' + oo00O00oO + '[/COLOR]' , url , 8087 , iiIiIIIiiI )
  if 64 - 64: OoOoOO00
def iIIIiIi1I1i ( url ) :
 o0000oO = oOoO0o00OO0 ( url )
 oOOo0 = re . compile ( 'a id="code_.+?data-f-href="(.+?)" data-code-embed="">(.+?)</a>' , re . DOTALL ) . findall ( o0000oO )
 for url , oo00O00oO in oOOo0 :
  OoOOoO0oOo ( url , oo00O00oO )
  if 70 - 70: o0000oOoOoO0o % iIii1I11I1II1 . Oo + Oo - OOooOOo % O0oO
def OoOOoO0oOo ( url , name ) :
 o0000oO = oOoO0o00OO0 ( url )
 oOOo0 = re . compile ( "playStream\('.+?', '(.+?)'\);" , re . DOTALL ) . findall ( o0000oO )
 for url in oOOo0 :
  print url
  iii1 ( '[COLORgreen]' + name + '[/COLOR]' , url , 222 , '' )
  if 38 - 38: O0oO % OoOO0ooOOoo0O - OoooooooOO
def oOo0OOoooO ( ) :
 Iiii1i1 = OO ( oOo0oooo00o ( 'aHR0cDovL2JyYXR1LW1hcmlhbi5yby8=' ) )
 oOOo0 = re . compile ( '<tr><td ><img width="25" height="25" src="(.+?)" alt="" /> </td>.+?<td >(.+?)</td>.+?<td >(.+?)</td>.+?<td >(.+?)</td>.+?<td >(.+?)</td>.+?<td >    <a class="wp-colorbox-youtube" href="(.+?)">Watch Online</a></td>.+?</tr>' , re . DOTALL ) . findall ( Iiii1i1 )
 for iiIiIIIiiI , time , iIi1iIIIiIiI , oO0ooOO , i1i1IiIiIi1Ii , oo000o in oOOo0 :
  o0OoOO000ooO0 ( ( time + '[COLORgreen]' + i1i1IiIiIi1Ii + '[/COLOR]' + oO0ooOO ) . replace ( '&#8211;' , ':' ) . replace ( '&ndash;' , '-' ) , oo000o , 8061 , iiIiIIIiiI )
def OooOo000o0o ( url ) :
 Iiii1i1 = OO ( url )
 oOOo0 = re . compile ( 'type:.+?,.+?url: "(.+?)"' , re . DOTALL ) . findall ( Iiii1i1 )
 for url in oOOo0 :
  iii1 ( '[COLORgreen]LINK 1[/COLOR]' , url , 222 , iIii1 + 'documentary.png' )
  if 42 - 42: OoOO % OoOO0ooOOoo0O
def OOO0 ( ) :
 o0000oO = oOoO0o00OO0 ( oOo0oooo00o ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vbTN1c3RyZWFtcw==' ) )
 oOOo0 = re . compile ( '<li><a href="(.+?)"> (.+?).m3u</a></li>' ) . findall ( o0000oO )
 for oo000o , oo00O00oO in oOOo0 :
  o0OoOO000ooO0 ( ( '[COLORgreen]' + oo00O00oO + '[/COLOR]' ) . replace ( '-' , ' ' ) . replace ( '_' , ' ' ) , ( oOo0oooo00o ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vbTN1c3RyZWFtcy8=' ) ) + oo000o , 8071 , iIii1 + 'streams.png' )
def iIiIIi ( url ) :
 o0000oO = OO ( url )
 oOOo0 = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( o0000oO )
 for oo00O00oO , url in oOOo0 :
  iii1 ( ( '[COLORgreen]' + oo00O00oO + '[/COLOR]' ) . replace ( '_' , ' ' ) , ( url ) . strip ( ) , 404 , iIii1 + 'streams.png' )
def III1I ( url ) :
 o0000oO = OO ( url )
 oOOo0 = re . compile ( 'EXTINF:(.+?),(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( o0000oO )
 for iiIiIIIiiI , oo00O00oO , url in oOOo0 :
  iii1 ( ( '[COLORgreen]' + oo00O00oO + '[/COLOR]' ) . replace ( '_' , ' ' ) , ( ( oOo0oooo00o ( 'aHR0cDovL2dlbmlldHYuaXB0di5yZTo4MDAwL2xpdmUv' ) ) + oooOOOOO + '/' + i1iiIII111ii + url ) . strip ( ) , 222 , iiIiIIIiiI )
  if 11 - 11: o0oO0 - OoOO0ooOOoo0O + o0oO0 * OoOO / OOOo0
def OoOOOO ( ) :
 o0000oO = oOoO0o00OO0 ( oOo0oooo00o ( 'aHR0cDovL3d3dy54bnh4LmNvbS8=' ) )
 oOOo0 = re . compile ( '<a href="(.+?)">(.+?)</a><br>' ) . findall ( o0000oO )
 for oo000o , oo00O00oO in oOOo0 :
  o0OoOO000ooO0 ( ( '[COLORgreen]' + oo00O00oO + '[/COLOR]' ) , oo000o , 8091 , iIii1 + 'streams.png' )
def I1iiIi111I ( url ) :
 o0000oO = OO ( url )
 oOOo0 = re . compile ( '<a href="(.+?)".+?src="(.+?)".+?title="(.+?)">' , re . DOTALL ) . findall ( o0000oO )
 for url , iiIiIIIiiI , oo00O00oO in oOOo0 :
  iii1 ( ( '[COLORgreen]' + oo00O00oO + '[/COLOR]' ) , url , 8092 , iiIiIIIiiI )
def Iiii1iIii ( url ) :
 o0000oO = OO ( url )
 oOOo0 = re . compile ( 'src=&quot;(.+?)&quot;' ) . findall ( o0000oO )
 for url in oOOo0 :
  oOoooO000O ( url )
  if 49 - 49: OOooOOo * o00O0oo + o0000oOoOoO0o + oO0o0ooO0
def IIi11 ( url ) :
 ooo0O0OOO000o = urllib2 . Request ( url )
 ooo0O0OOO000o . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
 iiI1iii = ''
 ooo0O = ''
 try :
  iiI1iii = urllib2 . urlopen ( ooo0O0OOO000o )
  ooo0O = iiI1iii . read ( )
  iiI1iii . close ( )
 except : pass
 if ooo0O != '' :
  return ooo0O
 else :
  ooo0O = 'Failed'
  return ooo0O
  if 79 - 79: Ooo00oOo00o * I1IiI . OoooooooOO - o0000oOoOoO0o * OOooOOo
def o000o0O0Oo00 ( ) :
 ooOOoOo = ( oOo0oooo00o ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 iiIi11iI1iii = Oo0o0000o0o0 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oo000 = iiIi11iI1iii . lower ( )
 oo000o = ( oOo0oooo00o ( 'aHR0cDovL2RsNC5tb3ZpZWZhcnNpLmNvbS9maWxtLzIwMTUtNy8=' ) )
 iIIi = ( oOo0oooo00o ( 'aHR0cDovL2RsLmF2YWRsLmNvbS9OZXcvTW92aWUv' ) )
 oooO = ( oOo0oooo00o ( 'aHR0cDovLzIxNy4yMTkuMTQzLjEwOC8xMzI3Lw==' ) )
 iiIIi = ( oOo0oooo00o ( 'aHR0cDovLzE3OC4xNjIuMjE0LjIzMi92b2QvbW92aWVzL2VuZ2xpc2gv' ) )
 i1i = ( oOo0oooo00o ( 'aHR0cDovL3Njb29ieXN0cmVhbS54MTBob3N0LmNvbS8vc2Nvb2J5L21vdi9hbGwucGhw' ) )
 iIIiI1iiI = ( oOo0oooo00o ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 I11Ii111I = ( oOo0oooo00o ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL3NlYXJjaC8/cT0=' ) ) + iiIi11iI1iii
 Oo00OO0 = ( oOo0oooo00o ( 'aHR0cDovL2xldHdhdGNoLnVzLz9vcD1zZWFyY2gmaz0=' ) ) + ( iiIi11iI1iii ) . replace ( ' ' , '+' )
 oo0O = ( oOo0oooo00o ( 'aHR0cDovL3d3dy5pemxlbWV5ZWRlZ2VyLmNvbS9hcmFtYT9xPQ==' ) ) + iiIi11iI1iii
 if 92 - 92: OoOO0ooOOoo0O % IIII % I1IiI
 o0000oO = IIi11 ( oo000o )
 OoOOO = IIi11 ( iIIi )
 iIi1Ii = IIi11 ( oooO )
 IiI1IIIII1I = IIi11 ( iiIIi )
 I1I1IiIi1 = IIi11 ( i1i )
 oOO0o0oo0 = IIi11 ( I11Ii111I )
 oOo000O = oOoO0o00OO0 ( Oo00OO0 )
 iIIooO0o0O0Oo = oOoO0o00OO0 ( oo0O )
 if 1 - 1: iIii1I11I1II1 + Oo / O0 - oO0o0ooO0 % IIII + IIII
 if iIIooO0o0O0Oo != 'Failed' :
  IiIIII = re . compile ( '<div class="inner">.+?<li>.+?<a href="(.+?)">.+?<img src="(.+?)" alt.+?<span class="year">(.+?)</span>.+?<span class="video-title">(.+?)</span>.+?</li>.+?</div>' , re . DOTALL ) . findall ( iIIooO0o0O0Oo )
  for oo000o , iiIiIIIiiI , i1i1ii , oo00O00oO in IiIIII :
   oo00O00oO = ( oo00O00oO ) . replace ( '  ' , '' ) . replace ( '\\t' , '' ) . replace ( '\\r' , '' ) . replace ( '\\n' , '' ) . replace ( '\\xc3\\x87' , '' ) + ' ' + ( i1i1ii ) . replace ( '  ' , '' ) . replace ( '\\t' , '' ) . replace ( '\\r' , '' ) . replace ( '\\n' , '' )
   iIiIIIi = iiIiIIIiiI
   oo000o = oo000o
   iII1ii1 ( oo00O00oO , iIiIIIi , oo000o )
   xbmcplugin . addSortMethod ( Oo00OOOOO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if o0000oO != 'Failed' :
  oOOo0 = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( o0000oO )
  for i11i11 , oo00O00oO in oOOo0 :
   if iiIi11iI1iii in oo00O00oO . lower ( ) :
    iii1 ( ( '[COLORgreen]' + oo00O00oO + '- source 1[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( oo000o + i11i11 ) , 222 , '' )
 if OoOOO != 'Failed' :
  oOOOoo00 = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( OoOOO )
  for i11i11 , oo00O00oO in oOOOoo00 :
   if iiIi11iI1iii in oo00O00oO . lower ( ) :
    iii1 ( ( '[COLORgreen]' + oo00O00oO + '- source 2[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( iIIi + i11i11 ) , 222 , '' )
 if iIi1Ii != 'Failed' :
  iIi1I11I = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( iIi1Ii )
  for i11i11 , oo00O00oO in iIi1I11I :
   if iiIi11iI1iii in oo00O00oO . lower ( ) :
    iii1 ( ( '[COLORgreen]' + oo00O00oO + '- source 3[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( oooO + i11i11 ) , 222 , '' )
 if IiI1IIIII1I != 'Failed' :
  i1iiIII1IIiIIII = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( IiI1IIIII1I )
  for i11i11 , oo00O00oO in i1iiIII1IIiIIII :
   if iiIi11iI1iii in oo00O00oO . lower ( ) :
    iii1 ( ( '[COLORgreen]' + oo00O00oO + '- source 4[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( iiIIi + i11i11 ) , 222 , '' )
 if I1I1IiIi1 != 'Failed' :
  I1iIIII1 = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( I1I1IiIi1 )
  for i11i11 , iiIiIIIiiI , oo00O00oO in I1iIIII1 :
   if iiIi11iI1iii in oo00O00oO . lower ( ) :
    o0OoOO000ooO0 ( ( '[COLORgreen]' + oo00O00oO + '- source Scooby[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( 'Ganool' , '' ) . replace ( 'ShAaNiG' , '' ) . replace ( 'YIFY' , '' ) . replace ( '[[ Max-Movie.In ]]' , '' ) . replace ( '.mkv' , '' ) . replace ( '.mp4' , '' ) . replace ( '.' , ' ' ) , i11i11 , 1006 , 'img' )
    if 57 - 57: I1IiI . iIii1I11I1II1 % o0oO0 % o00O0oo * I1IiI
    I11II1i ( 'tvshows' , 'Media Info 3' )
 if oOO0o0oo0 != 'Failed' :
  II1o0ooO0OOO = re . compile ( 'href="(.+?)".+?src="(.+?)" alt="Image of (.+?)"' , re . DOTALL ) . findall ( oOO0o0oo0 )
  for oo000o , iiIiIIIiiI , oo00O00oO in II1o0ooO0OOO :
   if iiIi11iI1iii in oo00O00oO . lower ( ) :
    o0OoOO000ooO0 ( ( '[COLORgreen]' + oo00O00oO + '- source Snag[/COLOR]' ) . replace ( '&#x27;' , '' ) , 'http://www.snagfilms.com' + oo000o , 7067 , iiIiIIIiiI )
    if 74 - 74: o00O0oo * i11iIiiIii / O0oO
    I11II1i ( 'tvshows' , 'Media Info 3' )
 if oOo000O != 'Failed' :
  OoOoo00O = re . compile ( '<div class="video_block video_block_default ">.+?<a href="#">.+?<a href="(.*?)".+?<img src="(.+?)" height=".+?" alt="(.+?)"' , re . DOTALL ) . findall ( oOo000O )
  for oo000o , iiIiIIIiiI , oo00O00oO in OoOoo00O :
   iii1 ( '[COLORgreen]' + oo00O00oO + '- Source 7[/COLOR]' , oo000o , 222 , iiIiIIIiiI )
 O0OOO0OOooo00 = [ '0-9/' , 'A/' , 'B/' , 'C/' , 'D/' , 'E/' , 'F/' , 'G/' , 'H/' , 'I/' , 'J/' , 'K/' , 'L/' , 'M/' , 'N/' , 'O/' , 'P/' , 'R/' , 'S/' , 'T/' , 'U/' , 'V/' , 'W/' , 'X/' , 'Y/' , 'Z/' ]
 if 29 - 29: OOooOOo
 if 86 - 86: OoOoOO00 . IIII
 for II11iI111i1 in O0OOO0OOooo00 :
  Oo00OoOo = ooOOoOo + II11iI111i1
  iIiIoO00Ooo0oO = IIi11 ( Oo00OoOo )
  if I1I1IiIi1 != 'Failed' :
   OOOoo0ooOo00O = re . compile ( '<li><a href="(.+?)"> (.+?)</a></li>' ) . findall ( iIiIoO00Ooo0oO )
   for i11i11 , oo00O00oO in OOOoo0ooOo00O :
    if iiIi11iI1iii in oo00O00oO . lower ( ) :
     iii1 ( ( '[COLORgreen]' + oo00O00oO + 'source 5[/COLOR]' ) . replace ( 'Ganool' , '' ) . replace ( 'ShAaNiG' , '' ) . replace ( 'YIFY' , '' ) . replace ( '[[ Max-Movie.In ]]' , '' ) . replace ( '.mkv' , '' ) . replace ( '.mp4' , '' ) . replace ( '.' , ' ' ) , ( ooOOoOo + II11iI111i1 + i11i11 ) , 222 , '' )
     if 38 - 38: iIii1I11I1II1 + i11iIiiIii * Ooo00oOo00o * o0oO0 % OoOO0ooOOoo0O
     I11II1i ( 'tvshows' , 'Media Info 3' )
     if 5 - 5: o0oO0 - O0oO + OOOo0 * O0 / Oo - o00O0oo
     if 75 - 75: OoooooooOO - OoOO0ooOOoo0O + OOooOOo / oO0o0ooO0 % i11iIiiIii
def iiiiii1 ( ) :
 if 66 - 66: OoOO * iIii1I11I1II1 % iIii1I11I1II1 * IIII - o0oO0 - IIII
 iiIi11iI1iii = Oo0o0000o0o0 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oo000 = iiIi11iI1iii . lower ( )
 oo000o = ( oOo0oooo00o ( 'aHR0cDovL2RsLmZhcnNpbW92aWUubmV0L1NlcmlhbC8=' ) )
 iIIi = ( oOo0oooo00o ( 'aHR0cDovL3N2Mi5kbC1wYXJzLmluLw==' ) )
 oooO = ( oOo0oooo00o ( 'aHR0cDovL3R2LmRsLXBhcnMuaW4v' ) )
 iiIIi = ( oOo0oooo00o ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9BbWVyaWNhbiUyMFNlcmlhbC8=' ) )
 i1i = ( oOo0oooo00o ( 'aHR0cDovL2RpemlsYWIuY29tL2Fyc2l2P2xpbWl0PSZ0dXI9Jm9yZGVyYnk9JnVsa2U9Jm9yZGVyPSZ5aWw9JmRpemlfYWRpPQ==' ) ) + ( iiIi11iI1iii ) . replace ( ' ' , '+' )
 iIIiI1iiI = ( oOo0oooo00o ( 'aHR0cDovL3Njb29ieXN0cmVhbS54MTBob3N0LmNvbS8vc2Nvb2J5L3Nob3dzL3R2YWxsLnBocA==' ) )
 Oo00OO0 = ( oOo0oooo00o ( 'aHR0cDovL2xldHdhdGNoLnVzLz9vcD1zZWFyY2gmaz0=' ) ) + ( iiIi11iI1iii ) . replace ( ' ' , '+' )
 oo0O = ( oOo0oooo00o ( 'aHR0cDovL3d3dy53YXRjaHNlcmllcy5saS9zZWFyY2gv' ) ) + iiIi11iI1iii . replace ( ' ' , '%20' )
 if 70 - 70: O0oO + OoOO
 o0000oO = IIi11 ( oo000o )
 OoOOO = IIi11 ( iIIi )
 iIi1Ii = IIi11 ( oooO )
 IiI1IIIII1I = IIi11 ( iiIIi )
 I1I1IiIi1 = cloudflare . source ( i1i )
 iIiIoO00Ooo0oO = IIi11 ( iIIiI1iiI )
 oOo000O = oOoO0o00OO0 ( Oo00OO0 )
 iIIooO0o0O0Oo = oOoO0o00OO0 ( oo0O )
 if o0000oO != 'Failed' :
  oOOo0 = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( o0000oO )
  for oo00O00oO in oOOo0 :
   if iiIi11iI1iii in oo00O00oO . lower ( ) :
    o0OoOO000ooO0 ( ( '[COLORgreen]' + oo00O00oO + ' source 1[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( oo000o + oo00O00oO ) . replace ( ' ' , '%20' ) , 1006 , '' )
    if 93 - 93: O0oO + o00O0oo
    I11II1i ( 'tvshows' , 'Media Info 3' )
 if OoOOO != 'Failed' :
  oOOOoo00 = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( OoOOO )
  for oo00O00oO in oOOOoo00 :
   if iiIi11iI1iii in oo00O00oO . lower ( ) :
    o0OoOO000ooO0 ( ( '[COLORgreen]' + oo00O00oO + ' source 2[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( iIIi + oo00O00oO ) . replace ( ' ' , '%20' ) , 1006 , '' )
    if 33 - 33: O0
    I11II1i ( 'tvshows' , 'Media Info 3' )
 if iIi1Ii != 'Failed' :
  iIi1I11I = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( iIi1Ii )
  for oo00O00oO in oOOOoo00 :
   if iiIi11iI1iii in oo00O00oO . lower ( ) :
    o0OoOO000ooO0 ( ( '[COLORgreen]' + oo00O00oO + ' source 3[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( oooO + oo00O00oO ) . replace ( ' ' , '%20' ) , 1006 , '' )
    if 78 - 78: O0 / OoOoOO00 * Ooo00oOo00o
    I11II1i ( 'tvshows' , 'Media Info 3' )
 if IiI1IIIII1I != 'Failed' :
  i1iiIII1IIiIIII = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( IiI1IIIII1I )
  for oo00O00oO in oOOOoo00 :
   if iiIi11iI1iii in oo00O00oO . lower ( ) :
    o0OoOO000ooO0 ( ( '[COLORgreen]' + oo00O00oO + ' source 4[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( iiIIi + oo00O00oO ) . replace ( ' ' , '%20' ) , 1006 , '' )
    if 50 - 50: OoooooooOO - iIii1I11I1II1 + i1IIi % O0oO - iIii1I11I1II1 % O0
    I11II1i ( 'tvshows' , 'Media Info 3' )
 if I1I1IiIi1 != 'Failed' :
  I1iIIII1 = re . compile ( '<a href="(.+?)" class="film-image">\n<img src="(.+?)" alt=""/>\n</a>\n<div class="tss-detail">\n<a class="title" style="" href=".+?">\n<span class="position">.+?</span>\n(.+?)</a>' ) . findall ( I1I1IiIi1 )
  for oo000o , iiIiIIIiiI , oo00O00oO in I1iIIII1 :
   if iiIi11iI1iii in oo00O00oO . lower ( ) :
    o0OoOO000ooO0 ( '[COLORgreen]' + oo00O00oO + ' - Source - Dizi[/COLOR]' , oo000o , 8062 , iiIiIIIiiI )
    if 58 - 58: IIII + iIii1I11I1II1
    I11II1i ( 'tvshows' , 'Media Info 3' )
 if iIiIoO00Ooo0oO != 'Failed' :
  OOOoo0ooOo00O = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( iIiIoO00Ooo0oO )
  for oo000o , iiIiIIIiiI , oo00O00oO in OOOoo0ooOo00O :
   if iiIi11iI1iii in oo00O00oO . lower ( ) :
    iii1 ( ( '[COLORgreen]' + oo00O00oO + '- Source Scooby[/COLOR]' ) , oo000o , 222 , 'img' )
    if 65 - 65: OoOoOO00 - O0oO % OOooOOo - I1IiI * oO0o0ooO0 + o00O0oo
    I11II1i ( 'tvshows' , 'Media Info 3' )
 if oOo000O != 'Failed' :
  OoOoo00O = re . compile ( '<div class="video_block video_block_default ">.+?<a href="#">.+?<a href="(.*?)".+?<img src="(.+?)" height=".+?" alt="(.+?)"' , re . DOTALL ) . findall ( oOo000O )
  for oo000o , iiIiIIIiiI , oo00O00oO in OoOoo00O :
   iii1 ( '[COLORgreen]' + oo00O00oO + ' - Source DiZzY[/COLOR]' , oo000o , 222 , iiIiIIIiiI )
 if iIIooO0o0O0Oo != 'Failed' :
  IiIIII = re . compile ( '<img src="(.+?)".+?<a href="(.+?)" title=".+?"><b>(.+?)</b>' , re . DOTALL ) . findall ( iIIooO0o0O0Oo )
  for iiIiIIIiiI , oo000o , oo00O00oO in IiIIII :
   if 'watch online' in oo00O00oO :
    pass
   else :
    oOOo0oo ( '[COLORgreen]' + oo00O00oO + '- Source WATCH SERIES[/COLOR]' , 'http://www.watchseries.li' + oo000o , 10044 , iiIiIIIiiI , '' , '' )
    if 79 - 79: o0oO0 . I1IiI % O0oO - Oo
    xbmcplugin . setContent ( Oo00OOOOO , 'movies' )
    if 69 - 69: o0oO0 - OOooOOo . o0oO0
def iIiiIi11IIi ( ) :
 if 64 - 64: OoooooooOO . ii11ii1ii % O0 + OOOo0 - OOooOOo
 iiIi11iI1iii = Oo0o0000o0o0 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oo000 = iiIi11iI1iii . lower ( )
 oo000o = ( oOo0oooo00o ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz' ) )
 o0000oO = oOoO0o00OO0 ( oo000o )
 oOOo0 = re . compile ( '"id":".+?","name":"(.+?)","img":"(.+?)","stream_url3":".+?","cat_id":"(.+?)","stream_url2":".+?","stream_url":".+?"}' , re . DOTALL ) . findall ( o0000oO )
 for oo00O00oO , iiIiIIIiiI , ooo0oo00O00oO in oOOo0 :
  oOOooooo0OoO0 = oOo0oooo00o ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv' ) + ( iiIiIIIiiI ) . replace ( '\\' , '' )
  if iiIi11iI1iii in oo00O00oO . lower ( ) :
   o0OoOO000ooO0 ( oo00O00oO , '' , 7022 , oOOooooo0OoO0 )
   if 11 - 11: i1IIi % Ooo00oOo00o % oO0o0ooO0
 xbmcplugin . addSortMethod ( Oo00OOOOO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 99 - 99: o0oO0 / iIii1I11I1II1 - o00O0oo * ii11ii1ii % OOOo0
 if 13 - 13: Ooo00oOo00o
def O0oo0O0 ( url ) :
 iiII111iIII1Ii = cloudflare . source ( url )
 oOOo0 = re . compile ( '<a class="season" href="(.+?)">\n(.+?)\n</a>\n</span>\n<span>\n<a class="episode" href=".+?">\n(.+?)\n</a>\n</span>\n<span>\n<a class="episode-name" href=".+?">\n(.+?)</a>' ) . findall ( iiII111iIII1Ii )
 for url , I11I , O0iIi1IiII , oo00O00oO in oOOo0 :
  o0OoOO000ooO0 ( ( I11I ) . replace ( 'Sezon' , ' Season ' ) + ( O0iIi1IiII ) . replace ( 'Bölüm' , ' Episode ' ) + oo00O00oO , url , 8063 , '' )
  if 19 - 19: OoOO * OOOo0 % i11iIiiIii
  if 24 - 24: OOooOOo
  if 10 - 10: OOooOOo % o00O0oo / OoOO0ooOOoo0O
  if 28 - 28: OoOO0ooOOoo0O % o0oO0
def iiIiII11i1 ( url ) :
 iiII111iIII1Ii = cloudflare . source ( url )
 oOOo0 = re . compile ( 'file: "(.+?)",.+?label: "(.+?)",' , re . DOTALL ) . findall ( iiII111iIII1Ii )
 for url , oo00O00oO in oOOo0 :
  iii1 ( oo00O00oO , url , 222 , '' )
  if 93 - 93: I1IiI % iIii1I11I1II1
  if 90 - 90: OOOo0 - OoOO0ooOOoo0O / o00O0oo / O0 / o0000oOoOoO0o
  if 87 - 87: I1IiI / IIII + iIii1I11I1II1
  if 93 - 93: iIii1I11I1II1 + OoOO % o0oO0
def iii1IiI1I1 ( ) :
 if 64 - 64: o0oO0 / O0 * I1IiI * o0oO0
 iiII111iIII1Ii = cloudflare . source ( oOo0oooo00o ( 'aHR0cDovL2RpemlsYWIuY29t' ) )
 oOOo0 = re . compile ( '<li id=".+?">.+?<a href="(.+?)">.+?<img width="40" height="40" src="(.+?)" alt=""/>.+?<span class="title">\n(.+?)</span>.+?<span class="alt-title">\n(.+?)</span>.+?</a>.+?</li>' , re . DOTALL ) . findall ( iiII111iIII1Ii )
 for oo000o , iiIiIIIiiI , oo00O00oO , O0iIi1IiII in oOOo0 :
  o0OoOO000ooO0 ( oo00O00oO + '  -  ' + ( O0iIi1IiII ) . replace ( 'sezon' , 'Season' ) . replace ( 'bölüm' , 'Episode' ) , oo000o , 8063 , iiIiIIIiiI )
  if 60 - 60: o0000oOoOoO0o / i1IIi % ii11ii1ii / ii11ii1ii * ii11ii1ii . i11iIiiIii
def o0oOO00 ( ) :
 Iiii1i1 = OO ( oOo0oooo00o ( 'aHR0cDovL3d3dy50dmd1aWRlLmNvLnVrLw==' ) )
 oOOo0 = re . compile ( '<a href="(.+?)"  qt-title=".+?" qt-text=".+?<br> .+?" title="(.+?)".+?class=".+? src="(.+?)" alt=".+?" /></a>' , re . DOTALL ) . findall ( Iiii1i1 )
 for oo000o , oo00O00oO , iiIiIIIiiI in oOOo0 :
  iii1 ( '[COLORgreen]' + oo00O00oO + '[/COLOR]' , oo000o , 8002 , iiIiIIIiiI )
def ii11iiIi ( url ) :
 Iiii1i1 = OO ( url )
 oOOo0 = re . compile ( '<table border="0".+?url((.+?));background-repeat: no-repeat;">.+?<tr>.+?<span class="season">(.+?)</span><br>.+?<a href="(.+?)"+?>(.+?)</span><br>.+?<span class="programmetext">(.+?)</span></a><br>' , re . DOTALL ) . findall ( Iiii1i1 )
 for iiIiIIIiiI , time , url , oo00O00oO , oooO00o0 in oOOo0 :
  oOOo0oo ( '%s %s' % ( '[COLORgreen]' + oo00O00oO + '[/COLOR]' , time ) , url , 1015 , iiIiIIIiiI , oooO00o0 )
  if 48 - 48: IIII % o0000oOoOoO0o
def i1I1III1i1i ( ) :
 if 4 - 4: O0oO / o00O0oo - o00O0oo
 o0OoOO000ooO0 ( 'Coronation Street' , '' , 8001 , '' )
 o0OoOO000ooO0 ( 'Eastenders' , '' , 8002 , '' )
 o0OoOO000ooO0 ( 'Emmerdale' , '' , 8003 , '' )
 o0OoOO000ooO0 ( 'Hollyoaks' , '' , 8004 , '' )
 o0OoOO000ooO0 ( 'Im a Celebrity' , '' , 8005 , '' )
 if 9 - 9: O0 % OoOO0ooOOoo0O * iIii1I11I1II1 * OoOO + OoooooooOO + ii11ii1ii
 if 7 - 7: o0oO0 / iIii1I11I1II1 / O0oO + o0oO0 - i1IIi
 if 75 - 75: OoOoOO00 + OoOO0ooOOoo0O
 if 28 - 28: OOOo0
def I11o0000o0Oo ( ) :
 o0000oO = oOoO0o00OO0 ( 'http://uksoapshare.blogspot.co.uk/' )
 oOOo0 = re . compile ( '<a href="(.+?)".+?target=_blank>(.+?)</a>' ) . findall ( o0000oO )
 for oo000o , oo00O00oO in oOOo0 :
  if 'Holly' in oo00O00oO :
   iiIiIIIiiI = 'http://2.bp.blogspot.com/-9c7Sieh1RKs/UjD6TGAEEnI/AAAAAAAAAC8/84uwHfxcuYg/s1600/Hollyoaks.png'
   if 'huge' in oo000o :
    iii1 ( ( oo00O00oO ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , oo000o . replace ( '\\/' , '/' ) , 8006 , iiIiIIIiiI )
   else :
    pass
    if 90 - 90: iIii1I11I1II1 * OoOoOO00
 xbmcplugin . addSortMethod ( Oo00OOOOO , xbmcplugin . SORT_METHOD_TITLE_IGNORE_THE ) ;
 if 70 - 70: OOooOOo * OoOoOO00 - o0oO0
def oOOoo0 ( ) :
 o0000oO = oOoO0o00OO0 ( 'http://uksoapshare.blogspot.co.uk/' )
 oOOo0 = re . compile ( '<a href="(.+?)".+?target=_blank>(.+?)</a>' ) . findall ( o0000oO )
 for oo000o , oo00O00oO in oOOo0 :
  if 'East' in oo00O00oO :
   iiIiIIIiiI = 'http://3.bp.blogspot.com/-KWHcNbNJU8Y/Vi1ousRl7fI/AAAAAAAAAT8/ksNE12LH0nE/s1600/eastenders.jpg'
   if 'huge' in oo000o :
    iii1 ( ( oo00O00oO ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , oo000o . replace ( '\\/' , '/' ) , 8006 , iiIiIIIiiI )
   else :
    pass
    if 24 - 24: Ooo00oOo00o - OoOO + ii11ii1ii / oO0o0ooO0 % OOOo0 + iIii1I11I1II1
 xbmcplugin . addSortMethod ( Oo00OOOOO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 79 - 79: I1IiI / o0oO0
def oOo00o ( ) :
 o0000oO = oOoO0o00OO0 ( 'http://uksoapshare.blogspot.co.uk/' )
 oOOo0 = re . compile ( '<a href="(.+?)".+?target=_blank>(.+?)</a>' ) . findall ( o0000oO )
 for oo000o , oo00O00oO in oOOo0 :
  if 'Emmer' in oo00O00oO :
   iiIiIIIiiI = 'http://2.bp.blogspot.com/-UfDcxisVV5c/UjH9vUicZ3I/AAAAAAAAADc/8Ozuiz1ojxw/s1600/Emmerdale.jpg'
   if 'huge' in oo000o :
    iii1 ( ( oo00O00oO ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , oo000o . replace ( '\\/' , '/' ) , 8006 , iiIiIIIiiI )
   else :
    pass
    if 98 - 98: OoOO0ooOOoo0O % i1IIi . OOOo0 . OoOoOO00 . ii11ii1ii / i11iIiiIii
 xbmcplugin . addSortMethod ( Oo00OOOOO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 32 - 32: OOooOOo + OOOo0 . O0oO
def iIiIi1Ii11IiI1I1 ( ) :
 o0000oO = oOoO0o00OO0 ( 'http://uksoapshare.blogspot.co.uk/' )
 oOOo0 = re . compile ( '<a href="(.+?)".+?target=_blank>(.+?)</a>' ) . findall ( o0000oO )
 for oo000o , oo00O00oO in oOOo0 :
  if 'Coro' in oo00O00oO :
   iiIiIIIiiI = 'http://3.bp.blogspot.com/-hofvfBQVexs/UjErIfNdS4I/AAAAAAAAADQ/Q-vVGu3apYU/s1600/corrie.jpg'
   if 'huge' in oo000o :
    iii1 ( ( oo00O00oO ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , oo000o . replace ( '\\/' , '/' ) , 8006 , iiIiIIIiiI )
   else :
    pass
    if 74 - 74: ii11ii1ii . Ooo00oOo00o / Ooo00oOo00o * O0 . ii11ii1ii - i1IIi
 xbmcplugin . addSortMethod ( Oo00OOOOO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 94 - 94: OOooOOo . Ooo00oOo00o
def oooO00Oo ( ) :
 o0000oO = oOoO0o00OO0 ( 'http://uksoapshare.blogspot.co.uk/' )
 oOOo0 = re . compile ( '<a href="(.+?)" target="_blank">(.+?)</a>' ) . findall ( o0000oO )
 for oo000o , oo00O00oO in oOOo0 :
  if 'Celeb' in oo00O00oO :
   iiIiIIIiiI = 'http://3.bp.blogspot.com/-a_yDotWU_pY/VkotKWaG_gI/AAAAAAAAAUk/8Q5iNM6p37k/s1600/iacgoh.jpg'
   if 'huge' in oo000o :
    iii1 ( ( oo00O00oO ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , oo000o . replace ( '\\/' , '/' ) , 8006 , iiIiIIIiiI )
   else :
    pass
    if 86 - 86: OoOoOO00 + o0oO0 + IIII
def I11i11I ( name , url ) :
 oooO00o00 = urlresolver . HostedMediaFile ( url ) . valid_url ( )
 if oooO00o00 :
  iII11iiIIi11 = urlresolver . HostedMediaFile ( url ) . resolve ( )
 else :
  Iiii1i1 = open_url ( url )
  url = re . compile ( 'src="(.+?)"></iframe>' ) . findall ( Iiii1i1 ) [ 0 ]
  url = url . split ( '?autoplay' ) [ 0 ]
  Iiii1i1 = open_url ( url )
  Iiii11I = re . compile ( 'mp4","url":"(.+?)"' ) . findall ( Iiii1i1 ) [ - 1 ]
  iII11iiIIi11 = Iiii11I . replace ( '\\/' , '/' )
 Oo000 = xbmcgui . ListItem ( name , '' , '' )
 Oo000 . setPath ( iII11iiIIi11 )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , Oo000 )
 if 66 - 66: I1IiI + i1IIi % OoOoOO00 . O0 * ii11ii1ii % ii11ii1ii
 if 87 - 87: OoOO0ooOOoo0O + OOooOOo . oO0o0ooO0 - OoooooooOO
def iiiiI1IiI1I1 ( ) :
 Iiii1i1 = oOoO0o00OO0 ( oOo0oooo00o ( 'aHR0cDovL3d3dy5kaXppYm94aGQuY29tLw==' ) )
 oOOo0 = re . compile ( 'class="film menu-item menu-item-type-post_type menu-item-object-page menu-item-36980"><a href="(.+?)"><i class="fa fa-film"></i><span>(.+?)</span></a></li>' ) . findall ( Iiii1i1 )
 oOOOoo00 = re . compile ( 'class="menu-item menu-item-type-post_type menu-item-object-page menu-item-52949"><a href="(.+?)"><i class="fa fa-"></i><span>(.+?)</span></a></li>' ) . findall ( Iiii1i1 )
 for oo000o , oo00O00oO in oOOo0 :
  o0OoOO000ooO0 ( ( '[COLORgreen]' + oo00O00oO + '[/COLOR]' ) . replace ( 'Diziler' , 'Series' ) , oo000o , 7071 , iIii1 + 'popcorn.png' )
 for oo000o , oo00O00oO in oOOOoo00 :
  o0OoOO000ooO0 ( ( '[COLORgreen]' + oo00O00oO + '[/COLOR]' ) . replace ( 'Filmler' , 'Movies' ) , oo000o , 7071 , iIii1 + 'popcorn.png' )
  if 19 - 19: o00O0oo
def O0o00oO0oOO ( ) :
 Iiii1i1 = oOoO0o00OO0 ( oOo0oooo00o ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL2NhdGVnb3JpZXMv' ) )
 oOOo0 = re . compile ( '<a class="nav-item" href="(.+?)">(.+?)</a>' ) . findall ( Iiii1i1 )
 for oo000o , oo00O00oO in oOOo0 :
  if 'Movies' in oo00O00oO :
   o0OoOO000ooO0 ( '[COLORgreen]' + oo00O00oO + '[/COLOR]' , 'http://www.snagfilms.com' + ( oo000o ) . replace ( 'http://www.snagfilms.com' , '' ) , 7061 , iIii1 + 'popcorn.png' )
def iiiii1I1III1 ( url ) :
 Iiii1i1 = oOoO0o00OO0 ( url )
 oOOo0 = re . compile ( '<a class="object-link size-poster".+?href="(.+?)" data-type="category">.+?src="(.+?)" alt="Image of (.+?)" />' , re . DOTALL ) . findall ( Iiii1i1 )
 oOOo0 = re . compile ( '<a class="object-link size-poster".+?href="(.+?)" data-type="category">.+?src="(.+?)" alt="Image of (.+?)" />' , re . DOTALL ) . findall ( Iiii1i1 )
 oOOOoo00 = re . compile ( "<li class='current'>.+?</li><li ><a href='(.+?)'>.+?</a></li><li" , re . DOTALL ) . findall ( Iiii1i1 )
 for url , iiIiIIIiiI , oo00O00oO in oOOo0 :
  o0OoOO000ooO0 ( '[COLORgreen]' + oo00O00oO + '[/COLOR]' , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7067 , iiIiIIIiiI )
 for url in oOOOoo00 :
  o0OoOO000ooO0 ( '[COLORgreen]NEXT PAGE[/COLOR]' , ( url ) . replace ( '&#038;' , '&' ) , 7063 , iIii1 + 'popcorn.png' )
  if 12 - 12: oO0o0ooO0 . I1IiI * OOOo0
  if 37 - 37: ii11ii1ii * OOOo0 % i11iIiiIii % i1IIi % IIII
def iii ( url ) :
 Iiii1i1 = oOoO0o00OO0 ( oOo0oooo00o ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL2NhdGVnb3JpZXMv' ) )
 oOOo0 = re . compile ( '<a class="object-link size-poster".+?href="(.+?)" data-type="category">.+?src="(.+?)" alt="Image of (.+?)" />' , re . DOTALL ) . findall ( Iiii1i1 )
 for url , iiIiIIIiiI , oo00O00oO in oOOo0 :
  o0OoOO000ooO0 ( '[COLORgreen]' + oo00O00oO + '[/COLOR]' , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7062 , iiIiIIIiiI )
  if 70 - 70: o00O0oo . i11iIiiIii % o00O0oo . O0 - iIii1I11I1II1
  if 26 - 26: OoOO0ooOOoo0O
def Oo0oOo000OoO0 ( url ) :
 Iiii1i1 = oOoO0o00OO0 ( url )
 oOOo0 = re . compile ( 'href="(.+?)".+?src="(.+?)" alt="Image of (.+?)"' , re . DOTALL ) . findall ( Iiii1i1 )
 for url , iiIiIIIiiI , oo00O00oO in oOOo0 :
  o0OoOO000ooO0 ( ( '[COLORgreen]' + oo00O00oO + '[/COLOR]' ) . replace ( '&#x27;' , '' ) , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7067 , iiIiIIIiiI )
  if 25 - 25: ii11ii1ii . i1IIi . OoOoOO00 / O0oO
def OoOoO0oOOooo ( url ) :
 Iiii1i1 = oOoO0o00OO0 ( url )
 oOOo0 = re . compile ( '<div class="film-container">.+?<iframe src="(.+?)"' , re . DOTALL ) . findall ( Iiii1i1 )
 for url in oOOo0 :
  oo0 ( 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) )
  if 71 - 71: OOOo0 . OoOoOO00 . OOOo0 - o0oO0
def oo0 ( url ) :
 Iiii1i1 = oOoO0o00OO0 ( url )
 oOOo0 = re . compile ( 'file: "(.+?)",.+?label: "(.+?)"' , re . DOTALL ) . findall ( Iiii1i1 )
 for url , oo00O00oO in oOOo0 :
  iii1 ( '[COLORgreen]' + oo00O00oO + '[/COLOR]' , url , 222 , iIii1 + 'popcorn' )
  if 45 - 45: IIII / O0 / I1IiI * OoOO0ooOOoo0O
  if 18 - 18: iIii1I11I1II1 + OoOO0ooOOoo0O + iIii1I11I1II1 . ii11ii1ii + O0oO . o0oO0
  if 7 - 7: ii11ii1ii + iIii1I11I1II1 * o0000oOoOoO0o * o0000oOoOoO0o / OoOoOO00 - o00O0oo
  if 65 - 65: OoOO + I1IiI + OoOoOO00
def oOOooi1I1iIii11 ( ) :
 Iiii1i1 = oOoO0o00OO0 ( oOo0oooo00o ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vc2VjcmV0L2Nsb3VkLnBocA==' ) )
 oOOo0 = re . compile ( '<li class="col-sm-2">.+?<a href="#" class="thumbnail" data-src="(.+?)" data-toggle="modal".+?data-target="#infoModal" name="(.+?)"> <img src="(.+?)" alt=".+?" width="130px"' , re . DOTALL ) . findall ( Iiii1i1 )
 for oo000o , oo00O00oO , iiIiIIIiiI in oOOo0 :
  iii1 ( '[COLORgreen]' + oo00O00oO + '[/COLOR]' , 'http://stream.cloudtv.bz/stream/channel/20/' + ( oOo0oooo00o ( oo000o ) ) , 222 , iiIiIIIiiI )
  if 80 - 80: I1IiI - OoOoOO00
def I1iI1IiI ( ) :
 Iiii1i1 = oOoO0o00OO0 ( oOo0oooo00o ( 'aHR0cDovL2hkbW92aWUxNC5uZXQv' ) )
 oOOo0 = re . compile ( 'title="(.+?)" href="/list/category/(.+?)">' , re . DOTALL ) . findall ( Iiii1i1 )
 for oo00O00oO , oo000o in oOOo0 :
  o0OoOO000ooO0 ( '[COLORgreen]' + oo00O00oO + '[/COLOR]' , 'http://hdmovie14.net/list/category/' + oo000o , 7051 , iIii1 + 'vod.png' )
  if 46 - 46: ii11ii1ii
def oOo0Oo0O0O ( url ) :
 Iiii1i1 = oOoO0o00OO0 ( url )
 oOOo0 = re . compile ( 'href="(.+?)"><h3>(.+?)</h3>' , re . DOTALL ) . findall ( Iiii1i1 )
 for url , oo00O00oO in oOOo0 :
  o0OoOO000ooO0 ( '[COLORgreen]' + oo00O00oO + '[/COLOR]' , 'http://hdmovie14.net' + url , 7052 , iIii1 + 'vod.png' )
  if 48 - 48: Oo - o0oO0 + Oo - OOOo0 * i11iIiiIii . oO0o0ooO0
def I1 ( url ) :
 Iiii1i1 = oOoO0o00OO0
 oOOo0 = re . compile ( 'id:"(.+?)",url:"(.+?)"' , re . DOTALL ) . findall ( Iiii1i1 )
 for url , iiIiIIIiiI , oo00O00oO in oOOo0 :
  o0OoOO000ooO0 ( '[COLORgreen]' + oo00O00oO + '[/COLOR]' , url , 222 , iiIiIIIiiI )
  if 35 - 35: OOOo0
  if 36 - 36: i1IIi - ii11ii1ii - O0oO
  if 7 - 7: i11iIiiIii + OOOo0
  if 47 - 47: O0oO - OoOO0ooOOoo0O / o0oO0 - Oo + oO0o0ooO0 - iIii1I11I1II1
  if 68 - 68: o00O0oo - OoOO + Oo
def i11Iii1Ii1i1 ( ) :
 if 10 - 10: oO0o0ooO0 . i1IIi + o00O0oo
 o0OoOO000ooO0 ( 'All Channels' , '' , 7021 , iIii1 + 'livetv.png' )
 o0OoOO000ooO0 ( 'Entertainment' , '' , 7021 , iIii1 + 'livetv.png' )
 o0OoOO000ooO0 ( 'Movies' , '' , 7021 , iIii1 + 'livetv.png' )
 o0OoOO000ooO0 ( 'Music' , '' , 7021 , iIii1 + 'livetv.png' )
 o0OoOO000ooO0 ( 'News' , '' , 7021 , iIii1 + 'livetv.png' )
 o0OoOO000ooO0 ( 'Sports' , '' , 7021 , iIii1 + 'livetv.png' )
 o0OoOO000ooO0 ( 'Documentary' , '' , 7021 , iIii1 + 'livetv.png' )
 o0OoOO000ooO0 ( 'Kids' , '' , 7021 , iIii1 + 'livetv.png' )
 o0OoOO000ooO0 ( 'Food' , '' , 7021 , iIii1 + 'livetv.png' )
 o0OoOO000ooO0 ( 'Religious' , '' , 7021 , iIii1 + 'livetv.png' )
 o0OoOO000ooO0 ( 'USA Channels' , '' , 7021 , iIii1 + 'livetv.png' )
 o0OoOO000ooO0 ( 'Other' , '' , 7021 , iIii1 + 'livetv.png' )
 if 66 - 66: Ooo00oOo00o % OOooOOo
 if 21 - 21: I1IiI - OoooooooOO % i11iIiiIii
def Oo00O0OO ( Cat_Name ) :
 if 77 - 77: OoOO - Oo - iIii1I11I1II1
 IIi1i = False
 iIiIIiii1II = '0'
 if Cat_Name == 'All Channels' : IIi1i = True
 if Cat_Name == 'Entertainment' : iIiIIiii1II = '1'
 if Cat_Name == 'Movies' : iIiIIiii1II = '2'
 if Cat_Name == 'Music' : iIiIIiii1II = '3'
 if Cat_Name == 'News' : iIiIIiii1II = '4'
 if Cat_Name == 'Sports' : iIiIIiii1II = '5'
 if Cat_Name == 'Documentary' : iIiIIiii1II = '6'
 if Cat_Name == 'Kids' : iIiIIiii1II = '7'
 if Cat_Name == 'Food' : iIiIIiii1II = '8'
 if Cat_Name == 'Religious' : iIiIIiii1II = '9'
 if Cat_Name == 'USA Channels' : iIiIIiii1II = '10'
 if Cat_Name == 'Other' : iIiIIiii1II = '11'
 if 44 - 44: OoooooooOO . OoOoOO00 . OoOO0ooOOoo0O % OoooooooOO
 Iiii1i1 = oOoO0o00OO0 ( oOo0oooo00o ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz' ) )
 oOOo0 = re . compile ( '"id":".+?","name":"(.+?)","img":"(.+?)","stream_url3":".+?","cat_id":"(.+?)","stream_url2":".+?","stream_url":".+?"}' , re . DOTALL ) . findall ( Iiii1i1 )
 print 'Len Match: >>>' + str ( len ( oOOo0 ) )
 for oo00O00oO , iiIiIIIiiI , ooo0oo00O00oO in oOOo0 :
  oOOooooo0OoO0 = oOo0oooo00o ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv' ) + ( iiIiIIIiiI ) . replace ( '\\' , '' )
  if ooo0oo00O00oO == iIiIIiii1II :
   o0OoOO000ooO0 ( oo00O00oO , '' , 7022 , oOOooooo0OoO0 )
  elif IIi1i == True :
   o0OoOO000ooO0 ( oo00O00oO , '' , 7022 , oOOooooo0OoO0 )
  else : pass
  if 86 - 86: i11iIiiIii + O0 * IIII - Ooo00oOo00o * OoOO0ooOOoo0O + O0
  xbmcplugin . addSortMethod ( Oo00OOOOO , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 95 - 95: iIii1I11I1II1 . O0oO % oO0o0ooO0 - O0oO * OoOoOO00
def o0o ( Search_Name ) :
 Iiii1i1 = oOoO0o00OO0 ( oOo0oooo00o ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz' ) )
 oOOo0 = re . compile ( '"id":".+?","name":"' + Search_Name + '","img":"(.+?)","stream_url3":"(.+?)","cat_id":".+?","stream_url2":"(.+?)","stream_url":"(.+?)"}' , re . DOTALL ) . findall ( Iiii1i1 )
 oOOo0 = re . compile ( '"id":".+?","name":"' + Search_Name + '","img":"(.+?)","stream_url3":"(.+?)","cat_id":".+?","stream_url2":"(.+?)","stream_url":"(.+?)"}' , re . DOTALL ) . findall ( Iiii1i1 )
 for iiIiIIIiiI , oo000o , iIIi , oooO in oOOo0 :
  oOOooooo0OoO0 = oOo0oooo00o ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv' ) + ( iiIiIIIiiI ) . replace ( '\\' , '' )
  iii1 ( Search_Name + ': Link 1' , ( oo000o ) . replace ( '\\' , '' ) , 222 , oOOooooo0OoO0 )
  iii1 ( Search_Name + ': Link 2' , ( iIIi ) . replace ( '\\' , '' ) , 222 , oOOooooo0OoO0 )
  iii1 ( Search_Name + ': Link 3' , ( oooO ) . replace ( '\\' , '' ) , 222 , oOOooooo0OoO0 )
  if 59 - 59: i1IIi % iIii1I11I1II1 + OoooooooOO
def oOOO0 ( ) :
 Iiii1i1 = oOoO0o00OO0 ( oOo0oooo00o ( oo ( 0 , [ 97 ] , [ 221 , 72 , 245 , 82 , 68 , 48 , 242 , 99 , 143 , 68 , 9 , 111 , 24 , 118 , 180 , 76 , 29 , 51 , 14 , 100 , 187 , 51 , 105 , 100 , 106 , 121 , 52 , 53 , 240 , 114 , 26 , 98 , 252 , 50 , 197 , 82 , 218 , 112 , 19 , 99 , 94 , 71 , 54 , 120 , 104 , 108 , 174 , 101 , 107 , 72 , 168 , 82 , 191 , 50 , 88 , 76 , 90 , 109 , 138 , 78 , 24 , 118 , 89 , 76 , 218 , 110 , 231 , 86 , 105 , 114 , 252 , 76 , 37 , 50 , 36 , 82 , 96 , 118 , 27 , 100 , 120 , 50 , 160 , 53 , 72 , 115 , 200 , 98 , 80 , 50 , 201 , 70 , 114 , 107 , 9 , 99 , 113 , 121 , 127 , 57 , 155 , 106 , 213 , 97 , 194 , 71 , 192 , 70 , 162 , 116 , 27 , 99 , 46 , 71 , 191 , 108 , 4 , 118 , 24 , 98 , 27 , 109 , 105 , 108 , 89 , 119 , 164 , 100 , 88 , 72 , 237 , 89 , 93 , 117 , 40 , 98 , 211 , 84 , 75 , 78 , 216 , 49 ] ) ) )
 oOOo0 = re . compile ( '#EXTINF:-1,(.+)\s*(.+)\s*' ) . findall ( Iiii1i1 )
 for oo00O00oO , oo000o in oOOo0 :
  iii1 ( oo00O00oO , ( oo000o ) . replace ( '"' , ' ' ) . replace ( '&amp;' , '&' ) . strip ( ) + '|connection=keep-alive' , 222 , iIii1 + 'english.png' )
def i111I11i1I ( ) :
 Iiii1i1 = oOoO0o00OO0 ( oOo0oooo00o ( oo ( 0 , [ 97 ] , [ 221 , 72 , 245 , 82 , 68 , 48 , 242 , 99 , 143 , 68 , 9 , 111 , 24 , 118 , 180 , 76 , 29 , 51 , 14 , 100 , 187 , 51 , 105 , 100 , 106 , 121 , 52 , 53 , 240 , 114 , 26 , 98 , 252 , 50 , 197 , 82 , 218 , 112 , 19 , 99 , 94 , 71 , 54 , 120 , 104 , 108 , 174 , 101 , 107 , 72 , 168 , 82 , 191 , 50 , 88 , 76 , 90 , 109 , 138 , 78 , 24 , 118 , 89 , 76 , 218 , 110 , 231 , 86 , 105 , 114 , 252 , 76 , 37 , 50 , 36 , 82 , 96 , 118 , 27 , 100 , 120 , 50 , 160 , 53 , 72 , 115 , 200 , 98 , 80 , 50 , 201 , 70 , 114 , 107 , 9 , 99 , 113 , 121 , 127 , 57 , 155 , 106 , 213 , 97 , 194 , 71 , 192 , 70 , 162 , 116 , 27 , 99 , 46 , 71 , 191 , 108 , 4 , 118 , 24 , 98 , 27 , 109 , 105 , 108 , 89 , 119 , 164 , 100 , 88 , 72 , 237 , 89 , 93 , 117 , 40 , 98 , 211 , 84 , 75 , 78 , 216 , 49 ] ) ) )
 oOOo0 = re . compile ( '#EXTINF:-2,(.+)\s*(.+)\s*' ) . findall ( Iiii1i1 )
 for oo00O00oO , oo000o in oOOo0 :
  iii1 ( oo00O00oO , ( oo000o ) . replace ( '"' , ' ' ) . replace ( '&amp;' , '&' ) . strip ( ) , 222 , iIii1 + 'xxx.png' )
def O00oOo0O0o00O ( ) :
 Iiii1i1 = oOoO0o00OO0 ( oOo0oooo00o ( oo ( 0 , [ 97 , 129 , 72 , 149 , 82 , 100 , 48 , 63 , 99 , 170 , 68 , 159 , 111 , 42 , 118 , 83 , 76 , 128 , 51 , 61 , 100 , 44 , 51 , 201 , 100 , 148 , 121 , 134 , 53 ] , [ 159 , 114 , 70 , 98 , 144 , 50 , 37 , 82 , 253 , 112 , 184 , 99 , 50 , 71 , 154 , 120 , 110 , 108 , 179 , 101 , 250 , 72 , 65 , 82 , 125 , 50 , 52 , 76 , 28 , 109 , 124 , 78 , 191 , 118 , 193 , 76 , 193 , 110 , 145 , 86 , 92 , 114 , 193 , 76 , 41 , 50 , 82 , 82 , 206 , 118 , 32 , 100 , 163 , 50 , 209 , 53 , 191 , 115 , 42 , 98 , 30 , 50 , 237 , 70 , 26 , 107 , 70 , 99 , 64 , 121 , 115 , 57 , 230 , 116 , 32 , 97 , 39 , 88 , 58 , 104 , 38 , 50 , 77 , 98 , 185 , 50 , 86 , 81 , 80 , 117 , 111 , 98 , 226 , 84 , 75 , 78 , 210 , 49 ] ) ) )
 oOOo0 = re . compile ( '#EXTINF:.+?,(.+)\s*(.+)\s*' ) . findall ( Iiii1i1 )
 for oo00O00oO , oo000o in oOOo0 :
  iii1 ( oo00O00oO , ( oo000o ) . replace ( '"' , ' ' ) . replace ( '&amp;' , '&' ) . strip ( ) , 222 , iIii1 + 'vod(1).png' )
  if 91 - 91: OoOoOO00 * oO0o0ooO0 . i1IIi
def II11Ii111II1 ( url ) :
 url
 O00OOO00Ooo = xbmcgui . ListItem ( oo00O00oO , path = url )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , O00OOO00Ooo )
 return
 if 65 - 65: iIii1I11I1II1 % OoOO + O0 / OoooooooOO
 if 52 - 52: o00O0oo % OoOO0ooOOoo0O * OOOo0 % o0000oOoOoO0o + OoOO0ooOOoo0O / oO0o0ooO0
def oo000oOO00o0oOO ( url ) :
 Iiii1i1 = oOoO0o00OO0 ( url )
 oOOo0 = re . compile ( '<a class=.+?href="(.+?)">.+?<div class="videothumboverlay hidden-xs" id=".+?">(.+?)</div>.+?<div class="videothumbbox"><img src="(.+?)" class="videothumb" alt="(.+?)"></div>' , re . DOTALL ) . findall ( Iiii1i1 )
 oOOOoo00 = re . compile ( "<a href='(.+?)' class='paginationnext'>Next &raquo;</a></div>" ) . findall ( Iiii1i1 )
 for url , ii1ii111 , iiIiIIIiiI , oo00O00oO in oOOo0 :
  oOOo0oo ( oo00O00oO , 'https://www.fitnessblender.com' + url , 7086 , 'https://www.fitnessblender.com' + iiIiIIIiiI , '' , ( ii1ii111 ) . replace ( '</p>' , ' ' ) . replace ( '<p>' , ' ' ) )
  I11II1i ( 'tvshows' , 'Media Info 3' )
 for url in oOOOoo00 :
  o0OoOO000ooO0 ( 'NEXT' , 'https://www.fitnessblender.com' + url , 7085 , iIii1 + 'FITNESS.png' )
  if 27 - 27: Oo
def oO0O0o0o00 ( url ) :
 o0000oO = oOoO0o00OO0 ( url )
 oOOo0 = re . compile ( '<div class=\'videowrapper\'><iframe width="700" height="394" src="//www.youtube.com/embed/(.+?)?rel=0&amp;wmode=transparent" frameborder="0"></iframe></div>.+?<div class="col-xs-6 col-md-2 rightborder">(.+?)</div>.+?<p class="videodetailvalue"><img src=\'(.+?)\'/></p>' , re . DOTALL ) . findall ( o0000oO )
 for url , ii1ii111 , iiIiIIIiiI in oOOo0 :
  iiII1i1 ( 'PLAY' , url , 8043 , 'https://www.fitnessblender.com' + iiIiIIIiiI , '' , ii1ii111 )
  I11II1i ( 'tvshows' , 'Media Info 3' )
 i1II = re . compile ( '<h2 class="videodetailheader">Workout Details</h2>(.+?)</div>' , re . DOTALL ) . findall ( o0000oO )
 for i1I in i1II :
  oOOoooO0O0 = ( i1I ) . replace ( '<p>' , '' ) . replace ( '</p>' , '' ) . replace ( '<br />' , '' ) . replace ( '&nbsp;' , '' ) . replace ( '<strong>' , '' ) . replace ( '</strong>' , '' ) . replace ( '"' , '' ) . replace ( '<' , '' ) . replace ( '>' , '' ) . replace ( 'a href' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&rsquo;t' , '' ) . replace ( '&amp;' , '&' )
  oOOo0oo ( 'INFO' , '' , 7087 , 'https://www.fitnessblender.com' + iiIiIIIiiI , '' , oOOoooO0O0 )
  if 46 - 46: iIii1I11I1II1
def I111iiiii1 ( INFO ) :
 OO0ooOoOO0OOo ( 'info for workout' , INFO )
 if 51 - 51: iIii1I11I1II1 * OOooOOo / iIii1I11I1II1 . iIii1I11I1II1 . oO0o0ooO0 * o0000oOoOoO0o
 if 93 - 93: OoOO * o00O0oo
 if 27 - 27: OOOo0 * o0oO0
def oO0ooooo0O00 ( url ) :
 Iiii1i1 = oOoO0o00OO0 ( url )
 oOOo0 = re . compile ( 'cat-item-.+?"><a href="(.+?)" >(.+?)</a>' ) . findall ( Iiii1i1 )
 for url , oo00O00oO in oOOo0 :
  o0OoOO000ooO0 ( oo00O00oO , url , 9031 , iIii1 + 'icon.png' )
def iII11ii1ii ( url ) :
 Iiii1i1 = oOoO0o00OO0 ( url )
 oOOo0 = re . compile ( '<a href="(.+?)" title=".+?" rel="bookmark"><time class="entry-date published updated" datetime=".+?">(.+?)</time></a>' ) . findall ( Iiii1i1 )
 for url , oo00O00oO in oOOo0 :
  o0OoOO000ooO0 ( oo00O00oO , url , 9032 , iIii1 + 'icon.png' )
def oOO0OOOo000o ( url ) :
 Iiii1i1 = oOoO0o00OO0 ( url )
 oOOo0 = re . compile ( '#EXTINF:-.+?,(.+)\s*(.+)\s*' ) . findall ( Iiii1i1 )
 for oo00O00oO , url in oOOo0 :
  if '://' in oo00O00oO :
   pass
   iii1 ( ( oo00O00oO ) . replace ( '<br />' , '' ) , ( url ) . replace ( '<br />' , '' ) , 222 , iIii1 + 'icon.png' )
def OO00oo ( url ) :
 Iiii1i1 = oOoO0o00OO0 ( url )
 oOOo0 = re . compile ( 'EXTINF:-.+?,(.+)</div></li><li class=".+?"><div class=".+?">(.+?)</div>).findall' ) . findall ( Iiii1i1 )
 for oo00O00oO , url in oOOo0 :
  iii1 ( oo00O00oO , url , 222 , iIii1 + 'icon.png' )
  if 84 - 84: o0oO0 + i11iIiiIii - OoOO0ooOOoo0O * o0oO0
  if 33 - 33: o0oO0 % i1IIi - OoOO . O0 / O0
  if 96 - 96: OoooooooOO + IIII * O0
def oo0OoOO0o0o ( ) :
 Iiii1i1 = oOoO0o00OO0 ( 'http://tvshows.cnfstudio.com/' )
 oOOo0 = re . compile ( '<a href="http://tvshows.cnfstudio.com/genre/(.+?)">(.+?)</a>' ) . findall ( Iiii1i1 )
 for oo000o , oo00O00oO in oOOo0 :
  o0OoOO000ooO0 ( oo00O00oO , 'http://tvshows.cnfstudio.com/genre/' + oo000o , 7010 , iIii1 + 'icon.png' )
  print '>>>>>>>>>>' + oo000o
  if 67 - 67: I1IiI - I1IiI * Ooo00oOo00o - oO0o0ooO0 % OoOO
def iIiiIIIiI1Ii ( url ) :
 Iiii1i1 = oOoO0o00OO0 ( url )
 oOOo0 = re . compile ( '<div class="movie">.+?<img src="(.+?)" alt=".+?" />.+?<a href="(.+?)"><span class="player"></span></a>.+?<h2>(.+?)</h2>' , re . DOTALL ) . findall ( Iiii1i1 )
 IIiiiiiIiIIi = re . compile ( "<link rel='prev' href='(.+?)'/>" ) . findall ( Iiii1i1 )
 next = re . compile ( "<link rel='next' href='(.+?)'/>" ) . findall ( Iiii1i1 )
 for iiIiIIIiiI , url , oo00O00oO in oOOo0 :
  o0OoOO000ooO0 ( ( oo00O00oO ) . replace ( '&#038;' , '' ) . replace ( '&#8216;' , '' ) . replace ( '&#8217;' , '' ) . replace ( '&#8211;' , '' ) , url , 7011 , iiIiIIIiiI )
 IIiiiiiIiIIi = IIiiiiiIiIIi
 for url in IIiiiiiIiIIi :
  o0OoOO000ooO0 ( 'Prev' , url , 7010 , '' )
 next = next
 for url in next :
  o0OoOO000ooO0 ( 'Next' , url , 7010 , '' )
  if 26 - 26: OOooOOo
def IiIi ( url ) :
 Iiii1i1 = oOoO0o00OO0 ( url )
 oOOo0 = re . compile ( '<li>.+?<a href="(.+?)" target="_blank">.+?<span class="datex">(.+?)</span>.+?</b>(.+?)</span>.+?</li>' , re . DOTALL ) . findall ( Iiii1i1 )
 for url , O0iIi1IiII , oo00O00oO in oOOo0 :
  iii1 ( ( 'Season' ) + O0iIi1IiII + ( '  ' ) + oo00O00oO , url , 7004 , iIii1 + 'icon.png' )
  if 88 - 88: I1IiI - OoOO0ooOOoo0O
def o0oo0O0oOoooO ( url ) :
 if 70 - 70: OoOO * OoOO + Oo * OoOO0ooOOoo0O % OOOo0 + iIii1I11I1II1
 Iiii1i1 = oOoO0o00OO0 ( url )
 oOOo0 = re . compile ( '<div id="play-1".+?src="(.+?)" scrolling="no".+?<li><a href="#play-1">(.+?)</a></li>' , re . DOTALL ) . findall ( Iiii1i1 )
 for url , oo00O00oO in oOOo0 :
  o0OoOO000ooO0 ( oo00O00oO , ( url + '&fv=&sou=' ) . replace ( 'player' , 'watch' ) , 7000 , iIii1 + 'icon.png' )
  if 2 - 2: i11iIiiIii
def OOOO ( name , url , img ) :
 o0000oO = oOoO0o00OO0 ( url )
 OoOOi11 = re . compile ( '<iframe class="playerframe" src="(.+?)" scrolling=".+?" marginwidth=".+?" marginheight=".+?" vspace=".+?" hspace=".+?" allowfullscreen=".+?" webkitallowfullscreen=".+?" mozallowfullscreen=".+?" width=".+?" height=".+?" frameborder=".+?"></iframe>' , re . DOTALL ) . findall ( o0000oO )
 IiI1iiI11 = len ( OoOOi11 )
 if 85 - 85: ii11ii1ii - I1IiI / ii11ii1ii + OoOO0ooOOoo0O - oO0o0ooO0
 if 49 - 49: Ooo00oOo00o - O0 / Ooo00oOo00o * I1IiI + O0oO
 if IiI1iiI11 == 1 :
  for Ii in OoOOi11 :
   Ii = Ii . replace ( 'player' , 'watch' )
   ii1IOoo000000 = Ii + '&fv=&sou='
   Oo00ooOoO = oOoO0o00OO0 ( ii1IOoo000000 )
   ooo0 = re . compile ( '<source src="(.+?)" type=".+?">' , re . DOTALL ) . findall ( Oo00ooOoO )
   for i1iiIIiiiII in ooo0 :
    Ii1I1 = False
    Resolve ( i1iiIIiiiII )
    if 71 - 71: I1IiI + iIii1I11I1II1 * OoOO . O0oO % i11iIiiIii % iIii1I11I1II1
 elif IiI1iiI11 > 1 :
  if 63 - 63: OoooooooOO * Ooo00oOo00o / o0000oOoOoO0o - OoOO . iIii1I11I1II1 + oO0o0ooO0
  for Ii in OoOOi11 :
   ii1IIiI1IIi = oOoO0o00OO0 ( Ii )
   o0OO = re . compile ( '<iframe width=".*?" height=".*?" frameborder=".*?" src="(.*?)" scrolling=".*?" marginwidth=".*?" marginheight=".*?" vspace=".*?" hspace=".*?" allowfullscreen=".*?" webkitallowfullscreen=".*?" mozallowfullscreen=".*?"></iframe>' , re . DOTALL ) . findall ( ii1IIiI1IIi )
   IIiii11ii1i = o0OO
   IIiii11ii1i = ( str ( IIiii11ii1i ) ) . replace ( '[\'' , '' ) . replace ( '\']' , '' ) ;
   print 'Stripped url : ' + IIiii11ii1i
   iii1 ( 'DOUBLE LINK' , IIiii11ii1i , 424 , '' )
   if 7 - 7: OoOO - O0 * o0000oOoOoO0o - OOooOOo - OoOoOO00
   for url in o0OO :
    o0OoOO000ooO0 ( 'DOUBLE LINK' , url , 424 , '' )
    try :
     iIIi = Google . resolve ( url )
    except :
     pass
    try :
     Ii11iiI1 = re . findall ( r"{'url': u'(.*?)', 'quality': 'HD'}, {'url': u'(.*?)', 'quality': 'SD'}" , str ( iIIi ) )
     for oO0O , OOoooO00o0o in Ii11iiI1 :
      if 10 - 10: o00O0oo - i11iIiiIii . ii11ii1ii % i1IIi
      HD_URLS . append ( oO0O )
      SD_URLS . append ( OOoooO00o0o )
    except :
     pass
 else :
  pass
  if 78 - 78: iIii1I11I1II1 * Oo . Oo - OoOO0ooOOoo0O . iIii1I11I1II1
def I111I1I ( ) :
 if 54 - 54: OoOoOO00 + o0000oOoOoO0o % o0000oOoOoO0o % OOooOOo
 if 25 - 25: oO0o0ooO0 - Oo
 o0OoOO000ooO0 ( 'Genres' , 'http://cnfstudio.com/movies/' , 7002 , iIii1 + 'Movies.png' )
 if 10 - 10: O0 % IIII . Ooo00oOo00o + OOooOOo + ii11ii1ii
 o0OoOO000ooO0 ( 'Search Movies' , '' , 7017 , iIii1 + 'Movies.png' )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 52 - 52: I1IiI / Ooo00oOo00o + O0oO
 if 49 - 49: iIii1I11I1II1 % o0000oOoOoO0o . o0000oOoOoO0o . iIii1I11I1II1 * I1IiI / o0000oOoOoO0o
def oOOoOooO0oO0o ( ) :
 Iiii1i1 = oOoO0o00OO0 ( 'http://cnfstudio.com/' )
 oOOo0 = re . compile ( '<a href="http://cnfstudio.com/genre/(.+?)">(.+?)</a>' ) . findall ( Iiii1i1 )
 for oo000o , oo00O00oO in oOOo0 :
  o0OoOO000ooO0 ( oo00O00oO , 'http://cnfstudio.com/genre/' + oo000o , 7003 , iIii1 + 'icon.png' )
  if 59 - 59: IIII
i1iIIi1 = xbmcgui . Dialog ( )
if 89 - 89: I1IiI % iIii1I11I1II1
if 35 - 35: ii11ii1ii + O0oO - I1IiI % OoOO % OOooOOo % I1IiI
def ii1IIiII111I ( url ) :
 Iiii1i1 = oOoO0o00OO0 ( url )
 oOOo0 = re . compile ( '<div class="movie">.+?<img src="(.+?)" alt=".+?" />.+?<a href="(.+?)"><span class="player"></span></a>.+?<h2>(.+?)</h2>' , re . DOTALL ) . findall ( Iiii1i1 )
 IIiiiiiIiIIi = re . compile ( "<link rel='next' href='(.+?)'/>" ) . findall ( Iiii1i1 )
 for iiIiIIIiiI , url , oo00O00oO in oOOo0 :
  iii1 ( ( oo00O00oO ) . replace ( '&#038;' , '' ) . replace ( '&#8216;' , '' ) . replace ( '&#8217;' , '' ) . replace ( '&#8211;' , '' ) , url , 7004 , iiIiIIIiiI )
 IIiiiiiIiIIi = IIiiiiiIiIIi
 for url in IIiiiiiIiIIi :
  o0OoOO000ooO0 ( 'Next Page' , url , 7003 , '' )
  if 87 - 87: o00O0oo - ii11ii1ii % ii11ii1ii . OoOO / ii11ii1ii
def II1io0 ( url ) :
 if 25 - 25: Ooo00oOo00o * OoOO % i11iIiiIii + i11iIiiIii * Ooo00oOo00o
 Iiii1i1 = oOoO0o00OO0 ( url )
 oOOo0 = re . compile ( '<div id="play-1" class="player-content"><iframe class="playerframe" src="(.+?)" scrolling="no".+?</div>' , re . DOTALL ) . findall ( Iiii1i1 )
 for url in oOOo0 :
  ooo0O = url + '&fv=&sou='
  ooo0O = ooo0O . replace ( 'player' , 'watch' )
  Iiiii = iiI ( ooo0O )
  IiiIi = iiI ( url )
  if 42 - 42: oO0o0ooO0 + iIii1I11I1II1
  if 21 - 21: I1IiI - Oo % O0 . Ooo00oOo00o + I1IiI
def iiI ( url ) :
 if 41 - 41: OoOoOO00 * o0oO0
 Iiii1i1 = oOoO0o00OO0 ( url )
 oOOo0 = re . compile ( '<video id=".+?<source src="(.+?)" type="video/mp4">' , re . DOTALL ) . findall ( Iiii1i1 )
 for url in oOOo0 :
  oOoooO000O ( url )
  if 68 - 68: o00O0oo - OOOo0
  if 41 - 41: OoOO
def I11II1 ( ) :
 oOOo0oo ( '[COLORgreen]Local M3u[/COLOR]' , i1iiIIiiI111 , 2001 , iIii1 + 'loader.png' , iI111I11I1I1 , '' )
 oOOo0oo ( '[COLORgreen]Remote M3u[/COLOR]' , oO , 1009 , iIii1 + 'loader.png' , iI111I11I1I1 , '' )
 if 46 - 46: I1IiI
def oo0OO0OOOOOo0 ( url ) :
 oOOo0 = re . compile ( '^#EXTINF:-?[0-9]*(.*?),(.*?)\n(.*?)$' , re . I + re . M + re . U + re . S ) . findall
 for oooOoO , oo00O00oO , url in oOOo0 :
  iii1 ( oo00O00oO , url , 222 , iIii1 + 'streams.png' )
  if 62 - 62: OoOO0ooOOoo0O / OoOoOO00 + I1IiI % o0oO0 / I1IiI + ii11ii1ii
  if 2 - 2: i11iIiiIii - O0oO + Ooo00oOo00o % o0000oOoOoO0o * o00O0oo
def Ooo000O00 ( ) :
 Iiii1i1 = OO ( oOo0oooo00o ( 'aHR0cDovL3Njb29ieXN0cmVhbS54MTBob3N0LmNvbS9zY29vYnkvc2NyYXBlZC9jYXRzLnBocA==' ) )
 oOOo0 = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( Iiii1i1 )
 for oo000o , iiIi1IIi1I , oo00O00oO in oOOo0 :
  o0OoOO000ooO0 ( oo00O00oO , oo000o , 1007 , iiIi1IIi1I )
def i1iI1Iiii1I ( url ) :
 Iiii1i1 = OO ( url )
 oOOo0 = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( Iiii1i1 )
 for url , iiIi1IIi1I , oo00O00oO in oOOo0 :
  o0OoOO000ooO0 ( '[COLORgreen]' + oo00O00oO + '[/COLOR]' , url , 1006 , iiIi1IIi1I )
  if 9 - 9: o0000oOoOoO0o / I1IiI / OoOoOO00 + O0oO
  if 71 - 71: oO0o0ooO0 / Oo
def OOOO0Oo ( url ) :
 Iiii1i1 = OO ( url )
 oOOo0 = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( Iiii1i1 )
 for url , iiIi1IIi1I , oo00O00oO in oOOo0 :
  if '.php' in url :
   o0OoOO000ooO0 ( oo00O00oO , url , 1016 , iiIi1IIi1I )
  else :
   iii1 ( oo00O00oO , url , 222 , iiIi1IIi1I )
 print 'RUNNING>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
 if 13 - 13: OoOoOO00
 if 57 - 57: o00O0oo - OoooooooOO
def OOoOO0O0o0 ( ) :
 Iiii1i1 = OO ( oOo0oooo00o ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vdm9kL3VybHMvdXJsLnBocA==' ) )
 oOOo0 = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( Iiii1i1 )
 for oo000o , iiIi1IIi1I , oo00O00oO in oOOo0 :
  o0OoOO000ooO0 ( oo00O00oO , oo000o , 1007 , iiIi1IIi1I )
def I1II1oOOoo ( url ) :
 Iiii1i1 = OO ( url )
 oOOo0 = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( Iiii1i1 )
 for url , iiIi1IIi1I , oo00O00oO in oOOo0 :
  o0OoOO000ooO0 ( '[COLORgreen]' + oo00O00oO + '[/COLOR]' , url , 1006 , iiIi1IIi1I )
  if 9 - 9: o0000oOoOoO0o . Ooo00oOo00o * i1IIi . OoooooooOO
def II1OoooOo ( name , url , iconimage = None ) :
 print '--- Playing "{0}". {1}' . format ( name , url )
 I1I1IIiiii1ii = xbmcgui . ListItem ( path = url , thumbnailImage = iconimage )
 I1I1IIiiii1ii . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , I1I1IIiiii1ii )
 if 92 - 92: OoOO / OoOO0ooOOoo0O . ii11ii1ii
 if 30 - 30: o00O0oo . ii11ii1ii / OoOO0ooOOoo0O
def i1II11IiiiI ( url ) :
 Iiii1i1 = OO ( url )
 oOOo0 = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( Iiii1i1 )
 for url , iiIiIIIiiI , oo00O00oO in oOOo0 :
  o0OoOO000ooO0 ( '[COLORgreen]' + oo00O00oO + '[/COLOR]' , url , 1006 , iiIiIIIiiI )
def IIIi ( url ) :
 Iiii1i1 = OO ( url )
 Ii1iiI1 = url
 oOOo0 = re . compile ( "<a href='(.+?)'>(.+?)</a>" ) . findall ( Iiii1i1 )
 for url , oo00O00oO in oOOo0 :
  if '.mp3' in oo00O00oO :
   print '<<<<<<<<<<<<<<<<<<<' + url + '>>>>>>>>>>>>>>>>>>>>>>>>>>>'
   iii1 ( ( oo00O00oO ) . replace ( '.mp3' , '' ) . replace ( '/' , '' ) , 'http://hypem.com' + url , 222 , iIii1 + 'music.png' )
  else :
   o0OoOO000ooO0 ( ( oo00O00oO ) . replace ( '/' , '' ) , Ii1iiI1 + url , 1011 , iIii1 + 'music.png' )
def o0ooOOoO0oO0 ( ) :
 Iiii1i1 = OO ( oOo0oooo00o ( 'aHR0cDovL3d3dy5jeW4ubmV0L211c2ljLw==' ) )
 oOOo0 = re . compile ( '<td><a href="(.+?)"><img src="(.+?)"><br>(.+?)</a></td>' , re . DOTALL ) . findall ( Iiii1i1 )
 for oo000o , iiIiIIIiiI , oo00O00oO in oOOo0 :
  o0OoOO000ooO0 ( oo00O00oO , ( 'http://www.cyn.net/music/' + oo000o ) . replace ( ' ' , '%20' ) , 1031 , ( 'http://www.cyn.net/music/' + iiIiIIIiiI ) . replace ( ' ' , '%20' ) )
def oo00I1IiI1IIiI ( url , img ) :
 Iiii1i1 = OO ( url )
 iIIi = url
 img = img
 oOOo0 = re . compile ( '<a href="(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( Iiii1i1 )
 for url , oo00O00oO in oOOo0 :
  iii1 ( ( oo00O00oO ) . replace ( '.mp3' , '' ) , ( iIIi + '/' + url ) . replace ( ' ' , '%20' ) , 222 , img )
  if 79 - 79: i1IIi
  if 1 - 1: OoOO / i1IIi
def O0oo0 ( ) :
 ooOOoOo = ( oOo0oooo00o ( 'aHR0cDovL2h5cGVtLmNvbS9kb3dubG9hZC8=' ) )
 iiIi11iI1iii = Oo0o0000o0o0 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oo000 = iiIi11iI1iii . lower ( )
 oo000o = ( oOo0oooo00o ( 'aHR0cDovL3Bhbmljc3RyZWFtLm5ldC9zdHJlYW1zLw==' ) )
 iIIi = ( oOo0oooo00o ( 'aHR0cDovL21hc2xvdmQubm8taXAub3JnL3B1YmxpYy9tcDMv' ) )
 oooO = ( oOo0oooo00o ( 'aHR0cDovL3d3dy5jeW4ubmV0L211c2ljLw==' ) )
 if 37 - 37: i11iIiiIii
 o0000oO = IIi11 ( oo000o )
 OoOOO = IIi11 ( iIIi )
 iIi1Ii = IIi11 ( oooO )
 if 12 - 12: ii11ii1ii / o00O0oo
 if o0000oO != 'Failed' :
  oOOo0 = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( o0000oO )
  for oo00O00oO in oOOo0 :
   if iiIi11iI1iii in oo00O00oO . lower ( ) :
    o0OoOO000ooO0 ( ( oo00O00oO + ' source 1' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( oo000o + oo00O00oO ) . replace ( ' ' , '%20' ) , 1006 , '' )
    if 5 - 5: OoooooooOO
    I11II1i ( 'tvshows' , 'Media Info 3' )
 if OoOOO != 'Failed' :
  oOOOoo00 = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( o0000oO )
  for oo00O00oO in oOOOoo00 :
   if iiIi11iI1iii in oo00O00oO . lower ( ) :
    o0OoOO000ooO0 ( ( oo00O00oO + ' source 2' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( iIIi + oo00O00oO ) . replace ( ' ' , '%20' ) , 1006 , '' )
    if 18 - 18: OOOo0 % OoooooooOO - oO0o0ooO0 . i11iIiiIii * Oo % o00O0oo
    I11II1i ( 'tvshows' , 'Media Info 3' )
 if iIi1Ii != 'Failed' :
  iIi1I11I = re . compile ( '<td><a href=".+?"><img src=".+?"><br>(.+?)</a></td>' , re . DOTALL ) . findall ( iIi1Ii )
  for oo00O00oO in iIi1I11I :
   if iiIi11iI1iii in oo00O00oO . lower ( ) :
    o0OoOO000ooO0 ( ( oo00O00oO + ' source 3' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( oooO + oo00O00oO ) . replace ( ' ' , '%20' ) , 1031 , '' )
    if 12 - 12: i1IIi / OoOO0ooOOoo0O % o0oO0 * IIII * O0 * iIii1I11I1II1
    I11II1i ( 'tvshows' , 'Media Info 3' )
    if 93 - 93: Oo / ii11ii1ii + i1IIi * OoOO . OoooooooOO
    if 54 - 54: O0 / IIII % o0oO0 * i1IIi * O0
    if 48 - 48: OOooOOo . OoOO % I1IiI - I1IiI
    if 33 - 33: o0000oOoOoO0o % OoOoOO00 + Ooo00oOo00o
    if 93 - 93: i1IIi . IIII / OOOo0 + IIII
    if 58 - 58: ii11ii1ii + O0 . Oo + I1IiI - Ooo00oOo00o - I1IiI
def IIiiI ( ) :
 Iiii1i1 = oOoO0o00OO0 ( 'http://www.animetoon.org/cartoon' )
 oOOo0 = re . compile ( '<td><a href="(.+?)">(.+)</a></td>' ) . findall ( Iiii1i1 )
 for oo000o , oo00O00oO in oOOo0 :
  o0OoOO000ooO0 ( oo00O00oO , oo000o , 1002 , iIii1 + 'anime.png' )
  if 36 - 36: oO0o0ooO0
  if 52 - 52: O0oO % O0 . i1IIi . OoooooooOO
  if 33 - 33: OoOO0ooOOoo0O % OoOoOO00
def O000oo00OOOOO ( url ) :
 Iiii1i1 = oOoO0o00OO0 ( url )
 oOOOoo00 = re . compile ( '<img src="(.+?)" id="series_image" width="250" height="370" alt=".+?" />' ) . findall ( Iiii1i1 )
 for iiIiIIIiiI in oOOOoo00 :
  o0o0OoOo0O0OO = iiIiIIIiiI
 iIi1I11I = re . compile ( '<li><a href="(.+?)">Next</a></li>' ) . findall ( Iiii1i1 )
 for url in iIi1I11I :
  o0OoOO000ooO0 ( 'NEXT PAGE' , url , 1002 , o0o0OoOo0O0OO )
 oOOo0 = re . compile ( '&nbsp;<a href="(.+?)">(.+?)</a>' ) . findall ( Iiii1i1 )
 for url , oo00O00oO in oOOo0 :
  o0OoOO000ooO0 ( oo00O00oO , url , 1003 , o0o0OoOo0O0OO )
 xbmcplugin . addSortMethod ( Oo00OOOOO , xbmcplugin . SORT_METHOD_TITLE ) ;
def OOo ( url , IMAGE ) :
 Iiii1i1 = oOoO0o00OO0 ( url )
 oOOo0 = re . compile ( '"playlist">(.+?)</span></div><div><iframe src="(.+?)"' ) . findall ( Iiii1i1 )
 for oo00O00oO , url in oOOo0 :
  print oo00O00oO + '     ' + url
  if 'easy' in url :
   o000O0oo ( url )
  elif 'playpanda' in url :
   o000O0oo ( url )
   if 78 - 78: Ooo00oOo00o / Oo - iIii1I11I1II1 - i11iIiiIii * oO0o0ooO0
  xbmcplugin . addSortMethod ( Oo00OOOOO , xbmcplugin . SORT_METHOD_TITLE ) ;
def o000O0oo ( url ) :
 Iiii1i1 = oOoO0o00OO0 ( url )
 oOOo0 = re . compile ( "url: '(.+?)'," ) . findall ( Iiii1i1 )
 for url in oOOo0 :
  iii1 ( 'STREAM' , url , 222 , iIii1 + 'anime.png' )
  if 84 - 84: OoOO0ooOOoo0O + o00O0oo + OOooOOo
  if 33 - 33: o00O0oo
def ooOOO00oOOooO ( url ) :
 ooo0O0OOO000o = urllib2 . Request ( url )
 ooo0O0OOO000o . add_header ( 'User-Agent' , "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0" )
 ooo0O0OOO000o . add_header ( 'referer' , url )
 iiI1iii = urllib2 . urlopen ( ooo0O0OOO000o )
 ooo0O = iiI1iii . read ( )
 iiI1iii . close ( )
 return ooo0O
 if 46 - 46: iIii1I11I1II1 . i11iIiiIii - I1IiI % O0 / OoOoOO00 * i1IIi
def OO ( url ) :
 ooo0O0OOO000o = urllib2 . Request ( url )
 ooo0O0OOO000o . add_header ( 'User-Agent' , "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0" )
 iiI1iii = urllib2 . urlopen ( ooo0O0OOO000o )
 ooo0O = iiI1iii . read ( )
 iiI1iii . close ( )
 return ooo0O
 if 66 - 66: O0
def oOooOOo00ooO ( url ) :
 xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
 oO0o00oOOooO0 = ( '%s%s' % ( OOOoO000 , url ) )
 ooo0O = OO ( url )
 oOOo0 = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( ooo0O )
 for url , iiIi1IIi1I , oo00O00oO in oOOo0 :
  iii1 ( '%s' % ( oo00O00oO ) . replace ( 'GenieTv' , '[COLOR green]GenieTV[/COLOR]' ) . replace ( '.' , ' ' ) . replace ( 'mp4' , '' ) . replace ( 'mkv' , '' ) . replace ( '_' , ' ' ) , '%s' % ( url ) , 222 , iiIi1IIi1I )
  if 71 - 71: O0oO - OOooOOo - OoOO0ooOOoo0O
def oOoooO000O ( url ) :
 iiIO0OO0o0O00oO = xbmc . Player ( o00O ( ) )
 import urlresolver
 try : iiIO0OO0o0O00oO . play ( url )
 except : pass
 from urlresolver import common
 i1111 = xbmcgui . DialogProgress ( )
 i1111 . create ( 'LOADING' , 'Opening %s Now' % ( oo00O00oO ) )
 iiIO0OO0o0O00oO = xbmc . Player ( o00O ( ) )
 url = urlresolver . HostedMediaFile ( url ) . resolve ( )
 if i1111 . iscanceled ( ) :
  print "[COLORred]STREAM CANCELLED[/COLOR]"
  i1iIIi1 = xbmcgui . Dialog ( )
  if i1iIIi1 . yesno ( "[B]CANCELLED[/B]" , '[B]Was There A Problem[/B]' , '' , "" , 'Yes' , 'No' ) :
   i1iIIi1 . ok ( "Message Send" , "Your Message Has Been Sent" )
  else :
   return
 else :
  try : iiIO0OO0o0O00oO . play ( url )
  except : pass
  try : o0oOoO00o . resolve_url ( url )
  except : pass
  i1111 . close ( )
  if 92 - 92: Oo - O0oO
def II11iIIiiiII ( url ) :
 iiIO0OO0o0O00oO = xbmc . Player ( o00O ( ) )
 import urlresolver
 try : iiIO0OO0o0O00oO . play ( url )
 except : pass
 if 24 - 24: OoOO / O0oO / o0000oOoOoO0o % I1IiI / ii11ii1ii * o0oO0
 if 8 - 8: o00O0oo
def o00O ( ) :
 try :
  iIIi1 = getSet ( "core-player" )
  if ( iIIi1 == 'DVDPLAYER' ) : o0Ooo0o0Oo = xbmc . PLAYER_CORE_DVDPLAYER
  elif ( iIIi1 == 'MPLAYER' ) : o0Ooo0o0Oo = xbmc . PLAYER_CORE_MPLAYER
  elif ( iIIi1 == 'PAPLAYER' ) : o0Ooo0o0Oo = xbmc . PLAYER_CORE_PAPLAYER
  else : o0Ooo0o0Oo = xbmc . PLAYER_CORE_AUTO
 except : o0Ooo0o0Oo = xbmc . PLAYER_CORE_AUTO
 return o0Ooo0o0Oo
 return True
 if 55 - 55: iIii1I11I1II1 * oO0o0ooO0
def o0OoOO000ooO0 ( name , url , mode , iconimage ) :
 OooOOOOoO00OoOO = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 oOooo0O0o = True
 Oo000 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 Oo000 . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 oOooo0O0o = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = OooOOOOoO00OoOO , listitem = Oo000 , isFolder = True )
 return oOooo0O0o
 if 85 - 85: iIii1I11I1II1 . OoOoOO00
def iii1 ( name , url , mode , iconimage ) :
 OooOOOOoO00OoOO = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 oOooo0O0o = True
 Oo000 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 Oo000 . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 oOooo0O0o = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = OooOOOOoO00OoOO , listitem = Oo000 , isFolder = False )
 return oOooo0O0o
 if 54 - 54: o00O0oo . OoooooooOO % Oo
 if 22 - 22: OoOO0ooOOoo0O
 if 22 - 22: oO0o0ooO0 * o0000oOoOoO0o - Oo * O0 / i11iIiiIii
 if 78 - 78: Oo * O0 / o0oO0 + OoooooooOO + OoOO0ooOOoo0O
 if 23 - 23: oO0o0ooO0 % OoooooooOO / iIii1I11I1II1 + ii11ii1ii / i1IIi / OOooOOo
 if 94 - 94: i1IIi
 if 36 - 36: OOOo0 + Oo
def OO0ooOoOO0OOo ( heading , announce ) :
 class iIIiiiI1iI1 ( ) :
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
   try : I1II1 = open ( announce ) ; oO00000oO0o0O = I1II1 . read ( )
   except : oO00000oO0o0O = announce
   self . win . getControl ( self . CONTROL_TEXTBOX ) . setText ( str ( oO00000oO0o0O ) )
   return
 iIIiiiI1iI1 ( )
 if 34 - 34: Oo - i1IIi - o0oO0 - i1IIi
def O00Oo ( ) :
 OO0ooOoOO0OOo ( 'These are the main Sources you should get into you XBMC' , '[COLORwhite]http://architects.x10host.com[/COLOR]--- [CR]  [COLORred]http://repo.sharktech.co.uk[/COLOR]--- [CR]   [COLORwhite]http://fusion.tvaddons.ag[/COLOR]--- [CR]  [COLORred]http://i.totalxbmc.tv[/COLOR]--- [CR]   [COLORwhite]http://www.xunitytalk.com/xfinity[/COLOR]--- [CR]  [COLORred]http://srp.nu[/COLOR]--- [CR]   [COLORwhite]http://solved.no-issue.ca[/COLOR]--- [CR]  [COLORred]http://xbmc.aminhacasadigital.com[/COLOR]--- [CR]   [COLORwhite]http://xbmc.movieshd.co[/COLOR]--- [CR]  [COLORred]http://install.kaosbox.tv[/COLOR]--- [CR]   [COLORwhite]http://kodi-repo.com/mxr[/COLOR]--- [CR]  [COLORred]http://kodi.metalkettle.co[/COLOR]--- [CR]   [COLORwhite]http://prozone.getxbmc.com[/COLOR]--- [CR]  [COLORred]http://transform.mega-tron.tv[/COLOR]--- [CR]   [COLORwhite]http://muckys.kodimediaportal.ml[/COLOR]--- [CR]  [COLORred]http://jas0npc.pcriot.com[/COLOR]--- [CR]  [COLORwhite]Sports devil source[/COLOR]--- [CR]  [COLORred]http://iwillfolo.com/iwf[/COLOR]' )
 if 38 - 38: i1IIi . i11iIiiIii
 if 93 - 93: o0000oOoOoO0o * OoOoOO00 / o00O0oo - OOooOOo
 if 98 - 98: i11iIiiIii / OOOo0 * OOooOOo / O0oO
 if 67 - 67: o0000oOoOoO0o % OoOO
 if 39 - 39: i11iIiiIii + IIII
def O0O00Oo ( ) :
 xbmc . executebuiltin ( 'UpdateLocalAddons' )
 xbmc . executebuiltin ( 'UpdateAddonRepos' )
 i1iIIi1 = xbmcgui . Dialog ( )
 i1iIIi1 . ok ( "GenieTv" , '' , '                                 REFRESH SUCCESSFUL :)' , "                          [COLOR gold]Brought To You By Kodi Support Group, GenieTv[/COLOR]" )
 return
 if 7 - 7: iIii1I11I1II1 - i1IIi
 if 10 - 10: O0oO % O0 / OOOo0 % o0000oOoOoO0o
 if 25 - 25: OoOoOO00 / Ooo00oOo00o
 if 64 - 64: O0 % o0oO0
 if 40 - 40: OOooOOo + o0000oOoOoO0o
 if 77 - 77: i11iIiiIii % IIII + O0oO % OoooooooOO - o0000oOoOoO0o
 if 26 - 26: Oo + O0 - iIii1I11I1II1
 if 47 - 47: OoooooooOO
 if 2 - 2: I1IiI % O0oO * Oo * I1IiI
 if 65 - 65: i11iIiiIii + Oo * OoooooooOO - Ooo00oOo00o
 if 26 - 26: OOooOOo % OoOO0ooOOoo0O + OoOO0ooOOoo0O % o0000oOoOoO0o * i11iIiiIii / oO0o0ooO0
 if 64 - 64: OoOO % I1IiI / OoOoOO00 % o0oO0 - oO0o0ooO0
 if 2 - 2: O0oO - ii11ii1ii + OOooOOo * Ooo00oOo00o / oO0o0ooO0
 if 26 - 26: OoOO0ooOOoo0O * Oo
 if 31 - 31: o0000oOoOoO0o * OoOO . o00O0oo
 if 35 - 35: o0000oOoOoO0o
 if 94 - 94: o0oO0 / i11iIiiIii % O0
 if 70 - 70: o0000oOoOoO0o - Oo / OoooooooOO % OoooooooOO
 if 95 - 95: OoooooooOO % OoooooooOO . o00O0oo
 if 26 - 26: OoOO + IIII - OoOoOO00 . OoOoOO00 + ii11ii1ii + I1IiI
 if 68 - 68: O0
 if 76 - 76: ii11ii1ii
 if 99 - 99: OOooOOo
 if 1 - 1: o00O0oo * I1IiI * Ooo00oOo00o + Oo
def O0OOoOooO00 ( url ) :
 ooo0O = oOoO0o00OO0 ( OooO0 + o0o00OOOO ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 oOOo0 = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( ooo0O )
 for oo00O00oO , url , iIiIIIi , ooo00OOOooO , O00OOOoOoo0O in oOOo0 :
  oOOo0oo ( oo00O00oO , url , 42 , iIiIIIi , ooo00OOOooO , O00OOOoOoo0O )
 I11II1i ( 'movies' , 'MAIN' )
 if 42 - 42: o0oO0 * oO0o0ooO0
def i1iIIiI1111 ( url ) :
 ooo0O = oOoO0o00OO0 ( OooO0 + OooOO ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 oOOo0 = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( ooo0O )
 for oo00O00oO , url , iIiIIIi , ooo00OOOooO , O00OOOoOoo0O in oOOo0 :
  oOOo0oo ( oo00O00oO , url , 42 , iIiIIIi , ooo00OOOooO , O00OOOoOoo0O )
 I11II1i ( 'movies' , 'MAIN' )
 if 86 - 86: o00O0oo . OoOO0ooOOoo0O / IIII - OoooooooOO
def iii1IiI1i ( url ) :
 ooo0O = oOoO0o00OO0 ( OooO0 + OooO0ooO0o0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 oOOo0 = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( ooo0O )
 for oo00O00oO , url , iIiIIIi , ooo00OOOooO , O00OOOoOoo0O in oOOo0 :
  oOOo0oo ( oo00O00oO , url , 42 , iIiIIIi , ooo00OOOooO , O00OOOoOoo0O )
 I11II1i ( 'movies' , 'MAIN' )
 if 88 - 88: OoOO % Oo - o0000oOoOoO0o % OoOO + IIII - oO0o0ooO0
def ii1OO0 ( url ) :
 ooo0O = oOoO0o00OO0 ( OooO0 + OoOoO00OOoOOOo0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 oOOo0 = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( ooo0O )
 for oo00O00oO , url , iIiIIIi , ooo00OOOooO , O00OOOoOoo0O in oOOo0 :
  oOOo0oo ( oo00O00oO , url , 42 , iIiIIIi , ooo00OOOooO , O00OOOoOoo0O )
 I11II1i ( 'movies' , 'MAIN' )
 if 84 - 84: OoOO + OoOO0ooOOoo0O . oO0o0ooO0
def O0o00 ( url ) :
 ooo0O = oOoO0o00OO0 ( OooO0 + I1I1i1i ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 oOOo0 = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( ooo0O )
 for oo00O00oO , url , iIiIIIi , ooo00OOOooO , O00OOOoOoo0O in oOOo0 :
  oOOo0oo ( oo00O00oO , url , 42 , iIiIIIi , ooo00OOOooO , O00OOOoOoo0O )
 I11II1i ( 'movies' , 'MAIN' )
 if 74 - 74: O0 % OoooooooOO * Oo + OoOO0ooOOoo0O * oO0o0ooO0
def O000OO ( url ) :
 ooo0O = oOoO0o00OO0 ( OooO0 + I1Ii ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 oOOo0 = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( ooo0O )
 for oo00O00oO , url , iIiIIIi , ooo00OOOooO , O00OOOoOoo0O in oOOo0 :
  oOOo0oo ( oo00O00oO , url , 42 , iIiIIIi , ooo00OOOooO , O00OOOoOoo0O )
 I11II1i ( 'movies' , 'MAIN' )
 if 76 - 76: oO0o0ooO0 % I1IiI % iIii1I11I1II1 . OoOO0ooOOoo0O
def i11i ( url ) :
 ooo0O = oOoO0o00OO0 ( OooO0 + O0o0O00o0o ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 oOOo0 = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( ooo0O )
 for oo00O00oO , url , iIiIIIi , ooo00OOOooO , O00OOOoOoo0O in oOOo0 :
  oOOo0oo ( oo00O00oO , url , 42 , iIiIIIi , ooo00OOOooO , O00OOOoOoo0O )
 I11II1i ( 'movies' , 'MAIN' )
 if 6 - 6: ii11ii1ii - OoOO * i11iIiiIii + I1IiI / o0oO0 % OoOO0ooOOoo0O
def II11IiIIiiI ( url ) :
 ooo0O = oOoO0o00OO0 ( OooO0 + OOo0oOOOOoo0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 oOOo0 = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( ooo0O )
 for oo00O00oO , url , iIiIIIi , ooo00OOOooO , O00OOOoOoo0O in oOOo0 :
  oOOo0oo ( oo00O00oO , url , 42 , iIiIIIi , ooo00OOOooO , O00OOOoOoo0O )
 I11II1i ( 'movies' , 'MAIN' )
 if 80 - 80: i11iIiiIii % ii11ii1ii
def OOO00o0 ( url ) :
 ooo0O = oOoO0o00OO0 ( OooO0 + OOoO ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 oOOo0 = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( ooo0O )
 for oo00O00oO , url , iIiIIIi , ooo00OOOooO , O00OOOoOoo0O in oOOo0 :
  oOOo0oo ( oo00O00oO , url , 42 , iIiIIIi , ooo00OOOooO , O00OOOoOoo0O )
 I11II1i ( 'movies' , 'MAIN' )
 if 81 - 81: iIii1I11I1II1
def i1i1IIII ( url ) :
 ooo0O = oOoO0o00OO0 ( OooO0 + o0O0O ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 oOOo0 = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( ooo0O )
 for oo00O00oO , url , iIiIIIi , ooo00OOOooO , O00OOOoOoo0O in oOOo0 :
  oOOo0oo ( oo00O00oO , url , 5 , iIiIIIi , ooo00OOOooO , O00OOOoOoo0O )
 I11II1i ( 'movies' , 'MAIN' )
 if 45 - 45: OOooOOo % Oo * i1IIi - O0
 if 82 - 82: OoOoOO00 / oO0o0ooO0
 if 96 - 96: Oo / OoOO . OoOoOO00 . Oo
 if 91 - 91: OoOoOO00 . OoOO0ooOOoo0O + OOooOOo
 if 8 - 8: OoOO0ooOOoo0O * Oo / oO0o0ooO0 - Ooo00oOo00o - OoooooooOO
 if 100 - 100: OoOO . iIii1I11I1II1 . iIii1I11I1II1
 if 55 - 55: OoOO
 if 37 - 37: IIII / i11iIiiIii / Oo
 if 97 - 97: O0oO . o0000oOoOoO0o / OOOo0
def o00OO0o0 ( ) :
 try :
  if os . path . exists ( II ) == True :
   i1iIIi1 = xbmcgui . Dialog ( )
   if i1iIIi1 . yesno ( "Delete Thumbnails" , "[COLOR gold][B]##########WARNING ANDROID ONLY##########[/B][/COLOR]" , "This feature deletes your thumbnail folder and textures13.db" , "Are you sure you want to do proceed? This Can NOT Be Undone" ) :
    for iiI11ii1I1 , Ooo0OOoOoO0 , oOo0OOoO0 in os . walk ( II ) :
     i1II1IiiIi = 0
     i1II1IiiIi += len ( oOo0OOoO0 )
     if i1II1IiiIi > 0 :
      for I1II1 in oOo0OOoO0 :
       os . unlink ( os . path . join ( iiI11ii1I1 , I1II1 ) )
  ii111iI1i1 = os . path . join ( iiI1IiI , "Textures13.db" )
  os . unlink ( ii111iI1i1 )
  i1iIIi1 . ok ( "Restart KODI" , "Please restart KODI to rebuild thumbnail library" )
 except :
  i1iIIi1 = xbmcgui . Dialog ( )
  i1iIIi1 . ok ( i11 , "Error Deleting Thumbnails please visit Kodi Support Group, GenieTv on facebook" )
 return
 if 80 - 80: Ooo00oOo00o / IIII * OOOo0 % IIII
 if 95 - 95: O0 / o0000oOoOoO0o . O0oO
 if 17 - 17: o0000oOoOoO0o
 if 56 - 56: o0oO0 * OOooOOo + o0000oOoOoO0o
 if 48 - 48: IIII * Ooo00oOo00o % O0oO - o0000oOoOoO0o
 if 72 - 72: i1IIi % o0oO0 % IIII % OoOO - OoOO
 if 97 - 97: OOooOOo * O0 / OOooOOo * Ooo00oOo00o * Oo
 if 38 - 38: O0oO
 if 25 - 25: iIii1I11I1II1 % OoOoOO00 / o0000oOoOoO0o / ii11ii1ii
def iI1iIIIIIiIi1 ( url ) :
 print '############################################################       DELETING STANDARD CACHE             ###############################################################'
 iIioOo = os . path . join ( xbmc . translatePath ( 'special://home' ) , 'cache' )
 if os . path . exists ( iIioOo ) == True :
  for iiI11ii1I1 , Ooo0OOoOoO0 , oOo0OOoO0 in os . walk ( iIioOo ) :
   i1II1IiiIi = 0
   i1II1IiiIi += len ( oOo0OOoO0 )
   if 66 - 66: OoOoOO00 + Ooo00oOo00o
   if 19 - 19: Ooo00oOo00o . OoooooooOO * Ooo00oOo00o + IIII + OoooooooOO
   if i1II1IiiIi > 0 :
    if 19 - 19: Oo
    i1iIIi1 = xbmcgui . Dialog ( )
    if i1iIIi1 . yesno ( "Delete KODI Cache Files" , str ( i1II1IiiIi ) + " files found" , "Do you want to delete them?" ) :
     if 75 - 75: OoooooooOO . OoOO0ooOOoo0O + Ooo00oOo00o / o00O0oo - OOOo0 % o00O0oo
     for I1II1 in oOo0OOoO0 :
      try :
       os . unlink ( os . path . join ( iiI11ii1I1 , I1II1 ) )
      except :
       pass
     for O0OooooO0o0O0 in Ooo0OOoOoO0 :
      try :
       shutil . rmtree ( os . path . join ( iiI11ii1I1 , O0OooooO0o0O0 ) )
      except :
       pass
       if 74 - 74: I1IiI / i1IIi % OoooooooOO
   else :
    pass
 if xbmc . getCondVisibility ( 'system.platform.ATV2' ) :
  o00o0o000Oo = os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'Other' )
  if 100 - 100: i1IIi - i11iIiiIii . O0oO * Ooo00oOo00o
  for iiI11ii1I1 , Ooo0OOoOoO0 , oOo0OOoO0 in os . walk ( o00o0o000Oo ) :
   i1II1IiiIi = 0
   i1II1IiiIi += len ( oOo0OOoO0 )
   if 62 - 62: O0
   if i1II1IiiIi > 0 :
    if 41 - 41: i1IIi - OOOo0
    i1iIIi1 = xbmcgui . Dialog ( )
    if i1iIIi1 . yesno ( "Delete ATV2 Cache Files" , str ( i1II1IiiIi ) + " files found in 'Other'" , "Do you want to delete them?" ) :
     if 48 - 48: OOOo0 - OoOoOO00 / Ooo00oOo00o + OOOo0
     for I1II1 in oOo0OOoO0 :
      os . unlink ( os . path . join ( iiI11ii1I1 , I1II1 ) )
     for O0OooooO0o0O0 in Ooo0OOoOoO0 :
      shutil . rmtree ( os . path . join ( iiI11ii1I1 , O0OooooO0o0O0 ) )
      if 5 - 5: O0
   else :
    pass
  o0oo0Oo = os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'LocalAndRental' )
  if 10 - 10: ii11ii1ii
  for iiI11ii1I1 , Ooo0OOoOoO0 , oOo0OOoO0 in os . walk ( o0oo0Oo ) :
   i1II1IiiIi = 0
   i1II1IiiIi += len ( oOo0OOoO0 )
   if 87 - 87: Oo % o00O0oo
   if i1II1IiiIi > 0 :
    if 53 - 53: i1IIi - IIII + iIii1I11I1II1
    i1iIIi1 = xbmcgui . Dialog ( )
    if i1iIIi1 . yesno ( "Delete ATV2 Cache Files" , str ( i1II1IiiIi ) + " files found in 'LocalAndRental'" , "Do you want to delete them?" ) :
     if 75 - 75: ii11ii1ii
     for I1II1 in oOo0OOoO0 :
      os . unlink ( os . path . join ( iiI11ii1I1 , I1II1 ) )
     for O0OooooO0o0O0 in Ooo0OOoOoO0 :
      shutil . rmtree ( os . path . join ( iiI11ii1I1 , O0OooooO0o0O0 ) )
      if 92 - 92: o0000oOoOoO0o / O0 * OOOo0 - o0000oOoOoO0o
   else :
    pass
    if 99 - 99: i11iIiiIii % OoooooooOO
    if 56 - 56: IIII * O0oO
    if 98 - 98: o0000oOoOoO0o + O0 * O0oO + i11iIiiIii - OoOO0ooOOoo0O - iIii1I11I1II1
    if 5 - 5: OoOO0ooOOoo0O % Oo % IIII % o0oO0
 I1Iiii = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.whatthefurk/cache' ) , '' )
 if os . path . exists ( I1Iiii ) == True :
  for iiI11ii1I1 , Ooo0OOoOoO0 , oOo0OOoO0 in os . walk ( I1Iiii ) :
   i1II1IiiIi = 0
   i1II1IiiIi += len ( oOo0OOoO0 )
   if 22 - 22: o00O0oo * o0000oOoOoO0o + OOOo0 - o0000oOoOoO0o / ii11ii1ii
   if 18 - 18: i1IIi
   if i1II1IiiIi > 0 :
    if 4 - 4: IIII
    i1iIIi1 = xbmcgui . Dialog ( )
    if i1iIIi1 . yesno ( "Delete WTF Cache Files" , str ( i1II1IiiIi ) + " files found" , "Do you want to delete them?" ) :
     if 93 - 93: OoOO % i1IIi
     for I1II1 in oOo0OOoO0 :
      os . unlink ( os . path . join ( iiI11ii1I1 , I1II1 ) )
     for O0OooooO0o0O0 in Ooo0OOoOoO0 :
      shutil . rmtree ( os . path . join ( iiI11ii1I1 , O0OooooO0o0O0 ) )
      if 83 - 83: OOOo0 . Oo - o0000oOoOoO0o . OOooOOo
   else :
    pass
    if 73 - 73: OOOo0 - oO0o0ooO0 . oO0o0ooO0
    if 22 - 22: o0oO0 / o0oO0 - o00O0oo % o0000oOoOoO0o . OoOO0ooOOoo0O + IIII
 OooO00oo0O0 = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.4od/cache' ) , '' )
 if os . path . exists ( OooO00oo0O0 ) == True :
  for iiI11ii1I1 , Ooo0OOoOoO0 , oOo0OOoO0 in os . walk ( OooO00oo0O0 ) :
   i1II1IiiIi = 0
   i1II1IiiIi += len ( oOo0OOoO0 )
   if 10 - 10: IIII / OoooooooOO
   if 50 - 50: i11iIiiIii - OoooooooOO . OoOO + O0 . i1IIi
   if i1II1IiiIi > 0 :
    if 91 - 91: OOooOOo . oO0o0ooO0 % Oo - oO0o0ooO0 . OoOO % i11iIiiIii
    i1iIIi1 = xbmcgui . Dialog ( )
    if i1iIIi1 . yesno ( "Delete 4oD Cache Files" , str ( i1II1IiiIi ) + " files found" , "Do you want to delete them?" ) :
     if 25 - 25: iIii1I11I1II1
     for I1II1 in oOo0OOoO0 :
      os . unlink ( os . path . join ( iiI11ii1I1 , I1II1 ) )
     for O0OooooO0o0O0 in Ooo0OOoOoO0 :
      shutil . rmtree ( os . path . join ( iiI11ii1I1 , O0OooooO0o0O0 ) )
      if 63 - 63: o0oO0
   else :
    pass
    if 96 - 96: o0000oOoOoO0o
    if 34 - 34: I1IiI / Ooo00oOo00o - OOOo0 . O0 . OoOO0ooOOoo0O
 oooO0o0oOoO = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.iplayer/iplayer_http_cache' ) , '' )
 if os . path . exists ( oooO0o0oOoO ) == True :
  for iiI11ii1I1 , Ooo0OOoOoO0 , oOo0OOoO0 in os . walk ( oooO0o0oOoO ) :
   i1II1IiiIi = 0
   i1II1IiiIi += len ( oOo0OOoO0 )
   if 23 - 23: IIII + iIii1I11I1II1 % iIii1I11I1II1 / o0oO0 . OoOO + iIii1I11I1II1
   if 93 - 93: OoOO * OOooOOo / OoOO0ooOOoo0O - OoOO0ooOOoo0O . oO0o0ooO0 / OOOo0
   if i1II1IiiIi > 0 :
    if 11 - 11: O0oO - o0000oOoOoO0o % i11iIiiIii . iIii1I11I1II1 * OOOo0 - Oo
    i1iIIi1 = xbmcgui . Dialog ( )
    if i1iIIi1 . yesno ( "Delete BBC iPlayer Cache Files" , str ( i1II1IiiIi ) + " files found" , "Do you want to delete them?" ) :
     if 73 - 73: O0 + o0oO0 - O0 / OoooooooOO * Oo
     for I1II1 in oOo0OOoO0 :
      os . unlink ( os . path . join ( iiI11ii1I1 , I1II1 ) )
     for O0OooooO0o0O0 in Ooo0OOoOoO0 :
      shutil . rmtree ( os . path . join ( iiI11ii1I1 , O0OooooO0o0O0 ) )
      if 32 - 32: Ooo00oOo00o % OOOo0 % oO0o0ooO0
   else :
    pass
    if 66 - 66: I1IiI + OOooOOo
    if 54 - 54: ii11ii1ii + ii11ii1ii + o0000oOoOoO0o % i1IIi % i11iIiiIii
    if 100 - 100: ii11ii1ii
 OOOoo000o0oo0 = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/script.module.simple.downloader' ) , '' )
 if os . path . exists ( OOOoo000o0oo0 ) == True :
  for iiI11ii1I1 , Ooo0OOoOoO0 , oOo0OOoO0 in os . walk ( OOOoo000o0oo0 ) :
   i1II1IiiIi = 0
   i1II1IiiIi += len ( oOo0OOoO0 )
   if 71 - 71: o0oO0 . o0000oOoOoO0o + OoOO0ooOOoo0O
   if 8 - 8: i11iIiiIii * O0 + ii11ii1ii . iIii1I11I1II1 % o0000oOoOoO0o / o0000oOoOoO0o
   if i1II1IiiIi > 0 :
    if 70 - 70: OOOo0 + o00O0oo
    i1iIIi1 = xbmcgui . Dialog ( )
    if i1iIIi1 . yesno ( "Delete Simple Downloader Cache Files" , str ( i1II1IiiIi ) + " files found" , "Do you want to delete them?" ) :
     if 70 - 70: IIII . i11iIiiIii
     for I1II1 in oOo0OOoO0 :
      os . unlink ( os . path . join ( iiI11ii1I1 , I1II1 ) )
     for O0OooooO0o0O0 in Ooo0OOoOoO0 :
      shutil . rmtree ( os . path . join ( iiI11ii1I1 , O0OooooO0o0O0 ) )
      if 76 - 76: oO0o0ooO0 . IIII % oO0o0ooO0 - O0oO
   else :
    pass
    if 51 - 51: OoooooooOO + OOooOOo * iIii1I11I1II1 * OoOO / i1IIi
    if 19 - 19: oO0o0ooO0 - I1IiI % OoOO / OoooooooOO % oO0o0ooO0
 ooOoOoO0 = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.itv/Images' ) , '' )
 if os . path . exists ( ooOoOoO0 ) == True :
  for iiI11ii1I1 , Ooo0OOoOoO0 , oOo0OOoO0 in os . walk ( ooOoOoO0 ) :
   i1II1IiiIi = 0
   i1II1IiiIi += len ( oOo0OOoO0 )
   if 31 - 31: i11iIiiIii - o0oO0 / ii11ii1ii - o00O0oo
   if 5 - 5: i11iIiiIii * Oo
   if i1II1IiiIi > 0 :
    if 29 - 29: o00O0oo / o0oO0 % o0000oOoOoO0o
    i1iIIi1 = xbmcgui . Dialog ( )
    if i1iIIi1 . yesno ( "Delete ITV Cache Files" , str ( i1II1IiiIi ) + " files found" , "Do you want to delete them?" ) :
     if 10 - 10: iIii1I11I1II1 % OoooooooOO % ii11ii1ii
     for I1II1 in oOo0OOoO0 :
      os . unlink ( os . path . join ( iiI11ii1I1 , I1II1 ) )
     for O0OooooO0o0O0 in Ooo0OOoOoO0 :
      shutil . rmtree ( os . path . join ( iiI11ii1I1 , O0OooooO0o0O0 ) )
      if 39 - 39: OoOoOO00 * I1IiI . O0 * o0000oOoOoO0o
   else :
    pass
    if 89 - 89: o00O0oo - o0oO0 . o0000oOoOoO0o - O0oO - OOOo0
    if 79 - 79: IIII + IIII + o00O0oo
 iiiII1i1I = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.movies4me/cache' ) , '' )
 if os . path . exists ( ooOoOoO0 ) == True :
  for iiI11ii1I1 , Ooo0OOoOoO0 , oOo0OOoO0 in os . walk ( iiiII1i1I ) :
   i1II1IiiIi = 0
   i1II1IiiIi += len ( oOo0OOoO0 )
   if 97 - 97: O0 . O0oO / OoOoOO00 . O0 + OoooooooOO
   if 78 - 78: OoOoOO00 + IIII
   if i1II1IiiIi > 0 :
    if 66 - 66: iIii1I11I1II1
    i1iIIi1 = xbmcgui . Dialog ( )
    if i1iIIi1 . yesno ( "Delete Movies4me Cache Files" , str ( i1II1IiiIi ) + " files found" , "Do you want to delete them?" ) :
     if 57 - 57: IIII
     for I1II1 in oOo0OOoO0 :
      os . unlink ( os . path . join ( iiI11ii1I1 , I1II1 ) )
     for O0OooooO0o0O0 in Ooo0OOoOoO0 :
      shutil . rmtree ( os . path . join ( iiI11ii1I1 , O0OooooO0o0O0 ) )
      if 41 - 41: iIii1I11I1II1 * oO0o0ooO0 + Oo * OOooOOo % IIII / OoOO0ooOOoo0O
   else :
    pass
    if 63 - 63: i1IIi % i11iIiiIii % OoOoOO00 * OoooooooOO
    if 40 - 40: Oo
 iI1Ii11 = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.phstreams/Cache' ) , '' )
 if os . path . exists ( ooOoOoO0 ) == True :
  for iiI11ii1I1 , Ooo0OOoOoO0 , oOo0OOoO0 in os . walk ( iI1Ii11 ) :
   i1II1IiiIi = 0
   i1II1IiiIi += len ( oOo0OOoO0 )
   if 93 - 93: OOOo0 / o0oO0 / o0000oOoOoO0o + OoOoOO00 + i11iIiiIii
   if 16 - 16: OOOo0 - OoOO . Oo
   if i1II1IiiIi > 0 :
    if 94 - 94: I1IiI + IIII . o0oO0
    i1iIIi1 = xbmcgui . Dialog ( )
    if i1iIIi1 . yesno ( "Delete Phoenix Cache Files" , str ( i1II1IiiIi ) + " files found" , "Do you want to delete them?" ) :
     if 69 - 69: O0 - O0
     for I1II1 in oOo0OOoO0 :
      os . unlink ( os . path . join ( iiI11ii1I1 , I1II1 ) )
     for O0OooooO0o0O0 in Ooo0OOoOoO0 :
      shutil . rmtree ( os . path . join ( iiI11ii1I1 , O0OooooO0o0O0 ) )
      if 41 - 41: IIII % OOooOOo
   else :
    pass
    if 67 - 67: O0 % O0oO
    if 35 - 35: OOOo0 . I1IiI + OoooooooOO % Oo % OoOO0ooOOoo0O
 iIi1Ii1111i = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.spotitube/cache' ) , '' )
 if os . path . exists ( ooOoOoO0 ) == True :
  for iiI11ii1I1 , Ooo0OOoOoO0 , oOo0OOoO0 in os . walk ( iIi1Ii1111i ) :
   i1II1IiiIi = 0
   i1II1IiiIi += len ( oOo0OOoO0 )
   if 16 - 16: IIII . o0oO0 . Ooo00oOo00o
   if 53 - 53: I1IiI
   if i1II1IiiIi > 0 :
    if 84 - 84: Ooo00oOo00o
    i1iIIi1 = xbmcgui . Dialog ( )
    if i1iIIi1 . yesno ( "Delete YouTube Music Cache Files" , str ( i1II1IiiIi ) + " files found" , "Do you want to delete them?" ) :
     if 97 - 97: i1IIi
     for I1II1 in oOo0OOoO0 :
      os . unlink ( os . path . join ( iiI11ii1I1 , I1II1 ) )
     for O0OooooO0o0O0 in Ooo0OOoOoO0 :
      shutil . rmtree ( os . path . join ( iiI11ii1I1 , O0OooooO0o0O0 ) )
      if 98 - 98: OoooooooOO - OOOo0 + o0oO0
   else :
    pass
    if 98 - 98: oO0o0ooO0 . IIII . IIII - OoOO0ooOOoo0O
    if 65 - 65: Oo + OOooOOo - o00O0oo
 iiIII11 = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.supercartoons/cache' ) , '' )
 if os . path . exists ( ooOoOoO0 ) == True :
  for iiI11ii1I1 , Ooo0OOoOoO0 , oOo0OOoO0 in os . walk ( iiIII11 ) :
   i1II1IiiIi = 0
   i1II1IiiIi += len ( oOo0OOoO0 )
   if 44 - 44: O0oO - IIII
   if 100 - 100: OoOO . Ooo00oOo00o - o00O0oo + O0 * Ooo00oOo00o
   if i1II1IiiIi > 0 :
    if 59 - 59: OoOoOO00
    i1iIIi1 = xbmcgui . Dialog ( )
    if i1iIIi1 . yesno ( "Delete SuperCartoons Cache Files" , str ( i1II1IiiIi ) + " files found" , "Do you want to delete them?" ) :
     if 43 - 43: Oo + OoooooooOO
     for I1II1 in oOo0OOoO0 :
      os . unlink ( os . path . join ( iiI11ii1I1 , I1II1 ) )
     for O0OooooO0o0O0 in Ooo0OOoOoO0 :
      shutil . rmtree ( os . path . join ( iiI11ii1I1 , O0OooooO0o0O0 ) )
      if 47 - 47: o0oO0
   else :
    pass
    if 92 - 92: o0000oOoOoO0o % i11iIiiIii % Oo
    if 23 - 23: OoOoOO00 * oO0o0ooO0
 o0Oo = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.tvonline.cc/cache' ) , '' )
 if os . path . exists ( ooOoOoO0 ) == True :
  for iiI11ii1I1 , Ooo0OOoOoO0 , oOo0OOoO0 in os . walk ( o0Oo ) :
   i1II1IiiIi = 0
   i1II1IiiIi += len ( oOo0OOoO0 )
   if 16 - 16: oO0o0ooO0 % OOOo0 - o0oO0
   if 100 - 100: OoooooooOO * OoOO
   if i1II1IiiIi > 0 :
    if 83 - 83: iIii1I11I1II1 - o0oO0 - O0oO / Ooo00oOo00o - O0
    i1iIIi1 = xbmcgui . Dialog ( )
    if i1iIIi1 . yesno ( "Delete TVonline Cache Files" , str ( i1II1IiiIi ) + " files found" , "Do you want to delete them?" ) :
     if 81 - 81: o00O0oo - OoOO * ii11ii1ii / O0oO
     for I1II1 in oOo0OOoO0 :
      os . unlink ( os . path . join ( iiI11ii1I1 , I1II1 ) )
     for O0OooooO0o0O0 in Ooo0OOoOoO0 :
      shutil . rmtree ( os . path . join ( iiI11ii1I1 , O0OooooO0o0O0 ) )
      if 21 - 21: Ooo00oOo00o
   else :
    pass
    if 63 - 63: o0000oOoOoO0o . O0 * o0000oOoOoO0o + iIii1I11I1II1
    if 46 - 46: i1IIi + OoOoOO00 * i1IIi - o00O0oo
 Oo0OOOoOO = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.youtube/kodion' ) , '' )
 if os . path . exists ( ooOoOoO0 ) == True :
  for iiI11ii1I1 , Ooo0OOoOoO0 , oOo0OOoO0 in os . walk ( Oo0OOOoOO ) :
   i1II1IiiIi = 0
   i1II1IiiIi += len ( oOo0OOoO0 )
   if 11 - 11: O0 * I1IiI
   if 37 - 37: I1IiI + O0 . O0 * Oo % O0oO / oO0o0ooO0
   if i1II1IiiIi > 0 :
    if 18 - 18: OoooooooOO
    i1iIIi1 = xbmcgui . Dialog ( )
    if i1iIIi1 . yesno ( "Delete YouTube Cache Files" , str ( i1II1IiiIi ) + " files found" , "Do you want to delete them?" ) :
     if 57 - 57: o0oO0 . I1IiI * OOooOOo - OoooooooOO
     for I1II1 in oOo0OOoO0 :
      os . unlink ( os . path . join ( iiI11ii1I1 , I1II1 ) )
     for O0OooooO0o0O0 in Ooo0OOoOoO0 :
      shutil . rmtree ( os . path . join ( iiI11ii1I1 , O0OooooO0o0O0 ) )
      if 75 - 75: i11iIiiIii / OOooOOo . IIII . i1IIi . i1IIi / o0000oOoOoO0o
   else :
    pass
    if 94 - 94: o0oO0 + OOOo0
    if 56 - 56: I1IiI % OOooOOo
    if 40 - 40: OoOO0ooOOoo0O / IIII
 i1i11I1I1 = xbmc . translatePath ( 'special://masterprofile/addon_data/plugin.video.genesis' )
 i1iIIi1 = xbmcgui . Dialog ( )
 try :
  if i1iIIi1 . yesno ( "Delete Genesis Cache Files" , "Do you want to delete cache" ) :
   OOOOOoooO = os . path . join ( i1i11I1I1 , "cache.db" )
   os . unlink ( OOOOOoooO )
   if 59 - 59: OoOO % o0oO0
 except :
  pass
  if 36 - 36: OoooooooOO
 i1iIIi1 = xbmcgui . Dialog ( )
 i1iIIi1 . ok ( "GenieTv" , "                               Finished Deleting Cache " , "                          [COLOR gold]Brought To You By GenieTv[/COLOR]" )
 if 33 - 33: O0 + Oo - iIii1I11I1II1 % i11iIiiIii / OOOo0
 if 47 - 47: ii11ii1ii * OoOO + iIii1I11I1II1 - OoOO / IIII
 if 86 - 86: IIII
 if 43 - 43: OOOo0 / oO0o0ooO0 / o0oO0 + iIii1I11I1II1 + OoooooooOO
 if 33 - 33: OoOoOO00 - IIII - o0oO0
 if 92 - 92: Ooo00oOo00o * IIII
 if 92 - 92: OoOO
 if 7 - 7: oO0o0ooO0
 if 73 - 73: Ooo00oOo00o % ii11ii1ii
def I1I11i ( url ) :
 print '###' + i11 + ' - DELETING PACKAGES###'
 Iii1Iii = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' , '' ) )
 try :
  for iiI11ii1I1 , Ooo0OOoOoO0 , oOo0OOoO0 in os . walk ( Iii1Iii ) :
   i1II1IiiIi = 0
   i1II1IiiIi += len ( oOo0OOoO0 )
   if 91 - 91: o0oO0 * IIII * OoOoOO00
   if 79 - 79: O0oO
   if i1II1IiiIi > 0 :
    if 8 - 8: oO0o0ooO0 - OoOoOO00
    i1iIIi1 = xbmcgui . Dialog ( )
    if i1iIIi1 . yesno ( "Delete Package Cache Files" , str ( i1II1IiiIi ) + " files found" , "Do you want to delete them?" ) :
     if 18 - 18: I1IiI
     for I1II1 in oOo0OOoO0 :
      os . unlink ( os . path . join ( iiI11ii1I1 , I1II1 ) )
     for O0OooooO0o0O0 in Ooo0OOoOoO0 :
      shutil . rmtree ( os . path . join ( iiI11ii1I1 , O0OooooO0o0O0 ) )
     i1iIIi1 = xbmcgui . Dialog ( )
     i1iIIi1 . ok ( i11 , "       Deleting Packages all done" )
    else :
     pass
   else :
    i1iIIi1 = xbmcgui . Dialog ( )
    i1iIIi1 . ok ( i11 , "       No Packages to DELETE" )
 except :
  i1iIIi1 = xbmcgui . Dialog ( )
  i1iIIi1 . ok ( i11 , "Error Deleting Packages please visit Kodi Support Group, GenieTv on facebook" )
 return
 if 13 - 13: IIII % Ooo00oOo00o * iIii1I11I1II1 + ii11ii1ii - o0oO0 - OOOo0
 if 74 - 74: OoOoOO00 / O0
 if 56 - 56: o0000oOoOoO0o - O0 / O0 * i1IIi . OoooooooOO % iIii1I11I1II1
 if 21 - 21: IIII - OOOo0 % OoooooooOO + OOooOOo
 if 92 - 92: o0oO0 + IIII
 if 52 - 52: OoOoOO00 / OOOo0 . OoOO * IIII . o0000oOoOoO0o
 if 25 - 25: i11iIiiIii / I1IiI - O0oO / Ooo00oOo00o . OOooOOo . OOooOOo
 if 6 - 6: OoOO . o0000oOoOoO0o
 if 43 - 43: ii11ii1ii + OOooOOo
def iI1iiiiiii ( url , name ) :
 oOo00O0oo00o0 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 Oo00oo = os . path . join ( oOo00O0oo00o0 , 'advancedsettings.xml' )
 i1iIIi1 = xbmcgui . Dialog ( )
 oO0oO = os . path . join ( oOo00O0oo00o0 , 'advancedsettings.xml.bak' )
 if os . path . exists ( oO0oO ) == False :
  if i1iIIi1 . yesno ( "Back Up Original" , 'Have You Backed Up Your Original?' , '' , "[B][COLOR red]     AS YOU CANNOT GO BACK !!![/B][/COLOR]" ) :
   print '###' + i11 + ' - ADVANCED XML###'
   oOo00O0oo00o0 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
   Oo00oo = os . path . join ( oOo00O0oo00o0 , 'advancedsettings.xml' )
   try :
    os . remove ( Oo00oo )
    print '=== GenieTv - REMOVING    ' + str ( Oo00oo ) + '    ==='
   except :
    pass
   ooo0O = I11 . http_GET ( url ) . content
   IIo0Oo0oO0oOO00 = open ( Oo00oo , "w" )
   IIo0Oo0oO0oOO00 . write ( ooo0O )
   IIo0Oo0oO0oOO00 . close ( )
   print '=== GenieTv - WRITING NEW    ' + str ( Oo00oo ) + '    ==='
   i1iIIi1 = xbmcgui . Dialog ( )
   i1iIIi1 . ok ( i11 , "       Done Adding new Advanced XML" )
 else :
  print '###' + i11 + ' - ADVANCED XML###'
  oOo00O0oo00o0 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
  Oo00oo = os . path . join ( oOo00O0oo00o0 , 'advancedsettings.xml' )
  try :
   os . remove ( Oo00oo )
   print '=== GenieTv - REMOVING    ' + str ( Oo00oo ) + '    ==='
  except :
   pass
  ooo0O = I11 . http_GET ( url ) . content
  IIo0Oo0oO0oOO00 = open ( Oo00oo , "w" )
  IIo0Oo0oO0oOO00 . write ( ooo0O )
  IIo0Oo0oO0oOO00 . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( Oo00oo ) + '    ==='
  i1iIIi1 = xbmcgui . Dialog ( )
  i1iIIi1 . ok ( i11 , "       Done Adding new Advanced XML" )
 return
 if 71 - 71: O0oO / OOOo0 / O0
def IiI ( url , name ) :
 print '###' + i11 + ' - CHECK ADVANCE XML###'
 oOo00O0oo00o0 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 Oo00oo = os . path . join ( oOo00O0oo00o0 , 'advancedsettings.xml' )
 try :
  IIo0Oo0oO0oOO00 = open ( Oo00oo ) . read ( )
  if 'zero' in IIo0Oo0oO0oOO00 :
   name = '0CACHE'
  elif 'tuxen' in IIo0Oo0oO0oOO00 :
   name = 'TUXENS'
  elif 'muckys' in IIo0Oo0oO0oOO00 :
   name = 'MUCKYS'
  elif 'p2p1' in IIo0Oo0oO0oOO00 :
   name = '1st P2P RECOMMENDED'
  elif 'p2p2' in IIo0Oo0oO0oOO00 :
   name = '2nd P2P RECOMMENDED'
  elif 'mikey' in IIo0Oo0oO0oOO00 :
   name = 'MIKEY1234'
 except :
  name = "NO ADVANCED"
 i1iIIi1 = xbmcgui . Dialog ( )
 i1iIIi1 . ok ( i11 , "[COLOR yellow]YOU HAVE[/COLOR] " + name + "[COLOR yellow] XML SETTINGS SETUP[/COLOR]" )
 return
 if 34 - 34: O0 / OoOO0ooOOoo0O
def OOOoo0O00Oooo ( url ) :
 print '###' + i11 + ' - DELETING ADVANCE XML###'
 oOo00O0oo00o0 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 Oo00oo = os . path . join ( oOo00O0oo00o0 , 'advancedsettings.xml' )
 try :
  os . remove ( Oo00oo )
  i1iIIi1 = xbmcgui . Dialog ( )
  print '=== GenieTv - DELETING    ' + str ( Oo00oo ) + '    ==='
  i1iIIi1 . ok ( i11 , "       Remove Advanced Settings Sucessfull" )
 except :
  i1iIIi1 = xbmcgui . Dialog ( )
  i1iIIi1 . ok ( i11 , "       No Advanced Settings To Remove" )
 return
 if 31 - 31: o0000oOoOoO0o + OoOoOO00 * Oo + Oo . o0000oOoOoO0o
 if 90 - 90: O0oO * iIii1I11I1II1 - o0000oOoOoO0o % o0oO0 . IIII
 if 66 - 66: I1IiI
 if 25 - 25: Oo * OoooooooOO % OoOO * IIII * OoOO0ooOOoo0O
 if 90 - 90: OOooOOo * OoOO0ooOOoo0O / IIII
 if 40 - 40: OOOo0 * OOooOOo . OOOo0
 if 62 - 62: o0oO0 + OoOoOO00 % o0oO0
 if 50 - 50: OoooooooOO + OoOO * OOOo0 - o00O0oo / i11iIiiIii
 if 5 - 5: O0 - OOOo0
 if 44 - 44: OoOoOO00 . OoOoOO00 + OoOO0ooOOoo0O * o00O0oo
def i1iIi ( url = 'http://www.iplocation.net/' , inc = 1 ) :
 oOOo0 = re . compile ( "<td width='80'>(.+?)</td><td>(.+?)</td><td>(.+?)</td><td>.+?</td><td>(.+?)</td>" ) . findall ( I11 . http_GET ( url ) . content )
 for i1II1i , iI1iI , oOo , III1IiIi1 in oOOo0 :
  if inc < 2 : i1iIIi1 = xbmcgui . Dialog ( ) ; i1iIIi1 . ok ( 'Check My IP' , "[B][COLOR gold]Your IP Address is: [/COLOR][/B] %s" % i1II1i , '[B][COLOR gold]Your IP is based in: [/COLOR][/B] %s' % oOo , '[B][COLOR gold]Your Service Provider is:[/COLOR][/B] %s' % III1IiIi1 )
  inc = inc + 1
  if 72 - 72: Ooo00oOo00o + i11iIiiIii + ii11ii1ii
  if 96 - 96: OoOO % i1IIi / OOooOOo
  if 13 - 13: OoOoOO00 - Oo % i11iIiiIii + oO0o0ooO0
  if 88 - 88: O0 . OoOO % OOOo0
  if 10 - 10: OOOo0 + O0
  if 75 - 75: O0 % iIii1I11I1II1 / I1IiI % OoOO0ooOOoo0O / IIII
  if 31 - 31: i11iIiiIii * I1IiI
  if 69 - 69: i11iIiiIii
  if 61 - 61: O0
def iIiiI111I11 ( url , name ) :
 i1iIIi1 = xbmcgui . Dialog ( )
 if i1iIIi1 . yesno ( "GenieTv" , '                                    Install Latest .ini File' ) :
  print '###' + i11 + ' - CUSTOM FTV INI###'
  oOo00O0oo00o0 = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/script.ftvguide' , '' ) )
  Oo00oo = os . path . join ( oOo00O0oo00o0 , 'addons2.ini' )
  ooo0O = I11 . http_GET ( url ) . content
  IIo0Oo0oO0oOO00 = open ( Oo00oo , "w" )
  IIo0Oo0oO0oOO00 . write ( ooo0O )
  IIo0Oo0oO0oOO00 . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( Oo00oo ) + '    ==='
  i1iIIi1 = xbmcgui . Dialog ( )
  i1iIIi1 . ok ( i11 , "                               Done Adding New .ini File" )
 return
 if 86 - 86: OoOO + oO0o0ooO0 / OoooooooOO - o0000oOoOoO0o
def o00O0 ( url , name ) :
 i1iIIi1 = xbmcgui . Dialog ( )
 if i1iIIi1 . yesno ( "GenieTv" , '                               Install Custom Settings' ) :
  print '###' + i11 + ' - CUSTOM FTV SETTINGS###'
  oOo00O0oo00o0 = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/script.ftvguide' , '' ) )
  Oo00oo = os . path . join ( oOo00O0oo00o0 , 'settings.xml' )
  ooo0O = I11 . http_GET ( url ) . content
  IIo0Oo0oO0oOO00 = open ( Oo00oo , "w" )
  IIo0Oo0oO0oOO00 . write ( ooo0O )
  IIo0Oo0oO0oOO00 . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( Oo00oo ) + '    ==='
  i1iIIi1 = xbmcgui . Dialog ( )
  i1iIIi1 . ok ( i11 , "                               Done Adding New Settings" )
 return
 if 40 - 40: Ooo00oOo00o . i11iIiiIii + ii11ii1ii + OOOo0 . OoOO
 if 90 - 90: O0oO . I1IiI * OoOoOO00 % o0oO0
def II1IiII1 ( ) :
 try :
  Ii1iI1IIIII = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/script.ftvguide' , '' ) )
  if os . path . exists ( Ii1iI1IIIII ) == True :
   i1iIIi1 = xbmcgui . Dialog ( )
   if i1iIIi1 . yesno ( "GenieTv" , "                               Delete FTV Guide Database" ) :
    Ooo0OOOo = os . path . join ( Ii1iI1IIIII , "source.db" )
    os . unlink ( Ooo0OOOo )
  i1iIIi1 . ok ( "GenieTv" , "                                     FTV Database Reset" )
 except :
  i1iIIi1 = xbmcgui . Dialog ( )
  i1iIIi1 . ok ( i11 , "               Error Deleting Database No Database To Delete" )
 return
 if 86 - 86: O0
 if 11 - 11: o00O0oo + oO0o0ooO0 * i1IIi % OoooooooOO * o00O0oo * Ooo00oOo00o
 if 7 - 7: oO0o0ooO0 . o00O0oo . oO0o0ooO0 - O0oO
 if 33 - 33: o0oO0 + OoooooooOO - Ooo00oOo00o / i1IIi / OoooooooOO
 if 82 - 82: ii11ii1ii / OoOO0ooOOoo0O - oO0o0ooO0 / Oo * Ooo00oOo00o
def oOoO0o00OO0 ( url ) :
 ooo0O0OOO000o = urllib2 . Request ( url )
 ooo0O0OOO000o . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
 iiI1iii = urllib2 . urlopen ( ooo0O0OOO000o )
 ooo0O = iiI1iii . read ( )
 iiI1iii . close ( )
 return ooo0O
 if 55 - 55: OoooooooOO
 if 73 - 73: I1IiI - ii11ii1ii % Oo + ii11ii1ii - O0 . Ooo00oOo00o
 if 38 - 38: O0
 if 79 - 79: i1IIi . OoOO
 if 34 - 34: O0oO * OoOoOO00
 if 71 - 71: IIII
 if 97 - 97: ii11ii1ii
def OOo0oO0o ( params ) :
 plugintools . log ( "freshstart.main_list " + repr ( params ) ) ; iI1iIO0oo0000o = plugintools . message_yes_no ( i11 , "Do you wish to restore your" , "Kodi configuration to default settings?" )
 if iI1iIO0oo0000o :
  OOoO0oooO = xbmcaddon . Addon ( id = oOOoo00O0O ) . getAddonInfo ( 'path' ) ; OOoO0oooO = xbmc . translatePath ( OOoO0oooO ) ;
  o00oo = os . path . join ( OOoO0oooO , ".." , ".." ) ; o00oo = os . path . abspath ( o00oo ) ; plugintools . log ( "freshstart.main_list xbmcPath=" + o00oo ) ; O000Oo00 = False
  try :
   for iiI11ii1I1 , Ooo0OOoOoO0 , oOo0OOoO0 in os . walk ( o00oo , topdown = True ) :
    Ooo0OOoOoO0 [ : ] = [ O0OooooO0o0O0 for O0OooooO0o0O0 in Ooo0OOoOoO0 if O0OooooO0o0O0 not in Oo0oO0ooo ]
    for oo00O00oO in oOo0OOoO0 :
     try : os . remove ( os . path . join ( iiI11ii1I1 , oo00O00oO ) )
     except :
      if oo00O00oO not in [ "Addons15.db" , "MyVideos75.db" , "Textures13.db" , "xbmc.log" ] : O000Oo00 = True
      plugintools . log ( "Error removing " + iiI11ii1I1 + " " + oo00O00oO )
    for oo00O00oO in Ooo0OOoOoO0 :
     try : os . rmdir ( os . path . join ( iiI11ii1I1 , oo00O00oO ) )
     except :
      if oo00O00oO not in [ "Database" , "userdata" ] : O000Oo00 = True
      plugintools . log ( "Error removing " + iiI11ii1I1 + " " + oo00O00oO )
   if not O000Oo00 : plugintools . log ( "freshstart.main_list All user files removed, you now have a clean install" ) ; plugintools . message ( i11 , "The process is complete, you're now back to a fresh Kodi configuration with GenieTv!" , "Please reboot your system or restart Kodi in order for the changes to be applied." )
   else : plugintools . log ( "freshstart.main_list User files partially removed" ) ; plugintools . message ( i11 , "The process is complete, you're now back to a fresh Kodi configuration with GenieTv" , "Please reboot your system or restart Kodi in order for the changes to be applied." )
  except : plugintools . message ( i11 , "Problem found" , "Your settings has not been changed" ) ; import traceback ; plugintools . log ( traceback . format_exc ( ) ) ; plugintools . log ( "freshstart.main_list NOT removed" )
  plugintools . add_item ( action = "" , title = "Now Exit Kodi" , folder = False )
 else : plugintools . message ( i11 , "Your settings" , "has not been changed" ) ; plugintools . add_item ( action = "" , title = "Done" , folder = False )
 oO00oooOOoOo0 ( )
 if 43 - 43: Ooo00oOo00o . o0oO0 * Oo
 if 20 - 20: i1IIi . i1IIi - o0000oOoOoO0o
 if 89 - 89: o0oO0 - o0000oOoOoO0o . O0 % OoooooooOO . i11iIiiIii
def IiII ( ) :
 iII1I = [ ]
 o00oOOo0Oo = sys . argv [ 2 ]
 if len ( o00oOOo0Oo ) >= 2 :
  Oooo0o0oO = sys . argv [ 2 ]
  o0OOoOooO0ooO = Oooo0o0oO . replace ( '?' , '' )
  if ( Oooo0o0oO [ len ( Oooo0o0oO ) - 1 ] == '/' ) :
   Oooo0o0oO = Oooo0o0oO [ 0 : len ( Oooo0o0oO ) - 2 ]
  IiiiIi = o0OOoOooO0ooO . split ( '&' )
  iII1I = { }
  for ii1Ii11IiiI1 in range ( len ( IiiiIi ) ) :
   IiI111 = { }
   IiI111 = IiiiIi [ ii1Ii11IiiI1 ] . split ( '=' )
   if ( len ( IiI111 ) ) == 2 :
    iII1I [ IiI111 [ 0 ] ] = IiI111 [ 1 ]
    if 82 - 82: OOOo0 % Ooo00oOo00o % o0000oOoOoO0o + o0000oOoOoO0o
 return iII1I
 if 6 - 6: Oo
Ii1I1i = base64 . decodestring ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20v' )
ii = base64 . decodestring ( 'L3N0b3JhZ2UvZW11bGF0ZWQvMA==' )
OOI1iI1ii1II = base64 . decodestring ( 'L2dlbmllLnR4dA==' )
O0OOOOoO00oo = base64 . decodestring ( 'LmFyY2hpdGVjdHMueDEwaG9zdC5jb20vdGVzdC93aC50eHQ=' )
i1I1ii = base64 . decodestring ( 'aHR0cDovL2ZpeGVzLmFyY2hpdGVjdHMueDEwaG9zdC5jb20vZml4ZXMudHh0' )
OoOiII11IiIi = base64 . decodestring ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vYXBwcy9hcHBzLnhtbA==' )
o0o00OOOO = base64 . decodestring ( 'L2FkZG9ucy9uZXcudHh0' )
iII1I1i = base64 . decodestring ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vdm9kL3ZvZC5waHA=' )
OooOO = base64 . decodestring ( 'L2FkZG9ucy9pcHR2LnR4dA==' )
OooO0ooO0o0 = base64 . decodestring ( 'L2FkZG9ucy92aWRlby50eHQ=' )
OoOoO00OOoOOOo0 = base64 . decodestring ( 'L2FkZG9ucy9zcG9ydHMudHh0' )
I1I1i1i = base64 . decodestring ( 'L2FkZG9ucy9raWRzLnR4dA==' )
I1Ii = base64 . decodestring ( 'L2FkZG9ucy9tdXNpYy50eHQ=' )
O0o0O00o0o = base64 . decodestring ( 'L2FkZG9ucy9wcm9ncmFtcy50eHQ=' )
OOo0oOOOOoo0 = base64 . decodestring ( 'L2FkZG9ucy94eHgudHh0' )
OOoO = base64 . decodestring ( 'L2FkZG9ucy9yZXBvLnR4dA==' )
i1Iii1i1I = base64 . decodestring ( 'L2FkZG9ucy9wYWNrcy50eHQ=' )
IIiii = base64 . decodestring ( 'L2FkZG9ucy9za2lucy50eHQ=' )
OOooo = base64 . decodestring ( 'L2FkZG9ucy9hcnQudHh0' )
oo0O0oO = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2dvdGhhbS50eHQ=' )
I11i1ii1 = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2hlbGl4LnR4dA==' )
O000oo = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2lzZW5nYXJkLnR4dA==' )
o0O0O = base64 . decodestring ( 'L2FkZG9ucy9SU1MudHh0' )
OOOoO000 = base64 . decodestring ( 'Q1VOVA==' )
def oOOo0oo ( name , url , mode , iconimage , fanart , description ) :
 OooOOOOoO00OoOO = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 oOooo0O0o = True
 Oo000 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 Oo000 . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 Oo000 . setProperty ( "Fanart_Image" , fanart )
 if mode == 5 :
  oOooo0O0o = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = OooOOOOoO00OoOO , listitem = Oo000 , isFolder = False )
 else :
  oOooo0O0o = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = OooOOOOoO00OoOO , listitem = Oo000 , isFolder = True )
 return oOooo0O0o
def iiII1i1 ( name , url , mode , iconimage , fanart , description ) :
 OooOOOOoO00OoOO = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 oOooo0O0o = True
 Oo000 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 Oo000 . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 Oo000 . setProperty ( "Fanart_Image" , fanart )
 oOooo0O0o = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = OooOOOOoO00OoOO , listitem = Oo000 , isFolder = False )
 return oOooo0O0o
 if 77 - 77: iIii1I11I1II1 * OoOO
 if 15 - 15: iIii1I11I1II1 . OoOO0ooOOoo0O . ii11ii1ii * i11iIiiIii
Oooo0o0oO = IiII ( )
oo000o = None
oo00O00oO = None
iiiI1I1iIIIi1 = None
iIiIIIi = None
ooo00OOOooO = None
O00OOOoOoo0O = None
if 72 - 72: o0000oOoOoO0o
if 26 - 26: IIII % Oo
try :
 oo000o = urllib . unquote_plus ( Oooo0o0oO [ "url" ] )
except :
 pass
try :
 oo00O00oO = urllib . unquote_plus ( Oooo0o0oO [ "name" ] )
except :
 pass
try :
 iIiIIIi = urllib . unquote_plus ( Oooo0o0oO [ "iconimage" ] )
except :
 pass
try :
 iiiI1I1iIIIi1 = int ( Oooo0o0oO [ "mode" ] )
except :
 pass
try :
 ooo00OOOooO = urllib . unquote_plus ( Oooo0o0oO [ "fanart" ] )
except :
 pass
try :
 O00OOOoOoo0O = urllib . unquote_plus ( Oooo0o0oO [ "description" ] )
except :
 pass
 if 72 - 72: O0 + OOooOOo + OOOo0 / Oo
 if 83 - 83: IIII - OOOo0 . o00O0oo
print str ( ooOoOoo0O ) + ': ' + str ( O0OoO000O0OO )
print "Mode: " + str ( iiiI1I1iIIIi1 )
print "URL: " + str ( oo000o )
print "Name: " + str ( oo00O00oO )
print "IconImage: " + str ( iIiIIIi )
if 34 - 34: I1IiI - OoOO * OoooooooOO
if 5 - 5: i11iIiiIii * oO0o0ooO0 - o00O0oo - ii11ii1ii - i1IIi + oO0o0ooO0
def I11II1i ( content , viewType ) :
 if 4 - 4: o0oO0 + O0 . i1IIi * ii11ii1ii - OOooOOo
 if content :
  xbmcplugin . setContent ( int ( sys . argv [ 1 ] ) , content )
 if o0oOoO00o . getSetting ( 'auto-view' ) == 'true' :
  xbmc . executebuiltin ( "Container.SetViewMode(%s)" % o0oOoO00o . getSetting ( viewType ) )
  if 42 - 42: OOooOOo * I1IiI . Ooo00oOo00o - oO0o0ooO0 / OoOoOO00
  if 25 - 25: Oo % I1IiI
if iiiI1I1iIIIi1 == None :
 OO0o00o ( )
 if 75 - 75: i1IIi
elif iiiI1I1iIIIi1 == 1 :
 iI11iI1IiiIiI ( oo000o )
 if 74 - 74: Oo + O0oO - OoOO - Ooo00oOo00o + oO0o0ooO0 - iIii1I11I1II1
elif iiiI1I1iIIIi1 == 44 :
 IiI1i ( oo000o )
 if 54 - 54: ii11ii1ii + OoOoOO00 . OOOo0 / Ooo00oOo00o . o0oO0
elif iiiI1I1iIIIi1 == 2 :
 O000OOOOOo ( )
 if 58 - 58: IIII % i11iIiiIii * OoOoOO00 . ii11ii1ii
elif iiiI1I1iIIIi1 == 3 :
 oOOOOo0 ( )
 if 94 - 94: i11iIiiIii . OoOO0ooOOoo0O + iIii1I11I1II1 * O0oO * O0oO
elif iiiI1I1iIIIi1 == 21 :
 o0ooO ( )
 if 36 - 36: o0000oOoOoO0o - IIII . IIII
elif iiiI1I1iIIIi1 == 4 :
 I1111I1iII11 ( )
 if 60 - 60: i11iIiiIii * Oo % Ooo00oOo00o + Ooo00oOo00o
elif iiiI1I1iIIIi1 == 5 :
 O0oOOO0ooOOO0OOO ( oo00O00oO , oo000o , O00OOOoOoo0O )
 if 84 - 84: iIii1I11I1II1 + OoooooooOO
elif iiiI1I1iIIIi1 == 6 :
 I1I11i ( oo000o )
 if 77 - 77: O0 * ii11ii1ii * OoOO + Ooo00oOo00o + ii11ii1ii - O0oO
elif iiiI1I1iIIIi1 == 7 :
 iI1iiiiiii ( oo000o , oo00O00oO )
 if 10 - 10: ii11ii1ii + IIII
elif iiiI1I1iIIIi1 == 8 :
 IiI ( oo000o , oo00O00oO )
 if 58 - 58: OOOo0 + OoooooooOO / oO0o0ooO0 . o0oO0 % OOooOOo / ii11ii1ii
elif iiiI1I1iIIIi1 == 9 :
 FIXREPOSADDONS ( oo000o )
 if 62 - 62: OoOoOO00
elif iiiI1I1iIIIi1 == 10 :
 O0O00Oo ( )
 if 12 - 12: IIII + OoOoOO00
elif iiiI1I1iIIIi1 == 11 :
 OOOoo0O00Oooo ( oo000o )
 if 92 - 92: O0oO % iIii1I11I1II1 - oO0o0ooO0 / i11iIiiIii % o0oO0 * OOooOOo
elif iiiI1I1iIIIi1 == 12 :
 i1iIi ( )
 if 80 - 80: oO0o0ooO0
elif iiiI1I1iIIIi1 == 13 :
 o00OO0o0 ( )
 if 3 - 3: ii11ii1ii * o0000oOoOoO0o
elif iiiI1I1iIIIi1 == 14 :
 iI1iIIIIIiIi1 ( oo000o )
 if 53 - 53: iIii1I11I1II1 / oO0o0ooO0 % Ooo00oOo00o + IIII / o0oO0
elif iiiI1I1iIIIi1 == 15 :
 i11I1iIiII ( )
 if 74 - 74: Oo
elif iiiI1I1iIIIi1 == 16 :
 iIiiI111I11 ( oo000o , oo00O00oO )
 if 8 - 8: OOOo0 % OoOoOO00 - OOooOOo - o0000oOoOoO0o % OOOo0
elif iiiI1I1iIIIi1 == 17 :
 o00O0 ( oo000o , oo00O00oO )
 if 93 - 93: o00O0oo * oO0o0ooO0 / OoOO0ooOOoo0O
elif iiiI1I1iIIIi1 == 18 :
 II1IiII1 ( )
 if 88 - 88: OoOO
elif iiiI1I1iIIIi1 == 19 :
 oo0oO0oOOoo ( oo00O00oO , oo000o , O00OOOoOoo0O )
 if 1 - 1: Oo
elif iiiI1I1iIIIi1 == 40 :
 I1I1i1I ( oo00O00oO , oo000o , O00OOOoOoo0O )
 if 95 - 95: OoooooooOO / o0000oOoOoO0o % OoooooooOO / o0oO0 * IIII
elif iiiI1I1iIIIi1 == 42 :
 Oooo0oOO ( oo00O00oO , oo000o , O00OOOoOoo0O )
 if 75 - 75: O0
elif iiiI1I1iIIIi1 == 43 :
 oooOo0OOOoo0 ( oo00O00oO , oo000o , O00OOOoOoo0O )
 if 56 - 56: Ooo00oOo00o / OoOoOO00
elif iiiI1I1iIIIi1 == 20 :
 iiIii ( oo000o )
 if 39 - 39: I1IiI - OoooooooOO - i1IIi / OoOoOO00
elif iiiI1I1iIIIi1 == 22 :
 O0OOoOooO00 ( oo000o )
 if 49 - 49: Oo + O0 + IIII . OoOoOO00 % o0oO0
elif iiiI1I1iIIIi1 == 23 :
 i1iIIiI1111 ( oo000o )
 if 33 - 33: I1IiI . iIii1I11I1II1 / o0000oOoOoO0o % o00O0oo
elif iiiI1I1iIIIi1 == 24 :
 iii1IiI1i ( oo000o )
 if 49 - 49: Ooo00oOo00o + OoOoOO00 / IIII - O0 % o00O0oo
elif iiiI1I1iIIIi1 == 25 :
 ii1OO0 ( oo000o )
 if 27 - 27: Ooo00oOo00o + Oo
elif iiiI1I1iIIIi1 == 26 :
 O0o00 ( oo000o )
 if 92 - 92: OOOo0 % oO0o0ooO0
elif iiiI1I1iIIIi1 == 27 :
 O000OO ( oo000o )
 if 31 - 31: OoooooooOO - OoOO / O0oO
elif iiiI1I1iIIIi1 == 28 :
 i11i ( oo000o )
 if 62 - 62: i11iIiiIii - o0000oOoOoO0o
elif iiiI1I1iIIIi1 == 29 :
 II11IiIIiiI ( oo000o )
 if 81 - 81: o0000oOoOoO0o
elif iiiI1I1iIIIi1 == 30 :
 IIi ( oo000o )
 if 92 - 92: OoOO0ooOOoo0O - Oo - OoooooooOO / IIII - i1IIi
elif iiiI1I1iIIIi1 == 31 :
 OOO00o0 ( oo000o )
 if 81 - 81: i1IIi / O0oO % i11iIiiIii . iIii1I11I1II1 * I1IiI + OoooooooOO
elif iiiI1I1iIIIi1 == 32 :
 o0oo ( )
 if 31 - 31: i1IIi % OoOoOO00
elif iiiI1I1iIIIi1 == 33 :
 Oo0oO ( )
 if 13 - 13: iIii1I11I1II1 - OoOoOO00 % O0 . o00O0oo % Ooo00oOo00o
elif iiiI1I1iIIIi1 == 35 :
 O0OooOo0o ( oo000o )
 if 2 - 2: OoooooooOO - o00O0oo % OoOO / OOOo0 / OOooOOo
elif iiiI1I1iIIIi1 == 34 :
 ii11IIII11I ( oo000o )
 if 3 - 3: OoOoOO00 / OoOO0ooOOoo0O
elif iiiI1I1iIIIi1 == 36 :
 OooOOOOo ( oo000o )
 if 48 - 48: o0oO0 . ii11ii1ii
elif iiiI1I1iIIIi1 == 37 :
 iii1i ( oo000o )
 if 49 - 49: i1IIi - I1IiI . Oo + iIii1I11I1II1 - o0oO0 / Oo
elif iiiI1I1iIIIi1 == 38 :
 Oo0oOOOoOooOo ( oo000o )
 if 24 - 24: OoOO - oO0o0ooO0 / o0oO0
elif iiiI1I1iIIIi1 == 41 :
 OOo0oO0o ( Oooo0o0oO )
 if 10 - 10: I1IiI * i1IIi
elif iiiI1I1iIIIi1 == 39 :
 i1i1IIII ( oo000o )
 if 15 - 15: o0000oOoOoO0o + i1IIi - OoOoOO00 % OOOo0
elif iiiI1I1iIIIi1 == 45 :
 TEXTS ( )
 if 34 - 34: OOOo0
elif iiiI1I1iIIIi1 == 46 :
 O00Oo ( )
 if 57 - 57: OoOO0ooOOoo0O . o00O0oo % OOooOOo
elif iiiI1I1iIIIi1 == 47 :
 GEVID ( )
 if 32 - 32: o0000oOoOoO0o / IIII - O0 * iIii1I11I1II1
elif iiiI1I1iIIIi1 == 48 :
 O0O ( oo00O00oO , oo000o , O00OOOoOoo0O )
 if 70 - 70: OoooooooOO % OoooooooOO % Ooo00oOo00o
elif iiiI1I1iIIIi1 == 49 :
 OOo0o ( )
 if 98 - 98: Ooo00oOo00o
elif iiiI1I1iIIIi1 == 222 :
 oOoooO000O ( oo000o )
 if 18 - 18: o0000oOoOoO0o + Oo - Ooo00oOo00o / O0oO / OoOO0ooOOoo0O
elif iiiI1I1iIIIi1 == 333 :
 oOooOOo00ooO ( oo000o )
 if 53 - 53: OoOO0ooOOoo0O + OOooOOo . OoOO / o0000oOoOoO0o
 if 52 - 52: O0oO + O0oO
elif iiiI1I1iIIIi1 == 1001 :
 IIiiI ( )
 if 73 - 73: OOooOOo . i11iIiiIii % OoooooooOO + o0oO0 . OoooooooOO / OoOO0ooOOoo0O
elif iiiI1I1iIIIi1 == 1005 :
 OOoOO0O0o0 ( )
 if 54 - 54: I1IiI . OoooooooOO
elif iiiI1I1iIIIi1 == 1007 :
 I1II1oOOoo ( oo000o )
 if 36 - 36: OoOO / OoOoOO00 * IIII % ii11ii1ii
elif iiiI1I1iIIIi1 == 1010 :
 i1II11IiiiI ( oo000o )
 if 31 - 31: OoOoOO00 + OoOO0ooOOoo0O - OoooooooOO . o0000oOoOoO0o
elif iiiI1I1iIIIi1 == 1011 :
 IIIi ( oo000o )
 if 28 - 28: o00O0oo . ii11ii1ii
elif iiiI1I1iIIIi1 == 1030 :
 o0ooOOoO0oO0 ( )
 if 77 - 77: ii11ii1ii % OoOoOO00
elif iiiI1I1iIIIi1 == 1031 :
 oo00I1IiI1IIiI ( oo000o , iIiIIIi )
 if 81 - 81: I1IiI % o00O0oo / O0 * iIii1I11I1II1 % IIII . OOOo0
elif iiiI1I1iIIIi1 == 1006 :
 Parse . ParseURL ( oo000o )
 if 90 - 90: OOooOOo
elif iiiI1I1iIIIi1 == 2030 :
 Parse . addonParseURL ( oo000o )
 if 44 - 44: OOooOOo / ii11ii1ii . Oo + I1IiI
elif iiiI1I1iIIIi1 == 2031 :
 Parse . apkParseURL ( oo000o )
 if 32 - 32: IIII - o0oO0 * oO0o0ooO0 * o0000oOoOoO0o
elif iiiI1I1iIIIi1 == 1002 :
 O000oo00OOOOO ( oo000o )
 if 84 - 84: o00O0oo + ii11ii1ii % OOOo0 + i11iIiiIii
elif iiiI1I1iIIIi1 == 1003 :
 OOo ( oo000o , iIiIIIi )
 if 37 - 37: o0000oOoOoO0o % ii11ii1ii / o0oO0
elif iiiI1I1iIIIi1 == 1004 :
 o000O0oo ( oo000o )
 if 94 - 94: o0000oOoOoO0o / Ooo00oOo00o . OOooOOo
elif iiiI1I1iIIIi1 == 1008 :
 oOOooi1I1iIii11 ( )
 if 1 - 1: Oo . OoOoOO00
elif iiiI1I1iIIIi1 == 1009 :
 M3UPLAY ( oo000o )
 if 93 - 93: OoOoOO00 . i11iIiiIii + OoOoOO00 % OoOO
elif iiiI1I1iIIIi1 == 2001 :
 oo0OO0OOOOOo0 ( oo000o )
 if 98 - 98: O0oO * OoOO * I1IiI + o00O0oo * oO0o0ooO0
elif iiiI1I1iIIIi1 == 1013 :
 II1i111Ii1i ( )
 if 4 - 4: IIII
elif iiiI1I1iIIIi1 == 1014 :
 o0oOO00 ( )
 if 16 - 16: iIii1I11I1II1 * oO0o0ooO0 + OoOO . O0 . OOooOOo
elif iiiI1I1iIIIi1 == 1015 :
 ii11iiIi ( oo000o )
 if 99 - 99: i11iIiiIii - oO0o0ooO0
elif iiiI1I1iIIIi1 == 1016 :
 OOOO0Oo ( oo000o )
 if 85 - 85: O0oO % ii11ii1ii
elif iiiI1I1iIIIi1 == 1023 :
 iIIIIii1 ( )
 if 95 - 95: Ooo00oOo00o * OoOO0ooOOoo0O * oO0o0ooO0 . OOooOOo
elif iiiI1I1iIIIi1 == 1024 :
 Ooo000O00 ( )
 if 73 - 73: Ooo00oOo00o
elif iiiI1I1iIIIi1 == 1025 :
 i1iI1Iiii1I ( oo000o )
 if 28 - 28: OoooooooOO - o0000oOoOoO0o
elif iiiI1I1iIIIi1 == 4001 :
 iiI1 ( )
 if 84 - 84: OoOoOO00
elif iiiI1I1iIIIi1 == 4002 :
 i11Iiii ( )
 if 36 - 36: OoOO0ooOOoo0O - I1IiI - iIii1I11I1II1
elif iiiI1I1iIIIi1 == 4003 :
 iI1ii1Ii ( )
 if 10 - 10: ii11ii1ii / o00O0oo * i1IIi % O0 + o0000oOoOoO0o
elif iiiI1I1iIIIi1 == 3000 :
 I11II1 ( )
 if 25 - 25: O0oO - o00O0oo / O0 . OoooooooOO % OOOo0 . i1IIi
elif iiiI1I1iIIIi1 == 404 :
 II1OoooOo ( oo00O00oO , oo000o , iIiIIIi )
 if 19 - 19: OoOoOO00 / OoOoOO00 % ii11ii1ii + OoOO + OoOO + oO0o0ooO0
elif iiiI1I1iIIIi1 == 7030 :
 i11Iii1Ii1i1 ( )
 if 4 - 4: OOooOOo + o0000oOoOoO0o / oO0o0ooO0 + i1IIi % OOooOOo % oO0o0ooO0
elif iiiI1I1iIIIi1 == 7021 :
 Oo00O0OO ( oo00O00oO )
 if 80 - 80: o00O0oo
elif iiiI1I1iIIIi1 == 7022 :
 o0o ( oo00O00oO )
 if 26 - 26: iIii1I11I1II1 . OoooooooOO - iIii1I11I1II1
elif iiiI1I1iIIIi1 == 7000 :
 OOOO ( oo00O00oO , oo000o , img )
 if 59 - 59: ii11ii1ii + o0000oOoOoO0o . OoOO
elif iiiI1I1iIIIi1 == 7050 :
 I1iI1IiI ( )
 if 87 - 87: Ooo00oOo00o
elif iiiI1I1iIIIi1 == 7051 :
 oOo0Oo0O0O ( oo000o )
 if 34 - 34: O0oO . I1IiI / i11iIiiIii / oO0o0ooO0
elif iiiI1I1iIIIi1 == 7060 :
 O0o00oO0oOO ( )
 if 46 - 46: Oo + OoOoOO00 * OOOo0 + OoOO0ooOOoo0O
elif iiiI1I1iIIIi1 == 7061 :
 iii ( oo000o )
 if 31 - 31: o00O0oo * OOooOOo * o00O0oo + Ooo00oOo00o * OOooOOo . O0oO
elif iiiI1I1iIIIi1 == 7063 :
 iiiii1I1III1 ( oo000o )
 if 89 - 89: OoooooooOO * o00O0oo * OOOo0 . o0oO0 * o00O0oo / oO0o0ooO0
elif iiiI1I1iIIIi1 == 7062 :
 Oo0oOo000OoO0 ( oo000o )
 if 46 - 46: i11iIiiIii
elif iiiI1I1iIIIi1 == 7064 :
 NATatozcat ( )
 if 15 - 15: O0 / i1IIi / i1IIi . oO0o0ooO0 % I1IiI + OOOo0
elif iiiI1I1iIIIi1 == 7067 :
 OoOoO0oOOooo ( oo000o )
 if 48 - 48: O0oO % oO0o0ooO0 % o00O0oo % iIii1I11I1II1 . o00O0oo
elif iiiI1I1iIIIi1 == 7066 :
 NATatozA ( oo000o )
 if 14 - 14: oO0o0ooO0 * Ooo00oOo00o % O0 + o0000oOoOoO0o + ii11ii1ii
elif iiiI1I1iIIIi1 == 7065 :
 oo0 ( oo000o )
 if 23 - 23: Oo % oO0o0ooO0 + o00O0oo - O0oO
elif iiiI1I1iIIIi1 == 7070 :
 iiiiI1IiI1I1 ( )
 if 65 - 65: OoooooooOO
elif iiiI1I1iIIIi1 == 7071 :
 DIZIlist ( oo000o )
 if 22 - 22: OoOO0ooOOoo0O + OoOoOO00 + Oo
elif iiiI1I1iIIIi1 == 7072 :
 DIZIpull ( oo000o )
 if 83 - 83: o0oO0
elif iiiI1I1iIIIi1 == 7073 :
 WATCHDIZI ( oo000o )
 if 43 - 43: OoOO0ooOOoo0O
elif iiiI1I1iIIIi1 == 7002 :
 oOOoOooO0oO0o ( )
 if 84 - 84: OoOO0ooOOoo0O . IIII . oO0o0ooO0
elif iiiI1I1iIIIi1 == 7003 :
 ii1IIiII111I ( oo000o )
 if 2 - 2: Oo - I1IiI
elif iiiI1I1iIIIi1 == 7004 :
 II1io0 ( oo000o )
 if 49 - 49: o00O0oo + OoOoOO00 / OoOO - I1IiI % I1IiI + OOOo0
elif iiiI1I1iIIIi1 == 7020 :
 iiI ( oo000o )
 if 54 - 54: o0oO0 % Oo - OoOO0ooOOoo0O
elif iiiI1I1iIIIi1 == 7001 :
 oo0OoOO0o0o ( )
 if 16 - 16: ii11ii1ii * oO0o0ooO0 / o0000oOoOoO0o
elif iiiI1I1iIIIi1 == 7010 :
 iIiiIIIiI1Ii ( oo000o )
 if 46 - 46: OoOoOO00
elif iiiI1I1iIIIi1 == 7011 :
 IiIi ( oo000o )
 if 13 - 13: IIII + OoOoOO00 % OOOo0
elif iiiI1I1iIIIi1 == 7012 :
 o0oo0O0oOoooO ( oo000o )
 if 30 - 30: OoooooooOO - i11iIiiIii + OoOO / Oo - i11iIiiIii
elif iiiI1I1iIIIi1 == 7013 :
 cnfTVPlay2 ( oo000o )
elif iiiI1I1iIIIi1 == 7014 :
 CNF_Studio_Indexer . MV_Movies ( oo000o )
elif iiiI1I1iIIIi1 == 7015 :
 CNF_Studio_Indexer . Movie_ByYear ( oo000o )
elif iiiI1I1iIIIi1 == 7016 :
 CNF_Studio_Indexer . Resolve_CNF_Link ( oo00O00oO , oo000o , iIiIIIi )
elif iiiI1I1iIIIi1 == 7017 :
 CNF_Studio_Indexer . Search_Movie ( )
elif iiiI1I1iIIIi1 == 7018 :
 I111I1I ( )
elif iiiI1I1iIIIi1 == 7019 :
 CNF_Studio_Indexer . List_Movies ( oo000o )
elif iiiI1I1iIIIi1 == 7020 :
 CNF_Studio_Indexer . Get_Movie_Page ( oo000o )
elif iiiI1I1iIIIi1 == 7024 :
 CNF_Studio_Indexer . Box_Office ( oo000o )
 if 74 - 74: O0 . o0000oOoOoO0o
elif iiiI1I1iIIIi1 == 8000 :
 i1I1III1i1i ( )
elif iiiI1I1iIIIi1 == 8001 :
 iIiIi1Ii11IiI1I1 ( )
elif iiiI1I1iIIIi1 == 8002 :
 oOOoo0 ( )
elif iiiI1I1iIIIi1 == 8003 :
 oOo00o ( )
elif iiiI1I1iIIIi1 == 8004 :
 I11o0000o0Oo ( )
elif iiiI1I1iIIIi1 == 8005 :
 oooO00Oo ( )
elif iiiI1I1iIIIi1 == 8006 :
 I11i11I ( oo00O00oO , oo000o )
elif iiiI1I1iIIIi1 == 8030 :
 III1IiiI ( oo000o )
elif iiiI1I1iIIIi1 == 8045 :
 o00oo0 ( )
elif iiiI1I1iIIIi1 == 8046 :
 Oo0oOooOoOo ( oo000o )
elif iiiI1I1iIIIi1 == 8047 :
 ooOo0O0o0 ( oo000o )
elif iiiI1I1iIIIi1 == 8040 :
 IiII1iiI ( )
elif iiiI1I1iIIIi1 == 8041 :
 iII ( oo000o )
elif iiiI1I1iIIIi1 == 8042 :
 Ooo0 ( oo000o )
elif iiiI1I1iIIIi1 == 8043 :
 yt . PlayVideo ( oo000o )
elif iiiI1I1iIIIi1 == 8044 :
 o0o00oO0oo000 ( oo000o )
elif iiiI1I1iIIIi1 == 8060 :
 oOo0OOoooO ( )
elif iiiI1I1iIIIi1 == 8061 :
 OooOo000o0o ( oo000o )
elif iiiI1I1iIIIi1 == 8070 :
 OOO0 ( )
elif iiiI1I1iIIIi1 == 8071 :
 iIiIIi ( oo000o )
elif iiiI1I1iIIIi1 == 7080 :
 III1I ( oo000o )
elif iiiI1I1iIIIi1 == 8090 :
 OoOOOO ( )
elif iiiI1I1iIIIi1 == 8091 :
 I1iiIi111I ( oo000o )
elif iiiI1I1iIIIi1 == 8092 :
 Iiii1iIii ( oo000o )
elif iiiI1I1iIIIi1 == 8081 :
 iii1IiI1I1 ( )
elif iiiI1I1iIIIi1 == 8062 :
 O0oo0O0 ( oo000o )
elif iiiI1I1iIIIi1 == 8063 :
 iiIiII11i1 ( oo000o )
elif iiiI1I1iIIIi1 == 8050 :
 ooO ( )
elif iiiI1I1iIIIi1 == 8051 :
 Ooo0oOooo0 ( oo000o )
elif iiiI1I1iIIIi1 == 8052 :
 iiI1IIIi ( oo000o )
elif iiiI1I1iIIIi1 == 8085 :
 III1I1I ( )
elif iiiI1I1iIIIi1 == 8086 :
 O0OO0o0OO0OO ( oo000o )
elif iiiI1I1iIIIi1 == 8087 :
 iIIIiIi1I1i ( oo000o )
elif iiiI1I1iIIIi1 == 8088 :
 OoOOoO0oOo ( oo000o , oo00O00oO )
elif iiiI1I1iIIIi1 == 9000 :
 oO000Oo000 ( )
elif iiiI1I1iIIIi1 == 1111 :
 O0oo0 ( )
elif iiiI1I1iIIIi1 == 9001 :
 o000o0O0Oo00 ( )
elif iiiI1I1iIIIi1 == 9002 :
 iiiiii1 ( )
elif iiiI1I1iIIIi1 == 9003 :
 iIiiIi11IIi ( )
elif iiiI1I1iIIIi1 == 50 :
 I1i ( oo000o )
elif iiiI1I1iIIIi1 == 9020 :
 OO00Oo ( )
elif iiiI1I1iIIIi1 == 9021 :
 oOOO0 ( )
elif iiiI1I1iIIIi1 == 9022 :
 i111I11i1I ( )
elif iiiI1I1iIIIi1 == 9023 :
 O00oOo0O0o00O ( )
elif iiiI1I1iIIIi1 == 9024 :
 II11Ii111II1 ( oo000o )
elif iiiI1I1iIIIi1 == 9030 :
 oO0ooooo0O00 ( oo000o )
elif iiiI1I1iIIIi1 == 9031 :
 iII11ii1ii ( oo000o )
elif iiiI1I1iIIIi1 == 9032 :
 oOO0OOOo000o ( oo000o )
elif iiiI1I1iIIIi1 == 9033 :
 OO00oo ( oo000o )
elif iiiI1I1iIIIi1 == 7085 :
 oo000oOO00o0oOO ( oo000o )
elif iiiI1I1iIIIi1 == 7086 :
 oO0O0o0o00 ( oo000o )
elif iiiI1I1iIIIi1 == 7087 :
 I111iiiii1 ( O00OOOoOoo0O )
elif iiiI1I1iIIIi1 == 10000 : Ii11Ii1I ( )
elif iiiI1I1iIIIi1 == 10001 : o0O0OOOOoOO0 ( )
elif iiiI1I1iIIIi1 == 10002 : iIIi1iiI1i11 ( )
elif iiiI1I1iIIIi1 == 10003 : OooO0oo ( )
elif iiiI1I1iIIIi1 == 10004 : O0OoooO0 ( )
elif iiiI1I1iIIIi1 == 10005 : o0ooooO0o0O ( )
elif iiiI1I1iIIIi1 == 10006 : iI1i11II1i ( oo000o )
elif iiiI1I1iIIIi1 == 10007 : I11I1i1iIII1I ( oo000o , iIiIIIi )
elif iiiI1I1iIIIi1 == 10008 : II1 ( )
elif iiiI1I1iIIIi1 == 10009 : iiIIii ( )
elif iiiI1I1iIIIi1 == 10010 : IIiooOoO0OO0oOO ( oo000o )
elif iiiI1I1iIIIi1 == 10011 : oO00oOOo0Oo ( oo000o )
elif iiiI1I1iIIIi1 == 10012 : II11iIIiiiII ( oo000o )
elif iiiI1I1iIIIi1 == 10013 : ooO0oo ( oo000o )
elif iiiI1I1iIIIi1 == 10014 : I1i111iiIIIi ( )
elif iiiI1I1iIIIi1 == 10015 : I1ii11Ii ( )
elif iiiI1I1iIIIi1 == 10016 : IiIi1iIIi1 ( oo000o )
elif iiiI1I1iIIIi1 == 10017 : IIIiI11ii1I ( )
elif iiiI1I1iIIIi1 == 10018 : ii1Ii1IiIIi ( )
elif iiiI1I1iIIIi1 == 10019 : OOOo ( )
elif iiiI1I1iIIIi1 == 10020 : o0 ( )
elif iiiI1I1iIIIi1 == 10021 : OOO0oOoO0O ( )
elif iiiI1I1iIIIi1 == 10022 : oOO ( oo000o )
elif iiiI1I1iIIIi1 == 10023 : OOO0oOOo00O ( oo00O00oO , oo000o )
elif iiiI1I1iIIIi1 == 10024 : I1iOOOO ( oo000o )
elif iiiI1I1iIIIi1 == 10025 : OoO ( )
elif iiiI1I1iIIIi1 == 10026 : i1iiIiI1Ii1i ( )
elif iiiI1I1iIIIi1 == 10027 : oOOoo ( )
elif iiiI1I1iIIIi1 == 10028 : Ii1i1i1i1I1Ii ( )
elif iiiI1I1iIIIi1 == 10029 : I1II ( )
elif iiiI1I1iIIIi1 == 423 : I111IiiIi1 ( oo000o )
elif iiiI1I1iIIIi1 == 426 : o0O0Oo00 ( oo000o )
elif iiiI1I1iIIIi1 == 10030 : I1i1i1 ( )
elif iiiI1I1iIIIi1 == 10031 : Latest_Izle_Movies ( )
elif iiiI1I1iIIIi1 == 10032 : IIIi11I11 ( )
elif iiiI1I1iIIIi1 == 10033 : OOOO0O00o ( )
elif iiiI1I1iIIIi1 == 10034 : oOoO0 ( )
elif iiiI1I1iIIIi1 == 10035 : Ii1i1iI ( )
elif iiiI1I1iIIIi1 == 10036 : OOOO0OOO ( oo000o )
elif iiiI1I1iIIIi1 == 10037 : I1i11111i1i11 ( oo000o )
elif iiiI1I1iIIIi1 == 10038 : iII1ii1 ( )
elif iiiI1I1iIIIi1 == 10039 : Oo00o0OO0O00o ( oo000o )
elif iiiI1I1iIIIi1 == 10040 : Ii1i1i1111 ( )
elif iiiI1I1iIIIi1 == 10041 : ii1I11iIiIII1 ( oo000o )
elif iiiI1I1iIIIi1 == 10042 : oOo00oOOOOO ( oo000o )
elif iiiI1I1iIIIi1 == 10043 : iiii1I1 ( )
elif iiiI1I1iIIIi1 == 10044 : Ii1 ( oo000o )
elif iiiI1I1iIIIi1 == 10045 : Oo0OooO0 ( oo000o )
elif iiiI1I1iIIIi1 == 10046 : iIiI ( oo000o )
elif iiiI1I1iIIIi1 == 10047 : OO0O0o0o0 ( oo000o )
elif iiiI1I1iIIIi1 == 10048 : iIIiI1I1i ( oo000o )
elif iiiI1I1iIIIi1 == 10049 : IIIIIii1ii11 ( oo000o )
xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
