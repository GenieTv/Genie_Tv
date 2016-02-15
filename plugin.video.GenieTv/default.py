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
i1iiIII111ii = xbmcgui . Dialog ( )
i1iIIi1 = xbmc . translatePath ( 'special://home/' )
ii11iIi1I = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + o00 , 'fanart.jpg' ) )
iI111I11I1I1 = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + o00 , 'icon.png' , ii11iIi1I , '' ) )
OOooO0OOoo = ( oOo0oooo00o ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vR2VuaWVBcnQv' ) )
iIii1 = ( oOo0oooo00o ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vR2VuaWVBcnQvb3JpZ2luLnBuZw==' ) )
oOOoO0 = "2.3.6"
O0OoO000O0OO = xbmc . translatePath ( 'special://database' )
iiI1IiI = xbmc . translatePath ( 'special://thumbnails' ) ;
II = "GenieTv"
ooOoOoo0O = ( oOo0oooo00o ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20=' ) )
OooO0 = 'http://'
II11iiii1Ii = o0oOoO00o . getLocalizedString
OO0o = CookieJar ( )
Ooo = urllib2 . build_opener ( urllib2 . HTTPCookieProcessor ( OO0o ) )
Ooo . addheaders = [ ( 'User-Agent' , 'Mozilla/5.0' ) ]
O0o0Oo = int ( sys . argv [ 1 ] )
if 78 - 78: iIii1I11I1II1 - o00O0oo * Ooo00oOo00o + OOooOOo + oO0o0ooO0 + oO0o0ooO0
def I11I11i1I ( ) :
 ii11i1iIII ( '[COLORgreen]WIZARD[/COLOR]' , ooOoOoo0O , 4001 , OOooO0OOoo + 'MB.png' , ii11iIi1I , '' )
 ii11i1iIII ( '[COLORgreen]STREAMS[/COLOR]' , ooOoOoo0O , 4002 , OOooO0OOoo + 'streams.png' , ii11iIi1I , '' )
 ii11i1iIII ( '[COLORgreen]MUSIC[/COLOR]' , ooOoOoo0O , 4003 , OOooO0OOoo + 'MUSIC.png' , ii11iIi1I , '' )
 if 3 - 3: i1IIi / OOOo0 % o0000oOoOoO0o * i11iIiiIii / O0 * o0000oOoOoO0o
 ii11i1iIII ( '[COLORgreen]BUILDERS TOOLBOX[/COLOR]' , ooOoOoo0O , 32 , OOooO0OOoo + 'builderstoolbox.png' , ii11iIi1I , '' )
 ii11i1iIII ( '[COLORgreen]SOURCE LIST[/COLOR]' , ooOoOoo0O , 46 , OOooO0OOoo + 'sources.png' , ii11iIi1I , '' )
 ii11i1iIII ( '[COLORgreen]MAINTENANCE[/COLOR]' , ooOoOoo0O , 3 , OOooO0OOoo + 'MAIN6.png' , ii11iIi1I , '' )
 ii11i1iIII ( '[COLORgreen]ADDONS[/COLOR]' , ( oOo0oooo00o ( 'aHR0cDovL21pcnJvcnMua29kaS50di9hZGRvbnMv' ) ) , 2030 , OOooO0OOoo + 'ADDONS.png' , ii11iIi1I , '' )
 ii11i1iIII ( '[COLORgreen]APK TOOL[/COLOR]' , ooOoOoo0O , 2 , OOooO0OOoo + 'APK.png' , ii11iIi1I , '' )
 ii11i1iIII ( '[COLORgreen]GenieTv RSS Feed[/COLOR]' , ooOoOoo0O , 39 , OOooO0OOoo + 'RSS.png' , ii11iIi1I , '' )
 ii11i1iIII ( '[COLORgreen]ADDONS PACKS[/COLOR]' , ooOoOoo0O , 30 , OOooO0OOoo + 'ADDONP.png' , ii11iIi1I , '' )
 III1ii1iII ( 'movies' , 'MAIN' )
 if 54 - 54: OOOo0 % OoOoOO00 % OoOoOO00
def iI1 ( ) :
 ii11i1iIII ( '[COLORgreen]RESTORE MY BUILD[/COLOR]' , ooOoOoo0O , 49 , OOooO0OOoo + 'MB.png' , ii11iIi1I , '' )
 ii11i1iIII ( '[COLORgreen]WIPE GENIE[/COLOR]' , ooOoOoo0O , 41 , OOooO0OOoo + 'wipegenie.png' , ii11iIi1I , '' )
 ii11i1iIII ( '[COLORgreen]WISHES PC[/COLOR]' , ooOoOoo0O , 1 , OOooO0OOoo + 'WISHESPC.png' , ii11iIi1I , '' )
 ii11i1iIII ( '[COLORgreen]WISHES ANDROID[/COLOR]' , ooOoOoo0O , 44 , OOooO0OOoo + 'WISHESAN.png' , ii11iIi1I , '' )
 III1ii1iII ( 'movies' , 'MAIN' )
def i11Iiii ( ) :
 ii11i1iIII ( '[COLORgreen]SEARCH[/COLOR]' , ooOoOoo0O , 9000 , OOooO0OOoo + 'search.png' , ii11iIi1I , '' )
 ii11i1iIII ( '[COLORgreen]M3U STREAMS[/COLOR]' , ooOoOoo0O , 8070 , OOooO0OOoo + 'streams.png' , ii11iIi1I , '' )
 ii11i1iIII ( '[COLORgreen]GenieTv VOD[/COLOR]' , ooOoOoo0O , 1005 , OOooO0OOoo + 'vod.png' , ii11iIi1I , '' )
 ii11i1iIII ( '[COLORgreen]Origin[/COLOR]' , '' , 10000 , OOooO0OOoo + 'ORIGIN.png' , ii11iIi1I , '' )
 ii11i1iIII ( '[COLORgreen]POPCORN BOX[/COLOR]' , ooOoOoo0O , 7061 , OOooO0OOoo + 'popcorn.png' , ii11iIi1I , '' )
 if 23 - 23: OOooOOo . OoOoOO00
 ii11i1iIII ( '[COLORgreen]RECENT EPISODES[/COLOR]' , ooOoOoo0O , 8081 , OOooO0OOoo + 'recent.png' , ii11iIi1I , '' )
 ii11i1iIII ( '[COLORgreen]ANIME[/COLOR]' , ooOoOoo0O , 1001 , OOooO0OOoo + 'anime.png' , ii11iIi1I , '' )
 ii11i1iIII ( '[COLORgreen]CLASSIC TOONS[/COLOR]' , ooOoOoo0O , 8050 , OOooO0OOoo + 'classictoons.png' , ii11iIi1I , '' )
 ii11i1iIII ( '[COLORgreen]CHAMPION IPTV[/COLOR]' , ooOoOoo0O , 9020 , OOooO0OOoo + 'UKiptvandvod.png' , ii11iIi1I , 'UK IPTV AND HD VOD' )
 ii11i1iIII ( '[COLORgreen]SCOOBY STREAMS[/COLOR]' , ooOoOoo0O , 1023 , OOooO0OOoo + 'scoob.png' , ii11iIi1I , '' )
 ii11i1iIII ( '[COLORgreen]Pandoras Box[/COLOR]' , ooOoOoo0O , 10025 , OOooO0OOoo + 'PANDORASBOX.png' , ii11iIi1I , '' )
 ii11i1iIII ( '[COLORgreen]THE REAPER[/COLOR]' , ( oOo0oooo00o ( 'aHR0cDovL3RoZXJlYXBlci54MTBob3N0LmNvbS9UaGVfUmVhcGVycy9tYWluLnBocA==' ) ) , 1016 , OOooO0OOoo + 'reap.png' , ii11iIi1I , '' )
 ii11i1iIII ( '[COLORgreen]DOCUMENTARIES[/COLOR]' , ooOoOoo0O , 8040 , OOooO0OOoo + 'documentary.png' , ii11iIi1I , '' )
 if 98 - 98: iIii1I11I1II1 % I1IiI * ii11ii1ii * I1IiI
 ii11i1iIII ( '[COLORgreen]PLAYLIST LOADER[/COLOR]' , ooOoOoo0O , 3000 , OOooO0OOoo + 'loader.png' , ii11iIi1I , '' )
 if 45 - 45: O0oO . I1IiI
 if 83 - 83: OoOO . iIii1I11I1II1 . ii11ii1ii
 if 31 - 31: o00O0oo . o00O0oo - OOooOOo / Ooo00oOo00o + o0oO0 * OOOo0
 if 63 - 63: O0oO % i1IIi / OoooooooOO - OoooooooOO
 if 8 - 8: I1IiI
 if 60 - 60: o0000oOoOoO0o / o0000oOoOoO0o
 if 46 - 46: o00O0oo * OoOO0ooOOoo0O - Ooo00oOo00o * OoOO - O0oO
 if 83 - 83: OoooooooOO
 III1ii1iII ( 'movies' , 'MAIN' )
 if 31 - 31: OoOoOO00 - OoOO0ooOOoo0O . O0oO % I1IiI - O0
 if 4 - 4: OoOoOO00 / o0oO0 . oO0o0ooO0
def O0oo0OO0oOOOo ( ) :
 ii11i1iIII ( '[COLORgreen]Cartoons[/COLOR]' , '' , 10001 , OOooO0OOoo + 'ORIGINCARTOON.png' , ii11iIi1I , '' )
 ii11i1iIII ( '[COLORgreen]Dizzy TV[/COLOR]' , '' , 10018 , OOooO0OOoo + 'dtv.png' , ii11iIi1I , '' )
 ii11i1iIII ( '[COLORgreen]Football[/COLOR]' , '' , 10002 , OOooO0OOoo + 'ORIGINFOOTBALL.png' , ii11iIi1I , '' )
 ii11i1iIII ( '[COLORgreen]Stand Up[/COLOR]' , '' , 10003 , OOooO0OOoo + 'ORIGINSTANDUP.png' , ii11iIi1I , '' )
 if 35 - 35: IIII % OOOo0
 if 70 - 70: oO0o0ooO0 * ii11ii1ii
def i1II1 ( ) :
 ii11i1iIII ( '[COLORgreen]SCOOBY STREAMS[/COLOR]' , ( oOo0oooo00o ( 'aHR0cDovL3Njb29ieXN0cmVhbS54MTBob3N0LmNvbS9zY29vYnkvdHZjYXRzLnBocA==' ) ) , 1016 , OOooO0OOoo + 'scoob.png' , ii11iIi1I , '' )
 ii11i1iIII ( '[COLORgreen]SCOOBY SCRAPES[/COLOR]' , ooOoOoo0O , 1024 , OOooO0OOoo + 'scoob.png' , ii11iIi1I , '' )
 if 66 - 66: OoooooooOO + o00O0oo + o00O0oo - i1IIi
def O0o0Ooo ( ) :
 ii11i1iIII ( '[COLORgreen]Live Tv[/COLOR]' , ooOoOoo0O , 9021 , OOooO0OOoo + 'english.png' , ii11iIi1I , '' )
 ii11i1iIII ( '[COLORgreen]XXX[/COLOR]' , ooOoOoo0O , 9022 , OOooO0OOoo + 'xxx.png' , ii11iIi1I , '' )
 ii11i1iIII ( '[COLORgreen]Hd VOD[/COLOR]' , ooOoOoo0O , 9023 , OOooO0OOoo + 'vod(1).png' , ii11iIi1I , '' )
 if 56 - 56: o0oO0 . I1IiI * oO0o0ooO0 . I1IiI
 if 72 - 72: oO0o0ooO0 / i1IIi * Oo - O0oO
def Oo0O0O0ooO0O ( ) :
 ii11i1iIII ( '[COLORgreen]SEARCH MOVIES[/COLOR]' , ooOoOoo0O , 9001 , OOooO0OOoo + 'MOVIESv.png' , ii11iIi1I , '' )
 ii11i1iIII ( '[COLORgreen]SEARCH SERIES[/COLOR]' , ooOoOoo0O , 9002 , OOooO0OOoo + 'TVSHOWSv.png' , ii11iIi1I , '' )
 ii11i1iIII ( '[COLORgreen]SEARCH CARTOONS[/COLOR]' , '' , 10005 , OOooO0OOoo + 'ORIGINCARTOON' , ii11iIi1I , '' )
 ii11i1iIII ( '[COLORgreen]SEARCH LiveTv[/COLOR]' , ooOoOoo0O , 9003 , OOooO0OOoo + 'livetv.png' , ii11iIi1I , '' )
 if 15 - 15: ii11ii1ii + I1IiI - OoooooooOO / OoOO0ooOOoo0O
 if 58 - 58: i11iIiiIii % o0000oOoOoO0o
def OO00Oo ( ) :
 ii11i1iIII ( '[COLORgreen]RADIO[/COLOR]' , ooOoOoo0O , 1013 , OOooO0OOoo + 'radio.png' , ii11iIi1I , '' )
 ii11i1iIII ( '[COLORgreen]MUSIC[/COLOR]' , ooOoOoo0O , 1030 , OOooO0OOoo + 'MUSIC.png' , ii11iIi1I , '' )
 ii11i1iIII ( '[COLORgreen]MUSIC ARCHIVE[/COLOR]' , ooOoOoo0O + ( oOo0oooo00o ( 'L3ZvZC91cmxzL211c2ljLnBocA==' ) ) , 1010 , OOooO0OOoo + 'MUSIC.png' , ii11iIi1I , '' )
 ii11i1iIII ( '[COLORgreen]MUSIC SEARCH[/COLOR]' , ooOoOoo0O , 1111 , OOooO0OOoo + 'search.png' , ii11iIi1I , '' )
 ii11i1iIII ( '[COLORgreen]AUDIO BOOKS[/COLOR]' , 'http://doremisa.com/audiobooks/' , 1006 , OOooO0OOoo + 'search.png' , ii11iIi1I , '' )
 if 51 - 51: IIII * OOooOOo + o0000oOoOoO0o + Ooo00oOo00o
 III1ii1iII ( 'movies' , 'MAIN' )
 if 66 - 66: I1IiI
def oO000Oo000 ( ) :
 i111IiI1I ( 'DELETE CACHE' , 'url' , 14 , OOooO0OOoo + 'MAIN5.png' , ii11iIi1I , '' )
 i111IiI1I ( 'DELETE PACKAGES' , 'url' , 6 , OOooO0OOoo + 'MAIN4.png' , ii11iIi1I , '' )
 i111IiI1I ( 'FORCE REFRESH' , 'url' , 10 , OOooO0OOoo + 'MAIN3.png' , ii11iIi1I , 'Force Refresh All Repos' )
 if 70 - 70: o00O0oo . Oo / OOooOOo . o00O0oo - O0 / IIII
 i111IiI1I ( 'CHECK MY IP' , 'url' , 12 , OOooO0OOoo + 'MAIN2.png' , ii11iIi1I , '' )
 i111IiI1I ( 'ANDROID ONLY DELETE TEXTURE13.DB&THUBMNAIL FOLDER' , 'url' , 13 , OOooO0OOoo + 'MAIN1.png' , ii11iIi1I , 'Only Works On Android On Windows It Deletes Your Thumnails Folder But Does Not Delete The Textures13.db' )
 ii11i1iIII ( '[COLORgreen]ADVANCED SETTINGS XML[/COLOR]' , ooOoOoo0O , 4 , OOooO0OOoo + 'XML.png' , ii11iIi1I , '' )
 ii11i1iIII ( '[COLORgreen]URL FIXES[/COLOR]' , ooOoOoo0O , 20 , OOooO0OOoo + 'URLFIX.png' , ii11iIi1I , '' )
 III1ii1iII ( 'movies' , 'MAIN' )
 if 62 - 62: iIii1I11I1II1 * I1IiI
 if 26 - 26: oO0o0ooO0 . O0oO
def oOOOOo0 ( ) :
 ii11i1iIII ( '[COLORgreen]REPOS[/COLOR]' , ( oOo0oooo00o ( 'aHR0cDovL21pcnJvcnMua29kaS50di9hZGRvbnMv' ) ) , 2030 , OOooO0OOoo + 'repos.png' , ii11iIi1I , '' )
 ii11i1iIII ( '[COLORgreen]NEW[/COLOR]' , ooOoOoo0O , 22 , OOooO0OOoo + 'NEW.png' , ii11iIi1I , '' )
 ii11i1iIII ( '[COLORgreen]IPTV[/COLOR]' , ooOoOoo0O , 23 , OOooO0OOoo + 'IPTV.png' , ii11iIi1I , '' )
 ii11i1iIII ( '[COLORgreen]VIDEO[/COLOR]' , ooOoOoo0O , 24 , OOooO0OOoo + 'VIDEO.png' , ii11iIi1I , '' )
 ii11i1iIII ( '[COLORgreen]SPORTS[/COLOR]' , ooOoOoo0O , 25 , OOooO0OOoo + 'SPORTS.png' , ii11iIi1I , '' )
 ii11i1iIII ( '[COLORgreen]KIDS[/COLOR]' , ooOoOoo0O , 26 , OOooO0OOoo + 'KIDS.png' , ii11iIi1I , '' )
 ii11i1iIII ( '[COLORgreen]MUSIC[/COLOR]' , ooOoOoo0O , 27 , OOooO0OOoo + 'MUSIC.png' , ii11iIi1I , '' )
 ii11i1iIII ( '[COLORgreen]PROGRAMS[/COLOR]' , ooOoOoo0O , 28 , OOooO0OOoo + 'PROGRAMS.png' , ii11iIi1I , '' )
 ii11i1iIII ( '[COLORgreen]XXX[/COLOR]' , 'URL' , 29 , OOooO0OOoo + 'XXX.png' , ii11iIi1I , '' )
 III1ii1iII ( 'movies' , 'MAIN' )
 if 20 - 20: i1IIi + ii11ii1ii - o0oO0
 if 30 - 30: OoOoOO00 - OoOO0ooOOoo0O - i11iIiiIii % I1IiI - OoOoOO00 * o00O0oo
def oO00O0O0O ( ) :
 i111IiI1I ( 'CHECK ADVANCED XML' , ooOoOoo0O , 8 , OOooO0OOoo + 'XML.png' , ii11iIi1I , '' )
 i111IiI1I ( 'MUCKYS XML' , ooOoOoo0O + '/wizard/muckys.xml' , 7 , OOooO0OOoo + 'XML.png' , ii11iIi1I , '' )
 i111IiI1I ( '0CACHE XML' , ooOoOoo0O + '/wizard/0cache.xml' , 7 , OOooO0OOoo + 'XML.png' , ii11iIi1I , '' )
 i111IiI1I ( 'MIKEY1234 XML' , ooOoOoo0O + '/wizard/mikey.xml' , 7 , OOooO0OOoo + 'XML.png' , ii11iIi1I , '' )
 i111IiI1I ( 'TUXENS XML' , ooOoOoo0O + '/wizard/tuxens.xml' , 7 , OOooO0OOoo + 'XML.png' , ii11iIi1I , '' )
 i111IiI1I ( 'P2P RECOMMENDED XML1' , ooOoOoo0O + '/wizard/p2p1.xml' , 7 , OOooO0OOoo + 'XML.png' , ii11iIi1I , '' )
 i111IiI1I ( 'P2P RECOMMENDED XML2' , ooOoOoo0O + '/wizard/p2p2.xml' , 7 , OOooO0OOoo + 'XML.png' , ii11iIi1I , '' )
 i111IiI1I ( 'DELETE XML' , ooOoOoo0O , 11 , OOooO0OOoo + 'XML.png' , ii11iIi1I , '' )
 III1ii1iII ( 'movies' , 'MAIN' )
 if 31 - 31: o0000oOoOoO0o - OoOoOO00 . o0000oOoOoO0o
def i1I11i1I ( ) :
 i111IiI1I ( '[COLORgreen]My Local Zip[/COLOR]' , oo0o0O00 , 48 , OOooO0OOoo + 'MB.png' , ii11iIi1I , '' )
 i111IiI1I ( '[COLORgreen]My Online Zip[/COLOR]' , oO0o0o0ooO0oO , 43 , OOooO0OOoo + 'MB.png' , ii11iIi1I , '' )
 if 81 - 81: iIii1I11I1II1 + iIii1I11I1II1 * IIII * o0oO0 % o0oO0
def ooOO00O00oo ( ) :
 i111IiI1I ( 'INSTALL FTV GUIDE AND OTHER ADDONS REQUIRED' , ooOoOoo0O + '/wizard/customftv/ftvguide-addons.zip' , 5 , OOooO0OOoo + 'FTV4.png' , ii11iIi1I , '' )
 i111IiI1I ( 'FTV GUIDE FIRST RUN SETTINGS' , ooOoOoo0O + '/wizard/customftv/settings.xml' , 17 , OOooO0OOoo + 'FTV3.png' , ii11iIi1I , '' )
 i111IiI1I ( 'FTV GUIDE ADDONS2.INI UPDATE DAILY' , 'http://ren.byethost12.com/addons2.ini' , 16 , OOooO0OOoo + 'FTV1.png' , ii11iIi1I , '' )
 i111IiI1I ( 'RESET FTV DATABASE' , 'url' , 18 , OOooO0OOoo + 'FTV2.png' , ii11iIi1I , '' )
 if 3 - 3: O0oO - O0 / O0oO % Ooo00oOo00o / O0oO . OOOo0
 if 50 - 50: IIII
 if 14 - 14: o0000oOoOoO0o % Ooo00oOo00o * o0000oOoOoO0o
def iII ( ) :
 ii11i1iIII ( '[COLORgreen]SKINS[/COLOR]' , ooOoOoo0O , 33 , OOooO0OOoo + 'skinp.png' , ii11iIi1I , '' )
 ii11i1iIII ( '[COLORgreen]ARTWORK PACKS[/COLOR]' , ooOoOoo0O , 34 , OOooO0OOoo + 'artp.png' , ii11iIi1I , '' )
 ii11i1iIII ( '[COLORgreen]CREATE UNIVERSAL PATHS[/COLOR]' , i1iIIi1 , 35 , OOooO0OOoo + 'GUI.png' , ii11iIi1I , '' )
 III1ii1iII ( 'movies' , 'MAIN' )
 if 96 - 96: Oo
def Ii1I1IIii1II ( url ) :
 O0ii1ii1ii = oooooOoo0ooo ( I1I1IiI1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 III1iII1I1ii = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( O0ii1ii1ii )
 for oOOo0 , url , oo00O00oO , iIiIIIi , ooo00OOOooO in III1iII1I1ii :
  ii11i1iIII ( oOOo0 , url , 5 , oo00O00oO , iIiIIIi , ooo00OOOooO )
 III1ii1iII ( 'movies' , 'MAIN' )
 if 67 - 67: o0000oOoOoO0o * OoOO * ii11ii1ii + OoOO0ooOOoo0O / i1IIi
def I1I111 ( ) :
 ii11i1iIII ( '[COLORgreen]GOTHAM SKINS[/COLOR]' , ooOoOoo0O , 36 , OOooO0OOoo + 'GSKIN.png' , ii11iIi1I , '' )
 ii11i1iIII ( '[COLORgreen]HELIX SKINS[/COLOR]' , ooOoOoo0O , 37 , OOooO0OOoo + 'HSKIN.png' , ii11iIi1I , '' )
 ii11i1iIII ( '[COLORgreen]ISENGAARD SKINS[/COLOR]' , i1iIIi1 , 38 , OOooO0OOoo + 'ISKIN.png' , ii11iIi1I , '' )
 III1ii1iII ( 'movies' , 'MAIN' )
 if 82 - 82: i11iIiiIii - oO0o0ooO0 * OoooooooOO / o0000oOoOoO0o
def i1oOo ( url ) :
 O0ii1ii1ii = oooooOoo0ooo ( ooOoOoo0O + oOO00Oo ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 III1iII1I1ii = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( O0ii1ii1ii )
 for oOOo0 , url , oo00O00oO , iIiIIIi , ooo00OOOooO in III1iII1I1ii :
  ii11i1iIII ( oOOo0 , url , 42 , oo00O00oO , iIiIIIi , ooo00OOOooO )
 III1ii1iII ( 'movies' , 'MAIN' )
 if 6 - 6: OoOO
def oOOo0oOo0 ( url ) :
 O0ii1ii1ii = oooooOoo0ooo ( ooOoOoo0O + IIooooo ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 III1iII1I1ii = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( O0ii1ii1ii )
 for oOOo0 , url , oo00O00oO , iIiIIIi , ooo00OOOooO in III1iII1I1ii :
  ii11i1iIII ( oOOo0 , url , 42 , oo00O00oO , iIiIIIi , ooo00OOOooO )
 III1ii1iII ( 'movies' , 'MAIN' )
 if 1 - 1: Oo / OOooOOo % oO0o0ooO0 * IIII . i11iIiiIii
def III1Iiii1I11 ( url ) :
 O0ii1ii1ii = oooooOoo0ooo ( ooOoOoo0O + IIIIiiIiI ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 III1iII1I1ii = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( O0ii1ii1ii )
 for oOOo0 , url , oo00O00oO , iIiIIIi , ooo00OOOooO in III1iII1I1ii :
  ii11i1iIII ( oOOo0 , url , 42 , oo00O00oO , iIiIIIi , ooo00OOOooO )
 III1ii1iII ( 'movies' , 'MAIN' )
 if 91 - 91: oO0o0ooO0 % i1IIi % iIii1I11I1II1
def IIi1I11I1II ( url ) :
 O0ii1ii1ii = oooooOoo0ooo ( oOo0oooo00o ( 'aHR0cHM6Ly9kbC5kcm9wYm94dXNlcmNvbnRlbnQuY29tL3MvN2ZrMjhndDlwb3QxMjJhL0JVSUxEUy50eHQ/ZGw9MA==' ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 III1iII1I1ii = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( O0ii1ii1ii )
 for oOOo0 , url , oo00O00oO , iIiIIIi , ooo00OOOooO in III1iII1I1ii :
  ii11i1iIII ( oOOo0 , url , 42 , oo00O00oO , iIiIIIi , ooo00OOOooO )
 III1ii1iII ( 'movies' , 'MAIN' )
 if 63 - 63: OoooooooOO - Ooo00oOo00o . OoOoOO00 / OOooOOo . I1IiI / O0
def o0OOOO00O0Oo ( url ) :
 O0ii1ii1ii = oooooOoo0ooo ( ooOoOoo0O + ii ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 III1iII1I1ii = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( O0ii1ii1ii )
 for oOOo0 , url , oo00O00oO , iIiIIIi , ooo00OOOooO in III1iII1I1ii :
  ii11i1iIII ( oOOo0 , url , 40 , oo00O00oO , iIiIIIi , ooo00OOOooO )
 III1ii1iII ( 'movies' , 'MAIN' )
 if 90 - 90: OOooOOo % i1IIi / Ooo00oOo00o
def IIi ( url ) :
 O0ii1ii1ii = oooooOoo0ooo ( ooOoOoo0O + i1Iii1i1I ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 III1iII1I1ii = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( O0ii1ii1ii )
 for oOOo0 , url , oo00O00oO , iIiIIIi , ooo00OOOooO in III1iII1I1ii :
  ii11i1iIII ( oOOo0 , url , 5 , oo00O00oO , iIiIIIi , ooo00OOOooO )
 III1ii1iII ( 'movies' , 'MAIN' )
 if 91 - 91: ii11ii1ii + OOOo0 . OoOO0ooOOoo0O * ii11ii1ii + OOOo0 * Oo
def O000OOOOOo ( ) :
 Iiii1i1 = OO ( oOo0oooo00o ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vYXBrdG9vbC9hcGsucGhw' ) )
 III1iII1I1ii = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( Iiii1i1 )
 for oo000o , iiIi1IIi1I , oOOo0 in III1iII1I1ii :
  o0OoOO000ooO0 ( oOOo0 , oo000o , 2031 , OOooO0OOoo + 'APK.png' )
  if 56 - 56: oO0o0ooO0
def oo0oO0oOOoo ( name , url , description ) :
 oOo00O0oo00o0 = xbmc . translatePath ( os . path . join ( iiOOooooO0Oo , 'Download' ) )
 i1111 = xbmcgui . DialogProgress ( )
 i1111 . create ( "Your App Is Downloading" , "Why not check out our website" , '' , 'Http://architects.x10host.com' )
 OOiIiIIi1 = os . path . join ( oOo00O0oo00o0 , name + '.apk' )
 try :
  os . remove ( OOiIiIIi1 )
 except :
  pass
 downloader . download ( url , OOiIiIIi1 , i1111 )
 i1iiIII111ii = xbmcgui . Dialog ( )
 i1iiIII111ii . ok ( "GenieTv" , "[COLORred]Please press ok, exit kodi and go to your downloads folder to install your app[/COLOR]" , "[COLORblue]Tool Brought To You By Architects@Work[/COLOR]" )
 if 7 - 7: o0oO0 - Oo - OoOO + o0oO0
def iI1I11iiI1i ( url ) :
 oOo00O0oo00o0 = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/resources/downloads' ) )
 i1111 = xbmcgui . DialogProgress ( )
 i1111 . create ( "Your fILM Is Downloading" , "Why not check out our website" , '' , 'Http://architects.x10host.com' )
 OOiIiIIi1 = os . path . join ( oOo00O0oo00o0 , oOOo0 + '.mp4' )
 try :
  os . remove ( OOiIiIIi1 )
 except :
  pass
 downloader . download ( url , OOiIiIIi1 , i1111 )
 i1iiIII111ii = xbmcgui . Dialog ( )
 i1iiIII111ii . ok ( "GenieTv" , "[COLORred]Please press ok, Your download With Be Avaiilable Via The My Downloads Button[/COLOR]" , "[COLORblue]Tool Brought To You By Architects@Work[/COLOR]" )
 if 78 - 78: OoOO % O0 % o00O0oo
 if 46 - 46: OoooooooOO . i11iIiiIii
def OOo0oO00ooO00 ( name , url , description ) :
 oOo00O0oo00o0 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 i1111 = xbmcgui . DialogProgress ( )
 i1111 . create ( "Your Art Pack Is Downloading" , "Why not check out our website" , '' , 'Http://architects.x10host.com' )
 OOiIiIIi1 = os . path . join ( oOo00O0oo00o0 , name )
 try :
  os . remove ( OOiIiIIi1 )
 except :
  pass
 downloader . download ( url , OOiIiIIi1 , i1111 )
 oOO0O00oO0Ooo = xbmc . translatePath ( os . path . join ( i1 ) )
 time . sleep ( 2 )
 i1111 . update ( 0 , "" , "Placing Your Art Please Wait" )
 print '======================================='
 print oOO0O00oO0Ooo
 print '======================================='
 extract . all ( OOiIiIIi1 , oOO0O00oO0Ooo , i1111 )
 i1iiIII111ii = xbmcgui . Dialog ( )
 i1iiIII111ii . ok ( "GenieTv" , "[COLORred]Once complete your artwork will be stored in your Media folder, Accessible via the Homefolder, Enjoy[/COLOR]" )
 if 67 - 67: Ooo00oOo00o - OoOO0ooOOoo0O
 if 36 - 36: IIII
def I11iI ( url ) :
 O0ii1ii1ii = oooooOoo0ooo ( oOo0oooo00o ( 'aHR0cDovL2dlbmlldHYuYXJjaGl0ZWN0cy54MTBob3N0LmNvbS90ZXN0L3doLnR4dA==' ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 III1iII1I1ii = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( O0ii1ii1ii )
 for oOOo0 , url , oo00O00oO , iIiIIIi , ooo00OOOooO in III1iII1I1ii :
  ii11i1iIII ( oOOo0 , url , 5 , oo00O00oO , iIiIIIi , ooo00OOOooO )
 try :
  O0ii1ii1ii = oooooOoo0ooo ( I1iI1ii1II + oooOOOOO + O0O0OOOOoo ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
  III1iII1I1ii = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( O0ii1ii1ii )
  for oOOo0 , url , oo00O00oO , iIiIIIi , ooo00OOOooO in III1iII1I1ii :
   ii11i1iIII ( oOOo0 , url , 5 , oo00O00oO , iIiIIIi , ooo00OOOooO )
 except : pass
 III1ii1iII ( 'movies' , 'INFO' )
 if 74 - 74: ii11ii1ii + OoOoOO00 / Ooo00oOo00o
 if 100 - 100: I1IiI * iIii1I11I1II1
def oOo00oOoO000 ( url ) :
 O0ii1ii1ii = oooooOoo0ooo ( oOo0oooo00o ( 'aHR0cDovL2dlbmlldHYuYXJjaGl0ZWN0cy54MTBob3N0LmNvbS90ZXN0L3doLnR4dA==' ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 III1iII1I1ii = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( O0ii1ii1ii )
 for oOOo0 , url , oo00O00oO , iIiIIIi , ooo00OOOooO in III1iII1I1ii :
  ii11i1iIII ( oOOo0 , url , 43 , oo00O00oO , iIiIIIi , ooo00OOOooO )
 try :
  O0ii1ii1ii = oooooOoo0ooo ( I1iI1ii1II + oooOOOOO + O0O0OOOOoo ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
  III1iII1I1ii = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( O0ii1ii1ii )
  for oOOo0 , url , oo00O00oO , iIiIIIi , ooo00OOOooO in III1iII1I1ii :
   ii11i1iIII ( oOOo0 , url , 43 , oo00O00oO , iIiIIIi , ooo00OOOooO )
 except : pass
 III1ii1iII ( 'movies' , 'INFO' )
 if 93 - 93: OOooOOo % i1IIi . o00O0oo . i11iIiiIii
 if 56 - 56: ii11ii1ii % O0 - OOOo0
def O00o0OO0 ( name , url , description ) :
 oOo00O0oo00o0 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 i1111 = xbmcgui . DialogProgress ( )
 i1111 . create ( "GenieTv" , "Downloading Content" , '' , 'Please Wait' )
 OOiIiIIi1 = os . path . join ( oOo00O0oo00o0 , name + '.zip' )
 try :
  os . remove ( OOiIiIIi1 )
 except :
  pass
 downloader . download ( url , OOiIiIIi1 , i1111 )
 IIi1I1iiiii = xbmc . translatePath ( os . path . join ( 'special://home' , 'addons' ) )
 time . sleep ( 2 )
 i1111 . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print IIi1I1iiiii
 print '======================================='
 extract . all ( OOiIiIIi1 , IIi1I1iiiii , i1111 )
 i1iiIII111ii = xbmcgui . Dialog ( )
 i1iiIII111ii . ok ( "GenieTv" , "Press ok to finish install" , "[COLOR yellow]Brought To You By Architects@Work[/COLOR]" )
 o00oOOooOOo0o ( )
 if 66 - 66: oO0o0ooO0 - oO0o0ooO0 - i11iIiiIii . ii11ii1ii - OoOO0ooOOoo0O
 if 77 - 77: I1IiI - OoOoOO00 - o0oO0
def IiiiIIiIi1 ( name , url , description ) :
 oOo00O0oo00o0 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 i1111 = xbmcgui . DialogProgress ( )
 i1111 . create ( "GenieTv" , "Downloading " , '' , 'Please Wait' )
 OOiIiIIi1 = os . path . join ( oOo00O0oo00o0 , 'plugin.program.GenieTv.install' + '.zip' )
 try :
  os . remove ( OOiIiIIi1 )
 except :
  pass
 downloader . download ( url , OOiIiIIi1 , i1111 )
 IIi1I1iiiii = xbmc . translatePath ( os . path . join ( 'special://' , 'home' ) )
 time . sleep ( 2 )
 i1111 . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print IIi1I1iiiii
 print '======================================='
 extract . all ( OOiIiIIi1 , IIi1I1iiiii , i1111 )
 i1iiIII111ii = xbmcgui . Dialog ( )
 i1iiIII111ii . ok ( "GenieTv" , "Press ok to force close kodi, if unsuccessful using windows Please kill kodi via taskmanager" , "[COLOR yellow]Brought To You By Architects@Work[/COLOR]" )
 OoOOoOooooOOo ( )
 if 87 - 87: OOOo0
def oOOOoo0O0oO ( name , url , description ) :
 oOo00O0oo00o0 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 i1111 = xbmcgui . DialogProgress ( )
 i1111 . create ( "GenieTv" , "Downloading " , '' , 'Please Wait' )
 OOiIiIIi1 = os . path . join ( oOo00O0oo00o0 , 'plugin.program.GenieTv.install' + '.zip' )
 try :
  os . remove ( OOiIiIIi1 )
 except :
  pass
 downloader . download ( url , OOiIiIIi1 , i1111 )
 IIi1I1iiiii = xbmc . translatePath ( os . path . join ( 'special://' , 'home' ) )
 time . sleep ( 2 )
 i1111 . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print IIi1I1iiiii
 print '======================================='
 extract . all ( OOiIiIIi1 , IIi1I1iiiii , i1111 )
 i1iiIII111ii = xbmcgui . Dialog ( )
 i1iiIII111ii . ok ( "GenieTv" , "Please Disconnect The Power From Your Device. DO NOT EXIT CLEANLY VIA SHUTDOWN" , "[COLOR yellow]Brought To You By Architects@Work[/COLOR]" )
 if 6 - 6: OoOO0ooOOoo0O * OOooOOo + oO0o0ooO0
 if 44 - 44: o00O0oo % Ooo00oOo00o + OoooooooOO - O0 - o00O0oo - OoOoOO00
def O0O ( name , url , description ) :
 IIi1I1iiiii = xbmc . translatePath ( os . path . join ( 'special://' , 'home' ) )
 i1111 = xbmcgui . DialogProgress ( )
 OOiIiIIi1 = os . path . join ( oo0o0O00 )
 time . sleep ( 2 )
 i1111 . create ( "GenieTv" , "Restoring" , '' , 'Please Wait' )
 print '======================================='
 print IIi1I1iiiii
 print '======================================='
 extract . all ( OOiIiIIi1 , IIi1I1iiiii , i1111 )
 i1iiIII111ii = xbmcgui . Dialog ( )
 i1iiIII111ii . ok ( "GenieTv" , "Please Disconnect The Power From Your Device. DO NOT EXIT CLEANLY VIA SHUTDOWN" , "[COLOR yellow]Brought To You By Architects@Work[/COLOR]" )
 if 80 - 80: o00O0oo * OOooOOo / OOooOOo
 if 5 - 5: OOOo0
def OoOOoOooooOOo ( ) :
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
  i1iiIII111ii . ok ( "[COLOR=red][B]WARNING  !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu." , '' )
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
  i1iiIII111ii . ok ( "[COLOR=red][B]WARNING  !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu." , '' )
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
  i1iiIII111ii . ok ( "[COLOR=red][B]WARNING  !!![/COLOR][/B]" , "Your system has been detected as Android, you " , "[COLOR=yellow][B]MUST[/COLOR][/B] force close XBMC/Kodi. [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu." , "Pulling the power cable is the simplest method to force close." )
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
  i1iiIII111ii . ok ( "[COLOR=red][B]WARNING  !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu." , "Use task manager and NOT ALT F4" )
 else :
  print "############   try atv force close  #################"
  try : os . system ( 'killall AppleTV' )
  except : pass
  print "############   try raspbmc force close  #################"
  try : os . system ( 'sudo initctl stop kodi' )
  except : pass
  try : os . system ( 'sudo initctl stop xbmc' )
  except : pass
  i1iiIII111ii . ok ( "[COLOR=red][B]WARNING  !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit via the menu." , "Your platform could not be detected so just pull the power cable." )
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
    oo00OO0000oO = IIo0Oo0oO0oOO00 . replace ( i1iIIi1 , 'special://home/' )
    I1II1 = open ( ( os . path . join ( iiI11ii1I1 , file ) ) , mode = 'w' )
    I1II1 . write ( str ( oo00OO0000oO ) )
    I1II1 . close ( )
 OoOOoOooooOOo ( )
 if 86 - 86: iIii1I11I1II1 / I1IiI . OoOoOO00
def II1i111Ii1i ( ) :
 Iiii1i1 = OO ( oOo0oooo00o ( 'aHR0cDovL3d3dy5saXN0ZW5saXZlLmV1L3VrLmh0bWw=' ) )
 III1iII1I1ii = re . compile ( '<tr>.+?<td><a href=".+?"><b>(.+?)</b>.+?<td><a href="(.+?)">' , re . DOTALL ) . findall ( Iiii1i1 )
 for oOOo0 , oo000o in III1iII1I1ii :
  iii1 ( oOOo0 , oo000o , 222 , OOooO0OOoo + 'radio.png' )
  if 96 - 96: i11iIiiIii % OoOO0ooOOoo0O
def ooO ( ) :
 Iiii1i1 = OO ( oOo0oooo00o ( 'aHR0cDovL3d3dy50b29uamV0LmNvbS8=' ) )
 III1iII1I1ii = re . compile ( '<a href="(.+?)" style="font-size:.8em;">(.+?)</a>' ) . findall ( Iiii1i1 )
 for oo000o , oOOo0 in III1iII1I1ii :
  o0OoOO000ooO0 ( '[COLORgreen]' + oOOo0 + '[/COLOR]' , 'http://www.toonjet.com/' + oo000o , 8051 , OOooO0OOoo + 'classictoons.png' )
def Ooo0oOooo0 ( url ) :
 Iiii1i1 = OO ( url )
 III1iII1I1ii = re . compile ( '<a href="(.+?)"><img src="(.+?)"' ) . findall ( Iiii1i1 )
 oOOOoo00 = re . compile ( '<a href="(.+?)">.+?</a></td></tr></table>' ) . findall ( Iiii1i1 )
 for url , iiIiIIIiiI in III1iII1I1ii :
  if 'ol.gif' in iiIiIIIiiI :
   pass
  elif 'link_block_' in iiIiIIIiiI :
   pass
  elif '.png' in iiIiIIIiiI :
   pass
  else :
   o0OoOO000ooO0 ( ( iiIiIIIiiI ) . replace ( 'http://www.toonjet.com/images/icons/' , '' ) . replace ( 'images/icons/' , '' ) . replace ( '.jpg' , '' ) . replace ( '_icon' , '' ) . replace ( '_' , ' ' ) , 'http://www.toonjet.com/' + url , 8052 , OOooO0OOoo + 'vod.png' )
 for url in oOOOoo00 :
  o0OoOO000ooO0 ( 'NEXT PAGE' , 'http://www.toonjet.com/' + url , 8051 , OOooO0OOoo + 'documentary.png' )
def iiI1IIIi ( url ) :
 Iiii1i1 = OO ( url )
 III1iII1I1ii = re . compile ( '<iframe width="640" height="480" src="(.+?)" frameborder="0" allowfullscreen></iframe>' ) . findall ( Iiii1i1 )
 for url in III1iII1I1ii :
  iii1 ( '[COLORgreen]PLAY[/COLOR]' , ( url ) . replace ( 'http://www.youtube.com/embed/' , '' ) . replace ( '?autoplay=0' , '' ) , 8043 , OOooO0OOoo + 'classictoons.png' )
  if 47 - 47: Oo % o0000oOoOoO0o % i11iIiiIii - O0 + o0oO0
  if 94 - 94: O0oO
  if 4 - 4: o00O0oo % OoOO * Ooo00oOo00o
def o0O0OOOOoOO0 ( ) :
 if 23 - 23: i11iIiiIii
 ii11i1iIII ( '[COLORgreen]Cartoons[/COLOR]' , '' , 10004 , OOooO0OOoo + 'ORIGINCARTOON.png' , ii11iIi1I , '' )
 ii11i1iIII ( '[COLORgreen]Search Cartoons[/COLOR]' , '' , 10005 , OOooO0OOoo + 'ORIGINCARTOON.png' , ii11iIi1I , '' )
 if 30 - 30: OOooOOo - i1IIi % OoOoOO00 + o0000oOoOoO0o * iIii1I11I1II1
def o0ooooO0o0O ( ) :
 iiIi11iI1iii = Oo0o0000o0o0 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oo000 = iiIi11iI1iii . lower ( )
 o0000oO = oooooOoo0ooo ( oOo0oooo00o ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2NhcnRvb24=' ) )
 III1iII1I1ii = re . compile ( '<td><a href="(.+?)">(.+)</a></td>' ) . findall ( o0000oO )
 for oo000o , oOOo0 in III1iII1I1ii :
  if iiIi11iI1iii in oOOo0 . lower ( ) :
   if 'Dad!' in oOOo0 :
    pass
   elif 'Family Guy' in oOOo0 :
    pass
   elif '2 Stupid' in oOOo0 :
    pass
   elif 'The Zelfs' in oOOo0 :
    pass
   elif 'A Clone' in oOOo0 :
    pass
   elif 'A.T.O.M' in oOOo0 :
    pass
   elif 'Almost Naked' in oOOo0 :
    pass
   elif 'Angry Kid' in oOOo0 :
    pass
   elif 'Annoying Orange' in oOOo0 :
    pass
   elif 'Aqua Teen' in oOOo0 :
    pass
   elif 'Assy Mcgee' in oOOo0 :
    pass
   elif 'Astroblast' in oOOo0 :
    pass
   elif 'Atomic Betty' in oOOo0 :
    pass
   elif 'Axe Cop' in oOOo0 :
    pass
   elif 'Baby Playpen' in oOOo0 :
    pass
   elif 'Beavis and Butt' in oOOo0 :
    pass
   elif 'Celebrity Deathmatch' in oOOo0 :
    pass
   elif 'Clerks The' in oOOo0 :
    pass
   elif 'Crapston Villas' in oOOo0 :
    pass
   elif 'Duckman:' in oOOo0 :
    pass
   elif 'Stripperella' in oOOo0 :
    pass
   elif 'Vixen' in oOOo0 :
    pass
   else :
    ii11i1iIII ( '[COLORgreen]' + oOOo0 + '[/COLOR]' , oo000o , 10006 , OOooO0OOoo + 'ORIGINCARTOON.png' , ii11iIi1I , '' )
  xbmcplugin . addSortMethod ( O0o0Oo , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 15 - 15: I1IiI % OOOo0 * o0000oOoOoO0o
def O0OoooO0 ( ) :
 Iiii1i1 = oooooOoo0ooo ( oOo0oooo00o ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2NhcnRvb24=' ) )
 III1iII1I1ii = re . compile ( '<td><a href="(.+?)">(.+)</a></td>' ) . findall ( Iiii1i1 )
 for oo000o , oOOo0 in III1iII1I1ii :
  if 'Dad!' in oOOo0 :
   pass
  elif 'Family Guy' in oOOo0 :
   pass
  elif '2 Stupid' in oOOo0 :
   pass
  elif 'The Zelfs' in oOOo0 :
   pass
  elif 'A Clone' in oOOo0 :
   pass
  elif 'A.T.O.M' in oOOo0 :
   pass
  elif 'Almost Naked' in oOOo0 :
   pass
  elif 'Angry Kid' in oOOo0 :
   pass
  elif 'Annoying Orange' in oOOo0 :
   pass
  elif 'Aqua Teen' in oOOo0 :
   pass
  elif 'Assy Mcgee' in oOOo0 :
   pass
  elif 'Astroblast' in oOOo0 :
   pass
  elif 'Atomic Betty' in oOOo0 :
   pass
  elif 'Axe Cop' in oOOo0 :
   pass
  elif 'Baby Playpen' in oOOo0 :
   pass
  elif 'Beavis and Butt' in oOOo0 :
   pass
  elif 'Celebrity Deathmatch' in oOOo0 :
   pass
  elif 'Clerks The' in oOOo0 :
   pass
  elif 'Crapston Villas' in oOOo0 :
   pass
  elif 'Duckman:' in oOOo0 :
   pass
  elif 'Stripperella' in oOOo0 :
   pass
  elif 'Vixen' in oOOo0 :
   pass
  else :
   ii11i1iIII ( '[COLORgreen]' + oOOo0 + '[/COLOR]' , oo000o , 10006 , OOooO0OOoo + 'ORIGINCARTOON.png' , ii11iIi1I , '' )
 xbmcplugin . addSortMethod ( O0o0Oo , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 85 - 85: o0000oOoOoO0o
def iI1i11II1i ( url ) :
 Iiii1i1 = oooooOoo0ooo ( url )
 oOOOoo00 = re . compile ( '<img src="(.+?)" id="series_image" width="250" height="370" alt=".+?" />' ) . findall ( Iiii1i1 )
 for iiIiIIIiiI in oOOOoo00 :
  o0o0OoOo0O0OO = iiIiIIIiiI
 iIi1I11I = re . compile ( '<li><a href="(.+?)">Next</a></li>' ) . findall ( Iiii1i1 )
 for url in iIi1I11I :
  ii11i1iIII ( '[COLORgreen]NEXT PAGE[/COLOR]' , url , 10007 , o0o0OoOo0O0OO , ii11iIi1I , '' )
 III1iII1I1ii = re . compile ( '&nbsp;<a href="(.+?)">(.+?)</a>' ) . findall ( Iiii1i1 )
 for url , oOOo0 in III1iII1I1ii :
  iii1 ( '[COLORgreen]' + oOOo0 + '[/COLOR]' , url , 10007 , o0o0OoOo0O0OO )
  if 42 - 42: iIii1I11I1II1 / O0oO / Ooo00oOo00o - OoooooooOO
  if 33 - 33: I1IiI * OoOO0ooOOoo0O - OoOoOO00
 xbmcplugin . addSortMethod ( O0o0Oo , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 83 - 83: I1IiI - o00O0oo / o0000oOoOoO0o / O0oO + OoOO - O0
def I11I1i1iIII1I ( url , IMAGE ) :
 Iiii1i1 = oooooOoo0ooo ( url )
 III1iII1I1ii = re . compile ( '"playlist">(.+?)</span></div><div><iframe src="(.+?)"' ) . findall ( Iiii1i1 )
 for oOOo0 , url in III1iII1I1ii :
  print oOOo0 + '     ' + url
  if 'easy' in url :
   iI ( url )
   if 2 - 2: o0oO0 / oO0o0ooO0 . oO0o0ooO0 % O0oO
   if 11 - 11: iIii1I11I1II1
  xbmcplugin . addSortMethod ( O0o0Oo , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 20 - 20: OoOoOO00 % Oo + ii11ii1ii + o0oO0
def iI ( url ) :
 Iiii1i1 = oooooOoo0ooo ( url )
 III1iII1I1ii = re . compile ( "url: '(.+?)'," ) . findall ( Iiii1i1 )
 for url in III1iII1I1ii :
  II11iIIiiiII ( url )
  if 79 - 79: O0 * i11iIiiIii - IIII / IIII
  if 48 - 48: O0
  if 93 - 93: i11iIiiIii - OOOo0 * ii11ii1ii * o0000oOoOoO0o % O0 + OoooooooOO
def I1i1i1 ( ) :
 if 73 - 73: O0 * oO0o0ooO0 + o00O0oo + o0oO0
 ii11i1iIII ( '[COLORgreen]Stand Up[/COLOR]' , '' , 10014 , OOooO0OOoo + 'ORIGINSTANDUP.png' , ii11iIi1I , '' )
 ii11i1iIII ( '[COLORgreen]Search Comedian[/COLOR]' , '' , 10015 , OOooO0OOoo + 'ORIGINSTANDUP.png' , ii11iIi1I , '' )
 ii11i1iIII ( '[COLORgreen]Others[/COLOR]' , '' , 10017 , OOooO0OOoo + 'ORIGINSTANDUP.png' , ii11iIi1I , '' )
 if 40 - 40: OoOoOO00 . I1IiI * O0oO + OoOO0ooOOoo0O + OoOO0ooOOoo0O
def I1ii1I1iiii ( ) :
 o0000oO = oooooOoo0ooo ( ( oOo0oooo00o ( 'aHR0cDovL2JhY2syYmFzaWNzYnVpbGQuY28udWsvdGVzdC9zdGFuZHVwbGlzdC5waHA=' ) ) )
 III1iII1I1ii = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( o0000oO )
 for oo000o , iiIiIIIiiI , oOOo0 in III1iII1I1ii :
  iii1 ( '[COLORgreen]' + oOOo0 + '[/COLOR]' , oo000o , 222 , iiIiIIIiiI )
  if 36 - 36: OoooooooOO . Ooo00oOo00o
def oOIIiIi ( ) :
 iiIi11iI1iii = Oo0o0000o0o0 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oo000 = iiIi11iI1iii . lower ( )
 o0000oO = oooooOoo0ooo ( ( oOo0oooo00o ( 'aHR0cDovL3d3dy5jb3VjaHRyaXBwZXIuY29tL2ZvcnVtMi9wYWdlLnBocD9wYWdlPTM=' ) ) )
 OOoOooOoOOOoo = re . compile ( '<tr>.+?<td width=".+?" align=".+?">.+?<img border=".+?" src="..(.+?)" width=".+?" height=".+?"></td>.+?<td width=".+?" valign=".+?" align=".+?"><font size=".+?">(.+?)</font></td>.+?<td width=".+?">(.+?)</td>' , re . DOTALL ) . findall ( o0000oO )
 for iiIiIIIiiI , Iiii1iI1i , iIiiiI1IiI1I1 in OOoOooOoOOOoo :
  for iiIi11iI1iii in Iiii1iI1i :
   print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< img >>>>>>>>>>>>>>>>>>>>>>>>>>'
   I1ii1ii11i1I = re . compile ( '<a href="(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( iIiiiI1IiI1I1 )
   for oo000o , oOOo0 in I1ii1ii11i1I :
    if 'tube' in oo000o :
     pass
    elif 'stage' in oo000o :
     iii1 ( '[COLORgreen]' + Iiii1iI1i + '   -   ' + oOOo0 + '[/COLOR]' , ( oo000o ) . replace ( '" target="_blank' , '' ) , 10016 , 'http://couchtripper.com/' + iiIiIIIiiI , )
    elif 'vee' in oo000o :
     pass
     if 58 - 58: oO0o0ooO0 + Oo
def II1I1I1Ii ( ) :
 o0000oO = oooooOoo0ooo ( ( oOo0oooo00o ( 'aHR0cDovL3d3dy5jb3VjaHRyaXBwZXIuY29tL2ZvcnVtMi9wYWdlLnBocD9wYWdlPTM=' ) ) )
 OOoOooOoOOOoo = re . compile ( '<tr>.+?<td width=".+?" align=".+?">.+?<img border=".+?" src="..(.+?)" width=".+?" height=".+?"></td>.+?<td width=".+?" valign=".+?" align=".+?"><font size=".+?">(.+?)</font></td>.+?<td width=".+?">(.+?)</td>' , re . DOTALL ) . findall ( o0000oO )
 for iiIiIIIiiI , Iiii1iI1i , iIiiiI1IiI1I1 in OOoOooOoOOOoo :
  I1ii1ii11i1I = re . compile ( '<a href="(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( iIiiiI1IiI1I1 )
  for oo000o , oOOo0 in I1ii1ii11i1I :
   if 'tube' in oo000o :
    pass
   elif 'stage' in oo000o :
    iii1 ( '[COLORgreen]' + Iiii1iI1i + '   -   ' + oOOo0 + '[/COLOR]' , ( oo000o ) . replace ( '" target="_blank' , '' ) , 10016 , 'http://couchtripper.com/' + iiIiIIIiiI )
   elif 'vee' in oo000o :
    pass
    if 70 - 70: Ooo00oOo00o % OoOO + OoOO0ooOOoo0O / o00O0oo % O0
    if 100 - 100: OOooOOo + OoOO0ooOOoo0O * OOooOOo
 xbmcplugin . addSortMethod ( O0o0Oo , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 80 - 80: OOooOOo * O0 - o00O0oo
def oo00O00Oo ( url ) :
 o0000oO = oooooOoo0ooo ( url )
 print '>>>>>>>>>>>>>>>>>>>>>>>>' + url + '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'
 IIIII1II = re . compile ( "url\[.+?\] = '(.+?)';" ) . findall ( o0000oO )
 print '>>>>>>>>>>>>>>>>>>>>>>>' + ( str ( IIIII1II ) ) + '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
 for url in IIIII1II :
  II11iIIiiiII ( ( url ) . replace ( '[' , '' ) . replace ( ']' , '' ) . replace ( '\'' , '' ) )
  if 35 - 35: iIii1I11I1II1
  if 42 - 42: O0oO . OOOo0 . i1IIi + I1IiI + OoOO0ooOOoo0O + OOOo0
  if 31 - 31: oO0o0ooO0 . OoOO0ooOOoo0O - o0oO0 . OoooooooOO / OoooooooOO
  if 56 - 56: Ooo00oOo00o / OoOO / i11iIiiIii + OoooooooOO - Oo - o0000oOoOoO0o
  if 21 - 21: O0 % IIII . OOOo0 / OoOoOO00 + IIII
  if 53 - 53: OoOO - OOOo0 - OoOO * oO0o0ooO0
  if 71 - 71: O0 - iIii1I11I1II1
def i1II ( ) :
 if 14 - 14: OoOO / OoOO % o0oO0
 ooOii ( '[COLOR darkgoldenrod]Open Pandora\'s Box[/COLOR]' , '' , 10029 , 'https://encrypted-tbn1.gstatic.com/images?q=tbn%3AANd9GcTQ9r4TA8yIw9ggxuwsHxWojo6tPVfgTe8QIOxOQwzNR2TavtCi6Q' , ii11iIi1I , '' )
 ooOii ( '[COLOR darkgoldenrod]Search[/COLOR]' , '' , 10026 , 'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png' , ii11iIi1I , '' )
 if 82 - 82: I1IiI - Ooo00oOo00o % I1IiI * i11iIiiIii . OoOoOO00 % OoOoOO00
 xbmcplugin . setContent ( O0o0Oo , 'movies' )
 if 54 - 54: o0000oOoOoO0o + o00O0oo
def o00I1 ( ) :
 ooOii ( 'Search Pandoras Films' , '' , 10027 , OOooO0OOoo + 'PANDORASBOX.png' , ii11iIi1I , '' )
 ooOii ( 'Search Pandoras TV' , '' , 10028 , OOooO0OOoo + 'PANDORASBOX.png' , ii11iIi1I , '' )
 if 55 - 55: oO0o0ooO0 . OoOoOO00 % Ooo00oOo00o * oO0o0ooO0 + o0oO0 + o00O0oo
def II1Iiiiii ( ) :
 if 36 - 36: OOOo0 - o0000oOoOoO0o
 iiIi11iI1iii = Oo0o0000o0o0 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oo000 = iiIi11iI1iii . lower ( )
 i11i11111i1i = [ 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' ]
 if 72 - 72: OoOO0ooOOoo0O % ii11ii1ii + Ooo00oOo00o / OoOO + IIII
 for I1I1i in i11i11111i1i :
  I1IIIiIiIi = Base_Pand + I1I1i + CAT
  o0000oO = oooooOoo0ooo ( I1IIIiIiIi )
  III1iII1I1ii = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( o0000oO )
  for oo000o , oo00O00oO , IIIII1 , iIiIIIi , oOOo0 in III1iII1I1ii :
   if iiIi11iI1iii in oOOo0 . lower ( ) :
    iIi1Ii1i1iI ( oOOo0 , oo000o , 222 , oo00O00oO , iIiIIIi , IIIII1 )
    if 16 - 16: OoOO0ooOOoo0O / Oo / OoooooooOO * OOOo0 + i1IIi % OoOO0ooOOoo0O
    xbmcplugin . setContent ( O0o0Oo , 'movies' )
    xbmcplugin . addSortMethod ( O0o0Oo , xbmcplugin . SORT_METHOD_TITLE ) ;
    if 71 - 71: I1IiI
    if 14 - 14: i11iIiiIii % OoOO0ooOOoo0O
def OooO0oo ( ) :
 if 89 - 89: o00O0oo
 iiIi11iI1iii = Oo0o0000o0o0 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oo000 = iiIi11iI1iii . lower ( )
 i11i11111i1i = [ 'a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' , 'p' , 'q' , 'r' , 's' , 't' , 'u' , 'v' , 'w' , 'x' , 'y' , 'z' ]
 if 76 - 76: o0oO0
 for I1I1i in i11i11111i1i :
  IIIiI11ii1I = Base_Pand + I1I1i + CAT
  o0000oO = oooooOoo0ooo ( IIIiI11ii1I )
  III1iII1I1ii = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( o0000oO )
  for oOOo0 , IIIII1 , oo000o , iiIiIIIiiI , iIiIIIi , IiiiI in III1iII1I1ii :
   if iiIi11iI1iii in oOOo0 . lower ( ) :
    ooOii ( oOOo0 , oo000o , IiiiI , iiIiIIIiiI , iIiIIIi , IIIII1 )
    if 61 - 61: OoOO0ooOOoo0O % OoOO0ooOOoo0O * OOooOOo / OOooOOo
    xbmcplugin . setContent ( O0o0Oo , 'movies' )
    xbmcplugin . addSortMethod ( O0o0Oo , xbmcplugin . SORT_METHOD_TITLE ) ;
    if 75 - 75: IIII . o0oO0
    if 50 - 50: I1IiI
def O00o0OO0000oo ( ) :
 if 27 - 27: O0
 Iiii1i1 = oooooOoo0ooo ( oOo0oooo00o ( 'aHR0cDovL3NlZWR1cmdyZWVkLngxMGhvc3QuY29tL29yaWdpbi9zcG9uZ2VtYWluLnBocA==' ) )
 III1iII1I1ii = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( Iiii1i1 )
 for oOOo0 , IIIII1 , oo000o , iiIiIIIiiI , iIiIIIi , IiiiI in III1iII1I1ii :
  ooOii ( oOOo0 , oo000o , IiiiI , iiIiIIIiiI , iIiIIIi , IIIII1 )
  if 79 - 79: OOooOOo - o0000oOoOoO0o + OOooOOo . OoOO
def ii1III11 ( url ) :
 if 7 - 7: oO0o0ooO0 % O0 . I1IiI + OOOo0 - o0000oOoOoO0o
 xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
 o0o0O00oo0 = ( '%s%s' % ( Ii1ii1IiIII , url ) )
 O0ii1ii1ii = oooooOoo0ooo ( url )
 III1iII1I1ii = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( O0ii1ii1ii )
 for url , oo00O00oO , IIIII1 , ooO0o , oOOo0 in III1iII1I1ii :
  iIi1Ii1i1iI ( oOOo0 , url , 222 , oo00O00oO , ooO0o , IIIII1 )
  if 51 - 51: IIII
  III1ii1iII ( 'tvshows' , 'Media Info 3' )
  if 25 - 25: OoooooooOO + IIII * ii11ii1ii
  xbmcplugin . addSortMethod ( O0o0Oo , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 92 - 92: OOOo0 + o0000oOoOoO0o + O0 / OOooOOo + O0oO
  if 18 - 18: o0oO0 * I1IiI . oO0o0ooO0 / ii11ii1ii / i11iIiiIii
def IIIII ( url ) :
 if 78 - 78: o00O0oo * i1IIi
 Iiii1i1 = oooooOoo0ooo ( url )
 III1iII1I1ii = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( Iiii1i1 )
 for oOOo0 , IIIII1 , url , iiIiIIIiiI , iIiIIIi , IiiiI in III1iII1I1ii :
  ooOii ( oOOo0 , url , IiiiI , iiIiIIIiiI , iIiIIIi , IIIII1 )
  if 1 - 1: OOOo0 / IIII * o0oO0
 III1ii1iII ( 'tvshows' , 'Media Info 3' )
 if 1 - 1: o0000oOoOoO0o * OOooOOo . I1IiI / O0
 if 100 - 100: O0oO . OOooOOo * Oo % O0 * O0
 xbmcplugin . addSortMethod ( O0o0Oo , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 14 - 14: ii11ii1ii . o0oO0 + OoOoOO00 / oO0o0ooO0 / o0000oOoOoO0o
def iIi1Ii1i1iI ( name , url , mode , iconimage , fanart , description ) :
 if 74 - 74: O0 / i1IIi
 OoO = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 Iiiiii111i1ii = True
 i1i1iII1 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 i1i1iII1 . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 i1i1iII1 . setProperty ( "Fanart_Image" , fanart )
 Iiiiii111i1ii = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = OoO , listitem = i1i1iII1 , isFolder = False )
 return Iiiiii111i1ii
 if 25 - 25: iIii1I11I1II1 % oO0o0ooO0 . o0oO0
def ooOii ( name , url , mode , iconimage , fanart , description ) :
 if 14 - 14: OoOO + ii11ii1ii - oO0o0ooO0 / O0 . O0oO
 OoO = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 Iiiiii111i1ii = True
 i1i1iII1 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 i1i1iII1 . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 i1i1iII1 . setProperty ( "Fanart_Image" , fanart )
 Iiiiii111i1ii = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = OoO , listitem = i1i1iII1 , isFolder = True )
 return Iiiiii111i1ii
 if 45 - 45: O0oO
 if 83 - 83: I1IiI . OoooooooOO
 if 58 - 58: i11iIiiIii + OoooooooOO % OoooooooOO / IIII / i11iIiiIii
 if 62 - 62: Ooo00oOo00o / ii11ii1ii
 if 7 - 7: OoooooooOO . IIII
 if 53 - 53: o00O0oo % o00O0oo * OOooOOo + I1IiI
 if 92 - 92: OoooooooOO + i1IIi / o00O0oo * O0
def O00oOo00o0o ( ) :
 if 85 - 85: oO0o0ooO0 + OoooooooOO * oO0o0ooO0 - O0oO % i11iIiiIii
 ii11i1iIII ( '[COLORgreen]Recent Episodes[/COLOR]' , '' , 10019 , OOooO0OOoo + 'dtv.png' , ii11iIi1I , '' )
 ii11i1iIII ( '[COLORgreen]Genres[/COLOR]' , '' , 10020 , OOooO0OOoo + 'dtv.png' , ii11iIi1I , '' )
 ii11i1iIII ( '[COLORgreen]Search[/COLOR]' , '' , 10021 , OOooO0OOoo + 'dtv.png' , ii11iIi1I , '' )
 if 71 - 71: ii11ii1ii - o0oO0 / I1IiI * I1IiI / i1IIi . i1IIi
def ooo000ooO0000 ( ) :
 if 97 - 97: Oo * OOOo0 . iIii1I11I1II1
 Iiii1i1 = cloudflare . source ( oOo0oooo00o ( 'aHR0cDovL2RpemlsYWIuY29t' ) )
 III1iII1I1ii = re . compile ( '<li id=".+?">.+?<a href="(.+?)">.+?<img width="40" height="40" src="(.+?)" alt=""/>.+?<span class="title">\n(.+?)</span>.+?<span class="alt-title">\n(.+?)</span>.+?</a>.+?</li>' , re . DOTALL ) . findall ( Iiii1i1 )
 for oo000o , iiIiIIIiiI , oOOo0 , I1Ii1111iIi in III1iII1I1ii :
  ii11i1iIII ( oOOo0 + '  -  ' + ( I1Ii1111iIi ) . replace ( 'sezon' , 'Season' ) . replace ( 'bölüm' , 'Episode' ) , oo000o , 10023 , OOooO0OOoo + 'dtv.png' , ii11iIi1I , '' )
  if 31 - 31: o0000oOoOoO0o . O0oO * o0oO0 + i11iIiiIii * OoOO
  if 93 - 93: ii11ii1ii / iIii1I11I1II1 * i1IIi % OoooooooOO * O0 * o0000oOoOoO0o
  if 64 - 64: OoOoOO00 + O0 / iIii1I11I1II1 / Oo . o0oO0 % IIII
def iiI1I1ii ( ) :
 if 85 - 85: o0oO0 / O0
 ii11i1iIII ( '[COLORgreen]Action[/COLOR]' , 'Aksiyon' , 10024 , OOooO0OOoo + 'dtv.png' , ii11iIi1I , '' )
 ii11i1iIII ( '[COLORgreen]Adventure[/COLOR]' , 'Macera' , 10024 , OOooO0OOoo + 'dtv.png' , ii11iIi1I , '' )
 ii11i1iIII ( '[COLORgreen]Animation[/COLOR]' , 'Animasyon' , 10024 , OOooO0OOoo + 'dtv.png' , ii11iIi1I , '' )
 ii11i1iIII ( '[COLORgreen]Anime[/COLOR]' , 'Anime' , 10024 , OOooO0OOoo + 'dtv.png' , ii11iIi1I , '' )
 ii11i1iIII ( '[COLORgreen]Biography[/COLOR]' , 'Biyografi' , 10024 , OOooO0OOoo + 'dtv.png' , ii11iIi1I , '' )
 ii11i1iIII ( '[COLORgreen]Comedy[/COLOR]' , 'Komedi' , 10024 , OOooO0OOoo + 'dtv.png' , ii11iIi1I , '' )
 ii11i1iIII ( '[COLORgreen]Crime[/COLOR]' , 'Su%C3%A7' , 10024 , OOooO0OOoo + 'dtv.png' , ii11iIi1I , '' )
 ii11i1iIII ( '[COLORgreen]Documentary[/COLOR]' , 'Belgesel' , 10024 , OOooO0OOoo + 'dtv.png' , ii11iIi1I , '' )
 ii11i1iIII ( '[COLORgreen]Drama[/COLOR]' , 'Dram' , 10024 , OOooO0OOoo + 'dtv.png' , ii11iIi1I , '' )
 ii11i1iIII ( '[COLORgreen]Family[/COLOR]' , 'Aile' , 10024 , OOooO0OOoo + 'dtv.png' , ii11iIi1I , '' )
 ii11i1iIII ( '[COLORgreen]Fantasy[/COLOR]' , 'Fantastik' , 10024 , OOooO0OOoo + 'dtv.png' , ii11iIi1I , '' )
 ii11i1iIII ( '[COLORgreen]History[/COLOR]' , 'Tarih' , 10024 , OOooO0OOoo + 'dtv.png' , ii11iIi1I , '' )
 ii11i1iIII ( '[COLORgreen]Horror[/COLOR]' , 'Korku' , 10024 , OOooO0OOoo + 'dtv.png' , ii11iIi1I , '' )
 ii11i1iIII ( '[COLORgreen]Mini-Series[/COLOR]' , 'Mini%20Dizi' , 10024 , OOooO0OOoo + 'dtv.png' , ii11iIi1I , '' )
 ii11i1iIII ( '[COLORgreen]Musical[/COLOR]' , 'M%C3%BCzikal' , 10024 , OOooO0OOoo + 'dtv.png' , ii11iIi1I , '' )
 ii11i1iIII ( '[COLORgreen]Mystery[/COLOR]' , 'Gizem' , 10024 , OOooO0OOoo + 'dtv.png' , ii11iIi1I , '' )
 ii11i1iIII ( '[COLORgreen]Romance[/COLOR]' , 'Romantik' , 10024 , OOooO0OOoo + 'dtv.png' , ii11iIi1I , '' )
 ii11i1iIII ( '[COLORgreen]Science Fiction[/COLOR]' , 'Bilim%20Kurgu' , 10024 , OOooO0OOoo + 'dtv.png' , ii11iIi1I , '' )
 ii11i1iIII ( '[COLORgreen]Sport[/COLOR]' , 'Spor' , 10024 , OOooO0OOoo + 'dtv.png' , ii11iIi1I , '' )
 ii11i1iIII ( '[COLORgreen]Thriller[/COLOR]' , 'Gerilim' , 10024 , OOooO0OOoo + 'dtv.png' , ii11iIi1I , '' )
 ii11i1iIII ( '[COLORgreen]War[/COLOR]' , 'Sava%C5%9F' , 10024 , OOooO0OOoo + 'dtv.png' , ii11iIi1I , '' )
 ii11i1iIII ( '[COLORgreen]Western[/COLOR]' , 'Tarih' , 10024 , OOooO0OOoo + 'dtv.png' , ii11iIi1I , '' )
 ii11i1iIII ( '[COLORgreen]Youth[/COLOR]' , 'Gen%C3%A7lik' , 10024 , OOooO0OOoo + 'dtv.png' , ii11iIi1I , '' )
 if 18 - 18: OOooOOo % O0 * ii11ii1ii
def o0 ( url ) :
 Iii = 'http://dizilab.com/arsiv?limit=100&tur=' + url + '&orderby=&ulke=&order=&yil=&dizi_adi='
 o0000oO = cloudflare . source ( Iii )
 III1iII1I1ii = re . compile ( '<div class="tv-series-single">.+?<a href="(.+?)" class="film-image">.+?<img src="(.+?)" alt=""/>.+?<span class="position">.+?</span>\n(.+?)</a>' , re . DOTALL ) . findall ( o0000oO )
 for url , iiIiIIIiiI , oOOo0 in III1iII1I1ii :
  ii11i1iIII ( '[COLORgreen]' + oOOo0 + '[/COLOR]' , url , 10022 , OOooO0OOoo + 'dtv.png' , ii11iIi1I , '' )
  if 19 - 19: o0000oOoOoO0o % OoOoOO00 / i11iIiiIii / oO0o0ooO0 - OoooooooOO
  if 37 - 37: OoOO0ooOOoo0O / OoooooooOO - i11iIiiIii
  if 18 - 18: oO0o0ooO0 . OOOo0
  if 40 - 40: O0 - OoooooooOO - IIII
def iIiii ( ) :
 if 76 - 76: OOOo0 . o0oO0 - ii11ii1ii - oO0o0ooO0 * Ooo00oOo00o
 iiIi11iI1iii = Oo0o0000o0o0 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oo000 = iiIi11iI1iii . lower ( )
 oo000o = ( oOo0oooo00o ( 'aHR0cDovL2RpemlsYWIuY29tL2Fyc2l2P2xpbWl0PSZ0dXI9Jm9yZGVyYnk9JnVsa2U9Jm9yZGVyPSZ5aWw9JmRpemlfYWRpPQ==' ) ) + ( iiIi11iI1iii ) . replace ( ' ' , '+' )
 o0000oO = cloudflare . source ( oo000o )
 III1iII1I1ii = re . compile ( '<a href="(.+?)" class="film-image">\n<img src="(.+?)" alt=""/>\n</a>\n<div class="tss-detail">\n<a class="title" style="" href=".+?">\n<span class="position">.+?</span>\n(.+?)</a>' ) . findall ( o0000oO )
 for oo000o , iiIiIIIiiI , oOOo0 in III1iII1I1ii :
  if iiIi11iI1iii in oOOo0 . lower ( ) :
   ii11i1iIII ( '[COLORgreen]' + oOOo0 + '[/COLOR]' , oo000o , 10022 , OOooO0OOoo + 'dtv.png' )
   if 54 - 54: IIII + O0 + o0000oOoOoO0o * O0oO - OoOO0ooOOoo0O % OoOO
   if 13 - 13: o0oO0 / oO0o0ooO0 * Ooo00oOo00o . Ooo00oOo00o * o0oO0
   if 63 - 63: O0oO / O0 * Oo + OoOoOO00 / IIII + o00O0oo
def OOoO000 ( url ) :
 o0000oO = cloudflare . source ( url )
 III1iII1I1ii = re . compile ( '<a class="season" href="(.+?)">\n(.+?)\n</a>.+?<a class="episode" href=".+?">\n(.+?)\n</a>.+?<a class="episode-name" href=".+?">\n(.+?)</a>' , re . DOTALL ) . findall ( o0000oO )
 for oOOOO , Ii , Ii1ii111i1 , oOOo0 in III1iII1I1ii :
  i1i1i1I = ( Ii1ii111i1 ) . replace ( 'Sezon' , '' ) . replace ( 'bölüm' , '' ) . replace ( 'Bölüm' , '' ) . replace ( 'BÃ¶lÃ¼m' , '' ) . replace ( '.' , '' )
  oOoo000 = ( Ii ) . replace ( 'bölüm' , '' ) . replace ( 'Sezon' , '' ) . replace ( 'Bölüm' , '' ) . replace ( 'BÃ¶lÃ¼m' , '' ) . replace ( '.' , '' )
  OooOo00o = 'Season ' + oOoo000 + 'Episode ' + i1i1i1I + oOOo0
  IiI11i1IIiiI ( OooOo00o , oOOOO )
  if 60 - 60: ii11ii1ii * OOOo0
  xbmcplugin . addSortMethod ( O0o0Oo , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 17 - 17: OoOO0ooOOoo0O % Oo / ii11ii1ii . IIII * OoOO0ooOOoo0O - OoOoOO00
  if 41 - 41: o00O0oo
def IiI11i1IIiiI ( name , url ) :
 oOOOO = url
 oOOoo0o0OOOO = name
 i1IiII1III = cloudflare . source ( oOOOO )
 oOOOoo00 = re . compile ( 'file: "(.+?)",.+?label: "(.+?)",' , re . DOTALL ) . findall ( i1IiII1III )
 for IIIII1II , i1O00oo in oOOOoo00 :
  iii1 ( '[COLORgreen]' + oOOoo0o0OOOO + i1O00oo + '[/COLOR]' , IIIII1II , 10012 , OOooO0OOoo + 'dtv.png' )
  if 77 - 77: oO0o0ooO0 % OoOO0ooOOoo0O - o0000oOoOoO0o % o0oO0 - Ooo00oOo00o / Oo
 xbmcplugin . addSortMethod ( O0o0Oo , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 4 - 4: OoooooooOO - i1IIi % o00O0oo - OoOO0ooOOoo0O * OOooOOo
 if 85 - 85: OoooooooOO * iIii1I11I1II1 . oO0o0ooO0 / OoooooooOO % OOOo0 % O0
 if 36 - 36: o00O0oo / OoOoOO00 / IIII / IIII + ii11ii1ii
 if 95 - 95: IIII
def Ooo0oo ( ) :
 ii11i1iIII ( '[COLORgreen]Highlights[/COLOR]' , '' , 10008 , OOooO0OOoo + 'ORIGINFOOTBALL.png' , ii11iIi1I , '' )
 ii11i1iIII ( '[COLORgreen]Fixtures[/COLOR]' , '' , 10009 , OOooO0OOoo + 'ORIGINFOOTBALL.png' , ii11iIi1I , '' )
 if 41 - 41: I1IiI * o0000oOoOoO0o / I1IiI % OoOO
def IioO0oOOO0Ooo ( ) :
 Iiii1i1 = oooooOoo0ooo ( oOo0oooo00o ( 'aHR0cDovL2xpdmVvbnNhdC5jb20vcXVpY2tpbmRleC5odG1s' ) )
 III1iII1I1ii = re . compile ( '<a target="_self" href="(.+?)".+?src="(.+?)" alt="(.+?)"' , re . DOTALL ) . findall ( Iiii1i1 )
 for oo000o , iiIiIIIiiI , oOOo0 in III1iII1I1ii :
  ii11i1iIII ( '[COLORgreen]' + ( oOOo0 ) . replace ( 'amp;' , '' ) + '[/COLOR]' , oOo0oooo00o ( 'aHR0cDovL2xpdmVvbnNhdC5jb20v' ) + oo000o , 10010 , oOo0oooo00o ( 'aHR0cDovL2xpdmVvbnNhdC5jb20v' ) + iiIiIIIiiI , ii11iIi1I , '' )
  if 38 - 38: OOOo0
def oOo0OoOOo0 ( url ) :
 o0000oO = oooooOoo0ooo ( url )
 iII11I1Ii1 = re . compile ( 'AndClearL.+?><h2.+?head>(.*?)float' , re . DOTALL ) . findall ( o0000oO )
 for iII11I1Ii1 in iII11I1Ii1 :
  o0o0 = re . compile ( '(.*?)</h2>' ) . findall ( str ( iII11I1Ii1 ) )
  for oOo0oO in o0o0 :
   oOo0oO = oOo0oO
  IIi1IIIIi = re . compile ( 'comp_head>(.*?)</span>.*?<div class = fLeft width = ".*?"><img src="(.*?)">.*?</div>.*?ST:(.*?)</div>(.+?)<!-- around all of channel types ENDS 2-->' , re . DOTALL ) . findall ( str ( iII11I1Ii1 ) )
  for OOOoO , iiIiIIIiiI , time , I1i in IIi1IIIIi :
   iiiI = re . compile ( ",CAPTION, '(.+?)&nbsp" ) . findall ( I1i )
   ii11i1iIII ( '[COLORgreen]' + oOo0oO + ' - ' + OOOoO + ' - ' + time + '[/COLOR]' , '' , 10010 , oOo0oooo00o ( 'aHR0cDovL2xpdmVvbnNhdC5jb20=' ) + iiIiIIIiiI , ii11iIi1I , ( str ( iiiI ) ) )
   if 21 - 21: i11iIiiIii / i1IIi + OOOo0 * OoOO0ooOOoo0O . O0oO
 III1ii1iII ( 'tvshows' , 'Media Info 3' )
 if 84 - 84: O0 . o0000oOoOoO0o - OoOoOO00 . o0oO0 / OoOoOO00
def iii1I1i ( ) :
 if 86 - 86: Oo / OoOO + O0 * oO0o0ooO0
 ii11i1iIII ( '[COLORgreen]Shows[/COLOR]' , 'http://www.fullmatchesandshows.com/category/show/' , 10011 , 'http://www.fm-base.co.uk/forum/attachments/club-competition-logos/3885-soccer-am-logo-socceram.png' , OOooO0OOoo + 'fanart.jpg' , '' )
 ii11i1iIII ( '[COLORgreen]Premier League[/COLOR]' , 'http://www.fullmatchesandshows.com/premier-league/' , 10011 , 'https://footballseasons.files.wordpress.com/2013/05/premier-league.png' , OOooO0OOoo + 'fanart.jpg' , '' )
 ii11i1iIII ( '[COLORgreen]La Liga[/COLOR]' , 'http://www.fullmatchesandshows.com/la-liga/' , 10011 , 'http://1.bp.blogspot.com/-c6kQ40ryhyo/U19cUlz25sI/AAAAAAAABak/qtn5chSFZm0/s1600/la-liga-logo_display_image.png' , OOooO0OOoo + 'fanart.jpg' , '' )
 ii11i1iIII ( '[COLORgreen]Bundesliga[/COLOR]' , 'http://www.fullmatchesandshows.com/bundesliga/' , 10011 , 'http://m.img.brothersoft.com/iphone/189/518670189_icon175x175.jpg' , OOooO0OOoo + 'fanart.jpg' , '' )
 ii11i1iIII ( '[COLORgreen]Champions League[/COLOR]' , 'http://www.fullmatchesandshows.com/champions-league/' , 10011 , 'http://www.ecursuri.ro/images/teste/test-champions-league.jpg' , OOooO0OOoo + 'fanart.jpg' , '' )
 ii11i1iIII ( '[COLORgreen]Serie A[/COLOR]' , 'http://www.fullmatchesandshows.com/category/serie-a/' , 10011 , 'http://files.jcriccione.it/200000223-2484526782/serie%20a.png' , OOooO0OOoo + 'fanart.jpg' , '' )
 ii11i1iIII ( '[COLORgreen]Ligue 1[/COLOR]' , 'http://www.fullmatchesandshows.com/category/ligue-1/' , 10011 , 'http://a1.mzstatic.com/us/r30/Purple5/v4/37/c7/44/37c744ae-5824-42b7-6ce0-5f471f52baab/icon180x180.jpeg' , OOooO0OOoo + 'fanart.jpg' , '' )
 ii11i1iIII ( '[COLORgreen]Copa America 2015[/COLOR]' , 'http://www.fullmatchesandshows.com/copa-america-2015/' , 10011 , 'https://pbs.twimg.com/profile_images/521966985907691520/Nq9OAPIo_400x400.png' , OOooO0OOoo + 'fanart.jpg' , '' )
 ii11i1iIII ( '[COLORgreen]CONCACAF[/COLOR]' , 'http://www.fullmatchesandshows.com/category/concacaf/' , 10011 , 'http://a3.mzstatic.com/us/r30/Purple3/v4/40/26/14/4026147c-7022-4ca3-504e-e78950cc3f1c/icon175x175.png' , OOooO0OOoo + 'fanart.jpg' , '' )
 ii11i1iIII ( '[COLORgreen]Women World Cup[/COLOR]' , 'http://www.fullmatchesandshows.com/category/women-world-cup/' , 10011 , 'https://upload.wikimedia.org/wikipedia/en/thumb/7/76/2015_FIFA_Women\'s_World_Cup_logo.svg/967px-2015_FIFA_Women\'s_World_Cup_logo.svg.png' , OOooO0OOoo + 'fanart.jpg' , '' )
 if 19 - 19: OoOoOO00 * IIII + o00O0oo
def O0o ( url ) :
 o0000oO = oooooOoo0ooo ( url )
 III1iII1I1ii = re . compile ( 'itemprop="image" class="entry-thumb" src="(.+?)".+?<h3 itemprop="name" class="entry-title td-module-title"><a itemprop="url" href="(.+?)" rel="bookmark" title=".+?">(.+?)</a></h3>' , re . DOTALL ) . findall ( o0000oO )
 for iiIiIIIiiI , url , oOOo0 in III1iII1I1ii :
  oO00oO = oOOo0 . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' )
  iii1 ( '[COLORgreen]' + oO00oO + '[/COLOR]' , url , 10013 , iiIiIIIiiI )
  if 36 - 36: OoOO0ooOOoo0O
def O0oii111 ( url ) :
 o0000oO = oooooOoo0ooo ( url )
 III1iII1I1ii = re . compile ( '<script data-config="(.+?)" data-height' ) . findall ( o0000oO )
 for IIIII1II in III1iII1I1ii :
  O0OO0oOoO0O0O = ( IIIII1II ) . replace ( '/v2' , '' ) . replace ( 'zeus.json' , 'video-sd.mp4?hosting_id=21772' ) . replace ( 'config.playwire.com' , 'cdn.video.playwire.com' )
  II11iIIiiiII ( 'http:' + O0OO0oOoO0O0O )
  if 99 - 99: OoOO
  if 16 - 16: IIII * I1IiI . o0oO0 / i1IIi . Ooo00oOo00o - i1IIi
def I1IiIIi ( ) :
 Iiii1i1 = OO ( oOo0oooo00o ( 'aHR0cDovL2pvaG5sb2NrZXIuY29tLw==' ) )
 III1iII1I1ii = re . compile ( '<li id="menu-item-.+?" class=".+?"><a href="(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( Iiii1i1 )
 for oo000o , oOOo0 in III1iII1I1ii :
  o0OoOO000ooO0 ( oOOo0 , oo000o , 8046 , OOooO0OOoo + 'documentary.png' )
def IiOOo00 ( url ) :
 Iiii1i1 = OO ( url )
 III1iII1I1ii = re . compile ( 'data-type="inline" href="(.+?)" >.+?src="(.+?)" class="entry-thumbnail wp-post-image" alt="(.+?)" itemprop="image"' , re . DOTALL ) . findall ( Iiii1i1 )
 oOOOoo00 = re . compile ( 'class="inactive">.+?</a><a href="(.+?)">Next</a></div>' , re . DOTALL ) . findall ( Iiii1i1 )
 for url , iiIiIIIiiI , oOOo0 in III1iII1I1ii :
  iii1 ( ( oOOo0 ) . replace ( '&#8211;' , '-' ) . replace ( '&#8217;' , '' ) , url , 8047 , iiIiIIIiiI )
 for url in oOOOoo00 :
  o0OoOO000ooO0 ( 'NEXT PAGE' , url , 8046 , OOooO0OOoo + 'documentary.png' )
  if 37 - 37: i1IIi
def III1i1iI1 ( url ) :
 Iiii1i1 = OO ( url )
 III1iII1I1ii = re . compile ( "src='http://www.youtube.com/embed/(.+?)?version=3&#038;rel=1&#038;fs=1&#038;autohide=2&#038;showsearch=0&#038;showinfo=1&#038;iv_load_policy=1&#038;wmode=transparent' frameborder='0' allowfullscreen='true'></iframe>" ) . findall ( Iiii1i1 )
 for url in III1iII1I1ii :
  yt . PlayVideo ( url )
  if 97 - 97: o0000oOoOoO0o - i11iIiiIii
def i1iIi1II11 ( ) :
 Iiii1i1 = OO ( oOo0oooo00o ( 'aHR0cDovL3RvcGRvY3VtZW50YXJ5ZmlsbXMuY29tLw==' ) )
 III1iII1I1ii = re . compile ( '<a href="(.+?)" >(.+?)</a></li><li>' ) . findall ( Iiii1i1 )
 for oo000o , oOOo0 in III1iII1I1ii :
  o0OoOO000ooO0 ( oOOo0 , oo000o , 8041 , OOooO0OOoo + 'documentary.png' )
def i1I1II1iIIi11 ( url ) :
 Iiii1i1 = OO ( url )
 III1iII1I1ii = re . compile ( '<h2><a href="(.+?)" title="(.+?)">.+?</a></h2>.+?src="(.+?)"' , re . DOTALL ) . findall ( Iiii1i1 )
 oOOOoo00 = re . compile ( 'class="inactive">.+?</a><a href="(.+?)">Next</a></div>' , re . DOTALL ) . findall ( Iiii1i1 )
 for url , oOOo0 , iiIiIIIiiI in III1iII1I1ii :
  o0OoOO000ooO0 ( ( oOOo0 ) . replace ( '&#039;s' , '' ) , url , 8042 , iiIiIIIiiI )
 for url in oOOOoo00 :
  o0OoOO000ooO0 ( 'NEXT PAGE' , url , 8041 , OOooO0OOoo + 'documentary.png' )
  if 49 - 49: OoooooooOO * o0000oOoOoO0o - Oo . OoOO
  if 89 - 89: o0oO0 + o00O0oo * o0oO0 / o0oO0
def i11i11 ( url ) :
 Iiii1i1 = OO ( url )
 III1iII1I1ii = re . compile ( '<meta itemprop="name" content="(.+?)".+?<meta itemprop="thumbnailUrl" content="(.+?)".+?<meta itemprop="embedUrl" content="(.+?)".+?<meta itemprop="description" content="(.+?)" />' , re . DOTALL ) . findall ( Iiii1i1 )
 oOOOoo00 = re . compile ( '<div class="video new-video"><iframe width="766" height="431" src="(.+?)&amp;iv_load_policy=3&amp;showinfo=0&amp;autohide=1"' , re . DOTALL ) . findall ( Iiii1i1 )
 for oOOo0 , iiIiIIIiiI , url , OoOoO00O0 in III1iII1I1ii :
  iii1 ( ( oOOo0 ) . replace ( '&#039;s' , '' ) , url . replace ( 'https://www.youtube.com/embed/' , '' ) , 8043 , iiIiIIIiiI )
 for url in oOOOoo00 :
  OoOOO ( ( url ) . replace ( '//' , 'http://' ) )
  if 67 - 67: oO0o0ooO0 % oO0o0ooO0 / oO0o0ooO0
def OoOOO ( url ) :
 Iiii1i1 = OO ( url )
 III1iII1I1ii = re . compile ( '<link rel="canonical" href="(.+?)">  <link rel="stylesheet"' ) . findall ( Iiii1i1 )
 for url in III1iII1I1ii :
  iii1 ( 'PLAY' , ( url ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , OOooO0OOoo + 'documentary.png' )
  if 53 - 53: iIii1I11I1II1
def oooo00o0o0o ( ) :
 o0000oO = OO ( 'http://www.stream2watch.co/live-tv' )
 III1iII1I1ii = re . compile ( '<a href="(.+?)">.+?<img src="(.+?)" alt=".+?"/>.+?<span class="country_name">(.+?)<br />(.+?)</span>' , re . DOTALL ) . findall ( o0000oO )
 for oo000o , iiIiIIIiiI , oOOo0 , O0Oo00oO0O00 in III1iII1I1ii :
  o0OoOO000ooO0 ( ( oOOo0 + '[COLORgreen]' + O0Oo00oO0O00 + '[/COLOR]' ) , oo000o , 8086 , iiIiIIIiiI )
  if 32 - 32: OoOoOO00 . o00O0oo - oO0o0ooO0 * O0oO
def OOO00oo0ooO ( url ) :
 o0000oO = OO ( url )
 III1iII1I1ii = re . compile ( '<a class="front_channel_href" href="(.+?)" title=".+?">.+?<img class="front_channel_thumb" src="(.+?)" alt=".+?"/>.+?<span class="front_channel_name">(.+?)</span>' , re . DOTALL ) . findall ( o0000oO )
 for url , iiIiIIIiiI , oOOo0 in III1iII1I1ii :
  o0OoOO000ooO0 ( '[COLORgreen]' + oOOo0 + '[/COLOR]' , url , 8087 , iiIiIIIiiI )
  if 38 - 38: iIii1I11I1II1 - OoOoOO00 - OOOo0
def ooo ( url ) :
 o0000oO = oooooOoo0ooo ( url )
 III1iII1I1ii = re . compile ( 'a id="code_.+?data-f-href="(.+?)" data-code-embed="">(.+?)</a>' , re . DOTALL ) . findall ( o0000oO )
 for url , oOOo0 in III1iII1I1ii :
  OOOO0oooo ( url , oOOo0 )
  if 51 - 51: O0 - i1IIi / OOOo0
def OOOO0oooo ( url , name ) :
 o0000oO = oooooOoo0ooo ( url )
 III1iII1I1ii = re . compile ( "playStream\('.+?', '(.+?)'\);" , re . DOTALL ) . findall ( o0000oO )
 for url in III1iII1I1ii :
  print url
  iii1 ( '[COLORgreen]' + name + '[/COLOR]' , url , 222 , '' )
  if 37 - 37: OOooOOo % o0oO0
def O0II11i11II ( ) :
 Iiii1i1 = OO ( oOo0oooo00o ( 'aHR0cDovL2JyYXR1LW1hcmlhbi5yby8=' ) )
 III1iII1I1ii = re . compile ( '<tr><td ><img width="25" height="25" src="(.+?)" alt="" /> </td>.+?<td >(.+?)</td>.+?<td >(.+?)</td>.+?<td >(.+?)</td>.+?<td >(.+?)</td>.+?<td >    <a class="wp-colorbox-youtube" href="(.+?)">Watch Online</a></td>.+?</tr>' , re . DOTALL ) . findall ( Iiii1i1 )
 for iiIiIIIiiI , time , II1Ii1iI1i1 , OOOoO , IIi1IIIIi , oo000o in III1iII1I1ii :
  o0OoOO000ooO0 ( ( time + '[COLORgreen]' + IIi1IIIIi + '[/COLOR]' + OOOoO ) . replace ( '&#8211;' , ':' ) . replace ( '&ndash;' , '-' ) , oo000o , 8061 , iiIiIIIiiI )
def o0OoO000O ( url ) :
 Iiii1i1 = OO ( url )
 III1iII1I1ii = re . compile ( 'type:.+?,.+?url: "(.+?)"' , re . DOTALL ) . findall ( Iiii1i1 )
 for url in III1iII1I1ii :
  iii1 ( '[COLORgreen]LINK 1[/COLOR]' , url , 222 , OOooO0OOoo + 'documentary.png' )
  if 94 - 94: I1IiI . O0 / o00O0oo . ii11ii1ii - i1IIi
def iIi1III1I ( ) :
 o0000oO = oooooOoo0ooo ( oOo0oooo00o ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vbTN1c3RyZWFtcw==' ) )
 III1iII1I1ii = re . compile ( '<li><a href="(.+?)"> (.+?).m3u</a></li>' ) . findall ( o0000oO )
 for oo000o , oOOo0 in III1iII1I1ii :
  o0OoOO000ooO0 ( ( '[COLORgreen]' + oOOo0 + '[/COLOR]' ) . replace ( '-' , ' ' ) . replace ( '_' , ' ' ) , ( oOo0oooo00o ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vbTN1c3RyZWFtcy8=' ) ) + oo000o , 8071 , OOooO0OOoo + 'streams.png' )
def oo0oo0OOOOOoO ( url ) :
 o0000oO = OO ( url )
 III1iII1I1ii = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( o0000oO )
 for oOOo0 , url in III1iII1I1ii :
  iii1 ( ( '[COLORgreen]' + oOOo0 + '[/COLOR]' ) . replace ( '_' , ' ' ) , ( url ) . strip ( ) , 404 , OOooO0OOoo + 'streams.png' )
  if 80 - 80: iIii1I11I1II1 * O0oO % o0000oOoOoO0o % Oo
def OooOO0o0 ( url ) :
 oOOoo0 = urllib2 . Request ( url )
 oOOoo0 . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
 i1111IIiii1 = ''
 O0ii1ii1ii = ''
 try :
  i1111IIiii1 = urllib2 . urlopen ( oOOoo0 )
  O0ii1ii1ii = i1111IIiii1 . read ( )
  i1111IIiii1 . close ( )
 except : pass
 if O0ii1ii1ii != '' :
  return O0ii1ii1ii
 else :
  O0ii1ii1ii = 'Failed'
  return O0ii1ii1ii
  if 49 - 49: OoOO0ooOOoo0O . iIii1I11I1II1
def OOOoOoOooo ( ) :
 oo00OOoOoO00 = ( oOo0oooo00o ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 iiIi11iI1iii = Oo0o0000o0o0 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oo000 = iiIi11iI1iii . lower ( )
 oo000o = ( oOo0oooo00o ( 'aHR0cDovL2RsNC5tb3ZpZWZhcnNpLmNvbS9maWxtLzIwMTUtNy8=' ) )
 oOOOO = ( oOo0oooo00o ( 'aHR0cDovL2RsLmF2YWRsLmNvbS9OZXcvTW92aWUv' ) )
 I1iii = ( oOo0oooo00o ( 'aHR0cDovLzIxNy4yMTkuMTQzLjEwOC8xMzI3Lw==' ) )
 oOO0OO0O = ( oOo0oooo00o ( 'aHR0cDovLzE3OC4xNjIuMjE0LjIzMi92b2QvbW92aWVzL2VuZ2xpc2gv' ) )
 o00o = ( oOo0oooo00o ( 'aHR0cDovL3Njb29ieXN0cmVhbS54MTBob3N0LmNvbS8vc2Nvb2J5L21vdi9hbGwucGhw' ) )
 III11I = ( oOo0oooo00o ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 Ii1I11I = ( oOo0oooo00o ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL3NlYXJjaC8/cT0=' ) ) + iiIi11iI1iii
 iiIii1I = ( oOo0oooo00o ( 'aHR0cDovL2xldHdhdGNoLnVzLz9vcD1zZWFyY2gmaz0=' ) ) + ( iiIi11iI1iii ) . replace ( ' ' , '+' )
 if 47 - 47: o0oO0 . o0000oOoOoO0o / OOooOOo
 o0000oO = OooOO0o0 ( oo000o )
 i1IiII1III = OooOO0o0 ( oOOOO )
 OOoOO = OooOO0o0 ( I1iii )
 OO0OO0OO = OooOO0o0 ( oOO0OO0O )
 OoooO0o = OooOO0o0 ( o00o )
 IIIii1iiIi = OooOO0o0 ( Ii1I11I )
 oooo0OOo = oooooOoo0ooo ( iiIii1I )
 if 72 - 72: O0 / o0oO0 + OoooooooOO * oO0o0ooO0
 if o0000oO != 'Failed' :
  III1iII1I1ii = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( o0000oO )
  for OoOo0OOOoOo , oOOo0 in III1iII1I1ii :
   if iiIi11iI1iii in oOOo0 . lower ( ) :
    iii1 ( ( oOOo0 + '[COLORgreen] source 1[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( oo000o + OoOo0OOOoOo ) , 222 , '' )
 if i1IiII1III != 'Failed' :
  oOOOoo00 = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( i1IiII1III )
  for OoOo0OOOoOo , oOOo0 in oOOOoo00 :
   if iiIi11iI1iii in oOOo0 . lower ( ) :
    iii1 ( ( oOOo0 + '[COLORgreen] source 2[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( oOOOO + OoOo0OOOoOo ) , 222 , '' )
 if OOoOO != 'Failed' :
  iIi1I11I = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( OOoOO )
  for OoOo0OOOoOo , oOOo0 in iIi1I11I :
   if iiIi11iI1iii in oOOo0 . lower ( ) :
    iii1 ( ( oOOo0 + '[COLORgreen] source 3[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( I1iii + OoOo0OOOoOo ) , 222 , '' )
 if OO0OO0OO != 'Failed' :
  IIiiIIi1 = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( OO0OO0OO )
  for OoOo0OOOoOo , oOOo0 in IIiiIIi1 :
   if iiIi11iI1iii in oOOo0 . lower ( ) :
    iii1 ( ( oOOo0 + '[COLORgreen] source 4[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( oOO0OO0O + OoOo0OOOoOo ) , 222 , '' )
 if OoooO0o != 'Failed' :
  ooO000O = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( OoooO0o )
  for OoOo0OOOoOo , iiIiIIIiiI , oOOo0 in ooO000O :
   if iiIi11iI1iii in oOOo0 . lower ( ) :
    o0OoOO000ooO0 ( ( oOOo0 + '[COLORgreen] source Scooby[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( 'Ganool' , '' ) . replace ( 'ShAaNiG' , '' ) . replace ( 'YIFY' , '' ) . replace ( '[[ Max-Movie.In ]]' , '' ) . replace ( '.mkv' , '' ) . replace ( '.mp4' , '' ) . replace ( '.' , ' ' ) , ( OoOo0OOOoOo ) , 1006 , 'img' )
    if 53 - 53: OOooOOo . oO0o0ooO0 / o00O0oo
    III1ii1iII ( 'tvshows' , 'Media Info 3' )
 if IIIii1iiIi != 'Failed' :
  I11iiIi1i1 = re . compile ( 'href="(.+?)".+?src="(.+?)" alt="Image of (.+?)"' , re . DOTALL ) . findall ( IIIii1iiIi )
  for OoOo0OOOoOo , iiIiIIIiiI , oOOo0 in I11iiIi1i1 :
   if iiIi11iI1iii in oOOo0 . lower ( ) :
    o0OoOO000ooO0 ( ( '[COLORgreen]' + oOOo0 + '- source Snag[/COLOR]' ) . replace ( '&#x27;' , '' ) , 'http://www.snagfilms.com' + oo000o , 7067 , iiIiIIIiiI )
    if 41 - 41: o00O0oo % ii11ii1ii
    III1ii1iII ( 'tvshows' , 'Media Info 3' )
 if oooo0OOo != 'Failed' :
  i1iIiIi1I = re . compile ( '<div class="video_block video_block_default ">.+?<a href="#">.+?<a href="(.*?)".+?<img src="(.+?)" height=".+?" alt="(.+?)"' , re . DOTALL ) . findall ( oooo0OOo )
  for oo000o , iiIiIIIiiI , oOOo0 in i1iIiIi1I :
   iii1 ( oOOo0 + ' - Source 7' , oo000o , 222 , iiIiIIIiiI )
 i11i11111i1i = [ '0-9/' , 'A/' , 'B/' , 'C/' , 'D/' , 'E/' , 'F/' , 'G/' , 'H/' , 'I/' , 'J/' , 'K/' , 'L/' , 'M/' , 'N/' , 'O/' , 'P/' , 'R/' , 'S/' , 'T/' , 'U/' , 'V/' , 'W/' , 'X/' , 'Y/' , 'Z/' ]
 if 37 - 37: o00O0oo % Ooo00oOo00o
 if 79 - 79: ii11ii1ii + OOOo0 / OOOo0
 for I1I1i in i11i11111i1i :
  I1IIIiIiIi = oo00OOoOoO00 + I1I1i
  OO0O0ooOOO00 = OooOO0o0 ( I1IIIiIiIi )
  if OoooO0o != 'Failed' :
   IiIiiiiI1 = re . compile ( '<li><a href="(.+?)"> (.+?)</a></li>' ) . findall ( OO0O0ooOOO00 )
   for OoOo0OOOoOo , oOOo0 in IiIiiiiI1 :
    if iiIi11iI1iii in oOOo0 . lower ( ) :
     iii1 ( ( oOOo0 + '[COLORgreen] source 5[/COLOR]' ) . replace ( 'Ganool' , '' ) . replace ( 'ShAaNiG' , '' ) . replace ( 'YIFY' , '' ) . replace ( '[[ Max-Movie.In ]]' , '' ) . replace ( '.mkv' , '' ) . replace ( '.mp4' , '' ) . replace ( '.' , ' ' ) , ( oo00OOoOoO00 + I1I1i + OoOo0OOOoOo ) , 222 , '' )
     if 62 - 62: ii11ii1ii % oO0o0ooO0 * Ooo00oOo00o - i1IIi
     III1ii1iII ( 'tvshows' , 'Media Info 3' )
     if 66 - 66: i11iIiiIii / OOooOOo - OoooooooOO / i1IIi . i11iIiiIii
     if 16 - 16: Oo % ii11ii1ii + o0000oOoOoO0o - O0 . oO0o0ooO0 / O0oO
def IIi1I ( ) :
 if 27 - 27: O0 . O0oO / oO0o0ooO0
 iiIi11iI1iii = Oo0o0000o0o0 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oo000 = iiIi11iI1iii . lower ( )
 oo000o = ( oOo0oooo00o ( 'aHR0cDovL2RsLmZhcnNpbW92aWUubmV0L1NlcmlhbC8=' ) )
 oOOOO = ( oOo0oooo00o ( 'aHR0cDovL3N2Mi5kbC1wYXJzLmluLw==' ) )
 I1iii = ( oOo0oooo00o ( 'aHR0cDovL3R2LmRsLXBhcnMuaW4v' ) )
 oOO0OO0O = ( oOo0oooo00o ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9BbWVyaWNhbiUyMFNlcmlhbC8=' ) )
 o00o = ( oOo0oooo00o ( 'aHR0cDovL2RpemlsYWIuY29tL2Fyc2l2P2xpbWl0PSZ0dXI9Jm9yZGVyYnk9JnVsa2U9Jm9yZGVyPSZ5aWw9JmRpemlfYWRpPQ==' ) ) + ( iiIi11iI1iii ) . replace ( ' ' , '+' )
 III11I = ( oOo0oooo00o ( 'aHR0cDovL3Njb29ieXN0cmVhbS54MTBob3N0LmNvbS8vc2Nvb2J5L3Nob3dzL3R2YWxsLnBocA==' ) )
 iiIii1I = ( oOo0oooo00o ( 'aHR0cDovL2xldHdhdGNoLnVzLz9vcD1zZWFyY2gmaz0=' ) ) + ( iiIi11iI1iii ) . replace ( ' ' , '+' )
 if 96 - 96: ii11ii1ii % o0oO0 % o00O0oo - o0oO0 % I1IiI + ii11ii1ii
 o0000oO = OooOO0o0 ( oo000o )
 i1IiII1III = OooOO0o0 ( oOOOO )
 OOoOO = OooOO0o0 ( I1iii )
 OO0OO0OO = OooOO0o0 ( oOO0OO0O )
 OoooO0o = cloudflare . source ( o00o )
 OO0O0ooOOO00 = OooOO0o0 ( III11I )
 oooo0OOo = oooooOoo0ooo ( iiIii1I )
 if o0000oO != 'Failed' :
  III1iII1I1ii = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( o0000oO )
  for oOOo0 in III1iII1I1ii :
   if iiIi11iI1iii in oOOo0 . lower ( ) :
    o0OoOO000ooO0 ( ( oOOo0 + ' source 1' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( oo000o + oOOo0 ) . replace ( ' ' , '%20' ) , 1006 , '' )
    if 3 - 3: O0
    III1ii1iII ( 'tvshows' , 'Media Info 3' )
 if i1IiII1III != 'Failed' :
  oOOOoo00 = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( i1IiII1III )
  for oOOo0 in oOOOoo00 :
   if iiIi11iI1iii in oOOo0 . lower ( ) :
    o0OoOO000ooO0 ( ( oOOo0 + ' source 2' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( oOOOO + oOOo0 ) . replace ( ' ' , '%20' ) , 1006 , '' )
    if 64 - 64: i1IIi % o0oO0 / i11iIiiIii - i1IIi % OoOO0ooOOoo0O . oO0o0ooO0
    III1ii1iII ( 'tvshows' , 'Media Info 3' )
 if OOoOO != 'Failed' :
  iIi1I11I = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( OOoOO )
  for oOOo0 in oOOOoo00 :
   if iiIi11iI1iii in oOOo0 . lower ( ) :
    o0OoOO000ooO0 ( ( oOOo0 + ' source 3' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( I1iii + oOOo0 ) . replace ( ' ' , '%20' ) , 1006 , '' )
    if 8 - 8: Oo + OoOoOO00 * OoOO0ooOOoo0O * I1IiI * o0000oOoOoO0o / IIII
    III1ii1iII ( 'tvshows' , 'Media Info 3' )
 if OO0OO0OO != 'Failed' :
  IIiiIIi1 = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( OO0OO0OO )
  for oOOo0 in oOOOoo00 :
   if iiIi11iI1iii in oOOo0 . lower ( ) :
    o0OoOO000ooO0 ( ( oOOo0 + ' source 4' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( oOO0OO0O + oOOo0 ) . replace ( ' ' , '%20' ) , 1006 , '' )
    if 21 - 21: OoOO / OoooooooOO
    III1ii1iII ( 'tvshows' , 'Media Info 3' )
 if OoooO0o != 'Failed' :
  ooO000O = re . compile ( '<a href="(.+?)" class="film-image">\n<img src="(.+?)" alt=""/>\n</a>\n<div class="tss-detail">\n<a class="title" style="" href=".+?">\n<span class="position">.+?</span>\n(.+?)</a>' ) . findall ( OoooO0o )
  for oo000o , iiIiIIIiiI , oOOo0 in ooO000O :
   if iiIi11iI1iii in oOOo0 . lower ( ) :
    o0OoOO000ooO0 ( oOOo0 + ' - Source - Dizi' , oo000o , 8062 , iiIiIIIiiI )
    if 11 - 11: OoOO0ooOOoo0O % o00O0oo - i11iIiiIii - OoOO + o0oO0 + IIII
    III1ii1iII ( 'tvshows' , 'Media Info 3' )
 if OO0O0ooOOO00 != 'Failed' :
  IiIiiiiI1 = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( OO0O0ooOOO00 )
  for oo000o , iiIiIIIiiI , oOOo0 in IiIiiiiI1 :
   if iiIi11iI1iii in oOOo0 . lower ( ) :
    iii1 ( ( oOOo0 + '[COLORgreen] source Scooby[/COLOR]' ) , oo000o , 222 , 'img' )
    if 87 - 87: O0oO * i1IIi / ii11ii1ii
    III1ii1iII ( 'tvshows' , 'Media Info 3' )
 if oooo0OOo != 'Failed' :
  i1iIiIi1I = re . compile ( '<div class="video_block video_block_default ">.+?<a href="#">.+?<a href="(.*?)".+?<img src="(.+?)" height=".+?" alt="(.+?)"' , re . DOTALL ) . findall ( oooo0OOo )
  for oo000o , iiIiIIIiiI , oOOo0 in i1iIiIi1I :
   iii1 ( oOOo0 + ' - Source 7' , oo000o , 222 , iiIiIIIiiI )
def IIII1i1 ( ) :
 if 70 - 70: i11iIiiIii % ii11ii1ii / OOOo0
 iiIi11iI1iii = Oo0o0000o0o0 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oo000 = iiIi11iI1iii . lower ( )
 oo000o = ( oOo0oooo00o ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz' ) )
 o0000oO = oooooOoo0ooo ( oo000o )
 III1iII1I1ii = re . compile ( '"id":".+?","name":"(.+?)","img":"(.+?)","stream_url3":".+?","cat_id":"(.+?)","stream_url2":".+?","stream_url":".+?"}' , re . DOTALL ) . findall ( o0000oO )
 for oOOo0 , iiIiIIIiiI , ooOOOOo0 in III1iII1I1ii :
  IiiIi = oOo0oooo00o ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv' ) + ( iiIiIIIiiI ) . replace ( '\\' , '' )
  if iiIi11iI1iii in oOOo0 . lower ( ) :
   o0OoOO000ooO0 ( oOOo0 , '' , 7022 , IiiIi )
   if 10 - 10: Ooo00oOo00o / Oo
 xbmcplugin . addSortMethod ( O0o0Oo , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 15 - 15: oO0o0ooO0 . I1IiI / oO0o0ooO0 * o0000oOoOoO0o - OOOo0 % ii11ii1ii
 if 57 - 57: O0 % I1IiI % OoOO
def iI1iii ( url ) :
 OOOo = cloudflare . source ( url )
 III1iII1I1ii = re . compile ( '<a class="season" href="(.+?)">\n(.+?)\n</a>\n</span>\n<span>\n<a class="episode" href=".+?">\n(.+?)\n</a>\n</span>\n<span>\n<a class="episode-name" href=".+?">\n(.+?)</a>' ) . findall ( OOOo )
 for url , Ii , I1Ii1111iIi , oOOo0 in III1iII1I1ii :
  o0OoOO000ooO0 ( ( Ii ) . replace ( 'Sezon' , ' Season ' ) + ( I1Ii1111iIi ) . replace ( 'Bölüm' , ' Episode ' ) + oOOo0 , url , 8063 , '' )
  if 79 - 79: I1IiI % IIII % Oo
  if 29 - 29: OoooooooOO . OOOo0 % ii11ii1ii - oO0o0ooO0
  if 8 - 8: i1IIi
  if 32 - 32: OoOO / OoOoOO00
def II1Iii ( url ) :
 OOOo = cloudflare . source ( url )
 III1iII1I1ii = re . compile ( 'file: "(.+?)",.+?label: "(.+?)",' , re . DOTALL ) . findall ( OOOo )
 for url , oOOo0 in III1iII1I1ii :
  iii1 ( oOOo0 , url , 222 , '' )
  if 73 - 73: o0000oOoOoO0o * OoooooooOO . O0 . IIII
  if 55 - 55: Oo
  if 77 - 77: OoOoOO00
  if 16 - 16: OOOo0 * OoOoOO00 / iIii1I11I1II1 - oO0o0ooO0
def IiI1IiI11iII ( ) :
 if 64 - 64: OoOO - OOOo0 / oO0o0ooO0 - Ooo00oOo00o
 OOOo = cloudflare . source ( oOo0oooo00o ( 'aHR0cDovL2RpemlsYWIuY29t' ) )
 III1iII1I1ii = re . compile ( '<li id=".+?">.+?<a href="(.+?)">.+?<img width="40" height="40" src="(.+?)" alt=""/>.+?<span class="title">\n(.+?)</span>.+?<span class="alt-title">\n(.+?)</span>.+?</a>.+?</li>' , re . DOTALL ) . findall ( OOOo )
 for oo000o , iiIiIIIiiI , oOOo0 , I1Ii1111iIi in III1iII1I1ii :
  o0OoOO000ooO0 ( oOOo0 + '  -  ' + ( I1Ii1111iIi ) . replace ( 'sezon' , 'Season' ) . replace ( 'bölüm' , 'Episode' ) , oo000o , 8063 , iiIiIIIiiI )
  if 37 - 37: i11iIiiIii / oO0o0ooO0
def oo00OoO ( ) :
 Iiii1i1 = OO ( oOo0oooo00o ( 'aHR0cDovL3d3dy50dmd1aWRlLmNvLnVrLw==' ) )
 III1iII1I1ii = re . compile ( '<a href="(.+?)"  qt-title=".+?" qt-text=".+?<br> .+?" title="(.+?)".+?class=".+? src="(.+?)" alt=".+?" /></a>' , re . DOTALL ) . findall ( Iiii1i1 )
 for oo000o , oOOo0 , iiIiIIIiiI in III1iII1I1ii :
  iii1 ( '[COLORgreen]' + oOOo0 + '[/COLOR]' , oo000o , 8002 , iiIiIIIiiI )
def iIIi1IIi ( url ) :
 Iiii1i1 = OO ( url )
 III1iII1I1ii = re . compile ( '<table border="0".+?url((.+?));background-repeat: no-repeat;">.+?<tr>.+?<span class="season">(.+?)</span><br>.+?<a href="(.+?)"+?>(.+?)</span><br>.+?<span class="programmetext">(.+?)</span></a><br>' , re . DOTALL ) . findall ( Iiii1i1 )
 for iiIiIIIiiI , time , url , oOOo0 , OoOoO00O0 in III1iII1I1ii :
  ii11i1iIII ( '%s %s' % ( '[COLORgreen]' + oOOo0 + '[/COLOR]' , time ) , url , 1015 , iiIiIIIiiI , OoOoO00O0 )
  if 43 - 43: O0oO % oO0o0ooO0
def o0O0ooOOoO ( ) :
 if 19 - 19: i11iIiiIii
 o0OoOO000ooO0 ( 'Coronation Street' , '' , 8001 , '' )
 o0OoOO000ooO0 ( 'Eastenders' , '' , 8002 , '' )
 o0OoOO000ooO0 ( 'Emmerdale' , '' , 8003 , '' )
 o0OoOO000ooO0 ( 'Hollyoaks' , '' , 8004 , '' )
 o0OoOO000ooO0 ( 'Im a Celebrity' , '' , 8005 , '' )
 if 54 - 54: OoOoOO00 . o0000oOoOoO0o
 if 73 - 73: I1IiI . OOOo0
 if 32 - 32: I1IiI * OOOo0 % o0oO0 * o00O0oo . O0
 if 48 - 48: oO0o0ooO0 * oO0o0ooO0
def I1I1 ( ) :
 o0000oO = oooooOoo0ooo ( 'http://uksoapshare.blogspot.co.uk/' )
 III1iII1I1ii = re . compile ( '<a href="(.+?)".+?target=_blank>(.+?)</a>' ) . findall ( o0000oO )
 for oo000o , oOOo0 in III1iII1I1ii :
  if 'Holly' in oOOo0 :
   iiIiIIIiiI = 'http://2.bp.blogspot.com/-9c7Sieh1RKs/UjD6TGAEEnI/AAAAAAAAAC8/84uwHfxcuYg/s1600/Hollyoaks.png'
   if 'huge' in oo000o :
    iii1 ( ( oOOo0 ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , oo000o . replace ( '\\/' , '/' ) , 8006 , iiIiIIIiiI )
   else :
    pass
    if 4 - 4: OOooOOo % I1IiI * OoOO0ooOOoo0O
 xbmcplugin . addSortMethod ( O0o0Oo , xbmcplugin . SORT_METHOD_TITLE_IGNORE_THE ) ;
 if 32 - 32: i11iIiiIii - O0oO
def oo00ooOoo ( ) :
 o0000oO = oooooOoo0ooo ( 'http://uksoapshare.blogspot.co.uk/' )
 III1iII1I1ii = re . compile ( '<a href="(.+?)".+?target=_blank>(.+?)</a>' ) . findall ( o0000oO )
 for oo000o , oOOo0 in III1iII1I1ii :
  if 'East' in oOOo0 :
   iiIiIIIiiI = 'http://3.bp.blogspot.com/-KWHcNbNJU8Y/Vi1ousRl7fI/AAAAAAAAAT8/ksNE12LH0nE/s1600/eastenders.jpg'
   if 'huge' in oo000o :
    iii1 ( ( oOOo0 ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , oo000o . replace ( '\\/' , '/' ) , 8006 , iiIiIIIiiI )
   else :
    pass
    if 28 - 28: o00O0oo
 xbmcplugin . addSortMethod ( O0o0Oo , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 1 - 1: o00O0oo
def IiiiI1 ( ) :
 o0000oO = oooooOoo0ooo ( 'http://uksoapshare.blogspot.co.uk/' )
 III1iII1I1ii = re . compile ( '<a href="(.+?)".+?target=_blank>(.+?)</a>' ) . findall ( o0000oO )
 for oo000o , oOOo0 in III1iII1I1ii :
  if 'Emmer' in oOOo0 :
   iiIiIIIiiI = 'http://2.bp.blogspot.com/-UfDcxisVV5c/UjH9vUicZ3I/AAAAAAAAADc/8Ozuiz1ojxw/s1600/Emmerdale.jpg'
   if 'huge' in oo000o :
    iii1 ( ( oOOo0 ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , oo000o . replace ( '\\/' , '/' ) , 8006 , iiIiIIIiiI )
   else :
    pass
    if 100 - 100: OoOO . o00O0oo % i1IIi . o0oO0
 xbmcplugin . addSortMethod ( O0o0Oo , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 79 - 79: Ooo00oOo00o % OoOO0ooOOoo0O / iIii1I11I1II1 + I1IiI * Ooo00oOo00o
def IiI1 ( ) :
 o0000oO = oooooOoo0ooo ( 'http://uksoapshare.blogspot.co.uk/' )
 III1iII1I1ii = re . compile ( '<a href="(.+?)".+?target=_blank>(.+?)</a>' ) . findall ( o0000oO )
 for oo000o , oOOo0 in III1iII1I1ii :
  if 'Coro' in oOOo0 :
   iiIiIIIiiI = 'http://3.bp.blogspot.com/-hofvfBQVexs/UjErIfNdS4I/AAAAAAAAADQ/Q-vVGu3apYU/s1600/corrie.jpg'
   if 'huge' in oo000o :
    iii1 ( ( oOOo0 ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , oo000o . replace ( '\\/' , '/' ) , 8006 , iiIiIIIiiI )
   else :
    pass
    if 28 - 28: ii11ii1ii * OoooooooOO . OoOoOO00 / i11iIiiIii + OoOO
 xbmcplugin . addSortMethod ( O0o0Oo , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 38 - 38: IIII . o00O0oo
def IIIIIIIiI ( ) :
 o0000oO = oooooOoo0ooo ( 'http://uksoapshare.blogspot.co.uk/' )
 III1iII1I1ii = re . compile ( '<a href="(.+?)" target="_blank">(.+?)</a>' ) . findall ( o0000oO )
 for oo000o , oOOo0 in III1iII1I1ii :
  if 'Celeb' in oOOo0 :
   iiIiIIIiiI = 'http://3.bp.blogspot.com/-a_yDotWU_pY/VkotKWaG_gI/AAAAAAAAAUk/8Q5iNM6p37k/s1600/iacgoh.jpg'
   if 'huge' in oo000o :
    iii1 ( ( oOOo0 ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , oo000o . replace ( '\\/' , '/' ) , 8006 , iiIiIIIiiI )
   else :
    pass
    if 12 - 12: oO0o0ooO0 . IIII . I1IiI / O0
def OO0oOOo0o ( name , url ) :
 I1 = urlresolver . HostedMediaFile ( url ) . valid_url ( )
 if I1 :
  III11iiii11i1 = urlresolver . HostedMediaFile ( url ) . resolve ( )
 else :
  Iiii1i1 = open_url ( url )
  url = re . compile ( 'src="(.+?)"></iframe>' ) . findall ( Iiii1i1 ) [ 0 ]
  url = url . split ( '?autoplay' ) [ 0 ]
  Iiii1i1 = open_url ( url )
  ooOo0OoO = re . compile ( 'mp4","url":"(.+?)"' ) . findall ( Iiii1i1 ) [ - 1 ]
  III11iiii11i1 = ooOo0OoO . replace ( '\\/' , '/' )
 i1i1iII1 = xbmcgui . ListItem ( name , '' , '' )
 i1i1iII1 . setPath ( III11iiii11i1 )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , i1i1iII1 )
 if 36 - 36: IIII - OoooooooOO / Ooo00oOo00o
 if 34 - 34: o0oO0
def i1iI1 ( ) :
 Iiii1i1 = oooooOoo0ooo ( oOo0oooo00o ( 'aHR0cDovL3d3dy5kaXppYm94aGQuY29tLw==' ) )
 III1iII1I1ii = re . compile ( 'class="film menu-item menu-item-type-post_type menu-item-object-page menu-item-36980"><a href="(.+?)"><i class="fa fa-film"></i><span>(.+?)</span></a></li>' ) . findall ( Iiii1i1 )
 oOOOoo00 = re . compile ( 'class="menu-item menu-item-type-post_type menu-item-object-page menu-item-52949"><a href="(.+?)"><i class="fa fa-"></i><span>(.+?)</span></a></li>' ) . findall ( Iiii1i1 )
 for oo000o , oOOo0 in III1iII1I1ii :
  o0OoOO000ooO0 ( ( '[COLORgreen]' + oOOo0 + '[/COLOR]' ) . replace ( 'Diziler' , 'Series' ) , oo000o , 7071 , OOooO0OOoo + 'popcorn.png' )
 for oo000o , oOOo0 in oOOOoo00 :
  o0OoOO000ooO0 ( ( '[COLORgreen]' + oOOo0 + '[/COLOR]' ) . replace ( 'Filmler' , 'Movies' ) , oo000o , 7071 , OOooO0OOoo + 'popcorn.png' )
  if 44 - 44: ii11ii1ii - o00O0oo / OoOoOO00 * Ooo00oOo00o * Oo
def OO0ooo0o0 ( ) :
 Iiii1i1 = oooooOoo0ooo ( oOo0oooo00o ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL2NhdGVnb3JpZXMv' ) )
 III1iII1I1ii = re . compile ( '<a class="nav-item" href="(.+?)">(.+?)</a>' ) . findall ( Iiii1i1 )
 for oo000o , oOOo0 in III1iII1I1ii :
  if 'Movies' in oOOo0 :
   o0OoOO000ooO0 ( '[COLORgreen]' + oOOo0 + '[/COLOR]' , 'http://www.snagfilms.com' + ( oo000o ) . replace ( 'http://www.snagfilms.com' , '' ) , 7061 , OOooO0OOoo + 'popcorn.png' )
def oO0ooOoO ( url ) :
 Iiii1i1 = oooooOoo0ooo ( url )
 III1iII1I1ii = re . compile ( '<a class="object-link size-poster".+?href="(.+?)" data-type="category">.+?src="(.+?)" alt="Image of (.+?)" />' , re . DOTALL ) . findall ( Iiii1i1 )
 III1iII1I1ii = re . compile ( '<a class="object-link size-poster".+?href="(.+?)" data-type="category">.+?src="(.+?)" alt="Image of (.+?)" />' , re . DOTALL ) . findall ( Iiii1i1 )
 oOOOoo00 = re . compile ( "<li class='current'>.+?</li><li ><a href='(.+?)'>.+?</a></li><li" , re . DOTALL ) . findall ( Iiii1i1 )
 for url , iiIiIIIiiI , oOOo0 in III1iII1I1ii :
  o0OoOO000ooO0 ( '[COLORgreen]' + oOOo0 + '[/COLOR]' , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7067 , iiIiIIIiiI )
 for url in oOOOoo00 :
  o0OoOO000ooO0 ( '[COLORgreen]NEXT PAGE[/COLOR]' , ( url ) . replace ( '&#038;' , '&' ) , 7063 , OOooO0OOoo + 'popcorn.png' )
  if 59 - 59: O0 % Oo
  if 92 - 92: o00O0oo % oO0o0ooO0 / ii11ii1ii % ii11ii1ii * OOOo0
def OooO00oOOo0Oo ( url ) :
 Iiii1i1 = oooooOoo0ooo ( oOo0oooo00o ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL2NhdGVnb3JpZXMv' ) )
 III1iII1I1ii = re . compile ( '<a class="object-link size-poster".+?href="(.+?)" data-type="category">.+?src="(.+?)" alt="Image of (.+?)" />' , re . DOTALL ) . findall ( Iiii1i1 )
 for url , iiIiIIIiiI , oOOo0 in III1iII1I1ii :
  o0OoOO000ooO0 ( '[COLORgreen]' + oOOo0 + '[/COLOR]' , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7062 , iiIiIIIiiI )
  if 5 - 5: OOooOOo . O0 / Oo % Ooo00oOo00o
  if 60 - 60: OoOoOO00 / iIii1I11I1II1 + ii11ii1ii . i11iIiiIii
def i1iiIIIi ( url ) :
 Iiii1i1 = oooooOoo0ooo ( url )
 III1iII1I1ii = re . compile ( 'href="(.+?)".+?src="(.+?)" alt="Image of (.+?)"' , re . DOTALL ) . findall ( Iiii1i1 )
 for url , iiIiIIIiiI , oOOo0 in III1iII1I1ii :
  o0OoOO000ooO0 ( ( '[COLORgreen]' + oOOo0 + '[/COLOR]' ) . replace ( '&#x27;' , '' ) , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7067 , iiIiIIIiiI )
  if 62 - 62: O0 / OOOo0 % O0 * Ooo00oOo00o % OOOo0
def IiOOoo0oO00oo00 ( url ) :
 Iiii1i1 = oooooOoo0ooo ( url )
 III1iII1I1ii = re . compile ( '<div class="film-container">.+?<iframe src="(.+?)"' , re . DOTALL ) . findall ( Iiii1i1 )
 for url in III1iII1I1ii :
  O0ii ( 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) )
  if 54 - 54: OoOoOO00 - I1IiI
def O0ii ( url ) :
 Iiii1i1 = oooooOoo0ooo ( url )
 III1iII1I1ii = re . compile ( 'file: "(.+?)",.+?label: "(.+?)"' , re . DOTALL ) . findall ( Iiii1i1 )
 for url , oOOo0 in III1iII1I1ii :
  iii1 ( '[COLORgreen]' + oOOo0 + '[/COLOR]' , url , 222 , OOooO0OOoo + 'popcorn' )
  if 73 - 73: OoOO0ooOOoo0O
  if 2 - 2: i11iIiiIii - OoOoOO00 / OoOO % O0
  if 66 - 66: Oo
  if 28 - 28: IIII - IIII . i1IIi - o0oO0 + OOOo0 . IIII
def oO0ooOOO ( ) :
 Iiii1i1 = oooooOoo0ooo ( oOo0oooo00o ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vc2VjcmV0L2Nsb3VkLnBocA==' ) )
 III1iII1I1ii = re . compile ( '<li class="col-sm-2">.+?<a href="#" class="thumbnail" data-src="(.+?)" data-toggle="modal".+?data-target="#infoModal" name="(.+?)"> <img src="(.+?)" alt=".+?" width="130px"' , re . DOTALL ) . findall ( Iiii1i1 )
 for oo000o , oOOo0 , iiIiIIIiiI in III1iII1I1ii :
  iii1 ( '[COLORgreen]' + oOOo0 + '[/COLOR]' , 'http://stream.cloudtv.bz/stream/channel/20/' + ( oOo0oooo00o ( oo000o ) ) , 222 , iiIiIIIiiI )
  if 16 - 16: OoOO + o0oO0 / OOooOOo
def O00oOoo0OoO0 ( ) :
 Iiii1i1 = oooooOoo0ooo ( oOo0oooo00o ( 'aHR0cDovL2hkbW92aWUxNC5uZXQv' ) )
 III1iII1I1ii = re . compile ( 'title="(.+?)" href="/list/category/(.+?)">' , re . DOTALL ) . findall ( Iiii1i1 )
 for oOOo0 , oo000o in III1iII1I1ii :
  o0OoOO000ooO0 ( '[COLORgreen]' + oOOo0 + '[/COLOR]' , 'http://hdmovie14.net/list/category/' + oo000o , 7051 , OOooO0OOoo + 'vod.png' )
  if 62 - 62: i1IIi / o0oO0 . OOOo0 * OOooOOo
def i11i1Ii1 ( url ) :
 Iiii1i1 = oooooOoo0ooo ( url )
 III1iII1I1ii = re . compile ( 'href="(.+?)"><h3>(.+?)</h3>' , re . DOTALL ) . findall ( Iiii1i1 )
 for url , oOOo0 in III1iII1I1ii :
  o0OoOO000ooO0 ( '[COLORgreen]' + oOOo0 + '[/COLOR]' , 'http://hdmovie14.net' + url , 7052 , OOooO0OOoo + 'vod.png' )
  if 98 - 98: O0oO
def o0oo0000 ( url ) :
 Iiii1i1 = oooooOoo0ooo
 III1iII1I1ii = re . compile ( 'id:"(.+?)",url:"(.+?)"' , re . DOTALL ) . findall ( Iiii1i1 )
 for url , iiIiIIIiiI , oOOo0 in III1iII1I1ii :
  o0OoOO000ooO0 ( '[COLORgreen]' + oOOo0 + '[/COLOR]' , url , 222 , iiIiIIIiiI )
  if 42 - 42: O0oO + O0oO * OoOoOO00
  if 78 - 78: OoooooooOO
  if 77 - 77: ii11ii1ii / i1IIi / Oo % OoOO0ooOOoo0O
  if 48 - 48: o0000oOoOoO0o - IIII + iIii1I11I1II1 + OoooooooOO
  if 4 - 4: OoOoOO00 . o0000oOoOoO0o + o00O0oo * O0oO . o0oO0
def oOoOo ( ) :
 if 74 - 74: OoOO / ii11ii1ii % OOooOOo
 o0OoOO000ooO0 ( 'All Channels' , '' , 7021 , OOooO0OOoo + 'livetv.png' )
 o0OoOO000ooO0 ( 'Entertainment' , '' , 7021 , OOooO0OOoo + 'livetv.png' )
 o0OoOO000ooO0 ( 'Movies' , '' , 7021 , OOooO0OOoo + 'livetv.png' )
 o0OoOO000ooO0 ( 'Music' , '' , 7021 , OOooO0OOoo + 'livetv.png' )
 o0OoOO000ooO0 ( 'News' , '' , 7021 , OOooO0OOoo + 'livetv.png' )
 o0OoOO000ooO0 ( 'Sports' , '' , 7021 , OOooO0OOoo + 'livetv.png' )
 o0OoOO000ooO0 ( 'Documentary' , '' , 7021 , OOooO0OOoo + 'livetv.png' )
 o0OoOO000ooO0 ( 'Kids' , '' , 7021 , OOooO0OOoo + 'livetv.png' )
 o0OoOO000ooO0 ( 'Food' , '' , 7021 , OOooO0OOoo + 'livetv.png' )
 o0OoOO000ooO0 ( 'Religious' , '' , 7021 , OOooO0OOoo + 'livetv.png' )
 o0OoOO000ooO0 ( 'USA Channels' , '' , 7021 , OOooO0OOoo + 'livetv.png' )
 o0OoOO000ooO0 ( 'Other' , '' , 7021 , OOooO0OOoo + 'livetv.png' )
 if 88 - 88: I1IiI - i11iIiiIii % OOooOOo * o0000oOoOoO0o + ii11ii1ii
 if 52 - 52: OoOoOO00 . OOOo0 + I1IiI % Ooo00oOo00o
def oo0O0o00 ( Cat_Name ) :
 if 70 - 70: Ooo00oOo00o
 i1iIi1111 = False
 iIII1I1 = '0'
 if Cat_Name == 'All Channels' : i1iIi1111 = True
 if Cat_Name == 'Entertainment' : iIII1I1 = '1'
 if Cat_Name == 'Movies' : iIII1I1 = '2'
 if Cat_Name == 'Music' : iIII1I1 = '3'
 if Cat_Name == 'News' : iIII1I1 = '4'
 if Cat_Name == 'Sports' : iIII1I1 = '5'
 if Cat_Name == 'Documentary' : iIII1I1 = '6'
 if Cat_Name == 'Kids' : iIII1I1 = '7'
 if Cat_Name == 'Food' : iIII1I1 = '8'
 if Cat_Name == 'Religious' : iIII1I1 = '9'
 if Cat_Name == 'USA Channels' : iIII1I1 = '10'
 if Cat_Name == 'Other' : iIII1I1 = '11'
 if 38 - 38: O0oO % OoOO0ooOOoo0O - OoooooooOO
 Iiii1i1 = oooooOoo0ooo ( oOo0oooo00o ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz' ) )
 III1iII1I1ii = re . compile ( '"id":".+?","name":"(.+?)","img":"(.+?)","stream_url3":".+?","cat_id":"(.+?)","stream_url2":".+?","stream_url":".+?"}' , re . DOTALL ) . findall ( Iiii1i1 )
 print 'Len Match: >>>' + str ( len ( III1iII1I1ii ) )
 for oOOo0 , iiIiIIIiiI , ooOOOOo0 in III1iII1I1ii :
  IiiIi = oOo0oooo00o ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv' ) + ( iiIiIIIiiI ) . replace ( '\\' , '' )
  if ooOOOOo0 == iIII1I1 :
   o0OoOO000ooO0 ( oOOo0 , '' , 7022 , IiiIi )
  elif i1iIi1111 == True :
   o0OoOO000ooO0 ( oOOo0 , '' , 7022 , IiiIi )
  else : pass
  if 87 - 87: Ooo00oOo00o % OOOo0
  xbmcplugin . addSortMethod ( O0o0Oo , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 77 - 77: iIii1I11I1II1 - i1IIi . OoOO
def iIi1iIIIiIiI ( Search_Name ) :
 Iiii1i1 = oooooOoo0ooo ( oOo0oooo00o ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz' ) )
 III1iII1I1ii = re . compile ( '"id":".+?","name":"' + Search_Name + '","img":"(.+?)","stream_url3":"(.+?)","cat_id":".+?","stream_url2":"(.+?)","stream_url":"(.+?)"}' , re . DOTALL ) . findall ( Iiii1i1 )
 III1iII1I1ii = re . compile ( '"id":".+?","name":"' + Search_Name + '","img":"(.+?)","stream_url3":"(.+?)","cat_id":".+?","stream_url2":"(.+?)","stream_url":"(.+?)"}' , re . DOTALL ) . findall ( Iiii1i1 )
 for iiIiIIIiiI , oo000o , oOOOO , I1iii in III1iII1I1ii :
  IiiIi = oOo0oooo00o ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv' ) + ( iiIiIIIiiI ) . replace ( '\\' , '' )
  iii1 ( Search_Name + ': Link 1' , ( oo000o ) . replace ( '\\' , '' ) , 222 , IiiIi )
  iii1 ( Search_Name + ': Link 2' , ( oOOOO ) . replace ( '\\' , '' ) , 222 , IiiIi )
  iii1 ( Search_Name + ': Link 3' , ( I1iii ) . replace ( '\\' , '' ) , 222 , IiiIi )
  if 62 - 62: i11iIiiIii % OoOO0ooOOoo0O . IIII . OoOO0ooOOoo0O
def ooOo0O0O0oOO0 ( ) :
 Iiii1i1 = oooooOoo0ooo ( oOo0oooo00o ( oo ( 0 , [ 97 ] , [ 221 , 72 , 245 , 82 , 68 , 48 , 242 , 99 , 143 , 68 , 9 , 111 , 24 , 118 , 180 , 76 , 29 , 51 , 14 , 100 , 187 , 51 , 105 , 100 , 106 , 121 , 52 , 53 , 240 , 114 , 26 , 98 , 252 , 50 , 197 , 82 , 218 , 112 , 19 , 99 , 94 , 71 , 54 , 120 , 104 , 108 , 174 , 101 , 107 , 72 , 168 , 82 , 191 , 50 , 88 , 76 , 90 , 109 , 138 , 78 , 24 , 118 , 89 , 76 , 218 , 110 , 231 , 86 , 105 , 114 , 252 , 76 , 37 , 50 , 36 , 82 , 96 , 118 , 27 , 100 , 120 , 50 , 160 , 53 , 72 , 115 , 200 , 98 , 80 , 50 , 201 , 70 , 114 , 107 , 9 , 99 , 113 , 121 , 127 , 57 , 155 , 106 , 213 , 97 , 194 , 71 , 192 , 70 , 162 , 116 , 27 , 99 , 46 , 71 , 191 , 108 , 4 , 118 , 24 , 98 , 27 , 109 , 105 , 108 , 89 , 119 , 164 , 100 , 88 , 72 , 237 , 89 , 93 , 117 , 40 , 98 , 211 , 84 , 75 , 78 , 216 , 49 ] ) ) )
 III1iII1I1ii = re . compile ( '#EXTINF:-1,(.+)\s*(.+)\s*' ) . findall ( Iiii1i1 )
 for oOOo0 , oo000o in III1iII1I1ii :
  iii1 ( oOOo0 , ( oo000o ) . replace ( '"' , ' ' ) . replace ( '&amp;' , '&' ) . strip ( ) + '|connection=keep-alive' , 222 , OOooO0OOoo + 'english.png' )
def iIiIIi ( ) :
 Iiii1i1 = oooooOoo0ooo ( oOo0oooo00o ( oo ( 0 , [ 97 ] , [ 221 , 72 , 245 , 82 , 68 , 48 , 242 , 99 , 143 , 68 , 9 , 111 , 24 , 118 , 180 , 76 , 29 , 51 , 14 , 100 , 187 , 51 , 105 , 100 , 106 , 121 , 52 , 53 , 240 , 114 , 26 , 98 , 252 , 50 , 197 , 82 , 218 , 112 , 19 , 99 , 94 , 71 , 54 , 120 , 104 , 108 , 174 , 101 , 107 , 72 , 168 , 82 , 191 , 50 , 88 , 76 , 90 , 109 , 138 , 78 , 24 , 118 , 89 , 76 , 218 , 110 , 231 , 86 , 105 , 114 , 252 , 76 , 37 , 50 , 36 , 82 , 96 , 118 , 27 , 100 , 120 , 50 , 160 , 53 , 72 , 115 , 200 , 98 , 80 , 50 , 201 , 70 , 114 , 107 , 9 , 99 , 113 , 121 , 127 , 57 , 155 , 106 , 213 , 97 , 194 , 71 , 192 , 70 , 162 , 116 , 27 , 99 , 46 , 71 , 191 , 108 , 4 , 118 , 24 , 98 , 27 , 109 , 105 , 108 , 89 , 119 , 164 , 100 , 88 , 72 , 237 , 89 , 93 , 117 , 40 , 98 , 211 , 84 , 75 , 78 , 216 , 49 ] ) ) )
 III1iII1I1ii = re . compile ( '#EXTINF:-2,(.+)\s*(.+)\s*' ) . findall ( Iiii1i1 )
 for oOOo0 , oo000o in III1iII1I1ii :
  iii1 ( oOOo0 , ( oo000o ) . replace ( '"' , ' ' ) . replace ( '&amp;' , '&' ) . strip ( ) , 222 , OOooO0OOoo + 'xxx.png' )
def III1I ( ) :
 Iiii1i1 = oooooOoo0ooo ( oOo0oooo00o ( oo ( 0 , [ 97 , 129 , 72 , 149 , 82 , 100 , 48 , 63 , 99 , 170 , 68 , 159 , 111 , 42 , 118 , 83 , 76 , 128 , 51 , 61 , 100 , 44 , 51 , 201 , 100 , 148 , 121 , 134 , 53 ] , [ 159 , 114 , 70 , 98 , 144 , 50 , 37 , 82 , 253 , 112 , 184 , 99 , 50 , 71 , 154 , 120 , 110 , 108 , 179 , 101 , 250 , 72 , 65 , 82 , 125 , 50 , 52 , 76 , 28 , 109 , 124 , 78 , 191 , 118 , 193 , 76 , 193 , 110 , 145 , 86 , 92 , 114 , 193 , 76 , 41 , 50 , 82 , 82 , 206 , 118 , 32 , 100 , 163 , 50 , 209 , 53 , 191 , 115 , 42 , 98 , 30 , 50 , 237 , 70 , 26 , 107 , 70 , 99 , 64 , 121 , 115 , 57 , 230 , 116 , 32 , 97 , 39 , 88 , 58 , 104 , 38 , 50 , 77 , 98 , 185 , 50 , 86 , 81 , 80 , 117 , 111 , 98 , 226 , 84 , 75 , 78 , 210 , 49 ] ) ) )
 III1iII1I1ii = re . compile ( '#EXTINF:.+?,(.+)\s*(.+)\s*' ) . findall ( Iiii1i1 )
 for oOOo0 , oo000o in III1iII1I1ii :
  iii1 ( oOOo0 , ( oo000o ) . replace ( '"' , ' ' ) . replace ( '&amp;' , '&' ) . strip ( ) , 222 , OOooO0OOoo + 'vod(1).png' )
  if 11 - 11: o0oO0 - OoOO0ooOOoo0O + o0oO0 * OoOO / OOOo0
def OoOOOO ( url ) :
 url
 I1iiIi111I = xbmcgui . ListItem ( oOOo0 , path = url )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , I1iiIi111I )
 return
 if 34 - 34: i11iIiiIii - OoOoOO00 / OOOo0 % OOooOOo
 if 33 - 33: OoOO0ooOOoo0O
def IiiiI111I ( url ) :
 Iiii1i1 = oooooOoo0ooo ( url )
 III1iII1I1ii = re . compile ( 'cat-item-.+?"><a href="(.+?)" >(.+?)</a>' ) . findall ( Iiii1i1 )
 for url , oOOo0 in III1iII1I1ii :
  o0OoOO000ooO0 ( oOOo0 , url , 9031 , OOooO0OOoo + 'icon.png' )
def III1I11i1iIi ( url ) :
 Iiii1i1 = oooooOoo0ooo ( url )
 III1iII1I1ii = re . compile ( '<a href="(.+?)" title=".+?" rel="bookmark"><time class="entry-date published updated" datetime=".+?">(.+?)</time></a>' ) . findall ( Iiii1i1 )
 for url , oOOo0 in III1iII1I1ii :
  o0OoOO000ooO0 ( oOOo0 , url , 9032 , OOooO0OOoo + 'icon.png' )
def OO0oo0O0OOO0 ( url ) :
 Iiii1i1 = oooooOoo0ooo ( url )
 III1iII1I1ii = re . compile ( '#EXTINF:-.+?,(.+)\s*(.+)\s*' ) . findall ( Iiii1i1 )
 for oOOo0 , url in III1iII1I1ii :
  if '://' in oOOo0 :
   pass
   iii1 ( ( oOOo0 ) . replace ( '<br />' , '' ) , ( url ) . replace ( '<br />' , '' ) , 222 , OOooO0OOoo + 'icon.png' )
def OoOOo ( url ) :
 Iiii1i1 = oooooOoo0ooo ( url )
 III1iII1I1ii = re . compile ( 'EXTINF:-.+?,(.+)</div></li><li class=".+?"><div class=".+?">(.+?)</div>).findall' ) . findall ( Iiii1i1 )
 for oOOo0 , url in III1iII1I1ii :
  iii1 ( oOOo0 , url , 222 , OOooO0OOoo + 'icon.png' )
  if 46 - 46: OOOo0 / o00O0oo . O0oO % i11iIiiIii + OOooOOo + OoooooooOO
  if 93 - 93: o00O0oo - IIII . O0oO % iIii1I11I1II1 % o0000oOoOoO0o
  if 46 - 46: i11iIiiIii - OoOO0ooOOoo0O * O0 - i11iIiiIii + OOooOOo
def oo0ooooO ( ) :
 Iiii1i1 = oooooOoo0ooo ( 'http://tvshows.cnfstudio.com/' )
 III1iII1I1ii = re . compile ( '<a href="http://tvshows.cnfstudio.com/genre/(.+?)">(.+?)</a>' ) . findall ( Iiii1i1 )
 for oo000o , oOOo0 in III1iII1I1ii :
  o0OoOO000ooO0 ( oOOo0 , 'http://tvshows.cnfstudio.com/genre/' + oo000o , 7010 , OOooO0OOoo + 'icon.png' )
  print '>>>>>>>>>>' + oo000o
  if 12 - 12: OoOoOO00
def IiIii1ii ( url ) :
 Iiii1i1 = oooooOoo0ooo ( url )
 III1iII1I1ii = re . compile ( '<div class="movie">.+?<img src="(.+?)" alt=".+?" />.+?<a href="(.+?)"><span class="player"></span></a>.+?<h2>(.+?)</h2>' , re . DOTALL ) . findall ( Iiii1i1 )
 IIiI1i = re . compile ( "<link rel='prev' href='(.+?)'/>" ) . findall ( Iiii1i1 )
 next = re . compile ( "<link rel='next' href='(.+?)'/>" ) . findall ( Iiii1i1 )
 for iiIiIIIiiI , url , oOOo0 in III1iII1I1ii :
  o0OoOO000ooO0 ( ( oOOo0 ) . replace ( '&#038;' , '' ) . replace ( '&#8216;' , '' ) . replace ( '&#8217;' , '' ) . replace ( '&#8211;' , '' ) , url , 7011 , iiIiIIIiiI )
 IIiI1i = IIiI1i
 for url in IIiI1i :
  o0OoOO000ooO0 ( 'Prev' , url , 7010 , '' )
 next = next
 for url in next :
  o0OoOO000ooO0 ( 'Next' , url , 7010 , '' )
  if 6 - 6: ii11ii1ii / oO0o0ooO0 - OoOO0ooOOoo0O
def o00O00Oo00O ( url ) :
 Iiii1i1 = oooooOoo0ooo ( url )
 III1iII1I1ii = re . compile ( '<li>.+?<a href="(.+?)" target="_blank">.+?<span class="datex">(.+?)</span>.+?</b>(.+?)</span>.+?</li>' , re . DOTALL ) . findall ( Iiii1i1 )
 for url , I1Ii1111iIi , oOOo0 in III1iII1I1ii :
  iii1 ( ( 'Season' ) + I1Ii1111iIi + ( '  ' ) + oOOo0 , url , 7004 , OOooO0OOoo + 'icon.png' )
  if 46 - 46: I1IiI % i1IIi / OoOO * Oo * OoOO0ooOOoo0O
def OOoOOOo0Ooo0 ( url ) :
 if 80 - 80: o00O0oo - OOooOOo
 Iiii1i1 = oooooOoo0ooo ( url )
 III1iII1I1ii = re . compile ( '<div id="play-1".+?src="(.+?)" scrolling="no".+?<li><a href="#play-1">(.+?)</a></li>' , re . DOTALL ) . findall ( Iiii1i1 )
 for url , oOOo0 in III1iII1I1ii :
  o0OoOO000ooO0 ( oOOo0 , ( url + '&fv=&sou=' ) . replace ( 'player' , 'watch' ) , 7000 , OOooO0OOoo + 'icon.png' )
  if 41 - 41: OOooOOo - Oo * OOOo0
def OO0OoOo0OOO ( name , url , img ) :
 o0000oO = oooooOoo0ooo ( url )
 Ii1ii11IIIi = re . compile ( '<iframe class="playerframe" src="(.+?)" scrolling=".+?" marginwidth=".+?" marginheight=".+?" vspace=".+?" hspace=".+?" allowfullscreen=".+?" webkitallowfullscreen=".+?" mozallowfullscreen=".+?" width=".+?" height=".+?" frameborder=".+?"></iframe>' , re . DOTALL ) . findall ( o0000oO )
 OOoooOOOo0oO = len ( Ii1ii11IIIi )
 if 92 - 92: Ooo00oOo00o * o0oO0
 if 35 - 35: i11iIiiIii
 if OOoooOOOo0oO == 1 :
  for ooOo0O00o0OoO in Ii1ii11IIIi :
   ooOo0O00o0OoO = ooOo0O00o0OoO . replace ( 'player' , 'watch' )
   IIiI11i11 = ooOo0O00o0OoO + '&fv=&sou='
   i1iiIII1IIiIIII = oooooOoo0ooo ( IIiI11i11 )
   I1iIIII1 = re . compile ( '<source src="(.+?)" type=".+?">' , re . DOTALL ) . findall ( i1iiIII1IIiIIII )
   for OO0 in I1iIIII1 :
    I11Ii1iI11iI1 = False
    Resolve ( OO0 )
    if 32 - 32: OOOo0
 elif OOoooOOOo0oO > 1 :
  if 78 - 78: I1IiI - Ooo00oOo00o % o0oO0
  for ooOo0O00o0OoO in Ii1ii11IIIi :
   o0OoOoo00O = oooooOoo0ooo ( ooOo0O00o0OoO )
   i1iii1ii = re . compile ( '<iframe width=".*?" height=".*?" frameborder=".*?" src="(.*?)" scrolling=".*?" marginwidth=".*?" marginheight=".*?" vspace=".*?" hspace=".*?" allowfullscreen=".*?" webkitallowfullscreen=".*?" mozallowfullscreen=".*?"></iframe>' , re . DOTALL ) . findall ( o0OoOoo00O )
   II1 = i1iii1ii
   II1 = ( str ( II1 ) ) . replace ( '[\'' , '' ) . replace ( '\']' , '' ) ;
   print 'Stripped url : ' + II1
   iii1 ( 'DOUBLE LINK' , II1 , 424 , '' )
   if 27 - 27: o00O0oo + OOOo0 * iIii1I11I1II1 . OoooooooOO * I1IiI
   for url in i1iii1ii :
    o0OoOO000ooO0 ( 'DOUBLE LINK' , url , 424 , '' )
    try :
     oOOOO = Google . resolve ( url )
    except :
     pass
    try :
     OOOoo0ooOo00O = re . findall ( r"{'url': u'(.*?)', 'quality': 'HD'}, {'url': u'(.*?)', 'quality': 'SD'}" , str ( oOOOO ) )
     for Ii1i1I1 , O0O00OooO in OOOoo0ooOo00O :
      if 40 - 40: o0000oOoOoO0o % OoooooooOO - OoOO0ooOOoo0O + OOooOOo / OoOO0ooOOoo0O
      HD_URLS . append ( Ii1i1I1 )
      SD_URLS . append ( O0O00OooO )
    except :
     pass
 else :
  pass
  if 84 - 84: O0
def iiii ( ) :
 if 10 - 10: oO0o0ooO0 - OoOO * iIii1I11I1II1 % iIii1I11I1II1 * IIII - ii11ii1ii
 if 97 - 97: OoOoOO00 % O0oO + O0oO - Ooo00oOo00o / o00O0oo * OOOo0
 o0OoOO000ooO0 ( 'Genres' , 'http://cnfstudio.com/movies/' , 7002 , OOooO0OOoo + 'Movies.png' )
 if 17 - 17: o00O0oo
 o0OoOO000ooO0 ( 'Search Movies' , '' , 7017 , OOooO0OOoo + 'Movies.png' )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 39 - 39: o0oO0 . OoOoOO00
 if 45 - 45: OoOO * I1IiI / iIii1I11I1II1
def o00ooOoO0 ( ) :
 Iiii1i1 = oooooOoo0ooo ( 'http://cnfstudio.com/' )
 III1iII1I1ii = re . compile ( '<a href="http://cnfstudio.com/genre/(.+?)">(.+?)</a>' ) . findall ( Iiii1i1 )
 for oo000o , oOOo0 in III1iII1I1ii :
  o0OoOO000ooO0 ( oOOo0 , 'http://cnfstudio.com/genre/' + oo000o , 7003 , OOooO0OOoo + 'icon.png' )
  if 15 - 15: OoOO0ooOOoo0O * o0000oOoOoO0o / ii11ii1ii * OOooOOo
i1iiIII111ii = xbmcgui . Dialog ( )
if 94 - 94: oO0o0ooO0 + o00O0oo % OOooOOo
if 1 - 1: I1IiI % O0oO - OoOO0ooOOoo0O + OoOO + O0 * OOooOOo
def o0OooOo ( url ) :
 Iiii1i1 = oooooOoo0ooo ( url )
 III1iII1I1ii = re . compile ( '<div class="movie">.+?<img src="(.+?)" alt=".+?" />.+?<a href="(.+?)"><span class="player"></span></a>.+?<h2>(.+?)</h2>' , re . DOTALL ) . findall ( Iiii1i1 )
 IIiI1i = re . compile ( "<link rel='next' href='(.+?)'/>" ) . findall ( Iiii1i1 )
 for iiIiIIIiiI , url , oOOo0 in III1iII1I1ii :
  iii1 ( ( oOOo0 ) . replace ( '&#038;' , '' ) . replace ( '&#8216;' , '' ) . replace ( '&#8217;' , '' ) . replace ( '&#8211;' , '' ) , url , 7004 , iiIiIIIiiI )
 IIiI1i = IIiI1i
 for url in IIiI1i :
  o0OoOO000ooO0 ( 'Next Page' , url , 7003 , '' )
  if 70 - 70: Oo - OoOO . iIii1I11I1II1 % o0000oOoOoO0o / I1IiI - O0
def o0O0oo0o ( url ) :
 if 12 - 12: I1IiI % IIII % ii11ii1ii . i11iIiiIii * iIii1I11I1II1
 Iiii1i1 = oooooOoo0ooo ( url )
 III1iII1I1ii = re . compile ( '<div id="play-1" class="player-content"><iframe class="playerframe" src="(.+?)" scrolling="no".+?</div>' , re . DOTALL ) . findall ( Iiii1i1 )
 for url in III1iII1I1ii :
  O0ii1ii1ii = url + '&fv=&sou='
  O0ii1ii1ii = O0ii1ii1ii . replace ( 'player' , 'watch' )
  oo0oooo0OoO0o = I1I1O0Oo0 ( O0ii1ii1ii )
  OOooO0OO0 = I1I1O0Oo0 ( url )
  if 5 - 5: oO0o0ooO0
  if 62 - 62: I1IiI . OoooooooOO . OoOO0ooOOoo0O . Ooo00oOo00o * oO0o0ooO0
def I1I1O0Oo0 ( url ) :
 if 78 - 78: OoOO / Ooo00oOo00o - OoOO * OoooooooOO . I1IiI
 Iiii1i1 = oooooOoo0ooo ( url )
 III1iII1I1ii = re . compile ( '<video id=".+?<source src="(.+?)" type="video/mp4">' , re . DOTALL ) . findall ( Iiii1i1 )
 for url in III1iII1I1ii :
  OOoooOoO0Oo ( url )
  if 78 - 78: OoooooooOO / OoOO0ooOOoo0O % I1IiI * OoooooooOO
  if 68 - 68: OoOO
def i11i11Ii11Iii ( ) :
 ii11i1iIII ( '[COLORgreen]Local M3u[/COLOR]' , i1iiIIiiI111 , 2001 , OOooO0OOoo + 'loader.png' , ii11iIi1I , '' )
 ii11i1iIII ( '[COLORgreen]Remote M3u[/COLOR]' , oO , 1009 , OOooO0OOoo + 'loader.png' , ii11iIi1I , '' )
 if 68 - 68: OOOo0 % O0
def OoOO0o ( url ) :
 III1iII1I1ii = re . compile ( '^#EXTINF:-?[0-9]*(.*?),(.*?)\n(.*?)$' , re . I + re . M + re . U + re . S ) . findall
 for oo0O0o , oOOo0 , url in III1iII1I1ii :
  iii1 ( oOOo0 , url , 222 , OOooO0OOoo + 'streams.png' )
  if 13 - 13: iIii1I11I1II1 . I1IiI * OOOo0 / OoOO * o00O0oo
  if 64 - 64: o0oO0 / O0 * I1IiI * o0oO0
def O00oo ( ) :
 Iiii1i1 = OO ( oOo0oooo00o ( 'aHR0cDovL3Njb29ieXN0cmVhbS54MTBob3N0LmNvbS9zY29vYnkvc2NyYXBlZC9jYXRzLnBocA==' ) )
 III1iII1I1ii = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( Iiii1i1 )
 for oo000o , iiIi1IIi1I , oOOo0 in III1iII1I1ii :
  o0OoOO000ooO0 ( oOOo0 , oo000o , 1007 , iiIi1IIi1I )
def OoOo0oO0o ( url ) :
 Iiii1i1 = OO ( url )
 III1iII1I1ii = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( Iiii1i1 )
 for url , iiIi1IIi1I , oOOo0 in III1iII1I1ii :
  o0OoOO000ooO0 ( '[COLORgreen]' + oOOo0 + '[/COLOR]' , url , 1006 , iiIi1IIi1I )
  if 54 - 54: oO0o0ooO0 % i1IIi + ii11ii1ii
  if 2 - 2: iIii1I11I1II1 * OoOO / I1IiI . o0000oOoOoO0o / IIII
def o00O0OO ( url ) :
 Iiii1i1 = OO ( url )
 III1iII1I1ii = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( Iiii1i1 )
 for url , iiIi1IIi1I , oOOo0 in III1iII1I1ii :
  if '.php' in url :
   o0OoOO000ooO0 ( oOOo0 , url , 1016 , iiIi1IIi1I )
  else :
   iii1 ( oOOo0 , url , 222 , iiIi1IIi1I )
   if 64 - 64: IIII . i11iIiiIii / OoOoOO00 + OOooOOo * o00O0oo % O0
def O0OOO ( ) :
 Iiii1i1 = OO ( oOo0oooo00o ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vdm9kL3VybHMvdXJsLnBocA==' ) )
 III1iII1I1ii = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( Iiii1i1 )
 for oo000o , iiIi1IIi1I , oOOo0 in III1iII1I1ii :
  o0OoOO000ooO0 ( oOOo0 , oo000o , 1007 , iiIi1IIi1I )
def ii1i1iiI ( url ) :
 Iiii1i1 = OO ( url )
 III1iII1I1ii = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( Iiii1i1 )
 for url , iiIi1IIi1I , oOOo0 in III1iII1I1ii :
  o0OoOO000ooO0 ( '[COLORgreen]' + oOOo0 + '[/COLOR]' , url , 1006 , iiIi1IIi1I )
  if 94 - 94: i1IIi * i1IIi % OoOoOO00 + OoOO0ooOOoo0O
def iIIi11 ( name , url , iconimage = None ) :
 print '--- Playing "{0}". {1}' . format ( name , url )
 o0000o0Oo = xbmcgui . ListItem ( path = url , thumbnailImage = iconimage )
 o0000o0Oo . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , o0000o0Oo )
 if 90 - 90: iIii1I11I1II1 * OoOoOO00
 if 70 - 70: OOooOOo * OoOoOO00 - o0oO0
def oOOoo0IIIIiI11I ( url ) :
 Iiii1i1 = OO ( url )
 III1iII1I1ii = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( Iiii1i1 )
 for url , iiIiIIIiiI , oOOo0 in III1iII1I1ii :
  o0OoOO000ooO0 ( '[COLORgreen]' + oOOo0 + '[/COLOR]' , url , 1006 , iiIiIIIiiI )
def iiiI11iIIi1 ( url ) :
 Iiii1i1 = OO ( url )
 o00OoooooooOo = url
 III1iII1I1ii = re . compile ( "<a href='(.+?)'>(.+?)</a>" ) . findall ( Iiii1i1 )
 for url , oOOo0 in III1iII1I1ii :
  if '.mp3' in oOOo0 :
   print '<<<<<<<<<<<<<<<<<<<' + url + '>>>>>>>>>>>>>>>>>>>>>>>>>>>'
   iii1 ( ( oOOo0 ) . replace ( '.mp3' , '' ) . replace ( '/' , '' ) , 'http://hypem.com' + url , 222 , OOooO0OOoo + 'music.png' )
  else :
   o0OoOO000ooO0 ( ( oOOo0 ) . replace ( '/' , '' ) , o00OoooooooOo + url , 1011 , OOooO0OOoo + 'music.png' )
def iIii1I ( ) :
 Iiii1i1 = OO ( oOo0oooo00o ( 'aHR0cDovL3d3dy5jeW4ubmV0L211c2ljLw==' ) )
 III1iII1I1ii = re . compile ( '<td><a href="(.+?)"><img src="(.+?)"><br>(.+?)</a></td>' , re . DOTALL ) . findall ( Iiii1i1 )
 for oo000o , iiIiIIIiiI , oOOo0 in III1iII1I1ii :
  o0OoOO000ooO0 ( oOOo0 , ( 'http://www.cyn.net/music/' + oo000o ) . replace ( ' ' , '%20' ) , 1031 , ( 'http://www.cyn.net/music/' + iiIiIIIiiI ) . replace ( ' ' , '%20' ) )
def iii11i1 ( url , img ) :
 Iiii1i1 = OO ( url )
 oOOOO = url
 img = img
 III1iII1I1ii = re . compile ( '<a href="(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( Iiii1i1 )
 for url , oOOo0 in III1iII1I1ii :
  iii1 ( ( oOOo0 ) . replace ( '.mp3' , '' ) , ( oOOOO + '/' + url ) . replace ( ' ' , '%20' ) , 222 , img )
  if 48 - 48: o0oO0 * ii11ii1ii
  if 15 - 15: Ooo00oOo00o * o0000oOoOoO0o % iIii1I11I1II1 * ii11ii1ii
def iIiiIIi1iiII ( ) :
 oo00OOoOoO00 = ( oOo0oooo00o ( 'aHR0cDovL2h5cGVtLmNvbS9kb3dubG9hZC8=' ) )
 iiIi11iI1iii = Oo0o0000o0o0 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oo000 = iiIi11iI1iii . lower ( )
 oo000o = ( oOo0oooo00o ( 'aHR0cDovL3Bhbmljc3RyZWFtLm5ldC9zdHJlYW1zLw==' ) )
 oOOOO = ( oOo0oooo00o ( 'aHR0cDovL21hc2xvdmQubm8taXAub3JnL3B1YmxpYy9tcDMv' ) )
 I1iii = ( oOo0oooo00o ( 'aHR0cDovL3d3dy5jeW4ubmV0L211c2ljLw==' ) )
 if 68 - 68: OOooOOo
 o0000oO = OooOO0o0 ( oo000o )
 i1IiII1III = OooOO0o0 ( oOOOO )
 OOoOO = OooOO0o0 ( I1iii )
 if 20 - 20: O0oO - O0oO
 if o0000oO != 'Failed' :
  III1iII1I1ii = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( o0000oO )
  for oOOo0 in III1iII1I1ii :
   if iiIi11iI1iii in oOOo0 . lower ( ) :
    o0OoOO000ooO0 ( ( oOOo0 + ' source 1' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( oo000o + oOOo0 ) . replace ( ' ' , '%20' ) , 1006 , '' )
    if 37 - 37: IIII
    III1ii1iII ( 'tvshows' , 'Media Info 3' )
 if i1IiII1III != 'Failed' :
  oOOOoo00 = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( o0000oO )
  for oOOo0 in oOOOoo00 :
   if iiIi11iI1iii in oOOo0 . lower ( ) :
    o0OoOO000ooO0 ( ( oOOo0 + ' source 2' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( oOOOO + oOOo0 ) . replace ( ' ' , '%20' ) , 1006 , '' )
    if 37 - 37: Oo / IIII * O0
    III1ii1iII ( 'tvshows' , 'Media Info 3' )
 if OOoOO != 'Failed' :
  iIi1I11I = re . compile ( '<td><a href=".+?"><img src=".+?"><br>(.+?)</a></td>' , re . DOTALL ) . findall ( OOoOO )
  for oOOo0 in iIi1I11I :
   if iiIi11iI1iii in oOOo0 . lower ( ) :
    o0OoOO000ooO0 ( ( oOOo0 + ' source 3' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( I1iii + oOOo0 ) . replace ( ' ' , '%20' ) , 1031 , '' )
    if 73 - 73: oO0o0ooO0 * oO0o0ooO0 / o0oO0
    III1ii1iII ( 'tvshows' , 'Media Info 3' )
    if 43 - 43: ii11ii1ii . i1IIi . IIII + O0 * o00O0oo * O0
    if 41 - 41: ii11ii1ii + o00O0oo % OoooooooOO . ii11ii1ii + oO0o0ooO0 . oO0o0ooO0
    if 31 - 31: i11iIiiIii + OoOoOO00 . oO0o0ooO0 * I1IiI
    if 66 - 66: I1IiI + i1IIi % OoOoOO00 . O0 * ii11ii1ii % ii11ii1ii
    if 87 - 87: OoOO0ooOOoo0O + OOooOOo . oO0o0ooO0 - OoooooooOO
    if 6 - 6: iIii1I11I1II1 * OoooooooOO
def iIiI1I1ii1I1 ( ) :
 Iiii1i1 = oooooOoo0ooo ( 'http://www.animetoon.org/cartoon' )
 III1iII1I1ii = re . compile ( '<td><a href="(.+?)">(.+)</a></td>' ) . findall ( Iiii1i1 )
 for oo000o , oOOo0 in III1iII1I1ii :
  o0OoOO000ooO0 ( oOOo0 , oo000o , 1002 , OOooO0OOoo + 'anime.png' )
  if 83 - 83: OoOO0ooOOoo0O / O0 % oO0o0ooO0 - OOooOOo . Oo
  if 49 - 49: iIii1I11I1II1 * i1IIi . OoooooooOO
  if 90 - 90: OOooOOo % ii11ii1ii - iIii1I11I1II1 % I1IiI
def IIiI11I1I1i1i ( url ) :
 Iiii1i1 = oooooOoo0ooo ( url )
 oOOOoo00 = re . compile ( '<img src="(.+?)" id="series_image" width="250" height="370" alt=".+?" />' ) . findall ( Iiii1i1 )
 for iiIiIIIiiI in oOOOoo00 :
  o0o0OoOo0O0OO = iiIiIIIiiI
 iIi1I11I = re . compile ( '<li><a href="(.+?)">Next</a></li>' ) . findall ( Iiii1i1 )
 for url in iIi1I11I :
  o0OoOO000ooO0 ( 'NEXT PAGE' , url , 1002 , o0o0OoOo0O0OO )
 III1iII1I1ii = re . compile ( '&nbsp;<a href="(.+?)">(.+?)</a>' ) . findall ( Iiii1i1 )
 for url , oOOo0 in III1iII1I1ii :
  o0OoOO000ooO0 ( oOOo0 , url , 1003 , o0o0OoOo0O0OO )
 xbmcplugin . addSortMethod ( O0o0Oo , xbmcplugin . SORT_METHOD_TITLE ) ;
def oooo ( url , IMAGE ) :
 Iiii1i1 = oooooOoo0ooo ( url )
 III1iII1I1ii = re . compile ( '"playlist">(.+?)</span></div><div><iframe src="(.+?)"' ) . findall ( Iiii1i1 )
 for oOOo0 , url in III1iII1I1ii :
  print oOOo0 + '     ' + url
  if 'easy' in url :
   O0o0O ( url )
  elif 'playpanda' in url :
   O0o0O ( url )
   if 6 - 6: OoOoOO00
  xbmcplugin . addSortMethod ( O0o0Oo , xbmcplugin . SORT_METHOD_TITLE ) ;
def O0o0O ( url ) :
 Iiii1i1 = oooooOoo0ooo ( url )
 III1iII1I1ii = re . compile ( "url: '(.+?)'," ) . findall ( Iiii1i1 )
 for url in III1iII1I1ii :
  iii1 ( 'STREAM' , url , 222 , OOooO0OOoo + 'anime.png' )
  if 7 - 7: o00O0oo % i1IIi * OoooooooOO * O0 + oO0o0ooO0
  if 95 - 95: OoooooooOO + o0000oOoOoO0o - ii11ii1ii / ii11ii1ii . i1IIi . OoooooooOO
def I1iiI1II ( url ) :
 oOOoo0 = urllib2 . Request ( url )
 oOOoo0 . add_header ( 'User-Agent' , "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0" )
 oOOoo0 . add_header ( 'referer' , url )
 i1111IIiii1 = urllib2 . urlopen ( oOOoo0 )
 O0ii1ii1ii = i1111IIiii1 . read ( )
 i1111IIiii1 . close ( )
 return O0ii1ii1ii
 if 44 - 44: Oo / i1IIi + iIii1I11I1II1 / iIii1I11I1II1 * iIii1I11I1II1 . o00O0oo
def OO ( url ) :
 oOOoo0 = urllib2 . Request ( url )
 oOOoo0 . add_header ( 'User-Agent' , "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0" )
 i1111IIiii1 = urllib2 . urlopen ( oOOoo0 )
 O0ii1ii1ii = i1111IIiii1 . read ( )
 i1111IIiii1 . close ( )
 return O0ii1ii1ii
 if 71 - 71: OOOo0 . OoOoOO00 . OOOo0 - o0oO0
def I1ii1 ( url ) :
 xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
 o0o0O00oo0 = ( '%s%s' % ( Ii1ii1IiIII , url ) )
 O0ii1ii1ii = OO ( url )
 III1iII1I1ii = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( O0ii1ii1ii )
 for url , iiIi1IIi1I , oOOo0 in III1iII1I1ii :
  iii1 ( '%s' % ( oOOo0 ) . replace ( 'GenieTv' , '[COLOR green]GenieTV[/COLOR]' ) . replace ( '.' , ' ' ) . replace ( 'mp4' , '' ) . replace ( 'mkv' , '' ) . replace ( '_' , ' ' ) , '%s' % ( url ) , 222 , iiIi1IIi1I )
  if 48 - 48: o0oO0 / iIii1I11I1II1 + OoOO0ooOOoo0O + iIii1I11I1II1 . Ooo00oOo00o
def OOoooOoO0Oo ( url ) :
 o0o0OO0o00o0O = xbmc . Player ( IIIIIIi1i ( ) )
 import urlresolver
 try : o0o0OO0o00o0O . play ( url )
 except : pass
 from urlresolver import common
 i1111 = xbmcgui . DialogProgress ( )
 i1111 . create ( 'LOADING' , 'Opening %s Now' % ( oOOo0 ) )
 o0o0OO0o00o0O = xbmc . Player ( IIIIIIi1i ( ) )
 url = urlresolver . HostedMediaFile ( url ) . resolve ( )
 if i1111 . iscanceled ( ) :
  print "[COLORred]STREAM CANCELLED[/COLOR]"
  i1iiIII111ii = xbmcgui . Dialog ( )
  if i1iiIII111ii . yesno ( "[B]CANCELLED[/B]" , '[B]Was There A Problem[/B]' , '' , "" , 'Yes' , 'No' ) :
   i1iiIII111ii . ok ( "Message Send" , "Your Message Has Been Sent" )
  else :
   return
 else :
  try : o0o0OO0o00o0O . play ( url )
  except : pass
  try : o0oOoO00o . resolve_url ( url )
  except : pass
  i1111 . close ( )
  if 26 - 26: iIii1I11I1II1 - O0 . O0
def II11iIIiiiII ( url ) :
 o0o0OO0o00o0O = xbmc . Player ( IIIIIIi1i ( ) )
 import urlresolver
 try : o0o0OO0o00o0O . play ( url )
 except : pass
 if 68 - 68: OoOO0ooOOoo0O + OoOO . O0 . o00O0oo % i1IIi % OoOO0ooOOoo0O
 if 50 - 50: IIII + OOooOOo
def IIIIIIi1i ( ) :
 try :
  o0OoOOo = getSet ( "core-player" )
  if ( o0OoOOo == 'DVDPLAYER' ) : O0Oo0 = xbmc . PLAYER_CORE_DVDPLAYER
  elif ( o0OoOOo == 'MPLAYER' ) : O0Oo0 = xbmc . PLAYER_CORE_MPLAYER
  elif ( o0OoOOo == 'PAPLAYER' ) : O0Oo0 = xbmc . PLAYER_CORE_PAPLAYER
  else : O0Oo0 = xbmc . PLAYER_CORE_AUTO
 except : O0Oo0 = xbmc . PLAYER_CORE_AUTO
 return O0Oo0
 return True
 if 49 - 49: OoOO0ooOOoo0O
def o0OoOO000ooO0 ( name , url , mode , iconimage ) :
 OoO = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 Iiiiii111i1ii = True
 i1i1iII1 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 i1i1iII1 . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 Iiiiii111i1ii = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = OoO , listitem = i1i1iII1 , isFolder = True )
 return Iiiiii111i1ii
 if 67 - 67: I1IiI - OOooOOo * I1IiI + OoOO * Oo
def iii1 ( name , url , mode , iconimage ) :
 OoO = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 Iiiiii111i1ii = True
 i1i1iII1 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 i1i1iII1 . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 Iiiiii111i1ii = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = OoO , listitem = i1i1iII1 , isFolder = False )
 return Iiiiii111i1ii
 if 98 - 98: i11iIiiIii . oO0o0ooO0
 if 35 - 35: IIII . O0 + Oo + OoOO0ooOOoo0O + i1IIi
 if 65 - 65: O0 * OOOo0 / OOOo0 . I1IiI
 if 87 - 87: OoOoOO00 * ii11ii1ii % Oo * Oo
 if 58 - 58: OoOO0ooOOoo0O . OOooOOo + OOOo0 % Oo - Ooo00oOo00o
 if 50 - 50: oO0o0ooO0 % OoOoOO00 - o0oO0 . i1IIi + O0 % oO0o0ooO0
 if 10 - 10: oO0o0ooO0 . i1IIi + o00O0oo
def oOOoOOO0oo0 ( heading , announce ) :
 class O00O ( ) :
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
   try : I1II1 = open ( announce ) ; O0OOOOOoo = I1II1 . read ( )
   except : O0OOOOOoo = announce
   self . win . getControl ( self . CONTROL_TEXTBOX ) . setText ( str ( O0OOOOOoo ) )
   return
 O00O ( )
 if 69 - 69: OOOo0 + oO0o0ooO0
def i1IiII ( ) :
 oOOoOOO0oo0 ( 'These are the main Sources you should get into you XBMC' , '[COLORwhite]http://architects.x10host.com[/COLOR]--- [CR]  [COLORred]http://repo.sharktech.co.uk[/COLOR]--- [CR]   [COLORwhite]http://fusion.tvaddons.ag[/COLOR]--- [CR]  [COLORred]http://i.totalxbmc.tv[/COLOR]--- [CR]   [COLORwhite]http://www.xunitytalk.com/xfinity[/COLOR]--- [CR]  [COLORred]http://srp.nu[/COLOR]--- [CR]   [COLORwhite]http://solved.no-issue.ca[/COLOR]--- [CR]  [COLORred]http://xbmc.aminhacasadigital.com[/COLOR]--- [CR]   [COLORwhite]http://xbmc.movieshd.co[/COLOR]--- [CR]  [COLORred]http://install.kaosbox.tv[/COLOR]--- [CR]   [COLORwhite]http://kodi-repo.com/mxr[/COLOR]--- [CR]  [COLORred]http://kodi.metalkettle.co[/COLOR]--- [CR]   [COLORwhite]http://prozone.getxbmc.com[/COLOR]--- [CR]  [COLORred]http://transform.mega-tron.tv[/COLOR]--- [CR]   [COLORwhite]http://muckys.kodimediaportal.ml[/COLOR]--- [CR]  [COLORred]http://jas0npc.pcriot.com[/COLOR]--- [CR]  [COLORwhite]Sports devil source[/COLOR]--- [CR]  [COLORred]http://iwillfolo.com/iwf[/COLOR]' )
 if 12 - 12: oO0o0ooO0 / I1IiI
 if 56 - 56: i11iIiiIii - iIii1I11I1II1 . OoOoOO00
 if 81 - 81: IIII / I1IiI * IIII . O0
 if 61 - 61: Ooo00oOo00o * OoOO0ooOOoo0O + O0oO . iIii1I11I1II1 % o0000oOoOoO0o . O0oO
 if 53 - 53: O0oO * IIII / iIii1I11I1II1 / OOOo0 % ii11ii1ii
def o00oOOooOOo0o ( ) :
 xbmc . executebuiltin ( 'UpdateLocalAddons' )
 xbmc . executebuiltin ( 'UpdateAddonRepos' )
 i1iiIII111ii = xbmcgui . Dialog ( )
 i1iiIII111ii . ok ( "GenieTv" , '' , '                                 REFRESH SUCCESSFUL :)' , "                          [COLOR gold]Brought To You By Kodi Support Group, GenieTv[/COLOR]" )
 return
 if 39 - 39: Ooo00oOo00o / OoooooooOO . Ooo00oOo00o * ii11ii1ii / I1IiI
 if 38 - 38: Ooo00oOo00o / o0oO0 % O0oO * o0000oOoOoO0o + i11iIiiIii % o0oO0
 if 61 - 61: O0oO - o00O0oo % ii11ii1ii / o0oO0 / oO0o0ooO0 + iIii1I11I1II1
 if 87 - 87: O0oO + o0oO0 + O0 / i1IIi % IIII / O0oO
 if 64 - 64: Ooo00oOo00o % IIII . O0oO % Ooo00oOo00o + o0000oOoOoO0o * IIII
 if 83 - 83: OOooOOo % OoOO + o0000oOoOoO0o % i11iIiiIii + O0
 if 65 - 65: iIii1I11I1II1 % OoOO + O0 / OoooooooOO
 if 52 - 52: o00O0oo % OoOO0ooOOoo0O * OOOo0 % o0000oOoOoO0o + OoOO0ooOOoo0O / oO0o0ooO0
 if 80 - 80: OoooooooOO + IIII
 if 95 - 95: O0oO / OoOO * O0oO - OoooooooOO * OoooooooOO % Ooo00oOo00o
 if 43 - 43: Oo . O0oO
 if 12 - 12: O0oO + OoOO0ooOOoo0O + o0000oOoOoO0o . IIII / o00O0oo
 if 29 - 29: IIII . o0oO0 - OoOoOO00
 if 68 - 68: iIii1I11I1II1 + OoOoOO00 / OoOO
 if 91 - 91: I1IiI % iIii1I11I1II1 . OOOo0
 if 70 - 70: o0000oOoOoO0o % OoOoOO00 % O0 . i1IIi / O0oO
 if 100 - 100: ii11ii1ii * i11iIiiIii % OoOO / Oo / o0oO0 + ii11ii1ii
 if 59 - 59: O0oO - IIII
 if 14 - 14: iIii1I11I1II1 - iIii1I11I1II1
 if 5 - 5: IIII
 if 84 - 84: OoOoOO00 * OoOO * OoOoOO00 % IIII / OOOo0
 if 100 - 100: IIII . o00O0oo - iIii1I11I1II1 . i11iIiiIii / OoOoOO00
 if 71 - 71: O0oO * Oo . o0000oOoOoO0o
 if 49 - 49: IIII * O0 . IIII
def ii1II1II ( url ) :
 O0ii1ii1ii = oooooOoo0ooo ( ooOoOoo0O + i11i11II11i ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 III1iII1I1ii = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( O0ii1ii1ii )
 for oOOo0 , url , oo00O00oO , iIiIIIi , ooo00OOOooO in III1iII1I1ii :
  ii11i1iIII ( oOOo0 , url , 42 , oo00O00oO , iIiIIIi , ooo00OOOooO )
 III1ii1iII ( 'movies' , 'MAIN' )
 if 9 - 9: I1IiI - ii11ii1ii * o0oO0 . o0oO0 - OOOo0
def OOooOooo0OOo0 ( url ) :
 O0ii1ii1ii = oooooOoo0ooo ( ooOoOoo0O + oo0o0OoOO0o0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 III1iII1I1ii = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( O0ii1ii1ii )
 for oOOo0 , url , oo00O00oO , iIiIIIi , ooo00OOOooO in III1iII1I1ii :
  ii11i1iIII ( oOOo0 , url , 42 , oo00O00oO , iIiIIIi , ooo00OOOooO )
 III1ii1iII ( 'movies' , 'MAIN' )
 if 14 - 14: OOooOOo % IIII + ii11ii1ii + Ooo00oOo00o
def OOOoOOo0o ( url ) :
 O0ii1ii1ii = oooooOoo0ooo ( ooOoOoo0O + IiI1Iii1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 III1iII1I1ii = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( O0ii1ii1ii )
 for oOOo0 , url , oo00O00oO , iIiIIIi , ooo00OOOooO in III1iII1I1ii :
  ii11i1iIII ( oOOo0 , url , 42 , oo00O00oO , iIiIIIi , ooo00OOOooO )
 III1ii1iII ( 'movies' , 'MAIN' )
 if 85 - 85: i11iIiiIii / i11iIiiIii . Ooo00oOo00o . O0
def OooOo ( url ) :
 O0ii1ii1ii = oooooOoo0ooo ( ooOoOoo0O + oOo0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 III1iII1I1ii = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( O0ii1ii1ii )
 for oOOo0 , url , oo00O00oO , iIiIIIi , ooo00OOOooO in III1iII1I1ii :
  ii11i1iIII ( oOOo0 , url , 42 , oo00O00oO , iIiIIIi , ooo00OOOooO )
 III1ii1iII ( 'movies' , 'MAIN' )
 if 30 - 30: OoOO0ooOOoo0O + OoOoOO00 - IIII * OoooooooOO
def I1iIiiiI1 ( url ) :
 O0ii1ii1ii = oooooOoo0ooo ( ooOoOoo0O + OOO0O00Oo ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 III1iII1I1ii = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( O0ii1ii1ii )
 for oOOo0 , url , oo00O00oO , iIiIIIi , ooo00OOOooO in III1iII1I1ii :
  ii11i1iIII ( oOOo0 , url , 42 , oo00O00oO , iIiIIIi , ooo00OOOooO )
 III1ii1iII ( 'movies' , 'MAIN' )
 if 13 - 13: iIii1I11I1II1
def IiIIII1iiIIi ( url ) :
 O0ii1ii1ii = oooooOoo0ooo ( ooOoOoo0O + i1I1IiI1ii ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 III1iII1I1ii = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( O0ii1ii1ii )
 for oOOo0 , url , oo00O00oO , iIiIIIi , ooo00OOOooO in III1iII1I1ii :
  ii11i1iIII ( oOOo0 , url , 42 , oo00O00oO , iIiIIIi , ooo00OOOooO )
 III1ii1iII ( 'movies' , 'MAIN' )
 if 64 - 64: oO0o0ooO0 * ii11ii1ii % OoOoOO00 - I1IiI + ii11ii1ii
def OO0OOoo0OOO ( url ) :
 O0ii1ii1ii = oooooOoo0ooo ( ooOoOoo0O + ooooOoo0OO ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 III1iII1I1ii = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( O0ii1ii1ii )
 for oOOo0 , url , oo00O00oO , iIiIIIi , ooo00OOOooO in III1iII1I1ii :
  ii11i1iIII ( oOOo0 , url , 42 , oo00O00oO , iIiIIIi , ooo00OOOooO )
 III1ii1iII ( 'movies' , 'MAIN' )
 if 85 - 85: OoOoOO00 . o0oO0 % OoOO0ooOOoo0O % o0000oOoOoO0o
def OOo00ooOoO0o ( url ) :
 O0ii1ii1ii = oooooOoo0ooo ( ooOoOoo0O + i1i1iiIIiiiII ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 III1iII1I1ii = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( O0ii1ii1ii )
 for oOOo0 , url , oo00O00oO , iIiIIIi , ooo00OOOooO in III1iII1I1ii :
  ii11i1iIII ( oOOo0 , url , 42 , oo00O00oO , iIiIIIi , ooo00OOOooO )
 III1ii1iII ( 'movies' , 'MAIN' )
 if 5 - 5: OoooooooOO / OOooOOo % o0000oOoOoO0o % Ooo00oOo00o * oO0o0ooO0 + iIii1I11I1II1
def I11iiI11iiI ( url ) :
 O0ii1ii1ii = oooooOoo0ooo ( ooOoOoo0O + OOO ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 III1iII1I1ii = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( O0ii1ii1ii )
 for oOOo0 , url , oo00O00oO , iIiIIIi , ooo00OOOooO in III1iII1I1ii :
  ii11i1iIII ( oOOo0 , url , 42 , oo00O00oO , iIiIIIi , ooo00OOOooO )
 III1ii1iII ( 'movies' , 'MAIN' )
 if 14 - 14: Ooo00oOo00o + i1IIi % OOOo0 % O0 - o00O0oo + Oo
def oOo0OOO00Oo ( url ) :
 O0ii1ii1ii = oooooOoo0ooo ( ooOoOoo0O + i1ii1ii1II1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 III1iII1I1ii = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( O0ii1ii1ii )
 for oOOo0 , url , oo00O00oO , iIiIIIi , ooo00OOOooO in III1iII1I1ii :
  ii11i1iIII ( oOOo0 , url , 5 , oo00O00oO , iIiIIIi , ooo00OOOooO )
 III1ii1iII ( 'movies' , 'MAIN' )
 if 6 - 6: OoOO0ooOOoo0O % OoOoOO00 - OoOO0ooOOoo0O + ii11ii1ii
 if 31 - 31: i11iIiiIii * OOooOOo / o0000oOoOoO0o * i1IIi + OOooOOo
 if 79 - 79: IIII % Ooo00oOo00o % OOOo0 / i11iIiiIii
 if 34 - 34: iIii1I11I1II1 % OoOoOO00 * ii11ii1ii . o00O0oo - OoooooooOO
 if 3 - 3: i1IIi - o0000oOoOoO0o % iIii1I11I1II1 * Oo . OoOO
 if 36 - 36: OoOO0ooOOoo0O
 if 13 - 13: I1IiI % o0oO0
 if 81 - 81: IIII - OOooOOo - Oo - o00O0oo / OoOO0ooOOoo0O % o0000oOoOoO0o
 if 52 - 52: ii11ii1ii / oO0o0ooO0
def i1ii1IIIII ( ) :
 try :
  if os . path . exists ( iiI1IiI ) == True :
   i1iiIII111ii = xbmcgui . Dialog ( )
   if i1iiIII111ii . yesno ( "Delete Thumbnails" , "[COLOR gold][B]##########WARNING ANDROID ONLY##########[/B][/COLOR]" , "This feature deletes your thumbnail folder and textures13.db" , "Are you sure you want to do proceed? This Can NOT Be Undone" ) :
    for iiI11ii1I1 , Ooo0OOoOoO0 , oOo0OOoO0 in os . walk ( iiI1IiI ) :
     oOOO0 = 0
     oOOO0 += len ( oOo0OOoO0 )
     if oOOO0 > 0 :
      for I1II1 in oOo0OOoO0 :
       os . unlink ( os . path . join ( iiI11ii1I1 , I1II1 ) )
  Iii1i11iiI1 = os . path . join ( O0OoO000O0OO , "Textures13.db" )
  os . unlink ( Iii1i11iiI1 )
  i1iiIII111ii . ok ( "Restart KODI" , "Please restart KODI to rebuild thumbnail library" )
 except :
  i1iiIII111ii = xbmcgui . Dialog ( )
  i1iiIII111ii . ok ( i11 , "Error Deleting Thumbnails please visit Kodi Support Group, GenieTv on facebook" )
 return
 if 95 - 95: OoOO * iIii1I11I1II1 + ii11ii1ii
 if 5 - 5: Oo
 if 100 - 100: o00O0oo + iIii1I11I1II1
 if 59 - 59: IIII
 if 89 - 89: I1IiI % iIii1I11I1II1
 if 35 - 35: ii11ii1ii + O0oO - I1IiI % OoOO % OOooOOo % I1IiI
 if 45 - 45: OOOo0 * OoOO0ooOOoo0O % Ooo00oOo00o
 if 24 - 24: o0oO0 - o0000oOoOoO0o * OoOO
 if 87 - 87: o00O0oo - ii11ii1ii % ii11ii1ii . OoOO / ii11ii1ii
def II1i ( url ) :
 print '############################################################       DELETING STANDARD CACHE             ###############################################################'
 o0II1IIi1iII1i = os . path . join ( xbmc . translatePath ( 'special://home' ) , 'cache' )
 if os . path . exists ( o0II1IIi1iII1i ) == True :
  for iiI11ii1I1 , Ooo0OOoOoO0 , oOo0OOoO0 in os . walk ( o0II1IIi1iII1i ) :
   oOOO0 = 0
   oOOO0 += len ( oOo0OOoO0 )
   if 26 - 26: O0
   if 17 - 17: OoOoOO00
   if oOOO0 > 0 :
    if 9 - 9: OoooooooOO + OoOO
    i1iiIII111ii = xbmcgui . Dialog ( )
    if i1iiIII111ii . yesno ( "Delete KODI Cache Files" , str ( oOOO0 ) + " files found" , "Do you want to delete them?" ) :
     if 33 - 33: O0
     for I1II1 in oOo0OOoO0 :
      try :
       os . unlink ( os . path . join ( iiI11ii1I1 , I1II1 ) )
      except :
       pass
     for iiI1ii in Ooo0OOoOoO0 :
      try :
       shutil . rmtree ( os . path . join ( iiI11ii1I1 , iiI1ii ) )
      except :
       pass
       if 76 - 76: o00O0oo + iIii1I11I1II1 + I1IiI . Ooo00oOo00o
   else :
    pass
 if xbmc . getCondVisibility ( 'system.platform.ATV2' ) :
  i1i1 = os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'Other' )
  if 68 - 68: o00O0oo - OOOo0
  for iiI11ii1I1 , Ooo0OOoOoO0 , oOo0OOoO0 in os . walk ( i1i1 ) :
   oOOO0 = 0
   oOOO0 += len ( oOo0OOoO0 )
   if 41 - 41: OoOO
   if oOOO0 > 0 :
    if 21 - 21: o0oO0 + OOooOOo % O0oO + i11iIiiIii + oO0o0ooO0 + OoOoOO00
    i1iiIII111ii = xbmcgui . Dialog ( )
    if i1iiIII111ii . yesno ( "Delete ATV2 Cache Files" , str ( oOOO0 ) + " files found in 'Other'" , "Do you want to delete them?" ) :
     if 98 - 98: O0oO
     for I1II1 in oOo0OOoO0 :
      os . unlink ( os . path . join ( iiI11ii1I1 , I1II1 ) )
     for iiI1ii in Ooo0OOoOoO0 :
      shutil . rmtree ( os . path . join ( iiI11ii1I1 , iiI1ii ) )
      if 49 - 49: Oo * OoOO + OOooOOo - i11iIiiIii
   else :
    pass
  OOooO = os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'LocalAndRental' )
  if 28 - 28: o0oO0 - OoOO0ooOOoo0O / OOOo0
  for iiI11ii1I1 , Ooo0OOoOoO0 , oOo0OOoO0 in os . walk ( OOooO ) :
   oOOO0 = 0
   oOOO0 += len ( oOo0OOoO0 )
   if 27 - 27: i1IIi + OOOo0 * ii11ii1ii + OoOO0ooOOoo0O . OoOO
   if oOOO0 > 0 :
    if 1 - 1: OoOO0ooOOoo0O * IIII + o0000oOoOoO0o
    i1iiIII111ii = xbmcgui . Dialog ( )
    if i1iiIII111ii . yesno ( "Delete ATV2 Cache Files" , str ( oOOO0 ) + " files found in 'LocalAndRental'" , "Do you want to delete them?" ) :
     if 77 - 77: OoOO % i11iIiiIii . OoOO0ooOOoo0O % OoOO0ooOOoo0O
     for I1II1 in oOo0OOoO0 :
      os . unlink ( os . path . join ( iiI11ii1I1 , I1II1 ) )
     for iiI1ii in Ooo0OOoOoO0 :
      shutil . rmtree ( os . path . join ( iiI11ii1I1 , iiI1ii ) )
      if 36 - 36: Oo % o00O0oo / i11iIiiIii % O0oO + Ooo00oOo00o
   else :
    pass
    if 23 - 23: OoOoOO00
    if 93 - 93: OoOO . o0000oOoOoO0o / i1IIi
    if 50 - 50: O0oO / i1IIi % OoooooooOO
    if 83 - 83: ii11ii1ii * ii11ii1ii + OoOO0ooOOoo0O
 OooooOoO = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.whatthefurk/cache' ) , '' )
 if os . path . exists ( OooooOoO ) == True :
  for iiI11ii1I1 , Ooo0OOoOoO0 , oOo0OOoO0 in os . walk ( OooooOoO ) :
   oOOO0 = 0
   oOOO0 += len ( oOo0OOoO0 )
   if 79 - 79: o0oO0 % OoOO0ooOOoo0O
   if 54 - 54: I1IiI - O0oO
   if oOOO0 > 0 :
    if 65 - 65: O0oO . o0oO0 + OoOO0ooOOoo0O / Oo + IIII % i1IIi
    i1iiIII111ii = xbmcgui . Dialog ( )
    if i1iiIII111ii . yesno ( "Delete WTF Cache Files" , str ( oOOO0 ) + " files found" , "Do you want to delete them?" ) :
     if 28 - 28: i11iIiiIii + O0 / ii11ii1ii
     for I1II1 in oOo0OOoO0 :
      os . unlink ( os . path . join ( iiI11ii1I1 , I1II1 ) )
     for iiI1ii in Ooo0OOoOoO0 :
      shutil . rmtree ( os . path . join ( iiI11ii1I1 , iiI1ii ) )
      if 3 - 3: Ooo00oOo00o * i1IIi . OOOo0 . O0 - I1IiI
   else :
    pass
    if 81 - 81: OOOo0 - iIii1I11I1II1 / OOOo0 / O0
    if 34 - 34: o00O0oo * o00O0oo - ii11ii1ii - O0 . i11iIiiIii
 IioOo0O = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.4od/cache' ) , '' )
 if os . path . exists ( IioOo0O ) == True :
  for iiI11ii1I1 , Ooo0OOoOoO0 , oOo0OOoO0 in os . walk ( IioOo0O ) :
   oOOO0 = 0
   oOOO0 += len ( oOo0OOoO0 )
   if 30 - 30: o00O0oo . ii11ii1ii / OoOO0ooOOoo0O
   if 2 - 2: IIII % OOOo0 - O0oO
   if oOOO0 > 0 :
    if 79 - 79: OoooooooOO / ii11ii1ii . O0
    i1iiIII111ii = xbmcgui . Dialog ( )
    if i1iiIII111ii . yesno ( "Delete 4oD Cache Files" , str ( oOOO0 ) + " files found" , "Do you want to delete them?" ) :
     if 79 - 79: OoOO - OoOoOO00
     for I1II1 in oOo0OOoO0 :
      os . unlink ( os . path . join ( iiI11ii1I1 , I1II1 ) )
     for iiI1ii in Ooo0OOoOoO0 :
      shutil . rmtree ( os . path . join ( iiI11ii1I1 , iiI1ii ) )
      if 43 - 43: i1IIi + O0 % Ooo00oOo00o / o00O0oo * OOOo0
   else :
    pass
    if 89 - 89: OOOo0 . Oo + ii11ii1ii . O0 % OOooOOo
    if 84 - 84: OoooooooOO + O0oO / OOOo0 % OoOO0ooOOoo0O % ii11ii1ii * OOOo0
 OOoO0oooo = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.iplayer/iplayer_http_cache' ) , '' )
 if os . path . exists ( OOoO0oooo ) == True :
  for iiI11ii1I1 , Ooo0OOoOoO0 , oOo0OOoO0 in os . walk ( OOoO0oooo ) :
   oOOO0 = 0
   oOOO0 += len ( oOo0OOoO0 )
   if 24 - 24: o0000oOoOoO0o / OOOo0 * i1IIi % OoooooooOO
   if 99 - 99: i11iIiiIii . OoOoOO00 . OoooooooOO
   if oOOO0 > 0 :
    if 59 - 59: i11iIiiIii . OoooooooOO / o0000oOoOoO0o * ii11ii1ii + OoooooooOO
    i1iiIII111ii = xbmcgui . Dialog ( )
    if i1iiIII111ii . yesno ( "Delete BBC iPlayer Cache Files" , str ( oOOO0 ) + " files found" , "Do you want to delete them?" ) :
     if 3 - 3: i11iIiiIii * Oo % iIii1I11I1II1 % OOOo0 * oO0o0ooO0 / OoOO0ooOOoo0O
     for I1II1 in oOo0OOoO0 :
      os . unlink ( os . path . join ( iiI11ii1I1 , I1II1 ) )
     for iiI1ii in Ooo0OOoOoO0 :
      shutil . rmtree ( os . path . join ( iiI11ii1I1 , iiI1ii ) )
      if 95 - 95: IIII * O0 * O0oO . OoooooooOO % Oo + ii11ii1ii
   else :
    pass
    if 98 - 98: OoOO . OoooooooOO
    if 54 - 54: O0 / IIII % o0oO0 * i1IIi * O0
    if 48 - 48: OOooOOo . OoOO % I1IiI - I1IiI
 i1IiI1Iiii = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/script.module.simple.downloader' ) , '' )
 if os . path . exists ( i1IiI1Iiii ) == True :
  for iiI11ii1I1 , Ooo0OOoOoO0 , oOo0OOoO0 in os . walk ( i1IiI1Iiii ) :
   oOOO0 = 0
   oOOO0 += len ( oOo0OOoO0 )
   if 87 - 87: IIII / O0oO - Oo
   if 56 - 56: O0
   if oOOO0 > 0 :
    if 45 - 45: I1IiI - Ooo00oOo00o - I1IiI
    i1iiIII111ii = xbmcgui . Dialog ( )
    if i1iiIII111ii . yesno ( "Delete Simple Downloader Cache Files" , str ( oOOO0 ) + " files found" , "Do you want to delete them?" ) :
     if 41 - 41: Oo / i1IIi / Oo - oO0o0ooO0 . OOooOOo
     for I1II1 in oOo0OOoO0 :
      os . unlink ( os . path . join ( iiI11ii1I1 , I1II1 ) )
     for iiI1ii in Ooo0OOoOoO0 :
      shutil . rmtree ( os . path . join ( iiI11ii1I1 , iiI1ii ) )
      if 65 - 65: O0 * i11iIiiIii . OoooooooOO / OOOo0 / oO0o0ooO0
   else :
    pass
    if 69 - 69: o0oO0 % o0oO0
    if 76 - 76: i11iIiiIii * oO0o0ooO0 / Ooo00oOo00o % ii11ii1ii + OoOO0ooOOoo0O
 IiIi1II111I = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.itv/Images' ) , '' )
 if os . path . exists ( IiIi1II111I ) == True :
  for iiI11ii1I1 , Ooo0OOoOoO0 , oOo0OOoO0 in os . walk ( IiIi1II111I ) :
   oOOO0 = 0
   oOOO0 += len ( oOo0OOoO0 )
   if 80 - 80: o00O0oo / OoOO0ooOOoo0O
   if 21 - 21: Oo - iIii1I11I1II1 - O0oO
   if oOOO0 > 0 :
    if 1 - 1: OOOo0 * OoOO0ooOOoo0O + o00O0oo + OOOo0 - i11iIiiIii
    i1iiIII111ii = xbmcgui . Dialog ( )
    if i1iiIII111ii . yesno ( "Delete ITV Cache Files" , str ( oOOO0 ) + " files found" , "Do you want to delete them?" ) :
     if 79 - 79: o0oO0 . OoOO / OoOO - o0oO0 * Oo / OOooOOo
     for I1II1 in oOo0OOoO0 :
      os . unlink ( os . path . join ( iiI11ii1I1 , I1II1 ) )
     for iiI1ii in Ooo0OOoOoO0 :
      shutil . rmtree ( os . path . join ( iiI11ii1I1 , iiI1ii ) )
      if 19 - 19: ii11ii1ii
   else :
    pass
    if 46 - 46: iIii1I11I1II1 . i11iIiiIii - I1IiI % O0 / OoOoOO00 * i1IIi
    if 66 - 66: O0
 oOooOOo00ooO = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.movies4me/cache' ) , '' )
 if os . path . exists ( IiIi1II111I ) == True :
  for iiI11ii1I1 , Ooo0OOoOoO0 , oOo0OOoO0 in os . walk ( oOooOOo00ooO ) :
   oOOO0 = 0
   oOOO0 += len ( oOo0OOoO0 )
   if 71 - 71: O0oO - OOooOOo - OoOO0ooOOoo0O
   if 28 - 28: iIii1I11I1II1
   if oOOO0 > 0 :
    if 7 - 7: OOooOOo % IIII * I1IiI
    i1iiIII111ii = xbmcgui . Dialog ( )
    if i1iiIII111ii . yesno ( "Delete Movies4me Cache Files" , str ( oOOO0 ) + " files found" , "Do you want to delete them?" ) :
     if 58 - 58: IIII / o0000oOoOoO0o + OoOoOO00 % oO0o0ooO0 - OoooooooOO
     for I1II1 in oOo0OOoO0 :
      os . unlink ( os . path . join ( iiI11ii1I1 , I1II1 ) )
     for iiI1ii in Ooo0OOoOoO0 :
      shutil . rmtree ( os . path . join ( iiI11ii1I1 , iiI1ii ) )
      if 25 - 25: I1IiI % OoooooooOO * Oo - i1IIi * OoOoOO00 * OoOO
   else :
    pass
    if 30 - 30: o0000oOoOoO0o % I1IiI / ii11ii1ii * O0 * o00O0oo . OOOo0
    if 46 - 46: I1IiI - O0
 O00Ooo = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.phstreams/Cache' ) , '' )
 if os . path . exists ( IiIi1II111I ) == True :
  for iiI11ii1I1 , Ooo0OOoOoO0 , oOo0OOoO0 in os . walk ( O00Ooo ) :
   oOOO0 = 0
   oOOO0 += len ( oOo0OOoO0 )
   if 92 - 92: I1IiI % O0
   if 55 - 55: iIii1I11I1II1 * oO0o0ooO0
   if oOOO0 > 0 :
    if 85 - 85: iIii1I11I1II1 . OoOoOO00
    i1iiIII111ii = xbmcgui . Dialog ( )
    if i1iiIII111ii . yesno ( "Delete Phoenix Cache Files" , str ( oOOO0 ) + " files found" , "Do you want to delete them?" ) :
     if 54 - 54: o00O0oo . OoooooooOO % Oo
     for I1II1 in oOo0OOoO0 :
      os . unlink ( os . path . join ( iiI11ii1I1 , I1II1 ) )
     for iiI1ii in Ooo0OOoOoO0 :
      shutil . rmtree ( os . path . join ( iiI11ii1I1 , iiI1ii ) )
      if 22 - 22: OoOO0ooOOoo0O
   else :
    pass
    if 22 - 22: oO0o0ooO0 * o0000oOoOoO0o - Oo * O0 / i11iIiiIii
    if 78 - 78: Oo * O0 / o0oO0 + OoooooooOO + OoOO0ooOOoo0O
 I1iiIiiIiiI = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.spotitube/cache' ) , '' )
 if os . path . exists ( IiIi1II111I ) == True :
  for iiI11ii1I1 , Ooo0OOoOoO0 , oOo0OOoO0 in os . walk ( I1iiIiiIiiI ) :
   oOOO0 = 0
   oOOO0 += len ( oOo0OOoO0 )
   if 94 - 94: i1IIi
   if 36 - 36: OOOo0 + Oo
   if oOOO0 > 0 :
    if 46 - 46: oO0o0ooO0
    i1iiIII111ii = xbmcgui . Dialog ( )
    if i1iiIII111ii . yesno ( "Delete YouTube Music Cache Files" , str ( oOOO0 ) + " files found" , "Do you want to delete them?" ) :
     if 65 - 65: i1IIi . ii11ii1ii / o0oO0
     for I1II1 in oOo0OOoO0 :
      os . unlink ( os . path . join ( iiI11ii1I1 , I1II1 ) )
     for iiI1ii in Ooo0OOoOoO0 :
      shutil . rmtree ( os . path . join ( iiI11ii1I1 , iiI1ii ) )
      if 11 - 11: IIII * o0oO0 / o0oO0 - OoOO0ooOOoo0O
   else :
    pass
    if 68 - 68: OOOo0 % IIII - IIII / OOOo0 + ii11ii1ii - Oo
    if 65 - 65: o0oO0 - i1IIi
 O00Oo = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.supercartoons/cache' ) , '' )
 if os . path . exists ( IiIi1II111I ) == True :
  for iiI11ii1I1 , Ooo0OOoOoO0 , oOo0OOoO0 in os . walk ( O00Oo ) :
   oOOO0 = 0
   oOOO0 += len ( oOo0OOoO0 )
   if 38 - 38: i1IIi . i11iIiiIii
   if 93 - 93: o0000oOoOoO0o * OoOoOO00 / o00O0oo - OOooOOo
   if oOOO0 > 0 :
    if 98 - 98: i11iIiiIii / OOOo0 * OOooOOo / O0oO
    i1iiIII111ii = xbmcgui . Dialog ( )
    if i1iiIII111ii . yesno ( "Delete SuperCartoons Cache Files" , str ( oOOO0 ) + " files found" , "Do you want to delete them?" ) :
     if 67 - 67: o0000oOoOoO0o % OoOO
     for I1II1 in oOo0OOoO0 :
      os . unlink ( os . path . join ( iiI11ii1I1 , I1II1 ) )
     for iiI1ii in Ooo0OOoOoO0 :
      shutil . rmtree ( os . path . join ( iiI11ii1I1 , iiI1ii ) )
      if 39 - 39: i11iIiiIii + IIII
   else :
    pass
    if 7 - 7: iIii1I11I1II1 - i1IIi
    if 10 - 10: O0oO % O0 / OOOo0 % o0000oOoOoO0o
 iiII = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.tvonline.cc/cache' ) , '' )
 if os . path . exists ( IiIi1II111I ) == True :
  for iiI11ii1I1 , Ooo0OOoOoO0 , oOo0OOoO0 in os . walk ( iiII ) :
   oOOO0 = 0
   oOOO0 += len ( oOo0OOoO0 )
   if 28 - 28: o0oO0 . OoooooooOO + OOooOOo + o00O0oo % oO0o0ooO0
   if 80 - 80: Oo
   if oOOO0 > 0 :
    if 86 - 86: ii11ii1ii * o0000oOoOoO0o . I1IiI / Oo + OoOO
    i1iiIII111ii = xbmcgui . Dialog ( )
    if i1iiIII111ii . yesno ( "Delete TVonline Cache Files" , str ( oOOO0 ) + " files found" , "Do you want to delete them?" ) :
     if 8 - 8: I1IiI
     for I1II1 in oOo0OOoO0 :
      os . unlink ( os . path . join ( iiI11ii1I1 , I1II1 ) )
     for iiI1ii in Ooo0OOoOoO0 :
      shutil . rmtree ( os . path . join ( iiI11ii1I1 , iiI1ii ) )
      if 16 - 16: OOooOOo . o0000oOoOoO0o
   else :
    pass
    if 50 - 50: o0oO0 * I1IiI + ii11ii1ii - i11iIiiIii + Oo * ii11ii1ii
    if 20 - 20: O0oO / OOooOOo % I1IiI
 O00oo0O00 = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.youtube/kodion' ) , '' )
 if os . path . exists ( IiIi1II111I ) == True :
  for iiI11ii1I1 , Ooo0OOoOoO0 , oOo0OOoO0 in os . walk ( O00oo0O00 ) :
   oOOO0 = 0
   oOOO0 += len ( oOo0OOoO0 )
   if 65 - 65: OoOO0ooOOoo0O + OoOoOO00
   if 61 - 61: i11iIiiIii * OoOO % Oo * O0oO - OoooooooOO - Ooo00oOo00o
   if oOOO0 > 0 :
    if 83 - 83: o0oO0 / OoOO0ooOOoo0O
    i1iiIII111ii = xbmcgui . Dialog ( )
    if i1iiIII111ii . yesno ( "Delete YouTube Cache Files" , str ( oOOO0 ) + " files found" , "Do you want to delete them?" ) :
     if 39 - 39: IIII + o0000oOoOoO0o
     for I1II1 in oOo0OOoO0 :
      os . unlink ( os . path . join ( iiI11ii1I1 , I1II1 ) )
     for iiI1ii in Ooo0OOoOoO0 :
      shutil . rmtree ( os . path . join ( iiI11ii1I1 , iiI1ii ) )
      if 9 - 9: OOOo0 % o0000oOoOoO0o . Oo * OOOo0
   else :
    pass
    if 99 - 99: O0 . OOooOOo % o0000oOoOoO0o - Oo / o0000oOoOoO0o
    if 20 - 20: I1IiI * oO0o0ooO0
    if 19 - 19: OoooooooOO
 oOOO0ooOoOOO = xbmc . translatePath ( 'special://masterprofile/addon_data/plugin.video.genesis' )
 i1iiIII111ii = xbmcgui . Dialog ( )
 try :
  if i1iiIII111ii . yesno ( "Delete Genesis Cache Files" , "Do you want to delete cache" ) :
   o0IiIiI111IIII1 = os . path . join ( oOOO0ooOoOOO , "cache.db" )
   os . unlink ( o0IiIiI111IIII1 )
   if 100 - 100: OoOO0ooOOoo0O * O0 + OOOo0 + I1IiI . OoOO0ooOOoo0O
 except :
  pass
  if 73 - 73: OoOO . OoOoOO00 * oO0o0ooO0 % OoOO + I1IiI - Ooo00oOo00o
 i1iiIII111ii = xbmcgui . Dialog ( )
 i1iiIII111ii . ok ( "GenieTv" , "                               Finished Deleting Cache " , "                          [COLOR gold]Brought To You By GenieTv[/COLOR]" )
 if 19 - 19: oO0o0ooO0 * Oo . oO0o0ooO0 . Ooo00oOo00o / Ooo00oOo00o - OoOO
 if 9 - 9: O0oO * IIII * O0oO
 if 74 - 74: iIii1I11I1II1 / OOooOOo
 if 58 - 58: iIii1I11I1II1 - OOOo0 % OOooOOo % OoooooooOO * iIii1I11I1II1 + OoOO0ooOOoo0O
 if 25 - 25: OoOO0ooOOoo0O % O0
 if 44 - 44: O0oO . o00O0oo * OoOoOO00 / IIII + iIii1I11I1II1
 if 14 - 14: O0 % IIII % o00O0oo * OoOO
 if 65 - 65: o0000oOoOoO0o % OoOO + ii11ii1ii
 if 86 - 86: iIii1I11I1II1 / O0 . O0oO % iIii1I11I1II1 % Oo
def OooO00oO ( url ) :
 print '###' + i11 + ' - DELETING PACKAGES###'
 OOoOOOo0 = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' , '' ) )
 try :
  for iiI11ii1I1 , Ooo0OOoOoO0 , oOo0OOoO0 in os . walk ( OOoOOOo0 ) :
   oOOO0 = 0
   oOOO0 += len ( oOo0OOoO0 )
   if 84 - 84: OoOO + OoOO0ooOOoo0O . oO0o0ooO0
   if 71 - 71: o0oO0 / o0oO0 . I1IiI % oO0o0ooO0
   if oOOO0 > 0 :
    if 50 - 50: o0oO0 + oO0o0ooO0 / o0000oOoOoO0o / o0000oOoOoO0o % O0
    i1iiIII111ii = xbmcgui . Dialog ( )
    if i1iiIII111ii . yesno ( "Delete Package Cache Files" , str ( oOOO0 ) + " files found" , "Do you want to delete them?" ) :
     if 87 - 87: Oo + o0oO0
     for I1II1 in oOo0OOoO0 :
      os . unlink ( os . path . join ( iiI11ii1I1 , I1II1 ) )
     for iiI1ii in Ooo0OOoOoO0 :
      shutil . rmtree ( os . path . join ( iiI11ii1I1 , iiI1ii ) )
     i1iiIII111ii = xbmcgui . Dialog ( )
     i1iiIII111ii . ok ( i11 , "       Deleting Packages all done" )
    else :
     pass
   else :
    i1iiIII111ii = xbmcgui . Dialog ( )
    i1iiIII111ii . ok ( i11 , "       No Packages to DELETE" )
 except :
  i1iiIII111ii = xbmcgui . Dialog ( )
  i1iiIII111ii . ok ( i11 , "Error Deleting Packages please visit Kodi Support Group, GenieTv on facebook" )
 return
 if 66 - 66: OOooOOo * OoOO0ooOOoo0O + o00O0oo * OOooOOo + OoOO0ooOOoo0O / OoooooooOO
 if 86 - 86: o00O0oo . oO0o0ooO0 - oO0o0ooO0
 if 71 - 71: iIii1I11I1II1 . OoOoOO00 % iIii1I11I1II1
 if 22 - 22: i11iIiiIii % ii11ii1ii % o0oO0 % o0oO0 . Ooo00oOo00o
 if 85 - 85: o0oO0 . O0 / OoOO0ooOOoo0O * o0oO0 - Ooo00oOo00o - i11iIiiIii
 if 25 - 25: o0oO0 % Oo - OoOO0ooOOoo0O
 if 80 - 80: IIII % OoOoOO00 - Oo - iIii1I11I1II1
 if 9 - 9: OOooOOo % ii11ii1ii . ii11ii1ii
 if 28 - 28: OoooooooOO % OoOO + ii11ii1ii + O0 . O0oO
def ooOO0OOO00o ( url , name ) :
 oOo00O0oo00o0 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 OoOoO0ooooO0 = os . path . join ( oOo00O0oo00o0 , 'advancedsettings.xml' )
 i1iiIII111ii = xbmcgui . Dialog ( )
 IIII1ii1 = os . path . join ( oOo00O0oo00o0 , 'advancedsettings.xml.bak' )
 if os . path . exists ( IIII1ii1 ) == False :
  if i1iiIII111ii . yesno ( "Back Up Original" , 'Have You Backed Up Your Original?' , '' , "[B][COLOR red]     AS YOU CANNOT GO BACK !!![/B][/COLOR]" ) :
   print '###' + i11 + ' - ADVANCED XML###'
   oOo00O0oo00o0 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
   OoOoO0ooooO0 = os . path . join ( oOo00O0oo00o0 , 'advancedsettings.xml' )
   try :
    os . remove ( OoOoO0ooooO0 )
    print '=== GenieTv - REMOVING    ' + str ( OoOoO0ooooO0 ) + '    ==='
   except :
    pass
   O0ii1ii1ii = I11 . http_GET ( url ) . content
   IIo0Oo0oO0oOO00 = open ( OoOoO0ooooO0 , "w" )
   IIo0Oo0oO0oOO00 . write ( O0ii1ii1ii )
   IIo0Oo0oO0oOO00 . close ( )
   print '=== GenieTv - WRITING NEW    ' + str ( OoOoO0ooooO0 ) + '    ==='
   i1iiIII111ii = xbmcgui . Dialog ( )
   i1iiIII111ii . ok ( i11 , "       Done Adding new Advanced XML" )
 else :
  print '###' + i11 + ' - ADVANCED XML###'
  oOo00O0oo00o0 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
  OoOoO0ooooO0 = os . path . join ( oOo00O0oo00o0 , 'advancedsettings.xml' )
  try :
   os . remove ( OoOoO0ooooO0 )
   print '=== GenieTv - REMOVING    ' + str ( OoOoO0ooooO0 ) + '    ==='
  except :
   pass
  O0ii1ii1ii = I11 . http_GET ( url ) . content
  IIo0Oo0oO0oOO00 = open ( OoOoO0ooooO0 , "w" )
  IIo0Oo0oO0oOO00 . write ( O0ii1ii1ii )
  IIo0Oo0oO0oOO00 . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( OoOoO0ooooO0 ) + '    ==='
  i1iiIII111ii = xbmcgui . Dialog ( )
  i1iiIII111ii . ok ( i11 , "       Done Adding new Advanced XML" )
 return
 if 52 - 52: Ooo00oOo00o - OoOO0ooOOoo0O - o0oO0 - OOooOOo + i1IIi
def Iii1 ( url , name ) :
 print '###' + i11 + ' - CHECK ADVANCE XML###'
 oOo00O0oo00o0 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 OoOoO0ooooO0 = os . path . join ( oOo00O0oo00o0 , 'advancedsettings.xml' )
 try :
  IIo0Oo0oO0oOO00 = open ( OoOoO0ooooO0 ) . read ( )
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
 i1iiIII111ii = xbmcgui . Dialog ( )
 i1iiIII111ii . ok ( i11 , "[COLOR yellow]YOU HAVE[/COLOR] " + name + "[COLOR yellow] XML SETTINGS SETUP[/COLOR]" )
 return
 if 96 - 96: Oo / OoOO . OoOoOO00 . Oo
def ooIi111iII ( url ) :
 print '###' + i11 + ' - DELETING ADVANCE XML###'
 oOo00O0oo00o0 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 OoOoO0ooooO0 = os . path . join ( oOo00O0oo00o0 , 'advancedsettings.xml' )
 try :
  os . remove ( OoOoO0ooooO0 )
  i1iiIII111ii = xbmcgui . Dialog ( )
  print '=== GenieTv - DELETING    ' + str ( OoOoO0ooooO0 ) + '    ==='
  i1iiIII111ii . ok ( i11 , "       Remove Advanced Settings Sucessfull" )
 except :
  i1iiIII111ii = xbmcgui . Dialog ( )
  i1iiIII111ii . ok ( i11 , "       No Advanced Settings To Remove" )
 return
 if 83 - 83: OoooooooOO + Ooo00oOo00o * OoOO . O0
 if 13 - 13: OOooOOo
 if 7 - 7: OOOo0 + IIII / i11iIiiIii / Oo
 if 97 - 97: O0oO . o0000oOoOoO0o / OOOo0
 if 83 - 83: o0000oOoOoO0o - ii11ii1ii * OoOO
 if 90 - 90: Oo * OOOo0
 if 75 - 75: ii11ii1ii - I1IiI * i11iIiiIii . OoooooooOO - Oo . o0000oOoOoO0o
 if 6 - 6: o0000oOoOoO0o * OoOO / OoooooooOO % o00O0oo * OOooOOo
 if 28 - 28: IIII * OOOo0 % IIII
 if 95 - 95: O0 / o0000oOoOoO0o . O0oO
def iII11II1II ( url = 'http://www.iplocation.net/' , inc = 1 ) :
 III1iII1I1ii = re . compile ( "<td width='80'>(.+?)</td><td>(.+?)</td><td>(.+?)</td><td>.+?</td><td>(.+?)</td>" ) . findall ( I11 . http_GET ( url ) . content )
 for OOO00000o0 , OOOO000Ooo0O , oOo0oOooo0O , iI1iIIIIIiIi1 in III1iII1I1ii :
  if inc < 2 : i1iiIII111ii = xbmcgui . Dialog ( ) ; i1iiIII111ii . ok ( 'Check My IP' , "[B][COLOR gold]Your IP Address is: [/COLOR][/B] %s" % OOO00000o0 , '[B][COLOR gold]Your IP is based in: [/COLOR][/B] %s' % oOo0oOooo0O , '[B][COLOR gold]Your Service Provider is:[/COLOR][/B] %s' % iI1iIIIIIiIi1 )
  inc = inc + 1
  if 19 - 19: I1IiI . OOooOOo . OoooooooOO
  if 13 - 13: OoOO0ooOOoo0O . Oo / OoOoOO00
  if 43 - 43: iIii1I11I1II1 % Ooo00oOo00o
  if 84 - 84: Oo
  if 44 - 44: OoooooooOO * i11iIiiIii / Oo
  if 75 - 75: OoooooooOO . OoOO0ooOOoo0O + Ooo00oOo00o / o00O0oo - OOOo0 % o00O0oo
  if 89 - 89: oO0o0ooO0 * iIii1I11I1II1 + i11iIiiIii . OoooooooOO
  if 51 - 51: OoOO0ooOOoo0O / o0oO0 + Ooo00oOo00o % I1IiI / o00O0oo
  if 25 - 25: OOooOOo
def I1i1i111Ii1I ( url , name ) :
 i1iiIII111ii = xbmcgui . Dialog ( )
 if i1iiIII111ii . yesno ( "GenieTv" , '                                    Install Latest .ini File' ) :
  print '###' + i11 + ' - CUSTOM FTV INI###'
  oOo00O0oo00o0 = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/script.ftvguide' , '' ) )
  OoOoO0ooooO0 = os . path . join ( oOo00O0oo00o0 , 'addons2.ini' )
  O0ii1ii1ii = I11 . http_GET ( url ) . content
  IIo0Oo0oO0oOO00 = open ( OoOoO0ooooO0 , "w" )
  IIo0Oo0oO0oOO00 . write ( O0ii1ii1ii )
  IIo0Oo0oO0oOO00 . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( OoOoO0ooooO0 ) + '    ==='
  i1iiIII111ii = xbmcgui . Dialog ( )
  i1iiIII111ii . ok ( i11 , "                               Done Adding New .ini File" )
 return
 if 64 - 64: i11iIiiIii . o0oO0
def oooOoOoOO ( url , name ) :
 i1iiIII111ii = xbmcgui . Dialog ( )
 if i1iiIII111ii . yesno ( "GenieTv" , '                               Install Custom Settings' ) :
  print '###' + i11 + ' - CUSTOM FTV SETTINGS###'
  oOo00O0oo00o0 = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/script.ftvguide' , '' ) )
  OoOoO0ooooO0 = os . path . join ( oOo00O0oo00o0 , 'settings.xml' )
  O0ii1ii1ii = I11 . http_GET ( url ) . content
  IIo0Oo0oO0oOO00 = open ( OoOoO0ooooO0 , "w" )
  IIo0Oo0oO0oOO00 . write ( O0ii1ii1ii )
  IIo0Oo0oO0oOO00 . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( OoOoO0ooooO0 ) + '    ==='
  i1iiIII111ii = xbmcgui . Dialog ( )
  i1iiIII111ii . ok ( i11 , "                               Done Adding New Settings" )
 return
 if 51 - 51: OoOoOO00 / Oo / OOOo0 + i11iIiiIii
 if 5 - 5: o0000oOoOoO0o
def iii1IiiiI1i1 ( ) :
 try :
  IIIiI1i1 = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/script.ftvguide' , '' ) )
  if os . path . exists ( IIIiI1i1 ) == True :
   i1iiIII111ii = xbmcgui . Dialog ( )
   if i1iiIII111ii . yesno ( "GenieTv" , "                               Delete FTV Guide Database" ) :
    IIi11iII11i1 = os . path . join ( IIIiI1i1 , "source.db" )
    os . unlink ( IIi11iII11i1 )
  i1iiIII111ii . ok ( "GenieTv" , "                                     FTV Database Reset" )
 except :
  i1iiIII111ii = xbmcgui . Dialog ( )
  i1iiIII111ii . ok ( i11 , "               Error Deleting Database No Database To Delete" )
 return
 if 5 - 5: OoOoOO00 - IIII
 if 86 - 86: IIII * o0000oOoOoO0o + O0 * O0oO + i11iIiiIii - ii11ii1ii
 if 70 - 70: i11iIiiIii
 if 57 - 57: o0000oOoOoO0o % OoOO0ooOOoo0O + o0oO0 * o00O0oo . Oo
 if 78 - 78: OoooooooOO / i1IIi . OoOO0ooOOoo0O
def oooooOoo0ooo ( url ) :
 oOOoo0 = urllib2 . Request ( url )
 oOOoo0 . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
 i1111IIiii1 = urllib2 . urlopen ( oOOoo0 )
 O0ii1ii1ii = i1111IIiii1 . read ( )
 i1111IIiii1 . close ( )
 return O0ii1ii1ii
 if 88 - 88: o0000oOoOoO0o + OOOo0 - o0000oOoOoO0o / OoooooooOO - i11iIiiIii
 if 24 - 24: iIii1I11I1II1
 if 89 - 89: o00O0oo / i1IIi - OOooOOo % OOOo0 . Oo - O0
 if 71 - 71: Ooo00oOo00o % OOOo0 - oO0o0ooO0 . oO0o0ooO0
 if 22 - 22: o0oO0 / o0oO0 - o00O0oo % o0000oOoOoO0o . OoOO0ooOOoo0O + IIII
 if 64 - 64: i1IIi % ii11ii1ii / o00O0oo % OoooooooOO
 if 24 - 24: O0oO + OoooooooOO . IIII / I1IiI / o0000oOoOoO0o
def ooOoo ( params ) :
 plugintools . log ( "freshstart.main_list " + repr ( params ) ) ; OO0Oo00Oo = plugintools . message_yes_no ( i11 , "Do you wish to restore your" , "Kodi configuration to default settings?" )
 if OO0Oo00Oo :
  iIi = xbmcaddon . Addon ( id = oOOoo00O0O ) . getAddonInfo ( 'path' ) ; iIi = xbmc . translatePath ( iIi ) ;
  O0OoOOoooo = os . path . join ( iIi , ".." , ".." ) ; O0OoOOoooo = os . path . abspath ( O0OoOOoooo ) ; plugintools . log ( "freshstart.main_list xbmcPath=" + O0OoOOoooo ) ; O0oIi1iIiIi1I11 = False
  try :
   for iiI11ii1I1 , Ooo0OOoOoO0 , oOo0OOoO0 in os . walk ( O0OoOOoooo , topdown = True ) :
    Ooo0OOoOoO0 [ : ] = [ iiI1ii for iiI1ii in Ooo0OOoOoO0 if iiI1ii not in Oo0oO0ooo ]
    for oOOo0 in oOo0OOoO0 :
     try : os . remove ( os . path . join ( iiI11ii1I1 , oOOo0 ) )
     except :
      if oOOo0 not in [ "Addons15.db" , "MyVideos75.db" , "Textures13.db" , "xbmc.log" ] : O0oIi1iIiIi1I11 = True
      plugintools . log ( "Error removing " + iiI11ii1I1 + " " + oOOo0 )
    for oOOo0 in Ooo0OOoOoO0 :
     try : os . rmdir ( os . path . join ( iiI11ii1I1 , oOOo0 ) )
     except :
      if oOOo0 not in [ "Database" , "userdata" ] : O0oIi1iIiIi1I11 = True
      plugintools . log ( "Error removing " + iiI11ii1I1 + " " + oOOo0 )
   if not O0oIi1iIiIi1I11 : plugintools . log ( "freshstart.main_list All user files removed, you now have a clean install" ) ; plugintools . message ( i11 , "The process is complete, you're now back to a fresh Kodi configuration with GenieTv!" , "Please reboot your system or restart Kodi in order for the changes to be applied." )
   else : plugintools . log ( "freshstart.main_list User files partially removed" ) ; plugintools . message ( i11 , "The process is complete, you're now back to a fresh Kodi configuration with GenieTv" , "Please reboot your system or restart Kodi in order for the changes to be applied." )
  except : plugintools . message ( i11 , "Problem found" , "Your settings has not been changed" ) ; import traceback ; plugintools . log ( traceback . format_exc ( ) ) ; plugintools . log ( "freshstart.main_list NOT removed" )
  plugintools . add_item ( action = "" , title = "Now Exit Kodi" , folder = False )
 else : plugintools . message ( i11 , "Your settings" , "has not been changed" ) ; plugintools . add_item ( action = "" , title = "Done" , folder = False )
 OoOOoOooooOOo ( )
 if 12 - 12: iIii1I11I1II1 . o0oO0
 if 36 - 36: O0oO . IIII * OoooooooOO - OOooOOo
 if 60 - 60: OoOO0ooOOoo0O . oO0o0ooO0 / iIii1I11I1II1 + OoOO0ooOOoo0O * O0oO
def OoooO00OoO0 ( ) :
 iiIiI1I1I1IiI = [ ]
 I1IIII11 = sys . argv [ 2 ]
 if len ( I1IIII11 ) >= 2 :
  o0I1iI111ii111i = sys . argv [ 2 ]
  o00iI1Ii11iIiiI1 = o0I1iI111ii111i . replace ( '?' , '' )
  if ( o0I1iI111ii111i [ len ( o0I1iI111ii111i ) - 1 ] == '/' ) :
   o0I1iI111ii111i = o0I1iI111ii111i [ 0 : len ( o0I1iI111ii111i ) - 2 ]
  i11iII11ii = o00iI1Ii11iIiiI1 . split ( '&' )
  iiIiI1I1I1IiI = { }
  for oOo000O00O0 in range ( len ( i11iII11ii ) ) :
   iI1iiIii1I11I = { }
   iI1iiIii1I11I = i11iII11ii [ oOo000O00O0 ] . split ( '=' )
   if ( len ( iI1iiIii1I11I ) ) == 2 :
    iiIiI1I1I1IiI [ iI1iiIii1I11I [ 0 ] ] = iI1iiIii1I11I [ 1 ]
    if 32 - 32: OoooooooOO % OoOO % iIii1I11I1II1 / O0
 return iiIiI1I1I1IiI
 if 61 - 61: OoOoOO00 . O0 - o00O0oo - ii11ii1ii / i11iIiiIii - OoOoOO00
I1iI1ii1II = base64 . decodestring ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20v' )
iiOOooooO0Oo = base64 . decodestring ( 'L3N0b3JhZ2UvZW11bGF0ZWQvMA==' )
O0O0OOOOoo = base64 . decodestring ( 'L2dlbmllLnR4dA==' )
O0oo0oOo = base64 . decodestring ( 'LmFyY2hpdGVjdHMueDEwaG9zdC5jb20vdGVzdC93aC50eHQ=' )
I1I1IiI1 = base64 . decodestring ( 'aHR0cDovL2ZpeGVzLmFyY2hpdGVjdHMueDEwaG9zdC5jb20vZml4ZXMudHh0' )
i111iI1i1iI = base64 . decodestring ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vYXBwcy9hcHBzLnhtbA==' )
i11i11II11i = base64 . decodestring ( 'L2FkZG9ucy9uZXcudHh0' )
IiiI1i111I1i = base64 . decodestring ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vdm9kL3ZvZC5waHA=' )
oo0o0OoOO0o0 = base64 . decodestring ( 'L2FkZG9ucy9pcHR2LnR4dA==' )
IiI1Iii1 = base64 . decodestring ( 'L2FkZG9ucy92aWRlby50eHQ=' )
oOo0 = base64 . decodestring ( 'L2FkZG9ucy9zcG9ydHMudHh0' )
OOO0O00Oo = base64 . decodestring ( 'L2FkZG9ucy9raWRzLnR4dA==' )
i1I1IiI1ii = base64 . decodestring ( 'L2FkZG9ucy9tdXNpYy50eHQ=' )
ooooOoo0OO = base64 . decodestring ( 'L2FkZG9ucy9wcm9ncmFtcy50eHQ=' )
i1i1iiIIiiiII = base64 . decodestring ( 'L2FkZG9ucy94eHgudHh0' )
OOO = base64 . decodestring ( 'L2FkZG9ucy9yZXBvLnR4dA==' )
i1Iii1i1I = base64 . decodestring ( 'L2FkZG9ucy9wYWNrcy50eHQ=' )
OO0O0OO0O0 = base64 . decodestring ( 'L2FkZG9ucy9za2lucy50eHQ=' )
ii = base64 . decodestring ( 'L2FkZG9ucy9hcnQudHh0' )
oOO00Oo = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2dvdGhhbS50eHQ=' )
IIooooo = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2hlbGl4LnR4dA==' )
IIIIiiIiI = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2lzZW5nYXJkLnR4dA==' )
i1ii1ii1II1 = base64 . decodestring ( 'L2FkZG9ucy9SU1MudHh0' )
Ii1ii1IiIII = base64 . decodestring ( 'Q1VOVA==' )
def ii11i1iIII ( name , url , mode , iconimage , fanart , description ) :
 OoO = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 Iiiiii111i1ii = True
 i1i1iII1 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 i1i1iII1 . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 i1i1iII1 . setProperty ( "Fanart_Image" , fanart )
 if mode == 5 :
  Iiiiii111i1ii = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = OoO , listitem = i1i1iII1 , isFolder = False )
 else :
  Iiiiii111i1ii = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = OoO , listitem = i1i1iII1 , isFolder = True )
 return Iiiiii111i1ii
def i111IiI1I ( name , url , mode , iconimage , fanart , description ) :
 OoO = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 Iiiiii111i1ii = True
 i1i1iII1 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 i1i1iII1 . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 i1i1iII1 . setProperty ( "Fanart_Image" , fanart )
 Iiiiii111i1ii = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = OoO , listitem = i1i1iII1 , isFolder = False )
 return Iiiiii111i1ii
 if 78 - 78: OoOO / OoooooooOO . OoOO
 if 50 - 50: IIII . o0oO0 - O0 % OOOo0 . O0oO
o0I1iI111ii111i = OoooO00OoO0 ( )
oo000o = None
oOOo0 = None
IiiiI = None
oo00O00oO = None
iIiIIIi = None
ooo00OOOooO = None
if 17 - 17: O0 + OoooooooOO
if 78 - 78: OoOoOO00 + IIII
try :
 oo000o = urllib . unquote_plus ( o0I1iI111ii111i [ "url" ] )
except :
 pass
try :
 oOOo0 = urllib . unquote_plus ( o0I1iI111ii111i [ "name" ] )
except :
 pass
try :
 oo00O00oO = urllib . unquote_plus ( o0I1iI111ii111i [ "iconimage" ] )
except :
 pass
try :
 IiiiI = int ( o0I1iI111ii111i [ "mode" ] )
except :
 pass
try :
 iIiIIIi = urllib . unquote_plus ( o0I1iI111ii111i [ "fanart" ] )
except :
 pass
try :
 ooo00OOOooO = urllib . unquote_plus ( o0I1iI111ii111i [ "description" ] )
except :
 pass
 if 66 - 66: iIii1I11I1II1
 if 57 - 57: IIII
print str ( II ) + ': ' + str ( oOOoO0 )
print "Mode: " + str ( IiiiI )
print "URL: " + str ( oo000o )
print "Name: " + str ( oOOo0 )
print "IconImage: " + str ( oo00O00oO )
if 41 - 41: iIii1I11I1II1 * oO0o0ooO0 + Oo * OOooOOo % IIII / OoOO0ooOOoo0O
if 63 - 63: i1IIi % i11iIiiIii % OoOoOO00 * OoooooooOO
def III1ii1iII ( content , viewType ) :
 if 40 - 40: Oo
 if content :
  xbmcplugin . setContent ( int ( sys . argv [ 1 ] ) , content )
 if o0oOoO00o . getSetting ( 'auto-view' ) == 'true' :
  xbmc . executebuiltin ( "Container.SetViewMode(%s)" % o0oOoO00o . getSetting ( viewType ) )
  if 47 - 47: I1IiI
  if 65 - 65: O0 + O0oO % o00O0oo * OOOo0 / o0oO0 / I1IiI
if IiiiI == None :
 I11I11i1I ( )
 if 71 - 71: i11iIiiIii / I1IiI . OoOO
elif IiiiI == 1 :
 I11iI ( oo000o )
 if 33 - 33: OoOO
elif IiiiI == 44 :
 oOo00oOoO000 ( oo000o )
 if 39 - 39: Ooo00oOo00o + O0 + o0oO0 * OoOoOO00 % O0 - O0
elif IiiiI == 2 :
 O000OOOOOo ( )
 if 41 - 41: IIII % OOooOOo
elif IiiiI == 3 :
 oO000Oo000 ( )
 if 67 - 67: O0 % O0oO
elif IiiiI == 21 :
 oOOOOo0 ( )
 if 35 - 35: OOOo0 . I1IiI + OoooooooOO % Oo % OoOO0ooOOoo0O
elif IiiiI == 4 :
 oO00O0O0O ( )
 if 39 - 39: o00O0oo
elif IiiiI == 5 :
 IiiiIIiIi1 ( oOOo0 , oo000o , ooo00OOOooO )
 if 60 - 60: OoOO0ooOOoo0O
elif IiiiI == 6 :
 OooO00oO ( oo000o )
 if 62 - 62: O0oO * o0000oOoOoO0o
elif IiiiI == 7 :
 ooOO0OOO00o ( oo000o , oOOo0 )
 if 74 - 74: I1IiI . iIii1I11I1II1
elif IiiiI == 8 :
 Iii1 ( oo000o , oOOo0 )
 if 87 - 87: o0oO0
elif IiiiI == 9 :
 FIXREPOSADDONS ( oo000o )
 if 41 - 41: I1IiI . iIii1I11I1II1 % o0oO0 + O0
elif IiiiI == 10 :
 o00oOOooOOo0o ( )
 if 22 - 22: OOooOOo + Oo . o0oO0 + ii11ii1ii * oO0o0ooO0 . i11iIiiIii
elif IiiiI == 11 :
 ooIi111iII ( oo000o )
 if 90 - 90: OoOO0ooOOoo0O * I1IiI - Oo + OOooOOo
elif IiiiI == 12 :
 iII11II1II ( )
 if 53 - 53: OoooooooOO . OoooooooOO + OOooOOo - oO0o0ooO0 + OoOO0ooOOoo0O
elif IiiiI == 13 :
 i1ii1IIIII ( )
 if 44 - 44: O0oO - IIII
elif IiiiI == 14 :
 II1i ( oo000o )
 if 100 - 100: OoOO . Ooo00oOo00o - o00O0oo + O0 * Ooo00oOo00o
elif IiiiI == 15 :
 ooOO00O00oo ( )
 if 59 - 59: OoOoOO00
elif IiiiI == 16 :
 I1i1i111Ii1I ( oo000o , oOOo0 )
 if 43 - 43: Oo + OoooooooOO
elif IiiiI == 17 :
 oooOoOoOO ( oo000o , oOOo0 )
 if 47 - 47: o0oO0
elif IiiiI == 18 :
 iii1IiiiI1i1 ( )
 if 92 - 92: o0000oOoOoO0o % i11iIiiIii % Oo
elif IiiiI == 19 :
 oo0oO0oOOoo ( oOOo0 , oo000o , ooo00OOOooO )
 if 23 - 23: OoOoOO00 * oO0o0ooO0
elif IiiiI == 40 :
 OOo0oO00ooO00 ( oOOo0 , oo000o , ooo00OOOooO )
 if 80 - 80: O0oO / i11iIiiIii + OoooooooOO
elif IiiiI == 42 :
 O00o0OO0 ( oOOo0 , oo000o , ooo00OOOooO )
 if 38 - 38: ii11ii1ii % o0oO0 + i1IIi * OoooooooOO * OoOO
elif IiiiI == 43 :
 oOOOoo0O0oO ( oOOo0 , oo000o , ooo00OOOooO )
 if 83 - 83: iIii1I11I1II1 - o0oO0 - O0oO / Ooo00oOo00o - O0
elif IiiiI == 20 :
 Ii1I1IIii1II ( oo000o )
 if 81 - 81: o00O0oo - OoOO * ii11ii1ii / O0oO
elif IiiiI == 22 :
 ii1II1II ( oo000o )
 if 21 - 21: Ooo00oOo00o
elif IiiiI == 23 :
 OOooOooo0OOo0 ( oo000o )
 if 63 - 63: o0000oOoOoO0o . O0 * o0000oOoOoO0o + iIii1I11I1II1
elif IiiiI == 24 :
 OOOoOOo0o ( oo000o )
 if 46 - 46: i1IIi + OoOoOO00 * i1IIi - o00O0oo
elif IiiiI == 25 :
 OooOo ( oo000o )
 if 79 - 79: OoOoOO00 - OoOO * ii11ii1ii - I1IiI . ii11ii1ii
elif IiiiI == 26 :
 I1iIiiiI1 ( oo000o )
 if 11 - 11: O0 * I1IiI
elif IiiiI == 27 :
 IiIIII1iiIIi ( oo000o )
 if 37 - 37: I1IiI + O0 . O0 * Oo % O0oO / oO0o0ooO0
elif IiiiI == 28 :
 OO0OOoo0OOO ( oo000o )
 if 18 - 18: OoooooooOO
elif IiiiI == 29 :
 OOo00ooOoO0o ( oo000o )
 if 57 - 57: o0oO0 . I1IiI * OOooOOo - OoooooooOO
elif IiiiI == 30 :
 IIi ( oo000o )
 if 75 - 75: i11iIiiIii / OOooOOo . IIII . i1IIi . i1IIi / o0000oOoOoO0o
elif IiiiI == 31 :
 I11iiI11iiI ( oo000o )
 if 94 - 94: o0oO0 + OOOo0
elif IiiiI == 32 :
 iII ( )
 if 56 - 56: I1IiI % OOooOOo
elif IiiiI == 33 :
 I1I111 ( )
 if 40 - 40: OoOO0ooOOoo0O / IIII
elif IiiiI == 35 :
 O0OooOo0o ( oo000o )
 if 29 - 29: o00O0oo - o00O0oo / o0oO0
elif IiiiI == 34 :
 o0OOOO00O0Oo ( oo000o )
 if 49 - 49: o0000oOoOoO0o + OoOO % Ooo00oOo00o - Oo - O0 - OoooooooOO
elif IiiiI == 36 :
 i1oOo ( oo000o )
 if 4 - 4: OoOoOO00 - OoOO % Oo * i11iIiiIii
elif IiiiI == 37 :
 oOOo0oOo0 ( oo000o )
 if 18 - 18: Oo % O0
elif IiiiI == 38 :
 III1Iiii1I11 ( oo000o )
 if 66 - 66: iIii1I11I1II1 % i11iIiiIii / OOOo0
elif IiiiI == 41 :
 ooOoo ( o0I1iI111ii111i )
 if 47 - 47: ii11ii1ii * OoOO + iIii1I11I1II1 - OoOO / IIII
elif IiiiI == 39 :
 oOo0OOO00Oo ( oo000o )
 if 86 - 86: IIII
elif IiiiI == 45 :
 TEXTS ( )
 if 43 - 43: OOOo0 / oO0o0ooO0 / o0oO0 + iIii1I11I1II1 + OoooooooOO
elif IiiiI == 46 :
 i1IiII ( )
 if 33 - 33: OoOoOO00 - IIII - o0oO0
elif IiiiI == 47 :
 GEVID ( )
 if 92 - 92: Ooo00oOo00o * IIII
elif IiiiI == 48 :
 O0O ( oOOo0 , oo000o , ooo00OOOooO )
 if 92 - 92: OoOO
elif IiiiI == 49 :
 i1I11i1I ( )
 if 7 - 7: oO0o0ooO0
elif IiiiI == 222 :
 OOoooOoO0Oo ( oo000o )
 if 73 - 73: Ooo00oOo00o % ii11ii1ii
elif IiiiI == 333 :
 I1ii1 ( oo000o )
 if 32 - 32: OoOO0ooOOoo0O + oO0o0ooO0 + iIii1I11I1II1 * Oo
 if 62 - 62: i11iIiiIii
elif IiiiI == 1001 :
 iIiI1I1ii1I1 ( )
 if 2 - 2: OOOo0
elif IiiiI == 1005 :
 O0OOO ( )
 if 69 - 69: OoooooooOO / Oo * O0oO
elif IiiiI == 1007 :
 ii1i1iiI ( oo000o )
 if 99 - 99: OoOoOO00 * iIii1I11I1II1 % O0 * OoOO / OoOoOO00 % OoooooooOO
elif IiiiI == 1010 :
 oOOoo0IIIIiI11I ( oo000o )
 if 14 - 14: IIII . IIII % o0oO0
elif IiiiI == 1011 :
 iiiI11iIIi1 ( oo000o )
 if 42 - 42: OOooOOo . OoOO0ooOOoo0O - o0oO0
elif IiiiI == 1030 :
 iIii1I ( )
 if 33 - 33: OoOoOO00 / O0 / IIII - o0000oOoOoO0o - i1IIi
elif IiiiI == 1031 :
 iii11i1 ( oo000o , oo00O00oO )
 if 8 - 8: i11iIiiIii . oO0o0ooO0 / iIii1I11I1II1 / ii11ii1ii / IIII - o00O0oo
elif IiiiI == 1006 :
 Parse . ParseURL ( oo000o )
 if 32 - 32: OOooOOo . i1IIi * Oo
elif IiiiI == 2030 :
 Parse . addonParseURL ( oo000o )
 if 98 - 98: o00O0oo - OoOoOO00 / OOOo0 . OoOO * IIII . o0000oOoOoO0o
elif IiiiI == 2031 :
 Parse . apkParseURL ( oo000o )
 if 25 - 25: i11iIiiIii / I1IiI - O0oO / Ooo00oOo00o . OOooOOo . OOooOOo
elif IiiiI == 1002 :
 IIiI11I1I1i1i ( oo000o )
 if 6 - 6: OoOO . o0000oOoOoO0o
elif IiiiI == 1003 :
 oooo ( oo000o , oo00O00oO )
 if 43 - 43: ii11ii1ii + OOooOOo
elif IiiiI == 1004 :
 O0o0O ( oo000o )
 if 50 - 50: OoOO % i1IIi * O0
elif IiiiI == 1008 :
 oO0ooOOO ( )
 if 4 - 4: iIii1I11I1II1 . i1IIi
elif IiiiI == 1009 :
 M3UPLAY ( oo000o )
 if 63 - 63: iIii1I11I1II1 + IIII % i1IIi / OOOo0 % OoOoOO00
elif IiiiI == 2001 :
 OoOO0o ( oo000o )
 if 60 - 60: OOooOOo . I1IiI % O0oO / OOOo0 / O0
elif IiiiI == 1013 :
 II1i111Ii1i ( )
 if 19 - 19: i11iIiiIii . OOOo0 + OoOoOO00 / OoOO0ooOOoo0O . ii11ii1ii * o0oO0
elif IiiiI == 1014 :
 oo00OoO ( )
 if 59 - 59: iIii1I11I1II1 / ii11ii1ii % o0oO0
elif IiiiI == 1015 :
 iIIi1IIi ( oo000o )
 if 84 - 84: iIii1I11I1II1 / OOOo0 . I1IiI % o0000oOoOoO0o
elif IiiiI == 1016 :
 o00O0OO ( oo000o )
 if 99 - 99: Oo + i11iIiiIii
elif IiiiI == 1023 :
 i1II1 ( )
 if 36 - 36: o00O0oo * O0oO * iIii1I11I1II1 - o0000oOoOoO0o % i11iIiiIii
elif IiiiI == 1024 :
 O00oo ( )
 if 98 - 98: iIii1I11I1II1 - i1IIi + o0oO0 % o0000oOoOoO0o + o0oO0 / OoOO
elif IiiiI == 1025 :
 OoOo0oO0o ( oo000o )
 if 97 - 97: IIII % o0oO0 + OoOoOO00 - IIII % Ooo00oOo00o + o0oO0
elif IiiiI == 4001 :
 iI1 ( )
 if 31 - 31: OOooOOo
elif IiiiI == 4002 :
 i11Iiii ( )
 if 35 - 35: I1IiI + o00O0oo * o0oO0 / I1IiI
elif IiiiI == 4003 :
 OO00Oo ( )
 if 69 - 69: o0oO0 . OoOO0ooOOoo0O - OOOo0
elif IiiiI == 3000 :
 i11i11Ii11Iii ( )
 if 29 - 29: i11iIiiIii . ii11ii1ii / OOOo0 . OoOO0ooOOoo0O + i11iIiiIii
elif IiiiI == 404 :
 iIIi11 ( oOOo0 , oo000o , oo00O00oO )
 if 26 - 26: IIII / o00O0oo - OoooooooOO
elif IiiiI == 7030 :
 oOoOo ( )
 if 9 - 9: OoooooooOO * ii11ii1ii
elif IiiiI == 7021 :
 oo0O0o00 ( oOOo0 )
 if 9 - 9: Oo + oO0o0ooO0
elif IiiiI == 7022 :
 iIi1iIIIiIiI ( oOOo0 )
 if 64 - 64: O0 * OOOo0 / OOOo0
elif IiiiI == 7000 :
 OO0OoOo0OOO ( oOOo0 , oo000o , img )
 if 57 - 57: ii11ii1ii / OoooooooOO % ii11ii1ii . O0 / ii11ii1ii
elif IiiiI == 7050 :
 O00oOoo0OoO0 ( )
 if 63 - 63: IIII + iIii1I11I1II1 + OOOo0 + O0oO
elif IiiiI == 7051 :
 i11i1Ii1 ( oo000o )
 if 72 - 72: Ooo00oOo00o + i11iIiiIii + ii11ii1ii
elif IiiiI == 7060 :
 OO0ooo0o0 ( )
 if 96 - 96: OoOO % i1IIi / OOooOOo
elif IiiiI == 7061 :
 OooO00oOOo0Oo ( oo000o )
 if 13 - 13: OoOoOO00 - Oo % i11iIiiIii + oO0o0ooO0
elif IiiiI == 7063 :
 oO0ooOoO ( oo000o )
 if 88 - 88: O0 . OoOO % OOOo0
elif IiiiI == 7062 :
 i1iiIIIi ( oo000o )
 if 10 - 10: OOOo0 + O0
elif IiiiI == 7064 :
 NATatozcat ( )
 if 75 - 75: O0 % iIii1I11I1II1 / I1IiI % OoOO0ooOOoo0O / IIII
elif IiiiI == 7067 :
 IiOOoo0oO00oo00 ( oo000o )
 if 31 - 31: i11iIiiIii * I1IiI
elif IiiiI == 7066 :
 NATatozA ( oo000o )
 if 69 - 69: i11iIiiIii
elif IiiiI == 7065 :
 O0ii ( oo000o )
 if 61 - 61: O0
elif IiiiI == 7070 :
 i1iI1 ( )
 if 21 - 21: Ooo00oOo00o % iIii1I11I1II1 . Ooo00oOo00o
elif IiiiI == 7071 :
 DIZIlist ( oo000o )
 if 99 - 99: OOooOOo * OoOO0ooOOoo0O % OoOO * OoOO + OoooooooOO
elif IiiiI == 7072 :
 DIZIpull ( oo000o )
 if 82 - 82: o0000oOoOoO0o / I1IiI - OoOO0ooOOoo0O / o0oO0
elif IiiiI == 7073 :
 WATCHDIZI ( oo000o )
 if 50 - 50: OoOO0ooOOoo0O + Ooo00oOo00o . i11iIiiIii + ii11ii1ii + i11iIiiIii
elif IiiiI == 7002 :
 o00ooOoO0 ( )
 if 31 - 31: OoOO * O0oO . I1IiI * o0000oOoOoO0o
elif IiiiI == 7003 :
 o0OooOo ( oo000o )
 if 28 - 28: IIII + OOOo0 - Oo % OoOO0ooOOoo0O . o0000oOoOoO0o + OOOo0
elif IiiiI == 7004 :
 o0O0oo0o ( oo000o )
 if 72 - 72: o00O0oo / Oo / OoOO * I1IiI + OoOO0ooOOoo0O
elif IiiiI == 7020 :
 I1I1O0Oo0 ( oo000o )
 if 58 - 58: OOooOOo % OOOo0 . OOOo0 * Ooo00oOo00o - IIII . OoooooooOO
elif IiiiI == 7001 :
 oo0ooooO ( )
 if 10 - 10: O0oO
elif IiiiI == 7010 :
 IiIii1ii ( oo000o )
 if 48 - 48: oO0o0ooO0 * i1IIi % OoooooooOO * o00O0oo * Ooo00oOo00o
elif IiiiI == 7011 :
 o00O00Oo00O ( oo000o )
 if 7 - 7: oO0o0ooO0 . o00O0oo . oO0o0ooO0 - O0oO
elif IiiiI == 7012 :
 OOoOOOo0Ooo0 ( oo000o )
 if 33 - 33: o0oO0 + OoooooooOO - Ooo00oOo00o / i1IIi / OoooooooOO
elif IiiiI == 7013 :
 cnfTVPlay2 ( oo000o )
elif IiiiI == 7014 :
 CNF_Studio_Indexer . MV_Movies ( oo000o )
elif IiiiI == 7015 :
 CNF_Studio_Indexer . Movie_ByYear ( oo000o )
elif IiiiI == 7016 :
 CNF_Studio_Indexer . Resolve_CNF_Link ( oOOo0 , oo000o , oo00O00oO )
elif IiiiI == 7017 :
 CNF_Studio_Indexer . Search_Movie ( )
elif IiiiI == 7018 :
 iiii ( )
elif IiiiI == 7019 :
 CNF_Studio_Indexer . List_Movies ( oo000o )
elif IiiiI == 7020 :
 CNF_Studio_Indexer . Get_Movie_Page ( oo000o )
elif IiiiI == 7024 :
 CNF_Studio_Indexer . Box_Office ( oo000o )
 if 82 - 82: ii11ii1ii / OoOO0ooOOoo0O - oO0o0ooO0 / Oo * Ooo00oOo00o
elif IiiiI == 8000 :
 o0O0ooOOoO ( )
elif IiiiI == 8001 :
 IiI1 ( )
elif IiiiI == 8002 :
 oo00ooOoo ( )
elif IiiiI == 8003 :
 IiiiI1 ( )
elif IiiiI == 8004 :
 I1I1 ( )
elif IiiiI == 8005 :
 IIIIIIIiI ( )
elif IiiiI == 8006 :
 OO0oOOo0o ( oOOo0 , oo000o )
elif IiiiI == 8030 :
 IIi1I11I1II ( oo000o )
elif IiiiI == 8045 :
 I1IiIIi ( )
elif IiiiI == 8046 :
 IiOOo00 ( oo000o )
elif IiiiI == 8047 :
 III1i1iI1 ( oo000o )
elif IiiiI == 8040 :
 i1iIi1II11 ( )
elif IiiiI == 8041 :
 i1I1II1iIIi11 ( oo000o )
elif IiiiI == 8042 :
 i11i11 ( oo000o )
elif IiiiI == 8043 :
 yt . PlayVideo ( oo000o )
elif IiiiI == 8044 :
 OoOOO ( oo000o )
elif IiiiI == 8060 :
 O0II11i11II ( )
elif IiiiI == 8061 :
 o0OoO000O ( oo000o )
elif IiiiI == 8070 :
 iIi1III1I ( )
elif IiiiI == 8071 :
 oo0oo0OOOOOoO ( oo000o )
elif IiiiI == 8081 :
 IiI1IiI11iII ( )
elif IiiiI == 8062 :
 iI1iii ( oo000o )
elif IiiiI == 8063 :
 II1Iii ( oo000o )
elif IiiiI == 8050 :
 ooO ( )
elif IiiiI == 8051 :
 Ooo0oOooo0 ( oo000o )
elif IiiiI == 8052 :
 iiI1IIIi ( oo000o )
elif IiiiI == 8085 :
 oooo00o0o0o ( )
elif IiiiI == 8086 :
 OOO00oo0ooO ( oo000o )
elif IiiiI == 8087 :
 ooo ( oo000o )
elif IiiiI == 8088 :
 OOOO0oooo ( oo000o , oOOo0 )
elif IiiiI == 9000 :
 Oo0O0O0ooO0O ( )
elif IiiiI == 1111 :
 iIiiIIi1iiII ( )
elif IiiiI == 9001 :
 OOOoOoOooo ( )
elif IiiiI == 9002 :
 IIi1I ( )
elif IiiiI == 9003 :
 IIII1i1 ( )
elif IiiiI == 50 :
 iI1I11iiI1i ( oo000o )
elif IiiiI == 9020 :
 O0o0Ooo ( )
elif IiiiI == 9021 :
 ooOo0O0O0oOO0 ( )
elif IiiiI == 9022 :
 iIiIIi ( )
elif IiiiI == 9023 :
 III1I ( )
elif IiiiI == 9024 :
 OoOOOO ( oo000o )
elif IiiiI == 9030 :
 IiiiI111I ( oo000o )
elif IiiiI == 9031 :
 III1I11i1iIi ( oo000o )
elif IiiiI == 9032 :
 OO0oo0O0OOO0 ( oo000o )
elif IiiiI == 9033 :
 OoOOo ( oo000o )
elif IiiiI == 10000 : O0oo0OO0oOOOo ( )
elif IiiiI == 10001 : o0O0OOOOoOO0 ( )
elif IiiiI == 10002 : Ooo0oo ( )
elif IiiiI == 10003 : I1i1i1 ( )
elif IiiiI == 10004 : O0OoooO0 ( )
elif IiiiI == 10005 : o0ooooO0o0O ( )
elif IiiiI == 10006 : iI1i11II1i ( oo000o )
elif IiiiI == 10007 : I11I1i1iIII1I ( oo000o , oo00O00oO )
elif IiiiI == 10008 : iii1I1i ( )
elif IiiiI == 10009 : IioO0oOOO0Ooo ( )
elif IiiiI == 10010 : oOo0OoOOo0 ( oo000o )
elif IiiiI == 10011 : O0o ( oo000o )
elif IiiiI == 10012 : II11iIIiiiII ( oo000o )
elif IiiiI == 10013 : O0oii111 ( oo000o )
elif IiiiI == 10014 : II1I1I1Ii ( )
elif IiiiI == 10015 : oOIIiIi ( )
elif IiiiI == 10016 : oo00O00Oo ( oo000o )
elif IiiiI == 10017 : I1ii1I1iiii ( )
elif IiiiI == 10018 : O00oOo00o0o ( )
elif IiiiI == 10019 : ooo000ooO0000 ( )
elif IiiiI == 10020 : iiI1I1ii ( )
elif IiiiI == 10021 : iIiii ( )
elif IiiiI == 10022 : OOoO000 ( oo000o )
elif IiiiI == 10023 : IiI11i1IIiiI ( oOOo0 , oo000o )
elif IiiiI == 10024 : o0 ( oo000o )
elif IiiiI == 10025 : i1II ( )
elif IiiiI == 10026 : o00I1 ( )
elif IiiiI == 10027 : II1Iiiiii ( )
elif IiiiI == 10028 : OooO0oo ( )
elif IiiiI == 10029 : O00o0OO0000oo ( )
elif IiiiI == 423 : IIIII ( oo000o )
elif IiiiI == 426 : ii1III11 ( oo000o )
if 55 - 55: OoooooooOO
xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
